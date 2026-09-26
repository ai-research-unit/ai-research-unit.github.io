# __Biquaternion Relations Between Subspaces__

## Introduction

The six distinguished subspaces of $\mathbb{B}$ are defined by the four involutions, but they are not independent objects: they intersect one another, they sum to subspaces of $\mathbb{B}$, they split the eight real coordinates into four **coordinate blocks**, and they are permuted and negated by the involutions. This article collects those relations in one place, after the six individual articles *Biquaternion Centre Subspace*, *Biquaternion Vector Subspace*, *Biquaternion Quaternion Subspace*, *Biquaternion Anti-Quaternion Subspace*, *Biquaternion Hermitian Subspace* and *Biquaternion Anti-Hermitian Subspace*, and before the structural article *Biquaternion Involution Lattice*, which treats the four involutions themselves.

Every number below — dimensions of intersections, of sums, and the entries of the tables — is derived here from the definitions by the comparison of coefficients, so the article doubles as the index of the six subspaces.

## The Three Decompositions

The three commuting involutions $\bar{\cdot}$, ${}^{*}$ and ${}^{\dagger}$ each split $\mathbb{B}$ into a fixed space and an anti-fixed space, and each split gives a direct-sum decomposition of the algebra into two of the distinguished subspaces:

| involution | fixed space | anti-fixed space | decomposition |
|---|---|---|---|
| $\bar{\cdot}$ | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$ |
| ${}^{*}$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$ |
| ${}^{\dagger}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ | $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ |

The fourth conjugation, the reversal $\flat = -\dagger$, has the same eigenspaces as $\dagger$ with the signs exchanged: its fixed space is $\mathbb{M}_-$ and its anti-fixed space is $\mathbb{M}_+$, so it produces no subspace beyond those of the table. The three decompositions are the **scalar–vector**, the **quaternion** and the **Hermitian** decomposition of the algebra, and every element has three readings, one per row.

## The Six Subspaces at a Glance

