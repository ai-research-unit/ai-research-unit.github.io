# __The Four Carrier Lists of One Algebra__

## Introduction

**The subject.** The operator space carries four group actions, and each action decomposes the sixteen in its own way. The article writes the lists, computes each one, and identifies which action produces which list. The lists are not interchangeable: two are isotypic, one is a line and a hyperplane, one is a block decomposition, and two are carrier lists. The title counts the four lists of the principal copy; the rotor copy adds two more, and the article writes all six.

**The order of the article.** The four actions come first; the lists second, one section each. The reading then puts the lists side by side.

**It assumes** *The Copy Acting on Sixteen Dimensions*, *The Conjugation Labels Are Integer* and *The Clebsch–Gordan Decomposition of the Operators*. **The row of the elements is** where the same four actions give the four lists of the four-dimensional algebra.

**The result in one line.** The principal copy gives four copies of the module, the rotor copy eight copies of the spinor, the full unit group gives the identity line and the traceless hyperplane, the pair of copies gives the four blocks of a chosen splitting of the module, and the two conjugations give the carriers $7+5+3+1$ and the pieces $2+9+5$.

**Boundaries.** The carriers and their weights are *The Clebsch–Gordan Decomposition* and *The Spin Decomposition*; the conjugation orbits are *The Conjugation Action, the Orbits and the Flag Variety*; the unit group is *The Unitary Group of the Biquaternion Algebra*.

## The Four Actions

**Definition.** The actions are: the **principal copy**, left multiplication by the elements of the copy; the **full unit group**, left multiplication by every unit of the algebra; the **pair of copies**, left multiplication by the copy and right multiplication by the copy simultaneously; and the **conjugation**, the commutator with an element of the copy.

**Proposition.** The four actions commute with one another in the sense that the first and the third are restrictions of the second, and the fourth is the difference of the two halves of the third.

*Proof.* The copy is contained in the unit group; the pair acts by left and right multiplication; and the commutator is the difference of the two.

**Corollary.** Every decomposition of one action is a refinement or a coarsening of the decomposition of the second, and the four lists measure the four ways the sixteen can be cut.

*Proof.* The containment of the groups and the definition of each action.

**The reading.** Four actions, one space. The lists differ because the actions differ, and the article computes each list on the same sixteen dimensions.

## The Principal Copy: Four Copies of the Module

**Theorem.** Under left multiplication by the copy the operator space is isotypic,
$$
\operatorname{End}(\mathbb{B})\cong V_{3/2}^{\oplus 4},\qquad 16=4+4+4+4 .
$$

*Proof.* The operators are the linear maps of the module, and the space of linear maps is the direct sum of four copies of the module, one for each value on a basis; left multiplication acts on the values.

**Corollary.** The Casimir of the left action is the scalar $\tfrac{15}{4}$ on the whole space, and no carrier of the left action is smaller than the module.

*Proof.* The Casimir acts by $j(j+1)$ on each copy, with $j=\tfrac32$.

**Corollary.** The four carriers $7+5+3+1$ are not the decomposition of the left action, and they belong to the conjugation action.

*Proof.* The left action is isotypic, so its only isotypic component is the whole space.

**The reading.** This is the first correction the article records: the four carriers are often attributed to the principal copy, and they are not its decomposition. The principal copy sees sixteen dimensions as four equal blocks and no more.

## The Full Units: $1+15$

**Proposition.** Under left multiplication by the group of units the space splits into the line of the identity and the hyperplane of the traceless operators,
$$
16=1+15 .
$$

*Proof.* The trace is invariant under left multiplication by a unit, since the trace is invariant under similarity; the identity is carried to a scalar multiple of itself, so its line is invariant; the traceless hyperplane is the kernel of the trace and is invariant as well.

**Corollary.** The two pieces are irreducible for the unit group, the line being acted on by the scalars and the hyperplane by the quotient.

*Proof.* The unit group acts transitively on the traceless hyperplane by left multiplications and scalings.

**Corollary.** The split $1+15$ is coarser than every other list, since the unit group contains all the other groups of the enumeration.

*Proof.* Containment of the groups and the invariance of the two pieces.

**The reading.** One line and one hyperplane: the unit group sees only the trace. Every finer list must respect this split, and the traceless hyperplane is where the three other actions do their work.

## The Two Copies: $1+3+3+9$

**Proposition.** Split the module as a line and a three-dimensional complement; then the space of the operators splits into the four blocks of dimensions $1,3,3,9$, and the pair of copies preserves the block structure:
$$
16=1\cdot1+1\cdot3+3\cdot1+3\cdot3 .
$$

