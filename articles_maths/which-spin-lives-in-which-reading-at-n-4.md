# __Which Spin Lives in Which Reading at $n=4$__

## Introduction

**The subject.** The four lists of *The Four Carrier Lists of One Algebra* use the same sixteen dimensions, and the question is which spin, that is which label, occurs in which reading. The article answers with a table and with the diagonal contents of the factorised and block readings.

**The order of the article.** The first section fixes the table of spins against the four readings. The second computes the diagonal contents. The third checks them against the Clebsch–Gordan rule and finds $V_2\oplus3V_1\oplus2V_0$ of dimensions $5+9+2$. The fourth identifies the half-integer pair. The fifth draws the lesson and the boundary.

**It assumes** *The Four Carrier Lists of One Algebra at $n=4$* for the four lists and *The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$* for the principal one. The row at order two is *Which Spin Lives in Which Reading*.

**The result in one line.** Spin $3$ occurs as a piece only in the principal reading, spin $2$ in the principal reading and as a diagonal content of the factorised one, spin $1$ in three readings, and the half-integer $\tfrac32$ only on the module and on the minimal left ideals.

**Boundaries.** The article compares the readings and computes the diagonal contents; it does not compute the Casimir of the factorised or block groups, which would refine the diagonal contents.

## The Table

**Proposition.** The occurrences of the spins in the four readings are

| spin | dimension | principal | $U(4)$ | factorised | block |
|---|---|---|---|---|---|
| $3$ | $7$ | piece $V_3$ | none | content of $(1,1)$ | none |
| $2$ | $5$ | piece $V_2$ | none | content of $(1,1)$ | none |
| $\tfrac32$ | $4$ | module only | none | none | none |
| $1$ | $3$ | piece $V_1$ | none | pieces $(1,0)$ and $(0,1)$ | content of the diagonal blocks |
| $\tfrac12$ | $2$ | none | none | none | the pair in the corners |
| $0$ | $1$ | piece $V_0$ | the scalars | piece $(0,0)$ | the scalars of each block |

*Proof.* The principal column is the decomposition of the tensor square. The $U(4)$ column is the decomposition $\mathbb{C}\mathrm I\oplus\mathfrak{sl}_4$, and the traceless part contains no proper invariant piece. The factorised column is the tensor product $1\otimes1+1\otimes3+3\otimes1+3\otimes3$, whose diagonal contents are computed in the next section. The block column is the splitting into the two diagonal and two off-diagonal blocks.

**Corollary.** Spin $3$ occurs as a piece in the principal reading alone, and spin $2$ as a piece in the principal reading alone.

*Proof.* The table: the other lists have no piece of dimension $7$ or $5$.

**Corollary.** Spin $1$ occurs in three readings: as the piece $V_1$, as the two triplets of the factorised list, and as the diagonal content of the block list.

*Proof.* The dimensions $3$ in the table.

**The reading.** The table is the precise form of the statement that the phrase "the spins of $M_4(\mathbb{C})$" is ambiguous: the same label appears in different readings and not in others.

## The Diagonal Contents

**Proposition.** In the factorised reading, restricting the action to the diagonal copy $SU(2)\subset SU(2)\times SU(2)$ gives the pieces $(1,0)$ and $(0,1)$ both equal to the triplet $V_1$, the piece $(0,0)$ equal to $V_0$, and the piece $(1,1)$ equal to $V_2\oplus V_1\oplus V_0$.

*Proof.* The diagonal copy acts on $\mathbb{C}^{2}\otimes\mathbb{C}^{2}$ by $g\otimes g$, so on $\operatorname{End}(\mathbb{C}^{2})\otimes\operatorname{End}(\mathbb{C}^{2})$ by the tensor product of the conjugation actions; the pieces $(1,0)$ and $(0,1)$ are the triplets, and $(1,1)$ is the tensor product $V_1\otimes V_1$, which decomposes as $V_2\oplus V_1\oplus V_0$ by the Clebsch–Gordan rule.

**Corollary.** The diagonal contents of the factorised list are $V_2\oplus3V_1\oplus2V_0$, of dimensions $5+9+2=16$.

*Proof.* One $V_2$ and one $V_1$ and one $V_0$ from $(1,1)$, one $V_1$ from each triplet and one $V_0$ from the trivial piece.

**Corollary.** The principal reading gives $V_3\oplus V_2\oplus V_1\oplus V_0$, of dimensions $7+5+3+1=16$, which is a different decomposition of the same space into the same labels with different multiplicities.

*Proof.* The principal list and the diagonal contents differ in the multiplicities of $V_3$, $V_1$ and $V_0$.

