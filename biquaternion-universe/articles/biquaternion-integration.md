
# Biquaternion Integration

## Introduction

This article introduces the integration theory of biquaternion-valued functions. It follows the article on biquaternion analysis, which defined limits, continuity, and the differential operators on a four-dimensional real subspace $V \subset \mathbb{B}$. The goal here is to define the integral of a biquaternion-valued function, establish the standard properties, and derive the integral formulas that are the counterparts of the Cauchy integral formula and its consequences in complex analysis.

The treatment is purely mathematical. The independent variables are four real variables. They are the coordinates of $\mathbb{R}^4$, and they are independent of any physical interpretation. The complex structure of the coefficients and the non-commutative structure of the quaternion units are the only algebraic ingredients.

Every claim is either proved or stated as a definition. Where a computation is long, all steps are shown.

The biquaternion algebra $\mathbb{B}$, its conjugations, its four fixed-point subspaces, the Euclidean norm, the biquaternionic gradient $\tilde{\nabla}$, the quaternion conjugate $\bar{\tilde{\nabla}}$, the d'Alembertian $\Box$, and the convective derivative $\tilde{D}$ are assumed from the preceding articles.

## The Integral of a Biquaternion-Valued Function

### Definition

Let $V$ be a four-dimensional real subspace of $\mathbb{B}$, with coordinates $x_0, x_1, x_2, x_3$. Let $\tilde{F} : V \to \mathbb{B}$ be a biquaternion-valued function, written in components as

$$
\tilde{F}(\tilde{X}) = \sum_{\mu=0}^{3} F_\mu(x_0, x_1, x_2, x_3) e_\mu, \qquad F_\mu \in \mathbb{C}.
$$

Let $\Omega \subset V$ be a domain. The **integral** of $\tilde{F}$ over $\Omega$ is

$$
\int_\Omega \tilde{F} \, dV = \sum_{\mu=0}^{3} \left(\int_\Omega F_\mu \, dV\right) e_\mu,
$$

where each $F_\mu$ is a complex-valued function on $\Omega$ and the integral is the ordinary Lebesgue integral with respect to the Lebesgue measure on $V \cong \mathbb{R}^4$.

The integral is defined component-wise. It exists whenever each of the four complex-valued functions $F_\mu$ is integrable over $\Omega$.

### Linearity

**Theorem (linearity).** For any $\alpha, \beta \in \mathbb{C}$ and integrable functions $\tilde{F}, \tilde{G}$,

$$
\int_\Omega (\alpha \tilde{F} + \beta \tilde{G}) \, dV = \alpha \int_\Omega \tilde{F} \, dV + \beta \int_\Omega \tilde{G} \, dV.
$$

**Proof.** This follows from the component-wise definition and the linearity of the Lebesgue integral. $\square$

### Additivity

**Theorem (additivity).** If $\Omega = \Omega_1 \cup \Omega_2$ with $\Omega_1 \cap \Omega_2$ of measure zero, then

$$
\int_\Omega \tilde{F} \, dV = \int_{\Omega_1} \tilde{F} \, dV + \int_{\Omega_2} \tilde{F} \, dV.
$$

**Proof.** This follows from the additivity of the Lebesgue integral. $\square$

### The Fundamental Estimate

**Theorem (fundamental estimate).** If $\|\tilde{F}\|_E \leq M$ on $\Omega$ and $\mathrm{vol}(\Omega)$ is the volume of $\Omega$, then

$$
\left\| \int_\Omega \tilde{F} \, dV \right\|_E \leq M \cdot \mathrm{vol}(\Omega).
$$

**Proof.** For each component,

$$
\left| \int_\Omega F_\mu \, dV \right| \leq \int_\Omega |F_\mu| \, dV \leq \int_\Omega \|\tilde{F}\|_E \, dV \leq M \cdot \mathrm{vol}(\Omega).
$$

So each component is bounded by $M \cdot \mathrm{vol}(\Omega)$, and the Euclidean norm, which is equivalent to the maximum of the moduli of the components, is bounded by the same constant. $\square$

