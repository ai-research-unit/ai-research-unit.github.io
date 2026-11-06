# __Confinement and the Loss of Partonic Information in Biquaternionic Form__

## Introduction

Confinement is the statement that the coloured degrees of freedom of a non-abelian gauge theory do not appear in the spectrum. No isolated quark and no isolated gluon is an asymptotic state; the observable particles are colour singlets, and the colour interaction becomes strong at long distances rather than weak. The standard diagnostic is the **Wilson loop**: the trace of the holonomy of the gauge connection around a closed curve, whose expectation value distinguishes a **perimeter law**, in which the loop can be screened, from an **area law**, in which the flux is confined to a tube and the potential between two sources rises linearly with their separation.

This article asks what confinement is, information-theoretically, and its answer is that confinement is a **loss** of partonic information. That answer is a contrast with the companion article on gauge redundancy, and the contrast is the point. A gauge orbit is a redundancy: many descriptions of one configuration, and a gauge choice recovers the configuration, so nothing is lost. Confinement is not that. The partonic labels — the colour of a quark, the adjoint index of a gluon — are not redundant labels on a configuration that could be re-described; they are labels of a description that the asymptotic theory does not contain. There is no gauge in which a coloured asymptotic state appears, because there is no such state. The information is lost to the observable algebra, not hidden in the description.

Four qualifications discipline the article, and they are stated at the outset because the framework's relation to confinement is easy to overstate.

- **The order parameter is available to the framework.** The Wilson loop is a holonomy of a connection in the material sector, traced in the informational realization of the gauge group, and this is a construction the biquaternion algebra supplies exactly. The loop's asymptotic behaviour, and the information-theoretic interpretation of that behaviour, can therefore be written in the framework's own objects. This part is genuinely housed.
- **The confinement mechanism is not available.** The series has no colour group, no $\mathrm{SU}(3)$, no three-dimensional colour module, no non-perturbative biquaternionic action, measure or regulator, and hence no derivation of the area law, no string tension, and no mass gap. This is the finding of *Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda*, and it is inherited here without softening.
- **The two confinement pictures are not the same object.** The absent mechanism is the non-perturbative gauge dynamics behind the loop. There is a second picture, the **bag**, in which confinement is a linear **boundary condition** on the field inside a bounded region; that picture is a boundary-value problem, and it is the one piece of confinement the framework's own function theory does reach. The article keeps the two apart rather than letting "no mechanism" cover both.
- **The loss of partonic information is a statement in standard quantum field theory.** Colour, confinement, and the colour-singlet structure of the asymptotic algebra are imported. What the framework contributes is the carrier on which the order parameter is built and the informational language in which the loss is described; the physics of the loss is cited as standard.

The article proceeds as follows. The order parameter is reviewed and the two laws are given their information-theoretic interpretation, with the scaling of the loop's "information cost" recomputed. The loss of the partonic labels is then formulated as a superselection statement and made precise with the relative entropy of the accessible restrictions, recomputed on generic states. The scale-dependence of the parton picture is stated as an ultraviolet-to-infrared coarse-graining, and confinement is modelled as an effectively lossy channel onto the colour-neutral algebra, with the decoherence article as the closest written model. The other confinement picture — the bag as a linear boundary condition, the two Dirac equations it uses (the one-sided chiral pair and the two-sided equation the dictionary produces), and its reduction to a boundary equation in the algebra — is then given, because it is the part of confinement the framework houses. The framework's own objects are then separated from the imports in a ledger, and the ceiling that makes the colour group a no-route obstacle is recorded there.

$$
U(C) = \mathcal{P}\exp\!\left(i\oint_C \sum_\mu\varepsilon_\mu A_\mu\,dx_\mu\right),
\qquad
W(C) = \mathrm{Tr}\,U(C),
$$

with $\varepsilon$ the corpus's plain weight, $\mathcal{P}$ the path ordering and the trace over the informational realization. The state of the informational sector is the corpus's $\tilde{Ϛ}$, of trace one and parametrized by the Bloch vector $\vec r$, and the relative entropy of two states is $S(\tilde{Ϛ}_1\|\tilde{Ϛ}_2)$; the trace, twice the scalar part, is the one of *Norm and Pairing Conventions*. The symbols $SU(3)$, $N_c$, $N_f$, $\alpha_s$, and the colour labels $\mathbf{3}$, $\mathbf{8}$ are **standard QCD notation, not framework objects**; they are used only where standard results are quoted or where an object is named as missing. Throughout, $i$ is the central scalar imaginary, so $i^2=-1$; wherever two imaginary factors meet, the display below simplifies them explicitly.

The derivative of this article is the corpus's gradient $\tilde\nabla$, with its quaternion conjugate $\tilde\nabla^\natural$ and the d'Alembertian $\Box$, fixed in *Operator and Calculus Conventions*, where the material-sector reading of the time derivative is stated as well. Every other first-order operator here is written from these, by a shift or by the central imaginary. No other first-order operator is introduced, and no letter stands for a side: an action that is not a multiplication by an element is written out as one, in the form $f\mapsto fb$.

## Confinement and the Order Parameter

### The Wilson Loop as the Criterion

The order parameter of the gauge theory is the expectation of the Wilson loop in the gauge-field path integral,

$$
\langle W(C)\rangle = \frac{\displaystyle\int\mathcal{D}\tilde{A}\;W(C)\,\exp(iS[\tilde{A}])}{\displaystyle\int\mathcal{D}\tilde{A}\;\exp(iS[\tilde{A}])} .
$$

Its asymptotic behaviour for large loops is the standard criterion of the phase. In the biquaternion framework the three operations of which the loop is built are provided by the algebra: the integration of a material one-form along the curve, the exponentiation into the informational realization of the group, and the trace as twice the scalar part. The average is over material-sector configurations and the trace is over the informational realization, so the order parameter is a two-sector bilinear. This construction is that of the companion article on Wilson loops, and it is recalled rather than re-derived.

### The Two Laws and the Static Potential

Two asymptotic behaviours are possible for a large loop.

$$
\langle W(C)\rangle \sim \exp\bigl(-\mu_{\mathrm{prm}}\,\mathrm{perim}(C)\bigr)
\qquad\text{(perimeter law)},
\qquad
\boxed{\;\langle W(C)\rangle \sim \exp\bigl(-\sigma\,\mathrm{area}(C)\bigr)\;}\quad\text{(area law)} .
$$

A **perimeter law** is the behaviour of a theory in which the flux between two sources can spread: the cost is proportional to the length of the loop, and the sources are screened. An **area law** is the behaviour of a confining theory: a flux tube forms, the cost is proportional to the enclosed area, and the coefficient $\sigma$ is the **string tension**.

The rectangular loop of spatial width $L$ and temporal extent $T$ connects the law to the static potential. For large $T$ the loop exponentiates the energy of the pair of sources it creates,

$$
\langle W(C_{L\times T})\rangle \sim \exp(-iT\,V(L)),
$$

so that an area law corresponds to $V(L) = \sigma L$, a linearly rising potential, and a perimeter law to a potential that flattens at large $L$. The first display is Euclidean and the second Minkowski; the next subsection converts between them. These statements are standard, proved on the lattice by the strong-coupling expansion, and cited rather than reproduced; the framework's relation to them is the subject of the ledger below.

### The Information Cost of the Loop

The loop's expectation value is exponentially small in the size of the loop, and its negative logarithm is the natural cost of the configuration: in the Euclidean theory it is the action of the flux that the loop describes, so that for the rectangular loop it equals $T\,V(L)$ — the energy of the separated sources multiplied by the time they are held apart. Define

$$
I(C) := -\log\bigl|\langle W(C)\rangle\bigr| .
$$

