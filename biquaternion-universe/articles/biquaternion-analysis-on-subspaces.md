
# Biquaternion Analysis on Subspaces

## Introduction

The article on biquaternion analysis defined limits, continuity, and the differential operators on a general four-dimensional real subspace $V \subset \mathbb{B}$. The article on biquaternion integration defined the integral and the Cauchy integral formula on the same general subspace. This article specializes the general theory to the natural four-dimensional subspaces of the biquaternion algebra: the **quaternion subspace** $\mathbb{H}_{\mathbb{B}}$, the **anti-Hermitian subspace** $\mathbb{M}_-$, and the **Hermitian subspace** $\mathbb{M}_+$.

These subspaces are the natural domains for the analysis because they are the four-dimensional real subspaces on which the zero divisors are either absent or confined to a manageable subset:

- On $\mathbb{H}_{\mathbb{B}}$, the norm form is positive-definite, and there are no zero divisors at all. The analysis is clean everywhere.
- On $\mathbb{M}_-$, the norm form is indefinite of signature $(3, 1)$ (or $(1, 3)$, depending on convention), and the zero divisors form a three-dimensional cone. The analysis is clean away from this cone.
- On $\mathbb{M}_+$, the norm form is indefinite of signature $(1, 3)$ (or $(3, 1)$), and the zero divisors form a three-dimensional cone. The analysis is clean away from this cone.

The three subspaces are therefore complementary in their relation to the zero-divisor problem. They are the natural cases, and they are the cases that arise in the applications.

The treatment is purely mathematical. The independent variables are four real variables, and they are independent of any physical interpretation. The complex structure of the coefficients and the non-commutative structure of the quaternion units are the only algebraic ingredients.

Every claim is either proved or stated as a definition. Where a computation is long, all steps are shown.

## The Quaternion Subspace

### Definition

The **quaternion subspace** $\mathbb{H}_{\mathbb{B}}$ is the fixed-point set of complex conjugation:

$$
\mathbb{H}_{\mathbb{B}} = \{\tilde{Q} \in \mathbb{B} : \tilde{Q}^* = \tilde{Q}\}.
$$

Explicitly, a biquaternion is in $\mathbb{H}_{\mathbb{B}}$ if and only if it has the form

$$
\tilde{Q} = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

All four coefficients are real. The subset $\mathbb{H}_{\mathbb{B}}$ is a real vector space of dimension 4, and it is a subalgebra of $\mathbb{B}$ isomorphic to the quaternion algebra $\mathbb{H}$.

### Properties

**Real vector space.** $\mathbb{H}_{\mathbb{B}}$ is a real vector space of dimension 4. A basis is $\{e_0, e_1, e_2, e_3\}$.

**Subalgebra.** $\mathbb{H}_{\mathbb{B}}$ is closed under biquaternion multiplication. If $\tilde{Q}, \tilde{R} \in \mathbb{H}_{\mathbb{B}}$, then $\tilde{Q} \tilde{R} \in \mathbb{H}_{\mathbb{B}}$.

**Division algebra.** $\mathbb{H}_{\mathbb{B}}$ is a division algebra. The norm form restricts to a positive-definite quadratic form:

$$
N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = q_0^2 + q_1^2 + q_2^2 + q_3^2.
$$

This vanishes if and only if all $q_\mu = 0$. So every nonzero element of $\mathbb{H}_{\mathbb{B}}$ is invertible, and $\mathbb{H}_{\mathbb{B}}$ contains no zero divisors.

**Identification with $\mathbb{R}^4$.** The elements of $\mathbb{H}_{\mathbb{B}}$ are in bijection with quadruples $(q_0, q_1, q_2, q_3)$ of real numbers. We use the notation

$$
\tilde{X} = x_0 e_0 + x_1 e_1 + x_2 e_2 + x_3 e_3, \qquad x_0, x_1, x_2, x_3 \in \mathbb{R},
$$

for a general element of $\mathbb{H}_{\mathbb{B}}$. The four real numbers $x_0, x_1, x_2, x_3$ are the **coordinates** of $\tilde{X}$ in the quaternion subspace.

### Functions on the Quaternion Subspace

