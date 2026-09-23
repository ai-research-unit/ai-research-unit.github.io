# __Confinement and the Loss of Partonic Information in Biquaternionic Form__

## Introduction

Confinement is the statement that the coloured degrees of freedom of a non-abelian gauge theory do not appear in the spectrum. No isolated quark and no isolated gluon is an asymptotic state; the observable particles are colour singlets, and the colour interaction becomes strong at long distances rather than weak. The standard diagnostic is the **Wilson loop**: the trace of the holonomy of the gauge connection around a closed curve, whose expectation value distinguishes a **perimeter law**, in which the loop can be screened, from an **area law**, in which the flux is confined to a tube and the potential between two sources rises linearly with their separation.

This article asks what confinement is, information-theoretically, and its answer is that confinement is a **loss** of partonic information. That answer is a contrast with the companion article on gauge redundancy, and the contrast is the point. A gauge orbit is a redundancy: many descriptions of one configuration, and a gauge choice recovers the configuration, so nothing is lost. Confinement is not that. The partonic labels — the colour of a quark, the adjoint index of a gluon — are not redundant labels on a configuration that could be re-described; they are labels of a description that the asymptotic theory does not contain. There is no gauge in which a coloured asymptotic state appears, because there is no such state. The information is lost to the observable algebra, not hidden in the description.

Three qualifications discipline the article, and they are stated at the outset because the framework's relation to confinement is easy to overstate.

- **The order parameter is available to the framework.** The Wilson loop is a holonomy of a connection in the material sector, traced in the informational realization of the gauge group, and this is a construction the biquaternion algebra supplies exactly. The loop's asymptotic behaviour, and the information-theoretic reading of that behaviour, can therefore be written in the framework's own objects. This part is genuinely housed.
- **The confinement mechanism is not available.** The series has no colour group, no $\mathfrak{su}(3)$, no three-dimensional colour module, no non-perturbative biquaternionic action, measure or regulator, and hence no derivation of the area law, no string tension, and no mass gap. This is the finding of *Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda*, and it is inherited here without softening.
- **The loss of partonic information is a statement in standard quantum field theory.** Colour, confinement, and the colour-singlet structure of the asymptotic algebra are imported. What the framework contributes is the carrier on which the order parameter is built and the informational language in which the loss is described; the physics of the loss is cited as standard.

The article proceeds as follows. The order parameter is reviewed and the two laws are given their information-theoretic reading, with the scaling of the loop's "information cost" recomputed. The loss of the partonic labels is then formulated as a superselection statement and made precise with the relative entropy of the accessible restrictions, recomputed on generic states. The scale-dependence of the parton picture is stated as an ultraviolet-to-infrared coarse-graining, and confinement is modelled as an effectively idempotent channel onto the colour-neutral algebra, with the decoherence article as the closest written model. The framework's own objects are then separated from the imports in a ledger, and the ceiling that makes the colour group a no-route obstacle is recorded.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with quaternion basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, $e_1e_2 = e_3$, and central scalar imaginary $i$, $i^2 = -1$; the material sector is $\mathbb{M}_-$ and the informational sector $\mathbb{M}_+$, with $\mathbb{B} = \mathbb{M}_-\oplus\mathbb{M}_+$. The connection is $\tilde{A} = \sum_{\mu=0}^{3}A_\mu e_\mu \in \mathbb{M}_-$; the gauge group is realized in the informational sector, the canonical example being $\mathfrak{su}(2) = \mathrm{span}_\mathbb{R}\{ie_1,ie_2,ie_3\}$ with generators $T^a = ie_a$ and $[ie_i,ie_j] = 2i\varepsilon_{ijk}ie_k$. The holonomy and Wilson loop are

$$
U(C) = \mathcal{P}\exp\!\left(i\oint_C A_\mu\,dx^\mu\right),
\qquad
W(C) = \mathrm{Tr}\,U(C),
$$

with $\mathcal{P}$ the path ordering and the trace over the informational realization. The states of the informational sector are $\tilde{\rho}\in\mathbb{M}_+$ with $\tilde{\rho}\geq0$, $\mathrm{Tr}\tilde{\rho} = 1$, and are parametrized by the Bloch vector, $\tilde{\rho} = \tfrac12(e_0 + i\mathbf{r})$, $|\mathbf{r}|\leq1$, in the quaternion realization. The relative entropy is $S(\tilde{\rho}\|\tilde{\sigma})$; the trace formula is $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$, $\mathrm{Tr}(e_0) = 2$. The symbols $SU(3)$, $N_c$, $N_f$, $\alpha_s$, and the colour labels $\mathbf{3}$, $\mathbf{8}$ are **standard QCD notation, not framework objects**; they are used only where standard results are quoted or where an object is named as missing. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium.

