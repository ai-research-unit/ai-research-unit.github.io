# __Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form__

## Introduction

A mass term is the only term of a field equation that carries no derivative, and that single fact fixes its algebraic shape. Every other term pairs the field with a gradient; a term with no derivative has nothing to differentiate, so it must pair the field with *another field* — and since a free equation is written in terms of one field, that other field must be a **conjugate** of it. The only freedom left is *which* conjugate. That choice is not cosmetic. It is what separates the two kinds of mass, and it is why the words "mass" and "conjugation" belong in the same sentence.

The framework carries several conjugations, and they are easy to conflate because two of them are antilinear and both are called a real structure: the algebra's $\flat$ and the **charge conjugation** $\mathcal{C}$ that lives on the spinor module. This article separates them and settles what each is for. Its claims:

- **Established, and recomputed below.** The biquaternion algebra carries three antilinear involutions — complex conjugation $^{*}$, Hermitian conjugation $^{\dagger}=\bar{\cdot}^{\,*}$, and the anti-Hermitian conjugation $\flat=-\dagger$ — alongside the *linear* quaternion conjugation $\bar{\cdot}$. Their fixed spaces are four distinct subspaces, of real dimensions $2, 4, 4$ and $4$, and only the last two of them are the framework's sectors. In particular the one involution that is **linear**, quaternion conjugation, is the one whose fixed space is *not* a sector.
- **Established, and recomputed below.** The **Dirac mass** is linear and couples the two chiralities, $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$; it pairs no field with its own conjugate. The **Majorana mass** is antilinear and pairs a field with its own conjugate, and it is physical: its reality condition has a four-real-dimensional solution space and it preserves the mass shell $p^2 = m^2$.
- **Established, and recomputed below.** The retired single-field equation $\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^\flat$ fails, and it fails **on the dispersion**: its central-phase plane waves have nullity $0$ on the timelike shell and nullity $4$ on the spacelike shell, so its solutions lie on the spacelike locus. This is reproduced here from the block representation by pure real arithmetic.
- **The distinction the whole article turns on.** The diagnosis of that failure is the *pairing*, not the antilinearity. A Majorana mass is also antilinear and is perfectly physical. What the retired equation did was use the **algebra's** real structure $\flat$ as though it were the mass of a field on the **module** — and the two are different real structures on different spaces.

- **Gap, left visible.** The framework does not derive the values of either mass, and it does not decide which kind a given fermion carries; that is empirical input, as the neutrino companion states. What the framework supplies is the algebraic distinction and the reality structure each kind is built on.

The article is organised as follows. A section fixes what antilinear means in this algebra and tabulates the involutions. A section gives the argument that a mass is a pairing with a conjugate. A section distinguishes the two conjugates and the two masses. A section separates the two real structures, on the algebra and on the module, which is where the retired equation went wrong. A section places charge conjugation in its group-theoretic setting, the $\mathrm{Spin}^c$ structure, and reads off which spinors can carry the algebra's central $U(1)$. A section exhibits the dispersion failure in full. A section records what the antilinear structure is genuinely for.

## What Antilinear Means Here

The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, and scalar imaginary $i$ generating the center together with $e_0$. An element is a sum with complex coefficients,

$$
\tilde{Q} = (a_0 + i b_0)e_0 + (a_1 + i b_1)e_1 + (a_2 + i b_2)e_2 + (a_3 + i b_3)e_3 , \qquad a_\mu, b_\mu \in \mathbb{R},
$$

so $\mathbb{B}$ has real dimension $8$ and complex dimension $4$.

Two involutions generate the rest.

**Quaternion conjugation** reverses the vector part and fixes the center:

$$
\bar{\tilde{Q}} = (a_0 + ib_0)e_0 - (a_1 + ib_1)e_1 - (a_2 + ib_2)e_2 - (a_3 + ib_3)e_3 .
$$

It is $\mathbb{C}$-**linear**, because it fixes $i$, and it is an anti-automorphism, $\overline{\tilde{A}\tilde{B}} = \bar{\tilde{B}}\,\bar{\tilde{A}}$.

**Complex conjugation** negates the scalar imaginary and fixes the units:

$$
\tilde{Q}^{*} = (a_0 - ib_0)e_0 + (a_1 - ib_1)e_1 + (a_2 - ib_2)e_2 + (a_3 - ib_3)e_3 .
$$

It is $\mathbb{C}$-**antilinear**, $(\alpha\tilde{A})^{*} = \alpha^{*}\tilde{A}^{*}$, and it is an automorphism, $(\tilde{A}\tilde{B})^{*} = \tilde{A}^{*}\tilde{B}^{*}$.

