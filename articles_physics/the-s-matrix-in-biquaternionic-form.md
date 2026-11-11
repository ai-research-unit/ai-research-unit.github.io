# __The S-Matrix in Biquaternionic Form__

## Introduction

The **S-matrix** is the operator that carries the state of a scattering experiment from the remote past to the remote future. In the interaction picture it is the time-ordered exponential of the interaction Hamiltonian,

$$
S \;=\; T\exp\!\left(-i\int d^4r\;\mathcal{H}_I(x)\right),
$$

and the transition probability is the squared matrix element of $S$ between the initial state and the final state. Its defining property is **unitarity**, $S^{\dagger} S = 1$. It is the object in which the dynamics of an interacting field theory is summarized. Throughout, $i$ is the central scalar imaginary of the algebra, with $i^2=-1$; $\hbar$ and $c$ are written explicitly wherever a momentum or an energy appears.

The companion articles have assembled every ingredient this article needs. *The Dirac Equation in Biquaternionic Form* fixes the one-sided pair $\tilde{Ξ}_{\mathrm{sp},L},\tilde{Ξ}_{\mathrm{sp},R}$ that the quantized field satisfies and keeps it apart from Kravchenko's two-sided equation. *Canonical Quantization of the Biquaternion Dirac Field* promotes the biquaternion Dirac field to an operator-valued field, builds the mode algebra, and produces a Fock space, recording that the construction transcribes standard canonical quantization rather than deriving it from the algebra $\mathbb{B}$. *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* sharpens that result: the Fock space is a **module** over $\mathbb{B}$, not an object of it, and the algebra hosts exactly one fermionic mode. *The Feynman Propagator in Biquaternionic Form* supplies the two-point function and the finding that the algebra provides the complex plane and the axis of the $i\epsilon$ but not the orientation that selects the Feynman contour.

This article asks what "the S-matrix in biquaternionic form" names. The finding is stated at the outset.

- **Established, and recomputed below.** Conditional on the one-mode identification of the Fock article, the S-matrix of a single fermionic mode is a **star-unitary** element of $\mathbb{B}$: $\tilde{\mathcal S}_{\Psi}\tilde{\mathcal S}_{\Psi}^{*} = e_t$. That condition is not the unit-norm condition $\langle\tilde{\mathcal S}_{\Psi}\rangle_{\natural}=1$ that the framework uses for its Lorentz rotors. The two define different groups, $\mathrm{U}(2)$ and $\mathrm{SL}(2,\mathbb{C})$, and they intersect in the spin rotations $\mathrm{SU}(2)$; the S-matrix belongs to the first, and not in general to the second. A fermion-parity-conserving one-mode S-matrix is $\tilde{\mathcal S}_{\Psi} = \exp(i\theta_0)\tilde\Pi_+ + \exp(i\theta_1)\tilde\Pi_-$, whose quaternionic norm is the scalar phase $\exp(i(\theta_0+\theta_1))$, generally not $1$. Its transition probabilities are given by the element formula $2\,\mathrm{Sc}(\tilde\Pi_f\,\tilde{\mathcal S}_{\Psi}\tilde{Ϛ}_{\Psi,i}\,\tilde{\mathcal S}_{\Psi}^{*})$.
- **Standard, and transcribed.** The interaction picture, the Dyson series, the unitarity relation $S = 1+iT$, the finite-dimensional identity $2\,\mathrm{Im}\,T = T^\dagger T$, the optical theorem, and the contraction of the Dyson series into Feynman propagators by Wick's theorem. None of this depends on the biquaternion structure beyond the kinematical conventions already fixed by the read-list articles.
- **Gap, left visible.** The S-matrix of the *field* is an operator on an infinite-dimensional Fock space and is **not** an element of $\mathbb{B}$; the algebra hosts at most the one-mode truncation. And the algebra does not select the boundary condition — the $i\epsilon$ orientation, equivalently the in/out splitting — that makes the time-ordered exponential a well-defined distributional object. That gap is inherited from the propagator article and is not closed here.

The article is organized as follows. The next section fixes the interaction-picture definition and the Dyson series. The section after that separates the two conditions that carry the name of unitarity inside $\mathbb{B}$, which is where a sign or a group can silently go wrong. The following section constructs the one-mode S-matrix and states exactly how far the algebra reaches. The next section records the transition probability and the Born rule. A section derives and checks the unitarity relation, whose diagonal is the optical theorem. A section follows the Dyson series into the propagator, writes the contraction that builds it, and locates the boundary-condition gap. A section separates what the algebra supplies from what it only transcribes. A section reads the S-matrix on the polar word. The article closes with open questions, a summary, the notation, and the further reading.

## The S-Matrix in the Interaction Picture

Split the Hamiltonian into a free part and an interaction, $H = H_0 + H_I$, and write the fields in the interaction picture, where they evolve with $H_0$ and the state evolves with $H_I$. The evolution operator is

$$
U_I(r'_t,r'_{t,1}) \;=\; T\exp\!\left(-i\int_{r'_{t,1}}^{r'_{t}}dr'_{t,2}\,H_I(r'_{t,2})\right),
$$

with $T$ the time-ordering operator, and the S-matrix is the limit

$$
S \;=\; U_I(+\infty,-\infty).
$$

Expanding the exponential gives the **Dyson series**,

$$
S \;=\; \sum_{n=0}^{\infty}\frac{1}{n!}\left(-i\right)^{n}
\int d^4r_1\cdots d^4r_n\; T\big\{\mathcal{H}_I(x_1)\cdots\mathcal{H}_I(x_n)\big\},
$$

the $n=0$ term being the identity. Since $H_I$ is Hermitian, the evolution operator obeys $i\,\partial/\partial r'_t\, U_I(r'_t,r'_{t,1}) = H_I(r'_t)U_I(r'_t,r'_{t,1})$ with $U_I(r'_{t,1},r'_{t,1}) = 1$, which gives $U_I^\dagger U_I = 1$; hence the S-matrix is unitary, $S^{\dagger}S = 1$. The adjoint is written $\dagger$ on operators and $*$ on elements of $\mathbb{B}$, so that the two cannot be confused. For an element of $\mathbb{B}$ the condition is $\tilde{\mathcal S}_{\Psi}^{*}\tilde{\mathcal S}_{\Psi} = e_t$, equivalent to $\tilde{\mathcal S}_{\Psi}\tilde{\mathcal S}_{\Psi}^{*} = e_t$, because either order makes $\tilde{\mathcal S}_{\Psi}^{*}$ the inverse of $\tilde{\mathcal S}_{\Psi}$; the two orders are used interchangeably below. (Individual truncations of the Dyson series are not unitary; it is the summed operator that is.)

