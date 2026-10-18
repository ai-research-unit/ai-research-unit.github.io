# __Canonical Quantization of the Biquaternion Klein–Gordon Field__

## Introduction

The companion article *The Klein–Gordon Equation in Biquaternionic Form* closes on a two-fold defect. The equation $\left(\Box-m^2c^2/\hbar^2\right)\tilde{\Phi}=0$ is second order in the time coordinate and has no first-order square root inside $\mathbb{B}$, and its conserved density is not positive definite, so that it admits no one-particle interpretation, the negative-frequency branch carrying the sign of the frequency. Canonical quantization is the standard resolution of both defects at once: the field becomes an operator, the negative-frequency branch becomes an antiparticle branch, and the non-positive density becomes the charge of a many-particle theory. This article carries that resolution out for the framework's scalar field.

Its question is the one the Dirac and Maxwell companion articles asked for their own fields: how much of the second-quantized structure is supplied by the algebra $\mathbb{B}$, and how much is transcribed from standard quantum field theory? The answer for the scalar is the cleanest of the three, and it is largely negative in a way that is worth stating at the outset.

- **The standard part.** The Lagrangian, the Legendre transform, the equal-time commutators, the mode expansion, the mode algebra, the Hamiltonian, the normal-ordering constant and the conserved charge are textbook quantum field theory, transcribed into the notation of this series. None of it is new, and none of it depends on the biquaternion structure beyond the kinematical conventions already fixed by the companion articles.
- **The structural finding.** The scalar field takes values in the **centre** $\mathbb{C}_{\mathbb{B}}$ of the algebra, and the algebra supplies no bosonic ladder of its own. The companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* proves that no pair $a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}\in\mathbb{B}$ satisfies $[a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}]=e_t$: the trace of a commutator vanishes while $\mathrm{Tr}(e_t)=2$. The mode algebra of the quantized scalar field is therefore the Weyl algebra of an imported module, not an object of $\mathbb{B}$. Where the Dirac field needed a $\mathbb{Z}/2$ grading that the algebra does not contain, and the Maxwell field needed a gauge-fixing principle that the algebra does not supply, the scalar field needs nothing from the algebra at all — and that is itself the finding.
- **The open part.** The $\mathbb{B}$-intrinsic operator field, the intrinsic Lagrangian and conjugate momentum, the biquaternion Fock space, and the regularization of the vacuum energy are not settled here, exactly as in the two parent quantizations.

The article is organised as follows. The next section fixes the classical field, its action and its conjugate momentum, and records why the Legendre transform is regular here — unlike both the Dirac and the Maxwell cases. The following section reads the field as a central-valued object and fixes the mass shell as a level set of the biquaternion norm. The next section states the equal-time commutation relations and the reasons they are commutators. The section after that carries out the expansion in the plane waves of the parent equation. The next section derives the mode algebra and the Fock space, and states the bosonic obstruction. A section gives the Hamiltonian, the four-momentum and the charge. The following section treats the commutator function and microcausality. The article closes with an explicit accounting of what is standard and what is open.

- Companion article *The Klein–Gordon Equation in Biquaternionic Form*, for the field equation, its two frequency branches, the mass-shell condition, and the conserved current.
- Companion article *Noether's Theorem in Biquaternionic Form*, for the scalar Lagrangian, its central scalar form, the $\mathrm{U}(1)$ current $\tilde J\in\mathbb{M}_-$, and the energy–momentum tensor.
- Companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the material four-wavevector, the biquaternion norm, and the $ict$ coordinate.
- Companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, for the trace argument against a bosonic mode in $\mathbb{B}$, and for the exterior and symmetric algebras as the fermionic and bosonic Fock spaces.
- Companion article *The Spin–Statistics Theorem in Biquaternionic Form*, for the connection between spin and the choice of bracket.
- Companion article *Canonical Quantization of the Biquaternion Dirac Field*, for the contrasting constrained quantization and the grading the algebra does not supply.
- Companion article *Canonical Quantization of the Biquaternion Maxwell Field*, for the contrasting first-class constraints and the gauge redundancy the algebra does not remove.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_t=1,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_\mu^2=-e_t$ and $\vec e_\mu \vec e_\nu=-\delta_{\mu\nu}e_t+\varepsilon_{\mu\nu\lambda}\vec e_\lambda$, and $i$ is the scalar imaginary with $i^2=-1$, commuting with every $\vec e_\mu$. The material (anti-Hermitian) and informational (Hermitian) sectors are $\mathbb{M}_-$ and $\mathbb{M}_+$, with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ and $i\mathbb{M}_\pm=\mathbb{M}_\mp$; the centre is $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_t,ie_t\}$. The conjugations are ${}^{\natural}$ (quaternion), $\bar{\cdot}$ (complex), ${}^{*}=({}^{\natural})^{\,*}$ (Hermitian) and ${}^\flat=-{}^{*}$. The biquaternionic gradient is $\tilde{\nabla}=e_t\partial/\partial Q_t+\vec e_x\partial/\partial Q_x+\vec e_y\partial/\partial Q_y+\vec e_z\partial/\partial Q_z$, its quaternion conjugate is $\tilde{\nabla}^{\natural}=e_t\partial/\partial Q_t-\vec e_x\partial/\partial Q_x-\vec e_y\partial/\partial Q_y-\vec e_z\partial/\partial Q_z$, and $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}=\tilde{\nabla}^{\natural}\tilde{\nabla}=\partial^2/\partial Q_t^2+\Delta=\Delta+ \partial^2/\partial Q_t^2$. The trace formula is $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$, normalized so that $\mathrm{Tr}(e_t)=2$ in the matrix representation $\mathbb{B}\cong M_2(\mathbb{C})$. The spacetime metric of the $ict$ sector is $\eta=\mathrm{diag}(-1,+1,+1,+1)$ (level 2), and the mass parameter is $\mu=mc/\hbar$. The analytic parts use natural units $\hbar=c=1$, as the parent articles do; dimensionful factors are restored where they carry meaning.

