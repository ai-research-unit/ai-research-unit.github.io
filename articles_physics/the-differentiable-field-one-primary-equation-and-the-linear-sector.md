# __The Differentiable Field: One Primary Equation and the Linear Sector of the Biquaternion Universe__

## Introduction

The framework states its own test. *Introduction to the Biquaternion Universe* asks, in its first open question, "Is the biquaternion algebra merely a convenient reformulation of known physics, or does the structure of the universe genuinely follow the algebra?", and answers that "A structural hypothesis of this kind can only be evaluated by the richness of the consequences it produces". The present article is about one way of producing such consequences, and about its exact price.

There are two ways to use $\mathbb{B}$ in physics, and they are not the same claim.

**Translation.** Take an equation of physics as given, write it in the algebra, and read what the algebra adds: a geometric meaning, a unification of notation, a constraint that was invisible. The Maxwell equations, the Dirac equation and the gauge principle enter this way, and most of the corpus is of this kind.

**Derivation.** Take the algebra and a definition of the derivative as the only input, ask what a differentiable function must obey, and read the equations of physics as consequences of the answer. Nothing is transcribed, because there is nothing to transcribe from: the field equations become the integrability conditions of one condition on one function.

The first route assumes the dynamics and explains its shape. The second route produces the dynamics and must then explain why it produces *this* dynamics rather than another. The corpus has committed to the first, and its mathematics article *The Two-Sided Derivative over the Biquaternion Algebra* now records the second in its own terms. This article states what the second route gives physics, what it costs, and the one place where the two routes cannot both be right.

## What the Corpus Takes as Input

### The Ledger

The corpus is not uniform about what it postulates, and the distinction between what it derives and what it imports is the first thing to state plainly.

| Item | Status in the corpus | Owner |
|---|---|---|
| The algebra $\mathbb{B}$, its product and its conjugations | postulated | *Introduction to the Algebra of Biquaternions* |
| The interval and the four-vectors of relativity | derived from $\mathbb{B}_{\Phi}$ | *The Material Sector: Four-Vectors, Interval and Lorentz Action* |
| The Lorentz group and its action | derived as the norm-one group | *The Lorentz Group as Biquaternion Norm Automorphisms* |
| The state space and the Born form | derived from $\mathbb{B}_{\Psi}$ | *The Informational Sector: States, Observables and Probability* |
| The Dirac equation | transcribed into the algebra | *The Dirac Equation in Biquaternionic Form* |
| The Maxwell equations | transcribed, or obtained from a biquaternion wave equation | *Nonlinear Maxwell Equations in Biquaternionic Form* |
| The gauge principle | postulated, with a ceiling on the group | *The Gauge Principle in Biquaternionic Form* |
| $\hbar$ | imported, nowhere derived | — |

The pattern is visible in one line: **the corpus derives the arena and imports the dynamics.** The interval, the group, the cone and the state space follow from the algebra; the equations of motion are written into it. The derivation route is an attempt to close that gap, and it closes it from the dynamics side rather than the kinematic one.

### Translation and Derivation Are Not Rivals

A translation is not wasted work when the derivation succeeds. The derivation produces *an* equation set; it must then be compared with the known one, and the comparison is only possible if the known one has already been written in the same algebra. The corpus's transcription articles are the dictionary that makes the derivation legible, and the derivation route is the test of whether the dictionary is a dictionary of one language or of two.

## The Primary Equation

### The Condition, Stated Once

The mathematics is the companion article's and the reader should take it there; one sentence fixes what this article needs. A function is differentiable when its differential factorises, $dF=L\,dZ\,R$, with no inverse taken, and in the matrix model $\mathbb{B}\cong M_2(\mathbb{C})$ this says that for each component $\Sigma$, taken on its own, the array $\mathsf D\Sigma$ of its four coordinate derivatives has rank at most one, equivalently $\det\mathsf D\Sigma=0$, equivalently $N(\nabla\Sigma)=0$. In Cartesian coordinates that last form is the complex eikonal,

$$
\left(\frac{\partial\Sigma}{\partial z_0}\right)^2-\left(\frac{\partial\Sigma}{\partial z_1}\right)^2-\left(\frac{\partial\Sigma}{\partial z_2}\right)^2-\left(\frac{\partial\Sigma}{\partial z_3}\right)^2=0 ,
$$

so the biquaternion gradient of every component is a zero divisor of the algebra. That is the whole of the primary input.