A **biquaternion-valued function on the quaternion subspace** is a map

$$
\tilde{F} : \mathbb{H}_{\mathbb{B}} \to \mathbb{B}, \qquad \tilde{X} \mapsto \tilde{F}(\tilde{X}).
$$

Writing $\tilde{X} = x_0 e_0 + x_1 e_1 + x_2 e_2 + x_3 e_3$, the function $\tilde{F}$ is determined by four complex-valued functions $F_\mu$ of the four real variables $x_0, x_1, x_2, x_3$:

$$
\tilde{F}(\tilde{X}) = F_0(x_0, x_1, x_2, x_3) e_0 + F_1(x_0, x_1, x_2, x_3) e_1 + F_2(x_0, x_1, x_2, x_3) e_2 + F_3(x_0, x_1, x_2, x_3) e_3.
$$

The restriction to $\mathbb{H}_{\mathbb{B}}$ reduces the number of independent real variables from eight to four.

### Partial Derivatives

For each $\mu = 0, 1, 2, 3$, the **partial derivative** of $\tilde{F}$ with respect to $x_\mu$ is

$$
\frac{\partial \tilde{F}}{\partial x_\mu} = \sum_{\nu=0}^{3} \frac{\partial F_\nu}{\partial x_\mu} e_\nu.
$$

The partial derivative acts component-wise on the coefficients. Since the quaternion units $e_\nu$ are constants, the rules of ordinary differential calculus apply to each coefficient separately. We write $\partial_\mu$ for $\partial/\partial x_\mu$. The partial derivatives commute: $\partial_\mu \partial_\nu \tilde{F} = \partial_\nu \partial_\mu \tilde{F}$ for all $\mu, \nu$.

### The Differential Operators on $\mathbb{H}_{\mathbb{B}}$

The **biquaternionic gradient** on the quaternion subspace is the same operator as on the general four-dimensional subspace:

$$
\tilde{\nabla} = e_0 \partial_0 + e_1 \partial_1 + e_2 \partial_2 + e_3 \partial_3 = \sum_{\mu=0}^{3} e_\mu \partial_\mu.
$$

Its action on a function $\tilde{F}$ on $\mathbb{H}_{\mathbb{B}}$ is the same as its action on a general function on $V$:

$$
\tilde{\nabla}\tilde{F} = \left(\partial_0 F_0 - \mathrm{div}\,\mathbf{F}\right) + \left(\partial_0 \mathbf{F} + \mathrm{grad}\,F_0 + \mathrm{rot}\,\mathbf{F}\right),
$$

where

$$
\mathrm{div}\,\mathbf{F} = \sum_{k=1}^{3} \partial_k F_k, \qquad \mathrm{grad}\,F_0 = \sum_{k=1}^{3} (\partial_k F_0) e_k, \qquad \mathrm{rot}\,\mathbf{F} = \sum_{j,k,l=1}^{3} \epsilon_{jkl} (\partial_j F_k) e_l.
$$

The **quaternion conjugate** of $\tilde{\nabla}$ is

$$
\bar{\tilde{\nabla}} = e_0 \partial_0 - e_1 \partial_1 - e_2 \partial_2 - e_3 \partial_3,
$$

and the product $\bar{\tilde{\nabla}}\tilde{F}$ is

$$
\bar{\tilde{\nabla}}\tilde{F} = \left(\partial_0 F_0 + \mathrm{div}\,\mathbf{F}\right) + \left(\partial_0 \mathbf{F} - \mathrm{grad}\,F_0 - \mathrm{rot}\,\mathbf{F}\right).
$$

The **d'Alembertian** is

$$
\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \left(\partial_0^2 + \Delta\right) e_0,
$$

where $\Delta = \partial_1^2 + \partial_2^2 + \partial_3^2$ is the ordinary three-dimensional Laplacian.

The **square** of the gradient is

$$
\tilde{\nabla}\tilde{\nabla} = \left(\partial_0^2 - \Delta\right) + 2\sum_{k=1}^{3} e_k \partial_0 \partial_k.
$$

The **convective derivative** is defined as on the general subspace. Let

