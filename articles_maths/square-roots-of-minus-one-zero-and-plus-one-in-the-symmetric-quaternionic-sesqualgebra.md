# __Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Sesqualgebra__

## Introduction

This article computes the roots of the three central values $-1$, $0$ and $+1$ in the block, the symmetric
quaternionic sesquilinear product
$\tilde\Xi\star\tilde Q=\tfrac12(\tilde\Xi^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde\Xi^{\natural})$ of
*Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*. It follows
*Nilpotents of the Symmetric Quaternionic Sesqualgebra* and prepares
*Square Roots of a General Element in the Symmetric Quaternionic Sesqualgebra*, which reads the same
equation for an arbitrary value.

The root is relative to a product, and the product is part of the definition: it is stated once for a
general product in *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the
Roots*, and read on the products of the space. The unqualified word means the root in the block. The three
values are the central scalars $\lambda e_0$ with $\lambda\in\{-1,0,+1\}$, the values singled out by the
polynomial equations $\xi^2=1$ and $\xi^2=0$ of the biquaternion algebra; the root of $0$ is the nilpotent
of the block, computed in *Nilpotents of the Symmetric Quaternionic Sesqualgebra*, and is recalled here for
the sake of the comparison, while the roots of $-1$ and $+1$ are new.

The product is *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*; the diagonal is
*The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra*; the zero divisors
are *Zero Divisors of the Symmetric Quaternionic Sesqualgebra*; the idempotents are *Idempotents of the
Symmetric Quaternionic Sesqualgebra*; the roots of the three central values in the plain product are
*Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*; and the isotropic elements of
the Krein form are *The Isotropic Structure of the General Quaternionic Sesqualgebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$,
$e_k^2=-e_0$ and $e_1e_2=e_3$; $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$ and central
scalar imaginary $i$; $\mathbf Q=\sum_kQ_ke_k$; $(\mathbf\Xi,\mathbf Q)=\sum_k\Xi_kQ_k$; ${}^{\natural}$ negates
$e_1,e_2,e_3$ and fixes the coefficients, ${}^{*}={}^{\natural}\circ\bar{\cdot}$; and
$\mathbb{H}_{\mathbb{B}}$ is the real quaternion subspace. The diagonal is
$\tilde Q\star\tilde Q=K(\tilde Q,\tilde Q)e_0-Q_0\overline{\mathbf Q}-\overline{Q_0}\mathbf Q$ with
$K(\tilde Q,\tilde Q)=|Q_0|^2-\sum_k|Q_k|^2$. Throughout this article the product is the block.

## Definition

**Definition (root of an element in a product).** Let $\star$ be a product on $\mathbb{B}$ and let
$\tilde A\in\mathbb{B}$. A **square root of $\tilde A$ in $\star$** is an element $\tilde\Xi$ with

$$
\tilde\Xi\star\tilde\Xi=\tilde A .
$$

When $\tilde A=\lambda e_0$ is a central scalar with $\lambda\in\mathbb{C}$, the roots are the **roots of
$\lambda$ in $\star$**, and the equation reads $\tilde\Xi\star\tilde\Xi=\lambda e_0$.

This is *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots*.
Unqualified, the product is the block. The origin is a root of $0$ in every product and is excluded from
the families below.

## The Reduction to the Central Condition

**Proposition (the shape of the square).** For every $\tilde\Xi=\alpha e_0+\mathbf x$ the diagonal is

$$
\tilde\Xi\star\tilde\Xi=K(\tilde\Xi,\tilde\Xi)e_0-2\,\mathrm{Re}\bigl(\alpha\overline{\mathbf x}\bigr),
\qquad
K(\tilde\Xi,\tilde\Xi)=|\alpha|^2-\lVert\mathbf x\rVert^2 ,
$$

whose scalar part is real and whose vector part is a real vector; the diagonal is a real quaternion.

*Proof.* This is the diagonal theorem of *The Non-Central Diagonal and the Two Halves of the Symmetric
Quaternionic Sesqualgebra*.

