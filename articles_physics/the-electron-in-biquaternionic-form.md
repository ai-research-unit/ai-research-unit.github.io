# __The Electron in Biquaternionic Form__

## Introduction

The electron is the object on which the relativistic quantum theory of this series is calibrated. It is the particle of Dirac's 1928 equation, the spin-$\tfrac{1}{2}$ system whose magnetic moment is measured to twelve significant figures, and the fermion whose two chiral halves the Standard Model treats differently. In the biquaternion framework of these articles the electron is the standard realization of the **biquaternion Dirac field** $\tilde{\Psi}$: an element of $\mathbb{B}$, equivalently a field in the spinor module on which $\mathbb{B}\cong M_2(\mathbb{C})$ acts, satisfying the linear, chirality-off-diagonal pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R,
$$

with $m = m_e$ the electron mass and massless limit $\tilde{\nabla}\tilde{\Psi} = 0$. Each chiral component satisfies the Klein–Gordon equation $(\Box - m^2c^2/\hbar^2)\tilde{\Psi} = 0$. The anti-Hermitian conjugation $\tilde{\Psi}^\flat = -\tilde{\Psi}^\dagger$ is the algebra's real structure, not the mass term.

A framework that reformulates known physics can be read in two very different ways. Read generously, every correct statement about the electron becomes a statement the framework "contains"; read carefully, most of those statements are properties of the Dirac equation that the framework merely transcribes, and the specific numbers attached to the electron must be inserted by hand. This article takes the second reading and asks a single question: **which properties of the electron are consequences of the biquaternion structure, which are consequences of the Dirac equation the framework contains, which are parameters inserted from outside, and which lie outside the framework altogether?**

The answer, stated plainly at the outset, is the following. The framework *forces* the electron's spin-$\tfrac{1}{2}$ representation content and its tree-level gyromagnetic factor $g=2$; it *contains* the chirality decomposition, the mass term as the linear coupler of the two chiralities (the algebra's two central ideals), and the Zitterbewegung with its scale; it *inserts* the mass $m_e$, the charge $e$, and the unit $\hbar$; and it does *not* contain the anomalous magnetic moment, the weak chiral coupling, or a derivation of the mass or charge values. The electron is not an element of either subspace $\mathbb{M}_\pm$: its spin state, its current, and its Coulomb field are distributed across both, the operation that exchanges the two subspaces is the central $i$ (the rest-energy phase), and the algebra's real structure $\flat = -\dagger$ acts on them with opposite signs, while the mass term couples the two chiralities.

A second, less comfortable point belongs in the introduction. Almost every statement the framework makes about "the electron" is a statement about a general structureless spin-$\tfrac{1}{2}$ field. The algebra does not single the electron out. Its mass, its charge, and the identity of its antiparticle are the inputs that make the general field into *this* field.

## The Electron as a Biquaternion Field

The notation is that of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, scalar imaginary $i$, and biquaternionic gradient

$$
\tilde{\nabla} = e_0\,\partial_{ict} + e_1\,\partial_x + e_2\,\partial_y + e_3\,\partial_z.
$$

Hermitian conjugation $\tilde{Q}^\dagger = \bar{\tilde{Q}}^{*}$ defines the two sectors by their fixed points,

$$
\mathbb{M}_- = \{\tilde{Q} : \tilde{Q}^\dagger = -\tilde{Q}\}, \qquad
\mathbb{M}_+ = \{\tilde{Q} : \tilde{Q}^\dagger = \tilde{Q}\}, \qquad
\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-,
$$

with $\mathbb{H}_{\mathbb{B}}$ the real quaternion subspace. The trace formula is $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$.

The electron field carries the electron's data in the following objects.

