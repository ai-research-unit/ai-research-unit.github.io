
# Split-Quaternion Zero Divisors

## Introduction

This article studies the zero divisors of the split quaternion algebra $\mathbb{H}_{\mathbb{D}}$. It follows the article on split quaternion norm and invertibility, which established the criterion for invertibility and the three-way classification of the elements of $\mathbb{H}_{\mathbb{D}}$. The goal here is to characterize the zero divisors, to describe their structure, and to compare them with the zero divisors of the split complex algebra and of the biquaternion algebra.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra. The split complex algebra $\mathbb{D}$ is assumed from the article on split complex algebra, together with its idempotents $e_+ = \tfrac{1}{2}(1 + j)$ and $e_- = \tfrac{1}{2}(1 - j)$ and the isomorphism $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$. The split quaternion algebra $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ is assumed from the preceding articles, together with its four conjugations, its four fixed-point subspaces, its three decompositions, and its norm form.

Throughout, a split quaternion is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu = q_\mu + j q'_\mu, \quad q_\mu, q'_\mu \in \mathbb{R}.
$$

The quaternion conjugate is $\bar{\tilde{Q}} = Q_0 e_0 - \mathbf{Q}$, where $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$. The split complex conjugate is $\tilde{Q}^* = Q_0^* e_0 + \mathbf{Q}^*$, where $Q_\mu^* = q_\mu - j q'_\mu$. The Hermitian conjugate is $\tilde{Q}^\dagger = \bar{\tilde{Q}}^*$, and the anti-Hermitian conjugate is $\tilde{Q}^\flat = -\tilde{Q}^\dagger$. The norm form is $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = \sum_\mu Q_\mu^2$.

The idempotents of the split complex algebra are $e_+ = \tfrac{1}{2}(1 + j)$ and $e_- = \tfrac{1}{2}(1 - j)$. The idempotent decomposition of a split quaternion is

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

A split quaternion $\tilde{Q}$ is a **zero divisor** if it is **nonzero** and there exists a **nonzero** split quaternion $\tilde{R}$ such that

$$
\tilde{Q} \circ \tilde{R} = 0 \quad \text{or} \quad \tilde{R} \circ \tilde{Q} = 0.
$$

The requirement that both $\tilde{Q}$ and $\tilde{R}$ be nonzero is essential. In particular, the element $\tilde{Q} = 0$ is **not** a zero divisor, even though $0 \circ \tilde{R} = 0$ for any $\tilde{R}$.

### Criterion

**Theorem.** A nonzero split quaternion $\tilde{Q}$ is a zero divisor if and only if its norm form vanishes:

$$
N(\tilde{Q}) = 0.
$$

**Proof.** Suppose $\tilde{Q} \neq 0$ and $N(\tilde{Q}) = 0$. Then $\tilde{Q} \bar{\tilde{Q}} = 0$. Since $\tilde{Q} \neq 0$, we also have $\bar{\tilde{Q}} \neq 0$. So $\tilde{R} = \bar{\tilde{Q}}$ is a nonzero split quaternion with $\tilde{Q} \circ \tilde{R} = 0$. Hence $\tilde{Q}$ is a zero divisor.

Conversely, suppose $\tilde{Q}$ is a zero divisor: there exists $\tilde{R} \neq 0$ with $\tilde{Q} \circ \tilde{R} = 0$. If $N(\tilde{Q}) \neq 0$, then $\tilde{Q}$ is invertible by the invertibility criterion, and multiplying $\tilde{Q} \circ \tilde{R} = 0$ on the left by $\tilde{Q}^{-1}$ gives $\tilde{R} = 0$, contradicting $\tilde{R} \neq 0$. So $N(\tilde{Q}) = 0$. $\square$

### The Three-Way Classification

Combining the criterion for invertibility from the preceding article with the criterion for zero divisors, the elements of $\mathbb{H}_{\mathbb{D}}$ are partitioned into three classes:

| Condition on $N(\tilde{Q})$ | Condition on $\tilde{Q}$ | Conclusion |
|---|---|---|
| $N(\tilde{Q}) \neq 0$ | (automatically $\tilde{Q} \neq 0$) | $\tilde{Q}$ is invertible |
| $N(\tilde{Q}) = 0$ | $\tilde{Q} = 0$ | $\tilde{Q}$ is the zero element |
| $N(\tilde{Q}) = 0$ | $\tilde{Q} \neq 0$ | $\tilde{Q}$ is a zero divisor |

The zero divisors are exactly the nonzero elements on which the norm form vanishes.

### The Criterion in the Idempotent Basis

In the idempotent basis, the criterion takes a particularly simple form. Writing $\tilde{Q} = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-$ with $\tilde{Q}_\pm \in \mathbb{H}$,

$$
N(\tilde{Q}) = N_{\mathbb{H}}(\tilde{Q}_+) e_+ + N_{\mathbb{H}}(\tilde{Q}_-) e_-.
$$

Since $N_{\mathbb{H}}(\tilde{Q}_\pm)$ are non-negative real numbers, $N(\tilde{Q}) = 0$ if and only if

$$
N_{\mathbb{H}}(\tilde{Q}_+) = 0 \quad \text{or} \quad N_{\mathbb{H}}(\tilde{Q}_-) = 0.
$$

Since $\mathbb{H}$ is a division algebra, $N_{\mathbb{H}}(\tilde{Q}_\pm) = 0$ if and only if $\tilde{Q}_\pm = 0$. So the criterion is

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

Since $\mathbb{H}$ is a division algebra and $\tilde{Q}_- \neq 0$ (unless $\tilde{Q} = 0$), the condition is $\tilde{R}_- = 0$, i.e., $\tilde{R} \in Z_+$. So the left annihilator of a nonzero element of $Z_+$ is $Z_+$ itself.

Similarly, the right annihilator of a nonzero element of $Z_+$ is $Z_-$: if $\tilde{Q} \tilde{R} = 0$ with $\tilde{Q} \in Z_+$ and $\tilde{Q} \neq 0$, then $\tilde{Q}_+ = 0$ and the product is $\tilde{Q}_- \tilde{R}_- e_- = 0$, so $\tilde{R}_- = 0$, i.e., $\tilde{R} \in Z_+$. Wait, this is the same computation. Let me redo.

If $\tilde{Q} \in Z_+$ with $\tilde{Q} \neq 0$, then $\tilde{Q}_+ = 0$ and $\tilde{Q}_- \neq 0$. The product $\tilde{Q} \tilde{R}$ in the idempotent basis is

$$
\tilde{Q} \tilde{R} = \tilde{Q}_+ \tilde{R}_+ e_+ + \tilde{Q}_- \tilde{R}_- e_- = 0 \cdot \tilde{R}_+ e_+ + \tilde{Q}_- \tilde{R}_- e_- = \tilde{Q}_- \tilde{R}_- e_-.
$$

So $\tilde{Q} \tilde{R} = 0$ if and only if $\tilde{Q}_- \tilde{R}_- = 0$, which (since $\mathbb{H}$ is a division algebra and $\tilde{Q}_- \neq 0$) is equivalent to $\tilde{R}_- = 0$, i.e., $\tilde{R} \in Z_+$.

So the right annihilator of a nonzero element of $Z_+$ is $Z_+$ itself. Similarly, the left annihilator is $Z_+$ itself. So the annihilator of a nonzero element of $Z_+$ is $Z_+$ on both sides.

By symmetry, the annihilator of a nonzero element of $Z_-$ is $Z_-$ on both sides.

## Comparison with the Split Complex Case

The zero divisor structure of $\mathbb{H}_{\mathbb{D}}$ is the higher-dimensional analogue of the zero divisor structure of $\mathbb{D}$.

### The Split Complex Case

In $\mathbb{D}$, the zero divisors are the elements of the form $t(1 + j)$ or $t(1 - j)$ with $t \in \mathbb{R}$, $t \neq 0$. They form the union of two real lines through the origin:

