---
title: "Games"
weight: 30
---

A **game** is a task environment with more than one agent. Some characteristics of games could be:

- Deterministic vs Stochastic
- Fully observable vs Partially observable
- Number of players
- Team vs Individual
- Turn based vs Simultaneous
- Zero sum vs General sum
    - Zero sum: where agents have opposite utilities (one maximizes, the other one minimizes)
    - General sum: agents have independent utilities, allowing for cooperation, alliances, competition...

A **standard game** is deterministic, observable, two-player, turn-based, and zero-sum. It can be formulated using:

- An initial state $s_0$
- Players (and current player to move)
- Actions for current player to move
- Transition model
- Terminal test (game over condition)
- Terminal values (utility function)

## Adversarial Search

### Minimax

See 61B notes

### Expectimax

Like minimax, but with **chance nodes** (circular) which take the average (expected value) of child nodes.

### Monte Carlo Tree Search

For problems with very large branching factors (like Go), normal alpha-beta search is hopelessly slow.

One possible solution is MCTS, which:

1. **Evaluates by rollouts:** play $N$ random games using a fast, fixed rollout policy from the current position, and count wins and losses.
2. **Selectively searches** parts of the tree that will improve the decision, regardless of depth
    1. Skip moves that are very bad (like hanging queen), explore good moves more deeply
    2. Allocate more rollouts to more promising nodes, as well as rollouts that create the most variance (uncertain).

**UCB1 Formula:**

 ****$\frac{U(n)}{N(n)} + C \times \sqrt{\frac{\log N (P(n))}{N(n)}}$

- $N(n)$ = total number of rollouts from node $n$
- $U(n)$ = total number of wins for rollouts
- Approximate solution to bandit problems (how do you spend money to evaluate gambling machines)

**UCT:**

While time not exceeded:

- Recursively apply UCB formula to current search tree to choose a path down to a leaf $n$
- Add a new child $c$ to $n$ and run a rollout from $c$
- Update win counts from $c$ back to root

When complete, choose the action leading to the child with the highest $N(c)$ value

- As $N \to \infty$, UCT selects the minimax move