**Corollary (the two conditions for a root of a central value).** $\tilde\Xi\star\tilde\Xi=\lambda e_0$ holds
for a real $\lambda$ exactly when

$$
\alpha\overline{\mathbf x}\in i\mathbb{R}^3
\qquad\text{and}\qquad
K(\tilde\Xi,\tilde\Xi)=\lambda ,
$$

and for a non-real complex $\lambda$ it holds never.

*Proof.* The right-hand side $\lambda e_0$ is central, so the vector part
$-2\mathrm{Re}(\alpha\overline{\mathbf x})$ of the left side must vanish, that is
$\alpha\overline{\mathbf x}\in i\mathbb{R}^3$; the scalar part $K(\tilde\Xi,\tilde\Xi)$ is real and must equal
$\lambda$, so $\lambda$ is real. Conversely the two conditions make the two sides agree.

## The Root of Zero

**Theorem (the roots of $0$).** The roots of $0$ in the block are the origin and the elements

$$
\alpha(e_0+i\boldsymbol\mu),
\qquad
\alpha\in\mathbb{C}^{\times},\quad
\boldsymbol\mu\in\mathbb{R}^3,\quad
\lVert\boldsymbol\mu\rVert=1 .
$$

*Proof.* This is the square-zero set of *Nilpotents of the Symmetric Quaternionic Sesqualgebra*: the
parameters $\mathbf c=|\alpha|^2\boldsymbol\mu$ of that theorem are exactly the real unit-vector directions
here.

The root set of $0$, without the origin, is the nilpotent cone of real dimension four. It contains no pure
element, in contrast with the plain product, whose roots of $0$ are the pure isotropic vectors.

## The Roots of Minus One

**Theorem (the roots of $-1$).** The roots of $-1$ in the block are the disjoint union of the **pure
family**

$$
\tilde\Xi=\mathbf\Xi\in\mathbb{C}^3,\qquad \lVert\mathbf\Xi\rVert^2=1 ,
$$

the pure vectors of unit modulus, and the **non-pure family** $\mathcal R_{-1}$ of the elements

$$
\tilde\Xi=\alpha e_0+\frac{i\alpha}{|\alpha|^2}\mathbf c ,
\qquad
\alpha\in\mathbb{C}^{\times},\quad
\mathbf c\in\mathbb{R}^3,\quad
\lVert\mathbf c\rVert^2=|\alpha|^2\bigl(|\alpha|^2+1\bigr) .
$$

*Proof.* Let $\tilde\Xi=\alpha e_0+\mathbf x$ and apply the corollary of §*The Reduction*.

If $\alpha=0$ the vector part vanishes automatically and $K=-\lVert\mathbf x\rVert^2=-1$, so
$\lVert\mathbf x\rVert^2=1$: the pure unit vectors.

If $\alpha\neq0$ the condition $\alpha\overline{\mathbf x}\in i\mathbb{R}^3$ writes
$\alpha\overline{x_k}=-ic_k$ with $c_k\in\mathbb{R}$, that is $x_k=i\alpha c_k/|\alpha|^2$, the vector
$\mathbf c=(c_1,c_2,c_3)$ real; then $\lVert\mathbf x\rVert^2=\lVert\mathbf c\rVert^2/|\alpha|^2$ and
$K=|\alpha|^2-\lVert\mathbf c\rVert^2/|\alpha|^2=-1$ reads $\lVert\mathbf c\rVert^2=|\alpha|^2(|\alpha|^2+1)$,
which is always solvable because $|\alpha|^2(|\alpha|^2+1)>0$. Conversely the display satisfies both
conditions. The two families are disjoint because the first has $\alpha=0$ and the second $\alpha\neq0$.

**Corollary (the shape).** The pure family is a real sphere of dimension five in the vector subspace and
the non-pure family is a real manifold of dimension four; the root set of $-1$ has real dimension five.

