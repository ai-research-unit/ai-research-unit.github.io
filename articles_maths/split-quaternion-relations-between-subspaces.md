
# __Split-Quaternion Relations Between Subspaces__

## Introduction

The four distinguished subspaces of $\mathbb{H}_{\mathrm{s}}$ — the scalar line $S$, the vector subspace $V$ and the two split-complex planes $\mathbb{D}_2, \mathbb{D}_3$ — are defined by different conditions, but they are not independent: they contain one another, they intersect, they sum to subspaces of $\mathbb{H}_{\mathrm{s}}$, and they are cut out of the four real coordinates by the involutions. This article collects those relations in one place, after the individual articles *Split-Quaternion Scalar and Vector Subspaces* and *Split-Quaternion Split-Complex Subspaces*, and before the structural article *Split-Quaternion Involution Lattice*, which treats the involutions themselves.

Every number below — dimensions of intersections, of sums, and the entries of the tables — is derived from the definitions by comparison of coefficients, so the article doubles as an index of the four subspaces and of the coordinate blocks.

## The Three Decompositions

Two of the three involutions split $\mathbb{H}_{\mathrm{s}}$ into distinguished subspaces, and the third splits it into two further subspaces:

| involution | fixed space | anti-fixed space | decomposition |
|---|---|---|---|
| ${}^{\natural}$ | $S = \mathbb{R}\cdot 1$ | $V = \operatorname{span}\{\vec e_x,\vec e_y,\vec e_z\}$ | $\mathbb{H}_{\mathrm{s}} = S \oplus V$ |
| $\alpha$ | $\mathbb{D}_3 = \operatorname{span}\{1,\vec e_z\}$ | $\operatorname{span}\{\vec e_x,\vec e_y\}$ | $\mathbb{H}_{\mathrm{s}} = \mathbb{D}_3 \oplus \operatorname{span}\{\vec e_x,\vec e_y\}$ |
| $\rho$ | $\operatorname{span}\{1,\vec e_x,\vec e_y\}$ | $\mathbb{R} \vec e_z$ | $\mathbb{H}_{\mathrm{s}} = \operatorname{span}\{1,\vec e_x,\vec e_y\} \oplus \mathbb{R} \vec e_z$ |

The three decompositions are the **scalar–vector** decomposition, and the two decompositions associated with the principal involution and the reversal. Every element has three readings, one per row. The finest common refinement of the three is the coordinate-block decomposition of the next section.

## The Four Subspaces at a Glance

| subspace | defining condition | real basis | $\dim_{\mathbb{R}}$ | subalgebra | norm |
|---|---|---|---|---|---|
| $S$ | $\tilde{q}^{\natural} = \tilde q$ | $1$ | $1$ | yes, $\cong \mathbb{R}$ | $q_t^2$, positive definite |
| $V$ | $\tilde{q}^{\natural} = -\tilde q$ | $\vec e_x,\vec e_y,\vec e_z$ | $3$ | no (Lie) | $q_x^2-q_y^2-q_z^2$, signature $(2,1)$ |
| $\mathbb{D}_2$ | closed under products of $1, \vec e_y$ | $1,\vec e_y$ | $2$ | yes, $\cong \mathbb{D}$ | $q_t^2-q_y^2$, signature $(1,1)$ |
| $\mathbb{D}_3$ | $\alpha(\tilde q) = \tilde q$ | $1,\vec e_z$ | $2$ | yes, $\cong \mathbb{D}$ | $q_t^2-q_z^2$, signature $(1,1)$ |

Only three of the four are closed under multiplication: the scalar line and the two split-complex planes. The vector subspace is not a subalgebra but is closed under the commutator, and it is the only one of the four that carries a nonzero bracket — the other three are commutative. The norms are the restrictions of $\langle\cdot\rangle_{\natural}$; all four are non-degenerate, the first definite and the other three indefinite.

## The Four Coordinate Blocks

The four real coordinates of a split-quaternion are $(q_t,q_x,q_y,q_z)$ in the basis $1, \vec e_x, \vec e_y, \vec e_z$. They group into four one-dimensional **coordinate blocks**,

$$
\mathbb{H}_{\mathrm{s}} = \langle 1 \rangle \oplus \langle \vec e_x \rangle \oplus \langle \vec e_y \rangle \oplus \langle \vec e_z \rangle,
$$

where $\langle \cdot\rangle$ denotes the real span of the displayed elements. Each of the blocks $\langle 1\rangle$, $\langle \vec e_y\rangle$ and $\langle \vec e_z\rangle$ is the intersection of the distinguished subspaces containing it, and $\langle \vec e_x\rangle$ is the complement of $\mathbb{D}_2 + \mathbb{D}_3$ in $\mathbb{H}_{\mathrm{s}}$; each of the four distinguished subspaces is a sum of blocks:

$$
\boxed{\;
S = \langle 1 \rangle, \qquad V = \langle \vec e_x \rangle \oplus \langle \vec e_y \rangle \oplus \langle \vec e_z \rangle
\;}
$$,

$$
\mathbb{D}_2 = \langle 1 \rangle \oplus \langle \vec e_y \rangle, \qquad \mathbb{D}_3 = \langle 1 \rangle \oplus \langle \vec e_z \rangle .
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
\boxed{\;
S \cap V = \{0\}, \quad S \cap \mathbb{D}_2 = S, \quad S \cap \mathbb{D}_3 = S, \quad V \cap \mathbb{D}_2 = \mathbb{R} \vec e_y
\;}
$$,

$$
V \cap \mathbb{D}_3 = \mathbb{R} \vec e_z, \quad \mathbb{D}_2 \cap \mathbb{D}_3 = S .
$$

Three features are worth isolating:

- The scalar line is contained in both split-complex planes, so it meets them in dimension $1$; it meets the vector subspace only in the origin, being the complement of $V$ in the scalar–vector decomposition.
- The vector subspace meets each split-complex plane in a single line, spanned by the common basis element $\vec e_y$ or $\vec e_z$, and the two planes meet each other in the scalar line.
- No two of the four subspaces are equal, and no pair except the obvious containment pairs is nested: $S \subset \mathbb{D}_2$, $S \subset \mathbb{D}_3$, and $S \subset S \oplus V$ but $S \not\subseteq V$, $\mathbb{D}_2 \not\subseteq \mathbb{D}_3$.

## The Sums

The sums of the pairs, with the same ordering:

| | $S$ | $V$ | $\mathbb{D}_2$ | $\mathbb{D}_3$ |
|---|---|---|---|---|
| $S$ | $1$ | $4$ | $2$ | $2$ |
| $V$ | $4$ | $3$ | $4$ | $4$ |
| $\mathbb{D}_2$ | $2$ | $4$ | $2$ | $3$ |
| $\mathbb{D}_3$ | $2$ | $4$ | $3$ | $2$ |

The dimension of a sum is the sum of the dimensions minus the dimension of the intersection. The pairs that span the whole algebra are $S + V = \mathbb{H}_{\mathrm{s}}$, $V + \mathbb{D}_2 = \mathbb{H}_{\mathrm{s}}$, and $V + \mathbb{D}_3 = \mathbb{H}_{\mathrm{s}}$; the pair $\mathbb{D}_2 + \mathbb{D}_3 = \operatorname{span}\{1,\vec e_y,\vec e_z\}$ has dimension $3$ and misses the line $\mathbb{R} \vec e_x$; and $S + \mathbb{D}_k = \mathbb{D}_k$ because $S$ lies inside each split-complex plane. The sum $V + \mathbb{D}_k$ spans the algebra because $V$ contributes $\vec e_x$ and $\mathbb{D}_k$ contributes $1$, and together with $\vec e_y$ or $\vec e_z$ they exhaust the four coordinates.

## The Involutions as Sign Patterns

Each involution preserves each of the four subspaces, and its restriction to a subspace is diagonal in the displayed bases with signs $\pm 1$. The following table records the multiplicity of the sign $-1$ on each subspace, in the basis of the table above:

| involution | $S$ | $V$ | $\mathbb{D}_2$ | $\mathbb{D}_3$ |
|---|---|---|---|---|
| ${}^{\natural}$ | $0$ of $1$ | $3$ of $3$ | $1$ of $2$ | $1$ of $2$ |
| $\alpha$ | $0$ of $1$ | $2$ of $3$ | $1$ of $2$ | $0$ of $2$ |
| $\rho$ | $0$ of $1$ | $1$ of $3$ | $0$ of $2$ | $1$ of $2$ |

The vanishing rows are the definitions: ${}^{\natural}$ acts as the identity exactly on $S$, $\alpha$ exactly on $\mathbb{D}_3$, and $\rho$ exactly on $\operatorname{span}\{1,\vec e_x,\vec e_y\} \supset \mathbb{D}_2$. The full multiplicities give the anti-fixed spaces: ${}^{\natural}$ negates all of $V$, $\alpha$ negates the plane $\operatorname{span}\{\vec e_x,\vec e_y\}$, and $\rho$ negates the line $\mathbb{R} \vec e_z$. The remaining entries are mixed restrictions. The composition rule ${}^{\natural} = \alpha\rho$ is visible row by row: the coordinates negated by ${}^{\natural}$ are exactly those negated by one of $\alpha, \rho$ but not both, so the multiplicities compose by symmetric difference.

## How the Product and the Commutator Act

### The Scalar Line

