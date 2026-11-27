# __The Charged Spin-One Fluid from the Polar Action: Compressibility, Covariant Vorticity and Three Currents__

## Introduction

[The Charged Spin-One Fluid: Three Currents and a Compressibility](the-charged-spin-one-fluid.html) lists five changes the coupling makes to the vector fluid and derives each from the coupled equation. [The Lagrangian and the Coupled Proca Equation in Polar Variables](the-lagrangian-and-the-coupled-proca-equation-in-polar-variables.html) writes the coupled action in the eight parameters of the complete word and finds a kinetic term of sigma-model type with a field-dependent metric.

This article varies that action and reads the five changes as five statements about one functional. **Every one of them is a statement about which terms of the action the connection reaches.** The connection reaches the derivative term and not the mass term. The derivative term is the field strength's square, so the vorticity is covariantized and the curl gains a term bilinear in the potential. The mass term is untouched, so the pressure and the equation of state survive. The constraint's divergence is taken with the covariant derivative and the ordinary divergence does not vanish, so the fluid is compressible. And the phase's shift is a symmetry while the rotor's is not, so there is one charge and not two.

**The claim that matters most, and it is a negative one.** The corpus says the question "whether the extra four parameters can be read as a second fluid" is not settled. This article settles it against. The four extra parameters are the phase and the rotor. The phase's shift is a symmetry of the action, so the phase carries a conserved current and is a fluid's charge. The rotor's shift is not a symmetry, because the rotor enters the mass term and the metric's cross terms, and a direction whose shift is not a symmetry carries no conserved current. A second fluid would need a second conserved density, and there is none.

**The strongest objection.** *The action route needs the element-form functional to be right, and the coupled Proca action contains a term bilinear in the potential that the free action did not, so the substitution is not a substitution but a new theory.* The objection is correct about the term and wrong about its status. The bilinear term is what covariance requires, and it is what makes the action invariant. Its presence means the chart's equations are nonlinear in the parameters, which the polar companion states, and it does not mean the fluid reading is a different reading: the term is part of the field strength, so it is part of the vorticity, and that is the article's first positive statement.

**Position in the block.** The coupled member of the pair whose free member is [Spin-One Fluid Equations from the Proca Polar Action](spin-one-fluid-equations-from-the-proca-polar-action.html). It sits at the top of the fluid ladder, above the spinor rung, and it is the only rung at which the carrier has to double.

## Conventions

**The conventions are the charged spin-one fluid article's and the coupled polar companion's.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_{\imath}^{2}=-e_t$; $i$ central; $^{*}$ Hermitian, $^{\natural}$ quaternionic; $\mathrm{Sc}$ the coefficient of $e_t$; the pairing $\mathrm{Sc}(\cdot^{*}\cdot)$. The word is the four-factor decomposition of the complex element,

$$
\tilde A=\varrho\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
\qquad
\varrho>0,
$$

with the free ranges for the angles. The eight real parameters are the eight real components of a complex four-vector.

The connection and the coupling. $\tilde A_\Phi$ is the external potential, $ϙ$ the coupling, and

$$
\tilde\nabla_{\mathrm{gco},\Phi}=\tilde\nabla_\Phi+\frac{2\pi i\,ϙ}{h}\tilde A_\Phi
$$

in the coupled polar companion's normalization; the field strength is built from the covariant gradients,

$$
\tilde F=\tfrac12\bigl((\tilde\nabla_\Phi)^{\natural}_{\mathrm{gco}}\tilde A-\tilde\nabla_{\mathrm{gco},\Phi}\tilde A\bigr)_{V},
$$

and it therefore carries the term $\frac{2\pi iϙ}{h}\mathrm{Vect}(\tilde A_\Phi^{\natural}\tilde A)$ bilinear in the potential.

The metric. The chart's kinetic term is $\tfrac12 G^{ab}(q)\partial q_a\partial q_b$ with $G$ field-dependent, of sigma-model type, and the eight parameters are its coordinates. $\nu_m=\frac{mc}{h}$, and the measure is $\mathrm{d}^{4}r$.

