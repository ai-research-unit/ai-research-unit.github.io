# __Which Terms Survive: Invariance as a Linear Condition on a Density__

## Introduction

**The claim.** Once a carrier is accepted and a pairing is chosen, the set of candidate terms is fixed by the carrier, and the *subset* that survives is fixed by invariance. **Admissibility is therefore a computation and not a preference**: for each candidate term the group's infinitesimal action is applied to it, and the term is kept exactly when the result vanishes. There is no third step and no judgement call.

**Why the corpus needs this stated once.** The strong sector says of the gluon mass that it is "not admitted, because it is not invariant". The primordial sector says of a quartic that it is "a declared choice of coefficients and not a symmetry the group supplies". **Those two sentences are the same filter, used in opposite directions** — one to exclude a term, one to exclude a claim about a term. Neither sector states the filter; each states its own use of it. This article states it.

**What it inherits.** The pairing and the trace are settled in [the section's hub](the-invariant-density-which-pairing-the-action-can-integrate.html), and the hub's own "why the quadratic and nothing else" is this filter applied to the curvature alone, closing on dimension. **This article generalises the filter to any term and leaves the counting to [the closure article](the-closure-of-the-term-list-dimension-locality-and-the-count-that-ends-the-search.html).** What is here is the condition itself, its three verdicts, and the sentence the corpus has been writing in sector-sized pieces.

## The Candidate Space

**A candidate term is built from the field and its derivatives, contracted with the invariants of the carrier and the pairing.** Three ingredients and no others:

- **the field and its derivatives**, in the carrier's own tensor algebra;
- **the pairing**, which is what turns a product of fields into a number — the trace for a matrix-valued field, the scalar part or the Hermitian form for an element, per the hub;
- **the group's invariants**, which is where the contraction is chosen among the possible ones.

**The group enters twice, and both entries are its own.** **First in the candidate space**: $d_{abc}$ exists for $\mathrm{SU}(3)$ and $\mathrm{SU}(4)$ and vanishes for $\mathrm{SU}(2)$, so $\operatorname{tr}F^3$ is a candidate for one group and not another, with no change to the carrier. **Then in the condition**: the transformation law whose action is tested is the group's, so the verdict is the group's too. **A group therefore decides both which terms are put to the test and which of them pass** — which is the sense in which invariance is the group's filter and not a filter the group merely happens to satisfy.

**The candidates are graded by dimension and by derivative order, and both gradings are finite at each degree.** A term of dimension $d$ with $k$ derivatives and $p$ fields satisfies $d=k+p\,\delta$, where $\delta$ is the field's dimension. **The grading is what makes the candidate set a set and not a stream**: at each dimension there are finitely many ways to contract the available objects, and the list can be written down and closed. The closing is the next article's subject; the existence of a finite list is this one's premise.

**Two terms that differ by a total derivative are one term.** The action of a total divergence is a boundary term and does not vary; the corpus's actions are densities on a domain with the boundary term dropped. **So the candidate space is the space of densities modulo total derivatives**, and a term that is a total derivative is a candidate of dimension $d$ with no content. This is why the $\theta$ term survives as a term and does nothing classically, and it is the same fact that condition 2 of [Helmholtz](the-inverse-problem-of-the-calculus-of-variations-helmholtz-conditions.html) reports from the equation side.

## The Condition

**Let $T$ be a candidate and let $\tilde g(\alpha)$ be a one-parameter family in the group, with generator $\tau_\alpha$.** The infinitesimal action on $T$ is a derivation, and the condition is

$$
\delta_\alpha T=0\quad\text{for every }\alpha .
$$

**Nothing more.** The term is admitted when its variation under every generator vanishes, and rejected when one generator's variation is nonzero. **The test is linear in $T$**, which is why it can be run term by term and why a sum of admitted terms is admitted: the condition is a set of linear equations on the coefficients of the candidate space, and the admitted terms are its kernel.

**Read as a subspace statement.** The variations $\delta_\alpha$ span a subspace $V$ of the space of candidates' images; the admitted terms are those annihilated by all of $V$ — the kernel of the map $T\mapsto(\delta_\alpha T)_\alpha$. **Admissible terms form a linear subspace**, and the practical question *which terms may I write* becomes *what is the kernel of this finite matrix of linear conditions*. The matrix's rank is the obstruction, and it is computable.

**Why invariance is the right condition, in one line.** A local transformation is a redundancy and not a change — the hub's argument — so a density that moved under it would make the action depend on the description, and the stationarity condition would select a representative rather than a field. **The condition on the density is the exact shadow of that requirement.**

## Three Verdicts, and the Corpus's Standard Examples

**Every candidate falls in one of three classes, and the corpus has a canonical example of each.**

**Admitted.** The curvature's square, $-\tfrac12\operatorname{tr}\sum_{\imath\jmath}F_{\imath\jmath}F_{\imath\jmath}$, is invariant because the trace is cyclic — the hub's one-line computation. The Dirac pair, $\bar\Xi(i\gamma^\imath D_\imath-m)\Xi$, is invariant because $\bar\Xi$ carries the conjugate representation and the two factors' transformations cancel. **Both are admitted at unit or at a constant local multiplier**, the distinction being [Helmholtz's](the-inverse-problem-of-the-calculus-of-variations-helmholtz-conditions.html).

**Not admitted.** A mass term for a connection,

$$
m^2\sum_a\sum_\imath A_{a,\imath}A_{a,\imath},
$$