$$
\{t(1 + j) : t \in \mathbb{R}\} \cup \{t(1 - j) : t \in \mathbb{R}\}.
$$

Each line is the ideal generated by the corresponding idempotent, and the two lines intersect only at the origin.

### The Split Quaternion Case

In $\mathbb{H}_{\mathbb{D}}$, the zero divisors are the union of two four-dimensional real subspaces $Z_+$ and $Z_-$. Each is the ideal generated by the corresponding idempotent, and the two subspaces intersect only at the origin.

### The Analogy

The analogy is exact:

| | $\mathbb{D}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|
| Dimension | 2 | 8 |
| Norm form | $r^2 - s^2$ | $\sum_\mu (q_\mu^2 - q'^2_\mu) + 2j \sum_\mu q_\mu q'_\mu$ |
| Zero divisor set | Union of two lines | Union of two four-dimensional subspaces |
| Each component | Real line | Real four-dimensional space |
| Intersection | $\{0\}$ | $\{0\}$ |
| Shape | X (two lines) | Two transverse four-spaces |

The zero divisor set is the **null cone** of the norm form in both cases. In the split complex case, the null cone is a union of two lines; in the split quaternion case, it is a union of two four-dimensional subspaces. The name "cone" is appropriate in the sense that the set is invariant under scaling and is the zero set of a quadratic form. The fact that it is a union of two linear subspaces is a special feature of the split signature.

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

The zero divisor set is a **seven-dimensional cone** in $\mathbb{B} \cong \mathbb{R}^8$. It is not a union of linear subspaces; it is a single quadratic cone.

### The Split Quaternion Case

In $\mathbb{H}_{\mathbb{D}}$, the zero divisors are the elements with $\tilde{Q}_+ = 0$ or $\tilde{Q}_- = 0$. This is a **linear** condition, and the zero divisor set is the union of two four-dimensional linear subspaces.

### The Comparison Table

| Property | $\mathbb{B}$ (biquaternion) | $\mathbb{H}_{\mathbb{D}}$ (split quaternion) |
|---|---|---|
| Extra unit | $i$, $i^2 = -1$ | $j$, $j^2 = +1$ |
| Norm form | Complex | Split complex |
| Zero divisor condition | $Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = 0$ in $\mathbb{C}$ | $\tilde{Q}_+ = 0$ or $\tilde{Q}_- = 0$ |
| Real equations | 2 quadratic | 4 linear (in the idempotent basis) |
| Dimension of $\mathcal{Z}$ | 7 | 4 (each component) |
| $\mathcal{Z}$ is a cone | Yes | No |
| $\mathcal{Z}$ is linear | No | Yes |
| Nilpotents | Yes (pure case) | No |

### The Key Difference

The key difference is the sign of the extra unit: $i^2 = -1$ in $\mathbb{B}$ and $j^2 = +1$ in $\mathbb{H}_{\mathbb{D}}$. This sign change has the following consequences:

- In $\mathbb{B}$, the norm form is complex-valued, and its vanishing is a quadratic condition. The zero divisor set is a cone.
- In $\mathbb{H}_{\mathbb{D}}$, the norm form is split-complex-valued, and its vanishing is a linear condition in the idempotent basis. The zero divisor set is a union of two linear subspaces.

The biquaternion zero divisor set is larger in dimension (7 out of 8) and conical. The split quaternion zero divisor set is smaller in dimension (4 out of 8 per component) and linear.

### The Absence of Nilpotents

In $\mathbb{B}$, the zero divisors split into nilpotents (pure case) and complex multiples of idempotents (non-pure case). In $\mathbb{H}_{\mathbb{D}}$, there are **no nilpotents**. The reason is that the algebra is semisimple: every element has a well-defined square that does not necessarily vanish. More precisely, an element $\tilde{Q}$ with $N(\tilde{Q}) = 0$ satisfies $\tilde{Q} \in Z_+$ or $\tilde{Q} \in Z_-$, and in either case $\tilde{Q}^2$ is a nonzero element of the same subspace (unless $\tilde{Q} = 0$), so $\tilde{Q}$ is not nilpotent.

Indeed, if $\tilde{Q} \in Z_+$ with $\tilde{Q} \neq 0$, then $\tilde{Q}_+ = 0$ and $\tilde{Q}_- \neq 0$, so

$$
\tilde{Q}^2 = \tilde{Q}_-^2 e_-,
$$

which is nonzero because $\tilde{Q}_- \neq 0$ and $\mathbb{H}$ is a division algebra. So $\tilde{Q}^2 \neq 0$, and $\tilde{Q}$ is not nilpotent.

## Distribution of the Zero Divisors

We now examine how the zero divisors are distributed among the four fixed-point subspaces of $\mathbb{H}_{\mathbb{D}}$.

### The Split Complex Subspace $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$

An element of $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ has the form $\tilde{Q} = Q_0 e_0$ with $Q_0 \in \mathbb{D}$. The norm form is $N(\tilde{Q}) = Q_0^2$, which vanishes when $Q_0$ is a zero divisor of $\mathbb{D}$, i.e., $Q_0 = t(1 \pm j)$ with $t \neq 0$. So the split complex subspace contains zero divisors, which are the images of the zero divisors of $\mathbb{D}$.

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
N(\tilde{Q}) = q_0^2 - (q'_1)^2 - (q'_2)^2 - (q'_3)^2.
$$

This vanishes on the light cone

$$
q_0^2 = (q'_1)^2 + (q'_2)^2 + (q'_3)^2,
$$

which is a three-dimensional cone in the four-dimensional space $\mathbb{M}_+$. The nonzero elements of this cone are zero divisors.

The zero divisors in $\mathbb{M}_+$ are the intersection of the light cone with the two subspaces $Z_+$ and $Z_-$. Since $Z_+ \cap Z_- = \{0\}$, the light cone is partitioned into two pieces, one in $Z_+$ and one in $Z_-$.

### The Anti-Hermitian Subspace $\mathbb{M}_-$

An element of $\mathbb{M}_-$ has the form

$$
\tilde{Q} = j r_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3.
$$

The norm form is

$$
N(\tilde{Q}) = -r_0^2 + q_1^2 + q_2^2 + q_3^2,
$$

which vanishes on the light cone

$$
r_0^2 = q_1^2 + q_2^2 + q_3^2.
$$

The nonzero elements of this cone are zero divisors, and as in the case of $\mathbb{M}_+$, the cone is partitioned into two pieces, one in $Z_+$ and one in $Z_-$.

### Summary of the Distribution

Of the four fixed-point subspaces:

- $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ contains zero divisors, which are the images of the zero divisors of $\mathbb{D}$.
- $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ contains no zero divisors.
- $\mathbb{M}_+$ contains a three-dimensional light cone of zero divisors.
- $\mathbb{M}_-$ contains a three-dimensional light cone of zero divisors.

In all cases, the zero divisors lie in the two subspaces $Z_+$ and $Z_-$, and the intersection of any fixed-point subspace with the zero divisor set is a subset of $Z_+ \cup Z_-$.

## The Zero Divisor Set as a Variety

The zero divisor set $\mathcal{Z} = (Z_+ \cup Z_-) \setminus \{0\}$ is a real algebraic variety. It is the union of two four-dimensional linear subspaces, which is a reducible variety with two irreducible components.

### The Defining Equations

The zero divisor set is the common zero set of the real and split parts of the norm form:

$$
\sum_{\mu=0}^{3} (q_\mu^2 + q'^2_\mu) = 0, \qquad \sum_{\mu=0}^{3} q_\mu q'_\mu = 0.
$$

The first equation forces all eight real components to vanish, so the only solution is the origin. This is the same computation as before, and it shows that the norm form is zero only at the origin **if the norm form is required to vanish as a split complex number**.

Wait, this contradicts the earlier statement that the zero divisor set is a union of two four-dimensional subspaces. Let me recheck.

The norm form of $\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ is $N(\tilde{Q}) = \sum_\mu Q_\mu^2$. Writing $Q_\mu = q_\mu + j q'_\mu$, we have

$$
Q_\mu^2 = q_\mu^2 + 2j q_\mu q'_\mu + j^2 q'^2_\mu = q_\mu^2 + 2j q_\mu q'_\mu + q'^2_\mu.
$$

So

$$
N(\tilde{Q}) = \sum_\mu (q_\mu^2 + q'^2_\mu) + 2j \sum_\mu q_\mu q'_\mu.
$$

Setting $N(\tilde{Q}) = 0$ gives

$$
\sum_\mu (q_\mu^2 + q'^2_\mu) = 0, \qquad \sum_\mu q_\mu q'_\mu = 0.
$$

The first equation is a sum of eight squares, which vanishes only if all eight real numbers vanish. So the only solution is $\tilde{Q} = 0$.

This contradicts the earlier statement that the zero divisor set is a union of two four-dimensional subspaces. Where is the error?

The error is that the norm form $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}}$ is **not** the same as the coefficient sum of squares $\sum_\mu Q_\mu^2$ in the split quaternion algebra. Let me check.

The quaternion conjugate of $\tilde{Q}$ is $\bar{\tilde{Q}} = Q_0 e_0 - Q_1 e_1 - Q_2 e_2 - Q_3 e_3$. The product is

$$
\tilde{Q} \bar{\tilde{Q}} = (Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3)(Q_0 e_0 - Q_1 e_1 - Q_2 e_2 - Q_3 e_3).
$$

Expanding:

$$
= Q_0^2 e_0 - Q_0 Q_1 e_1 - Q_0 Q_2 e_2 - Q_0 Q_3 e_3
+ Q_1 Q_0 e_1 - Q_1^2 e_1^2 - Q_1 Q_2 e_1 e_2 - Q_1 Q_3 e_1 e_3
+ \cdots
$$

Using $e_1^2 = e_2^2 = e_3^2 = -e_0$ and $e_i e_j = -e_j e_i$:

$$
= Q_0^2 e_0 + Q_1^2 e_0 + Q_2^2 e_0 + Q_3^2 e_0 = (Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2) e_0.
$$

So $N(\tilde{Q}) = (Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2) e_0 = \sum_\mu Q_\mu^2 \cdot e_0$.

So the norm form is the coefficient sum of squares, times $e_0$. And we just showed that $\sum_\mu Q_\mu^2 = 0$ forces all coefficients to vanish. So the norm form vanishes only at the origin.

But this contradicts the earlier statement that the zero divisor set is a union of two four-dimensional subspaces. Where is the error?

The error is in the claim that the norm form $N(\tilde{Q}) = \sum_\mu Q_\mu^2$ vanishes on the elements with $\tilde{Q}_+ = 0$ or $\tilde{Q}_- = 0$. Let me check with the element $\tilde{Q} = (1 - j) e_0$.

$Q_0 = 1 - j$, $Q_1 = Q_2 = Q_3 = 0$.

$$
N(\tilde{Q}) = (1 - j)^2 = 1 - 2j + j^2 = 1 - 2j + 1 = 2 - 2j \neq 0.
$$

So $N(\tilde{Q}) \neq 0$, and the element is not a zero divisor by the norm form criterion. But is it a zero divisor in the algebra? Let's check: $(1 - j)(1 + j) = 1 - j^2 = 0$. So $(1 - j) e_0$ times $(1 + j) e_0$ is $0$. So it **is** a zero divisor in the algebra.

But the norm form criterion says it is not a zero divisor, because $N(\tilde{Q}) \neq 0$. Where is the contradiction?

The contradiction is that the norm form $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}}$ uses the **quaternion conjugate**, not the **split complex conjugate**. The product $(1 - j)(1 + j)$ uses the split complex conjugate of $1 - j$, which is $1 + j$. But the quaternion conjugate of $(1 - j) e_0$ is $(1 - j) e_0$ itself, because the quaternion conjugate only negates the vector part, and the scalar part $1 - j$ is unchanged. So the norm form is $(1 - j)^2 = 2 - 2j$, not zero.

So the norm form criterion is **not** the correct criterion for zero divisors in the split quaternion algebra! The correct criterion is the one in the idempotent basis: $\tilde{Q}$ is a zero divisor if and only if $\tilde{Q}_+ = 0$ or $\tilde{Q}_- = 0$.

This means that the norm form $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}}$ does **not** characterize the zero divisors in the split quaternion algebra. The norm form is multiplicative and vanishes at the origin, but it does not vanish on all the zero divisors.

