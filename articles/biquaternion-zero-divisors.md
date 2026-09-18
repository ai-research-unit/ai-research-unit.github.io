
# Biquaternion Zero Divisors

## Introduction

This article studies the zero divisors of the biquaternion algebra $\mathbb{B}$. It follows the article on biquaternion norm and invertibility, which established the criterion for invertibility and the three-way classification of the elements of $\mathbb{B}$. The goal here is to characterize the zero divisors, to split them into two families, and to describe their structure.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra. The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is assumed from the article on biquaternion algebra, together with its four conjugations and its four fixed-point subspaces. The invertibility criterion is assumed from the article on biquaternion norm and invertibility. The classification of the roots of $-1$ is assumed from the article on biquaternion roots of minus one, and it is stated here in the form in which it is used.

Throughout this article, the quaternion basis is written $e_0 = 1, e_1, e_2, e_3$, and the scalar imaginary is written $i$, so that it does not collide with the quaternion units. A general biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu \in \mathbb{C}.
$$

The quaternion conjugate is denoted $\bar{\tilde{Q}}$, the complex conjugate is denoted $\tilde{Q}^*$, the Hermitian conjugate is denoted $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$, and the anti-Hermitian conjugate is denoted $\tilde{Q}^\flat = -\tilde{Q}^\dagger$. The norm form is $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = \sum_\mu Q_\mu^2$.

## Definition and Criterion

### Definition

A biquaternion $\tilde{Q}$ is a **zero divisor** if it is **nonzero** and there exists a **nonzero** biquaternion $\tilde{R}$ such that

$$
\tilde{Q} \circ \tilde{R} = 0 \quad \text{or} \quad \tilde{R} \circ \tilde{Q} = 0.
$$

The requirement that both $\tilde{Q}$ and $\tilde{R}$ be nonzero is essential. In particular, the element $\tilde{Q} = 0$ is **not** a zero divisor, even though $0 \circ \tilde{R} = 0$ for any $\tilde{R}$.

### Criterion

**Theorem.** A nonzero biquaternion $\tilde{Q}$ is a zero divisor if and only if its norm form vanishes:

$$
N(\tilde{Q}) = 0.
$$

**Proof.** Suppose $\tilde{Q} \neq 0$ and $N(\tilde{Q}) = 0$. Then $\tilde{Q} \bar{\tilde{Q}} = 0$. Since $\tilde{Q} \neq 0$, we also have $\bar{\tilde{Q}} \neq 0$. So $\tilde{R} = \bar{\tilde{Q}}$ is a nonzero biquaternion with $\tilde{Q} \circ \tilde{R} = 0$. Hence $\tilde{Q}$ is a zero divisor.

Conversely, suppose $\tilde{Q}$ is a zero divisor: there exists $\tilde{R} \neq 0$ with $\tilde{Q} \circ \tilde{R} = 0$. If $N(\tilde{Q}) \neq 0$, then $\tilde{Q}$ is invertible by the invertibility criterion, and multiplying $\tilde{Q} \circ \tilde{R} = 0$ on the left by $\tilde{Q}^{-1}$ gives $\tilde{R} = 0$, contradicting $\tilde{R} \neq 0$. So $N(\tilde{Q}) = 0$. $\square$

### The Three-Way Classification

Combining the criterion for invertibility from the preceding article with the criterion for zero divisors, the elements of $\mathbb{B}$ are partitioned into three classes:

| Condition on $N(\tilde{Q})$ | Condition on $\tilde{Q}$ | Conclusion |
|---|---|---|
| $N(\tilde{Q}) \neq 0$ | (automatically $\tilde{Q} \neq 0$) | $\tilde{Q}$ is invertible |
| $N(\tilde{Q}) = 0$ | $\tilde{Q} = 0$ | $\tilde{Q}$ is the zero element |
| $N(\tilde{Q}) = 0$ | $\tilde{Q} \neq 0$ | $\tilde{Q}$ is a zero divisor |

The zero divisors are exactly the nonzero elements on which the norm form vanishes.

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

In the **pure case**, the norm form reduces to

$$
N(\tilde{Q}) = (\mathbf{Q}, \mathbf{Q}) = Q_1^2 + Q_2^2 + Q_3^2,
$$

a complex scalar. The vanishing of the norm form is the condition $(\mathbf{Q}, \mathbf{Q}) = 0$, which has nontrivial complex solutions (the nilpotents).

