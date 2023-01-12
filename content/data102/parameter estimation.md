---
weight: 40
---


Suppose we observe $n$ data points ($x_1$ to $x_n$).
Let $\theta$ be some unknown parameter that describes the distribution the data points were sampled from.

As an example, let's say we are trying to quantify how good a product is based on how many positive and negative reviews it has.
 - This means that data $x_i$ is either $0$ (bad review) or $1$ (good review)
 - Let $p(x_i | \theta) = \theta^{x_i} (1-\theta)^{1-x_i}$. This means that reviews are positive with probability $\theta$, and negative with probability $1-\theta$.


## Maximum Likelihood Estimation (MLE)
[http://prob140.org/textbook/content/Chapter_20/01_Maximum_Likelihood.html](http://prob140.org/textbook/content/Chapter_20/01_Maximum_Likelihood.html)


In a Frequentist approach, $\theta$ is fixed, so our goal is to find the best estimate for $\theta$ using the data given.

Recall that **likelihood** is the probability of the data given the parameter, $$p(x_i | \theta)$$


**Goal:** Given an iid sample of $N$ points $x_1, \cdots, x_N$, and a distribution described by a parameter $\theta$, what’s the value of $\theta$ that gives the highest probability of this set of points occurring in the probability distribution? (i.e. we want to maximize likelihood value)

- Formal definition: find $\theta$ that maximizes $L(\theta) = \prod_{i=1}^N P_\theta(x_i)$, where $P_\theta$ is the probability of one data point $x_i$ occurring given a value of $\theta$.
- $MLE(\theta | X=x) = argmax_\theta P(X=x|\theta) = argmax_\theta \ln P(X=x | \theta)$
- Occurs when $\frac{\partial}{\partial \theta} L(\theta) = 0$
- Calculating derivatives of products is pain, so we can monotonically transform the likelihood function using $\log$. Since $\max(f(x)) = \max(\log(f(x))$ we can find the maximum of the **log likelihood function:** $\log L(\theta)$

Using MLE to predict CPT values given data points:

- $P(Y=y) = MLE(\theta | (X,Y))$ = (# data points with $X=x$) / (# data points total)
- $P(X=x|Y=y) = MLE(\theta | (X,Y))$ = (# data pooints where ($X=x, Y=y$) ) / (# data points where $Y=y$)

## Bayesian Parameter Estimation
Now, $\theta$ is random. We then need to specify a **prior** $p(\theta)$ that represents what we believe the distribution for $\theta$ might look like.

In a Bayesian approach, we calculate the **posterior** distribution $p(\theta|x)$, which is an update to the prior now that we have observed some data.

Through Bayes' Rule, $p(\theta|x) = \frac{p(x|\theta)p(\theta)}{p(x)}$.
 - $p(x|\theta)$ is the likelihood.
 - $p(\theta)$ is the prior.
 - $p(x) = \int p(x|\theta)p(\theta)d\theta$. This integral is often impossible to compute, especially for high-dimensional data. 

Rather than needing to compute $p(x)$, we can simply state that $p(\theta|x)$ is proportional to the likelihood times the prior, $p(x|\theta)p(\theta)$.


A convenient choice for the prior is the Beta distribution.

$$p(\theta) \propto \theta^{\alpha - 1}(1-\theta)^{\beta - 1} = Beta(\alpha,\beta)$$
The Beta(1,1) distribution is equivalent to the Uniform distribution.


Given that the data $x_i$ are sampled from a Bernoulli($\theta$) distribution, which has a likelihood function $p(x|\theta) = \theta^{k} (1-\theta)^{n - k}$ (where $k$ is the number of positive values out of $n$ total values), and a prior of Beta($\alpha, \beta)$, we can compute the posterior as such:
$$p(\theta|x) \propto p(x|\theta)p(\theta) \propto (\theta^{k} (1-\theta)^{n - k}) \cdot (\theta^{\alpha - 1}(1 - \theta)^{\beta - 1})$$
$$\propto \theta^{k+\alpha-1} (1-\theta)^{n-k+\beta - 1}$$
which is a $Beta(k + \alpha, n-k+\beta)$ distribution.



## Maximum A Posteriori (MAP)
Point estimators, one of which is the MAP method, reduce a posterior distribution into a single number.

We can calculate it as the argmax of the posterior with respect to $\theta$, i.e. the value of $\theta$ that gives us the largest value for the posterior.

MAP is analogous to the mode of the distribution.


## Minimum Mean-Squared Error (MMSE)
MMSE is another point estimator that finds the value of $\theta$ that gives the smallest mean squared error:

$$\hat\theta = argmax_{\hat\theta} E_{\theta|x} (\hat\theta - \theta)^2$$
MMSE is analogous to the mean of the distribution.


## Example: Estimating the Mean with Gaussian (Normal) Likelihood
Suppose we're given that $n$ people have heights $x_1, \cdots, x_n$ distributed normally.
We're trying to find $\mu$, which is the population mean.

Then, the likelihood $p(x_i | \mu) = N(x_i; \mu, \sigma)$ describes the probability of getting any one height given the mean.

Under a frequentist approach, we can calculate the MLE to be $\hat\mu_{MLE} = \frac{1}{n} \sum_{i=1}^n x_i$.

Under a Bayesian approach, we're trying to find the posterior $p(\mu | x) \propto p(x | \mu) p(\mu)$.

If the likelhiood and prior ar both normal, then the posterior is also normal. This (along with the beta example with Bernoulli distributions) is an example of a **conjugate prior**: in general, conuugate priors have the same family as the posterior.

