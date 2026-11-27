# __The Charged Spin-Half Fluid from the Polar Action: Charge Reaches the Velocity and Not the Spin__

## Introduction

[The Charged Spin-Half Fluid: Charge Couples to the Lorentz Force, Spin Does Not](the-charged-spin-half-fluid-charge-couples-to-the-lorentz-force-spin-does-not.html) states the rung's division of labour in its title. [The Lagrangian and the Coupled Dirac Equation in Polar Variables](the-lagrangian-and-the-coupled-dirac-equation-in-polar-variables.html) writes the coupled action in the eight coordinates and gives the type table that produces the division.

This article varies the action and reads the division as a statement about fluid equations. The connection is central, so it has one type in each slot, and the type decides which bracket it reaches: the phase's in time, the boost's in space, and neither the scale's nor the rotor's.

**The claim, and why it is not the scalar rungs' claim.**

*At the scalar rungs the connection could not reach the velocity.* There the velocity is a phase gradient, the connection joins the phase's bracket, and its effect on the flow is a shift inside a gradient. Here the velocity is the boost, and the connection's spatial part is Hermitian — the boost's own type. So the connection reaches the velocity directly, and the velocity it reaches is the mechanical one.

*At this rung the connection cannot reach the spin.* The rotor's bracket is a real vector and the connection is central, so the two never meet. The spin current is charge-blind, exactly and by type.

*The two statements are one table.* The type table is the article's instrument: four brackets, four types, and a central addition that joins two of them. What the fluid reads from it is which of its equations is covariant and which is untouched.

**The strongest objection.** *That charge bends the flow and not the spin is in the fluid article's title, so the article restates a known result.* It restates the result and replaces its warrant. The fluid article's warrant is a computation with the equation; this article's is the algebraic type of a central number against four brackets, and the type argument is the one that survives when the field is not a solution. The difference matters at one point: the type argument says the spin's neutrality is not an accident of the Dirac matrices, and a reader who thinks it is will not find the reason in the equation route.

**Position in the block.** The coupled member of the pair whose free member is [Spin-Half Fluid Equations from the Dirac Polar Action](spin-half-fluid-equations-from-the-dirac-polar-action.html).

## Conventions

**The conventions are the free companion's, with the coupled companion's ordering.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$, $\vec e_{\imath}^{2}=-e_t$; $i$ central; $^{*}$ Hermitian, $^{\natural}$ quaternionic; $\mathrm{Sc}$ the coefficient of $e_t$; the pairing $\mathrm{Sc}(\cdot^{*}\cdot)$. The word is

$$
\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\,\tilde u_{\mathrm r}\,\tilde U_{\Psi,\mathrm b},
$$

with $\varrho>0$, $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$, $\theta_{\mathrm{rpd}}\ge0$, $\theta_{\mathrm{axr}}\in[0,2\pi]$, unit real axes, and the rotor on the left, which is the coupled companion's ordering.

**On the ordering, stated once.** The free companion orders the boost first and obtains a cross term between the rotor's rate and the boost axis in the temporal slot. The coupled companion orders the rotor first and obtains the phase's term alone. The two orderings describe the same field and differ by conjugating the boost axis by the rotor; the split of the eight equations into evolutions and constraints differs between them, and this article uses the coupled companion's split throughout and does not transfer the free one.

The connection. $\tilde A_\Phi=i a'_t e_t+\vec A$ with real components, $ϙ$ the coupling, $q=-ϙ$, and $\mathcal A^{\mathrm{gco}}_{\imath}=\mathcal A_{\imath}+\frac{2\pi iϙ}{h}A_{\imath}$. The mechanical momentum is $\vec\pi=\vec p-q\vec A$. The densities are $\rho_{\mathrm{num}}=\varrho^{2}$, $\gamma=\cosh\theta_{\mathrm{rpd}}$, $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$.

## The Action in the Word

