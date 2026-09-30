# __Biquaternion Integration__

## Introduction

This article introduces the integration theory of biquaternion-valued functions. It follows *Biquaternion Analysis*, which defined limits, continuity and the differential operators on a four-dimensional real subspace of $\mathbb{B}$. The goal is to define the integral of a biquaternion-valued function, establish the standard properties, and derive the integral formulas that are the counterparts of the Cauchy integral formula and its consequences in complex analysis.

Throughout the main body we work on the **quaternion subspace** $\mathbb{H}_{\mathbb{B}}$, whose four coordinates $q_0, q_1, q_2, q_3$ are all real. On this subspace the framework's partial derivatives coincide with the ordinary real partial derivatives, and the framework's gradient $\tilde{\nabla}$ coincides with the Cauchy–Riemann operator on $\mathbb{R}^4$. The integration theory on $\mathbb{H}_{\mathbb{B}}$ is therefore the standard Clifford analysis of $\mathbb{R}^4$, with $\mathbb{B} \cong \mathrm{Cl}_{1,3}^+$ playing the role of the Clifford algebra. The extension to the indefinite subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$, where the partial derivatives carry factors of $-i$, is not developed here; it is discussed in the open questions. The anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ is one further case of the same kind as $\mathbb{H}_{\mathbb{B}}$: every coefficient is purely imaginary, so the theory there is the theory below carried through the central rotation $\tilde{Q} \mapsto i\tilde{Q}$, with the Cauchy kernel scaled by $i$ and the sign of the d'Alembertian reversed. That case therefore needs no separate treatment.

The physical content of the article is the field-theoretic machinery of conservation laws and Green's functions: the divergence theorem is the conservation of a four-current, the fundamental solution is the Green's function of the d'Alembertian, and the Cauchy integral formula is the representation of a field by its boundary values. Every claim is either proved or stated as a definition. Where a computation is long, all steps are shown.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$, central scalar imaginary $i$, and general element $\tilde{Q}=\sum_\mu Q_\mu e_\mu$; on $\mathbb{H}_{\mathbb{B}}$ the coordinates $q_\mu$ are real. Its conjugations, its six distinguished subspaces, the Euclidean norm and the biquaternionic gradient $\tilde{\nabla}$, the quaternion conjugate $\bar{\tilde{\nabla}}$, the d'Alembertian $\Box$ and the convective derivative are assumed from *Biquaternion Algebra* and *Biquaternion Analysis*; the null cone and the zero divisors are *Biquaternion Norm and Invertibility* and *Biquaternion Zero Divisors*.

## The Integral of a Biquaternion-Valued Function

### Definition

Let $\tilde{F} : \mathbb{H}_{\mathbb{B}} \to \mathbb{B}$ be a biquaternion-valued function, written in components as

$$
\tilde{F}(\tilde{Q}) = \sum_{\mu=0}^{3} F_\mu(q_0, q_1, q_2, q_3) e_\mu, \qquad F_\mu \in \mathbb{C}.
$$

Let $\Omega \subset \mathbb{H}_{\mathbb{B}}$ be a domain. The **integral** of $\tilde{F}$ over $\Omega$ is

$$
\int_\Omega \tilde{F} \, dV = \sum_{\mu=0}^{3} \left(\int_\Omega F_\mu \, dV\right) e_\mu,
$$

where each $F_\mu$ is a complex-valued function on $\Omega$ and the integral is the ordinary Lebesgue integral with respect to the Lebesgue measure on the four real coordinates $(q_0, q_1, q_2, q_3)$.

The integral is defined component-wise. It exists whenever each of the four complex-valued functions $F_\mu$ is integrable over $\Omega$.

### Linearity

**Theorem (linearity).** For any $\alpha, \beta \in \mathbb{C}$ and integrable functions $\tilde{F}, \tilde{G}$,

$$
\int_\Omega (\alpha \tilde{F} + \beta \tilde{G}) \, dV = \alpha \int_\Omega \tilde{F} \, dV + \beta \int_\Omega \tilde{G} \, dV.
$$

**Proof.** This follows from the component-wise definition and the linearity of the Lebesgue integral.

### Additivity

**Theorem (additivity).** If $\Omega = \Omega_1 \cup \Omega_2$ with $\Omega_1 \cap \Omega_2$ of measure zero, then

$$
\int_\Omega \tilde{F} \, dV = \int_{\Omega_1} \tilde{F} \, dV + \int_{\Omega_2} \tilde{F} \, dV.
$$

**Proof.** This follows from the additivity of the Lebesgue integral.

### The Fundamental Estimate

**Theorem (fundamental estimate).** If $\|\tilde{F}\|_E \leq M$ on $\Omega$ and $\mathrm{vol}(\Omega)$ is the volume of $\Omega$, then

$$
\left\| \int_\Omega \tilde{F} \, dV \right\|_E \leq M \cdot \mathrm{vol}(\Omega).
$$

**Proof.** For each component,

$$
\left| \int_\Omega F_\mu \, dV \right| \leq \int_\Omega |F_\mu| \, dV \leq \int_\Omega \|\tilde{F}\|_E \, dV \leq M \cdot \mathrm{vol}(\Omega).
$$

So each component is bounded by $M \cdot \mathrm{vol}(\Omega)$, and the Euclidean norm, which is equivalent to the maximum of the moduli of the components, is bounded by the same constant.

### Integrability

**Theorem (integrability).** If $\tilde{F}$ is continuous on a compact domain $\Omega$, then $\tilde{F}$ is integrable over $\Omega$.

