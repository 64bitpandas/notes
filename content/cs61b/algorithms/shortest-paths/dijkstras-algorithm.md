---
title: "Dijkstra's Algorithm"
weight: 1
---

> [!info] Content Note
>
> Before continuing, make sure you're comfortable with [Graphs](../../abstract-data-types/graphs.md), [Stacks and Queues](../../abstract-data-types/collections/stacks-and-queues.md), and [Shortest Paths](./).


## One sentence overview

Visit vertices in order of best-known distance from source; on visit, relax every edge from the visited vertex.

## Detailed Breakdown

Djikstras uses a **PriorityQueue** to maintain the path with lowest cost from the starting node to every other node, an **edgeTo** array to keep track of the best known predecessor for each vertex, and a **distTo** array to keep track of the best known distance from the source vertex to every other vertex.

**Relaxing** the edges of a vertex v just refers to the process of updating edgeTo\[n] for each neighbor n to v.

You'll see in the pseudocode and diagrams below that succesful relaxation only occurs when the edge connecting the vertex being visited to one of its neighbors yields a smaller total distance than the current shortest path to that neighboring vertex that the algorithm has seen.

Now, here's a demonstration on how it works! Let's start out with this graph:

![](<../../img/assets/image (92).png>)

We'll start at node A and try to figure out the shortest path from A to each node. Since we have no idea how far each node is, we'll take the conservative guess that everything is infinitely far away ♾😎

The first thing we have to do is update A's adjacent nodes, which are **B** and **D**. Since there's only one known path to each, it shouldn't be too hard to see why we need to update the values below. One thing to note is that the priority queue **sorts the vertices by the distance it takes to get there.**

![](<../../img/assets/image (93).png>)

Now, we have a choice to move on to either **B** or **D**. Since B has a **shorter distance,** we'll move on to that first. When we move on, we have to **remove that value from the priority queue** and **update all of its neighbors.** Here, we see that going from **B to D** is **shorter** than **A to D**, so we have to **update distTo AND edgeTo of D** to reflect this new, shorter path. **This process** (updating each adjacent node) **is called relaxing the edges of a node.**

![](<../../img/assets/image (94).png>)

Now, let's move onto **D** since it has the next shortest path. Again, we **remove D from the priority queue** and **relax C** since we found a shorter path.

![](<../../img/assets/image (95).png>)

Finally, we'll move onto **C** as that has the next shortest path in the priority queue. This will reveal our final node, **E**.

![](<../../img/assets/image (96).png>)

Since **the priority queue is now empty,** our search is done! 😄 Here's what the final solution looks like **in a tree form**:

![Dijkstra's Algorithm ALWAYS produces a solution in a tree format.](<../../img/assets/image (98).png>)

It's a very spindly tree indeed, but hopefully it demonstrates that the result is **acyclic**.

## Properties of Dijkstra's Algorithm

**Dijkstra's Algorithm has some invariants (things that must always be true):**

1. edgeTo\[v] always contains best known predecessor for v
2. distTo\[v] contains best known distance from source to v
3. PQ contains all unvisited vertices in order of distTo

**Additionally, there are some properties that are good to know:**

* always visits vertices **in order of total distance from source**
* relaxation always **fails on edges to visited vertices**
* guarantees to work optimally **as long as** **edges are all non-negative**
* solution always creates a **tree form.**
* can think of as **union of shortest paths to all vertices**
* **edges in solution tree always has V-1 edges**, where V = the number of vertices. This is because every vertex in the tree except the root should have **exactly one input.**

## Pseudocode

```java
public Class Djikstra() {

    public Djikstra() {
        PQ = new PriorityQueue<>();
        distTo = new Distance[numVertices];
        edgeTo = new Edge[numVertices];
    }

    public void doDijkstras(Vertex sourceVertex) {
        PQ.add(sourceVertex, 0);
        for(v : allOtherVertices) {
            PQ.add(v, INFINITY);
        }
        while (!PQ.isEmpty()) {
            Vertex p = PQ.removeSmallest();
            relax(p);
        }
    }
    // Relaxes all edges of p
    void relax(Vertex p) {
        for (q : p.neighbors()) {
            if (distTo[p] + q.edgeWeight < distTo[q]) {
                distTo[q] = distTo[p] + q.edgeWeight;
                edgeTo[q] = p;
                PQ.changePriority(q, distTo[q]);
            }
        }
    }
}
```

## Runtime Analysis

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