## Confinement and the Order Parameter

### The Wilson Loop as the Criterion

The order parameter of the gauge theory is the expectation of the Wilson loop in the gauge-field path integral,

$$
\langle W(C)\rangle = \frac{\displaystyle\int\mathcal{D}\tilde{A}\;W(C)\,e^{iS[\tilde{A}]}}{\displaystyle\int\mathcal{D}\tilde{A}\;e^{iS[\tilde{A}]}} .
$$

Its asymptotic behaviour for large loops is the standard criterion of the phase. In the biquaternion framework the three operations of which the loop is built are provided by the algebra: the integration of a material one-form along the curve, the exponentiation into the informational realization of the group, and the trace as twice the scalar part. The average is over material-sector configurations and the trace is over the informational realization, so the order parameter is a two-sector bilinear. This construction is that of the companion article on Wilson loops, and it is recalled rather than re-derived.

### The Two Laws and the Static Potential

Two asymptotic behaviours are possible for a large loop.

- A **perimeter law**,
$$
\langle W(C)\rangle \sim e^{-\mu_{\mathrm{per}}\,\mathrm{perim}(C)},
$$
is the behaviour of a theory in which the flux between two sources can spread: the cost is proportional to the length of the loop, and the sources are screened.

- An **area law**,
$$
\langle W(C)\rangle \sim e^{-\sigma\,\mathrm{area}(C)},
$$
is the behaviour of a confining theory: a flux tube forms, the cost is proportional to the enclosed area, and the coefficient $\sigma$ is the **string tension**.

The rectangular loop of spatial width $L$ and temporal extent $T$ connects the law to the static potential. For large $T$ the loop exponentiates the energy of the pair of sources it creates,

$$
\langle W(\square_{L\times T})\rangle \sim e^{-iT\,V(L)},
$$

so that an area law corresponds to $V(L) = \sigma L$, a linearly rising potential, and a perimeter law to a potential that flattens at large $L$. These statements are standard, proved on the lattice by the strong-coupling expansion, and cited rather than reproduced; the framework's relation to them is the subject of the ledger below.

### The Information Cost of the Loop

The loop's expectation value is exponentially small in the size of the loop, and its negative logarithm is the natural cost of the configuration: in the Euclidean theory it is the action of the flux that the loop describes, so that for the rectangular loop it equals $T\,V(L)$ — the energy of the separated sources multiplied by the time they are held apart. Define

$$
I(C) := -\log\bigl|\langle W(C)\rangle\bigr| .
$$

The definition reads the decay of the loop's modulus, so it is the **Euclidean** cost: it is taken in the signature in which the perimeter and area laws above hold as written, with real exponents. In Minkowski signature the rectangular loop is $e^{-iTV(L)}$, a pure phase whose modulus is exactly one for real $V(L)$, so the cost as defined would vanish on it identically. The two are related by the analytic continuation $T\to -iT$ (the Minkowski $T$), which turns the phase into the decay and the decay back into the phase. The information cost and the potential are the same quantity read in the two signatures, and the scaling analysis below is made in the Euclidean one.

Then the two laws read

$$
I(C) \simeq \mu_{\mathrm{per}}\,\mathrm{perim}(C)
\qquad\text{or}\qquad
I(C) \simeq \sigma\,\mathrm{area}(C),
$$

and the two are distinguished not by the size of $I$ but by its **scaling**: the first grows with the length of the loop, the second with the region it encloses. For the rectangular loop,

$$
I(\square_{L\times T}) \simeq
\begin{cases}
2\mu_{\mathrm{per}}(L+T), & \text{perimeter},\\[2pt]
\sigma\,LT, & \text{area},
\end{cases}
$$

so that the quantity $I/T$ at large $T$ is a constant for the perimeter law and grows linearly in $L$ for the area law:

$$
\lim_{T\to\infty}\frac{I(\square_{L\times T})}{T}
=
\begin{cases}
2\mu_{\mathrm{per}}, & \text{perimeter},\\[2pt]
\sigma L, & \text{area}.
\end{cases}
$$

This was recomputed directly. With the area law at unit string tension, $I = LT$, the ratio $I/T$ took the values $1.000$, $2.000$, $4.000$ at $L = 1,2,4$ for both $T = 50$ and $T = 100$, reproducing $\sigma L$ exactly. With the perimeter law at $\mu_{\mathrm{per}} = 0.5$ per unit length, $I = 0.5\cdot2(L+T)$, the ratio took the values $1.020, 1.040, 1.080$ at $T = 50$ and $1.010, 1.020, 1.040$ at $T = 100$, approaching the constant $2\mu_{\mathrm{per}} = 1$ as $T$ grows and the $L/T$ correction vanishes. The two behaviours are therefore distinguishable by a single number extracted from the large-$T$ limit of the loop, and that number is either constant in $L$ or proportional to $L$.

