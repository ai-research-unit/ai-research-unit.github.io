# __The SVD of Endomorphisms of $M_n(\mathbb{C})$__

## Introduction

**The question.** What are the singular values of a linear map of $M_n(\mathbb{C})$ into itself, and what does the tensor structure of the operator algebra say about them?

**The answer in one line.** For a single product the singular values are the $n^2$ numbers
$$
\sigma_i(A)\sigma_j(B),\qquad 1\le i,j\le n,
$$
the operator norm is $\lVert A\rVert_2\lVert B\rVert_2$, and every Schatten norm is multiplicative.

**Why the article is needed.** The biquaternion article computed the singular values of an endomorphism by writing it as a $4\times4$ matrix and taking its four singular values. At general $n$ an operator has $n^2$ singular values, and for a single product they are not $n^2$ independent numbers but a rank-one table of $n$ numbers against $n$ numbers. The count and the factorisation are both new.

**Boundaries.** The operator families are *The Endomorphisms of $M_n(\mathbb{C})$*; the matrix form is *The Axis-Free $M_{n^2}(\mathbb{C})$ Representation of the Operators of $M_n(\mathbb{C})$*; the length and the two ranks are *The Length and the Two Ranks on $M_n(\mathbb{C})$*. The biquaternion original is *The SVD Decomposition of Endomorphisms of the Biquaternion Algebra*.

**Conventions.** $T_{A,B}(X)=AXB$. For a matrix $A$ write $A=U_A\Sigma_AV_A^{*}$ with $\sigma_1(A)\ge\cdots\ge\sigma_n(A)\ge0$. The Schatten $p$-norm is $\lVert A\rVert_p=(\sum_i\sigma_i(A)^p)^{1/p}$, with $\lVert A\rVert_\infty=\sigma_1(A)$.

## The Singular Values of a Product

**Proposition (the SVD of $T_{A,B}$).** With $A=U_A\Sigma_AV_A^{*}$ and $B=U_B\Sigma_BV_B^{*}$,
$$
T_{A,B}=(V_B^{\mathsf T}\otimes U_A)\,(\Sigma_B\otimes\Sigma_A)\,(U_B^{\mathsf T}\otimes V_A)^{*} .
$$

*Proof.* $B^{\mathsf T}=\overline{V_B}\Sigma_BU_B^{\mathsf T}$, and $(U_B^{\mathsf T})^{-1}=V_B^{\mathsf T}$ because $U_B$ is unitary. The outer factors are unitary, being Kronecker products of unitary matrices, and the middle factor is diagonal because both factors are. $\square$

**Corollary.** The singular values of $T_{A,B}$ are $\sigma_i(A)\sigma_j(B)$ with multiplicity one each, and
$$
\operatorname{rank}T_{A,B}=\operatorname{rank}A\operatorname{rank}B,\qquad \lVert T_{A,B}\rVert_2=\lVert A\rVert_2\lVert B\rVert_2 .
$$

*Proof.* The diagonal of $\Sigma_B\otimes\Sigma_A$ consists of the products, in the order of the Kronecker product. The rank is the number of nonzero products, which is the product of the numbers of nonzero factors. $\square$

**The factorisation is rank one in the table.** Arrange the $n^2$ singular values as an $n\times n$ table with entry $\sigma_i(A)\sigma_j(B)$. The table has rank one as a matrix. This is the statement that the biquaternion SVD could not make: four numbers, but four numbers of the form $x_iy_j$.

**Schatten norms.** For every $p\in[1,\infty]$,
$$
\lVert T_{A,B}\rVert_p=\lVert A\rVert_p\lVert B\rVert_p ,
$$
because the sum of the $p$-th powers of the products factorises: $\sum_{ij}(\sigma_i\sigma_j)^p=(\sum_i\sigma_i^p)(\sum_j\sigma_j^p)$.

**The inner product.** For the Hilbert–Schmidt form,
$$
\langle T_{A,B},T_{C,D}\rangle=\langle A,C\rangle\langle B,D\rangle ,
$$
so the identification $A\otimes B\mapsto T_{A,B}$ is a Hilbert-space isometry of $M_n\otimes M_n$ onto the operator space; it is the flip of the two tensor slots composed with the canonical identification.

**The modulus.** $T_{A,B}^{*}T_{A,B}=T_{A^{*}A,BB^{*}}$, so
$$
\lvert T_{A,B}\rvert=T_{\lvert A\rvert,\lvert B^{*}\rvert},
$$
the modulus of a product is the product of the moduli. The unitary part of the polar decomposition is $T_{U_A,V_B^{*}}$ on the range.

## The Degenerate Cases

**A singular factor.** If $\operatorname{rank}A=r$ and $\operatorname{rank}B=s$, then $T_{A,B}$ has rank $rs$ and kernel of dimension $n^2-rs$. The image is $AM_nB=\{AXB\}$, which is spanned by the $rs$ products of the chosen bases of the row and column spaces.