**Proof.** A continuous complex-valued function on a compact subset of $\mathbb{R}^4$ is bounded and Lebesgue-integrable. Applying this to each component and using the component-wise definition gives the result.

**Theorem (absolute integrability).** If $\|\tilde{F}\|_E$ is integrable over $\Omega$, then $\tilde{F}$ is integrable over $\Omega$.

**Proof.** Since $|F_\mu| \leq \|\tilde{F}\|_E$ for each $\mu$, the integrability of $\|\tilde{F}\|_E$ implies the integrability of each $|F_\mu|$, hence the integrability of each $F_\mu$.

## Integration by Parts

### The Scalar Case

**Theorem (integration by parts).** Let $\phi$ be a scalar function and $\tilde{F}$ a biquaternion-valued function, both continuously differentiable on a domain $\Omega$ with piecewise smooth boundary $\partial \Omega$. Then for each $\mu$,

$$
\int_\Omega \left(\frac{\partial \phi}{\partial q_\mu}\right) \tilde{F} \, dV = \int_{\partial \Omega} \phi \tilde{F} \, n_\mu \, dS - \int_\Omega \phi \left(\frac{\partial \tilde{F}}{\partial q_\mu}\right) dV,
$$

where $n_\mu$ is the $\mu$-th component of the outward unit normal on $\partial \Omega$ and $dS$ is the surface measure.

**Proof.** This is the standard integration by parts formula in $\mathbb{R}^4$, applied to the scalar function $\phi$ and the scalar function $F_\nu$ for each component. Summing over $\nu$ gives the result.

### The Vector Case

**Theorem (integration by parts for the gradient).** Let $\tilde{F}$ and $\tilde{G}$ be continuously differentiable biquaternion-valued functions on $\Omega$ with piecewise smooth boundary $\partial \Omega$, and write

$$
\tilde{F}\overleftarrow{\nabla} = \sum_{\mu=0}^{3} \left(\frac{\partial \tilde{F}}{\partial q_\mu}\right) e_\mu
$$

for the **right gradient** of $\tilde{F}$. Then

$$
\int_\Omega \tilde{F} (\tilde{\nabla}\tilde{G}) \, dV = \int_{\partial \Omega} \tilde{F} \tilde{n} \tilde{G} \, dS - \int_\Omega (\tilde{F}\overleftarrow{\nabla}) \tilde{G} \, dV,
$$

and equivalently

$$
\int_\Omega (\tilde{\nabla}\tilde{F}) \tilde{G} \, dV = \int_{\partial \Omega} \tilde{n} \tilde{F} \tilde{G} \, dS - \int_\Omega \sum_{\mu=0}^{3} e_\mu \tilde{F} \left(\frac{\partial \tilde{G}}{\partial q_\mu}\right) dV,
$$

where $\tilde{n} = \sum_\mu n_\mu e_\mu$ is the biquaternion-valued outward unit normal.

**Proof.** The Leibniz rule for the gradient gives $\tilde{\nabla}(\tilde{F}\tilde{G}) = (\tilde{\nabla}\tilde{F})\tilde{G} + \sum_\mu e_\mu \tilde{F}\,\partial_\mu \tilde{G}$, and the divergence theorem applied to the product $\tilde{F}\tilde{G}$ gives the second display. For the first display, apply the ordinary divergence theorem in $\mathbb{R}^4$ to the field with components $\tilde{F} e_\mu \tilde{G}$ and sum over $\mu$.

**Remark (the non-commutative correction).** The transposition that moves the derivative off $\tilde{G}$ while leaving $\tilde{F}(\tilde{\nabla}\tilde{G})$ in the volume term is **false for a non-central** $\tilde{F}$: the Leibniz term $\sum_\mu e_\mu \tilde{F}\,\partial_\mu \tilde{G}$ equals $\tilde{F}(\tilde{\nabla}\tilde{G})$ only when $\tilde{F}$ commutes with every unit $e_\mu$. The right gradient $\overleftarrow{\nabla}$ is the transposition that removes the restriction.

## The Divergence Theorem

**Theorem (divergence theorem).** Let $\tilde{F}$ be a continuously differentiable biquaternion-valued function on a domain $\Omega$ with piecewise smooth boundary $\partial \Omega$. Then

$$
\int_\Omega \tilde{\nabla} \tilde{F} \, dV = \int_{\partial \Omega} \tilde{n} \tilde{F} \, dS,
$$

where $\tilde{n} = \sum_{\mu=0}^{3} n_\mu e_\mu$ is the biquaternion-valued outward unit normal.

**Proof.** The gradient $\tilde{\nabla}\tilde{F}$ is a biquaternion-valued function with components

$$
(\tilde{\nabla}\tilde{F})_\nu = \sum_{\mu=0}^{3} \left(\frac{\partial F_\nu}{\partial q_\mu}\right) e_\mu e_\nu.
$$

Integrating each component over $\Omega$ and applying the ordinary divergence theorem in $\mathbb{R}^4$ gives

$$
\int_\Omega \frac{\partial F_\nu}{\partial q_\mu} \, dV = \int_{\partial \Omega} F_\nu n_\mu \, dS.
$$

Multiplying by $e_\mu e_\nu$ and summing gives the result.

**Theorem (divergence theorem for the quaternion conjugate).** Under the same hypotheses,

$$
\int_\Omega \bar{\tilde{\nabla}} \tilde{F} \, dV = \int_{\partial \Omega} \bar{\tilde{n}} \tilde{F} \, dS,
$$

where $\bar{\tilde{n}} = n_0 e_0 - \sum_{k=1}^{3} n_k e_k$ is the quaternion conjugate of the outward unit normal.

