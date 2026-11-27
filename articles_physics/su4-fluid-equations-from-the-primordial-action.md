# __The $\mathrm{SU}(4)$ Fluid Equations from the Primordial Action: Fifteen Vorticities, a Four-Component Condensate and One Covariant Continuity__

## Introduction

[The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html) writes the $\mathrm{SU}(4)$ action in one display, varies it, and obtains one equation and fifteen Gauss laws. It says nothing about a fluid, and neither does any other article of the primordial block: the block has a mechanics, a mass matrix, a potential and an instanton, and no hydrodynamics.

This article supplies the missing reading, and the reading is exact rather than analogical. **The Yang–Mills equation is the statement that the covariant divergence of an antisymmetric two-form equals a current, and the Bianchi identity is the statement that the two-form is a covariant curl.** Those are the two statements a fluid's vorticity satisfies: an antisymmetric derivative whose divergence is the source, and a curl whose exterior derivative vanishes. So the fifteen connections are read here as fifteen vorticity potentials, and the sixteen Weyl fields as the source that rides them.

**The rung's mark, and it is the reason the article is not an exercise in vocabulary.** At all eight earlier rungs of this collection the fluid was **one** object. The velocity was the field's phase-gradient, or its frame, or its direction; the vorticity was then derived from the velocity, and the only questions were whether it vanishes identically and what its transport law looks like. **Here the fluid is two objects.** The velocity comes from the condensate, through the frame of the scalar matrix's polar decomposition; the vorticity comes from the connection, and it is a fundamental field with its own equation. Neither is derived from the other, and the coupling is what relates them.

**The consequence, stated as the article's thesis.** Once the flow carries the charge it responds to, every conservation law splits in two. The covariant statements hold — continuity, Helmholtz, the conservation of the current. The ordinary statements fail, and **the failure is one and the same term in all three cases**: the connection contracted with the field it transports. That sentence is the article, and §*The Fifteen Divergences Are One Object* proves it for continuity, §*Helmholtz Fails Covariantly Only* for the vorticity, and §*The Gauss Law Is the Constraint* for the constraint.

**The strongest objection.** *Nothing in the fluid reading constrains the theory, so the reading is decoration; a fluid has a velocity, a density and an equation of state, and the fifteen connections supply none of the three.* The objection is right about what a fluid needs and wrong about what this action supplies. The density is the scalar matrix's eigenvalues, four of them, and this article computes their chart. The velocity is the frame, and the same computation gives it. The equation of state is $V(Ξ)$, which is a function of the four eigenvalues alone because the invariants $\operatorname{tr}Ξ^{n}$ are. The fifteen connections supply the vorticity, which a fluid also needs and which the earlier eight rungs had to derive. **So the count closes at this rung for the first time: a density, a velocity, an equation of state and a vorticity, all four present and all four independent.**

**Position in the block.** The variational companion of [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html), and the last rung of the fluid ladder whose eight matter rungs are [the Schrödinger pair](schrodinger-fluid-equations-from-the-polar-action.html), [the Klein–Gordon pair](klein-gordon-fluid-equations-from-the-polar-action.html), [the Dirac pair](spin-half-fluid-equations-from-the-dirac-polar-action.html) and [the Proca pair](spin-one-fluid-equations-from-the-proca-polar-action.html). Its nearest neighbour in structure is the charged vector rung, where the ordinary divergence of the field already failed to vanish and its value was the field's own amplitude. Here the failure is the exchange between the fifteen, and the amplitude is not what carries it.

## Conventions

**The conventions are the Lagrangian article's, restated so that every sign on this page is checkable from it alone.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_{\imath}^{2}=-e_t$; the coordinates are $R_{\imath}$, all indices are low, the measure is $d^4r$, and every contraction carries its weight: $\sum_{\imath}\varepsilon_{\imath}$ with $\varepsilon_{\imath}=(1,-1,-1,-1)$.

The algebra and the generators. $t_{a}$, $a=1,\dots,15$, are the normalised Hermitian generators with $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$; the printed anti-Hermitian arrays $G_{a}$ and the integer rotation $A_{j}=\sum_{k}M_{k}-2M_{j}$ are what the normalisation is computed from and never what a coefficient is read off. The bracket is $[t_{a},t_{b}]=i\sum_{c}F^{c}{}_{ab}t_{c}$, with $F$ totally antisymmetric.

The connection and the curvature. $A_{\imath}=\sum_{a}A_{a,\imath}t_{a}$ Hermitian, the covariant derivative $D_{\imath}=\partial_{\imath}-ig_{4}A_{\imath}$, and

$$
\mathbb{F}_{\imath\jmath}=\partial_{\imath}A_{\jmath}-\partial_{\jmath}A_{\imath}-ig_{4}[A_{\imath},A_{\jmath}],
\qquad
[D_{\imath},D_{\jmath}]=-ig_{4}\mathbb{F}_{\imath\jmath},
\qquad
\mathbb{F}_{\imath\jmath}=\sum_{a}F_{a,\imath\jmath}t_{a},
$$

