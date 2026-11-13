# The Lagrangian of the Spin Fluid

## Introduction

**The spinor case is the one in which the action's canonical structure has a closed form, and the closed form says something the equations do not.** In [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html) the fluid is a triple at each event — a density, a frame and a spin direction — and the system does not close. Here the same field is written as an action in those variables, and the action's canonical structure is computed rather than asserted: which of the triple's data are canonical and which are not, with what weights.

**Three results.**

*First, the kinetic term is one closed form, and in the fluid's variables it reads as a charge density times a bracket of two rates.*

$$
\mathcal L_{\mathrm{kin}}=\hbar c\,\rho_{\mathrm{chg}}\Bigl(\dot\theta_{\mathrm{pha}}-\beta\,\vec n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r}\Bigr),
$$

with $\beta=\lvert\vec v\rvert/c$, $\vec\omega_{\mathrm r}$ the rotor's body angular velocity and $\vec n_{\mathrm{rot}}$ the boost axis carried into the body frame. **The spin's weight in the kinetic term is $\beta$**, so a fluid at rest has no spin term at all, and the spin is canonically visible only when the flow moves.

*Second, the canonical table follows, and it is the article's centrepiece.* The phase's momentum is $\hbar c\rho_{\mathrm{chg}}$; the spin's is $-\hbar c\rho_{\mathrm{chg}}\beta\vec n_{\mathrm{rot}}$; the density's and the velocity's are zero identically. **The density and the velocity are never canonical, the phase is always canonical, and the spin is canonical only away from rest.** That is the particle setting's answer to the block's question of which of the triple's data carry dynamics.

*Third, the mass term is the one term the fluid's data do not determine.* The polar companion finds that the mass bilinear vanishes on the frame's parts and returns only when it carries a declared unit direction. The fluid chart inherits the declaration and cannot remove it: **the mass is not a function of the density, the frame and the spin, but of those and one direction.** The article states the consequence precisely, because it is the one place where this layer's articles have a term the fluid variables do not supply.

**Position in the block.** This is the variational companion of [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html) and the fifth of the eight articles of this layer. It is the first in which the canonical structure is not trivial, and the first in which the particle setting is a real restriction: the block's vorticity is a spatial gradient of the frame and the closed form below has no spatial gradient anywhere.

**Conventions.** $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ with $\tilde U_{\Psi,\mathrm b}=\exp(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b})$ and $\tilde u_{\mathrm r}=\exp(\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r})$, $\rho_{\mathrm{num}}=r^{2}$, $\gamma=\cosh\theta_{\mathrm{rpd}}$, $\beta=\tanh\theta_{\mathrm{rpd}}$, $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$, $\vec s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$, and $\vec\omega_{\mathrm r}=\tilde u_{\mathrm r}^{-1}\dot{\tilde u}_{\mathrm r}$ with $\vec n_{\mathrm{rot}}=\tilde u_{\mathrm r}^{-1}\vec u_{\mathrm b}\tilde u_{\mathrm r}$. The action is the element action of [The Variational Principle and the Dirac Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-dirac-equation-in-biquaternionic-polar-variables.html), and the spatial derivatives are set to zero: the field is homogeneous, which is the setting in which the polar flow is the parent's flow.

## The Kinetic Term

**The computation is the polar companion's and its result is one line.** Substituting the word into $\frac{\hbar c}{2}\mathrm{Re}\,\mathrm{Sc}[\tilde\Xi_L^{*}\tilde\nabla_\Phi^{\natural}\tilde\Xi_L+\tilde\Xi_R^{*}\tilde\nabla_\Phi\tilde\Xi_R]$ and keeping the temporal slots gives

$$
\mathcal L_{\mathrm{kin}}=\hbar c\,r^{2}\bigl(\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}-\sinh\theta_{\mathrm{rpd}}\,\vec n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r}\bigr),
$$

and the two factors are the fluid's: $r^{2}\cosh\theta_{\mathrm{rpd}}=\rho_{\mathrm{chg}}$ and $\sinh\theta_{\mathrm{rpd}}/\cosh\theta_{\mathrm{rpd}}=\beta$. Factoring $r^{2}\cosh\theta_{\mathrm{rpd}}$ out of the bracket,

