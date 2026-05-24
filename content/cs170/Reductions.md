---
title: "Reductions"
weight: 170
created: "April 1, 2021 9:12 AM"
---

## Introduction

The strategy of reduction is to reduce a particular Problem A into another Problem B using a subroutine. We can then use Problem B to solve Problem A.

**Good news:** If Problem B is efficient, then this provides a fast algorithm for Problem A.

**Bad news:** If Problem A is hard, Problem B must be hard too.

**Step by Step:**

1. Preprocess - turn the input of A into an input for B.
2. Run Problem B.
3. Postprocess - convert the output of B into the output of A.

We can use reduction to:

- Reduce bipartite matching to max flow
- Reduce any polynomial time to linear programing
- Reduce matrix version to matrix multiplication

## Bipartite Matching

**Problem:** Given a bipartite graph $G(L, R, E)$ such that two sides $L$ and $R$ are connected with edges $E$, find the maximum number of an edge subset $M \subseteq E$ such that every edge in $M$ touches any vertex at most once. In other words, we'd like to find $\max(|M|)$.

For example, if we're given a set of computers and a set of jobs, and given that each job can only be run on a subset of computers, what is the maximum number of jobs that can be run at one time?

**Solve using Max Flow:**

Some problems to solve in preprocessing:

- Identify the source and destination vertices (S and T)
    
    **Solution:** Create new vertices $s$ and $t$. $s$ connects to all of the vertices in $L$ and $t$ connects to all of the vertices in $R$.
    
- Set capacities of edges $c_e$
    
    **Solution:** Set all capacities to 1 for edges in $E$.
    
- Direct edges
    
    **Solution:** Direct all edges going from $L$ into $R$ (left to right).
    
- Find a connection between $|M|$ and max flow
    
    **Solution:** Think about max flow using the max flow min cut theorem. 
    

## Circuit Value Problem

**Problem:** Given a boolean circuit (A DAG with AND, NOT, and OR operations), 

**Claim:** Any efficient (polynomial time) algorithm can be reduced to the Circuit Value problem, which can be then reduced into linear programming.

**Informal proof:** Polynomial time algorithms can be computed by computers with a polynomial amount of memory and time. We can then capture the logic performed by the computer as a set of logic gates and feed this into the circuit value problem.

**Convert to Linear Programming:**

- Boolean constraint: For all variables, $0 \le x_i \le 1$.
- AND gates: If $x_k = x_i \land x_j$, then $x_k \le x_i, x_k \le x_j, x_k \ge x_i + x_j - 1$.
- OR gates: If $x_k = x_i \lor x_j$, then $x_k \ge x_i$, $x_k \ge x_j$, $x_k \le x_i + x_j$
- NOT gates: If $x_k = \lnot x_i$, then $x_k = 1 - x_i$.

## Matrix Inversion and Multiply

**Claim:** Multiplying and inverting matrices are problems that reduce to each other.

**Multiply → Invert:** Use the typical matrix inversion algorithm (put matrix into upper triangular form using Gaussian elimination). The pre and post processing takes $O(n^2)$ so if inversion takes $O(n^e)$ where $e \ge 2$, then multiplication should also take $O(n^e)$.