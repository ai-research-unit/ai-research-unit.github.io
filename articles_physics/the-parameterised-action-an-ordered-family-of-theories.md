# __The Parameterised Action: An Ordered Family of Theories__

## Introduction

**The claim.** The density that [stage $0$](the-action-as-input-the-quadratic-part-the-interaction-part-and-the-truncation.html) supplies is not one object but a member of a family, labelled by a truncation scale and ordered by the degrees of its operators. Two things follow at once, and the section depends on both. The method's input is always *a family read at a stated member*, never *the* density. And the family has a direction: raising the label restores operators, lowering it discards them, and the discarded part carries an error that must be quoted.

**Why the family is not a pedantry.** A reader who takes the density as a single object will read every later stage as exact, and will have no place to put the error bar that [the limits of the expansion](the-limits-of-the-expansion-gauge-fixing-asymptotic-series-and-strong-coupling.html) insist on. A reader who takes it as a family sees where the error bar comes from: it is the size of the first member not read. The family is what makes a truncated list an *approximation* rather than an arbitrary subset, and the difference is the difference between a calculation and an assertion.

**The strongest objection.** *If the density is a family, the theory is not defined.* The objection mistakes definiteness for completeness. The theory at a stated member is perfectly definite: finitely many operators, finitely many coefficients, finitely many diagrams at each order. What is indefinite is only the claim that this member is the last one — and that claim is not made. The family is how the method says *this is the theory I am using, and here is what I am not using*.

**Position.** The first of the articles that stand outside the four stages. It governs *which* action [stage $0$](the-action-as-input-the-quadratic-part-the-interaction-part-and-the-truncation.html) is handed; [the expansion parameter](the-expansion-parameter-order-counting-and-non-commuting-truncations.html) governs how the list is graded once it is handed over.

## The Family and Its Label

**The density at a label $\Lambda$ is the list of operators whose degree does not exceed the label's bound.**

$$
\mathcal L_\Lambda=\sum_{d_i\le d_{\max}(\Lambda)} g_i(\Lambda)\,\mathcal O_i[\Phi] ,
\qquad d_1\le d_2\le\cdots
$$

**The label is part of the definition, not a cut imposed from outside.** "The density" of an application is always "the family at this label, truncated at this degree". Symmetry and the field content fix which operators *may* appear; they do not fix how many, because the admitted set is infinite once derivatives are allowed. The label is what turns an infinite admissible set into a finite list, and it is the reason the list can be written at all.

**The coefficients depend on the label, and the dependence is not optional.** A coefficient at one label absorbs the effect of the operators dropped at that label; a coefficient at another label absorbs a different set. The two are not the same number, and a coefficient quoted without its label is an incomplete statement. [Renormalisation as an Operation](renormalisation-as-an-operation-the-arbitrary-scale.html) is the article that performs the translation between labels; this one states that the translation is needed.

## What "the Same Theory at the Next Order" Means

**The family is ordered, so the next member can be named, and the naming is by agreement on observables.**

