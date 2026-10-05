# __Comparison of the Six Subspaces__

## Introduction

The six distinguished subspaces of $\mathbb{B}$ — the centre, the vector subspace, the quaternion and anti-quaternion subspaces, and the Hermitian and anti-Hermitian subspaces — are defined and tabulated one by one in *Introduction to the Six Subspaces*. They are not independent objects: they intersect, they sum to subspaces of $\mathbb{B}$ larger than themselves, they are built from four common pieces, and the four conjugations act on each of them by signs.

This article collects those relations in one place. Every number below is derived from the definitions by the comparison of coefficients, so the article doubles as the index of the six. Its tool is the four coordinate blocks, which are the pieces into which the eight real coordinates of $\mathbb{B}$ group and of which every one of the six is a sum.

The frame is the three decompositions of the algebra, established in *Decompositions Along the Six Subspaces*:

| involution | fixed space | anti-fixed space | decomposition |
|---|---|---|---|
| quaternion conjugation ${}^{\natural}$ | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$ |
| complex conjugation $\bar{\cdot}$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$ |
| Hermitian conjugation ${}^{*}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ | $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ |

The reversal $\flat = -{}^{*}$ gives no fourth decomposition: its two spaces are those of ${}^{*}$ in the other order. The three decompositions are the scalar–vector, the quaternion and the Hermitian decomposition of $\mathbb{B}$, and their three pairs are the only pairs of distinct subspaces that meet in the origin.

## The Six Subspaces and the Coordinate Blocks

The relations between the six subspaces are read off from four subspaces of $\mathbb{B}$, the **coordinate blocks**, into which the eight real coordinates group.

**Definition.** The **coordinate blocks** are the four real subspaces

$$
A_1 = \mathbb{R}e_0 , \qquad A_2 = \mathbb{R}(ie_0) , \qquad
B_1 = \operatorname{span}_{\mathbb{R}}\{e_1, e_2, e_3\} , \qquad B_2 = \operatorname{span}_{\mathbb{R}}\{ie_1, ie_2, ie_3\} ,
$$

the two **scalar blocks** $A_1, A_2$ of dimension $1$ and the two **vector blocks** $B_1, B_2$ of dimension $3$. They are the pieces into which the eight real coordinates of $\mathbb{B}$ group: the two scalar blocks carry the two real coordinates of the scalar coefficient $Q_0$, and the two vector blocks the six real coordinates of the vector part.

Each block is the intersection of the three subspaces that contain it:

| block | basis | $\dim_{\mathbb{R}}$ | it is the intersection |
|---|---|---|---|
| $A_1$ | $e_0$ | $1$ | $\mathbb{C}_{\mathbb{B}} \cap \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+$ |
| $A_2$ | $ie_0$ | $1$ | $\mathbb{C}_{\mathbb{B}} \cap i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$ |
| $B_1$ | $e_1, e_2, e_3$ | $3$ | $\mathrm{Vect}(\mathbb{B}) \cap \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$ |
| $B_2$ | $ie_1, ie_2, ie_3$ | $3$ | $\mathrm{Vect}(\mathbb{B}) \cap i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+$ |

**Theorem.** Each of the six subspaces is the sum of two blocks:

| subspace | blocks | $\dim_{\mathbb{R}}$ |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $A_1 \oplus A_2$ | $2$ |
| $\mathrm{Vect}(\mathbb{B})$ | $B_1 \oplus B_2$ | $6$ |
| $\mathbb{H}_{\mathbb{B}}$ | $A_1 \oplus B_1$ | $4$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $A_2 \oplus B_2$ | $4$ |
| $\mathbb{M}_+$ | $A_1 \oplus B_2$ | $4$ |
| $\mathbb{M}_-$ | $A_2 \oplus B_1$ | $4$ |

**Proof.** Each subspace is defined by conditions on the real coordinates: the centre by the vanishing of the six vector coordinates, the vector subspace by the vanishing of the two scalar ones, the quaternion subspace by the vanishing of the three imaginary parts of the vector coordinates and of the imaginary part of the scalar one, and the other three by the corresponding sign choices. Reading the conditions block by block gives the table.

