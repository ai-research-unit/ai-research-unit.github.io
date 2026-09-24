# __Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda__

## Introduction

**Quantum chromodynamics** (QCD) is the non-abelian gauge theory of the colour interaction: a gauge theory with group $SU(3)$, quarks in the fundamental three-dimensional representation, gluons in the adjoint, a coupling that becomes weak at short distances, and a spectrum from which the coloured states are absent — confinement. This article is a research agenda for QCD inside the biquaternion framework. Its subject is not a result; it is the boundary between what the framework has built and what QCD requires.

The starting position is stated at the outset, because the whole agenda depends on it and because it is easy to overstate.

- **The framework has a non-abelian gauge construction.** It has a connection, a curvature with the commutator term, the adjoint transformation law, the Bianchi identity, and a gauge-invariant Yang–Mills density, developed inside the algebra for a gauge algebra that is present in the material sector. This is established and is recalled in the next section.
- **The framework records a chiral-fermion issue.** Its spinor module carries the chiral projectors and a chirality-odd mass bilinear; the gauge group drawn from the algebra's center is vector-like and cannot be chiral; and whether the framework's own mass is the real form of a Dirac mass or a conjugate-pairing (Majorana-type) term is open. This is established, and it is inherited here unchanged.
- **The framework has not constructed a colour theory.** Nothing in the series derives $SU(3)$, and nothing derives any three-valued internal structure that could play the role of colour. The word "colour" occurs in the corpus only where standard QCD is being transcribed — in the renormalization-group article, which imports the $SU(3)$ one-loop coefficients, and in the spinor-helicity article, which states plainly that the framework "does not contain a colored gauge theory". No article derives a colour group, a quark colour triplet, a gluon octet, a confinement mechanism, or a colour coupling.

The discipline this forces on the article is the one the genre requires: **an agenda that quietly assumes a colour group has fabricated its premise.** The colour group is therefore carried as an **open item throughout**, never as a working assumption. Wherever a standard QCD statement is written down — $N_c=3$, $b_0 = 11 - \tfrac{2}{3}N_f$, the area law — it is flagged as standard input, not as a framework result.

**The three-way classification.** The article sorts every item into one of three categories, and the distinction is the point of the agenda.

1. **Established.** Recomputed in the series and inherited here; the non-abelian gauge machinery and the chiral structure of the module.
2. **Obstacle with a known route.** The object does not exist, but the route to it is identifiable, usually because standard field theory supplies the computation and the framework must reproduce it on its own carrier.
3. **Obstacle with no route yet.** No mechanism has been proposed, and naming an object is not the same as having a route to it. Confinement and the colour group are in this class.

The four obstacles the agenda treats are the **colour group** (§"The Colour Group"), **confinement** (§"Confinement"), the **chiral-fermion issue** as it bears on the quark couplings (§"The Chiral-Fermion Issue"), and the **running coupling and asymptotic freedom** (§"The Running Coupling"). They are not independent: the last needs the first and the third, and confinement needs apparatus all of them need. A closing ledger collects them, and a short synthesis names the two upstream items.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_1e_2 = e_3$, and $i$ is the scalar imaginary, $i^2 = -1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector), with $\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+$; $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the center. The biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$, its quaternion conjugate is $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_1\partial_x - e_2\partial_y - e_3\partial_z$, and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$. For the non-abelian sector we use the $\mathfrak{su}(2)$ connection and field strength of the read list, $\mathcal{A}_\mu \in \mathfrak{su}(2)$, $F_{\mu\nu} = \partial_\mu\mathcal{A}_\nu - \partial_\nu\mathcal{A}_\mu + i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$, $\kappa = q/\hbar$, with $[D_\mu,D_\nu] = i\kappa F_{\mu\nu}$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the **speed of light in the medium** and $c_0$ the vacuum speed of light. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged. The symbols $SU(3)$, $N_c$, $T^a$, $N_f$, and $\alpha_s$ are **standard QCD notation, not framework objects**; they are used only where standard results are being quoted or where an object is being named as missing.

## What the Framework Already Reaches

### The non-abelian gauge construction

The read-list article *Non-Abelian Gauge Fields in Biquaternionic Form* builds the general non-abelian gauge structure inside $\mathbb{B}$. Its results are established and are used here unchanged.

The vector part of the material sector, $\mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\}$, closes under the commutator and is $\mathfrak{su}(2)$ in a non-standard normalization,

$$
[e_a,e_b] = 2\,\varepsilon_{abc}\,e_c, \qquad a,b,c = 1,2,3,
\qquad T_a = \tfrac12 e_a,\quad [T_a,T_b] = \varepsilon_{abc}T_c,\quad \mathrm{Tr}(T_aT_b) = -\tfrac12\delta_{ab}.
$$

The gauge group is the unit real quaternions, $SU(2) = \{U \in \mathbb{H}_{\mathbb{B}} : U\bar U = e_0\}$, acting on a matter field by left multiplication. A local transformation $U(\tilde{X})$ forces the connection

$$
\mathcal{A}'_\mu = U\,\mathcal{A}_\mu\,U^{-1} + \frac{i}{\kappa}\,(\partial_\mu U)\,U^{-1},
$$

which reduces to the abelian law $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$ when $U$ is central. The field strength

