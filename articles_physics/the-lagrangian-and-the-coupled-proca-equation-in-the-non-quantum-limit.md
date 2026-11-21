# __The Lagrangian and the Coupled Proca Equation in the Non-Quantum Limit__

## Introduction
The same deletion that fails in the free Proca action succeeds in the coupled one, because the complex carrier puts the oscillation in the phase and leaves the amplitude an envelope whose kinetic term is genuinely small.

The covariant Proca action with the complex word substituted,

$$
S=\int\mathrm{d}^{4}\varrho\;\Bigl\{\tfrac12\sum_\mu\varepsilon_\mu\bigl(\partial_\mu \varrho\bigr)^{2}
+\tfrac12\varrho^{2}\sum_\mu\varepsilon_\mu\bigl(\kappa^{\mathrm{kin}}_\mu\bigr)^{2}
-\tfrac12k_m^{2}\varrho^{2}\,\mathcal{V}
+\text{(the frame's terms)}\Bigr\},
$$

with $\kappa^{\mathrm{kin}}_\mu=\partial_\mu\theta_{\mathrm{pha}}+\frac{q}{\hbar}A_\mu$ the mechanical phase gradient and $\mathcal V$ the invariant length's frame factor. Three blocks and the same four brackets as the Dirac chart.

The amplitude's kinetic term is order two; the mass term is order zero; the phase's bracket is order zero. **So the deletion of the amplitude's kinetic term is a deletion across two orders**, which is what makes it controlled.

There the field was real, the phase unavailable, and the oscillation in the amplitude. The amplitude's kinetic term was then of the same size as the mass term, so deleting it was not an approximation. **The two actions are the same action; the two limits differ because the two words differ.**

For $\tilde A=A_0e^{i(\vec k\cdot\vec r-\omega r'_{t})}\tilde U$ with constant $A_0$ and $\tilde U$, the amplitude's kinetic term vanishes identically. The truncated action therefore reproduces every constant-envelope plane wave exactly, and its corrections are what a varying envelope costs.

The coupled Proca action's amplitude block is order two and the mass and phase blocks are order zero, so the deletion is controlled by $\epsilon$. The variation of the phase returns the covariant transport equation, which is the continuity equation and is exact in the pair; the variation of the amplitude returns the mechanical mass shell as a constraint; the variation of the frame returns the polarisation's transport. On a constant-envelope plane wave the deleted term vanishes identically, so the limit is exact there and its error is the envelope's curvature. The mass term's frame factor is not displayed in closed form in the six angles, so the frame's variation is exact as a system and not as a formula.

The covariant Proca action, the minimal substitution, the transverse polarisation and the Madelung-like pair are standard. Added here: the comparison of the two Proca deletions in one ledger, the exactness statement on constant envelopes, and the reading of the free/coupled split as a split of carriers.

The word is defined for $\varrho>0$; the limit is a statement on the chart's domain; the cone is $\varrho=0$.
## Conventions
The conventions are restated here so that every sign below is checkable from this page alone. Those of the coupled polar variational parent: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_{t}=1$ and $\vec e_\mu^{2}=-e_{t}$; $\mathrm{Sc}$ the coefficient of $e_{t}$; $\tilde\nabla_{\mathrm{gco},\Phi,\mu}=\partial_\mu+iq\tilde A_\mu/\hbar$; the complete polar decomposition $\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$; $\varepsilon_\mu$ the metric signs; $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial r_{t}^{\prime\,2}$; $k_m=mc/\hbar$; $\epsilon=1/(\pi_{\Phi}L)$.
## The Action in the Non-Quantum Limit: The Blocks
| block | derivative count | order |
|---|---|---|
| $\tfrac12\sum_\mu\varepsilon_\mu(\partial_\mu \varrho)^{2}$ | two on the amplitude | $2$ |
| $\tfrac12\varrho^{2}\sum_\mu\varepsilon_\mu(\kappa^{\mathrm{kin}}_\mu)^{2}$ | two on the phase | $0$ |
| $-\tfrac12k_m^{2}\varrho^{2}\mathcal V$ | none, but depends on the frame | $0$ |
| the frame's terms | two on the frame's connections | $2$ |

One order-two block is deleted and one is kept. The amplitude's is deleted; the frame's is kept, because the frame's connection is the velocity and the polarisation and its transport is the limit's order one. So the deletion is one block and not "the curvatures": the amplitude's curvature goes and the frame's stays.

Why the asymmetry. The amplitude is the envelope and its curvature is $\epsilon^{2}$ against the mass term. The frame's curvature is the transport law's own content and removing it would remove the dynamics. The two curvatures are of the same order and their fates differ because of what they are, which is a statement a term count alone cannot make.

The ledger across the two Proca articles.

| action | carrier | deleted block | ratio to kept blocks | exact on |
|---|---|---|---|---|
| free Proca | real | $\tfrac12(\partial \varrho)^{2}$ | order one | nothing |
| coupled Proca | complex | $\tfrac12(\partial \varrho)^{2}$ | $\epsilon^{2}$ | constant envelopes |

The same block, two verdicts, and the difference is the word's second factor. A complex word's phase absorbs the oscillation, so the amplitude's gradient is a slow gradient; a real word has no phase and the amplitude's gradient is the oscillation itself.

On a constant envelope the deleted term is identically zero, so the truncated action is not an approximation there but the same functional. The limit's error is exactly the envelope's curvature and nothing else, and that is the strongest statement available in the family.

### The Limits and the Truncation’s Error

There is no small parameter, and the section has to say so first. The deleted block is the amplitude's kinetic term; the kept blocks are the frame's terms and the mass. At a plane wave the ratio of the deleted block to the mass term is not $\epsilon^{2}$ but a number of order one, and it is the same number at every time. **The truncation therefore has no error estimate, and the article's claim is that it has none.**

Why the ratio is of order one. The amplitude's gradient is the envelope's curvature, and a real carrier has no oscillation to separate from an envelope. The two derivatives of $\varrho$ are the same size as the mass when the envelope turns on the scale $1/k_m$, which is the only scale the theory has, so there is no regime in which the deletion is small.

What the error would be if it were small. Restoring the block adds the quantum potential to the amplitude's equation, with the density in the denominator. In the scalar family that term is the correction; here it is comparable to the term that was kept, which is the technical statement of the failure.

The article can still say which term is deleted and what the surviving equations are. It cannot say that the surviving theory approximates the parent, and every sentence about the truncated theory is restricted to that statement. That is the difference between this family and the scalar one, and the section exists to make the difference explicit rather than let a reader carry over the scalar's result.

No bound, no distance, no rate. The word "controlled" does not appear in the article's claims about this limit, and the section's job is to keep it out.

Why the deletion is still made. Because the surviving equations are the ones the corpus calls the non-quantum limit, and the reader is owed a statement of what that limit is even when it is not an approximation. The article separates the definition from the justification, and this section is where the justification fails and is said to fail.

Three equations and a constraint, all exact on the truncated functional. The variations of the truncated action give the frame's transport, the constraint that the scalar part of the conjugate gradient vanishes, and the mass-shell relation on the amplitude. They are exact solutions of the truncated action and not approximations to the parent's, and the article says exactly that and no more.

Varying the frame parameters gives the same equations as the parent's, because the frame's blocks were not touched. The frame's dynamics is therefore the parent's, and that is the one sector in which the truncation costs nothing.

The vanishing of the scalar part of the conjugate gradient is one of the three variations and carries no scale derivative, so it survives unchanged. The Proca field's constraint is exact in the truncated theory, which is why the article's constraint section can be read before the limit section without loss.

The truncated amplitude equation is the mass term's own stationarity, $\partial\varrho$-free, and it is the equation of a different theory. The article does not present it as an approximation to the parent's, and a reader who has followed the error section knows why.

Charge, energy and stress are the frame's first integrals and carry the parent's expressions. The charge has no mass in it and the energy has mass-squared, and both statements survive the truncation because neither integrates the deleted block.

Any claim that the truncated theory describes a solution of the Proca equation whose envelope varies. That class is outside the limit, and the article's one sentence about it is in this section.

## The Variation: Three of Them
Varying the phase. The covariant transport,

$$
\partial_{r'_{t}}\bigl(\rho_{\mathrm{num}}\,\mathcal E/c\bigr)+\vec\nabla_\Phi\cdot\bigl(\rho_{\mathrm{num}}\,\vec\pi\bigr)=0,
\qquad
\vec\pi=\hbar\vec\kappa ,
$$

the continuity equation for the charge density and the mechanical current. It is exact in the pair and unchanged by the deletion, because the deleted block carries no phase.

Varying the amplitude. With the kinetic block deleted,

$$
\sum_\mu\varepsilon_\mu\bigl(\kappa^{\mathrm{kin}}_\mu\bigr)^{2}+k_m^{2}\mathcal V=0
\qquad\Longleftrightarrow\qquad
\frac{\mathcal E^{2}}{c^{2}}-\lvert\vec\pi\rvert^{2}=m^{2}c^{2}\mathcal V ,
$$

the mass shell with the frame factor on the right. Keeping the block would add $\Box_\Phi \varrho/\varrho$ to the right, which is the quantum potential and is order two.

Varying the frame. The polarisation's transport, from the frame's own terms and from $\mathcal V$'s dependence on the angles. The parent does not display the general invariant length in closed form in the six angles, so the variation is exact as an Euler–Lagrange equation and not as a formula.

What the three variations give together. A constraint, a transport, and a transport — the same three-plus-one structure as the free chart, now with the phase's bracket available and therefore with a genuine guidance equation among them.

## The Constraints the Action Imposes: The Amplitude's Equation Is the Constraint

The block table decides which of the three variations returns a constraint. The amplitude's order-two block is deleted, so no term of the truncated density carries a time derivative of $\varrho$. Its Euler–Lagrange equation is therefore not an evolution equation: it determines the amplitude at each instant from the phase's gradient, the frame factor $\mathcal V$ and the connection, and it advances nothing.

That determination is the mass's statement. The only other place $\varrho$ appears is $-\tfrac12k_m^{2}\varrho^{2}\mathcal V$, which carries no derivative, so the amplitude is determined exactly where $k_m\neq0$. At $k_m=0$ the equation loses its right side and $\varrho$ becomes a variable that propagates: that difference is the whole distance between the massive chart's count and the massless one's.

The two transports are untouched, and the asymmetry is the limit's structure. The phase's transport and the frame's transport keep the terms the table marks and lose the deleted block's contribution, and both remain equations of motion. So the truncation moves the transports and leaves the constraint, and the deleted block is the only place where the two kinds of equation were mixed.

It is not a gauge condition: the mass term breaks the local invariance of the field the amplitude multiplies, so the constraint pairs with the inherited gauge condition rather than generating a transformation, and the count falls by one pair. It is not a Gauss law either, since no connection equation is varied in this limit, and the section claims neither.

## The Structural Consequence: The Coupling Reaches the Constraint and Not the Mass
Two brackets out of four, and the two are the ones that matter. The potential is central with a temporal and a spatial slot, so it enters the amplitude's covariant derivative and the frame's transport. It does not enter the mass block, which is a function of $\varrho$ and the frame alone, and it does not enter the rotor, which is a real vector part.

The Lorenz condition is covariantised, because it is the scalar part of a covariant divergence; the mass shell is not, because the mass term is unchanged; and the spin direction is not, because the connection cannot reach it. Those three statements are the article's ledger, and they are exact: no approximation enters, since the coupling is a substitution in the derivative.

Set the connection to a pure gradient, $\tilde A_\Phi=\partial\Lambda$. The covariant derivative shifts by a central element, the field strength is unchanged, and the constraint's scalar part is unchanged, because the extra term is a divergence. The mass block never sees the connection at all. So the gauge orbit is a direction in which only the phase moves, and the structural three-way split is visible in one choice.
## The Noether Currents: The Conserved Charge of the Coupled Chart
**The charge exists once the potential is complex.** The free Proca field has no phase symmetry; the coupled one does, because the potential is complex and the phase rotation is compensated by the connection. So the charge appears with the coupling and not before it, and its density is the phase's conjugate momentum,

$$
\rho_{\mathrm{ch}}=q\,\varrho^{2}\cosh\theta_{\mathrm{rpd}}=q\,N ,
$$

with $q$ the parent's charge.

Why the coupling creates it. In the free theory the phase is not a variable; in the coupled theory it is, and the connection absorbs its gradient. The Noether procedure then returns the current that the connection multiplies in the action, which is the same object the element article calls the source. The identity of current and source is therefore a statement about the variation, and the limit does not weaken it.

As in every family of the corpus, the charge carries no mass and the energy carries the mass squared. The limit's contribution is that both survive with their signs intact, and that the constraint the coupling covariantises is the one that removes the fourth degree of freedom.
## What the Principle Adds and What It Relabels: By the Variational Route
Adds.

*The deletion's verdict as a coefficient comparison.* Two blocks with the same derivative count, one deleted and one kept, and the reason stated: the amplitude's curvature is small and the frame's is the dynamics.

*The exactness on constant envelopes.* A statement that no order-counting argument can make, because it is about a class of solutions and not about a term.

*The pair of Proca articles' contrast as one ledger.* The free and coupled actions differ by the word, and the ledger shows where.

Does not add.

*No closed mass term.* The invariant length's dependence on the six angles is not displayed, so the frame's variation stays formal.

*No constraint algebra.* As in the Dirac Lagrangian article, the constraint structure's closure is not examined.

*No derivation of the force.* The Lorentz force is read from the shell's gradient and not from the action.
## Summary
The coupled Proca action's blocks are ordered by derivative count: the amplitude's kinetic term is order two, the phase's bracket and the mass term are order zero, and the frame's terms are order two. The limit deletes the amplitude's kinetic block and keeps everything else.

The deletion is controlled here because the complex carrier's phase absorbs the oscillation and leaves the amplitude an envelope. On a constant envelope the deleted block vanishes identically, so the limit is exact there and its error is the envelope's curvature.

The three variations give the covariant transport, the mass shell with the frame factor, and the polarisation's transport. The pair is unchanged by the deletion and the shell gains the quantum potential only when the block is kept.

**The same block is deleted in the free Proca action and there the deletion is not controlled**, because a real field's oscillation falls on the amplitude. The two articles' contrast is a contrast of carriers, and its ledger is two rows long.
## Summary of Notation
| Symbol | Meaning |
|---|---|
| $\tilde A=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The coupled word on the complex carrier |
| $\varrho>0$, $\rho_{\mathrm{num}}=\varrho^{2}$ | The scale; the density |
| $\kappa^{\mathrm{kin}}_\mu=\partial_\mu\theta_{\mathrm{pha}}+qA_\mu/\hbar$ | The mechanical phase gradient |
| $\hbar\vec\kappa=\vec\pi$, $\hbar c\kappa_t=\mathcal E$ | Mechanical momentum and energy |
| $\mathcal V$ | The invariant length's frame factor; not closed in the six angles |
| $k_m=mc/\hbar$ | The mass wave number |
| $\epsilon=1/(\pi_{\Phi}L)$ | The parameter of the amplitude's curvature |
| $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial r_{t}^{\prime\,2}$ | The d'Alembertian of the material sector |
## Further Reading
- [The Lagrangian and the Coupled Proca Equation in Polar Variables](the-lagrangian-and-the-coupled-proca-equation-in-polar-variables.html), the parent: the action, the blocks and the frame's factor.
- [The Coupled Proca equation in the Non-Quantum Limit](the-coupled-proca-equation-in-the-non-quantum-limit.html), the companion: the restored phase, the mass shell, the transverse polarisation and the tetrad.
- [The Lagrangian and the Proca Equation in the Non-Quantum Limit](the-lagrangian-and-the-proca-equation-in-the-non-quantum-limit.html), the free companion, where the same deletion is not controlled.
- [The Lagrangian and the Coupled Klein–Gordon Equation in the Non-Quantum Limit](the-lagrangian-and-the-coupled-klein-gordon-equation-in-the-non-quantum-limit.html), the scalar companion with the same three variations.
- [The Non-Quantum Limit of the Biquaternion Model](the-non-quantum-limit-of-the-biquaternion-model.html), for the parameter and the difference between the limit and the approximation.
## Verification
The amplitude's kinetic term carries two derivatives on $\varrho$; the phase's bracket carries two on the phase and none on the scale; the mass term carries none. The counts are an inspection and they are exact.

For constant $A_0$ and constant $\tilde U$ the word's scale is $\varrho=\lvert A_0\rvert$, so $\partial_\mu \varrho=0$ and the block vanishes identically. The truncated action is then the full action, which is the exactness claim.

The deleted block contains no phase and no potential, so both functional derivatives with respect to $\theta_{\mathrm{pha}}$ are the same expression. No rearrangement is needed.

With the kinetic block deleted, the variation gives $\sum_\mu\varepsilon_\mu(\kappa^{\mathrm{kin}}_\mu)^{2}+k_m^{2}\mathcal V=0$, which is $\mathcal E^{2}/c^{2}-\lvert\vec\pi\rvert^{2}=m^{2}c^{2}\mathcal V$; keeping the block adds $\Box_\Phi \varrho/\varrho$. The two differ by the deleted block and by nothing else.

No closed form for $\mathcal V$ in the six angles was derived, and no solution of the order-one system was integrated. The first omission is the parent's and is recorded as such.