Three features of this construction are worth naming, because they are the points at which the biquaternion structure enters.

**The time ordering is fermionic.** The fields in $\mathcal{H}_I$ are the biquaternion Dirac field on the module it acts on, and their time-ordered products carry the anticommutation sign. This is the same sign that the propagator article traced, and it is not an extra convention: it is the statement that the field operators anticommute, inherited from the canonical quantization article.

**The $i$ in the exponent is the algebra's scalar imaginary.** The factor $-i$ is built from the same central element $i$, with $i^2=-1$, that makes the material time coordinate $i r'_t$ and that appears in the deformed mass shell $\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural}+m^{2}\,c^{4}-i\epsilon$. The algebra names this element; it does not choose its sign in the exponent, which is fixed by the convention that $S$ be unitary and that forward time evolution be generated by $\exp(-iHr'_t)$.

**The interaction is written in biquaternion notation.** The interaction Hamiltonian is built from the biquaternion fields and their conjugates; its specific form — for electromagnetism, the minimal coupling of the Dirac current to the potential — is the gauge-principle article's subject and is not rederived here. Nothing below depends on which interaction is chosen; the structural statements are about the S-matrix as a unitary operator, not about a particular vertex.

The S-matrix is usually separated into the forward part and the transition part,

$$
S \;=\; 1 + iT,
$$

with $T$ the transition operator. Unitarity then reads

$$
(1-iT^\dagger)(1+iT) = 1
\;\;\Longleftrightarrow\;\;
i(T-T^\dagger) + T^\dagger T = 0,
$$

and that equation rearranges to

$$
T-T^\dagger = i\,T^\dagger T
\;\;\Longleftrightarrow\;\;
2\,\mathrm{Im}\,T = T^\dagger T,
$$

where $\mathrm{Im}\,T := (T-T^\dagger)/(2i)$. This is the exact unitarity relation; its diagonal matrix elements are the optical theorem, and it is derived and checked in the one-mode case below.

## Two Notions of Unitarity in the Algebra

Two conditions carry the name of unitarity inside $\mathbb{B}$, and the S-matrix forces the choice between them. The framework's Lorentz rotors are the elements of unit **quaternionic norm**; the unitarity of an element acting on a module is the **star condition**. The two are not the same condition. *Norm and Pairing Conventions* fixes both, with their level sets:

| Condition | Element form | Group | Real dimension |
|---|---|---|---|
| Unit quaternionic norm | $\langle\tilde U\rangle_{\natural}=1$ | $\mathrm{SL}(2,\mathbb{C})$ | 6 (non-compact) |
| Star-unitary | $\tilde{\mathcal S}_{\Psi}\tilde{\mathcal S}_{\Psi}^{*}=e_t$ | $\mathrm{U}(2)$ | 4 (compact) |

**Neither condition implies the other.** The convention states the two examples that separate them: a boost is of unit norm and not star-unitary, and a central phase is star-unitary and not of unit norm. Their intersection is the set of real unit quaternions, the spin rotations $\mathrm{SU}(2)$. A reader who carries the word "unitarity" from one condition to the other changes a group and a dimension count without changing a single symbol.

**Which condition the S-matrix satisfies is not a convention.** The S-matrix acts on the module, and the form it preserves there is the Hermitian one. Its condition is therefore the star condition,

$$
\boxed{\;\tilde{\mathcal S}_{\Psi}\tilde{\mathcal S}_{\Psi}^{*} = e_t\;}.
$$

The left side is Hermitian, and the Hermitian subspace $\mathbb{B}_{\Psi}$ is four-real-dimensional; the condition is therefore four real equations on the eight real parameters of $\tilde{\mathcal S}_{\Psi}$. The unit-norm condition is one complex equation on the same eight parameters, that is two real conditions.

**The difference bites on this article's object.** The one-mode S-matrix constructed in the next section is star-unitary, and its quaternionic norm is a phase which is generally not $1$. Reading "unitarity" as unit norm therefore places the S-matrix in the wrong group. That is the whole content of the section, and it is the reason the two names are kept apart everywhere below.

## The One-Mode S-Matrix

The algebra can host an S-matrix only where the Fock article's one-mode identification applies. The field S-matrix is an operator on the exterior algebra of the solution space of the field equation, an infinite-dimensional object; the algebra $\mathbb{B}$ is four-dimensional over $\mathbb{C}$ and cannot contain it. For a single fermionic mode, however, the Fock space is the two-dimensional **fundamental module** of $\mathbb{B}$, on which $\mathbb{B}$ acts as the whole operator algebra, and an S-matrix on that module is an element of $\mathbb{B}$. It is the one case where the S-matrix is a biquaternion.

**Conditional statement.** *If* a single mode of the Dirac field is isolated and its scattering is described on the two-dimensional module, *then* the one-mode S-matrix is a star-unitary element of $\mathbb{B}$,

$$
\tilde{\mathcal S}_{\Psi}\tilde{\mathcal S}_{\Psi}^{*} = e_t, \qquad \tilde{\mathcal S}_{\Psi} \in \mathbb{B}.
$$

The operator on the module is the action $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{\mathcal S}_{\Psi}\tilde{Ξ}_{\mathrm{sp}}$, read from the left. The conditionality is the Fock article's: whether the one-mode identification is a structural feature of the framework or a coincidence of the dimension count is not decided there, and this article does not decide it either. The S-matrix is not a derivation from the algebra; it is the algebra's one-mode truncation of a standard operator.

**The physical one-mode S-matrix is diagonal in the parity states.** The one-mode S-matrix is taken to conserve fermion parity: a scattering process does not turn an even state into an odd one. The parity element of the mode is $(-1)^F = i\vec u_{\mathrm p}$, with the axis $\vec u_{\mathrm p}=\vec e_z$ supplied by the physics and declared here; it squares to $e_t$. Fermion-parity conservation is the statement that $\tilde{\mathcal S}_{\Psi}$ commutes with $i\vec u_{\mathrm p}$. The elements of $\mathbb{B}$ that commute with $i\vec u_{\mathrm p}$ are exactly the complex span of $e_t$ and $i\vec u_{\mathrm p}$, and that span is also the span of the two pure states

$$
\tilde\Pi_\pm(\vec u_{\mathrm p}) = \tfrac12\left(e_t \pm i\vec u_{\mathrm p}\right),
$$

the vacuum and the occupied state. The two are idempotent, $\tilde\Pi_\pm^2=\tilde\Pi_\pm$, orthogonal, $\tilde\Pi_+\tilde\Pi_-=0$, complete, $\tilde\Pi_++\tilde\Pi_-=e_t$, and each is its own star, $\tilde\Pi_\pm^{*}=\tilde\Pi_\pm$.

A fermion-parity-conserving S-matrix therefore reads $\tilde{\mathcal S}_{\Psi}=a\tilde\Pi_+ + b\tilde\Pi_-$ with $a,b$ complex, and the star condition forces $|a|=|b|=1$, because the cross terms vanish and the two remaining equations are independent. Writing $a=\exp(i\theta_0)$ and $b=\exp(i\theta_1)$,

$$
\boxed{\;\tilde{\mathcal S}_{\Psi} = \exp(i\theta_0)\,\tilde\Pi_+(\vec u_{\mathrm p}) + \exp(i\theta_1)\,\tilde\Pi_-(\vec u_{\mathrm p})\;}.
$$

This is the one-mode S-matrix in its physical form: a phase on the vacuum and a phase on the occupied mode, which is what "no particle creation or annihilation in the asymptotic region" means at this level.

**Its quaternionic norm is a phase, not one.** The quaternionic conjugate of each state is the other, $\tilde\Pi_\pm^{\natural}=\tilde\Pi_\mp$, so

$$
\tilde{\mathcal S}_{\Psi}\tilde{\mathcal S}_{\Psi}^{\natural} = \exp(i(\theta_0+\theta_1))(\tilde\Pi_+ + \tilde\Pi_-) = \exp(i(\theta_0+\theta_1))\,e_t .
$$

The fermion-parity-conserving one-mode S-matrix is of unit norm only when $\theta_0+\theta_1 \in 2\pi\mathbb{Z}$. This is the concrete form of the preceding section's warning: a physical, star-unitary S-matrix is generally not a Lorentz rotor, and one should not assign it to the rotor group on the strength of the word "unitarity". On 100 random parameter pairs the star condition held, the commutation with $i\vec u_{\mathrm p}$ held, and the norm matched $\exp(i(\theta_0+\theta_1))$ to machine precision; none of the 100 pairs had $\langle\tilde{\mathcal S}_{\Psi}\rangle_{\natural}=1$.

**The S-matrix generated by a biquaternion Hamiltonian.** The finite-dimensional S-matrix also has a generator form. If the one-mode dynamics over an interval of duration $\tau$ is generated by a Hermitian element $\tilde H_\Psi \in \mathbb{B}_{\Psi}$, then

$$
\tilde{\mathcal S}_{\Psi} = \exp(-i\tilde H_\Psi\tau),
$$

and $\tilde H_\Psi^{*} = \tilde H_\Psi$ with $i$ central gives $\tilde{\mathcal S}_{\Psi}^{*} = \exp(+i\tilde H_\Psi\tau) = \tilde{\mathcal S}_{\Psi}^{-1}$, so $\tilde{\mathcal S}_{\Psi}$ is star-unitary, as it must be. What the quaternionic norm computes here is instructive. Write $\tilde H_\Psi = r_t e_t + \tilde V_{\Phi,\mathrm{pu}}$, with $r_t=\mathrm{Sc}(\tilde H_\Psi)$ real and $\tilde V_{\Phi,\mathrm{pu}}$ the pure part; the Hermiticity of $\tilde H_\Psi$ makes $\tilde V_{\Phi,\mathrm{pu}}$ equal to $i\vec r_\Psi$ with $\vec r_\Psi$ real, so $-i\tau\tilde H_\Psi = -i\tau r_t\,e_t+\tau\vec r_\Psi$, and the two terms commute. Hence

$$
\tilde{\mathcal S}_{\Psi} = \exp(-i\tau r_t)\,\tilde V_{\Phi,\mathrm{pu},\tau}, \qquad \tilde V_{\Phi,\mathrm{pu},\tau} = \exp(\tau\vec r_\Psi).
$$

The second factor is inverted by its own quaternionic conjugate, because $\natural$ negates $\vec r_\Psi$, so $\tilde V_{\Phi,\mathrm{pu},\tau}\tilde V_{\Phi,\mathrm{pu},\tau}^{\natural}=e_t$ and its quaternionic norm is $1$. The first factor is central, with norm $\exp(-2i\tau r_t)$. The quaternionic norm is multiplicative, so

$$
\langle\tilde{\mathcal S}_{\Psi}\rangle_{\natural} = \exp\!\left(-2i\tau\,\mathrm{Sc}(\tilde H_\Psi)\right).
$$

So the quaternionic norm of the one-mode S-matrix is the exponential of the scalar part of its generator. It equals $1$ whenever the generator has no scalar part, $\mathrm{Sc}(\tilde H_\Psi) = 0$. For a generic duration $\tau$ this is the only way it returns to $1$; at the special durations with $2\tau\,\mathrm{Sc}(\tilde H_\Psi)\in 2\pi\mathbb{Z}$ it returns to $1$ with a nonzero scalar part as well — $\tilde H_\Psi=\pi e_t$ at $\tau=1$ gives $\tilde{\mathcal S}_{\Psi}=-e_t$, which is star-unitary with $\langle\tilde{\mathcal S}_{\Psi}\rangle_{\natural}=1$. This was verified numerically for Hermitian generators with and without a scalar part: for $\mathrm{Sc}(\tilde H_\Psi)=0$ the quaternionic norm was $1$ to $10^{-15}$; for $\mathrm{Sc}(\tilde H_\Psi)=0.8$ it matched $\exp(-2i\tau\,\mathrm{Sc}(\tilde H_\Psi))$ at both $\tau = 0.6$ and $\tau = 1.7$; and the star condition held in every case. The quaternionic norm is thus not a unitarity condition at all: it measures the scalar part of the generator, and unitarity is blind to it.

### The Cartan Factor of the S-Matrix

Every element off the zero-divisor cone has the Cartan pairing $\tilde{\mathcal S}_{\Psi}=\tilde A_{\Phi}\tilde Q_0$, with $\tilde A_{\Phi}=\sqrt{\tilde{\mathcal S}_{\Psi}\tilde{\mathcal S}_{\Psi}^{*}}$ Hermitian positive and $\tilde Q_0=\tilde A_{\Phi}^{-1}\tilde{\mathcal S}_{\Psi}$ star-unitary; where $\tilde A_{\Phi}$ is not invertible, $\tilde Q_0$ is the partial isometry of the generalized pairing (*The Polar Decomposition and Its Three Pairings*; *The Polar Decomposition of an N-Degenerate Biquaternion*). Here $\tilde A_{\Phi}$ is the Cartan amplitude, written $\tilde Q_H$ in the pairing article; the letter is changed because $\tilde Q$ is the generic element in the polar word and $\tilde H_\Psi$ is the generator. For the one-mode S-matrix, the star condition is exactly the statement that the amplitude is trivial:

$$
\tilde{\mathcal S}_{\Psi}\tilde{\mathcal S}_{\Psi}^{*}=e_t
\qquad\Longrightarrow\qquad
\tilde A_{\Phi}=e_t,\qquad \tilde Q_0=\tilde{\mathcal S}_{\Psi} .
$$

A star-unitary $\tilde{\mathcal S}_{\Psi}$ carries only phase: its Cartan amplitude is the identity. This is the scattering form of the statement that unitarity is the triviality of the Hermitian factor: the S-matrix's polar word has scale one and no boost, and its content is the central phase and the spin rotation.

The non-trivial case is a truncation, not the full S-matrix. If probability leaves the one-mode sector — a channel to unobserved modes, or an open-system effective S-matrix — the element can be $\tilde{\mathcal S}_{\Psi}=\tilde\Pi_+ + a\tilde\Pi_-$ with $0<a<1$ (or $a>1$ for gain). Then $\tilde A_{\Phi}=\tilde\Pi_+ + a\tilde\Pi_-$ and $\tilde Q_0=e_t$; the two values of $\tilde A_{\Phi}$ are the absorption factors, and $1-a^{2}$ is the probability lost (negative for gain). The same amplitude-versus-phase split appears for a resonance pole, where the Cartan amplitude of the pole term is $\exp(-\frac{\Gamma\,t}{2\,\hbar})$ (see *The Unstable State and the Complex Energy Pole in Biquaternionic Form*, §*The Complex Angle of the Resonance*). At $a=0$ the amplitude is not invertible, the second factor is the partial isometry $\tilde\Pi_+$, and the generalized pairing is the one that applies. The article's S-matrix is star-unitary by construction, so its Cartan factor is $e_t$; the non-star-unitary reading belongs to the truncation and is not claimed for the field S-matrix.

**Then the algebra stops.** A second mode already needs the operators on a module of complex dimension four, a complex space of dimension sixteen, which does not embed in the four-dimensional $\mathbb{B}$ over $\mathbb{C}$; this is the Fock article's capacity count, and the S-matrix inherits it. Consequently the S-matrix of a spin flip between two modes, or of any genuinely multi-mode process, is not an element of $\mathbb{B}$ on any interpretation. The finite-dimensional S-matrix is not a truncation of the field S-matrix to a subalgebra; it is the field S-matrix's action on the single module the algebra happens to carry.

## The S-Matrix Element and the Born Rule

The S-matrix element is read off the algebra of the informational sector. For an initial state described by a positive element $\tilde{Ϛ}_{\Psi,i} \in \mathbb{B}_{\Psi}$ normalised by $\langle\tilde{Ϛ}_{\Psi,i},e_t\rangle_{*}=\tfrac12$ and a final measurement whose outcome is the pure state $\tilde\Pi_f \in \mathbb{B}_{\Psi}$, the transition probability is

$$
\boxed{\;P_{i\to f} \;=\; 2\,\mathrm{Sc}\!\left(\tilde\Pi_f\,\tilde{\mathcal S}_{\Psi}\,\tilde{Ϛ}_{\Psi,i}\,\tilde{\mathcal S}_{\Psi}^{*}\right)\;},
$$

which is the Born rule of the informational-sector article applied to the scattering channel $\tilde{Ϛ}_{\Psi,i} \mapsto \tilde{\mathcal S}_{\Psi}\tilde{Ϛ}_{\Psi,i}\tilde{\mathcal S}_{\Psi}^{*}$. The S-matrix acts as a **reversible** channel: it is star-unitary, in contrast with the pure states that implement measurement, which are not. The reversible/irreversible dichotomy of $\mathbb{B}_{\Psi}$ is thus visible in the scattering formalism, with the S-matrix on the reversible side.

The formula was checked against the elementary Born rule on cases chosen for the purpose rather than for convenience. Take the two occupation states, $\tilde\Pi_+(\vec u_{\mathrm p})$ for the vacuum and $\tilde\Pi_-(\vec u_{\mathrm p})$ for the occupied state, and take for $\tilde{\mathcal S}_{\Psi}$ a rotation of the abstract two-state space about $\vec e_y$,

$$
\tilde{\mathcal S}_{\Psi} = \cos\frac{\theta}{2}\,e_t + \sin\frac{\theta}{2}\,\vec e_y .
$$

This rotation does **not** conserve fermion parity — it is the Bloch rotation, which in the one-mode truncation is also the spin rotation, and it mixes the two occupation levels. It is chosen to exercise the off-diagonal Born weight; the physical one-mode S-matrix of the preceding section is diagonal, and its Born weights are $0$ and $1$. For $\theta = 0.77$ the two routes give

$$
2\,\mathrm{Sc}\!\left(\tilde\Pi_+\,(\tilde{\mathcal S}_{\Psi}\,\tilde\Pi_-\,\tilde{\mathcal S}_{\Psi}^{*})\right)
= \sin^2\!\frac{\theta}{2} = \tfrac12\left(1-\cos\theta\right) = 0.141044665\ldots,
$$

agreeing to machine precision. The second route is the geometry of the informational sector: the state carries the vector $\vec r=-\vec u_{\mathrm p}$ on the Bloch ball, the rotation carries it to $\vec r\cdot\vec u_{\mathrm p}=-\cos\theta$, and the weight of a state of vector $\vec r$ in the pure state of axis $\vec u_{\mathrm p}$ is $\tfrac12(1+\vec r\cdot\vec u_{\mathrm p})$. A mixed initial state $\tilde{Ϛ}_{\Psi,i} = \tfrac12(e_t + 0.4\,i\vec u_{\mathrm p})$, which is positive and normalised, gave $2\,\mathrm{Sc}(\tilde\Pi_+\tilde{\mathcal S}_{\Psi}\tilde{Ϛ}_{\Psi,i}\tilde{\mathcal S}_{\Psi}^{*}) = 0.643582134\ldots$, matching $\tfrac12(1+0.4\cos\theta)$ on the same route. The element formula is the operational content of the one-mode S-matrix: it turns the biquaternion $\tilde{\mathcal S}_{\Psi}$ into numbers.

Nothing in this section is specific to a scattering process. The normalised Hermitian form is the Born rule, read here on the scattering channel, and it would apply to any star-unitary element acting on the one-mode state space; the S-matrix is one such element. That generality is the honest interpretation: the algebra supplies the state space, the operator, and the pairing, and the *interpretation* of the pairing as a scattering cross-section requires the field-theoretic measure that the algebra does not contain.

## Unitarity, the Optical Theorem, and the Algebra

The unitarity relation of the interaction picture is an algebraic identity in the one-mode truncation, and it is worth deriving it there because it is where the S-matrix's unitarity is actually used.

With $\tilde{\mathcal S}_{\Psi} = e_t + i\tilde T$, the condition $\tilde{\mathcal S}_{\Psi}^{*}\tilde{\mathcal S}_{\Psi} = e_t$ gives, in the algebra,

$$
(e_t-i\tilde T^{*})(e_t+i\tilde T)
= e_t + i(\tilde T-\tilde T^{*}) + \tilde T^{*}\tilde T
= e_t,
$$

where the last term uses $(-i\tilde T^{*})(i\tilde T)=-i^2\tilde T^{*}\tilde T=+\tilde T^{*}\tilde T$ and $i^2=-1$. Hence

$$
i(\tilde T-\tilde T^{*}) + \tilde T^{*}\tilde T = 0
\;\;\Longleftrightarrow\;\;
2\,\mathrm{Im}\,\tilde T = \tilde T^{*} \tilde T,
$$

with $\mathrm{Im}\,\tilde T := \tfrac{1}{2i}(\tilde T-\tilde T^{*}) \in \mathbb{B}_{\Psi}$. (Using $\tilde{\mathcal S}_{\Psi}\tilde{\mathcal S}_{\Psi}^{*} = e_t$ instead gives $2\,\mathrm{Im}\,\tilde T = \tilde T\tilde T^{*}$, which agrees because $\tilde T$ built from a star-unitary $\tilde{\mathcal S}_{\Psi}$ is normal.) This is the same relation as the operator identity $2\,\mathrm{Im}\,T = T^\dagger T$ written for the one-mode truncation, and it is an exact biquaternion identity: it says that the Hermitian part $2\,\mathrm{Im}\,\tilde T$ equals the positive element $\tilde T^{*}\tilde T$.

The identity was checked on elements not used to state it. For four independently generated star-unitary elements $\tilde{\mathcal S}_{\Psi}$ with random central phase and random spin axis, $\tilde T = (\tilde{\mathcal S}_{\Psi}-e_t)/i$ was formed and the difference $2\,\mathrm{Im}\,\tilde T - \tilde T^{*}\tilde T$ was computed in the algebra; its largest component was of order $10^{-16}$, so the identity holds to machine precision.

The physical content is the **optical theorem**: the diagonal element of $2\,\mathrm{Im}\,T$ in an initial state equals the squared norm of $T$ applied to that state, which is the summed transition probability out of it. That element is positive, so it is the total rate. In a field theory with a continuum of final states the relation becomes the standard one between the forward scattering amplitude and the total cross-section. The optical theorem is the statement that the operator $S$ is unitary; the algebra does not weaken or strengthen it, and in the one-mode truncation it is the exact identity above.

One should not oversell what was checked. The identity $2\,\mathrm{Im}\,T = T^\dagger T$ is a consequence of unitarity alone; it is true for any unitary operator and hence for any star-unitary element, and the numerical check confirms that the algebra implements it correctly rather than testing a biquaternion-specific claim. The genuinely biquaternion statements are the two of the preceding sections: that the star condition is the right condition and not the unit-norm condition, and that the one-mode truncation is the whole of the algebra's reach.

## The Dyson Series, the Propagator, and the Contour

The Dyson series is evaluated by **Wick's theorem**: the time-ordered product of field operators is the sum over all contractions, and each contraction is a two-point function. The contractions are exactly the objects of the propagator article: the positive- and negative-frequency pieces $W_\pm$, and their time-ordered combination $S_F$ with its Feynman contour. The biquaternion content of the S-matrix is therefore inherited from the propagator's, not independent of it.

Three inheritances should be named.

**The fermionic sign.** The relative minus in the time ordering is the anticommutator of the field, and it propagates into a minus sign on every closed fermion loop of a Feynman diagram. The propagator article shows that this sign is not carried by the contour; it is carried by the numerator of the propagator. It is not an extra convention: it is the statement that the field operators anticommute, inherited from the canonical quantization article.

**The $i\epsilon$.** The time-ordered exponential requires the interaction to be switched on and off adiabatically in the remote past and future, which is a deformation of the integration contour by the same $i\epsilon$ that makes $S_F$ a distribution. The propagator article's finding applies verbatim: the algebra provides the complex plane and locates the deformation along the $i r'_t$ axis of $\mathbb{B}_{\Phi}$, but the *orientation* — Feynman versus anti-Feynman, and the in/out splitting itself — is a boundary condition that the algebra does not select.

**The asymptotic states.** In and out states are plane-wave states from the solutions article, labeled by on-shell momenta. Two equations carry the name *Dirac equation*, and the external states belong to only one of them. They are solutions of the corpus's **one-sided** pair

$$
\tilde\nabla_\Phi\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L},
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R},
$$

