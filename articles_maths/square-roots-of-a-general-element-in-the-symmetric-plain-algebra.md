# __Square Roots of a General Element in the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra $\mathbb{B}^{\bullet}$ is the complex space $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ under the Jordan product $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ of *Introduction to the Symmetric Plain Algebra of Biquaternions*. This article determines, for an element $\tilde Q$, the elements $\tilde P$ with $\tilde P\bullet\tilde P=\tilde Q$.

The equation names a product, and throughout this article the square is the one of the symmetric plain product. Because the square of the block is the **plain square**, the equation $\tilde P\bullet\tilde P=\tilde Q$ is the equation $\tilde P^2=\tilde Q$ of the algebra, and the whole classification of *Square Roots of a General Element in the General Plain Algebra* transfers verbatim. What this article adds is the block's notation: the **conjugate scalar** that decides the reduced quadratic is the block's **generic norm** $n=N(\tilde Q)$, so the degeneracy of the root problem is the vanishing of the norm, that is the isotropy of $\tilde Q$; the block's zero divisors and invertible elements then read the classification.

A root is defined relative to a product, and the definition is stated once for a general product in *Definitions for the Study of the 12 Algebraic Structures*, §*The Root*; throughout this article the product is $\bullet$ and, unqualified, **root** means root of $\bullet$. The general root problem of the algebra is *Square Roots of a General Element in the General Plain Algebra*; the three central values are *Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Algebra*; the generic norm is *Norm and Invertibility in the Symmetric Plain Algebra*; and the degenerate radicands are *Zero Divisors of the Symmetric Plain Algebra*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$, central scalar imaginary $i$ and coefficients in $\mathbb{C}$. An element is $\tilde P=P_0e_0+\mathbf{P}$ with $\mathbf{P}=\sum_kP_ke_k$, and $(\mathbf{P},\mathbf{P})=\sum_kP_k^2$. The product with the mark is $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$; the generic norm is $N(\tilde Q)=Q_0^2+(\mathbf{Q},\mathbf{Q})$.

## The Definition and the Reduction

**Definition (root of an element).** Let $\star$ be a product on $\mathbb{B}$; then $\tilde P$ is a **square root of $\tilde Q$ of $\star$** when $\tilde P\star\tilde P=\tilde Q$, and the **root set** of $\tilde Q$ of $\star$ is the set of all such $\tilde P$.

Throughout this article the product is $\bullet$, the equation is

$$
\tilde P\bullet\tilde P=\tilde Q,
$$

and, the two squares being equal, it is the plain equation $\tilde P^2=\tilde Q$; the root set of the block is the root set of the algebra, element by element.

**Theorem (the reduction).** With $\tilde P=P_0e_0+\mathbf{P}$ and $\tilde Q=Q_0e_0+\mathbf{Q}$, the equation $\tilde P\bullet\tilde P=\tilde Q$ is equivalent to the pair

$$
2P_0\mathbf{P}=\mathbf{Q},\qquad P_0^2-(\mathbf{P},\mathbf{P})=Q_0 .
$$

*Proof.* The square of the block is the plain square, $\tilde P\bullet\tilde P=\bigl[P_0^2-(\mathbf{P},\mathbf{P})\bigr]e_0+2P_0\mathbf{P}$, and the equality with $\tilde Q$ is the equality of the scalar and the vector parts.

The vector equation decides the shape of the answer, and it has the two outcomes of the algebra: either $\mathbf{Q}\neq0$, and then $P_0\neq0$ and $\mathbf{P}=\mathbf{Q}/(2P_0)$, so a root is fixed by its scalar part; or $\mathbf{Q}=0$, and then a root is either a complex scalar or pure.

**Definition (the data).** The two data are the complex square of the vector part and the generic norm,

$$
(\mathbf{Q},\mathbf{Q})=Q_1^2+Q_2^2+Q_3^2,\qquad n=N(\tilde Q)=Q_0^2+(\mathbf{Q},\mathbf{Q})=\tilde Q\tilde Q^{\natural},
$$

and $n$ is the **generic norm** of the block, not a length: it is an element of $\mathbb{C}$, and it is the conjugate scalar of the algebra article. Its vanishing is the condition of isotropy of $\tilde Q$.

## The Roots with Non-Vanishing Vector Part

**Proposition.** Let $\mathbf{Q}\neq0$. Then a root has $P_0\neq0$ and $\mathbf{P}=\mathbf{Q}/(2P_0)$, and the scalar part $P_0$ satisfies the reduced quadratic

