# __Term Selection in an Effective Field Theory: Accuracy, Power Counting and the Size of What Is Cut__

## Introduction

**The claim.** The input of [the Lagrangian method](the-lagrangian-method-from-a-truncated-effective-lagrangian-to-the-feynman-diagram.html) is chosen, not given, and this article states the choice. Once derivatives are allowed, the terms a symmetry admits are infinite. A calculation keeps finitely many. The passage from the infinite list to the finite one is a decision, and the decision is made from the accuracy the answer must reach, the scale at which the observable is measured, and the label at which the family is read. That decision is what makes the calculation an approximation with a stated error rather than a truncated formula with an unstated one.

**Why the decision needs its own article.** [Stage $0$](the-action-as-input-the-quadratic-part-the-interaction-part-and-the-truncation.html) writes the list and [the parameterised action](the-parameterised-action-an-ordered-family-of-effective-field-theories.html) says that the list is a member of a family. Neither says *which* member, for *which* question. The choice is usually left implicit, and an implicit choice is the commonest source of two calculations that cannot be compared: they were made at different accuracies and neither says so.

**The decision is not a fifth stage, and it is not the truncation either.** The four stages are performed in a fixed order and each produces an object the next consumes. The selection produces no object. It fixes what stage $0$ is handed, it uses the observables that stage $4$ defines, and it therefore borrows from both ends of the chain. It is stated in the section's input group because its output is the input, and it is stated once because the rule is one inequality.

**The strongest objection.** *The estimate behind the rule is dimensional analysis, so the selection is guesswork dressed as bookkeeping.* The estimate is dimensional analysis, and it is the reason the method works. The coefficient of an operator, read at the label where that operator is generated, is of order one in the units the label supplies. That single statement turns a degree into a size. Where it fails — a strongly coupled generator, a coefficient small for no visible reason, a scale ratio near one — the selection inherits the failure. This article names those three failures instead of hiding them inside an error bar.

**Position.** Fourth of the articles of *The Input: A Truncated Action*, after [the expansion parameter](the-expansion-parameter-order-counting-and-non-commuting-truncations.html), whose grading it reads as an estimate of size, and before the four stages begin.

## The Rule

**Three numbers enter, and each comes from a different place.**

| symbol | what it is | where it comes from |
|---|---|---|
| $\Lambda$ | the label at which the family is read, the cutoff | a choice, constrained from both sides by [the parameterised action](the-parameterised-action-an-ordered-family-of-effective-field-theories.html) |
| $Q$ | the scale of the observable | the kinematics of the question |
| $\epsilon$ | the accuracy the answer must reach | the question, stated as a number |

**The rule is one inequality.**

$$
\text{keep }\mathcal O_i
\quad\Longleftrightarrow\quad
\bigl\lvert g_i\bigr\rvert\left(\frac{Q}{\Lambda}\right)^{d_i-4}\ \ge\ \epsilon ,
$$

with $g_i$ the coefficient at $\Lambda$ and $d_i$ the degree of the operator. The left side is the estimated contribution of the term to the observable, relative to the leading one, and the rule keeps the term when that contribution is at least as large as the accuracy required.

**The rule reproduces the three regimes as a consequence, and this is the first check on it.** For $d_i<4$ the ratio is raised to a negative power, so the contribution grows as $Q/\Lambda$ falls: the term is kept at every accuracy and cannot be cut. For $d_i=4$ the contribution is $\lvert g_i\rvert$, independent of the ratio: the term is kept or cut according to a coefficient that no power of the cutoff suppresses. For $d_i>4$ the contribution falls: the term is cut once the ratio is small enough. The three regimes of [the parameterised action](the-parameterised-action-an-ordered-family-of-effective-field-theories.html) are the three behaviours of one function, and the article that states them as a table states them here as a limit.

**The rule implies the closure that [the parameterised action](the-parameterised-action-an-ordered-family-of-effective-field-theories.html) demands.** If two operators carry coefficients of one order, the one of lower degree has the larger contribution whenever $Q<\Lambda$, so the rule never retains a term while cutting a lower-degree term of the same class. That is the first trap of the family — a list not closed under lowering the degree — and the inequality closes it without a separate check.

**The rule is a comparison of sizes and not a bound on error.** It says which terms matter. It does not say how much the answer would move if a kept coefficient were wrong, and it does not say what the sum of the cut terms is; that sum is estimated term by term, and the estimate is the article's next subject.

**The constant term is kept by the rule and then divides out.** A degree-zero operator has the largest contribution of all, so no accuracy cuts it. It multiplies $Z[J]$ by a phase, and every correlator normalised by $Z[J]$ is free of it. [Stage $0$](the-action-as-input-the-quadratic-part-the-interaction-part-and-the-truncation.html) says where it goes: into the vacuum energy, not into a diagram.

