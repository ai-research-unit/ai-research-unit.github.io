# __Zero Divisors of the Biquaternion Algebra__

## Introduction

This article studies the zero divisors of the biquaternion algebra $\mathbb{B}$. It follows *Norm
and Invertibility in the Biquaternion Algebra*, which established the criterion for invertibility
and the three-way classification of the elements of $\mathbb{B}$, and it opens the element theory
of the block: the two families it separates are developed in *Square Roots of One and the
Idempotents of the Biquaternion Algebra* and *Square Roots of Zero and the Nilpotents of the
Biquaternion Algebra*, and its vocabulary of pure and non-pure is used throughout. The goal here
is to characterize the zero divisors **of the general plain bilinear product**, to split them into
two families, and to describe their structure.

**The results.** A nonzero biquaternion is a zero divisor of the plain product exactly when its central square vanishes, $\tilde{Q}\tilde{Q}^{\natural} = 0$; the elements therefore fall into the three classes invertible, zero and zero divisor. The zero divisors split into two disjoint families: the **pure** ones, exactly the nonzero nilpotents with $\tilde{Q}^2 = 0$ and $Q_x^2 + Q_y^2 + Q_z^2 = 0$, forming a cone of real dimension $4$; and the **non-pure** ones, exactly the complex multiples of the nontrivial idempotents, with $\tilde{Q}^2 = 2 Q_t \tilde{Q}$ and $Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2 = 0$, forming the rest of the cone. The zero-divisor set is a complex cone of complex dimension $3$ and real dimension $6$.

A divisor is relative to a product. The definition is stated once for a general product in
*Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and read on the products of the space;
the unqualified "zero divisor" means "zero divisor of the general plain bilinear product", the
multiplication of the biquaternion algebra, and every other product is named. The four general
products and their common zero-divisor set are *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

Every claim is proved or stated as a definition, no physics is invoked and no examples are given.
The algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, its four conjugations and
its remarkable subspaces are assumed from *The Biquaternion Algebra as a Vector Space over $\mathbb{C}$ and $\mathbb{R}$* and
*Introduction to the Remarkable Subspaces*, and the invertibility criterion from *Norm and
Invertibility in the Biquaternion Algebra*. The idempotents that the non-pure family produces are
*Square Roots of One and the Idempotents of the Biquaternion Algebra*, and the nilpotents of the
pure family are *Square Roots of Zero and the Nilpotents of the Biquaternion Algebra*.

Throughout this article, the quaternion basis is written $e_t = 1, \vec e_x, \vec e_y, \vec e_z$, and the scalar
imaginary is written $i$, so that it does not collide with the quaternion units. A general
biquaternion is written

$$
\tilde{Q} = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z, \qquad Q_\mu \in \mathbb{C}.
$$

The quaternion conjugate is denoted $\tilde{Q}^{\natural}$, the complex conjugate is denoted
$\bar{\tilde{Q}}$, the Hermitian conjugate is denoted
$\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$, and the anti-Hermitian conjugate is denoted
$\tilde{Q}^\flat = -\tilde{Q}^{*}$. A product of the space is written $\star$ when the statement is
one about an arbitrary product and only the fact that it is a product is used, as in §*Definition*;
the four general products keep their signs $\tilde Q_1\tilde Q_2$, $\tilde Q_1^{\natural}\tilde Q_2$,
$\tilde Q_1\tilde Q_2^{*}$, $\tilde Q_1^{\natural}\tilde Q_2^{*}$, and the general plain bilinear product,
the multiplication of the algebra, is written $\tilde Q_1\tilde Q_2$. The product
$\tilde{Q}\tilde{Q}^{\natural}$ lies in the scalar line $\mathbb{C}_{\mathbb{B}}$; its vanishing is
the algebraic condition that decides the zero divisors of the plain product, and it is never read
here as a length.

## Definition

The word names a product, so the definition is stated for a general product and then read on the
products of this space; it is stated once and for all in *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. Let $\star$ be a product on $\mathbb{B}$ — any of the twelve products of
*The 12 Products of the Biquaternion Complex Space*, that is one of the four general products or
one of their symmetric or antisymmetric parts.

