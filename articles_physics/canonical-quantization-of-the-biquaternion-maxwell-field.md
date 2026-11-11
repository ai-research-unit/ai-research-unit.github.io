# __Canonical Quantization of the Biquaternion Maxwell Field__

## Introduction

The companion article *Canonical Quantization of the Biquaternion Dirac Field* closes by calling its own extension **not canonical**. The part of it that works is the standard canonical quantization of the Dirac field, transcribed onto the biquaternion plane waves of the parent solution article; the part that would be genuinely biquaternionic — a $\mathbb{B}$-intrinsic Lagrangian, a native Fock space, the embedding of the $\mathbb{Z}/2$ fermion-parity grading in the algebra — is left open. It leaves the second-quantization question open for any field, and this article takes that question up for the framework's other classical field.

This article is that treatment for the electromagnetic field of *Maxwell's Equations in the Biquaternionic Formulation*. It has to answer a question the Dirac article could not pose, because there was nothing to compare it with: **does Maxwell behave better or worse than Dirac did?** The answer given here, stated at the outset, is that it behaves neither better nor worse in a simple ranking, but differently, and that the difference is instructive.

- **Better in one respect.** Maxwell needs no new algebraic structure. The field is bosonic, so ordinary commutators suffice. No grading has to be imposed on the algebra, and the indefinite inner product that the covariant quantization requires is, up to convention, the one the material sector $\mathbb{B}_{\Phi}$ already carries, its one minus the square of the $i$ in $Q_t=i r'_t$. Where the Dirac case had to bolt on a $\mathbb{Z}/2$ structure the algebra does not supply, Maxwell bolts on nothing.
- **Worse in another.** In the Dirac case the field appearing in the biquaternion equation is, through its spinor-module representative, the field that is canonically quantized: its momentum is tied to it by a second-class constraint. In the Maxwell case the natural variable is the **field strength** $\tilde{F}$, which is gauge invariant and has no canonical partner; the equation for it is first order and cannot be obtained from a local Lagrangian in which $\tilde{F}$ alone is varied. Canonical quantization therefore forces a return to the potential $\tilde{A}_{\Phi}$, and with it a gauge redundancy that the algebra does not resolve. The framework **cannot fix the gauge naturally**, and that is a finding, not an inconvenience to be smoothed over.

The article has the same standard/open division as its parent, and it is worth stating before the formalism.

- **The standard part.** Maxwell's theory in the potential formulation, its Legendre transform, its first-class constraints, and its covariant quantization by the Gupta–Bleuler subsidiary condition are textbook quantum field theory, transcribed into the notation of this series.
- **The open part.** What is not standard, and what this article cannot settle, is whether the gauge condition can be selected by the algebra rather than imposed from outside; whether the operator-valued field should be $\mathbb{B}$-valued or valued in a complex-vector module; whether the biquaternion structure gives the physical polarizations a native meaning; and what a biquaternion Fock space would be. The last two are the subjects of the planned companion articles on the photon and on the Fock space.

The article is organized as follows. The next section fixes the natural variable and explains why it is natural and why that is a problem. The following section develops the gauge freedom and the two equivalent formulations of the classical theory. The next section carries out the constraint analysis. The section after that writes the constraints in the biquaternion notation and isolates what the algebra does and does not determine. The next section performs the Gupta–Bleuler quantization and exhibits the two transverse physical polarizations with positive norm. A section compares the result with the scalar field, a section compares it with the Dirac case, and the article closes with an explicit accounting of what is standard and what is open.

## The Natural Variable and Why It Is Not Canonical

The classical theory of the companion article is one equation for one object:

$$
\boxed{\;\tilde\nabla_\Phi\tilde{F}=-\sqrt{\mu}\,\tilde{J}_{\Phi},\qquad \tilde{F}=i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H,\qquad \tilde J_{\Phi}=ic\rho\,e_t+\vec J\;}.
$$

The field strength $\tilde{F}$ is a biquaternion with vanishing scalar part. It is **gauge invariant**, and it is the object that the equation is written for. This is what it means to say that the field strength is the natural variable of the biquaternionic formulation. Two properties make it natural, and both are worth recording before the difficulty is described.

First, the equation is **first order**: $\tilde\nabla_\Phi$ appears once. This is the same order as the biquaternion Dirac equation, and it is one order lower than the wave equation for the potential.