so that $F_{a,\imath\jmath}$ is real and $\mathbb{F}$ Hermitian. The coupling $g_{4}$ is one number for the whole group. The scalar is $Ξ$, a Hermitian $4\times4$ with $16$ real components, transforming as $Ξ\mapsto UΞU^{\dagger}$, and its covariant derivative is $D_{\imath}Ξ=\partial_{\imath}Ξ-ig_{4}[A_{\imath},Ξ]$.

**The two objects the article adds.** The **frame** is $U\in\mathrm{U}(4)$ in $Ξ=UPU^{\dagger}$ with $P=\mathrm{diag}(\rho_{1},\dots,\rho_{4})$ real, and the **frame velocity** is the covariant logarithmic derivative

$$
\Omega_{\imath}=U^{\dagger}D_{\imath}U=U^{\dagger}\partial_{\imath}U-ig_{4}U^{\dagger}A_{\imath}U .
$$

It is anti-Hermitian, it is invariant under a constant relabelling of the frame, and its off-diagonal entries are the flow's internal velocities. The four $\rho_{k}$ are the densities, ordered $\rho_{1}\ge\dots\ge\rho_{4}$, and each is non-negative on the branch where $P$ is positive semidefinite.

## The Action in the Fluid Chart

**Seven terms, and only four of them carry fluid content.**

| piece | what it is | what it is in the fluid |
| --- | --- | --- |
| $-\tfrac14\sum_{a,\imath,\jmath}F_{a,\imath\jmath}F_{a,\imath\jmath}$ | the fifteen | the vorticity's own energy and transport |
| $\sum_{f}\bar\xi_{f}(-i\sum_{\imath}\varepsilon_{\imath}\gamma_{\imath}D_{\imath})\xi_{f}$ | the sixteen | the source that rides the flow |
| $\operatorname{tr}(D_{\imath}Ξ)^{\dagger}(D_{\imath}Ξ)$ | the condensate | the four densities' gradients and the frame's velocity |
| $V(Ξ)$ | the condensate | the equation of state |
| $\mathcal{L}_{\mathrm{gf}}+\mathcal{L}_{\mathrm{gh}}$ | the representative | the gauge choice, no fluid content |
| $\mathcal{L}_{\mathrm{Yuk}}$ | source and condensate | the source's mixing, no fluid content at this order |

**Why this table is not a redescription.** Three of the four fluid objects come from one term each and no term supplies two. The densities and the frame come from the same term but decouple in the chart, which §*The Condensate in Its Eigenvalue Chart* computes. The vorticity comes from a term of its own and from no derivative of the condensate. **So the action's term structure is already the fluid's object structure**, and that is a statement about the action rather than about the reading.

**What "one force" means in the chart.** The coupling $g_{4}$ appears twice and the identity of the two appearances is the whole content of the phrase *one force*: it appears once in the vorticity, through the commutator in $\mathbb{F}$, and once in the frame's velocity, through the $g_{4}$ of $\Omega_{\imath}$. **In fluid language the sentence is: the vorticity and the velocity's transport are built from the same $g_{4}$, so the Euler equation is nonlinear in the flow.** At the eight earlier rungs the coupling appeared once, in the matter bracket, and the vorticity was a derivative of the same field that carried the velocity; there was nothing for a second appearance to be identical to. **Here the second appearance is what makes the fluid self-interacting, and its absence is exactly the abelian case**, where $\mathbb{F}=\mathrm{d}A$, the vorticity is the curl of a potential, and the Euler equation is linear.

## The Rung's Mark: Two Objects Where the Eight Had One

**The eight rungs, in one sentence each.** The Schrödinger rung's velocity is the phase gradient and its vorticity vanishes identically. The Klein–Gordon rung's is a four-gradient with a rapidity in the potential and its vorticity is the field strength on the central class. The Dirac rung's is a frame element and its vorticity is the frame's Maurer–Cartan form. The Proca rung's is a direction and its vorticity is the curl of the current. **In every case the vorticity is a function of the velocity**, so the fluid has one field and the vorticity's dynamics is the velocity's dynamics.

**Here the two are independent.** The velocity $\Omega_{\imath}$ is built from $Ξ$'s frame; the vorticity $F_{a,\imath\jmath}$ is built from $A_{a,\imath}$; and the equation of motion is an equation for the vorticity, not for the velocity. **So the rung's mark is a change in which object the equation is about**, and that is sharper than any change of coefficients.

**Three statements follow, and each is a section below.**

*The vorticity is not created, it is counted.* No question of baroclinic generation arises, because the vorticity is initial data. What the equation says is how the vorticity is transported by the flow and sourced by the current.

*The velocity has no equation of its own.* The four densities obey wave equations with the frame's velocity as a source; the frame obeys the equation that makes it a frame, which is algebraic in the chart. **A fluid whose velocity is a frame and whose vorticity is a connection is a fluid with a kinematic constraint and a dynamical vorticity**, and the constraint is not a gauge choice.

*The current is the only place the two meet.* The Euler equation's right-hand side is $j_{a}$, which is the fermion bilinear plus $2i\operatorname{tr}((D_{\jmath}Ξ)[t_{a},Ξ])$; the second term is linear in the frame's velocity, so the vorticity is sourced by the velocity's own rotation. **That is the fluid's statement of the Higgs mechanism's kinematics**: the condensate's frame current is what the vorticity responds to.

