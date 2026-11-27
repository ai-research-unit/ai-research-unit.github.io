# __Five Steps from a Lagrangian to Fluid Equations: A Derivation Common to Scalar, Spinor, Vector and Matrix Fields__

## Introduction

The corpus reads five fields as fluids, and the readings were made one at a time. The Schrödinger field was read in [The Schrödinger Fluid](the-schrodinger-fluid.html), the scalar in [The Spin-Zero Fluid](the-spin-zero-fluid.html), the spinor in [The Spin-Half Fluid of the Biquaternion Dirac Field](the-spin-half-fluid-of-the-biquaternion-dirac-field.html), the vector in [The Spin-One Fluid](the-spin-one-fluid.html), the matrix in [The SU(4) Fluid Equations from the Primordial Action](su4-fluid-equations-from-the-primordial-action.html). Each article states its own derivation, and each derivation was written without the others in view.

**This article states the derivation once, and the claim is that the five derivations are one derivation.** Not that they resemble one another: that the same five steps, in the same order, produce the fluid equations at every rung, and that the differences between the rungs sit in *one* of the five steps and nowhere else. The claim is falsifiable in a way a resemblance is not. Run the five steps on a field and see whether the equations come out. If they do not, the article says which step failed.

**The warrant is that the skeleton was found and not imposed.** The five steps were extracted from the five finished articles, which were written independently and by different routes. That is the sense in which the skeleton is a derivation: it is the common part of five derivations that did not know they had one, and a sixth derivation that walks it is evidence for it rather than an application of it. What the extraction added is the ordering — the fact that step four is a step, and that step five is a test rather than a computation.

