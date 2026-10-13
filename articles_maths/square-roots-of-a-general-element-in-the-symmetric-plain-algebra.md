# __Square Roots of a General Element in the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra $\mathbb{B}^{\bullet}$ is the complex space $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ under the Jordan product $\tilde\Xi\bullet\tilde Q=\tfrac12(\tilde\Xi\tilde Q+\tilde Q\tilde\Xi)$ of *Introduction to the Symmetric Plain Algebra of Biquaternions*. This article determines, for an element $\tilde Q$, the elements $\tilde\Xi$ with $\tilde\Xi\bullet\tilde\Xi=\tilde Q$.

The equation names a product, and throughout this article the square is the one of the symmetric plain product. Because the square of the block is the **plain square**, the equation $\tilde\Xi\bullet\tilde\Xi=\tilde Q$ is the equation $\tilde\Xi^2=\tilde Q$ of the algebra, and the whole classification of *Square Roots of a General Element in the General Plain Algebra* transfers verbatim. What this article adds is the block's notation: the **conjugate scalar** that decides the reduced quadratic is the block's **central square** $C(\tilde Q)=\tilde Q\tilde Q^{\natural}$, so the degeneracy of the root problem is the vanishing of that square, that is the isotropy of $\tilde Q$; the block's zero divisors and invertible elements then read the classification.

A root is defined relative to a product, and the definition is stated once for a general product in *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots*; throughout this article the product is $\bullet$ and, unqualified, **root** means root of $\bullet$. The general root problem of the algebra is *Square Roots of a General Element in the General Plain Algebra*; the roots of $+1$, the roots of $-1$ and the idempotents are *Square Roots of One and the Idempotents of the Symmetric Plain Algebra*; the roots of $0$ and the nilpotents are *Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra*; and the degenerate radicands are *Zero Divisors of the Symmetric Plain Algebra*.

**The results.** The block's equation $\tilde\Xi\bullet\tilde\Xi=\tilde Q$ is the plain equation $\tilde\Xi^2=\tilde Q$, so the root sets of the block and of the general plain product coincide. For a radicand with non-vanishing vector part the roots come in pairs $\pm\tilde\Xi$: there are **four** generically, **two** in the two degenerate rows, and **none** for the rootless row $\mathbf{Q}\neq0$, $Q_0=0$, $C(\tilde Q)=0$; the degeneracy is governed by the central square, whose vanishing is the isotropy of $\tilde Q$. For a complex scalar radicand $\tilde Q=Q_0e_0$ the roots are the two scalars $\pm\sqrt{Q_0}e_0$ together with a **four-parameter family** of pure $\mathbf\Xi$ with $(\mathbf\Xi,\mathbf\Xi)=-Q_0$, and the three central values recover the three sets of the companion articles. Each case below states its answer first and then proves it.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$, central scalar imaginary $i$ and coefficients in $\mathbb{C}$. An element is $\tilde\Xi=\Xi_0e_0+\mathbf\Xi$ with $\mathbf\Xi=\sum_k\Xi_ke_k$, and $(\mathbf\Xi,\mathbf\Xi)=\sum_k\Xi_k^2$. The product with the mark is $\tilde\Xi\bullet\tilde Q=\tfrac12(\tilde\Xi\tilde Q+\tilde Q\tilde\Xi)$; the central square is $C(\tilde Q)=Q_0^2+(\mathbf{Q},\mathbf{Q})=\tilde Q\tilde Q^{\natural}$.

## The Definition and the Reduction

**Definition (root of an element).** Let $\star$ be a product on $\mathbb{B}$; then $\tilde\Xi$ is a **square root of $\tilde Q$ of $\star$** when $\tilde\Xi\star\tilde\Xi=\tilde Q$, and the **root set** of $\tilde Q$ of $\star$ is the set of all such $\tilde\Xi$.

Throughout this article the product is $\bullet$, the equation is

$$
\tilde\Xi\bullet\tilde\Xi=\tilde Q,
$$

and, the two squares being equal, it is the plain equation $\tilde\Xi^2=\tilde Q$; the root set of the block is the root set of the algebra, element by element.

**Theorem (the reduction).** With $\tilde\Xi=\Xi_0e_0+\mathbf\Xi$ and $\tilde Q=Q_0e_0+\mathbf{Q}$, the equation $\tilde\Xi\bullet\tilde\Xi=\tilde Q$ is equivalent to the pair

