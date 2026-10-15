# __Square Roots of One and the Idempotents of the General Quaternionic Algebra__

## Introduction

This article classifies the square roots of the central value $+1$ in the general quaternionic bilinear
product, and then the **idempotents** of that product, the elements the same squaring map keeps on their
own square.

Both notions name a product, and throughout this article the product is the general quaternionic bilinear
product $\tilde p\star\tilde q=\tilde p^{\natural}\tilde q$ of the general quaternionic algebra, the
$\mathrm{GQA}$ of *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the square of the
article is the square of $\star$, and an unqualified *idempotent* is an idempotent of $\star$. The general
definition of the square and of the roots of a central value, and the general definition of an idempotent,
are *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, §*The Element Vocabulary*.

The whole problem is decided by one identity. The square of every element of this product is the central
element $N(\tilde p)e_0$, so the root equation of the value $\lambda$ reduces to the single real equation
$N(\tilde p)=\lambda$, and the idempotent equation collapses to a quadratic on the scalar line. The roots of
$+1$ are the level set $N=1$, the unit sphere $\mathrm{Sp}(1)$ of real dimension three; the idempotents are
as small as they can be, the two trivial ones $0$ and $e_0$.

**The results.** The roots of $+1$ in the general quaternionic product are the elements of the norm-one
level set $\mathrm{Sp}(1)$, the unit sphere of the quaternion algebra, of real dimension three; they contain
the central pair $\pm e_0$ and the pure unit vectors $\hat u$. The idempotents of the product are $0$ and
$e_0$ alone, and the product has no nontrivial idempotent. The two sets are not related by the halving map
that carries the roots of $+1$ onto the idempotents of the plain product: the map
$\tilde\xi\mapsto\tfrac12(e_0+\tilde\xi)$ produces an idempotent of $\star$ only at $\tilde\xi=\pm e_0$, and
every other root of $+1$ is sent out of the idempotent set. On the operator side the left multiplication
$L_{\tilde p}$ is a projector exactly when $\tilde p$ is an idempotent of the plain product, so over
$\mathbb{R}$ the only projectors of that form are the zero operator and the identity. Read on the two
remarkable subspaces, the idempotent equation leaves the two trivial idempotents in the centre and only $0$
in the vector subspace. The roots of $-1$ are empty, and they are quoted in one paragraph at the end of the
roots-of-one part and used nowhere below.

**Boundaries.** The product, the square and the algebraic norm are *Introduction to the General Quaternionic
Algebra of Quaternions* and *Norm and Invertibility in the General Quaternionic Algebra*; the general root
problem for an arbitrary radicand is *Square Roots of a General Element in the General Quaternionic
Algebra*; the roots of $0$ and the nilpotents of the product are *Square Roots of Zero and the Nilpotents of
the General Quaternionic Algebra*; the zero divisors are *Zero Divisors of the General Quaternionic
Algebra*; the idempotents of the plain product of the same space and the Hermitian idempotents of the
complex chapter are *Square Roots of One and the Idempotents of the General Plain Algebra*; the projectors
and the operator theory are *The Left Multiplications of the Quaternionic Product
and the Opposite Monoid* and *The Specificities of the General Quaternionic Algebra*; the structure-level
comparison of the six root sets is *Square Roots of a General Element in the Algebraic Structures over the
Quaternion $\mathbb{R}$ Space*, and that of the six idempotent sets is *Square Roots of One and the
Idempotents in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*.

**Conventions.** $\mathbb{H}$ is the real quaternion algebra with basis $e_0=1,e_1,e_2,e_3$, the rules
$e_k^2=-e_0$ and $e_1e_2=e_3$. Juxtaposition is the plain product and $\star$ the general quaternionic
bilinear product $\tilde p\star\tilde q=\tilde p^{\natural}\tilde q$, with the conjugation
$\tilde p^{\natural}=p_0-\vec p$ and $\tilde p=p_0e_0+\vec p$,
$\vec p=p_1e_1+p_2e_2+p_3e_3$. The **algebraic norm** is

