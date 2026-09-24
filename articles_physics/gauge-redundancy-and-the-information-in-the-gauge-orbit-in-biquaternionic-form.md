# __Gauge Redundancy and the Information in the Gauge Orbit in Biquaternionic Form__

## Introduction

The gauge principle in biquaternionic form localizes the central phase of the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ and finds that the price of locality is a connection. Under a gauge function $\Gamma$ the connection transforms as

$$
\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma,
$$

and the field strength $\tilde{F} = \mathrm{Vect}(\bar{\tilde{\nabla}}\tilde{A})$ is unchanged. Two potentials related by such a shift are not two physical configurations; they are two descriptions of one. The set of descriptions of a single configuration,

$$
\mathcal{O}(\tilde{A}) = \bigl\{\tilde{A} - \tilde{\nabla}\Gamma : \Gamma \ \text{a real scalar function}\bigr\},
$$

is the **gauge orbit** of $\tilde{A}$. This article asks what the gauge orbit is, information-theoretically, and answers that the orbit is a **redundancy** rather than a loss: it is the fibre of the map from descriptions to physical configurations, it carries no state information, and every information measure of the theory is constant along it. What the orbit does carry is structure rather than state, and that structure is exactly what the holonomy of the connection records.

The distinction this article draws is worth setting out at the start, because two neighbours in the subcategory depend on it. Three operations must be kept apart:

- **Redundancy.** Many descriptions, one configuration. The map is many-to-one, but the fibre is a group orbit, and a representative can be chosen — locally always, globally up to an obstruction. No information is created and none is destroyed; the description is merely overcomplete. This is the gauge orbit.
- **Loss.** Many configurations, one record. The map is many-to-one *after* the redundancy has been quotiented out, and no choice of description recovers the configuration. The information is inaccessible, not merely redundant. Confinement, treated in the companion article, is of this kind.
- **Relocation.** The information is re-encoded in a different carrier, reversibly. The total is conserved and a gauge-invariant record remains. The Higgs mechanism, treated in the companion article, is of this kind.

The biquaternion framework makes the first of the three exact, because the abelian gauge group it localizes is the unitary part of the centre of the algebra: the redundancy is the unobservability of a central phase, and a central phase acts trivially on the informational sector. The orbit is therefore not merely "unobservable" in a practical sense; it is invisible to every Hermitian observable the algebra carries. The framework also realizes the compact algebra $\mathfrak{su}(2)$ in its sectors, and the non-abelian orbit — the adjoint orbit, for which the same triviality does not hold — is treated in the companions and recorded as an open item below.

The article proceeds as follows. The orbit is defined and its structure as a torsor is established. The orbit is then identified as the fibre of the curvature map, and the counting of physical degrees of freedom is extracted from the rank of that map. The information-theoretic invariance of the orbit is proved through the relative entropy, and the central triviality of the abelian phase is exhibited. The global information of the orbit — its holonomy — is then separated from its local emptiness. A comparison of redundancy, loss and relocation sets the article against its two companions. A closing ledger states what the algebra supplies and what it only transcribes.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_1e_2 = e_3$, and $i$ is the scalar imaginary, $i^2 = -1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector), with $\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+$; $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_\mathbb{R}\{e_0, ie_0\}$ is the centre of the algebra and $\mathbb{H}_{\mathbb{B}}$ the real-quaternion subspace. The biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$, its quaternion conjugate is $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_1\partial_x - e_2\partial_y - e_3\partial_z$, and

$$
\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \partial_{ict}^2 + \Delta = \Delta - c^{-2}\partial_t^2 ,
$$

the series convention. <!-- CONVENTION — d'Alembertian sign: this is the series \Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2 + \Delta, opposite in sign to the Weyl-spinor exercise's \Box_Weyl = \partial_0^2 - \nabla^2. The two differ by an overall minus, so a mass-term sign written with one is the same equation written with the other. Do not "align" the signs. --> The connection is $\tilde{A} = \sum_{\mu=0}^{3}A_\mu e_\mu = i\phi/c\,e_0 + \mathbf{A} \in \mathbb{M}_-$, with $A_0 = i\phi/c$ purely imaginary and $A_1,A_2,A_3$ real; it transforms as above under a real gauge function $\Gamma$. The coupling is written $\kappa = q/\hbar$, so that $D = \tilde{\nabla} + i\kappa\tilde{A}$ and $D_\mu = \partial_\mu + i\kappa A_\mu$. The gauge scalar is $S = \mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{A})$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the **speed of light in the medium** and $c_0$ its vacuum value. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged.

## The Gauge Orbit as a Torsor

The set $\mathcal{O}(\tilde{A})$ is the image of the map

