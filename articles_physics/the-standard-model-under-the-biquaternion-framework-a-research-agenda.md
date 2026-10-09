# __The Standard Model under the Biquaternion Framework — A Research Agenda__

## Introduction

**The Standard Model** is the gauge theory of $SU(3)_c\times SU(2)_L\times U(1)_Y$: three gauge factors, matter in chiral representations — the left-handed quarks and leptons in $SU(2)_L$ doublets and their right-handed partners in singlets — a scalar doublet whose expectation value breaks the electroweak symmetry and supplies the fermion and weak-boson masses, and hypercharge assignments under which the anomalies cancel. This article is a research agenda for the Standard Model inside the biquaternion framework. It is a **synthesis**, not a new derivation: its subject is the boundary between what the framework has built and what the Standard Model requires, and its value is a clear statement of where that boundary lies.

The starting position is stated at the outset, because the whole agenda depends on it and because it is easy to overstate.

- **The framework has an abelian gauge principle.** The center of the algebra is $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$; its unitary part is $U(1)$; localizing a central phase forces a connection with the transformation law $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$, a covariant derivative, and a curvature. This is established in *The Gauge Principle in Biquaternionic Form* and is recalled in the next section.
- **The framework has a compact non-abelian gauge algebra inside the material sector.** The material sector decomposes as a Lie algebra, $\mathbb{M}_- = \mathbb{R}(ie_0)\oplus\mathrm{SU}(2)$, and on the $\mathrm{SU}(2)$ factor the full non-abelian gauge construction — a connection transforming in the adjoint, a curvature containing the commutator term, the Bianchi identity, and a gauge-invariant Yang–Mills density — is built. This is established in *Non-Abelian Gauge Fields in Biquaternionic Form* and is recalled in the next section.
- **The framework has not derived the Standard Model's gauge group, its chiral weak-isospin action, its hypercharge, or its scalar sector.** No source in the series derives a colour group or any three-valued internal structure. The $\mathrm{SU}(2)$ that is present acts vector-like on the algebra's own module and is therefore not weak isospin. No source derives a hypercharge assignment; the word "hypercharge" does not occur in any of the sources this agenda builds on. The scalar and symmetry-breaking sector is not built.

The discipline this forces on the article is the one the genre requires: **an agenda that quietly assumes its way to the Standard Model has fabricated its premise.** Each Standard Model structure is therefore carried as an **open item throughout**, never as a working assumption. Wherever a standard statement is written down — $SU(3)$, $SU(2)_L$, $U(1)_Y$, the mixing angle, the Higgs doublet, a generation — it is flagged as standard input, not as a framework result.

**The three-way classification.** The article sorts every item into one of three categories, and the distinction is the point of the agenda.

1. **Established.** Recomputed in the series and inherited here: the abelian gauge principle on the center; the compact algebra $\mathrm{SU}(2)$ inside $\mathbb{M}_-$ with the full non-abelian machinery; the ceiling on the gauge algebra; and the exact chiral structure on the spinor module.
2. **Obstacle with a known route.** The object does not exist, but the route to it is identifiable, usually because standard field theory or a finite algebraic check supplies the computation and the framework must reproduce it on its own carrier.
3. **Obstacle with no route yet.** No mechanism has been proposed, and naming an object is not the same as having a route to it. Colour, weak isospin, hypercharge, and the scalar sector are in this class.

**The spine of the article is the three gauge factors.** Each is stated with its source and its exact status: $U(1)$ from the abelian gauge principle; $\mathrm{SU}(2)$ from the material-sector decomposition; $SU(3)$ from nothing. The matter and scalar sectors are treated next: the chiral-fermion issue is open, hypercharge is underived, and the scalar and symmetry-breaking sector is unbuilt.

**Three temptations are refused.** (a) The isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$, whose commutator algebra contains $\mathrm{SU}(2)$, is **not** a derivation of $SU(2)_L$: weak isospin is a chiral structure, and the chirality problem must be resolved first. (b) The factors are **not** assembled into a product group and called the Standard Model's gauge group, because no hypercharge assignment is derived and one of the three factors is absent altogether. (c) Where the article counts what the framework supplies, it counts framework objects, not Standard Model parameters. These three refusals are the article's spine of caution, and each is argued where it arises.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_1e_2 = e_3$, and $i$ is the scalar imaginary, $i^2 = -1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector), with $\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+$; $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the center. The biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$, its quaternion conjugate is $\tilde{\nabla}^{\natural} = e_0\partial_{ict} - e_1\partial_x - e_2\partial_y - e_3\partial_z$, and $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla}$. For the abelian factor we use the connection $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$ and the law $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$ of the gauge-principle article. For the non-abelian factor we use the $\mathrm{SU}(2)$ connection and field strength of the read list, $\mathcal{A}_\mu \in \mathrm{SU}(2)$, $F_{\mu\nu} = \partial_\mu\mathcal{A}_\nu - \partial_\nu\mathcal{A}_\mu + i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$, $\kappa = q/\hbar$, with $[D_\mu,D_\nu] = i\kappa F_{\mu\nu}$. The spinor module is $\Delta = S\oplus\bar{S}$, $S=\mathbb{C}^2$, with $\gamma_5$ and $P_L = \tfrac12(I_4-\gamma_5)$, $P_R = \tfrac12(I_4+\gamma_5)$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the **speed of light in the medium** and $c_0$ the vacuum speed of light. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged. The symbols $SU(3)$, $SU(2)_L$, $U(1)_Y$, $T_3$, $Y$, $\theta_W$, and "Higgs" are **standard-model notation, not framework objects**; they are used only where a standard structure is being named as an input or as a missing item.

## What the Framework Already Reaches

### The abelian gauge principle and the central $U(1)$

The read-list article *The Gauge Principle in Biquaternionic Form* derives the framework's abelian gauge structure from the center of the algebra. Its results are established and are recalled here unchanged.

The center of $\mathbb{B}$ is the complex scalar line $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$, and its unitary part is

$$
U(1) \;=\; \{\lambda = e^{i\theta} : \theta \in \mathbb{R}\} \;\subset\; \mathbb{C}_{\mathbb{B}} .
$$

Because $\lambda$ is central and constant, it passes through the gradient, so the massless biquaternion equation $\tilde{\nabla}\tilde{\Psi} = 0$ is invariant under the global phase $\tilde{\Psi}\mapsto e^{i\theta}\tilde{\Psi}$. Making the phase local, $\lambda = e^{iq\Gamma(\tilde{Q})/\hbar}$, forces a connection with the transformation law

$$
\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma,
\qquad
D = \tilde{\nabla} + \frac{iq}{\hbar}\tilde{A},
\qquad
D_\mu = \partial_\mu + \frac{iq}{\hbar}A_\mu,
$$

under which $D\tilde{\Psi}$ transforms by the phase factor. The field strength is the vector part of $\tilde{\nabla}^{\natural}\tilde{A}$ and satisfies the curvature identity $[D_\mu,D_\nu] = \tfrac{iq}{\hbar}F_{\mu\nu}$. The abelian gauge group is **canonically attached to the algebra**: the only phase that commutes with the whole algebra must lie in the center, and the center is one complex dimension, so no choice of representation is made in selecting it.

