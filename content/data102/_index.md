---
title: "Data 102: Inference"
BookCollapseSection: true
---

## Data102 Notes

Here are my notes for the Fall 2022 offering of [Data 102](https://data102.org/), Berkeley's Inference for Data Science course.

Data 102 explores two major concepts: **making decisions under uncertainty** and **modeling the real world**. This is all about making assumptions-- here are some definitions:
 - **Frequentist:** $y$ (data) is random, $\theta$ (parameter) is fixed
 - **Bayesian:** $y$ is random, $\theta$ is random
 - **Parametric:** Make assumptions about the relationship between $\theta$ and $y$, then use these assumptions to find the best value of $\theta$ given $y$
 - **Nonparametric:** Don't make any assumptions, and find any good function $f$ such that $\theta = f(y)$

## Table of Contents
 - [[Binary Decision Making]]: Confusion matrix, sensitivity, specificity, TPR/FPR/FNR/FDP etc.
 - [[Hypothesis Testing]]: Null/alternative hypotheses, multiple hypothesis testing, controlling FWER/FDR, online decision making, likelihood ratios
 - [[Decision Theory]]: Loss functions, risk, bias-variance tradeoff
 - [[Parameter Estimation]]: Likelihood, MLE, Bayesian parameter estimation, Bayesian hierarchical models
 - [[Sampling]]: Markov chains, MCMC, Metropolis-Hastings, Rejection sampling, Gibbs sampling
 - [[Regression and GLMs]]: Generalized linear models, posterior predictive check
 - [[Nonparametric Methods]]: K-Nearest Neighbors, decision trees, random forests, neural networks, gradient ascent/descent
 - [[Interpretability]]: Interpretability, explainability
 - [[Causality]]: Colliders, confounders, structural causal models, risk ratios, potential outcomes framework
 - [[Concentration Inequalities]]: Markov, Chebychev, Chernoff, Hoeffding
 - [[Bandits]]: Multi-Armed Bandit Framework, UCB/ETC, Thomson Sampling, Regret
 - [[Markov Decision Processes]]: Value iteration, Q-value iteration, Policy iteration
 - [[Reinforcement Learning]]: Q-Learning

 
## How to contribute

See the [contributing guide](/contributing) for more details!

For the most part, these notes should be pretty complete in terms of content, but could use some cleaning up (as well as more examples).

#### Credits

* [Ben Cuan](https://github.com/64bitpandas)






