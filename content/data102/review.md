PDF = probability density function = probability that $X=x$ 
CDF = cumulative density function = $P(X \le t) = \int_{-\infty}^t f(x)dx$


Bayes Rule: 
$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$
Alternate form for binary decision making (total probability):
$$P(A=1) = P(A=1|B=0)P(B=0) + P(A=1|B=1)P(B=1)$$


![[Pasted image 20220928190049.png]]
![[Pasted image 20221018001126.png]]
![[Pasted image 20221018001145.png]]



![[Pasted image 20221028161106.png]]

![[Pasted image 20221028161315.png]] IPW formula: 4 possibilities for values of $y_i$ and $z_i$. Sum up number of times each possibility occurs and divide them by how likely they are to be treated ($e(x)$).
 - $e(X) = P(Z=1|X)$
 - Strategy:
	 - make a table of all possible values of X and Z
	 - divide each one by how likely it is to occur, and sum them all together
	 - divide the whole result by $n$

![[Pasted image 20221101130056.png]]