Two properties of this factor are as important for the agenda as the factor itself. First, the charge $q$ is a **parameter**; the algebra does not fix it. Second, a central element acts as a **scalar** on the algebra: left multiplication by $\lambda = e^{i\theta}$ multiplies every entry, and hence every component of every module, by the same factor. A gauge group drawn from the center therefore assigns every component the same charge — it is **vector-like** and cannot distinguish left from right. This is established in *Chiral Fermions in the Biquaternion Framework*, and it is the reason the abelian factor as it stands cannot be weak hypercharge, which is chiral.

### The compact algebra inside the material sector

The read-list article *Non-Abelian Gauge Fields in Biquaternionic Form* builds the general non-abelian gauge structure inside $\mathbb{B}$. Its results are established and are recalled here unchanged.

The vector part of the material sector, $\mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\}$, closes under the commutator and is $\mathrm{SU}(2)$ in a non-standard normalization,

$$
[e_a,e_b] = 2\,\varepsilon_{abc}\,e_c, \qquad a,b,c = 1,2,3,
\qquad T_a = \tfrac12 e_a,\quad [T_a,T_b] = \varepsilon_{abc}T_c,\quad \mathrm{Tr}(T_aT_b) = -\tfrac12\delta_{ab}.
$$

The scalar part of $\mathbb{M}_-$ is the central line $\mathbb{R}(ie_0)$, so the material sector decomposes as a direct sum of Lie algebras,

$$
\mathbb{M}_- \;=\; \mathbb{R}(ie_0) \;\oplus\; \mathrm{SU}(2) \qquad \text{(direct sum of Lie algebras)},
$$

which is $\mathrm{U}(1)\oplus\mathrm{SU}(2) = \mathrm{U}(2)$ of real dimension $4$. The gauge group generated by the compact factor is the unit real quaternions, $SU(2) = \{U \in \mathbb{H}_{\mathbb{B}} : U\bar U = e_0\}$, acting on a matter field by left multiplication. A local transformation $U(\tilde{Q})$ forces the connection

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

is **not** gauge invariant but transforms in the adjoint representation, $F'_{\mu\nu} = U F_{\mu\nu} U^{-1}$; it satisfies the Bianchi identity $D_\lambda F_{\mu\nu} + D_\mu F_{\nu\lambda} + D_\nu F_{\lambda\mu} = 0$; and $-\tfrac12\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$ is a gauge-invariant density, with the matrix trace on the $\mathrm{SU}(2)$ factor and not the informational trace formula. What this construction supplies is the **general machinery of a non-abelian gauge theory**; what it does not supply is a chiral action of the factor on matter, because left multiplication acts on the algebra's own module vector-like (the module is discussed below).

One gap in the construction is carried here unchanged, because it bears on how a Standard Model factor could ever be identified. The reality class of the connection is **not** gauge invariant in a single Hermitian-conjugation eigenspace: the $ict$ derivative makes the Maurer–Cartan form $(\partial_\mu U)U^{-1}$ anti-Hermitian in the spatial directions and Hermitian in the time direction, so a condition placing all four components $\mathcal{A}_\mu$ in one eigenspace cannot survive a gauge transformation. A consistent **mixed** assignment exists — $\mathcal{A}_0$ anti-Hermitian (in $\mathrm{SU}(2)\subset\mathbb{M}_-$), $\mathcal{A}_k$ Hermitian (in $i\,\mathrm{SU}(2)\subset\mathbb{M}_+$) — but whether it is the intended physical one is open. The obstruction is a property of the $ict$ derivative, not of the gauge algebra.

### The ceiling on the gauge algebra

The available gauge algebra is determined by the algebra, not chosen, and it is bounded. The reasoning is inherited from the read list and from *Modules over the General Plain Algebra of Biquaternions*.

- **The compact subalgebra has dimension at most four.** The compact algebra present in $\mathbb{M}_-$ is $\mathrm{U}(2)$, and $\mathbb{B}\cong M_2(\mathbb{C})$ has the Cartan decomposition
$$
\mathrm{GL}(2,\mathbb{C}) = \mathrm{U}(2)\oplus i\,\mathrm{U}(2), \qquad \dim_\mathbb{R} = 4+4 = 8,
$$
with $[\mathrm{U}(2),\mathrm{U}(2)]\subseteq\mathrm{U}(2)$ and $[\mathrm{U}(2),i\mathrm{U}(2)]\subseteq i\mathrm{U}(2)$. Because every compact subalgebra of a real Lie algebra lies in a maximal compact subalgebra, and the maximal compact subalgebra of $\mathrm{GL}(2,\mathbb{C})$ is a conjugate of $\mathrm{U}(2)$, **any compact gauge algebra that is a subalgebra of $\mathbb{B}$ under the commutator, on the present construction, has real dimension at most $4$.**
- **Every module has even complex dimension.** The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is simple and Artinian, so every module is a direct sum of copies of its unique simple module, which is $\mathbb{C}^2$. Consequently every $\mathbb{B}$-module has complex dimension divisible by two, and a three-dimensional internal space for a quark is not a $\mathbb{B}$-module.

This is the precise ceiling of the present construction. The non-abelian machinery is real, and it is real for $\mathrm{U}(2)$; a colour theory needs a compact simple algebra of dimension $8$ and a three-dimensional module, and neither is available. The ceiling is the formal reason the framework stops where it does, and it is the reason colour is an obstacle with no route yet rather than a gap with a known route.

### The chiral structure on the module

The article *Chiral Fermions in the Biquaternion Framework* establishes the framework's chirality kinematics, and this agenda inherits it without change.

The Dirac module is $\Delta = S\oplus\bar{S}$, $S=\mathbb{C}^2$; the chirality operator is $\gamma_5 = \mathrm{diag}(-I_2,I_2)$ with $\gamma_5^2 = I_4$, and the projectors $P_L = \tfrac12(I_4-\gamma_5)$, $P_R = \tfrac12(I_4+\gamma_5)$ are idempotent, orthogonal, complete, of rank two, and Lorentz invariant. The Dirac mass bilinear $\bar\Psi\Psi = \psi_L^\dagger\psi_R + \psi_R^\dagger\psi_L$ is chirality-odd and vanishes on a state of definite chirality. On the module a **chiral abelian** gauge symmetry with independent charges is consistent: with $Q = q_LP_L+q_RP_R$, the covariant derivative $D_\mu = \partial_\mu + \tfrac{i}{\hbar}A_\mu Q$ is gauge covariant for arbitrary $q_L,q_R$, and the mass bilinear is gauge invariant **if and only if $q_L = q_R$**. This **mass selection rule** is the framework's form of the Standard Model's requirement that a chiral fermion acquire mass only through a compensating scalar.

Two further results of that article bear on the agenda. The framework's **own** gauge group, drawn from the center, is vector-like: on the algebra's module the central phase gives every component the same charge, so it cannot be a chiral gauge group. (The article records a qualification: under the alternative real-structure reading of the module the central phase would act axially, with $e^{i\theta}$ on $S$ and $e^{-i\theta}$ on $\bar S$, and which reading is physical is not settled. Under neither reading does the center supply independent left and right charges, so a derived chiral gauge group remains out of reach either way.) And the framework's **mass term** is the linear chiral pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$, through which the continuous central phase passes: the vector $U(1)$ is conserved for the massive field, and what the mass breaks is the axial symmetry, $\partial_\mu j_5^\mu = 2im\bar{\psi}\gamma_5\psi$. The algebra's anti-linear object is the real structure $\tilde{\Psi}^{\flat} = -\tilde{\Psi}^{*}$, whose separate conjugate pairing — Majorana-type or the real form of an ordinary Dirac mass — is the open reading treated in *The Neutrino and Majorana Fermions in Biquaternionic Form*.

