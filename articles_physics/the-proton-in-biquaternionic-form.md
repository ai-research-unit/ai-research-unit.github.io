# __The Proton in Biquaternionic Form__

## Introduction

The proton is the stable charged baryon: spin-$\tfrac{1}{2}$, electric charge $+1$ in units of the elementary charge, mass $938.272$ MeV, and a composite of three quarks bound by the colour interaction. In the biquaternion framework of these articles it can be placed as a massive spin-$\tfrac{1}{2}$ Dirac field, and the purpose of this article is to separate, as the corpus's discipline requires, what the framework's own structure says about it from what is imported from standard physics.

The framework is a research programme, not a completed theory, and three of its existing results bear directly on any claim about the proton.

- **It has a non-abelian gauge construction inside the algebra** — a connection, a curvature containing the commutator term, the adjoint transformation law, the Bianchi identity and a gauge-invariant Yang–Mills density — built on the compact factor $\mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\}=\mathfrak{su}(2)$ of the material sector (*Non-Abelian Gauge Fields in Biquaternionic Form*).
- **It has a chirality structure on the Dirac module and a charge operator on that module**, $Q=q_LP_L+q_RP_R$, with the mass selection rule $q_L=q_R$: a massive Dirac field in the framework is vector-like (*Chiral Fermions in the Biquaternion Framework*).
- **It has no colour group, no confinement mechanism, and no quark content.** The compact algebra available inside $\mathbb{B}$ is at most $\mathfrak{u}(2)$ of real dimension $4$; every $\mathbb{B}$-module has even complex dimension, so no three-dimensional colour module exists within the present construction; and nothing in the series derives $SU(3)$ or a confinement mechanism (*Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda*).

The consequence for the proton is stated at the outset, because the article depends on it.

- **Representable, and checked below.** The proton can be placed in the framework as a massive spin-$\tfrac{1}{2}$ Dirac field. Its spin-$\tfrac{1}{2}$ representation content is the unique simple module of $\mathbb{B}\cong M_2(\mathbb{C})$; its electric charge is the eigenvalue of the module charge operator; and, being massive, it is necessarily vector-like on the module. The value $+1$ is a value the operator carries, and this is verified explicitly.
- **Not derived.** Nothing in the algebra selects $q_p=+1$, relates it to the electron's charge $-1$, or makes it an integer. The free biquaternion Dirac equation contains no charge at all, so the proton and the neutron satisfy the *same* free equation and differ only in an inserted coupling. The charge value is a parameter, exactly as the electron's charge is a parameter.
- **Outside the framework.** The proton's compositeness — its quark content, its colour, its binding, its anomalous magnetic moment, and the fact that it is a bound state at all — is not in the framework. These are standard-physics imports, and the QCD agenda records that the framework has no route to them.

This is a deliberately modest accounting, and it is the honest one. The sharpest test the proton offers is its charge: the framework's charge operator must give $+1$ for the proton where the corresponding operator gives $0$ for the neutron. The operator carries both values, and that is a genuine, checkable statement about its spectrum; but the *selection* of $+1$ and $0$ is not a framework result. The negative half of that sentence is the more useful one, and it is stated plainly rather than smoothed over with a derivation the algebra does not supply.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$ and $e_1e_2=e_3$, and $i$ is the scalar imaginary, $i^2=-1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector), with $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$; $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$ is the complex scalar subspace, which is the center of the algebra. The biquaternionic gradient is $\tilde{\nabla}=e_0\partial_{ict}+e_1\partial_x+e_2\partial_y+e_3\partial_z$, its quaternion conjugate is $\bar{\tilde{\nabla}}=e_0\partial_{ict}-e_1\partial_x-e_2\partial_y-e_3\partial_z$, and $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\bar{\tilde{\nabla}}\tilde{\nabla}$. The abelian potential and field strength are $\tilde{A}=i\phi/c\,e_0+\mathbf{A}$ and $\tilde{F}=i\sqrt{\epsilon}\,\mathbf{E}-\sqrt{\mu}\,\mathbf{H}$. Throughout, $c=1/\sqrt{\epsilon\mu}$ is the **speed of light in the medium** and $c_0$ the vacuum speed of light. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged. The matrix realization is $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ with $\Phi(e_0)=I_2$, $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$; the spinor module is $S=\mathbb{C}^2$, the unique simple left $\mathbb{B}$-module, carrying the left-handed Weyl representation $(\tfrac12,0)$, and $\bar{S}=(0,\tfrac12)$ is its conjugate; the Dirac module is $\Delta=S\oplus\bar{S}$, $\dim_\mathbb{C}\Delta=4$.