**Definition.** Let $\star$ be a product on $\mathbb{B}$ and let $\tilde{Q}_1\in\mathbb{B}$. The
element $\tilde{Q}_1$ is a **left zero divisor of $\star$** when $\tilde{Q}_1\neq0$ and there is a
nonzero $\tilde{Q}_2$ with $\tilde{Q}_1\star\tilde{Q}_2 = 0$; it is a **right zero divisor of $\star$** when
$\tilde{Q}_1\neq0$ and there is a nonzero $\tilde{Q}_2$ with $\tilde{Q}_2\star\tilde{Q}_1 = 0$; and it is a
**zero divisor of $\star$** when it is one or the other. An element that is both a left and a right
zero divisor of $\star$ is a **two-sided zero divisor of $\star$**.

The requirement that both $\tilde{Q}_1$ and $\tilde{Q}_2$ be nonzero is essential. In particular, the
element $\tilde{Q}_1 = 0$ is **not** a zero divisor of any product, even though $0\star\tilde{Q}_2 = 0$
for any $\tilde{Q}_2$.

**On the products of the space.** Substituting the product for $\star$ gives one definition to a
product. On the general plain bilinear product the two equations are $\tilde Q_1\tilde Q_2 = 0$ and
$\tilde Q_2\tilde Q_1 = 0$, the classical pair; on $\tilde Q_1^{\natural}\tilde Q_2$ they are
$\tilde Q_1^{\natural}\tilde Q_2 = 0$ and $\tilde Q_2^{\natural}\tilde Q_1 = 0$; and the outer product has
every nonzero element as a zero divisor, since $\tilde Q\wedge\tilde Q = 0$. The four general
products, four different equations, happen to select the one cone $\mathcal{C}\setminus\{0\}$
described here, a coincidence of this algebra proved in *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.
Throughout the rest of this article, unqualified, the product is the general plain bilinear
product.

## The Criterion

**The criterion is the vanishing of the central square: a nonzero biquaternion $\tilde{Q}$ is a zero divisor of the plain product if and only if $\tilde{Q}\tilde{Q}^{\natural} = 0$.**

The criterion is a statement of the plain product, and it is labelled as such. The criterion for
the other three general products, and the reason the three have no criterion of the ring-theoretic
form, are in *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**Theorem (the criterion for the general plain bilinear product).** For the plain product, a
nonzero biquaternion $\tilde{Q}$ is a zero divisor if and only if the product
$\tilde{Q}\tilde{Q}^{\natural}$ vanishes:

$$
\tilde{Q}\tilde{Q}^{\natural} = 0.
$$

**Proof.** Suppose $\tilde{Q}_1 \neq 0$ and $\tilde{Q}_1\tilde{Q}_1^{\natural} = 0$. Then
$\tilde{Q}_1 \tilde{Q}_1^{\natural} = 0$. Since $\tilde{Q}_1 \neq 0$, we also have
$\tilde{Q}_1^{\natural} \neq 0$. So $\tilde{Q}_2 = \tilde{Q}_1^{\natural}$ is a nonzero biquaternion with
$\tilde{Q}_1\tilde{Q}_2 = 0$. Hence $\tilde{Q}_1$ is a zero divisor.

Conversely, suppose $\tilde{Q}_1$ is a zero divisor: there exists $\tilde{Q}_2 \neq 0$ with
$\tilde{Q}_1\tilde{Q}_2 = 0$. If $\tilde{Q}_1\tilde{Q}_1^{\natural} \neq 0$, then $\tilde{Q}_1$ is invertible
by the invertibility criterion, and multiplying $\tilde{Q}_1\tilde{Q}_2 = 0$ on the left by
$\tilde{Q}_1^{-1}$ gives $\tilde{Q}_2 = 0$, contradicting $\tilde{Q}_2 \neq 0$. So
$\tilde{Q}_1\tilde{Q}_1^{\natural} = 0$.

The proof uses the plain product twice: the left zero-divisor equation is the plain one, and the
inverse $\tilde{Q}^{-1}$ is the inverse of the plain product, the only one of the four general
products that has a two-sided unit. Neither ingredient is available for the other three, and that
is why the criterion is a plain-product criterion and not a general one.

## The Three-Way Classification

**Every element of the plain algebra is exactly one of three: invertible, the zero element, or a zero divisor.**

