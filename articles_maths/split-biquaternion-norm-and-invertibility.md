
# __Split-Biquaternion Norm and Invertibility__

## Introduction

This article studies the split-biquaternion norm of the algebra and the invertibility of its elements. It follows the article on split biquaternion algebra, which defined the algebra, its four conjugations, and its four fixed-point subspaces. The goal here is to define the split-biquaternion norm and the Hermitian form, to establish the criterion for invertibility, and to describe the group of units.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra. The split complex algebra $\mathbb{D}$ is assumed from the article on split complex algebra, together with its idempotents $\tilde\Pi_1 = \tfrac{1}{2}(1 + j)$ and $\tilde\Pi_2 = \tfrac{1}{2}(1 - j)$ and the isomorphism $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$. The split biquaternion algebra $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ is assumed from the preceding article, together with its four conjugations, its four fixed-point subspaces, and its three decompositions.

Throughout, a split biquaternion is written

$$
\tilde{Q} = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z, \qquad Q_\mu = q_\mu + j q'_\mu, \quad q_\mu, q'_\mu \in \mathbb{R}.
$$

The quaternion conjugate is $\tilde{Q}^{\natural} = Q_t e_t - \vec Q$, where $\vec Q = Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z$. The split complex conjugate is $\bar{\tilde{Q}} = \bar{Q_t} e_t + \bar{\vec Q}$, where $Q_{\bar{\mu}} = q_\mu - j q'_\mu$. The Hermitian conjugate is $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$, and the anti-Hermitian conjugate is $\tilde{Q}^\flat = -\tilde{Q}^{*}$.

The idempotents of the split complex algebra are denoted $\tilde\Pi_1 = \tfrac{1}{2}(1 + j)$ and $\tilde\Pi_2 = \tfrac{1}{2}(1 - j)$. The idempotent decomposition of a split biquaternion is

$$
\tilde{Q} = \tilde{Q}_+ \tilde\Pi_1 + \tilde{Q}_- \tilde\Pi_2,
$$

with $\tilde{Q}_\pm = \tilde{Q} \tilde\Pi_{1,2} \in \mathbb{H}$ ordinary quaternions.

## The Split-Biquaternion Norm

### Definition

The **split-biquaternion norm** of a split biquaternion $\tilde{Q}$ is

$$
\langle\tilde{Q}\rangle_{\natural} = \tilde{Q} \tilde{Q}^{\natural} = \sum_{\mu\in\{t,x,y,z\}} Q_\mu^2,
$$

where $\tilde{Q}^{\natural}$ is the quaternion conjugate.

**Basic properties.**

- $\langle\tilde{Q}\rangle_{\natural}$ is a split complex number in general. It is real when $\tilde{Q}$ lies in the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ or in the imaginary translate $j \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, and outside their union it need not be real.
- $\langle\tilde{Q}\rangle_{\natural}$ is **anisotropic**: it vanishes only when $\tilde{Q} = 0$, so the split-biquaternion norm does not by itself detect the zero divisors. Those are described by the idempotent criterion below, and are studied in the article on split biquaternion zero divisors.
- $\langle\tilde{Q}\rangle_{\natural}$ is invariant under quaternion conjugation: $\langle\tilde{Q}^{\natural}\rangle_{\natural} = \langle\tilde{Q}\rangle_{\natural}$.
- $\langle\tilde{Q}\rangle_{\natural}$ is not invariant under split complex conjugation: $\langle\bar{\tilde{Q}}\rangle_{\natural} = \langle\tilde{Q}\rangle_{\natural}^*$.
- $\langle\tilde{Q}\rangle_{\natural}$ is not invariant under Hermitian conjugation: $\langle\tilde{Q}^{*}\rangle_{\natural} = \langle\tilde{Q}\rangle_{\natural}^*$.

### Explicit Form

Writing $Q_\mu = q_\mu + j q'_\mu$ and using $j^2 = +1$,

