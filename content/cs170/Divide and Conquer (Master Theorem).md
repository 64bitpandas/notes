---
title: "Divide and Conquer (Master Theorem)"
weight: 20
created: "January 19, 2021 9:26 AM"
---

### Divide and Conquer: an Intro

![[/cs170/img/Divide-and-Conquer-Master-Theorem/Untitled.png]]

Sometimes, especially for recursive algorithms, we can write a runtime as a **recurrence relation**: that is,  part of a function's runtime definition is the function itself with a smaller problem size.

This applies directly to a method called **divide and conquer,** which goes something like this:

- We're given some input $x$ and are trying to evaluate a function $A(x)$.
- We can split $x$ into smaller parts $x_1, x_2, \cdots x_a$.
- We can then find the output of each individual part $A(x_1), A(x_2), \cdots A(x_a)$.
- Sum up all of these outputs to get the original desired value $A(x)$.

Take this example (Karatsuba Multiplication): $T(n) = 3T(n/2) + cn$

![[/cs170/img/Divide-and-Conquer-Master-Theorem/Untitled 1.png]]

### The General Form

$$
T(n) = a \cdot T(\frac{n}{b}) + c \cdot n^d
$$

$a$, $b$ and $c$ are constants and $T(n)$ is the total amount of work that must be done for an input size of $n$.

### Master Theorem for Recurrences

**Root Heavy**

$$
\frac{a}{b^d} < 1 \implies T(n) = O(n^d)
$$

**Balanced**

$$
\frac{a}{b^d}= 1 \implies T(n) = O(n^dlog(n))
$$

**Leaf Heavy**

$$
\frac{a}{b^d} > 1 \implies T(n) = O(n^{log_b(a)})
$$

**Proof:**

Here's a chart of how the problem evolves down the layers. At the end, we will need to calculate $T(1)$, which is assumed (without loss of generality) to be a constant work per problem $c$.

![[/cs170/img/Divide-and-Conquer-Master-Theorem/Untitled 2.png]]

If we sum up all of the total work per layer, we get the expression:

$$
T(n) = c \cdot n^d(1 + \frac{a}{b^d} + \cdots + (\frac{a}{b^d})^{log(b)^n})
$$

There are three cases (as shown above). We can split them now to evaluate this sum.

**Root Heavy:** $a/b^d < 1$, so $d > log_b(a)$.

Recall that $1 + p + p^2 + \cdots + p^k = \frac{p^{k+1}-1}{p-1}$ by the geometric series formula. 

So:

$$
T(n) = c \cdot n^d(\frac{1-(a/b^d)^{log_b(n)+1}}{1-a/b^d})
$$

which simplifies to $$c \cdot n^d (

**Balanced:** $a/b^d = 1$. 

This means that the work for each layer must be $1$ because $\frac{a}{b^d} = \frac{a}{b^{log_b(a)}} = \frac{a}{a}$. 

Since there are $log_b(n)$ layers, the total work done must be $c \cdot n^d (log_b(n)) \implies O(n^d log_b(n))$.

![[/cs170/img/Divide-and-Conquer-Master-Theorem/Untitled 3.png]]

![[/cs170/img/Divide-and-Conquer-Master-Theorem/Untitled 4.png]]