$$
N(\tilde p)=\tilde p^{\natural}\tilde p=p_0^2+\lvert\vec p\rvert^2=\sum_{\mu=0}^{3}p_\mu^2 ,
$$

positive definite, with polar form $\beta(\tilde p,\tilde q)=p_0q_0+\vec p\cdot\vec q$. A **central
value** is an element $\lambda e_0$ with $\lambda\in\mathbb{R}$, and $\hat u$ denotes a real unit vector of
$\mathbb{R}^3$. The centre is the scalar line $\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$ and the vector subspace
is $\mathrm{Vect}(\mathbb{H})=\{\vec p\}$; the two are supplementary and orthogonal for the norm. A root
of a central value carries the lower-case xi $\tilde\xi$ of the quaternion layer, and an idempotent the
lower-case pi $\tilde\pi$.

## The Root Equation and Its Reduction

**Definition.** Let $\lambda\in\mathbb{R}$. A **square root of the central value $\lambda$** in the general
quaternionic product is an element $\tilde\xi$ with

$$
\tilde\xi\star\tilde\xi=\lambda e_0 .
$$

The root is relative to the product, and this article uses the one of $\star$ throughout; the general
definition of the square and of the roots of a central value is *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, §*The Element Vocabulary*.

**Theorem (the reduction).** For every $\tilde\xi\in\mathbb{H}$,

$$
\tilde\xi\star\tilde\xi=\lambda e_0 \iff N(\tilde\xi)=\lambda .
$$

**Proof.** The square is $N(\tilde\xi)e_0$ by *Norm and Invertibility in the General Quaternionic Algebra*,
and $e_0\neq0$.

**Corollary (the level set).** The roots of the central value $\lambda$ are the level set
$\{\tilde\xi:N(\tilde\xi)=\lambda\}$.

**Remark (no vector equation).** The reduction is a single real equation in the four coordinates, and it
holds for every $\lambda$ at once. The plain product reduces the same problem to the pair
$\xi_0^2-\lvert\vec\xi\rvert^2=\lambda$ and $2\xi_0\vec\xi=0$, whose second equation forces
$\xi_0=0$ or $\vec\xi=0$ (*Square Roots of One and the Idempotents of the General Plain Algebra*); the
quaternionic square is central for every element, so the second equation does not arise and the root set is
the level set itself. The general value is *Square Roots of a General Element in the General Quaternionic
Algebra*, and the value $0$ is *Square Roots of Zero and the Nilpotents of the General Quaternionic
Algebra*.

## The Roots of Plus One

**The roots of $+1$ are exactly the solutions of $N(\tilde\xi)=\xi_0^2+\lvert\vec\xi\rvert^2=1$, the
unit sphere $\mathrm{Sp}(1)$ of the quaternion algebra, of real dimension three, containing the central pair
$\pm e_0$ and the pure unit vectors $\hat u$.**

### Statement and Dimension

**Theorem.** The roots of $+1$ in the general quaternionic product are the solutions of

$$
N(\tilde\xi)=\xi_0^2+\lvert\vec\xi\rvert^2=1 ,
$$

the unit sphere $\mathrm{Sp}(1)$ of real dimension three. It contains the two central roots $\pm e_0$ and the
pure unit vectors $\hat u$.

**Proof.** The criterion is the reduction. The norm is positive definite and nondegenerate, and its level set
at the value $1$ is a nondegenerate quadric in the four real coordinates, of real dimension $4-1=3$. The
elements $\pm e_0$ have $N=1$; a pure unit vector $\hat u$ has $\xi_0=0$ and
$\lvert\vec\xi\rvert^2=1$, and satisfies the equation.

**Corollary (the count).** The root set of $+1$ is never a finite set; its cardinality is that of the
continuum, and the article states the count by dimension rather than by cardinality, as the corpus does.

### The Comparison with the Plain Product

