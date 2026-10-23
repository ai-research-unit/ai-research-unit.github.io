# __The S-Matrix in Biquaternionic Form__

## Introduction

The **S-matrix** is the operator that carries the state of a scattering experiment from the remote past to the remote future. In the interaction picture it is the time-ordered exponential of the interaction Hamiltonian,

$$
S \;=\; T\exp\!\left(-i\int d^4x\;\mathcal{H}_I(x)\right),
$$

and the transition probability is the squared matrix element $|\langle f|S|i\rangle|^2$. Its defining property is **unitarity**, $S^{*} S = 1$. It is the object in which the dynamics of an interacting field theory is summarized.

The companion articles have assembled every ingredient this article needs. *Canonical Quantization of the Biquaternion Dirac Field* promotes the biquaternion Dirac field to an operator-valued field, builds the mode algebra, and produces a Fock space, recording that the construction transcribes standard canonical quantization rather than deriving it from the algebra $\mathbb{B}$. *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* sharpens that result: the Fock space is a **module** over $\mathbb{B}$, not an object of it, and the algebra hosts exactly one fermionic mode. *The Feynman Propagator in Biquaternionic Form* supplies the two-point function and the finding that the algebra provides the complex plane and the axis of the $i\epsilon$ but not the orientation that selects the Feynman contour.

This article asks what "the S-matrix in biquaternionic form" names. The finding is stated at the outset.

- **Established, and recomputed below.** Conditional on the one-mode identification of the Fock article, the S-matrix of a single fermionic mode is a **matrix-unitary** element of $\mathbb{B}$. Matrix unitarity, $\tilde{S}\tilde{S}^{*} = e_t$, is *not* the biquaternion-norm condition $\tilde{S}\tilde{S}^{\natural} = e_t$ that the framework uses to define its Lorentz rotors. The two conditions define different groups, $\mathrm{U}(2)$ and $SL(2,\mathbb{C})$, and they intersect in the spin rotations $SU(2)$; the S-matrix belongs to the first, not the second. Every matrix-unitary biquaternion factors as $\tilde{S} = \exp(i\theta)\tilde u$ with $\tilde u$ a unit real quaternion, and a parity-conserving one-mode S-matrix is $\tilde{S} = \exp(i\theta_0)\tilde\Pi_+ + \exp(i\theta_1)\tilde\Pi_-$, whose biquaternion norm is the phase $\exp(i(\theta_0+\theta_1))$, generally not $e_t$. Its transition probabilities are given by the trace formula $2\,\mathrm{Sc}(\tilde\Pi_f\,\tilde{S}\tilde{Ϛ}_i\,\tilde{S}^{*})$.
- **Standard, and transcribed.** The interaction picture, the Dyson series, the unitarity relation $S = 1+iT$, the finite-dimensional identity $2\,\mathrm{Im}\,T = T^\dagger T$, the optical theorem, and the contraction of the Dyson series into Feynman propagators by Wick's theorem. None of this depends on the biquaternion structure beyond the kinematical conventions already fixed by the read-list articles.
- **Gap, left visible.** The S-matrix of the *field* is an operator on an infinite-dimensional Fock space and is **not** an element of $\mathbb{B}$; the algebra hosts at most the one-mode truncation. And the algebra does not select the boundary condition — the $i\epsilon$ orientation, equivalently the in/out splitting — that makes the time-ordered exponential a well-defined distributional object. That gap is inherited from the propagator article and is not closed here.

The article is organized as follows. The next section fixes the interaction-picture definition and the Dyson series. The section after that separates the two inequivalent interpretations of "unitary" inside $\mathbb{B}$, which is where a sign or a group can silently go wrong. The following section constructs the one-mode S-matrix and states exactly how far the algebra reaches. The next section records the transition probability and the Born rule. A section derives and checks the unitarity (optical) relation. A section returns to the Dyson series and its contractions, and locates the boundary-condition gap. A section separates what the algebra supplies from what it only transcribes. The article closes with open questions.

## The S-Matrix in the Interaction Picture

Split the Hamiltonian into a free part and an interaction, $H = H_0 + H_I$, and write the fields in the interaction picture, where they evolve with $H_0$ and the state evolves with $H_I$. The evolution operator is

$$
U_I(t',t'_1) \;=\; T\exp\!\left(-i\int_{t'_1}^{t'}dt'_2\,H_I(t'_2)\right),
$$

with $T$ the time-ordering operator, and the S-matrix is the limit

$$
S \;=\; U_I(+\infty,-\infty).
$$

Expanding the exponential gives the **Dyson series**,

$$
S \;=\; \sum_{n=0}^{\infty}\frac{1}{n!}\left(-i\right)^{n}
\int d^4x_1\cdots d^4x_n\; T\big\{\mathcal{H}_I(x_1)\cdots\mathcal{H}_I(x_n)\big\},
$$

the $n=0$ term being the identity. Since $H_I$ is Hermitian, the evolution operator obeys $i\,\partial/\partial t' U_I(t',t'_1) = H_I(t')U_I(t',t'_1)$ with $U_I(t'_1,t'_1) = 1$, which gives $U_I^\dagger U_I = 1$; hence the S-matrix is unitary, $S^{*} S = 1$. (Individual truncations of the Dyson series are not unitary; it is the summed operator that is.)

Three features of this construction are worth naming, because they are the points at which the biquaternion structure enters.

**The time ordering is fermionic.** The fields in $\mathcal{H}_I$ are the biquaternion Dirac field on its spinor module, and their time-ordered products carry the anticommutation sign. This is the same sign that the propagator article traced, and it is not an extra convention: it is the statement that the field operators anticommute, inherited from the canonical quantization article.