| Electron datum | Biquaternion object |
|---|---|
| The field | $\tilde{\Psi}\in\mathbb{B}$, equivalently a four-component Dirac spinor $\psi$ |
| Free equation | $\tilde{\nabla}\tilde{\Psi}_R = m_e\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m_e\tilde{\Psi}_R$ |
| Mass | the coefficient $m_e$ of the linear, chirality-off-diagonal mass pair |
| Charge | the coupling $q=-e$ inserted in the gradient (see below) |
| Spin state | an idempotent $\tilde{P}_+(\hat{\mathbf{n}}) = \tfrac{1}{2}(e_0 + i\hat{\mathbf{n}})\in\mathbb{M}_+$ |
| Spin observables | Hermitian elements $\tilde{H} = i\mathbf{h}\cdot\mathbf{e}\in\mathbb{M}_+$ |
| Conserved current | $\tilde{J} = ic\,j^0 e_0 + \mathbf{j}\in\mathbb{M}_-$ |
| Chiral halves | the left- and right-handed Weyl spinors of the spinor module |

The placement of these objects already contains the article's main structural observation: the electron's state-like data (its spin) and its field-strength-like data (its Coulomb field) are $\mathbb{M}_+$ objects, its current is an $\mathbb{M}_-$ object, the algebra's real structure $\flat$ acts on the two sectors with opposite signs while the mass term couples the two chiralities, and it is the rest-energy phase that rotates one sector into the other. There is no single sector of the algebra in which "the electron" lives.

## Mass: A Term the Framework Needs but Cannot Supply

The electron mass appears in the free equation as the coefficient of the linear, chirality-off-diagonal mass pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R .
$$

Three statements are worth separating: how the mass couples the two chiralities, how the algebra's real structure acts on the two sectors, and what phase the mass puts between the sectors.

**It mixes the chiralities.** The spinor module of the electron is the direct sum of the left-handed and right-handed Weyl halves — the two central ideals of $\mathbb{B}$ — and the mass term couples them: without it, the electron would be two independent massless Weyl fields. The electron's mass is therefore represented, in the framework, as a chirality-mixing term, and this is the structural origin, in the biquaternion reading, of the fact that a lone Weyl field cannot carry a mass. The coupling is necessarily off-diagonal: left multiplication preserves each central ideal, so no combination of the form $a\tilde{\Psi}_L + b\tilde{\Psi}_R$ relates them, and the mass is the off-diagonal pair above.

**The real structure acts on the two sectors with opposite signs.** For $\tilde{\Psi} = \tilde{\Psi}_+ + \tilde{\Psi}_-$ with $\tilde{\Psi}_\pm\in\mathbb{M}_\pm$ one has $\tilde{\Psi}_\pm^\dagger = \pm\tilde{\Psi}_\pm$, hence

$$
\tilde{\Psi}^\flat = -\tilde{\Psi}^\dagger = -\tilde{\Psi}_+ + \tilde{\Psi}_-,
$$

so $\flat$ acts as $-1$ on the $\mathbb{M}_+$ part and $+1$ on the $\mathbb{M}_-$ part. It **preserves** each sector and marks it with a sign: it is diagonal on the sector decomposition, not an exchange of the two sectors. This is a property of the algebra's real structure, not of the mass term: a coupling built on $\flat$ pairs the field with its conjugate — a Majorana-type mass $m\tilde{\Psi}^\flat$, whose central-phase plane waves sit on the spacelike locus — and it is not the electron's mass. The operation that exchanges the two sectors is multiplication by the central $i$, $i\mathbb{M}_\pm = \mathbb{M}_\mp$. Verified from the fixed-point definitions.

**It sets the rate at which the two sectors rotate into one another.** Factoring the rest energy out of a free plane wave gives

$$
e^{-imc^2t/\hbar} = \cos\!\Big(\frac{mc^2t}{\hbar}\Big)e_0 - \sin\!\Big(\frac{mc^2t}{\hbar}\Big)(ie_0),
$$

