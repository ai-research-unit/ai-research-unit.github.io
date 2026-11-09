# __Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda__

## Introduction

**Quantum chromodynamics** (QCD) is the non-abelian gauge theory of the colour interaction: a gauge theory with group $SU(3)$, quarks in the fundamental three-dimensional representation, gluons in the adjoint, a coupling that becomes weak at short distances, and a spectrum from which the coloured states are absent — confinement. This article is a research agenda for QCD inside the biquaternion framework. Its subject is not a result; it is the boundary between what the framework has built and what QCD requires.

The starting position is stated at the outset, because the whole agenda depends on it and because it is easy to overstate.

- **The framework has a non-abelian gauge construction.** It has a connection, a curvature with the commutator term, the adjoint transformation law, the Bianchi identity, and a gauge-invariant Yang–Mills density, developed inside the algebra for a gauge algebra that is present in the material sector. This is established and is recalled in the next section.
- **The framework records a chiral-fermion issue.** The field $\tilde{Ξ}_{\mathrm{sp}}$ splits into the two values $L$ and $R$, and its mass bilinear is odd under their exchange; the gauge group drawn from the algebra's centre is vector-like and cannot be chiral; and the interpretation of the separate conjugate-pairing (Majorana-type) term built on the algebra's real structure is open. This is established, and it is inherited here unchanged.
- **The framework has not constructed a colour theory.** Nothing in the series derives $SU(3)$, and nothing derives any three-valued internal structure that could play the role of colour. The word "colour" occurs in the corpus only where standard QCD is being transcribed — in the renormalization-group article, which imports the $SU(3)$ one-loop coefficients, and in the helicity-formalism article, which states plainly that the framework "does not contain a colored gauge theory". No article derives a colour group, a quark colour triplet, a gluon octet, a confinement mechanism, or a colour coupling.

The discipline this forces on the article is the one the genre requires: **an agenda that quietly assumes a colour group has fabricated its premise.** The colour group is therefore carried as an **open item throughout**, never as a working assumption. Wherever a standard QCD statement is written down — $N_c=3$, $b_0 = 11 - \tfrac{2}{3}N_f$, the area law — it is flagged as standard input, not as a framework result.

**The three-way classification.** The article sorts every item into one of three categories, and the distinction is the point of the agenda.

1. **Established.**
2. **Obstacle with a known route.** The object does not exist, but the route to it is identifiable, usually because standard field theory supplies the computation and the framework must reproduce it on its own carrier.
3. **Obstacle with no route yet.** No mechanism has been proposed, and naming an object is not the same as having a route to it. Confinement and the colour group are in this class.

The four obstacles the agenda treats are the **colour group** (§"The Colour Group"), **confinement** (§"Confinement"), the **chiral-fermion issue** as it bears on the quark couplings (§"The Chiral-Fermion Issue"), and the **running coupling and asymptotic freedom** (§"The Running Coupling"). They are not independent: the last needs the first and the third, and confinement needs apparatus all of them need. A closing ledger collects them, and a short synthesis names the two upstream items.

## What the Framework Already Reaches

### The non-abelian gauge construction

The read-list article *Non-Abelian Gauge Fields in Biquaternionic Form* builds the general non-abelian gauge structure inside $\mathbb{B}$. Its results are established and are used here unchanged.

The vector part of the material sector, $\mathrm{span}_\mathbb{R}\{\vec e_x,\vec e_y,\vec e_z\}$, closes under the commutator and is $\mathrm{SU}(2)$ in a non-standard normalization,

$$
[e_a,e_b] = 2\,\varepsilon_{abc}\,e_c, \qquad a,b,c = 1,2,3,
\qquad T_a = \tfrac12 e_a,\quad [T_a,T_b] = \varepsilon_{abc}T_c,\quad \mathrm{Tr}(T_aT_b) = -\tfrac12\delta_{ab}.
$$

The gauge group is the unit real quaternions, $SU(2) = \{\tilde U \in \mathbb{B}_{H} : \tilde U\bar{\tilde U} = e_t\}$, acting on a matter field by left multiplication. A local transformation $\tilde U(\tilde{Q})$ forces the connection

$$
\mathcal{A}_{2,\mu} = \tilde U\,\mathcal{A}_\mu\,\tilde U^{-1} + \frac{i}{\kappa}\,(\partial/\partial R_\mu \tilde U)\,\tilde U^{-1},
$$

which reduces to the abelian law $\tilde{A}_{\Phi,2} = \tilde{A}_{\Phi} - \tilde{\nabla}\Lambda$ when $\tilde U=e^{i\kappa\Lambda}$ is central. The field strength

$$
F_{\mu\nu} = \partial/\partial R_\mu \mathcal{A}_\nu - \partial/\partial R_\nu \mathcal{A}_\mu + i\kappa\,[\mathcal{A}_\mu, \mathcal{A}_\nu],
\qquad
F = d\mathcal{A} + i\kappa\,\mathcal{A}\wedge\mathcal{A},
\qquad
[D_\mu,D_\nu] = i\kappa F_{\mu\nu},
$$

is **not** gauge invariant but transforms in the adjoint representation, $F_{2,\mu\nu} = \tilde U F_{\mu\nu} \tilde U^{-1}$; it satisfies the Bianchi identity $D_\lambda F_{\mu\nu} + D_\mu F_{\nu\lambda} + D_\nu F_{\lambda\mu} = 0$; and $-\tfrac12\mathrm{Tr}\bigl(\sum_{\mu,\nu}\varepsilon_\mu\varepsilon_\nu F_{\mu\nu}F_{\mu\nu}\bigr)$ is a gauge-invariant density, with the trace taken on the $\mathrm{SU}(2)$ factor.

What this construction is, for the purposes of this agenda, is the **general machinery of a non-abelian gauge theory**: everything that depends only on having a compact simple factor and a non-commuting connection is present. What it is not is a *colour* theory, because the factor it uses is $\mathrm{SU}(2)$ and the connection is $\mathrm{SU}(2)$-valued. The whole question of QCD is whether the framework can replace that factor by colour; the next section shows where that step stops.

### The gauge algebra the algebra contains, and its ceiling

