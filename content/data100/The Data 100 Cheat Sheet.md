
# Resources

**Textbook:** [http://www.textbook.ds100.org/ch/01/lifecycle_intro.html](http://www.textbook.ds100.org/ch/01/lifecycle_intro.html)

# Data Science Lifecycle

![[/data100/img/Untitled.png]]

[http://www.ds100.org/fa20/lecture/lec01/](http://www.ds100.org/fa20/lecture/lec01/)

# Data Sampling

[https://docs.google.com/presentation/d/1pI4shcpHeNU9vjOaG9l7cYfPe4GWy6hXICpQR8zTH1A/edit#slide=id.g8960eb33b8_0_151](https://docs.google.com/presentation/d/1pI4shcpHeNU9vjOaG9l7cYfPe4GWy6hXICpQR8zTH1A/edit#slide=id.g8960eb33b8_0_151)

## Types of Samples

A **convenience sample** is whoever you can get ahold of.

- Not a good idea for inference!
- Haphazard ≠ random.
- Sources of bias can introduce themselves in ways you may not think of!

In a **quota sample**, you first specify your desired breakdown of various subgroups, and then reach those targets however you can.

- For example: you may want to sample individuals in your town, and you may want the age distribution of your sample to match that of your town’s census results.

**Quota samples are not random.**

## Samples and Population

- **Population: The group that you want to learn something about.**
- **Sampling Frame: The list from which the sample is drawn.**
    - If you’re sampling people, the sampling frame is the set of all people that could possibly end up in your sample.
- **Sample: Who you actually end up sampling.**
    - A subset of your sampling frame.
    - Samples are often used to make **inferences about the population**.
    - How you draw the sample will affect your accuracy.
    - Two common sources of error:
        - **chance error**: random samples can vary from what is expected, in any direction.
        - **bias**: a systematic error in one direction.

## Types of Biases

**Selection Bias**

- Systematically excluding (or favoring) particular groups.
- How to avoid: Examine the sampling frame and the method of sampling.

**Response Bias**

- People don’t always respond truthfully.
- How to avoid: Examine the nature of questions and the method of surveying.

**Non-response Bias**

- People don’t always respond.
- How to avoid: Keep your surveys short, and be persistent.
- People who don’t respond aren’t like the people who do!

# EDA

[https://docs.google.com/presentation/d/1_bjyzr7Wd4-jJurzSKoYKuNk0JJi_XI8o-xkMKN3qf4/edit#slide=id.g8adf084dad_0_256](https://docs.google.com/presentation/d/1_bjyzr7Wd4-jJurzSKoYKuNk0JJi_XI8o-xkMKN3qf4/edit#slide=id.g8adf084dad_0_256)

![[/data100/img/Untitled 1.png]]

![[/data100/img/Untitled 2.png]]

![[/data100/img/Untitled 3.png]]

# Visualization

[Lecture 9](https://docs.google.com/presentation/d/1ARdZQSRAlsuqCEDOwZvqq1adoGHjUk29pN54SpFTLtE/edit#slide=id.g984a1a470f_1_15)

[Lecture 10](http://www.ds100.org/fa20/lecture/lec10/)

# Modeling

[https://docs.google.com/presentation/d/1fYsAhfvItcj5gL5ZHdZgV2gC27ui34-8-y5JG91ldl0/edit#slide=id.g85cd27fca3_0_18](https://docs.google.com/presentation/d/1fYsAhfvItcj5gL5ZHdZgV2gC27ui34-8-y5JG91ldl0/edit#slide=id.g85cd27fca3_0_18)

![[/data100/img/Untitled 4.png]]

(**RMSE** is the square root of the MSE)

![[/data100/img/Untitled 5.png]]

![[/data100/img/Untitled 6.png]]

**Min(MSE) is the sample variance.**

# Linear Regression

[http://www.ds100.org/fa20/lecture/lec12/](http://www.ds100.org/fa20/lecture/lec12/)

[https://docs.google.com/presentation/d/15olJS1Yuk22spzrNx4It6-eLm8gkZM4pFKKOWhKXBUI/edit#slide=id.g8ada35e807_0_96](https://docs.google.com/presentation/d/15olJS1Yuk22spzrNx4It6-eLm8gkZM4pFKKOWhKXBUI/edit#slide=id.g8ada35e807_0_96)

**Optimal Parameters:** 

![[/data100/img/Untitled 7.png]]

![[/data100/img/Untitled 8.png]]

![[/data100/img/Untitled 9.png]]

![[/data100/img/Untitled 10.png]]

![[/data100/img/Untitled 11.png]]

![[/data100/img/Untitled 12.png]]

**Least Squares Estimate**

[https://docs.google.com/presentation/d/15olJS1Yuk22spzrNx4It6-eLm8gkZM4pFKKOWhKXBUI/edit#slide=id.g8ada35e807_0_96](https://docs.google.com/presentation/d/15olJS1Yuk22spzrNx4It6-eLm8gkZM4pFKKOWhKXBUI/edit#slide=id.g8ada35e807_0_96)

![[/data100/img/Untitled 13.png]]

# Feature Engineering

[http://www.ds100.org/fa20/lecture/lec14/](http://www.ds100.org/fa20/lecture/lec14/)

### Uninformative features (e.g., UID)

- Is this informative (probably not?)
- **Transformation: remove uninformative features (why?)**
    - They could influence the model.

### Quantitative Features (e.g., Age)

- **Transformation: May apply non-linear transformations (e.g., log)**
- **Transformation: Normalize/standardize (more on this later …)**
    - Example: (x – mean)/stdev

### Categorical Features (e.g., State)

- How do we convert State into meaningful numbers?
    - Alabama = 1 , …, Utah = 50 ?
    - Implies order/magnitude means something … we don’t want that ...
    
    **Transformation**: *One-hot-Encode*
    
    ![[/data100/img/Untitled 14.png]]
    

# Bias and Variance

## Error

**Chance Error:** Due to randomness. Appears in both observations and training sample

**Bias:** Non-random error due to model being different from true data

- Positive bias = overestimate
    
    
    ![[/data100/img/Untitled 15.png]]


![[/data100/img/Untitled 16.png]]

# Gradient Descent

[https://docs.google.com/presentation/d/1gi7Ar5O7T0qE_abZeZvX-VURC-i3sWwwK6FtsuIwkQc/edit#slide=id.g8c5b259fcb_0_767](https://docs.google.com/presentation/d/1gi7Ar5O7T0qE_abZeZvX-VURC-i3sWwwK6FtsuIwkQc/edit#slide=id.g8c5b259fcb_0_767)

![[/data100/img/Untitled 17.png]]

# Logistic Regression

[http://www.ds100.org/fa20/lecture/lec18/](http://www.ds100.org/fa20/lecture/lec18/)

![[/data100/img/Untitled 18.png]]

![[/data100/img/Untitled 19.png]]

![[/data100/img/Untitled 20.png]]

![[/data100/img/Untitled 21.png]]

![[/data100/img/Untitled 22.png]]

![[/data100/img/Untitled 23.png]]

![[/data100/img/Untitled 24.png]]

![[/data100/img/Untitled 25.png]]

![[/data100/img/Untitled 26.png]]

![[/data100/img/Untitled 27.png]]

- Precision penalizes false positives, and recall penalizes false negatives.
- We can achieve **100% recall** by making our classifier output “1”, regardless of the input.
    - We would have no false negatives, but many false positives, and so our **precision would be low**.
- This suggests that there is a **tradeoff** between precision and recall – they are inversely related.
    - Ideally, both would be near 100%, but that’s unlikely to happen.
- We can **adjust** our classification **threshold** to suit our needs, depending on the domain.
    - **Higher threshold** – fewer false positives. **Precision tends to increase.**

**Lower threshold**

– fewer false negatives.

**Recall increases**

.

In each of the following cases, what would we want to maximize: precision, recall, or accuracy?

- Predicting whether or not a patient has some disease.
    - Maximize **recall**.
    - Presumably if we say someone has the disease, they will go through further testing.
    - If we say they don’t, the condition may be left untreated, which is dangerous.
- Determining whether or not someone should be sentenced to life in prison.
    - Maximize **precision**.
    - We don’t want to sentence guilty people, so we want to be very sure that this is a true positive.
- Determining if an email is spam or ham.
    - Maximize **accuracy**, though this one is subjective.
    - Depends what you think is worse – having a bunch of spam emails ending up in your inbox, or a bunch of non-spam emails being filtered out.
    
    ![[/data100/img/Untitled 28.png]]

    ![[/data100/img/Untitled 29.png]]
    

# Clustering

[https://docs.google.com/presentation/d/19TdgyT7vnnz6mR0-yftJH6iVpplQeTnohobvAr0dOeY/edit#slide=id.g8e2e3a4c90_0_1346](https://docs.google.com/presentation/d/19TdgyT7vnnz6mR0-yftJH6iVpplQeTnohobvAr0dOeY/edit#slide=id.g8e2e3a4c90_0_1346)

# Decision Trees

[https://docs.google.com/presentation/d/1oN7at3ljTNtRgRR6wO7Di8O3vK4M2pKBzPL3zomot2s/edit](https://docs.google.com/presentation/d/1oN7at3ljTNtRgRR6wO7Di8O3vK4M2pKBzPL3zomot2s/edit)

![[/data100/img/Untitled 30.png]]

![[/data100/img/Untitled 31.png]]

# SVD/PCA

![[/data100/img/Untitled 32.png]]

[https://docs.google.com/presentation/d/1mk9g45VZP8U-9cLCke72aPB1Ve1D8LvpKsPX2Ix-VX4/edit#slide=id.ga21a3d7989_0_540](https://docs.google.com/presentation/d/1mk9g45VZP8U-9cLCke72aPB1Ve1D8LvpKsPX2Ix-VX4/edit#slide=id.ga21a3d7989_0_540)

# Ridge Regression

![[/data100/img/Untitled 33.png]]

![[/data100/img/Untitled 34.png]]

![[/data100/img/Untitled 35.png]]
