# __Two Filters That Never Meet: Invariance and Helmholtz__

## Introduction

**The claim.** The section's fourth filter asks *is this term allowed inside the density*, and the sixth asks *does this equation come from any density at all*. **The two questions are about different objects — a term and an equation — they are decided by different kinds of mathematics, and neither constrains the other.** This article states the non-interference explicitly, because the corpus's most-quoted sentence is the second filter's and its most-used sentence is the first's, and they are routinely read as one.

**Why the confusion is natural and why it must be broken.** Both filters produce the phrase *there is no action for that*. **But one means *the density cannot contain this term* and the other means *the equation cannot be the variation of any density***, and the difference shows in the corpus's own cleanest case: **a viscous fluid has no gauge group at all**, so the phrase as applied to viscosity cannot be the first filter's at any group.

**What the article has to do.** State the two questions side by side and show they are about different objects; show the second to be group-blind; show that a group cannot manufacture a density that Helmholtz forbids; show that passing Helmholtz does not mean an admitted term exists; and then separate the four grades the corpus actually uses, of which two are routinely conflated.

## The Two Questions, Side by Side

| | invariance | Helmholtz |
|---|---|---|
| **about** | a term $T$ in a density | an equation $E$ |
| **asks** | does $\delta_\alpha T=0$ for every generator? | is $DE=(DE)^\dagger$ in the $L^2$ pairing? |
| **mathematics** | linear algebra on the candidate space | differential identities on the linearisation |
| **depends on the group** | **yes**, essentially | **no**, not at all |
| **answer** | admitted, not admitted, admitted after breaking | variational at unit multiplier, at a multiplier, not at all |
| **failure means** | the term is absent | no density produces this equation |

**The rows that matter are the fourth and the last.** The fourth says the second filter has no group in it; the last says the two failures mean different things. **A term's absence and an equation's non-existence are not the same absence**, and the corpus's shorthand uses one phrase for both.

## The Second Filter Is Group-Blind

**The theorem's hypothesis mentions no group.** Helmholtz's test is the self-adjointness of the equation's linearisation with respect to the $L^2$ pairing; the adjoint moves derivatives by integration by parts and flips signs, and **nothing in that operation refers to a symmetry**. The theorem holds for a mechanical equation in one variable and for a field equation in four, as [the Helmholtz article](the-inverse-problem-of-the-calculus-of-variations-helmholtz-conditions.html) states: "a field equation and a mechanical equation are graded by the same list."

**The corpus's proof of blindness is its own quoted failure.** The damped oscillator fails condition 2 for every nonzero damping, and **the viscous fluid is the field version of the same failure** — one line, exact, and with no group anywhere in the neighbourhood. **If a group were what decides existence, a viscous fluid would have to be described by some group's theory and would fail for a group reason. It is not, and it does not.**

**The converse blindness is the sharper one.** The same theorem passes for **every carrier the corpus uses** — spin $0$, $\tfrac12$ and $1$ at unit or at a constant local multiplier — **and it passes regardless of which group, if any, gauges them.** [The Helmholtz article](the-inverse-problem-of-the-calculus-of-variations-helmholtz-conditions.html) records the reason: the Dirac operator is not self-adjoint in the ordinary pairing and becomes so in the one weighted by $\gamma^0$, which is the $\bar\psi$ of the Dirac density. **The $\gamma^0$ is a multiplier, and a multiplier knows nothing about $\mathrm{SU}(3)$.**

**So the second filter's output is one binary answer per equation, and the answer is the same across groups.** That is the sense in which it "does not know about groups" — not that it is ignorant of symmetry, but that a change of group cannot change its verdict.

## A Group Cannot Manufacture a Density

**The direction that does hold, and it is one-way.** Invariance operates on candidates that are already densities. **If no density's variation produces the equation — if the linearisation is not self-adjoint — then no group's invariance requirement can create one**, because invariance is a condition *on* a density and not a construction *of* one.

**Stated as a containment.** Let $\mathcal D$ be the densities and $\mathcal E$ the equations. The variation map $\delta S/\delta$ takes $\mathcal D$ onto the variational equations. **Invariance selects a subspace of $\mathcal D$; Helmholtz characterises the image.** Narrowing the domain cannot enlarge the image, so **the second filter's veto survives every choice of group**: a non-variational equation is non-variational in every sector, and the sectors' groups are irrelevant to it.

**That is the whole of the positive interaction, and it is asymmetric.** Helmholtz bounds what any group can achieve; the group does not bound what Helmholtz can accept.

## Passing Helmholtz Does Not Mean an Admitted Term Exists

**The converse error, and it is the one the corpus is more likely to make.** A carrier can pass the second filter and carry no admitted term. **The cleanest case is a massless abelian vector before gauge fixing**: its quadratic kernel satisfies Helmholtz, and the kernel is not invertible — the gauge orbit is a flat direction. **Non-invertibility is not non-existence of an action**; it is the absence of a propagator, and the two are different diagnoses with different repairs.

**The repairs are different, which is the test of the distinction.**

- **A non-invertible kernel is repaired by a term** — a gauge-fixing term, or ghosts — **added to an action that exists.**
- **A non-variational equation is repaired by nothing** — no term restores self-adjointness, because the obstruction is in the equation's structure. (A multiplier repairs only the case where a local multiplier exists, and the viscous case is where none does.)

**So the grades must be kept apart, and the corpus uses four.**