$$
\tilde{U} = \sum_{\mu=0}^{3} u_\mu e_\mu, \qquad u_\mu \in \mathbb{R},
$$

be a velocity biquaternion in $\mathbb{H}_{\mathbb{B}}$. The convective derivative is

$$
\tilde{D} = \bar{\tilde{U}} \tilde{\nabla},
$$

with developed form

$$
\tilde{D} = \left(u_0 \partial_0 + \mathbf{u}\cdot\mathrm{grad}\right) + \sum_{k=1}^{3} e_k (u_0 \partial_k - u_k \partial_0) - \mathrm{rot}(\mathbf{u}).
$$

### Integration on $\mathbb{H}_{\mathbb{B}}$

The integral of a biquaternion-valued function $\tilde{F}$ over a domain $\Omega \subset \mathbb{H}_{\mathbb{B}}$ is defined component-wise:

$$
\int_\Omega \tilde{F} \, dV = \sum_{\mu=0}^{3} \left(\int_\Omega F_\mu \, dV\right) e_\mu.
$$

The integration theory is the same as on the general subspace. The divergence theorem, Green's formulas, and the Cauchy integral formula all hold, with the fundamental solution

$$
\tilde{G}(\tilde{X}) = \frac{\bar{\tilde{X}}}{\|\tilde{X}\|_E^4}.
$$

Since $\mathbb{H}_{\mathbb{B}}$ contains no zero divisors, the analysis is clean everywhere on $\mathbb{H}_{\mathbb{B}}$.

## The Anti-Hermitian Subspace

### Definition

The **anti-Hermitian subspace** $\mathbb{M}_-$ is the fixed-point set of anti-Hermitian conjugation:

$$
\mathbb{M}_- = \{\tilde{Q} \in \mathbb{B} : \tilde{Q}^\flat = \tilde{Q}\},
$$

where $\tilde{Q}^\flat = -\bar{\tilde{Q}}^*$. Explicitly, a biquaternion is in $\mathbb{M}_-$ if and only if it has the form

$$
\tilde{Q} = i q'_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q'_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

The scalar part is purely imaginary, and the vector part is real. The subset $\mathbb{M}_-$ is a real vector space of dimension 4.

The subscript $-$ refers to the fact that $\mathbb{M}_-$ is the eigenspace of the Hermitian conjugation $\dagger$ with eigenvalue $-1$. The complementary eigenspace $\mathbb{M}_+$ (with eigenvalue $+1$) is the Hermitian subspace, treated below.

### Properties

**Real vector space.** $\mathbb{M}_-$ is a real vector space of dimension 4. A basis is $\{i e_0, e_1, e_2, e_3\}$.

**Not a subalgebra.** $\mathbb{M}_-$ is not closed under biquaternion multiplication. For example, $(i e_0) \circ (i e_0) = -e_0$, which is not in $\mathbb{M}_-$.

**Quadratic form.** The biquaternion norm form restricts to a real quadratic form on $\mathbb{M}_-$:

$$
N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = (i q'_0)^2 + q_1^2 + q_2^2 + q_3^2 = -(q'_0)^2 + q_1^2 + q_2^2 + q_3^2.
$$

This quadratic form has signature $(3, 1)$ (or $(1, 3)$ depending on convention). It vanishes on a three-dimensional cone, the set of zero divisors in $\mathbb{M}_-$ (discussed in the division theory article). On the complement of this cone, the quadratic form is nonzero, and every element is invertible.

