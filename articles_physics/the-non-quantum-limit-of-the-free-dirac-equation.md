# __The Non-Quantum Limit of the Free Dirac Equation__

## Introduction

**The limit in the first-order family, and what the first order changes.** The Schrödinger and Klein–Gordon families are second order and the limit there is a statement about which of two real lines of an identity survives. The Dirac equation is first order and the phase enters the gradient as a multiplication, so the limit is a statement about a **symbol**: to leading order the gradient acts as multiplication by $i\tilde K_\Psi$, and the eikonal is the condition that this multiplication reproduce the mass.

**What the article establishes, in five sentences.** The pair $\tilde\nabla_\Phi\tilde\Xi_R=k_m\tilde\Xi_L$, $(\tilde\nabla_\Phi)^\natural\tilde\Xi_L=k_m\tilde\Xi_R$ is exact and its second-order consequence is one identity in the amplitude and the phase. The identity separates into a real line and an imaginary line: the real line is the mass shell corrected by the quantum potential, the imaginary line is the continuity equation and is exact. The criterion is unchanged at $\epsilon=1/(k_\Phi L)$, and the mass is **not ordered by it**, which is the family's structural difference: $k_m$ sits at order zero beside the phase's gradient and no power counting in it is available. At order zero the eikonal is $\frac{E^{2}}{c^{2}}-\lvert\vec p\rvert^{2}=m^{2}c^{2}$ read as $\langle\tilde K_\Psi\rangle_\natural=k_m^{2}$, its characters are the straight timelike lines of a dust, and the spin is absent for a structural reason: a norm is central and cannot act on $\xi$. The error of the eikonal is $2\epsilon^{2}$ in relative terms, and the transport equation is not an approximation at all.

**What is not new, and where the mechanics is.** The chiral pair, the covariant derivative, the reading of $\vec v=c^{2}\vec p/E$ and the derivation of the Lorentz force are *Relativistic Mechanics from the Dirac Wave*'s, and the article cites it for the flow and the force. **What is added here is the limit's own account**: the criterion read on a first-order symbol, the ordering table, the exactness of the transport line, the two sheets and the sign of the density, the pair-creation boundary, and the ledger of what the limit does not order.

**Notation, stated once.** The action of the field is $S_{\tilde\Xi}$ and the spinor phase is $\theta_{\mathrm{phs}}=S_{\tilde\Xi}/\hbar$, real because the action is real. The word is $\tilde\Xi=A\,e^{i\theta_{\mathrm{phs}}}\xi$ with $A>0$ real and $\xi$ slowly varying; the two chiral halves carry the same phase. The subscript on $S_{\tilde\Xi}$ is not decoration: the spin $\tilde S_{\Psi,\eta}$ appears below and a bare $S$ would be read for either.

## The Pair and the Exact Identity

**The equations.**

$$
\tilde\nabla_\Phi\tilde\Xi_{R}=k_{m}\tilde\Xi_{L},
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_{L}=k_{m}\tilde\Xi_{R},
\qquad
k_{m}=\frac{m\,c}{\hbar},
$$

