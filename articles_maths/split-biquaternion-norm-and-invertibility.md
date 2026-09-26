# __Split-Biquaternion Norm and Invertibility__

## Introduction

This article studies the norm form of the split biquaternion algebra and the invertibility of its elements. It follows the article on split biquaternion algebra, which defined the algebra, its four conjugations, and its four fixed-point subspaces. The goal here is to define the norm form and the Hermitian form, to establish the criterion for invertibility, and to describe the group of units.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra. The split complex algebra $\mathbb{D}$ is assumed from the article on split complex algebra, together with its idempotents $e_+ = \tfrac{1}{2}(1 + j)$ and $e_- = \tfrac{1}{2}(1 - j)$ and the isomorphism $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$. The split biquaternion algebra $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ is assumed from the preceding article, together with its four conjugations, its four fixed-point subspaces, and its three decompositions.

Throughout, a split biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu = q_\mu + j q'_\mu, \quad q_\mu, q'_\mu \in \mathbb{R}.
$$

The quaternion conjugate is $\bar{\tilde{Q}} = Q_0 e_0 - \mathbf{Q}$, where $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$. The split complex conjugate is $\tilde{Q}^* = Q_0^* e_0 + \mathbf{Q}^*$, where $Q_\mu^* = q_\mu - j q'_\mu$. The Hermitian conjugate is $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$, and the anti-Hermitian conjugate is $\tilde{Q}^\flat = -\tilde{Q}^\dagger$.

The idempotents of the split complex algebra are denoted $e_+ = \tfrac{1}{2}(1 + j)$ and $e_- = \tfrac{1}{2}(1 - j)$. The idempotent decomposition of a split biquaternion is

$$
\tilde{Q} = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-,
$$

with $\tilde{Q}_\pm = \tilde{Q} e_\pm \in \mathbb{H}$ ordinary quaternions.

## The Norm Form

### Definition

The **norm form** of a split biquaternion $\tilde{Q}$ is

$$
N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = \sum_{\mu=0}^{3} Q_\mu^2,
$$

where $\bar{\tilde{Q}}$ is the quaternion conjugate.

**Basic properties.**

- $N(\tilde{Q})$ is a split complex number in general. It is real when $\tilde{Q}$ lies in the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ or in the imaginary translate $j \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, and outside their union it need not be real.
- $N(\tilde{Q})$ is **anisotropic**: it vanishes only when $\tilde{Q} = 0$, so the norm form does not by itself detect the zero divisors. Those are described by the idempotent criterion below, and are studied in the article on split biquaternion zero divisors.
- $N(\tilde{Q})$ is invariant under quaternion conjugation: $N(\bar{\tilde{Q}}) = N(\tilde{Q})$.
- $N(\tilde{Q})$ is not invariant under split complex conjugation: $N(\tilde{Q}^*) = N(\tilde{Q})^*$.
- $N(\tilde{Q})$ is not invariant under Hermitian conjugation: $N(\tilde{Q}^\dagger) = N(\tilde{Q})^*$.

### Explicit Form

Writing $Q_\mu = q_\mu + j q'_\mu$ and using $j^2 = +1$,