with $e_0\in\mathbb{M}_+$ and $ie_0\in\mathbb{M}_-$ (an imaginary scalar is anti-Hermitian). The rest-energy phase is central, and because $i\mathbb{M}_\pm = \mathbb{M}_\mp$ it is a rotation between the sectors at angular frequency $mc^2/\hbar$: it takes the $\mathbb{M}_+$ direction $e_0$ toward the $\mathbb{M}_-$ direction $ie_0$ and back. The mass sets this scale — the frequency is $mc^2/\hbar$ — through the mass shell. This is the sense in which the electron's mass, in the framework, *is* the rate of the rotation between the material and informational subspaces.

**What is not derived.** The value $m_e = 9.1093837015\times10^{-31}$ kg, or equivalently $m_ec^2 = 0.510998950$ MeV, is not a consequence of the algebra or of the equation; it is a parameter. The framework is scale-free until $m_e$ is supplied, and every electron scale below — the Compton length, the Zitterbewegung frequency — is set by the supplied value, not produced by the structure.

## Charge: A Coupling Constant in the Gradient

The free biquaternion Dirac equation contains no charge. Charge enters only through the coupling of the field to the four-potential $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}\in\mathbb{M}_-$. In the spinor-module form this is the minimal substitution $\hat{\mathbf{p}}\to\hat{\mathbf{p}} - q\mathbf{A}$, with $q$ the particle's charge; for the electron $q = -e$. The precise biquaternion form of this coupling is set out in the companion article *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*, which derives the coupled equation $D\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{D}\tilde{\Psi}_L = m\tilde{\Psi}_R$ and shows that it is exactly gauge covariant in the massive case as well as the massless one, the central phase passing through the linear mass pair; the charge is therefore *represented* in the framework, not derived by it.

Four statements are worth separating.

**The current is derived.** Given the equation, the Dirac current $j^\mu = \bar{\psi}\gamma^\mu\psi$ is conserved, and in the series' notation it is the four-vector biquaternion

$$
\tilde{J} = ic\,j^0 e_0 + \mathbf{j}\in\mathbb{M}_-, \qquad j^0 = \psi^\dagger\psi \ge 0 .
$$

That the electron's conserved current is a material-sector object is a structural consequence of the equation, not an added assumption.

**The value and sign of the charge are inserted.** Nothing in the algebra fixes $e$, explains why charge is quantised, or explains why the electron and the proton have equal and opposite charge. The equation with $q = -e$ and the equation with $q = +e$ are the same equation; the labelling of which branch is the electron is a convention. Charge conjugation makes this explicit: the equation admits a symmetry, generated by the matrix $C = i\gamma^2\gamma^0$ satisfying $C\gamma^{\mu T}C^{-1} = -\gamma^\mu$, under which the conserved current reverses sign and the two frequency branches are exchanged. Verified by direct computation of the $4\times4$ matrices. The framework represents both signs of charge on the same footing.

**The electron's Coulomb field is an $\mathbb{M}_+$ object.** For a point charge $q$ at rest the field-strength biquaternion is, from the companion article on Maxwell's equations,

$$
\tilde{F}(\mathbf{x}) = \frac{i\,q\,\hat{\mathbf{x}}}{4\pi\sqrt{\epsilon}\,\|\mathbf{x}\|^2},
$$

a purely imaginary vector, hence an element of the Hermitian subspace $\mathbb{M}_+$. The electron's charge shows itself, in the framework, through a field in the informational sector, while its current lies in the material sector. The two faces of the same charge sit in opposite halves of the algebra.

**What is derived once the coupling is inserted.** The minimal substitution yields the magnetic coupling with the coefficient $1/2m$, and hence the sign relation $\boldsymbol{\mu}_e = -(e/m_e)\mathbf{S}$: the electron's magnetic moment is anti-parallel to its spin because its charge is negative. The magnitude, however, is dimensional and carries $e$ and $\hbar$.

## Spin: Derived as a Representation, Normalised by Hand