## The Proton as a Spin-$\tfrac{1}{2}$ Biquaternion Dirac Field

The proton enters the framework the way any massive spin-$\tfrac12$ fermion does: as a biquaternion field $\tilde{\Psi}$ satisfying the biquaternion Dirac equation

$$
\tilde{\nabla}\tilde{\Psi}_R=m_p\,\tilde{\Psi}_L,
\qquad
\bar{\tilde{\nabla}}\tilde{\Psi}_L=m_p\,\tilde{\Psi}_R,
$$

or, equivalently, as a field $\Psi\in\Delta$ in the spinor module satisfying the standard Dirac equation. In this section we record what is structural about placing it there and what is not.

**The spin-$\tfrac12$ representation content is forced once the field is placed in the module.** The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ has a unique simple module, of complex dimension $2$, and its group of unit-norm biquaternions is $SL(2,\mathbb{C})$, the double cover of the proper orthochronous Lorentz group. A field in $\Delta=S\oplus\bar{S}$ transforms in the two inequivalent two-component representations

$$
\Delta=\left(\tfrac12,0\right)\oplus\left(0,\tfrac12\right),
\qquad \dim_\mathbb{C}\Delta=4,
$$

so it carries spin $\tfrac12$, and a rotation by $2\pi$ acts as $-e_0$ on the module while acting as $+e_0$ on the four-vectors of $\mathbb{M}_-$. The half-integral, double-valued character of the proton's spin is therefore a representation-theoretic consequence of where the field lives, and *not* of anything proton-specific. What the framework does **not** derive is why this composite object has spin $\tfrac12$: that is angular-momentum addition among constituents in standard physics, and the framework has no constituent structure to add. The correct statement is the conditional one — *if* the proton is modelled as a field in the module, its spin is $\tfrac12$.

**The mass term is structural; the mass value is not.** The proton mass appears exactly once, as the coefficient of the linear mass term $m_p$ that couples the two chiral halves, $\tilde{\nabla}\tilde{\Psi}_R=m_p\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L=m_p\tilde{\Psi}_R$; it is the only mass term in the free equation. The algebra's real structure $\flat=-\dagger$ is a different object: for $\tilde{\Psi}=\tilde{\Psi}_++\tilde{\Psi}_-$ with $\tilde{\Psi}_\pm\in\mathbb{M}_\pm$ one has $\tilde{\Psi}^{\flat}=-\tilde{\Psi}_++\tilde{\Psi}_-$, so $\flat$ acts as $+1$ on the material part and $-1$ on the informational part.

The value $m_p=938.272$ MeV, or $1.6726\times10^{-27}$ kg, is not a consequence of the algebra or of the equation. It is a parameter, and the framework is scale-free until it is supplied. Equivalently, the free proton field carries the mass-shell relation

$$
\tilde{P}=m_p\tilde{U},
\qquad
\tilde{P}\bar{\tilde{P}}=-m_p^2c^2,
$$

in the corpus's four-momentum convention $\tilde{P}=iE/c\,e_0+\mathbf{p}$: the *form* of the mass shell is structural, the number in it is an import.

