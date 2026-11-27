# __Differentiating a First-Order Transport Law: Force, Transport and Product-Rule Terms__

## Introduction

**Every force in this corpus is obtained by differentiating a first-order statement once, and a transport law is the form that statement takes wherever a chart supplies a flow.** That sentence is the whole of the corpus's route from a conservation law to an acceleration law, and it is where the corpus has made its one recorded error. The error was not in the derivation. It was in the *naming*: a display called a product-rule term a force term, and the display had to be repaired.

**The article's subject is the repair, stated as a general procedure.** Differentiate a first-order transport law and three kinds of term appear. One is the acceleration — the second derivative of the transported quantity. One is the transport — the quantity being carried along a flow that changes. One is the product rule — a term that exists because the differentiation was applied to a product and both factors vary. **The third kind is the one that gets mislabelled, and this article states three tests that separate it from the first, gives the corpus's own case, and states the prohibition.**

**Why an article on a product rule.** Because the corpus's fluids are all built this way, and the mistake is not an arithmetic slip but a conceptual one: a term that looks like a force because it sits where a force would sit. **A reader who has seen the three kinds once, with the tests that separate them, will not repeat the error; a reader who has only seen the finished balances will not know there was an error to avoid.**

**The article's scope, stated so that it is not over-read.** It is about differentiating transport laws of the form "a divergence equals a source", which is the form every rung's first-order equation takes. It is not about differentiating arbitrary equations, and the three kinds are the kinds a transport law of that form produces. **The article says where the classification stops.**

## Conventions

The material sector is $\mathbb{B}_{\Phi}$ with gradient $\partial_{\imath}$, and the flow velocity is $u^{\imath}$ where the rung supplies one. The transport law of a quantity $\mathcal Q$ is

