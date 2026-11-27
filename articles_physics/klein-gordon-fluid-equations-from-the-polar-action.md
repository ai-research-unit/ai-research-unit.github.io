# __Klein–Gordon Fluid Equations from the Polar Action: Continuity, Mass Shell and the Frame's Transport__

## Introduction

[The Spin-Zero Fluid](the-spin-zero-fluid.html) states the mass shell as a condition and derives the flow from it. [The Lagrangian and the Spin-Zero Fluid](the-lagrangian-and-the-spin-zero-fluid.html) removes the condition by writing an action in two variables and varying them. [The Lagrangian and the Klein–Gordon Equation in Polar Variables](the-lagrangian-and-the-klein-gordon-equation-in-polar-variables.html) writes the same action in the eight coordinates of the complete word and reports that its Euler–Lagrange equations are the Klein–Gordon equation pulled back to the parameters.

This article does the last step those three leave undone. It varies the eight-coordinate action and reads the equations as the fluid's, one equation per fluid statement, with no equation written first and nothing substituted into an equation.

**The claim, in one sentence.** Continuity is the phase's equation, the mass shell with the quantum potential is the scale's, and the two are the only equations of the pair, because the action is second order and no momentum vanishes.

**Two consequences that the two-field chart cannot state.**

*First, the field's rapidity is the flow's Lorentz factor on shell.* The density is $\rho_{\mathrm{num}}=\varrho^{2}$ and the charge density is $\gamma\varrho^{2}$ with $\gamma=\cosh\theta_{\mathrm{rpd}}$, while the flow's own Lorentz factor is $E/(mc^{2})$ on the mass shell. The two agree on shell, so the chart's rapidity carries the flow's $\gamma$ and is not an internal angle. That is an identity of the polar displays and it is what makes the frame a fluid variable here.

*Second, the frame appears in the density and not only in the potential.* At the Schrödinger rung the frame entered the guidance equation through the potential and the density was frame-free. Here the frame multiplies the density, so a fluid reading that suppresses the frame suppresses part of the density. The difference between the two rungs is the order of the action.

**The strongest objection.** *This is the variational derivation of the relativistic Madelung pair, which is standard, and the spin-zero fluid article already prints the result.* The objection is right about the pair and wrong about the chart. The standard derivation varies a density and a phase; this one varies eight coordinates, two of which are the pair's and six of which are the frame's, and the exact statement this article makes is that the six frame coordinates have equations of their own that the pair never uses. A two-variable derivation cannot show that the pair closes; the eight-coordinate one can, and it shows where it closes and where it does not.

**Position in the block.** This is the variational companion of [The Spin-Zero Fluid](the-spin-zero-fluid.html) and the free member of the pair whose coupled member is [The Charged Klein–Gordon Fluid from the Polar Action](charged-klein-gordon-fluid-equations-from-the-polar-action.html). It sits above [Schrödinger Fluid Equations from the Polar Action](schrodinger-fluid-equations-from-the-polar-action.html), where the same construction is first order.

## Conventions

**The conventions are the polar companion's, restated so that every sign is checkable from this page alone.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_{\imath}^{2}=-e_t$; $i$ central; $^{*}$ Hermitian, $^{\natural}$ quaternionic conjugation; $\mathrm{Sc}$ the coefficient of $e_t$; the pairing is $\mathrm{Sc}(\cdot^{*}\cdot)$. The word is

$$
\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
\qquad
\tilde U_{\Psi,\mathrm b}=\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr),
\qquad
\tilde u_{\mathrm r}=\exp\Bigl(\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr),
$$

with $\varrho>0$, $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$, $\theta_{\mathrm{rpd}}\ge0$, $\theta_{\mathrm{axr}}\in[0,2\pi]$, and unit real axes.

The letters. The action variable is $S_{\tilde\Xi}=\frac{h}{2\pi}\theta_{\mathrm{pha}}$, the proper density is $\rho_{\mathrm{num}}=\varrho^{2}$, the Lorentz factor is $\gamma=\cosh\theta_{\mathrm{rpd}}$, and the charge density is $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}=\rho_{\mathrm{num}}E/(mc^{2})$ on shell. The four-velocity is $\tilde V_\Phi=\tilde\nabla_\Phi S_{\tilde\Xi}/m$, with $\sum_{\imath}\varepsilon_{\imath}V_{\Phi,\imath}V_{\Phi,\imath}=-c^{2}$ on the mass shell. The d'Alembertian is $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial r^{\prime 2}_{t}$ with $r'_t=c\,t'$, the four-gradient is $\tilde\nabla_\Phi$, and $\nu_m=\frac{mc}{h}$. The quantum potential is $Q_{\mathrm{qnt}}=-\frac{h^{2}}{4\pi^{2}}\Box_\Phi\varrho/(2m\varrho)$.