Combining the criterion for invertibility from the preceding article with the criterion for zero
divisors, the elements of $\mathbb{B}$ are partitioned into three classes: those invertible in the
plain product, the zero element, and the plain-product zero divisors.

| Condition on $\tilde{Q}\tilde{Q}^{\natural}$ | Condition on $\tilde{Q}$ | Conclusion |
|---|---|---|
| $\tilde{Q}\tilde{Q}^{\natural} \neq 0$ | (automatically $\tilde{Q} \neq 0$) | $\tilde{Q}$ is invertible |
| $\tilde{Q}\tilde{Q}^{\natural} = 0$ | $\tilde{Q} = 0$ | $\tilde{Q}$ is the zero element |
| $\tilde{Q}\tilde{Q}^{\natural} = 0$ | $\tilde{Q} \neq 0$ | $\tilde{Q}$ is a zero divisor |

The zero divisors are exactly the nonzero elements on which $\tilde{Q}\tilde{Q}^{\natural}$
vanishes. The classification is a classification of the elements of $\mathbb{B}$ by their behaviour
in the plain product, and it does not describe them under the other products.

## The Algebra Is Not a Division Algebra

**The plain algebra is not a division algebra: it has zero divisors.**

By definition, a **division algebra** is an algebra in which every nonzero element is invertible.
For the finite-dimensional algebra $\mathbb{B}$, this is equivalent to containing no zero divisors:
if every nonzero element is invertible, then no nonzero element can annihilate another; and
conversely, if there are no zero divisors, then by the criterion above every nonzero element has an
inverse.

The biquaternion algebra $\mathbb{B}$ contains zero divisors, so it is **not** a division algebra.
This is in contrast to the Frobenius theorem, which states that the only finite-dimensional
associative real division algebras are $\mathbb{R}$, $\mathbb{C}$, and $\mathbb{H}$.

## The Two Families of Zero Divisors

**The zero divisors split into two disjoint families: the pure ones ($Q_t = 0$), which are the nilpotents, and the non-pure ones ($Q_t \neq 0$), which are the complex multiples of the idempotents.**

The zero divisors split into two families according to the value of the scalar part $Q_t$. A
biquaternion is **pure** when $Q_t = 0$,

$$
\tilde{Q} = Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z, \qquad Q_x, Q_y, Q_z \in \mathbb{C},
$$

and **non-pure** when $Q_t \neq 0$. The distinction is structural, and it organizes the
classification.

The scalar part is the right invariant because the scalar imaginary $i$ is central: the scalar part
is the component of the element in the central direction, and the vector part is the component
perpendicular to it, so "pure" and "non-pure" ask whether the central component vanishes. The two
cases read the criterion $\tilde{Q}\tilde{Q}^{\natural} = Q_t^2 + (\vec Q, \vec Q) = 0$
differently — in the pure case the scalar contribution drops out, in the non-pure case it can
cancel the vector contribution — and the two resulting families are structurally distinct: a
nilpotent in the pure case, a complex multiple of an idempotent in the non-pure one, as the
sections below compute.

## Pure Zero Divisors

**A nonzero pure biquaternion is a zero divisor exactly when $Q_x^2 + Q_y^2 + Q_z^2 = 0$, and then it is a nilpotent with $\tilde{Q}^2 = 0$.**

### The Square of a Pure Biquaternion

Let $\tilde{Q} = Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z$ be a pure biquaternion. Using the product formula for
two pure biquaternions,

$$
\tilde{Q}_2 \tilde{Q} = -\sum_{\mu\in\{x,y,z\}} Q_{2\mu} Q_\mu + \sum_{\mu,\nu,\lambda\in\{x,y,z\}} \epsilon_{\mu\nu\lambda} Q_{2\mu} Q_\nu \vec e_\lambda,
$$

and setting $\tilde{Q}_2 = \tilde{Q}$, we get

$$
\tilde{Q}^2 = -\sum_{\mu\in\{x,y,z\}} Q_\mu^2 + \sum_{\mu,\nu,\lambda\in\{x,y,z\}} \epsilon_{\mu\nu\lambda} Q_\mu Q_\nu \vec e_\lambda.
$$

The vector part vanishes, because $\epsilon_{\mu\nu\lambda}$ is antisymmetric in $\mu, \nu$ while $Q_\mu Q_\nu$ is
symmetric. Therefore

