# __Square Roots of a General Element in the Symmetric Plain Sesqualgebra__

## Introduction

The symmetric plain sesqualgebra is the operation $\tilde\Xi\star\tilde Q = H(\tilde\Xi,\tilde Q)e_0$ on the biquaternion space (*Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*). This article determines the **square roots** of a general element: the elements $\tilde\Xi$ with $\tilde\Xi\star\tilde\Xi = \tilde A$, for an arbitrary $\tilde A\in\mathbb{B}$.

The whole classification follows from one structural fact. The square of an element is always in the **centre**: $\tilde\Xi\star\tilde\Xi = H(\tilde\Xi)e_0$ with $H(\tilde\Xi) = \sum_\mu\lvert \Xi_\mu\rvert^{2}$ a real non-negative number (*Norm and Invertibility in the Symmetric Plain Sesqualgebra*). The equation $\tilde\Xi\star\tilde\Xi = \tilde A$ therefore has no solution unless $\tilde A$ is central, and when $\tilde A = \lambda e_0$ the equation is the scalar one $H(\tilde\Xi) = \lambda$, solvable exactly when $\lambda$ is a non-negative real. The **image of the square map** is the real ray $\mathbb{R}_{\geq0}e_0$, and the square roots of a point of that ray form the algebraic-norm quadric at the corresponding value. Non-central elements have no square root, the negative reals have none, and the non-real complex numbers have none.

**Placement.** The article is the fifth entry of the *Common Theory* section of the block, after the three central values and before the idempotents. It uses the product and the class of the introduction, the algebraic norm and the square map of *Norm and Invertibility in the Symmetric Plain Sesqualgebra*, and the three central values of *Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Sesqualgebra*.

**Boundaries.** The product, its class and its placement are *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*; the relative definition of the square root and the general reduction are *Definitions for the Study of the 12 Algebraic Structures* and *Square Roots of a General Element in the General Plain Algebra*. The three central values of the block are *Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Sesqualgebra*, and those of the parent are the article of the same title in the general plain algebra. Nothing topological and nothing metric appears.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with central scalar imaginary $i$. A general element is $\tilde{Q} = \sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; the natural conjugation is $\tilde{Q}^{\natural} = \sum_\mu\varepsilon_\mu Q_\mu e_\mu$ with $\varepsilon = (1,-1,-1,-1)$, the coefficientwise conjugation is $\overline{\tilde{Q}} = \sum_\mu\overline{Q_\mu}e_\mu$, and the Hermitian conjugation is $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$. The product of the block is

$$
\tilde\Xi\star\tilde Q = H(\tilde\Xi,\tilde Q)e_0, \qquad H(\tilde\Xi,\tilde Q) = \sum_{\mu=0}^{3}\Xi_\mu\overline{Q_\mu},
$$

and the algebraic norm is $H(\tilde{Q}) = H(\tilde{Q},\tilde{Q}) = \sum_\mu\lvert Q_\mu\rvert^{2}$. The **centre** of $\mathbb{B}$ is the line $\mathbb{C}e_0 = \mathbb{C}_{\mathbb{B}}$.

## The Reduction

**Definition (recalled).** A **square root** of $\tilde A\in\mathbb{B}$ in the block is an element $\tilde\Xi$ with $\tilde\Xi\star\tilde\Xi = \tilde A$. The definition is that of *Definitions for the Study of the 12 Algebraic Structures*, read on the product $\star$; a square root of a central element is also a **root** when it is required to be nonzero, the distinction being the one of the article on the three central values.

**Theorem (the square is central).** For every $\tilde\Xi\in\mathbb{B}$,

$$
\tilde\Xi\star\tilde\Xi = H(\tilde\Xi)e_0, \qquad H(\tilde\Xi) = \sum_{\mu=0}^{3}\lvert \Xi_\mu\rvert^{2} \in \mathbb{R}_{\geq0}.
$$

Consequently the square map $\tilde\Xi\mapsto\tilde\Xi\star\tilde\Xi$ has its image in the real ray $\mathbb{R}_{\geq0}e_0$, and the equation $\tilde\Xi\star\tilde\Xi = \tilde A$ has no solution unless $\tilde A$ lies in that ray.

*Proof.* The display is the square map of *Norm and Invertibility in the Symmetric Plain Sesqualgebra*: the product is the central value $H(\tilde\Xi,\tilde\Xi)e_0$ and $H(\tilde\Xi,\tilde\Xi) = \sum_\mu\lvert \Xi_\mu\rvert^{2}$ is real and non-negative. The image statement is immediate from the display; for the necessity, if $\tilde\Xi\star\tilde\Xi = \tilde A$ then $\tilde A = H(\tilde\Xi)e_0$, which is a central element with a real non-negative coefficient, so a non-central $\tilde A$ or a central $\tilde A$ with a non-real or negative coefficient is excluded.

