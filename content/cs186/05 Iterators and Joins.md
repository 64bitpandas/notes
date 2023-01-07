# Iterators and Joins

## Cost Notation

Used to analyze the size of a database.

$R$ is a table.

$[R]$ is the number of pages needed to store $R$

$p_R$ is the number of records per page of $R$.

$|R|$ is the cardinality of $R$, or the number of records.

- $|R| = p_R \times [R]$

## Simple Join

Intuitively, joining two tables is essentially a double for loop over the records in each table:

```python
for record r in R:
	for record s in S:
		if join_condition(r, s):
			add <r, s> to result buffer
```

where `join_condition` is an optional function, also known as $\theta$, that returns a boolean (true if record should be added to result).

The cost of a simple join is the cost of scanning $R$ once, added to the cost of scanning $S$ once per tuple in $R$:

$[R] + |R|[S]$

## Page Nested Loop Join

Simple join is inefficient because it requires an I/O for every individual record for both tables.

We can improve this by operating on the page level rather than the record level: before moving onto the next page, process all of the joins for the records on the current page.

```python
for rpage in R:
	for spage in S:
			for rtuple in rpage:
					for stuple in spage:
						if join_condition(rtuple, stuple):
							add <r, s> to result buffer
```

Now, the cost becomes the cost of scanning $R$ once, then scanning $S$ once per *page* of $R$:

$[R] + ([R] \times [S])$

## Block Nested Loop Join

To improve upon loop join even further, let’s take advantage of the fact that we can have $B$ pages in our buffer.

Rather than having to load in one page at a time, we can instead load in:

- $1$ page of $S$
- $1$ output buffer
- $B-2$ pages of $R$

and then load in each page of $S$ one by one to join to all $B-2$ pages of $R$ before loading in a new set of $B-2$ pages.

```python
for rblock of B-2 pages in R:
	for spage in S:
		for rtuple in rblock:
			for stuple in sblock:
				add <rtuple, stuple> to result buffer
```

The cost now becomes the cost of scanning $R$ once, plus scanning $S$ once per number of blocks:

$[R] + \lceil [R] / (B-2) \rceil \times [S]$ 

## Index Nested Loop Join

In previous version of nested loop join, we’d need to loop through all of the elements in order to join them. 

However, with the power of B+ trees, we can quickly look up tuples that are equivalent in the two tables when computing an equijoin.

```python
for r_row in R:
	for 
```

Cost: $[R] + |R| \times t_S$ where $t_S$ is the cost of finding all matching $S$ tuples

- Alternative 1 B+Tree: cost to traverse root to leave and read all leaves with matching utples
- Alternative 2/3 B+Tree: cost of retrieving RIDs + cost to fetch actual records
    - If clustered, 1 IO per page. If not clustered, 1 IO per tuple.
- If no index, then $t_S = |S|$ which devolves INLJ into SNLJ.

## Sort-Merge Join

**Main idea:** When joining on a comparison (like equality or $<$), sort on the desired indices first, then for every range (group of values with identical indices) check for matches and yield all matches.

![Untitled](Iterators%20and%20Joins/Untitled.png)

The cost of sort-merge join is the sum of:

- The cost of sorting $R$
- The cost of sorting $S$
- The cost of iterating through R once, $[R]$
- The cost of iterating through S once, $[S]$

One optimization we can make is to stream both relations directly into the merge part when in the last pass of sorting! This will reduce the IO cost by removing the need to re-read $[R] + [S]$.

- Subtract $2 \times ([R] + [S])$ IOs

## Hash Join

If we have an equality predicate, we can use the power of hashing to match identical indices quickly.

Naively, if we load all records in table $R$ into a hash table, we can scan $S$ once and probe the hash table for matches.

- This requires $R$ to be less than $(B-2) \times H$ where $H$ is the hash fill factor.

## Grace Hash Join

If the memory requirement of $R < (B-2) * H$ is not satisfied, we will have to partition out $R$ and process each group separately.

Essentially, Grace Hash Join is very similar to the divide-and-conquer approach for hashing in the first place:

![Untitled](Iterators%20and%20Joins/Untitled%201.png)

- In the dividing phase, matching tuples between $R$ and $S$ get put into the same partition.
- In the conquering phase, build a separate small hash table for each partition in memory, and if it matches, stream the partition into the output buffer.

Full process:

1. Partitioning step: make $B-1$ partitions.
2. If any partitions are larger than $B-2$ pages, then recursively partition until they reach the desired size.
3. **Build and probe:** 
    1. Build an in-memory hash table of one table $R$, and stream in tuples of $S$.
    2. For all matching tuples of $R$ and $S$, stream them to the output buffer.