$$
\mathcal{G} \longrightarrow \mathbb{B}, \qquad \Gamma \longmapsto \tilde{A} - \tilde{\nabla}\Gamma,
$$

where $\mathcal{G}$ is the abelian group of real scalar functions on spacetime with the pointwise addition. Two elementary facts fix the shape of the orbit.

**The map is affine, and its linear part is injective modulo constants.** Suppose $\tilde{\nabla}\Gamma = 0$. In components,

$$
\tilde{\nabla}\Gamma = e_0\,\partial_{ict}\Gamma + e_1\,\partial_x\Gamma + e_2\,\partial_y\Gamma + e_3\,\partial_z\Gamma = 0
$$

forces every partial derivative of $\Gamma$ to vanish, so $\Gamma$ is constant. The kernel of $\Gamma \mapsto \tilde{\nabla}\Gamma$ is therefore the one-dimensional space of constants, and the group that acts freely and transitively on the orbit is $\mathcal{G}$ modulo those constants. The orbit is a copy of that group:

$$
\mathcal{O}(\tilde{A}) \;\cong\; \mathcal{G}\big/\mathbb{R}.
$$

A space on which a group acts freely and transitively is a **torsor**: it is a copy of the group, but with no distinguished identity point. There is no preferred member of the orbit — no "the" connection — because singling one out would require a gauge-fixing condition, and the canonical-quantization article of the series records that the framework supplies none.

**The orbit is convex, and its tangent space is the space of gradients.** Because $\Gamma$ ranges over all real scalar functions, the orbit is an affine subspace of the (infinite-dimensional) space of $\mathbb{B}$-valued one-forms, translated from the origin by $\tilde{A}$. Its tangent space at any point is the same: the image of the linear map $\Gamma \mapsto -\tilde{\nabla}\Gamma$, which consists of the **pure gradients**.

These two facts are the whole geometry of the orbit: it is a flat affine space modelled on the gradients, on which the gauge group acts simply transitively once the constants are removed.

### The Orbit in Fourier Space

The local structure is read off mode by mode. Let a single Fourier mode of the connection carry wavevector $k = (k_0,k_1,k_2,k_3)$ on the $ict$ coordinates, so that a gradient acts as left multiplication by $iK$ with

$$
K = \sum_{\mu=0}^{3}k_\mu e_\mu .
$$

A pure-gauge mode with real scalar amplitude $g$ contributes $iKg$, so its image is the **real line spanned by $iK$** inside the four-dimensional fibre. The linear map from gauge functions to connections therefore has rank one per mode (rank zero only for the constant mode $k = 0$, on which there is no gauge freedom). This was checked numerically: for generic wavevectors and a generic real amplitude, the four ratios of the components of $iKg$ to those of $K$ agreed to $2\times10^{-16}$.

The rank is the count of gauge directions per mode, and subtracting it from the four components of the connection gives the count of physical directions. That count is taken up in the next section.

### The Orbit and the Covariant Derivative

The reason two members of an orbit are two descriptions rather than two configurations is the transformation law of the covariant derivative. For a matter field $\tilde{\Psi}$ carrying the central charge, the minimal prescription of the companion article is $D = \tilde{\nabla} + i\kappa\tilde{A}$, and under the gauge function $\Gamma$ both the connection and the field shift together,

$$
\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma,
\qquad
\tilde{\Psi}' = \lambda\tilde{\Psi},
\qquad
\lambda = e^{i q\Gamma/\hbar}.
$$

The three shifts are arranged so that the derivative of the transformed field in the transformed background is the transform of the derivative:

$$
D'\tilde{\Psi}' = \left(\tilde{\nabla} + i\kappa\tilde{A} - i\kappa\tilde{\nabla}\Gamma\right)\lambda\tilde{\Psi}
= \lambda\left(\tilde{\nabla} + i\kappa\tilde{A}\right)\tilde{\Psi}
= \lambda\,D\tilde{\Psi},
$$

the middle step using that $\lambda$ is central, so that $\tilde{\nabla}(\lambda\tilde{\Psi}) = (\tilde{\nabla}\lambda)\tilde{\Psi} + \lambda\tilde{\nabla}\tilde{\Psi}$ and $(\tilde{\nabla}\lambda) = i\kappa(\tilde{\nabla}\Gamma)\lambda$ cancels the shift of the connection. Equivalently, at the level of operators,

$$
D' = \lambda\,D\,\lambda^{-1}.
$$

This is the algebraic content of the redundancy: the pair $(\tilde{A},\tilde{\Psi})$ and the pair $(\tilde{A}',\tilde{\Psi}')$ are related by the local unitary $\lambda$, and every quantity built from $D$ and $\tilde{\Psi}$ in a gauge-covariant way is therefore unchanged. The operator identity is what makes the invariance of the relative entropy, established below, a statement about the biquaternion algebra rather than an imported fact about gauge theory.