The electron's spin is where the framework is strongest and where the distinction between derived and inserted is sharpest.

**Derived: the representation.** The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ has a unique irreducible module, of complex dimension two, and group of unit-norm biquaternions $SL(2,\mathbb{C})$, the double cover of the proper orthochronous Lorentz group. A field placed in that module transforms in the spinor representation $(\tfrac12,0)$: its spin is $\tfrac{1}{2}$, and a rotation by $2\pi$ acts as $-e_0$ on the spinor module while acting as $+e_0$ on the four-vectors of $\mathbb{M}_-$. The twofold, double-valued character of electron spin is therefore a representation-theoretic consequence of where the field lives, not an independent postulate. The spin rotations are the unit-norm biquaternions with real vector part, forming $SU(2)$.

**Derived: the state and observable structure.** On the dictionary used in the companion articles, the electron's spin state along a unit direction $\hat{\mathbf{n}}$ is represented by the idempotent $\tilde{P}_+(\hat{\mathbf{n}}) = \tfrac{1}{2}(e_0 + i\hat{\mathbf{n}})\in\mathbb{M}_+$, and its spin observables are the Hermitian elements $i\mathbf{h}\cdot\mathbf{e}\in\mathbb{M}_+$. (The companion articles leave the spinor-to-biquaternion dictionary as a convention; the state and observable structure below is what is checked, and it does not depend on which of the equivalent dictionaries is fixed.) The trace formula reproduces the spin-$\tfrac{1}{2}$ expectation values. For $\tilde{H} = i h_k e_k$ and $\tilde{P} = \tfrac{1}{2}(e_0 + i n_j e_j)$ one has $2\,\mathrm{Sc}(\tilde{P}\tilde{H}) = n_jh_j$; in particular $2\,\mathrm{Sc}\big(\tilde{P}_+(e_3)(ie_3)\big) = 1$ and $2\,\mathrm{Sc}\big(\tilde{P}_+(e_3)(ie_1)\big) = 0$, the correct values for the spin along $z$ and $x$. Recomputed directly.

**Inserted: the magnitude.** The spin operator is $\hat{S}_k = \tfrac{\hbar}{2}\sigma_k$, corresponding to $\tfrac{\hbar}{2}ie_k$. The factor $\hbar/2$ is a normalisation, not a prediction: the algebra fixes that spin is two-valued and that its observables close under $SU(2)$, but it does not fix the unit in which spin is measured. The number $\tfrac{1}{2}$ in "spin-$\tfrac{1}{2}$" is algebra; the number $\hbar$ is physics inserted from outside.

## The Dirac Description of the Electron

The electron's relativistic dynamics is the biquaternion Dirac equation and its spinor-module transcription, the standard Dirac equation

$$
(i\hbar\gamma^\mu\partial_\mu - m_ec)\psi = 0
$$

in the notation of the companion solutions article. Its plane-wave solutions come in two branches at each momentum, the positive-frequency $u^{(r)}(\mathbf{p})e^{-i(Et-\mathbf{p}\cdot\mathbf{x})}$ and the negative-frequency $v^{(r)}(\mathbf{p})e^{+i(Et-\mathbf{p}\cdot\mathbf{x})}$, with $E = +\sqrt{\mathbf{p}^2c^2 + m_e^2c^4}$ and $r$ the spin label; together they span a four-dimensional complex amplitude space, which is the four components of the Dirac spinor. The spin sums, normalisations, and bilinears are constructed in the companion solutions article and are not repeated here.

**A note on the wave biquaternion.** The mass-shell condition is written in the corpus convention, in which the four-wavevector has the imaginary time component of the $ict$ convention,

$$
\tilde{K} = i\,\frac{\omega}{c}\,e_0 + \mathbf{k}, \qquad
N(\tilde{K}) = \tilde{K}\bar{\tilde{K}} = -\frac{\omega^2}{c^2} + \mathbf{k}^2 = -\frac{m_e^2c^2}{\hbar^2},
$$

