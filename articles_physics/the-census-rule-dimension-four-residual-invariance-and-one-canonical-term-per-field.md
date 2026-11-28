# __The Census Rule: Dimension Four, Residual Invariance, and One Canonical Term per Field__

## Introduction

**The claim.** The Lagrangian of the Standard Model, written in the broken phase and in the mass basis, is a list. This article states the rule that generates the list, and then counts it. The count is not the point. The point is that the rule is stated before the list, so that a reader with a pencil can add the rows up and get the same number.

**The answer.**

$$
\boxed{\;49=4+2+1+1+12+9+5+9+4+2\;}
$$

**The standing.** Every piece in the list is standard theory. Nothing here is derived from the biquaternion algebra, and no coefficient is computed. What the article and its twenty-two companions add is three things: a criterion that says which pieces are possible, a proof that nothing else is possible, and a count with its rule attached to it.

**Why a rule and not a list.** A list of terms is unfalsifiable. Given a Lagrangian, a reader can delete a term and ask why it was there, and the answer "it is in the Standard Model" is circular. A criterion makes every term answerable: it is in the list because it is a dimension-four invariant of the residual group, and every dimension-four invariant of the residual group is in the list.

## The Criterion

**Four conditions, and a piece must satisfy all four.**

A piece is admissible when it is a Lorentz scalar, invariant under the residual group $SU(3)_c\times U(1)_{\mathrm{em}}$, of mass dimension at most four, and built from the fields the broken phase contains.

The first two are symmetries. The third is renormalisability. The fourth is what makes this a broken-phase list rather than a symmetric-phase one: the fields are the mass eigenstates, so a piece is built from $G^a_\mu$, $A_\mu$, $Z_\mu$, $W^\pm_\mu$, $h$ and the twelve fermion species, and not from $W_{a,\mu}$, $B_\mu$ and the doublet.

**Why the broken phase.** Because the list is then one list. In the symmetric phase a piece may be built from a doublet, and the number of pieces depends on how the scalar is written, on whether the conjugate doublet is a second object, and on how many components are counted separately. In the broken phase every field has a definite mass, one scalar remains, and the residual group is a product of a colour factor and a phase. The pieces are then exactly the terms a calculator would use.

**The price, stated now.** The criterion of this article is residual invariance, and residual invariance alone is too weak. A Majorana mass $\tfrac12m_\nu\bar\nu^c_L\nu_L$ is a dimension-three invariant of $SU(3)_c\times U(1)_{\mathrm{em}}$ and would be admitted. It is excluded, and the exclusion does not come from this criterion but from a second one: every piece must descend from a dimension-four invariant of the *unbroken* group. That second criterion is stated and used in [The Completeness of the List](the-completeness-of-the-list-why-no-other-dimension-four-piece-exists.html) and [The Unitary-Gauge Image](the-unitary-gauge-image-the-lineage-of-every-piece-and-where-the-three-goldstones-went.html), and the neutrino mass is its one witness.

## The Four Counting Conventions

A count needs a convention as much as a criterion needs a rule. Four are used, and each is stated so that it can be changed without ambiguity.

| Convention | Statement | What it excludes |
|---|---|---|
| one piece per canonical term | a sum over colour, and a sum over the species of one type, is one piece | eighteen quark kinetic terms counted as one |
| $\mathrm{h.c.}$ counted once | a term and its Hermitian conjugate are one piece | doubling the charged current |
| self-interactions inside the curvature | the triple and quartic gauge vertices are sub-structures of the four field-strength pieces and are counted as vertices, not pieces | six extra rows in the piece list |
| coefficient-blind | two pieces differing only by a coefficient are one piece | counting $h\bar uu$ and $h\bar dd$ as different kinds |

**The second convention is the one that decides the total.** The charged current has two terms, one with quarks and one with leptons, and they are two pieces and not one. Its Hermitian conjugate is a third and a fourth term of the same two pieces.

**The third convention is the one that decides between the two counts.** With self-interactions folded into the curvatures the count is forty-nine. With them separated the count is fifty-five, and the six added rows are $\gamma W^+W^-$, $ZW^+W^-$, $W^+W^-W^+W^-$, $W^+W^-AA$, $W^+W^-AZ$ and $W^+W^-ZZ$. Both numbers are correct and they count different objects. The category uses forty-nine for pieces and fifty-five for vertices.

## The Summation

**The ten groups, in the order the companions present them.**

