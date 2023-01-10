
## What does nonparametric mean?

Nonparametric methods make no assumptions about the distribution of the data or parameters; the null hypothesis is solely generated based on the data.

In some other contexts, the number of parameters in a nonparametric method is either infinite or grows with the number of data points. 

Supposing the true state of the world is $\theta$ and our data is $x$, parametric/forward models attempt to make some assumptions about $\theta$ that make us most likely to see the data $x$. Nonparametric models go the other direction, allowing us to directly infer $\theta$ based on the observed data.



## Logistic Regression vs K-Nearest Neighbors

Logistic regression is the example of a parametric model, where we try to categorize inputs into either 0 or 1:

$$y = \sigma(\beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_k x_k)$$
In this case, we must assume several things, such as linearity of data and the fact that the distribution can be roughly modelled using a sigmoid function. 

**Pros:**
 - Simple (only $k$ parameters needed)
 - Interpretable (gives either 0 or 1 as output)
 - Convex loss function (guarantees an answer)
 - Easy to solve

**Cons:**
 - Makes assumption of linear data
 - Requires feature engineering to model complex/nonlinear data
 - Too simple for some data sets

---
On the other hand, K-nearest neighbors finds the $k$ points in the training set closest to a particular value, and uses majority vote at their $y$ values. KNN makes no assumptions about the underlying distribution other than that the training data is representative of the population/test data.

Here's an example of some data that's not linearly separable in which logistic regression fails, but KNN is effective:
![[Pasted image 20221017132113.png]]


**Pros:**
 - No assumptions made about the data/world
 - Simple algorithm

**Cons:**
 - Must save all training points
 - More difficult to interpret results (less compelling explanation)


## Decision Trees

Start at some value $(x_1, x_2, \cdots, x_n)$.
Decide which feature $i$ to split on, and create two paths, for $x_i < z$ and $x_i > z$ where $z$ is some meaningful boundary.
Repeat the previous step, making a binary decision once for each feature.


Decision trees are very effective if clear boundaries exist in between data of different categories, but they are sensitive to variability in the data set. To mitigate this issue, we can take multiple decision trees, and average all of their results. 

### Random Forests
Using bootstrap aggregation (bagging), do the following:
 - independently train a large number of trees on a bootstrap sample of the data using a subset of the features.
 - Specifically, if there are $K$ features, each tree gets $K/3$ features if performing regression and $\sqrt K$ features for classification.

Random forests also have the benefit of controlling the depth of trees: when there are thousands of features, using a single decision tree would have an incredibly large number of decisions to make.


## Neural Networks

![[09 Neural Networks]]