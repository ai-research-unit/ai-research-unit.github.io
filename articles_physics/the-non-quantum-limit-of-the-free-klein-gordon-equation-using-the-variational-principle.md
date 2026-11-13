# __The Non-Quantum Limit of the Free Klein–Gordon Equation using the Variational Principle__

## Introduction

**The same limit, taken on the action instead of on the equation.** Substitution into the equation and variation of the action give the same pair, and the corpus establishes that elsewhere. What the variational route adds is a second statement of the criterion, a functional for the limit, and the character of the passage: **the limit is the deletion of one term from a Lagrangian, and that deletion turns a regular variational problem into a constrained one.**

**The one term.** The polar action of the Klein–Gordon field is three terms: the amplitude's gradient squared, the density times the squared phase gradient, and the density times the rest mass squared. The limit drops the first. What is left is a functional of the phase alone, weighted by a density that the phase's own equation then transports.

**The criterion, measured on the action.** With the rest energy in the phase, the phase's gradients are of order $k_m$ and the amplitude's gradients are of order $1/L$. So the three terms are of order one, order one and order $\delta^{2}$ with $\delta=1/(k_mL)$, and the limit is the statement that the third is negligible. **The two order-one terms must balance each other, and their balance is the eikonal.** That is the variational form of the criterion, and it is stricter than the equation-level one because it says which two terms balance and not merely which one is dropped.

**The character of the passage.** Dropping the amplitude's gradient removes the second time derivative of $r$ from the problem. The conjugate momentum of $r$ vanishes identically, the Legendre transform becomes degenerate, and the equation that consistency forces is the eikonal. **The non-quantum limit of a second-order field is the passage from a regular to a constrained variational problem, and the eikonal is the constraint that the degeneracy produces.** This is the article's structural result, and it has no counterpart in the substitution route.

**What the article does not do.** It does not re-derive the polar action, the frame metric or the Jacobian argument; those are the variational polar companion's. It does not take the nonrelativistic limit, which is the parent's and which acts on the rest phase rather than on the amplitude.