$$
F_{\mu\nu} = \partial_\mu \mathcal{A}_\nu - \partial_\nu \mathcal{A}_\mu + i\kappa\,[\mathcal{A}_\mu, \mathcal{A}_\nu],
\qquad
F = d\mathcal{A} + i\kappa\,\mathcal{A}\wedge\mathcal{A},
\qquad
[D_\mu,D_\nu] = i\kappa F_{\mu\nu},
$$

is **not** gauge invariant but transforms in the adjoint representation, $F'_{\mu\nu} = U F_{\mu\nu} U^{-1}$; it satisfies the Bianchi identity $D_\lambda F_{\mu\nu} + D_\mu F_{\nu\lambda} + D_\nu F_{\lambda\mu} = 0$; and $-\tfrac12\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$ is a gauge-invariant density, with the matrix trace on the $\mathfrak{su}(2)$ factor and not the informational trace formula.

What this construction is, for the purposes of this agenda, is the **general machinery of a non-abelian gauge theory**: everything that depends only on having a compact simple factor and a non-commuting connection is present. What it is not is a *colour* theory, because the factor it uses is $\mathfrak{su}(2)$ and the connection is $\mathfrak{su}(2)$-valued. The whole question of QCD is whether the framework can replace that factor by colour; the next section shows where that step stops.

### The gauge algebra the algebra contains, and its ceiling

The available gauge algebra is determined by the algebra, not chosen. The material sector decomposes as a Lie algebra under the commutator,

$$
\mathbb{M}_- \;=\; \mathbb{R}(ie_0) \;\oplus\; \mathfrak{su}(2),
$$

so the compact algebra present is $\mathfrak{u}(1)\oplus\mathfrak{su}(2) = \mathfrak{u}(2)$, of real dimension $4$. This is exactly the anti-Hermitian subspace of $\mathbb{B}\cong M_2(\mathbb{C})$: anti-Hermitian $2\times2$ complex matrices *are* $\mathfrak{u}(2)$, and the Cartan decomposition of the real Lie algebra $\mathfrak{gl}(2,\mathbb{C})$ is

$$
\mathfrak{gl}(2,\mathbb{C}) \;=\; \mathfrak{u}(2) \;\oplus\; i\,\mathfrak{u}(2),
\qquad \dim_\mathbb{R} = 4 + 4 = 8,
$$

with $[\mathfrak{u}(2),\mathfrak{u}(2)]\subseteq\mathfrak{u}(2)$ and $[\mathfrak{u}(2),i\mathfrak{u}(2)]\subseteq i\mathfrak{u}(2)$. The decomposition was checked on a basis of $\mathfrak{u}(2)$ and the brackets close as stated. Because every compact subalgebra of a real Lie algebra lies in a maximal compact subalgebra, and the maximal compact subalgebra of $\mathfrak{gl}(2,\mathbb{C})$ is $\mathfrak{u}(2)$, **any gauge algebra that is a subalgebra of $\mathbb{B}$ under the commutator has real dimension at most $4$.**

The matter side has the matching ceiling. The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is simple and Artinian, so every module is a direct sum of copies of its unique simple module, which is $\mathbb{C}^2$. Consequently **every $\mathbb{B}$-module has complex dimension divisible by two.** A colour triplet — a complex three-dimensional internal space for the quark — is not a $\mathbb{B}$-module.

$$
\dim_\mathbb{C} M = 2k \ \ (k \in \mathbb{Z}_{\ge 0}) \quad\text{for every } \mathbb{B}\text{-module } M,
\qquad\text{so } \dim_\mathbb{C} = 3 \text{ is impossible.}
$$

This is the precise ceiling of the present construction, and it is what makes the colour group an obstacle rather than a gap with a known route. It is not a failure of the framework's arithmetic; it is a statement about the carrier. The non-abelian machinery is real, and it is real for $\mathfrak{u}(2)$; colour needs a compact simple algebra of dimension $8$ and a three-dimensional module, and neither is available in $\mathbb{B}$ on the present construction.

### The chiral-fermion issue

The read-list article *Chiral Fermions in the Biquaternion Framework* establishes the following, and this agenda inherits it without change.

The Dirac module is $\Delta = S\oplus\bar{S}$, $S=\mathbb{C}^2$; the chirality operator is $\gamma_5 = \mathrm{diag}(-I_2,I_2)$ with $\gamma_5^2 = I_4$, and the projectors $P_L = \tfrac12(I_4-\gamma_5)$, $P_R = \tfrac12(I_4+\gamma_5)$ are idempotent, orthogonal, complete, of rank two, and Lorentz invariant. These were rechecked on the read-list's representation: $P_L^2=P_L$, $P_R^2=P_R$, $P_LP_R=0$, $P_L+P_R=I_4$, $\gamma_5$ anticommutes with each generator and commutes with every even product, hence with the Lorentz action. The Dirac mass bilinear $\bar\Psi\Psi = \psi_L^\dagger\psi_R + \psi_R^\dagger\psi_L$ is chirality-odd and vanishes on a state of definite chirality. On the module a chiral abelian symmetry with independent charges is consistent, with $D_\mu = \partial_\mu + \tfrac{i}{\hbar}A_\mu Q$, $Q = q_LP_L+q_RP_R$; the mass bilinear is gauge invariant **if and only if $q_L = q_R$**.

Two further results of that article are the ones that bear on QCD.

