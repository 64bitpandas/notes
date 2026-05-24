---
title: "Minimum Spanning Trees"
weight: 90
created: "February 11, 2021 9:11 AM"
---

### The Problem

Given an undirected graph $G$ with positive edge weights, find a subset $T \subseteq E$ such that:

- All vertices are connected.
- The sum of edge weights in $T$ is minimized.

We can notice that $T$ is actually a **tree**!

### Tree Properties

An undirected graph $T$ is a tree if:

1. $T$ is connected.
2. $T$ has no cycles.
3. $|E| = |V| - 1$.

 **Any 2 of these properties implies the third.**

- Proof
    
    1 and 2 implies 3:
    
    Pick any vertex to be the root, run DFS. Every vertex has one parent except for the root. This shows that there is 1 less vertex than there are edges.
    
    2 and 3 implies 1:
    
    Suppose we have $|V|$ vertices with no edges. (So, there are $|V|$ connected components.) We can keep adding edges one at a time such that either the number of components decreases by 1, or we create a cycle. If we always choose edges such that the former condition applies to all of them, we can add a maximum of $|V| - 1$ edges before we guarantee that a cycle must be created.
    

### Cuts in a Graph

A **cut** in a graph $G(V, E)$ is a partition $V = S \cup (V \setminus S)$ referring to edges connecting $S$ and $V \setminus S$. (In other words, it's a way to split the graph into two connected components.

**Claim:** The lightest (smallest weight) edge in a cut appears in some MST.

- Proof
    
    Let $T$ be a MST, and $e$ be a light edge connecting two components $S$ and $V \setminus S$.
    
    Now, suppose there is another edge $e' \ne e$ such that it also connects $S$ and $V \setminus S$.
    
    However, having two edges connecting the same two components suggests that there is a cycle somewhere in the graph, so this isn't a MST! 
    
    If we get rid of $e'$, then the graph would be a tree because we are destroying a cycle. Since T has no cycles and is connected, it must be a tree.
    

### Kruskal's Algorithm

- Let $X$ be an empty set.
- Sort all edges by weight.
- For all edges in increasing order:
    
    If $X \cup \{e\}$ has no cycle, then add $e$ to $X$. 
    
- **Proof:**
    
    We can prove Kruskal's by induction.
    
    **Base case:** From the [[Cuts]] section, we know that the lightest edge in a graph is part of its MST.
    
    **Recursive case:** Suppose we already added the $k$ lightest edges, and we're trying to add edge $k+1$. Now, suppose that there are connected component(s) created by the $k$ edges. We know that adding another edge that doesn't create a cycle must connect two previously disconnected components, because if they were already connected the edge would already be part of the $k$ edges. 
    
    Since we do this $|V| - 1$ times, it creates a tree that, by construction, minimizes the total weight count.
    
- **Implementation: Naive**
    - Sorting the edges can be done using an $O(|E| \log |E|)$ algorithm in the worst case (quicksort, mergesort, etc)
    - Figuring out if $X$ has no cycle can be done using DFS, which is an $O(|V| + |E|)$ algorithm. Naively running DFS once per edge will result in a runtime of $O(|V| \cdot |E|)$. However, **we can do better!**
- **Implementation: Union Find**
    
    Using a **union find** structure will be beneficial because we can continually keep track of connected groups of vertices. The best way to see if an edge $e(u, v)$ creates a cycle is to check if $u$ and $v$ already have the same parent in the union find. More formally, we can use this algorithm:
    
    ```python
    def kruskal(E, V)
    X = UnionFind() # create empty union find
    for each v in V:
    	X.makeset(v) # create a distinct set in the union find
    sorted_edges = sort(E)
    
    for e(u, v) in sorted_edges:
    	if X.find(u) != x.find(v):
    		union(u, v) # merge connected components of u and v
    ```
    
    The runtime of this algorithm is $O(|E| \log |V|)$:
    
    - The cost of making the set is $O(|V|)$.
    - The cost of sorting is $O(|E| \log |E|)$.
    - The cost of finding (over all loops) is $O(|E| \cdot \log(|V|))$.
    - The cost of unions is $O(|V| \log |V|)$ since every vertex is unioned once.
- **Implementation: Efficient Union Find**
    
    For each $v \in V$, keep track of:
    
    - $\pi(v)$, the parent of $v$, which points to the parent of $v$ in the tree. This defines the connected component of which $v$ belongs.
    - rank($v$), which is the height of the subtree rooted at v (i.e. how many layers are below $v$).
    
    This will allow us to make some modifications to the `union` and `find` functions:
    
    - We will make sure to make all vertices on a path to a particular root point to the root itself. We can guarantee this characteristic by changing $\pi(v)$ to the root for every vertex on the path to the desired vertex every time we run `find` . This is known as **path compression.**
        - The cost of this operation is $\log^* |V|$, run $|E|$ times, such that if $\log^* |V| \le 5$, $|V| \le 2^{65536}$... (log star grows veeeeeeeery slowly...)
        
        ```python
        def find(v):
        	if v != parent[v]:
        		parent[v] = find(v)
        	return parent[v]
        ```
        

### A greedy solution: Prim's Algorithm

As long as there is no cycle, just add the cheapest edge to $T$. When we run into an edge that cannot be added without creating a cycle, then the MST is complete. This is **Prim's Algorithm,** more formally:

- Let X be an empty set.
- Until $|V| - 1$ edges are added (i.e. the graph is connected):
    - Pick a cut $S, V \setminus S$ such that X doesn't cross the cut.
    - Add an edge $e$ with smallest weight in cut to $X$.

The differences between Prim's and Kruskal's are:

- Prim's Algorithm creates a subtree that is connected at every step, whereas Kruskal's Algorithm does not guarantee subcomponents to be connected until the very end.
- Prim's Algorithm computes the cut based on vertices from $X$, whereas Kruskal's algorithm computes the cut based on connected components of a particular vertex $u$.

- **Implementation: Priority Queue**
    
    ```python
    def prims(V, E):
    	cost = [inf for v in V]
    	prev = [None for v in V]
    	for all v in V:
    		cost[v] = 0 # pick any initial vertex
    		H = PriorityQueue(V) # create priority queue based on cost containing all v
    		while H is not empty:
    			v = H.remove_min()
    			for each e(v, u) in E:
    				if cost(u) > weight(e):
    					cost(u) = weight(e)
    					prev(u) = v
    ```
    

 ****which runs in $O(|E| \cdot \log|V|)$ with a simple implementation.

However, we can do better: $O(|E| \log^*(|V|)$.