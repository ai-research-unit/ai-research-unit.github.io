# The Lagrangian of the Charged Spin Fluid

## Introduction

**The connection is a central element, and a central element decomposes into two of the four brackets and none of the others.** That single fact is the whole of the charged spin fluid's structure — the force without a torque, the norms that survive, the vorticity that stays the frame's — and the action is the place where it is one sentence instead of five results.

**Three results.**

*First, the coupling's decomposition fixes its reach.* The connection is Hermitian, so in the bracket decomposition it contributes a central imaginary in its time slot and a Hermitian element in its spatial slots. Those are the phase's bracket and the boost's. It contributes nothing to the real scalar, which is the scale's, and nothing to the real vector, which is the rotor's. **The density and the spin are therefore outside the coupling's reach by type, and not by cancellation.**

*Second, the same decomposition is why there is no torque.* A torque would have to enter the rotor's bracket; the connection has no real-vector part, so it cannot. The action states this as the absence of a term, and [The Charged Spin Fluid](the-charged-spin-fluid.html) states it as a computation: the force equation gains $-ϙ F^{\mu\nu}J_\nu$ and the spin's transport law gains nothing.

*Third, every norm in the spinor case survives, and the reason is that a connection transports and does not measure.* The velocity is a unit element's square, so its norm is fixed by the frame and no added connection can move it. At the scalar rung the velocity is a gradient, and there the shell's right-hand side carries the quantum potential; here it carries nothing.

**Position in the block.** This is the variational companion of [The Charged Spin Fluid](the-charged-spin-fluid.html) and the sixth of the eight articles of this layer. It is the article in which the coupling changes the least: the canonical table of [The Lagrangian of the Spin Fluid](the-lagrangian-of-the-spin-fluid.html) is reproduced line for line.