Second, the **real and imaginary parts of the single complex equation separate the homogeneous and inhomogeneous Maxwell equations**. Writing $\vec F=\tilde{F}$ and decomposing $\tilde\nabla_\Phi\tilde{F}=-\sqrt{\mu}\,\tilde{J}_{\Phi}$ into its scalar and vector parts gives the two equations

$$
\mathrm{div}\,\vec F=R_0,\qquad \partial/\partial R_t\,\vec F+\mathrm{rot}\,\vec F=-\vec R,
$$
where $R_0$ and $\vec R$ are the scalar and vector parts of $-\sqrt{\mu}\,\tilde J_{\Phi}$.

Because $\sqrt{\epsilon}\,\vec E$ is the imaginary part of $\vec F$ and $-\sqrt{\mu}\,\vec H$ is its real part, the real part of $\mathrm{div}\,\vec F=R_0$ is $\mathrm{div}\,\vec H=0$, the imaginary part is Gauss's law $\mathrm{div}(\epsilon\vec E)=\rho$, and the vector equation reproduces Faraday's law from its imaginary part and the Ampère–Maxwell law from its real part. A single complex equation thus contains all four Maxwell equations, with the field's own complex structure doing the bookkeeping. This is the cleanest expression of why the biquaternion formulation prefers $\tilde{F}$.

The difficulty is that **none of this gives a canonical structure**. Canonical quantization needs a Lagrangian, a field, and a momentum conjugate to it, and the two are paired by the Legendre transform. The first-order equation $\tilde\nabla_\Phi\tilde{F}=-\sqrt{\mu}\,\tilde{J}_{\Phi}$ has no momentum conjugate to $\tilde{F}$: it is a first-order equation, and one cannot perform a Legendre transform on it directly. Worse, there is no local Lagrangian in four dimensions whose Euler–Lagrange equation is the first-order Maxwell system when $\tilde{F}$ is the only field. A polynomial invariant built from $\tilde{F}$ alone, such as the biquaternion norm $\tilde{F}\tilde{F}^{\natural}$, has an algebraic variation and gives $\tilde{F}=0$ rather than the field equation; a Lagrangian built from derivatives of $\tilde{F}$ gives a higher-derivative equation. The two homogeneous Maxwell equations that $\tilde\nabla_\Phi\tilde{F}=0$ encodes are, on the potential, the **Bianchi identity** $\tilde{F}=(\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}-\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi})$; they are not equations of motion. To vary $\tilde{F}$ into the field equation one must impose that identity as a constraint, and the multiplier one introduces for it is precisely the potential. This is worked out in the next section.

The natural variable, in short, is not the canonical variable. That is the structural difference from the Dirac case and the reason the rest of the article must pass through the potential.

## Gauge Freedom and the Two Formulations

The potential is not unique. Two potentials give the same field strength when they differ by

$$
\tilde{A}_{\Phi,2}=\tilde{A}_{\Phi}-\tilde\nabla_\Phi\Gamma,
$$

with $\Gamma$ an arbitrary scalar function. The scalar part

$$
S=\mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}\right)
$$

is the gauge degree of freedom of the companion article: it transforms as

$$
S_2=S-\Box\Gamma,
$$

and the field strength is invariant, $\tilde{F}_2=\tilde{F}$. The companion article states plainly that $S$ "is a gauge artifact" and that the **Lorenz gauge** $S=0$ is "a choice of gauge, not a physical condition". In that gauge the potential obeys the second-order equation

$$
\Box\tilde{A}_{\Phi}=-\mu\tilde J_{\Phi},\qquad \tilde J_{\Phi}=ic\rho\,e_t+\vec J.
$$

Two equivalent formulations of the classical theory are therefore available, and the choice matters for quantization.

**The second-order, potential formulation.** The field is $\tilde{A}_{\Phi}$; the Lagrangian density is $\mathcal{L}=\hbar\left(-\tfrac14 \sum_{\mu,\nu}F_{\mu\nu}F_{\mu\nu}\right)$; it is second order, and it is the formulation in which the Legendre transform and the canonical momentum are defined. This is the route the rest of the article follows.

**The first-order, Palatini formulation.** If one wants the field strength to remain the independent variable, one takes $\tilde{F}$ and $\tilde{A}_{\Phi}$ as independent and uses the first-order action

$$
S=\int d^4r\left[-\sum_{\mu,\nu}F_{\mu\nu}\,\partial/\partial R_\mu A_\nu+\tfrac14 \sum_{\mu,\nu}F_{\mu\nu}F_{\mu\nu}\right].
$$

