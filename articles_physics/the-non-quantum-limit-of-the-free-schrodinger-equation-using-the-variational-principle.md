# __The Non-Quantum Limit of the Free Schrödinger Equation using the Variational Principle__

## Introduction

**The same limit, taken on the action.** Substitution into the equation and variation of the action give the same pair, and the corpus establishes that elsewhere. What the variational route adds here is three things the second-order family does not supply in the same form: the criterion read off the action's own term count, the density recognised as a Lagrange multiplier, and the exact statement of what the limit does to the constraint structure of a *first-order* system — which is nothing, and that is the result.

**The one term.** The polar action is four terms: the density times the phase rate, the density times the squared phase gradient, the amplitude's gradient squared, and the density times the potential. **The limit drops the third and keeps the other three.** The three that survive assemble into the density times a bracket that depends on the phase alone.

**The structural result, in one sentence.** Because the truncated Lagrangian is the density times a bracket in the phase, the density becomes the Lagrange multiplier of the Hamilton–Jacobi constraint, and its own equation is the conservation of the bracket's current.

**Why this family is not the second-order one.** There the parent carried the second time derivative of the amplitude, so the limit lowered the order in time and created a primary constraint whose consistency was the eikonal. Here the parent carries no time derivative of $r$ at all: $p_r=0$ before the limit and after it. **The order the limit lowers is the spatial order of the amplitude equation**, and the constraint count is unchanged. The eikonal is the *same* constraint both times; what changes is that it stops being a differential equation.

**What the article does not do.** It does not re-derive the polar action, the frame metric or the Jacobian argument; those are *The Variational Principle and the Schrödinger Equation in Biquaternionic Polar Variables*'s, and the article cites them. It does not take the nonrelativistic limit, which acts on the rest phase and does not exist in this family's normalization.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_\mu^{2}=-e_t$, $i$ central, $\mathrm{Sc}$ the coefficient of $e_t$, the pairing $\mathrm{Sc}(\cdot^{*}\cdot)$, $\Delta_\Phi$ the Laplacian, $t'$ the time. The word is $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon e_t$ with $\rho=r^{2}$ and $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$. The parameter is $\epsilon=1/(k_\Phi L)$ with $k_\Phi=\lvert\vec p\rvert/\hbar$ and $L$ the length over which $r$ or $\vec p$ varies, and the mass ratio $1/(k_mL)$ with $k_m=mc/\hbar$ sits beside it as the one-particle window.

## The Action in the Chart

**The polar action for the central field, in the operator setting.**

$$
S_{\mathrm{central}}=\int\mathrm{d}t'\,\mathrm{d}^{3}x\;\Bigl\{-\hbar\,r^{2}\dot\theta_{\mathrm{pha}}
-\frac{\hbar^{2}}{2m}\bigl(\lvert\vec\nabla_\Phi r\rvert^{2}+r^{2}\lvert\vec\nabla_\Phi\theta_{\mathrm{pha}}\rvert^{2}\bigr)
-r^{2}V_{\mathrm{op}}\Bigr\}.
$$

**Four terms, and one of them is not optional.** The parent says it plainly: the term in $\lvert\vec\nabla_\Phi r\rvert^{2}$ is the quantum potential's source, and dropping it is dropping the quantum potential.

| group | term | what it is | the limit |
|---|---|---|---|
| the phase's rate | $-\hbar\,r^{2}\dot\theta_{\mathrm{pha}}$ | the density times the frequency | keeps |
| the phase's gradient | $-\frac{\hbar^{2}}{2m}r^{2}\lvert\vec\nabla\theta_{\mathrm{pha}}\rvert^{2}$ | the density times the kinetic energy | keeps |
| the amplitude's gradient | $-\frac{\hbar^{2}}{2m}\lvert\vec\nabla r\rvert^{2}$ | the source of $Q$ | **drops** |
| the potential | $-r^{2}V_{\mathrm{op}}$ | the density times the potential | keeps |

**The action is the element action in other coordinates.** No term was added and none was dropped, and the only object that changed is the measure of the parameter space. On the central block the frame metric is diagonal with $g_{rr}=1$ and $g_{\theta\theta}=r^{2}$, and the density is $\rho=r^{2}$ exactly, with no rapidity factor.

