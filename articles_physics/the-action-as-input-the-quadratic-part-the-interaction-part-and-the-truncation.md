# __The Action as Input: The Quadratic Part, the Interaction Part, and the Truncation__

## Introduction

**The claim.** The first operation of the Lagrangian method is a truncation, not a computation. For the situation at hand — the fields it contains, the group they carry, the derivative order the density may reach — one writes down every term the filters admit up to a stated degree: the kinetic terms, the mass terms, the fixing terms, the ghost terms, every interaction monomial, and the source. The list is finite because the degree bound cuts it, and the cut is the truncation. It is then grouped by degree in the field. What is cut is cut at a stated degree, and its size is stated with it.

**Only the sum is physical.** This is the article's central sentence and the section's. The density $\mathcal L$ is the theory. The split into $\mathcal L_{2}$ and $\mathcal L_{\ge3}$ is the bookkeeping that organises perturbation theory, and the bookkeeping is not unique. It moves under field redefinitions, and it moves under a change of the point about which the field is expanded. Two physicists with the same theory and different expansion points write different $\mathcal L_{2}$'s and compute the same physics. A diagram is a statement about a split; a statement about a split is a statement about the theory only through the sum it came from.

**Why the stage deserves an article.** The stage looks trivial — *write the Lagrangian* — and it is where the method's physics is decided. A term cut from the list is a propagator or a vertex that never appears, and no later stage recovers it; a coefficient misread here is a wrong vertex at every order. The stage has one rule — write every term the filters admit up to the stated degree — and two traps: believing that the grouping is a statement about the theory instead of about the calculation, and forgetting that the cut is an approximation whose error must be quoted.

**The strongest objection.** *If the split is arbitrary, the diagrams are arbitrary.* The answer is the sentence above, read as a theorem of the method: a change of split changes which diagrams one draws and not what their sum is, because the sum is the density's. [The Leading Order](the-leading-order-tree-diagrams-as-the-stationary-phase-of-the-path-integral.html) makes the same point from the other side, where the sum of the tree diagrams is the solution of the equation the unsplit density defines.

**Position.** The first article of the section *The Lagrangian Method*, and stage $0$ of the chain that [the hub](the-lagrangian-method-from-a-truncated-effective-lagrangian-to-the-feynman-diagram.html) states.

## The Input Is a Truncated List, Not an Order

**A situation is specified before anything is computed.** The specification has three parts, and each part narrows the list.

| the part | what it fixes | where the corpus states it |
|---|---|---|
| the field content | which carriers are present, hence which degrees appear | [The Carrier Roster](the-carrier-roster-three-spins-and-no-fourth.html) |
| the group | which representations exist and which terms survive invariance | [What a Group Can Accept](what-a-group-can-accept-a-carrier-must-transform-in-a-representation.html) |
| the derivative order | how many derivatives a term may carry | [The Closure of the Term List](the-closure-of-the-term-list-dimension-locality-and-the-count-that-ends-the-search.html) |

**The list is what the filters leave after the degree bound, and the filters run in one order.** The carrier roster comes first, because a field must exist before a group can act on it. The group comes second, because invariance is a condition on terms built from fields. The derivative and dimension bounds come third, because they need a field content to count. What the three leave is a finite candidate space, and the truncation is a choice inside it: the degree at which the list stops.

**The truncated list is a list of monomials, not a formula.** Every term is a monomial in the fields and their derivatives times a coefficient. That is what makes the next two stages possible: a monomial has one degree, so it goes into one of the two groups, and it has one coefficient, so it becomes one vertex.

## The List Is Constrained, and Then Cut

**The collection is not "anything goes", and the constraints are what make it a scientific step.** Three bounds and one classification do the work.

**The bounds are field content, symmetry and derivative order.** The field content fixes which monomials exist at all. Symmetry is a set of linear conditions on their coefficients, and its kernel is the admitted set. The derivative order and the dimension bound the search, and the bound is what turns an infinite list into a finite one. [The Closure of the Term List](the-closure-of-the-term-list-dimension-locality-and-the-count-that-ends-the-search.html) states the three and records what the count does not close: it proves finiteness and not uniqueness.

**The classification is of the coefficients, and it has exactly three sources.** Every coefficient in the list is forced by the basis, required from outside invariance, or declared. The three are not degrees of confidence; they are three different kinds of statement, and conflating them is what makes a theory unfalsifiable in the part where it is physics.

