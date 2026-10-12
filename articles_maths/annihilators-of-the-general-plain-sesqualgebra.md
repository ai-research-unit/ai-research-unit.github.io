# __Annihilators of the General Plain Sesqualgebra__

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

The block of this article is the **general plain sesquimultiplication**
$$
\tilde P\star\tilde Q=\tilde P\tilde Q^{*}
=\bigl[P_0Q_0-(\mathbf P,\overline{\mathbf Q})\bigr]+P_0\overline{\mathbf Q}+\overline{Q_0}\mathbf P-\mathbf P\times\overline{\mathbf Q},
$$
the plain product with the conjugate linear star in the second slot (*Introduction to the General
Plain Sesqualgebra of Biquaternions*). Its zero divisors are again the elements of the cone
$C(\tilde P)=0$ (*Zero Divisors of the General Plain Sesqualgebra*, above this article in this
category), and it is the sibling of the general plain algebra, from which it inherits the cone: the
star in the slot turns the plain annihilator into its conjugate and identifies the two sides. The
article owns that reading, the operator with its rank, and the shape of the annihilator on the
remarkable subspaces; the zero-divisor set and its comparison with the parent and the four general
products are the cited article's.

## The Annihilator of a Product

**Definition (annihilator).** Let $\star$ be a product on $\mathbb{B}$ and let
$\tilde Q\in\mathbb{B}$. The **left annihilator** and the **right annihilator** of $\tilde Q$ in
$\star$ are
$$
A_\star(\tilde Q)=\{\tilde X:\tilde Q\star\tilde X=0\},\qquad
B_\star(\tilde Q)=\{\tilde X:\tilde X\star\tilde Q=0\}.
$$
They are the kernels of the left and the right multiplication, and they are nonzero exactly when
$\tilde Q$ is a zero divisor of the corresponding side.

Throughout this article the product is the **general plain sesquimultiplication** $\star$, and
unqualified, *annihilator* means the annihilator of $\star$. The one-sided multiplications are the
operators
$$
L_{\tilde P}\tilde X=\tilde P\tilde X^{*},\qquad
R_{\tilde P}\tilde X=\tilde X\tilde P^{*},
$$
both conjugate-linear in $\tilde X$ because the star is, with kernel a complex subspace. The block
is the sibling of the general plain algebra, whose annihilators are *Annihilators of the General
Plain Algebra*.

## The Two Annihilators Coincide

**Theorem (the two annihilators are equal, and they are the conjugate of the plain annihilator).**
For every $\tilde Q$,
$$
B_\star(\tilde Q)=A_\star(\tilde Q)=\bigl\{\tilde Z^{*}:\tilde Z\in K(\tilde Q)\bigr\}=K(\tilde Q)^{*},
\qquad K(\tilde Q)=\{\tilde Z:\tilde Q\tilde Z=0\},
$$
where $K(\tilde Q)$ is the plain left annihilator of $\tilde Q$ and $K(\tilde Q)^{*}$ is its image
under the involution. For a nonzero zero divisor the two annihilators are equal and of complex
dimension two; for a unit of the plain product both are $\{0\}$.

*Proof.* The right annihilator is
$B_\star(\tilde Q)=\{\tilde X:\tilde Q\tilde X^{*}=0\}=\{\tilde X:\tilde X^{*}\in K(\tilde Q)\}=K(\tilde Q)^{*}$,
the star being a bijection. For the left annihilator, $\tilde X\star\tilde Q=0$ reads
$\tilde X\tilde Q^{*}=0$, and applying the anti-automorphism ${}^{*}$ gives
$\tilde Q\tilde X^{*}=0$, with the converse by the same argument because ${}^{*}$ is a bijection;
the two sets are therefore equal. The dimension is that of the plain annihilator, two on the cone
and zero off it.

**Example.** For the zero divisor $\tilde Q=e_0+ie_1$, of central square $1-1=0$, the common
annihilator is
$$
A_\star(e_0+ie_1)=\mathbb{C}\{e_1+ie_0,\ e_2+ie_3\}.
$$

## The Multiplication Operator and the Rank

The two one-sided multiplications are conjugate-linear, so they have no determinant in the complex
sense; what is read is the rank, the complex dimension of the image, which is half the real rank of
the underlying real-linear map.

**Corollary (the rank and the annihilator).** The rank of $L_{\tilde P}$ and the annihilator of
$\tilde P$ are