The pattern of the table is the reason the six subspaces are neither more nor fewer than six. Each of the four four-dimensional subspaces takes **one scalar block and one vector block**, and there are exactly four ways of choosing one block from each of the two pairs; the centre takes both scalar blocks and the vector subspace both vector blocks. The three decompositions are exactly the three ways of splitting the four blocks into two complementary pairs: $\{A_1, B_1\}$ against $\{A_2, B_2\}$ gives the quaternion decomposition, $\{A_1, B_2\}$ against $\{A_2, B_1\}$ gives the Hermitian one, and $\{A_1, A_2\}$ against $\{B_1, B_2\}$ gives the scalar–vector one. A four-element set has exactly three pairings into two pairs, which is why there are exactly three decompositions and no fourth.

## The Intersections

**Theorem.** Two distinct subspaces of the six meet in the blocks they have in common; consequently the dimension of their intersection is $0$, $1$ or $3$, and never $2$, $4$, $5$ or $6$.

**Proof.** Each subspace is a sum of two blocks, and two of them share either no block, one scalar block, or one vector block. Sharing no block gives intersection $\{0\}$ and dimension $0$; sharing one scalar block gives dimension $1$; sharing one vector block gives dimension $3$. Two distinct subspaces cannot share two blocks, since two blocks determine a subspace of the list.

The fifteen dimensions, the diagonal carrying the dimensions of the subspaces themselves:

| | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
|---|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $2$ | $0$ | $1$ | $1$ | $1$ | $1$ |
| $\mathrm{Vect}(\mathbb{B})$ | $0$ | $6$ | $3$ | $3$ | $3$ | $3$ |
| $\mathbb{H}_{\mathbb{B}}$ | $1$ | $3$ | $4$ | $0$ | $1$ | $3$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $1$ | $3$ | $0$ | $4$ | $3$ | $1$ |
| $\mathbb{M}_+$ | $1$ | $3$ | $1$ | $3$ | $4$ | $0$ |
| $\mathbb{M}_-$ | $1$ | $3$ | $3$ | $1$ | $0$ | $4$ |

Three features of the table are used again and again in the thematic articles.

- The two members of a decomposition meet in the origin. The entries $0$ are exactly the three pairs $(\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B}))$, $(\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}})$ and $(\mathbb{M}_+, \mathbb{M}_-)$, and no other pair meets in the origin.
- The centre meets each of the other four subspaces in a scalar line: $A_1 = \mathbb{R}e_0$ with the quaternion and Hermitian subspaces, $A_2 = \mathbb{R}(ie_0)$ with the anti-quaternion and anti-Hermitian ones.
- The vector subspace meets each of the other four in a vector triple: $B_1$ with the quaternion and anti-Hermitian subspaces, $B_2$ with the anti-quaternion and Hermitian ones.

In particular, no two of the six subspaces are equal, since equal subspaces would meet in their common dimension, and no off-diagonal entry of the table is $2$, $4$ or $6$.

## The Sums

The dimension of a sum is the sum of the dimensions minus the dimension of the intersection, which is the arithmetic of the two tables above:

| | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
|---|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $2$ | $8$ | $5$ | $5$ | $5$ | $5$ |
| $\mathrm{Vect}(\mathbb{B})$ | $8$ | $6$ | $7$ | $7$ | $7$ | $7$ |
| $\mathbb{H}_{\mathbb{B}}$ | $5$ | $7$ | $4$ | $8$ | $7$ | $5$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $5$ | $7$ | $8$ | $4$ | $5$ | $7$ |
| $\mathbb{M}_+$ | $5$ | $7$ | $7$ | $5$ | $4$ | $8$ |
| $\mathbb{M}_-$ | $5$ | $7$ | $5$ | $7$ | $8$ | $4$ |

Exactly three pairs have sum $8$, that is, span the whole algebra, and they are the three complementary pairs of the three decompositions. Every other pair spans a proper subspace: the pairs whose intersection is a vector triple have sum $7$, and the pairs whose intersection is a scalar line have sum $5$. A reader who wants to write an element of $\mathbb{B}$ as the sum of one element of each of two prescribed subspaces therefore has exactly three pairs to choose from, and cannot do it with any other pair.

## The Lattice of the Fixed Spaces