**The $i$ in the exponent is the algebra's scalar imaginary.** The factor $-i$ is built from the same central element $i$ that makes the material time coordinate $ict'$ and that appears in the deformed mass shell $\tilde{P}\tilde{P}^{\natural}/\hbar^{2}+m^2-i\epsilon$. The algebra names this element; it does not choose its sign in the exponent, which is fixed by the convention that $S$ be unitary and that forward time evolution be generated by $\exp(-iHt')$.

**The interaction is written in biquaternion notation.** The interaction Hamiltonian is built from the biquaternion fields and their conjugates; its specific form — for electromagnetism, the minimal coupling of the Dirac current to the potential — is the gauge-principle article's subject and is not rederived here. Nothing below depends on which interaction is chosen; the structural statements are about the S-matrix as a unitary operator, not about a particular vertex.

The S-matrix is usually separated into the forward part and the transition part,

$$
S \;=\; 1 + iT,
$$

with $T$ the transition operator. Unitarity then reads

$$
(1-iT^\dagger)(1+iT) = 1
\;\;\Longleftrightarrow\;\;
T-T^\dagger = i\,T^\dagger T
\;\;\Longleftrightarrow\;\;
2\,\mathrm{Im}\,T = T^\dagger T,
$$

where $\mathrm{Im}\,T := (T-T^\dagger)/(2i)$. This is the exact unitarity relation; its diagonal matrix elements are the optical theorem, and it is derived and checked in the one-mode case below.

## Two Notions of Unitary in the Algebra

The word "unitary" has two inequivalent interpretations inside $\mathbb{B}$, and the S-matrix forces the distinction. This is the section where a formula can be right and its interpretation wrong.

The framework's own usage is the **biquaternion norm**. The introduction defines the Lorentz rotor group as the unit-norm biquaternions,

$$
\tilde U\tilde U^{\natural} = e_t
\;\;\Longleftrightarrow\;\;
\langle\tilde U\rangle_{\natural} := \tilde U\tilde U^{\natural} = e_t,
$$

where $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \sum_\mu Q_\mu^2$ is the biquaternion norm, and identifies this group with $SL(2,\mathbb{C})$. In the matrix representation $\langle\cdot\rangle_{\natural}$ is the determinant: for $\tilde S = a\,e_t + b\,\vec e_x + c\,\vec e_y + d\,\vec e_z$,

$$
\mathsf{M}_2(\tilde S) = aI_2 - i(b\sigma_1+c\sigma_2+d\sigma_3),
\qquad
\det\mathsf{M}_2(\tilde S) = a^2+b^2+c^2+d^2 = \langle\tilde S\rangle_{\natural}.
$$

So the unit-norm condition is $\det\mathsf{M}_2(\tilde S) = 1$, a single complex equation, two real conditions on eight real parameters.

The condition the S-matrix needs is different. Unitarity of an operator on a Hilbert space is $\mathsf{M}_2(\tilde S)^\dagger\mathsf{M}_2(\tilde S) = I_2$, which in the algebra reads

$$
\boxed{\;\tilde S\tilde S^{*} = e_t\;}.
$$

Because $\tilde S\tilde S^{*}$ is Hermitian, this is four real conditions on eight real parameters.

The two conditions are inequivalent, and neither contains the other.

| Condition | Biquaternion form | Matrix form | Group | Real dimension |
|---|---|---|---|---|
| Unit norm | $\tilde S\tilde S^{\natural} = e_t$ | $\det\mathsf{M}_2(\tilde S)=1$ | $SL(2,\mathbb{C})$ | 6 (non-compact) |
| Matrix unitary | $\tilde S\tilde S^{*} = e_t$ | $\mathsf{M}_2(\tilde S)^\dagger\mathsf{M}_2(\tilde S)=I_2$ | $\mathrm{U}(2)$ | 4 (compact) |

**Neither membership implies the other.** A boost biquaternion

$$
\tilde U = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\vec u_{\mathrm b},
\qquad \vec u_{\mathrm b}^2 = -e_t,
$$

has $\langle\tilde U\rangle_{\natural} = 1$ and so lies in $SL(2,\mathbb{C})$, but $\tilde U\tilde U^{*} = \tilde U^2 = \cosh\psi + i\sinh\psi\,\vec u_{\mathrm b} \neq e_t$; its square is not the identity, so it is not matrix-unitary. Conversely, a matrix-unitary biquaternion is generally not of unit norm: the central phase $\tilde S = \exp(i\theta)e_t$ is unitary for every real $\theta$, but $\langle \exp(i\theta)e_t\rangle_{\natural} = \exp(2i\theta)$, which equals $1$ only for $\theta \in \pi\mathbb{Z}$.

This distinction is exactly the one the informational-space article draws when it warns that "only the rotation rotors are unitary in the matrix sense", and it is the reason the phrase "unit-norm biquaternion" must not be silently read as "unitary operator". A Lorentz rotor of unit norm that is not a pure rotation is *not* a unitary operator, and a physical S-matrix is *not* in general a unit-norm biquaternion.

**The intersection is the spin rotations.** The elements that satisfy both conditions are the real unit quaternions

$$
\tilde u\tilde u^{\natural} = e_t, \qquad \tilde u \in \mathbb{H}_{\mathbb{B}},
$$

which form $SU(2)$; in the matrix representation these are $\tilde u = \cos\frac{\alpha}{2}e_t + \sin\frac{\alpha}{2}\,\vec u_{\mathrm r}\cdot\mathbf{e}$, the spin rotations of the angular-momentum article. The intersection $\mathrm{U}(2)\cap SL(2,\mathbb{C}) = SU(2)$ is therefore the rotation subgroup, consistent with the informational-space article's statement that only the rotation rotors are unitary in the matrix sense (the introduction's statement is the weaker one, that the rotation rotors lie in $\mathbb{H}_{\mathbb{B}}$).

**The structure of the matrix-unitary group.** Every element of $\mathrm{U}(2)$ factors into a central phase and a spin rotation,

$$
\tilde S = \exp(i\theta)\,\tilde u, \qquad \tilde u \in \mathbb{H}_{\mathbb{B}},\; \tilde u\tilde u^{\natural} = e_t,
$$

