# __Annihilators of the General Quaternionic Sesqualgebra__

## Introduction

The zero divisor of a product is a property of one element alone: it says that *some* nonzero
partner exists that the element kills. The annihilator says *which* partners those are, and it is
the finer object. It is the set of elements killed by a fixed element,
$$
A_\star(\tilde Q)=\{\tilde X:\tilde Q\star\tilde X=0\},\qquad
B_\star(\tilde Q)=\{\tilde X:\tilde X\star\tilde Q=0\},
$$
the left and the right annihilator (*Definitions for the Study of the 12 Algebraic Structures*,
§*The Zero Divisor and the Annihilator*). When the product is carried by a multiplication operator
the annihilator is the kernel of that operator, so it is a linear subspace.

The block of this article is the **general quaternionic sesquimultiplication**
$$
\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q^{*}
=\bigl[P_0Q_0+(\mathbf P,\overline{\mathbf Q})\bigr]-P_0\overline{\mathbf Q}-\overline{Q_0}\mathbf P+\mathbf P\times\overline{\mathbf Q},
$$
the product of the natural conjugate of the first factor with the conjugate of the second
(*Introduction to the General Quaternionic Sesqualgebra of Biquaternions*). It is the block with
**both** involution signs, and its zero divisors are the elements of the cone $C(\tilde P)=0$
(*Zero Divisors of the General Quaternionic Sesqualgebra*, above this article in this category).
The block is the meeting point of the two general families: the cone and the plane of the general
plain algebra, and the two distinct sides of the general plain sesqualgebra, are both present, and
the two annihilators of an element are two distinct planes. The article owns that reading, the
operator with its rank, and the shape of the annihilator on the remarkable subspaces; the
zero-divisor set and its coincidence with the other three general products are the cited article's.

**The results.** The annihilator of an element is the set of partners that it kills, the left and the right annihilator being the kernels of the two one-sided multiplications. For the general quaternionic sesquimultiplication $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q^{*}$ both annihilators are $\{0\}$ off the cone and a complex plane on the cone $C(\tilde P)=0$; the left annihilator is the star of the plain annihilator of $\tilde P^{\natural}$, and the operator is conjugate-linear, of complex rank four off the cone and two on it. The block carries both involution signs, so the two planes are **distinct**. Each section below states its result first and then proves it.

## The Annihilator of a Product

**The annihilator of an element is the set of partners that it kills; the left annihilator is the kernel of the left multiplication and the right annihilator is the kernel of the right multiplication, and they are nonzero exactly when the element is a zero divisor of the corresponding side.**

**Definition (annihilator).** Let $\star$ be a product on $\mathbb{B}$ and let
$\tilde Q\in\mathbb{B}$. The **left annihilator** and the **right annihilator** of $\tilde Q$ in
$\star$ are
$$
A_\star(\tilde Q)=\{\tilde X:\tilde Q\star\tilde X=0\},\qquad
B_\star(\tilde Q)=\{\tilde X:\tilde X\star\tilde Q=0\}.
$$
They are the kernels of the left and the right multiplication, and they are nonzero exactly when
$\tilde Q$ is a zero divisor of the corresponding side.

Throughout this article the product is the **general quaternionic sesquimultiplication** $\star$,
and unqualified, *annihilator* means the annihilator of $\star$. The one-sided multiplications are
the operators
$$
L_{\tilde P}\tilde X=\tilde P^{\natural}\tilde X^{*},\qquad
R_{\tilde P}\tilde X=\tilde X^{\natural}\tilde P^{*},
$$
both conjugate-linear in $\tilde X$, with kernel a complex subspace. The block is the sibling of
the general plain sesqualgebra and of the general quaternionic algebra, whose annihilators are
*Annihilators of the General Plain Sesqualgebra* and *Annihilators of the General Quaternionic
Algebra*.

## The Two Annihilators, and the Conjugate of the Plain Annihilator

