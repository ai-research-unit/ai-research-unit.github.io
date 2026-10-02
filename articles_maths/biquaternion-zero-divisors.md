# __Biquaternion Zero Divisors__

## Introduction

This article studies the zero divisors of the biquaternion algebra $\mathbb{B}$. It follows *Biquaternion Norm and Invertibility*, which established the criterion for invertibility and the three-way classification of the elements of $\mathbb{B}$. The goal here is to characterize the zero divisors, to split them into two families, and to describe their structure.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra. The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is assumed from the article on biquaternion algebra, together with its four conjugations and its six distinguished subspaces. The invertibility criterion is assumed from the article on biquaternion norm and invertibility. The classification of the roots of $-1$ is assumed from the article on biquaternion roots of minus one. The idempotent classification that depends on it is the subject of *Biquaternion Idempotents and Projections*, and the roots themselves are not restated here.

Throughout this article, the quaternion basis is written $e_0 = 1, e_1, e_2, e_3$, and the scalar imaginary is written $i$, so that it does not collide with the quaternion units. A general biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu \in \mathbb{C}.
$$

The quaternion conjugate is denoted $\tilde{Q}^{\natural}$, the complex conjugate is denoted $\bar{\tilde{Q}}$, the Hermitian conjugate is denoted $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$, and the anti-Hermitian conjugate is denoted $\tilde{Q}^\flat = -\tilde{Q}^{*}$. The product $\tilde{Q}\tilde{Q}^{\natural}$ lies in the scalar line $\mathbb{C}_{\mathbb{B}}$; its vanishing is the algebraic condition that decides the zero divisors, and it is never read here as a length.

## Definition and Criterion

### Definition

A biquaternion $\tilde{Q}$ is a **zero divisor** if it is **nonzero** and there exists a **nonzero** biquaternion $\tilde{R}$ such that

$$
\tilde{Q} \circ \tilde{R} = 0 \quad \text{or} \quad \tilde{R} \circ \tilde{Q} = 0.
$$

The requirement that both $\tilde{Q}$ and $\tilde{R}$ be nonzero is essential. In particular, the element $\tilde{Q} = 0$ is **not** a zero divisor, even though $0 \circ \tilde{R} = 0$ for any $\tilde{R}$.

### Criterion

**Theorem.** A nonzero biquaternion $\tilde{Q}$ is a zero divisor if and only if the product $\tilde{Q}\tilde{Q}^{\natural}$ vanishes:

$$
\tilde{Q}\tilde{Q}^{\natural} = 0.
$$

**Proof.** Suppose $\tilde{Q} \neq 0$ and $\tilde{Q}\tilde{Q}^{\natural} = 0$. Then $\tilde{Q} \tilde{Q}^{\natural} = 0$. Since $\tilde{Q} \neq 0$, we also have $\tilde{Q}^{\natural} \neq 0$. So $\tilde{R} = \tilde{Q}^{\natural}$ is a nonzero biquaternion with $\tilde{Q} \circ \tilde{R} = 0$. Hence $\tilde{Q}$ is a zero divisor.

Conversely, suppose $\tilde{Q}$ is a zero divisor: there exists $\tilde{R} \neq 0$ with $\tilde{Q} \circ \tilde{R} = 0$. If $\tilde{Q}\tilde{Q}^{\natural} \neq 0$, then $\tilde{Q}$ is invertible by the invertibility criterion, and multiplying $\tilde{Q} \circ \tilde{R} = 0$ on the left by $\tilde{Q}^{-1}$ gives $\tilde{R} = 0$, contradicting $\tilde{R} \neq 0$. So $\tilde{Q}\tilde{Q}^{\natural} = 0$.

### The Three-Way Classification

Combining the criterion for invertibility from the preceding article with the criterion for zero divisors, the elements of $\mathbb{B}$ are partitioned into three classes:

| Condition on $\tilde{Q}\tilde{Q}^{\natural}$ | Condition on $\tilde{Q}$ | Conclusion |
|---|---|---|
| $\tilde{Q}\tilde{Q}^{\natural} \neq 0$ | (automatically $\tilde{Q} \neq 0$) | $\tilde{Q}$ is invertible |
| $\tilde{Q}\tilde{Q}^{\natural} = 0$ | $\tilde{Q} = 0$ | $\tilde{Q}$ is the zero element |
| $\tilde{Q}\tilde{Q}^{\natural} = 0$ | $\tilde{Q} \neq 0$ | $\tilde{Q}$ is a zero divisor |

The zero divisors are exactly the nonzero elements on which $\tilde{Q}\tilde{Q}^{\natural}$ vanishes.

### The Algebra Is Not a Division Algebra