## The Classical Field and Its Conjugate Momentum

The relativistic scalar field of the framework is the central-valued complex field

$$
\tilde{\Phi}(\tilde{R})=\phi(\tilde{R})\,e_t,\qquad \phi:\mathbb{R}^{1,3}\to\mathbb{C},
$$

with $\tilde{R}=ict\,e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z\in\mathbb{M}_-$. Its action is $S[\tilde{\Phi}]=\int\mathcal{L}\,d^4x$ with the real Lagrangian density established by the companion article *Noether's Theorem in Biquaternionic Form*,

$$
\mathcal{L}=-\,\mathrm{Sc}\!\left[(\tilde{\nabla}^{\natural}\tilde{\Phi}^{*})(\tilde{\nabla}\tilde{\Phi})\right]
-\frac{m^2c^2}{\hbar^2}\,\mathrm{Sc}\!\left[\tilde{\Phi}^{*}\tilde{\Phi}\right]
=-\,(\partial/\partial Q_t\,\phi^*)(\partial/\partial Q_t\,\phi)-\sum_k(\partial/\partial Q_k\,\phi^*)(\partial/\partial Q_k\,\phi)-\mu^2\phi^*\phi .
$$

Because $\partial/\partial Q_t=-\tfrac{i}{c}\partial/\partial t$, the Lagrangian written in the physical time is

$$
\mathcal{L}=\frac{1}{c^2}|\partial\phi/\partial t|^2-|\nabla\phi|^2-\mu^2|\phi|^2 .
$$

The **conjugate momentum** is

$$
\pi=\frac{\partial\mathcal{L}}{\partial\left(\partial\phi/\partial t\right)}=\frac{1}{c^2}\left(\partial\phi/\partial t\right)^{\,*},\qquad
\pi^\dagger=\frac{\partial\mathcal{L}}{\partial\left(\partial\phi/\partial t\right)^{\,*}}=\frac{1}{c^2}\partial\phi/\partial t,
$$

and the Legendre transform is **regular**: $\pi$ determines $\partial\phi/\partial t$ and conversely, so the phase space is the full space of pairs $(\phi,\pi)$ and no constraint appears. This is the first point of contrast with the two parent quantizations. The Dirac field carried a **second-class** constraint, $\pi-i\psi^\dagger\approx0$, because its equation is first order in time; the Maxwell field carried two **first-class** constraints, $\pi^0\approx0$ and $\mathrm{div}\,\vec\pi\approx0$, because its potential is a gauge field. The scalar field carries neither. Its equation is second order, so the momentum is independent, and its field is single-component, so there is no gauge redundancy to remove. The canonical structure is therefore taken over from the classical theory without modification — which is the technical reason the quantization below is a transcription with no obstruction and no new structure.

The equation of motion obtained by varying the action is the parent's biquaternion Klein–Gordon equation,

$$
\left(\Box-\mu^2\right)\tilde{\Phi}=0 .
$$


## The Field as a Central-Valued Object

The value space of the field is the centre, and the reason is structural rather than chosen. A field of spin $0$ carries no Lorentz index; in a framework whose state module is the two-dimensional spinor module, a field that carries no spinor index is a field whose values commute with every element of the algebra, which is to say a central-valued field. Written in real components, the complex scalar is two real scalars, one in each sector's scalar direction,

