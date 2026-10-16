# __Zero Divisors of the Quaternion Algebra__

## Introduction

This article studies the zero divisors of the quaternion algebra $\mathbb{H}$. It follows *Norm and
Invertibility in the Quaternion Algebra*, above this article in this category, which established
the criterion for invertibility and the three-way classification of the elements of $\mathbb{H}$, and
it opens the element theory of the block: the zero divisors of the complexified block, of the
idempotent and the nilpotent type, are *Zero Divisors of the Biquaternion Algebra*, in the
neighbouring *Biquaternion* category, and the vocabulary of pure and non-pure is used throughout. The goal here is to characterise the zero
divisors **of the quaternion product**, to name the two families the complexified theory
separates, and to prove that over $\mathbb{R}$ both are empty.

A divisor is relative to a product. The definition is stated once for a general product in *Algebras: A General Introduction*; the unqualified "zero divisor" means "zero divisor of the quaternion product", the multiplication of the quaternion algebra.

Every claim is proved or stated as a definition, no physics is invoked and no examples are given.
The algebra $\mathbb{H}$, its natural conjugation and its remarkable subspaces are assumed from
*Introduction to the Quaternion Algebra* and *Introduction to the Remarkable Subspaces of the Quaternions*,
and the invertibility criterion and the quaternion norm from *Norm and Invertibility in the General
Plain Algebra*. The annihilator of an element, the two multiplication operators and their rank are
*Annihilators of the Quaternion Algebra*, below this article in this category.

## Conventions

Throughout this article the quaternion basis is written $e_0 = 1, e_1, e_2, e_3$, with
$e_k^2 = -e_0$ and $e_1e_2 = e_3$, $e_2e_3 = e_1$, $e_3e_1 = e_2$. A general quaternion is

$$
\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3 = q_0 e_0 + \vec q,
\qquad \vec q = q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q_\mu \in \mathbb{R},
$$

with **scalar part** $q_0 = \mathrm{Sc}(\tilde q)$ and **vector part** $\vec q$. The natural
conjugation is $\tilde q^{\natural} = q_0 e_0 - \vec q$. Over $\mathbb{R}$ the bar is the identity
and the star coincides with the natural conjugation, so the chapter has exactly two general products,
the plain one $\tilde p\tilde q$ and the quaternionic one $\tilde p^{\natural}\tilde q$; the plain
product is the one of this article. A product of the space is written $\star$ when the statement is
one about an arbitrary product and only the fact that it is a product is used, as in §*Definition*.

The plain form is $\langle\tilde p,\tilde q\rangle = \mathrm{Sc}(\tilde p\tilde q) = p_0q_0 - (\vec p,\vec q)$,
indefinite of signature $(1,3)$; the quaternion form is
$\langle\tilde p,\tilde q\rangle_{\natural} = \mathrm{Sc}(\tilde p^{\natural}\tilde q) = p_0q_0 + (\vec p,\vec q)$,
positive definite. The **quaternion norm** is
$\langle\tilde q\rangle_{\natural} = \tilde q\tilde q^{\natural} = \tilde q^{\natural}\tilde q = q_0^2 + |\vec q|^2$,
a positive real vanishing only at $\tilde q = 0$, and it is multiplicative,
$\langle\tilde p\tilde q\rangle_{\natural} = \langle\tilde p\rangle_{\natural}\langle\tilde q\rangle_{\natural}$, by *Norm and Invertibility in the Quaternion Algebra*, above this article in this category. The centre is the scalar line $\mathbb{R}e_0$; the
vector subspace is $\mathrm{Vect}(\mathbb{H}) = \{\vec q\}$, of dimension three.

## Definition

**Definition.** Let $\star$ be a product on $\mathbb{H}$ and let $\tilde q\in\mathbb{H}$. The element
$\tilde q$ is a **left zero divisor of $\star$** when $\tilde q\neq0$ and there is a nonzero
$\tilde r$ with $\tilde q\star\tilde r = 0$; it is a **right zero divisor of $\star$** when
$\tilde q\neq0$ and there is a nonzero $\tilde r$ with $\tilde r\star\tilde q = 0$; and it is a
**zero divisor of $\star$** when it is one or the other. An element that is both a left and a right
zero divisor of $\star$ is a **two-sided zero divisor of $\star$**.

