# __The Ten Ranks of the Two-Sided Operators at $n=4$__

## Introduction

**The subject.** The two-sided operator $T_{A,B}(X)=AXB$ is an element of the endomorphism algebra of the sixteen-dimensional matrix space, so it has a rank as a linear operator, a number between zero and sixteen. That number is the product of the two matrix ranks,

$$
\operatorname{rank}T_{A,B}=\operatorname{rank}A\cdot\operatorname{rank}B,
$$

and the products of two integers between zero and four form a set of exactly ten numbers.

**The order of the article.** The first section proves the product law through the Kronecker form. The second lists the ten values and the seven absences, and identifies the absences as the integers that are not such a product. The third describes the stratification and the rank-one stratum. The fourth compares with the biquaternion row, where the set is $\{0,1,2,4\}$ and the single absence is three. The fifth states the law at general order and draws the boundary with the article on length.

**It assumes** *The Two-Sided Operators and the Segre Cone at $n=4$* for the product rule $T_{A,B}T_{C,D}=T_{AC,DB}$, and *The Left Ideals and the Image of a Left Multiplication at $n=4$* for the dimension of the two-sided image.

**The result in one line.** The operator rank is multiplicative in the two factors, so it takes ten values and misses seven, and the value sixteen occurs exactly on the pairs of invertible factors.

**Boundaries.** The word rank carries three meanings in this section of the corpus, and this article uses the third. The *matrix rank* of a matrix $A$ is the dimension of its column space, at most four. The *length* of an operator is the rank of its coefficient matrix, at most four. The *operator rank* of $T_{A,B}$ is the dimension of its image as a map on the sixteen-dimensional space, at most sixteen. The present article is about the third; *The Length and the Two Ranks at $n=4$* is about the first two.

## The Product Law

**Definition.** For $A,B\in M_4(\mathbb{C})$ the **two-sided operator** is $T_{A,B}(X)=AXB$, and its **operator rank** is the dimension of its image in $M_4(\mathbb{C})$.

**Proposition.** $T_{A,B}=L_A R_B=R_B L_A$, and the map $(A,B)\mapsto T_{A,B}$ is bilinear.

*Proof.* $L_A R_B(X)=A(XB)=(AX)B=R_B L_A(X)$, and bilinearity is bilinearity of the product.

**Proposition (the Kronecker form).** Under the identification $\operatorname{End}(M_4(\mathbb{C}))\cong M_4(\mathbb{C})\otimes M_4(\mathbb{C})$ in which $T_{A,B}$ corresponds to $A\otimes B^{\mathsf T}$, the operator rank is at most $\operatorname{rank}A\cdot\operatorname{rank}B$ and the bound is attained.

*Proof.* Choose bases in which $A$ has $r$ nonzero columns and $B^{\mathsf T}$ has $s$ nonzero columns, with $r=\operatorname{rank}A$ and $s=\operatorname{rank}B$. In the induced basis of the tensor square, the Kronecker product has nonzero entries only at the $rs$ index pairs, so it has rank exactly $rs$; a change of basis does not alter the rank of a linear map.

**Corollary.** $\operatorname{rank}T_{A,B}=\operatorname{rank}A\cdot\operatorname{rank}B$.

*Proof.* The proposition gives the exact value, and the value is the product of the two matrix ranks.

**Corollary.** $T_{A,B}$ is invertible exactly when both $A$ and $B$ are invertible, and then its inverse is $T_{A^{-1},B^{-1}}$.

*Proof.* The rank is sixteen exactly when the product of the ranks is sixteen, so both factors have rank four; the inverse is checked by composing.

**Corollary.** $\ker T_{A,B}$ has dimension $16-\operatorname{rank}A\cdot\operatorname{rank}B$.

*Proof.* The rank–nullity theorem and the product law.

**The two extreme cases.** If $A$ is invertible, $T_{A,B}$ has the same rank as $R_B$, namely $4\operatorname{rank}B$, since composing with an invertible operator does not change the rank. If both factors are singular, the rank drops by a product of two deficits, and the drop can be as large as sixteen.

*Proof.* The rank of a composite is the rank of the second factor when the first is invertible, and the product law gives the general value.

## The Ten Values

**Theorem.** The set of values of the operator rank of $T_{A,B}$ over all pairs $(A,B)$ is

$$
\{0,1,2,3,4,6,8,9,12,16\},
$$

a set of ten numbers. The numbers $5,7,10,11,13,14,15$ do not occur.

*Proof.* The rank is a product $rs$ with $r,s\in\{0,1,2,3,4\}$. The multiplication table of that set contains exactly the ten numbers displayed: the values are $0$; the five singletons $1,2,3,4$; the four products $2\cdot2=4$, $2\cdot3=6$, $3\cdot3=9$, $2\cdot4=8$, $3\cdot4=12$, $4\cdot4=16$; and no others. Every displayed value is realised, by pairs of matrices of the stated ranks. The seven remaining numbers between zero and sixteen are not of the form $rs$ with both factors at most four: five and seven are primes larger than four, ten and fourteen have a prime factor larger than four, eleven and thirteen exceed four and are prime, and fifteen equals $3\cdot5$ with a factor larger than four.

