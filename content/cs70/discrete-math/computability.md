---
title: "Computability"
weight: 999
---

Computability is the study of a massively important question:  **do there exist any problems that are impossible for a computer to solve?**

## **The Halting Problem**

It turns out that the above question itself is impossible to solve: in other words, **there cannot exist a program HALT which determines if a program can halt in finite time given a particular input.**

This was originally proposed by Alan Turing- he proved the nonexistence by attempting to feed the Halting Problem into itself: if the Halting Problem doesn't halt, then it is supposed to output an answer. That means that the Halting Problem would state that the Halting Problem halts, even though it didn't. This paradox led to demonstrating that the Halting Problem simply cannot be solved.

<iframe
    width="640"
    height="480"
    src="https://www.youtube.com/embed/macM_MtS_w4"
    frameborder="0"
    allow="encrypted-media"
    allowfullscreen
>
</iframe>

## Reductions

**Reducing** a problem A to another problem B means that we can solve problem A if we know how to solve problem B.

For instance, we might be able to write psuedocode that has a whole bunch of known components, but rely on the output of problem B in order to determine the final output.

One application of reduction is to show that **a program cannot exist if it requires the Halting Problem as a component.**