## The Three Gauge Factors

### $U(1)$: present, but not weak hypercharge

**Source.** *The Gauge Principle in Biquaternionic Form*. **Status.** The gauge principle is established; the identification with weak hypercharge is not made and has no route yet.

What is established is a single abelian gauge factor, canonical and vector-like: the unitary part of the center, with connection law $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$ and curvature $[D_\mu,D_\nu] = \tfrac{iq}{\hbar}F_{\mu\nu}$. What weak hypercharge requires is a factor that (i) carries a definite set of **assignments** — different eigenvalues on different Standard Model multiplets, the pattern that makes $Q = T_3 + Y$ work and that cancels the anomalies — and (ii) acts **chirally**, with independent left and right charges on a single fermion, since the left- and right-handed components of the Standard Model fermions carry different hypercharge.

The framework's abelian factor supplies neither. Its action on the algebra's module is scalar, so it gives every component the same charge; under the alternative real-structure reading it would be axial, but still a single one-dimensional charge with no room for independent left and right assignments. And the coupling $q$ is one parameter, not a table. There is no object in the series from which the numbers $1/6$, $-1/2$, $2/3$, and so on could be read off. **An abelian gauge factor is established; weak hypercharge is not derived, and no computation in the series points toward it.** This item is classified **no route yet**.

### $SU(2)$: the algebra is present, weak isospin is not

**Source.** *Non-Abelian Gauge Fields in Biquaternionic Form*, on the decomposition $\mathbb{M}_- = \mathbb{R}(ie_0)\oplus\mathrm{SU}(2)$. **Status.** The compact algebra, the connection, and the full non-abelian gauge construction are established; the identification with $SU(2)_L$ is not, and is blocked on the chirality problem.

The $\mathrm{SU}(2)$ factor is genuinely there: $\mathrm{span}_\mathbb{R}\{e_1,e_2,e_3\}$ closes under the commutator with $[e_a,e_b] = 2\varepsilon_{abc}e_c$, the connection transforms in the adjoint, and the Yang–Mills density is gauge invariant. So the framework supplies a compact simple gauge factor of exactly the dimension and rank that $SU(2)$ has, with the general machinery attached. It is tempting to conclude that $SU(2)$ — and therefore, with the abelian factor, the electroweak gauge group — has been derived. **It has not, and the reason is the trap the subject of this article exists to mark.**

**The coincidence is not the derivation.** The algebra $\mathbb{B}$ is isomorphic to $M_2(\mathbb{C})$, whose commutator algebra $\mathrm{GL}(2,\mathbb{C})$ contains $\mathrm{SU}(2)$ — indeed many conjugates of it, and the unit-norm real quaternions generate one. That $\mathrm{SU}(2)$ is available is a fact about the algebra; it does not make the factor the Standard Model's weak isospin. The gauge factor of the non-abelian article acts on matter by **left multiplication**, and on the left regular module $S\oplus S$ left multiplication by $U$ acts as $U$ on both columns. The two columns carry the **same** representation: the action is vector-like. $SU(2)_L$ is a **chiral** gauge symmetry — its left-handed doublets and right-handed singlets transform inequivalently — so the vector-like $\mathrm{SU}(2)$ of the algebra is not $SU(2)_L$, however compact and however correctly normalized. The chirality problem must be resolved first, and it is not resolved.

**The chirality problem is upstream and open.** What the framework has is exact chirality kinematics on the module (the projectors, the mass bilinear, the selection rule) and an abelian chiral covariant derivative $D_\mu = \partial_\mu + \tfrac{i}{\hbar}A_\mu Q$ with $Q = q_LP_L+q_RP_R$. What it does not have is a **non-abelian chiral** gauge group: a non-central action of a compact factor under which the two chiral halves transform inequivalently. The chiral article states the obstruction plainly — a chiral gauge action has $q_L\neq q_R$ and cannot be central, so it is not supplied by the framework's $\mathbb{B}$-valued gauge principle — and the non-abelian article supplies the algebra but not the chiral action. *The Neutrino and Majorana Fermions in Biquaternionic Form* records the same conclusion for the weak interaction: the framework "does not derive the Standard Model's chiral $SU(2)_L$ structure; it transcribes a chiral gauge theory onto the module, with the chiral assignment put in by hand." Since the assignment is put in by hand, the item is classified **no route yet**.

The reality-class gap of the non-abelian article is a second, smaller obstacle on this factor: even the connection's Hermitian-conjugation class is not settled in a single eigenspace, and the mixed assignment that does close has not been tied to a physical principle. It is classified under the known-route items in the ledger, because the computation that would settle it is a finite and identifiable check.

### $SU(3)$: nothing derives a three

**Source.** No source. **Status.** **No route yet.**

$SU(3)$ is not in the framework, on the present construction, for two independent reasons, both stated in the ceiling above: its algebra $\mathrm{SU}(3)$ has real dimension $8$, while every compact subalgebra of $\mathbb{B}$ under the commutator has dimension at most $4$; and its quark fundamental $\mathbf{3}$ would be a complex three-dimensional module, while every $\mathbb{B}$-module has complex dimension divisible by two. There is no colour group, no triplet, no octet, no colour coupling, and no confinement mechanism anywhere in the series. The article *Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda* carries this gap as its central open item and is the place where its consequences are developed; this agenda inherits the negative result and does not restate its argument.

The one candidate ever named in the series is an enlargement of the carrier — a module of the form $S\otimes X$, or an endomorphism algebra built from the algebra's own structures — in which a larger internal factor could act. It is named as a **candidate only**, because it either assumes the answer by choosing $X = \mathbb{C}^3$ or has no known outcome. Writing $SU(3)$ down and proceeding is the fabricated premise the agenda exists to prevent. **No route yet.**

**The exceptional groups are that same candidate in its extreme form.** Two instances of the enlargement dominate the literature, and both are recorded here for the same reason the smaller ones are: they are targets, not routes. The first is the $E_8$ programme, in which the gauge fields and the fermions of a generation are placed in the adjoint $\mathbf{248}$, the smallest faithful representation of $E_8$; the second is the $E_8\times E_8$ of heterotic string compactification, of rank sixteen and dimension $496$, in which the Standard-Model group is a subgroup of the commutant of a broken factor. Set against the framework's ceiling these are the same enlargement of the carrier pushed to its largest known form: the compact subalgebra of $\mathbb{B}$ has dimension at most four, the intrinsic group is $\mathrm{U}(2)$ of rank two, the module is $\mathbb{C}^2$, and a carrier able to hold a $\mathbf{248}$ or a $\mathbf{496}$ is the candidate with the largest carrier anyone has written down. Naming $E_8$ therefore does not supply the missing three, and the ledger below is unchanged by the naming.

There is a second reason to treat the exceptional rungs differently from the others, and it is not a framework argument. Whether the observed chiral fermions can be placed in $E_8$ at all, with the Standard-Model gauge group as the commutant, was examined exhaustively by Distler and Garibaldi; their conclusion is that the only embeddings compatible with the Standard-Model gauge group require the fermions to fill a complete $\mathbf{248}$, that is three generations together with a conjugate set, and that the resulting spectrum is not chiral in the required sense without additional matter or a second $E_8$. The $E_8$ rung is thus closed on its own terms, before the framework's ceiling is consulted. This is a sharper version of the caution the agenda exists to enforce — that a large group is not an explanation — and it is why the exceptional candidates are recorded here with a negative result attached rather than as open candidates.

