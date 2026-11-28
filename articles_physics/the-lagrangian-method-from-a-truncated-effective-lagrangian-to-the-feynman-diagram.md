# __The Lagrangian Method: From a Truncated Effective Lagrangian to the Feynman Diagram__

## Introduction

**The claim.** A situation in this corpus begins with a truncation: the density for the fields it contains, cut at a stated degree. From that truncation one method returns diagrams. The method has one input and four stages, and the stages are not alternatives. Stage $0$ supplies the input by writing the truncated density; stage $1$ defines the integral; stage $2$ solves its quadratic part exactly; stage $3$ expands the rest; stage $4$ contracts the expansion into graphs. This article states the method once and names it, so that the articles of the corpus that carry its stages can be read as one machine. The density is an effective Lagrangian at a stated cutoff, and the method that works with it is an effective field theory; the vocabulary is fixed in its own section below.

**Why it is worth stating once.** The corpus already contains every part. The [functional integral](the-functional-integral-in-biquaternionic-form.html), the [generating functional](the-generating-functional-and-the-effective-action-in-biquaternionic-form.html), the [Wick theorem](the-wick-theorem-in-biquaternionic-form.html), the [$S$-matrix](the-s-matrix-in-biquaternionic-form.html) and the [LSZ reduction](the-lsz-reduction-formula-in-biquaternionic-form.html) each have their own article, their own derivation and their own declared gap, and [The Quantisation Hub](the-quantisation-hub-the-sixteen-articles-that-import-the-promotion.html) lists them in the order in which the operation is performed. The hub is the index of the parts. What no article states is the machine they compose: the split of one density into a quadratic and a polynomial part, the inversion of the first into the propagator, the expansion of the second into vertices, and the contraction of both into diagrams. That chain begins before the hub's list, at the density, and ends after it, at the amputated amplitude. A reader who begins at the $S$-matrix does not know that the vertex was fixed two stages earlier, in the split of the density. A reader who begins at the Gaussian does not know that its inverse is what the diagrams call the propagator.

**The strongest objection, named at the start.** *This is standard field theory, restated, and the algebra adds nothing.* The objection is right about derivation and wrong about content. This section derives nothing. The quantisation is a postulate of Dirac's, stated once in [The Lagrangian and the Second Quantisation](the-lagrangian-and-the-second-quantisation.html) and imported here. What the section adds is three things. It states the order. It states, at every stage, what the algebra fixes and what it merely transcribes. And it states the three places where the route fails, each with the object that repairs it, and the one operation that is not a failure. A method whose limits are located is a different object from a method whose limits are unstated.

**The classical counterpart, and the model for this section.** [Five Steps from a Lagrangian to Fluid Equations](five-steps-from-a-lagrangian-to-fluid-equations.html) states the classical arrow once: five steps, one per slot, with each step's failure named. The five steps were extracted from five derivations written independently, and the extraction is what makes them a skeleton rather than an imposition. This section has the same shape for the quantum arrow: four stages, one per object, with the failures named in the last article. The two sections are the two halves of one sentence — the same density can be read classically or quantumly, and the reading is an order.

**Position.** The last section but one of *Biquaternion Universe Action*. It follows the promotion, because it uses the action quantum, which the reading order forbids earlier, and because it uses the commutator the promotion introduces. It precedes *Other aspects*, which holds apparatus the chain assumes and does not own.

**What it does not do.** It does not re-derive the functional integral, the Wick theorem, the determinant, the $S$-matrix or the LSZ formula. Each has its article, cited at the stage that uses it. It does not claim that the corpus quantises: the import is stated. It adds no field, no coupling and no prediction.

## The Chain in One Display

The input: one density, truncated at a stated degree.

$$
S[\phi]=\int\mathrm{d}^{4}r\;\mathcal L(\phi,\partial\phi),\qquad \mathcal L=\mathcal L_{2}+\mathcal L_{\ge3}.
$$