$$
\tilde{\Phi}=\frac{1}{\sqrt2}\Big(\underbrace{\phi_1\,e_t}_{\in\,\mathbb{M}_+}+\underbrace{\phi_2\,ie_t}_{\in\,\mathbb{M}_-}\Big),
\qquad
\mathrm{Sc}\!\left(\tilde{\Phi}^{*}\tilde{\Phi}\right)=\frac12\left(\phi_1^2+\phi_2^2\right),
$$

with $\phi_1,\phi_2$ the two real scalar fields of the sector in the normalization in which the kinetic term is $\frac12[(\partial\phi_1)^2+(\partial\phi_2)^2]$ — the component normalization that the companion articles on the quantized field and on symmetry breaking use throughout — and the complex structure that makes the two into a single complex field is the central scalar imaginary $i$. The scalar field is, in this precise sense, the field of the centre; the spinor module on which the Dirac field lives is not involved.

The quadratic form of the theory is the biquaternion norm. The material four-wavevector is

$$
\tilde P/\hbar=i\frac{\omega}{c}\,e_t+\vec k\in\mathbb{M}_-,
\qquad
\tilde P^{\natural}/\hbar=i\frac{\omega}{c}\,e_t-\vec k,
\qquad
\langle\tilde P/\hbar\rangle_{\natural}=\tilde P\tilde P^{\natural}/\hbar^{2}=\left(-\frac{\omega^2}{c^2}+\vec k^2\right)e_t ,
$$

and the plane-wave phase is the scalar part $\mathrm{Sc}(\tilde P\tilde R^{\natural})/\hbar=\vec k\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)-\omega t$. Substituting $\tilde{\Phi}=\phi_0\exp(i\mathrm{Sc}(\tilde P\tilde R^{\natural})/\hbar)e_t$ into $\left(\Box-\mu^2\right)\tilde{\Phi}=0$ gives $\omega^2/c^2-\vec k^2=\mu^2$, which is the mass-shell condition

$$
\langle\tilde P/\hbar\rangle_{\natural}=-\frac{m^2c^2}{\hbar^2}\,e_t .
$$


## Equal-Time Commutation Relations

Quantization promotes the classical field and its momentum to operators $\phi^{\mathrm{fop}}$, $\phi^{\mathrm{fop}\dagger}$, $\pi^{\mathrm{fop}}$, $\pi^{\mathrm{fop}\dagger}$ and imposes equal-time brackets. Because the field is complex, $\phi$ and $\phi^\dagger$ are independent, and the canonical relations are

$$
\big[\phi^{\mathrm{fop}}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t),\pi^{\mathrm{fop}}(\vec y,t)\big]
=\big[\phi^{\mathrm{fop}\dagger}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t),\pi^{\mathrm{fop}\dagger}(\vec y,t)\big]
=i\hbar\,\delta^{(3)}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-\vec y),
$$

with

$$
\big[\phi^{\mathrm{fop}},\phi^{\mathrm{fop}}\big]=\big[\phi^{\mathrm{fop}},\phi^{\mathrm{fop}\dagger}\big]
=\big[\pi^{\mathrm{fop}},\pi^{\mathrm{fop}\dagger}\big]=\big[\pi^{\mathrm{fop}},\pi^{\mathrm{fop}}\big]=0 ,
\qquad
\big[\phi^{\mathrm{fop}},\pi^{\mathrm{fop}\dagger}\big]=\big[\phi^{\mathrm{fop}\dagger},\pi^{\mathrm{fop}}\big]=0 ,
$$

the last two being the cross relations of each of the two independent fields with the momentum conjugate to the other.

In natural units, where $\pi=\left(\partial\phi/\partial t\right)^{\dagger}$, the first relation reads $[\phi^{\mathrm{fop}}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t),\left(\partial\phi^{\mathrm{fop}}/\partial t\right)^{\dagger}(\vec y,t)]=i\delta^{(3)}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-\vec y)$.

The brackets are **commutators**, and the choice is forced, as the companion article *The Spin–Statistics Theorem in Biquaternionic Form* establishes; the three operative reasons may be stated compactly. **Boundedness of the energy:** a commutator makes the particle and antiparticle contributions to the Hamiltonian both positive, whereas an anticommutator would give opposite signs and an energy unbounded below. **Microcausality:** for a spin-$0$ field it is the commutator $[\phi^{\mathrm{fop}}(x),\phi^{\mathrm{fop}\dagger}(y)]$ that must vanish outside the light cone, and it does; the anticommutator does not, and quantizing with it would correlate causally disconnected measurements. **Positivity of the norm:** the symmetric Fock space built on the one-particle space has positive-definite inner product, while the antisymmetric projection of a bosonic one-particle space is not the structure the field equation's solution space supports. The three reasons point the same way for a field of integer spin; the general theorem is not rederived here.