> Two members $\mathcal L_\Lambda$ and $\mathcal L_{\Lambda'}$, with $\Lambda'$ the lower label, agree to order $k$ if every observable computed from either differs by terms of order $k+1$ in the ordering parameter.

**Three consequences, and each is used in a later article.**

- **Agreement is a statement about observables, not about densities.** Two densities that differ by an operator vanishing on the equations of motion agree at every order without being equal. This is why the family is an equivalence class of densities and not a set of them, and it is the content of [the dictionary](the-dictionary-field-redefinition-and-change-of-representation.html).
- **Agreement is order by order.** Advancing a member is not "adding a term"; it is "restoring a term whose effect was previously estimated as small". The estimate and the term are the same information read twice, and a reader who adds terms without updating the estimate has lost the error bar.
- **Agreement is transitive only within the claimed order.** Two members that both agree with a third to order $k$ need not agree with each other to order $k+1$. The relation is an approximation, and approximations do not compose for free.

## The Three Regimes of an Operator

**The degree of an operator, read against the dimension of the base space, sorts the list into three regimes, and the sort is what gives the family its direction.**

| regime | what it does as the label is lowered | can it be cut |
|---|---|---|
| below the marginal degree | grows | no: relevant operators cannot be dropped at any order |
| at the marginal degree | stationary | no: marginal operators are unsuppressed and their coefficients must be measured |
| above the marginal degree | shrinks | yes: irrelevant operators are cut with a controlled error |

**The sort is a sort of the list and not of the physics.** An irrelevant operator is not "unphysical"; it is an operator whose effect at the label in use is smaller than the error being quoted. Raising the label makes it relevant and it must be restored. This is why the family is a family and not a hierarchy of truths.

**The corpus's own truncations sit at the marginal degree, and the reason is stated in [Ostrogradsky](ostrogradsky-or-why-no-rung-goes-past-two-derivatives.html).** A rung stops at two derivatives because the third derivative's operator is irrelevant at the rung's label and would be restored only at a label the corpus does not use. [Power Counting on a Frame](power-counting-on-a-frame.html) states the degrees that make the sort computable.

## Choosing the Label

**Selecting a member is a two-sided decision, and both sides are constraints.**

- **From below.** The label must be high enough that the cut operators are irrelevant *for the observables of interest* — not for all observables, and not in general. An operator cut for being small at one kinematics may be large at another.
- **From above.** The label must be low enough that the retained marginal coefficients are measurable, or at least that their number does not exceed what the application can supply.

**The interval between the two is the domain in which the method is useful.** When the interval is empty — when the label needed for accuracy retains more coefficients than can be measured — the application has no valid member at that location, and the remedy is not a better calculation. It is a different member, or a different grading, or a different method. [The limits of the expansion](the-limits-of-the-expansion-gauge-fixing-asymptotic-series-and-strong-coupling.html) names the third response.

**The corpus states the same squeeze in its own terms at the vacuum restructuring.** [Matching at $M_C$](matching-at-m-c.html) fixes four quantities at one label; the count of conditions there is the "from above" constraint, and the requirement that the matching reproduce the low-energy numbers is the "from below" constraint.

## The Two Traps

**The first trap is a truncation that is not closed under lowering the degree.** If an operator of degree $d$ is retained, every operator of lower degree permitted by the same symmetry must be retained. A list that keeps a high-degree operator and drops a lower-degree one of the same symmetry class is not a member of the family, and its error estimate is meaningless. The check is a sort of the retained list, and it is trivial to perform.

**The second trap is a coefficient attributed to the wrong label.** A number measured at one label, inserted into a density written at another, is wrong by the running — and the error is finite, not small. The count of coefficients and the count of measurements must be made at the *same* label; [the operation](renormalisation-as-an-operation-the-arbitrary-scale.html) is what moves between them.

## What the Algebra Supplies Here

**The algebra supplies the grading of the operators, and it does not supply the label.** The degrees are read from the biquaternion structure: the corpus's carriers have dimensions $1$, $2$ and $3$, so the monomials built from them have degrees the algebra fixes. What the algebra does not supply is where the list stops — that is a choice of the application, made against a measurement, and it is the one thing in this article that no derivation produces.

## Summary

**The density is a family ordered by the degrees of its operators, and the method reads it at a stated member.** The label is part of the definition; the coefficients depend on the label; and "the same theory at the next order" is an agreement on observables, order by order.

**The three regimes of an operator give the family its direction.** Relevant operators cannot be cut, marginal ones must be measured, irrelevant ones are cut with a controlled error. The label is chosen by a two-sided squeeze, and the interval between the two sides is the method's domain of usefulness.

**Two traps: a list not closed under lowering the degree, and a coefficient attributed to the wrong label.** Both are checkable before any integral is evaluated.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Lambda$ | the truncation label: the scale at which the family is read |
| $d_i$ | the degree of the operator $\mathcal O_i$ |
| $d_{\max}(\Lambda)$ | the highest degree retained at the label $\Lambda$ |
| $g_i(\Lambda)$ | the coefficient of $\mathcal O_i$ at the label $\Lambda$ |
| $\mathcal O_i[\Phi]$ | an operator built from the fields and their derivatives |

## Further Reading

- [The Action as Input: The Quadratic Part, the Interaction Part, and the Truncation](the-action-as-input-the-quadratic-part-the-interaction-part-and-the-truncation.html), the stage that consumes this family.
- [The Expansion Parameter: Order Counting and Non-Commuting Truncations](the-expansion-parameter-order-counting-and-non-commuting-truncations.html), the grading of the list once the member is chosen.
- [Renormalisation as an Operation: The Arbitrary Scale](renormalisation-as-an-operation-the-arbitrary-scale.html), the translation of coefficients between labels.
- [Power Counting on a Frame](power-counting-on-a-frame.html), the degrees that make the sort computable.
- [Ostrogradsky, or Why No Rung Goes Past Two Derivatives](ostrogradsky-or-why-no-rung-goes-past-two-derivatives.html), the corpus's rungs as truncations.
- [Matching at $M_C$: Four Quantities Cross, and Every Mass Comes from the Vacuum That Made It](matching-at-m-c.html), the two-sided squeeze worked at the corpus's own threshold.
