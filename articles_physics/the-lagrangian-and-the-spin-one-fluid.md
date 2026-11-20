# __The Lagrangian and the Spin-One Fluid__

## Introduction

**At this rung the fluid's variables are the field's own, and the action's mass term does double work.** The Proca field is $A_\mu=r\,u_\mu$: a magnitude and a direction, which are a density and a velocity. So the fluid is not a reading of a polar decomposition imposed from outside — it is the field's own parameterisation, and the action written in it is the Proca action and nothing else.

**Three results.**

*First, one term of the action does two things, and they are the same thing.* The mass term $\frac{k_m^{2}}{2}r^{2}$ removes the gauge freedom and supplies the Lorenz condition; the Lorenz condition in the fluid's variables is $\sum_\mu\partial_\mu(ru_\mu)=0$, which is continuity. **The spin-one fluid's continuity is the replacement for its lost gauge freedom**, and both come from one term.

*Second, the density's variation and the direction's variation are the longitudinal and transverse parts of the field equation, and the Lorenz condition is neither: it is their consequence*, by the identity $\sum_{\mu,\nu}\partial_\mu\partial_\nu F_{\nu\mu}=0$. The action therefore explains the block's phrase that the free incompressibility is the mass's gift: without the mass the identity has nothing to balance, and the condition does not arise.

*Third, this is the only action in the layer with no $\hbar$ in its derivative term, and correspondingly the only fluid in the block whose acceleration law has no quantum force.* The polar decomposition of a vector field produces no second derivative of the magnitude, and the action says why: $A=ru$ has one derivative and the Lagrangian is quadratic in it.

**Position in the block.** This is the variational companion of [The Spin-One Fluid](the-spin-one-fluid.html) and the seventh of the eight articles of this layer. It is the only one in which a Lagrange multiplier is genuinely needed, and the only one whose fluid is not a quantum fluid.

## Conventions

**The conventions are restated here so that every sign below is checkable from this page alone.** $A_\mu=r\,u_\mu$ with $r>0$ and $\sum_\mu\varepsilon_\mu u_\mu u_\mu=-1$; the temporal slot carries the $i$, so $\sum_\mu\varepsilon_\mu A_\mu A_\mu=-r^{2}$. **No index is raised**: a contraction names its summed index, weighted by $\varepsilon_\mu$ wherever a value is displayed. $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$; $k_m=mc/\hbar$; $\mathcal L=-\frac14\sum_{\mu,\nu}F_{\mu\nu}F_{\mu\nu}-\frac{k_m^{2}}{2}\sum_\mu\varepsilon_\mu A_\mu A_\mu$ in the corpus's signs, whose Euler–Lagrange equation is $\sum_\nu\partial_\nu F_{\nu\mu}=k_m^{2}A_\mu$. The transverse derivative is $\nabla_\mu=\sum_\nu\mathsf{P}_{\mu\nu}\partial_\nu$ with $\mathsf{P}_{\mu\nu}=g_{\mu\nu}+u_\mu u_\nu$.

## The Action in the Field's Own Variables

**One substitution, and the field strength splits into a magnitude's part and a direction's part.** Since $A=ru$,

$$
F_{\mu\nu}=r\,\omega_{\mu\nu}+\bigl(\partial_\mu r\bigr)u_\nu-\bigl(\partial_\nu r\bigr)u_\mu,
\qquad
\omega_{\mu\nu}=\partial_\mu u_\nu-\partial_\nu u_\mu .
$$

**Three pieces, and each has a name in the fluid's language.** The first is the direction's vorticity times the density; the second and third are the density's gradient wedged with the velocity. The field strength therefore carries two independent objects: **the flow's vorticity and the density's gradient**, and the spin-one fluid is the only one in this layer whose field strength is made of the fluid's own derivatives rather than of a potential's.

**The Lagrangian, with the mass term expanded.**

$$
\mathcal L=\frac{1}{2}\Bigl[\sum_\mu\bigl(\partial_\mu r\bigr)^{2}-\bigl(\sum_\mu\varepsilon_\mu u_\mu\partial_\mu r\bigr)^{2}\Bigr]-\frac{r^{2}}{4}\sum_{\mu,\nu}\omega_{\mu\nu}\omega_{\mu\nu}-\sum_{\mu,\nu}\varepsilon_\mu\,r\,\omega_{\mu\nu}\bigl(\partial_\mu r\bigr)u_\nu+\frac{k_m^{2}}{2}r^{2},
$$