| source | what it means | the corpus's case |
|---|---|---|
| forced by the basis | the normalisation of a square fixes it | the $\tfrac12$ of a kinetic term, the $\tfrac14$ of a curvature square |
| required from outside invariance | a sign, fixed by positivity | the sign that makes the energy bounded below |
| declared | a choice among survivors, labelled as a choice | the quartics of the primordial potential, with the odd-power one set to zero |

**A "collection" that skipped the classification would be a list of numbers with no ledger.** [What Invariance Cannot Decide](what-invariance-cannot-decide-declared-coefficients-signs-and-normalisations.html) is the article that keeps the three apart, and this stage inherits its verdicts rather than re-arguing them.

## The Filter That Is Not Applied

**A reader coming from the older literature expects a fourth filter, and this stage does not apply it.** The filter is renormalisability: keep only the terms whose divergences can be absorbed by the terms already written. It is a theorem about one special list, not a condition a density must meet. Applied as a rule it would delete every operator above the marginal degree, and delete with them the finite corrections those operators carry — the corrections a measurement at a finite accuracy can see.

**What replaces it is the degree bound, and the bound is a statement about accuracy.** Every term the symmetries admit is written down, and the bound says where the writing stops. The bound is set by the size of the first term omitted, as [term selection](term-selection-in-an-effective-field-theory-accuracy-power-counting-and-the-size-of-what-is-cut.html) computes it, and not by any property of the terms themselves.

**A renormalisable theory is then a special case of the family, not a different kind of density.** It is the case in which the coefficients above the marginal degree are zero at the label in use and stay negligible at every scale the application reaches. That is a strong and useful accident, and it is an accident: nothing in the filters produces it. A census that stops at degree four is a choice of label, and a choice that must be declared as one.

**Nothing in the stages changes when the bound is raised.** Stage $2$ inverts a quadratic operator and stage $3$ expands a polynomial; a list carrying operators of degree six is as finite as a list stopping at four, and the four stages treat the two identically. What changes is the counterterms: each order in the expansion brings the operators of that order, the list does not close at any finite degree, and it does not need to. That is the sense in which [the operation](renormalisation-as-an-operation-the-arbitrary-scale.html) runs infinitely many coefficients rather than repairing a breakdown.

## The Grouping into Two Parts

**The grading is by degree in the field, and the two operative groups are degree two and degree three or more.** Written in full, the density grades as

$$
\mathcal L=\mathcal L_{0}+\mathcal L_{1}+\mathcal L_{2}+\mathcal L_{\ge3},
$$

and the four groups have four different jobs.

| group | degree | what it is | where it goes |
|---|---|---|---|
| $\mathcal L_{0}$ | $0$ | a constant, a vacuum energy | a number: the gravity article carries it as an additive $\Lambda$ and calls it "not part of the action problem" |
| $\mathcal L_{1}$ | $1$ | a term linear in the field | the source $J$, and a tadpole that a chosen expansion point removes |
| $\mathcal L_{2}$ | $2$ | kinetic, mass, fixing | the Gaussian, hence the propagator |
| $\mathcal L_{\ge3}$ | $\ge3$ | every interaction monomial | the vertices |

**The two groups that matter are $\mathcal L_{2}$ and $\mathcal L_{\ge3}$, and the other two are bookkeeping.** $\mathcal L_{1}$ is not an interaction: a linear term is a source, and the generating functional carries it in the exponent as the source term $\frac{2\pi}{h}\int J\phi$. $\mathcal L_{0}$ is a number: it shifts the action by a volume and enters neither a propagator nor a vertex, and whether it is carried is the cosmological-constant question and not this section's. The plan's two-way split is therefore the operative one, and the grading above says where the two omitted groups went.

**The grouping is a reorganisation and not a truncation.** Nothing is deleted. $\mathcal L_{2}+\mathcal L_{\ge3}$ is $\mathcal L$ minus a constant and a source, and a constant and a source are not physics at the level of the diagrams. If a term were dropped, a propagator or a vertex would be missing, and the missing object would show up as a wrong answer at the first order that needed it.

**The grouping is not the same as the expansion parameter.** The split is by field degree; the expansion is by coupling. A quartic monomial is of degree four and of order one in its coupling, and the method uses the second number. This is the one place where a reader who thinks of "orders" as field degree goes wrong, and it is stated again in [The Interaction Series and the Vertex](the-interaction-series-and-the-vertex-wick-contraction-from-the-polynomial-part-of-the-action.html).

## Only the Sum Is Physical

**The split is not invariant, and three operations move it.** Each is a real computation, not a pathology.

**A field redefinition moves it.** Redefine $\tilde\Xi\mapsto\tilde\Xi+\alpha\tilde\Xi^{3}$ and a quartic term contributes to the quadratic part. The density is unchanged as a functional of the new field; the grouping is not.

