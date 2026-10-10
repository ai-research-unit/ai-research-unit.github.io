# __Biquaternion Integration__

## Introduction

This article introduces the integration theory of biquaternion-valued functions. It follows the article on biquaternion analysis, which defined limits, continuity, and the differential operators on a four-dimensional real subspace of $\mathbb{B}$. The goal here is to define the integral of a biquaternion-valued function, establish the standard properties, and derive the integral formulas that are the counterparts of the Cauchy integral formula and its consequences in complex analysis.

Throughout the main body of this article, we work on the **quaternion subspace** $\mathbb{H}_{\mathbb{B}}$, whose four coordinates $q_0, q_1, q_2, q_3$ are all real. On this subspace, the framework's partial derivatives coincide with the ordinary real partial derivatives, and the framework's gradient $\tilde{\nabla}$ coincides with the Cauchy–Riemann operator on $\mathbb{R}^4$. The integration theory on $\mathbb{H}_{\mathbb{B}}$ is therefore the standard Clifford analysis of $\mathbb{R}^4$, with the biquaternion algebra $\mathbb{B}$ (isomorphic to $\mathrm{Cl}_{1,3}^+$) playing the role of the Clifford algebra. The extension to the indefinite subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$, where the partial derivatives carry factors of $-i$, is not developed here; it is discussed in the open questions. The anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ is the one further case of the same kind as $\mathbb{H}_{\mathbb{B}}$: every coefficient is purely imaginary, so the theory there is the theory below carried through the central rotation $\tilde{Q} \mapsto i\tilde{Q}$, with the Cauchy kernel scaled by $i$ and the sign of the d'Alembertian reversed. That case therefore needs no separate treatment, and the questions left open below concern the indefinite subspaces, where the kernel does change.

The treatment is purely mathematical. The independent variables are four real parameters — the coordinates of $\mathbb{H}_{\mathbb{B}}$. They are independent of any physical interpretation. The complex structure of the coefficients and the non-commutative structure of the quaternion units are the only algebraic ingredients.

Every claim is either proved or stated as a definition. Where a computation is long, all steps are shown.

The biquaternion algebra $\mathbb{B}$, its conjugations, its six distinguished subspaces, the Euclidean norm, the biquaternionic gradient $\tilde{\nabla}$, the quaternion conjugate $\tilde{\nabla}^{\natural}$, the d'Alembertian $\Box$, and the convective derivative $\tilde{D}$ are assumed from the preceding articles.

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

**Proof.** The Leibniz rule for the gradient gives $\tilde{\nabla}(\tilde{F}\tilde{G}) = (\tilde{\nabla}\tilde{F})\tilde{G} + \sum_\mu e_\mu \tilde{F}\,\partial_\mu \tilde{G}$, and the divergence theorem applied to the product $\tilde{F}\tilde{G}$ gives the second display. For the first display, apply the ordinary divergence theorem in $\mathbb{R}^4$ to the field with components $\tilde{F} e_\mu \tilde{G}$ and sum over $\mu$: the volume integrand is $\sum_\mu \partial_\mu(\tilde{F} e_\mu \tilde{G}) = (\tilde{F}\overleftarrow{\nabla})\tilde{G} + \tilde{F}(\tilde{\nabla}\tilde{G})$, and the boundary integrand is $\sum_\mu n_\mu \tilde{F} e_\mu \tilde{G} = \tilde{F}\tilde{n}\tilde{G}$.

**Remark (the non-commutative correction).** The transposition that moves the derivative off $\tilde{G}$ while leaving $\tilde{F}(\tilde{\nabla}\tilde{G})$ in the volume term is **false for a non-central** $\tilde{F}$: the Leibniz term $\sum_\mu e_\mu \tilde{F}\,\partial_\mu \tilde{G}$ equals $\tilde{F}(\tilde{\nabla}\tilde{G})$ only when $\tilde{F}$ commutes with every unit $e_\mu$. The right gradient $\overleftarrow{\nabla}$ is the transposition that removes the restriction, and all the forms coincide when $\tilde{F}$ is a real scalar multiple of $e_0$, which is the scalar case above and the case of the classical formula in *Quaternion Integration*.

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
\int_\Omega \tilde{\nabla}^{\natural} \tilde{F} \, dV = \int_{\partial \Omega} \tilde{n}^{\natural} \tilde{F} \, dS,
$$