Read information-theoretically, the area law says that the cost of maintaining the configuration is proportional to the **area swept** by the separation, not to its boundary. The flux configuration is non-local: the tube stores an amount of information per unit length that does not decay with separation, and the string tension $\sigma$ is the information cost per unit of separation per unit of time. A perimeter law, by contrast, is the behaviour of a short-ranged correlation: the cost is a boundary term and the sources are screened. Confinement is thus the statement that the loop's information cost is **extensive in the enclosed region rather than in its boundary**, and it is the signature that the coloured flux cannot be spread into the vacuum.

## The Parton Labels and Their Loss

### Colour as a Superselected Label

In the partonic description the fundamental fields carry colour: a quark transforms in the fundamental representation $\mathbf{3}$ and a gluon in the adjoint $\mathbf{8}$. In the confined phase the asymptotic observables are colour singlets, and the colour labels are not observable at infinity. The structure is that of a **superselection rule**: the observable algebra at infinity commutes with the colour generators, and two states that differ only by a colour rotation are indistinguishable to it.

This is standard physics and is imported. Two features of it are worth separating, because only one is a loss.

- The **total colour charge** of a physical state is a superselected (in fact vanishing) label: physical states are colour singlets. This is a constraint on the state space, not an information channel.
- The **individual parton colours** inside a hadron are not labels on the asymptotic state space at all. A hadron is one colour-singlet state; the many partonic configurations that produce it are not distinguishable by any asymptotic observable. This is the non-invertibility, and it is the loss.

The distinction between the two is the distinction between a constraint and a channel, and the information-theoretic content is in the second.

One qualification keeps the model honest. The colour symmetry of QCD is local, so a rigid colour rotation is a gauge transformation of the full theory, and the superselection statement above is a statement about the algebra of colour-invariant operators rather than about a group of physical rotations. What makes the restriction a loss and not a redundancy is that the partonic configurations a hadron's infrared description cannot separate are not gauge copies of one another: they differ in the momenta and the number of their constituents, which no change of description removes. The model of the next subsection uses the framework's own internal charge, realized in the informational sector, for which the rotation is non-trivial — the framework's gauge group is the abelian central phase, which acts trivially on $\mathbb{M}_+$, so the two are distinct transformations of the algebra.

### The Restricted State and the Vanishing Relative Entropy

The superselection statement can be made exact without a colour group, on the framework's own state space, by using the commutant structure that any charge superselection rule produces. Let a charge generator be represented on the informational sector by an element of $\mathfrak{su}(2)\subset\mathbb{M}_+$, so that the rotation $\tilde{\rho}\mapsto U\tilde{\rho}\,U^\dagger$ with $U = \exp(i\theta\, n_a ie_a/2)$ is the charge rotation about the axis $\mathbf{n}$. The **accessible** state is the restriction of $\tilde{\rho}$ to the algebra of observables commuting with the charge; in the quaternion realization this restriction is the dephasing of the Bloch vector along the charge axis,

$$
\mathbf{r} \;\longmapsto\; (\mathbf{r}\cdot\hat{\mathbf{n}})\,\hat{\mathbf{n}},
$$

the projection of the Bloch vector onto the axis, which is the full-dephasing limit of the companion article on idempotent projection. Two states that differ by a charge rotation have **the same accessible state**:

$$
\mathbf{r}\cdot\hat{\mathbf{n}} = (R_{\hat{\mathbf{n}}}(\theta)\mathbf{r})\cdot\hat{\mathbf{n}},
$$

because a rotation about $\hat{\mathbf{n}}$ preserves the component along $\hat{\mathbf{n}}$. Their full relative entropy is generally positive, but the relative entropy of their accessible restrictions vanishes. This was checked on explicit states: with $\mathbf{r} = (0.5,-0.3,0.4)$ and a charge rotation about $\hat{\mathbf{n}} = (0,0,1)$ by $1.1$ radians, the full relative entropy was $S(\tilde{\rho}\|\tilde{\rho}_{\mathrm{rot}}) = 0.231562$, while the accessible relative entropy vanished identically, and the two accessible Bloch vectors agreed exactly.

The lesson is the article's thesis in its sharpest form. A charge rotation is not a gauge transformation: it changes the state, and the full relative entropy detects the change. But the change is invisible to the accessible algebra, and the accessible algebra is the whole of what survives to asymptotic observation. The information lost is exactly the component of the state along the unobservable charge directions, and no re-description recovers it.