$$
4P_0^4-4Q_0P_0^2-(\mathbf{Q},\mathbf{Q})=0,
\qquad\text{that is}\qquad 4x^2-4Q_0x-(\mathbf{Q},\mathbf{Q})=0\ \text{ in }x=P_0^2 .
$$

*Proof.* Substitute $\mathbf{P}=\mathbf{Q}/(2P_0)$ into the scalar equation: $P_0^2-\frac{(\mathbf{Q},\mathbf{Q})}{4P_0^2}=Q_0$, and multiply by $4P_0^2$.

**Proposition (the discriminant).** The discriminant of the reduced quadratic $4x^2-4Q_0x-(\mathbf{Q},\mathbf{Q})=0$ is $16N(\tilde Q)$, and it vanishes exactly when $\tilde Q$ is isotropic.

*Proof.* The equation $4x^2-4Q_0x-(\mathbf{Q},\mathbf{Q})=0$ has discriminant $16Q_0^2+16(\mathbf{Q},\mathbf{Q})=16n$.

So the root problem of the block degenerates exactly on the isotropic cone of the generic norm, which is the locus of the non-invertible elements of *Norm and Invertibility in the Symmetric Plain Algebra*.

## The Roots of a Complex Scalar

**Proposition.** Let $\tilde Q=Q_0e_0$ be a complex scalar. Then a root is either a complex scalar or pure: the scalars give the two elements $\pm\sqrt{Q_0}e_0$, and the pure roots are the four-real-parameter family of pure $\mathbf{P}$ with

$$
(\mathbf{P},\mathbf{P})=-Q_0 .
$$

*Proof.* With $\mathbf{Q}=0$ the vector equation is $2P_0\mathbf{P}=0$, so $\mathbf{P}=0$ or $P_0=0$; the first case gives $P_0^2=Q_0$, the second $(\mathbf{P},\mathbf{P})=-Q_0$.

The three central values of the companion article are the cases $Q_0=-1,0,+1$ of this proposition, and they reproduce the three classifications.

## The Classification

Collecting the two cases, every $\tilde Q$ falls into exactly one of the following rows, and the table is the classification of the block.

| condition on $\tilde Q=Q_0e_0+\mathbf{Q}$ | number of roots |
|---|---|
| $\mathbf{Q}\neq0$, $(\mathbf{Q},\mathbf{Q})\neq0$, $n\neq0$ | four |
| $\mathbf{Q}\neq0$, $(\mathbf{Q},\mathbf{Q})\neq0$, $n=0$ | two |
| $\mathbf{Q}\neq0$, $(\mathbf{Q},\mathbf{Q})=0$, $Q_0\neq0$ | two |
| $\mathbf{Q}\neq0$, $n=0$, $Q_0=0$ | none |
| $\mathbf{Q}=0$ | a four-parameter family |

*Proof.* The table is the classification of *Square Roots of a General Element in the General Plain Algebra*, and the reduction shows that the block's root set is the same set.

**The roots in each row.**

**No roots.** If $\mathbf{Q}\neq0$, $n=0$ and $Q_0=0$, then $\tilde Q$ has no square root of the block and the root set is empty; the radicand is then a pure non-zero isotropic element, that is a **nilpotent** of the block (*Nilpotents of the Symmetric Plain Algebra*).

**Two roots.** If $\mathbf{Q}\neq0$ and either $(\mathbf{Q},\mathbf{Q})\neq0$ with $n=0$, or $(\mathbf{Q},\mathbf{Q})=0$ with $Q_0\neq0$, the root set is a single pair $\tilde P=\pm\bigl(\sqrt{x}\,e_0+\mathbf{Q}/(2\sqrt{x})\bigr)$, with $x=Q_0/2$ in the first instance and $x=Q_0$ in the second.

**Four roots.** If $\mathbf{Q}\neq0$, $(\mathbf{Q},\mathbf{Q})\neq0$ and $n\neq0$, the root set is two pairs, one for each solution $x_\pm$ of the reduced quadratic,

$$
\tilde P=\pm\Bigl(\sqrt{x_+}\,e_0+\frac{\mathbf{Q}}{2\sqrt{x_+}}\Bigr),\qquad
\tilde P=\pm\Bigl(\sqrt{x_-}\,e_0+\frac{\mathbf{Q}}{2\sqrt{x_-}}\Bigr).
$$