**The free equation contains no charge.** Neither the linear chiral mass pair $\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L=m\tilde{\Psi}_R$ nor the standard Dirac equation it transcribes contains a coupling.

Charge enters only when the field is coupled to a four-potential, through minimal substitution. Two immediate consequences follow and they are the theme of the next section. First, the proton and the neutron satisfy the same free equation with the same operator; whatever distinguishes them is an inserted coupling and not a structure of the equation. Second, the framework's ability to state the proton's charge is the ability of its charge operator to *carry* the value $+1$, not an ability to produce it.

## The Charge Operator on the Dirac Module

The framework's charge operator is the module operator of *Chiral Fermions in the Biquaternion Framework*,

$$
Q=q_LP_L+q_RP_R,
\qquad
P_L=\tfrac12\left(I_4-\gamma_5\right),\quad P_R=\tfrac12\left(I_4+\gamma_5\right),
\qquad \gamma_5=\mathrm{diag}(-I_2,I_2),
$$

with $P_L,P_R$ the chiral projectors on $\Delta$ and $q_L,q_R$ real parameters. The covariant derivative is $D_\mu=\partial_\mu+\tfrac{i}{\hbar}A_\mu Q$, and the framework's own abelian gauge structure — the one drawn from the central line $\mathbb{C}_{\mathbb{B}}$ — is the specialization in which the action is vector-like.

Two structural facts about $Q$ are inherited from the chiral-fermion article and are used here. First, $Q$ is Hermitian and diagonal in the chiral basis,

$$
Q=\frac{q_L+q_R}{2}I_4+\frac{q_R-q_L}{2}\gamma_5,
\qquad
[\,Q,\gamma_5\,]=0,
$$

with spectrum $\{q_L\ (\text{twice}),\,q_R\ (\text{twice})\}$. Second, the **mass selection rule**: the Dirac bilinear $\bar{\Psi}\Psi=\psi_L^{\dagger}\psi_R+\psi_R^{\dagger}\psi_L$ acquires the position-dependent phase $e^{\frac{i}{\hbar}(q_R-q_L)\Gamma}$ under a gauge transformation, so it is gauge invariant for all $\Gamma$ **if and only if** $q_R=q_L$. A framework fermion that carries a mass is therefore *forced* to be vector-like, and its charge operator collapses to a multiple of the identity,

$$
q_L=q_R=q
\quad\Longrightarrow\quad
Q=q\,I_4 .
$$

This much is a derivation: the mass term of the framework and the charge operator of the framework are not independent, and for the proton — which is massive — they force the vector-like form. It is the structural reason a colour interaction, which is vector-like, sits comfortably with massive baryons, just as the QCD agenda records. One qualification belongs to the step: the selection rule is a statement about the Dirac mass bilinear, and the parent's mass term is precisely that — the linear chiral pair — so the vector-like forcing follows directly. The open real-form question of the chiral-fermion article concerns a separate conjugate pairing built on the algebra's real structure $\flat$, a neutral-fermion coupling that does not enter the charged proton's Dirac mass; it is carried into the open questions below.

**The check on the values $+1$ and $0$.** The proton's charge is $+1$ and the neutron's is $0$, in units of the elementary charge. Substituting the two assignments into the operator gives

$$
Q_p=Q\big|_{q=+1}=I_4,
\qquad
Q_n=Q\big|_{q=0}=0,
$$

with spectra $\{+1\ (\text{multiplicity }4)\}$ and $\{0\ (\text{multiplicity }4)\}$ respectively. Each is Hermitian, each commutes with $\gamma_5$, each is a multiple of the identity (hence vector-like, hence compatible with the mass selection rule), and the two are distinct. This was recomputed exactly in the faithful representation $\Phi(e_k)=-i\sigma_k$, together with the projector algebra ($P_L^2=P_L$, $P_R^2=P_R$, $P_LP_R=0$, $P_L+P_R=I_4$) and the selection rule on both branches (the vector-like branch $q_L=q_R$ and the axial branch $q_R=-q_L$). So the operator *carries* the proton's $+1$; the value is an eigenvalue the framework's charge operator has.

