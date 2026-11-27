# __The Charged Klein–Gordon Fluid from the Polar Action: Two Shifted Slots and the Frame Untouched__

## Introduction

[The Charged Spin-Zero Fluid](the-charged-spin-zero-fluid.html) reads the coupled Klein–Gordon equation and finds that the vorticity is the field strength and the charge density is the time component of the current. [The Lagrangian and the Coupled Klein–Gordon Equation in Polar Variables](the-lagrangian-and-the-coupled-klein-gordon-equation-in-polar-variables.html) writes the coupled action in the eight coordinates and reports that the connection shifts two slots and spares the frame.

This article varies that action and reads the equations as the charged fluid's. The result is exact and it is a contrast with the rung below: **at the second-order rung the connection reaches two brackets, the phase's in space and the scale's in time, and those two are precisely the two the fluid uses.** So the fluid's equations become covariant by one substitution and acquire no new term, and the frame's six equations are untouched.

**Why the two brackets and not one.** The addition to the logarithmic derivative is $\frac{2\pi iϙ}{h}\tilde A_\Phi$, and the connection is material, $\tilde A_\Phi=i a'_t e_t+\vec A$ with real components. Multiplying by the central $i$ therefore gives a real central number in the temporal slot and an imaginary one in the spatial slots. The same connection reaches the scale's bracket in time and the phase's bracket in space, and that is a fact about the connection's own form and not about the field.

**What the rungs' contrast amounts to.** At the Schrödinger rung the action's derivative is temporal only, so the connection reaches the phase alone and the continuity equation's coefficient is untouched. Here the derivative is four-dimensional, so the connection reaches the scale as well, and the mass shell becomes the mechanical one. The two rungs are one substitution read at two orders, and the difference between them is which slots the action has.

**The strongest objection.** *A shift of two brackets is a rewriting of minimal coupling and nothing more; the article is a change of letters.* The objection is right about the physics and wrong about what the article claims. Minimal coupling is standard and the corpus says so. What is not standard is the location: the shift sits in two of the four types, it cannot reach the other two, and the two it reaches are the fluid's two equations. That is why the charged scalar fluid is a fluid with a charge and no spin, and the reason is a type argument rather than a computation.

**Position in the block.** This is the variational companion of [The Charged Spin-Zero Fluid](the-charged-spin-zero-fluid.html) and the coupled member of the pair whose free member is [Klein–Gordon Fluid Equations from the Polar Action](klein-gordon-fluid-equations-from-the-polar-action.html).

## Conventions

**The conventions are the free polar companion's, restated for the coupled article.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_{\imath}^{2}=-e_t$; $i$ central; $^{*}$ Hermitian, $^{\natural}$ quaternionic; $\mathrm{Sc}$ the coefficient of $e_t$; the pairing $\mathrm{Sc}(\cdot^{*}\cdot)$. The word and the ranges are the free article's. The density is $\rho_{\mathrm{num}}=\varrho^{2}$, the Lorentz factor is $\gamma=\cosh\theta_{\mathrm{rpd}}$, and the charge density is $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$.

The connection and the coupling. $\tilde A_\Phi=i a'_t e_t+\vec A$ with $a'_t$ and $\vec A$ real, $ϙ$ the coupling with $q=-ϙ$, and

$$
\tilde\nabla_{\mathrm{gco},\Phi}=\tilde\nabla_\Phi+\frac{2\pi i\,ϙ}{h}\tilde A_\Phi,
\qquad
\mathcal A^{\mathrm{gco}}_{\imath}=\tilde\Xi^{-1}\tilde\nabla_{\mathrm{gco},\Phi,\imath}\tilde\Xi=\mathcal A_{\imath}+\frac{2\pi i\,ϙ}{h}A_{\imath}.
$$

The mechanical momentum and energy are $\vec\pi=\vec p-q\vec A$ and $\mathcal E=E-ϙ\omicron_{\mathrm{pot}}$, with $\omicron_{\mathrm{pot}}=c\,a'_t$. Time is $r'_t=c\,t'$, $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial r^{\prime 2}_{t}$, and $\nu_m=\frac{mc}{h}$.