The requirement that both $\tilde q$ and $\tilde r$ be nonzero is essential. In particular, the
element $\tilde q = 0$ is **not** a zero divisor of any product, even though
$0\star\tilde r = 0$ for any $\tilde r$.

**On the products of the space.** Substituting the product for $\star$ gives one definition to a
product. On the quaternion product the two equations are $\tilde q\tilde r = 0$ and
$\tilde r\tilde q = 0$; on $\tilde p^{\natural}\tilde q$ they are $\tilde q^{\natural}\tilde r = 0$
and $\tilde r^{\natural}\tilde q = 0$; and the cross product has every nonzero element as a zero
divisor, since $\tilde q\wedge\tilde q = 0$. Throughout the rest of this article, unqualified, the
product is the quaternion product. A product that has a two-sided unit and no zero
divisor is a **division rule**, and an algebra whose product is a division rule is a **division
algebra**; the theorem of §*The Criterion Is Never Satisfied Off the Origin* shows that the plain
product is one, so every nonzero element of the quaternion product is a unit.

## The Criterion

The complexified block decides its zero divisors by the vanishing of $\tilde Q\tilde Q^{\natural}$,
and the same criterion holds here, but its conclusion is reversed by the positivity of the norm.

**Theorem (the criterion for the quaternion product).** For the quaternion product, a nonzero
quaternion $\tilde q$ is a zero divisor if and only if the product $\tilde q\tilde q^{\natural}$
vanishes:

$$
\tilde q\tilde q^{\natural} = 0.
$$

**Proof.** Suppose $\tilde q \neq 0$ and $\tilde q\tilde q^{\natural} = 0$. Since $\tilde q \neq 0$
we also have $\tilde q^{\natural} \neq 0$. So $\tilde r = \tilde q^{\natural}$ is a nonzero
quaternion with $\tilde q\tilde r = 0$, and $\tilde q$ is a zero divisor.

Conversely, suppose $\tilde q$ is a zero divisor: there is a nonzero $\tilde r$ with
$\tilde q\tilde r = 0$ or with $\tilde r\tilde q = 0$. If $\tilde q\tilde q^{\natural} \neq 0$ then
$\tilde q$ is invertible by the invertibility criterion. In the first case multiplying
$\tilde q\tilde r = 0$ on the left by $\tilde q^{-1}$ gives $\tilde r = 0$; in the second case
multiplying $\tilde r\tilde q = 0$ on the right by $\tilde q^{-1}$ gives $\tilde r = 0$. Either way a
contradiction, so $\tilde q\tilde q^{\natural} = 0$.

The proof uses the quaternion product twice: the zero-divisor equation is the plain one, and the inverse
is the inverse of the quaternion product, the only one of the two general products that has a two-sided
unit. Neither ingredient is available for the quaternionic product, and that is why the criterion is
a plain-product criterion.

## The Criterion Is Never Satisfied Off the Origin

Over $\mathbb{R}$ the criterion has no solution away from the origin, because the product
$\tilde q\tilde q^{\natural}$ is the quaternion norm.

**Theorem (the zero-divisor set is empty).** For the quaternion product, the only
quaternion with $\tilde q\tilde q^{\natural} = 0$ is $\tilde q = 0$. Consequently $\mathbb{H}$ has no
zero divisor: $\tilde p\tilde q = 0$ forces $\tilde p = 0$ or $\tilde q = 0$.

