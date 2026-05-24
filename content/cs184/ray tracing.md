Ray tracing is an alternative technique to rasterization that accomplishes the same thing (converting the world into a 2D screen).

## Overview
### Ray Casting
Early ray tracing (1968): To generate an image:
1. Cast a ray for every pixel from the camera to the world.
2. Use a shading calculation (e.g. Blinn Phong) to calculate the color at the intersection of that ray to the object that it collides with.
3. Check for shadows by casting a ray from the light source to the point. (If the ray is blocked, then a shadow should be drawn.)

It turns out that raycasting is actually very similar to the rasterization algorithm!

### Recursive Ray Tracing
Recursive ray tracing is used for reflection and transparency. If there is a reflective surface, we can trace secondary rays until the ray hits a non-specular surface (or reaches max recursion depth). The final pixel color is a weighted sum of contributions along rays.

## Basic Algorithm

### Ray Equation

A ray is defined as an origin $o$, and a direction vector $d$. Rays vary with time:
$$r(t) = o + td$$
- $r(t)$ = position
- $t$ = some unit time

### Plane Equation
A plane is defined by a normal vector and a point on the plane.

For all points $p$ on the plane, a vector drawn from that point to another point on the plane $p'$ should be orthogonal to the normal vector:
$$p: (p - p') \cdot N = 0$$

Planes can also be defined by an equation
$$ax + by + cz + d = 0$$


### Ray Intersection With Plane
**Main idea:** figure out the time in which a ray intersects with a plane.

Set $p = r(t)$ and solve for $t$:
$$(p - p') \cdot N = (o + td - p') \cdot N = 0$$
$$t = \frac{(p' - o) \cdot N}{d \cdot N} $$
### Ray Intersection With Triangle
**Main idea:** Since a triangle falls within a plane, we can first do a ray-plane intersection, then test if the hit point is inside the triangle using the three-line test.

We can represent the intersection in barycentric coordinates. Suppose $\alpha = b_1$, $\beta = b_2$, $\gamma = 1 - b_1 - b_2$ at the intersection.

Then:
$$P = (1 - b_1 - b_2)P_0 + b_1 P_1 + b_2 P_2$$
Setting $r(t) = P$ yields the following equation:
$$O - tD = (1-b_1-b_2)P_0 + b_1P_1 + b_2P_2
$$
which can be rewritten as this matrix equation:

$$\begin{bmatrix}  -D & P_1 - P_0 & P_2 - P_0 \end{bmatrix} \begin{bmatrix}  t \\ b_1 \\ b_2 \end{bmatrix} = O - P_0$$


### Ray Intersection With Sphere
A sphere can be defined as the set of all points $p$ such that $(p - c)^2 - R^2 = 0$, where $c$ is the center of the sphere and $R$ is the radius.

Solving for the intersection yields a quadratic equation, which has three possibilities:
 - No real roots = no intersection
 - One real roots = ray is tangent to sphere
 - Two real roots = ray passes through sphere

### Bounding Volumes
A way of increasing performance of ray tracing is to use bounding volumes around complex objects. If a ray does not pass through the volume, there is no need to calculate the intersection.


## Spatial Partitioning
One way of preprocessing for faster ray tracing is to build an **acceleration grid** which stores which objects are within which parts of space. (This is essentially like building lots of bounding boxes next to each other.)

This is actually a form of a hierarchical problem: to create this grid, we can decompose space by recursively subdividing it based on where finer objects are located. 

### KD Trees
(Short for k-dimensional trees)

Main idea: at each node, split on one of the axes (x, y, or z).

Internal nodes store:
 - Which axis they split on
 - Split position (coordinate of split plane along axies)
 - List of child nodes

Leaf nodes store:
 - A list of objects/triangles that are in that region of space
 - Mailbox information (store common computations done in that space to be looked up in the future)

To build a KD tree for preprocessing:
1. Create a bounding box
2. Recursively split cells along axis-aligned planes
	1. Can use simple rules (like mean/median splits)
	2. Can also try to minimize expected cost of ray intersection (see Bounding Volume Hierarchy)
3. Continue splitting until a termination criterion is met (max number of splits, max number of objects in cell, etc)

### Bounding Volume Hierarchy