## The Action in the Word

The functional. The polar companion's action is the free polar action with the bracket replaced,

$$
S=\int\mathrm{d}^{4}x\;\Bigl\{\mathrm{Sc}\Bigl[\tilde\Xi^{*}\tilde\Xi\,\mathcal A^{\mathrm{gco}}_{\imath}\bigl(\mathcal A^{\mathrm{gco}}_{\imath}\bigr)^{*}\Bigr]-\mathrm{Sc}\bigl(\tilde\Xi^{*}\tilde\Xi\bigr)\,4\pi^{2}\nu_m^{2}\Bigr\},
$$

summed over the four slots with the metric signs.

**The shift is additive, and that is the whole of the substitution.** The connection is a multiple of the identity in the frame's own basis, so it adds to the bracket and multiplies nothing. The weight $\tilde\Xi^{*}\tilde\Xi$ is built from the frame and the scale, and it cannot see a central addition. The mass term carries no derivative, so it cannot see one either. The action therefore separates into the free action plus a linear term in $A$ plus a quadratic one.

**The three pieces.** Expanding,

$$
\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde\Xi\,\mathcal A^{\mathrm{gco}}\bigl(\mathcal A^{\mathrm{gco}}\bigr)^{*}\bigr]
=\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde\Xi\,\mathcal A\mathcal A^{*}\bigr]
+\frac{2\pi i\,ϙ}{h}\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde\Xi\bigl(A\mathcal A^{*}-\mathcal A A\bigr)\bigr]
+\frac{(2\pi)^{2}ϙ^{2}}{h^{2}}\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde\Xi\bigr]A^{2}.
$$

The first is the free kinetic term, the second is the interaction, and the third is the term that a presentation writing "current times potential" omits. The third is what makes the action invariant under the local transformation, and it is also what makes the stress gauge-invariant.

**The two slots.** In the temporal slot the addition is real, so it joins the scale's bracket. In the three spatial slots it is imaginary, so it joins the phase's. It reaches the boost's bracket and the rotor's bracket nowhere, and the reason is that those two are non-central in the frame's basis while the addition is central in every slot.

## The Variation: Continuity, Covariant by One Substitution

Varying $\theta_{\mathrm{pha}}$. The phase appears in the bracket's central imaginary part, and in the temporal slot the connection has gone to the scale's part and not to the phase's. The Euler–Lagrange equation is therefore

$$
\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}\frac{\partial\mathcal L}{\partial(\partial_{\imath}\theta_{\mathrm{pha}})}=0
\qquad\Longrightarrow\qquad
\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}\bigl(\rho_{\mathrm{num}}V^{\mathrm{gco}}_{\Phi,\imath}\bigr)=0,
$$

with $V^{\mathrm{gco}}_{\Phi,\imath}$ the mechanical four-velocity. On the central class this is