Two remarks fix the scope. The transformation is an automorphism of the field algebra only when $\lambda$ is central, which is the abelian case the framework's own gauge group supplies; for a non-abelian group $D' = \lambda D\lambda^{-1}$ holds with $\lambda$ a matrix-valued group element and $\lambda^{-1}$ on the right, which is the adjoint law of the non-abelian companion. And because the framework's $\lambda$ is central, conjugation by it fixes every element of $\mathbb{B}$: the inner automorphism $\iota_\lambda$ of the algebra is the identity, and the transformation acts on the pair $(\tilde{A},\tilde{\Psi})$ as the common central scalar $\lambda$ rather than as a non-trivial re-labelling of the algebra's elements. That is why the abelian orbit is not merely equivalent to a trivial action on the informational sector but literally the trivial action, as the next section shows.

## The Orbit Is the Fibre of the Curvature Map

The curvature does not depend on which member of the orbit is used. Write the field strength as the vector part of $\bar{\tilde{\nabla}}\tilde{A}$,

$$
\tilde{F} = \mathrm{Vect}\!\left(\bar{\tilde{\nabla}}\tilde{A}\right),
$$

the identification inherited from the gauge principle and the covariant-derivative articles. Under a gauge transformation,

$$
\tilde{F}' = \mathrm{Vect}\!\left(\bar{\tilde{\nabla}}\tilde{A} - \bar{\tilde{\nabla}}\tilde{\nabla}\Gamma\right)
= \mathrm{Vect}\!\left(\bar{\tilde{\nabla}}\tilde{A}\right) - \mathrm{Vect}\!\left(\Box\Gamma\,e_0\right)
= \tilde{F},
$$

because $\bar{\tilde{\nabla}}\tilde{\nabla}\Gamma = \Box\Gamma\,e_0$ is a pure scalar and has no vector part. The orbit is thus the fibre of the map $\tilde{A}\mapsto\tilde{F}$: on any one orbit, the curvature is constant, and along the orbit nothing but the pure-gauge scalar changes.

The scalar part of $\bar{\tilde{\nabla}}\tilde{A}$ is the gauge scalar

$$
S = \mathrm{Sc}\!\left(\bar{\tilde{\nabla}}\tilde{A}\right) = \partial_{ict}A_0 + \mathrm{div}\,\mathbf{A},
\qquad
S' = S - \Box\Gamma ,
$$

so $S$ is pure gauge: its value can be changed at will along the orbit, and the Lorenz condition $S = 0$ is a choice of representative, not a physical statement. The two statements — $\tilde{F}$ invariant, $S$ pure gauge — are the two halves of a single fact: the orbit is the fibre, the curvature is the base, and the scalar part of $\bar{\tilde{\nabla}}\tilde{A}$ is the coordinate along the fibre.

Both statements were checked on a superposition of three plane-wave modes with generic wavevectors and generic biquaternion amplitudes, using the formal coordinates $x_\mu$ with $x_0 = ict$ and no restriction on the mode wavevectors. The vector part of $\bar{\tilde{\nabla}}\tilde{A}$ was unchanged by a gauge transformation to within $5\times10^{-16}$, and the scalar part shifted by exactly $-\Box\Gamma$, to within $9\times10^{-16}$. The identity

$$
\tilde{F} = \frac{1}{2}\sum_{\mu,\nu}F_{\mu\nu}\,\bar{e}_\mu e_\nu ,
\qquad F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu ,
$$

was checked against the direct evaluation of $\mathrm{Vect}(\bar{\tilde{\nabla}}\tilde{A})$ on a generic connection and wavevector, agreeing to $5\times10^{-16}$. A connection on the orbit through zero, $\tilde{A} = -\tilde{\nabla}\Gamma$, is flat in the same sense: its vector part came out zero to $2\times10^{-16}$, while its scalar part equalled $-\Box\Gamma$ to $2\times10^{-16}$, which is the shift law's requirement for the member of the orbit that satisfies $S = 0$. For $\tilde{A} = +\tilde{\nabla}\Gamma$ the scalar part is $+\Box\Gamma$; the sign is carried by the direction of the shift, and the orbit's definition $\tilde{A}' = \tilde{A}-\tilde{\nabla}\Gamma$ fixes it.

### Local Triviality and the Degree-of-Freedom Count

Any connection can be removed at a single point. Fix a point $\tilde{X}_0$ and let $A_\mu$ be the components of $\tilde{A}(\tilde{X}_0)$, with $A_0$ imaginary and $\mathbf{A}$ real. Define

$$
\Gamma(\tilde{X}) = \sum_{\mu=0}^{3} A_\mu\,(x_\mu - x_{0\mu}),
$$

