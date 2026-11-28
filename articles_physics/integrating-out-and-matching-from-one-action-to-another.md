# __Integrating Out and Matching: From One Action to Another__

## Introduction

**The claim.** A member of the family of [the parameterised action](the-parameterised-action-an-ordered-family-of-theories.html) can be *derived* from another member, rather than postulated beside it, by two operations performed in a fixed order. First the field whose scale lies outside the regime of interest is integrated out. Then the coefficients of what remains are fixed by requiring that it reproduce the parent's observables to the required order. The first operation alone gives a density with undetermined coefficients; the second alone gives coefficients with no origin; together they define what it means for one rung to stand on another.

**Why this is the section's load-bearing article.** Without it, every rung of the corpus is an independent postulate that happens to agree with its neighbours, and the agreement is a coincidence. With it, the rungs are a chain, and the chain is checkable: the derived coefficients are computed from the parent and compared with the measured ones, and the comparison is the falsifiable content of the reduction. [Matching at $M_C$](matching-at-m-c.html) is the corpus doing exactly this at its own threshold, and the count of conditions it performs is the craft this article states in general.

**The strongest objection.** *If the reduced density is derived, it says nothing the parent does not.* That is right, and it is the point. A derived rung is not new physics; it is the parent's physics re-expressed in a parameter that is actually small in the regime. What it buys is calculability, not content. Any difference between the two is an error in one of them, and finding that error is the use of the reduction.

**Position.** After [the expansion parameter](the-expansion-parameter-order-counting-and-non-commuting-truncations.html), whose grading it changes, and after [the operation](renormalisation-as-an-operation-the-arbitrary-scale.html), with which it shares its count of conditions. It is the article that pairs with the fourth stage: the stages produce diagrams, this produces the density the diagrams are drawn from.

## Integrating Out

**Split the fields into the ones kept and the ones removed, the removed ones being those whose characteristic scale lies beyond the regime.**

$$
e^{\,iS_{\mathrm{eff}}[\phi]}=\int\mathcal D\chi\;e^{\,iS[\phi,\chi]} .
$$

**Three features of the operation are structural, and each is a statement about the method.**

- **The result is local, to the order at which it is computed.** The integral produces a series of local operators in the kept field, ordered by the removed field's scale. This is the mechanism by which integrating out generates a member of the family instead of a non-local object. A reader who finds a non-local term has computed at too low an order, or has integrated out a field that is not actually heavy in the regime.
- **The result is a series, not a closed form.** Each power of the removed field's coupling produces operators of increasing degree in the kept field, and the series is truncated like every other series in the method.
- **The result is exact only in the limit of infinite separation of scales.** At finite separation, each operator carries a residual dependence on the removed scale, and that dependence is what matching removes. The two operations are therefore not independent: the residue of the first is the input of the second.

**The corpus's own instance is the heavy sector.** [The Heavy Sector Below Its Threshold: Decoupling, Matching, and the One Loop](the-heavy-sector-below-its-threshold-decoupling-matching-and-the-one-loop.html) integrates out the states above the threshold and states the one-loop residue that the integration leaves. The article is the model for this one, and it is cited rather than repeated.

## Matching

**The coefficients produced by the integration are not yet the coefficients of the reduced density. Matching fixes them by equality of observables.**

$$
\Gamma_{\mathrm{parent}}^{(n)}\Big|_{\text{to order }k}
=
\Gamma_{\mathrm{reduced}}^{(n)}\Big|_{\text{to order }k}
\qquad\text{for a sufficient set of } n .
$$

**"A sufficient set" is the crux, and it is a counting problem.** Matching must be done on enough quantities to fix every coefficient of the reduced density, and no more. Counting the coefficients and counting the conditions is the whole craft; a mismatch means the reduced density is either underdetermined — a coefficient survives free — or overconstrained — the reduction is inconsistent and one of the two densities is wrong.

**Three points of method, each of which is a common source of a finite error.**

- **On-shell and off-shell matching are equivalent when done consistently.** Off-shell matching is usually simpler; on-shell matching needs fewer conditions but must be aligned with the kinematics order by order. Mixing the two in one calculation is a standard error.
- **Matching is order by order, and the orders must be aligned.** A coefficient matched at one order in the parent must be matched at the corresponding order in the reduced density. Misaligning the orders produces an answer that is wrong by a finite amount and looks entirely reasonable.
- **Matching is done at a label, and the label must be the same on both sides.** The coefficient fixed here is the coefficient at this label; using it at another label requires [the running](renormalisation-as-an-operation-the-arbitrary-scale.html).