Everything else is a consequence, and the chain is short: a null gradient, hence a direction field; a direction field, hence a congruence of rays; a congruence that the twistor form of the solution makes shear-free and geodesic; a null congruence of that kind that is the principal direction of a null electromagnetic field; and an over-determined system whose integrability forces the self-duality of its curvature, whose Bianchi identity is Maxwell's equation for the trace part and the Yang–Mills equation for the trace-free part. The condition as an equation, the reason complexification is what makes it non-empty, the twistor solution, the generating system and the self-duality are all in *The Algebrodynamical Programme*; the congruence side is *Null Electromagnetic Fields and the Shear-Free Congruence*. This article does not restate them.

### The Eikonal as Primary, and the Inversion of the WKB Relation

The corpus contains the eikonal twice already, in two different roles. *The WKB Approximation and the Hamilton–Jacobi Equation in Biquaternionic Form* derives it as the short-wavelength limit of the linear wave equation: the phase of a rapidly oscillating solution obeys it approximately, and the approximation improves as the wavelength shrinks.

*Null Electromagnetic Fields and the Shear-Free Congruence* carries the eikonal in its **exact complex** form, and it is the closer comparison. Bateman's representation writes a null Maxwell field as $C=d\alpha\wedge d\beta$ from two complex functions that are **required**, as a hypothesis, to obey $\partial\alpha\cdot\partial\alpha=\partial\beta\cdot\partial\beta=\partial\alpha\cdot\partial\beta=0$ in the complexified metric — which is the companion article's eikonal, written for two functions instead of one. Nothing forces it there: it is an assumption on the data, made so that the field built from them is null and duality-pure.

Two differences from the WKB case have to be kept, because without them the two passages read as a contradiction. The corpus's Hamilton–Jacobi equation squares the gradient with the Hermitian form, $\nabla S\,\nabla S^{\natural}$, which is positive definite on a real gradient and therefore never vanishes — the WKB article says as much, remarking that the null cone is not reached by a phase gradient. The primary eikonal squares it with the complex quadratic form $N$, which is indefinite and does vanish, on the cone. And the Hamilton–Jacobi equation carries a right-hand side, twice the kinetic energy, where the primary eikonal is homogeneous.

In the derivation route the eikonal is **exact and primary**, and the wave equation is not a separate postulate but a consequence. The consequence is not the one usually expected. Both equations hold for the same function: every solution the programme constructs satisfies the eikonal *and* $\Box\Sigma=0$, and neither is a limit of the other. The two relations that the algebraic constraint imposes on the solution multiply to the eikonal and cross-differentiate to the wave equation, which is the whole of the mechanism; the mathematics article carries the derivation and the checks.

So the inversion is not a change of subject but a change of **explanatory order**. The WKB reading says: the wave equation is fundamental and the eikonal is its short-wavelength shadow. The derivation reading says: the algebraic constraint is fundamental, the eikonal is one of its consequences and the wave equation the other. Neither reading denies the other's equations, and they disagree only about which one is doing the explaining. Bateman's representation is the intermediate case, and naming it makes the inversion exact rather than rhetorical: there the eikonal is exact and **assumed**, here it is exact and **forced**. The derivation reading has the better claim on the word, because the algebraic constraint is what selects the solutions and the two differential equations are what the selection yields.

This also dissolves the most obvious objection to a nonlinear primary equation. The nonlinearity is real — the solution set is not a vector space — but it is inert: it is not a nonlinear dynamics standing beside a linear one, it is an algebraic selection inside a linear space. The cost is additivity, not linearity.

### The Fields as Semi-Derivatives

What plays the role of the field is not $\Sigma$ but the multiplier. The condition splits as $d\eta=Ξ\,dZ\,\zeta$, with $Ξ$ the left semi-derivative carrying the gauge field and $\eta,\zeta$ two $SL(2,\mathbb{C})$-spinors; the system is eight equations for six unknowns, and the connection it generates is weakly self-dual — the self-dual part of its curvature vanishes on the solutions rather than identically — so that its Bianchi identity is the field equation. That construction is *The Algebrodynamical Programme*, §*The Generating System and the Gauge Fields*, and it is not repeated here.

The point for this article is the direction of the implication. In the corpus's gauge articles the connection is introduced because a symmetry is made local, and the field strength is defined as its curvature; the gauge principle is the postulate. Here the connection is what a differentiable function carries, the curvature is its integrability obstruction, and the field equations are identities. No gauge principle is assumed.

