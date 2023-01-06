# Dijkstra's Algorithm 

## One sentence overview:
Visit vertices in order of best-known distance from source; on visit relax every edge from the visited vertex.

## Dijkstra's vs BFS big idea:
BFS returns the shortest paths in an unweighted graph, where the shortest path is just defined to be the fewest number of edges traveled along a path. In Djikstras, we can generalize the breadth-first traversal to find the path with the lowest cost, where the cost is determined by different weights on the edges. Djikstras uses a PQueue to maintain the path with lowest cost from the starting node to every other node. 

## Important points: 
- always visits vertices in order of total distance from source
- relaxation always fails on edges to visited vertices 
- guarantees to work optimally as long as edges are all non-negative
- solution always a tree form, true for undirected graphs
- can think of as union of shortest paths to all vertices 
- edges in solution tree always has V-1 edges, where V = #vertices b/c for each vertex, exactly one input source except the root 

## Key invariants:
1. edgeTo[v] always contains best known predecessor for v
2. distTo[v] contains best known distance from source to v
3. PQ contains all unvisited vertices in order of distTo


## PseudoCode:
    PQ.add(sourceVertex, 0)
    For v in allOtherVertices:
	    PQ.add(v, infinity)
    While !PQ.isEmpty():
	    P = PQ.removeSmallest
	    relax(P)
	    
    (relaxing edge p → q)
    relax(Vertex p):
	    If distTo[p] + q < distTo[q]:
		    distTo[q] = distTo[p] + q
		    edgeTo[q] = p
		    PQ.changePriority(q, distTo[q])

		

## Runtime:
$O(V*log(V) + V*log(V) + E*log(V)) → O(E*log(V)) $
- each add operation to PQ takes log(V), and perform this V times
- each removeFirst operation to PQ takes log(V) and perform this V times 
- each change priority operation to PQ takes log(V), perform this as many times as there are edges
- everything else = O(1) 
- usually # edges >= # vertices 


# A* Algorithm
- Literally just Dijkstra’s, but with an added heuristic function to consider. Motivation: can help bias our algorithm in the right direction so that it doesn’t make a bunch of bad moves. 
- For each vertex instead of only comparing distTo[v], also have a heuristic evaluation, so visit vertices in order of d(goal, v) + h(v, goal)
- Not all vertices get visited, algorithm only cares about finding the best path to the goal, and not any other vertex (that’s how the heuristic will be designed)
- heuristic must be both:
    * Admissible - heuristic of each vertex returns a cost that is <= the true cost/distance i.e. h(A) <= cost(A, goal)
    * Consistent - difference between heuristics of two vertices <= true cost between them i.e. h(A) - h(B) <= cost(A, B)
- Demo:https://docs.google.com/presentation/d/177bRUTdCa60fjExdr9eO04NHm0MRfPtCzvEup1iMccM/edit#slide=id.g369665031c_0_350