- **The canonically available gauge group is vector-like.** The framework's own abelian gauge group is the unitary part of the center $\mathbb{C}_{\mathbb{B}}$, which acts as a *scalar* on $M_2(\mathbb{C})$; every component of the module receives the same charge. Chirality requires a non-central action, hence a non-abelian gauge structure — the structure the non-abelian article supplies for $\mathfrak{su}(2)$ but does not dress with matter.
- **The framework's mass term is chirality-exchanging.** The massive Dirac equation is the linear chiral pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$, whose mass term couples the two chiral halves off-diagonally; it is the real-form expression of an ordinary Dirac mass. Because it couples the two chiralities it breaks the **axial** (chiral) symmetry, $\partial_\mu j_5^\mu = 2im\,\bar{\tilde{\Psi}}\gamma_5\tilde{\Psi}$, while the vector phase $U(1)$ — fermion number — passes through the linear mass and is exact for the massive field. A genuinely antilinear Majorana-type pairing lives instead on the algebra's real structure $\flat = -\tilde{\Psi}^{\dagger}$ and on the separate single-field equation built on it, whose plane waves lie on the spacelike locus.

Finally, the article states that no biquaternion formulation of the anomaly is attempted anywhere in the series. The anomaly is the place where QCD's chirality is physically indispensable.

### The reach of the renormalization group

The series **does** contain a renormalization-group article, *The Renormalization Group in Biquaternionic Form*, and it **does** reach the non-abelian case. It performs the shell integration and obtains the standard one-loop gauge beta function

$$
\beta_g = -\frac{g^3}{16\pi^2}\,b_0, \qquad b_0 = \frac{11}{3}C_2(G) - \frac{2}{3}\sum_{\text{Weyl}}T(r),
$$

negative for pure $SU(N)$, with $C_2(G) = N$ recomputed from the structure constants on both $SU(2)$ and $SU(3)$ — the independent-case check the corpus's discipline requires. For $SU(3)$ with $N_f$ Dirac quark flavours, each flavour contributing two Weyl fermions of index $T=\tfrac12$, this is $b_0 = 11 - \tfrac{2}{3}N_f$; the arithmetic gives $b_0>0$ — asymptotic freedom — for $N_f < \tfrac{33}{2}$, and the two-loop Banks–Zaks fixed point is computed as well. The article's own framing, however, is explicit: the effective action, the measure, the regulator, the gauge group, the matter content, and the coupling values are all **inputs**; the beta functions are **transcribed** from standard field theory and would not change if $\mathbb{B}$ were replaced by any other notation for complexified four-dimensional spacetime. The flow acts on central scalars only, so the framework's regulator is sector-blind, and its algebraically natural sharp cutoff breaks gauge invariance while the gauge-safe regulator (dimensional regularisation) is external to the four-dimensional algebra.

For QCD this means: the *form* of the running and the *sign* of the non-abelian beta function have been written in biquaternion notation, and the standard QCD threshold has been reproduced, but the colour group and the quark content that give them meaning are still the missing objects of the previous sections.

## The Colour Group: Nothing Derives a Three

QCD begins with a group. The colour group is $SU(3)$, its rank-two simple compact algebra $\mathfrak{su}(3)$ has real dimension $8$, and the quarks sit in its complex three-dimensional fundamental representation $\mathbf{3}$ while the gluons sit in the eight-dimensional adjoint. Nothing in the biquaternion series supplies any of this. This section states precisely what is and is not available, and it distinguishes a derivation from a positing.

**What is available.** From the preceding section: the compact algebra available in $\mathbb{B}$ is $\mathfrak{u}(2)$ at most, of dimension $4$; the unique simple module is $\mathbb{C}^2$; and every $\mathbb{B}$-module has even complex dimension. The tempting identifications of "three" in the framework are all false leads, and it is worth naming them so that they are not mistaken for a route:

- **The three quaternion units $e_1,e_2,e_3$.** There are three of them, but they span the **adjoint** of $\mathfrak{su}(2)$ — the spin-one representation — not a complex triplet. $SU(2)$ has no complex three-dimensional representation, and its fundamental is two-dimensional. Counting three basis vectors is not constructing colour.
- **The two chiralities, the two Peirce ideals, the two sectors.** These give a $\mathbb{Z}_2$, not a $\mathbb{Z}_3$. The complexification $\mathbb{C}\otimes_\mathbb{R}\mathbb{B}\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C})$ has two simple summands; the Peirce decomposition $\mathbb{B} = \mathbb{B}p\oplus\mathbb{B}q$ has two summands; the sectors are two. Nothing in the corpus produces a triple.
- **The three components of the complement of the light cone.** The zero-divisor cone gives a three-part classification of intervals (timelike, spacelike, null) and the complement of the cone has three connected components. A partition of a cone is not a group, and interval type is not an internal quantum number.
- **The dimension count $8 = 8$.** Both $\mathbb{B}$ and $\mathfrak{su}(3)$ are eight-real-dimensional, but $\mathbb{B}$'s compact part is $\mathfrak{u}(2)$ and its module is two-dimensional. Equality of dimensions is a coincidence of counting, not an embedding.

