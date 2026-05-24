---
title: "Number Representation"
weight: 10
---

## Bases and Bits

In Arabic numerals, we use **base 10**. So for example, $533 = 5 \times 10^2 + 3 \times 10^1 + 3 \times 10^0$.

There are also other common bases, where we multiply each digit by a different value. The most common are **binary (base 2), octal (base 8), and hexadecimal (base 16).**

> 💡 **Bits are bits.** They can represent literally whatever you want!

> 🔥 With $n$ bits, we can represent $2^n$ different things!

## Signed and Unsigned Integers

Integers can either be **unsigned** (positive only) or **signed** (positive or negative).

In a signed integer, the left-most bit is reserved as the **sign bit** where **0 is positive** and **1 is negative.**

There are some helpful properties we'd like signed numbers to follow:

- There should be a **single zero** (where all bits are 0).
- The zero should be treated as **positive.**
- Half of the numbers should be greater than 0, and the other half should be less.

### Two's Complement

One of the most common representations for negative numbers is Two's Complement, which makes operations like addition much more intuitive.

In Two's Complement, **the sign bit has negative weight.** In other words, we take the largest possible number and **subtract** the numerical portion from that largest amount.

An easy way to compute Two's Complement is to **invert all bits and add 1.** 

For an example, let's try to find the bit representation of $-3$.

$3_{ten} = 0011_{two}$

Invert all bits:

$1100_{two}$

Add one:

$1101_{two} = -3_{ten}$

### Binary Addition

Adding two positive numbers is straightforward- same process as base 10:

![[/cs61c/img/Number-Representation/Untitled.png]]

Adding negative numbers works too. There is a **carry out bit** if the result has more bits than we have available.

![[/cs61c/img/Number-Representation/Untitled 1.png]]

If the result is greater than the largest possible number the bits can store, an **overflow** occurs and the number wraps around:

![[/cs61c/img/Number-Representation/Untitled 2.png]]