# __The Electron in Biquaternionic Form__

## Introduction

The electron is the object on which the relativistic quantum theory of this series is calibrated. It is the particle of Dirac's 1928 equation, the spin-$\tfrac{1}{2}$ system whose magnetic moment is measured to twelve significant figures, and the fermion whose two chiral halves the Standard Model treats differently. In the biquaternion framework of these articles the electron is the standard realization of the **biquaternion Dirac field** $\tilde{\Psi}$: a field in the Dirac module $\Delta=S\oplus S^{\mathrm{c}}$ on which $\mathbb{B}\cong M_2(\mathbb{C})$ acts, satisfying the chirality-off-diagonal pair

$$
\begin{aligned}
\tilde{\nabla}\tilde{\Psi}_R &= m\tilde{\Psi}_L,\\[4pt]
\tilde{\nabla}^{\natural}\tilde{\Psi}_L &= m\tilde{\Psi}_R,
\end{aligned}
$$

with $m = m_e$ the electron mass. At $m=0$ the pair decouples into the two one-sided equations

$$
\tilde{\nabla}\tilde{\Psi}_R = 0, \qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L = 0,
$$

one for each chirality. Each chiral component satisfies the Klein–Gordon equation $(\Box - m^2c^2/\hbar^2)\tilde{\Psi}_{L,R} = 0$, with $\hbar$ and $c$ restored. The anti-Hermitian involution $\tilde{Q}^\flat = -\tilde{Q}^{*}$ is the algebra's real structure; it is defined on $\mathbb{B}$, not on the module, and it is not the mass term.

A framework that reformulates known physics can be read in two very different ways. Read generously, every correct statement about the electron becomes a statement the framework "contains"; read carefully, most of those statements are properties of the Dirac equation that the framework merely transcribes, and the specific numbers attached to the electron must be inserted by hand. This article takes the second interpretation and asks a single question: **which properties of the electron are consequences of the biquaternion structure, which are consequences of the Dirac equation the framework contains, which are parameters inserted from outside, and which lie outside the framework altogether?**

The answer, stated plainly at the outset, is the following. The framework *forces* the electron's spin-$\tfrac{1}{2}$ representation content and its tree-level gyromagnetic factor $g=2$; it *contains* the chirality decomposition, the mass term as the off-diagonal coupler of the two chiral halves $S$ and $S^{\mathrm{c}}$, and the Zitterbewegung with its scale; it *inserts* the mass $m_e$, the charge $e$, and the unit $\hbar$; and it does *not* contain the anomalous magnetic moment, the weak chiral coupling, or a derivation of the mass or charge values. The electron's data are not contained in either subspace $\mathbb{M}_\pm$: its spin state, its current, and its Coulomb field are distributed across both, the operation that exchanges the two subspaces is the central $i$ (the rest-energy phase), and the algebra's real structure $\flat = -{}^{*}$ acts on the two sectors with opposite signs, while the mass term couples the two chiralities.

A second, less comfortable point belongs in the introduction. Almost every statement the framework makes about "the electron" is a statement about a general structureless spin-$\tfrac{1}{2}$ field. The algebra does not single the electron out. Its mass, its charge, and the identity of its antiparticle are the inputs that make the general field into *this* field.

## The Electron as a Biquaternion Field

The notation is that of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ satisfying the product rules

$$
\vec e_x^2 = \vec e_y^2 = \vec e_z^2 = -e_t, \qquad
\vec e_x\vec e_y = -\vec e_y\vec e_x = \vec e_z,
$$

and their cyclic images, and with the scalar imaginary $i$, $i^2 = -1$. The biquaternionic gradient is

$$
\tilde{\nabla} = e_t\,\partial/\partial Q_t + \vec e_x\,\partial/\partial Q_x + \vec e_y\,\partial/\partial Q_y + \vec e_z\,\partial/\partial Q_z.
$$

The coordinates are the corpus's: $Q_t = ict'$ and $Q_x=x$, $Q_y=y$, $Q_z=z$, with $t'$ the real time of the material sector. The conjugate gradient is $\tilde{\nabla}^{\natural} = e_t\,\partial/\partial Q_t - \vec e_x\,\partial/\partial Q_x - \vec e_y\,\partial/\partial Q_y - \vec e_z\,\partial/\partial Q_z$, and the product is the central d'Alembertian

$$
\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \frac{\partial^2}{\partial Q_t^2} + \frac{\partial^2}{\partial Q_x^2} + \frac{\partial^2}{\partial Q_y^2} + \frac{\partial^2}{\partial Q_z^2}.
$$

Two-sided multiplication is written as a **cell**: $L_a\psi = a\psi$, $R_b\psi = \psi b$, and $T_{a,b} = L_aR_b$, so that $T_{a,b}\psi = a\psi b$. Cells compose as

$$
T_{a,b}T_{c,d} = T_{ac,db},
$$

which is the single rule behind every sign below. The cells are the article's working objects; the gamma frame appears only in the last section.

Hermitian conjugation $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$ defines the two sectors by their fixed points,

$$
\mathbb{M}_- = \{\tilde{Q} : \tilde{Q}^{*} = -\tilde{Q}\}, \qquad
\mathbb{M}_+ = \{\tilde{Q} : \tilde{Q}^{*} = \tilde{Q}\}, \qquad
\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-,
$$

where $\natural$ is the quaternion conjugation, which changes the sign of the vector part, and the bar is complex conjugation of the coefficients. The quaternion subspace is the real-coefficient part, $\mathbb{H}_{\mathbb{B}} = \{\tilde{Q} : \bar{\tilde{Q}} = \tilde{Q}\}$. The trace formula is $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$.