The available gauge algebra is determined by the algebra, not chosen. The material sector decomposes as a Lie algebra under the commutator,

$$
\mathbb{B}_{\Phi} \;=\; \mathbb{R}(ie_t) \;\oplus\; \mathrm{SU}(2),
$$

so the compact algebra present is $\mathrm{U}(1)\oplus\mathrm{SU}(2) = \mathrm{U}(2)$, of real dimension $4$. This is exactly the anti-Hermitian subspace of $\mathbb{B}\cong M_2(\mathbb{C})$: anti-Hermitian $2\times2$ complex matrices *are* the Lie algebra $\mathrm{u}(2)$, and the Cartan decomposition of the real Lie algebra $\mathrm{GL}(2,\mathbb{C})$ is

$$\boxed{\;\mathrm{GL}(2,\mathbb{C}) \;=\; \mathrm{U}(2) \;\oplus\; i\,\mathrm{U}(2),
\qquad \dim_\mathbb{R} = 4 + 4 = 8\;},$$

with $[\mathrm{U}(2),\mathrm{U}(2)]\subseteq\mathrm{U}(2)$ and $[\mathrm{U}(2),i\mathrm{U}(2)]\subseteq i\mathrm{U}(2)$. The decomposition was checked on a basis of $\mathrm{U}(2)$ and the brackets close as stated. Because every compact subalgebra of a real Lie algebra lies in a maximal compact subalgebra, and the maximal compact subalgebra of $\mathrm{GL}(2,\mathbb{C})$ is $\mathrm{U}(2)$, **any compact gauge algebra that is a subalgebra of $\mathbb{B}$ under the commutator has real dimension at most $4$.**

The matter side has the matching ceiling. The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is simple and Artinian, so every module is a direct sum of copies of its unique simple module, which is $\mathbb{C}^2$. Consequently **every $\mathbb{B}$-module has complex dimension divisible by two.** A colour triplet — a complex three-dimensional internal space for the quark — is not a $\mathbb{B}$-module.

$$
\boxed{\;\dim_\mathbb{C} M = 2k \ \ (k \in \mathbb{Z}_{\ge 0}) \quad\text{for every } \mathbb{B}\text{-module } M,
\qquad\text{so } \dim_\mathbb{C} = 3 \text{ is impossible.}\;}
$$

This is the precise ceiling of the present construction, and it is what makes the colour group an obstacle rather than a gap with a known route. It is not a failure of the framework's arithmetic; it is a statement about the carrier. The non-abelian machinery is real, and it is real for $\mathrm{U}(2)$; colour needs a compact simple algebra of dimension $8$ and a three-dimensional module, and neither is available in $\mathbb{B}$ on the present construction.

### The chiral-fermion issue

The read-list article *Chiral Fermions in the Biquaternion Framework* establishes the following, and this agenda inherits it without change. The gradient, the d'Alembertian and the two first-order equations are those of *Operator and Calculus Conventions*, and the two values $L$ and $R$ are those of *Special Element Conventions*; none of the three is derived here.

**The field and its two values.** The field is an element $\tilde{Ξ}_{\mathrm{sp}}$ of $\mathbb{B}$. It splits into two parts,

$$
\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R},
$$

the $L$ part of value $-1$ and the $R$ part of value $+1$ under the frame's chirality basis operator (*Special Element Conventions*, §*The Chirality Convention*), and only the zero element has both parts zero. The value is a subscript of the element: a general element, a product, a unit and a field all carry it. Left multiplication keeps the value, and a product takes the value of its right factor. A Lorentz action multiplies on the left, so it preserves both values.

**The two Dirac equations.** The dynamics is the chiral pair

$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R} = k_m\,\tilde{Ξ}_{\mathrm{sp},L},
$$
$$
\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\,\tilde{Ξ}_{\mathrm{sp},R} .
$$

Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

Each member is a left multiplication, and the mass is the off-diagonal pairing of the two parts. The second member is the biquaternion conjugate of the first: the conjugation exchanges the two sides, so the conjugate of a left action on $\tilde{Ξ}_{\mathrm{sp},R}$ is written as a left action of $\tilde\nabla^{\natural}$ on $\tilde{Ξ}_{\mathrm{sp},L}$ (*Operator and Calculus Conventions*, §*The Two Sides and the Renaming Theorem*). Eliminating one part returns the mass shell, $\Box\tilde{Ξ}_{\mathrm{sp},R}=k_m^{2}\tilde{Ξ}_{\mathrm{sp},R}$. No basis operator enters the pair itself, because both members are left multiplications.

**The pair.** The two members are two first-order lines on a pair of elements of $\mathbb{B}$, the pair of *Operator and Calculus Conventions*, §*The Plain Bilinear Product, Its Form and Its Norm*: $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L}$ and $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R}$, each line composed with its partner being $\Box$.

**Why one field carries the massless case and not the massive one.** The square of the gradient is not scalar. The diagonal basis operators of the coefficient basis are the four squares, $e_te_t=e_t$ and $\vec e_\eta\vec e_\eta=-e_t$, so the diagonal part is scalar; the cross terms are the ones that do not cancel — the pairs of two distinct spatial units cancel by antisymmetry, and the time–space pairs add, because $e_t$ commutes with the three spatial units. This is a derived form, read from the multiplication here. Hence $\tilde\nabla^2\neq\Box$, and the square is not even scalar, while a scalar square is what a one-field first-order massive equation would need. The **free** equation therefore stays first order in one field; the **massive** equation is the chiral pair above, two fields and one mass; and a one-field first-order massive equation does not exist here. This article writes none.

**The mass bilinear.** The Dirac mass bilinear is the frame's scalar with the timelike unit $i\vec e_x$ inserted on the right,

$$
B(\tilde{Ξ}_{\mathrm{sp}})=\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*\tilde{Ξ}_{\mathrm{sp}}\,i\vec e_x\bigr),
$$