| Group | Pieces | Where |
|---|---|---|
| the four field strengths | $4$ | [The Four Field Strengths](the-four-field-strengths-one-kinetic-piece-per-gauge-field.html) |
| the two vector masses | $2$ | [The Two Vector Masses](the-two-vector-masses-proca-as-the-representative-of-the-condensate.html) |
| the Higgs kinetic piece | $1$ | [The Higgs Kinetic and Mass Pieces](the-higgs-kinetic-and-mass-pieces-and-the-tadpole-condition.html) |
| the Higgs mass piece | $1$ | the same |
| the twelve fermion kinetic pieces | $12$ | [The Twelve Fermion Kinetic Pieces](the-twelve-fermion-kinetic-pieces-nine-massive-species-three-neutrinos-and-their-currents.html) |
| the nine fermion masses | $9$ | [The Nine Dirac Masses](the-nine-dirac-masses-and-the-tenth-the-minimal-model-omits.html) |
| the five gauge interactions | $5$ | [The Five Blocks](the-replacement-of-the-derivative-five-blocks-and-nothing-else.html) |
| the nine Higgs–fermion pieces | $9$ | [The Higgs–Fermion Pieces](the-higgs-fermion-pieces-nine-couplings-fixed-by-nine-masses.html) |
| the four Higgs–vector pieces | $4$ | [The Four Higgs–Vector Pieces](the-four-higgs-vector-pieces-two-normalisations-and-the-photon-that-does-not-appear.html) |
| the two Higgs self-pieces | $2$ | [The Higgs Self-Pieces](the-higgs-self-pieces-two-couplings-and-one-quartic.html) |

**The free and the interacting halves.** The first six groups are the quadratic pieces: twenty-nine of them, each carrying one coefficient, each fixing one mass or one normalisation. The last four are the interactions: twenty of them. The split is a check, $29+20=49$, and it is also a statement: every free piece is fixed by a mass and every interaction by a coupling.

**The four Higgs–vector pieces are the ones a first draft of this category omits.** Expanding the scalar kinetic term in the unitary chart gives $\tfrac{(v+h)^2}{8}\bigl[g^2(W_1^2+W_2^2)+(gW_3-g_{\mathrm Y}B)^2\bigr]$, and the square brings four terms and not two: $hVV$ and $hhVV$. A list that carries $hWW$ and $hZZ$ and stops there is a list of the vertices a first-year course draws, not of the pieces the Lagrangian contains. The four are in the count and [The Four Higgs–Vector Pieces](the-four-higgs-vector-pieces-two-normalisations-and-the-photon-that-does-not-appear.html) writes them.

## The Three Counts

| Count | Value | Rule |
|---|---|---|
| pieces | $49$ | the four conventions above |
| vertices | $55$ | pieces, with the six gauge self-interaction structures separated out |
| blocks | $22$ | pieces, with the three flavour sums folded ($12\to1$, $9\to1$, $9\to1$) |
| parameters | $19$ | $18$ multiplying a piece, $+1$ multiplying none |

**The block count is the least useful and it is stated for completeness.** Folding the flavour sums removes $11+8+8=27$ rows from forty-nine. Any further folding — a single "gauge kinetic" block, a single "Yukawa" block — is a choice of presentation and not a fact about the Lagrangian, so the category does not print a fourth number for it.

**The parameter count is the one that matters.** Eighteen of the nineteen multiply a row of the list: the strong coupling, the electric charge, the weak mixing angle, the vacuum value, the Higgs mass, nine fermion masses and the four mixing parameters. The nineteenth, $\theta_{\mathrm{QCD}}$, multiplies no row, because the operator it multiplies is a total derivative and is not in the list. [The Coefficients the List Carries](the-coefficients-the-list-carries-eighteen-constants-and-the-one-that-multiplies-no-piece.html) prints the map.

## What the Count Is Not

**Not a count of diagrams.** A piece with four fields contains more than one vertex once the fields are permuted; $-\tfrac14G^a_{\mu\nu}G^{a\mu\nu}$ contains a three-gluon and a four-gluon vertex. The list counts monomials.

**Not a count of measurements.** The nineteen parameters are measured many times each: the Higgs mass fixes the cubic and the quartic self-coupling too, and one coupling fixes a whole column of vertices. A count of measurements is larger and is a different object.

**Not a claim of completeness by itself.** A summation line is arithmetic. The claim that no other piece exists is a theorem, and it is proved in [The Completeness of the List](the-completeness-of-the-list-why-no-other-dimension-four-piece-exists.html) by enumerating the field multiplicities and excluding the rest one candidate at a time.

## Checks