**A complex scalar.** If $\tilde Q=Q_0e_0$, the root set is the two elements $\pm\sqrt{Q_0}e_0$ together with the four-real-parameter family of pure $\mathbf{P}$ with $(\mathbf{P},\mathbf{P})=-Q_0$.

**Remark (the block's reading of the degenerate rows).** The rows with $n=0$ are exactly the rows whose radicand is a zero divisor or degenerate of the block, the isotropic cone of the generic norm; the row with no root is the pure isotropic radicand, which is both a nilpotent and a zero divisor; and the four-root row is the invertible radicand, $n\neq0$. So the number of roots is governed by the block's own functional, and the singularity of the root problem is the vanishing of the norm.

## The Three Central Values

The classification specialises to $\tilde Q=-e_0,0,+e_0$ and reproduces the three sets of *Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Algebra*; the agreement is the check that the two computations are the same computation.

| central value | scalar roots | the pure family |
|---|---|---|
| $-e_0$ | $\pm ie_0$ | $(\mathbf{P},\mathbf{P})=1$ |
| $0$ | $0$ | $(\mathbf{P},\mathbf{P})=0$, the nilpotent cone |
| $+e_0$ | $\pm e_0$ | $(\mathbf{P},\mathbf{P})=-1$, indexing the idempotents |

**Corollary.** A pure root of a central value has $\tilde P\bullet\tilde P=\lambda e_0$ with $\lambda=-(\mathbf{P},\mathbf{P})$, and the three families are the pure quadrics of the three central values.

## The Coincidence with the General Plain Algebra

**Theorem.** For every $\tilde Q$ the root set of $\tilde Q$ of the block equals the root set of $\tilde Q$ of the general plain product, and the coincidence is the identity of the two squares.

*Proof.* The equation of the block is $\tilde P^2=\tilde Q$ by the reduction, which is the equation of the algebra.

So the general root theory of the block is the general root theory of the algebra, and the block's contribution is the reading of the conjugate scalar as the generic norm and of the degenerate rows as the isotropic cone and the nilpotent cone.

## Summary

The equation $\tilde P\bullet\tilde P=\tilde Q$ of the block is the plain equation $\tilde P^2=\tilde Q$, so the classification of the general plain algebra transfers verbatim and the root sets coincide. In coordinates the equation is the pair $2P_0\mathbf{P}=\mathbf{Q}$ and $P_0^2-(\mathbf{P},\mathbf{P})=Q_0$; when the vector part of the radicand is non-zero a root is fixed by its scalar part $P_0$, whose square solves the reduced quadratic $4x^2-4Q_0x-(\mathbf{Q},\mathbf{Q})=0$ in $x=P_0^2$, of discriminant $16N(\tilde Q)$; when the radicand is a complex scalar the root is a complex scalar or pure, and the pure roots form the family $(\mathbf{P},\mathbf{P})=-Q_0$. The number of roots is four, two or none according to the signs and the vanishing of $(\mathbf{Q},\mathbf{Q})$ and of the generic norm $n=N(\tilde Q)$; the degenerate rows with $n=0$ are the isotropic radicands, the row with no root is the nilpotent radicand, and the four-root row is the invertible radicand. The three central values reproduce the three sets of the companion article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\bullet\tilde Q$ | the symmetric plain product, the multiplication of the block |
| $\tilde P\bullet\tilde P=\tilde Q$ | the root equation, the plain equation $\tilde P^2=\tilde Q$ |
| $(\mathbf{Q},\mathbf{Q})=Q_1^2+Q_2^2+Q_3^2$ | the complex square of the vector part |
| $n=N(\tilde Q)=Q_0^2+(\mathbf{Q},\mathbf{Q})$ | the generic norm, the conjugate scalar |
| $4x^2-4Q_0x-(\mathbf{Q},\mathbf{Q})=0$, $x=P_0^2$ | the reduced quadratic, of discriminant $16n$ |
| $(\mathbf{P},\mathbf{P})=-Q_0$ | the pure roots of a complex scalar |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures*, §*The Root*, for the product-relative definition.
- *Square Roots of a General Element in the General Plain Algebra*, for the classification the block restates.
- *Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Algebra*, for the three central values.
- *Norm and Invertibility in the Symmetric Plain Algebra*, for the generic norm whose vanishing governs the degenerate rows.
- *Nilpotents of the Symmetric Plain Algebra* and *Zero Divisors of the Symmetric Plain Algebra*, for the radicands with no root and with two roots.
