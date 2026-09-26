# __Split-Biquaternion Zero Divisors__

## Introduction

This article studies the zero divisors of the split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$. It follows the article on split biquaternion norm and invertibility, which established the criterion for invertibility and the three-way classification of the elements of $\mathbb{H}_{\mathbb{D}}$. The goal here is to characterize the zero divisors, to describe their structure, and to compare them with the zero divisors of the split complex algebra and of the biquaternion algebra.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra. The split complex algebra $\mathbb{D}$ is assumed from the article on split complex algebra, together with its idempotents $e_+ = \tfrac{1}{2}(1 + j)$ and $e_- = \tfrac{1}{2}(1 - j)$ and the isomorphism $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$. The split biquaternion algebra $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ is assumed from the preceding articles, together with its four conjugations, its four fixed-point subspaces, its three decompositions, and its norm form.

Throughout, a split biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu = q_\mu + j q'_\mu, \quad q_\mu, q'_\mu \in \mathbb{R}.
$$

The quaternion conjugate is $\bar{\tilde{Q}} = Q_0 e_0 - \mathbf{Q}$, where $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$. The split complex conjugate is $\tilde{Q}^* = Q_0^* e_0 + \mathbf{Q}^*$, where $Q_\mu^* = q_\mu - j q'_\mu$. The Hermitian conjugate is $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$, and the anti-Hermitian conjugate is $\tilde{Q}^\flat = -\tilde{Q}^\dagger$. The norm form is $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = \sum_\mu Q_\mu^2$.

The idempotents of the split complex algebra are $e_+ = \tfrac{1}{2}(1 + j)$ and $e_- = \tfrac{1}{2}(1 - j)$. The idempotent decomposition of a split biquaternion is

$$
\tilde{Q} = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-,
$$

with $\tilde{Q}_\pm = \tilde{Q} e_\pm \in \mathbb{H}$ ordinary quaternions. The norm form in the idempotent basis is

$$
N(\tilde{Q}) = N_{\mathbb{H}}(\tilde{Q}_+) e_+ + N_{\mathbb{H}}(\tilde{Q}_-) e_-,
$$

where $N_{\mathbb{H}}(\tilde{Q}_\pm) = \tilde{Q}_\pm \bar{\tilde{Q}}_\pm$ is the ordinary quaternion norm, a non-negative real number.

## Definition and Criterion

### Definition

A split biquaternion $\tilde{Q}$ is a **zero divisor** if it is **nonzero** and there exists a **nonzero** split biquaternion $\tilde{R}$ such that

$$
\tilde{Q} \circ \tilde{R} = 0 \quad \text{or} \quad \tilde{R} \circ \tilde{Q} = 0.
$$

The requirement that both $\tilde{Q}$ and $\tilde{R}$ be nonzero is essential. In particular, the element $\tilde{Q} = 0$ is **not** a zero divisor, even though $0 \circ \tilde{R} = 0$ for any $\tilde{R}$.

### Criterion

**Theorem.** A nonzero split biquaternion $\tilde{Q}$ is a zero divisor if and only if at least one of its two idempotent components vanishes:

$$
\tilde{Q} \neq 0 \quad \text{and} \quad (\tilde{Q}_+ = 0 \ \text{or}\ \tilde{Q}_- = 0).
$$

**Proof.** In the idempotent basis the product is $\tilde{Q} \tilde{R} = \tilde{Q}_+ \tilde{R}_+ e_+ + \tilde{Q}_- \tilde{R}_- e_-$, so $\tilde{Q} \tilde{R} = 0$ if and only if $\tilde{Q}_+ \tilde{R}_+ = 0$ and $\tilde{Q}_- \tilde{R}_- = 0$. If $\tilde{Q}_+ = 0$ and $\tilde{Q} \neq 0$, then $\tilde{Q}_- \neq 0$, and $\tilde{R} = e_+ \neq 0$ satisfies $\tilde{Q} \tilde{R} = 0$, so $\tilde{Q}$ is a zero divisor. Conversely, if $\tilde{Q} \tilde{R} = 0$ with $\tilde{R} \neq 0$, then $\tilde{R}_+ \neq 0$ or $\tilde{R}_- \neq 0$; in the first case $\tilde{Q}_+ \tilde{R}_+ = 0$ with $\tilde{R}_+ \neq 0$ forces $\tilde{Q}_+ = 0$, since $\mathbb{H}$ is a division algebra, and in the second case $\tilde{Q}_- = 0$. $\square$

