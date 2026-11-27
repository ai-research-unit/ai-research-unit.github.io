# __The Charged Schrödinger Fluid from the Polar Action: The Connection Shifts the Potential and Not the Continuity__

## Introduction

[The Charged Schrödinger Fluid](the-charged-schrodinger-fluid.html) makes three claims and derives them from the couple equation: the vorticity becomes the magnetic field, the acceleration law gains the Lorentz force, and the momentum splits into a canonical and a kinetic half. [The Lagrangian and the Coupled Schrödinger Equation in Polar Variables](the-lagrangian-and-the-coupled-schrodinger-equation-in-polar-variables.html) writes the same action in the same word and reports that the connection enters the potential and nothing else.

This article varies that action and reads the fluid equations off the variations. The result is narrow and exact: **the connection reaches the phase bracket and no other, so continuity survives with the mechanical momentum in place of the canonical one, and the quantum potential does not move.** The vorticity identity follows from the chart, not from the equation, because the velocity is a shifted gradient and the curl of a gradient is a curvature.

**The sharp claim.** Under the equation route the vorticity identity is a consequence of the wave equation: one takes the curl of the velocity and uses the equation to eliminate the time derivative. Under the action route the identity is prior to the equation. The phase's conjugate momentum is fixed by the action's coefficient, the velocity is that momentum over the mass, and its curl is the curl of a gradient plus the curl of the connection. The first vanishes identically and the second is the field strength. No equation is used, and the identity therefore holds for every configuration in the chart, not only on solutions.

That is the difference the two routes make at this rung, and it is a difference in status and not in content.

**What the coupling does not do.** It does not touch the scale's gradient energy, so Madelung's quantum potential is unchanged. It does not touch the four vanishing momenta, so the constraint structure is unchanged. It does not touch the cross term between the rotor's rate and the boost axis, so the frame's canonical structure is unchanged. The polar companion states all three, and this article reads each of them as a statement about the fluid.

**Position in the block.** This is the variational companion of [The Charged Schrödinger Fluid](the-charged-schrodinger-fluid.html) and the coupled member of the pair whose free member is [Schrödinger Fluid Equations from the Polar Action](schrodinger-fluid-equations-from-the-polar-action.html). Its action is the polar companion's and its word is the free article's.

## Conventions

**The conventions are the free polar companion's, restated for the coupled article.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_{\imath}^{2}=-e_t$; $i$ central; $^{*}$ Hermitian and $^{\natural}$ quaternionic conjugation; $\mathrm{Sc}$ the coefficient of $e_t$; the pairing $\mathrm{Sc}(\cdot^{*}\cdot)$. The word is $\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ with the free ranges, and $\rho_{\mathrm{num}}=\varrho^{2}$, $\gamma=\cosh\theta_{\mathrm{rpd}}$, $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$.

The connection. $\tilde A_\Phi=i(\omicron_{\mathrm{pot}}/c)e_t+\vec A$ with $\omicron_{\mathrm{pot}}$ and $\vec A$ real, the coupling is $ϙ$ with $q=-ϙ$, and the covariant derivative is

$$
\tilde\nabla_{\mathrm{gco},\Phi}=\tilde\nabla_\Phi+\frac{2\pi i\,ϙ}{h}\tilde A_\Phi,
\qquad
D_{t'}=\partial_{t'}-\frac{2\pi i\,ϙ}{h}\omicron_{\mathrm{pot}},
\qquad
D_{\imath}=\partial_{\imath}+\frac{2\pi i\,ϙ}{h}A_{\imath}.
$$

The mechanical momentum is $\vec\pi=\vec p-q\vec A$ and the mechanical energy is $\mathcal E=E-ϙ\omicron_{\mathrm{pot}}$. The local transformation is $\digamma_{\mathrm{cph}}=\exp(\frac{2\pi iϙ\Gamma}{h})$ with $\Gamma$ real, and $\tilde A_\Phi\mapsto\tilde A_\Phi-\partial\Gamma$.

The two settings. In the **constant setting** the connection's coefficients are constants and its only slot is the energy; in the **operator setting** it sits in the spatial derivatives as well. The fluid equations need the second, and §*The Action in the Word* states it. Where a closed form is quoted from the polar companion, the setting is named.

## The Action in the Word

The action. The polar companion's functional is

