# __Hamiltonian Field Theory in Biquaternionic Form__

## Introduction

The companion article *Lagrangian and Hamiltonian Mechanics in Biquaternionic Form* ends where the finite-dimensional theory ends: one configuration biquaternion $\tilde q$, one momentum biquaternion $\tilde p$, one phase-space biquaternion $\tilde q+i\tilde p$, and a Poisson bracket on the functions of that finite collection of numbers. A field is not a finite collection of numbers. Its configuration is a *function* of the position, and the variational derivative replaces the partial derivative: the Legendre transform acts on a density, the momentum conjugate to the field is itself a function of the position, and the bracket that survives is a bracket on functionals. This article performs that transcription for the field the corpus actually uses — the central scalar field of the Klein–Gordon articles — and states plainly what the algebra supplies and what it does not.

Two objects are built here, and they answer two different questions. The first is the **Hamiltonian density** $\mathcal H$, the Legendre transform of the Lagrangian density, which is also the energy density of the companion article on stress–energy; the second is the **field Poisson bracket**, the bracket on functionals of the field and its conjugate momentum, together with the continuity equation that the density satisfies along the motion. Their sum is the classical Hamiltonian field theory in biquaternion form. The article then says where the algebra's contribution stops: for a central field the bracket is the standard one, and the biquaternion content is the packaging of the density and the flux rather than a change of the bracket. The genuinely different Hamiltonian formalism for a field — the covariant one, in which the conjugate object is a *quadruple* of momenta rather than one momentum field — is named at the end and developed in the mathematical corpus.

The conventions are those of the read list. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, $e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$; $i$ is central with $i^2=-1$; the conjugations are $\bar{\cdot}$ (quaternion), ${}^*$ (complex), and $\dagger=\bar{\cdot}^{\,*}$ (Hermitian); $\mathbb{M}_-$ and $\mathbb{M}_+$ are the anti-Hermitian and Hermitian sectors, the material and informational ones. The material coordinate is $\tilde Q=ict\,e_0+\mathbf{x}$, the $ict$ metric is $\eta=\mathrm{diag}(-1,+1,+1,+1)$, and the d'Alembertian is $\Box=\tilde\nabla\bar{\tilde\nabla}=\partial_{ict}^2+\Delta$. The central scalar field is $\tilde\Phi(\tilde Q)=\phi(\tilde Q)e_0$ with $\tilde Q\in\mathbb{M}_-$, its Lagrangian density is the one fixed by *Noether's Theorem in Biquaternionic Form* and used by *Canonical Quantization of the Biquaternion Klein–Gordon Field*,

$$
\mathcal{L}=-\mathrm{Sc}\!\left[(\bar{\tilde\nabla}\tilde\Phi^\dagger)(\tilde\nabla\tilde\Phi)\right]-\mu^2\,\mathrm{Sc}\!\left[\tilde\Phi^\dagger\tilde\Phi\right]
=\frac{1}{c^2}|\dot\phi|^2-|\nabla\phi|^2-\mu^2|\phi|^2,
\qquad \mu=\frac{mc}{\hbar},
$$

and the equation of motion is $\left(\Box-\mu^2\right)\tilde\Phi=0$, that is $\ddot\phi=c^2(\Delta\phi-\mu^2\phi)$.

The companion articles are:

- Companion article *Lagrangian and Hamiltonian Mechanics in Biquaternionic Form*, for the finite-dimensional Legendre transform, the phase-space biquaternion and the Poisson bracket that this article extends to a density.
- Companion article *The Action Principle and the Classical Limit as Stationary Phase in Biquaternionic Form*, for the action and its first variation, and for the boundary term that the field case reproduces as a flux.
- Companion article *Noether's Theorem in Biquaternionic Form*, for the Lagrangian density, the conserved currents, and the canonical energy–momentum tensor.
- Companion article *Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form*, for the energy–momentum biquaternion and the electromagnetic packaging that the scalar field's density and flux repeat.
- Companion article *Canonical Quantization of the Biquaternion Klein–Gordon Field*, for the quantum theory that takes this classical canonical structure over without modification, and for the constraint analysis of the Dirac and Maxwell fields that this article contrasts with.

## The Standard Hamiltonian Field Theory