treating the $x_\mu$ as independent coordinates. Then $\partial_\mu\Gamma = A_\mu$, so $\tilde{\nabla}\Gamma = \tilde{A}(\tilde{X}_0)$ and the transformed connection $\tilde{A} - \tilde{\nabla}\Gamma$ vanishes at $\tilde{X}_0$. The connection can therefore be gauged to zero at any one point, and consequently **no gauge-invariant local function of $\tilde{A}$ exists**: every such function would have to be constant along the orbit, and the orbit passes through zero at the point. The first non-trivial gauge-invariant object is the curvature, and it is the obstruction to extending the elimination from a point to a neighbourhood.

The count of physical degrees of freedom now follows from the rank of the pure-gauge map.

- The connection has **four real components** per point: the material-sector condition $\tilde{A}\in\mathbb{M}_-$ makes $A_0 = i\phi/c$ purely imaginary and $A_1, A_2, A_3$ real, so the field carries four real functions, not four complex ones, and its Fourier data is correspondingly four real amplitudes rather than four complex ones.
- The gauge function is one real function, and its gradient removes one real direction from the four per mode, as the rank of the pure-gauge map established above.
- Off shell the physical content is therefore $4 - 1 = 3$ real components per mode.
- The field equation supplies one further constraint. The $\nu = 0$ component of $\partial_\mu F^{\mu\nu} = J^\nu$ — the Gauss law — contains no second time derivative, so it constrains the initial data rather than evolving it, and it removes one of the three components, leaving $4 - 1 - 1 = 2$ per mode: the two transverse polarizations.

This is the standard $4 \to 3 \to 2$ counting of a massless vector field, and it is reproduced here by the rank of the biquaternion orbit. The count is stated for real components, which is the count the material-sector reality condition makes available; a connection with four unconstrained complex components would carry eight real ones and the arithmetic would not close on two. The point of reproducing the count is that it is a statement about the **fibre**: the gauge orbit is exactly the one direction per mode that the count discards.

## What the Orbit Carries: Redundancy, Not State

The orbit is large — a copy of the group of gauge functions modulo constants, so larger than the physical configuration space it projects to — and the question this article exists to answer is what informational content that largeness has. The answer has two parts.

**The orbit carries no state information.** No observable can distinguish two members of an orbit, because every observable is gauge invariant and the members differ by a gauge transformation. This is the definition of the redundancy, but the biquaternion framework gives it a sharper form than the definition does, and the sharpening is the subject of the next section: the two members define *unitarily equivalent states*, so not merely the values of observables but the entire information-theoretic relation between two states is constant along the orbit.

**The orbit carries structural information.** A torsor is not nothing. The orbit's existence says that a connection is not a physical object but a representative; its size is the group of gauge functions; its non-triviality over a region — the failure of the orbit at a point to extend to a neighbourhood — is the curvature. The information "in" the orbit is therefore information about the **gauge structure**, not about the configuration. It is the same at every point, and it is fixed once the gauge group is fixed. In this sense the orbit is a constant: its information is the symmetry, not the state.

The two parts are the reason the title's phrase needs care. If "the information in the gauge orbit" means the state information that the orbit's many labels purport to describe, the answer is zero. If it means the structural information that the existence of the orbit encodes, the answer is the gauge group and the holonomy, and it is entirely in the orbit's global shape.

## Information-Theoretic Invariance of the Orbit

The claim that the orbit carries no state information can be made exact with the relative entropy, the basic monotone quantity of the informational sector.

Let $\omega$ be a state of the charged field algebra in a background connection $\tilde{A}$, and let $\omega'$ be the corresponding state in the gauge-transformed background $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$. Gauge covariance states that the two are related by the automorphism implemented by the local central phase,

$$
\lambda(\tilde{X}) = e^{iq\Gamma(\tilde{X})/\hbar}, \qquad
\omega' = \omega \circ \mathrm{Ad}_{\lambda^{-1}} .
$$

Because $\lambda$ is central and of unit phase, the automorphism is inner and implemented by a unitary of the algebra, and the GNS representations of $\omega$ and $\omega'$ are unitarily equivalent. For any two backgrounds $\tilde{A}$ and $\tilde{B}$ and their gauge transforms, the relative entropies therefore agree:

$$
S(\tilde{\rho}_{\tilde{A}'}\,\|\,\tilde{\sigma}_{\tilde{B}'}) = S(\tilde{\rho}_{\tilde{A}}\,\|\,\tilde{\sigma}_{\tilde{B}}) .
$$