**The honest qualification.** Carrying a value is not selecting it. The eigenvalue $q$ is a free real parameter of the framework; nothing in $\mathbb{B}$, in the Dirac equation, or in the gauge principle fixes it to $+1$ for the proton, to $0$ for the neutron, or to any integer at all. The framework does not relate $q_p$ to the electron's $q_e$, so the equality of their magnitudes and the opposite signs — a striking and measured fact about the world — are not framework results; the electron article records the same absence for the electron. Nor does the framework explain why the proton's charge is an integer while a hypothetical fractionally charged constituent would not be; charge quantisation is not derived anywhere in the series. And the framework cannot *distinguish* the proton's field from the neutron's: the two are the same kind of object in the unique simple module, differing only in the value of an inserted coupling, exactly as the electron and muon are the same kind of object differing only in mass. In short, the sharpest test the proton offers is passed as a statement about the operator's spectrum and failed as a derivation. That is the result, and it is a negative one about derivation.

## Which Generator Carries the Electric Charge

The charge operator must not be silently identified with a Lie-algebra generator without saying which; here the answer is definite, and it is itself a checkable structural result.

The framework's abelian gauge group is the unitary part of the center,

$$
U(1)\subset\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\},
\qquad
U(1)=\{e^{i\theta}\},
$$

and the infinitesimal generator of the gauge transformation is the central element $ie_0\in\mathbb{M}_-$. On the module, the corresponding Hermitian charge operator is a multiple of the identity, $Q=qI_4$, whose unit generator is the central Hermitian element $e_0$ ($\Phi(e_0)=I_2$), up to the sign convention that relates an anti-Hermitian algebra element to its Hermitian observable. The electric charge is therefore carried by the **abelian factor** of the algebra — the central line — and not by the non-abelian factor.

The non-abelian factor cannot be the electric charge, and this is checked, not asserted. The generators of the compact factor are $T_a=\tfrac12e_a$; they are anti-Hermitian, and in the faithful representation

$$
\Phi(T_a)=-\tfrac{i}{2}\sigma_a,
\qquad
\text{eigenvalues } \pm \tfrac{i}{2}\ \ (\text{purely imaginary}).
$$

A charge operator is an observable: it must be Hermitian with real eigenvalues. The $T_a$ fail the first condition and have imaginary spectra, so no $\mathfrak{su}(2)$ generator in $\mathbb{M}_-$ can be the electric charge. Their Hermitian partners are the isospin-like generators $iT_a=\tfrac12 ie_a\in\mathbb{M}_+$, with

$$
\Phi(iT_a)=\tfrac12\sigma_a,
\qquad
\text{eigenvalues } \pm\tfrac12,
$$

which are Hermitian but have *half-integer* spectra; they cannot carry the proton's integer charge $+1$ either. All three $T_a$ and all three $iT_a$ were checked in the faithful representation. The conclusion is sharp: the proton's electric charge lives on the central $U(1)$, the $\mathfrak{su}(2)$ generators are a different set of quantum numbers, and identifying the two would be an error the framework's own spectrum forbids.

Three further distinctions belong here, because the framework has several conserved-looking quantities and they are easy to conflate.

