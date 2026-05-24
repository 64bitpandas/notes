---
title: "Network Flow"
weight: 140
created: "March 9, 2021 9:16 AM"
---

# What is Flow?

Suppose we have a directed graph with a source $s$ and sink $v$. Each edge has a positive capacity $c > 0$.

A (feasible) flow is a function that maps edges to real numbers $f: E \to \mathbb{R}$ that satisfies:

- **Capacity constraints:** $\forall e \in E$, $0 \le f(e) \le c(e)$. Each edge can only have a particular capacity (think pipes).
- **Conservation constraints:** $\forall u \in V \setminus \{s, t\}$, $\sum f(w, u) = \sum f(u, v)$. The amount of flow that enters a particular vertex is the same amount that leaves that vertex.

The **value** of a flow is the amount that leaves the source. This should equal the amount that enters the sink if the flow is feasible.

![[/cs170/img/Network-Flow/Untitled.png]]

# Optimizing Network Flow

One common problem is to try and find the maximum feasible flow in a graph. In other words, we'd like to find the max value.

We can do this by realizing that **network flow reduces to a linear programming problem.**

- **Proof:**
    
    Let the variables be the set of all $f(e)$ for $e \in E$.
    
    There are $O(|E| + |V|)$ linear constraints:
    
    - For each edge, we have to observe capacity constraints.
    - For each vertex, we have to observe conservation constraints.
    
    Our objective function, the value of $f$, is linear because it's calculated by taking the sum of all edge weights going out of the source.
    

If we can solve max flow using linear programming, then it will take polynomial time (given current algorithms). 

## Making Network Flow Efficient

Polynomial time is nice, but let's see if we can do better!

**Main idea:** For each possible path from source to sink, find the maximum flow through that path only. Enable new paths to cancel existing flow.

We can create a **residual network** to implement this, such that a residual network $G^f$ has:

- Vertices which are the same as the original graph
- Edges such that we only keep the original edges where $f(u, v) < c(u,v)$ or $f(v,u) > 0$.
- Capacities such that for each edge $(u,v)$:
    - If $f(u, v) < c(u, v)$, then the residual capacity is $c(u,v) - f(u,v)$.
    - If $f(v,u) > 0$, then the residual capacity is $f(v, u)$.

**Algorithm:**

1. Initialize a zero flow for all edges.
2. While still possible:
    - Pick any path from $s$ to $t$ in the residual network $G^f$.
    - Increase the flow $f$ by the maximum amount possible on this path.
    - Update the residual graph to reflect this flow.

**Runtime:**

In each iteration, we need to figure out an $(s,t)$ path and update the current flow in the residual graph. This takes $O(|V| + |E|) = O(|E|)$ time (since there are fewer vertices than edges).

In terms of the number of iterations, we can't know for sure but it is possible to put a bound on it. We can observe that:

- Values are always integers.
- The value at iteration $i$ is strictly greater than the value at iteration $i-1$.
- Therefore, we increase the value by at least 1 every iteration, and it cannot go beyond the maximum flow.

Given these observations, the number of iterations is upper bounded by the maximum flow, which is upper bounded by $c \cdot |E|$.

This is the **Ford-Fulkerson algorithm** which runs in $O(|E| \cdot val(f_{max})) = O(c \cdot |E|^2)$. This is only *weakly polynomial time* because it relies on the capacities, which could be arbitrarily large.

As an improvement, we can choose $(s,t)$ paths according to BFS, taking the fewest edge paths. This bounds the number of iterations to $O(|V| \cdot |E|)$. This is known as the **Edmonds-Karp algorithm** which runs in $O(|E|^2 \cdot |V|)$ time.

# Cut Bound Flows

A $(s, t)$ cut in a graph is a pair $(L, R)$ such that $s \in L, t \in R, L \cup R = V, L \cap R = \emptyset$. In other words, this is a cut in the graph.

Define the capacity of a cut $(L, R)$ to be the amount of flow that exits $L$ and enters $R$.

![[/cs170/img/Network-Flow/Untitled 1.png]]

**Observation:** The minimum cut (i.e. the one with the smallest capacity) always produces the max flow; this is known as the **max-flow min-cut theorem.**

Minimum cuts:

- Have all edges going from $L$ to $R$ at maximum capacity,
- Have all edges going from $R$ to $L$ having $0$ capacity,
- Have no path from $s$ to $t$ in the residual network (otherwise we could improve the cut).
- Have $s$ in $L$ and $t$ in $R$.