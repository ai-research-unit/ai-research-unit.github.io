# __Annihilators of the General Quaternionic Sesqualgebra__

## Introduction

The zero divisor of a product is a property of one element alone: it says that *some* nonzero
partner exists that the element kills. The annihilator says *which* partners those are, and it is
the finer object. It is the set of elements killed by a fixed element,
$$
A_\star(\tilde Q_1)=\{\tilde Q_2:\tilde Q_1\star\tilde Q_2=0\},\qquad
B_\star(\tilde Q_1)=\{\tilde Q_2:\tilde Q_2\star\tilde Q_1=0\},
$$
the left and the right annihilator (*Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*,
§*The Zero Divisor and the Annihilator*). When the product is carried by a multiplication operator
the annihilator is the kernel of that operator, so it is a linear subspace.

The block of this article is the **general quaternionic sesquimultiplication**
$$
\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2^{*}
=\bigl[Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})\bigr]-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1+\vec Q_1\times\overline{\vec Q_2},
$$
the product of the natural conjugate of the first factor with the conjugate of the second
(*Introduction to the General Quaternionic Sesqualgebra*). It is the block with
**both** involution signs, and its zero divisors are the elements of the cone $C(\tilde Q_1)=0$
(*Zero Divisors of the General Quaternionic Sesqualgebra*, above this article in this category).
The block is the meeting point of the two general families: the cone and the plane of the general
plain algebra, and the two distinct sides of the general plain sesqualgebra, are both present, and
the two annihilators of an element are two distinct planes. The article owns that reading, the
operator with its rank, and the shape of the annihilator on the remarkable subspaces; the
zero-divisor set and its coincidence with the other three general products are the cited article's.

**The results.** The annihilator of an element is the set of partners that it kills, the left and the right annihilator being the kernels of the two one-sided multiplications. For the general quaternionic sesquimultiplication $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2^{*}$ both annihilators are $\{0\}$ off the cone and a complex plane on the cone $C(\tilde Q_1)=0$; the left annihilator is the star of the plain annihilator of $\tilde Q_1^{\natural}$, and the operator is conjugate-linear, of complex rank four off the cone and two on it. The block carries both involution signs, so the two planes are **distinct**. Each section below states its result first and then proves it.

## The Annihilator of a Product

**The annihilator of an element is the set of partners that it kills; the left annihilator is the kernel of the left multiplication and the right annihilator is the kernel of the right multiplication, and they are nonzero exactly when the element is a zero divisor of the corresponding side.**

**Definition (annihilator).** Let $\star$ be a product on $\mathbb{B}$ and let
$\tilde Q_1\in\mathbb{B}$. The **left annihilator** and the **right annihilator** of $\tilde Q_1$ in
$\star$ are
$$
A_\star(\tilde Q_1)=\{\tilde Q_2:\tilde Q_1\star\tilde Q_2=0\},\qquad
B_\star(\tilde Q_1)=\{\tilde Q_2:\tilde Q_2\star\tilde Q_1=0\}.
$$
They are the kernels of the left and the right multiplication, and they are nonzero exactly when
$\tilde Q_1$ is a zero divisor of the corresponding side.

Throughout this article the product is the **general quaternionic sesquimultiplication** $\star$,
and unqualified, *annihilator* means the annihilator of $\star$. The one-sided multiplications are
the operators
$$
L_{\tilde Q_1}\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2^{*},\qquad
R_{\tilde Q_1}\tilde Q_2=\tilde Q_2^{\natural}\tilde Q_1^{*},
$$
both conjugate-linear in $\tilde Q_2$, with kernel a complex subspace. The block is the sibling of
the general plain sesqualgebra and of the general quaternionic algebra, whose annihilators are
*Annihilators of the General Plain Sesqualgebra* and *Annihilators of the General Quaternionic
Algebra*.

## The Two Annihilators, and the Conjugate of the Plain Annihilator

**The left annihilator of $\tilde Q_1$ is the star of the plain left annihilator of $\tilde Q_1^{\natural}$, of complex dimension two on the cone and $\{0\}$ off it, and on the cone the two annihilators $A_\star(\tilde Q_1)$ and $B_\star(\tilde Q_1)$ are distinct complex planes.**