The bracket. $\mathcal A_{\imath}=\tilde\Xi^{-1}\partial_{\imath}\tilde\Xi$, which splits into a real scale rate, a central imaginary phase rate, a Hermitian boost connection and a real-vector rotor connection. The action is quadratic in it with algebraic weight $\tilde\Xi^{*}\tilde\Xi\cdot$, which is the property everything below uses.

## The Action in the Word

The element form. The polar companion's functional is

$$
S=\int\mathrm{d}^{4}x\;\Bigl\{\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde\Xi\,\mathcal A_{\imath}\mathcal A_{\imath}^{*}\bigr]-\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde\Xi\bigr]\,4\pi^{2}\nu_m^{2}\Bigr\},
$$

summed over the four slots with the metric signs $\varepsilon_{\imath}$.

**The two terms, and what each can do.** The kinetic term is quadratic in the bracket, so it is second order in the parameters and supplies the metric. The mass term is algebraic, so it supplies no metric and only a potential. That split is the whole of the difference from the Schrödinger rung, where the kinetic term is first order and the Hessian is degenerate.

**The metric.** Written in parameters the kinetic term is a quadratic form $\tfrac12 G^{ab}(q)\partial_{\imath}q_a\partial_{\imath}q_b$ with $G$ built from the frame. The rapidity enters it twice: as $\cosh\theta_{\mathrm{rpd}}$ on the four squares and as $\sinh\theta_{\mathrm{rpd}}$ on two cross terms. The two identities that make it invertible are $\cosh^{2}-\sinh^{2}=1$ and the transversality of the boost axis, and the Legendre transform is regular for that reason.

**The central class.** $\theta_{\mathrm{rpd}}=0$ and $\tilde u_{\mathrm r}=\varepsilon e_t$. The metric collapses to $(1,\varrho^{2})$ in the scale and the phase, the cross terms vanish, and the action is Madelung's with a mass,

$$
\mathcal L=-\varrho^{2}\Bigl(\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}S_{\tilde\Xi}\partial_{\imath}S_{\tilde\Xi}+m^{2}c^{2}\Bigr)-\frac{hc}{8\pi^{2}\nu_m}\sum_{\imath}\varepsilon_{\imath}\bigl(\partial_{\imath}\varrho\bigr)^{2},
$$

up to the corpus's normalization, which is [The Lagrangian and the Spin-Zero Fluid](the-lagrangian-and-the-spin-zero-fluid.html)'s display and is cited here.

## The Variation: The Phase Equation Is Continuity

Varying $\theta_{\mathrm{pha}}$. The phase appears in the bracket and nowhere else, and its bracket is the central imaginary part. The Euler–Lagrange equation is therefore a divergence,

$$
\partial_{\imath}\frac{\partial\mathcal L}{\partial(\partial_{\imath}\theta_{\mathrm{pha}})}=0
\qquad\Longrightarrow\qquad
\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}\bigl(\rho_{\mathrm{num}}V_{\Phi,\imath}\bigr)=0,
$$

which is $\partial_{\imath}J_{\Phi,\imath}=0$ with $\tilde J_\Phi=\rho_{\mathrm{num}}\tilde V_\Phi$.

**Why this is continuity and not a conservation law with an extra name.** The current is the density times the four-velocity, and the four-velocity is the phase gradient over the mass. The equation says the divergence of that current vanishes. There is no other content and no correction term, because the connection is absent and the mass term carries no phase.

**What the general word adds.** Nothing to this equation. The phase's bracket is one type, the coefficient is the frame density, and the frame appears only as a factor outside the divergence — a factor that the divergence differentiates. The equation is therefore the same equation with $\rho_{\mathrm{num}}$ replaced by $\gamma\rho_{\mathrm{num}}$ in the current, which is to say that the conserved density is the charge density and not the proper density. That is the same statement the free polar article makes from the equation side.

**The objection.** *A conserved density that is not positive definite is not a fluid's density.* The objection is correct and it is the relativistic rung's central defect: the charge density changes sign with the branch, because the energy does. The fluid's own density is $\rho_{\mathrm{num}}$, which is positive, and it is conserved only after division by $\gamma$. The action states this without ambiguity: the phase's coefficient is $\rho_{\mathrm{chg}}$, and the proper density is what the current carries after the Lorentz factor is removed.