**One warning, from the fluid article.** The scale $\varrho$ is the fluid's amplitude and not its density. Every fluid formula is homogeneous in it: the velocity and the vorticity are independent of $\varrho$ and the stress is quadratic in it. The density the fluid carries is the charge bilinear, and the two are different objects.

## The Action in the Word

The functional. The coupled polar companion's action is the free Proca action with the ordinary gradient replaced by the covariant one in the derivative term and nowhere else,

$$
S[\tilde A]=\int\mathrm{d}^{4}r\;\Bigl[\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)-\tfrac12\,4\pi^{2}\nu_m^{2}\,\langle\tilde A\rangle_\natural\Bigr],
$$

and the replacement is the whole of the coupling.

**Why the mass term cannot be covariantized.** The mass term is algebraic and contains no derivative, so there is no gradient for the connection to enter. That single fact is the source of half the article's statements: the equation of state survives, the pressure survives, and the mass shell survives, because the term that carries them is the term the connection cannot reach.

**Why the field term changes in kind and not only in letters.** With ordinary gradients the field strength is $r\Omega+\mathrm{d}r\wedge u$, a sum of a term in the direction's derivative and a term in the density's gradient. With covariant gradients there is a third piece, bilinear in the potential and the field. So the field strength's square is no longer a quadratic form in the parameters' derivatives: it is a quartic functional. The chart's equations are therefore nonlinear, and the nonlinearity is the interaction.

**The metric, and what it is for.** The kinetic term is a sigma-model term: the parameters are coordinates on an eight-dimensional target and the metric is the chart's. Its role in the fluid reading is negative — it says the fluid's kinetic energy is not a sum of squares but a quadratic form — and its role in the constraint analysis is positive: its rank decides how many parameters are dynamical.

## The Variation: The Phase's Equation Is the Charge Conservation

Varying $\theta_{\mathrm{pha}}$. The phase appears in the derivative term through the covariant gradient and in the mass term's invariant. The invariant is $\langle\tilde A\rangle_\natural=\tilde A\tilde A^{\natural}$, and a central phase leaves it unchanged: the conjugate carries the opposite phase and the two commute. So the shift of the phase is a symmetry of the action, with the connection shifted to compensate, and Noether's theorem gives a conserved current.

$$
\partial_{\imath}J^{\imath}_{\mathrm{chg}}=0,
\qquad
J_{\mathrm{chg}}\ \text{the phase's conjugate current}.
$$

**Three statements.**

*The charge current is conserved for every $m$, including zero.* This is the fluid article's "the Noether current of the phase symmetry is conserved for every $m$", and the action route's reason is that the mass term is phase-invariant. The free fluid had no such current, because it had no phase; its charge was the sign of the branch.

*The phase's current is not the number current.* The number current's divergence is the Lorenz condition, and at this rung the Lorenz condition is covariant and the number current is not conserved. The two currents are different objects and the article's §*Compressibility* says how they differ.

*The phase is the chart's symmetry direction, and this is what makes it a fluid variable.* A fluid's charge is a conserved density; a conserved density is a shift symmetry's Noether charge; the phase's shift is the only shift in the chart that is a symmetry. That chain is the article's argument against a second fluid, and it is completed in §*The Rotor Is Not a Second Fluid*.

## The Variation: The Scalar Part Is the Constraint, and the Constraint Is Compressible

Varying the frame and the scale. The four equations of the free rung become eight, and the structure the article reads is the scalar part's: the divergence of the field equation, taken with the covariant derivative, is the constraint.

**The covariant Lorenz condition.** The scalar part of the field equation forces

$$
\mathrm{Sc}\bigl((\tilde\nabla_{\mathrm{gco},\Phi})^{\natural}\tilde A\bigr)=0,
$$

which is the covariant Lorenz condition, exact and blind to the frame. It is the constraint and it is one equation on eight parameters.

**The ordinary divergence does not vanish, and its value is the amplitude.** Using the constraint,

$$
\mathrm{Sc}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A\bigr)
=-\frac{2\pi i\,ϙ}{h}\langle\tilde A\rangle_\natural
=-\frac{2\pi i\,ϙ}{h}\,\varrho^{2}e^{2i\theta_{\mathrm{pha}}} .
$$