The definition reads the decay of the loop's modulus, so it is the **Euclidean** cost: it is taken in the signature in which the perimeter and area laws above hold as written, with real exponents. In Minkowski signature the rectangular loop is $\exp(-iTV(L))$, a pure phase whose modulus is exactly one for real $V(L)$, so the cost as defined would vanish on it identically. The two are related by the analytic continuation $T\to -iT$ (the Minkowski $T$), which turns the phase into the decay and the decay back into the phase. The information cost and the potential are the same quantity read in the two signatures, and the scaling analysis below is made in the Euclidean one.

Then the two laws read

$$
I(C) \simeq \mu_{\mathrm{prm}}\,\mathrm{perim}(C)
\qquad\text{or}\qquad
I(C) \simeq \sigma\,\mathrm{area}(C),
$$

and the two are distinguished not by the size of $I$ but by its **scaling**: the first grows with the length of the loop, the second with the region it encloses. For the rectangular loop,

$$
I(C_{L\times T}) \simeq
\begin{cases}
2\mu_{\mathrm{prm}}(L+T), & \text{perimeter},\\[2pt]
\sigma\,LT, & \text{area},
\end{cases}
$$

so that the quantity $I/T$ at large $T$ is a constant for the perimeter law and grows linearly in $L$ for the area law:

$$
\lim_{T\to\infty}\frac{I(C_{L\times T})}{T}
=
\begin{cases}
2\mu_{\mathrm{prm}}, & \text{perimeter},\\[2pt]
\sigma L, & \text{area}.
\end{cases}
$$

With the area law at unit string tension, $I = LT$, the ratio $I/T$ took the values $1.000$, $2.000$, $4.000$ at $L = 1,2,4$ for both $T = 50$ and $T = 100$, reproducing $\sigma L$ exactly. With the perimeter law at $\mu_{\mathrm{prm}} = 0.5$ per unit length, $I = 0.5\cdot2(L+T)$, the ratio took the values $1.020, 1.040, 1.080$ at $T = 50$ and $1.010, 1.020, 1.040$ at $T = 100$, approaching the constant $2\mu_{\mathrm{prm}} = 1$ as $T$ grows and the $L/T$ correction vanishes. The two behaviours are therefore distinguishable by a single number extracted from the large-$T$ limit of the loop, and that number is either constant in $L$ or proportional to $L$.

Read information-theoretically, the area law says that the cost of maintaining the configuration is proportional to the **area swept** by the separation, not to its boundary. The flux configuration is non-local: the tube stores an amount of information per unit length that does not decay with separation, and the string tension $\sigma$ is the information cost per unit of separation per unit of time. A perimeter law, by contrast, is the behaviour of a short-ranged correlation: the cost is a boundary term and the sources are screened. Confinement is thus the statement that the loop's information cost is **extensive in the enclosed region rather than in its boundary**, and it is the signature that the coloured flux cannot be spread into the vacuum.

## The Parton Labels and Their Loss

### Colour as a Superselected Label

In the partonic description the fundamental fields carry colour: a quark transforms in the fundamental representation $\mathbf{3}$ and a gluon in the adjoint $\mathbf{8}$. In the confined phase the asymptotic observables are colour singlets, and the colour labels are not observable at infinity. The structure is that of a **superselection rule**: the observable algebra at infinity commutes with the colour generators, and two states that differ only by a colour rotation are indistinguishable to it.

This is standard physics and is imported. Two features of it are worth separating, because only one is a loss.

- The **total colour charge** of a physical state vanishes, and the vanishing is a superselection constraint: physical states are colour singlets. This is a restriction on the state space, not an information channel.
- The **individual parton colours** inside a hadron are not labels on the asymptotic state space at all. A hadron is one colour-singlet state; the many partonic configurations that produce it are not distinguishable by any asymptotic observable. This is the non-invertibility, and it is the loss.

The distinction between the two is the distinction between a constraint and a channel, and the information-theoretic content is in the second.

One qualification keeps the model honest. Colour in QCD is a local symmetry, and a rigid colour rotation is the constant member of that local group; on the physical subspace, where the Gauss law is imposed, it acts trivially. The superselection statement above is therefore a statement about the algebra of colour-invariant operators, not about a group of physical rotations. What makes the restriction a loss and not a redundancy is that the partonic configurations a hadron's infrared description cannot separate are not gauge copies of one another: they differ in the momenta and the number of their constituents, and no change of description removes the difference.

The model of the next subsection does not use colour at all. It uses the framework's own internal charge, realized in the informational sector, for which the rotation is a genuine transformation of the algebra and not a redundancy; the framework's own gauge group is the abelian central phase, which conjugates every element trivially, so the two are different transformations and only the first is a loss.

### The Restricted State and the Vanishing Relative Entropy

The superselection statement can be made exact without a colour group, on the framework's own state space, by using the commutant structure that any charge superselection rule produces. Let the charge along the axis $\vec u$ be the Hermitian element $\vec u\cdot\vec S$ of $\mathbb{M}_+$, the generator of *Special Element Conventions*, in the units $\hbar=c=1$ used throughout, so that the charge rotation is rotor conjugation,

$$
\tilde{Ϛ}\;\longmapsto\;U\tilde{Ϛ}\,U^{*},
$$

with $U$ the corpus's rotation rotor about $\vec u$ by $\theta$, a real unit quaternion with $U^{*}=U^{-1}$. The **accessible** state is the restriction of $\tilde{Ϛ}$ to the algebra of observables commuting with the charge; in the quaternion realization this restriction is the dephasing of the Bloch vector along the charge axis,

$$
\vec r \;\longmapsto\; (\vec r\cdot\vec u)\,\vec u,
$$

the projection of the Bloch vector onto the axis, which is the full-dephasing limit of the companion article [Decoherence as Idempotent Projection](decoherence-as-idempotent-projection.html). Two states that differ by a charge rotation have **the same accessible state**:

$$
\boxed{\;\vec r\cdot\vec u = (\mathsf{R}_{\vec u}(\theta)\vec r)\cdot\vec u\;},
$$

because the rotation $\mathsf{R}_{\vec u}(\theta)$ of the Bloch vector induced by conjugation with $U$ preserves the component along $\vec u$. Their full relative entropy is generally positive, but the relative entropy of their accessible restrictions vanishes. The relative entropy is $S(\tilde{Ϛ}_1\|\tilde{Ϛ}_2)=\mathrm{Tr}\,\tilde{Ϛ}_1(\log\tilde{Ϛ}_1-\log\tilde{Ϛ}_2)$, and it was evaluated on explicit states: with $\vec r = (0.5,-0.3,0.4)$ and a charge rotation about $\vec u = (0,0,1)$ by $1.1$ radians, the full relative entropy was $S(\tilde{Ϛ}\|\tilde{Ϛ}_{\mathrm{rot}}) = 0.231562$, while the accessible relative entropy vanished identically, and the two accessible Bloch vectors agreed exactly, both $(0,0,0.4)$.

The lesson is the article's thesis in its sharpest form. A rotation by the framework's charge is not a gauge transformation: it changes the state, and the full relative entropy detects the change. But the change is invisible to the accessible algebra, and the accessible algebra is the whole of what survives to asymptotic observation. The information lost is exactly the component of the state along the unobservable charge directions, and no re-description recovers it.

### Why This Is Loss and Not Redundancy

The contrast with the companion article on gauge redundancy is now exact.