$$
\langle\tilde{Q}\rangle_{\natural} = \sum_{\mu\in\{t,x,y,z\}} (q_\mu^2 + q'^2_\mu) + 2j \sum_{\mu\in\{t,x,y,z\}} q_\mu q'_\mu.
$$

So the real part of the split-biquaternion norm is the sum of the squares of all eight real components, and the split part is twice the inner product of the real and split parts. This is the **same structure** as in the biquaternion case, with $j$ in place of $i$. The difference is the sign of the square of the extra unit: $j^2 = +1$ versus $i^2 = -1$.

### Multiplicativity

**Theorem.** The split-biquaternion norm is multiplicative:

$$
\langle\tilde{Q}_1 \bullet \tilde{Q}_2\rangle_{\natural} = \langle\tilde{Q}_1\rangle_{\natural} \, \langle\tilde{Q}_2\rangle_{\natural}.
$$

**Proof.** Compute

$$
\langle\tilde{Q}_1 \bullet \tilde{Q}_2\rangle_{\natural} = (\tilde{Q}_1 \tilde{Q}_2)(\tilde{Q}_1 \tilde{Q}_2)^{\natural} = \tilde{Q}_1 \tilde{Q}_2 \tilde{Q}_2^{\natural} \tilde{Q}_1^{\natural} = \tilde{Q}_1 \langle\tilde{Q}_2\rangle_{\natural} \tilde{Q}_1^{\natural}.
$$

Since $\langle\tilde{Q}_2\rangle_{\natural}$ is a split complex number and the split complex unit $j$ commutes with the quaternion units, $\langle\tilde{Q}_2\rangle_{\natural}$ commutes with $\tilde{Q}_1$ and with $\tilde{Q}_1^{\natural}$. So

$$
\tilde{Q}_1 \langle\tilde{Q}_2\rangle_{\natural} \tilde{Q}_1^{\natural} = \langle\tilde{Q}_2\rangle_{\natural} \tilde{Q}_1 \tilde{Q}_1^{\natural} = \langle\tilde{Q}_2\rangle_{\natural} \langle\tilde{Q}_1\rangle_{\natural}.
$$

**Corollary.** If $\langle\tilde{Q}_1\rangle_{\natural}$ and $\langle\tilde{Q}_2\rangle_{\natural}$ are invertible in $\mathbb{D}$, then $\langle\tilde{Q}_1 \bullet \tilde{Q}_2\rangle_{\natural}$ is invertible in $\mathbb{D}$.

**Corollary.** If $\langle\tilde{Q}_1\rangle_{\natural} = 0$ or $\langle\tilde{Q}_2\rangle_{\natural} = 0$, then $\langle\tilde{Q}_1 \bullet \tilde{Q}_2\rangle_{\natural} = 0$. In particular, the product of a zero divisor with any split biquaternion is either zero or a zero divisor.

### The Split-Biquaternion Norm in the Idempotent Basis

In the idempotent basis, the split-biquaternion norm takes a particularly simple form. Writing $\tilde{Q} = \tilde{Q}_+ \tilde\Pi_1 + \tilde{Q}_- \tilde\Pi_2$ with $\tilde{Q}_\pm \in \mathbb{H}$,

$$
\langle\tilde{Q}\rangle_{\natural} = N_{\mathbb{H}}(\tilde{Q}_+) \tilde\Pi_1 + N_{\mathbb{H}}(\tilde{Q}_-) \tilde\Pi_2,
$$

where $N_{\mathbb{H}}(\tilde{Q}_\pm) = \tilde{Q}_\pm \tilde{Q}^{\natural}_\pm$ is the ordinary quaternion norm of $\tilde{Q}_\pm$, which is a non-negative real number.

So the split-biquaternion norm of a split biquaternion is the pair of non-negative real numbers $(N_{\mathbb{H}}(\tilde{Q}_+), N_{\mathbb{H}}(\tilde{Q}_-))$, embedded in the split complex algebra via the idempotent basis. This is the cleanest form of the split-biquaternion norm, and it is the form in which the invertibility criterion is most transparent.

### The Quadratic Form and Its Polarisation

The split-biquaternion norm is the quadratic form of the bilinear pairing obtained by polarisation. For two split biquaternions $\tilde Q_1 = \sum_\mu Q_{1\mu} e_\mu$ and $\tilde Q_2 = \sum_\mu Q_{2\mu} e_\mu$, set

$$
\langle\tilde Q_1,\tilde Q_2\rangle = \sum_{\mu\in\{t,x,y,z\}} Q_{1\mu} Q_{2\mu},
$$

a split complex number, so that $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle$. The pairing is symmetric, split-complex-bilinear, and its polarisation is the quadratic form

$$
\langle\tilde Q_1 + \tilde Q_2\rangle_{\natural} - \langle\tilde Q_1\rangle_{\natural} - \langle\tilde Q_2\rangle_{\natural} = 2 \langle\tilde Q_1,\tilde Q_2\rangle.
$$

The **quadratic space** so defined is the split complex quadratic space of dimension $4$ whose form is anisotropic: $\langle\tilde{Q},\tilde{Q}\rangle = 0$ forces $\tilde{Q} = 0$, since the real part of $\langle\cdot,\cdot\rangle_{\natural}$ is a sum of squares. This is the same construction as in the biquaternion case, with the split complex algebra in place of the complex field and $j^2 = +1$ in place of $i^2 = -1$.

**Proposition.** The polarisation $\langle\cdot,\cdot\rangle$ is $\mathbb{D}$-bilinear, symmetric and non-degenerate, and the unit basis is orthonormal:

$$
\langle\tilde Q_1,\tilde Q_2\rangle = \tfrac{1}{2}\left(\tilde Q_1 \tilde Q_2^{\natural} + \tilde Q_2 \tilde Q_1^{\natural}\right), \qquad \langle e_\mu, e_\nu\rangle = \delta_{\mu\nu}.
$$

**Proof.** Bilinearity is that of the polarisation of a quadratic form, symmetry is its defining property, and $\langle e_\mu, e_\nu\rangle = \delta_{\mu\nu}$ is immediate from the coordinate formula. Non-degeneracy follows because $\langle e_\mu, e_\mu\rangle = e_t$ is a unit of $\mathbb{D}$.

**Remark.** Unlike the biquaternion case, where the norm is the determinant of a $2\times 2$ complex matrix, here $\langle\cdot\rangle_{\natural}$ is not a determinant of a matrix over a field, because the algebra is a product of two division algebras; the polarisation $\langle\cdot,\cdot\rangle$ is the honest $\mathbb{D}$-valued bilinear form and not a trace form.

### The Real Forms and Their Signatures

Writing $Q_\mu = q_\mu + jq'_\mu$ with $q_\mu, q'_\mu \in \mathbb{R}$,

$$
\langle\tilde{Q}\rangle_{\natural} = R(\tilde{Q}) + j\,I(\tilde{Q}), \qquad R(\tilde{Q}) = \sum_\mu (q_\mu^2 + q'^2_\mu), \quad I(\tilde{Q}) = 2\sum_\mu q_\mu q'_\mu.
$$

**Proposition.** The form $R$ is the Euclidean form, positive definite of signature $(8,0)$; the form $I$ is the polarisation of the pairing of each real coordinate with its split partner, non-degenerate of signature $(4,4)$. The Hermitian scalar form $g(\tilde Q_1, \tilde Q_2) = \mathrm{Sc}(\tilde Q_1 \tilde Q_2^{*})$ is also non-degenerate of signature $(4,4)$.

**Proof.** $R$ is a sum of squares of the eight real coordinates. $I$ has the matrix with two $4\times 4$ off-diagonal blocks $I_4$, of signature $(4,4)$. The Hermitian form is non-degenerate of signature $(4,4)$ as established in *Split-Biquaternion Rotations and the Lorentz Group*.

The signatures of $\langle\cdot,\cdot\rangle_{\natural}$ restricted to the four distinguished subspaces are:

| Subspace | Condition | $\langle\cdot\rangle_{\natural}$ restricted | Signature |
|---|---|---|---|
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | $Q_\mu = 0$, $\mu \geq 1$ | $q_t^2 + q'^2_0 + 2jq_0q'_t$ | real part $(2,0)$ |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | $q'_\mu = 0$ | $\sum_\mu q_\mu^2$ | $(4,0)$ |
| $\mathbb{M}_+$ | $q'_t = 0$, $q_k = 0$ | $q_t^2 - \sum_k q'^2_k$ | $(1,3)$ |
| $\mathbb{M}_-$ | $q_t = 0$, $q'_k = 0$ | $-q'^2_0 + \sum_k q_k^2$ | $(3,1)$ |

On the quaternion subspace the split-biquaternion norm is real and positive definite; on the two Hermitian sectors it is real and Lorentzian; on the centre it is split complex, the split complex norm of $\mathbb{D}$.

## The Hermitian Form

### Definition

The **Hermitian form** of a split biquaternion $\tilde{Q}$ is

$$
\tilde{Q} \tilde{Q}^{*}, \qquad \text{whose scalar part is } \sum_{\mu\in\{t,x,y,z\}} Q_\mu Q_{\bar{\mu}} = \sum_{\mu\in\{t,x,y,z\}} (q_\mu^2 - q'^2_\mu),
$$

where $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$ is the Hermitian conjugate and $Q_{\bar{\mu}} = q_\mu - j q'_\mu$ is the split complex conjugate.

**Basic properties.**

- $\tilde{Q} \tilde{Q}^{*}$ need not be real: only its **scalar part** is, and that scalar part is the difference between the sum of the squares of the real parts and the sum of the squares of the split parts.
- The scalar part is **not positive-definite**: it can be positive, negative, or zero. Its signature is $(4, 4)$ on the eight-dimensional real space $\mathbb{H}_{\mathbb{D}}$.
- The product $\tilde{Q} \tilde{Q}^{*}$ vanishes exactly when one of the idempotent components vanishes, that is on the union of two four-dimensional subspaces; the scalar part vanishes on the quadric hypersurface $\sum_\mu q_\mu^2 = \sum_\mu q'^2_\mu$, of dimension $7$.
- It is **not multiplicative**: $\tilde{Q} \tilde{Q}^{*}$ does not satisfy a product formula.

### The Signature

The scalar part of the Hermitian form is a real quadratic form of signature $(4, 4)$:

- The positive directions are the four real coefficients $q_t, q_x, q_y, q_z$.
- The negative directions are the four split coefficients $q'_t, q'_x, q'_y, q'_z$.

So the scalar part of the Hermitian form is the difference of two positive-definite forms, each of rank 4.

### The Zero Set

The scalar part of the Hermitian form vanishes when

$$
\sum_{\mu\in\{t,x,y,z\}} q_\mu^2 = \sum_{\mu\in\{t,x,y,z\}} q'^2_\mu.
$$

This is a quadric hypersurface of dimension $7$ in $\mathbb{H}_{\mathbb{D}} \cong \mathbb{R}^8$, the analogue of the null cone of a Lorentzian four-space, with signature $(4, 4)$ instead of $(1, 3)$.

### The Inner Product

The Hermitian form is polarised by the **inner product**

$$
\langle \tilde Q_1, \tilde Q_2 \rangle = \sum_{\mu\in\{t,x,y,z\}} Q_{1\bar{\mu}} Q_{2\mu},
$$

which is a split complex number in general:

$$
\langle \tilde Q_1, \tilde Q_2 \rangle = \sum_{\mu\in\{t,x,y,z\}} (q_{1\mu} q_{2\mu} - q'_{1\mu} q'_{2\mu}) + j \sum_{\mu\in\{t,x,y,z\}} (q_{1\mu} q'_{2\mu} - q'_{1\mu} q_{2\mu}).
$$

Its real part is the real form of signature $(4, 4)$ above, and its split part is the cross-term. The pairing is linear in the second argument and split-antilinear in the first, and it is Hermitian in the sense that $\langle \tilde Q_1, \tilde Q_2 \rangle^* = \langle \tilde Q_2, \tilde Q_1 \rangle$.

### Relation Between the Three Forms

The three quadratic objects are related as follows.

- **Norm:** $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q} \tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$, split complex-valued, anisotropic, multiplicative, with polarisation $\langle\cdot,\cdot\rangle$.
- **Hermitian form:** $\tilde{Q} \tilde{Q}^{*}$, whose scalar part is $\sum_\mu (q_\mu^2 - q'^2_\mu)$, real, indefinite of signature $(4, 4)$, vanishing on a quadric hypersurface of dimension $7$; the full product is not multiplicative.
- **Inner product:** $\langle \tilde Q_1, \tilde Q_2 \rangle = \sum_\mu Q_{1\bar{\mu}} Q_{2\mu}$, split complex-valued, Hermitian, linear in the second argument.

The three are distinct, and each is useful in a different context. The split-biquaternion norm controls invertibility through the reduced norm below. The zero divisors are not a condition on the split-biquaternion norm; they are the vanishing of an idempotent component. The Hermitian form is indefinite and does not control the topological structure; the Euclidean norm, defined separately, does.

## The Euclidean Norm

### Definition

The **Euclidean norm** of a split biquaternion $\tilde{Q}$ is

$$
\|\tilde{Q}\|_E = \sqrt{\sum_{\mu\in\{t,x,y,z\}} (q_\mu^2 + q'^2_\mu)}.
$$

It is a genuine norm on the real vector space $\mathbb{H}_{\mathbb{D}} \cong \mathbb{R}^8$: positive-definite, subadditive, and homogeneous of degree one.

### Relation to the Split-Biquaternion Norm and the Hermitian Form

The Euclidean norm is not the square root of the Hermitian form, because the Hermitian form is indefinite. It is also not the modulus of the split-biquaternion norm, because the split-biquaternion norm is split complex and its modulus is

$$
|\langle\tilde{Q}\rangle_{\natural}| = \sqrt{\left(\sum_\mu (q_\mu^2 + q'^2_\mu)\right)^2 - 4\left(\sum_\mu q_\mu q'_\mu\right)^2},
$$

which is not the Euclidean norm squared.

The Euclidean norm is defined separately, and it is the ordinary Euclidean norm on the underlying real vector space. It is the split-biquaternion norm that defines the topology of $\mathbb{H}_{\mathbb{D}}$, the convergence of sequences, and the completeness of the algebra as a metric space.

### Multiplicativity

The Euclidean norm is **not** multiplicative with respect to the split biquaternion product. This is the same situation as in the biquaternion case, where the Euclidean norm is not multiplicative because the Hermitian form is not multiplicative.

The split-biquaternion norm, which is multiplicative, is split complex-valued and anisotropic: it is the idempotent components, not the value of the split-biquaternion norm, that detect the zero divisors. The Euclidean norm, which is positive-definite, is not multiplicative, and it does not detect the zero divisors.

## Invertibility

### Definition

A split biquaternion $\tilde Q_1$ is **invertible** if there exists a split biquaternion $\tilde Q_2$ such that

$$
\tilde Q_1 \bullet \tilde Q_2 = \tilde Q_2 \bullet \tilde Q_1 = e_t.
$$

The split biquaternion $\tilde Q_2$, if it exists, is the **inverse** of $\tilde Q_1$ and is denoted $\tilde Q_1^{-1}$.

### Left and Right Inverses

In a general non-commutative algebra, the notions of left inverse, right inverse, and two-sided inverse are distinct. In the split biquaternion algebra, however, they coincide, for the same reason as in the biquaternion algebra: the algebra is finite-dimensional over $\mathbb{R}$, and in a finite-dimensional algebra over a field, a right inverse is also a left inverse.

### Criterion for Invertibility

**Theorem.** A split biquaternion $\tilde Q_1$ is invertible if and only if its split-biquaternion norm is invertible in $\mathbb{D}$:

$$
\langle\tilde Q_1\rangle_{\natural} \in \mathbb{D}^\times.
$$

**Proof.** Suppose $\langle\tilde Q_1\rangle_{\natural}$ is invertible in $\mathbb{D}$. Define

$$
\tilde Q_2 = \tilde Q_1^{\natural} \, \langle\tilde Q_1\rangle_{\natural}^{-1}.
$$

This is legitimate because $\langle\tilde Q_1\rangle_{\natural}$ is a unit of $\mathbb{D}$: mere non-vanishing would not suffice, since $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$ has zero divisors. Then

$$
\tilde Q_1 \bullet \tilde Q_2 = \langle\tilde Q_1\rangle_{\natural} \langle\tilde Q_1\rangle_{\natural}^{-1} = e_t,
$$

so $\tilde Q_2$ is a right inverse, hence also a left inverse.

Conversely, suppose $\tilde Q_1$ is invertible. Applying the split-biquaternion norm to $\tilde Q_1 \bullet \tilde Q_1^{-1} = e_t$ and using multiplicativity gives

$$
\langle\tilde Q_1\rangle_{\natural} \langle\tilde Q_1^{-1}\rangle_{\natural} = \langle e_t\rangle_{\natural} = 1,
$$

so $\langle\tilde Q_1\rangle_{\natural}$ is invertible in $\mathbb{D}$, with inverse $\langle\tilde Q_1^{-1}\rangle_{\natural}$.

**Remark.** The hypothesis is not simply $\tilde{Q} \neq 0$, nor $\langle\tilde{Q}\rangle_{\natural} \neq 0$, which is the same thing by anisotropy. For $\tilde{Q} = \tilde\Pi_1$ one has $\langle\tilde{Q}\rangle_{\natural} = \tilde\Pi_1$, a nonzero zero divisor of $\mathbb{D}$, and $\tilde\Pi_1$ is a zero divisor of $\mathbb{H}_{\mathbb{D}}$, since $\tilde\Pi_1 \tilde\Pi_2 = 0$.

### The Inverse Formula

When $\langle\tilde{Q}\rangle_{\natural}$ is invertible in $\mathbb{D}$, equivalently when $\tilde{Q}$ is invertible, the inverse is

$$
\tilde{Q}^{-1} = \tilde{Q}^{\natural} \, \langle\tilde{Q}\rangle_{\natural}^{-1}.
$$

This is the split biquaternion analogue of the formula $\tilde q^{-1} = \tilde q^{\natural}/|\tilde q|^2$ for quaternions.

### The Criterion in the Idempotent Basis

The invertibility criterion takes a particularly simple form in the idempotent basis. Writing $\tilde{Q} = \tilde{Q}_+ \tilde\Pi_1 + \tilde{Q}_- \tilde\Pi_2$ with $\tilde{Q}_\pm \in \mathbb{H}$,

$$
\langle\tilde{Q}\rangle_{\natural} = N_{\mathbb{H}}(\tilde{Q}_+) \tilde\Pi_1 + N_{\mathbb{H}}(\tilde{Q}_-) \tilde\Pi_2.
$$

Since $N_{\mathbb{H}}(\tilde{Q}_\pm)$ are non-negative real numbers, $\langle\tilde{Q}\rangle_{\natural}$ is a unit of $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$ if and only if both of its components are nonzero:

$$
N_{\mathbb{H}}(\tilde{Q}_+) \neq 0 \quad \text{and} \quad N_{\mathbb{H}}(\tilde{Q}_-) \neq 0.
$$

Mere non-vanishing of $\langle\tilde{Q}\rangle_{\natural}$ would require only one component to be nonzero, and that is not sufficient, as the example $\tilde{Q} = \tilde\Pi_1$ above shows. Since $\mathbb{H}$ is a division algebra, $N_{\mathbb{H}}(\tilde{Q}_\pm) \neq 0$ if and only if $\tilde{Q}_\pm \neq 0$. So the invertibility criterion is

$$
\tilde{Q} \text{ is invertible} \iff \tilde{Q}_+ \neq 0 \text{ and } \tilde{Q}_- \neq 0.
$$

This is the cleanest form of the invertibility criterion. It is a **linear** condition in the idempotent basis: the element is invertible if and only if neither of its two idempotent components vanishes.

**Comparison with the biquaternion case.** In the biquaternion algebra, the invertibility criterion $\langle\tilde{Q}\rangle_{\natural} \neq 0$ is a **quadratic** condition, and the zero divisor set is a complex cone of complex dimension 3 (real dimension 6). In the split biquaternion algebra, the invertibility criterion is a linear condition in the idempotent basis, and the zero divisor set is a union of two four-dimensional linear subspaces. The difference is a consequence of the fact that $\mathbb{H}_{\mathbb{D}}$ is semisimple while $\mathbb{B}$ is simple.

### The Reduced Norm

The split-biquaternion norm alone does not give an inverse. The formula

$$
\tilde{Q}^{-1} = \tilde{Q}^{\natural} \, \langle\tilde{Q}\rangle_{\natural}^{-1}
$$

requires $\langle\tilde{Q}\rangle_{\natural}$ to be invertible in $\mathbb{D}$, not merely nonzero: since $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$ has zero divisors, when $\tilde{Q}$ is a zero divisor the value $\langle\tilde{Q}\rangle_{\natural}$ is a nonzero zero divisor of $\mathbb{D}$ and $\langle\tilde{Q}\rangle_{\natural}^{-1}$ does not exist.

In the idempotent basis the inverse of a unit of $\mathbb{D}$ is computed componentwise. Writing $\langle\tilde{Q}\rangle_{\natural} = N_+ \tilde\Pi_1 + N_- \tilde\Pi_2$ with $N_\pm = N_{\mathbb{H}}(\tilde{Q}_\pm) \in \mathbb{R}$,

$$
\langle\tilde{Q}\rangle_{\natural}^{-1} = \frac{\tilde\Pi_1}{N_+} + \frac{\tilde\Pi_2}{N_-} = \frac{\langle\tilde{Q}\rangle_{\natural}^*}{\Delta(\tilde{Q})},
$$

where $\langle\tilde{Q}\rangle_{\natural}^* = N_- \tilde\Pi_1 + N_+ \tilde\Pi_2$ is the split complex conjugate of $\langle\tilde{Q}\rangle_{\natural}$. Substituting into $\tilde{Q}^{-1} = \tilde{Q}^{\natural} \langle\tilde{Q}\rangle_{\natural}^{-1}$ expresses the inverse through the **reduced norm**

$$
\Delta(\tilde{Q}) = N_{\mathbb{H}}(\tilde{Q}_+) N_{\mathbb{H}}(\tilde{Q}_-) = \langle\tilde{Q}\rangle_{\natural} \langle\tilde{Q}\rangle_{\natural}^* \in \mathbb{R},
$$

a real quartic, the product of the two ordinary quaternion norms:

$$
\tilde{Q}^{-1} = \frac{\tilde{Q}^{\natural} \, \langle\tilde{Q}\rangle_{\natural}^*}{\Delta(\tilde{Q})}, \qquad \Delta(\tilde{Q}) \neq 0.
$$

The identity is forced by multiplicativity of the split-biquaternion norm: $\tilde{Q} \tilde{Q}^{\natural} \langle\tilde{Q}\rangle_{\natural}^* = \langle\tilde{Q}\rangle_{\natural} \langle\tilde{Q}\rangle_{\natural}^* = \Delta(\tilde{Q}) e_t$, so the right-hand side is a two-sided inverse of $\tilde{Q}$ exactly when $\Delta(\tilde{Q}) \neq 0$.

The reduced norm gives the invertibility criterion in its sharpest form:

$$
\tilde{Q} \text{ is invertible} \iff \Delta(\tilde{Q}) \neq 0 \iff \tilde{Q}_+ \neq 0 \text{ and } \tilde{Q}_- \neq 0.
$$

The difference from the biquaternion algebra is the field. There $\mathbb{C}$ is a field, so $\langle\tilde{Q}\rangle_{\natural} \neq 0$ is already the criterion, and the zero divisors are exactly the nonzero elements with $\langle\tilde{Q}\rangle_{\natural} = 0$. Here the split-biquaternion norm takes values in $\mathbb{D}$, which is not a field, so the criterion is the invertibility of $\langle\tilde{Q}\rangle_{\natural}$ in $\mathbb{D}$, equivalently $\Delta(\tilde{Q}) \neq 0$.

### A Worked Element

For the element $\tilde{Q}$ with $Q_t = 1 + j$, $Q_x = 2$, $Q_y = 1 - j$, $Q_z = 0$,

$$
\langle\tilde{Q}\rangle_{\natural} = (1 + j)^2 + 2^2 + (1 - j)^2 + 0^2 = (2 + 2j) + 4 + (2 - 2j) = 8.
$$

Since $8 \in \mathbb{D}^\times$, the element is a unit, and

$$
\tilde{Q} \tilde{Q}^{\natural} = 8 e_t, \qquad \tilde{Q}^{-1} = \tfrac{1}{8} \tilde{Q}^{\natural} = \tfrac{1}{8}\big(1 - 2 \vec e_x - \vec e_y\big) + \tfrac{j}{8}\big(1 + \vec e_y\big).
$$

The criterion is not the naive one $\langle\tilde{Q}\rangle_{\natural} \neq 0$. For $\tilde\Pi_1$ one has $\langle\tilde\Pi_1\rangle_{\natural} = \tilde\Pi_1 \neq 0$, yet $\tilde\Pi_1$ is a zero divisor, because $\tilde\Pi_1$ is a nonzero non-unit of $\mathbb{D}$ and so does not lie in $\mathbb{D}^\times$. In the idempotent basis $N_{\mathbb{H}}(\tilde{Q}_+) = N_{\mathbb{H}}(\tilde{Q}_-) = 8$, so $\langle\tilde{Q}\rangle_{\natural} = 8\tilde\Pi_1 + 8\tilde\Pi_2 = 8$, matching the direct computation.

### Corollaries

**Corollary.** The inverse of an invertible element is invertible, and $(\tilde{Q}^{-1})^{-1} = \tilde{Q}$.

**Corollary.** If $\tilde{Q}$ is invertible, then $\tilde{Q}^{\natural}$, $\bar{\tilde{Q}}$, $\tilde{Q}^{*}$, and $\tilde{Q}^\flat$ are invertible, and their inverses are the corresponding conjugates of $\tilde{Q}^{-1}$.

**Corollary.** The product of two invertible elements is invertible, with $(\tilde Q_1 \tilde Q_2)^{-1} = \tilde Q_2^{-1} \tilde Q_1^{-1}$.

## The Group of Units

### Definition

The **group of units** of $\mathbb{H}_{\mathbb{D}}$ is the set of invertible elements:

$$
\mathbb{H}_{\mathbb{D}}^\times = \{\tilde{Q} \in \mathbb{H}_{\mathbb{D}} : \langle\tilde{Q}\rangle_{\natural} \in \mathbb{D}^\times\}
= \{\tilde{Q} \in \mathbb{H}_{\mathbb{D}} : N_{\mathbb{H}}(\tilde{Q}_+) \neq 0 \text{ and } N_{\mathbb{H}}(\tilde{Q}_-) \neq 0\}.
$$

It is a group under multiplication, with identity $e_t$.

### Structure

**Theorem.** The group of units is isomorphic to the direct product of two copies of the quaternion unit group:

$$
\mathbb{H}_{\mathbb{D}}^\times \cong \mathbb{H}^\times \times \mathbb{H}^\times,
$$

where $\mathbb{H}^\times = \mathbb{H} \setminus \{0\}$ is the group of nonzero quaternions.

**Proof.** In the idempotent basis, an element is invertible if and only if both idempotent components are nonzero. The multiplication is componentwise, so the group of units is the direct product of the groups of units of the two components. Each component is a copy of $\mathbb{H}$, and its group of units is $\mathbb{H}^\times$.

### Basic Properties

**Openness.** The group of units is an open subset of $\mathbb{H}_{\mathbb{D}}$ in the Euclidean topology. Indeed, the invertibility condition is that both idempotent components are nonzero, which is an open condition.

**Non-compactness.** The group of units is not compact, because it contains the real line $\{a e_t : a \in \mathbb{R}, a \neq 0\}$, which is unbounded.

**Connected components.** The group of units is connected. Indeed, in the idempotent basis, an invertible element is a pair $(\tilde{Q}_+, \tilde{Q}_-)$ with both components nonzero, and $\mathbb{H} \setminus \{0\} \cong S^3 \times (0, \infty)$ is connected; the group of units is therefore homeomorphic to $(\mathbb{H} \setminus \{0\}) \times (\mathbb{H} \setminus \{0\})$, with a single component. (The group $\mathbb{D}^\times$ of split complex scalars, by contrast, does have four components.)

**Centre.** The centre of $\mathbb{H}_{\mathbb{D}}^\times$ is the group of invertible split complex scalars, which is the group of units of $\mathbb{D}$:

$$
Z(\mathbb{H}_{\mathbb{D}}^\times) = \mathbb{D}^\times = \{Q_t \in \mathbb{D} : Q_t \neq 0\}.
$$

The group of units of $\mathbb{D}$ has four connected components, corresponding to the four sign combinations of the real and split parts.

## The Three-Way Classification

Combining the criterion for invertibility with the definition of the zero element, the elements of $\mathbb{H}_{\mathbb{D}}$ are partitioned into three classes:

| Condition on $\langle\tilde{Q}\rangle_{\natural}$ | Condition on $\tilde{Q}$ | Conclusion |
|---|---|---|
| $\langle\tilde{Q}\rangle_{\natural} \in \mathbb{D}^\times$ | (automatically $\tilde{Q} \neq 0$) | $\tilde{Q}$ is invertible |
| $\langle\tilde{Q}\rangle_{\natural} = 0$ | $\tilde{Q} = 0$ | $\tilde{Q}$ is the zero element |
| $\langle\tilde{Q}\rangle_{\natural}$ a nonzero zero divisor of $\mathbb{D}$ | $\tilde{Q} \neq 0$ | $\tilde{Q}$ is a zero divisor |

The zero divisors are the subject of the article on split biquaternion zero divisors.

### The Algebra Is Not a Division Algebra

By definition, a **division algebra** is an algebra in which every nonzero element is invertible. Equivalently, an algebra is a division algebra if and only if it contains no zero divisors.

The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$ contains zero divisors, so it is **not** a division algebra. This is in contrast to the quaternion algebra $\mathbb{H}$, which is a division algebra, and to the biquaternion algebra $\mathbb{B}$, which is also not a division algebra.

The Frobenius theorem states that the only finite-dimensional associative real division algebras are $\mathbb{R}$, $\mathbb{C}$, and $\mathbb{H}$. The split biquaternion algebra is a fourth finite-dimensional associative real algebra, but it is not a division algebra, because it contains zero divisors.

## Distribution of the Invertible Elements

We now examine how the invertible elements are distributed among the four fixed-point subspaces of $\mathbb{H}_{\mathbb{D}}$ defined in the preceding article. The criterion is the same in all cases: an element is invertible if and only if its split-biquaternion norm is invertible in $\mathbb{D}$, equivalently if and only if both of its idempotent components are nonzero.

### The Split Complex Subspace $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$

An element of $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ has the form

$$
\tilde{Q} = Q_t e_t, \qquad Q_t \in \mathbb{D}.
$$

The split-biquaternion norm is

$$
\langle\tilde{Q}\rangle_{\natural} = Q_t^2.
$$

Since $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$, this vanishes only when $Q_t = 0$; the element $Q_t e_t$ is a zero divisor if and only if $Q_t$ is a zero divisor in $\mathbb{D}$, that is a nonzero multiple of $1 \pm j$, which need not be detected by $\langle\cdot\rangle_{\natural}$ vanishing. So the split complex subspace contains the zero divisors $Q_t e_t$ with $Q_t = t(1 \pm j)$ for $t \neq 0$, inherited from the split complex algebra.

The invertible elements of $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ are those with $Q_t$ not a multiple of $1 \pm j$, i.e., with $Q_t$ invertible in $\mathbb{D}$.

### The Quaternion Subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$

An element of $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ has the form

$$
\tilde{Q} = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z, \qquad q_\mu \in \mathbb{R}.
$$

The split-biquaternion norm is

$$
\langle\tilde{Q}\rangle_{\natural} = q_t^2 + q_x^2 + q_y^2 + q_z^2.
$$

This is a sum of squares of real numbers, and it vanishes if and only if all $q_\mu = 0$, i.e., if and only if $\tilde{Q} = 0$. So the quaternion subspace contains no zero divisors, and every nonzero element is invertible. This reflects the Frobenius theorem: $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ is a copy of the division algebra $\mathbb{H}$.

### The Hermitian Subspace $\mathbb{M}_+$

An element of $\mathbb{M}_+$ has the form

$$
\tilde{Q} = q_t e_t + j q'_x \vec e_x + j q'_y \vec e_y + j q'_z \vec e_z, \qquad q_t, q'_x, q'_y, q'_z \in \mathbb{R}.
$$

With $Q_t = q_t$ (real) and $Q_k = j q'_k$ (purely split-imaginary), the split-biquaternion norm is

$$
\langle\tilde{Q}\rangle_{\natural} = Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2 = q_t^2 + (j q'_x)^2 + (j q'_y)^2 + (j q'_z)^2 = q_t^2 + (q'_x)^2 + (q'_y)^2 + (q'_z)^2.
$$

Since $j^2 = +1$, the split-imaginary vector components contribute $(j q'_k)^2 = j^2 (q'_k)^2 = +(q'_k)^2$.

So the split-biquaternion norm on $\mathbb{M}_+$ is

$$
\langle\tilde{Q}\rangle_{\natural} = q_t^2 + (q'_x)^2 + (q'_y)^2 + (q'_z)^2,
$$

which is a **real**, positive-definite number, of signature $(4, 0)$. It vanishes only at the origin, so $\mathbb{M}_+$ contains no zero divisors and every nonzero element of $\mathbb{M}_+$ is invertible.

### The Anti-Hermitian Subspace $\mathbb{M}_-$

An element of $\mathbb{M}_-$ has the form

$$
\tilde{Q} = j r_0 e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z, \qquad r_0, q_x, q_y, q_z \in \mathbb{R}.
$$

The split-biquaternion norm is

$$
\langle\tilde{Q}\rangle_{\natural} = (j r_0)^2 + q_x^2 + q_y^2 + q_z^2 = r_0^2 + q_x^2 + q_y^2 + q_z^2,
$$

which is a **real**, positive-definite number, of signature $(4, 0)$. It vanishes only at the origin, so $\mathbb{M}_-$ contains no zero divisors and every nonzero element of $\mathbb{M}_-$ is invertible.

### Summary of the Distribution

Of the four fixed-point subspaces:

- $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ contains zero divisors (inherited from $\mathbb{D}$), and the invertible elements are those whose scalar part is invertible in $\mathbb{D}$.
- $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ is a division algebra: every nonzero element is invertible.
- $\mathbb{M}_+$ is positive-definite of signature $(4, 0)$: it contains no zero divisors and every nonzero element of it is invertible.
- $\mathbb{M}_-$ is positive-definite of signature $(4, 0)$: it contains no zero divisors and every nonzero element of it is invertible.

## Summary

The split-biquaternion norm $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q} \tilde{Q}^{\natural}$ is a split complex-valued multiplicative quadratic form on the split biquaternion algebra. It is anisotropic: it vanishes only at the origin, so it does not detect the zero divisors. In the idempotent basis, it is the pair of ordinary quaternion norms of the two idempotent components, which is the cleanest form of the split-biquaternion norm. Its polarisation is the symmetric split-complex-bilinear pairing $\langle\tilde Q_1,\tilde Q_2\rangle = \sum_\mu Q_{1\mu} Q_{2\mu}$.

The scalar part of the Hermitian form $\tilde{Q} \tilde{Q}^{*}$ is a real indefinite quadratic form of signature $(4, 4)$; the product itself need not be real. Its polarisation is the Hermitian inner product $\langle \tilde Q_1, \tilde Q_2 \rangle = \sum_\mu Q_{1\bar{\mu}} Q_{2\mu}$. Neither defines a Euclidean norm. The Euclidean norm is defined separately and is positive-definite but not multiplicative.

The invertibility criterion is: $\tilde{Q}$ is invertible if and only if $\langle\tilde{Q}\rangle_{\natural}$ is invertible in $\mathbb{D}$, equivalently if and only if the reduced norm $\Delta(\tilde{Q}) = N_{\mathbb{H}}(\tilde{Q}_+) N_{\mathbb{H}}(\tilde{Q}_-)$ is nonzero, equivalently if and only if both idempotent components are nonzero:

$$
\tilde{Q} \text{ is invertible} \iff \tilde{Q}_+ \neq 0 \text{ and } \tilde{Q}_- \neq 0.
$$

This is a linear condition in the idempotent basis, in contrast to the quadratic condition in the biquaternion case.

The inverse is $\tilde{Q}^{-1} = \tilde{Q}^{\natural}/\langle\tilde{Q}\rangle_{\natural}$. The group of units $\mathbb{H}_{\mathbb{D}}^\times$ is isomorphic to $\mathbb{H}^\times \times \mathbb{H}^\times$, and it is connected.

The algebra $\mathbb{H}_{\mathbb{D}}$ is partitioned into three classes: the zero element, the invertible elements, and the zero divisors. Of the four fixed-point subspaces, the quaternion subspace is a division algebra, the split complex subspace contains zero divisors inherited from $\mathbb{D}$, and the Hermitian and anti-Hermitian subspaces are positive-definite and contain no zero divisors.

The zero divisors themselves are studied in the article on split biquaternion zero divisors, and the roots of $-1$ are studied in the article on split biquaternion roots of minus one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}}$ | Split biquaternion algebra |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | General split biquaternion |
| $Q_\mu = q_\mu + j q'_\mu$ | Split complex coefficient |
| $\tilde{Q}^{\natural}$ | Quaternion conjugate |
| $\bar{\tilde{Q}}$ | Split complex conjugate |
| $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$ | Hermitian conjugate |
| $\tilde{Q}^\flat = -\tilde{Q}^{*}$ | Anti-Hermitian conjugate |
| $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q} \tilde{Q}^{\natural}$ | Split-Biquaternion norm |
| $\langle\tilde Q_1,\tilde Q_2\rangle = \sum_\mu Q_{1\mu} Q_{2\mu}$ | Polarisation of the split-biquaternion norm |
| $\langle \tilde Q_1, \tilde Q_2 \rangle = \sum_\mu Q_{1\bar{\mu}} Q_{2\mu}$ | Hermitian inner product |
| $\tilde{Q} \tilde{Q}^{*} = \sum_\mu (q_\mu^2 - q'^2_\mu)$ | Hermitian form (signature $(4,4)$) |
| $\Delta(\tilde{Q}) = N_{\mathbb{H}}(\tilde{Q}_+) N_{\mathbb{H}}(\tilde{Q}_-) = \langle\tilde{Q}\rangle_{\natural} \langle\tilde{Q}\rangle_{\natural}^*$ | Reduced norm (determinant) |
| $\|\tilde{Q}\|_E = \sqrt{\sum_\mu (q_\mu^2 + q'^2_\mu)}$ | Euclidean norm |
| $\tilde{Q}^{-1} = \tilde{Q}^{\natural}/\langle\tilde{Q}\rangle_{\natural}$ | Inverse |
| $\mathbb{H}_{\mathbb{D}}^\times$ | Group of units |
| $\tilde\Pi_1 = \tfrac{1}{2}(1 + j)$ | Positive idempotent |
| $\tilde\Pi_2 = \tfrac{1}{2}(1 - j)$ | Negative idempotent |
| $\tilde{Q}_\pm = \tilde{Q} \tilde\Pi_{1,2}$ | Idempotent components |
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | Split complex subspace |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | Quaternion subspace |
| $\mathbb{M}_+$ | Hermitian subspace |
| $\mathbb{M}_-$ | Anti-Hermitian subspace |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation of quaternions and their complexification.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the algebraic structure and the split-biquaternion norm.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis.

