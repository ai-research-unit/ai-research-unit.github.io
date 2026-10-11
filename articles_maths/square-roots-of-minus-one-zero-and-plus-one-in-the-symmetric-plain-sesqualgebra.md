# __Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Sesqualgebra__

## Introduction

The symmetric plain sesqualgebra is the operation $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ on the biquaternion space (*Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*). This article determines the **roots** of the three central values $-1$, $0$ and $+1$: the nonzero elements $\tilde{Q}$ satisfying $\tilde{Q}\star\tilde{Q} = \lambda e_0$ for $\lambda = -1$, $0$ and $+1$.

The reduction is short and it settles the three sets at once. The square of an element is $\tilde{Q}\star\tilde{Q} = N(\tilde{Q})e_0$, with $N(\tilde{Q}) = H(\tilde{Q},\tilde{Q}) = \sum_\mu\lvert Q_\mu\rvert^{2}$ the norm of the block (*Norm and Invertibility in the Symmetric Plain Sesqualgebra*), a real non-negative number. The equation of the root is therefore a real positivity, $\sum_\mu\lvert Q_\mu\rvert^{2} = \lambda$, and the three central values separate: **minus one has no root**, because the sum is non-negative; **zero has no root**, because the sum vanishes only with the element; and **plus one has a root**, exactly the elements of norm one, a real quadric of real dimension seven. The block carries no root of $-1$ and no nonzero root of $0$, and this is the sign of the difference from the plain product, where both classes are nonempty and they classify the idempotents and the nilpotents.

**Placement.** The article is the fourth entry of the *Common Theory* section of the block, after the zero divisors and before the square roots of a general element. It uses the product and the class of the introduction, the norm and the definiteness of *Norm and Invertibility in the Symmetric Plain Sesqualgebra*, and the zero-divisor set of *Zero Divisors of the Symmetric Plain Sesqualgebra*; it feeds the idempotent article of the block, *Idempotents of the Symmetric Plain Sesqualgebra*.

**Boundaries.** The product, its class and its placement are *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*; the relative definition of the root, of the square root and of the three central values is *Definitions for the Study of the 12 Algebraic Structures*. The three sets of the parent are *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*, and the general reduction is *Square Roots of a General Element in the General Plain Algebra*. The idempotents and the nilpotents of the parent are *Idempotents of the General Plain Algebra* and *Nilpotents of the General Plain Algebra*, and the roots of the block read on the idempotents are *Idempotents of the Symmetric Plain Sesqualgebra*. Nothing topological and nothing metric appears.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with central scalar imaginary $i$. A general element is $\tilde{Q} = \sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; the natural conjugation is $\tilde{Q}^{\natural} = \sum_\mu\varepsilon_\mu Q_\mu e_\mu$ with $\varepsilon = (1,-1,-1,-1)$, the coefficientwise conjugation is $\overline{\tilde{Q}} = \sum_\mu\overline{Q_\mu}e_\mu$, and the Hermitian conjugation is $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$. The product of the block is

$$
\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0, \qquad H(\tilde P,\tilde Q) = \sum_{\mu=0}^{3}P_\mu\overline{Q_\mu},
$$

and the norm is $N(\tilde{Q}) = H(\tilde{Q},\tilde{Q}) = \sum_\mu\lvert Q_\mu\rvert^{2}$.

## The Problem and Its Reduction

**Definition (recalled).** A **root of $\lambda$** in the block is a nonzero element $\tilde{Q}$ with $\tilde{Q}\star\tilde{Q} = \lambda e_0$; the **root set** of $\lambda$ is the set of such elements. The definition is that of *Definitions for the Study of the 12 Algebraic Structures*, read on the product $\star$; a root of $0$ is a nonzero square-zero element, and a root of $+1$ is a nonzero element of square one.

**Theorem (the reduction).** For every $\tilde{Q}\in\mathbb{B}$,

$$
\tilde{Q}\star\tilde{Q} = N(\tilde{Q})e_0 = \Bigl(\sum_{\mu=0}^{3}\lvert Q_\mu\rvert^{2}\Bigr)e_0,
$$

with $N(\tilde{Q})$ a real non-negative number vanishing exactly at $\tilde{Q} = 0$. Consequently the equation $\tilde{Q}\star\tilde{Q} = \lambda e_0$ is the scalar equation $N(\tilde{Q}) = \lambda$ together with the requirement $\tilde{Q}\neq0$, and the three central values are read on the single real function $N$.

*Proof.* The display is the definition of the norm and the square map of *Norm and Invertibility in the Symmetric Plain Sesqualgebra*, $\tilde{Q}\star\tilde{Q} = N(\tilde{Q})e_0$, with $N(\tilde{Q}) = \sum_\mu\lvert Q_\mu\rvert^{2}$; a sum of squares of moduli is real and non-negative, and it vanishes exactly when every $Q_\mu$ does. The two sides of $\tilde{Q}\star\tilde{Q} = \lambda e_0$ are therefore central, and comparing the coefficients gives $N(\tilde{Q}) = \lambda$.