$$
\partial_{r'_t}\rho_{\mathrm{num}}+\vec\nabla_\Phi\cdot\bigl(\rho_{\mathrm{num}}\vec v\bigr)=0,
\qquad
\vec v=\vec\pi/m,
$$

which is the charged scalar fluid's continuity equation.

**Three statements.**

*Continuity is unchanged in form and shifted in content.* The divergence is an ordinary one and the current is the mechanical one. No source term appears, because the connection is not in the phase's temporal coefficient; it is in the phase's spatial coefficient and in the scale's temporal one, and both are inside the current.

*The conserved density is the proper density, and the conserved charge is the time component of the same current.* $\rho_{\mathrm{chg}}=\rho_{\mathrm{num}}E/(mc^{2})$ on shell, and the sign is the energy's. That is the relativistic rung's defect and the coupling does not repair it, as the charged spin-zero article records.

*The equation is not the Lorenz condition.* The Lorenz condition is the divergence of the potential; this is the divergence of the current. At this rung the two are related by the equation of motion and are not the same object, and the vector rung is where the distinction becomes damaging.

## The Variation: The Mass Shell Becomes Mechanical

Varying $\varrho$. The scale's bracket now carries the connection in the temporal slot, so the scale's variation produces a mass shell in the mechanical energy,

$$
\sum_{\imath}\varepsilon_{\imath}\pi_{\imath}\pi_{\imath}=-m^{2}c^{2}-\frac{2mQ_{\mathrm{qnt}}}{c^{2}},
\qquad
Q_{\mathrm{qnt}}=-\frac{h^{2}}{4\pi^{2}}\frac{\Box_\Phi\varrho}{2m\varrho},
$$

with $\pi_{r'_t}=\mathcal E/c$ and $\vec\pi$ the mechanical momentum.

**The derivation, and the one place it could fail.** The scale appears in the weight and in the mass term, and the weight multiplies the bracket's square. A shift inside the square produces a term linear in the scale's variation only through the cross term between the shift and the scale's own rate — and in the temporal slot that cross term is $\varrho\,\delta\varrho$ times the connection times the scale rate, which is a total derivative after integration by parts and vanishes for compact support. So the shift enters the mass shell as a substitution of the momentum and not as a new term. **That is the calculation the article rests on, and it is why the mass shell stays a mass shell.**

**What the coupling does to the guidance.** It replaces the canonical momentum by the mechanical one and leaves the quantum potential alone. The quantum potential is the variation of $\lvert\vec\nabla_\Phi\varrho\rvert^{2}$, which carries no connection, as at the rung below. The charged scalar fluid's guidance is therefore the free guidance with the mechanical momentum, and the Lorentz force appears in it through $\vec\pi$ and not as an added term.

**The honesty about the force.** A reader who wants the Lorentz force as a displayed term will not find it here, and the reason is that it is not a term: it is what the mechanical momentum does when the mass shell is differentiated. The charged spin-zero fluid article says the same thing in the equation route's language, and it is the point at which the two routes agree most visibly.

## The Frame's Equations: Untouched, and the Vorticity

**The frame is spared.** The connection reaches neither the boost's bracket nor the rotor's, so the six frame equations are the free ones with the mechanical momentum in place of the canonical. The count is unchanged: eight coordinates, eight second-order equations, no vanishing momentum.

**The vorticity, from the chart.** The four-velocity is $\tilde V^{\mathrm{gco}}_\Phi=\tilde\pi/m$, and the field strength is the curl of the connection. In the chart the velocity's curl is

$$
\partial_{\imath}V^{\mathrm{gco}}_{\jmath}-\partial_{\jmath}V^{\mathrm{gco}}_{\imath}
=\frac{1}{m}\bigl(\partial_{\imath}\pi_{\jmath}-\partial_{\jmath}\pi_{\imath}\bigr)
=\frac{q}{m}F_{\imath\jmath}+\frac{1}{m}\bigl(\partial_{\imath}\partial_{\jmath}-\partial_{\jmath}\partial_{\imath}\bigr)S_{\tilde\Xi},
$$

and the second term is the curl of a gradient and vanishes identically on the central class. So on the central class the vorticity is the field strength up to the coupling, which is the charged spin-zero fluid's identity.

**What the identity costs at this rung.** The velocity is a four-vector whose norm the mass shell fixes, so the vorticity's rank is not bounded by two as it is at the non-relativistic rung. The identity therefore reaches rank four whenever $\vec E\cdot\vec B\ne0$, and the fluid's vorticity is not a simple two-form. The action route shows where the difference comes from: the norm is a second-order object, and a second-order object's curl is not constrained by the dimension of the rest space.

## The Constraints: None, and the One Redundancy

**No constraint.** The action is second order and regular, as in the free case, and the coupling does not change the metric because it is a shift and not a factor. The Hessian is non-degenerate for every finite rapidity, and the Legendre transform is regular.

**One redundancy appears.** The local transformation translates the phase and shifts the connection, and the pair is invariant. In the chart it is a translation of one coordinate compensated by a shift of $\tilde A_\Phi$, exactly as at the first-order rung. The Noether charge is the phase's momentum, which is the charge density.

**The two statements are one.** The charge is the phase's conjugate momentum, and it is the source the connection's own equation needs. The action route shows this in one line: the phase enters only through its covariant gradient, so the current is the coefficient and the symmetry is the translation.

## The Noether Currents: Charge, Stress, No Spin

**Charge.** The phase shift gives $\tilde J_\Phi=\rho_{\mathrm{num}}\tilde\pi/m$, which is continuity's current, and it is the source of the connection's equation.

**Stress.** Translation gives the stress, and the coupling enters in three places: the mechanical momentum in the dust term, the linear term in $A$ which is a total derivative on shell, and the quadratic term which is what makes the stress gauge-invariant. The polar companion's remark that the quadratic term is what makes the action invariant is the same remark.

**No spin.** The rotor's bracket is untouched, and the rotor is not a spin direction at this rung. The charged scalar fluid is a charged fluid without spin, and the action says so by one type: the addition is central and the rotor's bracket is not.

## What the Alternative Route Adds and What It Relabels

**Adds.** The location of the coupling in two brackets and the reason it is two and not one — the signature of the temporal slot. The exact statement that the shift enters the mass shell as a substitution and not as a term, with the integration by parts that makes it so. The statement that the frame's six equations are untouched, which the two-field chart cannot state because it has no frame. And the reason the quantum potential is charge-blind, as at the rung below but now with the scale's bracket in the argument.

**Does not add.** No new equation, no new solution. Minimal coupling is standard and the polar companion says so. The free article's open item, the explicit frame gradients, remains open with covariant letters.

**Relabels.** "The vorticity is the field strength." On the equation route it is a theorem about solutions with a qualification about rank. On the action route it is a statement about the velocity's definition, and the qualification about rank is a statement about the order of the action.

## Open Questions

**The frame's gradients under coupling.** Whether the operator-setting gradient terms in the frame's six coordinates acquire any connection term. The type argument says no, and a computation would settle it.

**The interaction's second term.** The linear term in $A$ is a total derivative on shell. Whether it is a total derivative off shell, and therefore whether the interaction's energy is the quadratic term alone, is not stated here and is worth a display.

## Summary

The coupled polar action of the Klein–Gordon field varies into the charged scalar fluid's equations. The connection is a central imaginary addition, so it joins the scale's bracket in the temporal slot and the phase's in the spatial ones, and those two are the fluid's two equations: continuity with the mechanical current, and the mass shell with the mechanical momentum and an unchanged quantum potential. The shift enters the mass shell as a substitution and not as a new term, by one integration by parts. The frame's six equations are untouched, so the charged scalar fluid is a charged fluid without spin. The article adds the location of the coupling and the reason for it, and it adds nothing to the equations.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\tilde A_\Phi=i a'_t e_t+\vec A$ | external connection |
| $ϙ$, $q=-ϙ$ | coupling and electric charge |
| $\mathcal A^{\mathrm{gco}}_{\imath}$ | $\mathcal A_{\imath}+\frac{2\pi iϙ}{h}A_{\imath}$ |
| $\vec\pi=\vec p-q\vec A$, $\mathcal E=E-ϙ\omicron_{\mathrm{pot}}$ | mechanical momentum and energy |
| $\rho_{\mathrm{num}}=\varrho^{2}$, $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$ | proper and charge densities |
| $V^{\mathrm{gco}}_\Phi=\tilde\pi/m$ | mechanical four-velocity |
| $F_{\imath\jmath}$ | field strength, the curl of the connection |
| $Q_{\mathrm{qnt}}$ | $-\frac{h^{2}}{4\pi^{2}}\Box_\Phi\varrho/(2m\varrho)$, charge-blind |

## Further Reading

- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, for the relativistic spin-zero fluid.
- Fritz London, "Superfluids" (Wiley, 1950), volume 1, for the charged scalar fluid and the vorticity-field identity.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), for the covariant Madelung pair with an external field.
- Vitaly L. Ginzburg and Lev D. Landau, "On the theory of superconductivity," *Zhurnal Eksperimental'noi i Teoreticheskoi Fiziki* **20** (1950) 1064–1082, for the vorticity of a charged condensate and the qualification its rank carries.