Varying with respect to $A_\nu$ gives $\sum_\mu\partial/\partial R_\mu F_{\mu\nu}=0$, the inhomogeneous Maxwell equations, and varying with respect to $F_{\mu\nu}$ gives $F_{\mu\nu}=\partial/\partial R_\mu A_\nu-\partial/\partial R_\nu A_\mu$, the definition that makes the homogeneous equations automatic; on shell the integrand is $-\tfrac14\sum_{\mu,\nu}F_{\mu\nu}F_{\mu\nu}$. The field strength is present as an independent variable, but the potential reappears as its Lagrange multiplier, carrying no kinetic term of its own. The gauge freedom is not removed by this route; it is relocated. There is no local action in four dimensions in which the gauge-invariant field strength alone is varied and Maxwell's equations, rather than $\tilde{F}=0$, follow.

This is the first finding of the article. The biquaternion formulation writes the theory in its most compact and most covariant form, first order in a gauge-invariant object; canonical quantization cannot start from that object. It must either return to the potential and accept the gauge redundancy, or use the first-order formulation and accept the potential as a multiplier. In neither case does the algebra supply the missing structure.

## The Constraint Structure

The Legendre transform of the potential formulation is singular, and the singularities are of a different kind from the Dirac case. The conjugate momenta are

$$
\pi_\mu=\frac{\partial\mathcal{L}}{\partial(\partial/\partial R_t A_\mu)}=-F_{t\mu},
$$

so that

$$
\pi_0=0,\qquad \vec\pi=-i\vec E.
$$

The vanishing of $\pi_0$ is a **primary constraint**: the time component of the potential has no conjugate momentum, because $\mathcal{L}$ contains no time derivative of $A_0$. It is not the end of the story. The Hamiltonian, after integrating by parts, is

$$
\mathcal{H}=\tfrac12\left(\vec E^2+\vec B^2\right)-A_0\,\mathrm{div}\,\vec\pi,
$$

in which $A_0$ appears as a Lagrange multiplier. Consistency of the primary constraint with the evolution requires $\mathrm{div}\,\vec\pi\approx0$, which is **Gauss's law**, and it is a **secondary constraint**. The two constraints

$$
\pi_0\approx0,\qquad \mathrm{div}\,\vec\pi\approx0
$$

are **first class**: their Poisson bracket with each other vanishes, and each generates a gauge transformation of the potential. Because they are first class, the theory is not a theory of four vector-field components; the physical content is the gauge orbit, not the orbit's representatives.

Counting degrees of freedom makes the point. The phase space of the four components of $A_\mu$ has $4\times2=8$ dimensions. A first-class constraint removes two phase-space dimensions — the constraint itself and the gauge direction it generates — so two first-class constraints remove four, leaving $8-4=4$ phase-space dimensions, that is, **two field degrees of freedom** at each point. These are the two transverse polarizations.

The contrast with the Dirac field is exact and should be set beside it. There the conjugate momentum was $\pi=i\tilde{Ξ}_{\mathrm{sp}}^{\dagger}$, algebraically tied to the field by the **second-class** constraint $\xi=\pi-i\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\approx0$; the momentum was not independent, and the gauge freedom was absent, but the bracketing had to become anticommutation. Here the momentum is independent in its spatial components, one entire component of it vanishes, and a divergence constraint appears; the constraint is first class, gauge freedom is present, and the bracketing stays commutation. Both theories have singular Legendre transforms. The singularity of the Dirac case forces a different bracket; the singularity of the Maxwell case forces a choice of gauge.

## The Constraints in Biquaternion Notation

The two constraints have a compact form in the notation of the companion articles. Let $\tilde{\pi}$ be the biquaternion whose components are the canonical momenta conjugate to $\tilde{A}_{\Phi}$:

$$
\tilde{\pi}=\pi_0e_t+\vec\pi,\qquad \pi_0=0,\qquad \vec\pi=-i\vec E.
$$

Then $\pi_0=0$ is the statement that the **scalar part** of $\tilde{\pi}$ vanishes,

$$
\mathrm{Sc}(\tilde{\pi})\approx0,
$$

and Gauss's law is a scalar-part condition as well. A direct computation of the quaternion product gives

$$
\mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{\pi}\right)=\partial/\partial R_t\,\pi_0+\mathrm{div}\,\vec\pi,
$$

so that on the constraint surface, where $\pi_0\approx0$,

