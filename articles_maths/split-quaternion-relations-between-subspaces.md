
# __Split-Quaternion Relations Between Subspaces__

## Introduction

The four distinguished subspaces of $\mathbb{H}_{\mathrm{s}}$ — the scalar line $S$, the vector subspace $V$ and the two split-complex planes $\mathbb{D}_2, \mathbb{D}_3$ — are defined by different conditions, but they are not independent: they contain one another, they intersect, they sum to subspaces of $\mathbb{H}_{\mathrm{s}}$, and they are cut out of the four real coordinates by the involutions. This article collects those relations in one place, after the individual articles *Split-Quaternion Scalar and Vector Subspaces* and *Split-Quaternion Split-Complex Subspaces*, and before the structural article *Split-Quaternion Involution Lattice*, which treats the involutions themselves.

Every number below — dimensions of intersections, of sums, and the entries of the tables — is derived from the definitions by comparison of coefficients, so the article doubles as an index of the four subspaces and of the coordinate blocks.

**Conventions.** The algebra is $\mathbb{H}_{\mathrm{s}}$, with basis $1, e_1, e_2, e_3$, the relations $e_1^2 = -1$, $e_2^2 = e_3^2 = +1$, $e_3 = e_1 e_2$, $e_1 e_2 = -e_2 e_1$, and a general element $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$. The conjugation ${}^{\natural}$, the principal involution $\alpha$ and the reversal $\rho$ are as in *Split-Quaternion Subspaces and the Involutions*, and $N$, $B$ are the split-quaternion norm and its polarisation.

## The Three Decompositions

Two of the three involutions split $\mathbb{H}_{\mathrm{s}}$ into distinguished subspaces, and the third splits it into two further subspaces:

| involution | fixed space | anti-fixed space | decomposition |
|---|---|---|---|
| ${}^{\natural}$ | $S = \mathbb{R}\cdot 1$ | $V = \operatorname{span}\{e_1,e_2,e_3\}$ | $\mathbb{H}_{\mathrm{s}} = S \oplus V$ |
| $\alpha$ | $\mathbb{D}_3 = \operatorname{span}\{1,e_3\}$ | $\operatorname{span}\{e_1,e_2\}$ | $\mathbb{H}_{\mathrm{s}} = \mathbb{D}_3 \oplus \operatorname{span}\{e_1,e_2\}$ |
| $\rho$ | $\operatorname{span}\{1,e_1,e_2\}$ | $\mathbb{R} e_3$ | $\mathbb{H}_{\mathrm{s}} = \operatorname{span}\{1,e_1,e_2\} \oplus \mathbb{R} e_3$ |

The three decompositions are the **scalar–vector** decomposition, and the two decompositions associated with the principal involution and the reversal. Every element has three readings, one per row. The finest common refinement of the three is the coordinate-block decomposition of the next section.

## The Four Subspaces at a Glance

| subspace | defining condition | real basis | $\dim_{\mathbb{R}}$ | subalgebra | norm |
|---|---|---|---|---|---|
| $S$ | $\tilde{q}^{\natural} = \tilde q$ | $1$ | $1$ | yes, $\cong \mathbb{R}$ | $q_0^2$, positive definite |
| $V$ | $\tilde{q}^{\natural} = -\tilde q$ | $e_1,e_2,e_3$ | $3$ | no (Lie) | $q_1^2-q_2^2-q_3^2$, signature $(2,1)$ |
| $\mathbb{D}_2$ | closed under products of $1, e_2$ | $1,e_2$ | $2$ | yes, $\cong \mathbb{D}$ | $q_0^2-q_2^2$, signature $(1,1)$ |
| $\mathbb{D}_3$ | $\alpha(\tilde q) = \tilde q$ | $1,e_3$ | $2$ | yes, $\cong \mathbb{D}$ | $q_0^2-q_3^2$, signature $(1,1)$ |

Only three of the four are closed under multiplication: the scalar line and the two split-complex planes. The vector subspace is not a subalgebra but is closed under the commutator, and it is the only one of the four that carries a nonzero bracket — the other three are commutative. The norms are the restrictions of $N$; all four are non-degenerate, the first definite and the other three indefinite.

## The Four Coordinate Blocks

The four real coordinates of a split-quaternion are $(q_0,q_1,q_2,q_3)$ in the basis $1, e_1, e_2, e_3$. They group into four one-dimensional **coordinate blocks**,

$$
\mathbb{H}_{\mathrm{s}} = \langle 1 \rangle \oplus \langle e_1 \rangle \oplus \langle e_2 \rangle \oplus \langle e_3 \rangle,
$$