The electron's data are carried by the following objects.

| Electron datum | Biquaternion object |
|---|---|
| The field | $\tilde{\Psi}\in\Delta=S\oplus S^{\mathrm{c}}$, equivalently a four-component Dirac spinor $\psi$ |
| Free equation | $\tilde{\nabla}\tilde{\Psi}_R = m_e\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m_e\tilde{\Psi}_R$ |
| Mass | the coefficient $m_e$ of the chirality-off-diagonal mass pair |
| Charge | the coupling $ϙ=-e$ inserted in the gradient (see below) |
| Spin state | an idempotent $\tilde\Pi_1(\vec u) = \tfrac{1}{2}(e_t + i\vec u)\in\mathbb{M}_+$ |
| Spin observables | Hermitian elements $\tilde{H} = i \sum_k h_k\vec e_k\in\mathbb{M}_+$ |
| Conserved current | $\tilde{J} = ic\,j_0 e_t + \vec j\in\mathbb{M}_-$ |
| Chiral halves | the two halves $S$ and $S^{\mathrm{c}}$ of $\Delta$, the left- and right-handed Weyl spinors |

The placement of these objects already contains the article's main structural observation: the electron's state-like data (its spin) and its field-strength-like data (its Coulomb field) are $\mathbb{M}_+$ objects, its current is an $\mathbb{M}_-$ object, the algebra's real structure $\flat$ acts on the two sectors with opposite signs while the mass term couples the two chiralities, and it is the rest-energy phase that rotates one sector into the other. There is no single sector of the algebra in which "the electron" lives.

## Mass: A Term the Framework Needs but Cannot Supply

The electron mass appears in the free equation as the coefficient of the chirality-off-diagonal mass pair

$$
\begin{aligned}
\tilde{\nabla}\tilde{\Psi}_R &= m\tilde{\Psi}_L,\\[4pt]
\tilde{\nabla}^{\natural}\tilde{\Psi}_L &= m\tilde{\Psi}_R .
\end{aligned}
$$

Three statements are worth separating — how the mass couples the two chiralities, how the algebra's real structure acts on the two sectors, and what phase the mass puts between the sectors — and a fourth, negative statement closes the section.

**It mixes the chiralities.** The Dirac module $\Delta$ of the electron is the direct sum of the left-handed and right-handed Weyl halves — the two chiral halves $S$ and $S^{\mathrm{c}}$ — and the mass term couples them: without it, the electron would be two independent massless Weyl fields. The electron's mass is therefore represented, in the framework, as a chirality-mixing term, and this is the structural origin, in the biquaternion interpretation, of the fact that a lone Weyl field cannot carry a mass. The coupling is necessarily off-diagonal: left multiplication preserves each chiral half, so no element of $\mathbb{B}$ relates them, and the mass is the off-diagonal pair above. The pair is complex-linear in the module but not left-$\mathbb{B}$-linear, which is the precise sense in which the mass sits outside the action the algebra supplies of itself.

**The real structure acts on the two sectors with opposite signs.** For an algebra element $\tilde{Q} = \tilde{Q}_+ + \tilde{Q}_-$ with $\tilde{Q}_\pm\in\mathbb{M}_\pm$ one has $\tilde{Q}_\pm^{*} = \pm\tilde{Q}_\pm$, hence

$$
\tilde{Q}^\flat = -\tilde{Q}^{*} = -\tilde{Q}_+ + \tilde{Q}_-,
$$

so $\flat$ acts as $-1$ on the $\mathbb{M}_+$ part and $+1$ on the $\mathbb{M}_-$ part. It **preserves** each sector and marks it with a sign: it is diagonal on the sector decomposition, not an exchange of the two sectors. This is a property of the algebra's real structure, not of the mass term.

**It is not the mass, though it has the shape of one.** An algebra-level coupling built on $\flat$ — the single-field equation $\tilde{\nabla}F = mF^\flat$ on $F\in\mathbb{B}$ — is Majorana-shaped: because $\flat$ is antilinear, such a term pairs the field with its own conjugate and is not invariant under the continuous central phase, which is exactly how a Majorana pairing differs from an ordinary Dirac mass. But it is the wrong equation for the electron, not merely a differently written one: its central-phase plane waves sit on the spacelike locus rather than on the mass shell. The electron's mass must therefore break the central phase rather than being built from $\flat$, and in this article it does — it is the off-diagonal chiral pair, and $\flat$ is used only for conjugation. The operation that exchanges the two sectors is multiplication by the central $i$, $i\mathbb{M}_\pm = \mathbb{M}_\mp$.

**It sets the rate at which the two sectors rotate into one another.** Factoring the rest energy out of a free plane wave gives

