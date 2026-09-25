# __Split-Biquaternion Analysis on Subspaces__

## Introduction

The article on split biquaternion analysis defined limits, continuity, and the differential operators on a general four-dimensional real subspace $V \subset \mathbb{H}_{\mathbb{D}}$. The article on split biquaternion integration defined the integral and the Cauchy integral formula on the same general subspace. This article specializes the general theory to the four natural subspaces of the split biquaternion algebra: the **split complex subspace** $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, the **quaternion subspace** $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, the **Hermitian subspace** $\mathbb{M}_+$, and the **anti-Hermitian subspace** $\mathbb{M}_-$.

The four subspaces are the natural domains for the analysis because they are the four fixed-point sets of the four conjugations, and because they have different algebraic and geometric properties:

- On the split complex subspace $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, the algebra is commutative, two-dimensional, and contains zero divisors.
- On the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, the algebra is the quaternion algebra, a division algebra, and the norm form is positive-definite.
- On the Hermitian subspace $\mathbb{M}_+$, the Hermitian form is indefinite of signature $(1, 3)$, the norm form is positive definite, and there are no zero divisors.
- On the anti-Hermitian subspace $\mathbb{M}_-$, the Hermitian form is indefinite of signature $(3, 1)$, the norm form is positive definite, and there are no zero divisors.

The four subspaces are therefore complementary, and each of them is the natural domain for a different aspect of the theory.

The treatment is purely mathematical. The independent variables are real variables, and they are independent of any physical interpretation. The split complex structure of the coefficients and the non-commutative structure of the quaternion units are the only algebraic ingredients.

Every claim is either proved or stated as a definition. Where a computation is long, all steps are shown.

The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$, its conjugations, its four fixed-point subspaces, the Euclidean norm, the split-biquaternion gradient $\tilde{\nabla}$, the quaternion conjugate $\bar{\tilde{\nabla}}$, the d'Alembertian $\Box$, the square $\tilde{\nabla}^2$, the convective derivative $\tilde{D}$, the integral, and the Cauchy integral formula are assumed from the preceding articles.

The idempotents of the split complex algebra are $e_+ = \tfrac{1}{2}(1 + j)$ and $e_- = \tfrac{1}{2}(1 - j)$. The idempotent decomposition of a split biquaternion is

$$
\tilde{Q} = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-,
$$

with $\tilde{Q}_\pm = \tilde{Q} e_\pm \in \mathbb{H}$ ordinary quaternions.

## The Split Complex Subspace

### Definition

The **split complex subspace** $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ is the fixed-point set of quaternion conjugation:

$$
\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} = \{\tilde{Q} \in \mathbb{H}_{\mathbb{D}} : \bar{\tilde{Q}} = \tilde{Q}\}.
$$

Explicitly, a split biquaternion is in $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ if and only if it has the form

$$
\tilde{Q} = Q_0 e_0, \qquad Q_0 \in \mathbb{D}.
$$

The vector part vanishes. The subset $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ is a real vector space of dimension 2, and it is a subalgebra of $\mathbb{H}_{\mathbb{D}}$ isomorphic to the split complex algebra $\mathbb{D}$.

### Properties

**Real vector space.** $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ is a real vector space of dimension 2. A basis is $\{e_0, j e_0\}$.

**Subalgebra.** $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ is closed under split biquaternion multiplication. If $\tilde{Q}, \tilde{R} \in \mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, then $\tilde{Q} \tilde{R} \in \mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$.

**Commutative.** $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ is commutative, because the split complex algebra is commutative.

**Not a division algebra.** $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ contains zero divisors. The zero divisors are the elements $Q_0 e_0$ with $Q_0$ a nonzero multiple of $1 \pm j$, i.e., the elements $\pm t(1 \mp j) e_0$ with $t \neq 0$. These form the union of the two real lines $\mathbb{R}(1 + j)$ and $\mathbb{R}(1 - j)$ in the two-dimensional real space $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$.

