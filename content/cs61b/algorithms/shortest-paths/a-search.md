---
title: "A* Search"
weight: 999
---

> [!info] Content Note
>
> In order to understand A\*, you'll need to be comfortable [Dijkstra's Algorithm](dijkstras-algorithm.md) first!


## A\* Algorithm

The A\* Search Algorithm is **incredibly similar to Dijkstra's Algorithm** with one addition: a **heuristic function.**

This heuristic function calculates weights of a path **from a vertex to a goal vertex.** This way, we can help bias our algorithm in the right direction so that it doesn’t make a bunch of bad moves.

This has an important implication: **not all vertices get visited.** The algorithm only cares about finding the best path to the goal, and not any other vertex (assuming we design our heuristic well).

The **order** that the vertices get visited is lowest **distance + heuristic**. This is basically the same as Dijkstra's, just with that added heuristic term.

## What's a good heuristic?

Heuristic functions can be really tricky to design, since there isn't much to go off of.

**A good heuristic has these two properties:**

* **Admissible** - heuristic of each vertex returns a cost that is <= the true cost/distance i.e. h(A) <= cost(A, goal)
* **Consistent** - difference between heuristics of two vertices <= true cost between them i.e. h(A) - h(B) <= cost(A, B)

## **Want more?**

[Here's a cool demo!](https://docs.google.com/presentation/d/177bRUTdCa60fjExdr9eO04NHm0MRfPtCzvEup1iMccM/edit#slide=id.g369665031c\_0\_350)