**Conventions.** Those of the free companion, with $\tilde A_\Phi=i a'_t e_t+\sum_\eta A_\eta\vec e_\eta\in\mathbb{B}_\Phi$, covariant derivative $\partial_\mu+\frac{iϙ}{\hbar}A_\mu$ acting from the left, $ϙ$ the coupling and $q=-ϙ$ the electric charge. The four brackets of $\tilde\Xi^{-1}\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi$ are the real scalar (the scale's), the central imaginary (the phase's), the Hermitian element (the boost's) and the real vector (the rotor's). Gauge transformations are central: $\tilde\Xi\mapsto\tilde\Xi\lambda$ with $\lambda=\exp(iϙ\Gamma/\hbar)\in\mathbb{C}$, $A_\mu\mapsto A_\mu-\partial_\mu\Gamma$.

## The Coupling in the Brackets

**The word's logarithmic derivative splits into four objects of four types, and the connection is one object of two.** Since $\tilde A_\Phi\in\mathbb{B}_\Phi$ is Hermitian,

$$
\frac{iϙ}{\hbar}\tilde A_\Phi=\frac{iϙ}{\hbar}a'_t\,e_t+\frac{iϙ}{\hbar}\vec A,
$$

and the first term is central imaginary while the second is Hermitian with a real vector coefficient. In the bracket decomposition of $\tilde\Xi^{-1}\tilde\nabla_{\mathrm{gco},\mu}\tilde\Xi$,

| bracket | type | what the free bracket reads | what the connection adds |
| --- | --- | --- | --- |
| scale | real scalar | $\partial_\mu\ln r$ | $0$ |
| phase | central imaginary | $\partial_\mu\theta_{\mathrm{pha}}$ | $-ϙ a'_t/\hbar$ in the time slot |
| boost | Hermitian | the rapidity's connection | $ϙ\vec A/\hbar$ in the spatial slots |
| rotor | real vector | $\vec\omega_{\mathrm r}$'s connection | $0$ |

**The two zeros are the article's first result and they are structural.** The scale is real and the connection has no real scalar part; the rotor is a real vector and the connection has no real vector part. **No cancellation occurs and no small parameter is used**: the two brackets the coupling cannot reach are the two factors of the word that carry the fluid's density and its spin.

**This is the type argument of the block's charged articles, in its most economical form.** The scalar charged articles state it as one sentence about a central element reaching the phase and the boost and not the scale and the rotor; here it is a table whose two zeros are read off the decomposition of $\tilde A_\Phi$.

## The Kinetic Term and the Two Covariant Rates

**The free kinetic term is a charge density times two rates, and the coupling makes both of them covariant.**

$$
\mathcal L_{\mathrm{kin}}=\hbar c\,\rho_{\mathrm{chg}}\bigl(\dot\theta_{\mathrm{pha}}-\beta\,\hat n_{\mathrm{rot}}\cdot\vec\omega_{\mathrm r}\bigr)
\;\longrightarrow\;
\mathcal L_{\mathrm{kin}}^{\mathrm{gco}}=\hbar c\,\rho_{\mathrm{chg}}\bigl(\mathcal R_{\mathrm{pha}}-\beta\,\mathcal R_{\mathrm{rpd}}\bigr),
$$

**The two covariant rates are the time slots of the phase's bracket and of the boost's.** The first is the gauge-invariant phase rate, $\dot\theta_{\mathrm{pha}}-ϙ a'_t/\hbar$, which is the free article's $\mathcal E$ up to the mass; the second is the rapidity's rate with the vector potential's component along the boost axis added, and it is what makes the velocity the mechanical one.

**The weight $\beta$ is untouched, and that is the sharpest form of "no torque".** If the coupling had a rotor-bracket component, the second rate would acquire a term independent of $\beta$ and the spin would be canonically visible at rest. It has none, so the weight stays $\beta$ and the rest frame stays spinless. **The statement "the coupling adds a force and not a torque" is, in the action, the statement that $\beta$ is not modified.**

**The sign and the normalisation are the scalar charged article's.** The coupling enters the time slot with the same sign there and here, because the substitution is the same substitution; the difference is that here it also enters the boost's bracket, and there it entered the velocity's gradient. **The Lorentz force's sign is fixed once for both rungs**, and the sign of the second rate's modification is what the block's $\langle\tilde V_\Phi\rangle_\natural=-c^{2}$ requires.

## The Canonical Table Is Unchanged

**Four statements, and the coupling moves none of them.**

| momentum | value | changed by the coupling? |
| --- | --- | --- |
| $p_{\theta_{\mathrm{pha}}}$ | $\hbar c\,\rho_{\mathrm{chg}}$ | no |
| $\vec p_{\mathrm{spin}}$ | $-\hbar c\,\rho_{\mathrm{chg}}\beta\,\hat n_{\mathrm{rot}}$ | no |
| $p_{\theta_{\mathrm{rpd}}}$ | $0$ | no |
| $p_{u_{\mathrm b}}$, $p_{r}$ | $0$ | no |

**The invariance of the table is "no torque" stated canonically.** A torque is a change in the spin's momentum; the spin's momentum is a closed form in the rotor and the boost, and the connection is in neither, so the form is unchanged. The force is a change in the velocity's momentum, and the velocity is not canonical here at all: its momentum is zero before and after. **The asymmetry is exact: the coupling moves the one quantity that has no momentum and leaves alone the two that have.**

**What the table says about the block's claim of a surviving normalisation.** $\langle\tilde V_\Phi\rangle_\natural=-c^{2}$ for every field, and the table gives the reason: the velocity is built from the boost element, the boost's bracket is a connection, and a connection does not change a norm. **A connection changes transports; a norm is not a transport.** The free companion's normalisation is therefore not "surviving" anything — nothing was ever at risk.

**And the contrast with the scalar rung is exact.** There the velocity is $\tilde P^{\mathrm{mech}}/m$, a four-vector whose norm the mass shell fixes, and the shell's right-hand side carries $-2Q_{\mathrm{qnt}}/m$; the coupling changes the velocity and not the shell, so the norm moves with the field through the quantum potential. Here the velocity is a unit's square and no term is available to move it. **One rung has a norm that measures the state; the other has a norm that is a property of the frame.**

## Norms Survive and the Vorticity Stays the Frame's

**The two rungs differ in what kind of object the velocity is, and every downstream difference follows.**

*At the scalar rung the velocity is a gradient.* $\tilde V_\Phi=\tilde P^{\mathrm{mech}}_\Phi/m$ with $\tilde P_\Phi=\tilde\nabla_\Phi S_{\tilde\Xi}$, so the velocity is the covariant derivative of a function, and its curl is the field strength: $\omega=ϙ F/m$. The coupling makes the flow rotational, and the rotation is the field's.

*At the spinor rung the velocity is a square.* $\tilde V_\Phi=ic\tilde U_{\Psi,\mathrm b}^{-2}$, the square of a unit element read through the quaternionic norm, so it is a function of the boost factor alone. **A square of a unit is not the derivative of anything** — the block's article states this as the reason the Dirac velocity does not come from a potential — and adding a connection to a bracket does not turn a square into a gradient.

**Hence the vorticity stays the frame's.** [The Charged Spin Fluid](the-charged-spin-fluid.html) finds that the vorticity is the frame's and that the coupling does not put the field strength into it, in contrast to the scalar case's $\mathrm{d}V=ϙ F/m$. The action's version: the connection enters the boost's bracket, the boost's bracket is not the velocity's curl, and the velocity's curl is the antisymmetrised derivative of a square, which is a frame quantity.

**The consequence for what the fluid can and cannot do is worth stating.** The charged scalar fluid's rotation is a field-theoretic input that costs no field; the charged spin fluid's rotation is a property of its own frame, so the field cannot supply it and the fluid cannot be made rotational by turning on a field. **The two charged fluids are therefore not the same fluid with different spins**: one has its vorticity sourced from outside and the other has it sourced from within.

## Gauge Invariance Is Exact Because the Group Is Central

**The invariance is one line and it rests on the gauge element's being central.** With $\tilde\Xi\mapsto\tilde\Xi\lambda$ and $\lambda\in\mathbb{C}$ central,

$$
\tilde\Xi^{-1}\bigl(\partial_\mu+\tfrac{iϙ}{\hbar}A_\mu\bigr)\tilde\Xi
\longmapsto
\tilde\Xi^{-1}\bigl(\partial_\mu+\tfrac{iϙ}{\hbar}A_\mu\bigr)\tilde\Xi+\lambda^{-1}\partial_\mu\lambda,
$$

and $\lambda^{-1}\partial_\mu\lambda=iϙ\partial_\mu\Gamma/\hbar$ is central, so it cancels against the transformed connection. **The frame's brackets do not see the shift at all**, because it is added on the left of the element and the frame's factors are to the right, and because a central element commutes past every one of them.

**This is why the invariance is exact here and needs no boundary term, and it is also why it cannot reach the spin.** A gauge transformation is a multiplication of the word by a central factor; the word's factors are the phase's and the frame's; a central multiplication can be absorbed into the phase's factor — which is what a phase shift is — and cannot be absorbed into the frame's, because the frame's factors are not central. So the shift is entirely the phase's, and the boost's bracket's apparent change is the connection's cancellation. **The coupling's reach and the gauge group's reach coincide, and both are the central direction of the algebra.**

**The current and the stress follow as at the scalar charged rung.** The global subgroup supplies the charge current $ϙ\tilde J_\Phi$; translation invariance supplies the stress, whose divergence is $-ϙ F^{\mu\nu}J_\nu$ plus the free spin term; and the canonical tensor computed with the phase as the variable is gauge dependent by a total derivative, while the tensor written in the frame's brackets is not.

## What the Fluid Variational Principle Adds and Does Not Add

**Adds.** The coupling's reach as a table with two structural zeros, and hence the type argument in one line. "No torque" as the invariance of the weight $\beta$ rather than as a computation. The canonical table's invariance, which is the same statement read canonically. The surviving normalisation as the statement that a connection transports and does not measure. The gauge invariance's exactness as the centrality of the gauge group rather than as a checked cancellation. And the contrast with the scalar rung as a difference in the kind of object the velocity is: a gradient there, a square here.

**Does not add.** No new equation: the parent's, with the polar companion's Euler–Lagrange equations as its components. No closure: the four primary constraints remain second class and the Dirac bracket remains open. No vorticity, for the particle setting's structural reason given in the free companion. No mass without a declared direction: the coupling does not supply one, and a connection could not, since a direction is not a transport. No thermodynamics.

**The one asymmetry within the layer.** Of the eight articles, this is the one in which the coupling changes nothing that the canonical structure can see. That is not an accident of the formalism: the coupling's image is the phase and the boost, and the canonical structure's non-trivial rows are the phase's and the spin's. **The one row the coupling could have moved is the spin's, and the type argument is exactly what forbids it.**

## Open Questions

1. **The bracket with the connection.** Whether the Dirac bracket closes when the constraints are computed with the covariant one-form — that is, whether the connection's presence changes the class of the four constraints — is not settled. The polar companion's computation is for the free field.

2. **The operator setting.** As in the free companion, the frame's spatial gradients are where the vorticity lives, and the article does not compute them. Whether the connection's spatial part changes their closed form by more than a substitution is open.

3. **The mass and the direction.** One declared direction, as in the free companion. Whether the coupling's phase freedom can absorb it in some naming of the parts is not settled and the article does not claim it can.

## Summary

**The coupling's reach.** Central imaginary in the time slot, Hermitian in the spatial ones: the phase's bracket and the boost's. Nothing in the scale's and nothing in the rotor's.

**The kinetic term.** Two rates, both made covariant; the weight $\beta$ unchanged, which is "no torque" in the action.

**The canonical table.** Unchanged line for line: $p_{\theta_{\mathrm{pha}}}=\hbar c\rho_{\mathrm{chg}}$, $\vec p_{\mathrm{spin}}=-\hbar c\rho_{\mathrm{chg}}\beta\hat n_{\mathrm{rot}}$, the rest zero.

**The norms.** Every norm survives, because a connection transports and does not measure; the scalar rung's shell is a norm that measures, and it is the exception.

**The vorticity.** The frame's and not the field's, because the velocity is a unit's square and not a gradient. The two charged rungs differ in the kind of object the velocity is.

**Gauge invariance.** Exact, and exact because the gauge group is central and therefore commutes with the frame.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The word, four factors |
| $ϙ$ | Coupling; minus the electric charge |
| $\tilde A_\Phi=i a'_t e_t+\vec A$ | The connection; Hermitian, hence central-imaginary in time and Hermitian in space |
| $\lambda=\exp(iϙ\Gamma/\hbar)$ | The gauge element; central, hence commuting with the frame |
| $\tilde V_\Phi=ic\tilde U_{\Psi,\mathrm b}^{-2}$ | The velocity; a unit's square, norm $-c^{2}$ for every field |
| $\rho_{\mathrm{num}}=r^{2}$, $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$ | Proper and charge densities |
| $\beta=\tanh\theta_{\mathrm{rpd}}$ | The spin's canonical weight |
| $\mathcal R_{\mathrm{pha}}$, $\mathcal R_{\mathrm{rpd}}$ | The two covariant rates |
| $\vec p_{\mathrm{spin}}=-\hbar c\rho_{\mathrm{chg}}\beta\hat n_{\mathrm{rot}}$ | The spin's momentum; unchanged by the coupling |
| $p_{r}=p_{\theta_{\mathrm{rpd}}}=p_{u_{\mathrm b}}=0$ | The four vanishing momenta |
| $\omega_{\mu\nu}$ | The vorticity; the frame's, not $ϙ F/m$ |
| $\mathcal L_{\mathrm{kin}}^{\mathrm{gco}}$ | The kinetic Lagrangian density with the connection |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part |

## Further Reading

- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 2–35, for the charged spin fluid's equations and the absence of a torque.
- Fritz Bopp and Rudolf Haag, "Über die Möglichkeit von Spinmodellen," *Zeitschrift für Naturforschung* **5a** (1950) 644–653, for the spinning fluid with an external field and the transport it does and does not acquire.
- Friedrich W. Hehl, Peter von der Heyde, G. David Kerlick and James M. Nester, "General relativity with spin and torsion," *Reviews of Modern Physics* **48** (1976) 393–416, for the statement that a minimal coupling moves a momentum and not a spin.
- Peter A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for the second-class reduction that the four vanishing momenta require.
- The companion articles: [The Variational Principle and the Coupled Dirac Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-coupled-dirac-equation-in-biquaternionic-polar-variables.html), the same action with the connection and the reconstruction conjecture; [The Charged Spin Fluid](the-charged-spin-fluid.html), the equations, the force and the absent torque; [The Lagrangian of the Spin Fluid](the-lagrangian-of-the-spin-fluid.html), the free table this article reproduces; [The Lagrangian of the Charged Klein–Gordon Fluid](the-lagrangian-of-the-charged-klein-gordon-fluid.html), the rung where the velocity is a gradient and the vorticity becomes the field; and [The Lagrangian of the Charged Proca Fluid](the-lagrangian-of-the-charged-proca-fluid.html), where the connection reaches the field's own divergence.
