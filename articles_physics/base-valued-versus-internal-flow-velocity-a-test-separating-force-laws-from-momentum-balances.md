# __Base-Valued versus Internal Flow Velocity: A Test Separating Force Laws from Momentum Balances__

## Introduction

Five rungs of this corpus derive a fluid, and four of them end with a force law while the fifth ends with a momentum balance. The difference is not a matter of effort or of how far the derivation was pushed. **It is decided at the first line of the derivation, by a property of the velocity the rung supplies, and the test that decides it takes one question to state.**

**The question.** Is the fluid's velocity *a single vector of the base*, or is it *a family of internal elements indexed by the base's directions*? At the gradient rungs the velocity is $\vec\nabla_{\Phi}S/m$: one vector, an element of the material sector's tangent space at each point. At the frame rungs it is $A_{\imath}/\varrho$ or $ic\tilde U_{\Psi,\mathrm b}^{-2}$: one direction, again an element of the base. At the matrix rung it is $\Omega_{\imath}=U_{\mathrm{frm}}^{\dagger}D_{\imath}U_{\mathrm{frm}}$, and there is no single vector to point at — there are four, one for each base direction, and each of them takes values in $\mathfrak{u}(4)$ and not in the base.

**Why that matters, in one sentence.** A force law is an equation for the acceleration of a trajectory, and a trajectory needs a tangent vector to be differentiated along; an internal velocity supplies no tangent vector, so the equation it produces relates a momentum's divergence to a curvature and is not an equation for an acceleration. **The article's claim is that this single structural fact, and nothing else, separates a force law from a momentum balance in this corpus.**

**What the article is not.** It is not a claim that the matrix rung's fluid is a weaker fluid. A balance is a law of a different kind, not a law of lesser rank, and the article argues this at length because the corpus's own vocabulary — "a fluid *on* the material sector and not *in* it" — can be read as a demotion. It is not one. **The corpus's statement is a location, and the article's job is to make the location precise enough to be tested.**

**The step this article is.** It is S5 of [Five Steps from a Lagrangian to Fluid Equations](five-steps-from-a-lagrangian-to-fluid-equations.html). S4 manufactured the acceleration slot and left open what kind of equation fills it; S5 reads the answer off the velocity's provenance. **S4 asks whether a spare derivative exists; S5 asks where the derivative is taken.** A rung can pass S4 and produce a balance, and the matrix rung is the case.

## Conventions

The base is the material sector $\mathbb{B}_{\Phi}$ with its gradient $\partial_{\imath}$, $\imath\in\{t,x,y,z\}$. The fibre is whatever the rung's word puts over the base: a phase circle at the scalar rungs, a frame at the spinor and vector rungs, an $\mathrm{SU}(4)$ frame at the matrix rung. The conventions are [The Two Sectors](the-two-sectors-the-hermitian-split-and-the-four-bridges.html) and [The Algebraic Vocabulary](the-algebraic-vocabulary-element-conjugations-six-subspaces-and-two-ledgers.html).

**A base vector is a section of $T\mathbb{B}_{\Phi}$:** at each point $x$ it assigns one element of the tangent space at $x$, and it can be differentiated along itself. **An internal element is a section of a bundle whose fibre is an algebra:** at each point it assigns one algebra element, and its derivative along a base direction is a covariant derivative on the fibre.

**A connection is neither, and it is the object the article has to place.** A connection $\Omega_{\imath}$ assigns one algebra element *per base direction*, so it is a one-form with values in the algebra. **It is not a base vector — it has four components where a base vector has one — and it is not an internal element either, because its index is a base index.** It is the object that tells you how the fibre's frame changes as you move, and its values are the changes. **The article's whole subject is the consequence of that distinction for the equation the fluid produces.**