with $\Box_\Phi=(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi=\Delta_\Phi-\partial^{2}/\partial {r'_{t}}^{2}$ and $r'_t=c\,t$. Each half obeys $(\Box_\Phi-k_m^{2})\tilde\Xi=0$, and the operator is a central scalar, so **the expansion never has to choose a chiral half**. That is the first thing the first order gives: one scalar identity serves both halves.

**The identity.** Multiply $(\Box_\Phi-k_{m}^{2})\tilde\Xi=0$ by $-\hbar^{2}$ and divide by $\tilde\Xi$:

$$
-\left[\frac{(\partial_{t}S_{\tilde\Xi})^{2}}{c^{2}}-\lvert\nabla S_{\tilde\Xi}\rvert^{2}-m^{2}c^{2}\right]
+\hbar^{2}\left[\frac{1}{c^{2}}\frac{\partial_{t}^{2}A}{A}-\frac{\nabla^{2}A}{A}\right]
+\frac{i\hbar}{A^{2}}\left[\frac{1}{c^{2}}\partial_{t}\!\left(A^{2}\partial_{t}S_{\tilde\Xi}\right)-\nabla\cdot\left(A^{2}\nabla S_{\tilde\Xi}\right)\right]=0 .
$$

**Three lines, one identity, and no order taken.** The first line is a difference of energies of scale $p^{2}$; the second is the quantum potential's; the third is the continuity equation's, and it is imaginary.

| line | scale | order | what it is |
|---|---|---|---|
| first | $p^{2}$ | $1$ | the mass shell, corrected by the second line |
| second | $\hbar^{2}/(L^{2})$ | $\epsilon^{2}$ | the quantum potential $Q$ |
| third | $\hbar\,p/L$ | $\epsilon$ | the continuity equation, **exactly** |

**The third line is not a small term.** Its magnitude is $\epsilon$ against the first, which is *larger* than the second's $\epsilon^{2}$, and that ordering is the family's signature: the transport equation is the leading order of the imaginary part and the quantum potential is the subleading order of the real part. **The two are not in competition, because they are the two parts of one complex identity.**

**Why the third line is exact.** It is the imaginary part, and the only term with an imaginary part is itself. Setting it to zero is not an approximation, it is the identity's imaginary component. **The transport equation of this family is exact, as in the Klein–Gordon family and for the same reason**: the quantum potential is real and cannot reach it.

**What first order changes, in one line.** The gradient acting on $\tilde\Xi$ is, to leading order,

$$
\tilde\nabla_\Phi\tilde\Xi=\frac{1}{\hbar}\Bigl(\frac{\partial_{t}S_{\tilde\Xi}}{c}\,e_{t}+i\nabla S_{\tilde\Xi}\Bigr)\tilde\Xi+\mathcal{O}(\epsilon),
$$

**so the limit is the statement that a differential operator is a multiplication.** For a second-order family the same statement is about a Laplacian; here it is about a Dirac operator, and the object that replaces a Laplacian is an element of the algebra. Its entries are $\frac{1}{\hbar c}\partial_{t}S_{\tilde\Xi}$ in the temporal slot and $\frac{i}{\hbar}\nabla S_{\tilde\Xi}$ in the vector slots, real in the first and imaginary in the second, which is the $\mathbb{B}_{\Psi}$ type.

**The symbol, named.** Write

$$
\tilde K_{\Psi}=\frac{1}{\hbar}\Bigl(\frac{E}{c}\,e_{t}+i\vec p\cdot\vec e\Bigr),
\qquad
E=-\partial_{t}S_{\tilde\Xi},
\qquad
\vec p=\nabla S_{\tilde\Xi}.
$$

**The limit says: the operator is $\tilde K_{\Psi}$ to relative order $\epsilon$, and the equation is the algebraic statement about $\tilde K_{\Psi}$ that the exact equation implies.**

## The Criterion

**Unchanged, and for the same reason as in the other families.**

$$
\epsilon=\frac{1}{k_{\Phi}L}=\frac{\hbar}{\lvert\vec p\rvert L},
$$

with $L$ the length over which $A$ varies. The discarded object is the amplitude's derivative against the phase's, and the phase's derivative is the momentum over $\hbar$ in every family. **The criterion is a property of the word and not of the equation's order.**

**The mass is not ordered by it.** This is the family's structural difference, and it is worth stating precisely, because a reader who has read the second-order articles will expect it. There the mass term competes with $\partial_{t}S_{\tilde\Xi}$ in the eikonal and the ratio $k_mL$ is a second parameter, the one-particle window, nested inside $\epsilon$ by $1/(k_mL)=\epsilon\lvert\vec p\rvert/(mc)$. **Here $k_m$ is not in the phase at all**: it is the constant the gradient's multiplication must reproduce, and the eikonal is the condition that it does. So no power counting in $k_m$ is available and none is needed.

**What $1/(k_mL)$ does mean here.** It is $\hbar/(mcL)$, the Compton length over $L$, and a small value says that the amplitude varies slowly on the scale at which pairs are made. **That is the boundary of the one-particle reading and not a parameter of the expansion**, and in this family it has a sharper meaning than in the others: the negative branch of the eikonal is not a defect to be removed but the antiparticle's branch, and the scale at which the two branches stop being separable is $1/k_m$.

**The table.**

| comparison | ratio | the limit |
|---|---|---|
| amplitude's gradient against the phase's gradient | $\epsilon^{2}=\hbar^{2}/(\lvert\vec p\rvert^{2}L^{2})$ | yes; the limit is $\epsilon\to0$ |
| amplitude's gradient against the mass term | $\hbar^{2}/(m^{2}c^{2}L^{2})=(k_mL)^{-2}$ | no; a boundary of the one-particle reading |
| quantum potential against the eikonal | $\epsilon^{2}$ | no; the error |
| the third line against the eikonal | $\epsilon$ | no; it is an equation |

**Read the last two rows together.** The imaginary line is larger than the real correction and is not an error, and a table that sorted the three lines by size and dropped the large ones would drop the transport equation and keep the quantum potential. **The ordering of a complex identity is by part, not by magnitude**, and that is the trap the first-order family sets.

## Order Zero: the Eikonal as a Norm

**Drop the second line and keep the first; the third is the other part.**

$$
\frac{E^{2}}{c^{2}}-\lvert\vec p\rvert^{2}=m^{2}c^{2},
\qquad\text{that is}\qquad
\langle\tilde K_{\Psi}\rangle_{\natural}=k_{m}^{2},
$$

**with $\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^\natural=\sum_\mu Q_\mu^{2}$ and the $i$ on the vector slots.** The sign is the sector's: in the material sector the $i$ sits on the temporal slot and the norm reads $-k_m^{2}$, as the Klein–Gordon articles have it. **Same object, same convention, opposite sign because the $i$ moved.**

**The characters are dust's.** The eikonal is a first-order partial differential equation, so its characteristics are the rays of $\vec p=\nabla S_{\tilde\Xi}$ and

$$
\vec v=\frac{c^{2}\vec p}{E},
$$

**which is $\vec p=\gamma m\vec v$ read backwards.** The rays are straight in the free case, timelike, and carry the density $A^{2}$ — so the object the limit delivers is a congruence of timelike lines with a density, and not a trajectory. **The limit does not select one line**: it delivers all of them, and a trajectory is a choice of one characteristic.

**What the eikonal is not.** It is not an equation for a ray but for a family, and that is the same in every family: the eikonal is a Hamilton–Jacobi equation, its complete integral is a family, and the limit's classical object is the family. The word "trajectory" in the corpus's summaries always means one member of it.

**The two branches, and this is the family's own statement.** The eikonal is quadratic in $E$ and its two roots are $E=\pm c\sqrt{\lvert\vec p\rvert^{2}+m^{2}c^{2}}$. **The limit keeps both**, and neither is a defect: they are the field's two chiral halves' shared eikonal, and the sign of $\partial_t S_{\tilde\Xi}$ is what distinguishes them.

**The sign of the density, stated carefully, because the two families differ.** The transport current is $j^{\mu}=A^{2}\partial^{\mu}S_{\tilde\Xi}$, whose temporal component is $A^{2}\partial_{t}S_{\tilde\Xi}/c$ and therefore changes sign with the branch. **The Dirac bilinear $\tilde\Xi^{*}\tilde\Xi$ is positive definite and is not this current**: the two differ by the Gordon term, which is a total derivative carrying the spin and is of order $\hbar$. So the limit's current inherits the sign ambiguity, and the positivity of the Dirac density lives in the term the limit drops. *The Gordon Decomposition of the Dirac Current in Biquaternionic Form* is where that split is computed; the limit's business is to record that the split is at order one and is not removable at order zero.

**This is a genuine difference from the Klein–Gordon family.** There the indefinite charge is a property of the pair and the limit keeps it, and the article recorded it as a defect that only second quantisation removes. Here the indefiniteness is in the transport current and the positive object exists at order zero in the algebra; **the limit separates them, and the separation is the spin.**

## Order One: the Transport Equation

**The third line, set to zero.**

$$
\frac{1}{c^{2}}\partial_{t}\!\left(A^{2}\partial_{t}S_{\tilde\Xi}\right)-\nabla\cdot\left(A^{2}\nabla S_{\tilde\Xi}\right)=0,
\qquad\text{that is}\qquad
\partial_{\mu}\bigl(A^{2}\partial^{\mu}S_{\tilde\Xi}\bigr)=0 .
$$

**Exact, and it is the conservation of $j^{\mu}=A^{2}\partial^{\mu}S_{\tilde\Xi}$.** Nothing was discarded to obtain it.

**What it does and does not determine.** It determines $A^{2}$ along the rays once the rays are known, and it determines nothing about the rays. **The pair is triangular in the same order as everywhere else**: the eikonal fixes the rays, the rays fix the drift, the transport fixes the density. What is specific here is that the transport equation is the *imaginary* part of one complex identity and the eikonal is the *real* part, so the two are one equation's components and not two equations.

**A density, not a probability.** $A^{2}$ is the density of the congruence, and the corpus does not read it as a probability at this stage: a probability needs the positive bilinear, which is the Gordon split's other half. **The limit's $A^{2}$ is a number density of dust lines**, and that is the reading the transport equation supports.

**Why the spin cannot be here either.** The transport equation is scalar and the density is a scalar; no spinor index appears in it. **The spin enters only where the two chiral halves stop sharing a phase**, which is order one and is the next section's subject.

## The Spin Is Absent at Order Zero, Structurally

**The argument is one line and it is exact.** The leading multiplier is $\tilde K_{\Psi}$, and the eikonal is its norm, $\langle\tilde K_{\Psi}\rangle_\natural$. **A norm is central**, so it commutes with $\xi$ and cannot act on it. The order-zero equation therefore cannot see the spinor at all, and the reason is algebraic and not an approximation.

**What that rules out.** No spin term can appear in the eikonal, in the flow or in the transport equation, whatever the field. The force computed from the coupled eikonal in the companion carries no spin for that reason, and the result is the Lorentz force and not the Bargmann–Michel–Telegdi equation.

**Where the spin is.** At order one, in the failure of the two orderings of the coupled gradient to commute. The corpus's $g=2$ article identifies the term, whose space–space part is $\sum_\eta\tilde S_{\Psi,\eta}B_\eta$ and whose coefficient is $-\frac{ϙ}{m}$, and this article locates it rather than deriving it. **The statement worth keeping is the ordering**: the spin is not a small correction to a classical particle, it is the first term at which the operator stops being a multiplication, and a limit that dropped it would be a limit of a scalar equation.

**The $\hbar$ is not small.** $\frac{\hbar}{2}$ survives the limit because the limit sends $\epsilon\to0$ and not $\hbar\to0$. **This is the sharpest statement of why the corpus's criterion had to be an inverse length**: a limit that set $\hbar$ to zero would set the spin to zero and would not be a limit of the Dirac family at all.

## Failure Regions

**Three, and they are places.**

*Caustics.* Where the congruence focuses, $A$ diverges and $\epsilon$ grows without bound. The eikonal is still a solution; the expansion is not, because the amplitude's gradient is no longer small. **A caustic is where the limit's own criterion fails, and the failure is measured in $\epsilon$ and not in the distance to the caustic.**

*Where the amplitude varies on the de Broglie scale.* $\epsilon\sim1$ over a region, so the second line of the identity is comparable with the first and the quantum potential is of the same size as the eikonal. This is the region the approximation excludes by construction.

*Where the amplitude varies on the Compton scale.* $(k_mL)\sim1$, so the one-particle reading fails: the two branches of the eikonal stop being separable and the negative branch is no longer interpretable as the antiparticle's partner of a positive-branch state. **The limit has no claim there**, and the region's size is $\hbar/(mc)$, which is the only place in this family where the mass sets a length.

**What is not a failure region.** A turning point in the Schrödinger sense is not one here. The eikonal's characteristics are timelike everywhere and its flow is $\vec v=c^{2}\vec p/E$ with $\lvert\vec v\rvert<c$ for every $\vec p$, so a turning point would need $\vec p=0$ and the flow cannot stop at one. **The classical turning point is a $\beta$ limit's object**, and the audit's remark that the two limits do not commute at the order of the discarded term is the reason a statement carried from one to the other must name its path.

**A plane wave is the case in which nothing is dropped.** For $\tilde\Xi=\xi\,e^{-i\theta_{\mathrm{pwp}}}$ with $\theta_{\mathrm{pwp}}=p\cdot x/\hbar$ the amplitude is constant, both $A$-derivative lines vanish identically, and the eikonal is satisfied exactly. **The limit is empty where it is exact**, and it acts only where the amplitude varies — the same verdict as in the three other families.

## What the Limit Does Not Order

**Four things, and each is a statement about the family.**

*The mass.* $k_m$ is a constant of the eikonal and not a term of an expansion. **No statement of the form "the mass is small" belongs to this limit**, and the nonrelativistic limit is the separate $\beta$ family that subtracts the rest phase.

*The spin.* It sits at order one, in the commutator, and the limit neither removes nor produces it. Its coefficient is fixed by the algebra and its value $g=2$ is the corpus's result and not this article's.

*The charge.* With a connection the eikonal carries it in the mechanical momentum and the criterion must be written on that, as the coupled companion shows. **The limit orders $\epsilon$ and not the coupling**, exactly as in the other families.

*Superposition.* The limit is not linear: the eikonal of a sum is not the sum of the eikonals, and two waves with different phases give no single $\epsilon$. **The limit acts on one phase and one amplitude**, which is what makes it a limit of a family of solutions and not of the equation.

## Summary

The Dirac equation is first order, so its non-quantum limit is the statement that the gradient is, to relative order $\epsilon$, multiplication by $\tilde K_{\Psi}=\frac{1}{\hbar}(\frac{E}{c}e_{t}+i\vec p\cdot\vec e)$. The pair $\tilde\nabla_\Phi\tilde\Xi_R=k_m\tilde\Xi_L$, $(\tilde\nabla_\Phi)^\natural\tilde\Xi_L=k_m\tilde\Xi_R$ gives one exact identity whose real part is the mass shell corrected by the quantum potential and whose imaginary part is the continuity equation. The criterion is unchanged at $\epsilon=1/(k_\Phi L)$; the mass is not ordered by it, because $k_m$ is the constant the eikonal must reproduce rather than a term of the expansion; and $1/(k_mL)$ is the boundary of the one-particle reading and not a parameter.

At order zero the eikonal is $\frac{E^{2}}{c^{2}}-\lvert\vec p\rvert^{2}=m^{2}c^{2}$, read as $\langle\tilde K_\Psi\rangle_\natural=k_m^{2}$, its characters are timelike straight lines with density $A^{2}$, and the flow is $\vec v=c^{2}\vec p/E$. The spin is absent at order zero for an algebraic reason — a norm is central and cannot act on $\xi$ — and it enters at order one in the commutator of the two orderings. The transport equation is exact and its current $A^{2}\partial^{\mu}S_{\tilde\Xi}$ changes sign with the eikonal's branch, while the positive Dirac bilinear differs from it by the Gordon term, so the limit separates the sign ambiguity from the positivity and the separation is the spin. The three failure regions are caustics, the de Broglie scale and the Compton scale, and the last is the only place where the mass sets a length.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\nabla_\Phi\tilde\Xi_R=k_m\tilde\Xi_L$ | The first half of the pair |
| $(\tilde\nabla_\Phi)^\natural\tilde\Xi_L=k_m\tilde\Xi_R$ | The second half |
| $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial{r'_t}^{2}$ | The central scalar the pair squares to; $r'_t=c\,t$ |
| $\tilde\Xi=A\,e^{i\theta_{\mathrm{phs}}}\xi$ | The word; $A>0$ real, $\theta_{\mathrm{phs}}=S_{\tilde\Xi}/\hbar$, $\xi$ slowly varying |
| $\epsilon=1/(k_\Phi L)=\hbar/(\lvert\vec p\rvert L)$ | The parameter of the limit; $L$ the length over which $A$ varies |
| $k_m=mc/\hbar$ | The mass wave number; the Compton length's reciprocal |
| $\tilde K_\Psi=\frac{1}{\hbar}(\frac{E}{c}e_t+i\vec p\cdot\vec e)$ | The symbol; the gradient's leading multiplier |
| $\langle\tilde K_\Psi\rangle_\natural=k_m^{2}$ | The eikonal, as a norm |
| $Q=\frac{\hbar^{2}}{2m}\frac{\Box_\Phi A}{A}$ | The quantum potential; the second line's content |
| $j^{\mu}=A^{2}\partial^{\mu}S_{\tilde\Xi}$ | The transport current; exact; changes sign with the branch |
| $1/(k_mL)$ | The one-particle boundary; not the criterion |

## Further Reading

- Paul A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the equation whose short-wavelength content is at issue.
- Michael V. Berry and K. E. Mount, "Semiclassical approximations in wave mechanics," *Reports on Progress in Physics* **35** (1972) 315–397, for the eikonal method, its transport equation and its failure at caustics.
- Robert G. Littlejohn, "The semiclassical evolution of wave packets," *Physics Reports* **138** (1986) 193–291, for the symbol calculus of a first-order operator and the subleading spin term.
- Michel H. L. Pryce, "The mass-centre in the restricted theory of relativity and its connexion with the quantum theory of elementary particles," *Proceedings of the Royal Society A* **195** (1948) 62–81, for the classical limit of the Dirac equation and the spin supplementary condition.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), chapter 2, for the Gordon decomposition and the positivity of the bilinear density.
