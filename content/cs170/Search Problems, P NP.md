---
title: "Search Problems, P/NP"
weight: 180
created: "April 7, 2021 1:18 PM"
---

# Intro to Search Problems

## Definitions

A **binary relation** is a subset of pairs of finite bit strings, where $(x,w)$ is a (instance, witness) relationship. Remember that any data structure can be represented as a bit string, since it can be programmed into a computer.

The **decision problem** `decide(R)` takes an input instance $x$, and determines if there exists a witness $w$ such that $(x, w) \in R$, i.e. does there exist a solution to the problem?

The **search problem** `search(R)` ****takes an input instance $x$ and finds a witness $w$ to solve the problem.

## Examples

As an example of a search problem, **max flow:**

- **The instance** $x = (G, s, t)$ where $G$ is the network graph, $s$ is a source, and $t$ is a sink.
- The **witness** is the max flow of the graph.
- The **decision problem** is trivial: there always exists a max flow of any graph $G$.
- The **search problem** solves for $w$. One example of a search algorithm for max-flow is Ford Fulkerson.

As an example of a problem where `decide(R)` does not exist: the **halting problem.** (It is undecidable whether or not a program halts in finite time: there is no possible witness.)

# P and NP

P and NP are classes of relations.

**P** is the complexity class of all relations $R$ such that `decide(R)` takes polynomial time with respect to the size of the input $x$.

- P stands for "polynomial".

**NP** is the class of all relations $R$ such that if we are given a possible solution to $R$ (i.e. $\exists w, R(x, w) = 1)$ then we can verify that it is indeed a solution in polynomial time.

- NP stands for "non-determinstic polynomial time".

**P is a subset of NP.** (if we can solve in poly time, we can always verify in polynomial time also)

It is common belief that $P \ne NP$, but it has never been proven. (If they are equal, then that means we can solve anything in polynomial time.)

### NP-hard and NP-complete

A problem $A$ is **NP-hard** if all problems $B$ in $NP$ can reduce into $A$.

A problem $A$ is **NP-complete** if $A$ is NP-hard **and** $A$ is in NP.

**An NP-hard problem does NOT have to be NP-complete, and vice versa.** 

![[/cs170/img/Search-Problems-P-NP/Untitled.png]]

# CSAT: NP-Complete Reductions

CSAT, or "circuit satisfiability" , is a binary relation that takes in a circuit as an input and evaluates the circuit to see if it is possible to make the output true.

**Claim:** CSAT is NP-complete. (both NP and NP-hard)

- **CSAT is in NP:** if we're given a solution, we can simply run it through the circuit which is an efficient process.
- **CSAT is NP-hard:** Everything in NP can be reduced to CSAT. This is because it is possible to create a circuit to evaluate any problem, so we can preprocess an algorithm into a circuit and run it through the CSAT verifier which is NP.

## Reducing CSAT to 3SAT

Recall that SAT (the satisfiability problem) is a simpler boolean algebra problem that outputs True if it is possible to satisfy a particular expression of AND, OR, and NOT operations.

Since there is a one to one correspondence between a circuit and boolean algebra, we can simply convert the logic gates into $\land, \lor, \lnot$ operations.

![[/cs170/img/Search-Problems-P-NP/Untitled 1.png]]

SAT can then be reduced into the 3SAT problem, which is the SAT problem with at most 3 variables per clause.

The trick to convert an arbitrary amount of variables into a list of 3-variable clauses is to introduce new variables $y_1, \cdots, y_{k-3}$ such that if the original statement is $(a_1 \lor a_2 \cdots \lor a_k)$, then this statement is equivalent to $(a_1 \lor a_2 \lor y_1) \land (\lnot y_1 \lor a_3 \lor y_2) \land (\lnot y_2 \lor a_4 \lor y_3) \cdots$

We have shown that for any NP problem, we can reduce as follows:

NP problem → CSAT → SAT → 3SAT

## Applications of 3SAT

![[/cs170/img/Search-Problems-P-NP/Untitled 2.png]]

### Independent Set Problem

**Problem:** Determine if a graph $G$ has $g$ or more unconnected vertices.

**Transform to 3SAT:**

- Label each vertex a variable (e.g. $x$ or $\lnot x$).
- Group up sets of 3 vertices into **cliques.** These are the 3SAT clauses.
- In every clique, connect all literals to their negations (to encode the fact that only one can be true).

![[/cs170/img/Search-Problems-P-NP/Untitled 3.png]]

If there is an independent set with size equal to the number of clauses, then the 3SAT problem should return true.

Otherwise, if the expression is not satisfiable, then we cannot find such an independent set.

We can transform the independent set problem to **vertex cover:**

**Problem**: Find a subset of vertices $S \subseteq V$ that touch every edge in the graph.

**Transformation:** There exists a vertex cover of size $k$ if and only if there exists an independent set of size $|V| - k$.

We can also solve the **clique problem:**

**Problem:** Find a subset $S \subseteq V$ that is fully connected (all vertices connected to every other vertex in the set with one edge).

**Transformation:** $S$ is an clique if and only if $S$ is an independent set in the graph $(V, \bar{E})$ which contains all of the edges *not* in $E$.

### 3D Matching

