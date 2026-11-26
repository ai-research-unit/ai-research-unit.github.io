# __The Centraliser, the Complement, and the Index: Dimension Falls at a Breaking, Rank Rises at an Arrival__

## Introduction

**The layer.** This article is about the vocabulary of the transition, and its Layer-A content is the two ways a symmetry can appear or disappear when a vacuum is chosen. **It proves one theorem, computes four dimensions, and settles a word.**

**The question.** When the primordial force breaks and two forces are left, in what sense does anything *survive*, in what sense does anything *break*, and in what sense is a force *created*? The three words are used loosely everywhere in physics writing; here they are used exactly.

**The answer.**

$$
\boxed{\;
\text{a subgroup that leaves: dimension falls, rank does not rise;}
\;}
$$
$$
\boxed{\;
\text{an index that arrives: rank rises, and no subgroup was involved.}
\;}
$$

**So a transition can do two opposite things at once, and they are not two mechanisms.** The same vacuum that removes six directions can announce a two-dimensional space; the first is a breaking by dimension, the second a birth by rank. **The two are compatible because they act on different objects: the first on the algebra, the second on the representation the condensate carries.**

**What this article establishes.** The three-operation grammar and the table of which operation applies where; the obstruction theorem in its sharpest form, with the dimension that makes it irreversible; the reason the same number six appears in both stories and why that coincidence is the trap; and the resolution of the word *emergent*, which the earlier plan used and which this article replaces.

**Not established.** Anything about dynamics. Whether the index *arrives with* the condensation or is *required by* it is a question this article states and does not answer. **It distinguishes the two readings and refuses to blur them**, which is the most a structural article can do.

**Where the rest is.** The transition is [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). The mechanism is [Rank Five From Three](rank-five-from-three-the-weak-factors-as-a-condensate-index.html). The theorem that forecloses the other route is [The Charge Theorem](the-charge-theorem-the-sextet-cannot-be-recomposed-into-the-weak-pair.html). The scales are [The Matching at $M_C$](matching-at-m-c-the-four-quantities-that-cross-and-where-the-masses-come-from.html).

## The Three Operations, and What Each Requires

**The vocabulary, with the object each operation acts on.**

| operation | object it acts on | what must be true | example in this model |
| --- | --- | --- | --- |
| **survives** | a subalgebra | the vacuum is annihilated by it | colour, $\mathrm{SU}(3)_c$ |
| **breaks** | a complement | the vacuum does not commute with it | the sextet, $\mathfrak m$ |
| **arrives** | a factor | the transition carries an index | $\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ |

**The three are not degrees of the same process.** *Survives* and *breaks* are statements about a single algebra and a single vacuum: the vacuum splits the algebra into a centraliser and a complement, and the two words name the two pieces. **Both are decided by one computation, $[iD,\cdot\,]$, and both are therefore reversible in principle** — a different vacuum gives a different split.

**Arrives is a statement of a different kind.** It does not say which piece of the algebra survives; **it says that the list of factors has grown.** No computation on $\mathfrak{su}(4)$ alone can produce it, because the list of factors before the transition has no weak entries to preserve or destroy.

**The confusion this article removes.** A reader who has only the first two operations will try to express the third in their terms — "the weak force survives as a subalgebra" or "the weak force emerges from the debris" or "the weak force is the complement of colour". **All three are phrased in a vocabulary that cannot express arrival, and all three are false for that reason before any calculation is done.**

## The Rank Account: Downward Inside, Free Across

**Inside one algebra, rank is monotone.** That is the lemma, and it is one line: a torus of a subalgebra lies in a torus of the algebra.

**Across independent factors, rank is additive.** That is the definition of rank for a direct product: a maximal torus of $G\times H$ is a torus of $G$ times a torus of $H$.

**So the two halves of the account behave differently, and the difference is the whole story.**