obtained by expanding $-\frac14F^{2}$ and using $u^{2}=-1$. Four terms: the density's gradient energy, the vorticity's energy, a cross term, and the mass.

**The cross term is what makes the free spin-one fluid's acceleration law as short as the block's.** $a_\mu=-\nabla_\mu\ln r-r^{-1}E_\mu$ has no quantum force because the two pieces of $F$ are first derivatives and no second derivative of $r$ survives the variation; the cross term is where the density's gradient and the vorticity meet, and it is the term that turns the field equation into a statement about the flow's acceleration.

**There is no $\hbar$ anywhere in the derivative terms.** The only place the quantum of action appears is inside $k_m$. So this rung's fluid is not a Madelung fluid: it is a classical field read as a medium, and the block's article says as much by giving an acceleration law with no quantum potential.

## The Variation: The Two Variations and the Multiplier

**The density's variation is the field equation contracted with the flow, and the direction's variation is its transverse part.** That is the cleanest way to state the pair, and it follows from the split of $\delta A_\mu=u_\mu\,\delta r+r\,\delta u_\mu$ into a longitudinal and a transverse piece.

The $r$ variation gives $\sum_\mu\varepsilon_\mu u_\mu(\sum_\nu\partial_\nu F_{\nu\mu}-k_m^{2}A_\mu)=0$, since $\partial F/\partial r$ along $u$ is the contraction; the $\delta u$ variation, restricted to $u\cdot\delta u=0$, gives the transverse part, $\sum_\nu\mathsf{P}_{\mu\nu}(\sum_\lambda\partial_\lambda F_{\lambda\nu}-k_m^{2}A_\nu)=0$. **The two together are the field equation and neither alone is.**

**The unit condition is the one place in this layer where a multiplier is genuinely needed.** The word's parameterisation absorbs the unit conditions of the boost and the rotor — a unit element is invertible for every value of its parameters — but the Proca direction is invertible by declaration and not by parameterisation: $u_\mu$ is three functions subject to one constraint, and the constraint must be imposed. Written with a multiplier,

$$
\mathcal L_{\lambda}=\mathcal L+\lambda\bigl(\sum_\mu\varepsilon_\mu u_\mu u_\mu+1\bigr),
$$

and the multiplier enters the direction's equation as $\lambda u_\mu$, which is a force along the flow. **It plays the part a pressure plays in an incompressible fluid**, and the analogy is exact in one respect: it is the constraint's force and not the fluid's own.

**The contrast with the spin article is worth recording.** There the parameterisation removed the need for a multiplier and the constraints appeared as vanishing momenta; here the parameterisation cannot remove it and the constraints appear as a projection. **The difference is that a unit rotor has three parameters and a unit vector has two plus one constraint**: the word's frame is a group element, and a direction is a coset.

## The Constraints the Action Imposes: The Unit Condition Is the One Constraint

**The word's parameterisation postpones the unit condition rather than removing it.** With $A=ru$ the field is split into a magnitude and a direction, and the direction is described by parameters while the condition $u\cdot u=1$ remains a relation among them that the action does not supply. A multiplier is therefore needed, and this is the one place in the layer where it genuinely is.

**The constraint is first class and it is the only one.** The multiplier's equation enforces the condition, the condition is preserved by the flow because the density is invariant under the reparameterisation of the direction, and no second condition follows. The count of degrees is the naive count minus the constraint's, which is why three polarisations survive where a count of the components would give four.

**The mass term adds no constraint.** It is a function of the magnitude and the frame and carries no derivative of an independent variable, so it changes the equations and leaves the count alone. **That is what the structural consequence means when it says the mass term does two things**: it fixes the direction's weight in the action and it does not restrict the data.

**The contrast with the spin article is why the section exists.** There the parameterisation removes the need for a multiplier and the constraint is carried by the chart itself. Here it does not, and the difference is a fact about which chart is used rather than about the field.

## The Structural Consequence: The Mass Term Does Two Things

**The Euler–Lagrange equation is the field equation, and its divergence is an identity on one side.**

$$
\sum_\nu\partial_\nu F_{\nu\mu}=k_m^{2}A_\mu
\qquad\Longrightarrow\qquad
0=\sum_{\mu,\nu}\partial_\mu\partial_\nu F_{\nu\mu}=k_m^{2}\sum_\mu\partial_\mu A_\mu,
$$

