---
weight: 110
---

**Main idea:** making repeated decisions based on feedback, factoring in the tradeoff between exploring new decisions or keeping existing good decisions

### Multi-Armed Bandit Framework
The Multi-Armed bandit problem arises when the following are true:
 - We need to get the data as a part of the process
 - Exploration/exploitation tradeoff (both have a cost)
 - Stochastic: rewards are random

**Setup:**
 - Selection rounds $1, \cdots, T$
 - Arms (choices) $1, \cdots, K$
 - $P_i$: reward distribution for arm $i$
 - $\mu_i$: mean reward for $P_i$ distribution
 - At each round $t$, choose an arm $A_t$ such that a reward $X_t \sim P_{A_t}$ is procured
 - Define *pseudo-regret* at time $T$ as $\bar R_t = \sum_{t=1}^T (\mu^* - \mu_{A_t})$ where $\mu^*$ is the best mean possible.
	 - The term in the sum is also known as the **optimality gap**, $\Delta_a$ (how much worse arm $a$ is than the best arm).

**Goal:** maximize total expected reward

**Known:** only $A_t$ and $X_t$

**Examples:**
- AB testing
- Advertising
- Gambling
- Optimizing blog posts
- Training hyperparameters for ML models

**Algorithms:**
 - Explore then commit (ETC): choose the arm with the highest sample mean
	 - not optimal: will never choose the true best arm if not explored
 - Upper Confidence Bound (UCB): choose arm with highest upper bound in the confidence interval
	 - Confidence interval calculation (derived from Hoeffding's Inequality): $$UCB_i(t) = \hat\mu_i(t) + \sqrt{\frac{\log(1/\delta)}{2T_i(t)}}$$
	 - (where $\delta$) is something like .05, that specifies how wide our confidence interval should be
	 - Choose a $\delta$ as a decreasing function of $t$ to ensure that confidence intervals will get narrower as we explore something more
	 - Hoeffding requires variables to be independent, which isn't actually true for the UCB algorithm (which arm we choose depends on which arms we chose before). However, the result still holds.
		 - UCB regret is bounded by $3 \sum_{a=1}^K \Delta_a + 24 \log(T) \sum_{a=1}^K \frac{1}{\Delta_a}$ which says that the regret grows logarithmically with respect to $T$.
 - Thomson Sampling: draw a sample from the posterior for each arm, and choose arm according to $argmax_a \bar\mu_a$


### Other Bandit Problems
**Adversarial Bandits:** rewards are chosen by an adversarial actor
**Contextual bandits:** rewards are correlated with confounding variables
**Linear bandits:** arms are a vector of arm choices (online linear regression)
**Non-stationary bandits:** arm reward distributions change over time
**Structured bandits:** previous choices affect future choices (such as navigation on a road network)