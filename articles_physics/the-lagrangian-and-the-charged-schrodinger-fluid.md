# __The Lagrangian and the Charged Schrödinger Fluid__

**Declared omissions.** The reality of the action is settled inside the action section so slot 5 is omitted, with its four subsections. The second variation is not computed, so slot 8 is omitted. The two settings are not contrasted, so slot 10 is omitted. No limit is taken here, so slot 11 is omitted. No comparison beyond the parent is attempted, so slot 13 is omitted.

## Introduction

**The coupling is one substitution and the action shows it as one substitution.** In [The Lagrangian and the Schrödinger Fluid](the-lagrangian-and-the-schrodinger-fluid.html) the Lagrangian has four terms. Here two of the four change in a single way — the phase's derivative becomes a covariant derivative — and the third does not change at all. That asymmetry is the type argument of [The Charged Schrödinger Fluid](the-charged-schrodinger-fluid.html), and the action is where it is visible without a decomposition.

**Three results.**

*First, the minimal substitution acts inside the brackets and nowhere else.* The two replacements are $\partial_{t'}S\mapsto\partial_{t'}S-ϙ\varphi$ and $\vec\nabla_\Phi S\mapsto\nabla S-q\vec A$, and they are the two slots of one object: the four-derivative of the phase. The gradient energy is untouched.

*Second, the Lagrangian density is gauge invariant term by term, and not up to a total derivative.* The shift of the phase and the shift of the potential cancel inside each bracket, so no boundary term is needed and the invariance is exact in the density.

*Third, the action supplies the Clebsch structure that a rotational fluid needs, and it supplies it as a potential rather than as an extra pair of fields.* The velocity is $\vec\pi/m$, a gradient plus a potential; its curl is $ϙ\vec B/m$, which is the block's unconditional identity, and the rank is two because a three-vector curl is a rank-two object.

**Position in the block.** This is the variational companion of [The Charged Schrödinger Fluid](the-charged-schrodinger-fluid.html) and the second of the eight articles of this layer. It is the only one of the eight whose equation is first order, and therefore the only one in which the two slots of a single covariant derivative exhaust the action's dependence on the phase, with no shell term between them.

## Conventions

