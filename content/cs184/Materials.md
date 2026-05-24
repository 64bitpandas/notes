In terms of graphics rendering, a material is equivalent to a BRDF: it's a 4-dimensional function that captures how light bounces off of objects.

**Microfacet theory:** Although all materials have microsurfaces (lots of bumps that make the normal vectors point in many directions), at a distance they all look smooth (macrosurface). 

There should be two BRDF's: the macroscale is flat and rough, while the microscale is bumpy and specular. Each microfacet (microscale calculation) has its own normal vector that is drawn from some distribution.
- Concentrated microfacet normals (similar directions) = glossy
- Spread out normals (pointing in lots of different directions) = diffuse

## Anisotropic BRDFs
So far, we've assumed that all specular highlights are elliptical. However, this is not always the case- different materials can have characteristic highlight patterns (brushed metals, fibers, etc).

The key detail that anisotropic BRDFs introduce is the directionality of the underying surface. 


Isotropic BRDFs are a reflection function of the incoming direction and reflected direction of rays. Although there are four terms, the $\phi_r$ term is redundant:
$$f_r(\theta_i, \phi_i; \theta_r, \phi_r) = f_r(\theta_i, \theta_r, \phi_r - \phi_i)$$
Anisotropic BRDFs do not have this property. 

