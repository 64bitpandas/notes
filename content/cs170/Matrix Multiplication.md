---
title: "Matrix Multiplication"
weight: 30
created: "January 19, 2021 9:26 AM"
---

### General Method

If we were just to multiply two matrixes by hand (let's say we are trying to find $XY$), then we would need to multiply the $i$th row of $X$ with the $j$th column of $Y$ to get the $i,j$ position of the result $Z$.

![[/cs170/img/Matrix-Multiplication/Untitled.png]]

### Naive Algorithm

A straightforward way of going by this is simply to loop through every possible value of $i$ and $j$:

```python
for i in range(n):
	for j in range(n):
		for k in range(n):
			z[i][j] += x[i][k] * y[k][j]
```

This has a runtime of $O(n^3)$. Oof.

### Recursive Algorithm

Let's try employing divide and conquer to make this problem better! Instead of doing each row and column individually, what if we split up the matrix into smaller matrices:

![[/cs170/img/Matrix-Multiplication/Untitled 1.png]]

By the general form of the recurrence relation, we can write the runtime as:

$T(n) = 8T(n/2) + O(n^2)$

since we are splitting the work into 8 separate matrix multiplications ($AE, BG...$) and the dimension of each subpart is $n/2$. We then require $n^2$ time to put these parts back together.

If we let $a=8$,  $b=2$, and $d=2$, then by the Master Theorem $O(n) = n^{log_b(a)} = n^{log_28} = n^3$. Whoops...

### Strassen's Algorithm

![[/cs170/img/Matrix-Multiplication/Untitled 2.png]]

Somehow, if we rewrite the products as such, we only need to compute 7 products rather than 8!

This means that the Master Theorem should evaluate to $O(n^{log_27})$ which is about $n^{2.81}$. This is less than $n^3$ so it's an improvement (albeit a small one).