**The two verdicts, named once.** A *force law* is an equation of the form $a^{\imath}=F^{\imath}/m$ — an acceleration equated to a force, with the acceleration a derivative along a base vector. A *momentum balance* is an equation of the form $\partial_{\jmath}\Pi^{\jmath\imath}=\mathcal F^{\imath}$ — a divergence of a flux equated to a source, with no trajectory anywhere in it. **Both are equations of motion; only the first is an equation for a worldline.**

## The Test, Stated Precisely

**The test has two clauses, and a rung passes the second only if it passes the first.** The article states them separately because the corpus's shorthand — "*in* the base or *on* it" — fuses them and the fusion hides which clause a rung fails.

| clause | the question | what passing means |
| --- | --- | --- |
| **first** | does the rung supply a *distinguished* base vector to be the flow? | the velocity is one vector field, not a family indexed by directions |
| **second** | is the velocity's value at each point an element of the base's tangent space? | the velocity can be differentiated along itself |

**The first clause is the one that fails at the matrix rung, and the failure is structural.** $\Omega_{\imath}$ is indexed by $\imath$; there are four of them; and no combination of them is distinguished by the rung. **The rung has no flow direction, only a set of base directions.** A velocity that is a family indexed by the same index as the derivative cannot be differentiated along itself, because "along itself" would require choosing one member of the family as *the* direction, and the rung does not choose.

**The second clause is the one that fails for any internal velocity, and it is the one the corpus's shorthand names.** Even if a rung chose a flow direction, an internal value at each point is not a tangent vector, so the derivative along the flow would be a covariant derivative on the fibre and not a directional derivative on the base. **The two clauses fail together at the matrix rung, and the article separates them because a future rung could fail only one.**

**What the test does not ask.** It does not ask whether the rung is non-abelian, whether the fibre is trivial, whether the group is compact, or how many internal indices the velocity carries. **Those are properties of the fibre, and the test is about the base.** A rung with a large non-abelian fibre and a base-valued velocity passes; a rung with a one-dimensional abelian fibre and an internal velocity fails. The next section makes that concrete with the corpus's own two examples.

## Three Encodings, Three Verdicts

**The corpus's five rungs encode the velocity three ways, and each encoding passes or fails the test for a reason visible in the encoding.**

| rung | the velocity | a distinguished base vector? | a base-valued value? | the verdict |
| --- | --- | --- | --- | --- |
| Schrödinger, Klein–Gordon | $\vec\nabla_{\Phi}S/m$, $\partial_{\imath}S/m$ | **yes**, the gradient | **yes** | force law |
| Dirac, Proca | $ic\tilde U_{\Psi,\mathrm b}^{-2}$, $A_{\imath}/\varrho$ | **yes**, the frame's direction | **yes** | force law |
| $\mathrm{SU}(4)$ | $\Omega_{\imath}=U_{\mathrm{frm}}^{\dagger}D_{\imath}U_{\mathrm{frm}}$ | **no**, four members, none distinguished | **no** | momentum balance |

**The gradient rungs pass both clauses because a gradient of a scalar is a vector.** $\vec\nabla_{\Phi}S$ is one vector field, distinguished by being the gradient of the action, and it is tangent to the base. **Its direction is the flow, and the flow's direction is the velocity's own direction** — which is the degenerate case that makes the material derivative possible: $\vec v\cdot\vec\nabla_{\Phi}$ is a derivative along $\vec v$ because $\vec v$ is a base vector.

**The frame rungs pass both clauses because a direction is a vector.** $A_{\imath}/\varrho$ is a unit vector at each point, distinguished by the field, and tangent to the base. **The velocity is a direction rather than a gradient, and that is why the manufacturing at these rungs is a projection rather than a differentiation** — there is no scalar whose gradient is the velocity, so there is nothing to differentiate — **but the test's verdict is the same, because the direction is a base vector.** The article stresses this: a rung can pass S5 and still manufacture its acceleration law by projection, because S5 is about *where* the velocity lives and not about *how* the law is obtained.

