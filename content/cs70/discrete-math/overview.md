---
title: "Discrete Math Overview"
weight: -1
---

## What even is discrete math?

According to [Wikipedia](https://en.wikipedia.org/wiki/Discrete\_mathematics), "_Discrete mathematics_ is the study of mathematical structures that are fundamentally discrete rather than continuous." Very helpful, thank you Wikipedia. The floor is indeed made of floor rather than sky.

The word **discrete** means "distinct" or "countable". This suggests that discrete math has to do with **countable numbers** like integers, rather than the continuous $f(x)$functions we're used to seeing that are defined for any real$x$, even ones we don't know the exact value of like $\pi$.

Dealing with countable integers is nice because **that's how computers work.** Behind the scenes, every floating point number is actually just a whole bunch of bits, which are countable :) I would say that dealing with integers makes things nicer too (since we no longer have to deal with decimals), but you might be inclined to disagree.

## A brief summary of the contents covered

Discrete math is an extremely wide field of mathematics. Here, we'll be covering the basics as well as a few important applications:

* [**Propositional logic**](propositional-logic.md) and sets give us the **language** we need to talk about discrete math.
* ****[**Proofs**](proofs.md) **** allow us to demonstrate **how** and **why** things work the way they do.
* [**Stable Matching**](stable-matching.md) explores how we can apply sets to create optimal matches between two groups with preferences.
* [**Graph theory** ](classes/cs70/discrete-math/graphs.md)provides a highly visual representation of a wide variety of mathematical relationships using vertices, edges, and faces. One of the most important concepts here is **Euler's Formula** which relates the number of vertices, edges, and faces together.
* ****[**Modular arithmetic** ](modular-arithmetic.md)explores what happens when when all numbers are remainders of dividing itself by another number. There are some really important theorems here, like the **Chinese Remainder Theorem, Euclid's Algorithm,** and **Fermat's Little Theorem.**
* ****[**RSA Cryptography**](rsa-cryptography.md) **** is an interesting application of how modular arithmetic is used to encrypt and decrypt messages using a public-private key pair.
* [**Polynomials** ](polynomials.md)can be used in a discrete sense to create **secret sharing** schemes, and can be recovered from points using **Lagrange Interpolation.**