Composing them gives the two Hermitian conjugations of the series. Because one factor is linear and the other antilinear, each composite is antilinear:

$$
\tilde{Q}^\dagger = \bar{\tilde{Q}}^{\,*} = \big(\tilde{Q}^{*}\big)\bar{\ } , \qquad
\tilde{Q}^\flat = -\tilde{Q}^\dagger .
$$

Both are anti-automorphisms; the second carries a sign, $(\tilde{A}\tilde{B})^\flat = -\tilde{B}^\flat\tilde{A}^\flat$, and that sign is its only departure from an ordinary anti-automorphism. The two differ by the central sign alone, and that sign is what moves the fixed space from one sector to the other.

| involution | action on generators | $\mathbb{C}$-linearity | character | fixed space |
|---|---|---|---|---|
| $\bar{\tilde{Q}}$ | $e_k \mapsto -e_k$, $i \mapsto i$ | linear | anti-automorphism | $\mathbb{C}_{\mathbb{B}} = \{Q_0e_0\}$ (center), real dim $2$ |
| $\tilde{Q}^{*}$ | $e_k \mapsto e_k$, $i \mapsto -i$ | antilinear | automorphism | $\mathbb{H}_{\mathbb{B}}$, real dim $4$ |
| $\tilde{Q}^{\dagger} = \bar{\tilde{Q}}^{\,*}$ | $e_k \mapsto -e_k$, $i \mapsto -i$ | antilinear | anti-automorphism | $\mathbb{M}_+$, real dim $4$ |
| $\tilde{Q}^{\flat} = -\tilde{Q}^{\dagger}$ | $e_k \mapsto -e_k$, $i \mapsto -i$, with a sign | antilinear | anti-automorphism with twist | $\mathbb{M}_-$, real dim $4$ |

Four involutions, four distinct fixed spaces, of real dimensions $2, 4, 4, 4$. The two sectors of the framework are the last two rows, and they are the fixed spaces of *antilinear* maps. The real-quaternion sector $\mathbb{H}_{\mathbb{B}}$ is also antilinear, and the center is the fixed space of the one linear involution. Nothing in the table is a sign variant of anything else: each row has its own fixed space, and the fixed spaces are what the framework builds on.

On the two sectors $\flat$ acts by a sign, and this is the fact the rest of the article uses:

$$
\tilde{\Psi}^\flat = +\tilde{\Psi}\ \ (\tilde{\Psi}\in\mathbb{M}_-), \qquad
\tilde{\Psi}^\flat = -\tilde{\Psi}\ \ (\tilde{\Psi}\in\mathbb{M}_+).
$$

The sign is the central $i$: $\mathbb{M}_+$ is the Hermitian sector and $\mathbb{M}_-$ the anti-Hermitian one, and $\mathbb{M}_- = i\,\mathbb{M}_+$. Since $i$ is central, an antilinear map can move one sector to the other, and $\flat$ does exactly that with a sign.

## Why a Mass Is a Pairing with a Conjugate

The argument is short and it is the reason the two topics of this article are one topic.

Write the free equation of a field as

$$
\mathcal{D}\tilde{\Psi} = \text{(mass term)},
$$

where $\mathcal{D}$ is first order and carries the gradient. The mass term is defined as the part of the equation that survives when every derivative is dropped. Being non-derivative, it cannot pair the field with $\partial_\mu\tilde{\Psi}$; being bilinear and built from a single field, it must pair $\tilde{\Psi}$ with something constructed from $\tilde{\Psi}$ itself. The only constructions available that do not reintroduce a derivative are the involutions of the previous section.

So a mass term has the shape

$$
\text{mass} \;\sim\; \tilde{\Psi}^{\,\bullet}\,\tilde{\Psi} \quad\text{or}\quad \tilde{\Psi}\,\tilde{\Psi}^{\,\bullet},
$$

with $\bullet$ one of $\bar{\cdot}$, $*$, $\dagger$, $\flat$. The involutions are not interchangeable — they have different fixed spaces — so **each choice of involution is a different kind of mass**. That is the whole content of the phrase "the two kinds of mass": the kinds are indexed by the conjugation, not by a numerical value.

Two of those choices are realised in physics, and they are the two extremes of the table.

**The identity-like choice gives the Dirac mass.** The pairing that uses the *chiral partner* rather than a conjugation asks for no involution at all: it pairs $\tilde{\Psi}_L$ with $\tilde{\Psi}_R$, two independent halves of one field. It is linear, and it is the mass term of the Dirac equation.

