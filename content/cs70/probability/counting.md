---
weight: 10
---

## Introduction

If you're reading this, I think it's safe to assume you already know how to count... (1, 2, 3, whatever) so what's the big deal about counting?

When we say counting in this context, we mean **counting sequences of decisions.** For example, we might want to get the **total number of ways to choose toppings on a pizza** or something.

There are **two main types** of problems: those where **order matters** and those where it doesn't.

## The First Rule of Counting: When the order matters

Here's a sample problem: let's try to figure out the total number of unique 5-character strings we can make with the letters 'A' through 'E'. For instance, 'ABCDE' and 'DABBA' are both valid.

Lots of these types of problems can be visualized using **slots,** where each slot is one character or option: ****

****![](<../img/assets/image (19) (1).png>)****

To get the total number of ways to fill the slots, we can **multiply the number of ways each individual slot can be filled together.**

So for the problem above, we get that there are 5 ways to fill each slot, and 5 slots in total. So, $5 \times 5 \times 5 \times 5 \times 5 = 3125$strings.

## **The Second Rule: When the order doesn't matter**

In order to tackle these types of problems, we'll need to introduce the **combinatorial** $\binom{n}{k} = \frac{n!}{k!(n-k)!}$. When you see this, it means "the number of ways we can choose $n$things from $k$total elements if order doesn't matter".



## Stars and Bars

<iframe
    width="640"
    height="480"
    src="https://www.youtube.com/embed/UTCScjoPymA"
    frameborder="0"
    allow="encrypted-media"
    allowfullscreen
>
</iframe>

When we need to split items into groups, it's sometimes nice to add **bars** that separate the items. This is great if there are particular classes of items rather than unique ones (if they're unique, just use slots.)

How this works is that we can treat each item as a **star**, and the stars are separated by **bars** that designate one group from another.

This means that if there are $n$stars and $k$groups, then there must be $\binom{n+k-1}{k-1}$total ways to split the stars into groups.

One application of this is to get the total number of equations $y_0 + y_1 + \cdots + y_k = n$for a fixed $n$. We can think of there being $n$number of ones (our stars), and $k$number of plus signs (our bars). There can also be an empty group (representing $y_i = 0$), which bumps us up to $k+1$groups. By the Stars and Bars principle, there are $\binom{n+k}{k}$such equations for non-negative numbers.

## The Inclusion-Exclusion Principle

Used to calculate the probability of the union of events.

[http://prob140.org/textbook/content/Chapter\_05/02\_Inclusion\_Exclusion.html](http://prob140.org/textbook/content/Chapter\_05/02\_Inclusion\_Exclusion.html)