$$
\tilde{Q}^2 = -(Q_x^2 + Q_y^2 + Q_z^2) e_t = -\tilde{Q}\tilde{Q}^{\natural} e_t.
$$

### The Criterion in the Pure Case

**Theorem.** The following three conditions on a nonzero pure biquaternion $\tilde{Q}$ are
equivalent:

1. $\tilde{Q}$ is a zero divisor. 2. $\tilde{Q}\tilde{Q}^{\natural} = 0$, i.e.
$Q_x^2 + Q_y^2 + Q_z^2 = 0$. 3. $\tilde{Q}^2 = 0$.

**Proof.** The equivalence of (1) and (2) is the general criterion for zero divisors. The
equivalence of (2) and (3) follows from the computation of the square above:
$\tilde{Q}^2 = -\tilde{Q}\tilde{Q}^{\natural} e_t$ vanishes if and only if
$\tilde{Q}\tilde{Q}^{\natural} = 0$.

A biquaternion satisfying $\tilde{Q}^2 = 0$ is called a **nilpotent**, written $\tilde\Upsilon$
where the nilpotency is the point (§*The nilpotent convention* of *Conventions in Mathematics*), so
in the pure case, the zero divisors are exactly the nonzero nilpotents.

### Properties

A pure zero divisor $\tilde{Q}$ has the following properties.

- **Self-annihilation.** $\tilde{Q}^2 = 0$. The annihilator of $\tilde{Q}$ contains $\tilde{Q}$ itself, and therefore contains the whole complex line spanned by $\tilde{Q}$.
- **Non-invertibility.** By the criterion for invertibility, $\tilde{Q}$ has no inverse.
- **Purity preserved.** The scalar part of $\tilde{Q}$ is zero by hypothesis, and the square $\tilde{Q}^2 = 0$ also has zero scalar part. So the property of being pure is preserved under squaring.

### The Bivector Form

A pure biquaternion has three complex coefficients, and each one splits into a real and an
imaginary part. Writing $Q_k = \rho_k + i\rho'_k$ with $\rho_k, \rho'_k \in \mathbb{R}$, and
reading each triple as a vector of $\mathbb{R}^3$, a pure biquaternion is the sum of two real
vectors carrying the central imaginary on the second,

$$
\tilde{Q} = \vec\rho + i\,\vec\rho', \qquad \vec\rho, \vec\rho' \in \mathbb{R}^3 .
$$

An element of this form is a **bivector** in the older vocabulary; the term and its setting are
recorded in *A Brief History of Biquaternions in Physics*.

Squaring and separating real and imaginary parts, using the product rule
$\vec\rho\,\vec\sigma = -\vec\rho\cdot\vec\sigma + \vec\rho\times\vec\sigma$
for two real vectors, the square of a pure biquaternion is

$$
\tilde{Q}^2 = \bigl(|\vec\rho'|^2 - |\vec\rho|^2\bigr)\, e_t - 2i\,(\vec\rho\cdot\vec\rho')\, e_t .
$$

The square is therefore a complex scalar, and it vanishes exactly when the two conditions

$$
\vec\rho\cdot\vec\rho' = 0, \qquad |\vec\rho| = |\vec\rho'|,
$$

hold. This restates the criterion proved above in real coordinates.

**Corollary (the pure zero divisors as bivectors).** A nonzero pure biquaternion
$\tilde{Q} = \vec\rho + i\vec\rho'$ is a zero divisor if and only if its two real
parts are orthogonal and of equal length. Equivalently, writing $\vec\rho = r\vec{u}$ and
$\vec\rho' = r\vec u_{v}$ with $r = |\vec\rho| = |\vec\rho'|$, the pure
zero divisors are exactly the elements

$$
r\,(\vec{u} + i\vec u_{v}), \qquad \vec{u}\cdot\vec u_{v} = 0, \qquad |\vec{u}| = |\vec u_{v}| = 1, \qquad r > 0 .
$$

The parameters are a positive radius, a real unit direction, and a perpendicular real unit
direction — one, two and one real parameters. The pure zero divisors therefore form a real cone of
dimension $4$, agreeing with the dimension recorded for the pure family below.