### Why This Is Loss and Not Redundancy

The contrast with the companion article on gauge redundancy is now exact.

A gauge transformation is implemented by the central phase, which for the framework's gauge group is central and of unit modulus: it therefore fixes the state itself, $\tilde{\rho}\mapsto\lambda\tilde{\rho}\lambda^\dagger = \tilde{\rho}$, and not merely its restriction. The two descriptions are two ways of writing one state, and the coincidence is exact rather than a projection. A charge rotation also acts by a unitary, but the accessible algebra is a **proper subalgebra** — the commutant of the charge — so the rotated state restricts to the same accessible state only because the distinction has been projected out by the restriction, not because it was never there. The map from states to accessible states is many-to-one on a non-trivial fibre, and the fibre is the set of states with the same charge-axis component. That is the structure of a lossy channel, and the next section develops it.

One more distinction is worth recording. In the gauge case the fibre is a group orbit and a representative recovers the configuration; the locality of the gauge choice is the only obstruction. In the confinement case the fibre contains partonic configurations that no asymptotic operation distinguishes, and the obstruction is the spectrum itself. Redundancy is a property of the description; loss is a property of the theory.

## The Parton Picture Is an Ultraviolet Description

### Resolution and Scale

The parton picture is not a description of a hadron at rest; it is a description at a resolution. The parton distribution functions are functions of the momentum transfer, and the coupling runs: at short distances the colour coupling is weak and the partons are resolved, while at long distances it is strong and the resolution fails. The information-theoretic reading is that the partonic information is **ultraviolet data**, and confinement is its infrared fate.

The framework's own renormalization-group article reaches the non-abelian case and reproduces the standard one-loop beta function,

$$
\beta_g = -\frac{g^3}{16\pi^2}b_0,
\qquad
b_0 = \frac{11}{3}C_2(G) - \frac{2}{3}\sum_{\text{Weyl}}T(r),
$$

with $C_2(G) = N$ and the QCD coefficient $b_0 = 11 - \tfrac{2}{3}N_f$ for $SU(3)$. But the article states plainly that the gauge group, the matter content, the action, the measure, and the regulator are **inputs**, and that the beta functions are transcriptions. The flow acts on central scalars, and the algebraically natural sharp cutoff is imposed on the central norm form $\tilde{k}\bar{\tilde{k}}$. So the framework houses the form of the flow, and the flow is the coarse-graining that degrades the partonic information, but the group and the matter that give the flow its meaning are the missing objects.

### Coarse-Graining as a Channel

On general grounds the flow from an ultraviolet description to an infrared description is a **completely positive trace-preserving map** between state spaces, and relative entropy is monotone under it:

$$
S\bigl(\Phi(\tilde{\rho})\,\big\|\,\Phi(\tilde{\sigma})\bigr) \;\leq\; S(\tilde{\rho}\|\tilde{\sigma}).
$$

The inequality is the precise sense in which the flow loses information: two partonic states that were distinguishable at the ultraviolet scale become less distinguishable, or indistinguishable, at the infrared scale. When the image of the map is a proper subalgebra — when distinct states are identified by it, as for the colour-singlet expectation of the next section — the inequality can be strict, and it becomes an equality at zero whenever the two states lie in the same fibre. The restricted relative entropy computed above is exactly that case, and there the loss is total.

The framework's own relative-entropy companion supplies the monotonicity statement; the flow supplies the map; and the confinement statement is that the infrared map has the colour directions in its kernel. What the framework cannot supply is the map itself, because it has no colour and no non-perturbative action.

## Confinement as an Effectively Idempotent Channel

### The Colour-Singlet Conditional Expectation

The loss can be modelled by a single map. Let $\mathcal{M}$ be the algebra of observables carrying the colour action and $\mathcal{N}\subset\mathcal{M}$ the colour-neutral subalgebra, the fixed points of the colour rotations. The **conditional expectation** onto the fixed points,

$$
E:\mathcal{M}\to\mathcal{N},
\qquad
E(X) = \int_{G} dU\;U X U^{-1},
$$

averaging over the colour group with its normalized Haar measure, is a completely positive unital idempotent map: $E^2 = E$. It is the colour-singlet projection, and it is the natural model of what the asymptotic description retains. Applied to a state, it discards exactly the off-diagonal colour coherences and keeps the colour-neutral content, so that

$$
S\bigl(E(\tilde{\rho})\,\big\|\,E(\tilde{\sigma})\bigr) \;<\; S(\tilde{\rho}\|\tilde{\sigma})
$$

whenever at least one of the two states carries a colour coherence. The model is the same idempotent-projection structure that the companion article on decoherence develops in the informational sector; there, the projection is onto the pointer basis selected by an environment, and here it is onto the colour singlets selected by the spectrum.