**Theorem (the left annihilator and the plain annihilator).** For every $\tilde Q_1$,
$$
A_\star(\tilde Q_1)=\bigl\{\tilde Q_2^{*}:\tilde Q_2\in \langle\tilde Q_1^{\natural}\rangle_{\natural*}\bigr\}=\langle\tilde Q_1^{\natural}\rangle_{\natural*}^{*},
\qquad \langle\tilde Q_1^{\natural}\rangle_{\natural*}=\{\tilde Q_2:\tilde Q_1^{\natural}\tilde Q_2=0\},
$$
the image under the involution of the plain annihilator of $\tilde Q_1^{\natural}$. For a nonzero
element of the cone the left annihilator is of complex dimension two, and off the cone it is
$\{0\}$.

*Proof.* The element $\tilde Q_2$ lies in $A_\star(\tilde Q_1)$ exactly when
$\tilde Q_1^{\natural}\tilde Q_2^{*}=0$, that is exactly when $\tilde Q_2^{*}$ lies in the plain left
annihilator of $\tilde Q_1^{\natural}$; the star is a bijection, so the annihilator is its image. The
dimension is that of the plain annihilator, two when $\tilde Q_1^{\natural}$ is a nonzero plain zero
divisor, which is exactly $C(\tilde Q_1^{\natural})=C(\tilde Q_1)=0$, and zero otherwise.

**Theorem (the two annihilators are distinct on the cone).** For a nonzero zero divisor $\tilde Q_1$
of the cone the two annihilators $A_\star(\tilde Q_1)$ and $B_\star(\tilde Q_1)$ are distinct complex
planes.

*Proof.* Both are of complex dimension two on the cone: the first by the preceding theorem, and the
second is the same computation with $\tilde Q_2^{\natural}\tilde Q_1^{*}=0$, whose left multiplication
by $\tilde Q_1^{*}$ has the same rank as that by $\tilde Q_1^{\natural}$. They are distinct by the
examples below, whose second generators differ.

**Example.** For the non-pure zero divisor $\tilde Q_1=e_t+i\vec e_x$, of central square $1-1=0$, the two
annihilators are
$$
A_\star(e_t+i\vec e_x)=\mathbb{C}\{e_t+i\vec e_x,\ \vec e_y-i\vec e_z\},\qquad
B_\star(e_t+i\vec e_x)=\mathbb{C}\{e_t+i\vec e_x,\ \vec e_y+i\vec e_z\},
$$
two distinct planes sharing the line $\mathbb{C}\tilde Q_1$.

## The Multiplication Operator and the Rank

**The conjugate-linear operator $L_{\tilde Q_1}$ is of complex rank four with trivial kernel for a nonzero element off the cone, of rank two with a two-dimensional kernel for a nonzero element on the cone, and the zero operator at the origin.**

The two one-sided multiplications are conjugate-linear, so what is read is the rank, the complex
dimension of the image.

**Corollary (the rank and the annihilator).** The rank of $L_{\tilde Q_1}$ and the annihilator of
$\tilde Q_1$ are

| $\tilde Q_1$ | $C(\tilde Q_1)$ | $\operatorname{rank}L_{\tilde Q_1}$ | $\dim\ker L_{\tilde Q_1}$ |
|---|---|---|---|
| $0$ | $0$ | $0$ | $4$ |
| $\tilde Q_1\neq0$, $C(\tilde Q_1)\neq0$ | $\neq0$ | $4$ | $0$ |
| $\tilde Q_1\neq0$, $C(\tilde Q_1)=0$ | $0$ | $2$ | $2$ |

*Proof.* The star is a bijection, so $L_{\tilde Q_1}$ has the same rank and kernel as the
multiplication $\tilde Q_2\mapsto\tilde Q_1^{\natural}\tilde Q_2$ of the general quaternionic algebra,
whose rank is four for a unit of the plain product and two for a nonzero zero divisor.

## The Dichotomy by the Cone

**The annihilator reads the cone twice: off the cone both annihilators are $\{0\}$ and the element is a unit of the plain product, and on the cone each annihilator is a complex plane; the block carries both involution signs, so the two sides are distinct, unlike its two siblings, whose single involution identifies them.**