where the phase $\exp(i\theta)$ lies in the centre $\mathbb{C}_{\mathbb{B}}$ and commutes with everything, and the rotor carries the $SU(2)$ part. The parametrization is two-to-one, $(\exp(i\theta),\tilde u)\sim(\exp(i(\theta+\pi)),-\tilde u)$, because $-e_t$ is itself a real unit quaternion; this is the usual $\mathrm{U}(2) = \mathrm{U}(1)\cdot SU(2)$ up to the shared centre. The central phase that appears here is the same unitary part of the centre that the gauge principle identifies as the abelian gauge group; the S-matrix's overall phase and the Maxwell $\mathrm{U}(1)$ are the same one-parameter subgroup of $\mathbb{B}$. We record this as an observation and do not develop it.

The check that matters is independent of the examples that suggested the formulas. The three claims — that the two conditions are inequivalent, that $\mathrm{U}(2)$ elements factor as $\exp(i\theta)\tilde u$, and that the intersection is $SU(2)$ — were recomputed as follows. The isomorphism $\mathsf{M}_2$ and the identity $\det\mathsf{M}_2(\tilde S) = \langle\tilde S\rangle_{\natural}$ were checked on random biquaternions to a maximum absolute error of order $10^{-15}$. Two hundred generic unit-norm biquaternions — complex-coefficient elements with $\sum_\mu S_\mu^2 = 1$, which are the bulk of $SL(2,\mathbb{C})$ — were tested for matrix unitarity: none passed. That is as expected, because the unit-norm elements that *are* unitary are the measure-zero intersection $SU(2)$. Three hundred random $\mathrm{U}(2)$ elements of the form $\exp(i\theta)\tilde u$ were tested by extracting $\theta$ from $\det\mathsf{M}_2(\tilde S)$ and checking that the remainder $\exp(-i\theta)\tilde S$ has real coefficients; the largest imaginary part was of order $10^{-16}$. Boost biquaternions at $\psi = 0.7, 1.5, 2.3$ all had $\langle\tilde U\rangle_{\natural}=1$ and all failed matrix unitarity, with $\tilde U\tilde U^{*}=\tilde U^2=\cosh\psi+i\sinh\psi\,\vec u_{\mathrm b}$, whose scalar part alone is $\cosh\psi$ (a matrix equal to $\cosh\psi\,e_t$ is obtained instead for the *real-quaternion* element $\cosh(\psi/2)e_t+\sinh(\psi/2)\vec u_{\mathrm b}$, which is not Hermitian and not the boost above). The random tests were run on elements generated by the general parametrizations, not on the special cases used to state the claims.

## The One-Mode S-Matrix

The algebra can host an S-matrix only where the Fock article's one-mode identification applies. The field S-matrix is an operator on the exterior algebra of the spinor-module solution space, an infinite-dimensional object; the algebra $\mathbb{B}$ is four-dimensional and cannot contain it. For a single fermionic mode, however, the Fock space is the two-dimensional **fundamental module** of $\mathbb{B}\cong M_2(\mathbb{C})$, on which $\mathbb{B}$ acts as the full operator algebra, and an S-matrix on that module is an element of $\mathbb{B}$. It is the one case where the S-matrix is a biquaternion.

**Conditional statement.** *If* a single mode of the Dirac field is isolated and its scattering is described on the two-dimensional module, *then* the one-mode S-matrix is a matrix-unitary element of $\mathbb{B}$,
$$
\tilde S\tilde S^{*} = e_t, \qquad \tilde S \in \mathbb{B}.
$$
The conditionality is the Fock article's: whether the one-mode identification is a structural feature of the framework or a coincidence of the dimension count $\dim_\mathbb{C}M_2(\mathbb{C}) = 4 = \dim_\mathbb{C}\mathbb{B}$ is not decided there, and this article does not decide it either. The S-matrix is not a derivation from the algebra; it is the algebra's one-mode truncation of a standard operator.

**The physical one-mode S-matrix is diagonal.** An S-matrix must conserve fermion parity: a scattering process cannot turn an even state into an odd one. Parity conservation is the statement that $\tilde S$ commutes with the grading $(-1)^F = i\vec e_z$, and the elements of $\mathbb{B}$ that commute with $i\vec e_z$ are exactly the complex span of $e_t$ and $i\vec e_z$, which is also the span of the two occupation idempotents $\tilde\Pi_+ = \tfrac12(e_t+i\vec e_z)$ and $\tilde\Pi_- = \tfrac12(e_t-i\vec e_z)$. Here $i\vec e_z$ is a root of $+1$, $(i\vec e_z)^2=e_t$, and $\tilde\Pi_+$ and $\tilde\Pi_-$ are its two associated idempotents. A parity-conserving S-matrix therefore has the form

$$
\boxed{\;\tilde S = \exp(i\theta_0)\,\tilde\Pi_+ + \exp(i\theta_1)\,\tilde\Pi_-, \qquad \tilde\Pi_\pm = \tfrac12\left(e_t\pm i\vec e_z\right)\;},
$$

because unitarity forces the two eigenvalues to lie on the unit circle. This is the one-mode S-matrix in its physical form: a phase on the vacuum and a phase on the occupied mode, which is what "no particle creation or annihilation in the asymptotic region" means at this level.

**Its biquaternion norm is a phase, not one.** The quaternion conjugate of $\tilde\Pi_\pm$ is $\tilde\Pi_\mp$, so

$$
\tilde S\tilde S^{\natural} = \exp(i(\theta_0+\theta_1))(\tilde\Pi_+ + \tilde\Pi_-) = \exp(i(\theta_0+\theta_1))\,e_t .
$$