$$
\mathcal L_{\mathrm{kin}}=\hbar c\,\rho_{\mathrm{chg}}\bigl(\dot\theta_{\mathrm{pha}}-\beta\,\vec n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r}\bigr).
$$

**The reading of the bracket is the article's first statement.** The kinetic term is a charge density times a difference of two rates: the phase's rate, which every fluid of this block carries, and the spin's rate, which is the rotor's angular velocity resolved along the boost axis as seen from the body. **The second rate is weighted by $\beta$, so it is the flow's speed that makes the spin visible**, and the weight is not a small parameter but the ratio of the momentum's spatial part to its energy.

**At rest the bracket collapses to the phase's rate and the spin leaves the kinetic term.** That is not an approximation and it is not a choice of gauge: $\sinh\theta_{\mathrm{rpd}}=0$ at $\theta_{\mathrm{rpd}}=0$, so the second term vanishes identically for every rotor angle and every rotor rate. **A spinor fluid at rest has the canonical structure of a scalar fluid**, and the spin's dynamics is a property of a moving frame. The polar companion states this and the fluid chart states it as a weight in a bracket.

**The sign of the second term is the frame's and it is worth recording.** It is negative, so the spin's contribution to the kinetic term opposes the phase's. The polar companion notes that the two kinetic terms of the Schrödinger and Dirac companions have the same shape and opposite signs, and the fluid reading says where the sign sits: in the cross term between the flow's direction and the rotor's rate, not in the phase's term.

## The Canonical Table

**Four statements, and each is an identity rather than a sample.** Differentiating the closed form,

| momentum | value | fluid reading |
| --- | --- | --- |
| $p_{\theta_{\mathrm{pha}}}$ | $\hbar c\,r^{2}\cosh\theta_{\mathrm{rpd}}=\hbar c\,\rho_{\mathrm{chg}}$ | the charge density; the phase is canonical in every frame |
| $\vec p_{\mathrm{spin}}$ | $-\hbar c\,r^{2}\sinh\theta_{\mathrm{rpd}}\,\vec n_{\mathrm{rot}}=-\hbar c\,\rho_{\mathrm{chg}}\beta\,\vec n_{\mathrm{rot}}$ | the charge density times $\beta$, along the boost axis in the body frame |
| $p_{\theta_{\mathrm{rpd}}}$ | $0$ | the rapidity is not canonical |
| $p_{u_{\mathrm b}}$ | $0$ | the velocity's direction is not canonical |
| $p_{r}$ | $0$ | the density is not canonical |

**The middle row is the one the block's articles could not state.** $\vec p_{\mathrm{spin}}$ is a closed form and not a projector: it is a vector, its magnitude is $\hbar c\rho_{\mathrm{chg}}\beta$, and its direction is $\vec n_{\mathrm{rot}}$. **The canonical spin is therefore locked to the flow's direction, and the lock is through the frame's rotor**: $\vec n_{\mathrm{rot}}$ is the boost axis carried into the body frame, so it is the velocity's direction as the spin's own frame sees it.

**The lock the block states is a lock of magnitudes, and it does not identify the two directions.** [Spin-Velocity Locking on the Degenerate Sector](spin-velocity-locking-on-the-degenerate-sector.html) constrains the rapidity against the spin angle, $\cosh(\theta_{\mathrm{rpd}}/2)\cos(\theta_{\mathrm{axr}}/2)=\varepsilon$, and constrains the two axes to be orthogonal; nothing in it makes $\vec n_{\mathrm{rot}}$ and $\vec s$ one vector. They are different objects for a structural reason: $\vec n_{\mathrm{rot}}=\tilde u_{\mathrm r}^{-1}\vec u_{\mathrm b}\tilde u_{\mathrm r}$ is the boost axis carried into the body frame, and $\vec s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$ is the declared axis carried out of it, so the rotor acts on the two in inverse senses. **The canonical spin is the flow's direction as the body frame sees it and the spin direction is the body frame's own axis**, and they coincide only where the rotor is trivial and the boost is along $\vec e_z$, which is the end of the sector where both momenta vanish. Off that point the difference between them is the quantity [The Non-Uniqueness of the Spin Fluid](the-non-uniqueness-of-the-spin-fluid.html) isolates.

