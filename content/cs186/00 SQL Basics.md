# SQL Basics

## Relational Terminology

- **Database:** a set of named relations
- **Relation:** a table
    - **Schema:** description (metadata)
        - **Fixed**, with **unique** attribute names and **atomic** types (integers, text, etc.)
    - **Instance:** the set of data that satisfies the schema
        - Often changes, and can contain a multiset of tuples
- **Attribute** (column):  a field
- **Tuple** (row): one record

## SQL Introduction

SQL is a relational database language that consists of two sub-languages:

- **DDL** (data definition language) is used to define and modify the schema
- **DML** (data manipulation language) is used for queries

These languages can be implemented with many algorithms, but the end result must be consistent.                                                                                                   

### Primary Keys

Primary keys are unique and can be used to identify an entry. Many times, adding `PRIMARY KEY (id)` is good enough, but other times, like tracking boat reservations, would need more data (`PRIMARY KEY (sid, bid, day)`) since a boat can be reserved many different times.

### Foreign Keys

Foreign keys reference other tables. Building onto the boat example, the boat ID would be the same as the ID’s in a table of boats, so we could add `FOREIGN KEY (bid) REFERENCES Boats` to the reserves table instead of copying everything over.

![Untitled](SQL%20Basics/Untitled.png)

### Logical Processing Order

SQL Queries are typically processed in the following order:

1. `FROM` (find the table that is being referenced, join if needed)
2. `WHERE` (filters out rows)
3. `GROUP BY` (aggregate)
4. `HAVING` (filters out groups)
5. `SELECT` (choose columns)
6. `ORDER BY` (sort)
7. `LIMIT` (cut off the output)


## Joins

By default, if a join (`SELECT ... FROM a, b...`) is done in SQL, a **cross product** (Cartesian product) is calculated. Every row in table `a` (the left table) is combined with every row in table `b` to create $R_a * R_b$ rows ($R_a$ = number of rows in table `a`)

![Untitled](SQL%20Basics/Untitled%201.png)

### Inner Join

An inner join takes only the rows in which a particular attribute (or list of attributes) can be found in both the left and right tables. 

- For example, an inner join on the `sid` attribute could be written out as `SELECT ... FROM a, b WHERE a.sid = b.sid`.
- Inner join is the **default behavior** for the JOIN operation, which looks like this:
    
    ```sql
    SELECT ...
    FROM a INNER JOIN b
    ON a.sid = b.sid
    ...
    ```
    

### Natural Join

A `NATURAL JOIN` automatically inner joins tables on whichever attributes are shared between the two tables. `SELECT ... FROM a NATURAL JOIN b ...` is completely equivalent to the example in the inner join section above.

### Outer Join

Left outer joins return all matched rows (as in an inner join), AND additionally preserves all unmatched rows from the left table.

- Any non-matching fields will be filled in with null values.

A right outer join is the same as the left outer join, except it preserves unmatched rows from the right table instead.

- Flipping the table order on a left outer join creates an equivalent right outer join.

A full outer join returns all rows, matched or unmatched, from the tables on both sides of the join clause. 

## String Comparisons

Using the `LIKE` operator, we can do the following:

- Match any single character: `_`
- Match zero, one. or multiple characters: `%`
- Example: `WHERE name LIKE 'B_%'` will match all rows with a name starting with a B and are at least 2 characters long

## Unions and Intersections

The `UNION` operator combines two queries (like an OR statement).

The `INTERSECT` operator combines two queries, and discards rows that do not appear in both (like an AND statement).

The `EXCEPT` operator subtracts one query’s results from another.

UNION, INTERSECT, and EXCEPT operate using **set semantics** (distinct elements) and will keep only one of each unique element in the result.

Using UNION ALL, INTERSECT ALL, and EXCEPT ALL will manage **cardinalities** and will add or subtract the number of identical elements accordingly.

- UNION ALL = sum of cardinalities
- INTERSECT ALL = minimum of cardinalities
- EXCEPT ALL = difference of cardinalities

## Nested Queries

The  `IN` operator allows subqueries to be made. For example, we can `SELECT ... FROM ... WHERE id IN (SELECT .....)`

- The `EXISTS` keyword can be used in place of `IN` to make **correlated subqueries** where the table in the subquery interacts with the outer query.
- `ANY` and `ALL` can be used as well: `SELECT * FROM a WHERE a.value > ANY (subquery...)` would only keep rows in `a` that are bigger than the smallest value in the subquery.
- `ALL` can be used to compute an argmax: for example, if we want a sailor with the highest rating, we can `SELECT * FROM s WHERE s.rating >= ALL(SELECT s2.rating FROM s s2)`

## Views

A view is a **named query.** It can be thought of as a temporary table that can be accessed in future queries to make development simpler.  Unlike tables, it is not computed immediately, and results are cached when they are needed.

```sql
CREATE VIEW name
AS SELECT ...
```

A “view on the fly” can also be created using the `WITH` keyword:

```sql
WITH name(col1, col2) AS
(SELECT ...), 
name2(col1, col2) AS (SELECT ...),
SELECT ...k
```