**The left annihilator of $\tilde Q$ is the star of the plain left annihilator of $\tilde Q^{\natural}$, of complex dimension two on the cone and $\{0\}$ off it, and on the cone the two annihilators $A_\star(\tilde Q)$ and $B_\star(\tilde Q)$ are distinct complex planes.**

**Theorem (the left annihilator and the plain annihilator).** For every $\tilde Q$,
$$
A_\star(\tilde Q)=\bigl\{\tilde Z^{*}:\tilde Z\in K(\tilde Q^{\natural})\bigr\}=K(\tilde Q^{\natural})^{*},
\qquad K(\tilde Q^{\natural})=\{\tilde Z:\tilde Q^{\natural}\tilde Z=0\},
$$
the image under the involution of the plain annihilator of $\tilde Q^{\natural}$. For a nonzero
element of the cone the left annihilator is of complex dimension two, and off the cone it is
$\{0\}$.

*Proof.* The element $\tilde X$ lies in $A_\star(\tilde Q)$ exactly when
$\tilde Q^{\natural}\tilde X^{*}=0$, that is exactly when $\tilde X^{*}$ lies in the plain left
annihilator of $\tilde Q^{\natural}$; the star is a bijection, so the annihilator is its image. The
dimension is that of the plain annihilator, two when $\tilde Q^{\natural}$ is a nonzero plain zero
divisor, which is exactly $C(\tilde Q^{\natural})=C(\tilde Q)=0$, and zero otherwise.

**Theorem (the two annihilators are distinct on the cone).** For a nonzero zero divisor $\tilde Q$
of the cone the two annihilators $A_\star(\tilde Q)$ and $B_\star(\tilde Q)$ are distinct complex
planes.

*Proof.* Both are of complex dimension two on the cone: the first by the preceding theorem, and the
second is the same computation with $\tilde X^{\natural}\tilde Q^{*}=0$, whose left multiplication
by $\tilde Q^{*}$ has the same rank as that by $\tilde Q^{\natural}$. They are distinct by the
examples below, whose second generators differ.

**Example.** For the non-pure zero divisor $\tilde Q=e_0+ie_1$, of central square $1-1=0$, the two
annihilators are
$$
A_\star(e_0+ie_1)=\mathbb{C}\{e_0+ie_1,\ e_2-ie_3\},\qquad
B_\star(e_0+ie_1)=\mathbb{C}\{e_0+ie_1,\ e_2+ie_3\},
$$
two distinct planes sharing the line $\mathbb{C}\tilde Q$.

## The Multiplication Operator and the Rank

**The conjugate-linear operator $L_{\tilde P}$ is of complex rank four with trivial kernel for a nonzero element off the cone, of rank two with a two-dimensional kernel for a nonzero element on the cone, and the zero operator at the origin.**

The two one-sided multiplications are conjugate-linear, so what is read is the rank, the complex
dimension of the image.

**Corollary (the rank and the annihilator).** The rank of $L_{\tilde P}$ and the annihilator of
$\tilde P$ are

| $\tilde P$ | $C(\tilde P)$ | $\operatorname{rank}L_{\tilde P}$ | $\dim\ker L_{\tilde P}$ |
|---|---|---|---|
| $0$ | $0$ | $0$ | $4$ |
| $\tilde P\neq0$, $C(\tilde P)\neq0$ | $\neq0$ | $4$ | $0$ |
| $\tilde P\neq0$, $C(\tilde P)=0$ | $0$ | $2$ | $2$ |

*Proof.* The star is a bijection, so $L_{\tilde P}$ has the same rank and kernel as the
multiplication $\tilde Z\mapsto\tilde P^{\natural}\tilde Z$ of the general quaternionic algebra,
whose rank is four for a unit of the plain product and two for a nonzero zero divisor.

## The Dichotomy by the Cone

**The annihilator reads the cone twice: off the cone both annihilators are $\{0\}$ and the element is a unit of the plain product, and on the cone each annihilator is a complex plane; the block carries both involution signs, so the two sides are distinct, unlike its two siblings, whose single involution identifies them.**