$$
\exp\!\Big(-i\frac{mc^2t'}{\hbar}\Big)
= \cos\!\Big(\frac{mc^2t'}{\hbar}\Big)e_t - \sin\!\Big(\frac{mc^2t'}{\hbar}\Big)(ie_t),
$$

where the right-hand side uses only $i^2=-1$ and $e_t=1$: expanding the exponential, $\exp(-i\theta)=e_t-i\theta e_t-\tfrac12\theta^2e_t+\cdots$ and collecting the real and imaginary parts gives the cosine and the sine. Here $e_t\in\mathbb{M}_+$ and $ie_t\in\mathbb{M}_-$ (an imaginary scalar is anti-Hermitian). The rest-energy phase is central, and because $i\mathbb{M}_\pm = \mathbb{M}_\mp$ it is a rotation between the sectors at angular frequency $mc^2/\hbar$: it takes the $\mathbb{M}_+$ direction $e_t$ toward the $\mathbb{M}_-$ direction $ie_t$ and back. The mass sets this scale — the frequency is $mc^2/\hbar$ — through the mass shell. This is the sense in which the electron's mass, in the framework, *is* the rate of the rotation between the material and informational subspaces.

**What is not derived.** The value $m_e = 9.1093837015\times10^{-31}$ kg, or equivalently $m_ec^2 = 0.510998950$ MeV, is not a consequence of the algebra or of the equation; it is a parameter. The framework is scale-free until $m_e$ is supplied, and every electron scale below — the Compton length, the Zitterbewegung frequency — is set by the supplied value, not produced by the structure.

## Charge: A Coupling Constant in the Gradient

The free biquaternion Dirac equation contains no charge. Charge enters only through the coupling of the field to the four-potential $\tilde{A} = i\phi/c\,e_t + \vec A\in\mathbb{M}_-$. In the spinor-module form this is the minimal substitution

$$
\tilde P \to \tilde P - ϙ\tilde A, \qquad\text{equivalently}\qquad p_\mu \to p_\mu - ϙA_\mu,
$$

with $ϙ$ the particle's charge; for the electron $ϙ = -e$. The precise biquaternion form of this coupling is set out in the companion article *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*, which replaces $\tilde\nabla\to D = \tilde\nabla+\frac{iϙ}{\hbar}\tilde{A}$ and $\tilde\nabla^{\natural}\to\bar D = \tilde\nabla^{\natural}+\frac{iϙ}{\hbar}\tilde{A}^{\natural}$, and derives the coupled equation

$$
\begin{aligned}
D\tilde{\Psi}_R &= m\tilde{\Psi}_L,\\[4pt]
\bar{D}\tilde{\Psi}_L &= m\tilde{\Psi}_R,
\end{aligned}
$$

and shows that it is exactly gauge covariant in the massive case as well as the massless one, the central phase passing through the linear mass pair; the charge is therefore *represented* in the framework, not derived by it.

Four statements are worth separating.

**The current is derived.** Given the equation, the Dirac current is conserved. The generator cell of the coordinate $x_\mu$ is

$$
G_\mu := iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}, \qquad \nu(t)=x,\quad \nu(k)=y,
$$

and with the Dirac adjoint $\psi^\dagger G_0 = \psi^\dagger(iR_{\vec e_x}^{\mathrm{axf}})$ the current is the bilinear

$$
j_\mu = \psi^{\dagger}G_0\,G_\mu\,\psi .
$$

In the series' notation the four-vector biquaternion is

$$
\boxed{\;\tilde{J} = ic\,j_0 e_t + \vec j\in\mathbb{M}_-, \qquad j_0 = \psi^\dagger\psi \ge 0\;},
$$

and its conservation reads $\mathrm{Sc}(\tilde\nabla^{\natural}\tilde{J}) = 0$, that is $\partial j_0/\partial t' + \nabla\cdot\vec j = 0$. That the electron's conserved current is a material-sector object is a structural consequence of the equation, not an added assumption.

**The value and sign of the charge are inserted.** Nothing in the algebra fixes $e$, explains why charge is quantised, or explains why the electron and the proton have equal and opposite charge. The equation with $ϙ = -e$ and the equation with $ϙ = +e$ have the same form, related by $\tilde{A}\to-\tilde{A}$; the labelling of which branch is the electron is a convention. Charge conjugation makes this explicit: the equation admits the antisymmetric cell

$$
C = -iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},\qquad C^{T} = -C,\qquad C^2 = -e_t,\qquad
C\,G_\mu^{T}C^{-1} = -G_\mu\quad(\mu=0,1,2,3),
$$

under which the conserved current reverses sign and the two frequency branches are exchanged. The framework represents both signs of charge on the same footing.

**The electron's Coulomb field is an $\mathbb{M}_+$ object.** For a point charge $ϙ$ at rest the field-strength biquaternion is, from the companion article on Maxwell's equations,

