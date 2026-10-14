# __Square Roots of a General Element in the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra of $\mathbb{H}$ carries the Jordan product $\tilde p\bullet\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$ of *Introduction to the Symmetric Plain Algebra of Quaternions*, and its square is the plain square. This article solves the equation

$$
\tilde p\bullet\tilde p=\tilde q
$$

for an arbitrary element $\tilde q$, by the scalar and vector split alone — free of Clifford algebras, norms and forms — states the classification of the root set, works the examples, and specialises to the central values. The equation names a product, so the root is relative to it: throughout this article the square is the one of the symmetric plain product, which is the plain square, and the general definitions of the power, the square and the root of a central value are *Definitions for the Study of the 6 Algebraic Structures*, §*The Element Vocabulary*.

**This is not the algebra $\mathbb{H}$.** The two algebras share the space, the addition, the real scalars and the unit, but $\bullet$ is a different multiplication and the projection onto the scalar line is not multiplicative. Throughout, the natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because $\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural sign and gives nothing new.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and $e_1^2=e_2^2=e_3^2=-e_0$. An element is $\tilde q=q_0e_0+\vec q$ with $\vec q=\sum_{k=1}^{3}q_ke_k$ and $q_\mu\in\mathbb{R}$; $|\vec q|^2=\vec q\cdot\vec q$ and $N(\tilde q)=q_0^2+|\vec q|^2$. The square of the block is the plain square, and the central root sets are *Square Roots of One and the Idempotents of the Symmetric Plain Algebra* and *Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra*.

## The Reduction

Since the square of the block is the plain square, the equation is $\tilde p^2=\tilde q$, and it separates.

**Proposition.** For $\tilde p=p_0e_0+\vec p$ and $\tilde q=q_0e_0+\vec q$,

$$
\tilde p^2=\tilde q\iff
\begin{cases}
p_0^2-|\vec p|^2=q_0,\\[2pt]
2p_0\vec p=\vec q .
\end{cases}
$$

*Proof.* The plain square is $\tilde p^2=(p_0^2-|\vec p|^2)e_0+2p_0\vec p$, and the scalar and vector parts must match those of $\tilde q$.

The two cases are cut by the vanishing of the vector part of the radicand.

## The Two Cases

### The Central Case $\vec q=0$

**Theorem.** Let $\tilde q=q_0e_0$.

- If $q_0>0$ the roots are the two scalars $\tilde p=\pm\sqrt{q_0}\,e_0$.
- If $q_0=0$ the only root is $\tilde p=0$.
- If $q_0<0$ the roots are the pure elements of norm $-q_0$,

$$
\tilde p\in\mathrm{Vect}(\mathbb{H}),\qquad |\vec p|^2=-q_0,
$$

the quadric of radius $\sqrt{-q_0}$ in the vector subspace, of real dimension two.

*Proof.* The vector equation $2p_0\vec p=0$ gives $p_0=0$ or $\vec p=0$. If $\vec p=0$ the scalar equation is $p_0^2=q_0$, which has the two roots $\pm\sqrt{q_0}$ when $q_0>0$, the one root $0$ when $q_0=0$, and no root when $q_0<0$. If $p_0=0$ the scalar equation is $-|\vec p|^2=q_0$, which has no solution when $q_0>0$, the one solution $\vec p=0$ when $q_0=0$, and the quadric $|\vec p|^2=-q_0$ when $q_0<0$.

### The Non-Central Case $\vec q\neq0$

**Theorem.** Let $\vec q\neq0$, and set

$$
x=\frac{q_0+\sqrt{q_0^2+|\vec q|^2}}{2}>0,\qquad p_0=\pm\sqrt{x},\qquad \vec p=\frac{\vec q}{2p_0}.
$$

Then the roots are exactly the two elements

$$
\tilde p_{\pm}=\pm\sqrt{x}\,e_0+\frac{\vec q}{\pm2\sqrt{x}},
$$

and there are no others.

*Proof.* Since $\vec q\neq0$, the vector equation forces $p_0\neq0$ and $\vec p=\vec q/(2p_0)$. Substituting into the scalar equation gives $p_0^2-\frac{|\vec q|^2}{4p_0^2}=q_0$; with $x=p_0^2>0$ this is the quadratic $4x^2-4q_0x-|\vec q|^2=0$, whose roots are $\frac{q_0\pm\sqrt{q_0^2+|\vec q|^2}}{2}$. The discriminant $q_0^2+|\vec q|^2=N(\tilde q)$ is positive because $\tilde q\neq0$, so the two roots are real; the smaller one is negative because $\sqrt{q_0^2+|\vec q|^2}>|q_0|\geq q_0$ when $\vec q\neq0$, so only $x=\frac{q_0+\sqrt{q_0^2+|\vec q|^2}}{2}$ is admissible, and it is positive. Each sign of $p_0=\pm\sqrt{x}$ gives one root, so there are exactly two, and each satisfies the equations by construction.

## The Classification

**Theorem (classification).** Every element $\tilde q$ of the block has a square root, and the root set is one of the following.

| $\tilde q$ | root set | count |
|---|---|---|
| $\tilde q$ non-central, or $\tilde q=q_0e_0$ with $q_0>0$ | two elements | two roots |
| $\tilde q=0$ | $\{0\}$ | one root |
| $\tilde q=q_0e_0$ with $q_0<0$ | the quadric $\{\tilde p\in\mathrm{Vect}(\mathbb{H}) : \lvert\vec p\rvert^2=-q_0\}$ | a quadric of roots |