- **Electric charge versus chirality.** The operator $Q$ is diagonal in the chiral basis and commutes with $\gamma_5$ for every $q_L,q_R$; the axial combination $q_R=-q_L$ is $Q=\tfrac{q_R-q_L}{2}\gamma_5$, proportional to the chirality operator. But $\gamma_5$ is a chirality label, not an electric charge, and the axial assignment is precisely one that fails the mass selection rule. For the massive proton only the vector-like specialization survives, and it is blind to chirality.
- **Electric charge versus the $\mathfrak{su}(2)$ generators.** As above, these are real-spectrum (after multiplication by $i$) but half-integer-valued; they are isospin-like, not electric.
- **Electric charge versus baryon number.** The framework supplies no baryon-number current, no conserved fermion number beyond the central phase, and no composite quantum number at all. The framework's own mass term is the linear chiral pair, through which the continuous central phase passes, so the proton's electric charge is conserved by the massive free equation; what remains open is a separate conjugate pairing built on the algebra's real structure $\flat$, the real-form question of the chiral-fermion article. The framework still does not supply baryon number, and that gap is inherited, not resolved here.

## What the Framework Does Not Supply: Compositeness and Colour

The proton is not an elementary field in nature; it is a bound state. Nothing in the biquaternion framework represents that, and the omission is not a gap with a known route.

**No colour group.** The compact algebra available inside $\mathbb{B}$ is the maximal compact subalgebra of $\mathfrak{gl}(2,\mathbb{C})$, namely $\mathfrak{u}(2)=\mathfrak{u}(1)\oplus\mathfrak{su}(2)$, of real dimension $4$; a $\mathfrak{su}(3)$ of dimension $8$ does not embed in it. The matter side has the matching ceiling: $\mathbb{B}\cong M_2(\mathbb{C})$ is simple, its unique simple module is $\mathbb{C}^2$, every $\mathbb{B}$-module is a direct sum of copies of it, and therefore every module has even complex dimension, so a three-dimensional colour module does not exist. (This was spot-checked: a minimal left ideal $\mathbb{B}p$ has complex dimension $2$, and the anti-Hermitian $2\times2$ matrices span a real four-dimensional space.) The framework has no colour triplet and no gluon octet.

**No confinement.** There is no Wilson loop, no area law, no string tension, no mass gap, and no gauge-fixing principle in the series, and the QCD agenda classifies confinement as an obstacle with no route yet. The zero-divisor cone of $\mathbb{M}_-$ is not an area law.

**No quark content.** Nothing derives a quark, a flavour, or a fractional charge. The identification "proton $=uud$" is standard physics, and the framework can only transcribe the phrase. Since the framework cannot even host a three-dimensional internal module, it cannot host the triplet in which a quark would sit.

**No bound-state structure.** The framework has no two-body or many-body bound-state formalism on which a baryon could be built, and no action, measure or gauge-invariant regulator of the kind the QCD agenda names as prerequisites. The proton must therefore be represented as an *effective* elementary spin-$\tfrac12$ field, with all composite physics absorbed into imported parameters.

The consequence is that the proton's compositeness — the reason its mass is 938 MeV rather than a Lagrangian parameter, the reason its magnetic moment is not the Dirac value, and the reason its charge is an integer — is entirely outside the framework. The framework can describe the effective proton; it cannot explain why there is one.

## Spin, Statistics and the Magnetic Moment

**Spin.** The spin-$\tfrac12$ representation content is derived conditionally, as in the first section: it follows from the module, not from any proton-specific structure. The spin-statistics theorem is transcribed rather than derived (*The Spin–Statistics Theorem in Biquaternionic Form*), but the framework does identify the half-integer representations as native to the module, on which $-e_0$ acts as $-\mathrm{id}$, while the integer-spin representations descend to the Lorentz group. The proton, placed in the module, is a fermion for exactly the same structural reason as the electron; the framework does not derive that this particular composite is a fermion.

**The magnetic moment.** Carrying the biquaternion Dirac equation to the non-relativistic regime produces the tree-level gyromagnetic factor $g=2$ for any structureless spin-$\tfrac12$ field with the inserted charge, exactly as for the electron (*The Electron in Biquaternionic Form*). Applied to the proton's effective field this gives a magnetic moment $\boldsymbol{\mu}_p=(e\,q_p/m_p)\mathbf{S}$ with $q_p=+1$, of one nuclear magneton $\mu_N=e\hbar/2m_p$ when $\mathbf{S}$ is aligned with the field. The measured proton moment is $2.7928\,\mu_N$, i.e. $g_p\approx5.586$. The deviation is *not* a small radiative correction of the kind the electron's $g-2$ is: it is a large strong-interaction and compositeness effect, produced by the quark and gluon dynamics of the bound state, and the framework supplies none of it. For the proton, therefore, even the tree-level value is not a prediction about the real object — it is the value the framework would assign to a fictitious elementary field of the same mass and charge.

