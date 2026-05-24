---
title: "Horn Formulas"
weight: 110
created: "February 23, 2021 10:04 AM"
---

# Horn Formulas

## The Problem: Boolean Expressions

Suppose we have a boolean expression such as $(w \lor y \lor z) \land (y \implies w) \lor (\lnot u \land \lnot v \land \lnot z)$ and so on. 

We'd like to answer the question: are there any values of boolean variables that make this statement true?

In the general case, this problem is NP-hard...

## A Special Case

There are some special cases, though, that can be solved with a greedy algorithm. These are called **Horn clauses:**

1. $(z \land w) \implies u$
2. $\implies x$ (x is true)
3. $(\lnot u \lor \lnot v \lor \lnot y)$

## Solving the Special Case

Suppose we have a collection of Horn clauses. We can use the following algorithm to calculate the answer:

- Set all variables to false. This satisfies 3 and 1, but not 2.
- While an implication is not satisfied:
    - Set the variable(s) in question in clause 2 to true.
    - If all negative clauses are still satisfied, then we're done!
    - If not, then it's not satisfiable.