*Proof.* This is the union of the two cases above. The discriminant $4N(\tilde q)$ of the reduced quadratic is never negative, since the norm is positive definite, so the equation always has a root.

**Remark (the "no root" class is empty here).** The outline of the block lists a class of "no root". **That class does not occur in this block**: the discriminant of the reduced quadratic is $16\,N(\tilde q)$, the norm is positive definite, and every element of $\mathbb{H}$ therefore has a square root. In the central negative case the root set is the quadric $\lvert\vec p\rvert^2=-q_0$ of real dimension two, and in the central non-negative and non-central cases it is a two-element set.

## Worked Examples

The roots below are checked by squaring.

**Example ($\tilde q=e_1$).** Here $q_0=0$, $\vec q=e_1$, $|\vec q|^2=1$, $N=1$, so $x=\tfrac12$ and $p_0=\pm\tfrac{1}{\sqrt2}$, $\vec p=\pm\tfrac{1}{\sqrt2}e_1$. The roots are

$$
\tilde p_{\pm}=\pm\tfrac{1}{\sqrt2}\bigl(e_0+e_1\bigr),\qquad
\tilde p_{\pm}^2=\tfrac12\bigl(e_0+2e_1+e_1^2\bigr)=\tfrac12(2e_1)=e_1 .
$$

**Example ($\tilde q=e_0+e_1$).** Here $q_0=1$, $|\vec q|^2=1$, $N=2$, so $x=\tfrac{1+\sqrt2}{2}$ and the two roots are $\tilde p_{\pm}=\pm\sqrt{x}\,e_0\pm\frac{1}{2\sqrt{x}}e_1$; squaring either returns $e_0+e_1$ by the theorem.

**Example ($\tilde q=-e_0$).** The central negative case with $q_0=-1$: the roots are the pure elements of norm one, the quadric $\lvert\vec p\rvert^2=1$ of the vector subspace, of real dimension two.

**Example ($\tilde q=e_0$).** The central positive case with $q_0=1$: the two roots $\pm e_0$.

**Example ($\tilde q=0$).** The origin: the one root $0$.

## The Specialisation to the Central Values

The central values give back the root sets of the companion articles, as the consistency check of the method.

**At the three central values the classification reproduces the sets of the companion articles: the roots of $-e_0$ are the pure elements of norm one, the roots of $0$ are the origin alone, and the roots of $+e_0$ are the two central scalars $\pm e_0$.**

| $\tilde q$ | the general method | the companion root set |
|---|---|---|
| $-e_0$ | central negative, the quadric $\lvert\vec p\rvert^2=1$ | $\Sigma_{-}$, the pure quadric of the vector subspace |
| $0$ | the case $q_0=0$, the one root $0$ | $\Sigma_{0}=\{0\}$ |
| $+e_0$ | central positive, the two roots $\pm e_0$ | $\Sigma_{+}=\{\pm e_0\}$ |

The sets $\Sigma_{-}$ and $\Sigma_{+}$ are classified in *Square Roots of One and the Idempotents of the Symmetric Plain Algebra*, the set $\Sigma_{0}$ in *Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra*, and the agreement is the check that the computations are the same computation.

## Summary

The square of the block is the plain square, and the equation $\tilde p\bullet\tilde p=\tilde q$ reduces to the pair $p_0^2-|\vec p|^2=q_0$, $2p_0\vec p=\vec q$. When the radicand is central there are three behaviours: two scalar roots $\pm\sqrt{q_0}e_0$ for $q_0>0$, the one root $0$ at the origin, and the quadric $|\vec p|^2=-q_0$ of pure roots for $q_0<0$. When the radicand is non-central the roots are exactly two, $\tilde p_{\pm}=\pm\sqrt{x}e_0+\vec q/(\pm2\sqrt{x})$ with $x=\tfrac12(q_0+\sqrt{q_0^2+|\vec q|^2})$, because the reduced quadratic has one admissible positive root and each sign of $p_0$ gives a root. Every element of the block therefore has a square root, the root set is a two-element set outside the origin and the negative scalar axis, and the "no root" class of the outline is empty over $\mathbb{R}$ where the norm is definite.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\bullet\tilde p=\tilde p^2$ | the square of the block is the plain square |
| $p_0^2-\lvert\vec p\rvert^2=q_0$, $2p_0\vec p=\vec q$ | the reduced pair of equations |
| $x=\tfrac12\bigl(q_0+\sqrt{q_0^2+\lvert\vec q\rvert^2}\bigr)$ | the admissible positive root of the reduced quadratic |
| $\tilde p_{\pm}=\pm\sqrt{x}e_0+\vec q/(\pm2\sqrt{x})$ | the two non-central roots |
| $\{\tilde p\in\mathrm{Vect}(\mathbb{H}) : \lvert\vec p\rvert^2=-q_0\}$ | the quadric of roots of a central negative element |

## Further Reading

- *Introduction to the Symmetric Plain Algebra of Quaternions*, for the product and the square.
- *Square Roots of One and the Idempotents of the Symmetric Plain Algebra*, for the roots of $+e_0$, the roots of $-e_0$ and the idempotents.
- *Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra*, for the roots of $0$ and the empty nilpotent class.
- *Square Roots of a General Element in the General Plain Algebra*, for the same equation on the plain product.
- *Norm and Invertibility in the Symmetric Plain Algebra*, for the norm that makes the discriminant positive.
