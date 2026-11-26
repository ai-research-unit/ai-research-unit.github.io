# __The Four Carrier Lists of One Algebra at $n=4$__

## Introduction

**The subject.** Four different copies of $SU(2)$, or groups containing it, act on the same sixteen-dimensional algebra, and each gives its own list of irreducible pieces: $7+5+3+1$ for the principal copy, $1+15$ for $U(4)$, $1+3+3+9$ for the factorised copy and $8+3+3+2$ for the block copy. The article computes the four lists and draws the lesson: a label without a named group is meaningless.

**The order of the article.** The first section recalls the principal list. The second computes the $U(4)$ list and the commutant argument. The third computes the factorised list from the tensor product. The fourth computes the block list. The fifth assembles the table and draws the boundary.

**It assumes** *The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$* for the principal list and *The Spin Group at $n=4$* for the copy. The row at order two is *The Four Carrier Lists of One Algebra*.

**The result in one line.** The same sixteen dimensions carry the four decompositions $7+5+3+1$, $1+15$, $1+3+3+9$ and $8+3+3+2$, each belonging to its own group.

**Boundaries.** The article computes the four lists and identifies the group of each; it does not compute the Casimir of the three new groups, and it does not compare the lists element by element, which is *Two Numbers and Two Readings: $\tfrac32$ for the Module, $3$ for the Largest Carrier*.

## The Principal List

**Proposition.** The principal copy acts on the algebra with the four irreducible pieces $V_3,V_2,V_1,V_0$ of dimensions $7,5,3,1$.

*Proof.* The tensor square of $V_{3/2}$ decomposes into the four labels $0,\dots,3$, of dimensions $1,3,5,7$.

**Corollary.** The list is $7+5+3+1=16$, and the top label $3$ occurs.

*Proof.* The proposition.

**Corollary.** The principal list is the finest of the four, and the other three are coarser or differently grouped.

*Proof.* The comparison of the four lists in the table.

## The $U(4)$ List

**Proposition.** Under the conjugation action of $U(4)$ on $M_4(\mathbb{C})$, the algebra decomposes as $\mathbb{C}\mathrm I\oplus\mathfrak{sl}_4$, of dimensions $1+15$, and the traceless part is irreducible.

*Proof.* The trace is an invariant linear form, so the scalars are an invariant subspace and the traceless matrices a complementary one; the commutant of $U(4)$ in $\operatorname{End}(M_4)$ is spanned by the identity operator, by Schur's lemma, so the traceless part carries no proper invariant subspace.

**Corollary.** The $U(4)$ list is $1+15$, with a single carrier of dimension fifteen.

*Proof.* The proposition.

**Corollary.** The principal copy's four carriers are not $U(4)$-invariant: the principal copy is a three-dimensional subgroup, and its isotypic pieces are cut by a smaller group.

*Proof.* A $U(4)$-invariant subspace is a sum of the two pieces of the $U(4)$ list, of dimensions $1$ and $15$, and no principal carrier has dimension fifteen.

**The reading.** The commutant computation is what makes the traceless part irreducible: without it, the decomposition into the fifteen would be only a decomposition into the eigenspaces of the trace.

## The Factorised List

**Proposition.** Write $\mathbb{C}^{4}=\mathbb{C}^{2}\otimes\mathbb{C}^{2}$ and let $SU(2)\times SU(2)$ act factor by factor. Then $\operatorname{End}(\mathbb{C}^{4})\cong\operatorname{End}(\mathbb{C}^{2})\otimes\operatorname{End}(\mathbb{C}^{2})$, and the list is $1+3+3+9$.

*Proof.* $\operatorname{End}(\mathbb{C}^{2}\otimes\mathbb{C}^{2})\cong\operatorname{End}(\mathbb{C}^{2})\otimes\operatorname{End}(\mathbb{C}^{2})$, and $\operatorname{End}(\mathbb{C}^{2})$ decomposes under conjugation as the scalars and the traceless part, of dimensions $1$ and $3$. The tensor product of the two lists is $1\otimes1+1\otimes3+3\otimes1+3\otimes3=1+3+3+9$.

**Corollary.** The four pieces are the trivial, the two triplets and the nine-dimensional piece, and they sum to sixteen.

*Proof.* The proposition.

**Corollary.** The nine-dimensional piece is the tensor product of the two triplets, and it is irreducible under the product group.

*Proof.* A tensor product of irreducible modules for a product group is irreducible.

**The reading.** The factorised list is the tensor square of the list of $M_2(\mathbb{C})$, which is the reason the row at order two appears inside the row at order four.

## The Block List

**Proposition.** Write $\mathbb{C}^{4}=S_{+}\oplus S_{-}$ with $S_{\pm}$ of dimension two and let the copy act block-diagonally. Then the algebra decomposes into the two diagonal blocks, of dimension eight in total, and the two off-diagonal blocks, each of dimension four; each off-diagonal block splits further into a triplet and a singlet, and the two singlets form a two-dimensional piece. The list is $8+3+3+2$.