**A change of expansion point moves it.** Expand the quartic about a constant background and a quartic term becomes a mass term. This is the operation the corpus performs whenever it breaks a symmetry, and it is the clearest case: the same density, a different $\mathcal L_{2}$, and a different propagator.

**A change of the vacuum moves it.** A shift of the field by its expectation value is the previous operation with the shift fixed by a condition rather than chosen.

**What the invariance of the sum buys.** Because every one of the three leaves $\mathcal L$ unchanged, the sum of the diagrams is unchanged too. The diagrams themselves are different. A mass insertion in one split is a four-point vertex in another, and the two computations agree order by order in their own couplings because they are the same Feynman–Dyson series of the same integral.

**The statement to keep.** Only the full sum $\mathcal L$ is physical. The split into $\mathcal L_{2}$ and $\mathcal L_{\ge3}$ is the bookkeeping that organises perturbation theory, and it moves under field redefinitions and changes of expansion point. A reader who forgets this will read a diagram as a fact about the theory rather than as a term in a series about a chosen split.

## The Split Moves: The Quartic about a Background

**The worked case is the corpus's own quartic.** [The Lagrangian and the Interacting Scalar Field](the-lagrangian-and-the-interacting-scalar-field.html) writes

$$
\mathcal L_{\mathrm{int}}=-\frac{\varpi_{\mathrm{cpl}}}{4}N^{2},\qquad N=\mathrm{Sc}\bigl(\tilde\Xi^{*}\tilde\Xi\bigr),
$$

and this article asks what the split does when the field is expanded about a constant background. Write the background as $\varrho_{0}e_t$ and the fluctuation as $\xi$, so that $N=\varrho_{0}^{2}+2\varrho_{0}\mathrm{Sc}(\xi)+\mathrm{Sc}(\xi^{*}\xi)$ in the one-component chart. Then

$$
N^{2}=\varrho_{0}^{4}+4\varrho_{0}^{3}\mathrm{Sc}(\xi)+4\varrho_{0}^{2}\bigl(\mathrm{Sc}(\xi)\bigr)^{2}+2\varrho_{0}^{2}\mathrm{Sc}(\xi^{*}\xi)+\cdots
$$

**The quadratic terms were recomputed symbolically, and they split the fluctuation into two masses.** The last two terms are the quadratic ones, and with the background real and the fluctuation written as a radial part $u$ and a transverse part $w$ they combine to give

$$
-\frac{\varpi_{\mathrm{cpl}}}{4}N^{2}\;\supset\;-\frac{3\varpi_{\mathrm{cpl}}}{2}\varrho_{0}^{2}\,u^{2}-\frac{\varpi_{\mathrm{cpl}}}{2}\varrho_{0}^{2}\,w^{2},
$$

so the radial direction acquires three times the mass the transverse directions acquire. The ratio $3$ is exact, and it is the same $3:1$ that the symmetry-breaking articles of the corpus use.

**What this shows about the split.** The quartic monomial sat in $\mathcal L_{\ge3}$ before the expansion and contributes to $\mathcal L_{2}$ after it. Nothing about the theory changed. The propagator changed, because the propagator is the inverse of whatever $\mathcal L_{2}$ the split selected. A reader who believed the split was a fact about the theory would conclude that the background had created a mass; the mass was in the quartic and the split moved it.

**The warrant.** The expansion was recomputed with a symbolic algebra on the one-component chart, and the coefficient ratio came out $3$ exactly. The check is small and it is stated because the claim is the article's central one.

## The Truncation at Three Rungs

**The list is different at every rung, and the difference is the whole of the rung's physics: a rung is a truncation.** Three columns show the shape.

| rung | $\mathcal L_{2}$ | $\mathcal L_{\ge3}$ | vertex types |
|---|---|---|---|
| central scalar, quartic | the free Klein–Gordon density, $-\mathrm{Sc}(\partial\tilde\Xi^{*}\partial\tilde\Xi)-4\pi^{2}\nu_m^{2}\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$ | $-\frac{\varpi_{\mathrm{cpl}}}{4}N^{2}$ | one, the four-point |
| QED | the free Dirac density plus the free Maxwell density; no fixing, no ghost, because the corpus's QED article stops at the classical action | $\frac{2\pi q}{h}\mathrm{Sc}\bigl[\tilde\Xi^{*}\tilde A_{\Phi}\tilde\Xi\bigr]$ | one, the fermion–photon |
| Yang–Mills | the quadratic connection density plus the fixing term plus the ghost term | the three- and four-gluon terms and the ghost–gluon term, all from the commutator in the curvature | four, with the ghost |

