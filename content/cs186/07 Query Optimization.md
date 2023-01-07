# Query Optimization

**Query optimization** is the bridge between a declarative language (like SQL, where you describe “what” you want) and an imperative language (like Java, which describes how the answer is actually computed).

## System R Optimizers

![Untitled](Query%20Optimization/Untitled.png)

The query parser first checks for correctness and authorization (user permissions to access the table). It then generates a parse tree out of the query. This step is usually fairly straightforward.

Next, the query rewriter converts queries into smaller query blocks, and flattens the views.

Once the query is rewritten, it gets passed into the query optimizer. The primary goal of a query optimizer is to translate a simple query plan into a better query plan. A cost-based query optimizer processes one query block at a time (e.g. select, project, join, group by, order by). 

- For each block, consider:
    - all relevant access methods
    - All left-deep join trees: right branches are always simple FROM clauses
    
    ![Untitled](Query%20Optimization/Untitled%201.png)
    
- Typically, we don’t care about exact performance; the main purpose of query optimization is to prune out extremely inefficient options.

## The Components of a Query Optimizer

There are three main problems:

1. **Plan space:** for a given query,  what plans are considered?
    1. Two query plans are **physically equivalent** if they result in the same content and the same physical properties (primarily sort order and hash grouping).
2. **Cost estimation:** how do we estimate how much a plan will cost?
    1. In System R, cost is represented as a single number: #IOs + CPU-factor*#tuples (where CPU factor is the proportion of time the system spends actually computing the query). We typically just care about the IO cost. 
    2. For each term, determine its **selectivity** $S$ (size of output / size of input).  Lower selectivity value is better (filters more items).
        1. Result cardinality is equal to the max number of tuples multiplied by the product of all selectivities.
        2. If searching for `col = value`,  $S = 1/N(l)$ where $N(l)$ is the number of unique values in the table.
        3. If searching for `col1 = col2`, then $S = 1/max(N(l_1), N(l_2))$.
        4. If searching for `col > value`, then $S = (max(l) - value) / max(l) - min(l) + 1).$
        5. If we are missing the needed stats to compute any of the above, assume that $S = 1/10$. 
        6. If searching for a disjunction (or) $Q_1 \lor Q_2$, $S = S_1 + S_2 - (S_1 \times S_2)$.
        7. If searching for a conjunction (and) $Q_1 \land Q2$, $S = S_1 \times S_2$.
        8. If searching for a negation (not), $\lnot Q_1$, $S = 1 - S_1$.
        9. For joins, simply apply the selectivity query to the cross product of the two tables that are being joined.
    3. For clustered indexes, the approximate number of IOs is $(P(L) + P(R)) \times S$ where $P$ is the number of pages and $S$ is selectivity.
    4. For unclustered indexes, the approximate cost is $(P(L) + T(R))\times S$ where $T$ is the number of tuples.
    5. A sequential scan of a file takes $N(R)$ cost.
3. **Search strategy:** how do we search the plan space?

## Relational Algebra Equivalences

Selections:

- $\sigma_{c_1 \land \cdots \land c_n}(R) \equiv \sigma_{c_1}(\cdots(\sigma_{c_n}(R))\cdots)$ (cascade)
- $\sigma_{c1}(\sigma_{c2}(R)) \equiv \sigma_{c2}(\sigma_{c1}(R))$ (commutative)

Projections:

- Can also cascade like selections:
    
    ![Untitled](Query%20Optimization/Untitled%202.png)
    
    - Make sure that the table being selected from actually has the desired column to begin with

Cross (Cartesian) products:

- $R \times (S \times T) \equiv (R \times S) \times T$ (associative)
- $R \times S \equiv S \times R$ (commutative)

Joins:

- Are sometimes commutative or associative, but not always (depends on the  join condition)
    - Need to make sure that the same rows are being filtered out at each step
    - Some join orders require cross products, others don’t (cross products less efficient)