**Conventions.** Those of the free companion: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_\mu^{2}=-e_t$, $i$ central, $\mathrm{Sc}$ the coefficient of $e_t$, the pairing $\mathrm{Sc}(\cdot^{*}\cdot)$, $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial {r'_{t}}^{2}$ with $r'_t=c\,t'$, $k_m=mc/\hbar$. The word is $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon e_t$ with $\rho_{\mathrm{num}}=r^{2}$ and $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$. The parameter is $\delta=1/(k_mL)$ with $L$ the length over which $r$ varies.

## The Action in the Chart

**The polar action.** Substituting the word into the element action gives, for the central field,

$$
S_{\mathrm{central}}=\int\mathrm{d}^{4}x\;\Bigl\{(\partial_{r'_t}r)^{2}-\lvert\nabla r\rvert^{2}
+r^{2}\bigl[(\partial_{r'_t}\theta_{\mathrm{pha}})^{2}-\lvert\nabla\theta_{\mathrm{pha}}\rvert^{2}\bigr]-k_m^{2}r^{2}\Bigr\}.
$$

**Three groups of terms, and they are the whole of the article.**

| group | term | what it is |
|---|---|---|
| the amplitude's gradient | $(\partial r)^{2}-\lvert\nabla r\rvert^{2}$ | the kinetic term of the scale |
| the density times the phase's square | $r^{2}[(\partial\theta)^{2}-\lvert\nabla\theta\rvert^{2}]$ | the kinetic term of the angle |
| the density times the rest term | $k_m^{2}r^{2}$ | the mass term |

**The action is the element action in other coordinates.** No term was added and none was dropped; the only object that changed is the measure of the parameter space. The frame metric of the general element is the variational companion's, and on the central block it is diagonal with $g_{rr}=1$ and $g_{\theta\theta}=r^{2}$.

**The two variations, for reference.** Varying $\theta_{\mathrm{pha}}$ gives the transport equation and varying $r$ gives the amplitude equation with $Q$, and the pair is the free companion's exactly. The article's subject is what happens to the action, and therefore to the pair, when one group of terms is removed.

## The Criterion Measured on the Action

**The phase's gradients are of order $k_m$, and that is a statement about the rest energy.** The action is written with the rest energy inside the phase, so $\partial_{r'_t}S_{\tilde\Xi}=-E/c$ and $E\simeq mc^{2}$ in the regime the limit addresses. Hence

$$
(\partial_{r'_t}\theta_{\mathrm{pha}})^{2}-\lvert\nabla\theta_{\mathrm{pha}}\rvert^{2}
=\frac{1}{\hbar^{2}}\Bigl[\Bigl(\frac{E}{c}\Bigr)^{2}-\lvert\vec p\rvert^{2}\Bigr]\sim k_m^{2},
$$

and the phase's kinetic term is the same size as the mass term. **Both are order one, and the eikonal is the statement that they differ by a term of order $\delta^{2}$.**

**The amplitude's gradients are of order $1/L$.** With $r$ varying over $L$,

$$
(\partial r)^{2}\sim\frac{r^{2}}{L^{2}}=r^{2}k_m^{2}\,\delta^{2}.
$$

**So the three groups stand in the ratios $1:1:\delta^{2}$, and one number compares all three.** The criterion is not an extra input; it is the ratio of two terms that both stand in the same functional. That is the whole of what the variational route contributes to the definition, and it is the cleanest statement of the criterion in the corpus: **the small quantity is the amplitude's gradient against the rest term, and everything else in the action is of the same size and must be kept.**

**A warning that the statement is about the normalization.** If the rest phase is divided out first, as the nonrelativistic limit does, then the remaining phase $\sigma$ has gradients of order $\lvert\vec p\rvert$ and the ratios change: the phase's term becomes order $\beta^{2}$ and the amplitude's order $\epsilon^{2}$. The statement "the phase's gradients are order one" is therefore a statement about the relativistic normalization in which the rest energy sits in the phase, and it is the normalization the limit of this article is written in.

## The Truncated Action

**Drop the first group.**

$$
S^{\mathrm{trunc}}_{\mathrm{central}}=\int\mathrm{d}^{4}x\;\Bigl\{r^{2}\bigl[(\partial_{r'_t}\theta_{\mathrm{pha}})^{2}-\lvert\nabla\theta_{\mathrm{pha}}\rvert^{2}\bigr]-k_m^{2}r^{2}\Bigr\}.
$$

**Two variations, and neither produces $Q$.**

*Varying $\theta_{\mathrm{pha}}$* gives

$$
\nabla\cdot\bigl(r^{2}\nabla S_{\tilde\Xi}\bigr)-\frac{\partial}{\partial r'_t}\bigl(r^{2}\partial_{r'_t}S_{\tilde\Xi}\bigr)=0 ,
$$

which is the transport equation, exact and unchanged. **The truncation does not touch it**, because the dropped term contains no $\theta_{\mathrm{pha}}$.

*Varying $r$* gives

$$
2r\Bigl[(\partial_{r'_t}\theta_{\mathrm{pha}})^{2}-\lvert\nabla\theta_{\mathrm{pha}}\rvert^{2}-k_m^{2}\Bigr]=0
\qquad\Longrightarrow\qquad
\Bigl(\frac{\partial S_{\tilde\Xi}}{\partial r'_t}\Bigr)^{2}-\lvert\nabla S_{\tilde\Xi}\rvert^{2}=m^{2}c^{2}
$$

away from $r=0$, which is the eikonal and nothing more. **The quantum potential was in the discarded group and went with it.**

**So the truncated action's two Euler–Lagrange equations are the limit's two equations, exactly.** Not to leading order and not up to a remainder: exactly, because the discarded group is the only place $\Box_\Phi r$ can come from. That is the sharpest form of the equivalence between the two routes: **the limit of the equations is the variation of the truncated action.**

**One line, and it is the article's summary.** Everything the limit drops sits in one group of terms, and everything the limit keeps sits in the other two.

## The Limit Is Singular

**What the truncation does to the order.** In the exact action the term $(\partial_{r'_t}r)^{2}$ carries two time derivatives of $r$, so the amplitude equation is second order and the Cauchy data are $(r,\partial_{r'_t}r)$. In the truncated action that term is gone, so the equation for $r$ carries no derivative of $r$ at all: it is algebraic in the fields and constrains $\theta_{\mathrm{pha}}$ alone. **One initial datum is lost, and it is $\partial_{r'_t}r$.**

**A singular limit in the technical sense.** A perturbation that lowers the order of an equation's highest derivative is singular: the solutions of the perturbed problem do not converge uniformly to a solution of the unperturbed one on the whole domain, and a boundary or initial layer appears. Here the layer is at the places where $\partial_{r'_t}r$ would have been large, which is where $\delta$ is not small, and the layer's width is the Compton length.

**The Legendre transform degenerates, and the eikonal is the constraint.** The momentum conjugate to $r$ is

$$
p_r=\frac{\partial\mathcal L^{\mathrm{trunc}}}{\partial(\partial_{r'_t}r)}=0 ,
$$

identically, because $r$ appears in the truncated Lagrangian with no time derivative. So the truncated problem has a primary constraint, and its consistency requires $\dot p_r=0$, which is

$$
\frac{\partial\mathcal L^{\mathrm{trunc}}}{\partial r}=2r\Bigl[(\partial_{r'_t}\theta_{\mathrm{pha}})^{2}-\lvert\nabla\theta_{\mathrm{pha}}\rvert^{2}-k_m^{2}\Bigr]=0 .
$$

**The secondary constraint is the eikonal.** The variational companion records that the exact second-order problem has an invertible kinetic matrix and no constraints, and contrasts it with the first-order families where four momenta vanish. The limit supplies the missing case: **a second-order family acquires a constraint precisely in the limit, and the constraint is the classical equation of motion.** The eikonal is not an equation that happens to be first order; it is a constraint, and that is why it constrains the phase alone.

**The system becomes triangular.** In the exact problem the two equations each contain both functions and are coupled at second order. In the truncated problem

1. the eikonal is a first-order equation for $\theta_{\mathrm{pha}}$ alone;
2. the flow is then fixed, $\vec v=\nabla S_{\tilde\Xi}/m$;
3. the transport equation is a first-order equation for $\ln r$ along that flow;
4. and $r$ follows by quadrature along the rays.

**The limit triangularises the system, and that is why it is solvable.** A first-order equation for the phase, then a flow, then a transport along the flow: this is the classical recipe, and the triangular structure is what the discarded group was hiding.

**Where the discarded branch lives.** The lost datum is $\partial_{r'_t}r$; the solutions it would have selected are the ones whose amplitude changes on the Compton scale. They are not lost by an error of the method: they are the solutions for which $\delta$ is not small, and the approximation has no claim on them. **The singular character and the region of validity are the same statement**, which is what the substitution route can only assert and what the action exhibits.

## What the Variational Route Adds

**Four things, and each is checked.**

*The criterion at action level.* The substitution route compares $Q$ with the mass in the equation. The variational route compares the amplitude's gradient with the rest term in the Lagrangian, and the two comparisons are the same comparison because the amplitude equation is the variation of exactly those terms. The action-level form is the sharper one, because it says which two terms must balance — the phase's kinetic term and the mass term — and that balance is the eikonal.

*A functional for the limit.* The substitution route produces equations and no action. The truncated action is the action whose variations are the limit's equations, so the limit has a variational principle of its own and not only a pair of equations.

*The character of the passage.* The order drop, the vanishing momentum and the constraint are visible only from the action. **The eikonal's status as a constraint is a variational fact**, and no manipulation of the field equation displays it.

*The conservation law's status.* In the exact theory the charge conservation follows from the equation and its conjugate. In the truncated theory the transport equation *is* the Euler–Lagrange equation of the phase, so conservation is the symmetry's equation and not a consequence of the dynamics. **The limit cannot spoil a conservation law that is itself a variation**, and that is why the transport equation survives untouched in both routes. The variational argument is the reason; the substitution route records the fact.

**What it does not add.** It adds no new equation, no new solution, and no new invariant. The pair is the pair. Both routes give the free companion's equations, and the equivalence is exact in both directions on the $N$-regular set.

**A note on the two routes' scope.** The variational route needs the word to be a bijection with a smooth inverse, so its equations hold on the $N$-regular set and nowhere else. The substitution route has the same restriction, since it substitutes the same word. The difference is that the action inherits the restriction as a domain of definition of a functional, and the substitution inherits it as a domain of differentiability of a function.

## Noether in the Limit

**The charge.** The phase's Noether current in the truncated theory is

$$
j_{r'_t}=2r^{2}\partial_{r'_t}\theta_{\mathrm{pha}}=-\frac{2r^{2}E}{\hbar c},
\qquad
j_\eta=-2r^{2}\partial_{r_\eta}\theta_{\mathrm{pha}},
$$

which is the exact theory's current with the same amplitude. **The truncation does not change the current**, because the current is built from $r$ and $\partial\theta$ and the discarded group contains neither in a form that enters the Noether computation.

**The charge is indefinite and the energy is not.** The charge is linear in the phase rate and the energy is quadratic in it, so

$$
\rho_{\mathrm{chg}}\ \text{changes sign with the sheet},
\qquad
T^{00}=(\partial_{r'_t}r)^{2}+\lvert\nabla r\rvert^{2}+r^{2}\bigl[(\partial_{r'_t}\theta)^{2}+\lvert\nabla\theta\rvert^{2}\bigr]+k_m^{2}r^{2}>0 .
$$

**In the truncated theory the energy loses its first two terms and stays positive**, so the limit preserves the asymmetry: the charge can be negative and the energy cannot. The free companion reaches that asymmetry from the current; the action reaches it from the two Noether charges' degrees in the velocity. **The limit does not repair the defect, and the action shows why it cannot**: the defect is a power of the velocity and the truncation removes a term that is even in it.

**One consequence worth stating.** Because the amplitude's gradient term is dropped from the energy and not from the charge, the truncated energy is $r^{2}[(\partial\theta)^{2}+|\nabla\theta|^{2}+k_m^{2}]$, which is the energy of a pressureless fluid with a rest density. **The limit's energy is dust's energy**, and the discarded terms are exactly the pressure-like terms of the quantum fluid. That is another name for the same statement as the eikonal's: the quantum potential is the fluid's internal stress and the limit is the passage to dust.

## What the Limit Does and Does Not Do

**Does.** It deletes one group of terms from a Lagrangian, produces a pair of equations that are the truncated action's variations, lowers the order, creates a constraint whose consistency is the eikonal, triangularises the system, and preserves the exact transport equation and the sign structure of the charge.

**Does not.** It does not select a sheet of the mass shell; it does not remove the second sheet; it does not supply a uniform approximation at a caustic; and it does not produce a state.

**The one sentence for the record.** Substitution says which equations survive; variation says which functional they vary, and therefore what kind of problem the limit leaves behind.

## Summary

The polar action of the free Klein–Gordon field is three groups of terms: the amplitude's gradient squared, the density times the squared phase gradient, and the density times the rest term. With the rest energy in the phase the phase's gradients are of order $k_m$ and the amplitude's are of order $1/L$, so the three groups stand in the ratios $1:1:\delta^{2}$ with $\delta=1/(k_mL)$. The limit drops the first group. What remains is a functional of the phase weighted by a density, and its two Euler–Lagrange equations are the eikonal $(\partial S)^{2}-|\nabla S|^{2}=m^{2}c^{2}$ and the exact transport equation — the limit's pair, exactly and not to leading order.

The passage is singular. The discarded group carried the second time derivative of $r$, so the conjugate momentum of $r$ vanishes identically in the truncated theory, the Legendre transform degenerates, and the consistency condition is the eikonal. **The eikonal is a constraint, and the limit is what creates it.** The truncated system is triangular: the eikonal fixes the phase, the phase fixes the flow, the transport fixes the density along the flow. The charge current and the charge's indefiniteness survive the truncation unchanged, the energy loses its pressure-like terms and stays positive, and the truncated energy is dust's.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S_{\mathrm{central}}$ | The polar action; three groups of terms |
| $(\partial r)^{2}-\lvert\nabla r\rvert^{2}$ | The amplitude's gradient; dropped by the limit |
| $r^{2}[(\partial\theta)^{2}-\lvert\nabla\theta\rvert^{2}]$ | The density times the phase's square; kept |
| $k_m^{2}r^{2}$ | The rest term; kept |
| $\delta=1/(k_mL)$ | The parameter; the ratio of the third group to the first two |
| $S^{\mathrm{trunc}}_{\mathrm{central}}$ | The truncated action; the limit's functional |
| $p_r=\partial\mathcal L^{\mathrm{trunc}}/\partial(\partial_{r'_t}r)=0$ | The primary constraint created by the truncation |
| $(\partial S)^{2}-\lvert\nabla S\rvert^{2}=m^{2}c^{2}$ | The secondary constraint, which is the eikonal |
| $j_{r'_t}=-2r^{2}E/(\hbar c)$ | The charge current; unchanged by the truncation |
| $T^{00}>0$ | The energy; positive on both sheets, in both theories |

## Further Reading

- E. Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1927) 322–326, for the hydrodynamic action of the pair.
- T. Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 2–80, for the relativistic action and its constraints.
- P. A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for primary and secondary constraints and the degenerate Legendre transform.
- C. M. Bender and S. A. Orszag, *Advanced Mathematical Methods for Scientists and Engineers* (Springer, 1999), chapters 9 and 10, for singular perturbation and the loss of a boundary condition.
- H. Goldstein, C. P. Poole, and J. L. Safko, *Classical Mechanics* (Addison-Wesley, 2002), for the Hamilton–Jacobi equation as a constrained problem and the characteristic flow.
- J. L. Anderson and P. G. Bergmann, "Constraints in covariant field theories," *Physical Review* **83** (1951) 1018–1025, for the constraint analysis of a degenerate field Lagrangian.