The scalar case has one feature the two parent cases do not. Because the field is single-component and the Legendre transform regular, the canonical relation is imposed **directly**, without the Dirac-bracket modification the Dirac field required. There is no constraint surface to project onto and no gauge orbit to fix. What the algebra does not supply is not a constraint resolution but the ladder itself, and that is the subject of the section after next.

## The Mode Expansion

The field equation is linear, so the general solution is a superposition of plane waves. In natural units, with $E_{\vec p}=+\sqrt{\vec p^2+\mu^2}$ and $p\cdot x=E_{\vec p}t-\vec p\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$, the quantized field expands as

$$
\phi^{\mathrm{fop}}(x)=\int\!\frac{d^3p}{(2\pi)^3}\,\frac{1}{\sqrt{2E_{\vec p}}}
\left(a^{\mathrm{fop}}_{\vec p}\,\exp(-ip\cdot x)+{b^{\mathrm{fop}}_{\vec p}}^\dagger\,\exp(+ip\cdot x)\right),
$$

and its adjoint as

$$
\phi^{\mathrm{fop}\dagger}(x)=\int\!\frac{d^3p}{(2\pi)^3}\,\frac{1}{\sqrt{2E_{\vec p}}}
\left(b^{\mathrm{fop}}_{\vec p}\,\exp(-ip\cdot x)+{a^{\mathrm{fop}}_{\vec p}}^\dagger\,\exp(+ip\cdot x)\right).
$$

The operator $a^{\mathrm{fop}}_{\vec p}$ annihilates a particle of momentum $\vec p$ and $b^{\mathrm{fop}}_{\vec p}$ annihilates an antiparticle; the two branches of the parent equation, distinguished by the sign of the frequency, become the particle and antiparticle branches.

The biquaternion form of the expansion is the replacement of the phase $\exp(\mp ip\cdot x)$ by a central unitary element built from the material four-wavevector. With $\tilde P/\hbar=iE_{\vec p}e_t+\vec p$ in natural units, the identity above gives

$$
\mathrm{Sc}\!\left(\tilde P\tilde R^{\natural}\right)/\hbar=\vec p\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)-E_{\vec p}t=-p\cdot x ,
\qquad
\exp(-ip\cdot x)=\exp(\,i\,\mathrm{Sc}(\tilde P\tilde R^{\natural})/\hbar),
\qquad
\exp(+ip\cdot x)=\exp(-i\,\mathrm{Sc}(\tilde P\tilde R^{\natural})/\hbar) .
$$

The exponentials are central, so the mode expansion is a sum of central phases multiplying operators; the field operator at each event is an operator times $e_t$, i.e. it is central-valued as an operator-valued distribution, and the transport of the phase is the framework's own. The normalization $1/\sqrt{2E_{\vec p}}$ and the measure $d^3p/(2\pi)^3$ are the standard Lorentz-invariant ones and are inherited.

For a **real** (neutral) scalar field the field is Hermitian, $\phi^{\mathrm{fop}}=\phi^{\mathrm{fop}\dagger}$, which forces $b^{\mathrm{fop}}_{\vec p}=a^{\mathrm{fop}}_{\vec p}$; there is one set of modes, the field creates and destroys its own antiparticle, and the charge below vanishes identically. For a **complex** (charged) field the two sets are independent. The biquaternion framework does not by itself prefer either: the real field is a Hermitian central-valued operator field, the complex field a pair of them related by the central phase, and the distinction is the standard one.

## The Mode Algebra and the Fock Space

The mode operators inherit their brackets from the equal-time relations. A direct computation gives

$$
\big[a^{\mathrm{fop}}_{\vec p},{a^{\mathrm{fop}}_{\vec k}}^\dagger\big]
=\big[b^{\mathrm{fop}}_{\vec p},{b^{\mathrm{fop}}_{\vec k}}^\dagger\big]
=(2\pi)^3\delta^{(3)}(\vec p-\vec k),
\qquad
\big[a^{\mathrm{fop}}_{\vec p},{b^{\mathrm{fop}}_{\vec k}}^\dagger\big]=0,
$$

with all other commutators vanishing. The equal-time canonical relation is recovered from these: the positive- and negative-frequency branches enter the commutator $[\phi^{\mathrm{fop}}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t),\left(\partial\phi^{\mathrm{fop}}/\partial t\right)^{\dagger}(\vec y,t)]$ with opposite phases, the terms that survive combine into a single momentum integral, and