**The conventions are the corpus's, restated here so that every sign below is checkable from this page alone.** Those of the free companion, with the connection added: $ϙ$ is the coupling and equals minus the electric charge, $q=-ϙ$; $\varphi$ and $\vec A$ are the scalar and vector potentials; $\vec E=-\vec\nabla_\Phi\varphi-\partial_{t'}\vec A$ and $\vec B=\vec\nabla_\Phi\times\vec A$; a gauge transformation is $\theta_{\mathrm{pha}}\mapsto\theta_{\mathrm{pha}}+ϙ\Gamma/\hbar$, $\varphi\mapsto\varphi+\partial_{t'}\Gamma$, $\vec A\mapsto\vec A-\vec\nabla_\Phi\Gamma$. The field is $\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\varepsilon\,e_t$, $\rho_{\mathrm{num}}=\varrho^{2}$, and the covariant derivative is $\partial_\mu+\frac{iϙ}{\hbar}A_\mu$, so the mechanical momentum is $\tilde P^{\mathrm{mech}}=\tilde P+ϙ\tilde A$.

## The Action in the Fluid Variables

**The free action's two slots are the two places the connection can go, and it goes to both.** With $S=\hbar\theta_{\mathrm{pha}}$ and $\vec\pi=\vec\nabla_\Phi S-q\vec A$,

$$
\boxed{\;\mathcal L_{\mathrm{fl}}=-\rho_{\mathrm{num}}\Bigl(\partial_{t'}S-ϙ\varphi+\frac{\vec\pi^{2}}{2m}\Bigr)-\frac{\hbar^{2}}{2m}(\vec\nabla_\Phi \varrho)^{2}\;}
$$

**The first bracket is one object and not two.** The combination $\partial_{t'}S-ϙ\varphi$ is the time slot of the covariant derivative of the phase, and the corpus names it $\mathcal E=-\hbar\partial_{t'}\theta_{\mathrm{pha}}+ϙ\varphi$, the kinetic energy. The spatial slot is $\vec\pi$, the kinetic momentum. **Both are gauge invariant and neither is separately meaningful**: a shift of the phase moves both, and a shift of the potential moves both back.

**The gradient energy is unchanged, and the reason is algebraic.** The third term carries the amplitude and its derivatives and no phase, so no substitution can reach it. In the word, the amplitude and the phase are separate factors and the connection is a central element: it multiplies the phase factor and commutes past the amplitude. That is the whole of the type argument, and in the action it is the statement that one term of four is untouched.

**The action has no external potential and needs none.** In the free article $V$ stood for a potential given from outside; here the potentials are the coupling's own and the term $\rho_{\mathrm{num}}ϙ\varphi$ is the potential energy, $-\rho_{\mathrm{num}}q\varphi$ with $q=-ϙ$. A second external potential would be a second, unrelated coupling, and the article does not add one.

## The Variation: Three of Them

**Varying the phase gives continuity, and the current is the kinetic one.** $\mathcal L_{\mathrm{fl}}$ depends on $S$ through $\partial_{t'}S$ and $\vec\nabla_\Phi S$, and $\partial\mathcal L_{\mathrm{fl}}/\partial(\vec\nabla_\Phi S)=-\rho_{\mathrm{num}}\vec\pi/m$, so

$$
\partial_{t'}\rho_{\mathrm{num}}+\sum_j\partial_j\bigl(\rho_{\mathrm{num}}v_j\bigr)=0,
\qquad
\vec v=\frac{\vec\pi}{m}.
$$

**The equation is the free one with $\vec v$ replaced, and it is not a new equation.** The charge current is $ϙ\vec j$ and its conservation is this continuity equation multiplied by $ϙ$; neither the coupling nor the field appears in it, which is the statement that the continuity equation is the gauge invariance's Noether identity and not the dynamics'.

**Varying the amplitude gives the energy equation, and its gradient is the Lorentz force.**

$$
\partial_{t'}S-ϙ\varphi+\frac{\vec\pi^{2}}{2m}+Q=0
\qquad\Longrightarrow\qquad
\mathcal E=\frac{\vec\pi^{2}}{2m}+Q .
$$

The gradient of the first display is the block's acceleration law. The computation is three lines and it is worth doing once, because the two signs that are easiest to get wrong appear in it. Taking $\vec\nabla_\Phi$,

$$
\partial_{t'}\vec\pi+ϙ\vec E+\frac{1}{m}\sum_j\pi_j\nabla\pi_j+\vec\nabla_\Phi Q=0,
$$

using $\vec\nabla_\Phi(\partial_{t'}S)=\partial_{t'}\vec\pi-ϙ\partial_{t'}\vec A$ and $ϙ\vec\nabla_\Phi\varphi+ϙ\partial_{t'}\vec A=-ϙ\vec E$. Then $\sum_j\pi_j\nabla\pi_j=m(\vec v\cdot\nabla)\vec\pi+ϙ\,\vec v\times\vec B$, because $\vec\nabla_\Phi(\vec\pi^{2}/2)=\vec\pi\cdot\nabla\vec\pi+\vec\pi\times(\vec\nabla_\Phi\times\vec\pi)$ and $\vec\nabla_\Phi\times\vec\pi=ϙ\vec B$. Hence

$$
\frac{\mathrm{D}\vec\pi}{\mathrm{D}t}=-ϙ\bigl(\vec E+\vec v\times\vec B\bigr)-\vec\nabla_\Phi Q,
$$

which is the block's display and, with $q=-ϙ$, the standard force on a charge $q$. **The action therefore fixes the sign that the block's articles state**, and it fixes it in one place instead of three: the sign of $ϙ\varphi$ in the first bracket.

**The third variation is absent because there is no third field.** The velocity is $\vec\pi/m$, a function of the phase and the potential. Promoting it to a field would add a multiplier equal to the momentum density, exactly as in the free companion, and the constraint it enforces would be $\vec v=\vec\pi/m$ with $\vec\pi$ now carrying $\vec A$. Nothing is gained, and the rotational case does not need the promotion, for the reason the next section gives.

## The Constraints the Action Imposes: Gauge Invariance, Term by Term

**The density is invariant and not merely invariant up to a divergence.** Under $S\mapsto S+ϙ\Gamma$ and $\varphi\mapsto\varphi+\partial_{t'}\Gamma$,

$$
\partial_{t'}S-ϙ\varphi\longmapsto\partial_{t'}S+ϙ\partial_{t'}\Gamma-ϙ\varphi-ϙ\partial_{t'}\Gamma=\partial_{t'}S-ϙ\varphi,
$$

and under $\vec A\mapsto\vec A-\vec\nabla_\Phi\Gamma$ the combination $\vec\nabla_\Phi S-q\vec A$ is fixed by the same cancellation. The amplitude and the gradient energy do not move. So every term of $\mathcal L_{\mathrm{fl}}$ is separately invariant, and the action is invariant without a boundary term.

**The invariance is stronger than the free article's and it is a different kind.** The free action is invariant under a constant shift of the phase, which is a global symmetry with a Noether current. This one is invariant under a *local* shift, which is a redundancy and not a symmetry: the current it implies is the charge current, and its conservation is an identity rather than a consequence of the equations. **A local invariance gives no conserved quantity beyond the one the global subgroup gives**, and the global subgroup here is the constant shift, whose current is $ϙ\rho_{\mathrm{num}}$ — the charge density.

**The canonical energy is gauge dependent and the fluid's energy is not.** The Legendre transform of $\mathcal L_{\mathrm{fl}}$ in $\dot S$ gives $\rho_{\mathrm{num}}\vec\pi^{2}/2m+\mathcal E_{\mathrm{grad}}-\rho_{\mathrm{num}}ϙ\varphi$, which moves under a gauge transformation; the quantity $\mathcal E$ of the energy equation does not. This is the standard situation for a charged field, and it is worth stating because it limits what the article may call the fluid's energy: **$\mathcal E$ is the kinetic energy and it is gauge invariant; the canonical energy is the matter action's and only the sum with the field's energy is physical.** No thermodynamics is intended here, and the third category's local thermal state is a different object.

## The Structural Consequence: The Coupling Supplies the Clebsch Structure

**A rotational fluid needs a second representation of its velocity, and the connection is one.** The Clebsch form of a velocity with rank-two vorticity is $\vec v=\vec\nabla_\Phi\phi_{\mathrm{clb}}+\alpha_{\mathrm{clb}}\vec\nabla_\Phi\beta_{\mathrm{clb}}$, with the pair carrying the curl. Here

$$
\vec v=\frac{\vec\nabla_\Phi S}{m}+\frac{ϙ}{m}\vec A,
$$

so the representation is of that shape after a transcription: $\phi_{\mathrm{clb}}=S/m$, and the whole second term is the pair's, because $\vec A$ is one vector where the Clebsch form wants two scalars. **The potential plays the pair's part and is not itself a pair.** Its own curl is the vorticity, so its two stream functions are what the pair would be, and they belong to the field rather than to the matter. The transcription is exact and the point of it is that a constant $\alpha_{\mathrm{clb}}$ would describe an irrotational flow: the rotation is in $\vec A$ and not in the coupling's coefficient.

**The rank follows and it is the block's.** The curl of the velocity is a three-vector, $\vec\nabla_\Phi\times\vec v=ϙ\vec B/m$, so the vorticity two-form has no time-space part and its rank is at most two. The block's ladder says the same: the charged Schrödinger fluid has rank two where the field is present, and the charged spin-zero fluid reaches rank four only when $\vec E\cdot\vec B\ne0$, because only a four-vector velocity with the shell's norm can carry a vorticity that knows both halves of the field. **The action explains the rank**: the velocity's second term is a three-vector potential, and a three-vector cannot make a four-dimensional two-form.

**What the action adds to the block's statement is the reason the pair costs nothing.** In a classical rotational fluid the Clebsch pair is two extra fields with their own equations, and [The Clebsch Potentials and the Rank of the Vorticity](the-clebsch-potentials-and-the-rank-of-the-vorticity.html) states the cost. Here the pair is not extra: the potential is already in the action as the thing the phase couples to, and its equation is Maxwell's, which the matter action does not contain. **The charge fluid is rotational for free because its rotation is the field's.**

## The Noether Currents: The Charge the Coupling Creates

**The charge exists because the coupling does.** The free Schrödinger fluid is neutral; with the connection present the phase rotation is local and compensated, so the current that the connection multiplies is conserved:

$$
\rho_{\mathrm{chg}}=q\,\rho_{\mathrm{num}},
\qquad
\vec j_{\mathrm{chg}}=q\,\rho_{\mathrm{num}}\vec v ,
\qquad
\vec v=\frac{\vec\nabla_\Phi S-q\vec A}{m},
$$

with $q$ the charge. The velocity is the mechanical one, and that is the whole of the coupling's effect on the current.

**The energy and the quantum potential.** The stress is the free one, because the quantum potential depends on $\varrho$ alone and the coupling does not touch $\varrho$. So the charge current is covariantised and the stress is not, which is the article's *What the Charge Does Not Change* seen from the currents.

**The sign.** The sign of the charge is the sign of $q$, and the density remains positive. The two are independent: a negative charge with a positive density is a negative temporal component, and the article's gauge-invariance section is what makes the pair consistent under a gauge transformation.

## What the Principle Adds and What It Relabels: In the Fluid Chart

**Adds.** The coupling as one substitution in one object, the four-derivative of the phase, rather than as three separate amendments to three equations. The gauge invariance as an exact property of the density, with the reason each term is separately invariant. The sign of the Lorentz force fixed once, at the potential energy's term. The Clebsch structure identified as the connection, which explains the rank and explains why the pair is free. And the quantum sector visible as the one term the connection cannot reach.

**Does not add.** No new equation: the two Euler–Lagrange equations are the block's, and the acceleration law is the second's gradient. No new current: the charge current is the phase current multiplied by the coupling. No field equation: the action is the matter action, and $\vec E$ and $\vec B$ are given. No statement about the quantum potential's gauge behaviour beyond its invariance, which is the free article's.

**The one thing it states that the block does not.** The block's charged article notes that the coupling adds no fourth datum and adds a redundancy. The action states the redundancy as the invariance of the density, and it lets the count be read: four terms, two of them gauge invariant only in pairs, one of them not gauge dependent at all, and one of them — the potential energy — whose partner is the phase's time derivative. **The count of independent gauge-invariant combinations is two**, $\mathcal E$ and $\vec\pi$, and they are the two the word's phase and boost would have supplied at the rung above.

## What the Principle Adds and What It Relabels: The Fluid Alone

**The coupling becomes a modification of the fluid's own velocity.** In the element reading the connection enters the covariant bracket; in the fluid reading, the corresponding statement is that **the velocity that carries the density is not the canonical velocity but the gauge-shifted one**. The minimal substitution is then not a recipe but a description: the fluid moves in the field the particle feels, not in the potential the chart names.

**What it adds: the two velocities and the slip between them.** The canonical velocity and the mechanical velocity differ by the connection evaluated along the flow, and the fluid reading is where both are written side by side. **The element reading has the same two objects but does not need to distinguish them**, because it never asks which one carries the density. The fluid reading asks, and the answer — the mechanical one — is the article's contribution.

**What it adds: the density fluctuation and the potential.** The charge density is the density, and the potential's coupling to it is an energy. In the fluid reading that energy is a pressure-like term in the fluid's own frame, with the temporal slot entering through the rapidity and the spatial slot through the boost. **The two slots' different types are visible here as two different pressures**, which is a statement the element reading can make only as a type fact.

**What it does not add.** No new equation: **the continuity equation is the same continuity equation with a covariant divergence**, and the article says so in one line.

**What it inherits.** The gauge covariance, the nodal exception, and the frame's constrained character. **The first is inherited exactly and the third is inherited with a shift**, because the potential now depends on the frame and the frame is where the potential is extremal.

**What the coupling costs the fluid reading.** Nothing. **The fluid reading was already the reading in which the velocity is primary, and the coupling is a velocity shift**, so the coupled fluid is the free fluid with one word changed. The article's brevity about it is deliberate.

## Open Questions

1. **The pair's rank in the operator setting.** The action above is written for a homogeneous field. In the inhomogeneous case the amplitude's gradient and the potential's gradient both carry spatial structure, and whether the Clebsch identification survives — that is, whether the potential remains a second potential when $\vec B$ varies — is not settled here. The block's charged article keeps its identity $\vec\nabla_\Phi\times\vec v=ϙ\vec B/m$ in general, so the rank statement survives; the *representation* is the part that may not.

2. **The boundary term at the nodes.** The action is stated on $\varrho>0$, as in the free companion. Whether the gradient energy's variation produces a boundary term at a nodal surface that requires a condition there is not addressed, and [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html) is where the surface itself is described.

## Summary

**The action.** $\mathcal L_{\mathrm{fl}}=-\rho_{\mathrm{num}}(\partial_{t'}S-ϙ\varphi+\vec\pi^{2}/2m)-\frac{\hbar^{2}}{2m}(\vec\nabla_\Phi \varrho)^{2}$, with $\vec\pi=\vec\nabla_\Phi S-q\vec A$.

**The variations.** The phase gives continuity with $\vec j=\rho_{\mathrm{num}}\vec v$; the amplitude gives $\mathcal E=\vec\pi^{2}/2m+Q$; the gradient of the second is $\mathrm{D}\vec\pi/\mathrm{D}t=-ϙ(\vec E+\vec v\times\vec B)-\vec\nabla_\Phi Q$, which is the standard Lorentz force for $q=-ϙ$.

**The coupling.** One substitution in the phase's four-derivative. Two terms changed, one untouched, and the untouched one is the whole of the quantum correction.

**The Clebsch structure.** The velocity is a gradient plus a potential, so the connection *is* the second Clebsch potential and the vorticity's rank is two. The pair costs nothing because it is the field.

**Gauge invariance.** Exact in the density, term by term, with no boundary term. The canonical energy is gauge dependent; $\mathcal E$ is not.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\varepsilon\,e_t$ | The word; the free article's, unchanged |
| $ϙ$ | Coupling; minus the electric charge, $q=-ϙ$ |
| $\varphi$, $\vec A$ | Scalar and vector potentials; gauge dependent |
| $S=\hbar\theta_{\mathrm{pha}}$ | Phase; gauge dependent |
| $\partial_{t'}S-ϙ\varphi$ | Time slot of the covariant derivative; the kinetic energy's negative |
| $\vec\pi=\vec\nabla_\Phi S-q\vec A$ | Kinetic momentum; gauge invariant |
| $\vec v=\vec\pi/m$ | Velocity; gauge invariant |
| $\mathcal E=-\partial_{t'}S+ϙ\varphi$ | Kinetic energy; gauge invariant |
| $\rho_{\mathrm{num}}=\varrho^{2}$ | Density; gauge invariant |
| $Q=-\hbar^{2}\Delta_\Phi \varrho/(2m\varrho)$ | Quantum potential; untouched by the coupling |
| $\mathcal E_{\mathrm{grad}}=\frac{\hbar^{2}}{2m}\int(\vec\nabla_\Phi \varrho)^{2}$ | Gradient energy; untouched by the coupling |
| $\vec E=-\vec\nabla_\Phi\varphi-\partial_{t'}\vec A$, $\vec B=\vec\nabla_\Phi\times\vec A$ | Field strengths; gauge invariant |
| $\phi_{\mathrm{clb}},\alpha_{\mathrm{clb}},\beta_{\mathrm{clb}}$ | Clebsch potentials; here $\phi_{\mathrm{clb}}=S/m$, $\alpha_{\mathrm{clb}}=ϙ/m$, $\beta_{\mathrm{clb}}$ the potential's |
| $\mathcal L_{\mathrm{fl}}$ | The Lagrangian density in the fluid variables |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part |

## Further Reading

- Erwin Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1926) 322–326, for the fluid equations before a connection is added.
- Takehiko Takabayasi, "On the formulation of the Schrödinger theory in terms of the hydrodynamical quantities," *Progress of Theoretical Physics* **8** (1952) 143–164, for the velocity treated as an independent variable, which is what the Clebsch structure is.
- Fritz London, "Zur Theorie der Supraleitung," *Zeitschrift für Physik* **37** (1926) 915–925, for the phase's gauge behaviour and the current it implies.
- Peter R. Holland, *The Theory of Motion* (Cambridge University Press, 1993), chapter 4, for the charged fluid's energy equation and the gauge dependence of its canonical energy.
- Clifford Truesdell and Richard Toupin, "The classical field theories," in *Handbuch der Physik* III/1 (Springer, 1960), §157, for the Clebsch representation and the rank of a velocity field.
- The companion articles: [The Lagrangian and the Coupled Schrödinger Equation in Polar Variables](the-lagrangian-and-the-coupled-schrodinger-equation-in-polar-variables.html), the same action in the polar chart; [The Charged Schrödinger Fluid](the-charged-schrodinger-fluid.html), the equations varied here; [The Lagrangian and the Schrödinger Fluid](the-lagrangian-and-the-schrodinger-fluid.html), the $ϙ=0$ case; [The Clebsch Potentials and the Rank of the Vorticity](the-clebsch-potentials-and-the-rank-of-the-vorticity.html), for the representation the coupling supplies; and [The Lagrangian and the Charged Spin-Zero Fluid](the-lagrangian-and-the-charged-spin-zero-fluid.html), where the same substitution meets the mass shell.
