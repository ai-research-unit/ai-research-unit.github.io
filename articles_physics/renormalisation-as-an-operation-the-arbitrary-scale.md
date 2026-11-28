# __Renormalisation as an Operation: The Arbitrary Scale__

## Introduction

**The claim.** Renormalisation is not a repair of a breakdown; it is an operation the method performs whether or not anything diverges. A truncated density carries a scale $\Lambda$ that is a choice, so its coefficients are functions of that scale and not numbers. The operation consists of three steps — define the coefficients at a scale, fix them on a set of conditions, and evolve them — and its content is that the third step has no freedom: the evolution is determined by the requirement that observables not depend on the choice made in the first two.

**Why it is separated from the limits of the expansion.** The method's genuine boundaries are stated [in the next article](the-limits-of-the-expansion-gauge-fixing-asymptotic-series-and-strong-coupling.html): a kernel that cannot be inverted, a series that does not converge, and a coupling that is of order one. Renormalisation is none of these. Every one of the three boundaries is a place where the method stops applying *even when performed perfectly*; the scale is a place where the method applies and must be performed. Filing the two together makes the method look fragile in a way it is not, and it hides the one operation that a reader must be able to carry out before the boundaries can even be stated.

**The strongest objection.** *If the coefficients depend on an arbitrary scale, nothing is predicted.* The objection is the reason the operation exists. The coefficients depend on the scale; the observables do not; and the statement that the observables do not is a differential equation for the coefficients. That equation is what converts a family of arbitrary numbers into a prediction: the value at one scale fixes the value at every other.

**Position.** After [the diagram expansion](the-feynman-rules-and-the-diagram-expansion-propagators-vertices-loops-and-symmetry-factors.html) and before [the limits of the expansion](the-limits-of-the-expansion-gauge-fixing-asymptotic-series-and-strong-coupling.html). It is the operation that the third of those limits presupposes.

## The Scale Enters with the Truncation

**A truncated density is a family, and the label of the family is a scale.** The corpus's density at a truncation is

$$
\mathcal L_\Lambda=\sum_{d_i\le d_{\max}(\Lambda)} g_i(\Lambda)\,\mathcal O_i[\Phi] ,
$$

and the coefficients $g_i(\Lambda)$ are not the coefficients of anything else. Each one absorbs the effect of the operators that were discarded at that truncation, so a coefficient quoted without its scale is an incomplete statement in the same way that a length quoted without units is incomplete.

**This is a consequence of truncating, not of diverging.** Two readers who truncate the same exact density at two different degrees write two different lists of coefficients, both correct, both describing the same physics. Nothing has diverged; the difference is that each has folded a different set of operators into the numbers he keeps. The scale is the price of keeping a finite list, and the price is paid whether or not an integral is infinite.

**The corpus's own truncations are of exactly this kind.** [Ostrogradsky, or Why No Rung Goes Past Two Derivatives](ostrogradsky-or-why-no-rung-goes-past-two-derivatives.html) states that the corpus's rungs stop at two derivatives; that statement is a truncation, and the coefficients of the rung are understood at the rung's scale. [Power Counting on a Frame](power-counting-on-a-frame.html) states the degrees that the truncation orders.

## The Operation, in Three Steps

| step | what is done | what is free | what is not free |
|---|---|---|---|
| **define** | express the density in parameters at a chosen scale | the scale, and the scheme: which conditions are imposed | that a choice must be made |
| **fix** | determine the parameters from chosen conditions | which observables, at which kinematics | that enough conditions are needed to fix every coefficient |
| **evolve** | compute the change of the parameters with the scale | nothing | the evolution, which is determined |

**The freedom in the first two steps is real and it is not a defect.** Two schemes give different intermediate numbers and the same observables. A reader who compares two computations done in different schemes and reports a discrepancy has compared the schemes and not the physics.

**The freedom in the third step is zero, and that is the content of the operation.** Once the density is fixed and the conditions are chosen, the way the coefficients move with the scale is computed, not selected.

