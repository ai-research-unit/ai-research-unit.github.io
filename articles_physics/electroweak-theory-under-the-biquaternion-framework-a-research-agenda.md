# __Electroweak Theory under the Biquaternion Framework — A Research Agenda__

## Introduction

**Electroweak theory** is the gauge theory of the weak and electromagnetic interactions: a gauge theory with group $SU(2)_L \times U(1)_Y$, matter in **chiral** representations — left-handed quarks and leptons in $SU(2)_L$ doublets and their right-handed partners in singlets — a scalar doublet whose vacuum expectation value breaks the symmetry to the electromagnetic $U(1)$, and massive $W^\pm$ and $Z$ bosons alongside the massless photon. Two features are structural rather than incidental. The gauge group acts *inequivalently* on the two chiralities, so no bare fermion mass is gauge invariant; and the fermion masses exist only because of the scalar sector, whose vacuum expectation value carries the charge the mass term lacks. This article is a research agenda for electroweak theory inside the biquaternion framework. Its subject is not a result; it is the boundary between what the framework has built and what electroweak theory requires.

The starting position is stated at the outset, because the whole agenda depends on it and because it is easy to overstate.

- **The framework has an abelian gauge principle.** It has a canonical central $U(1)$, a connection, a transformation law, a covariant derivative, and a curvature, together with the statement that the framework cannot fix the gauge. This is established and is recalled in the next section.
- **The framework has a non-abelian gauge field construction, and the algebra it needs is present.** The material sector decomposes as a Lie algebra, $\mathbb{M}_- = \mathbb{R}(ie_0)\oplus\mathfrak{su}(2)$, so the compact algebra available is $\mathfrak{u}(1)\oplus\mathfrak{su}(2)=\mathfrak{u}(2)$, of real dimension four. That is exactly the dimension count of the electroweak gauge group. It supplies the **algebra** of a non-abelian gauge theory. It does **not** supply a **chiral** gauge theory, and the two are different objects.
- **The framework has not constructed the electroweak sector.** Nothing derives weak hypercharge; no chiral non-abelian matter representation is built; there is no scalar sector, no symmetry breaking, and no Yukawa coupling; and the framework's inability to fix the gauge bounds the physical content of any orbit.

The word "electroweak" occurs in the corpus only where standard theory is being named or imported. *The Dirac Equation in Biquaternionic Form* states that the framework "does not by itself derive the mass term or the electroweak structure". *The CPT Theorem in Biquaternionic Form* records the electroweak relevance of the discrete operations $C$ and $P$ and says plainly that it "is imported". *The Neutrino and Majorana Fermions in Biquaternionic Form* names a dimension-five operator arising "after electroweak symmetry breaking" as something the framework does not represent. No article constructs $SU(2)_L\times U(1)_Y$, a hypercharge assignment, a Higgs doublet, or a $W$ or $Z$ field.

The discipline this forces on the article is the one the genre requires: **an agenda that quietly assumes hypercharge or chirality has fabricated its own premise.** Both are therefore carried as **open items throughout**, never as working assumptions. Wherever a standard electroweak statement is written down — the group, the hypercharge values, the Weinberg angle, the Higgs doublet, the $W$ and $Z$ masses — it is flagged as standard input, not as a framework result.

**The three-way classification.** The article sorts every item into one of three categories, and the distinction is the point of the agenda.

1. **Established.** Recomputed in the series and inherited here; the abelian gauge principle, the non-abelian construction on $\mathfrak{su}(2)$, the Lie-algebra decomposition $\mathbb{M}_- = \mathbb{R}(ie_0)\oplus\mathfrak{su}(2)$, and the chiral structure on the spinor module.
2. **Obstacle with a known route.** The object does not exist, but the route to it is identifiable, usually because standard field theory supplies the computation and the framework must reproduce it on its own carrier, or because the object can be built on a declared carrier at the cost of leaving the framework's own construction.
3. **Obstacle with no route yet.** No mechanism has been proposed, and naming an object is not the same as having a route to it. The hypercharge values and a gauge-fixing principle are in this class.