**Remark.** The norm form is not the criterion: as the closing section computes, $N(\tilde{Q}) = 0$ forces $\tilde{Q} = 0$. The zero divisor condition is **linear** in the idempotent basis.

### The Three-Way Classification

Combining the criterion for invertibility from the preceding article with the criterion for zero divisors, the elements of $\mathbb{H}_{\mathbb{D}}$ are partitioned into three classes:

| Condition on the idempotent components | Condition on $\tilde{Q}$ | Conclusion |
|---|---|---|
| $\tilde{Q}_+ \neq 0$ and $\tilde{Q}_- \neq 0$ | (automatically $\tilde{Q} \neq 0$) | $\tilde{Q}$ is invertible |
| $\tilde{Q}_+ = 0$ and $\tilde{Q}_- = 0$ | $\tilde{Q} = 0$ | $\tilde{Q}$ is the zero element |
| exactly one of $\tilde{Q}_+$, $\tilde{Q}_-$ vanishes | $\tilde{Q} \neq 0$ | $\tilde{Q}$ is a zero divisor |

The zero divisors are exactly the nonzero elements with at least one vanishing idempotent component.

### The Criterion in the Idempotent Basis

In the idempotent basis, the criterion takes a particularly simple form. Writing $\tilde{Q} = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-$ with $\tilde{Q}_\pm \in \mathbb{H}$,

$$
N(\tilde{Q}) = N_{\mathbb{H}}(\tilde{Q}_+) e_+ + N_{\mathbb{H}}(\tilde{Q}_-) e_-.
$$

Since $N_{\mathbb{H}}(\tilde{Q}_\pm)$ are non-negative real numbers, $N(\tilde{Q}) = 0$ if and only if

$$
N_{\mathbb{H}}(\tilde{Q}_+) = 0 \quad \text{and} \quad N_{\mathbb{H}}(\tilde{Q}_-) = 0.
$$

Since $\mathbb{H}$ is a division algebra, $N_{\mathbb{H}}(\tilde{Q}_\pm) = 0$ if and only if $\tilde{Q}_\pm = 0$. So $N(\tilde{Q}) = 0$ if and only if $\tilde{Q} = 0$: the norm form is anisotropic, and the criterion for zero divisors is the vanishing of one idempotent component rather than of the norm form.

$$
\tilde{Q} \text{ is a zero divisor} \iff \tilde{Q} \neq 0 \text{ and } (\tilde{Q}_+ = 0 \text{ or } \tilde{Q}_- = 0).
$$

This is the cleanest form of the criterion. It is a **linear** condition in the idempotent basis: the element is a zero divisor if and only if at least one of its two idempotent components vanishes, and it is not the zero element.

## The Two Families of Zero Divisors

The criterion in the idempotent basis shows that the zero divisor set splits into two families.

### The Two Subspaces

Define

$$
Z_+ = \{\tilde{Q} \in \mathbb{H}_{\mathbb{D}} : \tilde{Q}_+ = 0\},
$$

$$
Z_- = \{\tilde{Q} \in \mathbb{H}_{\mathbb{D}} : \tilde{Q}_- = 0\}.
$$

Each of these is a **four-dimensional real linear subspace** of $\mathbb{H}_{\mathbb{D}}$.

**$Z_+$.** An element of $Z_+$ satisfies $\tilde{Q} e_+ = 0$, i.e., $\tilde{Q}(1 + j) = 0$. Writing $\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ with $Q_\mu \in \mathbb{D}$, the condition is that each coefficient $Q_\mu$ is a split complex multiple of $1 - j$. Since the ideal generated by $1 - j$ in $\mathbb{D}$ is the one-dimensional real subspace $\mathbb{R}(1 - j)$, the condition is

$$
Q_\mu = t_\mu (1 - j), \qquad t_\mu \in \mathbb{R}.
$$

There are four real parameters $t_0, t_1, t_2, t_3$, so $Z_+$ is four-dimensional. It is isomorphic to $\mathbb{H}$ via the map $\tilde{Q} \mapsto (t_0, t_1, t_2, t_3)$.

**$Z_-$.** An element of $Z_-$ satisfies $\tilde{Q} e_- = 0$, i.e., $\tilde{Q}(1 - j) = 0$. The condition is that each coefficient $Q_\mu$ is a split complex multiple of $1 + j$:

$$
Q_\mu = s_\mu (1 + j), \qquad s_\mu \in \mathbb{R}.
$$

There are four real parameters $s_0, s_1, s_2, s_3$, so $Z_-$ is four-dimensional. It is isomorphic to $\mathbb{H}$.

### The Zero Divisor Set

The zero divisor set is

$$
\mathcal{Z} = (Z_+ \cup Z_-) \setminus \{0\}.
$$

The two subspaces intersect at the origin:

$$
Z_+ \cap Z_- = \{0\}.
$$

Indeed, an element in both would have all coefficients both multiples of $1 - j$ and multiples of $1 + j$. Since $(1 - j)$ and $(1 + j)$ are linearly independent in $\mathbb{D}$, this forces all coefficients to vanish, i.e., $\tilde{Q} = 0$.

So the zero divisor set is the union of two four-dimensional linear subspaces that intersect only at the origin.

### Dimension

The zero divisor set has real dimension $4$ in the sense that each of the two components is four-dimensional. The union $Z_+ \cup Z_-$ is not a manifold at the origin, but away from the origin it is a disjoint union of two four-dimensional submanifolds.

## The Structure of the Zero Divisors

### Algebraic Structure of the Two Families

Each of $Z_+$ and $Z_-$ is a **left ideal** and a **right ideal** of $\mathbb{H}_{\mathbb{D}}$. Indeed:

- If $\tilde{Q} \in Z_+$ and $\tilde{R} \in \mathbb{H}_{\mathbb{D}}$, then $(\tilde{Q} \tilde{R}) e_+ = \tilde{Q} (\tilde{R} e_+) = \tilde{Q} e_+ \tilde{R}_+ = 0 \cdot \tilde{R}_+ = 0$, so $\tilde{Q} \tilde{R} \in Z_+$. So $Z_+$ is a right ideal.
- Similarly, $(\tilde{R} \tilde{Q}) e_+ = \tilde{R} (\tilde{Q} e_+) = 0$, so $\tilde{R} \tilde{Q} \in Z_+$. So $Z_+$ is a left ideal.

So $Z_+$ and $Z_-$ are two-sided ideals of $\mathbb{H}_{\mathbb{D}}$. This is the algebraic content of the idempotent decomposition: the two ideals $\mathbb{H} e_+$ and $\mathbb{H} e_-$ are the two summands of the semisimple algebra.

### The Idempotents

The idempotents of $\mathbb{H}_{\mathbb{D}}$ are the elements $\tilde{P}$ with $\tilde{P}^2 = \tilde{P}$. In the idempotent basis, an element $\tilde{P} = \tilde{P}_+ e_+ + \tilde{P}_- e_-$ is idempotent if and only if

$$
\tilde{P}_+^2 = \tilde{P}_+, \qquad \tilde{P}_-^2 = \tilde{P}_-.
$$

In the quaternion algebra $\mathbb{H}$, the idempotents are only $0$ and $1$. So the idempotents of $\mathbb{H}_{\mathbb{D}}$ are the four elements

$$
0, \qquad e_+, \qquad e_-, \qquad e_+ + e_- = 1.
$$

These are the only idempotents. The two nontrivial idempotents $e_+$ and $e_-$ are the ones associated with the two ideals $Z_-$ and $Z_+$ respectively (note the reversal: $e_+$ is annihilated by $Z_+$, i.e., $e_+ \in Z_-$).

Each of the idempotents $e_+$ and $e_-$ is a zero divisor, because $e_+ e_- = 0$ with both $e_+$ and $e_-$ nonzero.

### The Annihilators

For an element $\tilde{Q} \in Z_+$ (i.e., $\tilde{Q}_+ = 0$), the left annihilator is

$$
\{\tilde{R} : \tilde{R} \tilde{Q} = 0\} = \{\tilde{R} : \tilde{R} \tilde{Q}_- e_- = 0\} = \{\tilde{R} : \tilde{R}_- \tilde{Q}_- = 0\}.
$$

Since $\mathbb{H}$ is a division algebra and $\tilde{Q}_- \neq 0$ (unless $\tilde{Q} = 0$), the condition is $\tilde{R}_- = 0$, i.e., $\tilde{R} \in Z_-$. So the left annihilator of a nonzero element of $Z_+$ is $Z_-$ itself.