**What positing would and would not be.** One can of course write down a colour group and tensor it on: take the matter field to be $\psi\otimes c$ with $c\in\mathbb{C}^3$, let $SU(3)$ act on $c$ and $\mathbb{B}$ act on the spinor index, and build a connection valued in $\mathfrak{su}(3)$ on the colour factor. That constructs *a* theory with colour, and it is exactly the move through which the corpus already passes once: the chiral-fermion article writes its abelian chiral connection as "a connection valued in the algebra of module endomorphisms", i.e. on an enlarged carrier rather than inside $\mathbb{B}$. But it is an **adjoining of an independent factor**, and adjoining $\mathbb{C}^3$ is not deriving it. The framework fixes neither the dimension three, nor the group $SU(3)$, nor the reason the factor should exist at all. To posit $SU(3)$ and then present the resulting construction as the framework's colour theory is precisely the fabrication the agenda must not commit.

**The one candidate route, stated as a candidate.** If colour is to come from the framework rather than be added to it, the construction must be enlarged in a way the algebra *forces*. Two shapes of such an enlargement are conceivable. The first is to let the carrier be the endomorphism algebra of a $\mathbb{B}$-module or of a tensor product $S\otimes X$, where $X$ is an internal space whose dimension the algebra somehow determines; since $\mathrm{End}(\Delta)\cong M_4(\mathbb{C})$ and $\mathrm{End}(S\otimes\mathbb{C}^3)\cong M_6(\mathbb{C})$ both contain $\mathfrak{su}(3)$, the group can live there — the question is what fixes $X$. The second is to look for a rank-two compact structure already inside $\mathbb{B}$'s representation theory, for instance in the decomposition of tensor powers or in the complexification, on the chance that an $\mathfrak{su}(3)$ subalgebra of some natural endomorphism algebra appears. Neither of these is a route yet. The first assumes the answer ($X=\mathbb{C}^3$); the second is a search with no known outcome, and the ceiling argument of the preceding section is evidence against it. The honest classification is therefore **no route yet**, with the candidate named so that it can be tried rather than forgotten.

**What would settle it.** A theorem of one of two forms would settle the colour-group question, and either outcome is a result:

- **Positive.** An algebra-internal construction that produces a rank-two compact gauge algebra and a complex three-dimensional internal module from $\mathbb{B}$'s own structures — its ideals, its zero divisors, its tensor powers, or its complexification — together with a **selection principle** that fixes $N_c = 3$. A construction of the group without a principle that selects three does not settle it, because the framework would then host a continuum of colour groups.
- **Negative.** A no-go theorem covering not only $\mathbb{B}$-valued connections but all $\mathbb{B}$-invariant enlargements, showing that any colour group must be adjoined as an independent factor. A negative result settles the question by relocating it: colour would then be an input, and the framework's contribution to QCD would be limited to whatever the general non-abelian machinery adds once colour is supplied.

Until one of these exists, the colour group stays open, and every use of it below is flagged.

## Confinement: No Mechanism

Confinement is the defining feature of QCD: quarks and gluons are not observed as isolated states, the potential between a separated colour pair grows linearly, and the spectrum contains only colour-singlet states. If a framework claims to contain a colour theory, confinement is the first thing that must be accounted for. The biquaternion framework does not account for it, and the honest statement is stronger than "the mechanism is unproven": **no mechanism has been proposed.** This is not a gap with a known route; it is an obstacle with no route yet.

Four things that would be needed are all absent.

- **A non-perturbative formulation.** The renormalization-group article is a perturbative calculation: a one-loop shell integration, one- and two-loop beta functions, and the Gaussian and Banks–Zaks fixed points. Asymptotic freedom is an ultraviolet statement; confinement is an infrared statement. A perturbative beta function, however accurately transcribed, has no bearing on it.
- **A Wilson loop, or something equivalent.** The standard non-perturbative diagnostic is the Wilson loop $W(C) = \mathrm{Tr}\,\mathcal{P}\exp\!\oint_C \mathcal{A}$, whose large-loop behaviour $\langle W(C)\rangle \sim e^{-\sigma A(C)}$ is the area law, with $\sigma$ the string tension. No Wilson loop is defined anywhere in the series, and it cannot be defined without the measure the path-integral article places outside finite-dimensional $\mathbb{B}$.
- **A gauge-invariant regulator.** The renormalization-group article records that the algebra's natural cutoff is central, sector-blind, and breaks gauge invariance, while dimensional regularisation leaves the four-dimensional algebra; a biquaternionic gauge-invariant regulator is itself an open problem. Non-perturbative gauge theory, on the lattice or otherwise, requires such a regulator, so confinement cannot even be posed before that gap is closed.
- **A gauge-fixing principle and a mass gap.** The canonical-quantization article on the Maxwell field records that the framework cannot fix the gauge naturally, and no gauge-fixing principle is supplied. No mass gap — the statement that the spectrum has a lowest positive mass — is established or even formulated.

The framework's closest structures are the zero divisor cone and the null four-vectors of $\mathbb{M}_-$. It is worth saying why they do not help. The light cone is a statement about the norm form of a biquaternion; it classifies momenta and propagation directions. Confinement is a statement about the energy of a *configuration of colour sources* — a potential that grows with separation. A null direction is not an area law, and the fact that a massless field propagates on the light cone says nothing about the force between two colour charges. The zero-divisor structure is a genuine feature of the algebra, but reading confinement from it would be an analogy, not a derivation, and the analogy is not made here.