## What Is Imported from Standard Physics

The table sorts the proton's properties by the status they have in the framework, in the manner of the electron article.

| Property of the proton | Status in the framework | Where it comes from |
|---|---|---|
| Spin-$\tfrac12$ representation content | Represented (forced once modelled) | unique simple module of $\mathbb{B}\cong M_2(\mathbb{C})$ |
| Spin states, observables, Born rule | Derived | idempotents of $\mathbb{M}_+$; $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ |
| Mass term is off-diagonal in chirality; real structure acts $+1/-1$ on $\mathbb{M}_\mp$ | Derived | linear chiral pair; $\tilde{\Psi}^{\flat}=-\tilde{\Psi}_++\tilde{\Psi}_-$; Weyl decomposition |
| Vector-like charge operator $Q=qI_4$ for a massive field | Derived | mass selection rule $q_L=q_R$ |
| Conserved current $\tilde{J}\in\mathbb{M}_-$ | Derived | Dirac current $j^\mu=\bar{\psi}\gamma^\mu\psi$ |
| Electric charge generator is the central $U(1)$ | Derived | $\mathbb{C}_{\mathbb{B}}$ central; $\mathfrak{su}(2)$ generators have imaginary/half-integer spectra |
| Charge value $q_p=+1$ | Represented (parameter) | inserted coupling; not selected by the algebra |
| $|q_p|=|q_e|$, opposite signs | Outside | no framework structure; independent parameters |
| Charge quantisation (integrality) | Outside | not derived in the framework |
| Mass value $m_p$ | Represented (parameter) | inserted into the Dirac equation |
| Compositeness; quark content $uud$; colour; confinement | Outside | standard QCD; no route in the framework |
| Anomalous magnetic moment $g_p\approx5.586$ | Outside | strong-interaction / composite dynamics |
| Baryon number | Outside | not constructed |
| Conservation of the charge under the framework's own mass | Derived | linear chiral pair passes the continuous central phase; the real structure's separate pairing is the open reading |
| Empirical contact | Outside | no prediction distinguishing the framework from standard physics |

## Open Questions

1. **Is the charge value derivable at all?** The framework's charge operator carries $+1$ for the proton and $0$ for the neutron, but no principle of the algebra selects those values. Is there a framework-internal quantisation condition — an anomaly, a topological constraint, or a compactness condition on the central $U(1)$ — that would fix $q$ to integers, or to the specific integer $+1$ for the proton? None is known, and none is proposed here.

2. **Is there any relation between $q_p$ and $q_e$?** The measured equality $|q_p|=|q_e|$ and the opposite signs are not explained. In the framework the proton and electron are independent fields in the same module, with independent couplings; nothing ties them.

3. **Which generator, in the end?** This article shows that the electric charge must be the central $U(1)$ generator, because the $\mathfrak{su}(2)$ generators and their Hermitian partners have imaginary and half-integer spectra. Is that identification forced, or could an enlarged carrier host a different Hermitian generator with integer spectrum that also plays the role of electric charge? The ceiling result of the QCD agenda suggests not within $\mathbb{B}$, but the enlarged-carrier question is open.

4. **Can the framework host a bound state?** The proton's compositeness is entirely imported because the framework has no bound-state formalism and no colour. A biquaternionic bound-state construction — if one could be built on the carrier the QCD agenda says is missing — is the only route by which compositeness could enter. No route yet.

