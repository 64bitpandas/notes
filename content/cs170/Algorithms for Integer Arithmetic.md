---
title: "Algorithms for Integer Arithmetic"
weight: 10
created: "January 19, 2021 9:26 AM"
---

> 💡 Creating good algorithms requires two main building blocks: **correctness** and **efficiency.**



## Addition

We would like to define an algorithm $A_{add}$ such that...

$(\forall x,y)(A_{add}(x,y) \to x+y)$

### A naive approach

One straightforward way to add is to "count by fingers"- that is, keep adding one continually until you reach the end of the number.

Given $n$ digits, this algorithm, in the worst case, must add one $10^n - 1$ times. This is quite inefficient! Let's see if we can do better.

### The carry method

This is the 'long addition' we learned in elementary school: for each digit location, we sum up the digits at that location, then carry over the tens digit (if any) to the next location.

![[/cs170/img/Algorithms-for-Integer-Arithmetic/Untitled.png]]

Since in the Arabic numeral system there's a constant limit to how large each digit can be (at most 9), the runtime for an individual digit must be constant time $\Theta(1)$.

There are $n$ digits, and each digit takes $\Theta(1)$ time, so the runtime for summing two inputs must be $\Theta(n)$.

This is much better than the finger-counting approach, and actually is the most efficient known algorithm for addition!

## Multiplication

$(\forall x,y)(A_{mul}(x,y) \to x \cdot y)$

### Some naive approaches

If, like for addition, we are trying to multiply x and y together and simply add $x$ a total of $y$ times, then the efficiency has an upper bound runtime of $O(10^n \cdot n)$ where $n$ is the cost to add $x$ one time.

So let's consider doing long multiplication, where we multiply each digit of $x$ individually with $y$, and add them all up:

![[/cs170/img/Algorithms-for-Integer-Arithmetic/Untitled 1.png]]

This becomes $O(n^2)$ since 

> 💡 The formal definition of Big O is: $O(f(n)) \iff \exists c,N (\forall n \ge N)(T(N) \le c \cdot f(n))$

### Karatsuba Multiplication

This is an example of a powerful technique called **divide and conquer.** 

The main premise of this algorithm is a recursive way to break down a number into smaller bits, and multiplying those bits all together using distribution.

For example: 

![[/cs170/img/Algorithms-for-Integer-Arithmetic/Untitled 2.png]]

If we are trying to get $x \cdot y$:

$x \cdot y = (x_H \cdot 10^{n/2} + x_L)(y_H \cdot 10^{n/2} + y_L)$

Distributing this yields:

$x \cdot y = x_H \cdot y_H \cdot 10^n + (x_H y_L + x_Ly_H) \cdot 10^{n/2} + x_Ly_L$

If the number is larger than 4 digits, we can continue applying this by breaking down the 'high' and 'low' even further into their own two parts.

**Runtime:**

For a single operation, the runtime will be $O(c \cdot n)$ 

The recursive tree structure will look something like this:

![[/cs170/img/Algorithms-for-Integer-Arithmetic/Untitled 3.png]]

Each node splits into four smaller numbers ($x_H, x_L, y_H, y_L$). There are $log_2(n)$ layers total, and a single layer $i$ has a runtime of $2^i c \cdot n$.

So the total runtime is:

$$
⁍
$$

If we recall the geometric sum formula,

$$
\sum_{i=0}^{log_2(n)} 2^i = \frac{2^{log_2(n)+1} - 1}{2 - 1} \le 2n
$$

Plugging this back into the original runtime equation yields a runtime

$O(2n^2 \cdot c) \equiv O(n^2)$

Oops! This isn't any better. But it's directly related to a much better algorithm:

### Better than $n^2$?

If we realize that **we don't actually need to compute** $x_Hy_L$ **and** $x_L y_H$ **since we only need their sum,** we can do this instead:

1. Compute Karatsuba($x_H, y_H$). (A)
2. Compute Karatsuba $(X_L, Y_L)$ (B).
3. Compute Karatsuba $(x_H + x_L, y_H + y_L)$ (C).
4. Find the original Karatsuba($x, y$) as $A \cdot 10^n + (C - A - B) \cdot 10^{n/2} + B$.

What does this do? Well, it makes the branching factor **3** instead of **4.** 

Since there is a $(3/2)^{log_2(n)}$ factor in the calculation now, it doesn't simplify as nicely. But it becomes $O(n^{log_2(3)})$ which is less than $O(n^2)$ ($log_2(3)$ is about $1.58$.