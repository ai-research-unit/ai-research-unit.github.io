# __The Expansion Parameter: Order Counting and Non-Commuting Truncations__

## Introduction

**The claim.** The diagram sum is a formal series, and a series is truncated only by a number that orders it. This article states what that number is, what it is not, and the one property of it that the rest of the section relies on: **two truncations in different parameters generally do not commute**, so the order in which they are applied is part of the calculation and must be declared.

**Why the article is not bookkeeping.** Almost every dispute about a perturbative result is a dispute about the order at which it was computed, and almost every such dispute is settled by writing down the grading. A result quoted without its grading cannot be compared with any other result, because the comparison is a comparison of two different truncations that have been given the same name. Stating the grading is what makes two calculations comparable, and the non-commutation is what makes a comparison subtle rather than mechanical.

**The strongest objection.** *The grading is a convention, so it cannot change the physics.* The grading is a convention; the truncation is not. A convention fixes the order in which terms are added; the truncation throws away everything past a point in that order; and the thrown-away part is a physical contribution. Two gradings are two different throwings-away, hence two different approximations, hence two different answers — and the difference between them is a computation of the residue, not a matter of taste. [The limits of the expansion](the-limits-of-the-expansion-gauge-fixing-asymptotic-series-and-strong-coupling.html) is where the residue becomes visible as a boundary.

**Position.** After [the parameterised action](the-parameterised-action-an-ordered-family-of-effective-field-theories.html), whose list it grades, and after [the four stages](the-lagrangian-method-from-a-truncated-effective-lagrangian-to-the-feynman-diagram.html), whose output it orders. It is the article that converts the diagram expansion from a topology into an approximation.

## The Grading

**A grading assigns to each coupling a power of the ordering parameter, and to each diagram the sum of its vertices' powers.**

$$
\text{order of a diagram}=\sum_i \nu_i V_i ,
\qquad \nu_i \text{ the power carried by } g_i .
$$

**Two properties matter, and each is a statement of method.**

- **The grading is homogeneous in each coupling.** The order of a diagram depends only on its vertex content, not on its topology. This is what lets the truncation be decided combinatorially, before any integral is evaluated: a reader can say which diagrams survive a truncation by counting vertices.
- **The grading is a choice.** Nothing forbids assigning the same power to every coupling, and nothing forbids unequal weights. Both are legitimate. Which is *useful* depends on whether the resulting parameter is small in the regime of interest, and that is an empirical question about the application, not a theorem.

**The grading of the list and the grading of the series are distinct, and the distinction is the section's.** [Stage $0$](the-action-as-input-the-quadratic-part-the-interaction-part-and-the-truncation.html) grades the *list* by degree in the field, for the split. This article grades the *series* by power of the coupling, for the truncation. The first decides which diagrams exist; the second decides which are kept. Confusing the two produces the classic error of calling a change of split a change of order.

**The choice of grading is where the corpus's loop expansion and its coupling expansion part company.** The loop number counts internal integrations; the coupling power counts vertices. They are different gradings of the same diagrams, and [the leading order](the-leading-order-tree-diagrams-as-the-stationary-phase-of-the-path-integral.html) states the one case in which they agree.

## The Ratio of Scales Is a Third Grading

**An effective field theory carries a third grading, and the literature's power counting is that one.**

$$
\text{order of }\mathcal O_i=d_i-4,
\qquad
\text{its contribution}\sim\Bigl(\frac{Q}{\Lambda}\Bigr)^{d_i-4},
$$

with $Q$ the scale of the observable and $\Lambda$ the label. It grades the *list* and not the diagrams, and a term is sized by it before any integral is evaluated.

**Three differences separate it from the two gradings above, and each changes how a calculation is written.**

- **It orders the list, not the series.** The coupling grading of this article assigns a power to a vertex and hence to a diagram. The scale grading assigns a power to an operator and hence to a coefficient. The first decides which diagrams are kept; the second decides which terms exist to be drawn.
- **Its small parameter is a regime and not a theory.** $Q/\Lambda$ is small in a regime of a theory. The same density read at another $Q$ has another ordering, and the same diagram has another size. A coupling, by contrast, is small or large independently of the kinematics.
- **The application supplies it.** The powers $\nu_i$ are a choice of bookkeeping, as this article says; $d_i-4$ is fixed by the operator's dimension and by nothing else. The scale ratio is the one grading the algebra fixes the exponents of and the application fixes the value of.