**The density is cut, and the cut is an input.** No concrete $\mathcal L$ is complete: the filters of [stage $0$](the-action-as-input-the-quadratic-part-the-interaction-part-and-the-truncation.html) bound the list by a derivative and dimension bound, and the bound is a choice. What the method requires is not completeness but a *declared* incompleteness — which terms were cut, how large they are in the expansion parameter, and in which regime the estimate holds. A density supplied without those three statements is not an input; it is an assertion, and no later stage can supply the error bar it lacks.

Stage $1$ defines the object every later stage works on,

$$
Z[J]=\int\mathcal D\phi\;\exp\Bigl(i\theta_{\mathrm{act}}+i\theta_{\mathrm{src}}\Bigr),\qquad
\theta_{\mathrm{act}}=\frac{2\pi}{h}\mathrm{Re}\,S,\qquad
\theta_{\mathrm{src}}=\frac{2\pi}{h}\int J\phi ,
$$

and all physics is a derivative of $Z[J]$ with respect to the source.

Stage $2$ splits and factorises. The quadratic part is integrated exactly, and its inverse is the propagator,

$$
Z[J]=e^{\,iS_{\mathrm{int}}[\delta/i\delta J]}\,Z_{0}[J],\qquad
Z_{0}[J]=\bigl(\det W\bigr)^{-1/2}\exp\Bigl(-\tfrac12\int J\Delta J\Bigr),\qquad
\Delta=iW^{-1},
$$

where $Z_{0}$ and $\Delta$ in the second line are written in the units $\frac{2\pi}{h}=1$ that the rest of the section uses.

Stage $3$ expands the rest. One monomial of $\mathcal L_{\ge3}$ is one vertex, and the functional derivatives bring down fields that Wick's theorem pairs,

$$
e^{\,iS_{\mathrm{int}}[\delta/i\delta J]}=\sum_{n\ge0}\frac{1}{n!}\bigl(iS_{\mathrm{int}}\bigr)^{n},
\qquad
\text{one monomial}\;\longrightarrow\;\text{one vertex at one point.}
$$

Stage $4$ collects. The terms are the diagrams, and the diagrams are read by four rules.

| stage | the job | the object built | the article that derives it |
|---|---|---|---|
| $0$ | state the truncation, group the list | $\mathcal L=\mathcal L_{2}+\mathcal L_{\ge3}$ | [The Action as Input](the-action-as-input-the-quadratic-part-the-interaction-part-and-the-truncation.html) |
| $1$ | define what is computed | $Z[J]$ | [The Generating Functional and the Exact Gaussian](the-generating-functional-and-the-exact-gaussian-the-quadratic-part-inverted-into-the-propagator.html) |
| $2$ | invert the quadratic part | $\Delta$, the propagator | [The Generating Functional and the Exact Gaussian](the-generating-functional-and-the-exact-gaussian-the-quadratic-part-inverted-into-the-propagator.html) |
| $3$ | expand the polynomial part | one vertex per monomial | [The Interaction Series and the Vertex](the-interaction-series-and-the-vertex-wick-contraction-from-the-polynomial-part-of-the-action.html) |
| $4$ | contract and read | diagrams, the $S$-matrix | [The Feynman Rules and the Diagram Expansion](the-feynman-rules-and-the-diagram-expansion-propagators-vertices-loops-and-symmetry-factors.html) |

**The stages form one order and not a preference.** Stage $2$ follows stage $0$, because it inverts the part that stage $0$ isolated. Stage $3$ follows stage $2$, because it expands the exponential whose action on the Gaussian is now known. Stage $4$ follows stage $3$, because a contraction needs a series to contract. Any other order either inverts what is not there or expands what has not been defined.

## What the Process Is Called

**The chain has no single canonical name, and the absence is why it is often mistaken for four techniques.** Each name below denotes one part. The whole is the composite, and the composite is what a physicist means by doing perturbation theory.