**Position.** A methodological article of the category *Biquaternion Universe Action*, in the section *From the Field Equation to the Fluid*. Its subject is the middle arrow of the category's chain. The apparatus the arrow needs — the action, the pairing it can integrate, the connection, the curvature — is [the section above](the-relativistic-particle-and-the-lagrangian-the-stationary-action-principle.html), and is not restated. The arrow's output, once it exists, is the subject of [the section below](differentiating-a-first-order-transport-law-force-transport-and-product-rule-terms.html). The criterion that decides *which* of the equations a rung produces deserve to be called fluid equations is [Criterion for a Fluid Equation: One Polar Coordinate's Euler–Lagrange Equation, Not a Combination](criterion-for-a-fluid-equation-one-polar-coordinates-euler-lagrange-equation.html), and this article uses that criterion without re-arguing it.

**The five steps, stated before they are argued.**

| step | the claim | what it supplies |
| --- | --- | --- |
| S1 | the action is a pairing of logarithmic derivatives against itself, plus one algebraic term | the two terms every slot is read from |
| S2 | the polar word factorises the field into real parameters, and the factorisation is a bijection on the invertibles | the coordinates |
| S3 | the parts of the logarithmic derivative have distinct algebraic types, and the pairing is diagonal on them; one variation per coordinate then fills one slot per type | the slots |
| S4 | the phase and the frame enter only through their derivatives, so their equations are one order lower and leave a derivative available; the acceleration law is manufactured from them and never varied | the force term |
| S5 | whether the fluid's velocity is a section of the base's tangent bundle decides whether S4 yields a force law or a momentum balance | the sorting |

**Two of the five steps are the ones a reader will not have seen stated.** S3 is usually presented as one step, the polar substitution, and it is two: a statement about the action (the pairing does not mix types) and a statement about the variation (the type of a term decides which slot its equation fills). S4 is usually not presented at all, because at the scalar rungs it is performed without comment: "Euler is not varied, it is differentiated" is a remark inside a derivation, not a step. It is a step, it is the reason a force exists at every rung, and its content is that the second derivative of the fast coordinate lives in the force slot and nowhere else.

**What the article does not do.** It does not add an equation to any rung and it does not claim that the fluid chart is more than a chart. Every equation it displays is a sibling article's, reached by the same route. The claim is about the *order* of the derivation and the *location* of its failures.

## Conventions

The algebra, the element, the four conjugations and the six subspaces are [The Algebraic Vocabulary](the-algebraic-vocabulary-element-conjugations-six-subspaces-and-two-ledgers.html); the two sectors and the four bridges are [The Two Sectors](the-two-sectors-the-hermitian-split-and-the-four-bridges.html). This article uses four symbols and no others.

The **field** is $\tilde\Xi$, an element of $\mathbb{B}$ or of a module over it, at each event of the material sector. The **gradient** is $\partial_{\imath}$, the material sector's, with $\imath\in\{t,x,y,z\}$. The **logarithmic derivative** is

$$
\mathcal A_{\imath}=\tilde\Xi^{-1}\partial_{\imath}\tilde\Xi ,
$$

and it is the article's central object: one element of the algebra per direction, defined wherever $\tilde\Xi$ is invertible. The **scalar pairing** is the one the action integrates, $\langle\tilde Q_1\tilde Q_2\rangle_{\natural}$ or its trace form at the matrix rung; [The Invariant Density](the-invariant-density-which-pairing-the-action-can-integrate.html) states which pairing and why, and this article takes the answer.

**The four types.** The algebra splits into four invariant subspaces, and the split is the one the four factors of the word correspond to.

| type | dimension | what it is | the word's factor |
| --- | --- | --- | --- |
| real central | $1$ | the real line $\mathbb{R}e_t$ | the scale $\varrho$ |
| central imaginary | $1$ | the line $\mathbb{R}(ie_t)$ | the phase $e^{i\theta_{\mathrm{pha}}}$ |
| Hermitian traceless | $3$ | the boost's space | the boost $\tilde U_{\Psi,\mathrm b}$ |
| real traceless | $3$ | the rotor's space | the rotor $\tilde u_{\mathrm r}$ |

**The four dimensions add to eight, and the addition is a theorem.** $1+1+3+3=8$ is the real dimension of $\mathbb{B}$, and the four types are the four factors' parameter spaces. That is why the word is a chart and not a parametrisation with slack: the parameters and the data have the same count, and S2's bijection is what turns the count into an identification.

One further convention, used from S4 onward. The **order** of an equation is the order of its highest derivative of the field's data. The field equations of this corpus are second order — Klein–Gordon, Proca, Dirac and Yang–Mills alike — with one exception stated where it occurs, the first-order Schrödinger action. Order is the quantity S4 is about, and it is a property of the coordinate and not of the field.

## S1: The Action Is a Pairing plus One Algebraic Term

**Every rung's action has two terms.** A kinetic term that pairs the logarithmic derivative with itself, and an algebraic term that is a function of the field with no derivative at all.

$$
S=\int d^{4}r\;\Bigl[\;\kappa\,\bigl\langle\,\textstyle\sum_{\imath}\mathcal A_{\imath}\mathcal A_{\imath}\bigr\rangle_{\natural}\;-\;V(\tilde\Xi)\;\Bigr],
$$

with $\kappa$ a constant carrying the units and the sign, and $V$ a scalar function of the field. The display is schematic in one respect that matters: the sum over $\imath$ carries the metric's signs, and at the matrix rung the pairing is a trace rather than the quaternionic norm. Neither changes the structure, which is that there are two terms and they are of two kinds.

**The kinetic term is built from $\mathcal A_{\imath}$ and not from $\partial_{\imath}\tilde\Xi$, and the difference is the whole of the mechanism.** A kinetic term $\langle\sum_{\imath}\partial_{\imath}\tilde\Xi\,\partial_{\imath}\tilde\Xi\rangle_{\natural}$ is invariant under the *global* multiplication of the field by a constant element, and under nothing else. The logarithmic form is invariant under $\tilde\Xi\mapsto\tilde\Xi\,\tilde G$ for a constant invertible $\tilde G$ — a much larger group, because $\mathcal A_{\imath}$ is unchanged by a right multiplication — and it is the reason the field's *internal frame* is a coordinate rather than a fixed gauge choice. **The logarithm is what makes the frame an object the fluid can carry.**

**The algebraic term is a function of the field's invariants and of nothing else.** It cannot depend on $\mathcal A_{\imath}$ without becoming part of the kinetic term, and it cannot depend on the direction without breaking the invariance the kinetic term has. Two consequences follow, and both are used later. The algebraic term is where the *pressure* comes from, because it is the only term that is not a derivative and a pressure is what a fluid has when it resists compression rather than acceleration. And the algebraic term is where a *mass* comes from, because a mass term is quadratic in the field and carries no derivative.

**The two terms are the whole input, and the claim is that the fluid's six slots are read from them.** This is worth stating as a discipline rather than an observation. A derivation that needs a third term to reach a fluid slot is not a declension of this skeleton; it is a different construction, and the corpus's one such block says so. [Causal Dissipative Fluid Physics](causal-dissipative-fluid-physics-in-biquaternionic-form.html) has no action behind it, because a dissipative term is not the variation of anything. That block is outside the skeleton, and the exclusion is a feature: the skeleton covers the Lagrangian fluids, and the boundary of that class is exactly the existence of S1.

**One subtlety, stated because it recurs.** The pairing must be *scalar*, in the sense of returning an element of the centre with the invariance the action needs. [The Invariant Density](the-invariant-density-which-pairing-the-action-can-integrate.html) derives the three requirements — cyclicity, reality, positivity as a Euclidean statement — and shows that at $2\times2$ the element pairing and the trace are one functional, so the obstruction on $\mathbb{C}^{4}$ is dimension and not symmetry. The consequence for this article is narrow: the pairing is *diagonal on the types*, which is S3a, and it is diagonal because it is scalar and the types are distinct invariant subspaces. S1 and S3a are therefore not independent, and the article states them separately because the derivation uses them separately.

## S2: The Polar Word Is a Bijection on the Invertibles

**The word is a factorisation of the field into real parameters.** At the spinor rung,

$$
\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
$$

with $\varrho>0$ the scale, $\theta_{\mathrm{pha}}$ the phase, $\tilde U_{\Psi,\mathrm b}$ a Hermitian positive unit element carrying a rapidity and a real unit axis, and $\tilde u_{\mathrm r}$ a real unit quaternion carrying an angle and a real unit axis. The four factors are the four types of the conventions table, and the parameters are real.

**The word is a bijection, and the bijection is the requirement.** On the invertible elements, and with the phase taken modulo $2\pi$ and the rotor's angle modulo $4\pi$, the map from parameters to field is one-to-one and onto. That is the statement $1+1+3+3=8$ upgraded from a count to an identification: the parameters *are* the field's real data, not a redundant description of them.

**Where the bijection fails, and the failure is part of the definition.** Three loci, and they are the corpus's three singular sets.

| field | the singular set | what fails there | where it is stated |
| --- | --- | --- | --- |
| spinor, scalar | the zero-divisor cone $N(\tilde\Xi)=0$ | no polar decomposition exists; the field has no density | [The Domain of the Polar Decomposition](the-domain-of-the-polar-decomposition-invertible-elements-and-the-zero-divisor-cone.html) |
| scalar, Schrödinger | the nodal set $\varrho=0$ | the phase is undefined, the velocity diverges | [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html) |
| matrix, $\mathrm{SU}(4)$ | the crossings $\rho_{k}=\rho_{l}$ | the pair's guidance entry is $0/0$ | [The SU(4) Fluid Equations](su4-fluid-equations-from-the-primordial-action.html) |

**The three are one phenomenon at three rungs, and the article says so because a reader will otherwise read them as three defects.** In each case the word's map ceases to be a bijection: at the cone the field is not invertible and the word does not exist; at the node the scale vanishes and the phase's coordinate degenerates; at the crossing two eigenvalues coincide and the frame's action on the pair is undefined. **The fluid chart is a chart, and a chart has a singular locus.** The field equations survive where the chart does not, and that asymmetry is the subject of the third of this article's equivalences.

**The matrix rung's word is the same word, one group up.** There the field is $\Xi=U_{\mathrm{frm}}PU_{\mathrm{frm}}^{\dagger}$ with $P=\mathrm{diag}(\rho_{1},\dots,\rho_{4})$, the parameters are four eigenvalues and a twelve-parameter frame, and the count is $4+12=16$ against the sixteen real components of a Hermitian matrix. **The redundancy is $\mathrm{U}(1)^{4}$, the subgroup that commutes with $P$**, and it is the reason the frame contributes twelve and not sixteen. The word is again a bijection, now onto the orbits of that subgroup, and the singular locus is the crossing.

**Two things S2 supplies and nothing else does.** The coordinates — the derivation has nothing to vary until the word exists. And the *order separation*, which the article postpones to S4 because it is the payoff: the word does not merely rename the field's data, it puts the phase and the frame at one order below the scale, and that spare derivative is what the force will be made of.

## S3: The Type Decomposition, and One Equation per Coordinate

Step three is two statements, and the article keeps them apart because a derivation uses them in order.

### S3a: The Pairing Does Not Mix the Types

**The logarithmic derivative has four parts, and they are of four different types.** Differentiating $\tilde\Xi=\varrho\,e^{i\theta}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ and multiplying by $\tilde\Xi^{-1}$,

$$
\mathcal A_{\imath}
=\underbrace{\partial_{\imath}\ln\varrho}_{\text{real central}}
+\underbrace{i\,\partial_{\imath}\theta_{\mathrm{pha}}}_{\text{central imaginary}}
+\underbrace{\tilde U_{\Psi,\mathrm b}^{-1}\partial_{\imath}\tilde U_{\Psi,\mathrm b}}_{\text{Hermitian traceless}}
+\underbrace{\tilde u_{\mathrm r}^{-1}\partial_{\imath}\tilde u_{\mathrm r}}_{\text{real traceless}} .
$$

The four terms are not four approximations to one object. They lie in four invariant subspaces of the algebra, and each is closed under the operations the other three are built from.

**The scalar pairing is diagonal on those subspaces, so the kinetic term is a sum of four squares with no cross term.** This is the step that is usually compressed into "substitute and expand". It is not an algebraic accident: the pairing returns a central element, the four types are distinct subspaces of the algebra, and a scalar pairing of two elements of different types vanishes identically. **The kinetic term is therefore four independent squares, and the action is four theories that share a field.** The corpus states it once for the collapse — "the two squares are separate because the bracket's real and imaginary parts are of different types and do not mix under the scalar pairing" — and the statement is the general one.

**What S3a buys, and what its failure would cost.** Because the squares do not mix, each coordinate's equation is a statement about one type and can be read alone. A pairing that mixed types would produce cross terms, and a cross term is a coupling in the *kinetic* term — a kinetic mixing that turns two coordinates' equations into one system and destroys the slot assignment of S3b. **The corpus has a worked example of the failure**: the matrix rung's trace pairing mixes nothing, but the informational reduction $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ is not cyclic and would cost the invariance of the Yang–Mills action, which [The Yang–Mills Equation](the-yang-mills-equation-in-biquaternionic-form.html) states as the reason the trace is used there.

**The class this excludes.** S3a is where a theory with derivative cross-coupling — a Chern–Simons term, a Pauli term with an arbitrary coefficient, a non-minimal coupling — leaves the skeleton. It is not that such theories have no fluid; it is that their kinetic term is not four squares, so the type-to-slot map does not exist and the derivation must be redone by hand. The skeleton is a statement about actions of the S1 form.

### S3b: The Type of a Term Decides Which Slot Its Equation Fills

**Varying one coordinate gives one equation, and the equation inherits the type of the term the coordinate appears in.** This is the claim, and its content is easiest to see as a table.

| coordinate | its type | its equation's type | the slot it fills |
| --- | --- | --- | --- |
| $\varrho$ | real central | a real scalar, second order | the density's transport |
| $\theta_{\mathrm{pha}}$ | central imaginary | a divergence, first order | continuity |
| $\tilde U_{\Psi,\mathrm b}$ | Hermitian traceless | a vector-valued transport | the boost's transport |
| $\tilde u_{\mathrm r}$ | real traceless | a vector-valued transport | the rotor's transport |

**The equations come out in the type's shape and in no other.** A real central coordinate's variation yields a real scalar equation because the coordinate is central and real; a central imaginary coordinate appears in the action only through $\partial_{\imath}\theta$, so its Euler–Lagrange equation is the vanishing of a divergence, and a divergence is continuity. **No rung can produce a spin equation from a scalar action**, because the type is not there to vary — and that is a stronger statement than "the action does not contain spin": it says that the slot list is a function of the type list, and a missing type is a missing slot.

**The honesty, because the map is not onto the six slots.** Two of a fluid's six slots are coordinate equations at the gradient rungs — continuity and the density's transport — and the other four are read from the same two terms rather than varied. The acceleration slot is the derivative of the density's equation, not an independent variation; the vorticity is a function of the velocity; the equation of state is the algebraic term's contribution to the stress. [Criterion for a Fluid Equation](criterion-for-a-fluid-equation-one-polar-coordinates-euler-lagrange-equation.html) says this in the vocabulary of warrants, and the statement here is its complement: **S3b assigns the slots that *can* be coordinate equations, and says of the others that they are read.** The two statements agree, and the ladder's count is the same in both.

**At the matrix rung the same statement is the guidance equation, and it is algebraic rather than a divergence.** The frame's coordinate is the entry $U_{\mathrm{frm},kl}$, and its variation gives $\Omega_{\imath,kl}=M_{kl}/q_{kl}$ — an algebraic relation, because at that rung the frame enters the action through a first-order covariant derivative and not through a phase gradient. **The type is the same — Hermitian traceless, the frame's — and the equation's shape is not**, because the rung's action is first order in the frame. That is the one place in the ladder where S3b's output does not look like its siblings', and it is the reason S4 exists as a separate step rather than as a remark.

## S4: The Acceleration Law Is Manufactured, Not Varied

**This is the step the corpus performs without naming, and it is the step that produces the force at every rung.** The statement has three parts, and the third is the one usually written as a remark.

*First, the word separates the coordinates by order.* The scale appears in the algebraic term undifferentiated, so its variation carries a $\partial V/\partial\varrho$ piece and its equation has the field equation's order. The phase appears only as $\partial_{\imath}\theta_{\mathrm{pha}}$, so its variation is the vanishing of a divergence, and it is **one order lower**. The frame appears only as $\tilde U^{-1}\partial_{\imath}\tilde U$, so its equation is one order lower too — a transport, or at the matrix rung an algebraic relation.

*Second, the rung therefore carries a first-order relation that defines the velocity.* At the scalar rungs it is the guidance equation, $\partial_{\imath}S=m v_{\imath}$ together with the statement that fixes the zero of $S$; at the matrix rung it is $\Omega_{\imath,kl}=M_{kl}/q_{kl}$. **A defining relation that is first order leaves exactly one derivative available**, and that derivative is what the acceleration law is made of.

*Third, the acceleration law is obtained from a coordinate's equation rather than varied.* The corpus's sentence is exact and it is the general one: **Euler is not varied; it is differentiated.** Differentiating the guidance relation consumes the available derivative, and the result relates the velocity's own derivative to the other terms — which is what a force is. **The second derivative of the phase appears nowhere else in the system.** Continuity has only first derivatives; the quantum Hamilton–Jacobi equation has only first derivatives of the phase; the acceleration law is the only place the phase's second derivative lives, and it gets there by differentiation. That is the sharpest statement of what S4 is.

**The honesty about the frame rungs, because the word "differentiated" does not cover them.** At the Proca and Dirac rungs the frame's equation is already second order, and the fluid's acceleration law is its component *transverse to the flow* — a projection, not a differentiation. **The general statement is therefore not "differentiate" but "manufacture from a coordinate's equation", and the manufacturing is a differentiation where the velocity is a gradient, a projection where it is a direction, and a derivative of the algebraic guidance relation at the matrix rung.** Three operations, one claim: the acceleration law is never an independent variation.

**Three kinds of term come out of the manufacturing, and the article insists on keeping them apart.** Differentiating a product produces the genuine second derivative — the acceleration; the transport of the quantity being carried; and a product-rule term from the fact that both the quantity and the flow vary. At the scalar rungs the three are the acceleration $\partial_{t'}\vec v$, the convective term $(\vec v\cdot\vec\nabla)\vec v$, and the gradient of the quantum potential. **The product-rule term is never the force term**, and the corpus's error log contains a display that merged them. [Differentiating a First-Order Transport Law](differentiating-a-first-order-transport-law-force-transport-and-product-rule-terms.html) states the three in full.

**Why this is not new physics, stated plainly.** The manufactured equation is a consequence of an equation already in the rung: differentiate the guidance relation and use the field equation, and the acceleration law follows. It adds no term to the action and no equation to the system. **What S4 changes is the reading** — the same content appears once as a transport law and once as an acceleration law, and the corpus keeps both because they answer different questions. **What S4 adds is the location**: the second derivative of the fast coordinate lives in the force slot and nowhere else, and that is why a force slot exists at every rung.

**At the matrix rung S4 manufactures a balance and not a law, and the reason is S5.** The guidance relation there is algebraic in $\Omega_{\imath}$, and its derivative gives $\partial_{\jmath}\Pi_{\imath}=\dots$ — a divergence of a matrix-valued momentum. There is no $v^{\imath}\partial_{\imath}$ anywhere in it, because $\Omega_{\imath}$ is internal, and no material derivative means no worldline, which means no $F=ma$. **That is not a defect of the manufacturing; it is the manufacturing reporting a fact about the rung.** Which brings the article to the fifth step.

## S5: Base-Valued or Internal — the Test That Sorts the Output

**The question is one line: is the fluid's velocity a section of the base's own tangent bundle?** The base is the material sector $\mathbb{B}_{\Phi}$ at every rung; the fibre is what changes. The velocity is a frame element at the spinor and vector rungs and an algebra element at the matrix rung, and the test asks whether the first is an element of $\mathbb{B}_{\Phi}$ at each point and the second is not.

| rung | the velocity | in the base, or on it? | what S4 produces |
| --- | --- | --- | --- |
| Schrödinger, Klein–Gordon | $\vec\nabla_{\Phi}S/m$, $\partial_{\imath}S/m$: a gradient | **in** | a force law, by differentiating the transport |
| Dirac, Proca | $ic\tilde U_{\Psi,\mathrm b}^{-2}$; $A_{\imath}/\varrho$: a direction | **in** | a force law, by projecting the frame's equation |
| $\mathrm{SU}(4)$ | $\Omega_{\imath}=U_{\mathrm{frm}}^{\dagger}D_{\imath}U_{\mathrm{frm}}\in\mathfrak{u}(4)$ | **on** | a momentum balance, no material derivative |

**Three ways of filling one slot, and the three are what the test sorts.** At the gradient rungs the transport law is a divergence of a current, and differentiating it gives the acceleration of a worldline: Euler. At the frame rungs the frame's equation is vector-valued and the fluid's acceleration is its component along the flow, so the slot is filled by a *projection* — defined only where the frame exists and only along the directions the flow selects. At the matrix rung the velocity is internal, the transport is a parallel transport in $\mathfrak{u}(4)$, and the slot is filled by the field equation itself, whose subject happens to be the vorticity.

**Why the internal case cannot produce a law, in one paragraph.** A force law is an equation for the acceleration of a trajectory. A trajectory needs a tangent vector that is an element of the base at each point, and a derivative along it. An internal velocity supplies neither: $\Omega_{\imath}$ is a connection on a bundle whose base is the event manifold, but its values are in $\mathfrak{u}(4)$ and its "derivative along the flow" is a covariant derivative on the *fibre*. The object that would play the role of $v^{\imath}\partial_{\imath}$ does not exist. **So the equation is a balance among fibre-valued objects, and a balance is not less than a law — it is a law of a different kind, one that relates a momentum's divergence to a curvature rather than an acceleration to a force.**

**The test is not "abelian versus non-abelian", and the article states this because the confusion is natural.** A non-abelian *base-valued* velocity — a fluid of charged particles with an $\mathrm{SU}(2)$ charge, say — has a material derivative and obeys Wong's equations, which are a force law with a non-abelian charge. An *internal* $\mathrm{U}(1)$ velocity would have none. The discriminator is where the velocity lives, not what group it takes values in. Wong's own equations are the proof: they are non-abelian and they are a law, because the probe moves on the base and only its charge is internal.

## The Five Steps Run on Five Fields

**The claim is that the five steps produce each rung's fluid, and the check is to run them and compare.** The matrix below is the article's centrepiece. Read down a column and it is one rung's derivation; read across a row and it is one step's version at five rungs.

| | Schrödinger | Klein–Gordon | Dirac | Proca | $\mathrm{SU}(4)$ |
| --- | --- | --- | --- | --- | --- |
| **S1 the action** | first order in time, kinetic $+\tfrac{h^{2}}{8\pi^{2}m}\lvert\nabla\tilde\Xi\rvert^{2}$, potential $V$ | second order, kinetic $+$ mass | first order, the Dirac kinetic term with the bispinor ideal | second order, kinetic $+\tfrac12m^{2}A^{2}$ | second order, $\mathrm{Tr}(D_{\imath}PD_{\imath}P)$ plus the eigenvalue potential |
| **S2 the word** | $\varrho e^{i\theta}\varepsilon e_t$, $2+1$ data | $\varrho e^{i\theta}\varepsilon e_t$ | $\varrho e^{i\theta}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$, $1+1+3+3$ | $\varepsilon i\varrho\tilde U_{\Psi,\mathrm b}$ | $U_{\mathrm{frm}}PU_{\mathrm{frm}}^{\dagger}$, $4+12$ |
| **S3 the types** | real central, central imaginary | same | four types | real central, Hermitian traceless | four eigenvalues, frame's twelve |
| **S4 the order** | phase first order, scale second | phase first order, scale second | phase first order, frame's | frame first order, scale second | frame's guidance algebraic, density second |
| **S5 the sort** | velocity is a gradient, **in** | velocity a four-gradient, **in** | velocity a direction, **in** | velocity a direction, **in** | velocity internal, **on** |
| **the output** | Euler with the quantum force | Euler with $\gamma^{-1}$ | the spin fluid's acceleration | Euler, projected | the momentum balance |

**Two readings of the matrix, and both are the article's point.** The columns differ — the words differ, the orders differ, the sorts differ — and the rows are the same operation. **The skeleton is the rows; the declension is the column.** A new Lagrangian is a new column, and the question of whether it is a fluid is the question of whether its column can be filled.

**The two ends of the table are the two hard cases, and they are hard for opposite reasons.** The Schrödinger rung is the one whose action is *first* order, so its Hessian vanishes and S4's language must be the kinetic matrix rather than the second variation; that is a fact about the rung and not a failure of the step. The $\mathrm{SU}(4)$ rung is the one whose velocity is internal, so S5 sends it to a balance; that is a fact about the rung too, and the corpus's own statement — "a fluid *on* the material sector and not *in* it" — is S5's output in the corpus's words.

**The middle three rungs are where the skeleton does the most work and gets the least credit.** At the Klein–Gordon rung S4 produces Euler with a $\gamma^{-1}$ factor, and the factor is the rung's signature: the velocity's magnitude is not free, so the acceleration law carries the price of the constraint. At the Dirac rung S4 produces the acceleration of a spin fluid, and the spin's contribution enters through the same type-slot map — the rotor's transport is the spin's equation, and it is a *transport* and not an acceleration, because the rotor is a coordinate whose equation is first order. At the Proca rung S4's output is a projection, and the projection is why the fluid's Euler equation is two of the frame's components and not all four.

**What the matrix does not show, and the honesty requires saying it.** The entries are stated at the level of what kind of object each step produces, not at the level of the formula. A reader who wants the formulas reads the five articles, and this matrix is an index to them. **The claim it supports is structural and not numerical**: that the five columns are the same five operations. The claim it does not support is that the equations are equal — they are not, and the differences are the rungs' physics.

## The Protocol: Running the Five Steps on a Lagrangian the Corpus Has Not Treated

**The skeleton is only an approach if it can be run on something new.** This section states the run as five questions, and the point of the questions is that each has a *failure mode*. A new Lagrangian either passes the five or names the step it breaks, and a broken step is a result.

### The Five Questions

| step | the question | the answer that passes |
| --- | --- | --- |
| S1 | is the action a pairing of logarithmic derivatives plus one algebraic term? | the two terms exist and the pairing is scalar |
| S2 | is the field invertible, and is the word a bijection onto its real parameters? | the count closes, $1+1+3+3=8$ or its rung's analogue |
| S3 | are the parts of $\mathcal A_{\imath}$ of distinct types, and does the pairing leave them unmixed? | the kinetic term is a sum of squares with no cross term |
| S4 | is a derivative available — is some coordinate's equation one order below the field equation's? | the guidance relation is first order, and the acceleration law can be manufactured from it |
| S5 | is the velocity a section of the base? | answered either way; the answer sorts the output, it does not fail the rung |

**S5 is the odd one out and the article marks it.** The first four are pass-or-fail; the fifth is a branch. A rung that passes S1 to S4 and reports "internal" at S5 has not failed — it has produced a balance, which is what its physics is. **The test does not grade a rung; it tells you what the rung's force equation will be.**

### The Five Failure Modes

| step | how it fails | what the failure means |
| --- | --- | --- |
| S1 | there is no action | a dissipative or phenomenological fluid; the skeleton does not apply |
| S2 | the field is constrained, or the word is not a bijection | the coordinates do not exist; the count does not close |
| S3 | the pairing mixes types | cross terms in the kinetic energy; the slot map is a system, not a list |
| S4 | every coordinate's equation is the field equation's order | no guidance relation to differentiate or project; there is no force slot to fill |
| S5 | — (a branch, not a failure) | — |

**The first failure mode is the corpus's own boundary, and the corpus has its members.** [Causal Dissipative Fluid Physics](causal-dissipative-fluid-physics-in-biquaternionic-form.html) is a fluid with no action: its Israel–Stewart equations are a relaxation of a first-order constitutive law, and no Lagrangian produces them. The skeleton's first question excludes it at once, and the exclusion is honest — the block is a fluid and not a Lagrangian fluid, and the two classes are different.

**The second failure mode is a real class and the corpus has its members.** A pure spinor has no density: $\varrho=0$ identically, the word degenerates, and the count does not close. A constrained field — a field on a constraint surface — has fewer coordinates than the word would give it. **The failure is not a defect of the field; it is the word telling you the field is not of the class.** The corpus's massless fluid is the sharpest case: at $N(\tilde\Xi)=0$ the label chart and the value chart both fail, and the failure is proved rather than observed.

**The third failure mode is the one a new Lagrangian is most likely to hit, and the article names the culprits.** Any term with two derivatives and two different types in it — a mixed Chern–Simons, a non-minimal coupling, a Pauli term with arbitrary coefficient — puts a cross term in the kinetic energy. The rung then has no slot list, and the derivation must be done by hand. **This is not a prohibition on such theories; it is a statement that the skeleton's shortcut does not apply to them.**

**The fourth failure mode is the one to watch for, because it looks like success.** A rung whose every coordinate's equation is second order has fluid slots and no force slot: it has a continuity-like equation for each coordinate and no transport to differentiate. **It is a set of coupled wave equations wearing a fluid's names**, and S4 is the step that tells them apart. The Dirac rung is the near miss: its equations are first order in time, so it has a transport, and it is the rung whose *rank* fails rather than whose order does — a difference the next subsection states.

### The Two Ways a Rung Can Be Ill-Defined, and Only One Is S4's

**A rung can fail to close for want of order, and it can fail to close for want of rank.** S4 detects the first: no first-order equation, no force. The second is a different test, and [Criterion for a Fluid Equation](criterion-for-a-fluid-equation-one-polar-coordinates-euler-lagrange-equation.html) owns it: the highest-derivative form must be nondegenerate on the physical subspace, and the Dirac rung's four vanishing momenta are the corpus's example of a rung that passes the count and fails the rank. **The skeleton's five steps do not include the rank test, and the article says so rather than pretending they do.** The five steps produce the slots; the rank test decides whether the slots are filled by equations that determine rates. A complete declension runs both, and the corpus's ladder table is the one place both verdicts are recorded side by side.

## The Classical Layer: The Count the Skeleton Has to Reproduce

**An ordinary fluid is the skeleton's degenerate case, and stating it fixes what the skeleton means.** The classical equations are not derived here — they are the base, written before any field was read as a fluid, and they sit in *The fluid's equations and their solutions* in *Biquaternion Universe Non Relativistic Non Quantum Approximation*. What belongs here is the one comparison that S2 makes possible, because the comparison is a count and the count is the test.

| Object | Data at a point | Removed by |
| --- | --- | --- |
| The element $\tilde\Xi$ | $8=1+1+3+3$ | — |
| A general fluid | $5$: $\rho_{\mathrm{num}}$, $\vec v$, $s_{\mathrm{spc}}$ | — |
| A barotropic fluid | $4$: no independent entropy | the law of state |
| A barotropic irrotational fluid | $2$: $\rho_{\mathrm{num}}$ and a potential | the vorticity |

**S2 closes at the top rung and at the bottom rung, and at no rung in between.** At the top the word's four factors and the fluid's five data are not equal — $8$ against $5$ — and the identification of scale with density, boost with velocity and rotor with spin is a map onto five of the eight, the remaining three being the ones no fluid variable answers to. At the bottom the counts agree exactly, $2=2$: a scale and a phase against a density and a potential. So the fluid of a field is **barotropic and irrotational by construction**, and that is not a modelling choice made per article. It is what the word is: one phase, and its gradient for the velocity, with no second thermodynamic datum anywhere in the algebra.

**The three data that do not survive are each removed by a named structure, and none is removed by counting.** The velocity has three components where the phase has one, and the excess is the vorticity: restoring it means replacing the one phase with the three Clebsch functions of a rank-two flow, which is a condition on the *rank* of the flow and not on its order — the second kind of ill-definedness this article separates from S4's. The entropy is a second thermodynamic datum, and the algebra carries one phase and no second thermal coordinate at all, so a non-barotropic fluid is outside the image for want of a variable. The pressure is not removed at all: it is a *term*, and a fluid that carries one is not in the image of the reverse map unless its stress also carries a second-gradient part. Each of the three is the subject of one article of the classical layer, and the three together are the map of what the reading discards.

**The classical layer is also where each of the five steps takes its limiting form, and the limits are worth stating because they are the skeleton's own boundary conditions.** S1 fails for the viscous fluid, and it is the only classical realisation of the failure mode "there is no action": the dissipation has a fixed sign under time reversal, so no functional of the flow alone produces it. S2 closes only at the bottom rung, as above. S3 has nothing to do at the classical layer, because the classical equations are written on a scalar and a vector and there is no type decomposition to respect. S4 has no spare derivative to spend: the temporal slot of the flow element carries the constant $ic$, there is no phase coordinate one order below, and the acceleration law is the *definition* of the material derivative rather than a law manufactured from a transport equation — which is exactly why the classical fluid has Euler's equation and no wave equation. S5 is answered before it is asked, because a classical velocity is a vector of the base, so the classical fluid is a law and not a balance.

**The consequence is a rule for everything above this section.** A field's fluid sits on the bottom rung or on a rung the word supplies, and when an article reports a rotational fluid, a non-barotropic one or a viscous one, it is reporting a departure from the reading and not a variation inside it. The classical articles exist so that each departure has a name in advance: vorticity, entropy and the law of state are the three names, and no article above them has to invent one.

## The Three Equivalences, Stated Separately

**The word "equivalent" is doing three jobs in this literature, and the article separates them because the skeleton depends on the separation.**

| question | the answer | why it matters here |
| --- | --- | --- |
| same **content**? | **yes**: the word is a bijection, so the two descriptions have the same solution set | S2's bijection is what makes the fluid chart lossless |
| same **warrant**? | **no**: a fluid equation is a coordinate's Euler–Lagrange equation; the equation route's output is a combination on the field equation | S3b's slot assignment is what the criterion grades |
| same **domain**? | **no**: the word is a bijection on the invertibles only, so the chart has a singular locus | S2's failure table is the chart's boundary |

**The first equivalence is the one that licenses the reading, and it is exact.** Because the map is one-to-one and onto, every solution of the field equation is a solution of the fluid equations and back. The fluid chart adds nothing and loses nothing. **A reader who suspects the corpus of substituting a different theory at each rung can be answered with the bijection**: the same solutions, re-coordinatised.

**The second equivalence is the one that makes the criterion a criterion, and it is where the corpus's methodological claim lives.** The equation route — multiply by $\tilde\Xi^{*}$, take the parts — produces continuity, an energy equation and a vorticity identity together, and it cannot say which of them to keep. **The action route can**, because only a coordinate's variation gives that coordinate's equation. The content is the same; the *selection* is not, and the selection is what a fluid reading needs.

**The third equivalence is the one that keeps the corpus honest, and it is asymmetric.** The field equation survives where the chart does not: at the zero-divisor cone, at the node, at the crossing. **The fluid is a chart with a singular locus, and the physics continues past it.** That asymmetry is why the corpus states its singular sets one by one rather than treating them as technicalities, and why a claim that "the fluid equations are the field equation" is true on the chart's domain and only there.

**The three, in one sentence.** *Same solutions, different warrant, smaller domain* — and a derivation that confuses them will claim either too much (that the fluid is a new theory) or too little (that it is only a rewriting).

## What This Article Does Not Claim

**That the skeleton is a theorem.** It is an extraction, and its warrant is that five independent derivations share it. A sixth field could walk the five steps and fail at a step for a reason the article does not anticipate, and that would be a result rather than a refutation. **The skeleton is a protocol with a stated boundary, not a law about fields.**

**That a fluid equation is a *better* equation than the field equation.** They are the same equation on the chart's domain, and the field equation is the one that survives where the chart does not. **The fluid reading is a reading**, and the article's claim is about which reading a slot belongs to, not about which is true.

**That the five steps derive the fluid equations from nothing.** Each rung's equations were already there. The derivation re-*derives* them by the action route so that the warrant is a variation and not a construction, and the content is unchanged. **A reader looking for a new prediction will not find one here**, and the corpus's honest position is that the fluid chart predicts nothing the field equation does not.

**That S4 is original to this article.** The sentence "Euler is not varied, it is differentiated" is the corpus's, and every rung that has a force slot performed S4 before this article named it. **What the article adds is that S4 is one claim at every rung — the acceleration law is never varied — that the second derivative of the fast coordinate lives in the force slot and nowhere else, and that S4's three kinds of term are not interchangeable.** The naming is the contribution; the mathematics is the rungs'.

**That the ladder closes uniformly.** It does not. Continuity's warrant degrades monotonically on the way up, and the top rung's continuity is an identity that fails in a stated sense. **The skeleton produces the slots at every rung; it does not promise that every slot is filled by a conservation law at every rung.** The ladder table records what each rung actually gets.

**That "fluid" is a claim about a medium.** Nothing here says the field *is* a material substance. The word names a chart in which certain quantities play the roles of density, flow, vorticity and pressure, and the corpus's discipline is to say which role each object plays and what would falsify the assignment. **The strongest statement the article makes is that five fields admit the same chart, not that any of them is made of anything.**

**That the protocol's failure modes are exhaustive.** They cover the failure modes the corpus has met: no action, no bijection, mixed types, no order reduction. A fifth kind could exist, and the protocol would then be incomplete rather than wrong.

## Open Questions

**Does the skeleton extend to a constrained system with a first-class algebra that is not a gauge theory?** The $\mathrm{SU}(4)$ rung's fifteen Gauss laws are first class and its counting is $60-2\times15=30$. A system whose constraints are second class would close differently, and S4's language — which coordinate's equation is first order — would need the Dirac bracket. Whether the five steps survive the replacement is not settled.

**Is S3a's diagonal pairing a consequence of the types or of the scalar pairing, and could a non-scalar pairing keep the slot map?** If the slot map survives a pairing that is not scalar, then S3a is weaker than the article states. The corpus has one test case — the informational reduction that is not cyclic — and it is a failure of invariance rather than of the slot map, so the question is open.

**What is the fluid of a field with a fermionic condensate?** The spinor rung's word is bosonic; a Grassmann-valued field has no $\varrho>0$. The corpus treats the spinor's fluid as a bilinear reading, and whether that is S2 or a different step is not settled.

**Does the order reduction of S4 have a gravitational analogue, where the "scale" is the conformal factor and the "phase" the frame?** The corpus's gravity category states a frame and a connection; whether the conformal factor's equation is the one whose order matches and the frame's is the one that is one low is not stated anywhere. If it were true, S4 would be a statement about any field theory with a polar decomposition, and the skeleton would be wider than the Lagrangian fluids.

**Can the protocol be mechanised?** The five questions are decidable on an action of the S1 form — the types are computable, the count closes or not, the orders are readable. A script that takes an action and returns the five answers would turn the protocol into a check, and the corpus's verification directory is where such a script would live.

## What This Article Adds and What It Relabels

**Adds.** The five-step skeleton as one statement, extracted from five independent derivations; **S4 as a named step**, with its content that the acceleration law is manufactured from a first-order guidance relation and never varied, that the second derivative of the fast coordinate lives in the force slot alone, and that the manufacturing is a differentiation at the gradient and matrix rungs and a projection at the frame rungs; **S5 as a branch** rather than a computation, with the base-versus-internal test that sorts a law from a balance and the explicit answer that the discriminator is where the velocity lives and not which group it takes values in; the **five-by-five matrix** that runs the steps on the five fields; the **protocol** — five questions with five failure modes, including the fourth that looks like success; and the **separation of the three equivalences**, with the third's asymmetry named.

**Does not add.** No new action, no new solution, no new equation at any rung. Every display is a sibling's, and the matrix is an index to the five articles rather than a computation.

**Relabels three phrases.** *"The polar substitution gives the fluid variables"* — it gives the coordinates, and the slots come from the types of their terms, which is S3b and not S2. *"The fluid equations are the field equation rewritten"* — same content, different warrant, and a smaller domain; the three are separate questions. *"The primordial fluid is a different kind of fluid"* — it is the same five steps, with an internal velocity, and S5 is the step that says so.

## Summary

**An equation is a fluid equation when it is one coordinate's Euler–Lagrange equation in the polar chart, and this article states the derivation that produces those equations at five rungs.** The derivation has five steps. The action is a pairing of logarithmic derivatives plus one algebraic term (S1). The polar word factorises the field into real parameters and is a bijection on the invertibles (S2). The parts of the logarithmic derivative have distinct types, the pairing is diagonal on them so the kinetic term is a sum of squares, and one variation per coordinate fills one slot per type (S3). The phase and the frame enter only through derivatives, so their equations are one order lower and leave a derivative available; the acceleration law is manufactured from them — differentiated where the velocity is a gradient, projected where it is a direction — and never varied (S4). And whether the velocity is a section of the base decides whether that slot holds a law or a balance (S5).

**Step three is two steps and step four is the one usually left out.** S3a is a statement about the action; S3b is a statement about the variation. S4 is the inverse of S2's order reduction, and it is the reason a force exists at every rung without a third term in the action. **The five steps are the skeleton; the rung is the column.**

**The skeleton is falsifiable and the article states the failures.** No action excludes the dissipative block. No bijection excludes the pure spinor and the constrained field. Mixed types cost the slot map. All-second-order equations give slots and no force. **Each failure names the step, and a named step is a result.**

**The three equivalences are separate.** Same solutions, different warrant, smaller domain. A derivation that merges them claims either that the fluid is a new theory or that it is only a rewriting, and it is neither.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\tilde\Xi$ | the field, an element of $\mathbb{B}$ or of a module over it |
| $\partial_{\imath}$ | the material sector's gradient, $\imath\in\{t,x,y,z\}$ |
| $\mathcal A_{\imath}=\tilde\Xi^{-1}\partial_{\imath}\tilde\Xi$ | the logarithmic derivative, one algebra element per direction |
| $\varrho$, $\theta_{\mathrm{pha}}$ | the scale and the phase: the two central coordinates |
| $\tilde U_{\Psi,\mathrm b}$, $\tilde u_{\mathrm r}$ | the boost and the rotor: the two frame coordinates |
| $\langle\cdot\rangle_{\natural}$ | the quaternionic (scalar) pairing the action integrates |
| $P=\mathrm{diag}(\rho_{1},\dots,\rho_{4})$, $U_{\mathrm{frm}}$ | the matrix rung's densities and frame |
| $\Omega_{\imath}=U_{\mathrm{frm}}^{\dagger}D_{\imath}U_{\mathrm{frm}}$ | the matrix rung's internal velocity |
| S1–S5 | the five steps of the skeleton |
| $\mathbb{B}_{\Phi}$ | the material sector, the base at every rung |

## Further Reading

- [Criterion for a Fluid Equation: One Polar Coordinate's Euler–Lagrange Equation, Not a Combination](criterion-for-a-fluid-equation-one-polar-coordinates-euler-lagrange-equation.html), the criterion this article's S3b serves, and the ladder table where both closure tests are recorded.
- [The Relativistic Quantum Space as a Fluid](the-relativistic-quantum-space-as-a-fluid.html), the object the skeleton is applied to, read before any state is put on it.
- [The Euler and Continuity Equations in Biquaternionic Form](the-euler-and-continuity-equations-in-biquaternionic-form.html), the classical layer's five data and three equations, against which the six slots are counted.
- [The Invariant Density: Which Pairing the Action Can Integrate](the-invariant-density-which-pairing-the-action-can-integrate.html), S1's pairing and the reason it is scalar.
- [The Domain of the Polar Decomposition: Invertible Elements and the Zero-Divisor Cone](the-domain-of-the-polar-decomposition-invertible-elements-and-the-zero-divisor-cone.html), S2's singular locus at the spinor and scalar rungs.
- [Differentiating a First-Order Transport Law: Force, Transport and Product-Rule Terms](differentiating-a-first-order-transport-law-force-transport-and-product-rule-terms.html), S4's three kinds of term, and the prohibition that the product-rule term is never a force.
- [Base-Valued versus Internal Flow Velocity: A Test Separating Force Laws from Momentum Balances](base-valued-versus-internal-flow-velocity-a-test-separating-force-laws-from-momentum-balances.html), S5 as its own subject.
- [The SU(4) Fluid Equations from the Primordial Action](su4-fluid-equations-from-the-primordial-action.html), the matrix rung where S4 produces a balance.