The three decompositions of the frame table come from the three involutions ${}^{\natural}$, $\bar{\cdot}$ and ${}^{*}$. Including the reversal $\flat=-{}^{*}$ gives four involutions and, for each, a fixed and an anti-fixed space; the reversal has the same two eigenspaces as ${}^{*}$ with the signs exchanged, so eight labelled spaces reduce to the six subspaces.

| involution | fixed space | anti-fixed space | generated by |
|---|---|---|---|
| ${}^{\natural}$ | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}(\mathbb{B})$ | the complex structure and the vector structure |
| $\bar{\cdot}$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | the real structure |
| ${}^{*}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ | the Hermitian structure |
| $\flat$ | $\mathbb{M}_-$ | $\mathbb{M}_+$ | the reversal |

Only the Hermitian pair is counted twice, since $\{\tilde Q:\tilde Q^{\flat}=\tilde Q\}=\mathbb{M}_-$ and $\{\tilde Q:\tilde Q^{\flat}=-\tilde Q\}=\mathbb{M}_+$ are the eigenvalue equations of ${}^{*}$ read with the opposite labels.

Over the coordinate blocks the subspaces sit at the following levels of dimension, a line joining a subspace to the minimal ones containing it in the diagram of the article:

| level | subspaces |
|---|---|
| $\mathbb{B}$ | the whole algebra, dimension $8$ |
| the sums | $\mathbb{C}_{\mathbb{B}}+\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}+i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_++\mathbb{M}_-$ — all equal to $\mathbb{B}$ |
| the four-dimensional spaces | $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ |
| the three-dimensional triples | $\langle e_1,e_2,e_3\rangle=\mathrm{Vect}\cap\mathbb{H}_{\mathbb{B}}$, $\langle ie_1,ie_2,ie_3\rangle=\mathrm{Vect}\cap\mathbb{M}_+$ |
| the two-dimensional centre | $\mathbb{C}_{\mathbb{B}}=\langle e_0\rangle\oplus\langle ie_0\rangle$ |
| the one-dimensional lines | $\langle e_0\rangle$, $\langle ie_0\rangle$ |
| the origin | $0$ |

The object is not a chain, and it is not closed under sum, being the union of the three decompositions of $\mathbb{B}$ rather than a single distributive lattice: the intersections of §*The Intersections* are its meets, and the sums of §*The Sums* are its joins wherever the sum does not reach the top. Its skeleton is the block table, that is, the three decompositions of the four coordinate blocks, and the levels record how the six subspaces sit over those blocks.

## Worked Examples

**An element and its blocks.** Take $\tilde{Q} = 3e_1 + ie_2$. Its real part $3e_1$ lies in the real vector block $B_1$ and its imaginary part $ie_2$ in the imaginary vector block $B_2$, while both scalar blocks carry nothing. Every subspace containing $\tilde{Q}$ must then contain both $B_1$ and $B_2$, and the only sum of two blocks that does so is $\mathrm{Vect}(\mathbb{B}) = B_1 \oplus B_2$: the element lies in the vector subspace and in none of the other five. Its two parts lie in the two three-dimensional intersections $B_1 = \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$ and $B_2 = i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+$, which is the block reading of the entries $3$ of the intersection table.

**An intersection of dimension three.** The quaternion subspace is $A_1 \oplus B_1$ and the anti-Hermitian subspace is $A_2 \oplus B_1$, so they share the single block $B_1$ and meet in it:

$$
\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_- = B_1 = \operatorname{span}_{\mathbb{R}}\{e_1, e_2, e_3\}, \qquad \dim_{\mathbb{R}} = 3 .
$$

The same answer follows from the defining conditions: an element of $\mathbb{H}_{\mathbb{B}}$ has real coefficients, and an element of $\mathbb{M}_-$ has a purely imaginary scalar coefficient and real vector coefficients, so the scalar coefficient must vanish and the element is a real vector. The element $e_1 + 2e_2$ is a concrete member, and $3$ is the entry of this pair in the intersection table.

## The Involutions as Sign Patterns

Each of the four conjugations preserves each of the six subspaces, since it commutes with the three commuting involutions that define them, and its restriction to a subspace is diagonal in the real basis of that subspace with eigenvalues $+1$ and $-1$ only. The following table records, for each conjugation and each subspace, the multiplicity of the eigenvalue $-1$, written as a fraction of the dimension.

