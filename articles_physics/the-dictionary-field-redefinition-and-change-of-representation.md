# __The Dictionary: Field Redefinition and Change of Representation__

## Introduction

**The claim.** Any application of the method may choose to write the density in a different set of variables, and such a choice is a change of *representation*, not a change of theory. It is legitimate exactly when it commutes with the operations of the method — the four stages, the truncation, and the reduction between rungs — and it is the burden of a representation change to show that it does. Where the commutation holds, the change is a rewriting and the results carry over. Where it fails, one of two things is true, and telling them apart is the scientific content of the change: a *constraint*, in which case the failure is a prediction, or a *mistake*, in which case it is an error.

**Why the article is needed.** The corpus is a transcription of standard field theory into the biquaternion algebra, and every one of its articles is a change of representation. If a change of representation were not governed by a stated condition, the whole corpus would be a pile of rewritings whose equivalence is asserted rather than shown. The condition is what makes a transcription checkable, and the check is what the corpus's "what the algebra supplies" paragraphs perform article by article.

**The strongest objection.** *If two densities are related by a field redefinition, the difference between them is unobservable, so nothing needs to be proved.* The premise is true only for redefinitions of a particular form, and the form is exactly what the condition identifies. A general redefinition changes the measure, and the measure's change is an observable contribution. Asserting invariance without the condition is how an anomaly is missed.

**Position.** After [the parameterised action](the-parameterised-action-an-ordered-family-of-theories.html) and [the expansion parameter](the-expansion-parameter-order-counting-and-non-commuting-truncations.html), because commutation is with those two that is hardest to check. It is the article that licenses every other article's transcription.

## The Invariance of the Integral

**Everything in this article follows from one line: the functional integral is invariant under a change of integration variable, up to its Jacobian.**

