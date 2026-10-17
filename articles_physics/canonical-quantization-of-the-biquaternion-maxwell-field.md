# __Canonical Quantization of the Biquaternion Maxwell Field__

## Introduction

The companion article *Canonical Quantization of the Biquaternion Dirac Field* closes by calling its own extension **not canonical**. The part of it that works is the standard canonical quantization of the Dirac field, transcribed onto the biquaternion plane waves of the parent solution article; the part that would be genuinely biquaternionic — a $\mathbb{B}$-intrinsic Lagrangian, a native Fock space, the embedding of the $\mathbb{Z}/2$ fermion-parity grading in the algebra — is left open. It leaves the second-quantization question open for any field, and this article takes that question up for the framework's other classical field.

This article is that treatment for the electromagnetic field of *Maxwell's Equations in the Biquaternionic Formulation*. It has to answer a question the Dirac article could not pose, because there was nothing to compare it with: **does Maxwell behave better or worse than Dirac did?** The answer given here, stated at the outset, is that it behaves neither better nor worse in a simple ranking, but differently, and that the difference is instructive.

- **Better in one respect.** Maxwell needs no new algebraic structure. The field is bosonic, so ordinary commutators suffice. No grading has to be imposed on the algebra, and the indefinite metric that the covariant quantization requires is, up to convention, the spacetime metric that the material sector $\mathbb{M}_-$ already carries. Where the Dirac case had to bolt on a $\mathbb{Z}/2$ structure the algebra does not supply, Maxwell bolts on nothing.
- **Worse in another.** In the Dirac case the field appearing in the biquaternion equation is, through its spinor-module representative, the field that is canonically quantized: its momentum is tied to it by a second-class constraint. In the Maxwell case the natural variable is the **field strength** $\tilde{F}$, which is gauge invariant and has no canonical partner; the equation for it is first order and cannot be obtained from a local Lagrangian in which $\tilde{F}$ alone is varied. Canonical quantization therefore forces a return to the potential $\tilde{A}$, and with it a gauge redundancy that the algebra does not resolve. The framework **cannot fix the gauge naturally**, and that is a finding, not an inconvenience to be smoothed over.

The article has the same standard/open division as its parent, and it is worth stating before the formalism.

- **The standard part.** Maxwell's theory in the potential formulation, its Legendre transform, its first-class constraints, and its covariant quantization by the Gupta–Bleuler subsidiary condition are textbook quantum field theory, transcribed into the notation of this series.
- **The open part.** What is not standard, and what this article cannot settle, is whether the gauge condition can be selected by the algebra rather than imposed from outside; whether the operator-valued field should be $\mathbb{B}$-valued or valued in a complex-vector module; whether the biquaternion structure gives the physical polarizations a native meaning; and what a biquaternion Fock space would be. The last two are the subjects of the planned companion articles on the photon and on the Fock space.

The article is organized as follows. The next section fixes the natural variable and explains why it is natural and why that is a problem. The following section develops the gauge freedom and the two equivalent formulations of the classical theory. The next section carries out the constraint analysis. The section after that writes the constraints in the biquaternion notation and isolates what the algebra does and does not determine. The next section performs the Gupta–Bleuler quantization and exhibits the two transverse physical polarizations with positive norm. A section compares the result with the scalar field, a section compares it with the Dirac case, and the article closes with an explicit accounting of what is standard and what is open.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_t=1,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_\mu^2=-e_t$, and $i$ is the scalar imaginary with $i^2=-1$. The biquaternionic gradient is $\tilde{\nabla}=e_t\partial/\partial Q_t+\vec e_x\partial/\partial Q_x+\vec e_y\partial/\partial Q_y+\vec e_z\partial/\partial Q_z$ and $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}=\tilde{\nabla}^{\natural}\tilde{\nabla}$. The potential and field strength are $\tilde{A}=i\phi/c\,e_t+\vec A$ and $\tilde{F}=i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H$, and the single Maxwell equation is $\tilde{\nabla}\tilde{F}=-\tilde{R}$. For the quantization of a free field we set $\epsilon=\epsilon_0$, $\mu=\mu_0$ and use natural units $\hbar=c=1$, in which $\tilde{F}=i\vec E-\vec H$; dimensionful factors are restored only where they carry meaning. The spacetime metric of the $ict$ sector is $\eta=\mathrm{diag}(-1,+1,+1,+1)$, the signature of the biquaternion norm on $\mathbb{M}_-$; the Clifford metric of the parent Dirac article is $g=-\eta$.