### The Conjugate Momentum Field

The Legendre transform of a field theory is performed pointwise in the position and acts on the Lagrangian *density*. Write $\dot\phi=\partial_t\phi$ and define the **conjugate momentum field** by the partial derivative of the density with respect to the velocity field,

$$
\pi=\frac{\partial\mathcal{L}}{\partial\dot\phi}=\frac{1}{c^2}\dot\phi^{\,*},
\qquad
\pi^\dagger=\frac{\partial\mathcal{L}}{\partial\dot\phi^{\,*}}=\frac{1}{c^2}\dot\phi .
$$

The second formula is the conjugate of the first, and both are needed because the field is complex; on the real field $\phi=\phi^*$ the two agree. The transform is **regular**: $\pi$ determines $\dot\phi$ and conversely, since $\dot\phi=c^2\pi^\dagger$, so the phase space of the theory is the full space of pairs $(\phi,\pi)$ at each position and there is no constraint. This is the first structural fact of the transcription, and it is the point at which the scalar field differs from the two fields whose quantization the corpus treats alongside it. The Dirac field, being first order in time, carries a second-class constraint $\pi-i\psi^\dagger\approx0$; the Maxwell field, being a gauge field, carries the two first-class constraints $\pi^0\approx0$ and $\mathrm{div}\,\boldsymbol\pi\approx0$; the scalar field carries neither. A regular Legendre transform is what makes the phase space unconstrained, and an unconstrained phase space is what makes the Hamiltonian transcription a transposition with nothing added.

### The Hamiltonian Density

The Legendre transform of the density is the **Hamiltonian density**

$$
\mathcal{H}=\pi\dot\phi+\pi^\dagger\dot\phi^{\,*}-\mathcal{L},
$$

and the **total Hamiltonian** is its integral over space, $H=\int\mathcal{H}\,d^3x$. Substituting the density and the momentum field gives

$$
\mathcal{H}=\frac{1}{c^2}|\dot\phi|^2+|\nabla\phi|^2+\mu^2|\phi|^2,
$$

the sum of three squares. Two remarks fix the sign bookkeeping. First, **the Hamiltonian density is not minus the Lagrangian density**, although it is so for a mechanical Lagrangian whose kinetic energy is quadratic in the velocities: here $-\mathcal{L}=\frac{1}{c^2}|\dot\phi|^2-|\nabla\phi|^2-\mu^2|\phi|^2$, which differs from $\mathcal{H}$ by the kinetic term again, since the Legendre transform of a complex field pairs $\pi$ with $\dot\phi$ *and* $\pi^\dagger$ with $\dot\phi^*$. Second, **the density is the energy density**: the expression above is exactly the time–time component $T^0{}_0$ that *Noether's Theorem in Biquaternionic Form* obtains from translation invariance, positive because it is a sum of squares. The Hamiltonian of the field and the energy of the field are the same functional, and that is not a coincidence of the conventions but the content of the Legendre transform for a Lagrangian with no explicit time dependence.

**Verification.** At the event $t=0.7$, $\mathbf{x}=(0.31,-0.47,0.23)$, with $c=2$, $\mu=1.1$, and $\phi$ a superposition of three on-shell plane waves of wavevectors $(1.3,0.2,-0.5)$, $(-0.9,0.4,0.1)$, $(0.6,0.6,-0.3)$ and complex amplitudes $1.0+0.3i$, $0.7-0.2i$, $-0.5+0.4i$, the equation of motion had residual $1.8\times10^{-15}$; the direct evaluation of $\mathcal{H}$ and its evaluation from the Legendre transform $\pi\dot\phi+\pi^\dagger\dot\phi^*-\mathcal{L}$ agreed to the last bit $(6.684439532033879)$; and $-\mathcal{L}$ was $-1.3880$, below $\mathcal{H}$ by $2c^{-2}|\dot\phi|^2=8.0724$ as the remark requires. The superposition is used rather than a single plane wave because the cross terms are what a sign error in the Legendre transform would disturb.

### The Hamiltonian Field Equations

Hamilton's equations for the field are the pair

$$
\dot\phi=\frac{\delta H}{\delta\pi^\dagger}=c^2\pi^\dagger,
\qquad
\dot\pi=-\frac{\delta H}{\delta\phi^\dagger}=-c^2(\Delta\phi-\mu^2\phi),
$$