Similarly, the right annihilator of a nonzero element of $Z_+$ is $Z_-$. If $\tilde{Q} \in Z_+$ with $\tilde{Q} \neq 0$, then $\tilde{Q}_+ = 0$ and $\tilde{Q}_- \neq 0$, and the product $\tilde{Q} \tilde{R}$ in the idempotent basis is

$$
\tilde{Q} \tilde{R} = \tilde{Q}_+ \tilde{R}_+ e_+ + \tilde{Q}_- \tilde{R}_- e_- = \tilde{Q}_- \tilde{R}_- e_-.
$$

So $\tilde{Q} \tilde{R} = 0$ if and only if $\tilde{Q}_- \tilde{R}_- = 0$, which (since $\mathbb{H}$ is a division algebra and $\tilde{Q}_- \neq 0$) is equivalent to $\tilde{R}_- = 0$, i.e., $\tilde{R} \in Z_-$.

So the annihilator of a nonzero element of $Z_+$ is $Z_-$ on both sides: the two annihilators agree, and they are the other component of the zero divisor set, not the component containing the element. Indeed $e_+ \in Z_-$ annihilates every element of $Z_+$, while the elements of $Z_+$ do not annihilate one another.

By symmetry, the annihilator of a nonzero element of $Z_-$ is $Z_+$ on both sides.

## Comparison with the Split Complex Case

The zero divisor structure of $\mathbb{H}_{\mathbb{D}}$ is the higher-dimensional analogue of the zero divisor structure of $\mathbb{D}$.

### The Split Complex Case

In $\mathbb{D}$, the zero divisors are the elements of the form $t(1 + j)$ or $t(1 - j)$ with $t \in \mathbb{R}$, $t \neq 0$. They form the union of two real lines through the origin:

$$
\{t(1 + j) : t \in \mathbb{R}\} \cup \{t(1 - j) : t \in \mathbb{R}\}.
$$

Each line is the ideal generated by the corresponding idempotent, and the two lines intersect only at the origin.

### The Split Biquaternion Case

In $\mathbb{H}_{\mathbb{D}}$, the zero divisors are the union of two four-dimensional real subspaces $Z_+$ and $Z_-$. Each is the ideal generated by the corresponding idempotent, and the two subspaces intersect only at the origin.

### The Analogy

The analogy is exact:

| | $\mathbb{D}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|
| Dimension | 2 | 8 |
| Norm form | $r^2 - s^2$ | $\sum_\mu (q_\mu^2 + q'^2_\mu) + 2j \sum_\mu q_\mu q'_\mu$ |
| Zero divisor set | Union of two lines | Union of two four-dimensional subspaces |
| Each component | Real line | Real four-dimensional space |
| Intersection | $\{0\}$ | $\{0\}$ |
| Shape | X (two lines) | Two transverse four-spaces |

In the split complex case the zero divisor set is exactly the **null cone** of the norm form $r^2 - s^2$, a union of two lines. In the split biquaternion case this is no longer so: the norm form $N(\tilde{Q})$ is anisotropic, so its null set is the origin, and the zero divisor set is instead the zero set of the **reduced norm** $N_{\mathbb{H}}(\tilde{Q}_+) N_{\mathbb{H}}(\tilde{Q}_-)$, a quartic that vanishes exactly on $Z_+ \cup Z_-$. The name "cone" is appropriate in the sense that the set is invariant under scaling, but the set is not the zero set of a quadratic form: it is a union of two four-dimensional subspaces, which is a special feature of the split signature.

## Comparison with the Biquaternion Case

The zero divisor structure of $\mathbb{H}_{\mathbb{D}}$ is fundamentally different from that of the biquaternion algebra $\mathbb{B}$.

### The Biquaternion Case

In $\mathbb{B}$, the zero divisors are the elements with $Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = 0$ in $\mathbb{C}$. This is a complex equation, equivalent to two real equations:

$$
q_0^2 + q_1^2 + q_2^2 + q_3^2 = q'^2_0 + q'^2_1 + q'^2_2 + q'^2_3,
$$

$$
q_0 q'_0 + q_1 q'_1 + q_2 q'_2 + q_3 q'_3 = 0.
$$

The zero divisor set is a **six-dimensional cone** in $\mathbb{B} \cong \mathbb{R}^8$: it is a complex hypersurface of complex dimension $3$. It is not a union of linear subspaces; it is a single quadratic cone.

### The Split Biquaternion Case

In $\mathbb{H}_{\mathbb{D}}$, the zero divisors are the elements with $\tilde{Q}_+ = 0$ or $\tilde{Q}_- = 0$. This is a **linear** condition, and the zero divisor set is the union of two four-dimensional linear subspaces.

### The Comparison Table

| Property | $\mathbb{B}$ (biquaternion) | $\mathbb{H}_{\mathbb{D}}$ (split biquaternion) |
|---|---|---|
| Extra unit | $i$, $i^2 = -1$ | $j$, $j^2 = +1$ |
| Norm form | Complex | Split complex |
| Zero divisor condition | $Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = 0$ in $\mathbb{C}$ | $\tilde{Q}_+ = 0$ or $\tilde{Q}_- = 0$ |
| Real equations | 2 quadratic | 4 linear on each component |
| Dimension of $\mathcal{Z}$ | 6 | 4 (each component) |
| $\mathcal{Z}$ is a cone | Yes | Yes |
| $\mathcal{Z}$ is linear | No | Yes |
| Nilpotents | Yes (pure case) | No (nonzero) |

### The Key Difference

The key difference is the sign of the extra unit: $i^2 = -1$ in $\mathbb{B}$ and $j^2 = +1$ in $\mathbb{H}_{\mathbb{D}}$. This sign change has the following consequences:

- In $\mathbb{B}$, the norm form is complex-valued, and its vanishing is a quadratic condition; since $\mathbb{C}$ is a field, that condition is the zero divisor criterion, and the zero divisor set is a cone.
- In $\mathbb{H}_{\mathbb{D}}$, the norm form is split-complex-valued and anisotropic, so its vanishing is **not** the zero divisor criterion: it forces $\tilde{Q} = 0$. The criterion is instead the linear vanishing of one idempotent component, and the zero divisor set is a union of two linear subspaces.

The biquaternion zero divisor set is larger in dimension (6 out of 8) and conical. The split biquaternion zero divisor set is smaller in dimension (4 out of 8 per component) and linear.

### The Absence of Nilpotents

In $\mathbb{B}$, the zero divisors split into nilpotents (pure case) and complex multiples of idempotents (non-pure case). In $\mathbb{H}_{\mathbb{D}}$, there are **no nonzero nilpotents**. The reason is that $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H} \oplus \mathbb{H}$ is a product of two division algebras, so $\tilde{Q}^2 = 0$ forces $\tilde{Q}_+^2 = 0$ and $\tilde{Q}_-^2 = 0$, hence $\tilde{Q}_+ = \tilde{Q}_- = 0$ and $\tilde{Q} = 0$. (Semisimplicity alone would not suffice: the full matrix algebra $M_2(\mathbb{R})$ is simple and has nonzero nilpotents.) More precisely, a nonzero zero divisor $\tilde{Q}$ satisfies $\tilde{Q} \in Z_+$ or $\tilde{Q} \in Z_-$, and in either case $\tilde{Q}^2$ is a nonzero element of the same subspace, so $\tilde{Q}$ is not nilpotent.

Indeed, if $\tilde{Q} \in Z_+$ with $\tilde{Q} \neq 0$, then $\tilde{Q}_+ = 0$ and $\tilde{Q}_- \neq 0$, so

$$
\tilde{Q}^2 = \tilde{Q}_-^2 e_-,
$$

which is nonzero because $\tilde{Q}_- \neq 0$ and $\mathbb{H}$ is a division algebra. So $\tilde{Q}^2 \neq 0$, and $\tilde{Q}$ is not nilpotent.

## Distribution of the Zero Divisors

We now examine how the zero divisors are distributed among the four fixed-point subspaces of $\mathbb{H}_{\mathbb{D}}$.

### The Split Complex Subspace $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$

An element of $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ has the form $\tilde{Q} = Q_0 e_0$ with $Q_0 \in \mathbb{D}$. The norm form is $N(\tilde{Q}) = Q_0^2$, which vanishes only when $Q_0 = 0$. The element $Q_0 e_0$ is a zero divisor exactly when $Q_0$ is a zero divisor of $\mathbb{D}$, i.e., $Q_0 = t(1 \pm j)$ with $t \neq 0$. So the split complex subspace contains zero divisors, which are the images of the zero divisors of $\mathbb{D}$.