In the **non-pure case**, the norm form contains the scalar contribution $Q_0^2$ in addition to the vector contribution:

$$
N(\tilde{Q}) = Q_0^2 + (\mathbf{Q}, \mathbf{Q}),
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
\tilde{Q}^2 = -(Q_1^2 + Q_2^2 + Q_3^2) e_0 = -N(\tilde{Q}) e_0.
$$

### The Criterion

**Theorem.** The following three conditions on a pure biquaternion $\tilde{Q}$ are equivalent:

1. $\tilde{Q}$ is a zero divisor.
2. $N(\tilde{Q}) = 0$, i.e. $Q_1^2 + Q_2^2 + Q_3^2 = 0$.
3. $\tilde{Q}^2 = 0$.

**Proof.** The equivalence of (1) and (2) is the general criterion for zero divisors. The equivalence of (2) and (3) follows from the computation of the square above: $\tilde{Q}^2 = -N(\tilde{Q}) e_0$ vanishes if and only if $N(\tilde{Q}) = 0$. $\square$

A biquaternion satisfying $\tilde{Q}^2 = 0$ is called a **nilpotent**, so in the pure case, the zero divisors are exactly the nilpotents.

### Properties

A pure zero divisor $\tilde{Q}$ has the following properties.

- **Self-annihilation.** $\tilde{Q} \circ \tilde{Q} = 0$. The annihilator of $\tilde{Q}$ contains $\tilde{Q}$ itself, and therefore contains the whole complex line spanned by $\tilde{Q}$.
- **Non-invertibility.** By the criterion for invertibility, $\tilde{Q}$ has no inverse.
- **Purity preserved.** The scalar part of $\tilde{Q}$ is zero by hypothesis, and the square $\tilde{Q}^2 = 0$ also has zero scalar part. So the property of being pure is preserved under squaring.

## Non-Pure Zero Divisors

### The Square of a Non-Pure Biquaternion

Let $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$ with $Q_0 \in \mathbb{C}$, $Q_0 \neq 0$, and $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$. Using the product formula,

$$
\tilde{Q}^2 = (Q_0^2 - (\mathbf{Q}, \mathbf{Q})) e_0 + 2 Q_0 \mathbf{Q},
$$

where $(\mathbf{Q}, \mathbf{Q}) = Q_1^2 + Q_2^2 + Q_3^2$.

### The Relation to the Norm Form

The norm form of $\tilde{Q}$ is

$$
N(\tilde{Q}) = Q_0^2 + (\mathbf{Q}, \mathbf{Q}).
$$

So the condition $N(\tilde{Q}) = 0$ is equivalent to

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
\frac{\tilde{Q}^2}{2 Q_0} = \tilde{Q}.
$$

Define

$$
\tilde{P} = \frac{\tilde{Q}}{2 Q_0}.
$$

Then

$$
\tilde{P}^2 = \frac{\tilde{Q}^2}{(2 Q_0)^2} = \frac{2 Q_0 \tilde{Q}}{4 Q_0^2} = \frac{\tilde{Q}}{2 Q_0} = \tilde{P}.
$$

So $\tilde{P}$ is an **idempotent**: an element satisfying $\tilde{P}^2 = \tilde{P}$. And $\tilde{Q}$ is recovered from $\tilde{P}$ by

$$
\tilde{Q} = 2 Q_0 \tilde{P}.
$$

So every non-pure zero divisor is a complex multiple of an idempotent.

### The Idempotent Classification

The idempotents of $\mathbb{B}$ are classified as follows. The classification depends on the roots of $-1$ in $\mathbb{B}$, which are classified in the article on biquaternion roots of minus one.

**Theorem.** Every idempotent of $\mathbb{B}$ is either trivial ($0$ or $e_0$) or of the form

$$
\tilde{P} = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i,
$$

where $\xi \in \mathbb{B}$ is a root of $-1$, i.e. $\xi^2 = -1$. There are no other idempotents in $\mathbb{B}$.

**Proof.** Write $\tilde{P} = A e_0 + \mathbf{B}$ with $A \in \mathbb{C}$ and $\mathbf{B} = B_1 e_1 + B_2 e_2 + B_3 e_3$ a pure biquaternion. Then

$$
\tilde{P}^2 = (A^2 - (\mathbf{B}, \mathbf{B})) e_0 + 2 A \mathbf{B}.
$$