and it is odd under the exchange of the two values: it changes sign when $\tilde{Ξ}_{\mathrm{sp},L}$ and $\tilde{Ξ}_{\mathrm{sp},R}$ are exchanged, and it vanishes on a field of a single value, so it pairs one part of each value. Both statements were rechecked on the defining representation. A chiral abelian symmetry with independent charges is consistent when the charge element $Ϙ$ carries the values $ϙ_L$ and $ϙ_R$ on the two parts; the element $Ϙ$ is central exactly when $ϙ_L=ϙ_R$, and the mass bilinear is gauge invariant **if and only if $ϙ_L = ϙ_R$**.

Two further results of that article are the ones that bear on QCD.

- **The canonically available gauge group is vector-like.** The framework's own abelian gauge group is the $*$-unitary part of the centre $\mathbb{B}_{C}$, which acts as a *scalar* on $M_2(\mathbb{C})$; every part of the field receives the same charge. A chiral gauge group requires a non-central action, hence a non-abelian gauge structure — the structure the non-abelian article supplies for $\mathrm{SU}(2)$ but does not dress with matter.
- **The framework's mass term relates the two parts.** The mass is the off-diagonal coefficient of the chiral pair, and it is the real-form expression of an ordinary Dirac mass. An axial rotation turns the two parts by opposite phases and the mass is the term that relates them, so the rotation cannot pass through it: that is the breaking of the **axial** symmetry. The vector phase $\mathrm{U}(1)$ — fermion number — turns both parts by one phase and passes through the linear mass, and is exact for the massive field. The mass moves no value: it is a central coefficient and keeps the value of each part. The value is exchanged by a right multiplication perpendicular to the axis, or by the coefficient conjugation, and those are the two moves the two-sided form uses. With the axial current $j_{5\mu}$,

    $$
    j_{50}=\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*\tilde{Ξ}_{\mathrm{sp}}\,(-i\vec e_z)\bigr),
    \qquad
    j_{5\eta}=\mathrm{Sc}\bigl(i\tilde{Ξ}_{\mathrm{sp}}^*\vec e_\eta\tilde{Ξ}_{\mathrm{sp}}\bigr),
    $$

    the time component multiplying on the right and the three spatial ones on the left, and

    $$
    \sum_\mu\frac{\partial j_{5\mu}}{\partial R_\mu}=2im\,\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*\tilde{Ξ}_{\mathrm{sp}}\,\vec e_y\bigr),
    $$

    a plain sum, because the signs are carried by the units inside the bilinears and not by the sum. The insertion is $\vec e_y$ where the mass bilinear carries $i\vec e_x$. The density $\mathrm{Sc}(\tilde{Ξ}_{\mathrm{sp}}^*\tilde{Ξ}_{\mathrm{sp}}\vec e_y)$ is imaginary, so the $i$ of the coefficient makes the product real. It vanishes only at $m=0$. A genuinely antilinear Majorana-type pairing lives instead on the algebra's real structure $\tilde{Ξ}_{\mathrm{sp}}^{\flat} = -\tilde{Ξ}_{\mathrm{sp}}^*$ and on the separate single-field equation built on it, whose plane waves lie on the spacelike locus.

The anomaly, finally, is where QCD's chirality is physically indispensable; the series' position on it is recorded in §"The Chiral-Fermion Issue and the Quark Couplings".

### The reach of the renormalization group

The series **does** contain a renormalization-group article, *The Renormalization Group in Biquaternionic Form*, and it **does** reach the non-abelian case. It performs the shell integration and obtains the standard one-loop gauge beta function

$$
\beta_g = -\frac{g^3}{16\pi^2}\,b_0, \qquad b_0 = \frac{11}{3}C_2(G) - \frac{2}{3}\sum_{\text{Weyl}}T(r),
$$

negative for pure $SU(N)$, with $C_2(G) = N$ recomputed from the structure constants on both $SU(2)$ and $SU(3)$ — the independent-case check the corpus's discipline requires. For $SU(3)$ with $N_f$ Dirac quark flavours, each flavour contributing two Weyl fermions of index $T=\tfrac12$, this is $b_0 = 11 - \tfrac{2}{3}N_f$; the arithmetic gives $b_0>0$ — asymptotic freedom — for $N_f < \tfrac{33}{2}$, and the two-loop Banks–Zaks fixed point is computed as well. The article's own framing, however, is explicit: the effective action, the measure, the regulator, the gauge group, the matter content, and the coupling values are all **inputs**; the beta functions are **transcribed** from standard field theory and would not change if $\mathbb{B}$ were replaced by any other notation for complexified four-dimensional spacetime. The flow acts on central scalars only, so the framework's regulator is sector-blind, and its algebraically natural sharp cutoff breaks gauge invariance while the gauge-safe regulator (dimensional regularisation) is external to the four-dimensional algebra.

For QCD this means: the *form* of the running and the *sign* of the non-abelian beta function have been written in biquaternion notation, and the standard QCD threshold has been reproduced, but the colour group and the quark content that give them meaning are still the missing objects of the previous sections.

## The Colour Group: Nothing Derives a Three

QCD begins with a group. The colour group is $SU(3)$, its rank-two simple compact algebra $\mathrm{SU}(3)$ has real dimension $8$, and the quarks sit in its complex three-dimensional fundamental representation $\mathbf{3}$ while the gluons sit in the eight-dimensional adjoint. Nothing in the biquaternion series supplies any of this. This section states precisely what is and is not available, and it distinguishes a derivation from a positing.

**What is available.** From the preceding section: the compact algebra available in $\mathbb{B}$ is $\mathrm{U}(2)$ at most, of dimension $4$; the unique simple module is $\mathbb{C}^2$; and every $\mathbb{B}$-module has even complex dimension. The tempting identifications of "three" in the framework are all false leads, and it is worth naming them so that they are not mistaken for a route:

- **The three quaternion units $\vec e_x,\vec e_y,\vec e_z$.** There are three of them, but they span the **adjoint** of $\mathrm{SU}(2)$ — the spin-one representation — not a complex triplet. $SU(2)$ has no complex three-dimensional representation, and its fundamental is two-dimensional. Counting three basis vectors is not constructing colour.
- **The two values, the two sectors, the two summands.** These give a $\mathbb{Z}_2$, not a $\mathbb{Z}_3$. The complexification $\mathbb{C}\otimes_\mathbb{R}\mathbb{B}\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C})$ has two simple summands; the field splits into the $L$ and $R$ parts; the sectors are two. Nothing in the corpus produces a triple.
- **The three components of the complement of the light cone.** The zero-divisor cone gives a three-part classification of intervals (timelike, spacelike, null) and the complement of the cone has three connected components. A partition of a cone is not a group, and interval type is not an internal quantum number.
- **The dimension count $8 = 8$.** Both $\mathbb{B}$ and $\mathrm{SU}(3)$ are eight-real-dimensional, but $\mathbb{B}$'s compact part is $\mathrm{U}(2)$ and its module is two-dimensional. Equality of dimensions is a coincidence of counting, not an embedding.

**What positing would and would not be.** One can of course write down a colour group and tensor it on: take the matter field to be $\tilde{Ξ}_{\mathrm{sp}}\otimes c$ with $c\in\mathbb{C}^3$, let $SU(3)$ act on $c$ and $\mathbb{B}$ act on $\tilde{Ξ}_{\mathrm{sp}}$, and build a connection valued in $\mathrm{SU}(3)$ on the colour factor. That constructs *a* theory with colour, and it is exactly the move through which the corpus already passes once: the chiral-fermion article writes its abelian chiral connection as "a connection valued in the algebra of module endomorphisms", i.e. on an enlarged carrier rather than inside $\mathbb{B}$. But it is an **adjoining of an independent factor**, and adjoining $\mathbb{C}^3$ is not deriving it. The framework fixes neither the dimension three, nor the group $SU(3)$, nor the reason the factor should exist at all. To posit $SU(3)$ and then present the resulting construction as the framework's colour theory is precisely the fabrication the agenda must not commit.

**The one candidate route, stated as a candidate.** If colour is to come from the framework rather than be added to it, the construction must be enlarged in a way the algebra *forces*. Two shapes of such an enlargement are conceivable. The first is to let the carrier be the endomorphism algebra of a $\mathbb{B}$-module tensored with an internal space $X$, whose dimension the algebra somehow determines; since the endomorphism algebra of a carrier of complex dimension six contains $\mathrm{SU}(3)$, the group can live there — the question is what fixes $X$. The second is to look for a rank-two compact structure already inside $\mathbb{B}$'s representation theory, for instance in the decomposition of tensor powers or in the complexification, on the chance that an $\mathrm{SU}(3)$ subalgebra of some natural endomorphism algebra appears. Neither of these is a route yet. The first assumes the answer ($X=\mathbb{C}^3$); the second is a search with no known outcome, and the ceiling argument of the preceding section is evidence against it. The honest classification is therefore **no route yet**, with the candidate named so that it can be tried rather than forgotten.

**What would settle it.** A theorem of one of two forms would settle the colour-group question, and either outcome is a result:

- **Positive.** An algebra-internal construction that produces a rank-two compact gauge algebra and a complex three-dimensional internal module from $\mathbb{B}$'s own structures — its zero divisors, its tensor powers, or its complexification — together with a **selection principle** that fixes $N_c = 3$. A construction of the group without a principle that selects three does not settle it, because the framework would then host a continuum of colour groups.
- **Negative.** A no-go theorem covering not only $\mathbb{B}$-valued connections but all $\mathbb{B}$-invariant enlargements, showing that any colour group must be adjoined as an independent factor. A negative result settles the question by relocating it: colour would then be an input, and the framework's contribution to QCD would be limited to whatever the general non-abelian machinery adds once colour is supplied.

Until one of these exists, the colour group stays open, and every use of it below is flagged.

## Confinement: No Mechanism

Confinement is the defining feature of QCD: quarks and gluons are not observed as isolated states, the potential between a separated colour pair grows linearly, and the spectrum contains only colour-singlet states. If a framework claims to contain a colour theory, confinement is the first thing that must be accounted for. The biquaternion framework does not account for it, and the honest statement is stronger than "the mechanism is unproven": **no mechanism has been proposed.** This is not a gap with a known route; it is an obstacle with no route yet.

Four things that would be needed are all absent.

- **A non-perturbative formulation.** The renormalization-group article is a perturbative calculation: a one-loop shell integration, one- and two-loop beta functions, and the Gaussian and Banks–Zaks fixed points. Asymptotic freedom is an ultraviolet statement; confinement is an infrared statement. A perturbative beta function, however accurately transcribed, has no bearing on it.
- **A Wilson loop, or something equivalent.** The standard non-perturbative diagnostic is the Wilson loop $W(C) = \mathrm{Tr}\,\mathcal{P}\exp\!\oint_C \mathcal{A}$, whose large-loop behaviour $\langle W(C)\rangle \sim \exp(-\sigma A(C))$ is the area law, with $\sigma$ the string tension. No Wilson loop is defined anywhere in the series, and it cannot be defined without the measure the path-integral article places outside finite-dimensional $\mathbb{B}$.
- **A gauge-invariant regulator.** The renormalization-group article records that the algebra's natural cutoff is central, sector-blind, and breaks gauge invariance, while dimensional regularisation leaves the four-dimensional algebra; a biquaternionic gauge-invariant regulator is itself an open problem. Non-perturbative gauge theory, on the lattice or otherwise, requires such a regulator, so confinement cannot even be posed before that gap is closed.
- **A gauge-fixing principle and a mass gap.** The canonical-quantization article on the Maxwell field records that the framework cannot fix the gauge naturally, and no gauge-fixing principle is supplied. No mass gap — the statement that the spectrum has a lowest positive mass — is established or even formulated.

The framework's closest structures are the zero divisor cone and the null four-vectors of $\mathbb{B}_{\Phi}$. It is worth saying why they do not help. The light cone is a statement about the biquaternion norm of a biquaternion; it classifies momenta and propagation directions. Confinement is a statement about the energy of a *configuration of colour sources* — a potential that grows with separation. A null direction is not an area law, and the fact that a massless field propagates on the light cone says nothing about the force between two colour charges. The zero-divisor structure is a genuine feature of the algebra, but reading confinement from it would be an analogy, not a derivation, and the analogy is not made here.