### The product group is not assembled: the electroweak pair as a direct sum

**Trap (b).** It is tempting to assemble the two available factors, add colour, and write the Standard Model's gauge group. That would be naming the target and calling it the result.

What the framework's compact algebra actually is, as a Lie algebra, is $\mathrm{U}(2) = \mathrm{U}(1)\oplus\mathrm{SU}(2)$ — locally the same direct sum $\mathrm{SU}(2)\oplus\mathrm{U}(1)$ that the electroweak sector has. The resemblance is real and it is where it stops. The framework's $\mathrm{U}(1)$ is the **center** of the full algebra and acts as a scalar on the algebra's module, giving equal charges to all components; the Standard Model's $U(1)_Y$ is chiral, with independent left and right eigenvalues and a definite assignment pattern. The framework's $\mathrm{SU}(2)$ acts vector-like, not as $SU(2)_L$. No **mixing angle** exists, because a mixing angle is a relation between two independent couplings and the framework supplies no relation; even the relative normalization of the two factors is unconstrained. No scalar, and therefore no symmetry breaking, is present. And the reality-class gap means that even the connection's placement in $\mathbb{M}_-\oplus\mathbb{M}_+$ is not settled.

So the honest statement of the electroweak gap, built from the two read-list sources, is: **the framework reaches the Lie algebra of the electroweak pair as a direct sum of a vector-like abelian factor and a vector-like $\mathrm{SU}(2)$, and it does not reach the pair as a theory.** The factors are present; the chiral action, the hypercharge assignments, the relative coupling, and the scalar are all absent. This account is built from the gauge-principle and non-abelian articles alone, and no separate electroweak agenda is relied upon; the gap stated here rests only on those two sources.

## The Matter Sector: Chirality, Hypercharge, Content

### The chiral-fermion issue

The Standard Model's matter is chiral: the left-handed quarks and leptons sit in $SU(2)_L$ doublets, their right-handed partners in singlets, and no gauge-invariant bare fermion mass exists. The framework reaches the **kinematics** of chirality and not its **dynamics**.

Established and inherited: the module $\Delta = S\oplus\bar{S}$; the chirality operator and the projectors; the chirality-odd mass bilinear; the chiral abelian covariant derivative $D_\mu = \partial_\mu + \tfrac{i}{\hbar}A_\mu Q$ with $Q = q_LP_L+q_RP_R$; and the selection rule $q_L = q_R$ for a gauge-invariant bare mass. These are exact and are the framework's form of the statement that a chiral fermion is massless in the unbroken phase.

Not established: a **chiral gauge group**. The framework's canonical gauge group is the scalar center, which assigns one charge to every component; the abelian chiral structure lives on the module as an operator $Q$ that is *not* an element of $\mathbb{B}$ (its chiral part is proportional to $\gamma_5$, a central element of the complexification), so it is not of the form $\tilde{A}\in\mathbb{B}$; and a non-abelian chiral action requires non-commuting generators that are not supplied. The chiral article's summary is that without those conditions **the framework has no chiral gauge group at all**. The neutrino article reaches the same place from the weak-interaction side and calls the chiral assignment an empirical input. The item is **no route yet**.

### Hypercharge is underived

The Standard Model's hypercharge is a specific $U(1)$ with a specific assignment table and a chiral action, and it is the ingredient that makes the electric charge $Q = T_3 + Y$ and cancels the gauge and gravitational anomalies. The framework has a $U(1)$ — the unitary center — but the assignment table is not derivable from it, and the word "hypercharge" does not occur in any of the sources this agenda builds on. The only abelian charge the framework possesses is a single parameter $q$, the same for every component; the gauge principle supplies no second abelian direction, no non-central abelian action is available to it, and there is no anomaly computation from which an assignment could be inferred. **No route yet.**

### The content is not selected — and what the framework supplies, counted

**Trap (c).** A count of free parameters or of fields can be read as a statement about the Standard Model if it is not said exactly what is being counted. The count given here is a count of **what the framework supplies**, and of what it does not; it is not a count of Standard Model fields and not a count of Standard Model parameters.

The framework supplies:

- **One compact gauge factor of each kind.** One abelian factor — the unitary center, real dimension $1$ — and one compact simple factor — $\mathrm{SU}(2)$, real dimension $3$ — joined in the material sector's Lie algebra $\mathrm{U}(2)$ of real dimension $4$.
- **One exact chiral module structure**, on a four-complex-dimensional Dirac module $\Delta = S\oplus\bar{S}$, with projectors, a chirality-odd mass bilinear, and the selection rule.
- **The general connections, curvatures, Bianchi identities, and gauge-invariant densities** on the two factors, each carrying a coupling parameter whose value the algebra does not fix, and with no relation between the two couplings.

The framework does not supply, and nothing in the series derives: a colour group or colour representation; a chiral $SU(2)_L$; a hypercharge value or assignment; a mixing angle; a scalar field with the Standard Model's quantum numbers, its potential, or its vacuum expectation value; a Yukawa coupling; the number of fermion generations or the representation content of any generation; or a relation among the couplings of its factors. These are the absent objects. Writing a number here for the Standard Model — three colours, three generations, a stated hypercharge — would be importing the target; the agenda counts only the framework's own objects, and the count is short.

## The Scalar and Symmetry-Breaking Sector: Unbuilt

The Standard Model's masses come from one sector the sources this agenda builds on have not begun: a scalar field with the required $SU(2)_L$ quantum numbers, its potential, its vacuum expectation value, and its Yukawa couplings to the fermions. The companion *The Higgs Mechanism in Biquaternionic Form* works the abelian mechanism for the complex central scalar $\tilde{\Phi} = \varphi\,e_0$; that scalar is a singlet of the material $\mathrm{SU}(2)$ and cannot break $SU(2)$, no Yukawa coupling is constructed, and the Standard Model's electroweak scalar sector is not built.

The framework does point at what the sector would have to do. The **mass selection rule** says that a fermion with $q_L\neq q_R$ has no gauge-invariant bare mass, so a mass can arise only through a compensating field carrying the opposite charge $q_L-q_R$; the chiral article reads off the quantum numbers such a scalar must carry. That is a statement of the **requirement**, not a construction of the object. There is no dynamics that would give the scalar an expectation value, no potential whose minimum could break the symmetry, and no coupling to the gauge sector that would give the weak bosons a mass. The framework's own mass term is the linear chiral pair, which conserves fermion number and breaks the axial symmetry; the algebra's real structure $\flat$ carries a separate conjugate pairing whose reading — Majorana-type or real-form Dirac — is open, and it is the pairing of a single fermion, not a symmetry-breaking sector.

This is the largest single missing piece on the way from the gauge machinery to the Standard Model, and it is classified **no route yet**.

## The Ledger

The table collects the agenda's items and sorts each into the three-way classification. "Established" means recomputed in the series and inherited here; "known route" means the object does not exist but the computation that would produce it is identifiable; "no route yet" means no mechanism has been proposed.

