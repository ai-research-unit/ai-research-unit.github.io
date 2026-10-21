# __Annihilators of the General Plain Sesqualgebra__

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

The block of this article is the **general plain sesquimultiplication**
$$
\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}
=\bigl[Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})\bigr]-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2},
$$
the plain product with the conjugate linear star in the second slot (*Introduction to the General
Plain Sesqualgebra of Biquaternions*). Its zero divisors are again the elements of the cone
$C(\tilde Q_1)=0$ (*Zero Divisors of the General Plain Sesqualgebra*, above this article in this
category), and it is the sibling of the general plain algebra, from which it inherits the cone: the
star in the slot turns the plain annihilator into its conjugate and identifies the two sides. The
article owns that reading, the operator with its rank, and the shape of the annihilator on the
remarkable subspaces; the zero-divisor set and its comparison with the parent and the four general
products are the cited article's.

**The results.** The left and the right multiplications of the block, $L_{\tilde Q_1}\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ and $R_{\tilde Q_1}\tilde Q_2=\tilde Q_2\tilde Q_1^{*}$, are conjugate-linear, and the two annihilators coincide, $A_\star(\tilde Q_1)=B_\star(\tilde Q_1)=\langle\tilde Q_1\rangle_{\natural*}^{*}$, the conjugate of the plain annihilator $\langle\tilde Q_1\rangle_{\natural*}=\{\tilde Q_2:\tilde Q_1\tilde Q_2=0\}$. Off the cone every annihilator is $\{0\}$ and the operator has complex rank four; on the cone each is a complex plane of complex dimension two and the operator has complex rank two. The block is the one of the general products for which the two annihilators are equal rather than merely two.

## The Annihilator of a Product

**The annihilator of an element is the set of partners that it kills, the left and the right annihilator being the kernels of the left multiplication $\tilde Q_1\tilde Q_2^{*}$ and the right multiplication $\tilde Q_2\tilde Q_1^{*}$, and each is nonzero exactly when the element is a zero divisor of the corresponding side.**

**Definition (annihilator).** Let $\star$ be a product on $\mathbb{B}$ and let
$\tilde Q_1\in\mathbb{B}$. The **left annihilator** and the **right annihilator** of $\tilde Q_1$ in
$\star$ are
$$
A_\star(\tilde Q_1)=\{\tilde Q_2:\tilde Q_1\star\tilde Q_2=0\},\qquad
B_\star(\tilde Q_1)=\{\tilde Q_2:\tilde Q_2\star\tilde Q_1=0\}.
$$
They are the kernels of the left and the right multiplication, and they are nonzero exactly when
$\tilde Q_1$ is a zero divisor of the corresponding side.

Throughout this article the product is the **general plain sesquimultiplication** $\star$, and
unqualified, *annihilator* means the annihilator of $\star$. The one-sided multiplications are the
operators
$$
L_{\tilde Q_1}\tilde Q_2=\tilde Q_1\tilde Q_2^{*},\qquad
R_{\tilde Q_1}\tilde Q_2=\tilde Q_2\tilde Q_1^{*},
$$
both conjugate-linear in $\tilde Q_2$ because the star is, with kernel a complex subspace. The block
is the sibling of the general plain algebra, whose annihilators are *Annihilators of the General
Plain Algebra*.

## The Two Annihilators Coincide

**The two annihilators are equal and are the conjugate of the plain annihilator, $B_\star(\tilde Q_1)=A_\star(\tilde Q_1)=\langle\tilde Q_1\rangle_{\natural*}^{*}$ with $\langle\tilde Q_1\rangle_{\natural*}=\{\tilde Q_2:\tilde Q_1\tilde Q_2=0\}$: off the cone both are $\{0\}$ and the element is a unit of the plain product, and on the cone each is a complex plane of complex dimension two.**

