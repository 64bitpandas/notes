---
title: "Prim's Algorithm"
weight: 2
---

> [!info] Content Note
>
> Before reading, review [Minimum Spanning Trees](./), as that is the foundation of Prim's algorithm!

## Conceptual Overview

Prim's algorithm is an optimal way to construct a **minimum spanning tree**. It basically starts from an arbitrary vertex, then considers all its immediate neighbors and picks the edge with smallest weight to be part of the MST. **Note:** this creates a cut in the graph, where the two nodes in the MST being constructed are in one set, and every other vertex of the graph is in another set.

Now, the edges taken into consideration include all immediate neighbors of every node in the MST. Add the edge that has the smallest weight to the MST. Repeat until every vertex has been visited. The result is an MST for the graph.

## Detailed Breakdown

The way Prim's algorithm is usually implemented is via [PriorityQueue](../../abstract-data-types/collections/stacks-and-queues.md), `edgeTo` array, and` distTo` array. You will soon see its similarities to [Dijkstra's](../shortest-paths/dijkstras-algorithm.md).

First, insert all vertices into the PriorityQueue, storing vertices in order of **distance from MST**. Then, remove vertex with highest priority in the PriorityQueue and relax its edges. In each of these iterations, the distTo and edgeTo arrays will be updated for each vertex v if the **weight of the edge is smaller than the current value in distTo\[v]**. In other words, only update if the distance from the MST to the vertex is the best seen so far. This is a very important point, and is one of the subtleties that makes Prim's algorithm fundamentally different from Dijkstra's.

## Useful Properties/Invariants

The MST under construction is **always connected.**

## Pseudocode

```java
public class Prims() {

    public Prims() {
        PQ = new PriorityQueue<>();
        edgeTo = new Edge[numVertices];
        distTo = new Dist[numVertices];
        marked = new boolean[numVertices];
    }

    public void doPrims() {
        PQ.add(sourceVertex, 0);
        for(v : allOtherVertices) {
            PQ.add(v, INFINITY);
        }
        while (!PQ.isEmpty()) {
            Vertex p = PQ.removeSmallest();
            marked[p] = true;
            relax(p);
        }
    }

    public void relax(Vertex p) {
        for (q : p.neighbors()) {
            if (marked[q]) { continue; }
            if (q.edgeWeight < distTo[q]) {
                distTo[q] = q.edgeWeigth;
                edgeTo[q] = p;
                PQ.changePriority(q, distTo[q]);
            }
        }
    }
}
```

Looking at this pseudocode, the resemblance to Dijkstra's makes them seem nearly identical. But hopefully you've read the conceptual overviews first, and you understand the remarkable subtlety that leads to two very fundamentally different algorithms.

## Runtime Analysis

This is the same as for Dijkstra's Algorithm.

**Unsimplified:**

$
\theta(V * log(V) + V * log(V) + E * log(V))
$

**Simplified:**

$
\theta(E * log(V))
$

**Explanation:**

* each add operation to PQ takes log(V), and perform this V times
* each removeFirst operation to PQ takes log(V) and perform this V times
* each change priority operation to PQ takes log(V), perform this at most as many times as there are edges
* everything else = O(1)
* usually, there are more or equal edges compared to the number of vertices.

## Demo

[https://docs.google.com/presentation/d/1GPizbySYMsUhnXSXKvbqV4UhPCvrt750MiqPPgU-eCY/edit#slide=id.g9a60b2f52\_0\_0](https://docs.google.com/presentation/d/1GPizbySYMsUhnXSXKvbqV4UhPCvrt750MiqPPgU-eCY/edit#slide=id.g9a60b2f52\_0\_0)
