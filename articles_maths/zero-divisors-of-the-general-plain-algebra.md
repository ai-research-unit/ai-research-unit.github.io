# __Zero Divisors of the General Plain Algebra__

## Introduction

This article studies the zero divisors of the biquaternion algebra $\mathbb{B}$. It closes the element theory of the block: it follows *Biquaternion Norm and Invertibility*, which established the criterion for invertibility and the three-way classification of the elements of $\mathbb{B}$, and it uses the idempotents and the nilpotents built from that classification. The goal here is to characterize the zero divisors **of the general plain bilinear product**, to split them into two families, and to describe their structure.

A divisor is relative to a product. The definition is stated once for a general product in *Definitions for the Study of the 12 Algebraic Structures* and read on the products of the space; the unqualified "zero divisor" means "zero divisor of the general plain bilinear product", the multiplication of the general plain algebra, and every other product is named. The four general products and their common zero-divisor set are *The Zero Divisors and the Four General Products*.

Every claim is proved or stated as a definition, no physics is invoked and no examples are given. The algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$, its four conjugations and its remarkable subspaces are assumed from *Biquaternions as a Vector Space over $\mathbb{C}$* and *Introduction to the Remarkable Subspaces*, and the invertibility criterion from *Biquaternion Norm and Invertibility*. The idempotents that the non-pure family produces are *Idempotents of the General Plain Algebra*, and the nilpotents of the pure family are *Nilpotents of the General Plain Algebra*.

Throughout this article, the quaternion basis is written $e_0 = 1, e_1, e_2, e_3$, and the scalar imaginary is written $i$, so that it does not collide with the quaternion units. A general biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu \in \mathbb{C}.
$$

The quaternion conjugate is denoted $\tilde{Q}^{\natural}$, the complex conjugate is denoted $\bar{\tilde{Q}}$, the Hermitian conjugate is denoted $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$, and the anti-Hermitian conjugate is denoted $\tilde{Q}^\flat = -\tilde{Q}^{*}$. A product of the space is written $\star$ when the statement is one about an arbitrary product and only the fact that it is a product is used, as in §*Definition*; the four general products keep their signs $\tilde P\tilde Q$, $\tilde P^{\natural}\tilde Q$, $\tilde P\tilde Q^{*}$, $\tilde P^{\natural}\tilde Q^{*}$, and the general plain bilinear product, the multiplication of the algebra, is written $\tilde P\tilde Q$. The product $\tilde{Q}\tilde{Q}^{\natural}$ lies in the scalar line $\mathbb{C}_{\mathbb{B}}$; its vanishing is the algebraic condition that decides the zero divisors of the plain product, and it is never read here as a length.

## Definition

The word names a product, so the definition is stated for a general product and then read on the products of this space; it is stated once and for all in *Definitions for the Study of the 12 Algebraic Structures*. Let $\star$ be a product on $\mathbb{B}$ — any of the twelve products of *The 12 Products of the Biquaternion Complex Space*, that is one of the four general products or one of their symmetric or antisymmetric parts.

**Definition.** Let $\star$ be a product on $\mathbb{B}$ and let $\tilde Q\in\mathbb{B}$. The element $\tilde Q$ is a **left zero divisor of $\star$** when $\tilde Q\neq0$ and there is a nonzero $\tilde R$ with $\tilde Q\star\tilde R = 0$; it is a **right zero divisor of $\star$** when $\tilde Q\neq0$ and there is a nonzero $\tilde R$ with $\tilde R\star\tilde Q = 0$; and it is a **zero divisor of $\star$** when it is one or the other. An element that is both a left and a right zero divisor of $\star$ is a **two-sided zero divisor of $\star$**.

The requirement that both $\tilde{Q}$ and $\tilde{R}$ be nonzero is essential. In particular, the element $\tilde{Q} = 0$ is **not** a zero divisor of any product, even though $0\star\tilde{R} = 0$ for any $\tilde{R}$.