**Theorem (the two annihilators are equal, and they are the conjugate of the plain annihilator).**
For every $\tilde Q_1$,
$$
B_\star(\tilde Q_1)=A_\star(\tilde Q_1)=\bigl\{\tilde Q_2^{*}:\tilde Q_2\in \langle\tilde Q_1\rangle_{\natural*}\bigr\}=\langle\tilde Q_1\rangle_{\natural*}^{*},
\qquad \langle\tilde Q_1\rangle_{\natural*}=\{\tilde Q_2:\tilde Q_1\tilde Q_2=0\},
$$
where $\langle\tilde Q_1\rangle_{\natural*}$ is the plain left annihilator of $\tilde Q_1$ and $\langle\tilde Q_1\rangle_{\natural*}^{*}$ is its image
under the involution. For a nonzero zero divisor the two annihilators are equal and of complex
dimension two; for a unit of the plain product both are $\{0\}$.

*Proof.* The left annihilator is
$A_\star(\tilde Q_1)=\{\tilde Q_2:\tilde Q_1\tilde Q_2^{*}=0\}=\{\tilde Q_2:\tilde Q_2^{*}\in \langle\tilde Q_1\rangle_{\natural*}\}=\langle\tilde Q_1\rangle_{\natural*}^{*}$,
the star being a bijection. For the right annihilator, $\tilde Q_2\star\tilde Q_1=0$ reads
$\tilde Q_2\tilde Q_1^{*}=0$, and applying the anti-automorphism ${}^{*}$ gives
$\tilde Q_1\tilde Q_2^{*}=0$, with the converse by the same argument because ${}^{*}$ is a bijection;
the two sets are therefore equal. The dimension is that of the plain annihilator, two on the cone
and zero off it.

**Example.** For the zero divisor $\tilde Q_1=e_t+i\vec e_x$, of central square $1-1=0$, the common
annihilator is
$$
A_\star(e_t+i\vec e_x)=\mathbb{C}\{\vec e_x+ie_t,\ \vec e_y+i\vec e_z\}.
$$

## The Multiplication Operator and the Rank

**The conjugate-linear operator $L_{\tilde Q_1}$ has complex rank four and kernel $\{0\}$ off the cone, complex rank two and kernel of complex dimension two on the cone, and rank $0$ with kernel of dimension four at $\tilde Q_1=0$.**

The two one-sided multiplications are conjugate-linear, so they have no determinant in the complex
sense; what is read is the rank, the complex dimension of the image, which is half the real rank of
the underlying real-linear map.

**Corollary (the rank and the annihilator).** The rank of $L_{\tilde Q_1}$ and the annihilator of
$\tilde Q_1$ are

| $\tilde Q_1$ | $C(\tilde Q_1)$ | $\operatorname{rank}L_{\tilde Q_1}$ | $\dim\ker L_{\tilde Q_1}$ |
|---|---|---|---|
| $0$ | $0$ | $0$ | $4$ |
| $\tilde Q_1\neq0$, $C(\tilde Q_1)\neq0$ | $\neq0$ | $4$ | $0$ |
| $\tilde Q_1\neq0$, $C(\tilde Q_1)=0$ | $0$ | $2$ | $2$ |

*Proof.* The star is a bijection, so $L_{\tilde Q_1}$ has the same rank and kernel as the plain
multiplication $\tilde Q_2\mapsto\tilde Q_1\tilde Q_2$, whose rank is four for a unit and two for a
nonzero zero divisor; the kernel dimension is $4$ minus the rank.

## The Dichotomy by the Cone

**The annihilator reads the cone twice, trivially off it and as a complex plane on it, and the star makes the two sides coincide, where the parent's two annihilators are distinct.**