$$
\boxed{\;\mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{\pi}\right)\approx0\;}.
$$

The two constraints are therefore the scalar parts of $\tilde{\pi}$ and of $(\tilde\nabla_\Phi)^{\natural}\tilde{\pi}$. This is the same shape as the **integrability condition** of the companion article, $\sqrt{\mu}\,\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi})=0$, which expresses charge conservation; Gauss's law and charge conservation are written with the same operator. That is a genuine feature of the notation: the constraint is not an extra object appended to the algebra but a scalar-part projection that already appears in it.

The gauge freedom, correspondingly, is the freedom to add $\tilde\nabla_\Phi\Gamma$ to $\tilde{A}_{\Phi}$; it lives in the scalar direction of the material sector, and $S=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi})$ is its field. The physical field strength is the **vector part** of $(\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}$, invariant under the transformation, and the framework's own account says the scalar part is not physical.

Two points about this interpretation must be kept separate.

The first is a **structural observation**, and it is suggestive but convention-dependent. The potential $\tilde{A}_{\Phi}=i\,a'_t\,e_t+\vec A$ has an imaginary scalar part and a real vector part: it is an element of the material sector $\mathbb{B}_{\Phi}$. The conjugate momentum $\tilde{\pi}$ has a vanishing (real) scalar part and a purely imaginary vector part: in the $i r'_t$ convention it is an element of the complementary sector $\mathbb{B}_{\Psi}$. The canonical pair thus straddles the two sectors that the framework distinguishes as material and informational — the same pairing of "configuration" and "operator" that the article on $\mathbb{B}_{\Psi}$ describes for its action on $\mathbb{B}_{\Phi}$. Whether this is a meaningful statement about the algebra or a consequence of writing the momentum with the $i r'_t$ derivative is not decided here, and it is recorded as an open question. In a real-time formulation the momentum of the same theory is real, and the placement reverses; the physical content is unchanged.

The second is the **finding**. Nothing in the algebra selects a gauge. The gauge-invariant content of the theory is a functional of $\tilde{F}$ alone, and $\tilde{F}$ is invariant under every gauge transformation; so no gauge-invariant functional of $\tilde{A}_{\Phi}$ — no biquaternion norm, no trace, no conjugation built from the basis and $i$ — can break the degeneracy, because any such functional is a function of $\tilde{F}$. The Lorenz condition $S=0$ is available and is the framework's covariant choice, but the companion article itself declines to make it physical, and the algebra offers no principle that prefers it to $A_0=0$ (the temporal gauge) or to any other. The gauge must be fixed from outside the algebra. This is the sense in which the biquaternion framework cannot quantize Maxwell "automatically".

## Gupta–Bleuler Quantization

Covariant quantization proceeds with all four polarizations and imposes a subsidiary condition. Expand the free potential in plane waves,

$$
A_\mu(x)=\int\!\frac{d^3k_\Phi}{(2\pi)^3}\sqrt{\frac{c}{2\omega_k}}\sum_{r=0}^{3}
\left[\epsilon^{(r)}_\mu(\vec k_\Phi)\,a_{\mathrm{fop},r}(\vec k_\Phi)\,\exp(-ik\cdot x)
+\epsilon^{(r)*}_\mu(\vec k_\Phi)\,a_{\mathrm{fop},r}^{\dagger}(\vec k_\Phi)\,\exp(+ik\cdot x)\right],
$$

with $\omega_k=c\lvert\vec k_\Phi\rvert$ an angular frequency for the massless field, $k\cdot x=\vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)-\omega_k r'_t/c$, and with polarization vectors normalized as $\langle\epsilon^{(r)},\epsilon^{(s)}\rangle_{\natural}=\sigma_{\mathrm{met},r}\delta_{rs}$, where $(\sigma_{\mathrm{met},0},\sigma_{\mathrm{met},1},\sigma_{\mathrm{met},2},\sigma_{\mathrm{met},3})=(-1,+1,+1,+1)$, the one minus being the square of the $i$ that the time coefficient carries, $Q_t=i r'_t$, and the natural form on the four units $e_t,\vec e_x,\vec e_y,\vec e_z$ being $\delta_{\mu\nu}$. The mode operators carry the corresponding commutators,

$$
\boxed{\;\big[a_{\mathrm{fop},r}(\vec k_\Phi),a_{\mathrm{fop},s}^{\dagger}(\vec k_2)\big]
=\sigma_{\mathrm{met},r}\,\delta_{rs}\,(2\pi)^3\,\delta^{(3)}(\vec k_\Phi-\vec k_2)\;},
$$