**Each row is a truncation and not a derivation.** The scalar's list is [the interacting scalar article's](the-lagrangian-and-the-interacting-scalar-field.html). The QED list is [the QED article's](the-lagrangian-and-quantum-electrodynamics.html), which states in as many words that it has no fixing term, no ghost term and no vertex, and that the vertex is a quantisation's object. The Yang–Mills list is [the Yang–Mills action article's](the-yang-mills-equation-in-biquaternionic-form.html), with the fixing and the ghosts from [The Connection Path Integral](the-connection-path-integral-in-biquaternionic-form.html).

**The QED row is the one that shows why the truncation is a stage.** The classical article collects three terms and stops. The method's stage $0$ must add the fixing term and the ghost term, because without them $\mathcal L_{2}$ is not invertible and stage $2$ has nothing to invert. The fixing and the ghost are not physics added to QED; they are the price of writing its quadratic part as an invertible operator, and [The Limits of the Expansion](the-limits-of-the-expansion-gauge-fixing-asymptotic-series-and-strong-coupling.html) is where that price is named.

## Summary

**Stage $0$ is a truncation.** For the situation's field content, group and derivative order, one writes down every admitted term up to a stated degree — kinetic, mass, fixing, ghost, interaction, source — and groups the list by degree in the field into the quadratic part and the polynomial part. The list is finite because the degree bound cuts it, and its coefficients are forced, required or declared.

**Only the sum is physical.** The split into $\mathcal L_{2}$ and $\mathcal L_{\ge3}$ is bookkeeping, and it moves under field redefinitions and changes of expansion point. Expanding the corpus's quartic about a constant background moves a quartic monomial into the quadratic part and gives the fluctuation two masses, in the ratio $3:1$; the theory did not change and the propagator did.

**The split is by field degree and the expansion is by coupling.** A quartic is one vertex at order $\lambda$. What is cut is cut at a stated degree and carries a stated error, and the two groups that matter are the quadratic part, which becomes the propagator, and the polynomial part, which becomes the vertices.

**No renormalisability filter is applied, and the degree bound is what stands in its place.** The list is every term the symmetries admit; the bound is where the writing stops, and it is set by the size of the first term omitted. A renormalisable theory is the special case in which the coefficients above the marginal degree vanish at the label and stay negligible at every scale the application reaches.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathcal L$ | the full density, the theory |
| $\mathcal L_{0},\mathcal L_{1},\mathcal L_{2},\mathcal L_{\ge3}$ | the grading by field degree |
| $N=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$ | the scalar density of the interacting scalar, real and non-negative |
| $\varpi_{\mathrm{cpl}}$ | the quartic coupling, real |
| $\varrho_{0}$, $\xi$ | a constant background and the fluctuation about it |
| $u$, $w$ | the radial and transverse parts of the fluctuation |
| $\kappa=\frac{2\pi\varkappa}{h}$ | the gauge coupling as the Action block writes it |

## Further Reading

- [The Closure of the Term List: Dimension, Locality and the Count That Ends the Search](the-closure-of-the-term-list-dimension-locality-and-the-count-that-ends-the-search.html), the bound that makes the list finite.
- [What Invariance Cannot Decide: Declared Coefficients, Signs and Normalisations](what-invariance-cannot-decide-declared-coefficients-signs-and-normalisations.html), the three sources of a coefficient.
- [Term Selection in an Effective Field Theory: Accuracy, Power Counting and the Size of What Is Cut](term-selection-in-an-effective-field-theory-accuracy-power-counting-and-the-size-of-what-is-cut.html), the decision that places the degree bound.
- [The Lagrangian and the Interacting Scalar Field](the-lagrangian-and-the-interacting-scalar-field.html), the quartic this article expands, and the reason its coefficient is $\frac{\varpi_{\mathrm{cpl}}}{4}$.
- [The Lagrangian and Quantum Electrodynamics](the-lagrangian-and-quantum-electrodynamics.html), the collection that stops at the classical action and says so.
- [The Generating Functional and the Exact Gaussian: The Quadratic Part Inverted into the Propagator](the-generating-functional-and-the-exact-gaussian-the-quadratic-part-inverted-into-the-propagator.html), the stage that inverts what this one isolated.
- [Five Steps from a Lagrangian to Fluid Equations](five-steps-from-a-lagrangian-to-fluid-equations.html), the classical counterpart's step S1, where the same density is read as a fluid's two terms.