where $\tilde{n}^{\natural} = n_0 e_0 - \sum_{k=1}^{3} n_k e_k$ is the quaternion conjugate of the outward unit normal.

**Proof.** This is the same computation as above, with the signs of the vector components reversed.

## Green's Formulas

### First Green's Formula

**Theorem (first Green's formula).** Let $\tilde{F}$ and $\tilde{G}$ be twice continuously differentiable biquaternion-valued functions on $\Omega$ with piecewise smooth boundary $\partial \Omega$, and let $\partial_{\tilde{n}} = \sum_\mu n_\mu \partial_{q_\mu}$ be the scalar normal derivative. Then

$$
\int_\Omega \left[ \sum_{\mu=0}^{3} \left(\frac{\partial \tilde{F}}{\partial q_\mu}\right) (\left(\frac{\partial \tilde{G}}{\partial q_\mu}\right))^{\natural} + \tilde{F}\, (\Box \tilde{G})^{\natural} \right] dV = \int_{\partial \Omega} \tilde{F}\, (\partial_{\tilde{n}} \tilde{G})^{\natural} \, dS.
$$

**Proof.** Apply the ordinary divergence theorem in $\mathbb{R}^4$ to the biquaternion-valued field with components $\tilde{F}\,(\partial_\mu \tilde{G})^{\natural}$: it gives $\int_\Omega \partial_\mu(\tilde{F}\,(\partial_\mu \tilde{G})^{\natural})\,dV = \int_{\partial\Omega} n_\mu \tilde{F}\,(\partial_\mu \tilde{G})^{\natural}\,dS$. The product rule expands the volume integrand as $(\partial_\mu\tilde{F})\,(\partial_\mu \tilde{G})^{\natural} + \tilde{F}\,(\partial_\mu^2 \tilde{G})^{\natural}$, the second term because $\partial_\mu$ is real and therefore commutes with the conjugation. Summing over $\mu$ replaces $\sum_\mu \partial_\mu^2$ by $\Box$ and $\sum_\mu n_\mu \partial_\mu$ by $\partial_{\tilde{n}}$.

**Remark (the classical case).** For real-valued $u$ and $v$ the conjugate is the identity, the first sum is the Euclidean inner product $\nabla u \cdot \nabla v$, and the identity is the classical first Green formula $\int_\Omega (\nabla u\cdot\nabla v + u\,\Delta v)\,dV = \int_{\partial\Omega} u\,\partial_n v\,dS$ of the companion *Partial Differential Equations*.

### Second Green's Formula

**Theorem (second Green's formula).** Under the same hypotheses,

$$
\int_\Omega \left[ \tilde{F}\, (\Box \tilde{G})^{\natural} - (\Box \tilde{F})\, \tilde{G}^{\natural} \right] dV = \int_{\partial \Omega} \left[ \tilde{F}\, (\partial_{\tilde{n}} \tilde{G})^{\natural} - (\partial_{\tilde{n}} \tilde{F})\, \tilde{G}^{\natural} \right] dS.
$$

**Proof.** For each $\mu$ the product rule gives

$$
\partial_{q_\mu} \left[ \tilde{F}\, (\partial_{q_\mu} \tilde{G})^{\natural} - (\partial_{q_\mu} \tilde{F})\, \tilde{G}^{\natural} \right] = \tilde{F}\, (\partial_{q_\mu}^2 \tilde{G})^{\natural} - (\partial_{q_\mu}^2 \tilde{F})\, \tilde{G}^{\natural},
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

the two mixed terms being the same product and cancelling. Summing over $\mu$ makes the left side a divergence whose volume integral is the stated volume integrand, $(\Box\tilde{F})\tilde{G} - \tilde{F}(\Box\tilde{G})$; the divergence theorem turns it into the boundary integral, which by $\sum_\mu n_\mu \partial_{q_\mu} = \partial_{\tilde{n}}$ is the stated surface term.

The derivative in the surface term is essential and cannot be dropped. The products $\tilde{n}\tilde{F}$ and $\tilde{n}\tilde{G}$ alone, with no derivative, would give a boundary term that vanishes identically for central $\tilde{F}$ and $\tilde{G}$; for scalar $u,v$ the classical identity it would have to reproduce is $\int_\Omega (v\Delta u - u\Delta v)\,dV = \int_{\partial\Omega} (v\partial_n u - u\partial_n v)\,dS$, whose right side is not zero.

**Remark (the two pairings).** This formula is the second Green formula with $\tilde{G}$ replaced by $\tilde{G}^{\natural}$, up to the sign of both sides: the second Green formula carries the conjugation in the pairing, this one in the plain product, and the two have the same content. The plain form is the one used in the representation formula below.

### The Representation Formula

**The fundamental solution of $\Box$.** Since $\Delta(\|\tilde{Q}\|_E^{-2}) = -4\pi^2 \delta_0$ in four dimensions, the operator $\Box$ has the central fundamental solution

$$
G_\Box(\tilde{Q}) = -\frac{e_0}{4\pi^2 \|\tilde{Q}\|_E^2}, \qquad \Box G_\Box = \delta_0 ,
$$

homogeneous of degree $-2$. It is a different object from the gradient kernel $\tilde{Q}^{\natural}/\|\tilde{Q}\|_E^4$ of the preceding sections, which is homogeneous of degree $-3$ and inverts the first-order operator $\tilde{\nabla}$ rather than the second-order $\Box$. The companion physics article *The Biquaternion D'Alembertian and Its Green's Functions* writes the corresponding kernel, with the opposite overall sign because its fourth coordinate is $ict$, as $G_{\mathrm{inv}} = \frac{1}{4\pi^2\rho^2}$ with $-\Box G_{\mathrm{inv}} = \delta^{(4)}$.

**Theorem (representation formula).** Let $\Omega \subset \mathbb{H}_{\mathbb{B}}$ be a bounded domain with piecewise smooth boundary, let $u$ be a twice continuously differentiable biquaternion-valued function on $\bar\Omega$, and let $G_\Box$ be as above; write $G_\Box(\tilde{Q}_0 - \tilde{Q})$ for the kernel translated to an interior point $\tilde{Q}_0 \in \Omega$, and let $\partial_{\tilde{n}}$ act on $\tilde{Q}$. Then

$$
u(\tilde{Q}_0) = \int_\Omega G_\Box(\tilde{Q}_0 - \tilde{Q})\,(\Box u)(\tilde{Q})\,dV + \int_{\partial \Omega} \left[ u(\tilde{Q})\,\partial_{\tilde{n}} G_\Box(\tilde{Q}_0 - \tilde{Q}) - G_\Box(\tilde{Q}_0 - \tilde{Q})\,\partial_{\tilde{n}} u(\tilde{Q}) \right] dS .
$$

**Proof.** Apply the Green formula for $\Box$ to $u$ and to $G_\Box(\tilde{Q}_0 - \cdot)$ on the domain $\Omega \setminus B(\tilde{Q}_0,\varepsilon)$, whose boundary is $\partial\Omega$ together with the small sphere. The term $G_\Box(\tilde{Q}_0 - \cdot)$ is annihilated by $\Box$ away from $\tilde{Q}_0$, while its image under $\Box$ is $\delta_0$, so the volume integrand carries $-u(\tilde{Q}_0)$ from the excised ball and $G_\Box(\tilde{Q}_0-\tilde{Q})(\Box u)(\tilde{Q})$ from $\Omega$; the outer and inner boundary pieces assemble into the stated surface integral. Letting $\varepsilon \to 0$ gives the identity. The volume integral converges at $\tilde{Q}_0$ because the kernel is of order $\|\tilde{Q}-\tilde{Q}_0\|_E^{-2}$, which is integrable in four dimensions. $\square$

**Corollary ($\Box$-harmonic case).** If $\Box u = 0$ in $\Omega$ the volume term drops out and

$$
u(\tilde{Q}_0) = \int_{\partial \Omega} \left[ u\,\partial_{\tilde{n}} G_\Box(\tilde{Q}_0 - \cdot) - G_\Box(\tilde{Q}_0 - \cdot)\,\partial_{\tilde{n}} u \right] dS ,
$$

so a function annihilated by the four-dimensional Laplacian is determined at every interior point by its boundary values and its normal derivative. This is the second-order companion of the Cauchy integral formula above, which represents a function annihilated by the first-order operator $\tilde{\nabla}$ by its boundary values alone; here it is the vanishing of $\Box u$, not the size of the kernel's singularity, that removes the volume term.

**The Kirchhoff–Green reading.** For the wave operator the same identity is the **Kirchhoff–Green representation**: on a domain whose boundary is split into an initial surface and a lateral surface, the volume integral is the source term and the surface integral carries the initial data and the boundary data, and the low-dimensional cases are the classical d'Alembert, Poisson and Kirchhoff formulas of the companion *Partial Differential Equations*. The operator $\Box$ of this article is the four-dimensional Laplacian in the real coordinates of $\mathbb{H}_{\mathbb{B}}$; its wave reading, in which the fourth coordinate is $ict$, is the one used by the companion physics articles, and the biquaternionic analogue of the Kirchhoff and Green formulas for that wave ("biwave") operator is constructed by L. A. Alexeyeva in the 2021 paper cited in Further Reading, whose biwave family also unifies the Maxwell- and Dirac-equivalent second-order equations in one operator.

**Verification.** The Green identity and the representation formula were checked numerically on the quaternion subspace, where the four coordinates are real. On the ball $B(0,1.7) \subset \mathbb{R}^4$ the two sides of the representation formula agreed below $10^{-12}$ for the harmonic test functions $q_1$ and $q_1^2 - q_2^2$ and for $u$ with non-vanishing Laplacian ($\|\tilde{Q}\|_E^2$, for which $\Box u = 8$, and $e^{q_0}$), and to the same bound at off-centre test points on balls of radius $1.7$ and $0.9$. The integration-by-parts identity, the Stokes form $\int_{\partial\Omega}\tilde{F}\tilde{n}\tilde{G}\,dS = \int_\Omega[(\tilde{F}\overleftarrow{\nabla})\tilde{G} + \tilde{F}(\tilde{\nabla}\tilde{G})]\,dV$, the first and second Green formulas, and the Green formula for $\Box$ were checked on the same ball and agreed to $10^{-11}$ or better for biquaternion-valued $\tilde{F}$ and $\tilde{G}$. The commutative-looking variants fail on the same data: the discarded boundary form $(\tilde{n}\tilde{F})\tilde{G} - \tilde{F}(\tilde{n}\tilde{G})$ by order one, and the earlier forms of the first and second Green formulas by order one on the same quadrature.

## The Fundamental Solution

### Definition

The **fundamental solution** of the gradient operator $\tilde{\nabla}$ on $\mathbb{H}_{\mathbb{B}}$ is the biquaternion-valued function

$$
\tilde{G}(\tilde{Q}) = \frac{\tilde{Q}^{\natural}}{\|\tilde{Q}\|_E^4},
$$

where $\tilde{Q}^{\natural}$ is the quaternion conjugate of $\tilde{Q}$ and $\|\tilde{Q}\|_E^4 = (\|\tilde{Q}\|_E^2)^2$ is the fourth power of the Euclidean norm.

The function $\tilde{G}$ is defined for $\tilde{Q} \neq 0$ in $\mathbb{H}_{\mathbb{B}}$. It is homogeneous of degree $-3$: $\tilde{G}(\lambda \tilde{Q}) = \lambda^{-3} \tilde{G}(\tilde{Q})$ for $\lambda > 0$.

### The Gradient of the Fundamental Solution

**Theorem (on $\mathbb{H}_{\mathbb{B}}$).** For $\tilde{Q} \in \mathbb{H}_{\mathbb{B}}$ with $\tilde{Q} \neq 0$,

$$
\tilde{\nabla} \tilde{G}(\tilde{Q}) = 0.
$$

**Proof.** Write $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ with $\|\tilde{Q}\|_E^2 = \sum_\mu Q_\mu^2$ (all $Q_\mu$ are real, since $\tilde{Q} \in \mathbb{H}_{\mathbb{B}}$). The quaternion conjugate is $\tilde{Q}^{\natural} = Q_0 e_0 - \sum_k Q_k e_k$. So

$$
\tilde{G}(\tilde{Q}) = \frac{Q_0 e_0 - \sum_k Q_k e_k}{(\sum_\mu Q_\mu^2)^2}.
$$

A direct computation gives

$$
\tilde{\nabla} \tilde{G} = \sum_\mu e_\mu \frac{\partial}{\partial q_\mu} \left( \frac{\tilde{Q}^{\natural}}{\|\tilde{Q}\|_E^4} \right) = \frac{\tilde{\nabla} \tilde{Q}^{\natural}}{\|\tilde{Q}\|_E^4} + \tilde{Q}^{\natural} \tilde{\nabla} \left( \frac{1}{\|\tilde{Q}\|_E^4} \right),
$$

where we have used the product rule and the fact that $\tilde{Q}^{\natural}$ and the scalar function $1/\|\tilde{Q}\|_E^4$ commute with the partial derivatives (since $\tilde{Q}^{\natural}$ is a function of $\tilde Q$ and the partial derivative acts on the variable $\tilde Q$).

The first term is $\tilde{\nabla}\tilde{Q}^{\natural} = \sum_\mu e_\mu e_\mu^{\natural} = e_0 - e_1^2 - e_2^2 - e_3^2 = 4 e_0$. (Here we used $\partial_{q_\mu}\tilde{Q}^{\natural} = e_\mu^{\natural}$, which holds because the coefficients $Q_\mu$ are real: $\partial_{q_0}\tilde{Q}^{\natural} = e_0$ and $\partial_{q_k}\tilde{Q}^{\natural} = -e_k$.)

For the second term, on $\mathbb{H}_{\mathbb{B}}$ the coefficients are real, so $\partial_{q_\mu}\|\tilde Q\|_E^2 = \partial_{q_\mu}(\sum_\nu Q_\nu^2) = 2Q_\mu$. Hence

$$
\partial_{q_\mu}\left(\frac{1}{\|\tilde Q\|_E^4}\right) = -\frac{2}{\|\tilde Q\|_E^6} \partial_{q_\mu}\|\tilde Q\|_E^2 = -\frac{2 \cdot 2 Q_\mu}{\|\tilde Q\|_E^6} = -\frac{4 Q_\mu}{\|\tilde Q\|_E^6}.
$$

Therefore

$$
\tilde{\nabla}\left(\frac{1}{\|\tilde Q\|_E^4}\right) = \sum_\mu e_\mu \left(-\frac{4 Q_\mu}{\|\tilde Q\|_E^6}\right) = -\frac{4}{\|\tilde Q\|_E^6}\sum_\mu Q_\mu e_\mu = -\frac{4\tilde Q}{\|\tilde Q\|_E^6}.
$$

Multiplying by $\tilde{Q}^{\natural}$ on the left:

$$
\tilde{Q}^{\natural} \tilde{\nabla}\left(\frac{1}{\|\tilde Q\|_E^4}\right) = -\frac{4\tilde{Q}^{\natural}\tilde Q}{\|\tilde Q\|_E^6}.
$$

On $\mathbb{H}_{\mathbb{B}}$, $\tilde{Q}^{\natural}\tilde Q = \sum_\mu Q_\mu^2 e_0 = \|\tilde Q\|_E^2 e_0$. So this term is $-4\|\tilde Q\|_E^2 e_0/\|\tilde Q\|_E^6 = -4e_0/\|\tilde Q\|_E^4$.

Combining both terms:

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

On the sphere $\|\tilde{Q}\|_E = \varepsilon$, the outward unit normal is $\tilde{n} = \tilde{Q}/\varepsilon$, and $\tilde{G} = \tilde{Q}^{\natural}/\varepsilon^4$. So

$$
\tilde{G} \tilde{n} = \frac{\tilde{Q}^{\natural}}{\varepsilon^4} \cdot \frac{\tilde{Q}}{\varepsilon} = \frac{\|\tilde{Q}\|_E^2}{\varepsilon^5} e_0 = \frac{1}{\varepsilon^3} e_0.
$$

So

$$
\int_{\|\tilde{Q}\|_E = \varepsilon} \tilde{G} \tilde{n} \phi \, dS = \frac{1}{\varepsilon^3} \int_{\|\tilde{Q}\|_E = \varepsilon} \phi \, dS \cdot e_0.
$$

As $\varepsilon \to 0$, the average of $\phi$ over the sphere tends to $\phi(0)$, and the surface area of the sphere of radius $\varepsilon$ is $2\pi^2 \varepsilon^3$. So the integral tends to $2\pi^2 \phi(0) e_0$. Therefore

$$
\langle \tilde{\nabla} \tilde{G}, \phi \rangle = -2\pi^2 \phi(0) e_0,
$$

which is the distributional identity

$$
\tilde{\nabla} \tilde{G} = -2\pi^2 \delta_0 e_0.
$$

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

Apply the divergence theorem to the product $\tilde{G}(\tilde{Q} - \tilde{Q}_0) \tilde{F}(\tilde{Q})$ on the domain $\Omega_\varepsilon = \Omega \setminus B(\tilde{Q}_0, \varepsilon)$, where $B(\tilde{Q}_0, \varepsilon)$ is the ball of radius $\varepsilon$ centred at $\tilde{Q}_0$. The boundary of $\Omega_\varepsilon$ consists of $\partial \Omega$ and the sphere $\partial B(\tilde{Q}_0, \varepsilon)$.

By the divergence theorem,

$$
\int_{\Omega_\varepsilon} \tilde{\nabla} \left( \tilde{G}(\tilde{Q} - \tilde{Q}_0) \tilde{F}(\tilde{Q}) \right) dV = \int_{\partial \Omega} \tilde{G}(\tilde{Q} - \tilde{Q}_0) \tilde{n} \tilde{F}(\tilde{Q}) \, dS + \int_{\partial B(\tilde{Q}_0, \varepsilon)} \tilde{G}(\tilde{Q} - \tilde{Q}_0) \tilde{n} \tilde{F}(\tilde{Q}) \, dS.
$$

On the small sphere, $\tilde{n} = -(\tilde{Q} - \tilde{Q}_0)/\varepsilon$ (pointing inward toward $\tilde{Q}_0$, hence with a sign), and the computation of the boundary term gives

$$
\int_{\partial B(\tilde{Q}_0, \varepsilon)} \tilde{G}(\tilde{Q} - \tilde{Q}_0) \tilde{n} \tilde{F}(\tilde{Q}) \, dS \to -2\pi^2 \tilde{F}(\tilde{Q}_0) \quad \text{as } \varepsilon \to 0.
$$

The volume integral on the left is

$$
\int_{\Omega_\varepsilon} \tilde{\nabla} \left( \tilde{G}(\tilde{Q} - \tilde{Q}_0) \tilde{F}(\tilde{Q}) \right) dV = \int_{\Omega_\varepsilon} \tilde{G}(\tilde{Q} - \tilde{Q}_0) (\tilde{\nabla}\tilde{F})(\tilde{Q}) \, dV,
$$

using the product rule and the fact that $\tilde{\nabla}\tilde{G} = 0$ away from $\tilde{Q}_0$.

Combining and taking the limit $\varepsilon \to 0$, we obtain

$$
\int_\Omega \tilde{G}(\tilde{Q} - \tilde{Q}_0) (\tilde{\nabla}\tilde{F})(\tilde{Q}) \, dV = \int_{\partial \Omega} \tilde{G}(\tilde{Q} - \tilde{Q}_0) \tilde{n} \tilde{F}(\tilde{Q}) \, dS - 2\pi^2 \tilde{F}(\tilde{Q}_0).
$$

Rearranging gives the stated formula.

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

**Proof.** Apply the Cauchy integral formula to a large ball of radius $R$ centred at $\tilde{Q}_0$, and estimate the boundary integral using the boundedness of $\tilde{F}$. The kernel $\tilde{G}(\tilde{Q} - \tilde{Q}_0)$ is of order $R^{-3}$ on the sphere of radius $R$, and the surface area is of order $R^3$, so the boundary integral is of order $R^0$, i.e., bounded. As $R \to \infty$, the boundary integral tends to zero, so $\tilde{F}(\tilde{Q}_0)$ is independent of $\tilde{Q}_0$.

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

## The Residue Theory

### The Residue

The Cauchy integral formula for a function that is regular except at isolated singularities leads to a residue theory. However, the non-commutativity of $\mathbb{B}$ makes the definition of the residue more delicate than in the complex case.

**Definition (isolated singularity).** A point $\tilde{Q}_0$ is an **isolated singularity** of $\tilde{F}$ if $\tilde{F}$ is defined and regular on a punctured neighborhood $0 < \|\tilde{Q} - \tilde{Q}_0\|_E < r$ of $\tilde{Q}_0$.

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

The integration theory developed in this article is the biquaternion analogue of the Cauchy integral theory in complex analysis and of the Fueter theory in quaternionic analysis.

**Complex analysis.** In complex analysis, the Cauchy integral formula expresses the value of a holomorphic function at an interior point in terms of its boundary values, with the kernel $1/(A - A_0)$. The biquaternion analogue uses the kernel $\tilde{G}(\tilde{Q} - \tilde{Q}_0) = (\tilde{Q}^{\natural} - \tilde{Q}^{\natural}_0)/\|\tilde{Q} - \tilde{Q}_0\|_E^4$, which is the fundamental solution of the gradient operator in four dimensions.

**Quaternionic analysis.** In Fueter's quaternionic analysis, the analogue of the Cauchy integral formula involves the kernel $q^{-1}/\|q\|^2$ and the quaternion-valued integration over the boundary of a domain in $\mathbb{R}^4$. The biquaternion case is the generalization to complex coefficients, with the additional structure of the four conjugations.

**Clifford analysis.** The general Clifford analysis on $\mathbb{R}^n$ uses the kernel $\tilde Q^{-1}/\|\tilde Q\|^{n-2}$, equivalently $\tilde Q^{\natural}/\|\tilde Q\|^n$ (homogeneous of degree $1 - n$), and the Clifford algebra-valued integration. The biquaternion case is the case $n = 4$ of this general theory, with the specific structure of the even subalgebra of $\mathrm{Cl}_{1,3}$.

## Open Questions

The following questions are not answered in this article and are left for later work:

1. **The extension to $\mathbb{M}_+$ and $\mathbb{M}_-$.** The integration theory presented here is for functions on the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, where the four coordinates are real. Extending the theory to the indefinite subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$ requires modifying the fundamental solution, because the kernel $\tilde{Q}^{\natural}/\|\tilde Q\|_E^4$ is not annihilated by the framework's gradient on these subspaces. Indeed, on $\mathbb{M}_+$ and $\mathbb{M}_-$, the coefficients $Q_\mu$ include imaginary entries, and the identity $\tilde{Q}^{\natural}\tilde Q = \|\tilde Q\|_E^2 e_0$ fails, so the proof of $\tilde\nabla\tilde G = 0$ does not carry over. Whether a modified kernel exists, and how it relates to the standard Clifford analysis of $\mathbb{R}^{3,1}$ or $\mathbb{R}^{1,3}$, is open.

2. **The residue theory in the non-commutative case.** The definition of the residue given above is one of several possible definitions. What is the correct definition that makes the residue theorem hold in the strongest form?

3. **The Cauchy integral formula for other domains.** What is the form of the Cauchy integral formula for domains with non-smooth boundaries, or for domains that are not simply connected?

4. **Applications.** What are the applications of the biquaternion integration theory to the solution of partial differential equations?

6. **The general subspace.** Can the integration theory be extended from $\mathbb{H}_{\mathbb{B}}$ to the full biquaternion algebra $\mathbb{B}$ and to its indefinite subspaces, with a canonical choice of fundamental solution for each?

## Summary

The integral of a biquaternion-valued function on the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ is defined component-wise with respect to the Lebesgue measure. It is linear, additive, and satisfies the fundamental estimate. The standard theorems of integration carry over: integration by parts, the divergence theorem, and Green's formulas. Because the algebra is not commutative, transposing the gradient off a product requires the right gradient $\overleftarrow{\nabla}$, and the commutative-looking forms hold only for central fields; the identities are stated in the forms that hold for general biquaternion-valued fields.

The **fundamental solution** of the gradient operator on $\mathbb{H}_{\mathbb{B}}$ is $\tilde{G}(\tilde{Q}) = \tilde{Q}^{\natural}/\|\tilde{Q}\|_E^4$, which satisfies $\tilde{\nabla} \tilde{G} = 0$ away from the origin and $\tilde{\nabla} \tilde{G} = -2\pi^2 \delta_0 e_0$ in the sense of distributions. The fundamental solution of the second-order operator $\Box$ is the central function $G_\Box = -e_0/(4\pi^2\|\tilde{Q}\|_E^2)$.

The **Green formula for $\Box$** and its **representation formula** express a biquaternion-valued function at an interior point by the volume integral of its $\Box$ against $G_\Box$ together with a surface integral of its boundary values and normal derivative; when $\Box u = 0$ the volume term drops out and the interior value is carried by the boundary alone. For the wave operator this is the biquaternionic **Kirchhoff–Green representation**, the analogue of the classical Kirchhoff and Green formulas.

The **Cauchy integral formula** expresses the value of a continuously differentiable function at an interior point in terms of its boundary values and the volume integral of its gradient. For functions satisfying $\tilde{\nabla}\tilde{F} = 0$ (the biquaternion analogue of the Cauchy–Riemann equations), the volume integral vanishes and the value at the interior point is given entirely by the boundary values.

The Cauchy integral formula implies the **mean value property**, the **maximum principle**, **Liouville's theorem**, the **identity theorem**, and the **Cauchy estimates**. These are the biquaternion analogues of the standard consequences of the Cauchy integral formula in complex analysis.

The **residue theory** for biquaternion-valued functions is more delicate than in the complex case, because of the non-commutativity of the algebra. The residue at an isolated singularity is defined as a boundary integral, and the residue theorem expresses the integral over the boundary of a domain in terms of the residues at the singularities inside.

The integration theory is related to complex analysis, Fueter's quaternionic analysis, and the general Clifford analysis. The biquaternion case on $\mathbb{H}_{\mathbb{B}}$ is the case $n = 4$ with complex coefficients, and enriches the structure with the four conjugations and the two polar forms.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion subspace (real coordinates $q_0, q_1, q_2, q_3$) |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | Point in $\mathbb{H}_{\mathbb{B}}$ (all $Q_\mu$ real) |
| $\partial/\partial q_\mu$ | Ordinary real partial derivative |
| $\tilde{\nabla} = \sum_\mu e_\mu \partial/\partial q_\mu$ | Biquaternionic gradient (Cauchy–Riemann operator) |
| $\tilde{F}\overleftarrow{\nabla} = \sum_\mu (\partial \tilde{F}/\partial q_\mu) e_\mu$ | Right gradient of $\tilde{F}$ |
| $\tilde{\nabla}^{\natural}$ | Quaternion conjugate of the gradient |
| $\Box = \partial^2/\partial q_0^2 + \Delta_q$ | d'Alembertian |
| $\tilde{n}$ | Biquaternion-valued outward unit normal |
| $\partial_{\tilde{n}} = \sum_\mu n_\mu \partial_{q_\mu}$ | Scalar normal derivative in the outward direction |
| $\tilde{G}(\tilde{Q}) = \tilde{Q}^{\natural}/\|\tilde{Q}\|_E^4$ | Fundamental solution of the gradient |
| $G_\Box(\tilde{Q}) = -e_0/(4\pi^2\|\tilde{Q}\|_E^2)$ | Fundamental solution of $\Box$ |
| $dV$ | Lebesgue measure on the four real coordinates of $\mathbb{H}_{\mathbb{B}}$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- R. Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta\Delta u = 0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* **7** (1934–35) 307–330, for the analysis of quaternion-valued functions of four real variables.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford analysis.
- John Ryan, *Clifford Algebras in Analysis and Related Topics* (CRC Press, 1996), for the analytic theory of Clifford algebras.
- A. Sudbery, "Quaternionic analysis", *Mathematical Proceedings of the Cambridge Philosophical Society* **85** (1979) 199–225, for the quaternionic analogue of the Cauchy integral formula.
- L. A. Alexeyeva, "Biquaternionic wave equations and the properties of their generalized solutions", *Differential Equations* **57** (5) (2021) 594–604 (DOI 10.1134/S0012266121050049), for the fundamental and generalized solutions of the biquaternionic wave ("biwave") operator, the conditions on its shock fronts, the Cauchy problem, and the analogues of the Kirchhoff and Green representation formulas.