with all other commutators vanishing. The signs are not optional: the timelike mode has $\sigma_{\mathrm{met},0}=-1$, so the one-particle state $a_{\mathrm{fop},0}^{\dagger}|0\rangle$ has **negative norm**, $\langle0|a_{\mathrm{fop},0}a_{\mathrm{fop},0}^{\dagger}|0\rangle=-1$. The longitudinal mode has positive norm, as do the two transverse modes.

The negative-norm states are removed by a **subsidiary condition**. The Lorenz gauge condition $S=0$ is imposed on the positive-frequency part of the field,

$$
\mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}A\right)^{(+)}|\tilde{Ξ}_{\mathrm{sp}}\rangle=0,
$$

which for a mode with momentum along $\vec e_z$ reduces to

$$
\boxed{\;\big(a_{\mathrm{fop},0}(\vec k_\Phi)-a_{\mathrm{fop},3}(\vec k_\Phi)\big)|\tilde{Ξ}_{\mathrm{sp}}\rangle=0\;}.
$$

This condition does not set the timelike and longitudinal excitations to zero individually; it leaves the combination $a_{\mathrm{fop},0}^{\dagger}-a_{\mathrm{fop},3}^{\dagger}$. That combination is annihilated by the condition,

$$
\big(a_{\mathrm{fop},0}-a_{\mathrm{fop},3}\big)\big(a_{\mathrm{fop},0}^{\dagger}-a_{\mathrm{fop},3}^{\dagger}\big)|0\rangle
=\big(\sigma_{\mathrm{met},0}+\sigma_{\mathrm{met},3}\big)|0\rangle=0,
$$

and it has **zero norm**,

$$
\big\|\big(a_{\mathrm{fop},0}^{\dagger}-a_{\mathrm{fop},3}^{\dagger}\big)|0\rangle\big\|^2
=\sigma_{\mathrm{met},0}+\sigma_{\mathrm{met},3}=-1+1=0,
$$

so, lying in the physical subspace and being null, it is orthogonal to every state in that subspace and decouples from all physical amplitudes. On the quotient by the zero-norm states, the physical subspace has **positive-definite norm** and consists exactly of the two transverse polarizations. Their polarization sum is the transverse projector,

$$
\boxed{\;\sum_{\lambda=1}^{2}\epsilon_i^{(\lambda)}(\vec k_\Phi)\,\epsilon_j^{(\lambda)}(\vec k_\Phi)
=\delta_{ij}-\vec u_{\Phi,i}\vec u_{\Phi,j}\;},
$$

which makes the physical field transverse: the polarization sum annihilates every component along $\vec u_\Phi$.

This is the quantization, and it works: two transverse polarizations, no negative-norm physical states, a positive-definite physical inner product. But the machinery was imported. The subsidiary condition is a condition on the potential, and the framework does not supply it; the indefinite inner product with $\sigma_{\mathrm{met},0}=-1$ is a structure the algebra does not by itself demand. The one compensating observation is the one made above: the indefinite form $\sigma_{\mathrm{met}}$, with $\sigma_{\mathrm{met},0}=-1$ and $\sigma_{\mathrm{met},\eta}=+1$, is the biquaternion norm of $\mathbb{B}_{\Phi}$, its one minus the square of the $i$ in $Q_t=i r'_t$, so the indefinite inner product is not a new object but the framework's own. Whether that identification has content beyond the coincidence of form is open.

The alternatives should be named. The **Coulomb gauge** $\mathrm{div}\,\vec A=0$ removes the gauge freedom non-covariantly, leaves only the two transverse modes from the start, and gives a manifestly positive-definite norm, at the price of an instantaneous interaction and a loss of manifest Lorentz covariance. It is the same physical theory; it differs in which structure is imposed by hand. The framework's covariance preference points at Gupta–Bleuler, but the preference is not a derivation.

## Comparison with the Scalar Field

The counting is worth setting beside the scalar field, because the difference is where the gauge structure lives. A real scalar field $\xi_{\mathrm{scl}}$ of mass $m$ has conjugate momentum $\pi=\partial\xi_{\mathrm{scl}}/\partial r'_t$, the canonical commutator $[\xi_{\mathrm{fop}}(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z),\pi_{\mathrm{fop}}(\vec y)]=i\delta^{(3)}(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z-\vec y)$, and a mode expansion with **one** polarization,

