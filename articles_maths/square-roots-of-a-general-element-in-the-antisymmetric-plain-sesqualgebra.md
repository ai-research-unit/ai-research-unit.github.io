# __Square Roots of a General Element in the Antisymmetric Plain Sesqualgebra__

## Introduction

This article solves the square-root problem in the antisymmetric plain sesqualgebra: given $\tilde Q\in\mathbb{B}$, find every $\tilde\Xi\in\mathbb{B}$ with

$$
\tilde\Xi\diamond\tilde\Xi=\tilde Q,
$$

for the product $\tilde\Xi\diamond\tilde Q=\operatorname{Vect}(\tilde\Xi\tilde Q^{*})$ of *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions*.

The method is the scalar–vector split, carried by the real structure of the coefficients. The split writes each element as a real quaternion plus $i$ times a real quaternion, and the diagonal of the block then closes in a single expression in the eight real data of the root; the expression exhibits the diagonal as $2i$ times a **real** vector, and that is the whole classification. Every value of the diagonal is of that form, and the square-root equation is solvable exactly for the radicands of that form: the block has **no root of a radicand outside the Hermitian pure vectors**, and for a radicand inside them the roots form a real five-parameter family. The squaring map is thus a map whose image is a real three-dimensional space and each of whose fibres is a real five-dimensional family, and the discrepancy is the non-associativity and the non-injectivity of the projection.

The article is algebraic. No norm enters and no form is needed beyond the description of the image. The three central values $\tilde\Xi\diamond\tilde\Xi=-e_0,0,+e_0$ are the degenerate data of the classification and are *Square Roots of One and the Idempotents of the Antisymmetric Plain Sesqualgebra* and *Square Roots of Zero and the Nilpotents of the Antisymmetric Plain Sesqualgebra*; the criterion for the diagonal to vanish and the quadric it traces are *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*; the square-zero class is *Square Roots of Zero and the Nilpotents of the Antisymmetric Plain Sesqualgebra*. The general definition of the square root is *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots*; the model of the method is *Square Roots of a General Element in the General Plain Algebra*; and the two models of the block, which read the same classification through the matrix and the regular representation, are *The Antisymmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* and *The Antisymmetric Plain Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*.

Throughout, the square is the square of $\diamond$ and the root is the root in $\diamond$, unqualified. $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0=1,e_1,e_2,e_3$ with $e_1e_2=e_3$, central scalar imaginary $i$ and coefficients in $\mathbb{C}$; the projection $\operatorname{Vect}$ removes the scalar part, its kernel is the centre $\mathbb{C}_{\mathbb{B}}$, the Hermitian subspace is $\mathbb{M}_+$ and the vector subspace $\operatorname{Vect}(\mathbb{B})$. The conjugations are ${}^{\natural}$, the coefficientwise $\bar{\cdot}$ and the star ${}^{*}=\bar{\cdot}\circ{}^{\natural}$.

**The results.** In the real splitting $\tilde\Xi=\tilde\xi+i\tilde\xi'$ the diagonal is $2i$ times a real vector, $\tilde\Xi\diamond\tilde\Xi=2i(\xi_0\boldsymbol{\xi}'-\xi'_0\boldsymbol{\xi}-\boldsymbol{\xi}'\times\boldsymbol{\xi})$, so its image is the space $i\mathbb{R}^{3}=\mathbb{M}_+\cap\operatorname{Vect}(\mathbb{B})$ of the Hermitian pure vectors, of real dimension three. The block has **no root of a radicand outside $i\mathbb{R}^{3}$**, and for a nonzero Hermitian pure vector the roots form a **real five-parameter family** in bijection with $(\mathbb{R}^{4}\setminus\{0\})\times\mathbb{R}$, with $\tilde\Xi=e_0+\tfrac12\tilde Q$ a canonical member. For $\tilde Q=0$ the root set is the square-zero cone, of real dimension five, and the three central values recover the parity of the companion articles: no root of $\pm1$ and the cone for $0$.

## The Reduction

### The Real Form of an Element

Every coefficient $\Xi_\mu$ of a biquaternion is complex, and the element is written as a real quaternion plus $i$ times a real quaternion,

$$
\tilde\Xi=\tilde\xi+i\tilde\xi',\qquad
\tilde\xi=\xi_0e_0+\boldsymbol{\xi},\quad
\tilde\xi'=\xi'_0e_0+\boldsymbol{\xi}',\qquad
\xi_0,\xi'_0\in\mathbb{R},\quad \boldsymbol{\xi},\boldsymbol{\xi}'\in\mathbb{R}^{3},
$$