## The Three Corpus Objects the Gradient Meets

A null element of the algebra is not a new object in this corpus, and the three objects that the gradient lands on are already owned. What the derivation adds is that they are met **necessarily** rather than by choice.

### The Zero-Divisor Cone

The gradient is null in the sense of the biquaternion norm, so it lies on the zero-divisor cone, which is the light cone of the material sector and the locus of the pure states of the informational sector, a pure state being a rank-one projector and a rank-one matrix having vanishing determinant (*The Topology of the Zero-Divisor Cone*, *The Light Cone as the Biquaternion Zero-Divisor Cone*, *The Informational Sector: States, Observables and Probability*). The corpus treats that coincidence of three descriptions as a structural fact about the algebra. The derivation route makes it a fact about fields: every differentiable function has a gradient on the cone, so any field theory built this way lives on the cone by construction.

### The Celestial Sphere

A null gradient has a direction, and the direction is a point of the celestial sphere, with the phase of the little group attached to it (*The Celestial Sphere of the Null Cone: Null Directions, Chirality and the Phase*). In the corpus the sphere is the geometry of the massless shell, imported from the relativity of the null cone. In the derivation route it appears as the space in which the gradient of a differentiable function takes its values: the primary equation is a map from the domain into the null directions, and the phase is the freedom the direction leaves open.

### The Shear-Free Congruence

The direction field of a null solution of Maxwell's equations is tangent to a geodesic shear-free congruence, and conversely every such congruence is the principal direction of some null field; that is the Mariot–Robinson theorem, and *Null Electromagnetic Fields and the Shear-Free Congruence* records it together with the honest qualification that the association is **classical**. What the nonlinear system adds is not the association but the construction: it builds the field from the congruence and forces the self-duality instead of receiving it. The derivation route is therefore not a new theorem about null fields; it is a new status for an old one.

### The Three in One Table

| Object | In the corpus | In the derivation route |
|---|---|---|
| Zero-divisor cone | the light cone, the pure-state locus, the zero set of the norm | where every gradient lives |
| Celestial sphere | the sphere of null directions and the little-group phase | the target of the gradient map |
| Shear-free congruence | the principal direction of a null field | the ray system the solution generates |

## What the Derivation Buys

### Gauge Equations Without a Gauge Postulate

The gain is not a new equation but a new status for the old ones. Maxwell and Yang–Mills become identities, and the gauge principle becomes a theorem about the curvature of the connection a differentiable function carries. That is the strongest form the corpus's open question 1 could take: the dynamics is a consequence of the algebra and of one definition, and the definition is not adjustable without changing what a derivative means.

### A Fixed Scale, and What It Does Not Settle

The scale question is the one place where the derivation has real physical content, and it must be stated with more care than it usually is.

**The eikonal alone is scale covariant.** Its condition is homogeneous of degree two in the gradient, so a component may be multiplied by any constant and the condition survives. It is immediate from the polar form, $N(\lambda g)=\lambda^2N(g)$ for every complex $\lambda$. Nothing about a single component's amplitude is fixed by differentiability.

**The connection is not.** The curvature of a connection is $dA+[A,A]$, one term linear in the potential and one quadratic in it. Scaling the potential therefore does not scale the curvature:

$$
F(\lambda A)=\lambda\,F(A)+(\lambda^2-\lambda)\,[A,A] .
$$

The two terms scale differently, so a solution of the self-duality relation $F=iF^{*}$ survives a rescaling only for $\lambda=1$ — or for a commutator term that is itself (anti)self-dual in the same sense, which a generic potential does not have. The admissible amplitudes are isolated, not continuous.

**That is where a fixed amplitude can come from, and it is not a quantum assumption.** A linear theory cannot prefer one amplitude, because its solution space is a vector space and every multiple of a solution is a solution. A theory whose field equations carry a quadratic term can, and here does: the amplitude of the connection is pinned by the self-duality condition rather than left free, and the pinning is a property of the algebra's product and not of $\hbar$. Nothing in the algebra knows about $\hbar$.

The step from a fixed amplitude to a **discrete** charge is the programme's, and it is a further claim, not a corollary of the scaling identity. The programme's value $q=N/4$, with $N$ an integer winding number — the source's letter, colliding with the norm's $N$ above — is stated there with two reasons of its own, one topological and one dynamical, and with a pointer to a general theorem in its later papers; *The Algebrodynamical Programme*, §*Particle-Like Solutions and the Self-Quantized Charge*, records it with that attribution.