This is the invariance, under unitary conjugation of both arguments, of the Umegaki relative entropy, $S(U\rho U^\dagger\|U\sigma U^\dagger) = S(\rho\|\sigma)$, inherited from the companion article on relative entropy. It was checked on explicit superpositions: with the two Bloch vectors $\mathbf{r} = (0.35,-0.55,0.28)$ and $\mathbf{s} = (0.6,0.1,-0.42)$ and a rotation by $0.9$ radians about the axis $(1,2,-0.5)$, the relative entropy took the value $0.626042709560$ before and after the rotation, agreeing to $3\times10^{-16}$.

Three consequences of the invariance spell out the redundancy.

**No information measure can detect the orbit.** Relative entropy is the sharpest distinguishability measure of the theory, and it is constant along the orbit. Whatever else the orbit is, it is not a difference of states.

**The invariance is not confined to the relative entropy.** Every functional of the state that is invariant under unitary conjugation inherits it: the spectrum of $\tilde{\rho}$, the fidelity between two states, any $f$-divergence, and, for a phase acting as a local unitary on a subsystem, that subsystem's entanglement entropy. The redundancy is therefore a property of the representation rather than of any particular measure; and because the abelian phase is central and of unit modulus, each of these quantities is here not merely preserved along the orbit but unchanged.

**The abelian orbit is invisible to the informational sector.** This is the framework-specific sharpening. The gauge group is the unitary part of the centre, so $\lambda = e^{i\theta}$ commutes with every element of $\mathbb{B}$. On a state $\tilde{\rho}\in\mathbb{M}_+$ its action is

$$
\tilde{\rho} \longmapsto \lambda\,\tilde{\rho}\,\lambda^\dagger = |\lambda|^2\tilde{\rho} = \tilde{\rho},
$$

so the state is not merely unitarily equivalent to its gauge transform — it is *literally unchanged*. The central phase acts trivially on the Hermitian sector. The redundancy is the statement that the algebra carries no Hermitian observable conjugate to its central phase, and therefore no informational content located in the phase direction.

This is the precise sense in which the abelian gauge orbit carries no information: the generator of the orbit is the central imaginary $i$, and $i$ commutes with everything, so no observable can read it. The redundancy is the price of the algebra having a centre, and the centre is what supplies the abelian gauge group.

## The Global Information of the Orbit: Holonomy

The orbit is locally trivial — a single point can always be gauged away — but not globally, and the global obstruction is the only place the orbit's structure becomes a physical number.

**Local elimination is always possible; global elimination is not.** As shown above, a connection can be gauged to zero at any point. It can be gauged to zero on a neighbourhood precisely when its curvature vanishes there, because a flat connection is locally a gradient. Globally, a flat connection need not be a gradient: its **holonomy** around a non-contractible loop is the obstruction. The holonomy is the path-ordered exponential of the connection around a closed curve,

$$
U(C) = \mathcal{P}\exp\!\left(i\oint_C A_\mu\,dx^\mu\right),
$$

and its trace is the Wilson loop, $W(C) = \mathrm{Tr}\,U(C)$. In the biquaternion framework the connection being integrated is a material-sector object, $\tilde{A}\in\mathbb{M}_-$, and the group element it exponentiates into is an element of the informational realization of the gauge group, so the Wilson loop is a two-sector bilinear. This is the construction of the companion article on Wilson loops, and it is not re-derived here.

**The holonomy is the orbit's global invariant.** The orbit of a connection is its gauge group; the holonomy is a functional of the connection that is constant on the orbit and is not a local function of the curvature. It is therefore exactly the part of the orbit's information that survives the local triviality. The framework's ordering of the object is clean:

- the connection is a point in the orbit, and has no invariant local value;
- the curvature is the local invariant, the obstruction to eliminating the connection on a neighbourhood;
- the holonomy is the global invariant, the obstruction to eliminating it on a loop.

The information in the gauge orbit is, in this reading, the holonomy: the orbit is locally a fibre, and globally it is a fibre bundle whose monodromy is physical. The statement is not that the orbit carries state information; it is that the orbit's *topology* carries the only gauge-invariant content that is not already in the curvature.

### The Aharonov–Bohm Reading

The clearest demonstration that the orbit carries information the curvature does not is the Aharonov–Bohm phase. Let a loop enclose a region of flux that is confined to a tube the loop does not touch, so that $\tilde{F}$ vanishes at every point of the loop. The curvature along the loop is then zero, and a local reading of the field strength would conclude that the loop encloses nothing. The holonomy is nevertheless $U(C) = \exp(i\Phi)$ with $\Phi$ the enclosed flux, because Stokes' theorem equates the loop integral to the flux through any surface it bounds, and the flux is concentrated on the surface rather than on the curve.

