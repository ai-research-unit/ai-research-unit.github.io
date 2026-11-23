# __The Lagrangian and the Charged Spin-Zero Fluid__

## Introduction

At this rung the coupling adds no term to the action; it changes one variable. The two terms of [The Lagrangian and the Spin-Zero Fluid](the-lagrangian-and-the-spin-zero-fluid.html) survive intact, and the only change is that the four-velocity is the mechanical one, $\tilde V_\Phi=\tilde P^{\mathrm{mech}}_\Phi/m$ with $\tilde P^{\mathrm{mech}}_\Phi=\tilde P_\Phi+ϙ\tilde A_\Phi$. That is the minimal coupling stated covariantly, and it is why the density is untouched: a substitution inside one square cannot reach a term that carries no phase.

*First, the action is written in gauge-invariant variables, so its gauge invariance is not a symmetry but a redundancy already quotiented out.* The free action's phase $S_{\tilde\Xi}$ and the potentials appear only in the combination $\partial_{\imath} S_{\tilde\Xi}-q A_{\imath}$. The action is therefore a functional of $\varrho$ and that combination alone, and no shift of either moves it. At the first-order rung the invariance had to be checked term by term inside two brackets; here the bracket is one object and the checking is a definition.

*Second, the mass shell is unchanged in form and the whole of the coupling is in the velocity.* The variation of the density returns $\sum_{\imath} V_{\Phi,\imath}V_{\Phi,\imath}=-c^{2}-2Q_{\mathrm{qnt}}/m$, the free display verbatim, with $V$ the mechanical velocity. The connection's spatial part enters the velocity and not the shell: the shell's right-hand side carries the density and the d'Alembertian, and the coupling cannot reach either.

*Third, the vorticity is the field strength, and the action says why it costs nothing.* The velocity's curl is the curl of a potential, so $\omega_{\imath\jmath}=ϙ F_{\imath\jmath}/m$ is an identity about the variables and not an equation about the flow. In the Clebsch language the connection supplies the second and third potentials, and their rank is the field's.

This is the variational companion of [The Charged Spin-Zero Fluid](the-charged-spin-zero-fluid.html) and the fourth of the eight articles of this layer. It is the first in which the action's variables are gauge invariant by construction, and the first in which the fluid's vorticity is not a property of the flow.

## Conventions

