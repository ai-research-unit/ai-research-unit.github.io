# __Idempotents of the General Quaternionic Algebra__

## Introduction

This article classifies the **idempotents** of the quaternion algebra $\mathbb{H}$ read through the
general quaternionic bilinear product, and it is the real member of the general quaternionic family
whose complex sibling is *Idempotents of the General Quaternionic Algebra*.

An idempotent is relative to a product, and the definition is stated once in *Definitions for the
Study of the 6 Algebraic Structures*, §*The Element Vocabulary*; throughout this article the product
is the general quaternionic product $\tilde p\star\tilde q=\tilde p^{\natural}\tilde q$, and the
unqualified "idempotent" means an idempotent of it. The article rests on one computation: the
quaternionic square of every element is the central element $N(\tilde p)e_0$, so an idempotent is
central and the idempotent equation collapses to $A^2=A$ on the scalar line. The answer is as small
as it could be: **the idempotents of the product are $0$ and $e_0$ alone**, and the product has no
nontrivial idempotent.

The companion article of the complex chapter, *Idempotents of the General Quaternionic Algebra*, gives
the same answer, $0$ and $e_0$; the contrast is with the plain product, whose complex idempotents
are the **Hermitian idempotents** $\tfrac12(e_0+i\hat\mu)$ over the real unit vectors $\hat\mu$, a
family of complex dimension two lying on the zero-divisor cone, and the general quaternionic product
displaces each of them into a **square-zero** element (*Idempotents of the General Plain Algebra*).
Over $\mathbb{R}$ neither the family nor the cone exists: there is no central imaginary unit to build
the Hermitian idempotents, and the definite norm leaves no isotropic direction, so the plain
idempotents collapse to the same two trivial points as the idempotents of the general quaternionic
product. The article gives the classification, names the absent correspondence with the roots of
$+e_0$, reads the idempotents as projectors on the operator side, and records the collapse on the
remarkable subspaces.

**Boundaries.** The idempotents of the plain product and the Hermitian idempotents of the complex
chapter are *Idempotents of the General Plain Algebra*; the square, the norm and the isotope reading
are *Introduction to the General Quaternionic Algebra of Quaternions* and *Norm and Invertibility in
the General Quaternionic Algebra*; the roots of the three central values are *Square Roots of Minus
One, Zero and Plus One in the General Quaternionic Algebra*; the zero divisors are *Zero Divisors of
the General Quaternionic Algebra*, above this article in this category, and the nilpotents are
*Nilpotents of the General Quaternionic Algebra*, below it; the structure-level comparison of the six
idempotent sets is *Idempotents in the 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the projectors and the operator theory are *The Left
Multiplications of the Quaternionic Product and the Opposite Monoid* and *The Specificities of the
General Quaternionic Algebra*, both below this article in this category; and the complex sibling is
*Idempotents of the General Quaternionic Algebra*.

## Conventions

$\mathbb{H}$ is the real quaternion algebra with basis $e_0=1,e_1,e_2,e_3$, the rules
$e_k^2=-e_0$ and $e_1e_2=e_3$. Over $\mathbb{R}$ the coefficientwise conjugation is the identity and
the Hermitian star coincides with the natural conjugation, so the block carries the single
involution

$$
\tilde p^{\natural}=p_0-\mathbf p,\qquad \tilde p=p_0e_0+\mathbf p,\quad
\mathbf p=p_1e_1+p_2e_2+p_3e_3 .
$$

Juxtaposition is the plain product and $\star$ is the general quaternionic bilinear product
$\tilde p\star\tilde q=\tilde p^{\natural}\tilde q$. The **algebraic norm** is

$$
N(\tilde p)=\tilde p^{\natural}\tilde p=p_0^2+|\mathbf p|^2=\sum_{\mu=0}^{3}p_\mu^2 ,
$$