**The matrix rung fails both clauses, and the failure is not a defect of the derivation.** $\Omega_{\imath}$ has a base index and an algebra value. **Its four members are the four base directions' worth of frame change, and none of them is distinguished** — the frame's eigenvalue decomposition picks no direction in the base. **So the rung has a connection and not a velocity**, and its fluid's "velocity" is a name for the connection. The corpus's phrase for this is exact: the fluid is *on* the material sector — its variables are functions on the base — and not *in* it — they are not tangent to the base.

## Why an Internal Velocity Has No Material Derivative

**The material derivative is the test's whole content made explicit, and it is worth writing out because its absence is what a balance is.** For a base-valued velocity $u^{\imath}$, the material derivative of any quantity $\mathcal Q$ is

$$
\frac{\mathrm{D}\mathcal Q}{\mathrm{D}\tau}=u^{\imath}\partial_{\imath}\mathcal Q ,
$$

and it exists because $u^{\imath}$ is a vector: the contraction eats the index. **The acceleration is $\mathrm{D}u^{\imath}/\mathrm{D}\tau$, and a force law is the statement that it equals a force over a mass.** Every word in that sentence requires $u$ to be a base vector.

**Run the construction with $\Omega_{\imath}$ and see where it stops.** The nearest analogue of the acceleration is $u^{\jmath}\partial_{\jmath}\Omega_{\imath}$. **But there is no $u$.** The only velocity-like object in the rung is $\Omega$ itself, and contracting $\Omega$ with $\partial$ would require choosing one of its four members as the direction — which is exactly the choice the rung does not make. **The construction stops at the first symbol, and it stops for a reason that is not repairable by a better choice of notation.**

**The honest repair, and why it does not give a law.** One *can* write $\Omega^{\jmath}D_{\jmath}\Omega_{\imath}$ — contract the base index of the connection with the covariant derivative. **The result is not a material derivative**: it contracts a one-form with a covariant derivative and produces a two-form, its meaning is a curvature's derivative rather than a trajectory's acceleration, and it carries no trajectory. **Calling it an acceleration would be a naming, not a derivation**, and the corpus does not make the naming.

**What the rung has instead, stated as the balance it is.** The matrix rung's manufactured equation is

$$
\partial_{\jmath}\Pi^{\jmath}{}_{\imath,kl}=\bigl[\text{curvature}\bigr]_{kl}+\bigl[\text{transport}\bigr]_{kl}+\Omega_{kl}\,\partial_{\imath}q_{kl},
$$

a divergence of a matrix-valued flux equated to a matrix-valued source. **It is a conservation law for the fibre's momentum, and it holds at every point.** A force law would say how a *test trajectory* accelerates; the balance says how the field's momentum is transported. **The two answer different questions and neither implies the other.**

**The structural reason there is no trajectory, stated once and at the level of the rung.** A trajectory is a curve in the base, and its tangent vector is a base vector. **The matrix rung's fluid has no curve because it has no flow: the word decomposes the field into a frame and four densities, and neither carries a preferred direction in the base.** The dynamics of the frame is a rotation of the fibre as you move, and a rotation has no direction. **A fluid without a direction cannot have streamlines, and a fluid without streamlines cannot have an acceleration along them.**

## The Discriminator Is Not Abelian-ness

**The natural hypothesis — force laws are abelian, balances are non-abelian — is false, and the corpus has the counterexample in its own pages.** Wong's equations describe a particle with an $\mathrm{SU}(2)$ charge moving on the base, and they are a force law: $\dot u^{\imath}=g\,Q^{a}F^{a\imath}{}_{\jmath}u^{\jmath}$ with $\dot Q^{a}$ given by the bracket. **Non-abelian, and a law, because the velocity $u$ is a base vector and only the charge is internal.**

**The mirror-image counterexample is a $\mathrm{U}(1)$ connection and it is in the corpus's electromagnetism category.** A $\mathrm{U}(1)$ connection $A_{\imath}$ is an internal velocity in the article's sense: one algebra element per base direction, values in $\mathfrak{u}(1)$. **Its equation is $\partial_{\nu}F^{\nu\mu}=j^{\mu}$ — a balance — and not a force law.** Abelian, and a balance, because the velocity is internal.