The four obstacles the agenda treats are the **chiral-fermion obstacle** (the framework's non-abelian construction is vector-like on the spinor module), **weak hypercharge** (nothing derives it), the **scalar sector and symmetry breaking** (needed for masses, not available), and the **inability to fix the gauge** (which bounds the physical content of any orbit). They are not independent: the scalar sector needs the chiral action and the hypercharge assignments, and every physical statement about masses needs a gauge fixing. A closing ledger collects them, and a short synthesis names the upstream items.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_1e_2 = e_3$, and $i$ is the scalar imaginary, $i^2 = -1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector), with $\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+$; $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the center. The biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$, its quaternion conjugate is $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_1\partial_x - e_2\partial_y - e_3\partial_z$, and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$. The matrix realization is $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ with $\Phi(e_0)=I_2$, $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$; the spinor module is $S=\mathbb{C}^2=(\tfrac12,0)$, its conjugate $\bar{S}=(0,\tfrac12)$ is the right-handed Weyl module, and $\Delta = S\oplus\bar{S}$ is the Dirac module with chirality operator $\gamma_5$ and projectors $P_L = \tfrac12(I_4-\gamma_5)$, $P_R = \tfrac12(I_4+\gamma_5)$. For the non-abelian sector we use the $\mathfrak{su}(2)$ connection and field strength of the read list, $\mathcal{A}_\mu \in \mathfrak{su}(2)$, $F_{\mu\nu} = \partial_\mu\mathcal{A}_\nu - \partial_\nu\mathcal{A}_\mu + i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$, $\kappa = q/\hbar$, with $[D_\mu,D_\nu] = i\kappa F_{\mu\nu}$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the **speed of light in the medium** and $c_0$ the vacuum speed of light. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged. The symbols $SU(2)_L$, $U(1)_Y$, $Y$, $T_3$, $\theta_W$, $W^\pm$, $Z$, $H$, $v$, and the hypercharge assignments are **standard electroweak notation, not framework objects**; they are used only where standard results are being quoted or where an object is being named as missing. The framework's non-abelian coupling is written $\kappa=q/\hbar$, never $g$ or $g'$.

## What the Framework Already Reaches

### The abelian gauge principle

The read-list article *The Gauge Principle in Biquaternionic Form* derives the abelian gauge structure from the center of the algebra. Its results are established and are used here unchanged.

The center is $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_\mathbb{R}\{e_0, ie_0\}$, and its unitary part is $U(1) = \{e^{i\theta}\}$. A constant central phase is a symmetry of the massless biquaternion field equation, because a central constant passes through the gradient. Localizing it, $\lambda(\tilde{X}) = e^{iq\Gamma(\tilde{X})/\hbar}$ with real $\Gamma$, forces a connection $\tilde{A}$ with the transformation law

$$
\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma,
\qquad
D = \tilde{\nabla} + \frac{iq}{\hbar}\tilde{A},
\qquad
D_\mu = \partial_\mu + \frac{iq}{\hbar}A_\mu,
$$

under which the field equation is gauge covariant. The curvature is the abelian $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$, with $[D_\mu,D_\nu] = \tfrac{iq}{\hbar}F_{\mu\nu}$, and a real gauge function keeps $\tilde{A}$ in the material sector $\mathbb{M}_-$. The coupling $q$ is a parameter: the algebra does not fix its value.

Two inherited facts bear directly on this agenda. First, the **gauge group is canonically attached**: it is the unitary part of the center, and no choice is made in selecting it. Second, the **mass term is linear and passes the continuous central phase**: the framework's Dirac mass is the linear chiral pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$, so the vector $U(1)$ is conserved for the massive field and the broken symmetry is the axial one. The algebra's anti-linear object is the real structure $\tilde{\Psi}^{\flat} = -\tilde{\Psi}^{\dagger}$: because $\flat$ is anti-linear, $(\lambda\tilde{\Psi})^{\flat} = \lambda^{*}\tilde{\Psi}^{\flat}$, so a conjugate coupling built on it would survive the continuous central phase only for real $\lambda$, i.e. only $\lambda = \pm 1$ — a discrete $\mathbb{Z}_2$, not the continuous $U(1)$. Whether the framework deploys such a coupling is the open Majorana reading.

Finally, the same article and its parents record the negative fact that the framework **cannot fix the gauge**. That fact is treated here as an obstacle in its own right, because every statement about a massive vector spectrum is normally a statement in a fixed gauge.

### The non-abelian construction, and the algebra it runs on

The read-list article *Non-Abelian Gauge Fields in Biquaternionic Form* builds the general non-abelian gauge structure inside $\mathbb{B}$. Its results are established and are used here unchanged.

The vector part of the material sector closes under the commutator and is $\mathfrak{su}(2)$ in a non-standard normalization,

$$
[e_a,e_b] = 2\,\varepsilon_{abc}\,e_c, \qquad
T_a = \tfrac12 e_a,\quad [T_a,T_b] = \varepsilon_{abc}T_c,\quad \mathrm{Tr}(T_aT_b) = -\tfrac12\delta_{ab},
$$

and the material sector decomposes as a direct sum of Lie algebras,

$$
\mathbb{M}_- \;=\; \mathbb{R}(ie_0) \;\oplus\; \mathfrak{su}(2),
\qquad\text{so the compact algebra available is}\qquad
\mathfrak{u}(2) = \mathfrak{u}(1)\oplus\mathfrak{su}(2),\quad \dim_\mathbb{R} = 4 .
$$

This is the read-list article's central algebraic result, and it is the reason the electroweak question can be posed at all: the compact algebra of dimension four that electroweak theory uses is *already present in the material sector*, not adjoined. What is not present is the way electroweak theory uses it. The gauge group of the construction is the unit real quaternions, $SU(2) = \{U \in \mathbb{H}_{\mathbb{B}} : U\bar U = e_0\}$, acting on a matter field **by left multiplication**, and the connection transforms as

$$
\mathcal{A}'_\mu = U\,\mathcal{A}_\mu\,U^{-1} + \frac{i}{\kappa}\,(\partial_\mu U)\,U^{-1},
$$

with curvature $F_{\mu\nu} = \partial_\mu\mathcal{A}_\nu - \partial_\nu\mathcal{A}_\mu + i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$ transforming in the adjoint, $F'_{\mu\nu} = UF_{\mu\nu}U^{-1}$, satisfying the Bianchi identity, and admitting the gauge-invariant density $-\tfrac12\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$.

Two gaps of this construction are inherited and matter here. The first is the **matter representation**: the covariant derivative acts by left multiplication, the representation carried by the matter field is not specified, and the non-abelian version of the chiral charge operator is not constructed (the read-list article's open question 3). The second is the **reality class of the connection**: no single Hermitian-conjugation eigenspace is gauge invariant across all four components, because the $ict$ derivative $\partial_0 = -i\partial_t$ flips the conjugation behaviour of the Maurer–Cartan form in the time direction. A consistent mixed assignment exists — $\mathcal{A}_0$ anti-Hermitian traceless in $\mathfrak{su}(2)\subset\mathbb{M}_-$, $\mathcal{A}_k$ Hermitian traceless in $i\,\mathfrak{su}(2)\subset\mathbb{M}_+$ — but whether it is the intended physical assignment is not settled.

For the purposes of this agenda, the construction is the **general machinery of a non-abelian gauge theory on $\mathfrak{u}(2)$**. The dimension of that algebra matches the dimension of the electroweak gauge algebra, and the match is a coincidence of counting, not an identification. The identification fails in two ways that the rest of the article makes precise: the $\mathfrak{su}(2)$ here acts on matter by left multiplication, which is vector-like; and the $\mathfrak{u}(1)$ here is the center, whose action is scalar, which is also vector-like. Weak isospin and weak hypercharge are both chiral.

### The chiral structure on the spinor module

The read-list article *Chiral Fermions in the Biquaternion Framework* establishes the following, and this agenda inherits it without change.

The Dirac module is $\Delta = S\oplus\bar{S}$; the chirality operator is $\gamma_5 = \mathrm{diag}(-I_2,I_2)$ with $\gamma_5^2 = I_4$, and the projectors $P_L = \tfrac12(I_4-\gamma_5)$, $P_R = \tfrac12(I_4+\gamma_5)$ are idempotent, orthogonal, complete, of rank two, and Lorentz invariant, because $\gamma_5$ anticommutes with the generators and commutes with every even product. The Dirac mass bilinear $\bar\Psi\Psi = \psi_L^{\dagger}\psi_R + \psi_R^{\dagger}\psi_L$ is chirality-odd and vanishes on a state of definite chirality.

On the module, a chiral abelian gauge symmetry with independent charges is consistent: with

$$
Q = q_L P_L + q_R P_R,
\qquad
D_\mu = \partial_\mu + \tfrac{i}{\hbar}A_\mu Q,
\qquad
[D_\mu,D_\nu] = \tfrac{i}{\hbar}F_{\mu\nu}Q,
$$

the covariant derivative is gauge covariant for **arbitrary** $q_L, q_R$, and the mass bilinear is gauge invariant **if and only if** $q_L = q_R$. A genuinely chiral fermion has no gauge-invariant bare mass.

Two structural facts of that article are the hinges of this agenda. The first is that the **canonically available gauge group is vector-like**: the framework's own abelian gauge group is the unitary part of the center, which acts as a *scalar* on $M_2(\mathbb{C})$, so every component receives the same charge. Chirality requires a non-central action. The second is that the **chiral charge operator is a module endomorphism, not an algebra element**: $Q = \tfrac{q_L+q_R}{2}I_4 + \tfrac{q_R-q_L}{2}\gamma_5$, and $\gamma_5$ is a central idempotent combination of the complexification $\mathbb{C}\otimes_\mathbb{R}\mathbb{B}$, not an element of $\mathbb{B}$. The chiral structure therefore does not fit the form $\tilde{\nabla} + \tfrac{iq}{\hbar}\tilde{A}$ with $\tilde{A}\in\mathbb{B}$; it is a connection valued in the algebra of module endomorphisms, $\mathrm{End}(\Delta)$.

A qualification recorded in that article is carried here because it bears on hypercharge. The corpus does not settle how the biquaternion field is identified with the Dirac module. The left regular module is $S\oplus S$, whose two columns both carry the defining representation; the Dirac module is $S\oplus\bar{S}$, whose second factor carries the conjugate action, and the passage between them is the real structure. Under the Lorentz-conjugate assignment a central phase would act as $e^{i\theta}$ on the left half and $e^{-i\theta}$ on the right half — an **axial**, not vector-like, action. Which reading is physical is the same unsettled "two-$i$" question as the embedding of the projectors. It matters here because it decides whether the framework's abelian factor is vector-like or axial.

### The mass term and the real structure

The framework's Dirac equation carries the **linear chiral mass pair** $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$, with massless limit $\tilde{\nabla}\tilde{\Psi} = 0$. The mass is complex-linear in the field, so the continuous central phase passes through it and the vector $U(1)$ — fermion number — is conserved for the massive field; what the mass breaks is the axial symmetry, $\partial_\mu j_5^\mu = 2im\bar{\psi}\gamma_5\psi$, which vanishes only at $m=0$. The algebra's anti-linear object is the **real structure** $\tilde{\Psi}^{\flat} = -\tilde{\Psi}^{\dagger}$, order-reversing with a sign and swapping the two chiral ideals; a coupling built on it pairs the field with its conjugate. Whether the framework intends such a **Majorana-type** conjugate pairing, or whether its real structure only supplies the real-form expression of an ordinary **Dirac** mass, is not settled in the read list, and for that separate coupling the two readings differ on whether a conserved fermion number exists at all. This is inherited as an open item, and it is the pivot on which the scalar-sector question turns: a Majorana-type coupling needs no scalar doublet, whereas the linear Dirac mass for a chiral fermion needs a compensating field carrying the charge difference $q_L-q_R$ (the negative of the phase $e^{i(q_R-q_L)\Gamma/\hbar}$ the mass bilinear acquires).

## The Chiral-Fermion Obstacle: an Algebra Is Not a Chiral Gauge Theory

Electroweak theory is chiral, and this is not a detail of its matter content but the reason its masses need a scalar. The left-handed quarks and leptons sit in $SU(2)_L$ doublets; the right-handed ones are $SU(2)_L$ singlets. The framework's position is stated most sharply as a contrast between what it has and what this requires.

**What it has.** The algebra $\mathfrak{su}(2)$ is present in the material sector, by the decomposition $\mathbb{M}_- = \mathbb{R}(ie_0)\oplus\mathfrak{su}(2)$; the non-abelian connection, curvature, adjoint law, Bianchi identity, and invariant density are constructed on it; and a chiral abelian structure with independent left and right charges is constructed on the Dirac module. So both a non-abelian algebra and a chiral charge operator exist in the series — but not in the same construction.

**Why they do not meet.** The framework's non-abelian construction couples the gauge group to matter by **left multiplication** with a $\mathbb{B}$-valued connection. Under that action the two chiral halves of $\Delta$ carry the defining module and its conjugate, and for $SU(2)$ the conjugate of the doublet is **equivalent** to the doublet: the group is pseudoreal, $2\cong\bar{2}$, realized by the intertwiner $\varepsilon = \bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)$ with $\varepsilon g^{*}\varepsilon^{-1} = g$ for every $g\in SU(2)$. A gauge transformation manufactured from an element of $\mathbb{B}$ therefore cannot make the right-handed half a singlet or give the two halves inequivalent representations: it charges both halves, and it charges them equivalently. **A $\mathbb{B}$-valued connection is vector-like on $\Delta$.** The pseudoreality was checked on a generic $SU(2)$ element and on the matrix realization, not merely on a single generator.

There is a second, representation-theoretic way to say the same thing. The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is simple and Artinian, so every $\mathbb{B}$-module is a direct sum of copies of its unique simple module $\mathbb{C}^2$ and has complex dimension $2k$. A one-dimensional $\mathbb{B}$-module would therefore be a trivial module, and $\mathbb{B}$ has none; a fortiori the left action of $\mathfrak{su}(2)\subset\mathbb{B}$ on $\Delta$ is nonzero on every sub-object, since every nonzero $\mathbb{B}$-submodule is a sum of copies of the simple module $S=\mathbb{C}^2$, on which $\mathfrak{su}(2)$ acts nontrivially. A right-handed $SU(2)_L$ singlet is not a structure the left-multiplication construction can express: there is no sub-object on which that action is trivial. This is a statement about the carrier, not about arithmetic: the electroweak assignment is perfectly writable, but it is not the one $\mathbb{B}$'s left action supplies.

**What a chiral non-abelian structure would require.** It would replace the $\mathbb{B}$-valued connection by an $\mathrm{End}(\Delta)$-valued one whose generators act only on the left half — schematically $G^a = T^a P_L$ on $\Delta$, with $T^a$ the $\mathfrak{su}(2)$ generators of the read list. The covariance computation is the abelian $Q$-case of the chiral-fermion article with $Q$ promoted to a matrix of generators, and it is identifiable: one verifies $D_\mu'(\Lambda\Psi) = \Lambda D_\mu\Psi$ for $\Lambda = \exp(\tfrac{i}{\hbar}\Gamma^a G_a)$ with an $\mathfrak{su}(2)$-valued gauge function. The cost is explicit: such a connection is **not** $\mathbb{B}$-valued and does not act by left multiplication, so it is not the framework's own non-abelian construction; it is that construction's chiral analogue, valued in a larger algebra. Whether the framework may adjoin it, or must derive it, is the open question.

**The remaining pieces of the obstacle, named.** The matter representation is unbuilt (the read-list parent's open question 3): what representation the matter field carries under the non-abelian group is not specified. The reality class of the connection is unsettled: the mixed assignment $\mathcal{A}_0$ anti-Hermitian, $\mathcal{A}_k$ Hermitian is the consistent one, but whether it is intended is open, and it bears on how the physical vector fields are identified with connection components. And a chiral gauge theory must satisfy anomaly-cancellation conditions on its spectrum; no biquaternion formulation of the anomaly is attempted anywhere in the series, so the consistency of any constructed chiral spectrum is unexamined.

**What would settle it.** The object is a **chiral non-abelian matter representation**: a declared carrier with an $\mathfrak{su}(2)$-module structure in which the left half transforms in the doublet and the right half in the singlet, a connection valued in that structure's endomorphisms, and a verification of gauge covariance and of the resulting mass selection rule. The computation is not mysterious — it is the standard one — but naming the carrier is a decision the framework has not made, and the pseudoreality argument shows it cannot be the framework's own left action. A second settling object is a **biquaternion axial-anomaly computation**; a third is a **decision on the real-structure identification** ("two-$i$"), since it fixes whether the framework's abelian factor is vector-like or axial. Classification: **known route, outside the framework's own construction** — the object is identifiable, but it is not reached by the $\mathbb{B}$-valued connection, and the route's endpoint is a modelling choice rather than a derivation.

## Weak Hypercharge: Nothing Derives It

Electroweak theory needs a second gauge factor. With $SU(2)_L$ it forms $SU(2)_L\times U(1)_Y$, and its charge, weak hypercharge $Y$, is what distinguishes the right-handed partners and what the scalar doublet carries into the masses. The framework's position on $Y$ is simple and should be stated without softening: **nothing in this series derives weak hypercharge, its values, or even its character.** The word does not appear anywhere in the read list, and no article in the series assigns a hypercharge. This is an open item, not an assumption.

Three separate facts make the gap precise.

**First, the framework's own abelian factor is vector-like.** The abelian gauge group the algebra supplies canonically is the unitary part of the center $\mathbb{C}_{\mathbb{B}}$, and a central element acts as a *scalar* on $M_2(\mathbb{C})$, giving every component the same charge. Weak hypercharge is chiral: it acts differently on the two chiralities, since $Y(\psi_L)\neq Y(\psi_R)$ for the electron, for example. So $U(1)_Y$ is not the framework's $U(1)$; it is a different kind of abelian factor, one whose action is non-central. The mismatch is not a missing number, it is a missing *character*.

**Second, the chiral abelian structure that does exist leaves its charges free.** The chiral-fermion article constructs $Q = q_L P_L + q_R P_R$ on the module and shows the mass selection rule $q_L = q_R$. That is exactly the right room for a chiral abelian factor — two independent charges — but $q_L$ and $q_R$ are parameters, exactly as $q$ is in the gauge principle, and nothing fixes them. The structure shows *how* a chiral $U(1)$ would act; it does not say *which* $U(1)$ acts. Weak hypercharge would be a particular assignment of these charges to the fermion multiplets, and no such assignment is derived.

**Third, even the character of the framework's abelian factor is undecided.** As the chiral-fermion article's qualification records, under the Lorentz-conjugate reading a central phase acts axially rather than vector-like. So the framework does not yet say whether its own $U(1)$ is vector-like or axial; a fortiori it does not say whether it can play the role of hypercharge.

A fourth, related gap is the **relative normalization of the two couplings**. In the standard theory the Weinberg angle is fixed by the embedding of $U(1)_Y$ in $SU(2)_L\times U(1)_Y$ and the measured couplings, and electric charge is $Q_{\mathrm{em}} = T_3 + Y$. The framework supplies two couplings $\kappa$ (non-abelian) and $q$ (abelian) as free parameters, and no embedding; so neither the mixing angle nor the electric-charge relation is derived.

**What would settle it.** The standard route to hypercharge values is not an assumption but a computation: the requirement that the chiral spectrum be anomaly-free, together with the observed electric-charge spectrum, fixes the hypercharge assignments up to normalization. The settling object is therefore a **biquaternion anomaly computation on the framework's spectrum**, which would either reproduce the standard conditions — in which case $Y$ becomes a framework output for the spectrum the framework supplies — or fail to reproduce them. A second settling object is a **no-go**: a demonstration that the framework's abelian factor cannot carry independent left and right charges, forcing $Y$ to be adjoined as an independent factor. A third is a **positive construction**: a derivation of a chiral abelian generator from the algebra's own structure, rather than from the module's projectors. Classification: the values are **no route yet**; the anomaly route is **known in standard field theory, unrealised in the framework**.

## The Scalar Sector and Symmetry Breaking

The scalar sector is where electroweak theory gets its masses, and it is the obstacle that depends most visibly on the two before it.

The need is established on the framework's own terms. The chiral-fermion article's mass selection rule says that a bare Dirac mass is gauge invariant if and only if $q_L = q_R$: a genuinely chiral fermion has no gauge-invariant mass. Its mass must wait for a field whose charge cancels the phase, i.e. one carrying $q_L - q_R$, which is what the Standard Model's Higgs field supplies. So the framework itself identifies the quantum numbers a compensating scalar must carry; what it does not supply is the scalar.

What the framework has is a scalar *field type* but not a scalar *sector*. The gauge-principle article treats a complex scalar biquaternion field $\tilde{\Phi} = \phi\,e_0$ obeying a massive Klein–Gordon equation, and notes that its mass term is linear, so the central phase survives the mass. That is a scalar carrying the central $U(1)$ — and it is exactly the vector-like abelian factor that hypercharge is not. In the read list there is no scalar *doublet*, no gauge-invariant potential with a non-trivial minimum, no vacuum expectation value, no kinetic term whose expansion gives the vector masses, and no Yukawa coupling. The Dirac article states the framework's relation to the mechanism plainly: it "does not derive the Higgs mechanism; it simply provides a compact notation for the mass term once the mechanism is assumed". The concurrent Higgs-mechanism article is not read here and nothing in this agenda depends on it; the mechanism is carried as an open item.

Three dependencies make this obstacle structural rather than technical.

- **It needs the chiral action.** A scalar that compensates a chiral fermion must carry the same non-abelian representation structure that the chiral-fermion obstacle leaves unbuilt. Without a chiral $SU(2)_L$, there is no doublet for the scalar to be.
- **It needs hypercharge.** The scalar's quantum numbers are exactly the assignments that nothing derives. The Standard Model's scalar is an $SU(2)_L$ doublet of hypercharge $\tfrac12$; both the doublet and the $\tfrac12$ are missing objects here.
- **It is contingent on the mass reading.** If the framework deploys a Majorana-type coupling on the real structure $\flat$, the field that carries it must be neutral (or in a real representation) and the Higgs story is replaced by a different one. The scalar program is therefore conditional on the unresolved Majorana-versus-Dirac question.

**What would settle it.** The object is a **gauge-charged scalar on the framework's carrier** with a declared $SU(2)_L\times U(1)_Y$ representation, a gauge-invariant potential with a non-trivial minimum, a covariant kinetic term whose expansion about that minimum produces the vector-boson masses, and a Yukawa coupling whose charge reproduces the selection rule. The computation is standard; what is not standard is the carrier and the quantum numbers, which are precisely the outputs of the two preceding obstacles. Classification: **known route, blocked** — on the chiral matter representation and on hypercharge, with a contingent branch if the mass reading is Majorana-type.

## Gauge Fixing and the Physical Content of an Orbit

The fourth obstacle is not an object the electroweak sector needs but a condition on what may be said about it. The framework **cannot fix the gauge**: the canonical-quantization article records it, the gauge-principle article lists a gauge-fixing principle among the things the algebra does not supply, and the non-abelian article adds the Gribov-type question of whether a gauge orbit intersects a gauge-fixing surface more than once. Nothing in the read list addresses it.

Why this bounds the electroweak sector specifically. In a gauge theory the physical content is the **orbit**, not the connection: a statement about a component $\mathcal{A}_\mu$ is not a statement about the world unless it is gauge invariant or a gauge has been fixed. The vector-boson masses are the sharp case. The standard account exhibits them in unitary gauge, where the Goldstone modes are removed and the massive $W$ and $Z$ appear directly; if no gauge can be fixed, that account is unavailable, and one must instead identify the physical masses as poles of gauge-invariant correlators. The framework has neither a gauge-fixing function nor an invariant spectral analysis, so it can neither exhibit the massive vector spectrum by choice of gauge nor certify it invariantly.

Two inherited facts sharpen the bound. The first is the **mixed reality class** of the non-abelian connection: because $\partial_0 = -i\partial_t$ flips the conjugation behaviour of the Maurer–Cartan form, the time component and the space components of $\mathcal{A}_\mu$ lie in opposite Hermitian-conjugation eigenspaces, and while the mixed assignment is internally consistent, whether it is the intended physical one is unsettled. Until it is settled, even the identification of the physical vector fields with components of the connection is provisional. The second is that the **gauge function and the connection are material-sector objects** only for real $\Gamma$; the electroweak rotation that mixes the two factors is not of this abelian form, so the abelian gauge-fixing analysis does not extend to it.

**What would settle it.** The object is a **gauge-fixing principle internal to the algebra** — an algebraic condition selecting a preferred representative of each orbit, generalizing the abelian Lorenz condition $S = 0$ that the parent already has, together with a demonstration that it selects a section (the Gribov question) — or, alternatively, a proof that the framework's physical content is determined entirely by gauge-invariant objects, with the massive spectrum read off from invariants such as the curvature and $\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$ and their correlators. Either would convert "the framework cannot fix the gauge" from a bound on what can be said into a statement about how physics is to be expressed. Classification: **no route yet** for a fixing principle; the invariant formulation is a conceivable route but is not constructed.

## The Ledger

The table collects the items of the agenda and sorts each into the three-way classification. "Established" means recomputed in the series and inherited here; "known route" means the object does not exist but the computation that would produce it is identifiable; "no route yet" means no mechanism has been proposed.

| Item | Status | Object or computation that would settle it |
|---|---|---|
| Abelian gauge principle: central $U(1)$, connection $\tilde{A}'=\tilde{A}-\tilde{\nabla}\Gamma$, covariant derivative, abelian curvature | Established | — |
| Non-abelian construction on $\mathfrak{su}(2)$: connection, adjoint curvature with $[\mathcal{A},\mathcal{A}]$, Bianchi identity, gauge-invariant density | Established | — |
| Available compact algebra $\mathbb{M}_-=\mathbb{R}(ie_0)\oplus\mathfrak{su}(2)$, i.e. $\mathfrak{u}(2)$, real dimension $4$ | Established | — |
| Mixed reality class of the connection ($\mathcal{A}_0$ anti-Hermitian, $\mathcal{A}_k$ Hermitian; no single eigenspace) | Established gap (read list) | A declaration of the intended assignment, or a reformulation removing the mismatch |
| Chiral structure on $\Delta$: $\gamma_5$, $P_{L,R}$, selection rule $q_L=q_R$, vector-like center | Established | — |
| $\mathfrak{su}(2)$ as the algebra of weak isospin | Established as an **algebra** only | — |
| Chiral non-abelian gauge action ($SU(2)_L$ doublets and singlets) | Known route, **outside the $\mathbb{B}$-valued construction** | A declared carrier with $\mathfrak{su}(2)$-module structure (left doublet, right singlet), an $\mathrm{End}(\Delta)$-valued connection, and verified gauge covariance; pseudoreality shows it cannot be the left action of $\mathbb{B}$ |
| Non-abelian matter representation (read-list open question 3) | Open, known route | Construct the $\mathfrak{su}(2)$ charge operator on the spinor module and verify covariance |
| Weak hypercharge: values $Y$ | **No route yet** | A derivation fixing $Y$, e.g. anomaly cancellation on the framework's spectrum; or a no-go forcing $Y$ to be adjoined |
| Character of the abelian factor (vector-like or axial) | Open, inherited | Decide the real-structure ("two-$i$") identification of the field with $\Delta$ |
| Weinberg angle, electric-charge relation $Q_{\mathrm{em}}=T_3+Y$ | **No route yet** | Fix both couplings and the embedding of $\mathfrak{u}(1)$ in $\mathfrak{u}(2)$; requires hypercharge |
| Scalar sector: doublet, potential, vacuum expectation value, kinetic term | Known route, blocked | A gauge-charged scalar with a declared representation, a non-trivial invariant minimum, and a covariant kinetic term for the vector masses |
| Yukawa coupling and fermion masses | Known route, blocked | A coupling whose charge reproduces $q_L-q_R$; contingent on the mass reading |
| Mass reading: Majorana-type or real-form Dirac | Open, inherited | Decide on the real module |
| Gauge fixing | **No route yet** | A biquaternionic gauge-fixing functional selecting a section, or a proof that physical content is orbit-invariant |
| Gribov copies of any fixing | No route yet | Follows the fixing principle; not addressed anywhere |
| Anomaly cancellation | Known route in standard field theory; no framework realisation | A biquaternion axial-current or triangle-anomaly computation |
| $W^\pm$, $Z$ spectrum and masses | Blocked | The scalar kinetic term in a fixed gauge, or an invariant pole analysis |
| Empirical contact | Open | A prediction distinguishing the framework from standard electroweak theory |

## What Would Settle It

The obstacles are not independent, and the dependency chain is short. The scalar sector needs the chiral action and the hypercharge assignments; the chiral non-abelian action needs a declared carrier and a connection that is not the framework's own $\mathbb{B}$-valued one; hypercharge needs either a derivation or a no-go; and every physical statement about masses needs a gauge fixing. Two items are therefore upstream of everything else.

1. **A chiral matter representation, and a decision about its carrier.** Either the framework supplies an object on which $SU(2)_L$ acts with inequivalent left and right representations — which, by the pseudoreality argument, cannot be the left action of $\mathbb{B}$ and must be an $\mathrm{End}(\Delta)$-valued or otherwise enlarged structure — or it is shown that the chiral sector must be adjoined as an independent representation. Either outcome converts the framework's relation to electroweak theory from "unknown" to "stated". The one thing that does not convert it is writing $SU(2)_L$ doublets and singlets down and proceeding; that is the fabricated premise the agenda exists to prevent.
2. **A weak hypercharge assignment, derived or refused.** Either hypercharge comes out of an internal principle — the anomaly-cancellation route is the standard candidate, and no framework realisation exists — or it is shown that the framework's abelian factor cannot carry independent left and right charges and that $Y$ must be adjoined. As with chirality, the honest alternatives are a derivation and a no-go; an assumption is neither.

A third item is a condition on all physical statements rather than an object of the theory: **a gauge-fixing principle, or an invariant formulation**. Without one, the framework can compute curvature components but cannot say what the massive spectrum is, because it cannot connect an orbit to an observation. This is upstream of the $W$ and $Z$ masses in the same way the colour group and the quark content are upstream of QCD's running coupling in the companion agenda: the computation is standard, and its inputs are the missing objects.

With those settled, the rest of the agenda becomes ordinary work: build the scalar doublet, expand its kinetic term, read off the vector masses, write the Yukawa coupling, and compute the anomaly. Without them, the honest summary of the framework's relation to electroweak theory is the one this article opened with: it has a canonical abelian gauge principle, it has a non-abelian construction on an algebra of exactly the right dimension, it has an exact chiral structure on a two-dimensional module, and it does not have an electroweak sector.

Finally, the genre's standing caution applies here in its strongest form. *The Empirical Status of the Biquaternion Framework* records that on every domain developed, the framework is so far empirically equivalent to the standard theory it reformulates. A biquaternionic electroweak sector, if one is ever constructed, would inherit that position unless it makes a prediction standard electroweak theory does not; and a sector whose gauge group, hypercharge assignments, scalar potential, and gauge fixing are all imported has no prospect of doing so. The agenda's most useful output may be to make that consequence visible early, rather than to produce a construction that appears to answer electroweak theory while assuming all of it.

## Summary

This article is a research agenda for electroweak theory inside the biquaternion framework. Its finding is that the framework reaches the general machinery of a non-abelian gauge theory on a compact algebra of the right dimension, together with an exact chiral structure on the spinor module, and stops before any chiral gauge theory, any hypercharge assignment, or any scalar sector.

What is established is recalled: the abelian gauge principle, with a canonical central $U(1)$, the connection $\tilde{A}'=\tilde{A}-\tilde{\nabla}\Gamma$, the covariant derivative, the abelian curvature, and the linear chiral mass with its conserved vector $U(1)$ and broken axial symmetry; the non-abelian construction,

with a connection transforming inhomogeneously, a curvature transforming in the adjoint and containing the commutator term and satisfying the Bianchi identity, and a gauge-invariant density, built on the $\mathfrak{su}(2)$ factor of the material sector; the Lie-algebra decomposition $\mathbb{M}_-=\mathbb{R}(ie_0)\oplus\mathfrak{su}(2)$, so that the compact algebra available is $\mathfrak{u}(2)$, of real dimension four; the chiral structure on the Dirac module, with exact projectors, a chirality-odd mass bilinear, and the selection rule $q_L=q_R$; and the vector-like character of the center.

What is not established is everything electroweak-specific.

- **A chiral gauge theory.** The framework's non-abelian connection is $\mathbb{B}$-valued and acts by left multiplication, which is vector-like on $\Delta$ because the $SU(2)$ doublet is pseudoreal and $\mathbb{B}$ has no one-dimensional module. The chiral abelian structure that does exist is valued in $\mathrm{End}(\Delta)$, not $\mathbb{B}$. **Known route, outside the framework's own construction**, with the carrier named as the thing to be decided.
- **Weak hypercharge.** Nothing derives its values or its chiral character; the framework's canonical abelian factor is the scalar center, which is vector-like. The word does not occur in the read list. **No route yet** for the values; the anomaly-cancellation route is standard but unrealised.
- **The scalar sector and symmetry breaking.** The framework has a scalar field type with a linear mass but no doublet; in the read list there is no potential, no vacuum expectation value, and no Yukawa coupling, and the framework states that it does not derive the mechanism. **Known route, blocked** on the chiral action and on hypercharge, and contingent on the mass reading.
- **Gauge fixing.** The framework cannot fix the gauge, and the non-abelian case adds the Gribov question; without a fixing or an invariant formulation, the physical content of an orbit — including the vector masses — cannot be exhibited. **No route yet.**

The two upstream items are a chiral matter representation with a declared carrier and a weak hypercharge assignment that is either derived or refused. Everything else depends on them. The article commits throughout to the agenda's central discipline: no section assumes $SU(2)_L$ doublets, hypercharge, or a scalar doublet, and where standard electroweak numbers appear, they are marked as imports.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H} \cong M_2(\mathbb{C})$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_1e_2=e_3$ |
| $i$ | Scalar imaginary, $i^2=-1$, central |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors; $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ | Center of the algebra; the vector-like abelian factor |
| $\tilde{\nabla} = e_0\partial_{ict}+e_k\partial_k$, $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}$ | Biquaternionic gradient and d'Alembertian |
| $\tilde{A}' = \tilde{A}-\tilde{\nabla}\Gamma$, $D=\tilde{\nabla}+\tfrac{iq}{\hbar}\tilde{A}$ | Abelian connection law and covariant derivative (read list) |
| $[e_a,e_b]=2\varepsilon_{abc}e_c$, $T_a=\tfrac12 e_a$ | Commutator and normalized generators of $\mathfrak{su}(2)\subset\mathbb{M}_-$ |
| $\mathbb{M}_- = \mathbb{R}(ie_0)\oplus\mathfrak{su}(2)$, $\mathfrak{u}(2)=\mathfrak{u}(1)\oplus\mathfrak{su}(2)$ | Available compact algebra (real dimension $4$) |
| $U \in SU(2)$ (unit real quaternions), $\mathcal{A}_\mu\in\mathfrak{su}(2)$, $\kappa=q/\hbar$ | Gauge group, non-abelian connection, coupling (read list) |
| $\mathcal{A}'_\mu=U\mathcal{A}_\mu U^{-1}+\tfrac{i}{\kappa}(\partial_\mu U)U^{-1}$ | Non-abelian connection law |
| $F_{\mu\nu}=\partial_\mu\mathcal{A}_\nu-\partial_\nu\mathcal{A}_\mu+i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$, $F'_{\mu\nu}=UF_{\mu\nu}U^{-1}$ | Non-abelian curvature; adjoint law |
| $\Phi(e_0)=I_2$, $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$ | Matrix realization |
| $S=\mathbb{C}^2=(\tfrac12,0)$, $\bar{S}=(0,\tfrac12)$, $\Delta=S\oplus\bar{S}$ | Weyl modules and Dirac module |
| $\gamma_5$, $P_L=\tfrac12(I_4-\gamma_5)$, $P_R=\tfrac12(I_4+\gamma_5)$ | Chirality operator and projectors |
| $\bar\Psi\Psi$, $Q=q_LP_L+q_RP_R$, selection rule $q_L=q_R$ | Chirality-odd mass bilinear; chiral charge operator |
| $\varepsilon=\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)$, $\varepsilon g^{*}\varepsilon^{-1}=g$ | Pseudoreality intertwiner: $2\cong\bar{2}$ for $SU(2)$ |
| $\mathrm{End}(\Delta)$ | Module endomorphisms; the home a chiral gauge connection would need |
| $\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L,\ \bar{\tilde{\nabla}}\tilde{\Psi}_L=m\tilde{\Psi}_R$; $\tilde{\Psi}^{\flat}=-\tilde{\Psi}^{\dagger}$ | Linear chiral mass pair; algebra real structure $\flat$ (Majorana/Dirac reading of its pairing open) |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Inherited informational trace formula |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| **Standard electroweak notation, not framework objects** | |
| $SU(2)_L$, $U(1)_Y$ | Electroweak gauge group — not derived |
| $Y$, $T_3$, $Q_{\mathrm{em}}=T_3+Y$ | Weak hypercharge, weak isospin, electric charge — no derivation of $Y$ |
| $\theta_W$, $g$, $g'$ | Weinberg angle and couplings — not fixed |
| $H$, $v$, Yukawa couplings | Scalar doublet, vacuum expectation value, fermion masses — not constructed |
| $W^\pm$, $Z$, photon | Massive and massless vector bosons — not identified |

## Further Reading

- *Non-Abelian Gauge Fields in Biquaternionic Form* — the immediate parent; the connection, the adjoint curvature, the Bianchi identity, the gauge-invariant density, the Lie-algebra decomposition $\mathbb{M}_-=\mathbb{R}(ie_0)\oplus\mathfrak{su}(2)$, and the open matter-representation question this agenda inherits.
- *The Gauge Principle in Biquaternionic Form* — the abelian origin of the connection, the central $U(1)$, the linear mass and the real structure, and the gauge-fixing gap.

- *Chiral Fermions in the Biquaternion Framework* — the module's chirality structure, the vector-like center, the mass selection rule, the module-valued chiral charge operator, and the real-structure qualification that bears on hypercharge.
- *The Covariant Derivative and Gauge Connection in Biquaternionic Form* — the abelian connection whose non-abelian extension is the parent's starting point.
- *Maxwell's Equations in the Biquaternionic Formulation* — the abelian potential, field strength, and gauge scalar that the electroweak factors would generalize.
- *The Dirac Equation in Biquaternionic Form* — the mass term, the chirality of the mass bilinear, and the corpus's explicit statement that the framework does not derive the electroweak structure.

- *The Neutrino and Majorana Fermions in Biquaternionic Form* — the real-structure question and the unrepresented dimension-five operator; the article in which the mass reading is pursued.
- *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism* and *The Spinor Module in Biquaternionic Form and Its Lorentz Action* — the left/right matter-representation issue and the module structure on which the chiral analysis rests.
- *The Electron in Biquaternionic Form* — the physical reading of chirality and its separation from the sector split.
- *Biquaternion Representation Theory* and *Lie Algebras: A General Introduction* — the module structure of $M_2(\mathbb{C})$, the pseudoreality of $\mathfrak{su}(2)$, and the compact-subalgebra facts behind the available gauge algebra.
- *The Lorentz Group in Biquaternionic Form — Structure and Representations* — the representation theory on which the doublet and singlet bookkeeping would rest.
- *Canonical Quantization of the Biquaternion Maxwell Field* — the framework's inability to fix the gauge, on which the physical-content obstacle turns. (*Canonical Quantization of the Biquaternion Dirac Field*, which does not treat the gauge, records the separate second-class constraint $\pi - i\psi^{\dagger}\approx 0$.)
- *The Field-Strength Biquaternion and Its Invariants* — the abelian invariants and the norm form, whose non-abelian extension is open.
- *The CPT Theorem in Biquaternionic Form* — the discrete operations and the corpus's statement that their electroweak relevance is imported.
- *The Empirical Status of the Biquaternion Framework* — the standing empirical-equivalence result, the caution under which any biquaternionic electroweak sector would labour.
- *Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda* — the sibling agenda whose three-way classification and settling-object discipline this article follows.
- *The Einstein Field Equations under the Biquaternion Framework — A Research Agenda* — the companion agenda whose format and ledger this article follows.
