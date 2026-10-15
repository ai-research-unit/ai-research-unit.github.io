# __Annihilators of the Antisymmetric Plain Sesqualgebra__

## Introduction

The zero divisor of a product is a property of one element alone: it says that *some* nonzero
partner exists that the element kills. The annihilator says *which* partners those are, and it is
the finer object. It is the set of elements killed by a fixed element,
$$
A_\star(\tilde Q)=\{\tilde X:\tilde Q\star\tilde X=0\},\qquad
B_\star(\tilde Q)=\{\tilde X:\tilde X\star\tilde Q=0\},
$$
the left and the right annihilator (*Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*,
§*The Zero Divisor and the Annihilator*). When the product is carried by a multiplication operator
the annihilator is the kernel of that operator, so it is a linear subspace.

The block of this article is the **antisymmetric plain sesquimultiplication**
$$
\tilde P\diamond\tilde Q=\operatorname{Vect}\bigl(\tilde P\tilde Q^{*}\bigr)
=\tfrac12\bigl(\tilde P\tilde Q^{*}-\overline{\tilde Q\tilde P^{*}}\bigr),
$$
the vector part of the sesquilinear plain product (*Introduction to the Antisymmetric Plain
Sesqualgebra of Biquaternions*). It is conjugate-alternating, so the two annihilators of an element
are one set. Its zero-divisor set is the whole punctured space (*Zero Divisors of the
Antisymmetric Plain Sesqualgebra*, above this article in this category), and it is the block for
which the annihilator is read through the parent invertibility: a **line** when the element is a
unit of the plain product and a **plane** when it is not. The article owns that reading, the
operator with its rank, and the shape of the annihilator on the remarkable subspaces; the
zero-divisor set and the contrast with the four general products are the cited article's.

**The results.** The annihilator of an element is the set of partners that it kills. The block is conjugate-alternating, so the two annihilators of an element coincide, $B_\diamond(\tilde Q)=A_\diamond(\tilde Q)$; for a nonzero $\tilde Q$ the common annihilator is the star of the central-carrying set, $A_\diamond(\tilde Q)=\{\tilde Z^{*}:\tilde Q\tilde Z\in\mathbb{C}_{\mathbb{B}}\}$. It is a **complex line** when $\tilde Q$ is invertible in the plain product and a **complex plane** when it is not, so the annihilator measures the parent invertibility. The operator $L_{\tilde Q}$ has complex rank three on the plain units, two on the plain zero divisors and zero at the origin.

## The Annihilator of a Product

**The annihilator of an element is the set of partners that it kills; the left annihilator is the kernel of the left multiplication and the right annihilator is the kernel of the right multiplication, and each is nonzero exactly when the element is a zero divisor of the corresponding side.**

**Definition (annihilator).** Let $\star$ be a product on $\mathbb{B}$ and let
$\tilde Q\in\mathbb{B}$. The **left annihilator** and the **right annihilator** of $\tilde Q$ in
$\star$ are
$$
A_\star(\tilde Q)=\{\tilde X:\tilde Q\star\tilde X=0\},\qquad
B_\star(\tilde Q)=\{\tilde X:\tilde X\star\tilde Q=0\}.
$$
They are the kernels of the left and the right multiplication, and they are nonzero exactly when
$\tilde Q$ is a zero divisor of the corresponding side.

Throughout this article the product is the **antisymmetric plain sesquimultiplication** $\diamond$,
and unqualified, *annihilator* means the annihilator of $\diamond$. The left multiplication is the
operator
$$
L_{\tilde P}\tilde X=\tilde P\diamond\tilde X=\operatorname{Vect}\bigl(\tilde P\tilde X^{*}\bigr),
$$
conjugate-linear in $\tilde X$, with kernel the annihilator. The block is the sibling of the
antisymmetric quaternionic sesqualgebra and of the general plain sesqualgebra, whose annihilators
are *Annihilators of the Antisymmetric Quaternionic Sesqualgebra* and *Annihilators of the General
Plain Sesqualgebra*.

## The Two Annihilators Coincide

