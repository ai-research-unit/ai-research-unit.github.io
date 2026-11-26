# __The Lagrangian and the Coupled Klein–Gordon Equation in the Non-Quantum Limit__

## Introduction
The limit in one sentence. Write the parent's coupled polar action, delete the scale's kinetic term — the same Lorentz scalar the free family deletes — and the two variations of what is left are the mechanical mass shell and the covariant transport equation.

The parent prints the action in the mechanical variables. [The Lagrangian and the Coupled Klein–Gordon Equation in Polar Variables](the-lagrangian-and-the-coupled-klein-gordon-equation-in-polar-variables.html) writes the action first in the general element with the covariant logarithmic derivative and then for the central field, where the connection appears in the phase's two brackets and nowhere else. The scale's block is untouched by the coupling, so the limit here is the free limit applied to a shifted phase.

The deletion is the free deletion, and it is one Lorentz scalar. $(\partial_{r'_{t}}\varrho)^{2}-\lvert\vec\nabla_\Phi \varrho\rvert^{2}$ is invariant under boosts of the material sector, and the connection does not enter it. The limit therefore commutes with the Lorentz group and with the symmetry group, because the deleted block is a scalar of both.

The coupling survives the truncation entire, and that is this article's point. The parent splits the interaction into a piece linear in the potential times the free phase rate and a piece quadratic in the potential with no phase. Both are order zero, because neither carries a derivative of the scale. So the truncation deletes no part of the interaction, and a reader who expected the potential to enter as a perturbation finds it in the leading term twice.

The quadratic piece is not optional, and the parent says why. It is the piece that makes the action bounded below — the quadratic term in the spatial bracket is positive for every $\vec A$ — and it is the piece that makes the action invariant under a local phase translation. A truncation that dropped it would destroy both properties, which is the variational form of the statement that the coupling is not a perturbation.

What the article establishes, in five sentences. The parent's central action has four blocks: the covariant phase bracket of order zero, the scale's kinetic term of order two, and the mass term of order zero, with the interaction distributed inside the first two of them. The single deletion removes the scale's kinetic term, which is a Lorentz scalar, so the truncated action is covariant. Varying the scale gives the mechanical mass shell as an algebraic constraint and varying the phase gives the covariant transport equation, unchanged term for term. The truncated action is $\varrho^{2}\left[\left(\partial_{r'_{t}}S+q\omicron_{\mathrm{pot}}/c\right)^{2}-\lvert\vec\pi\rvert^{2}-\nu_m^{2}\right]$, degenerate in the scale, and its content is charged relativistic dust.

What is not new. The covariant Madelung action, the interaction's two pieces, the boundedness argument and the Lagrange-multiplier form of the mass shell are all standard. Added here: the ordering of the parent's blocks with the interaction inside them, the statement that neither interaction piece is deleted because neither carries a scale derivative, and the reading of the truncated action as charged dust with the mechanical shell as its Hamiltonian.

The restriction is the parent's. The central field is $\theta_{\mathrm{rpd}}=0$ with the rotor a sign, and the class is invariant only under a central Hamiltonian. The limit is defined there, as in the other families.