$$
S=\int\mathrm{d}t'\,\mathrm{d}^{3}x\;\mathrm{Sc}\Bigl[\frac{i h}{4\pi}\bigl(\tilde\Xi^{*}\partial_{t'}\tilde\Xi-(\partial_{t'}\tilde\Xi^{*})\tilde\Xi\bigr)
-\frac{hc}{8\pi^{2}\nu_m}\sum_{\imath\in\{x,y,z\}}\bigl(D_{\imath}\tilde\Xi\bigr)^{*}\bigl(D_{\imath}\tilde\Xi\bigr)
+ϙ\omicron_{\mathrm{pot}}\,\tilde\Xi^{*}\tilde\Xi\Bigr],
$$

and the connection enters in two places, both of them covariant derivatives or algebraic.

The bracket, and the one place the connection can go. Because the word is invertible,

$$
\mathcal A^{\mathrm{gco}}_{\imath}=\tilde\Xi^{-1}D_{\imath}\tilde\Xi=\mathcal A_{\imath}+\frac{2\pi i\,ϙ}{h}A_{\imath},
$$

and the addition is a **central imaginary number**. The bracket decomposes into a real scalar, a central imaginary, a Hermitian part and a real vector, and a central imaginary addition has one place to go. It joins the phase rate and it reaches neither the scale, nor the boost, nor the rotor. The polar companion's sentence is that the connection is a shift and not a factor, and here it is the statement that fixes everything below.

The consequence for the metric. The kinetic term is $\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi\,\mathcal A^{\mathrm{gco}}_{\imath}(\mathcal A^{\mathrm{gco}}_{\imath})^{*})$ summed over the slots with the metric signs. The weight $\tilde\Xi^{*}\tilde\Xi=\varrho^{2}\cosh\theta_{\mathrm{rpd}}$ is built from the frame and the scale, and the connection is central, so the shift cannot change the weight and cannot change the metric. What it changes is one term linear in $A$ and one quadratic. The quadratic term is what makes the action invariant, and it is the term a presentation writing the interaction as "current times potential" does not display.

The constant setting's closed form. When the coefficients are constants the whole coupling is one substitution in the potential,

$$
V_{\mathrm{gco}}=(h_t-ϙ\omicron_{\mathrm{pot}})\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}\,\bigl((\vec h_\Psi-q\vec A)\cdot\vec u_{\mathrm b}\bigr),
$$

and every other term of the Lagrangian is the free one letter for letter. The phase coefficient $-\frac{h}{2\pi}\varrho^{2}\cosh\theta_{\mathrm{rpd}}$ is untouched, the cross term $\frac{h}{4\pi}\varrho^{2}\sinh\theta_{\mathrm{rpd}}(\vec\Omega\cdot\vec u_{\mathrm b})$ is untouched, and the four vanishing momenta stay vanishing.

## The Variation: The Phase Equation Is the Covariant Continuity

Varying $\theta_{\mathrm{pha}}$ is again the cleanest, and the coupling changes its coefficients and not its structure. The phase appears in the action only through its covariant rate and its covariant gradient, and the Euler–Lagrange equation is

$$
D_{t'}\frac{\partial\mathcal L}{\partial(D_{t'}\theta_{\mathrm{pha}})}
+\sum_{\imath}D_{\imath}\frac{\partial\mathcal L}{\partial(D_{\imath}\theta_{\mathrm{pha}})}=0 .
$$

On the central class the coefficients are $-\rho_{\mathrm{num}}$ and $-\rho_{\mathrm{num}}\vec\pi/m$, and the equation is

