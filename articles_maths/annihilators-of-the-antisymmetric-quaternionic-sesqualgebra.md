# __Annihilators of the Antisymmetric Quaternionic Sesqualgebra__

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

The block of this article is the **antisymmetric quaternionic sesquimultiplication**
$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}\bigr)
=\mathbf P\times\overline{\mathbf Q},
$$
scalar part zero and vector part the cross product of the vector part of the first argument with
the **conjugate** of the vector part of the second (*Introduction to the Antisymmetric Quaternionic
Sesqualgebra of Biquaternions*). It is the only one of the twelve whose value is a single cross
term, and it is conjugate-alternating, so the two annihilators of an element are one set. Its
zero-divisor set is the whole punctured space (*Zero Divisors of the Antisymmetric Quaternionic
Sesqualgebra*, above this article in this category). The annihilator is the simplest of the twelve:
the **plane** spanned by the centre and the conjugate of the vector part, for every non-central
element. The article owns that reading, the operator with its rank, and the shape of the
annihilator on the remarkable subspaces; the zero-divisor set is the cited article's.

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

Throughout this article the product is the **antisymmetric quaternionic sesquimultiplication**
$\diamond$, and unqualified, *annihilator* means the annihilator of $\diamond$. The left
multiplication is the operator
$$
L_{\tilde P}\tilde X=\tilde P\diamond\tilde X=\mathbf P\times\overline{\mathbf X},
$$
conjugate-linear in $\tilde X$, with kernel the annihilator. The block is the sibling of the
antisymmetric plain sesqualgebra and the antisymmetric quaternionic algebra, whose annihilators are
*Annihilators of the Antisymmetric Plain Sesqualgebra* and *Annihilators of the Antisymmetric
Quaternionic Algebra*.

## The Two Annihilators Coincide

**Theorem (the two annihilators coincide).** For every $\tilde P$,
$$
B_\diamond(\tilde P)=A_\diamond(\tilde P)=\ker L_{\tilde P}.
$$

*Proof.* The block is conjugate-alternating,
$\tilde X\diamond\tilde P=-\overline{\tilde P\diamond\tilde X}$; a vector part is zero exactly when
its conjugate is, so the two products vanish together and the two annihilators are one set.

## The Annihilator of an Element

**Theorem (the annihilator is the centre together with the conjugate of the vector part).** For a
non-central element $\tilde Q$, of vector part $\mathbf Q\neq0$,
$$
A_\diamond(\tilde Q)=B_\diamond(\tilde Q)=\mathbb{C}e_0\oplus\mathbb{C}\overline{\mathbf Q},
$$
a complex plane. For a central element, $\mathbf Q=0$ and $\tilde Q=\lambda e_0$, the operator is
zero and both annihilators are all of $\mathbb{B}$.

*Proof.* The equation $\mathbf Q\times\overline{\mathbf X}=0$ holds exactly when
$\overline{\mathbf X}$ is a complex multiple of $\mathbf Q$, because the cross product of two
vectors of $\mathbb{C}^{3}$ vanishes exactly when they are linearly dependent over $\mathbb{C}$;
this is exactly when $\mathbf X$ is a complex multiple of $\overline{\mathbf Q}$, and the scalar
part $X_0$ is free. The set is therefore the plane
$\mathbb{C}e_0\oplus\mathbb{C}\overline{\mathbf Q}$. For $\mathbf Q=0$ the operator is identically
zero.