$$
\operatorname{rank}\bigl(\text{subalgebra}\bigr)\ \le\ \operatorname{rank}\bigl(\text{algebra}\bigr),
\qquad
\operatorname{rank}(G\times H)=\operatorname{rank}G+\operatorname{rank}H .
$$

**The first line forbids the weak force inside $\mathrm{SU}(4)$.** The second line forbids nothing, because it is not a statement about inclusion. **A construction that uses only the first line will fail; one that uses the second will succeed if, and only if, it can produce the factors as separate factors.**

**The accounting for this model.**

| step | operation | rank |
| --- | --- | --- |
| start | $\mathrm{SU}(4)$ | $3$ |
| breaks | $\mathrm{SU}(4)\to\mathrm{SU}(3)\times\mathrm{U}(1)$ | $3$, unchanged: $2+1$ |
| arrives | $\times\,\mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ | $3+1+1=5$ |

**The middle row is why the first row's number never changes.** A rank-preserving breaking followed by an arrival of two ranks: **no step in the table breaks the lemma, and the endpoint has rank five.** A careful reader should be suspicious at this point, and the next two sections are the answers to the suspicion.

## The Obstruction, in Its Sharpest Form

**The theorem, stated so that no rearrangement escapes it.**

> **Theorem.** There is no $g\in\mathrm{SU}(4)$ and no subspace $\mathfrak h$ of $\mathfrak{su}(4)$ with $\operatorname{Ad}_g\mathfrak m=\mathfrak h$ and $\mathfrak h$ closed under brackets of dimension $6$ — in particular, $\mathfrak{so}(4)$ is not a conjugate of the sextet.

**Proof, in three steps.**

**Step one: conjugation preserves brackets.**

$$
\bigl[\,gXg^{-1},\ gYg^{-1}\,\bigr]=g\,[X,Y]\,g^{-1}.
$$

**Step two: therefore it preserves closure and the dimension of the closure.** If $\mathfrak a$ is any subspace, then

$$
\operatorname{Ad}_g\bigl([\mathfrak a,\mathfrak a]\bigr)=\bigl[\operatorname{Ad}_g\mathfrak a,\ \operatorname{Ad}_g\mathfrak a\bigr],
$$

**so the dimension of the bracket span is an invariant of the orbit.**

**Step three: the invariant differs.**

$$
\dim[\mathfrak m,\mathfrak m]=9\ \ (\text{it is all of }\mathfrak u(3)),
\qquad
\dim[\mathfrak{so}(4),\mathfrak{so}(4)]=6\ \ (\text{it is all of }\mathfrak{so}(4)).
$$

**Nine is not six, so the two subspaces lie on different orbits.** 

**Why the number nine matters.** The sextet's brackets close on the *strong* force and on nothing else: $[\mathfrak m,\mathfrak m]=\mathfrak u(3)$, dimension $9$, which is the dimension of the surviving sector. **So the sextet is not a reservoir of weak directions — it is a reservoir of colour directions.** Its own algebra regenerates what colour already is.

**The same theorem in one sentence.** **A closed set can only be carried to a closed set, and the sextet's closure is nine-dimensional while any six-dimensional closed set's closure is six-dimensional.** The obstruction is a dimension count on a closure, and that is why it survives every change of basis, ordering, and dynamics.

## Four Dimensions That Describe the Relation

**A second, quantitative description of the same relation**, useful because it says how far apart the two readings are rather than merely that they differ.

$$
\dim\mathfrak u(3)=9,\qquad
\dim\mathfrak s(\mathfrak u(2)\oplus\mathfrak u(2))=7,\qquad
\dim\bigl(\mathfrak u(3)+\mathfrak s\bigr)=12 .
$$

**So the two maximal-rank readings share four dimensions and differ in three.**