| | base-valued velocity | internal velocity |
| --- | --- | --- |
| **abelian fibre** | a charged dust with a $\mathrm{U}(1)$ charge: **force law** | the $\mathrm{U}(1)$ connection itself: **balance** |
| **non-abelian fibre** | a particle with an $\mathrm{SU}(2)$ charge, Wong's equations: **force law** | the $\mathrm{SU}(4)$ frame's connection: **balance** |

**The table is the article's central negative result, and it is a two-by-two with the discriminator on the horizontal axis only.** Reading down a column fixes the verdict and varies the group; reading across a row varies the verdict and fixes nothing but where the velocity lives. **The horizontal axis decides, the vertical axis does not.**

**The corpus's own wording says exactly this, and the article is making it precise rather than correcting it.** [The Primordial Force Law](the-primordial-force-law-and-the-two-wong-terms.html) lists four differences between the primordial fluid's law and Wong's, and the deepest is the one this article names: in Wong's equations the velocity is a vector on the base and the charge is a matrix in the fibre; in the primordial fluid the velocity *is* the matrix. **A matrix velocity is not a vector velocity with extra indices; it is a different kind of object, and the kind is what decides the verdict.**

**The one thing the two-by-two must not be read as claiming.** It does not say that an internal velocity's equation is "really" a force law in disguise, or that a base-valued velocity's equation is "really" a balance. **It says the two equations have different logical forms**, and the forms are the ones the corpus displays. A reader who wants to relate them — the balance as the field-theoretic statement and the law as its probe limit — will find that relation in the electromagnetism articles, and it is a relation between two equations and not an identity of one with the other.

## What Each Verdict Buys

**A force law buys trajectories, and with them the whole classical vocabulary.** A mass shell, a conserved energy per worldline, a conserved momentum per worldline, and the notion of a test particle. **The gradient and frame rungs' fluids are fluids in the classical sense**: their Euler equations are equations for streamlines, and a streamline is a worldline. [The Euler and Continuity Equations](the-euler-and-continuity-equations-in-biquaternionic-form.html) is the corpus's statement of what that vocabulary carries.

**A balance buys a conservation law per point, and with it the whole field-theoretic vocabulary.** A conserved stress, a conserved momentum density, and the statement that the fibre's momentum is transported and not created except by curvature. **The matrix rung's fluid is a fluid in the field-theoretic sense**: it has densities, fluxes and sources, and it has no streamlines because it has no direction. **It is not less than a fluid; it is a fluid of a different kind**, and the corpus's ladder table records it as such rather than as an incomplete entry.

**The honest asymmetry, which the article does not paper over.** A force law determines a trajectory given initial data; a balance determines a field given initial data and boundary conditions. **The two are different kinds of prediction**, and a reader who asks "which rung predicts more" is asking a question with no answer until the comparison is made prediction by prediction. **The article's claim is only about logical form.**

**What a rung loses by being internal, stated as narrowly as the corpus states it.** It loses the material derivative, and with it the acceleration slot as an equation for a rate. **The six slots of a fluid survive** — density, flow, pressure, vorticity, continuity, acceleration — **but the acceleration slot's content is a balance's divergence and not a trajectory's rate.** That is what [Criterion for a Fluid Equation](criterion-for-a-fluid-equation-one-polar-coordinates-euler-lagrange-equation.html) means by saying that the slots are read and not all varied, and it is why the matrix rung is a fluid and not a failure to be one.

## The Corpus's Instance, Stated Plainly