positive definite, with polar form $\beta(\tilde p,\tilde q)=p_0q_0+\mathbf p\cdot\mathbf q$. The
centre is the scalar line $\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$ and the vector subspace is
$\mathrm{Vect}(\mathbb{H})=\{\mathbf p\}$; the two are supplementary and orthogonal for the norm.

## Definition, and the Square

**Definition.** Let $\star$ be a product on $\mathbb{H}$ and let $\tilde\pi\in\mathbb{H}$. The element
$\tilde\pi$ is **idempotent of $\star$** when $\tilde\pi\star\tilde\pi=\tilde\pi$; the **trivial
idempotents** are $0$ and the left unit $e_0$, and an idempotent different from both is
**nontrivial**. The definition is *Definitions for the Study of the 6 Algebraic Structures*,
§*The Element Vocabulary*, and it names the product.

**Lemma (the square is central).** For every $\tilde p\in\mathbb{H}$,

$$
\tilde p\star\tilde p=\tilde p^{\natural}\tilde p=N(\tilde p)\,e_0 , \qquad
N(\tilde p)=p_0^2+p_1^2+p_2^2+p_3^2 .
$$

**Proof.** With $\tilde p=p_0e_0+\mathbf p$ the product has scalar part $p_0^2+\mathbf p\cdot\mathbf p$
and vector part $p_0\mathbf p-p_0\mathbf p-\mathbf p\times\mathbf p=0$ at equal arguments; the square
is $N(\tilde p)e_0$ (*Introduction to the General Quaternionic Algebra of Quaternions*, and *Square
Roots of Minus One, Zero and Plus One in the General Quaternionic Algebra*, §*The Reduction of the
Equation*).

The lemma is the reason the idempotent equation is trivial here and nontrivial for the plain product.
The plain square of the same element is $p_0^2e_0+2p_0\mathbf p+\mathbf p^2$, whose vector part is not
obliged to vanish; the quaternionic square carries no vector part at all, and the equation is a
quadratic in one real variable.

## The Classification

**Theorem (idempotents).** The solutions of $\tilde\pi\star\tilde\pi=\tilde\pi$ are $\tilde\pi=0$ and
$\tilde\pi=e_0$; the general quaternionic product has no nontrivial idempotent.

**Proof.** By the lemma the left-hand side is $N(\tilde\pi)e_0$, an element of the centre
$\mathbb{R}_{\mathbb{H}}$, so an idempotent is central, $\tilde\pi=Ae_0$ with $A\in\mathbb{R}$. For a
central element the equation reads $A^2e_0=Ae_0$, that is $A^2=A$, or $A(A-1)=0$; the field
$\mathbb{R}$ gives $A\in\{0,1\}$. Both values satisfy the equation.

Equivalently, in coordinates: the equality
$|p|^2e_0=p_0e_0+\mathbf p$ of the lemma forces the vector part $\mathbf p$ to vanish and the scalar
equation $|p|^2=p_0$ to hold; with $\mathbf p=0$ this is $p_0^2=p_0$, whose roots are $0$ and $1$.

**Remark (the equation is weaker than centrality).** The single scalar equation $N(\tilde\pi)=\pi_0$
is not idempotence; it must be read with centrality attached. Every **pure** element $\mathbf p$ with
$\mathbf p\neq0$ has $N(\mathbf p)=|\mathbf p|^2\neq0$ and is not central, so it fails the equation
and is not an idempotent; and the central element $-e_0$, of norm $1$, satisfies $N=1\neq\pi_0=-1$ and
is not idempotent either. The scalar equation alone does not decide idempotence.

## The Idempotents and the Roots of Plus One

The idempotent equation and the equation of the square roots of a central value are two different
equations on the same square, and over $\mathbb{R}$ their solution sets do not match.

**Proposition (the roots of $+e_0$).** The roots of $+e_0$ are the elements of the norm-one level
set,
$$
\{\tilde\xi:\tilde\xi\star\tilde\xi=e_0\}=\{\tilde\xi:N(\tilde\xi)=1\} ,
$$
the unit sphere $\mathrm{Sp}(1)$ of the quaternion algebra, of real dimension three; every root of
$+e_0$ is a unit of norm one, with the two-sided inverse $\zeta(\tilde\xi)=\tilde\xi$. The statement
is *Square Roots of Minus One, Zero and Plus One in the General Quaternionic Algebra*,
§*The Three Root Sets*.