The value $+1$ is read side by side with the plain product, and the exchange of the two signed values is the
whole of the difference.

| value $\lambda$ | quaternionic $\tilde\xi\star\tilde\xi$ | plain $\tilde\xi^2$ |
|---|---|---|
| $-1$ | no root | the pure elements with $\lvert\vec\xi\rvert=1$, of real dimension two |
| $+1$ | the norm-one level set $\mathrm{Sp}(1)$, of real dimension three | $\{\pm e_0\}$ alone |

**Proposition.** The two root sets of $-1$ are as different as they can be: the plain equation has a
two-dimensional family of roots, the pure elements of norm one, and the quaternionic equation has none. The
two root sets of $+1$ are exchanged in the same way: the plain equation has two roots, $\pm e_0$, and the
quaternionic equation has the whole three-dimensional unit sphere.

**Proof.** The plain square is $(\xi_0^2-\lvert\vec\xi\rvert^2)e_0+2\xi_0\vec\xi$; the equation
$\tilde\xi^2=\lambda e_0$ is the pair $\xi_0^2-\lvert\vec\xi\rvert^2=\lambda$,
$2\xi_0\vec\xi=0$. For $\lambda=-1$ the second equation forces a pure root, and then
$-\lvert\vec\xi\rvert^2=-1$ gives $\lvert\vec\xi\rvert=1$; for $\lambda=+1$ it forces
$\xi_0=0$, which gives $-\lvert\vec\xi\rvert^2=1$, impossible, or $\vec\xi=0$, which gives
$\xi_0=\pm1$. The quaternionic column is §*Statement and Dimension* and the emptiness at $-1$; the plain
column is *Square Roots of One and the Idempotents of the General Plain Algebra*.

**Remark (the roots of $+1$ and the units).** The quaternionic root set of $+1$ is exactly the norm-one
shell $N=1$, a subgroup of the group of units of the *plain* algebra; the units of the plain algebra are the
elements of nonzero norm, the shell is their norm-one stratum, and the two readings meet at the norm.

**The roots of $-1$.** The roots of $-1$ are empty, and this paragraph is all the article spends on them. A
multiplication by a central scalar $c$ rescales the square by $c^2$, because the product is
$\mathbb{R}$-bilinear and the scalar is central,

$$
(c\tilde\xi)\star(c\tilde\xi)=c^{2}\bigl(\tilde\xi\star\tilde\xi\bigr),
$$

so no central multiple turns a root of $+1$ into a root of $-1$: over $\mathbb{R}$ the centre is the field
$\mathbb{R}$, with no element of negative square and no central imaginary unit. The equation
$N(\tilde\xi)=-1$ has no solution at all, the norm being positive definite, so the root set of $-1$ is the
**empty set**. It is quoted here and used nowhere below.

## The Idempotents of the Product

**The idempotents of the general quaternionic product are $0$ and $e_0$ alone; the product has no nontrivial
idempotent.**

### Definition and the Square

**Definition.** Let $\star$ be a product on $\mathbb{H}$ and let $\tilde\pi\in\mathbb{H}$. The element
$\tilde\pi$ is **idempotent of $\star$** when $\tilde\pi\star\tilde\pi=\tilde\pi$; the **trivial
idempotents** are $0$ and the left unit $e_0$, and an idempotent different from both is **nontrivial**. The
definition is *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, §*The Element Vocabulary*, and it
names the product. Throughout this part the product is $\star$.

**Lemma (the square is central).** For every $\tilde p\in\mathbb{H}$,

$$
\tilde p\star\tilde p=\tilde p^{\natural}\tilde p=N(\tilde p)\,e_0 , \qquad
N(\tilde p)=p_0^2+p_1^2+p_2^2+p_3^2 .
$$

**Proof.** With $\tilde p=p_0e_0+\vec p$ the product has scalar part $p_0^2+\vec p\cdot\vec p$ and
vector part $p_0\vec p-p_0\vec p-\vec p\times\vec p=0$ at equal arguments; the square is
$N(\tilde p)e_0$ (*Introduction to the General Quaternionic Algebra of Quaternions*).

