# __Zero Divisors of the Antisymmetric Quaternionic Sesqualgebra__

## Introduction

A zero divisor of a product is a nonzero element that annihilates a nonzero element, on one side or
on the other, and the definition is relative to the product: the equation $\tilde Q\star\tilde R=0$
names the class, and the class changes with $\star$. For the conjugate cross product

$$
\tilde P\diamond\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural}\bigr)=\mathbf{P}\times\overline{\mathbf{Q}}
$$

of *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions* the equation is
decided by one vector criterion, the $\mathbb{C}$-linear dependence of two vector parts, and the
criterion is met by every nonzero element. The verdict is therefore the extreme one:

**the zero-divisor set of the block is the whole space with the origin removed.** Every nonzero
biquaternion is a two-sided zero divisor of the block, and no zero-divisor set of the twelve can be
larger: the four general products share the cone $\mathcal{C}$ of real dimension six, a proper part
of the block's set. The reason is the shape of the rule: the block reads the vector part of the
first argument and the conjugate of the vector part of the second, so that an element with a
nonzero vector part is annihilated by the conjugates of the elements parallel to it, and an element
of the centre annihilates everything on both sides.

The two families of the set are read apart, and the annihilators are not lines but planes. For a
non-central element the two annihilators coincide in one complex plane, spanned by the scalar and
by the conjugate of the vector part, of real dimension four, so that the equation
$\tilde A\diamond\tilde R=\tilde W$ has a solution exactly on one complex plane of values and the
solution is determined modulo a plane; for a central element both annihilators are the whole space.
The definition and the annihilators are *Definitions for the Study of the 12 Algebraic Structures*,
§*The Zero Divisor and the Annihilator*; the comparison with the four general products, whose
zero-divisor sets coincide with one another and are proper subsets of the space, is *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the annihilation pair of an element with
its conjugate is the operator content of *The Adjoint Operators of the Antisymmetric Quaternionic
Sesqualgebra*; and the cone of the diagonal, which is a proper part of the set, is *The Conjugate
Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra*.

**Conventions.** As in the block: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis
$e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$ and $e_k^2=-e_0$, a generic element $\tilde Q=Q_0e_0+\mathbf{Q}$
with $\mathbf{Q}=\sum_kQ_ke_k$, and the product $\diamond$ for the block. The bar is the
coefficientwise conjugation, on the element and on the vector part alike, so that
$\overline{\mathbf{Q}}$ is the vector whose coordinates are $\overline{Q_k}$. The two annihilators
of an element $\tilde A$ are written $A_\diamond(\tilde A)=\{\tilde R:\tilde A\diamond\tilde R=0\}$
and $B_\diamond(\tilde A)=\{\tilde R:\tilde R\diamond\tilde A=0\}$, the left and the right one.

## The Definition, Relative to a Product

**Definition (zero divisor and annihilator).** Let $\star$ be a product on $\mathbb{B}$ and let
$\tilde Q\in\mathbb{B}$. The element $\tilde Q$ is a **left zero divisor of $\star$** when
$\tilde Q\neq0$ and there is a nonzero $\tilde R$ with $\tilde Q\star\tilde R=0$; a **right zero
divisor** when $\tilde Q\neq0$ and there is a nonzero $\tilde R$ with $\tilde R\star\tilde Q=0$;
and a **zero divisor** when it is one or the other. It is a **two-sided zero divisor** when it is
both. The **left annihilator** and the **right annihilator** of a zero divisor are the sets

$$
A_\star(\tilde Q)=\{\tilde X:\tilde Q\star\tilde X=0\},\qquad B_\star(\tilde Q)=\{\tilde X:\tilde X\star\tilde Q=0\},
$$

and an element of a unital product that is neither a left nor a right zero divisor is **regular**.
Throughout this article the product is the block $\diamond$, so that, unqualified, a zero divisor
is a zero divisor of the block and an annihilator is an annihilator of the block.

Two points of the definition are used below and are worth stating with it. The origin is not a zero
divisor of any product, even though $0\star\tilde R=0$ for every $\tilde R$: both elements are
required to be nonzero. And the word regular is defined only in a unital product: for a product
without a unit the regularity of an element is not defined, and the block has no unit, so the
vocabulary of regularity is unavailable to it and the only reading of the element theory is the
pair of annihilators.

## The Criterion

**Theorem (every nonzero element is a two-sided zero divisor).** Let $\tilde A\neq0$ be a
biquaternion. Then $\tilde A\diamond\overline{\tilde A}=0$ and
$\overline{\tilde A}\diamond\tilde A=0$. Consequently every nonzero element of the block is a
two-sided zero divisor, and the zero-divisor set of the block is $\mathbb{B}\setminus\{0\}$.

