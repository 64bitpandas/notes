---
title: "Greedy Algorithms"
weight: 80
created: "February 11, 2021 9:11 AM"
---

## What are greedy algorithms?

Greedy algorithms are a general algorithmic approach:

At every step, choose what to do based on local information without considering the next steps. This works nicely in some cases because of the efficiency of such a concept.

### A simple example

Let's say you have 6 assignments that are due in 1, 1, 2, 2, 4, and 5 hours respectively. Each one takes 1 hour to complete. What is the maximum number you can complete before the deadline?

A greedy algorithm would simply choose to do the one that is due earliest, until we run out of completable assignments. (So, the first, third, fourth, and fifth assignments). We can prove that this is indeed the optimal solution:

- By contradiction, assume that there exists an optimal solution $S$ that is not the greedy solution $G$. We can show that by swapping assignments due at the same time, all elements in $S$ can also be present in $G$ no matter what $S$ is.

## Set Cover

Given $n$ number of points in a set $V$, and a bunch of subsets $S_1, \cdots S_m \subseteq V$ such that the union of the subsets is $V$, find the smallest number of sets that cover $V$.

![[/cs170/img/Greedy-Algorithms/Untitled.png]]

In the example above, we can choose $S_1$ and $S_3$ to cover $V$, so it can be covered in 2 sets.

Another way of thinking about this problem less abstractly is to represent each point as a town, and all sets being nearby towns from a particular town as a center. Our goal might be to build as few schools as possible such that all towns can be serviced.

### Set Cover Greedy Strategy

**Main idea:** At each step, pick the set $S_i$ that covers the most uncovered points.

**More formal algorithm:**

Let $J$ be the empty set. While $S_J \ne V$ such that $S_J = \bigcup_{i \in J} S_i$: 

- Pick $i \not\in J$ with the largest $|S_i \setminus S_J|$.
- Add it to $J$.

**Problem:** This greedy strategy doesn't guarantee an optimal solution! Take this example: 

![[/cs170/img/Greedy-Algorithms/Untitled 1.png]]

With this greedy algorithm, we'd choose $S_1$ first, then all of the other sets, to result in a total $|J|$ of 5. However, we could also have not chosen $S_1$ at all... so $4$ is the optimal result.

Unfortunately, an optimal set cover solution that can be done in polynomial time is not currently known so this is as good as we can hope to get in a reasonable amount of algorithmic complexity.

### A compromise

Rather than finding all the sets, let's try just finding enough such that $n_t$ points remain. 

Supposing we choose one set at each time step $t$, then $n_t \le c^t \times n$ where $c$ is a constant. We need to show that $c < 1$:

- Let $k$ represent the number of sets that cover $V$.
- Taking the log of both sides, $\ln(c^t \times n) < \ln(1) = 0$, so $t \ln(c) + \ln(n) < 0$.
- The above step demonstrates that $t > \frac{\ln(n)}{\ln(1/c)}$.
- $n_t \le n_{t-1} - \frac{n_{t-1}}{k} = (1 - \frac{1}{k})n_{t-1} = c \cdot n_{t-1}$.
    - $n_{t-1}$ points are covered by $k$ sets, so some unchosen set *must* cover at least $n_{t-1}/k$ points!
    - Since the greedy choice is always the largest one, it must be greater than or equal to this amount.
- Plug in $c$ in terms of $k$ to show that $k \ge \frac{1}{\ln(1/c)}$.
- This algorithm runs in $k \ln(n)$ time.

## Exchange Argument

This is a general method of proving that greedy algorithms produce an optimal solution:

1. Start with an output from the greedy algorithm.
2. Exchange items in your output's ordering to create a new, alternative ordering.
3. Prove that the exchange is not optimal. If exchanging any two arbitrary values in the original output creates a less optimal solution, then the original output must be optimal itself.