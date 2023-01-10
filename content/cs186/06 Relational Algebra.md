---
title: "Relational Algebra"
weight: 60
---

## Introduction

**Relational algebra** is a language that represents a logical query plan for translating SQL queries into underlying actions. This is useful because SQL queries don't save information for the *order* in which operations are carried out. As you'll see, several different ways of processing the same query could lead to the same result.

It represents *how* we perform operations on sets to achieve the desired result. In contrast, [relational calculus](https://en.wikipedia.org/wiki/Relational_calculus) represents the result (the *what* of a calculation). We won't cover relational calculus in this class, since everything that can be represented with relational calculus can be equivalently represented in relational algebra.

## Relevant Materials
 - [Note 9](https://notes.bencuan.me/cs186/coursenotes/n09-RelAlg.pdf)
 - [Discussion 6](https://docs.google.com/presentation/d/1qMc6ihzx2xA0wUhn5Ahgb53MXsT6A6P6igzcftze1y8/edit)

## Operators

### Unary Operators

Unary operators work on a **single relation.** 

- **Projection**: $\pi$ (pi)
    - Retains only desired columns (vertical)
    - Example: `SELECT name FROM R` becomes $\pi_{name}(R)$
- **Selection**: $\sigma$ (sigma)
    - Retains only a subset of rows (horizontal)
    - Example: `SELECT * FROM R WHERE id = 100` becomes $\sigma_{id=100}(R)$
- **Renaming**: $\rho$ (rho)
    - rename attributes and relations
    - Example: $\rho((1 \to sid1, 4 \to sid2), S)$ renames the 1st and 4th columns to `sid1` and `sid2` respectively

### Binary Operators

Binary operators work on **pairs of relations.** 

- Union: $\cup$
    - Or operator: either in r1 or r2
    - Equivalent to `UNION` in SQL (doesn’t keep duplicates: `UNION ALL` does)
- Set difference:  $-$
    - Tuples in r1, but not in r2
    - Equivalent to `EXCEPT` in SQL
- Cross product: $\times$
    - Joins r1 with all r2
    - Equivalent to `FROM r1, r2...` in SQL

The schemas for both relations must be identical for union and set difference.

### Compound Operators

Compound operators are macros (shorthand) for several unary or binary operators together.

- Intersection: $\cap$
    - And operator: both in r1 and r2
- Joins: $\bowtie$, $\Join_\theta$
    - Combine relations that satisfy predicates (combination of cross product, selection)
    - Theta join ($\Join_{\theta}$): join on any logical expression $\theta$
    - Natural join ($\Join$): equi-join on all matching column names
        - $R \Join S = \pi_{unique cols} \sigma_{matching cols equal}(R \times S)$

### Extended Relational Algebra

- Group by: $\gamma$
    - Usage: $\gamma_{age, AVG(rating),COUNT(*)>2}(S)$ = `GROUP BY age, AVG(rating) HAVING COUNT(*)>2`

## Converting SQL to Relational Algebra

Here's my process for converting between SQL queries and Relational Algebra!

First, recall the SQL Logical Processing Order:
1. `FROM` (find the table that is being referenced, join if needed)
2. `WHERE` (filters out rows)
3. `GROUP BY` (aggregate)
4. `HAVING` (filters out groups)
5. `SELECT` (choose columns)
6. `ORDER BY` (sort)
7. `LIMIT` (cut off the output)

The key is to go through the query in this order, and build a relational algebra statement inside out.

Here's a nonsensical example query:
```sql
SELECT a.name, b.capital
FROM countries AS a, countries AS b
WHERE a.name = b.capital
GROUP BY continent
```

The logical processing order for this would be:
1. Join the `countries` table with itself
2. Filter for rows where `a.name = b.capital`
3. Group by continent
4. Filter for columns `name` and `capital`

Building it would look like this:
1. $\rho_a countries \times \rho_b countries$ (FROM)
2. $\sigma_{a.name = b.capital}(\rho_a countries \times \rho_b countries)$ (WHERE)
3. $\gamma_{continent}(\sigma_{a.name = b.capital}(\rho_a countries \times \rho_b countries))$ (GROUP BY)
4. $\pi_{a.name, b.capital}(\gamma_{continent}(\sigma_{a.name = b.capital}(\rho_a countries \times \rho_b countries)))$ (SELECT)



