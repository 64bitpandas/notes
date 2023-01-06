---
title: "Depth First Search (DFS)"
---

## Depth First Traversal

Before we move on to searching, let's talk about **traversing. Traversal** is the act of **visiting nodes in a specific order.** This can be done either in trees or in graphs.

For trees in particular, there are **three main ways** to traverse.

![The example tree we will use for traversal illustrations.](<../../img/assets/image (89).png>)

The first way is **inorder** traversal, which visits **all left children**, then **the node itself,** then **all right children.** The end result should be that the nodes were visited in **sorted order.**

The second way is **preorder** traversal, which visits **the node itself first,** then **all left children,** then **all right children.** This method is useful for applications such as printing a directory tree structure.

The third way is **postorder** traversal, which visits **all left children,** then **all right children,** then **finally the node itself.** This method is useful for when operations need to be done on all children before the result can be read in the node, for instance getting the sizes of all items in the folder.

Here are some pseudocodey algorithms for tree traversals.

```java
// INORDER will print A B C D E F G
void inOrder(Node x) {
    if (x == null) return;
    inOrder(x.left);
    print(x);
    inOrder(x.right);
}

// PREORDER will print D B A C F E G
void preOrder(Node x) {
    if (x == null) return;
    print(x);
    preOrder(x.left);
    preOrder(x.right);
}

// PREORDER will print A C B E G F D
void postOrder(Node x) {
    if (x == null) return;
    preOrder(x.left);
    preOrder(x.right);
    print(x);
}
```

## Depth First Search in Graphs

Graphs are a little more complicated to traverse due to the fact that they could have **cycles** in them, unlike trees. This means that we need to **keep track of all the nodes already visited** and add to that list whenever we encounter a new node.

Depth First Search is great for determining if everything in a graph is connected.

Here's an outline of how this might go:

* Keep an array of 'marks' (true if node has been visited) and, optionally, an edgeTo array that will automatically keep track of how to get to each connected node from a source node
* When each vertex is visited:
  * Mark the vertex
  * For each adjacent unmarked vertex:
    * Set edgeTo of that vertex equal to this current vertex
    * Call the recursive method on that vertex

Like trees, DFS can be done **inorder, preorder, or postorder.** It's nearly identical behavior to trees, with the addition of the marks array.