5. **Does the framework's own mass violate the charge it relies on?** No: the framework's mass term is the linear chiral pair, through which the continuous central phase passes, so the massive free equation conserves the proton's charge. The reading the chiral-fermion article leaves open concerns a separate conjugate pairing on the algebra's real structure $\flat$, a neutral-fermion coupling that does not enter the charged proton's mass. The live question is therefore whether that separate pairing exists physically, not whether the proton's charge survives its own mass.

6. **Baryon number.** Nothing in the framework distinguishes the proton's conserved fermion number from the electron's. Is there any framework object that could carry baryon number, given that the algebra's abelian charge is the electromagnetic-type $U(1)$ and no composite quantum number is constructed?

7. **Empirical contact.** As everywhere in the framework, the unresolved question is whether any of this yields a prediction distinguishing it from standard physics. The construction above is a reformulation, and a reformulation that must import the proton's mass, charge and compositeness has no prospect of doing so.

## Summary

The proton can be placed in the biquaternion framework as a massive spin-$\tfrac12$ Dirac field, $\tilde{\nabla}\tilde{\Psi}_R=m_p\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L=m_p\tilde{\Psi}_R$, and the framework makes three structural statements about it. The spin-$\tfrac12$ representation content follows from the unique simple module of $\mathbb{B}\cong M_2(\mathbb{C})$; the mass term is the chirality-mixing linear pair of the two chiral halves; and, being massive,

the proton is forced by the mass selection rule $q_L=q_R$ to be vector-like, so the general charge operator $Q=q_LP_L+q_RP_R$ on the Dirac module collapses to

$$
Q=q_p\,I_4,
$$

with the central $U(1)$ of $\mathbb{C}_{\mathbb{B}}$ as its generator.

On the sharpest available test, the framework's charge operator gives $+1$ for the proton and $0$ for the neutron as exact eigenvalues: $Q_p=I_4$, spectrum $\{+1\}$, and $Q_n=0$, spectrum $\{0\}$, both Hermitian, both chirality-blind, both compatible with the mass selection rule. This was verified exactly in the faithful representation, together with the projector algebra and the selection rule on the vector-like and axial branches. But the *selection* of the values is not a framework result: $q$ is a free parameter, nothing fixes it to $+1$ or to an integer, nothing relates $q_p$ to the electron's charge, and the free equation contains no charge at all. The test is therefore passed as a statement about the operator's spectrum and failed as a derivation — a negative result, stated plainly.

It was also shown that the electric charge cannot be carried by the non-abelian factor: the $\mathfrak{su}(2)$ generators $T_a=\tfrac12e_a$ have purely imaginary spectra $\pm\tfrac i2$, and their Hermitian partners $iT_a$ have half-integer spectra $\pm\tfrac12$, so neither can be the proton's integer electric charge. The charge lives on the central line $\mathbb{C}_{\mathbb{B}}$. This settles the "which generator" question within the present construction.

