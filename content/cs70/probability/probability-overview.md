---
weight: -1
---

The probability section of this guide will likely never be fully completed, due to the fact that the [Prob 140 textbook](http://prob140.org/textbook/content/README.html) is such an excellent resource in probability theory. Go read it and do the problems!

Instead of a full write-up, the pages in this section will typically just link to relevant sections from the textbook. Personally, I found everything I needed to do well in CS70 probability (and much more) here, including examples that are very similar to problems you might see on the homework.

TL;DR don't use this section of the guide, just read the 140 textbook.

Here is a running list of topics in this section:

* [**Counting**](/cs70/probability/counting.md) provides us an intuitive method of figuring out how many possible ways there are to do something.
* [**Discrete probability distributions**](/cs70/probability/discrete-probability.md), such as the Binomial or Geometric distributions, describe the probabilities of a finite set of outcomes.
* [**Continuous probability distributions**](/cs70/probability/continuous-probability.md), such as the Poisson or Normal distributions, help us model real values, like lifetime or height.
* [**Markov chains**](/cs70/probability/markov-chains.md) model transitions between discrete states.
* [**Expectation and variance**](/cs70/probability/expectation-and-variance.md) are tools to describe the characteristics of a random variable or distribution.
* [**Concentration inequalities**](/cs70/probability/concentration-inequalities.md) allow us to approximate bounds for random variables when we only know their expectation and/or variance.

There is far more to explore in learning the basics of probability- not everything is included in this list!

### Reference

[http://prob140.org/assets/final\_reference\_fa18.pdf](http://prob140.org/assets/final\_reference\_fa18.pdf)

| Distribution                                                                                              | Values               | Density                                                      | Expectation           | Variance                                   | Links |
| --------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------ | --------------------- | ------------------------------------------ | ----- |
| Uniform(m,n)                                                                                              | \[m, n]              | $\frac{1}{n-m+1}$                                          | $\frac{m+n}{2}$     | $\frac{(n-m+1)^2-1}{12}$                 |       |
| <p>Bernoulli(p)</p><p>Indicator</p>                                                                       | 0, 1                 | <p>P(X=1) = p</p><p>P(X=0) = 1-p</p>                         | $p$                 | $p(1-p)$                                 |       |
| Binomial(n,p)                                                                                             | \[0, n]              | $\binom{n}{k}p^kq^{n-k}$                                   | $np$                | $np(1-p)$                                |       |
| Poisson($\mu$)                                                                                          | $x\ge0$            | $e^{-\mu}\frac{\mu^k}{k!}$                                 | $\mu$               | $\mu$                                    |       |
| Geometric(p)                                                                                              | $x \ge 1$          | $(1-p)^kp$                                                 | $\frac{1}{p}$       | $\frac{1-p}{p^2}$                        |       |
| Hypergeom.(N,G,n)                                                                                         | \[0, n]              | $\frac{\binom{G}{g}\binom{B}{b}}{\binom{N}{n}}$            | $n\frac{G}{N}$      | $n\frac{G}{N}\frac{B}{N}\frac{N-n}{N-1}$ |       |
| Uniform Continuous                                                                                        | (a, b)               | $\frac{1}{b-a}$                                            | $\frac{a+b}{2}$     | $\frac{(b-a)^2}{12}$                     |       |
| Beta(r,s)                                                                                                 | (0, 1)               | $\frac{\Gamma(r+s)}{\Gamma(r)\Gamma(s)}x^{r-1}(1-x)^{s-1}$ | $\frac{r}{r+s}$     | $\frac{rs}{(r+s)^2(r+s)}$                |       |
| <p>Exponential(<span class="math">\lambda</span>)</p><p>(Gamma(1, <span class="math">\lambda</span>))</p> | $x\ge0$            | $\lambda e^{-\lambda x}$                                   | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$                    |       |
| Gamma(r, $\lambda$)                                                                                     | $x\ge0$            | $\frac{\lambda^r}{\Gamma(r)}x^{r-1}e^{\lambda x}$          | $\frac{r}{\lambda}$ | $\frac{r}{\lambda^2}$                    |       |
| Normal(0,1)                                                                                               | $x \in \mathbb{R}$ | $\frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}x^2}$                 | 0                     | 1                                          |       |

Where $\binom{n}{k} = \frac{n!}{k!(n-k)!}$and $\Gamma(r) = \int_0^\infty x^{r-1}e^{-x}dx = (r-1)\Gamma(r-1) = (r-1)!$