$S$ is the centre, so it acts on every subspace by scalar multiplication: $S \cdot V \subseteq V$, $S \cdot \mathbb{D}_k \subseteq \mathbb{D}_k$, and $[S, \tilde q] = 0$ for all $\tilde q$. As a product, $S \times S \to S$ is closed.

### The Vector Subspace

The product of two vectors is not a vector: it splits as

$$
\boxed{\;
\vec q\vec q_1 = -B(\vec q,\vec q_1)\cdot 1 + \tfrac{1}{2}[\vec q,\vec q_1]
\;}
$$,

with scalar part $-B(\vec q,\vec q_1) \in S$ and the remainder $\tfrac{1}{2}[\vec q,\vec q_1] \in V$; so $V \cdot V \subseteq S \oplus V = \mathbb{H}_{\mathrm{s}}$, with equality. The commutator stays in $V$, and in the basis $\vec e_x, \vec e_y, \vec e_z$,

$$
[\vec e_x,\vec e_y] = 2 \vec e_z, \qquad [\vec e_y,\vec e_z] = -2 \vec e_x, \qquad [\vec e_z,\vec e_x] = 2 \vec e_y,
$$

so $[V,V] \subseteq V$ and $V \cong \mathrm{SL}_2(\mathbb{R})$. The bracket is alternating and satisfies the Jacobi identity. It is the antisymmetrisation of the product on the vector subspace.

### The Split-Complex Planes

Each split-complex plane is a commutative subalgebra, so $\mathbb{D}_k \cdot \mathbb{D}_k \subseteq \mathbb{D}_k$ and $[\mathbb{D}_k, \mathbb{D}_k] = 0$. Across the planes the product leaves both: since $\vec e_y \vec e_z = -\vec e_x$ and $\vec e_z \vec e_y = \vec e_x$, one has $\mathbb{D}_2 \cdot \mathbb{D}_3 = \mathbb{H}_{\mathrm{s}}$ and $\mathbb{D}_2 \cdot \mathbb{D}_3 \not\subseteq \mathbb{D}_2 \cup \mathbb{D}_3$. The product of a scalar with a plane stays in the plane, and the two planes share only the scalar line.

### The Operation Table

| product | $S$ | $V$ | $\mathbb{D}_2$ | $\mathbb{D}_3$ |
|---|---|---|---|---|
| $S \cdot$ | $S$ | $V$ | $\mathbb{D}_2$ | $\mathbb{D}_3$ |
| $V \cdot$ | $V$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{H}_{\mathrm{s}}$ |
| $\mathbb{D}_2 \cdot$ | $\mathbb{D}_2$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{D}_2$ | $\mathbb{H}_{\mathrm{s}}$ |
| $\mathbb{D}_3 \cdot$ | $\mathbb{D}_3$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{D}_3$ |

The commutator table is the antisymmetrisation of this one: it vanishes on the diagonal pairs among $S, \mathbb{D}_2, \mathbb{D}_3$ (all commutative), equals the bracket of $V$ restricted to the vector–vector entry, and is nonzero only where the product table has an off-diagonal entry that is not symmetric.

## Worked Verifications

**Example (an intersection of dimension one).** Take $V \cap \mathbb{D}_2$. An element is $q_x \vec e_x + q_y \vec e_y + q_z \vec e_z = q_t + q_y \vec e_y$; comparing coefficients gives $q_x = 0$, $q_z = 0$ and $q_t = 0$, so the intersection is $\mathbb{R} \vec e_y$, of dimension $1$, as tabulated.

**Example (a pair that spans the algebra).** The four elements $\vec e_x, \vec e_y, \vec e_z$ span $V$ and $1, \vec e_y$ span $\mathbb{D}_2$; together they include $1, \vec e_x, \vec e_y, \vec e_z$, a basis, so $V + \mathbb{D}_2 = \mathbb{H}_{\mathrm{s}}$, in agreement with $\dim V + \dim \mathbb{D}_2 - \dim(V \cap \mathbb{D}_2) = 3 + 2 - 1 = 4$.

**Example (a product that leaves its subspace).** $\vec e_y \in \mathbb{D}_2$ and $\vec e_z \in V$; their product is $\vec e_y \vec e_z = -\vec e_x \notin \mathbb{D}_2$ and $\notin \mathbb{D}_3$ (indeed $\vec e_x \in V$), consistent with the entry $\mathbb{H}_{\mathrm{s}}$ in the product table.

