## Introduction
So far, with a rasterizer, we've seen how to draw polygons to the screen. However, this assumes that we already know where the polygons are in space. How do we model more complex objects, curves, faces, and fluids?


## Parametric Coordinates
We can represent a curve using a function $x(u)$, where $u$ is a real number. 
Parametric curves may have multiple formulae for the same curve, but they are not all the same: for example, the function $x(u) = [u,u]$ plots a diagonal line with uniform spacing between points, whereas $x(u) = [u^3, u^3]$ also results in a diagonal line but can't be differentiated at $u=0$.

### Tangents
The tangent to a curve $t(u)$ can be calculated as such:
$$ t(u) = \frac{\partial x}{\partial u}$$
The tangent to a surface is calculated in the same way, but must be split into $t_u$ and $t_v$.

To calculate the normal of a parametric surface, use
$$\hat n = \frac{t_u \times t_v}{||t_u \times t_v||}$$
Degeneracies may occur if $\partial x / \partial u = 0$ or $t_u \times t_v = 0$.

## Splines
**Goal:** Given a few points in space, figure out a way to connect them into a smooth, continuous curve.

### Cubic Hermite Interpolation
Given two points and the derivatives at those two points, we can find a unique cubic function that passes through those two points using a system of equations:
$$x(u) = c_0 + c_1u + c_2u^2 + c_3u^3$$
$$x'(u) = c_1 + 2c_2u + 3c_3u^2$$
Assuming $u_0 = 0$ and $u_1 = 1$, this will create a system of 4 equations. Here's the basis matrix $\beta_H$:

![[/cs184/img/Pasted-image-20230209121032.png]]
![[/cs184/img/Pasted-image-20230209121046.png]]

### Catmull-Rom Interpolation
If we have more than two points, we might need a higher order function. However, these are expensive to compute and hard to manage, so instead we can just make a series of cubic hermite curves.

Given some points:
 - Set the derivative equal to the slope between the next two lines (example: for $y_1$, set the derivative to $1/2(y_2 - y_0)$
 - Since we have a derivative and a point, use cubic hermite interpolation to connect the points.
![[/cs184/img/Pasted-image-20230209121815.png]]
![[/cs184/img/Pasted-image-20230209121841.png]]
![[/cs184/img/Pasted-image-20230209121854.png]]


### Bezier Curves
Rather than using points as ways to set derivatives, use them as handles for editing the tangent line (so the tangents are set indirectly). The nice thing about this is that all parameters become points, and the process is nearly idential to Catmull-Rom (just with a different transform matrix).
![[/cs184/img/Pasted-image-20230209122159.png]]

**Convex hull property:** All points on a curve are inside of the convex hull of control points. In other words, if we draw a bounding box of control points, the curve is always inside. 
 - The Bezier basis is invariant with respect to affine transforms.

## Meshes
A mesh is a configuration of connected triangles.
 - **topology:** what is connected to what. (which vertices are connected to which triangles)
 - **geometry:** the physical shape of an object.

If two meshes have the same topology, we can easily animate interpolation: $V_{new} = \alpha V_1 + (1-\alpha) V_2$

Two meshes can have the same topology and different geometry, or same geometry and different topology.![[/cs184/img/Pasted-image-20230209160905.png|400]]

### Manifolds
A **manifold** is a surface that always yields a disk when cut.
![[/cs184/img/Pasted-image-20230209161046.png|400]]

Assuming that a mesh is a manifold, we have some nice properties:
 - edges always connect 2 faces and 2 vertices
 - faces consist of a ring of edges and vertices
 - a vertex consists of a ring of edges and faces
 - $F - E + V = 2$ 


### Storing Meshes in Memory
While we can store each individual triangle, this is not very efficient for building meshes. There are some strategies to make it better:

**Triangle-neighbor:** For each triangle, store its vertices as well as the neighboring triangles (up to 3).
**Half-edge:** A half-edge represents one side of an edge with a direction. Edges consist of two half-edges, but all edges and vertices can be uniquely defined by one half-edge.

```cpp
struct HalfEdge {
	HalfEdge *twin; // same edge, different direction
	HalfEdge *next; // next edge that starts at the end vertex of this edge
	Vertex *vertex;
	Edge *edge;
	Face *face;
}

// for the below: halfedge = any halfedge adjacent to that vertex

struct Vertex {
	Point pt;
	HalfEdge *halfedge; 
}

struct Edge {
	Halfedge *halfedge;
}

struct Face {
	Halfedge *halfedge;
}
```


### Mesh Traversal
Use twin and next pointers to move around the mesh to process all vertices of a face:
```cpp
HalfEdge* h = f->halfedge;
do {
	process(h->vertex);
	h = h->next;
} while (h != f->halfedge);
```

Return all edges opposite of a vertex (example: if vertex is at the center of a hexagon, return outer edges of the hexagon)
- Idea: skip every other halfedge, then switch to the twin to continue traversing
```cpp
vector<EdgeIter> getOuterEdges(Vertex v) {
	vector<EdgeIter> edges;
	HalfEdgeIter curr = v->halfedge();
	HalfEdgeIter start = curr;
	do {
		edges.push_back(h->next()->edge())
		h = h->next()->next()->twin();
	} while (curr != start);
	return edges;
}
```


Laplacian smoothing:

Given a vertex $v$ at position $x$, modify $v$'s position using the formula
$$L(V) = \frac{1}{n} \sum_{v_j \in N(v)} x_j - x$$
(where $N(v)$ is the set of neighboring vertices and $n$ is the number of vertices in $N(v)$. The position is updated using $x' = x + kL(v)$.

```cpp
void diffuse(VertexIter v, float k) {
	Vector3D L(0,0,0);
	HalfedgeIter h = v->halfedge();
	halfedgeIter start = h;
	int n = 0;
	do {
		// get one neighbor using half edge
		VertexIter v_j = h->next()->vertex();
		// x_j - x
		Vector3D dir = v_j->position() - v->position();
		// add to L vector
		L += dir;
		n += 1;
		// Move to next v_j
		h = h->twin()->next()
	} while (h != start);
	v->position() = v->position() + k*L/n;
}
```


### Local Mesh Operations
**Edge flip:** triangle vertices flip
![[/cs184/img/Pasted-image-20230215164856.png]]

**Edge split:** insert midpoint of existing edge joining two triangles, and draw a line through it

![[/cs184/img/Pasted-image-20230215164908.png]]


### Subdivision
**Main idea:** start with a coarse mesh, and make it smoother algorithmically.

There are two main techniques: Loop subdivision and Catmull-Rom subdivision.

#### Loop Subdivision
1. Split each triangle into 4 smaller triangles by using the midpoints of the edges.
2. Assign new vertex positions according to a predetermined weighting scheme: ![[/cs184/img/Pasted-image-20230215165100.png]]

#### Catmull-Clark Subdivision
This type of subdivision is more robust, and is designed to work with non-triangle polygons.
1. Add a vertex in the middle of each face
2. Add a midpoint to each edge
3. Connect all new vertices
4. Adjust vertex positions to weighted average

An *extraordinary vertex* is a vertex that is connected to more than 4 other vertices. After subdividing, if there are $N$ extraordinary points and $K$ non-quad faces, then there will be $N+K$ extraordinary vertices, and all faces will be converted into quads.