because $F$ is antisymmetric. **The Lorenz condition is therefore a consequence of the equation and not a condition imposed on it, and it exists exactly when $k_m\ne0$.**

**The same term removes the gauge freedom.** With $k_m=0$ the action is invariant under $A_\mu\mapsto A_\mu+\partial_\mu\Gamma$; with $k_m\ne0$ it is not, because the mass term is not. **One term supplies the condition and destroys the freedom the condition replaces**, and the two statements are the same statement seen from two sides: a massless vector has a redundancy and no condition, a massive one has a condition and no redundancy, and the count of physical components is the same in both cases.

**In the fluid's variables the condition is continuity.** With $A_\mu=r\,u_\mu$,

$$
\sum_\mu\varepsilon_\mu\partial_\mu A_\mu=0
\qquad\Longleftrightarrow\qquad
\sum_\mu\varepsilon_\mu\partial_\mu\bigl(r\,u_\mu\bigr)=0,
$$

which is the continuity equation for a density $r$ and a velocity $u_\mu$. **The spin-one fluid therefore has a continuity equation that is not an equation of motion**: it is the integrability of the field equation, and it disappears with the mass.

**The block's phrase is exact and the action explains it.** [The Spin-One Fluid](the-spin-one-fluid.html) finds that the fluid's free incompressibility is the mass's gift. The action's version: nothing in the derivative terms forces $\sum_\mu\partial_\mu(ru_\mu)$ to vanish, and the identity $\sum_{\mu,\nu}\partial_\mu\partial_\nu F_{\nu\mu}=0$ has no right-hand side to balance until the mass supplies one. **The incompressibility is not a property of the flow; it is a property of the pair $(r,u)$ and of the mass.**

**And the flow's own expansion is not zero.** Differentiating $ru_\mu$ gives $\sum_\mu\varepsilon_\mu\partial_\mu u_\mu=-\sum_\mu\varepsilon_\mu u_\mu\partial_\mu\ln r$, so the velocity's divergence is the density's logarithmic derivative along the flow. The divergence-free object is the field, and reading it as continuity is what makes the density and the velocity into a fluid's.

## The Noether Currents: Stress, Spin and No Charge

**No charge, and the spin is the field's own.** The Proca potential is real on the material sector, so the phase rotation is not a symmetry and there is no conserved charge; the parameter that would carry one is absent from the branch. What the chart does carry is the spin sector: the rotor is a physical variable here, unlike the scalar rungs, and its conjugate momentum is a genuine spin current.

**The stress.** The translation current is the chart's energy–momentum, with the mass term contributing $\tfrac12k_m^{2}\lvert\vec A\rvert^{2}$ to the energy density and the frame's sigma-model term contributing the rest. The stress is what the frame's transport conserves.

**Why the mass term does two things.** It fixes the longitudinal coefficient and it makes the spin's longitudinal polarisation physical. The first is a statement about the stress, the second about the spin current, and the article keeps them apart because a single term producing two effects is exactly what a reader is entitled to have explained twice.

**The sign.** With no charge there is no sign to fix, and the spin's sign is the frame's. That absence is the sharpest difference between this rung and the two below it, and it is why the fluid form of the Proca field is a fluid of a field and not of a medium.

## What the Principle Adds and What It Relabels: The Fluid Chart Against the Block

**Three statements, and the block makes each of them in the equations' language.**

*The vorticity is the direction's, and it is not the field strength.* $\omega=\mathrm{d}u$ and $F=r\,\mathrm{d}u+\mathrm{d}r\wedge u$, so the field strength carries the vorticity plus the density's gradient, and only in a region of constant density are the two the same object. The block's article states the vorticity and the self-dual split; the action states the decomposition that produces both.

*The rank of $\omega$ is two, and the reason is the dimension of the rest space.* The vorticity of a congruence is the curl projected onto the plane orthogonal to the flow, $\omega^{\perp}_{\mu\nu}=\sum_{\alpha,\beta}\mathsf{P}_{\mu\alpha}\mathsf{P}_{\nu\beta}\omega_{\alpha\beta}$ with $\mathsf{P}_{\mu\nu}=g_{\mu\nu}+u_\mu u_\nu$: $\omega^{\perp}$ annihilates $u$ by construction, and a two-form supported on three dimensions is simple, so its rank is at most two and is two wherever the vorticity is non-zero. **The raw curl is a different object, and its contraction with the flow is the acceleration**: $\sum_\nu\varepsilon_\nu\omega_{\mu\nu}u_\nu=-a_\mu$, so $\mathrm{d}u$ is neither transverse nor always simple — the block's sentence that $\omega\wedge\omega=0$ for every invertible element timelike flow holds for $\omega^{\perp}$ and not for $\mathrm{d}u$. The first-order charged fluid has rank two for the other reason, that a three-vector curl cannot make a four-dimensional two-form; the spinor fluid's is rank two for every solution, as its own article establishes.