| subspace | defining condition | real basis | $\dim_{\mathbb{R}}$ | subalgebra | norm form |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\bar{\tilde{Q}} = \tilde{Q}$ | $e_0, ie_0$ | $2$ | yes, $\cong \mathbb{C}$ | $Q_0^2$, complex, real signature $(1,1)$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\bar{\tilde{Q}} = -\tilde{Q}$ | $e_1,e_2,e_3,ie_1,ie_2,ie_3$ | $6$ | no | $Q_1^2+Q_2^2+Q_3^2$, complex, real signature $(3,3)$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\tilde{Q}^{*} = \tilde{Q}$ | $e_0,e_1,e_2,e_3$ | $4$ | yes, $\cong \mathbb{H}$ | $q_0^2+q_1^2+q_2^2+q_3^2$, definite positive |
| $i\mathbb{H}_{\mathbb{B}}$ | $\tilde{Q}^{*} = -\tilde{Q}$ | $ie_0,ie_1,ie_2,ie_3$ | $4$ | no | $-\sum_\mu (q'_\mu)^2$, definite negative |
| $\mathbb{M}_+$ | $\tilde{Q}^{\dagger} = \tilde{Q}$ | $e_0,ie_1,ie_2,ie_3$ | $4$ | no, Jordan | $q_0^2 - |\mathbf{q}'|^2$, signature $(1,3)$ |
| $\mathbb{M}_-$ | $\tilde{Q}^{\flat} = \tilde{Q}$ | $ie_0,e_1,e_2,e_3$ | $4$ | no, Lie | $|\mathbf{q}|^2 - (q'_0)^2$, signature $(3,1)$ |

Only two of the six are closed under multiplication, and only one of the six is closed under the commutator as a Lie algebra and one under the symmetrized product as a Jordan algebra; the table names them in the last column's first words.

## The Four Coordinate Blocks

The eight real coordinates of $\mathbb{B}$ are $(q_0,q_1,q_2,q_3,q'_0,q'_1,q'_2,q'_3)$. They group into four real subspaces, each of dimension one or three, and each block is the simultaneous intersection of three of the six subspaces:

| block | basis | $\dim_{\mathbb{R}}$ | as an intersection |
|---|---|---|---|
| the real scalar line | $e_0$ | $1$ | $\mathbb{C}_{\mathbb{B}} \cap \mathbb{H}_{\mathbb{B}} = \mathbb{C}_{\mathbb{B}} \cap \mathbb{M}_+ = \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+$ |
| the real vector triple | $e_1,e_2,e_3$ | $3$ | $\mathrm{Vect}(\mathbb{B}) \cap \mathbb{H}_{\mathbb{B}} = \mathrm{Vect}(\mathbb{B}) \cap \mathbb{M}_- = \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$ |
| the imaginary vector triple | $ie_1,ie_2,ie_3$ | $3$ | $\mathrm{Vect}(\mathbb{B}) \cap i\mathbb{H}_{\mathbb{B}} = \mathrm{Vect}(\mathbb{B}) \cap \mathbb{M}_+ = i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+$ |
| the imaginary scalar line | $ie_0$ | $1$ | $\mathbb{C}_{\mathbb{B}} \cap i\mathbb{H}_{\mathbb{B}} = \mathbb{C}_{\mathbb{B}} \cap \mathbb{M}_- = i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$ |

The blocks are the building units of the whole article: each of the six subspaces is a sum of blocks,

$$
\mathbb{C}_{\mathbb{B}} = \langle e_0 \rangle \oplus \langle ie_0 \rangle , \qquad \mathrm{Vect}(\mathbb{B}) = \langle e_1,e_2,e_3\rangle \oplus \langle ie_1,ie_2,ie_3\rangle ,
$$

$$
\mathbb{H}_{\mathbb{B}} = \langle e_0 \rangle \oplus \langle e_1,e_2,e_3 \rangle , \qquad i\mathbb{H}_{\mathbb{B}} = \langle ie_0 \rangle \oplus \langle ie_1,ie_2,ie_3 \rangle ,
$$

$$
\mathbb{M}_+ = \langle e_0 \rangle \oplus \langle ie_1,ie_2,ie_3 \rangle , \qquad \mathbb{M}_- = \langle ie_0 \rangle \oplus \langle e_1,e_2,e_3 \rangle ,
$$

and every intersection in this article is a sum of blocks, which is why the dimension arithmetic below is so simple. The first row of the second table is the reason the two subspaces of a pair in the same row of the last table below meet in a block and not in the origin.

## The Intersections

The fifteen pairwise intersections, with the blocks of which they are made:

| | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
|---|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $2$ | $0$ | $1$ | $1$ | $1$ | $1$ |
| $\mathrm{Vect}(\mathbb{B})$ | $0$ | $6$ | $3$ | $3$ | $3$ | $3$ |
| $\mathbb{H}_{\mathbb{B}}$ | $1$ | $3$ | $4$ | $0$ | $1$ | $3$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $1$ | $3$ | $0$ | $4$ | $3$ | $1$ |
| $\mathbb{M}_+$ | $1$ | $3$ | $1$ | $3$ | $4$ | $0$ |
| $\mathbb{M}_-$ | $1$ | $3$ | $3$ | $1$ | $0$ | $4$ |

The diagonal carries the dimensions of the subspaces themselves. The entries are $0$, $1$ or $3$, and they are computed from the block decompositions: a subspace meets another in a block if the two share a block, in a sum of blocks if they share two, and in the origin if they share none. For instance $\mathbb{M}_+$ and $\mathbb{M}_-$ share no block and meet in the origin; $\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_-$ share the real vector triple and meet in it; $\mathbb{C}_{\mathbb{B}}$ and $\mathrm{Vect}(\mathbb{B})$ share no block, being the two members of a decomposition.

Three features of the table deserve to be isolated, because they are the relations that the individual articles use:

- the two members of a decomposition meet in the origin — the entries $0$ for the three pairs $(\mathbb{C}_{\mathbb{B}},\mathrm{Vect}(\mathbb{B}))$, $(\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}})$ and $(\mathbb{M}_+,\mathbb{M}_-)$;
- the centre meets each of the four remaining subspaces in one of the two scalar lines, $e_0$ for the quaternion and Hermitian cases and $ie_0$ for the anti-quaternion and anti-Hermitian ones;
- the vector subspace meets each of the four remaining subspaces in one of the two vector triples, real for the quaternion and anti-Hermitian cases and imaginary for the anti-quaternion and Hermitian ones.

## The Sums

The sums of the pairs, with the same ordering:

| | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
|---|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $2$ | $8$ | $5$ | $5$ | $5$ | $5$ |
| $\mathrm{Vect}(\mathbb{B})$ | $8$ | $6$ | $7$ | $7$ | $7$ | $7$ |
| $\mathbb{H}_{\mathbb{B}}$ | $5$ | $7$ | $4$ | $8$ | $7$ | $5$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $5$ | $7$ | $8$ | $4$ | $5$ | $7$ |
| $\mathbb{M}_+$ | $5$ | $7$ | $7$ | $5$ | $4$ | $8$ |
| $\mathbb{M}_-$ | $5$ | $7$ | $5$ | $7$ | $8$ | $4$ |