both gradients acting from the left, with the mass carried as the off-diagonal pairing of the two halves. Kravchenko's **two-sided** equation — the spatial gradient acting from the left and the mass from the right through $\vec e_z$, with the componentwise conjugation in the mass term — is a different operator. It is related to the pair by the dictionary of *The Dirac Equation in Biquaternionic Form*, but it is not the equation whose solutions are quantized here, and its mass term is of a different kind. The on-shell condition is the biquaternion mass shell $\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}= -m^{2}\,c^{2}$. The reduction of the S-matrix element to an amputated correlation function — the LSZ formula — replaces each external leg by the corresponding plane wave and applies the wave operator. The biquaternion form of that reduction is the placement of the external legs on the mass shell and is not rederived here; what matters is that the external data are the solutions article's biquaternion plane waves, and the internal data are the propagator, so the whole Dyson series is written in the read-list notation without a new ingredient. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

The gap is therefore the propagator's gap, seen from the S-matrix side: the algebra can *write* the time-ordered exponential and can name the $i\epsilon$, but it cannot *choose* the contour, and the choice is what makes the exponential well-defined as a distribution. This article inherits that gap and records it rather than closing it.

## The Contraction that Builds a Propagator

The numerator of the propagator is an operator on the module, and it is not a single multiplier. Acting on an element it is