Equating to $\tilde{P} = A e_0 + \mathbf{B}$ gives the two equations

$$
A^2 - (\mathbf{B}, \mathbf{B}) = A, \qquad 2 A \mathbf{B} = \mathbf{B}.
$$

If $\mathbf{B} = 0$, then $A^2 = A$, so $A = 0$ or $A = 1$, giving the trivial idempotents. If $\mathbf{B} \neq 0$, then the second equation gives $A = 1/2$. Substituting into the first gives $1/4 - (\mathbf{B}, \mathbf{B}) = 1/2$, so $(\mathbf{B}, \mathbf{B}) = -1/4$.

Define $\xi = -2 i \mathbf{B}$. Then $\xi$ is pure, and

$$
(\xi, \xi) = \sum_{k=1}^{3} (-2 i B_k)^2 = -4 \sum_{k=1}^{3} B_k^2 = -4 (\mathbf{B}, \mathbf{B}) = 1,
$$

so $\xi^2 = -(\xi, \xi) = -1$. Thus $\xi$ is a root of $-1$, and $\mathbf{B} = \xi \cdot (i/2)$. Hence

$$
\tilde{P} = \tfrac{1}{2} e_0 + \tfrac{1}{2} \xi i.
$$

The sign choice arises from replacing $\xi$ by $-\xi$, which is also a root of $-1$. $\square$

The trivial idempotents correspond to the degenerate roots $\xi = \pm i$: with $\xi = i$, the formula gives $\tilde{P} = \frac{1}{2} e_0 + \frac{1}{2} i \cdot i = \frac{1}{2} e_0 - \frac{1}{2} e_0 = 0$; with $\xi = -i$, it gives $\tilde{P} = \frac{1}{2} e_0 - \frac{1}{2} i \cdot i = \frac{1}{2} e_0 + \frac{1}{2} e_0 = e_0$.

### Properties

A non-pure zero divisor $\tilde{Q}$ has the following properties.

- **Form.** $\tilde{Q} = 2 Q_0 \tilde{P}$ with $\tilde{P}$ idempotent. So the zero divisor is a complex multiple of an idempotent.
- **Square.** $\tilde{Q}^2 = 2 Q_0 \tilde{Q}$. This is a complex multiple of $\tilde{Q}$ itself, with the multiplier being twice the scalar part.
- **Non-invertibility.** By the criterion for invertibility, $\tilde{Q}$ has no inverse.
- **Nontrivial annihilator.** The element $\tilde{Q} - 2 Q_0 e_0 = 2 Q_0 (\tilde{P} - e_0)$ is annihilated by $\tilde{Q}$ on the right and on the left:

$$
\tilde{Q} \circ (\tilde{Q} - 2 Q_0 e_0) = \tilde{Q}^2 - 2 Q_0 \tilde{Q} = 0,
$$

$$
(\tilde{Q} - 2 Q_0 e_0) \circ \tilde{Q} = \tilde{Q}^2 - 2 Q_0 \tilde{Q} = 0.
$$

## The Roots of Minus One

The classification of the idempotents depends on the classification of the roots of $-1$ in $\mathbb{B}$. The roots are stated here; the proof is in the article on biquaternion roots of minus one.

**Theorem.** The roots of $-1$ in $\mathbb{B}$, i.e. the elements $\xi \in \mathbb{B}$ with $\xi^2 = -1$, are exactly:

1. **The trivial roots:** $\xi = \pm i$ (the scalar imaginary).
2. **The real quaternion roots:** $\xi = \pm \mu$, where $\mu$ is a unit pure real quaternion, i.e. $\mu = \mu_1 e_1 + \mu_2 e_2 + \mu_3 e_3$ with $\mu_1, \mu_2, \mu_3 \in \mathbb{R}$ and $\mu_1^2 + \mu_2^2 + \mu_3^2 = 1$.
3. **The non-trivial roots:** $\xi = b \mu + d \nu i$, where $\mu$ and $\nu$ are perpendicular unit pure real quaternions and $b, d \in \mathbb{R}$ satisfy $b^2 - d^2 = 1$ with $b \neq 0$ and $d \neq 0$.

The three families are distinguished by the value of the real and imaginary parts of $\xi$. Writing $\xi = \xi_0 e_0 + \xi_1 e_1 + \xi_2 e_2 + \xi_3 e_3$ with $\xi_\mu = a_\mu + i b_\mu$, the trivial roots have $a_\mu = 0$ for all $\mu$, $b_0 = \pm 1$, and $b_k = 0$ for $k = 1, 2, 3$; the real quaternion roots have $b_\mu = 0$ for all $\mu$ and $a_0 = 0$; and the non-trivial roots have both a nonzero real part and a nonzero imaginary part in the vector directions.