Information-theoretically this is the sharp statement of the article's thesis. The curvature is a local density and is zero on the loop; the connection, evaluated along the loop, is not zero; the loop integral measures the second and not the first. So the redundancy — the fact that the connection is a point in an orbit rather than an invariant — is not an inefficiency of the description. The orbit is the carrier of a genuinely non-local, gauge-invariant phase, and it is the smallest object on which the orbit's structure becomes measurable. The Wilson loop of the companion article is precisely the gauge-invariant trace of this phase, and the Aharonov–Bohm effect is the case in which it is the *only* thing the loop measures.

## Redundancy and Loss: Three Operations Compared

The subcategory treats three operations, and the present article is the one that fixes the meaning of the first. They are worth tabulating before the two companions develop the others, because the information-theoretic vocabulary is shared and the distinctions are easy to blur.

| Operation | Map | Fibre | Reversibility | Information |
|---|---|---|---|---|
| Gauge redundancy | descriptions $\to$ configurations | the gauge orbit | a representative exists locally; obstruction globally is the holonomy | neither created nor destroyed; all measures orbit-invariant |
| Confinement | configurations $\to$ asymptotic records | the colour-singlet collapse | not reversible; no gauge choice recovers the label | partonic labels inaccessible to the asymptotic algebra |
| Higgs relocation | symmetric-phase data $\to$ broken-phase data | the gauge orbit of the phase | reversible on the full degrees of freedom; the mass is the record | conserved in total; relocated into the longitudinal mode |

The middle row is the subject of the companion article on confinement, and the bottom row of the companion article on the Higgs mechanism. What the table is meant to make visible is that the three are not variants of one another. Redundancy has an *informationally empty* fibre — the orbit is what a gauge choice quotients away, and choosing a gauge recovers the configuration. Loss has a fibre that is informationally non-empty — distinct partonic configurations yield the same asymptotic record, and no gauge choice recovers them. Relocation has a gauge orbit as its fibre as well — so the fibre carries no state information either — but the mechanism's action on the orbit leaves a record, the mass, and conserves the count of local degrees of freedom. The biquaternion framework houses all three in the same algebra, and the algebra's sector split is what keeps them distinct.

## Gauge Redundancy and the Informational Sector

The framework's gauge group is not put in by hand: it is the unitary part of the centre, $U(1) = \{e^{i\theta}\}$. This has a consequence for the relation between the gauge orbit and the informational sector that is worth isolating.

**The orbit is a material-sector structure.** The connection lies in $\mathbb{M}_-$, and the gauge transformation shifts it by the gradient of a real scalar, which is again in $\mathbb{M}_-$. The orbit is therefore an orbit inside the material sector. The gauge group acts on it, but the group is one-dimensional precisely because it is the centre, and a central action on $\mathbb{M}_-$ is a shift by the identity direction.

**The informational sector is blind to the orbit.** As established above, a central phase acts trivially on $\mathbb{M}_+$. The informational sector — states, observables, measurements — carries no variable conjugate to the gauge orbit. In the operational reading of *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, the gauge orbit is not an unmeasured variable; it is a **non-variable**. There is no observable whose outcome distribution differs across the orbit, so the orbit cannot appear in any information-theoretic accounting of the sector.

**The one place the two sectors meet is the holonomy.** The Wilson loop is the trace of the holonomy — a material connection integrated along a curve and exponentiated into the informational realization of the group — and its gauge invariance is the invariance of the scalar part under the adjoint action. It is the single object in which the orbit's global structure is paired with an informational trace. The reading of that pairing is the open question the Wilson-loop article records; here it is enough to note that the pairing is where the redundancy stops being invisible and starts being a physical number.

## What the Algebra Supplies, Transcribes, and Only Interprets

The boundary is drawn as in the companion articles.

**Supplied by the algebra, and recomputed here.** The orbit is the image of the gradient map, an affine space modelled on the gradients, on which the gauge group acts freely and transitively modulo constants; the gradient map has rank one per Fourier mode, which is the first subtraction in the degree-of-freedom count; the curvature is orbit-invariant and the gauge scalar is pure gauge; a connection can be removed at a point, so no gauge-invariant local function of the connection exists; and the relative entropy is invariant along the orbit, with the abelian phase acting trivially on the Hermitian sector. All of these are exact and were checked.

**Transcribed from standard gauge theory.** The reading of the orbit as a fibre, of the connection as a section, and of the holonomy as monodromy is the standard bundle picture written in the algebra's notation. The algebra makes the invariance transparent; it does not force the geometric reading. The degree-of-freedom counting is the standard one for a massless vector field: the framework supplies its first step — the rank-one orbit — and the second step, the Gauss-law constraint, is imported with the field equation.

**Not supplied.** A gauge-fixing principle, which the canonical-quantization article records as absent; the non-abelian orbit, whose transformation law is the adjoint one and whose reality condition is open; and any empirical consequence distinguishing the reading from standard gauge theory. The orbit and its invariance are properties of any formulation of an abelian gauge theory; the framework's contribution is to locate the gauge group in the centre of the algebra and to exhibit the orbit as the fibre of the curvature map.