which is $E^2 = \mathbf{p}^2c^2 + m_e^2c^4$ under $E = \hbar\omega$, $\mathbf{p} = \hbar\mathbf{k}$. The parent Dirac article writes the wave biquaternion with a *real* time component in one paragraph and follows it with an "or equivalently" chain whose clauses are mutually inconsistent; that cluster is recorded as an open item in the parent's companion and is not reproduced here. The form above is the one used by the companion solutions article and the one consistent with the mass shell.

**Antiparticle.** The two frequency branches are exchanged by charge conjugation, and in the quantized reading the negative-frequency branch describes the positron. The framework represents the electron and the positron on the same algebraic footing; which branch is called the electron is fixed by the charge convention of the previous section, not by the algebra.

## Gyromagnetic Ratio: The One Quantitative Number the Equation Predicts

The Dirac description yields one celebrated number. Carrying the biquaternion Dirac equation to the non-relativistic regime — the computation is performed in the companion solutions article and its exercise — eliminates the small component and leaves the Pauli equation with the spin term

$$
-\frac{q\hbar}{2m_e}\,\boldsymbol{\sigma}\cdot\mathbf{B} \;\longleftrightarrow\; -\frac{q\hbar}{2m_e}\,i\,\mathbf{B} \in \mathbb{M}_+ .
$$

Writing the coupling as $-\boldsymbol{\mu}\cdot\mathbf{B}$ identifies $\boldsymbol{\mu} = (q/m_e)\mathbf{S}$ with $\mathbf{S} = \tfrac{\hbar}{2}\boldsymbol{\sigma}$, which is $\boldsymbol{\mu} = g\,(q/2m_e)\mathbf{S}$ with

$$
\boxed{\;g = 2\;}
$$

The coefficient $1/2m_e$ is produced by the elimination, not put in by hand: this is Dirac's tree-level prediction, here a property of the biquaternionic mass term. For the electron, $q = -e$, so

$$
\boldsymbol{\mu}_e = -\frac{e}{m_e}\mathbf{S} = -g\,\frac{e}{2m_e}\mathbf{S}, \qquad g = 2,
$$

of magnitude one Bohr magneton $\mu_B = e\hbar/2m_e = 9.274010\times10^{-24}$ J T$^{-1}$ when $\mathbf{S}$ is aligned with $\mathbf{B}$.

Two qualifications belong with the result. First, the derivation is the standard Dirac one, transcribed; the biquaternion form supplies the compact notation and the sector reading of the spin coupling as an $\mathbb{M}_+$ observable, not an independent derivation. Second, $g=2$ is not an electron-specific number: it holds for any structureless spin-$\tfrac{1}{2}$ field, so it distinguishes the electron from a spin-1 particle but not from a muon.

**Outside the framework: the anomaly.** The measured value is $g/2 = 1.00115965218$, i.e. $a = (g-2)/2 = 1.159652\times10^{-3}$, close to the one-loop Schwinger value $a \approx \alpha/2\pi = 1.161410\times10^{-3}$. This is a radiative correction of quantum electrodynamics; it lies outside the classical equation treated here, and the framework does not contain it. The tree-level $g=2$ is the whole of what the equation supplies.

## Zitterbewegung: The Scale of the Mass, Not a Signature of a Sector

The electron is the particle on which the Zitterbewegung was found. In the framework's own terms, the trembling is the interference of the two frequency branches, with angular frequency $2E/\hbar$ and amplitude of order $\hbar/(2mc)$. For the electron at rest these are

$$
\omega_Z = \frac{2m_ec^2}{\hbar} = 1.55269\times10^{21}\ \text{rad s}^{-1},
\qquad \frac{\hbar}{2m_ec} = 193.1\ \text{fm},
$$

half the reduced Compton wavelength $386.2$ fm. These are the standard values, reconfirmed numerically in the companion article on the Zitterbewegung.

