## Reflection
Reflection is the process by which light incident on a surface interacts with the surface such that it leaves on the same side without change in frequency.

### Cagetories of reflection
**Ideal specular:** perfect mirror reflection
**Ideal diffuse:** equal reflection in all directions
**Glossy specular:** majority of light reflected near mirror direction
**Retro-reflective:** light bounces back towards the way it came


### Reflection at a point
incoming differential irradiance:$$dE(\omega_i) = L(\omega_i) \cos \theta_i d \omega_i$$
Exiting differential radiance: $$dL_r(\omega_r)$$

## BRDF
**Bidirectional reflectance distribution function:** represents how much light is reflected into each outgoing direction $w_r$ from each incoming direction $\omega_i$
$$f_r(\omega_i \to \omega_r) = \frac{dL_r(\omega_r)}{L_i(\omega_i)\cos \theta_i d\omega_i}$$
### The Reflection Equation
![[/cs184/img/Pasted-image-20230304235356.png]]
![[/cs184/img/Pasted-image-20230304235126.png]]
The radiance received from a point $p$ at camera angle $\omega_r$ from the source is calculated as such:
 - Over all incoming directions:
	 - Use the BRDF $f_r$ and the angle $\theta_i$ to calculate the incoming radiance to point $p$

## Multiple Lighting Sources
If we have multiple lights, we can randomly choose light $i$ with probability $p_i$, then randomly sample over that light's directions with probability $p_L$. The weight for the lighting calculation will then be $1/(p_i p_L)$.

## Global Illumination

### The Rendering Equation
![[/cs184/img/Pasted-image-20230304235001.png]]

Let's break that down:
https://www.youtube.com/watch?v=AODo_RjJoUA
![[/cs184/img/Pasted-image-20230304235016.png]]
![[/cs184/img/Pasted-image-20230304235546.png]]



## Path Tracing Algorithm


### Russian Roulette
