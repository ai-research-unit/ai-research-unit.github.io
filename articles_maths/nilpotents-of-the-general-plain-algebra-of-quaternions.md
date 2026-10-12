# __Nilpotents of the General Plain Algebra__

## Introduction

The general plain bilinear product $\tilde p\tilde q$ is the multiplication of the quaternion algebra
$\mathbb{H}$, the one of the six products of *The 6 Products of the Quaternion Real Space*
that makes $\mathbb{H}$ an associative unital real algebra, and that algebra is the subject of
*Introduction to the General Plain Algebra of Quaternions*, above this article in this category. This
article studies its **nilpotents**: the nonzero elements whose square vanishes.

The class is empty, and it is empty for a reason that is visible in one line. The square of a general
element closes in two terms, one central and one along the vector part,

$$
\tilde q^2 = \bigl[q_0^2 - |\mathbf q|^2\bigr]e_0 + 2q_0\mathbf q ,
$$

and the central coefficient is the difference of two squares while the vector coefficient is
$2q_0\mathbf q$. Over $\mathbb{R}$ the two cannot vanish together off the origin: the vector term
forces the scalar part to vanish, and the central term then forces the vector part to vanish. The
complexified block, where the central coefficient is a difference of *complex* squares, does the
opposite, and its nilpotents form the pure isotropic cone of real dimension four, the *pure* family
of its zero divisors, the other family being the multiples of the nontrivial idempotents. Over
$\mathbb{R}$ both families are empty.

The neighbouring element theories are elsewhere. The zero divisors of the algebra are *Zero Divisors of
the General Plain Algebra*, above this article in this category, and the idempotents, the other class
that the complexified block names, are *Idempotents of the General Plain Algebra*, above this article
in this category. The nilpotents appear in the classification of the three central values as the
nonzero roots of $0$ in *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*,
above this article in this category, and the class of the empty element theory is folded in *The
Specificities of the General Plain Algebra*, below this article in this category.

## Conventions

The algebra $\mathbb{H}$ has basis $e_0 = 1, e_1, e_2, e_3$, with $e_0$ the unit, $e_k^2 = -e_0$ and
$e_1e_2 = e_3 = -e_2e_1$. A general element is $\tilde q = q_0e_0 + \mathbf q$, with
$q_0 = \mathrm{Sc}(\tilde q) \in \mathbb{R}$ and $\mathbf q = q_1e_1 + q_2e_2 + q_3e_3$; the natural
conjugation is $\tilde q^{\natural} = q_0e_0 - \mathbf q$; and the quaternion norm is
$N(\tilde q) = \tilde q\tilde q^{\natural} = q_0^2 + |\mathbf q|^2$, positive definite over
$\mathbb{R}$ by *Norm and Invertibility in the General Plain Algebra*, above this article in this
category. The plain form is $B(\tilde p,\tilde q) = \mathrm{Sc}(\tilde p\tilde q) = p_0q_0 - (\mathbf p,\mathbf q)$,
indefinite of signature $(1,3)$; the two forms are *The 2 Forms over the Quaternion $\mathbb{R}$
Space*. The scalar line $\mathbb{R}e_0$ is the centre and $\mathrm{Vect}(\mathbb{H})$ is the vector
subspace, of dimension three.

The plain product $\tilde p\tilde q$ is associative with the two-sided unit $e_0$, and it is a division
algebra: every nonzero element is invertible, $\tilde q^{-1} = \tilde q^{\natural}/N(\tilde q)$, so
there is no zero divisor. A nilpotent is written $\tilde\Upsilon$ and a generic element $\tilde q$.
The vocabulary of the nilpotent, of the square-zero element and of the cube-zero element is
*Definitions for the Study of the 6 Algebraic Structures*, §*The Element Vocabulary*, and the six
structures are *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*.

## Definition

**Definition.** A **square-zero element** of the general plain algebra is an element $\tilde q$ with