**The two gradings are multiplied and neither replaces the other.** A diagram's size is the product of its vertices' coefficients and of its loop factors, and each coefficient carries the scale ratio of its operator. So the scale grading enters *inside* the coupling grading, through the estimated size of the coefficient, and [term selection](term-selection-in-an-effective-field-theory-accuracy-power-counting-and-the-size-of-what-is-cut.html) is the article where the multiplication is performed.

**A reader who conflates the two calls a term of higher order when it is only of higher dimension.** A dimension-six operator can be first order in its coupling and second order in the scale ratio at once. Which of the two orders is meant must be said, and saying it is the whole of this article's discipline.

## Several Parameters at Once

**In practice the grading is a vector, and the series is a multiple expansion.**

$$
\varepsilon=\{\varepsilon_1,\varepsilon_2,\dots\},\qquad p=\sum_a p_a\,\varepsilon_a .
$$

**Three consequences, each a statement of method.**

1. **A multi-parameter truncation is a region, not a threshold.** "The leading order" is not a number; it is a corner of an order lattice. A reader who says "leading order" without saying which corner has said nothing.
2. **The parameters are independent as bookkeeping but not as physics.** If a coupling is small because a second parameter is small, the two orders are not independent, and the grading must say which dominates. Otherwise a term can be counted twice — once as a coupling order and once as a parameter order.
3. **The error is the first term outside the region.** With one parameter that is a single number. With several it is a boundary, and its size must be estimated *on that boundary*, not at the origin.

**The corpus's own counting is of the second kind.** [Power Counting on a Frame](power-counting-on-a-frame.html) uses a frame in which a parameter multiplies the monomials, so the order of a term is its degree in that parameter; [The Closure of the Term List](the-closure-of-the-term-list-dimension-locality-and-the-count-that-ends-the-search.html) uses the dimension bound. The two gradings coexist, and where they disagree the disagreement is a statement about which parameter is smaller in the regime, not about which counting is right.

## Non-Commuting Truncations

**This is the article's central statement, and it is easy to state and easy to overlook.**

> Truncating in one parameter and then in another generally gives a different result from truncating in the other order.

**Formally, if $T_1$ and $T_2$ are the two truncations,**

$$
T_1^{(n)}\,T_2^{(m)}\neq T_2^{(m)}\,T_1^{(n)} .
$$

**The reason is not exotic.** Each truncation discards terms. A term that lies inside the retained region for one order of operations may lie outside it for the other, and the discarded remainder propagates differently through the subsequent stages. The simplest instance is a residue of order $\varepsilon_1^{\,n+1}\varepsilon_2^{\,0}$ that one ordering retains and the other drops.

**Three consequences follow, and each changes how a calculation is written.**

- **The order of operations is part of the method.** It must be declared, exactly as the grading is declared. An undeclared order of truncations is not a calculation; it is a number whose provenance is unknown.
- **The residue is content, not error.** Where the two orderings differ, the difference is a real contribution that one ordering keeps. That residue is frequently the most interesting object in the calculation, and it is invisible whenever the ordering is left implicit. This is why the section treats the non-commutation as a subject rather than as a nuisance.
- **Commutativity is a special case, and it must be proved.** For a pair of parameters the two orderings may agree to the order of interest. That agreement is a result; it is not a default, and a reader who assumes it has assumed the answer.

**The corpus has one worked instance of the residue, and it is the reason the corpus's reading order is stated.** The action quantum enters once, in the promotion stated in [The Lagrangian and the Second Quantisation](the-lagrangian-and-the-second-quantisation.html), and nowhere earlier. That rule is a statement about the order of two truncations: the truncation that defines the classical bracket must be taken before the truncation that counts loops, and reversing them is not the same calculation. [The Limits of the Expansion](the-limits-of-the-expansion-gauge-fixing-asymptotic-series-and-strong-coupling.html) is where the reversal becomes visible as the asymptotic boundary.

