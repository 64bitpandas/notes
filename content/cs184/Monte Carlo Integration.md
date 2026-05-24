Integration is used for lots of applications in graphics (radiometry, exposure/motion blur simulations, etc. etc.). These integrals are often multi-dimensional, over time, space, and/or polar coordinates. This is very expensive: the *curse of dimensionality* outlines the fact that:
 - The complete set of samples is exponential over the number of dimensions: $N^d$
 - The error of numerical integration is inversely proportional to the number of samples: $\frac{1}{N^{1/d}}$
 - The error for random sampling is proportional to $1/\sqrt N$.

The above suggests that for higher dimensions, random sampling integration methods (like Monte Carlo integration) become much better than numerical integration methods.


## Overview
**Main idea:** estimate an integral based on random sampling of the function.

Advantages:
 - general, relatively simple method
 - only requires evaluating the function at any point (discontinuities allowed)
 - efficient for high dimensional integrals

Disadvantages:
 - Noise (only correct on average)
 - Slow to converge, many samples needed

Let's define the Monte Carlo estimator for the integral of a given function $f(x)$.
 - Suppose we have a random variable  $X_i \sim p(x)$
 - $p(x)$ must be nonzero for all $x$ where $f(x)$ is nonzero.
 - Then,
 - $$F_N = \frac{1}{N} \sum_{i=1}^N \frac{f(X_i)}{p(X_i)}$$
Properties:
 - Variance decrease linearly with the number of samples.
 - Error is inversely proportional to the square root of the number of samples (standard deviation).

## Basic Monte Carlo Estimator
Basic MCE is a simple special case where we sample with a uniform random variable such that $X_i \sim p(x) = C$.

As a reminder, the PDF of a uniform random variable is $C = \frac{1}{b-a}$.
Then, $$F_N = \frac{b-a}{N} \sum_{i=1}^N f(X_i)$$
This estimator is *unbiased* (approaches true answer given infinite number of samples).


### N-dimensional basic estimator
To generalize to multiple dimensions, we can change the $b-a$ term to be a multiple of all of the ranges in every dimension.

## Example: Direct Lighting Estimate
**Main idea:** sample directions over hemisphere uniformly in a solid angle. 

Let's suppose our integral $E(p) = \int L(p, \omega) cos \theta d \omega$, and our estimator is $p(\omega) = 1/(2\pi)$ (number of steradians in hemisphere).

Then, our estimator will be
$$F_N = \frac{2\pi}{N} \sum_{i=1}^N L(p, \omega_i) \cos \theta$$


Here it is in algorithm form:
1. Input: surface point $p$
2. Initialize estimator $F_N$ to $0$
3. For each of $N$ samples:
	1. Generate random direction $\omega_i$
	2. Compute radiance $L_i$ arriving at $p$ from direction $\omega_i$
	3. Increment MC estimator by adding $\frac{2\pi}{N} L_i \cos \theta$ 


## Inversion Method
1. Compute PDF by normalizing
2. Compute CDF
3. sample from $p(x)$ 


Example: Suppose we want to sample from the exponential distribution $p_\lambda(x) = \lambda e ^{-\lambda x}$ using a uniform random variable $U \sim \text{Normal}(0,1)$.

First, we can recognize that the PDF is equal to $p(x)$, so no action needs to be done.

Then, to compute the CDF, take the integral of $p(x)$: $\int_0^x p(x) dx = 1 - e^{-\lambda x}$

The inverse of the CDF is  $-\log(1-x)/\lambda$. This can be used alongside the random variable $U$ to get the final random variable for sampling:
$$F_\lambda(x) = -\frac{\log(1-U)}{\lambda}$$