*The equation of state is the mass term's, and the action shows it as the only term without a derivative.* The mass term $\frac{k_m^{2}}{2}r^{2}$ is the one term in the action that carries the density and no gradient, and it fixes the pressure in one line: the energy density it contributes is $\epsilon=\frac{k_m^{2}}{2}r^{2}$ and the force it exerts is $-\vec\nabla_\Phi\ln r$, so $\mathrm{d}p/(\epsilon+p)=\mathrm{d}\ln r$ and $p=\epsilon$. **A spin-one fluid is stiff, and the stiffness is the mass's**, which is the block's reading of the acceleration law; the action's addition is that no other law is available, because no other term of the action is free of derivatives.

## What the Principle Adds and What It Relabels: In the Fluid Chart

**Adds.** The mass term's double role, stated once: it removes the gauge freedom and supplies the condition that replaces it, and in the fluid's variables that condition is continuity. The pair of variations as the field equation's longitudinal and transverse parts, with the Lorenz condition as their consequence by an identity. The multiplier's necessity and its reading as a pressure. The decomposition of the field strength into vorticity and density gradient. And the reason this rung has no quantum force: the action has no second derivative of the magnitude.

**Does not add.** No new equation: the four components are the field's. No new current: the Proca current is $k_m^{2}A_\mu$ up to the normalisation, and it is the field. No gauge invariance to discuss, because the mass removed it. No thermodynamics, and no quantum potential, since this rung has none. And no statement about the massless limit's fluid reading, which the block's article explicitly denies.

**The one thing the action says that the equations cannot.** The Lorenz condition, the loss of gauge freedom, the continuity equation and the stiffness of the flow are four statements about four different objects, and in the action they are one term. **That is the strongest case in the layer for writing the fluid's Lagrangian**: not a new result, but the location of four results in one coefficient.

## What the Principle Adds and What It Relabels: The Fluid Alone

**The constraint becomes a property of the fluid's own frame.** In the element reading the vanishing of the scalar part of the conjugate gradient is a condition that the variation produces; in the fluid reading, the corresponding statement is that **the fluid's four-velocity cannot have a longitudinal component that carries the mass**. The constraint is the same equation, and the fluid reading says what it means: a pressure cannot push along the direction the fluid is already moving.

**What the fluid adds: no charge.** The stress is the whole of the fluid's content, and the charge is zero. In the element reading that is a computation; in the fluid reading it is a count — **a real flow has no phase to carry a charge**, and the article's section on the absence of a charge is the statement of the count in the fluid's language.

**What the fluid adds: the branch as a pressure sign.** The two branches of the Proca chart differ by the sign of the algebraic mass term, and in the fluid reading that sign is the sign of the pressure's own contribution. **A reader who has the branch as a sign of a coefficient can read it here as a sign of a pressure**, and the article says the two are the same statement.

**What it does not add.** No new solution and no new equation: every fluid equation is the element equation with a word changed. **The fluid reading's claim is interpretive and the article says so in its first paragraph.**

**What it inherits, and what it does not.** It inherits the frame's constrained character — the frame is fixed by the mass, not evolved — and it does not inherit the charge, which the Proca field never had. **The articles in this family that do have a charge are the coupled ones**, and the Proca fluid's silence about it is a statement rather than an omission.

**One difference from the spin-half fluid.** There the torque was the new object; here the pressure is. **A spin-one fluid has no torque because its spin is a frame and not a density of angular momentum**, and the article's comparison sentence says exactly that.

## Open Questions

1. **The massless limit.** The action's derivative terms survive at $k_m=0$ and the fluid reading does not, because the field becomes pure gauge and $A=ru$ is then a gauge-dependent split. Whether some gauge-fixed chart makes the limit continuous is not settled, and the block's article denies the reading without stating the obstruction in these terms.

