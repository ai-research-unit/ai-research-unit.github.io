# __Zero Divisors of the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra of $\mathbb{H}$ carries the Jordan product
$\tilde p\bullet\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$ of *Introduction to the
Symmetric Plain Algebra of Quaternions*. Unlike the plain algebra, which is a division algebra, the
block has zero divisors: the product of two nonzero elements can vanish. This article determines
them.

**This is not the algebra $\mathbb{H}$.** The two algebras share the space, the addition, the real
scalars and the unit, but $\bullet$ is a different multiplication and the projection onto the
scalar line is not multiplicative. Throughout, the natural sign ${}^{\natural}$ is the quaternion
conjugation, the bar is the identity because $\mathbb{R}$ has no nontrivial involution, and the
star coincides with the natural sign and gives nothing new.

The invertibility criterion is *Norm and Invertibility in the Symmetric Plain Algebra*, where the
contrast between invertibility and division is stated; the multiplication operators, of which the
zero divisors are exactly the singular ones with nonzero parameter, are *The Multiplication
Operators of the Symmetric Plain Algebra*, below this article in this category.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$ and
$e_1^2=e_2^2=e_3^2=-e_0$. A generic element is $\tilde q=q_0e_0+\vec q$ with
$\vec q=\sum_{k=1}^{3}q_ke_k$ and $q_\mu\in\mathbb{R}$; $\vec p\cdot\vec q$ is the
Euclidean dot product and $\vec p\times\vec q$ the vector product of the vector parts; the
norm is $N(\tilde q)=\tilde q\tilde q^{\natural}=q_0^2+|\vec q|^2$ and the scalar line and the
vector subspace $\mathrm{Vect}(\mathbb{H})=\operatorname{Im}\mathbb{H}$ are those of *Introduction
to the Remarkable Subspaces of the Quaternions*.

## The Zero Divisors of the Block

### The Definition

**Definition.** A nonzero element $\tilde p$ is a **zero divisor** of the block when there is a
nonzero element $\tilde q$ with

$$
\tilde p\bullet\tilde q=0 .
$$

Since the product is commutative, the left and the right zero divisors are the same, and the
element $\tilde q$ is a **partner** of $\tilde p$.

### The Criterion

**Theorem (criterion).** A nonzero element is a zero divisor if and only if it is **pure**:

$$
\tilde p\ \text{is a zero divisor}\iff p_0=0\iff \tilde p\in\mathrm{Vect}(\mathbb{H})\setminus\{0\} .
$$

*Proof.* Write $\tilde p=p_0e_0+\vec p$ and $\tilde q=q_0e_0+\vec q$, so that

$$
\tilde p\bullet\tilde q=\bigl(p_0q_0-\vec p\cdot\vec q\bigr)e_0+p_0\vec q+q_0\vec p .
$$

If $p_0=0$ and $\tilde p\neq0$, choose a nonzero pure $\vec v$ with $\vec v\perp\vec p$
and $\tilde q=\vec v$; then $\tilde p\bullet\tilde q=-\vec p\cdot\vec v\,e_0=\mathbf 0$.
If $p_0\neq0$, suppose $\tilde p\bullet\tilde q=0$; the vector part gives
$p_0\vec q=-q_0\vec p$, so $\vec q$ is a multiple of $\vec p$, say
$\vec q=\lambda\vec p$; the scalar part then gives $p_0q_0=\lambda|\vec p|^2$, and
combining the two, $p_0q_0=\lambda|\vec p|^2$ with $\lambda=-q_0/p_0$ yields
$p_0^2q_0=-q_0|\vec p|^2$, that is $q_0(p_0^2+|\vec p|^2)=0$, so $q_0=0$; then
$\vec q=\lambda\vec p$ and the scalar part is $-\lambda|\vec p|^2=0$, so $\lambda=0$ and
$\tilde q=0$, a contradiction. Hence a nonzero element with $p_0\neq0$ has no nonzero partner.