**Which setting this is.** The Hamiltonian is a constant element, $\tilde H_\Psi=h_t\,e_t+i\vec h_\Psi$, in the polar parents; the operator setting is the same substitution in the field-theoretic action, and it is the one where a length $L$ exists. Both are in the parent, and neither result is transferred to the other. The article works in the operator setting because $\epsilon$ needs a region, and it names the polar potential $V=h_t\cosh\theta_{\mathrm{rpd}}+\sinh\theta_{\mathrm{rpd}}(\vec h_\Psi\cdot\vec u_{\mathrm b})$ only to warn that it is not $V_{\mathrm{op}}$: they coincide when the operator's potential is the constant $h_t$.

## The Criterion Measured on the Action

**Every term of the action is a density times a scalar.** Write $E=-\hbar\dot\theta_{\mathrm{pha}}$ and $\vec p=\hbar\nabla\theta_{\mathrm{pha}}$; then

$$
-\hbar\,r^{2}\dot\theta_{\mathrm{pha}}=r^{2}E,
\qquad
\frac{\hbar^{2}}{2m}r^{2}\lvert\nabla\theta_{\mathrm{pha}}\rvert^{2}=r^{2}\frac{\lvert\vec p\rvert^{2}}{2m},
\qquad
\frac{\hbar^{2}}{2m}\lvert\nabla r\rvert^{2}=r^{2}\frac{\hbar^{2}}{2mL^{2}}.
$$

**The last is the second times $\epsilon^{2}$, exactly.**

$$
\frac{\frac{\hbar^{2}}{2mL^{2}}}{\frac{\lvert\vec p\rvert^{2}}{2m}}=\frac{\hbar^{2}}{\lvert\vec p\rvert^{2}L^{2}}=\epsilon^{2}.
$$

**So the action's own term count is the criterion, and no argument is needed to get it.** The four terms are $r^{2}E$, $r^{2}T$, $r^{2}T\epsilon^{2}$ and $r^{2}V_{\mathrm{op}}$, and the only one that is smaller than the rest by a power of $\epsilon$ is the one the limit drops.

**This is where the first-order family is easier than the second.** In the Klein–Gordon action the same comparison of the amplitude's gradient with the phase's gradient also gives $\epsilon^{2}$, but there the mass term is larger than both for a slow particle, and it is tempting to compare against *it* instead, which gives $\delta^{2}$. **The temptation does not exist here**, because the largest term is the phase's own kinetic energy and the potential, both of the same order as the phase's gradient. The rule is one rule for the whole corpus, and this family is where it is hardest to get wrong.

**The one term that is not ordered at all.** $r^{2}V_{\mathrm{op}}$ is kept at full strength and is not small in $\epsilon$; what the approximation needs is that $V_{\mathrm{op}}$ be smooth on the de Broglie scale, so that its gradient does not enter at an order the expansion has not kept. That is a condition on the potential and not a parameter of the problem, and it is the standard condition the phase-integral method needs.

**The second ratio, and why it is not the criterion.**

$$
\frac{1}{k_mL}=\frac{\hbar}{mcL},
$$

**the Compton wavelength over $L$.** In this family $\hbar\omega$ is not the dominant term of the equation — the rest energy is already divided out of the Schrödinger equation, by the theory and not by a limit — so the mass length does not compete with the phase. A small $1/(k_mL)$ says the region is large against the Compton length, which is the condition for a one-particle description and for the nonrelativistic treatment to be consistent. **It is a precondition and not the limit**, and the audit records the same verdict.

**One nesting statement, since the corpus uses both.** In a relativistic family the two ratios satisfy $\delta=\epsilon\lvert\vec p\rvert/(mc)<\epsilon$; here the analogue is $1/(k_mL)=\epsilon\lvert\vec p\rvert/(mc)$, the same relation with the same content. The limit is the larger of the two and always implies the window.

## The Truncated Action

**Delete the amplitude's gradient and nothing else.**

$$
S^{\mathrm{trunc}}=\int\mathrm{d}t'\,\mathrm{d}^{3}x\;r^{2}\Bigl[-\hbar\dot\theta_{\mathrm{pha}}
-\frac{\hbar^{2}}{2m}\lvert\vec\nabla\theta_{\mathrm{pha}}\rvert^{2}-V_{\mathrm{op}}\Bigr].
$$

**The bracket depends on the phase alone.** That is the whole of the truncation: $r$ survives only as the factor in front.

**Varying the phase.**