| Item | Status | Object or computation that would settle it |
|---|---|---|
| Abelian gauge principle: center $\mathbb{C}_{\mathbb{B}}$, unitary $U(1)$, connection $\tilde{A}'=\tilde{A}-\tilde{\nabla}\Gamma$, covariant derivative, curvature identity | Established (source 6) | — |
| Compact algebra in the material sector: $[e_a,e_b]=2\varepsilon_{abc}e_c$, $\mathbb{M}_-=\mathbb{R}(ie_0)\oplus\mathrm{SU}(2)=\mathrm{U}(2)$ | Established (source 5) | — |
| Non-abelian machinery: adjoint connection law, commutator curvature, Bianchi identity, gauge-invariant Yang–Mills density | Established (source 5) | — |
| Ceiling: compact subalgebra of $\mathbb{B}$ has dimension $\le 4$; every $\mathbb{B}$-module has complex dimension $2k$ | Established | — |
| Chiral module structure: $\gamma_5$, projectors, chirality-odd bilinear, chiral abelian $D_\mu$, selection rule $q_L=q_R$ | Established | — |
| Vector-like character of the center on the algebra's module | Established | — |
| Linear chiral mass with conserved vector $U(1)$; real structure $\flat$ (antilinear) | Established; reading of $\flat$'s pairing (Majorana/Dirac) open | Decide the reading on the real module |
| Reality class of the non-abelian connection | **Known route** | Recompute the transformation for the mixed assignment ($\mathcal{A}_0$ anti-Hermitian, $\mathcal{A}_k$ Hermitian) and find a principle fixing the placement of $i$; or a no-go |
| Non-abelian matter representation (source 5, open question 3) | **Known route** | Construct the $\mathrm{SU}(2)$ representation on the chosen matter module and verify $D'_\mu(U\Psi)=U D_\mu\Psi$ |
| Gauge and gravitational anomalies of a chiral spectrum | **Known route** in standard field theory; no framework realisation | A biquaternion computation of the axial-current divergence or the triangle diagram |
| Gauge-fixing principle | **Known route** in standard field theory; no framework realisation | Reproduce the Faddeev–Popov or BV procedure in the algebra, or prove a no-go |
| Electroweak mixing angle | **Known route, blocked** | Fix $U(1)_Y$ and $SU(2)_L$ and the scalar from the framework's own structure, then compute the relative coupling |
| $SU(2)_L$: chiral weak isospin | **No route yet** | A non-central compact action on $\Delta$ with inequivalent chiral halves; the chirality problem is upstream |
| $U(1)_Y$ and the hypercharge assignments | **No route yet** | A derivation of a non-central abelian direction and its assignment table; none exists in the series |
| $SU(3)$ and the number of colours $N_c=3$ | **No route yet** | A positive internal construction with a principle selecting three, or a no-go covering all enlargements; positing is not a route |
| Exceptional carriers: $E_6$, $E_7$, $E_8$, $E_8\times E_8$ | **No route yet** (targets, not candidates) | A principle selecting a carrier of dimension $27$, $56$, $248$ or $496$; the $E_8$ case is closed on its own terms by Distler–Garibaldi |
| Scalar and symmetry-breaking sector | **No route yet** | A biquaternion scalar in the required non-abelian representation, with a symmetry-breaking potential, a vacuum expectation value, and Yukawa couplings |
| Fermion generations and representation content | **No route yet** | A principle selecting the matter content; none is proposed |
| Empirical contact | Open | A prediction distinguishing the framework from the Standard Model |

## What Would Settle It

The obstacles are not independent, and the dependency chain is short.

The three **upstream** items are (1) the **chirality problem** — a non-central compact action on the module under which the two chiral halves transform inequivalently; (2) the **hypercharge problem** — a non-central abelian direction with a derivable assignment table; and (3) the **scalar sector** — a biquaternion scalar with a potential, an expectation value, and Yukawa couplings. Everything else hangs from them. Weak isospin needs (1); the electroweak pair needs (1) and (2) together; the mixing angle needs (1), (2), and (3); fermion masses need (3); and the anomaly conditions need a chiral spectrum first, which is (1).

Two further items are upstream in a different sense, because they are prerequisites for stating any of the above as a framework result rather than a transcription. The **reality class of the connection** must be settled, since a gauge factor whose connection cannot be assigned a definite conjugation behaviour cannot be cleanly identified with a Standard Model factor; and the **matter representation** must be constructed, since the non-abelian article's connection acts by left multiplication and the representation carried by the matter field has not been specified. Both are classified as known routes precisely because the computations are finite and identifiable: the first is a transformation check, the second is a covariance check, and both were performed in the parents for the cases they consider.

What is **not** on this list, and is the point of the agenda, is a derivation of the Standard Model. None of the three upstream items exists; colour does not exist for independent reasons; and no item on the list, if settled, would by itself produce the Standard Model. The three-way classification is not a schedule with three phases; it is a statement that some of the framework's gaps have a computation attached and some do not, and that the boundary between them is where the honest description of the framework's relation to the Standard Model lies.

Finally, the genre's standing caution applies here in its strongest form. *The Empirical Status of the Biquaternion Framework* records that on every domain developed, the framework is so far empirically equivalent to the standard theory it reformulates. A biquaternionic Standard Model, if one is ever constructed, would inherit that position unless it makes a prediction the Standard Model does not; and a theory whose gauge group, matter content, hypercharge, and scalar sector are all imported has no prospect of doing so. The agenda's most useful output may be to make that consequence visible early, rather than to produce a construction that appears to answer the Standard Model while assuming all of it.

## The Gürsey Reading, the Reversion Test, and the Einstein–Mayer Equation

A short 2001 comment by Gsponer and Hurni is the most useful *methodological* source on this agenda's own problem — why biquaternion and Clifford reformulations of Dirac's, Proca's and Maxwell's theories keep producing results that look new and are not. Nothing in it is a new equation; its value is diagnostic and criterial, and the corpus records it because it supplies the default reading for "extra" components and an operational legitimacy test.

**The diagnosis, and the Gürsey reading.** Compared with matrix or tensor formulations, Clifford-number formulations suffer losses of information (the numbers carry no spinor or tensor indices), ambiguities from noncommutativity and residual definitional freedom, and — the difficulty this agenda meets most often — an **increase in the number of components** when a vector or a spinor is replaced by a Clifford number, and again when an ordinary scalar such as the mass is promoted to one. The comment's fifth difficulty is the one the corpus's own algebra is exempt from: with a **real** Clifford algebra in place of a complexified one the quantum-mechanical imaginary is left implicit, and the authors record the well known fact that "if '$i$' is not explicit in a quantum theory, it must be replaced by the definition of special rules or by an equivalent antiunitary operator." The comment chooses the biquaternions precisely because they are the complexified algebra, $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, in which there are no difficulties with the quantum interpretation; the corpus's central scalar imaginary is the explicit $i$ the condition demands. That is the one place in this list where the framework's *choice of algebra* is not a matter of taste, and it is the positive side of a fact recorded in *The Empirical Status of the Biquaternion Framework*: quaternionic quantum-statistical deviations are unavailable there because the algebra is complex and associative — the same complexification that forecloses the deviations is what leaves the quantum interpretation unrestricted.

The comment records that these difficulties were met long ago (Lanczos, Proca, Einstein) and that in the reading **Gürsey** initiated they are resolved by recognising that **most such generalizations describe superpositions of particles of different intrinsic spin and isospin**. The worked instance is the simplest generalization of the Dirac equation: replacing the two Weyl spinors by two biquaternions $A$, $B$ gives Lanczos's fundamental system $\nabla A = mB$, $\nabla B = mA$, invariant under $A\to AG$, $B\to BG$ with $G$ unitary, and the doubled solution count is the **isospin doublet** of the two spin-$\frac12$ superpositions

$$
D_+ = A\sigma + B^{*}\bar{\sigma},
\qquad
D_- = (A\bar{\sigma} - B^{*}\sigma)\,i\vec{e}_1 ,
$$