$$
\tilde Q \;\longmapsto\; i\,\tilde Q\,\vec e_x\,E
-i\left(\vec e_x\tilde Q\vec e_y\,p_x+\vec e_y\tilde Q\vec e_y\,p_y+\vec e_z\tilde Q\vec e_y\,p_z\right),
$$

with one term per component of the momentum, each of the form $\tilde Q\mapsto a\tilde Qb$ with two multipliers. This is why the framework writes the contraction with two-sided multipliers, the basis operators of *Operators Acting on Two Sides*: a single multiplier would keep the operator inside the four-dimensional algebra, and the four components need the pair. The arrays the framework prints for the propagation are not used in the body of an article; the reasons are the subject of *Why AXF Matrices instead of Pauli and Gamma Matrices*.

Two of the multipliers that the corpus prints are single ones, because $e_t$ is the unit of the algebra and a slot carrying it collapses: the time term is the single multiplier $\tilde Q\mapsto i\tilde Q\vec e_xE$, and the multiplier $\tilde Q\mapsto-i\tilde Q\vec e_z$, which the solutions article reads on the two values $\tilde{Ξ}_{\mathrm{sp},L},\tilde{Ξ}_{\mathrm{sp},R}$, is the other single one. The derivative form of the contraction replaces $p_\mu$ by $\partial/\partial R_\mu$.