So the field's ordinary divergence is the field's own complex norm, and the fluid's expansion is its amplitude.

**What the two displays say together, and this is the article's sharpest fluid statement.** The free fluid was incompressible because the divergence of its velocity vanished identically, and that vanishing was the mass's gift: it came from taking the divergence of the field equation, and at $m=0$ there was nothing on the right and no condition. Here the constraint is still the mass's gift, and the divergence it controls is the covariant one. The ordinary divergence is not controlled, and its value is the amplitude. **So the compressibility is not a new term in the equations: it is the distance between two divergences, and that distance is what a connection does to a derivative.**

**The objection.** *A fluid whose expansion is its own amplitude has no equation of state and is not a fluid.* The expansion being the amplitude is the statement that the fluid's volume element is the field's normalization, which is exactly what a complex field allows and a real one does not. The equation of state is a separate statement about the pressure, and the pressure's source is the mass term, which the connection does not reach. The two statements are independent, and the article's next section is the second.

## The Variation: The Pressure Survives and the Vorticity Does Not

**The mass term is untouched, so the equation of state is the free one.** The stiff equation of state $\epsilon=p=\tfrac12m^{2}\varrho^{2}$ came from the mass term's being a pure power of the modulus. The connection cannot enter an algebraic term, so the equation of state is unchanged, the sound speed is still $c$, and the fluid is still barotropic in its amplitude.

**The field term is covariantized, so the vorticity is not the free one.** The field strength is now the covariant curl, and the covariant curl of a direction is not the ordinary one:

$$
F^{\mathrm{gco}}=r\Omega+\mathrm{d}r\wedge u+\frac{2\pi i\,ϙ}{h}\mathrm{Vect}\bigl(\tilde A_\Phi^{\natural}\tilde A\bigr).
$$

The third term is bilinear in the potential and the field, and it is what makes the flow rotational where the free flow could not be.

**What this changes in the fluid's Euler equation.** The acceleration is the contraction of the covariant curl with the flow, so the force is no longer a density gradient alone: the bilinear term contributes a force that depends on the potential. The fluid article's "the coupling changes the vector fluid more than it changes either of the other two" is this: at the scalar and spinor rungs the connection joined a bracket that carried a phase, and here it joins the field strength itself.

**Why the equation of state's survival and the vorticity's change are compatible.** They are statements about different terms. The pressure is the mass term's; the vorticity is the derivative term's; the connection reaches the second and not the first. A reader who thinks a charged fluid must have a changed equation of state is reading the coupling as a shift of every term, and the action says which terms it reaches.

## The Rotor Is Not a Second Fluid

**The corpus's open question, stated.** The free Proca word has four parameters and no room for an orientation. The coupled word has eight, and the four extra are the phase and the rotor. Whether the extra four can be read as a second fluid is not settled in the corpus.

**The article's answer, and its warrant.** A fluid is a conserved density and a flow. A conserved density is a shift symmetry's Noether charge. The phase's shift is a symmetry of the action: the mass term's invariant is blind to it and the derivative term is covariant by construction. The rotor's shift is not: the rotor enters the mass term's invariant, and it enters the metric's cross terms, so a shift of it changes the action.

**Therefore the extra four parameters carry one conserved density and not two.** The phase's is the charge current, conserved for every mass. The rotor's has no current, because it has no symmetry. A direction with no conserved density is not a fluid, and the rotor is such a direction. It is a parameter of the chart that the free word had no room for, and its physical reading is open — the article does not claim it is a spin, because at this rung the spin is not in the chart at all.

**What the rotor does do.** It enters the mass term and the metric, so it changes the energy and the inertia and not the transport. That is the signature of a shape parameter rather than a fluid's degree of freedom, and it is the sharpest available answer to the corpus's question.

## The Three Currents, and Which One Is Conserved

**The response.** $m^{2}\tilde A$: the field's own value, which the equation sets equal to the divergence of the field strength. It is a current in the sense of being a four-vector and not in the sense of being conserved.

**The direction.** $\tilde A/\varrho$: the unit flow, which the fluid article identifies with the velocity. It carries no charge and its divergence is the expansion.

