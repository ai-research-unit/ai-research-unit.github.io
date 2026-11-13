# __The Non-Quantum Limit of the Coupled Klein–Gordon Equation using the Variational Principle__

## Introduction

**The same deletion, with a connection in the Lagrangian.** The limit is the removal of the amplitude's gradient group from the polar action. With a connection the action carries three further groups — the linear and quadratic interaction terms and nothing else — and **none of them is touched**. The truncated action is still gauge invariant, the pair it produces is the mechanical pair, and the constraint it creates is the mechanical mass shell.

**The criterion orders one ratio and not the field.** The amplitude's gradient is order $\delta^{2}$ against the rest term, with $\delta=1/(k_mL)$. The field's terms are order $\varkappa\lvert\vec A\rvert/\lvert\vec p\rvert$ and $(\varkappa\lvert\vec A\rvert/mc)^{2}$, which are ratios of the field to the momentum and to the rest momentum. **The limit says nothing about the field's strength**, so a strong field is semiclassical whenever the amplitude is smooth on the Compton scale.

**The variational statement that the substitution route cannot make.** The connection splits the action into a free part and two interaction terms, and the quadratic term is what makes the whole gauge invariant. A truncation that dropped any gauge-dependent piece would break the symmetry; the limit's truncation drops a functional of $r$ alone, which is invariant by inspection. **The limit and gauge invariance commute, and the reason is visible only in the action.**

**What the article establishes, in four sentences.** The truncated action's variations are the mechanical eikonal and the mechanical transport equation, exactly. The constraint structure is the free one: $p_r$ vanishes identically, and the secondary constraint is the mechanical mass shell. The charge current is the exact one, gauge invariant, and its sign remains indefinite. The triangular structure survives with the Lorentz flow in place of the free flow.

**What is not new.** The charged Madelung action is standard and the corpus's polar variational companion derives it. Added here: the ordering of the interaction terms against the two parameters, the gauge-invariance argument for the truncation, the constraint analysis in the coupled case, and the statement that the limit orders the amplitude and not the field.

**Conventions.** Those of the coupled limit companion and of the coupled variational polar companion. The connection is $\tilde A_\Phi=i a'_t e_t+\vec A$ with $\varphi=c\,a'_t$; the coupling is $\varkappa$, minus the electric charge; the mechanical momentum is $\vec\pi=\vec p+\varkappa\vec A$ and the mechanical energy is $\mathcal E=E+\varkappa\varphi$. The word is $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon e_t$ with $\rho_{\mathrm{num}}=r^{2}$ and $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$. The d'Alembertian is $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial {r'_{t}}^{2}$ with $r'_t=c\,t'$, and $k_m=mc/\hbar$.

## The Action and Its Three Groups

**The coupled polar action for the central field.**

