# __Spin-Half Fluid Equations from the Dirac Polar Action: Vorticity as the Curl of the Frame's Gradient__

## Introduction

[The Spin-Half Fluid of the Biquaternion Dirac Field](the-spin-half-fluid-of-the-biquaternion-dirac-field.html) reads the Dirac equation and names the density, the velocity, the spin direction and the vorticity. [The Lagrangian and the Dirac Equation in Polar Variables](the-lagrangian-and-the-dirac-equation-in-polar-variables.html) substitutes the word into the action and finds that the kinetic term closes, that four momenta vanish, and that the mass term needs a fixed direction.

That article also names the gap this one exists to fill: the constant setting drops the frame's spatial gradients, and the operator setting's action must contain them and does not compute them. This article takes the action route as far as the chart allows and states exactly how far that is.

**The claim, and its two halves.**

*The half that is established.* The fluid's four equations are four coordinates' equations, and the assignment is forced. Continuity is the phase's equation. The spin current is the rotor's momentum, and it is a derivative of the action and not a bilinear of the field. The guidance equation is the scale's equation, and it is a **constraint** and not an evolution, because the action is first order. The vorticity is not an equation at all: it is the curl of the velocity, and the velocity is the frame's square, so the vorticity is the frame's own Maurer–Cartan form.

*The half that is not.* The frame's spatial gradient block is not computed here. It is stated as the object the operator-setting action must contain, its role is identified, and the article does not pretend to a display it does not have.

**Why the assignment is worth making even so.** Under the equation route the spin current is a bilinear: one writes $\tilde\Xi^{*}$ times a generator times $\tilde\Xi$ and identifies the result with a current. Under the action route the spin current is $\partial L/\partial\dot\theta_{\mathrm{axr}}$, a momentum, and the identification is a definition rather than an interpretation. The two objects agree, and the second says why the first is conserved: the action is invariant under the rotor's shift, and the current is its Noether charge.

**The strongest objection.** *The polar companion already prints the momentum table, so the momenta are known and this article adds a vocabulary.* The objection names the article's real scope. The momenta are known. What is not in the polar companion is the statement of which fluid equation each momentum's equation is, and the statement that at this rung one of them is a constraint rather than an evolution, which is the structural difference between the spin-half fluid and the two scalar fluids.

**Position in the block.** This is the variational companion of [The Spin-Half Fluid of the Biquaternion Dirac Field](the-spin-half-fluid-of-the-biquaternion-dirac-field.html) and the free member of the pair whose coupled member is [The Charged Spin-Half Fluid from the Polar Action](charged-spin-half-fluid-equations-from-the-polar-action.html). It sits above the scalar rungs and below the vector rung.

## Conventions

**The conventions are the polar companion's, restated so that every sign is checkable from this page alone.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_{\imath}^{2}=-e_t$; $i$ central; $^{*}$ Hermitian, $^{\natural}$ quaternionic; $\mathrm{Sc}$ the coefficient of $e_t$; the pairing throughout is $\mathrm{Sc}(\cdot^{*}\cdot)$. The word is

$$
\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
\qquad
\tilde U_{\Psi,\mathrm b}=\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr),
\qquad
\tilde u_{\mathrm r}=\exp\Bigl(\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr),
$$

with $\varrho>0$, $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$, $\theta_{\mathrm{rpd}}\ge0$, $\theta_{\mathrm{axr}}\in[0,2\pi]$, unit real axes, and the ordering above. The coupled companion orders the rotor on the left; the two orderings differ by a conjugation of the boost axis and the free ordering is used here throughout.

The letters. The proper density is $\rho_{\mathrm{num}}=\varrho^{2}$ and the Lorentz factor is $\gamma=\cosh\theta_{\mathrm{rpd}}$, so the charge density is $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$. The action variable is $S_{\tilde\Xi}=\frac{h}{2\pi}\theta_{\mathrm{pha}}$. The rotor's **body** angular velocity is $\vec\omega_{\mathrm r}=\tilde u_{\mathrm r}^{-1}\dot{\tilde u}_{\mathrm r}$, and $\hat n_{\mathrm{rot}}=\tilde u_{\mathrm r}^{-1}\vec u_{\mathrm b}\tilde u_{\mathrm r}$ is the boost axis carried into the body frame. The idempotents of the declared direction are $\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$. The mass wave number is $\nu_m=\frac{mc}{h}$.

## The Action in the Word

The element form. The polar companion's action is