The one-mode S-matrix is not of this kind. It is a single multiplier, the action $\tilde Q\mapsto\tilde{\mathcal S}_{\Psi}\tilde Q$ of the preceding sections, and that is the structural difference between the S-matrix of a mode and the contraction that builds the propagator: one is an element read from the left, the other is a sum of two-sided terms.

## What the Algebra Supplies and What It Does Not

**What the algebra supplies.**

- *A finite-dimensional S-matrix.* Conditional on the Fock article's one-mode identification, the S-matrix of the single mode is a star-unitary element, and the star condition is an exact condition inside $\mathbb{B}$.
- *The right unitarity group.* The algebra distinguishes $\mathrm{U}(2)$, the physical one, from $\mathrm{SL}(2,\mathbb{C})$, the unit-norm group of the Lorentz rotors; the intersection is the spin rotations $\mathrm{SU}(2)$. The S-matrix's overall phase is the central $\mathrm{U}(1)$ and its spin part is a real unit quaternion.
- *The Born rule for the process.* The transition probability is the normalised Hermitian form, read as $2\,\mathrm{Sc}(\tilde\Pi_f\tilde{\mathcal S}_{\Psi}\tilde{Ϛ}_{\Psi,i}\tilde{\mathcal S}_{\Psi}^{*})$, an element-level formula using only the informational sector.
- *The generator's meaning.* When the one-mode S-matrix is generated by a Hermitian $\tilde H_\Psi \in \mathbb{B}_{\Psi}$, its quaternionic norm is $\exp(-2i\tau\,\mathrm{Sc}(\tilde H_\Psi))$: the norm measures the scalar part of the generator, and unitarity is independent of it.
- *The Cartan amplitude.* A star-unitary $\tilde{\mathcal S}_{\Psi}$ has $\tilde A_{\Phi}=e_t$: unitarity is the triviality of the amplitude. A truncation that is not star-unitary has $\tilde A_{\Phi}\neq e_t$, and the values of $\tilde A_{\Phi}$ are the absorption or gain factors.