The parity-conserving one-mode S-matrix is unit norm only when $\theta_0+\theta_1 \in 2\pi\mathbb{Z}$. This is the concrete form of the previous section's warning: a physically unitary S-matrix is generally not in $SL(2,\mathbb{C})$, and one should not assign it to the Lorentz rotor group on the strength of the word "unitarity". Computed for three parameter pairs with $\theta_0,\theta_1$ at generic values, the matrix unitarity held, $\tilde S$ commuted with $i\vec e_z$, and $\langle\tilde S\rangle_{\natural}$ matched $\exp(i(\theta_0+\theta_1))$ to machine precision — none of the three had $\langle\tilde S\rangle_{\natural}=1$.

**The S-matrix generated by a biquaternion Hamiltonian.** The finite-dimensional S-matrix also has a generator form. If the one-mode dynamics over an interval of duration $\tau$ is generated by a Hermitian biquaternion $\tilde H \in \mathbb{M}_+$, then

$$
\tilde S = \exp(-i\tilde H\tau),
$$

and $\tilde H^{*} = \tilde H$ with $i$ central gives $\tilde S^{*} = \exp(+i\tilde H\tau) = \tilde S^{-1}$, so $\tilde S$ is matrix-unitary, as it must be. What the biquaternion norm computes here is instructive. Since $\det\mathsf{M}_2(\tilde S) = \exp(\mathrm{tr}\,\mathsf{M}_2(-i\tilde H\tau))$ and the trace pairing gives $\mathrm{Tr}(\tilde H) = 2\,\mathrm{Sc}(\tilde H)$,

$$
\langle\tilde S\rangle_{\natural} = \langle\tilde S,\tilde S\rangle_{\natural} = \det\mathsf{M}_2(\tilde S) = \exp\!\left(-2i\tau\,\mathrm{Sc}(\tilde H)\right).
$$

So the biquaternion norm of the one-mode S-matrix is the exponential of the trace of its generator, and it equals $e_t$ whenever the generator is traceless, $\mathrm{Sc}(\tilde H) = 0$. For a generic duration $\tau$ that is the only way it returns to $e_t$; at the special durations with $2\tau\,\mathrm{Sc}(\tilde H)\in 2\pi\mathbb{Z}$ it returns to $e_t$ with a nonzero trace as well — $\tilde H=\pi e_t$ at $\tau=1$ gives $\tilde S=-e_t$, which is matrix-unitary with $\langle\tilde S\rangle_{\natural}=1$ — so the "precisely" is meant generically in $\tau$. This was verified numerically for a Hermitian generator with and without a scalar part: for $\mathrm{Sc}(\tilde H)=0$ the biquaternion norm was $1$ to $10^{-10}$; for $\mathrm{Sc}(\tilde H)=0.8$ it matched $\exp(-2i\tau\,\mathrm{Sc}(\tilde H))$ at both $\tau = 0.6$ and $\tau = 1.7$; and matrix unitarity held in every case. The biquaternion norm is thus not a unitarity condition at all: it measures the *trace* of the generator, and unitarity is blind to it.

### The Cartan Factor of the S-Matrix

Every element off the cone has the Cartan pairing $\tilde S=\tilde A\tilde U$, with $\tilde A=\sqrt{\tilde S\tilde S^{*}}$ Hermitian positive and $\tilde U=\tilde A^{-1}\tilde S$ unitary; at a rank-one point of the cone $\tilde A$ is rank one and $\tilde U$ is the partial isometry of the generalized pairing (*The Polar Decomposition and Its Three Pairings*; *The Generalized Polar Decomposition of a Biquaternion*). Here $\tilde A$ is the Cartan amplitude, written $\tilde H$ in the pairing article; the letter is changed because $\tilde H$ is the generator in this article. For the one-mode S-matrix, matrix unitarity is exactly the statement that the amplitude is trivial:

$$
\tilde S\tilde S^{*}=e_t
\qquad\Longrightarrow\qquad
\tilde A=e_t,\qquad \tilde U=\tilde S .
$$

A unitary S-matrix carries only phase: its Cartan amplitude is the identity. This is the scattering form of the statement that unitarity is the triviality of the Hermitian factor: the S-matrix's polar word has scale one and no boost, and its content is the central phase and the spin rotation.

The non-trivial case is a truncation, not the full S-matrix. If probability leaves the one-mode sector — a channel to unobserved modes, or an open-system effective S-matrix — the element can be $\tilde S=\tilde\Pi_+ + a\tilde\Pi_-$ with $0<a<1$ (or $a>1$ for gain). Then $\tilde A=\tilde\Pi_+ + a\tilde\Pi_-$ and $\tilde U=e_t$; the eigenvalues of $\tilde A$ are the absorption factors, and $1-a^{2}$ is the probability lost (negative for gain). The same amplitude-versus-phase split appears for a resonance pole, where the Cartan amplitude of the pole term is $e^{-\Gamma t/2\hbar}$ (see *The Unstable State and the Complex Energy Pole*, §*The Complex Angle of the Resonance*). At $a=0$ the amplitude is rank one, the second factor is the partial isometry $\tilde\Pi_+$, and the generalized pairing is the one that applies. The article's S-matrix is unitary by construction, so its Cartan factor is $e_t$; the non-unitary reading belongs to the truncation and is not claimed for the field S-matrix.

**Then the algebra stops.** A second mode already needs the two-mode operator algebra $M_4(\mathbb{C})$, of complex dimension sixteen, which does not embed in the four-dimensional $\mathbb{B}$; this is the Fock article's capacity count, and the S-matrix inherits it. Consequently the S-matrix of a spin-flip between two modes, or of any genuinely multi-mode process, is not an element of $\mathbb{B}$ on any interpretation. The finite-dimensional S-matrix is not a truncation of the field S-matrix to a subalgebra; it is the field S-matrix's action on the single module the algebra happens to carry.

## The S-Matrix Element and the Born Rule

The S-matrix element is read off the algebra of the informational sector. For an initial state described by a positive element $\tilde{Ϛ}_i \in \mathbb{M}_+$ normalised by $\langle\tilde{Ϛ}_i,e_t\rangle_{*}=\tfrac12$ (trace one in the $2\times2$ image) and a final measurement represented by a Hermitian idempotent $\tilde\Pi_f \in \mathbb{M}_+$, the transition probability is