**What would settle it.** A framework-internal object whose computed behaviour establishes either the area law or its absence. Concretely: define a biquaternionic Wilson loop on the enlarged carrier that the colour-group question settles, and compute its large-loop asymptotics, exhibiting a string tension $\sigma>0$; or exhibit a mass gap in the framework's spectrum; or prove that no such object can be defined in $\mathbb{B}$, which settles the question negatively and shows that confinement, like the colour group, must be imported. All three require, as a prerequisite, the action, measure, and gauge-invariant regulator that the series does not yet have — which is why confinement is downstream of apparatus as well as of the colour group.

## The Chiral-Fermion Issue and the Quark Couplings

The chiral-fermion issue is inherited from the read-list article and carried unchanged. It has three parts: the module's chirality structure is exact, the framework's canonically available gauge group is vector-like and cannot be chiral, and the framework's own mass term is a linear off-diagonal chirality coupling that breaks the axial symmetry while leaving the vector $U(1)$ exact.

The question for this agenda is how much of that is a *QCD* obstacle. The answer requires care, because one natural reading of the issue does not apply to colour and another does.

**The gauge-chirality obstruction is not itself a colour obstruction.** Colour is a **vector-like** interaction: the left- and right-handed components of a quark carry the *same* colour representation, so a colour gauge transformation acts identically on $\psi_L$ and $\psi_R$. The chiral-fermion article's finding that the center is scalar and vector-like, and cannot generate a chiral gauge group, is therefore not an obstruction to colour; if anything it is the opposite, since a vector-like action is exactly what colour needs. It is worth saying this plainly so that the chiral-fermion result is not over-read: the framework's inability to make a *chiral gauge group* bears on the electroweak sector, not on colour.

**What does bear on QCD is the missing colour representation of the quark.** The chiral-fermion article constructs its chiral covariant derivative on the module for an *abelian* phase, with a charge operator $Q = q_LP_L + q_RP_R$. The non-abelian article constructs a connection with values in $\mathfrak{su}(2)$ but explicitly leaves the matter representation open: its open question 3 states that for a non-abelian connection the left and right actions differ and the representation carried by the matter field must be specified, and that the non-abelian charge operator is not constructed. QCD needs the quark in the **fundamental of the colour group**, with the covariant derivative acting on the colour index. By the ceiling of §"The Colour Group", a colour triplet is not a $\mathbb{B}$-module, so this representation must live on an enlarged carrier. The matter representation and the colour group therefore share a single settling object: a construction, on whatever carrier is justified, of a field transforming in the colour fundamental with the connection acting on the internal index.

**The global chiral sector of QCD is a further, distinct obstacle.** Beyond the gauge representation, the quarks carry an approximate global chiral symmetry $SU(N_f)_L\times SU(N_f)_R$ (for the light flavours), which is spontaneously broken and whose consequences — light Goldstone pions, the $\eta'$ mass, the axial anomaly, the $\theta$-vacuum — are central to QCD. The framework supplies the chirality operator and the projectors on the module, and it records that the chirality label is invisible to $\mathbb{B}$ alone and appears only through the real structure or the complexification. What it does not supply is any computation of the **anomaly**: the chiral-fermion article states explicitly that no biquaternion formulation of the anomaly is attempted, and names the instanton/soliton article as its natural home. The anomaly is not decoration; it is what makes the flavour-singlet axial current non-conserved and gives the $\eta'$ its mass, and anomaly cancellation is a consistency condition on a chiral spectrum. Whether the framework reproduces the anomaly coefficient, and whether it has anything to say about the $\theta$-angle and strong $CP$, is unaddressed.

**The framework's mass term interacts with both.** The massive biquaternion Dirac equation is the linear chiral pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$, whose mass term couples the two chiral halves off-diagonally; it is the real-form expression of an ordinary Dirac mass, so the reading is settled. The framework therefore carries a conserved fermion number — the central phase passes through the linear mass and the vector $U(1)$ is exact for the massive field — and what the mass breaks is the **axial** charge, $\partial_\mu j_5^\mu = 2im\,\bar{\tilde{\Psi}}\gamma_5\tilde{\Psi}$, vanishing only at $m = 0$. That is the framework's transcription of exactly the chiral-symmetry breaking that organises the light-hadron spectrum, though the framework derives no condensate, no Goldstone pions, and no anomaly coefficient. The genuinely antilinear pairing lives on the algebra's real structure $\flat$ and on the separate single-field equation built on it, whose plane waves lie on the spacelike locus; that is a different equation from the parent's, and it is not the framework's mass term.

**What would settle it.** Three computations, in order of dependence:

1. **The colour representation of the quark.** Construct the matter field on the carrier that the colour-group question settles, with the covariant derivative acting on the internal colour index, and check its gauge covariance. This is the same object as obstacle 1's, and it has a known route *conditional on that carrier existing*; without the carrier it is blocked.
2. **The anomaly.** Compute the divergence of the axial current, or the triangle diagram, on the biquaternion module, and compare the coefficient with the standard result. The standard computation defines the target; the framework must reproduce it or fail to, and either is a result. This is a **known route in standard field theory with no framework realisation yet**.
3. **The mass reading.** Largely settled on the parent's equation: the mass term is the linear chiral pair, the real-form expression of an ordinary Dirac mass, so the framework carries a conserved fermion number and what the mass breaks is the axial charge. What remains open is the separate question the chiral-fermion article poses — how the algebra's real structure $\flat$, and the single-field equation $\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^{\flat}$ built on it, read on the real module, and whether that real-form choice is what distinguishes a Majorana from a Dirac fermion.