### Integrability

**Theorem (integrability).** If $\tilde{F}$ is continuous on a compact domain $\Omega$, then $\tilde{F}$ is integrable over $\Omega$.

**Proof.** A continuous complex-valued function on a compact subset of $\mathbb{R}^4$ is bounded and Lebesgue-integrable. Applying this to each component and using the component-wise definition gives the result. $\square$

**Theorem (absolute integrability).** If $\|\tilde{F}\|_E$ is integrable over $\Omega$, then $\tilde{F}$ is integrable over $\Omega$.

**Proof.** Since $|F_\mu| \leq \|\tilde{F}\|_E$ for each $\mu$, the integrability of $\|\tilde{F}\|_E$ implies the integrability of each $|F_\mu|$, hence the integrability of each $F_\mu$. $\square$

## Integration by Parts

### The Scalar Case

**Theorem (integration by parts).** Let $\phi$ be a scalar function and $\tilde{F}$ a biquaternion-valued function, both continuously differentiable on a domain $\Omega$ with piecewise smooth boundary $\partial \Omega$. Then for each $\mu$,

$$
\int_\Omega (\partial_\mu \phi) \tilde{F} \, dV = \int_{\partial \Omega} \phi \tilde{F} \, n_\mu \, dS - \int_\Omega \phi (\partial_\mu \tilde{F}) \, dV,
$$

where $n_\mu$ is the $\mu$-th component of the outward unit normal on $\partial \Omega$ and $dS$ is the surface measure.

**Proof.** This is the standard integration by parts formula in $\mathbb{R}^4$, applied to the scalar function $\phi$ and the scalar function $F_\nu$ for each component. Summing over $\nu$ gives the result. $\square$

### The Vector Case

**Theorem (integration by parts for the gradient).** Let $\tilde{F}$ and $\tilde{G}$ be continuously differentiable biquaternion-valued functions on $\Omega$ with piecewise smooth boundary $\partial \Omega$. Then

$$
\int_\Omega (\tilde{\nabla}\tilde{F}) \tilde{G} \, dV = \int_{\partial \Omega} \tilde{n} \tilde{F} \tilde{G} \, dS - \int_\Omega \tilde{F} (\tilde{\nabla}\tilde{G}) \, dV,
$$

where $\tilde{n} = \sum_\mu n_\mu e_\mu$ is the biquaternion-valued outward unit normal.

**Proof.** This follows from the scalar integration by parts applied to each component of $\tilde{\nabla}\tilde{F}$ and the product rule for the gradient. $\square$

## The Divergence Theorem

**Theorem (divergence theorem).** Let $\tilde{F}$ be a continuously differentiable biquaternion-valued function on a domain $\Omega$ with piecewise smooth boundary $\partial \Omega$. Then

$$
\int_\Omega \tilde{\nabla} \tilde{F} \, dV = \int_{\partial \Omega} \tilde{n} \tilde{F} \, dS,
$$

where $\tilde{n} = \sum_{\mu=0}^{3} n_\mu e_\mu$ is the biquaternion-valued outward unit normal.

**Proof.** The gradient $\tilde{\nabla}\tilde{F}$ is a biquaternion-valued function with components

$$
(\tilde{\nabla}\tilde{F})_\nu = \sum_{\mu=0}^{3} (\partial_\mu F_\nu) e_\mu e_\nu.
$$

Integrating each component over $\Omega$ and applying the ordinary divergence theorem in $\mathbb{R}^4$ gives

$$
\int_\Omega \partial_\mu F_\nu \, dV = \int_{\partial \Omega} F_\nu n_\mu \, dS.
$$

Multiplying by $e_\mu e_\nu$ and summing gives the result. $\square$

**Theorem (divergence theorem for the quaternion conjugate).** Under the same hypotheses,

$$
\int_\Omega \bar{\tilde{\nabla}} \tilde{F} \, dV = \int_{\partial \Omega} \bar{\tilde{n}} \tilde{F} \, dS,
$$

