---
linkTitle: "Minimum Spanning Trees"
BookCollapseSection: true
weight: 30
---

## Spanning Tree Definition

A **spanning tree** $T$ is a subgraph of a graph $G$ where $T$:

* Is connected (there's a path to every vertex)
* Is acyclic (no cycles)
* Includes every vertex (spanning property)

**Notice:** the first two properties defines a tree structure, and the last property makes the tree spanning.

A **minimum spanning tree** is a spanning tree with minimum total edge weight.

Example: I want to connect an entire town with wiring and would like to find the optimal wiring connection that connects everyone but uses the least wire.

## MST vs. Shortest Path Tree

In contrast to a shortest path tree, which is essentially the solution tree to running Dijkstra’s with root node = source vertex, a MST has no source. However, it is possible for the MST to be the same as the SPT.

We can think of the MST as a global property for the entire graph, as opposed to SPT which depends on which node is the source node.

If the edges of the graph are not unique, there’s a chance that the MST is not unique.

## Cuts Property

* A **cut** is defined as assigning the nodes in a graph into two sets.
* A **crossing edge** is an edge that connects two nodes that are in different sets
* The smallest crossing edge is the crossing edge with smallest weight

The **Cut Property** states that the smallest crossing edge is always going to be in the MST, no matter how the cut is made.

![](<../../img/assets/image (109).png>)