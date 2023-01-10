# Stable Matching

## Introduction

The **stable matching problem** deals with how to match one group to another group while trying to maximize everyone's 'happiness'. 

It works best when the two groups are **distinct** \(nobody can be in both groups at once\) and the orderings are **complete** \(everyone in the other group has to show up in all orderings\). Before we get to examples of when this might apply, I'll throw out a few examples where we **can't** use this algorithm so you don't get any wrong ideas:

* We **cannot** use this for creating room groups based on roommate preferences \(because everyone is in one big group\).
* We **cannot** use this for situations where people are limited to their top three choices in jobs.

### Some Definitions

In order to more concretely set up the stable matching problem, let's define some terms formally:

A **pairing** is a set of job-candidate pairs that uniquely \(disjointly\) matches each job to each candidate. For example, {\(Esports, Joe\), \(Steakhouse, Donald\)} is a valid pairing if we're trying to match Joe and Donald to two possible jobs.

Note that 'job' and 'candidate' can be replaced with any two arbitrary groups, as long as one group doesn't contain any items from the other group!

A **rogue couple** is a single pair where neither person in the pair wants to be with the other person. If a pairing is **stable**, it cannot contain any rogue couples.

**x-optimal matching** is a stable pairing that favors the choices of group x over the other group. This group is **whichever group chooses**- In the example above, the pairing would be **job optimal**, and **candidate pessimal.** \(More on why later.\)

## The Propose and Reject Algorithm

There are a good number of ways we can get stable matchings, but one of the most commonly used methods is the **propose-reject algorithm.** It goes like this:

1. On the first day, each job sends an offer to their favorite candidate.
2. Each candidate has their own set of preferences, though, so if they get multiple job offers they'll reject all but their favorite one.
3. The candidate will then say to their favorite offer, "I like it, but please wait until tomorrow so I can see if I get a better offer."
4. Repeat until each job gets exactly one candidate.

#### Important notes about this algorithm:

* **It is guaranteed to terminate.** \(Check the proofs section to see why\)
* **Every day, it gets better for candidates.** This is because candidates can choose their best offer, so as more offers keep rolling in they get more \(and better\) choices. This means that this particular algorithm is **job-optimal** and **candidate-pessimal.** Indeed, regardless of what the groups are, **whichever group proposes will have optimal results.**

### An Example

Let's say that three people **Alice \(A\), Bob \(B\),** and **Charlie \(C\)** applied to jobs in **Capitol One \(1\), Two Sigma \(2\),** and **3M \(3\)** . Their preferences are \(in order from most to least favored\):

CANDIDATES                 JOBS  
A \|\| 1 2 3                         1 \|\| C A B  
B \|\| 1 2 3                         2 \|\| A B C  
C \|\| 2 1 3                         3 \|\| A C B

On day 1,  Capitol One will send an offer to Charlie. Two Sigma and 3M will send job offers to Alice. Since Alice got multiple offers, they will reject 3M and keep Two Sigma on their list.  
**Day 1: \(1,C\), \(2, A\)**

On day 2, Capitol One will send an offer to Charlie again, and Two Sigma will send an offer to Alice again. Since 3M was rejected yesterday, they'll move onto the next person on their list, Charlie. However, Charlie still prefers Capitol One over 3M so he will reject 3M.  
**Day 2: \(1,C\), \(2,A\)**

On day 3, Capitol One will send an offer to Charlie again, and Two Sigma will send an offer to Alice again. Since 3M was rejected yesterday, they'll move onto their final person, Bob. **Since no more candidates or jobs are left unmatched, this algorithm terminates in the stable pairing \(1, C\), \(2, A\), \(3, B\).**

### Proofs of the Propose-Reject Algorithm

#### Existence \(Termination\)

**We can prove this by contradiction:** suppose that a job isn't paired yet after the end of the algorithm. This would mean that the job must have made an offer to every single possible candidate and got rejected by all of them. But this is illegal! Those candidates must be matched with other jobs if they rejected this one, meaning there needs to be 1 more job than there actually is. Therefore, all jobs and candidates must be paired at the end of the algorithm.

#### Stability

Let's say a job J and candidate C are matched after the algorithm terminates. If J preferred another candidate C\*, then that would mean C\* were higher up on its list and must have made an offer to C\* before C. However, the fact that J is matched with C and not C\* means that C\* rejected J, and thus prefers another job over J. This means that the pairing J and C is stable. \(You can repeat this argument for any pair J and C.\)

#### Optimality

Theorem: Job Propose, Candidate Reject produces a job-optimal pairing.

* Proof by contradiction: assume that there's a job j that doesn't get an optimal candidate c.
* Let t be the first day job j gets rejected by its optimal candidate g.
* On that day, there was another job offer j\* that c preferred.
* Therefore, j\* likes c at least as much as the optimal candidate. **This creates a rogue couple.** 
* By the Well Ordering Principle, this is the first day that job j was rejected

**Pessimality**

Theorem: Job Propose, Candidate Reject produces a candidate-pessimal pairing:

* Let T be a pairing where \(j, c\) is a pair.
* Let S be a stable pairing that is worse for c than T is. So \(j, c\*\) is a pair.
* Since j prefers c to c\*, \(j, c\*\) is a rogue couple for S which is a **contradiction.** Therefore, T is the worst possible pairing for c.

### 