The lemma is the reason the idempotent equation is trivial here and nontrivial for the plain product. The
plain square of the same element is $p_0^2e_0+2p_0\vec p+\vec p^2$, whose vector part is not obliged
to vanish; the quaternionic square carries no vector part at all, and the equation is a quadratic in one real
variable.

### The Classification

**Theorem (idempotents).** The solutions of $\tilde\pi\star\tilde\pi=\tilde\pi$ are $\tilde\pi=0$ and
$\tilde\pi=e_0$; the general quaternionic product has no nontrivial idempotent.

**Proof.** By the lemma the left-hand side is $N(\tilde\pi)e_0$, an element of the centre
$\mathbb{R}_{\mathbb{H}}$, so an idempotent is central, $\tilde\pi=Ae_0$ with $A\in\mathbb{R}$. For a central
element the equation reads $A^2e_0=Ae_0$, that is $A^2=A$, or $A(A-1)=0$; the field $\mathbb{R}$ gives
$A\in\{0,1\}$. Both values satisfy the equation.

**Remark (the equation is weaker than centrality).** The single scalar equation $N(\tilde\pi)=\pi_0$ is not
idempotence; it must be read with centrality attached. Every pure element $\vec p\neq0$ has
$N(\vec p)=\lvert\vec p\rvert^2\neq0$ and is not central, so it fails the equation and is not an
idempotent; and the central element $-e_0$, of norm $1$, satisfies $N=1\neq\pi_0=-1$ and is not idempotent
either. The scalar equation alone does not decide idempotence.

### The Halving Map and the Roots of One

**The halving map $\tilde\xi\mapsto\tfrac12(e_0+\tilde\xi)$ carries the plain roots of $+1$ onto the plain
idempotents, but it is not a bijection of the roots of $+1$ of $\star$ onto the idempotents of $\star$: it
yields an idempotent of $\star$ only at $\tilde\xi=\pm e_0$.**

**Proposition (the plain halving map).** For the plain product the map
$\tilde\xi\mapsto\tfrac12(e_0+\tilde\xi)$ is a bijection of the plain roots of $+1$ onto the plain
idempotents, with inverse $\tilde\pi\mapsto2\tilde\pi-e_0$. Over $\mathbb{R}$ the plain roots of $+1$ are
$\pm e_0$ and the plain idempotents are $0$ and $e_0$, and the map is the pair
$\tilde\xi=e_0\mapsto\tilde\pi=e_0$ and $\tilde\xi=-e_0\mapsto\tilde\pi=0$ (*Square Roots of One and the
Idempotents of the General Plain Algebra*).

**Proof.** If $\tilde\xi\tilde\xi=e_0$ then
$\bigl(\tfrac12(e_0+\tilde\xi)\bigr)^2=\tfrac14(e_0+2\tilde\xi+e_0)=\tfrac12(e_0+\tilde\xi)$; conversely
from $\tilde\pi^2=\tilde\pi$ the element $\tilde\xi=2\tilde\pi-e_0$ has
$\tilde\xi^2=4\tilde\pi-4\tilde\pi+e_0=e_0$. The two maps are inverse to each other.

**Proposition (the map misses here).** Let $\tilde\xi$ be a root of $+1$ of $\star$ and put
$\tilde\pi=\tfrac12(e_0+\tilde\xi)$. Then

$$
\tilde\pi\star\tilde\pi-\tilde\pi=\tfrac14\bigl(\tilde\xi^{\natural}-\tilde\xi\bigr)=-\tfrac12\vec\xi ,
$$

so $\tilde\pi$ is an idempotent of $\star$ exactly when $\vec\xi=0$, that is exactly for
$\tilde\xi=\pm e_0$.

**Proof.** The product is $\mathbb{R}$-bilinear, so

