# __Zero Divisors of the General Quaternionic Sesqualgebra__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries, on its
underlying complex space, the four general products of *The Four General Products and Their Relations over the Biquaternion Algebra*, and this article treats the **zero divisors** of the fourth, the
**general quaternionic sesquilinear product**

$$
\tilde Q_1 \star \tilde Q_2 = \tilde Q_1^{\natural}\tilde Q_2^{*} ,
$$

whose rule, multiplication table and axioms are *Introduction to the General Quaternionic
Sesqualgebra of Biquaternions*, and whose two halves, $\mathrm{SQS}$ and $\mathrm{AQS}$, are *The
Symmetric and Antisymmetric Parts of a Sesqualgebra Product*.

A zero divisor is defined **by a product**, so the set belongs to the product and not to the space.
The article states the definition for a general product $\star$ (quoted from *Definitions for the
Study of the Algebraic Structures*), fixes the product of the block, gives the criterion and the
two families, describes the set, and then compares the set with the sets of the other three general
products: the four sets **coincide**, and that is a theorem quoted, not a licence to transfer a
classification. The finer structure of the GQS set, its square-zero subfamily and its non-pure
members, is the point of the article and is owned by *Nilpotents of the General Quaternionic
Sesqualgebra*; the position of the set in the remarkable subspaces is *Remarkable Subspaces under
the General Quaternionic Sesqualgebra of Biquaternions*.

$$
\tilde Q^{\natural} = Q_t - \vec Q , \qquad \tilde Q^{*} = \overline{\tilde Q^{\natural}} = \overline{Q_t} - \overline{\vec Q} , \qquad \overline{\tilde Q} = \tilde Q^{\natural*} = \overline{Q_t} + \overline{\vec Q} ,
$$

where the bar on a coefficient is the complex conjugate. The **central square** is

$$
C(\tilde Q) = \sum_{\mu\in\{t,x,y,z\}} Q_\mu^2 , \qquad C(\tilde Q)e_t = \tilde Q\tilde Q^{\natural} = \tilde Q^{\natural}\tilde Q ,
$$

and its vanishing is the zero-divisor criterion of the general plain algebra (*Zero Divisors of the
General Plain Algebra*). The product is $\tilde Q_1\star\tilde Q_2 = \tilde Q_1^{\natural}\tilde Q_2^{*}$,
with the natural conjugation ${}^{\natural}$ in the first slot and the star ${}^{*}$ in the second;
the juxtaposition $\tilde Q_1\tilde Q_2$ is the general plain bilinear product, the multiplication of
the algebra.

**The results.** A nonzero element $\tilde Q$ is a zero divisor of the general quaternionic sesquilinear product $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2^{*}$ if and only if its central square vanishes, $C(\tilde Q)=\sum_\mu Q_\mu^{2}=0$; the left and the right reading give the same condition, and the four general products share this one set. The set is the complex cone $\{C(\tilde Q)=0\}$ of complex dimension three and real dimension six, the same subset the plain product cuts out. It splits by the scalar part into the pure family $Q_t=0$ with $\sum_k Q_k^{2}=0$ and the non-pure family $Q_t\neq0$ with $\sum_k Q_k^{2}=-Q_t^{2}$, and the square-zero elements, of real dimension four, lie in the **non-pure** family, so the split by the square and the split by the scalar part cut across each other. Each section below states its result first and then proves it.

## The Definition

**Definition (zero divisor of a product).** Let $\star$ be a product on $\mathbb{B}$. A nonzero
element $\tilde Q$ is a **left zero divisor of $\star$** when there is a nonzero $\tilde Q_2$ with
$\tilde Q\star\tilde Q_2 = 0$; a **right zero divisor of $\star$** when there is a nonzero $\tilde Q_2$
with $\tilde Q_2\star\tilde Q = 0$; and a **zero divisor of $\star$** when it is a left zero divisor
or a right zero divisor. The equation and the pair both name the product, so the notion is relative
to it; the general definition, with the two-sided reading, is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

Throughout this article the product is the general quaternionic sesquilinear product
$\tilde Q_1\star\tilde Q_2 = \tilde Q_1^{\natural}\tilde Q_2^{*}$, and, unqualified, **zero divisor** means
**zero divisor of $\star$**. The zero-divisor sets of the other three general products, and the
theorem that the four coincide, are *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

## The Criterion

**A nonzero element $\tilde Q$ is a zero divisor of $\star$ exactly when its central square vanishes, $C(\tilde Q)=\sum_\mu Q_\mu^{2}=0$, the same equation as for the plain product.**

**Theorem (the criterion).** A nonzero element $\tilde Q$ is a zero divisor of $\star$ if and only
if