## The Variation: The Scale Equation Is the Mass Shell

Varying $\varrho$. The scale appears in the kinetic term through the weight and in the mass term algebraically, and its equation is a mass shell with a curvature term,

$$
\sum_{\imath}\varepsilon_{\imath}V_{\Phi,\imath}V_{\Phi,\imath}=-c^{2}-\frac{2Q_{\mathrm{qnt}}}{m},
\qquad
Q_{\mathrm{qnt}}=-\frac{h^{2}}{4\pi^{2}}\frac{\Box_\Phi\varrho}{2m\varrho},
$$

on the central class, which is [The Spin-Zero Fluid](the-spin-zero-fluid.html)'s display arrived at as an equation of motion.

**The derivation, in one line.** The gradient energy is quadratic in $\partial_{\imath}\varrho$, so its variation is a divergence of $\partial_{\imath}\varrho$; dividing by $\varrho$ turns the divergence into the logarithmic curvature, and the logarithmic curvature is the quantum potential. The mass term's variation gives the constant, and the phase's gradient gives the velocity's norm. Nothing else contributes.

**What the general word adds, and it is the article's second result.** The weight is $\varrho^{2}\cosh\theta_{\mathrm{rpd}}$, so the scale's variation is not the central one: varying $\varrho$ at fixed frame gives the mass shell multiplied by $\cosh\theta_{\mathrm{rpd}}$, and varying the rapidity gives a second equation in which the rapidity's gradient appears as a source. That is the structure [The Spin-One Fluid](the-spin-one-fluid.html) records at the vector rung and the scalar rung shares: **a rapidity gradient feeds the mass shell**. The central class cannot show it, because the rapidity is zero there and its gradient is zero with it.

**The pressure, and where it comes from.** The mass term is algebraic, so it contributes to the stress and not to the metric. Its contribution is along the flow, and its equation of state is fixed by the coefficient — the same structure the spin-one rung reads as $\epsilon=p$. This article does not recompute the stress; [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html) owns it, and the polar action's translation current is the same object up to an improvement.

## The Frame's Equations: The Fluid's Missing Half

Six coordinates remain, and their equations are the frame's.

**The count.** Eight coordinates, eight equations, all second order, no vanishing momentum. The action is regular in form and the article states the regularity of the Hessian as a property of the metric, not as a theorem about the reduced system.

**What the frame's equations say.** The rapidity's equation and the two boost-axis equations are the transport of the frame along the flow; the rotor's are the transport of the orientation. On the central class the frame is frozen and the equations are empty. Off it they are not, and their content is that the field's own boost is carried by the flow rather than by the phase.

**Why the fluid does or does not need them.** The pair closes as a pair of equations for $\varrho$ and $\theta_{\mathrm{pha}}$ only where the frame is frozen. Where it is not, the mass shell contains the rapidity's gradient and the pair does not close: the frame's equations must be solved with it. This is the exact sense in which the relativistic scalar fluid is a fluid with an internal frame and the non-relativistic one is not.

**The objection.** *A fluid whose equations do not close is not a fluid.* The answer is that it closes on the shell that defines it: on the mass shell the rapidity is the flow's Lorentz factor, and the frame's transport becomes a statement about the flow. The closure is therefore at the level of the four-velocity and not at the level of the eight parameters, which is why the two-field chart — density and phase — is available at all.

## The Constraints: None, and Why the Rungs Differ

The action is second order, so no momentum vanishes identically and there is no primary constraint. The polar companion states this and contrasts it with the first-order rungs, where six momenta vanish.

**Why the order decides.** A first-order action carries one rate per coordinate at most; a coordinate whose rate is absent has zero momentum and its equation is a constraint. A second-order action carries a rate squared, so the momentum is linear in the rate and vanishes only where the metric degenerates. The metric here is built from $\cosh$ and $\sinh$, and it is non-degenerate for every finite rapidity.

**What the fluid gains from the absence.** No Dirac bracket, no reduced phase space, no constraint surface. The fluid's two equations are the field's, and the frame's six are the field's, and the count is eight and eight. The relativistic scalar fluid is therefore the one rung of the three at which the fluid reading needs no constraint analysis, and that is a statement about the order of the action and not about the algebra.

## The Noether Currents: Stress, Charge and No Spin

**Translation** gives the stress, and the polar companion computes it as the chart's energy–momentum. Its two pieces are the frame's sigma-model term and the mass term, and the cross terms of the metric are what make it differ from the canonical tensor of the element form.