The conventions are restated here so that every sign below is checkable from this page alone. Those of the free companion, with the connection: $ϙ$ is the coupling, $q=-ϙ$ the electric charge; $\tilde A_\Phi=i a'_t e_t+\sum_\eta A_\eta\vec e_\eta$ with $a'_t=\omicron_{\mathrm{pot}}$; the covariant derivative is $\partial_{\imath}+\frac{2\pi iϙ}{h}A_{\imath}$; $\tilde P^{\mathrm{mech}}_\Phi=\tilde P_\Phi+ϙ\tilde A_\Phi$; $F_{\imath\jmath}=\partial_{\imath} A_{\jmath}-\partial_{\jmath} A_{\imath}$, $\vec E=-\vec\nabla_\Phi\omicron_{\mathrm{pot}}-\partial_{t'}\vec A$, $\vec B=\vec\nabla_\Phi\times\vec A$. A gauge transformation is $S_{\tilde\Xi}\mapsto S_{\tilde\Xi}+ϙ\Gamma$ together with $A_{\imath}\mapsto A_{\imath}-\partial_{\imath}\Gamma$, that is $\theta_{\mathrm{pha}}\mapsto\theta_{\mathrm{pha}}+\frac{2\pi ϙ\Gamma}{h}$. The temporal slot's sign is the one that looks odd and is not: the invariant is $W_0=(\partial_{t'}S_{\tilde\Xi}+ϙ a'_t)/m$, so the scalar potential moves against the phase and not with it, where the first-order rung's bracket $\partial_{t'}S-ϙ\omicron_{\mathrm{pot}}$ carries the opposite sign on the phase and the potential moves with it. The two rungs differ in the sign of one bracket and in nothing else, and a reader moving between the two articles should expect the scalar potential to shift in opposite directions.

## The Action in the Fluid Variables

One substitution, in the four-derivative of the phase, and the action is the free one written in the new variable.

$$
\boxed{\;\mathcal L_{\mathrm{fl}}=-\frac{m\rho_{\mathrm{num}}}{2}\Bigl[\sum_{\imath} V_{\Phi,\imath}V_{\Phi,\imath}+c^{2}\Bigr]-\frac{h^{2}}{8\pi^{2}m}\sum_{\imath}(\partial_{\imath} \varrho)^{2},
\qquad
V_{\Phi,\imath}=\frac{\partial_{\imath} S_{\tilde\Xi}-q A_{\imath}}{m}\;}
$$

Compare the two displays: the dust term, the coefficient $m\rho_{\mathrm{num}}/2$, the $c^{2}$, the gradient energy with its $\frac{h^{2}}{4\pi^{2}}/2m$ — every symbol is the free one. What is different is that $V$ is no longer a pure gradient, and the whole of the coupling is in that one word.

The connection is a central element of $\mathbb{B}_\Phi$, so it multiplies the phase factor of the word and commutes past the amplitude. A term built from $\varrho$ and its derivatives therefore cannot contain $\tilde A_\Phi$ at all. In the action that is the second term: **the gradient energy is the unique term the coupling cannot reach, and it is the whole of the quantum sector.**

The action has two arguments and they are the two gauge-invariant data of the fluid. Write them as $\varrho$ and $W_{\imath}=(\partial_{\imath} S_{\tilde\Xi}-q A_{\imath})/m$. Then $\mathcal L_{\mathrm{fl}}=\mathcal L_{\mathrm{fl}}[\varrho,\partial_{\imath} \varrho,W_{\imath}]$, and no other combination of the word's data survives a gauge transformation. The free action's two arguments were $\varrho$ and $S_{\tilde\Xi}$; the charged action's are $\varrho$ and $W$, and the change of variable is the whole of the coupling.

## The Variation: Two of Them

Since $\mathcal L_{\mathrm{fl}}$ depends on $S_{\tilde\Xi}$ only through $V$,

$$
\partial_{\imath}\bigl(\rho_{\mathrm{num}}V_{\Phi,\imath}\bigr)=0,
$$

which is $\partial_{\imath}\tilde J_{\Phi,\imath}=0$ with $\tilde J_\Phi=\rho_{\mathrm{num}}\tilde V_\Phi$. The charge current is $ϙ\tilde J_\Phi$, and its conservation is this equation multiplied by the coupling. The continuity equation has the same form as the free one and refers to a different current, and the difference is what makes the charge density $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$ the source in Gauss's law.

Varying the amplitude gives the free shell verbatim.

$$
\sum_{\imath} V_{\Phi,\imath}V_{\Phi,\imath}=-c^{2}-\frac{2Q_{\mathrm{qnt}}}{m},
\qquad
Q_{\mathrm{qnt}}=-\frac{h^{2}\Box_\Phi \varrho}{8\pi^{2}m\varrho},
$$

because the variation of the gradient term is the free article's and the variation of the dust term is $-\frac{m}{2}$ times the bracket. The right-hand side is coupling-blind, and that is the action's version of the block's statement that the quantum potential is charge-blind: it carries $\varrho$ and its d'Alembertian, and the connection is not in it.

Differentiating the display, with $\tilde P^{\mathrm{mech}}_\Phi=\tilde P_\Phi+ϙ\tilde A_\Phi$,

$$
\partial_{\jmath}\sum_{\imath} p^{\mathrm{mech}}_{\imath} p^{\mathrm{mech}}_{\imath}=-m\partial_{\jmath} Q_{\mathrm{qnt}}
\qquad\Longrightarrow\qquad
\sum_{\imath} V_{\Phi,\imath}\,\partial_{\imath} p^{\mathrm{mech}}_{\jmath}=-\partial_{\jmath} Q_{\mathrm{qnt}}-\frac{ϙ}{m}\sum_{\imath} p^{\mathrm{mech}}_{\imath} F_{\jmath\imath},
$$

the second term being the Lorentz force and the first the quantum force. In three-vector form the spatial slots read

$$
\frac{\mathrm{d}\vec p^{\mathrm{mech}}}{\mathrm{d}t}=-ϙ\bigl(\vec E+\vec v\times\vec B\bigr)-\frac{1}{\gamma}\vec\nabla_\Phi Q_{\mathrm{qnt}},
$$

which is the block's boxed law. The sign is fixed by the substitution's time slot: the energy is $E^{\mathrm{mech}}=E+ϙ a'_t$, so $E=E^{\mathrm{mech}}-ϙ a'_t$ and, with $q=-ϙ$, the potential energy is $q\omicron_{\mathrm{pot}}$. The action fixes the sign in one place, and the block's article fixes it in three.

Two fields, $\varrho$ and $S_{\tilde\Xi}$, or equivalently $\varrho$ and $W$; two equations; no multiplier. The constraint structure is not the coupling's business, and this is the rung at which that is cleanest: the first-order charged fluid has a gauge redundancy and the relativistic one has a redundancy plus a shell, and neither has a subsidiary condition.

## The Constraints the Action Imposes: Gauge Invariance as a Redundancy

Both arguments, $\varrho$ and $W_{\imath}$, are fixed by a gauge transformation, so $\mathcal L_{\mathrm{fl}}$ is fixed by construction and no boundary term arises.

There the action's terms were $-\rho_{\mathrm{num}}\mathcal E$ and $-\rho_{\mathrm{num}}\vec\pi^{2}/2m$, each invariant, but $S$ and $\omicron_{\mathrm{pot}}$ appeared separately and the invariance had to be checked inside each bracket. Here they never appear separately.

What the redundancy costs and what it does not. It removes one of the word's eight parameters from the action's arguments: $\theta_{\mathrm{pha}}$ and $a'_t$ enter only through $W_0$, so the phase and the scalar potential are one degree of freedom between them. It does not remove the current: the constant shift is a global subgroup and its Noether current is the charge current. A redundancy and a symmetry are different objects, and the action shows both at once: the local one is the redundancy that the variables have already absorbed, the global one is the current.

Computing $T_{\imath\jmath}$ with $S_{\tilde\Xi}$ as the variable gives a tensor that moves under a gauge transformation by terms in $\partial\Gamma$; the difference is a total derivative, so the conserved charges are unaffected, and the tensor written in $W$ and $\partial \varrho$ is invariant. The same caution as at the first-order charged rung applies: **the article may call $\mathcal E^{\mathrm{mech}}$ and $\sigma^{Q}$ the fluid's, and must not call the canonical tensor the fluid's without saying which variable it was computed from.**

## The Structural Consequence: The Vorticity Is the Field Strength

With $V_{\imath}=(\partial_{\imath} S_{\tilde\Xi}-q A_{\imath})/m$,

$$
\omega_{\imath\jmath}=\partial_{\imath} V_{\jmath}-\partial_{\jmath} V_{\imath}=\frac{ϙ}{m}F_{\imath\jmath}.
$$

The display is not an equation of motion and not a constraint; it is a computation. The phase's part of the curl vanishes because a gradient's curl does, and the potential's part is the field strength by definition. So the charged flow is rotational for exactly the reason the free flow is irrotational: the velocity is a derivative, and what it is a derivative of has a curl.

At the first order the velocity is $\vec\pi/m$ and its curl is a three-vector, $ϙ\vec B/m$, so the vorticity's rank is two at most. Here the velocity is a four-vector and its curl is a two-form on four dimensions, so the rank is four exactly when $\vec E\cdot\vec B\ne0$ — the block's ladder, and the action's explanation of it: a three-vector potential cannot make a four-dimensional two-form, and a four-vector one can.

A rotational fluid written in Eulerian variables needs the pair $(\alpha_{\mathrm{clb}},\beta_{\mathrm{clb}})$, as [The Clebsch Potentials and the Rank of the Vorticity](the-clebsch-potentials-and-the-rank-of-the-vorticity.html) states. Here the pair's part is played by the connection: the velocity is $\partial S_{\tilde\Xi}/m-q A_{\imath}/m$, one vector standing where the Clebsch form wants two scalars, and its own equation is Maxwell's, which the matter action does not contain. The fluid's rotation is not a new degree of freedom because it is already the field's, and the equality of the rank with the field's rank is the same statement.

## The Structural Consequence: What the Charge Does Not Change, and Why That Is the Article's Main Point

Three objects are exactly the free ones.

*The gradient energy.* $-\frac{h^{2}}{8\pi^{2}m}\sum_{\imath}(\partial_{\imath} \varrho)^{2}$, unchanged, because it carries the amplitude and the connection reaches the phase.

*The quantum potential and the quantum stress.* $Q_{\mathrm{qnt}}$ and $\sigma^{Q}_{ij}$ are functions of $\varrho$ and its derivatives, and the block's identity $\partial_j\sigma^{Q}_{j\eta}=-\rho_{\mathrm{num}}\partial_\eta Q_{\mathrm{qnt}}$ is unchanged with it.

*The mass shell's right-hand side.* $-c^{2}-2Q_{\mathrm{qnt}}/m$ is the free display's, and the coupling's only trace in the shell is that the velocity is mechanical.

So the coupling's entire content is one substitution in one variable, and the action states that in a form no equation-by-equation account can. The block's charged article says the same thing in three sentences — the force becomes the Lorentz force, the quantum force stays, the density is untouched — and the action says it as one line: the variables are $(\varrho,W)$ and only $W$ is charged.

## The Noether Currents: The Charge and the Vorticity

The charge current is $q\rho_{\mathrm{num}}$ and $q\rho_{\mathrm{num}}\vec v$, and the article's *The Vorticity Is the Field Strength* identifies the curl of the velocity with the magnetic field. The two statements are one: the current is what sources the field, and the vorticity is what the field measures.

The energy. The stress is the free scalar fluid's, because the coupling enters only the phase's rate and gradient and the stress is built from $\varrho$ and $S$; the quantum potential's contribution is unchanged. The mass shell is covariantised, the stress is not.

The charge's sign is $q$'s and the density is positive, so a change of sign of $q$ reverses the current and not the density. That is what the article means by the charge not changing the fluid: the fluid's density, velocity field and stress are the neutral ones, and the charge is a label on the current.

## What the Principle Adds and What It Relabels: In the Fluid Chart

Adds. The coupling as a change of variable rather than an added term, with the reason: a central element multiplies the phase factor and cannot reach the amplitude. Gauge invariance as a property of the variables rather than a checked symmetry, and the reason the current survives it. The sign of the Lorentz force fixed at the substitution's time slot. The vorticity's identity as a computation about the variables, and the rank as the field's. And the coupling-blindness of the entire quantum sector as one term of the action.

Does not add. No new equation: continuity and the shell are the block's, and the boxed law is the shell's gradient. No field equation: the action is the matter action and $A_{\imath}$ is given. No statement about the charge's quantization: $ϙ$ is a parameter here and the connection's own dynamics is outside the block. No thermodynamics.

The four charged articles of this layer differ in what the coupling can reach. At the first order it reaches the phase and the velocity and not the gradient energy; here it reaches the velocity and not the gradient energy either; in the spinor case it reaches the frame's transport and not the rotor's norm; in the vector case it reaches the field's own divergence and turns the Lorentz condition into a statement about the charge. The action states each case as which variable is charged, and the four are one sentence: the connection is central, and what is central reaches the phase and the boost's logarithm and cannot reach a modulus.

## What the Principle Adds and What It Relabels: The Fluid Alone

The charge is the phase and nothing else, and the spin-zero fluid is where that is exact. The charged biquaternion fluid carries a frame as well as a density and a phase, and the coupling reaches the scale bracket and the phase bracket and never the frame's. **So the fluid's charge density is the density and its current is the phase's gradient, unchanged by the frame's presence**, and the article's comparison with the charged Schrödinger fluid is the statement that the frame does not enter the charge at all.

The temporal slot of the potential is real and the spatial slot is Hermitian, so in the fluid's own frame the coupling is a longitudinal pressure and a transverse one. The element reading can say this as a type fact and does; the fluid reading says it as a stress, and the article's section on the potential's two slots is where the two statements are put side by side.

A frame that is reconstructed from the element and not fixed by the potential is a free choice in the free fluid; in the charged fluid the potential fixes it, and the article states the condition under which the extremum is unique. That condition is the fluid reading's own contribution, because the element reading has no reason to ask about uniqueness.

No new equation and no new charge. The charge is the Schrödinger fluid's charge, and the article says so in one line rather than deriving it twice.

The nodal exception and the gauge covariance — the second now through the phase's covariant derivative and not through the density.

At the frame's degeneracy, where the potential's extremum is not unique. The article states it once, and that statement is the difference between this fluid and its uncharged companion.

## Open Questions

$\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$ with $\gamma=(E+ϙ a'_t)/(mc^{2})$, so the charge density's sign is the energy's and the action's indefiniteness is inherited. Whether a single functional covers both signs, and whether the two are related by charge conjugation, is the second category's question; the action states the problem and does not solve it.

The chart fails at $\varrho=0$, and here the failure is on a surface that also carries a phase singularity with a flux through it. The block's charged article states the flux quantisation; whether the action requires a boundary term there is open.

## Summary

The action. $\mathcal L_{\mathrm{fl}}=-\frac{m\rho_{\mathrm{num}}}{2}[\sum_{\imath} V_{\Phi,\imath}V_{\Phi,\imath}+c^{2}]-\frac{h^{2}}{8\pi^{2}m}\sum_{\imath}(\partial_{\imath} \varrho)^{2}$, with $V_{\imath}=(\partial_{\imath} S-q A_{\imath})/m$: the free action in a new variable.

The variations. The phase gives $\partial_{\imath}(\rho_{\mathrm{num}}V_{\Phi,\imath})=0$; the amplitude gives the free shell verbatim; the gradient of the second is $\mathrm{d}\vec p^{\mathrm{mech}}/\mathrm{d}t=-ϙ(\vec E+\vec v\times\vec B)-\gamma^{-1}\vec\nabla_\Phi Q_{\mathrm{qnt}}$.

The vorticity. $\omega=ϙ F/m$ is an identity about the variables, so the rotation is the field's and costs no field; the rank is the field strength's.

Gauge invariance. A redundancy already quotiented out, because the action's arguments are $\varrho$ and $W$; the global subgroup supplies the charge current; the canonical stress is gauge dependent and the tensor in $W$ is not.

What the charge changes. One variable. The gradient energy, the quantum potential, the quantum stress and the shell's right-hand side are the free ones.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\varepsilon e_t$ | The word; the free article's, unchanged |
| $ϙ$ | Coupling; minus the electric charge, $q=-ϙ$ |
| $\tilde A_\Phi=i a'_t e_t+\vec A$ | The connection; $a'_t=\omicron_{\mathrm{pot}}$ |
| $S_{\tilde\Xi}=\frac{h}{2\pi}\theta_{\mathrm{pha}}$ | Phase; gauge dependent |
| $W_{\imath}=(\partial_{\imath} S_{\tilde\Xi}-q A_{\imath})/m$ | Mechanical four-velocity; the action's second argument |
| $\tilde P^{\mathrm{mech}}_\Phi=\tilde P_\Phi+ϙ\tilde A_\Phi$ | Mechanical momentum; $m\tilde V_\Phi$ |
| $\rho_{\mathrm{num}}=\varrho^{2}$ | Proper density; gauge invariant |
| $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$ | Charge density; the current's temporal component over $c$ |
| $Q_{\mathrm{qnt}}=-\frac{h^{2}}{4\pi^{2}}\Box_\Phi \varrho/(2m\varrho)$ | Quantum potential; coupling-blind |
| $\mathcal E_{\mathrm{grad}}=-\frac{h^{2}}{8\pi^{2}m}\int\sum_{\imath}(\partial_{\imath} \varrho)^{2}$ | Gradient energy; coupling-blind |
| $F_{\imath\jmath}=\partial_{\imath} A_{\jmath}-\partial_{\jmath} A_{\imath}$ | Field strength; $m\omega=ϙ F$ |
| $\vec E=-\vec\nabla_\Phi\omicron_{\mathrm{pot}}-\partial_{t'}\vec A$, $\vec B=\vec\nabla_\Phi\times\vec A$ | Field strengths |
| $\gamma=E/(mc^{2})$ | Signed Lorentz factor |
| $\nu_m=\frac{mc}{h}$ | Mass wave number |
| $\mathcal L_{\mathrm{fl}}$ | The Lagrangian density in the fluid variables |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part |

## Further Reading

- Erwin Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1926) 322–326, for the fluid pair before a connection is added.
- Louis de Broglie, *La mécanique ondulatoire du photon et la théorie quantique des champs* (Gauthier-Villars, 1949), for the relativistic charged fluid and the mechanical velocity's role.
- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 2–35, part I, for the covariant current and the vorticity of a charged relativistic flow.
- Fritz London, "Zur Theorie der Supraleitung," *Zeitschrift für Physik* **37** (1926) 915–925, for the phase's gauge behaviour and the flux it quantises.
- Clifford Truesdell and Richard Toupin, "The classical field theories," in *Handbuch der Physik* III/1 (Springer, 1960), for the Clebsch representation of a rotational velocity and the rank it carries.
- The companion articles: [The Lagrangian and the Coupled Klein–Gordon Equation in Polar Variables](the-lagrangian-and-the-coupled-klein-gordon-equation-in-polar-variables.html), the same action in the polar chart; [The Charged Spin-Zero Fluid](the-charged-spin-zero-fluid.html), the equations varied here and the boxed Lorentz law; [The Lagrangian and the Spin-Zero Fluid](the-lagrangian-and-the-spin-zero-fluid.html), the $ϙ=0$ case with the indefinite gradient energy; [The Lagrangian and the Charged Schrödinger Fluid](the-lagrangian-and-the-charged-schrodinger-fluid.html), the rung below, where the same substitution has no shell to meet; and [The Clebsch Potentials and the Rank of the Vorticity](the-clebsch-potentials-and-the-rank-of-the-vorticity.html), for the cost the connection pays for free.