**The matrix rung is the corpus's one internal-velocity fluid, and everything the article has said abstractly is visible in it.** The word is $\Xi=U_{\mathrm{frm}}PU_{\mathrm{frm}}^{\dagger}$ with $P=\mathrm{diag}(\rho_{1},\dots,\rho_{4})$; the fluid's densities are the four eigenvalues; the fluid's "velocity" is $\Omega_{\imath}=U_{\mathrm{frm}}^{\dagger}D_{\imath}U_{\mathrm{frm}}\in\mathfrak{u}(4)$; and the manufactured equation is the pair's momentum balance.

**Why the eigenvalues cannot supply the flow, which is the natural objection.** The four densities are scalars, so a gradient of one of them is a base vector, and a reader may ask why *that* is not the velocity. **The answer is that no one of them is distinguished**: the four are symmetric under the frame's permutations, the rung's algebraic term is symmetric in them up to the splitting the corpus records, and choosing one would be a choice the rung does not make. **A gradient of a symmetric function of the four is a base vector, and it is not the fluid's velocity — it is the direction in which the symmetric function changes.** The distinction is the first clause of the test in its sharpest form: a distinguished base vector is one the rung chooses, and the rung chooses none.

**Why the frame cannot supply a flow direction either, and this is the subtler half.** The frame is an $\mathrm{SU}(4)$ element, and an $\mathrm{SU}(4)$ element has no preferred vector — its action on the four-dimensional space is a rotation, and a rotation has no axis in four dimensions the way a rotation in three does. **So the frame's own structure supplies no direction, and the connection it generates is the closest thing to a velocity the rung has.**

**The corpus's phrase for the result, quoted exactly.** The primordial fluid is "a fluid *on* the material sector and not *in* it." **The article's contribution is to say what *on* and *in* mean**: *on* because the frame and the densities are functions of the base point, so the fluid's variables live over the base; *not in* because none of them is a vector of the base, so the fluid has no direction and its equation is a balance.

**What the phrase does not mean, and this is the article's warning.** *On* is not a demotion. The matrix rung's balance is the strongest statement the corpus makes about the primordial fluid's dynamics — it is the equation the whole primordial-force block is built around — and it is a balance because the physics is a balance. **A reader who reads "not in" as "not really a fluid" has read the location as a verdict**, and the two are different.

## Objections

**"An internal velocity is a fiction; the real velocity is whatever moves the energy."** The objection is worth taking seriously because it is the standard intuition. **The answer is that the energy flux at the matrix rung is a matrix-valued object too**: $\Pi_{\imath,kl}$ carries the pair index, and there is no energy current that is a base vector and no other. **The fiction objection assumes a base-valued energy flux exists and the internal velocity is a stand-in for it; at this rung it does not exist.** The article's test is therefore not a choice of variables but a statement about what the rung contains.

**"Then the matrix rung should be described without the word 'velocity' at all."** This is a fair objection and the corpus's answer is that the word is retained with its meaning narrowed: **the velocity is the object that enters the transport terms, and at the matrix rung that object is a connection.** Dropping the word would lose the ladder's uniformity; keeping it without the narrowing would claim a force law. **The corpus keeps it and narrows it, and this article is the narrowing.**

**"Does the test depend on the coordinate chart?"** No: the first clause asks whether a distinguished base vector exists, and the second asks whether the value is tangent to the base. **Both are chart-independent statements about the bundle**, which is why the test can be applied before any chart is chosen. The word's singular locus does not affect the verdict either — the test is about the velocity's *type*, not about where the type is well defined.

**"Is the diagnosis falsifiable?"** Yes, in the following sense. **If a rung were found whose velocity is internal and whose equation is nevertheless an equation for a trajectory, the test would be refuted.** The article knows of none, and the corpus's five rungs are consistent with it. **A rung whose velocity is base-valued and whose equation is a balance would refute it in the other direction**, and the article knows of none of those either. The test is a claim about the corpus's five rungs and a conjecture about others; the article labels it as such.

**"Why not simply say that the matrix rung's equation has no material derivative because the group is non-abelian?"** Because the two-by-two table refutes it, and because the reason is visible in the object: $\Omega_{\imath}$ fails to be a velocity at the *index* level, before any group structure is used. **A $\mathrm{U}(1)$ connection fails the same way for the same reason**, and it is abelian. The group's size is irrelevant to the diagnosis.