$$
(e_0+\tilde\xi)\star(e_0+\tilde\xi)
= e_0\star e_0+e_0\star\tilde\xi+\tilde\xi\star e_0+\tilde\xi\star\tilde\xi
= e_0+\tilde\xi+\tilde\xi^{\natural}+N(\tilde\xi)e_0 ,
$$

and $N(\tilde\xi)=1$; dividing by four and subtracting $\tilde\pi=\tfrac12(e_0+\tilde\xi)$ leaves
$\tfrac14(\tilde\xi^{\natural}-\tilde\xi)$. Since $\tilde\xi^{\natural}-\tilde\xi=-2\vec\xi$, the
difference vanishes exactly when the vector part of $\tilde\xi$ does, and the roots of $+1$ with vanishing
vector part are $\pm e_0$.

The two propositions are the whole of the relation between the roots of one and the idempotents. The halving
map sends the two central roots onto $e_0$ and $0$, and every other root of the three-dimensional sphere out
of the idempotent set; the idempotents are read from the squaring map directly, in §*The Classification*.

**Remark (the absent complex correspondence).** In the complex chapter the plain idempotents are the
Hermitian family $\tfrac12(e_0+i\hat u)$ over the real unit vectors $\hat u$, and there the halving map is
a bijection of the plain roots of $+1$, the elements $i\hat u$ with $(i\hat u)^2=e_0$, onto them. Over
$\mathbb{R}$ the centre is the field $\mathbb{R}$ itself, with no central imaginary unit, so the imaginary
unit vectors do not exist, the Hermitian family has no real counterpart, and the map
$\tilde\pi\mapsto2\tilde\pi-e_0$ followed by the division by the central imaginary has no analogue
(*Square Roots of One and the Idempotents of the General Plain Algebra*, the plain chapter over
$\mathbb{C}$, for the Hermitian family).

### The Trivial Family and Orthogonality

**Definition.** Two idempotents $\tilde\pi,\tilde\rho$ are **orthogonal** when
$\tilde\pi\star\tilde\rho=0$; a family of pairwise orthogonal idempotents is **complete** when its members
sum to $e_0$.

**Proposition (the family).** The idempotent set is $\{0,e_0\}$; the two are orthogonal, the origin being
orthogonal to every element; there is no nontrivial idempotent and no pair of nontrivial orthogonal
idempotents. The only complete orthogonal family of nonzero idempotents is $\{e_0\}$.

**Proof.** The classification gives the set. For orthogonality, $0\star e_0=0$ and $0\star0=0$, while
$e_0\star e_0=e_0\neq0$; a nontrivial idempotent does not exist, so no pair of them can be orthogonal. A
complete family of nonzero orthogonal idempotents summing to $e_0$ is available only as $\{e_0\}$, since any
member other than $e_0$ would be a nontrivial idempotent, and $e_0$ cannot be split, $e_0$ being of norm one
and the only idempotent of norm one.

### Idempotents as Projections

**Theorem (the projector criterion).** The left multiplication
$L_{\tilde p}(\tilde x)=\tilde p\star\tilde x$ is a projector, $L_{\tilde p}^{2}=L_{\tilde p}$, if and only
if $\tilde p$ is an idempotent of the plain product. Over $\mathbb{R}$ the plain idempotents are $0$ and
$e_0$ alone, so the only projectors of the form $L_{\tilde p}$ are the zero operator and the identity.

**Proof.** $L_{\tilde p}=L^{\mathrm{plain}}_{\tilde p^{\natural}}$ by the isotope identity, and the plain
left multiplications are faithful; so $L_{\tilde p}^{2}=L_{\tilde p}$ exactly when
$(\tilde p^{\natural})^2=\tilde p^{\natural}$, that is when $\tilde p$ is a plain idempotent. The plain
idempotents are $0$ and $e_0$, and $L_{e_0}\tilde x=e_0^{\natural}\tilde x=\tilde x$ is the identity while
$L_0$ is zero. The theorem and the monoid law $L_{\tilde p}L_{\tilde q}=L_{\tilde q\tilde p}$ are *The Left
Multiplications of the Quaternionic Product and the Opposite Monoid*.

