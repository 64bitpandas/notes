---
title: "Union Find (Disjoint Sets)"
weight: 993
---

# Union Find (Disjoint Sets)

> [!info] Content Note
>
> This is not a complete entry, because I feel like existing course materials already cover this in an extremely intuitive manner. See[ lab 14](https://inst.eecs.berkeley.edu/~cs61b/sp20/materials/lab/lab14/index.html) for an guide on how to implement your own Union Find structure!

The Union Find data structure is a way of representing a bunch of nodes that are connected to each other in subsets. It's used in [Kruskal's Algorithm](/cs61b/algorithms/minimum-spanning-trees/kruskals-algorithm.md) among other things.

Union Find is named as such because it supports two functions, **find** (which returns the group that a value is contained in), and **union** (which connects two values to form a single group).

Union Find tracks each set with an ID, typically **the value of the root of each set.** In the sections below, we'll discuss how to add an item to a set, as well as figure out which set an existing item is in.

## Union

In order to **join two values together,** we need to use the **union** function. Let's see what it does visually:

![Calling union(1,2).](<../img/assets/image (78).png>)

There are lots of ways to represent this behavior. One possible method is to keep an **array of parent values** corresponding to each actual value. In the example above, for instance, we can choose 1 as our parent and make 2 fall under that. Let's see how this might work:

![Parents list.](<../img/assets/image (79).png>)

Now, let's say we call `union(3,2)`. We can just set the parent of 3 to 2, as to create a structure like this:

![union(1,2) followed by union(3,2)](<../img/assets/image (80).png>)

This looks a lot like a tree!

You might have noticed that this looks like a **spindly tree** though, which is bad for runtime! Perhaps we can convert it to the equivalent of a bushy tree- the union function can be made much more efficient using tricks such as WeightedQuickUnion and Path Compression. Watch [this playlist](https://www.youtube.com/watch?v=JNa8BRRs8L4\&list=PL8FaHk7qbOD59HbdZE3x52KOhJJS54BlT\&index=1) for more information!

## Find

First, let's explore how to implement an efficient way to **find which set a value is in.** Using the union function from above, we can do this pretty easily with this simple algorithm:

* If the parent is 0, simply return the value.
* If the parent is not 0, return the result of calling the function on the parent value.

If we follow this algorithm on the example in the Union section, we can see that calling `find(3)` will go to `2`, then finally to `1` and return `1`.