**Phase shift** gives the charge current, and the charge current is continuity's. The identification of the two is exact: the phase's equation is the conservation of the phase's momentum, and the phase's momentum is the current.

**There is no spin current.** The rotor's momentum is not zero — the action is second order and every coordinate is canonical — but the rotor is not a spin direction. At the scalar rung the rotor rotates the field's value and carries no angular momentum of its own, and the corpus's spin-half article is where the rotor becomes a spin. A fluid whose rotor is canonical and not a spin is a fluid with an orientation and no spin dynamics, and that is what the relativistic scalar fluid is.

## What the Alternative Route Adds and What It Relabels

**Adds.** The exact statement that the pair closes only where the frame is frozen, and that the frame is what carries the rapidity's gradient into the mass shell. The on-shell identification $\cosh\theta_{\mathrm{rpd}}=E/(mc^{2})$, which makes the chart's rapidity the flow's Lorentz factor. The count of eight and eight against the first-order rungs' eight and two. And the location of the mass term as an algebraic object that supplies a mass shell and a stress and no metric.

**Does not add.** No new equation; the pair is the relativistic Madelung pair and the article says so. No new solution. The frame's explicit equations in the operator setting are stated structurally; the polar companion does not print the general Jacobian and this article does not either.

**Relabels.** The phrase "the mass shell is a constraint". Under the equation route the shell is a condition imposed on the velocity. Under the action route it is the variation of the scale, and its status as an equation of motion is what [The Lagrangian and the Spin-Zero Fluid](the-lagrangian-and-the-spin-zero-fluid.html) already establishes in two variables. The eight-coordinate version adds that the shell is one of eight and that the other six are the frame's.

## Open Questions

**The frame's gradients.** The operator-setting action's gradient terms in the six frame coordinates are not computed. Whether their variation closes into a transport law with a closed form is the same open item the polar companion records for the general Jacobian.

**The sign of the stress's mass term.** The mass term's contribution to the pressure is stated here by structure and not by display. A reader who needs the display has the stress-tensor article; whether the polar action's translation current reproduces it without an improvement is not settled in this article.

## Summary

The polar action of the Klein–Gordon field is second order and regular, and its eight equations are the fluid's. The phase's equation is continuity for the charge current, with the proper density carried by the four-velocity. The scale's equation is the mass shell with the quantum potential, and on the general word it carries the rapidity's gradient as a source. The frame's six equations are the transport of the boost and the rotor, and they are what the pair needs where the frame is not frozen. No momentum vanishes, so no constraint analysis is required — the one rung of the three where that is true. The article adds no equation and no solution; it adds the assignment of each fluid statement to one coordinate, the on-shell identity that makes the chart's rapidity the flow's Lorentz factor, and the exact statement of where the pair closes.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\tilde\Xi$ | the field, an $N$-regular biquaternion |
| $\varrho$, $\theta_{\mathrm{pha}}$, $\theta_{\mathrm{rpd}}$, $\theta_{\mathrm{axr}}$ | scale, phase, rapidity, rotor angle |
| $\vec u_{\mathrm b}$, $\vec u_{\mathrm r}$ | boost and rotor axes |
| $\rho_{\mathrm{num}}=\varrho^{2}$ | proper density |
| $\gamma=\cosh\theta_{\mathrm{rpd}}$ | Lorentz factor; equals $E/(mc^{2})$ on shell |
| $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$ | charge density |
| $S_{\tilde\Xi}=\frac{h}{2\pi}\theta_{\mathrm{pha}}$ | action variable |
| $\tilde V_\Phi=\tilde\nabla_\Phi S_{\tilde\Xi}/m$ | four-velocity |
| $\mathcal A_{\imath}=\tilde\Xi^{-1}\partial_{\imath}\tilde\Xi$ | four-type bracket |
| $G^{ab}$ | parameter metric, $\cosh$ on the squares and $\sinh$ on the cross terms |
| $Q_{\mathrm{qnt}}$ | $-\frac{h^{2}}{4\pi^{2}}\Box_\Phi\varrho/(2m\varrho)$ |
| $\nu_m$ | $mc/h$ |

## Further Reading

- Erwin Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1927) 322–326, for the non-relativistic pair and its variational principle.
- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, for the relativistic spin-zero fluid and its mass shell.
- Fritz London, "Superfluids" (Wiley, 1950), volume 1, for the relativistic scalar fluid and the indefiniteness of its charge density.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), for the covariant Madelung pair and its quantum potential.
