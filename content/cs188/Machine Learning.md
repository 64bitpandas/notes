---
title: "Machine Learning"
weight: 90
---

## What is Machine Learning?

So far, we’ve used Bayes’ Nets, Markov Decision Processes, etc. to solve models. But how do we actually determine what those models are in the first place?

This is where machine learning comes in: the process of improving models through experience. There are two different categories of algorithms: **supervised learning,** where relationships are inferred between given input and output data to predict outputs for new inputs, and **unsupervised learning,** where no outputs are given and the algorithm recognizes structures or patterns in the inputs. ****

# Naive Bayes

Naive Bayes is an example of a classification algorithm that sorts data into categories.

First, features need to be extracted.

- Features are any information that can be represented as data.
- Feature engineering can be used to apply feature functions to inputs.

Given existing data points $X = \{X_1, \cdots, X_n\}$ and labels $Y$, predict $P(Y=y|X=x)$ for a new data point $(X,Y)$.

- Given a list of features $f_1, \cdots, f_n$, a prediction for the label can be calculated using $prediction(f_1, \cdots, f_n) = \argmax_y P(Y=y) \prod_{i=1}^n P(F_i = f_i | Y = y)$. The CPT’s for all of these features will need to be learned using parameter estimation, such as Maximum Likelihood Estimation.

### Maximum Likelihood Estimation

[http://prob140.org/textbook/content/Chapter_20/01_Maximum_Likelihood.html](http://prob140.org/textbook/content/Chapter_20/01_Maximum_Likelihood.html)

**Goal:** Given an iid sample of $N$ points $x_1, \cdots, x_N$, and a distribution described by a parameter $\theta$, what’s the value of $\theta$ that gives the highest probability of this set of points occurring in the probability distribution? (i.e. we want to maximize likelihood value)

- Formal definition: find $\theta$ that maximizes $L(\theta) = \prod_{i=1}^N P_\theta(x_i)$, where $P_\theta$ is the probability of one data point $x_i$ occurring given a value of $\theta$.
- $MLE(\theta | X=x) = argmax_\theta P(X=x|\theta) = argmax_\theta \ln P(X=x | \theta)$
- Occurs when $\frac{\partial}{\partial \theta} L(\theta) = 0$
- Calculating derivatives of products is pain, so we can monotonically transform the likelihood function using $\log$. Since $\max(f(x)) = \max(\log(f(x))$ we can find the maximum of the **log likelihood function:** $\log L(\theta)$

Using MLE to predict CPT values given data points:

- $P(Y=y) = MLE(\theta | (X,Y))$ = (# data points with $X=x$) / (# data points total)
- $P(X=x|Y=y) = MLE(\theta | (X,Y))$ = (# data pooints where ($X=x, Y=y$) ) / (# data points where $Y=y$)

### Laplace Smoothing

Prevent overfitting due to outliers by adding in an extra hyperparameter $k$ into the probability:

$P_L(X=x)$ = (# data points where $X=x)$ + $k$ / (total # of data points + $k |X|$) where $|X|$ is the number of possible values of $X$.

- Smaller $k$ = more consistent with data ($k=0$ is just MLE), larger $k$ = more uniform distribution ($k \to \infty$ is just a uniform)

 

# Supervised Learning

**Goal:** learn an unknown target function $f$

- Input: training set of labelled examples $(x_j, y_j)$ such that $y_j = f(x_j)$
- Output: hypothesis $h$ that is close to $f$ (used to predict accurately on test set)

The hypothesis $h$ can come in many forms (linear, logistic, neural net, decision tree...)

**Classification:** learning $f$ with discrete output values

**Regression:** learning $f$ with real-valued output values

**Measuring success:**

- Which hypothesis space $h$ do we use?
- How do we measure degree of fit?
- How do we trade off degree of fit to complexity?
- How do we find $h$ given $H$?

## Linear Regression

In linear regression, our hypothesis comes in the form

$$
h_w(\bold{x}) = w_0 + w_1 x_1 + \cdots + w_n x_n = \bold{w^T x}
$$

The loss function of the hypothesis $h_w$ can be found using the following equation:

$$
Loss(h_w) = \frac{1}{2} ||\bold{y - Xw}||^2 = \frac{1}{2} \sum_j (y_j - h_w(x_j))^2
$$

where $\bold{y}$ is a vector of true labels, $\bold{w}$ is a vector of weights, and $\bold{X}$ is a vector of feature vectors.

## Perceptrons

Perceptrons are classifiers that find a decision boundary that perfectly separates the training data into categories.

**Perceptron Convergence Theorem:** if the points are linearly separable, the perceptron algorithm is guaranteed to find a perfect separator.

1. Initialize all weights to 0
2. For each training sample:
    1. Classify the sample using the current weights: $y = 1$ if $w^T f(x) > 0$, $-1$ otherwise. (dot product weights with features)
    2. If the predicted label $y$ is different from the actual label $y^*$, then update weights using $w ← w + y^* f(x)$.

#