*Proof.* The pure vectors of unit modulus are the sphere $S^5$ of the real six-dimensional vector subspace;
the parameters of the non-pure family are the punctured plane of real dimension two and the sphere of
radius $|\alpha|\sqrt{|\alpha|^2+1}$ of real dimension two.

**Corollary (the named witnesses).** $e_1$, $e_2$ and $ie_1$ are roots of $-1$; the element $e_1+ie_2$ is
not, it is a root of $-2$.

*Proof.* $K(e_1,e_1)=K(e_2,e_2)=K(ie_1,ie_1)=-1$, each a pure vector of unit modulus. For $e_1+ie_2$,
$K=-2$ with vanishing vector part, so its square is $-2e_0$.

## The Roots of Plus One

**Theorem (the roots of $+1$).** The roots of $+1$ in the block are the elements

$$
\tilde\Xi=\alpha e_0+\frac{i\alpha}{|\alpha|^2}\mathbf c ,
\qquad
\alpha\in\mathbb{C}^{\times},\quad
|\alpha|\geq1,\quad
\mathbf c\in\mathbb{R}^3,\quad
\lVert\mathbf c\rVert^2=|\alpha|^2\bigl(|\alpha|^2-1\bigr) .
$$

There is no pure root of $+1$.

*Proof.* The reduction gives the same two conditions. If $\alpha=0$ then $K=-\lVert\mathbf x\rVert^2=1$ is
impossible. If $\alpha\neq0$ the central condition writes $\mathbf x=i\alpha\mathbf c/|\alpha|^2$ with
$\mathbf c$ real and $K=|\alpha|^2-\lVert\mathbf c\rVert^2/|\alpha|^2=1$ reads
$\lVert\mathbf c\rVert^2=|\alpha|^2(|\alpha|^2-1)$, solvable exactly when $|\alpha|^2\geq1$.

**Corollary (the unit candidate).** $\tilde\Xi=e_0$ is a root of $+1$: it is the case $\alpha=1$,
$\mathbf c=\mathbf 0$. It is the only element of the block that is at once an idempotent and a root of
$+1$.

*Proof.* $e_0\star e_0=e_0$ by the multiplication table, so the square of $e_0$ is $e_0$, that is $+1$
times $e_0$. If a nontrivial idempotent $-\tfrac12e_0+\boldsymbol\mu$ had square $e_0$ then the idempotent
equation would give $-\tfrac12e_0+\boldsymbol\mu=e_0$, false; the origin is not a root of $+1$; so $e_0$ is
the only common element.

## Comparison of the Three Sets

| value $\lambda$ | pure roots | non-pure roots | real dimension |
|---|---|---|---|
| $-1$ | unit vectors of $\mathbb{C}^3$ | $\mathcal R_{-1}$, any $\alpha\in\mathbb{C}^{\times}$ | $5$ |
| $0$ | none except the origin | the nilpotent cone $\alpha(e_0+i\boldsymbol\mu)$ | $4$ |
| $+1$ | none | $\mathcal R_{+1}$, $|\alpha|\geq1$ | $4$ |

The three sets are pairwise disjoint: the square is a function and its three values are distinct scalars. The
root of $0$ is the nilpotent cone of *Nilpotents of the Symmetric Quaternionic Sesqualgebra*; the roots of
$-1$ and of $+1$ are the two involutive values, and the unit candidate $e_0$ is the simplest root of $+1$.
The root of $-1$ is the only one of the three whose solutions enter the vector subspace, and there they are
exactly the pure vectors of unit modulus: the vector subspace contributes an involution, an element of
square $-\lVert\mathbf\Xi\rVert^2 e_0$, and no element of square $+1$.

Unlike the plain product, the block's root of $-1$ is not the parametrisation of its idempotents: there the
idempotent $\tfrac12(e_0+\xi i)$ and the root of $-1$ are built from the same $\xi$, while here the
idempotents are $-\tfrac12e_0+\boldsymbol\mu$ and lie on no one of the three root sets. The comparison of
the element theory is *Idempotents of the Symmetric Quaternionic Sesqualgebra*.