$$
\partial_{t'}\mathcal Q+\partial_{\imath}\bigl(\mathcal Q\,u^{\imath}\bigr)=\mathcal S ,
$$

with $\mathcal S$ the source, zero where the rung's law is a strict conservation. **The left side is a divergence; the equation is first order in $\mathcal Q$; and differentiating it once produces the three kinds.**

**The two derivatives that matter, and why they are different.** A *partial* derivative $\partial_{t'}$ differentiates at fixed position; a *material* derivative

$$
\frac{\mathrm{D}}{\mathrm{D}t}=\partial_{t'}+u^{\imath}\partial_{\imath}
$$

differentiates along the flow. **The convective term $u^{\imath}\partial_{\imath}$ is the difference between the two, and it is where the second kind of term is born.** The corpus's notation is [The Euler and Continuity Equations'](the-euler-and-continuity-equations-in-biquaternionic-form.html).

**The matrix rung's notation, because the article's sharpest case is there.** The pair momentum is $M_{kl}$, the inertia is $q_{kl}=\rho_{k}-\rho_{l}$, the internal velocity is $\Omega_{\imath,kl}=U_{\mathrm{frm}}^{\dagger}D_{\imath}U_{\mathrm{frm}}$, and the guidance relation is $\Omega_{\imath,kl}=M_{kl}/q_{kl}$. **The three kinds appear there with names, and the correspondence to the scalar case is exact**; the last section before the summary states it.

## Differentiating the Transport Law: The Three Kinds

**One differentiation, three kinds of term, and the split is forced by the product rule.** Differentiate the transport law once with respect to $t'$ and use the flow's own equation to eliminate $\partial_{t'}\mathcal Q$; the product rule produces

$$
\partial^{2}_{t'}\mathcal Q
+\partial_{\imath}\bigl(\partial_{t'}\mathcal Q\,u^{\imath}\bigr)
+\partial_{\imath}\bigl(\mathcal Q\,\partial_{t'}u^{\imath}\bigr)
=\partial_{t'}\mathcal S ,
$$

and the middle two terms are of different kinds even though they look alike.

| kind | where it comes from | its content | the corpus's name for it |
| --- | --- | --- | --- |
| **acceleration** | the second derivative of $\mathcal Q$ | the rate of the rate | the acceleration term |
| **transport** | $\partial_{\imath}(\partial_{t'}\mathcal Q\,u^{\imath})$ | the quantity's rate carried by the flow | the transport term; at the matrix rung the commutator |
| **product rule** | $\partial_{\imath}(\mathcal Q\,\partial_{t'}u^{\imath})$ | the flow's own variation, multiplied by the quantity | the product-rule term; at the matrix rung $\Omega_{kl}\partial_{\imath}q_{kl}$ |

**The acceleration term is the one that makes the equation second order, and it is the only one that does.** It is the second derivative of the transported quantity, so it is the term that turns a first-order transport law into a second-order equation. **Nothing else in the display is second order in $\mathcal Q$**, and that is the first thing to check when classifying: a term that is not second order in the quantity is not the acceleration.

**The transport term is the flow carrying the quantity, and it is a genuine dynamical term.** It vanishes when the quantity's rate is uniform in space, and it does not vanish when the flow is uniform — because the flow's *carrying* is what the term records. **At the matrix rung it is the commutator $[\Omega,\Pi]$, and the commutator is the exact form the transport takes when the quantity is matrix-valued and the chart is non-abelian**: the flow carries the momentum and rotates it as it carries, and the rotation is the commutator.

**The product-rule term is the one that must be named carefully, and the article names it by its origin rather than by its appearance.** It arises because the differentiation was applied to $\mathcal Q\,\partial_{t'}u^{\imath}$ — a product of two factors — and both factors vary. **Its size is set by how fast the flow's own derivative changes, multiplied by the quantity being carried.** In a chart where the flow's derivative is uniform, the term is a total derivative and integrates away; in a chart where it is not, the term is nonzero and carries no dynamical information about $\mathcal Q$ at all.

## The Three Tests

**A term that sits on the left-hand side where a force could sit is not thereby a force.** The article gives three tests, each of which a genuine force term passes and the product-rule term fails. **They are independent, and a term that passes all three is a force for the purposes of this corpus.**

### Test One: The Vanishing Test

**Set the field's source to zero and ask whether the term survives.** A force term is built from the source — the field strength, the potential's gradient, the curvature — so it vanishes when the source does. **The product-rule term is built from the transported quantity and the flow's variation, and neither of those is the source.** So at a configuration with no source and a non-uniform flow, the product-rule term is nonzero and the force is zero.

**The test is the cleanest of the three and it is the one the corpus's error failed.** A display had assigned the product-rule term to the force side; the test would have caught it immediately, because the display's own equation holds with a vanishing source and a nonzero product-rule term. **A reader who applies only this test will catch the common case.**

**Its limitation, stated so the test is not over-trusted.** The test requires a configuration with a vanishing source and a non-uniform flow, and at some rungs such a configuration may not exist — a rung whose flow is necessarily uniform, or whose source never vanishes. **Where the test cannot be run, the other two still apply.**

### Test Two: The Uniform-Inertia Test

**Set the inertia uniform and ask whether the term survives.** At the matrix rung the product-rule term is $\Omega_{kl}\,\partial_{\imath}q_{kl}$, with $q_{kl}=\rho_{k}-\rho_{l}$ the pair's inertia. **If the four densities are equal, $q_{kl}=0$ for every pair and the term vanishes identically** — and so does the guidance relation's denominator, which is the rung's singular locus and a separate matter. If the densities differ but their *differences are uniform*, $\partial_{\imath}q_{kl}=0$ and the term vanishes while the force need not.

**The test's content is that the term is a derivative of the inertia and not of the state.** A force does not vanish because the inertia is uniform; a product-rule term does, because the inertia's variation is the whole of its content. **At the scalar rungs the same test reads: set the density uniform and ask whether the term survives.** The product-rule term does not, and the force — the potential's gradient — need not be uniform at all.

**Why this test is the definitional one.** The product-rule term is, by construction, the term that appears when the differentiation is applied to a product in which one factor is *not* the transported quantity. **The uniform-inertia test is that statement made operational**: uniform inertia removes the factor's variation and the term with it.

### Test Three: The Uniform-Flow Test

**Set the flow uniform — constant in space and time — and ask whether the term survives.** In a chart with a uniform flow, the convective term vanishes and the product-rule term vanishes with it, because both are built from derivatives of $u$. **A force term does not vanish in a uniform flow**: a charged particle in a uniform electric field accelerates, and the field is as uniform as the flow.

**The test distinguishes the transport term from the force as well, and that is its second use.** The transport term $[\Omega,\Pi]$ does not vanish in a uniform flow — the flow carries and rotates — while the convective part of the acceleration does. **So the test separates the three kinds pairwise**: acceleration (survives uniform flow, is second order in $\mathcal Q$), transport (survives uniform flow, is first order), product rule (vanishes in uniform flow).

### What a Fourth Test Would Fail to Do, and Why the Article Does Not Give One

**The natural fourth test is gauge invariance: a force term must be invariant under a relabelling of the frame, and the product-rule term might not be.** The test does not discriminate, and the corpus's verification is what shows it. **The connection $\Omega_{\imath}$ is gauge-covariant under the frame's relabelling** — a check in the corpus's verification directory tests exactly this and finds the connection unchanged to $10^{-8}$ — **so $\Omega_{kl}\partial_{\imath}q_{kl}$ is as gauge-invariant as the curvature term beside it.** The test would pass both and separate neither.

**The article states this because a reader will expect a fourth test and will be right to expect that invariance arguments are the usual tool.** The invariance argument fails here for a structural reason: the product-rule term is built from gauge-covariant objects, so no gauge argument can distinguish it. **The three tests that do distinguish it are the three that use the term's *origin* rather than its transformation.**

## The Matrix Rung's Correspondence

**The corpus's sharpest case is the matrix rung, and the three kinds appear there with names that a reader of the literature will recognize.** The balance is

$$
\partial_{\jmath}\Pi_{\imath,kl}
+\bigl[\Omega_{\jmath},\Pi_{\imath}\bigr]_{kl}
+\Omega_{\jmath,kl}\,\partial_{\imath}q_{kl}
=-\bigl[U_{\mathrm{frm}}\,D_{\jmath}D_{\imath}\Xi\,U_{\mathrm{frm}}^{\dagger}\bigr]_{kl},
$$

and each term is one of the three kinds.

| the term | its kind | the test it passes |
| --- | --- | --- |
| $\partial_{\jmath}\Pi_{\imath,kl}$ | the acceleration | second order in the pair momentum; survives uniform inertia and uniform flow |
| $[\Omega_{\jmath},\Pi_{\imath}]_{kl}$ | the transport | first order; survives uniform flow; vanishes when the momentum commutes with the connection |
| $\Omega_{\jmath,kl}\,\partial_{\imath}q_{kl}$ | the product rule | vanishes at uniform inertia |
| $-[U D_{\jmath}D_{\imath}\Xi U^{\dagger}]_{kl}$ | the force | vanishes when the field's second covariant derivative vanishes |

**The transport term's commutator form is not an accident of the rung; it is what the transport term becomes when the quantity is matrix-valued.** The flow carries the momentum and, in a non-abelian chart, rotates it as it carries; the rotation is the commutator. **In an abelian chart the commutator vanishes and the transport term reduces to the scalar case's $\partial_{\imath}(\mathcal Q u^{\imath})$.** So the commutator is the general form and the scalar case is its abelian limit.

**The product-rule term's form, $\Omega_{\jmath,kl}\partial_{\imath}q_{kl}$, is the general form of "the flow's variation times the quantity" for a pair.** The quantity is the pair's inertia $q_{kl}$; the flow's variation is $\Omega_{\jmath,kl}$; and the term is their product. **It is exactly the term a reader would write down if asked to "differentiate the pair's momentum and keep everything", and it is exactly the term that is not a force.**

**The force term, $-[\dots]$, is the field's second covariant derivative in the frame's basis.** It vanishes when the field is covariantly constant, it carries the field's curvature, and it is the only term in the display built from the field rather than from the pair. **That is the vanishing test's statement at this rung**: set the field flat, and three of the four terms remain and the fourth does not.

**Why this table is the article's centrepiece.** Because the correspondence is exact — the three kinds at the matrix rung are the three kinds of the scalar transport law under the replacements $\mathcal Q\to\Pi$, $u\to\Omega$, and $\partial\to D$ — and because it shows the classification is not a scalar-only device. **A reader who wants to know whether a display's term is a force term can find its rung in the table and read the verdict off.**

## The Corpus's Case, and What Went Wrong

**The corpus's error is worth recounting exactly, because it is a textbook case of a classification slip and it is the reason this article exists.** The primordial force law's derivation had reached the pair's balance and had produced a display with four terms. Three of the four were assigned correctly — the derivative of the pair momentum, the commutator, and the curvature — and the fourth, the product-rule term, was displayed on the same side as the force and read as part of it.

**Why the display looked right, which is the instructive part.** The product-rule term is nonzero in exactly the configurations where the force is nonzero: a field with a spatially varying eigenvalue splitting also has a spatially varying inertia, so the two terms appear together and their sum looks like a single force. **The error was not visible in any one configuration; it was visible in the classification.** A reader checking the display against a solution would find agreement; a reader checking the *kind* of each term would find the misassignment.

**How it was caught.** By the three tests, applied in the order the previous section states. **The vanishing test**: the display's own equation holds with the curvature set to zero and the product-rule term nonzero, so the product-rule term cannot be part of the force. **The uniform-inertia test**: with $\partial_{\imath}q_{kl}=0$ the term vanishes and the force does not, so the term is a function of the inertia's variation. **The uniform-flow test**: the term vanishes in a chart where $\Omega$ is uniform, and the force does not.

**The repair, stated as the corpus now states it.** The product-rule term is on the left, with the acceleration and the transport, and the force is alone on the right. **The corpus's verification check F is the repaired display's numerical witness** — a residual of $4.5\times10^{-8}$ on data of order $0.6$ for the balance with the term on the left, and no such agreement with it on the right. **The check is not what caught the error** — the check was written after — **but it is what keeps the repair from regressing**, and the article says so rather than implying the numerical test found the mistake.

**The general lesson, in one sentence, and it is the article's thesis.** *A term's position in a display is a claim about its kind, and a claim about its kind is testable independently of any solution.* The three tests are that independent test; the displays are the claims; and the corpus's rule is that a display introducing a new term must state which of the three kinds it is.

## A Checklist for a New Display

**The article's practical content is a checklist, and the checklist is meant to be applied before a display is written rather than after.** It has five lines, and the fifth is the one the corpus's error skipped.

| step | the question | the failure it prevents |
| --- | --- | --- |
| 1 | which term is second order in the transported quantity? | calling a first-order term the acceleration |
| 2 | which term vanishes when the source vanishes? | calling the force something that is not the force |
| 3 | which term vanishes at uniform inertia? | **calling the product-rule term a force** |
| 4 | which term vanishes at uniform flow? | confusing the transport with the product rule |
| 5 | has each term's kind been *stated*, and not only its position? | the corpus's error |

**Line 5 is the methodological rule and it is worth more than the other four.** A display that puts a term somewhere has made an implicit claim; a display that labels it has made an explicit one and can be checked. **The corpus's house style asks for the labels, and this article is why.**

**The checklist applied to a scalar case, so that it is not abstract.** Take the Schrödinger rung's transport law $\partial_{t}\varrho+\vec\nabla\cdot(\varrho\vec v)=0$ and differentiate it. **Line 1**: the second derivative of $\varrho$ is the acceleration term, and it is the only term second order in $\varrho$. **Line 2**: no term vanishes when the potential vanishes, because this transport law has no source — so the checklist must be applied one level up, to the acceleration law the transport law generates. **Line 3**: with $\varrho$ uniform, the product-rule term $\vec v\cdot\vec\nabla\varrho$... vanishes, and the force does not. **Line 4**: with $\vec v$ uniform, the convective term vanishes and the potential's gradient does not. **The four lines, applied in order, produce the classification the fluid articles display** — and the fifth line is what makes the classification visible in the article rather than in the reader's head.

**What the checklist does not do.** It does not tell you whether the display is *correct* — only whether its terms are correctly classified. **A display can classify every term correctly and still be wrong**, and the corpus's numerical checks are for that. The checklist and the checks are complementary, and the article says so because a reader might take the checklist as a substitute for verification.

## Where the Classification Stops

**The three kinds are the kinds a transport law of the divergence form produces, and a transport law of another form produces others.** The article states the boundary so that the classification is not applied where it does not hold.

**A transport law with a source produces a source term under differentiation, and the source term is a fourth kind.** Differentiating $\partial_{t'}\mathcal Q+\partial_{\imath}(\mathcal Q u^{\imath})=\mathcal S$ gives $\partial_{t'}\mathcal S$ on the right, and that term is neither acceleration, transport nor product rule: it is the rate of the source. **The corpus's rungs with sources — the massive rungs' eigenvalues, the coupled rungs — therefore have four kinds and not three**, and the article's table should be read as the sourceless case.

**A transport law that is nonlinear in the flow produces a term of mixed kind.** If the flow's own equation is nonlinear, the term $\partial_{\imath}(\mathcal Q\partial_{t'}u^{\imath})$ contains the flow's nonlinearity as well as its variation, and the term is neither purely transport nor purely product rule. **The corpus's non-abelian rungs are of this kind**, and the commutator is how the mixing appears: $[\Omega,\Pi]$ carries both the carrying and the rotating.

**A constrained flow produces no new kind but a different equation for the flow**, and the differentiation must use the constraint rather than the unconstrained equation. **The corpus's Proca rung is the case**, and its Euler equation is obtained by projecting the constrained equation rather than by differentiating an unconstrained transport. **The classification survives — three kinds still appear — but the differentiation is a projection**, which is [the spare derivative's](the-spare-derivative-in-the-polar-chart.html) subject.

**The honest summary of the boundary.** The three kinds are general for sourceless transport laws linear in the flow. Outside that class, the classification is a starting point and the article does not claim more. **A reader who applies the three tests to a term of an unfamiliar kind will learn which of the three it most resembles, and that is useful even when it is not decisive.**

## What This Article Does Not Claim

**That the three kinds are exhaustive for every transport law.** They are exhaustive for the sourceless linear class, and the previous section states the exceptions. **A fourth kind — the source's rate — is named and not developed.**

**That the three tests are independent in every case.** They are independent in the cases the article applies them to, and the uniform-inertia test presupposes an inertia. **A rung with no inertia — the scalar rungs before the pair structure appears — cannot run test two as stated**; the article gives the scalar reading (uniform density) and says it is a reading.

**That the product-rule term is negligible.** It is not negligible; it is nonzero and it matters. **The claim is that it is not a force term**, and a balance that omits it is wrong. **The corpus's error was not omitting it but mislabelling it**, and the distinction matters: an omitted term breaks the equation, a mislabelled one breaks the reading.

**That the numerical check F caught the error.** It did not; the classification tests did, and the numerical check was written afterwards to prevent regression. **The article states this because the corpus's honesty rules require distinguishing what a check proves from what a derivation established.**

**That the commutator is the only form the transport term takes in a non-abelian chart.** It is the form for a matrix-valued quantity carried by a connection. **A quantity carried by a different transport — a spinor's, a density matrix's — takes the covariant derivative's form, which reduces to the commutator in the adjoint representation.** The article states the commutator's case and not the general one.

**That a force term is always algebraic in the field.** The matrix rung's force term carries two covariant derivatives, and the scalar rungs' carries one gradient. **What is true is that the force term is built from the source and vanishes with it**, which is test one, and the article does not claim an order for it.

## Open Questions

**Is there a term that passes all three tests and is not a force?** The article knows of none, and the three tests are stated as a sufficient condition within the corpus. **A term built from the source but multiplied by a function of the state — a state-dependent coupling — passes test one only if the function vanishes with the source**, which it need not. **Such a term is a force with a state-dependent coefficient**, and whether the corpus's classification should name it a fourth kind is open.

**Can the three kinds be derived rather than classified?** The kinds are what the product rule produces; a derivation would exhibit them as the components of a single object — the derivative of a divergence — under a decomposition. **The article does not have the decomposition**, and it suspects the decomposition is the Hodge decomposition of the differentiated current, which would make the three kinds the exact, coexact and harmonic parts. **That is a conjecture and it is labelled as one.**

**Does the classification survive the passage to a distributional chart?** At the singular locus the derivatives are distributional and the product rule acquires delta terms. **Whether the delta terms are a fourth kind or a limit of the product-rule kind is not settled**, and the corpus's singular sets are where the question would be asked.

**Is there a rung where the product-rule term is the only term?** That would be a configuration with a stationary quantity, a uniform flow and a varying inertia. **If such a configuration exists at the matrix rung**, its balance would be a statement about the inertia's variation alone, and the article does not know whether the rung admits it.

## What This Article Adds and What It Relabels

**Adds.** The **three kinds of term** named by origin rather than by appearance, with the table of what each is and what it is not; the **three tests** — vanishing, uniform inertia, uniform flow — with the explicit statement that a fourth, gauge invariance, does *not* discriminate and the verification that shows why; the **matrix-rung correspondence**, exact under $\mathcal Q\to\Pi$, $u\to\Omega$, $\partial\to D$, with the commutator as the transport term's general form and the scalar case as its abelian limit; the **corpus's error recounted** with what made it invisible and what caught it; the **five-line checklist**, of which the fifth — state the kind, not only the position — is the methodological rule; and the **boundary** of the classification, with the source's rate named as a fourth kind outside it.

**Repeats, and says so.** The table of the three kinds appears twice in the corpus: here, and in [The Spare Derivative in the Polar Chart](the-spare-derivative-in-the-polar-chart.html), where it is a step in the manufacturing rather than a subject. **The repetition is deliberate** — a reader who meets the prohibition while learning the manufacturing should not have to follow a link to learn why it is a prohibition — **and the two statements must not diverge:** if either article's table changes, the other's changes with it. What is this article's and not the other's is the tests, the checklist and the corpus's case.

**Does not add.** No new equation. The balance is [The Primordial Force Law's](the-primordial-force-law-and-the-two-wong-terms.html); the tests are this article's; the correspondence is a reading of a display that already existed.

**Relabels.** *"The force has three parts"* — the force has one part, and the left side of the balance has three. *"The quantum potential is a force"* — it is, and the convective term beside it is not, and the distinction is test three. *"The product-rule term is small"* — it is not small; it is not a force.

## Summary

**A first-order transport law, differentiated once, produces three kinds of term: the acceleration, the transport and the product rule.** The acceleration is the second derivative of the transported quantity and the only term that makes the equation second order. The transport is the flow carrying the quantity, and it takes the commutator's form when the quantity is matrix-valued. **The product rule is what the differentiation produces because it was applied to a product whose factors both vary, and it is never a force term.**

**Three tests separate them, and each is a configuration in which one kind vanishes and the others do not.** The vanishing test sets the source to zero. The uniform-inertia test sets the inertia's variation to zero. The uniform-flow test sets the flow's variation to zero. **A fourth test — gauge invariance — does not discriminate, because the product-rule term is built from gauge-covariant objects, and the article says so rather than leaving the gap.**

**The corpus's one recorded error was a product-rule term displayed as a force term, and it was caught by the tests and not by the numerical check.** The check was written afterwards and now prevents regression. **The check's residual is $4.5\times10^{-8}$ on data of order $0.6$, and the article says plainly that the check did not find the mistake.**

**The classification is a claim about kinds, and a claim about kinds is testable independently of any solution.** That is the article's thesis, and the five-line checklist is its operational form: the fifth line asks that a display state each term's kind and not only its position.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mathcal Q$ | the transported quantity |
| $u^{\imath}$, $\Omega_{\imath}$ | the flow velocity: base-valued, or the internal connection |
| $\mathcal S$ | the transport law's source |
| $\mathrm{D}/\mathrm{D}t=\partial_{t'}+u^{\imath}\partial_{\imath}$ | the material derivative |
| $\Pi_{\imath,kl}$, $M_{kl}$, $q_{kl}$ | the matrix rung's momentum flux, pair momentum and inertia |
| acceleration / transport / product rule | the three kinds; second order in $\mathcal Q$, first order, and the inertia's variation |
| the vanishing test | set the source to zero |
| the uniform-inertia test | set $\partial q=0$ |
| the uniform-flow test | set $\partial u=0$ |

## Further Reading

- [The Primordial Force Law and the Two Wong Terms](the-primordial-force-law-and-the-two-wong-terms.html), where the balance is derived and the error is repaired.
- [The Spare Derivative in the Polar Chart](the-spare-derivative-in-the-polar-chart.html), the step that produces the transport law this article differentiates.
- [The Euler and Continuity Equations in Biquaternionic Form](the-euler-and-continuity-equations-in-biquaternionic-form.html), the scalar case's acceleration and convective terms.
- [Five Steps from a Lagrangian to Fluid Equations](five-steps-from-a-lagrangian-to-fluid-equations.html), where this article is the detail behind S4's third part.
- [Base-Valued versus Internal Flow Velocity](base-valued-versus-internal-flow-velocity-a-test-separating-force-laws-from-momentum-balances.html), the test that decides whether the manufactured equation is a law or a balance.
