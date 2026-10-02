
# __Split-Biquaternion Zero Divisors__

## Introduction

This article studies the zero divisors of the split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$. It follows the article on split biquaternion norm and invertibility, which established the criterion for invertibility and the three-way classification of the elements of $\mathbb{H}_{\mathbb{D}}$. The goal here is to characterize the zero divisors, to describe their structure, and to compare them with the zero divisors of the split complex algebra and of the biquaternion algebra.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra. The split complex algebra $\mathbb{D}$ is assumed from the article on split complex algebra, together with its idempotents $\tilde\Pi_+ = \tfrac{1}{2}(1 + j)$ and $\tilde\Pi_- = \tfrac{1}{2}(1 - j)$ and the isomorphism $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$. The split biquaternion algebra $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ is assumed from the preceding articles, together with its four conjugations, its four fixed-point subspaces, and its three decompositions. The split-biquaternion norm, its idempotent-basis form, and the reduced norm are used from *Split-Biquaternion Norm and Invertibility*.

Throughout, a split biquaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu = q_\mu + j q'_\mu, \quad q_\mu, q'_\mu \in \mathbb{R}.
$$

The quaternion conjugate is $\tilde{Q}^{\natural} = Q_0 e_0 - \mathbf{Q}$, where $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$. The split complex conjugate is $\bar{\tilde{Q}} = \bar{Q_0} e_0 + \mathbf{Q}^*$, where $Q_\bar{\mu} = q_\mu - j q'_\mu$. The Hermitian conjugate is $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$, and the anti-Hermitian conjugate is $\tilde{Q}^\flat = -\tilde{Q}^{*}$.

The idempotents of the split complex algebra are $\tilde\Pi_+ = \tfrac{1}{2}(1 + j)$ and $\tilde\Pi_- = \tfrac{1}{2}(1 - j)$. The idempotent decomposition of a split biquaternion is

$$
\tilde{Q} = \tilde{Q}_+ \tilde\Pi_+ + \tilde{Q}_- \tilde\Pi_-,
$$

with $\tilde{Q}_\pm = \tilde{Q} \tilde\Pi_\pm \in \mathbb{H}$ ordinary quaternions.

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

**Proof.** In the idempotent basis the product is $\tilde{Q} \tilde{R} = \tilde{Q}_+ \tilde{R}_+ \tilde\Pi_+ + \tilde{Q}_- \tilde{R}_- \tilde\Pi_-$, so $\tilde{Q} \tilde{R} = 0$ if and only if $\tilde{Q}_+ \tilde{R}_+ = 0$ and $\tilde{Q}_- \tilde{R}_- = 0$. If $\tilde{Q}_+ = 0$ and $\tilde{Q} \neq 0$, then $\tilde{Q}_- \neq 0$, and $\tilde{R} = \tilde\Pi_+ \neq 0$ satisfies $\tilde{Q} \tilde{R} = 0$, so $\tilde{Q}$ is a zero divisor. Conversely, if $\tilde{Q} \tilde{R} = 0$ with $\tilde{R} \neq 0$, then $\tilde{R}_+ \neq 0$ or $\tilde{R}_- \neq 0$; in the first case $\tilde{Q}_+ \tilde{R}_+ = 0$ with $\tilde{R}_+ \neq 0$ forces $\tilde{Q}_+ = 0$, since $\mathbb{H}$ is a division algebra, and in the second case $\tilde{Q}_- = 0$.

**Remark.** The split-biquaternion norm is not the criterion: it is anisotropic, so $N(\tilde{Q}) = 0$ forces $\tilde{Q} = 0$ (this is proved in *Split-Biquaternion Norm and Invertibility*). The zero divisor condition is **linear** in the idempotent basis.

### The Criterion in the Idempotent Basis

In the idempotent basis the criterion is simply the vanishing of one component. Writing $\tilde{Q} = \tilde{Q}_+ \tilde\Pi_+ + \tilde{Q}_- \tilde\Pi_-$ with $\tilde{Q}_\pm \in \mathbb{H}$,