$$
S_{\mathrm{central}}=\int\mathrm{d}^{4}x\;\Bigl\{(\partial_{r'_t}r)^{2}-\lvert\nabla r\rvert^{2}
+\frac{\rho_{\mathrm{num}}}{\hbar^{2}}\Bigl[\bigl(\partial_{r'_t}S_{\tilde\Xi}-\varkappa a'_t\bigr)^{2}-\bigl\lvert\nabla S_{\tilde\Xi}+\varkappa\vec A\bigr\rvert^{2}\Bigr]-k_m^{2}\rho_{\mathrm{num}}\Bigr\}.
$$

**Two groups and three terms.** The amplitude's gradient is one group. The second group is the density times a bracket; the bracket is the free bracket with the connection added, and its square produces three terms:

$$
\bigl(\partial S\bigr)^{2}-\lvert\nabla S\rvert^{2}
\ \longrightarrow\
\underbrace{\bigl(\partial S\bigr)^{2}-\lvert\nabla S\rvert^{2}}_{\text{free}}
\;\underbrace{-\,2\varkappa\bigl(a'_t\,\partial_{r'_t}S+\vec A\cdot\nabla S\bigr)}_{\text{linear}}
\;+\;\underbrace{\varkappa^{2}\bigl(a'^{2}_{t}-\lvert\vec A\rvert^{2}\bigr)}_{\text{quadratic}} .
$$

**The linear term is the current times the potential, and the quadratic term is what repairs it.** A presentation that writes minimal coupling as "current times potential" keeps the linear term and omits the quadratic one, and is not gauge invariant. **The action keeps both because they come from one square**, and that is the polar companion's finding read as a statement about terms.

**Gauge invariance, term by term.** Under $\theta_{\mathrm{pha}}\mapsto\theta_{\mathrm{pha}}+\varkappa\Lambda/\hbar$ and $\vec A\mapsto\vec A-\nabla\Lambda$, $a'_t\mapsto a'_t+\partial_{r'_t}\Lambda$, each of the two brackets is invariant on its own, so the second group is invariant, and the first and third groups are invariant because they contain $r$ alone. **Every group of the action is gauge invariant separately.** That fact is what makes the truncation safe, and it is the only place the article needs it.

## The Criterion Orders the Amplitude and Not the Field

**Two parameters, and the limit knows one of them.** The connection contributes two dimensionless ratios:

| ratio | size | ordered by the limit |
|---|---|---|
| amplitude's gradient against the rest term | $\delta^{2}=1/(k_mL)^{2}$ | yes; the limit is $\delta\to0$ |
| linear interaction against the phase's kinetic term | $\varkappa\lvert\tilde A\rvert/\lvert\vec p\rvert$ | **no** |
| quadratic interaction against the rest term | $(\varkappa\lvert\tilde A\rvert/mc)^{2}$ | **no** |

**The second and third rows are ordered by the field.** A vector potential comparable with the momentum puts the linear term at order one, and a potential comparable with the rest momentum puts the quadratic term at order one. Neither is small because the limit is taken, and neither becomes large.

**What follows for the truncation.** The only group that may be dropped is the first. The two interaction groups must be kept at full strength, and the reason is not that they are large but that the limit is not the expansion that would make them small. **A derivation that expanded in the coupling would be a different limit**, and the article does not take it.

**What follows for a claim of approximation.** The error of the limit is $\lvert Q\rvert$ against the rest term, with $Q$ unchanged by the connection; the error of neglecting the field's terms entirely would be a different error, of the size of the field's ratios. The two must not be confused, and only the first is the error of this limit.

## The Truncated Action

**Delete the first group and nothing else.**

$$
S^{\mathrm{trunc}}_{\mathrm{central}}=\int\mathrm{d}^{4}x\;\Bigl\{\frac{\rho_{\mathrm{num}}}{\hbar^{2}}\Bigl[\bigl(\partial_{r'_t}S_{\tilde\Xi}-\varkappa a'_t\bigr)^{2}-\bigl\lvert\nabla S_{\tilde\Xi}+\varkappa\vec A\bigr\rvert^{2}\Bigr]-k_m^{2}\rho_{\mathrm{num}}\Bigr\}.
$$

**The two variations.**

*Varying the phase* gives the covariant transport equation,

$$
\nabla\cdot\Bigl(\rho_{\mathrm{num}}\bigl(\nabla S_{\tilde\Xi}+\varkappa\vec A\bigr)\Bigr)
-\frac{\partial}{\partial r'_t}\Bigl(\rho_{\mathrm{num}}\bigl(\partial_{r'_t}S_{\tilde\Xi}-\varkappa a'_t\bigr)\Bigr)=0 ,
$$

which is the mechanical current's conservation and is exact.

*Varying the amplitude* gives, away from $r=0$,

$$
\bigl(\partial_{r'_t}S_{\tilde\Xi}-\varkappa a'_t\bigr)^{2}-\bigl\lvert\nabla S_{\tilde\Xi}+\varkappa\vec A\bigr\rvert^{2}=m^{2}c^{2},
$$

which is the mechanical mass shell.

**These are the limit's two equations, and they follow exactly.** Not to leading order: $\Box_\Phi r$ can only come from the discarded group, so its absence from the truncated variation is the absence of $Q$ and nothing else.

**The truncated action is gauge invariant.** The discarded group is a functional of $r$ alone; the surviving groups are invariant bracket by bracket; so the truncation preserves the symmetry exactly, term by term. **The limit commutes with the gauge transformation**, in the sense that truncating after a gauge transformation and gauge-transforming after truncating give the same functional.

**Why the quadratic term cannot be dropped.** Suppose a truncation kept the linear interaction and dropped the quadratic one, on the ground that the field is weak. Then the quadratic term's absence would leave the bracket $\partial S-\varkappa a'_t$ with only half of its invariance, and the resulting pair would not be gauge invariant even though the exact pair is. **The limit's own truncation has no such problem because it drops a term that contains neither the phase nor the connection.** That is the argument the substitution route cannot make, and it is the article's clearest contribution.

## The Constraint Structure

**The same degeneracy, and the same constraint.**

$$
p_r=\frac{\partial\mathcal L^{\mathrm{trunc}}}{\partial(\partial_{r'_t}r)}=0 ,
\qquad
\dot p_r=0\ \Longrightarrow\ \bigl(\partial_{r'_t}S-\varkappa a'_t\bigr)^{2}-\bigl\lvert\nabla S+\varkappa\vec A\bigr\rvert^{2}=m^{2}c^{2} .
$$

**The connection does not change the singular character of the limit.** The vanishing of $p_r$ is caused by the absence of $\partial_{r'_t}r$ from the truncated Lagrangian, and the connection adds no derivative of $r$ at all, so the primary constraint is the free one and the secondary constraint is the free one with the mechanical momentum. The corpus records that the exact coupled problem is as regular as the exact free one — the coupling shifts velocities and adds a term with no velocity, so the rank does not change. **The limit then makes both problems degenerate in the same way.**

**One difference, and it is worth naming.** The secondary constraint now contains the potentials, so the constraint surface moves with the field. A constraint that depends on an external field is still a constraint; what changes is that the surface is not fixed once and for all, and a gauge transformation moves the potentials and the phase in a way that leaves the surface where it was. **The constraint is gauge invariant as an equation**, which is the statement that the mechanical mass shell is a physical surface and the canonical one is not.

**The triangular structure survives, with the Lorentz flow.**

1. The mechanical eikonal is a first-order equation for $\theta_{\mathrm{pha}}$ given the potentials.
2. The flow is the mechanical one, $\vec v=(\nabla S+\varkappa\vec A)/m$, and its acceleration is the Lorentz force.
3. The covariant transport is a first-order equation for $\ln r$ along that flow.
4. The density follows by quadrature, and the current's conservation is the phase's own variation.

## The Current and the Charge

**The current is the exact one.**

$$
\vec j_{\mathrm{mech}}=\frac{\rho_{\mathrm{num}}}{m}\bigl(\nabla S_{\tilde\Xi}+\varkappa\vec A\bigr),
\qquad
c\rho_{\mathrm{chg}}=\frac{\rho_{\mathrm{num}}}{m}\bigl(E+\varkappa\varphi\bigr).
$$

**The truncation does not change it**, because the current is built from $r$ and the bracket and the discarded group contains neither in a form that enters the Noether computation.

**Its conservation is the phase's Euler–Lagrange equation**, so the limit cannot spoil it: the transport equation is not a consequence of the dynamics but the variation itself. That is the free article's statement with the mechanical current, and the connection changes neither the logic nor the status.

**The sign is indefinite and the potential moves the boundary.**

$$
\rho_{\mathrm{chg}}=\frac{\rho_{\mathrm{num}}}{mc^{2}}\bigl(E+\varkappa\varphi\bigr) .
$$

The bracket is the mechanical energy; the potential shifts the value at which it changes sign and does not remove the sign change. **The limit preserves the defect exactly**, and the action shows why: the defect is a power of the velocity, the truncation removes a term that is even in it, and an even term cannot repair an odd one.

**The energy stays positive.** In the truncated theory

$$
T^{00}_{\mathrm{trunc}}=\frac{\rho_{\mathrm{num}}}{\hbar^{2}}\Bigl[\bigl(\partial_{r'_t}S-\varkappa a'_t\bigr)^{2}+\bigl\lvert\nabla S+\varkappa\vec A\bigr\rvert^{2}\Bigr]+k_m^{2}\rho_{\mathrm{num}}>0 ,
$$

which is a sum of squares times a positive density. **The truncated energy is dust's energy in a field**, and the discarded terms are the fluid's internal stress. The charge is odd in the mechanical energy and the energy is even in it, in the coupled theory as in the free one.

## What the Variational Route Adds

**Three things, and the first is the reason for the article.**

*The gauge argument for the truncation.* The limit drops a group that is invariant by itself, so the truncated action is invariant and the truncated equations are gauge invariant order by order. A truncation that dropped part of an invariant combination would not be. **Only the action exhibits which piece is safe to drop**, because only the action shows the grouping.

*The interaction's two terms.* The linear and quadratic terms come from one square, so a presentation that keeps one and not the other is not the truncation of a gauge-invariant functional. The variational route separates them, prices them against the two field ratios, and shows that the limit orders neither.

*The constraint's invariance.* The secondary constraint is the mechanical mass shell, and it is gauge invariant as an equation while the canonical mass shell is not. **The limit's own expansion variable is therefore the mechanical momentum**, for the same reason as in the substitution route and with a sharper argument: the constraint that the limit produces must be a statement about a gauge-invariant surface.

**What it does not add.** No new equation, no new solution, no new invariant, and no ordering of the field. The pair is the substitution route's pair, and the two routes are equivalent on the $N$-regular set.

## The Two Limits, and What Each Orders

**The relativistic limit and the semiclassical limit act on different objects.** The nonrelativistic limit divides out the rest phase and drops the kinetic energy's square against the rest energy; the semiclassical limit drops the amplitude's gradient. In the coupled theory the connection enters both, and in both it enters at full strength.

**At leading order the two limits commute**, and the final pair is the coupled Schrödinger limit's pair. At the order of the discarded term they do not: the semiclassical-first path has a Lorentz dust midway, the nonrelativistic-first path has a charged quantum fluid midway, and the two are different objects.

**One inequality, and it is the article's practical statement.** The limit's smallness is $\delta$ and the field's smallness is $\varkappa\lvert\tilde A\rvert/\lvert\vec p\rvert$. They are independent, so a field can be deep in the semiclassical regime and dominated by its connection, which is the ordinary case in a laboratory. **That independence is why the coupled limit is a separate article and not a paragraph of the free one.**

## Summary

The coupled polar action is the free polar action with the bracket replaced by the covariant one, and the replacement produces a linear and a quadratic interaction term from one square. With the rest energy in the phase, the amplitude's gradient is order $\delta^{2}=1/(k_mL)^{2}$ against the rest term, while the interaction terms are ordered by $\varkappa\lvert\tilde A\rvert/\lvert\vec p\rvert$ and $(\varkappa\lvert\tilde A\rvert/mc)^{2}$ — ratios of the field, which the limit does not touch. The limit drops the amplitude's gradient group and nothing else.

The truncated action's variations are the mechanical eikonal and the covariant transport equation, exactly, and the truncated action is gauge invariant because the discarded group is a functional of $r$ alone. The constraint structure is the free one: $p_r$ vanishes identically, and the secondary constraint is the mechanical mass shell, which is gauge invariant as an equation. The current is the exact mechanical one, its conservation is the phase's own variation, its sign is indefinite, and the truncated energy is dust's and positive. The limit orders the amplitude and not the field; it commutes with the gauge transformation; and the term it must not be confused with — the quadratic interaction — is the term that a naive "current times potential" truncation would drop.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S_{\mathrm{central}}$ | The coupled polar action; two groups |
| $(\partial r)^{2}-\lvert\nabla r\rvert^{2}$ | The amplitude's gradient; the only group dropped |
| $\rho_{\mathrm{num}}\bigl[(\partial S-\varkappa a'_t)^{2}-\lvert\nabla S+\varkappa\vec A\rvert^{2}\bigr]/\hbar^{2}$ | The density times the mechanical bracket; kept |
| $-2\varkappa\rho_{\mathrm{num}}(a'_t\partial S+\vec A\cdot\nabla S)/\hbar^{2}$ | The linear interaction; kept |
| $\varkappa^{2}\rho_{\mathrm{num}}(a'^{2}_{t}-\lvert\vec A\rvert^{2})/\hbar^{2}$ | The quadratic interaction; kept, and required by gauge invariance |
| $\delta=1/(k_mL)$ | The parameter of the limit |
| $\varkappa\lvert\tilde A\rvert/\lvert\vec p\rvert$, $(\varkappa\lvert\tilde A\rvert/mc)^{2}$ | The field's ratios; not ordered by the limit |
| $p_r=0$ | The primary constraint; caused by the truncation |
| $\langle\tilde P^{\mathrm{mech}}\rangle_{\natural}=-m^{2}c^{2}$ | The secondary constraint, gauge invariant as an equation |
| $T^{00}_{\mathrm{trunc}}>0$ | The truncated energy; dust's, in a field |

## Further Reading

- T. Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 2–80, for the charged relativistic fluid and its constraints.
- E. Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1927) 322–326, for the hydrodynamic action.
- P. A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for primary and secondary constraints.
- J. L. Anderson and P. G. Bergmann, "Constraints in covariant field theories," *Physical Review* **83** (1951) 1018–1025, for the constraint analysis of a degenerate field Lagrangian.
- C. M. Bender and S. A. Orszag, *Advanced Mathematical Methods for Scientists and Engineers* (Springer, 1999), chapters 9 and 10, for singular perturbation and the loss of a boundary condition.
- L. D. Landau and E. M. Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the four-potential, the Lorentz force and the gauge transformation of a charged scalar.