$$
\big[a_{\mathrm{fop}}(\vec k_\Phi),a_{\mathrm{fop}}^{\dagger}(\vec k_2)\big]=(2\pi)^3\,\delta^{(3)}(\vec k_\Phi-\vec k_2),
$$

with dispersion $\omega_k=c\sqrt{\vec k_\Phi^2+k_m^{2}}$. Its Fock space has positive-definite norm, there is no constraint, and no gauge condition has to be imposed: the Legendre transform is regular. The massless scalar field has one mode. The photon has **two** physical transverse modes and reaches them only after the two unphysical modes — the timelike and the longitudinal — have been removed by a subsidiary condition. The photon is not a scalar particle with an extra label; the reduction from four components to two is performed by the gauge structure, and that structure is what the algebra does not fix. If the gauge field is given a mass, as in the Proca theory, the gauge freedom is absent, the constraint structure changes, and a third (longitudinal) polarization becomes physical — which shows that the two-polarization count is a consequence of the gauge symmetry, not of the number of field components.

## Comparison with the Dirac Case

The two quantizations may now be set side by side.

- **The constraint.** The Dirac field carries a **second-class** constraint $\pi-i\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\approx0$: the momentum is algebraically tied to the field. The Maxwell field carries two **first-class** constraints, $\pi_0\approx0$ and $\mathrm{div}\,\vec\pi\approx0$: the momentum is largely independent, one component of it vanishes, and the constraints generate gauge transformations.
- **The bracket.** Second-class constraints force the bracket to be changed, and positivity forces the change to be to **anticommutators**; the Dirac field is fermionic. First-class constraints leave the bracket a **commutator** and instead require a gauge choice; the Maxwell field is bosonic.
- **The added structure.** The Dirac quantization required a $\mathbb{Z}/2$ grading that the algebra does not supply and had to impose it on the mode algebra. The Maxwell quantization requires no new algebraic structure at all: the scalar imaginary already supplies the phase, the modes commute, and the indefinite inner product needed for the covariant treatment is the framework's own, its one minus the square of the $i$ in $Q_t=i r'_t$.
- **The natural variable.** In the Dirac case the natural variable of the biquaternion equation is the field that is quantized. In the Maxwell case it is not: $\tilde{F}$ is gauge invariant and first order, and the passage to canonical variables reintroduces the potential and its redundancy.

The verdict is therefore not a ranking. **Maxwell is a transcription of standard canonical quantization, exactly as the Dirac case was, but its obstruction is the opposite kind.** Dirac was blocked by a structure the algebra does not contain; Maxwell is blocked by a redundancy the algebra does not remove. The first asks for an addition to the algebra; the second asks for a gauge-fixing principle that the algebra declines to provide. Which of those is more hopeful for the research program is a question this article cannot answer, but the two are not the same question, and the Dirac article's phrase "not canonical" applies here with a different meaning.

## What Is Standard and What Is Open

**Standard, and transcribed here.** The single biquaternion Maxwell equation $\tilde\nabla_\Phi\tilde{F}=-\sqrt{\mu}\,\tilde{J}_{\Phi}$ and the real/imaginary separation of the homogeneous and inhomogeneous equations; the gauge transformation and the transformation of $S$; the second-order potential equation in the Lorenz gauge; the first-order Palatini action and the two variations; the conjugate momenta $\pi_\mu=-F_{t\mu}$, the primary constraint $\pi_0\approx0$, the Gauss-law secondary constraint, and the first-class character of both; the degree-of-freedom count giving two field degrees of freedom; the Gupta–Bleuler mode expansion, commutators, subsidiary condition, zero-norm unphysical combination, transverse polarization sum, and positive-definite physical norm. None of this is new, and none of it depends on the biquaternion structure beyond the kinematical conventions of the companion articles.

**Open, and not settled here.**