$$
\int\mathcal D\Phi\;e^{\,iS[\Phi]}
=
\int\mathcal D\Phi'\;\Bigl|\frac{\mathcal D\Phi}{\mathcal D\Phi'}\Bigr|\,e^{\,iS[\Phi(\Phi')]} .
$$

**Two cases, and the whole article is their separation.**

- **The Jacobian is trivial.** For a linear change, or a change whose Jacobian is field-independent, only the density changes, and the change is a rewriting: $S'[\Phi']=S[\Phi(\Phi')]$. The diagram series computed from $S'$ in the primed variables is the same series, and the change is *innocent*.
- **The Jacobian is not trivial.** The change contributes a term to the density, and that term must be kept. Omitting it is the standard source of an anomaly, and the corpus states its anomalies in exactly this way: as a term the transformation produces and the naive transcription drops.

**The measure is therefore not a technicality.** A representation change that preserves the action but alters the measure is not a rewriting, and the alteration is physics. The corpus's own convention that the algebra supplies "the central scalar that makes the cutoff sector-blind" is a statement about the measure, and it is the reason the corpus can compare rungs at all.

## Redefinitions That Vanish on the Equations of Motion

**The most important class is the shift by the equation of motion.**

$$
\Phi\;\to\;\Phi+\delta\Phi,\qquad \delta\Phi\propto\frac{\delta S}{\delta\Phi} .
$$

**Three consequences, and the third is the one usually forgotten.**

- **The shift changes the density**, by terms of higher degree. So two densities related by such a shift are not equal.
- **The shift does not change observables, to the order considered**, because the change in the action is the equation of motion integrated against itself.
- **The invariance is order by order and not exact.** At the next order the shift contributes, and the contribution must be tracked if the order is being advanced. A reader who treats the equivalence as exact will drop a term that the next order needs.

**This is why the corpus's "the density is an equivalence class" claim is safe.** Two representatives of the class give the same observables to the stated order, and the class is the object the method actually uses. [What Invariance Cannot Decide](what-invariance-cannot-decide-declared-coefficients-signs-and-normalisations.html) states the part of the density that no redefinition can remove: the declared coefficients are declared precisely because they sit in the class's invariant part.

## The Commutation Condition

**This is the article's central statement.**

> A change of representation is legitimate if and only if it commutes with the operations of the method.

**Concretely, for every operation $O$ of the four stages and of the reduction, and for every truncation $T$,**

$$
D\bigl(O[S]\bigr)=O\bigl(D[S]\bigr),
\qquad
D\bigl(T[S]\bigr)=T\bigl(D[S]\bigr),
$$

**where $D$ is the dictionary.** The first says that computing in the new representation and then translating equals translating and then computing. The second says that truncating before or after the change gives the same result — which is *not* automatic, because the degree of an operator is not generally preserved by a nonlinear redefinition.

**Three tests follow, and a change of representation must pass all three before its results are used.**

| test | the statement | what a failure means |
|---|---|---|
| completeness | the dictionary is invertible on the relevant space | the representation has lost information |
| innocence | the Jacobian is field-independent, or it is included | a term has been dropped from the density |
| commutation with truncation | the degree is preserved, or its shift is computed | results at a given order are not the same order |

**The third test is the one that the corpus's transcriptions must pass repeatedly.** A nonlinear redefinition can turn an operator of one degree into a sum of operators of higher degree, and then a truncation taken before the change is not the same truncation as one taken after it. The residue is the migration of operators across the cut, and it must be computed rather than assumed away.

## What a Failure Means

**A failure of the condition is not automatically an error. It is one of two things, and distinguishing them is the article's scientific content.**

- **A constraint.** The representation may fail to commute because the algebra it uses forbids a configuration the original allowed. Then the non-commutation is a physical statement: the reformulation is not a rewriting, and the difference is a prediction. This is the only route by which a change of representation produces new content.
- **A mistake.** The representation may fail to commute because the dictionary was stated incorrectly — a sign, an ordering, a term omitted, a Jacobian ignored. This is the overwhelmingly more common case, and the burden of proof runs toward it.

**The discipline is therefore: attempt to prove commutation; if it holds, the representation is a legitimate and useful rewriting; if it fails, assume a mistake until the failure has been shown to be a constraint.** A corpus whose transcriptions never test the condition has no way to tell its predictions from its typos.

**The corpus states its own line here, and it is the same line.** The section's articles each carry a paragraph naming what the algebra supplies and what it merely transcribes. Those paragraphs are the commutation test, performed article by article; where an article reports a failure, it reports a constraint and says so.

## The Invariant

**Commutation, verified on a reference quantity.** Choose one observable computable in both representations, compute it both ways, and compare to the claimed order.

**The choice of quantity matters, and the reason is structural.** It must be one on which every stage has a nontrivial action, so that a failure in any one of them shows up. A quantity computed from the propagator alone tests only the Gaussian, and will pass for a dictionary that fails at the vertex or at the symmetry factor. The corpus's habit of checking a reduction on a computed number — a ratio, a residue, a coefficient — is this test, and the numbers are quoted so that a reader can repeat the comparison.

## What the Algebra Supplies Here

**The algebra supplies the dictionary itself and nothing about its innocence.** The map from a biquaternion field to the standard variables is the content of the corpus's every article; whether that map preserves the measure, the degrees and the truncation is not read off the algebra. It is proved, article by article, or it is not proved and the article says so. This is the one place in the method where the algebra's role is entirely on the side of the map and not of the check.

## Summary

**A change of representation is legitimate exactly when it commutes with the operations of the method and with the truncation.** The invariance of the functional integral up to its Jacobian is the whole content: a trivial Jacobian gives a rewriting, a nontrivial one gives an anomaly that must be kept.

**Redefinitions that vanish on the equations of motion leave observables unchanged order by order, and not exactly.** The density is an equivalence class; the declared coefficients are its invariant part.

**Where commutation fails, the failure is a constraint or a mistake.** Assume the mistake until the constraint is shown, and verify each change on a reference quantity that exercises every stage.

## Summary of Notation

| symbol | meaning |
|---|---|
| $D$ | the dictionary, the map between the two representations |
| $O$ | an operation of the method, one of the stages or the reduction |
| $T$ | a truncation |
| $\Phi$, $\Phi'$ | the field in the two representations |
| $\delta\Phi$ | a shift proportional to the equation of motion |

## Further Reading

- [The Action as Input: The Quadratic Part, the Interaction Part, and the Truncation](the-action-as-input-the-quadratic-part-the-interaction-part-and-the-truncation.html), the stage whose split moves under a redefinition.
- [The Parameterised Action: An Ordered Family of Theories](the-parameterised-action-an-ordered-family-of-theories.html), the equivalence class of densities that this article defines.
- [The Expansion Parameter: Order Counting and Non-Commuting Truncations](the-expansion-parameter-order-counting-and-non-commuting-truncations.html), the grading that the third test must preserve.
- [What Invariance Cannot Decide: Declared Coefficients, Signs and Normalisations](what-invariance-cannot-decide-declared-coefficients-signs-and-normalisations.html), the invariant part of the class.
- [The Lagrangian and the Second Quantisation](the-lagrangian-and-the-second-quantisation.html), the corpus's largest single transcription, and its stated gap.
