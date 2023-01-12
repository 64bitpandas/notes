---
weight: 130
---

## Introduction

Reinforcement Learning (RL) is an example of **online planning,** where agents have no prior knowledge of rewards or transitions and must explore an environment before using an estimated policy.

- Model-based learning: attempts to estimate transition and reward functions with samples attained during exploration before solving MDP with estimates using value or policy iteration
- Model-free learning: attempts to estimate values/Q-values of states directly without construction a reward or transition model in MDP

Passive reinforcement learning: agent is given a policy and learns the values of states under that policy.

- direct evaluation, TD learning

Active reinforcement learning: use feedback to iteratively update policy, eventually learning optimal policy

- Q-learning

## Direct Evaluation

1. Fix a policy $\pi$
2. Have the agent experience several episodes (group of samples) 
3. Compute estimated value of any state $s$ by dividing total utility (reward from leaving state) by number of times visited

Direct evaluation loses all transition information, since each state’s value is computed separately.

## Temporal Difference (TD) Learning

TD learning maintains an estimated value $V^\pi(s)$ for each state by averaging returns achieved from $s$ across all samples.

$$
V^\pi(s) \leftarrow (1-\alpha)V^\pi(s) + \alpha[R(s, \pi(s), s') + \gamma V^\pi(s')]
$$

- $\alpha$ is a learning rate: higher $\alpha$ should be used when the current estimate is bad, and low $\alpha$ should be used when the current estimate is good.
- $\pi(s)$ is an action sampled from the current policy. This action will lead to a new state $s’$, whose value will be used to calculate the new value of the current state.
- $V^\pi(s)$ will only converge to the optimal value $V^*(s)$ if the policy used is optimal. TD learning by itself cannot learn this optimal policy.

## Q-Learning

Q-learning is like TD learning, but using Q-values instead of normal utility values.

Regardless of the optimality of the policy used or actions taken, Q-learning will still converge to the optimal policy given a reasonable learning rate and enough exploration.

$$
Q(s, a) \leftarrow (1-\alpha)Q(s,a) + \alpha[R(s, a, s') + \gamma \max_{a'} Q(s', a')]
$$

**Approximate Q-learning** improves Q-learning by using a feature representation for states:

- Let $\textnormal{difference} = [R(s, a, s’) + \gamma \max_{a’} Q(s’, a’)] - Q(s, a)]$
- Update weights using $w_I \leftarrow w_i + \alpha \times \textnormal{difference} \times f_i(s, a)$
- Update Q-values using $Q(s, a) \leftarrow Q(s, a) + \alpha \cdot \textnormal{difference}$
- Define $Q(s, a) = w \cdot f(s, a)$
- Define $V(s) = w \cdot f(s)$

**SARSA variation:** use the action performed by the current policy to learn the Q-value.
$$Q(s,a) \leftarrow (1-\alpha)Q(s,a) + \alpha(R(s,a,s') + \max_a Q(s', a))$$
 - only converges if $\alpha$ approaches $0$ over time, and if trajectories include all states

## Exploration vs Exploitation

The following methods distribute time between exploration and exploitation:

### Epsilon-Greedy

Define some probability $\epsilon \in [0, 1]$. With probability $\epsilon$, randomly explore. With probability $1 - \epsilon$, choose the next state based on the current best policy.

### Exploration Function

During the Q-learning update, maximize over some exploration function instead of Q-values:

$$
Q(s, a) \leftarrow (1-\alpha)Q(s,a) + \alpha[R(s,a,s') + \gamma \max_a' f(s', a')]
$$

where $f(s, a) = Q(s, a) + \frac{k}{N(s, a)}$

- $k$ is a constant determining the degree of exploration. Decrease towards 0 over time to decrease the amount of exploration being done.
- $N(s, a)$ is the number of times the Q-state has been visited.