where $\delta/\delta$ is the variational derivative and the second equation uses the first to eliminate $\pi$. Eliminating $\pi$ between them returns $\ddot\phi=c^2(\Delta\phi-\mu^2\phi)$, the Klein–Gordon equation: the Hamiltonian field equations and the Euler–Lagrange equation are the same equations, exactly as in the finite-dimensional case. The only new feature is that the conjugate equation is a *PDE for a density* rather than an ODE for a number, and the variational derivative is what makes the pairing between them work.

### The Field Poisson Bracket

The bracket of the finite-dimensional theory is replaced by a bracket on functionals. For functionals $A[\phi,\pi]$, $B[\phi,\pi]$ of the field and its conjugate momentum,

$$
\{A,B\}=\int d^3x\left(
\frac{\delta A}{\delta\phi}\frac{\delta B}{\delta\pi}
+\frac{\delta A}{\delta\phi^{\,*}}\frac{\delta B}{\delta\pi^\dagger}
-\frac{\delta A}{\delta\pi}\frac{\delta B}{\delta\phi}
-\frac{\delta A}{\delta\pi^\dagger}\frac{\delta B}{\delta\phi^{\,*}}
\right),
$$

so that the canonical brackets are the distributional relations

$$
\{\phi(\mathbf{x}),\pi(\mathbf{y})\}=\delta^3(\mathbf{x}-\mathbf{y}),
\qquad
\{\phi(\mathbf{x}),\phi(\mathbf{y})\}=\{\pi(\mathbf{x}),\pi(\mathbf{y})\}=0,
$$

with the conjugates carrying the mirrored signs. The bracket is antisymmetric and satisfies the Jacobi identity, and it does so **locally**: the Jacobi sum of three functionals is an integral of a sum of terms each of which is the Jacobi sum of the corresponding local expression in $(\phi,\pi)$ at a point, which vanishes because the finite-dimensional bracket of the canonical pair vanishes. The field bracket is therefore not a new algebraic structure; it is the same bracket applied at every point and integrated, and the delta functions are the statement that distinct points do not interact through the bracket. The Hamiltonian flow of the total Hamiltonian along the bracket is the field equation: for any functional $A$, $\dot A=\{A,H\}$, which on the canonical pair returns the pair of equations above.

### The Continuity Equation and the Energy Flux

The energy density is conserved along the motion by a local conservation law. Differentiating $\mathcal{H}$ in time and using the equation of motion gives

$$
\partial_t\mathcal{H}+\nabla\cdot\mathbf{S}=0,
\qquad
\mathbf{S}=-(\dot\phi^{\,*}\nabla\phi+\dot\phi\,\nabla\phi^{\,*})=-c^2(\pi\nabla\phi+\pi^\dagger\nabla\phi^{\,*});
$$

the mass terms cancel between the time derivative of $\mu^2|\phi|^2$ and the equation of motion, and the surviving terms are a divergence. The vector $\mathbf{S}$ is the **energy flux**. For a single plane wave $\phi=\phi_0e^{i(\mathbf{k}\cdot\mathbf{x}-\omega t)}$ one has $\mathbf{S}=2\omega\mathbf{k}|\phi_0|^2$, directed along the wavevector, so the energy travels the way the wave travels. Integrating the conservation law over a volume and using the vanishing of the flux at infinity makes the four-momentum

$$
P_\nu=\frac{1}{c}\int T_{0\nu}\,d^3x
$$

time-independent, the statement that the flux of the companion stress–energy article is a conserved current.

**Verification.** On the same on-shell superposition as above, the flux $\mathbf{S}$ computed from $\dot\phi$ and $\nabla\phi$ and the time derivative $\partial_t\mathcal{H}$ computed analytically gave $\nabla\cdot\mathbf{S}=1.6415626452868701$ and $-\partial_t\mathcal{H}=1.6415626452868741$, a residual of $4.0\times10^{-15}$. The cancellation is a genuine test of the mass-term bookkeeping: dropping the equation of motion, or flipping the sign of the mass term, leaves the $\mu^2$ contributions uncancelled and the residual at order unity.

## The Biquaternionic Transcription