**Corollary (the operator form of the criterion).** With the left multiplication operator
$L^{\bullet}_{\tilde p}\tilde q=\tilde p\bullet\tilde q$ of *The Multiplication Operators of the
Symmetric Plain Algebra*, a nonzero element is a zero divisor exactly when $L^{\bullet}_{\tilde p}$
is singular, and

$$
\det L^{\bullet}_{\tilde p}=p_0^2\,N(\tilde p),
$$

which vanishes, for $\tilde p\neq0$, exactly when $p_0=0$.

The set of partners of a pure element is its **annihilator**, whose two sides, whose operator and
whose rank are the companion article's (*Annihilators of the Symmetric Plain Algebra*, below this
article in this category).

## The Pairs That Multiply to Zero

### The Orthogonality Criterion

**Theorem.** For nonzero $\tilde p,\tilde q$,

$$
\tilde p\bullet\tilde q=0\iff \tilde p=\vec q_a,\ \tilde q=\vec v\ \text{with}\ \vec q_a,\vec v\ \text{pure},\ \text{nonzero and orthogonal},\ \vec q_a\cdot\vec v=0 .
$$

*Proof.* By the criterion both factors are pure, and the product of two pure elements is
$\vec q_a\bullet\vec v=-\vec q_a\cdot\vec v\,e_0$, which vanishes exactly when
$\vec q_a\cdot\vec v=0$.

So the zero-divisor pairs are exactly the pairs of orthogonal nonzero vectors of the
three-dimensional vector subspace.

### The Families and the Dimension Count

**Proposition.** The zero-divisor set of the block is the vector subspace with the origin removed,
of real dimension three; the set of zero-divisor pairs is the set of ordered pairs of orthogonal
nonzero vectors, of real dimension five; and the set of unordered pairs, equivalently the set of
two-planes through the origin of the vector subspace, is the Grassmannian
$\mathrm{Gr}(2,3)\cong\mathbb{RP}^2$ of dimension two.

*Proof.* The zero-divisor set is $\mathrm{Vect}(\mathbb{H})\setminus\{0\}$, of real dimension
three. A pair is an ordered pair $(\vec q_a,\vec v)$ with $\vec q_a\neq0$, $\vec v\neq0$,
$\vec q_a\cdot\vec v=0$: choosing $\vec q_a$ is three parameters, then $\vec v$ ranges over
the two-dimensional plane $\vec q_a^{\perp}$ minus the origin, two parameters, so the ordered
pairs form a set of dimension five. The unordered pair determines the plane
$\mathbb{R}\vec q_a\oplus\mathbb{R}\vec v=\vec q_a^{\perp}$, and every two-plane of
$\mathbb{R}^3$ arises, so the unordered pairs of an orthonormal pair are the two-planes, the
Grassmannian $\mathrm{Gr}(2,3)$ of dimension two.

## The Squares of the Elements

### The Square of a Pure Element

**Proposition.** The square of a pure element is a non-positive scalar:

$$
\vec q_a\bullet\vec q_a=\vec q_a^2=-|\vec q_a|^2e_0 .
$$

In particular a pure element is a zero divisor **and** has a central square, and
$\vec q_a\bullet\vec q_a=0$ only for $\vec q_a=0$.

*Proof.* The square is the plain square, and $\vec q_a^2=-\vec q_a\cdot\vec q_a\,e_0$ because
the cross term of a vector with itself vanishes. The scalar $-|\vec q_a|^2$ is zero only for
$\vec q_a=0$.

### The Square of a Non-Pure Element

**Proposition.** The square of a general element is

$$
\tilde q\bullet\tilde q=\bigl(q_0^2-|\vec q|^2\bigr)e_0+2q_0\vec q,
$$

with scalar part $q_0^2-|\vec q|^2$ and vector part $2q_0\vec q$. It has a nonzero vector
part exactly when $\tilde q$ is non-pure and nonzero.

*Proof.* The square is the plain square, displayed by the scalar–vector rule with
$\tilde p=\tilde q$. The vector part $2q_0\vec q$ vanishes when $q_0=0$ or $\vec q=0$, that
is, for a pure element or a scalar.