$$
\boxed{\;P_{i\to f} \;=\; \mathrm{Tr}\!\left(\tilde\Pi_f\,\tilde S\,\tilde{Ϛ}_i\,\tilde S^{*}\right)
\;=\; 2\,\mathrm{Sc}\!\left(\tilde\Pi_f\,\tilde S\,\tilde{Ϛ}_i\,\tilde S^{*}\right)\;},
$$

which is the Born rule of the informational-space article applied to the scattering channel $\tilde{Ϛ}_i \mapsto \tilde S\tilde{Ϛ}_i\tilde S^{*}$. The S-matrix acts as a **reversible** channel: it is matrix-unitary, in contrast with the idempotent projections that implement measurement. The reversible/irreversible dichotomy of $\mathbb{M}_+$ is thus visible in the scattering formalism, with the S-matrix on the reversible side.

The formula was checked against the elementary Born rule on cases chosen for the purpose rather than for convenience. Take the two occupation states $|0\rangle,|1\rangle$ with idempotents $\tilde\Pi_+ = \tfrac12(e_t+i\vec e_z)$ and $\tilde\Pi_- = \tfrac12(e_t-i\vec e_z)$, and take for $\tilde S$ a spin rotation about $\vec e_y$,

$$
\tilde S = \cos\frac{\theta}{2}\,e_t + \sin\frac{\theta}{2}\,\vec e_y,
$$

whose matrix is $\mathsf{M}_2(\tilde S) = \begin{pmatrix}\cos\frac{\theta}{2} & -\sin\frac{\theta}{2}\\ \sin\frac{\theta}{2} & \cos\frac{\theta}{2}\end{pmatrix}$. For $\theta = 0.77$ the two routes give

$$
\mathrm{Tr}\!\left(\tilde\Pi_0\,\tilde S\,\tilde\Pi_1\,\tilde S^{*}\right)
= 2\,\mathrm{Sc}\!\left(\tilde\Pi_0\,\tilde S\,\tilde\Pi_1\,\tilde S^{*}\right)
= |\langle 0|\tilde S|1\rangle|^2 = \sin^2\!\frac{\theta}{2} = 0.141044665\ldots,
$$

agreeing to machine precision. A mixed initial state $\tilde{Ϛ}_i = \tfrac12(e_t + 0.4\,i\vec e_z)$, which is positive and of trace one, gave $\mathrm{Tr}(\tilde\Pi_0\tilde S\tilde{Ϛ}_i\tilde S^{*}) = 2\,\mathrm{Sc}(\tilde\Pi_0\tilde S\tilde{Ϛ}_i\tilde S^{*}) = 0.643582134\ldots$ by both routes. The trace formula is the operational content of the one-mode S-matrix: it turns the biquaternion $\tilde S$ into numbers.

Nothing in this section is specific to a scattering process. The normalised Hermitian form is the Born rule, read here as the trace formula, and it would apply to any unitary biquaternion acting on the one-mode state space; the S-matrix is one such element. That generality is the honest interpretation: the algebra supplies the state space, the operator, and the pairing, and the *interpretation* of the pairing as a scattering cross-section requires the field-theoretic measure that the algebra does not contain.

## Unitarity, the Optical Theorem, and the Algebra

The unitarity relation of the interaction picture is an algebraic identity in the one-mode truncation, and it is worth deriving it there because it is where the S-matrix's unitarity is actually used.

With $\tilde S = e_t + i\tilde Q$, the condition $\tilde S^{*}\tilde S = e_t$ gives, in the algebra,

$$
(e_t-i\tilde Q^{*})(e_t+i\tilde Q) = e_t
\;\;\Longleftrightarrow\;\;
i(\tilde Q-\tilde Q^{*}) + \tilde Q^{*}\tilde Q = 0
\;\;\Longleftrightarrow\;\;
2\,\mathrm{Im}\,\tilde Q = \tilde Q^{*} \tilde Q,
$$

with $\mathrm{Im}\,\tilde Q := \tfrac{1}{2i}(\tilde Q-\tilde Q^{*}) \in \mathbb{M}_+$. (Using $\tilde S\tilde S^{*} = e_t$ instead gives $2\,\mathrm{Im}\,\tilde Q = \tilde Q\tilde Q^{*}$, which agrees because $\tilde Q$ built from a unitary $\tilde S$ is normal.) This is the same relation as the operator identity $2\,\mathrm{Im}\,T = T^\dagger T$ written for the one-mode truncation, and it is an exact biquaternion identity: it says that the Hermitian part $2\,\mathrm{Im}\,\tilde Q$ equals the positive element $\tilde Q^{*}\tilde Q$.

The identity was checked on elements not used to state it. For four independently generated matrix-unitary biquaternions $\tilde S = \exp(i\theta)\tilde u$ with random central phase and random spin axis, $\tilde Q = (\tilde S-e_t)/i$ was formed and the difference $2\,\mathrm{Im}\,\tilde Q - \tilde Q^{*}\tilde Q$ was computed in the algebra; its largest component was of order $10^{-16}$, so the identity holds to machine precision.

The physical content is the **optical theorem**: the diagonal element $\langle i|2\,\mathrm{Im}\,T|i\rangle = \langle i|T^\dagger T|i\rangle$ is positive and equals the summed transition probability out of the initial state, so it is the total rate, and in a field theory with a continuum of final states it becomes the usual relation between the forward scattering amplitude and the total cross-section. The optical theorem is the statement that the operator $S$ is unitary; the algebra does not weaken or strengthen it, and in the one-mode truncation it is the exact identity above.