$$
\tilde{F}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = \frac{i\,ϙ\,\vec u_x}{4\pi\sqrt{\epsilon}\,\|(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\|^2},
$$

a purely imaginary vector, hence an element of the Hermitian subspace $\mathbb{M}_+$, with $\vec u_x = (x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)/\|(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\|$ the radial unit vector. The electron's charge shows itself, in the framework, through a field in the informational sector, while its current lies in the material sector. The two faces of the same charge sit in opposite halves of the algebra.

**What is derived once the coupling is inserted.** The minimal substitution yields the magnetic coupling with the coefficient $1/2m_e$, and hence the sign relation $\vec\mu_e = -(e/m_e)\vec S$: the electron's magnetic moment is anti-parallel to its spin because its charge is negative. The magnitude, however, is dimensional and carries $e$ and $\hbar$.

## Spin: Derived as a Representation, Normalised by Hand

The electron's spin is where the framework is strongest and where the distinction between derived and inserted is sharpest.

**Derived: the representation.** The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ has a unique irreducible module, of complex dimension two, and the group of unit-norm biquaternions $\{Q : QQ^{\natural} = e_t\}$ is $SL(2,\mathbb{C})$, the double cover of the proper orthochronous Lorentz group. A field in that module is a Weyl spinor, the representation $(\tfrac12,0)$; the Dirac field of the previous section lives in $\Delta = S\oplus S^{\mathrm{c}}$, the direct sum of the two inequivalent modules, and so carries $(\tfrac12,0)\oplus(0,\tfrac12)$. In either case the spin is $\tfrac12$: a rotation by $2\pi$ acts as $-e_t$ on the spinor module while acting as $+e_t$ on the four-vectors of $\mathbb{M}_-$. The twofold, double-valued character of electron spin is therefore a representation-theoretic consequence of where the field lives, not an independent postulate. The spin rotations are the real unit quaternions, forming $SU(2)$.

**Derived: the state and observable structure.** On the dictionary used in the companion articles, the electron's spin state along a unit direction $\vec u$ is represented by the idempotent $\tilde\Pi_1(\vec u) = \tfrac{1}{2}(e_t + i\vec u)\in\mathbb{M}_+$, and its spin observables are the Hermitian elements $i \sum_k h_k\vec e_k\in\mathbb{M}_+$. (The companion articles leave the spinor-to-biquaternion dictionary as a convention; the state and observable structure below is what is checked, and it does not depend on which of the equivalent dictionaries is fixed.) The trace formula reproduces the spin-$\tfrac{1}{2}$ expectation values. For $\tilde{H} = i \sum_k h_k \vec e_k$ and $\tilde\Pi(\vec n) = \tfrac{1}{2}(e_t + i n_\nu \vec e_\nu)$ one has $2\,\mathrm{Sc}(\tilde\Pi\tilde{H}^{*}) = n_\nu h_\nu$; in particular $2\,\mathrm{Sc}\big(\tilde\Pi_1(\vec e_z)(i\vec e_z)\big) = 1$ and $2\,\mathrm{Sc}\big(\tilde\Pi_1(\vec e_z)(i\vec e_x)\big) = 0$, the correct values for the spin along $z$ and $x$.

**Inserted: the magnitude.** The spin operator is $S_k = \tfrac{\hbar}{2}(i\vec e_k)$. The cell $i\vec e_k$ is Hermitian and squares to $+e_t$, so it is the algebra's spin component and has the two eigenvalues $\pm1$. The factor $\hbar/2$ is a normalisation, not a prediction: the algebra fixes that spin is two-valued and that its observables close under $SU(2)$, but it does not fix the unit in which spin is measured. The number $\tfrac{1}{2}$ in "spin-$\tfrac{1}{2}$" is algebra; the number $\hbar$ is physics inserted from outside.

## The Dirac Description of the Electron

The electron's relativistic dynamics is the chiral pair $\tilde{\nabla}\tilde{\Psi}_R=m_e\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L=m_e\tilde{\Psi}_R$. The plane-wave solutions are computed on the spinor module, in the notation of the companion solutions article. They come in two branches at each momentum, the positive-frequency $w^{(r)}(\vec p)\exp\!\big(-i(Et'-\vec p\cdot\vec r)/\hbar\big)$ and the negative-frequency $v^{(r)}(\vec p)\exp\!\big(+i(Et'-\vec p\cdot\vec r)/\hbar\big)$, with $\vec r = x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$, $E = +\sqrt{\vec p^2c^2 + m_e^2c^4}$ and $r$ the spin label; together they span a four-dimensional complex amplitude space, which is the four components of the Dirac spinor. The spin sums, normalisations, and bilinears are constructed in the companion solutions article and are not repeated here.

**A note on the wave biquaternion.** The mass-shell condition is written in the corpus convention, in which the four-wavevector has the imaginary time component of the $ict'$ convention,

$$
\tilde P/\hbar = i\,\frac{\omega}{c}\,e_t + \vec k, \qquad
\langle\tilde P/\hbar\rangle_{\natural} = \tilde P\tilde P^{\natural}/\hbar^{2} = -\frac{\omega^2}{c^2} + \vec k^2 = -\frac{m_e^2c^2}{\hbar^2},
$$

with $\langle\tilde Q\rangle_\natural = \tilde Q\tilde Q^\natural$ the quaternionic norm, and $\vec k^2$ the Euclidean square $k_x^2+k_y^2+k_z^2$, which is what the norm of a vector part produces. This is $E^2 = \vec p^2c^2 + m_e^2c^4$ under $E = \hbar\omega$, $\vec p = \hbar\vec k$, and it is the form used by the companion solutions article and by the parent Dirac article.

**Antiparticle.** The two frequency branches are exchanged by charge conjugation, and in the quantized interpretation the negative-frequency branch describes the positron. The framework represents the electron and the positron on the same algebraic footing; which branch is called the electron is fixed by the charge convention of the previous section, not by the algebra.

### The One-Sided and the Two-Sided Forms of the Equation

The article carries two Dirac equations, and they must not be read as one. They use the same cells and the same mass coefficient; they differ in which side of the field the derivative acts and in where the mass sits.

The **one-sided equation** is the corpus's definition: the chiral pair above. The gradient acts by left multiplication, the field is the module-valued $\tilde\Psi = \tilde\Psi_L+\tilde\Psi_R\in\Delta$, and the mass is the off-diagonal pairing of the two chiral halves,

$$
\begin{aligned}
\tilde{\nabla}\tilde{\Psi}_R &= m\,\tilde{\Psi}_L,\\[4pt]
\tilde{\nabla}^{\natural}\tilde{\Psi}_L &= m\,\tilde{\Psi}_R .
\end{aligned}
$$

This is the form in which chirality is visible, and it is the form the sections on mass and on the two chiralities use.

The **two-sided equation** is the dictionary form of V. V. Kravchenko: a single equation on the algebra-valued field $F\in\mathbb{B}$,

$$
\mathcal{N}F = \Big(i\frac{\partial}{\partial t'}+D_3\Big)F - m\,i\,\overline{F}\,\vec e_z = 0,
\qquad\text{that is}\qquad
-\tilde{\nabla}^{\natural}F - m\,i\,\overline{F}\,\vec e_z = 0
$$

in natural units, with $D_3 = \sum_k\vec e_k\,\partial/\partial Q_k$ and the bar the coefficientwise complex conjugation. The time derivative and the spatial gradient act by left multiplication; the mass term acts by right multiplication through $\vec e_z$ and carries the antilinear conjugation. This is the form in which the quaternionic analysis acts — the shifted operator, the Cauchy kernel, and the integral representation of the harmonic spinor field.

| | One-sided equation | Two-sided equation |
|---|---|---|
| Equation | $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$, $\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R$ | $\mathcal{N}F=0$, as displayed |
| Field | $\tilde\Psi\in\Delta=S\oplus S^{\mathrm{c}}$ | $F\in\mathbb{B}$ |
| Mass | the off-diagonal pairing of $S$ and $S^{\mathrm{c}}$ | $-mi\,\overline{F}\,\vec e_z$: a conjugation and a direction |
| Derivative | left, by $\tilde\nabla$ and $\tilde\nabla^{\natural}$ | left by $i\partial/\partial t'$ and $D_3$; right by $\vec e_z$ in the mass |
| Chirality | the cell $\gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$, acting as $\operatorname{diag}(-I_2,I_2)$ | the same cell, the dictionary's volume element, a right multiplication by $\vec e_z$ |
| Use | the definition, the kinematics, and the mass term | the analytic theory and the integral representation |

The two are related by an explicit real-linear dictionary, not by an identity of operators. The one-sided pair is the definition, and the two-sided single equation is the form in which the analytic machinery acts. The electron's mass is the same coefficient $m_e$ in both; what changes is the representation, not the physics.

## Gyromagnetic Ratio: The One Quantitative Number the Equation Predicts

The Dirac description yields one celebrated number. Carrying the biquaternion Dirac equation to the non-relativistic regime — the computation is performed in the companion solutions article and its exercise — eliminates the small component and leaves the Pauli equation with the spin term. With $\sigma_k\mapsto i\vec e_k$, that term is the Hermitian element

$$
-\frac{ϙ\hbar}{2m_e}\,i\,\vec B \in \mathbb{M}_+ .
$$

Writing the coupling as $-\vec\mu\cdot\vec B$ identifies $\vec\mu = (ϙ/m_e)\vec S$, with the spin components $S_k = \tfrac{\hbar}{2}i\vec e_k$, which is $\vec\mu = g\,(ϙ/2m_e)\vec S$ with

$$
g = 2 .
$$

The coefficient $1/2m_e$ is produced by the elimination, not put in by hand: this is Dirac's tree-level prediction, here a property of the biquaternionic mass term. For the electron, $ϙ = -e$, so

$$
\boxed{\;\vec\mu_e = -\frac{e}{m_e}\vec S = -g\,\frac{e}{2m_e}\vec S, \qquad g = 2\;},
$$

of magnitude one Bohr magneton $\mu_B = e\hbar/2m_e = 9.274010\times10^{-24}$ J T$^{-1}$ when $\vec S$ is aligned with $\vec B$.

Two qualifications belong with the result. First, the derivation is the standard Dirac one, transcribed; the biquaternion form supplies the compact notation and the sector interpretation of the spin coupling as an $\mathbb{M}_+$ observable, not an independent derivation. Second, $g=2$ is not an electron-specific number: it holds for any structureless spin-$\tfrac{1}{2}$ field, so it distinguishes the electron from a spin-1 particle but not from a muon.

**Outside the framework: the anomaly.** The measured value is $g/2 = 1.00115965218$, i.e. $a = (g-2)/2 = 1.159652\times10^{-3}$, close to the one-loop Schwinger value $a \approx \alpha/2\pi = 1.161410\times10^{-3}$. This is a radiative correction of quantum electrodynamics; it lies outside the classical equation treated here, and the framework does not contain it. The tree-level $g=2$ is the whole of what the equation supplies.

## Zitterbewegung: The Scale of the Mass, Not a Signature of a Sector

The electron is the particle on which the Zitterbewegung was found. In the framework's own terms, the trembling is the interference of the two frequency branches, with angular frequency $2E/\hbar$ and amplitude of order $\hbar/(2mc)$. For the electron at rest these are

$$
\omega_Z = \frac{2m_ec^2}{\hbar} = 1.55269\times10^{21}\ \text{rad s}^{-1},
\qquad \frac{\hbar}{2m_ec} = 193.1\ \text{fm},
$$

half the reduced Compton wavelength $386.2$ fm. These are the standard values, reconfirmed numerically in the companion article on the Zitterbewegung.

The framework's temptation is to read the trembling as the observable face of the complexification — positive- and negative-energy components being the two sectors. The companion article tests that identification and refutes it: the energy-sign projector is built from $\beta = iR_{\vec e_x}^{\mathrm{axf}} = iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$, an *odd* Clifford element, outside the even subalgebra $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}$, while the sector projectors are built from Hermitian conjugation, internal to $\mathbb{B}$; the two splittings are also splittings of different objects (the spinor module and the algebra). What survives is a relation of scale and phase: at rest the trembling frequency is exactly twice the rest-energy sector-rotation frequency $m_ec^2/\hbar$, because the trembling phase is the square of the free-evolution phase. For the electron this means that its rest energy sets both the rate at which the sectors rotate into one another and the frequency of the trembling, without the trembling being an informational-sector effect.

## The Two Chiralities

The electron field is a section of $\Delta$, and the module decomposes into a left-handed and a right-handed Weyl half,

$$
\tilde\Psi = \tilde\Psi_L + \tilde\Psi_R, \qquad \tilde\Psi_L\in S,\quad \tilde\Psi_R\in S^{\mathrm{c}},
$$

each a two-component Weyl spinor. The decomposition is expressed by the chirality cell $-iR_{\vec e_z}^{\mathrm{axf}} = -iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$, the operator $\psi\mapsto -i\,e_t\,\psi\,\vec e_z$: it anticommutes with every generator,

$$
\big(-iR_{\vec e_z}^{\mathrm{axf}}\big)\big(iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\big)
= -\big(iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\big)\big(-iR_{\vec e_z}^{\mathrm{axf}}\big),
$$

and therefore commutes with every Clifford-even element, the biquaternion subalgebra among them. Its square uses $i^2=-1$ and $\vec e_z^2=-e_t$,

$$
\big(-iR_{\vec e_z}^{\mathrm{axf}}\big)^2 = (-i)^2R_{\vec e_z^2}^{\mathrm{axf}} = (-1)(-e_t) = e_t ,
$$

so it is a grading. The massless equation splits into two independent Weyl equations, one per chirality; the mass term couples them, which is the same statement as the chirality-mixing of the mass section.

Two structural points and two cautions.

**Derived.** The two-chiral structure itself is a consequence of the spinor representation: the Dirac spinor is the direct sum of the two inequivalent two-component representations of $SL(2,\mathbb{C})$, and the mass term is the unique Lorentz-invariant coupling between them. For a massless electron, chirality coincides with helicity, so the two branches become two definite chiralities. This is a genuine structural consequence of the algebra and of the equation.

**Represented, not derived: the weak chiral coupling.** In the Standard Model the electron couples to the weak interaction through its left-handed component only. The framework contains the chirality decomposition, so it has the vocabulary for this, but it does not select the coupling: nothing in $\mathbb{B}$ or in the Dirac equation says that one chirality couples and the other does not. The $V-A$ structure is an input.

**Caution: the status of the chirality projectors.** Whether the projectors associated with chirality are to be read as objects inside $\mathbb{B}$ alone, or as central idempotents of the complexified algebra, depends on how the biquaternion imaginary is identified with the Clifford volume element — the two-$i$ point that the companion articles record. The parent Dirac article states the projectors as central idempotents of the complexified even algebra. This article therefore asserts the splitting of the equation and the commutation of the chirality cell with the even subalgebra, which are verified, and does not assert a canonical embedding of the projectors in $\mathbb{B}$, which the corpus has not settled.

**Caution: chirality is not the same as the sector split.** The chiral decomposition is a decomposition of the spinor module by the chirality operator; the sector decomposition is a decomposition of the algebra by Hermitian conjugation. The Zitterbewegung article reaches the same distinction from the other side when it rejects the identification of the energy branches with $\mathbb{M}_\pm$ and names chirality as the Clifford-even candidate for the interference structure. The two decompositions share no projector.

## Derived, Represented, Outside: An Accounting

| Feature of the electron | Status in the framework | Where it comes from |
|---|---|---|
| Spin-$\tfrac{1}{2}$ representation content | Derived | $\mathbb{B}\cong M_2(\mathbb{C})$, unique irreducible module; $SL(2,\mathbb{C})$ double cover |
| Spin states, observables, expectation values | Derived | idempotents of $\mathbb{M}_+$; $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ |
| Spin magnitude $\hbar/2$ | Represented | normalisation of $S_k = \tfrac{\hbar}{2}i\vec e_k$ |
| Tree-level $g=2$, $\vec\mu_e = -(e/m_e)\vec S$ | Derived (conditional) | $1/2m_e$ coefficient from the mass term plus minimal coupling |
| Conserved current $\tilde{J}\in\mathbb{M}_-$ | Derived | Dirac current $j_\mu = \psi^{\dagger}G_0\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\psi$, $\mathrm{Sc}(\tilde\nabla^{\natural}\tilde{J}) = 0$ |
| Coulomb field $\tilde{F}\in\mathbb{M}_+$ | Derived (from Maxwell) | point-charge solution; purely imaginary vector |
| Mass term couples the two chiral halves $S$ and $S^{\mathrm{c}}$, off-diagonally | Derived | off-diagonal chiral pair; Weyl decomposition |
| Two-sided single-equation form | Derived (dictionary) | the real-linear dictionary $F\in\mathbb{B}$; a change of representation, not of physics |
| Rest-energy phase rotates sectors at $mc^2/\hbar$ | Derived | $\exp(-i\theta) = \cos\theta\,e_t - \sin\theta\,(ie_t)$ |
| Zitterbewegung frequency and amplitude | Derived | two-branch interference; $2E/\hbar$, $\hbar/(2mc)$ |
| Mass value $m_e$ | Represented | parameter of the equation |
| Charge value $e$, sign convention, quantisation | Represented | minimal coupling; no derivation in the framework |
| Electron/positron labelling | Represented | charge convention; charge conjugation is a symmetry |
| Anomalous moment $a=(g-2)/2$ | Outside | radiative QED correction |
| Weak $V-A$ chiral coupling | Outside | Standard Model input |
| Quantization of the field | Partly outside | transcription to the spinor module exists; $\mathbb{B}$-intrinsic quantization open |
| Anything that would distinguish the electron from another spin-$\tfrac{1}{2}$ field | Outside | the algebra contains no such discriminator |

## The Gaps, Named

Two gaps are structural and cannot be closed by better notation: the mass value and the charge value are inputs, and the anomaly is outside the classical equation. Three further gaps belong to the programme rather than to this article. **Quantization** has been carried out on the spinor module, but the $\mathbb{B}$-intrinsic form — the operator-valued biquaternion field, its Lagrangian, its Fock space, and the embedding of the fermionic $\mathbb{Z}/2$ grading in $\mathbb{B}$ — remains open, so the electron as a quantum field is only partly inside the framework. **Empirical contact** is absent: nothing here distinguishes the framework from standard relativistic quantum physics for the electron. And the framework is **not electron-specific**: it represents the electron, the muon, and any other structureless spin-$\tfrac{1}{2}$ field by the same objects, with no reason in the algebra to prefer one mass or charge over another. These are labelled gaps, not a closed account.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The bracket is the frame, on the generators as on the metric, $\gamma_\mu[\mathbb{M}_-]$ or $\gamma_\mu[\mathbb{B}]$, so that a glyph names a display and not an object of the algebra.

The sections above are written in cells; this section writes the same cells as gamma matrices, for readers who want the standard notation. The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Each gamma is a single cell $T_{a,b}=L_aR_b$, a pure tensor, and a general element of $M_4(\mathbb{C})$ is a sum of at most four such cells.

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

$\gamma_5$ is the cell of the chirality operator $\Gamma:\psi\mapsto -i\,e_t\,\psi\,\vec e_z = -iR_{\vec e_z}^{\mathrm{pau}}$, which acts on the Dirac module. The central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$, where $\tilde\Xi_{\mathrm{ad}}$ is the central root of $-1$ that complexifies the real subalgebra $\mathbb{B}_{\mathbb{R}}=\mathbb{H}_{\mathbb{B}}$ ($\tilde\Xi_{\mathrm{ad}}^2=-1$, $[\tilde\Xi_{\mathrm{ad}},i]=0$), is the difference of the two central idempotents of the complexified algebra, so $\chi^2=i^2\tilde\Xi_{\mathrm{ad}}^2=(-1)(-1)=e_t$. The grading $\chi$ is central and belongs to the algebra, $\Gamma$ is its representative on the module, and $\gamma_5$ is that representative written as a cell.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$. The generator cells $G_\mu$ of the charge section are these gammas, $G_\mu=\gamma_\mu[\mathbb{M}_-]$, and the charge-conjugation cell is $C = -iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} = i\gamma_2[\mathbb{M}_-]\gamma_0[\mathbb{M}_-]$, the antisymmetric matrix with $C^2=-I_4$ that reverses all four gammas under transposition.

**The identities the bodies cite.** In the $\gamma$ reading, with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the cells,
$$
\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k[\mathbb{M}_-])^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu[\mathbb{M}_-],\gamma_5\}=0,
$$
$$
[\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]]=2\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\quad(\mu\ne\nu),\qquad
[\gamma_a[\mathbb{M}_-],S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d[\mathbb{M}_-]-\varepsilon_a\delta_{ad}\gamma_c[\mathbb{M}_-],\qquad
S_{cd}=\tfrac14[\gamma_c[\mathbb{M}_-],\gamma_d[\mathbb{M}_-]],
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-])=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}
-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}
+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$
The contraction sums follow from the squares. With one index raised, $\gamma^\mu[\mathbb{M}_-]=-\varepsilon_\mu\gamma_\mu[\mathbb{M}_-]$, so that $\sum_\mu\gamma^\mu[\mathbb{B}]\gamma_\mu[\mathbb{B}]=-4I_4$, $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2\gamma_\alpha[\mathbb{M}_-]$, $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]$.
## Summary

