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
| The interval and the four-vectors of relativity | derived from $\mathbb{M}_-$ | *The Material Sector: Four-Vectors, Interval and Lorentz Action* |
| The Lorentz group and its action | derived as the norm-one group | *The Lorentz Group as Biquaternion Norm Automorphisms* |
| The state space and the Born form | derived from $\mathbb{M}_+$ | *The Informational Sector: States, Observables and Probability* |
| The Dirac equation | transcribed into the algebra | *The Dirac Equation in Biquaternionic Form* |
| The Maxwell equations | transcribed, or obtained from a biquaternion wave equation | *Nonlinear Maxwell Equations in Biquaternionic Form* |
| The gauge principle | postulated, with a ceiling on the group | *The Gauge Principle in Biquaternionic Form* |
| $\hbar$ | imported, nowhere derived | — |

The pattern is visible in one line: **the corpus derives the arena and imports the dynamics.** The interval, the group, the cone and the state space follow from the algebra; the equations of motion are written into it. The derivation route is an attempt to close that gap, and it closes it from the dynamics side rather than the kinematic one.

### Translation and Derivation Are Not Rivals

A translation is not wasted work when the derivation succeeds. The derivation produces *an* equation set; it must then be compared with the known one, and the comparison is only possible if the known one has already been written in the same algebra. The corpus's transcription articles are the dictionary that makes the derivation legible, and the derivation route is the test of whether the dictionary is a dictionary of one language or of two.

## The Primary Equation

### The Condition and Its Chain

The mathematics is in the companion article and is quoted here in one paragraph. A function of the biquaternion variable is called differentiable when its differential factorises, $dF=L\,dZ\,R$, and the definition takes no inverse, so neither the noncommutativity nor the zero divisors obstruct it. In the matrix model $\mathbb{B}\cong M_2(\mathbb{C})$ the condition says that for each component $\Sigma$ of $F$ the two-by-two array of its four coordinate derivatives has rank at most one, which is

$$
\det\Sigma_{;AB}=0,\qquad\text{equivalently}\qquad N(\nabla\Sigma)=0,
$$

and in Cartesian coordinates this is the complex eikonal

$$
\left(\frac{\partial\Sigma}{\partial z_0}\right)^2-\left(\frac{\partial\Sigma}{\partial z_1}\right)^2-\left(\frac{\partial\Sigma}{\partial z_2}\right)^2-\left(\frac{\partial\Sigma}{\partial z_3}\right)^2=0 .
$$

The biquaternion gradient of every component is a zero divisor of the algebra. That is the whole of the primary input.

Everything else is a consequence, and the chain is short. The gradient is null, so it defines a direction field; the direction field is a null congruence; the congruence is shear-free and geodesic; a null congruence of that kind is the principal direction of a null electromagnetic field; and the integrability of the over-determined system that generates the congruence forces the self-duality of its curvature, whose Bianchi identity is Maxwell's equation for the trace part and the Yang–Mills equation for the trace-free part. The generating system, the self-duality and the identification of the Bianchi identity with the field equations are *The Algebrodynamical Programme*, worked out there in detail; the congruence side is *Null Electromagnetic Fields and the Shear-Free Congruence*.

### The Eikonal as Primary, and the Inversion of the WKB Relation

The corpus already contains the eikonal, in a different role. *The WKB Approximation and the Hamilton–Jacobi Equation in Biquaternionic Form* derives it as the short-wavelength limit of the linear wave equation: the phase of a rapidly oscillating solution obeys it approximately, and the approximation improves as the wavelength shrinks. In the derivation route the relation is inverted. The eikonal is **exact and primary**, and the linear wave equation is what the *derivatives* of its solution obey. Two statements, one arrow each way, and the corpus must hold both: the WKB reading is a theorem about a limit, the derivation reading is a postulate about what is fundamental. They are compatible, and the compatibility is the reason the inversion is worth taking seriously rather than dismissing as a change of subject.

### The Fields as Semi-Derivatives

What plays the role of the field is not $\Sigma$ but the multiplier. The spinor splitting of the condition writes the function as a pair of spinors and the condition as

$$
d\eta=\Phi\,dZ\,\xi ,
$$

with $\Phi$ transforming as a complex four-vector and $\eta,\xi$ as $SL(2,\mathbb{C})$-spinors. The system is eight differential equations for six unknown functions, so it is **over-determined**, and $\Phi$ — the left semi-derivative — carries the gauge field. Differentiating the equation and using it again gives an integrability condition whose object is a connection; requiring the curvature to annihilate the non-trivial spinor forces its self-dual part to vanish, and the Bianchi identity then delivers the field equations.

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

### A Fixed Scale, and Where Discreteness Can Come From

The scale question is the one place where the derivation has real physical content, and it must be stated with more care than it usually is.

**The eikonal alone is scale covariant.** Its condition is homogeneous of degree two in the gradient, so a component may be multiplied by any constant and the condition survives. Verified on the polar form: $N(\lambda g)=\lambda^2N(g)$ for every complex $\lambda$. Nothing about a single component's amplitude is fixed by differentiability.