**The conjugation choice gives the Majorana mass.** The pairing that uses the field's own conjugate, $\tilde{\Psi}$ with $\tilde{\Psi}^{\,\bullet}$, requires the field to *equal* its conjugate — a **reality condition** that halves the field's independent components. It is antilinear, and it is the mass term of a Majorana fermion.

The distinction is visible in the component count before any dynamics is imposed, and the count is decisive. The spinor module has real dimension $8$: four complex components. An antilinear involution on it has a fixed space of real dimension $4$ — half. So

$$
\text{Dirac field}: 8 \text{ real components}, \qquad
\text{Majorana field}: 4 \text{ real components},
$$

and the Majorana field is not a Dirac field with a constraint bolted on; it is a different carrier, of half the size, singled out by an antilinear pairing.

The framework's Dirac module is $\Delta = S\oplus\bar{S}$, the two chiral halves, of complex dimension $4$ and real dimension $8$. Its charge conjugation is the conjugate-linear map $\mathcal{C}$ satisfying $\mathcal{C}^2 = 1$ that exchanges the two halves; its fixed space is the Majorana spinor space, of real dimension four. The companion on the neutrino and Majorana fermions constructs that map and computes its consequences; the present article is concerned with the algebra-side counterpart, and with keeping the two apart.

## The Two Conjugates and the Two Masses

The two mass terms of a single fermion species, written on the spinor module with $\psi = (\psi_L,\psi_R)$ and $\psi^c$ the charge conjugate of $\psi$, are

$$
\mathcal{L}_{\text{Dirac}} = -m_D\,\bar{\psi}\psi = -m_D\big(\psi_L^{\dagger}\psi_R + \psi_R^{\dagger}\psi_L\big),
$$

$$
\mathcal{L}_{\text{Majorana}} = -\tfrac12 m_M\big(\psi_L^{T}\mathcal{C}\psi_L + \text{h.c.}\big).
$$

The first pairs $\psi_L$ with $\psi_R$ and is **linear**; it conserves fermion number and is invariant under the continuous phase $\psi\mapsto e^{i\alpha}\psi$. The second pairs $\psi_L$ with $\psi_L^{c}$ and is **antilinear**; it changes fermion number by two units, and it is not invariant under the continuous phase — which is exactly why it can be written only for a field that is not protected by a conserved charge.

| | Dirac mass | Majorana mass |
|---|---|---|
| pairs | $\psi_L$ with $\psi_R$ | $\psi$ with $\psi^{c}$ |
| linearity | linear | antilinear |
| fermion number | conserved | violated by $2$ |
| continuous phase | invariant | not invariant |
| needs a reality condition | no | yes, $\psi^{c}=\psi$ |
| independent real components | $8$ | $4$ |
| framework structure | the chiral pair of minimal left ideals | an antilinear real structure |

Both are masses; neither is a mistake. The two rows of the table are what the phrase "two kinds of mass" names, and the reason they are both called a mass is that both are non-derivative bilinears — the argument of the previous section.

In biquaternionic form the Dirac mass is the linear chiral pair of the parent article,

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R ,
$$
<!-- CONVENTION — the massive equation, canonical form. This linear, chirality-off-diagonal pair IS the biquaternionic Dirac mass for m ≠ 0; the derived articles state it in this orientation (∇̃ acting on Ψ_R, ∇̄̃ on Ψ_L). Two standing facts. (i) The mass term is LINEAR: the continuous central phase (fermion number) passes through it, so the vector U(1) is exact for the massive field, and what the mass breaks is the AXIAL symmetry. (ii) It is NOT the antilinear single-field equation ∇̃Ψ = mΨ♭ of the next section: that equation belongs to the algebra's real structure ♭ and is a different equation. Do not replace this pair by the antilinear form; this article exists to state the distinction. -->

the massless case being $\tilde{\nabla}\tilde{\Psi} = 0$. Applying $\bar{\tilde{\nabla}}$ to the first and substituting the second, with $\bar{\tilde{\nabla}}\tilde{\nabla} = \Box$, gives the Klein–Gordon equation for each chirality,

$$
\Box\tilde{\Psi}_R = m^2\tilde{\Psi}_R ,
$$

so the pair sits on the physical mass shell. This is the form every article in the series uses, and it is the sense in which the mass is chirality-off-diagonal: it is a coupling *between* the two chiralities, not a conjugation of either.

### Why the Dirac Mass Cannot Be Antilinear

That the mass must be a pairing with a conjugate does not make it a *self*-pairing, and the difference is forced by the algebra.