The signs. The parent writes the coupling as $ϙ$ with $ϙ=-q$; its temporal bracket is $\partial_{r'_{t}}\theta_{\mathrm{pha}}-\frac{2\pi ϙ}{h}a'_{t}$ and its spatial bracket is $\vec\nabla_\Phi\theta_{\mathrm{pha}}+\frac{2\pi ϙ}{h}\vec A$. Every display here uses $q$, the electric charge, $\vec\pi=\vec\nabla_\Phi S-q\vec A$ and $\mathcal E=E-q\omicron_{\mathrm{pot}}$ with $E=-c\,\partial_{r'_{t}}S$, so the temporal bracket is $-\mathcal E/c$ and the free article's convention $\mathcal E=E-q\omicron_{\mathrm{pot}}$ is the one kept.
## Conventions
The conventions are restated here so that every sign below is checkable from this page alone. Those of the coupled variational polar parent: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_{t}=1$ and $\vec e_{\imath}^{2}=-e_{t}$; $\mathrm{Sc}$ the coefficient of $e_{t}$; the word $\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\varepsilon e_{t}$; $\tilde A_\Phi=i(\omicron_{\mathrm{pot}}/c)e_{t}+\vec A$; $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial r_{t}^{\prime\,2}$; $\rho_{\mathrm{num}}=\varrho^{2}$; $\nu_m=\frac{mc}{h}$; $\epsilon=1/(\pi_{\Phi}L)$ with $\pi_{\Phi}=\frac{2\pi \lvert\vec\pi\rvert}{h}$.
## The Action in the Non-Quantum Limit: The Blocks
The parent's action for the central field.

$$
S_{\mathrm{cpl}}=\int\mathrm{d}^{4}x\;\Bigl\{\varrho^{2}\Bigl[\Bigl(\partial_{r'_{t}}\theta_{\mathrm{pha}}+\frac{q}{h}\frac{\omicron_{\mathrm{pot}}}{c}\Bigr)^{2}-\Bigl\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}-\frac{q}{h}\vec A\Bigr\rvert^{2}\Bigr]
+\bigl(\partial_{r'_{t}}\varrho\bigr)^{2}-\lvert\vec\nabla_\Phi \varrho\rvert^{2}-4\pi^{2}\nu_m^{2}\varrho^{2}\Bigr\},
$$

the free action with the two covariant substitutions and the amplitude's two terms untouched.

The blocks and their orders.

| block | what it carries | order in $\epsilon$ |
|---|---|---|
| $\varrho^{2}\bigl(\partial_{r'_{t}}\theta_{\mathrm{pha}}+\frac{2\pi q}{h}\frac{\omicron_{\mathrm{pot}}}{c}\bigr)^{2}$ | scale squared, two derivatives of the phase | $0$ |
| $-\varrho^{2}\bigl\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}-\frac{2\pi q}{h}\vec A\bigr\rvert^{2}$ | scale squared, two derivatives of the phase | $0$ |
| $(\partial_{r'_{t}}\varrho)^{2}-\lvert\vec\nabla_\Phi \varrho\rvert^{2}$ | two derivatives of the scale | $2$ |
| $-\nu_m^{2}\varrho^{2}$ | scale squared, no derivative | $0$ |

The order is a property of the block and never of the potential. $q\vec A$ sits inside a bracket that carries two derivatives of the phase, and a potential does not change the bracket's derivative count. The coupling is leading and the table says so without an estimate.

The interaction's two pieces, and both are order zero.

$$
\varrho^{2}\Bigl(\partial_{r'_{t}}\theta_{\mathrm{pha}}\Bigr)^{2}-\varrho^{2}\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}\rvert^{2}
+\frac{2\pi 2q\varrho^{2}}{h}\Bigl(\partial_{r'_{t}}\theta_{\mathrm{pha}}\frac{\omicron_{\mathrm{pot}}}{c}+\vec\nabla_\Phi\theta_{\mathrm{pha}}\cdot\vec A\Bigr)
+\frac{(2\pi)^{2} q^{2}\varrho^{2}}{h^{2}}\Bigl(\Bigl(\frac{\omicron_{\mathrm{pot}}}{c}\Bigr)^{2}-\lvert\vec A\rvert^{2}\Bigr).
$$

The first interaction piece is the current times the potential and the second is the potential squared. The parent states both, and the second is the one a "current times potential" presentation omits. Both are order zero, so both are leading, so neither is a correction.

Why the quadratic piece cannot be dropped, in the parent's two reasons. It makes the kinetic part bounded below, because $-\lvert\vec A\rvert^{2}$ enters with a plus sign after the overall minus of the bracket; and it is what makes the action invariant under a local phase translation, because the potential's shift has to be compensated in a term quadratic in the potential. A truncation in powers of $q$ would break both, and that is why no such truncation is the non-quantum limit.

Delete the scale's block.

$$
S_{\mathrm{cl}}=\int\mathrm{d}^{4}x\;\varrho^{2}\Bigl[\Bigl(\partial_{r'_{t}}S+\frac{q\omicron_{\mathrm{pot}}}{c}\Bigr)^{2}-\lvert\vec\pi\rvert^{2}-m^{2}c^{2}\Bigr]
$$

with $S=\frac{h}{2\pi}\theta_{\mathrm{pha}}$ and $m^{2}c^{2}=h^{2}\nu_m^{2}$; the bracket's first factor is $-\mathcal E/c$.

The action is degenerate in the scale. No term carries a derivative of $\varrho$, so the scale's variation is algebraic and its momentum vanishes. The scale is a Lagrange multiplier of one constraint, and the constraint is the mechanical mass shell.

The deletion is invariant under both groups. $(\partial_{r'_{t}}\varrho)^{2}-\lvert\vec\nabla_\Phi \varrho\rvert^{2}$ is a Lorentz scalar of the material sector, and it contains no phase and no potential, so it is invariant under the symmetry group as well. Deleted and transformed commute for both, and the truncated action is covariant and invariant because the deleted object was.

The contrast with the first-order families is one line. There the deleted term is $\lvert\vec\nabla_\Phi \varrho\rvert^{2}$ alone, which no boost preserves, so the limit there is defined in a frame and its action is the action of a fluid with a distinguished time. Here the limit is defined on the manifold, and the truncated action's only time is the sector's.

### The Limits and the Truncation’s Error

The truncated action differs from the parent by the scale's kinetic term, which carries two derivatives and therefore two powers of the parameter. **The error is of order $\epsilon^{2}$**, and the ratio that makes it small is the amplitude's gradient against the mass term, $|\partial\varrho|^{2}/(\nu_m^{2}\varrho^{2})$.

Restoring it adds the quantum potential. Varying the parent with the block present gives the truncated equation plus a divergence of a gradient over the density. The correction is a quantum term with the density in its denominator, so it is large where the density is small and it is the reason the truncated theory cannot describe a nodal region.

The error is amplitude-only and invariant. The deleted block contains no phase and no connection, and the scale is invariant. The correction therefore cannot move the transport equation, cannot move the current, and cannot break covariance, and it commutes with a boost because the block is a Lorentz scalar.

What the coupling does to the error. Nothing, and that is worth stating: the connection sits inside the covariant bracket and the deleted block is the scale's gradient squared, which the connection does not enter. The error is the same functional of the amplitude in the coupled theory as in the free one, which is why the coupled article's error section is one paragraph long.

What the error is not. It is not a bound. **The expansion is asymptotic and convergence is not claimed**, so the statement is that the truncated equations hold to order $\epsilon^{2}$ where the amplitude varies slowly, not that the solutions are close in a norm.

Why the section is separate from the deletion. Which term is deleted and what the deletion costs are two questions, and a reader can be right about the first and wrong about the second. The article answers them in two sections for that reason.

The covariant transport, verbatim. The phase's variation of the truncated action gives the covariant transport because the deleted block contains no phase and no connection. **The equation surviving is not an approximation: it is the parent's equation with the order-two term removed**, and the removal does not touch it.

The mass shell on the truncated class. The scale's variation gives a constant amplitude along the flow, and on that class the mass-shell relation is exact. The truncated scale equation is the statement that the amplitude does not vary, not an eikonal equation; the eikonal is the parent's, and it is restored by putting the deleted block back.

The currents, unchanged. Density, charge and energy are first integrals of the transport, and the transport is untouched. Their expressions are the parent's, and the coupling enters them only where it entered before — through the shifted frequency in the energy and not at all in the charge.

The covariance. The truncated action is a sum of covariant blocks and the deleted block was one too, so the truncation commutes with a local transformation. The truncated theory is invariant, which the article states as a separate section rather than as a remark, because it is the property that fails in the first-order family.

The covariance under boosts. The deleted block is a scalar, so the truncation commutes with a boost. The truncated coupled theory is Lorentz covariant, and the article contrasts this with the family whose deleted term is a spatial gradient and whose truncation therefore singles out a frame.

What does not survive. The amplitude's dynamics near a node, and any configuration whose density varies on the Compton scale. The article states the boundary once, in this section, so that the earlier sections can be read as exact statements on a restricted class rather than as approximations everywhere.

## The Variation: Varying the Scale: the Mechanical Mass Shell
The scale's variation.

$$
2\varrho\Bigl[\Bigl(\partial_{r'_{t}}S+\frac{q\omicron_{\mathrm{pot}}}{c}\Bigr)^{2}-\lvert\vec\pi\rvert^{2}-m^{2}c^{2}\Bigr]=0 ,
$$

that is, away from the node and with $\mathcal E/c=-\left(\partial_{r'_{t}}S+q\omicron_{\mathrm{pot}}/c\right)$,

$$
\boxed{\ \frac{\mathcal E^{2}}{c^{2}}-\lvert\vec\pi\rvert^{2}=m^{2}c^{2}\ }
$$

which is the mechanical mass shell of the equation-route companion.

With the block kept the same variation carries the quantum potential.

$$
2\varrho\Bigl[\Bigl(\partial_{r'_{t}}S+\frac{q\omicron_{\mathrm{pot}}}{c}\Bigr)^{2}-\lvert\vec\pi\rvert^{2}-m^{2}c^{2}\Bigr]-2\Box_\Phi \varrho=0 ,
$$

which divided by $2\varrho$ is $\mathcal E^{2}/c^{2}-\lvert\vec\pi\rvert^{2}=m^{2}c^{2}+\frac{h^{2}}{4\pi^{2}}\Box_\Phi \varrho/\varrho$ — the parent's amplitude equation with the quantum potential on the right. **The two differ by the deleted block and by nothing else.**

The constraint is the truncated theory's Hamiltonian. A degenerate Lagrangian of this shape has no momentum conjugate to the scale, and the Legendre transform returns the mechanical shell as the only constraint. **The limit has converted the scale from a dynamical field into the carrier of one constraint**, which is what "the density becomes auxiliary" means in covariant language.
## The Constraints the Action Imposes: Gauge Invariance and the Deletion
The invariants. The truncated action is built from two combinations, $\left(\partial_{r'_{t}}S+q\omicron_{\mathrm{pot}}/c\right)$ and $\vec\nabla_\Phi S-q\vec A$, and both are unchanged under the local phase translation with the potential's shift. The action is invariant term for term, the quadratic piece supplying the compensation for the potential's square.

The deletion commutes with the transformation, and the reason is structural. The deleted block is built from the scale, the scale is inert under the symmetry group, and an invariant object removed from an invariant action leaves an invariant action. No computation is needed and none was done: the statement is a consequence of the block's content.

Why this matters for the limit's meaning. The non-quantum limit is supposed to be a statement about the field and not about the chart. The covariance and the local invariance of the deletion are what make that true, and they are the two properties the first-order families cannot have in the same form.
## The Structural Consequence: Varying the Phase: the Covariant Transport, Unchanged
The phase's variation.

$$
\vec\nabla_\Phi\cdot\bigl(\rho_{\mathrm{num}}\vec\pi\bigr)+\frac{\partial}{\partial r'_{t}}\Bigl(\rho_{\mathrm{num}}\frac{\mathcal E}{c}\Bigr)=0 ,
$$

the covariant transport equation, with the mechanical momentum in the spatial divergence and the mechanical energy in the temporal one.

It is identical on the full action. The deleted block carries no phase, so both derivatives of the Lagrangian with respect to $\theta_{\mathrm{pha}}$ are one expression, and no rearrangement is needed to see it. The transport equation is not an order of an expansion; it is invariant under the deletion.

The conjugate momentum is the mechanical one, and the quadratic piece is what makes it so. Differentiating the spatial bracket with respect to $\vec\nabla_\Phi\theta_{\mathrm{pha}}$ returns $-2\varrho^{2}\left(\vec\nabla_\Phi\theta_{\mathrm{pha}}-\frac{2\pi q}{h}\vec A\right)$, that is $\rho\vec\pi$ up to $\frac{h}{2\pi}$. **The interaction's linear piece is what shifts the conjugate momentum from the canonical to the mechanical one**, and the quadratic piece is what keeps the shift consistent under a local transformation.

The pair the truncated action produces is charged relativistic dust. A flow along the mechanical momentum, a density carried by it, no pressure, and a normalisation that is the mechanical shell. The parent's own phrase for the free case is irrotational dust; with the connection the flow is still dust and it is no longer irrotational in the kinematic sense, which is the equation-route companion's vorticity split.
## The Noether Currents: Density, Charge and Energy
The current is the density times the transport velocity, and the limit makes that literal. The phase's momentum is the density,
$$
\rho=\varrho^{2}\cosh\theta_{\mathrm{rpd}}\ \longrightarrow\ \varrho^{2}\quad\text{in the non-quantum limit},
$$
and the phase's Euler–Lagrange equation is the continuity equation $\partial_{r'_t}\rho+\vec\nabla_\Phi\cdot(\rho\vec v)=0$ with $\vec v$ the transport velocity. The limit does not change the equation; it removes the terms that made $\rho$ differ from $\varrho^{2}$.

The charge and the energy. The charge is the integral of $\rho$, times the coupling where the field is charged, and it carries no mass. The energy is the mass shell's value, and it carries the mass. The split is exact in the parent and survives the limit unchanged, which is why this article's verification section can check both in one line each.

What the deletion does to the two. The deleted term is a gradient of the scale, and a gradient cannot change a charge; it can change the energy's value at a given configuration but not its conservation. So the limit's currents are the parent's currents with the density's correction dropped, and the error in each is the order of the deleted block.
## What the Principle Adds and What It Relabels: By the Variational Route
Three things, and the second is the coupling's.

*The deletion is a scalar of both groups.* Covariance and local invariance of the limit are properties of the deleted block, not estimates about solutions.

*Both interaction pieces are leading, and the table shows it.* A reader who thought the potential enters as a perturbation can see that the linear and quadratic pieces sit in blocks of order zero, and that the quadratic one is required by boundedness and by local invariance. That is the cleanest statement in the corpus of why the coupling cannot be expanded.

*The scale's lost dynamics is visible as degeneracy.* The full action has a second-order equation for $\varrho$; the truncated one has a constraint. The quantum potential is the whole of the scale's dynamics, so removing it is not removing a correction from an equation but removing a field's kinetic term from an action.

What it does not add.

*The second parameter.* $\delta$ is invisible to a term count, because both the scale's block and the phase's carry two derivatives. The one-particle condition must come from the discarded term's size against $m^{2}c^{2}$.

*The slow-connection hypothesis.* The truncated action's leading bracket contains $\vec A$, so a potential varying as fast as the phase makes the bracket vary as fast as the scale. The action cannot state that condition, because it is a statement about the field and not about a term.

*The boundary terms.* Deleting the scale's block changes the natural boundary condition on the scale from Neumann to none. The corpus works on the whole of space and does not examine the boundary, and this article records the gap.
## Summary
The parent's coupled central action has four blocks: the covariant phase bracket, the scale's kinetic term, and the mass term, with the interaction distributed inside the first. One power of $\epsilon=1/(\pi_{\Phi}L)$ goes to each derivative of the scale, so the scale's block is order two and everything else is order zero.

The limit is the deletion of that block, and the block is a Lorentz scalar with no phase and no potential, so the deletion commutes with boosts and with local transformations. **The truncated action is covariant and invariant because the deleted object was.**

Varying the scale gives the mechanical mass shell as an algebraic constraint and varying the phase gives the covariant transport equation, unchanged term for term. The truncated action is $\varrho^{2}\left[\left(\partial_{r'_{t}}S+q\omicron_{\mathrm{pot}}/c\right)^{2}-\lvert\vec\pi\rvert^{2}-m^{2}c^{2}\right]$, degenerate in the scale, and its content is charged relativistic dust with the mechanical shell as its Hamiltonian.

The coupling survives entire: both interaction pieces are order zero, the quadratic one is required by boundedness and by local invariance, and the truncation deletes none of the interaction. The variational route's blind spots are the second parameter and the slow-connection hypothesis, neither of which a term count can see.
## Summary of Notation
| Symbol | Meaning |
|---|---|
| $\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\varepsilon e_{t}$ | The parent's polar word on the central class |
| $\varrho>0$, $\rho_{\mathrm{num}}=\varrho^{2}$ | The scale; the proper density |
| $S=\frac{h}{2\pi}\theta_{\mathrm{pha}}$, $E=-c\,\partial_{r'_{t}}S$ | The action; the canonical energy |
| $\tilde A_\Phi=i(\omicron_{\mathrm{pot}}/c)e_{t}+\vec A$ | The connection |
| $q$; the parent's $ϙ=-q$ | The electric charge; the parent's coupling |
| $\vec\pi=\vec\nabla_\Phi S-q\vec A$ | Mechanical momentum |
| $\mathcal E=E-q\omicron_{\mathrm{pot}}$ | Mechanical energy; $-\mathcal E/c$ is the temporal bracket |
| $S_{\mathrm{cpl}}$, $S_{\mathrm{cl}}$ | The parent's action; the truncated charged-dust action |
| $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial r_{t}^{\prime\,2}$ | The d'Alembertian of the material sector |
| $\nu_m=\frac{mc}{h}$ | The mass wave number |
| $\epsilon=1/(\pi_{\Phi}L)$ | The parameter; one power per derivative of the scale |
## Further Reading
- [The Lagrangian and the Coupled Klein–Gordon Equation in Polar Variables](the-lagrangian-and-the-coupled-klein-gordon-equation-in-polar-variables.html), the parent: the covariant logarithmic derivative, the central action, and the interaction's two pieces.
- [The Coupled Klein–Gordon Equation in the Non-Quantum Limit](the-coupled-klein-gordon-equation-in-the-non-quantum-limit.html), the companion: the same limit on the parent's pair, the Lorentz force, and the two vorticities.
- [The Lagrangian and the Klein–Gordon Equation in the Non-Quantum Limit](the-lagrangian-and-the-klein-gordon-equation-in-the-non-quantum-limit.html), the free variational companion, where the same scalar is deleted.
- [The Lagrangian and the Coupled Schrödinger Equation in the Non-Quantum Limit](the-lagrangian-and-the-coupled-schrodinger-equation-in-the-non-quantum-limit.html), the non-relativistic companion, where the deleted term is frame dependent.
- [The Non-Quantum Limit of the Biquaternion Model](the-non-quantum-limit-of-the-biquaternion-model.html), for the parameter and the difference between the limit and the approximation.
## Verification
Both Euler–Lagrange systems were computed, with the block and without it.

| variation | full action | truncated action |
|---|---|---|
| with respect to $\varrho$ | mechanical shell with $+\frac{h^{2}}{4\pi^{2}}\Box_\Phi \varrho/\varrho$ | mechanical shell alone |
| with respect to $\theta_{\mathrm{pha}}$ | $\vec\nabla_\Phi\cdot(\rho\vec\pi)+\partial_{r'_{t}}(\rho\mathcal E/c)=0$ | the same, identically |

The second row was compared symbolically and is equal as written. The deleted block carries no phase.

The first row was checked for the sign and for the interaction's coefficients. Keeping the block, the $\varrho$-equation divided by $2\varrho$ returns the covariant bracket minus $\nu_m^{2}$ minus $\Box_\Phi \varrho/\varrho$; deleting the block removes the divergence and keeps every coefficient of $q\omicron_{\mathrm{pot}}$ and of $\lvert\vec A\rvert^{2}$ unchanged. The interaction is not touched by the deletion, which is the check the article's claim requires.

The two interaction pieces were checked against the parent's expansion. Expanding the parent's bracket returns the free kinetic term, the term linear in the potential multiplying the free phase rate, and the term quadratic in the potential with no phase; the coefficients agree with the parent's display term for term, and all three were confirmed to carry no derivative of the scale.

The covariance and the local invariance of the deletion were checked as identities. The block is the sector's contraction of one gradient with itself and contains neither the phase nor the potential, so it is a scalar of both groups and its removal preserves both invariances.

What was not checked. No boundary-value problem was solved, no constraint analysis beyond the primary one was performed, and no numerical solution of the truncated system was run. The claims are about blocks and identities, and both were verified as algebra.