**Remark (why the obstruction is total).** The square map is not surjective, and its failure is not a matter of one value: the image is a ray inside a complex line, so the square misses all of the vector subspace $\mathrm{Vect}(\mathbb{B})$, all of the imaginary central line $i\mathbb{R}e_0$, and the negative central ray. In the plain product the square map has a much larger image, and the description of that image is the classification of the parent, *Square Roots of a General Element in the General Plain Algebra*. The rank-one shape of the block is the reason for the difference, and it is the reason the block's classification is a single scalar equation.

## The Image of the Square Map

**Theorem (the image is the real ray).** The image of the square map of the block is exactly the set of the central elements with a real non-negative coefficient,

$$
\{\tilde\Xi\star\tilde\Xi : \tilde\Xi\in\mathbb{B}\} = \mathbb{R}_{\geq0}e_0 = \{\lambda e_0 : \lambda\in\mathbb{R}, \lambda\geq0\}.
$$

*Proof.* The inclusion is the reduction. For the converse, every positive value is attained, $H(\sqrt{\lambda}e_0) = \lambda$ for $\lambda\geq0$, and the value $0$ is attained at the origin.

**Corollary (the square map is a quadric onto a ray).** The square map is a positive definite quadratic map on the $8$-real-dimensional space $\mathbb{B}$ with a one-real-dimensional image; its fibres are the level sets $\{H = \lambda\}$ for $\lambda\geq0$, the fibre at $0$ being the single point $\{0\}$ and each fibre at a positive value being a quadric of real dimension seven.

## The Roots of a Central Value

**Theorem (the square roots of a central value).** Let $\lambda\in\mathbb{C}$ and let $\tilde A = \lambda e_0$. The square roots of $\tilde A$ in the block are the elements of algebraic norm $\lambda$,

$$
\{\tilde\Xi\in\mathbb{B} : H(\tilde\Xi) = \lambda\},
$$

and the set is as follows: empty for $\lambda\notin\mathbb{R}$ and for $\lambda<0$; the single point $\{0\}$ for $\lambda = 0$; and the real quadric of real dimension seven for $\lambda>0$. Passing to the roots of the article on the three central values, the nonzero elements of the last set are the roots of $\lambda$, and the point $0$ is a square root of $0$ but not a root of $0$.

*Proof.* The reduction turns the equation into $H(\tilde\Xi) = \lambda$, and the discussion of the three cases is the corollary of the reduction in *Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Sesqualgebra*. The dimension is that of a positive level set of a definite quadratic form on an eight-real-dimensional space.

**Corollary (the three central values).** At $\lambda = -1$, $0$ and $+1$ the theorem reproduces the three sets of the article on the central values: the empty set, the empty set of roots (the point $0$ being excluded), and the algebraic-norm-one quadric. The present article extends the trichotomy to every central value.

## The Classification

The square roots of a general element $\tilde A$ are collected in one table.

| the element $\tilde A$ | square roots of $\tilde A$ | size |
|---|---|---|
| non-central, $\tilde A\notin\mathbb{C}e_0$ | none | none |
| central with non-real coefficient, $\tilde A = \lambda e_0$, $\lambda\notin\mathbb{R}$ | none | none |
| central with negative coefficient, $\tilde A = \lambda e_0$, $\lambda<0$ | none | none |
| the origin, $\tilde A = 0$ | $\{0\}$ | one point |
| central with positive coefficient, $\tilde A = \lambda e_0$, $\lambda>0$ | $\{H = \lambda\}$ | real dimension seven |

Only one row carries a genuine family, and the family is the orbit of any one of its elements under the group of the linear maps that preserve $H$; the roots of the central values of the previous article are the nonzero entries of the last row.

**Corollary (the criterion for the existence of a square root).** An element $\tilde A$ has a square root in the block exactly when it is a central element with a real non-negative coefficient, that is exactly when $\tilde A$ lies in the ray $\mathbb{R}_{\geq0}e_0$.

## Worked Examples

**A central value.** The element $\tilde A = 3e_0$ has the square roots $\{\tilde\Xi : H(\tilde\Xi) = 3\}$, a real quadric of real dimension seven; the element $\tilde\Xi = \sqrt{3}e_0$ is one of them, and so is $\tilde\Xi = \sqrt{3}e_1$, since $H(\sqrt{3}e_1) = 3$.

