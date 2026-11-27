# __Schrödinger Fluid Equations from the Polar Action: Continuity and Guidance as Two Euler–Lagrange Equations__

## Introduction

[The Schrödinger Fluid](the-schrodinger-fluid.html) reads the wave equation and names a density, a velocity and a quantum potential. [The Lagrangian and the Schrödinger Equation in Polar Variables](the-lagrangian-and-the-schrodinger-equation-in-polar-variables.html) substitutes the polar word into the action and reports the flow. Neither writes the fluid's equations as the variations of a functional.

This article does. It varies the polar action in the eight parameters of the word and reads the result as fluid equations. The phase's variation is the continuity equation. The scale's variation is the guidance equation, with the quantum potential. The four frame variations are the transport of the boost axis and of the rotor, and the fluid neither needs them nor carries them.

**The two routes, and what the difference is.** On the equation route the field equation is written first, the word is substituted into it, and the types are separated. On the action route no equation is written: the functional is written, it is varied in each coordinate, and the equations that come out are the fluid's. The two routes must agree, and on the central class they do, because both are Madelung's.

The agreement is not the point. The point is what each route can see. The equation route sees the eight components of one equation and must decide by hand which combination is continuity and which is guidance. The action route sees eight coordinates, each with its own equation, and the identification is the coordinate's name rather than a combination: the phase's coordinate gives continuity, the scale's gives guidance, and the four frame coordinates give the frame's transport. Nothing has to be recombined, and nothing can be mis-combined.

**The strongest objection, stated before it is answered.** Madelung wrote this variational principle in 1927, and the polar companion says so in one sentence: "These are Madelung's pair read on a constant Hamiltonian." An article that varies a polar action and finds continuity and a quantum Hamilton–Jacobi equation is therefore either a restatement or a rediscovery.

The answer has two parts. First, for the central class the objection holds and the article says so: that case is closed, standard, and cited. Second, the central class is the case in which the word collapses to $\varrho\,e^{i\theta_{\mathrm{pha}}}\varepsilon e_t$ and four of the eight parameters are frozen. It cannot show the frame, and the frame is not decoration. The density of the biquaternionic field is $\varrho^{2}$, the charge density is $\gamma\varrho^{2}$ with $\gamma=\cosh\theta_{\mathrm{rpd}}$, and the phase's conjugate momentum is $-\frac{h}{2\pi}\varrho^{2}\cosh\theta_{\mathrm{rpd}}$. A chart in which the momentum of the phase is not the density is a chart in which the identification "phase momentum equals $-\frac{h}{2\pi}\rho_{\mathrm{num}}$" has already failed, and the failure is a statement about the fluid: the fluid's density is the proper density, and the phase moves the charge.

**Position in the block.** This is the variational companion of [The Schrödinger Fluid](the-schrodinger-fluid.html) and of [The Lagrangian and the Schrödinger Fluid](the-lagrangian-and-the-schrodinger-fluid.html). The difference from the second is the chart: that article writes the action in the fluid's two variables, $\varrho$ and $S_{\tilde\Xi}$, and this one writes it in the eight parameters of the complete word. The two-field chart is the central class of this one, and the six parameters it drops are the frame.

## Conventions

**The conventions are restated here so that every sign below is checkable from this page alone.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_{\imath}^{2}=-e_t$; $i$ is the central scalar imaginary; $^{*}$ is Hermitian conjugation and $^{\natural}$ quaternion conjugation; $\mathrm{Sc}$ is the coefficient of $e_t$. The pairing is $\mathrm{Sc}(\cdot^{*}\cdot)$. The word is

$$
\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
\qquad
\tilde U_{\Psi,\mathrm b}=\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr),
\qquad
\tilde u_{\mathrm r}=\exp\Bigl(\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr),
$$

with $\varrho>0$, $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$, $\theta_{\mathrm{rpd}}\ge0$, $\theta_{\mathrm{axr}}\in[0,2\pi]$, and $\vec u_{\mathrm b}$, $\vec u_{\mathrm r}$ unit real vectors. The word is a bijection onto the $N$-regular set.

The densities. The proper density is $\rho_{\mathrm{num}}=\varrho^{2}$, the Lorentz factor of the flow is $\gamma=\cosh\theta_{\mathrm{rpd}}$, and the charge density is $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$. The Hermitian norm is $2\,\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)=2\varrho^{2}\cosh\theta_{\mathrm{rpd}}$, which is twice the charge density; the factor is the corpus's normalization of the norm and not a second density.