where $\langle \cdot\rangle$ denotes the real span of the displayed elements. Each of the blocks $\langle 1\rangle$, $\langle e_2\rangle$ and $\langle e_3\rangle$ is the intersection of the distinguished subspaces containing it, and $\langle e_1\rangle$ is the complement of $\mathbb{D}_2 + \mathbb{D}_3$ in $\mathbb{H}_{\mathrm{s}}$; each of the four distinguished subspaces is a sum of blocks:

$$
S = \langle 1 \rangle, \qquad V = \langle e_1 \rangle \oplus \langle e_2 \rangle \oplus \langle e_3 \rangle,
$$

$$
\mathbb{D}_2 = \langle 1 \rangle \oplus \langle e_2 \rangle, \qquad \mathbb{D}_3 = \langle 1 \rangle \oplus \langle e_3 \rangle .
$$

The blocks are the building units of the article: every intersection below is a sum of blocks, which is why the dimension arithmetic is so simple.

## The Intersections

The ten pairwise intersections of the four subspaces, with the dimensions (the diagonal carries the dimensions of the subspaces themselves):

| | $S$ | $V$ | $\mathbb{D}_2$ | $\mathbb{D}_3$ |
|---|---|---|---|---|
| $S$ | $1$ | $0$ | $1$ | $1$ |
| $V$ | $0$ | $3$ | $1$ | $1$ |
| $\mathbb{D}_2$ | $1$ | $1$ | $2$ | $1$ |
| $\mathbb{D}_3$ | $1$ | $1$ | $1$ | $2$ |

Explicitly,

$$
S \cap V = \{0\}, \quad S \cap \mathbb{D}_2 = S, \quad S \cap \mathbb{D}_3 = S, \quad V \cap \mathbb{D}_2 = \mathbb{R} e_2,
$$

$$
V \cap \mathbb{D}_3 = \mathbb{R} e_3, \quad \mathbb{D}_2 \cap \mathbb{D}_3 = S .
$$

Three features are worth isolating:

- The scalar line is contained in both split-complex planes, so it meets them in dimension $1$; it meets the vector subspace only in the origin, being the complement of $V$ in the scalar–vector decomposition.
- The vector subspace meets each split-complex plane in a single line, spanned by the common basis element $e_2$ or $e_3$, and the two planes meet each other in the scalar line.
- No two of the four subspaces are equal, and no pair except the obvious containment pairs is nested: $S \subset \mathbb{D}_2$, $S \subset \mathbb{D}_3$, and $S \subset S \oplus V$ but $S \not\subseteq V$, $\mathbb{D}_2 \not\subseteq \mathbb{D}_3$.

## The Sums

The sums of the pairs, with the same ordering:

| | $S$ | $V$ | $\mathbb{D}_2$ | $\mathbb{D}_3$ |
|---|---|---|---|---|
| $S$ | $1$ | $4$ | $2$ | $2$ |
| $V$ | $4$ | $3$ | $4$ | $4$ |
| $\mathbb{D}_2$ | $2$ | $4$ | $2$ | $3$ |
| $\mathbb{D}_3$ | $2$ | $4$ | $3$ | $2$ |

The dimension of a sum is the sum of the dimensions minus the dimension of the intersection. The pairs that span the whole algebra are $S + V = \mathbb{H}_{\mathrm{s}}$, $V + \mathbb{D}_2 = \mathbb{H}_{\mathrm{s}}$, and $V + \mathbb{D}_3 = \mathbb{H}_{\mathrm{s}}$; the pair $\mathbb{D}_2 + \mathbb{D}_3 = \operatorname{span}\{1,e_2,e_3\}$ has dimension $3$ and misses the line $\mathbb{R} e_1$; and $S + \mathbb{D}_k = \mathbb{D}_k$ because $S$ lies inside each split-complex plane. The sum $V + \mathbb{D}_k$ spans the algebra because $V$ contributes $e_1$ and $\mathbb{D}_k$ contributes $1$, and together with $e_2$ or $e_3$ they exhaust the four coordinates.

## The Involutions as Sign Patterns

Each involution preserves each of the four subspaces, and its restriction to a subspace is diagonal in the displayed bases with signs $\pm 1$. The following table records the multiplicity of the sign $-1$ on each subspace, in the basis of the table above:

| involution | $S$ | $V$ | $\mathbb{D}_2$ | $\mathbb{D}_3$ |
|---|---|---|---|---|
| ${}^{\natural}$ | $0$ of $1$ | $3$ of $3$ | $1$ of $2$ | $1$ of $2$ |
| $\alpha$ | $0$ of $1$ | $2$ of $3$ | $1$ of $2$ | $0$ of $2$ |
| $\rho$ | $0$ of $1$ | $1$ of $3$ | $0$ of $2$ | $1$ of $2$ |