**The four zeros are the scalar rung's statement, extended.** There the density and the velocity are not canonical and nothing else is; here the phase and the spin are canonical and the other two are not. **The count is the triple's**: three data, of which the density and the frame never carry momentum and the phase and the spin do. That is why the block's fluid can be described by a density and a direction and why the dynamics sits in the two angles.

**The qualification is part of the table and not a footnote.** At $\theta_{\mathrm{rpd}}=0$ the spin's momentum vanishes with the density's and the velocity's, and the table has one non-zero row. The polar companion records that an earlier version of its own statement claimed the phase and the spin unconditionally, and that the claim was wrong at rest. The fluid chart's version of the correction is the weight $\beta$: **the spin's canonical weight is the flow's speed, so the rest frame is the degenerate case of the table and not an exception to it.**

## The Constraints and Where the Non-Closure Lives

**The four vanishing momenta are four primary constraints, and they are second class.** That is the polar companion's computation, and the fluid chart states its content: $\phi_1=p_r$, $\phi_2=p_{\theta_{\mathrm{rpd}}}$, $\phi_{3,4}=p_{u_{\mathrm{b}}}$ vanish on every configuration, and their brackets with the configuration variables are not zero, so they are second class and the system is reduced by a Dirac bracket rather than by a gauge.

**The block's non-closure is a property of that bracket and not of the equations.** [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html) finds that the fluid's four brackets do not close: the algebra of the flow's derivatives produces terms the fluid's data cannot express, and the obstruction is structural. In the variational formulation the same fact has a location: **the reduced phase space is the Dirac bracket's, and the fluid's variables close if and only if that bracket's algebra closes on them.** A non-closure of the equations and a non-closure of the bracket are the same obstruction read in two languages, and the bracket is the language in which it can be attacked, because a bracket is an object one computes rather than an equation one solves.

**What the article does not claim is that the bracket closes.** The polar companion lists the closure as an open question and states it as finite and explicit: the one-form is known, the constraints are known, and what remains is the bracket. The fluid chart narrows the question rather than answering it: **the question is whether the Dirac bracket of the spin fluid's three data is a Lie algebra**, and the block's non-closure says the answer is not obviously yes.

**The counting is worth recording because it is where the two rungs differ.** At the first-order rung there are no constraints and the Dirac bracket is the Poisson bracket. At the scalar relativistic rung there are none either. Here there are four, and they are the price of writing the velocity as a coordinate: **a fluid always has more coordinates than canonical ones, and the difference is the constraints.**

## The Mass Term and the Declared Direction

**The mass is the one term the fluid's data do not determine, and the article states it without softening it.** The polar companion finds that the element-form mass bilinear vanishes on the frame's parts: the two chiral parts sit in complementary right ideals, $\Pi_+\Pi_-=0$, and $\mathrm{Sc}$ is cyclic, so the pairing is zero identically. The mass returns only when the bilinear carries a fixed unit direction inside it, $\tilde\Xi_R\mapsto\tilde\Xi_R i\vec v$ with $\vec v\perp\vec e_z$.

**The consequence for the action is exact and it is a limitation.** The spin fluid's action is not a functional of the density, the frame and the spin alone: it is a functional of those and of one declared direction, and the direction is not one of the triple's data. A reader who expects the Lagrangian of a fluid to be written in the fluid's variables will find that this one is written in the fluid's variables plus a constant of the formulation.

**The comparison with Takabayasi is the reason the point matters.** His mass term is written in his variables and needs no declaration, because his seventh quantity is an internal angle and the mass is a function of it. [The Dirac Fluid and the Takabayasi Correspondence](the-dirac-fluid-and-the-takabayasi-correspondence.html) identifies that angle with the rotor's, by a count argument that it states as forced but not as a theorem, and it records that the corpus's mass coupling depends on the boost and not on the rotor angle. **So the two formulations agree on the mass only after a decision about what the angle is**, and the decision is exactly the declared direction: the corpus's action fixes a direction where Takabayasi's carries an angle.

**What follows is a statement of scope and not a resolution.** The action below is the corpus's, with the declaration, and every canonical statement in this article is independent of it — the kinetic term and the table do not contain the mass term at all. **A reader who wants the mass without a declared direction must change the naming of the parts, and that is a different article.** The corpus's [Klein–Gordon from the Dirac Square](klein-gordon-from-the-dirac-square-in-biquaternionic-form.html) supplies the second-order equation in which the pairing does not arise, and it is the natural place to look for the resolution.

