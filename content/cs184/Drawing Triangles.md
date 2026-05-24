## Introduction
Digital drawing involves creating a 2D representation on a screen, paper, or other medium. It's useful for a lot of applications like:
- CNC machines
- Laser cutters
- CRT monitors

There are several different methods to do this. For the time being, we will focus on the technique of **rasterization**, which involves first representing the scene or object in a 3D, digital context, then converting that representation into a 2D image.

## Raster Displays
Raster scanning refers to the act of rendering a 2D array of pixels from left to right, top to bottom. 

The memory for an individual unit of raster scanning is a **frame buffer**, which has information to hold an image (which is just an array of color values). The digital representation is then converted into an analog signal for display on a monitor.

Since there are many display implementations (LCD, mirrors, etc), we'll make the simplifying assumption that each pixel is just a square that can perfectly replicate any color value over its entire area. (In reality, pixels are separated into RGB components that each cover some independent portion of the pixel.)

## Primitives

A graphics engine (like OpenGL) provides a library of *primitives* that convert coordinates into continuous lines or shapes, and rasterizes them into the frame buffer.
![[/cs184/img/Pasted-image-20230119155822.png]]

### Graphics Pipeline

![[/cs184/img/Pasted-image-20230119160014.png|400]]
* Per-vertex operations: converting vertices to lines, and transforming them if needed
* Rasterizer: converting lines to pixels
* Per-fragement operations: shaders
* Frame buffer operations: conversion from frame buffer data to screen image

## Triangles
Triangles are often used as the most basic polygon component of meshes. 
They are nice for a variety of reasons:
- You can break up all other polygons into a bunch of triangles
- Guaranteed to be planar
- Well-defined for a variety of operations mathematically (such as interpolation)

### Rasterizing a triangle
To rasterize a triangle to the frame buffer, we need to convert the three vertices (input) into a set of discrete pixel values approximating the triangle (output). 

A simple approach to do so is to use **periodic sampling**, which is basically just evaluating a function on a range of discrete points. (Sampling is a key concept in graphics- it'll pop up again in many instances later on!)

An intuitive way of understanding sampling is to imagine superimposing the triangle over the 2D grid of pixels, and choosing all the pixels whose centers are inside of the triangle.
![[/cs184/img/Pasted-image-20230119160812.png|300]]

Here's a simple **point sampling** rasterization program, which takes in an indicator function `f` and enables pixels if they are inside the triangle.
```python
for x in range(xmax):
	for y in range(ymax):
		image[x][y] = f(x+0.5, y+0.5) # add 0.5 to get center of pixel
```

How does the above code work (especially `f`)?
* A triangle is an intersection of three half planes (i.e. a plane that is cut off at a line). 
* All we need to do is make sure the sampled point is inside all three of these half planes.
* Define an equation $L(x, y) = V \cdot N = -(x- x_0)(y_1 - y_0) + (y-y_0)(x_1-x_0)$.
	* $V$ is a line from $P_0$ to $P$, the point we're trying to evaluate.
	* $N$ is the normal vector for the line connecting $P_0$ and $P_1$.
	* If $L(x,y) > 0$, this means that the point is on the correct side of that edge (i.e. the dot product of $V$ and $N$ suggests that the angle is less than 90 degrees).
* Supposing we have three points $P_0, P_1, P_2$, apply the equation to all three combinations of points.

### Edge Rules
For a watertight mesh (which has triangles sharing common edges), we need to make sure not to overdraw pixels on the boundaries (i.e. draw the edge twice). 

OpenGL solves this by only drawing the "top edge" and "left edge" of a triangle.

### Tiled Triangle Traversal
In a modern GPU implementation, the process of rendering a triangle is made more efficient by dividing the frame buffer into larger *blocks* (rectangular groups of pixels). The GPU can then parallelize the computation by sending each pixel in the block to a different processor.

We can also skip testing blocks that are entirely inside or outside the triangle (early in/out detection).