### Comparison with Decoherence

The comparison is close and the difference is the reason the article keeps the two words apart.

- **Decoherence** is a dynamical process: an environment entangles with the system, and the off-diagonal coherences of the reduced state decay. The information is not destroyed; it is delocalized into correlations with the environment, and in principle it could be recovered from the whole. The projection is effective, not fundamental.
- **Confinement** is a spectral statement: the coloured states are absent from the asymptotic spectrum, so there is no coloured environment in which the colour could be stored and no larger system from which it could be recovered. The projection is the restriction to what exists asymptotically.

The formal structure — an idempotent channel onto a subalgebra — is shared, and that is why the decoherence article is the closest written model. The physical content is different: decoherence is the loss of *phase coherence* into an environment, confinement is the absence of the *labels* from the spectrum. The first is a relocation to an inaccessible but existing sector; the second is a loss with no such sector. The article on the Higgs mechanism treats the third case, in which what is removed is a gauge coordinate rather than a physical degree of freedom, so that the removal is a reversible re-encoding rather than a loss.

## The Mass Gap and the Correlation Length

### Confinement as a Gap

Confinement is tied to a **mass gap**. In the lattice formulation the area law implies one — the Osterwalder–Seiler result, cited as standard, is that a theory whose loops obey an area law has no massless excitation — and the link is natural: a massless coloured state would be an unconfined long-range colour field, and a gap says that no such massless carrier exists, so the colour force is transmitted only over a finite range. Both statements are part of the standard lattice confinement analysis, cited rather than derived.

The gap is where the information-theoretic reading becomes a statement about **correlations**. Let $O$ be a local operator of the colour-singlet sector — a glueball operator, in standard language. Its connected two-point function decays at long distance at the rate set by the lightest intermediate state,

$$
\bigl\langle O(x)O(y)\bigr\rangle_{c} \;\sim\; e^{-m|x-y|} \quad\text{as } |x-y|\to\infty,
$$

with $m$ the lightest mass, so that the **correlation length** is $\xi = 1/m$. Beyond $\xi$ even the colour-singlet correlations are lost: a local measurement cannot learn the configuration of a distant source, and the information that survives at long distance is the global one — the string between the sources. An operator that carries colour explicitly is the one dressed by a Wilson line, and its long-distance behaviour is the area law of the previous section, a decay governed by the string tension rather than by $m$; the exponential above is the gap's statement about the singlet sector, and the area law is the confining statement about the coloured one.

### The Two Ways Information Fails to Propagate

The gap and the area law are two faces of the same loss and it is worth stating how they differ.

- The **area law** is a statement about the *energy* of a configuration of separated sources: it grows with their separation, so the sources cannot be pulled apart.
- The **gap** is a statement about the *decay of correlations*: the colour-singlet sector is correlated only over a finite distance.

Both say that the confined theory has no long-range carrier: the first, that separating colour sources costs an energy growing without bound; the second, that correlations die off beyond the correlation length — the colour-singlet ones included.

The information-theoretic reading of the second is a statement about the **scale at which a source can be read at all**. A colour-singlet operator's connected correlator is the object whose long-distance decay defines $\xi$, so $\xi$ is the distance beyond which no local measurement retains information about a distant source: the correlation is the measurable proxy for distinguishability, and its exponential decay is what a loss statement can be built on without further assumption.

It is worth being exact about what is not claimed. Whether the relative entropy between two configurations differing in a distant colour measurement inherits precisely the scale $\xi$ is a question this article does not settle. Pinsker's bound relates the relative entropy to the trace distance from below, so a relative entropy that stays bounded away from zero entails that some observable distinguishes the two states; it does not entail that the distinguishing observable is local. It is the converse direction — small local correlators forcing a small relative entropy — that the scale statement would need, and that direction holds only with a bound running the other way, under regularity conditions on the states that the framework does not supply. What is safe, and is the sharpest form of the loss available here, is the qualitative contrast: in the confined phase the correlations that could carry a colour distinction die off exponentially and the label is absent from the spectrum altogether, whereas in an unconfined phase whose gauge field stays massless — the Coulomb phase of QED is the standard instance — the long-range field does carry the charge to infinity, and the correlations decay only as a power. The framework has no mass gap and no derived correlation length; the statement is carried as standard physics.

## The Biquaternion Framework: What It Can and Cannot State

### The Loop in the Two Sectors