One should not oversell what was checked. The identity $2\,\mathrm{Im}\,T = T^\dagger T$ is a consequence of matrix unitarity alone; it is true for any unitary matrix and hence for any matrix-unitary biquaternion, and the numerical check confirms the algebra implements it correctly rather than testing a biquaternion-specific claim. The genuinely biquaternion statements are the two of the preceding sections: that matrix unitarity is the right condition and not biquaternion-norm unitarity, and that the one-mode truncation is the whole of the algebra's reach.

## The Dyson Series, the Propagator, and the Contour

The Dyson series is evaluated by **Wick's theorem**: the time-ordered product of field operators is the sum over all contractions, and each contraction is a two-point function. The contractions are exactly the objects of the propagator article: the positive- and negative-frequency pieces $W_\pm$, and their time-ordered combination $S_F$ with its Feynman contour. The biquaternion content of the S-matrix is therefore inherited from the propagator's, not independent of it.

Three inheritances should be named.

**The fermionic sign.** The relative minus in the time ordering is the anticommutator of the field, and it propagates into a minus sign on every closed fermion loop of a Feynman diagram. It is the same sign the propagator article chose the contour to reproduce.

**The $i\epsilon$.** The time-ordered exponential requires the interaction to be switched on and off adiabatically in the remote past and future, which is a deformation of the integration contour by the same $i\epsilon$ that makes $S_F$ a distribution. The propagator article's finding applies verbatim: the algebra provides the complex plane and locates the deformation along the $ict'$ axis of $\mathbb{M}_-$, but the *orientation* — Feynman versus anti-Feynman, and the in/out splitting itself — is a boundary condition that the algebra does not select.

**The asymptotic states.** In and out states are plane-wave states of the parent's solutions, labeled by on-shell momenta; the on-shell condition is the biquaternion mass shell $\tilde P\tilde P^{\natural}=-m^2c^2$. The reduction of the S-matrix element to an amputated correlation function — the LSZ formula — replaces each external leg by the corresponding plane wave and applies the wave operator. The biquaternion form of that reduction is the placement of the external legs on the mass shell and is not rederived here; what matters is that the external data are the parent's biquaternion plane waves, and the internal data are the propagator, so the whole Dyson series is written in the read-list notation without a new ingredient.

The gap is therefore the propagator's gap, seen from the S-matrix side: the algebra can *write* the time-ordered exponential and can name the $i\epsilon$, but it cannot *choose* the contour, and the choice is what makes the exponential well-defined as a distribution. This article inherits that gap and records it rather than closing it.

## What the Algebra Supplies and What It Does Not

**What the algebra supplies.**

- *A finite-dimensional S-matrix.* Conditional on the Fock article's one-mode identification, the S-matrix of the single mode is a matrix-unitary biquaternion, and matrix unitarity is an exact condition inside $\mathbb{B}$.
- *The right unitarity group.* The algebra distinguishes $\mathrm{U}(2)$, the physical one, from $SL(2,\mathbb{C})$, the biquaternion-norm group of the Lorentz rotors; the intersection is the spin rotations $SU(2)$. The S-matrix's overall phase is the central $\mathrm{U}(1)$ and its spin part is a real unit quaternion.
- *The Born rule for the process.* The transition probability is the normalised Hermitian form, read through the trace $2\,\mathrm{Sc}(\tilde\Pi_f\tilde S\tilde{Ϛ}_i\tilde S^{*})$, an element-level formula using only the informational sector.
- *The generator's meaning.* When the one-mode S-matrix is generated by a Hermitian $\tilde H \in \mathbb{M}_+$, its biquaternion norm is $\exp(-2i\tau\,\mathrm{Sc}(\tilde H))$: the biquaternion norm measures the trace of the generator, and unitarity is independent of it.
- *The Cartan amplitude.* A matrix-unitary $\tilde S$ has $\tilde A=e_t$: unitarity is the triviality of the amplitude. A non-unitary truncation has $\tilde A\neq e_t$, and the eigenvalues of $\tilde A$ are the absorption or gain factors.

**What it only transcribes.**

- *The Dyson series and its unitarity.* The time-ordered exponential, $S = 1+iT$, and $2\,\mathrm{Im}\,T = T^\dagger T$ are standard; the algebra realizes them in the one-mode truncation and adds no new content to them.
- *The contraction into propagators.* Wick's theorem and the Feynman propagator are the propagator article's standard material.
- *The optical theorem.* It is the diagonal of the unitarity relation and is a consequence of unitarity alone.
- *The interaction.* Which interaction Hamiltonian to use, and its vertex, are not supplied by the algebra; they are chosen by the dynamics.

**What is a gap.**

- *The field S-matrix is not in the algebra.* The algebra hosts one mode; the field S-matrix acts on an infinite-dimensional Fock space, and the multi-mode operator algebras exceed $\mathbb{B}$ by dimension.
- *The boundary condition is not selected.* The $i\epsilon$ orientation, hence the Feynman contour and the in/out splitting, is analytic input. The algebra names the axis but not the direction, as the propagator article argued.
- *The conditional one-mode identification.* Whether the single-mode S-matrix is a structural feature of the framework or a coincidence of dimensions is inherited from the Fock article and remains undecided.

**What is interpretation.** Reading $\tilde S$ as a scattering operator on a qubit-like informational sector is an interpretation of the algebraic structure; the algebra contains the unitary element and the trace pairing, but the identification of the two occupation states with asymptotic particle states requires the field-theoretic interpretation of the module, which is not derived here.

## The Polar Word and the Moduli of an Amplitude

The one-mode core of this article is already polar: $\tilde S=\exp(i\theta_0)\tilde\Pi_++\exp(i\theta_1)\tilde\Pi_-$ is a scale times a phase on each idempotent, and every matrix-unitary biquaternion is $\exp(i\theta)\tilde u$ with $\tilde u$ a unit real quaternion. Read on the polar word $\tilde Q=r\,\exp(i\alpha)B\tilde u$ of *The Polar Decomposition of Biquaternions*, the four factors carry the four moduli a scattering amplitude is built from: $r$ the magnitude, $\alpha$ the global phase, $B$ the frame velocity and $\tilde u$ the spin rotation, so the polar word is read as the four moduli of an amplitude.