2. **The constraint's class.** Whether the unit condition and the transverse projection produce a second-class system with a Dirac bracket that closes — the spin-one fluid's analogue of the spin article's open problem — is not computed here.

3. **The multiplier's sign.** $\lambda$ is determined by the equations and its sign is the density's gradient's, so a region of decreasing density has a negative pressure in this reading. Whether that is physical or an artefact of the split is not settled.

## Summary

**The action.** $\mathcal L=\frac12[(\partial r)^{2}-(u\cdot\partial r)^{2}]-\frac{r^{2}}{4}\omega^{2}-\sum_{\mu,\nu}\varepsilon_\mu r\,\omega_{\mu\nu}\partial_\mu r\,u_\nu+\frac{k_m^{2}}{2}r^{2}$, with $A=ru$ and $u^{2}=-1$.

**The mass term.** It removes the gauge freedom, supplies the Lorenz condition, and in the fluid's variables that condition is continuity $\sum_\mu\partial_\mu(ru_\mu)=0$. One term, four statements.

**The variations.** The density's is the field equation's longitudinal part, the direction's its transverse part, and the Lorenz condition is their consequence by $\partial\partial F=0$.

**The multiplier.** The only genuine one in the layer; it is the unit condition's force and plays a pressure's part.

**The quantum sector.** Absent: no $\hbar$ in the derivative terms, no quantum potential, no quantum force. The spin-one fluid is a classical field read as a medium.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A_\mu=r\,u_\mu$ | The field in the fluid's variables; $r$ the density, $u$ the velocity |
| $r>0$ | Density; the field's magnitude |
| $u_\mu$, $\sum_\mu\varepsilon_\mu u_\mu u_\mu=-1$ | Unit four-velocity; three functions and one constraint |
| $\omega_{\mu\nu}=\partial_\mu u_\nu-\partial_\nu u_\mu$ | The raw curl, whose contraction with $u$ is $-a_\mu$; its projection $\omega^{\perp}$ is the vorticity and is rank two |
| $F_{\mu\nu}=r\omega_{\mu\nu}+\partial_\mu r\,u_\nu-\partial_\nu r\,u_\mu$ | The field strength; vorticity plus density gradient |
| $k_m=mc/\hbar$ | Mass wave number; the only place $\hbar$ appears |
| $\nabla_\mu=\sum_\nu\mathsf{P}_{\mu\nu}\partial_\nu$ | Transverse derivative; $\mathsf{P}_{\mu\nu}=g_{\mu\nu}+u_\mu u_\nu$ |
| $\lambda$ | Multiplier of the unit condition; a pressure |
| $E_\mu=\sum_\nu\varepsilon_\nu F_{\mu\nu}u_\nu$ | The electric part along the flow |
| $a_\mu=\sum_\nu\varepsilon_\nu u_\nu\partial_\nu u_\mu$ | The flow's acceleration |
| $\mathcal L$ | The Proca Lagrangian in the fluid variables |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part |

## Further Reading

- Alexandru Proca, "Sur la théorie ondulatoire des électrons positifs et négatifs," *Journal de Physique et le Radium* **7** (1936) 347–353, for the massive vector field and the condition its mass implies.
- John R. Oppenheimer and Julian S. Schwinger, "On the interaction of mesotrons and nuclear particles," *Physical Review* **60** (1941) 150, for the massive vector field's constraint structure.
- Clifford Truesdell and Richard Toupin, "The classical field theories," in *Handbuch der Physik* III/1 (Springer, 1960), for the polar decomposition of a vector field into magnitude and direction and the strain it induces.
- Friedrich W. Hehl, "On the kinematics of the torsion of space-time," *Foundations of Physics* **15** (1985) 451–471, for a unit vector field's vorticity, its transversality and its rank.
- The companion articles: [The Lagrangian and the Proca Equation in Polar Variables](the-lagrangian-and-the-proca-equation-in-polar-variables.html), the same action in the chart and the branch's role; [The Spin-One Fluid](the-spin-one-fluid.html), the acceleration law without a quantum force and the Lorenz condition read as continuity; [The Third Polarization and the Self-Dual Split of the Massive Field Strength](the-third-polarization-and-the-self-dual-split-of-the-massive-field-strength.html), for the decomposition of $F$ that the substitution produces; and the charged companion [The Lagrangian and the Charged Spin-One Fluid](the-lagrangian-and-the-charged-spin-one-fluid.html), where the connection's divergence stops being zero and the condition stops being continuity.