**A vanishing factor.** $T_{A,B}=0$ exactly when $A=0$ or $B=0$.

*Proof.* $T_{A,B}(E_{kl})=A_{ik}B_{lj}$ entrywise, so all these vanish for all $i,j,k,l$ only if every product $A_{ik}B_{lj}$ vanishes. If $A\neq0$ some $A_{ik}\neq0$, and then all $B_{lj}=0$. $\square$

**The condition number.** For invertible $A,B$,
$$
\kappa(T_{A,B})=\kappa(A)\kappa(B),
$$
the ratio of the largest to the smallest product being the product of the ratios.

**The zero singular values.** The number of zero singular values is $n^2-rs$, the same as the kernel dimension, and it is never $n^2$ unless one factor vanishes. So a nonzero product is never a quasinilpotent, and the smallest singular value of $T_{A,B}$ is $\sigma_n(A)\sigma_n(B)$.

## The One-Sided Operators

**The singular values of $L_A$.** $L_A=T_{A,\mathrm I}=\mathrm I\otimes A$, so its singular values are the $\sigma_i(A)$, each with multiplicity $n$.

**The singular values of $R_B$.** $R_B=T_{\mathrm I,B}=B^{\mathsf T}\otimes\mathrm I$, so its singular values are the $\sigma_i(B)$, each with multiplicity $n$.

**The consequence.** A one-sided operator is as far from a general product as possible in its singular values: the table $\sigma_i(A)\sigma_j(\mathrm I)$ has $n$ distinct rows, all equal, so its rank-one structure is degenerate in the other direction. This is why the one-sided operators form a subspace of dimension $n^2$ inside the $n^4$-dimensional space, while the two-sided products do not form a subspace at all.

**The spectra.** The eigenvalues of $T_{A,B}$ are the products $\lambda_i(A)\lambda_j(B)$ with algebraic multiplicity, because the eigenvalues of a Kronecker product multiply and the two factors are triangularisable in a common flag after a unitary change of each. Weyl's inequality gives $\lvert\lambda_i(A)\lambda_j(B)\rvert\le\sigma_1(A)\sigma_1(B)$, with equality for normal $A,B$.

## A General Endomorphism

**The terms.** A general operator is a sum $M=\sum_{\nu=1}^{m}T_{A_\nu,B_\nu}$. The least $m$ is the length $\ell(M)$, and the rank of the operator is at most $\sum_\nu\operatorname{rank}A_\nu\operatorname{rank}B_\nu$. The two quantities are independent, and the length is computed in *The Length and the Two Ranks on $M_n(\mathbb{C})$*.

**The singular values of a sum.** There is no product formula. The singular values of $T_{A,B}+T_{C,D}$ are those of the sum of two Kronecker products, and they depend on the relative position of the four matrices. What survives is the inequality $\lVert T_{A,B}+T_{C,D}\rVert_2\le\lVert A\rVert_2\lVert B\rVert_2+\lVert C\rVert_2\lVert D\rVert_2$.

**The best rank-one approximation.** By Eckart–Young in the operator Hilbert space, the best approximation of $M$ by a single product is obtained from the largest singular triple of the $n^2\times n^2$ matrix of $M$. For $M=T_{A,B}$ that triple is $\sigma_1(A)\sigma_1(B)$ with the vector $v_1(B)\otimes u_1(A)$, so the approximation is exact and recovers the two leading vectors.

**What the SVD does not see.** The SVD of $T_{A,B}$ is the SVD of the operator, not of the pair. Two different pairs can have the same operator only if they differ by a scalar, $T_{A,B}=T_{\lambda A,\lambda^{-1}B}$, so the pair is determined up to one parameter and the SVD determines the singular values only up to the same ambiguity.

## Comparison with the Biquaternion SVD

**The four numbers.** At $n=2$ the operator space has dimension $16$ and its matrices are $4\times4$, so an operator has four singular values. For a product they are $\sigma_1\sigma_1,\sigma_1\sigma_2,\sigma_2\sigma_1,\sigma_2\sigma_2$.

**What the $4\times4$ reading hid.** The biquaternion article listed four numbers and read the largest as the operator norm. The tensor reading says the four numbers are a product table, so the largest is the product of the two largest, and the operator norm is multiplicative in the pair. The biquaternion article's norm formula agrees numerically at $n=2$ but does not display the factorisation, because in a $4\times4$ frame there is no pair to factor over.

**What does not generalise.** At $n=2$ the four singular values satisfy the relation $\lambda_1\lambda_4=\lambda_2\lambda_3$, which is the rank-one condition on a $2\times2$ table. At general $n$ the corresponding condition is that the $n\times n$ table of singular values has rank one. That is a much stronger statement than any single relation among $n^2$ numbers, and it is the exact sense in which a product is a degenerate operator.

## The Finite Check