$$
\boxed{\; C(\tilde Q) = \sum_{\mu\in\{t,x,y,z\}} Q_\mu^2 = 0 \;}.
$$

**Proof.** The product is $\tilde Q\star\tilde Q_2 = \tilde Q^{\natural}\tilde Q_2^{*}$. An element
$\tilde Q_2$ runs through $\mathbb{B}$ exactly when $\tilde Q_2^{*}$ does, because ${}^{*}$ is a
bijection, so the existence of a nonzero $\tilde Q_2$ with $\tilde Q\star\tilde Q_2 = 0$ is the
existence of a nonzero $\tilde Q_1$ with $\tilde Q^{\natural}\tilde Q_1 = 0$, that is,
$\tilde Q^{\natural}$ is a left zero divisor of the plain product, with $\tilde Q_1 = \tilde Q_2^{*}$.
The zero-divisor criterion of the plain algebra says that this happens exactly when
$C(\tilde Q^{\natural}) = 0$, and the natural conjugation keeps the three vector squares and the
scalar square, so $C(\tilde Q^{\natural}) = Q_t^2 + \sum_k Q_k^2 = C(\tilde Q)$. The left statement
follows; the right statement is the same computation with $\tilde Q_2^{\natural}\tilde Q^{*} = 0$,
which for varying $\tilde Q_2$ says that $\tilde Q^{*}$ is a right zero divisor of the plain product;
the plain criterion applied to $\tilde Q^{*}$ gives back one condition because
$C(\tilde Q^{*}) = \overline{C(\tilde Q)}$ vanishes exactly when $C(\tilde Q)$ does. The two
conditions are one, which is the statement.

The criterion is the same equation as for the plain product, and the coincidence is the subject of
the comparison below. What the GQS criterion does **not** inherit is the reading of the criterion:
an element of $C = 0$ whose scalar part vanishes is a nilpotent of the plain algebra, while here
the square of a zero divisor need not vanish at all.

**Example.** The element $\tilde Q = \vec e_x + i\vec e_y$ has $\vec Q = \vec e_x + i\vec e_y$, so
$C(\tilde Q) = 1 + i^2 = 0$ and it is a zero divisor. Its left partner is the element
$\tilde Q_2 = ie_t - \vec e_z$, for which

$$
\tilde Q\star\tilde Q_2 = (\vec e_x+i\vec e_y)^{\natural}(ie_t-\vec e_z)^{*} = (-\vec e_x-i\vec e_y)(-ie_t+\vec e_z) = 0 ,
$$

and its square is

$$
\tilde Q\star\tilde Q = (\overline{\tilde Q}\tilde Q)^{\natural} = (-2e_t+2i\vec e_z)^{\natural} = -2e_t-2i\vec e_z \neq 0 .
$$

So $\tilde Q$ is a zero divisor whose left multiplication is not square-zero, in contrast to a
nonzero nilpotent, which annihilates itself (*Nilpotents of the General Quaternionic
Sesqualgebra*).

## The Two Families

**The zero-divisor set splits by the scalar part into the disjoint pure family $Q_t=0$ with $\sum_k Q_k^{2}=0$ and non-pure family $Q_t\neq0$ with $\sum_k Q_k^{2}=-Q_t^{2}\neq0$, whose union with the origin is the whole set, and the square-zero elements lie in the non-pure family, so the split by the square cuts across the split by the scalar part.**

The zero-divisor set splits by the scalar part, as it does for the plain product, and the split is
named.

**Definition (the two families).** A zero divisor $\tilde Q$ of $\star$ is **pure** when $Q_t = 0$
and **non-pure** when $Q_t \neq 0$. The set is the disjoint union of the two families and the
origin.

**Proposition (the pure family).** A pure zero divisor $\tilde Q = \vec Q$ satisfies

$$
\boxed{\; \sum_{k=1}^{3} Q_k^2 = 0 \;},
$$

and conversely every nonzero pure element with $\sum_k Q_k^2 = 0$ is a zero divisor.

**Proof.** Purity is $Q_t = 0$, and the criterion $C(\tilde Q) = Q_t^2 + \sum_k Q_k^2 = 0$ is then
the displayed relation. The converse is the criterion read backwards.

**Proposition (the non-pure family).** A non-pure zero divisor satisfies

$$
\sum_{k=1}^{3} Q_k^2 = -Q_t^2 \neq 0 ,
$$

and the family is non-empty; every element of the square-zero family of *Nilpotents of the General
Quaternionic Sesqualgebra*, in particular $e_t + i\vec e_x$, is non-pure.