**What it only transcribes.**

- *The Dyson series and its unitarity.* The time-ordered exponential, $S = 1+iT$, and $2\,\mathrm{Im}\,T = T^\dagger T$ are standard; the algebra realizes them in the one-mode truncation and adds no new content to them.
- *The contraction into propagators.* Wick's theorem and the Feynman propagator are the propagator article's standard material.
- *The optical theorem.* It is the diagonal of the unitarity relation and is a consequence of unitarity alone.
- *The interaction.* Which interaction Hamiltonian to use, and its vertex, are not supplied by the algebra; they are chosen by the dynamics.

**What remains a gap.**

- *The field S-matrix is not in the algebra.* The algebra hosts one mode; the field S-matrix acts on an infinite-dimensional Fock space, and the multi-mode operator algebras exceed $\mathbb{B}$ by dimension.
- *The boundary condition is not selected.* The $i\epsilon$ orientation, hence the Feynman contour and the in/out splitting, is analytic input. The algebra names the axis but not the direction, as the propagator article argued.
- *The conditional one-mode identification.* Whether the single-mode S-matrix is a structural feature of the framework or a coincidence of dimensions is inherited from the Fock article and remains undecided.

**What is interpretation.** Reading $\tilde{\mathcal S}_{\Psi}$ as a scattering operator on a qubit-like informational sector is an interpretation of the algebraic structure; the algebra contains the star-unitary element and the scalar pairing, but the identification of the two occupation states with asymptotic particle states requires the field-theoretic interpretation of the module, which is not derived here.

## The Polar Word and the Moduli of an Amplitude

The one-mode core of this article is already polar: $\tilde{\mathcal S}_{\Psi}=\exp(i\theta_0)\tilde\Pi_++\exp(i\theta_1)\tilde\Pi_-$ is a phase on each of the two states, and every star-unitary element is $\exp(i\theta)\tilde u$ with $\tilde u$ a unit real quaternion (*Norm and Pairing Conventions*, §*The Unitary Convention*). Read on the polar word $\tilde Q=r\,\varkappa_{\mathrm{phs}}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r}$ of *The Polar Decomposition of an N-Regular Biquaternion*, the four factors carry the four moduli a scattering amplitude is built from: $r$ the magnitude, $\varkappa_{\mathrm{phs}}$ the global phase, $\tilde U_{\Psi,\mathrm b}$ the frame velocity and $\tilde u_{\mathrm r}$ the spin rotation. The polar word is thus read as the four moduli of an amplitude.