$$
\frac{\partial}{\partial t'}\bigl(\hbar\,r^{2}\bigr)+\vec\nabla\cdot\Bigl(\frac{\hbar^{2}}{m}r^{2}\vec\nabla\theta_{\mathrm{pha}}\Bigr)=0
\qquad\Longleftrightarrow\qquad
\frac{\partial\rho}{\partial t'}+\vec\nabla\cdot\Bigl(\rho\frac{\vec\nabla S_{\tilde\Xi}}{m}\Bigr)=0 ,
$$

with $\rho=r^{2}$ and $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$. **This is the continuity equation, exact, and the truncation did not touch it**, because the discarded term contains no $\theta_{\mathrm{pha}}$.

**Varying the amplitude.**

$$
-\hbar\dot\theta_{\mathrm{pha}}-\frac{\hbar^{2}}{2m}\lvert\nabla\theta_{\mathrm{pha}}\rvert^{2}-V_{\mathrm{op}}=0
\qquad\Longleftrightarrow\qquad
\frac{\partial S_{\tilde\Xi}}{\partial t'}+\frac{\lvert\nabla S_{\tilde\Xi}\rvert^{2}}{2m}+V_{\mathrm{op}}=0 .
$$

**This is the Hamilton–Jacobi equation and nothing else.** The quantum potential was the discarded term's variation and went with it.

**So the truncated action's two Euler–Lagrange equations are the limit's two equations, exactly.** Not to leading order and not up to a remainder: exactly, because $\Delta_\Phi r$ can only come from $\lvert\nabla r\rvert^{2}$ and there is no other source.

**The checks.** Both variations were verified on a $31\times31$ grid against a central difference of the discrete action: the amplitude variation to $3\times10^{-6}$ relative in both the exact and the truncated functionals, and the phase variation to $4\times10^{-7}$ relative, reproducing the divergence form above and not its negative.

**One line, and it is the article's summary.** Everything the limit drops sits in one term, and everything the limit keeps sits in the other three, and the dropped term is the only one that carries a derivative of $r$.

## The Density Is the Multiplier

**The truncated Lagrangian has the form**

$$
\mathcal L^{\mathrm{trunc}}=r^{2}F(\theta,\nabla\theta),
\qquad
F=-\hbar\dot\theta_{\mathrm{pha}}-\frac{\hbar^{2}}{2m}\lvert\nabla\theta_{\mathrm{pha}}\rvert^{2}-V_{\mathrm{op}} .
$$

**Varying $r$ gives $2rF=0$, that is $F=0$.** The density is not determined by its own variation; it multiplies the constraint. **In the truncated theory $r^{2}$ is the Lagrange multiplier of the Hamilton–Jacobi constraint**, and the multiplier is a field with its own dynamics.

**Its dynamics is the conservation of the constraint's current.** The variation of $\theta_{\mathrm{pha}}$ is

$$
\partial_\mu\Bigl(r^{2}\frac{\partial F}{\partial(\partial_\mu\theta_{\mathrm{pha}})}\Bigr)=0 ,
$$

which is continuity again, now read as the statement that **the multiplier is transported by the current of the constraint it multiplies.** A Lagrange multiplier that is a constant would give no equation; a multiplier that is a field gives one, and the equation is the transport of the density along the flow the constraint defines.

**The same structure appears in the second-order family, and there it is new.** In the truncated Klein–Gordon action the density likewise multiplies the mass shell, and the phase variation likewise gives the transport equation. The difference is in the parent: there $r$ was dynamical at second order in time, and the truncation is what demoted it to a multiplier. **Here the parent already had $r$ without a time derivative, and the truncation completes a demotion that was half made.**

**How half made.** In the parent, $r$ enters through $\lvert\nabla r\rvert^{2}$ and through the overall $r^{2}$ of the other three terms. So the parent's Lagrangian is not $r^{2}F$ but $r^{2}F-\frac{\hbar^{2}}{2m}\lvert\nabla r\rvert^{2}$: the multiplier structure is there with one term spoiling it. Dropping that term is what makes $r$ a pure multiplier, and the quantum potential is exactly the price of the spoiling.

**A corollary worth stating.** The multiplier form makes the truncated system's two equations independent in a way the parent's are not. In the parent the phase equation contains $r$ through $\rho$ and the amplitude equation contains $r$ through $\Delta_\Phi r$; neither can be solved without the other. In the truncated system the constraint contains no $r$ at all, so it can be solved first. **The truncation is what decouples them.**

## The Limit Does Not Create a Constraint Here

**The parent is already degenerate.** The momentum conjugate to the amplitude is

$$
p_r=\frac{\partial\mathcal L}{\partial\dot r}=0 ,
$$

identically, because the action is first order in time. The parent records this: four of the eight momenta vanish, and on the central field the vanishing one is $p_r$. **So the primary constraint exists before the limit and is not created by it.**

**The secondary constraint is the amplitude equation, and it changes character rather than count.** Its consistency requires $\dot p_r=\partial\mathcal L/\partial r=0$, which is

$$
-2\hbar r\dot\theta_{\mathrm{pha}}-\frac{\hbar^{2}}{m}r\lvert\nabla\theta_{\mathrm{pha}}\rvert^{2}+\frac{\hbar^{2}}{m}\Delta_\Phi r-2rV_{\mathrm{op}}=0
$$

in the parent and

$$
-2\hbar r\dot\theta_{\mathrm{pha}}-\frac{\hbar^{2}}{m}r\lvert\nabla\theta_{\mathrm{pha}}\rvert^{2}-2rV_{\mathrm{op}}=0
$$

in the truncated theory. **The two differ by one term, and that term is the only differential operator in either.** So the constraint count is the same, and what changes is that the secondary constraint stops being a differential equation in space.

**The order lowered is spatial, and the layer is spatial.** In the second-order family the limit lowered the order in time and the layer was an initial layer. Here the order with respect to time is one in both theories and the order with respect to space falls from two to zero, so the layer is a **spatial** layer: the region where the amplitude varies on the de Broglie scale, of width $L$ with $\epsilon\sim1$. Outside it $r$ is determined by the transport equation and inside it the truncated constraint has no claim.

**One consequence, and it is the reason the first-order family is the clean one.** A constraint that is algebraic in the fields can be solved for the phase at every point, and the phase is what the flow is made of. So the truncated system determines the phase first, pointwise, and the density afterwards by transport. **The limit reduces a coupled system of two partial differential equations to one algebraic equation and one transport equation.**

## The Triangular Structure

**After the truncation, in order.**

1. The Hamilton–Jacobi equation fixes $S_{\tilde\Xi}$ from the data, and it is first order in time and second order in space.
2. The flow is fixed by the phase, $\vec v=\nabla S_{\tilde\Xi}/m$.
3. The continuity equation fixes $\rho$ along that flow, by quadrature.
4. Nothing else is required: $r=\sqrt{\rho}$ and the pair is solved.

**Before the truncation the same list does not close.** Step one needs $Q$, which needs $r$; step three needs $S_{\tilde\Xi}$; and the two are coupled through $\Delta_\Phi r$ in a way that no ordering removes. **The limit is what makes the list an algorithm**, and this is the variational statement corresponding to the substitution route's remark that the eikonal and the transport equation are the classical recipe.

**The same four steps in the second-order family**, with the mass shell in place of the Hamilton–Jacobi equation and the dust flow in place of the gradient flow. The triangular structure is a property of the limit and not of the family.

## Noether in the Limit

**The density is the canonical momentum.**

$$
p_{\theta}=\frac{\partial\mathcal L}{\partial\dot\theta_{\mathrm{pha}}}=-\hbar\,r^{2}=-\hbar\,\rho ,
$$

**exactly, and this is the first-order family's defining feature.** The parent says it: in a second-order action the momentum conjugate to the phase is proportional to the phase rate, and the statement that the density *is* the momentum belongs to the first-order cases. Here the density is the momentum, and the coefficient is $-\hbar$.

**Three consequences, and each is a difference from the second-order family.**

*The sign of the density is fixed by the action.* $\rho=-p_\theta/\hbar$ and $\rho>0$, so the density is positive definite and there is no indefinite charge to inherit. **The first-order family has no defect of the second-order family's kind**, and the variational route shows the mechanism: the density is a momentum whose sign the action's overall coefficient fixes, and there is no second sheet for the limit to keep.

*The truncation does not change the current.* Both the exact and the truncated current are $\vec j=\rho\nabla S_{\tilde\Xi}/m$, because the discarded term contains neither $\rho$'s rate nor the phase.

*The energy is the truncated Hamiltonian.*

$$
H^{\mathrm{trunc}}=\int\mathrm{d}^{3}x\;r^{2}\Bigl[\frac{\lvert\nabla S_{\tilde\Xi}\rvert^{2}}{2m}+V_{\mathrm{op}}\Bigr],
$$

**which is the density times the classical energy and is non-negative for $V_{\mathrm{op}}\ge0$.** In the parent the energy carries the extra $\frac{\hbar^{2}}{2m}\lvert\nabla r\rvert^{2}$, which is the quantum fluid's internal stress; the truncated energy is the energy of a pressureless fluid, and the discarded term is exactly the pressure.

**The conservation law's status.** In the truncated theory continuity *is* the phase's Euler–Lagrange equation, so it is the symmetry's equation and not a consequence of the dynamics. **A limit cannot spoil a conservation law that is itself a variation**, and that is why the transport equation survives untouched in both routes. The variational argument is the reason; the substitution route records the fact.

## What the Variational Route Adds

**Four things, and each is checked against the substitution article.**

*The criterion without an argument.* The action's four terms are $r^{2}E$, $r^{2}T$, $r^{2}T\epsilon^{2}$ and $r^{2}V_{\mathrm{op}}$, so the ratio of the dropped term to the kept ones is $\epsilon^{2}$ as a matter of inspection. The substitution route must compare $Q$ with the sensitivity of the momentum, which is the same ratio reached by a longer road. **Here the term count and the criterion are the same statement**, and the second-order family's temptation to compare against the mass term has no counterpart.

*A functional for the limit.* The truncated action is the action whose variations are the limit's equations, and its Lagrangian is the density times a bracket in the phase. The substitution route produces equations and no functional.

*The multiplier.* The truncated Lagrangian has the form $r^{2}F(\theta)$ with $F$ the Hamilton–Jacobi constraint, so the density is a Lagrange multiplier with its own equation. **That reading is available only from the action**, and it makes the decoupling of the two equations a fact about the form of $\mathcal L$ and not a remark about the equations.

*The exact statement of what does not change.* $p_r=0$ in the parent and in the truncated theory, so the limit creates no constraint in this family. The substitution route can only observe that the quantum potential disappears; the action shows that its disappearance is a change in the *character* of one secondary constraint and not in the count.

**What it does not add.** No new equation, no new solution, no new invariant. The pair is the substitution article's pair, and the equivalence of the two routes is exact in both directions on the $N$-regular set, by the parent's Jacobian argument.

## The Two Routes Are Equivalent, and the Proof Is One Line

**The residuals are the Jacobian's image.** For a real variation of the parameters,

$$
\delta S=2\,\mathrm{Re}\int\mathrm{d}t'\,\mathrm{Sc}\bigl[\delta\tilde\Xi^{*}E\bigr],
\qquad
E=i\hbar\,\partial_{t'}\tilde\Xi-\tilde H_\Psi\tilde\Xi ,
$$

so the eight Euler–Lagrange residuals are $R_a=2\,\mathrm{Re}\,\mathrm{Sc}\bigl[(\partial\tilde\Xi/\partial p_a)^{*}E\bigr]$. **The eight vectors $\partial\tilde\Xi/\partial p_a$ are the columns of the word's real Jacobian, which is invertible on the units, so the residuals vanish exactly when $E$ vanishes.**

**What that gives for this article.** The exact polar action's equations are the Schrödinger equation's, so the exact pair is exact in both routes. The truncated action's equations are the limit's pair, so the limit is exact in both routes. **The equivalence is inherited by the truncation** because the truncation is a change in the functional and both routes truncate the same object.

**Where the two routes differ, and it is only in the reading.** The substitution route says which equations survive; the variational route says which functional they vary, and therefore what kind of problem the limit leaves behind. That difference is the multiplier, the unchanged constraint count, and the spatial rather than temporal character of the singular passage.

## Where the Limit Does and Does Not Reach

**Reaches.** It deletes one term, produces the pair exactly, makes the density a multiplier, decouples the two equations, preserves continuity and the sign of the density, and turns the energy into dust's.

**Does not reach.** It does not supply a uniform approximation at a turning point, at a caustic, or where the amplitude varies on the de Broglie scale; it does not order the potential, which needs its own smoothness condition; and it does not act on the algebra, which the audit's *The Limit Is Not the Contraction* establishes.

**One qualification the action makes visible.** The truncated constraint is algebraic, so the phase is determined pointwise from the potential. Where $V_{\mathrm{op}}$ has a discontinuity, so does the phase's rate, and the density responds through the transport equation alone. **The limit's classical object is therefore a flow whose acceleration is $-\nabla V_{\mathrm{op}}/m$ and whose density is transported by it**, which is the dust reading again and is the same object the substitution route produces.

## Summary

The polar action of the free Schrödinger field is four terms, and with $E=-\hbar\dot\theta_{\mathrm{pha}}$ and $\vec p=\hbar\nabla\theta_{\mathrm{pha}}$ they are $r^{2}E$, $r^{2}\lvert\vec p\rvert^{2}/(2m)$, $r^{2}\hbar^{2}/(2mL^{2})$ and $r^{2}V_{\mathrm{op}}$. The third is the second times $\epsilon^{2}=1/(k_\Phi L)^{2}$, so the action's own term count is the criterion and no sensitivity argument is needed. The limit drops the third term, the amplitude's gradient, and what is left is the density times a bracket in the phase alone.

The truncated action's two variations are the Hamilton–Jacobi equation and the continuity equation, exactly and not to leading order, because $\Delta_\Phi r$ has no other source. Its Lagrangian has the form $r^{2}F(\theta)$ with $F$ the constraint, so **the density is the Lagrange multiplier of the Hamilton–Jacobi constraint** and its own equation is the transport of the multiplier by the constraint's current. In this family the parent already had $p_r=0$, so the limit creates no constraint: it changes the secondary constraint from a second-order spatial equation into an algebraic one, and the layer it fails in is spatial and of width $L$ with $\epsilon\sim1$. The density is the canonical momentum, $p_\theta=-\hbar\rho$, so it is positive definite, there is no indefinite charge, and the truncated energy is dust's. The two routes are equivalent by the word's Jacobian, and the variational route's contribution is the reading: the multiplier, the unchanged constraint count, and the spatial character of the passage.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S_{\mathrm{central}}$ | The polar action; four terms |
| $-\hbar r^{2}\dot\theta_{\mathrm{pha}}$ | The density times the phase rate; $=r^{2}E$ |
| $-\frac{\hbar^{2}}{2m}r^{2}\lvert\nabla\theta_{\mathrm{pha}}\rvert^{2}$ | The density times the kinetic energy; $=r^{2}T$ |
| $-\frac{\hbar^{2}}{2m}\lvert\nabla r\rvert^{2}$ | The amplitude's gradient; the only term dropped; $=r^{2}T\epsilon^{2}$ |
| $-r^{2}V_{\mathrm{op}}$ | The density times the potential; kept, and ordered by its own smoothness |
| $\rho=r^{2}$ | The density; and the canonical momentum, $p_\theta=-\hbar\rho$ |
| $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$ | The action |
| $\epsilon=1/(k_\Phi L)$ | The parameter of the limit |
| $1/(k_mL)$ | The one-particle window; a precondition, not the limit |
| $S^{\mathrm{trunc}}=\int r^{2}F$ | The truncated action; $F$ the Hamilton–Jacobi constraint |
| $F=0$ | The constraint the density multiplies |
| $p_r=0$ | The primary constraint, in the parent and in the truncation |
| $H^{\mathrm{trunc}}=\int r^{2}[\lvert\nabla S\rvert^{2}/2m+V_{\mathrm{op}}]$ | The truncated energy; dust's |

## Further Reading

- E. Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1927) 322–326, for the hydrodynamic action of the pair.
- T. Takabayasi, "On the formulation of quantum mechanics associated with classical pictures," *Progress of Theoretical Physics* **8** (1952) 143–182, for the hydrodynamic reading and its constraints.
- P. A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for primary and secondary constraints and the treatment of a multiplier that is a field.
- H. Goldstein, C. P. Poole, and J. L. Safko, *Classical Mechanics* (Addison-Wesley, 2002), for the Hamilton–Jacobi equation, its characteristics and the multiplier form of a constrained variational problem.
- C. M. Bender and S. A. Orszag, *Advanced Mathematical Methods for Scientists and Engineers* (Springer, 1999), chapters 9 and 10, for singular perturbation, the lowering of derivative order and the width of the resulting layer.
- J. B. Keller, "Corrected Bohr–Sommerfeld quantum conditions for nonseparable systems," *Annals of Physics* **4** (1958) 180–188, for the eikonal as a first-order equation whose characteristics are the rays.
- M. V. Berry and K. E. Mount, "Semiclassical approximations in wave mechanics," *Reports on Progress in Physics* **35** (1972) 315–397, for the conditions the potential must satisfy for the short-wavelength expansion to be uniform.
