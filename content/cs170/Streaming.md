---
title: "Streaming"
weight: 200
created: "April 22, 2021 10:57 AM"
---

# Streaming Algorithms

In applications like the internet, we might have vast amounts of data "streaming" by. How do we quickly store and update this data via approximation?

## Examples of Streaming Algorithms

### Morris's Algorithm for Approximate Counting

**Problem:** Suppose we were counting total sales. Given an input of $n$ sales with prices $p_1, \cdots, p_n$, output the total $p = \sum_{i=1}^n p_i$.

**Solution:** Initialize a running counter $X$.  With probability $\frac{1}{2^X}$, increment $X$ by $1$. Then, return $\tilde{n} = 2^X - 1$.

This takes an exponentially fewer number of bits when compared to the normal representation of $n$. ($\log \log n$ number of bits)

### Flajolet-Muller (FM) Algorithm

**Problem:** Given a stream $i_1, \cdots, i_m$ with each element in the set $\{1, \cdots, n\}$, count the distinct number of elements in the stream.

**Idealized solution:** We can use real numbers (which don't actually exist in computers) to initially propose a solution. 

Every time a new number appears, we pick a random function $h(i)$ that returns a random number uniformly distributed in $[0, 1]$.

We first initialize a counter $X=1$. Then, when a number appears, we update $X$ to be the minimum of $X, h(i)$.

Finally, we return $\frac{1}{X} - 1$.

The intuition as to why this works is that if we pick $t$ random numbers, we would expect the average gap between them to be $\frac{1}{t} - 1$. 

**Practical solution:** Pick a random number between 1 and $B$, then divide by $B$ at the last step. Additionally, keeping multiple estimates and taking the average decrease variance.