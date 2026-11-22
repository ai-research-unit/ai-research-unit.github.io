# __The Hermitian Pair of Operators Acting on One Side in $M_n(\mathbb{C})$__

## Introduction

**The question.** What are the Hermitian and anti-Hermitian parts of a one-sided operator, and what real and complex structures do they define on the carrier?

**The answer in one line.** The decomposition of $L_A$ is read off from the decomposition of $A$,
$$
L_A=L_H+iL_K,\qquad H=\tfrac12(A+A^{*}),\quad K=\tfrac1{2i}(A-A^{*}),
$$
so the self-adjoint part of the left copy is the real space of Hermitian matrices, of real dimension $n^2$, and it is not a complex subspace.

**Why the article is needed.** The biquaternion article could describe the Hermitian part as the real part of a $4\times4$ matrix and the anti-Hermitian part as the imaginary part. At general $n$ the split is the split of the parameter into its Hermitian and skew-Hermitian parts, and the two parts have different real dimensions and different algebraic roles: one is a Jordan algebra, the other a Lie algebra.

**Boundaries.** The adjoints are *The Adjoint Pair of $L$ and $R$ Operators on $M_n(\mathbb{C})$*; the two-sided Hermitian pairs are *The Hermitian Pair of Operators Acting on Two Sides in $M_n(\mathbb{C})$*; the cone of positive elements is *Positivity and the Positive Cone of $M_n(\mathbb{C})$*. The biquaternion original is *The Hermitian Pair of Operators Acting on One Side*.

**Conventions.** $H=\tfrac12(A+A^{*})$ and $K=\tfrac1{2i}(A-A^{*})$ are Hermitian. The Hilbert–Schmidt form is $\langle S,T\rangle=\operatorname{tr}(S^{*}T)$. The real vector space of Hermitian matrices is written $M_n^{\mathrm{sa}}$.

## The Two Parts

**Proposition.** Every $A$ has a unique decomposition $A=H+iK$ with $H,K$ Hermitian, and correspondingly
$$
L_A=L_H+iL_K,\qquad L_H=L_H^{\dagger},\qquad (iL_K)^{\dagger}=-iL_K .
$$

*Proof.* $H$ and $K$ are Hermitian by construction, and uniqueness follows from $A^{*}=H-iK$. The adjoint of $L_H$ is $L_{H^{*}}=L_H$, and the adjoint of $iL_K$ is $-iL_K$. $\square$

**The real dimensions.** $M_n^{\mathrm{sa}}$ has real dimension $n^2$, and the skew-Hermitian matrices $iM_n^{\mathrm{sa}}$ also have real dimension $n^2$. Together they give the $2n^2$ real dimensions of $M_n$.

**The two are not complex subspaces.** Multiplication by $i$ exchanges them, so neither is invariant under the complex structure of $M_n$. This is the whole difference from the transpose split of *Operator Chirality on $M_n(\mathbb{C})$*, where both halves are complex subspaces.

## Self-Adjointness

**Proposition.** $L_A$ is self-adjoint if and only if $A$ is Hermitian; $L_A$ is anti-self-adjoint if and only if $A$ is skew-Hermitian.

*Proof.* $L_A^{\dagger}=L_{A^{*}}$, and $L$ is injective. $\square$

**The real space.** The self-adjoint operators of the left copy form the real space $L(M_n^{\mathrm{sa}})$, of real dimension $n^2$. It is a real subspace and not a complex one: $iL_A=L_{iA}$ is anti-self-adjoint for nonzero Hermitian $A$.

**The spectral reading.** A self-adjoint one-sided operator has real spectrum, namely the spectrum of the Hermitian parameter. The spectral theorem for the one-sided operator is the spectral theorem for the parameter, transported by $L$.

## Positivity

**Proposition.** $L_A\ge0$ if and only if $A\ge0$.

*Proof.* $\langle X,L_AX\rangle=\operatorname{tr}(X^{*}AX)$, which is nonnegative for all $X$ exactly when $A$ is positive semidefinite. $\square$

**The cone.** The positive one-sided operators form a closed convex cone isomorphic to the cone of positive semidefinite matrices. Its interior is the set of $L_A$ with $A>0$, and its extreme rays are the $L_A$ with $A$ of rank one.

**The order.** $L_A\le L_B$ exactly when $A\le B$, so the Loewner order on $M_n$ is transported to the left copy without change.