## Worked Examples

**A pure root of $-1$.** $\tilde\Xi=e_1$: $e_1\star e_1=-e_0$, and $\lVert e_1\rVert^2=1$.

**A non-pure root of $-1$.** $\tilde\Xi=e_0+i\sqrt2\,e_1$: here $\alpha=1$ and $\mathbf c=(\sqrt2,0,0)$ with
$\lVert\mathbf c\rVert^2=2=1\cdot(1+1)$, so $\tilde\Xi\star\tilde\Xi=-e_0$.

**A root of $+1$.** $\tilde\Xi=e_0$; and $\tilde\Xi=\sqrt2\,e_0+ie_1$ has $\alpha=\sqrt2$,
$|\alpha|^2=2$, $\mathbf x=i e_1=i\alpha\mathbf c/|\alpha|^2$ with $\mathbf c=(\sqrt2,0,0)$ of
$\lVert\mathbf c\rVert^2=2=|\alpha|^2(|\alpha|^2-1)$, so $\tilde\Xi\star\tilde\Xi=e_0$.

**A root of $0$.** $\tilde\Xi=e_0+ie_1$: the square vanishes, and it is the nilpotent of the previous
article.

**A root of $-2$ that is neither of the three.** $\tilde\Xi=e_1+ie_2$: $K=-2$ and the vector part vanishes,
so $\tilde\Xi\star\tilde\Xi=-2e_0$; this is not a root of $-1$, $0$ or $+1$.

## Summary

The roots of the three central values in the block are the solutions of $\tilde\Xi\star\tilde\Xi=\lambda e_0$
for $\lambda\in\{-1,0,+1\}$. The root of $0$ is the nilpotent cone $\alpha(e_0+i\boldsymbol\mu)$, of real
dimension four and with no pure element. The roots of $-1$ are the disjoint union of the pure unit vectors,
a real five-sphere, and the family $\mathcal R_{-1}$ of real dimension four; those of $+1$ are the family
$\mathcal R_{+1}$ with $|\alpha|\geq1$, of real dimension four, and contain $e_0$, the only common element of
the idempotents and the roots of $+1$. The vector subspace contributes a root of $-1$ for each of its unit
vectors and no root of $+1$, and the three root sets are pairwise disjoint; the idempotents
$-\tfrac12e_0+\boldsymbol\mu$ lie on none of them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi\star\tilde\Xi=\lambda e_0$ | the root equation of a central value |
| $\alpha\overline{\mathbf x}\in i\mathbb{R}^3,\ K(\tilde\Xi,\tilde\Xi)=\lambda$ | the two conditions, $\lambda$ real |
| $\alpha(e_0+i\boldsymbol\mu)$ | the roots of $0$, the nilpotent cone |
| $\{\mathbf\Xi:\lVert\mathbf\Xi\rVert^2=1\}$ | the pure roots of $-1$ |
| $\mathcal R_\lambda=\{\alpha e_0+\tfrac{i\alpha}{|\alpha|^2}\mathbf c:\lVert\mathbf c\rVert^2=|\alpha|^2(|\alpha|^2-\lambda)\}$ | the non-pure roots of $\lambda$ |
| $K(\tilde\Xi,\tilde\Xi)=|\Xi_0|^2-\lVert\mathbf\Xi\rVert^2$ | the scalar part of the diagonal, real |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*Powers, the Square and the Roots*, for the definitions of the square and the roots relative to a general product.
- *Nilpotents of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/nilpotents-of-the-symmetric-quaternionic-sesqualgebra.md`), for the root of $0$, its cone and its index-two property.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra.md`), for the same three values in the plain product, with the idempotent parametrisation.
- *Idempotents of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/idempotents-of-the-symmetric-quaternionic-sesqualgebra.md`), for the class that lies on none of the three root sets.
- *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-non-central-diagonal-and-the-two-halves-of-the-symmetric-quaternionic-sesqualgebra.md`), for the diagonal formula that carries the reduction.
- *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the product and its table.