$$
\tilde q^2 = 0 .
$$

A **nilpotent** is, in the vocabulary of *Definitions for the Study of the 6 Algebraic Structures*, a
**nonzero** element with a vanishing power, $\tilde\Upsilon^k = 0$ for some $k$; the class of this
article is the class the corpus calls the nilpotent class, and its members are the nonzero elements
whose square vanishes. A nilpotent is of **index two** when its square vanishes while it does not.

The equation names a product, and the notion is relative to it; throughout this article the product
is the general plain bilinear product, the multiplication of the algebra. The element $0$ satisfies
$\tilde q^2 = 0$ but is not a nilpotent, since the corpus requires a nilpotent to be nonzero; the
square-zero set and the nilpotent class are kept apart below, and the relation between them is stated
in both readings.

## The Criterion

The square of a general element closes in two terms, one central and one along the vector part,
because the square of the vector part is central:

$$
\mathbf q^2 = -|\mathbf q|^2 e_0 , \qquad \tilde q^2 = \bigl[q_0^2 - |\mathbf q|^2\bigr]e_0 + 2q_0\mathbf q .
$$

**Theorem (the criterion for a square-zero element).** For $\tilde q\in\mathbb{H}$ the following are
equivalent: $\tilde q^2 = 0$; the scalar part and the vector part both vanish, $q_0 = 0$ and
$\mathbf q = 0$; and $\tilde q = 0$.

**Proof.** The displayed formula expands the square. The two coefficients of the sum, central and
vector, must vanish separately. If $q_0 \neq 0$ then the vector coefficient $2q_0\mathbf q$ vanishes
only for $\mathbf q = 0$, and then the central coefficient is $q_0^2 \neq 0$, a contradiction; so
$q_0 = 0$. With $q_0 = 0$ the formula reads $\tilde q^2 = -|\mathbf q|^2 e_0$, which vanishes exactly
when $|\mathbf q|^2 = q_1^2 + q_2^2 + q_3^2 = 0$, a sum of three squares of real numbers, hence
exactly when $\mathbf q = 0$. So $\tilde q = 0$ is the only square-zero element.

**Corollary.** The square-zero set of the plain product is the singleton $\{0\}$, and the nilpotent
class — the nonzero square-zero elements — is the empty set. The algebra therefore carries no
nilpotent whatever, of index two or of any higher index; the general statement, with its proof from
invertibility, is the theorem of §*Index Two*.

Over the complexified block the same computation passes through the complex bilinear form
$(\mathbf Q,\mathbf Q) = Q_1^2+Q_2^2+Q_3^2$: the criterion there is $Q_0 = 0$ and
$(\mathbf Q,\mathbf Q) = 0$, a complex vector part on the isotropic cone, and the nilpotents are the
nonzero elements of that cone, of real dimension four. The difference is exactly the passage from the
sum of three real squares, which is positive definite, to the sum of three complex squares, which is
isotropic on a cone.

## Index Two

**Theorem (no higher index).** For the general plain algebra, $\tilde q^k = 0$ for some $k$ if and
only if $\tilde q = 0$; equivalently, a vanishing power vanishes at the first step.

**Proof.** If $\tilde q \neq 0$ it is a unit, with inverse $\tilde q^{-1}$. Multiplying
$\tilde q^k = 0$ on the left by $\tilde q^{-1}$ gives $\tilde q^{k-1} = 0$, and iterating gives
$\tilde q = 0$, a contradiction. So no nonzero element has a vanishing power, of index two or of any
higher index.

The direct computation of the cube agrees, and it is worth recording because it mirrors the
complexified expansion:

$$
\tilde q^2 = \bigl[q_0^2-|\mathbf q|^2\bigr]e_0 + 2q_0\mathbf q , \qquad
\tilde q^3 = q_0\bigl[q_0^2-3|\mathbf q|^2\bigr]e_0 + \bigl[3q_0^2-|\mathbf q|^2\bigr]\mathbf q .
$$