## The Composition Law

**Two truncations composed give a truncation of the composed order, plus a remainder.**

$$
T_1^{(n)}\,T_2^{(m)}=\sum_{p_1\le n,\ p_2\le m}\text{terms}\;+\;\text{remainder},
\qquad
\text{remainder}=O(\varepsilon_1^{n+1})+O(\varepsilon_2^{m+1})+\text{cross terms}.
$$

**Composing three or more multiplies the number of orderings that must be considered, and the number of possible residues.** This is why a systematic study is organised as a lattice of orderings rather than as a list of cases: the cases are the corners, and the corners are fewer than the paths between them. A study that enumerates paths instead of corners will report the same corner many times and call the repetitions independent checks.

**The corpus's structure follows this law.** The sections are ordered so that each truncation is taken once, in one place, and the articles that follow rely on the order rather than re-taking it. That is why the reading order of the constants is stated as a rule and not as a preference.

## What the Algebra Supplies Here

**The algebra supplies no grading.** The powers $\nu_i$ are properties of the density and of the regime, not of the biquaternion structure. What the algebra supplies is the *degrees* that [the parameterised action](the-parameterised-action-an-ordered-family-of-effective-field-theories.html) sorts by, and the pairing that makes the diagrams computable once the order is fixed. A reader who expects the algebra to fix the ordering parameter is asking it to fix a physical regime, which is not a mathematical question.

## Summary

**A series is truncated only by an ordering parameter, and the grading is a choice that must be declared.** The order of a diagram is fixed by its vertex content, which is what makes the truncation combinatorial, and the choice of grading is decided by whether the resulting parameter is small.

**With several parameters the truncation is a region, not a threshold, and the error is estimated on the boundary.** The parameters are independent as bookkeeping and not as physics, and the corpus's two gradings — by frame parameter and by dimension — coexist with a stated relation.

**Truncations in different parameters do not commute, and the residue is content.** The order of operations is part of the method; commutativity is a special case to be proved and not a default; and a study is organised as a lattice of orderings, not as a list of paths.

**The ratio of scales is a third grading, and it is the one an effective field theory is organised by.** It orders the list rather than the diagrams, its small parameter is a regime rather than a theory, and it enters inside the coupling grading through the estimated size of a coefficient. Its exponents are fixed by dimension; its value is supplied by the application.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\varepsilon$ | the ordering parameter, or the vector of them |
| $\nu_i$ | the power of $\varepsilon$ carried by the coupling $g_i$ |
| $V_i$ | the number of vertices of type $i$ |
| $T^{(n)}$ | the truncation operator that keeps orders up to $n$ |
| $p$ | the total order of a diagram, $\sum_i\nu_iV_i$ |
| $Q$, $\Lambda$ | the scale of the observable and the label, whose ratio grades the list |
| $d_i$ | the degree of the operator $\mathcal O_i$, so that $d_i-4$ is its order in the ratio |

## Further Reading

- [The Parameterised Action: An Ordered Family of Effective Field Theories](the-parameterised-action-an-ordered-family-of-effective-field-theories.html), the list that this article grades.
- [Term Selection in an Effective Field Theory: Accuracy, Power Counting and the Size of What Is Cut](term-selection-in-an-effective-field-theory-accuracy-power-counting-and-the-size-of-what-is-cut.html), the multiplication of the scale grading into the coupling grading.
- [The Leading Order: Tree Diagrams as the Stationary Phase of the Path Integral](the-leading-order-tree-diagrams-as-the-stationary-phase-of-the-path-integral.html), the one case in which the loop grading and the coupling grading agree.
- [The Limits of the Expansion: Gauge Fixing, Asymptotic Series and Strong Coupling](the-limits-of-the-expansion-gauge-fixing-asymptotic-series-and-strong-coupling.html), where a chosen grading stops being an approximation.
- [Power Counting on a Frame](power-counting-on-a-frame.html), the corpus's frame-parameter grading.
- [The Closure of the Term List: Dimension, Locality and the Count That Ends the Search](the-closure-of-the-term-list-dimension-locality-and-the-count-that-ends-the-search.html), the corpus's dimension grading.
