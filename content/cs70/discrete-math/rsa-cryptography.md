---
title: "RSA Cryptography"
weight: 960
---

## Introduction

The internet is built upon the fact that stuff needs to go from point A to point B quickly, accurately, and securely. We'll talk about the **secure** part of that now (the accurate part will be addressed [soon](/cs70/discrete-math/polynomials.md)!).

One of the ways we can make sure our top-secret messages can't get intercepted is to **encrypt** them- mix them up to become incomprehensible using some secret code, then decrypt it at the other end. This has a major problem though- how can you agree to use the same secret code as someone else if you've never met them before?

**RSA** (named after creators Rivest, Shamir, Adleman) is an encryption scheme that takes advantage of **public keys** to solve this very problem. In the RSA system, everyone broadcasts their public key all over. When encrypting a message, the sender can lock their message using their **private key** paired with the _sender's_ public key, such that only the sender themselves can unlock the message using their own private key.

This poses yet another problem: how can we choose these public and private keys so that they work nicely with each other? Well, we can use modular arithmetic of course!! :smile:

## The RSA Cheat Sheet

**Variables:**\
 **-**$p, q$are two distinct prime numbers.\
 **-** $e$is relatively prime to $(p-1)(q-1)$.\
 **-** $N = pq$\
 \- $x$is the original message; $y$is the encrypted message

**Public Key:** $(N, e)$\
**Private Key:** $d = e^{-1} \pmod{(p-1)(q-1)}$****

**Encryption:** $E(x) = x^e \pmod{N}$\
**Decryption:** $D(y) = y^d \pmod{N}$****

****

## Example

Let our two prime numbers be $p = 5, q = 11$. (In the real world, these would be much larger for security purposes- but let's not make this too hard on ourselves!)

The first step is to **choose our public key.** We know e must be relatively prime to $(p-1)(q-1) = (4)(10) = 40$. A small number that satisfies this is $3$, so we can go ahead and use that. Therefore, our public key is $(N, e) = (55, 3)$.

The next step is to **compute the private key.** Using the formula,  $d = 3^{-1} \pmod{40}$. We could use [Euclid's Extended Algorithm](/cs70/discrete-math/modular-arithmetic.md#using-euclids-extended-algorithm-for-inverses) to compute this value, which ends up being $27$. Therefore, $d = 27$.

After we have computed our keys, we must **encrypt the message.** This yields $y = x^3 \pmod{55}$for some arbitrary message $x$.

Finally, we must **decrypt the message** by passing $y$into the decryption formula. This yields $x = y^{27} \pmod{55}$.

If all goes well, the decrypted message should be the same as the original message!