**Corollary.** Ten of the seventeen numbers from zero to sixteen occur, and seven do not.

*Proof.* The theorem and the count $17-10=7$.

**The pattern of the table.** The set is not closed under addition: $3+3=6$ is a value and $4+4=8$ is a value, while $3+4=7$ is not. The set is closed under multiplication, since the product of two products of numbers at most four is again such a product.

*Proof.* The first claim by the three examples, the second because $(rs)(r's')=(rr')(ss')$ and the two new factors are at most four.

**Corollary.** The rank values of $T_{A,B}$ are exactly the products of two numbers in $\{0,1,2,3,4\}$, and the seven absences are exactly the non-products.

*Proof.* The theorem, read as a statement about the multiplication table.

**The size of the strata.** The pairs of matrix ranks $(r,s)$ number twenty-five, and three of them give the value four, namely $(1,4)$, $(2,2)$ and $(4,1)$. The value is therefore not a complete invariant of the pair, and the stratum of operators of rank four is the union of three rank pairs.

*Proof.* Direct inspection of the table: the value four comes from the pairs with $rs=4$.

## The Stratification

**Definition.** For a pair of ranks $(r,s)$ let $\Sigma_{r,s}$ be the set of operators $T_{A,B}$ with $\operatorname{rank}A=r$ and $\operatorname{rank}B=s$.

**Proposition.** $\Sigma_{r,s}$ is a locally closed subvariety of the endomorphism algebra of dimension $8r-r^{2}+8s-s^{2}-1$, and its image under the Kronecker map is a single orbit of the group $\mathrm{GL}_4\times\mathrm{GL}_4$ acting on the two factors.

*Proof.* The matrices of rank $r$ in $M_4$ form an irreducible variety of dimension $8r-r^{2}$, the determinantal variety of the $(r+1)$-minors; the pair $(A,B)$ therefore ranges over a variety of dimension $8r-r^{2}+8s-s^{2}$; the operators $T_{A,B}$ and $T_{\lambda A,\lambda^{-1}B}$ coincide, and no other coincidence occurs, so the image loses exactly one dimension.

**Corollary.** The rank-one stratum $\Sigma_{1,1}$ has dimension thirteen and is the image of four copies of $\mathbb{P}^{3}$: the factor $A$ is an outer product $ab^{\mathsf T}$ and the factor $B$ an outer product $cd^{\mathsf T}$, and the operator is the rank-one operator attached to the pair of decomposable tensors.

*Proof.* With $A=ab^{\mathsf T}$ and $B=cd^{\mathsf T}$ one has $T_{A,B}(X)=a\,(b^{\mathsf T}Xc)\,d^{\mathsf T}$, an operator of rank one; the four vectors are each defined up to a scalar, so the stratum is the image of $\mathbb{P}^{3}\times\mathbb{P}^{3}\times\mathbb{P}^{3}\times\mathbb{P}^{3}$, of dimension twelve, with a cone direction.

**Corollary.** The rank-one stratum is contained in the cone of all rank-one operators on the sixteen-dimensional space, which is the cone over $\mathbb{P}^{15}\times\mathbb{P}^{15}$ of dimension thirty-one, and it is the intersection of that cone with the image of the two-sided operators.

*Proof.* A rank-one operator is an outer product of two vectors of the sixteen-dimensional space; the two-sided operators with both factors of rank one are exactly those whose two vectors are decomposable, first as $a\otimes c$ and second as $b\otimes d$.

**Corollary.** The value sixteen occurs on a single stratum, the pair $(4,4)$, which is open and dense in the family of two-sided operators; the value zero occurs only at the zero operator.

*Proof.* The product is sixteen only for $(4,4)$, and it is zero only when one factor is zero.

**The closure order.** The closure of $\Sigma_{r,s}$ contains $\Sigma_{r',s'}$ exactly when $r'\le r$ and $s'\le s$, so the ten values are not nested as numbers but the strata are nested as pairs. The value four therefore lies above three different pairs, and the stratification by the ten numbers is coarser than the stratification by the twenty-five pairs.

*Proof.* The determinantal varieties are nested by rank, and the product map is monotone in each factor.

## The Comparison with the Biquaternion Row

**Proposition.** At $n=2$, where the factors range over the biquaternion algebra and have rank at most two, the operator rank of $T_{a,b}$ takes exactly the values $\{0,1,2,4\}$, and the single absence is three.

*Proof.* The products of two numbers in $\{0,1,2\}$ are $0,1,2,4$; the product $2\cdot2=4$ is the full rank of the operator on the four-dimensional space, and three is not a product.

**Corollary.** The rank law is the same law at both rows; only the range of the factors changes.

*Proof.* The Kronecker form does not depend on the order.

