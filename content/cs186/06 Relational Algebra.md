# Relational Algebra

**Relational algebra** is a language that represents a logical query plan for translating SQL queries into underlying actions.

- perform operations on sets (the “how”)
- operational description of transformations
- Related to relational calculus (which describes the result of a computation: the “what”) by Codd’s Theorem: everything that can be represented with relational calculus can be equivalently represented in relational algebra

# Operators

## Unary Operators

Unary operators work on a **single relation.** 

- Projection: $\pi$
    - retains only desired columns (vertical)
- Selection: $\sigma$
    - retains only a subset of rows (horizontal)
- Renaming: $\rho$
    - rename attributes and relations

## Binary Operators

Binary operators work on **pairs of relations.** 

- Union: $\cup$
    - Or operator: either in r1 or r2
    - Equivalent to `UNION` in SQL (doesn’t keep duplicates: `UNION ALL` does)
- Set difference:  $-$
    - Tuples in r1, but not in r2
    - Equivalent to `EXCEPT` in SQL
- Cross product: $\times$
    - Joins r1 with all r2

The schemas for both relations must be identical for union and set difference.

## Compound Operators

Compound operators are macros (shorthand) for several unary or binary operators together.

- Intersection: $\cap$
    - And operator: both in r1 and r2
- Joins: $\bowtie$, $\Join_\theta$
    - Combine relations that satisfy predicates (combination of cross product, selection)
    - Theta join ($\Join_{\theta}$): join on any logical expression $\theta$
    - Natural join ($\Join$): equi-join on all matching column names
        - $R \Join S = \pi_{unique cols} \sigma_{matching cols equal}(R \times S)$

## Extended Relational Algebra

- Group by: $\gamma$
    - Usage: $\gamma_{age, AVG(rating),COUNT(*)>2}(S)$ = `GROUP BY age, AVG(rating) HAVING COUNT(*)>2`

## Examples

$\pi_{sname,age}(S)$: `SELECT sname, age FROM s`

$\sigma_{rating>8}(S)$: `SELECT * FROM s WHERE rating>8`

$\rho(Temp1(1 \to sid1, 4 \to sid2), R \times S)$: combines every tuple in $R$ with every tuple in $S$, then renames the 1st and 4th columns to `sid1` and `sid2` respectively