The order parameter is the framework's own construction. The connection integrated along the curve is a material one-form, $\tilde{A}\in\mathbb{M}_-$; the group element it exponentiates into is an element of the informational realization of the gauge group; and the trace is twice the scalar part. The loop is therefore an $\mathbb{M}_+$ trace of an object whose logarithm lies in $\mathbb{M}_-$, and its gauge invariance is the invariance of the scalar part under the adjoint action. The small-loop expansion, $W = 1 + ia^2F_{\mu\nu} + O(a^4)$, and the centrality of $\tilde{F}^2$, whose two scalar parts are the two Lorentz invariants of the field strength, are established in the Wilson-loop companion and are not repeated. What this gives the present article is a place to put the order parameter and, consequently, a place to put the information-theoretic reading of its two laws.

### The Ceiling: No Colour

What the framework cannot supply is the colour theory whose order parameter the loop is supposed to be. The compact algebra available inside $\mathbb{B}$ is the maximal compact subalgebra of $\mathfrak{gl}(2,\mathbb{C})$, namely

$$
\mathfrak{u}(2) = \mathfrak{u}(1)\oplus\mathfrak{su}(2),
\qquad \dim_\mathbb{R} = 4 ,
$$

and the matter side has the matching ceiling: $\mathbb{B}\cong M_2(\mathbb{C})$ is simple with unique simple module $\mathbb{C}^2$, so every $\mathbb{B}$-module has complex dimension $2k$ and a three-dimensional colour module does not exist. No $\mathfrak{su}(3)$ subalgebra and no colour triplet are available on the present construction. The consequence for this article is direct: the partonic information whose loss confinement describes is not present in the framework at all, so the framework's own loss statement is at best the corresponding statement for a $\mathfrak{u}(2)$ theory, which is not QCD. The area law, the string tension, the flux tube, the mass gap, and the colour-singlet structure are imports.

This is exactly the position the QCD agenda records, and the information-theoretic reading does not change it. It sharpens it: the loss of partonic information is a statement about which labels the asymptotic algebra contains, and the framework's asymptotic algebra — whatever it is — is built on a carrier that has no colour labels to lose.

## What the Algebra Supplies, Transcribes, and Does Not Supply

**Supplied by the algebra, and recomputed here.** The Wilson loop as a two-sector bilinear: a material-sector connection integrated along a curve, exponentiated into the informational realization of the group, traced to a gauge-invariant number. The information-theoretic reading of the two laws, with the scaling of $I(C) = -\log|\langle W(C)\rangle|$ recomputed: $I/T\to$ constant for the perimeter law and $I/T\to\sigma L$ for the area law, in both cases to the stated accuracy. The superselection structure of a charge rotation on the informational sector, with the accessible state as the dephasing along the charge axis and the accessible relative entropy vanishing while the full relative entropy is positive — recomputed on explicit states. The conditional expectation onto the charge-neutral subalgebra as an idempotent channel — realized on the framework's own compact algebra $\mathfrak{su}(2)\subset\mathbb{M}_+$, the group whose singlets the framework's own superselection analysis selects, and only transcribed for a colour group — and the monotonicity of relative entropy under it, cited from the companion articles.

**Transcribed from standard physics.** Confinement itself: the area law as the criterion, the flux tube, the linearly rising potential, the string tension, the lattice strong-coupling argument that establishes the area law, the mass gap, the colour group and its representations, the partonic description and its scale dependence, and the running of the colour coupling. The colour-singlet structure of the asymptotic algebra and the superselection of colour are standard. All of these are imports and are flagged as such throughout.

**Not supplied.** The colour group, the confinement mechanism, the area law, the string tension, the mass gap, the non-perturbative biquaternionic action, measure and gauge-invariant regulator, and any empirical consequence. The framework states the order parameter and the informational language; it does not derive the physics that gives them their QCD meaning. The honest summary is the QCD agenda's: confinement is an obstacle with no route yet.

**Companion articles.** The construction rests on the following written articles of the series.

- Companion article *Wilson Loops in Biquaternionic Form*, for the holonomy, the loop as a two-sector bilinear, the perimeter and area laws, and the small-loop expansion.
- Companion article *Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda*, for the ceiling on the compact gauge algebra, the absence of a colour group and a colour triplet, and the no-route status of confinement.
- Companion article *The Renormalization Group in Biquaternionic Form*, for the one-loop running and the statement that the group, matter, action, measure and regulator are inputs.
- Companion article *Decoherence as Idempotent Projection*, for the idempotent-channel model of a loss onto a subalgebra and the full-dephasing limit.
- Companion article *Relative Entropy and the Biquaternion Framework*, for the relative entropy and its monotonicity under completely positive maps.
- Companion article *Non-Abelian Gauge Fields in Biquaternionic Form*, for the non-abelian connection and the generators realized in the informational sector.
- Companion article *Chiral Fermions in the Biquaternion Framework*, for the chiral structure of the module and the vector-like character of the framework's gauge group.
- Companion article *Gauge Redundancy and the Information in the Gauge Orbit in Biquaternionic Form*, for the redundancy case against which this article's loss is defined.
- Companion article *The Higgs Mechanism as an Erasure of Information in Biquaternionic Form*, for the relocation case against which this article's loss is defined.