## The Euler Equation, and the Continuity That Is Covariant

**The equation, as the Lagrangian article writes it.**

$$
\sum_{\imath}\varepsilon_{\imath}D_{\imath}F_{a,\imath\jmath}=+g_{4}\,j_{a,\jmath},
\qquad
j_{a,\jmath}=\sum_{f}\bar\xi_{f}\gamma_{\jmath}t_{a}\xi_{f}
+2i\operatorname{tr}\bigl((D_{\jmath}Ξ)[t_{a},Ξ]\bigr).
$$

**The spatial components are the Euler equation.** A vorticity whose covariant divergence is a current is a vorticity carried by a flow and stressed by a source; the fifteen components are the fifteen internal directions, and the statement is component by component.

**The covariant derivative in the equation is not a convenience.** Writing it out,

$$
\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}F_{a,\imath\jmath}
=-\sum_{\imath}\varepsilon_{\imath}g_{4}f_{abc}A_{b,\imath}F_{c,\imath\jmath}+g_{4}j_{a,\jmath},
$$

so the ordinary divergence of the vorticity is **not** the current: the commutator term is an extra stress. **The fluid statement is that the vorticity is transported by the flow, and the transport term is the connection's action on it.** In an abelian fluid the transport term is absent and the vorticity's divergence is the current; that is the difference between a fluid whose vorticity is a passive field and a fluid whose vorticity carries the charge it responds to.

**The continuity equation, and where it comes from.** Take the covariant divergence of the equation. The left side vanishes identically, because $\sum_{\jmath}\varepsilon_{\jmath}D_{\jmath}\sum_{\imath}\varepsilon_{\imath}D_{\imath}\mathbb{F}_{\imath\jmath}=\tfrac12\sum_{\imath\jmath}\varepsilon_{\imath}\varepsilon_{\jmath}[D_{\imath},D_{\jmath}]\mathbb{F}_{\imath\jmath}$ and the commutator is antisymmetric against the antisymmetric $\mathbb{F}$. So

$$
\sum_{\imath}\varepsilon_{\imath}D_{\imath}j_{a,\imath}=0 .
$$

**This is the fluid's continuity equation, and it is covariant.** Three things about it are worth the ink.

*It is an identity of the vorticity and not a variation.* Continuity is not one of the fifteen equations; it is what they say when contracted with the gradient. **So this fluid has no separate continuity equation to solve**: the current's conservation is a consequence of the vorticity's antisymmetry, and the density's own equation is elsewhere — it is the wave equation of §*The Equation of State*, and not this line.

*It is covariant, so it is not a conservation law.* The ordinary divergence is not zero:

$$
\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}j_{a,\imath}
=i\,g_{4}\sum_{b,c}f_{abc}\sum_{\imath}\varepsilon_{\imath}A_{b,\imath}j_{c,\imath},
$$

and the right-hand side is the connection contracted with the current in the adjoint. **The fluid exchanges charge with its own flow**, and the exchange term is not small: it is the same order as the current.

*The failure is the same term as the vorticity's extra stress.* Compare the two displays: the vorticity's ordinary divergence carries $f_{abc}A_{b}F_{c}$, and the current's carries $f_{abc}A_{b}j_{c}$. **One object, two occurrences, one reason**: the connection is charged under itself.

## The Fifteen Divergences Are One Object, and There Is No Charge

**The claim.** The fifteen failures are not fifteen independent facts. The right-hand side of the display above is $i\,g_{4}\sum_{b,c}f_{abc}\sum_{\imath}\varepsilon_{\imath}A_{b,\imath}j_{c,\imath}$, which is the adjoint commutator $\sum_{\imath}\varepsilon_{\imath}[A_{\imath},j_{\imath}]$ read in components. **So there is one failure and fifteen components of it**, and the failure is the connection contracted with the current in the representation the current carries.

**The consequence, and it is a negative one.** A fluid conserves its densities component by component; this one does not. Suppose a linear combination $\sum_{a}c_{a}j_{a,\imath}$ were ordinarily conserved. Its divergence is $i\,g_{4}\sum_{a,b,c}c_{a}f_{abc}\sum_{\imath}\varepsilon_{\imath}A_{b,\imath}j_{c,\imath}$, and for this to vanish for every field the coefficients must satisfy $\sum_{a}c_{a}f_{abc}=0$ for every pair $(b,c)$. That condition says $[\sum_{a}c_{a}t_{a},t_{b}]=0$ for every $b$: the element $\sum_{a}c_{a}t_{a}$ would be central. **$\mathfrak{su}(4)$ is simple and has no central element, so $c=0$.** There is no ordinarily conserved combination of the fifteen, and the check is one line of the structure constants rather than an enumeration.

**Why this is the fluid's version of a sentence the Lagrangian article already prints.** That article says the ordinary divergence is not zero and that **above $M_{C}$ there is a current and no charge**. The fluid chart says the same thing in its own vocabulary: a charge is a conserved density, a conserved density is a closed combination of the fifteen, and no combination closes. **The fifteen transport one another and conserve nothing**, and the reason is the simplicity of the algebra and not a property of the fields.

