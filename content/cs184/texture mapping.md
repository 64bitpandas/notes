Texture can be used to store a lot of complex information about an object without needing to split it up into really tiny polygons.

Color, roughness, and brightness are all examples of properties that can be modelled using texture mapping.

## Coordinate spaces
There are three main coordinate spaces that we need to deal with:
1. **Screen space** describes the location of the pixel on the screen we want to access. (2D, using $x$ and $y$ coordinates)
2. **World space** describes the location that pixel corresponds to on the object itself. (3D, using $x, y, z$ coordinates)
3. **Texture space** describes the properties mapped to that location on the object. (2D, using $u$ and $v$ coordinates)
![[/cs184/img/Pasted-image-20230201180532.png]]


## Barycentric Coordinates
The barycentric coordinate system describes locations inside of a triangle. Essentially, they represent the weighted average of points with the weights summing to one with convex hull properties.

To find the coordinates corresponding to cartesian space, solve the following system of 3 equations, where $(x,y)$ is the point and $A,B,C$ are the vertices:
$$
(x, y) = \alpha A + \beta B + \gamma C; \alpha + \beta + \gamma = 1
$$

Barymetric coordinates can also be viewed geometrically:
![[/cs184/img/Pasted-image-20230201181121.png]]

The matrix conversion is as follows:
![[/cs184/img/Pasted-image-20230201181236.png]]



## Mipmaps
Mipmaps solve the problem of texture aliasing when viewing objects from a far distance. (Depending on the distance, the amount of texture used per pixel can change drastically.)

Mipmaps downsize textures based on the relative distance between 


## Texture Maps

 - **Displacement Mapping:** texture stores perturbation to surface position. This is very difficult to implement, so we can approximate it with **bump mapping** (texture stores perturbation to surface normal instead).
 - **3D Mapping:** taking slices of a 3D object, and determining the texture for each slice. Since this is expensive, it can be approximated using 3D procedural noise and volume rendering.
 - **Shadow Mapping:** pre-render scene by transforming it to the coordinate space of the light, render a shadow buffer, and save it as a map.