**What would settle it.** A framework-internal object whose computed behaviour establishes either the area law or its absence. Concretely: define a biquaternionic Wilson loop on the enlarged carrier that the colour-group question settles, and compute its large-loop asymptotics, exhibiting a string tension $\sigma>0$; or exhibit a mass gap in the framework's spectrum; or prove that no such object can be defined in $\mathbb{B}$, which settles the question negatively and shows that confinement, like the colour group, must be imported. All three require, as a prerequisite, the action, measure, and gauge-invariant regulator that the series does not yet have — which is why confinement is downstream of apparatus as well as of the colour group.

## The Chiral-Fermion Issue and the Quark Couplings

The chiral-fermion issue is inherited from the read-list article, whose content is carried unchanged. It has three parts: the splitting of the field into its two values is exact, the framework's canonically available gauge group is vector-like and cannot be chiral, and the framework's own mass term is a linear off-diagonal chiral coupling that breaks the axial symmetry while leaving the vector $\mathrm{U}(1)$ exact. One of the gaps that article left — the anomaly — has since been partly closed elsewhere in the series, and that is addressed below.

The question for this agenda is how much of that is a *QCD* obstacle. The answer requires care, because one natural interpretation of the issue does not apply to colour and another does.

**The gauge-chirality obstruction is not itself a colour obstruction.** Colour is a **vector-like** interaction: the $L$ and $R$ parts of a quark carry the *same* colour representation, so a colour gauge transformation acts identically on $\tilde{Ξ}_{\mathrm{sp},L}$ and $\tilde{Ξ}_{\mathrm{sp},R}$. The chiral-fermion article's finding that the centre is scalar and vector-like, and cannot generate a chiral gauge group, is therefore not an obstruction to colour; if anything it is the opposite, since a vector-like action is exactly what colour needs. It is worth saying this plainly so that the chiral-fermion result is not over-read: the framework's inability to make a *chiral gauge group* bears on the electroweak sector, not on colour.

**What does bear on QCD is the missing colour representation of the quark.** The chiral-fermion article constructs its chiral covariant derivative for an *abelian* phase, with a charge element $Ϙ$ of values $ϙ_L$ and $ϙ_R$. The non-abelian article constructs a connection with values in $\mathrm{SU}(2)$ but explicitly leaves the matter representation open: its open question 3 states that for a non-abelian connection the left and right actions differ and the representation carried by the matter field must be specified, and that the non-abelian charge operator is not constructed. QCD needs the quark in the **fundamental of the colour group**, with the covariant derivative acting on the colour index. By the ceiling of §"The Colour Group", a colour triplet is not a $\mathbb{B}$-module, so this representation must live on an enlarged carrier. The matter representation and the colour group therefore share a single settling object: a construction, on whatever carrier is justified, of a field transforming in the colour fundamental with the connection acting on the internal index.

**The global chiral sector of QCD is a further, distinct obstacle.** Beyond the gauge representation, the quarks carry an approximate global chiral symmetry $SU(N_f)_L\times SU(N_f)_R$ (for the light flavours), which is spontaneously broken and whose consequences — light Goldstone pions, the $\eta_{\mathrm s}$ mass, the axial anomaly, the $\theta$-vacuum — are central to QCD. The framework supplies the two values, so a chiral global action is available on the field: every element of $\mathbb{B}$ splits into $\tilde{Ξ}_{\mathrm{sp},L}$ and $\tilde{Ξ}_{\mathrm{sp},R}$. It also records the price: the value is a subscript of the element and not a central charge of $\mathbb{B}$, so its central form exists only in the complexification (*Special Element Conventions*, §*The Chirality Convention*).

The **anomaly** is now partly supplied, and the position has to be stated carefully because it has moved. The chiral-fermion article attempted no biquaternion formulation of it; the companion *Anomalies and Anomaly Cancellation in Biquaternionic Form* does. It writes the Adler–Bell–Jackiw divergence in the framework's own objects,

$$
\langle\tilde\nabla,\tilde J_{\Phi,5}\rangle_{\natural}=\sum_\mu\frac{\partial j_{5\mu}}{\partial R_\mu}
=2im\,\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*\tilde{Ξ}_{\mathrm{sp}}\,\vec e_y\bigr)-\frac{e^2}{16\pi^2}\,\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma},
$$

identifies the anomaly density with the second biquaternion invariant $I_2=\vec E\cdot\vec B$, exhibits the 't Hooft vertex as a product of the bilinears the framework already carries, and verifies the Standard Model's cancellation conditions generation by generation. What is imported there is the coefficient, quoted from standard field theory rather than derived, and the triangle coefficient $\mathrm{Tr}_R[T_a\{T_b,T_c\}]$ runs over the representation $R$ of whatever gauge group is supplied — for colour, a group the framework does not own. The $\theta$-angle and strong $CP$ lie outside that article by its own statement. So the QCD-specific gap is narrower than it was and is still real: the anomaly is formulated at the level of a single abelian current, and the **colour-dressed** coefficient, the flavour-singlet $\mathrm{U}(1)_A$ at $N_f$ flavours, and the strong $CP$ question remain unbuilt.

**The framework's mass term interacts with both.** The mass is the off-diagonal pairing of the chiral pair written in §"The chiral-fermion issue"; it is the real-form expression of an ordinary Dirac mass, so the interpretation is settled. The framework therefore carries a conserved fermion number — the central phase passes through the linear mass and the vector $\mathrm{U}(1)$ is exact for the massive field — and what the mass breaks is the **axial** charge, with the divergence $\sum_\mu\partial j_{5\mu}/\partial R_\mu=2im\,\mathrm{Sc}\bigl(\tilde{Ξ}_{\mathrm{sp}}^*\tilde{Ξ}_{\mathrm{sp}}\,\vec e_y\bigr)$ established there, which vanishes only at $m=0$. That is the framework's transcription of exactly the chiral-symmetry breaking that organises the light-hadron spectrum. The companion article *The Chiral Condensate and Dynamical Symmetry Breaking in Biquaternionic Form* takes the next step and identifies the condensate with a dynamically generated coefficient of this same linear pair, but it transcribes the gap equation, and the scale, the interaction and the Goldstone counting are standard input rather than framework results. The genuinely antilinear pairing lives on the algebra's real structure $\flat$ and on the separate single-field equation built on it, whose plane waves lie on the spacelike locus; that is a different equation from the gradient equation, and it is not the framework's mass term.