### The Field and Its Conjugate Momentum

The field is central-valued, $\tilde\Phi=\phi e_0$, and its conjugate momentum is central-valued for the same reason: the momentum field is obtained from the field by a central operation, so it lives in the centre. Writing

$$
\tilde\Pi=\pi e_0\in\mathbb{C}_{\mathbb{B}},
$$

the pair $(\tilde\Phi,\tilde\Pi)$ is the field-theoretic analogue of the pair $(\tilde q,\tilde p)$ of the finite-dimensional article, with one difference that is worth stating: $\tilde q$ was a real quaternion in $\mathbb{H}_{\mathbb{B}}$ and $\tilde p$ its conjugate momentum in the same subspace, while $\tilde\Phi$ and $\tilde\Pi$ are central, in $\mathbb{C}_{\mathbb{B}}$. The value space is smaller because the spin of the field is zero. A field that carried a spinor index would take its values in the spinor module, and its conjugate momentum would carry the same index; the central scalar is the case in which the index is absent, and in that case the momentum field is a second complex number at each point rather than a second biquaternion.

### The Hamiltonian Density as a Hermitian Bilinear

The density is the sum of two Hermitian forms. With $\tilde\nabla\tilde\Phi$ the biquaternionic gradient of the field — its four coefficients are the four partial derivatives, $(\partial_{ict}\phi,\partial_1\phi,\partial_2\phi,\partial_3\phi)$ —

$$
\boxed{\;\mathcal{H}=\mathrm{Sc}\!\left[(\tilde\nabla\tilde\Phi)^\dagger(\tilde\nabla\tilde\Phi)\right]+\mu^2\,\mathrm{Sc}\!\left[\tilde\Phi^\dagger\tilde\Phi\right].\;}
$$

The second term is the mass form, positive and central. The first is the **kinetic-plus-gradient form**, and the identity $\mathrm{Sc}[(\tilde\nabla\tilde\Phi)^\dagger(\tilde\nabla\tilde\Phi)]=c^{-2}|\dot\phi|^2+|\nabla\phi|^2$ is where the $ict$ convention does its quiet work: the time coefficient of the gradient is $\partial_{ict}\phi=-ic^{-1}\dot\phi$, so $|\partial_{ict}\phi|^2=c^{-2}|\dot\phi|^2$ and the kinetic term is *positive*, not negative. This is the same sign that makes the norm of a material four-vector have signature $(3,1)$ and the d'Alembertian $\Box=\partial_{ict}^2+\Delta$; a reader who computes $|\partial_{ict}\phi|^2$ as $-\frac{1}{c^2}|\dot\phi|^2$ has conjugated the operator instead of the field, and will find the kinetic energy negative. The form $\tilde X^\dagger\tilde X$ is of course positive definite on the algebra — that is the Hermitian form of $\mathbb{M}_+$ — and it is *this* form, not the holomorphic norm $N(\tilde X)=\tilde X\bar{\tilde X}$ of signature $(3,1)$, that the energy density uses. The distinction matters: the norm's vanishing set is the light cone, the Hermitian form's is only the origin.

**Verification.** On the same superposition the biquaternion expression and the component expression $c^{-2}|\dot\phi|^2+|\nabla\phi|^2+\mu^2|\phi|^2$ agreed exactly, $6.684439532033879$ both ways, with the scalar part evaluated through the $2\times2$ matrix representation $\Phi$ of the conventions article; the check confirms the sign of the $ict$ term and the reality of each form.

### The Energy–Momentum Biquaternion

The density and the flux are the scalar and vector parts of one Hermitian biquaternion:

$$
\tilde W=\mathcal{H}\,e_0+\frac{i}{c}\mathbf{S}\in\mathbb{M}_+,
\qquad
\tilde\nabla\tilde W=0
\ \ \text{on shell}.
$$

The scalar part of the biquaternion divergence is the continuity equation. This is the *same packaging* that the companion article on stress–energy gives the electromagnetic field, $\tilde W=\frac{1}{2}\tilde F\tilde F^\dagger=W\,e_0+\frac{i}{c}\mathbf{S}$, whose scalar part is the Poynting theorem; the scalar field's energy density sits in the scalar direction of the informational sector and its flux in the three vector directions $ie_k$, so the two fields' energy–momentum biquaternions are elements of the same sector in the same arrangement. The one difference is that the electromagnetic $\tilde W$ is bilinear in the field strength whereas the scalar $\tilde W$ is bilinear in the gradient of the field, which is the field-theoretic way of saying that the scalar field carries no spin and its energy comes entirely from the derivatives.