**For every element the right annihilator equals the left one, $B_\diamond(\tilde Q)=A_\diamond(\tilde Q)$, because the block is conjugate-alternating, so the block has one annihilator per element and not two.**

**Corollary (the right annihilator equals the left one).** For every $\tilde Q$,
$$
B_\diamond(\tilde Q)=A_\diamond(\tilde Q),
$$
so the block has one annihilator per element and not two.

*Proof.* The block is conjugate-alternating,
$\tilde R\diamond\tilde Q=-\overline{\tilde Q\diamond\tilde R}$; a vector part is zero exactly when
its conjugate is, so the two products vanish together and the two annihilators are one set.

## The Annihilator of an Element

**For a nonzero element the common annihilator is the star of the set of the $\tilde Z$ with $\tilde Q\tilde Z$ central, $A_\diamond(\tilde Q)=\{\tilde Z^{*}:\tilde Q\tilde Z\in\mathbb{C}_{\mathbb{B}}\}$, a complex line when $\tilde Q$ is invertible in the plain product and a complex plane when it is not.**

**Theorem (the annihilator is the star of the central-carrying set).** For a nonzero $\tilde Q$ the
common annihilator is the star of the set of the $\tilde Z$ with $\tilde Q\tilde Z$ central,
$$
A_\diamond(\tilde Q)=\bigl\{\tilde Z^{*}:\tilde Q\tilde Z\in\mathbb{C}_{\mathbb{B}}\bigr\}.
$$
It is a **complex line** when $\tilde Q$ is invertible in the plain product and a **complex plane**
when it is not; off the cone and on the cone, respectively.

*Proof.* The element $\tilde R$ lies in $A_\diamond(\tilde Q)$ exactly when $\tilde Q\tilde R^{*}$
is central, that is exactly when $\tilde R^{*}$ satisfies
$\tilde Q(\tilde R^{*})\in\mathbb{C}_{\mathbb{B}}$; the star is a bijection, so the annihilator is
the star of the stated set. If $\tilde Q$ is invertible in the plain product, the equation
$\tilde Q\tilde Z=\lambda e_0$ has the single solution line $\tilde Z\in\mathbb{C}\tilde Q^{-1}$,
so the set is a complex line. If $\tilde Q$ is not invertible, it is a plain zero divisor, and
$\mathbb{B}\tilde Q$ is a minimal left ideal of complex dimension two, which contains no nonzero
central element because $e_0$ generates $\mathbb{B}$; hence $\tilde Q\tilde Z$ is central exactly
when $\tilde Q\tilde Z=0$, that is exactly when $\tilde Z$ lies in the kernel of the plain left
multiplication by $\tilde Q$, of complex dimension two.

**Example.** For the element $\tilde Q=e_0+2e_1+3e_2+4e_3$, of central square $1+4+9+16=30\neq0$,
the annihilator is the complex line
$$
A_\diamond(\tilde Q)=\mathbb{C}\tilde Q,
$$
and for the zero divisor $\tilde Q=e_1+ie_2$, of central square $1-1=0$, it is the complex plane
$$
A_\diamond(e_1+ie_2)=\mathbb{C}\{e_1-ie_2,\ e_0+ie_3\}.
$$

## The Multiplication Operator and the Rank

**The operator $L_{\tilde Q}$ has the annihilator $A_\diamond(\tilde Q)$ as its kernel, so it has complex rank three on the plain units, rank two on the nonzero plain zero divisors and rank zero at the origin.**

**Corollary (the rank).** The operator $L_{\tilde Q}$ has kernel $A_\diamond(\tilde Q)$, so as an
endomorphism of $\mathbb{B}$ it has complex rank three when $\tilde Q$ is a unit of the plain
product, rank two when it is a nonzero zero divisor, and rank zero at the origin.

*Proof.* The kernel is the annihilator by definition, of complex dimension one, two and four in
the three cases, and the rank is four minus the dimension.

## The Dichotomy

**The annihilator measures the parent invertibility: it is a complex line exactly for the elements invertible in the plain product and a complex plane exactly for the plain zero divisors**, and the block's zero-divisor set is the whole punctured space.