**Proof.** The relation is the criterion with $Q_t \neq 0$. The element $e_t + i\vec e_x$ has $Q_t = 1$,
$Q_x = i$, $Q_y = Q_z = 0$, so $C = 1 - 1 = 0$, and it is a zero divisor with nonzero scalar part.
Its square vanishes, as the cited article records, so the non-pure family is not the complement of
the square-zero family.

This is the point at which the GQS set departs from the plain one. In the plain algebra the pure
family is exactly the nonzero nilpotents and the non-pure family is the part of the cone with
non-vanishing scalar part; here the square-zero elements are **non-pure**, so the two splittings,
the one by the scalar part and the one by the vanishing of the square, cut across each other. The
family split is a split of the cone, and the square-zero split is a different split of the same
cone.

## The Set

**The zero-divisor set is the punctured complex cone $\{\tilde Q\neq0:C(\tilde Q)=0\}$, of complex dimension three and real dimension six, the zero set of the non-degenerate complex quadratic form $C$ on $\mathbb{C}^4$, containing the pure vector-subspace part of complex dimension two and the non-pure part of complex dimension three.**

**Theorem (the set).** The zero-divisor set of $\star$ is

$$
\boxed{\; \{\tilde Q \neq 0 : C(\tilde Q) = 0\} = \{\tilde Q \neq 0 : Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2 = 0\} \;},
$$

a complex cone of complex dimension three and real dimension six, the zero set of the
non-degenerate complex quadratic form $C$ on $\mathbb{C}^4$. Its vertex is the origin, which is not
a zero divisor, and it contains the whole vector subspace part $\{Q_t = 0, \sum_k Q_k^2 = 0\}$ of
complex dimension two together with the non-pure part $Q_t \neq 0$ of complex dimension three.

**Proof.** The description is the criterion. The form $C$ is non-degenerate and its zero set is the
affine cone over the non-singular quadric $C = 0$ in $\mathbb{P}^3$, of complex dimension two, so
the affine cone has complex dimension three and real dimension six. The vector-subspace part is the
cone over a conic in $\mathbb{P}^2$, of complex dimension two, and for $Q_t \neq 0$ one solves
$\sum_k Q_k^2 = -Q_t^2$, a quadric in three variables, so the non-pure part has complex dimension
three.

The dimension is the same as for the plain product, because the criterion is the same form; the two
cones are the same subset of $\mathbb{B}$.

## The Coincidence with the Other Three Products

**The four general products have the same zero-divisor set $\{\tilde Q\neq0:C(\tilde Q)=0\}$, a quoted theorem that holds for the left and the right reading separately; the predicate coincides but the square does not, the square-zero set of $\star$ being of real dimension four while that of the plain product is the pure isotropic cone.**

**Theorem (the four products have one zero-divisor set, quoted).** The four general products of
*The Four General Products and Their Relations over the Biquaternion Algebra* have the same zero-divisor set,
namely $\{\tilde Q \neq 0 : C(\tilde Q) = 0\}$. The theorem is *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*,
and it holds for the left and the right reading separately.

**Proof.** The four products are $\theta(\tilde Q)\phi(\tilde Q_2)$ with
$\theta \in \{\mathrm{id}, {}^{\natural}\}$ and $\phi \in \{\mathrm{id}, {}^{*}\}$, and both
$\theta$ and $\phi$ are bijections preserving the vanishing of the central square, so the plain
criterion transfers to each of the four. The general-argument form is in the cited article.

The coincidence is the reason the criterion of §*The Criterion* needed no new computation and the
reason the set of §*The Set* is the set of the block: the four products separate the elements only
through the product, and the zero-divisor predicate is blind to the two slot involutions because it
is the vanishing of the central square, which the involutions preserve. It is **not** a licence to
transfer the classification silently, and the difference appears as soon as the square is taken:
the square-zero set of the plain product is the pure isotropic cone, of real dimension four, while
the square-zero set of $\star$ is a different real four-dimensional family, that of *Nilpotents of
the General Quaternionic Sesqualgebra*. The predicate coincides, the square does not.

## The Zero Divisors and the Square-Zero Elements

**Every nonzero element with $\tilde Q\star\tilde Q=0$ is a zero divisor of $\star$, and the square-zero elements form a proper subfamily of the zero-divisor set, of real dimension four, lying in the non-pure family; in the plain algebra the square-zero elements are instead the pure zero divisors.**

The relation between the two families of this article and the nilpotents of the block is the one
place where the GQS zero-divisor theory says something the plain theory does not.

**Theorem (the square-zero elements are zero divisors).** Every nonzero element with
$\tilde Q\star\tilde Q = 0$ is a zero divisor of $\star$, and the square-zero elements form a
proper subfamily of the zero-divisor set, of real dimension four, lying in the non-pure family.

