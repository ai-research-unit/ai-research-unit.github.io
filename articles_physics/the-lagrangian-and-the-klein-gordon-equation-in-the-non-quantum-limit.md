# __The Lagrangian and the Klein–Gordon Equation in the Non-Quantum Limit__

**Declared omissions.** The reality of the action is settled inside the action section so slot 5 is omitted, with its four subsections. The constraint is the parent's and the limit neither adds nor removes one, so slot 6 is omitted. The second variation is not computed, so slot 8 is omitted. The two settings are not contrasted, so slot 10 is omitted. No comparison beyond the parent is attempted, so slot 13 is omitted. No open question is separated from the verification, so slot 14 is omitted.

## Introduction

**The limit in one sentence.** Write the parent's polar action for the central field, delete the scale's kinetic term — one Lorentz scalar — and the two variations of what is left are the mass shell and the transport equation.

**The parent prints both halves.** [The Lagrangian and the Klein–Gordon Equation in Polar Variables](the-lagrangian-and-the-klein-gordon-equation-in-polar-variables.html) writes the action first for the general element in the parameter basis, with a metric $g_{ab}$ on the parameter space, and then for the central field, where only the scale and the angle are left. The central action has three blocks, and this article deletes one.

**The deletion is a Lorentz scalar, and that is this family's characteristic result.** The deleted block is $(\partial_{r'_{t}}\varrho)^{2}-\lvert\vec\nabla_\Phi \varrho\rvert^{2}$, which is $(\partial \varrho)^{2}$ on the material sector and is invariant under every boost of the sector. **The limit therefore commutes with the Lorentz group**, and the truncated action is covariant. In the first-order family the deleted term is $\lvert\vec\nabla_\Phi \varrho\rvert^{2}$ alone, which is frame dependent, so there the limit is defined in a frame; here it is defined on the manifold.

**The consequence is structural and worth the article's second sentence.** The limit removes the scale's dynamics and leaves the scale in the action without a derivative of itself. The scale is then an auxiliary field, its variation is the mass shell, and the theory the limit produces is a constrained system whose Hamiltonian is that constraint. **Relativistic dust with a normalisation** is the parent's own phrase for the pair without the quantum term, and this is the action of it.

**What the article establishes, in five sentences.** The parent's central action has three blocks: the scale's kinetic term of order two, the phase's kinetic term of order zero, and the mass term of order zero. The single deletion removes the scale's kinetic term, which is a Lorentz scalar, so the truncation preserves covariance. Varying the scale of the truncated action gives the mass shell as an algebraic constraint, and varying the phase gives the transport equation, unchanged term for term. The truncated action is $\varrho^{2}\left[(\partial\theta_{\mathrm{pha}})^{2}-k_{m}^{2}\right]$, degenerate in the scale, and its Euler–Lagrange system is the parent's pair with the quantum potential removed.

**What is not new.** The relativistic Madelung action, the Lagrange-multiplier form of a mass-shell constraint, and the reading of the pair as irrotational dust are standard. Added here: the ordering of the parent's three blocks against one parameter, the observation that the deletion is a Lorentz scalar and the limit therefore covariant, and the reading of the limit as the removal of the scale's own dynamics.

**The restriction is the parent's.** The central field is $\theta_{\mathrm{rpd}}=0$ with the rotor a sign, and the parent proves that class is invariant only under a central Hamiltonian. The limit is defined there, as in the other families.

## Conventions

**The conventions are the corpus's, restated here so that every sign below is checkable from this page alone.** Those of the variational polar parent: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_{t}=1$ and $\vec e_\mu^{2}=-e_{t}$; $\mathrm{Sc}$ the coefficient of $e_{t}$; the word $\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\varepsilon e_{t}$ with $\varrho>0$; $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$; $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial r_{t}^{\prime\,2}$ on the material sector with $r'_{t}=ct'$; $\rho_{\mathrm{num}}=\varrho^{2}$; $k_{m}=mc/\hbar$; $\epsilon=1/(k_{\Phi}L)$ with $L^{-1}=\lvert\vec\nabla_\Phi\ln \varrho\rvert$.

