# __The Non-Quantum Limit, the Variational Principle and the Coupled Klein–Gordon Equation in Biquaternionic Polar Variables__

## Introduction

**The limit in one sentence.** Write the parent's coupled polar action, delete the scale's kinetic term — the same Lorentz scalar the free family deletes — and the two variations of what is left are the mechanical mass shell and the covariant transport equation.

**The parent prints the action in the mechanical variables.** [The Variational Principle and the Coupled Klein–Gordon Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-coupled-klein-gordon-equation-in-biquaternionic-polar-variables.html) writes the action first in the general element with the covariant logarithmic derivative and then for the central field, where the connection appears in the phase's two brackets and nowhere else. **The scale's block is untouched by the coupling**, so the limit here is the free limit applied to a shifted phase.

**The deletion is the free deletion, and it is one Lorentz scalar.** $(\partial_{r'_{t}}r)^{2}-\lvert\vec\nabla_\Phi r\rvert^{2}$ is invariant under boosts of the material sector, and the connection does not enter it. **The limit therefore commutes with the Lorentz group and with the gauge group**, because the deleted block is a scalar of both.

**The coupling survives the truncation entire, and that is this article's point.** The parent splits the interaction into a piece linear in the potential times the free phase rate and a piece quadratic in the potential with no phase. Both are order zero, because neither carries a derivative of the scale. **So the truncation deletes no part of the interaction**, and a reader who expected the potential to enter as a perturbation finds it in the leading term twice.

**The quadratic piece is not optional, and the parent says why.** It is the piece that makes the action bounded below — the quadratic term in the spatial bracket is positive for every $\vec A$ — and it is the piece that makes the action invariant under a local phase translation. **A truncation that dropped it would destroy both properties**, which is the variational form of the statement that the coupling is not a perturbation.

**What the article establishes, in five sentences.** The parent's central action has four blocks: the covariant phase bracket of order zero, the scale's kinetic term of order two, and the mass term of order zero, with the interaction distributed inside the first two of them. The single deletion removes the scale's kinetic term, which is a Lorentz scalar, so the truncated action is covariant. Varying the scale gives the mechanical mass shell as an algebraic constraint and varying the phase gives the covariant transport equation, unchanged term for term. The truncated action is $r^{2}\left[\left(\partial_{r'_{t}}S+q\varphi/c\right)^{2}-\lvert\vec\pi\rvert^{2}-k_{m}^{2}\right]$, degenerate in the scale, and its content is charged relativistic dust.

**What is not new.** The covariant Madelung action, the interaction's two pieces, the boundedness argument and the Lagrange-multiplier form of the mass shell are all standard. Added here: the ordering of the parent's blocks with the interaction inside them, the statement that neither interaction piece is deleted because neither carries a scale derivative, and the reading of the truncated action as charged dust with the mechanical shell as its Hamiltonian.

**The restriction is the parent's.** The central field is $\theta_{\mathrm{rpd}}=0$ with the rotor a sign, and the class is invariant only under a central Hamiltonian. The limit is defined there, as in the other families.