## The Natural Variable and Why It Is Not Canonical

The classical theory of the companion article is one equation for one object:

$$
\tilde{\nabla}\tilde{F}=-\tilde{R},\qquad \tilde{F}=i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H,\qquad \tilde{R}=\frac{i\rho}{\sqrt{\epsilon}}\,e_t+\sqrt{\mu}\,\vec J.
$$

The field strength $\tilde{F}$ is a biquaternion with vanishing scalar part. It is **gauge invariant**, and it is the object that the equation is written for. This is what it means to say that the field strength is the natural variable of the biquaternionic formulation. Two properties make it natural, and both are worth recording before the difficulty is described.

First, the equation is **first order**: $\tilde{\nabla}$ appears once. This is the same order as the biquaternion Dirac equation, and it is one order lower than the wave equation for the potential.

Second, the **real and imaginary parts of the single complex equation separate the homogeneous and inhomogeneous Maxwell equations**. Writing $\vec F=\tilde{F}$ and decomposing $\tilde{\nabla}\tilde{F}=-\tilde{R}$ into its scalar and vector parts gives the two equations

$$
\mathrm{div}\,\vec F=R_0,\qquad \partial/\partial Q_t\,\vec F+\mathrm{rot}\,\vec F=-\vec R.
$$

Because $\sqrt{\epsilon}\,\vec E$ is the imaginary part of $\vec F$ and $-\sqrt{\mu}\,\vec H$ is its real part, the real part of $\mathrm{div}\,\vec F=R_0$ is $\mathrm{div}\,\vec H=0$, the imaginary part is Gauss's law $\mathrm{div}(\epsilon\vec E)=\rho$, and the vector equation reproduces Faraday's law from its imaginary part and the Ampère–Maxwell law from its real part. A single complex equation thus contains all four Maxwell equations, with the field's own complex structure doing the bookkeeping. This is the cleanest expression of why the biquaternion formulation prefers $\tilde{F}$.

The difficulty is that **none of this gives a canonical structure**. Canonical quantization needs a Lagrangian, a field, and a momentum conjugate to it, and the two are paired by the Legendre transform. The first-order equation $\tilde{\nabla}\tilde{F}=-\tilde{R}$ has no momentum conjugate to $\tilde{F}$: it is a first-order equation, and one cannot perform a Legendre transform on it directly. Worse, there is no local Lagrangian in four dimensions whose Euler–Lagrange equation is the first-order Maxwell system when $\tilde{F}$ is the only field. A polynomial invariant built from $\tilde{F}$ alone, such as the biquaternion norm $\tilde{F}\tilde{F}^{\natural}$, has an algebraic variation and gives $\tilde{F}=0$ rather than the field equation; a Lagrangian built from derivatives of $\tilde{F}$ gives a higher-derivative equation. The two homogeneous Maxwell equations that $\tilde{\nabla}\tilde{F}=0$ encodes are, on the potential, the **Bianchi identity** $\tilde{F}=\tilde{\nabla}^{\natural}\tilde{A}-\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{A})$; they are not equations of motion. To vary $\tilde{F}$ into the field equation one must impose that identity as a constraint, and the multiplier one introduces for it is precisely the potential. This is worked out in the next section.

The natural variable, in short, is not the canonical variable. That is the structural difference from the Dirac case and the reason the rest of the article must pass through the potential.

## Gauge Freedom and the Two Formulations

The potential is not unique. Two potentials give the same field strength when they differ by

$$
\tilde{A}'=\tilde{A}-\tilde{\nabla}\Gamma,
$$

with $\Gamma$ an arbitrary scalar function. The scalar part

$$
S=\mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde{A}\right)
$$

is the gauge degree of freedom of the companion article: it transforms as

$$
S'=S-\Box\Gamma,
$$