$$
\tilde{Q} \text{ is a zero divisor} \iff \tilde{Q} \neq 0 \text{ and } (\tilde{Q}_+ = 0 \text{ or } \tilde{Q}_- = 0).
$$

This is a **linear** condition in the idempotent basis, in contrast to the quadratic condition $N(\tilde{Q}) = 0$ that characterises the zero divisors of the biquaternion algebra. The two families of the criterion are the two four-dimensional subspaces studied next.

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

**$Z_+$.** An element of $Z_+$ satisfies $\tilde{Q} \tilde\Pi_+ = 0$, i.e., $\tilde{Q}(1 + j) = 0$. Writing $\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ with $Q_\mu \in \mathbb{D}$, the condition is that each coefficient $Q_\mu$ is a split complex multiple of $1 - j$. Since the ideal generated by $1 - j$ in $\mathbb{D}$ is the one-dimensional real subspace $\mathbb{R}(1 - j)$, the condition is

$$
Q_\mu = t_\mu (1 - j), \qquad t_\mu \in \mathbb{R}.
$$

There are four real parameters $t_0, t_1, t_2, t_3$, so $Z_+$ is four-dimensional. It is isomorphic to $\mathbb{H}$ via the map $\tilde{Q} \mapsto (t_0, t_1, t_2, t_3)$.

**$Z_-$.** An element of $Z_-$ satisfies $\tilde{Q} \tilde\Pi_- = 0$, i.e., $\tilde{Q}(1 - j) = 0$. The condition is that each coefficient $Q_\mu$ is a split complex multiple of $1 + j$:

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

The zero divisor set has real dimension $4$ in the sense that each of the two components is four-dimensional. That the union $Z_+ \cup Z_-$ is not a manifold at the origin, that away from the origin it is a disjoint union of two four-dimensional submanifolds, and its differential structure, are analytic and topological statements and are in *Split-Biquaternion Topology* and *Split-Biquaternion Analysis*; only the dimension count, which is algebraic, is used here.

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
| Norm | $r^2 - s^2$ | $\sum_\mu (q_\mu^2 + q'^2_\mu) + 2j \sum_\mu q_\mu q'_\mu$ |
| Zero divisor set | Union of two lines | Union of two four-dimensional subspaces |
| Each component | Real line | Real four-dimensional space |
| Intersection | $\{0\}$ | $\{0\}$ |
| Shape | X (two lines) | Two transverse four-spaces |

In the split complex case the zero divisor set is exactly the **null cone** of the norm $r^2 - s^2$, a union of two lines. In the split biquaternion case this is no longer so: the split-biquaternion norm $N(\tilde{Q})$ is anisotropic, so its null set is the origin, and the zero divisor set is instead the zero set of the **reduced norm** $N_{\mathbb{H}}(\tilde{Q}_+) N_{\mathbb{H}}(\tilde{Q}_-)$, a quartic that vanishes exactly on $Z_+ \cup Z_-$. The name "cone" is appropriate in the sense that the set is invariant under scaling, but the set is not the zero set of a quadratic form: it is a union of two four-dimensional subspaces, which is a special feature of the split signature.

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
| Norm | Complex | Split complex |
| Zero divisor condition | $Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = 0$ in $\mathbb{C}$ | $\tilde{Q}_+ = 0$ or $\tilde{Q}_- = 0$ |
| Real equations | 2 quadratic | 4 linear on each component |
| Dimension of $\mathcal{Z}$ | 6 | 4 (each component) |
| $\mathcal{Z}$ is a cone | Yes | Yes |
| $\mathcal{Z}$ is linear | No | Yes |
| Nilpotents | Yes (pure case) | No (nonzero) |

### The Key Difference

The key difference is the sign of the extra unit: $i^2 = -1$ in $\mathbb{B}$ and $j^2 = +1$ in $\mathbb{H}_{\mathbb{D}}$. This sign change has the following consequences:

- In $\mathbb{B}$, the norm is complex-valued, and its vanishing is a quadratic condition; since $\mathbb{C}$ is a field, that condition is the zero divisor criterion, and the zero divisor set is a cone.
- In $\mathbb{H}_{\mathbb{D}}$, the split-biquaternion norm is split-complex-valued and anisotropic, so its vanishing is **not** the zero divisor criterion: it forces $\tilde{Q} = 0$. The criterion is instead the linear vanishing of one idempotent component, and the zero divisor set is a union of two linear subspaces.

The biquaternion zero divisor set is larger in dimension (6 out of 8) and conical. The split biquaternion zero divisor set is smaller in dimension (4 out of 8 per component) and linear.

### The Absence of Nilpotents

In $\mathbb{B}$, the zero divisors split into nilpotents (pure case) and complex multiples of idempotents (non-pure case). In $\mathbb{H}_{\mathbb{D}}$, there are **no nonzero nilpotents**. The reason is that $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H} \oplus \mathbb{H}$ is a product of two division algebras, so $\tilde{Q}^2 = 0$ forces $\tilde{Q}_+^2 = 0$ and $\tilde{Q}_-^2 = 0$, hence $\tilde{Q}_+ = \tilde{Q}_- = 0$ and $\tilde{Q} = 0$. (Semisimplicity alone would not suffice: the full matrix algebra $M_2(\mathbb{R})$ is simple and has nonzero nilpotents.) More precisely, a nonzero zero divisor $\tilde{Q}$ satisfies $\tilde{Q} \in Z_+$ or $\tilde{Q} \in Z_-$, and in either case $\tilde{Q}^2$ is a nonzero element of the same subspace, so $\tilde{Q}$ is not nilpotent.