## The Running Coupling and Asymptotic Freedom

This is the one obstacle for which the series has already built the machinery and reached the non-abelian case, and the honest statement is therefore different from the preceding two. The renormalization-group article performs the one-loop shell integration for a non-abelian gauge coupling, obtains $\beta_g = -(g^3/16\pi^2)b_0$ with $b_0 = \tfrac{11}{3}C_2(G) - \tfrac{2}{3}\sum_{\text{Weyl}}T(r)$, recomputes $C_2(G)=N$ on $SU(2)$ and $SU(3)$, and reproduces the QCD values $b_0 = 11-\tfrac{2}{3}N_f$ for $SU(3)$ with $N_f$ Dirac flavours, the asymptotic-freedom threshold $N_f < \tfrac{33}{2}$, and the two-loop Banks–Zaks fixed point. The sign of the non-abelian beta function is the correct one and was checked on independent cases, which is the corpus's verification discipline.

What the article also records, in its own words, is that this is a **transcription**: the effective action, the measure, the regulator, the gauge group, the matter content, and the value of the coupling are all inputs; the beta functions are standard field theory written in biquaternion notation and would not change if $\mathbb{B}$ were replaced by any other notation. Two framework-specific limitations follow directly.

- **The flow acts on central scalars.** The scale $\mu$, the couplings, and the beta functions are real multiples of $e_0$, i.e. central, hence in $\mathbb{M}_+$. The flow rescales central coefficients and does not rotate one sector into the other. It cannot, for example, generate a sector-sensitive scale, and it gives no handle on the medium-dependent local complex structure $c=1/\sqrt{\epsilon\mu}$, which the article records as an open question.
- **The regulator is external, and the natural one breaks gauge invariance.** The algebra hosts the central invariant $\tilde{k}\bar{\tilde{k}}$ on which a cutoff is imposed, but not the cutoff; the sharp cutoff is not gauge invariant, and dimensional regularisation leaves the four-dimensional algebra. A biquaternionic gauge-invariant regulator is an open problem. For a *perturbative* one- and two-loop running this is manageable in transcription; for anything non-perturbative it is disabling.

So the running coupling and asymptotic freedom are an obstacle with a **known route** — the route is the standard one-loop computation, and it has been carried out in the framework's notation — but the route's *inputs* are exactly the missing objects: the colour group (obstacle 1) and the quark content (obstacle 3). In addition, the route reaches only the perturbative ultraviolet; it says nothing about confinement, which is the infrared companion of asymptotic freedom and is the obstacle with no route.

**What would settle it.** Fixing $C_2(G)$ and $T(r)$ for the framework's own gauge group and matter, i.e. settling obstacles 1 and 3, and supplying the $\mathbb{B}$-valued action, measure, and gauge-invariant regulator that the renormalization-group article names as absent. With those, the running $\alpha_s(\mu)$ is fixed by the framework rather than imported, and the sign of the beta function becomes a computed prediction to be checked rather than a transcribed standard result. A second, independent settling object is a **non-perturbative** computation that connects the asymptotically free ultraviolet to the confining infrared — a lattice or gap-equation analogue on the framework's carrier — because the two-loop perturbative flow alone cannot. As with the other obstacles, a negative result would also settle it: a demonstration that the framework's central flow cannot accommodate a sector-specific or non-perturbative structure would show that QCD's renormalization structure is imported wholesale.

## The Ledger

The table collects the items of the agenda and sorts each into the three-way classification. "Established" means recomputed in the series and inherited here; "known route" means the object does not exist but the computation that would produce it is identifiable; "no route yet" means no mechanism has been proposed.

| Item | Status | Object or computation that would settle it |
|---|---|---|
| Non-abelian gauge construction: connection, curvature with $[\mathcal{A},\mathcal{A}]$, adjoint law, Bianchi identity, gauge-invariant Yang–Mills density | Established | — |
| Available compact gauge algebra $\mathfrak{u}(1)\oplus\mathfrak{su}(2)=\mathfrak{u}(2)$, the maximal compact subalgebra of $\mathbb{B}$ | Established | — |
| No $\mathfrak{su}(3)$ subalgebra and no three-dimensional $\mathbb{B}$-module within the present construction | Established (within the $\mathbb{B}$-valued construction) | A positive internal construction with a principle selecting $N_c=3$, or a no-go covering all $\mathbb{B}$-invariant enlargements |
| Colour group $SU(3)$ and the number of colours $N_c=3$ | **No route yet** | The two theorems above; positing is not a route |
| Chirality structure on the module; vector-like center; mass selection rule $q_L=q_R$ | Established | — |
| Colour fundamental representation of the quark (internal index, covariant derivative) | Known route, blocked on the carrier | Construct the matter field on the settled carrier and verify gauge covariance |
| Confinement: area law, string tension, mass gap | **No route yet** | A biquaternionic Wilson loop with an area law, or a mass gap, or a no-go; prerequisite: action, measure, gauge-invariant regulator |
| Non-perturbative apparatus: $\mathbb{B}$-valued action, measure, gauge-invariant regulator | **No route yet** | An action and a regulator that live in the algebra and preserve gauge invariance |
| Running coupling and asymptotic freedom beyond transcription | Known route, blocked on inputs | Fix $C_2(G)$ and $T(r)$ from the framework's own group and matter; supply the action, measure, and regulator |
| Axial anomaly, $U(1)_A$ problem, $\theta$-vacuum, strong $CP$ | Known route in standard field theory; no framework realisation | A biquaternion computation of the axial-current divergence or the triangle diagram |
| The framework's mass term: linear off-diagonal chirality coupling (vector $U(1)$ exact, axial broken) | Established | The linear chiral pair; the separate $\flat$-pairing on the single-field equation is a distinct, still-open reading |