### The Associated Idempotents

**Proposition.** The idempotents of the block are exactly $0$ and $e_0$, and no nontrivial
idempotent is attached to a zero divisor:

$$
\tilde\pi\bullet\tilde\pi=\tilde\pi\iff \tilde\pi\in\{0,e_0\}.
$$

*Proof.* The equation is the plain equation $\tilde\pi^2=\tilde\pi$, since the square of the block
is the plain square. From the vector part, $(2\pi_0-1)\vec\pi=0$: either
$\vec\pi=0$, giving $\pi_0^2=\pi_0$ and $\tilde\pi\in\{0,e_0\}$, or $\pi_0=\tfrac12$, and
then the scalar part reads $\tfrac14-|\vec\pi|^2=\tfrac12$, that is
$|\vec\pi|^2=-\tfrac14$, which has no real solution.

**Remark (why no idempotent is built from a zero divisor).** In an algebra with a pure root of
$+e_0$ the element $\tfrac12(e_0+\vec q_a)$ is a nontrivial idempotent; here the square of a pure
element is $-|\vec q_a|^2e_0$, the negative of what is needed, so the construction never closes
and **the zero divisors of the block carry no idempotent with them**.

## Summary

A nonzero element of the block is a zero divisor, that is, has a nonzero partner $\tilde q$ with
$\tilde p\bullet\tilde q=0$, if and only if it is pure: the criterion is $p_0=0$, equivalently the
vanishing of the left multiplication operator, whose determinant is $p_0^2N(\tilde p)$. The
partners of a nonzero pure $\vec q_a$ are the elements of the two-dimensional plane
$\vec q_a^{\perp}$ inside the vector subspace, and the zero-divisor pairs are exactly the pairs of
orthogonal nonzero pure elements, an ordered family of real dimension five whose unordered version
is the Grassmannian $\mathrm{Gr}(2,3)\cong\mathbb{RP}^2$. A pure element has the negative scalar
square $-|\vec q_a|^2e_0$; a non-pure element has the square
$(q_0^2-|\vec q|^2)e_0+2q_0\vec q$ with nonzero vector part; and the idempotents are only $0$
and $e_0$, so no nontrivial idempotent is attached to a zero divisor. The definiteness of the norm
collapses the criterion to $q_0=0$ and the idempotents to $\{0,e_0\}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\bullet\tilde q=0$, $\tilde p,\tilde q\neq0$ | a zero-divisor pair |
| $p_0=0$ | the criterion: the element is pure |
| $\operatorname{Ann}(\vec q_a)=\vec q_a^{\perp}\cap\mathrm{Vect}(\mathbb{H})$ | the plane of partners of a pure $\vec q_a$ |
| $\det L^{\bullet}_{\tilde p}=p_0^2N(\tilde p)$ | the operator form of the criterion |
| $\vec q_a\bullet\vec q_a=-|\vec q_a|^2e_0$ | the square of a pure element |
| $(q_0^2-\lvert\vec q\rvert^2)e_0+2q_0\vec q$ | the square of a general element |
| $\{0,e_0\}$ | the idempotents of the block |

## Further Reading

- *Introduction to the Symmetric Plain Algebra of Quaternions*, for the product and its square.
- *Norm and Invertibility in the Symmetric Plain Algebra*, for the invertibility criterion and the contrast with division.
- *The Multiplication Operators of the Symmetric Plain Algebra*, below this article in this category, for the operator whose singularity is the criterion.
- *Annihilators of the Symmetric Plain Algebra* (`articles_maths/annihilators-of-the-symmetric-plain-algebra-of-quaternioid.md`), below this article in this category, the companion article, for the annihilator of an element, the operator and its rank and the dichotomy.
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, below this article in this category, for the idempotents and the Peirce decomposition.
- *Introduction to the Remarkable Subspaces of the Quaternions*, for the scalar line, the vector subspace and the orthogonality.