| $\tilde P$ | $C(\tilde P)$ | $\operatorname{rank}L_{\tilde P}$ | $\dim\ker L_{\tilde P}$ |
|---|---|---|---|
| $0$ | $0$ | $0$ | $4$ |
| $\tilde P\neq0$, $C(\tilde P)\neq0$ | $\neq0$ | $4$ | $0$ |
| $\tilde P\neq0$, $C(\tilde P)=0$ | $0$ | $2$ | $2$ |

*Proof.* The star is a bijection, so $L_{\tilde P}$ has the same rank and kernel as the plain
multiplication $\tilde Z\mapsto\tilde P\tilde Z$, whose rank is four for a unit and two for a
nonzero zero divisor; the kernel dimension is $4$ minus the rank.

## The Dichotomy by the Cone

The zero-divisor set of the block is the punctured cone $\{\tilde Q\neq0:C(\tilde Q)=0\}$, the same
cone as the parent. The annihilator reads the cone twice, as in the parent: off the cone both
annihilators are $\{0\}$ and the element is a unit of the plain product, and on the cone each is a
complex plane. What the star changes is the coincidence: the two annihilators are equal, and they
are the conjugate of the plain annihilator, whereas in the parent they are distinct. The block is
the sibling of the general quaternionic algebra, whose $\mathbb{C}$-linear involution does the same
work, and it is the sibling of the antipodal *Annihilators of the General Quaternionic
Sesqualgebra*, whose two sides are again distinct.

## The Annihilator on the Remarkable Subspaces

**The centre.** A nonzero central element $\tilde P=\lambda e_0$ has
$L_{\lambda e_0}\tilde X=\lambda\tilde X^{*}$, whose kernel is the set of the $\tilde X$ with
$\tilde X^{*}=0$, that is $\{0\}$: the central elements are units of the plain product and their
annihilator is $\{0\}$.

**The vector subspace.** A nonzero pure element $\tilde P=\mathbf P$ has
$C(\tilde P)=(\mathbf P,\mathbf P)$; it is a zero divisor of the cone exactly when the vector part
is isotropic, and then the annihilators are the conjugate of the plain annihilator of $\mathbf P$,
a complex plane.

**The conjugate-changed subspaces.** The star in the second slot exchanges the element and its
conjugate, so on the Hermitian subspace, where the star fixes the vector part, the annihilator of a
nonzero Hermitian zero divisor is the conjugate of its plain annihilator in the same subspace.

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. The general plain
sesquimultiplication $\tilde P\star\tilde X=\tilde P\tilde X^{*}$ carries the conjugate linear star
in the slot, and the conjugate-alternation identifies the two sides: the two annihilators of an
element are equal and are the conjugate of the plain annihilator
$K(\tilde Q)=\{\tilde Z:\tilde Q\tilde Z=0\}$. Off the cone both annihilators vanish and the
element is a unit of the plain product; on the cone each is a complex plane. The block is the plain
parent with the star added, and the star is exactly what turns the two distinct planes of the
parent into one plane.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ | the general plain sesquimultiplication, the operation $\mathrm{GPS}$, the plain product with the star in the second slot |
| $A_\star(\tilde P),B_\star(\tilde P)$ | the left and the right annihilator, equal by the conjugate-alternation |
| $K(\tilde Q)=\{\tilde Z:\tilde Q\tilde Z=0\}$ | the plain left annihilator, the parent's object |
| $K(\tilde Q)^{*}$ | the common annihilator of the block, the conjugate of the plain annihilator |
| $C(\tilde P)=\sum_\mu P_\mu^{2}$ | the central square, the criterion of the cone |
| the complex plane on the cone | the annihilator of a nonzero zero divisor, of dimension two |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*The Zero Divisor and the Annihilator*, for the zero divisor and the annihilator of a general product.
- *Introduction to the General Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-sesqualgebra-of-biquaternions.md`), for the operation and its table.
- *Zero Divisors of the General Plain Sesqualgebra* (`articles_maths/zero-divisors-of-the-general-plain-sesqualgebra.md`), above this article in this category, for the criterion and the two families.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), the parent, whose two annihilators are distinct.
- *Annihilators of the General Plain Algebra* (`articles_maths/annihilators-of-the-general-plain-algebra.md`), the parent's annihilators, the two distinct planes.
- *Annihilators of the General Quaternionic Sesqualgebra* (`articles_maths/annihilators-of-the-general-quaternionic-sesqualgebra.md`), the sibling whose two sides are distinct again.