$$
\partial_{t'}\rho_{\mathrm{num}}+\vec\nabla_\Phi\cdot\bigl(\rho_{\mathrm{num}}\vec v\bigr)=0,
\qquad
\vec v=\frac{\vec\nabla_\Phi S_{\tilde\Xi}-q\vec A}{m}=\frac{\vec\pi}{m},
$$

which is the charged fluid's continuity equation. The form is the free one and the velocity is the mechanical one.

**Three statements, and each is a warrant.**

*The continuity equation survives the coupling.* The connection enters the phase's coefficients and the equation is a divergence of those coefficients, so the coupling cannot destroy it. This is exact and it is the reason the charged Schrödinger fluid keeps its density.

*The velocity is the mechanical momentum and not the canonical one.* The action decides this: the phase's gradient appears only in the combination $\vec\nabla_\Phi\theta_{\mathrm{pha}}+\frac{2\piϙ}{h}\vec A$, so the conjugate momentum is the mechanical momentum. The split of the momentum into a canonical and a kinetic half, which the fluid article states, is therefore a statement about the chart's gradient basis and not a dynamical fact.

*The continuity equation is chargeless.* Nothing in it refers to $ϙ$ except through $\vec v$, and $\vec v$ is what the flow is. A reader who expects the coupling to appear as a source term in continuity will not find one, and the reason is the type of the addition: a central scalar cannot source a real divergence.

## The Variation: The Scale Equation Keeps Madelung's Quantum Potential

Varying $\varrho$ gives the covariant Hamilton–Jacobi equation, and the article's sharpest statement is about what does **not** change.

$$
\mathcal E+\frac{\vec\pi^{2}}{2m}+V+Q=0,
\qquad
Q=-\frac{h^{2}}{4\pi^{2}}\frac{\Delta_\Phi\varrho}{2m\varrho},
$$

with $\mathcal E$ and $\vec\pi$ the mechanical energy and momentum and $V$ the potential. $Q$ is Madelung's, letter for letter.

**Why the quantum potential is charge-blind.** The gradient energy is $\frac{hc}{8\pi^{2}\nu_m}\sum_{\imath}(D_{\imath}\tilde\Xi)^{*}(D_{\imath}\tilde\Xi)$, and on the central class its $\varrho$-dependent part is $\frac{hc}{8\pi^{2}\nu_m}(\vec\nabla_\Phi\varrho)^{2}$ with no $A$ in it. The covariant derivative acts on the phase and on the scale separately, and the connection is central, so it cannot enter the scale's term. The quantum potential is the variation of a term the connection never sees.

**The objection.** A reader will object that a covariant derivative acting on $\varrho e^{i\theta}$ produces a term in $\varrho\vec A$ and therefore a coupling of the connection to the density. That is correct and it is the quadratic term of the action, not the gradient energy's $\varrho$-curvature. The two are different objects: the first is a term in $\varrho^{2}\lvert A\rvert^{2}$ and $\varrho^{2}\vec A\cdot\vec\nabla\theta$, which are the interaction; the second is $\lvert\vec\nabla\varrho\rvert^{2}$, which is the quantum potential's source. The connection reaches the first and not the second, and the quantum potential is the second.

**What the coupling does to the guidance.** It shifts the velocity. The guidance equation says the flow is the mechanical momentum over the mass, and the mechanical momentum is the canonical one minus $q\vec A$. So the coupling bends the flow and leaves the quantum force alone. The fluid article states this as "the quantum force stays charge-blind", and the action route states it as the type of the addition.

## The Frame's Equations: Unchanged, and the Vorticity Reads the Connection

**The frame is untouched.** The four vanishing momenta are the free article's four, because the phase coefficient they are read from is untouched. The frame's equations therefore have the free form with $V$ replaced by $V_{\mathrm{gco}}$.

**The vorticity, and this is the article's one genuinely new derivation.** The velocity is a shifted gradient, $\vec v=\vec\nabla_\Phi S_{\tilde\Xi}/m-q\vec A/m$. Taking the curl,

$$
\vec\nabla_\Phi\times\vec v=-\frac{q}{m}\vec\nabla_\Phi\times\vec A=\frac{\varkappa}{m}\vec B,
\qquad
\varkappa=-q,
$$

because the curl of a gradient vanishes identically.

**What the derivation is and what it is not.** It is not a consequence of the wave equation. It uses the definition of the velocity, which the action fixes through the coefficient of the phase's gradient, and the identity $\vec\nabla\times\vec\nabla=0$. It therefore holds for every configuration in the chart and not only on solutions. Under the equation route the same identity is obtained after eliminating the time derivative with the equation, and the elimination is what makes it look dynamical. It is not.

**What the derivation does not give.** The vorticity's rate. $\partial_{t'}\vec\omega=-\frac{\varkappa}{m}\vec\nabla\times\vec E$ is Faraday's law, and it needs the connection to be a field obeying Maxwell's equations. The action here treats the connection as external and fixed, so the rate is not a statement of this functional. The fluid article states it and attributes it to the connection's own equation.

## The Constraints and the Redundant Direction

**The constraints survive.** Four momenta vanish identically, the Hessian is degenerate in four directions, and the four frame equations are constraints rather than evolutions. The coupling changes none of the count, because the phase coefficient it would have to change is not changed.

**A fifth direction appears, and it is the phase.** The local transformation translates $\theta_{\mathrm{pha}}$ and leaves the other seven parameters alone, so the coupled chart has a direction along which field and connection together are unchanged. The free chart has no such direction: all eight parameters are physical.

**The two statements are one.** The momentum conjugate to the redundant direction is $-\frac{h}{2\pi}\rho_{\mathrm{chg}}$, and the charge is the source the connection's own equation needs. So the redundant direction of the chart is the charge, and the Noether current of the phase shift is the current that sources the field. The action route displays this in one line; the equation route needs the equation and its conjugate.