The zero-divisor set of the block is the punctured cone $\{\tilde Q_1\neq0:C(\tilde Q_1)=0\}$, one
equation, and the annihilator reads the cone twice: off the cone both annihilators are $\{0\}$ and
the element is a unit of the plain product, and on the cone each is a complex plane. The block
carries both involution signs, and the two sides are **distinct**: this is the difference from the
general plain sesqualgebra and from the general quaternionic algebra, each of which identifies its
two sides by its single involution. In the meeting of the two signs the coincidence is lost.

## The Annihilator on the Remarkable Subspaces

**On the centre the annihilator is $\{0\}$; on the vector subspace a nonzero element has a complex-plane annihilator exactly when its vector part is isotropic; and on the Hermitian and anti-Hermitian subspaces the two annihilators meet in the conjugate of the plain annihilator, the distinction of the sides being read off the anti-Hermitian directions.**

**The centre.** A nonzero central element $\tilde Q_1=\lambda e_t$ has
$L_{\lambda e_t}\tilde Q_2=\lambda\tilde Q_2^{*}$, whose kernel is the set of the $\tilde Q_2$ with
$\tilde Q_2^{*}=0$, that is $\{0\}$: the central elements are units of the plain product and their
annihilator is $\{0\}$.

**The vector subspace.** A nonzero pure element $\tilde Q_1=\vec Q_1$ has
$C(\tilde Q_1)=(\vec Q_1,\vec Q_1)$; it is a zero divisor of the cone exactly when the vector part
is isotropic, and then each annihilator is a complex plane, the star of the plain annihilator for
the left one and the conjugate of the plain annihilator for the right one.

**The Hermitian and anti-Hermitian subspaces.** On the Hermitian subspace the two involutions agree
on the vector part and the two annihilators meet in the conjugate of the plain annihilator, so the
distinction between the sides is read off the anti-Hermitian directions.

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. The general
quaternionic sesquimultiplication $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2^{*}$ carries
both the natural conjugation and the star, and its two annihilators of an element are **distinct**.
The left annihilator is the star of the plain annihilator of $\tilde Q_1^{\natural}$, and the right
annihilator is the corresponding object of the other side; both are $\{0\}$ off the cone and
complex planes on the cone, and for $\tilde Q_1=e_t+i\vec e_x$ they are the distinct planes spanned by
$\tilde Q_1$ and $\vec e_y\mp i\vec e_z$. The block is the meeting point of the two general families, and the
meeting of the two involution signs is exactly what makes the two sides two again.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2^{*}$ | the general quaternionic sesquimultiplication, the operation $\mathrm{GQS}$, the product with both involution signs |
| $A_\star(\tilde Q_1),B_\star(\tilde Q_1)$ | the left and the right annihilator of $\tilde Q_1$ in the block, distinct on the cone |
| $\langle\tilde Q_1^{\natural}\rangle_{\natural*}=\{\tilde Q_2:\tilde Q_1^{\natural}\tilde Q_2=0\}$ | the plain left annihilator of $\tilde Q_1^{\natural}$, whose star is the left annihilator of the block |
| $\langle\tilde Q_1^{\natural}\rangle_{\natural*}^{*}$ | the left annihilator of the block, the star of the plain annihilator |
| $C(\tilde Q_1)=\sum_\mu Q_{1,\mu}^{2}$ | the central square, the criterion of the cone |
| the two complex planes on the cone | the two annihilators of a nonzero zero divisor, distinct |

## Further Reading

- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), §*The Zero Divisor and the Annihilator*, for the zero divisor and the annihilator of a general product.
- [Introduction to the General Quaternionic Sesqualgebra](introduction-to-the-general-quaternionic-sesqualgebra.html), for the operation and its table.
- [Zero Divisors of the General Quaternionic Sesqualgebra](zero-divisors-of-the-general-quaternionic-sesqualgebra.html), above this article in this category, for the criterion and the two families.
- [Zero Divisors of the Biquaternion Algebra](zero-divisors-of-the-biquaternion-algebra.html), the parent, for the cone $C(\tilde Q_1)=0$.
- [Annihilators of the General Plain Sesqualgebra](annihilators-of-the-general-plain-sesqualgebra.html), the sibling whose single star identifies the two sides.
- [Annihilators of the General Quaternionic Algebra](annihilators-of-the-general-quaternionic-algebra.html), the sibling whose single natural conjugation identifies the two sides.