The interpretation is labeled and its boundary is stated. The S-matrix of this article is finite-dimensional and conditional on the one-mode identification, and the identification of the polar factors with physical amplitude moduli is an interpretation, not a theorem: it names the shape the amplitude takes in the framework's word, and it does not compute a cross section. The owner of the polar word is *The Polar Decomposition of an N-Regular Biquaternion*.

## Open Questions

1. **Is the one-mode S-matrix structural or accidental?** The identification of a single fermionic mode with $\mathbb{B}$, and hence of its S-matrix with a star-unitary element, rests on the equality of the complex dimension of the algebra with that of the operators on a two-dimensional module. If the framework's one-mode identification is a coincidence, so is the biquaternion S-matrix.

2. **Can the algebra select the contour?** We have argued it cannot, on the ground that the Feynman, retarded and advanced propagators differ only by a boundary condition. A derivation of the $i\epsilon$ orientation from an algebraic property of $\mathbb{B}$ would contradict that argument; no candidate is offered, and the contrary possibility is recorded.

3. **Is there a biquaternion unitarity relation that is more than the star condition?** The quaternionic norm of the S-matrix is the exponential of the scalar part of its generator, which is unitarity-blind. Whether the quaternionic norm carries independent physical content for scattering — a relation between the scalar part of the Hamiltonian and an observable phase — is not established.

4. **The interaction vertex in biquaternion form.** The Dyson series here is interaction-agnostic. The biquaternion form of a specific vertex, and whether the algebra supplies any selection principle for it, belongs to the gauge-principle article and its planned companions.

5. **Time reversal and antiunitary symmetries.** The S-matrix is star-unitary; the discrete spacetime symmetries include antiunitary ones, and their biquaternion realization — involving the conjugation of the coefficients of $\mathbb{B}$ — is not treated here. It belongs to the planned companions on CPT and on the discrete symmetries, and nothing is claimed.

6. **The field S-matrix as a functional of the algebra.** Is there any sense in which the full field S-matrix is determined by a biquaternion-valued generating functional, even though it is not an element of $\mathbb{B}$? The parent articles leave the intrinsic $\mathbb{B}$-valued field and Lagrangian open; this article inherits that gap.

7. **Empirical content.** As with the rest of the framework, whether any of this yields a prediction distinguishing it from standard quantum field theory is the unanswered question. Nothing in the S-matrix construction changes that.

## Summary

The S-matrix in biquaternionic form has a small exact core and a large transcribed body. The core is finite-dimensional. Conditional on the Fock article's one-mode identification, the S-matrix of a single fermionic mode is an element of $\mathbb{B}$ that satisfies the **star condition**,

$$
\tilde{\mathcal S}_{\Psi}\tilde{\mathcal S}_{\Psi}^{*} = e_t,
$$

and that condition is *not* the unit-norm condition $\langle\tilde{\mathcal S}_{\Psi}\rangle_{\natural} = 1$: the first defines $\mathrm{U}(2)$, the second $\mathrm{SL}(2,\mathbb{C})$, and they intersect in the spin rotations $\mathrm{SU}(2)$. A fermion-parity-conserving one-mode S-matrix is

$$
\tilde{\mathcal S}_{\Psi} = \exp(i\theta_0)\tilde\Pi_+(\vec u_{\mathrm p}) + \exp(i\theta_1)\tilde\Pi_-(\vec u_{\mathrm p}),
$$

whose quaternionic norm is the scalar phase $\exp(i(\theta_0+\theta_1))$, generally not $1$. When the one-mode S-matrix is generated by a Hermitian $\tilde H_\Psi \in \mathbb{B}_{\Psi}$, $\tilde{\mathcal S}_{\Psi} = \exp(-i\tilde H_\Psi\tau)$ and

$$
\langle\tilde{\mathcal S}_{\Psi}\rangle_{\natural} = \exp\!\left(-2i\tau\,\mathrm{Sc}(\tilde H_\Psi)\right),
$$

so the quaternionic norm measures the scalar part of the generator while unitarity is independent of it. The transition probability is the Born rule applied to the star-unitary channel,

$$
P_{i\to f} = 2\,\mathrm{Sc}\!\left(\tilde\Pi_f\tilde{\mathcal S}_{\Psi}\tilde{Ϛ}_{\Psi,i}\tilde{\mathcal S}_{\Psi}^{*}\right),
$$

checked against the Bloch-vector route on a rotation and on a mixed initial state.

The transcribed body is the interaction-picture Dyson series, its unitarity $S = 1+iT$ with $2\,\mathrm{Im}\,T = T^\dagger T$, the optical theorem, and the contraction of time-ordered products into Feynman propagators, whose numerator is a sum of two-sided multipliers rather than a single one. The fermionic time-ordering sign and the $i\epsilon$ are inherited from the canonical quantization and propagator articles.