The vanishing rows are the definitions: ${}^{\natural}$ acts as the identity exactly on $S$, $\alpha$ exactly on $\mathbb{D}_3$, and $\rho$ exactly on $\operatorname{span}\{1,e_1,e_2\} \supset \mathbb{D}_2$. The full multiplicities give the anti-fixed spaces: ${}^{\natural}$ negates all of $V$, $\alpha$ negates the plane $\operatorname{span}\{e_1,e_2\}$, and $\rho$ negates the line $\mathbb{R} e_3$. The remaining entries are mixed restrictions. The composition rule ${}^{\natural} = \alpha\rho$ is visible row by row: the coordinates negated by ${}^{\natural}$ are exactly those negated by one of $\alpha, \rho$ but not both, so the multiplicities compose by symmetric difference.

## How the Product and the Commutator Act

### The Scalar Line

$S$ is the centre, so it acts on every subspace by scalar multiplication: $S \cdot V \subseteq V$, $S \cdot \mathbb{D}_k \subseteq \mathbb{D}_k$, and $[S, \tilde q] = 0$ for all $\tilde q$. As a product, $S \times S \to S$ is closed.

### The Vector Subspace

The product of two vectors is not a vector: it splits as

$$
\mathbf{u}\mathbf{v} = -B(\mathbf{u},\mathbf{v})\cdot 1 + \tfrac{1}{2}[\mathbf{u},\mathbf{v}],
$$

with scalar part $-B(\mathbf{u},\mathbf{v}) \in S$ and the remainder $\tfrac{1}{2}[\mathbf{u},\mathbf{v}] \in V$; so $V \cdot V \subseteq S \oplus V = \mathbb{H}_{\mathrm{s}}$, with equality. The commutator stays in $V$, and in the basis $e_1, e_2, e_3$,

$$
[e_1,e_2] = 2 e_3, \qquad [e_2,e_3] = -2 e_1, \qquad [e_3,e_1] = 2 e_2,
$$

so $[V,V] \subseteq V$ and $V \cong \mathrm{SL}_2(\mathbb{R})$. The bracket is alternating and satisfies the Jacobi identity. It is the antisymmetrisation of the product on the vector subspace.

### The Split-Complex Planes

Each split-complex plane is a commutative subalgebra, so $\mathbb{D}_k \cdot \mathbb{D}_k \subseteq \mathbb{D}_k$ and $[\mathbb{D}_k, \mathbb{D}_k] = 0$. Across the planes the product leaves both: since $e_2 e_3 = -e_1$ and $e_3 e_2 = e_1$, one has $\mathbb{D}_2 \cdot \mathbb{D}_3 = \mathbb{H}_{\mathrm{s}}$ and $\mathbb{D}_2 \cdot \mathbb{D}_3 \not\subseteq \mathbb{D}_2 \cup \mathbb{D}_3$. The product of a scalar with a plane stays in the plane, and the two planes share only the scalar line.

### The Operation Table

| product | $S$ | $V$ | $\mathbb{D}_2$ | $\mathbb{D}_3$ |
|---|---|---|---|---|
| $S \cdot$ | $S$ | $V$ | $\mathbb{D}_2$ | $\mathbb{D}_3$ |
| $V \cdot$ | $V$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{H}_{\mathrm{s}}$ |
| $\mathbb{D}_2 \cdot$ | $\mathbb{D}_2$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{D}_2$ | $\mathbb{H}_{\mathrm{s}}$ |
| $\mathbb{D}_3 \cdot$ | $\mathbb{D}_3$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{D}_3$ |

The commutator table is the antisymmetrisation of this one: it vanishes on the diagonal pairs among $S, \mathbb{D}_2, \mathbb{D}_3$ (all commutative), equals the bracket of $V$ restricted to the vector–vector entry, and is nonzero only where the product table has an off-diagonal entry that is not symmetric.

## Worked Verifications

**Example (an intersection of dimension one).** Take $V \cap \mathbb{D}_2$. An element is $q_1 e_1 + q_2 e_2 + q_3 e_3 = q_0' + q_2' e_2$; comparing coefficients gives $q_1 = 0$, $q_3 = 0$, $q_0' = 0$ and $q_2 = q_2'$, so the intersection is $\mathbb{R} e_2$, of dimension $1$, as tabulated.

**Example (a pair that spans the algebra).** The four elements $e_1, e_2, e_3$ span $V$ and $1, e_2$ span $\mathbb{D}_2$; together they include $1, e_1, e_2, e_3$, a basis, so $V + \mathbb{D}_2 = \mathbb{H}_{\mathrm{s}}$, in agreement with $\dim V + \dim \mathbb{D}_2 - \dim(V \cap \mathbb{D}_2) = 3 + 2 - 1 = 4$.

**Example (a product that leaves its subspace).** $e_2 \in \mathbb{D}_2$ and $e_3 \in V$; their product is $e_2 e_3 = -e_1 \notin \mathbb{D}_2$ and $\notin \mathbb{D}_3$ (indeed $e_1 \in V$), consistent with the entry $\mathbb{H}_{\mathrm{s}}$ in the product table.