| conjugation | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
|---|---|---|---|---|---|---|
| ${}^{\natural}$ | $0$ of $2$ | $6$ of $6$ | $3$ of $4$ | $3$ of $4$ | $3$ of $4$ | $3$ of $4$ |
| $\bar{\cdot}$ | $1$ of $2$ | $3$ of $6$ | $0$ of $4$ | $4$ of $4$ | $3$ of $4$ | $1$ of $4$ |
| ${}^{*}$ | $1$ of $2$ | $3$ of $6$ | $3$ of $4$ | $1$ of $4$ | $0$ of $4$ | $4$ of $4$ |
| $\flat$ | $1$ of $2$ | $3$ of $6$ | $1$ of $4$ | $3$ of $4$ | $4$ of $4$ | $0$ of $4$ |

The eight vanishing cells are the definitions of the six subspaces read back: ${}^{\natural}$ acts as the identity exactly on the centre and as its negative exactly on the vector subspace; $\bar{\cdot}$ exactly on the quaternion subspace and its negative exactly on the anti-quaternion one; ${}^{*}$ exactly on $\mathbb{M}_+$ and its negative exactly on $\mathbb{M}_-$; and $\flat$ exactly on $\mathbb{M}_-$ and its negative exactly on $\mathbb{M}_+$. The mixed cells, which are neither $0$ nor the full dimension, are the restrictions that are neither the identity nor its negative; each of them is fixed by the block membership of the subspace, since a conjugation negates a block as a whole.

The table also exhibits the composition rule ${}^{*} = \bar{\cdot}\circ{}^{\natural}$. The coordinates negated by ${}^{*}$ are exactly those negated by one of $\bar{\cdot}$ and ${}^{\natural}$ but not by both, so the multiplicities compose by symmetric difference. On the quaternion subspace, for instance, $\bar{\cdot}$ negates none of the four coordinates and ${}^{\natural}$ negates the three vector ones, so ${}^{*}$ negates the same three and the multiplicity is $3$; on $\mathbb{M}_+$, $\bar{\cdot}$ and ${}^{\natural}$ negate the same three coordinates, and those cancel, leaving multiplicity $0$.

Two consequences follow from the table alone. First, no subspace other than the centre is fixed pointwise by more than one of the four conjugations, and the six subspaces are pairwise distinct as sets. Second, a subspace is fixed pointwise by exactly those conjugations whose multiplicity of $-1$ on it vanishes.

## The Complex Structure and the Six Subspaces