### Singularities That Carry the Particle Data

The singular locus of a solution is the branch set of the generating function, $d\Pi/dG=0$, and it is simultaneously the singularity of the semi-derivative, of the electromagnetic field and of the effective geometry — one locus, three readings, which is the programme's answer to why a particle's charge, its field and its gravitational effect share an origin. The coincidence is derived there rather than assumed; what belongs here is that this route produces it.

## What It Costs

### No Action Principle

The generating system is over-determined, eight equations for six unknowns, and the over-determination is what denies it a variational principle of the usual kind. A Lagrangian is what canonical quantisation needs, and the corpus's quantisation articles — *Canonical Quantization of the Biquaternion Graviton Field*, *The Path Integral in Biquaternionic Form* — presuppose one. The derivation route buys its explanatory power at the price of the method by which the rest of the corpus quantises. Any quantisation of it must be a quantisation of a constrained system, and the programme itself says that this requires new methods.

The programme's own position is less absolute than that: the primary system admits no Lagrangian, while the **secondary** gauge fields associated with it do, since they are ordinary field equations once the congruence is given. So the action exists one storey down. That is not enough for canonical quantisation of the primary field, and it is more than nothing.

### No Superposition

The eikonal is quadratic, so the sum of two solutions is not a solution: for two null gradients the norm of the sum is twice their polar form, which does not vanish. On 100 random pairs of complex null gradients normalised to $\sum_\mu\lvert g_\mu\rvert^2=1$ the smallest value of $\lvert N(g_1+g_2)\rvert$ was $0.063$ against a median of $0.96$, so the failure is generic and neither rare nor small. The solution set is not a vector space.

The cost is narrower than that sentence suggests, and the eikonal section says why. Every solution the programme constructs is harmonic, so the class sits **inside** a linear space, the solutions of $\Box\Sigma=0$, and the nonlinear condition is an algebraic selection within it. The harmonicity is a property of the constructed class and not of the eikonal: a function can solve the eikonal without being harmonic, and the mathematics article carries the witness. What fails is additivity of the class, not the existence of a linear ambient space. A formalism built on the harmonic space would have the right linearity; what it would not have is the assurance that a superposition of two states is a state.

That is still the deepest of the costs, because the corpus's quantum sector rests on the linearity of the state space and not merely on the availability of one. A primary equation that selects a nonlinear subset of a linear space does not contradict quantum mechanics, but it forbids taking the linear structure as primitive: on this reading the linear space is what the constraint is imposed on, not what generates it.

### The Real Slice Is Not Natural

The programme's rule for what counts as meaningful is invariance under the algebra automorphisms, $\mathrm{Aut}(\mathbb{B})\cong SO(3,\mathbb{C})$, and the Hermitian form is not invariant under them, so the programme calls the restriction to the real slice artificial. The corpus makes the quaternion conjugation primitive instead, with $\mathbb{B}_{\Psi}\oplus\mathbb{B}_{\Phi}$ as its fixed and anti-fixed spaces. The argument for the programme's side is in *The Algebrodynamical Programme*, §*The Induced Causal Minkowski Geometry with Phase*.

This is not a difference of taste: it is the point at which the two cannot both have the primitive object.

## The Fork: Product First or Conjugation First

The corpus's structure is built on the **quaternion conjugation** $\natural$, the $\mathbb{C}$-linear involution: it cuts the algebra into the material and the informational sectors, it gives the interval its signature, and it makes the two slots of one product physically different. That conjugation is not an algebra automorphism, and the corpus already knows what that means: *Frames, Rotations and the Lorentz Group* states that a boost preserves the interval and the sectors but not the product, and concludes that a boost is a motion and not a symmetry of the algebraic structure.

The derivation route is built on the **product** instead. Its derivative is defined by multiplication alone, its invariants are the automorphism invariants, and a structure that the product does not preserve is not a structure of the theory. The Hermitian form fails that test, so the real slice fails it, and the two sectors are, on this reading, an artefact of a coordinate choice.

That is not the end of the argument, and leaving it there would misrepresent the programme. The product-first route is not left without geometry: it **builds** an arena, from the one object the automorphisms do preserve. The construction is due to the source and is worked out in *The Algebrodynamical Programme*; it is summarized here because it decides what the fork is about.