| name | what it denotes | the scope it names |
|---|---|---|
| perturbative quantum field theory | expand in a small parameter | the whole enterprise |
| Feynman–Dyson expansion, Dyson series | the expansion of $Z[J]$ or of the $S$-matrix in powers of the coupling | the series |
| path-integral perturbation theory, functional methods | Gaussian integration plus the expansion of $e^{iS_{\mathrm{int}}}$ | the route |
| Feynman diagram expansion | Wick contraction into graphs | the output |
| weak-coupling expansion | the parameter is $g$, $\lambda$ or $y$ | the regime of validity |
| loop expansion | the same diagrams grouped by powers of the action quantum | an equivalent organisation, and not a second expansion |
| deriving the Feynman rules | the step from $\mathcal L$ to propagators and vertices | the practical recipe |

**The closest single label is *perturbative quantum field theory*, and the closest label for the manipulation is *path-integral perturbation theory*.** The output is the *Feynman diagram expansion*. The section uses the first as the name of the method and the third as the name of its result.

**The loop expansion is not a second expansion.** It groups the same diagrams by the number of closed loops instead of by the power of the coupling. The two groupings are different, and truncating at fixed loop order is not the same as truncating at fixed coupling order. [The Leading Order](the-leading-order-tree-diagrams-as-the-stationary-phase-of-the-path-integral.html) states where the equivalence holds and where it stops.

## The Input Is an Effective Lagrangian

**The input has a name in the literature, and the method is the one that goes with it.** A density cut at a stated degree, carrying every term the symmetries admit below that degree, is an *effective Lagrangian*. The method that computes with it is an *effective field theory*. The name is not decoration: it is the reason the cut is legitimate, and it is the reason the coefficients are not predictions.

**Five words change, and nothing else does.**

| the corpus's word | the literature's word | what it denotes |
|---|---|---|
| the density cut at a stated degree | the effective Lagrangian | the input of stage $0$ |
| the label $\Lambda$ | the cutoff | the member of the family that is read |
| $g_i(\Lambda)$ | the Wilson coefficient | a coefficient, a function of the label |
| the degree $d_i$ | the power counting | the exponent that sizes a term |
| the ratio $Q/\Lambda$ | the expansion parameter of the effective theory | the small number the truncation is ordered by |

**The stages are unchanged under the name, and this is the section's point.** Nothing in stages $1$ to $4$ refers to a scale ratio: they invert an operator, expand a polynomial, and contract fields. What the name adds is a statement about the *input* — that it is the most general density consistent with the symmetries, cut where the accuracy requires — and one decision the stages do not contain. That decision is which of the admitted terms to keep for a stated accuracy, and it is [term selection](term-selection-in-an-effective-field-theory-accuracy-power-counting-and-the-size-of-what-is-cut.html).

**Two expansions are at work and they are not the same.** The *series* is the expansion of the exponential in the coupling, and it is what stages $3$ and $4$ truncate. The *family* is the expansion of the density in the ratio of the observable's scale to the cutoff, and it is what stage $0$ truncates. A calculation that declares one and not the other is ordered in one direction only, and [the expansion parameter](the-expansion-parameter-order-counting-and-non-commuting-truncations.html) shows why the two orderings do not commute.

**The applications live outside this section, and the plan says where.** Two categories carry a complete Lagrangian written at a stated label: *Biquaternion Universe Primordial Force Effective Field Theory* (PFEFT) and *Biquaternion Universe Standard Model Effective Field Theory* (SMEFT). They are read after this section, because each is one member of the family of [the parameterised action](the-parameterised-action-an-ordered-family-of-effective-field-theories.html) written out in full. This section states the method those two sections apply, and it takes no example from either.

## Why the Split Is the Right Organisation

Four facts do the work, and each has one consequence.

