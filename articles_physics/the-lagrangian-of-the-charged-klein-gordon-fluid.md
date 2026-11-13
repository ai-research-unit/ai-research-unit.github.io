# The Lagrangian of the Charged Klein–Gordon Fluid

## Introduction

**At this rung the coupling adds no term to the action; it changes one variable.** The two terms of [The Lagrangian of the Klein–Gordon Fluid](the-lagrangian-of-the-klein-gordon-fluid.html) survive intact, and the only change is that the four-velocity is the mechanical one, $\tilde V_\Phi=\tilde P^{\mathrm{mech}}_\Phi/m$ with $\tilde P^{\mathrm{mech}}_\Phi=\tilde P_\Phi+ϙ\tilde A_\Phi$. That is the minimal coupling stated covariantly, and it is why the density is untouched: **a substitution inside one square cannot reach a term that carries no phase.**

**Three results.**

*First, the action is written in gauge-invariant variables, so its gauge invariance is not a symmetry but a redundancy already quotiented out.* The free action's phase $S_{\tilde\Xi}$ and the potentials appear only in the combination $\partial_\mu S_{\tilde\Xi}+ϙ A_\mu$. The action is therefore a functional of $r$ and that combination alone, and no shift of either moves it. At the first-order rung the invariance had to be checked term by term inside two brackets; here the bracket is one object and the checking is a definition.

*Second, the mass shell is unchanged in form and the whole of the coupling is in the velocity.* The variation of the density returns $\sum_\mu V_{\Phi,\mu}V_{\Phi,\mu}=-c^{2}-2Q_{\mathrm{qnt}}/m$, the free display verbatim, with $V$ the mechanical velocity. The connection's spatial part enters the velocity and not the shell: the shell's right-hand side carries the density and the d'Alembertian, and the coupling cannot reach either.

*Third, the vorticity is the field strength, and the action says why it costs nothing.* The velocity's curl is the curl of a potential, so $\omega_{\mu\nu}=ϙ F_{\mu\nu}/m$ is an identity about the variables and not an equation about the flow. In the Clebsch language the connection supplies the second and third potentials, and their rank is the field's.

**Position in the block.** This is the variational companion of [The Charged Klein–Gordon Fluid](the-charged-klein-gordon-fluid.html) and the fourth of the eight articles of this layer. It is the first in which the action's variables are gauge invariant by construction, and the first in which the fluid's vorticity is not a property of the flow.