Left multiplication by an element of $\mathbb{B}$ preserves each minimal left ideal, and those ideals are the chiralities. So no combination $a\tilde{\Psi}_L + b\tilde{\Psi}_R$ of left multiplications can carry one chirality into the other. A mass that couples the chiralities therefore has to act as a **right** multiplication, and a right multiplication by the field itself — a pairing of $\tilde{\Psi}$ with $\tilde{\Psi}^{\,\bullet}$ — is a pairing of the field with its own conjugate. The distinction between the two mass terms is thus an algebraic dichotomy on the sides of the module, not a preference:

- coupling the **two chiralities** requires a right multiplication by the *other* chirality — linear, off-diagonal, the Dirac mass;
- pairing the field with **its own conjugate** requires an involution of the field — antilinear, the Majorana mass.

A single equation with a single field and a single mass term can realise the second. It cannot realise the first, because the first needs two independent chiralities and hence two fields, which is what the pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$ provides.

## Two Real Structures, on Two Different Spaces

This is the section on which the retired equation's diagnosis turns, and it separates two objects that the word "conjugation" hides.

The framework calls $\flat$ the algebra's **real structure**. The neutrino companion constructs charge conjugation $\mathcal{C}$ on the spinor module and calls it a real structure too. Both are antilinear, both are involutions up to sign, and both pair an object with its own conjugate. They are nevertheless **different maps on different spaces**, and neither may stand in for the other:

| | algebra real structure $\flat$ | module charge conjugation $\mathcal{C}$ |
|---|---|---|
| acts on | the algebra $\mathbb{B}$, real dim $8$ | the spinor module $\Delta$, real dim $8$ |
| defined by | the generators: $e_k\mapsto -e_k$, $i\mapsto -i$, with a sign | the Clifford relation $\mathcal{C}^{-1}\gamma^\mu\mathcal{C} = -\gamma^{\mu T}$ |
| fixed space | $\mathbb{M}_-$, the anti-Hermitian sector, real dim $4$ | the Majorana spinor space, real dim $4$ |
| commutes with the kinetic operator | **no** | **yes**, up to a sign |
| exchanges the chiral halves | with $^{\dagger}$ the sector split is by $\flat$ | yes |
| role | the $\mathbb{M}_\pm$ split, traces, bilinears | the Majorana reality condition |

The third row and the fourth row are the substance. The fixed spaces have the *same real dimension four*, which is why the two are so easy to identify — and why the identification is wrong. The neutrino companion tests it on the equation and reports the obstruction: **the Dirac operator does not preserve $\mathbb{M}_-$.** Left multiplication by a spatial generator carries an element of $\mathbb{M}_-$ out of the subspace, because the gradient is a sum of odd Clifford elements while $\mathbb{M}_-$ is an even-algebra subspace. A reality condition that the kinetic operator does not respect cannot be imposed on a field: the constrained field would not stay constrained under time evolution. So $\mathbb{M}_-$ is a perfectly good real form *of the algebra* — Lorentz-stable under the rotor action $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ — and simultaneously not the Majorana reality condition *of the module*, despite the matching dimension count.

The moral is the one this article exists to record:

$$
\boxed{\ \text{the algebra's } \flat \text{ and the module's } \mathcal{C} \text{ are different real structures; the dimension count does not identify them.}\ }
$$

The algebras and the modules of this framework have parallel vocabularies — conjugation, real structure, sectors, chirality — and the parallel is not an identity. A statement about $\flat$ is a statement about the algebra; a reality condition on a fermion is a statement about the module. Moving between them requires a construction, not a substitution.

## Charge Conjugation, the $\mathrm{Spin}^c$ Structure and the Neutral Spinors

The preceding section separates the algebra's $\flat$ from the module's $\mathcal{C}$ and keeps the two apart. Having separated them, it is worth asking what else acts on the module. Besides the Lorentz action there is an extra central circle, and the group that includes both is $\mathrm{Spin}^c$.

**The group.** The companion *Spinors: Categorization* defines the $\mathrm{Spin}^c$ group as

$$
\mathrm{Spin}^c(n) \;=\; \frac{\mathrm{Spin}(n)\times U(1)}{\{\pm 1\}},
\qquad
\mathfrak{spin}^c(1,3) \;=\; \mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}\oplus\mathfrak{u}(1),
$$