A gauge transformation is implemented by the central phase, which for the framework's gauge group is central and of unit modulus: it therefore fixes the state itself, $\tilde{Ϛ}\mapsto\lambda\tilde{Ϛ}\lambda^{*} = \tilde{Ϛ}$, and not merely its restriction. The two descriptions are two ways of writing one state, and the coincidence is exact rather than a projection. A charge rotation also acts by a $*$-unitary, but the accessible algebra is a **proper subalgebra** — the commutant of the charge — so the rotated state restricts to the same accessible state only because the distinction has been projected out by the restriction, not because it was never there. The map from states to accessible states is many-to-one on a non-trivial fibre, and the fibre is the set of states with the same charge-axis component. That is the structure of a lossy channel, and it is developed in section *Confinement as an Effectively Lossy Channel*.

One more distinction is worth recording. In the gauge case the fibre is a group orbit and a representative recovers the configuration; the locality of the gauge choice is the only obstruction. In the confinement case the fibre contains partonic configurations that no asymptotic operation distinguishes, and the obstruction is the spectrum itself. Redundancy is a property of the description; loss is a property of the theory.

## The Parton Picture Is an Ultraviolet Description

### Resolution and Scale

The parton picture is not a description of a hadron at rest; it is a description at a resolution. The parton distribution functions are functions of the momentum transfer, and the coupling runs: at short distances the colour coupling is weak and the partons are resolved, while at long distances it is strong and the resolution fails. The information-theoretic interpretation is that the partonic information is **ultraviolet data**, and confinement is its infrared fate.

The framework's own renormalization-group article reaches the non-abelian case and reproduces the standard one-loop beta function,

$$
\beta_g = -\frac{g^3}{16\pi^2}b_0,
\qquad
b_0 = \frac{11}{3}C_2(G) - \frac{2}{3}\sum_{\text{Weyl}}T(r),
$$

with $C_2(G) = N$ and the QCD coefficient $b_0 = 11 - \tfrac{2}{3}N_f$ for $SU(3)$. But the article states plainly that the gauge group, the matter content, the action, the measure, and the regulator are **inputs**, and that the beta functions are transcriptions. The flow acts on central scalars, and the algebraically natural sharp cutoff is imposed on the central biquaternion norm $\tilde{P}\tilde{P}^{\natural}$. So the framework houses the form of the flow, and the flow is the coarse-graining that degrades the partonic information, but the group and the matter that give the flow its meaning are the missing objects.

### Coarse-Graining as a Channel

On general grounds the flow from an ultraviolet description to an infrared description is a **completely positive trace-preserving map** between state spaces, and relative entropy is monotone under it:

$$
S\bigl(Ξ(\tilde{Ϛ}_1)\,\big\|\,Ξ(\tilde{Ϛ}_2)\bigr) \;\leq\; S(\tilde{Ϛ}_1\|\tilde{Ϛ}_2).
$$

The inequality is the precise sense in which the flow loses information: two partonic states that were distinguishable at the ultraviolet scale become less distinguishable, or indistinguishable, at the infrared scale. When the image of the map is a proper subalgebra — when distinct states are identified by it, as for the colour-singlet expectation of the next section — the inequality can be strict, and the left side vanishes identically whenever the two states share an image, however distinguishable they were under the full algebra. The restricted relative entropy computed above is exactly that case, and there the loss is total.

The framework's own relative-entropy companion supplies the monotonicity statement; the flow supplies the map; and the confinement statement is that the infrared map has the colour directions in its kernel. What the framework cannot supply is the map itself, because it has no colour and no non-perturbative action.

## Confinement as an Effectively Lossy Channel

### The Colour-Singlet Conditional Expectation

The loss can be modelled by a single map. Let $\mathcal{M}$ be the algebra of observables carrying the colour action and $\mathcal{N}\subset\mathcal{M}$ the colour-neutral subalgebra, the fixed points of the colour rotations. The **conditional expectation** onto the fixed points,

$$
E:\mathcal{M}\to\mathcal{N},
\qquad
E(\tilde{Q}) = \int_{G} dU\;U \tilde{Q} U^{-1},
$$

averaging over the colour group with its normalized Haar measure, is a completely positive unital map that fixes its image: $E\circ E = E$. It is the colour-singlet projection, and it is the natural model of what the asymptotic description retains. Applied to a state, it discards exactly the off-diagonal colour coherences and keeps the colour-neutral content, so that

$$
S\bigl(E(\tilde{Ϛ}_1)\,\big\|\,E(\tilde{Ϛ}_2)\bigr) \;\leq\; S(\tilde{Ϛ}_1\|\tilde{Ϛ}_2),
$$

and the left side vanishes whenever the two states have the same image, so the inequality is strict for any two distinct states that the averaging identifies — in particular for two states related by a colour rotation and not equal. The model has the same screening structure that the companion article on decoherence develops in the informational sector; there, the projection is onto the pointer basis selected by an environment, and here it is onto the colour singlets selected by the spectrum.

### Comparison with Decoherence

The comparison is close and the difference is the reason the article keeps the two words apart.

- **Decoherence** is a dynamical process: an environment entangles with the system, and the off-diagonal coherences of the reduced state decay. The information is not destroyed; it is delocalized into correlations with the environment, and in principle it could be recovered from the whole. The projection is effective, not fundamental.
- **Confinement** is a spectral statement: the coloured states are absent from the asymptotic spectrum, so there is no coloured environment in which the colour could be stored and no larger system from which it could be recovered. The projection is the restriction to what exists asymptotically.

The formal structure — a channel that fixes a subalgebra — is shared, and that is why the decoherence article is the closest written model. The physical content is different: decoherence is the loss of *phase coherence* into an environment, confinement is the absence of the *labels* from the spectrum. The first is a relocation to an inaccessible but existing sector; the second is a loss with no such sector. The article on the Higgs mechanism treats the third case, in which what is removed is a gauge coordinate rather than a physical degree of freedom, so that the removal is a reversible re-encoding rather than a loss.

## The Mass Gap and the Correlation Length

### Confinement as a Gap

Confinement is tied to a **mass gap**. In the lattice formulation the area law implies one — the Osterwalder–Seiler result, cited as standard, is that a theory whose loops obey an area law has no massless excitation — and the link is natural: a massless coloured state would be an unconfined long-range colour field, and a gap says that no such massless carrier exists, so the colour force is transmitted only over a finite range. Both statements are part of the standard lattice confinement analysis, cited rather than derived.

The gap is where the information-theoretic interpretation becomes a statement about **correlations**. Let $O$ be a local operator of the colour-singlet sector — a glueball operator, in standard language. Its connected two-point function decays at long distance at the rate set by the lightest intermediate state,

$$
\bigl\langle O(x)O(y)\bigr\rangle_{c} \;\sim\; \exp(-m|x-y|) \quad\text{as } |x-y|\to\infty,
$$

with $m$ the lightest mass, so that the **correlation length** is $\zeta = 1/m$. Beyond $\zeta$ even the colour-singlet correlations are lost: a local measurement cannot learn the configuration of a distant source, and the information that survives at long distance is the global one — the string between the sources. An operator that carries colour explicitly is the one dressed by a Wilson line, and its long-distance behaviour is the area law of the previous section, a decay governed by the string tension rather than by $m$; the exponential above is the gap's statement about the singlet sector, and the area law is the confining statement about the coloured one.

### The Two Ways Information Fails to Propagate

The gap and the area law are two faces of the same loss and it is worth stating how they differ.

- The **area law** is a statement about the *energy* of a configuration of separated sources: it grows with their separation, so the sources cannot be pulled apart.
- The **gap** is a statement about the *decay of correlations*: the colour-singlet sector is correlated only over a finite distance.

Both say that the confined theory has no long-range carrier: the first, that separating colour sources costs an energy growing without bound; the second, that correlations die off beyond the correlation length — the colour-singlet ones included.

The information-theoretic interpretation of the second is a statement about the **scale at which a source can be read at all**. A colour-singlet operator's connected correlator is the object whose long-distance decay defines $\zeta$, so $\zeta$ is the distance beyond which no local measurement retains information about a distant source: the correlation is the measurable proxy for distinguishability, and its exponential decay is what a loss statement can be built on without further assumption.