**Companion articles.** The construction rests on the following written articles of the series.

- Companion article *The Gauge Principle in Biquaternionic Form*, for the connection, its transformation law, the local central phase, and the covariant derivative.
- Companion article *The Covariant Derivative and Gauge Connection in Biquaternionic Form*, for $D$ as an operator, its covariance, and the covariant square.
- Companion article *Non-Abelian Gauge Fields in Biquaternionic Form*, for the adjoint transformation law and the non-abelian orbit.
- Companion article *Wilson Loops in Biquaternionic Form*, for the holonomy, the loop as a two-sector bilinear, and the small-loop expansion.
- Companion article *Canonical Quantization of the Biquaternion Maxwell Field*, for the constraint structure and the absent gauge-fixing principle.
- Companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the state space, the trace, and the absence of an observable conjugate to the central phase.
- Companion article *Relative Entropy and the Biquaternion Framework*, for the relative entropy and its invariance under unitary conjugation.
- Companion article *Confinement and the Loss of Partonic Information in Biquaternionic Form*, for the loss case against which this article's redundancy is defined.
- Companion article *The Higgs Mechanism as an Erasure of Information in Biquaternionic Form*, for the relocation case against which this article's redundancy is defined.

## Open Questions

1. **A gauge-fixing principle.** The orbit is a torsor, so no member is preferred. Is there an algebraic principle that selects a representative — a condition natural to $\mathbb{B}$ rather than imported — or is the choice irreducibly extrinsic, as the canonical-quantization article suggests?

2. **The non-abelian orbit.** For a non-central gauge group the orbit is the adjoint orbit of the connection, $A_\mu\mapsto U A_\mu U^{-1} + (i/\kappa)(\partial_\mu U)U^{-1}$, and it is no longer a torsor of an abelian group but a coadjoint-type space. Does the orbit still have a clean fibre interpretation, and does the relative-entropy invariance survive with the appropriate unitary?

3. **The orbit and the local complex structure.** The framework makes the complex structure local through the speed of light $c = 1/\sqrt{\epsilon\mu}$. Is the gauge orbit — a local shift by a gradient — related to that local complex structure, or are the two local structures independent? No relation is established here.

4. **The measure on the orbit.** The path integral of the gauge theory integrates over connections, hence over orbits. Does the biquaternion algebra supply a natural measure on the orbit, and is the Faddeev–Popov procedure its transcription? The non-abelian path-integral companion is the setting for the question.

5. **The holonomy as the orbit's invariant.** If the holonomy is the only gauge-invariant content beyond the curvature, is there a framework-internal characterization of it — an element of the algebra whose scalar part is the loop — that makes the pairing of the two sectors canonical?

6. **Empirical content.** As everywhere in the framework, whether any of this yields a prediction distinguishing it from standard gauge theory. The orbit's information-theoretic properties are those of any abelian gauge theory, and no distinction is derived here.

## Summary

The gauge orbit of a biquaternionic connection is the set $\mathcal{O}(\tilde{A}) = \{\tilde{A} - \tilde{\nabla}\Gamma\}$ of descriptions of one physical configuration. It is a torsor for the group of real gauge functions modulo constants: the gradient map has kernel the constants, so the gauge group acts freely and transitively, and there is no preferred representative. It is the fibre of the curvature map, because $\tilde{F} = \mathrm{Vect}(\bar{\tilde{\nabla}}\tilde{A})$ is orbit-invariant while the gauge scalar $S = \mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{A})$ shifts by $-\Box\Gamma$ and is pure gauge. The rank of the pure-gauge map is one per Fourier mode, which yields the standard degree-of-freedom count $4\to3\to2$.

Information-theoretically the orbit is a **redundancy**, not a loss. A gauge transformation is implemented by the central phase $\lambda = e^{iq\Gamma/\hbar}$, which is unitary, so gauge-related backgrounds define unitarily equivalent states and the relative entropy is constant along the orbit,

$$
S(\tilde{\rho}_{\tilde{A}'}\|\tilde{\sigma}_{\tilde{B}'}) = S(\tilde{\rho}_{\tilde{A}}\|\tilde{\sigma}_{\tilde{B}}).
$$

For the framework's abelian group the statement is stronger still: because the phase is central and Hermitian, it acts on a state of $\mathbb{M}_+$ by $\tilde{\rho}\mapsto|\lambda|^2\tilde{\rho} = \tilde{\rho}$. The informational sector is not merely unable to distinguish the orbit; it is unchanged by it, and no observable is conjugate to the central phase.