**What happens below $M_{C}$.** The residual algebra is nine-dimensional, its generators are exactly the nine that commute with the vacuum $P_{0}$, and those are the ones whose action on the chart leaves the degenerate pairs alone. **The charge returns when the residual algebra does**, and the count of it is the count of generators the condensate does not move — nine, which the same table gives.

**The objection.** *A conservation law that fails is not a conservation law, so the fluid has no continuity equation at all.* It has one and it is covariant: $\sum_{\imath}\varepsilon_{\imath}D_{\imath}j_{a,\imath}=0$ holds identically, off shell and on. **What fails is the ordinary version, and the ordinary version is what a fluid's continuity equation usually is.** The article therefore says precisely what it means: the fluid's continuity holds in the covariant sense and its ordinary form measures exchange, and no exchange-free component exists.

## Helmholtz Fails Covariantly Only

**The Bianchi identity is the fluid's statement that the vorticity is a curl.** $D_{\imath}\mathbb{F}_{\jmath\kappa}+D_{\jmath}\mathbb{F}_{\kappa\imath}+D_{\kappa}\mathbb{F}_{\imath\jmath}=0$ holds for every connection. Written with ordinary derivatives,

$$
\partial_{\imath}F_{a,\jmath\kappa}+\partial_{\jmath}F_{a,\kappa\imath}+\partial_{\kappa}F_{a,\imath\jmath}
=g_{4}f_{abc}\bigl(A_{b,\imath}F_{c,\jmath\kappa}+A_{b,\jmath}F_{c,\kappa\imath}+A_{b,\kappa}F_{c,\imath\jmath}\bigr),
$$

so the ordinary version of the identity fails, and **it fails by the same term as before**: the connection contracted with the field, summed cyclically.

**Three readings of one line.** The abelian identity $\mathrm{d}F=0$ says the vorticity is the curl of a potential, hence that vortex lines cannot end, hence Helmholtz's first theorem. The covariant identity says the same thing covariantly: the vorticity is the covariant curl of the connection, and the covariant vortex lines do not end. **The ordinary statement is false**, and its failure is the commutator.

**What replaces Helmholtz's second theorem.** Circulation is materially conserved in an ideal fluid because the vorticity is frozen into the flow. Here the vorticity is frozen into the flow *covariantly*, and the ordinary circulation changes by the connection's transport. **The fluid statement is that the vortex lines are transported by the flow and simultaneously rotated by the connection**, and the two are different because the connection's rotation is a gauge rotation.

**The sharp break with the eight.** At those rungs the vorticity was either identically zero (Schrödinger), an identity of the chart (charged Schrödinger), or a derived object whose transport was the velocity's transport (Dirac, Proca). **Here the vorticity has an equation of its own, first order in the vorticity, and it is the equation of motion.** Helmholtz's theorems become statements about that equation's structure constants rather than about the velocity's.

## The Gauss Law Is the Constraint, and the Fluid Is Not Incompressible

**The temporal component.** $\sum_{\imath}\varepsilon_{\imath}D_{\imath}F_{a,\imath t}=+g_{4}j_{a,t}$ contains no second time derivative of $A_{a,t}$, so it fixes $A_{a,t}$: fifteen constraints, each first class, each removing two of the four components.

**In the fluid chart this is the multiplier.** $A_{a,t}$ is the scalar potential, and the constraint is elliptic: it determines $A_{a,t}$ from the charge distribution at once. **A fluid whose multiplier is fixed by an elliptic equation with the charge as its source is a fluid with an instantaneous pressure**, and that is the structure of an incompressible fluid — with one difference that matters.

**The difference.** In an incompressible fluid the constraint is that the velocity's divergence vanishes and the pressure is the multiplier. Here the constraint is that the *electric* divergence equals the charge, and what is fixed is the longitudinal part of the field. **So the fluid is not incompressible; it is charge-constrained.** The divergence that is set is not the flow's but the field's, and the setting is by the source rather than to zero.

**Why this is the rung the Proca pair predicted.** At the vector rungs the free fluid was incompressible and the charged one was not, and the reason was that the Lorenz condition was the mass's gift: no mass, no condition. **The fifteen have no mass term** — the Lagrangian article lists that absence first, and gives the reason, that a mass term is not invariant. **So there is nothing to set a divergence to zero, and the constraint that survives is the Gauss law.** The fluid's compressibility is a consequence of the group's structure and not of a choice, and the abelian limit does not restore it: the photon has no fluid, as the vector article says, and the fifteen have a fluid with an elliptic constraint instead.

## The Condensate in Its Eigenvalue Chart: Four Densities and One Frame

**The decomposition.** $Ξ=UPU^{\dagger}$ with $U\in\mathrm{U}(4)$ and $P=\mathrm{diag}(\rho_{1},\dots,\rho_{4})$ real. The stabiliser is the four diagonal phases, so the frame has $16-4=12$ physical parameters, and with the four densities the count is $16$ — the scalar's real components, exactly.

**The computation.** With $\Omega_{\imath}=U^{\dagger}D_{\imath}U$ and $[Ω,P]_{kl}=Ω_{kl}(\rho_{l}-\rho_{k})$,

$$
U^{\dagger}(D_{\imath}Ξ)U=\partial_{\imath}P+[Ω_{\imath},P],
$$