## The Estimate of a Coefficient

**The estimate is a statement about the label at which the operator is generated, and it has one content: at that label the coefficient is of order one.**

$$
g_i(\Lambda_i)\sim1
\quad\text{in the units }\Lambda_i\text{ supplies},
$$

so a coefficient quoted at a lower label has been reduced by the running and by the loops that generate it. Three corrections are standard, and each multiplies the estimate rather than replacing it.

| correction | the factor | when it applies |
|---|---|---|
| a loop-generated operator | $\frac{1}{16\pi^{2}}\approx6.3\times10^{-3}$ per loop | the operator has no tree-level source in the parent |
| a coupling at each vertex of its generator | one power per vertex | the operator is generated by an interaction of known strength |
| a strongly coupled generator | $4\pi$ per loop instead of $1/16\pi^{2}$ | the sector that generates it is not weakly coupled |

**The estimate fails in three ways, and each is a statement about the application.** When the ratio $Q/\Lambda$ is near one, no power suppresses anything, the rule keeps every term, and the list is not an approximation of anything. When a coefficient is small for no visible reason, the rule cuts a term that a measurement would need; the smallness is then either protected by a symmetry, in which case it is a fact and the rule is right, or it is a fine-tuning, in which case the selection is right and the model is the puzzle. When the generating sector is strongly coupled, the loop factor is $4\pi$ and not $1/16\pi^{2}$, and the two differ by $64\pi^{3}\approx2.0\times10^{3}$: an estimate that used the weak factor is wrong by three orders of magnitude.

**The estimate is the one place in the method where a number is assumed rather than derived.** Every stage of the chain is exact at its order; the estimate is not an order, it is a size. A reader who wants the selection to be a theorem is asking for the coefficients to be computed, and computing them is what [matching](integrating-out-and-matching-from-one-effective-field-theory-to-another.html) does when a parent theory is available. Where no parent is available, the estimate is the only statement that can be made, and it is made explicitly.

## Two Senses of the Word Relevant

**The literature uses one word for two sets, and the two decide different things.**

| sense | what it measures | what it decides |
|---|---|---|
| a relevant operator | whether the term grows as the label is lowered, $d_i\le4$ | whether the term may be cut at all |
| a relevant term | whether the contribution reaches the accuracy, $\lvert g_i\rvert(Q/\Lambda)^{d_i-4}\ge\epsilon$ | whether the term is kept for this observable |

**The first set is a property of the operator; the second is a property of the pair (operator, question).** A relevant operator is retained in every calculation at every accuracy, because its contribution grows as the scale falls. A relevant term need not be a relevant operator, and the gap between the two is where selections go wrong.

**The gap is measurable, and a small case shows its size.** Take $Q/\Lambda=\tfrac12$, one operator of degree four with $\lvert g\rvert=10^{-2}$ and one of degree six with $\lvert g\rvert=10^{-1}$. The degree-four contribution is $10^{-2}$; the degree-six contribution is $10^{-1}\times(\tfrac12)^{2}=2.5\times10^{-2}$. The irrelevant operator contributes more than twice what the marginal one does, so a rule written as *keep the operators of degree four and below* would cut the larger term and keep the smaller. The inequality keeps both, and an accuracy of $5\times10^{-2}$ would cut both.

**The arithmetic is the whole of the argument.** $(\tfrac12)^{2}=\tfrac14$, and $10^{-1}/4=2.5\times10^{-2}$, which exceeds $10^{-2}$.

## The Three Fates of a Term

**Every term of the infinite list ends in one of three states, and a calculation that records only two of them has lost its error bar.**

| fate | the condition | what the calculation carries |
|---|---|---|
| computed | contribution at or above the accuracy | the term, with its coefficient at the label, through all four stages |
| cut and sized | contribution below the accuracy | the estimated size of the largest cut term, quoted as the error |
| neither | contribution below the accuracy by more than the estimate's own error | nothing, and the omission is stated |

**The second row is the one that is usually missing.** The largest cut term is not computed; it is estimated, by the same inequality read with the next degree. Its estimate is the number the answer must be quoted with, and it is quoted in the same units as the answer so that the two can be compared. An accuracy of $1\%$ that is not accompanied by an estimate of the first omitted term is a wish.

**The third row exists because the estimate has its own accuracy.** A term whose estimated contribution is below the accuracy by more than the estimate's own error cannot be sized at all; the honest statement is that the calculation is insensitive to it. This is the weakest of the three and it is stated so that it is not mistaken for the second.

## What the Selection Does Not Do

**It does not fix a value.** A coefficient is measured, or computed from a parent by [matching](integrating-out-and-matching-from-one-effective-field-theory-to-another.html), or declared as a choice in the ledger of [What Invariance Cannot Decide](what-invariance-cannot-decide-declared-coefficients-signs-and-normalisations.html). The selection says which coefficients are needed, never what they are.