with $\sigma=\tfrac12(1+i\vec{e}_3)$ an idempotent and $\bar{\sigma}$ its conjugate. Each is a **bispinor** — one half of $A$ in one minimal left ideal and half of the conjugate of $B$ in the other — and the two differ by the exchange of the idempotents and by the postmultiplication by $i\vec{e}_1$, the unit vector perpendicular to the axis $\vec{e}_3$; both satisfy the Klein–Gordon equation and the combined form $\nabla D = mD^*ie_3$, which is strictly equivalent to Dirac's. The isospin reading is the comment's resolution of the doubling: the interpretation of $D_+$ and $D_-$ as an isospin doublet, which the comment attributes for the first time to Gürsey, is what "solves the 'doubling' problem that puzzled Lanczos", and the same authors' Hamilton review draws out the particle content — $D_+$ the proton, $D_-$ the neutron, hence Lanczos's doubling is isospin. The corpus's default reading of an "extra" component in a biquaternion reformulation should be this one — an isospin or spin multiplicity — and not new physics. It is the interpretive companion of the framework's repeated structural finding that the algebra contains more than the physics selects.

**The legitimacy test.** The comment states the requirement under which such a formulation is to be trusted: every field must be an **irreducible representation of the full Poincaré group, including the discrete space and time reversal symmetries**, and must be **covariant under reversion** — a requirement the authors call specific to any theory written with Clifford numbers. This is a checkable filter, and it gives the corpus's discrete-symmetry material an operational role. The conjugations and their fixed spaces, reversion among them, are catalogued in *Comparison of the Six Subspaces*; the discrete-symmetry result is in *The CPT Theorem in Biquaternionic Form*; and the general identification of reversal with Clifford reversion is in *The Dirac Algebra and Biquaternions — A Dictionary*. The corpus records the filter with the source's own qualifier: it is a condition a Clifford-number formulation must meet, not a theorem that every biquaternion equation meets.

**The Einstein–Mayer equation: a paper route to the scalar sector.** Promoting the mass $m$ to a biquaternion $E$ — the "hypercomplex mass", whose general form the comment attributes to Einstein and Mayer — gives

$$
\nabla A = B E^{\dagger},
\qquad
\nabla B = A E ,
$$

so that the pair no longer shares one mass: the second-order equations become eigenvalue equations for it. The comment records the two standard readings. When $E E^{\dagger} = m^2$ the pair is degenerate and reads as a **proton–neutron** isospin doublet, and with a pseudoscalar $E$ the charge-independent theory of nuclear forces; when $E E = 0$ one of the two masses necessarily vanishes and the pair reads as an **electron–neutrino** doublet, and with a parity-violating $SU(2)$ gauge the low-energy weak phenomenology is equivalent to the Standard Model's. Two algebraic facts make both readings available, and both were checked: the product of a biquaternion with its quaternion conjugate is central and equals $\sum_i q_i^2$, so a real scalar coefficient $E = s$ gives the same mass $m^2 = s^2$ to both members of the pair; and the null equation $E \circ E = 0$ has nonzero solutions — the zero divisors, of which $E = e_1 + i e_2$ is one. Carried further, if $E$ is derivatively coupled, $\nabla E = AB$, the system gives Petiau's double-periodic waves, interpolating between de Broglie and solitonic solutions; and if $E$ is read as the Higgs field, $\Box E = -\mu E + \lambda E E^{\dagger} E$ is invariant under $E \to G^{*} E H$ and carries the manifest $SU(2)_L\times SU(2)_R$ symmetry of the sigma-model that leads to the electroweak theory after the $SU(2)_R$ breaking. This is precisely the **scalar and symmetry-breaking sector** the ledger above marks *no route yet*, and it is worth recording that the literature route exists on paper and dates from 1932 — while noting the source's own verdict, which is that its outputs are Standard Model re-descriptions and not derivations.

**The prior-art warning.** The comment's conclusion is that, under the two conditions above, many of the difficulties of noncommutative Clifford numbers can be overcome and that **most, if not all, apparently new results can be interpreted using standard concepts and without introducing new physics**. That is the corpus's own standing caution (*The Empirical Status of the Biquaternion Framework*) stated in 2001 by authors sympathetic to the programme, and it is recorded here for exactly that reason: the corpus should be able to cite an external statement of the discipline it practises, not merely assert it. The same authors' review work argues the opposite side — that the physics can reside in the mathematical structure — and the corpus records both, since a programme's value and its novelty are different questions.

**The stronger companion claim.** The same two authors made a much stronger claim in an earlier, shorter place: a four-page contribution to the Cornelius Lanczos centenary conference (1994, arXiv:hep-ph/0112317), which argues for the Lanczos quaternionic equation as a **replacement** for Dirac's equation. It is a different item from the 2001 comment above, and the bibliography must keep the two apart. The claim is worth recording because it takes the Einstein–Mayer route from a *paper possibility* to asserted *consequences*, and it is the only place the corpus knows where that route is pushed to particle content.

- **Unified spins.** The quaternionic equation is said to describe, in one framework, particles of spin $0$, $\tfrac12$, $1$ and $\tfrac32$.
- **Two classes of solutions.** Point-like **partons** in two families, **quarks and leptons**; and **extended hadrons**.
- **Quantum numbers from the equations.** The electric charges come out correct and fractional or integral as required, and **baryonic charge** is carried; the **neutrino and the u-quark masses are zero by eigenvalue equations** — a claim the same authors partly withdraw in the 1996 note recorded below.
- **Electroweak sector.** Claimed **identical to the Standard Model's, with the same two free parameters $e$ and $\sin^2\theta$**, and **no Higgs symmetry-breaking mechanism**.
- **The paper's own concession.** For the extended-hadron class, no simple mass eigenvalue equation is claimed and the **strong interaction is essentially non-local**.

This bears on the agenda in two places, and in opposite directions.

It bears **positively on the scalar sector**, which the ledger marks *no route yet*. The Einstein–Mayer generalized mass makes the masses eigenvalues of a mass operator rather than outputs of a symmetry-breaking vacuum, so the missing non-abelian scalar is not needed for mass generation. That is the one route the corpus knows of that would bypass the singlet problem, and it is recorded here as such.

It bears **neutrally on the ledger's other rows and not at all on empirical contact**. The electroweak sector is claimed to have the *same two* free parameters as the Standard Model, so nothing is derived about the couplings; only the mass sector changes. And the two natural tests are the two the corpus already applies. First, the **same sector also masses the $W$ and the $Z$**, and a Higgs-free account owes a relation for those masses; the source exhibits none in the abstract. Second, the observable content of a mass-generation mechanism is the **pattern** — the charged-fermion ratios, the two mass-squared differences, the mixing angles — and an eigenvalue equation earns its place only by fixing that pattern, not by producing non-zero eigenvalues for some entries. The source does not exhibit the pattern. It is precisely the empty cell of *Derived Dimensionless Relations* in the empirical-status article, and it stays empty until a ratio is produced.

For the **charge-quantisation question** the paper is the corpus's nearest thing to an answer and does not settle it. That the framework should explain why the charges are $0,\pm\tfrac13,\pm\tfrac23,\pm1$ rather than assuming a representation that carries them is a natural demand the corpus has not met. The claim here is that the charges *come out* of the equations rather than being assigned — which is the right form of answer — but a four-page abstract does not display the derivation, and the corpus's own test applies: a construction that **encodes** the assignment in its choice of representation has not explained quantisation, and only a derivation that the assignments are **forced** would. The baryonic-charge point is new for the corpus in that the proton article records baryon number as *outside* the framework and not constructed; the claim here is that it is carried by the algebraic solutions. Both remain claims attached to a four-page source.