## Distribution of the Zero Divisors

We now examine how the zero divisors are distributed among the four fixed-point subspaces of $\mathbb{B}$ defined in the basic algebra article.

### The Complex Subspace $\mathbb{C}_{\mathbb{B}}$

An element of $\mathbb{C}_{\mathbb{B}}$ has the form $\tilde{Q} = Q_0 e_0$ with $Q_0 \in \mathbb{C}$. The norm form is $N(\tilde{Q}) = Q_0^2$, which vanishes only at $\tilde{Q} = 0$. So $\mathbb{C}_{\mathbb{B}}$ contains no zero divisors. This reflects the fact that $\mathbb{C}_{\mathbb{B}}$ is a copy of the field $\mathbb{C}$.

### The Quaternion Subspace $\mathbb{H}_{\mathbb{B}}$

An element of $\mathbb{H}_{\mathbb{B}}$ has real coefficients, and its norm form is a sum of squares of real numbers, which vanishes only at $\tilde{Q} = 0$. So $\mathbb{H}_{\mathbb{B}}$ contains no zero divisors. This reflects the Frobenius theorem: $\mathbb{H}_{\mathbb{B}}$ is a copy of the division algebra $\mathbb{H}$.

### The Hermitian Subspace $\mathbb{M}_+$

An element of $\mathbb{M}_+$ has the form

$$
\tilde{Q} = q_0 e_0 + i q'_1 e_1 + i q'_2 e_2 + i q'_3 e_3, \qquad q_0, q'_1, q'_2, q'_3 \in \mathbb{R}.
$$

The norm form is