$$
2\Xi_0\mathbf\Xi=\mathbf{Q},\qquad \Xi_0^2-(\mathbf\Xi,\mathbf\Xi)=Q_0 .
$$

*Proof.* The square of the block is the plain square, $\tilde\Xi\bullet\tilde\Xi=\bigl[\Xi_0^2-(\mathbf\Xi,\mathbf\Xi)\bigr]e_0+2\Xi_0\mathbf\Xi$, and the equality with $\tilde Q$ is the equality of the scalar and the vector parts.

The vector equation decides the shape of the answer, and it has the two outcomes of the algebra: either $\mathbf{Q}\neq0$, and then $\Xi_0\neq0$ and $\mathbf\Xi=\mathbf{Q}/(2\Xi_0)$, so a root is fixed by its scalar part; or $\mathbf{Q}=0$, and then a root is either a complex scalar or pure.

**Definition (the data).** The two data are the complex square of the vector part and the central square,

$$
(\mathbf{Q},\mathbf{Q})=Q_1^2+Q_2^2+Q_3^2,\qquad C=C(\tilde Q)=Q_0^2+(\mathbf{Q},\mathbf{Q})=\tilde Q\tilde Q^{\natural},
$$

and $C$ is the **central square** of the block, an element of $\mathbb{C}$ and not a real number: it is the conjugate scalar of the algebra article. Its vanishing is the condition of isotropy of $\tilde Q$.

## The Roots with Non-Vanishing Vector Part

**For a radicand with non-vanishing vector part a root has $\Xi_0\neq0$ and $\mathbf\Xi=\mathbf{Q}/(2\Xi_0)$, where $x=\Xi_0^2$ solves the reduced quadratic $4x^2-4Q_0x-(\mathbf{Q},\mathbf{Q})=0$, of discriminant $16C(\tilde Q)$; the discriminant vanishes exactly when the radicand is isotropic.**

**Proposition.** Let $\mathbf{Q}\neq0$. Then a root has $\Xi_0\neq0$ and $\mathbf\Xi=\mathbf{Q}/(2\Xi_0)$, and the scalar part $\Xi_0$ satisfies the reduced quadratic

$$
4\Xi_0^4-4Q_0\Xi_0^2-(\mathbf{Q},\mathbf{Q})=0,
\qquad\text{that is}\qquad 4x^2-4Q_0x-(\mathbf{Q},\mathbf{Q})=0\ \text{ in }x=\Xi_0^2 .
$$

*Proof.* Substitute $\mathbf\Xi=\mathbf{Q}/(2\Xi_0)$ into the scalar equation: $\Xi_0^2-\frac{(\mathbf{Q},\mathbf{Q})}{4\Xi_0^2}=Q_0$, and multiply by $4\Xi_0^2$.

**Proposition (the discriminant).** The discriminant of the reduced quadratic $4x^2-4Q_0x-(\mathbf{Q},\mathbf{Q})=0$ is $16C(\tilde Q)$, and it vanishes exactly when $\tilde Q$ is isotropic.

*Proof.* The equation $4x^2-4Q_0x-(\mathbf{Q},\mathbf{Q})=0$ has discriminant $16Q_0^2+16(\mathbf{Q},\mathbf{Q})=16c$.

So the root problem of the block degenerates exactly on the isotropic cone of the central square, which is the locus of the non-invertible elements of *Norm and Invertibility in the Symmetric Plain Algebra*.

## The Roots of a Complex Scalar

**A complex scalar radicand $\tilde Q=Q_0e_0$ has the two scalar roots $\pm\sqrt{Q_0}e_0$ and the four-real-parameter family of pure roots $\mathbf\Xi$ with $(\mathbf\Xi,\mathbf\Xi)=-Q_0$.**

**Proposition.** Let $\tilde Q=Q_0e_0$ be a complex scalar. Then a root is either a complex scalar or pure: the scalars give the two elements $\pm\sqrt{Q_0}e_0$, and the pure roots are the four-real-parameter family of pure $\mathbf\Xi$ with

$$
(\mathbf\Xi,\mathbf\Xi)=-Q_0 .
$$