The static limit makes the arrangement visible. For a time-independent field the flux vanishes, $\tilde W=\mathcal{H}e_0$, and the conservation law reduces to $\nabla\cdot\mathbf{S}=0$, which is empty; the energy is conserved trivially. For a running wave it is the other way: $\mathcal{H}$ and $|\mathbf{S}|/c$ are equal and the biquaternion has the null-field pattern of a single travelling wave, exactly as the companion stress–energy article records for the massless scalar and for the electromagnetic wave.

### The Brackets in the Algebra

The canonical bracket is read in the algebra as the scalar part of a pairing. Since $\phi$ and $\pi$ are the coefficients of central elements, the bracket of the algebra's central directions is the bracket of the two complex numbers, and the field bracket above is its integral over space. The biquaternion content of the brackets is therefore not a new bracket but the **sector bookkeeping** of the fields being bracketed: $\tilde\Phi\in\mathbb{C}_{\mathbb{B}}$ while its time derivative is not, and the momentum $\tilde\Pi$ is central whereas the momentum of a bivector-valued field would lie in $\mathbb{M}_-$ or $\mathbb{M}_+$. The scalar field brackets with itself in the centre, and this is the classical face of the fact, recorded by the quantization article, that the scalar field's canonical structure is taken over from the classical theory without modification.

## The Sector Reading of the Hamiltonian Density

The field of spin zero is the field of the centre, and the centre is the direct sum of the two sectors' scalar lines, $\mathbb{C}_{\mathbb{B}}=T_{\mathrm i}\oplus T_{\mathrm m}$ with $T_{\mathrm i}=\mathbb{R}e_0$ and $T_{\mathrm m}=\mathbb{R}(ie_0)$. Writing the complex scalar as two real scalars, one in each sector's scalar direction,

$$
\tilde\Phi=\frac{1}{\sqrt2}\left(\underbrace{\phi_1\,e_0}_{\in\,\mathbb{M}_+}+\underbrace{\phi_2\,ie_0}_{\in\,\mathbb{M}_-}\right),
\qquad
\mathrm{Sc}\!\left[\tilde\Phi^\dagger\tilde\Phi\right]=\frac12\left(\phi_1^2+\phi_2^2\right),
$$

the Hamiltonian density splits accordingly,

$$
\mathcal{H}=\frac12\left[
\frac{1}{c^2}\left(\dot\phi_1^2+\dot\phi_2^2\right)
+|\nabla\phi_1|^2+|\nabla\phi_2|^2
+\mu^2\left(\phi_1^2+\phi_2^2\right)
\right],
$$

the sum of the two sectors' kinetic, gradient and mass terms. Three features of this split are the ones the informational articles use. First, **both sectors contribute to the energy with the same sign**, so the energy is positive whichever sector carries the field. Second, the split is not the charge: the energy is the sum of the sector contributions, positive definite, whereas the charge is the pairing of the two sectors' fields that is antisymmetric in them, $j^0\propto\mathrm{Im}(\phi^*\dot\phi)\propto\phi_1\dot\phi_2-\phi_2\dot\phi_1$, and its sign is not fixed. The same two readings appear in the phase-space biquaternion of the companion symplectic article as the real and imaginary parts of the Hermitian pairing: the real part is the metric and is additive over the sectors, the imaginary part is the symplectic form and is antisymmetric. Third, **the split is a split of the kinetic and gradient terms as well as the mass term**, so the sector exchange that the oscillator article realises as a quarter-period advance is, in the field, an exchange of the two real scalars at every point.

**Verification.** With $\phi_1$ a superposition of three real on-shell modes and $\phi_2$ a superposition of two, so that both sectors are occupied, $\mathrm{Sc}[\tilde\Phi^\dagger\tilde\Phi]$ and $\frac12(\phi_1^2+\phi_2^2)$ agreed exactly, and the biquaternion density agreed with the component form above to $4.4\times10^{-16}$ at the event used throughout. Two-sector superpositions are used because with a single real scalar the split is invisible: the cross-sector terms that the check exercises vanish when one sector is empty.