**The count, honestly.** The free system has four constraints and no redundancy. The coupled system has four constraints and one redundancy. The difference is one, and it is the phase, and the phase is where the connection sits.

## The Noether Currents: Charge, Energy and No Spin

**The phase shift** gives the charge current, and it is the current continuity conserves, $\tilde J_\Phi=\rho_{\mathrm{num}}\tilde\pi/m$ on the central class. It is conserved by the phase's equation, which is the statement that continuity and charge conservation are one equation and not two.

**Translation** gives the stress. The coupling changes it in two ways: the mechanical momentum replaces the canonical one in the dust term, and the quadratic term in $A$ contributes. The polar companion's remark that the quadratic term is what makes the action invariant is also the remark that it is what makes the stress gauge-invariant.

**There is no spin current.** The rotor's momentum vanishes, as in the free case, and the coupling does not change a momentum that is zero. The charged Schrödinger fluid is a charged fluid without spin, and the action says so by the vanishing of one derivative.

## What the Alternative Route Adds and What It Relabels

**Adds.** The status of the vorticity identity as an identity of the chart rather than a consequence of the equation. The exact statement that the quantum potential is charge-blind because the connection is central, which the equation route states as an observation about a formula and the action route states as a statement about a term. The location of the interaction in the quadratic term. And the identification of the chart's redundant direction with the charge.

**Does not add.** No new equation. The four fluid equations — continuity, guidance, vorticity and the frame's transport — are the fluid article's, and the polar companion's closure argument is repeated with covariant letters. The free article's open item, the explicit frame gradients in the operator setting, remains open here for the same reason.

**Relabels.** The phrase "the vorticity is the magnetic field". On the equation route it is a theorem about solutions. On the action route it is a statement about the velocity's definition, and the theorem about solutions is its corollary.

## Open Questions

**The frame's gradients under coupling.** Whether the operator-setting gradient terms in the frame's angles acquire a connection term of their own is not settled here. The type argument says they cannot, because the connection is central, and a computation would confirm it.

**The connection's back-reaction.** The connection is external throughout. Whether the functional's variation with respect to $\tilde A_\Phi$ reproduces the Maxwell equation with the phase current as source is the polar companion's question, and the answer would close the loop between the two Noether currents.

## Summary

The coupled polar action of the Schrödinger field varies into the charged fluid's equations. The connection is a central imaginary addition to the bracket, so it joins the phase and reaches nothing else: continuity survives with the mechanical momentum as the velocity, the quantum potential keeps Madelung's form, and the four vanishing momenta stay vanishing. The vorticity identity is obtained without the equation, because the velocity is a shifted gradient and the curl of a gradient is zero. The coupling adds one thing the free chart does not have, a redundant direction, and the direction is the phase, whose conjugate momentum is the charge. Nothing in the fluid's equations changes except the velocity, and that is the exact content of the polar companion's sentence that the connection is a shift and not a factor.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\tilde A_\Phi=i(\omicron_{\mathrm{pot}}/c)e_t+\vec A$ | external connection, real components |
| $ϙ$, $q=-ϙ$ | coupling; $q$ the electric charge of the older convention |
| $D_{\imath}$, $D_{t'}$ | covariant derivatives |
| $\vec\pi=\vec p-q\vec A$ | mechanical momentum; the velocity is $\vec\pi/m$ |
| $\mathcal A^{\mathrm{gco}}_{\imath}$ | $\tilde\Xi^{-1}D_{\imath}\tilde\Xi=\mathcal A_{\imath}+\frac{2\pi iϙ}{h}A_{\imath}$ |
| $V_{\mathrm{gco}}$ | shifted potential |
| $\varkappa=-q$ | coupling in the fluid's letters |
| $\vec\omega=\vec\nabla_\Phi\times\vec v$ | vorticity; equals $\varkappa\vec B/m$ identically |
| $\digamma_{\mathrm{cph}}$ | $\exp(\frac{2\pi iϙ\Gamma}{h})$, the local phase transformation |
| $Q$ | Madelung's quantum potential, charge-blind |

## Further Reading

- Erwin Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1927) 322–326, for the variational principle of the pair.
- Takehiko Takabayasi, "On the formulation of quantum mechanics associated with classical pictures," *Progress of Theoretical Physics* **8** (1952) 143–182, for the fluid reading of a charged scalar wave.
- Fritz London, "Superfluids" (Wiley, 1950), volume 1, for the identification of the vorticity of a charged condensate with the magnetic field.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), for the covariant Madelung pair and the charge-blindness of the quantum potential.