**The authors' own 1996 note, and the currents behind the claim.** The arXiv version of this item carries a *Note added in 1996*, and it must be read with the claim, because it withdraws the charge-quantisation mechanism. The printed paper argued that "a remarkable property of the Nishijima group is that it has exactly two non-trivial decompositions in a product $U(1,Q)\otimes U(1)$, such that the electric charge is quantized", the doublet carrying charges $(0,-1)$ in one and $(+\tfrac23,-\tfrac13)$ in the other, with $U(1,Q)$ the discrete ring $R_4$ or $R_6$, so that "electron charge quantization necessarily implies the existence of quark states of fractional electric charge". The 1996 note states plainly that "the restriction of the Nishigima group to $U(1,Q)\otimes U(1)$ is not sufficient to set the correct fractional or integral electric and baryonic charges of the quarks and leptons". The test applied above — are the assignments *forced* by the equations, or *encoded* in the choice of representation? — is therefore answered in the negative by the source itself, and the charge-quantisation cell stays empty on the authors' word rather than on the corpus's inference.

The algebraic objects behind the claimed quantum numbers are worth recording, because they are the corpus's nearest thing to a baryon-number carrier. The paper exhibits **two conserved currents**, the probability current and the **barycharge** current,

$$C = AA^{+} + BB^{+}, \qquad S = AEA^{+} + BEB^{+},$$

and the distinction between them is the whole content of the gauge statement: $C$ is invariant under *any* non-abelian unitary gauge transformation $SU(2)\otimes U(1)$ of $A$ or $B$, whereas $S$ is invariant only for abelian gauge transformations that also commute with the generalized mass $E$ — "the general Nishijima group, which contains the electric and baryonic gauge groups". The route therefore gives baryon number an abelian current of its own, and not only a place in the classification of solutions. That is the object the proton article cites, and the 1996 note is the reason it is cited there as unfulfilled.

**The evidential tier.** Both items are recorded in the lowest tier the corpus uses, and the reason is the medium rather than the authors. Gsponer and Hurni are careful workers on Lanczos's electrodynamics, and the corpus already cites their *Foundations of Physics* paper; but a four-page conference abstract asserting a replacement for the Dirac equation, the quark–lepton spectrum, the absence of a Higgs, and a non-local strong interaction contains **no derivation**, and the paper's own title is a **question**. The register is therefore correct in the source, and the corpus matches it: **claims reported, derivations not available in this source**, pointer to a programme with a history. The "parton" terminology is also historically loaded — the paper's two families are quarks and leptons, the modern reading — and "baryonic charge" is the paper's own term.

## Summary

This article is a research agenda for the Standard Model inside the biquaternion framework. Its finding is that the framework reaches the general machinery of an abelian and a non-abelian gauge theory, on the largest compact algebra the algebra admits, together with an exact chiral structure on its spinor module — and that it stops before the Standard Model, whose gauge group, chiral action, hypercharge, and scalar sector it does not derive.

What is established is recalled: the abelian gauge principle on the center, with $U(1)$ canonically attached and the connection law $\tilde{A}'=\tilde{A}-\tilde{\nabla}\Gamma$; the compact algebra inside the material sector, $\mathbb{M}_- = \mathbb{R}(ie_0)\oplus\mathrm{SU}(2)$, with the full non-abelian construction — adjoint connection, commutator curvature, Bianchi identity, gauge-invariant Yang–Mills density; the ceiling, that a compact subalgebra of $\mathbb{B}$ on the present construction has real dimension at most $4$ and every $\mathbb{B}$-module has even complex dimension; and the chiral module structure, with exact projectors, a chirality-odd mass bilinear, and the selection rule $q_L=q_R$.

What is not established is everything Standard-Model-specific.

- **$U(1)$.** The abelian gauge factor exists and is canonical, but it is vector-like on the algebra's module and supplies one charge, not a hypercharge assignment table. **No route yet.**
- **$SU(2)$.** The compact algebra and its gauge machinery exist, but the factor acts vector-like, so it is **not** $SU(2)_L$; weak isospin is chiral and the chirality problem is unresolved. The isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$, whose commutator algebra contains $\mathrm{SU}(2)$, is a coincidence of algebra, not a derivation of weak isospin. **No route yet.**
- **$SU(3)$.** Nothing derives a colour group or a three-valued internal structure; the dimension ceiling and the module-dimension parity forbid both on the present construction. **No route yet.**
- **The product.** The framework's compact algebra $\mathrm{U}(2)$ is locally the electroweak direct sum $\mathrm{SU}(2)\oplus\mathrm{U}(1)$, but the abelian factor is vector-like, no hypercharge assignment is derived, and the relative coupling and mixing angle are unconstrained. The factors are present as a direct sum; the electroweak theory is not.
- **The matter sector.** The chirality kinematics are exact; the chiral gauge group is absent, the hypercharge is underived, and the representation content and generation number are not selected. **No route yet.**
- **The scalar sector.** Unbuilt. The mass selection rule names what a compensating scalar would have to carry, and the framework supplies no scalar field with the required quantum numbers, and no corresponding potential, expectation value, or Yukawa coupling. **No route yet.**

The obstacles with a known route are the finite, identifiable ones: the reality class of the non-abelian connection, the non-abelian matter representation, the anomaly, the gauge-fixing principle, and — conditional on the no-route items above — the electroweak mixing. The upstream items are the chirality problem, the hypercharge problem, and the scalar sector. None of them exists, and settling none of them would by itself produce the Standard Model.