and the cross term between the two pieces vanishes because $[Ω,P]$ has zero diagonal. So

$$
\operatorname{tr}\bigl(D_{\imath}Ξ\bigr)^{\dagger}\bigl(D_{\imath}Ξ\bigr)
=\sum_{k}\bigl(\partial_{\imath}\rho_{k}\bigr)^{2}
+\sum_{k\ne l}\bigl|\Omega_{\imath,kl}\bigr|^{2}\bigl(\rho_{k}-\rho_{l}\bigr)^{2}.
$$

**Two statements, and the second is the article's.**

*The densities and the frame decouple.* The four densities' gradients appear alone, with no cross terms and no connection. **A four-component fluid whose species share one frame has no relative kinetic energy except through the frame**, and that is exactly what the display says.

*The connection reaches the frame and never the densities.* Every appearance of $A$ is inside $\Omega$, and $\Omega$'s off-diagonal entries are weighted by $(\rho_{k}-\rho_{l})^{2}$. **So the force couples to the flow's internal rotation and to nothing else**, and the two consequences are the next two sections.

**The identity direction is invisible, and this is the Lagrangian article's sentence proved in one line.** Replace $A_{\imath}$ by $A_{\imath}+c_{\imath}\mathbb{1}$. The off-diagonal entries of $U^{\dagger}A_{\imath}U$ do not change, so the off-diagonal entries of $\Omega_{\imath}$ do not change either; the diagonal of $\Omega_{\imath}$ shifts by $-ig_{4}c_{\imath}$, and the diagonal enters the display only through the weight $(\rho_{k}-\rho_{l})^{2}$ at $k=l$, which is zero. **So the display is unchanged.** The $\mathrm{U}(1)$ direction of the connection does not couple to a Hermitian scalar at all, because a Hermitian matrix has no charge under the overall phase. The Lagrangian article states the same thing as "the identity part of the vacuum is invisible to the force"; here it is a computation in the chart, and the chart shows it is a structural zero and not a small number.

**The centrifugal reading.** For one complex scalar the same computation gives $(\partial\varrho)^{2}+\varrho^{2}(\partial\theta-gA)^{2}$, and the $\varrho$-equation's $\varrho(\partial\theta-gA)^{2}$ term is the centrifugal force of the phase's rotation. **The display is the four-density version of that term**: the frame's rotation pushes the densities apart where the splitting is largest, and it does not act at all where the densities are equal.

## The Six Heavy Vectors Are Six Stratified Frame Directions

**The count, from the chart.** Each unordered pair $(k,l)$ carries one complex off-diagonal entry $U_{kl}$, that is two real directions; twelve in all, and $4+12=16$.

**The splitting decides which of them are heavy.** At the vacuum $P_{0}=\mathrm{diag}(v,v,v,-3v)$ — the traceless direction the potential chooses — three pairs are split and three are degenerate. The display's weight $(\rho_{k}-\rho_{l})^{2}$ is therefore nonzero on the first three, which is $3\times2=6$ real directions, and zero on the last three, which is another $6$.

**The identification.** The six split directions are the six that acquire a mass from the gauge-kinetic term: with $Ω=U^{\dagger}\partial U-ig_{4}U^{\dagger}AU$, the weight multiplies $g_{4}^{2}|(U^{\dagger}AU)_{kl}|^{2}$ and the off-diagonal components of the connection acquire the coefficient $g_{4}^{2}(\rho_{k}-\rho_{l})^{2}$. **So the six heavy vectors and the six eaten directions are the same six, and the mass is the fluid's stratification stiffness.** The Lagrangian article's arithmetic — sixteen real scalars, six eaten, ten surviving — is in the chart: $4$ densities $+\ 6$ degenerate frame directions $=\ 10$.

**Why this belongs in a fluid article.** Because it says what the mass of a heavy vector is: **the frame's inertia against a density difference.** A vector that rotates the frame in a direction where the fluid is uniform costs nothing; a vector that rotates it in a direction where the fluid is stratified costs $g_{4}^{2}(\rho_{k}-\rho_{l})^{2}$ per unit field. **That is a fluid statement of the Higgs mechanism**, exact at this level and gauge-invariant by construction, since it is written in the eigenvalues.

**The objection.** *This is the standard Higgs mechanism in a gauge-variant chart, so nothing is gained.* The mechanism is standard and the chart is gauge-invariant, which is the point: the display above is invariant under $U\to UW$ with $W$ a constant unitary, and the connection enters only through $\Omega$, which is a covariant object. **What the chart adds is the location of the mass**: not in a potential evaluated at a vacuum expectation value, but in the coefficient of a flow's rotation, weighted by a density splitting.

## The Equation of State: Four Pressures and No Baroclinic Torque

**The potential in the chart.** Every invariant $\operatorname{tr}Ξ^{n}$ is $\sum_{k}\rho_{k}^{n}$, so

$$
V=\mu_{\Phi}^{2}\sum_{k}\rho_{k}^{2}+\mu_{2}^{2}\Bigl(\sum_{k}\rho_{k}\Bigr)^{2}
+\lambda_{1}\sum_{k}\rho_{k}^{4}+\lambda_{2}\Bigl(\sum_{k}\rho_{k}^{2}\Bigr)^{2}
+\lambda_{3}\Bigl(\sum_{k}\rho_{k}\Bigr)^{2}\sum_{k}\rho_{k}^{2}+\lambda_{4}\Bigl(\sum_{k}\rho_{k}\Bigr)^{4},
$$