## Open Questions

1. **A sector-theoretic order parameter.** The confinement transition is a change in the long-distance behaviour of $\langle W(C)\rangle$. Is there a biquaternionic order parameter — an element of the algebra whose norm or scalar part measures the transition, rather than a functional of loops — and does the transition appear as a change in a property of the algebra's own objects? The Wilson-loop companion records the same question.

2. **The information budget of the flux tube.** The string tension is the cost per unit length of the tube. Is there a framework-internal object whose entropy density is $\sigma$, in the way the series' *Black Hole Thermodynamics in Biquaternionic Form* relates an entropy to a horizon area? No such object is known.

3. **Can the loss be made a theorem?** On the framework's carrier the accessible algebra is a commutant of a charge, and the restricted relative entropy vanishes. Is there a general statement — an algebraic theorem about idempotent conditional expectations and their fibres — that would state the loss without importing colour, and that would apply to whatever gauge theory the framework eventually carries?

4. **The regulator and the loss.** The loss is a statement about the infrared. The framework's regulators are sector-blind and its sharp cutoff breaks gauge invariance. Does a gauge-invariant regulator within the algebra change the information-theoretic picture, and is there a renormalization of the restricted relative entropy?

5. **The relation to the Reeh–Schlieder statements.** The local algebra of a region is large: by Reeh–Schlieder it is cyclic and separating for the vacuum and contains operators of every particle number. The confinement loss is nevertheless a statement about the asymptotic algebra. How the two coexist — a large local algebra and a small asymptotic one — is the structural question, and the framework's infinite-dimensional module algebra is the setting for it.

6. **Empirical content.** As everywhere, whether any of this yields a prediction distinguishing the framework from standard QCD. Since the colour group, matter content, coupling, and confinement mechanism are all imports, no such prediction is in view.

## Summary

Confinement is the absence of the coloured degrees of freedom from the asymptotic spectrum, diagnosed by the Wilson loop: a perimeter law for a screened phase and an area law for a confining one, with the rectangular loop giving the static potential. In the biquaternion framework the loop is a two-sector bilinear — a material-sector connection integrated around a curve, exponentiated into the informational realization of the gauge group, and traced to a gauge-invariant number — so the order parameter is housed exactly.

The information-theoretic reading is that confinement is a **loss** of partonic information, in contrast with the redundancy of the gauge orbit. The loop's information cost $I(C) = -\log|\langle W(C)\rangle|$ scales with the perimeter in a screened phase and with the area in a confining one; for the rectangular loop, $I/T$ tends to a constant for the perimeter law and to $\sigma L$ for the area law, and both were recomputed to the stated accuracy. The string tension is the information cost per unit separation per unit time, and the area scaling is the signature that the coloured flux cannot spread into the vacuum.

The loss of the partonic labels is a superselection statement. A charge rotation is not a gauge transformation: it changes the state, and the full relative entropy detects the change. But the accessible algebra is the commutant of the charge, and the charge-rotated states restrict to the same accessible state, whose relative entropy vanishes. This was checked on explicit states, where the full relative entropy was $0.231562$ and the accessible relative entropy was zero to machine precision. The map from states to accessible states is many-to-one on a non-trivial fibre, which makes it a lossy channel; the conditional expectation onto the colour-neutral subalgebra is an idempotent model of it, and the decoherence article is the closest written model while differing in that decoherence delocalizes information into an environment and confinement has no such environment.