a double cover of $SO(1,3)\times U(1)$: the spin group extended by a central circle. It is **not** the complexification of $\mathrm{Spin}(1,3)$ — that is the larger $\mathrm{Spin}(1,3)_{\mathbb{C}}$, of real dimension twelve — and the looser name is sometimes used for it; the definition above is the one used here. $W_3$ is the integral class obstructing its existence, and the group is available exactly when $w_2$ is the mod $2$ reduction of an integral class. The Clifford action of $\mathrm{Cl}_{1,3}$ on the Dirac module is projective, realising a Lorentz transformation $\Lambda$ by $\pm S(\Lambda)$; that is why the acting group is the double cover $\mathrm{Spin}(1,3)$, and $\mathrm{Spin}^c$ is the central extension that adds the circle. The extra factor is **central** in $\mathrm{Spin}^c$, and it acts on the Dirac module by the same scalar on both chiral halves.

**The framework's central $U(1)$ is that factor.** The gauge principle article localizes the unitary part of the center — the complex scalar subspace $\mathbb{C}_{\mathbb{B}}$, of real dimension $2$ — whose unitary elements are the phases $\lambda = e^{i\theta}e_0$, and the minimal-coupling article writes the covariant derivative $D = \tilde{\nabla} + (iq/\hbar)\tilde{A}$ for exactly that phase. The phase is central in $\mathbb{B}$, and $\gamma_5$ — which anticommutes with every generator, and so commutes with every even element — is central in the complexified algebra $\mathbb{C}\otimes_\mathbb{R}\mathbb{B}$; the two therefore commute, and the phase acts with the same phase on the two chiral halves. The framework's $U(1)$ is **vector-like**, and this is structural rather than an artifact of the representation. It is the electromagnetic $U(1)$.

**Which spinors can carry it.** A spinor can be rotated by the central phase and remain a spinor of its own type only when its defining condition survives the rotation. The Dirac module imposes no condition, and $\psi\mapsto e^{i\alpha}\psi$ is a symmetry of the free equation, so the Dirac spinor — with linearly independent left and right components — carries the $U(1)$ and is charged. The Majorana spinor is the fixed-point set of the module's antilinear real structure, $\psi = \mathcal{C}\bar{\psi}^{T}$, and $\mathcal{C}$ is conjugate-linear, so

$$
\psi = \mathcal{C}\bar{\psi}^{T}
\quad\Longrightarrow\quad
e^{i\alpha}\psi = e^{-i\alpha}\,\mathcal{C}\bar{\psi}^{T}.
$$

The condition is preserved only for $e^{2i\alpha} = 1$, that is $\alpha = 0,\pi$: the continuous phase does not act, and the Majorana spinor is **blind to the central $U(1)$** — electrically neutral. The **ELKO** spinor, a Lounesto class-$5$ spinor, is neutral for the same reason: it too is fixed by an antilinear condition. The three cases therefore stand as: Dirac charged, Majorana and ELKO neutral.

It matters for the previous section *which* of the article's two real structures does the work. It is the **module's** $\mathcal{C}$ — the fixed-point condition that halves the field — and not the algebra's $\flat$. The distinction between them is thus not bookkeeping; it decides which spinors can carry a charge. The minimal-coupling article reaches the same obstruction from the other side, finding that a mass term pairing the field with its conjugate would retain only $\lambda = \pm 1$ of the phase.

**What the identification re-reads.** Three negative results that the series records separately fall under one heading, though their causes come in two parts. The anomaly article finds the central phase vector-like, so that its cubic trace cancels identically; the custodial-symmetry and $W$-and-$Z$ articles find the framework's non-abelian actions — the adjoint on the material sector, and left multiplication on the spinor module — vector-like, so that they cannot give the left- and right-handed fermions inequivalent representations. For the **central** phase, the cause is now group-theoretic: it is the central circle of $\mathrm{Spin}^c$, central in an algebra that contains $\gamma_5$, so it commutes with $\gamma_5$ and acts equally on the two chiralities. For the non-abelian actions the cause is parallel but distinct: they multiply the two chiral halves alike. The two together are why the chiral $U(1)$ of hypercharge is not a gauge structure of $\mathbb{B}$.

**Gap, left visible.** What the identification does **not** settle is whether $C$ and $P$ become inner operations of the enlarged structure. The CPT companion records their internal matrices, $i\gamma^2$ and $\gamma^0$, to be odd Clifford elements outside $\mathbb{B}$, hence outer as operations of the algebra, and leaves their intrinsic realization open. $\mathrm{Spin}^c$ is the central extension of $\mathrm{Spin}(1,3)$ by a circle and is the natural candidate for a structure in which the relevant direction is inner — but charge conjugation in four dimensions is **antilinear**, while the extra $U(1)$ of $\mathrm{Spin}^c$ is a linear phase. Whether the antilinear $C$ can be realised through a linear group, or is irreducibly external to every such group, is **not decided here** and is stated as a question rather than a result.

