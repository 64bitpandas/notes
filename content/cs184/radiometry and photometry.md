## Introduction
Lights work by converting energy into photons, which each carry a small amount of energy away. Some of these photons reflect from objects and bounce into our eyes, which we perceive as light.

**Radiometry** is a measurement system for illumination, used to quantify the spatial properties of light. It can be used to perform lighting calculations to represent reality.

### Assumptions
1. Assume a geometric optics model of light: photons travel in straight lines, and can be represented as rays.
2. Assume a steady state flow: the rate of energy consumption of light sources is constant, so flux/power and energy can be interchangable.

## Summary

![[/cs184/img/Pasted-image-20230304225750.png]]
![[/cs184/img/Pasted-image-20230304151739.png]]

## Radiometric units vs. Photometric units

Radiometric units are the standard SI units for measuring quantities of energy in space.
Every radiometric unit has a photometric equivalent, which accounts for the response of the human visual system.

**radiant/luminous energy $Q$** (joules): amount of energy in the form of electromagnetic radiation. 

**radiant/luminous flux/power $\Phi$:** (watts, lumens/lm) the density of energy: amount of energy emitted, reflected, transmitted, or received per unit time.
 - Luminous flux $\Phi_v$ can be represented as $\int_0^\infty \Phi_e(\lambda)V(\lambda)d\lambda$, where $\Phi_e$ is the radiant flux, and $V$ is the efficiency curve (amount of light the eye can perceive at a given wavelength $\lambda$).
$$\Phi = \frac{dQ}{dt}$$

**Radiant Intensity:** $I$ (candela, cd) the power per unit solid angle emitted by a point light source.
 - A solid angle is a block of 3D space within a sphere. $\omega$, a steradian, is like a radian but 3D. 
 - Definition of solid angle: $\Omega = A/r^2$ so a sphere as $4\pi$ steradians.
$$I(\omega) = \frac{d\Phi}{d\omega}$$
The radiant intensity of an **isotropic point source** (emit light uniformly in all directions) can be derived as such:
$$\Phi = \int_{S^2} I d\omega = 4\pi I; I = \frac{\Phi}{4\pi}$$

## Irradiance
**Irradiance/Illuminance:** $E$ (lux): power per unit area incident on a surface point
$$E(x) = \frac{d\Phi(x)}{dA}$$
**Irradiance Falloff:** The intensity decreases by the square of the distance from the light source.
$$E' = \frac{E}{r^2}$$ where $E$ is the irradiance over a sphere at radius $1$, $E = \Phi/(4\pi)$ 


## Lambert's Cosine Law

![[/cs184/img/Pasted-image-20230302134340.png]]


## Radiance
Radiance is the fundamental quantity that describes the distribution of light in an environment. Formally, it is the power emitted, reflected, transmitted, or received by a surface per unit solid angle per unit projected area.

$$L(p, \omega) = \frac{d^2 \Phi(p, \omega)}{d\omega dA \cos \theta}$$
Unit: nit (lumens per steradian-meter^2)

Radiance is invariant along a ray in a vacuum.

To convert radiance into irradiance:
$$E(p) = \int_{H^2} L_i(p, \omega) \cos \theta d\omega$$

![[/cs184/img/Pasted-image-20230304153118.png]]