**What would settle it.** Three computations, in order of dependence:

1. **The colour representation of the quark.** Construct the matter field on the carrier that the colour-group question settles, with the covariant derivative acting on the internal colour index, and check its gauge covariance. This is the same object as obstacle 1's, and it has a known route *conditional on that carrier existing*; without the carrier it is blocked.
2. **The anomaly.** The abelian divergence and the 't Hooft vertex now exist in the framework, with the coefficient quoted from the standard result. What remains is the **colour-dressed** computation: the triangle coefficient $\mathrm{Tr}_R[T_a\{T_b,T_c\}]$ on a module that carries colour, and the flavour-singlet $\mathrm{U}(1)_A$ at $N_f$ flavours, compared against the standard value. That is a **known route, blocked on the colour carrier of item 1**: the standard computation defines the target, and the framework must reproduce the coefficient or fail to.
3. **The mass interpretation.** Largely settled on the parent's equation: the mass term is the linear chiral pair, the real-form expression of an ordinary Dirac mass, so the framework carries a conserved fermion number and what the mass breaks is the axial charge. What remains open is the separate question the chiral-fermion article poses — how the algebra's real structure $\flat$, and the single-field equation $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp}} = k_m\tilde{Ξ}_{\mathrm{sp}}^{\flat}$ built on it, read on the real form, and whether that real-form choice is what distinguishes a Majorana from a Dirac fermion.

## The Running Coupling and Asymptotic Freedom

This is the one obstacle for which the series has already built the machinery and reached the non-abelian case, and the honest statement is therefore different from the preceding two. The renormalization-group article performs the one-loop shell integration for a non-abelian gauge coupling, obtains $\beta_g = -(g^3/16\pi^2)b_0$ with $b_0 = \tfrac{11}{3}C_2(G) - \tfrac{2}{3}\sum_{\text{Weyl}}T(r)$, recomputes $C_2(G)=N$ on $SU(2)$ and $SU(3)$, and reproduces the QCD values $b_0 = 11-\tfrac{2}{3}N_f$ for $SU(3)$ with $N_f$ Dirac flavours, the asymptotic-freedom threshold $N_f < \tfrac{33}{2}$, and the two-loop Banks–Zaks fixed point. The sign of the non-abelian beta function is the correct one and was checked on independent cases, which is the corpus's verification discipline.

What the article also records, in its own words, is that this is a **transcription**: the effective action, the measure, the regulator, the gauge group, the matter content, and the value of the coupling are all inputs; the beta functions are standard field theory written in biquaternion notation and would not change if $\mathbb{B}$ were replaced by any other notation. Two framework-specific limitations follow directly.

- **The flow acts on central scalars.** The scale $\mu$, the couplings, and the beta functions are real multiples of $e_t$, i.e. central, hence in $\mathbb{B}_{\Psi}$. The flow rescales central coefficients and does not rotate one sector into the other. It cannot, for example, generate a sector-sensitive scale, and it gives no handle on the medium-dependent local complex structure $c=1/\sqrt{\epsilon\mu}$, which the article records as an open question.
- **The regulator is external, and the natural one breaks gauge invariance.** The algebra hosts the central invariant $\tilde{Q}\tilde{Q}^{\natural}$ on which a cutoff is imposed, but not the cutoff; the sharp cutoff is not gauge invariant, and dimensional regularisation leaves the four-dimensional algebra. A biquaternionic gauge-invariant regulator is an open problem. For a *perturbative* one- and two-loop running this is manageable in transcription; for anything non-perturbative it is disabling.

So the running coupling and asymptotic freedom are an obstacle with a **known route** — the route is the standard one-loop computation, and it has been carried out in the framework's notation — but the route's *inputs* are exactly the missing objects: the colour group (obstacle 1) and the quark content (obstacle 3). In addition, the route reaches only the perturbative ultraviolet; it says nothing about confinement, which is the infrared companion of asymptotic freedom and is the obstacle with no route.

**What would settle it.** Fixing $C_2(G)$ and $T(r)$ for the framework's own gauge group and matter, i.e. settling obstacles 1 and 3, and supplying the $\mathbb{B}$-valued action, measure, and gauge-invariant regulator that the renormalization-group article names as absent. With those, the running $\alpha_s(\mu)$ is fixed by the framework rather than imported, and the sign of the beta function becomes a computed prediction to be checked rather than a transcribed standard result. A second, independent settling object is a **non-perturbative** computation that connects the asymptotically free ultraviolet to the confining infrared — a lattice or gap-equation analogue on the framework's carrier — because the two-loop perturbative flow alone cannot. As with the other obstacles, a negative result would also settle it: a demonstration that the framework's central flow cannot accommodate a sector-specific or non-perturbative structure would show that QCD's renormalization structure is imported wholesale.

## The Ledger

The table collects the items of the agenda and sorts each into the three-way classification. "Established" means recomputed in the series and inherited here; "known route" means the object does not exist but the computation that would produce it is identifiable; "no route yet" means no mechanism has been proposed.

