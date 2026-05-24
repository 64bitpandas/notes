---
title: "Logic"
weight: 40
---

# What is logic and why is it important?

In the beginning of the course, we discussed **atomic, factored, and structured** representations (atomic = single points per state, factored = representation of multiple states, structured = language to describe those states).

While search problems deal with atomic representations, **logic deals with factored representations.** 

## Knowledge

Agents acquire knowledge through perception, learning, and language. Agents need to know:

- The effects of actions (transition model),
- How the world affects sensors (sensor model),
- And the current state of the world (especially important for partially observable worlds).

A **knowledge base** is a set of sentences in a formal language. It is a declarative approach to building an agent:

- First, either tell it what it needs to know, or how to learn about it.
- Next, ask what to do now based on the knowledge base.

If we have a language that’s powerful enough to represent anything, and an inference algorithm to answer any question written in that language, then we can theoretically solve any problem. Of course, we’re still pretty far away from that!

## Syntax and Semantics

**Syntax** describes which statements are allowed in the language.

**Semantics** describe **truth,** and describes which statements are true in which worlds (environments/states). 

# Types of Logic

**Propositional logic** is defined in terms of booleans and boolean operations.

- Syntax: $P \land (\lnot Q \lor R)$
- Possible World: bitstring of true/false values per variable (i.e. $P=1, Q=0, R=1$)
- Semantics: $P \land Q$ is true iff $P$ is true and $Q$ is true... (repeat per operation)

**First-order logic** operates on functions, symbols, continuous variables, and propositions.

- Syntax: $\forall x \exists y P(x,y) \land Q(f(x)) \implies f(x) = f(y)$
- Possible world: described by which cases propositions $P$ and $Q$ hold

**Relational databases** relate objects to each other.

- Syntax: relational sentences: e.g. A, B are siblings
- Possible worlds: a list of typed objects and typed relations
- Semantics: all sentences in the database are true, everything else is false
- Includes knowledge graphs like Facebook, Google Knowledge Graph...

## Inference: Entailment

**Entailment:** $\alpha \models \beta$ iff in every world where $\alpha$ is true, $\beta$ is also true.

- The worlds where $\alpha$ is true is a subset of worlds where $\beta$ is true
- $\beta$ follows from $\alpha$ ($\alpha$ is a stronger, more specific statement)
- $\alpha \models \beta$ iff $\alpha \implies \beta$ is true in all worlds
- Latex: `\models`

### Proofs

A **proof** is a demonstration of entailment between $\alpha$ and $\beta$.

- A **sound** algorithm is one where everything it claims to prove is entailed.
- A **complete** algorithm is one in which everything that is entailed can be proved.
    - Very difficult, does not currently exist for number theory

**Proof methods:**

- Model checking: for every possible world, if $\alpha$ is true make sure that $\beta$ is also true.
    - Requires finitely many worlds (i.e. good for propositional logic, bad for first-order logic)
    - If a contradictive example is found ($\alpha$ is true when $\beta$ is false)
- Theorem-proving: find a sequence of proof steps leading from $\alpha$ to $\beta$

### Entailment Proof Examples

Theorem Proof Example: is the following statement correct?

- $(A \land B) \implies C \models (A \implies C) \lor (B \implies C)$
- Since $A \implies B \iff \lnot A \lor B:$
- $\lnot(A \land B) \lor C \models \lnot A \lor C \lor \lnot B \lor C$
- Using De Morgan’s Laws, $\lnot(A \land B) \iff \lnot A \lor \lnot B$.
- $\lnot A \lor \lnot B  \lor C \models \lnot A \lor \lnot B \lor C$
- Since both sides are completely equivalent, in all models where $\alpha$ is true, $\beta$ must also be true.

# Propositional Logic

![[/cs188/img/Logic/Untitled.png]]

![[/cs188/img/Logic/Untitled 1.png]]

## Syntax and Semantics

Given $m$, a **model** assigning values to a world $\{X_1, \cdots, X_n\}$ where any $X_i$ is either true or false:

- $X_i$ is a valid sentence.
- If $\alpha$ and $\beta$ are valid sentences, then :
    - $\lnot \alpha$ is a sentence.
    - $\alpha \land \beta$ is a sentence. (and)
    - $\alpha \lor \beta$ is a sentence. (or)
    - $\alpha \implies \beta$ is a sentence. (implies)
        - $\lnot \alpha \lor \beta$ is equivalent
    - $\alpha \iff \beta$ is a sentence. (iff)
        - True only if $\alpha \implies \beta$ and $\beta \implies \alpha$
    - There are no other sentences.