and the field strength is invariant, $\tilde{F}'=\tilde{F}$. The companion article states plainly that $S$ "is a gauge artifact" and that the **Lorenz gauge** $S=0$ is "a choice of gauge, not a physical condition". In that gauge the potential obeys the second-order equation

$$
\Box\tilde{A}=-\mu\tilde{R}',\qquad \tilde{R}'=ic\rho+\vec J.
$$

Two equivalent formulations of the classical theory are therefore available, and the choice matters for quantization.

**The second-order, potential formulation.** The field is $\tilde{A}$; the Lagrangian density in natural units is $\mathcal{L}=-\tfrac14 F_{\mu\nu}F^{\mu\nu}$; it is second order, and it is the formulation in which the Legendre transform and the canonical momentum are defined. This is the route the rest of the article follows.

**The first-order, Palatini formulation.** If one wants the field strength to remain the independent variable, one takes $\tilde{F}$ and $\tilde{A}$ as independent and uses the first-order action

$$
S=\int d^4x\left[-F_{\mu\nu}\,\partial^\mu A^\nu+\tfrac14 F_{\mu\nu}F^{\mu\nu}\right].
$$

Varying with respect to $A_\nu$ gives $\partial/\partial Q_\mu F^{\mu\nu}=0$, the inhomogeneous Maxwell equations, and varying with respect to $F_{\mu\nu}$ gives $F_{\mu\nu}=\partial/\partial Q_\mu A_\nu-\partial/\partial Q_\nu A_\mu$, the definition that makes the homogeneous equations automatic; on shell the integrand is $-\tfrac14F_{\mu\nu}F^{\mu\nu}$. The field strength is present as an independent variable, but the potential reappears as its Lagrange multiplier, carrying no kinetic term of its own. The gauge freedom is not removed by this route; it is relocated. There is no local action in four dimensions in which the gauge-invariant field strength alone is varied and Maxwell's equations, rather than $\tilde{F}=0$, follow.

This is the first finding of the article. The biquaternion formulation writes the theory in its most compact and most covariant form, first order in a gauge-invariant object; canonical quantization cannot start from that object. It must either return to the potential and accept the gauge redundancy, or use the first-order formulation and accept the potential as a multiplier. In neither case does the algebra supply the missing structure.

## The Constraint Structure

The Legendre transform of the potential formulation is singular, and the singularities are of a different kind from the Dirac case. In natural units and with the metric $\eta=\mathrm{diag}(-1,+1,+1,+1)$, the conjugate momenta are

$$
\pi^\mu=\frac{\partial\mathcal{L}}{\partial(\partial/\partial Q_t A_\mu)}=-F^{t\mu},
$$

so that

$$
\pi^0=0,\qquad \vec\pi=-i\vec E.
$$

The vanishing of $\pi^0$ is a **primary constraint**: the time component of the potential has no conjugate momentum, because $\mathcal{L}$ contains no time derivative of $A_0$. It is not the end of the story. The Hamiltonian, after integrating by parts, is

$$
\mathcal{H}=\tfrac12\left(\vec E^2+\vec B^2\right)-A_0\,\mathrm{div}\,\vec\pi,
$$

in which $A_0$ appears as a Lagrange multiplier. Consistency of the primary constraint with the evolution requires $\mathrm{div}\,\vec\pi\approx0$, which is **Gauss's law**, and it is a **secondary constraint**. The two constraints

$$
\pi^0\approx0,\qquad \mathrm{div}\,\vec\pi\approx0
$$

are **first class**: their Poisson bracket with each other vanishes, and each generates a gauge transformation of the potential. Because they are first class, the theory is not a theory of four vector-field components; the physical content is the gauge orbit, not the orbit's representatives.

Counting degrees of freedom makes the point. The phase space of the four components of $A_\mu$ has $4\times2=8$ dimensions. A first-class constraint removes two phase-space dimensions — the constraint itself and the gauge direction it generates — so two first-class constraints remove four, leaving $8-4=4$ phase-space dimensions, that is, **two field degrees of freedom** at each point. These are the two transverse polarizations.