## Common Heuristics

**Selection and projection cascade and pushdown:** apply selections ($\sigma$) and projections ($\pi$) as soon as you have the relevant tables. i.e. push them as far to the right as possible

**Avoid Cartesian products:** given a choice, do theta-joins rather than cross products.

**Put the more effective selection onto the outer loop before a join:** reorder joins such that we are joining a smaller table in the outer loop with a larger table in the inner loop, especially if this allows us to filter out more rows in the outer loop

**Materialize inner tables before joins:** rather than calculating selections on the fly, create a temporary filtered table before passing it into a join

- Not effective 100% of the time since it costs IO’s to write and re-read the table

**Use left-deep trees only** (explained in an earlier section).

## Algorithms

**Table access with selections and projections:**

- Heap scan
- Index scan if available

**Equijoins:**

- Block nested loop join when simple algorithm needed
- Index nested loop join if one relation is small and the other one is indexed
- Sort-merge join if equal-size tables, small memory
- Grace hash join if 1 table is small

**Non equijoins:**

- Block nested loop join

## Statistics and Catalogs

In order to perform query optimization we need to store metadata about what we’re referencing.

![Untitled](Query%20Optimization/Untitled%203.png)

Catalogs are updated periodically (since they are just estimations, and we can save computation).

## Selinger Query Optimization

The Selinger query optimization algorithm uses dynamic programming over $n$ passes (where $n$ is the number of relations).

In each of the passes, we use the fact that left-deep plans can differ in the order of relations, access method for leaf operators, and join methods for join operators to enumerate all of the plans.

More specifically:

- In the 1st pass, find the best single relation plan for each relation. (what’s the best way to scan a table?)
    - This includes full scans (# IOs = # pages in table) and index scans (# IOs depends on type of index and any applicable selects, since selections are pushed down)
- In each $i$ith pass, find the best way to join the result of an $i-1$ relation plan to the $i$th relation. (The $i-1$ plan will always be the outer relation due to the left-deep property.)
- For each subset of relations, retain only:
    - Cheapest plan overall for each combination of tables,
    - Cheapest plan for each interesting order of tuples

**The principle of optimality:** the best overall plan is composed of the best decisions on the subplans. This means that if we find the cheapest way to join a subset of tables, we can add on more tables one by one by finding the cheapest cost for that single join operation.

### Interesting Orders

So, what are interesting orders? 

If a GROUP BY or ORDER BY clause will be processed later on, it may be useful to take a temporary hit in IO cost in order to avoid needing to resort or regroup the table in a future step.

## Selectivity Estimation Practice

Suppose $R(a,b,c)$ has 1000 tuples and $S(a)$ has 500 tuples. We have the following indexes:

- R.a: 50 unique integers uniformly distributed in $[1, 50]$
- R.b: 100 unique float values uniformly distributed in $[1, 100]$
- S.a: 25 unique integers uniformly distributed in $[1, 25]$

`SELECT * FROM R`: Full scan requires iterating through every tuple in $R$, so 1000 tuples are outputted.

`SELECT * FROM R WHERE a = 42`:

- The selectivity is $1/50$ since there are 50 unique values in a and exactly one of them is desired.
- $1000 \times 1/50 = 20$ tuples.

`SELECT * FROM R WHERE c = 42`:

- We have no information, so by default $$S=1
- $1000 \times 1/10 = 100$ tuples.

`SELECT * FROM R WHERE a <= 25`:

- Exactly 1/2 of all possible values of `a` are less than 25 (exact formula listed above).
- $1000 \times 1/2 = 500$ tuples.

`SELECT * FROM R WHERE b <= 25`:

- Using the equation for selectivity of inequalities, (value - low) / (high - low) = (25-1)/(100-1) = 24/99.
- $\lfloor 1000 \times 24/99 \rfloor = 242$ tuples.

## Access Plans

Suppose we have 

![Untitled](Query%20Optimization/Untitled%204.png)