$$
\big[\phi^{\mathrm{fop}}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t),\pi^{\mathrm{fop}}(\vec y,t)\big]
=i\hbar\int\!\frac{d^3p}{(2\pi)^3}\,\exp(\,i\vec p\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-\vec y))
=i\hbar\,\delta^{(3)}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-\vec y).
$$

The Fock space is the **symmetric** algebra of the one-particle space,

$$
\mathcal{F}=\bigoplus_{n\ge0}\Big(\mathcal{H}_1^{\otimes n}\Big)_{+},
\qquad
\mathcal{H}_1=L^2\!\left(\mathbb{R}^3,\frac{d^3p}{(2\pi)^3\,2E_{\vec p}}\right),
$$

with the occupation basis $|n_{\vec p_1},n_{\vec p_2},\dots\rangle$ and the vacuum $|0\rangle$ annihilated by every $a^{\mathrm{fop}}_{\vec p}$ and $b^{\mathrm{fop}}_{\vec p}$. The symmetric projection is the standard bosonic construction and is carried by the commutator, exactly as the companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* records. The scalar Fock space is standard and imported; the biquaternion framework contributes the central phase and the biquaternion-norm interpretation of the dispersion, and nothing algebraic.

The obstruction to anything more is worth stating precisely, because it distinguishes the scalar case from the Dirac case. The mode operators $a^{\mathrm{fop}}_{\vec p},{a^{\mathrm{fop}}_{\vec p}}^\dagger$ are **not** elements of $\mathbb{B}$. They are elements of the Weyl algebra of the one-particle space, which is infinite-dimensional, and no finite-dimensional algebra can contain them: if $[a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}]=c\,e_t$ held for $a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}\in\mathbb{B}$, the trace would give $0=\mathrm{Tr}([a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}])=c\,\mathrm{Tr}(e_t)=2c$, hence $c=0$. The companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* draws the consequence for the algebra: $\mathbb{B}\cong M_2(\mathbb{C})$ hosts exactly one **fermionic** mode and no bosonic mode at all. The scalar field, being bosonic, has no native one-mode core in $\mathbb{B}$; its ladder is a construction on an imported module. The contrast with the Dirac quantization is exact: there the algebra at least carried the one-mode anticommutator and the fermion-parity grading; here it carries neither the commutator nor any scalar analog of the grading.


## The Hamiltonian, Momentum and Charge

The Hamiltonian density is the time–time component of the canonical energy–momentum tensor, and in natural units

$$
H=\int d^3x\left(\left(\partial\phi^{\mathrm{fop}}/\partial t\right)^{\dagger} \partial\phi^{\mathrm{fop}}/\partial t+\nabla\phi^{\mathrm{fop}\dagger}\cdot\nabla\phi^{\mathrm{fop}}+\mu^2\phi^{\mathrm{fop}\dagger}\phi^{\mathrm{fop}}\right).
$$

Substituting the mode expansion and using the commutators gives, before normal ordering,

$$
H=\int\!\frac{d^3p}{(2\pi)^3}\,E_{\vec p}\left({a^{\mathrm{fop}}_{\vec p}}^\dagger a^{\mathrm{fop}}_{\vec p}+{b^{\mathrm{fop}}_{\vec p}}^\dagger b^{\mathrm{fop}}_{\vec p}\right)
+\underbrace{\int d^3x\int\!\frac{d^3p}{(2\pi)^3}E_{\vec p}}_{\text{c-number}} .
$$

The c-number is quartically divergent and proportional to the volume, $V\int\frac{d^3p}{(2\pi)^3}E_{\vec p}$: it is the zero-point energy of the two real fields that make up the complex one, each contributing $\tfrac12V\int\frac{d^3p}{(2\pi)^3}E_{\vec p}$, equivalently $(2\pi)^3\delta^{(3)}(0)\int\frac{d^3p}{(2\pi)^3}E_{\vec p}$ with $(2\pi)^3\delta^{(3)}(0)=V$. **Normal ordering** removes it and gives

$$
:\!H\!:\,=\int\!\frac{d^3p}{(2\pi)^3}\,E_{\vec p}\left({a^{\mathrm{fop}}_{\vec p}}^\dagger a^{\mathrm{fop}}_{\vec p}+{b^{\mathrm{fop}}_{\vec p}}^\dagger b^{\mathrm{fop}}_{\vec p}\right),
$$

a positive operator: particles and antiparticles both contribute energy $+E_{\vec p}$. The spatial momentum and the conserved charge are