The framework's temptation is to read the trembling as the observable face of the complexification — positive- and negative-energy components being the two sectors. The companion article tests that identification and refutes it: the energy-sign projector is built from $\beta = \gamma^0$, an *odd* Clifford element with no representative in $\mathbb{B}\cong\mathrm{Cl}^+_{1,3}$, while the sector projectors are built from Hermitian conjugation, internal to $\mathbb{B}$; the two splittings are also splittings of different objects (the spinor module and the algebra). What survives is a relation of scale and phase: at rest the trembling frequency is exactly twice the rest-energy sector-rotation frequency $m_ec^2/\hbar$, because the trembling phase is the square of the free-evolution phase. For the electron this means that its rest energy sets both the rate at which the sectors rotate into one another and the frequency of the trembling, without the trembling being an informational-sector effect.

## The Two Chiralities

The electron field is a Dirac spinor, and the spinor module decomposes into a left-handed and a right-handed Weyl half,

$$
\psi = \begin{pmatrix}\psi_L\\ \psi_R\end{pmatrix},
$$

each a two-component Weyl spinor. The decomposition is expressed by the chirality operator $\gamma_5$: it anticommutes with every generator, $\gamma_5\gamma^\mu = -\gamma^\mu\gamma_5$, and therefore commutes with every Clifford-even element, the biquaternion subalgebra among them. The massless equation splits into two independent Weyl equations, one per chirality; the mass term couples them, which is the same statement as the chirality-mixing of the mass section.

Two structural points and two cautions.

**Derived.** The two-chiral structure itself is a consequence of the spinor representation: the Dirac spinor is the direct sum of the two inequivalent two-component representations of $SL(2,\mathbb{C})$, and the mass term is the unique Lorentz-invariant coupling between them. For a massless electron, chirality coincides with helicity, so the two branches become two definite chiralities. This is a genuine structural consequence of the algebra and of the equation.

**Represented, not derived: the weak chiral coupling.** In the Standard Model the electron couples to the weak interaction through its left-handed component only. The framework contains the chirality decomposition, so it has the vocabulary for this, but it does not select the coupling: nothing in $\mathbb{B}$ or in the Dirac equation says that one chirality couples and the other does not. The $V-A$ structure is an input.

**Caution: the status of the chirality projectors.** Whether the projectors associated with chirality are to be read as objects inside $\mathbb{B}$ alone, or as central idempotents of the complexified algebra, depends on how the biquaternion imaginary is identified with the Clifford volume element — the two-$i$ point that the companion articles record. The parent Dirac article states the projectors as central idempotents of the complexified even algebra. This article therefore asserts the splitting of the equation and the commutation of $\gamma_5$ with the even subalgebra, which are verified, and does not assert a canonical embedding of the projectors in $\mathbb{B}$, which the corpus has not settled.

**Caution: chirality is not the same as the sector split.** The chiral decomposition is a decomposition of the spinor module by $\gamma_5$; the sector decomposition is a decomposition of the algebra by Hermitian conjugation. The Zitterbewegung article reaches the same distinction from the other side when it rejects the identification of the energy branches with $\mathbb{M}_\pm$ and names chirality as the Clifford-even candidate for the interference structure. The two decompositions share no projector.

## Derived, Represented, Outside: An Accounting