$$
N(\tilde{Q}) = q_0^2 - (q'_1)^2 - (q'_2)^2 - (q'_3)^2.
$$

This vanishes for the nonzero elements satisfying

$$
q_0^2 = (q'_1)^2 + (q'_2)^2 + (q'_3)^2.
$$

This is the equation of a **double cone** in the four-dimensional real space $\mathbb{M}_+$, with apex at the origin. The nonzero elements of this cone are zero divisors. The set of zero divisors in $\mathbb{M}_+$ is therefore a three-dimensional submanifold of $\mathbb{M}_+$.

The elements of $\mathbb{M}_+$ **outside** the cone have $N(\tilde{Q}) \neq 0$ and are invertible. The set of invertible elements of $\mathbb{M}_+$ is the complement of the cone, which has **three** connected components:

- The **future timelike region** $q_0 > 0$ and $q_0^2 > (q'_1)^2 + (q'_2)^2 + (q'_3)^2$, on which $N(\tilde{Q}) > 0$.
- The **past timelike region** $q_0 < 0$ and $q_0^2 > (q'_1)^2 + (q'_2)^2 + (q'_3)^2$, on which $N(\tilde{Q}) > 0$.
- The **spacelike region** $q_0^2 < (q'_1)^2 + (q'_2)^2 + (q'_3)^2$, on which $N(\tilde{Q}) < 0$.

### The Anti-Hermitian Subspace $\mathbb{M}_-$

An element of $\mathbb{M}_-$ has the form

$$
\tilde{Q} = i q'_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q'_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

The norm form is

$$
N(\tilde{Q}) = -(q'_0)^2 + q_1^2 + q_2^2 + q_3^2.
$$

This vanishes for the nonzero elements satisfying

$$
(q'_0)^2 = q_1^2 + q_2^2 + q_3^2.
$$

This is again the equation of a **double cone** in the four-dimensional real space $\mathbb{M}_-$, with apex at the origin. The nonzero elements of this cone are zero divisors. The set of zero divisors in $\mathbb{M}_-$ is therefore a three-dimensional submanifold of $\mathbb{M}_-$.

The elements of $\mathbb{M}_-$ **outside** the cone have $N(\tilde{Q}) \neq 0$ and are invertible. The set of invertible elements of $\mathbb{M}_-$ is the complement of the cone, which has **three** connected components:

- The **spacelike region** $q_1^2 + q_2^2 + q_3^2 > (q'_0)^2$, on which $N(\tilde{Q}) > 0$.
- The **future timelike region** $q'_0 > 0$ and $(q'_0)^2 > q_1^2 + q_2^2 + q_3^2$, on which $N(\tilde{Q}) < 0$.
- The **past timelike region** $q'_0 < 0$ and $(q'_0)^2 > q_1^2 + q_2^2 + q_3^2$, on which $N(\tilde{Q}) < 0$.

### Summary of the Distribution

Of the four fixed-point subspaces of $\mathbb{B}$:

- $\mathbb{C}_{\mathbb{B}}$ and $\mathbb{H}_{\mathbb{B}}$ contain no zero divisors. They are the subalgebras of $\mathbb{B}$ among the four subspaces that are division algebras.
- $\mathbb{M}_+$ and $\mathbb{M}_-$ contain a three-dimensional cone of zero divisors. The nonzero elements outside the cone are invertible, and the zero divisors form the cone itself (minus the origin).

The two cones have the same structure: in each case, the equation is that the square of one real coordinate equals the sum of the squares of the other three. In $\mathbb{M}_+$ the special coordinate is $q_0$ (the real scalar part); in $\mathbb{M}_-$ it is $q'_0$ (the imaginary scalar part).

## Structure of the Zero Divisors

We now summarize the structure of the zero divisors of $\mathbb{B}$ in terms of the pure/non-pure distinction.

### The Pure Case

A pure biquaternion $\tilde{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ is a zero divisor if and only if

$$
Q_1^2 + Q_2^2 + Q_3^2 = 0,
$$

and in that case $\tilde{Q}^2 = 0$. So the pure zero divisors are exactly the nilpotents. They form the zero divisors whose scalar part vanishes.

### The Non-Pure Case

A non-pure biquaternion $\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ with $Q_0 \neq 0$ is a zero divisor if and only if $N(\tilde{Q}) = 0$, and in that case

$$
\tilde{Q}^2 = 2 Q_0 \tilde{Q}.
$$

So the non-pure zero divisors are exactly the complex multiples of the idempotents of $\mathbb{B}$. They form the zero divisors whose scalar part is nonzero.

### The Comparison Table

The two cases are distinct in their structure:

| | Pure case ($Q_0 = 0$) | Non-pure case ($Q_0 \neq 0$) |
|---|---|---|
| Form | $\tilde{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ | $\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ |
| Criterion | $Q_1^2 + Q_2^2 + Q_3^2 = 0$ | $Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = 0$ |
| Square | $\tilde{Q}^2 = 0$ | $\tilde{Q}^2 = 2 Q_0 \tilde{Q}$ |
| Structure | Nilpotent | Complex multiple of an idempotent |
| Annihilator | Contains $\tilde{Q}$ itself | Contains $\tilde{Q} - 2 Q_0 e_0$ |
| Idempotent | None | $\tilde{P} = \tilde{Q}/(2 Q_0)$ |

### The Union

The set of zero divisors of $\mathbb{B}$ is the union of the set of pure zero divisors (the nilpotents) and the set of non-pure zero divisors (the complex multiples of the idempotents). The two families are **disjoint**: they are distinguished by whether the scalar part $Q_0$ vanishes, and the origin is excluded from both by the definition of a zero divisor. Their union is the zero divisor set $\mathcal{Z}$.

The two families have different dimensions as complex cones:

- The **pure family** (the nilpotent cone) is a complex cone of complex dimension $2$ — equivalently, real dimension $4$ — since it is defined by one complex equation in the three complex coefficients $(Q_1, Q_2, Q_3)$.
- The **non-pure family** is an open dense subset of the full zero divisor cone (the condition $Q_0 \neq 0$ is open, and the closure of the resulting family is the whole cone). Its complex dimension is $3$, equivalently real dimension $6$, matching that of the full zero divisor set.

## The Structure of the Zero Divisor Set

The zero divisor set $\mathcal{Z} \subset \mathbb{B}$ is

$$
\mathcal{Z} = \{\tilde{Q} \in \mathbb{B} : \tilde{Q} \neq 0, \; N(\tilde{Q}) = 0\}.
$$

It is the complement of the invertible elements in the complement of the zero element:

$$
\mathcal{Z} = \mathbb{B} \setminus (\{0\} \cup \mathbb{B}^\times).
$$

**Basic properties.**

- The closed cone $\{N(\tilde{Q}) = 0\}$ is the zero-set of the continuous (indeed polynomial) map $N : \mathbb{B} \to \mathbb{C}$; it is therefore a closed subset of $\mathbb{B}$. The set $\mathcal{Z}$ itself is this closed cone with the origin removed, and is therefore **not closed**: it is a closed cone minus its apex.
- $\mathcal{Z}$ is a cone away from the origin: if $\tilde{Q} \in \mathcal{Z}$ and $\alpha \in \mathbb{C} \setminus \{0\}$, then $\alpha \tilde{Q} \in \mathcal{Z}$, because $N(\alpha \tilde{Q}) = \alpha^2 N(\tilde{Q}) = 0$.

**Dimension.** The zero divisor set has **real dimension $6$** (equivalently, **complex dimension $3$** as a complex algebraic cone in $\mathbb{C}^4$). The reasoning is the following. The norm form $N : \mathbb{B} \to \mathbb{C}$ is a single complex-valued polynomial equation in the four complex coefficients $(Q_0, Q_1, Q_2, Q_3)$, or equivalently two real equations in the eight real coordinates. The solution set of $N(\tilde{Q}) = 0$ is therefore a **complex hypersurface** in $\mathbb{C}^4$ of complex dimension $4 - 1 = 3$, hence real dimension $2 \cdot 3 = 6$.

The two real equations are independent at every nonzero point of the zero set, so the zero set is a smooth real $6$-manifold away from the origin. (The two real equations are $N_r = 0$ and $N_i = 0$, with gradients $\nabla N_r$ and $\nabla N_i$ proportional only when $(q_0, q_1, q_2, q_3, q'_0, q'_1, q'_2, q'_3) = (0, \dots, 0)$; since the origin is excluded from $\mathcal{Z}$, the gradients are linearly independent everywhere on $\mathcal{Z}$.)

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | General biquaternion |
| $Q_\mu = q_\mu + i q'_\mu$ | Complex coefficient |
| $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}}$ | Norm form |
| $\mathcal{Z}$ | Zero divisor set |
| $\tilde{P}^2 = \tilde{P}$ | Idempotent equation |
| $\tilde{Q}^2 = 0$ | Nilpotent equation |
| $\mathbb{C}_{\mathbb{B}}$ | Complex subspace |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion subspace |
| $\mathbb{M}_+$ | Hermitian subspace |
| $\mathbb{M}_-$ | Anti-Hermitian subspace |

## Summary

The zero divisors of the biquaternion algebra are the nonzero elements on which the norm form vanishes. They split into two families:

- The **pure zero divisors**, which have vanishing scalar part and satisfy $Q_1^2 + Q_2^2 + Q_3^2 = 0$. These are exactly the nilpotents: their square is zero, and their annihilator contains themselves. They form a complex cone of real dimension $4$.
- The **non-pure zero divisors**, which have nonzero scalar part and satisfy $Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = 0$. These are exactly the complex multiples of the idempotents of $\mathbb{B}$: their square is $2 Q_0 \tilde{Q}$, and their annihilator contains $\tilde{Q} - 2 Q_0 e_0$. They form an open dense subset of the full zero divisor cone.

The idempotents are either trivial ($0$ or $e_0$) or of the form $\tfrac{1}{2} e_0 \pm \tfrac{1}{2} \xi i$, where $\xi$ is a root of $-1$ in $\mathbb{B}$. The roots of $-1$ are classified as the trivial roots $\pm i$, the real quaternion roots $\pm \mu$ with $\mu$ a unit pure real quaternion, and the non-trivial roots $b\mu + d\nu i$ with $b^2 - d^2 = 1$ and $\mu \perp \nu$ unit pure real quaternions.

Of the four fixed-point subspaces of $\mathbb{B}$, $\mathbb{C}_{\mathbb{B}}$ and $\mathbb{H}_{\mathbb{B}}$ contain no zero divisors, while $\mathbb{M}_+$ and $\mathbb{M}_-$ contain a three-dimensional double cone of zero divisors (within the four-dimensional subspace).

The zero divisor set is a complex cone of complex dimension $3$ (real dimension $6$) in $\mathbb{B} \cong \mathbb{C}^4$, with the origin removed. The classification of the roots of $-1$ that underlies the idempotent classification is studied in the article on biquaternion roots of minus one.

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original discovery of the zero divisors and the nilpotents.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the classification of the zero divisors.
- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63–68, for the classification of the roots of $-1$.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the semi-norm and the algebraic properties of the biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra perspective.