$$
:\!P^{\mathrm{fop}}\!:\,=\int\!\frac{d^3p}{(2\pi)^3}\,\vec p\left({a^{\mathrm{fop}}_{\vec p}}^\dagger a^{\mathrm{fop}}_{\vec p}+{b^{\mathrm{fop}}_{\vec p}}^\dagger b^{\mathrm{fop}}_{\vec p}\right),
\qquad
Ϙ^{\mathrm{fop}}=\int\!\frac{d^3p}{(2\pi)^3}\left({a^{\mathrm{fop}}_{\vec p}}^\dagger a^{\mathrm{fop}}_{\vec p}-{b^{\mathrm{fop}}_{\vec p}}^\dagger b^{\mathrm{fop}}_{\vec p}\right),
$$

with $Ϙ^{\mathrm{fop}}$ the Noether charge of the parent's $\mathrm{U}(1)$ current $\tilde J\in\mathbb{M}_-$; particles and antiparticles carry opposite charge. The normal-ordered charge is the difference of two non-negative operators and is therefore unbounded above and below, as it must be for a conserved charge; the normal-ordered Hamiltonian, being their sum, is non-negative after the vacuum energy is removed.

The vacuum energy has the same status in this framework as in the parent quantizations. The c-number is a **central scalar**, a multiple of $e_t$, hence commutes with every element of the algebra and with every operator built from the field; as a constant it is unobservable, and its dependence on boundary conditions — the finite, observable part — is the subject of the companion article *The Vacuum State and the Casimir Effect in Biquaternionic Form*, which reaches it for the scalar and electromagnetic cases. The framework's contribution is to identify the vacuum energy as the trace part of the Hamiltonian, not to select a regularization of it.

## Microcausality and the Commutator Function

The commutator of two field operators is not an operator but a multiple of the identity. From the mode algebra,

$$
\big[\phi^{\mathrm{fop}}(x),\phi^{\mathrm{fop}\dagger}(y)\big]
=\int\!\frac{d^3p}{(2\pi)^3\,2E_{\vec p}}
\left(\exp(-ip\cdot(x-y))-\exp(+ip\cdot(x-y))\right)
\equiv i\Delta(x-y),
$$

a c-number, the **commutator function** (Pauli–Jordan function) times a central unit; the commutators $[\phi^{\mathrm{fop}},\phi^{\mathrm{fop}}]$ and $[\phi^{\mathrm{fop}\dagger},\phi^{\mathrm{fop}\dagger}]$ vanish identically. This c-number character is the precise sense in which a bosonic field is a **classical** field with operator coefficients: the non-commutativity of the field at two events is a fixed function, not a dynamical operator. For the Dirac field the corresponding object is an operator-valued matrix, and the difference is the difference between the bosonic and fermionic cases.

Two properties of $\Delta$ are the physical content. At equal times it vanishes,

$$
\big[\phi^{\mathrm{fop}}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t),\phi^{\mathrm{fop}\dagger}(\vec y,t)\big]=0,
$$

because the integrand of the momentum integral is odd under $\vec p\to-\vec p$; this is the statement that the field is a canonical coordinate and not its own momentum. For spacelike separation, $\langle\tilde{R}-\tilde R'\rangle_{\natural}>0$, it vanishes as well, which is **microcausality**: two measurements of the field in causally disconnected regions commute, and the quantization does not correlate them. For timelike separation it does not vanish, and the commutator is what enforces the canonical relation and the positivity of the energy. The standard result that $\Delta$ has support on the light cone and its interior is inherited from the standard theory; the framework's notation neither alters it nor needs to.

## What Is Standard and What Is Open

Because the question addressed here is the second-quantization question of the framework, we separate the two kinds of statement explicitly.

**Standard quantum field theory, transcribed.**

- The Lagrangian $\mathcal{L}=-(\partial/\partial Q_t\,\phi^*)(\partial/\partial Q_t\,\phi)-\sum_k(\partial/\partial Q_k\,\phi^*)(\partial/\partial Q_k\,\phi)-\mu^2\phi^*\phi$, the conjugate momentum $\pi=c^{-2}\left(\partial\phi/\partial t\right)^{\,*}$, and the regular Legendre transform.
- The equal-time commutators, imposed and verified, and the three reasons the bracket is a commutator rather than an anticommutator.
- The mode expansion in the parent's plane waves, the mode commutators, and the recovery of the equal-time relation.
- The symmetric Fock space, the occupation basis, the vacuum, and the number operator.
- The Hamiltonian, its normal-ordering constant, the four-momentum and the charge.
- The commutator function, its equal-time vanishing, and microcausality.

**Open in the biquaternion framework.**

