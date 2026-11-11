# __Hamiltonian Field Theory in Biquaternionic Form__

## Introduction

The companion article *Lagrangian and Hamiltonian Mechanics in Biquaternionic Form* ends where the finite-dimensional theory ends: one configuration biquaternion $\tilde q$, one momentum biquaternion $\tilde p$, one phase-space biquaternion $\tilde q+i\tilde p$, and a Poisson bracket on the functions of that finite collection of numbers. A field is not a finite collection of numbers. Its configuration is a *function* of the position, and the variational derivative replaces the partial derivative: the Legendre transform acts on a density, the momentum conjugate to the field is itself a function of the position, and the bracket that survives is a bracket on functionals. This article performs that transcription for the field the corpus actually uses — the central scalar field of the Klein–Gordon articles — and states plainly what the algebra supplies and what it does not.

Two objects are built here, and they answer two different questions. The first is the **Hamiltonian density** $\mathcal H$, the Legendre transform of the Lagrangian density, which is also the energy density of the companion article on stress–energy; the second is the **field Poisson bracket**, the bracket on functionals of the field and its conjugate momentum, together with the continuity equation that the density satisfies along the motion. Their sum is the classical Hamiltonian field theory in biquaternion form. The article then says where the algebra's contribution stops: for a central field the bracket is the standard one, and the biquaternion content is the packaging of the density and the flux rather than a change of the bracket. The genuinely different Hamiltonian formalism for a field — the covariant one, in which the conjugate object is a *quadruple* of momenta rather than one momentum field — is named at the end and developed in the mathematical corpus.

The conventions are those of the read list: the algebra, the units, the sectors, the material coordinate, the $i r'_t$ metric, the d'Alembertian and the conjugations are those of *Algebra and Element Conventions*, *Physics Units and Common Elements Conventions* and *Operator and Calculus Conventions*, and none is restated here. The central scalar field is $\tilde{Ξ}(\tilde R_\Phi)=\xi(\tilde R_\Phi)e_t$ with $\tilde R_\Phi\in\mathbb{B}_{\Phi}$, its Lagrangian density is the one fixed by *Noether's Theorem in Biquaternionic Form* and used by *Canonical Quantization of the Biquaternion Klein–Gordon Field*,

$$
\mathcal{L}=-\mathrm{Sc}\!\left[((\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}^{*})(\tilde\nabla_\Phi\tilde{Ξ})\right]-k_m^{2}\,\mathrm{Sc}\!\left[\tilde{Ξ}^{*}\tilde{Ξ}\right]
=|\partial\xi/\partial r'_t|^2-|\nabla\xi|^2-k_m^{2}|\xi|^2,
\qquad k_m=\dfrac{mc}{\hbar},
$$

