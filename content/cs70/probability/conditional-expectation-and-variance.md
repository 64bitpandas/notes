---
weight: 90
---

Properties:

### Conditional Expectation

$E(X|Y)$is the conditional expectation of $X$given $Y$

* $E(X|Y=y)$is a fixed value, but $E(X|Y)$is a random variable \(it is a function of $Y$\)
* Iterated expectation: $E(E(X|Y)) = E(X)$
* Additivity: $E(Y+Z | X) = E(Y|X) + E(Z|X)$
  * **does not work** on the right hand side: $E(Y | X+Z) \ne E(Y|X) + E(Y|Z)$
* Linearity: $E(aX + b | Y) = aE(X|Y) + b$
* Conditioning on the same variable: $E(g(S)T | S) = g(S)E(T|S)$

### Conditional Variance

If $Var(Y)$is difficult to find directly, we can use the **variance decomposition** to condition the variance on another variable.

$
Var(Y) = E(Var(Y|X)) + Var(E(Y|X))
$