## The Retired Equation: The Diagnosis Is the Dispersion

The series previously wrote the massive equation as a single **antilinear** equation in one field,

$$
\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^\flat , \qquad \tilde{\Psi}^\flat = -\tilde{\Psi}^\dagger ,
$$
<!-- CONVENTION — verified, do not "fix". The claim that the retired equation ∇̃Ψ = mΨ♭ has its central-phase plane waves on the SPACELIKE locus is deliberate and is re-derived in this section (pure real arithmetic, no libraries): the two-frequency system for a single-mode field has nullity 0 on the timelike shell k₀² = k² + m² and nullity 4 on the spacelike shell k² = k₀² + m². So the spacelike dispersion is a property of that equation, not a typo, and it is exactly why the equation was retired as the mass term. Do not relocate it to the physical mass shell. -->

using the algebra's real structure. The equation is well formed; what disqualifies it is not its shape but its solutions.

Take the central-phase plane-wave ansatz of the parent article, in the block gamma representation of the canonical-quantization and spin–statistics articles, with $\tilde{\Psi} = \tilde{\Psi}_0\exp(i\,\mathrm{Sc}(\tilde{k}\bar{\tilde{X}})) = \tilde{\Psi}_0e^{i\theta}$ and $\tilde{k} = ik_0e_0 + e_1k_1 + e_2k_2 + e_3k_3$, $k_0 = \omega/c$. A single phase cannot satisfy the equation: $\tilde{\nabla}$ multiplies the phase by $+ik$, while $\flat$ conjugates the phase, so the two sides carry $e^{+i\theta}$ and $e^{-i\theta}$ and cannot match. The equation's solutions are therefore necessarily **two-frequency** superpositions,

$$
\tilde{\Psi} = \tilde{\Psi}_0\,e^{i\theta} + \tilde{\Psi}_1\,e^{-i\theta},
$$

and the equation becomes a linear system for the pair $(\tilde{\Psi}_0,\tilde{\Psi}_1)$. Its solvability depends on $\tilde{k}$, and the dependence is the whole story.

Since $\flat$ is antilinear and $i^\flat = -i$, the conjugation acts on the two modes by

$$
\tilde{\nabla}\tilde{\Psi} = i\tilde{k}\tilde{\Psi}_0e^{i\theta} - i\tilde{k}\tilde{\Psi}_1e^{-i\theta}, \qquad
\tilde{\Psi}^\flat = -\tilde{\Psi}_0^\dagger e^{-i\theta} - \tilde{\Psi}_1^\dagger e^{i\theta} ,
$$

and matching exponentials gives the two matrix equations

$$
i\tilde{k}\tilde{\Psi}_0 + m\tilde{\Psi}_1^{\dagger} = 0, \qquad
i\tilde{k}\tilde{\Psi}_1 - m\tilde{\Psi}_0^{\dagger} = 0 .
$$

These are $16$ real linear equations in the $16$ real unknowns $(\tilde{\Psi}_0,\tilde{\Psi}_1)$. Their nullity, computed by elimination and quoted for a representative momentum, is

| locus | shell condition | nullity |
|---|---|---|
| timelike | $k_0^2 = \mathbf{k}^2 + m^2$ | $0$ |
| spacelike | $\mathbf{k}^2 = k_0^2 + m^2$ | $4$ |
| elsewhere | — | $0$ |

The nullity vanishes on the physical shell and jumps to four on the spacelike locus. The equation has no timelike solutions and a four-real-dimensional family of spacelike ones — so its propagating modes are spacelike, at any $m\neq 0$. An equation whose central-phase plane waves are spacelike is not the Dirac equation, and it contradicts the four-momentum kinematics the rest of the series uses. That is why the equation was retired, and reproducing the two nullities by hand is a matter of pure real arithmetic.

### What the Failure Does and Does Not Show

The nullity table is easy to misread in two opposite ways, and both errors are worth naming.

**It does not say that antilinear equations are unphysical.** A Majorana mass is antilinear and physical, and its eigenequation has solutions on the ordinary shell. What differs between the two cases is not the linearity but the **space the conjugate lives on**:

- a **Majorana mass** pairs the field with a conjugate defined *on the same space as the field*, and its reality condition reduces the field to a real form on which the kinetic operator acts consistently; its mass shell is the ordinary $p^2 = m^2$, and its solution space is the four-real-dimensional Majorana space of the previous sections.
- the **retired equation** paired a field with the *algebra's* conjugate $\flat$, an involution of $\mathbb{B}$ that the field's own kinetic operator does not respect — left multiplication by a spatial generator carries $\mathbb{M}_-$ out of itself. The mismatch between the space of the pairing and the space of the dynamics is what the spacelike dispersion is measuring.