**On the products of the space.** Substituting the product for $\star$ gives one definition to a product. On the general plain bilinear product the two equations are $\tilde Q\tilde R = 0$ and $\tilde R\tilde Q = 0$, the classical pair; on $\tilde P^{\natural}\tilde Q$ they are $\tilde Q^{\natural}\tilde R = 0$ and $\tilde R^{\natural}\tilde Q = 0$; and the outer product has every nonzero element as a zero divisor, since $\tilde Q\wedge\tilde Q = 0$. The four general products, four different equations, happen to select the one cone $\{c = 0\}\setminus\{0\}$ described here, a coincidence of this algebra proved in *The Zero Divisors and the Four General Products*. Throughout the rest of this article, unqualified, the product is the general plain bilinear product.

## The Criterion

The criterion is a statement of the plain product, and it is labelled as such. The criterion for the other three general products, and the reason the three have no criterion of the ring-theoretic form, are in *The Zero Divisors and the Four General Products*.

**Theorem (the criterion for the general plain bilinear product).** For the plain product, a nonzero biquaternion $\tilde{Q}$ is a zero divisor if and only if the product $\tilde{Q}\tilde{Q}^{\natural}$ vanishes:

$$
\tilde{Q}\tilde{Q}^{\natural} = 0.
$$

**Proof.** Suppose $\tilde{Q} \neq 0$ and $\tilde{Q}\tilde{Q}^{\natural} = 0$. Then $\tilde{Q} \tilde{Q}^{\natural} = 0$. Since $\tilde{Q} \neq 0$, we also have $\tilde{Q}^{\natural} \neq 0$. So $\tilde{R} = \tilde{Q}^{\natural}$ is a nonzero biquaternion with $\tilde{Q}\tilde{R} = 0$. Hence $\tilde{Q}$ is a zero divisor.

Conversely, suppose $\tilde{Q}$ is a zero divisor: there exists $\tilde{R} \neq 0$ with $\tilde{Q}\tilde{R} = 0$. If $\tilde{Q}\tilde{Q}^{\natural} \neq 0$, then $\tilde{Q}$ is invertible by the invertibility criterion, and multiplying $\tilde{Q}\tilde{R} = 0$ on the left by $\tilde{Q}^{-1}$ gives $\tilde{R} = 0$, contradicting $\tilde{R} \neq 0$. So $\tilde{Q}\tilde{Q}^{\natural} = 0$.

The proof uses the plain product twice: the left zero-divisor equation is the plain one, and the inverse $\tilde{Q}^{-1}$ is the inverse of the plain product, the only one of the four general products that has a two-sided unit. Neither ingredient is available for the other three, and that is why the criterion is a plain-product criterion and not a general one.

## The Three-Way Classification

Combining the criterion for invertibility from the preceding article with the criterion for zero divisors, the elements of $\mathbb{B}$ are partitioned into three classes: those invertible in the plain product, the zero element, and the plain-product zero divisors.

| Condition on $\tilde{Q}\tilde{Q}^{\natural}$ | Condition on $\tilde{Q}$ | Conclusion |
|---|---|---|
| $\tilde{Q}\tilde{Q}^{\natural} \neq 0$ | (automatically $\tilde{Q} \neq 0$) | $\tilde{Q}$ is invertible |
| $\tilde{Q}\tilde{Q}^{\natural} = 0$ | $\tilde{Q} = 0$ | $\tilde{Q}$ is the zero element |
| $\tilde{Q}\tilde{Q}^{\natural} = 0$ | $\tilde{Q} \neq 0$ | $\tilde{Q}$ is a zero divisor |

The zero divisors are exactly the nonzero elements on which $\tilde{Q}\tilde{Q}^{\natural}$ vanishes. The classification is a classification of the elements of $\mathbb{B}$ by their behaviour in the plain product, and it does not describe them under the other products.

## The Algebra Is Not a Division Algebra

By definition, a **division algebra** is an algebra in which every nonzero element is invertible. For the finite-dimensional algebra $\mathbb{B}$, this is equivalent to containing no zero divisors: if every nonzero element is invertible, then no nonzero element can annihilate another; and conversely, if there are no zero divisors, then by the criterion above every nonzero element has an inverse.