- **The intrinsic operator field.** Whether the quantized scalar field should be treated as central-valued, as the algebra's centre requires, or whether a $\mathbb{B}$-valued field with a nontrivial transformation under the algebra is available, is not decided. The central-valued interpretation is the one adopted here because it is the one the classical field has.
- **The intrinsic Lagrangian and pairings.** The parent Dirac and Maxwell quantizations record that the $\mathbb{B}$-intrinsic Lagrangian and conjugate momentum are not fixed by the algebra alone. The same holds here, more simply: the central field's action is already a central scalar, but whether the trace pairing $\mathrm{Tr}$ rather than the scalar projection $\mathrm{Sc}$ is the natural pairing is a convention the algebra does not force.
- **The biquaternion Fock space.** Whether there is a Fock space native to $\mathbb{B}$, rather than the symmetric algebra of a module's solution space, is settled negatively for the algebra by the companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*; a construction native to some larger structure attached to $\mathbb{B}$ is not exhibited.
- **The bosonic gap.** No element pair in $\mathbb{B}$ realizes $[a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}]=e_t$. Whether the framework can be extended by an infinite-dimensional module that is canonically attached to $\mathbb{B}$ — rather than imported — is the structural question the scalar sector raises and cannot answer.
- **The vacuum energy.** Whether the algebra singles out a regularization of the quartically divergent zero-point constant, or assigns it a geometric meaning, is open, as in the parent quantizations and in the Casimir article.
- **Empirical content.** Whether any of this yields a prediction distinguishing the framework from standard scalar field theory is the unanswered framework-level question.

## Summary

The biquaternion Klein–Gordon field is quantized by promoting its central-valued representative to an operator-valued field. The classical theory has the action of the companion Noether article, conjugate momentum $\pi=c^{-2}\left(\partial\phi/\partial t\right)^{\,*}$, and a **regular** Legendre transform: unlike the Dirac case there is no second-class constraint, and unlike the Maxwell case there is no gauge redundancy. The equal-time relations are commutators,

$$
\big[\phi^{\mathrm{fop}}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t),\pi^{\mathrm{fop}}(\vec y,t)\big]
=\big[\phi^{\mathrm{fop}\dagger}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t),\pi^{\mathrm{fop}\dagger}(\vec y,t)\big]
=i\hbar\,\delta^{(3)}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-\vec y),
$$

with all other equal-time brackets vanishing; commutation rather than anticommutation is forced by the boundedness of the energy, by microcausality, and by positivity of the norm.

The field expands in the parent's plane waves,

$$
\phi^{\mathrm{fop}}(x)=\int\!\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_{\vec p}}}
\left(a^{\mathrm{fop}}_{\vec p}\exp(-ip\cdot x)+{b^{\mathrm{fop}}_{\vec p}}^\dagger \exp(+ip\cdot x)\right),
$$

the phases being central unitaries $\exp(\pm i\,\mathrm{Sc}(\tilde P\tilde R^{\natural})/\hbar)$ built from the material four-wavevector $\tilde P/\hbar=iE_{\vec p}e_t+\vec p$; the mode commutators are $[a^{\mathrm{fop}}_{\vec p},{a^{\mathrm{fop}}_{\vec k}}^\dagger]=[b^{\mathrm{fop}}_{\vec p},{b^{\mathrm{fop}}_{\vec k}}^\dagger]=(2\pi)^3\delta^{(3)}(\vec p-\vec k)$ and all others zero, and they reproduce the equal-time relation. The Fock space is the symmetric algebra of the one-particle space. The Hamiltonian is $:\!H\!:=\int\frac{d^3p}{(2\pi)^3}E_{\vec p}(a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}+b^{\mathrm{fop}\dagger}b^{\mathrm{fop}})$ after normal ordering, and the normal-ordered charge has particles and antiparticles of opposite sign.