What the framework cannot supply is the colour theory itself. The compact algebra inside $\mathbb{B}$ is at most $\mathfrak{u}(2)$ of dimension $4$, every $\mathbb{B}$-module has even complex dimension, and a colour triplet and a gluon octet do not exist on the present construction. The area law, string tension, flux tube, mass gap, and colour-singlet structure are therefore imports, and the framework's contribution is the carrier of the order parameter and the informational language of the loss, not the physics of confinement.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H} \cong M_2(\mathbb{C})$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_1e_2 = e_3$ |
| $i$ | Scalar imaginary, $i^2 = -1$, central |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material and informational sectors |
| $\tilde{A} = \sum_\mu A_\mu e_\mu\in\mathbb{M}_-$ | Gauge connection (material sector) |
| $T^a = ie_a\in\mathbb{M}_+$ | Generators realized in the informational sector |
| $U(C) = \mathcal{P}\exp(i\oint_C A_\mu dx^\mu)$ | Holonomy |
| $W(C) = \mathrm{Tr}\,U(C)$ | Wilson loop; order parameter |
| $\langle W(C)\rangle \sim e^{-\mu_{\mathrm{per}}\,\mathrm{perim}}$ | Perimeter law (screening) |
| $\langle W(C)\rangle \sim e^{-\sigma\,\mathrm{area}}$ | Area law (confinement) |
| $\mu_{\mathrm{per}}$ | Perimeter coefficient |
| $\sigma$ | String tension |
| $\square_{L\times T}$, $V(L)$ | Rectangular loop; static potential; $\langle W\rangle\sim e^{-iTV(L)}$ |
| $I(C) = -\log|\langle W(C)\rangle|$ | Information cost of the loop |
| $\tilde{\rho} = \tfrac12(e_0 + i\mathbf{r})$, $|\mathbf{r}|\leq1$ | State of the informational sector (Bloch ball) |
| $\mathbf{r}\cdot\hat{\mathbf{n}}$ | Component along the charge axis; accessible content |
| $R_{\hat{\mathbf{n}}}(\theta)$, $U = e^{i\theta n_a ie_a/2}$ | Charge rotation |
| $S(\tilde{\rho}\|\tilde{\sigma})$ | Relative entropy; monotone under channels |
| $E(X) = \int_G dU\, UXU^{-1}$ | Colour-singlet conditional expectation; idempotent channel |
| $\beta_g = -(g^3/16\pi^2)b_0$, $b_0 = 11 - \tfrac{2}{3}N_f$ | One-loop running (transcribed) |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace pairing; $\mathrm{Tr}(e_0) = 2$ |
| $\mathfrak{u}(2) = \mathfrak{u}(1)\oplus\mathfrak{su}(2)$, $\dim_\mathbb{R} = 4$ | Ceiling on the framework's compact gauge algebra |
| **Standard QCD notation, not framework objects** | |
| $SU(3)$, $N_c = 3$, $\mathbf{3}$, $\mathbf{8}$ | Colour group, number of colours, quark, gluon — no route yet |
| $N_f$, $\alpha_s$ | Quark flavour number, strong coupling — imports |

## Further Reading

- Kenneth G. Wilson, "Confinement of Quarks," *Physical Review D* **10** (1974) 2445–2459, for the Wilson loop, the area law, and confinement as a criterion.
- John B. Kogut, "An Introduction to Lattice Gauge Theory and Spin Systems," *Reviews of Modern Physics* **51** (1979) 659–713, for the lattice formulation and the strong-coupling derivation of the area law.
- K. Osterwalder and E. Seiler, "Gauge Field Theories on a Lattice," *Annals of Physics* **110** (1978) 440–471, for the statement that the area law implies a mass gap.
- Alexander M. Polyakov, *Gauge Fields and Strings* (Harwood, 1987), for the flux tube, the string picture, and the large-distance behaviour of the loop.
- Gerard 't Hooft, "On the Phase Transition Towards Permanent Quark Confinement," *Nuclear Physics B* **138** (1978) 1–25, for the confinement criterion and the behaviour of the loop in the two phases.
- Yu. M. Makeenko and A. A. Migdal, "Exact Equation for the Loop Average in Multicolor QCD," *Physics Letters B* **88** (1979) 135–137, for the loop equation and its large-$N$ closure.
- J. D. Bjorken and E. A. Paschos, "Inelastic Electron–Proton and Gamma–Proton Scattering and the Structure of the Nucleon," *Physical Review* **185** (1969) 1975–1982, for the parton picture and its scale dependence.
- H. David Politzer, "Reliable Perturbative Results for Strong Interactions?", *Physical Review Letters* **30** (1973) 1346–1349, for asymptotic freedom and the running of the colour coupling.
- David J. Gross and Frank Wilczek, "Ultraviolet Behavior of Non-Abelian Gauge Theories," *Physical Review Letters* **30** (1973) 1343–1346, for asymptotic freedom.
- Roman W. Jackiw and Claudio Rebbi, "Vacuum Periodicity in a Yang–Mills Quantum Theory," *Physical Review Letters* **37** (1976) 172–175, for the topological vacuum structure of the confined phase.
- Huzihiro Araki, "Relative entropy of states of von Neumann algebras," *Publications of the Research Institute for Mathematical Sciences* **11** (1976) 809–833, for relative entropy, monotonicity, and its behaviour under conditional expectations.
- M. Ohya and D. Petz, *Quantum Entropy and Its Use* (Springer, 1993), for the monotonicity of relative entropy under completely positive maps and the structure of idempotent channels.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the channel formalism and the distinguishability measures used here.