The dimension of a sum is the sum of the dimensions minus the dimension of the intersection, which is the arithmetic of the two previous tables. Exactly three pairs have sum $8$, that is, span the algebra: the three pairs of the decompositions. No other pair does. The pairs of dimension $7$ are the ones whose intersection is a vector triple, and the pairs of dimension $5$ the ones whose intersection is a scalar line.

## The Involutions as Sign Patterns

Each of the four involutions preserves each of the six subspaces, and its restriction to a subspace is diagonal in the displayed bases, with signs $+1$ and $-1$ only. The following table records the multiplicity of the sign $-1$ on each subspace, in the basis of the article of that subspace:

| involution | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
|---|---|---|---|---|---|---|
| $\bar{\cdot}$ | $0$ of $2$ | $6$ of $6$ | $3$ of $4$ | $3$ of $4$ | $3$ of $4$ | $3$ of $4$ |
| ${}^{*}$ | $1$ of $2$ | $3$ of $6$ | $0$ of $4$ | $4$ of $4$ | $3$ of $4$ | $1$ of $4$ |
| ${}^{\dagger}$ | $1$ of $2$ | $3$ of $6$ | $3$ of $4$ | $1$ of $4$ | $0$ of $4$ | $4$ of $4$ |
| $\flat$ | $1$ of $2$ | $3$ of $6$ | $1$ of $4$ | $3$ of $4$ | $4$ of $4$ | $0$ of $4$ |

The vanishing entries are the definitions: $\bar{\cdot}$ acts as the identity exactly on the centre, ${}^{*}$ exactly on the quaternion subspace, ${}^{\dagger}$ exactly on $\mathbb{M}_+$, and $\flat$ exactly on $\mathbb{M}_-$. The full multiplicities are the definitions of the complementary subspaces: $\bar{\cdot}$ acts as minus the identity exactly on the vector subspace, ${}^{*}$ as minus the identity exactly on $i\mathbb{H}_{\mathbb{B}}$, ${}^{\dagger}$ as minus the identity exactly on $\mathbb{M}_-$, and $\flat$ as minus the identity exactly on $\mathbb{M}_+$. The remaining entries are the mixed restrictions, which are neither the identity nor its negative.

Two consequences follow from the table alone. First, no subspace other than the centre is fixed pointwise by more than one of the four involutions, and the six subspaces are pairwise distinct as sets. Second, the composition rule $\dagger = {}^{*}\circ\bar{\cdot}$ is visible row by row: the coordinates negated by ${}^{\dagger}$ are exactly those negated by one of ${}^{*}$ and $\bar{\cdot}$ but not by both, so the multiplicities compose by symmetric difference. On the quaternion subspace, for instance, ${}^{*}$ negates none and $\bar{\cdot}$ negates the three vector units, so ${}^{\dagger}$ negates the same three and the multiplicity is $3$; on $\mathbb{M}_+$, ${}^{*}$ and $\bar{\cdot}$ negate the same three coordinates, and those cancel, leaving multiplicity $0$.

## How the Operations Act on the Splits

### The Central Imaginary Unit

Multiplication by $i$ preserves the centre and the vector subspace, exchanges the quaternion subspace with the anti-quaternion subspace, and exchanges the two sectors:

$$
i\,\mathbb{C}_{\mathbb{B}} = \mathbb{C}_{\mathbb{B}} , \qquad i\,\mathrm{Vect}(\mathbb{B}) = \mathrm{Vect}(\mathbb{B}) , \qquad i\,\mathbb{H}_{\mathbb{B}} = i\mathbb{H}_{\mathbb{B}} , \qquad i\,i\mathbb{H}_{\mathbb{B}} = \mathbb{H}_{\mathbb{B}} ,
$$

$$
i\,\mathbb{M}_+ = \mathbb{M}_- , \qquad i\,\mathbb{M}_- = \mathbb{M}_+ .
$$

The action is read off from the block table: $i$ preserves each block up to its complex structure, exchanging the real scalar line with the imaginary one and the real vector triple with the imaginary one, and the two stable subspaces $\mathbb{C}_{\mathbb{B}}$ and $\mathrm{Vect}(\mathbb{B})$ are exactly those made of a block and its image. The reader will recognize in this action, and in the two-fold repetition of the operator classes it produces, the reason the six subspaces fall into four classes under the conjugations of the algebra, as developed in *Biquaternion Operator Representation*.

### The Product and the Brackets

The following table records, for each pair of equal subspaces, where the product, the commutator and the symmetrized product of two of their elements fall:

| subspace | product | commutator | symmetrized product |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\mathbb{C}_{\mathbb{B}}$ | $0$ | $\mathbb{C}_{\mathbb{B}}$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$, with the scalar part $-(\mathbf{Q},\mathbf{R})$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{C}_{\mathbb{B}}$, namely $-(\mathbf{Q},\mathbf{R})e_0$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\mathbb{H}_{\mathbb{B}}$ | $\operatorname{span}\{e_1,e_2,e_3\}$ | $\mathbb{H}_{\mathbb{B}}$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{H}_{\mathbb{B}}$ | $\operatorname{span}\{e_1,e_2,e_3\}$ | $\mathbb{H}_{\mathbb{B}}$ |
| $\mathbb{M}_+$ | not contained; contains a real vector part $-\mathbf{q}'\times\mathbf{r}'$ | $\mathbb{M}_-$ | $\mathbb{M}_+$ |
| $\mathbb{M}_-$ | not contained; contains an imaginary vector part $i(q'_0\mathbf{r}+r'_0\mathbf{q})$ | $\mathbb{M}_-$ | $\mathbb{M}_+$ |

The table is the summary of the algebraic sections of the six subspace articles, and it explains the two structural identifications of the algebra: the vector subspace is a Lie algebra under the commutator, and the Hermitian and anti-Hermitian sectors are Jordan algebras under the symmetrized product, in each case with the sign pattern given by the table.

## The Matrix Picture

Under the isomorphism $\Phi : \mathbb{B} \to M_2(\mathbb{C})$ the six subspaces have the following images:

| subspace | image | matrix characterization |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | scalar matrices | $M = \lambda I$ |
| $\mathrm{Vect}(\mathbb{B})$ | traceless matrices | $\operatorname{Tr} M = 0$, that is $\mathfrak{sl}_2(\mathbb{C})$ |
| $\mathbb{H}_{\mathbb{B}}$ | matrices $\begin{pmatrix} z & w \\ -\bar{w} & \bar{z}\end{pmatrix}$ | $M_{21} = -\overline{M_{12}}$, $M_{22} = \overline{M_{11}}$ |
| $i\mathbb{H}_{\mathbb{B}}$ | matrices $\begin{pmatrix} u & v \\ \bar{v} & -\bar{u}\end{pmatrix}$ | $M_{21} = \overline{M_{12}}$, $M_{22} = -\overline{M_{11}}$ |
| $\mathbb{M}_+$ | Hermitian matrices | $M = M^{\dagger}$ |
| $\mathbb{M}_-$ | anti-Hermitian matrices | $M = -M^{\dagger}$ |

Three of the six images have a one-line characterization by an equation on the matrix: the centre by being scalar, the vector subspace by having zero trace, and the two sectors by the self-adjointness condition with a sign. The two middle rows are the coefficient conditions of the quaternion and anti-quaternion subspaces, which in the matrix picture become the two possible relations between the two entries of each row. The table also shows what the isomorphism preserves and what it does not: the decompositions of the algebra are read off from the trace and from the Hermitian decomposition, while the scalar–vector decomposition is the pair (scalar, traceless).

## Worked Verifications

### The Three Decompositions

Take the element $\tilde{Q} = (2+i)e_0 + 3e_1 + ie_2 - 4e_3$. Its three readings are:

$$
\tilde{Q} = \underbrace{(2+i)e_0}_{\mathbb{C}_{\mathbb{B}}} + \underbrace{3e_1 + ie_2 - 4e_3}_{\mathrm{Vect}(\mathbb{B})} , \qquad
\tilde{Q} = \underbrace{2e_0 + 3e_1 - 4e_3}_{\mathbb{H}_{\mathbb{B}}} + \underbrace{ie_0 + ie_2}_{i\mathbb{H}_{\mathbb{B}}} , \qquad
\tilde{Q} = \underbrace{2e_0 + ie_2}_{\mathbb{M}_+} + \underbrace{ie_0 + 3e_1 - 4e_3}_{\mathbb{M}_-} ,
$$

and the three decompositions sum to the same element, as they must, since each is a direct-sum decomposition of the same eight real coordinates.

### An Intersection of Dimension Three

The intersection $\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$ consists of the elements that are both real-coefficient and anti-Hermitian: from $Q_1,Q_2,Q_3$ real and equal to $q_k$, together with the anti-Hermitian condition that the vector coefficients are real and the scalar coefficient is imaginary, one gets $Q_0 = 0$; the intersection is the real vector triple $\operatorname{span}\{e_1,e_2,e_3\}$. The dimension $3$ is the entry of the table, and the element $e_1 + 2e_2$ is a concrete member.

### A Pair That Spans the Algebra