| Feature of the electron | Status in the framework | Where it comes from |
|---|---|---|
| Spin-$\tfrac{1}{2}$ representation content | Derived | $\mathbb{B}\cong M_2(\mathbb{C})$, unique irreducible module; $SL(2,\mathbb{C})$ double cover |
| Spin states, observables, Born rule | Derived | idempotents of $\mathbb{M}_+$; $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ |
| Spin magnitude $\hbar/2$ | Represented | normalisation of $\hat{S}_k = \tfrac{\hbar}{2}\sigma_k$ |
| Tree-level $g=2$, $\boldsymbol{\mu}_e = -(e/m_e)\mathbf{S}$ | Derived (conditional) | $1/2m$ coefficient from the mass term plus minimal coupling |
| Conserved current $\tilde{J}\in\mathbb{M}_-$ | Derived | Dirac current $j^\mu = \bar{\psi}\gamma^\mu\psi$, $\partial_\mu j^\mu = 0$ |
| Coulomb field $\tilde{F}\in\mathbb{M}_+$ | Derived (from Maxwell) | point-charge solution; purely imaginary vector |
| Mass term couples the two chiralities (central ideals), off-diagonally | Derived | linear chiral pair; Weyl decomposition |
| Rest-energy phase rotates sectors at $mc^2/\hbar$ | Derived | $e^{-i\theta} = \cos\theta\,e_0 - \sin\theta\,(ie_0)$ |
| Zitterbewegung frequency and amplitude | Derived | two-branch interference; $2E/\hbar$, $\hbar/(2mc)$ |
| Mass value $m_e$ | Represented | parameter of the equation |
| Charge value $e$, sign convention, quantisation | Represented | minimal coupling; no derivation in the framework |
| Electron/positron labelling | Represented | charge convention; charge conjugation is a symmetry |
| Anomalous moment $a=(g-2)/2$ | Outside | radiative QED correction |
| Weak $V-A$ chiral coupling | Outside | Standard Model input |
| Quantization of the field | Partly outside | transcription to the spinor module exists; $\mathbb{B}$-intrinsic quantization open |
| Anything that would distinguish the electron from another spin-$\tfrac{1}{2}$ field | Outside | the algebra contains no such discriminator |

## The Gaps, Named

Two gaps are structural and cannot be closed by better notation: the mass value and the charge value are inputs, and the anomaly is outside the classical equation. Three further gaps belong to the programme rather than to this article. **Quantization** has been carried out on the spinor module, but the $\mathbb{B}$-intrinsic form — the operator-valued biquaternion field, its Lagrangian, its Fock space, and the embedding of the fermionic $\mathbb{Z}/2$ grading in $\mathbb{B}$ — remains open, so the electron as a quantum field is only partly inside the framework. **Empirical contact** is absent: nothing here distinguishes the framework from standard relativistic quantum mechanics for the electron. And the framework is **not electron-specific**: it represents the electron, the muon, and any other structureless spin-$\tfrac{1}{2}$ field by the same objects, with no reason in the algebra to prefer one mass or charge over another. These are labelled gaps, not a closed account.

## Summary

The electron is the biquaternion Dirac field, satisfying the linear, chirality-off-diagonal pair $\tilde{\nabla}\tilde{\Psi}_R = m_e\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m_e\tilde{\Psi}_R$, and its spinor-module transcription, the standard Dirac equation. Its mass appears as the coefficient of that off-diagonal chirality coupling; the algebra's real structure $\tilde{\Psi}^\flat = -\tilde{\Psi}^\dagger$ acts on the two sectors with opposite signs, and the rest-energy phase $e^{-im_ec^2t/\hbar} = \cos(m_ec^2t/\hbar)e_0 - \sin(m_ec^2t/\hbar)(ie_0)$ rotates the two sectors into one another at $m_ec^2/\hbar$. Its charge is inserted at the gradient by minimal coupling, which for the linear mass pair is exactly gauge covariant; the conserved current is then derived and lies in $\mathbb{M}_-$, while the static Coulomb field of a point charge is a purely imaginary vector and lies in $\mathbb{M}_+$.