The interpretation is labelled and its boundary is stated. The S-matrix of this article is finite-dimensional and conditional on the one-mode identification, and the identification of the polar factors with physical amplitude moduli is an interpretation and not a theorem: it names the shape the amplitude takes in the framework's word, and it does not compute a cross section. The owner of the polar word is *The Polar Decomposition of Biquaternions*.

## Open Questions

1. **Is the one-mode S-matrix structural or accidental?** The identification of a single fermionic mode with $\mathbb{B}$ and hence of its S-matrix with a matrix-unitary biquaternion rests on $\dim_\mathbb{C}M_2(\mathbb{C}) = \dim_\mathbb{C}\mathbb{B}$. If the framework's one-mode identification is a coincidence, so is the biquaternion S-matrix.

2. **Can the algebra select the contour?** We have argued it cannot, on the ground that Feynman, retarded, and advanced differ only by a boundary condition. A derivation of the $i\epsilon$ orientation from an algebraic property of $\mathbb{B}$ would contradict that argument; no candidate is offered, and the contrary possibility is recorded.

3. **Is there a biquaternion unitarity relation that is more than matrix unitarity?** The biquaternion norm of the S-matrix is the exponential of the trace of its generator, which is unitarity-blind. Whether the biquaternion norm carries independent physical content for scattering — a relation between the trace of the Hamiltonian and an observable phase — is not established.

4. **The interaction vertex in biquaternion form.** The Dyson series here is interaction-agnostic. The biquaternion form of a specific vertex, and whether the algebra supplies any selection principle for it, belongs to the gauge-principle article and its planned companions.

5. **Time reversal and antiunitary symmetries.** The S-matrix is unitary; the discrete spacetime symmetries include antiunitary ones, and their biquaternion realization — involving complex conjugation of $\mathbb{B}$ — is not treated here. It belongs to the planned companions on CPT and on the discrete symmetries, and nothing is claimed.

6. **The field S-matrix as a functional of the algebra.** Is there any sense in which the full field S-matrix is determined by a biquaternion-valued generating functional, even though it is not an element of $\mathbb{B}$? The parents leave the intrinsic $\mathbb{B}$-valued field and Lagrangian open; this article inherits that gap.

7. **Empirical content.** As with the rest of the framework, whether any of this yields a prediction distinguishing it from standard quantum field theory is the unanswered question. Nothing in the S-matrix construction changes that.

## Summary

The S-matrix in biquaternionic form has a small exact core and a large transcribed body. The core is finite-dimensional. Conditional on the Fock article's one-mode identification, the S-matrix of a single fermionic mode is an element of $\mathbb{B}$ that is **matrix-unitary**,

$$
\tilde S\tilde S^{*} = e_t,
$$

and matrix unitarity is *not* the biquaternion-norm condition $\tilde S\tilde S^{\natural} = e_t$: the first defines $\mathrm{U}(2)$, the second $SL(2,\mathbb{C})$, and they intersect in the spin rotations $SU(2)$. Every matrix-unitary biquaternion is $\exp(i\theta)\tilde u$ with $\tilde u$ a unit real quaternion, and a parity-conserving one-mode S-matrix is

$$
\tilde S = \exp(i\theta_0)\tilde\Pi_+ + \exp(i\theta_1)\tilde\Pi_-, \qquad \tilde\Pi_\pm = \tfrac12(e_t\pm i\vec e_z),
$$

whose biquaternion norm is the phase $\exp(i(\theta_0+\theta_1))$, generally not $e_t$. When the one-mode S-matrix is generated by a Hermitian $\tilde H \in \mathbb{M}_+$, $\tilde S = \exp(-i\tilde H\tau)$ and

$$
\langle\tilde S\rangle_{\natural} = \exp\!\left(-2i\tau\,\mathrm{Sc}(\tilde H)\right),
$$

so the biquaternion norm measures the trace of the generator while unitarity is independent of it. The transition probability is the Born rule applied to the unitary channel,

$$
P_{i\to f} = \mathrm{Tr}\!\left(\tilde\Pi_f\tilde S\tilde{Ϛ}_i\tilde S^{*}\right) = 2\,\mathrm{Sc}\!\left(\tilde\Pi_f\tilde S\tilde{Ϛ}_i\tilde S^{*}\right),
$$

checked against $|\langle f|\tilde S|i\rangle_{*}|^2$ on a spin rotation and on a mixed initial state.

The transcribed body is the interaction-picture Dyson series, its unitarity $S = 1+iT$ with $2\,\mathrm{Im}\,T = T^\dagger T$, the optical theorem, and the contraction of time-ordered products into Feynman propagators. The fermionic time-ordering sign and the $i\epsilon$ are inherited from the canonical quantization and propagator articles.

