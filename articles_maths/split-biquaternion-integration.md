
# __Split-Biquaternion Integration__

## Introduction

This article introduces the integration theory of split-biquaternion-valued functions. It follows the article on split biquaternion analysis, which defined limits, continuity, and the differential operators on a four-dimensional real subspace $V \subset \mathbb{H}_{\mathbb{D}}$. The goal here is to define the integral of a split-biquaternion-valued function, establish the standard properties, and derive the integral formulas that are the counterparts of the Cauchy integral formula and its consequences.

The treatment is purely mathematical. The independent variables are four real variables. They are the coordinates of $\mathbb{R}^4$, and they are independent of any physical interpretation. The split complex structure of the coefficients and the non-commutative structure of the quaternion units are the only algebraic ingredients.

Every claim is either proved or stated as a definition. Where a computation is long, all steps are shown.

The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$, its conjugations, its four fixed-point subspaces, the Euclidean norm, the split-biquaternion gradient $\tilde{\nabla}$, the quaternion conjugate $\tilde{\nabla}^{\natural}$, the d'Alembertian $\Box$, the square $\tilde{\nabla}^2$, and the convective derivative $\tilde{D}$ are assumed from the preceding articles.

The idempotents of the split complex algebra are $\tilde\Pi_1 = \tfrac{1}{2}(1 + j)$ and $\tilde\Pi_2 = \tfrac{1}{2}(1 - j)$. The idempotent decomposition of a split biquaternion is

$$
\tilde{Q} = \tilde{Q}_+ \tilde\Pi_1 + \tilde{Q}_- \tilde\Pi_2,
$$

with $\tilde{Q}_\pm = \tilde{Q} \tilde\Pi_{1,2} \in \mathbb{H}$ ordinary quaternions.

## The Integral of a Split-Biquaternion-Valued Function

### Definition

Let $V$ be a four-dimensional real subspace of $\mathbb{H}_{\mathbb{D}}$, with coordinates $Q_t, Q_x, Q_y, Q_z$. Let $F^{\mathrm{fn}} : V \to \mathbb{H}_{\mathbb{D}}$ be a split-biquaternion-valued function, written in components as

$$
F^{\mathrm{fn}}(\tilde{Q}) = \sum_{\mu\in\{t,x,y,z\}} F_\mu(Q_t, Q_x, Q_y, Q_z) e_\mu, \qquad F_\mu \in \mathbb{D}.
$$

Let $\Omega \subset V$ be a domain. The **integral** of $F^{\mathrm{fn}}$ over $\Omega$ is

$$
\int_\Omega F^{\mathrm{fn}} \, dV = \sum_{\mu\in\{t,x,y,z\}} \left(\int_\Omega F_\mu \, dV\right) e_\mu,
$$

where each $F_\mu$ is a split-complex-valued function on $\Omega$. Writing $F_\mu = u_\mu + j v_\mu$ with $u_\mu, v_\mu \in \mathbb{R}$, the integral is

$$
\int_\Omega F_\mu \, dV = \left(\int_\Omega u_\mu \, dV\right) + j \left(\int_\Omega v_\mu \, dV\right),
$$

where each of the eight real-valued integrals is the ordinary Lebesgue integral with respect to the Lebesgue measure on $V \cong \mathbb{R}^4$.

The integral is defined component-wise. It exists whenever each of the eight real-valued functions is integrable over $\Omega$.

### Linearity

**Theorem (linearity).** For any $\alpha, \beta \in \mathbb{D}$ and integrable functions $F^{\mathrm{fn}}, G^{\mathrm{fn}}$,

$$
\int_\Omega (\alpha F^{\mathrm{fn}} + \beta G^{\mathrm{fn}}) \, dV = \alpha \int_\Omega F^{\mathrm{fn}} \, dV + \beta \int_\Omega G^{\mathrm{fn}} \, dV.
$$

**Proof.** This follows from the component-wise definition and the linearity of the Lebesgue integral.

### Additivity

**Theorem (additivity).** If $\Omega = \Omega_1 \cup \Omega_2$ with $\Omega_1 \cap \Omega_2$ of measure zero, then

$$
\int_\Omega F^{\mathrm{fn}} \, dV = \int_{\Omega_1} F^{\mathrm{fn}} \, dV + \int_{\Omega_2} F^{\mathrm{fn}} \, dV.
$$

**Proof.** This follows from the additivity of the Lebesgue integral.

### The Fundamental Estimate

**Theorem (fundamental estimate).** If $\|F^{\mathrm{fn}}\|_E \leq M$ on $\Omega$ and $\mathrm{vol}(\Omega)$ is the volume of $\Omega$, then

$$
\left\| \int_\Omega F^{\mathrm{fn}} \, dV \right\|_E \leq M \cdot \mathrm{vol}(\Omega).
$$

**Proof.** For each of the eight real components,

$$
\left| \int_\Omega u_\mu \, dV \right| \leq \int_\Omega |u_\mu| \, dV \leq \int_\Omega \|F^{\mathrm{fn}}\|_E \, dV \leq M \cdot \mathrm{vol}(\Omega),
$$

and similarly for $v_\mu$. So each component is bounded by $M \cdot \mathrm{vol}(\Omega)$, and the Euclidean norm, which is equivalent to the maximum of the absolute values of the eight components, is bounded by the same constant.

### Integrability

**Theorem (integrability).** If $F^{\mathrm{fn}}$ is continuous on a compact domain $\Omega$, then $F^{\mathrm{fn}}$ is integrable over $\Omega$.

**Proof.** A continuous real-valued function on a compact subset of $\mathbb{R}^4$ is bounded and Lebesgue-integrable. Applying this to each of the eight real components and using the component-wise definition gives the result.

**Theorem (absolute integrability).** If $\|F^{\mathrm{fn}}\|_E$ is integrable over $\Omega$, then $F^{\mathrm{fn}}$ is integrable over $\Omega$.

**Proof.** Since $|u_\mu| \leq \|F^{\mathrm{fn}}\|_E$ and $|v_\mu| \leq \|F^{\mathrm{fn}}\|_E$ for each $\mu$, the integrability of $\|F^{\mathrm{fn}}\|_E$ implies the integrability of each component.