The framework derives the electron's spin-$\tfrac{1}{2}$ representation content from the unique irreducible module of $\mathbb{B}\cong M_2(\mathbb{C})$, and the spin state and observable structure from the idempotents of $\mathbb{M}_+$ with the trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$; the magnitude $\hbar/2$ is a normalisation. It derives the tree-level gyromagnetic factor $g=2$ from the $1/2m_e$ coefficient produced by eliminating the small component, giving $\boldsymbol{\mu}_e = -(e/m_e)\mathbf{S}$ and one Bohr magneton $\mu_B = e\hbar/2m_e = 9.274010\times10^{-24}$ J T$^{-1}$; the anomalous part $a\approx\alpha/2\pi$ is outside the equation. It reproduces the Zitterbewegung at $\omega_Z = 2m_ec^2/\hbar = 1.55269\times10^{21}$ rad s$^{-1}$ and amplitude $\hbar/(2m_ec) = 193.1$ fm, and the companion article's test shows the trembling is the second harmonic of the sector rotation, not a signature of either sector. It contains the two-chirality structure and the mass term as the chirality-mixing coupling, but not the weak $V-A$ coupling of the left-handed electron.

The electron is not an element of either sector: state-like and field-strength-like data are $\mathbb{M}_+$, current is $\mathbb{M}_-$, the real structure $\flat$ acts on the two sectors with opposite signs while the mass term couples the two chiralities, and the rest-energy phase rotates the sectors into one another. What the framework cannot supply is the electron's mass, its charge, its anomalous moment, its empirical signature, and any reason to single it out among spin-$\tfrac{1}{2}$ fields. Those are the labelled gaps, and they are not closed by the notation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) subspaces |
| $\mathbb{H}_{\mathbb{B}}$ | Real quaternion subspace |
| $\tilde{\nabla} = e_0\partial_{ict} + e_k\partial_k$ | Biquaternionic gradient (Dirac operator) |
| $\tilde{\Psi}$, $\tilde{\Psi}^\flat = -\tilde{\Psi}^\dagger$ | Biquaternion Dirac field and anti-Hermitian conjugate (the algebra's real structure; not the mass term) |
| $\tilde{P}_+(\hat{\mathbf{n}}) = \tfrac{1}{2}(e_0 + i\hat{\mathbf{n}})$ | Spin-state idempotent in $\mathbb{M}_+$ |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula (Born rule) |
| $\tilde{J} = ic\,j^0 e_0 + \mathbf{j}$ | Conserved four-current, in $\mathbb{M}_-$ |
| $\tilde{F} = iq\hat{\mathbf{x}}/(4\pi\sqrt{\epsilon}\|\mathbf{x}\|^2)$ | Coulomb field of a point charge, in $\mathbb{M}_+$ |
| $\tilde{K} = i\omega/c\,e_0 + \mathbf{k}$ | Four-wavevector; $N(\tilde{K}) = -m^2c^2/\hbar^2$ |
| $m_e$, $e$, $\hbar$ | Electron mass, elementary charge, reduced Planck constant |
| $\gamma_5$, $\psi_L$, $\psi_R$ | Chirality operator; left- and right-handed Weyl spinors |
| $g$, $\mu_B = e\hbar/2m_e$ | Gyromagnetic factor; Bohr magneton |

## Further Reading

- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original Dirac equation and the prediction $g=2$.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the velocity operator and the spin-$\tfrac{1}{2}$ formalism.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the standard treatment of the electron, its current, and its magnetic moment.
- J. J. Sakurai, *Advanced Quantum Mechanics* (Addison-Wesley, 1967), for the non-relativistic limit, the Darwin term, and the Zitterbewegung.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the two-component spinor calculus and the Weyl spinors.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the spacetime-algebra account of the Dirac electron.
- CODATA Task Group on Fundamental Constants, *CODATA recommended values of the fundamental physical constants* (2018), for $m_e$, $e$, $\hbar$, and the measured electron magnetic moment.
- The companion articles of this series: *The Dirac Equation in Biquaternionic Form*, *The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit*, *Zitterbewegung in Biquaternionic Form*, *Spin-1/2 Quantum Mechanics in Biquaternionic Form*, *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, and *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*.