| quantity | value | what it is |
| --- | --- | --- |
| $\dim\mathfrak u(3)$ | $9$ | colour plus $B-L$ |
| $\dim\mathfrak s(\mathfrak u(2)\oplus\mathfrak u(2))$ | $7$ | weak pair plus $B-L$ |
| their span | $12$ | $9+7-4$ |
| their intersection | $4$ | $\operatorname{span}\{A_{xy},A_{xz},A_{yz},iD\}$ |
| their Lie closure | $15$ | all of $\mathfrak{su}(4)$ |
| the closure defect | $3$ | the span misses three directions of the fifteen |

**Read the intersection.** The common part is the three colour rotation planes plus $B-L$: **what colour and the weak pair share, in this basis, is the *rotation* part of colour and the abelian direction, and nothing else.** The colour planes $iS_{xy},iS_{xz},iS_{yz}$ are not in the weak pair; the weak planes $T^{L}_{a},T^{R}_{a}$ all contain a leptoquark component and so are not in colour.

**Read the closure.** Twelve plus brackets gives fifteen. **The two readings generate the algebra between them**, which is the algebraic reason they cannot both be exact: a vacuum annihilated by both would be annihilated by all fifteen generators, and $\mathfrak{su}(4)$ is simple, so no such vacuum exists. **The corpus's statement that the two are the maximal-rank subgroups and their closure is everything is this line.**

**Read the defect.** Three directions are in neither. **They are the ones that carry the leptoquark content**, which is why the weak planes, which do contain leptoquark components, are not available as factors of the surviving algebra. **This is the same fact as the theorem of the previous section, counted differently.**

## Why Six Keeps Appearing, and Why That Is the Trap

**The coincidence, stated plainly.**

$$
\underbrace{15}_{\mathfrak{su}(4)}=\underbrace{8+1}_{9}+\underbrace{6}_{\mathfrak m},
\qquad
\underbrace{15}_{\text{endpoint}}=\underbrace{8+1}_{9}+\underbrace{3+3}_{6}.
$$

**The same fifteen, the same nine, and the same six — split two ways.** In the first split the six is a complement and is *not* closed; in the second the six is two factors and *is* closed. **The numbers agree and the algebra does not**, which is exactly the configuration that produces a plausible and wrong story.

**Why the wrong story is so attractive.** It costs nothing to write: the sextet is six, the weak pair is six, both sit in fifteen alongside nine. **The reader supplies the missing step — that the six can be rearranged into the six — and that step is the one the theorem forbids.**

**Why the correction is not pedantry.** The two splits differ in a measurable way: the first has a six-dimensional subspace whose brackets span nine, the second has a six-dimensional subalgebra whose brackets span six. **A prediction that depends on the sextet's brackets — the mass matrix, the flavour bound, the proton-decay dimension — is a prediction about the first split, and nothing in it knows about the second.**

**The sentence that carries it into the articles.** **Equal dimension is not equal structure: nine plus six open is $\mathfrak{su}(4)$, nine plus three plus three closed is the world after the transition, and the difference between the two sixes is closure.**

## What an Index Is, and Why Only an Index Can Arrive

**The inventory of a transition.** At a breaking a theory has four kinds of object at its disposal: a vacuum, a condensate, a scalar multiplet, and a set of couplings. **Which of them can carry a factor?**

**A vacuum cannot.** It is a point of a coset, and choosing a point removes symmetry; it never adds a group.

**A condensate cannot, by itself.** The condensate is a number times a direction, and a direction is annihilated or not annihilated; there is no third option.

**A coupling cannot.** A coupling is a number multiplying an invariant, and an invariant is built from the groups that already exist.

**A scalar multiplet can, and only a multiplet can.** A multiplet is specified by its indices, and an index names a space on which a group acts. **When a multiplet appears in the spectrum carrying an index, a factor exists whether or not anyone has written it down**; the transition does not create the group, it makes the index dynamical by making its scalar condense.

**This is the precise content of the phrase "arrives with the index".** The weak force is not manufactured; it was never absent from the *representation theory*, only from the *algebra*. **The transition is the moment the difference stops mattering, because the object carrying the index is the object doing the breaking.**

