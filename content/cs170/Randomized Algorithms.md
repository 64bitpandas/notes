---
title: "Randomized Algorithms"
weight: 190
created: "April 20, 2021 9:51 AM"
---

## Types of Randomized Algorithms

There are two main classes of random algorithms, Las Vegas algorithms and Monte Carlo algorithms.

**Las Vegas algorithms** are **correct, and probably fast.** 

For example, randomized quicksort (where we choose a random pivot) is guaranteed to return a correct sort regardless of the pivots chosen, but it's possible to choose bad pivots and result in a poor runtime.

**Monte Carlo algorithms** are **fast, and probably correct.**

For example, Karger's algorithm finds the global min cut by randomly finding a large number of random min cuts. While the runtime of this is fast, it is not guaranteed to give the correct min cut every time.

## Proof that random quicksort is O(n log n)

In the worst case, random quicksort could always choose the largest variable, and so $O(n^2)$ runtime is needed.

In the best case, random quicksort chooses the median every time, for a runtime of $O(n\log n)$.

**Why is the expected runtime of random quicksort equal to the best case runtime?**

In quicksort, the runtime $T(n)$ is determined by the number of comparisons needed.

So, $T(n) = \sum_{i<j} X_{ij} = \sum_{i=1}^{n-1} \sum_{j=i+1}^n X_{ij}$ where $X_{ij}$ is equal to $1$ if the $i$th smallest entry needs to be compared to the $j$th smallest entry, otherwise $0$. 

We can determine $X_{ij}$ by noticing that values in quicksort are only compared if: 1) both numbers are in the same subarray, and 2) one of the numbers is the pivot.

Conversely, if the numbers are in the same subarray, they are not compared (ie $X_{ij} = 0$) if the pivot is between the two numbers.

So, out of $j-i+1$ possible pivots to choose, only 2 of them result in $X_{ij} = 1$ so the expected value $E(X_{ij})$ is equal to $\frac{2}{j-i+1}$.

We can plug this in to the original equation to find $E(T(n)) = \sum_{i=1}^{n-1} \sum_{j=i+1}^n  \frac{2}{j-i+1}$ which is upper bounded by the approximation $2 n\log n$.

By Markov's Inequality, the probability that the runtime of any particular choice of pivots exceeds $200 n\log n$ is 1%, so it is safe to say that the vast majority of random pivot choices will result in a good runtime.

## Freivald's Algorithm

Here's an example of a Monte Carlo algorithm.

**Problem:** Given three $n \times n$ matrices $A,B,C$, test whether $C = AB$ without actually multiplying the matrices.

**Intuition:** For a random vector $x$, it is likely that if $Cx \ne ABx$, then $C \ne AB$. Vector multiplication only takes $O(n^2)$ time to compute, so it is more efficient than full matrix multiplication. If we choose enough random vectors, then the probability of there being a false positive will be extremely low.

## Karger's Algorithm

Here is another example of Monte Carlo.

**Problem:** Find the global min cut of a graph (such that the cut selects a set of edges with the smallest edge weight that splits the graph into two unconnected sets).

This can already be done with running Ford-Fulkerson on each vertex, but randomizing can help us get a better runtime.

**Algorithm:**

Define a `contract(e)` function that replaces two vertices `(u,v)` with a single vertex `UV`, removes the edge connecting them, and consolidate all edges connected to `u` or `v` such that they are all now connected to `UV`.

Until 2 vertices are remaining, contract a random edge. Then, return the cut between the two remaining vertices. Repeat this N times.

The probability of choosing a correct min cut in any single run is about $\frac{1}{n(n-1)}$ since we have to not choose an edge in the global min cut every time.