**The count in the corpus is four.** [Matching at $M_C$](matching-at-m-c.html) fixes four quantities at the threshold and reads every mass from the vacuum that made it. The number four is the "from above" side of the squeeze in [the parameterised action](the-parameterised-action-an-ordered-family-of-theories.html): it is as many conditions as the application can supply at that label.

## Running Is a Third Operation and Not Part of These Two

**The reduced density's coefficients depend on the label at which the truncation was defined, and their dependence is fixed by the requirement that observables be independent of it.**

$$
\Lambda\frac{\mathrm d}{\mathrm d\Lambda}\,\Gamma^{(n)}=0
\quad\Longrightarrow\quad
\Lambda\frac{\mathrm d g_i}{\mathrm d\Lambda}=\beta_i(g) .
$$

**The three operations answer three different questions, and the difference is worth a table.**

| operation | the question it answers |
|---|---|
| integrating out | which operators appear |
| matching | what their coefficients are at one label |
| running | how those coefficients change with the label |

**The three must be consistent.** Matching at one label followed by running to another must agree with matching directly at the second. That consistency is a nontrivial check on the whole reduction, and it is [the operation](renormalisation-as-an-operation-the-arbitrary-scale.html) in its general form applied to the reduced side.

## What the Reduction Buys

**Three things, and no fourth.**

1. **Fewer fields.** The removed field no longer appears, and every diagram containing it disappears with it.
2. **A different grading.** The reduced density is naturally graded by a parameter appropriate to the low regime, so the truncation can be taken in a parameter that is small there. This is the point of the reduction, and it is why the reduced rung can be *more* accurate than the parent at low energy even though it contains fewer terms.
3. **A finite coefficient count at each order, each of which is either measured or computed.** The two must agree, and the agreement on a quantity not used in matching is the falsifiable content of the whole construction.

**What it does not buy is new physics.** The reduction makes no statement the parent does not make; it re-expresses those statements where they are calculable.

## The Invariant

**Observable equality, to the matched order.** For the set of quantities used in matching — and, as the real test, for at least one quantity *not* used — the two densities must give the same result to the claimed order.

**The second half of the sentence is the test that matters.** Matching guarantees agreement on the quantities used; agreement on an unused quantity is evidence that the reduction is correct and not merely fitted. A reduction that has never been tested on an unused observable has not been validated, and the corpus's matching articles state their unused checks where they have them.

## What the Algebra Supplies Here

**The algebra supplies the operators that survive the integration, and it does not supply the count.** The monomials built from the corpus's carriers are what the integration produces; which of them appears at which degree is read from the algebra. The number of conditions that must be matched is a property of the reduced density's coefficient count, and that is a statement about the list, not about $\mathbb B$.

## Summary

**A rung is derived from its parent by two operations: integrate out the field whose scale lies beyond the regime, then match the coefficients on observables.** The first gives a local series with undetermined coefficients; the second fixes them; running is the third operation and is not part of either.

**The craft is the count.** Enough conditions to fix every coefficient, no more, at one label, with the orders aligned. Underdetermined and overconstrained are both failures, and both are detectable before any diagram is computed.

**The reduction buys calculability, not content.** Its validation is agreement on a quantity that was not used in matching, and that agreement is the falsifiable statement the construction makes.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\phi$ | the field kept in the reduced density |
| $\chi$ | the field integrated out |
| $S_{\mathrm{eff}}[\phi]$ | the density produced by the integration |
| $\Gamma^{(n)}$ | the one-particle-irreducible functional at $n$ legs |
| $\Lambda$ | the truncation label, at which matching is performed |
| $\beta_i$ | the running of the coefficient $g_i$ |

## Further Reading

- [The Parameterised Action: An Ordered Family of Theories](the-parameterised-action-an-ordered-family-of-theories.html), the family between whose members this article moves.
- [Renormalisation as an Operation: The Arbitrary Scale](renormalisation-as-an-operation-the-arbitrary-scale.html), the third operation and the count of conditions it shares with matching.
- [The Heavy Sector Below Its Threshold: Decoupling, Matching, and the One Loop](the-heavy-sector-below-its-threshold-decoupling-matching-and-the-one-loop.html), the corpus's integration worked at its own threshold.
- [Matching at $M_C$: Four Quantities Cross, and Every Mass Comes from the Vacuum That Made It](matching-at-m-c.html), the count of four conditions, worked.
- [The Generating Functional and the Exact Gaussian: The Quadratic Part Inverted into the Propagator](the-generating-functional-and-the-exact-gaussian-the-quadratic-part-inverted-into-the-propagator.html), the Gaussian that the integration of a heavy field reuses.