## Covariant Hamiltonian Field Theory

The formalism so far is the **instantaneous** one: it singles out a time direction, differentiates with respect to it, and conjugate to the field there is one momentum field. It is the formalism in which the equal-time brackets of the quantization article are written, and it is the one in which the constraint analysis of the gauge field can be performed at all. It is not, however, the only Hamiltonian formalism for a field, and its relation to the covariant one is worth stating here because the gauge fields' Hamiltonian structure lives on the other side.

In the **covariant** formalism, all four derivatives of the field are treated on the same footing and conjugate to the field there is a *quadruple* of momenta, the **polymomentum** $p^\mu=\partial\mathcal{L}/\partial(\partial_\mu\phi)$, one per direction of differentiation. The Legendre transform is performed on the quadruple, and the resulting **De Donder–Weyl Hamiltonian** is $H=p^\mu\partial_\mu\phi-\mathcal{L}$, a function of the field and the four momenta. For the scalar field the polymomentum is the gradient, $p^\mu=\partial^\mu\phi$, and the De Donder–Weyl Hamiltonian is $\frac12p^\mu p_\mu+\frac12\mu^2\phi^2$, so the covariant equations

$$
\partial_\mu\phi=\frac{\partial H}{\partial p^\mu},
\qquad
\partial_\mu p^\mu=-\frac{\partial H}{\partial\phi}
$$

are the four-fold statement of the Klein–Gordon equation. Nothing is singled out and nothing is split, which is the formalism's virtue and its price: there is no unique pairing of the momenta with a single time, so there is **no covariant Poisson bracket**. The bracket of this article is the instantaneous one, and it exists because a time direction was chosen. The polymomentum formalism is the multisymplectic one; its geometry, its relation to the instantaneous formalism, and the theorem that its equations agree with the Euler–Lagrange equations for a hyperregular density belong to the mathematical corpus, in *Multisymplectic and Covariant Hamiltonian Field Theory*, and the present article only records the point of contact: the instantaneous Hamiltonian density is the time component of the conserved multimomentum current of the covariant formalism, $\mathcal{H}=J^0{}_0$, which is why the two descriptions agree on the energy.

## What the Transcription Does and Does Not Give

What the algebra gives the Hamiltonian field theory is short and definite.

- **The Hamiltonian density is a Hermitian form.** The kinetic, gradient and mass contributions are each the scalar part of a form built from the field and its gradient, and the assembled density is $\mathrm{Sc}[(\tilde\nabla\tilde\Phi)^\dagger(\tilde\nabla\tilde\Phi)]+\mu^2\mathrm{Sc}[\tilde\Phi^\dagger\tilde\Phi]$. The form is the algebra's own Hermitian pairing, not a transcription of a foreign object, and the $ict$ convention makes its kinetic term positive.
- **The energy density and the flux are one sector element.** They are the scalar and vector parts of the Hermitian biquaternion $\tilde W=\mathcal{H}e_0+\frac{i}{c}\mathbf{S}\in\mathbb{M}_+$, with $\tilde\nabla\tilde W=0$ on shell — the same element, in the same sector and the same arrangement, that the electromagnetic field's energy–momentum occupies.
- **The sector split is the energy–charge split.** The two real scalars in the two sectors' scalar directions contribute to the energy with the same sign and to the charge with opposite signs, and the split of the density is the field version of the phase-space biquaternion's real and imaginary parts.

What the algebra does not give, and what a reader should not expect, is a modification of the bracket. The scalar field is central, its conjugate momentum is central, and the bracket on functionals of the pair is the standard one; the Jacobi identity holds for the same local reason it holds for a finite system, and no algebraic anomaly appears. The interesting brackets — those in which the algebra's non-commutativity and the sector structure are load-bearing — are those of the fields that carry an index, and those lie beyond the scalar case: the Dirac field on the spinor module, whose conjugate momentum is constrained, and the gauge fields, whose conjugate momenta are constrained and which are naturally described in the covariant formalism named above. The scalar field is the case in which the Hamiltonian transcription is complete and uninteresting, which is exactly why it is the case in which the classical canonical structure can be handed to the quantization article untouched.