### The Integral in the Idempotent Basis

Because the split biquaternion algebra is the direct sum of two copies of the quaternion algebra, the integral can be computed in the idempotent basis. Writing $F^{\mathrm{fn}} = F^{\mathrm{fn}}_+ \tilde\Pi_1 + F^{\mathrm{fn}}_- \tilde\Pi_2$ with $F^{\mathrm{fn}}_\pm \in \mathbb{H}$,

$$
\int_\Omega F^{\mathrm{fn}} \, dV = \left(\int_\Omega F^{\mathrm{fn}}_+ \, dV\right) \tilde\Pi_1 + \left(\int_\Omega F^{\mathrm{fn}}_- \, dV\right) \tilde\Pi_2,
$$

where each of the two integrals is the quaternion-valued integral of the corresponding component. So the integration of split-biquaternion-valued functions reduces to the integration of two quaternion-valued functions, one for each idempotent component.

This is the same reduction as for the differential operators: the split biquaternion analysis is the quaternion analysis applied to each of the two components separately.

## Integration by Parts

### The Scalar Case

**Theorem (integration by parts).** Let $\phi$ be a scalar function and $F^{\mathrm{fn}}$ a split-biquaternion-valued function, both continuously differentiable on a domain $\Omega$ with piecewise smooth boundary $\partial \Omega$. Then for each $\mu$,

$$
\int_\Omega (\partial/\partial q_\mu \phi) F^{\mathrm{fn}} \, dV = \int_{\partial \Omega} \phi F^{\mathrm{fn}} \, n_\mu \, dS - \int_\Omega \phi (\partial/\partial q_\mu F^{\mathrm{fn}}) \, dV,
$$

where $n_\mu$ is the $\mu$-th component of the outward unit normal on $\partial \Omega$ and $dS$ is the surface measure.

**Proof.** This is the standard integration by parts formula in $\mathbb{R}^4$, applied to the scalar function $\phi$ and each of the eight real components of $F^{\mathrm{fn}}$. Summing over the components gives the result.

### The Vector Case

**Theorem (integration by parts for the gradient).** Let $F^{\mathrm{fn}}$ and $G^{\mathrm{fn}}$ be continuously differentiable split-biquaternion-valued functions on $\Omega$ with piecewise smooth boundary $\partial \Omega$, and write

$$
F^{\mathrm{fn}}\overleftarrow{\nabla} = \sum_{\mu\in\{t,x,y,z\}} (\partial/\partial q_\mu F^{\mathrm{fn}}) e_\mu
$$

for the **right gradient** of $F^{\mathrm{fn}}$. Then

$$
\int_\Omega F^{\mathrm{fn}} (\tilde{\nabla}G^{\mathrm{fn}}) \, dV = \int_{\partial \Omega} F^{\mathrm{fn}} \tilde{n} G^{\mathrm{fn}} \, dS - \int_\Omega (F^{\mathrm{fn}}\overleftarrow{\nabla}) G^{\mathrm{fn}} \, dV,
$$

and equivalently

$$
\int_\Omega (\tilde{\nabla}F^{\mathrm{fn}}) G^{\mathrm{fn}} \, dV = \int_{\partial \Omega} \tilde{n} F^{\mathrm{fn}} G^{\mathrm{fn}} \, dS - \int_\Omega \sum_{\mu\in\{t,x,y,z\}} e_\mu F^{\mathrm{fn}} (\partial/\partial q_\mu G^{\mathrm{fn}}) \, dV,
$$

where $\tilde{n} = \sum_\mu n_\mu e_\mu$ is the split-biquaternion-valued outward unit normal.

**Proof.** The Leibniz rule for the gradient gives $\tilde{\nabla}(F^{\mathrm{fn}}G^{\mathrm{fn}}) = (\tilde{\nabla}F^{\mathrm{fn}})G^{\mathrm{fn}} + \sum_\mu e_\mu F^{\mathrm{fn}}\,\partial/\partial q_\mu G^{\mathrm{fn}}$, and the divergence theorem applied to the product $F^{\mathrm{fn}}G^{\mathrm{fn}}$ gives the second display. For the first display, apply the ordinary divergence theorem in $\mathbb{R}^4$ to the field with components $F^{\mathrm{fn}} e_\mu G^{\mathrm{fn}}$ and sum over $\mu$.

**Remark (the non-commutative correction).** The transposition that moves the derivative off $G^{\mathrm{fn}}$ while leaving $F^{\mathrm{fn}}(\tilde{\nabla}G^{\mathrm{fn}})$ in the volume term is **false for a non-central** $F^{\mathrm{fn}}$: the Leibniz term $\sum_\mu e_\mu F^{\mathrm{fn}}\,\partial/\partial q_\mu G^{\mathrm{fn}}$ equals $F^{\mathrm{fn}}(\tilde{\nabla}G^{\mathrm{fn}})$ only when $F^{\mathrm{fn}}$ commutes with every unit $e_\mu$. The right gradient $\overleftarrow{\nabla}$ is the transposition that removes the restriction.

## The Divergence Theorem

**Theorem (divergence theorem).** Let $F^{\mathrm{fn}}$ be a continuously differentiable split-biquaternion-valued function on a domain $\Omega$ with piecewise smooth boundary $\partial \Omega$. Then

$$
\int_\Omega \tilde{\nabla} F^{\mathrm{fn}} \, dV = \int_{\partial \Omega} \tilde{n} F^{\mathrm{fn}} \, dS,
$$

where $\tilde{n} = \sum_{\mu\in\{t,x,y,z\}} n_\mu e_\mu$ is the split-biquaternion-valued outward unit normal.

**Proof.** The gradient $\tilde{\nabla}F^{\mathrm{fn}}$ is a split-biquaternion-valued function with components

$$
(\tilde{\nabla}F^{\mathrm{fn}})_\nu = \sum_{\mu\in\{t,x,y,z\}} (\partial/\partial q_\mu F_\nu) e_\mu e_\nu.
$$