The pair $(\mathbb{M}_+,\mathbb{M}_-)$ has intersection zero and dimensions $4$ and $4$, so it spans: every element of $\mathbb{B}$ is the sum of a Hermitian and an anti-Hermitian part,

$$
\tilde{Q} = \frac{\tilde{Q} + \tilde{Q}^{\dagger}}{2} + \frac{\tilde{Q} - \tilde{Q}^{\dagger}}{2} ,
$$

and the two summands are unique because the intersection is the origin. The same computation with $\bar{\cdot}$ in place of $\dagger$ gives the scalar–vector decomposition and with ${}^{*}$ the quaternion decomposition; the three are the rows of the first table of the article.

### A Mixed Element and Its Blocks

For $\tilde{Q} = 3e_1 + ie_2$ the real part $3e_1$ lies in the real vector triple and the imaginary part $ie_2$ in the imaginary vector triple; the two scalar lines carry nothing. The element therefore lies in $\mathrm{Vect}(\mathbb{B})$, which is the sum of the two vector triples; its real vector part puts it in $\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$ and its imaginary vector part in $i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+$; and it lies in no other of the six subspaces, since both scalar lines are empty. Reading an element simultaneously in the three decompositions and in the four blocks is the content of the block table.

## Summary

The six distinguished subspaces of $\mathbb{B}$ are organized by three decompositions — scalar–vector, quaternion and Hermitian — whose two members meet in the origin. Their intersections are sums of the four coordinate blocks, the real and imaginary scalar lines and the real and imaginary vector triples, and therefore have dimension $0$, $1$ or $3$; the lattice of intersections is read off from the block membership of the subspaces, and exactly the three pairs of the decompositions sum to the whole algebra, the pairs sharing a vector triple summing to a subspace of dimension $7$ and the pairs sharing a scalar line to one of dimension $5$. Each of the four involutions preserves each subspace and acts on it diagonally with signs $+1$ and $-1$, the vanishing multiplicities of the sign $-1$ identifying the six subspaces one by one. Multiplication by the central imaginary unit preserves the centre and the vector subspace and exchanges the quaternion with the anti-quaternion subspace and the two sectors. Multiplication behaves differently on each subspace: the centre and the quaternion subspace are closed under it, the vector subspace produces a scalar part proportional to a dot product, the anti-quaternion subspace lands in the quaternion one, and the two sectors produce cross-product and symmetric terms outside themselves; the commutator closes on the vector subspace and maps the Hermitian sector into the anti-Hermitian one, while the symmetrized product closes on each sector and supplies the two Jordan algebra structures. In the matrix picture the six subspaces are the scalar, the traceless, the two quaternion-type patterns, and the Hermitian and anti-Hermitian matrices.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B})$ | the centre and vector subspaces |
| $\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+, \mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |
| $\langle \cdot \rangle$ | the real span of the listed elements |
| coordinate block | one of $\langle e_0\rangle$, $\langle e_1,e_2,e_3\rangle$, $\langle ie_1,ie_2,ie_3\rangle$, $\langle ie_0\rangle$ |
| $\bar{\cdot}, {}^{*}, {}^{\dagger}, \flat$ | quaternion, complex, Hermitian conjugation and reversal |
| $\mathbf{q} \times \mathbf{r}$, $(\mathbf{q},\mathbf{r})$ | the cross and dot products of vector coefficient triples |
| $\Phi$ | the isomorphism $\mathbb{B} \to M_2(\mathbb{C})$ |
| $\tilde{Q} \circ \tilde{R}$ | the symmetrized product |

## Further Reading

- *Biquaternion Centre Subspace* (`articles_maths/biquaternion-centre-subspace.md`)
- *Biquaternion Vector Subspace* (`articles_maths/biquaternion-vector-subspace.md`)
- *Biquaternion Quaternion Subspace* (`articles_maths/biquaternion-quaternion-subspace.md`)
- *Biquaternion Anti-Quaternion Subspace* (`articles_maths/biquaternion-anti-quaternion-subspace.md`)
- *Biquaternion Hermitian Subspace* (`articles_maths/biquaternion-hermitian-subspace.md`)
- *Biquaternion Anti-Hermitian Subspace* (`articles_maths/biquaternion-anti-hermitian-subspace.md`)
- *Biquaternion Involution Lattice* (`articles_maths/biquaternion-involution-lattice.md`), for the four involutions, their group structure and the two spaces each defines
- *Biquaternion Algebra* (`articles_maths/biquaternion-algebra.md`), for the algebra, its multiplication and its three decompositions in their original setting
- *Biquaternion 2×2 Matrix Representation* (`articles_maths/biquaternion-2x2-matrix-representation.md`), for the isomorphism $\Phi$ and the matrix images in detail