The zero-divisor set of the block is the punctured cone $\{\tilde Q_1\neq0:C(\tilde Q_1)=0\}$, the same
cone as the parent. The annihilator reads the cone twice, as in the parent: off the cone both
annihilators are $\{0\}$ and the element is a unit of the plain product, and on the cone each is a
complex plane. What the star changes is the coincidence: the two annihilators are equal, and they
are the conjugate of the plain annihilator, whereas in the parent they are distinct. The block is
the sibling of the general quaternionic algebra, whose $\mathbb{C}$-linear involution does the same
work, and it is the sibling of the antipodal *Annihilators of the General Quaternionic
Sesqualgebra*, whose two sides are again distinct.

## The Annihilator on the Remarkable Subspaces

**On every remarkable subspace the annihilator is the ambient one intersected with the subspace: $\{0\}$ off the cone, and the conjugate of the plain annihilator, a complex plane, inside the subspace on the cone.**

**The centre.** A nonzero central element $\tilde Q_1=\lambda e_t$ has
$L_{\lambda e_t}\tilde Q_2=\lambda\tilde Q_2^{*}$, whose kernel is the set of the $\tilde Q_2$ with
$\tilde Q_2^{*}=0$, that is $\{0\}$: the central elements are units of the plain product and their
annihilator is $\{0\}$.

**The vector subspace.** A nonzero pure element $\tilde Q_1=\vec Q_1$ has
$C(\tilde Q_1)=(\vec Q_1,\vec Q_1)$; it is a zero divisor of the cone exactly when the vector part
is isotropic, and then the annihilators are the conjugate of the plain annihilator of $\vec Q_1$,
a complex plane.

**The conjugate-changed subspaces.** The star in the second slot exchanges the element and its
conjugate, so on the Hermitian subspace, where the star fixes the vector part, the annihilator of a
nonzero Hermitian zero divisor is the conjugate of its plain annihilator in the same subspace.

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. The general plain
sesquimultiplication $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ carries the conjugate linear star
in the slot, and the conjugate-alternation identifies the two sides: the two annihilators of an
element are equal and are the conjugate of the plain annihilator
$\langle\tilde Q_1\rangle_{\natural*}=\{\tilde Q_2:\tilde Q_1\tilde Q_2=0\}$. Off the cone both annihilators vanish and the
element is a unit of the plain product; on the cone each is a complex plane. The block is the plain
parent with the star added, and the star is exactly what turns the two distinct planes of the
parent into one plane.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ | the general plain sesquimultiplication, the operation $\mathrm{GPS}$, the plain product with the star in the second slot |
| $A_\star(\tilde Q_1),B_\star(\tilde Q_1)$ | the left and the right annihilator, equal by the conjugate-alternation |
| $\langle\tilde Q_1\rangle_{\natural*}=\{\tilde Q_2:\tilde Q_1\tilde Q_2=0\}$ | the plain left annihilator, the parent's object |
| $\langle\tilde Q_1\rangle_{\natural*}^{*}$ | the common annihilator of the block, the conjugate of the plain annihilator |
| $C(\tilde Q_1)=\sum_\mu Q_{1\mu}^{2}$ | the central square, the criterion of the cone |
| the complex plane on the cone | the annihilator of a nonzero zero divisor, of dimension two |

## Further Reading

- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), §*The Zero Divisor and the Annihilator*, for the zero divisor and the annihilator of a general product.
- [Introduction to the General Plain Sesqualgebra](introduction-to-the-general-plain-sesqualgebra.html), for the operation and its table.
- [Zero Divisors of the General Plain Sesqualgebra](zero-divisors-of-the-general-plain-sesqualgebra.html), above this article in this category, for the criterion and the two families.
- [Zero Divisors of the Biquaternion Algebra](zero-divisors-of-the-biquaternion-algebra.html), the parent, whose two annihilators are distinct.
- [Annihilators of the Biquaternion Algebra](annihilators-of-the-biquaternion-algebra.html), the parent's annihilators, the two distinct planes.
- [Annihilators of the General Quaternionic Sesqualgebra](annihilators-of-the-general-quaternionic-sesqualgebra.html), the sibling whose two sides are distinct again.