Integrating each component over $\Omega$ and applying the ordinary divergence theorem in $\mathbb{R}^4$ gives

$$
\int_\Omega \partial/\partial q_\mu F_\nu \, dV = \int_{\partial \Omega} F_\nu n_\mu \, dS.
$$

Multiplying by $e_\mu e_\nu$ and summing gives the result.

**Theorem (divergence theorem for the quaternion conjugate).** Under the same hypotheses,

$$
\int_\Omega \tilde{\nabla}^{\natural} F^{\mathrm{fn}} \, dV = \int_{\partial \Omega} \tilde{n}^{\natural} F^{\mathrm{fn}} \, dS,
$$

where $\tilde{n}^{\natural} = n_0 e_t - \sum_{k=1}^{3} n_k \vec e_k$ is the quaternion conjugate of the outward unit normal.

**Proof.** This is the same computation as above, with the signs of the vector components reversed.

## Green's Formulas

### First Green's Formula

**Theorem (first Green's formula).** Let $F^{\mathrm{fn}}$ and $G^{\mathrm{fn}}$ be twice continuously differentiable split-biquaternion-valued functions on $\Omega$ with piecewise smooth boundary $\partial \Omega$, and let $\partial/\partial\tilde n = \sum_\mu n_\mu \partial/\partial q_\mu$ be the scalar normal derivative. Then

$$
\int_\Omega \left[ \sum_{\mu\in\{t,x,y,z\}} (\partial/\partial q_\mu F^{\mathrm{fn}})\, ((\partial/\partial q_\mu G^{\mathrm{fn}}))^{\natural} + F^{\mathrm{fn}}\, (\Box G^{\mathrm{fn}})^{\natural} \right] dV = \int_{\partial \Omega} F^{\mathrm{fn}}\, (\partial/\partial\tilde n G^{\mathrm{fn}})^{\natural} \, dS.
$$

**Proof.** Apply the ordinary divergence theorem in $\mathbb{R}^4$ to the split-biquaternion-valued field with components $F^{\mathrm{fn}}\,(\partial/\partial q_\mu G^{\mathrm{fn}})^{\natural}$: it gives $\int_\Omega \partial/\partial q_\mu\,(F^{\mathrm{fn}}\,(\partial/\partial q_\mu G^{\mathrm{fn}})^{\natural})\,dV = \int_{\partial\Omega} n_\mu F^{\mathrm{fn}}\,(\partial/\partial q_\mu G^{\mathrm{fn}})^{\natural}\,dS$. The product rule expands the volume integrand as $(\partial/\partial q_\mu F^{\mathrm{fn}})\,(\partial/\partial q_\mu G^{\mathrm{fn}})^{\natural} + F^{\mathrm{fn}}\,(\partial^2/\partial q_\mu^2 G^{\mathrm{fn}})^{\natural}$, the second term because $\partial/\partial q_\mu$ is real and therefore commutes with the conjugation. Summing over $\mu$ replaces $\sum_\mu \partial^2/\partial q_\mu^2$ by $\Box$ and $\sum_\mu n_\mu \partial/\partial q_\mu$ by $\partial/\partial\tilde n$.

### Second Green's Formula

**Theorem (second Green's formula).** Under the same hypotheses,

$$
\int_\Omega \left[ F^{\mathrm{fn}}\, (\Box G^{\mathrm{fn}})^{\natural} - (\Box F^{\mathrm{fn}})\, {G^{\mathrm{fn}}}^{\natural} \right] dV = \int_{\partial \Omega} \left[ F^{\mathrm{fn}}\, (\partial/\partial\tilde n G^{\mathrm{fn}})^{\natural} - (\partial/\partial\tilde n F^{\mathrm{fn}})\, {G^{\mathrm{fn}}}^{\natural} \right] dS.
$$

**Proof.** For each $\mu$ the product rule gives

$$
\partial/\partial q_\mu \left[ F^{\mathrm{fn}}\, (\partial/\partial q_\mu G^{\mathrm{fn}})^{\natural} - (\partial/\partial q_\mu F^{\mathrm{fn}})\, {G^{\mathrm{fn}}}^{\natural} \right] = F^{\mathrm{fn}}\, (\partial^2/\partial q_\mu^2 G^{\mathrm{fn}})^{\natural} - (\partial^2/\partial q_\mu^2 F^{\mathrm{fn}})\, {G^{\mathrm{fn}}}^{\natural},
$$

the two mixed terms being the same product and cancelling. Summing over $\mu$ makes the left side the divergence of a split-biquaternion-valued field, whose volume integral is the stated volume integrand and whose boundary integral, by the ordinary divergence theorem and $\sum_\mu n_\mu \partial/\partial q_\mu = \partial/\partial\tilde n$, is the stated surface term. The conjugation is inert throughout because $\partial/\partial q_\mu$ is real.

### Green's Formula for the d'Alembertian

**Theorem (Green's formula for $\Box$).** Let $F^{\mathrm{fn}}$ and $G^{\mathrm{fn}}$ be twice continuously differentiable split-biquaternion-valued functions on $\Omega$ with piecewise smooth boundary $\partial \Omega$, and let $\partial/\partial\tilde n = \sum_\mu n_\mu \partial/\partial q_\mu$. Then

$$
\int_\Omega \left[ (\Box F^{\mathrm{fn}}) G^{\mathrm{fn}} - F^{\mathrm{fn}} (\Box G^{\mathrm{fn}}) \right] dV = \int_{\partial \Omega} \left[ (\partial/\partial\tilde n F^{\mathrm{fn}}) G^{\mathrm{fn}} - F^{\mathrm{fn}} (\partial/\partial\tilde n G^{\mathrm{fn}}) \right] dS,
$$

where $\Box = \partial^2/\partial Q_t^2 + \Delta$ is the four-dimensional Laplacian.

**Proof.** For each $\mu$ the product rule gives

$$
\partial/\partial q_\mu \left[ (\partial/\partial q_\mu F^{\mathrm{fn}}) G^{\mathrm{fn}} - F^{\mathrm{fn}} (\partial/\partial q_\mu G^{\mathrm{fn}}) \right] = (\partial^2/\partial q_\mu^2 F^{\mathrm{fn}}) G^{\mathrm{fn}} - F^{\mathrm{fn}} (\partial^2/\partial q_\mu^2 G^{\mathrm{fn}}),
$$

the two mixed terms cancelling. Summing over $\mu$ makes the left side a divergence whose volume integral is the stated volume integrand, and whose boundary integral, by the ordinary divergence theorem and $\sum_\mu n_\mu \partial/\partial q_\mu = \partial/\partial\tilde n$, is the stated surface term. This is the conjugate pairing of the second Green formula above, i.e. the second Green formula with $G^{\mathrm{fn}}$ replaced by ${G^{\mathrm{fn}}}^{\natural}$ up to the sign of both sides.

## The Fundamental Solution

### Definition

The **fundamental solution** of the gradient operator $\tilde{\nabla}$ is the split-biquaternion-valued function

$$
G^{\mathrm{fn}}(\tilde{Q}) = \frac{\tilde{Q}^{\natural}}{\|\tilde{Q}\|_E^4},
$$

where $\tilde{Q}^{\natural}$ is the quaternion conjugate of $\tilde{Q}$ and $\|\tilde{Q}\|_E^4 = (\|\tilde{Q}\|_E^2)^2$ is the fourth power of the Euclidean norm.

The function $G^{\mathrm{fn}}$ is defined for $\tilde{Q} \neq 0$. It is homogeneous of degree $-3$: $G^{\mathrm{fn}}(\lambda \tilde{Q}) = \lambda^{-3} G^{\mathrm{fn}}(\tilde{Q})$ for $\lambda > 0$.

The formula is identical to the biquaternion case. The reason is that the fundamental solution depends only on the Euclidean structure of the underlying real vector space $\mathbb{R}^4$ and on the quaternion conjugate, not on the sign of the extra unit.

### The Gradient of the Fundamental Solution

**Theorem.** For $\tilde{Q} \neq 0$,

$$
\tilde{\nabla} G^{\mathrm{fn}}(\tilde{Q}) = 0.
$$

**Proof.** Write $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ and $\|\tilde{Q}\|_E^2 = \sum_\mu Q_\mu^2$. The quaternion conjugate is $\tilde{Q}^{\natural} = Q_t e_t - \sum_k Q_k \vec e_k$. So

$$
G^{\mathrm{fn}}(\tilde{Q}) = \frac{Q_t e_t - \sum_k Q_k \vec e_k}{(\sum_\mu Q_\mu^2)^2}.
$$

A direct computation gives

$$
\tilde{\nabla} G^{\mathrm{fn}} = \sum_\mu e_\mu \partial/\partial q_\mu \left( \frac{\tilde{Q}^{\natural}}{\|\tilde{Q}\|_E^4} \right) = \frac{\tilde{\nabla} \tilde{Q}^{\natural}}{\|\tilde{Q}\|_E^4} + \tilde{Q}^{\natural} \tilde{\nabla} \left( \frac{1}{\|\tilde{Q}\|_E^4} \right).
$$

The first term is $\sum_\mu e_\mu \partial/\partial q_\mu \tilde{Q}^{\natural} = \sum_\mu e_\mu e_\mu^{\natural} = e_t - \vec e_x^2 - \vec e_y^2 - \vec e_z^2 = e_t + e_t + e_t + e_t = 4 e_t$. The second term is

$$
\tilde{Q}^{\natural} \tilde{\nabla} \left( \frac{1}{\|\tilde{Q}\|_E^4} \right) = \tilde{Q}^{\natural} \sum_\mu e_\mu \partial/\partial q_\mu \left( \frac{1}{\|\tilde{Q}\|_E^4} \right) = \tilde{Q}^{\natural} \sum_\mu e_\mu \left( -\frac{4 Q_\mu}{\|\tilde{Q}\|_E^6} \right) = -\frac{4 \tilde{Q}^{\natural} \tilde{Q}}{\|\tilde{Q}\|_E^6}.
$$

Since $\tilde{Q}^{\natural} \tilde{Q} = \|\tilde{Q}\|_E^2 e_t$, the second term is $-4 \|\tilde{Q}\|_E^2 / \|\tilde{Q}\|_E^6 \cdot e_t = -4 e_t / \|\tilde{Q}\|_E^4$. So the two terms cancel, and $\tilde{\nabla} G^{\mathrm{fn}} = 0$.

### The Distributional Gradient

**Theorem.** In the sense of distributions,

$$
\tilde{\nabla} G^{\mathrm{fn}} = 2\pi^2 \delta_0 e_t,
$$

where $\delta_0$ is the delta distribution at the origin and $2\pi^2$ is the surface area of the unit three-sphere in $\mathbb{R}^4$.

**Proof.** The function $G^{\mathrm{fn}}$ is locally integrable and smooth away from the origin. For a test function $\phi$ with compact support, the pairing $\langle \tilde{\nabla} G^{\mathrm{fn}}, \phi \rangle$ is defined by integration by parts:

$$
\langle \tilde{\nabla} G^{\mathrm{fn}}, \phi \rangle = -\int_{\mathbb{R}^4} G^{\mathrm{fn}} (\tilde{\nabla} \phi) \, dV = -\lim_{\varepsilon \to 0} \int_{\|\tilde{Q}\|_E > \varepsilon} G^{\mathrm{fn}} (\tilde{\nabla} \phi) \, dV.
$$

Applying the divergence theorem to the domain $\|\tilde{Q}\|_E > \varepsilon$ and using $\tilde{\nabla} G^{\mathrm{fn}} = 0$ away from the origin gives

$$
\int_{\|\tilde{Q}\|_E > \varepsilon} G^{\mathrm{fn}} (\tilde{\nabla} \phi) \, dV = \int_{\|\tilde{Q}\|_E = \varepsilon} G^{\mathrm{fn}} \tilde{n} \phi \, dS - \int_{\|\tilde{Q}\|_E > \varepsilon} (\tilde{\nabla} G^{\mathrm{fn}}) \phi \, dV = \int_{\|\tilde{Q}\|_E = \varepsilon} G^{\mathrm{fn}} \tilde{n} \phi \, dS.
$$

On the sphere $\|\tilde{Q}\|_E = \varepsilon$, the outward unit normal of the region $\|\tilde{Q}\|_E > \varepsilon$ points away from the origin, i.e. inward across this inner sphere, so $\tilde{n} = -\tilde{Q}/\varepsilon$, and $G^{\mathrm{fn}} = \tilde{Q}^{\natural}/\varepsilon^4$. So

$$
G^{\mathrm{fn}} \tilde{n} = \frac{\tilde{Q}^{\natural}}{\varepsilon^4} \cdot \left(-\frac{\tilde{Q}}{\varepsilon}\right) = -\frac{\|\tilde{Q}\|_E^2}{\varepsilon^5} e_t = -\frac{\varepsilon^2}{\varepsilon^5} e_t = -\frac{1}{\varepsilon^3} e_t.
$$

So

$$
\int_{\|\tilde{Q}\|_E = \varepsilon} G^{\mathrm{fn}} \tilde{n} \phi \, dS = -\frac{1}{\varepsilon^3} \int_{\|\tilde{Q}\|_E = \varepsilon} \phi \, dS \cdot e_t.
$$

As $\varepsilon \to 0$, the average of $\phi$ over the sphere tends to $\phi(0)$, and the surface area of the sphere of radius $\varepsilon$ is $2\pi^2 \varepsilon^3$. So the integral tends to $-2\pi^2 \phi(0) e_t$. Therefore

$$
\langle \tilde{\nabla} G^{\mathrm{fn}}, \phi \rangle = 2\pi^2 \phi(0) e_t,
$$

which is the distributional identity $\tilde{\nabla} G^{\mathrm{fn}} = 2\pi^2 \delta_0 e_t$, in agreement with the statement of the theorem.

## The Cauchy Integral Formula

### Statement

**Theorem (Cauchy integral formula).** Let $F^{\mathrm{fn}}$ be a continuously differentiable split-biquaternion-valued function on a domain $\Omega$ with piecewise smooth boundary $\partial \Omega$, and let $\tilde{Q}_0$ be an interior point of $\Omega$. Then

$$
F^{\mathrm{fn}}(\tilde{Q}_0) = \frac{1}{2\pi^2} \int_{\partial \Omega} G^{\mathrm{fn}}(\tilde{Q} - \tilde{Q}_0) \tilde{n} F^{\mathrm{fn}}(\tilde{Q}) \, dS(\tilde{Q}) - \frac{1}{2\pi^2} \int_\Omega G^{\mathrm{fn}}(\tilde{Q} - \tilde{Q}_0) (\tilde{\nabla}F^{\mathrm{fn}})(\tilde{Q}) \, dV(\tilde{Q}),
$$

where $G^{\mathrm{fn}}$ is the fundamental solution defined above, $\tilde{n}$ is the split-biquaternion-valued outward unit normal, and $dS$ is the surface measure.

### The Regular Case

**Theorem (Cauchy integral formula for regular functions).** If $F^{\mathrm{fn}}$ satisfies $\tilde{\nabla}F^{\mathrm{fn}} = 0$ on $\Omega$ (the split biquaternion analogue of the Cauchy–Riemann equations), then

$$
F^{\mathrm{fn}}(\tilde{Q}_0) = \frac{1}{2\pi^2} \int_{\partial \Omega} G^{\mathrm{fn}}(\tilde{Q} - \tilde{Q}_0) \tilde{n} F^{\mathrm{fn}}(\tilde{Q}) \, dS(\tilde{Q}).
$$

### Proof of the Cauchy Integral Formula

Apply the divergence theorem to the product $G^{\mathrm{fn}}(\tilde{Q} - \tilde{Q}_0) F^{\mathrm{fn}}(\tilde{Q})$ on the domain $\Omega_\varepsilon = \Omega \setminus B(\tilde{Q}_0, \varepsilon)$, where $B(\tilde{Q}_0, \varepsilon)$ is the ball of radius $\varepsilon$ centred at $\tilde{Q}_0$. The boundary of $\Omega_\varepsilon$ consists of $\partial \Omega$ and the sphere $\partial B(\tilde{Q}_0, \varepsilon)$.

By the divergence theorem,

$$
\int_{\Omega_\varepsilon} \tilde{\nabla} \left( G^{\mathrm{fn}}(\tilde{Q} - \tilde{Q}_0) F^{\mathrm{fn}}(\tilde{Q}) \right) dV = \int_{\partial \Omega} G^{\mathrm{fn}}(\tilde{Q} - \tilde{Q}_0) \tilde{n} F^{\mathrm{fn}}(\tilde{Q}) \, dS + \int_{\partial B(\tilde{Q}_0, \varepsilon)} G^{\mathrm{fn}}(\tilde{Q} - \tilde{Q}_0) \tilde{n} F^{\mathrm{fn}}(\tilde{Q}) \, dS.
$$

On the small sphere, the outward normal of $\Omega_\varepsilon$ points toward $\tilde{Q}_0$, so $\tilde{n} = -(\tilde{Q} - \tilde{Q}_0)/\varepsilon$, and the computation of the boundary term gives

$$
\int_{\partial B(\tilde{Q}_0, \varepsilon)} G^{\mathrm{fn}}(\tilde{Q} - \tilde{Q}_0) \tilde{n} F^{\mathrm{fn}}(\tilde{Q}) \, dS \to -2\pi^2 F^{\mathrm{fn}}(\tilde{Q}_0) \quad \text{as } \varepsilon \to 0.
$$

The volume integral on the left is

$$
\int_{\Omega_\varepsilon} \tilde{\nabla} \left( G^{\mathrm{fn}}(\tilde{Q} - \tilde{Q}_0) F^{\mathrm{fn}}(\tilde{Q}) \right) dV = \int_{\Omega_\varepsilon} G^{\mathrm{fn}}(\tilde{Q} - \tilde{Q}_0) (\tilde{\nabla}F^{\mathrm{fn}})(\tilde{Q}) \, dV,
$$

using the product rule and the fact that $\tilde{\nabla}G^{\mathrm{fn}} = 0$ away from $\tilde{Q}_0$.

Combining and taking the limit $\varepsilon \to 0$, we obtain

$$
\int_\Omega G^{\mathrm{fn}}(\tilde{Q} - \tilde{Q}_0) (\tilde{\nabla}F^{\mathrm{fn}})(\tilde{Q}) \, dV = \int_{\partial \Omega} G^{\mathrm{fn}}(\tilde{Q} - \tilde{Q}_0) \tilde{n} F^{\mathrm{fn}}(\tilde{Q}) \, dS - 2\pi^2 F^{\mathrm{fn}}(\tilde{Q}_0).
$$

Rearranging gives the stated formula.

### The Cauchy Integral Formula in the Idempotent Basis

In the idempotent basis, the Cauchy integral formula decomposes into two copies of the quaternion Cauchy integral formula. Writing $F^{\mathrm{fn}} = F^{\mathrm{fn}}_+ \tilde\Pi_1 + F^{\mathrm{fn}}_- \tilde\Pi_2$ and $G^{\mathrm{fn}} = G^{\mathrm{fn}}_+ \tilde\Pi_1 + G^{\mathrm{fn}}_- \tilde\Pi_2$,

$$
F^{\mathrm{fn}}_\pm(\tilde{Q}_0) = \frac{1}{2\pi^2} \int_{\partial \Omega} G^{\mathrm{fn}}_\pm(\tilde{Q} - \tilde{Q}_0) \tilde{n} F^{\mathrm{fn}}_\pm(\tilde{Q}) \, dS(\tilde{Q}) - \frac{1}{2\pi^2} \int_\Omega G^{\mathrm{fn}}_\pm(\tilde{Q} - \tilde{Q}_0) (\tilde{\nabla}F^{\mathrm{fn}}_\pm)(\tilde{Q}) \, dV(\tilde{Q}),
$$

where each formula is the quaternion Cauchy integral formula for the component. So the split biquaternion Cauchy integral formula is the pair of the quaternion Cauchy integral formulas, one for each component.

## Consequences of the Cauchy Integral Formula

### The Mean Value Property

**Theorem (mean value property).** If $F^{\mathrm{fn}}$ satisfies $\tilde{\nabla}F^{\mathrm{fn}} = 0$ on a ball $B(\tilde{Q}_0, r)$, then

$$
F^{\mathrm{fn}}(\tilde{Q}_0) = \frac{1}{2\pi^2 r^3} \int_{\partial B(\tilde{Q}_0, r)} F^{\mathrm{fn}}(\tilde{Q}) \, dS(\tilde{Q}),
$$

where $2\pi^2 r^3$ is the surface area of the three-sphere of radius $r$ in $\mathbb{R}^4$.

**Proof.** Apply the Cauchy integral formula to the ball $B(\tilde{Q}_0, r)$ and use the explicit form of the fundamental solution. The kernel becomes constant on the sphere, and the integral reduces to the average of $F^{\mathrm{fn}}$ over the sphere.

### The Maximum Principle

**Theorem (maximum principle).** If $F^{\mathrm{fn}}$ satisfies $\tilde{\nabla}F^{\mathrm{fn}} = 0$ on a domain $\Omega$ and $\|F^{\mathrm{fn}}\|_E$ attains its maximum at an interior point of $\Omega$, then $F^{\mathrm{fn}}$ is constant on $\Omega$.

**Proof.** Use the mean value property: if $\|F^{\mathrm{fn}}\|_E$ attains its maximum at $\tilde{Q}_0$, then $F^{\mathrm{fn}}(\tilde{Q}_0)$ equals the average of $F^{\mathrm{fn}}$ over every small sphere around $\tilde{Q}_0$, so $\|F^{\mathrm{fn}}(\tilde{Q}_0)\|_E \leq$ the average of $\|F^{\mathrm{fn}}\|_E \leq \|F^{\mathrm{fn}}(\tilde{Q}_0)\|_E$; both inequalities are equalities, so $\|F^{\mathrm{fn}}\|_E$ is constant on each such sphere. The Cauchy estimates for the first derivatives then give $\partial/\partial q_\mu F^{\mathrm{fn}}(\tilde{Q}_0) = 0$, so $F^{\mathrm{fn}}$ is constant in a neighbourhood of $\tilde{Q}_0$, and iterating over a connected chain of spheres, $F^{\mathrm{fn}}$ is constant on $\Omega$.

### Liouville's Theorem

**Theorem (Liouville).** If $F^{\mathrm{fn}}$ satisfies $\tilde{\nabla}F^{\mathrm{fn}} = 0$ on all of $V$ and $\|F^{\mathrm{fn}}\|_E$ is bounded, then $F^{\mathrm{fn}}$ is constant.

**Proof.** Apply the Cauchy integral formula to a large ball of radius $R$ centred at $\tilde{Q}_0$, and estimate the boundary integral using the boundedness of $F^{\mathrm{fn}}$. The kernel $G^{\mathrm{fn}}(\tilde{Q} - \tilde{Q}_0)$ is of order $R^{-3}$ on the sphere of radius $R$, and the surface area is of order $R^3$, so the boundary integral is of order $R^0$, i.e., bounded. As $R \to \infty$, the boundary integral tends to zero (using the decay of the kernel and the boundedness of $F^{\mathrm{fn}}$), so $F^{\mathrm{fn}}(\tilde{Q}_0)$ is independent of $\tilde{Q}_0$.

### The Identity Theorem

**Theorem (identity theorem).** If two functions $F^{\mathrm{fn}}$ and $G^{\mathrm{fn}}$ satisfying $\tilde{\nabla}F^{\mathrm{fn}} = \tilde{\nabla}G^{\mathrm{fn}} = 0$ on a connected domain $\Omega$ agree on an open subset of $\Omega$, then they agree on all of $\Omega$.

**Proof.** The difference $H^{\mathrm{fn}} = F^{\mathrm{fn}} - G^{\mathrm{fn}}$ satisfies $\tilde{\nabla}H^{\mathrm{fn}} = 0$ and vanishes on an open subset. By the maximum principle applied to $H^{\mathrm{fn}}$ and to $-H^{\mathrm{fn}}$, the modulus of $H^{\mathrm{fn}}$ cannot attain a maximum at an interior point unless $H^{\mathrm{fn}}$ is constant, and since $H^{\mathrm{fn}}$ vanishes on an open subset, the constant is zero.

### The Cauchy Estimates

**Theorem (Cauchy estimates).** If $F^{\mathrm{fn}}$ satisfies $\tilde{\nabla}F^{\mathrm{fn}} = 0$ on a ball $B(\tilde{Q}_0, R)$ and $\|F^{\mathrm{fn}}\|_E \leq M$ on the boundary, then for every multi-index $\alpha$,

$$
\|\partial^\alpha F^{\mathrm{fn}}(\tilde{Q}_0)\|_E \leq \frac{C_\alpha M}{R^{|\alpha|}},
$$

where $C_\alpha$ is a constant depending on $\alpha$ and $|\alpha|$ is the total order of the multi-index.

**Proof.** Differentiate the Cauchy integral formula with respect to $\tilde{Q}_0$ and estimate the resulting integral using the bound on $F^{\mathrm{fn}}$.

## The Residue Theory

### The Residue

The Cauchy integral formula for a function that is regular except at isolated singularities leads to a residue theory. However, the non-commutativity of $\mathbb{H}_{\mathbb{D}}$ and the presence of the zero divisor set make the definition of the residue more delicate than in the complex case.

**Definition (isolated singularity).** A point $\tilde{Q}_0$ is an **isolated singularity** of $F^{\mathrm{fn}}$ if $F^{\mathrm{fn}}$ is defined and regular on a punctured neighborhood $0 < \|\tilde{Q} - \tilde{Q}_0\|_E < r$ of $\tilde{Q}_0$.

**Definition (residue).** The **residue** of $F^{\mathrm{fn}}$ at an isolated singularity $\tilde{Q}_0$ is the split biquaternion

$$
\mathrm{Res}(F^{\mathrm{fn}}, \tilde{Q}_0) = \frac{1}{2\pi^2} \int_{\partial B(\tilde{Q}_0, \varepsilon)} G^{\mathrm{fn}}(\tilde{Q} - \tilde{Q}_0) \tilde{n} F^{\mathrm{fn}}(\tilde{Q}) \, dS(\tilde{Q}),
$$

where $\varepsilon$ is small enough that the sphere does not enclose any other singularity.

### The Residue Theorem

**Theorem (residue theorem).** Let $F^{\mathrm{fn}}$ be regular on a domain $\Omega$ except at isolated singularities $\tilde{Q}_1, \dots, \tilde{Q}_n$. Then

$$
\frac{1}{2\pi^2} \int_{\partial \Omega} G^{\mathrm{fn}}(\tilde{Q} - \tilde{Q}_0) \tilde{n} F^{\mathrm{fn}}(\tilde{Q}) \, dS(\tilde{Q}) = \sum_{k=1}^{n} \mathrm{Res}(F^{\mathrm{fn}}, \tilde{Q}_k)
$$

for any $\tilde{Q}_0$ outside the singularities.

**Proof.** Apply the Cauchy integral formula to the domain with small spheres removed around each singularity, and use the definition of the residue.

### The Residue in the Idempotent Basis

In the idempotent basis, the residue decomposes into two quaternion residues:

$$
\mathrm{Res}(F^{\mathrm{fn}}, \tilde{Q}_0) = \mathrm{Res}(F^{\mathrm{fn}}_+, \tilde{Q}_0) \tilde\Pi_1 + \mathrm{Res}(F^{\mathrm{fn}}_-, \tilde{Q}_0) \tilde\Pi_2,
$$

where each of the two residues is the quaternion residue of the corresponding component. So the split biquaternion residue theory is the pair of the quaternion residue theories, one for each component.

## The Role of the Zero Divisors

The zero divisor set of $\mathbb{H}_{\mathbb{D}}$ is the union of two four-dimensional linear subspaces $Z_+$ and $Z_-$. In the integration theory, the zero divisors play the following roles.

**In the fundamental solution.** The fundamental solution $G^{\mathrm{fn}}(\tilde{Q}) = \tilde{Q}^{\natural}/\|\tilde{Q}\|_E^4$ is defined for every $\tilde{Q} \neq 0$, including the nonzero zero divisors, since its denominator is the Euclidean norm. On the split complex directions the identity $\tilde{Q}^{\natural}\tilde{Q} = \|\tilde{Q}\|_E^2 e_t$ fails (for $\tilde{Q} = 1 + j$ one has $\tilde{Q}^{\natural}\tilde{Q} = 2 + 2j \neq 2$), and with it the proof that $\tilde{\nabla}G^{\mathrm{fn}} = 0$; the only singularity of $G^{\mathrm{fn}}$ is the origin.

**In the Cauchy integral formula.** The formula requires the function $F^{\mathrm{fn}}$ to be continuously differentiable on the domain. If the domain intersects the zero divisor set, the formula requires care, because the proof that the kernel is annihilated by the gradient fails on the intersection.

**In the residue theory.** The definition of the residue involves an integral over a small sphere around the singularity. If the sphere intersects the zero divisor set, the integral requires care.

**In the idempotent basis.** In the idempotent basis, the zero divisor set is described by the conditions $F^{\mathrm{fn}}_+ = 0$ or $F^{\mathrm{fn}}_- = 0$. The integration theory on the two components is the quaternion integration theory, which does not have zero divisors. So the zero divisor issue is isolated to the points where one of the components vanishes.

## The Relation to Complex and Quaternionic Analysis

The integration theory developed in this article is the split biquaternion analogue of the Cauchy integral theory in complex analysis and of the Fueter theory in quaternionic analysis.

**Complex analysis.** In complex analysis, the Cauchy integral formula expresses the value of a holomorphic function at an interior point in terms of its boundary values, with the kernel $1/(A - A_0)$. The split biquaternion analogue uses the kernel $G^{\mathrm{fn}}(\tilde{Q} - \tilde{Q}_0) = ((\tilde{Q} - \tilde{Q}_0))^{\natural}/\|\tilde{Q} - \tilde{Q}_0\|_E^4$, which is the fundamental solution of the gradient operator in four dimensions.

**Quaternionic analysis.** In Fueter's quaternionic analysis, the analogue of the Cauchy integral formula involves the kernel $\tilde q^{-1}/\|\tilde q\|^2$ and the quaternion-valued integration over the boundary of a domain in $\mathbb{R}^4$. The split biquaternion case is the generalization to split complex coefficients, and the idempotent decomposition reduces it to two copies of the quaternion case.

**Clifford analysis.** The general Clifford analysis on $\mathbb{R}^n$ uses the kernel $\tilde Q^{-1}/\|\tilde Q\|^{n-2}$, equivalently $\tilde Q^{\natural}/\|\tilde Q\|^n$ (homogeneous of degree $1 - n$), and the Clifford algebra-valued integration. The split biquaternion case is the case $n = 4$ of this general theory, with the specific structure of the even subalgebra of a definite (Euclidean) Clifford algebra.

## The Relation to the Split Complex Case

In the split complex algebra $\mathbb{D}$, the integration theory is different because the algebra is two-dimensional. The Cauchy integral formula for split complex functions involves the kernel $1/(A - A_0)$, whose singular locus is the translate $A_0 + \mathbb{R}(1 \pm j)$ of the zero divisor set of $\mathbb{D}$. The integral formula is

$$
f(A_0) = \frac{1}{2\pi i_{\mathbb{D}}} \oint_\gamma \frac{f(A)}{A - A_0} \, dA,
$$

where $i_{\mathbb{D}}$ is the "imaginary" unit of the split complex algebra. But the split complex algebra has no imaginary unit, so the formula is not directly analogous to the complex case. Instead, the split complex integration theory is expressed in the idempotent basis, where it reduces to two copies of the real integration theory.

The split biquaternion integration theory is the extension of the split complex integration theory by the quaternion units. The idempotent decomposition reduces it to two copies of the quaternion integration theory, which is the cleanest way to understand its structure.

## Open Questions

The following questions are not answered in this article and are left for later work:

1. **The residue theory in the non-commutative case.** The definition of the residue given above is one of several possible definitions. What is the correct definition that makes the residue theorem hold in the strongest form?

2. **The Cauchy integral formula for other domains.** What is the form of the Cauchy integral formula for domains with non-smooth boundaries, or for domains that are not simply connected?

3. **The role of the zero divisor set.** How do the integral formulas behave when the domain intersects the zero divisor set?

4. **The relation to the polar decomposition.** How does the polar decomposition of the split biquaternion algebra interact with the integration theory?

5. **The relation to the integral formulas of Clifford analysis.** How does the split biquaternion integration theory relate to the general Clifford analysis with split signature?

6. **Applications.** What are the applications of the split biquaternion integration theory to the solution of partial differential equations?

7. **The integration of functions on the split complex subspace.** How does the integration theory extend to the two-dimensional split complex subspace, and what replaces the four-dimensional Cauchy integral formula?

## Summary

The integral of a split-biquaternion-valued function on a four-dimensional subspace $V \subset \mathbb{H}_{\mathbb{D}}$ is defined component-wise with respect to the Lebesgue measure. It is linear, additive, and satisfies the fundamental estimate. The standard theorems of integration carry over: integration by parts, the divergence theorem, and Green's formulas. Because the algebra is not commutative, transposing the gradient off a product requires the right gradient $\overleftarrow{\nabla}$, and the identities are stated in the forms that hold for general split-biquaternion-valued fields.

The **fundamental solution** of the gradient operator is $G^{\mathrm{fn}}(\tilde{Q}) = \tilde{Q}^{\natural}/\|\tilde{Q}\|_E^4$, which satisfies $\tilde{\nabla}G^{\mathrm{fn}} = 2\pi^2 \delta_0 e_t$, the distributional identity established above.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}}$ | Split biquaternion algebra, $\mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis |
| $j$ | Split complex unit, central, $j^2 = +1$ |
| $\tilde\Pi_{1,2} = \tfrac{1}{2}(1 \pm j)$ | Idempotents of $\mathbb{D}$ |
| $\tilde{Q} = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu$ | General split biquaternion |
| $Q_\mu = q_\mu + j q'_\mu$, $F_\mu = u_\mu + j v_\mu$ | Split complex coefficients and values |
| ${}^{\natural}, \bar{\cdot}, {}^\dagger, {}^\flat$ | The four conjugations |
| $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q} \tilde{Q}^{\natural}$ | Split-Biquaternion norm |
| $\tilde{Q}_\pm = \tilde{Q} \tilde\Pi_{1,2}$ | Idempotent components |
| $V$ | A four-dimensional real subspace, coordinates $Q_t, \dots, Q_z$ |
| $\Omega \subset V$ | Domain of integration |
| $\partial \Omega$ | Boundary of $\Omega$ |
| $\int_\Omega F^{\mathrm{fn}} \, dV$ | Integral of $F^{\mathrm{fn}}$ over $\Omega$ |
| $\tilde{\nabla}, \tilde{\nabla}^{\natural}, \Box, \tilde{\nabla}^2, \tilde{D}$ | Gradient, conjugate gradient, d'Alembertian, gradient square, convective derivative |
| $\tilde{E}$ | Fundamental solution of $\Box$ |
| $\tilde{K}$ | Cauchy kernel |
| $\mathrm{Res}(F^{\mathrm{fn}}, \tilde{Q}_0)$ | Residue at an isolated singularity |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original formulation of quaternions and biquaternions.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), Chapter 3, for the algebra of the biquaternions.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of the real algebras.