It is worth being exact about what is not claimed. Whether the relative entropy between two configurations differing in a distant colour measurement inherits precisely the scale $\zeta$ is a question this article does not settle. Pinsker's bound, $S(\rho\|\sigma)\ge\tfrac12\|\rho-\sigma\|_1^{2}$, runs from the relative entropy down to the trace distance: a small relative entropy forces the two states to be close in trace distance, hence hard to distinguish by any observable. It says nothing about which observable distinguishes two states whose relative entropy is large, and in particular nothing about locality. It is the converse direction — small local correlators forcing a small relative entropy — that the scale statement would need, and that direction holds only with a bound running the other way, under regularity conditions on the states that the framework does not supply. What is safe, and is the sharpest form of the loss available here, is the qualitative contrast: in the confined phase the correlations that could carry a colour distinction die off exponentially and the label is absent from the spectrum altogether, whereas in an unconfined phase whose gauge field stays massless — the Coulomb phase of QED is the standard instance — the long-range field does carry the charge to infinity, and the correlations decay only as a power. The framework has no mass gap and no derived correlation length; the statement is carried as standard physics.

## The Biquaternion Framework: What It Can and Cannot State

### The Loop in the Two Sectors

The order parameter is the framework's own construction. The connection integrated along the curve is a material one-form, $\tilde{A}\in\mathbb{M}_-$; the group element it exponentiates into is an element of the informational realization of the gauge group; and the trace is twice the scalar part. The loop is therefore an $\mathbb{M}_+$ trace of an object whose logarithm lies in $\mathbb{M}_-$, and its gauge invariance is the invariance of the scalar part under the adjoint action. The small-loop expansion, $W = 1 + i\ell^2F_{\mu\nu} + O(\ell^4)$ for a loop of area $\ell^2$ in the $\mu\nu$ plane, and the centrality of $\tilde{F}^2$, whose two scalar parts are the two Lorentz invariants of the field strength, are established in the Wilson-loop companion and are not repeated. What this gives the present article is a place to put the order parameter and, consequently, a place to put the information-theoretic interpretation of its two laws.

### The Ceiling: No Colour

What the framework cannot supply is the colour theory whose order parameter the loop is supposed to be. The compact group available inside $\mathbb{B}$ is the maximal compact subgroup of $\mathrm{GL}(2,\mathbb{C})$, namely

$$
\mathrm{U}(2) = \bigl(\mathrm{U}(1)\times\mathrm{SU}(2)\bigr)/\mathbb{Z}_2,
\qquad \mathfrak{u}(2)=\mathfrak{u}(1)\oplus\mathfrak{su}(2),
\qquad \dim_\mathbb{R} = 4 ,
$$

and the matter side has the matching ceiling: $\mathbb{B}$ is simple, with a unique simple module of complex dimension two, so every $\mathbb{B}$-module has complex dimension $2k$ and a three-dimensional colour module does not exist. No $\mathrm{SU}(3)$ subgroup and no colour triplet are available on the present construction. The consequence for this article is direct: the partonic information whose loss confinement describes is not present in the framework at all, so the framework's own loss statement is at best the corresponding statement for a $\mathrm{U}(2)$ theory, which is not QCD. The area law, the string tension, the flux tube, the mass gap, and the colour-singlet structure are imports.

This is exactly the position the QCD agenda records, and the information-theoretic interpretation does not change it. It sharpens it: the loss of partonic information is a statement about which labels the asymptotic algebra contains, and the framework's asymptotic algebra — whatever it is — is built on a carrier that has no colour labels to lose.

## The Other Confinement Picture: A Linear Boundary Condition

The negative result above concerns **colour** confinement, and it stands: the order parameter is a loop and the mechanism sought is a non-perturbative property of the colour gauge field, and the framework has neither. There is, however, a second and older picture of confinement, and it is a different kind of object. In the **bag model** the hadron is a bounded region $\Omega$ and the coloured field is required to obey a **linear boundary condition** on $\partial\Omega$ — a ban on the flow of the field through the surface — instead of being held by a non-perturbative loop mechanism. The bag does not derive an area law and does not derive $\mathrm{SU}(3)$; it *assumes* the confining region and asks which fields can live inside it. What it produces is a boundary-value problem, and a boundary-value problem is an object the biquaternion algebra carries natively.

### Two Dirac Equations

Two biquaternionic forms of the massive Dirac equation are in play here, and they must not be read as one.

**The one-sided pair.** The corpus's equation is the chiral pair on the element-valued field,

$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=m\tilde{Ξ}_{\mathrm{sp},L},
\qquad
\tilde\nabla^\natural\tilde{Ξ}_{\mathrm{sp},L}=m\tilde{Ξ}_{\mathrm{sp},R},
$$

Both equations act from the left, and the mass is the off-diagonal pairing of the two halves. The two subscripts are the two values of the chirality: $\tilde{Ξ}_{\mathrm{sp},L}$ carries the $L$ value and $\tilde{Ξ}_{\mathrm{sp},R}$ the $R$ value, read from the element and the declared frame and fixed in *Special Element Conventions*, §*The Chirality Convention*. At $m=0$ the pair decouples into

$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=0,
\qquad
\tilde\nabla^\natural\tilde{Ξ}_{\mathrm{sp},L}=0,
$$

one equation per chirality; the second is the conjugate of the first, and the subscripts $R$ and $L$ name the chirality and not a side of multiplication.

**The two-sided form.** The bag uses Kravchenko's dictionary. A real-linear bijection $A$ carries the source's four-component field $Ξ$ to a biquaternion-valued function $F=A[Ξ]$, under which the Dirac equation becomes the single equation

