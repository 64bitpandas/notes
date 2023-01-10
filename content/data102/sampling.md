
## Some 188 review
![[04 Bayes Nets#Sampling]]


## Markov Chains
http://prob140.org/textbook/content/Chapter_10/01_Transitions.html

Markov chains are sequences of random variables, typically indexed by time. Each possible value is a state.

Markov chains follow the **Markov property:** each random variable only depends on the previous one.

Another property of Markov chains is that the transition probabilities between states are known and constant over time.

The steady state distribution is one that describes the probability of being at each state $x$ at time $


## Gibbs Sampling Revisited
Suppose we have $\theta_1, \cdots, \theta_n$ and we want $p(\theta_1, \cdots, \theta_n | x)$. Here's the general algoritm:
1. Sample a $p(\theta_1 | x, \theta_2, \cdots, \theta_n)$
2. Initialize $\theta^{(0)}$
3. Resample $\theta_1^{(1)}$ from $p(\theta_1 | x, \theta_2^{(0)}, \cdots, \theta_n^{(0)})$
4. Continue for all $\theta_i^{(1)}$
5. Repeat for each time step



## Metropolis-Hastings
The Metropolis-Hastings algorithm is a method to sample from an unnormalized target distribution $q(\theta)$. 

1. Generate a proposal $V(\theta' | \theta)$ (some distribution that depends on the current sample).
2. Accept or reject the new proposal:
	1. If $q(\theta') > q(\theta)$, immediately accept.
	2. Otherwise, accept with probability $q(\theta')/q(\theta)$.

Recall that $q(\theta) \propto(\theta | x) = p(\theta)p(x|\theta)$. Therefore, the ratio $q(\theta')/q(\theta)$ is equivalent to $P(\theta'|x)/P(\theta|x)$. So, the Metropolis-Hastings algorithm will reach the steady state distribution of the actual density.

### Choosing a Proposal
A poor proposal distribution for Metropolis-Hastings can create a large amount of unnecessary rejections. Here's an example:
![[Pasted image 20220928153000.png]]
Suppose we have four possible proposals to choose from:
 - A: uniform distribution of width 1 centered at the current t: Uniform[t-½, t+½]
 - B: shifted exponential distribution starting at the current t with lambda=1
 - C: normal distribution with mean at the current t and standard deviation 500
 - D: normal distribution with mean at the current t and standard deviation 40

In this example:
 - B is the worst because it's impossible to sample values from smaller $t$ than the current value.
 - A is poor because it will take a long time to converge.
 - C is poor because many proposals will be rejected.
 - D is the best because it allows us to generate samples across the entirety of the domain without having too many rejections.