The biquaternion algebra $\mathbb{B}$ contains zero divisors, so it is **not** a division algebra. This is in contrast to the Frobenius theorem, which states that the only finite-dimensional associative real division algebras are $\mathbb{R}$, $\mathbb{C}$, and $\mathbb{H}$.

## The Two Families of Zero Divisors

The zero divisors split into two families according to the value of the scalar part $Q_0$. A biquaternion is **pure** when $Q_0 = 0$,

$$
\tilde{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_1, Q_2, Q_3 \in \mathbb{C},
$$

and **non-pure** when $Q_0 \neq 0$. The distinction is structural, and it organizes the classification.

The scalar part is the right invariant because the scalar imaginary $i$ is central: the scalar part is the component of the element in the central direction, and the vector part is the component perpendicular to it, so "pure" and "non-pure" ask whether the central component vanishes. The two cases read the criterion $\tilde{Q}\tilde{Q}^{\natural} = Q_0^2 + (\mathbf{Q}, \mathbf{Q}) = 0$ differently — in the pure case the scalar contribution drops out, in the non-pure case it can cancel the vector contribution — and the two resulting families are structurally distinct: a nilpotent in the pure case, a complex multiple of an idempotent in the non-pure one, as the sections below compute.

## Pure Zero Divisors

### The Square of a Pure Biquaternion

Let $\tilde{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ be a pure biquaternion. Using the product formula for two pure biquaternions,

$$
\tilde{P} \tilde{Q} = -\sum_{k=1}^{3} P_k Q_k + \sum_{j,k,l=1}^{3} \epsilon_{jkl} P_j Q_k e_l,
$$

and setting $\tilde{P} = \tilde{Q}$, we get

$$
\tilde{Q}^2 = -\sum_{k=1}^{3} Q_k^2 + \sum_{j,k,l=1}^{3} \epsilon_{jkl} Q_j Q_k e_l.
$$

The vector part vanishes, because $\epsilon_{jkl}$ is antisymmetric in $j, k$ while $Q_j Q_k$ is symmetric. Therefore

$$
\tilde{Q}^2 = -(Q_1^2 + Q_2^2 + Q_3^2) e_0 = -\tilde{Q}\tilde{Q}^{\natural} e_0.
$$

### The Criterion in the Pure Case

**Theorem.** The following three conditions on a nonzero pure biquaternion $\tilde{Q}$ are equivalent:

1. $\tilde{Q}$ is a zero divisor.
2. $\tilde{Q}\tilde{Q}^{\natural} = 0$, i.e. $Q_1^2 + Q_2^2 + Q_3^2 = 0$.
3. $\tilde{Q}^2 = 0$.

**Proof.** The equivalence of (1) and (2) is the general criterion for zero divisors. The equivalence of (2) and (3) follows from the computation of the square above: $\tilde{Q}^2 = -\tilde{Q}\tilde{Q}^{\natural} e_0$ vanishes if and only if $\tilde{Q}\tilde{Q}^{\natural} = 0$.

A biquaternion satisfying $\tilde{Q}^2 = 0$ is called a **nilpotent**, written $\tilde\Upsilon$ where the nilpotency is the point (§*The nilpotent convention* of *Conventions in Mathematics*), so in the pure case, the zero divisors are exactly the nonzero nilpotents.

### Properties

A pure zero divisor $\tilde{Q}$ has the following properties.

- **Self-annihilation.** $\tilde{Q}^2 = 0$. The annihilator of $\tilde{Q}$ contains $\tilde{Q}$ itself, and therefore contains the whole complex line spanned by $\tilde{Q}$.
- **Non-invertibility.** By the criterion for invertibility, $\tilde{Q}$ has no inverse.
- **Purity preserved.** The scalar part of $\tilde{Q}$ is zero by hypothesis, and the square $\tilde{Q}^2 = 0$ also has zero scalar part. So the property of being pure is preserved under squaring.

### The Bivector Form

A pure biquaternion has three complex coefficients, and each one splits into a real and an imaginary part. Writing $Q_k = \rho_k + i\rho'_k$ with $\rho_k, \rho'_k \in \mathbb{R}$, and reading each triple as a vector of $\mathbb{R}^3$, a pure biquaternion is the sum of two real vectors carrying the central imaginary on the second,

$$
\tilde{Q} = \boldsymbol{\rho} + i\,\boldsymbol{\rho}', \qquad \boldsymbol{\rho}, \boldsymbol{\rho}' \in \mathbb{R}^3 .
$$

An element of this form is a **bivector** in the older vocabulary; the term and its setting are recorded in *A Brief History of Biquaternions in Physics*.

Squaring and separating real and imaginary parts, using the product rule $\boldsymbol{\rho}\,\boldsymbol{\sigma} = -\boldsymbol{\rho}\cdot\boldsymbol{\sigma} + \boldsymbol{\rho}\times\boldsymbol{\sigma}$ for two real vectors, the square of a pure biquaternion is

$$
\tilde{Q}^2 = \bigl(|\boldsymbol{\rho}'|^2 - |\boldsymbol{\rho}|^2\bigr)\, e_0 - 2i\,(\boldsymbol{\rho}\cdot\boldsymbol{\rho}')\, e_0 .
$$

The square is therefore a complex scalar, and it vanishes exactly when the two conditions

$$
\boldsymbol{\rho}\cdot\boldsymbol{\rho}' = 0, \qquad |\boldsymbol{\rho}| = |\boldsymbol{\rho}'|,
$$

hold. This restates the criterion proved above in real coordinates.

**Corollary (the pure zero divisors as bivectors).** A nonzero pure biquaternion $\tilde{Q} = \boldsymbol{\rho} + i\boldsymbol{\rho}'$ is a zero divisor if and only if its two real parts are orthogonal and of equal length. Equivalently, writing $\boldsymbol{\rho} = r\hat{u}$ and $\boldsymbol{\rho}' = r\hat{v}$ with $r = |\boldsymbol{\rho}| = |\boldsymbol{\rho}'|$, the pure zero divisors are exactly the elements

$$
r\,(\hat{u} + i\hat{v}), \qquad \hat{u}\cdot\hat{v} = 0, \qquad |\hat{u}| = |\hat{v}| = 1, \qquad r > 0 .
$$

The parameters are a positive radius, a real unit direction, and a perpendicular real unit direction — one, two and one real parameters. The pure zero divisors therefore form a real cone of dimension $4$, agreeing with the dimension recorded for the pure family below.

**Remark (the sign of the square).** The same formula shows that when the two parts are perpendicular the square is the real scalar $|\boldsymbol{\rho}'|^2 - |\boldsymbol{\rho}|^2$: positive, zero, or negative according as $|\boldsymbol{\rho}'|$ is greater than, equal to, or less than $|\boldsymbol{\rho}|$. A real vector has $v^2 = -|v|^2 < 0$ without exception, so it is only a bivector that allows a nonzero square of positive sign; this is what the reading of the theory at its origin turns on (*A Brief History of Biquaternions in Physics*).

## Non-Pure Zero Divisors

### The Square of a Non-Pure Biquaternion

Let $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$ with $Q_0 \in \mathbb{C}$, $Q_0 \neq 0$, and $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$. Using the product formula,

$$
\tilde{Q}^2 = (Q_0^2 - (\mathbf{Q}, \mathbf{Q})) e_0 + 2 Q_0 \mathbf{Q},
$$

where $(\mathbf{Q}, \mathbf{Q}) = Q_1^2 + Q_2^2 + Q_3^2$.

### The Relation to the Scalar Part

The product $\tilde{Q}\tilde{Q}^{\natural}$ is

$$
\tilde{Q}\tilde{Q}^{\natural} = Q_0^2 + (\mathbf{Q}, \mathbf{Q}).
$$

So the condition $\tilde{Q}\tilde{Q}^{\natural} = 0$ is equivalent to

$$
(\mathbf{Q}, \mathbf{Q}) = -Q_0^2.
$$

Substituting this into the expression for $\tilde{Q}^2$:

$$
\tilde{Q}^2 = (Q_0^2 + Q_0^2) e_0 + 2 Q_0 \mathbf{Q} = 2 Q_0^2 e_0 + 2 Q_0 \mathbf{Q} = 2 Q_0 (Q_0 e_0 + \mathbf{Q}) = 2 Q_0 \tilde{Q}.
$$

So every non-pure zero divisor satisfies

$$
\tilde{Q}^2 = 2 Q_0 \tilde{Q}.
$$

This is the key structural property of non-pure zero divisors: their square is a complex multiple of themselves, with the multiplier equal to twice the scalar part.

### The Associated Idempotent

From the relation $\tilde{Q}^2 = 2 Q_0 \tilde{Q}$, we divide by $2 Q_0$ (which is nonzero, since $Q_0 \neq 0$) and obtain

$$
\tilde\Pi = \frac{\tilde{Q}}{2 Q_0}, \qquad \tilde\Pi^2 = \frac{\tilde{Q}^2}{(2 Q_0)^2} = \frac{2 Q_0 \tilde{Q}}{4 Q_0^2} = \frac{\tilde{Q}}{2 Q_0} = \tilde\Pi,
$$

so $\tilde\Pi$ is an **idempotent** and $\tilde{Q}$ is recovered from it by $\tilde{Q} = 2 Q_0 \tilde\Pi$: every non-pure zero divisor is a complex multiple of an idempotent. The idempotents themselves — their classification and the dimension of the set they form — are the subject of *Idempotents of the General Plain Algebra*.

### Properties

A non-pure zero divisor $\tilde{Q}$ has no inverse, by the criterion for invertibility, and its annihilator is nontrivial: the element $\tilde{Q} - 2 Q_0 e_0 = 2 Q_0 (\tilde\Pi - e_0)$ is annihilated by $\tilde{Q}$ on the right and on the left,

$$
\tilde{Q}(\tilde{Q} - 2 Q_0 e_0) = \tilde{Q}^2 - 2 Q_0 \tilde{Q} = 0, \qquad (\tilde{Q} - 2 Q_0 e_0)\tilde{Q} = \tilde{Q}^2 - 2 Q_0 \tilde{Q} = 0.
$$

## Structure of the Zero Divisors

The two cases are distinct in their structure.

| | Pure case ($Q_0 = 0$) | Non-pure case ($Q_0 \neq 0$) |
|---|---|---|
| Form | $\tilde{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ | $\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ |
| Criterion | $Q_1^2 + Q_2^2 + Q_3^2 = 0$ | $Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = 0$ |
| Square | $\tilde{Q}^2 = 0$ | $\tilde{Q}^2 = 2 Q_0 \tilde{Q}$ |
| Structure | Nilpotent | Complex multiple of an idempotent |
| Annihilator | Contains $\tilde{Q}$ itself | Contains $\tilde{Q} - 2 Q_0 e_0$ |
| Idempotent | None | $\tilde\Pi = \tilde{Q}/(2 Q_0)$ |

The two families are **disjoint** — they are distinguished by whether the scalar part $Q_0$ vanishes, and the origin is excluded from both — and their union is the zero divisor set $\mathcal{Z}$. As complex cones the pure family (the nilpotent cone) has complex dimension $2$ in the three vector coefficients and real dimension $4$, and the non-pure family, being the rest of $\mathcal{Z}$, has complex dimension $3$ and real dimension $6$.

## The Zero Divisor Set

The zero divisor set $\mathcal{Z} \subset \mathbb{B}$ is

$$
\mathcal{Z} = \{\tilde{Q} \in \mathbb{B} : \tilde{Q} \neq 0, \; \tilde{Q}\tilde{Q}^{\natural} = 0\}.
$$

It is the complement of the invertible elements in the complement of the zero element, $\mathcal{Z} = \mathbb{B} \setminus (\{0\} \cup \mathbb{B}^\times)$, and it is a cone away from the origin: $\tilde{Q} \in \mathcal{Z}$ and $\alpha \in \mathbb{C} \setminus \{0\}$ give $\alpha \tilde{Q} \in \mathcal{Z}$, because $(\alpha \tilde{Q})(\alpha \tilde{Q})^{\natural} = \alpha^2 \tilde{Q}\tilde{Q}^{\natural} = 0$. The single complex equation $\tilde{Q}\tilde{Q}^{\natural} = 0$ in the four complex coefficients is a complex hypersurface of $\mathbb{C}^4$, so $\mathcal{Z}$ has complex dimension $3$ and real dimension $6$.

## The Zero Divisors and the Remarkable Subspaces

A zero divisor is an element on which $\tilde{Q}\tilde{Q}^{\natural}$ vanishes, so which subspaces contain zero divisors is the question of where that polynomial vanishes. Of the remarkable subspaces, $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ contain none: on the centre $\tilde{Q}\tilde{Q}^{\natural} = Q_0^2$ vanishes only at $\tilde{Q} = 0$, and on the two quaternion subspaces it is $\pm$ a sum of squares of real coefficients, which likewise vanishes only at zero. The vector subspace $\mathrm{Vect}(\mathbb{B})$ contains the nilpotents, on which it vanishes for nonzero $\tilde{Q}$, and $\mathbb{M}_+$ and $\mathbb{M}_-$ contain a null cone. A generic zero divisor lies in none of the remarkable subspaces.

## Summary

The zero divisors of the biquaternion algebra are the nonzero elements on which $\tilde{Q}\tilde{Q}^{\natural}$ vanishes. They split into two disjoint families. The **pure zero divisors** have vanishing scalar part and satisfy $Q_1^2 + Q_2^2 + Q_3^2 = 0$; they are exactly the nonzero nilpotents, with $\tilde{Q}^2 = 0$ and self-annihilation, and they form a complex cone of real dimension $4$. The **non-pure zero divisors** have nonzero scalar part and satisfy $Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = 0$; they are exactly the nonzero complex multiples of the nontrivial idempotents, with $\tilde{Q}^2 = 2 Q_0 \tilde{Q}$ and annihilator containing $\tilde{Q} - 2 Q_0 e_0$, and they form the rest of the zero divisor cone, of real dimension $6$. The set is a complex cone of complex dimension $3$ (real dimension $6$) in $\mathbb{B} \cong \mathbb{C}^4$, with the origin removed. Of the remarkable subspaces, $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ contain none, $\mathrm{Vect}(\mathbb{B})$ contains the nilpotent cone, and $\mathbb{M}_+$ and $\mathbb{M}_-$ contain a null cone; a generic zero divisor lies in none of them.

The non-pure family is read on the idempotents in *Idempotents of the General Plain Algebra*, and the pure family is *Nilpotents of the General Plain Algebra*.

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

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the product-relative definition of the zero divisor and the dictionary of the classes against the four general products.
- *Idempotents of the General Plain Algebra* (`articles_maths/idempotents-of-the-general-plain-algebra.md`) and *Nilpotents of the General Plain Algebra* (`articles_maths/nilpotents-of-the-general-plain-algebra.md`), for the two families of the zero-divisor set, the non-pure and the pure.
- *The Zero Divisors and the Four General Products* (`articles_maths/the-zero-divisors-and-the-four-general-products.md`) and *The Annihilating Elements of the Four General Products* (`articles_maths/the-annihilating-elements-of-the-four-general-products.md`), for the same set read against the four general products and the annihilators.
- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original discovery of the zero divisors and the nilpotents.
- William Rowan Hamilton, "On the Geometrical Interpretation of some Results obtained by calculation with Biquaternions," *Proceedings of the Royal Irish Academy* **5** (1853) 388–390, for the bivectors, the null-square bivectors $i + hj$ and $j + hk$, and the simplification $(1 + j + hk)^a = 1 + a(j + hk)$.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the classification of the zero divisors.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the algebraic properties of the biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.