| fact | consequence |
|---|---|
| $\mathcal L_{2}$ is quadratic in the field | its integral is Gaussian and exact, so the propagator is exact to all orders |
| $\mathcal L_{\ge3}$ is polynomial in the field | its monomials are local, so a vertex sits at one point |
| each factor of $S_{\mathrm{int}}$ costs one power of the coupling | the number of vertices is the order, so the series organises itself |
| the expansion parameter is the coupling, not the field degree | a quartic is one vertex at order $\lambda$, not fourth order |

**The third row is the one usually misstated.** The split is by field degree; that is what makes stage $2$ Gaussian and stage $3$ polynomial. The expansion is by coupling. These are two gradings of one density, and the method works because they need not agree: one quartic monomial, of fourth degree, is one vertex, of first order in its coupling.

**The first row is the one usually overclaimed.** The Gaussian is exact, and exactness here means exact per mode. The operator is inverted exactly. What the infinite product of eigenvalues means is the regularisation's business, and [The Functional Determinant](the-functional-determinant-in-biquaternionic-form.html) says what that business is. Stage $2$ never approximates the quadratic part. That is the whole reason for isolating it.

**The second row is what makes the diagrams drawable.** A non-local interaction — an operator of infinite order, a term with a denominator of derivatives — has no single point at which to put a vertex. The corpus's filters exclude such terms before stage $0$ begins, by the locality bound of [The Closure of the Term List](the-closure-of-the-term-list-dimension-locality-and-the-count-that-ends-the-search.html).

## What the Method Is Not

**It is not a derivation of the quantisation.** The promotion is a postulate. [The Lagrangian and the Second Quantisation](the-lagrangian-and-the-second-quantisation.html) states it and stops; this section begins after it, and no article below re-derives it.

**It is not a derivation of any particular theory.** The algebra's compact part is $\mathrm{U}(2)$ of dimension four with a two-dimensional module, and the strong and electroweak groups sit outside it. The method runs on whatever density stage $0$ collects. When that density is the Standard Model's, the method is the Standard Model's perturbation theory and the corpus is transcribing; [The Quantisation Hub](the-quantisation-hub-the-sixteen-articles-that-import-the-promotion.html) is the ledger of that import.

**It is not exact as a whole.** Stage $2$ is exact and each order is exact; the sum is not. [The Limits of the Expansion](the-limits-of-the-expansion-gauge-fixing-asymptotic-series-and-strong-coupling.html) states this with the three boundaries attached, each with its repair where one exists.

**It is not the only route.** A lattice evaluates the same integral without expanding. The method's claim is not that every question is answered by diagrams; it is that the questions it answers, it answers in one fixed order, with the errors of truncation located.

## Summary

**A situation begins with a truncated action, and from that truncation the method returns diagrams in four stages, with stage $0$ supplying the input.** Stage $0$ writes the density cut at a stated degree and groups it into a quadratic part and a polynomial part; what is cut is cut at that degree and its size is stated with it. Stage $1$ defines the generating functional, from whose derivatives every correlator comes. Stage $2$ inverts the quadratic part exactly, and the inverse is the propagator. Stage $3$ expands the polynomial part in the coupling: one monomial is one vertex, and Wick's theorem pairs the fields. Stage $4$ collects the terms into diagrams, reads them by four rules, and turns a correlator into an $S$-matrix element by amputation and the mass shell.

**The name is composite.** Perturbative quantum field theory is the framework, the Feynman–Dyson series is the series, path-integral perturbation theory is the route, and the Feynman diagram expansion is the output. The loop expansion regroups the same diagrams by the action quantum; it is not a second expansion.

**The input is an effective Lagrangian, and the method is the effective field theory built on it.** The cutoff, the Wilson coefficient, the power counting and the ratio $Q/\Lambda$ rename the label, the coefficient, the degree and the small parameter, and no stage changes under the rename. What the name adds is the decision the stages do not contain: which terms to keep for a stated accuracy, made once at stage $0$ and never revisited.