where $\mathbb{R}^{3}$ reads the three real coefficients of the vector part. The scalar part of $\tilde\Xi$ is the complex number $\Xi_0=\xi_0+i\xi'_0$ and the vector part is the complex vector $\mathbf\Xi=\boldsymbol{\xi}+i\boldsymbol{\xi}'$; the splitting is a real-linear isomorphism $\mathbb{B}\cong\mathbb{R}^{4}\oplus\mathbb{R}^{4}$ and it carries no choice beyond the central imaginary.

### The Diagonal in Coordinates

**Proposition (the diagonal).** For every $\tilde\Xi=\tilde\xi+i\tilde\xi'$,

$$
\tilde\Xi\diamond\tilde\Xi=2i\,\bigl(\xi_0\boldsymbol{\xi}'-\xi'_0\boldsymbol{\xi}-\boldsymbol{\xi}'\times\boldsymbol{\xi}\bigr),
$$

so the diagonal is $2i$ times a real vector.

*Proof.* Expand the parent product in the real form, $\tilde\Xi\tilde\Xi^{*}=\tilde\xi\tilde\xi^{\natural}+\tilde\xi'\tilde\xi'^{\natural}+i(\tilde\xi'\tilde\xi^{\natural}-\tilde\xi\tilde\xi'^{\natural})$. The first two terms are real scalars, so they contribute nothing to the vector part; the vector part of $\tilde\xi'\tilde\xi^{\natural}$ is $-\xi'_0\boldsymbol{\xi}+\xi_0\boldsymbol{\xi}'-\boldsymbol{\xi}'\times\boldsymbol{\xi}$, and the vector part of $\tilde\xi\tilde\xi'^{\natural}$ is $-\xi_0\boldsymbol{\xi}'+\xi'_0\boldsymbol{\xi}+\boldsymbol{\xi}'\times\boldsymbol{\xi}$, so their difference is $2(\xi_0\boldsymbol{\xi}'-\xi'_0\boldsymbol{\xi}-\boldsymbol{\xi}'\times\boldsymbol{\xi})$. Multiplying by $i$ and applying $\operatorname{Vect}$ gives the display.

The expression is the reason for everything that follows. It says three things at once: the diagonal is **real-vector-valued**, $2i$ times a vector of $\mathbb{R}^{3}$; it depends on the eight real data of the root through only three real components, so it cannot be injective; and it is the map of the real eight-dimensional space of roots onto the real three-dimensional target.

## The Existence

**The diagonal takes exactly the values $i\mathbb{R}^{3}=\mathbb{M}_+\cap\operatorname{Vect}(\mathbb{B})$, the Hermitian pure vectors, and every such value is attained:** the equation $\tilde\Xi\diamond\tilde\Xi=\tilde Q$ has no solution unless $\tilde Q$ is a pure vector with purely imaginary coefficients, and for every such $\tilde Q$ the canonical root $\tilde\Xi=e_0+\tfrac12\tilde Q$ solves it.

### The Necessary Condition

**Theorem (the image of the diagonal).** The diagonal of the block takes exactly the values

$$
\tilde\Xi\diamond\tilde\Xi\in i\mathbb{R}^{3}=\mathbb{M}_+\cap\operatorname{Vect}(\mathbb{B}),
$$

the **Hermitian pure vectors**, and every such value is attained. Equivalently, the equation $\tilde\Xi\diamond\tilde\Xi=\tilde Q$ has no solution unless $\tilde Q$ is a pure vector with purely imaginary coefficients,

$$
Q_0=0,\qquad \overline{Q_k}=-Q_k\quad(k=1,2,3),
$$

and for every such $\tilde Q$ it has a solution.

*Proof.* The diagonal is $2i\mathbf h$ with $\mathbf h\in\mathbb{R}^{3}$, so it is a pure vector with purely imaginary coefficients; conversely a pure vector with purely imaginary coefficients is $i\mathbf g$ with $\mathbf g\in\mathbb{R}^{3}$, and $\tilde\Xi=e_0+\tfrac12\tilde Q$ has $\xi_0=1$, $\xi'_0=0$, $\boldsymbol{\xi}=0$, $\boldsymbol{\xi}'=\tfrac12\mathbf g$, so its diagonal is $i\mathbf g=\tilde Q$; the identification with $\mathbb{M}_+\cap\operatorname{Vect}(\mathbb{B})$ is the statement that a pure vector is Hermitian exactly when its coefficients are purely imaginary.

**Corollary (the rootless radicands).** The elements outside $i\mathbb{R}^{3}$ have no square root in the block. The real vector $e_1$, whose coefficient is real and not purely imaginary, is rootless:

$$
\nexists\,\tilde\Xi\ \text{with}\ \tilde\Xi\diamond\tilde\Xi=e_1 ,
$$

although $e_1$ is itself square-zero, $e_1\diamond e_1=0$.

### A Canonical Root

The proof of the theorem delivers a root and it is worth naming, because it is a section of the diagonal map.

**Corollary (the canonical root).** For every Hermitian pure vector $\tilde Q$ the element

$$
\tilde\Xi=e_0+\tfrac12\tilde Q
$$

is a square root of $\tilde Q$.

*Proof.* Write $\tilde Q=2i\mathbf g$ with $\mathbf g\in\mathbb{R}^{3}$; then $\tfrac12\tilde Q=i\mathbf g$ and $\tilde\Xi=e_0+i\mathbf g$ has $\xi_0=1$, $\xi'_0=0$, $\boldsymbol{\xi}=0$, $\boldsymbol{\xi}'=\mathbf g$, so its diagonal is $2i(1\cdot\mathbf g-0-0)=2i\mathbf g=\tilde Q$.

The map $\tilde Q\mapsto e_0+\tfrac12\tilde Q$ is a real-linear section of the diagonal: it is injective, and its image, the roots with $\xi_0=1$, $\xi'_0=\boldsymbol{\xi}=0$ and $\boldsymbol{\xi}'\in\mathbb{R}^{3}$, is a real three-dimensional part of the root set. It is the analogue, for the block, of the two isolated roots $\pm\sqrt{Q_0}e_0$ of a complex scalar in the plain algebra, and it plays the same role: it names one root where the generic case has a family.

## The Root Set

**For a nonzero Hermitian pure vector $\tilde Q=2i\mathbf g$ the root set is in bijection with $(\mathbb{R}^{4}\setminus\{0\})\times\mathbb{R}$, a real five-parameter family**, the parameter $\boldsymbol{\xi}'$ being the unique solution of $\xi_0\boldsymbol{\xi}'-\xi'_0\boldsymbol{\xi}-\boldsymbol{\xi}'\times\boldsymbol{\xi}=\mathbf g$; for $\tilde Q=0$ the root set is the square-zero cone of real dimension five.

### The Equation in Real Coordinates

Let $\tilde Q$ be a Hermitian pure vector and write $\tilde Q=2i\mathbf g$ with $\mathbf g\in\mathbb{R}^{3}$. The equation $\tilde\Xi\diamond\tilde\Xi=\tilde Q$ reads, in the real coordinates of the root,

$$
\xi_0\boldsymbol{\xi}'-\xi'_0\boldsymbol{\xi}-\boldsymbol{\xi}'\times\boldsymbol{\xi}=\mathbf g .
$$

**Proposition (the equation is solved for the imaginary vector part).** Fix $\xi'_0\in\mathbb{R}$ and let $(\xi_0,\boldsymbol{\xi})\neq(0,0)$. Then the equation has exactly one solution $\boldsymbol{\xi}'$, the linear map $\boldsymbol{\xi}'\mapsto \xi_0\boldsymbol{\xi}'-\boldsymbol{\xi}'\times\boldsymbol{\xi}$ being invertible with eigenvalues $\xi_0$ and $\xi_0\pm i|\boldsymbol{\xi}|$, all nonzero.

*Proof.* Rewrite the equation as $\xi_0\boldsymbol{\xi}'+\boldsymbol{\xi}\times\boldsymbol{\xi}'=\mathbf g+\xi'_0\boldsymbol{\xi}$, that is $(\xi_0I+[\boldsymbol{\xi}]_\times)\boldsymbol{\xi}'=\mathbf h$ with $\mathbf h=\mathbf g+\xi'_0\boldsymbol{\xi}$ and $[\boldsymbol{\xi}]_\times$ the cross-product operator. The operator $[\boldsymbol{\xi}]_\times$ satisfies $[\boldsymbol{\xi}]_\times^{3}=-|\boldsymbol{\xi}|^{2}[\boldsymbol{\xi}]_\times$, and $\xi_0I+[\boldsymbol{\xi}]_\times$ has the eigenvalues $\xi_0$ and $\xi_0\pm i|\boldsymbol{\xi}|$, nonzero exactly when $(\xi_0,\boldsymbol{\xi})\neq(0,0)$; it is therefore invertible, and the solution is unique.

**Theorem (the root set).** Let $\tilde Q$ be a Hermitian pure vector.

- If $\tilde Q\neq0$, the root set of $\tilde Q$ is in bijection with $(\mathbb{R}^{4}\setminus\{0\})\times\mathbb{R}$: the parameters are $(\xi_0,\boldsymbol{\xi})\neq0$ and $\xi'_0$, and $\boldsymbol{\xi}'$ is determined by the proposition. The roots form a **real five-parameter family**.
- If $\tilde Q=0$, the root set is the square-zero cone, the criterion $\tilde\Xi\tilde\Xi^{*}$ central with $\tilde\Xi$ nonzero, of real dimension five (*Square Roots of Zero and the Nilpotents of the Antisymmetric Plain Sesqualgebra*).

*Proof.* The equation is the proposition, and a root with $(\xi_0,\boldsymbol{\xi})=(0,0)$ satisfies it only when $\mathbf g=0$; hence for $\tilde Q\neq0$ every root has $(\xi_0,\boldsymbol{\xi})\neq0$ and the parametrisation is a bijection, of real dimension $4+1=5$. For $\tilde Q=0$ the equation is $\tilde\Xi\diamond\tilde\Xi=0$, which is the square-zero condition, and its set is the cone of *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra*.

The dimension is the count of the free parameters: the root has eight real components, the four real components of $\tilde\xi$ and the four of $\tilde\xi'$, and the diagonal imposes the three real equations $\mathbf h=\mathbf g$ on them, so the root set has real dimension $8-3=5$.

### The Classification

Collecting the two steps, every radicand falls into exactly one row.

| condition on $\tilde Q$ | number of roots |
|---|---|
| $\tilde Q\notin i\mathbb{R}^{3}$ | none |
| $\tilde Q\in i\mathbb{R}^{3}$, $\tilde Q\neq0$ | a real five-parameter family |
| $\tilde Q=0$ | the square-zero cone, a real five-dimensional cone |

The generic radicand with a root is a nonzero Hermitian pure vector, and its root set is a five-parameter family of which the canonical root $e_0+\tfrac12\tilde Q$ is one member. The radicands without a root are the elements with a nonzero scalar part or a non-imaginary vector coefficient, and they are the majority of the space.

## The Central Values

**The classification specialises to the three central values: the block has the roots of $0$ and no root of $-1$ or $+1$**, since a central value $\lambda e_0$ is a Hermitian pure vector exactly when $\lambda=0$.

The classification specialises to the three central values of *Square Roots of One and the Idempotents of the Antisymmetric Plain Sesqualgebra* and *Square Roots of Zero and the Nilpotents of the Antisymmetric Plain Sesqualgebra*, and the agreement is the check that the two methods are the same.

A central value $\lambda e_0$ is a Hermitian pure vector exactly when $\lambda=0$, since $i\mathbb{R}^{3}$ has vanishing scalar part. Hence the row of the classification is the third for $\lambda=0$ and the first for $\lambda=\pm1$: **the block has the roots of $0$ and no root of $-1$ or $+1$**. This is the parity obstruction of the companion articles, recovered here as the statement that $\pm e_0\notin i\mathbb{R}^{3}$, and it is a special case of the necessary condition and not a new computation.

## Worked Examples

The examples are computed with the classification and verified by squaring.

**A nonzero Hermitian pure vector.** For $\tilde Q=2ie_3$ the parameter is $\mathbf g=e_3$, and the canonical root is $\tilde\Xi=e_0+ie_3$. A second root is obtained from the parameters $\xi_0=1$, $\boldsymbol{\xi}=e_1$, $\xi'_0=1$: the proposition solves $\boldsymbol{\xi}'+(\mathbf e_1\times\boldsymbol{\xi}')=e_3+e_1$, that is $\boldsymbol{\xi}'=e_1+\tfrac12e_2+\tfrac12e_3$, and the element $\tilde\Xi=e_0+e_1+i(e_0+e_1+\tfrac12e_2+\tfrac12e_3)$ has the same diagonal $2ie_3$, which is checked by $\xi_0\boldsymbol{\xi}'-\xi'_0\boldsymbol{\xi}-\boldsymbol{\xi}'\times\boldsymbol{\xi}=\boldsymbol{\xi}'-e_1-\boldsymbol{\xi}'\times e_1=e_3$.

**A rootless element.** For $\tilde Q=e_2$ the vector coefficient is real and not purely imaginary, so $\tilde Q\notin i\mathbb{R}^{3}$ and there is no root, though $e_2$ is square-zero.

**A square-zero radicand.** For $\tilde Q=0$ the root set is the cone; the member $\tilde\Xi=e_1+ie_1$, a complex multiple of the unit real quaternion $e_1$, is a root, since $\xi_0\boldsymbol{\xi}'-\xi'_0\boldsymbol{\xi}-\boldsymbol{\xi}'\times\boldsymbol{\xi}=0-e_1\times e_1=0$; the element $e_1+ie_2$, by contrast, has the diagonal $2ie_3\neq0$ and is not a root of $0$.

## Summary

The square-root problem of the block is solved by the real splitting $\tilde\Xi=\tilde\xi+i\tilde\xi'$ of the element into two real quaternions. The diagonal is

$$
\tilde\Xi\diamond\tilde\Xi=2i\,\bigl(\xi_0\boldsymbol{\xi}'-\xi'_0\boldsymbol{\xi}-\boldsymbol{\xi}'\times\boldsymbol{\xi}\bigr),
$$

$2i$ times a real vector, so the image of the diagonal is the space $i\mathbb{R}^{3}=\mathbb{M}_+\cap\operatorname{Vect}(\mathbb{B})$ of the Hermitian pure vectors, of real dimension three, and no radicand outside it has a root.

For a nonzero Hermitian pure vector $\tilde Q=2i\mathbf g$ the root set is in bijection with $(\mathbb{R}^{4}\setminus\{0\})\times\mathbb{R}$, the parameter $\boldsymbol{\xi}'$ being the unique solution of $(\xi_0I+[\boldsymbol{\xi}]_\times)\boldsymbol{\xi}'=\mathbf g+\xi'_0\boldsymbol{\xi}$; the roots form a real five-parameter family, and $\tilde\Xi=e_0+\tfrac12\tilde Q$ is a canonical member. For $\tilde Q=0$ the root set is the square-zero cone, of real dimension five.

The three central values are the degenerate data: $\pm e_0$ are outside $i\mathbb{R}^{3}$ and are rootless, and $0$ is the cone. The classification, the two models and the rank of a value are the articles named; this article is the Common Theory account of the same classification.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=\tilde\xi+i\tilde\xi'$ | the real splitting of the root into two real quaternions |
| $\xi_0,\xi'_0\in\mathbb{R}$, $\boldsymbol{\xi},\boldsymbol{\xi}'\in\mathbb{R}^{3}$ | the real data of the root, eight real components |
| $\tilde\Xi\diamond\tilde\Xi=2i(\xi_0\boldsymbol{\xi}'-\xi'_0\boldsymbol{\xi}-\boldsymbol{\xi}'\times\boldsymbol{\xi})$ | the diagonal in real coordinates |
| $i\mathbb{R}^{3}=\mathbb{M}_+\cap\operatorname{Vect}(\mathbb{B})$ | the image of the diagonal, the Hermitian pure vectors |
| $\tilde Q=2i\mathbf g$, $\mathbf g\in\mathbb{R}^{3}$ | a radicand with a root |
| $\tilde\Xi=e_0+\tfrac12\tilde Q$ | the canonical root of a Hermitian pure vector |
| $(\xi_0I+[\boldsymbol{\xi}]_\times)\boldsymbol{\xi}'=\mathbf g+\xi'_0\boldsymbol{\xi}$ | the linear equation that determines the root |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*Powers, the Square and the Roots*, for the square root and the root of a central value.
- *Square Roots of a General Element in the General Plain Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-general-plain-algebra.md`), for the model of the scalar–vector reduction.
- *Square Roots of One and the Idempotents of the Antisymmetric Plain Sesqualgebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-antisymmetric-plain-sesqualgebra.md`), for the roots of $+1$ and the idempotents.
- *Square Roots of Zero and the Nilpotents of the Antisymmetric Plain Sesqualgebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-antisymmetric-plain-sesqualgebra.md`), for the roots of $0$ and the nilpotents.
- *The Vector Part of the Square and the Jacobi Failure of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-vector-part-of-the-square-and-the-jacobi-failure-of-the-antisymmetric-plain-sesqualgebra.md`), for the criterion for the diagonal to vanish.
- *The Antisymmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-antisymmetric-plain-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the rank of a value.