| Item | Status | Object or computation that would settle it |
|---|---|---|
| Non-abelian gauge construction: connection, curvature with $[\mathcal{A},\mathcal{A}]$, adjoint law, Bianchi identity, gauge-invariant Yang–Mills density | Established | — |
| Available compact gauge algebra $\mathrm{U}(1)\oplus\mathrm{SU}(2)=\mathrm{U}(2)$, the maximal compact subalgebra of $\mathbb{B}$ | Established | — |
| No $\mathrm{SU}(3)$ subalgebra and no three-dimensional $\mathbb{B}$-module within the present construction | Established (within the $\mathbb{B}$-valued construction) | A positive internal construction with a principle selecting $N_c=3$, or a no-go covering all $\mathbb{B}$-invariant enlargements |
| Colour group $SU(3)$ and the number of colours $N_c=3$ | **No route yet** | The two theorems above; positing is not a route |
| The two values of the field; vector-like centre; mass selection rule $ϙ_L=ϙ_R$ | Established | — |
| Colour fundamental representation of the quark (internal index, covariant derivative) | Known route, blocked on the carrier | Construct the matter field on the settled carrier and verify gauge covariance |
| Confinement: area law, string tension, mass gap | **No route yet** | A biquaternionic Wilson loop with an area law, or a mass gap, or a no-go; prerequisite: action, measure, gauge-invariant regulator |
| Non-perturbative apparatus: $\mathbb{B}$-valued action, measure, gauge-invariant regulator | **No route yet** | An action and a regulator that live in the algebra and preserve gauge invariance |
| Running coupling and asymptotic freedom beyond transcription | Known route, blocked on inputs | Fix $C_2(G)$ and $T(r)$ from the framework's own group and matter; supply the action, measure, and regulator |
| Axial anomaly of one abelian current: divergence identity, density $=I_2$, 't Hooft vertex, Standard Model cancellation conditions | Established as a formulation; the coefficient is quoted, not derived | A framework derivation of the coefficient |
| Colour-dressed anomaly, flavour-singlet $\mathrm{U}(1)_A$ at $N_f$, $\theta$-vacuum, strong $CP$ | Known route, blocked on the colour carrier | The triangle coefficient $\mathrm{Tr}_R[T_a\{T_b,T_c\}]$ on a colour-carrying module; $\theta$ and strong $CP$ lie outside the anomaly article by its own statement |
| The framework's mass term: linear off-diagonal chiral coupling (vector $\mathrm{U}(1)$ exact, axial broken) | Established | The linear chiral pair; the separate $\flat$-pairing on the single-field equation is a distinct, still-open interpretation |
| Empirical contact: a prediction distinguishing the framework from standard QCD | **No route yet** | Any observable the two theories compute differently; none is proposed |

## What Would Settle It

The obstacles are not independent, and the dependency chain is short. The quark's colour representation (obstacle 3) needs the carrier that the colour-group question (obstacle 1) would settle; the running coupling (obstacle 4) needs both, plus the action and regulator; confinement (obstacle 2) needs the action and regulator and, to be a statement about colour at all, needs the colour group. Two items are therefore upstream of everything else.

1. **A derivation or a justified fixing of the internal colour structure.** Either colour comes out of $\mathbb{B}$ — a rank-two compact algebra and a three-dimensional internal module, with a principle that selects three — or it is shown that colour must be adjoined as an independent factor. Either outcome converts the framework's relation to QCD from "unknown" to "stated". The one thing that does not convert it is writing $SU(3)$ down and proceeding; that is the fabricated premise the agenda exists to prevent.
2. **A $\mathbb{B}$-valued action with a gauge-invariant regulator.** The renormalization-group article names the absent action, measure, and regulator, and the confinement section shows they are prerequisites for even posing the area law. Until they exist, every QCD computation in the framework is a transcription of a standard one, and every non-perturbative statement is unavailable.

With those two settled, the rest of the agenda becomes ordinary work: construct the quark representation, compute the anomaly, run the colour coupling, and look for the area law. Without them, the honest summary of the framework's relation to QCD is the one this article opened with: it has the general non-abelian gauge machinery, it has an exact splitting of the field into its two values, it has the form of the running coupling, and it does not have a colour theory.

Finally, the genre's standing caution applies here in its strongest form. *The Empirical Status of the Biquaternion Framework* records that on every domain developed, the framework is so far empirically equivalent to the standard theory it reformulates. A biquaternionic colour theory, if one is ever constructed, would inherit that position unless it makes a prediction standard QCD does not; and a theory whose colour group, matter content, coupling, and confinement mechanism are all imported has no prospect of doing so. The agenda's most useful output may be to make that consequence visible early, rather than to produce a construction that appears to answer QCD while assuming all of it.

## Summary

This article is a research agenda for quantum chromodynamics inside the biquaternion framework. Its finding is that the framework reaches the general machinery of a non-abelian gauge theory and stops before colour.

What is established is recalled: the non-abelian gauge construction, with a connection transforming in the adjoint, a curvature containing the commutator term and satisfying the Bianchi identity, and a gauge-invariant Yang–Mills density, built on the $\mathrm{SU}(2)$ factor of the material sector; the Lie-algebra decomposition $\mathbb{B}_{\Phi} = \mathbb{R}(ie_t)\oplus\mathrm{SU}(2)$, so that the compact algebra available is $\mathrm{U}(2)$; the two values of the field, a chirality-odd mass bilinear, and the selection rule $ϙ_L=ϙ_R$; the vector-like character of the centre; and a renormalization-group article that does reach the non-abelian case and reproduces the standard one-loop beta function, $C_2(G)=N$, the QCD coefficient $b_0=11-\tfrac{2}{3}N_f$, and the asymptotic-freedom threshold — as a transcription.

What is not established is everything QCD-specific.

- **The colour group.** Nothing derives $SU(3)$ or any three-valued internal structure. Within the framework's construction the compact algebra is at most $\mathrm{U}(2)$ of dimension $4$, and every $\mathbb{B}$-module has even complex dimension, so no $\mathrm{SU}(3)$ subalgebra and no colour triplet are available. Positing $SU(3)$ is not deriving it. **No route yet**, with the enlarged-carrier construction named as the only candidate.
- **Confinement.** No mechanism has been proposed. The perturbative renormalization group is an ultraviolet result and has no bearing on the infrared area law; there is no Wilson loop, no gauge-invariant regulator, no mass gap, and no gauge-fixing principle. **No route yet.**
- **The chiral-fermion issue.** Its gauge half does not obstruct colour, because colour is vector-like; but the quark's colour representation is unbuilt, the axial anomaly has a framework formulation only for a single abelian current with its coefficient quoted, and the framework's mass term, being the linear chiral coupling, breaks the axial charge while leaving fermion number exact.
- **The running coupling.** The series has the machinery and reaches the non-abelian case, but the gauge group, matter content, action, measure, and regulator are all inputs. **Known route, blocked on the very objects the other obstacles are missing.**