**Remark.** The complex sibling carries a two-parameter family of projectors, indexed by the plain
idempotents, whose elements are not idempotents of the product. Over $\mathbb{R}$ the indexing set is the
two-point set $\{0,e_0\}$, so the projector family is the trivial pair, and the displacement it records in
the complex block has no real content.

### The Idempotent Equation on the Remarkable Subspaces

**Proposition (the idempotent equation on the two subspaces).** On the centre the idempotents are $0$ and
$e_0$; on the vector subspace the only idempotent is $0$.

| subspace | element | $\tilde\pi\star\tilde\pi$ | idempotents |
|---|---|---|---|
| $\mathbb{R}_{\mathbb{H}}$, the centre | $Ae_0$ | $A^2e_0$ | $0$, $e_0$ |
| $\mathrm{Vect}(\mathbb{H})$, the vector subspace | $\vec p$ | $\lvert\vec p\rvert^2e_0$ | $0$ |

**Proof.** Each entry is the algebraic norm on the subspace of the same row, by the lemma. In the centre the
equation leaves $A^2=A$, hence $A\in\{0,1\}$. In the vector subspace a central element equals a vector only
at $0$; a nonzero pure element has square $\lvert\vec p\rvert^2e_0$, a nonzero central element, which
differs from the pure $\vec p$, so the origin alone is idempotent.

**Remark.** The centre carries the two trivial idempotents and the vector subspace only $0$; neither
remarkable subspace carries a nontrivial idempotent. Over $\mathbb{R}$ the quaternion algebra has exactly
these two distinguished subspaces and no third, the fixed and the anti-fixed space of the natural sign
(*Introduction to the Remarkable Subspaces of the Quaternions*); the Hermitian subspace of the complex
chapter, which carries the nontrivial Hermitian idempotents there, therefore has no real counterpart, and the
real idempotent set does not refine further.

### The Peirce Decomposition It Does Not Carry

A nonzero idempotent of an associative unital algebra carries the Peirce decomposition
$A=A_1\oplus A_{1/2}\oplus A_0$ with $A_\lambda=\{x:\Pi x=\lambda x\}$, and the decomposition is the source
of the minimal ideals and the matrix units. The construction uses associativity twice, in reading the two
maps as projections and in verifying that their images add.

For the general quaternionic product there is nothing to attach it to. The only nonzero idempotent is the
left unit $e_0$, and $L_{e_0}$ is the identity, so the only Peirce piece is the whole algebra. The
nontrivial decomposition, the frame of two orthogonal idempotents and its Peirce lines, is a property of the
plain algebra alone, and over $\mathbb{R}$ the plain algebra is a division algebra, whose only idempotents
are $0$ and $e_0$ and which carries no nontrivial frame either. What the product has in place of the
decomposition is the centrality of the square and the trivial projectors of §*Idempotents as Projections*.

### The Idempotents and the Nilpotents

**Theorem (disjoint classes).** No element of the block is both an idempotent and a nilpotent; the only
idempotent whose square vanishes is the origin.

**Proof.** The idempotents of $\star$ are $0$ and $e_0$, and the nilpotents are the nonzero square-zero
elements; the square-zero set of the block is the origin alone (*Square Roots of Zero and the Nilpotents of
the General Quaternionic Algebra*), so no nonzero idempotent is square-zero and the nilpotent class is
empty. Of the two idempotents, $e_0\star e_0=e_0\neq0$ and $0\star0=0$, so the origin is the only idempotent
whose square vanishes. The two classes meet in no element.

## Summary