The contrast with the Dirac field is exact and should be set beside it. There the conjugate momentum was $\pi=i\psi^\dagger$, algebraically tied to the field by the **second-class** constraint $\chi=\pi-i\psi^\dagger\approx0$; the momentum was not independent, and the gauge freedom was absent, but the bracketing had to become anticommutation. Here the momentum is independent in its spatial components, one entire component of it vanishes, and a divergence constraint appears; the constraint is first class, gauge freedom is present, and the bracketing stays commutation. Both theories have singular Legendre transforms. The singularity of the Dirac case forces a different bracket; the singularity of the Maxwell case forces a choice of gauge.

## The Constraints in Biquaternion Notation

The two constraints have a compact form in the notation of the companion articles. Let $\tilde{\pi}$ be the biquaternion whose components are the canonical momenta conjugate to $\tilde{A}$:

$$
\tilde{\pi}=\pi^0e_t+\vec\pi,\qquad \pi^0=0,\qquad \vec\pi=-i\vec E.
$$

Then $\pi^0=0$ is the statement that the **scalar part** of $\tilde{\pi}$ vanishes,

$$
\mathrm{Sc}(\tilde{\pi})\approx0,
$$

and Gauss's law is a scalar-part condition as well. A direct computation of the quaternion product gives

$$
\mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde{\pi}\right)=\partial/\partial Q_t\,\pi^0+\mathrm{div}\,\vec\pi,
$$

so that on the constraint surface, where $\pi^0\approx0$,

$$
\mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde{\pi}\right)\approx0.
$$

The two constraints are therefore the scalar parts of $\tilde{\pi}$ and of $\tilde{\nabla}^{\natural}\tilde{\pi}$. This is the same shape as the **integrability condition** of the companion article, $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{R})=0$, which expresses charge conservation; Gauss's law and charge conservation are written with the same operator. That is a genuine feature of the notation: the constraint is not an extra object appended to the algebra but a scalar-part projection that already appears in it.

The gauge freedom, correspondingly, is the freedom to add $\tilde{\nabla}\Gamma$ to $\tilde{A}$; it lives in the scalar direction of the material sector, and $S=\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{A})$ is its field. The physical field strength is the **vector part** of $\tilde{\nabla}^{\natural}\tilde{A}$, invariant under the transformation, and the framework's own account says the scalar part is not physical.

Two points about this interpretation must be kept separate.

The first is a **structural observation**, and it is suggestive but convention-dependent. The potential $\tilde{A}=i\phi/c\,e_t+\vec A$ has an imaginary scalar part and a real vector part: it is an element of the material sector $\mathbb{M}_-$. The conjugate momentum $\tilde{\pi}$ has a vanishing (real) scalar part and a purely imaginary vector part: in the $ict$ convention it is an element of the complementary sector $\mathbb{M}_+$. The canonical pair thus straddles the two sectors that the framework distinguishes as material and informational — the same pairing of "configuration" and "operator" that the article on $\mathbb{M}_+$ describes for its action on $\mathbb{M}_-$. Whether this is a meaningful statement about the algebra or a consequence of writing the momentum with the $ict$ derivative is not decided here, and it is recorded as an open question. In a real-time formulation the momentum of the same theory is real, and the placement reverses; the physical content is unchanged.

The second is the **finding**. Nothing in the algebra selects a gauge. The gauge-invariant content of the theory is a functional of $\tilde{F}$ alone, and $\tilde{F}$ is invariant under every gauge transformation; so no gauge-invariant functional of $\tilde{A}$ — no biquaternion norm, no trace, no conjugation built from the basis and $i$ — can break the degeneracy, because any such functional is a function of $\tilde{F}$. The Lorenz condition $S=0$ is available and is the framework's covariant choice, but the companion article itself declines to make it physical, and the algebra offers no principle that prefers it to $A_0=0$ (the temporal gauge) or to any other. The gauge must be fixed from outside the algebra. This is the sense in which the biquaternion framework cannot quantize Maxwell "automatically".

## Gupta–Bleuler Quantization

Covariant quantization proceeds with all four polarizations and imposes a subsidiary condition. Expand the free potential in plane waves,

$$
A_\mu(x)=\int\!\frac{d^3k}{(2\pi)^3}\frac{1}{\sqrt{2\omega_k}}\sum_{r=0}^{3}
\left[\epsilon^{(r)}_\mu(\vec k)\,a^{\mathrm{fop}}_r(\vec k)\,\exp(-ik\cdot x)
+\epsilon^{(r)*}_\mu(\vec k)\,a^{\mathrm{fop}\dagger}_r(\vec k)\,\exp(+ik\cdot x)\right],
$$