The article commits throughout to the agenda's central discipline: no section assumes a Standard Model structure, the three gauge factors are each stated with their source and status, and where standard numbers appear they are marked as imports. **The honest boundary is the result.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H} \cong M_2(\mathbb{C})$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_1e_2=e_3$ |
| $i$ | Scalar imaginary, $i^2=-1$, central |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors; $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ | Center of the algebra; source of the abelian gauge group |
| $\tilde{\nabla} = e_0\partial_{ict}+e_k\partial_k$ | Biquaternionic gradient |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural}$ | d'Alembertian |
| $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$ | Abelian connection (in $\mathbb{M}_-$) |
| $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$ | Abelian gauge transformation |
| $D = \tilde{\nabla} + \tfrac{iq}{\hbar}\tilde{A}$ | Abelian covariant derivative |
| $[e_a,e_b]=2\varepsilon_{abc}e_c$, $T_a=\tfrac12 e_a$ | Commutator and normalized generators of $\mathrm{SU}(2)\subset\mathbb{M}_-$ |
| $\mathbb{M}_- = \mathbb{R}(ie_0)\oplus\mathrm{SU}(2)=\mathrm{U}(2)$ | Material-sector Lie-algebra decomposition (dimension $4$) |
| $\mathcal{A}_\mu\in\mathrm{SU}(2)$, $\kappa=q/\hbar$ | Non-abelian connection and coupling |
| $F_{\mu\nu}=\partial_\mu\mathcal{A}_\nu-\partial_\nu\mathcal{A}_\mu+i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$ | Non-abelian field strength |
| $F'_{\mu\nu}=UF_{\mu\nu}U^{-1}$, $[D_\mu,D_\nu]=i\kappa F_{\mu\nu}$ | Adjoint transformation law and curvature identity |
| $D_\lambda F_{\mu\nu}+\text{cyclic}=0$ | Bianchi identity |
| $-\tfrac12\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$ | Gauge-invariant Yang–Mills density |
| $\mathrm{GL}(2,\mathbb{C})=\mathrm{U}(2)\oplus i\,\mathrm{U}(2)$ | Cartan decomposition fixing the ceiling: maximal compact subalgebra $\mathrm{U}(2)$ |
| $\Delta = S\oplus\bar{S}$, $S=\mathbb{C}^2$ | Dirac module; every $\mathbb{B}$-module has complex dimension $2k$ |
| $\gamma_5$, $P_L=\tfrac12(I_4-\gamma_5)$, $P_R=\tfrac12(I_4+\gamma_5)$ | Chirality operator and projectors |
| $\bar\Psi\Psi$, $Q=q_LP_L+q_RP_R$ | Chirality-odd mass bilinear; chiral charge operator; selection rule $q_L=q_R$ |
| $\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L,\ \tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R$; $\tilde{\Psi}^{\flat}=-\tilde{\Psi}^{*}$ | Linear chiral mass pair; algebra real structure $\flat$ (Majorana/Dirac reading of its pairing open) |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Inherited informational trace formula |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| **Standard-model notation, not framework objects** | |
| $SU(3)_c$, $SU(2)_L$, $U(1)_Y$ | Colour, weak-isospin and hypercharge groups — no route yet |
| $T_3$, $Y$, $Q=T_3+Y$ | Weak isospin, hypercharge, electric charge — underived |
| $\theta_W$ | Electroweak mixing angle — no relation supplied |
| Higgs doublet, vacuum expectation value, Yukawa coupling | Scalar and symmetry-breaking sector — unbuilt |

## Further Reading

- *The Gauge Principle in Biquaternionic Form* — the abelian gauge principle, the center and its unitary part, the connection, the covariant derivative, and the origin of the $U(1)$ factor this agenda follows.
- *Non-Abelian Gauge Fields in Biquaternionic Form* — the immediate parent; the decomposition $\mathbb{M}_-=\mathbb{R}(ie_0)\oplus\mathrm{SU}(2)$, the adjoint connection and curvature, the Bianchi identity, the gauge-invariant density, and the open reality-class gap.
- *The Covariant Derivative and Gauge Connection in Biquaternionic Form* — the abelian connection whose non-abelian extension the parent builds.
- *Chiral Fermions in the Biquaternion Framework* — the module's chirality structure, the vector-like center, the mass selection rule, the linear mass and the real structure, and the statement that the framework has no chiral gauge group.

- *The Neutrino and Majorana Fermions in Biquaternionic Form* — the Dirac/Weyl/Majorana distinction, the real-structure reading, and the explicit statement that the chiral $SU(2)_L$ assignment is empirical input.

- *Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda* — the colour gap, the ceiling on the gauge algebra, and the three-way classification this article shares.
- *The Renormalization Group in Biquaternionic Form* — the one-loop non-abelian beta function and the article's own statement that the group, matter, action, and regulator are inputs; the caution against reading a transcription as a derivation.
- *Modules over the General Plain Algebra of Biquaternions* and *Lie Algebras: A General Introduction* — the module structure and the compact-subalgebra facts behind the ceiling.
- *The Spinor Module in Biquaternionic Form and Its Lorentz Action* and *The Dirac Equation in Biquaternionic Form* — the spinor module, the mass term, and the real-structure origin of chirality.

- *Biquaternion Ideals and Peirce Decomposition* — the ideal decomposition, distinguished from the chiral and sector decompositions.
- *The Spinor-Helicity Formalism and Biquaternions* — the corpus's explicit statement that the framework "does not contain a colored gauge theory"; the transcription boundary this agenda makes systematic.
- *The Empirical Status of the Biquaternion Framework* — the standing empirical-equivalence result, the caution under which any biquaternionic Standard Model would labour.
- A. Gsponer and J.-P. Hurni, "Comment on Formulating and Generalizing Dirac's, Proca's, and Maxwell's Equations with Biquaternions or Clifford Numbers", *Foundations of Physics Letters* **14**(1) (2001) 77–85 (arXiv:math-ph/0201049), for the Gürsey isospin reading of the doubled solutions, the Poincaré-and-reversion legitimacy test, and the Einstein–Mayer equation with its proton–neutron, electron–neutrino, Petiau-wave, and Higgs readings.
- A. Gsponer and J.-P. Hurni, "Lanczos's Equation to Replace Dirac's Equation?", *Proceedings of the Cornelius Lanczos International Centenary Conference* (SIAM, 1994) 509–512 (arXiv:hep-ph/0112317), the same authors' stronger and earlier claim, for the Lanczos quaternionic equation as a replacement for Dirac's, for spins $0,\tfrac12,1,\tfrac32$ in one framework, for quarks and leptons with electric and baryonic charge read from the equations (neutrino and u-quark masses zero by eigenvalue equations), for extended hadrons with a non-local strong interaction, and for an electroweak sector claimed identical to the Standard Model's with no Higgs mechanism. Recorded as a claim: four pages, no derivation exhibited, and the title is a question.
- C. Lanczos, "Die tensoranalytischen Beziehungen der Diracschen Gleichung", *Zeitschrift für Physik* **57** (1929) 447–473 and 474–483, for Lanczos's fundamental equation and the doubling it implies.
- F. Gürsey, *Il Nuovo Cimento* **7** (1958) 411–415, for the isospin interpretation of the doubling.
- A. Einstein and W. Mayer, "Semi-Vektoren und Spinoren," *Sitzungsberichte der Preussischen Akademie* (1932) 522–550, for the generalization in which the mass becomes a Clifford coefficient. This is **not** the same paper as "Die Diracgleichung für Semivektoren," *Proceedings of the Royal Academy of Amsterdam* **36** (1933) 497–516, 615–619, which is the **Lagrangian formulation** the centenary contribution and the companion article *The Petiau System and the Quantisation of Mass in Biquaternionic Form* use; the two are distinct items of the same authors and a reader checking one against the other should keep them apart.
- Jacques Distler and Skip Garibaldi, "There is no $E_8$ gauge theory with three generations" (arXiv:0905.2658), for the exhaustive check that the Standard Model's chiral fermions do not fit in $E_8$ with the Standard-Model gauge group as the commutant; the basis of the ledger row on the exceptional carriers.
- Garrett Lisi, "An exceptionally simple theory of everything" (arXiv:0711.0770), for the $E_8$ programme that places one generation of fermions and the gauge fields in the adjoint $\mathbf{248}$; recorded as the instance of the exceptional candidate, and as a target rather than a route.
- David J. Gross, Jeffrey A. Harvey, Emil Martinec and Ryan Rohm, "Heterotic string theory (I). The free heterotic string", *Nuclear Physics B* 256 (1985) 253–284, for the $E_8\times E_8$ gauge group that this agenda's ledger records as the top rung of the rank ladder.
- G. Petiau, *Il Nuovo Cimento* **40** (1965) 84–101, for the double-periodic waves of the derivatively coupled system.
- *The Einstein Field Equations under the Biquaternion Framework — A Research Agenda* — the companion agenda whose three-way classification and settling-object discipline this article follows.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* and *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* — the two sectors, the four-vectors, and the trace formula on which the whole account rests.
- *Introduction to the Biquaternion Universe* — the algebra, the conjugations, and the research-program framing inherited throughout.