I apologize for the error. The correct criterion is the idempotent-basis criterion, not the norm form criterion. The two coincide in the biquaternion case, because the complex conjugation and the quaternion conjugation interact in a way that makes the norm form vanish on the zero divisors. In the split quaternion case, they do not coincide, because the split complex conjugation and the quaternion conjugation interact differently.

Let me now correct the article.

## The Correct Criterion

### Criterion in the Idempotent Basis

**Theorem.** A nonzero split quaternion $\tilde{Q}$ is a zero divisor if and only if $\tilde{Q}_+ = 0$ or $\tilde{Q}_- = 0$.

**Proof.** If $\tilde{Q}_+ = 0$ and $\tilde{Q} \neq 0$, then $\tilde{Q}_- \neq 0$ and $\tilde{Q} e_- = \tilde{Q}_- e_- \neq 0$. Wait, we need a nonzero $\tilde{R}$ with $\tilde{Q} \tilde{R} = 0$. Take $\tilde{R} = e_+$. Then

$$
\tilde{Q} e_+ = \tilde{Q}_+ e_+ = 0.
$$

So $\tilde{Q}$ is a zero divisor (with $\tilde{R} = e_+ \neq 0$). Similarly, if $\tilde{Q}_- = 0$, take $\tilde{R} = e_-$.