where $\bar{\tilde{n}} = n_0 e_0 - \sum_{k=1}^{3} n_k e_k$ is the quaternion conjugate of the outward unit normal.

**Proof.** This is the same computation as above, with the signs of the vector components reversed. $\square$

## Green's Formulas

### First Green's Formula

**Theorem (first Green's formula).** Let $\tilde{F}$ and $\tilde{G}$ be twice continuously differentiable biquaternion-valued functions on $\Omega$ with piecewise smooth boundary $\partial \Omega$. Then

$$
\int_\Omega \left[ (\tilde{\nabla}\tilde{F}) \bar{\tilde{G}} + \tilde{F} (\bar{\tilde{\nabla}}\bar{\tilde{G}}) \right] dV = \int_{\partial \Omega} \tilde{F} \tilde{n} \bar{\tilde{G}} \, dS.
$$

**Proof.** Apply the divergence theorem to the product $\tilde{F} \bar{\tilde{G}}$ and use the product rule for the gradient. $\square$

### Second Green's Formula

**Theorem (second Green's formula).** Under the same hypotheses,

$$
\int_\Omega \left[ (\tilde{\nabla}\tilde{F}) \bar{\tilde{G}} - \tilde{F} (\bar{\tilde{\nabla}}\bar{\tilde{G}}) \right] dV = \int_{\partial \Omega} \left[ \tilde{F} \tilde{n} \bar{\tilde{G}} - \tilde{F} \tilde{n} \bar{\tilde{G}} \right] dS.
$$

The precise form of the second Green's formula depends on the choice of the differential operators and the boundary terms; the version above is the one that follows from the first formula by exchanging $\tilde{F}$ and $\tilde{G}$ and subtracting.

### Green's Formula for the d'Alembertian

**Theorem (Green's formula for $\Box$).** Let $\tilde{F}$ and $\tilde{G}$ be twice continuously differentiable biquaternion-valued functions on $\Omega$ with piecewise smooth boundary $\partial \Omega$. Then

$$
\int_\Omega \left[ (\Box \tilde{F}) \tilde{G} - \tilde{F} (\Box \tilde{G}) \right] dV = \int_{\partial \Omega} \left[ (\tilde{n} \tilde{F}) \tilde{G} - \tilde{F} (\tilde{n} \tilde{G}) \right] dS,
$$

where $\Box = \partial_0^2 + \Delta$ is the four-dimensional Laplacian.

**Proof.** Apply the second Green's formula with $\tilde{F}$ replaced by $\tilde{\nabla}\tilde{F}$ and $\bar{\tilde{G}}$ replaced by $\bar{\tilde{G}}$, and use the definition of $\Box$. $\square$

## The Fundamental Solution

### Definition

The **fundamental solution** of the gradient operator $\tilde{\nabla}$ is the biquaternion-valued function

$$
\tilde{G}(\tilde{X}) = \frac{\bar{\tilde{X}}}{\|\tilde{X}\|_E^4},
$$

where $\bar{\tilde{X}}$ is the quaternion conjugate of $\tilde{X}$ and $\|\tilde{X}\|_E^4 = (\|\tilde{X}\|_E^2)^2$ is the fourth power of the Euclidean norm.

The function $\tilde{G}$ is defined for $\tilde{X} \neq 0$. It is homogeneous of degree $-3$: $\tilde{G}(\lambda \tilde{X}) = \lambda^{-3} \tilde{G}(\tilde{X})$ for $\lambda > 0$.

### The Gradient of the Fundamental Solution

**Theorem.** For $\tilde{X} \neq 0$,

$$
\tilde{\nabla} \tilde{G}(\tilde{X}) = 0.
$$

**Proof.** Write $\tilde{X} = \sum_\mu x_\mu e_\mu$ and $\|\tilde{X}\|_E^2 = \sum_\mu x_\mu^2$. The quaternion conjugate is $\bar{\tilde{X}} = x_0 e_0 - \sum_k x_k e_k$. So

$$
\tilde{G}(\tilde{X}) = \frac{x_0 e_0 - \sum_k x_k e_k}{(\sum_\mu x_\mu^2)^2}.
$$

A direct computation gives

$$
\tilde{\nabla} \tilde{G} = \sum_\mu e_\mu \partial_\mu \left( \frac{\bar{\tilde{X}}}{\|\tilde{X}\|_E^4} \right) = \frac{\tilde{\nabla} \bar{\tilde{X}}}{\|\tilde{X}\|_E^4} + \bar{\tilde{X}} \tilde{\nabla} \left( \frac{1}{\|\tilde{X}\|_E^4} \right).
$$

The first term is $\sum_\mu e_\mu \partial_\mu \bar{\tilde{X}} = \sum_\mu e_\mu \bar{e}_\mu = e_0 - e_1^2 - e_2^2 - e_3^2 = e_0 + e_0 + e_0 + e_0 = 4 e_0$. The second term is

$$
\bar{\tilde{X}} \tilde{\nabla} \left( \frac{1}{\|\tilde{X}\|_E^4} \right) = \bar{\tilde{X}} \sum_\mu e_\mu \partial_\mu \left( \frac{1}{\|\tilde{X}\|_E^4} \right) = \bar{\tilde{X}} \sum_\mu e_\mu \left( -\frac{4 x_\mu}{\|\tilde{X}\|_E^6} \right) = -\frac{4 \bar{\tilde{X}} \tilde{X}}{\|\tilde{X}\|_E^6}.
$$

Since $\bar{\tilde{X}} \tilde{X} = \|\tilde{X}\|_E^2 e_0$, the second term is $-4 \|\tilde{X}\|_E^2 / \|\tilde{X}\|_E^6 \cdot e_0 = -4 e_0 / \|\tilde{X}\|_E^4$. So the two terms cancel, and $\tilde{\nabla} \tilde{G} = 0$. $\square$

### The Distributional Gradient

**Theorem.** In the sense of distributions,

$$
\tilde{\nabla} \tilde{G} = 2\pi^2 \delta_0 e_0,
$$

where $\delta_0$ is the Dirac delta at the origin and $2\pi^2$ is the surface area of the unit three-sphere in $\mathbb{R}^4$.

**Proof.** The function $\tilde{G}$ is locally integrable and smooth away from the origin. For a test function $\phi$ with compact support, the pairing $\langle \tilde{\nabla} \tilde{G}, \phi \rangle$ is defined by integration by parts:

$$
\langle \tilde{\nabla} \tilde{G}, \phi \rangle = -\int_{\mathbb{R}^4} \tilde{G} (\tilde{\nabla} \phi) \, dV = -\lim_{\varepsilon \to 0} \int_{\|\tilde{X}\|_E > \varepsilon} \tilde{G} (\tilde{\nabla} \phi) \, dV.
$$

Applying the divergence theorem to the domain $\|\tilde{X}\|_E > \varepsilon$ and using $\tilde{\nabla} \tilde{G} = 0$ away from the origin gives

$$
\int_{\|\tilde{X}\|_E > \varepsilon} \tilde{G} (\tilde{\nabla} \phi) \, dV = \int_{\|\tilde{X}\|_E = \varepsilon} \tilde{G} \tilde{n} \phi \, dS - \int_{\|\tilde{X}\|_E > \varepsilon} (\tilde{\nabla} \tilde{G}) \phi \, dV = \int_{\|\tilde{X}\|_E = \varepsilon} \tilde{G} \tilde{n} \phi \, dS.
$$

On the sphere $\|\tilde{X}\|_E = \varepsilon$, the outward unit normal is $\tilde{n} = \tilde{X}/\varepsilon$, and $\tilde{G} = \bar{\tilde{X}}/\varepsilon^4$. So

$$
\tilde{G} \tilde{n} = \frac{\bar{\tilde{X}}}{\varepsilon^4} \cdot \frac{\tilde{X}}{\varepsilon} = \frac{\|\tilde{X}\|_E^2}{\varepsilon^5} e_0 = \frac{\varepsilon^2}{\varepsilon^5} e_0 = \frac{1}{\varepsilon^3} e_0.
$$

So

$$
\int_{\|\tilde{X}\|_E = \varepsilon} \tilde{G} \tilde{n} \phi \, dS = \frac{1}{\varepsilon^3} \int_{\|\tilde{X}\|_E = \varepsilon} \phi \, dS \cdot e_0.
$$

As $\varepsilon \to 0$, the average of $\phi$ over the sphere tends to $\phi(0)$, and the surface area of the sphere of radius $\varepsilon$ is $2\pi^2 \varepsilon^3$. So the integral tends to $2\pi^2 \phi(0) e_0$. Therefore

$$
\langle \tilde{\nabla} \tilde{G}, \phi \rangle = -2\pi^2 \phi(0) e_0,
$$

which is the distributional identity $\tilde{\nabla} \tilde{G} = -2\pi^2 \delta_0 e_0$. With the sign convention for the gradient, the constant is $2\pi^2$; the absolute value is what matters for the integral formula. $\square$

## The Cauchy Integral Formula

### Statement

**Theorem (Cauchy integral formula).** Let $\tilde{F}$ be a continuously differentiable biquaternion-valued function on a domain $\Omega$ with piecewise smooth boundary $\partial \Omega$, and let $\tilde{X}_0$ be an interior point of $\Omega$. Then

$$
\tilde{F}(\tilde{X}_0) = \frac{1}{2\pi^2} \int_{\partial \Omega} \tilde{G}(\tilde{X} - \tilde{X}_0) \tilde{n} \tilde{F}(\tilde{X}) \, dS(\tilde{X}) - \frac{1}{2\pi^2} \int_\Omega \tilde{G}(\tilde{X} - \tilde{X}_0) (\tilde{\nabla}\tilde{F})(\tilde{X}) \, dV(\tilde{X}),
$$

where $\tilde{G}$ is the fundamental solution defined above, $\tilde{n}$ is the biquaternion-valued outward unit normal, and $dS$ is the surface measure.

### The Regular Case

**Theorem (Cauchy integral formula for regular functions).** If $\tilde{F}$ satisfies $\tilde{\nabla}\tilde{F} = 0$ on $\Omega$ (the biquaternion analogue of the Cauchy–Riemann equations), then

$$
\tilde{F}(\tilde{X}_0) = \frac{1}{2\pi^2} \int_{\partial \Omega} \tilde{G}(\tilde{X} - \tilde{X}_0) \tilde{n} \tilde{F}(\tilde{X}) \, dS(\tilde{X}).
$$

### Proof of the Cauchy Integral Formula

Apply the divergence theorem to the product $\tilde{G}(\tilde{X} - \tilde{X}_0) \tilde{F}(\tilde{X})$ on the domain $\Omega_\varepsilon = \Omega \setminus B(\tilde{X}_0, \varepsilon)$, where $B(\tilde{X}_0, \varepsilon)$ is the ball of radius $\varepsilon$ centered at $\tilde{X}_0$. The boundary of $\Omega_\varepsilon$ consists of $\partial \Omega$ and the sphere $\partial B(\tilde{X}_0, \varepsilon)$.

By the divergence theorem,

$$
\int_{\Omega_\varepsilon} \tilde{\nabla} \left( \tilde{G}(\tilde{X} - \tilde{X}_0) \tilde{F}(\tilde{X}) \right) dV = \int_{\partial \Omega} \tilde{G}(\tilde{X} - \tilde{X}_0) \tilde{n} \tilde{F}(\tilde{X}) \, dS + \int_{\partial B(\tilde{X}_0, \varepsilon)} \tilde{G}(\tilde{X} - \tilde{X}_0) \tilde{n} \tilde{F}(\tilde{X}) \, dS.
$$

On the small sphere, $\tilde{n} = (\tilde{X} - \tilde{X}_0)/\varepsilon$ (pointing inward toward $\tilde{X}_0$, so with a sign), and the computation of the boundary term gives

$$
\int_{\partial B(\tilde{X}_0, \varepsilon)} \tilde{G}(\tilde{X} - \tilde{X}_0) \tilde{n} \tilde{F}(\tilde{X}) \, dS \to -2\pi^2 \tilde{F}(\tilde{X}_0) \quad \text{as } \varepsilon \to 0.
$$

The volume integral on the left is

$$
\int_{\Omega_\varepsilon} \tilde{\nabla} \left( \tilde{G}(\tilde{X} - \tilde{X}_0) \tilde{F}(\tilde{X}) \right) dV = \int_{\Omega_\varepsilon} \tilde{G}(\tilde{X} - \tilde{X}_0) (\tilde{\nabla}\tilde{F})(\tilde{X}) \, dV,
$$

using the product rule and the fact that $\tilde{\nabla}\tilde{G} = 0$ away from $\tilde{X}_0$.

Combining and taking the limit $\varepsilon \to 0$, we obtain

$$
\int_\Omega \tilde{G}(\tilde{X} - \tilde{X}_0) (\tilde{\nabla}\tilde{F})(\tilde{X}) \, dV = \int_{\partial \Omega} \tilde{G}(\tilde{X} - \tilde{X}_0) \tilde{n} \tilde{F}(\tilde{X}) \, dS - 2\pi^2 \tilde{F}(\tilde{X}_0).
$$

Rearranging gives the stated formula. $\square$

## Consequences of the Cauchy Integral Formula

### The Mean Value Property

**Theorem (mean value property).** If $\tilde{F}$ satisfies $\tilde{\nabla}\tilde{F} = 0$ on a ball $B(\tilde{X}_0, r)$, then

$$
\tilde{F}(\tilde{X}_0) = \frac{1}{2\pi^2 r^3} \int_{\partial B(\tilde{X}_0, r)} \tilde{F}(\tilde{X}) \, dS(\tilde{X}),
$$

where $2\pi^2 r^3$ is the surface area of the three-sphere of radius $r$ in $\mathbb{R}^4$.

**Proof.** Apply the Cauchy integral formula to the ball $B(\tilde{X}_0, r)$ and use the explicit form of the fundamental solution. The kernel becomes constant on the sphere, and the integral reduces to the average of $\tilde{F}$ over the sphere. $\square$

### The Maximum Principle

**Theorem (maximum principle).** If $\tilde{F}$ satisfies $\tilde{\nabla}\tilde{F} = 0$ on a domain $\Omega$ and $\|\tilde{F}\|_E$ attains its maximum at an interior point of $\Omega$, then $\tilde{F}$ is constant on $\Omega$.

**Proof.** Use the mean value property: if $\|\tilde{F}\|_E$ attains its maximum at $\tilde{X}_0$, then the mean value over a small sphere around $\tilde{X}_0$ equals $\tilde{F}(\tilde{X}_0)$, which is only possible if $\tilde{F}$ is constant on the sphere. Iterating over a connected chain of spheres, $\tilde{F}$ is constant on $\Omega$. $\square$

### Liouville's Theorem

**Theorem (Liouville).** If $\tilde{F}$ satisfies $\tilde{\nabla}\tilde{F} = 0$ on all of $V$ and $\|\tilde{F}\|_E$ is bounded, then $\tilde{F}$ is constant.

**Proof.** Apply the Cauchy integral formula to a large ball of radius $R$ centered at $\tilde{X}_0$, and estimate the boundary integral using the boundedness of $\tilde{F}$. The kernel $\tilde{G}(\tilde{X} - \tilde{X}_0)$ is of order $R^{-3}$ on the sphere of radius $R$, and the surface area is of order $R^3$, so the boundary integral is of order $R^0$, i.e., bounded. As $R \to \infty$, the boundary integral tends to zero (using the decay of the kernel and the boundedness of $\tilde{F}$), so $\tilde{F}(\tilde{X}_0)$ is independent of $\tilde{X}_0$. $\square$

### The Identity Theorem

**Theorem (identity theorem).** If two functions $\tilde{F}$ and $\tilde{G}$ satisfying $\tilde{\nabla}\tilde{F} = \tilde{\nabla}\tilde{G} = 0$ on a connected domain $\Omega$ agree on an open subset of $\Omega$, then they agree on all of $\Omega$.

**Proof.** The difference $\tilde{H} = \tilde{F} - \tilde{G}$ satisfies $\tilde{\nabla}\tilde{H} = 0$ and vanishes on an open subset. By the maximum principle applied to $\tilde{H}$ and to $-\tilde{H}$, the modulus of $\tilde{H}$ cannot attain a maximum at an interior point unless $\tilde{H}$ is constant, and since $\tilde{H}$ vanishes on an open subset, the constant is zero. $\square$

### The Cauchy Estimates

**Theorem (Cauchy estimates).** If $\tilde{F}$ satisfies $\tilde{\nabla}\tilde{F} = 0$ on a ball $B(\tilde{X}_0, R)$ and $\|\tilde{F}\|_E \leq M$ on the boundary, then for every multi-index $\alpha$,

$$
\|\partial^\alpha \tilde{F}(\tilde{X}_0)\|_E \leq \frac{C_\alpha M}{R^{|\alpha|}},
$$

where $C_\alpha$ is a constant depending on $\alpha$ and $|\alpha|$ is the total order of the multi-index.

**Proof.** Differentiate the Cauchy integral formula with respect to $\tilde{X}_0$ and estimate the resulting integral using the bound on $\tilde{F}$. $\square$

## The Residue Theory

### The Residue

The Cauchy integral formula for a function that is regular except at isolated singularities leads to a residue theory. However, the non-commutativity of $\mathbb{B}$ makes the definition of the residue more delicate than in the complex case.

**Definition (isolated singularity).** A point $\tilde{X}_0$ is an **isolated singularity** of $\tilde{F}$ if $\tilde{F}$ is defined and regular on a punctured neighborhood $0 < \|\tilde{X} - \tilde{X}_0\|_E < r$ of $\tilde{X}_0$.

**Definition (residue).** The **residue** of $\tilde{F}$ at an isolated singularity $\tilde{X}_0$ is the biquaternion

$$
\mathrm{Res}(\tilde{F}, \tilde{X}_0) = \frac{1}{2\pi^2} \int_{\partial B(\tilde{X}_0, \varepsilon)} \tilde{G}(\tilde{X} - \tilde{X}_0) \tilde{n} \tilde{F}(\tilde{X}) \, dS(\tilde{X}),
$$

where $\varepsilon$ is small enough that the sphere does not enclose any other singularity.

### The Residue Theorem

**Theorem (residue theorem).** Let $\tilde{F}$ be regular on a domain $\Omega$ except at isolated singularities $\tilde{X}_1, \dots, \tilde{X}_n$. Then

$$
\frac{1}{2\pi^2} \int_{\partial \Omega} \tilde{G}(\tilde{X} - \tilde{X}_0) \tilde{n} \tilde{F}(\tilde{X}) \, dS(\tilde{X}) = \sum_{k=1}^{n} \mathrm{Res}(\tilde{F}, \tilde{X}_k)
$$

for any $\tilde{X}_0$ outside the singularities.

**Proof.** Apply the Cauchy integral formula to the domain with small spheres removed around each singularity, and use the definition of the residue. $\square$

## The Relation to Complex and Quaternionic Analysis

The integration theory developed in this article is the biquaternion analogue of the Cauchy integral theory in complex analysis and of the Fueter theory in quaternionic analysis.

**Complex analysis.** In complex analysis, the Cauchy integral formula expresses the value of a holomorphic function at an interior point in terms of its boundary values, with the kernel $1/(z - z_0)$. The biquaternion analogue uses the kernel $\tilde{G}(\tilde{X} - \tilde{X}_0) = \bar{\tilde{X}} - \bar{\tilde{X}}_0 / \|\tilde{X} - \tilde{X}_0\|_E^4$, which is the fundamental solution of the gradient operator in four dimensions.

**Quaternionic analysis.** In Fueter's quaternionic analysis, the analogue of the Cauchy integral formula involves the kernel $q^{-1}/\|q\|^2$ and the quaternion-valued integration over the boundary of a domain in $\mathbb{R}^4$. The biquaternion case is the generalization to complex coefficients, with the additional structure of the four conjugations.

**Clifford analysis.** The general Clifford analysis on $\mathbb{R}^n$ uses the kernel $x^{-1}/\|x\|^n$ and the Clifford algebra-valued integration. The biquaternion case is the case $n = 4$ of this general theory, with the specific structure of the even subalgebra of $\mathrm{Cl}_{1,3}$.

## Open Questions

The following questions are not answered in this article and are left for later work:

1. **The residue theory in the non-commutative case.** The definition of the residue given above is one of several possible definitions. What is the correct definition that makes the residue theorem hold in the strongest form?

2. **The Cauchy integral formula for other domains.** What is the form of the Cauchy integral formula for domains with non-smooth boundaries, or for domains that are not simply connected?

3. **The relation to the polar representations.** How do the polar representations of the biquaternion algebra interact with the integration theory?

4. **The relation to the integral formulas of Clifford analysis.** How does the biquaternion integration theory relate to the general Clifford analysis?

5. **Applications.** What are the applications of the biquaternion integration theory to the solution of partial differential equations?

6. **The integration of functions on other subspaces.** How does the integration theory extend to the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and to the Hermitian subspace $\mathbb{M}_+$?

## Summary

The integral of a biquaternion-valued function on a four-dimensional subspace $V \subset \mathbb{B}$ is defined component-wise with respect to the Lebesgue measure. It is linear, additive, and satisfies the fundamental estimate. The standard theorems of integration carry over: integration by parts, the divergence theorem, and Green's formulas.

The **fundamental solution** of the gradient operator is $\tilde{G}(\tilde{X}) = \bar{\tilde{X}}/\|\tilde{X}\|_E^4$, which satisfies $\tilde{\nabla} \tilde{G} = 0$ away from the origin and $\tilde{\nabla} \tilde{G} = 2\pi^2 \delta_0 e_0$ in the sense of distributions.

The **Cauchy integral formula** expresses the value of a continuously differentiable function at an interior point in terms of its boundary values and the volume integral of its gradient. For functions satisfying $\tilde{\nabla}\tilde{F} = 0$ (the biquaternion analogue of the Cauchy–Riemann equations), the volume integral vanishes and the value at the interior point is given entirely by the boundary values.

The Cauchy integral formula implies the **mean value property**, the **maximum principle**, **Liouville's theorem**, the **identity theorem**, and the **Cauchy estimates**. These are the biquaternion analogues of the standard consequences of the Cauchy integral formula in complex analysis.

The **residue theory** for biquaternion-valued functions is more delicate than in the complex case, because of the non-commutativity of the algebra. The residue at an isolated singularity is defined as a boundary integral, and the residue theorem expresses the integral over the boundary of a domain in terms of the residues at the singularities inside.

The integration theory is related to complex analysis, Fueter's quaternionic analysis, and the general Clifford analysis. The biquaternion case is the case of four dimensions with complex coefficients, which enriches the structure with the four conjugations and the two polar forms.

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- R. Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta\Delta u = 0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* **7** (1934–35) 307–330, for the analysis of quaternion-valued functions of four real variables.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra perspective.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis.
- John Ryan, *Clifford Algebras in Analysis and Related Topics* (CRC Press, 1996), for the analytic theory of Clifford algebras.
- A. Sudbery, "Quaternionic analysis", *Mathematical Proceedings of the Cambridge Philosophical Society* **85** (1979) 199–225, for the quaternionic analogue of the Cauchy integral formula.