**Proof.** If $\tilde Q\star\tilde Q = 0$ then $\tilde Q$ is a zero divisor with
$\tilde Q_2 = \tilde Q$. The identification with the family $c(\vec u + i)$, its dimension and its
non-purity are *Square Roots of Zero and the Nilpotents of the General Quaternionic Sesqualgebra*.

**Corollary (the contrast with the plain product).** In the plain algebra the square-zero elements
are the pure zero divisors and the non-pure zero divisors have non-vanishing square; in the GQS the
square-zero elements are non-pure and a pure zero divisor, such as $\vec e_x + i\vec e_y$, has nonzero
square.

**Proof.** The plain statement is *Nilpotents of the General Plain Algebra*; the GQS statement is
the example of §*The Criterion* and the previous theorem.

So the two products agree on **which** elements are zero divisors and disagree on **how** a zero
divisor squares. That is the sharpest form of the zero-divisor clarification for the block: the
definition belongs to the product, the criterion happens to coincide, and the element theory built
on the square does not.

## Summary

The zero divisors of the general quaternionic sesquilinear product
$\tilde Q_1\star\tilde Q_2 = \tilde Q_1^{\natural}\tilde Q_2^{*}$ are defined relative to the product, and
they are the nonzero elements with $C(\tilde Q) = \sum_\mu Q_\mu^2 = 0$, equivalently
$\tilde Q\tilde Q^{\natural} = 0$; the left and the right reading give the same condition. The set
is the complex cone $C = 0$ of complex dimension three and real dimension six, the same subset of
the space that the plain product, the natural product and the general plain sesquilinear product
cut out, a coincidence that is a theorem of *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* because the criterion
is the vanishing of the central square and the four products differ only by the two slot
involutions.

The set splits by the scalar part into the pure family $Q_t = 0$, with $\sum_k Q_k^2 = 0$, and the
non-pure family $Q_t \neq 0$, with $\sum_k Q_k^2 = -Q_t^2$; the square-zero elements, which are a
real four-dimensional proper subfamily, lie in the **non-pure** family, so the split by the square
and the split by the scalar part cut across each other and the analogy with the plain product stops
at the criterion. The element $\vec e_x + i\vec e_y$ is a pure zero divisor whose square is $-2e_t - 2i\vec e_z$,
and the element $e_t + i\vec e_x$ is a non-pure zero divisor whose square vanishes.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q_1\star\tilde Q_2 = \tilde Q_1^{\natural}\tilde Q_2^{*}$ | the general quaternionic sesquilinear product |
| $\tilde Q^{\natural}$, $\tilde Q^{*}$, $\overline{\tilde Q}$ | the natural, the star and the Hermitian conjugations |
| zero divisor of $\star$ | a nonzero $\tilde Q$ with a nonzero right or left partner of vanishing product |
| $C(\tilde Q) = \sum_\mu Q_\mu^2$ | the central square, $C(\tilde Q)e_t = \tilde Q\tilde Q^{\natural}$ |
| $C(\tilde Q) = 0$ | the zero-divisor criterion |
| pure, non-pure | $Q_t = 0$; $Q_t \neq 0$ |
| $\vec e_x + i\vec e_y$ | a pure zero divisor with non-vanishing square |
| $e_t + i\vec e_x$ | a non-pure zero divisor with vanishing square |

## Further Reading

- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), for the definition of the zero divisor relative to a product and the two-sided reading.
- [N-Regularity and Degeneracy in the Biquaternion Algebra](n-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the criterion of the plain product, the two families and the element theory of the cone.
- [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the theorem that the four general products have one zero-divisor set, which this article quotes.
- [Square Roots of Zero and the Nilpotents of the General Quaternionic Sesqualgebra](square-roots-of-zero-and-the-nilpotents-of-the-general-quaternionic-sesqualgebra.html), for the square-zero family $c(\vec u+i)$, its real dimension and its non-purity.
- [Introduction to the General Quaternionic Sesqualgebra](introduction-to-the-general-quaternionic-sesqualgebra.html), for the product, its table and its axioms.
- [The Square of the General Quaternionic Sesquilinear Product and the Two Halves](the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.html), for the identity $\tilde Q\star\tilde Q = (\overline{\tilde Q}\tilde Q)^{\natural}$ used in the examples.
- [Remarkable Subspaces under the General Quaternionic Sesqualgebra](remarkable-subspaces-under-the-general-quaternionic-sesqualgebra.html), for the position of the cone in the remarkable subspaces.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the notation and the article format.
- [Annihilators of the General Quaternionic Sesqualgebra](annihilators-of-the-general-quaternionic-sesqualgebra.html), below this article in this category, the companion article, for the two distinct annihilators of an element and the rank table
