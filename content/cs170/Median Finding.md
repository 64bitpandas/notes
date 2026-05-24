---
title: "Median Finding"
weight: 50
created: "January 26, 2021 9:11 AM"
---

**Problem:** Given a set $S=\{a_1, \cdots, a_n\}$, find the median $a \in S$  such that half of the values in $S$ are greater than $a$ and the other half is less than $a$.

The median is less sensitive to outliers than the mean. 

## Finding the Median

### A naive solution

One method of finding the median is simply sorting the list, then getting the middle element. This requires $n\log(n)$ comparisons (see [[03 Sorting]] for more information). 

### A Divide and Conquer solution

We can realize that all of the numbers above and below the median *do not matter*, so if we don't have to sort them then we might be able to get a better runtime.

We can use divide and conquer to solve a harder problem (analogous to strong induction). This problem is **selection:** given a set of numbers $S$ and an index $k$, output the $k$th smallest element in $S$.

**The main idea:** Pick an $a \in S$ and split $S$ into three lists: 

- $S_l$ for elements less than $a$
- $S_a$ for elements equal to $a$
- $S_r$ for elements greater than $a$

We can split $S$ into these three lists using linear time ($n$ number of comparisons).

Then:

- If $k \le |S_l|$, the element must be in $S_l$ so we can re-run the algorithm only on $S_l$.
- If $k > |S_l| + |S_a|$, then the element must be in $S_r$ so we can re-run the algorithm only on $S_r$.
- Otherwise, $k$ must be in $S_a$ so return $a$.

**Runtime:** 

The runtime depends on which $a$ is selected. 

**Bad case:** If $a$ is always the largest or smallest element, then the problem size only decreases by $1$ every iteration. This results in a runtime of $O(n) + O(n-1) + \cdots = O(n^2)$.

**Good case:** If $a$ always splits $S$ in half, then we get the recurrence relation $T(n) = 1 \cdot T(n/2) + O(n) = O(n)$.

**The Problem:** guaranteeing the good case *requires* finding the median!

**The Solution:** pick $a$ at random. 

- Yes, this doesn't *guarantee* a good case all the time... but what if we relax the notion of 'good' to make it probable?
- Suppose we say $a$ is 'good' if it's between the 25th and 75th percentiles. This means that the size of $S$ is reduced to at least $\frac{3}{4}$ size per iteration.
- There is a 50% chance that $a$ is 'good', so the expectation of the number of attempts to get a good $a$ at random should be $2$.
- It takes $O(n)$ time to determine if $a$ is good (check against other elements in list), so finding $a$ takes an expected $2 \cdot O(n)$ time.
- Therefore, $\mathbb{E}T(n) \le \mathbb{E}T(\frac{3}{4} \cdot n) + 2 O(n)$ and thus by the Master Theorem, this is $O(n)$.