*Proof.* For the first product,
$\tilde A\diamond\overline{\tilde A}=\mathbf{A}\times\overline{\overline{\mathbf{A}}}=\mathbf{A}\times\mathbf{A}=0$;
for the second,
$\overline{\tilde A}\diamond\tilde A=\overline{\mathbf{A}}\times\overline{\mathbf{A}}=0$. The two
products vanish for every element and not only for the zero divisors, so the definition is met by
every nonzero $\tilde A$ with the witness $\overline{\tilde A}$, which is nonzero together with
$\tilde A$.

**Remark (the two families).** The set splits by the vector part.

1. **The central family**, the elements $\tilde A=\lambda e_0$ with $\lambda\neq0$, whose vector
part is zero and for which the product vanishes against every second argument: such an element
annihilates the whole space on both sides, and it is a two-sided zero divisor of the most
degenerate kind, the witness being any nonzero element. 2. **The non-central family**, the elements
whose vector part is nonzero, for which the transfer $\tilde A\mapsto\overline{\tilde A}$ is an
involution without fixed elements outside the central line and pairs every element with a nonzero
annihilator on each side.

The two families are exhaustive, and the definition of the set is the union of the two; the second
is the space minus the centre and the first is the centre minus the origin.

**Remark (the criterion is the one of the diagonal).** Write the equation
$\tilde A\diamond\tilde R=0$ in coordinates: it reads $\mathbf{A}\times\overline{\mathbf{R}}=0$,
which holds exactly when $\mathbf{A}$ and $\overline{\mathbf{R}}$ are $\mathbb{C}$-linearly
dependent, that is exactly when the vector part of one element is a complex multiple of the
conjugate of the vector part of the other. The criterion for the annihilation of a pair is
therefore the criterion for the vanishing of the diagonal of *The Conjugate Cross Product and the
Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra*, read on two different elements, and
the annihilators of an element are the elements whose vector part is parallel to the conjugate of
its own. The zero-divisor set is thus the union over the elements of the cone of the diagonal, and
the cone of the square-zero elements is the part of it on which the two elements of the pair
coincide.

**Remark (no element is excluded and no element is privileged).** In the four general products the
zero divisors are the elements with vanishing central square, so that the set is a proper part of
the space and the generic element is regular; in the block the set is everything and the word
regular has no referent. The contrast is not a defect of the definition: it is the statement that
the block has no invertible element either, so that the element theory of the block has no division
at all and every multiplication by a fixed element loses information, in the sense that the
annihilator of the element is a nonzero subspace. The loss is quantified in the next section.

## The Annihilators

The annihilator of an element is the kernel of the left or the right multiplication, the two
coinciding because the block is conjugate-alternating; for a non-central element it is the plane
spanned by the centre and the conjugate of the vector part, and for a central element it is the
whole space. The annihilators, the operator and the rank are the companion article *Annihilators of
the Antisymmetric Quaternionic Sesqualgebra*, below this article in this category.

## The Comparison with the Other Products

**The four general products.** The zero-divisor set of each of the four general products is the
same set,

$$
\{\tilde Q\neq0:\ C(\tilde Q)=0\},\qquad C(\tilde Q)=\sum_\mu Q_\mu^{2},
$$

a set of real dimension six in the eight dimensional space, and the coincidence of the four sets is
a theorem of the corpus, *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Four General Products Coincide*.
The comparison with the block is therefore a comparison of two sets on the same space, and the
block's set contains the general one strictly: the elements of the general set are zero divisors of
the block, and so is every other nonzero element, including the unit $e_0$ and the whole of the
vector subspace of real directions, which have a nonzero central square and are regular in the
general products.

**The annihilators separate where the sets coincide.** The annihilators of the four general
products are complex planes of complex dimension two, the kernels of a rank-one matrix, and they
depend on the product: the four pairs are related by the two conjugations, and the two sides
coincide for the natural and the general plain sesquilinear products and differ for the plain and
the general quaternionic sesquilinear ones, as *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* proves. The
annihilators of the block are complex planes of complex dimension two as well, for every
non-central element, and the whole space for the central ones, so the dimension does not separate
the block from the four general products; what separates them is the set, the cone of the four
against the whole space of the block, and the shape of the plane, the kernel of a rank-one matrix
for the four and the plane spanned by the centre and the conjugate of the vector part for the
block. The comparison, product by product and annihilator by annihilator, is *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and *Annihilators in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the reading for the block is the one above.

| product | the zero-divisor set | the annihilator of a non-degenerate zero divisor |
|---|---|---|
| $\tilde P\tilde Q$, $\tilde P^{\natural}\tilde Q$, $\tilde P\tilde Q^{*}$, $\tilde P^{\natural}\tilde Q^{*}$ | $\{\tilde Q\neq0:C(\tilde Q)=0\}$, one and the same set for the four | a complex plane of complex dimension two, the kernel of a rank-one matrix |
| the block $\mathbf{P}\times\overline{\mathbf{Q}}$ | the whole space with the origin removed | a complex plane of complex dimension two, $\mathbb{C}e_0\oplus\mathbb{C}\overline{\mathbf{A}}$ |