**Corollary (the trichotomy).** A necessary and sufficient condition for the existence of a root of $\lambda$ is $\lambda\in\mathbb{R}_{>0}$; for such a $\lambda$ the root set is the real quadric

$$
\{\tilde{Q}\in\mathbb{B} : N(\tilde{Q}) = \lambda\},
$$

a real algebraic set of real dimension seven. For $\lambda\in\mathbb{R}_{<0}$, for $\lambda\notin\mathbb{R}$, and for $\lambda = 0$ there is no root.

*Proof.* $N$ takes every positive real value, since $N(\sqrt{\lambda}e_0) = \lambda$ for $\lambda>0$, and takes no value outside $\mathbb{R}_{\geq0}$; at $\lambda = 0$ the only solution is $\tilde{Q} = 0$, which is excluded from being a root by the definition. The level set of the positive definite quadratic form $N$ at a positive value is a quadric whose real codimension is one, hence of real dimension seven.

## The Roots of Minus One

**Theorem (no root of $-1$).** There is no element $\tilde{Q}$ with $\tilde{Q}\star\tilde{Q} = -e_0$.

*Proof.* The equation reads $N(\tilde{Q}) = -1$ by the reduction, and $N(\tilde{Q}) = \sum_\mu\lvert Q_\mu\rvert^{2}\geq0$; no element has a negative norm.

**Remark (the sign of the rootlessness).** The block has no root of $-1$ because its form is definite; the plain product has a root of $-1$ for every splitting of the algebra, and the roots of $-1$ are in bijection with the idempotents (*Idempotents of the General Plain Algebra*). The block's idempotents are therefore not indexed by any root of $-1$; the idempotent theory of the block is *Idempotents of the Symmetric Plain Sesqualgebra* and it is not a reading of the present set.

## The Roots of Zero

**Theorem (no root of $0$).** The equation $\tilde{Q}\star\tilde{Q} = 0$ has the single solution $\tilde{Q} = 0$, so the block has no nonzero square-zero element and the root set of $0$ is empty.

*Proof.* The reduction reads $N(\tilde{Q}) = 0$, and the norm vanishes only at the origin; a root is required to be nonzero, so the set is empty.

**Remark (square-zero elements and nilpotents).** The block has no square-zero element, hence no nilpotent of index two; the index three exists nevertheless, and the nilpotents of the block are *Nilpotents of the Symmetric Plain Sesqualgebra*. The two statements are not in conflict: a nilpotent of index three carries a nonzero square and a vanishing cube, and its square is the central element $N(\tilde\Upsilon)e_0\neq0$.

## The Roots of Plus One

**Theorem (the roots of $+1$).** The root set of $+1$ is the quadric

$$
\mathcal{R}(+1) = \Bigl\{\tilde{Q}\in\mathbb{B} : \sum_{\mu=0}^{3}\lvert Q_\mu\rvert^{2} = 1\Bigr\},
$$

a real quadric of real dimension seven; it is nonempty, it contains the two elements $e_0$ and $ie_0$, and it is stable under the three conjugations and under complex multiplication by a scalar of modulus one.

*Proof.* The description is the corollary of the reduction at $\lambda = 1$. The elements $e_0$ and $ie_0$ have norm $1$ and are nonzero. The stability is that of $N$: $N(\lambda\tilde{Q}) = \lvert\lambda\rvert^{2}N(\tilde{Q})$, and each of the three conjugations preserves the moduli of the coordinates.

**Proposition (the roots of $+1$ are exactly the norm-one elements).** An element is a root of $+1$ if and only if it has norm one. Every root of $+1$ is a zero divisor of the block, and every root of $+1$ has a nonzero orthogonal companion, $\tilde{Q}^{\perp}$ being a hyperplane.

*Proof.* The first is the theorem. The zero-divisor statement is that every nonzero element is a zero divisor (*Zero Divisors of the Symmetric Plain Sesqualgebra*), and the companion is the hyperplane of the same article.

**Remark (the difference from the plain product).** In the plain product the roots of $+1$ are the image $\tilde P i$ of the roots of $-1$ under multiplication by $i$, and the idempotents are the different image $\tfrac12(e_0 + \tilde P i)$ of the same roots; here the roots of $+1$ are the norm-one quadric, a much larger set, and the idempotents of the block are only $0$ and $e_0$ (*Idempotents of the Symmetric Plain Sesqualgebra*). The element $e_0$ belongs to both descriptions, being an idempotent and a root of $+1$; every other root of $+1$ is not idempotent.

## The Three Sets Compared

| central value $\lambda$ | equation | root set | size |
|---|---|---|---|
| $-1$ | $N(\tilde{Q}) = -1$ | empty | none |
| $0$ | $N(\tilde{Q}) = 0$ | empty, $0$ being the only solution and excluded | none |
| $+1$ | $N(\tilde{Q}) = 1$ | the norm-one quadric | real dimension seven |

