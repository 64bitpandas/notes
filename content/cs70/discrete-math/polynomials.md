---
title: "Polynomials"
weight: 970
---

## Introduction

"I learned this in 4th grade", you say, "and I already know how to do Taylor approximations and binomial expansions and get local minima... what else is there to do?" (At least that was my first thought :stuck\_out\_tongue:)

Turns out, polynomials are super useful in the world of discrete math. Here, we'll cover two applications in discrete space, which are **secret sharing** and **error correction.**

### Important Properties

Gotta do some quick review first! Recall that all polynomials are in the form

$
a_dx^d + a_{d-1}x^{d-1} + \cdots + a_1x + a_0
$

where $d$is the **degree** of the polynomial (highest power) and $a_i$are the **coefficients.**

Polynomials have some nice properties:

* A nonzero polynomial of degree $d$has at most $d$real roots.
* If we're given $d+1$distinct points (x y pairs), there is exactly one, unique polynomial of degree $d$that goes through all of those points.

### Finite Fields

Like many things in discrete math, polynomials can be taken to a modulo as well! When this happens and we have $p(x) \pmod{m}$where $p(x)$is a polynomial and $m$is a prime number, we say that we're working in a **Galois Field** $GF(m)$.

Even when working over a finite field, the two properties of polynomials still apply. Finite fields restrict the number of possible polynomials, which is actually necessary for some of the applications below.

## Lagrange Interpolation

We have already established that $d+1$points only have one unique degree $d$polynomial that goes through all of them. But how do we find this one polynomial?

**Lagrange Interpolation** is a method to recover this polynomial given your original points. It has a lot of interesting ties to previously covered concepts like the Chinese Remainder Theorem and linear algebra (which won't be covered here, but explore it further to find out more!). Here's how it works:

First, let's find a polynomial that is degree $d$ and is equal to $1$at point $x_1$, but $0$everywhere else.  This isn't too hard to do: we can use $(x-x_2)(x-x_3)\cdots(x-x_{d+1})$. Note here that we skipped $x_1$because adding that term would make the polynomial degree $d+1$! However, this alone would result in a number other than 1 at $x_1$, so we can normalize it by dividing by all $(x_1-x_j)$:

$
\Delta_1(x) = \frac{\prod_{j \ne 1} (x - x_j)}{\prod_{j \ne i} (x_1 - x_j)}
$

Why are we doing this though? Well, you can think of it like creating a **basis** of polynomials so that we can take a linear combination of all of them to get the original. Since $\Delta_1(x_1) = 1$, we can multiply it by $y_1$ to ensure that it passes through the original point. Combining all of the delta polynomials for all $d+1$original points yields

$
p(x) = \sum_{i=1}^{d+1} y_i \Delta_i(x)
$

## Secret Sharing

Now, let's take a look at a cool application of Lagrange interpolation!

Here's the setup: let's say you're in the Super Secret Club and want to create a secret code for your Super Secret Vault™. However, you want to make sure that the Vault™ can only be opened if 30 of your 50 members agree. How would we pull this off?

Here's the solution: **create a 29-degree polynomial** and give each person in the club a point on that polynomial $(x_i, y_i)$. **Make sure none of the x's are 0!** Then, set the secret code equal to $y_0$, the y-value of the polynomial corresponding to $x=0$.

We know that a 29-degree unique polynomial can be recovered with 30 distinct points. So, if 30 members agree and get together to share their points, we can use Lagrange interpolation to recover the original polynomial! Once you have this original polynomial, it is a simple matter to recover the secret code by plugging in 0 to the polynomial.

## Error Correction

Lagrange interpolation can also be used to correct errors in data (if it gets erased or corrupted). There are two main types of errors: **erasure errors,** when the data is simply lost, and **general errors,** where the data is corrupted and displays something other than the original data.

### Erasure Errors

Erasure errors aren't too tough to think about once we have a good grasp of polynomial properties. Since we know that a unique polynomial of degree $d$can be recovered with $d+1$points, we could simply tack on an additional $k$points in order to protect the original polynomial from $k$erased points.

### General Errors

General errors, on the other hand, are slightly more difficult to consider because they could throw off the result wildly if we do not identify them. So how do we figure out which points are the errors?

Let us construct an error-locator polynomial $E(x) = (x-e_1)(x-e_2) \cdots (x-e_k)$ where an error $e_i$ represents the incorrect value given by one of the spies when in a larger group.

For any one point $i$ in the original polynomial $P(i)$, we know that $P(i)E(i) = r_iE(i)$ where $r_i$ is the original location of the point of the polynomial.

If we have $M$ original data points, this provides enough points for a $M-1$ degree polynomial, which we can call $Q(x)$. For any particular point, though, we know that $Q(i) = P(i)E(i)$ since the point given is either in the original polynomial, or is in the error-locator polynomial. Therefore, in order to solve for the true polynomial $P(x)$, we can take the ratio $\frac{Q(x)}{E(x)}$ by definition of $Q(x)$. Since we do not know what each value $e_i$ is, we need to solve a system of linear equations for each point to identify what these are. **This requires** $M + 2k$ **equations**, because we require the polynomial $Q(x)E(x)$ to perform this calculation.

****