**The count of conditions is the craft.** Matching the number of coefficients to the number of conditions is what makes the reduced density either underdetermined or overconstrained; a mismatch is not a small error but a statement that the operation was not defined. This is the same count that [Integrating Out and Matching](integrating-out-and-matching-from-one-effective-field-theory-to-another.html) performs for the reduction between rungs.

## What Must Cancel

**The statement that makes the operation well defined is that no observable depends on the scale.** Since an observable depends on the scale both explicitly and through the coefficients,

$$
\Lambda\frac{\mathrm d}{\mathrm d\Lambda}\,\mathcal O=0
\quad\Longrightarrow\quad
\Lambda\frac{\mathrm d g_i}{\mathrm d\Lambda}=\beta_i(g) .
$$

**The $\beta$ functions are computed, not chosen.** They follow from the cancellation, once the density is fixed and the conditions are chosen. [The Renormalization Group in Biquaternionic Form](the-renormalization-group-in-biquaternionic-form.html) states the shell integration that produces them and the fixed points of the resulting flow.

**The cancellation is exact only where the truncation is exact.** In a truncated density the cancellation holds to the truncation's order, and the remainder is of the size of the discarded operators. The running of a truncated density is therefore itself a truncated statement, and it must be reported with the same error as everything else — the size of the first omitted term. A reader who quotes a $\beta$ function to more orders than his truncation supports has quoted an artefact.

**The cancellation is the consistency condition that ties the three operations together.** A family truncated at $\Lambda$, matched at $\Lambda$ and evolved away from it must return the same observables as a family truncated and matched at the new scale. Whether it does is a nontrivial check, and it fails exactly when the truncation is not closed under the evolution.

## Why It Is Not a Failure

**A failure is a place where the method stops applying even when performed perfectly. The scale is not such a place.**

- If the cancellation is implemented correctly, the result is finite and scale-independent and the method proceeds. There is no residual limitation: the operation is complete.
- If it is implemented incorrectly, the result is wrong. That is an arithmetic error, and an arithmetic error is not a boundary of the method.

**The only genuine limitation nearby belongs to the truncation, not to the operation.** The $\beta$ functions of a truncated density are themselves truncated, and that limitation is a property of the finite list. It is stated, with the other three, in [the limits of the expansion](the-limits-of-the-expansion-gauge-fixing-asymptotic-series-and-strong-coupling.html).

**This distinction is worth stating plainly because the opposite reading is common.** Treating the scale as a breakdown leads to the belief that the method is valid only when the answers are finite, which is false: the operation is required precisely because the coefficient is a function of the scale, and it is required in every finite theory as much as in any other.

## The Two Directions

**The operation is used twice, and the two uses are the same operation applied in opposite directions.**

| use | the question | what the coefficients absorb |
|---|---|---|
| raising the scale | what happens as the truncation is lifted | the ignored operators of higher degree, which are restored |
| lowering the scale | what happens as the regime is approached | the operators that become relevant, which are integrated out |

**Both are consistent with the ordering of the truncation.** Raising $\Lambda$ restores operators; lowering it discards the irrelevant ones and shifts the coefficients to compensate. The only difference between the two uses is which end of the family is being described, and confusing them produces the standard error of treating the scale as if it had a single direction.

**The corpus reads the two directions differently in one respect, and the difference is a strength.** The upward direction is where the list grows and the corpus's rungs are compared; the downward direction is where [the reduction](integrating-out-and-matching-from-one-effective-field-theory-to-another.html) is performed and the corpus's thresholds appear. Keeping the directions apart is what lets the same operation serve both.

## The Tower and the Renormalisable Special Case

**A member of the family carries one coefficient per operator, so the general case is an infinite tower, and the operation is what makes the tower usable.** Each degree brings its coefficients and each order in the expansion brings its counterterms. The coefficients at one label fix them at every other, and that is the whole content of the three steps: no coefficient is determined by the method, and each is determined everywhere once it is determined somewhere.