a function of the four densities and of nothing else.

**So the equation of state is barotropic in the only sense available at this rung: no velocity enters it.** The potential carries no derivative of any kind, and the kinetic term is the only place a derivative appears. **And so the baroclinic torque vanishes**: the force is $-\partial V/\partial\rho_{k}$, a gradient in the density coordinates, so the pressure's gradient and the density's gradient are parallel pair by pair and their wedge is zero.

**But the baroclinic question is moot here, and the article says why rather than claiming a triumph.** At the eight rungs the vorticity was a derived object and the question was whether a flow started from rest could generate it; the answer was always no, for the same reason. **Here the vorticity is not derived and is never generated: it is initial data, constrained only by the Gauss law.** The absence of a baroclinic torque is therefore the statement that the *condensate* cannot rotate its own vorticity — a statement about the source term of the vorticity's equation, not about the vorticity's existence.

**What the four-density equation of state does say.** The pressure is anisotropic by construction: there is a pressure per density, $\partial V/\partial\rho_{k}$, rather than one scalar. **A four-density fluid with four pressures is a fluid with four sound speeds**, and the four are the eigenvalues of the Hessian $\partial^{2}V/\partial\rho_{k}\partial\rho_{l}$ along the physical directions. The Lagrangian article says the potential's six coefficients are free and that the group does not fix them; the fluid statement is that they fix four sound speeds and two mixing angles, and that the flat directions of the Hessian are the fluid's instabilities.

**The density's equation.** Varying $\rho_{k}$ in the chart,

$$
\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}\partial_{\imath}\rho_{k}
=-\tfrac12\frac{\partial V}{\partial\rho_{k}}
+\sum_{l\ne k}\bigl(\rho_{k}-\rho_{l}\bigr)\sum_{\imath}\varepsilon_{\imath}\bigl|\Omega_{\imath,kl}\bigr|^{2},
$$

with the $\tfrac12$ the kinetic term's normalisation and not a physics statement. **Three terms and three readings**: the left side is the density's own inertia, the second term is the pressure's force with the minus a force carries, and the third is the frame's centrifugal drive — the same object as the $\varrho(\partial\theta-gA)^{2}$ of the one-scalar case, weighted by the splitting, and it is diagonal in the densities because the eigenvalues decouple.

**What is absent, and deliberately.** There is no Bohm term of the Madelung shape in the equation as written, because the display above is the equation for the density and not for its square root; dividing by $\rho_{k}$ produces the usual $-\Delta\rho_{k}/2\rho_{k}$ and nothing else. **The fluid's quantum stress at this rung is diagonal in the density basis**, and that is a consequence of the chart and not of an approximation.

## The Helicity Term

**The one dimension-four term the display does not write.** $\operatorname{tr}(\mathbb{F}\wedge\mathbb{F})$ is a total derivative, $\mathrm{d}\,\mathrm{CS}(A)$ with $\mathrm{CS}$ the Chern–Simons three-form, and its integral is quantised. It is admitted by the group and its coefficient $\theta_{4}$ is free.

**In the fluid chart it is the helicity.** In the abelian case $\int A\wedge\mathrm{d}A=\int\vec A\cdot\vec B$ is exactly the fluid's helicity, the linkage number of the vortex lines, and the non-abelian version is the same construction with the trace and the commutator inside $\mathbb{F}$. **So $\theta_{4}$ is the coefficient of the flow's helicity**, and the quantisation of its integral is the statement that helicity is a counting invariant of the vorticity and not a continuous charge.

**Two consequences, both of them the Lagrangian article's, restated.** A total derivative does not enter the local equations, so **the helicity term does not change the fluid's equations at all**: it labels the flow's topology and nothing in §*The Euler Equation* moves. And its redundancy above $M_{C}$, where a chiral rotation of the sixteen removes it, reads as: the helicity label can be shifted by relabelling the source's chirality, which is possible exactly when the source is massless.

**What is not claimed.** The identification of $\theta_{4}$ with a fluid helicity is an identification and not a derivation, and the article labels it. What is derived is the total-derivative property and the resulting absence from the equations.

## The Fermions Are the Source

**A scope statement, so that the reading is not overextended.** The sixteen Weyl fields enter the fluid only through $j_{a}$ and through the Yukawa matrix. **They are not a second fluid here.** The alternative chart — the sixteen read as sixteen zitterbewegung flows, each with its own density and its own vorticity — is the spin-half article's chart, and it is a different chart of the same action, not a correction to this one.

**What the source does to the fluid.** It carries the charge the vorticity responds to; it is transported by the same $g_{4}$; and its ordinary divergence is not zero either, for the same commutator reason. **So the source rides the flow and exchanges with it**, and the fluid's Euler equation is not homogeneous. **At the eight rungs the source was the fluid**; here the fluid is the vacuum's condensate and the source is matter, and that division is the rung's largest change of vocabulary.

## What This Rung Adds to the Eight