**Remark (the sign of the square).** The same formula shows that when the two parts are
perpendicular the square is the real scalar $|\vec\rho'|^2 - |\vec\rho|^2$:
positive, zero, or negative according as $|\vec\rho'|$ is greater than, equal to, or less
than $|\vec\rho|$. A real vector has $v^2 = -|v|^2 < 0$ without exception, so it is only a
bivector that allows a nonzero square of positive sign; this is what the reading of the theory at
its origin turns on (*A Brief History of Biquaternions in Physics*).

## Non-Pure Zero Divisors

**A zero divisor with nonzero scalar part satisfies $Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2 = 0$ and $\tilde{Q}^2 = 2 Q_t \tilde{Q}$, and it is a complex multiple of the nontrivial idempotent $\tilde\Pi = \tilde{Q}/(2 Q_t)$.**

### The Square of a Non-Pure Biquaternion

Let $\tilde{Q} = Q_t e_t + \vec Q$ with $Q_t \in \mathbb{C}$, $Q_t \neq 0$, and
$\vec Q = Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z$. Using the product formula,

$$
\tilde{Q}^2 = (Q_t^2 - (\vec Q, \vec Q)) e_t + 2 Q_t \vec Q,
$$

where $(\vec Q, \vec Q) = Q_x^2 + Q_y^2 + Q_z^2$.

### The Relation to the Scalar Part

The product $\tilde{Q}\tilde{Q}^{\natural}$ is

$$
\tilde{Q}\tilde{Q}^{\natural} = Q_t^2 + (\vec Q, \vec Q).
$$

So the condition $\tilde{Q}\tilde{Q}^{\natural} = 0$ is equivalent to

$$
(\vec Q, \vec Q) = -Q_t^2.
$$

Substituting this into the expression for $\tilde{Q}^2$:

$$
\tilde{Q}^2 = (Q_t^2 + Q_t^2) e_t + 2 Q_t \vec Q = 2 Q_t^2 e_t + 2 Q_t \vec Q = 2 Q_t (Q_t e_t + \vec Q) = 2 Q_t \tilde{Q}.
$$

So every non-pure zero divisor satisfies

$$
\tilde{Q}^2 = 2 Q_t \tilde{Q}.
$$

This is the key structural property of non-pure zero divisors: their square is a complex multiple
of themselves, with the multiplier equal to twice the scalar part.

### The Associated Idempotent

From the relation $\tilde{Q}^2 = 2 Q_t \tilde{Q}$, we divide by $2 Q_t$ (which is nonzero, since
$Q_t \neq 0$) and obtain

$$
\tilde\Pi = \frac{\tilde{Q}}{2 Q_t}, \qquad \tilde\Pi^2 = \frac{\tilde{Q}^2}{(2 Q_t)^2} = \frac{2 Q_t \tilde{Q}}{4 Q_t^2} = \frac{\tilde{Q}}{2 Q_t} = \tilde\Pi,
$$

so $\tilde\Pi$ is an **idempotent** and $\tilde{Q}$ is recovered from it by
$\tilde{Q} = 2 Q_t \tilde\Pi$: every non-pure zero divisor is a complex multiple of an idempotent.
The idempotents themselves — their classification and the dimension of the set they form — are the
subject of *Square Roots of One and the Idempotents of the Biquaternion Algebra*.

**A non-pure zero divisor is a complex scalar times a product of two nilpotents.** The idempotent
$\tilde\Pi = \tilde{Q}/(2Q_t)$ attached to a non-pure zero divisor is nontrivial, and every
nontrivial idempotent of $\mathbb{B}$ is a product of two nilpotents (*Ideals and Peirce
Decomposition of the Biquaternion Algebra*, §*Systems of Matrix Units*). Its Peirce decomposition
supplies two mixed units $u \in \tilde\Pi\mathbb{B}(e_t-\tilde\Pi)$ and
$w \in (e_t-\tilde\Pi)\mathbb{B}\tilde\Pi$, normalised so that $uw = \tilde\Pi$; both are
square-zero, $u^2 = w^2 = 0$, hence nilpotent. So

$$
\tilde{Q} = 2 Q_t\, u w, \qquad u^2 = w^2 = 0 .
$$