*Proof.* With $\mathbf{Q}=0$ the vector equation is $2\Xi_0\mathbf\Xi=0$, so $\mathbf\Xi=0$ or $\Xi_0=0$; the first case gives $\Xi_0^2=Q_0$, the second $(\mathbf\Xi,\mathbf\Xi)=-Q_0$.

The three central values of the companion articles are the cases $Q_0=-1,0,+1$ of this proposition, and they reproduce the three classifications of those articles.

## The Classification

**The number of roots is read from the radicand: four when $\mathbf{Q}\neq0$, $(\mathbf{Q},\mathbf{Q})\neq0$ and $C\neq0$; two in the two rows with $\mathbf{Q}\neq0$ and either $(\mathbf{Q},\mathbf{Q})\neq0$, $C=0$ or $(\mathbf{Q},\mathbf{Q})=0$, $Q_0\neq0$; none when $\mathbf{Q}\neq0$, $Q_0=0$ and $C=0$; and a four-parameter family when $\mathbf{Q}=0$.**

Collecting the two cases, every $\tilde Q$ falls into exactly one of the following rows, and the table is the classification of the block.

| condition on $\tilde Q=Q_0e_0+\mathbf{Q}$ | number of roots |
|---|---|
| $\mathbf{Q}\neq0$, $(\mathbf{Q},\mathbf{Q})\neq0$, $C\neq0$ | four |
| $\mathbf{Q}\neq0$, $(\mathbf{Q},\mathbf{Q})\neq0$, $C=0$ | two |
| $\mathbf{Q}\neq0$, $(\mathbf{Q},\mathbf{Q})=0$, $Q_0\neq0$ | two |
| $\mathbf{Q}\neq0$, $C=0$, $Q_0=0$ | none |
| $\mathbf{Q}=0$ | a four-parameter family |

*Proof.* The table is the classification of *Square Roots of a General Element in the General Plain Algebra*, and the reduction shows that the block's root set is the same set.

**The roots in each row.**

**No roots.** If $\mathbf{Q}\neq0$, $C=0$ and $Q_0=0$, then $\tilde Q$ has no square root of the block and the root set is empty; the radicand is then a pure non-zero isotropic element, that is a **nilpotent** of the block (*Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra*).

**Two roots.** If $\mathbf{Q}\neq0$ and either $(\mathbf{Q},\mathbf{Q})\neq0$ with $C=0$, or $(\mathbf{Q},\mathbf{Q})=0$ with $Q_0\neq0$, the root set is a single pair $\tilde\Xi=\pm\bigl(\sqrt{x}\,e_0+\mathbf{Q}/(2\sqrt{x})\bigr)$, with $x=Q_0/2$ in the first instance and $x=Q_0$ in the second.

**Four roots.** If $\mathbf{Q}\neq0$, $(\mathbf{Q},\mathbf{Q})\neq0$ and $C\neq0$, the root set is two pairs, one for each solution $x_\pm$ of the reduced quadratic,

$$
\tilde\Xi=\pm\Bigl(\sqrt{x_+}\,e_0+\frac{\mathbf{Q}}{2\sqrt{x_+}}\Bigr),\qquad
\tilde\Xi=\pm\Bigl(\sqrt{x_-}\,e_0+\frac{\mathbf{Q}}{2\sqrt{x_-}}\Bigr).
$$

**A complex scalar.** If $\tilde Q=Q_0e_0$, the root set is the two elements $\pm\sqrt{Q_0}e_0$ together with the four-real-parameter family of pure $\mathbf\Xi$ with $(\mathbf\Xi,\mathbf\Xi)=-Q_0$.