**The trace.** $\operatorname{tr}L_A=n\operatorname{tr}A$, so the trace functional on the left copy is $n$ times the trace of the parameter.

## The Real and the Complex Structure

**The conjugation.** $\Theta(X)=X^{*}$ is a conjugate-linear involution of the carrier. It does not preserve the left copy: it sends it to the right copy, $\Theta L_A=R_{A^{*}}\Theta$.

**The consequence for the Hermitian pair.** The Hermitian part of $L_A$ is the fixed part under the adjoint, and the adjoint is not a real structure of the left copy alone. What the left copy carries is a real form in the weaker sense of a real subspace, $L(M_n^{\mathrm{sa}})$, of real dimension $n^2$.

**The complexification.** The complexification of $L(M_n^{\mathrm{sa}})$ is $L(M_n)$, the whole left copy: every $L_A$ is $L_H+iL_K$ with both parts in the real space. So the left copy is the complexification of the Hermitian one-sided operators.

**The unitary group.** $L_A$ is unitary exactly when $A$ is unitary, so the left copy contains a copy of $U(n)$ acting on the carrier. Its Lie algebra is the anti-self-adjoint part $iL(M_n^{\mathrm{sa}})$, of real dimension $n^2$, and the Hermitian part is the complement.

**The polar decomposition.** For $A=U\lvert A\rvert$ with $U$ unitary, $L_A=L_UL_{\lvert A\rvert}$, and $L_{\lvert A\rvert}$ is the positive part. So the polar decomposition of the one-sided operator is the polar decomposition of the parameter, and it is unique exactly when $A$ is invertible.

## The Jordan and the Lie Structure

**The Hermitian part is a Jordan algebra.** For Hermitian $H,K$ the product $HK$ need not be Hermitian, but the symmetrised product $\tfrac12(HK+KH)$ is, and $M_n^{\mathrm{sa}}$ with this product is a real Jordan algebra. The map $H\mapsto L_H$ transports the Jordan product to the symmetrised product of operators.

**The skew part is a Lie algebra.** For skew-Hermitian $K_1,K_2$ the commutator is skew-Hermitian, and $iM_n^{\mathrm{sa}}$ with the commutator is the real Lie algebra $\mathfrak{u}(n)$, of dimension $n^2$.

**The two fit together.** $M_n$ as a real algebra is the complexification of both: the Jordan algebra $M_n^{\mathrm{sa}}$ and the Lie algebra $\mathfrak{u}(n)$ are two real forms of the same complex object, and the Hermitian pair of a one-sided operator sees both.

## The Finite Check

Computed with numpy for $n=2,3,4,5$: for random complex $A$, the residual $\lVert L_A-L_H-iL_K\rVert$ is below $10^{-15}$, and $\lVert L_H-L_H^{\dagger}\rVert$, $\lVert(iL_K)^{\dagger}+iL_K\rVert$ are below $10^{-15}$. The real dimension of the self-adjoint part, computed as the rank of the real linear system $L_A=L_A^{\dagger}$ over the $2n^2$ real parameters, is $n^2$: it is $4,9,16,25$ for $n=2,3,4,5$.

The positivity test agrees in both directions: for $A$ sampled as $B^{*}B$, the smallest eigenvalue of $L_A$ is nonnegative, and for $A$ sampled as $B^{*}B-\lambda\mathrm I$ with $\lambda$ larger than the top eigenvalue of $B^{*}B$ it is negative; in both cases the sign agrees with that of the smallest eigenvalue of $A$.

## The Three Real Subspaces

**The self-adjoint part.** The one-sided operators that are self-adjoint for the Hilbert–Schmidt form are the $L_A$ with $A$ Hermitian, a real vector space of dimension $n^2$.

**The skew part.** The skew-adjoint one-sided operators are the $L_A$ with $A$ skew-Hermitian, also of dimension $n^2$.

**The unitary part.** The one-sided operators that are unitary are the $L_U$ with $U$ unitary, a group isomorphic to $U(n)$, of real dimension $n^2$.

**The table.**

| $n$ | $\dim\{\text{self-adjoint}\}$ | $\dim\{\text{Hermitian }A\}$ | $\dim U(n)$ |
|---|---|---|---|
| $2$ | $4$ | $4$ | $4$ |
| $3$ | $9$ | $9$ | $9$ |
| $4$ | $16$ | $16$ | $16$ |
| $5$ | $25$ | $25$ | $25$ |