with $\omega_k=|\vec k|$ for the massless field and with polarization vectors normalized as $\eta_{\mu\nu}\epsilon^{(r)\mu}\epsilon^{(s)\nu}=\zeta_r\delta_{rs}$, where $(\zeta_0,\zeta_1,\zeta_2,\zeta_3)=(-1,+1,+1,+1)$. The mode operators carry the corresponding commutators,

$$
\big[a^{\mathrm{fop}}_r(\vec k),a^{\mathrm{fop}\dagger}_s(\vec k')\big]
=\zeta_r\,\delta_{rs}\,(2\pi)^3\delta^{(3)}(\vec k-\vec k'),
$$

with all other commutators vanishing. The signs are not optional: the timelike mode has $\zeta_0=-1$, so the one-particle state $a^{\mathrm{fop}\dagger}_0|0\rangle$ has **negative norm**, $\langle0|a^{\mathrm{fop}}_0a^{\mathrm{fop}\dagger}_0|0\rangle=-1$. The longitudinal mode has positive norm, as do the two transverse modes.

The negative-norm states are removed by a **subsidiary condition**. The Lorenz gauge condition $S=0$ is imposed on the positive-frequency part of the field,

$$
\mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}A\right)^{(+)}|\psi\rangle=0,
$$

which for a mode with momentum along $\vec e_z$ reduces to

$$
\big(a^{\mathrm{fop}}_0(\vec k)-a^{\mathrm{fop}}_3(\vec k)\big)|\psi\rangle=0 .
$$

This condition does not set the timelike and longitudinal excitations to zero individually; it leaves the combination $a^{\mathrm{fop}\dagger}_0-a^{\mathrm{fop}\dagger}_3$. That combination is annihilated by the condition,

$$
\big(a^{\mathrm{fop}}_0-a^{\mathrm{fop}}_3\big)\big(a^{\mathrm{fop}\dagger}_0-a^{\mathrm{fop}\dagger}_3\big)|0\rangle
=\big(\zeta_0+\zeta_3\big)|0\rangle=0,
$$

and it has **zero norm**,

$$
\big\|\big(a^{\mathrm{fop}\dagger}_0-a^{\mathrm{fop}\dagger}_3\big)|0\rangle\big\|^2
=\zeta_0+\zeta_3=-1+1=0,
$$

so, lying in the physical subspace and being null, it is orthogonal to every state in that subspace and decouples from all physical amplitudes. On the quotient by the zero-norm states, the physical subspace has **positive-definite norm** and consists exactly of the two transverse polarizations. Their polarization sum is the transverse projector,

$$
\sum_{\lambda=1}^{2}\epsilon_i^{(\lambda)}(\vec k)\,\epsilon_j^{(\lambda)}(\vec k)
=\delta_{ij}-\vec{u_k}_i\vec{u_k}_j,
$$

which makes the physical field transverse: the polarization sum annihilates every component along $\vec u_k$.

This is the quantization, and it works: two transverse polarizations, no negative-norm physical states, a positive-definite physical inner product. But the machinery was imported. The subsidiary condition is a condition on the potential, and the framework does not supply it; the indefinite inner product with $\zeta_0=-1$ is a structure the algebra does not by itself demand. The one compensating observation is the one made above: the signature $(-,+,+,+)$ of that inner product is the signature of the biquaternion norm on $\mathbb{M}_-$, the $ict$ spacetime metric the framework already carries, so the indefinite metric is not a new object but the framework's own. Whether that identification has content beyond the coincidence of signatures is open.

The alternatives should be named. The **Coulomb gauge** $\mathrm{div}\,\vec A=0$ removes the gauge freedom non-covariantly, leaves only the two transverse modes from the start, and gives a manifestly positive-definite norm, at the price of an instantaneous interaction and a loss of manifest Lorentz covariance. It is the same physical theory; it differs in which structure is imposed by hand. The framework's covariance preference points at Gupta–Bleuler, but the preference is not a derivation.

## Comparison with the Scalar Field

The counting is worth setting beside the scalar field, because the difference is where the gauge structure lives. A real scalar field $\phi$ of mass $m$ has conjugate momentum $\pi=\partial\phi/\partial t$, the canonical commutator $[\phi^{\mathrm{fop}}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z),\pi^{\mathrm{fop}}(\vec y)]=i\delta^{(3)}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-\vec y)$, and a mode expansion with **one** polarization,