**Proof.** This is the same computation as above, with the signs of the vector components reversed.

**Physical reading: conservation of a four-current.** With the material coordinates $ict\,e_0 + \mathbf{x}$, the divergence theorem is the statement that the flux of a four-current through the boundary of a region equals the integral of its divergence inside. Setting the divergence to zero — which is what a field equation does — makes a quantity conserved, and this is the mechanism behind the continuity equation and the conservation of electric charge in *Biquaternion Electromagnetism* and of the energy–momentum four-vector in *Biquaternion Relativity*. The biquaternion-valued normal is what makes the statement hold for a field whose components mix under the algebra's multiplication.

## Green's Formulas

### First Green's Formula

**Theorem (first Green's formula).** Let $\tilde{F}$ and $\tilde{G}$ be twice continuously differentiable biquaternion-valued functions on $\Omega$ with piecewise smooth boundary $\partial \Omega$, and let $\partial_{\tilde{n}} = \sum_\mu n_\mu \partial_{q_\mu}$ be the scalar normal derivative. Then

$$
\int_\Omega \left[ \sum_{\mu=0}^{3} \left(\frac{\partial \tilde{F}}{\partial q_\mu}\right) \overline{\left(\frac{\partial \tilde{G}}{\partial q_\mu}\right)} + \tilde{F}\, \overline{\Box \tilde{G}} \right] dV = \int_{\partial \Omega} \tilde{F}\, \overline{\partial_{\tilde{n}} \tilde{G}} \, dS.
$$

**Proof.** Apply the ordinary divergence theorem in $\mathbb{R}^4$ to the biquaternion-valued field with components $\tilde{F}\,\overline{\partial_\mu \tilde{G}}$: it gives $\int_\Omega \partial_\mu(\tilde{F}\,\overline{\partial_\mu \tilde{G}})\,dV = \int_{\partial\Omega} n_\mu \tilde{F}\,\overline{\partial_\mu \tilde{G}}\,dS$. The product rule expands the volume integrand as $(\partial_\mu\tilde{F})\,\overline{\partial_\mu \tilde{G}} + \tilde{F}\,\overline{\partial_\mu^2 \tilde{G}}$, the second term because $\partial_\mu$ is real and therefore commutes with the conjugation. Summing over $\mu$ replaces $\sum_\mu \partial_\mu^2$ by $\Box$ and $\sum_\mu n_\mu \partial_\mu$ by $\partial_{\tilde{n}}$.

### Second Green's Formula

**Theorem (second Green's formula).** Under the same hypotheses,

$$
\int_\Omega \left[ \tilde{F}\, \overline{\Box \tilde{G}} - (\Box \tilde{F})\, \bar{\tilde{G}} \right] dV = \int_{\partial \Omega} \left[ \tilde{F}\, \overline{\partial_{\tilde{n}} \tilde{G}} - (\partial_{\tilde{n}} \tilde{F})\, \bar{\tilde{G}} \right] dS.
$$

**Proof.** For each $\mu$ the product rule gives

$$
\partial_{q_\mu} \left[ \tilde{F}\, \overline{\partial_{q_\mu} \tilde{G}} - (\partial_{q_\mu} \tilde{F})\, \bar{\tilde{G}} \right] = \tilde{F}\, \overline{\partial_{q_\mu}^2 \tilde{G}} - (\partial_{q_\mu}^2 \tilde{F})\, \bar{\tilde{G}},
$$

the two mixed terms being the same product and cancelling. Summing over $\mu$ makes the left side the divergence of a biquaternion-valued field, whose volume integral is the stated volume integrand and whose boundary integral, by the ordinary divergence theorem and $\sum_\mu n_\mu \partial_{q_\mu} = \partial_{\tilde{n}}$, is the stated surface term. The conjugation is inert throughout because $\partial_{q_\mu}$ is real.

### Green's Formula for the d'Alembertian

**Theorem (Green's formula for $\Box$).** Let $\tilde{F}$ and $\tilde{G}$ be twice continuously differentiable biquaternion-valued functions on $\Omega$ with piecewise smooth boundary $\partial \Omega$, and let $\partial_{\tilde{n}} = \sum_{\mu=0}^{3} n_\mu \partial_{q_\mu}$ be the scalar normal derivative in the outward direction, $\tilde{n} = \sum_\mu n_\mu e_\mu$ being the normal fixed by the divergence theorem. Then

$$
\int_\Omega \left[ (\Box \tilde{F}) \tilde{G} - \tilde{F} (\Box \tilde{G}) \right] dV = \int_{\partial \Omega} \left[ (\partial_{\tilde{n}} \tilde{F}) \tilde{G} - \tilde{F} (\partial_{\tilde{n}} \tilde{G}) \right] dS,
$$

where $\Box = \partial^2/\partial q_0^2 + \Delta_q$ is the four-dimensional Laplacian in the coordinates $q_0, q_1, q_2, q_3$.

**Proof.** For each $\mu$ the product rule gives

$$
\partial_{q_\mu} \left[ (\partial_{q_\mu} \tilde{F}) \tilde{G} - \tilde{F} (\partial_{q_\mu} \tilde{G}) \right] = (\partial_{q_\mu}^2 \tilde{F}) \tilde{G} - \tilde{F} (\partial_{q_\mu}^2 \tilde{G}),
$$

the two mixed terms being the same product and cancelling. Summing over $\mu$ makes the left side a divergence whose volume integral is the stated volume integrand, $(\Box\tilde{F})\tilde{G} - \tilde{F}(\Box\tilde{G})$; the divergence theorem turns it into the boundary integral, which by $\sum_\mu n_\mu \partial_{q_\mu} = \partial_{\tilde{n}}$ is the stated surface term. The derivative in the surface term is essential and cannot be dropped: for scalar $u,v$ the classical identity the formula must reproduce, $\int_\Omega (v\Delta u - u\Delta v)\,dV = \int_{\partial\Omega} (v\partial_n u - u\partial_n v)\,dS$, has a non-zero right side.

**Remark (the two pairings).** This formula is the second Green formula with $\tilde{G}$ replaced by $\bar{\tilde{G}}$, up to the sign of both sides; the second Green formula carries the conjugation in the pairing, this one in the plain product, and the two have the same content.

**Physical reading: reciprocity.** Green's formulas are the reciprocity relations between two fields: exchanging the two solutions of the wave equation and subtracting gives a boundary identity, which is the statement that the second-order operator is self-adjoint in the appropriate sense. In the field-theoretic reading they are the algebraic origin of the reciprocity theorems used to compute potentials from boundary data, and they are what makes a Green's function method possible at all.

## The Fundamental Solution

### Definition

The **fundamental solution** of the gradient operator $\tilde{\nabla}$ on $\mathbb{H}_{\mathbb{B}}$ is the biquaternion-valued function

$$
\tilde{G}(\tilde{Q}) = \frac{\bar{\tilde{Q}}}{\|\tilde{Q}\|_E^4},
$$

where $\bar{\tilde{Q}}$ is the quaternion conjugate of $\tilde{Q}$ and $\|\tilde{Q}\|_E^4 = (\|\tilde{Q}\|_E^2)^2$ is the fourth power of the Euclidean norm.

The function $\tilde{G}$ is defined for $\tilde{Q} \neq 0$ in $\mathbb{H}_{\mathbb{B}}$. It is homogeneous of degree $-3$: $\tilde{G}(\lambda \tilde{Q}) = \lambda^{-3} \tilde{G}(\tilde{Q})$ for $\lambda > 0$.

### The Gradient of the Fundamental Solution

**Theorem (on $\mathbb{H}_{\mathbb{B}}$).** For $\tilde{Q} \in \mathbb{H}_{\mathbb{B}}$ with $\tilde{Q} \neq 0$,

$$
\tilde{\nabla} \tilde{G}(\tilde{Q}) = 0.
$$

**Proof.** Write $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ with $\|\tilde{Q}\|_E^2 = \sum_\mu Q_\mu^2$ (all $Q_\mu$ are real, since $\tilde{Q} \in \mathbb{H}_{\mathbb{B}}$). The quaternion conjugate is $\bar{\tilde{Q}} = Q_0 e_0 - \sum_k Q_k e_k$. So

$$
\tilde{G}(\tilde{Q}) = \frac{Q_0 e_0 - \sum_k Q_k e_k}{(\sum_\mu Q_\mu^2)^2}.
$$

A direct computation gives

$$
\tilde{\nabla} \tilde{G} = \sum_\mu e_\mu \frac{\partial}{\partial q_\mu} \left( \frac{\bar{\tilde{Q}}}{\|\tilde{Q}\|_E^4} \right) = \frac{\tilde{\nabla} \bar{\tilde{Q}}}{\|\tilde{Q}\|_E^4} + \bar{\tilde{Q}} \tilde{\nabla} \left( \frac{1}{\|\tilde{Q}\|_E^4} \right),
$$

using the product rule and the fact that $\bar{\tilde{Q}}$ and the scalar function $1/\|\tilde{Q}\|_E^4$ commute with the partial derivatives.

The first term is $\tilde{\nabla}\bar{\tilde{Q}} = \sum_\mu e_\mu \bar e_\mu = e_0 - e_1^2 - e_2^2 - e_3^2 = 4 e_0$, since $\partial_{q_\mu}\bar{\tilde{Q}} = \bar e_\mu$ holds because the coefficients $Q_\mu$ are real.

For the second term, on $\mathbb{H}_{\mathbb{B}}$ the coefficients are real, so $\partial_{q_\mu}\|\tilde Q\|_E^2 = 2Q_\mu$. Hence

$$
\partial_{q_\mu}\left(\frac{1}{\|\tilde Q\|_E^4}\right) = -\frac{2}{\|\tilde Q\|_E^6} \partial_{q_\mu}\|\tilde Q\|_E^2 = -\frac{4 Q_\mu}{\|\tilde Q\|_E^6}.
$$

Therefore

$$
\tilde{\nabla}\left(\frac{1}{\|\tilde Q\|_E^4}\right) = \sum_\mu e_\mu \left(-\frac{4 Q_\mu}{\|\tilde Q\|_E^6}\right) = -\frac{4\tilde Q}{\|\tilde Q\|_E^6}.
$$

Multiplying by $\bar{\tilde Q}$ on the left:

$$
\bar{\tilde Q} \tilde{\nabla}\left(\frac{1}{\|\tilde Q\|_E^4}\right) = -\frac{4\bar{\tilde Q}\tilde Q}{\|\tilde Q\|_E^6}.
$$

On $\mathbb{H}_{\mathbb{B}}$, $\bar{\tilde Q}\tilde Q = \sum_\mu Q_\mu^2 e_0 = \|\tilde Q\|_E^2 e_0$. So this term is $-4\|\tilde Q\|_E^2 e_0/\|\tilde Q\|_E^6 = -4e_0/\|\tilde Q\|_E^4$. Combining both terms:

$$
\tilde\nabla\tilde G = \frac{4e_0}{\|\tilde Q\|_E^4} - \frac{4e_0}{\|\tilde Q\|_E^4} = 0.
$$

### The Distributional Gradient

**Theorem.** In the sense of distributions on $\mathbb{H}_{\mathbb{B}}$,

$$
\tilde{\nabla} \tilde{G} = -2\pi^2 \delta_0 e_0,
$$

where $\delta_0$ is the delta distribution at the origin and $2\pi^2$ is the surface area of the unit three-sphere in $\mathbb{R}^4$.

**Proof.** The function $\tilde{G}$ is locally integrable and smooth away from the origin. For a test function $\phi$ with compact support, the pairing $\langle \tilde{\nabla} \tilde{G}, \phi \rangle$ is defined by integration by parts:

$$
\langle \tilde{\nabla} \tilde{G}, \phi \rangle = -\int_{\mathbb{R}^4} \tilde{G} (\tilde{\nabla} \phi) \, dV = -\lim_{\varepsilon \to 0} \int_{\|\tilde{Q}\|_E > \varepsilon} \tilde{G} (\tilde{\nabla} \phi) \, dV.
$$

Applying the divergence theorem to the domain $\|\tilde{Q}\|_E > \varepsilon$ and using $\tilde{\nabla} \tilde{G} = 0$ away from the origin gives

$$
\int_{\|\tilde{Q}\|_E > \varepsilon} \tilde{G} (\tilde{\nabla} \phi) \, dV = \int_{\|\tilde{Q}\|_E = \varepsilon} \tilde{G} \tilde{n} \phi \, dS - \int_{\|\tilde{Q}\|_E > \varepsilon} (\tilde{\nabla} \tilde{G}) \phi \, dV = \int_{\|\tilde{Q}\|_E = \varepsilon} \tilde{G} \tilde{n} \phi \, dS.
$$

On the sphere $\|\tilde{Q}\|_E = \varepsilon$, the outward unit normal is $\tilde{n} = \tilde{Q}/\varepsilon$, and $\tilde{G} = \bar{\tilde{Q}}/\varepsilon^4$. So

$$
\tilde{G} \tilde{n} = \frac{\bar{\tilde{Q}}}{\varepsilon^4} \cdot \frac{\tilde{Q}}{\varepsilon} = \frac{\|\tilde{Q}\|_E^2}{\varepsilon^5} e_0 = \frac{1}{\varepsilon^3} e_0,
$$

and

$$
\int_{\|\tilde{Q}\|_E = \varepsilon} \tilde{G} \tilde{n} \phi \, dS = \frac{1}{\varepsilon^3} \int_{\|\tilde{Q}\|_E = \varepsilon} \phi \, dS \cdot e_0.
$$

As $\varepsilon \to 0$ the average of $\phi$ over the sphere tends to $\phi(0)$, and the surface area is $2\pi^2\varepsilon^3$, so the limit is $2\pi^2\phi(0)e_0$. Hence $\langle\tilde{\nabla}\tilde{G},\phi\rangle = -2\pi^2\phi(0)e_0$, which is the stated distributional identity.

## The Cauchy Integral Formula

### Statement

**Theorem (Cauchy integral formula).** Let $\tilde{F}$ be a continuously differentiable biquaternion-valued function on a domain $\Omega \subset \mathbb{H}_{\mathbb{B}}$ with piecewise smooth boundary $\partial \Omega$, and let $\tilde{Q}_0$ be an interior point of $\Omega$. Then

$$
\tilde{F}(\tilde{Q}_0) = \frac{1}{2\pi^2} \int_{\partial \Omega} \tilde{G}(\tilde{Q} - \tilde{Q}_0) \tilde{n} \tilde{F}(\tilde{Q}) \, dS(\tilde{Q}) - \frac{1}{2\pi^2} \int_\Omega \tilde{G}(\tilde{Q} - \tilde{Q}_0) (\tilde{\nabla}\tilde{F})(\tilde{Q}) \, dV(\tilde{Q}),
$$

where $\tilde{G}$ is the fundamental solution defined above, $\tilde{n}$ is the biquaternion-valued outward unit normal, and $dS$ is the surface measure.

### The Regular Case

**Theorem (Cauchy integral formula for regular functions).** If $\tilde{F}$ satisfies $\tilde{\nabla}\tilde{F} = 0$ on $\Omega$ (the biquaternion analogue of the Cauchy–Riemann equations), then

$$
\tilde{F}(\tilde{Q}_0) = \frac{1}{2\pi^2} \int_{\partial \Omega} \tilde{G}(\tilde{Q} - \tilde{Q}_0) \tilde{n} \tilde{F}(\tilde{Q}) \, dS(\tilde{Q}).
$$

### Proof of the Cauchy Integral Formula

Apply the divergence theorem to the product $\tilde{G}(\tilde{Q} - \tilde{Q}_0) \tilde{F}(\tilde{Q})$ on the domain $\Omega_\varepsilon = \Omega \setminus B(\tilde{Q}_0, \varepsilon)$, where $B(\tilde{Q}_0, \varepsilon)$ is the ball of radius $\varepsilon$ centred at $\tilde{Q}_0$. The boundary of $\Omega_\varepsilon$ consists of $\partial \Omega$ and the sphere $\partial B(\tilde{Q}_0, \varepsilon)$. By the divergence theorem,

$$
\int_{\Omega_\varepsilon} \tilde{\nabla} \left( \tilde{G}(\tilde{Q} - \tilde{Q}_0) \tilde{F}(\tilde{Q}) \right) dV = \int_{\partial \Omega} \tilde{G}(\tilde{Q} - \tilde{Q}_0) \tilde{n} \tilde{F}(\tilde{Q}) \, dS + \int_{\partial B(\tilde{Q}_0, \varepsilon)} \tilde{G}(\tilde{Q} - \tilde{Q}_0) \tilde{n} \tilde{F}(\tilde{Q}) \, dS.
$$

On the small sphere, $\tilde{n} = -(\tilde{Q} - \tilde{Q}_0)/\varepsilon$ (pointing inward toward $\tilde{Q}_0$), and the computation of the boundary term gives

$$
\int_{\partial B(\tilde{Q}_0, \varepsilon)} \tilde{G}(\tilde{Q} - \tilde{Q}_0) \tilde{n} \tilde{F}(\tilde{Q}) \, dS \to -2\pi^2 \tilde{F}(\tilde{Q}_0) \quad \text{as } \varepsilon \to 0.
$$

The volume integral on the left is

$$
\int_{\Omega_\varepsilon} \tilde{\nabla} \left( \tilde{G}(\tilde{Q} - \tilde{Q}_0) \tilde{F}(\tilde{Q}) \right) dV = \int_{\Omega_\varepsilon} \tilde{G}(\tilde{Q} - \tilde{Q}_0) (\tilde{\nabla}\tilde{F})(\tilde{Q}) \, dV,
$$

using the product rule and the fact that $\tilde{\nabla}\tilde{G} = 0$ away from $\tilde{Q}_0$. Combining and taking the limit $\varepsilon \to 0$,

$$
\int_\Omega \tilde{G}(\tilde{Q} - \tilde{Q}_0) (\tilde{\nabla}\tilde{F})(\tilde{Q}) \, dV = \int_{\partial \Omega} \tilde{G}(\tilde{Q} - \tilde{Q}_0) \tilde{n} \tilde{F}(\tilde{Q}) \, dS - 2\pi^2 \tilde{F}(\tilde{Q}_0).
$$

Rearranging gives the stated formula.

**Physical reading: a field from its boundary values.** The fundamental solution is the Green's function of the d'Alembertian, and the Cauchy formula is the statement that a field inside a region is determined by its values on the boundary together with the source term. This is the algebraic origin of the boundary-value method: the interior field of a source-free solution is a boundary integral, which is why a free field can be described by its boundary or initial data alone. The formula holds on $\mathbb{H}_{\mathbb{B}}$ and is not asserted on the material or informational slices, where the operator is hyperbolic and the boundary data must be characteristic data instead — the point developed in *Biquaternion Regular Functions* and *Biquaternion Analysis on Subspaces*.

## Consequences of the Cauchy Integral Formula

### The Mean Value Property

**Theorem (mean value property).** If $\tilde{F}$ satisfies $\tilde{\nabla}\tilde{F} = 0$ on a ball $B(\tilde{Q}_0, r)$, then

$$
\tilde{F}(\tilde{Q}_0) = \frac{1}{2\pi^2 r^3} \int_{\partial B(\tilde{Q}_0, r)} \tilde{F}(\tilde{Q}) \, dS(\tilde{Q}),
$$

where $2\pi^2 r^3$ is the surface area of the three-sphere of radius $r$ in $\mathbb{R}^4$.

**Proof.** Apply the Cauchy integral formula to the ball $B(\tilde{Q}_0, r)$ and use the explicit form of the fundamental solution. The kernel becomes constant on the sphere, and the integral reduces to the average of $\tilde{F}$ over the sphere.

### The Maximum Principle

**Theorem (maximum principle).** If $\tilde{F}$ satisfies $\tilde{\nabla}\tilde{F} = 0$ on a domain $\Omega$ and $\|\tilde{F}\|_E$ attains its maximum at an interior point of $\Omega$, then $\tilde{F}$ is constant on $\Omega$.

**Proof.** Use the mean value property: if $\|\tilde{F}\|_E$ attains its maximum at $\tilde{Q}_0$, then the mean value over a small sphere around $\tilde{Q}_0$ equals $\tilde{F}(\tilde{Q}_0)$, which is only possible if $\tilde{F}$ is constant on the sphere. Iterating over a connected chain of spheres, $\tilde{F}$ is constant on $\Omega$.

### Liouville's Theorem

**Theorem (Liouville).** If $\tilde{F}$ satisfies $\tilde{\nabla}\tilde{F} = 0$ on all of $\mathbb{H}_{\mathbb{B}}$ and $\|\tilde{F}\|_E$ is bounded, then $\tilde{F}$ is constant.

**Proof.** Apply the Cauchy integral formula to a large ball of radius $R$ centred at $\tilde{Q}_0$, and estimate the boundary integral using the boundedness of $\tilde{F}$. The kernel $\tilde{G}(\tilde{Q} - \tilde{Q}_0)$ is of order $R^{-3}$ on the sphere of radius $R$, and the surface area is of order $R^3$, so the boundary integral is of order $R^0$, i.e. bounded. As $R \to \infty$, the boundary integral tends to zero, so $\tilde{F}(\tilde{Q}_0)$ is independent of $\tilde{Q}_0$.

### The Identity Theorem

**Theorem (identity theorem).** If two functions $\tilde{F}$ and $\tilde{G}$ satisfying $\tilde{\nabla}\tilde{F} = \tilde{\nabla}\tilde{G} = 0$ on a connected domain $\Omega$ agree on an open subset of $\Omega$, then they agree on all of $\Omega$.

**Proof.** The difference $\tilde{H} = \tilde{F} - \tilde{G}$ satisfies $\tilde{\nabla}\tilde{H} = 0$ and vanishes on an open subset. By the maximum principle applied to $\tilde{H}$ and to $-\tilde{H}$, the modulus of $\tilde{H}$ cannot attain a maximum at an interior point unless $\tilde{H}$ is constant, and since $\tilde{H}$ vanishes on an open subset, the constant is zero.

### The Cauchy Estimates

**Theorem (Cauchy estimates).** If $\tilde{F}$ satisfies $\tilde{\nabla}\tilde{F} = 0$ on a ball $B(\tilde{Q}_0, R)$ and $\|\tilde{F}\|_E \leq M$ on the boundary, then for every multi-index $\alpha$,

$$
\left\|\frac{\partial^{|\alpha|} \tilde{F}}{\partial q^\alpha}(\tilde{Q}_0)\right\|_E \leq \frac{C_\alpha M}{R^{|\alpha|}},
$$

where $C_\alpha$ is a constant depending on $\alpha$ and $|\alpha|$ is the total order of the multi-index.

**Proof.** Differentiate the Cauchy integral formula with respect to $\tilde{Q}_0$ and estimate the resulting integral using the bound on $\tilde{F}$.

**Physical reading.** The mean value property and the maximum principle are the analytic statement that a source-free field has no isolated peaks: its value at a point is the average over any surrounding sphere, so a maximum in the interior is impossible unless the field is constant. In the field-theoretic reading this is the reason a static source-free configuration cannot be localised, and it is the analytic counterpart of the statement that a massless field is spread out. Liouville's theorem says that a bounded regular field on the whole space is constant, which is the algebraic statement that there is no localised massless mode in the theory on $\mathbb{H}_{\mathbb{B}}$.

## The Residue Theory

### The Residue

The Cauchy integral formula for a function that is regular except at isolated singularities leads to a residue theory. However, the non-commutativity of $\mathbb{B}$ makes the definition of the residue more delicate than in the complex case.

**Definition (isolated singularity).** A point $\tilde{Q}_0$ is an **isolated singularity** of $\tilde{F}$ if $\tilde{F}$ is defined and regular on a punctured neighbourhood $0 < \|\tilde{Q} - \tilde{Q}_0\|_E < r$ of $\tilde{Q}_0$.

**Definition (residue).** The **residue** of $\tilde{F}$ at an isolated singularity $\tilde{Q}_0$ is the biquaternion

$$
\mathrm{Res}(\tilde{F}, \tilde{Q}_0) = \frac{1}{2\pi^2} \int_{\partial B(\tilde{Q}_0, \varepsilon)} \tilde{G}(\tilde{Q} - \tilde{Q}_0) \tilde{n} \tilde{F}(\tilde{Q}) \, dS(\tilde{Q}),
$$

where $\varepsilon$ is small enough that the sphere does not enclose any other singularity.

### The Residue Theorem

**Theorem (residue theorem).** Let $\tilde{F}$ be regular on a domain $\Omega$ except at isolated singularities $\tilde{Q}_1, \dots, \tilde{Q}_n$. Then

$$
\frac{1}{2\pi^2} \int_{\partial \Omega} \tilde{G}(\tilde{Q} - \tilde{Q}_0) \tilde{n} \tilde{F}(\tilde{Q}) \, dS(\tilde{Q}) = \sum_{k=1}^{n} \mathrm{Res}(\tilde{F}, \tilde{Q}_k)
$$

for any $\tilde{Q}_0$ outside the singularities.

**Proof.** Apply the Cauchy integral formula to the domain with small spheres removed around each singularity, and use the definition of the residue.

## The Relation to Complex and Quaternionic Analysis

The integration theory developed here is the biquaternion analogue of the Cauchy integral theory in complex analysis and of the Fueter theory in quaternionic analysis.

**Complex analysis.** In complex analysis, the Cauchy integral formula expresses the value of a holomorphic function at an interior point in terms of its boundary values, with the kernel $1/(z - z_0)$. The biquaternion analogue uses the kernel $\tilde{G}(\tilde{Q} - \tilde{Q}_0) = (\bar{\tilde{Q}} - \bar{\tilde{Q}}_0)/\|\tilde{Q} - \tilde{Q}_0\|_E^4$, which is the fundamental solution of the gradient operator in four dimensions.

**Quaternionic analysis.** In Fueter's quaternionic analysis, the analogue of the Cauchy integral formula involves the kernel $q^{-1}/\|q\|^2$ and the quaternion-valued integration over the boundary of a domain in $\mathbb{R}^4$. The biquaternion case is the generalisation to complex coefficients, with the additional structure of the four conjugations.

**Clifford analysis.** The general Clifford analysis on $\mathbb{R}^n$ uses the kernel $x^{-1}/\|x\|^{n-2}$, equivalently $\bar{x}/\|x\|^n$ (homogeneous of degree $1 - n$), and the Clifford algebra-valued integration. The biquaternion case is the case $n = 4$ of this general theory, with the specific structure of the even subalgebra of $\mathrm{Cl}_{1,3}$.

## Open Questions

The following questions are not answered in this article and are left for later work:

1. **The extension to $\mathbb{M}_+$ and $\mathbb{M}_-$.** The integration theory presented here is for functions on the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, where the four coordinates are real. Extending the theory to the indefinite subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$ requires modifying the fundamental solution, because the kernel $\bar{\tilde Q}/\|\tilde Q\|_E^4$ is not annihilated by the framework's gradient on these subspaces. Indeed, on $\mathbb{M}_+$ and $\mathbb{M}_-$, the coefficients $Q_\mu$ include imaginary entries, and the identity $\bar{\tilde Q}\tilde Q = \|\tilde Q\|_E^2 e_0$ fails, so the proof of $\tilde\nabla\tilde G = 0$ does not carry over. Whether a modified kernel exists, and how it relates to the standard Clifford analysis of $\mathbb{R}^{3,1}$ or $\mathbb{R}^{1,3}$, is open.

2. **The residue theory in the non-commutative case.** The definition of the residue given above is one of several possible definitions. What is the correct definition that makes the residue theorem hold in the strongest form?

3. **The Cauchy integral formula for other domains.** What is the form of the Cauchy integral formula for domains with non-smooth boundaries, or for domains that are not simply connected?

4. **Applications.** What are the applications of the biquaternion integration theory to the solution of partial differential equations?

5. **The general subspace.** Can the integration theory be extended from $\mathbb{H}_{\mathbb{B}}$ to the full biquaternion algebra $\mathbb{B}$ and to its indefinite subspaces, with a canonical choice of fundamental solution for each?

**Physical form of the open problems.** The first question is the physical one of a propagator on a curved or indefinite background: on the material slice the Green's function of the wave operator is the light-cone-supported object of *Biquaternion Analysis on Subspaces* and *The Wave Equation on $\mathbb{M}_-$*, not the Euclidean kernel, and its existence is what the freedom of choosing a modified kernel encodes. The second and third are the questions of how much of the complex-analytic technology survives in the non-commutative and non-elliptic settings.

## Summary

The integral of a biquaternion-valued function on the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ is defined component-wise with respect to the Lebesgue measure. It is linear, additive and satisfies the fundamental estimate. The standard theorems of integration carry over: integration by parts, the divergence theorem, and Green's formulas. Because the algebra is not commutative, transposing the gradient off a product requires the right gradient $\overleftarrow{\nabla}$, and the identities are stated in the forms that hold for general biquaternion-valued fields.

The **fundamental solution** of the gradient operator on $\mathbb{H}_{\mathbb{B}}$ is $\tilde{G}(\tilde{Q}) = \bar{\tilde{Q}}/\|\tilde{Q}\|_E^4$, which satisfies $\tilde{\nabla} \tilde{G} = 0$ away from the origin and $\tilde{\nabla} \tilde{G} = -2\pi^2 \delta_0 e_0$ in the sense of distributions.

The **Cauchy integral formula** expresses the value of a continuously differentiable function at an interior point in terms of its boundary values and the volume integral of its gradient. For functions satisfying $\tilde{\nabla}\tilde{F} = 0$ (the biquaternion analogue of the Cauchy–Riemann equations), the volume integral vanishes and the value at the interior point is given entirely by the boundary values.

The Cauchy integral formula implies the **mean value property**, the **maximum principle**, **Liouville's theorem**, the **identity theorem** and the **Cauchy estimates**. These are the biquaternion analogues of the standard consequences of the Cauchy integral formula in complex analysis.

The **residue theory** for biquaternion-valued functions is more delicate than in the complex case, because of the non-commutativity of the algebra. The residue at an isolated singularity is defined as a boundary integral, and the residue theorem expresses the integral over the boundary of a domain in terms of the residues at the singularities inside.

Physically the divergence theorem is the conservation of a four-current, the fundamental solution is the Green's function of the d'Alembertian, and the Cauchy formula is the representation of a field by its boundary values; the theory is developed on $\mathbb{H}_{\mathbb{B}}$ and extended to the indefinite subspaces only off the null cone, the light cone of the material sector. The integration theory is related to complex analysis, Fueter's quaternionic analysis, and general Clifford analysis; the biquaternion case on $\mathbb{H}_{\mathbb{B}}$ is the case $n = 4$ with complex coefficients, enriched by the four conjugations and the two polar forms.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion subspace (real coordinates $q_0, q_1, q_2, q_3$) |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | Point in $\mathbb{H}_{\mathbb{B}}$ (all $Q_\mu$ real) |
| $\partial/\partial q_\mu$ | Ordinary real partial derivative |
| $\tilde{\nabla} = \sum_\mu e_\mu \partial/\partial q_\mu$ | Biquaternionic gradient (Cauchy–Riemann operator) |
| $\tilde{F}\overleftarrow{\nabla} = \sum_\mu (\partial \tilde{F}/\partial q_\mu) e_\mu$ | Right gradient of $\tilde{F}$ |
| $\bar{\tilde{\nabla}}$ | Quaternion conjugate of the gradient |
| $\Box = \partial^2/\partial q_0^2 + \Delta_q$ | d'Alembertian, the wave operator on the material slice |
| $\tilde{n}$ | Biquaternion-valued outward unit normal |
| $\partial_{\tilde{n}} = \sum_\mu n_\mu \partial_{q_\mu}$ | Scalar normal derivative in the outward direction |
| $\tilde{G}(\tilde{Q}) = \bar{\tilde{Q}}/\|\tilde{Q}\|_E^4$ | Fundamental solution of the gradient; the Green's function |
| $dV$ | Lebesgue measure on the four real coordinates of $\mathbb{H}_{\mathbb{B}}$ |

## Further Reading

- R. Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta\Delta u = 0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* **7** (1934–35) 307–330, for the analysis of quaternion-valued functions of four real variables.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the connection to Clifford algebras.
- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis.
- John Ryan, *Clifford Algebras in Analysis and Related Topics* (CRC Press, 1996), for the analytic theory of Clifford algebras.
- A. Sudbery, "Quaternionic analysis", *Mathematical Proceedings of the Cambridge Philosophical Society* **85** (1979) 199–225, for the quaternionic analogue of the Cauchy integral formula.