**Proof.** By the quaternion norm, $\tilde q\tilde q^{\natural} = q_0^2 + q_1^2 + q_2^2 + q_3^2$, a
sum of squares of real numbers. It vanishes only when every $q_\mu$ vanishes, that is at
$\tilde q = 0$. Since a zero divisor is required to be nonzero, and every nonzero $\tilde q$ has
$\tilde q\tilde q^{\natural} > 0$, the criterion admits no element. For the annihilating equation, if
$\tilde p\tilde q = 0$ with $\tilde q \neq 0$, multiplying on the right by $\tilde q^{-1}$ gives
$\tilde p = 0$; the case $\tilde p \neq 0$ is the same with the inverse on the left.

## The Three-Way Classification

Combining the criterion for invertibility from the preceding article with the criterion for zero
divisors, the elements of $\mathbb{H}$ are partitioned into three classes, and over $\mathbb{R}$ the
middle class collapses.

| Condition on $\tilde q\tilde q^{\natural}$ | Condition on $\tilde q$ | Conclusion |
|---|---|---|
| $\tilde q\tilde q^{\natural} \neq 0$ | (automatically $\tilde q \neq 0$) | $\tilde q$ is invertible |
| $\tilde q\tilde q^{\natural} = 0$ | $\tilde q = 0$ | $\tilde q$ is the zero element |
| $\tilde q\tilde q^{\natural} = 0$ | $\tilde q \neq 0$ | $\tilde q$ is a zero divisor |

The third row is empty: the second row exhausts the vanishing of $\tilde q\tilde q^{\natural}$. The
classification therefore has the same three slots as the complexified block but one of them is empty,
and every nonzero quaternion lies in the first row. This is the classification table of *Norm and
Invertibility in the Quaternion Algebra*, above this article in this category, read against the
criterion.

## The Algebra Is a Division Algebra

By the vocabulary of *Algebras: A General Introduction*, a product with no
zero divisor and a two-sided unit is a **division rule**, and an algebra whose product is a division
rule is a **division algebra**. For the finite-dimensional algebra $\mathbb{H}$, the two clauses of
the criterion agree: if every nonzero element is invertible then no nonzero element can annihilate
another, and conversely if there are no zero divisors then every nonzero element has an inverse by
the criterion above.

The quaternion algebra $\mathbb{H}$ contains no zero divisors, so it is a **division algebra**. This
is the point at which the real block separates from the complexified one: the biquaternion algebra
$\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries a genuine hypersurface of zero
divisors, while $\mathbb{H}$ carries none. The reason is exactly the signature of the two norms. The
biquaternion norm is the same sum of squares $\sum_\mu Q_\mu^2$, but computed in the complex
coefficients, so it vanishes on a complex cone of real dimension six; over $\mathbb{R}$ the same
expression is a sum of squares of real numbers and is positive definite, so the cone shrinks to the
origin.

**Theorem (Frobenius).** Every finite-dimensional associative division algebra over $\mathbb{R}$ is
isomorphic to $\mathbb{R}$, $\mathbb{C}$ or $\mathbb{H}$.

*Proof.* Quoted as standard. The dimension count is $1,2,4$, and $\mathbb{H}$ is the
largest-dimensional associative one; the statement and its companions are *The Specificities of the
Quaternion Algebra*, below this article in this category.

## The Two Families of the Complexified Block

The complexified block splits its zero divisors into two families according to the value of the
scalar part $Q_0$. A biquaternion is **pure** when $Q_0 = 0$ and **non-pure** when $Q_0 \neq 0$, and
the criterion reads differently in the two cases. Writing $\tilde Q = Q_0 e_0 + \vec Q$ with
$\vec Q$ a complex vector part,

$$
\tilde Q\tilde Q^{\natural} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = Q_0^2 + (\vec Q,\vec Q),
$$

so in the pure case the scalar contribution drops out and the condition is the isotropy of the
complex vector part, while in the non-pure case the scalar contribution can cancel the vector one.
The pure zero divisors are the nonzero nilpotents and the non-pure ones are the nonzero complex
multiples of the idempotents.

Over $\mathbb{R}$ the two families inherit the split but lose their elements, and for the same reason
in both cases: the criterion becomes the vanishing of a sum of squares of real coefficients.