**The reading.** The three real subspaces have the same dimension, because the Hermitian and skew-Hermitian parts are the two halves of the real space of parameters and the unitary group is the exponentiated skew part.

## The Polar Decomposition

**Proposition.** Every $L_A$ factors as $L_UL_{\lvert A\rvert}$ with $U$ unitary and $\lvert A\rvert$ positive semidefinite, and the factorisation is unique when $A$ is invertible.

*Proof.* $A=U\lvert A\rvert$ and $L$ is multiplicative. $\square$

**The consequence.** The one-sided operators decompose into a unitary part and a positive part, and the two parts commute. The positive part carries the singular values, the unitary part the phases.

**The reading at $n=2$.** The four real dimensions of the parameter give a circle of unitary parts and a three-dimensional cone of positive parts; the biquaternion description of the positive cone is the case $n=2$ of the same decomposition.

## The Commutation with the Conjugation

**Proposition.** With $\Theta(X)=X^{*}$ one has $\Theta L_A\Theta=R_{A^{*}}$ and $\Theta R_B\Theta=L_{B^{*}}$.

*Proof.* $\Theta L_A\Theta(X)=(AX^{*})^{*}=XA^{*}=R_{A^{*}}(X)$. $\square$

**The consequence.** The conjugation exchanges the two one-sided families, so the real structure pairs a left multiplication with a right one. A one-sided operator is $\Theta$-real only when the two coincide, which requires $A$ central.

**The reading.** The Hermitian pair of a left multiplication is a right multiplication by the adjoint parameter, and that is the one-sided shadow of the two-sided statement $\Theta T_{A,B}\Theta=T_{B^{*},A^{*}}$.

**The self-adjoint case.** For $A$ Hermitian, $\Theta L_A\Theta=R_A$, so the conjugation carries the self-adjoint left family to the self-adjoint right family, and the two families are mirror images.

## The Real Space of Parameters

**The decomposition.** $M_n=\mathfrak{u}(n)\oplus i\mathfrak{u}(n)$ as real spaces, so the parameter space splits into a skew part and a Hermitian part, each of real dimension $n^2$.

**The images.** The skew part maps to the unitary directions of $L$ and the Hermitian part to the self-adjoint directions, and the two images are orthogonal for the Hilbert–Schmidt form.

**The reading.** A one-sided operator is unitary exactly when its parameter is skew-Hermitian, and self-adjoint exactly when its parameter is Hermitian; the two conditions are the two real halves of one complex condition.

## Summary

The Hermitian and anti-Hermitian parts of a one-sided operator are the one-sided operators of the Hermitian and skew-Hermitian parts of the parameter. The self-adjoint part is a real space of dimension $n^2$, a Jordan algebra, and the anti-self-adjoint part is $\mathfrak{u}(n)$, a Lie algebra. Positivity is transported without change. The adjoint operation itself exchanges the two copies, so it is a real structure of the pair rather than of one side.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H,K$ | the Hermitian and skew-Hermitian parts of $A$ |
| $M_n^{\mathrm{sa}}$ | the real space of Hermitian matrices, dimension $n^2$ |
| $L(M_n^{\mathrm{sa}})$ | the self-adjoint one-sided operators |
| $\Theta$ | the conjugation $X\mapsto X^{*}$ |
| $\mathfrak{u}(n)$ | the skew-Hermitian matrices with the commutator |

## Further Reading
- [The Adjoint Pair of $L$ and $R$ Operators on $M_n(\mathbb{C})$](the-adjoint-pair-of-l-and-r-operators-on-mnc.html), for the adjoints.
- [The One-Sided Operators of $M_n(\mathbb{C})$](the-one-sided-operators-of-mnc.html), for the copies.
- [Hermitian and Anti-Hermitian Elements](hermitian-and-anti-hermitian-elements.html), for the element-level split.
- [Positivity and the Positive Cone of $M_n(\mathbb{C})$](the-cone-of-positive-operators.html), for the cone.
- [The Hermitian Pair of Operators Acting on One Side](the-hermitian-pair-of-operators-acting-on-one-side.html), for the case $n=2$.
- [The Hermitian Pair of Operators Acting on Two Sides in $M_n(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-two-sides-in-mnc.html), for the two-sided version.