## Logic

**Conjunctive Normal Form (CNF):** disjunctions (or) combined with conjunction (and)s

- Example: $(x_1 \lor x_2) \land (x_2 \lor \lnot x_3) \cdots$
- Opposite: **Disjunctive Normal Form (DNF)** which is the opposite: ands combined with ors

A sentence is:

- **valid** if sentence is true for all models
- **satisfiable** if sentence is true in 1 or more models
- **unsatisfiable** if sentence is false in all models

## Algorithms

### Forward Chaining

[https://en.wikipedia.org/wiki/Forward_chaining](https://en.wikipedia.org/wiki/Forward_chaining)

Repeatedly apply **Modus Ponens** to generate new facts:

- If $X$ implies $Y$ and $Y$ implies $Z$, then $X$ implies $Z$.
- Can only be used on a knowledge base of **definite clauses** of (conjunction of symbols) implies (symbol) OR a single symbol by itself
- Runs in linear time with respect to the size of the knowledge base:
    - Preprocess all symbols to determine which rules they appear in
    - Each rule keeps a count of how many premises are not yet satisfied.
- Forward chaining is **sound and complete** for all definite clause knowledge bases.

```python
def fc(kb, query):
	count = {number of symbols in rule for rule in kb}
	inferred = {False for symbol in kb}
	agenda = queue of symbols
	
	initialize agenda with all symbols known to be true
	while agenda is not empty:
		premise = agenda.pop()
		if premise is query:
			return True
		if inferred[premise] is False:
			inferred[premise] = True
			for rule in kb:
				if premise in rule:
					count[rule] -= 1
					if count[rule] == 0:
						agenda.push(premise.conclusion)
	return False
```

### DPLL

Davis-Putnam-Logemann-Loveland algorithm: a recursive depth-first search over models to determine satisfiability (SAT problem)

- Early termination conditions:
    - All clauses are satisfied
    - Any clause is falsified

Things to look for:

- **Pure literals:** symbols where all occurrences have the same sign (all positive, or all negated). If all positive, the symbol must be true; if all negative, the symbol must be false.
- **Unit clauses:** clauses left with a single literal (combination of trues, falses, and one symbol OR the symbol by itself)

```python
def DPLL(clauses, symbols, model):
	if all([clause is True for clause in clauses]):
		return True
	if any([clause is False for clause in clauses]):
		return False
	PS, is_positive = find_pure_symbol(clauses, symbols, model)
	if PS:
		model[PS] = is_positive
		symbols.remove(PS)
		return DPLL(clauses, symbols, model)
	UC, is_positive = find_unit_clause(clauses, symbols, model)
	if UC:
		model[UC] = is_positive
		symbols.remove(UC)
		return DPLL(clauses, symbols, model)
	# else, try setting a symbol to true and false, 
	# and see what happens in each case
	P = symbols.first
	return DPLL(clauses, symbols.rest, model where P is True)
			or DPLL(clauses, symbols.rest, model where P is False)
```

# First Order Logic

Unlike propositional logic, which is an atomforic representation, first order logic is a **structured** representation that uses language to describe the rules that govern a certain world.

In first-order logic, a possible world consists of:

- A non-empty set of objects
- A list of predicates
    - A list of which objects satisfy which predicates
- A list of functions
    - A mapping from input object to output objects for each function
- A list of constant symbols that refer to particular objects (0-ary functions)

Since there is no bound on the possible number of objects, there are **infinitely many possible worlds** describable with first-order logic, even if worlds can be described with a finite number of objects.

## Syntax and Semantics

A **term** refers to an object. It an be:

- A constant symbol like $A$
- A function symbol with terms as arguments, like $f(A)$

An **atomic sentence:**

- can take in terms as arguments and returns true or false based on if that predicate is true.
- or, can be an equality between two terms.

A **complex sentence:**

- can include logical connectives like $\lor$, $\iff$, etc.
- can include the universal quantifier $\forall$ or the existential quantifier $\exists$

### Common Mistakes

- Don’t use $\exists$ with $\implies$. (This will nearly always be true, since false is always a valid input into an implication.) Instead, do something like $\exists x \  f(x) \land \forall n \ g(n) \implies \cdots$
- Don’t use $\forall$ with $\land$.