**Proposition (the pure family is empty).** A pure quaternion $\vec p$ has
$\vec p\vec p^{\natural} = |\vec p|^2 e_0$ and $\vec p^2 = -|\vec p|^2 e_0$, so

$$
\vec p^2 = 0 \quad\Longleftrightarrow\quad |\vec p|^2 = p_1^2 + p_2^2 + p_3^2 = 0
\quad\Longleftrightarrow\quad \vec p = 0.
$$

So there is no nonzero pure zero divisor, and the pure family of the complexified block has no real
member.

**Proof.** For a pure quaternion the product with its conjugate is
$\vec p\vec p^{\natural} = |\vec p|^2 e_0$ and the square is
$\vec p^2 = -(\vec p,\vec p)e_0 = -|\vec p|^2 e_0$, as the coordinate rule gives directly.
A sum of three squares of real numbers vanishes only at $\vec p = 0$.

**Proposition (the non-pure family is empty).** A quaternion with $q_0 \neq 0$ has

$$
\tilde q\tilde q^{\natural} = q_0^2 + |\vec q|^2 \geq q_0^2 > 0,
$$

so it satisfies the criterion at no point. There is no non-pure zero divisor.

**Proof.** The scalar contribution $q_0^2$ is strictly positive and the vector contribution
$|\vec q|^2$ is nonnegative; their sum cannot vanish when $q_0 \neq 0$.

**Corollary.** Both families of the complexified block are empty over $\mathbb{R}$, and the
zero-divisor set of the quaternion product is empty. The two families, read on the real algebra, are the
classes of *Idempotents of the Quaternion Algebra* and *Nilpotents of the Quaternion Algebra*,
below this article in this category: the idempotent class is the pair $\{0, e_0\}$, and the nilpotent
class is empty, with square-zero set the single point $0$.

## The Zero Divisor Set

The zero divisor set $\mathcal{Z} \subset \mathbb{H}$ is

$$
\mathcal{Z} = \{\tilde q \in \mathbb{H} : \tilde q \neq 0, \; \tilde q\tilde q^{\natural} = 0\} = \varnothing.
$$

It is the complement of the invertible elements in the complement of the zero element,
$\mathcal{Z} = \mathbb{H} \setminus (\{0\} \cup \mathbb{H}^\times)$, and here that complement is empty
because $\mathbb{H}^\times = \mathbb{H}\setminus\{0\}$.

The complexified block reads the same formula as a complex hypersurface: the single complex equation
$\tilde Q\tilde Q^{\natural} = 0$ in the four complex coefficients has complex dimension $3$ and real
dimension $6$. Over $\mathbb{R}$ the equation is the quadratic form
$q_0^2 + q_1^2 + q_2^2 + q_3^2 = 0$, whose real vanishing locus is the single point $0$; the origin is
excluded from the zero-divisor set by the requirement that the element be nonzero, and what is left is
nothing. The cone of the complexified block meets the real space only at the origin.

**Remark (the cone is a point, and the point is excluded).** The comparison is worth stating in one
line. In $\mathbb{C}^4$ the equation cuts a three-complex-dimensional cone with the origin removed;
in $\mathbb{R}^4$ the same equation cuts the origin alone, and the definition of the zero divisor
removes it. The dimension drop is not a loss of rigour but the whole content of positive
definiteness: the biquaternion norm can vanish on a nonzero element, the quaternion norm cannot.

## The Zero Divisors and the Remarkable Subspaces

A zero divisor is an element on which $\tilde q\tilde q^{\natural}$ vanishes, so which subspaces
contain zero divisors is the question of where the norm vanishes. Of the remarkable subspaces, the
centre $\mathbb{R}e_0$ contains none: on the centre $\langle s e_0\rangle_{\natural} = s^2$ vanishes only at $s = 0$. The
vector subspace $\mathrm{Vect}(\mathbb{H})$ contains none: on it $\langle \vec q\rangle_{\natural} = |\vec q|^2$
vanishes only at $\vec q = 0$. No other subspace is any different, the norm being positive
definite on the whole space. So every remarkable subspace is free of zero divisors, and the only
element of the space on which the criterion is satisfied is the origin, which is not a zero divisor by
the definition of §*Definition*. The reading on the two subspaces is *Introduction to the Remarkable
Subspaces of the Quaternions*, and the two restrictions of the norm are read in *Norm and Invertibility in the Quaternion Algebra*.