**The signs.** The parent writes the coupling as $ϙ$ with $ϙ=-q$; its temporal bracket is $\partial_{r'_{t}}\theta_{\mathrm{pha}}-\frac{ϙ}{\hbar}a'_{t}$ and its spatial bracket is $\vec\nabla_\Phi\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A$. Every display here uses $q$, the electric charge, $\vec\pi=\vec\nabla_\Phi S-q\vec A$ and $\mathcal E=E-q\varphi$ with $E=-c\,\partial_{r'_{t}}S$, so the temporal bracket is $-\mathcal E/c$ and the free article's convention $\mathcal E=E-q\varphi$ is the one kept.

**Conventions.** Those of the coupled variational polar parent: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_{t}=1$ and $\vec e_\mu^{2}=-e_{t}$; $\mathrm{Sc}$ the coefficient of $e_{t}$; the word $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon e_{t}$; $\tilde A_\Phi=i(\varphi/c)e_{t}+\vec A$; $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial r_{t}^{\prime\,2}$; $\rho_{\mathrm{num}}=r^{2}$; $k_{m}=mc/\hbar$; $\epsilon=1/(\pi_{\Phi}L)$ with $\pi_{\Phi}=\lvert\vec\pi\rvert/\hbar$.

## The Action and Its Blocks

**The parent's action for the central field.**

$$
S_{\mathrm{cpl}}=\int\mathrm{d}^{4}x\;\Bigl\{r^{2}\Bigl[\Bigl(\partial_{r'_{t}}\theta_{\mathrm{pha}}+\frac{q}{\hbar}\frac{\varphi}{c}\Bigr)^{2}-\Bigl\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}-\frac{q}{\hbar}\vec A\Bigr\rvert^{2}\Bigr]
+\bigl(\partial_{r'_{t}}r\bigr)^{2}-\lvert\vec\nabla_\Phi r\rvert^{2}-k_{m}^{2}r^{2}\Bigr\},
$$

the free action with the two covariant substitutions and the amplitude's two terms untouched.

**The blocks and their orders.**

| block | what it carries | order in $\epsilon$ |
|---|---|---|
| $r^{2}\bigl(\partial_{r'_{t}}\theta_{\mathrm{pha}}+\frac{q}{\hbar}\frac{\varphi}{c}\bigr)^{2}$ | scale squared, two derivatives of the phase | $0$ |
| $-r^{2}\bigl\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}-\frac{q}{\hbar}\vec A\bigr\rvert^{2}$ | scale squared, two derivatives of the phase | $0$ |
| $(\partial_{r'_{t}}r)^{2}-\lvert\vec\nabla_\Phi r\rvert^{2}$ | two derivatives of the scale | $2$ |
| $-k_{m}^{2}r^{2}$ | scale squared, no derivative | $0$ |

**The order is a property of the block and never of the potential.** $q\vec A$ sits inside a bracket that carries two derivatives of the phase, and a potential does not change the bracket's derivative count. **The coupling is leading and the table says so without an estimate.**

**The interaction's two pieces, and both are order zero.**

$$
r^{2}\Bigl(\partial_{r'_{t}}\theta_{\mathrm{pha}}\Bigr)^{2}-r^{2}\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}\rvert^{2}
+\frac{2qr^{2}}{\hbar}\Bigl(\partial_{r'_{t}}\theta_{\mathrm{pha}}\frac{\varphi}{c}+\vec\nabla_\Phi\theta_{\mathrm{pha}}\cdot\vec A\Bigr)
+\frac{q^{2}r^{2}}{\hbar^{2}}\Bigl(\Bigl(\frac{\varphi}{c}\Bigr)^{2}-\lvert\vec A\rvert^{2}\Bigr).
$$

**The first interaction piece is the current times the potential and the second is the potential squared.** The parent states both, and the second is the one a "current times potential" presentation omits. **Both are order zero**, so both are leading, so neither is a correction.

**Why the quadratic piece cannot be dropped, in the parent's two reasons.** It makes the kinetic part bounded below, because $-\lvert\vec A\rvert^{2}$ enters with a plus sign after the overall minus of the bracket; and it is what makes the action invariant under a local phase translation, because the potential's shift has to be compensated in a term quadratic in the potential. **A truncation in powers of $q$ would break both**, and that is why no such truncation is the non-quantum limit.

## The Deletion

**Delete the scale's block.**

$$
S_{\mathrm{cl}}=\int\mathrm{d}^{4}x\;r^{2}\Bigl[\Bigl(\partial_{r'_{t}}S+\frac{q\varphi}{c}\Bigr)^{2}-\lvert\vec\pi\rvert^{2}-m^{2}c^{2}\Bigr]
$$

with $S=\hbar\theta_{\mathrm{pha}}$ and $m^{2}c^{2}=\hbar^{2}k_{m}^{2}$; the bracket's first factor is $-\mathcal E/c$.

**The action is degenerate in the scale.** No term carries a derivative of $r$, so the scale's variation is algebraic and its momentum vanishes. **The scale is a Lagrange multiplier of one constraint**, and the constraint is the mechanical mass shell.

**The deletion is invariant under both groups.** $(\partial_{r'_{t}}r)^{2}-\lvert\vec\nabla_\Phi r\rvert^{2}$ is a Lorentz scalar of the material sector, and it contains no phase and no potential, so it is invariant under the gauge group as well. **Deleted and transformed commute for both**, and the truncated action is covariant and gauge invariant because the deleted object was.

**The contrast with the first-order families is one line.** There the deleted term is $\lvert\vec\nabla_\Phi r\rvert^{2}$ alone, which no boost preserves, so the limit there is defined in a frame and its action is the action of a fluid with a distinguished time. **Here the limit is defined on the manifold**, and the truncated action's only time is the sector's.

## Varying the Scale: the Mechanical Mass Shell

**The scale's variation.**

$$
2r\Bigl[\Bigl(\partial_{r'_{t}}S+\frac{q\varphi}{c}\Bigr)^{2}-\lvert\vec\pi\rvert^{2}-m^{2}c^{2}\Bigr]=0 ,
$$

that is, away from the node and with $\mathcal E/c=-\left(\partial_{r'_{t}}S+q\varphi/c\right)$,

$$
\boxed{\ \frac{\mathcal E^{2}}{c^{2}}-\lvert\vec\pi\rvert^{2}=m^{2}c^{2}\ }
$$

which is the mechanical mass shell of the equation-route companion.

**With the block kept the same variation carries the quantum potential.**

$$
2r\Bigl[\Bigl(\partial_{r'_{t}}S+\frac{q\varphi}{c}\Bigr)^{2}-\lvert\vec\pi\rvert^{2}-m^{2}c^{2}\Bigr]-2\Box_\Phi r=0 ,
$$

which divided by $2r$ is $\mathcal E^{2}/c^{2}-\lvert\vec\pi\rvert^{2}=m^{2}c^{2}+\hbar^{2}\Box_\Phi r/r$ — the parent's amplitude equation with the quantum potential on the right. **The two differ by the deleted block and by nothing else.**

**The constraint is the truncated theory's Hamiltonian.** A degenerate Lagrangian of this shape has no momentum conjugate to the scale, and the Legendre transform returns the mechanical shell as the only constraint. **The limit has converted the scale from a dynamical field into the carrier of one constraint**, which is what "the density becomes auxiliary" means in covariant language.

## Varying the Phase: the Covariant Transport, Unchanged

**The phase's variation.**

$$
\vec\nabla_\Phi\cdot\bigl(\rho_{\mathrm{num}}\vec\pi\bigr)+\frac{\partial}{\partial r'_{t}}\Bigl(\rho_{\mathrm{num}}\frac{\mathcal E}{c}\Bigr)=0 ,
$$

the covariant transport equation, with the mechanical momentum in the spatial divergence and the mechanical energy in the temporal one.

**It is identical on the full action.** The deleted block carries no phase, so both derivatives of the Lagrangian with respect to $\theta_{\mathrm{pha}}$ are one expression, and no rearrangement is needed to see it. **The transport equation is not an order of an expansion**; it is invariant under the deletion.

**The conjugate momentum is the mechanical one, and the quadratic piece is what makes it so.** Differentiating the spatial bracket with respect to $\vec\nabla_\Phi\theta_{\mathrm{pha}}$ returns $-2r^{2}\left(\vec\nabla_\Phi\theta_{\mathrm{pha}}-\frac{q}{\hbar}\vec A\right)$, that is $\rho\vec\pi$ up to $\hbar$. **The interaction's linear piece is what shifts the conjugate momentum from the canonical to the mechanical one**, and the quadratic piece is what keeps the shift consistent under a gauge transformation.

**The pair the truncated action produces is charged relativistic dust.** A flow along the mechanical momentum, a density carried by it, no pressure, and a normalisation that is the mechanical shell. **The parent's own phrase for the free case is irrotational dust**; with the connection the flow is still dust and it is no longer irrotational in the kinematic sense, which is the equation-route companion's vorticity split.

## Gauge Invariance and the Deletion

**The invariants.** The truncated action is built from two combinations, $\left(\partial_{r'_{t}}S+q\varphi/c\right)$ and $\vec\nabla_\Phi S-q\vec A$, and both are unchanged under the local phase translation with the potential's shift. **The action is invariant term for term**, the quadratic piece supplying the compensation for the potential's square.

**The deletion commutes with the transformation, and the reason is structural.** The deleted block is built from the scale, the scale is inert under the gauge group, and a gauge invariant object removed from a gauge invariant action leaves a gauge invariant action. **No computation is needed and none was done**: the statement is a consequence of the block's content.

**Why this matters for the limit's meaning.** The non-quantum limit is supposed to be a statement about the field and not about the chart. The covariance and the gauge invariance of the deletion are what make that true, and they are the two properties the first-order families cannot have in the same form.

## What the Variational Route Adds

**Three things, and the second is the coupling's.**

*The deletion is a scalar of both groups.* Covariance and gauge invariance of the limit are properties of the deleted block, not estimates about solutions.

*Both interaction pieces are leading, and the table shows it.* A reader who thought the potential enters as a perturbation can see that the linear and quadratic pieces sit in blocks of order zero, and that the quadratic one is required by boundedness and by gauge invariance. **That is the cleanest statement in the corpus of why the coupling cannot be expanded.**

*The scale's lost dynamics is visible as degeneracy.* The full action has a second-order equation for $r$; the truncated one has a constraint. **The quantum potential is the whole of the scale's dynamics**, so removing it is not removing a correction from an equation but removing a field's kinetic term from an action.

**What it does not add.**

*The second parameter.* $\delta$ is invisible to a term count, because both the scale's block and the phase's carry two derivatives. **The one-particle condition must come from the discarded term's size against $m^{2}c^{2}$.**

*The slow-connection hypothesis.* The truncated action's leading bracket contains $\vec A$, so a potential varying as fast as the phase makes the bracket vary as fast as the scale. **The action cannot state that condition**, because it is a statement about the field and not about a term.

*The boundary terms.* Deleting the scale's block changes the natural boundary condition on the scale from Neumann to none. The corpus works on the whole of space and does not examine the boundary, and this article records the gap.

## Verification

**Both Euler–Lagrange systems were computed, with the block and without it.**

| variation | full action | truncated action |
|---|---|---|
| with respect to $r$ | mechanical shell with $+\hbar^{2}\Box_\Phi r/r$ | mechanical shell alone |
| with respect to $\theta_{\mathrm{pha}}$ | $\vec\nabla_\Phi\cdot(\rho\vec\pi)+\partial_{r'_{t}}(\rho\mathcal E/c)=0$ | the same, identically |

**The second row was compared symbolically and is equal as written.** The deleted block carries no phase.

**The first row was checked for the sign and for the interaction's coefficients.** Keeping the block, the $r$-equation divided by $2r$ returns the covariant bracket minus $k_{m}^{2}$ minus $\Box_\Phi r/r$; deleting the block removes the divergence and keeps every coefficient of $q\varphi$ and of $\lvert\vec A\rvert^{2}$ unchanged. **The interaction is not touched by the deletion**, which is the check the article's claim requires.

**The two interaction pieces were checked against the parent's expansion.** Expanding the parent's bracket returns the free kinetic term, the term linear in the potential multiplying the free phase rate, and the term quadratic in the potential with no phase; the coefficients agree with the parent's display term for term, and all three were confirmed to carry no derivative of the scale.

**The covariance and the gauge invariance of the deletion were checked as identities.** The block is the sector's contraction of one gradient with itself and contains neither the phase nor the potential, so it is a scalar of both groups and its removal preserves both invariances.

**What was not checked.** No boundary-value problem was solved, no constraint analysis beyond the primary one was performed, and no numerical solution of the truncated system was run. The claims are about blocks and identities, and both were verified as algebra.

## Summary

The parent's coupled central action has four blocks: the covariant phase bracket, the scale's kinetic term, and the mass term, with the interaction distributed inside the first. One power of $\epsilon=1/(\pi_{\Phi}L)$ goes to each derivative of the scale, so the scale's block is order two and everything else is order zero.

The limit is the deletion of that block, and the block is a Lorentz scalar with no phase and no potential, so the deletion commutes with boosts and with gauge transformations. **The truncated action is covariant and gauge invariant because the deleted object was.**

Varying the scale gives the mechanical mass shell as an algebraic constraint and varying the phase gives the covariant transport equation, unchanged term for term. The truncated action is $r^{2}\left[\left(\partial_{r'_{t}}S+q\varphi/c\right)^{2}-\lvert\vec\pi\rvert^{2}-m^{2}c^{2}\right]$, degenerate in the scale, and its content is charged relativistic dust with the mechanical shell as its Hamiltonian.

The coupling survives entire: both interaction pieces are order zero, the quadratic one is required by boundedness and by gauge invariance, and the truncation deletes none of the interaction. The variational route's blind spots are the second parameter and the slow-connection hypothesis, neither of which a term count can see.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon e_{t}$ | The parent's polar word on the central class |
| $r>0$, $\rho_{\mathrm{num}}=r^{2}$ | The scale; the proper density |
| $S=\hbar\theta_{\mathrm{pha}}$, $E=-c\,\partial_{r'_{t}}S$ | The action; the canonical energy |
| $\tilde A_\Phi=i(\varphi/c)e_{t}+\vec A$ | The connection |
| $q$; the parent's $ϙ=-q$ | The electric charge; the parent's coupling |
| $\vec\pi=\vec\nabla_\Phi S-q\vec A$ | Mechanical momentum |
| $\mathcal E=E-q\varphi$ | Mechanical energy; $-\mathcal E/c$ is the temporal bracket |
| $S_{\mathrm{cpl}}$, $S_{\mathrm{cl}}$ | The parent's action; the truncated charged-dust action |
| $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial r_{t}^{\prime\,2}$ | The d'Alembertian of the material sector |
| $k_{m}=mc/\hbar$ | The mass wave number |
| $\epsilon=1/(\pi_{\Phi}L)$ | The parameter; one power per derivative of the scale |

## Further Reading

- [The Variational Principle and the Coupled Klein–Gordon Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-coupled-klein-gordon-equation-in-biquaternionic-polar-variables.html), the parent: the covariant logarithmic derivative, the central action, and the interaction's two pieces.
- [The Non-Quantum Limit and the Coupled Klein–Gordon Equation in Biquaternionic Polar Variables](the-non-quantum-limit-and-the-coupled-klein-gordon-equation-in-biquaternionic-polar-variables.html), the companion: the same limit on the parent's pair, the Lorentz force, and the two vorticities.
- [The Non-Quantum Limit, the Variational Principle and the Klein–Gordon Equation in Biquaternionic Polar Variables](the-non-quantum-limit-the-variational-principle-and-the-klein-gordon-equation-in-biquaternionic-polar-variables.html), the free variational companion, where the same scalar is deleted.
- [The Non-Quantum Limit, the Variational Principle and the Coupled Schrödinger Equation in Biquaternionic Polar Variables](the-non-quantum-limit-the-variational-principle-and-the-coupled-schrodinger-equation-in-biquaternionic-polar-variables.html), the non-relativistic companion, where the deleted term is frame dependent.
- [The Non-Quantum Limit of the Biquaternion Model](the-non-quantum-limit-of-the-biquaternion-model.html), for the parameter and the difference between the limit and the approximation.