| rung | what the field is | the velocity | the vorticity | continuity |
| --- | --- | --- | --- | --- |
| Schrödinger | a wavefunction | the phase gradient | zero, identically | the phase's equation |
| Klein–Gordon | a wavefunction | a four-gradient | the central class's field strength | the phase's equation |
| Dirac | a spinor | a frame element | the frame's Maurer–Cartan form | the phase's equation |
| Proca, free | the current | the field's direction | the curl of the current | the Lorenz condition, an identity |
| Proca, charged | the current, complex | the frame | the covariant curl | the covariant Lorenz condition |
| $\mathrm{SU}(4)$ | the vorticity's potential | the condensate's frame | the connection's curvature, dynamical | covariant, with the exchange as its failure |

**Three things the table makes visible.** The velocity's source moves from the field to the condensate. The vorticity moves from derived to fundamental. And continuity moves from an equation to an identity — and then, at this rung, to an identity that is covariant and whose ordinary version measures exchange.

**The one thing that does not change.** At every rung the fluid's equations are obtained by varying an action and reading which term supplies which object. **That is the identity the collection exists to establish**, and this rung is its last and largest instance: fifteen vorticity fields, four densities, one frame, one $g_{4}$.

## Objections

**"A fluid has one velocity; this has none."** The velocity is $\Omega_{\imath}$, the condensate's covariant frame derivative, and it is a single object with twelve internal components. The fifteen connections are not fifteen velocities; they are one vorticity with fifteen internal components. **The mode count is the check**: $30$ transverse polarizations for the fifteen, $16$ real for the condensate, $32$ for the source, and the fluid's objects account for all of them.

**"Calling $\mathbb{F}$ a vorticity is a metaphor, since there is no velocity whose curl it is."** It is not a metaphor at the level of the identities: $\mathbb{F}$ is antisymmetric, its covariant divergence is the source, and its covariant cyclic sum vanishes — those three are the definition of a vorticity in the sense the eight rungs used. **What is genuinely metaphorical is the material reading of the vortex lines**, and the article says so in §*Helmholtz Fails Covariantly Only*: the lines are transported by the flow, but they are not the flow's own lines, because the flow's velocity and the vorticity's potential are different objects.

**"The eigenvalue chart degenerates at level crossings, so it cannot be a chart of the physics."** It cannot be a global chart, and the degeneracy is physical: at $\rho_{k}=\rho_{l}$ the frame's identification of that pair fails and the connection's coupling to it vanishes. **The chart's singularity and the restoration of the symmetry are the same point**, which is why the chart is worth using: it shows the two as one.

**"None of this constrains $\mathrm{SU}(4)$, so it is decoration."** Correct, and it is the same status the Lagrangian article claims for its display: transcription and not derivation. **The fluid reading is a change of chart of a transcribed action**, and its content is the location of each object in a term, not a new equation.

## Open Questions

**The velocity potential's global existence.** Inverting $\mathbb{F}=\mathrm{d}A-ig_{4}[A,A]$ for $A$ requires the covariant Poincaré lemma, and it fails on a nontrivial bundle. **So the fluid's vorticity potential is a patch object**, and on the instanton the patches do not glue. Whether the fluid reading survives as a description of a patchwise flow, or whether the instanton is where the reading ends, is not settled.

**The four densities' flow at a crossing.** At $\rho_{k}=\rho_{l}$ the frame's two directions degenerate and the effective description has a residual $\mathrm{U}(2)$ on that pair. **Whether the fluid at the crossing is a four-fluid with a symmetry or a two-fluid with a doubled label** is not settled, and the answer decides what the transition looks like in fluid language.

## Summary

The $\mathrm{SU}(4)$ action's fluid reading has four objects and one coupling. The densities are the four eigenvalues of the scalar matrix's polar decomposition; the velocity is the frame's covariant logarithmic derivative $\Omega_{\imath}=U^{\dagger}D_{\imath}U$; the equation of state is $V$ of the four eigenvalues, hence barotropic with four pressures; and the vorticity is the fifteen connections' curvature, which is a fundamental field with its own equation rather than a derived object.

The kinetic term's chart is the article's one computation and it carries three results: the densities and the frame decouple, with cross terms vanishing because $[Ω,P]$ has zero diagonal; the connection reaches the frame only, weighted by the eigenvalue splittings; and the identity direction of the connection is invisible to a Hermitian condensate, which is the Lagrangian article's "identity part of the vacuum" as a structural zero.

The conservation laws are all covariant and all fail ordinarily by one term, the connection contracted with the field it transports. Continuity fails by $f_{abc}A_{b}j_{c}$; Helmholtz fails by $f_{abc}A_{b}F_{c}$; and no combination of the fifteen is ordinarily conserved, because a closed combination would be a central element of a simple algebra.