**It does not choose the label.** The label is the two-sided squeeze of [the parameterised action](the-parameterised-action-an-ordered-family-of-effective-field-theories.html): high enough that the cut terms are small for the observables of interest, low enough that the retained coefficients can be measured. The selection takes the label and answers a narrower question at it.

**It does not make the series converge.** The selection truncates a series that is asymptotic in general, and it inherits the optimum-order problem of [the limits of the expansion](the-limits-of-the-expansion-gauge-fixing-asymptotic-series-and-strong-coupling.html). Adding terms past the optimal order makes the answer worse while making the list longer, and the rule of this article does not detect that; the detection is the limits article's.

**It does not apply when no ratio is small.** If $Q$ is comparable to every scale in the problem, the inequality keeps everything and the calculation has no expansion. That is not a failure of the rule; it is the regime the rule reports.

## The Check

**Three lines are run before any integral is evaluated, and each is cheap.**

1. The accuracy is a number, and it is the one the answer will be compared with.
2. Every retained operator has an estimated contribution at or above it, with the coefficient estimated at its generation label.
3. The largest cut operator is identified and its contribution estimated, and that estimate is attached to the answer.

**The closure of the retained list is implied by the second line** when the coefficients are of one order, by the argument above, and it is worth checking by sorting the list when they are not. A list that keeps a high-degree operator whose coefficient is large and drops a lower-degree one whose coefficient is small is legitimate; a list that does so without the two coefficients estimated is not.

## What the Algebra Supplies Here

**The algebra supplies the degrees and nothing else.** The degree $d_i$ of an operator is read from the dimensions of the carriers and the derivatives, exactly as [the parameterised action](the-parameterised-action-an-ordered-family-of-effective-field-theories.html) reads it. The accuracy, the scale $Q$ and the estimate of a coefficient are the application's, and the last of the three is the only number in the chain that no derivation produces.

## Summary

**An effective Lagrangian has infinitely many terms and a calculation keeps finitely many, so the choice of which to keep is part of the method.** The rule is one inequality: keep the operator whose estimated contribution $\lvert g_i\rvert(Q/\Lambda)^{d_i-4}$ reaches the required accuracy. It reproduces the three regimes of the family as a consequence and it implies the closure under lowering the degree.

**The estimate of a coefficient is order one at its generation label, corrected by a loop factor, by the couplings of its generator, and by the strong coupling where that applies.** The estimate is the one place in the method where a size is assumed rather than derived, and its three failures are named.

**Two senses of relevant must be kept apart: the operator that grows as the scale falls, and the term that matters for this observable.** A term ends in one of three states — computed, cut and sized, or neither — and only the second of them supplies the error bar the answer is quoted with.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Lambda$ | the label of the family, the cutoff |
| $Q$ | the scale of the observable |
| $\epsilon$ | the accuracy required of the answer |
| $\mathcal O_i$, $d_i$ | an operator and its mass degree |
| $g_i(\Lambda)$ | the coefficient of $\mathcal O_i$ at the label, the Wilson coefficient |
| $\lvert g_i\rvert(Q/\Lambda)^{d_i-4}$ | the estimated relative contribution of $\mathcal O_i$ |
| $\Lambda_i$ | the label at which $\mathcal O_i$ is generated |

## Further Reading

- [The Parameterised Action: An Ordered Family of Effective Field Theories](the-parameterised-action-an-ordered-family-of-effective-field-theories.html), the family whose member the selection reads.
- [The Action as Input: The Quadratic Part, the Interaction Part, and the Truncation](the-action-as-input-the-quadratic-part-the-interaction-part-and-the-truncation.html), the stage that writes the list this article prunes.
- [The Expansion Parameter: Order Counting and Non-Commuting Truncations](the-expansion-parameter-order-counting-and-non-commuting-truncations.html), the grading of the series that the contribution estimate makes quantitative.
- [Integrating Out and Matching: From One Effective Field Theory to Another](integrating-out-and-matching-from-one-effective-field-theory-to-another.html), where a coefficient is computed instead of estimated.
- [Renormalisation as an Operation: The Arbitrary Scale](renormalisation-as-an-operation-the-arbitrary-scale.html), the running that moves a coefficient from its generation label to the label in use.
- [The Limits of the Expansion: Gauge Fixing, Asymptotic Series and Strong Coupling](the-limits-of-the-expansion-gauge-fixing-asymptotic-series-and-strong-coupling.html), the regime in which the ratio is not small.
- [The Observables: Correlation Functions and Their Reduction](the-observables-correlation-functions-and-their-reduction.html), where the scale $Q$ of the question is defined.