$$
\mathcal NF=\left(i\frac{\partial}{\partial r'_t}+D_3\right)F-mi\,\overline{F}\,\vec e_z=0,
\qquad
D_3=\sum_{k=1}^{3}\vec e_k\frac{\partial}{\partial R_k}.
$$

Since $i\partial/\partial r'_t=-\partial/\partial R_t$ on the material sector in the natural units $\hbar=c=1$, the same operator reads

$$
\mathcal NF=-\tilde\nabla^\natural F-mi\,\overline{F}\,\vec e_z=0 .
$$

The derivative part acts from the left, the mass part from the right through $\vec e_z$, and the bar is the componentwise complex conjugation. One operator, three kinds of action: that mixture is what *two-sided* names. The mass is a conjugation together with a direction, not a scalar multiple of the field, and the equation is therefore not of the form $\tilde\nabla\tilde{Ξ}_{\mathrm{sp}}=\mu\tilde{Ξ}_{\mathrm{sp}}$ for any linear mass term of the algebra. The chiral pair and $\mathcal N$ are related by the dictionary, and they are not the same operator: the pair is the corpus's own equation, and $\mathcal N$ is the source's. The dictionary, the signs of $A$ and the line-by-line comparison of the two equations are set out in *The Dirac Equation in Biquaternionic Form*; what the bag adds is the boundary.

### The Linear Bag Model

Let $\vec q=r_x\vec e_x+r_y\vec e_y+r_z\vec e_z$, and let $Ξ$ be the source's four-component field, taken time-harmonic,

$$
Ξ(r'_t,\vec q)=Ξ_\omega(\vec q)\,e^{\,i\omega r'_t},
$$

obeying the massive Dirac equation in a bounded domain $\Omega$, with $\partial\Omega$ a closed Liapunov surface. The source writes that equation in its own frame; in the conventions it is the two-sided $\mathcal NF=0$ of the previous subsection, and its derivative part is the gradient alone. The source's time term, with its two imaginary factors, is the $e_t$ term of $\tilde\nabla$ read on the material sector, where the time derivative carries the $i$, so $i\partial/\partial r'_t=-\partial/\partial R_t$ and the free part is $-\tilde\nabla^\natural$. The spatial derivative is the sum $\sum_k\vec e_k\,\partial/\partial R_k$ that $\tilde\nabla$ carries, acting from the left. The mass is the conjugation together with the direction $-\vec e_z$, and it does not commute with the phase, $\overline{Ξ_\omega e^{i\omega r'_t}}=\overline{Ξ_\omega}\,e^{-i\omega r'_t}$. The amplitude is therefore taken on the complex-linear operator that the reduction below produces, and not on $\mathcal N$ directly; that is why the source reduces before he applies the ansatz.

The confinement of the field to $\Omega$ is a **linear boundary condition**: a fixed value for the field's direction along the outward normal, which forbids the flow of the particle through the surface. Translated from the source's frame, the condition is the action of the element $\sum_k u_k\vec e_k$,

$$
\left(\sum_{k=1}^{3}u_k\,\vec e_k\right)Ξ_\omega(\vec q)=i\,Ξ_\omega(\vec q)
\qquad(\vec q\in\partial\Omega),
$$

where $\vec u$ is the unit outward normal. The source's operator carried a constant right factor beside the left one; no right factor is carried here, because the dictionary's spatial coefficient is left multiplication by $\vec e_k$ — the same coefficient that carries the spatial derivative in $\mathcal N$ above — and not a left factor times a fixed right one. For a unit normal the element squares to $-e_t$, so the condition is carried by the element $P_{\vec u}=\tfrac12\bigl(e_t-i\sum_k u_k\vec e_k\bigr)$, which reads $Ξ_\omega=P_{\vec u}Ξ_\omega$: one half of the field is kept at the surface and one half is removed, and that removal is the ban on the flow. The equation and the condition together are the **linear bag model**, and the question they pose is a boundary-value question: for which boundary data $Ξ_\omega$ on $\partial\Omega$ does the pair have a solution, and is the associated integral operator invertible or Fredholm?

### The Biquaternionic Reduction

The reduction of the model to the algebra is due to V. V. Kravchenko (1995), and its steps are worth separating, because each is a place where the framework's own objects do the work. Four letters of the source are operators and not elements, and they are flagged once here: $u^{\pm}$ are the two halves of the change of variables, acting on the pair (field, conjugate); $S^{\pm}$, $S_\alpha$ and $K_\alpha$ are operators on the module, the first two selecting a part of the boundary data and the third an integral operator; and $P_\alpha=\tfrac12(I+S_\alpha)$ is an operator, with $I$ the identity operator. None of them is an element of the algebra, and none of them is written as one.

**A real-linear bijection of the source's module onto the algebra.** There is a bijection $A$ from the source's four-component functions $Ξ: G\subset\mathbb{R}^4 \to \mathbb{C}^4$ onto biquaternion-valued functions $F = A[Ξ]$, and it is $\mathbb{R}$-linear and not $\mathbb{C}$-linear: the central imaginary of the source's field becomes a right action of the algebra,

$$
A(iΞ) = -A(Ξ)\,\vec e_z ,
$$

that is $\tilde{Ξ}_{\mathrm{sp}}\mapsto-\tilde{Ξ}_{\mathrm{sp}}\vec e_z$ on the image. The dictionary has a second ingredient, the coefficient conjugation, which is not an operation of the algebra and which the equation carries in its mass term. Here $\overline{\cdot}$ is the componentwise complex conjugation — the corpus's bar, distinct from the Hermitian star $^{*}$ and from the algebra's real structure $\flat$. The equation consequently carries the mass term $-mi\,\overline{F}\,\vec e_z$, and that antilinear factor is the price of the dictionary. The dictionary is set out in *The Dirac Equation in Biquaternionic Form*, where the conjugation it uses is distinguished from both $\flat$ and $^{*}$.

**Removal of the conjugation operator.** Because the bar is antilinear, $\mathcal N$ is not a left multiplier, and the boundary-value machinery of the algebra — the Cauchy kernel, the Teodorescu transform, the Cauchy-type operator — does not apply to it directly. Splitting $\mathcal N$ into its two halves, with the bar in the off-diagonal places, turns the single antilinear equation into a coupled pair of **complex-linear** equations, one for the field and one for its conjugate. The two halves add to the whole, and their difference is the right action $M_{i\vec e_x}$, with $M_b:\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{Ξ}_{\mathrm{sp}} b$; adding and subtracting the two equations therefore reduces the pair to one complex-linear operator:

$$
R = D_3 + i\frac{\partial}{\partial r'_t}\,M_{i\vec e_x} - m M_{\vec e_y}
= D_3 - \frac{\partial}{\partial r'_t}M_{\vec e_x} - m M_{\vec e_y},
\qquad
\mathcal N = u^{+}Ru^{-},
$$

where the single step $i\cdot i=-1$ is the only place that the central imaginary enters, and it cancels: $R$ has no complex coefficient. The factors $u^{\pm}$ are the two halves of that change of variables, and they carry the bar; it has been moved off the operator and onto the field.

For a time-harmonic field the equation reduces, after that change of variables, to the **shifted Moisil–Teodoresco equation** with the source's parameter,

$$
D_\alpha \tilde{p} = 0, \qquad \alpha = -(i\omega \vec e_x + m \vec e_y)\in\mathbb{B},
\qquad D_\alpha = D + M_\alpha ,
$$

with $D=iD_3=i\sum_{k=1}^{3}\vec e_k\,\partial/\partial R_k$ ($D^2=\Delta$) and $M_\alpha$ the right action $f\mapsto f\alpha$. A direct reduction of $R$ gives $\alpha'=\omega\vec e_x-im\vec e_y=i\alpha$. The operators $D_{\alpha'}$ and $D_\alpha$ are not the same, but their degeneracy loci are, since $\langle i\alpha\rangle_{\natural}=-\langle\alpha\rangle_{\natural}$, so the mass-shell statement is unchanged. The source writes $\alpha$, and that normalization is kept below. So the massive time-harmonic Dirac field is, after one change of variables, an $\alpha$-hyperholomorphic biquaternionic function, and the whole boundary-value theory of $D_\alpha$ — the Borel–Pompeiu formula, the Cauchy integral formula, the Plemelj–Sokhotski formulas, the Cauchy integral theorem, the Morera theorem and the boundary-value criterion — becomes available to the bag.

### The Mass Shell Is the Zero-Divisor Condition

The parameter of the reduced equation is not a wave number but an element of the algebra. It has neither a scalar part nor an $\vec e_z$ component, $\alpha_t=\alpha_z=0$, so its quaternionic norm has two terms and gives the mass-shell relation,

$$
\boxed{\;\langle \alpha\rangle_{\natural} = \alpha_x^{2}+\alpha_y^{2} = (-i\omega)^2+(-m)^2 = -\omega^2+m^2 = m^2 - \omega^2\;},
$$

where $(-i\omega)^2=i^2\omega^2=-\omega^2$ uses $i^2=-1$. For an element with no scalar part the algebra square is minus the natural norm, $Q^2=-\langle Q\rangle_{\natural}e_t$, as *Product and Form Conventions* records; hence

$$
\alpha^{2}=(\omega^2-m^2)e_t .
$$

The element $\alpha$ is therefore a **nilpotent**, $\alpha^2=0$, exactly where its natural norm vanishes, and the boxed relation above and this one are the same condition read twice: the mass shell is where the parameter of the shifted equation loses its inverse. The zero-divisor set of the algebra is

$$
\mathcal Z=\{\tilde Q\neq0:\langle\tilde Q\rangle_{\natural}=0\},
$$

and the statement reads

$$
\alpha\in\mathcal Z \iff \omega^2 = m^2 ,
$$

with the origin $\omega=m=0$ excluded: it is the apex of the cone and is not a zero divisor.

This is the meeting point of the algebra's degeneracy and the physics of the mass shell: the parameter $\alpha$ has no inverse exactly where the bag's frequency is on shell. It also places the bag systematically: the Teodorescu transform $T_\alpha$ (not the generators $T_a$ of the notation table) and the Cauchy-type operator $K_\alpha$ are defined for every $\alpha\in\mathbb{B}$, but with different formulas on the three branches — $\alpha\notin\mathcal Z$, $\alpha\in\mathcal Z$ with $\alpha_t\neq0$, and $\alpha\in\mathcal Z$ with $\alpha_t = 0$ — and the bag's parameter has $\alpha_t = 0$ and lies in the last of the three. The mass shell is thus not an obstruction but the branch on which the algebra is richest (*N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*, *Zero Divisors as a Physical Locus in Biquaternionic Form*). It is also the point at which this framework's shift meets the scalar Helmholtz shift of *Electromagnetism in Media: The Local Complex Structure at Work*. For a scalar parameter, $D_\alpha = iD_3 + M_\alpha = i\,(D_3 + M_{-i\alpha})$ with $D_3 = \sum_k \vec e_k\,\partial/\partial R_k$, so the framework's operator is $i$ times the source's $D_{3,\beta} = D_3 + M_\beta$ evaluated at $\beta = -i\alpha$. The bag's parameter is not scalar, so the relation to the Helmholtz operator is formal only, and the genuinely non-scalar case is the one the bag needs.

### The Bag Condition Becomes a Boundary Equation

The confinement condition transforms along with the field. In the algebra it becomes a linear condition on the reduced field,

$$
S^-\tilde{p} = 0 \ \text{ on } \partial\Omega, \qquad\text{equivalently}\qquad \tilde{p} = S^+\tilde{p},
$$

where $S^\pm$ are the two complementary operators of the module — operators, not elements of the algebra — assembled from the boundary normal and a fixed unit direction. The bag model then meets the boundary-value theory of $D_\alpha$, which supplies a criterion: a Hölder function on $\partial\Omega$ is the boundary value of a $D_\alpha$-regular function in $\Omega$ if and only if $P_\alpha f = f$, where $P_\alpha = \tfrac12(I + S_\alpha)$ and $S_\alpha$ is the operator of singular integration with the biquaternionic parameter, built from the Cauchy-type operator $K_\alpha$. Combined with that criterion, the bag model reduces to the single boundary equation. There the criterion's $P_\alpha$ and the bag's $S^+$ coincide on the boundary data the model admits; that coincidence is the source's result, not an identity of the two constructions in general,

$$
\boxed{\;\tilde{p} = P_\alpha\tilde{p} = S^+\tilde{p} \qquad \text{on } \partial\Omega\;}.
$$

That is the shape of the result: a linear bag model becomes a **boundary singular integral equation** for the biquaternionic operator $D_\alpha$, and the solvability and Fredholmness of the bag become properties of that equation. The framework supplies the reduction, the function theory that makes the criterion available, and the place to ask the Fredholm question.

### What This Changes, and What It Does Not

**What it changes.** The QCD agenda's statement that "no mechanism has been proposed" is about the colour mechanism, and it stands: nothing here derives an area law, a string tension or a mass gap. But the framework's ledger on confinement must distinguish the two pictures rather than treat confinement as a single absent object. The loop criterion is a statement about a gauge-field expectation value, and the framework can place the loop but cannot evaluate it. The bag condition is a **boundary condition on a matter field**, and that is a boundary-value problem, which the framework can both state and attack with its own function theory. So the corpus can say something sharper than "no mechanism has been proposed": the confinement picture that is a boundary condition is housed, and the confinement picture that is a non-perturbative gauge dynamics is not.

**What it does not change.** The bag model is not a colour theory either. It assumes the confining region instead of deriving it, it fixes no colour group, and it yields no area law; only the boundary-value theory is the framework's. The colour ceiling stands, the bag's fields are a $\mathrm{U}(2)$-like transcription, and the model itself — the linear boundary condition, the confining region, the hadron as a bounded domain — is imported from nuclear physics. The honest placement is that the algebra houses the **boundary-value problem** that one confinement picture poses, and the QCD agenda's obstacle remains for the other.

## What the Algebra Supplies, Transcribes, and Does Not Supply

**Supplied by the algebra, and recomputed here.** The Wilson loop as a two-sector bilinear: a material-sector connection integrated along a curve, exponentiated into the informational realization of the group, traced to a gauge-invariant number. The information-theoretic interpretation of the two laws, with the scaling of $I(C) = -\log|\langle W(C)\rangle|$ recomputed: $I/T\to$ constant for the perimeter law and $I/T\to\sigma L$ for the area law, in both cases to the stated accuracy. The superselection structure of a charge rotation on the informational sector, with the accessible state as the dephasing along the charge axis and the accessible relative entropy vanishing while the full relative entropy is positive — recomputed on explicit states. The conditional expectation onto the charge-neutral subalgebra as a channel that fixes its image — realized on the framework's own compact algebra $\mathrm{SU}(2)\subset\mathbb{M}_+$, the group whose singlets the framework's own superselection analysis selects, and only transcribed for a colour group — and the monotonicity of relative entropy under it, cited from the companion articles. And, in the bag picture, the boundary-value theory of the shifted operator $D_\alpha$: the Borel–Pompeiu formula, the Cauchy integral formula, the Plemelj–Sokhotski formulas and the boundary-value criterion, with the reduction of the linear bag model to the boundary equation $\tilde{p} = P_\alpha\tilde{p} = S^+\tilde{p}$ — the reduction and the criterion are the source's, the algebra they use is the corpus's, and the three algebraic facts the reduction rests on (the two halves of the right action, which add to the whole and differ by $M_{i\vec e_x}$, the collapse $i\cdot i=-1$ that makes $R$ real, and the identity $\langle \alpha\rangle_{\natural} = m^2-\omega^2$) were recomputed here.

**Transcribed from standard physics.** Confinement itself: the area law as the criterion, the flux tube, the linearly rising potential, the string tension, the lattice strong-coupling argument that establishes the area law, the mass gap, the colour group and its representations, the partonic description and its scale dependence, and the running of the colour coupling. The bag model is transcribed too: the confining region, the hadron as a bounded domain, and the linear boundary condition that bans the flow through its surface are imports from nuclear physics, and the model derives neither an area law nor a colour group. The colour-singlet structure of the asymptotic algebra and the superselection of colour are standard. All of these are imports and are flagged as such throughout.

**Not supplied.** The colour group, the confinement mechanism, the area law, the string tension, the mass gap, the non-perturbative biquaternionic action, measure and gauge-invariant regulator, and any empirical consequence. The bag picture supplies the boundary-value problem, not the confining dynamics: it assumes the region and does not explain it, and it is not a colour theory. The framework states the order parameter and the informational language, and in the bag picture it states a boundary equation; it does not derive the physics that gives them their QCD meaning. The honest summary is the QCD agenda's: the gauge-dynamical confinement mechanism is an obstacle with no route yet.

**Companion articles.** The construction rests on the following written articles of the series.

- Companion article *Wilson Loops in Biquaternionic Form*, for the holonomy, the loop as a two-sector bilinear, the perimeter and area laws, and the small-loop expansion.
- Companion article *Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda*, for the ceiling on the compact gauge algebra, the absence of a colour group and a colour triplet, and the no-route status of confinement.
- Companion article *The Renormalization Group in Biquaternionic Form*, for the one-loop running and the statement that the group, matter, action, measure and regulator are inputs.
- Companion article *Decoherence as Idempotent Projection*, for the channel model of a loss onto a subalgebra and the full-dephasing limit.
- Companion article *Relative Entropy and the Biquaternion Framework*, for the relative entropy and its monotonicity under completely positive maps.
- Companion article *Non-Abelian Gauge Fields in Biquaternionic Form*, for the non-abelian connection and the generators realized in the informational sector.
- Companion article *Chiral Fermions in the Biquaternion Framework*, for the chiral structure of the module and the vector-like character of the framework's gauge group.
- Companion article *Gauge Redundancy and the Information in the Gauge Orbit in Biquaternionic Form*, for the redundancy case against which this article's loss is defined.
- Companion article *The Higgs Mechanism as an Erasure of Information in Biquaternionic Form*, for the relocation case against which this article's loss is defined.
- Companion article *The Dirac Equation in Biquaternionic Form*, for the spin–biquaternion dictionary of the bag model, and in particular for the distinction between the componentwise complex conjugation $\overline{\cdot}$ that the mass term carries and the algebra's real structure $\flat$.
- Companion article *Biquaternion Regular Functions*, for the shifted operator $D_\alpha$, the boundary-value criterion $P_\alpha f = f$, and the function theory the bag reduction uses.
- Companion article *N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*, for the zero-divisor set $\mathcal Z$ and the fact that the bag's parameter $\alpha$ lies in it exactly on the mass shell.
- Companion article *Electromagnetism in Media: The Local Complex Structure at Work*, for the scalar Helmholtz shift $D_{3,\alpha}=D_3+M_\alpha$, of which the bag's $D_\alpha$ is the non-scalar case.

## Open Questions

1. **A sector-theoretic order parameter.** The confinement transition is a change in the long-distance behaviour of $\langle W(C)\rangle$. Is there a biquaternionic order parameter — an element of the algebra whose norm or scalar part measures the transition, rather than a functional of loops — and does the transition appear as a change in a property of the algebra's own objects? The Wilson-loop companion records the same question.

2. **The information budget of the flux tube.** The string tension is the cost per unit length of the tube. Is there a framework-internal object whose entropy density is $\sigma$, in the way the series' *Black Hole Thermodynamics in Biquaternionic Form* relates an entropy to a horizon area? No such object is known.

3. **Can the loss be made a theorem?** On the framework's carrier the accessible algebra is a commutant of a charge, and the restricted relative entropy vanishes. Is there a general statement — an algebraic theorem about conditional expectations that fix their image and about their fibres — that would state the loss without importing colour, and that would apply to whatever gauge theory the framework eventually carries?

4. **The regulator and the loss.** The loss is a statement about the infrared. The framework's regulators are sector-blind and its sharp cutoff breaks gauge invariance. Does a gauge-invariant regulator within the algebra change the information-theoretic picture, and is there a renormalization of the restricted relative entropy?

5. **The relation to the Reeh–Schlieder statements.** The local algebra of a region is large: by Reeh–Schlieder it is cyclic and separating for the vacuum and contains operators of every particle number. The confinement loss is nevertheless a statement about the asymptotic algebra. How the two coexist — a large local algebra and a small asymptotic one — is the structural question, and the framework's infinite-dimensional module algebra is the setting for it.

6. **Empirical content.** As everywhere, whether any of this yields a prediction distinguishing the framework from standard QCD. Since the colour group, matter content, coupling, and confinement mechanism are all imports, no such prediction is in view.

7. **The Fredholm question for the bag.** The bag model reduces to the boundary equation $\tilde{p} = P_\alpha\tilde{p} = S^+\tilde{p}$ on $\partial\Omega$, so its solvability is the invertibility or the Fredholmness of the singular integral operator with symbol built from $S_\alpha$ and $S^+$. Is that Fredholm index computable within the algebra — and does the index carry any physical content, such as a count of the confined modes — or does it reduce to the index of the corresponding classical boundary problem? The source poses the systematic Fredholm theory as the next step and does not compute it.

8. **The zero-divisor branch.** The bag's parameter $\alpha$ lies in the zero-divisor set $\mathcal Z$ exactly on the mass shell, so the relevant branch of $T_\alpha$ and $K_\alpha$ is the one where the parameter has no inverse. Does the on-shell degeneracy of the shift have an interpretation of its own — the mass shell as a locus where the function theory changes character — or is it only the algebraic form of the dispersion relation? The zero-divisor articles treat the cone as a physical locus for a *field*; here it is the *parameter* that is singular, which is a different interpretation.

## Summary

Confinement is the absence of the coloured degrees of freedom from the asymptotic spectrum, diagnosed by the Wilson loop: a perimeter law for a screened phase and an area law for a confining one, with the rectangular loop giving the static potential. In the biquaternion framework the loop is a two-sector bilinear — a material-sector connection integrated around a curve, exponentiated into the informational realization of the gauge group, and traced to a gauge-invariant number — so the order parameter is housed exactly.

The information-theoretic interpretation is that confinement is a **loss** of partonic information, in contrast with the redundancy of the gauge orbit. The loop's information cost $I(C) = -\log|\langle W(C)\rangle|$ scales with the perimeter in a screened phase and with the area in a confining one; for the rectangular loop, $I/T$ tends to a constant for the perimeter law and to $\sigma L$ for the area law, and both were recomputed to the stated accuracy. The string tension is the information cost per unit separation per unit time, and the area scaling is the signature that the coloured flux cannot spread into the vacuum.

The loss of the partonic labels is a superselection statement, and the framework's model of it uses its own charge. A rotation by that charge is not a gauge transformation: it changes the state, and the full relative entropy detects the change. But the accessible algebra is the commutant of the charge, and the charge-rotated states restrict to the same accessible state, whose relative entropy vanishes. The map from states to accessible states is many-to-one on a non-trivial fibre, which makes it a lossy channel; the conditional expectation onto the colour-neutral subalgebra is a screening model of it, and the decoherence article is the closest written model while differing in that decoherence delocalizes information into an environment and confinement has no such environment.

What the framework cannot supply is the colour theory itself. The compact algebra inside $\mathbb{B}$ is at most $\mathrm{U}(2)$ of dimension $4$, every $\mathbb{B}$-module has even complex dimension, and a colour triplet and a gluon octet do not exist on the present construction. The area law, string tension, flux tube, mass gap, and colour-singlet structure are therefore imports, and the framework's contribution is the carrier of the order parameter and the informational language of the loss, not the physics of confinement.

The two confinement pictures must be kept apart, and the framework houses one of them. The non-perturbative gauge-dynamics picture is the one the QCD agenda rules out: a loop expectation value, an area law, a string tension and a mass gap, none of which the framework can derive.

The **bag** picture is different in kind. Two Dirac equations are kept apart there: the one-sided chiral pair, whose subscripts $L$ and $R$ are the two values of the chirality and whose mass is the off-diagonal pairing, and the two-sided operator $\mathcal N$, whose mass term is a complex conjugation together with a direction. The picture is a bounded region and a **linear boundary condition**, $\bigl(\sum_k u_k\vec e_k\bigr)Ξ_\omega = iΞ_\omega$ on the surface, which bans the flow of the field out of the region.

That condition is a boundary-value problem, and it was reduced to the algebra by Kravchenko (1995). A real-linear bijection carries the source's four-component field to a biquaternion; the mass term carries the componentwise complex conjugation $\overline{\cdot}$; factoring the equation removes it; the time-harmonic amplitude obeys $D_\alpha\tilde{p}=0$ with $\alpha = -(i\omega \vec e_x + m \vec e_y)$; the bag condition becomes the boundary condition $S^-\tilde{p}=0$; and the boundary-value criterion for $D_\alpha$ turns the model into the single boundary equation $\tilde{p} = P_\alpha\tilde{p} = S^+\tilde{p}$ on $\partial\Omega$.

What the framework supplies here is the function theory, the reduction and the Fredholm question; what it still does not supply is the confining dynamics, since the bag assumes the region rather than explaining it. The three facts the reduction leans on were recomputed: the two halves of the right action are complementary, the step $i\cdot i=-1$ leaves $R=D_3-\partial M_{\vec e_x}/\partial r'_t-mM_{\vec e_y}$ free of complex coefficients, and $\langle \alpha\rangle_{\natural} = m^2-\omega^2$, so the parameter of the reduced bag equation lies in the **zero-divisor set $\mathcal Z$ exactly on the mass shell**.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra of *Algebra and Element Conventions* |
| $e_t, \vec e_x, \vec e_y, \vec e_z$ | The coefficient basis; the structure constants are those of *Algebra and Element Conventions* |
| $i$ | The central scalar imaginary |
| $\tilde\nabla$, $\tilde\nabla^\natural$, $\Box$ | The gradient, its quaternion conjugate and the d'Alembertian, *Operator and Calculus Conventions* |
| $\mathbb{M}_+, \mathbb{M}_-$ | Informational and material sectors |
| $\tilde{A} = \sum_\mu A_\mu e_\mu\in\mathbb{M}_-$ | Gauge connection (material sector) |
| $T_a = i\vec e_a\in\mathbb{M}_+$ | Generators realized in the informational sector |
| $U(C) = \mathcal{P}\exp(i\oint_C \sum_\mu\varepsilon_\mu A_\mu dx_\mu)$ | Holonomy |
| $W(C) = \mathrm{Tr}\,U(C)$ | Wilson loop; order parameter |
| $\langle W(C)\rangle \sim \exp(-\mu_{\mathrm{prm}}\,\mathrm{perim})$ | Perimeter law (screening) |
| $\langle W(C)\rangle \sim \exp(-\sigma\,\mathrm{area})$ | Area law (confinement) |
| $\mu_{\mathrm{prm}}$ | Perimeter coefficient |
| $\sigma$ | String tension |
| $C_{L\times T}$, $V(L)$ | Rectangular loop; static potential; $\langle W\rangle\sim \exp(-iTV(L))$ |
| $I(C) = -\log|\langle W(C)\rangle|$ | Information cost of the loop |
| $\tilde{Ϛ}$, $\vec r$ | State of the informational sector and its Bloch vector, *Algebra and Element Conventions* |
| $\vec r\cdot\vec u$ | Component along the charge axis; accessible content |
| $\vec u\cdot\vec S$, $U$ | Charge along the axis $\vec u$ and its rotation rotor, $U^{*}=U^{-1}$ |
| $S(\tilde{Ϛ}_1\|\tilde{Ϛ}_2)$ | Relative entropy; monotone under channels |
| $E(\tilde{Q}) = \int_G dU\, U\tilde{Q}U^{-1}$ | Colour-singlet conditional expectation; a channel that fixes its image |
| $\beta_g = -(g^3/16\pi^2)b_0$, $b_0 = 11 - \tfrac{2}{3}N_f$ | One-loop running (transcribed) |
| $\mathrm{Tr}$ | The trace, twice the scalar part, *Norm and Pairing Conventions* |
| $\mathrm{U}(2)$, $\mathfrak{u}(2)=\mathfrak{u}(1)\oplus\mathfrak{su}(2)$, $\dim_\mathbb{R} = 4$ | Ceiling on the framework's compact gauge algebra |
| $A$ | Real-linear bijection from the source's four-component functions to biquaternion-valued functions (bag model) |
| $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde\nabla^\natural\tilde{Ξ}_{\mathrm{sp},L}=m\tilde{Ξ}_{\mathrm{sp},R}$ | One-sided Dirac pair; the subscripts $L$ and $R$ are the two values of the chirality |
| $D_3=\sum_k\vec e_k\partial/\partial R_k$, $D_3^2=-\Delta$ | Spatial Dirac operator of the dictionary |
| $\mathcal{N}F=(i\partial/\partial r'_t+D_3)F-mi\,\overline{F}\,\vec e_z$ | Two-sided Dirac operator; the bar is the conjugation in the mass term |
| $\overline{\cdot}$ | Componentwise complex conjugation; the mass term's antilinear factor |
| $R=D_3-\partial M_{\vec e_x}/\partial r'_t-mM_{\vec e_y}$, $\mathcal{N}=u^{+}Ru^{-}$ | Conjugation-free operator, after $i\cdot i=-1$; $u^{\pm}$ are the two halves of the change of variables |
| $\vec q$ | Position in the bag domain |
| $D_\alpha = D + M_\alpha$, $D = i\sum_k \vec e_k\,\partial/\partial R_k$ | Shifted Moisil–Teodoresco operator; $M_b$ is the right action $f\mapsto fb$ |
| $\alpha = -(i\omega \vec e_x + m \vec e_y)$ | Bag parameter; $\alpha\in\mathcal Z \iff \omega^2 = m^2$ |
| $\mathcal Z = \{\tilde Q\neq0 : \langle\tilde Q\rangle_{\natural}=0\}$ | Zero-divisor set; the mass shell in parameter space |
| $S^\pm$, $P_\alpha = \tfrac12(I+S_\alpha)$ | The two complementary boundary operators of the module; $P_\alpha$ built from the Cauchy-type operator $K_\alpha$ |
| $P_{\vec u}=\tfrac12\bigl(e_t-i\sum_k u_k\vec e_k\bigr)$ | Element of the algebra, acting on the left; $Ξ_\omega=P_{\vec u}Ξ_\omega$ is the linear condition |
| $\tilde{p} = P_\alpha\tilde{p} = S^+\tilde{p}$ | The bag reduced to one boundary integral equation |
| **Standard QCD notation, not framework objects** | |
| $SU(3)$, $N_c = 3$, $\mathbf{3}$, $\mathbf{8}$ | Colour group, number of colours, quark, gluon — no route yet |
| $N_f$, $\alpha_s$ | Quark flavour number, strong coupling — imports |

## Further Reading

- Kenneth G. Wilson, "Confinement of Quarks," *Physical Review D* **10** (1974) 2445–2459, for the Wilson loop, the area law, and confinement as a criterion.
- V. V. Kravchenko, "On a Biquaternionic Bag Model," *Zeitschrift für Analysis und ihre Anwendungen* **14** (1995), no. 1, 3–14, DOI 10.4171/ZAA/658, for the real-linear dictionary from the source's four-component fields to biquaternions, the removal of the conjugation operator in the mass term, the reduction of the linear bag model to the boundary equation $\tilde{p} = P_\alpha\tilde{p} = S^+\tilde{p}$, and the invertibility and Fredholm questions for the shifted operator $D_\alpha$.
- V. V. Kravchenko and M. V. Shapiro, *Integral Representations for Spatial Models of Mathematical Physics* (Pitman Research Notes in Mathematics 351, Addison-Wesley Longman, 1996), for the Teodorescu transform, the Cauchy-type operator and the operator of singular integration with a biquaternionic parameter, and the boundary-value criteria the bag reduction uses.
- A. W. Thomas, "Chiral Symmetry and the Bag Model: A New Starting Point for Nuclear Physics," *Advances in Nuclear Physics* **13** (1984) 1–137, for the bag model itself, the confining region and its linear boundary condition.
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
- M. Ohya and D. Petz, *Quantum Entropy and Its Use* (Springer, 1993), for the monotonicity of relative entropy under completely positive maps and the structure of channels that fix their image.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the channel formalism and the distinguishability measures used here.