## Summary

The zero divisors of the quaternion algebra are the nonzero elements on which
$\tilde q\tilde q^{\natural}$ vanishes. Over $\mathbb{R}$ that product is the quaternion norm
$q_0^2 + q_1^2 + q_2^2 + q_3^2$, a sum of squares of real numbers, so it vanishes only at the origin;
the criterion admits no element, the zero divisor set is the **empty set**, and the algebra is a
**division algebra**. The three-way classification of the elements keeps its invertible and zero
slots and loses its zero-divisor slot, and every nonzero quaternion is a unit,
$\tilde q^{-1} = \tilde q^{\natural}/\langle\tilde q\rangle_{\natural}$.

This is the opposite of the complexified block, whose zero divisors form the punctured complex cone
$\{N = 0\}$ of complex dimension three and real dimension six, split into the pure nilpotent family
and the non-pure idempotent family. The complexified cone is empty over $\mathbb{R}$ because the
quaternion norm is positive definite, and the two families read on the real algebra are the classes of
*Idempotents of the Quaternion Algebra* and *Nilpotents of the Quaternion Algebra*, below this
article in this category: the idempotents are $0$ and $e_0$, and the nilpotent class is empty, its
square-zero set being the single point $0$. Of the
remarkable subspaces, the centre and the vector subspace contain none, and no nonzero element of
either is a zero divisor.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra |
| $\tilde q = \sum_\mu q_\mu e_\mu$ | General quaternion |
| $\tilde q^{\natural} = q_0 e_0 - \vec q$ | Natural conjugation |
| $\langle\tilde q\rangle_{\natural} = \tilde q\tilde q^{\natural} = \sum_\mu q_\mu^2$ | Quaternion norm, positive definite over $\mathbb{R}$ |
| $\tilde q\tilde q^{\natural} = 0$ | Algebraic criterion for a zero divisor |
| $\mathcal{Z} = \varnothing$ | Zero divisor set |
| $\tilde\Pi^2 = \tilde\Pi$ | Idempotent equation |
| $\tilde q^2 = 0$ | Square-zero equation |
| $\mathbb{R}e_0$ | The centre, the scalar line |
| $\mathrm{Vect}(\mathbb{H})$ | The vector subspace |

## Further Reading

- *Norm and Invertibility in the Quaternion Algebra* (`articles_maths/norm-and-invertibility-in-the-quaternion-algebra.md`), for the quaternion norm, its multiplicativity, the invertibility criterion and the division property.
- *Square Roots of One and the Idempotents of the Quaternion Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-quaternion-algebra.md`) and *Square Roots of Zero and the Nilpotents of the Quaternion Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-quaternion-algebra.md`), below this article in this category, for the two classes that the complexified zero-divisor families become over $\mathbb{R}$.
- *Annihilators of the Quaternion Algebra* (`articles_maths/annihilators-of-the-quaternion-algebra.md`), below this article in this category, for the annihilator of an element, the two multiplication operators and their rank.
- *Zero Divisors of the Biquaternion Algebra* (`articles_maths/zero-divisors-of-the-biquaternion-algebra.md`), the complexified counterpart, for the punctured cone, its two families and the criterion in the complex coefficients.
- *The Specificities of the Quaternion Algebra* (`articles_maths/the-specificities-of-the-quaternion-algebra.md`), below this article in this category, for the folding of the empty classes.
- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the origin of the quaternion product and its norm.
- Leonard Dickson, *Algebras and Their Arithmetics* (University of Chicago Press, 1923), for the division property and the structure of the quaternion algebra.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for zero divisors, regular elements and the structure theory of finite-dimensional algebras.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for division rings, their units and their absence of zero divisors.