The constraint is the Gauss law and not incompressibility, because the fifteen have no mass term and there is nothing to set a divergence to zero. The six heavy vectors are the six frame directions the vacuum's eigenvalue splitting singles out, with mass $g_{4}^{2}(\rho_{k}-\rho_{l})^{2}$: the Higgs mechanism read as the frame's inertia against a density difference. The helicity term is $\theta_{4}$, a total derivative that does not enter the equations, and the fermions are the source and not a second fluid.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $Ξ=UPU^{\dagger}$ | the scalar's polar decomposition; $U$ the frame, $P=\mathrm{diag}(\rho_{k})$ the densities |
| $\rho_{k}$, $k=1,\dots,4$ | the four densities, the eigenvalues, ordered |
| $\Omega_{\imath}=U^{\dagger}D_{\imath}U$ | the frame velocity, covariant, anti-Hermitian |
| $A_{\imath}=\sum_{a}A_{a,\imath}t_{a}$ | the connection, Hermitian; the vorticity potential |
| $\mathbb{F}_{\imath\jmath}$ | the vorticity, $\partial_{\imath}A_{\jmath}-\partial_{\jmath}A_{\imath}-ig_{4}[A_{\imath},A_{\jmath}]$ |
| $g_{4}$ | the one coupling; appears in $\mathbb{F}$ and in $\Omega$ |
| $j_{a,\jmath}$ | the current: a fermion bilinear plus $2i\operatorname{tr}((D_{\jmath}Ξ)[t_{a},Ξ])$ |
| $\sum_{\imath}\varepsilon_{\imath}D_{\imath}F_{a,\imath\jmath}=+g_{4}j_{a,\jmath}$ | the Euler equation |
| $\sum_{\imath}\varepsilon_{\imath}D_{\imath}j_{a,\imath}=0$ | continuity, covariant, an identity of $\mathbb{F}$ |
| $ig_{4}f_{abc}A_{b,\imath}j_{c,\imath}$ | the ordinary divergence; the exchange, with no combination cancelling |
| $(\rho_{k}-\rho_{l})^{2}$ | the weight of the frame's rotation; zero on the degenerate pairs |
| $g_{4}^{2}(\rho_{k}-\rho_{l})^{2}$ | the six masses, the stratification stiffness |
| $V(\rho_{k})$ | the equation of state, four pressures, six free coefficients |
| $\theta_{4}$ | the coefficient of the helicity, $\operatorname{tr}(\mathbb{F}\wedge\mathbb{F})$ |

## Further Reading

- [The Lagrangian and the Primordial Force: The $\mathrm{SU}(4)$ Action, One Coupling on Fifteen Generators](the-lagrangian-and-the-primordial-force.html). The action this article reads, its variation, the fifteen Gauss laws, and the ceiling that makes both transcriptions.
- [The Yang–Mills Equation in Biquaternionic Form](the-yang-mills-equation-in-biquaternionic-form.html). The covariant conservation, the failure of ordinary conservation, and the Bianchi identity at the $\mathrm{SU}(2)$ rung, where the same three statements appear with three generators.
- [The Force Content of the $\mathrm{SU}(4)$ Model: One Connection, a Nine-Dimensional Kernel and Rank Five](the-force-content-of-the-su4-model-one-connection-a-nine-dimensional-kernel-and-rank-five.html). What the fifteen directions are, and which of them the condensate can see.
- [The Scalar Content: One Matrix and Ten Survivors](the-scalar-content-one-matrix-and-ten-survivors.html). The census that this article's $4+6=10$ reproduces from the chart.
- [The Breaking of the Primordial Force and the Mass of the Six Leptoquarks](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). The six heavy vectors' masses, which §*The Six Heavy Vectors Are Six Stratified Frame Directions* writes as $g_{4}^{2}(\rho_{k}-\rho_{l})^{2}$.
- [The Primordial Potential: One Symmetric Minimum above $M_{C}$](the-primordial-potential-one-symmetric-minimum-above-m-c.html). The six coefficients, and the minimum whose eigenvalue pattern the chart uses.
- [The $\mathrm{SU}(4)$ Instanton: A Matrix Transcription Outside the Algebra](the-su4-instanton-a-matrix-transcription-outside-the-algebra.html). The topological density whose coefficient is $\theta_{4}$, and the bundle on which §*Open Questions* expects the vorticity potential to fail to glue.
- [The Charged Spin-One Fluid from the Polar Action](charged-spin-one-fluid-equations-from-the-polar-action.html). The nearest earlier rung: the ordinary divergence failing to vanish, and the compressibility as the distance between two divergences.
- [The Two-Fluid Model in Biquaternionic Form](the-two-fluid-model-in-biquaternionic-form.html). The precedent for a multi-component fluid with relative velocities, which the twelve frame directions generalise.
- [The Relativistic Quantum Space as a Fluid](the-relativistic-quantum-space-as-a-fluid.html). The collection's founding statement of what a fluid reading of a field equation is for.
- Jean-Marie Souriau, *Structure of Dynamical Systems* (Birkhäuser, 1997), for a flow's vorticity as an antisymmetric two-form and the covariant statement of Helmholtz's theorems.
- Vladimir I. Arnold and Boris A. Khesin, *Topological Methods in Hydrodynamics* (Springer, 1998), for helicity as a linkage invariant and the Chern–Simons form of a flow.
- Darryl D. Holm and Boris A. Kupershmidt, "Poisson structures and Clebsch representations on groups," in *Fluids and Plasmas: Geometry and Dynamics* (AMS, 1984), for the Clebsch potential of a non-abelian flow and the multimomentum mapping that the fifteen components realise.