**Theorem (only $e_0$ is both).** Among the roots of $+e_0$ the only idempotent is $e_0$.

**Proof.** An idempotent of the block is $0$ or $e_0$; $0$ has norm $0$ and is not a root of $+e_0$,
while $e_0$ has norm $1$ and is. Hence the intersection of the idempotent set $\{0,e_0\}$ with the
norm-one sphere is the single point $e_0$.

**Corollary (no bijection).** The idempotents of the block and the roots of $+e_0$ do **not**
correspond: the root set is the three-dimensional sphere $\mathrm{Sp}(1)$ and the idempotent set is
the two-point set $\{0,e_0\}$, and the two have neither the same cardinality nor the same dimension.
The bijection that the plain algebra of the complex chapter carries, from the roots of $-1$ to the
idempotents by $\tilde\xi\mapsto\tfrac12(e_0+\tilde\xi i)$ with inverse
$\tilde\Pi\mapsto(2\tilde\Pi-e_0)/i$, has no analogue here. The inverse map is affine, $\tilde\Pi\mapsto
2\tilde\Pi-e_0$, followed by the division by the central imaginary unit $i$; over $\mathbb{R}$ the
centre is the field $\mathbb{R}$ itself, with no root of $-1$ and no central imaginary unit, and the
block has no two-sided unit on which to build the correspondence, so the map cannot be completed and
the correspondence has no analogue. The Hermitian family
itself, $\tfrac12(e_0+i\hat\mu)$ over the real unit vectors $\hat\mu$, has no real counterpart, and
its members are square-zero rather than idempotent for the general quaternionic product even after
the central unit $i$ is adjoined (*Idempotents of the General Plain Algebra*, the complex chapter,
for the Hermitian family and its displacement).

## The Trivial Family and Orthogonality

The idempotents are $0$ and $e_0$, and the two form the whole family.

**Definition.** Two idempotents $\tilde\pi,\tilde\rho$ are **orthogonal** when $\tilde\pi\star\tilde\rho=0$;
a family of pairwise orthogonal idempotents is **complete** when its members sum to $e_0$.

**Proposition (the family).** The idempotent set is $\{0,e_0\}$; the two are orthogonal, the origin
being orthogonal to every element; there is no nontrivial idempotent and no pair of nontrivial
orthogonal idempotents. The only complete orthogonal family of nonzero idempotents is $\{e_0\}$.

**Proof.** The classification gives the set. For orthogonality, $0\star e_0=0$ and $0\star0=0$, while
$e_0\star e_0=e_0\neq0$; a nontrivial idempotent does not exist, so no pair of them can be
orthogonal. A complete family of nonzero orthogonal idempotents summing to $e_0$ is available only as
$\{e_0\}$, since any member other than $e_0$ would be a nontrivial idempotent, and $e_0$ cannot be
split, $e_0$ being of norm one and the only idempotent of norm one.

## The Idempotents as Projections

On the operator side the idempotents of the plain algebra recover their usual role, with the index
conjugated, and over $\mathbb{R}$ the family is as small as the element family.

**Theorem (the projector criterion).** The left multiplication
$L_{\tilde p}(\tilde x)=\tilde p\star\tilde x$ is a projector, $L_{\tilde p}^{2}=L_{\tilde p}$, if and
only if $\tilde p$ is an idempotent of the plain product. Over $\mathbb{R}$ the plain idempotents are
$0$ and $e_0$ alone, so the only projectors of the form $L_{\tilde p}$ are the zero operator and the
identity.