**A non-central value.** The element $\tilde A = e_1$ has no square root, because the square of every element is central and $e_1$ is not. Likewise $\tilde A = ie_0$ has none, because the coefficient must be real.

**A negative value.** The element $\tilde A = -e_0$ has no square root, because a square is a non-negative multiple of $e_0$. This is the statement of the rootlessness of $-1$ read for the square map instead of the root set.

**The origin.** The element $\tilde A = 0$ has the single square root $0$; the block has no nonzero square-zero element, so the square map reaches the origin once. The element $e_0 + ie_1$ is not a square root of the origin, since $H(e_0 + ie_1) = 2$.

## The Relation to the Idempotents and to the Other Central Values

The **idempotents** of the block are $0$ and $e_0$ (*Idempotents of the Symmetric Plain Sesqualgebra*). They are square roots of themselves: $0$ is the square root of $0$ at the origin, and $e_0$ is the square root of $e_0$ at the value $\lambda = 1$. No other element of the algebraic-norm-one quadric is idempotent, so the idempotents are a two-point subset of the union of the fibres of the square map, and the fibre at $1$ is the quadric of the roots of $+1$.

The **three central values** $\lambda = -1, 0, +1$ are the entries of the article *Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Sesqualgebra*, and the present article is its extension to all values: the root sets there are the nonzero elements of the fibres here, and the fibre at the origin is the point $0$ that the root set of $0$ excludes.

The **parent** is *Square Roots of a General Element in the General Plain Algebra*: there the reduction is not a single scalar equation but a system, and the square map has a rich image. The block's reduction is the collapse of that system to the algebraic norm, and the collapse is the reason the block's classification is a single row of a quadric.

## Summary

The square of an element of the symmetric plain sesqualgebra is central, $\tilde\Xi\star\tilde\Xi = H(\tilde\Xi)e_0$ with $H(\tilde\Xi) = \sum_\mu\lvert \Xi_\mu\rvert^{2}\geq0$, so the equation of the square root $\tilde\Xi\star\tilde\Xi = \tilde A$ is solvable exactly when $\tilde A$ is a central element with a **real non-negative** coefficient, and then it reduces to the scalar equation $H(\tilde\Xi) = \lambda$. The **image of the square map** is the real ray $\mathbb{R}_{\geq0}e_0$. The square roots of $\tilde A = \lambda e_0$ are empty for $\lambda\notin\mathbb{R}$ and for $\lambda<0$, the single point $\{0\}$ for $\lambda = 0$, and the algebraic-norm quadric $\{H = \lambda\}$, a real quadric of real dimension seven, for $\lambda>0$. Non-central $\tilde A$ has no square root. The three central values of the previous article are the special cases $\lambda = -1$, $0$, $+1$; the idempotents $0$ and $e_0$ are the square roots of themselves; and the parent's classification, a system, collapses here to a single scalar equation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi\star\tilde Q = H(\tilde\Xi,\tilde Q)e_0$ | the product of the block |
| $H(\tilde{Q}) = H(\tilde{Q},\tilde{Q}) = \sum_\mu\lvert Q_\mu\rvert^{2}$ | the algebraic norm of the block, real and non-negative |
| $\tilde\Xi\star\tilde\Xi = H(\tilde\Xi)e_0$ | the square map, always central |
| $\mathbb{R}_{\geq0}e_0$ | the image of the square map, the non-negative central ray |
| $\{H = \lambda\}$ | the square roots of $\lambda e_0$, a quadric of real dimension seven for $\lambda>0$ |
| $\{0\}$ | the single square root of the origin |
| $\varnothing$ | the square roots of a non-central, a non-real central or a negative central element |
| $\mathbb{C}_{\mathbb{B}} = \mathbb{C}e_0$ | the centre of $\mathbb{B}$ |

## Further Reading

- *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the product, its class and its placement.
- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the relative definition of the square root and the root.
- *Norm and Invertibility in the Symmetric Plain Sesqualgebra* (`articles_maths/norm-and-invertibility-in-the-symmetric-plain-sesqualgebra.md`), for the algebraic norm and the square map.
- *Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Sesqualgebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-symmetric-plain-sesqualgebra.md`), for the three central values, which are the special cases of the present classification.
- *Square Roots of a General Element in the General Plain Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-general-plain-algebra.md`), for the classification of the parent, which is a system and not a scalar equation.
- *Idempotents of the Symmetric Plain Sesqualgebra* (`articles_maths/idempotents-of-the-symmetric-plain-sesqualgebra.md`), for the idempotents, which are square roots of themselves.