$$
S=\frac{h c}{4\pi}\int\mathrm{d}^{4}\varrho\;\mathrm{Re}\,\mathrm{Sc}\Bigl[\tilde\Xi_L^{*}\tilde\nabla_\Phi^{\natural}\tilde\Xi_L+\tilde\Xi_R^{*}\tilde\nabla_\Phi\tilde\Xi_R-2\pi\nu_m\bigl(\tilde\Xi_L^{*}\tilde\Xi_R+\tilde\Xi_R^{*}\tilde\Xi_L\bigr)\Bigr],
$$

and it is first order: the gradient is the only derivative.

The kinetic term, in closed form. With the ordering above,

$$
L_{\mathrm{kin}}=\frac{h}{2\pi}c\,\varrho^{2}\Bigl(\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}-\sinh\theta_{\mathrm{rpd}}\,\hat n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r}\Bigr),
$$

which is the polar companion's display and is quoted, not re-derived. Two features matter and neither is present at the scalar rungs.

**The phase momentum carries $\cosh\theta_{\mathrm{rpd}}$.** $p_{\theta_{\mathrm{pha}}}=\frac{h}{2\pi}c\varrho^{2}\cosh\theta_{\mathrm{rpd}}=\frac{h}{2\pi}c\,\rho_{\mathrm{chg}}$. The phase momentum is the charge density, exactly as at the scalar rungs.

**The spin momentum is a vector and it is not zero.** $p_{\theta_{\mathrm{axr}}}\hat{\ }=-\frac{h}{2\pi}c\varrho^{2}\sinh\theta_{\mathrm{rpd}}\,\hat n_{\mathrm{rot}}$. This is the article's hinge: at the scalar rungs the rotor's momentum vanishes and the fluid has no spin; here it does not vanish, and the rotor is transported.

The mass term, and the direction it needs. Written on the frame's parts the mass bilinear vanishes identically, because the two parts sit in complementary right ideals and $\mathrm{Sc}$ is cyclic. It returns only when the bilinear carries a fixed unit direction, $\tilde\Xi_R\mapsto\tilde\Xi_R i\vec v$. So the polar action carries a direction the element action does not, and only the directions perpendicular to the frame's third direction give a mass.

**That direction is a ninth object and it is not a coordinate of the word.** It is worth stating plainly: the action route at this rung needs data the chart does not supply. The word is a bijection onto the field; the mass direction is data of the value decomposition. A fluid reading that counts eight parameters therefore counts the field and not the action.

## The Variation: The Phase Equation Is Continuity

Varying $\theta_{\mathrm{pha}}$. The phase appears only in the kinetic term and only linearly in its rate, so the Euler–Lagrange equation is the conservation of the phase momentum,