In the general quaternionic bilinear product the square of every element is the central element
$N(\tilde p)e_0$, so the root equation of a central value reduces to the single real equation
$N(\tilde p)=\lambda$ and the idempotent equation forces centrality. The roots of $+1$ are the solutions of
$N=1$, the unit sphere $\mathrm{Sp}(1)$ of real dimension three; they contain the central pair $\pm e_0$ and
the pure unit vectors $\hat u$, and they are exactly the units of the plain algebra. The roots of $-1$ are
empty, because no central scalar can flip the sign of a square over $\mathbb{R}$ and the norm is definite;
they are quoted in one paragraph and used nowhere. The idempotents of the product are $0$ and $e_0$ alone,
and the product has no nontrivial idempotent; the two form a family of orthogonal idempotents whose only
complete nonzero subfamily is $\{e_0\}$. The halving map that carries the plain roots of $+1$ onto the plain
idempotents produces an idempotent of $\star$ only at $\pm e_0$, so the sphere of roots of one and the
two-point idempotent set do not correspond, and the Hermitian family of the complex chapter has no real
counterpart. On the operator side $L_{\tilde p}$ is a projector exactly when $\tilde p$ is a plain
idempotent, so over $\mathbb{R}$ the only projectors of the form $L_{\tilde p}$ are the zero operator and
the identity. Read on the two remarkable subspaces, the idempotent equation leaves the two trivial
idempotents in the centre and only $0$ in the vector subspace, no element is both an idempotent and a
nilpotent, and the origin is the only idempotent whose square vanishes.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde p\star\tilde q=\tilde p^{\natural}\tilde q$ | the general quaternionic bilinear product |
| $\tilde\xi$ | a root of a central value in the quaternion layer |
| $\{\tilde\xi:N(\tilde\xi)=\lambda\}$ | the root set of the central value $\lambda$ |
| $\mathrm{Sp}(1)=\{\tilde\xi:N(\tilde\xi)=1\}$ | the roots of $+1$, the unit sphere of real dimension three |
| $\varnothing$ | the root set of $-1$ |
| $\tilde\pi$ | an idempotent of the product; the nonzero ones are $e_0$ alone |
| $\tilde p\star\tilde p=N(\tilde p)e_0$ | the square, always central |
| $N(\tilde p)=\sum_\mu p_\mu^2$ | the quaternionic bilinear algebraic norm, positive definite |
| $\mathbb{R}_{\mathbb{H}},\mathrm{Vect}(\mathbb{H})$ | the centre and the vector subspace, carrying $0,e_0$ and $0$ |
| $L_{\tilde p}$ | the left multiplication, a projector iff $\tilde p$ is a plain idempotent |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the square roots of a central value in an algebra with a quadratic form, and for idempotents and square-zero elements in a non-associative algebra.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the sphere of square roots of $-1$ in the quaternion algebra and the division property.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the idempotent equation, the halving map and the Peirce decomposition in the absence of associativity.
- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the origin of the sphere of square roots of $-1$.
- *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternion-r-space.md`), §*The Element Vocabulary*, for the general definitions of the root of a central value, of an idempotent and of a projector.
- *Introduction to the General Quaternionic Algebra of Quaternions* (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-quaternions.md`), for the product, its table and its left unit.
- *Norm and Invertibility in the General Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-algebra-of-quaternions.md`), for the definite norm and the units.
- *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-general-quaternionic-algebra-of-quaternions.md`), for the roots of $0$, the empty square-zero set and the absence of nilpotents.
- *Square Roots of a General Element in the General Quaternionic Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-general-quaternionic-algebra-of-quaternions.md`), for the root problem of an arbitrary radicand.
- *Square Roots of One and the Idempotents of the General Plain Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-plain-algebra-of-quaternions.md`), for the plain classification of the same space and the halving map.
- *Introduction to the Remarkable Subspaces of the Quaternions* (`articles_maths/introduction-to-the-remarkable-subspaces-of-the-quaternions.md`), for the two distinguished subspaces of the real algebra and the absence of a third.
- *Zero Divisors of the General Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-algebra-of-quaternions.md`), for the empty zero-divisor set.
- *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* (`articles_maths/the-left-multiplications-of-the-quaternionic-product-and-the-opposite-monoid-of-quaternions.md`), for the monoid law and the projectors.