## What This Article Does Not Claim

**That a momentum balance is a defective force law.** The article's central caution is that the two are different logical forms, and a balance is the correct form at a rung with no flow. **The corpus's ladder is not a ranking.**

**That the test is a theorem.** It is a diagnosis that agrees with the corpus's five rungs and with the two-by-two table's four cells. A sixth rung could fail it, and the article says what would refute it.

**That a non-abelian charge makes an equation a balance.** The table's vertical axis is inert; the article states this twice because the confusion is the natural one and because the corpus's own phrasing about Wong's equations could be misread as making the group decisive.

**That the matrix rung's fluid has no velocity in any sense.** It has a velocity in the narrowed sense — the object in the transport terms — and the article's claim is that this object is a connection and not a vector. **The word is kept; the meaning is narrowed.**

**That the eigenvalues supply no dynamics.** They do: their equation is second order and sourced. What they do not supply is a *direction*, and the article separates the two statements because "the eigenvalues are dynamic" and "the eigenvalues give the flow" are different claims and only the first is true.

**That the balance's three terms are settled here.** The curvature, transport and product-rule assignments are [The Primordial Force Law's](the-primordial-force-law-and-the-two-wong-terms.html), and this article uses them without re-deriving them.

## Open Questions

**Is there a rung that passes the first clause and fails the second?** That would be a rung with a distinguished base direction whose velocity's value is nevertheless internal — a field that singles out a direction in the base but whose flow lives in the fibre. **The corpus has no such rung, and the article's clause structure exists to make the possibility statable.** If one were found, the article's verdict rule — "fails either clause, balance" — would predict a balance, and whether that prediction is right is untested.

**Can an internal velocity be *induced* to a base vector by a background?** A background that breaks the base's symmetry — a preferred frame, a condensate with a gradient — would single out a direction. **Whether the matrix rung's fluid would then acquire a material derivative, or only acquire a preferred index without a trajectory, is not settled.** The distinction matters because it separates "no direction exists" from "no direction is chosen".

**Does the verdict survive a coupling to a base-valued sector?** A matrix-rung fluid coupled to a charged dust would have a base-valued velocity available from the dust. **Whether the matrix rung's equation then becomes a law for the dust's worldlines — or stays a balance with a source — is a question about the coupled system** and the corpus does not have the computation.

**Is the six-slot count still the right count for an internal fluid?** The article says the six slots survive with the acceleration slot's content changed. **A stricter reading would say the vorticity slot also changes**, because vorticity is a property of a flow and an internal fluid has none. The corpus's criterion article counts six at every rung, and the article does not challenge the count; it flags that the count's justification at the internal rung is thinner than at the others.

## What This Article Adds and What It Relabels

**Adds.** The test as a **two-clause question** — a distinguished base vector, and a base-valued value — with the explicit statement that the matrix rung fails the first for a structural reason and the second for a definitional one; the **connection as the third kind of object**, neither a base vector nor an internal element, which is what an "internal velocity" actually is; the **two-by-two table** with the discriminator on the horizontal axis and the explicit statement that the group's size is inert; the **Wong and $\mathrm{U}(1)$-connection pair** as the two mirror-image counterexamples, drawn from the corpus's own pages; the **repair that fails** — contracting the connection with a covariant derivative produces a two-form and not an acceleration — stated so that the negative result is a derivation and not an assertion; and the **falsification conditions** in both directions.

**Does not add.** No new equation. The balance is the primordial force law's, the two-by-two's entries are Wong's and Maxwell's, and the six-slot count is the criterion's.

**Relabels.** *"A fluid on the material sector and not in it"* — made precise as two clauses and located in the bundle rather than in the vocabulary. *"Wong's equations differ from the primordial force law in four ways"* — with the deepest identified as the velocity's provenance, which is the only one of the four that decides the verdict. *"The matrix rung's fluid has no Euler equation"* — true, and the reason is not that the derivation stopped but that the rung has no direction to have an Euler equation along.