The zero-divisor set of the block is the punctured cone $\{\tilde Q\neq0:C(\tilde Q)=0\}$, one
equation, and the annihilator reads the cone twice: off the cone both annihilators are $\{0\}$ and
the element is a unit of the plain product, and on the cone each is a complex plane. The block
carries both involution signs, and the two sides are **distinct**: this is the difference from the
general plain sesqualgebra and from the general quaternionic algebra, each of which identifies its
two sides by its single involution. In the meeting of the two signs the coincidence is lost.

## The Annihilator on the Remarkable Subspaces

**On the centre the annihilator is $\{0\}$; on the vector subspace a nonzero element has a complex-plane annihilator exactly when its vector part is isotropic; and on the Hermitian and anti-Hermitian subspaces the two annihilators meet in the conjugate of the plain annihilator, the distinction of the sides being read off the anti-Hermitian directions.**

**The centre.** A nonzero central element $\tilde P=\lambda e_0$ has
$L_{\lambda e_0}\tilde X=\lambda\tilde X^{*}$, whose kernel is the set of the $\tilde X$ with
$\tilde X^{*}=0$, that is $\{0\}$: the central elements are units of the plain product and their
annihilator is $\{0\}$.

**The vector subspace.** A nonzero pure element $\tilde P=\mathbf P$ has
$C(\tilde P)=(\mathbf P,\mathbf P)$; it is a zero divisor of the cone exactly when the vector part
is isotropic, and then each annihilator is a complex plane, the star of the plain annihilator for
the left one and the conjugate of the plain annihilator for the right one.

**The Hermitian and anti-Hermitian subspaces.** On the Hermitian subspace the two involutions agree
on the vector part and the two annihilators meet in the conjugate of the plain annihilator, so the
distinction between the sides is read off the anti-Hermitian directions.

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. The general
quaternionic sesquimultiplication $\tilde P\star\tilde X=\tilde P^{\natural}\tilde X^{*}$ carries
both the natural conjugation and the star, and its two annihilators of an element are **distinct**.
The left annihilator is the star of the plain annihilator of $\tilde P^{\natural}$, and the right
annihilator is the corresponding object of the other side; both are $\{0\}$ off the cone and
complex planes on the cone, and for $\tilde Q=e_0+ie_1$ they are the distinct planes spanned by
$\tilde Q$ and $e_2\mp ie_3$. The block is the meeting point of the two general families, and the
meeting of the two involution signs is exactly what makes the two sides two again.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q^{*}$ | the general quaternionic sesquimultiplication, the operation $\mathrm{GQS}$, the product with both involution signs |
| $A_\star(\tilde P),B_\star(\tilde P)$ | the left and the right annihilator of $\tilde P$ in the block, distinct on the cone |
| $K(\tilde Q^{\natural})=\{\tilde Z:\tilde Q^{\natural}\tilde Z=0\}$ | the plain left annihilator of $\tilde Q^{\natural}$, whose star is the left annihilator of the block |
| $K(\tilde Q^{\natural})^{*}$ | the left annihilator of the block, the star of the plain annihilator |
| $C(\tilde P)=\sum_\mu P_\mu^{2}$ | the central square, the criterion of the cone |
| the two complex planes on the cone | the two annihilators of a nonzero zero divisor, distinct |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*The Zero Divisor and the Annihilator*, for the zero divisor and the annihilator of a general product.
- *Introduction to the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the operation and its table.
- *Zero Divisors of the General Quaternionic Sesqualgebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-sesqualgebra.md`), above this article in this category, for the criterion and the two families.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), the parent, for the cone $C(\tilde P)=0$.
- *Annihilators of the General Plain Sesqualgebra* (`articles_maths/annihilators-of-the-general-plain-sesqualgebra.md`), the sibling whose single star identifies the two sides.
- *Annihilators of the General Quaternionic Algebra* (`articles_maths/annihilators-of-the-general-quaternionic-algebra.md`), the sibling whose single natural conjugation identifies the two sides.