**Proof.** $L_{\tilde p}=L^{\mathrm{plain}}_{\tilde p^{\natural}}$ by the isotope identity, and the
plain left multiplications are faithful; so $L_{\tilde p}^{2}=L_{\tilde p}$ exactly when
$(\tilde p^{\natural})^2=\tilde p^{\natural}$, that is when $\tilde p^{\natural}$, equivalently
$\tilde p$, is a plain idempotent. The plain idempotents are $0$ and $e_0$, and
$L_{e_0}\tilde x=e_0^{\natural}\tilde x=\tilde x$ is the identity while $L_0$ is zero. The
theorem and the monoid law $L_{\tilde p}L_{\tilde q}=L_{\tilde q\tilde p}$ are *The Left
Multiplications of the Quaternionic Product and the Opposite Monoid*.

**Remark.** The complex sibling carries a two-parameter family of projectors, indexed by the plain
idempotents, whose elements are not idempotents of the product. Over $\mathbb{R}$ the indexing set is
the two-point set $\{0,e_0\}$, so the projector family is the trivial pair, and the displacement it
records in the complex block has no real content.

## The Idempotents on the Remarkable Subspaces

Since the square is always central, the equation $\tilde\pi\star\tilde\pi=\tilde\pi$ can hold inside a
subspace only when the subspace contains the two trivial idempotents; reading it on the two
remarkable subspaces records which ones do.

**Proposition (the idempotent equation on the two subspaces).** On the centre the idempotents are
$0$ and $e_0$; on the vector subspace the only idempotent is $0$.

| subspace | element | $\tilde\pi\star\tilde\pi$ | idempotents |
|---|---|---|---|
| $\mathbb{R}_{\mathbb{H}}$, the centre | $Ae_0$ | $A^2e_0$ | $0$, $e_0$ |
| $\mathrm{Vect}(\mathbb{H})$, the vector subspace | $\mathbf p$ | $\lvert\mathbf p\rvert^2e_0$ | $0$ |

**Proof.** Each entry is the algebraic norm on the subspace of the same row, by the lemma. In the
centre the equation leaves $A^2=A$, hence $A\in\{0,1\}$. In the vector subspace a central element
equals a vector only at $0$; a nonzero pure element has square $|\mathbf p|^2e_0$, a nonzero central
element, which differs from the pure $\mathbf p$, so the origin alone is idempotent.

**Remark.** The centre carries the two trivial idempotents and the vector subspace only $0$; neither
remarkable subspace carries a nontrivial idempotent. The reading is the collapse of the complex table,
which has six subspaces and carries the Hermitian idempotents in the Hermitian subspace; over
$\mathbb{R}$ there is no Hermitian subspace, the two complex subspaces that would carry them having
no real trace with a nontrivial idempotent.

## The Peirce Decomposition It Does Not Carry

A nonzero idempotent of an associative unital algebra carries the Peirce decomposition
$A=A_1\oplus A_{1/2}\oplus A_0$ with $A_\lambda=\{x:\Pi x=\lambda x\}$, and the decomposition is the
source of the minimal ideals and the matrix units. The construction uses associativity twice, in
reading the two maps as projections and in verifying that their images add.

For the general quaternionic product there is nothing to attach it to. The only nonzero idempotent is
the left unit $e_0$, and $L_{e_0}$ is the identity, so the only Peirce piece is the whole algebra. The
nontrivial decomposition, the frame of two orthogonal idempotents and its Peirce lines, is a property
of the plain algebra alone, and over $\mathbb{R}$ the plain algebra is a division algebra, whose only
idempotents are $0$ and $e_0$ and which carries no nontrivial frame either. What the product has in
place of the decomposition is the centrality of the square and the trivial projectors of
§*The Idempotents as Projections*.

## The Idempotents and the Nilpotents

The two classes the idempotent equation and the square-zero equation select are disjoint.

**Theorem (disjoint classes).** No element of the block is both an idempotent and a nilpotent; the
only idempotent whose square vanishes is the origin.

