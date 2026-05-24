---
title: "Duality"
weight: 150
created: "March 27, 2021 4:04 PM"
---

## Primal and Dual: An Example

Suppose we have an original, known as a **primal**, linear program with variables $x_1, \cdots, x_n$ and some constraints on those variables.

As an example, let's say we are trying to maximize $2x_1 + 4x_2$ such that:

- $x_1, x_2 \ge 0$
- $x_1 \le 50, x_2 \le 80$
- $x_1 + x_2 \le 100$

We can rewrite the objective function as a linear combination of the constraints:

- $y_1 \cdot (x_1 \le 50)$
- $y_2 \cdot (x_2 \le 80)$
- $y_3 \cdot (x_1 + x_2 \le 100)$

Such that $y_1, y_2, y_3 \ge 0$ so that the inequalities do not flip.

Combining all of these inequalities creates the big inequality:

$(y_1 + y_3) x_1 + (y_2 + y_3) x_2 \le 50 y_1 + 80 y_2 + 100 y_3$

(The above inequality is constructed by separating the $x$ terms by the inequalities that affect them, and recognizing that the largest possible value of them is the sum of all inequality bounds.)

Looking at the original objective function $2x_1 + 4x_2$, we can substitute the $y$ values from the above inequality to get the equivalent statements:

- $y_1 + y_3 \ge 2$
- $y_2 + y_3 \ge 4$

 (Since the objective function wants to maximize, it's OK to have larger values.)

Then, we can set the right side of the big inequality to the new objective function:

$\min(50y_1 + 80y_2 + 100y_3)$

This is actually another linear program, called the **dual LP.** 

## Properties of the Dual

- If two solutions to the primal and dual LP have the **same value,** then they are **both optimal.**
- If either the primal or dual is feasible, then the other must also be feasible.
- The max-flow min-cut theorem uses dual as a solution: the min cut capacity is the dual of the max flow, and so one can be used to solve the other.
- **Duality Theorem:** If the primal LP has a bounded max, then the dual LP has a bounded min, and the two values are equal.

## The General Case

**How do we find the dual of any generic primal LP?**

Suppose we have a primal LP:

- Objective function: maximize $C_1x_1 + \cdots + C_kx_k$
- A set of constraints $I$ (inequalities) that are in the form $I_i: a_{i1}x_1 + \cdots + a_{ik}x_k \le b_i$
- A set of constraints $E$ (equalities) that are in the form  $E_i:a_{i1}x_1 + \cdots + a_{ik}x_k = b_i$
- A set of constraints $N$ (non-negative) that are in the form $N_j: x_j \ge 0$

We can apply the following transformation to convert this into the dual LP:

![[/cs170/img/Duality/Untitled.png]]

- Each primal constraint $i$ gets one multiplier variable $y_i$.
- For all non-negative constraints, the transformed primal constraint is $\ge c_j$.
- For all full-range constraints, the transformed primal constraint is $= c_j$.
- The objective function minimizes the induced right hand side of the sum.

Here is the statement of the general dual LP:

- Objective function: minimize $b_1y_1 + \cdots + b_my_m$
- Non-negative: $\forall j \in N$, $a_{ij} y_1 + \cdots + a_{mj} y_m \ge c_j$
- Possibly negative: $\forall j \not\in N, a_{ij} y_1 + \cdots + a_{mj} y_m = c_j$
- All $y_i \ge 0$ for each inequality.

## Vector Form

If all constraints are inequalities and all variables are non-negative:

- The primal LP can be stated as maximizing the vector $< c, x >$ such that $Ax \le b$ and $x \ge 0$.
- The dual LP can be stated as minimizing the vector $<b, y>$ such that $A^T y \ge c$ and $y \ge 0$.