The three rows are read from the single real function $N$: the first two are its negative and its zero, forbidden by the definition of the root and by the definiteness, and the third is its value one. The block therefore carries exactly one of the three classes, and the one it carries is the largest.

**Corollary (the roots and the three conjugations).** The root set of $+1$ is carried to itself by the natural conjugation, by the coefficientwise conjugation, and by the Hermitian conjugation, these acting on the moduli of the coordinates; consequently a statement about a root of $+1$ is a statement about its three conjugates, and the root set is a real algebraic set closed under the three of them. The empty sets are stable for the same reason.

## The Relation to the Idempotents and to the Zero Divisors

**The idempotents.** The idempotents of the block, the elements with $\tilde{Q}\star\tilde{Q} = \tilde{Q}$, are $0$ and $e_0$ alone (*Idempotents of the Symmetric Plain Sesqualgebra*). The set of the idempotents meets the root set of $+1$ in the element $e_0$, and it meets the root sets of $-1$ and of $0$ nowhere: there is no idempotent of the block that is a root of either. The plain product's bijection between the idempotents and the roots of $-1$ is a bijection of the plain product and has no analogue here, because the present block has no root of $-1$.

**The zero divisors.** Every root of $+1$ is a zero divisor of the block, since every nonzero element is one; the converse fails, because the zero-divisor set is the whole punctured space and the root set of $+1$ is the norm-one quadric in it (*Zero Divisors of the Symmetric Plain Sesqualgebra*). Being a zero divisor is therefore no condition on the block, and the root condition is a genuine condition, the value of the norm.

**The sibling blocks.** The plain product has the three roots; the block has one. The difference lies in the sign of the diagonal: the plain product's quadratic form $\sum_\mu Q_\mu^{2}$ takes the two signs and vanishes off the origin, while the block's norm is definite, so the negative and the zero values are excluded. The comparison of the three central values with those of the parent is in *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*.

## Summary

The square of an element of the symmetric plain sesqualgebra is $\tilde{Q}\star\tilde{Q} = N(\tilde{Q})e_0$ with $N(\tilde{Q}) = \sum_\mu\lvert Q_\mu\rvert^{2}$ a real non-negative definite number, so the equation of the root $\tilde{Q}\star\tilde{Q} = \lambda e_0$ reduces to the scalar equation $N(\tilde{Q}) = \lambda$. The three central values separate on the sign: **minus one has no root**, the sum of squares being non-negative; **zero has no root**, the sum vanishing only at the origin and the origin being excluded; and **plus one has a root**, the root set being the norm-one quadric $\{N = 1\}$, a real quadric of real dimension seven, nonempty, containing $e_0$ and $ie_0$, stable under the three conjugations and under the multiplication by the complex scalars of modulus one. Every root of $+1$ is a zero divisor, and the converse fails because every nonzero element is one. The idempotents of the block are $0$ and $e_0$ and they meet the roots of $+1$ in $e_0$ alone; the plain product's bijection between the idempotents and the roots of $-1$ has no analogue, because the block has no root of $-1$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ | the product of the block |
| $N(\tilde{Q}) = H(\tilde{Q},\tilde{Q}) = \sum_\mu\lvert Q_\mu\rvert^{2}$ | the norm of the block, real and non-negative |
| $\tilde{Q}\star\tilde{Q} = N(\tilde{Q})e_0$ | the reduction of the root equation |
| $\mathcal{R}(+1) = \{N = 1\}$ | the root set of $+1$, the norm-one quadric, real dimension seven |
| $\mathcal{R}(-1) = \varnothing$ | no root of $-1$ |
| $\mathcal{R}(0) = \varnothing$ | no nonzero root of $0$ |
| $\tilde{Q}^{\natural}$, $\overline{\tilde{Q}}$, $\tilde{Q}^{*}$ | the three conjugations, acting on the root set by preserving the moduli of the coordinates |

## Further Reading

- *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the product, its class and its placement.
- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the relative definition of the root and of the square root.
- *Norm and Invertibility in the Symmetric Plain Sesqualgebra* (`articles_maths/norm-and-invertibility-in-the-symmetric-plain-sesqualgebra.md`), for the norm, its definiteness and the square map.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra.md`), for the three sets of the parent and the idempotent and nilpotent reading.
- *Square Roots of a General Element in the General Plain Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-general-plain-algebra.md`), for the general reduction the present one specialises.
- *Idempotents of the Symmetric Plain Sesqualgebra* (`articles_maths/idempotents-of-the-symmetric-plain-sesqualgebra.md`), for the idempotents the root sets here meet.
- *Nilpotents of the Symmetric Plain Sesqualgebra* (`articles_maths/nilpotents-of-the-symmetric-plain-sesqualgebra.md`), for the index-three nilpotents, which are not the roots of $0$.
- *Zero Divisors of the Symmetric Plain Sesqualgebra* (`articles_maths/zero-divisors-of-the-symmetric-plain-sesqualgebra.md`), for the punctured-space set that contains every root.