**Identification with $\mathbb{R}^2$.** The elements of $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ are in bijection with pairs $(q_0, q'_0)$ of real numbers, where $Q_0 = q_0 + j q'_0$. We use the notation

$$
\tilde{X} = x_0 e_0 + j x'_0 e_0, \qquad x_0, x'_0 \in \mathbb{R},
$$

for a general element of $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$. The two real numbers $x_0, x'_0$ are the **coordinates** of $\tilde{X}$ in the split complex subspace.

### Functions on the Split Complex Subspace

A **split-biquaternion-valued function on the split complex subspace** is a map

$$
\tilde{F} : \mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \to \mathbb{H}_{\mathbb{D}}, \qquad \tilde{X} \mapsto \tilde{F}(\tilde{X}).
$$

Writing $\tilde{X} = x_0 e_0 + j x'_0 e_0$, the function $\tilde{F}$ is determined by four split-complex-valued functions $F_\mu$ of the two real variables $x_0, x'_0$:

$$
\tilde{F}(\tilde{X}) = F_0(x_0, x'_0) e_0 + F_1(x_0, x'_0) e_1 + F_2(x_0, x'_0) e_2 + F_3(x_0, x'_0) e_3.
$$

The restriction to $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ reduces the number of independent real variables from eight to two.

### Partial Derivatives

For each $\mu = 0, 1$, we define the partial derivative of $\tilde{F}$ with respect to $x_\mu$ (where $x_1$ stands for $x'_0$) by

$$
\frac{\partial \tilde{F}}{\partial x_\mu} = \sum_{\nu=0}^{3} \frac{\partial F_\nu}{\partial x_\mu} e_\nu.
$$

The partial derivatives commute: $\partial_\mu \partial_\nu \tilde{F} = \partial_\nu \partial_\mu \tilde{F}$ for all $\mu, \nu$.

### The Differential Operators on $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$

Since $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ is two-dimensional, the four-dimensional gradient is not directly applicable. Instead, the natural differential operator is the **split complex derivative**

$$
\partial_{\mathbb{D}} = e_0 \partial_0 + j e_0 \partial'_0,
$$

where $\partial_0 = \partial/\partial x_0$ and $\partial'_0 = \partial/\partial x'_0$. The split complex derivative acts on a function $\tilde{F}$ by

$$
\partial_{\mathbb{D}} \tilde{F} = (\partial_0 F_0 + j \partial'_0 F_0) e_0 + (\partial_0 F_1 + j \partial'_0 F_1) e_1 + \cdots,
$$

which is the split complex derivative of each component.

The **split complex conjugate** of the derivative is

$$
\bar{\partial}_{\mathbb{D}} = e_0 \partial_0 - j e_0 \partial'_0,
$$

and the **split complex Laplacian** is

$$
\partial_{\mathbb{D}} \bar{\partial}_{\mathbb{D}} = \bar{\partial}_{\mathbb{D}} \partial_{\mathbb{D}} = (\partial_0^2 - \partial'^2_0) e_0,
$$

which is the **wave operator** in two dimensions. The operator $\partial_0^2 - \partial'^2_0$ is the d'Alembertian in $1+1$ dimensions.

The **square** of the derivative is

$$
\partial_{\mathbb{D}}^2 = (\partial_0^2 + \partial'^2_0) e_0 + 2 j \partial_0 \partial'_0 e_0,
$$

which is a split-complex-valued operator.

### Integration on $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$

The integral of a split-biquaternion-valued function $\tilde{F}$ over a domain $\Omega \subset \mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ is defined component-wise:

$$
\int_\Omega \tilde{F} \, dV = \sum_{\mu=0}^{3} \left(\int_\Omega F_\mu \, dV\right) e_\mu,
$$

where each $F_\mu$ is integrated over the two-dimensional domain $\Omega$ with respect to the Lebesgue measure on $\mathbb{R}^2$.

The integration theory on $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ is the two-dimensional analogue of the four-dimensional theory. The fundamental solution of the split complex derivative is the kernel

$$
\tilde{G}_{\mathbb{D}}(\tilde{X}) = \frac{\bar{\tilde{X}}}{\|\tilde{X}\|_E^2},
$$

where $\bar{\tilde{X}}$ is the split complex conjugate and $\|\tilde{X}\|_E^2 = x_0^2 + x'^2_0$ is the squared Euclidean norm. The kernel is defined for $\tilde{X} \neq 0$.

The Cauchy integral formula on $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ takes the form

$$
\tilde{F}(\tilde{X}_0) = \frac{1}{2\pi i_{\mathbb{D}}} \int_{\partial \Omega} \tilde{G}_{\mathbb{D}}(\tilde{X} - \tilde{X}_0) \tilde{n} \tilde{F}(\tilde{X}) \, ds(\tilde{X}),
$$

where $i_{\mathbb{D}}$ is a formal imaginary unit in the split complex algebra (which does not exist as an element of $\mathbb{D}$ but is used as a bookkeeping device), and $ds$ is the arc length on the boundary. The formula is not directly analogous to the complex case, because the split complex algebra has no imaginary unit. The correct form is obtained in the idempotent basis, where it reduces to two copies of the real Cauchy integral formula.

### Comparison with the Complex Subspace

In the biquaternion algebra $\mathbb{B}$, the complex subspace $\mathbb{C}_{\mathbb{B}}$ is the fixed-point set of quaternion conjugation, and it is a copy of the complex field. It is a division algebra, and the analysis on it is the ordinary complex analysis.

In the split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$, the split complex subspace $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ is the fixed-point set of quaternion conjugation, and it is a copy of the split complex algebra. It is **not** a division algebra, and the analysis on it is the split complex analysis, which is different from the complex analysis.

The key differences are:

- The split complex subspace contains zero divisors, while the complex subspace does not.
- The split complex Laplacian is the wave operator $\partial_0^2 - \partial'^2_0$, while the complex Laplacian is the harmonic operator $\partial_0^2 + \partial'^2_0$.
- The split complex Cauchy integral formula involves the idempotent decomposition, while the complex Cauchy integral formula is expressed in terms of the imaginary unit.

## The Quaternion Subspace

### Definition

The **quaternion subspace** $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ is the fixed-point set of split complex conjugation:

$$
\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} = \{\tilde{Q} \in \mathbb{H}_{\mathbb{D}} : \tilde{Q}^* = \tilde{Q}\}.
$$

Explicitly, a split biquaternion is in $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ if and only if it has the form

$$
\tilde{Q} = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

All four coefficients are real. The subset $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ is a real vector space of dimension 4, and it is a subalgebra of $\mathbb{H}_{\mathbb{D}}$ isomorphic to the quaternion algebra $\mathbb{H}$.

### Properties

**Real vector space.** $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ is a real vector space of dimension 4. A basis is $\{e_0, e_1, e_2, e_3\}$.

**Subalgebra.** $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ is closed under split biquaternion multiplication, and it is isomorphic to the quaternion algebra.

**Division algebra.** $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ is a division algebra. The norm form restricts to the positive-definite quaternion norm:

$$
N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = q_0^2 + q_1^2 + q_2^2 + q_3^2.
$$

This vanishes if and only if all $q_\mu = 0$. So every nonzero element is invertible, and there are no zero divisors.

**Identification with $\mathbb{R}^4$.** The elements of $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ are in bijection with quadruples $(q_0, q_1, q_2, q_3)$ of real numbers. We use the notation

$$
\tilde{X} = x_0 e_0 + x_1 e_1 + x_2 e_2 + x_3 e_3, \qquad x_0, x_1, x_2, x_3 \in \mathbb{R},
$$

for a general element of $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$.

### Functions and Operators

The functions on $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ are split-biquaternion-valued functions of four real variables. The differential operators are the same as on the general four-dimensional subspace:

$$
\tilde{\nabla} = e_0 \partial_0 + e_1 \partial_1 + e_2 \partial_2 + e_3 \partial_3,
$$

$$
\bar{\tilde{\nabla}} = e_0 \partial_0 - e_1 \partial_1 - e_2 \partial_2 - e_3 \partial_3,
$$

$$
\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = (\partial_0^2 + \Delta) e_0,
$$

$$
\tilde{\nabla}^2 = (\partial_0^2 - \Delta) + 2\sum_{k=1}^{3} e_k \partial_0 \partial_k,
$$

and the convective derivative $\tilde{D}$.

The analysis on $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ is the ordinary quaternion analysis, extended to functions with values in the full split biquaternion algebra. Since there are no zero divisors in $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, the analysis is clean everywhere.

The integral and the Cauchy integral formula are the same as on the general subspace, with the fundamental solution $\tilde{G}(\tilde{X}) = \bar{\tilde{X}}/\|\tilde{X}\|_E^4$.

### Comparison with the Quaternion Subspace of the Biquaternion Algebra

In the biquaternion algebra $\mathbb{B}$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ is the fixed-point set of complex conjugation, and it is a copy of the real quaternion algebra. It is a division algebra, and the analysis on it is the ordinary quaternion analysis.

In the split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$, the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ is the fixed-point set of split complex conjugation, and it is also a copy of the real quaternion algebra. It is a division algebra, and the analysis on it is the ordinary quaternion analysis.

The two quaternion subspaces are isomorphic as algebras, and the analysis on them is the same. The only difference is the embedding in the larger algebra, which affects the interpretation of the functions but not the operators.

## The Hermitian Subspace

### Definition

The **Hermitian subspace** $\mathbb{M}_+$ is the fixed-point set of Hermitian conjugation:

$$
\mathbb{M}_+ = \{\tilde{Q} \in \mathbb{H}_{\mathbb{D}} : \tilde{Q}^\dagger = \tilde{Q}\}.
$$

Explicitly, a split biquaternion is in $\mathbb{M}_+$ if and only if it has the form

$$
\tilde{Q} = q_0 e_0 + j q'_1 e_1 + j q'_2 e_2 + j q'_3 e_3, \qquad q_0, q'_1, q'_2, q'_3 \in \mathbb{R}.
$$

The scalar part is real, and the vector part is purely split-imaginary. The subset $\mathbb{M}_+$ is a real vector space of dimension 4.

### Properties

**Real vector space.** $\mathbb{M}_+$ is a real vector space of dimension 4. A basis is $\{e_0, j e_1, j e_2, j e_3\}$.

**Not a subalgebra.** $\mathbb{M}_+$ is not closed under split biquaternion multiplication.

**Norm form and Hermitian form.** On $\mathbb{M}_+$ the norm form restricts to

$$
N(\tilde{Q}) = (q'_1)^2 + (q'_2)^2 + (q'_3)^2 + q_0^2,
$$

since $(j q'_k)^2 = +(q'_k)^2$: it is positive definite of signature $(4, 0)$. It therefore vanishes only at the origin, and every nonzero element of $\mathbb{M}_+$ is invertible. The indefinite form of signature $(1, 3)$ associated with $\mathbb{M}_+$ is the scalar part of the **Hermitian** form,

$$
Q Q^\dagger = q_0^2 - (q'_1)^2 - (q'_2)^2 - (q'_3)^2,
$$

whose zero set is the three-dimensional cone $q_0^2 = (q'_1)^2 + (q'_2)^2 + (q'_3)^2$; that form does not detect zero divisors either, as the invertible element $e_0 + j e_1$ on the cone shows.

**Identification with $\mathbb{R}^4$.** The elements of $\mathbb{M}_+$ are in bijection with quadruples $(q_0, q'_1, q'_2, q'_3)$ of real numbers. We use the notation

$$
\tilde{X} = x_0 e_0 + j x_1 e_1 + j x_2 e_2 + j x_3 e_3, \qquad x_0, x_1, x_2, x_3 \in \mathbb{R},
$$

for a general element of $\mathbb{M}_+$.

### Functions and Operators

The functions on $\mathbb{M}_+$ are split-biquaternion-valued functions of four real variables. The differential operators are the same as on the general four-dimensional subspace, with the same formulas. The only difference is the interpretation of the coordinates: the zero divisor set does not meet $\mathbb{M}_+$ away from the origin.

The analysis on $\mathbb{M}_+$ is clean away from the origin, where the only singularity of the fundamental solution lies; the light cone of the Hermitian form is not a locus of zero divisors.

### Comparison with the Hermitian Subspace of the Biquaternion Algebra

In the biquaternion algebra $\mathbb{B}$, the Hermitian subspace $\mathbb{M}_+$ is the fixed-point set of Hermitian conjugation, and it has norm form of signature $(1, 3)$ (or $(3, 1)$, depending on convention), because the extra unit there satisfies $i^2 = -1$. The zero divisors form a three-dimensional cone.

In the split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$, the Hermitian subspace $\mathbb{M}_+$ is the fixed-point set of Hermitian conjugation, and its Hermitian form also has signature $(1, 3)$, but its norm form is positive definite of signature $(4, 0)$, so $\mathbb{M}_+$ contains no zero divisors.

The two Hermitian subspaces are isomorphic as real vector spaces and carry Hermitian forms of the same signature, but their norm forms differ: on $\mathbb{B}$ the norm form is the indefinite one and has a light cone of zero divisors, while on $\mathbb{H}_{\mathbb{D}}$ it is positive definite and there are none.

## The Anti-Hermitian Subspace

### Definition

The **anti-Hermitian subspace** $\mathbb{M}_-$ is the fixed-point set of anti-Hermitian conjugation:

$$
\mathbb{M}_- = \{\tilde{Q} \in \mathbb{H}_{\mathbb{D}} : \tilde{Q}^\flat = \tilde{Q}\}.
$$

Explicitly, a split biquaternion is in $\mathbb{M}_-$ if and only if it has the form

$$
\tilde{Q} = j q'_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q'_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

The scalar part is purely split-imaginary, and the vector part is real. The subset $\mathbb{M}_-$ is a real vector space of dimension 4.

### Properties

**Real vector space.** $\mathbb{M}_-$ is a real vector space of dimension 4. A basis is $\{j e_0, e_1, e_2, e_3\}$.

**Not a subalgebra.** $\mathbb{M}_-$ is not closed under split biquaternion multiplication.

**Norm form and Hermitian form.** On $\mathbb{M}_-$ the norm form restricts to

$$
N(\tilde{Q}) = (q'_0)^2 + q_1^2 + q_2^2 + q_3^2,
$$

since $(j q'_0)^2 = +(q'_0)^2$: it is positive definite of signature $(4, 0)$, it vanishes only at the origin, and every nonzero element of $\mathbb{M}_-$ is invertible. The indefinite form of signature $(3, 1)$ associated with $\mathbb{M}_-$ is the scalar part of the **Hermitian** form,

$$
Q Q^\dagger = -(q'_0)^2 + q_1^2 + q_2^2 + q_3^2,
$$

whose zero set is the three-dimensional cone $(q'_0)^2 = q_1^2 + q_2^2 + q_3^2$; as on $\mathbb{M}_+$, that form does not detect zero divisors.

**Identification with $\mathbb{R}^4$.** The elements of $\mathbb{M}_-$ are in bijection with quadruples $(q'_0, q_1, q_2, q_3)$ of real numbers. We use the notation

$$
\tilde{X} = j x_0 e_0 + x_1 e_1 + x_2 e_2 + x_3 e_3, \qquad x_0, x_1, x_2, x_3 \in \mathbb{R},
$$

for a general element of $\mathbb{M}_-$.

### Functions and Operators

The functions on $\mathbb{M}_-$ are split-biquaternion-valued functions of four real variables. The differential operators are the same as on the general four-dimensional subspace, with the same formulas.

The analysis on $\mathbb{M}_-$ is clean away from the origin; as on $\mathbb{M}_+$, the light cone of the Hermitian form is not a locus of zero divisors.

### Comparison with the Anti-Hermitian Subspace of the Biquaternion Algebra

In the biquaternion algebra $\mathbb{B}$, the anti-Hermitian subspace $\mathbb{M}_-$ is the fixed-point set of anti-Hermitian conjugation, and it has norm form of signature $(3, 1)$, again because the extra unit there satisfies $i^2 = -1$. The zero divisors form a three-dimensional cone.

In the split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$, the anti-Hermitian subspace $\mathbb{M}_-$ is the fixed-point set of anti-Hermitian conjugation, and its Hermitian form also has signature $(3, 1)$, but its norm form is positive definite of signature $(4, 0)$, so $\mathbb{M}_-$ contains no zero divisors.

The two anti-Hermitian subspaces are isomorphic as real vector spaces and carry Hermitian forms of the same signature, but their norm forms differ in character, as for $\mathbb{M}_+$. In the biquaternion series, the anti-Hermitian subspace was chosen for the physical applications because the indefinite form of signature $(3, 1)$ is the Lorentzian signature. In the split biquaternion case, the Lorentzian signature $(3, 1)$ is carried by the Hermitian form rather than by the norm form, and the anti-Hermitian subspace is natural for the same reason.

## Comparison of the Four Subspaces

The four subspaces are all real vector spaces, but of different dimensions and with different algebraic properties.

| Property | $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
|---|---|---|---|---|
| Dimension | 2 | 4 | 4 | 4 |
| Fixed-point set of | $\bar{\cdot}$ | ${}^*$ | $\dagger$ | $\flat$ |
| Basis | $\{e_0, j e_0\}$ | $\{e_0, e_1, e_2, e_3\}$ | $\{e_0, j e_1, j e_2, j e_3\}$ | $\{j e_0, e_1, e_2, e_3\}$ |
| Scalar part | Split complex | Real | Real | Purely split-imaginary |
| Vector part | Zero | Real | Purely split-imaginary | Real |
| Hermitian form signature | $(1, 1)$ | $(4, 0)$ | $(1, 3)$ | $(3, 1)$ |
| Zero divisors | Two lines | None | None | None |
| Subalgebra | Yes | Yes | No | No |
| Division algebra | No | Yes | No | No |

The key differences are:

**Dimension.** The split complex subspace is two-dimensional, while the other three are four-dimensional.

**Algebraic structure.** The split complex subspace and the quaternion subspace are subalgebras. The Hermitian and anti-Hermitian subspaces are not.

**Zero divisors.** The split complex subspace contains zero divisors (two lines), and the other three subspaces contain none, since the norm form is positive definite on each of them.

**Hermitian form.** The scalar part of the Hermitian form has signature $(1, 1)$ on the split complex subspace, $(4, 0)$ on the quaternion subspace, $(1, 3)$ on the Hermitian subspace, and $(3, 1)$ on the anti-Hermitian subspace. The norm form itself is positive definite of signature $(4, 0)$ on the quaternion, Hermitian and anti-Hermitian subspaces.

## Relation Between the Subspaces

The four subspaces are related by the conjugations of the split biquaternion algebra.

**Quaternion conjugation.** The quaternion conjugation $\bar{\cdot}$ fixes $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ and preserves $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ (it is the identity only on $\mathbb{R}e_0$), and it preserves $\mathbb{M}_+$ and $\mathbb{M}_-$, negating the vector part in each. It is multiplication by $j$ that exchanges them: $j\mathbb{M}_+ = \mathbb{M}_-$ and $j\mathbb{M}_- = \mathbb{M}_+$.

**Split complex conjugation.** The split complex conjugation ${}^*$ fixes $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ and $\mathbb{M}_-$ (up to sign) and $\mathbb{M}_+$ (up to sign), and maps $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ to itself.

**Hermitian conjugation.** The Hermitian conjugation $\dagger$ fixes $\mathbb{M}_+$ and $\mathbb{M}_-$, and acts on $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ and $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ by the corresponding conjugations.

**Intersections.** The pairwise intersections are:

$$
\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{H}_{\mathbb{H}_{\mathbb{D}}} = \mathbb{R} e_0, \qquad \mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{M}_+ = \mathbb{R} e_0, \qquad \mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{M}_- = \mathbb{R} j e_0,
$$

$$
\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{M}_+ = \mathbb{R} e_0, \qquad \mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{M}_- = \operatorname{span}_{\mathbb{R}}\{e_1, e_2, e_3\}, \qquad \mathbb{M}_+ \cap \mathbb{M}_- = \{0\}.
$$

**Spans.** The pairwise sums are:

$$
\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} + \mathbb{H}_{\mathbb{H}_{\mathbb{D}}} = \operatorname{span}_{\mathbb{R}}\{e_0, j e_0, e_1, e_2, e_3\} \ (\dim 5), \qquad \mathbb{H}_{\mathbb{H}_{\mathbb{D}}} + \mathbb{M}_- = \operatorname{span}_{\mathbb{R}}\{e_0, j e_0, e_1, e_2, e_3\} \ (\dim 5),
$$

and so on. The full algebra is the sum of the subspaces in various ways.

**Compatibility of the analysis.** The differential and integral operators on the four subspaces are the same operators, with the same formulas. The differences are in the domain and in the algebraic properties of the domain. So the analysis on the four subspaces is compatible: a function defined on a domain that intersects two or more subspaces can be analyzed on each subspace separately, and the results agree on the intersections.

## The Idempotent Decomposition and the Subspaces

The four subspaces are related to the idempotent decomposition in the following way.

**Split complex subspace.** The split complex subspace is the set of elements of the form $Q_0 e_0$ with $Q_0 \in \mathbb{D}$. In the idempotent basis, this is

$$
Q_0 e_0 = q_0 e_0 + j q'_0 e_0 = (q_0 + q'_0) e_+ + (q_0 - q'_0) e_-.
$$

So the split complex subspace is the set of elements whose idempotent components are real scalars (i.e., real multiples of the identity in $\mathbb{H}$).

**Quaternion subspace.** The quaternion subspace is the set of elements with real coefficients. In the idempotent basis, an element with real coefficients has the form

$$
q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3 = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-,
$$

where $\tilde{Q}_\pm = q_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ are the same quaternion in each component. So the quaternion subspace is the diagonal in $\mathbb{H} \oplus \mathbb{H}$: the set of pairs $(\tilde{Q}, \tilde{Q})$ with $\tilde{Q} \in \mathbb{H}$.

**Hermitian subspace.** The Hermitian subspace is the set of elements with real scalar part and purely split-imaginary vector part. In the idempotent basis, such an element has the form

$$
q_0 e_0 + j q'_1 e_1 + j q'_2 e_2 + j q'_3 e_3 = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-,
$$

where $\tilde{Q}_+ = q_0 + q'_1 e_1 + q'_2 e_2 + q'_3 e_3$ and $\tilde{Q}_- = q_0 - q'_1 e_1 - q'_2 e_2 - q'_3 e_3 = \bar{\tilde{Q}}_+$. So the Hermitian subspace is the set of pairs $(\tilde{Q}, \bar{\tilde{Q}})$ with $\tilde{Q} \in \mathbb{H}$.

**Anti-Hermitian subspace.** The anti-Hermitian subspace is the set of elements with purely split-imaginary scalar part and real vector part. In the idempotent basis, such an element has the form

$$
j q'_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3 = \tilde{Q}_+ e_+ + \tilde{Q}_- e_-,
$$

where $\tilde{Q}_+ = q'_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ and $\tilde{Q}_- = -q'_0 + q_1 e_1 + q_2 e_2 + q_3 e_3 = -\overline{\tilde{Q}}_+$. So the anti-Hermitian subspace is the set of pairs $(\tilde{Q}, -\bar{\tilde{Q}})$ with $\tilde{Q} \in \mathbb{H}$.

So the four subspaces correspond to four natural conditions on the pair $(\tilde{Q}_+, \tilde{Q}_-)$:

| Subspace | Condition on $(\tilde{Q}_+, \tilde{Q}_-)$ |
|---|---|
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | Both components are real scalars |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | $\tilde{Q}_+ = \tilde{Q}_-$ |
| $\mathbb{M}_+$ | $\tilde{Q}_- = \bar{\tilde{Q}}_+$ |
| $\mathbb{M}_-$ | $\tilde{Q}_- = -\bar{\tilde{Q}}_+$ |

This is the cleanest characterization of the four subspaces, and it shows how they arise from the idempotent decomposition.

## Summary of the Operators

The following table summarizes the differential operators on the four subspaces. The formulas are identical on the four subspaces (with the appropriate dimension); the table is included for reference.

| Operator | Definition | Result |
|---|---|---|
| $\tilde{\nabla}$ | $\sum_{\mu=0}^{3} e_\mu \partial_\mu$ | Split-quaternion-valued first-order operator |
| $\bar{\tilde{\nabla}}$ | $e_0 \partial_0 - \sum_{k=1}^{3} e_k \partial_k$ | Quaternion conjugate of $\tilde{\nabla}$ |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$ | $\partial_0^2 + \Delta$ | Scalar (times $e_0$) second-order operator |
| $\tilde{\nabla}^2$ | $(\partial_0^2 - \Delta) + 2\sum_k e_k \partial_0 \partial_k$ | Split-quaternion-valued second-order operator |
| $\tilde{D} = \bar{\tilde{U}}\tilde{\nabla}$ | $(u_0 \partial_0 + \mathbf{u}\cdot\mathrm{grad}) + \sum_k e_k(u_0 \partial_k - u_k \partial_0) - \mathrm{rot}(\mathbf{u})$ | Split-quaternion-valued first-order operator |
| $\int_\Omega \tilde{F} \, dV$ | $\sum_\mu \left(\int_\Omega F_\mu \, dV\right) e_\mu$ | Split-quaternion-valued integral |
| $\tilde{G}(\tilde{X})$ | $\bar{\tilde{X}}/\|\tilde{X}\|_E^4$ | Fundamental solution of $\tilde{\nabla}$ |

On the split complex subspace, the operators reduce to the two-dimensional operators $\partial_{\mathbb{D}}$, $\bar{\partial}_{\mathbb{D}}$, and $\partial_{\mathbb{D}} \bar{\partial}_{\mathbb{D}} = \partial_0^2 - \partial'^2_0$.

## The Role of the Zero Divisors

The zero divisor set of $\mathbb{H}_{\mathbb{D}}$ is the union of the two four-dimensional linear subspaces $Z_+$ and $Z_-$. The intersection of the zero divisor set with each of the four subspaces is as follows.

**Split complex subspace.** $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \cap (Z_+ \cup Z_-)$ is the union of the two real lines $\mathbb{R}(1 + j)$ and $\mathbb{R}(1 - j)$. These are the zero divisors of the split complex algebra.

**Quaternion subspace.** $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \cap (Z_+ \cup Z_-) = \{0\}$. The quaternion subspace contains no zero divisors.

**Hermitian subspace.** $\mathbb{M}_+ \cap (Z_+ \cup Z_-) = \{0\}$. The Hermitian form has an indefinite light cone of signature $(1, 3)$, but the norm form is positive definite on $\mathbb{M}_+$, so the cone contains no zero divisors.

**Anti-Hermitian subspace.** $\mathbb{M}_- \cap (Z_+ \cup Z_-) = \{0\}$. As on $\mathbb{M}_+$, the Hermitian form has an indefinite light cone of signature $(3, 1)$ but the norm form is positive definite, so the cone contains no zero divisors.

So the four subspaces have different zero divisor structures, and the analysis on each of them must take this into account.

## Open Questions

The following questions are not answered in this article and are left for later work:

1. **The analysis on the split complex subspace.** How does the split complex analysis on $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ relate to the ordinary complex analysis on $\mathbb{C}$? What replaces the complex Cauchy integral formula?

2. **The analysis on the quaternion subspace.** The analysis on $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ is the ordinary quaternion analysis. How does it relate to the analysis on the biquaternion quaternion subspace $\mathbb{H}_{\mathbb{B}}$?

3. **The analysis on $\mathbb{M}_+$ and $\mathbb{M}_-$.** The analysis on these subspaces differs from the quaternion subspace through the Hermitian form, whose light cone replaces the origin as the natural singular locus of the Euclidean kernel. What is the precise structure of the solutions of $\tilde{\nabla}\tilde{F} = 0$ and $\Box\tilde{F} = 0$ on these subspaces?

4. **The interaction between the subspaces.** If a function is defined on two of the subspaces, how do the analyses on the two subspaces interact?

5. **The relation to the biquaternion subspaces.** The biquaternion subspaces $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, and $\mathbb{M}_-$ have their own analyses, developed in the companion articles; how the analysis on each of the four subspaces of this article relates to the analysis on the corresponding biquaternion subspace remains to be made precise.

## Summary

This article studies the four distinguished real subspaces of the split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$ and the analysis on them, continuing the general treatment of split biquaternion analysis. The four subspaces are the fixed-point sets of the four conjugations: the split complex subspace $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, of real dimension two, the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, of dimension four, and the Hermitian and anti-Hermitian subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$. Each is defined precisely, its elements are described explicitly, and the four are compared.

The subspaces are then related to one another and to the idempotent decomposition of the algebra: the conjugations preserve and permute them, and each is described in terms of the idempotent components, so that the analysis on each subspace is the analysis on the corresponding component factor.

The differential operators of the general theory are restricted to the four subspaces and the resulting operators are gathered in a table; the formulas are the same on each subspace, with the appropriate dimension. The final sections record the intersection of the zero divisor set of $\mathbb{H}_{\mathbb{D}}$ with each subspace, and the questions that the article leaves open for later work.

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation of quaternions and biquaternions.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), Chapter 3, for the algebra of the biquaternions.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of the real algebras.