**The connection is not.** The curvature of a connection is $dA+[A,A]$, one term linear in the potential and one quadratic in it. Scaling the potential therefore does not scale the curvature:

$$
F(\lambda A)=\lambda\,F(A)+(\lambda^2-\lambda)\,[A,A] .
$$

The two terms scale differently, so the self-duality relation $F=iF^{*}$ selects $\lambda=1$ whenever the commutator does not vanish.

**That is where a discrete charge can come from, and it is not a quantum assumption.** A linear theory cannot prefer one amplitude, because its solution space is a vector space and every multiple of a solution is a solution. A theory whose field equations contain a quadratic term can, and does: the admissible potentials come in a discrete set of scales, and the programme's value $q=N/4$ is the expression of that discreteness in its own units. The mechanism is not $\hbar$; nothing in the algebra knows about $\hbar$. It is the failure of scale covariance of the connection, and that failure is a property of the algebra's product.

### Singularities That Carry the Particle Data

The singular locus of a solution is the branch set of the generating function, $\Pi_G=0$, and it is simultaneously the singularity of the semi-derivative, of the electromagnetic field and of the effective geometry. One locus, three readings, which is the programme's answer to why the particle's charge, its field and its gravitational effect have a common origin. The reading is the programme's and the corpus records it as such; what belongs here is only that the derivation route produces the coincidence rather than assuming it.

## What It Costs

### No Action Principle

The generating system is over-determined, eight equations for six unknowns, and an over-determined system has no free initial data and no variational principle of the usual kind. A Lagrangian is what canonical quantisation needs, and the corpus's quantisation articles — *Canonical Quantization of the Biquaternion Graviton Field*, *The Path Integral in Biquaternionic Form* — presuppose one. The derivation route buys its explanatory power at the price of the method by which the rest of the corpus quantises. Any quantisation of it must be a quantisation of a constrained system, and the programme itself says that this requires new methods.

### No Superposition

The eikonal is quadratic, so the sum of two solutions is not a solution: for two null gradients the norm of the sum is twice their polar form, which does not vanish. On 100 random pairs of complex null gradients the smallest value of $\lvert N(g_1+g_2)\rvert$ was $1.54$, so the failure is generic and not an accident of measure. The solution set is not a vector space, there is no Hilbert space of solutions to build on, and the linearity of the quantum formalism has to be recovered from something else rather than read off the equation.

This is the deepest of the costs, because the corpus's whole quantum sector rests on the linearity of the state space. A nonlinear primary equation does not contradict quantum mechanics — the linear equation can be its derived sector, for the derivatives — but it forbids taking the linear structure as the primitive one.

### The Real Slice Is Not Natural

The programme's own rule for what counts as meaningful is invariance under the algebra automorphisms, $\mathrm{Aut}(\mathbb{B})\cong SO(3,\mathbb{C})$, and the Hermitian form is not invariant under them. The programme draws the conclusion and calls the restriction to the real slice artificial. The corpus draws the opposite conclusion and makes the natural conjugation primitive, with $\mathbb{M}_+\oplus\mathbb{M}_-$ as its fixed and anti-fixed spaces.

This is not a difference of taste; it is the one point at which the two cannot both be right, and it is treated next.

## The Fork: Product First or Conjugation First

The corpus's structure is built on the **natural conjugation** $\natural$, the $\mathbb{C}$-linear quaternion conjugation: it cuts the algebra into the material and the informational sectors, it gives the interval its signature, and it makes the two slots of one product physically different. That conjugation is not an algebra automorphism, and the corpus already knows what that means: *Frames, Rotations and the Lorentz Group* states that a boost preserves the interval and the sectors but not the product, and concludes that a boost is a motion and not a symmetry of the algebraic structure.

The derivation route is built on the **product** instead. Its derivative is defined by multiplication alone, its invariants are the automorphism invariants, and a structure that the product does not preserve is not a structure of the theory. The Hermitian form fails that test, so the real slice fails it, and the two sectors are, on this reading, an artefact of a coordinate choice.

| | Conjugation first | Product first |
|---|---|---|
| Primitive | $\natural$, the split $\mathbb{M}_+\oplus\mathbb{M}_-$ | the product and its automorphisms |
| The real slice | the physical sector | not an invariant object |
| The Hermitian form | the probability form | outside the theory |
| What a boost is | a motion, not an automorphism | not a symmetry of the structure |
| The two sectors | material and informational | a coordinate artefact |

Neither column is refuted by the other, and this article does not choose between them. What it records is that the choice determines whether the corpus's central object — the real slice and its two readings — survives the derivation. A derivation that keeps the product and loses the sectors is not a derivation of the biquaternion universe; it is a derivation of a neighbouring theory that happens to share the algebra.

## Where the Two Agree

Three agreements are worth naming, because they are what makes the derivation worth pursuing inside this corpus rather than beside it.