| grade | statement | example |
|---|---|---|
| **variational at unit multiplier, invertible** | a density exists and propagates | Klein–Gordon, Proca |
| **variational, not invertible** | a density exists and does not propagate without a fixing | Maxwell, Yang–Mills |
| **variational at a constant local multiplier** | a density exists; the pairing is weighted | Dirac, with $\gamma^0$ |
| **not variational at any local multiplier** | no local density at all | the viscous term |

**Only the fourth is Helmholtz's veto.** The second is gauge degeneracy, the third is a change of pairing, and the first is the ordinary case. **Reading the second as the fourth is the error this table exists to prevent**, and it is why gauge fixing must not be described as *repairing a missing action*.

## What Each Filter Decides, in One Line Each

**Invariance decides which terms a density may contain.** Its domain is finite by [the closure count](the-closure-of-the-term-list-dimension-locality-and-the-count-that-ends-the-search.html), its verdict is per term, and its output is a subspace — never a point, which is [the residue](what-invariance-cannot-decide-declared-coefficients-signs-and-normalisations.html).

**Helmholtz decides whether a given equation has a density behind it at all.** Its domain is one equation, its verdict is binary plus a multiplier grade, and its output is a theorem about the equation's structure.

**The composition, in the order the section runs.** The carrier bounds what fields exist; the pairing makes products into numbers; the count bounds the candidate list; invariance selects inside it; the residue is declared; and Helmholtz then asks, of the equation the selected density produces, whether any density could have produced it — **a question that is answered after the fact and independently of every choice above it.**

**Why the order is not arbitrary.** Each filter's domain is supplied by the one before it, and the last one's question is asked of the *output* rather than of the input. **That is why Helmholtz sits at the end of the section and not at its beginning**, even though its subject — existence — sounds like the first question a reader would ask.

## What This Article Does Not Claim

**It does not claim the filters are unrelated in practice.** A term that fails invariance is absent from the density, and the equation that results is the one Helmholtz then grades. **The filters are sequential in the corpus's construction and independent in their verdicts**, and both halves of that sentence are needed.

**It does not claim Helmholtz is always the tighter filter.** In the corpus it vetoes exactly one thing — the viscous term — and passes every carrier the corpus uses. **Invariance excludes far more**: every gauge mass, every non-invariant contraction, every term of the wrong reality type. **A reader who takes this article as saying Helmholtz is the deep filter and invariance the shallow one has the emphasis backwards**; the correct statement is that they answer different questions and the corpus needs both.

**And it does not settle whether the viscous equations might become variational in some enlarged setting.** A nonlocal action, a multiplier that is an operator, an effective description with hidden degrees of freedom — all are outside the corpus's definition of *action* as a local density, and this article's claim is about that definition.

## Summary

Invariance asks whether a term is allowed inside a density; Helmholtz asks whether an equation comes from any density at all. **Different objects, different mathematics, different verdicts, and no constraint of either on the other.**

Helmholtz is **group-blind**: its hypothesis mentions no symmetry, its quoted failure — the damped oscillator and the viscous fluid — has no group in it, and its verdict is the same for every carrier the corpus uses, with the Dirac case passing at a constant local multiplier that is $\gamma^0$. **One interaction exists and is one-way**: invariance selects a subspace of densities, Helmholtz characterises their image, and narrowing the domain cannot enlarge the image — so a non-variational equation is non-variational in every sector.

Passing Helmholtz does not mean an admitted term exists. **A massless abelian vector passes and its kernel is non-invertible**; that is gauge degeneracy, repaired by adding a term, where a non-variational equation is repaired by nothing. **The four grades — unit multiplier invertible, variational-not-invertible, constant multiplier, not variational — must be kept apart**, and only the last is Helmholtz's veto.

**The composition runs: carrier, pairing, count, invariance, residue, Helmholtz.** Each filter's domain is supplied by the one before, and the last asks its question of the output — which is why existence, which sounds like the first question, is asked last.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal D$, $\mathcal E$ | The densities and the equations; $\delta S/\delta$ maps the first onto the variational part of the second |
| $DE=(DE)^\dagger$ | Helmholtz's test: self-adjointness of the linearisation |
| $\gamma^0$ | The Dirac multiplier; $\psi^\dagger\gamma^0=\bar\psi$ |
| $\delta_\alpha T$ | The invariance variation of a candidate term |
| The four grades | unit multiplier invertible; variational not invertible; constant multiplier; not variational |

## Further Reading

- [The Inverse Problem of the Calculus of Variations: Helmholtz's Conditions](the-inverse-problem-of-the-calculus-of-variations-helmholtz-conditions.html) — the theorem, the three conditions, the damped oscillator and the multiplier.
- [Which Terms Survive: Invariance as a Linear Condition on a Density](which-terms-survive-invariance-as-a-linear-condition-on-a-density.html) — the first of the two filters.
- [The Closure of the Term List: Dimension, Locality and the Count That Ends the Search](the-closure-of-the-term-list-dimension-locality-and-the-count-that-ends-the-search.html) — the finite domain invariance runs on.
- [The Dirac–Bergmann Algorithm: First- and Second-Class Constraints](the-dirac-bergmann-algorithm-first-and-second-class-constraints.html) — the singular Hessian: non-invertibility as a constraint and not as a non-existence.
- [The Invariant Density: Which Pairing the Action Can Integrate](the-invariant-density-which-pairing-the-action-can-integrate.html) — the section's hub and the pairing the adjoint is taken in.
- [Viscosity and the Rayleigh Dissipation Function](viscosity-and-the-rayleigh-dissipation-function.html) — the case with no group at all.