**And it is why the word is "index" and not "sector".** A new sector would be new fields with new couplings — a new group, a new scale, a new dynamics. An index is a property of a field the model already has. **The whole economy of the construction is in that distinction**, and it is the distinction the earlier version of this work lost when it proposed a confining sector.

## Where the Word "Emergent" Went Wrong

**The earlier plan said the weak pair is emergent.** The word came from condensed-matter usage: a symmetry of the low-energy spectrum that is not a symmetry of the microscopic Lagrangian. **It is a good word and it was the wrong word here**, for two reasons.

**Reason one: it presupposed a composite.** An emergent symmetry in that sense is a symmetry of a *composite spectrum*, and it requires bound states. **This model has none** — the charge theorem and the confinement-scale theorem both forbid the composites that would be needed. **So the vocabulary imported a mechanism the model does not have.**

**Reason two: it described the wrong direction.** Emergence says the group appears *from below*, out of the dynamics of constituents. **What happens here is that the group appears *from the side*, out of the representation of one field.** The rank goes up by two while the constituents stay put.

**The replacement, and its justification.**

| word | what it claims | true here? |
| --- | --- | --- |
| emergent | a symmetry of a composite spectrum | **no**: no composites exist |
| survives | a subalgebra of the algebra | for colour, **yes** |
| arrives | a factor borne by an index | for the weak pair, **yes** |

**"Arrives" is weaker than "emergent" and it is the weaker claim that is true.** It says less about mechanism and exactly enough about structure: **the factor is there because the index is there, and the index is there because the transition's scalar is a doublet.**

## What the Breaking Buys and What the Birth Adds

**The ledger, side by side.**

| | the breaking | the birth |
| --- | --- | --- |
| object acted on | the algebra $\mathfrak{su}(4)$ | the representation of $Ξ$ |
| operation | centraliser of $iD$ | the $\mathbf 2$ index |
| rank change | $3\to3$ | $3\to5$ |
| dimension change | $15\to9$ | $9\to15$ |
| what is removed | six directions | nothing |
| what is added | nothing | six directions, in three plus three |
| what it costs | six vectors at $32v^{2}$ | one postulated representation |

**The two rows that make the article worth writing.** The breaking removes six directions and the birth adds six directions, **at different scales, by different mechanisms, with different statuses.** A reader who conflates them will conclude that the transition does nothing; a reader who keeps them apart sees the whole structure in two lines.

**And the rank row is the one to check every future claim against.** Any claim that assigns the weak force a rank inside $\mathfrak{su}(4)$ contradicts the lemma. Any claim that assigns it a rank beside $\mathfrak{su}(4)$ is compatible with everything in this article. **There is no third possibility**, and that exhaustiveness is what makes the two-verb grammar worth adopting.

## The Checks

| claim | check | result |
| --- | --- | --- |
| the lemma | torus of $\mathfrak h$ lies in a torus of $\mathfrak g$ | $\operatorname{rank}$ monotone downwards |
| additivity | maximal torus of $G\times H$ | $\operatorname{rank}G+\operatorname{rank}H$ |
| the sextet's closure | $[\mathfrak m,\mathfrak m]$ computed | $\mathfrak u(3)$, dimension $9$ |
| the weak pair's closure | $[\mathfrak{so}(4),\mathfrak{so}(4)]$ | $\mathfrak{so}(4)$, dimension $6$ |
| the orbit invariant | $\dim$ of the closure is $\operatorname{Ad}$-invariant | $9\ne6$, no conjugation |
| the two subgroups | $9+7-4$ | span $12$, intersection $4$ |
| the intersection | $A_{xy},A_{xz},A_{yz},iD$ | colour rotations plus $B-L$ |
| the joint closure | span plus brackets | $15$, all of $\mathfrak{su}(4)$ |
| the dimension coincidence | $8+1+6=8+1+3+3$ | $15=15$ |
| the difference | closure of the six | open $9$ against closed $6$ |