Two gaps remain, and one identification remains conditional. The field S-matrix is an operator on an infinite-dimensional Fock space and is not an element of $\mathbb{B}$: the algebra hosts one mode, and a second mode already needs operators on a module of complex dimension four. The algebra names the complex plane and the axis of the $i\epsilon$ but does not select its orientation, which is the boundary condition that distinguishes the Feynman contour and defines the in/out splitting. And whether a single mode is structural or a coincidence of dimension counts is the Fock article's open question, inherited here. As with the parent articles, the biquaternion framework supplies notation, a finite-dimensional home, and the Born pairing — not a derivation of the scattering theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, the four-dimensional algebra over $\mathbb{C}$ |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\eta^2=-e_t$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{B}_{\Phi},\mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{B}_{H}$ | Real-quaternion subspace, home of the rotation rotors |
| $\mathbb{B}_{C}=\mathbb{C}e_t$ | Centre of the algebra, home of the S-matrix's overall phase |
| $\tilde{\nabla}=e_t\partial/\partial R_t+\sum_\eta\vec e_\eta\partial/\partial R_\eta$ | Biquaternionic gradient |
| $\Box=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}$ | d'Alembertian |
| $\langle\tilde{\mathcal S}_{\Psi}\rangle_{\natural}$ | Quaternionic norm, with $\tilde{\mathcal S}_{\Psi}\tilde{\mathcal S}_{\Psi}^{\natural}=\langle\tilde{\mathcal S}_{\Psi}\rangle_{\natural}e_t$ |
| $\langle\tilde{\mathcal S}_{\Psi}\rangle_{\natural}=1$ | Unit-norm element, the Lorentz-rotor condition, $\mathrm{SL}(2,\mathbb{C})$ |
| $\tilde{\mathcal S}_{\Psi}\tilde{\mathcal S}_{\Psi}^{*}=e_t$ | Star-unitary element, $\mathrm{U}(2)$ |
| $\tilde{\mathcal S}_{\Psi}=\tilde A_{\Phi}\tilde Q_0$, $\tilde A_{\Phi}=\sqrt{\tilde{\mathcal S}_{\Psi}\tilde{\mathcal S}_{\Psi}^{*}}$ | Cartan pairing of the S-matrix; $\tilde A_{\Phi}=e_t$ exactly when $\tilde{\mathcal S}_{\Psi}\tilde{\mathcal S}_{\Psi}^{*}=e_t$ |
| $\tilde u\in\mathbb{B}_{H}$, $\langle\tilde u\rangle_{\natural}=1$ | Unit real quaternion, $\mathrm{SU}(2)$; spin rotation |
| $\tilde U_{\Psi,\mathrm b}=\cosh\frac{\theta_{\mathrm{rpd}}}{2}+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$ | Boost element, of unit quaternionic norm; $\theta_{\mathrm{rpd}}$ is the rapidity |
| $\tilde{Ξ}_{\mathrm{sp}}$ | Element of the module on which the S-matrix acts |
| $\vec u_{\mathrm p}=\vec e_z$ | Parity axis of the one mode, declared where it enters |
| $(-1)^F=i\vec u_{\mathrm p}$ | Fermion-parity element of the one mode |
| $\tilde\Pi_\pm(\vec u)=\tfrac12(e_t\pm i\vec u)$ | The two pure states of the mode, vacuum and occupied |
| $\tilde{Ϛ}_{\Psi,i}$, $\tilde\Pi_f$ | Initial state and final pure state in $\mathbb{B}_{\Psi}$ |
| $2\,\mathrm{Sc}(\tilde\Pi_f\tilde{\mathcal S}_{\Psi}\tilde{Ϛ}_{\Psi,i}\tilde{\mathcal S}_{\Psi}^{*})$ | Transition probability (Born rule) |
| $\mathcal{H}_I$, $H_I$ | Interaction Hamiltonian density and Hamiltonian |
| $\tilde H_\Psi\in\mathbb{B}_{\Psi}$, $\tilde H_\Psi^{*}=\tilde H_\Psi$ | One-mode Hermitian generator |
| $S=T\exp(-i\int d^4r\;\mathcal{H}_I)$ | S-matrix, the time-ordered exponential (Dyson series) |
| $S=1+iT$ | Forward part plus transition part |
| $\tilde{\mathcal S}_{\Psi}=e_t+i\tilde T$ | One-mode transition operator $\tilde T$ |
| $2\,\mathrm{Im}\,T=T^\dagger T$ | Unitarity relation, whose diagonal is the optical theorem |
| $S_F$ | Feynman propagator (propagator article) |
| $\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}= -m^{2}\,c^{2}$ | Biquaternion mass shell of the external legs |
| $i\tilde Q\vec e_xE-i(\vec e_x\tilde Q\vec e_y\,p_x+\vec e_y\tilde Q\vec e_y\,p_y+\vec e_z\tilde Q\vec e_y\,p_z)$ | The contraction of the propagator numerator |
| $c$ | Speed of light, restored in the mass-shell relation |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}=\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$ | Sesquilinear form of the informational sector |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the two legacy displays are not printed in the body of an article.
- John A. Wheeler, "On the Mathematical Description of Light Nuclei by the Method of Resonating Group Structure," *Physical Review* **52** (1937) 1107–1122, for the introduction of the scattering matrix.
- Werner Heisenberg, "Die 'beobachtbaren Größen' in der Theorie der Elementarteilchen," *Zeitschrift für Physik* **120** (1943) 513–538, for the S-matrix program.
- Freeman J. Dyson, "The S-Matrix in Quantum Electrodynamics," *Physical Review* **75** (1949) 1736–1755, for the time-ordered exponential and the equivalence of the interaction-picture and Heisenberg-picture formulations.
- Eugene P. Wigner, "Resonance Reactions and Anomalous Scattering," *Physical Review* **70** (1946) 15–33, for the unitarity of the collision matrix and the analytic structure of the S-matrix.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the Dyson series, Wick's theorem, and the reduction of S-matrix elements to Feynman diagrams.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the optical theorem and the unitarity relation.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the interaction picture, the S-matrix, and the LSZ reduction in the convention used here.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the derivation of the S-matrix from asymptotic states and the unitarity of the scattering operator.
- R. Haag, *Local Quantum Physics: Fields, Particles, Algebras* (Springer, 1996), for the algebraic setting in which the S-matrix is an operator and scattering states are constructed from local fields.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the two-valued structure behind the star condition and the unit-norm condition.
- Companion articles: [Canonical Quantization of the Biquaternion Dirac Field](canonical-quantization-of-the-biquaternion-dirac-field.html); [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html); [The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit](the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html); [The LSZ Reduction Formula in Biquaternionic Form](the-lsz-reduction-formula-in-biquaternionic-form.html); [The Feynman Propagator in Biquaternionic Form](the-feynman-propagator-in-biquaternionic-form.html); [Fock Space and Creation/Annihilation Operators in Biquaternionic Form](fock-space-and-creation-annihilation-operators-in-biquaternionic-form.html); [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html); [Canonical Quantization of the Biquaternion Maxwell Field](canonical-quantization-of-the-biquaternion-maxwell-field.html); [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html); [Quantum Physics in Biquaternionic Form](quantum-physics-in-biquaternionic-form.html); [The KMS Condition and the Biquaternion Framework](the-kms-condition-and-the-biquaternion-framework.html); [The Polar Decomposition and Its Three Pairings](the-polar-decomposition-and-its-three-pairings.html); [The General Polar Decomposition, the Amplitude and the Operator-to-State Map](the-general-polar-decomposition-the-amplitude-and-the-operator-to-state-map.html); [The Polar Decomposition of an N-Degenerate Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-degenerate-biquaternion.html); [Operators Acting on Two Sides](../articles_maths/operators-acting-on-two-sides.html); [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html); [The Unstable State and the Complex Energy Pole in Biquaternionic Form](the-unstable-state-and-the-complex-energy-pole-in-biquaternionic-form.html).