**Problem:** Given sets $\{d_0, \cdots, d_k\}$, $\{c_0, \cdots, c_k\}$, $\{b_0, \cdots, b_k\}$, is there a set of triples ($d_i, c_j, b_k$) such that every element appears exactly once?

**Solution:** This can be solved if we represent each triple as a set of literals (such as $(x, y, \lnot z)$) such that every literal appears exactly twice $(x, \lnot x)$. This allows the problem to be reduced to 3SAT since we can always cover the solution space with a set of "true" triples and "false" triples.

![[/cs170/img/Search-Problems-P-NP/Untitled 4.png]]

If a literal appears more than once, then it can be split by adding new variables and combining them with an AND.

If a literal appears less than twice, then there are not enough triples to cover all of the variables.

### Zero-one Equations (ZOE)

**Problem:** Solve, if possible, the matrix equation $Ax = 1$, where every element in the matrix is either $0$ or $1$.

**Solution:** Represent ZOE as 3D matching by mapping $A$ such that:

- Each column in $A$ represents one triple.
- Each row in $A$ represents one variable.
- An element $A_{ij}$ is equal to $1$ if variable $i$ is in triple $j$, $0$ otherwise.

### Integer Linear Programming (ILP)

**Problem:** Same as linear programming, except that all values must be integers.

**Solution:** We need to convert $Ax = 1$ into an inequality by finding $Ax \le 1$ and $-Ax \le -1$. This will give us a system of inequalities that can represent an ILP problem.

### Rudrata-Hamiltonian Cycle (RHC)

**Problem:** Find a cycle in a graph $G$ that visits each vertex exactly once.

**Solution:**

First, we can reduce ZOE to RHC with paired edges (limited to using either $e_i$ or $e_i'$ in a given set of edge pairs $C = \{(e_i, e_i')\}$)

We can build a paired-edges graph from a ZOE matrix as follows:

![[/cs170/img/Search-Problems-P-NP/Untitled 5.png]]

As shown, each cycle chooses a value for each of the variables. By setting up an edge pair set, we can limit the possible solutions by making sure that a variable is either 1 or 0, and never both at the same time.

This can be further reduced to the **traveling salesperson problem** (find shortest cycle visiting each vertex once, i.e. shortest RHC) by observing that the TSP finds the shortest cycle of weight $|V|$ if and only if the same cycle is found for RHC (assuming edge weights are all $1$).

# Coping with NP-Hardness

### A general problem-solving method

Let's say we are interested in solving a task $A$. Here's a method we can use to find a solution:

1. Try to show that $A \in P$. If it is, then we can figure out a way to reduce $A$ to a commonly known problem (like shortest path, max flow, LP, etc.) or solve it directly.
2. If this is not possible, try to show that $A$ is in NP-hard. If it is, then we have some solutions:
    - Find a special case of $A$ that is in $P$ and solve those. (Sometimes, NP-hardness is only produced by strange edge cases.)
    - Use intelligent exponential search such as backtracking, branch and bound, etc. (mitigating the exponential)
    - Use an approximation algorithm (find an incorrect answer, but not by much)
    - Use heuristics (find inputs of interest using intuition)
    

## Approximation Algorithms for Optimization Problems

An **optimization problem** is any problem where we're trying to find the max or min of a set of values. (For example: max independent set, smallest weight tour, etc.)

Rather than finding the exact solution (which could take exponential time), we can instead reformulate our goal to **design an efficient NP-complete algorithm with as small of an approximation ratio as possible.**

(The approximation ratio is the ratio between the actual optimal value and the optimal value found by the algorithm. $\alpha(A) = 1$ means the algorithm finds the exact result.

Not all algorithms can be approximated: for example, TSP cannot be approximated with any polynomial ratio (otherwise P = NP).

### Example: Vertex Cover

**Problem:** Given an undirected graph $G$, minimize the size of the vertex cover $S \subseteq |V|$, i.e. $\min(|S|)$.

A **vertex cover** is a set of vertices $S$ such that every edge in the graph has an endpoint in $S$. 

Vertex cover is NP-hard because it reduces to the independent set problem ($S$ is a vertex cover if and only if $V \setminus S$ is an independent set.

Here's an approximation algorithm for vertex cover:

1. Find a maximal matching $M$ in $G$.
2. Output the vertex cover of the maximal matching. 
    - We know that the maximal matching has a vertex cover of size $2 |M|$ because by definition of a matching, every edge is connected to two unique vertices.
    - A maximal matching is a matching such that we cannot add any more edges without making it no longer a matching.

This approximation algorithm ahs an approximation ratio of $2$ because in the best case, the maximal matching contains all edges in $G$. In this case, we would only need $|M|$ number of vertices (one for each edge), but the algorithm would output $2 |M|$ size set cover.

## Heuristics

One big idea of heuristics (rather than choosing inputs at random) is to use **gradient ascent:** for $M$ iterations, pick a random point close by to the current value. Then, choose the best result out of those $M$ points and move to that input next.

We can improve gradient ascent using **simulated annealing**: with some probability, move to a worse option so that we don't get stuck at local maxima.

One way to implement this idea is with a **temperature schedule:** the probability of moving to a worse option decays exponentially ('cooling down') since we are less sure of the answer earlier in the algorithm.