These zero divisors are in $Z_+$ (if $Q_0$ is a multiple of $1 - j$) or in $Z_-$ (if $Q_0$ is a multiple of $1 + j$). They form a one-dimensional subset of the four-dimensional subspaces $Z_\pm$.

### The Quaternion Subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$

An element of $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ has real coefficients, and its norm form is a sum of squares of real numbers, which vanishes only at the origin. So the quaternion subspace contains no zero divisors.

### The Hermitian Subspace $\mathbb{M}_+$

An element of $\mathbb{M}_+$ has the form

$$
\tilde{Q} = q_0 e_0 + j q'_1 e_1 + j q'_2 e_2 + j q'_3 e_3.
$$

The norm form is

$$
N(\tilde{Q}) = q_0^2 + (q'_1)^2 + (q'_2)^2 + (q'_3)^2,
$$

since $(j q'_k)^2 = j^2 (q'_k)^2 = +(q'_k)^2$. This is a sum of squares, so it vanishes only at the origin, and $\mathbb{M}_+$ contains no zero divisors: a nonzero element of $\mathbb{M}_+$ has $\tilde{Q}_+ = q_0 + \sum_k q'_k e_k$ and $\tilde{Q}_- = \overline{\tilde{Q}_+}$ both nonzero, hence is invertible.

### The Anti-Hermitian Subspace $\mathbb{M}_-$

An element of $\mathbb{M}_-$ has the form

$$
\tilde{Q} = j r_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3.
$$

The norm form is

$$
N(\tilde{Q}) = r_0^2 + q_1^2 + q_2^2 + q_3^2,
$$

since $(j r_0)^2 = +r_0^2$. This is a sum of squares, so it vanishes only at the origin, and $\mathbb{M}_-$ contains no zero divisors: a nonzero element of $\mathbb{M}_-$ is invertible.

### Summary of the Distribution

Of the four fixed-point subspaces:

- $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ contains zero divisors, which are the images of the zero divisors of $\mathbb{D}$.
- $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ contains no zero divisors.
- $\mathbb{M}_+$ contains no zero divisors.
- $\mathbb{M}_-$ contains no zero divisors.

In all cases, the zero divisors lie in the two subspaces $Z_+$ and $Z_-$, and the intersection of any fixed-point subspace with the zero divisor set is a subset of $Z_+ \cup Z_-$.

## The Zero Divisor Set as a Variety

The union $Z_+ \cup Z_-$ is a real algebraic variety: it is the union of the two four-dimensional linear subspaces $Z_+$ and $Z_-$, a reducible variety with two irreducible components that meet only at the origin. The zero divisor set $\mathcal{Z} = (Z_+ \cup Z_-) \setminus \{0\}$ is this variety with the origin removed.

### The Norm Form Is Not the Defining Equation

The norm form is **anisotropic**. As computed above,
$$
N(\tilde{Q}) = \sum_{\mu=0}^{3} (q_\mu^2 + q'^2_\mu) + 2j \sum_{\mu=0}^{3} q_\mu q'_\mu,
$$
so the two real equations $\mathrm{Re}\,N(\tilde{Q}) = 0$ and $\mathrm{Im}\,N(\tilde{Q}) = 0$ read
$$
\sum_{\mu=0}^{3} (q_\mu^2 + q'^2_\mu) = 0, \qquad \sum_{\mu=0}^{3} q_\mu q'_\mu = 0.
$$
The first is a sum of eight squares, so it forces all eight real components to vanish, and the common solution is the origin. The null set of the norm form is therefore $\{0\}$, and the zero divisor set is **not** the null set of $N$.

The reason the norm form does not detect the zero divisors is that it takes values in $\mathbb{D}$, which is not a field: a nonzero norm need not be invertible. The element $\tilde{Q} = e_+$ has $N(\tilde{Q}) = e_+$, a nonzero zero divisor of $\mathbb{D}$, and $\tilde{Q}$ is itself a zero divisor of $\mathbb{H}_{\mathbb{D}}$, since $e_+ e_- = 0$. So $N(\tilde{Q}) \neq 0$ does not imply that $\tilde{Q}$ is invertible.

### The Reduced Norm

It is the product of the two idempotent norms that defines the zero divisor set. Define the **reduced norm** of $\tilde{Q}$ by
$$
\Delta(\tilde{Q}) = N_{\mathbb{H}}(\tilde{Q}_+) N_{\mathbb{H}}(\tilde{Q}_-) = N(\tilde{Q}) N(\tilde{Q})^* \in \mathbb{R},
$$
where $N(\tilde{Q})^*$ is the split complex conjugate of the norm form. It is a real quartic form, the product of the two ordinary quaternion norms, and it is the determinant of the algebra in the sense of the reduced norm: the determinant of left multiplication by $\tilde{Q}$ is $\Delta(\tilde{Q})^2$. In the idempotent basis,
$$
\Delta(\tilde{Q}) = 0 \iff \tilde{Q}_+ = 0 \ \text{or}\ \tilde{Q}_- = 0.
$$
The zero divisor set is therefore
$$
\mathcal{Z} = \{\tilde{Q} \in \mathbb{H}_{\mathbb{D}} : \Delta(\tilde{Q}) = 0\} \setminus \{0\}.
$$
In the split complex algebra the zero divisor set is the null cone of the quadratic norm form $r^2 - s^2$. In the split biquaternion algebra the defining form is instead a **quartic**, and the zero divisor set is not the zero set of any quadratic form: a nonzero quadratic form on $\mathbb{R}^8$ has a null set of dimension at least $7$, whereas $Z_+ \cup Z_-$ has dimension $4$. The set is invariant under scaling, so it is a cone, but it is a cone that is a union of two linear subspaces, and it is not a quadric.

## The Reduced Norm and the Inverse

### The Inverse Formula

The norm form alone does not give an inverse. The formula
$$
\tilde{Q}^{-1} = \bar{\tilde{Q}} \, N(\tilde{Q})^{-1},
$$
which holds in the quaternion and biquaternion algebras, requires $N(\tilde{Q})$ to be **invertible in** $\mathbb{D}$, not merely nonzero. Since $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$ has zero divisors, non-vanishing is not enough: when $\tilde{Q}$ is a zero divisor, $N(\tilde{Q})$ is a nonzero zero divisor of $\mathbb{D}$, and $N(\tilde{Q})^{-1}$ does not exist.

In the idempotent basis the inverse of a unit of $\mathbb{D}$ is computed componentwise. Writing $N(\tilde{Q}) = N_+ e_+ + N_- e_-$ with $N_\pm = N_{\mathbb{H}}(\tilde{Q}_\pm) \in \mathbb{R}$,
$$
N(\tilde{Q})^{-1} = \frac{e_+}{N_+} + \frac{e_-}{N_-} = \frac{N(\tilde{Q})^*}{\Delta(\tilde{Q})},
$$
where $N(\tilde{Q})^* = N_- e_+ + N_+ e_-$ is the split complex conjugate. Substituting this into $\tilde{Q}^{-1} = \bar{\tilde{Q}} N(\tilde{Q})^{-1}$ expresses the inverse through the determinant:
$$
\tilde{Q}^{-1} = \frac{\bar{\tilde{Q}} \, N(\tilde{Q})^*}{\Delta(\tilde{Q})}, \qquad \Delta(\tilde{Q}) \neq 0.
$$
The identity is forced by multiplicativity of the norm form: $\tilde{Q} \bar{\tilde{Q}} N(\tilde{Q})^* = N(\tilde{Q}) N(\tilde{Q})^* = \Delta(\tilde{Q}) e_0$, so the right-hand side is a two-sided inverse of $\tilde{Q}$ whenever $\Delta(\tilde{Q}) \neq 0$.

### Invertibility and Zero Divisors

The reduced norm gives the invertibility criterion in its sharpest form:
$$
\tilde{Q} \text{ is invertible} \iff \Delta(\tilde{Q}) \neq 0 \iff \tilde{Q}_+ \neq 0 \text{ and } \tilde{Q}_- \neq 0.
$$
Equivalently, $\tilde{Q}$ is invertible if and only if $N(\tilde{Q}) \in \mathbb{D}^\times$, that is, if and only if the norm form is a unit of the split complex algebra. The three classes are separated by the reduced norm:
$$
\Delta(\tilde{Q}) \neq 0 : \ \tilde{Q} \text{ invertible}, \qquad
\Delta(\tilde{Q}) = 0, \ \tilde{Q} \neq 0 : \ \tilde{Q} \text{ a zero divisor}, \qquad
\tilde{Q} = 0 : \ \tilde{Q} \text{ the zero element}.
$$
The difference from the biquaternion algebra is the field. There $\mathbb{C}$ is a field, so $N(\tilde{Q}) \neq 0$ is already the invertibility criterion, and the zero divisors are exactly the nonzero elements with $N(\tilde{Q}) = 0$. In $\mathbb{H}_{\mathbb{D}}$ the norm form takes values in $\mathbb{D}$, which is not a field, so the criterion is the invertibility of $N(\tilde{Q})$ in $\mathbb{D}$, equivalently $\Delta(\tilde{Q}) \neq 0$.

## Summary

The zero divisors of the split biquaternion algebra are the nonzero elements with at least one vanishing idempotent component:
$$
\tilde{Q} \text{ is a zero divisor} \iff \tilde{Q} \neq 0 \text{ and } (\tilde{Q}_+ = 0 \text{ or } \tilde{Q}_- = 0).
$$
The condition is **linear** in the idempotent basis, and the zero divisor set is the union of the two four-dimensional real subspaces $Z_+$ and $Z_-$, which meet only at the origin. Each is a two-sided ideal of $\mathbb{H}_{\mathbb{D}}$, and the annihilator of a nonzero element of one component is the other component on both sides. The only idempotents are $0$, $e_+$, $e_-$, and $e_0$; the two nontrivial ones are zero divisors, and there are no nonzero nilpotents.

The norm form $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ is anisotropic: it vanishes only at the origin, so it does not detect the zero divisors. The invertibility criterion is that the norm form be invertible in $\mathbb{D}$, equivalently that the **reduced norm**
$$
\Delta(\tilde{Q}) = N_{\mathbb{H}}(\tilde{Q}_+) N_{\mathbb{H}}(\tilde{Q}_-) = N(\tilde{Q}) N(\tilde{Q})^* \in \mathbb{R}
$$
be nonzero. The reduced norm is a real quartic, the product of the two ordinary quaternion norms, and the zero divisors are exactly its nonzero zeros. When $\Delta(\tilde{Q}) \neq 0$ the inverse is
$$
\tilde{Q}^{-1} = \frac{\bar{\tilde{Q}} \, N(\tilde{Q})^*}{\Delta(\tilde{Q})},
$$
which reduces to $\bar{\tilde{Q}}/N(\tilde{Q})$ when $N(\tilde{Q})$ is a unit of $\mathbb{D}$.

The union $Z_+ \cup Z_-$ is a reducible real algebraic variety with two irreducible components, the two four-dimensional subspaces, and it is invariant under scaling; the zero divisor set is that union with the origin removed. It is not the null set of the norm form and not a quadric: unlike the split complex case, where the zero divisors are the null cone of the quadratic norm form, here they are the nonzero zeros of the quartic $\Delta$. The split complex subspace contains zero divisors, inherited from $\mathbb{D}$; the quaternion, Hermitian, and anti-Hermitian subspaces contain none. In the biquaternion algebra, by contrast, the zero divisor set is a single complex cone of complex dimension $3$ (real dimension $6$), because $\mathbb{C}$ is a field and the norm form itself is the criterion.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}}$ | Split biquaternion algebra |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | General split biquaternion |
| $Q_\mu = q_\mu + j q'_\mu$ | Split complex coefficient |
| $e_+ = \tfrac{1}{2}(1 + j)$ | Positive idempotent |
| $e_- = \tfrac{1}{2}(1 - j)$ | Negative idempotent |
| $\tilde{Q} = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-$ | Idempotent decomposition |
| $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | Norm form |
| $N_{\mathbb{H}}(\tilde{Q}_\pm)$ | Ordinary quaternion norm of an idempotent component |
| $\Delta(\tilde{Q}) = N_{\mathbb{H}}(\tilde{Q}_+) N_{\mathbb{H}}(\tilde{Q}_-) = N(\tilde{Q}) N(\tilde{Q})^*$ | Reduced norm (determinant) |
| $Z_+ = \{\tilde{Q} : \tilde{Q}_+ = 0\}$ | Zero-divisor subspace with vanishing $+$ component |
| $Z_- = \{\tilde{Q} : \tilde{Q}_- = 0\}$ | Zero-divisor subspace with vanishing $-$ component |
| $\mathcal{Z} = (Z_+ \cup Z_-) \setminus \{0\}$ | Zero divisor set |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation of quaternions and their complexification.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the algebraic structure, the norm form, and the zero divisors of the split biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis.