## The Two Currents, and What the Particle Setting Cannot See

**The action's invariances give the block's two currents, and the identification is exact for one and conditional for the other.** Translation invariance gives the stress; the phase's shift gives the current; the frame's rotation gives the spin current. In the particle setting the first two are the block's $\tilde J_\Phi$ and $T_{\mu\nu}$ restricted to a homogeneous field, and the third is $\tilde S_{\Psi,\mathrm{sp}}=\rho_{\mathrm{num}}\frac{\hbar}{2}i\vec s$ with the transport law that the rotor's equation supplies.

**What the particle setting cannot see is the vorticity, and the reason is structural.** The block's central result is that the Dirac fluid's vorticity is the antisymmetrised gradient of the frame: a spatial derivative. The closed form above has no spatial derivative anywhere — the only derivative is the rotor's rate $\vec\omega_{\mathrm r}$, which is a body-frame angular velocity and not a gradient. **A homogeneous action cannot produce a gradient-sourced vorticity**, and no manipulation of the closed form will: the two objects are derivatives with respect to different arguments.

**The operator setting's action must therefore contain the frame's spatial gradients, and its structure is determined by what the block already knows.** [The Variational Principle and the Coupled Dirac Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-coupled-dirac-equation-in-biquaternionic-polar-variables.html) writes the operator action with the gradient terms collected as "terms in $\nabla r$, $\nabla\theta_{\mathrm{rpd}}$, $\nabla\theta_{\mathrm{axr}}$" and does not compute them. What the block's vorticity statement fixes is their content: the antisymmetrised gradient of the frame is the spin connection's field strength, so the gradient terms are the spin connection's kinetic term, and the vorticity is its curl. **The block's sentence "the vorticity is sourced by the frame's gradients" and the statement "the gradient terms are the spin connection's" are the same statement**, and the second is the one a variational formulation can use.

**The honest boundary.** This article does not compute those terms. It states the closed form of the particle setting, the canonical table that follows from it, the location of the non-closure, and the structure the operator setting must have. **A reader looking for the full field-theoretic Lagrangian of the spin fluid will find the particle setting's exact result and the operator setting's programme, and the two are not the same article.**

## What the Fluid Variational Principle Adds and Does Not Add

**Adds.** The kinetic term as one bracket with the spin's weight $\beta$ visible in it, which is the sharpest statement of why a rest frame has no spin dynamics. The canonical table as an identity: which of the triple's data carry momentum, with what weights and along which directions. The canonical spin's direction named as the boost axis in the body frame, and the block's degeneracy stated as a lock of magnitudes that does not make the two directions one vector. The location of the non-closure in the Dirac bracket, which turns the block's structural obstruction into a computable object. And the mass term's declared direction stated as the one place the fluid's data are insufficient.

**Does not add.** No new equation: the rotor's and the frame's equations are the parent's, and the polar companion's Euler–Lagrange equations are the equation's components in the parameter basis. No closure. No vorticity, for the structural reason above. No thermodynamics: the spin fluid's thermal state is a different category's object, and the spin potential there is not the momentum here.

**The one comparison that matters for the layer.** The scalar relativistic article of this layer finds the shell to be an equation of motion and the stress to be a translation current. Here the analogous statements are weaker: the constraints are constraints and not equations, because the frame's variables are coordinates with no kinetic term, and the stress is a restriction of the block's. **The difference is the count of the word's factors**: two for the scalar, four for the spinor, and the two extra factors carry no kinetic term at all.

## Open Questions

1. **The bracket.** Whether the Dirac bracket of $(\rho_{\mathrm{num}},\vec s,\vec v)$ closes is the polar companion's open question and this article's. It is finite: the constraints are known and the one-form is known.

2. **The mass without a declaration.** Whether a naming of the chiral parts exists in which the mass bilinear does not need a fixed direction is not settled. The second-order route avoids the pairing and is the place to look.

3. **The operator setting's gradient terms.** Their closed form is not in this article and not in the corpus. The block's vorticity statement fixes their content and not their coefficients.

4. **The rest frame.** At $\theta_{\mathrm{rpd}}=0$ the spin's momentum vanishes and the rotor's equations become constraints. Whether the rest-frame flow survives the reduction, or whether the rest frame is a singular point of the action, is open.