The electron is the biquaternion Dirac field, a section of $\Delta=S\oplus S^{\mathrm{c}}$ satisfying the chirality-off-diagonal pair $\tilde{\nabla}\tilde{\Psi}_R = m_e\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m_e\tilde{\Psi}_R$, and its spinor-module transcription, the standard Dirac equation. The same field has a two-sided single-equation form on $\mathbb{B}$, with the conjugation in the mass term; that is the form the quaternionic analysis uses, not a second theory. Its mass appears as the coefficient of the off-diagonal chirality coupling; the algebra's real structure $\flat=-{}^{*}$ acts on the two sectors with opposite signs, and the rest-energy phase $\exp(-im_ec^2t'/\hbar) = \cos(m_ec^2t'/\hbar)e_t - \sin(m_ec^2t'/\hbar)(ie_t)$ rotates the two sectors into one another at $m_ec^2/\hbar$. Its charge is inserted at the gradient by minimal coupling, which for the linear mass pair is exactly gauge covariant; the conserved current is then derived and lies in $\mathbb{M}_-$, while the static Coulomb field of a point charge is a purely imaginary vector and lies in $\mathbb{M}_+$.

The framework derives the electron's spin-$\tfrac{1}{2}$ representation content from the unique irreducible module of $\mathbb{B}\cong M_2(\mathbb{C})$, and the spin state and observable structure from the idempotents of $\mathbb{M}_+$ with the trace formula $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$; the magnitude $\hbar/2$ is a normalisation. It derives the tree-level gyromagnetic factor $g=2$ from the $1/2m_e$ coefficient produced by eliminating the small component, giving $\vec\mu_e = -(e/m_e)\vec S$ and one Bohr magneton $\mu_B = e\hbar/2m_e = 9.274010\times10^{-24}$ J T$^{-1}$; the anomalous part $a\approx\alpha/2\pi$ is outside the equation. It reproduces the Zitterbewegung at $\omega_Z = 2m_ec^2/\hbar = 1.55269\times10^{21}$ rad s$^{-1}$ and amplitude $\hbar/(2m_ec) = 193.1$ fm, and the companion article's test shows the trembling is the second harmonic of the sector rotation, not a signature of either sector. It contains the two-chirality structure and the mass term as the chirality-mixing coupling, but not the weak $V-A$ coupling of the left-handed electron.