**It does not say that the retired equation was a notation error.** The two real structures genuinely resemble one another — both antilinear, both fixed spaces of real dimension four — so the conflation was natural, and the spacelike locus is the price of it. Separating them, as the previous section does, removes the puzzle without removing any structure.

So the correct statement is narrower than "the antilinear equation was wrong", and sharper than "the antilinear equation was a slip". The framework had **two** real structures and used one where the other was meant; the dispersion is the physical signature of the substitution.

## What the Antilinear Structure Is For

The algebra's real structure is retained, and the companion articles use the antilinear structure in four ways, none of which is a Dirac mass.

**The $\mathbb{M}_\pm$ split itself.** The material and informational sectors are the fixed spaces of $\flat$ and $\dagger$, and the framework's identification of $\mathbb{M}_-$ with material space is the statement that the field is anti-Hermitian. The sign convention by which $\flat$ acts as $+$ on $\mathbb{M}_-$ and $-$ on $\mathbb{M}_+$ *is* the convention that makes $\mathbb{M}_-$ the material sector; the two are one convention seen twice.

**Bilinear pairings and the trace.** The invariant pairings of the series are built on $\flat$, and their order-reversing-with-a-twist character, $(\tilde{A}\tilde{B})^\flat = -\tilde{B}^\flat\tilde{A}^\flat$, is what makes the trace a scalar and not a matrix.

**Kramers degeneracy and antiunitary symmetry.** An antiunitary operator squaring to $-1$ forces every level to be at least doubly degenerate. The theorem is available to the antilinear maps alone — no linear involution yields the conclusion, whatever its spectrum. The framework's real structure is itself an involution, $\flat^2 = +1$, so it is not an operator of that kind: the degeneracy belongs to the antilinear symmetries built on the structure, and the theorem is the sharpest reason the distinction between an antilinear symmetry and a linear one has content.

**The discrete symmetries.** Charge conjugation and time reversal are antilinear, and the CPT companion establishes that the antilinearity is forced — a *linear* time reversal is not a symmetry of the Dirac equation. The internal matrices of $C$, $P$ and $T$ are Clifford elements, and their grades decide which chirality each carries to: $C$ and $P$ are odd and exchange the chiral halves, $T$ is even and preserves them, so $CPT$ is even and preserves them. The grade governs the chirality; the linearity governs the spacetime parity, since an antilinear map multiplies the induced determinant by $-1$ — the point recorded in *The Reflection and the Rotation in Biquaternionic Form*.

In every one of these uses the coupling pairs the field with its conjugate, and in every one of them the pairing is a **constraint or a symmetry**, not the mass of the Dirac equation. That is the pattern the retired equation violated, and stating it positively is the content of this article: an antilinear pairing is not thereby a mass, and a mass is not thereby antilinear.

## Summary

1. **Four involutions, four fixed spaces.** The algebra carries quaternion conjugation (linear) and complex, Hermitian and anti-Hermitian conjugation (all antilinear), with fixed spaces of real dimensions $2, 4, 4, 4$. The two sectors are the fixed spaces of the last two, and the one that is the fixed space of the *linear* involution is not a sector at all.

2. **A mass is a pairing with a conjugate.** The mass is the non-derivative part of the equation; it has nothing to differentiate, so it pairs the field with a conjugate of itself. Which conjugation is the definition of which kind of mass.

3. **The two kinds are the chiral pair and the self-pairing.** The Dirac mass is linear and couples the two chiralities; the Majorana mass is antilinear and pairs the field with its own conjugate. The counts differ before any dynamics is imposed: $8$ real components against $4$.

4. **The algebra's $\flat$ and the module's $\mathcal{C}$ are different real structures.** Both antilinear, both with a four-real-dimensional fixed space, but on different spaces. The Dirac operator preserves the module's real form and does not preserve $\mathbb{M}_-$; the matching dimension count does not identify them.

5. **The $\mathrm{Spin}^c$ structure organises charge conjugation, and it decides who is charged.** $\mathrm{Spin}^c(1,3) = \bigl(\mathrm{Spin}(1,3)\times U(1)\bigr)/\{\pm 1\}$ is the spin group extended by a central circle, and the framework's central $U(1)$ — the phase that minimal coupling localizes — is that circle. Being central it commutes with $\gamma_5$ and is therefore **vector-like**: the electromagnetic $U(1)$, not a chiral one. A Dirac spinor carries it; a Majorana or ELKO spinor is fixed by an antilinear condition and is blind to it, hence neutral. It is the module's $\mathcal{C}$, not the algebra's $\flat$, that enforces the neutrality.