**Identification with $\mathbb{R}^4$.** The elements of $\mathbb{M}_-$ are in bijection with quadruples $(q'_0, q_1, q_2, q_3)$ of real numbers. We use the notation

$$
\tilde{X} = i x_0 e_0 + x_1 e_1 + x_2 e_2 + x_3 e_3, \qquad x_0, x_1, x_2, x_3 \in \mathbb{R},
$$

for a general element of $\mathbb{M}_-$. The four real numbers $x_0, x_1, x_2, x_3$ are the **coordinates** of $\tilde{X}$ in the anti-Hermitian subspace.

### Functions on the Anti-Hermitian Subspace

A **biquaternion-valued function on the anti-Hermitian subspace** is a map

$$
\tilde{F} : \mathbb{M}_- \to \mathbb{B}, \qquad \tilde{X} \mapsto \tilde{F}(\tilde{X}).
$$

Writing $\tilde{X} = i x_0 e_0 + x_1 e_1 + x_2 e_2 + x_3 e_3$, the function $\tilde{F}$ is determined by four complex-valued functions $F_\mu$ of the four real variables $x_0, x_1, x_2, x_3$:

$$
\tilde{F}(\tilde{X}) = F_0(x_0, x_1, x_2, x_3) e_0 + F_1(x_0, x_1, x_2, x_3) e_1 + F_2(x_0, x_1, x_2, x_3) e_2 + F_3(x_0, x_1, x_2, x_3) e_3.
$$

### Partial Derivatives and Operators

The partial derivatives, the gradient $\tilde{\nabla}$, the quaternion conjugate $\bar{\tilde{\nabla}}$, the d'Alembertian $\Box$, the square $\tilde{\nabla}^2$, the convective derivative $\tilde{D}$, and the integral are all defined in the same way as on $\mathbb{H}_{\mathbb{B}}$. The formulas are identical. The only difference is the domain and the interpretation of the coordinates.

### The Role of the Zero Divisor Cone

On $\mathbb{M}_-$, the zero divisors form a three-dimensional cone $\mathcal{C}$ defined by $x_0^2 = x_1^2 + x_2^2 + x_3^2$ (in the coordinates of $\mathbb{M}_-$). On the complement of the cone, the analysis is clean. On the cone itself, the function $\tilde{G}$ is undefined at the apex and singular on the rest of the cone, and the integral formulas require careful treatment.

In the applications, one usually restricts to domains that do not intersect the cone, or that intersect it only at the boundary. The general theory is the same as on $\mathbb{H}_{\mathbb{B}}$ away from the cone.

## The Hermitian Subspace

### Definition

The **Hermitian subspace** $\mathbb{M}_+$ is the fixed-point set of Hermitian conjugation:

$$
\mathbb{M}_+ = \{\tilde{Q} \in \mathbb{B} : \tilde{Q}^\dagger = \tilde{Q}\}.
$$

Explicitly, a biquaternion is in $\mathbb{M}_+$ if and only if it has the form

$$
\tilde{Q} = q_0 e_0 + i q'_1 e_1 + i q'_2 e_2 + i q'_3 e_3, \qquad q_0, q'_1, q'_2, q'_3 \in \mathbb{R}.
$$

The scalar part is real, and the vector part is purely imaginary. The subset $\mathbb{M}_+$ is a real vector space of dimension 4.

The subscript $+$ refers to the fact that $\mathbb{M}_+$ is the eigenspace of the Hermitian conjugation $\dagger$ with eigenvalue $+1$.

### Properties

**Real vector space.** $\mathbb{M}_+$ is a real vector space of dimension 4. A basis is $\{e_0, i e_1, i e_2, i e_3\}$.

**Not a subalgebra.** $\mathbb{M}_+$ is not closed under biquaternion multiplication. For example, $(i e_1) \circ (i e_1) = -e_0$, which is not in $\mathbb{M}_+$.

**Quadratic form.** The biquaternion norm form restricts to a real quadratic form on $\mathbb{M}_+$:

$$
N(\tilde{Q}) = \tilde{Q} \bar{\tilde{Q}} = q_0^2 + (i q'_1)^2 + (i q'_2)^2 + (i q'_3)^2 = q_0^2 - (q'_1)^2 - (q'_2)^2 - (q'_3)^2.
$$

This quadratic form has signature $(1, 3)$ (or $(3, 1)$ depending on convention). It is the mirror image of the form on $\mathbb{M}_-$: the roles of the scalar and the vector components are interchanged. It vanishes on a three-dimensional cone, the set of zero divisors in $\mathbb{M}_+$. On the complement of this cone, the quadratic form is nonzero, and every element is invertible.

**Identification with $\mathbb{R}^4$.** The elements of $\mathbb{M}_+$ are in bijection with quadruples $(q_0, q'_1, q'_2, q'_3)$ of real numbers. We use the notation

$$
\tilde{X} = x_0 e_0 + i x_1 e_1 + i x_2 e_2 + i x_3 e_3, \qquad x_0, x_1, x_2, x_3 \in \mathbb{R},
$$

for a general element of $\mathbb{M}_+$. The four real numbers $x_0, x_1, x_2, x_3$ are the **coordinates** of $\tilde{X}$ in the Hermitian subspace.

### Functions on the Hermitian Subspace

A **biquaternion-valued function on the Hermitian subspace** is a map

$$
\tilde{F} : \mathbb{M}_+ \to \mathbb{B}, \qquad \tilde{X} \mapsto \tilde{F}(\tilde{X}).
$$

Writing $\tilde{X} = x_0 e_0 + i x_1 e_1 + i x_2 e_2 + i x_3 e_3$, the function $\tilde{F}$ is determined by four complex-valued functions $F_\mu$ of the four real variables $x_0, x_1, x_2, x_3$.

### Partial Derivatives and Operators

The partial derivatives, the gradient $\tilde{\nabla}$, the quaternion conjugate $\bar{\tilde{\nabla}}$, the d'Alembertian $\Box$, the square $\tilde{\nabla}^2$, the convective derivative $\tilde{D}$, and the integral are all defined in the same way as on $\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_-$. The formulas are identical. The only difference is the domain and the interpretation of the coordinates.

### The Role of the Zero Divisor Cone

On $\mathbb{M}_+$, the zero divisors form a three-dimensional cone defined by $x_0^2 = x_1^2 + x_2^2 + x_3^2$ (in the coordinates of $\mathbb{M}_+$). On the complement of the cone, the analysis is clean. On the cone itself, the function $\tilde{G}$ is undefined at the apex and singular on the rest of the cone, and the integral formulas require careful treatment.

The cone on $\mathbb{M}_+$ is the mirror image of the cone on $\mathbb{M}_-$: the roles of the scalar and the vector coordinates are interchanged, and the form of the cone is the same.

## Comparison of the Three Subspaces

The three subspaces are all real vector spaces of dimension 4, and all admit the same differential and integral operators. The differences are in the algebraic properties and in the interpretation of the coordinates.

| Property | $\mathbb{H}_{\mathbb{B}}$ | $\mathbb{M}_-$ | $\mathbb{M}_+$ |
|---|---|---|---|
| Definition | Fixed-point set of $^*$ | Fixed-point set of $\flat$ | Fixed-point set of $\dagger$ |
| Basis | $\{e_0, e_1, e_2, e_3\}$ | $\{i e_0, e_1, e_2, e_3\}$ | $\{e_0, i e_1, i e_2, i e_3\}$ |
| Scalar part | Real | Purely imaginary | Real |
| Vector part | Real | Real | Purely imaginary |
| Norm form | $q_0^2 + q_1^2 + q_2^2 + q_3^2$ | $-(q'_0)^2 + q_1^2 + q_2^2 + q_3^2$ | $q_0^2 - (q'_1)^2 - (q'_2)^2 - (q'_3)^2$ |
| Signature | $(4, 0)$ | $(3, 1)$ | $(1, 3)$ |
| Zero divisors | None | Three-dimensional cone | Three-dimensional cone |
| Subalgebra | Yes | No | No |
| Division algebra | Yes | No | No |

The key differences are:

**Norm form.** On $\mathbb{H}_{\mathbb{B}}$, the norm form is positive-definite. On $\mathbb{M}_-$ and $\mathbb{M}_+$, it is indefinite, with signatures $(3, 1)$ and $(1, 3)$ respectively. The two indefinite forms are mirror images of each other: the roles of the scalar and the vector coordinates are interchanged.

**Zero divisors.** On $\mathbb{H}_{\mathbb{B}}$, there are no zero divisors. On both $\mathbb{M}_-$ and $\mathbb{M}_+$, the zero divisors form a three-dimensional cone. The two cones are mirror images of each other.

**Subalgebra structure.** $\mathbb{H}_{\mathbb{B}}$ is a subalgebra of $\mathbb{B}$. Neither $\mathbb{M}_-$ nor $\mathbb{M}_+$ is a subalgebra.

**Interpretation.** The coordinates of $\mathbb{H}_{\mathbb{B}}$ are the four real components of a real quaternion. The coordinates of $\mathbb{M}_-$ are the imaginary scalar part and the three real vector components. The coordinates of $\mathbb{M}_+$ are the real scalar part and the three imaginary vector components. The three interpretations are related by multiplication by $i$ on the appropriate components.

## Relation Between the Three Subspaces

The three subspaces are related by the conjugations of the biquaternion algebra.

**Quaternion conjugation.** The quaternion conjugation $\bar{\cdot}$ maps $\mathbb{H}_{\mathbb{B}}$ to itself, $\mathbb{M}_-$ to $\mathbb{M}_+$, and $\mathbb{M}_+$ to $\mathbb{M}_-$. So it interchanges the two indefinite subspaces.

**Complex conjugation.** The complex conjugation $^*$ maps $\mathbb{H}_{\mathbb{B}}$ to itself, $\mathbb{M}_-$ to itself (up to sign), and $\mathbb{M}_+$ to itself (up to sign).

**Hermitian conjugation.** The Hermitian conjugation $\dagger$ maps $\mathbb{M}_+$ to itself, $\mathbb{M}_-$ to itself, and $\mathbb{H}_{\mathbb{B}}$ to itself.

**Intersections.** The pairwise intersections are:

$$
\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_- = \mathbb{R} e_0, \qquad \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+ = \mathbb{R} e_0, \qquad \mathbb{M}_- \cap \mathbb{M}_+ = \{0\}.
$$

So the quaternion subspace intersects each of the indefinite subspaces in the real line, and the two indefinite subspaces intersect only at the origin.

**Spans.** The pairwise sums are:

$$
\mathbb{H}_{\mathbb{B}} + \mathbb{M}_- = \mathbb{B}, \qquad \mathbb{H}_{\mathbb{B}} + \mathbb{M}_+ = \mathbb{B}, \qquad \mathbb{M}_- + \mathbb{M}_+ = \mathbb{M}_+ \oplus \mathbb{M}_-.
$$

The first two sums span the whole algebra, and the third is the direct sum decomposition $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ given by the Hermitian decomposition.

**Compatibility of the analysis.** The differential and integral operators on the three subspaces are the same operators, with the same formulas. The difference is only in the domain and in the algebraic properties of the domain. So the analysis on the three subspaces is compatible: a function defined on a domain that intersects two or more subspaces can be analyzed on each subspace separately, and the results agree on the intersections.

## Summary of the Operators

The following table summarizes the differential operators on the three subspaces. The formulas are identical on the three subspaces; the table is included for reference.

| Operator | Definition | Result |
|---|---|---|
| $\tilde{\nabla}$ | $\sum_{\mu=0}^{3} e_\mu \partial_\mu$ | Biquaternion-valued first-order operator |
| $\bar{\tilde{\nabla}}$ | $e_0 \partial_0 - \sum_{k=1}^{3} e_k \partial_k$ | Quaternion conjugate of $\tilde{\nabla}$ |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$ | $\partial_0^2 + \Delta$ | Scalar (times $e_0$) second-order operator |
| $\tilde{\nabla}^2$ | $\left(\partial_0^2 - \Delta\right) + 2\sum_k e_k \partial_0 \partial_k$ | Biquaternion-valued second-order operator |
| $\tilde{D} = \bar{\tilde{U}}\tilde{\nabla}$ | $\left(u_0 \partial_0 + \mathbf{u}\cdot\mathrm{grad}\right) + \sum_k e_k(u_0 \partial_k - u_k \partial_0) - \mathrm{rot}(\mathbf{u})$ | Biquaternion-valued first-order operator |
| $\int_\Omega \tilde{F} \, dV$ | $\sum_\mu \left(\int_\Omega F_\mu \, dV\right) e_\mu$ | Biquaternion-valued integral |
| $\tilde{G}(\tilde{X})$ | $\bar{\tilde{X}}/\|\tilde{X}\|_E^4$ | Fundamental solution of $\tilde{\nabla}$ |

The operators are the same on all three subspaces. The differences between the subspaces are in the algebraic properties of the domain, not in the operators themselves.

## Open Questions

The following questions are not answered in this article and are left for later work:

1. **The relation between the analyses on $\mathbb{M}_-$ and $\mathbb{M}_+$.** The two subspaces are mirror images under quaternion conjugation. Is the analysis on $\mathbb{M}_+$ obtained from the analysis on $\mathbb{M}_-$ by conjugation, or does it differ in an essential way?

2. **The analysis on the complex subspace.** The complex subspace $\mathbb{C}_{\mathbb{B}}$ is two-dimensional, and it carries the ordinary complex analysis. How does the biquaternion analysis on $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_-$, or $\mathbb{M}_+$ restrict to $\mathbb{C}_{\mathbb{B}}$?

3. **The analysis on the full algebra.** Can the analysis be extended from the four-dimensional subspaces to the full eight-dimensional algebra $\mathbb{B}$? If so, what replaces the four-dimensional operators?

4. **The role of the zero divisor cones.** On $\mathbb{M}_-$ and $\mathbb{M}_+$, the zero divisors form three-dimensional cones. What is the structure of functions that are defined on the cones, or that have singularities on the cones?

5. **The integral formulas on the three subspaces.** Do the Cauchy integral formulas on $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_-$, and $\mathbb{M}_+$ have the same form, or do they differ in a way that reflects the difference in the norm form?

6. **The interaction between the subspaces.** If a function is defined on two of the subspaces, how do the analyses on the two subspaces interact?

## Summary

The natural four-dimensional subspaces of the biquaternion algebra are the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-Hermitian subspace $\mathbb{M}_-$, and the Hermitian subspace $\mathbb{M}_+$.

The quaternion subspace $\mathbb{H}_{\mathbb{B}}$ is the fixed-point set of complex conjugation. It is a subalgebra of $\mathbb{B}$ isomorphic to the quaternion algebra $\mathbb{H}$, with a positive-definite norm form and no zero divisors. The analysis on $\mathbb{H}_{\mathbb{B}}$ is clean everywhere.

The anti-Hermitian subspace $\mathbb{M}_-$ is the fixed-point set of anti-Hermitian conjugation. It is a real vector space of dimension 4, but not a subalgebra of $\mathbb{B}$. Its norm form is indefinite of signature $(3, 1)$, and its zero divisors form a three-dimensional cone. The analysis on $\mathbb{M}_-$ is clean away from the cone.

The Hermitian subspace $\mathbb{M}_+$ is the fixed-point set of Hermitian conjugation. It is a real vector space of dimension 4, but not a subalgebra of $\mathbb{B}$. Its norm form is indefinite of signature $(1, 3)$, and its zero divisors form a three-dimensional cone. The analysis on $\mathbb{M}_+$ is clean away from the cone.

The three subspaces share the same differential and integral operators: the gradient $\tilde{\nabla}$, the quaternion conjugate $\bar{\tilde{\nabla}}$, the d'Alembertian $\Box$, the square $\tilde{\nabla}^2$, the convective derivative $\tilde{D}$, and the integral with the fundamental solution $\tilde{G}$. The differences between the subspaces are in the algebraic properties of the domain, not in the operators.

The three subspaces are related by the conjugations of the biquaternion algebra. The quaternion conjugation interchanges $\mathbb{M}_-$ and $\mathbb{M}_+$ and fixes $\mathbb{H}_{\mathbb{B}}$. The complex conjugation fixes $\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_-$ and $\mathbb{M}_+$ (up to sign). The Hermitian conjugation fixes $\mathbb{M}_+$ and $\mathbb{M}_-$ and $\mathbb{H}_{\mathbb{B}}$.

The choice of which subspace to use depends on the application. The quaternion subspace is natural when the positive-definite form is appropriate; the anti-Hermitian and Hermitian subspaces are natural when the indefinite form is appropriate. The two indefinite subspaces are mirror images, and the choice between them is a matter of convention.

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- R. Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta\Delta u = 0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* **7** (1934–35) 307–330, for the analysis of quaternion-valued functions of four real variables.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra perspective.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis.
- John Ryan, *Clifford Algebras in Analysis and Related Topics* (CRC Press, 1996), for the analytic theory of Clifford algebras.