## Distinctions That Are Easy to Lose

Breaking is not shrinking. The group loses six directions and keeps its rank; a breaking that reduced the rank would be a different event (*The Three Operations*).

Arriving is not emerging. Arrival is a property of an index; emergence is a property of a composite spectrum, and this model has no composites (*Where the Word "Emergent" Went Wrong*).

The sextet's brackets close on colour. That is not a detail: it is why the sextet is the parent of the strong force and not of the weak one (*The Obstruction*).

Equal dimension is not equal structure. Nine plus six open and nine plus three plus three closed are both fifteen and are not the same fifteen (*Why Six Keeps Appearing*).

An index is not a sector. The whole economy of the construction is that the weak force costs a representation and not a group (*What an Index Is*).

## Summary

**Three operations, three objects.** A subalgebra *survives* when the vacuum annihilates it, a complement *breaks* when the vacuum does not commute with it, and a factor *arrives* when the transition carries an index naming it. **Only the third raises the rank, and only the third is needed for the weak force.**

**Rank is monotone downwards inside an algebra and additive across factors.** That asymmetry is the entire account: $3\to3$ at the breaking, $3\to5$ at the birth, no step violating the lemma.

**The obstruction is a dimension count on a closure.** $\operatorname{Ad}$ preserves brackets, so it preserves the dimension of the closure; $[\mathfrak m,\mathfrak m]$ is nine-dimensional and any six-dimensional closed set closes on six; therefore no conjugation carries the sextet to the weak pair. **The sextet's brackets regenerate the strong force.**

**The relation between the two readings is four dimensions.** Span $12$, intersection $4=\operatorname{span}\{A_{xy},A_{xz},A_{yz},iD\}$, joint closure $15$. **They differ in three directions and together generate everything, which is why one vacuum cannot keep both.**

**Six appears twice and means two different things.** Nine plus six open is the algebra; nine plus three plus three closed is the world after the transition. **Closure is the difference, and it is the whole difference.**

**"Emergent" was the wrong word.** It imports a composite spectrum the model does not have. **"Arrives" says exactly what is true: the factor is there because the index is.**

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mathfrak m$ | the sextet, the complement of $\mathfrak u(3)$ |
| $\mathfrak u(3)$ | colour plus $B-L$, the centraliser of $iD$, dimension $9$ |
| $\mathfrak s(\mathfrak u(2)\oplus\mathfrak u(2))$ | the weak pair plus $B-L$, dimension $7$ |
| $\operatorname{Ad}_g$ | conjugation by $g$, which preserves brackets and closure dimensions |
| $[\mathfrak a,\mathfrak a]$ | the span of all brackets of elements of $\mathfrak a$ |
| $Ξ$ | the transition's scalar, whose $\mathbf 2$ index is the arriving factor |
| $\lambda$ | the index of a multiplet, the object that can carry a factor |

## Further Reading

- [Rank Five From Three: A Condensate Index, Five Ranks From Three](rank-five-from-three-the-weak-factors-as-a-condensate-index.html). The construction this article supplies the grammar for.
- [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). The surviving and the broken pieces, computed.
- [The Charge Theorem: The Sextet Cannot Be Recomposed Into the Weak Pair](the-charge-theorem-the-sextet-cannot-be-recomposed-into-the-weak-pair.html). The second and third closures.
- [The Commutation Table of the Fifteen Generators: 441 Entries, 164 Nonzero](the-commutation-table-of-the-fifteen-generators-225-entries-105-independent-80-nonzero-and-five-rules.html). The brackets that the closure dimensions are read from.
- [$\mathfrak{su}(4)$ as $\mathfrak{so}(4)$ and Nine More](../articles_internal/structures/structure-SU4-SO4-relations.html). The involution behind the twelve-and-nine split.