The zero-divisor set of the block is the whole punctured space, the punctured cone
$\{\tilde Q\neq0:C(\tilde Q)=0\}$ being the parent's, and the annihilator is the invariant that ties
the block to its parent: the annihilator measures the **parent invertibility**, because it is a line
exactly for the elements invertible in the plain product and a plane exactly for the plain zero
divisors. Every zero divisor of the block
exists, since the block is conjugate-alternating and never regular; what the annihilator separates
is not the zero-divisor class but the class of the parent. The block is the sibling of the
antisymmetric quaternionic sesqualgebra, which shares the line-or-plane dichotomy, and the sibling
of the general plain sesqualgebra, which has the plane but not the line.

## The Annihilator on the Remarkable Subspaces

**On each remarkable subspace the annihilator of a nonzero element is again a line or a plane, according to the parent invertibility, cut out by the same centrality equation**, the central elements annihilating the centre alone.

**The centre.** A nonzero central element $\tilde P=\lambda e_0$ has
$L_{\lambda e_0}\tilde X=\operatorname{Vect}(\lambda\tilde X^{*})$, whose kernel is the set of the
$\tilde X$ with vanishing vector part, that is the centre: the central elements annihilate the
centre alone.

**The vector subspace.** On the vector subspace the block is conjugate-alternating and its
annihilator of a nonzero pure element is a line or a plane according to the parent invertibility;
the plane case is exactly the isotropic cone of the plain product, and there the annihilator
contains the element in the degenerate direction.

**The conjugate-changed subspaces.** The star in the second slot exchanges an element and its
conjugate, so on the Hermitian subspace the annihilator of a nonzero element is again a line or a
plane, cut out by the same centrality equation; the anti-Hermitian subspace reads the conjugate
line.

## Summary

The annihilator of an element in a product is the set of partners the element kills, the left and
the right annihilator being the kernels of the left and the right multiplication. The antisymmetric
plain sesquimultiplication is conjugate-alternating, so the two annihilators of an element
coincide. The block measures the **parent invertibility**: for a nonzero element the common
annihilator is the star of the set of the $\tilde Z$ with $\tilde Q\tilde Z$ central, a complex
line when the element is a unit of the plain product and a complex plane when it is a plain zero
divisor. The operator has rank three on the units, two on the zero divisors and zero at the origin,
and the zero-divisor set of the block is the whole punctured space.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=\operatorname{Vect}(\tilde P\tilde Q^{*})$ | the antisymmetric plain sesquimultiplication, the operation $\mathrm{APS}$ |
| $A_\diamond(\tilde P),B_\diamond(\tilde P)$ | the left and the right annihilator, equal because the block is conjugate-alternating |
| $L_{\tilde P}$ | the left multiplication operator, $L_{\tilde P}\tilde X=\operatorname{Vect}(\tilde P\tilde X^{*})$ |
| $\{\tilde Z^{*}:\tilde P\tilde Z\in\mathbb{C}_{\mathbb{B}}\}$ | the common annihilator, the star of the central-carrying set |
| the complex line | the annihilator of an element invertible in the plain product |
| the complex plane | the annihilator of a plain zero divisor |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternioid-c-space.md`), §*The Zero Divisor and the Annihilator*, for the zero divisor and the annihilator of a general product.
- *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-sesqualgebra.md`), for the operation and its table.
- *Zero Divisors of the Antisymmetric Plain Sesqualgebra* (`articles_maths/zero-divisors-of-the-antisymmetric-plain-sesqualgebra.md`), above this article in this category, for the criterion and the two families.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-biquaternion-algebra.md`), the parent, for the invertibility and the rank-one matrix reading that the annihilator measures.
- *Annihilators of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/annihilators-of-the-antisymmetric-quaternionic-sesqualgebra.md`), the sibling with the same line-or-plane dichotomy.
- *Annihilators of the General Plain Sesqualgebra* (`articles_maths/annihilators-of-the-general-plain-sesqualgebra.md`), the sibling with the plane and the conjugate of the plain annihilator but no line.
