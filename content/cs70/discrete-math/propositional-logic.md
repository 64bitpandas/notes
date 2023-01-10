---
weight: 910
---

## What are Propositions?

Propositions are anything that can be **true** or **false.** This could include:

* Statements like "Birds can fly".
* Well defined equations with no free variables like $1 + 1 = 3$.

Propositions are **not:**

* Variables like $x$ or $5$.
* Equations with free variables like $P(x) = y$.
* Statements that aren't clearly true or false, like "I like trains."

### Connectives

Simple propositions can be **joined together** to make complex statements. There are three basic ways to connect propositions together:

* **Conjunction** is the **and** operation: for $P \land Q$to be true, $P$and $Q$must **both** be true.
* **Disjunction** is the **or** operation: for $P \lor Q$to be true, **either** $P$or $Q$must be true.
* **Negation** is the **not** operation: if $P$is true, then $\lnot P$is false.
  * The **law of the excluded middle** states that $P$and $\lnot P$ _cannot both be true._

One example where we can see these components in action is in **De Morgan's Laws**, which state how negation can be **distributed** across conjunction or disjunction:

$
\lnot(P \lor Q) \iff (\lnot P \land \lnot Q)
$

"If neither P nor Q are true, then P and Q must both be false."

$
\lnot(\forall x)(P(x)) \iff (\exists x)(\lnot P(x))
$

"If P(x) isn't true for every x, then there exists an x where P(x) is false."

****

Another example of distribution is this congruence, which works for any combination of and's and or's.

$
(P \lor Q) \land R \equiv (P \land R) \lor (Q \land R)
$

****

### Implication

One proposition can **imply** another, which looks like this:

$
P \implies Q
$

Roughly, implication in plain English can be stated in the form **if P, then Q.** However, there are a lot of nuances to what this really means!

#### Properties of Implication

* **Reversible:** Q is true if P is true. However, be careful- _this doesn't necessary mean that Q implies P!_
* **P is sufficient for Q:** Proving P allows us to say that Q is also true.
* **Q is necessary for P:** For P to be true, it is necessary that Q is true. (If Q is false, then P is also false.)
* **Contrapositive Equivalence:** If P implies Q, then $\lnot Q \implies \lnot P$.
  * Note that this is different from the **converse**, which is $Q \implies P$. This statement is **not logically equivalent!**

#### Truth Table

| P | Q | P $\implies$Q | P $\iff$Q |
| - | - | --------------- | ----------- |
| T | T | T               | T           |
| T | F | F               | F           |
| F | T | T               | F           |
| F | F | T               | T           |

**Note that the truth table for** $P \implies Q$ **is equivalent to the one for** $\lnot P \lor Q$**!**  That means this formula is logically the same as $P \implies Q$.

(If two propositions have the same truth table, then they are logically equivalent. However, it's still possible for a proposition to imply another even if their truth tables are different!)

### Quantifiers

Sometimes, we need to define a specific type of variable to work with in a propositional clause. For instance, take the proposition, _"There exists a natural number that is equal to the square of itself."_ We could write this as:

$
(\exists x \in \mathbb{N})(x=x^2)
$

You could think about the parentheses almost like defining a **scope** of variables, like what might happen in programming! Here, the first clause is _defining_ an arbitrary variable $x$to be any natural number.



## Exercises

{{< tabs "q1" >}}
{{< tab "Q1" >}}
Is the expression $\forall x \exists y (Q(x,y) \implies P(x))$equivalent to the expression $\forall x ((\exists y \ Q(x,y)) \implies P(x))$?\
(Source: Discussion 0 2a)
{{< /tab >}}

{{< tab "Answer 1" >}}
**No**, they are not equivalent. We can see this more clearly by converting the implication $Q \implies P$ to $\lnot Q \lor P$ as was demonstrated in the Truth Table section above.\
\
On the left side, this conversion is straightforward, yielding $\forall x \exists y (\lnot Q(x,y) \lor P(x))$.

On the right side, we'll need to invoke De Morgan's Laws to convert the 'exists' into a 'for all' since it was negated. This yields $\forall x (\forall y\lnot(Q(x,y)) \lor P(x))$which is not the same thing!
{{< /tab >}}
{{< /tabs >}}

{{< tabs "q2" >}}
{{< tab "Q2" >}}
An integer $a$is said to _divide_ another integer $b$ if $a$is a multiple of $b$. Write this idea out using propositional logic (a divides b can be written as $a \mid b$).

**Note:** This idea is going to be important for a lot of future sections!
{{< /tab >}}

{{< tab "Answer 2" >}}
$a \mid b \iff (\exists q \in \mathbb{Z})(a = qb)$

In plain English: "There exists an integer $q$such that when we multiply $q$with $b$, we get $a$."
{{< /tab >}}
{{< /tabs >}}

## Resources

Note 1: [https://www.eecs70.org/assets/pdf/notes/n1.pdf](https://www.eecs70.org/assets/pdf/notes/n1.pdf)  
Discussion 0: [https://www.eecs70.org/assets/pdf/dis00a.pdf](https://www.eecs70.org/assets/pdf/dis00a.pdf)