1. The summation. $4+2+1+1+12+9+5+9+4+2=49$, recomputed term by term.
2. The split. The twenty-nine quadratic pieces less the twenty interactions gives forty-nine, and the twenty interactions are $5+9+4+2$ by group.
3. The vertex count. $49+6=55$, the six being the two triple and four quartic gauge structures inside the $W$ curvature.
4. The block count. $49-11-8-8=22$.
5. The parameter count. $1+1+1+1+1+9+4=18$, and $18+1=19$.
6. The coefficient-per-piece check. Twenty-nine quadratic pieces, twenty-nine coefficients in [The Coefficients the List Carries](the-coefficients-the-list-carries-eighteen-constants-and-the-one-that-multiplies-no-piece.html) once the nine masses and the four mixing parameters are counted as they are used.
7. The degree-of-freedom check, which belongs to the count and not to the criteria: twenty-eight before the rotation ($12$ vectors $\times2$ plus $4$ scalars) and twenty-eight after ($8$ massless vectors $\times2$, the photon $\times2$, three massive vectors $\times3$, one scalar).
8. The list against the assembly. Four field strengths, one fermion kinetic term, one scalar kinetic term, one potential, one Yukawa sector and one vacuum-angle term: the six ancestors of [The Standard Model and the Lagrangian](the-standard-model-and-the-lagrangian-four-sectors-in-one-expression.html) account for every row, as [The Unitary-Gauge Image](the-unitary-gauge-image-the-lineage-of-every-piece-and-where-the-three-goldstones-went.html) tabulates.

## Summary

The list of possible Lagrangian pieces of the Standard Model in the broken phase is generated by four conditions — Lorentz scalar, invariant under $SU(3)_c\times U(1)_{\mathrm{em}}$, dimension at most four, built from the mass eigenstates — together with a descent condition that excludes pieces with no dimension-four ancestor of the unbroken group. Four counting conventions fix the arithmetic: one piece per canonical term with colour and species summed, $\mathrm{h.c.}$ counted once, gauge self-interactions counted inside the curvatures, and a coefficient treated as a label of a piece and not as a new piece.

The count is $49=4+2+1+1+12+9+5+9+4+2$: four field strengths, two vector masses, the Higgs kinetic and mass pieces, twelve fermion kinetic pieces, nine Dirac masses, five gauge interactions, nine Higgs–fermion pieces, four Higgs–vector pieces and two Higgs self-pieces. The same list carries fifty-five vertices once the six gauge self-interaction structures are separated out, twenty-two blocks once the three flavour sums are folded, and nineteen parameters.

Twenty-nine of the pieces are quadratic and each fixes one mass or normalisation; twenty are interactions and each carries a coupling. The four Higgs–vector pieces are the ones a sketch of the list usually drops, and the omission is not a convention but an error: the square $(v+h)^2$ produces $hhVV$ as well as $hVV$.

The criterion of residual invariance is too weak on its own: it would admit a Majorana neutrino mass. The descent condition is the second half of the criterion, and it is what makes the neutrino's absence from the list a statement about the symmetric phase and not a modelling choice.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{L}$ | The Lagrangian density of the broken phase |
| $G^a_\mu$, $A_\mu$, $Z_\mu$, $W^\pm_\mu$ | The twelve gauge fields in the mass basis |
| $G^a_{\mu\nu}$, $F_{\mu\nu}$, $Z_{\mu\nu}$, $W^\pm_{\mu\nu}$ | Their field strengths |
| $h$ | The one physical scalar |
| $g_s$, $e$, $g$, $g_{\mathrm Y}$, $\theta_W$ | The couplings and the weak mixing angle |
| $v$ | The vacuum value, $M_W=gv/2$ |
| $\theta_{\mathrm{QCD}}$ | The vacuum angle, the parameter that multiplies no piece |
| $49$, $55$, $22$, $19$ | Pieces, vertices, blocks, parameters |

## Further Reading

- [The Completeness of the List](the-completeness-of-the-list-why-no-other-dimension-four-piece-exists.html). The theorem that the forty-nine are all of them, and the exclusions one candidate at a time.
- [The Unitary-Gauge Image](the-unitary-gauge-image-the-lineage-of-every-piece-and-where-the-three-goldstones-went.html). Each of the forty-nine rows against the ancestor it descends from.
- [The Standard Model and the Lagrangian: Four Sectors in One Expression](the-standard-model-and-the-lagrangian-four-sectors-in-one-expression.html). The symmetric-phase assembly whose pieces these are the images of.
- [The Data Boundary](the-data-boundary.html). The rule that fixes where a measured number may be printed; this category prints symbols only.
- [The Parameter Count as the Measure of the Framework's Boundary](the-parameter-count-as-the-measure-of-the-frameworks-boundary.html). The nineteen, itemised and typed by the kind of object each one is.