and the equation of motion is $\left(\Box-k_m^{2}\right)\tilde{Ξ}=0$, that is $\partial^2\xi/\partial {r'_{t}}^2=c^2(\Delta\xi-k_m^{2}\xi)$.

The companion articles are:

- Companion article *Lagrangian and Hamiltonian Mechanics in Biquaternionic Form*, for the finite-dimensional Legendre transform, the phase-space biquaternion and the Poisson bracket that this article extends to a density.
- Companion article *The Action Principle and the Classical Limit as Stationary Phase in Biquaternionic Form*, for the action and its first variation, and for the boundary term that the field case reproduces as a flux.
- Companion article *Noether's Theorem in Biquaternionic Form*, for the Lagrangian density, the conserved currents, and the canonical energy–momentum tensor.
- Companion article *Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form*, for the energy–momentum biquaternion and the electromagnetic packaging that the scalar field's density and flux repeat.
- Companion article *Canonical Quantization of the Biquaternion Klein–Gordon Field*, for the quantum theory that takes this classical canonical structure over without modification, and for the constraint analysis of the Dirac and Maxwell fields that this article contrasts with.

## The Standard Hamiltonian Field Theory

### The Conjugate Momentum Field

The Legendre transform of a field theory is performed pointwise in the position and acts on the Lagrangian *density*. Write $\partial\xi/\partial r'_t$ for the time derivative at fixed position and define the **conjugate momentum field** by the partial derivative of the density with respect to the velocity field,

$$
\pi=\frac{\partial\mathcal{L}}{\partial\left(\partial\xi/\partial r'_t\right)}=\left(\partial\xi/\partial r'_t\right)^{\,*},
\qquad
\pi^\dagger=\frac{\partial\mathcal{L}}{\partial\left(\partial\xi/\partial r'_t\right)^{\,*}}=\partial\xi/\partial r'_t .
$$

The second formula is the conjugate of the first, and both are needed because the field is complex; on the real field $\xi=\xi^*$ the two agree. The transform is **regular**: $\pi$ determines $\partial\xi/\partial r'_t$ and conversely, since $\partial\xi/\partial r'_t=c^2\pi^\dagger$, so the phase space of the theory is the full space of pairs $(\xi,\pi)$ at each position and there is no constraint. This is the first structural fact of the transcription, and it is the point at which the scalar field differs from the two fields whose quantization the corpus treats alongside it. The Dirac field, being first order in time, carries a second-class constraint $\pi-i\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\approx0$; the Maxwell field, being a gauge field, carries the two first-class constraints $\pi^0\approx0$ and $\mathrm{div}\,\vec\pi\approx0$; the scalar field carries neither. A regular Legendre transform is what makes the phase space unconstrained, and an unconstrained phase space is what makes the Hamiltonian transcription a transposition with nothing added.

### The Hamiltonian Density

The Legendre transform of the density is the **Hamiltonian density**

$$
\mathcal{H}=\pi\partial\xi/\partial r'_t+\pi^\dagger\left(\partial\xi/\partial r'_t\right)^{\,*}-\mathcal{L},
$$

and the **total Hamiltonian** is its integral over space, $H=\int\mathcal{H}\,d^3r$. Substituting the density and the momentum field gives

$$
\mathcal{H}=|\partial\xi/\partial r'_t|^2+|\nabla\xi|^2+k_m^{2}|\xi|^2,
$$

the sum of three squares. Two remarks fix the sign bookkeeping. First, **the Hamiltonian density is not minus the Lagrangian density**, although it is so for a mechanical Lagrangian whose kinetic energy is quadratic in the velocities: here $-\mathcal{L}=|\partial\xi/\partial r'_t|^2-|\nabla\xi|^2-k_m^{2}|\xi|^2$, which differs from $\mathcal{H}$ by the kinetic term again, since the Legendre transform of a complex field pairs $\pi$ with $\partial\xi/\partial r'_t$ *and* $\pi^\dagger$ with $\left(\partial\xi/\partial r'_t\right)^{*}$. Second, **the density is the energy density**: the expression above is exactly the time–time component $T_{00}$ that *Noether's Theorem in Biquaternionic Form* obtains from translation invariance, positive because it is a sum of squares. The Hamiltonian of the field and the energy of the field are the same functional, and that is not a coincidence of the conventions but the content of the Legendre transform for a Lagrangian with no explicit time dependence.

### The Hamiltonian Field Equations

Hamilton's equations for the field are the pair

$$
\partial\xi/\partial r'_t=\frac{\delta H}{\delta\pi^\dagger}=c^2\pi^\dagger,
\qquad
\partial\pi/\partial r'_t=-\frac{\delta H}{\delta\xi^\dagger}=-c^2(\Delta\xi-k_m^{2}\xi),
$$

where $\delta/\delta$ is the variational derivative and the second equation uses the first to eliminate $\pi$. Eliminating $\pi$ between them returns $\partial^2\xi/\partial {r'_{t}}^2=c^2(\Delta\xi-k_m^{2}\xi)$, the Klein–Gordon equation: the Hamiltonian field equations and the Euler–Lagrange equation are the same equations, exactly as in the finite-dimensional case. The only new feature is that the conjugate equation is a *PDE for a density* rather than an ODE for a number, and the variational derivative is what makes the pairing between them work.

### The Field Poisson Bracket

The bracket of the finite-dimensional theory is replaced by a bracket on functionals. For functionals $A[\xi,\pi]$, $B[\xi,\pi]$ of the field and its conjugate momentum,

$$
\{A,B\}=\int d^3r\left(
\frac{\delta A}{\delta\xi}\frac{\delta B}{\delta\pi}
+\frac{\delta A}{\delta\xi^{\,*}}\frac{\delta B}{\delta\pi^\dagger}
-\frac{\delta A}{\delta\pi}\frac{\delta B}{\delta\xi}
-\frac{\delta A}{\delta\pi^\dagger}\frac{\delta B}{\delta\xi^{\,*}}
\right),
$$

so that the canonical brackets are the distributional relations

$$
\boxed{\ \{\xi(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z),\pi(\vec y)\}=\delta^3(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z-\vec y)\ },
\qquad
\{\xi(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z),\xi(\vec y)\}=\{\pi(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z),\pi(\vec y)\}=0,
$$

with the conjugates carrying the mirrored signs. The bracket is antisymmetric and satisfies the Jacobi identity, and it does so **locally**: the Jacobi sum of three functionals is an integral of a sum of terms each of which is the Jacobi sum of the corresponding local expression in $(\xi,\pi)$ at a point, which vanishes because the finite-dimensional bracket of the canonical pair vanishes. The field bracket is therefore not a new algebraic structure; it is the same bracket applied at every point and integrated, and the delta functions are the statement that distinct points do not interact through the bracket. The Hamiltonian flow of the total Hamiltonian along the bracket is the field equation: for any functional $A$, $\partial A/\partial r'_t=\{A,H\}$, which on the canonical pair returns the pair of equations above.

### The Continuity Equation and the Energy Flux

The energy density is conserved along the motion by a local conservation law. Differentiating $\mathcal{H}$ in time and using the equation of motion gives

$$
\boxed{\ \partial/\partial r'_t\mathcal{H}+\nabla\cdot\vec S=0\ },
\qquad
\vec S=-(\left(\partial\xi/\partial r'_t\right)^{\,*}\nabla\xi+\partial\xi/\partial r'_t\,\nabla\xi^{\,*})=-c^2(\pi\nabla\xi+\pi^\dagger\nabla\xi^{\,*});
$$

the mass terms cancel between the time derivative of $k_m^{2}|\xi|^2$ and the equation of motion, and the surviving terms are a divergence. The vector $\vec S$ is the **energy flux**. For a single plane wave $\xi=\xi_0\exp(i(\vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)-\omega r'_t/c))$ one has $\vec S=2\omega\vec k_\Phi|\xi_0|^2$, directed along the wavevector, so the energy travels the way the wave travels. Integrating the conservation law over a volume and using the vanishing of the flux at infinity makes the four-momentum

$$
P_\nu=\frac{1}{c}\int T_{t\nu}\,d^3r
$$

time-independent, the statement that the flux of the companion stress–energy article is a conserved current.

## The Biquaternionic Transcription

### The Field and Its Conjugate Momentum

The field is central-valued, $\tilde{Ξ}=\xi e_t$, and its conjugate momentum is central-valued for the same reason: the momentum field is obtained from the field by a central operation, so it lives in the centre. Writing

$$
\tilde\Pi=\pi e_t\in\mathbb{B}_{C},
$$

the pair $(\tilde{Ξ},\tilde\Pi)$ is the field-theoretic analogue of the pair $(\tilde q,\tilde p)$ of the finite-dimensional article, with one difference that is worth stating: $\tilde q$ was a real quaternion in $\mathbb{B}_{H}$ and $\tilde p$ its conjugate momentum in the same subspace, while $\tilde{Ξ}$ and $\tilde\Pi$ are central, in $\mathbb{B}_{C}$. The value space is smaller because the spin of the field is zero. A field that carried a spinor index would take its values in the spinor module, and its conjugate momentum would carry the same index; the central scalar is the case in which the index is absent, and in that case the momentum field is a second complex number at each point rather than a second biquaternion.

### The Hamiltonian Density as a Hermitian Bilinear

The density is the sum of two Hermitian forms. With $\tilde\nabla_\Phi\tilde{Ξ}$ the biquaternionic gradient of the field — its four coefficients are the four partial derivatives, $(\partial/\partial R_t\,\xi,\partial/\partial R_x\xi,\partial/\partial R_y\xi,\partial/\partial R_z\xi)$ —

$$
\boxed{\;\mathcal{H}=\mathrm{Sc}\!\left[(\tilde\nabla_\Phi\tilde{Ξ})^{*}(\tilde\nabla_\Phi\tilde{Ξ})\right]+k_m^{2}\,\mathrm{Sc}\!\left[\tilde{Ξ}^{*}\tilde{Ξ}\right]\;}.
$$

The second term is the mass form, positive and central. The first is the **kinetic-plus-gradient form**, and the identity $\mathrm{Sc}[(\tilde\nabla_\Phi\tilde{Ξ})^{*}(\tilde\nabla_\Phi\tilde{Ξ})]=|\partial\xi/\partial r'_t|^2+|\nabla\xi|^2$ is where the $i r'_t$ convention does its quiet work: the time coefficient of the gradient is $\partial/\partial R_t\,\xi=-ic^{-1}\partial\xi/\partial r'_t$, so $|\partial/\partial R_t\,\xi|^2=|\partial\xi/\partial r'_t|^2$ and the kinetic term is *positive*, not negative. This is the same sign that makes the norm of a material four-vector have signature $(3,1)$ and the d'Alembertian $\Box=\partial^2/\partial R_t^2+\Delta$; a reader who computes $|\partial/\partial R_t\,\xi|^2$ as $-|\partial\xi/\partial r'_t|^2$ has conjugated the operator instead of the field, and will find the kinetic energy negative. The form $\tilde Q_1^{*}\tilde Q_1$ is of course positive definite on the algebra — that is the Hermitian form of $\mathbb{B}_{\Psi}$ — and it is *this* form, not the holomorphic norm $\langle\tilde Q_1\rangle_{\natural} = \langle\tilde Q_1,\tilde Q_1\rangle_{\natural}=\tilde Q_1\tilde Q_1^{\natural}$ of signature $(3,1)$, that the energy density uses. The distinction matters: the norm's vanishing set is the light cone, the Hermitian form's is only the origin.

### The Energy–Momentum Biquaternion

The density and the flux are the scalar and vector parts of one Hermitian biquaternion:

$$
\tilde W_{\Psi}=\mathcal{H}\,e_t+\frac{i}{c}\vec S\in\mathbb{B}_{\Psi},
\qquad
\tilde\nabla_\Phi\tilde W_{\Psi}=0
\ \ \text{on shell}.
$$

The scalar part of the biquaternion divergence is the continuity equation. This is the *same packaging* that the companion article on stress–energy gives the electromagnetic field, $\tilde W_{\Psi}=\frac{1}{2}\tilde F\tilde F^{*}=W\,e_t+\frac{i}{c}\vec S$, whose scalar part is the Poynting theorem; the scalar field's energy density sits in the scalar direction of the informational sector and its flux in the three vector directions $i\vec e_\mu$, so the two fields' energy–momentum biquaternions are elements of the same sector in the same arrangement. The one difference is that the electromagnetic $\tilde W_{\Psi}$ is bilinear in the field strength whereas the scalar $\tilde W_{\Psi}$ is bilinear in the gradient of the field, which is the field-theoretic way of saying that the scalar field carries no spin and its energy comes entirely from the derivatives.

The static limit makes the arrangement visible. For a time-independent field the flux vanishes, $\tilde W_{\Psi}=\mathcal{H}e_t$, and the conservation law reduces to $\nabla\cdot\vec S=0$, which is empty; the energy is conserved trivially. For a running wave it is the other way: $\mathcal{H}$ and $|\vec S|/c$ are equal and the biquaternion has the null-field pattern of a single travelling wave, exactly as the companion stress–energy article records for the massless scalar and for the electromagnetic wave.

### The Brackets in the Algebra

The canonical bracket is read in the algebra as the scalar part of a pairing. Since $\xi$ and $\pi$ are the coefficients of central elements, the bracket of the algebra's central directions is the bracket of the two complex numbers, and the field bracket above is its integral over space. The biquaternion content of the brackets is therefore not a new bracket but the **sector bookkeeping** of the fields being bracketed: $\tilde{Ξ}\in\mathbb{B}_{C}$ while its gradient is not, and the momentum $\tilde\Pi$ is central whereas the momentum of a bivector-valued field would lie in $\mathbb{B}_{\Phi}$ or $\mathbb{B}_{\Psi}$. The scalar field brackets with itself in the centre, and this is the classical face of the fact, recorded by the quantization article, that the scalar field's canonical structure is taken over from the classical theory without modification.

## The Sector Reading of the Hamiltonian Density

The field of spin zero is the field of the centre, and the centre is the direct sum of the two sectors' scalar lines, $\mathbb{B}_{C}=T_{\mathrm i}\oplus T_{\mathrm m}$ with $T_{\mathrm i}=\mathbb{R}e_t$ and $T_{\mathrm m}=\mathbb{R}(ie_t)$. Writing the complex scalar as two real scalars, one in each sector's scalar direction,

$$
\tilde{Ξ}=\frac{1}{\sqrt2}\left(\underbrace{\xi_1\,e_t}_{\in\,\mathbb{B}_{\Psi}}+\underbrace{\xi_2\,ie_t}_{\in\,\mathbb{B}_{\Phi}}\right),
\qquad
\mathrm{Sc}\!\left[\tilde{Ξ}^{*}\tilde{Ξ}\right]=\frac12\left(\xi_1^2+\xi_2^2\right),
$$

the Hamiltonian density splits accordingly,

$$
\mathcal{H}=\frac12\left[
\left(\left(\partial\xi_{1}/\partial r'_t\right)^{2}+\left(\partial\xi_{2}/\partial r'_t\right)^{2}\right)
+|\nabla\xi_1|^2+|\nabla\xi_2|^2
+k_m^{2}\left(\xi_1^2+\xi_2^2\right)
\right],
$$

the sum of the two sectors' kinetic, gradient and mass terms. Three features of this split are the ones the informational articles use. First, **both sectors contribute to the energy with the same sign**, so the energy is positive whichever sector carries the field. Second, the split is not the charge: the energy is the sum of the sector contributions, positive definite, whereas the charge is the pairing of the two sectors' fields that is antisymmetric in them, $j_0\propto\mathrm{Im}(\xi^*\partial\xi/\partial r'_t)\propto\xi_1\partial\xi_{2}/\partial r'_t-\xi_2\partial\xi_{1}/\partial r'_t$, and its sign is not fixed. The same two readings appear in the phase-space biquaternion of the companion symplectic article as the real and imaginary parts of the Hermitian pairing: the real part is the metric and is additive over the sectors, the imaginary part is the symplectic form and is antisymmetric. Third, **the split is a split of the kinetic and gradient terms as well as the mass term**, so the sector exchange that the oscillator article realises as a quarter-period advance is, in the field, an exchange of the two real scalars at every point.

## Covariant Hamiltonian Field Theory

The formalism so far is the **instantaneous** one: it singles out a time direction, differentiates with respect to it, and conjugate to the field there is one momentum field. It is the formalism in which the equal-time brackets of the quantization article are written, and it is the one in which the constraint analysis of the gauge field can be performed at all. It is not, however, the only Hamiltonian formalism for a field, and its relation to the covariant one is worth stating here because the gauge fields' Hamiltonian structure lives on the other side.

In the **covariant** formalism, all four derivatives of the field are treated on the same footing and conjugate to the field there is a *quadruple* of momenta, the **polymomentum** $p_\mu=\partial\mathcal{L}/\partial(\partial/\partial R_\mu\,\xi)$, one per direction of differentiation. The Legendre transform is performed on the quadruple, and the resulting **De Donder–Weyl Hamiltonian** is $H=\sum_\mu p_\mu\partial/\partial R_\mu\,\xi-\mathcal{L}$, a function of the field and the four momenta. For the scalar field the polymomentum is the gradient, $p_\mu=\partial/\partial R_\mu\xi$, and the De Donder–Weyl Hamiltonian is $\frac12\sum_\mu p_\mu p_\mu+\frac12k_m^{2}\xi^2$, so the covariant equations

$$
\partial/\partial R_\mu\,\xi=\frac{\partial H}{\partial p_\mu},
\qquad
\sum_\mu\partial/\partial R_\mu\,p_\mu=-\frac{\partial H}{\partial\xi}
$$

are the four-fold statement of the Klein–Gordon equation. Nothing is singled out and nothing is split, which is the formalism's virtue and its price: there is no unique pairing of the momenta with a single time, so there is **no covariant Poisson bracket**. The bracket of this article is the instantaneous one, and it exists because a time direction was chosen. The polymomentum formalism is the multisymplectic one; its geometry, its relation to the instantaneous formalism, and the theorem that its equations agree with the Euler–Lagrange equations for a hyperregular density belong to the mathematical corpus, in *Multisymplectic and Covariant Hamiltonian Field Theory*, and the present article only records the point of contact: the instantaneous Hamiltonian density is the time component of the conserved multimomentum current of the covariant formalism, $\mathcal{H}=J_{00}$, which is why the two descriptions agree on the energy.

## What the Transcription Does and Does Not Give

What the algebra gives the Hamiltonian field theory is short and definite.

- **The Hamiltonian density is a Hermitian form.** The kinetic, gradient and mass contributions are each the scalar part of a form built from the field and its gradient, and the assembled density is $\mathrm{Sc}[(\tilde\nabla_\Phi\tilde{Ξ})^{*}(\tilde\nabla_\Phi\tilde{Ξ})]+k_m^{2}\mathrm{Sc}[\tilde{Ξ}^{*}\tilde{Ξ}]$. The form is the algebra's own Hermitian pairing, not a transcription of a foreign object, and the $i r'_t$ convention makes its kinetic term positive.
- **The energy density and the flux are one sector element.** They are the scalar and vector parts of the Hermitian biquaternion $\tilde W_{\Psi}=\mathcal{H}e_t+\frac{i}{c}\vec S\in\mathbb{B}_{\Psi}$, with $\tilde\nabla_\Phi\tilde W_{\Psi}=0$ on shell — the same element, in the same sector and the same arrangement, that the electromagnetic field's energy–momentum occupies.
- **The sector split is the energy–charge split.** The two real scalars in the two sectors' scalar directions contribute to the energy with the same sign and to the charge with opposite signs, and the split of the density is the field version of the phase-space biquaternion's real and imaginary parts.

What the algebra does not give, and what a reader should not expect, is a modification of the bracket. The scalar field is central, its conjugate momentum is central, and the bracket on functionals of the pair is the standard one; the Jacobi identity holds for the same local reason it holds for a finite system, and no algebraic anomaly appears. The interesting brackets — those in which the algebra's non-commutativity and the sector structure are load-bearing — are those of the fields that carry an index, and those lie beyond the scalar case: the Dirac field on the spinor module, whose conjugate momentum is constrained, and the gauge fields, whose conjugate momenta are constrained and which are naturally described in the covariant formalism named above. The scalar field is the case in which the Hamiltonian transcription is complete and uninteresting, which is exactly why it is the case in which the classical canonical structure can be handed to the quantization article untouched.

## Summary

The Hamiltonian field theory of the central scalar field is built from three objects.

**The conjugate momentum and the density.** The momentum field is $\pi=\left(\partial\xi/\partial r'_t\right)^{\,*}$ and its conjugate $\pi^\dagger=\partial\xi/\partial r'_t$; the Legendre transform is regular, so the phase space is unconstrained. The Hamiltonian density is $\mathcal{H}=\pi\partial\xi/\partial r'_t+\pi^\dagger\left(\partial\xi/\partial r'_t\right)^{\,*}-\mathcal{L}=|\partial\xi/\partial r'_t|^2+|\nabla\xi|^2+k_m^{2}|\xi|^2$, which is not minus the Lagrangian density and is the energy density $T_{00}$ of the translation current. In the algebra it is the Hermitian form $\mathcal{H}=\mathrm{Sc}[(\tilde\nabla_\Phi\tilde{Ξ})^{*}(\tilde\nabla_\Phi\tilde{Ξ})]+k_m^{2}\mathrm{Sc}[\tilde{Ξ}^{*}\tilde{Ξ}]$, positive because the $i r'_t$ convention puts the kinetic term in with a plus.

**The equations and the bracket.** Hamilton's field equations, $\partial\xi/\partial r'_t=\delta H/\delta\pi^\dagger$ and $\partial\pi/\partial r'_t=-\delta H/\delta\xi^\dagger$, are the Klein–Gordon equation; the field Poisson bracket is the integral over space of the local canonical bracket, with $\{\xi(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z),\pi(\vec y)\}=\delta^3(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z-\vec y)$, and its Jacobi identity is inherited locally from the canonical pair. The density satisfies the continuity equation $\partial/\partial r'_t\mathcal{H}+\nabla\cdot\vec S=0$ with flux $\vec S=-(\left(\partial\xi/\partial r'_t\right)^{\,*}\nabla\xi+\partial\xi/\partial r'_t\nabla\xi^{\,*})=-c^2(\pi\nabla\xi+\pi^\dagger\nabla\xi^{\,*})$, positive-directed along the wavevector for a plane wave.

**The packaging and the sector interpretation.** Density and flux are the scalar and vector parts of the Hermitian biquaternion $\tilde W_{\Psi}=\mathcal{H}e_t+\frac{i}{c}\vec S\in\mathbb{B}_{\Psi}$, with $\tilde\nabla_\Phi\tilde W_{\Psi}=0$ on shell — the electromagnetic arrangement. Splitting the central field into its two sector scalars, the energy is the sum of the two sectors' kinetic, gradient and mass terms with the same sign, whereas the charge is their difference with opposite signs.

The formalism is the instantaneous one. The covariant formalism treats the four derivatives alike, conjugates to the field a quadruple of polymomenta, and has no unique bracket and no unique pairing with a time; it is the multisymplectic geometry of the mathematical corpus, and the instantaneous density is its time component.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde{Ξ}=\xi\,e_t$ | The central scalar field, $\xi:\mathbb{R}^{1,3}\to\mathbb{C}$, $\tilde R_\Phi=i r'_t\,e_t+r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z\in\mathbb{B}_{\Phi}$ |
| $\mathcal{L}=|\partial\xi/\partial r'_t|^2-|\nabla\xi|^2-k_m^{2}|\xi|^2$ | The Lagrangian density, the sign fixed by *Noether's Theorem in Biquaternionic Form* |
| $1/k_m$ | The mass length, $\hbar/(mc)$; its reciprocal $k_m=mc/\hbar$ is the inverse reduced Compton wavelength, the mass parameter of the Klein–Gordon equation |
| $\pi=\partial\mathcal{L}/\partial\left(\partial\xi/\partial r'_t\right)=\left(\partial\xi/\partial r'_t\right)^{\,*}$ | The conjugate momentum field, and $\pi^\dagger=\partial\xi/\partial r'_t$ its conjugate |
| $\tilde\Pi=\pi\,e_t\in\mathbb{B}_{C}$ | The conjugate momentum field as a central biquaternion |
| $\mathcal{H}=\pi\partial\xi/\partial r'_t+\pi^\dagger\left(\partial\xi/\partial r'_t\right)^{\,*}-\mathcal{L}$ | The Hamiltonian density; it is $|\partial\xi/\partial r'_t|^2+|\nabla\xi|^2+k_m^{2}|\xi|^2$ and equals the energy density $T_{00}$ |
| $H=\int\mathcal{H}\,d^3r$ | The total Hamiltonian |
| $\mathcal{H}=\mathrm{Sc}[(\tilde\nabla_\Phi\tilde{Ξ})^{*}(\tilde\nabla_\Phi\tilde{Ξ})]+k_m^{2}\mathrm{Sc}[\tilde{Ξ}^{*}\tilde{Ξ}]$ | The Hamiltonian density as the sum of two Hermitian forms |
| $\{\xi(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z),\pi(\vec y)\}=\delta^3(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z-\vec y)$ | The canonical field bracket, with the mirrored brackets for the conjugates |
| $\{A,B\}$ | The field Poisson bracket on functionals, the integral over space of the local canonical bracket |
| $\vec S=-(\left(\partial\xi/\partial r'_t\right)^{\,*}\nabla\xi+\partial\xi/\partial r'_t\nabla\xi^{\,*})=-c^2(\pi\nabla\xi+\pi^\dagger\nabla\xi^{\,*})$ | The energy flux; $\partial/\partial r'_t\mathcal{H}+\nabla\cdot\vec S=0$ |
| $\tilde W_{\Psi}=\mathcal{H}e_t+\frac{i}{c}\vec S\in\mathbb{B}_{\Psi}$ | The energy–momentum biquaternion of the field, with $\tilde\nabla_\Phi\tilde W_{\Psi}=0$ on shell |
| $p_\mu=\partial\mathcal{L}/\partial(\partial/\partial R_\mu\,\xi)=\partial/\partial R_\mu\xi$ | The polymomentum of the covariant (De Donder–Weyl) formalism |
| $H_{DW}=\sum_\mu p_\mu\partial/\partial R_\mu\,\xi-\mathcal{L}=\frac12\sum_\mu p_\mu p_\mu+\frac12k_m^{2}\xi^2$ | The De Donder–Weyl Hamiltonian of the scalar field |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2)$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{\natural}=\langle\tilde{Q}_2\rangle_{\natural}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |

## Further Reading

- H. Goldstein, C. P. Poole and J. L. Safko, *Classical Mechanics* (3rd ed., Addison-Wesley, 2002), for the continuum Lagrangian, the field Hamiltonian and the transition from the discrete to the continuous phase space.
- L. D. Landau and E. M. Lifshitz, *The Classical Theory of Fields* (4th ed., Pergamon, 1975), for the canonical energy–momentum tensor and the energy density of the scalar field.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I: Foundations* (Cambridge, 1995), for the canonical formalism, the equal-time brackets and the constraint analysis of the gauge field.
- James D. Bjorken and Sidney D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the scalar-field canonical quantization and the Klein–Gordon momentum field.
- Paul A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for the first-class and second-class constraint analysis of the Maxwell and Dirac fields.
- Jerrold E. Marsden and Tudor S. Ratiu, *Introduction to Mechanics and Symmetry* (2nd ed., Springer, 1999), for the field-theoretic Poisson bracket and its relation to the multisymplectic structure.
- Mark J. Gotay, James Isenberg, Jerrold E. Marsden and Richard Montgomery, "Momentum maps and classical relativistic fields," *Physics Reports* (2004), for the covariant Hamiltonian formalism of field theory and the polymomentum.
- [Lagrangian and Hamiltonian Mechanics in Biquaternionic Form](lagrangian-and-hamiltonian-mechanics-in-biquaternionic-form.html), companion article, for the finite-dimensional Legendre transform, the phase-space biquaternion and the bracket that this article extends to a density.
- [The Action Principle and the Classical Limit as Stationary Phase in Biquaternionic Form](the-action-principle-and-the-classical-limit-as-stationary-phase-in-biquaternionic-form.html), companion article, for the action, its first variation and the boundary term.
- [Noether's Theorem in Biquaternionic Form](noethers-theorem-in-biquaternionic-form.html), companion article, for the Lagrangian density and the canonical energy–momentum tensor.
- [Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form](stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.html), companion article, for the energy–momentum biquaternion of the electromagnetic field and the conservation law for field and matter.
- [Canonical Quantization of the Biquaternion Klein–Gordon Field](canonical-quantization-of-the-biquaternion-klein-gordon-field.html), companion article, for the quantization of the classical structure built here.
- [Multisymplectic and Covariant Hamiltonian Field Theory](../articles_maths/multisymplectic-and-covariant-hamiltonian-field-theory.html), companion article in the mathematical corpus, for the polymomentum, the De Donder–Weyl equations and the multisymplectic form.