The field's value space is the centre $\mathbb{C}_{\mathbb{B}}$, and the algebra supplies no ladder for it: no pair in $\mathbb{B}$ satisfies $[a^{\mathrm{fop}},a^{\mathrm{fop}\dagger}]=e_t$, since the trace of a commutator vanishes while $\mathrm{Tr}(e_t)=2$. The scalar mode algebra is thus the Weyl algebra of an imported module. The quantization is a transcription of standard canonical quantization into the framework's notation; its distinctive content is the central-valuedness of the field, the biquaternion-norm interpretation of the mass shell, and the explicit determination that this sector, alone among the three, receives nothing algebraic from $\mathbb{B}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^2=-e_t$, $\vec e_\mu \vec e_\nu=-\delta_{\mu\nu}e_t+\varepsilon_{\mu\nu\lambda}\vec e_\lambda$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_+,\mathbb{M}_-$ | Informational (Hermitian) and material (anti-Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_t,ie_t\}$ | Centre; the scalar field's value space |
| $\tilde{R}=ict\,e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$, $\langle\tilde{R}\rangle_{\natural}=\tilde{R}\tilde{R}^{\natural}$ | Material coordinate, $\in\mathbb{M}_-$, and its biquaternion norm; spacelike means $N>0$ |
| $\tilde{\nabla}=e_t\partial/\partial Q_t+\sum_\mu \vec e_\mu\,\partial/\partial Q_\mu$ | Biquaternionic gradient |
| $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}=\tilde{\nabla}^{\natural}\tilde{\nabla}=\partial^2/\partial Q_t^2+\Delta$ | d'Alembertian |
| $\tilde{\Phi}=\phi\,e_t$, $\phi=(\phi_1+i\phi_2)/\sqrt2$ | Scalar field, valued in the centre; real components |
| $\mathcal{L}=-\,\mathrm{Sc}[(\tilde{\nabla}^{\natural}\tilde{\Phi}^{*})(\tilde{\nabla}\tilde{\Phi})]-\mu^2\mathrm{Sc}[\tilde{\Phi}^{*}\tilde{\Phi}]$ | Scalar Lagrangian density |
| $\mu=mc/\hbar$ | Mass parameter |
| $\pi=c^{-2}\left(\partial\phi/\partial t\right)^{\,*}$, $\pi^\dagger=c^{-2}\partial\phi/\partial t$ | Conjugate momenta; Legendre transform regular |
| $\tilde P/\hbar=i\omega/c\,e_t+\vec k$, $\langle\tilde P/\hbar\rangle_{\natural}=\tilde P\tilde P^{\natural}/\hbar^{2}$ | Material four-wavevector and biquaternion norm |
| $\langle\tilde P/\hbar\rangle_{\natural}=-m^2c^2/\hbar^2\,e_t$ | Mass-shell condition |
| $E_{\vec p}=\sqrt{\vec p^2+\mu^2}$, $p\cdot x=E_{\vec p}t-\vec p\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$ | On-shell energy and phase (natural units) |
| $a^{\mathrm{fop}}_{\vec p},b^{\mathrm{fop}}_{\vec p}$ | Particle and antiparticle annihilation operators |
| $[a^{\mathrm{fop}}_{\vec p},{a^{\mathrm{fop}}_{\vec k}}^\dagger]=(2\pi)^3\delta^{(3)}(\vec p-\vec k)$ | Mode commutators |
| $\mathcal{F}=\bigoplus_n(\mathcal{H}_1^{\otimes n})_+$ | Bosonic Fock space (symmetric algebra) |
| $:\!H\!:=\int\frac{d^3p}{(2\pi)^3}E_{\vec p}(a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}+b^{\mathrm{fop}\dagger}b^{\mathrm{fop}})$ | Normal-ordered Hamiltonian |
| $Ϙ^{\mathrm{fop}}=\int\frac{d^3p}{(2\pi)^3}(a^{\mathrm{fop}\dagger}a^{\mathrm{fop}}-b^{\mathrm{fop}\dagger}b^{\mathrm{fop}})$ | Conserved charge |
| $i\Delta(x-y)=[\phi^{\mathrm{fop}}(x),\phi^{\mathrm{fop}\dagger}(y)]$ | Commutator (Pauli–Jordan) function |
| $\mathrm{Tr}(e_t)=2$, $\mathrm{Tr}([\tilde Q_2,\tilde Q_1])=0$ | Trace identity; no bosonic mode in $\mathbb{B}$ |
| $\eta=\mathrm{diag}(-1,+1,+1,+1)$ | $ict$-coordinate metric (level 2) |

## Further Reading

- O. Klein, "Quantentheorie und fünfdimensionale Relativitätstheorie," *Zeitschrift für Physik* **37** (1926) 895–906, and W. Gordon, "Der Comptoneffekt nach der Schrödingerschen Theorie," *Zeitschrift für Physik* **40** (1926) 117–133, for the original scalar wave equation.
- W. Pauli and V. F. Weisskopf, "Über die Quantisierung der skalaren relativistischen Wellengleichung," *Helvetica Physica Acta* **7** (1934) 709–731, for the quantization of the scalar field by commutators and the interpretation of the antiparticle branch.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the canonical quantization of the scalar field, the mode expansion, and the commutator function.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the equal-time relations, the normal-ordering constant, and the Pauli–Jordan function.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the complex scalar field, its mode expansion, and its conserved charge.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the general construction of the Fock space and the connection between spin and statistics.
- P. A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for the classification of constraints that distinguishes the scalar, Dirac and Maxwell Legendre transforms.
- R. Haag, *Local Quantum Physics: Fields, Particles, Algebras* (Springer, 1996), for the algebraic formulation in which the field is an operator-valued distribution and the commutator function is the causal structure.