*Proof.* $\operatorname{End}(S_{+}\oplus S_{-})$ consists of the two diagonal blocks $\operatorname{End}(S_{\pm})$, of dimensions $4+4$, and the two off-diagonal blocks $\operatorname{Hom}(S_{\mp},S_{\pm})$, of dimensions $4+4$. Each four-dimensional block splits as the scalars plus the traceless part, of dimensions $1+3$, and the two singlets from the corners combine into the two-dimensional piece. The total is $8+3+3+2=16$.

**Corollary.** The block list is the coarsest in the sense that its largest piece has dimension eight, and its smallest has dimension two.

*Proof.* The list displayed.

**Corollary.** The two-dimensional piece is the only piece of even dimension in the four lists, and it is not a carrier of the principal copy.

*Proof.* The other lists have dimensions $7,5,3,1$; $1,15$; $1,3,3,9$; $8,3,3,2$.

**The reading.** The pair in the block list is the place where a half-integer label appears: the two singlets of the corners carry the pair $(\tfrac12,\tfrac12)$.

## The Table and the Lesson

**Proposition.** The four lists are

| group | list | total |
|---|---|---|
| principal $SU(2)$ | $7+5+3+1$ | $16$ |
| $U(4)$ | $1+15$ | $16$ |
| factorised $SU(2)\times SU(2)$ | $1+3+3+9$ | $16$ |
| block $SU(2)$ | $8+3+3+2$ | $16$ |

and each decomposition belongs to its own group.

*Proof.* The four propositions.

**Corollary.** The same sixteen dimensions carry four different decompositions, and the number of pieces is four, two, four and four.

*Proof.* The table.

**Corollary.** A phrase such as "the spin-two part of $M_4$" has no meaning without naming the group: the label $2$ occurs in the principal list and, as a diagonal content, in the factorised list, and in no other.

*Proof.* The comparison of the lists and the diagonal contents of the next article.

**The boundary.** The article gives the four lists and their groups. The identification of each spin in each reading, and the diagonal contents of the factorised and block lists, is the subject of *Two Numbers and Two Readings: $\tfrac32$ for the Module, $3$ for the Largest Carrier*.

## The Four Readings in Detail

**The list of labels.** The first reading is the list of the carrier labels, $7+5+3+1$, ordered by the label; it is the decomposition into isotypic components, and it is the finest invariant decomposition of the algebra as a module for the copy.

**The list of the trace.** The second reading separates the trace from the traceless part, $1+15$; it is the decomposition under the projection onto the centre, and it is the only reading in which one summand is a two-sided ideal.

**The list of the factors.** The third reading, $1+3+3+9$, belongs to the factorised copy on $\mathbb{C}^{2}\otimes\mathbb{C}^{2}$: it is the tensor product $1\otimes1+1\otimes3+3\otimes1+3\otimes3$ of the two scalar-plus-traceless lists, so the nine is the product of the two triplets and not a summand of the principal list.

**The list of the blocks.** The fourth reading, $8+3+3+2$, belongs to the block copy on $S_{+}\oplus S_{-}$: the two diagonal blocks give eight dimensions, each off-diagonal block splits as a triplet and a singlet, and the two singlets combine into the two-dimensional piece.

**The reading.** The four lists are the same sixteen dimensions sorted by four different structures, and each of them answers a different question about the algebra.

## Summary

Four groups act on the same algebra and give four decompositions of the same sixteen dimensions: the principal copy gives $7+5+3+1$; $U(4)$ gives $1+15$, with the traceless part irreducible by the commutant computation; the factorised copy on $\mathbb{C}^{2}\otimes\mathbb{C}^{2}$ gives $1+3+3+9$ from the tensor product of two $1+3$ lists; and the block copy gives $8+3+3+2$, with the two singlets of the corners forming the pair.

Each list is a decomposition of sixteen, and the four lists are different. A label without a named group is meaningless, and the phrase "the spins of $M_4(\mathbb{C})$" must be completed by the group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| principal list | $7+5+3+1$ |
| $U(4)$ list | $1+15$ |
| factorised list | $1+3+3+9$ |
| block list | $8+3+3+2$ |
| commutant | the algebra of operators commuting with the group |

## Further Reading

- [Spins $3$ to $\tfrac32$ by Reading at $n=4$: Principal and Factorised Lists](spins-by-reading-at-n-4.html), for the table of spins.
- [The $\mathrm{SU}(2)$ of $M_4(\mathbb{C})$ Acting on Sixteen Dimensions](the-su2-of-m4c-acting-on-sixteen-dimensions.html), for the action itself.
- [The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$](the-clebsch-gordan-decomposition-of-m4c.html), for the principal list.
- [The Four Carrier Lists of One Algebra](the-four-carrier-lists-of-one-algebra.html), for the row at order two.
- [The Truncated Rule: the Product of Two Carriers Is Not a Carrier](the-truncated-rule-the-product-of-two-carriers-at-n-4.html), for the products.