## Summary

The Hamiltonian field theory of the central scalar field is built from three objects.

**The conjugate momentum and the density.** The momentum field is $\pi=c^{-2}\dot\phi^{\,*}$ and its conjugate $\pi^\dagger=c^{-2}\dot\phi$; the Legendre transform is regular, so the phase space is unconstrained. The Hamiltonian density is $\mathcal{H}=\pi\dot\phi+\pi^\dagger\dot\phi^{\,*}-\mathcal{L}=c^{-2}|\dot\phi|^2+|\nabla\phi|^2+\mu^2|\phi|^2$, which is not minus the Lagrangian density and is the energy density $T^0{}_0$ of the translation current. In the algebra it is the Hermitian form $\mathcal{H}=\mathrm{Sc}[(\tilde\nabla\tilde\Phi)^\dagger(\tilde\nabla\tilde\Phi)]+\mu^2\mathrm{Sc}[\tilde\Phi^\dagger\tilde\Phi]$, positive because the $ict$ convention puts the kinetic term in with a plus.

**The equations and the bracket.** Hamilton's field equations, $\dot\phi=\delta H/\delta\pi^\dagger$ and $\dot\pi=-\delta H/\delta\phi^\dagger$, are the Klein–Gordon equation; the field Poisson bracket is the integral over space of the local canonical bracket, with $\{\phi(\mathbf{x}),\pi(\mathbf{y})\}=\delta^3(\mathbf{x}-\mathbf{y})$, and its Jacobi identity is inherited locally from the canonical pair. The density satisfies the continuity equation $\partial_t\mathcal{H}+\nabla\cdot\mathbf{S}=0$ with flux $\mathbf{S}=-(\dot\phi^{\,*}\nabla\phi+\dot\phi\nabla\phi^{\,*})=-c^2(\pi\nabla\phi+\pi^\dagger\nabla\phi^{\,*})$, positive-directed along the wavevector for a plane wave.

**The packaging and the sector reading.** Density and flux are the scalar and vector parts of the Hermitian biquaternion $\tilde W=\mathcal{H}e_0+\frac{i}{c}\mathbf{S}\in\mathbb{M}_+$, with $\tilde\nabla\tilde W=0$ on shell — the electromagnetic arrangement. Splitting the central field into its two sector scalars, the energy is the sum of the two sectors' kinetic, gradient and mass terms with the same sign, whereas the charge is their difference with opposite signs.

The formalism is the instantaneous one. The covariant formalism treats the four derivatives alike, conjugates to the field a quadruple of polymomenta, and has no unique bracket and no unique pairing with a time; it is the multisymplectic geometry of the mathematical corpus, and the instantaneous density is its time component.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Phi=\phi\,e_0$ | The central scalar field, $\phi:\mathbb{R}^{1,3}\to\mathbb{C}$, $\tilde Q=ict\,e_0+\mathbf{x}\in\mathbb{M}_-$ |
| $\mathcal{L}=\frac{1}{c^2}|\dot\phi|^2-|\nabla\phi|^2-\mu^2|\phi|^2$ | The Lagrangian density, the sign fixed by *Noether's Theorem in Biquaternionic Form* |
| $\mu=mc/\hbar$ | The inverse reduced Compton wavelength, the mass parameter of the Klein–Gordon equation |
| $\pi=\partial\mathcal{L}/\partial\dot\phi=c^{-2}\dot\phi^{\,*}$ | The conjugate momentum field, and $\pi^\dagger=c^{-2}\dot\phi$ its conjugate |
| $\tilde\Pi=\pi\,e_0\in\mathbb{C}_{\mathbb{B}}$ | The conjugate momentum field as a central biquaternion |
| $\mathcal{H}=\pi\dot\phi+\pi^\dagger\dot\phi^{\,*}-\mathcal{L}$ | The Hamiltonian density; it is $c^{-2}|\dot\phi|^2+|\nabla\phi|^2+\mu^2|\phi|^2$ and equals the energy density $T^0{}_0$ |
| $H=\int\mathcal{H}\,d^3x$ | The total Hamiltonian |
| $\mathcal{H}=\mathrm{Sc}[(\tilde\nabla\tilde\Phi)^\dagger(\tilde\nabla\tilde\Phi)]+\mu^2\mathrm{Sc}[\tilde\Phi^\dagger\tilde\Phi]$ | The Hamiltonian density as the sum of two Hermitian forms |
| $\{\phi(\mathbf{x}),\pi(\mathbf{y})\}=\delta^3(\mathbf{x}-\mathbf{y})$ | The canonical field bracket, with the mirrored brackets for the conjugates |
| $\{A,B\}$ | The field Poisson bracket on functionals, the integral over space of the local canonical bracket |
| $\mathbf{S}=-(\dot\phi^{\,*}\nabla\phi+\dot\phi\nabla\phi^{\,*})=-c^2(\pi\nabla\phi+\pi^\dagger\nabla\phi^{\,*})$ | The energy flux; $\partial_t\mathcal{H}+\nabla\cdot\mathbf{S}=0$ |
| $\tilde W=\mathcal{H}e_0+\frac{i}{c}\mathbf{S}\in\mathbb{M}_+$ | The energy–momentum biquaternion of the field, with $\tilde\nabla\tilde W=0$ on shell |
| $p^\mu=\partial\mathcal{L}/\partial(\partial_\mu\phi)=\partial^\mu\phi$ | The polymomentum of the covariant (De Donder–Weyl) formalism |
| $H_{DW}=p^\mu\partial_\mu\phi-\mathcal{L}=\frac12p^\mu p_\mu+\frac12\mu^2\phi^2$ | The De Donder–Weyl Hamiltonian of the scalar field |