**The same cone.** The characteristic set of the corpus's operator $\tilde\nabla$ is the zero-divisor cone, since the determinant of its symbol matrix is the norm, and the primary equation says the gradient lies on that cone. The two frameworks are built on the same quadratic form; they differ in degree, not in cone.

**The same twistor.** The general solution of the primary equation is generated by an arbitrary function of three twistor components, with the coordinate resolved from the incidence relation. The corpus's twistor article writes the same incidence relation for a different purpose. The object is shared; only its role differs.

**The same locus of states.** The null cone on which the gradient lives is the locus on which the corpus's pure states sit. A theory whose fields live on the state locus is not a foreign body in this corpus, whatever its vocabulary.

## Summary

The corpus derives its arena and imports its dynamics. The derivation route inverts the second half: one condition, the factorisation of the differential, and the field equations as its integrability conditions. The condition is that the gradient of every component of a differentiable function is a zero divisor; the eikonal is the coordinate form of that statement; the fields are the semi-derivatives; self-duality is the integrability condition; Maxwell and Yang–Mills are the Bianchi identities of the resulting curvature.

The gains are three: gauge equations without a gauge postulate, a fixed scale whose failure of scale covariance is where a discrete charge can come from, and a singular locus that carries the field, the charge and the effective geometry at once. The costs are three: no action principle, so no canonical quantisation; no superposition, so no linear state space; and a real slice that the theory's own invariance rule does not preserve.

The last is the fork. Conjugation first gives the two sectors and the corpus's quantum reading, at the price of a structure the product does not preserve. Product first gives the derivation, at the price of the sectors. The two share the cone, the twistor and the locus of states, so they are not strangers; but they cannot both be fundamental, and the choice between them is the choice of what the biquaternion universe is a universe of.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra, isomorphic to $M_2(\mathbb{C})$ |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | The informational and material sectors, the fixed spaces of ${}^{*}$ and $\flat$ |
| $\natural$ | The natural conjugation, $\mathbb{C}$-linear, fixing $\mathbb{H}_{\mathbb{B}}$ |
| $\tilde\nabla$ | The biquaternionic gradient $\sum_\mu e_\mu\partial/\partial Q_\mu$ |
| $N(\tilde Q)$ | The biquaternion norm $\sum_\mu Q_\mu^2$, zero on the cone |
| $\Sigma$ | One component of a differentiable function |
| $\Sigma_{;AB}$ | The two-by-two array of its four coordinate derivatives |
| $L$, $R$ | The left and right semi-derivatives in $dF=L\,dZ\,R$ |
| $\Phi$ | The left semi-derivative in the spinor splitting $d\eta=\Phi\,dZ\,\xi$ |
| $\eta$, $\xi$ | The two $SL(2,\mathbb{C})$-spinors of that splitting |
| $\Pi$, $G$ | The generating function and the projective coordinate it resolves |
| $F_{\mu\nu}$, $A_\mu$ | The curvature and the potential of the connection the condition carries |
| $q$ | The electric charge, $q=N/4$ in the programme's units |

## Further Reading

- [The Two-Sided Derivative over the Biquaternion Algebra: Rank-One Gradients, the Complex Eikonal and the Linear Sector](../articles_maths/the-two-sided-derivative-over-the-biquaternion-algebra.html), the mathematical companion: the three definitions, the rank-one criterion, the eikonal and the comparison with the operator form.
- [The Algebrodynamical Programme: Nonlinear Cauchy–Riemann Conditions, Self-Quantized Charge, and Induced Causal Geometry](the-algebrodynamical-programme-nonlinear-cauchy-riemann-conditions-self-quantized-charge-and-induced-causal-geometry.html), for the generating system, the self-duality, the quantised charge and the induced geometry.
- [Null Electromagnetic Fields and the Shear-Free Congruence](null-electromagnetic-fields-and-the-shear-free-congruence.html), for Bateman's representation, the Mariot–Robinson theorem and the static null field.
- [The Celestial Sphere of the Null Cone: Null Directions, Chirality and the Phase](the-celestial-sphere-of-the-null-cone-null-directions-chirality-and-the-phase.html), for the sphere of null directions and the little-group phase.
- [The Topology of the Zero-Divisor Cone](../articles_maths/the-topology-of-the-zero-divisor-cone.html), for the cone as a topological object and its Lorentzian slices.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html), for the postulate the derivation route replaces with a theorem.
- [Gauge Curvature and the Bianchi Identity in Biquaternionic Form](gauge-curvature-and-the-bianchi-identity-in-biquaternionic-form.html), for the Bianchi identity as a Jacobi identity and the form the field equations take.
- [The WKB Approximation and the Hamilton–Jacobi Equation in Biquaternionic Form](the-wkb-approximation-and-the-hamilton-jacobi-equation-in-biquaternionic-form.html), for the eikonal as the short-wavelength limit, the relation this article inverts.
- [Frames, Rotations and the Lorentz Group](frames-rotations-and-the-lorentz-group.html), for the statement that a boost is a motion and not an automorphism, which is the corpus's side of the fork.
- [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html), for the framework's own test of a structural hypothesis and its list of open questions.