## Summary

**Whether a rung's fluid ends in a force law or a momentum balance is decided by where its velocity lives, and the test takes two questions.** Is there a distinguished base vector to be the flow? Is the velocity's value at each point tangent to the base? **The gradient and frame rungs answer yes twice and end in force laws. The matrix rung answers no twice and ends in a balance.**

**The object at the matrix rung is a connection, not a velocity.** It assigns one algebra element per base direction, so it has no single direction and cannot be differentiated along itself. **The material derivative $u^{\imath}\partial_{\imath}$ does not exist there**, and its absence — not any property of the group — is what makes the manufactured equation a divergence of a flux rather than an acceleration.

**The discriminator is not abelian-ness.** Wong's $\mathrm{SU}(2)$ equations are a law with a matrix charge; a $\mathrm{U}(1)$ connection's equation is a balance with a scalar one. **The horizontal axis of the two-by-two decides and the vertical axis does not**, and the corpus's own four differences between the primordial law and Wong's contain this one as the deepest.

**A balance is a law of a different kind and not a weaker one.** A force law determines a trajectory; a balance determines a field. **The matrix rung's fluid has densities, fluxes and sources, and it has no streamlines because it has no direction** — and that is a statement about the rung's physics, not about the reach of its derivation.

**The test is falsifiable in both directions and the article says how.** An internal velocity whose equation is a trajectory's would refute it; a base-valued velocity whose equation is a balance would refute it. **The corpus's five rungs are consistent with it, and the article labels the wider claim as a conjecture.**

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mathbb{B}_{\Phi}$, $T\mathbb{B}_{\Phi}$ | the material sector and its tangent bundle; the base |
| $u^{\imath}$, $\vec\nabla_{\Phi}S/m$, $A_{\imath}/\varrho$ | base-valued velocities: a vector, a gradient, a direction |
| $\Omega_{\imath}=U_{\mathrm{frm}}^{\dagger}D_{\imath}U_{\mathrm{frm}}$ | the internal velocity: a $\mathfrak{u}(4)$-valued connection |
| $\mathrm{D}/\mathrm{D}\tau=u^{\imath}\partial_{\imath}$ | the material derivative; defined only for base-valued $u$ |
| $\Pi_{\imath,kl}$ | the matrix rung's pair momentum flux; matrix-valued |
| force law | $a^{\imath}=F^{\imath}/m$; an equation for a worldline |
| momentum balance | $\partial_{\jmath}\Pi^{\jmath\imath}=\mathcal F^{\imath}$; an equation for a field |
| *in* the base / *on* the base | tangent to it / a function over it |

## Further Reading

- [Five Steps from a Lagrangian to Fluid Equations](five-steps-from-a-lagrangian-to-fluid-equations.html), where this article is S5 and the test is the last of five steps.
- [The Spare Derivative in the Polar Chart](the-spare-derivative-in-the-polar-chart.html), S4, which manufactures the acceleration slot that this article then sorts.
- [The Primordial Force Law and the Two Wong Terms](the-primordial-force-law-and-the-two-wong-terms.html), the four differences, of which the velocity's provenance is the deepest.
- [Criterion for a Fluid Equation](criterion-for-a-fluid-equation-one-polar-coordinates-euler-lagrange-equation.html), the six slots and the rank test, and the ladder table where the verdicts are recorded side by side.
- [The Spin-One Fluid](the-spin-one-fluid.html) and [The Spin-Half Fluid of the Biquaternion Dirac Field](the-spin-half-fluid-of-the-biquaternion-dirac-field.html), the frame rungs whose velocity is a direction and whose verdict is a law.
- [The Relativistic Quantum Space as a Fluid](the-relativistic-quantum-space-as-a-fluid.html), the base the test is stated on.