What the framework does not supply is everything that makes the proton a proton. There is no colour group — the compact algebra inside $\mathbb{B}$ is at most $\mathfrak{u}(2)$ of dimension $4$, and every $\mathbb{B}$-module has even complex dimension, so no colour triplet exists. There is no confinement mechanism, no colour representation, no quark content, no bound-state formalism, and no baryon number. The proton's mass $938.272$ MeV, its charge $+1$, the equality of its charge magnitude with the electron's, the integrality of that charge, its quark content, and its anomalous magnetic moment $g_p\approx5.586$ are all imports from standard physics. The framework represents an effective elementary proton; it does not derive one, and it cannot explain why the effective object exists.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_1e_2 = e_3$ |
| $i$ | Scalar imaginary, $i^2 = -1$, central |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ | Center of the algebra; abelian (electric-charge) factor |
| $\tilde{\nabla} = e_0\partial_{ict} + e_k\partial_k$ | Biquaternionic gradient (Dirac operator) |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$ | d'Alembertian |
| $\Phi:\mathbb{B}\to M_2(\mathbb{C})$, $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$ | Faithful matrix representation used in the checks |
| $S=\mathbb{C}^2=(\tfrac12,0)$ | Unique simple left $\mathbb{B}$-module (left-handed Weyl) |
| $\bar{S}=(0,\tfrac12)$ | Conjugate right-handed Weyl module |
| $\Delta=S\oplus\bar{S}$ | Dirac spinor module, $\dim_\mathbb{C}\Delta=4$ |
| $\tilde{\Psi}$, $\tilde{\Psi}^{\flat}=-\tilde{\Psi}^{\dagger}$ | Biquaternion Dirac field and anti-Hermitian conjugate |
| $m_p$ | Proton mass (a parameter) |
| $\gamma_5=\mathrm{diag}(-I_2,I_2)$ | Chirality operator, $\gamma_5^2=I_4$ |
| $P_L=\tfrac12(I_4-\gamma_5)$, $P_R=\tfrac12(I_4+\gamma_5)$ | Chiral projectors |
| $Q=q_LP_L+q_RP_R$ | Charge operator on $\Delta$ |
| $q_L, q_R$ | Chiral couplings (real parameters); massive field forces $q_L=q_R$ |
| $q_p=+1$ | Proton charge eigenvalue (inserted, not derived) |
| $q_L=q_R \Rightarrow Q=qI_4$ | Vector-like specialization forced by the mass selection rule |
| $T_a=\tfrac12 e_a$ | Generators of $\mathfrak{su}(2)=\mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\}\subset\mathbb{M}_-$ |
| $\Phi(T_a)=-\tfrac i2\sigma_a$, $\Phi(iT_a)=\tfrac12\sigma_a$ | Imaginary and half-integer spectra; neither is the electric charge |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Inherited informational trace formula |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- *Chiral Fermions in the Biquaternion Framework* — the charge operator $Q=q_LP_L+q_RP_R$ on the Dirac module, the mass selection rule $q_L=q_R$, and the real-structure question that the separate pairing poses.

- *The Dirac Equation in Biquaternionic Form* — the biquaternion Dirac equation in its linear chiral-pair form, the spinor module, the mass term, and the mass-shell relation used here.

- *Non-Abelian Gauge Fields in Biquaternionic Form* — the $\mathfrak{su}(2)$ generators $T_a=\tfrac12e_a$, their spectra, and the compact factor of the material sector whose distinction from the charge generator this article checks.
- *Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda* — the ceiling on the compact gauge algebra, the absence of a colour triplet and of confinement, and the three-way classification of what the framework reaches and what it does not.
- *The Electron in Biquaternionic Form* — the sibling accounting, in which charge and mass are likewise parameters, and the statement that nothing in the algebra fixes $|q_e|=|q_p|$.
- *The Spin–Statistics Theorem in Biquaternionic Form* — half-integer representations as native to the module, and the sense in which the spin–statistics theorem is transcribed rather than derived.
- *The Spinor Module in Biquaternionic Form and Its Lorentz Action* — the module $\Delta=S\oplus\bar{S}$ and the Lorentz action that fixes the spin-$\tfrac12$ representation content.
- *The Gauge Principle in Biquaternionic Form* — the abelian gauge group as the unitary part of the center, on which the electric-charge identification rests.
- *Angular Momentum and Spin in Biquaternionic Form* — the spin operators $\tilde{S}_k=\tfrac\hbar2 ie_k$ and the idempotent state structure used implicitly here.
- *The Neutrino and Majorana Fermions in Biquaternionic Form* — the real structure and the Majorana-versus-Dirac reading that bears on charge conservation.

- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* and *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* — the two sectors, their bases and the trace formula inherited unchanged.
- *Introduction to the Biquaternion Universe* — the algebra, the conjugations and the sector split in which the whole construction is set.
