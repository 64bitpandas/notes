---
weight: 30
---

So far, in [[binary decision making]] and [[hypothesis testing]], we've explored how to make as few mistakes as possible when making binary predictions.

## Intro to Decision Theory
We can generalize a decision problem to the following:
 - Suppose there is some unknown quantity of interest $\theta$.
	 - $\theta$ is random under a Bayesian approach, and fixed if frequentist.
 - We collect/observe some data $X$.
 - There is some true distribution that the data is drawn from, $p(X | \theta)$.
 - We are tasked to create a good **estimator** $\delta(x)$ (also known as $\hat\theta$, which makes decisions based on the data.
 - In order to quantify how good/bad our estimator is, we can use a loss function $l(\delta(x), \theta)$, where higher loss values are worse.


## Loss Functions
### 0/1 Loss
In the case of binary decisions:
 - $\theta$ is either $0$ or $1$ and represents our reality.
 - $\sigma(x)$ is also either $0$ or $1$ and represents our decision.
 - A very simple loss function is to return $0$ if the decision matches reality, $1$ otherwise. This is known as **0/1 Loss**.

### L2 Loss
If our data is continuous, then 0/1 loss cannot be used.
Instead, we can define the loss as follows:
$$ l(\sigma(x), \theta) = (\sigma(x) - \theta)^2$$
This is known as $L_2$ loss.


## Applying Loss Functions

### Frequentist Risk
Under frequentist assumptions, the risk of choosing $\theta$ is equivalent to the expectation of the loss function:
$$R(\theta) = E_{x|\theta}[l(\sigma(x), \theta)] = \int l(\sigma(x), \theta) p(x|\theta) dx$$
In other words, take the average loss for every possible value, and weight it by how likely it is to get that value.


### Bayesian Posterior Risk
Syntactically, Bayesian risk looks very similar to frequentist risk:
$$\rho(\theta) = E_{\theta|x}[l(\sigma(x), \theta)] = \int l(\sigma(x), \theta) p(\theta|x) d\theta$$
The main difference is that rather than iterating over every possible value of data weighted by its probability, we iterate over every possible distribution weighted by how likely it is to get our data from it.

### Bayes Risk
$$E_{\theta, x}[l(\sigma(x), \theta)] = E_\theta[E_{x|\theta}[l(\sigma(x), \theta)]] = E_x[E_{\theta|x}[l(\sigma(x), \theta)]]$$
Bayes risk is the joint expectation of the loss function over all possible data and distributions. It can be represented using either the Frequentist risk or the Bayesian posterior risk.




### Bias-Variance Decomposition

Below is the calculation for the frequentist risk of the L2 loss function:
$$
\begin{align}
R(\theta) 
&= E_{x|\theta}\Big[\big(
    \delta(x) - E_{x|\theta}[\delta(x)] + E_{x|\theta}[\delta(x)] - \theta
\big)^2\Big] \\
&= E_{x|\theta}\Big[\big(
    \delta - \bar{\delta} + \bar{\delta} - \theta
\big)^2\Big] \\
&= E_{x|\theta}\Big[
    \big(\delta - \bar{\delta}\big)^2 +
    \underbrace{2\big(\delta - \bar{\delta}\big)\big(\bar{\delta} - \theta\big)}_{=0} + 
    \big(\bar{\delta} - \theta\big)^2
\Big] \\
&= E_{x|\theta}\Big[\big(\delta - \bar{\delta}\big)^2\Big] + 
     E_{x|\theta}\Big[\big(\bar{\delta} - \theta\big)^2\Big] \\
&= \underbrace{E_{x|\theta}\Big[\big(\delta - \bar{\delta}\big)^2\Big]}_{\text{variance of }\delta(x)} + 
     \big(\underbrace{\bar{\delta} - \theta}_{\text{bias of }\delta(x))}\big)^2 \\
\end{align}
$$
The **variance** of the estimator is a measurement for how spread out the data is when compared ot the average. Larger variance means that the model is more sensitive to randomness in the data.

The **bias** of the estimator is a measurement for how far the average of the estimator is from the true value of $\theta$. In other words, if we average out all of the randomness in the data, how close is our model to reality?


If the estimator were perfect, then the expectation of $\delta - \theta$ should be $0$, which would make the bias $0$.