If $\mathbf q = 0$ then $\tilde q^3 = q_0^3 e_0$ vanishes only for $q_0 = 0$; if $\mathbf q \neq 0$
the vanishing of the vector coefficient forces $|\mathbf q|^2 = 3q_0^2$, and the central coefficient
is then $q_0[q_0^2-9q_0^2] = -8q_0^3$, which vanishes only for $q_0 = 0$, whereupon
$|\mathbf q|^2 = 0$, a contradiction. So $\tilde q^3 = 0$ if and only if $\tilde q = 0$, and the same
conclusion holds for every higher power.

## The Nilpotents and the Zero Divisors

A nonzero square-zero element is a zero divisor in the strongest possible way: it annihilates itself.
This is the property that in the complexified block singles the nilpotents out among the zero
divisors.

**Proposition.** If $\tilde\Upsilon$ is a nonzero square-zero element then
$\tilde\Upsilon\tilde\Upsilon = 0$ on both sides, so $\tilde\Upsilon$ is a two-sided zero divisor,
with itself as annihilating partner.

**Proof.** The relation $\tilde\Upsilon^2 = 0$ is the product of $\tilde\Upsilon$ with itself, on
either side.

Over $\mathbb{R}$ the proposition has no instance, because there is no nonzero square-zero element,
and it is stated to locate the class against the empty zero-divisor set: a nonzero nilpotent would be
a zero divisor, the zero-divisor set is empty (*Zero Divisors of the General Plain Algebra*, above
this article in this category), and the nilpotent class is therefore empty. The two emptinesses are
the same emptiness seen from two sides. In the complexified block the relation runs the other way, and
the nonzero nilpotents are exactly the pure family of the zero-divisor cone.

## The Nilpotents and the Idempotents

**Theorem.** No element of $\mathbb{H}$ is both an idempotent and a nonzero nilpotent; the two classes
are disjoint.

**Proof.** An idempotent is $0$ or $e_0$ (*Idempotents of the General Plain Algebra*, above this
article in this category). The element $e_0$ is not square-zero, $e_0^2 = e_0 \neq 0$, and no nonzero
element is square-zero by the criterion; so no idempotent is a nilpotent.

Over $\mathbb{R}$ the disjointness is total: the idempotents are $0$ and $e_0$, the nilpotent class
is empty, and the square-zero set is the single point $0$, whose only member is the idempotent $0$
and not a nilpotent. The complexified block draws the same disjointness between two populated classes,
the nilpotent cone and the idempotent manifold, which meet only at the origin; the difference is that
both of its classes have points.

## The Nilpotents and the Central Values

The equation $\tilde x^2 = 0$ is the third of the three central power equations
$\tilde x^2 = c\, e_0$ for $c = -1, 0, +1$, and it is the one whose root set contains no nonzero
element.

**Proposition.** The solutions of $\tilde x^2 = 0$ are exactly the origin, and the origin is not a
nilpotent.

**Proof.** The criterion of §*The Criterion*.

**Corollary.** The root set of $0$ is $\{0\}$, the root set of $+1$ is $\{\pm e_0\}$, both central,
and the root set of $-1$ is the unit sphere of the vector subspace, of dimension two. So among the
three central values it is $c = 0$ whose root set is empty of nonzero elements, and the nilpotent
class, the class of the nonzero roots of $0$, is empty. This is the reading, in the vocabulary of this
article, of the root classification of *Square Roots of Minus One, Zero and Plus One in the General
Plain Algebra*, above this article in this category.

## The Square-Zero Set and the Remarkable Subspaces

A square-zero element of the complexified block is pure, and its vector part is isotropic. Over
$\mathbb{R}$ the square-zero set is the origin, and the statement is that neither remarkable subspace
contributes anything beyond it.