## Summary

**The action.** $\mathcal L_{\mathrm{kin}}=\hbar c\,\rho_{\mathrm{chg}}(\dot\theta_{\mathrm{pha}}-\beta\,\vec n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r})$ in the particle setting, with the mass term requiring a declared direction.

**The canonical table.** $p_{\theta_{\mathrm{pha}}}=\hbar c\rho_{\mathrm{chg}}$ in every frame; $\vec p_{\mathrm{spin}}=-\hbar c\rho_{\mathrm{chg}}\beta\vec n_{\mathrm{rot}}$, along the boost axis in the body frame and vanishing at rest; $p_r=p_{\theta_{\mathrm{rpd}}}=p_{u_{\mathrm b}}=0$ identically.

**The constraints.** Four primary, second class; the system is reduced by a Dirac bracket, and the block's non-closure is that bracket's failure to close on the fluid's data.

**The mass.** Not a function of the triple; it requires one declared direction, which is where this action differs from Takabayasi's.

**The limit.** The particle setting cannot see the vorticity, because the vorticity is a spatial gradient of the frame and the closed form has no spatial gradient.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The word, four factors |
| $\rho_{\mathrm{num}}=r^{2}$ | Proper density; not canonical |
| $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$ | Charge density; the phase's canonical weight |
| $\gamma=\cosh\theta_{\mathrm{rpd}}$, $\beta=\tanh\theta_{\mathrm{rpd}}$ | Lorentz factor and speed, $\beta=\lvert\vec v\rvert/c$ |
| $\vec s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$ | Spin direction; a unit vector |
| $\vec\omega_{\mathrm r}=\tilde u_{\mathrm r}^{-1}\dot{\tilde u}_{\mathrm r}$ | Rotor's body angular velocity |
| $\vec n_{\mathrm{rot}}=\tilde u_{\mathrm r}^{-1}\vec u_{\mathrm b}\tilde u_{\mathrm r}$ | Boost axis carried into the body frame |
| $p_{\theta_{\mathrm{pha}}}$, $\vec p_{\mathrm{spin}}$ | The two non-zero momenta |
| $p_r$, $p_{\theta_{\mathrm{rpd}}}$, $p_{u_{\mathrm b}}$ | The four vanishing momenta; second-class constraints |
| $\Pi_\pm$ | The chiral projectors; $\Pi_+\Pi_-=0$, the reason the mass needs a direction |
| $i\vec v$, $\vec v\perp\vec e_z$ | The declared direction of the mass bilinear |
| $\mathcal L_{\mathrm{kin}}$ | The kinetic Lagrangian density in the fluid variables |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part |

## Further Reading

- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 2–35, for the tensor formulation and its own Lagrangian, which carries multipliers and no declared direction.
- Takehiko Takabayasi, "The vector representation of spinning particles in quantum mechanics," *Progress of Theoretical Physics* **14** (1955) 283–302, for the canonical structure of the velocity and the spin before the Lagrangian is written.
- Fritz Bopp and Rudolf Haag, "Über die Möglichkeit von Spinmodellen," *Zeitschrift für Naturforschung* **5a** (1950) 644–653, for the classical spinning fluid and its constraints.
- Peter A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for the second-class reduction that the four vanishing momenta require.
- David Hestenes, "The Zitterbewegung interpretation of quantum mechanics," *Foundations of Physics* **20** (1990) 1213–1232, for the spinor's velocity and spin as frame quantities and for the weights they carry in a moving frame.
- The companion articles: [The Variational Principle and the Dirac Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-dirac-equation-in-biquaternionic-polar-variables.html), where the closed form and the four vanishing momenta are computed and the declared direction is found; [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html), the equations and the non-closure; [The Dirac Fluid and the Takabayasi Correspondence](the-dirac-fluid-and-the-takabayasi-correspondence.html), for the seven quantities and the angle; [Spin-Velocity Locking on the Degenerate Sector](spin-velocity-locking-on-the-degenerate-sector.html), for the sector on which the rapidity is locked to the spin angle and the two axes are orthogonal; and the charged companion [The Lagrangian of the Charged Spin Fluid](the-lagrangian-of-the-charged-spin-fluid.html), where a connection enters the bracket and leaves $\beta$ alone.