Computed with numpy for $n=2,3,4,5$, on random complex $A,B$: the sorted singular values of $T_{A,B}=B^{\mathsf T}\otimes A$ agree with the sorted products $\sigma_i(A)\sigma_j(B)$ to $10^{-14}$; the Schatten ratios $\lVert T\rVert_p/(\lVert A\rVert_p\lVert B\rVert_p)$ equal $1$ for $p=1,2,\infty$; the rank identity $\operatorname{rank}T=\operatorname{rank}A\operatorname{rank}B$ holds for random ranks $r,s$ obtained by truncating the SVD.

The inner-product identity was checked on random pairs: $\langle T_{A,B},T_{C,D}\rangle-\langle A,C\rangle\langle B,D\rangle$ is of the order of $10^{-15}$ at $n=3$. The modulus identity $\lvert T_{A,B}\rvert=T_{\lvert A\rvert,\lvert B^{*}\rvert}$ is exact from $T^{*}T=T_{A^{*}A,BB^{*}}$ and was checked by comparing the positive square roots at $n=3$.

### The Ordered Lists

At $n=2$ with $A=B=\operatorname{diag}(2,1)$ the singular values of $T_{A,B}$ are $4,2,2,1$: the four products, with the middle value repeated because $2\cdot1=1\cdot2$.

**The multiplicity.** A repeated product $\sigma_i(A)\sigma_j(B)=\sigma_{i'}(A)\sigma_{j'}(B)$ with $(i,j)\neq(i',j')$ occurs when the two lists have a common ratio; a generic pair of lists gives $n^2$ distinct products, and the generic multiplicity is one.

**The two normalisations.** The Hilbert–Schmidt norm of $T_{A,B}$ is $\lVert A\rVert_2\lVert B\rVert_2$ and the operator norm is $\lVert A\rVert\lVert B\rVert$, so the ratio of the two norms of the product is the product of the ratios of the parameters.

**The consequence for inversion.** When both parameters are invertible the inverse of $T_{A,B}$ is $T_{A^{-1},B^{-1}}$, of norm $\lVert A^{-1}\rVert\lVert B^{-1}\rVert$; the condition number of the product is the product of the condition numbers.

**The reading.** The singular value picture of the two-sided family is the product picture. It contains no information that is not in the two lists, and that is why the general case is simpler than the biquaternion case, where the four-dimensional frame mixed the two lists into one.

### The Symmetric Case

**The values.** For Hermitian $A$ and $B$ the singular values of $T_{A,B}$ are $\lvert\lambda_i(A)\lambda_j(B)\rvert$, the absolute values of the eigenvalues.

**The comparison.** The eigenvalue list and the singular value list differ by the signs of the eigenvalues, and the two agree exactly when both parameters are positive semidefinite.

**The reading.** The singular value picture is the eigenvalue picture with the signs forgotten, and for the two-sided family the signs are the signs of the two parameters, one per factor.

### The Rank

**Proposition.** $\operatorname{rank}T_{A,B}=\operatorname{rank}(A)\operatorname{rank}(B)$.

*Proof.* $T_{A,B}=B^{\mathsf T}\otimes A$, and the rank of a Kronecker product is the product of the ranks. $\square$

**The reading.** The rank is the number of nonzero singular values, and it is multiplicative. A rank-one parameter gives a rank-$n$ operator, not a rank-one operator.

## Summary

A product has singular values $\sigma_i(A)\sigma_j(B)$, arranged as a rank-one $n\times n$ table. Its rank is the product of the ranks, its operator norm the product of the norms, and every Schatten norm is multiplicative. The modulus of a product is the product of the moduli. A general endomorphism is a sum of products and has no product formula for its singular values. At $n=2$ the four singular values form a $2\times2$ table, and that is the structure the $4\times4$ reading hid.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma_i(A)$ | the $i$-th singular value of $A$, decreasing |
| $\lVert\cdot\rVert_p$ | the Schatten $p$-norm, $p\in[1,\infty]$ |
| $\lvert A\rvert$ | the positive square root of $A^{*}A$ |
| $\kappa(A)$ | the condition number $\sigma_1/\sigma_n$ |
| $\ell(M)$ | the length, the least number of products |

## Further Reading
- Horn and Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the singular value inequalities.
- [The Endomorphisms of $M_n(\mathbb{C})$](the-endomorphisms-of-mnc.html), for the families and the tensor square.
- [The Axis-Free $M_{n^2}(\mathbb{C})$ Representation of the Operators of $M_n(\mathbb{C})$](the-axis-free-representation-of-the-operators-of-mnc.html), for the Kronecker form used here.
- [The Length and the Two Ranks on $M_n(\mathbb{C})$](the-length-and-the-two-ranks-on-mnc.html), for the length of a general operator.
- [The SVD Decomposition of Endomorphisms of the Biquaternion Algebra](the-svd-decomposition-of-endomorphisms-of-the-biquaternion-algebra.html), for the case $n=2$.
- [The Singular Value Decomposition of the Operators on $\mathbb{C}^2$](the-singular-value-decomposition-of-the-operators-on-c2.html), for the smallest case in the operator frame.