**The order is the content.** The split is by field degree and the expansion is by coupling, so a quartic is one vertex at order $\lambda$. What is cut is cut at a stated degree and carries a stated error. And the three ways the route fails are named in the section's last article, each with the object that repairs it — together with the one operation, renormalisation, that is not a failure at all.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathcal L$, $S$ | the density and the action, $S=\int\mathrm{d}^{4}r\,\mathcal L$ |
| $\mathcal L_{2}$, $\mathcal L_{\ge3}$ | the quadratic part and the rest; the grouping is exact |
| $Z[J]$ | the generating functional with source $J$ |
| $\theta_{\mathrm{act}}$ | the action angle, $\frac{2\pi}{h}\mathrm{Re}\,S$ |
| $W$, $\Delta=W^{-1}$ | the quadratic operator and its inverse, the propagator |
| $S_{\mathrm{int}}$ | $\int\mathcal L_{\ge3}$, the interaction |
| $\mathcal M(\tilde Q_{\Phi})$ | the mass-shell operator, $N(\tilde Q_{\Phi})+m^{2}c^{2}$ |
| $h$, $\nu_m$ | the action quantum and the mass wave number, $\nu_m=\frac{mc}{h}$ |

## Further Reading

- [The Action as Input: The Quadratic Part, the Interaction Part, and the Truncation](the-action-as-input-the-quadratic-part-the-interaction-part-and-the-truncation.html), stage $0$, and the sense in which only the sum is physical.
- [Term Selection in an Effective Field Theory: Accuracy, Power Counting and the Size of What Is Cut](term-selection-in-an-effective-field-theory-accuracy-power-counting-and-the-size-of-what-is-cut.html), the decision that fixes what stage $0$ is handed.
- [The Generating Functional and the Exact Gaussian: The Quadratic Part Inverted into the Propagator](the-generating-functional-and-the-exact-gaussian-the-quadratic-part-inverted-into-the-propagator.html), stages $1$ and $2$, and the inversion that defines the propagator.
- [The Interaction Series and the Vertex: Wick Contraction from the Polynomial Part of the Action](the-interaction-series-and-the-vertex-wick-contraction-from-the-polynomial-part-of-the-action.html), stage $3$, and the counting that makes one monomial one vertex.
- [The Feynman Rules and the Diagram Expansion: Propagators, Vertices, Loops and Symmetry Factors](the-feynman-rules-and-the-diagram-expansion-propagators-vertices-loops-and-symmetry-factors.html), stage $4$, and the four reading instructions.
- [Three Diagrams of the SU(4) Model: The Kaon, the Proton Chain and a Gluon Exchange](three-diagrams-of-the-su4-model-the-kaon-the-proton-chain-and-a-gluon-exchange.html), the method's diagrams drawn in the corpus's own strong sector.
- [The Parameterised Action: An Ordered Family of Effective Field Theories](the-parameterised-action-an-ordered-family-of-effective-field-theories.html), the family of which stage $0$'s density is a member.
- [The Expansion Parameter: Order Counting and Non-Commuting Truncations](the-expansion-parameter-order-counting-and-non-commuting-truncations.html), the grading that turns the diagram sum into an approximation.
- [Integrating Out and Matching: From One Effective Field Theory to Another](integrating-out-and-matching-from-one-effective-field-theory-to-another.html), how one member of the family is derived from another.
- [The Dictionary: Field Redefinition and Change of Representation](the-dictionary-field-redefinition-and-change-of-representation.html), the condition under which a transcription of this corpus is a rewriting.
- [The Lagrangian and the Second Quantisation: From the Action to the Commutator](the-lagrangian-and-the-second-quantisation.html), the postulate this section imports.
- [Five Steps from a Lagrangian to Fluid Equations](five-steps-from-a-lagrangian-to-fluid-equations.html), the classical counterpart, from which this section takes its shape.