**Corollary (the annihilator reads the vector part's direction and nothing else).** The annihilator
of a non-central element depends only on the complex line of the conjugate of the vector part, so
two non-central elements with proportional vector parts have the same annihilator; the scalar part
enters only through the centre, and it does not change the annihilator.

**Example.** For the non-central element $\tilde Q=e_1+ie_2$, of vector part $\mathbf Q=e_1+ie_2$,
the annihilator is the complex plane
$$
A_\diamond(e_1+ie_2)=\mathbb{C}\{e_0,\ e_1-ie_2\}=\mathbb{C}e_0\oplus\mathbb{C}\overline{\mathbf Q}.
$$

## The Multiplication Operator and the Rank

**Corollary (the rank).** The operator $L_{\tilde Q}$ has kernel $A_\diamond(\tilde Q)$, image the
vector subspace $\operatorname{Vect}(\mathbb{B})$, and complex rank two for every non-central
element and rank zero at the centre.

*Proof.* The kernel is the annihilator by definition, of complex dimension two for a non-central
element and four at the centre; the rank is four minus the dimension.

## The Dichotomy

The zero-divisor set of the block is the whole punctured space, so it separates nothing, and the
block is the extreme of the twelve for the simplicity of the annihilator: it is
$\mathbb{C}e_0\oplus\mathbb{C}\overline{\mathbf Q}$ for every non-central element, a plane that
depends on the vector part's direction alone. The block is the sibling of the antisymmetric
quaternionic algebra, whose annihilator is the line $\mathbb{C}\tilde P$ off the cone and a plane
on it, and the sibling of the antisymmetric plain sesqualgebra, whose annihilator is a line or a
plane according to the parent invertibility; here there is no case distinction at all except the
degenerate centre.

## The Annihilator on the Remarkable Subspaces

**The centre.** A nonzero central element $\tilde P=\lambda e_0$ has $L_{\lambda e_0}=0$, so its
annihilator is all of $\mathbb{B}$: the centre annihilates every element on both sides, and the
centre is contained in every annihilator.

**The vector subspace.** On the vector subspace, where $\tilde X$ is pure, the operation is
$\tilde P\diamond\tilde X=\mathbf P\times\overline{\mathbf X}$, and the annihilator of a nonzero
pure element meets the vector subspace in the complex line $\mathbb{C}\overline{\mathbf P}$; the
scalar part of the ambient annihilator is exactly the centre.

**The conjugate-changed subspaces.** The conjugate in the second slot exchanges an element and its
conjugate, so on the Hermitian subspace the annihilator of a nonzero element is the plane
$\mathbb{C}e_0\oplus\mathbb{C}\mathbf Q$, and on the anti-Hermitian subspace it is
$\mathbb{C}e_0\oplus\mathbb{C}\mathbf Q$ with the conjugate line again.

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. The antisymmetric
quaternionic sesquimultiplication is the single cross term
$\tilde P\diamond\tilde X=\mathbf P\times\overline{\mathbf X}$, conjugate-alternating, so the two
annihilators of an element coincide. For a non-central element the common annihilator is the
complex plane $\mathbb{C}e_0\oplus\mathbb{C}\overline{\mathbf Q}$ spanned by the centre and the
conjugate of the vector part, and it depends on the vector part's direction alone; for a central
element the operator is zero and the annihilator is the whole space. The block is the simplest of
the twelve for the annihilator, and its zero-divisor set is the whole punctured space.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=\mathbf P\times\overline{\mathbf Q}$ | the antisymmetric quaternionic sesquimultiplication, the operation $\mathrm{AQS}$ |
| $A_\diamond(\tilde P),B_\diamond(\tilde P)$ | the left and the right annihilator, equal because the block is conjugate-alternating |
| $L_{\tilde P}$ | the left multiplication operator, $L_{\tilde P}\tilde X=\mathbf P\times\overline{\mathbf X}$ |
| $\mathbb{C}e_0\oplus\mathbb{C}\overline{\mathbf Q}$ | the annihilator of a non-central element, a complex plane |
| $\mathbb{B}$ | the annihilator of a central element, the whole space |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre, contained in every annihilator |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*The Zero Divisor and the Annihilator*, for the zero divisor and the annihilator of a general product.
- *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the operation, the class-preserving exchange and its table.
- *Zero Divisors of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/zero-divisors-of-the-antisymmetric-quaternionic-sesqualgebra.md`), above this article in this category, for the punctured space and the comparison with the other products.
- *Annihilators of the Antisymmetric Quaternionic Algebra* (`articles_maths/annihilators-of-the-antisymmetric-quaternionic-algebra.md`), the sibling whose annihilator is a line or a plane.
- *Annihilators of the Antisymmetric Plain Sesqualgebra* (`articles_maths/annihilators-of-the-antisymmetric-plain-sesqualgebra.md`), the sibling whose annihilator is a line or a plane according to the parent invertibility.
- *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/the-conjugate-cross-product-and-the-jacobi-failure-of-the-antisymmetric-quaternionic-sesqualgebra.md`), for the conjugate cross product that carries the block.
