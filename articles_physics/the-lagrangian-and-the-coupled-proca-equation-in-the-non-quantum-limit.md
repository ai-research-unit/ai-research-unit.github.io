# __The Lagrangian and the Coupled Proca Equation in the Non-Quantum Limit__

**Declared omissions.** The reality of the action is settled inside the action section and not in a section named for it, so slot 5 is omitted. The limit adds no constraint beyond the one the parent imposes, so slot 6 is omitted. The second variation is not computed, so slot 8 is omitted. The two settings are not contrasted, so slot 10 is omitted. No comparison beyond the parent is attempted, so slot 13 is omitted. No open question is separated from the verification, so slot 14 is omitted.

## Introduction

**The finding, in one sentence.** The same deletion that fails in the free Proca action succeeds in the coupled one, because the complex carrier puts the oscillation in the phase and leaves the amplitude an envelope whose kinetic term is genuinely small.

**The action.** The covariant Proca action with the complex word substituted,

$$
S=\int\mathrm{d}^{4}\varrho\;\Bigl\{\tfrac12\sum_\mu\varepsilon_\mu\bigl(\partial_\mu \varrho\bigr)^{2}
+\tfrac12\varrho^{2}\sum_\mu\varepsilon_\mu\bigl(\kappa^{\mathrm{kin}}_\mu\bigr)^{2}
-\tfrac12k_m^{2}\varrho^{2}\,\mathcal{V}
+\text{(the frame's terms)}\Bigr\},
$$

with $\kappa^{\mathrm{kin}}_\mu=\partial_\mu\theta_{\mathrm{pha}}+\frac{q}{\hbar}A_\mu$ the mechanical phase gradient and $\mathcal V$ the invariant length's frame factor. **Three blocks and the same four brackets as the Dirac chart.**

**The two blocks that decide the article, and their orders.** The amplitude's kinetic term is order two; the mass term is order zero; the phase's bracket is order zero. **So the deletion of the amplitude's kinetic term is a deletion across two orders**, which is what makes it controlled.

**Why the same deletion failed in the free companion.** There the field was real, the phase unavailable, and the oscillation in the amplitude. **The amplitude's kinetic term was then of the same size as the mass term**, so deleting it was not an approximation. **The two actions are the same action; the two limits differ because the two words differ.**

**The exactness on a plane wave, which is the sharpest illustration.** For $\tilde A=A_0e^{i(\vec k\cdot\vec r-\omega r'_{t})}\tilde U$ with constant $A_0$ and $\tilde U$, the amplitude's kinetic term vanishes identically. **The truncated action therefore reproduces every constant-envelope plane wave exactly**, and its corrections are what a varying envelope costs.

**What the article establishes, in five sentences.** The coupled Proca action's amplitude block is order two and the mass and phase blocks are order zero, so the deletion is controlled by $\epsilon$. The variation of the phase returns the covariant transport equation, which is the continuity equation and is exact in the pair; the variation of the amplitude returns the mechanical mass shell as a constraint; the variation of the frame returns the polarisation's transport. On a constant-envelope plane wave the deleted term vanishes identically, so the limit is exact there and its error is the envelope's curvature. The mass term's frame factor is not displayed in closed form in the six angles, so the frame's variation is exact as a system and not as a formula.

**What is not new.** The covariant Proca action, the minimal substitution, the transverse polarisation and the Madelung-like pair are standard. Added here: the comparison of the two Proca deletions in one ledger, the exactness statement on constant envelopes, and the reading of the free/coupled split as a split of carriers.

**The restriction.** The word is defined for $\varrho>0$; the limit is a statement on the chart's domain; the cone is $\varrho=0$.

## Conventions

**The conventions are the corpus's, restated here so that every sign below is checkable from this page alone.** Those of the coupled polar variational parent: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_{t}=1$ and $\vec e_\mu^{2}=-e_{t}$; $\mathrm{Sc}$ the coefficient of $e_{t}$; $\tilde\nabla_{\mathrm{gco},\Phi,\mu}=\partial_\mu+iq\tilde A_\mu/\hbar$; the complete polar decomposition $\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$; $\varepsilon_\mu$ the metric signs; $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial r_{t}^{\prime\,2}$; $k_m=mc/\hbar$; $\epsilon=1/(\pi_{\Phi}L)$.

## The Blocks

| block | derivative count | order |
|---|---|---|
| $\tfrac12\sum_\mu\varepsilon_\mu(\partial_\mu \varrho)^{2}$ | two on the amplitude | $2$ |
| $\tfrac12\varrho^{2}\sum_\mu\varepsilon_\mu(\kappa^{\mathrm{kin}}_\mu)^{2}$ | two on the phase | $0$ |
| $-\tfrac12k_m^{2}\varrho^{2}\mathcal V$ | none, but depends on the frame | $0$ |
| the frame's terms | two on the frame's connections | $2$ |

**One order-two block is deleted and one is kept.** The amplitude's is deleted; the frame's is kept, because the frame's connection is the velocity and the polarisation and its transport is the limit's order one. **So the deletion is one block and not "the curvatures"**: the amplitude's curvature goes and the frame's stays.

**Why the asymmetry.** The amplitude is the envelope and its curvature is $\epsilon^{2}$ against the mass term. The frame's curvature is the transport law's own content and removing it would remove the dynamics. **The two curvatures are of the same order and their fates differ because of what they are**, which is a statement a term count alone cannot make.

## The Three Variations

**Varying the phase.** The covariant transport,

$$
\partial_{r'_{t}}\bigl(\rho_{\mathrm{num}}\,\mathcal E/c\bigr)+\vec\nabla_\Phi\cdot\bigl(\rho_{\mathrm{num}}\,\vec\pi\bigr)=0,
\qquad
\vec\pi=\hbar\vec\kappa ,
$$

the continuity equation for the charge density and the mechanical current. **It is exact in the pair and unchanged by the deletion**, because the deleted block carries no phase.

**Varying the amplitude.** With the kinetic block deleted,

$$
\sum_\mu\varepsilon_\mu\bigl(\kappa^{\mathrm{kin}}_\mu\bigr)^{2}+k_m^{2}\mathcal V=0
\qquad\Longleftrightarrow\qquad
\frac{\mathcal E^{2}}{c^{2}}-\lvert\vec\pi\rvert^{2}=m^{2}c^{2}\mathcal V ,
$$

the mass shell with the frame factor on the right. **Keeping the block would add $\Box_\Phi \varrho/\varrho$ to the right**, which is the quantum potential and is order two.

**Varying the frame.** The polarisation's transport, from the frame's own terms and from $\mathcal V$'s dependence on the angles. **The parent does not display the general invariant length in closed form in the six angles**, so the variation is exact as an Euler–Lagrange equation and not as a formula.

**What the three variations give together.** A constraint, a transport, and a transport — the same three-plus-one structure as the free chart, now with the phase's bracket available and therefore with a genuine guidance equation among them.

## The Structural Consequence: The Coupling Reaches the Constraint and Not the Mass

**Two brackets out of four, and the two are the ones that matter.** The potential is central with a temporal and a spatial slot, so it enters the amplitude's covariant derivative and the frame's transport. It does not enter the mass block, which is a function of $\varrho$ and the frame alone, and it does not enter the rotor, which is a real vector part.

**The consequence.** The Lorenz condition is covariantised, because it is the scalar part of a covariant divergence; the mass shell is not, because the mass term is unchanged; and the spin direction is not, because the connection cannot reach it. Those three statements are the article's ledger, and they are exact: no approximation enters, since the coupling is a substitution in the derivative.

**The hand check.** Set the connection to a pure gradient, $\tilde A_\Phi=\partial\Lambda$. The covariant derivative shifts by a central element, the field strength is unchanged, and the constraint's scalar part is unchanged, because the extra term is a divergence. The mass block never sees the connection at all. So the gauge orbit is a direction in which only the phase moves, and the structural three-way split is visible in one choice.

## The Deletion in the Proca Pair

**The ledger across the two Proca articles.**

| action | carrier | deleted block | ratio to kept blocks | exact on |
|---|---|---|---|---|
| free Proca | real | $\tfrac12(\partial \varrho)^{2}$ | order one | nothing |
| coupled Proca | complex | $\tfrac12(\partial \varrho)^{2}$ | $\epsilon^{2}$ | constant envelopes |

**The same block, two verdicts, and the difference is the word's second factor.** A complex word's phase absorbs the oscillation, so the amplitude's gradient is a slow gradient; a real word has no phase and the amplitude's gradient is the oscillation itself.

**The exactness row deserves its sentence.** On a constant envelope the deleted term is identically zero, so the truncated action is not an approximation there but the same functional. **The limit's error is exactly the envelope's curvature and nothing else**, and that is the strongest statement available in the family.

## The Noether Currents: The Conserved Charge of the Coupled Chart

**The charge exists once the potential is complex.** The free Proca field has no phase symmetry; the coupled one does, because the potential is complex and the phase rotation is compensated by the connection. So the charge appears with the coupling and not before it, and its density is the phase's conjugate momentum,

$$
\rho_{\mathrm{ch}}=q\,\varrho^{2}\cosh\theta_{\mathrm{rpd}}=q\,N ,
$$

with $q$ the parent's charge.

**Why the coupling creates it.** In the free theory the phase is not a variable; in the coupled theory it is, and the connection absorbs its gradient. The Noether procedure then returns the current that the connection multiplies in the action, which is the same object the element article calls the source. The identity of current and source is therefore a statement about the variation, and the limit does not weaken it.

**The mass in the energy only.** As in every family of the corpus, the charge carries no mass and the energy carries the mass squared. The limit's contribution is that both survive with their signs intact, and that the constraint the coupling covariantises is the one that removes the fourth degree of freedom.

## What the Variational Route Adds

**Adds.**

*The deletion's verdict as a coefficient comparison.* Two blocks with the same derivative count, one deleted and one kept, and the reason stated: the amplitude's curvature is small and the frame's is the dynamics.

*The exactness on constant envelopes.* A statement that no order-counting argument can make, because it is about a class of solutions and not about a term.

*The pair of Proca articles' contrast as one ledger.* The free and coupled actions differ by the word, and the ledger shows where.

**Does not add.**

*No closed mass term.* The invariant length's dependence on the six angles is not displayed, so the frame's variation stays formal.

*No constraint algebra.* As in the Dirac variational article, the constraint structure's closure is not examined.

*No derivation of the force.* The Lorentz force is read from the shell's gradient and not from the action.

## Verification

**The orders were checked from the blocks.** The amplitude's kinetic term carries two derivatives on $\varrho$; the phase's bracket carries two on the phase and none on the scale; the mass term carries none. **The counts are an inspection and they are exact.**

**The amplitude block's vanishing was checked on a plane wave.** For constant $A_0$ and constant $\tilde U$ the word's scale is $\varrho=\lvert A_0\rvert$, so $\partial_\mu \varrho=0$ and the block vanishes identically. **The truncated action is then the full action**, which is the exactness claim.

**The pair's transport was checked to be unchanged by the deletion.** The deleted block contains no phase and no potential, so both functional derivatives with respect to $\theta_{\mathrm{pha}}$ are the same expression. **No rearrangement is needed.**

**The mass shell was checked to follow from the amplitude's variation.** With the kinetic block deleted, the variation gives $\sum_\mu\varepsilon_\mu(\kappa^{\mathrm{kin}}_\mu)^{2}+k_m^{2}\mathcal V=0$, which is $\mathcal E^{2}/c^{2}-\lvert\vec\pi\rvert^{2}=m^{2}c^{2}\mathcal V$; keeping the block adds $\Box_\Phi \varrho/\varrho$. **The two differ by the deleted block and by nothing else.**

**What was not checked.** No closed form for $\mathcal V$ in the six angles was derived, and no solution of the order-one system was integrated. **The first omission is the parent's and is recorded as such.**

## Summary

The coupled Proca action's blocks are ordered by derivative count: the amplitude's kinetic term is order two, the phase's bracket and the mass term are order zero, and the frame's terms are order two. The limit deletes the amplitude's kinetic block and keeps everything else.

The deletion is controlled here because the complex carrier's phase absorbs the oscillation and leaves the amplitude an envelope. **On a constant envelope the deleted block vanishes identically, so the limit is exact there** and its error is the envelope's curvature.

The three variations give the covariant transport, the mass shell with the frame factor, and the polarisation's transport. **The pair is unchanged by the deletion and the shell gains the quantum potential only when the block is kept.**

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