For the standard idempotents the factorisation is the multiplication table of the Peirce
decomposition, $\tilde\Pi_1 = \vec\Upsilon_x\vec\Upsilon_y$ and
$\tilde\Pi_2 = \vec\Upsilon_y\vec\Upsilon_x$ with $\vec\Upsilon_x^2 = \vec\Upsilon_y^2 = 0$,
so the corresponding non-pure zero divisors are $2 Q_t \vec\Upsilon_x\vec\Upsilon_y$ and
$2 Q_t \vec\Upsilon_y\vec\Upsilon_x$. The trivial idempotent $e_t$ is not a product of two
nilpotents, since a product equal to $e_t$ would make a factor a unit; the trivial idempotent $0$
is one, $0 = 0 \cdot 0$.

### Properties

A non-pure zero divisor $\tilde{Q}$ has no inverse, by the criterion for invertibility, and its
annihilator is nontrivial: the element $\tilde{Q} - 2 Q_t e_t = 2 Q_t (\tilde\Pi - e_t)$ is
annihilated by $\tilde{Q}$ on the right and on the left,

$$
\tilde{Q}(\tilde{Q} - 2 Q_t e_t) = \tilde{Q}^2 - 2 Q_t \tilde{Q} = 0, \qquad (\tilde{Q} - 2 Q_t e_t)\tilde{Q} = \tilde{Q}^2 - 2 Q_t \tilde{Q} = 0.
$$

## Structure of the Zero Divisors

**The two families are disjoint, they are separated by the vanishing of the scalar part, and their union is the whole zero-divisor set.**

The two cases are distinct in their structure.

| | Pure case ($Q_t = 0$) | Non-pure case ($Q_t \neq 0$) |
|---|---|---|
| Form | $\tilde{Q} = Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z$ | $\tilde{Q} = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z$ |
| Criterion | $Q_x^2 + Q_y^2 + Q_z^2 = 0$ | $Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2 = 0$ |
| Square | $\tilde{Q}^2 = 0$ | $\tilde{Q}^2 = 2 Q_t \tilde{Q}$ |
| Structure | Nilpotent | Complex multiple of an idempotent |
| Annihilator | Contains $\tilde{Q}$ itself | Contains $\tilde{Q} - 2 Q_t e_t$ |
| Idempotent | None | $\tilde\Pi = \tilde{Q}/(2 Q_t)$ |

The two families are **disjoint** — they are distinguished by whether the scalar part $Q_t$
vanishes, and the origin is excluded from both — and their union is the zero divisor set
$\mathcal{Z}$. As complex cones the pure family (the nilpotent cone) has complex dimension $2$ in
the three vector coefficients and real dimension $4$, and the non-pure family, being the rest of
$\mathcal{Z}$, has complex dimension $3$ and real dimension $6$.

## The Zero Divisor Set

**The zero-divisor set is the punctured complex cone $\mathcal{Z} = \{\tilde{Q} \neq 0 : \tilde{Q}\tilde{Q}^{\natural} = 0\}$, of complex dimension $3$ and real dimension $6$, the complement of the units among the nonzero elements.**

The zero divisor set $\mathcal{Z} \subset \mathbb{B}$ is

$$
\mathcal{Z} = \{\tilde{Q} \in \mathbb{B} : \tilde{Q} \neq 0, \; \tilde{Q}\tilde{Q}^{\natural} = 0\}.
$$

It is the complement of the invertible elements in the complement of the zero element,
$\mathcal{Z} = \mathbb{B} \setminus (\{0\} \cup \mathbb{B}^\times)$, and it is a cone away from the
origin: $\tilde{Q} \in \mathcal{Z}$ and $\alpha \in \mathbb{C} \setminus \{0\}$ give
$\alpha \tilde{Q} \in \mathcal{Z}$, because
$(\alpha \tilde{Q})(\alpha \tilde{Q})^{\natural} = \alpha^2 \tilde{Q}\tilde{Q}^{\natural} = 0$. The
single complex equation $\tilde{Q}\tilde{Q}^{\natural} = 0$ in the four complex coefficients is a
complex hypersurface of $\mathbb{C}^4$, so $\mathcal{Z}$ has complex dimension $3$ and real
dimension $6$.

## The Zero Divisors and the Remarkable Subspaces