**Remark (the block's reading of the degenerate rows).** The rows with $C=0$ are exactly the rows whose radicand is a zero divisor or degenerate of the block, the isotropic cone of the central square; the row with no root is the pure isotropic radicand, which is both a nilpotent and a zero divisor; and the four-root row is the invertible radicand, $C\neq0$. So the number of roots is governed by the central square, and the singularity of the root problem is its vanishing.

## The Three Central Values

**At the three central values the classification reproduces the three sets of the companion articles: the roots of $-e_0$ are the central $\pm ie_0$ with pure quadric $(\mathbf\Xi,\mathbf\Xi)=1$, the roots of $0$ are the origin with the nilpotent cone, and the roots of $+e_0$ are the central $\pm e_0$ with the pure quadric $(\mathbf\Xi,\mathbf\Xi)=-1$ that indexes the idempotents.**

The classification specialises to $\tilde Q=-e_0,0,+e_0$ and reproduces the roots of $+1$ and of $-1$ of *Square Roots of One and the Idempotents of the Symmetric Plain Algebra* and the roots of $0$ of *Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra*; the agreement is the check that the computations are the same computation.

| central value | scalar roots | the pure family |
|---|---|---|
| $-e_0$ | $\pm ie_0$ | $(\mathbf\Xi,\mathbf\Xi)=1$ |
| $0$ | $0$ | $(\mathbf\Xi,\mathbf\Xi)=0$, the nilpotent cone |
| $+e_0$ | $\pm e_0$ | $(\mathbf\Xi,\mathbf\Xi)=-1$, indexing the idempotents |

**Corollary.** A pure root of a central value has $\tilde\Xi\bullet\tilde\Xi=\lambda e_0$ with $\lambda=-(\mathbf\Xi,\mathbf\Xi)$, and the three families are the pure quadrics of the three central values.

## The Coincidence with the General Plain Algebra

**For every $\tilde Q$ the root set of $\tilde Q$ of the block equals the root set of $\tilde Q$ of the general plain product, the coincidence being the identity of the two squares.**

**Theorem.** For every $\tilde Q$ the root set of $\tilde Q$ of the block equals the root set of $\tilde Q$ of the general plain product, and the coincidence is the identity of the two squares.

*Proof.* The equation of the block is $\tilde\Xi^2=\tilde Q$ by the reduction, which is the equation of the algebra.

So the general root theory of the block is the general root theory of the algebra, and the block's contribution is the reading of the conjugate scalar as the central square and of the degenerate rows as the isotropic cone and the nilpotent cone.

## Summary

The equation $\tilde\Xi\bullet\tilde\Xi=\tilde Q$ of the block is the plain equation $\tilde\Xi^2=\tilde Q$, so the classification of the general plain algebra transfers verbatim and the root sets coincide. In coordinates the equation is the pair $2\Xi_0\mathbf\Xi=\mathbf{Q}$ and $\Xi_0^2-(\mathbf\Xi,\mathbf\Xi)=Q_0$; when the vector part of the radicand is non-zero a root is fixed by its scalar part $\Xi_0$, whose square solves the reduced quadratic $4x^2-4Q_0x-(\mathbf{Q},\mathbf{Q})=0$ in $x=\Xi_0^2$, of discriminant $16C(\tilde Q)$; when the radicand is a complex scalar the root is a complex scalar or pure, and the pure roots form the family $(\mathbf\Xi,\mathbf\Xi)=-Q_0$. The number of roots is four, two or none according to the signs and the vanishing of $(\mathbf{Q},\mathbf{Q})$ and of the central square $C=C(\tilde Q)$; the degenerate rows with $C=0$ are the isotropic radicands, the row with no root is the nilpotent radicand, and the four-root row is the invertible radicand. The three central values reproduce the three sets of the companion articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi\bullet\tilde Q$ | the symmetric plain product, the multiplication of the block |
| $\tilde\Xi\bullet\tilde\Xi=\tilde Q$ | the root equation, the plain equation $\tilde\Xi^2=\tilde Q$ |
| $(\mathbf{Q},\mathbf{Q})=Q_1^2+Q_2^2+Q_3^2$ | the complex square of the vector part |
| $C=C(\tilde Q)=Q_0^2+(\mathbf{Q},\mathbf{Q})$ | the central square, the conjugate scalar |
| $4x^2-4Q_0x-(\mathbf{Q},\mathbf{Q})=0$, $x=\Xi_0^2$ | the reduced quadratic, of discriminant $16C(\tilde Q)$ |
| $(\mathbf\Xi,\mathbf\Xi)=-Q_0$ | the pure roots of a complex scalar |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots*, for the product-relative definition.
- *Square Roots of a General Element in the General Plain Algebra*, for the classification the block restates.
- *Square Roots of One and the Idempotents of the Symmetric Plain Algebra*, for the roots of $+1$ and the roots of $-1$, the first two central values.
- *Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra*, for the roots of $0$, the third central value.
- *Norm and Invertibility in the Symmetric Plain Algebra*, for the invertible elements, the four-root row of the classification.
- *Zero Divisors of the Symmetric Plain Algebra*, for the radicands with no root and with two roots.