The automorphism group $\mathrm{Aut}(\mathbb{B})\cong SO(3,\mathbb{C})$ fixes the trace of the matrix — the scalar part $z_0=\tfrac12(\upsilon+v)$ — and rotates the traceless part as a complex three-vector $z$. The one invariant of that rotation is the complex quadratic form

$$
\sigma=z_1^2+z_2^2+z_3^2 ,
$$

and its modulus obeys the Lagrange identity $\sigma\sigma^{*}=T^2-\lvert\vec X\rvert^2$ with

$$
T=\vec z\cdot\vec z^{*},\qquad \vec X=i\,[\vec z\times\vec z^{*}] ,
$$

both real. So the product-first route recovers a Minkowski-type interval, and it recovers it as an **identity** rather than as a postulate. Three features follow, and each is a physical consequence rather than a technicality. The interval is non-negative by construction, $T^2-\lvert\vec X\rvert^2=\lvert\sigma\rvert^2\ge0$, so the arena is the causal domain only: there is no spacelike-separated region. The time $T=\lvert\vec p\rvert^2+\lvert\vec q\rvert^2$ for $z=\vec p+i\vec q$ is positive definite, so the arena comes with a future and no past. And $\sigma$ has a **phase**, invariant under the same group, which has nowhere to live in the macro-geometry and therefore sits as a fibre coordinate over it — the programme's phase extension, and its candidate for the origin of the wave properties of matter.

### The Two Columns

| | Conjugation first | Product first, with the phase extension |
|---|---|---|
| Primitive | $\natural$, the split $\mathbb{B}_{\Psi}\oplus\mathbb{B}_{\Phi}$ | the product, its automorphisms and the complex three-vector |
| The real slice | the physical sector | induced, and only the causal domain |
| The Hermitian form | the probability form | outside the theory |
| What a boost is | a motion, not an automorphism | an automorphism of the three-vector, not of the algebra |
| The two sectors | material and informational | a coordinate artefact |
| The arena | Minkowski, assumed | Minkowski-type, derived: $S^2=T^2-\lvert\vec X\rvert^2\ge0$ |
| Time | a coordinate of either sign | $T=\vec z\cdot\vec z^{*}\ge0$, future only |
| Extra invariant | none | the phase $\alpha$ of $\sigma$, a fibre coordinate |

Neither column is refuted by the other, and this article does not choose between them. What it records is that the choice is narrower and more interesting than a choice between geometry and no geometry. Both routes produce a Minkowski-type arena; they differ in whether time carries a sign, whether the space outside the cone exists, and whether there is an internal phase. A derivation that keeps the product and loses the sectors is a derivation of a neighbouring theory that shares the algebra — but it is a theory with a metric, a causal structure, an arrow of time and one extra invariant, not a theory with nothing. The source itself calls the identification of $T$ and $\vec X$ with the Minkowski coordinates informal, and the corpus records the construction as the source's, with that qualification.

## Where the Two Agree

Three agreements are worth naming, because they are what makes the derivation worth pursuing inside this corpus rather than beside it.

**The same cone.** The characteristic set of the corpus's four-dimensional gradient is the zero-divisor cone, since the determinant of its symbol matrix is the norm, and the primary equation says the gradient lies on that cone. The two frameworks are built on the same quadratic form; they differ in degree, not in cone.

**The same twistor.** The general solution of the primary equation is generated, on the programme's account, by an arbitrary function of three components of a twistor, with the coordinate resolved from the incidence relation. *Twistor Theory and Biquaternions* writes that relation for a different purpose, the representation of massless fields. The object is shared; only its role differs.

**The same locus of states.** The null cone on which the gradient lives is the locus on which the corpus's pure states sit. A theory whose fields live on the state locus is not a foreign body in this corpus, whatever its vocabulary.

## Summary

The corpus derives its arena and imports its dynamics. The derivation route inverts the second half: one condition, the factorisation of the differential, and the field equations as its integrability conditions. The condition is that the gradient of every component of a differentiable function is a zero divisor; the eikonal is the coordinate form of that statement; the fields are the semi-derivatives; self-duality is the integrability condition; Maxwell and Yang–Mills are the Bianchi identities of the resulting curvature.

The gains are three: gauge equations without a gauge postulate, a fixed amplitude whose isolation is where the programme locates the origin of its discrete charge, and a singular locus that carries the field, the charge and the effective geometry at once. The costs are three: no action principle, so no canonical quantisation; no additivity, so no linear state space on the solution class, although the class sits inside one; and a real slice that the theory's own invariance rule does not preserve.