## Further Reading

- H. Goldstein, C. P. Poole and J. L. Safko, *Classical Mechanics* (3rd ed., Addison-Wesley, 2002), for the continuum Lagrangian, the field Hamiltonian and the transition from the discrete to the continuous phase space.
- L. D. Landau and E. M. Lifshitz, *The Classical Theory of Fields* (4th ed., Pergamon, 1975), for the canonical energy–momentum tensor and the energy density of the scalar field.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I: Foundations* (Cambridge, 1995), for the canonical formalism, the equal-time brackets and the constraint analysis of the gauge field.
- James D. Bjorken and Sidney D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the scalar-field canonical quantization and the Klein–Gordon momentum field.
- Paul A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for the first-class and second-class constraint analysis of the Maxwell and Dirac fields.
- Jerrold E. Marsden and Tudor S. Ratiu, *Introduction to Mechanics and Symmetry* (2nd ed., Springer, 1999), for the field-theoretic Poisson bracket and its relation to the multisymplectic structure.
- Mark J. Gotay, James Isenberg, Jerrold E. Marsden and Richard Montgomery, "Momentum maps and classical relativistic fields," *Physics Reports* (2004), for the covariant Hamiltonian formalism of field theory and the polymomentum.
- *Lagrangian and Hamiltonian Mechanics in Biquaternionic Form* (`articles_physics/lagrangian-and-hamiltonian-mechanics-in-biquaternionic-form.md`), companion article, for the finite-dimensional Legendre transform, the phase-space biquaternion and the bracket that this article extends to a density.
- *The Action Principle and the Classical Limit as Stationary Phase in Biquaternionic Form* (`articles_physics/the-action-principle-and-the-classical-limit-as-stationary-phase-in-biquaternionic-form.md`), companion article, for the action, its first variation and the boundary term.
- *Noether's Theorem in Biquaternionic Form* (`articles_physics/noethers-theorem-in-biquaternionic-form.md`), companion article, for the Lagrangian density and the canonical energy–momentum tensor.
- *Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form* (`articles_physics/stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.md`), companion article, for the energy–momentum biquaternion of the electromagnetic field and the conservation law for field and matter.
- *Canonical Quantization of the Biquaternion Klein–Gordon Field* (`articles_physics/canonical-quantization-of-the-biquaternion-klein-gordon-field.md`), companion article, for the quantization of the classical structure built here.
- *Multisymplectic and Covariant Hamiltonian Field Theory* (`articles_maths/multisymplectic-and-covariant-hamiltonian-field-theory.md`), companion article in the mathematical corpus, for the polymomentum, the De Donder–Weyl equations and the multisymplectic form.