**The reading.** Neither list refines the other, and the word *coarser* has no meaning here, because the two decompositions belong to two different groups. The diagonal contents have six pieces against the four of the principal list, and no piece of dimension seven; the principal list has one triplet where the diagonal contents have three, and one singlet where they have two. The only comparison that survives is the count, $7+5+3+1=5+9+2=16$.

## The Half-Integer Pair

**Proposition.** In the block reading, the two off-diagonal corner blocks each split into a triplet and a singlet, and the two singlets form a two-dimensional piece on which the labels are the pair $(\tfrac12,\tfrac12)$.

*Proof.* Each corner is a four-dimensional space of homomorphisms between two two-dimensional spaces; under the block copy it decomposes as the scalars plus the traceless part, $1+3$; the two singlets combine into the two-dimensional piece, which carries the two half-integer eigenvalues.

**Corollary.** The half-integer pair is the only place in the four readings where a label of the form $\tfrac12$ occurs as a piece, and it is not a carrier of the principal copy.

*Proof.* The table, and the carriers have integer labels.

**Corollary.** The module's label $\tfrac32$ occurs in none of the four lists: it is the label of the module and of the ideals, and not of a piece of the algebra.

*Proof.* The four lists have integer labels; the module has $\tfrac32$.

**The reading.** The half-integer appears in the block reading as a pair in a corner, in the principal reading not at all, and in the module always. The three occurrences are of different kinds.

## The Lesson

**Proposition.** The multiplicity of a label depends on the reading: $V_1$ occurs once in the principal reading, three times in the diagonal contents, and twice as a factor in the factorised list.

*Proof.* The table and the diagonal contents.

**Corollary.** The ambiguity is resolved only by naming the group; without the group the question "how many times does spin one occur" has three answers.

*Proof.* The proposition.

**Corollary.** The Clebsch–Gordan check $5+9+2=16$ confirms that the diagonal contents exhaust the algebra, and the principal check $7+5+3+1=16$ confirms the same for the principal list.

*Proof.* The two sums.

**The boundary.** The article treats the four readings of the two lists with diagonal contents; a finer analysis would need the Casimir of each group, which is not computed here.

## The Check of the Dimensions

**The reading by labels.** The label reading assigns to each carrier one term, of dimension the odd number attached to its label, and the four terms are the isotypic components of the algebra; the check is that the sum of the odd numbers is the square of the dimension of the module.

**The reading by blocks.** The block reading assigns the carriers to the four blocks of the copy, and the check is that each carrier contributes to exactly one block once the labels are grouped by parity; the two odd-dimensional carriers fill the two off-diagonal blocks and the two even ones fill the diagonal.

**The reading by real forms.** The real reading assigns to each carrier its real form, of dimension equal to the complex dimension, and the check is that the real dimensions of the carriers together with their imaginary parts exhaust the thirty-two real dimensions of the algebra.

## Summary

The table of spins against the four readings has spin $3$ as a piece in the principal reading only, spin $2$ as a piece there and as a diagonal content of the factorised reading, spin $1$ in three readings, the half-integer $\tfrac32$ on the module and the ideals only, and the half-integer pair in the corners of the block reading.

The diagonal contents of the factorised list are $V_2\oplus3V_1\oplus2V_0$, of dimensions $5+9+2=16$, checked against the Clebsch–Gordan rule for $(1,1)\cong V_2\oplus V_1\oplus V_0$; the principal list is $V_3\oplus V_2\oplus V_1\oplus V_0$, of dimensions $7+5+3+1=16$.

A label without a group has no multiplicity. The phrase "the spins of $M_4(\mathbb{C})$" is resolved only by naming the reading.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(1,0),(0,1),(1,1)$ | the pieces of the factorised reading |
| $V_k$ | the carrier of label $k$ |
| $(\tfrac12,\tfrac12)$ | the pair in the corners of the block reading |
| $5+9+2$ | the diagonal contents of the factorised list |

## Further Reading

- [The Four Carrier Lists of One Algebra at $n=4$](the-four-carrier-lists-of-one-algebra-at-n-4.html), for the four lists.
- [The $\mathrm{SU}(2)$ of $M_4(\mathbb{C})$ Acting on Sixteen Dimensions](the-su2-of-m4c-acting-on-sixteen-dimensions.html), for the action.
- [The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$](the-clebsch-gordan-decomposition-of-m4c.html), for the principal list.
- [Which Spin Lives in Which Reading](which-spin-lives-in-which-reading.html), for the row at order two.
- [The Spin Decomposition of $M_4(\mathbb{C})$](the-spin-decomposition-of-m4c.html), for the weights.