$$
\big[a^{\mathrm{fop}}(\vec k),a^{\mathrm{fop}\dagger}(\vec k')\big]=(2\pi)^3\delta^{(3)}(\vec k-\vec k'),
$$

with dispersion $\omega_k=\sqrt{\vec k^2+m^2}$. Its Fock space has positive-definite norm, there is no constraint, and no gauge condition has to be imposed: the Legendre transform is regular. The massless scalar field has one mode. The photon has **two** physical transverse modes and reaches them only after the two unphysical modes — the timelike and the longitudinal — have been removed by a subsidiary condition. The photon is not a scalar particle with an extra label; the reduction from four components to two is performed by the gauge structure, and that structure is what the algebra does not fix. If the gauge field is given a mass, as in the Proca theory, the gauge freedom is absent, the constraint structure changes, and a third (longitudinal) polarization becomes physical — which shows that the two-polarization count is a consequence of the gauge symmetry, not of the number of field components.

## Comparison with the Dirac Case

The two quantizations may now be set side by side.

- **The constraint.** The Dirac field carries a **second-class** constraint $\pi-i\psi^\dagger\approx0$: the momentum is algebraically tied to the field. The Maxwell field carries two **first-class** constraints, $\pi^0\approx0$ and $\mathrm{div}\,\vec\pi\approx0$: the momentum is largely independent, one component of it vanishes, and the constraints generate gauge transformations.
- **The bracket.** Second-class constraints force the bracket to be changed, and positivity forces the change to be to **anticommutators**; the Dirac field is fermionic. First-class constraints leave the bracket a **commutator** and instead require a gauge choice; the Maxwell field is bosonic.
- **The added structure.** The Dirac quantization required a $\mathbb{Z}/2$ grading that the algebra does not supply and had to impose it on the mode algebra. The Maxwell quantization requires no new algebraic structure at all: the scalar imaginary already supplies the phase, the modes commute, and the indefinite metric needed for the covariant treatment is the framework's own spacetime metric.
- **The natural variable.** In the Dirac case the natural variable of the biquaternion equation is the field that is quantized. In the Maxwell case it is not: $\tilde{F}$ is gauge invariant and first order, and the passage to canonical variables reintroduces the potential and its redundancy.

The verdict is therefore not a ranking. **Maxwell is a transcription of standard canonical quantization, exactly as the Dirac case was, but its obstruction is the opposite kind.** Dirac was blocked by a structure the algebra does not contain; Maxwell is blocked by a redundancy the algebra does not remove. The first asks for an addition to the algebra; the second asks for a gauge-fixing principle that the algebra declines to provide. Which of those is more hopeful for the research program is a question this article cannot answer, but the two are not the same question, and the Dirac article's phrase "not canonical" applies here with a different meaning.

## What Is Standard and What Is Open

**Standard, and transcribed here.** The single biquaternion Maxwell equation $\tilde{\nabla}\tilde{F}=-\tilde{R}$ and the real/imaginary separation of the homogeneous and inhomogeneous equations; the gauge transformation and the transformation of $S$; the second-order potential equation in the Lorenz gauge; the first-order Palatini action and the two variations; the conjugate momenta $\pi^\mu=-F^{t\mu}$, the primary constraint $\pi^0\approx0$, the Gauss-law secondary constraint, and the first-class character of both; the degree-of-freedom count giving two field degrees of freedom; the Gupta–Bleuler mode expansion, commutators, subsidiary condition, zero-norm unphysical combination, transverse polarization sum, and positive-definite physical norm. None of this is new, and none of it depends on the biquaternion structure beyond the kinematical conventions of the companion articles.

**Open, and not settled here.**

- **The gauge-fixing principle.** The framework gives no algebraic reason to prefer $S=0$ to any other gauge, or to prefer Gupta–Bleuler to the Coulomb gauge. Whether a biquaternionic principle exists is the central open question. The companion article's judgement that $S$ is a gauge artifact is a negative statement, not a mechanism.
- **The intrinsic Lagrangian and pairings.** The parent Dirac article records that the $\mathbb{B}$-intrinsic Lagrangian and conjugate momentum are not fixed by the algebra. The same is true here, and more sharply, because the natural variable $\tilde{F}$ has no canonical partner at all. Whether a real-scalar Lagrangian built from the trace and norm pairings reproduces the standard constraint structure is not shown.
- **The biquaternion Fock space.** Whether there is a Fock space native to $\mathbb{B}$, rather than the exterior (fermionic) or symmetric (bosonic) algebra of a module's solution space, is the subject of the planned companion article on the Fock space.
- **The photon.** Whether the two transverse polarizations have a native meaning in the algebra — for instance, in the vector part of the material sector — is the subject of the planned article on the photon.
- **The sector straddle.** Whether $\tilde{A}\in\mathbb{M}_-$ and $\tilde{\pi}\in\mathbb{M}_+$ has algebraic content or is a convention effect is undecided.
- **The vacuum energy.** As in the Dirac case, whether the algebra singles out a regularization or a geometric meaning for the zero-point energy is open.
- **Empirical content.** Whether any of this yields a prediction distinguishing it from standard quantum electrodynamics is the unanswered framework-level question.

## Summary

The biquaternion Maxwell equation $\tilde{\nabla}\tilde{F}=-\tilde{R}$ is first order, and its natural variable $\tilde{F}=i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H$ is gauge invariant; its real and imaginary parts separate the homogeneous and the inhomogeneous Maxwell equations. But $\tilde{F}$ has no canonical partner, and no local Lagrangian in four dimensions produces the field equation by varying $\tilde{F}$ alone. Canonical quantization must therefore return to the potential $\tilde{A}$, and with it the gauge freedom $\tilde{A}'=\tilde{A}-\tilde{\nabla}\Gamma$, whose field is $S=\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{A})$ with $S'=S-\Box\Gamma$.

The Legendre transform is singular. The conjugate momenta are $\pi^\mu=-F^{t\mu}$, so $\pi^0\approx0$ is primary and Gauss's law $\mathrm{div}\,\vec\pi\approx0$ is secondary; both are **first class** and generate gauge transformations. The phase-space count $8-2\times2=4$ gives two field degrees of freedom. In the notation of the companion articles the constraints are $\mathrm{Sc}(\tilde{\pi})\approx0$ and $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{\pi})\approx0$, the same scalar-part shape as the charge-conservation condition $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{R})=0$.

Covariant quantization is Gupta–Bleuler: four polarizations with commutators $[a^{\mathrm{fop}}_r,a^{\mathrm{fop}\dagger}_s]=\zeta_r\delta_{rs}(2\pi)^3\delta^{(3)}$, $\zeta=(-1,+1,+1,+1)$, so the timelike mode has negative norm; the subsidiary condition $(a^{\mathrm{fop}}_0-a^{\mathrm{fop}}_3)|\psi\rangle=0$ leaves the zero-norm combination $a^{\mathrm{fop}\dagger}_0-a^{\mathrm{fop}\dagger}_3$, which decouples, and the physical subspace has positive-definite norm and exactly the two transverse polarizations, with $\sum_{\lambda=1}^2\epsilon_i^\lambda\epsilon_j^\lambda=\delta_{ij}-\vec{u_k}_i\vec{u_k}_j$. By comparison a real scalar field has one mode, no constraint, and positive norm. The two-polarization count follows from the gauge symmetry, not from the number of components.

The extension is a transcription of standard canonical quantization into the framework's notation, not a derivation of the quantized structure from $\mathbb{B}$. Unlike the Dirac case it requires no new grading, but unlike the Dirac case the natural variable is not the canonical one, and the gauge must be fixed from outside the algebra. The framework cannot quantize the Maxwell field automatically.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^2=-e_t$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_+,\mathbb{M}_-$ | Informational (Hermitian) and material (anti-Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\tilde{\nabla}=e_t\partial/\partial Q_t+\vec e_x\partial/\partial Q_x+\vec e_y\partial/\partial Q_y+\vec e_z\partial/\partial Q_z$ | Biquaternionic gradient |
| $\tilde{\nabla}^{\natural}$ | Quaternion-conjugate gradient |
| $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}=\tilde{\nabla}^{\natural}\tilde{\nabla}$ | d'Alembertian |
| $\tilde{A}=i\phi/c\,e_t+\vec A$ | Potential biquaternion (in $\mathbb{M}_-$) |
| $\tilde{F}=i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H$ | Field-strength biquaternion (vanishing scalar part) |
| $\tilde{R}=\frac{i\rho}{\sqrt{\epsilon}}e_t+\sqrt{\mu}\vec J$ | Source biquaternion |
| $\tilde{\nabla}\tilde{F}=-\tilde{R}$ | Biquaternionic Maxwell equation |
| $\Gamma$ | Gauge function, $\tilde{A}'=\tilde{A}-\tilde{\nabla}\Gamma$ |
| $S=\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{A})$, $S'=S-\Box\Gamma$ | Gauge degree of freedom; Lorenz gauge $S=0$ |
| $\eta=\mathrm{diag}(-1,+1,+1,+1)$ | $ict$ spacetime metric; biquaternion norm on $\mathbb{M}_-$ |
| $\mathcal{L}=-\tfrac14 F_{\mu\nu}F^{\mu\nu}$ | Maxwell Lagrangian density (potential formulation) |
| $\pi^\mu=\partial\mathcal{L}/\partial(\partial/\partial Q_t A_\mu)=-F^{t\mu}$ | Conjugate momenta: $\pi^0\approx0$, $\vec\pi=-i\vec E$ |
| $\tilde{\pi}=\pi^0e_t+\vec\pi$ | Momentum biquaternion |
| $\mathrm{Sc}(\tilde{\pi})\approx0$, $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{\pi})\approx0$ | Primary and Gauss-law constraints, both first class |
| $A_\mu$, $\epsilon^{(r)}_\mu$, $a^{\mathrm{fop}}_r,a^{\mathrm{fop}\dagger}_r$ | Quantized potential, polarization vectors, mode operators |
| $[a^{\mathrm{fop}}_r(\vec k),a^{\mathrm{fop}\dagger}_s(\vec k')]=\zeta_r\delta_{rs}(2\pi)^3\delta^{(3)}$ | Mode commutator, $\zeta=(-1,+1,+1,+1)$ |
| $(a^{\mathrm{fop}}_0-a^{\mathrm{fop}}_3)|\psi\rangle=0$ | Gupta–Bleuler subsidiary condition (momentum along $\vec e_z$) |
| $\sum_{\lambda=1}^2\epsilon_i^\lambda\epsilon_j^\lambda=\delta_{ij}-\vec{u_k}_i\vec{u_k}_j$ | Transverse polarization sum |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace pairing of the informational sector |

## Further Reading

- S. N. Gupta, "Theory of longitudinal photons in quantum electrodynamics," *Proceedings of the Physical Society A* **63** (1950) 681–691, and K. Bleuler, "Eine neue Methode zur Behandlung der longitudinalen und skalaren Photonen," *Helvetica Physica Acta* **23** (1950) 567–586, for the indefinite-metric quantization and the subsidiary condition.
- P. A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for first-class and second-class constraints and the constraint algorithm.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), and C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the canonical quantization of the electromagnetic field and the Coulomb-gauge treatment.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), and S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the Gupta–Bleuler construction and the physical-state condition.
- F. Strocchi, *An Introduction to the Non-Perturbative Foundations of Quantum Field Theory* (Oxford, 2013), for the constraint and gauge-structure analysis on which the first-class counting rests.
- I. Białynicki-Birula and Z. Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism," *Journal of Physics A* **46** (2013) 053001, for the complex-vector formulation and its quantization.
- L. A. Alexeyeva, "Maxwell Equations, Their Hamiltonian and Biquaternionic Forms and Properties of Their Solutions" (2016), for the biquaternionic Maxwell equation and the operator factorization used here.
- Companion articles: *Maxwell's Equations in the Biquaternionic Formulation*; *Canonical Quantization of the Biquaternion Dirac Field*; *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*; *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*.