**Example (a mixed element and its blocks).** For $\tilde q = 2 + 3\vec e_x - \vec e_y + 4\vec e_z$ the scalar block is $2$, the vector block is $3\vec e_x - \vec e_y + 4\vec e_z$, and the split-complex readings are $2 - \vec e_y + 4\vec e_z$ in $\mathbb{D}_2$ and $2 + 3\vec e_x + 4\vec e_z$ modulo the complementary block; the involution images are $\tilde{q}^{\natural} = 2 - 3\vec e_x + \vec e_y - 4\vec e_z$, $\alpha(\tilde q) = 2 - 3\vec e_x + \vec e_y + 4\vec e_z$, $\rho(\tilde q) = 2 + 3\vec e_x - \vec e_y - 4\vec e_z$.

## The Relation to the Corresponding Article for $\mathbb{B}$

The biquaternion article *Comparison of the Remarkable Subspaces* performs the same task for the remarkable subspaces of $\mathbb{B}$, cut out by the four $\mathbb{C}$-linear and conjugate-linear involutions. The bookkeeping is analogous — decompositions, a glance table, coordinate blocks, tables of intersections, sums, sign patterns and operations — but the geometry of the tables differs, because $\mathbb{B}$ has eight real coordinates and remarkable subspaces, whereas $\mathbb{H}_{\mathrm{s}}$ has four coordinates and four subspaces; in $\mathbb{B}$ the blocks have dimensions $1$ and $3$, while here all four blocks have dimension $1$, which is why the intersections here take only the values $0, 1, 2, 3$. The Biquaternions category is the structural model; nothing biquaternion-specific — the central unit $i$, the quaternionic half-algebra, the Hermitian and anti-Hermitian pairing — is imported here.

## Summary

The four distinguished subspaces of $\mathbb{H}_{\mathrm{s}}$ are the scalar line $S = \langle 1\rangle$, the vector subspace $V = \langle \vec e_x,\vec e_y,\vec e_z\rangle$, and the two split-complex planes $\mathbb{D}_2 = \langle 1,\vec e_y\rangle$ and $\mathbb{D}_3 = \langle 1,\vec e_z\rangle$. They are the eigenspaces of the involutions, with ${}^{\natural}$ giving $S \oplus V$, $\alpha$ giving $\mathbb{D}_3 \oplus \operatorname{span}\{\vec e_x,\vec e_y\}$, and $\rho$ giving $\operatorname{span}\{1,\vec e_x,\vec e_y\} \oplus \mathbb{R} \vec e_z$; the finest common decomposition is the coordinate-block decomposition $\mathbb{H}_{\mathrm{s}} = \langle 1\rangle \oplus \langle \vec e_x\rangle \oplus \langle \vec e_y\rangle \oplus \langle \vec e_z\rangle$.

The intersections are $S \cap V = 0$, $V \cap \mathbb{D}_k = \mathbb{R} \vec e_k$, and $\mathbb{D}_2 \cap \mathbb{D}_3 = S$, with $S$ inside both planes. The sums show that $V$ together with either split-complex plane spans the algebra, while the two planes together span only $\operatorname{span}\{1,\vec e_y,\vec e_z\}$. The involutions act on each subspace by the sign patterns tabulated above, and the composition rule ${}^{\natural} = \alpha\rho$ composes the multiplicities by symmetric difference. The product is closed on $S, \mathbb{D}_2, \mathbb{D}_3$, sends $V \cdot V$ into $S \oplus V$, and sends the products across the split-complex planes into the whole algebra; the commutator vanishes on the commutative pieces and makes $V$ the Lie algebra $\mathrm{SL}_2(\mathbb{R})$.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra | *Split-Quaternion Algebra* |
| $S = \langle 1\rangle$ | the scalar line | *Split-Quaternion Scalar and Vector Subspaces* |
| $V = \langle \vec e_x,\vec e_y,\vec e_z\rangle$ | the vector subspace | *Split-Quaternion Scalar and Vector Subspaces* |
| $\mathbb{D}_2 = \langle 1,\vec e_y\rangle$, $\mathbb{D}_3 = \langle 1,\vec e_z\rangle$ | the split-complex planes | *Split-Quaternion Split-Complex Subspaces* |
| $\langle \cdot \rangle$ | real span of the displayed elements | this article |
| ${}^{\natural}$, $\alpha$, $\rho$ | conjugation, principal involution, reversal | *Split-Quaternion Subspaces and the Involutions* |
| $B$, $\langle\cdot\rangle_{\natural}$ | the polarised form and the split-quaternion norm | *Split-Quaternion Norm and Invertibility* |
| $[\tilde q_1,\tilde q_2] = \tilde q_1 \tilde q_2-\tilde q_2\tilde q_1$ | the commutator | *Split-Quaternion Scalar and Vector Subspaces* |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the systematic bookkeeping of subspaces and their intersections in an algebra with idempotents.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the coordinate blocks and the involutions of a Clifford algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the lattice of subspaces fixed by the involutions of the low-dimensional Clifford algebras.