| Empirical contact | Open | A prediction distinguishing the framework from standard QCD |

## What Would Settle It

The obstacles are not independent, and the dependency chain is short. The quark's colour representation (obstacle 3) needs the carrier that the colour group (obstacle 1) would supply; the running coupling (obstacle 4) needs both, plus the action and regulator; confinement (obstacle 2) needs the action and regulator and, to be a statement about colour at all, needs the colour group. Two items are therefore upstream of everything else.

1. **A derivation or a justified fixing of the internal colour structure.** Either colour comes out of $\mathbb{B}$ — a rank-two compact algebra and a three-dimensional internal module, with a principle that selects three — or it is shown that colour must be adjoined as an independent factor. Either outcome converts the framework's relation to QCD from "unknown" to "stated". The one thing that does not convert it is writing $SU(3)$ down and proceeding; that is the fabricated premise the agenda exists to prevent.
2. **A $\mathbb{B}$-valued action with a gauge-invariant regulator.** The renormalization-group article names the absent action, measure, and regulator, and the confinement section shows they are prerequisites for even posing the area law. Until they exist, every QCD computation in the framework is a transcription of a standard one, and every non-perturbative statement is unavailable.

With those two settled, the rest of the agenda becomes ordinary work: construct the quark representation, compute the anomaly, run the colour coupling, and look for the area law. Without them, the honest summary of the framework's relation to QCD is the one this article opened with: it has the general non-abelian gauge machinery, it has an exact chirality structure on the Dirac module, it has the form of the running coupling, and it does not have a colour theory.

Finally, the genre's standing caution applies here in its strongest form. *The Empirical Status of the Biquaternion Framework* records that on every domain developed, the framework is so far empirically equivalent to the standard theory it reformulates. A biquaternionic colour theory, if one is ever constructed, would inherit that position unless it makes a prediction standard QCD does not; and a theory whose colour group, matter content, coupling, and confinement mechanism are all imported has no prospect of doing so. The agenda's most useful output may be to make that consequence visible early, rather than to produce a construction that appears to answer QCD while assuming all of it.

## Summary

This article is a research agenda for quantum chromodynamics inside the biquaternion framework. Its finding is that the framework reaches the general machinery of a non-abelian gauge theory and stops before colour.

What is established is recalled: the non-abelian gauge construction, with a connection transforming in the adjoint, a curvature containing the commutator term and satisfying the Bianchi identity, and a gauge-invariant Yang–Mills density, built on the $\mathfrak{su}(2)$ factor of the material sector; the Lie-algebra decomposition $\mathbb{M}_- = \mathbb{R}(ie_0)\oplus\mathfrak{su}(2)$, so that the compact algebra available is $\mathfrak{u}(2)$; the chiral structure on the Dirac module, with exact projectors, a chirality-odd mass bilinear, and the selection rule $q_L=q_R$; the vector-like character of the center; and a renormalization-group article that does reach the non-abelian case and reproduces the standard one-loop beta function, $C_2(G)=N$, the QCD coefficient $b_0=11-\tfrac{2}{3}N_f$, and the asymptotic-freedom threshold — as a transcription.

What is not established is everything QCD-specific.

- **The colour group.** Nothing derives $SU(3)$ or any three-valued internal structure. Within the framework's construction the compact algebra is at most $\mathfrak{u}(2)$ of dimension $4$, and every $\mathbb{B}$-module has even complex dimension, so no $\mathfrak{su}(3)$ subalgebra and no colour triplet are available. Positing $SU(3)$ is not deriving it. **No route yet**, with the enlarged-carrier construction named as the only candidate.
- **Confinement.** No mechanism has been proposed. The perturbative renormalization group is an ultraviolet result and has no bearing on the infrared area law; there is no Wilson loop, no gauge-invariant regulator, no mass gap, and no gauge-fixing principle. **No route yet.**
- **The chiral-fermion issue.** Its gauge-chirality half does not obstruct colour, because colour is vector-like; but the quark's colour representation is unbuilt, the axial anomaly has no framework formulation, and the framework's mass term, being the linear chirality coupling, breaks the axial charge while leaving fermion number exact.

- **The running coupling.** The series has the machinery and reaches the non-abelian case, but the gauge group, matter content, action, measure, and regulator are all inputs. **Known route, blocked on the very objects the other obstacles are missing.**