Two gaps remain. The field S-matrix is an operator on an infinite-dimensional Fock space and is not an element of $\mathbb{B}$: the algebra hosts one mode, and a second mode already requires $M_4(\mathbb{C})$. And the algebra names the complex plane and the axis of the $i\epsilon$ but does not select its orientation, which is the boundary condition that distinguishes the Feynman contour and defines the in/out splitting. As with the two parents, the biquaternion framework supplies notation, a finite-dimensional home, and the Born pairing — not a derivation of the scattering theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace (home of the rotation rotors) |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ | Centre of the algebra; home of the S-matrix's overall phase |
| $\tilde{\nabla}=e_t\partial/\partial Q_t+\vec e_k\partial/\partial Q_k$ | Biquaternionic gradient |
| $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}$ | d'Alembertian |
| $\mathsf{M}_2(\vec e_k)=-i\sigma_k$, $\mathsf{M}_2(i)=iI_2$ | Isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ |
| $\langle\tilde S\rangle_{\natural} = \langle\tilde S,\tilde S\rangle_{\natural}=\tilde S\tilde S^{\natural}=\sum_\mu S_\mu^2=\det\mathsf{M}_2(\tilde S)$ | Biquaternion norm; unit-norm (Lorentz-rotor) condition $\langle\tilde S\rangle_{\natural}=e_t$ |
| $\tilde S\tilde S^{\natural}=e_t$ | Unit-norm biquaternion $\Leftrightarrow SL(2,\mathbb{C})$ |
| $\tilde S\tilde S^{*}=e_t$ | Matrix-unitary biquaternion $\Leftrightarrow \mathrm{U}(2)$ |
| $\tilde S=\tilde A\tilde U$, $\tilde A=\sqrt{\tilde S\tilde S^{*}}$ | Cartan pairing of the S-matrix; $\tilde A=e_t$ exactly when $\tilde S\tilde S^{*}=e_t$ |
| $\tilde u\in\mathbb{H}_{\mathbb{B}}$, $\tilde u\tilde u^{\natural}=e_t$ | Unit real quaternion $\Leftrightarrow SU(2)$; spin rotation |
| $\psi$, $\bar\psi=\psi^\dagger\gamma^0$ | Spinor-module representative and its adjoint |
| $g=\mathrm{diag}(+1,-1,-1,-1)$, $\eta=-g$ | Clifford and $ict'$ metrics |
| $\not p=\gamma^0E-\boldsymbol{\gamma}\cdot\vec p$ | Feynman slash |
| $a^{\mathrm{fop}}_r(\vec p),b^{\mathrm{fop}}_r(\vec p)$ | Particle and antiparticle mode operators (parent's notation) |
| $\mathcal{H}_I$, $H_I$ | Interaction Hamiltonian density and Hamiltonian |
| $S=T\exp(-i\int d^4x\,\mathcal{H}_I)$ | S-matrix; time-ordered exponential (Dyson series) |
| $S=1+iT$ | Forward plus transition splitting |
| $2\,\mathrm{Im}\,T=T^\dagger T$ | Unitarity relation (optical theorem) |
| $w^{(r)},v^{(r)}$, $S_F$ | Plane-wave spinors and Feynman propagator (propagator article) |
| $\tilde P\tilde P^{\natural}=-m^2c^2$ | Biquaternion mass shell (external legs) |
| $\vec\Upsilon_x,\vec\Upsilon_y,\tilde\Pi_-$ | Single-mode ladder and number operators |
| $(-1)^F=i\vec e_z$ | Fermion-parity grading (one mode) |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ | Occupation idempotents (vacuum, occupied) |
| $\tilde{Ϛ}_i$, $\tilde\Pi_f$ | Initial state and final idempotent in $\mathbb{M}_+$ |
| $\operatorname{Tr}(\tilde\Pi\tilde H^{*})=\operatorname{Tr}(\tilde\Pi\tilde H)=2\,\mathrm{Sc}(\tilde\Pi\tilde H^{*}) = 2\langle\tilde\Pi,\tilde H\rangle_{*}$ | Trace reading of the Hermitian form (Born rule) |
| $c$ | Speed of light, restored in the mass-shell relation |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_1,\tilde{Q}_1\rangle_{*}=\sum_\mu\lvert Q_{1\mu}\rvert^{2}$ |

## Further Reading

- John A. Wheeler, "On the Mathematical Description of Light Nuclei by the Method of Resonating Group Structure," *Physical Review* **52** (1937) 1107–1122, for the introduction of the scattering matrix.
- Werner Heisenberg, "Die 'beobachtbaren Größen' in der Theorie der Elementarteilchen," *Zeitschrift für Physik* **120** (1943) 513–538, for the S-matrix program.
- Freeman J. Dyson, "The S-Matrix in Quantum Electrodynamics," *Physical Review* **75** (1949) 1736–1755, for the time-ordered exponential and the equivalence of the interaction-picture and Heisenberg-picture formulations.
- Eugene P. Wigner, "Resonance Reactions and Anomalous Scattering," *Physical Review* **70** (1946) 15–33, for the unitarity of the collision matrix and the analytic structure of the S-matrix.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the Dyson series, Wick's theorem, and the reduction of S-matrix elements to Feynman diagrams.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the optical theorem and the unitarity relation.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the interaction picture, the S-matrix, and the LSZ reduction in the convention used here.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the derivation of the S-matrix from asymptotic states and the unitarity of the scattering operator.
- R. Haag, *Local Quantum Physics: Fields, Particles, Algebras* (Springer, 1996), for the algebraic setting in which the S-matrix is an operator and scattering states are constructed from local fields.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the matrix representation of the biquaternion algebra and the structure of $SL(2,\mathbb{C})$ and $SU(2)$.
- Companion articles: [Canonical Quantization of the Biquaternion Dirac Field](canonical-quantization-of-the-biquaternion-dirac-field.html); [The Feynman Propagator in Biquaternionic Form](the-feynman-propagator-in-biquaternionic-form.html); [Fock Space and Creation/Annihilation Operators in Biquaternionic Form](fock-space-and-creation-annihilation-operators-in-biquaternionic-form.html); [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html); [Canonical Quantization of the Biquaternion Maxwell Field](canonical-quantization-of-the-biquaternion-maxwell-field.html); [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html); [Quantum Physics in Biquaternionic Form](quantum-physics-in-biquaternionic-form.html); [The KMS Condition and the Biquaternion Framework](the-kms-condition-and-the-biquaternion-framework.html); [The Polar Decomposition and Its Three Pairings](the-polar-decomposition-and-its-three-pairings.html); [The Cartan Pairing, the Amplitude and the Operator-to-State Map](the-cartan-pairing-amplitude-and-the-operator-to-state-map.html); [The Generalized Polar Decomposition of a Biquaternion: Partial Isometries and the Null Cone](../articles_maths/the-general-polar-decomposition-of-a-biquaternion-partial-isometries-and-the-null-cone.html).