The last is the fork. Conjugation first gives the two sectors and the corpus's quantum reading, at the price of a structure the product does not preserve. Product first gives the derivation, and — carried through — an induced Minkowski-type arena with a positive-definite time and an invariant phase, at the price of the sectors. The two share the cone, the twistor and the locus of states, so they are not strangers; but they cannot both be fundamental, and the choice between them is the choice of what the biquaternion universe is a universe of.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra, isomorphic to $M_2(\mathbb{C})$ |
| $\mathbb{B}_{\Psi}$, $\mathbb{B}_{\Phi}$ | The informational and material sectors, the fixed spaces of ${}^{*}$ and $\flat$ |
| $\natural$ | The quaternion conjugation, $\mathbb{C}$-linear, fixing $\mathbb{B}_{H}$ |
| $\tilde\nabla$ | The biquaternionic gradient $\sum_\mu e_\mu\partial/\partial R_\mu$ |
| $N(\tilde Q)$ | The biquaternion norm $\sum_\mu Q_\mu^2$, zero on the cone |
| $\Sigma$ | One component of a differentiable function |
| $\mathsf D\Sigma$ | The two-by-two array of its four coordinate derivatives |
| $L$, $R$ | The left and right semi-derivatives in $dF=L\,dZ\,R$ |
| $Ξ$ | The left semi-derivative in the spinor splitting $d\eta=Ξ\,dZ\,\zeta$ |
| $\eta$, $\zeta$ | The two $SL(2,\mathbb{C})$-spinors of that splitting |
| $\Pi$, $G$ | The generating function and the projective coordinate it resolves |
| $F_{\mu\nu}$, $A_\mu$ | The curvature and the potential of the connection the condition carries |
| $q$ | The electric charge, $q=N/4$ in the programme's units, $N$ the winding number and not the norm |
| $\sigma$ | The automorphism invariant $z_1^2+z_2^2+z_3^2$ of the complex three-vector |
| $T$, $\vec X$ | The induced time $\vec z\cdot\vec z^{*}$ and space $i\,\vec z\times\vec z^{*}$ |
| $S$, $\alpha$ | The modulus and the phase of $\sigma$, the latter the fibre coordinate |

## Further Reading

- [The Two-Sided Derivative over the Biquaternion Algebra: Rank-One Gradients, the Complex Eikonal and the Linear Sector](../articles_maths/the-two-sided-derivative-over-the-biquaternion-algebra.html), the mathematical companion: the three definitions, the rank-one criterion, the eikonal and the comparison with the operator form.
- [The Algebrodynamical Programme: Nonlinear Cauchy–Riemann Conditions, Self-Quantized Charge, and Induced Causal Geometry](the-algebrodynamical-programme-nonlinear-cauchy-riemann-conditions-self-quantized-charge-and-induced-causal-geometry.html), for the generating system, the self-duality, the quantised charge and the induced geometry.
- [Null Electromagnetic Fields and the Shear-Free Congruence](null-electromagnetic-fields-and-the-shear-free-congruence.html), for Bateman's representation, the Mariot–Robinson theorem and the static null field.
- [The Celestial Sphere of the Null Cone: Null Directions, Chirality and the Phase](the-celestial-sphere-of-the-null-cone-null-directions-chirality-and-the-phase.html), for the sphere of null directions and the little-group phase.
- [Twistor Theory and Biquaternions](twistor-theory-and-biquaternions.html), for the incidence relation and the projective spinor ratio that the generating function is written in.
- [The Topology of the Zero-Divisor Cone](../articles_maths/the-topology-of-the-zero-divisor-cone.html), for the cone as a topological object and its Lorentzian slices.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html), for the postulate the derivation route replaces with a theorem.
- [Gauge Curvature and the Bianchi Identity in Biquaternionic Form](gauge-curvature-and-the-bianchi-identity-in-biquaternionic-form.html), for the Bianchi identity as a Jacobi identity and the form the field equations take.
- [The WKB Approximation and the Hamilton–Jacobi Equation in Biquaternionic Form](the-wkb-approximation-and-the-hamilton-jacobi-equation-in-biquaternionic-form.html), for the eikonal as the short-wavelength limit, the relation this article inverts.
- [Frames, Rotations and the Lorentz Group](frames-rotations-and-the-lorentz-group.html), for the statement that a boost is a motion and not an automorphism, which is the corpus's side of the fork.
- [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html), for the framework's own test of a structural hypothesis and its list of open questions.