**Proof.** The idempotents of $\star$ are $0$ and $e_0$, and the nilpotents are the nonzero
square-zero elements; the square-zero set of the block is the origin alone (*Nilpotents of the
General Quaternionic Algebra*, below this article in this category), so no nonzero idempotent is
square-zero and the nilpotent class is empty. Of the two idempotents, $e_0\star e_0=e_0\neq0$ and
$0\star0=0$, so the origin is the only idempotent whose square vanishes. The two classes meet in no
element.

## Summary

In the general quaternionic bilinear product the square of every element is the central element
$N(\tilde p)e_0$, so the idempotent equation forces centrality and reduces to $A^2=A$ on the scalar
line. The idempotents of the product are $0$ and $e_0$ alone, and the product has no nontrivial
idempotent; the two form a family of orthogonal idempotents whose only complete nonzero subfamily is
$\{e_0\}$. The complex chapter's two-parameter family of Hermitian idempotents has no real
counterpart: there is no central imaginary unit to build it and no isotropic cone to carry it, and
the idempotents and the roots of $+e_0$, the three-dimensional sphere $\mathrm{Sp}(1)$, do not
correspond, the affine map $\tilde\Pi\mapsto2\tilde\Pi-e_0$ of the complex plain block being
unavailable. On the operator side $L_{\tilde p}$ is a projector exactly when $\tilde p$ is a plain
idempotent, so over $\mathbb{R}$ the only projectors of the form $L_{\tilde p}$ are the zero operator
and the identity. Read on the two remarkable subspaces, the idempotent equation leaves the two
trivial idempotents in the centre and only $0$ in the vector subspace, no element is both an
idempotent and a nilpotent, and the origin is the only idempotent whose square vanishes.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde p\star\tilde q=\tilde p^{\natural}\tilde q$ | the general quaternionic bilinear product |
| $\tilde\pi$ | an idempotent of the product; the nonzero ones are $e_0$ alone |
| $\tilde p\star\tilde p=N(\tilde p)e_0$ | the square, always central |
| $N(\tilde p)=\sum_\mu p_\mu^2$ | the quaternionic bilinear algebraic norm, positive definite |
| $\mathrm{Sp}(1)=\{\tilde\xi:N(\tilde\xi)=1\}$ | the roots of $+e_0$, the unit sphere of real dimension three |
| $\mathbb{R}_{\mathbb{H}},\mathrm{Vect}(\mathbb{H})$ | the centre and the vector subspace, carrying $0,e_0$ and $0$ |
| $L_{\tilde p}$ | the left multiplication, a projector iff $\tilde p$ is a plain idempotent |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for idempotents and square-zero elements in a non-associative algebra.
- *Definitions for the Study of the 6 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-6-algebraic-structures.md`), §*The Element Vocabulary*, for the general definition of an idempotent and of a projector.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the idempotent equation and the Peirce decomposition in the absence of associativity.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the idempotents of the quaternion algebra and the division property.
- *Introduction to the General Quaternionic Algebra of Quaternions* (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-quaternions.md`), for the product, its table and its conjugation.
- *Norm and Invertibility in the General Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-algebra-of-quaternions.md`), for the definite norm and the one-sided equations.
- *Square Roots of Minus One, Zero and Plus One in the General Quaternionic Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-quaternionic-algebra-of-quaternions.md`), for the roots of the three central values and the norm-one sphere.
- *Zero Divisors of the General Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-algebra-of-quaternions.md`) and *Nilpotents of the General Quaternionic Algebra* (`articles_maths/nilpotents-of-the-general-quaternionic-algebra-of-quaternions.md`), for the empty zero-divisor set and the square-zero elements.
- *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* (`articles_maths/the-left-multiplications-of-the-quaternionic-product-and-the-opposite-monoid-of-quaternions.md`), for the monoid law and the projectors.
- *Idempotents of the General Quaternionic Algebra* (`articles_maths/idempotents-of-the-general-quaternionic-algebra.md`), the complex sibling, whose Hermitian family the passage to $\mathbb{R}$ removes.