The two upstream items are a derivation (or a justified fixing) of the internal colour structure and a $\mathbb{B}$-valued action with a gauge-invariant regulator. Everything else depends on them. The article commits throughout to the agenda's central discipline: no section assumes a colour group, and where standard QCD numbers appear, they are marked as imports.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H} \cong M_2(\mathbb{C})$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_1e_2=e_3$ |
| $i$ | Scalar imaginary, $i^2=-1$, central |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors; $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ | Center of the algebra; the vector-like abelian factor |
| $\tilde{\nabla} = e_0\partial_{ict}+e_k\partial_k$ | Biquaternionic gradient |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$ | d'Alembertian |
| $[e_a,e_b]=2\varepsilon_{abc}e_c$, $T_a=\tfrac12 e_a$ | Commutator and normalized generators of $\mathfrak{su}(2)\subset\mathbb{M}_-$ |
| $\mathcal{A}_\mu\in\mathfrak{su}(2)$, $\kappa=q/\hbar$ | Non-abelian connection and coupling (read list) |
| $F_{\mu\nu}=\partial_\mu\mathcal{A}_\nu-\partial_\nu\mathcal{A}_\mu+i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$ | Non-abelian field strength |
| $F'_{\mu\nu}=UF_{\mu\nu}U^{-1}$, $[D_\mu,D_\nu]=i\kappa F_{\mu\nu}$ | Adjoint transformation law and curvature identity |
| $\mathbb{M}_- = \mathbb{R}(ie_0)\oplus\mathfrak{su}(2)$, $\mathfrak{u}(2)=\mathfrak{u}(1)\oplus\mathfrak{su}(2)$ | Available compact gauge algebra (dimension 4) |
| $\mathfrak{gl}(2,\mathbb{C}) = \mathfrak{u}(2)\oplus i\,\mathfrak{u}(2)$ | Cartan decomposition fixing the ceiling: maximal compact subalgebra $\mathfrak{u}(2)$ |
| $\Delta = S\oplus\bar{S}$, $S=\mathbb{C}^2$ | Dirac module and its unique simple summand; every $\mathbb{B}$-module has dimension $2k$ |
| $\gamma_5$, $P_L=\tfrac12(I_4-\gamma_5)$, $P_R=\tfrac12(I_4+\gamma_5)$ | Chirality operator and projectors (read list) |
| $\bar\Psi\Psi$, $Q=q_LP_L+q_RP_R$ | Chirality-odd mass bilinear; chiral charge operator; selection rule $q_L=q_R$ |
| $\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L=m\tilde{\Psi}_R$; $\tilde{\Psi}^{\flat}=-\tilde{\Psi}^{\dagger}$ | Mass term: linear off-diagonal chirality coupling; $\flat$ is the algebra's real structure, not the mass |

| $\tilde{k}\bar{\tilde{k}}$ | Central norm-form invariant; the cutoff is imposed on it |
| $\beta_g=-(g^3/16\pi^2)b_0$, $b_0=\tfrac{11}{3}C_2(G)-\tfrac{2}{3}\sum_{\text{Weyl}}T(r)$ | Non-abelian one-loop beta function (transcribed) |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Inherited informational trace formula |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| **Standard QCD notation, not framework objects** | |
| $SU(3)$, $\mathfrak{su}(3)$ (dimension $8$, rank $2$) | Colour group and algebra — no route yet |
| $N_c=3$, $\mathbf{3}$, $\mathbf{8}$ | Number of colours; quark fundamental; gluon adjoint — no route yet |
| $N_f$, $\alpha_s$ | Quark flavour number and strong coupling — inputs, not derived |
| $W(C)$, $\sigma$, $\langle W(C)\rangle\sim e^{-\sigma A(C)}$ | Wilson loop, string tension, area law — not defined in the series |

## Further Reading

- *Non-Abelian Gauge Fields in Biquaternionic Form* — the immediate parent; the connection, the adjoint curvature, the Bianchi identity, the gauge-invariant density, and the open matter-representation question this agenda inherits.
- *The Gauge Principle in Biquaternionic Form* — the abelian origin of the connection and the reality-condition gap the non-abelian construction takes up.
- *Chiral Fermions in the Biquaternion Framework* — the module's chirality structure, the vector-like center, the mass selection rule, the linear chirality-coupling mass term, and the unformulated anomaly.

- *The Renormalization Group in Biquaternionic Form* — the one-loop non-abelian beta function, $C_2(G)=N$, the QCD coefficient and threshold, and the article's own statement that these are transcribed with the group and matter as inputs; the source of the running-coupling item.
- *The Covariant Derivative and Gauge Connection in Biquaternionic Form* — the abelian connection whose non-abelian extension is the parent's starting point.
- *The Dirac Equation in Biquaternionic Form* and *The Spinor Module in Biquaternionic Form and Its Lorentz Action* — the spinor module, the linear chiral mass term, and the real-structure origin of chirality.

- *Canonical Quantization of the Biquaternion Maxwell Field* — the framework's inability to fix the gauge, a prerequisite the confinement item needs.
- *Biquaternion Representation Theory* and *Lie Algebras: A General Introduction* — the module structure and the compact-subalgebra facts behind the ceiling on the colour group.
- *Biquaternion Zero Divisors* and *Biquaternion Topology* — the null cone and the bivector structure, the objects closest to the confinement and topological-charge items.
- *The Lorentz Group in Biquaternionic Form — Structure and Representations* — the representation theory on which the adjoint and fundamental bookkeeping rests.
- *The Spinor-Helicity Formalism and Biquaternions* — the corpus's explicit statement that the framework "does not contain a colored gauge theory"; the transcription boundary this agenda makes systematic.
- *The Empirical Status of the Biquaternion Framework* — the standing empirical-equivalence result, the caution under which any biquaternionic QCD would labour.
- *The Einstein Field Equations under the Biquaternion Framework — A Research Agenda* — the companion agenda whose three-way classification and settling-object discipline this article follows.
