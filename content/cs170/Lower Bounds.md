---
title: "Lower Bounds"
weight: 210
created: "May 3, 2021 11:33 AM"
---

Typically, when we are considering algorithms we talk about the *upper bounds* of runtime, i.e. how long a function takes to calculate some result.

Now, let's try to prove a lower bound that applies to **any** problem that solves a particular problem.

### Sorting

We know that all comparison sorting algorithms take $\Omega(n \log n)$ time. This is because this is the required number of comparisons needed to find a relation between all numbers in a tree structure.

### NP-complete

The best known lower bound for an NP-complete algorithm is $\Omega(n)$... not particularly helpful. Proving lower bounds is fairly difficult to do. However, it is widely believed that the lower bound for NP-complete algorithms should be $\Omega(n^{\omega(1)})$, i.e. larger than any polynomial.

### Circuit Complexity

**Problem:** what size circuit is needed to solve a problem of input size $n$?

More formally, a circuit is a DAG of AND, OR, and NOT gates, and we are either wanting to find the number of wires or the depth of the circuit.

Currently, we know that there are $2^{2^n}$ number of possible functions on $n$ input bits.

We also know that the number of possible circuits is $2^{c \cdot w \log w}$ where $w$ is the number of wires and $c$ is some constant, because we need to be able to output a certain number of results given the size of the bitstrings.

So,  $2^{c \cdot w \log w} \ge 2^{2^n}$ and thus $cw\log w \ge 2^n$. Most functions will need an exponential number of wires. 

### Cell probe model

**Problem:** How many reads and writes to memory are needed to solve a problem of size $n$?

### Communication Complexity

If processor 1 owns bitstring $X$ and processor 2 owns bitstring $Y$, how many bits do they need to exchange to compute $f(X, Y)$?