Indeed, if $\tilde{Q} \in Z_+$ with $\tilde{Q} \neq 0$, then $\tilde{Q}_+ = 0$ and $\tilde{Q}_- \neq 0$, so

$$
\tilde{Q}^2 = \tilde{Q}_-^2 \tilde\Pi_-,
$$

which is nonzero because $\tilde{Q}_- \neq 0$ and $\mathbb{H}$ is a division algebra. So $\tilde{Q}^2 \neq 0$, and $\tilde{Q}$ is not nilpotent.

## Distribution of the Zero Divisors

We now examine how the zero divisors are distributed among the four fixed-point subspaces of $\mathbb{H}_{\mathbb{D}}$.

### The Split Complex Subspace $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$

An element of $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ has the form $\tilde{Q} = Q_0 e_0$ with $Q_0 \in \mathbb{D}$. Writing $Q_0 = A + jB$ with real $A, B$, its idempotent components correspond to the real numbers $A \pm B$, so exactly one component vanishes when $Q_0$ is a nonzero multiple of $1 \mp j$. The element $Q_0 e_0$ is therefore a zero divisor exactly when $Q_0$ is a zero divisor of $\mathbb{D}$, that is, $Q_0 = t(1 \pm j)$ with $t \neq 0$. So the split complex subspace contains zero divisors, which are the images of the zero divisors of $\mathbb{D}$.

These zero divisors are in $Z_+$ (if $Q_0$ is a multiple of $1 - j$) or in $Z_-$ (if $Q_0$ is a multiple of $1 + j$). They form a one-dimensional subset of the four-dimensional subspaces $Z_\pm$.

### The Quaternion Subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$

An element of $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ has real coefficients, so it has the form $\tilde{Q} = A$ with $A \in \mathbb{H}$, and its idempotent components correspond to $A$ in both summands. Both components vanish only when $\tilde{Q} = 0$, so the quaternion subspace contains no zero divisors.

### The Hermitian Subspace $\mathbb{M}_+$

An element of $\mathbb{M}_+$ has the form

$$
\tilde{Q} = q_0 e_0 + j q'_1 e_1 + j q'_2 e_2 + j q'_3 e_3 = A + jB, \qquad A = q_0, \quad B = q'_1 e_1 + q'_2 e_2 + q'_3 e_3.
$$