**A renormalisable theory is the member whose label can be sent to infinity.** In a generic member the limit does not exist: removing the cutoff changes the predictions unless infinitely many coefficients are tuned as it is removed. Where the limit does exist at fixed predictions, the finitely many coefficients absorb everything and the tower's contributions vanish with the ratio $Q/\Lambda$. That is the property the older literature read as a selection principle, and it is a property of one member and not of the family.

**Removability is therefore a statement about the list, and the method treats both kinds of member alike.** A member whose label cannot be removed is not a worse member; it is a member whose label is a physical scale, and whose predictions carry the ratio $Q/\Lambda$ as a parameter. [Term Selection](term-selection-in-an-effective-field-theory-accuracy-power-counting-and-the-size-of-what-is-cut.html) is where that ratio is used, and this article is where the coefficients it sizes are moved between labels.

**Nothing in the three steps changes with the kind of member.** Defining, fixing and evolving are performed on a renormalisable theory and on a truncated one in the same way; what changes is the number of coefficients carried and whether the label has a limit. A reader who expects a different operation for the second kind is looking for a difference the method does not make.

## What the Algebra Supplies Here

**The algebra supplies the pairing that makes the cutoff sector-blind.** The corpus's position, stated in [the renormalization group article](the-renormalization-group-in-biquaternionic-form.html) and repeated here, is that the flow, the coefficients and the fixed points are transcribed, and that the algebra supplies the central scalar on which the shell integration is performed. The operation itself is a property of the integral, and no transcription avoids it.

## Summary

**Renormalisation is an operation in three steps — define, fix, evolve — and its content is that the evolution is determined.** The coefficients of a truncated density are functions of the scale because each absorbs the discarded operators; the observables are not; and the requirement that they are not is the differential equation the coefficients obey.

**It is not a failure.** The three genuine boundaries are the singular kernel, the asymptotic series and the strong coupling; the scale is a place where the method applies and must be performed. The one limitation adjacent to it — that the $\beta$ functions of a truncated density are themselves truncated — belongs to the truncation and is stated with the others.

**The two directions of the operation are the two ends of the family.** Raising the scale restores operators; lowering it discards the irrelevant ones and shifts the coefficients. The same operation serves both, and the shift is what keeps the observables fixed.

**The general member carries an infinite tower, and the tower is what the three steps make usable.** A renormalisable theory is the special member whose label can be sent to infinity at fixed predictions, with finitely many coefficients absorbing everything. Removability is a property of that member's list and not of the method, and the three steps are performed identically on both kinds.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Lambda$ | the truncation scale, and in loop integrals a momentum cutoff |
| $g_i(\Lambda)$ | the coefficient of $\mathcal O_i$ at the scale $\Lambda$ |
| $d_i$ | the degree of the operator $\mathcal O_i$ |
| $\beta_i$ | the flow of $g_i$, $\Lambda\,\mathrm d g_i/\mathrm d\Lambda$ |
| $\mathcal O$ | an observable, independent of the scale |

## Further Reading

- [The Limits of the Expansion: Gauge Fixing, Asymptotic Series and Strong Coupling](the-limits-of-the-expansion-gauge-fixing-asymptotic-series-and-strong-coupling.html), the three boundaries that this operation is not.
- [Integrating Out and Matching: From One Effective Field Theory to Another](integrating-out-and-matching-from-one-effective-field-theory-to-another.html), the two operations that pair with this one, and the count of conditions they share.
- [The Renormalization Group in Biquaternionic Form](the-renormalization-group-in-biquaternionic-form.html), the shell integration, the flow and the fixed points.
- [The Heavy Sector Below Its Threshold: Decoupling, Matching, and the One Loop](the-heavy-sector-below-its-threshold-decoupling-matching-and-the-one-loop.html), the downward direction worked at the corpus's own threshold.
- [Power Counting on a Frame](power-counting-on-a-frame.html), the degrees by which the family is ordered.