The functional. The coupled companion's action is

$$
S=\int\mathrm{d}^{4}\varrho\;\Bigl[-\frac{h}{2\pi}c\,\rho_{\mathrm{num}}\,\partial_{r'_t}\theta_{\mathrm{pha}}-\rho_{\mathrm{num}}\,V\Bigr],
$$

with $\rho_{\mathrm{num}}$ the frame density and $V$ the potential's scalar part in the frame.

**The kinetic term is the phase's term and nothing else.** The scale, the boost and the rotor contribute to it only through the density. The companion's reason is a pairing argument: the pairing takes the scalar part, the scalar part of a product of brackets vanishes unless the types match, and in the temporal slot only the phase's central imaginary bracket and the boost's Hermitian bracket have a partner.

**The connection's two destinations.** The companion's table reads the temporal slot's addition as central imaginary, so it joins the phase's bracket, and the spatial slots' as Hermitian, so they join the boost's. It reaches neither the scale's nor the rotor's. In the action that shows up as the structure of $V$: $V$ depends on the rapidity and the boost axis and not on $\theta_{\mathrm{pha}}$.

**The reading differs from the scalar rung's, and the difference is the pairing's.** There the temporal addition is real and joins the scale, and the spatial one is imaginary and joins the phase. The spinor action pairs one chiral term with the quaternionic conjugate, which reverses the sign of the vector part, and the reversal is what exchanges the two destinations. A reader comparing the two rungs' tables should read the exchange as a fact about $\natural$ and not as a mistake in either.

**The four lines of the table, which is the article's spine.**

| bracket | type | connection | fluid equation |
| --- | --- | --- | --- |
| scale | real scalar | none | the density, and the guidance constraint |
| phase | central imaginary | temporal | continuity |
| boost | Hermitian | spatial | the velocity, and the Lorentz force |
| rotor | real vector | none | spin transport |

**What the table says in one sentence.** The connection reaches the two brackets the fluid reads its current and its velocity from, and it reaches neither of the two the fluid reads its density and its spin from.

## The Variation: Continuity Is Covariant, and Its Coefficient Is Not

Varying $\theta_{\mathrm{pha}}$. The phase appears in the kinetic term and, through $V$, not at all, because the connection's temporal part joined the phase's bracket in the logarithmic derivative and $V$ is a function of the frame. So

$$
\partial_{r'_t}\rho_{\mathrm{num}}+\vec\nabla_\Phi\cdot\bigl(\rho_{\mathrm{num}}\vec v\bigr)=0,
$$

with $\vec v$ the mechanical velocity.

**Three statements.**

*Continuity's coefficient is the proper density, and the connection does not change it.* This is the table's first line: the scale's bracket is real and central, so no central addition can join it. The charge density is $\gamma\rho_{\mathrm{num}}$ and $\gamma$ is the frame's.

*Continuity's current is the mechanical one, because the connection is in the phase's bracket.* The current is what the phase's momentum is, and the phase's momentum is read from the covariant rate.

*Continuity is the only evolution equation that carries a density.* The companion's count is two evolutions and six constraints, and the two are the scale's and the phase's. The phase's is the fluid's continuity; the scale's is a constraint and is treated below.

## The Variation: The Boost's Equation Is the Mechanical Velocity

Varying the boost's rapidity and axis. The connection's spatial part is Hermitian, so it joins the boost's bracket, and the boost's equation is the one that reads the velocity.

**What that means and why it is new relative to the scalar rungs.** At the scalar rungs the velocity is the phase gradient over the mass, and the connection's only route into it is the phase's bracket, so the velocity is shifted inside a gradient and the shift is a gauge transformation. Here the velocity is the boost, which is a frame element and not a gradient, and the connection's spatial part is exactly a frame element's type. The shift is therefore a shift of the frame, and a shift of the frame is not a gauge transformation: it changes the velocity.

**The fluid's statement.** The guidance constraint fixes the velocity's norm, and the velocity it fixes is the mechanical one, so $\sum_{\imath}\varepsilon_{\imath}\pi_{\imath}\pi_{\imath}$ is what appears. The Lorentz force in the acceleration is the derivative of that constraint, and it enters the same way it entered at the scalar rungs: as what the mechanical momentum does, not as an added term.

**The honesty.** The action here is first order, so this is a constraint and not an evolution: the velocity is fixed algebraically, and there is no independent acceleration law to display. A reader who wants the Lorentz force as a term in an equation of motion must go to the rung where the velocity is dynamical, and that is the vector rung.

## The Variation: The Rotor's Equation Is Charge-Blind

Varying the rotor's angle and axis. The rotor's bracket is a real vector, the connection is central, and the two cannot meet: the connection cannot enter the rotor's equation by any route, whatever the ordering. In the constant setting the equation is

$$
\frac{\partial V}{\partial\theta_{\mathrm{axr}}}=0,
\qquad
\frac{\partial V}{\partial\vec u_{\mathrm r}}=0,
$$

**The equation's status, stated honestly.** In the coupled companion's ordering the rotor's kinetic term is absent, so the rotor's equation carries no time derivative and is one of the six constraints: it says that $V$ is stationary in the rotor's parameters. The transport law appears when the rotor's bracket is restored to the kinetic term, which is the operator setting where $\theta_{\mathrm{axr}}$ becomes a field and the action acquires its gradient. So this article reads the constant setting's equation and states what the operator setting must add.

**Two consequences, and the second is the one that matters.**

*The spin current's form is unchanged by the coupling.* Where the rotor's momentum exists — the free companion's ordering, and the operator setting — its magnitude is proportional to $\varrho^{2}\sinh\theta_{\mathrm{rpd}}$ and its direction is the rotor's image of the boost axis, and neither carries $ϙ$. That is the fluid article's "spin does not couple to the Lorentz force", stated as a type.

*The spin's transport has no coupling in it, and its solution does.* The rotor's equation contains $V$, and $V$ depends on the connection through the boost and the rapidity. So the coupling changes where the frame sits and not which bracket the rotor's equation reads. This is the precise sense in which the spin is neutral: neutral means no coupling in its own equation, not no effect on its motion.

**The objection.** *A spin whose frame is moved by the coupling is a spin that couples.* The objection conflates the equation with its solution. The claim is that the rotor's equation has no $ϙ$ of its own — the connection never joins the rotor's bracket — so the rotor's law is the free one; the values it produces are the coupled ones. The fluid article's title says exactly this and the type table is its reason.

## The Constraints: Two Evolutions and Six Constraints

**The count.** Eight equations, two carrying a time derivative, and the companion's split is the scale's and the phase's.

**What the six are.** The six are the parameters whose velocity the action does not contain: the four frame angles that are not the rotor's, together with the two whose equations the potential fixes. Their equations say that the frame sits where the potential is extremal in the frame variables, which is the companion's display.

**No multipliers, and the distinction.** The parameterisation is exact, so the unit conditions cost nothing: the boost and the rotor are exponentials and no condition has to be imposed. The constraints are nevertheless there and they are Euler–Lagrange equations of the same functional. A reader who takes "no multipliers" for "no constraints" has the wrong picture.

**The fluid's use of the count.** The fluid's continuity is one of the two evolutions. The six constraints fix the frame, and the frame is what the fluid's velocity and spin are built from: the velocity is the boost, the spin direction is the rotor's image of the boost axis. So one of the fluid's two equations is an evolution and the other is read off the constraint surface, and the six constraints are what makes the velocity a unit element rather than a gradient. At the free rung the rotor's momentum exists and the spin's law is an evolution; here, in this ordering, it does not, and the difference is the ordering rather than the coupling.

## The Noether Currents: Charge, Spin, Stress

**Phase shift** gives the charge current. It is continuity's, and it is the source of the connection's equation.

**Rotor shift** gives the spin current. It carries no $ϙ$, and the reason is the table's fourth line.

**Translation** gives the stress. The coupling enters through the mechanical momentum in the momentum part and through the quadratic term in $A$ in the field part, and the antisymmetric part is the spin's.

**The two currents' independence.** The charge and the spin are two shifts with two charges, and neither is a function of the other. At the scalar rungs there is one; here there are two; at the vector rung there is one charge and a spin that the chart does not carry. The count of conserved densities is the rung's signature, and it is read off the momenta.

## What the Alternative Route Adds and What It Relabels

**Adds.** The type table as the reason for the division of labour, and the statement that the connection reaches the velocity at this rung because the velocity is a frame element and not a gradient. The distinction between a neutral equation and a neutral trajectory. And the location of the coupling in $V$ rather than in the kinetic term, which is what makes the constraint structure survive.

**Does not add.** No new equation. The fluid article's three claims are the article's conclusions and its own computation is the warrant for them; this article supplies a second warrant. The operator setting's frame gradients are not computed, as in the free article.

**Relabels.** "Charge couples to the Lorentz force and not to the spin." On the equation route this is a property of the Dirac matrices and the bilinears they contract. On the action route it is a property of a central number against four brackets, and it is therefore independent of the representation.

## Open Questions

**The constraint algebra.** Whether the six constraints are first class or second class is the companion's open question, and the fluid reading inherits it: a first-class constraint would be a gauge direction of the chart, and a second-class one restricts the initial data.

**The operator setting.** Whether the frame's gradient terms close into a spin-transport law in the operator setting, with the connection in the boost's slot only, is open in both companions and here.

## Summary

The coupled Dirac polar action varies into the charged spin-half fluid's equations, and the division of labour between charge and spin is the algebraic type of a central connection against four brackets. The connection joins the phase's bracket in time and the boost's in space, so continuity is covariant and the velocity is mechanical; it joins neither the scale's nor the rotor's, so the density's own equation and the spin's transport are unchanged. The spin's equation has no coupling in it and its solution does, and that is what neutrality means. Two evolutions and six constraints, no multipliers for the units, and two conserved densities where the scalar rungs have one.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\tilde\Xi=\varrho e^{i\theta_{\mathrm{pha}}}\tilde u_{\mathrm r}\tilde U_{\Psi,\mathrm b}$ | the word, coupled companion's ordering |
| $\rho_{\mathrm{num}}=\varrho^{2}$, $\gamma=\cosh\theta_{\mathrm{rpd}}$ | proper density and Lorentz factor |
| $\mathcal A^{\mathrm{gco}}_{\imath}$ | $\mathcal A_{\imath}+\frac{2\pi iϙ}{h}A_{\imath}$ |
| $\vec\pi=\vec p-q\vec A$ | mechanical momentum |
| $\hat n_{\mathrm{rot}}$ | boost axis in the body frame |
| $p_{\theta_{\mathrm{axr}}}$ | spin momentum, $-\frac{h}{2\pi}c\varrho^{2}\sinh\theta_{\mathrm{rpd}}\hat n_{\mathrm{rot}}$ |
| $V$ | potential, frame-dependent and phase-independent |
| $ϙ$, $q=-ϙ$ | coupling and electric charge |

## Further Reading

- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, for the spin-half fluid with an external field.
- Jean-Marie Souriau, *Structure of Dynamical Systems* (Birkhäuser, 1997), for the frame element as a Lorentz-group element and the Maurer–Cartan form as its connection.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), for the spin-half fluid's guidance constraint.
- Friedrich W. Hehl, Paul von der Heyde and G. David Kerlick, "General relativity with spin and torsion: foundations and prospects," *Reviews of Modern Physics* **48** (1976) 393–416, for the separation of a spinning flow's spin current from its circulation.