Its idempotent components correspond to the quaternions $A \pm B = q_0 \pm (q'_1 e_1 + q'_2 e_2 + q'_3 e_3)$, each of which vanishes only when its four real coefficients do. The component $A + B$ vanishes exactly when $q_0 = q'_1 = q'_2 = q'_3 = 0$, and $A - B$ likewise, so both components vanish only at the origin. Hence $\mathbb{M}_+$ contains no zero divisors.

### The Anti-Hermitian Subspace $\mathbb{M}_-$

An element of $\mathbb{M}_-$ has the form

$$
\tilde{Q} = j r_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3 = A + jB, \qquad A = q_1 e_1 + q_2 e_2 + q_3 e_3, \quad B = r_0.
$$

Its idempotent components correspond to $A \pm B = (q_1 e_1 + q_2 e_2 + q_3 e_3) \pm r_0$, each vanishing only when $q_1 = q_2 = q_3 = r_0 = 0$. Hence $\mathbb{M}_-$ contains no zero divisors.

### Summary of the Distribution

Of the four fixed-point subspaces:

- $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ contains zero divisors, which are the images of the zero divisors of $\mathbb{D}$.
- $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ contains no zero divisors.
- $\mathbb{M}_+$ contains no zero divisors.
- $\mathbb{M}_-$ contains no zero divisors.

In all cases, the zero divisors lie in the two subspaces $Z_+$ and $Z_-$, and the intersection of any fixed-point subspace with the zero divisor set is a subset of $Z_+ \cup Z_-$.

## The Structure of the Zero Divisors

### Algebraic Structure of the Two Families

Each of $Z_+$ and $Z_-$ is a **left ideal** and a **right ideal** of $\mathbb{H}_{\mathbb{D}}$. Indeed:

- If $\tilde{Q} \in Z_+$ and $\tilde{R} \in \mathbb{H}_{\mathbb{D}}$, then $(\tilde{Q} \tilde{R}) \tilde\Pi_+ = \tilde{Q} (\tilde{R} \tilde\Pi_+) = \tilde{Q} \tilde\Pi_+ \tilde{R}_+ = 0 \cdot \tilde{R}_+ = 0$, so $\tilde{Q} \tilde{R} \in Z_+$. So $Z_+$ is a right ideal.
- Similarly, $(\tilde{R} \tilde{Q}) \tilde\Pi_+ = \tilde{R} (\tilde{Q} \tilde\Pi_+) = 0$, so $\tilde{R} \tilde{Q} \in Z_+$. So $Z_+$ is a left ideal.

So $Z_+$ and $Z_-$ are two-sided ideals of $\mathbb{H}_{\mathbb{D}}$. This is the algebraic content of the idempotent decomposition: the two ideals $\mathbb{H} \tilde\Pi_+$ and $\mathbb{H} \tilde\Pi_-$ are the two summands of the semisimple algebra.

### The Idempotents

The idempotents of $\mathbb{H}_{\mathbb{D}}$ are the elements $\tilde P$ with $\tilde P^2 = \tilde P$. In the idempotent basis, an element $\tilde P = \tilde P_+ \tilde\Pi_+ + \tilde P_- \tilde\Pi_-$ is idempotent if and only if

$$
\tilde P_+^2 = \tilde P_+, \qquad \tilde P_-^2 = \tilde P_-.
$$

In the quaternion algebra $\mathbb{H}$, the idempotents are only $0$ and $1$. So the idempotents of $\mathbb{H}_{\mathbb{D}}$ are the four elements

$$
0, \qquad \tilde\Pi_+, \qquad \tilde\Pi_-, \qquad \tilde\Pi_+ + \tilde\Pi_- = 1.
$$

These are the only idempotents. The two nontrivial idempotents $\tilde\Pi_+$ and $\tilde\Pi_-$ are the ones associated with the two ideals $Z_-$ and $Z_+$ respectively (note the reversal: $\tilde\Pi_+$ is annihilated by $Z_+$, i.e., $\tilde\Pi_+ \in Z_-$).

Each of the idempotents $\tilde\Pi_+$ and $\tilde\Pi_-$ is a zero divisor, because $\tilde\Pi_+ \tilde\Pi_- = 0$ with both $\tilde\Pi_+$ and $\tilde\Pi_-$ nonzero.

### The Annihilators

For an element $\tilde{Q} \in Z_+$ (i.e., $\tilde{Q}_+ = 0$), the left annihilator is

$$
\{\tilde{R} : \tilde{R} \tilde{Q} = 0\} = \{\tilde{R} : \tilde{R} \tilde{Q}_- \tilde\Pi_- = 0\} = \{\tilde{R} : \tilde{R}_- \tilde{Q}_- = 0\}.
$$

Since $\mathbb{H}$ is a division algebra and $\tilde{Q}_- \neq 0$ (unless $\tilde{Q} = 0$), the condition is $\tilde{R}_- = 0$, i.e., $\tilde{R} \in Z_-$. So the left annihilator of a nonzero element of $Z_+$ is $Z_-$ itself.

Similarly, the right annihilator of a nonzero element of $Z_+$ is $Z_-$. If $\tilde{Q} \in Z_+$ with $\tilde{Q} \neq 0$, then $\tilde{Q}_+ = 0$ and $\tilde{Q}_- \neq 0$, and the product $\tilde{Q} \tilde{R}$ in the idempotent basis is

$$
\tilde{Q} \tilde{R} = \tilde{Q}_+ \tilde{R}_+ \tilde\Pi_+ + \tilde{Q}_- \tilde{R}_- \tilde\Pi_- = \tilde{Q}_- \tilde{R}_- \tilde\Pi_-.
$$

So $\tilde{Q} \tilde{R} = 0$ if and only if $\tilde{Q}_- \tilde{R}_- = 0$, which (since $\mathbb{H}$ is a division algebra and $\tilde{Q}_- \neq 0$) is equivalent to $\tilde{R}_- = 0$, i.e., $\tilde{R} \in Z_-$.

So the annihilator of a nonzero element of $Z_+$ is $Z_-$ on both sides: the two annihilators agree, and they are the other component of the zero divisor set, not the component containing the element. Indeed $\tilde\Pi_+ \in Z_-$ annihilates every element of $Z_+$, while the elements of $Z_+$ do not annihilate one another.

By symmetry, the annihilator of a nonzero element of $Z_-$ is $Z_+$ on both sides.

## The Zero Divisor Set as a Variety

The union $Z_+ \cup Z_-$ is a real algebraic variety: it is the union of the two four-dimensional linear subspaces $Z_+$ and $Z_-$, a reducible variety with two irreducible components that meet only at the origin. The zero divisor set $\mathcal{Z} = (Z_+ \cup Z_-) \setminus \{0\}$ is this variety with the origin removed.

### The Set Is Not Defined by the Split-Biquaternion Norm

The zero divisor set is not detected by the split-biquaternion norm: the split-biquaternion norm $N$ is anisotropic, so $N(\tilde{Q}) = 0$ forces $\tilde{Q} = 0$ and the zero divisor set is not the null set of $N$. The reason is that $N$ takes values in $\mathbb{D}$, which is not a field: the element $\tilde{Q} = \tilde\Pi_+$ has $N(\tilde{Q}) = \tilde\Pi_+$, a nonzero zero divisor of $\mathbb{D}$, yet $\tilde{Q}\tilde\Pi_- = 0$ makes $\tilde{Q}$ a zero divisor of $\mathbb{H}_{\mathbb{D}}$. The defining form of the set, the reduced norm, and the proof of the anisotropy are in *Split-Biquaternion Norm and Invertibility*.

### The Set Is Not a Quadric

The set $Z_+ \cup Z_-$ is a reducible variety with two irreducible components of dimension four, invariant under scaling. It is not the zero set of a single quadratic form: a nonzero quadratic form on $\mathbb{R}^8$ has a zero set of dimension at least seven, whereas $Z_+ \cup Z_-$ has dimension four. In the split complex algebra, by contrast, the zero divisor set is cut out by one quadratic form.

## Summary

The zero divisors of the split biquaternion algebra are the nonzero elements with at least one vanishing idempotent component:
$$
\tilde{Q} \text{ is a zero divisor} \iff \tilde{Q} \neq 0 \text{ and } (\tilde{Q}_+ = 0 \text{ or } \tilde{Q}_- = 0).
$$
The condition is **linear** in the idempotent basis, and the zero divisor set is the union of the two four-dimensional real subspaces $Z_+$ and $Z_-$, which meet only at the origin. Each is a two-sided ideal of $\mathbb{H}_{\mathbb{D}}$, and the annihilator of a nonzero element of one component is the other component on both sides. The only idempotents are $0$, $\tilde\Pi_+$, $\tilde\Pi_-$, and $e_0$; the two nontrivial ones are zero divisors, and there are no nonzero nilpotents.

The criterion is not the vanishing of the split-biquaternion norm. The split-biquaternion norm $N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural}$ is anisotropic, so it vanishes only at the origin and does not detect the zero divisors; the detecting quantity is the **reduced norm**
$$
\Delta(\tilde{Q}) = N_{\mathbb{H}}(\tilde{Q}_+) N_{\mathbb{H}}(\tilde{Q}_-) = N(\tilde{Q}) N(\tilde{Q})^* \in \mathbb{R},
$$
a real quartic and the product of the two ordinary quaternion norms, whose nonzero zeros are exactly the zero divisors. The split-biquaternion norm, the reduced norm, the invertibility criterion, and the inverse formula are studied in *Split-Biquaternion Norm and Invertibility*.