By definition, a **division algebra** is an algebra in which every nonzero element is invertible. For the finite-dimensional algebra $\mathbb{B}$, this is equivalent to containing no zero divisors: if every nonzero element is invertible, then no nonzero element can annihilate another; and conversely, if there are no zero divisors, then by the criterion above every nonzero element has an inverse.

The biquaternion algebra $\mathbb{B}$ contains zero divisors, so it is **not** a division algebra. This is in contrast to the Frobenius theorem, which states that the only finite-dimensional associative real division algebras are $\mathbb{R}$, $\mathbb{C}$, and $\mathbb{H}$.

## The Two Families of Zero Divisors

The zero divisors split into two families according to the value of the scalar part $Q_0$. The distinction is structural, and it is the organizing principle of the classification.

### The Pure Case

A biquaternion is **pure** if its scalar part vanishes:

$$
\tilde{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_1, Q_2, Q_3 \in \mathbb{C}.
$$

The pure case is studied in the section on pure zero divisors below.

### The Non-Pure Case

A biquaternion is **non-pure** if its scalar part is nonzero:

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_0 \in \mathbb{C}, \; Q_0 \neq 0.
$$

The non-pure case is studied in the section on non-pure zero divisors below.

### Why the Scalar Part Is the Right Invariant

The scalar part is the natural invariant because the scalar imaginary $i$ is central in $\mathbb{B}$: the scalar part is the component of the element in the central direction, and the vector part is the component perpendicular to it. The two cases of zero divisors — pure and non-pure — are distinguished by whether this central component vanishes.

In the **pure case**, the product $\tilde{Q}\tilde{Q}^{\natural}$ reduces to

$$
\tilde{Q}\tilde{Q}^{\natural} = (\mathbf{Q}, \mathbf{Q}) = Q_1^2 + Q_2^2 + Q_3^2,
$$

a complex scalar. The vanishing of $\tilde{Q}\tilde{Q}^{\natural}$ is the condition $(\mathbf{Q}, \mathbf{Q}) = 0$, which has nontrivial complex solutions (the nilpotents).

In the **non-pure case**, the product $\tilde{Q}\tilde{Q}^{\natural}$ contains the scalar contribution $Q_0^2$ in addition to the vector contribution:

$$
\tilde{Q}\tilde{Q}^{\natural} = Q_0^2 + (\mathbf{Q}, \mathbf{Q}),
$$

and the vanishing condition allows the scalar and vector contributions to cancel. The resulting solutions are the complex multiples of the idempotents.

The two cases are structurally distinct, and they lead to two different families of zero divisors.

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

### The Criterion

**Theorem.** The following three conditions on a nonzero pure biquaternion $\tilde{Q}$ are equivalent:

1. $\tilde{Q}$ is a zero divisor.
2. $\tilde{Q}\tilde{Q}^{\natural} = 0$, i.e. $Q_1^2 + Q_2^2 + Q_3^2 = 0$.
3. $\tilde{Q}^2 = 0$.

**Proof.** The equivalence of (1) and (2) is the general criterion for zero divisors. The equivalence of (2) and (3) follows from the computation of the square above: $\tilde{Q}^2 = -\tilde{Q}\tilde{Q}^{\natural} e_0$ vanishes if and only if $\tilde{Q}\tilde{Q}^{\natural} = 0$.

A biquaternion satisfying $\tilde{Q}^2 = 0$ is called a **nilpotent**, so in the pure case, the zero divisors are exactly the nonzero nilpotents.

### Properties

A pure zero divisor $\tilde{Q}$ has the following properties.

- **Self-annihilation.** $\tilde{Q} \circ \tilde{Q} = 0$. The annihilator of $\tilde{Q}$ contains $\tilde{Q}$ itself, and therefore contains the whole complex line spanned by $\tilde{Q}$.
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

The parameters are a positive radius, a direction on the unit sphere, and a perpendicular direction on its unit circle — one, two and one real parameters. The pure zero divisors therefore form a real cone of dimension $4$, agreeing with the dimension recorded for the pure family below.

**Remark (the sign of the square).** The same formula shows that when the two parts are perpendicular the square is the real scalar $|\boldsymbol{\rho}'|^2 - |\boldsymbol{\rho}|^2$: positive, zero, or negative according as $|\boldsymbol{\rho}'|$ is greater than, equal to, or less than $|\boldsymbol{\rho}|$. A real vector has $v^2 = -|v|^2 < 0$ without exception, so it is only a bivector that allows a nonzero square of positive sign; this is what the geometric reading of the theory at its origin turns on (*A Brief History of Biquaternions in Physics*).

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

so $\tilde\Pi$ is an **idempotent** and $\tilde{Q}$ is recovered from it by $\tilde{Q} = 2 Q_0 \tilde\Pi$: every non-pure zero divisor is a complex multiple of an idempotent. The idempotents themselves — their classification, their bijection with the roots of $-1$, and the dimension of the set they form — are the subject of *Biquaternion Idempotents and Projections*.

### Properties

A non-pure zero divisor $\tilde{Q}$ has the following properties.

- **Form.** $\tilde{Q} = 2 Q_0 \tilde\Pi$ with $\tilde\Pi$ idempotent. So the zero divisor is a complex multiple of an idempotent.
- **Square.** $\tilde{Q}^2 = 2 Q_0 \tilde{Q}$. This is a complex multiple of $\tilde{Q}$ itself, with the multiplier being twice the scalar part.
- **Non-invertibility.** By the criterion for invertibility, $\tilde{Q}$ has no inverse.
- **Nontrivial annihilator.** The element $\tilde{Q} - 2 Q_0 e_0 = 2 Q_0 (\tilde\Pi - e_0)$ is annihilated by $\tilde{Q}$ on the right and on the left:

$$
\tilde{Q} \circ (\tilde{Q} - 2 Q_0 e_0) = \tilde{Q}^2 - 2 Q_0 \tilde{Q} = 0,
$$

$$
(\tilde{Q} - 2 Q_0 e_0) \circ \tilde{Q} = \tilde{Q}^2 - 2 Q_0 \tilde{Q} = 0.
$$

## The Roots of Minus One

The non-pure zero divisors are complex multiples of idempotents, and the idempotents are classified by the roots of $-1$. Those roots are classified in *Biquaternion Square Roots of Minus One, Zero and Plus One*, and the resulting classification of the idempotents is the subject of *Biquaternion Idempotents and Projections*; neither is restated here.

## Distribution of the Zero Divisors

A zero divisor is an element on which $\tilde{Q}\tilde{Q}^{\natural}$ vanishes, so which subspaces contain zero divisors is the algebraic question of where that polynomial vanishes. Algebraically: $\mathbb{C}_{\mathbb{B}}$ and $\mathbb{H}_{\mathbb{B}}$ contain none, since $\tilde{Q}\tilde{Q}^{\natural}$ is a sum of squares of real coefficients there and vanishes only at $\tilde{Q}=0$; $\mathrm{Vect}(\mathbb{B})$ and $i\mathbb{H}_{\mathbb{B}}$ contain the nilpotents, on which it vanishes for nonzero $\tilde{Q}$; and $\mathbb{M}_+$ and $\mathbb{M}_-$ contain a null cone.

## Structure of the Zero Divisors

We now summarize the structure of the zero divisors of $\mathbb{B}$ in terms of the pure/non-pure distinction.

### The Pure Case

A pure biquaternion $\tilde{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ is a zero divisor if and only if

$$
Q_1^2 + Q_2^2 + Q_3^2 = 0,
$$

and in that case $\tilde{Q}^2 = 0$. So the pure zero divisors are exactly the nonzero nilpotents. They form the zero divisors whose scalar part vanishes.

### The Non-Pure Case

A non-pure biquaternion $\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ with $Q_0 \neq 0$ is a zero divisor if and only if $\tilde{Q}\tilde{Q}^{\natural} = 0$, and in that case

$$
\tilde{Q}^2 = 2 Q_0 \tilde{Q}.
$$

So the non-pure zero divisors are exactly the nonzero complex multiples of the nontrivial idempotents of $\mathbb{B}$. They form the zero divisors whose scalar part is nonzero.

### The Comparison Table

The two cases are distinct in their structure:

| | Pure case ($Q_0 = 0$) | Non-pure case ($Q_0 \neq 0$) |
|---|---|---|
| Form | $\tilde{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ | $\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ |
| Criterion | $Q_1^2 + Q_2^2 + Q_3^2 = 0$ | $Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = 0$ |
| Square | $\tilde{Q}^2 = 0$ | $\tilde{Q}^2 = 2 Q_0 \tilde{Q}$ |
| Structure | Nilpotent | Complex multiple of an idempotent |
| Annihilator | Contains $\tilde{Q}$ itself | Contains $\tilde{Q} - 2 Q_0 e_0$ |
| Idempotent | None | $\tilde\Pi = \tilde{Q}/(2 Q_0)$ |

### The Union

The set of zero divisors of $\mathbb{B}$ is the union of the set of pure zero divisors (the nilpotents) and the set of non-pure zero divisors (the complex multiples of the idempotents). The two families are **disjoint**: they are distinguished by whether the scalar part $Q_0$ vanishes, and the origin is excluded from both by the definition of a zero divisor. Their union is the zero divisor set $\mathcal{Z}$.

The two families have different dimensions as complex cones:

- The **pure family** (the nilpotent cone) is a complex cone of complex dimension $2$ — equivalently, real dimension $4$ — since it is defined by one complex equation in the three complex coefficients $(Q_1, Q_2, Q_3)$.
- The **non-pure family** is a complex cone of complex dimension $3$ — equivalently, real dimension $6$ — since it is defined by the single complex equation $Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = 0$ with $Q_0 \neq 0$, the full zero divisor cone with the pure family removed.

## The Zero Divisor Set

The zero divisor set $\mathcal{Z} \subset \mathbb{B}$ is

$$
\mathcal{Z} = \{\tilde{Q} \in \mathbb{B} : \tilde{Q} \neq 0, \; \tilde{Q}\tilde{Q}^{\natural} = 0\}.
$$

It is the complement of the invertible elements in the complement of the zero element:

$$
\mathcal{Z} = \mathbb{B} \setminus (\{0\} \cup \mathbb{B}^\times).
$$

**Basic properties.**

- $\mathcal{Z}$ is a cone away from the origin: if $\tilde{Q} \in \mathcal{Z}$ and $\alpha \in \mathbb{C} \setminus \{0\}$, then $\alpha \tilde{Q} \in \mathcal{Z}$, because $(\alpha \tilde{Q})((\alpha \tilde{Q}))^{\natural} = \alpha^2 \tilde{Q}\tilde{Q}^{\natural} = 0$.

**Dimension.** The zero divisor set has **real dimension $6$** (equivalently, **complex dimension $3$** as a complex algebraic cone in $\mathbb{C}^4$). The reasoning is the following. The vanishing $\tilde{Q}\tilde{Q}^{\natural} = 0$ is a single complex-valued polynomial equation in the four complex coefficients $(Q_0, Q_1, Q_2, Q_3)$, or equivalently two real equations in the eight real coordinates. The solution set of $\tilde{Q}\tilde{Q}^{\natural} = 0$ is therefore a **complex hypersurface** in $\mathbb{C}^4$ of complex dimension $4 - 1 = 3$, hence real dimension $2 \cdot 3 = 6$.

## Summary

The zero divisors of the biquaternion algebra are the nonzero elements on which $\tilde{Q}\tilde{Q}^{\natural}$ vanishes. They split into two families:

- The **pure zero divisors**, which have vanishing scalar part and satisfy $Q_1^2 + Q_2^2 + Q_3^2 = 0$. These are exactly the nonzero nilpotents: their square is zero, and their annihilator contains themselves. They form a complex cone of real dimension $4$.
- The **non-pure zero divisors**, which have nonzero scalar part and satisfy $Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = 0$. These are exactly the nonzero complex multiples of the nontrivial idempotents of $\mathbb{B}$: their square is $2 Q_0 \tilde{Q}$, and their annihilator contains $\tilde{Q} - 2 Q_0 e_0$. They form a complex cone of real dimension $6$.

The idempotents that appear here — trivial, Hermitian and general, with their bijection with the roots of $-1$ — are classified in *Biquaternion Idempotents and Projections*.

Of the six distinguished subspaces of $\mathbb{B}$, $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ contain no zero divisors, while $\mathbb{M}_+$ and $\mathbb{M}_-$ contain a three-dimensional double cone of zero divisors and $\mathrm{Vect}(\mathbb{B})$ contains the nilpotent cone, of real dimension $4$. A generic zero divisor lies in none of the six.

The zero divisor set is a complex cone of complex dimension $3$ (real dimension $6$) in $\mathbb{B} \cong \mathbb{C}^4$, with the origin removed. The classification of the roots of $-1$ that underlies the idempotent classification is studied in *Biquaternion Square Roots of Minus One, Zero and Plus One*, and the idempotent classification in *Biquaternion Idempotents and Projections*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | General biquaternion |
| $Q_\mu = q_\mu + i q'_\mu$ | Complex coefficient |
| $$\tilde{Q}\tilde{Q}^{\natural} = 0$$ | Algebraic criterion for a zero divisor |
| $\mathcal{Z}$ | Zero divisor set |
| $\tilde\Pi^2 = \tilde\Pi$ | Idempotent equation |
| $\tilde{Q}^2 = 0$ | Nilpotent equation |
| $\mathbb{C}_{\mathbb{B}}$ | Complex subspace |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion subspace |
| $\mathbb{M}_+$ | Hermitian subspace |
| $\mathbb{M}_-$ | Anti-Hermitian subspace |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original discovery of the zero divisors and the nilpotents.
- William Rowan Hamilton, "On the Geometrical Interpretation of some Results obtained by calculation with Biquaternions," *Proceedings of the Royal Irish Academy* **5** (1853) 388–390, for the bivectors, the null-square bivectors $i + hj$ and $j + hk$, and the simplification $(1 + j + hk)^x = 1 + x(j + hk)$.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the classification of the zero divisors.
- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63–68, for the classification of the roots of $-1$.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the algebraic properties of the biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.