6. **The retired equation failed on its dispersion.** Its central-phase plane waves have nullity $0$ on the timelike shell and $4$ on the spacelike one, so its modes are spacelike. Verified by elimination in the block representation.

7. **The failure was the pairing, not the antilinearity.** A Majorana mass is antilinear and physical. The retired equation paired a field with the algebra's conjugate, on a space where its kinetic operator does not respect it.

8. **The antilinear structure is retained and used.** The sector split, the bilinear pairings, Kramers degeneracy, and the discrete symmetries $C$ and $T$ are all built on it — as constraints and symmetries, never as the Dirac mass.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra; real dim $8$, complex dim $4$ |
| $\bar{\tilde{Q}}$, $\tilde{Q}^{*}$, $\tilde{Q}^{\dagger}$, $\tilde{Q}^{\flat}$ | Quaternion, complex, Hermitian, anti-Hermitian conjugations |
| $\tilde{Q}^\flat = -\tilde{Q}^\dagger$ | The algebra's real structure; antilinear involution |
| $\mathbb{M}_- = \{\tilde{Q} : \tilde{Q}^\flat = \tilde{Q}\}$ | Anti-Hermitian (material) sector, real dim $4$ |
| $\mathbb{M}_+ = \{\tilde{Q} : \tilde{Q}^\dagger = \tilde{Q}\}$ | Hermitian (informational) sector, real dim $4$ |
| $\mathbb{H}_{\mathbb{B}} = \{\tilde{Q} : \tilde{Q}^{*} = \tilde{Q}\}$ | Real-quaternion sector, real dim $4$ |
| $\mathbb{C}_{\mathbb{B}} = \{\tilde{Q} : \bar{\tilde{Q}} = \tilde{Q}\}$ | Center, real dim $2$ |
| $\tilde{\nabla}$, $\bar{\tilde{\nabla}}$ | Biquaternionic gradient and its conjugate; $\tilde{\nabla}\bar{\tilde{\nabla}} = \Box$ |
| $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$ | The Dirac mass: linear, chirality-off-diagonal |
| $\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^\flat$ | The retired equation; spacelike dispersion, not a mass term |
| $\mathcal{C}$, $\psi^{c} = \mathcal{C}\bar{\psi}^{T}$ | Charge conjugation on the module; the Majorana reality condition |
| $\mathrm{Spin}^c(1,3) = \bigl(\mathrm{Spin}(1,3)\times U(1)\bigr)/\{\pm 1\}$ | Central extension of the spin group by a circle; its central factor is the framework's central phase, and a charged spinor is one on which that factor acts non-trivially |
| $\Delta = S\oplus\bar{S}$ | Dirac module, real dim $8$; $\mathcal{C}$ exchanges the halves |
| $m_D$, $m_M$ | Dirac and Majorana masses |
| $\flat$ acts $+$ on $\mathbb{M}_-$, $-$ on $\mathbb{M}_+$ | The sector sign; the same convention as the material identification |

## Further Reading

- Foundational articles: *Introduction to the Biquaternion Universe*; *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*; *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*; *Conventions in the Biquaternion Universe* (the mass-term convention, the real structure $\flat$, and the dispersion failure this article expands).
- The Dirac mass in biquaternionic form: *The Dirac Equation in Biquaternionic Form* (the linear chiral pair and the massless limit $\tilde{\nabla}\tilde{\Psi} = 0$); *The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit*.
- The Majorana side: *The Neutrino and Majorana Fermions in Biquaternionic Form* (charge conjugation on the module, the Majorana condition, and the obstruction by which $\mathbb{M}_-$ fails to be a reality condition); *Chiral Fermions in the Biquaternion Framework* (why a chiral fermion cannot carry a bare Dirac mass).
- The antilinear discrete symmetries: *The CPT Theorem in Biquaternionic Form* ($C$ and $T$ antilinear, and why a linear $T$ is not a symmetry).
- On the reflection parity that antilinearity shifts: *The Reflection and the Rotation in Biquaternionic Form*.
- The Clifford structures: *The Dirac Algebra and Biquaternions — A Dictionary*; *Spinors*.
- The $\mathrm{Spin}^c$ structure and its obstruction: *Spinors: Categorization* (the definition of $\mathrm{Spin}^c$, $W_3$, and $w_2$ as the mod $2$ reduction of an integral class); *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism* (the localized central phase and the $\lambda = \pm 1$ obstruction).