| Remarkable subspace | Square-zero elements |
|---|---|
| $\mathbb{R}e_0$, the centre | $0$ alone; a nonzero scalar has $s^2 > 0$ |
| $\mathrm{Vect}(\mathbb{H})$, the vector subspace | $0$ alone; a nonzero pure element has $\mathbf q^2 = -\lvert\mathbf q\rvert^2 e_0 \neq 0$ |

The entries are forced by the two restrictions of the norm: on the centre $N(se_0) = s^2$, positive
for $s \neq 0$, and on the vector subspace $N(\mathbf q) = |\mathbf q|^2$, positive for
$\mathbf q \neq 0$. A zero of the plain square is thus nowhere but the origin, and both remarkable
subspaces carry the same square-zero set as the whole space. The two restrictions of the norm are *The
2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*.

## Summary

The nilpotents of the general plain algebra are the nonzero elements of vanishing square. The criterion
is $\tilde q^2 = 0$ if and only if $q_0 = 0$ and $\mathbf q = 0$, which is $\tilde q = 0$; so the
**square-zero set is the singleton $\{0\}$ and the nilpotent class is empty**. There is no nonzero
square-zero element and no element of index two or more: a vanishing power vanishes at the first step,
and the direct computation of the square and the cube confirms it, the central coefficient
$q_0^2 - |\mathbf q|^2$ and the vector coefficient $2q_0\mathbf q$ being unable to vanish together off
the origin.

This is the opposite of the complexified block, whose nilpotents form the pure isotropic cone of real
dimension four, the nonzero square-zero elements there being exactly the pure family of the
zero-divisor cone. Over $\mathbb{R}$ both families of that cone are empty: the square-zero family by
positive definiteness, the idempotent family by the same property of the norm, and the two classes of
the block, the idempotents and the nilpotents, are the pair $\{0, e_0\}$ and the empty set. The
square-zero set meets neither the centre nor the vector subspace except at the origin.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Upsilon$ | A nilpotent, a nonzero element of vanishing square |
| $\tilde q^2 = 0$ | The square-zero equation |
| $\{0\}$ | The square-zero set of the plain product |
| $\varnothing$ | The nilpotent class |
| $\tilde q^2 = [q_0^2-\lvert\mathbf q\rvert^2]e_0 + 2q_0\mathbf q$ | The square of a general element |
| $\tilde q^3 = q_0[q_0^2-3\lvert\mathbf q\rvert^2]e_0 + [3q_0^2-\lvert\mathbf q\rvert^2]\mathbf q$ | The cube of a general element |
| $N(\tilde q) = q_0^2+\lvert\mathbf q\rvert^2$ | Quaternion norm, positive definite |
| $\mathbb{R}e_0$, $\mathrm{Vect}(\mathbb{H})$ | Centre and vector subspace |

## Further Reading

- *Definitions for the Study of the 6 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-6-algebraic-structures.md`), §*The Element Vocabulary*, for the general definition of the nilpotent, of the square-zero element and of the cube-zero element.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra-of-quaternions.md`), above this article in this category, for the empty zero-divisor set and the two families of the complexified block.
- *Idempotents of the General Plain Algebra* (`articles_maths/idempotents-of-the-general-plain-algebra-of-quaternions.md`), above this article in this category, for the other class and its disjointness from this one.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra-of-quaternions.md`), above this article in this category, for the three central values and the root set of $0$.
- *The Specificities of the General Plain Algebra* (`articles_maths/the-specificities-of-the-general-plain-algebra-of-quaternions.md`), below this article in this category, for the folding of the empty classes and the isolation of the plain product among the six.
- *Nilpotents of the General Plain Algebra* (`articles_maths/nilpotents-of-the-general-plain-algebra.md`), the complexified counterpart, for the pure isotropic cone, its real dimension four and the index-two theorem.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for nilpotents and their place in the structure of a finite-dimensional algebra.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for nilpotents, units and the division property.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the square of a quaternion and the behaviour of its vector part.