The electron's data are not confined to either sector: state-like and field-strength-like data are $\mathbb{M}_+$, current is $\mathbb{M}_-$, the real structure $\flat$ acts on the two sectors with opposite signs while the mass term couples the two chiralities, and the rest-energy phase rotates the sectors into one another. What the framework cannot supply is the electron's mass, its charge, its anomalous moment, its empirical signature, and any reason to single it out among spin-$\tfrac{1}{2}$ fields. Those are the labelled gaps, and they are not closed by the notation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q_t=ict'$, $Q_k=x,y,z$ | Coordinates; $t'$ the real time of the material sector |
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$, $\vec e_x\vec e_y=\vec e_z$ cyclically |
| $L_a$, $R_b$, $T_{a,b}=L_aR_b$ | Cells, $T_{a,b}\psi=a\psi b$; $T_{a,b}T_{c,d}=T_{ac,db}$ |
| $G_\mu = iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ | Generator cell of $x_\mu$, with $\nu(t)=x$, $\nu(k)=y$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\natural$, $\bar{\cdot}$, ${}^{*}$ | Quaternion, complex, Hermitian conjugations; $\tilde Q^*=\overline{\tilde Q^\natural}$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) subspaces |
| $\mathbb{H}_{\mathbb{B}}$ | Real quaternion subspace, $\bar{\tilde Q}=\tilde Q$ |
| $\tilde{\nabla} = e_t\partial/\partial Q_t + \sum_{k=x,y,z}\vec e_k\partial/\partial Q_k$ | Biquaternionic gradient (Dirac operator) |
| $\Box = \tilde\nabla\tilde\nabla^\natural = \sum_\mu\partial^2/\partial Q_\mu^2$ | Central d'Alembertian; $Q_t=ict'$ |
| $\Delta = S\oplus S^{\mathrm{c}}$, $S$, $S^{\mathrm{c}}$ | Dirac module and its two chiral halves |
| $\tilde{\Psi}$, $\tilde{Q}^\flat = -\tilde{Q}^{*}$ | Biquaternion Dirac field; the algebra's real structure (not the mass term) |
| $\chi = i\tilde\Xi_{\mathrm{ad}}$, $\Gamma = -iR_{\vec e_z}^{\mathrm{axf}}$ | Central chirality grading, $\chi^2=e_t$; its representative on the module |
| $C = -iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | Charge-conjugation cell, $C^{T}=-C$, $C^2=-e_t$, $CG_\mu^{T}C^{-1}=-G_\mu$ |
| $\tilde\Pi_1(\vec u) = \tfrac{1}{2}(e_t + i\vec u)$ | Spin-state idempotent in $\mathbb{M}_+$ |
| $\mathrm{Sc}$, $\mathrm{Vect}$ | Scalar and vector parts of an algebra element |
| $\langle\tilde Q\rangle_\natural = \tilde Q\tilde Q^\natural$ | Quaternionic norm |
| $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | Trace reading at normalisation (expectation values) |
| $\tilde{J} = ic\,j_0 e_t + \vec j$ | Conserved four-current, in $\mathbb{M}_-$ |
| $\tilde{F} = iϙ\vec u_x/(4\pi\sqrt{\epsilon}\|(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\|^2)$ | Coulomb field of a point charge, in $\mathbb{M}_+$; $\vec u_x$ the radial unit vector |
| $\tilde P/\hbar = i(\omega/c)\,e_t + \vec k$ | Four-wavevector; $\langle\tilde P/\hbar\rangle_{\natural} = -m^2c^2/\hbar^2$ |
| $\varepsilon=(1,-1,-1,-1)$ | Sign weights of the $\mathbb{M}_-$ frame; metric in the gamma section |
| $m_e$, $e$, $\hbar$, $c$ | Electron mass, elementary charge, reduced Planck constant, speed of light |
| $\tilde\Psi_L$, $\tilde\Psi_R$ | Left- and right-handed Weyl halves, in $S$ and $S^{\mathrm{c}}$ |
| $\mathcal{N}F = (i\partial/\partial t'+D_3)F - mi\,\overline{F}\,\vec e_z$, $D_3=\sum_k\vec e_k\partial/\partial Q_k$ | Two-sided Dirac equation of the dictionary form |
| $g$, $\mu_B = e\hbar/2m_e$ | Gyromagnetic factor; Bohr magneton |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original Dirac equation and the prediction $g=2$.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the velocity operator and the spin-$\tfrac{1}{2}$ formalism.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the standard treatment of the electron, its current, and its magnetic moment.
- J. J. Sakurai, *Advanced Quantum Mechanics* (Addison-Wesley, 1967), for the non-relativistic limit, the Darwin term, and the Zitterbewegung.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the two-component spinor calculus and the Weyl spinors.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the spacetime-algebra account of the Dirac electron.
- V. V. Kravchenko, "On a Biquaternionic Bag Model," *Zeitschrift für Analysis und ihre Anwendungen* **14** (1995), no. 1, 3–14, for the two-sided biquaternionic Dirac equation with the conjugation in the mass term.
- CODATA Task Group on Fundamental Constants, *CODATA recommended values of the fundamental physical constants* (2018), for $m_e$, $e$, $\hbar$, and the measured electron magnetic moment.
- The companion articles of this series: [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), [The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit](the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html), [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html), [Zitterbewegung in Biquaternionic Form](zitterbewegung-in-biquaternionic-form.html), [Spin-1/2 Quantum Physics in Biquaternionic Form](spin-1-2-quantum-physics-in-biquaternionic-form.html), [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), and [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html).