**Conventions.** Those of the free companion, with the connection: $ϙ$ is the coupling, $q=-ϙ$ the electric charge; $\tilde A_\Phi=i a'_t e_t+\sum_\eta A_\eta\vec e_\eta$ with $a'_t=\varphi$; the covariant derivative is $\partial_\mu+\frac{iϙ}{\hbar}A_\mu$; $\tilde P^{\mathrm{mech}}_\Phi=\tilde P_\Phi+ϙ\tilde A_\Phi$; $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$, $\vec E=-\nabla\varphi-\partial_{t'}\vec A$, $\vec B=\nabla\times\vec A$. A gauge transformation is $S_{\tilde\Xi}\mapsto S_{\tilde\Xi}+ϙ\Gamma$ together with $A_\mu\mapsto A_\mu-\partial_\mu\Gamma$, that is $\theta_{\mathrm{pha}}\mapsto\theta_{\mathrm{pha}}+ϙ\Gamma/\hbar$. The temporal slot's sign is the one that looks odd and is not: the invariant is $W_0=(\partial_{t'}S_{\tilde\Xi}+ϙ a'_t)/m$, so the scalar potential moves against the phase and not with it, where the first-order rung's bracket $\partial_{t'}S-ϙ\varphi$ carries the opposite sign on the phase and the potential moves with it. **The two rungs differ in the sign of one bracket and in nothing else**, and a reader moving between the two articles should expect the scalar potential to shift in opposite directions.

## The Action in the Fluid Variables

**One substitution, in the four-derivative of the phase, and the action is the free one written in the new variable.**

$$
\boxed{\;\mathcal L_{\mathrm{fl}}=-\frac{m\rho_{\mathrm{num}}}{2}\Bigl[\sum_\mu V_{\Phi,\mu}V_{\Phi,\mu}+c^{2}\Bigr]-\frac{\hbar^{2}}{2m}\sum_\mu(\partial_\mu r)^{2},
\qquad
V_{\Phi,\mu}=\frac{\partial_\mu S_{\tilde\Xi}+ϙ A_\mu}{m}\;}
$$

**The structure is the free article's and the identity is exact.** Compare the two displays: the dust term, the coefficient $m\rho_{\mathrm{num}}/2$, the $c^{2}$, the gradient energy with its $\hbar^{2}/2m$ — every symbol is the free one. What is different is that $V$ is no longer a pure gradient, and the whole of the coupling is in that one word.

**The coupling could not have entered anywhere else, and the reason is the type argument in its shortest form.** The connection is a central element of $\mathbb{B}_\Phi$, so it multiplies the phase factor of the word and commutes past the amplitude. A term built from $r$ and its derivatives therefore cannot contain $\tilde A_\Phi$ at all. In the action that is the second term: **the gradient energy is the unique term the coupling cannot reach, and it is the whole of the quantum sector.**

**The action has two arguments and they are the two gauge-invariant data of the fluid.** Write them as $r$ and $W_\mu=(\partial_\mu S_{\tilde\Xi}+ϙ A_\mu)/m$. Then $\mathcal L_{\mathrm{fl}}=\mathcal L_{\mathrm{fl}}[r,\partial_\mu r,W_\mu]$, and no other combination of the word's data survives a gauge transformation. **The free action's two arguments were $r$ and $S_{\tilde\Xi}$; the charged action's are $r$ and $W$**, and the change of variable is the whole of the coupling.

## The Two Variations

**Varying the phase gives continuity of the mechanical current.** Since $\mathcal L_{\mathrm{fl}}$ depends on $S_{\tilde\Xi}$ only through $V$,

$$
\partial_\mu\bigl(\rho_{\mathrm{num}}V_{\Phi,\mu}\bigr)=0,
$$

which is $\partial_\mu\tilde J_{\Phi,\mu}=0$ with $\tilde J_\Phi=\rho_{\mathrm{num}}\tilde V_\Phi$. The charge current is $ϙ\tilde J_\Phi$, and its conservation is this equation multiplied by the coupling. **The continuity equation has the same form as the free one and refers to a different current**, and the difference is what makes the charge density $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$ the source in Gauss's law.

**Varying the amplitude gives the free shell verbatim.**

$$
\sum_\mu V_{\Phi,\mu}V_{\Phi,\mu}=-c^{2}-\frac{2Q_{\mathrm{qnt}}}{m},
\qquad
Q_{\mathrm{qnt}}=-\frac{\hbar^{2}\Box_\Phi r}{2mr},
$$

because the variation of the gradient term is the free article's and the variation of the dust term is $-\frac{m}{2}$ times the bracket. **The right-hand side is coupling-blind**, and that is the action's version of the block's statement that the quantum potential is charge-blind: it carries $r$ and its d'Alembertian, and the connection is not in it.

**The acceleration law is the shell's gradient and carries the Lorentz force.** Differentiating the display, with $\tilde P^{\mathrm{mech}}_\Phi=\tilde P_\Phi+ϙ\tilde A_\Phi$,

$$
\partial_\nu\sum_\mu p^{\mathrm{mech}}_\mu p^{\mathrm{mech}}_\mu=-m\partial_\nu Q_{\mathrm{qnt}}
\qquad\Longrightarrow\qquad
\sum_\mu V_{\Phi,\mu}\,\partial_\mu p^{\mathrm{mech}}_\nu=-\partial_\nu Q_{\mathrm{qnt}}-\frac{ϙ}{m}\sum_\mu p^{\mathrm{mech}}_\mu F_{\nu\mu},
$$

the second term being the Lorentz force and the first the quantum force. In three-vector form the spatial slots read

$$
\frac{\mathrm{d}\vec p^{\mathrm{mech}}}{\mathrm{d}t}=-ϙ\bigl(\vec E+\vec v\times\vec B\bigr)-\frac{1}{\gamma}\nabla Q_{\mathrm{qnt}},
$$

which is the block's boxed law. **The sign is fixed by the substitution's time slot**: the energy is $E^{\mathrm{mech}}=E+ϙ a'_t$, so $E=E^{\mathrm{mech}}-ϙ a'_t$ and, with $q=-ϙ$, the potential energy is $q\varphi$. The action fixes the sign in one place, and the block's article fixes it in three.

**The count is two and two, as at the free rung, and the coupling does not change it.** Two fields, $r$ and $S_{\tilde\Xi}$, or equivalently $r$ and $W$; two equations; no multiplier. The constraint structure is not the coupling's business, and this is the rung at which that is cleanest: **the first-order charged fluid has a gauge redundancy and the relativistic one has a redundancy plus a shell, and neither has a subsidiary condition.**

## The Vorticity Is the Field Strength

**The velocity's curl is the curl of a potential, so the vorticity is an identity about the variables.** With $V_\mu=(\partial_\mu S_{\tilde\Xi}+ϙ A_\mu)/m$,

$$
\omega_{\mu\nu}=\partial_\mu V_\nu-\partial_\nu V_\mu=\frac{ϙ}{m}F_{\mu\nu}.
$$

**The display is not an equation of motion and not a constraint; it is a computation.** The phase's part of the curl vanishes because a gradient's curl does, and the potential's part is the field strength by definition. So the charged flow is rotational for exactly the reason the free flow is irrotational: the velocity is a derivative, and what it is a derivative of has a curl.

**This is the sharpest difference between the two charged rungs.** At the first order the velocity is $\vec\pi/m$ and its curl is a three-vector, $ϙ\vec B/m$, so the vorticity's rank is two at most. Here the velocity is a four-vector and its curl is a two-form on four dimensions, so the rank is four exactly when $\vec E\cdot\vec B\ne0$ — the block's ladder, and the action's explanation of it: **a three-vector potential cannot make a four-dimensional two-form, and a four-vector one can.**

**The Clebsch cost is the field's and not the fluid's.** A rotational fluid written in Eulerian variables needs the pair $(\alpha_{\mathrm{clb}},\beta_{\mathrm{clb}})$, as [The Clebsch Potentials and the Rank of the Vorticity](the-clebsch-potentials-and-the-rank-of-the-vorticity.html) states. Here the pair's part is played by the connection: the velocity is $\partial S_{\tilde\Xi}/m+ϙ A_\mu/m$, one vector standing where the Clebsch form wants two scalars, and its own equation is Maxwell's, which the matter action does not contain. **The fluid's rotation is not a new degree of freedom because it is already the field's**, and the equality of the rank with the field's rank is the same statement.

## Gauge Invariance as a Redundancy

**The action is written in invariant variables, and that is stronger than being invariant.** Both arguments, $r$ and $W_\mu$, are fixed by a gauge transformation, so $\mathcal L_{\mathrm{fl}}$ is fixed by construction and no boundary term arises.

**The contrast with the first-order rung is instructive and it is not a difference of degree.** There the action's terms were $-\rho_{\mathrm{num}}\mathcal E$ and $-\rho_{\mathrm{num}}\vec\pi^{2}/2m$, each invariant, but $S$ and $\varphi$ appeared separately and the invariance had to be checked inside each bracket. Here they never appear separately.

**What the redundancy costs and what it does not.** It removes one of the word's eight parameters from the action's arguments: $\theta_{\mathrm{pha}}$ and $a'_t$ enter only through $W_0$, so the phase and the scalar potential are one degree of freedom between them. It does not remove the current: the constant shift is a global subgroup and its Noether current is the charge current. **A redundancy and a symmetry are different objects, and the action shows both at once**: the local one is the redundancy that the variables have already absorbed, the global one is the current.

**The canonical stress is gauge dependent and the physical one is not.** Computing $T_{\mu\nu}$ with $S_{\tilde\Xi}$ as the variable gives a tensor that moves under a gauge transformation by terms in $\partial\Gamma$; the difference is a total derivative, so the conserved charges are unaffected, and the tensor written in $W$ and $\partial r$ is invariant. The same caution as at the first-order charged rung applies: **the article may call $\mathcal E^{\mathrm{mech}}$ and $\sigma^{Q}$ the fluid's, and must not call the canonical tensor the fluid's without saying which variable it was computed from.**

## What the Charge Does Not Change, and Why That Is the Article's Main Point

**Three objects are exactly the free ones.**

*The gradient energy.* $-\frac{\hbar^{2}}{2m}\sum_\mu(\partial_\mu r)^{2}$, unchanged, because it carries the amplitude and the connection reaches the phase.

*The quantum potential and the quantum stress.* $Q_{\mathrm{qnt}}$ and $\sigma^{Q}_{ij}$ are functions of $r$ and its derivatives, and the block's identity $\partial_j\sigma^{Q}_{j\eta}=-\rho_{\mathrm{num}}\partial_\eta Q_{\mathrm{qnt}}$ is unchanged with it.

*The mass shell's right-hand side.* $-c^{2}-2Q_{\mathrm{qnt}}/m$ is the free display's, and the coupling's only trace in the shell is that the velocity is mechanical.

**So the coupling's entire content is one substitution in one variable, and the action states that in a form no equation-by-equation account can.** The block's charged article says the same thing in three sentences — the force becomes the Lorentz force, the quantum force stays, the density is untouched — and the action says it as one line: the variables are $(r,W)$ and only $W$ is charged.

## What the Fluid Variational Principle Adds and Does Not Add

**Adds.** The coupling as a change of variable rather than an added term, with the reason: a central element multiplies the phase factor and cannot reach the amplitude. Gauge invariance as a property of the variables rather than a checked symmetry, and the reason the current survives it. The sign of the Lorentz force fixed at the substitution's time slot. The vorticity's identity as a computation about the variables, and the rank as the field's. And the coupling-blindness of the entire quantum sector as one term of the action.

**Does not add.** No new equation: continuity and the shell are the block's, and the boxed law is the shell's gradient. No field equation: the action is the matter action and $A_\mu$ is given. No statement about the charge's quantization: $ϙ$ is a parameter here and the connection's own dynamics is outside the block. No thermodynamics.

**The comparison worth recording.** The four charged articles of this layer differ in what the coupling can reach. At the first order it reaches the phase and the velocity and not the gradient energy; here it reaches the velocity and not the gradient energy either; in the spinor case it reaches the frame's transport and not the rotor's norm; in the vector case it reaches the field's own divergence and turns the Lorentz condition into a statement about the charge. **The action states each case as which variable is charged**, and the four are one sentence: the connection is central, and what is central reaches the phase and the boost's logarithm and cannot reach a modulus.

## Open Questions

1. **The two signs of the charge and the two sheets.** $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$ with $\gamma=(E+ϙ a'_t)/(mc^{2})$, so the charge density's sign is the energy's, and the action's indefiniteness is inherited. Whether a single functional covers both signs, and whether the two are related by charge conjugation, is the second category's question; the action states the problem and does not solve it.

2. **The boundary at a nodal surface.** As in the free companion, the chart fails at $r=0$, and here the failure is on a surface that also carries a phase singularity with a flux through it. The block's charged article states the flux quantisation; whether the action requires a boundary term there is open.

## Summary

**The action.** $\mathcal L_{\mathrm{fl}}=-\frac{m\rho_{\mathrm{num}}}{2}[\sum_\mu V_{\Phi,\mu}V_{\Phi,\mu}+c^{2}]-\frac{\hbar^{2}}{2m}\sum_\mu(\partial_\mu r)^{2}$, with $V_\mu=(\partial_\mu S+ϙ A_\mu)/m$: the free action in a new variable.

**The variations.** The phase gives $\partial_\mu(\rho_{\mathrm{num}}V_{\Phi,\mu})=0$; the amplitude gives the free shell verbatim; the gradient of the second is $\mathrm{d}\vec p^{\mathrm{mech}}/\mathrm{d}t=-ϙ(\vec E+\vec v\times\vec B)-\gamma^{-1}\nabla Q_{\mathrm{qnt}}$.

**The vorticity.** $\omega=ϙ F/m$ is an identity about the variables, so the rotation is the field's and costs no field; the rank is the field strength's.

**Gauge invariance.** A redundancy already quotiented out, because the action's arguments are $r$ and $W$; the global subgroup supplies the charge current; the canonical stress is gauge dependent and the tensor in $W$ is not.

**What the charge changes.** One variable. The gradient energy, the quantum potential, the quantum stress and the shell's right-hand side are the free ones.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon e_t$ | The word; the free article's, unchanged |
| $ϙ$ | Coupling; minus the electric charge, $q=-ϙ$ |
| $\tilde A_\Phi=i a'_t e_t+\vec A$ | The connection; $a'_t=\varphi$ |
| $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$ | Phase; gauge dependent |
| $W_\mu=(\partial_\mu S_{\tilde\Xi}+ϙ A_\mu)/m$ | Mechanical four-velocity; the action's second argument |
| $\tilde P^{\mathrm{mech}}_\Phi=\tilde P_\Phi+ϙ\tilde A_\Phi$ | Mechanical momentum; $m\tilde V_\Phi$ |
| $\rho_{\mathrm{num}}=r^{2}$ | Proper density; gauge invariant |
| $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$ | Charge density; the current's temporal component over $c$ |
| $Q_{\mathrm{qnt}}=-\hbar^{2}\Box_\Phi r/(2mr)$ | Quantum potential; coupling-blind |
| $\mathcal E_{\mathrm{grad}}=-\frac{\hbar^{2}}{2m}\int\sum_\mu(\partial_\mu r)^{2}$ | Gradient energy; coupling-blind |
| $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$ | Field strength; $m\omega=ϙ F$ |
| $\vec E=-\nabla\varphi-\partial_{t'}\vec A$, $\vec B=\nabla\times\vec A$ | Field strengths |
| $\gamma=E/(mc^{2})$ | Signed Lorentz factor |
| $k_m=mc/\hbar$ | Mass wave number |
| $\mathcal L_{\mathrm{fl}}$ | The Lagrangian density in the fluid variables |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part |

## Further Reading

- Erwin Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1926) 322–326, for the fluid pair before a connection is added.
- Louis de Broglie, *La mécanique ondulatoire du photon et la théorie quantique des champs* (Gauthier-Villars, 1949), for the relativistic charged fluid and the mechanical velocity's role.
- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 2–35, part I, for the covariant current and the vorticity of a charged relativistic flow.
- Fritz London, "Zur Theorie der Supraleitung," *Zeitschrift für Physik* **37** (1926) 915–925, for the phase's gauge behaviour and the flux it quantises.
- Clifford Truesdell and Richard Toupin, "The classical field theories," in *Handbuch der Physik* III/1 (Springer, 1960), for the Clebsch representation of a rotational velocity and the rank it carries.
- The companion articles: [The Variational Principle and the Coupled Klein–Gordon Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-coupled-klein-gordon-equation-in-biquaternionic-polar-variables.html), the same action in the polar chart; [The Charged Klein–Gordon Fluid](the-charged-klein-gordon-fluid.html), the equations varied here and the boxed Lorentz law; [The Lagrangian of the Klein–Gordon Fluid](the-lagrangian-of-the-klein-gordon-fluid.html), the $ϙ=0$ case with the indefinite gradient energy; [The Lagrangian of the Charged Schrödinger Fluid](the-lagrangian-of-the-charged-schrodinger-fluid.html), the rung below, where the same substitution has no shell to meet; and [The Clebsch Potentials and the Rank of the Vorticity](the-clebsch-potentials-and-the-rank-of-the-vorticity.html), for the cost the connection pays for free.