- **The gauge-fixing principle.** The framework gives no algebraic reason to prefer $S=0$ to any other gauge, or to prefer Gupta–Bleuler to the Coulomb gauge. Whether a biquaternionic principle exists is the central open question. The companion article's judgement that $S$ is a gauge artifact is a negative statement, not a mechanism.
- **The intrinsic Lagrangian and pairings.** The parent Dirac article records that the $\mathbb{B}$-intrinsic Lagrangian and conjugate momentum are not fixed by the algebra. The same is true here, and more sharply, because the natural variable $\tilde{F}$ has no canonical partner at all. Whether a real-scalar Lagrangian built from the trace and norm pairings reproduces the standard constraint structure is not shown.
- **The biquaternion Fock space.** Whether there is a Fock space native to $\mathbb{B}$, rather than the exterior (fermionic) or symmetric (bosonic) algebra of a module's solution space, is the subject of the planned companion article on the Fock space.
- **The photon.** Whether the two transverse polarizations have a native meaning in the algebra — for instance, in the vector part of the material sector — is the subject of the planned article on the photon.
- **The sector straddle.** Whether $\tilde{A}_{\Phi}\in\mathbb{B}_{\Phi}$ and $\tilde{\pi}\in\mathbb{B}_{\Psi}$ has algebraic content or is a convention effect is undecided.
- **The vacuum energy.** As in the Dirac case, whether the algebra singles out a regularization or a geometric meaning for the zero-point energy is open.
- **Empirical content.** Whether any of this yields a prediction distinguishing it from standard quantum electrodynamics is the unanswered framework-level question.

## Summary

The biquaternion Maxwell equation $\tilde\nabla_\Phi\tilde{F}=-\sqrt{\mu}\,\tilde{J}_{\Phi}$ is first order, and its natural variable $\tilde{F}=i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H$ is gauge invariant; its real and imaginary parts separate the homogeneous and the inhomogeneous Maxwell equations. But $\tilde{F}$ has no canonical partner, and no local Lagrangian in four dimensions produces the field equation by varying $\tilde{F}$ alone. Canonical quantization must therefore return to the potential $\tilde{A}_{\Phi}$, and with it the gauge freedom $\tilde{A}_{\Phi,2}=\tilde{A}_{\Phi}-\tilde\nabla_\Phi\Gamma$, whose field is $S=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi})$ with $S_2=S-\Box\Gamma$.

The Legendre transform is singular. The conjugate momenta are $\pi_\mu=-F_{t\mu}$, so $\pi_0\approx0$ is primary and Gauss's law $\mathrm{div}\,\vec\pi\approx0$ is secondary; both are **first class** and generate gauge transformations. The phase-space count $8-2\times2=4$ gives two field degrees of freedom. In the notation of the companion articles the constraints are $\mathrm{Sc}(\tilde{\pi})\approx0$ and $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{\pi})\approx0$, the same scalar-part shape as the charge-conservation condition $\sqrt{\mu}\,\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi})=0$.

Covariant quantization is Gupta–Bleuler: four polarizations with commutators $[a_{\mathrm{fop},r},a_{\mathrm{fop},s}^{\dagger}]=\sigma_{\mathrm{met},r}\delta_{rs}(2\pi\hbar)^3\delta^{(3)}$, $\sigma_{\mathrm{met}}=(-1,+1,+1,+1)$, so the timelike mode has negative norm; the subsidiary condition $(a_{\mathrm{fop},0}-a_{\mathrm{fop},3})|\tilde{Ξ}_{\mathrm{sp}}\rangle=0$ leaves the zero-norm combination $a_{\mathrm{fop},0}^{\dagger}-a_{\mathrm{fop},3}^{\dagger}$, which decouples, and the physical subspace has positive-definite norm and exactly the two transverse polarizations, with $\sum_{\lambda=1}^2\epsilon_i^{(\lambda)}\epsilon_j^{(\lambda)}=\delta_{ij}-\vec u_{\Phi,i}\vec u_{\Phi,j}$. By comparison a real scalar field has one mode, no constraint, and positive norm. The two-polarization count follows from the gauge symmetry, not from the number of components.