**Remark (the remarkable subspaces).** The zero-divisor set of the block is the complement of the
origin, so it meets every nonzero subspace of the space in the whole of that subspace with the
origin removed; the centre is entirely in it, the vector subspace is entirely in it, and no
subspace of the block is free of zero divisors except the origin itself. The subspace-by-subspace
reading, with the behaviour of the block on each, is *Remarkable Subspaces under the Antisymmetric
Quaternionic Sesqualgebra of Biquaternions*.

## The Relation to the Square-Zero Elements and to the Idempotents

**The cone of the diagonal is a proper part of the set.** The elements whose square vanishes are
those whose vector part is a complex multiple of a real vector, a cone of real dimension six, and
they are a strict part of the zero-divisor set: the element $e_1+ie_2$ has a non-vanishing square,
$-2ie_3$, and is a zero divisor, its conjugate annihilating it on both sides. The two sets are read
on the same criterion, the vector part, and they are different parts of the space: the square-zero
elements are the pairs of an element with itself, and the zero divisors are the pairs of an element
with its conjugate, so that the cone is the diagonal of the set and the set is the closure of the
cone under the transfer of the conjugate.

**The idempotents are outside the set only at the origin.** The idempotent set of the block is the
origin alone, as *Idempotents of the Antisymmetric Quaternionic Sesqualgebra* proves, and the
origin is excluded from the zero-divisor set by the definition. The block therefore carries no
idempotent that is a zero divisor and no zero divisor that is an idempotent: the two classes meet
nowhere, and the whole of the element theory of the block is concentrated on the side of the
nilpotents and the zero divisors. This is the extreme form of the separation of the two classes,
and it is the element-theoretic statement of the absence of a projector in the block.

**The two classes of nilpotents sit inside the set.** The nilpotents of the block are the
square-zero elements and the elements of index four, as *Nilpotents of the Antisymmetric
Quaternionic Sesqualgebra* shows, and both classes are parts of the zero-divisor set, the second
being the isotropic cone of the vector subspace lifted over a free scalar coordinate. The
zero-divisor set is thus the largest of the three element-theoretic sets of the block, containing
the two nilpotent classes and excluding only the origin, and the three sets are read on the same
two quadratic data of the vector part.

## Summary

Every nonzero element of the block is a two-sided zero divisor, and the zero-divisor set of the
block is therefore the whole space with the origin removed: no zero-divisor set of the twelve can
be larger, and the four general products, whose sets coincide with the vanishing of the central
square, are proper subsets of it. The set splits into the central family, whose elements annihilate
the whole space, and the non-central family, whose elements are paired with their conjugates by a
mutual annihilation. The two annihilators of a non-central element coincide, and the common
annihilator is a complex plane of real dimension four, the central line together with the line of
the conjugate of the vector part. The annihilators of a central element are the whole space. The
left multiplication by a non-central element has that plane as its kernel and the plane of the
values orthogonal to the vector part in the complex bilinear dot as its image, so that the equation
$\tilde A\diamond\tilde R=\tilde W$ is solvable exactly on that plane and the block carries a
relative inverse of dimension two in place of an inverse. The cone of the square-zero elements is a
proper part of the set, the origin is outside it, and no idempotent of the block is a zero divisor.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde A\diamond\tilde R=0$ | the annihilation on the left, reading $\mathbf{A}\times\overline{\mathbf{R}}=0$ |
| $\tilde R\diamond\tilde A=0$ | the annihilation on the right, reading $\mathbf{R}\times\overline{\mathbf{A}}=0$ |
| $\mathbb{B}\setminus\{0\}$ | the zero-divisor set of the block |
| $\overline{\tilde A}$ | the annihilator-witness of $\tilde A$, on both sides |
| $A_\diamond(\tilde A)=B_\diamond(\tilde A)=\mathbb{C}e_0\oplus\mathbb{C}\overline{\mathbf{A}}$ | the common annihilator of a non-central element |
| $(\mathbf{W},\mathbf{A})=0$ | the image of the left multiplication by $\tilde A$ |
| $\{\tilde Q\neq0:C(\tilde Q)=0\}$ | the zero-divisor set of the four general products |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures*, §*The Zero Divisor and the Annihilator*, for the left, right and two-sided zero divisor, the annihilators, the regular element and the product-relative reading.
- *Zero Divisors of the General Plain Algebra*, for the model block, where the zero divisors are the elements of vanishing central square.
- *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, for the four sets, their coincidence and the one-sided inverse equations.
- *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, for the annihilators of the four general products and their comparison.
- *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra*, for the cone of the diagonal, which is the self-annihilation part of the set.
- *Nilpotents of the Antisymmetric Quaternionic Sesqualgebra* and *Idempotents of the Antisymmetric Quaternionic Sesqualgebra*, for the two classes that sit inside and outside the set.
- *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*, for the left multiplication, its kernel and its image.
- *Annihilators of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/annihilators-of-the-antisymmetric-quaternionic-sesqualgebra.md`), below this article in this category, the companion article, for the annihilator of a non-central element and the rank