**The reading.** At $n=2$ the operator algebra is $M_4(\mathbb{C})$, of dimension sixteen, and the two-sided operators form a seven-dimensional cone; at $n=4$ the operator algebra is $M_{16}(\mathbb{C})$, of dimension $256$, and the two-sided operators form a thirty-one-dimensional variety. In both cases the operator rank is the product of two matrix ranks, and the difference between the two sets of values is the difference between the ranges $\{0,1,2\}$ and $\{0,1,2,3,4\}$.

## The Law at General Order

**Proposition.** At order $n$ the operator rank of $T_{A,B}$ on $M_n(\mathbb{C})$ takes exactly the values $\{rs:0\le r,s\le n\}$, a set of $P(n)$ numbers where $P$ counts the distinct products of two integers between zero and $n$.

*Proof.* The Kronecker form and the rank law, with the factors of rank at most $n$.

**The small cases.** For $n=2$ the set is $\{0,1,2,4\}$, four values. For $n=3$ it is $\{0,1,2,3,4,6,9\}$, seven values. For $n=4$ it is the ten values of the theorem. For $n=5$ it is $\{0,1,2,3,4,5,6,8,9,10,12,15,16,20,25\}$, fifteen values. The count grows more slowly than $n^{2}$, since many products coincide.

*Proof.* Multiplication tables of the four sets, computed directly.

**Corollary.** At $n=2$ the only absence below the maximum is three; at $n=3$ the absences below nine are three numbers, five, seven and eight; at $n=4$ they are seven numbers.

*Proof.* Comparison of the set of products with the full range.

## The Boundary

**Against the length.** *The Length and the Two Ranks at $n=4$* studies two numbers attached to a single matrix: its matrix rank, the dimension of its column space, and its length, the smallest number of two-sided products whose sum it is. Both are at most four, and the length is the rank of the coefficient matrix, which is a matrix of order four. The present article studies a third number, the rank of the operator, which is at most sixteen and is the product of two matrix ranks. A matrix of rank one can have operator rank sixteen, as the identity does; the two notions are independent.

**Against the Segre cone.** The cone of *The Two-Sided Operators and the Segre Cone at $n=4$* is the set of operators of length one, that is, of coefficient matrix of rank one, and its dimension is seven. The rank-one stratum of the present article is a different set: it is the set of operators of operator rank one, of dimension thirteen. The two sets meet and neither contains the other.

**Against the rank of the algebra element.** The matrix rank of $A$ itself, as an element of $M_4(\mathbb{C})$, is one of the two factors and not the product. The distinction between the three numbers is the reason the word rank is always qualified in this section of the corpus.

## Summary

The two-sided operator $T_{A,B}(X)=AXB$ has operator rank $\operatorname{rank}A\cdot\operatorname{rank}B$, by the Kronecker form and the multiplicativity of the rank of a tensor product. The operator rank therefore takes exactly the ten values $0,1,2,3,4,6,8,9,12,16$ and never $5,7,10,11,13,14,15$, and the seven absences are the integers between zero and sixteen that are not products of two numbers at most four.

The pairs of matrix ranks stratify the family of two-sided operators, the stratum of a pair having dimension $8r-r^{2}+8s-s^{2}-1$, with the closures nested by the product order. The rank-one stratum is the image of four projective three-spaces, and it sits inside the cone of rank-one operators on the sixteen-dimensional space. At $n=2$ the same law gives the four values $0,1,2,4$ and the single absence three, and at general $n$ the values are the products of two integers between zero and $n$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_{A,B}(X)=AXB$ | the two-sided operator |
| $\operatorname{rank}A$ | the matrix rank, at most four |
| $\operatorname{rank}T_{A,B}$ | the operator rank, at most sixteen |
| $\Sigma_{r,s}$ | the operators with factor ranks $r$ and $s$ |
| $L_A,R_B$ | the left and right multiplications |
| $\mathbb{P}^{3}$ | the projective space of lines of $\mathbb{C}^4$ |

## Further Reading

- [The Two-Sided Operators and the Segre Cone at $n=4$](the-two-sided-operators-and-the-segre-cone-at-n-4.html), for the product rule and the coefficient matrix.
- [The Left Ideals and the Image of a Left Multiplication at $n=4$](the-left-ideals-and-the-image-of-a-left-multiplication-at-n-4.html), for the dimension of the two-sided image.
- [The Length and the Two Ranks at $n=4$](the-length-and-the-two-ranks-at-n-4.html), for the length and the matrix rank.
- [$\operatorname{End}(M_4(\mathbb{C}))$ as an Algebra: the Regular Representation](end-m4c-as-an-algebra-the-regular-representation.html), for the Kronecker identification of the endomorphism algebra.
- [The Kronecker Factorisation $M_4(\mathbb{C})\cong M_2(\mathbb{C})\otimes M_2(\mathbb{C})$](the-kronecker-factorisation-of-m4c-into-m2c-tensor-m2c.html), for the tensor form used in the proof.
