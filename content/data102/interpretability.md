---
weight: 80
---
## What do we look for in predictions?
**Accuracy:** We want predictions to be close to the true values.
**Simplicity:** We want the model to be easy to understand and trust.
**Interpretability:** We want to be able to explain why the model behaved the way it did.


## Components of interpretability

**What is it?**
 - transparency: understanding the model
 - explanations: understanding the predictions

**When and why do we care?**  
 - high stakes decisions have major impacts, and need to be understood
 - regulations such as GDPR requires explanations for algorithms

**What do we get from interpretability?**
 - Trust that the models will make accurate predictions
 - Causality: whether x actually causes y
 - Transferability: whether the model will do well in the real world
 - Informativeness: whether predictions can be used for decision making
 - Ethics: whether the model is fair from a human perspective

## Explanability
For black-box models such as deep decision trees and random forests, thousands of parameters can be involved, and it is difficult or impossible to explain how all of them relate to one another.

Instead of interpretability, we can go for explainability instead:
 - Surrogate models: approximate the model with a simpler model, and interpret that simpler model
 - Permutation-based approach: measure importance of a feature by modelling without that feature and interpreting the difference