fails: the inhomogeneous part of $A\mapsto\tilde gA\tilde g^{-1}+\tilde g\partial\tilde g^{-1}$ makes the variation nonzero. **The corpus's sentence is exact and its consequence is a measurement**: "the gluon is therefore massless by what the action permits and not because its mass happens to be small." [The next article](one-obstruction-four-groups-the-gauge-mass-that-is-never-admitted.html) shows the argument is one argument and not four.

**Admitted only after a change of the field's status.** The same mass term becomes admissible when the symmetry is broken or when the field is shifted: the Stueckelberg shift $A_\imath\mapsto A_\imath-\tfrac1g\partial_\imath\vartheta$ restores a symmetry that the mass term alone destroys, and the Higgs insertion gives the mass through a scalar's expectation. **The verdict is not reversed; the candidate is changed**, and the change is what the corpus means by *symmetry breaking*.

**And one candidate that is admitted and does nothing.** The $\theta$-term $\theta\sum F\tilde F$ is invariant, since $\tilde F$ transforms as $F$ does and the contraction is a singlet; it is a total derivative, so it is admitted with no classical effect. **Admitted and inert is a fourth class**, and it is the one that makes the distinction between *allowed* and *doing something* necessary.

## What the Filter Does Not Reach

**Four things invariance cannot decide, and each must be handed to another article.**

- **The overall coefficient.** Invariance is linear, so it fixes the *ratio* structure of the admitted space and never the scale: if $T$ is admitted, so is $cT$ for any $c$. The scale is fixed by normalisation — the hub's $\tfrac12$ and $\tfrac14$ — or by a measurement.
- **The sign.** $T$ and $-T$ are both admitted; the sign is fixed by positivity, which is a Euclidean statement and not an invariance statement.
- **The choice among admitted terms of different content.** When several invariants survive at one dimension, invariance admits all of them and selects none. **That is exactly the SU(4) potential**: four quartics written, the fifth set to zero, of which the sector's own article says it is "a declared choice of coefficients and not a symmetry the group supplies". [The declared-coefficient article](what-invariance-cannot-decide-declared-coefficients-signs-and-normalisations.html) is where that is handled.
- **Whether an action exists at all.** The filter runs on candidates that are already densities. Whether the resulting *equation* comes from a density is [Helmholtz's question](two-filters-that-never-meet-invariance-and-helmholtz.html), and it is asked of the equation and not of the term.

**The boundary stated once.** **Invariance is a filter on a space of candidates and not a generator of that space.** It can say no; it cannot say *and there is nothing else*. The space is the carrier's and the pairing's, and the filter is the group's — three different sources for the three different parts of the sentence *this term may appear*.

## Summary

With a carrier accepted and a pairing chosen, the candidate terms are graded finitely by dimension and derivative order, and pairs differing by a total derivative are one term. **A candidate is admitted exactly when its variation under every generator vanishes** — a set of linear conditions, so the admitted terms form a subspace, its rank is the obstruction, and admissibility is a computation.

The corpus's standard examples fill the classes. **Admitted**: the curvature's square, by cyclicity; the Dirac pair, by the conjugate representation. **Not admitted**: a connection's mass term, by the inhomogeneous part of the transformation — which is why the gluon's masslessness is a consequence of the action and not a measurement. **Admitted only after a change of status**: the same mass term under the Stueckelberg shift or the Higgs insertion — the candidate changes and the verdict is not reversed. **Admitted and inert**: $\theta\sum F\tilde F$, invariant and a total derivative.

Invariance fixes the ratio structure of the admitted space and not its scale, not its sign, and not the choice among several surviving invariants. **It is a filter and not a generator**: it can exclude, and it cannot assert that nothing else exists, because the candidate space is the carrier's and the pairing's and not the group's.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T$ | A candidate term in the density |
| $\tilde g(\alpha)$, $\tau_\alpha$ | A one-parameter group element and its generator |
| $\delta_\alpha T$ | The infinitesimal variation of the candidate under $\tau_\alpha$ |
| $d$, $k$, $p$ | Dimension, derivative count and field count of a candidate |
| $\delta$ | The field's dimension |
| $V$ | The span of the variations; the admitted terms are its kernel |
| $\theta\sum F\tilde F$ | The admitted, inert topological term |

## Further Reading

- [The Invariant Density: Which Pairing the Action Can Integrate](the-invariant-density-which-pairing-the-action-can-integrate.html) — the pairing, and this filter applied to the curvature alone.
- [One Obstruction, Four Groups: The Gauge Mass That Is Never Admitted](one-obstruction-four-groups-the-gauge-mass-that-is-never-admitted.html) — the exclusion, stated once for four sectors.
- [The Closure of the Term List: Dimension, Locality and the Count That Ends the Search](the-closure-of-the-term-list-dimension-locality-and-the-count-that-ends-the-search.html) — where the finite candidate list is shown to close.
- [What Invariance Cannot Decide: Declared Coefficients, Signs and Normalisations](what-invariance-cannot-decide-declared-coefficients-signs-and-normalisations.html) — the residue.
- [The Lagrangian and Quantum Chromodynamics: The Triplet, the Octet and the Feynman Rules](the-lagrangian-and-quantum-chromodynamics-the-triplet-the-octet-and-the-feynman-rules.html) — the sector sentence this article generalises.
- [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html) — the declared coefficient that bounds this filter from the other side.
