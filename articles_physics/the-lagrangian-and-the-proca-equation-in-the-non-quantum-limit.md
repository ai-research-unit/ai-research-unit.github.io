# __The Lagrangian and the Proca Equation in the Non-Quantum Limit__

**Declared omissions.** The reality of the action is settled inside the action section and not in a section named for it, so slot 5 is omitted. The limit adds no constraint beyond the one the parent imposes, so slot 6 is omitted. The second variation is not computed, so slot 8 is omitted. The two settings are not contrasted, so slot 10 is omitted. No comparison beyond the parent is attempted, so slot 13 is omitted. No open question is separated from the verification, so slot 14 is omitted.

## Introduction

**The finding, in one sentence.** The variational route confirms the local-form companion's result and makes it quantitative: in the Proca action the amplitude's kinetic term and the mass term are of the same size, so deleting one is not an approximation but a change of theory.

**The action and the two terms that decide the article.**

$$
S=\int\mathrm{d}^{4}\varrho\;\Bigl\{\tfrac12\sum_\mu\varepsilon_\mu\bigl(\partial_\mu \varrho\bigr)^{2}-\tfrac12k_m^{2}\varrho^{2}+\text{(the frame's terms)}\Bigr\},
$$

in the timelike branch's word $\tilde A_\Phi=\varepsilon i \varrho\tilde U$, with $\varepsilon_\mu$ the metric signs of the material sector. **The first and second terms are the amplitude's kinetic term and the mass term**, and the frame's terms carry the boost's connection.

**Why the two terms are the same size, in one line.** For a real plane wave $\varrho=\lvert\vec A_0\rvert\lvert\cos(\omega t')\rvert$ with $\omega^{2}-\lvert\vec k\rvert^{2}=k_m^{2}$, the kinetic term is $\omega^{2}\varrho^{2}\tan^{2}$ and the mass term is $k_m^{2}\varrho^{2}$, so their ratio is $\omega^{2}/k_m^{2}$ up to the tangent. **The ratio is of order one**, so neither term dominates and no truncation of the pair is controlled.

**What that does to the standard story.** In the Klein–Gordon family the deleted term is one derivative order above the kept ones, so the limit is an expansion and its error is a power of $\epsilon$. **Here the two terms carry the same two derivatives, one on the amplitude and one from the mass**, and there is no order difference to exploit. **The truncation's error is of the same size as the truncated term's content.**

**The variational reason, stated once.** The Proca action's amplitude sector is $(\Box_\Phi-k_m^{2})\varrho$ and both terms come from the same operator. **A term that is half of an operator cannot be dropped from the operator's own equation**, and the variational principle makes this visible because both terms appear as separate blocks with the same derivative count.

**What the article establishes, in four sentences.** The Proca action, with the real word substituted, has an amplitude sector whose two terms are the amplitude's Laplacian and the mass term, both of order $k_m^{2}$. For a solution the two are comparable, so the non-quantum truncation is not a controlled approximation in this family. The variational route's contribution is therefore negative and precise: it quantifies the obstruction the local-form companion found by order counting. What survives variationally is the frame's sector and the Lorenz constraint, and those are the chart's genuine content.

**What is not new.** The Proca action's decomposition into an amplitude and a frame, the Lorenz constraint as a trace, and the fact that a massive vector field's amplitude oscillates are standard. Added here: the statement that the two amplitude blocks carry the same derivative count, and the reading of the variational route as the place where the family's obstruction is quantified rather than merely observed.

**The restriction.** The word is defined for $\varrho>0$ on one branch; the boundary is the lightlike set where the norm vanishes.

## Conventions

**The conventions are the corpus's, restated here so that every sign below is checkable from this page alone.** Those of the polar parent and its variational companion: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_{t}=1$ and $\vec e_\mu^{2}=-e_{t}$; $\mathrm{Sc}$ the coefficient of $e_{t}$; $\tilde A_\Phi=a'_{t}e_{t}+\vec A$ real; $\Gamma_\mu$ the frame's connection; $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial r_{t}^{\prime\,2}$; $k_m=mc/\hbar$.

## The Action in the Word

**The blocks.**

| block | derivative count | order in $k_m$ |
|---|---|---|
| $\tfrac12\sum_\mu\varepsilon_\mu(\partial_\mu \varrho)^{2}$ | two, on the amplitude | $k_m^{2}$ |
| $-\tfrac12k_m^{2}\varrho^{2}$ | none | $k_m^{2}$ |
| the frame's terms | two, on the boost's connection | $k_m^{2}$ |

**All three carry $k_m^{2}$ and two derivatives**, and that is the whole of the difficulty: there is no hierarchy among them.

**The frame's terms.** The boost's connection enters the kinetic term through the covariant derivative, so the action is the free scalar action of the amplitude plus a sigma-model term for the frame. **The parent's two boxed equations are exactly the two variations of this display.**

**The constraint.** The Lorenz condition is the scalar part of the equation, $\mathrm{Sc}(\tilde\nabla_\Phi^{\natural}\tilde A_\Phi)=0$, which in the chart is one real equation among four. **It is a constraint on the frame and on the amplitude together**, and it is the chart's version of the transversality of a massive vector field.

## The Two Variations

**Two variations of one display, and a third for the constraint.** The chart's action has an amplitude block with two derivatives, a mass block with none, and the frame's sigma-model term. Varying the amplitude gives an equation with a second derivative and the mass term; varying the frame's angles gives the transport of the boost, which is the article's *What Survives*; varying the connection gives the Lorenz condition.

**The boundary term.** The amplitude's variation produces one, because its block carries two derivatives; on a region with fixed amplitude on the boundary it vanishes, and on a region that reaches infinity the fall-off kills it. The frame's variation produces none, because the frame enters algebraically through $\vec A=-\varrho\sinh\frac{\theta_{\mathrm{rpd}}}{2}\hat u_{\mathrm b}$ and through no derivative of its own beyond the covariant one.

**Why the constraint is not a choice.** The Lorenz condition is the scalar part of the connection's variation, so it is one of the Euler–Lagrange equations and not a gauge fixing. In the massless limit the same variation gives an identity instead, and that change of status is the article's *The Truncation and Its Error* read from the variation side.

## What Survives

**The frame's sector.** The variation of the frame's angles returns the parent's second boxed equation, and it is the chart's genuine dynamical content. **The frame of a real massive vector field is a dynamical object and its transport is exact.**

**The constraint.** The Lorenz condition is exact and it is one equation among four. **In the other families the analogous condition is the transversality of the polarisation**, and here it comes from the action's own structure.

**The absence of a quantum potential.** With no small parameter there is no term that plays the role of a correction, so nothing in this family deserves the name. **The corpus's language about a quantum potential does not transfer to the free Proca chart**, and the article records that rather than inventing one.

## The Noether Currents: The Stress and No Charge

**No charge, because there is no phase.** The Proca potential is real on the material sector, so a central phase rotation is not a symmetry of the action; the element article proves it and the chart inherits it. The parameter that would carry a charge, $\theta_{\mathrm{pha}}$, is not a variable of the branch, so there is no momentum to conserve and no density to call a charge.

**The stress.** Translation invariance gives the energy–momentum of the field, and in the chart its temporal component is the energy density,

$$
\mathcal{H}=\tfrac12\bigl(\epsilon\vec E^{2}+\vec B^{2}/\mu+k_m^{2}\lvert\vec A\rvert^{2}\bigr),
$$

with $\vec E$ and $\vec B$ the chart's fields. The energy is what the frame's transport conserves, and it is the only conserved quantity the free Proca action has.

**What the absence says about the limit.** A non-quantum limit is usually read as a particle limit, with a density and a flux. This family has neither, so the limit's language does not transfer: what survives is a field's stress and a constraint. That is the sharpest negative result of the family, and it is why the article refuses a truncation.

## The Truncation and Its Error

**What a non-quantum limit would delete.** The amplitude's kinetic term, by analogy with every other family. **What remains is $-\tfrac12k_m^{2}\varrho^{2}$ plus the frame's terms**, that is an algebraic amplitude and a dynamical frame.

**Why that is not an approximation here.** The deleted term is of the same size as the kept one for every solution, as the ratio $\omega^{2}/k_m^{2}$ shows. **An approximation whose discarded term equals the retained term is not an approximation**, and the article's claim is exactly this and no more.

**The comparison with the other families, in one table.**

| family | deleted term | size ratio to the kept terms | controlled |
|---|---|---|---|
| Klein–Gordon | $(\partial \varrho)^{2}$ | $\epsilon^{2}$ or $\delta^{2}$ | yes |
| Dirac | the frame's gradients | $\epsilon^{2}$ | yes |
| free Proca | $(\partial \varrho)^{2}$ | of order one | no |

**The third row is the article's result**, and the second row's entry is the reason the Dirac family could be treated at all: there the deleted terms are gradients of a frame that follows the momentum.

**What the variational route can still do.** It can state the constraint and the frame's transport as variations, which is exact. **It cannot justify a truncation, and the honest move is to say so and stop**, rather than to present a truncation whose error is unestimated because it is large.

## What the Variational Principle Adds to the Family

**Adds.**

*The obstruction as a comparison of coefficients.* A reader can see in one display that the amplitude's two blocks carry the same derivative count. **No order-counting argument is as convincing as two blocks with the same count.**

*The constraint's origin.* The Lorenz condition is a variation and not an extra assumption.

*The frame's dynamics as the surviving content.* What the chart is good for is stated positively: the boost's transport and the constraint.

**Does not add.**

*No controlled limit.* The article's negative result.

*No ray.* There is no phase to vary into a guidance equation.

*No estimate.* With no small parameter there is nothing to estimate, and no claim is made.

## Verification

**The derivative counts were checked from the display.** The amplitude's kinetic term carries two derivatives on $\varrho$; the mass term carries none; the frame's terms carry two on the connection. **The counts are an inspection and they are exact.**

**The size ratio was checked on a real plane wave.** With $\varrho=\lvert\vec A_0\rvert\lvert\cos(\omega t')\rvert$ and the Proca dispersion, the kinetic density is $\tfrac12\omega^{2}\lvert\vec A_0\rvert^{2}\sin^{2}(\omega t')$ and the mass density is $\tfrac12k_m^{2}\lvert\vec A_0\rvert^{2}\cos^{2}(\omega t')$; the ratio is $\omega^{2}\tan^{2}/k_m^{2}$, which is of order one at every time and unbounded near the zeros of the cosine. **The claim that the two are comparable holds at every time and fails only more strongly near the nodes.**

**The constraint was checked to be the trace.** Contracting the equation with the invertibles and taking the scalar part returns $\mathrm{Sc}(\tilde\nabla_\Phi^{\natural}\tilde A_\Phi)=0$, which is one real equation. **The count matches the parent's.**

**What was not checked.** No solution of the two boxed equations was integrated, and no error estimate was attempted. **The second omission is the result**: an error estimate would be an estimate of a quantity of order one.

## Summary

With the real word substituted, the Proca action's amplitude sector is $\tfrac12(\partial \varrho)^{2}-\tfrac12k_m^{2}\varrho^{2}$ plus the frame's terms, and both amplitude blocks carry two derivatives and a factor $k_m^{2}$.

For a real plane wave the two blocks are comparable at every time, with a ratio $\omega^{2}/k_m^{2}$ of order one. **So the non-quantum truncation, which would delete the amplitude's kinetic term, is not a controlled approximation in this family**, and the variational route's contribution is the precise form of that statement.

What survives is exact: the frame's transport and the Lorenz constraint, both variations of the same action. What does not survive is the language of a discarded term and a quantum potential, because there is no small parameter to make either meaningful.

The comparison with the other families is the ledger: the Klein–Gordon and Dirac truncations are controlled by $\epsilon$, and the Proca one is not controlled by anything.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde A_\Phi=a'_{t}e_{t}+\vec A$ | The real material four-vector |
| $\varrho>0$ | The scale; $\varrho^{2}=\mp\langle\tilde A_\Phi\rangle_\natural$ by branch |
| $\tilde U_{\Psi,\mathrm b}$ | The boost |
| $\Gamma_\mu$ | The frame's connection |
| $\varepsilon_\mu$ | The metric signs of the material sector |
| $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial r_{t}^{\prime\,2}$ | The d'Alembertian of the material sector |
| $k_m=mc/\hbar$ | The mass wave number |
| $\omega$ | The real plane wave's frequency, $\omega^{2}-\lvert\vec k\rvert^{2}=k_m^{2}$ |

## Further Reading

- [The Proca Equation in the Non-Quantum Limit](the-proca-equation-in-the-non-quantum-limit.html), the companion: the two brackets, the two boxed equations and the absent parameter.
- [The Lagrangian and the Proca Equation in Polar Variables](the-lagrangian-and-the-proca-equation-in-polar-variables.html), the parent: the action and its two variations.
- [The Proca Equation: Massive Spin 1 in Biquaternionic Form](the-proca-equation-massive-spin-1-in-biquaternionic-form.html), the element parent.
- [The Lagrangian and the Klein–Gordon Equation in the Non-Quantum Limit](the-lagrangian-and-the-klein-gordon-equation-in-the-non-quantum-limit.html), the scalar companion, where the deleted term is one order higher and the truncation is controlled.
- [The Non-Quantum Limit of the Biquaternion Model](the-non-quantum-limit-of-the-biquaternion-model.html), for the parameter and the difference between the limit and the approximation.
