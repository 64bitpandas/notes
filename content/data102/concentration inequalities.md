---
weight: 100
---

The goal of concentration inequalities is to provide bounds on the probability of a random variable taking values in its tail (regions farthest away from the mean).

This is especially useful when we don't know the distribution of a random variable, or we have a combination of other random variables (sample mean, quicksort, multi-arm bandit...).

## Markov's Inequality
If $X$ is a non-negative random variable with expectation $\mu$, then
$$P(X \ge t) \le \frac{\mu}{t}$$

## Chebyshev's Inequality
If we know the mean $\mu$ and the variance $\sigma^2$ of a random variable $X$, then the probability of a result being $t$ standard deviations away from the mean can be expressed as
$$P(|X - \mu| \ge t \sigma) \le \frac{1}{t^2}$$
Alternatively,
$$P(|X - \mu| \ge c) \le \frac{\sigma^2}{c^2}$$


## Chernoff Bound


$$P(X \ge t) = P(e^{\lambda X} \ge e^{\lambda t}) \le \frac{E[e^{\lambda x}]}{e^{\lambda t}}$$
Optimized form:
$$P(X \ge c) \le min_{t > 0} M_X(t) e^{-tc}$$

where $M_X(t) = E(e^{tX})$ (moment generating function)


## Hoeffding's Inequality
Hoeffding's inquality is a special case of the Chernoff bound where the bounds of a random variable are known.

**Hoeffding's Lemma:** if $X$ is a bounded random variable between $a$ and $b$ with mean $\mu$, then 
$$M_X(t) \le \exp(\frac{(b-a)^2}{8} \lambda^2 + \mu \lambda)$$

**Hoeffding's Inequality:** If we have $n$ independent (may not be identically distributed) bounded random variables between $a$ and $b$, 
$$P(\frac{1}{n} \sum_{i=1}^n (X_i - E(X_i)) \ge t) \le \exp(-\frac{2nt^2}{(a-b)^2})$$

### Proof
Let $Y$ be $\frac{1}{n} \sum_{i=1}^n (X_i - E(X_i))$. Then, the MGF $E[e^{\lambda Y}]$ = $E[\exp(\lambda/n \sum_{i=1}^n X_i)]$.

Using the properties of exponentials (exponential of sum is product of exponentials),
$E[e^{\lambda Y}] = E[\prod^n_{i=1} exp(\lambda/n X_i)]$.

Using independence rules, $E[\prod^n_{i=1} exp(\lambda/n X_i)] = \prod_{i=1}^n E[exp(\frac{\lambda}{n} X_i)]$

Using Hoefding's Lemma, the MGF must then be bounded by $\prod_{i=1}^n\exp(\frac{(b-a)^2}{8} \lambda^2 + \mu \lambda)$.