The action and the phase. The action variable is $S_{\tilde\Xi}=\frac{h}{2\pi}\theta_{\mathrm{pha}}$, defined modulo $h$. The rotor's angular velocity is $\vec\Omega$ with $\partial_{t'}\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{-1}=\frac12\vec\Omega$, the space-frame convention of the polar companion. Time is $t'$ and the spatial derivative is $\vec\nabla_\Phi$; the potential is

$$
V=h_t\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}\,(\vec h_\Psi\cdot\vec u_{\mathrm b}),
$$

with $\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi$ the Hamiltonian. The quantum potential is $Q=-\frac{h^{2}}{4\pi^{2}}\Delta_\Phi\varrho/(2m\varrho)$.

The two settings, and the one this article uses. In the **constant setting** $\tilde H_\Psi$ is a fixed element, the equation is an ordinary differential equation in $t'$, and the polar companion's closed forms hold letter for letter. In the **operator setting** $\tilde H_\Psi$ is a differential operator and the action carries the spatial gradients. Fluid equations are partial differential equations in space and time, so they require the operator setting, and §*The Action in the Word* states the functional in it. The constant setting is used where a closed form is quoted, and it is named every time.

## The Action in the Word

The element action. The polar companion's starting point is

$$
S[\tilde\Xi,\tilde\Xi^{*}]=\int\mathrm{d}t'\,\mathrm{Sc}\Bigl[\frac{i h}{4\pi}\bigl(\tilde\Xi^{*}\partial_{t'}\tilde\Xi-(\partial_{t'}\tilde\Xi^{*})\tilde\Xi\bigr)-\tilde\Xi^{*}\tilde H_\Psi\tilde\Xi\Bigr],
$$

in the constant setting. In the operator setting the Hamiltonian term is replaced by the gradient term of *The Lagrangian and the Coupled Schrödinger Equation in Polar Variables* with the connection set to zero,

$$
S=\int\mathrm{d}t'\,\mathrm{d}^{3}x\;\mathrm{Sc}\Bigl[\frac{i h}{4\pi}\bigl(\tilde\Xi^{*}\partial_{t'}\tilde\Xi-(\partial_{t'}\tilde\Xi^{*})\tilde\Xi\bigr)-\frac{hc}{8\pi^{2}\nu_m}\sum_{\imath\in\{x,y,z\}}(\partial_{\imath}\tilde\Xi)^{*}(\partial_{\imath}\tilde\Xi)\Bigr],
$$

with $\nu_m=\frac{mc}{h}$.

The bracket. Because the word is invertible, every derivative of the field is the field times a logarithmic derivative,

$$
\mathcal A_{\imath}=\tilde\Xi^{-1}\partial_{\imath}\tilde\Xi ,
$$

and the logarithmic derivative is the sum of four objects: a real central scale rate, a central imaginary phase rate, a Hermitian boost connection, and a real-vector rotor connection. The four pieces are the four types of the algebra. The kinetic term is the frame density times the square of the bracket, $\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi\,\mathcal A_{\imath}\mathcal A_{\imath}^{*})$, which is why the metric is field-dependent and why the connection of the coupled article cannot change it.

Two cases of the substitution, and they are different calculations.

**The central class.** $\theta_{\mathrm{rpd}}=0$ and $\tilde u_{\mathrm r}=\varepsilon e_t$, so the word is three parameters and the kinetic term is $-\frac{h}{2\pi}\varrho^{2}\dot\theta_{\mathrm{pha}}$. The action becomes Madelung's,

$$
\mathcal L_{\mathrm{fl}}=-\rho_{\mathrm{num}}\Bigl(\partial_{t'}S_{\tilde\Xi}+\frac{(\vec\nabla_\Phi S_{\tilde\Xi})^{2}}{2m}+V\Bigr)-\frac{hc}{8\pi^{2}\nu_m}\bigl(\vec\nabla_\Phi\varrho\bigr)^{2},
$$

which is [The Lagrangian and the Schrödinger Fluid](the-lagrangian-and-the-schrodinger-fluid.html)'s display and is cited, not re-derived.

**The general word.** All four factors. The kinetic term is the polar companion's exact result,

$$
L=-\frac{h}{2\pi}\varrho^{2}\cosh\theta_{\mathrm{rpd}}\,\dot\theta_{\mathrm{pha}}
+\frac{h}{4\pi}\varrho^{2}\sinh\theta_{\mathrm{rpd}}\,(\vec\Omega\cdot\vec u_{\mathrm b})
-\varrho^{2}V,
$$

and the cross term is the part the central class cannot show. In the operator setting the same computation is done slot by slot, and the gradient terms carry the frame's gradients beside the scale's and the phase's.

## The Variation: The Phase Equation Is Continuity

Varying $\theta_{\mathrm{pha}}$ is the cleanest of the eight, because the phase appears in the action only through its rate and its gradient. The action depends on $\partial_{t'}\theta_{\mathrm{pha}}$ and $\vec\nabla_\Phi\theta_{\mathrm{pha}}$ and on nothing else of the phase, so its Euler–Lagrange equation is a conservation law in the strict sense,

$$
\partial_{t'}\frac{\partial\mathcal L}{\partial(\partial_{t'}\theta_{\mathrm{pha}})}
+\sum_{\imath}\partial_{\imath}\frac{\partial\mathcal L}{\partial(\partial_{\imath}\theta_{\mathrm{pha}})}=0 .
$$

The coefficient of the phase's rate is the phase momentum, $p_{\theta_{\mathrm{pha}}}=-\frac{h}{2\pi}\varrho^{2}\cosh\theta_{\mathrm{rpd}}=-\frac{h}{2\pi}\rho_{\mathrm{chg}}$, and the coefficient of its gradient is the current. On the central class the two coefficients are $-\rho_{\mathrm{num}}$ and $-\rho_{\mathrm{num}}\vec\nabla_\Phi S_{\tilde\Xi}/m$, and the equation is

$$
\partial_{t'}\rho_{\mathrm{num}}+\vec\nabla_\Phi\cdot\bigl(\rho_{\mathrm{num}}\vec v\bigr)=0,
\qquad
\vec v=\frac{\vec\nabla_\Phi S_{\tilde\Xi}}{m},
$$

which is the continuity equation of [The Schrödinger Fluid](the-schrodinger-fluid.html) with the velocity as the phase gradient over the mass.

**Three statements about this equation, and each is a warrant.**

*It is one coordinate's equation and not a combination.* The equation route obtains continuity by multiplying the wave equation by $\tilde\Xi^{*}$ and subtracting its conjugate, which is a construction on the equation. Here nothing is constructed: $\theta_{\mathrm{pha}}$ is a coordinate and its Euler–Lagrange equation is the conservation of its momentum. The two are the same equation, and the second says why it is a conservation law — because the action cannot see the phase itself.

*It does not use the frame's equations.* The phase equation contains $\varrho$, $\theta_{\mathrm{rpd}}$ and $\vec u_{\mathrm{b}}$ as coefficients, and it contains no derivative of them that is not contracted with the current. It is therefore compatible with any frame, and the frame's own equations are not needed to write it. This is the structural fact that makes the fluid reading legitimate: the density and the phase close on their own.

*It is not $\varrho^{2}$ on the general word.* The conserved object is the phase momentum, and the phase momentum is the charge density, $\varrho^{2}\cosh\theta_{\mathrm{rpd}}$, not the proper density. On the central class the two coincide up to the normalization. A reader who identifies the density with $\varrho^{2}$ on the general word will write a continuity equation that the action does not give.

## The Variation: The Scale Equation Is the Guidance

Varying $\varrho$ gives the second member of the pair. On the central class the scale appears in two terms, the phase's coefficient and the gradient energy, and its Euler–Lagrange equation is

$$
\partial_{t'}S_{\tilde\Xi}+\frac{(\vec\nabla_\Phi S_{\tilde\Xi})^{2}}{2m}+V+Q=0,
\qquad
Q=-\frac{h^{2}}{4\pi^{2}}\frac{\Delta_\Phi\varrho}{2m\varrho},
$$

which is the quantum Hamilton–Jacobi equation. The derivation is one line and it is worth displaying because it is where the quantum potential comes from: the gradient energy is quadratic in $\vec\nabla_\Phi\varrho$, so its variation produces a divergence, and the divergence divided by $\varrho$ is the quantum potential.

**The objection, and the answer.** A reader will object that a guidance equation obtained by varying a density is a density equation and not a guidance equation, because it contains no trajectory. The answer is that the guidance equation is the statement that the flow is the phase gradient, and that statement is the coefficient of the phase's rate once the scale's equation is used. The two equations are one Hamilton–Jacobi pair: the second fixes the velocity, the first transports the density along it.

**What the general word changes.** Two things, and they are the reason this article is not the two-field article.

*The quantum potential keeps the Laplacian and the frame adds nothing to it.* The scale's gradient energy in the operator setting is $\frac{hc}{8\pi^{2}\nu_m}\sum_{\imath}(\partial_{\imath}\varrho)^{2}$, which is the term that produces $Q$, and it is a term in the scale alone. No frame parameter enters it. The quantum potential of the biquaternionic Schrödinger field is therefore Madelung's, exactly, with no correction from the boost or the rotor. That is a checkable statement and the polar companion states its equation-route form.

*The frame enters the guidance through the potential, and the potential is the only place it enters.* $V$ depends on $\theta_{\mathrm{rpd}}$ and on $\vec u_{\mathrm{b}}$, so the scale's equation contains them, and the pair does not close without the frame's equations when $V$ is not a constant. This is the precise sense in which the biquaternionic field's fluid is a fluid with an internal frame: the guidance equation carries the frame's data in its potential, and the continuity equation does not.

## The Frame's Equations: What the Fluid Does Not Need

The four remaining variations are the frame's, and the article states them and then says what they are worth.

**The count.** Four frame coordinates — the rapidity, the two angles of $\vec u_{\mathrm b}$, and the rotor's angle and axis, counted as three with one redundant. In the constant setting four of the eight momenta vanish identically, namely $p_{\varrho}$, $p_{\theta_{\mathrm{rpd}}}$ and the two conjugate to the boost axis. Their Euler–Lagrange equations are therefore not evolution equations; they fix the four rates the momenta do not fix. This is the polar companion's result and it is repeated here with the fluid reading attached.

**What the vanishing momenta mean in fluid words.** A coordinate whose momentum vanishes is a coordinate the action does not transport. The fluid's density and phase are transported; the frame's orientation is not. The frame is therefore not a fluid variable in the transport sense even where it is a fluid variable in the kinematic sense. That is the sharp difference between this rung and the spinor rung, where the rotor is transported and carries a spin current.

**The one frame statement the fluid uses.** The flow's velocity is the boost's direction, and the boost's rapidity is the flow's Lorentz factor. The solution the polar companion reports — $\varrho$ and $\theta_{\mathrm{rpd}}$ constant, $\dot\theta_{\mathrm{pha}}=-\frac{2\pi h_t}{h}$, $\vec\Omega=\frac{4\pi\vec h_\Psi}{h}$, and the boost axis fixed in the rotor's frame — is the free flow read in the chart. The fluid reads it as: a uniform density, a uniform Lorentz factor, a phase advancing at the energy, and a frame turning at twice the Hamiltonian's vector part. No fluid equation is needed for any of it.

## The Constraints the Action Imposes: Four Vanishing Momenta

The action is first order in the time derivative. Its Hessian with respect to the eight rates is therefore degenerate, and the degenerate directions are the four whose momenta vanish. The system has four primary constraints, and they are second class.

**Why this is a statement about the chart and not about the field.** A first-order action has one rate per coordinate at most, and the word supplies eight coordinates of which only the phase's rate appears. The constraints are the price of writing the field's orientation as coordinates when the action transports only the phase. The equation route meets the same fact as the statement that the wave equation is first order; the action route meets it as a degenerate Hessian.

**What the fluid does with them.** Nothing, and that is the point. The fluid's two equations are the two coordinates whose momenta do not vanish. A fluid reading that needed the constraints would be a reading of the constraint surface rather than of the field, and the corpus's scalar fluid is not that.

**The contrast with the rungs above.** At the Klein–Gordon rung the action is second order, no momentum vanishes, and the count of equations equals the count of coordinates. At the spinor rung the action is first order again, and the constraints are what the Dirac bracket is built on. The Schrödinger rung is the one at which the constraints are present and harmless, because the fluid uses only the two unconstrained coordinates.

## The Noether Currents: Density, Energy and the Absence of a Charge

**Translation invariance** gives the stress, and its time–time component is the energy density. On the central class the canonical tensor is the fluid's, with the dust term $\rho_{\mathrm{num}}m$ and the gradient energy contributing $-\frac{h^{2}}{8\pi^{2}m}\lvert\vec\nabla_\Phi\ln\varrho\rvert^{2}$ up to an improvement. The improvement matters and the corpus's *Quantum Stress Tensor of the Biquaternion Scalar Field* owns it.

**Phase invariance** gives the current, and the current is the one continuity conserves. The charge here is the phase's conjugate momentum, $-\frac{h}{2\pi}\rho_{\mathrm{chg}}$, which is the density times the Lorentz factor.

**There is no separate spin current, and this is the difference from the rungs above.** The rotor is a coordinate whose momentum vanishes, so the action supplies no transport law for it and no conserved spin. A fluid whose rotor is not transported has no spin dynamics, and the Schrödinger fluid is such a fluid.

## What the Alternative Route Adds and What It Relabels

**Adds.** The identification of each fluid equation with a coordinate rather than with a combination of components. The exact statement that the phase's conjugate momentum is the charge density and not the proper density, which the central class cannot show. The structural statement that the continuity equation is independent of the frame's equations while the guidance equation is not, which is what makes the fluid reading a reading of two coupled objects and not of eight. And the location of the quantum potential: it is the scale's gradient energy and no frame term reaches it.

**Does not add.** No new equation. No new solution. On the central class the pair is Madelung's and the article claims nothing there. The general word's frame equations are stated structurally and their explicit gradients in the operator setting are not computed; that is the same gap the polar companion records for the general Jacobian, and this article does not close it.

**Relabels.** The claim that the polar decomposition is a lens. Under the equation route the lens is a way of reading one equation. Under the action route the lens is a set of coordinates, and the equations of the coordinates are the fluid's. The two statements are the same statement, and the second is the one that makes the fluid's count visible before any equation is solved.

## Open Questions

**The explicit frame gradients.** The operator-setting action's gradient terms in $\theta_{\mathrm{rpd}}$, $\vec u_{\mathrm b}$ and $\theta_{\mathrm{axr}}$ are not written here. Whether their variation reduces to a transport law with a closed form is open, and it is the calculation that would make the general word's fluid equations as explicit as the central class's.

**The reduced flow.** The four second-class constraints define a Dirac bracket, and whether the reduced flow is the parent's flow is the polar companion's open question. The fluid reading does not depend on the answer, because it uses the two unconstrained coordinates, and a reader who wants the general flow needs it.

## Summary

The polar action of the Schrödinger field, varied in its eight coordinates, gives the fluid equations as the coordinates' Euler–Lagrange equations. The phase's equation is continuity for the phase momentum, which is the charge density. The scale's equation is the guidance equation with Madelung's quantum potential, and the potential is the only place the frame enters it. The four frame coordinates have vanishing momenta, so they are not transported and the fluid carries no spin. On the central class the two equations are Madelung's pair, standard since 1927; on the general word they are the same pair with the frame in the potential, and the density is the proper density rather than the charge density. The route adds no equation and no solution. It adds the assignment of each fluid equation to one coordinate, and the exact statement of which coordinates the fluid does and does not use.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\tilde\Xi$ | the field; an $N$-regular biquaternion |
| $\varrho>0$ | the scale |
| $\theta_{\mathrm{pha}}$ | the central phase; $S_{\tilde\Xi}=\frac{h}{2\pi}\theta_{\mathrm{pha}}$ |
| $\theta_{\mathrm{rpd}}\ge0$ | the rapidity of the boost |
| $\vec u_{\mathrm b}$, $\vec u_{\mathrm r}$ | boost axis and rotor axis, unit real vectors |
| $\theta_{\mathrm{axr}}\in[0,2\pi]$ | the rotor's angle |
| $\rho_{\mathrm{num}}=\varrho^{2}$ | proper density |
| $\gamma=\cosh\theta_{\mathrm{rpd}}$ | Lorentz factor of the flow |
| $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$ | charge density; $-\frac{h}{2\pi}$ times the phase momentum |
| $\mathcal A_{\imath}$ | $\tilde\Xi^{-1}\partial_{\imath}\tilde\Xi$, the four-type bracket |
| $\vec\Omega$ | rotor's angular velocity, $\partial_{t'}\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{-1}=\frac12\vec\Omega$ |
| $V$ | polar potential, $h_t\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}(\vec h_\Psi\cdot\vec u_{\mathrm b})$ |
| $Q$ | quantum potential, $-\frac{h^{2}}{4\pi^{2}}\Delta_\Phi\varrho/(2m\varrho)$ |
| $\nu_m$ | $mc/h$ |

## Further Reading

- Erwin Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1927) 322–326, for the continuity equation and the Hamilton–Jacobi equation of a scalar wave and for their variational principle.
- Takehiko Takabayasi, "On the formulation of quantum mechanics associated with classical pictures," *Progress of Theoretical Physics* **8** (1952) 143–182, for the fluid reading of the pair.
- David Bohm, "A suggested interpretation of the quantum theory in terms of hidden variables," *Physical Review* **85** (1952) 166–193, for the quantum potential and the guidance equation.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), for the variational derivation of the Madelung pair and its limits.