**The charge bilinear.** The phase symmetry's Noether current, conserved for every $m$ and vanishing on the real slice. It is the only one of the three that is conserved.

**The reading.** Three currents and one conservation law is the rung's count, and it is what makes the charged vector fluid different in kind from the free one. The free fluid had one current, the field itself, and one conservation law, the Lorenz condition. The charged fluid has three currents and one conservation law, and the two extra currents are the price of a complex carrier.

## What the Alternative Route Adds and What It Relabels

**Adds.** The location of each of the five changes in one term of the action: the compressibility in the covariant derivative's divergence, the vorticity in the covariant curl, the pressure's survival in the mass term's algebraicity, the charge in the phase's symmetry, and the rotor's status in the absence of one. The negative answer to the second-fluid question, with a warrant. And the statement that the compressibility is the distance between two divergences.

**Does not add.** No new equation and no new solution. The five changes are the fluid article's and its own computation is their warrant. The sigma-model metric is stated and not diagonalized, and the spacelike branch is not followed.

**Relabels.** "The Lorenz condition stops being the continuity equation." On the equation route this is a comparison of two formulas. On the action route it is the statement that there are two divergences, the covariant one and the ordinary one, and that the constraint controls the first while the second is the amplitude. A fluid's continuity is the ordinary divergence, so the fluid's continuity is what changes.

## Open Questions

**The rotor's physical reading.** Whether the rotor is a shape parameter, a hidden orientation, or the vestige of a spin the chart cannot carry, is open. The article rules out one reading — a second fluid's degree of freedom — and does not supply another.

**The massless limit's residue.** At $m=0$ the constraint disappears and the charge current survives. Whether the residue is a fluid, and in which sense, is the fluid article's question and is not settled by the action.

## Summary

The coupled Proca polar action varies into eight equations, and the fluid's content is a statement about which terms the connection reaches. It reaches the derivative term, so the vorticity is covariant and gains a bilinear piece and the flow is rotational; it cannot reach the mass term, so the stiff equation of state and the pressure survive. The constraint is the covariant Lorenz condition, and the ordinary divergence is the amplitude, so the fluid is compressible and the compressibility is the distance between two divergences. The phase's shift is a symmetry and the rotor's is not, so the extra four parameters carry one conserved density and not two: the rotor is a shape parameter and not a second fluid. Three currents, one conservation law, and one rung at which the carrier doubles.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\tilde A=\varrho e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | the word of the complex element |
| $\varrho$ | the fluid's amplitude, not its density |
| $\tilde\nabla_{\mathrm{gco},\Phi}$ | $\tilde\nabla_\Phi+\frac{2\pi iϙ}{h}\tilde A_\Phi$ |
| $\tilde F$ | covariant curl; carries $\frac{2\pi iϙ}{h}\mathrm{Vect}(\tilde A_\Phi^{\natural}\tilde A)$ |
| $G^{ab}(q)$ | sigma-model metric of the eight-parameter chart |
| $\mathrm{Sc}((\tilde\nabla_{\mathrm{gco},\Phi})^{\natural}\tilde A)=0$ | covariant Lorenz condition, the constraint |
| $-\frac{2\pi iϙ}{h}\varrho^{2}e^{2i\theta_{\mathrm{pha}}}$ | the ordinary divergence, the expansion |
| $\epsilon=p=\tfrac12m^{2}\varrho^{2}$ | stiff equation of state, unchanged by the coupling |
| $m^{2}\tilde A$, $\tilde A/\varrho$, $J_{\mathrm{chg}}$ | the three currents; only the third is conserved |

## Further Reading

- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, for the fluid reading of relativistic fields.
- Anders H. Taub, "General relativistic variational principle for perfect fluids," *Physical Review* **94** (1954) 1468–1470, for the variational derivation of a barotropic fluid and its constraint.
- Bernard F. Schutz, "Perfect fluids in general relativity: velocity potentials and a variational principle," *Physical Review D* **2** (1970) 2762–2773, for velocity potentials and the conservation of the conjugate current.
- Jean-Marie Souriau, *Structure of Dynamical Systems* (Birkhäuser, 1997), for a direction's covariant derivative and the split into acceleration and vorticity.