## The Action in the Non-Quantum Limit: The Three Blocks

**The parent's central action.**

$$
S_{\mathrm{central}}=\int\mathrm{d}^{4}x\;\Bigl[(\partial_{r'_{t}}\varrho)^{2}-\lvert\vec\nabla_\Phi \varrho\rvert^{2}+\varrho^{2}\bigl((\partial_{r'_{t}}\theta_{\mathrm{pha}})^{2}-\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}\rvert^{2}\bigr)-k_{m}^{2}\varrho^{2}\Bigr].
$$

Three blocks, and the middle one carries the phase twice.

**The blocks and their orders.**

| block | what it carries | order in $\epsilon$ |
|---|---|---|
| $(\partial_{r'_{t}}\varrho)^{2}-\lvert\vec\nabla_\Phi \varrho\rvert^{2}$ | two derivatives of the scale | $2$ |
| $\varrho^{2}\bigl((\partial_{r'_{t}}\theta_{\mathrm{pha}})^{2}-\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}\rvert^{2}\bigr)$ | scale squared, two derivatives of the phase | $0$ |
| $-k_{m}^{2}\varrho^{2}$ | scale squared, no derivative | $0$ |

**The first block is one object and not two.** $\partial_{r'_{t}}$ and $\vec\nabla_\Phi$ carry the same power, because the scale varies on a length $L$ in space and on the length $L$ in the material time $r'_{t}=ct'$. **The block is $(\partial \varrho)^{2}$ and the metric structure of the material sector is what makes its two halves one term**, so the order $2$ is assigned to the block and not to a spatial piece of it.

**The second block is the mass shell before it is a shell.** Its bracket is $\lvert\partial\theta_{\mathrm{pha}}\rvert^{2}$ with the material signs, so the truncated action is the statement that this bracket equals $k_{m}^{2}$ — and that is the mass shell with $S=\hbar\theta_{\mathrm{pha}}$.

**Why the middle block cannot be the scale's partner.** In the general element the action is the sigma-model form $g_{ab}(p)\,\partial p^{a}\partial p^{b}$ with a metric on the eight parameters, and the central field is its restriction to two coordinates. **The scale's block and the angle's block are two diagonal blocks of one metric**, and the order is a property of the coordinate: derivatives of the scale are order $\epsilon$ and derivatives of the angle are order zero.

## The Limit: The Deletion

**Delete the scale's block.**

$$
S_{\mathrm{cl}}=\int\mathrm{d}^{4}x\,\Bigl[\varrho^{2}\bigl((\partial_{r'_{t}}\theta_{\mathrm{pha}})^{2}-\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}\rvert^{2}\bigr)-k_{m}^{2}\varrho^{2}\Bigr]
=\int\mathrm{d}^{4}x\;\varrho^{2}\Bigl[\bigl(\partial\theta_{\mathrm{pha}}\bigr)^{2}-k_{m}^{2}\Bigr].
$$

**One block, no derivatives of the scale, and the action is degenerate in $\varrho$.** That degeneracy is the limit's content: the scale has become an auxiliary field.

**The deletion is Lorentz invariant, and this is the family's theorem.** $(\partial_{r'_{t}}\varrho)^{2}-\lvert\vec\nabla_\Phi \varrho\rvert^{2}$ is the material sector's invariant contraction of one gradient with itself. A boost of the sector mixes the two terms and preserves the combination, so removing it removes a Lorentz scalar. **Deleted and boosted commute**, and the truncated action is the boost of itself.

**The contrast with the first-order family is one sentence.** There the deleted term is $\lvert\vec\nabla_\Phi \varrho\rvert^{2}$, which a boost does not preserve, so the limit there is a statement in a chosen frame; here the limit is a statement on the manifold, and a reader who wants the covariant form of the non-quantum limit must take it from this equation.

**What is not deleted, and it matters.** The phase's block keeps both signs of the material signs, so the truncated action is not a Euclidean or a static object: it carries $(\partial_{r'_{t}}\theta)^{2}$ and $-\lvert\vec\nabla_\Phi\theta\rvert^{2}$ and its Euler–Lagrange equations are the relativistic ones. **The limit is not the non-relativistic reduction**; the second truncation, in $\beta=v/c$, is a different operation performed on the truncated theory.

## The Variation: Varying the Scale: the Mass Shell

**The truncated action has no $\partial \varrho$, so the scale's variation is algebraic.**

$$
2\varrho\Bigl[\bigl(\partial\theta_{\mathrm{pha}}\bigr)^{2}-k_{m}^{2}\Bigr]=0 ,
$$

that is, away from the node $\varrho=0$,

$$
\boxed{\ \bigl(\partial_{r'_{t}}\theta_{\mathrm{pha}}\bigr)^{2}-\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}\rvert^{2}=k_{m}^{2}\ }
$$

which with $S=\hbar\theta_{\mathrm{pha}}$ is $\left(\partial_{r'_{t}}S\right)^{2}-\lvert\vec\nabla_\Phi S\rvert^{2}=m^{2}c^{2}$, the mass shell.

**On the full action the same variation carries the quantum potential.** Keeping the scale's block, $\partial L/\partial(\partial_\mu \varrho)$ is nonzero and the Euler–Lagrange equation gains the divergence:

$$
2\varrho\Bigl[\bigl(\partial\theta_{\mathrm{pha}}\bigr)^{2}-k_{m}^{2}\Bigr]-2\Box_\Phi \varrho=0 ,
$$

which divided by $2\varrho$ is $\left(\partial\theta_{\mathrm{pha}}\right)^{2}-k_{m}^{2}=\Box_\Phi \varrho/\varrho$, that is the parent's amplitude line $\left(\partial S\right)^{2}-m^{2}c^{2}=\hbar^{2}\Box_\Phi \varrho/\varrho$. **The two equations differ by the deleted block and by nothing else**, and the sign is the one the metric of the material sector supplies.

**The scale is a Lagrange multiplier, and the constraint is the mass shell.** In the truncated action $\varrho^{2}$ multiplies the bracket, so a variation of $\varrho$ imposes the bracket's vanishing and a variation of anything else is weighted by it. **The equation of motion of the classical theory is the constraint**, and that is the covariant form of the statement the first-order companion makes when it calls the scale a multiplier.

**The Hamiltonian of the truncated theory is the constraint.** A degenerate Lagrangian of this shape has no independent momentum for the scale, and the Legendre transform produces the mass-shell condition as the only constraint. **The limit therefore produces a reparametrisation-invariant-looking system with the mass shell as its Hamiltonian**, which is the standard form of a relativistic particle or of dust, and the corpus's phrase for it is irrotational dust.

## The Structural Consequence: Varying the Phase: the Transport, Unchanged

**The phase's variation.**

$$
\partial_{r'_{t}}\!\left(\varrho^{2}\,\partial_{r'_{t}}S_{\tilde\Xi}\right)-\vec\nabla_\Phi\cdot\bigl(\varrho^{2}\vec\nabla_\Phi S_{\tilde\Xi}\bigr)=0 ,
$$

which is $\partial_{r'_{t}}(\rho_{\mathrm{num}}\partial_{r'_{t}}S)-\vec\nabla_\Phi\cdot(\rho_{\mathrm{num}}\vec\nabla_\Phi S)=0$, the parent's transport equation with the sign of the material d'Alembertian.

**It is identical on the full action, because the deleted block has no $\theta_{\mathrm{pha}}$.** Both derivatives of the Lagrangian with respect to the phase are the same expression before and after the deletion, so no rearrangement is needed. **The transport equation is not an order of an expansion**; it is invariant under a deletion that removes a whole block.

**The current follows from the same variation.** Differentiating $\varrho^{2}(\partial\theta)^{2}$ with respect to $\partial_\mu\theta$ returns $2\varrho^{2}\partial_\mu\theta$, so the current is $\rho_{\mathrm{num}}\partial_\mu S$, which is the parent's $\tilde J_\Phi=\rho_{\mathrm{num}}\tilde P_\Phi/m$ up to the mass factor. **The truncated action already knows the current**, and the transport equation is its conservation.

**The pair the limit produces, in the parent's words.** Relativistic irrotational dust: a pressureless flow along the phase gradient, with the density carried by the flow and the four-velocity normalised to $mc$. The parent states that with the quantum term the fluid is not dust, and that without it the pair is dust. **This article supplies the action of the dust and nothing more.**

## The Noether Currents: Density, Charge and Energy

**The current is the density times the transport velocity, and the limit makes that literal.** The phase's momentum is the density,
$$
\rho=\varrho^{2}\cosh\theta_{\mathrm{rpd}}\ \longrightarrow\ \varrho^{2}\quad\text{in the non-quantum limit},
$$
and the phase's Euler–Lagrange equation is the continuity equation $\partial_{r'_t}\rho+\vec\nabla_\Phi\cdot(\rho\vec v)=0$ with $\vec v$ the transport velocity. The limit does not change the equation; it removes the terms that made $\rho$ differ from $\varrho^{2}$.

**The charge and the energy.** The charge is the integral of $\rho$, times the coupling where the field is charged, and it carries no mass. The energy is the mass shell's value, and it carries the mass. The split is exact in the parent and survives the limit unchanged, which is why this article's verification section can check both in one line each.

**What the deletion does to the two.** The deleted term is a gradient of the scale, and a gradient cannot change a charge; it can change the energy's value at a given configuration but not its conservation. So the limit's currents are the parent's currents with the density's correction dropped, and the error in each is the order of the deleted block.

## The Limit: The Truncation and Its Error

**The error is the deleted block, and its order is two.** The truncated action differs from the parent by $(\partial\varrho)^{2}$ in the material signs, and each factor of $\partial$ carries one power of the parameter. **The error is therefore of order $\epsilon^{2}$**, and the ratio that makes it small is the amplitude's gradient over the scale the truncation assumes: $|\partial\varrho|^{2}/(k_m^{2}\varrho^{2})$, which is small exactly when the amplitude varies slowly compared with the Compton length.

**What restoring the term does.** Varying the parent's scale equation with the block present gives the same equation as the truncated one **plus a term that is a divergence of a gradient divided by the density** — the term the corpus calls the quantum potential. Its coefficient is $\hbar^{2}/2m$ in the material units, so it is a quantum correction and not a classical one, and its size relative to the mass term is $\epsilon^{2}$.

**Why the error is a functional of the amplitude alone.** The deleted block contains no phase and no potential, so the correction cannot move the phase's equation or the current. **The error is confined to the amplitude's equation**, and that is why the article can say the transport equation is untouched by the truncation and the mass-shell equation is not.

**Gauge covariance of the error.** The deleted block is a Lorentz scalar built from the scale's gradient; the scale is gauge invariant. **The error is therefore gauge invariant and the truncation commutes with a gauge transformation**, which is the property the first-order family does not have and which the article's section on gauge invariance states separately.

**What the error is not.** It is not a bound on any solution. **The expansion is asymptotic in $\epsilon$ and it is not claimed to converge**, so the statement is that the truncated equations hold to order $\epsilon^{2}$ for amplitudes that vary slowly, and not that the true solution is within a stated distance of the truncated one.

**Why the section is separate from the deletion.** A reader can accept that a term is deleted and still be wrong about what the deletion costs. **The two sections answer two questions** — which term, and how much — and the article keeps them apart because the family's honesty about its limits is the whole point of the reading.

## The Limit: What Survives

**Everything of order zero, and it survives exactly.** The truncated action's variations give the mass-shell relation for the scale and the covariant transport for the phase, and neither is an approximation to the parent's equation: **they are the parent's equations with the order-two term set to zero**, and the difference is the quantum potential and nothing else.

**The transport, unchanged.** Varying the phase of the truncated action gives the covariant transport verbatim, because the deleted block contains no phase. **The equation is identical and not merely equal to leading order**, which is a stronger statement than the truncation needs and the article makes it anyway.

**The mass shell, and what it becomes.** Varying the scale gives $\partial\varrho=0$ in the truncated action, so the amplitude is constant along the flow and the mass-shell relation is exact on that class. **The truncated equation is therefore not the eikonal equation of a varying amplitude but the statement that the amplitude does not vary**, and a reader who wants the eikonal must restore the order-two block.

**The currents.** The density and the charge are the phase's conjugate quantities and come from the transport's own equation. **They survive unchanged, with the same expressions as in the parent**, because they are first integrals of the transport and the transport is untouched.

**The covariance.** The truncated action is a sum of scalars, so it is Lorentz invariant; the deleted block was a scalar, so the truncation commutes with a boost. **The truncated theory is covariant**, and that is the property the article contrasts with the first-order family, where the deleted term is a spatial gradient alone and the truncation breaks the boost invariance of the kept terms.

**What does not survive.** The amplitude's dynamics. **Any solution whose density varies on the Compton scale is outside the truncated theory**, and the article says so in one sentence rather than leaving the reader to infer the boundary from the order count.

## What the Principle Adds and What It Relabels: By the Variational Route

**Three things, and the first is this family's own.**

*The deletion is covariant.* The order-two block is a Lorentz scalar, so the limit commutes with boosts and the truncated action is a covariant object. **No estimate can establish this**; it is a property of the term that was removed.

*The scale's own dynamics is what is lost, and the loss is visible as degeneracy.* The full action has a second-order equation for $\varrho$; the truncated one has an algebraic constraint. **The quantum potential is not a correction to an equation but the whole of the scale's dynamics**, which is why it cannot be removed from one equation only.

*The constraint structure is explicit.* The truncated theory's Hamiltonian is the mass shell, and the density is a multiplier. That is the covariant form of the fluid's pressurelessness, and it is the reason the limit's flow is dust.

**What it does not add, and the list has three items.**

*The second parameter.* $\delta=1/(k_{m}L)$ does not appear in the term count, because both blocks carry two derivatives and the count cannot see the mass scale. **The one-particle condition is invisible to the action route** and has to be argued from the discarded term's size against $m^{2}c^{2}$, which is the equation-route companion's business.

*The boundary terms.* Deleting $(\partial \varrho)^{2}$ changes the natural boundary condition on the scale: the full action needs a Neumann datum on it at the boundary and the truncated one does not. The corpus states the limit on the whole of space and does not examine the boundary.

*The general element.* The same rule applied to the sigma-model form would delete the scale's diagonal block of $g_{ab}$ and keep the angular blocks, because the angles' gradients are not ordered by $\epsilon$. **That truncation is not performed anywhere in the corpus**, and this article records the gap rather than performing it: on the general element the phases' and the angles' derivatives are of comparable size and the ordering would need a separate argument.

## Verification

**Both Euler–Lagrange systems were computed, with the block and without it.**

| variation | full action | truncated action |
|---|---|---|
| with respect to $\varrho$ | $\left(\partial\theta\right)^{2}-k_{m}^{2}=\Box_\Phi \varrho/\varrho$ | $\left(\partial\theta\right)^{2}=k_{m}^{2}$ |
| with respect to $\theta_{\mathrm{pha}}$ | $\partial_{r'_{t}}(\rho\partial_{r'_{t}}S)-\vec\nabla_\Phi\cdot(\rho\vec\nabla_\Phi S)=0$ | the same, identically |

**The second row was compared symbolically and is equal as written.** The deleted block carries no $\theta_{\mathrm{pha}}$, so the two derivatives of the Lagrangian with respect to the phase are one expression.

**The first row was checked for the sign.** Keeping the block, the $\varrho$-equation divided by $2\varrho$ is $\left(\partial\theta\right)^{2}-k_{m}^{2}-\Box_\Phi \varrho/\varrho=0$, which is the parent's amplitude line after $S=\hbar\theta_{\mathrm{pha}}$; deleting the block removes the divergence and leaves the bracket. **The two differ by exactly the quantum potential.**

**The covariance of the deletion was checked as an identity.** With $\Lambda$ a boost of the material sector, $(\partial \varrho)^{2}$ is unchanged because the contraction is taken with the sector's metric, so the deleted object is a scalar and the deletion commutes with $\Lambda$.

**What was not checked.** No boundary-value problem was solved, no constraint analysis beyond the primary one was performed, and no numerical solution of the truncated system was run. The claims are about blocks and identities, and both were verified as algebra.

## Summary

The parent's central action has three blocks: the scale's kinetic term, the phase's kinetic term, and the mass term. One power of $\epsilon=1/(k_{\Phi}L)$ goes to each derivative of the scale, so the first block is order two and the other two are order zero.

The limit is the deletion of the first block, which is $(\partial \varrho)^{2}$ in the material signs and is a Lorentz scalar. **The deletion commutes with boosts, and the truncated action is covariant** — the property the first-order family does not have, because there the deleted term is a spatial gradient alone.

Varying the scale of the truncated action gives the mass shell as an algebraic constraint, and varying the phase gives the transport equation, unchanged term for term. The truncated action is $\varrho^{2}\left[(\partial\theta)^{2}-k_{m}^{2}\right]$, degenerate in the scale, and its content is relativistic irrotational dust with the mass shell as its Hamiltonian.

The variational route's gain here is the covariance of the deletion and the visibility of what is lost: the scale's own dynamics. Its blind spot is the second parameter, which no term count can see.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=\varrho\,e^{i\theta_{\mathrm{pha}}}\varepsilon e_{t}$ | The parent's polar word on the central class |
| $\varrho>0$, $\rho_{\mathrm{num}}=\varrho^{2}$ | The scale; the proper density |
| $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$ | The action |
| $\partial^{2}$ | The material sector's invariant contraction of one gradient |
| $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial r_{t}^{\prime\,2}$ | The d'Alembertian of the material sector |
| $r'_{t}=ct'$ | The material length |
| $k_{m}=mc/\hbar$ | The mass wave number |
| $S_{\mathrm{central}}$, $S_{\mathrm{cl}}$ | The parent's action; the truncated one |
| $\epsilon=1/(k_{\Phi}L)$ | The parameter; one power per derivative of the scale |
| $g_{ab}$ | The metric on the parameter space of the general element |

## Further Reading

- [The Lagrangian and the Klein–Gordon Equation in Polar Variables](the-lagrangian-and-the-klein-gordon-equation-in-polar-variables.html), the parent: the sigma-model action, its restriction to the central field, and the two currents.
- [The Klein–Gordon Equation in the Non-Quantum Limit](the-klein-gordon-equation-in-the-non-quantum-limit.html), the companion: the same limit on the parent's pair, the two parameters, and the two denominators.
- [The Lagrangian and the Schrödinger Equation in the Non-Quantum Limit](the-lagrangian-and-the-schrodinger-equation-in-the-non-quantum-limit.html), the first-order variational companion, where the deleted term is not a scalar.
- [The Klein–Gordon Equation in Biquaternionic Polar Variables](the-klein-gordon-equation-in-biquaternionic-polar-variables.html), for the word and the exact pair.
- [The Non-Quantum Limit of the Biquaternion Model](the-non-quantum-limit-of-the-biquaternion-model.html), for the parameter and the difference between the limit and the approximation.
- [The Lagrangian and the Coupled Klein–Gordon Equation in the Non-Quantum Limit](the-lagrangian-and-the-coupled-klein-gordon-equation-in-the-non-quantum-limit.html), where the connection sits in the same three blocks.