$$
N(\tilde{Q}) = \sum_{\mu=0}^{3} (q_\mu^2 + q'^2_\mu) + 2j \sum_{\mu=0}^{3} q_\mu q'_\mu.
$$

So the real part of the norm form is the sum of the squares of all eight real components, and the split part is twice the inner product of the real and split parts. This is the **same structure** as in the biquaternion case, with $j$ in place of $i$. The difference is the sign of the square of the extra unit: $j^2 = +1$ versus $i^2 = -1$.

### Multiplicativity

**Theorem.** The norm form is multiplicative:

$$
N(\tilde{Q} \circ \tilde{R}) = N(\tilde{Q}) \, N(\tilde{R}).
$$

**Proof.** Compute

$$
N(\tilde{Q} \circ \tilde{R}) = (\tilde{Q} \tilde{R}) \overline{(\tilde{Q} \tilde{R})} = \tilde{Q} \tilde{R} \bar{\tilde{R}} \bar{\tilde{Q}} = \tilde{Q} N(\tilde{R}) \bar{\tilde{Q}}.
$$

Since $N(\tilde{R})$ is a split complex number and the split complex unit $j$ commutes with the quaternion units, $N(\tilde{R})$ commutes with $\tilde{Q}$ and with $\bar{\tilde{Q}}$. So

$$
\tilde{Q} N(\tilde{R}) \bar{\tilde{Q}} = N(\tilde{R}) \tilde{Q} \bar{\tilde{Q}} = N(\tilde{R}) N(\tilde{Q}).
$$

$\square$

**Corollary.** If $N(\tilde{Q})$ and $N(\tilde{R})$ are invertible in $\mathbb{D}$, then $N(\tilde{Q} \circ \tilde{R})$ is invertible in $\mathbb{D}$.

**Corollary.** If $N(\tilde{Q}) = 0$ or $N(\tilde{R}) = 0$, then $N(\tilde{Q} \circ \tilde{R}) = 0$. In particular, the product of a zero divisor with any split biquaternion is either zero or a zero divisor.

### The Norm Form in the Idempotent Basis

In the idempotent basis, the norm form takes a particularly simple form. Writing $\tilde{Q} = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-$ with $\tilde{Q}_\pm \in \mathbb{H}$,

$$
N(\tilde{Q}) = N_{\mathbb{H}}(\tilde{Q}_+) e_+ + N_{\mathbb{H}}(\tilde{Q}_-) e_-,
$$

where $N_{\mathbb{H}}(\tilde{Q}_\pm) = \tilde{Q}_\pm \bar{\tilde{Q}}_\pm$ is the ordinary quaternion norm of $\tilde{Q}_\pm$, which is a non-negative real number.

So the norm form of a split biquaternion is the pair of non-negative real numbers $(N_{\mathbb{H}}(\tilde{Q}_+), N_{\mathbb{H}}(\tilde{Q}_-))$, embedded in the split complex algebra via the idempotent basis. This is the cleanest form of the norm form, and it is the form in which the invertibility criterion is most transparent.

## The Hermitian Form

### Definition

The **Hermitian form** of a split biquaternion $\tilde{Q}$ is

$$
\tilde{Q} \tilde{Q}^\dagger, \qquad \text{whose scalar part is } \sum_{\mu=0}^{3} Q_\mu Q_\mu^* = \sum_{\mu=0}^{3} (q_\mu^2 - q'^2_\mu),
$$

where $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$ is the Hermitian conjugate and $Q_\mu^* = q_\mu - j q'_\mu$ is the split complex conjugate.

**Basic properties.**

- $\tilde{Q} \tilde{Q}^\dagger$ need not be real: only its **scalar part** is, and that scalar part is the difference between the sum of the squares of the real parts and the sum of the squares of the split parts.
- The scalar part is **not positive-definite**: it can be positive, negative, or zero. Its signature is $(4, 4)$ on the eight-dimensional real space $\mathbb{H}_{\mathbb{D}}$.
- The product $\tilde{Q} \tilde{Q}^\dagger$ vanishes exactly when one of the idempotent components vanishes, that is on the union of two four-dimensional subspaces; the scalar part vanishes on the quadric hypersurface $\sum_\mu q_\mu^2 = \sum_\mu q'^2_\mu$, of dimension $7$.
- It is **not multiplicative**: $\tilde{Q} \tilde{Q}^\dagger$ does not satisfy a product formula.

### The Signature

The scalar part of the Hermitian form is a real quadratic form of signature $(4, 4)$:

- The positive directions are the four real coefficients $q_0, q_1, q_2, q_3$.
- The negative directions are the four split coefficients $q'_0, q'_1, q'_2, q'_3$.

So the scalar part of the Hermitian form is the difference of two positive-definite forms, each of rank 4.

### The Zero Set

The scalar part of the Hermitian form vanishes when

$$
\sum_{\mu=0}^{3} q_\mu^2 = \sum_{\mu=0}^{3} q'^2_\mu.
$$

This is a quadric hypersurface of dimension $7$ in $\mathbb{H}_{\mathbb{D}} \cong \mathbb{R}^8$, the analogue of a light cone in Minkowski space, with signature $(4, 4)$ instead of $(1, 3)$.

## The Euclidean Norm

### Definition

The **Euclidean norm** of a split biquaternion $\tilde{Q}$ is

$$
\|\tilde{Q}\|_E = \sqrt{\sum_{\mu=0}^{3} (q_\mu^2 + q'^2_\mu)}.
$$

It is a genuine norm on the real vector space $\mathbb{H}_{\mathbb{D}} \cong \mathbb{R}^8$: positive-definite, subadditive, and homogeneous of degree one.

### Relation to the Norm Form and the Hermitian Form

The Euclidean norm is not the square root of the Hermitian form, because the Hermitian form is indefinite. It is also not the modulus of the norm form, because the norm form is split complex and its modulus is

$$
|N(\tilde{Q})| = \sqrt{\left(\sum_\mu (q_\mu^2 + q'^2_\mu)\right)^2 - 4\left(\sum_\mu q_\mu q'_\mu\right)^2},
$$

which is not the Euclidean norm squared.

The Euclidean norm is defined separately, and it is the ordinary Euclidean norm on the underlying real vector space. It is the norm that defines the topology of $\mathbb{H}_{\mathbb{D}}$, the convergence of sequences, and the completeness of the algebra as a metric space.

### Multiplicativity

The Euclidean norm is **not** multiplicative with respect to the split biquaternion product. This is the same situation as in the biquaternion case, where the Euclidean norm is not multiplicative because the Hermitian form is not multiplicative.

The norm form, which is multiplicative, is split complex-valued and anisotropic: it is the idempotent components, not the norm, that detect the zero divisors. The Euclidean norm, which is positive-definite, is not multiplicative, and it does not detect the zero divisors.

## Invertibility

### Definition

A split biquaternion $\tilde{Q}$ is **invertible** if there exists a split biquaternion $\tilde{R}$ such that

$$
\tilde{Q} \circ \tilde{R} = \tilde{R} \circ \tilde{Q} = e_0.
$$

The split biquaternion $\tilde{R}$, if it exists, is the **inverse** of $\tilde{Q}$ and is denoted $\tilde{Q}^{-1}$.

### Left and Right Inverses

In a general non-commutative algebra, the notions of left inverse, right inverse, and two-sided inverse are distinct. In the split biquaternion algebra, however, they coincide, for the same reason as in the biquaternion algebra: the algebra is finite-dimensional over $\mathbb{R}$, and in a finite-dimensional algebra over a field, a right inverse is also a left inverse.

### Criterion for Invertibility

**Theorem.** A split biquaternion $\tilde{Q}$ is invertible if and only if its norm form is invertible in $\mathbb{D}$:

$$
N(\tilde{Q}) \in \mathbb{D}^\times.
$$

**Proof.** Suppose $N(\tilde{Q})$ is invertible in $\mathbb{D}$. Define

$$
\tilde{R} = \bar{\tilde{Q}} \, N(\tilde{Q})^{-1}.
$$

This is legitimate because $N(\tilde{Q})$ is a unit of $\mathbb{D}$: mere non-vanishing would not suffice, since $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$ has zero divisors. Then

$$
\tilde{Q} \circ \tilde{R} = N(\tilde{Q}) N(\tilde{Q})^{-1} = e_0,
$$

so $\tilde{R}$ is a right inverse, hence also a left inverse.

Conversely, suppose $\tilde{Q}$ is invertible. Applying the norm form to $\tilde{Q} \circ \tilde{Q}^{-1} = e_0$ and using multiplicativity gives

$$
N(\tilde{Q}) N(\tilde{Q}^{-1}) = N(e_0) = 1,
$$

so $N(\tilde{Q})$ is invertible in $\mathbb{D}$, with inverse $N(\tilde{Q}^{-1})$. $\square$

**Remark.** The hypothesis is not simply $\tilde{Q} \neq 0$, nor $N(\tilde{Q}) \neq 0$, which is the same thing by anisotropy. For $\tilde{Q} = e_+$ one has $N(\tilde{Q}) = e_+$, a nonzero zero divisor of $\mathbb{D}$, and $e_+$ is a zero divisor of $\mathbb{H}_{\mathbb{D}}$, since $e_+ e_- = 0$.

### The Inverse Formula

When $N(\tilde{Q})$ is invertible in $\mathbb{D}$, equivalently when $\tilde{Q}$ is invertible, the inverse is

$$
\tilde{Q}^{-1} = \bar{\tilde{Q}} \, N(\tilde{Q})^{-1}.
$$

This is the split biquaternion analogue of the formula $q^{-1} = \bar{q}/|q|^2$ for quaternions.

### The Criterion in the Idempotent Basis

The invertibility criterion takes a particularly simple form in the idempotent basis. Writing $\tilde{Q} = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-$ with $\tilde{Q}_\pm \in \mathbb{H}$,

$$
N(\tilde{Q}) = N_{\mathbb{H}}(\tilde{Q}_+) e_+ + N_{\mathbb{H}}(\tilde{Q}_-) e_-.
$$

Since $N_{\mathbb{H}}(\tilde{Q}_\pm)$ are non-negative real numbers, $N(\tilde{Q}) \neq 0$ if and only if

$$
N_{\mathbb{H}}(\tilde{Q}_+) \neq 0 \quad \text{or} \quad N_{\mathbb{H}}(\tilde{Q}_-) \neq 0.
$$

Since $\mathbb{H}$ is a division algebra, $N_{\mathbb{H}}(\tilde{Q}_\pm) \neq 0$ if and only if $\tilde{Q}_\pm \neq 0$. So the invertibility criterion is

$$
\tilde{Q} \text{ is invertible} \iff \tilde{Q}_+ \neq 0 \text{ and } \tilde{Q}_- \neq 0.
$$

This is the cleanest form of the invertibility criterion. It is a **linear** condition in the idempotent basis: the element is invertible if and only if neither of its two idempotent components vanishes.

**Comparison with the biquaternion case.** In the biquaternion algebra, the invertibility criterion $N(\tilde{Q}) \neq 0$ is a **quadratic** condition, and the zero divisor set is a complex cone of complex dimension 3 (real dimension 6). In the split biquaternion algebra, the invertibility criterion is a linear condition in the idempotent basis, and the zero divisor set is a union of two four-dimensional linear subspaces. The difference is a consequence of the fact that $\mathbb{H}_{\mathbb{D}}$ is semisimple while $\mathbb{B}$ is simple.

### Corollaries

**Corollary.** The inverse of an invertible element is invertible, and $(\tilde{Q}^{-1})^{-1} = \tilde{Q}$.

**Corollary.** If $\tilde{Q}$ is invertible, then $\bar{\tilde{Q}}$, $\tilde{Q}^*$, $\tilde{Q}^\dagger$, and $\tilde{Q}^\flat$ are invertible, and their inverses are the corresponding conjugates of $\tilde{Q}^{-1}$.

**Corollary.** The product of two invertible elements is invertible, with $(\tilde{Q} \tilde{R})^{-1} = \tilde{R}^{-1} \tilde{Q}^{-1}$.

## The Group of Units

### Definition

The **group of units** of $\mathbb{H}_{\mathbb{D}}$ is the set of invertible elements:

$$
\mathbb{H}_{\mathbb{D}}^\times = \{\tilde{Q} \in \mathbb{H}_{\mathbb{D}} : N(\tilde{Q}) \in \mathbb{D}^\times\}
= \{\tilde{Q} \in \mathbb{H}_{\mathbb{D}} : N_{\mathbb{H}}(\tilde{Q}_+) \neq 0 \text{ and } N_{\mathbb{H}}(\tilde{Q}_-) \neq 0\}.
$$

It is a group under multiplication, with identity $e_0$.

### Structure

**Theorem.** The group of units is isomorphic to the direct product of two copies of the quaternion unit group:

$$
\mathbb{H}_{\mathbb{D}}^\times \cong \mathbb{H}^\times \times \mathbb{H}^\times,
$$

where $\mathbb{H}^\times = \mathbb{H} \setminus \{0\}$ is the group of nonzero quaternions.

**Proof.** In the idempotent basis, an element is invertible if and only if both idempotent components are nonzero. The multiplication is componentwise, so the group of units is the direct product of the groups of units of the two components. Each component is a copy of $\mathbb{H}$, and its group of units is $\mathbb{H}^\times$. $\square$

### Basic Properties

**Openness.** The group of units is an open subset of $\mathbb{H}_{\mathbb{D}}$ in the Euclidean topology. Indeed, the invertibility condition is that both idempotent components are nonzero, which is an open condition.

**Non-compactness.** The group of units is not compact, because it contains the real line $\{a e_0 : a \in \mathbb{R}, a \neq 0\}$, which is unbounded.

**Connected components.** The group of units is connected. Indeed, in the idempotent basis, an invertible element is a pair $(\tilde{Q}_+, \tilde{Q}_-)$ with both components nonzero, and $\mathbb{H} \setminus \{0\} \cong S^3 \times (0, \infty)$ is connected; the group of units is therefore homeomorphic to $(\mathbb{H} \setminus \{0\}) \times (\mathbb{H} \setminus \{0\})$, with a single component. (The group $\mathbb{D}^\times$ of split complex scalars, by contrast, does have four components.)

**Lie group structure.** The group of units is a Lie group of dimension $8$ over $\mathbb{R}$. Its Lie algebra is $\mathbb{H}_{\mathbb{D}}$ itself, with the commutator bracket.

**Center.** The center of $\mathbb{H}_{\mathbb{D}}^\times$ is the group of invertible split complex scalars, which is the group of units of $\mathbb{D}$:

$$
Z(\mathbb{H}_{\mathbb{D}}^\times) = \mathbb{D}^\times = \{Q_0 \in \mathbb{D} : Q_0 \neq 0\}.
$$

The group of units of $\mathbb{D}$ has four connected components, corresponding to the four sign combinations of the real and split parts.

### The Inverse Map

The **inverse map**

$$
\iota : \mathbb{H}_{\mathbb{D}}^\times \to \mathbb{H}_{\mathbb{D}}^\times, \qquad \iota(\tilde{Q}) = \tilde{Q}^{-1},
$$

is a smooth involution. Its differential at the identity is $-\mathrm{id}_{\mathbb{H}_{\mathbb{D}}}$, which is the reason the Lie algebra bracket is antisymmetric.

## The Three-Way Classification

Combining the criterion for invertibility with the definition of the zero element, the elements of $\mathbb{H}_{\mathbb{D}}$ are partitioned into three classes:

| Condition on $N(\tilde{Q})$ | Condition on $\tilde{Q}$ | Conclusion |
|---|---|---|
| $N(\tilde{Q}) \in \mathbb{D}^\times$ | (automatically $\tilde{Q} \neq 0$) | $\tilde{Q}$ is invertible |
| $N(\tilde{Q}) = 0$ | $\tilde{Q} = 0$ | $\tilde{Q}$ is the zero element |
| $N(\tilde{Q})$ a nonzero zero divisor of $\mathbb{D}$ | $\tilde{Q} \neq 0$ | $\tilde{Q}$ is a zero divisor |

The zero divisors are the subject of the article on split biquaternion zero divisors.

### The Algebra Is Not a Division Algebra

By definition, a **division algebra** is an algebra in which every nonzero element is invertible. Equivalently, an algebra is a division algebra if and only if it contains no zero divisors.

The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$ contains zero divisors, so it is **not** a division algebra. This is in contrast to the quaternion algebra $\mathbb{H}$, which is a division algebra, and to the biquaternion algebra $\mathbb{B}$, which is also not a division algebra.

The Frobenius theorem states that the only finite-dimensional associative real division algebras are $\mathbb{R}$, $\mathbb{C}$, and $\mathbb{H}$. The split biquaternion algebra is a fourth finite-dimensional associative real algebra, but it is not a division algebra, because it contains zero divisors.

## Distribution of the Invertible Elements

We now examine how the invertible elements are distributed among the four fixed-point subspaces of $\mathbb{H}_{\mathbb{D}}$ defined in the preceding article. The criterion is the same in all cases: an element is invertible if and only if its norm form is invertible in $\mathbb{D}$, equivalently if and only if both of its idempotent components are nonzero.

### The Split Complex Subspace $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$

An element of $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ has the form

$$
\tilde{Q} = Q_0 e_0, \qquad Q_0 \in \mathbb{D}.
$$

The norm form is

$$
N(\tilde{Q}) = Q_0^2.
$$

Since $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$, this vanishes only when $Q_0 = 0$; the element $Q_0 e_0$ is a zero divisor if and only if $Q_0$ is a zero divisor in $\mathbb{D}$, that is a nonzero multiple of $1 \pm j$, which need not be detected by $N$ vanishing. So the split complex subspace contains the zero divisors $Q_0 e_0$ with $Q_0 = t(1 \pm j)$ for $t \neq 0$, inherited from the split complex algebra.

The invertible elements of $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ are those with $Q_0$ not a multiple of $1 \pm j$, i.e., with $Q_0$ invertible in $\mathbb{D}$.

### The Quaternion Subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$

An element of $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ has the form

$$
\tilde{Q} = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q_\mu \in \mathbb{R}.
$$

The norm form is

$$
N(\tilde{Q}) = q_0^2 + q_1^2 + q_2^2 + q_3^2.
$$

This is a sum of squares of real numbers, and it vanishes if and only if all $q_\mu = 0$, i.e., if and only if $\tilde{Q} = 0$. So the quaternion subspace contains no zero divisors, and every nonzero element is invertible. This reflects the Frobenius theorem: $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ is a copy of the division algebra $\mathbb{H}$.

### The Hermitian Subspace $\mathbb{M}_+$

An element of $\mathbb{M}_+$ has the form

$$
\tilde{Q} = q_0 e_0 + j q'_1 e_1 + j q'_2 e_2 + j q'_3 e_3, \qquad q_0, q'_1, q'_2, q'_3 \in \mathbb{R}.
$$

With $Q_0 = q_0$ (real) and $Q_k = j q'_k$ (purely split-imaginary), the norm form is

$$
N(\tilde{Q}) = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = q_0^2 + (j q'_1)^2 + (j q'_2)^2 + (j q'_3)^2 = q_0^2 + (q'_1)^2 + (q'_2)^2 + (q'_3)^2.
$$

Since $j^2 = +1$, the split-imaginary vector components contribute $(j q'_k)^2 = j^2 (q'_k)^2 = +(q'_k)^2$.

So the norm form on $\mathbb{M}_+$ is

$$
N(\tilde{Q}) = q_0^2 + (q'_1)^2 + (q'_2)^2 + (q'_3)^2,
$$

which is a **real**, positive-definite number, of signature $(4, 0)$. It vanishes only at the origin, so $\mathbb{M}_+$ contains no zero divisors and every nonzero element of $\mathbb{M}_+$ is invertible.

### The Anti-Hermitian Subspace $\mathbb{M}_-$

An element of $\mathbb{M}_-$ has the form

$$
\tilde{Q} = j r_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad r_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

The norm form is

$$
N(\tilde{Q}) = (j r_0)^2 + q_1^2 + q_2^2 + q_3^2 = r_0^2 + q_1^2 + q_2^2 + q_3^2,
$$

which is a **real**, positive-definite number, of signature $(4, 0)$. It vanishes only at the origin, so $\mathbb{M}_-$ contains no zero divisors and every nonzero element of $\mathbb{M}_-$ is invertible.

### Summary of the Distribution

Of the four fixed-point subspaces:

- $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ contains zero divisors (inherited from $\mathbb{D}$), and the invertible elements are those whose scalar part is invertible in $\mathbb{D}$.
- $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ is a division algebra: every nonzero element is invertible.
- $\mathbb{M}_+$ is positive-definite of signature $(4, 0)$: it contains no zero divisors and every nonzero element of it is invertible.
- $\mathbb{M}_-$ is positive-definite of signature $(4, 0)$: it contains no zero divisors and every nonzero element of it is invertible.

## Summary

The norm form $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}}$ is a split complex-valued multiplicative quadratic form on the split biquaternion algebra. It is anisotropic: it vanishes only at the origin, so it does not detect the zero divisors. In the idempotent basis, it is the pair of ordinary quaternion norms of the two idempotent components, which is the cleanest form of the norm form.

The scalar part of the Hermitian form $\tilde{Q} \tilde{Q}^\dagger$ is a real indefinite quadratic form of signature $(4, 4)$; the product itself need not be real. It does not define a Euclidean norm. The Euclidean norm is defined separately and is positive-definite but not multiplicative.

The invertibility criterion is: $\tilde{Q}$ is invertible if and only if $N(\tilde{Q})$ is invertible in $\mathbb{D}$, equivalently if and only if both of its idempotent components are nonzero. In the idempotent basis, this is equivalent to both idempotent components being nonzero:

$$
\tilde{Q} \text{ is invertible} \iff \tilde{Q}_+ \neq 0 \text{ and } \tilde{Q}_- \neq 0.
$$

This is a linear condition in the idempotent basis, in contrast to the quadratic condition in the biquaternion case.

The inverse is $\tilde{Q}^{-1} = \bar{\tilde{Q}}/N(\tilde{Q})$. The group of units $\mathbb{H}_{\mathbb{D}}^\times$ is isomorphic to $\mathbb{H}^\times \times \mathbb{H}^\times$, and it is connected.

The algebra $\mathbb{H}_{\mathbb{D}}$ is partitioned into three classes: the zero element, the invertible elements, and the zero divisors. Of the four fixed-point subspaces, the quaternion subspace is a division algebra, the split complex subspace contains zero divisors inherited from $\mathbb{D}$, and the Hermitian and anti-Hermitian subspaces are positive-definite and contain no zero divisors.

The zero divisors themselves are studied in the article on split biquaternion zero divisors, and the roots of $-1$ are studied in the article on split biquaternion roots of minus one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}}$ | Split biquaternion algebra |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | General split biquaternion |
| $Q_\mu = q_\mu + j q'_\mu$ | Split complex coefficient |
| $\bar{\tilde{Q}}$ | Quaternion conjugate |
| $\tilde{Q}^*$ | Split complex conjugate |
| $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$ | Hermitian conjugate |
| $\tilde{Q}^\flat = -\tilde{Q}^\dagger$ | Anti-Hermitian conjugate |
| $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}}$ | Norm form |
| $\tilde{Q} \tilde{Q}^\dagger = \sum_\mu (q_\mu^2 - q'^2_\mu)$ | Hermitian form (signature $(4,4)$) |
| $\|\tilde{Q}\|_E = \sqrt{\sum_\mu (q_\mu^2 + q'^2_\mu)}$ | Euclidean norm |
| $\tilde{Q}^{-1} = \bar{\tilde{Q}}/N(\tilde{Q})$ | Inverse |
| $\mathbb{H}_{\mathbb{D}}^\times$ | Group of units |
| $e_+ = \tfrac{1}{2}(1 + j)$ | Positive idempotent |
| $e_- = \tfrac{1}{2}(1 - j)$ | Negative idempotent |
| $\tilde{Q}_\pm = \tilde{Q} e_\pm$ | Idempotent components |
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | Split complex subspace |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | Quaternion subspace |
| $\mathbb{M}_+$ | Hermitian subspace |
| $\mathbb{M}_-$ | Anti-Hermitian subspace |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation of quaternions and their complexification.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the algebraic structure and the norm form of the split biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis.