The union $Z_+ \cup Z_-$ is a reducible real algebraic variety with two irreducible components, the two four-dimensional subspaces, and it is invariant under scaling; the zero divisor set is that union with the origin removed. It is not the null set of the split-biquaternion norm and not a quadric: unlike the split complex case, where the zero divisors are the null cone of the quadratic norm, here they are the nonzero zeros of the quartic $\Delta$. The split complex subspace contains zero divisors, inherited from $\mathbb{D}$; the quaternion, Hermitian, and anti-Hermitian subspaces contain none. In the biquaternion algebra, by contrast, the zero divisor set is a single complex cone of complex dimension $3$ (real dimension $6$), because $\mathbb{C}$ is a field and the norm itself is the criterion.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}}$ | Split biquaternion algebra |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | General split biquaternion |
| $Q_\mu = q_\mu + j q'_\mu$ | Split complex coefficient |
| $\tilde\Pi_+ = \tfrac{1}{2}(1 + j)$ | Positive idempotent |
| $\tilde\Pi_- = \tfrac{1}{2}(1 - j)$ | Negative idempotent |
| $\tilde{Q} = \tilde{Q}_+ \tilde\Pi_+ + \tilde{Q}_- \tilde\Pi_-$ | Idempotent decomposition |
| $N(\tilde{Q}) = \tilde{Q} \tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ | Split-Biquaternion norm |
| $N_{\mathbb{H}}(\tilde{Q}_\pm)$ | Ordinary quaternion norm of an idempotent component |
| $\Delta(\tilde{Q}) = N_{\mathbb{H}}(\tilde{Q}_+) N_{\mathbb{H}}(\tilde{Q}_-) = N(\tilde{Q}) N(\tilde{Q})^*$ | Reduced norm (determinant) |
| $Z_+ = \{\tilde{Q} : \tilde{Q}_+ = 0\}$ | Zero-divisor subspace with vanishing $+$ component |
| $Z_- = \{\tilde{Q} : \tilde{Q}_- = 0\}$ | Zero-divisor subspace with vanishing $-$ component |
| $\mathcal{Z} = (Z_+ \cup Z_-) \setminus \{0\}$ | Zero divisor set |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation of quaternions and their complexification.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the algebraic structure, the split-biquaternion norm, and the zero divisors of the split biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis.