**The centre, the quaternion subspace and the anti-quaternion subspace contain no zero divisor; the vector subspace contains the nilpotent cone; the two Hermitian subspaces contain a null cone; and a generic zero divisor lies in none of the remarkable subspaces.**

A zero divisor is an element on which $\tilde{Q}\tilde{Q}^{\natural}$ vanishes, so which subspaces
contain zero divisors is the question of where that polynomial vanishes. Of the remarkable
subspaces, $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$
contain none: on the centre $\tilde{Q}\tilde{Q}^{\natural} = Q_t^2$ vanishes only at
$\tilde{Q} = 0$, and on the two quaternion subspaces it is $\pm$ a sum of squares of real
coefficients, which likewise vanishes only at zero. The vector subspace $\mathrm{Vect}(\mathbb{B})$
contains the nilpotents, on which it vanishes for nonzero $\tilde{Q}$, and $\mathbb{M}_+$ and
$\mathbb{M}_-$ contain a null cone. A generic zero divisor lies in none of the remarkable
subspaces.

## Summary

The zero divisors of the biquaternion algebra are the nonzero elements on which
$\tilde{Q}\tilde{Q}^{\natural}$ vanishes. They split into two disjoint families. The **pure zero
divisors** have vanishing scalar part and satisfy $Q_x^2 + Q_y^2 + Q_z^2 = 0$; they are exactly the
nonzero nilpotents, with $\tilde{Q}^2 = 0$ and self-annihilation, and they form a complex cone of
real dimension $4$. The **non-pure zero divisors** have nonzero scalar part and satisfy
$Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2 = 0$; they are exactly the nonzero complex multiples of the
nontrivial idempotents, with $\tilde{Q}^2 = 2 Q_t \tilde{Q}$ and annihilator containing
$\tilde{Q} - 2 Q_t e_t$, and they form the rest of the zero divisor cone, of real dimension $6$.
The set is a complex cone of complex dimension $3$ (real dimension $6$) in
$\mathbb{B} \cong \mathbb{C}^4$, with the origin removed. Of the remarkable subspaces,
$\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ contain none,
$\mathrm{Vect}(\mathbb{B})$ contains the nilpotent cone, and $\mathbb{M}_+$ and $\mathbb{M}_-$
contain a null cone; a generic zero divisor lies in none of them.

The non-pure family is read on the idempotents in *Square Roots of One and the Idempotents of the
Biquaternion Algebra*, and the pure family is *Square Roots of Zero and the Nilpotents of the
Biquaternion Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | General biquaternion |
| $Q_\mu = q_\mu + i q'_\mu$ | Complex coefficient |
| $\tilde{Q}\tilde{Q}^{\natural} = 0$ | Algebraic criterion for a zero divisor |
| $\mathcal{Z}$ | Zero divisor set |
| $\tilde\Pi^2 = \tilde\Pi$ | Idempotent equation |
| $\tilde{Q}^2 = 0$ | Nilpotent equation |
| $\mathbb{C}_{\mathbb{B}}$ | Complex subspace |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion subspace |
| $\mathbb{M}_+$ | Hermitian subspace |
| $\mathbb{M}_-$ | Anti-Hermitian subspace |

## Further Reading

- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), for the product-relative definition of the zero divisor and the dictionary of the classes against the four general products.
- [Square Roots of One and the Idempotents of the Biquaternion Algebra](square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html) and [Square Roots of Zero and the Nilpotents of the Biquaternion Algebra](square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.html), for the two families of the zero-divisor set, the non-pure and the pure, and for the Peirce factorisation $\tilde{Q} = 2 Q_t\,uw$ of the non-pure family.
- [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the same set read against the four general products and the annihilators.
- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original discovery of the zero divisors and the nilpotents.
- William Rowan Hamilton, "On the Geometrical Interpretation of some Results obtained by calculation with Biquaternions," *Proceedings of the Royal Irish Academy* **5** (1853) 388–390, for the bivectors, the null-square bivectors $i + hj$ and $j + hk$, and the simplification $(1 + j + hk)^a = 1 + a(j + hk)$.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the classification of the zero divisors.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the algebraic properties of the biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- [Annihilators of the Biquaternion Algebra](annihilators-of-the-biquaternion-algebra.html), below this article in this category, the companion article, for the annihilator of an element, the two multiplication operators and their rank, and the dichotomy by the cone