The two upstream items are a derivation (or a justified fixing) of the internal colour structure and a $\mathbb{B}$-valued action with a gauge-invariant regulator. Everything else depends on them. The article commits throughout to the agenda's central discipline: no section assumes a colour group, and where standard QCD numbers appear, they are marked as imports.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$, $e_t,\vec e_x,\vec e_y,\vec e_z$, $i$ | The biquaternion algebra, its four units and the central imaginary (*Algebra and Element Conventions*) |
| $\mathbb{B}_{\Psi}$, $\mathbb{B}_{\Phi}$ | The informational and material sectors (*Algebra and Element Conventions*) |
| $\mathbb{B}_{C}$ | The centre of the algebra; the vector-like abelian factor |
| $\mathbb{B}_{H}$ | The real-quaternion subspace |
| $\tilde\nabla$, $\Box$ | The biquaternionic gradient and the d'Alembertian (*Operator and Calculus Conventions*) |
| $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R}$ | The pair as two first-order lines (*Operator and Calculus Conventions*); each line composed with its partner is $\Box$ |
| $\tilde{Ξ}_{\mathrm{sp}}$, $\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{Ξ}_{\mathrm{sp},R}$ | The field and its two values, $L$ of value $-1$ and $R$ of value $+1$ (*Special Element Conventions*) |
| $B(\tilde{Ξ}_{\mathrm{sp}})$ | The mass bilinear of the read list; odd under the exchange of the two values |
| $j_{5\mu}$, $Ϙ$, $ϙ_L$, $ϙ_R$ | The axial current and the charge values on the two parts (read list) |
| $\tilde{Ξ}_{\mathrm{sp}}^{\flat}$ | The algebra's real structure (*Algebra and Element Conventions*); the single-field equation built on it is not the mass |
| $\tilde Q\tilde Q^{\natural}$ | The central quaternionic-norm invariant; the cutoff is imposed on it |
| $\mathcal{A}_\mu$, $F_{\mu\nu}$, $\kappa$ | The non-abelian connection, its field strength and the coupling (read list) |
| $[e_a,e_b]$, $T_a$ | The commutator and the generators of the $\mathrm{SU}(2)$ factor at the material sector (read list) |
| $\beta_g$, $b_0$, $C_2(G)$, $T(r)$ | The one-loop beta function and its coefficients, transcribed (*The Renormalization Group in Biquaternionic Form*) |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium, and in vacuum |
| **Standard QCD notation, not framework objects** | |
| $SU(3)$, $\mathrm{SU}(3)$ (dimension $8$, rank $2$) | Colour group and algebra — no route yet |
| $N_c=3$, $\mathbf{3}$, $\mathbf{8}$ | Number of colours; quark fundamental; gluon adjoint — no route yet |
| $N_f$, $\alpha_s$ | Quark flavour number and strong coupling — inputs, not derived |
| $W(C)$, $\sigma$, $\langle W(C)\rangle\sim \exp(-\sigma A(C))$ | Wilson loop, string tension, area law — not defined in the series |

## Further Reading

- [Non-Abelian Gauge Fields in Biquaternionic Form](non-abelian-gauge-fields-in-biquaternionic-form.html) — the immediate parent; the connection, the adjoint curvature, the Bianchi identity, the gauge-invariant density, and the open matter-representation question this agenda inherits.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html) — the abelian origin of the connection and the reality-condition gap the non-abelian construction takes up.
- [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html) — the splitting of the field into its two values, the vector-like centre, the mass selection rule, the linear chiral-coupling mass term, and the anomaly it leaves unformulated.
- [Anomalies and Anomaly Cancellation in Biquaternionic Form](anomalies-and-anomaly-cancellation-in-biquaternionic-form.html) — the Adler–Bell–Jackiw divergence written in the framework's own elements, the anomaly density as the second field invariant $I_2=\vec E\cdot\vec B$, the 't Hooft vertex, and the Standard Model cancellation conditions; the coefficient is quoted rather than derived, and $\theta$ and strong $CP$ lie outside its scope.
- [The Chiral Condensate and Dynamical Symmetry Breaking in Biquaternionic Form](the-chiral-condensate-and-dynamical-symmetry-breaking-in-biquaternionic-form.html) — the condensate as a dynamically generated coefficient of the same linear chiral pair, with the gap equation and the Goldstone counting transcribed.
- [The Renormalization Group in Biquaternionic Form](the-renormalization-group-in-biquaternionic-form.html) — the one-loop non-abelian beta function, $C_2(G)=N$, the QCD coefficient and threshold, and the article's own statement that these are transcribed with the group and matter as inputs; the source of the running-coupling item.
- [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html) — the abelian connection whose non-abelian extension is the parent's starting point.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) and [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html) — the field and its Lorentz action, the linear chiral mass term, and the real-structure origin of the two values.
- [Canonical Quantization of the Biquaternion Maxwell Field](canonical-quantization-of-the-biquaternion-maxwell-field.html) — the framework's inability to fix the gauge, a prerequisite the confinement item needs.
- [Modules over the Biquaternion Algebra](../articles_maths/the-category-of-modules.html) and [Lie Algebras: A General Introduction](../articles_maths/lie-algebras-a-general-introduction.html) — the module structure and the compact-subalgebra facts behind the ceiling on the colour group.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html) — the null cone and the bivector structure, the objects closest to the confinement and topological-charge items.
- [The Lorentz Group in Biquaternionic Form — Structure and Representations](the-lorentz-group-in-biquaternionic-form-structure-and-representations.html) — the representation theory on which the adjoint and fundamental bookkeeping rests.
- [Helicity in Biquaternionic Form](helicity-in-biquaternionic-form.html) — the corpus's explicit statement that the framework "does not contain a colored gauge theory"; the transcription boundary this agenda makes systematic.
- [The Empirical Status of the Biquaternion Framework](the-empirical-status-of-the-biquaternion-framework.html) — the standing empirical-equivalence result, the caution under which any biquaternionic QCD would labour.
- [The Einstein Field Equations under the Biquaternion Framework — A Research Agenda](the-einstein-field-equations-under-the-biquaternion-framework-a-research-agenda.html) — the companion agenda whose three-way classification and settling-object discipline this article follows.