$$
\partial_{\imath}\frac{\partial L}{\partial(\partial_{\imath}\theta_{\mathrm{pha}})}=0
\qquad\Longrightarrow\qquad
\partial_{r'_t}\rho_{\mathrm{chg}}+\vec\nabla_\Phi\cdot\bigl(\rho_{\mathrm{chg}}\vec v\bigr)=0,
$$

which is the spin-half fluid's continuity equation for the charge density.

**Three statements.**

*The conserved object is the charge density and the equation is exact.* No approximation, no weak-field step, and no spin correction. The spin does not enter continuity at all, and the reason is the one the type argument gives: the rotor's bracket is real-vector and the phase's bracket is central imaginary, and a variation of the phase cannot see the rotor.

*The velocity is the frame's.* The current is $\rho_{\mathrm{chg}}\vec v$ where $\vec v$ is read from the boost: the velocity is $ic\tilde U_{\Psi,\mathrm b}^{-2}$, a unit timelike element built from the frame alone. The density cancels out of it, which is why the velocity is a unit element and not a gradient.

*The equation is one coordinate's, and the coordinate is the phase.* The equation route obtains the same statement by multiplying the Dirac equation by $\tilde\Xi^{*}$ and taking the scalar part. The action route obtains it by varying one coordinate. Neither is deeper; the second is shorter and names the coordinate.

## The Variation: The Scale Equation Is a Constraint, and That Is the Rung's Mark

Varying $\varrho$. The scale appears in the kinetic term as $\varrho^{2}$ and in the mass term as $\varrho^{2}$, and no rate of $\varrho$ appears anywhere. Its Euler–Lagrange equation is therefore not an evolution equation:

$$
\frac{\partial L}{\partial\varrho}=0,
$$

an algebraic relation among $\dot\theta_{\mathrm{pha}}$, $\vec\omega_{\mathrm r}$, the frame's parameters and $\nu_m$.

**This is the guidance equation and it is a constraint.** At the scalar rungs the same statement is the mass shell, and it is an evolution equation because the action is second order. Here it is algebraic, and it fixes the velocity's norm rather than propagating it. The fluid reads it as the statement that the flow is on shell, and the on-shell condition is supplied by the action rather than imposed.

**The four vanishing momenta.** $p_\varrho=0$, $p_{\theta_{\mathrm{rpd}}}=0$, and the two conjugate to the boost axis vanish identically, on every configuration. Those four coordinates are the scale, the rapidity and the two angles of the boost axis, so their equations are the four constraints, and the four whose momenta do not vanish — the phase and the rotor's three — are the evolutions. The Dirac bracket is built on the four.

**Why the count matters for the fluid.** A fluid whose velocity is a unit element fixed by a constraint has no independent acceleration law. That is the sharp difference from the scalar rungs, where the velocity is a gradient and its acceleration is the gradient of the guidance equation. At this rung the acceleration is not a derived object: it is part of the constraint surface, and the spin-half fluid's Euler equation is a consequence of the constraint plus the spin transport, not a third variation.

## The Variation: The Rotor's Equation Is the Spin Transport

Varying $\theta_{\mathrm{axr}}$ and the rotor's axis. The rotor appears in the kinetic term through $\vec\omega_{\mathrm r}$ contracted with $\hat n_{\mathrm{rot}}$, and the momenta are the three-vector $-\frac{h}{2\pi}c\varrho^{2}\sinh\theta_{\mathrm{rpd}}\hat n_{\mathrm{rot}}$. The Euler–Lagrange equation is

$$
\partial_{t'}\Bigl(-\frac{h}{2\pi}c\varrho^{2}\sinh\theta_{\mathrm{rpd}}\,\hat n_{\mathrm{rot}}\Bigr)=\frac{\partial L}{\partial\theta_{\mathrm{axr}}},
$$

and on the flow the left side is the spin current's rate.

**The spin current is a momentum.** This is what the action route adds: the spin current is $\partial L/\partial\dot\theta_{\mathrm{axr}}$, so it is a derivative and not a bilinear. Under the equation route the same current is written $\tilde\Xi^{*}(\text{generator})\tilde\Xi$, and the two agree. The action route's version says why it is conserved: the action is invariant under a shift of the rotor's angle, and Noether's theorem supplies the current.

**The factor $\sinh\theta_{\mathrm{rpd}}$ is the rung's signature.** The spin momentum is proportional to the boost, so it vanishes in the rest frame however fast the rotor turns. A fluid at rest has no spin current, and a boosted one has a spin current proportional to its rapidity. That is not a small correction: it is the statement that the spin current and the boost are one object, and the polar companion says so in the same words.

**What the rotor's equation is not.** It is not a precession equation with a torque. The torque appears when the mass term's direction is varied and when the connection is coupled; the free action's rotor equation is a conservation law with no source, and the spin's precession is therefore not visible at this rung in this setting.

## The Vorticity: An Identity of the Chart

**The velocity and its square.** The velocity is $\tilde V_\Phi=ic\tilde U_{\Psi,\mathrm b}^{-2}$, a unit timelike element. It is a unit element squared, and the square of a unit element is not a gradient: a unit timelike element has three parameters against the one function a gradient supplies. There is therefore no scalar whose gradient is the velocity, and the flow is rotational in general.

**The identity.** The vorticity is the antisymmetrised gradient of the velocity's component spelling,

$$
\omega_{\imath\jmath}=\partial_{\imath}v_{\Phi,\jmath}-\partial_{\jmath}v_{\Phi,\imath},
$$

and because $\tilde V_\Phi$ is built from $\tilde U_{\Psi,\mathrm b}$ alone, differentiating gives products of the frame element with its logarithmic derivative $\tilde U_{\Psi,\mathrm b}^{-1}\partial_{\imath}\tilde U_{\Psi,\mathrm b}$. So the vorticity is the frame's Maurer–Cartan form read through the velocity, and it vanishes exactly where the frame is constant.

**What the action route contributes to this, and what it does not.** It contributes the statement that the frame's gradient is an object the *action* must contain: the operator-setting kinetic term is quadratic in $\tilde\Xi^{-1}\partial_{\imath}\tilde\Xi$, whose Hermitian part is the frame's connection. So the vorticity's source and the action's gradient term are one object, and that is why the vorticity is not an independent field. What the article does not contribute is the explicit block: the operator-setting gradient term in the three frame coordinates is not computed here, and the polar companion records the same gap.

**Three things the vorticity is not, and the corpus states all three.** It is not the spin: the spin direction is the rotor's image of the axis and the vorticity is the curl of the velocity, and the two are independent parameters tied only by the field equation. It is not the magnetic field: the Gordon term is a magnetisation current. And it has no independent dynamics: it is built from a Maurer–Cartan form, which is flat by construction.

## The Noether Currents: Charge, Spin, Stress

**Phase shift** gives the charge current, which is continuity's.

**Rotor shift** gives the spin current, which is the rotor's momentum. The two shifts are independent, and their two currents are the fluid's two conserved densities. That is the structural statement the spin-half rung adds to the scalar rungs, and it is visible in the chart as two coordinates with non-vanishing momenta.

**Translation** gives the stress, and its antisymmetric part is what a spin fluid has and a dust does not. The polar companion does not display it, and [The Spin-Half Energy-Momentum Tensor](the-spin-half-energy-momentum-tensor.html) owns it.

## What the Alternative Route Adds and What It Relabels

**Adds.** The spin current as a momentum rather than a bilinear, with the Noether argument that makes it conserved. The statement that the guidance equation is a constraint at this rung, and why: first order. The identification of the vorticity's source with the action's own gradient term, which is the reason the vorticity has no dynamics. And the honest count: the mass direction is a ninth object that the word does not carry.

**Does not add.** No new equation and no new solution. The polar companion's momentum table is the article's premise, and the spin-half fluid article's vorticity section is its conclusion. The explicit frame gradient block is named and not computed.

**Relabels.** "The spin is the rotor." On the equation route the spin is what the bilinear with the generator measures. On the action route the spin is the momentum conjugate to the rotor's angle, and the bilinear is the same object written in the field's letters. The second is what makes the spin a fluid variable, because a fluid's variables are its conserved densities.

## Open Questions

**The frame's gradient block.** The operator-setting kinetic term in $\theta_{\mathrm{rpd}}$ and $\vec u_{\mathrm b}$ is the object the vorticity is built from and the object the action lacks a display of. Until it is computed, the action route's vorticity statement is a statement about the chart's identity and not about the functional.

**The mass direction's variation.** The ninth object's variation is not an equation of the eight-coordinate system. Whether it is a constraint, a gauge direction, or the statement that the value decomposition must be fixed before the action is written, is open in the corpus and is named as open here.

## Summary

The Dirac polar action varies into the spin-half fluid's equations, and the assignment is forced by the momenta. The phase's equation is continuity for the charge density. The rotor's equation is the spin transport, with the spin current a momentum and not a bilinear. The scale's equation is a constraint and not an evolution, because the action is first order, and the four vanishing momenta make four constraints against the four evolutions of the phase and the rotor. The vorticity is not among the equations: it is the frame's Maurer–Cartan form read through the velocity, and the action's own gradient term is its source. The article adds the momenta's fluid reading and the rung's mark — a constrained velocity and a transported spin — and it states the gap it does not close.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\tilde\Xi=\varrho e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | the word, free ordering |
| $\rho_{\mathrm{num}}=\varrho^{2}$, $\gamma=\cosh\theta_{\mathrm{rpd}}$ | proper density and Lorentz factor |
| $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$ | charge density; $\frac{2\pi}{hc}$ times the phase momentum |
| $\vec\omega_{\mathrm r}=\tilde u_{\mathrm r}^{-1}\dot{\tilde u}_{\mathrm r}$ | rotor's body angular velocity |
| $\hat n_{\mathrm{rot}}=\tilde u_{\mathrm r}^{-1}\vec u_{\mathrm b}\tilde u_{\mathrm r}$ | boost axis in the body frame |
| $p_{\theta_{\mathrm{pha}}}=\frac{h}{2\pi}c\varrho^{2}\cosh\theta_{\mathrm{rpd}}$ | phase momentum |
| $p_{\theta_{\mathrm{axr}}}=-\frac{h}{2\pi}c\varrho^{2}\sinh\theta_{\mathrm{rpd}}\hat n_{\mathrm{rot}}$ | spin momentum |
| $\tilde V_\Phi=ic\tilde U_{\Psi,\mathrm b}^{-2}$ | velocity, a unit timelike element |
| $\omega_{\imath\jmath}$ | vorticity, the frame's Maurer–Cartan form through the velocity |
| $\vec v$ | mass direction, a ninth object not in the word |
| $\nu_m$ | $mc/h$ |

## Further Reading

- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, for the spin-half fluid, its spin tensor and its vorticity.
- Jean-Marie Souriau, *Structure of Dynamical Systems* (Birkhäuser, 1997), for the Maurer–Cartan form of the Lorentz group and its role in a spinning flow.
- Fritz London, "Superfluids" (Wiley, 1950), volume 1, for the bound spin current of a condensate.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), for the spin-half fluid's guidance equation and its constraints.