*Proof.* The module is the direct sum of the two pieces, and the linear maps of a direct sum decompose into the four blocks of maps between the summands; left multiplication acts on the source and right multiplication on the target, so the blocks are preserved.

**Corollary.** The block of dimension one is the projection onto the line along the complement, and the block of dimension nine is the space of the maps of the complement into itself.

*Proof.* The dimensions of the four blocks.

**Corollary.** The decomposition depends on the choice of the splitting, and the choice is a line of the module.

*Proof.* The blocks are defined by the two summands.

**The reading.** The list $1+3+3+9$ is the block decomposition of a chosen splitting, and it is the only one of the four lists that depends on a choice. It is useful for computations with a fixed spinor and useless for invariants.

## The Conjugation: $7+5+3+1$

**Theorem.** Under the conjugation action the space splits into the four carriers,
$$
16=7+5+3+1,
$$
with the labels $3,2,1,0$.

*Proof.* The weights of the conjugation action are the differences of the weights of the module, and the Clebsch–Gordan series of the square of the module gives the four summands; the dimensions are $2k+1$.

**Corollary.** The four carriers are the eigenspaces of the Casimir of the conjugation action, with the eigenvalues $12,6,2,0$.

*Proof.* The Casimir acts by $k(k+1)$ on the carrier of label $k$.

**Corollary.** The list is canonical, since the eigenvalues are distinct.

*Proof.* The eigenspaces of one operator are canonical.

**The reading.** The list $7+5+3+1$ is the only canonical list of the four, and it is the one attached to the algebra's own structure, the product and the commutator.

## The Table of the Six Lists

The algebra carries two copies of the spin group, the principal copy and the rotor copy, and each of them acts on the operator space in two ways, by multiplication and by conjugation. Six lists result.

| action | list | dimensions |
|---|---|---|
| principal copy, left multiplication | isotypic, Casimir $\tfrac{15}{4}$ | $4+4+4+4=16$ |
| rotor copy, left multiplication | isotypic, Casimir $\tfrac34$ | $2$ taken eight times $=16$ |
| full unit group | identity line and traceless hyperplane | $1+15=16$ |
| two commuting copies | four blocks of a chosen splitting | $1+3+3+9=16$ |
| principal conjugation | the four carriers | $7+5+3+1=16$ |
| rotor conjugation | two, nine and five | $2+9+5=16$ |

**The reading of the table.** Each row adds to sixteen, as it must, and the rows are six different decompositions of one space. The two left actions are isotypic and differ only in the module: the principal copy acts through the module of label $\tfrac32$ and the rotor copy through the spinor taken twice, which is why their Casimirs are $\tfrac{15}{4}$ and $\tfrac34$. The two conjugations are the two carrier lists, the four carriers of the principal copy and the three pieces of the rotor copy.

## The Reading

**Four lists, four meanings.** Isotypic, trace, blocks, carriers. A statement that quotes one list must say which action it belongs to, since the four lists have four different invariance groups.

**The two conjugations.** The list $7+5+3+1$ is the carrier list of the principal copy and $2+9+5$ is the carrier list of the rotor copy. Both are genuine decompositions of the same sixteen-dimensional space, and neither refines the other: the four carriers of the principal reading and the pieces $2$, $9$, $5$ of the rotor reading are cut by different commuting operators.

**Six, not four.** A list quoted without its copy is ambiguous. The four-carrier list belongs to the principal copy; the rotor copy gives three pieces, of dimensions two, nine and five, and its left action is isotypic with the smaller Casimir.

**One rule of thumb.** The finer the group, the coarser the list: the unit group gives two pieces, the pair of copies four blocks, the conjugation four carriers of unequal size, and the principal copy one isotypic block of four.

## Further Reading

- [The Copy Acting on Sixteen Dimensions](the-copy-acting-on-sixteen-dimensions.html), for the left and the conjugation actions compared.
- [The Conjugation Labels Are Integer](the-conjugation-labels-are-integer.html), for the arithmetic behind the list $7+5+3+1$.
- [The Unitary Group of the Biquaternion Algebra](the-unitary-group-of-the-biquaternion-algebra.html), for the unit group of the list $1+15$.
- [The Spin Decomposition: Four Carriers and the Weight Multiset $0^{4},\pm1^{3},\pm2^{2},\pm3$](the-spin-decomposition-four-carriers-and-the-weight-multiset.html), for the weights of the sixteen.