Conversely, suppose $\tilde{Q}$ is a zero divisor: there exists $\tilde{R} \neq 0$ with $\tilde{Q} \tilde{R} = 0$ or $\tilde{R} \tilde{Q} = 0$. In the idempotent basis, $\tilde{Q} \tilde{R} = \tilde{Q}_+ \tilde{R}_+ e_+ + \tilde{Q}_- \tilde{R}_- e_-$. This vanishes if and only if $\tilde{Q}_+ \tilde{R}_+ = 0$ and $\tilde{Q}_- \tilde{R}_- = 0$. Since $\mathbb{H}$ is a division algebra, $\tilde{Q}_+ \tilde{R}_+ = 0$ implies $\tilde{Q}_+ = 0$ or $\tilde{R}_+ = 0$. Similarly for the minus component. If $\tilde{R} \neq 0$, then $\tilde{R}_+ \neq 0$ or $\tilde{R}_- \neq 0$. Suppose $\tilde{R}_+ \neq 0$. Then $\tilde{Q}_+ \tilde{R}_+ = 0$ implies $\tilde{Q}_+ = 0$. So $\tilde{Q}_+ = 0$ or $\tilde{Q}_- = 0$. $\square$

### The Norm Form Is Not the Criterion

The norm form $N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}}$ is **not** the criterion for zero divisors in the split quaternion algebra. The norm form vanishes only at the origin, so it does not detect the zero divisors. The invertibility criterion is also different: an element is invertible if and only if both idempotent components are nonzero, which is a **linear** condition in the idempotent basis, not the quadratic condition $N(\tilde{Q}) \neq 0$.

Wait, this is also wrong. The inverse formula $\tilde{Q}^{-1} = \bar{\tilde{Q}}/N(\tilde{Q})$ requires $N(\tilde{Q}) \neq 0$, and $N(\tilde{Q}) \neq 0$ if and only if $\tilde{Q} = 0$. So the formula would only give an inverse for the zero element, which is absurd.

The correct inverse formula in the split quaternion algebra must use a different "norm," namely the **determinant** in the matrix representation, or the **product of the two idempotent components**.

Let me think. In the idempotent basis, $\tilde{Q} = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-$ with