The extension is a transcription of standard canonical quantization into the framework's notation, not a derivation of the quantized structure from $\mathbb{B}$. Unlike the Dirac case it requires no new grading, but unlike the Dirac case the natural variable is not the canonical one, and the gauge must be fixed from outside the algebra. The framework cannot quantize the Maxwell field automatically.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\eta^2=-e_t$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{B}_{\Psi},\mathbb{B}_{\Phi}$ | Informational (Hermitian) and material (anti-Hermitian) sectors |
| $\mathbb{B}_{H}$ | Real-quaternion subspace |
| $\tilde{\nabla}=e_t\partial/\partial R_t+\vec e_x\partial/\partial R_x+\vec e_y\partial/\partial R_y+\vec e_z\partial/\partial R_z$ | Biquaternionic gradient |
| $(\tilde\nabla_\Phi)^{\natural}$ | Quaternion-conjugate gradient |
| $\Box=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi$ | d'Alembertian |
| $\tilde{A}_{\Phi}=i\,a'_t\,e_t+\vec A$ | Potential biquaternion (in $\mathbb{B}_{\Phi}$) |
| $\tilde{F}=i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H$ | Field-strength biquaternion (vanishing scalar part) |
| $\tilde J_{\Phi}=ic\rho\,e_t+\vec J$ | Four-current; the source enters as $\sqrt{\mu}\,\tilde J_{\Phi}$ |
| $\tilde\nabla_\Phi\tilde{F}=-\sqrt{\mu}\,\tilde{J}_{\Phi}$ | Biquaternionic Maxwell equation |
| $\Gamma$ | Gauge function, $\tilde{A}_{\Phi,2}=\tilde{A}_{\Phi}-\tilde\nabla_\Phi\Gamma$ |
| $S=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi})$, $S_2=S-\Box\Gamma$ | Gauge degree of freedom; Lorenz gauge $S=0$ |
| $\delta_{\mu\nu}$ | Unit metric, all four coefficients $+1$; $\sum_{\mu,\nu}\delta_{\mu\nu}Q_\mu Q_\nu$ is the biquaternion norm on $\mathbb{B}_{\Phi}$, with $Q_t=i r'_t$ |
| $\mathcal{L}=-\tfrac14 \sum_{\mu,\nu}F_{\mu\nu}F_{\mu\nu}$ | Maxwell Lagrangian density (potential formulation) |
| $\pi_\mu=\partial\mathcal{L}/\partial(\partial/\partial R_t A_\mu)=-F_{t\mu}$ | Conjugate momenta: $\pi_0\approx0$, $\vec\pi=-i\vec E$ |
| $\tilde{\pi}=\pi_0e_t+\vec\pi$ | Momentum biquaternion |
| $\mathrm{Sc}(\tilde{\pi})\approx0$, $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{\pi})\approx0$ | Primary and Gauss-law constraints, both first class |
| $A_\mu$, $\epsilon^{(r)}_\mu$, $a_{\mathrm{fop},r},a_{\mathrm{fop},r}^{\dagger}$ | Quantized potential, polarization vectors, mode operators |
| $[a_{\mathrm{fop},r}(\vec k_\Phi),a_{\mathrm{fop},s}^{\dagger}(\vec k_2)]=\sigma_{\mathrm{met},r}\delta_{rs}(2\pi\hbar)^3\delta^{(3)}$ | Mode commutator, $\sigma_{\mathrm{met}}=(-1,+1,+1,+1)$ |
| $(a_{\mathrm{fop},0}-a_{\mathrm{fop},3})\lvert\tilde{Ξ}_{\mathrm{sp}}\rangle=0$ | Gupta–Bleuler subsidiary condition (momentum along $\vec e_z$) |
| $\sum_{\lambda=1}^2\epsilon_i^{(\lambda)}\epsilon_j^{(\lambda)}=\delta_{ij}-\vec u_{\Phi,i}\vec u_{\Phi,j}$ | Transverse polarization sum |
| $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | Trace reading of the plain form on the informational sector |

## Further Reading

- S. N. Gupta, "Theory of longitudinal photons in quantum electrodynamics," *Proceedings of the Physical Society A* **63** (1950) 681–691, and K. Bleuler, "Eine neue Methode zur Behandlung der longitudinalen und skalaren Photonen," *Helvetica Physica Acta* **23** (1950) 567–586, for the indefinite-metric quantization and the subsidiary condition.
- P. A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for first-class and second-class constraints and the constraint algorithm.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), and C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the canonical quantization of the electromagnetic field and the Coulomb-gauge treatment.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), and S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the Gupta–Bleuler construction and the physical-state condition.
- F. Strocchi, *An Introduction to the Non-Perturbative Foundations of Quantum Field Theory* (Oxford, 2013), for the constraint and gauge-structure analysis on which the first-class counting rests.
- I. Białynicki-Birula and Z. Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism," *Journal of Physics A* **46** (2013) 053001, for the complex-vector formulation and its quantization.
- L. A. Alexeyeva, "Maxwell Equations, Their Hamiltonian and Biquaternionic Forms and Properties of Their Solutions" (2016), for the biquaternionic Maxwell equation and the operator factorization used here.
- Companion articles: [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html); [Canonical Quantization of the Biquaternion Dirac Field](canonical-quantization-of-the-biquaternion-dirac-field.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html); [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html).