The scalar imaginary $i$ gives the real-linear map $J : \tilde{Q} \mapsto i\tilde{Q}$ with $J^2 = -\mathrm{id}$, the complex structure carried by every complex vector space, defined for $\mathbb{B}$ in *Biquaternions as a Vector Space over $\mathbb{C}$*. It is not one of the four conjugations, and its action on the six subspaces is read directly from the block table; no product is invoked. Since $i(q + iq') = -q' + iq$ on the coefficients, $J$ exchanges the two scalar blocks and the two vector blocks:

$$
J(A_1) = A_2, \qquad J(A_2) = A_1, \qquad J(B_1) = B_2, \qquad J(B_2) = B_1.
$$

A subspace made of a block together with its image is therefore stable, and a subspace made of the images of the blocks of another is exchanged with it:

$$
J(\mathbb{C}_{\mathbb{B}}) = \mathbb{C}_{\mathbb{B}}, \qquad J(\mathrm{Vect}(\mathbb{B})) = \mathrm{Vect}(\mathbb{B}), \qquad J(\mathbb{H}_{\mathbb{B}}) = i\mathbb{H}_{\mathbb{B}}, \qquad J(i\mathbb{H}_{\mathbb{B}}) = \mathbb{H}_{\mathbb{B}},
$$

$$
J(\mathbb{M}_+) = \mathbb{M}_-, \qquad J(\mathbb{M}_-) = \mathbb{M}_+.
$$

The centre and the vector subspace are stable, the quaternion subspace is carried onto the anti-quaternion subspace and conversely, and the Hermitian subspace onto the anti-Hermitian one and conversely. The contrast with the conjugations is the point: each of the four preserves each of the six subspaces, whereas $J$ pairs them, exchanging $\mathbb{H}_{\mathbb{B}}$ with $i\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_+$ with $\mathbb{M}_-$ and leaving the other two alone. Under the group generated by the four conjugations together with $J$, the six subspaces therefore fall into four classes: the centre, the vector subspace, and the two exchanged pairs. It is the complex structure, and not quaternion conjugation, that makes the pairs, and it is a fact about the linear space alone.

## Summary

The six distinguished subspaces of $\mathbb{B}$ are organized by the four coordinate blocks $A_1 = \mathbb{R}e_0$, $A_2 = \mathbb{R}(ie_0)$, $B_1 = \operatorname{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ and $B_2 = \operatorname{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$, each of which is the intersection of the three subspaces containing it. Every one of the six is a sum of two blocks: the centre of the two scalar blocks, the vector subspace of the two vector blocks, and each of the four four-dimensional subspaces of one scalar and one vector block, the four ways of choosing the pair being the four such subspaces. The three decompositions of the algebra are the three pairings of the four blocks into two complementary pairs, which is why there are exactly three. The four involutions, the reversal included, give a fixed space and an anti-fixed space each; the eight labelled spaces reduce to the six, the Hermitian pair being counted twice, and they sit over the four blocks in the lattice of the fixed spaces, which is not a chain and not closed under sum. Two distinct subspaces meet in the blocks they share, so the fifteen pairwise intersections have dimension $0$, $1$ or $3$: the members of a decomposition meet in the origin, the centre meets each other subspace in a scalar line, and the vector subspace in a vector triple. Exactly the three pairs of the decompositions sum to the whole algebra; the pairs sharing a vector triple sum to a subspace of dimension $7$, and those sharing a scalar line to one of dimension $5$. Two worked examples make the block arithmetic concrete: the element $3e_1 + ie_2$ lies in $\mathrm{Vect}(\mathbb{B})$ alone, and $\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$ is the single block $B_1$. Each of the four conjugations preserves each subspace and acts on it diagonally with signs $+1$ and $-1$, the vanishing multiplicities of $-1$ identifying the subspaces fixed by each conjugation and the table of multiplicities exhibiting the composition ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ as a symmetric difference. The complex structure $J : \tilde{Q} \mapsto i\tilde{Q}$ preserves the centre and the vector subspace and exchanges the other two pairs; none of the four conjugations does this, each of them preserving every one of the six.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B})$ | the centre and the vector subspace |
| $\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+, \mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |
| ${}^{\natural}, \bar{\cdot}, {}^{*}, \flat$ | quaternion, complex, Hermitian conjugation and reversal |
| $A_1, A_2$ | the scalar blocks $\mathbb{R}e_0$ and $\mathbb{R}(ie_0)$ |
| $B_1, B_2$ | the vector blocks $\operatorname{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ and $\operatorname{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$ |
| $\oplus$ | direct sum of real subspaces |
| $J$ | the complex structure $J : \tilde{Q} \mapsto i\tilde{Q}$, $J^2 = -\mathrm{id}$, exchanging the scalar blocks and the vector blocks |
| fixed space, anti-fixed space | the elements fixed, or negated, by an involution |
| lattice of the fixed spaces | the six subspaces under inclusion, the intersections as meets and the sums as joins |

## Further Reading

- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six subspaces themselves, one to a section
- *Decompositions Along the Six Subspaces* (`articles_maths/decompositions-along-the-six-subspaces.md`), for the three decompositions and the projection formulas
- *Biquaternions as a Vector Space over $\mathbb{C}$* (`articles_maths/biquaternions-as-a-vector-space-over-c.md`), for the algebra, its basis, its conjugations and its coordinate systems
- *The Group of Involutions* (`articles_maths/the-group-of-involutions.md`), for the four conjugations as an abstract group and the two spaces each defines
- *The Six Subspaces and the Four Complex Products* (`articles_maths/the-six-subspaces-and-the-four-complex-products.md`), for what the six give when the product is brought in, which is not part of this article
- *The Clifford Structure of the Biquaternion Algebra* (`articles_maths/biquaternion-clifford-structure.md`), for the grading of the algebra and the four grades
