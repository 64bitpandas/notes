---
linkTitle: "Shortest Paths"
BookCollapseSection: true
weight: 20
---

We've seen that Breadth-First Search can help us find the shortest path in an unweighted graph, where the shortest path was just defined to be the fewest number of edges traveled along a path. In the following shortest-paths algorithms, we will discover how we can generalize the breadth-first traversal to find the path with the lowest total cost, where the cost is determined by different weights on the edges.