**Example (a mixed element and its blocks).** For $\tilde q = 2 + 3e_1 - e_2 + 4e_3$ the scalar block is $2$, the vector block is $3e_1 - e_2 + 4e_3$, and the split-complex readings are $2 - e_2 + 4e_3$ in $\mathbb{D}_2$ and $2 + 3e_1 + 4e_3$ modulo the complementary block; the involution images are $\tilde{q}^{\natural} = 2 - 3e_1 + e_2 - 4e_3$, $\alpha(\tilde q) = 2 - 3e_1 + e_2 + 4e_3$, $\rho(\tilde q) = 2 + 3e_1 - e_2 - 4e_3$.

## The Relation to the Corresponding Article for $\mathbb{B}$

The biquaternion article *Comparison of the Six Subspaces* performs the same task for the six distinguished subspaces of $\mathbb{B}$, cut out by the four $\mathbb{C}$-linear and conjugate-linear involutions. The bookkeeping is analogous — decompositions, a glance table, coordinate blocks, tables of intersections, sums, sign patterns and operations — but the geometry of the tables differs, because $\mathbb{B}$ has eight real coordinates and six subspaces, whereas $\mathbb{H}_{\mathrm{s}}$ has four coordinates and four subspaces; in $\mathbb{B}$ the blocks have dimensions $1$ and $3$, while here all four blocks have dimension $1$, which is why the intersections here take only the values $0, 1, 2, 3$. The Biquaternions category is the structural model; nothing biquaternion-specific — the central unit $i$, the quaternionic half-algebra, the Hermitian and anti-Hermitian pairing — is imported here.

## Summary

The four distinguished subspaces of $\mathbb{H}_{\mathrm{s}}$ are the scalar line $S = \langle 1\rangle$, the vector subspace $V = \langle e_1,e_2,e_3\rangle$, and the two split-complex planes $\mathbb{D}_2 = \langle 1,e_2\rangle$ and $\mathbb{D}_3 = \langle 1,e_3\rangle$. They are the eigenspaces of the involutions, with ${}^{\natural}$ giving $S \oplus V$, $\alpha$ giving $\mathbb{D}_3 \oplus \operatorname{span}\{e_1,e_2\}$, and $\rho$ giving $\operatorname{span}\{1,e_1,e_2\} \oplus \mathbb{R} e_3$; the finest common decomposition is the coordinate-block decomposition $\mathbb{H}_{\mathrm{s}} = \langle 1\rangle \oplus \langle e_1\rangle \oplus \langle e_2\rangle \oplus \langle e_3\rangle$.

The intersections are $S \cap V = 0$, $V \cap \mathbb{D}_k = \mathbb{R} e_k$, and $\mathbb{D}_2 \cap \mathbb{D}_3 = S$, with $S$ inside both planes. The sums show that $V$ together with either split-complex plane spans the algebra, while the two planes together span only $\operatorname{span}\{1,e_2,e_3\}$. The involutions act on each subspace by the sign patterns tabulated above, and the composition rule ${}^{\natural} = \alpha\rho$ composes the multiplicities by symmetric difference. The product is closed on $S, \mathbb{D}_2, \mathbb{D}_3$, sends $V \cdot V$ into $S \oplus V$, and sends the products across the split-complex planes into the whole algebra; the commutator vanishes on the commutative pieces and makes $V$ the Lie algebra $\mathrm{SL}_2(\mathbb{R})$.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra | *Split-Quaternion Algebra* |
| $S = \langle 1\rangle$ | the scalar line | *Split-Quaternion Scalar and Vector Subspaces* |
| $V = \langle e_1,e_2,e_3\rangle$ | the vector subspace | *Split-Quaternion Scalar and Vector Subspaces* |
| $\mathbb{D}_2 = \langle 1,e_2\rangle$, $\mathbb{D}_3 = \langle 1,e_3\rangle$ | the split-complex planes | *Split-Quaternion Split-Complex Subspaces* |
| $\langle \cdot \rangle$ | real span of the displayed elements | this article |
| ${}^{\natural}$, $\alpha$, $\rho$ | conjugation, principal involution, reversal | *Split-Quaternion Subspaces and the Involutions* |
| $B$, $N$ | the polarised form and the split-quaternion norm | *Split-Quaternion Norm and Invertibility* |
| $[\tilde q,\tilde p] = \tilde q \tilde p-\tilde p\tilde q$ | the commutator | *Split-Quaternion Scalar and Vector Subspaces* |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the systematic bookkeeping of subspaces and their intersections in an algebra with idempotents.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the coordinate blocks and the involutions of a Clifford algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the lattice of subspaces fixed by the involutions of the low-dimensional Clifford algebras.