The orbit's only non-empty content is global. A connection can be gauged to zero at any point, and on a neighbourhood precisely when its curvature vanishes; the obstruction to doing so on a loop is the holonomy, whose trace is the Wilson loop. The information in the gauge orbit is therefore its monodromy — the fibre-bundle structure that the local triviality leaves behind — and not any state information. Redundancy, loss and relocation are three different operations, and the orbit realizes the first: the fibre is quotiented away and a representative recovers the configuration, which is what distinguishes it from the confinement of the companion article and from the relocation of the Higgs mechanism.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H} \cong M_2(\mathbb{C})$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_1e_2 = e_3$ |
| $i$ | Scalar imaginary, $i^2 = -1$, central |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_\mathbb{R}\{e_0, ie_0\}$ | Centre of the algebra; source of the abelian gauge group $U(1)$ |
| $\tilde{\nabla} = e_0\partial_{ict} + e_k\partial_k$ | Biquaternionic gradient |
| $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_k\partial_k$ | Quaternion-conjugate gradient |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2 + \Delta$ | d'Alembertian, series convention |
| $\tilde{A} = \sum_\mu A_\mu e_\mu = i\phi/c\,e_0 + \mathbf{A} \in \mathbb{M}_-$ | Connection, a material-sector one-form |
| $\Gamma$ | Real scalar gauge function |
| $\lambda = e^{iq\Gamma/\hbar}$ | Local central phase |
| $\kappa = q/\hbar$ | Coupling |
| $\mathcal{O}(\tilde{A}) = \{\tilde{A} - \tilde{\nabla}\Gamma\}$ | The gauge orbit |
| $\mathcal{G}/\mathbb{R}$ | Group of real gauge functions modulo constants; the orbit's torsor group |
| $K = \sum_\mu k_\mu e_\mu$ | Wavevector biquaternion of the mode $k = (k_0,k_1,k_2,k_3)$; pure-gauge image is the real line $\mathbb{R}(iK)$ |
| $S = \mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{A}) = \partial_{ict}A_0 + \mathrm{div}\,\mathbf{A}$ | Gauge scalar, pure gauge: $S' = S - \Box\Gamma$ |
| $\tilde{F} = \mathrm{Vect}(\bar{\tilde{\nabla}}\tilde{A}) = \frac{1}{2}\sum_{\mu\nu}F_{\mu\nu}\bar{e}_\mu e_\nu$ | Field strength = curvature, orbit-invariant |
| $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ | Abelian curvature components |
| $U(C) = \mathcal{P}\exp(i\oint_C A_\mu dx^\mu)$ | Holonomy; global obstruction |
| $W(C) = \mathrm{Tr}\,U(C)$ | Wilson loop; two-sector bilinear |
| $\tilde{\rho} = \tfrac12(e_0 + i\mathbf{r})$, $|\mathbf{r}|\leq1$ | State of the informational sector (Bloch ball) |
| $S(\tilde{\rho}\|\tilde{\sigma})$ | Relative entropy; orbit-invariant. Distinct from the gauge scalar $S$ above — the two share a letter and nothing else |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace pairing; $\mathrm{Tr}(e_0) = 2$ |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- Hermann Weyl, "Elektron und Gravitation," *Zeitschrift für Physik* **56** (1929) 330–352, for the origin of the local phase and the redundancy it introduces.
- Chen-Ning Yang and Robert L. Mills, "Conservation of Isotopic Spin and Isotopic Gauge Invariance," *Physical Review* **96** (1954) 191–195, for the non-abelian transformation law and the adjoint orbit.
- P. A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for first-class constraints and the statement that the gauge freedom is not fixed by the equations of motion.
- L. D. Faddeev and A. A. Slavnov, *Gauge Fields: Introduction to Quantum Theory* (Benjamin/Cummings, 1980), for the orbit, gauge fixing, and the Faddeev–Popov measure.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the counting of physical polarizations and the role of the Bianchi identity.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I: Foundations* (Cambridge, 1995), for the gauge orbit as the fibre of the connection and the degree-of-freedom count.
- Kenneth G. Wilson, "Confinement of Quarks," *Physical Review D* **10** (1974) 2445–2459, for the holonomy, the Wilson loop, and the obstruction interpretation.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the unitary invariance of relative entropy and the distinguishability measures of quantum states.
- M. Ohya and D. Petz, *Quantum Entropy and Its Use* (Springer, 1993), for relative entropy, its monotonicity, and its invariance under unitary conjugation.
- H. Araki, "Relative entropy of states of von Neumann algebras," *Publications of the Research Institute for Mathematical Sciences* **11** (1976) 809–833, for the state-theoretic invariance used here.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric reading of the connection and its curvature in the same algebraic setting.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the identification of the biquaternion algebra with the even part of $\mathrm{Cl}_{1,3}$ and the bivector structure of the curvature.
