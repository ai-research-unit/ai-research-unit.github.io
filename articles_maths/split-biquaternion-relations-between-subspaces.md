
# __Split-Biquaternion Relations Between Subspaces__

## Introduction

The four distinguished subspaces of $\mathbb{H}_{\mathbb{D}}$ are defined by the four involutions, but they are not independent objects: they intersect one another, they sum to subspaces of $\mathbb{H}_{\mathbb{D}}$, they split the eight real coordinates into four **coordinate blocks**, and they are permuted and negated by the involutions. This article collects those relations in one place, after the four individual articles *Split-Biquaternion Split-Complex Subspace*, *Split-Biquaternion Quaternion Subspace*, *Split-Biquaternion Hermitian Subspace* and *Split-Biquaternion Anti-Hermitian Subspace*, and before the structural article *Split-Biquaternion Involution Lattice*, which treats the four involutions themselves.

Every number below — dimensions of intersections, of sums, and the entries of the tables — is derived here from the definitions by the comparison of coefficients, so the article doubles as the index of the four subspaces. Throughout, $\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ with $Q_\mu = q_\mu + j q'_\mu \in \mathbb{D}$, and the conjugations are ${}^{\natural}$ (quaternion), $\bar{\cdot}$ (split complex), ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ and ${}^{\flat} = -{}^{*}$.

## The Three Decompositions

The three commuting involutions ${}^{\natural}$, $\bar{\cdot}$ and ${}^{*}$ each split $\mathbb{H}_{\mathbb{D}}$ into a fixed space and an anti-fixed space, and each split gives a direct-sum decomposition of the algebra into two subspaces:

| involution | fixed space | anti-fixed space | decomposition |
|---|---|---|---|
| ${}^{\natural}$ | $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | $\mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$ | $\mathbb{H}_{\mathbb{D}} = \mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \oplus \mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$ |
| $\bar{\cdot}$ | $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | $j\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | $\mathbb{H}_{\mathbb{D}} = \mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \oplus j\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ |
| ${}^{*}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ | $\mathbb{H}_{\mathbb{D}} = \mathbb{M}_+ \oplus \mathbb{M}_-$ |

The fourth conjugation, the anti-Hermitian conjugation $\flat = -{}^{*}$, has the same eigenspaces as ${}^{*}$ with the signs exchanged: its fixed space is $\mathbb{M}_-$ and its anti-fixed space is $\mathbb{M}_+$, so it produces no subspace beyond those of the table. The three decompositions are the **scalar–vector**, the **split complex** and the **Hermitian** decomposition of the algebra, and every element has three readings, one per row.

## The Four Subspaces at a Glance

| subspace | defining condition | real basis | $\dim_{\mathbb{R}}$ | subalgebra | norm |
|---|---|---|---|---|---|
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | $\tilde{Q}^{\natural} = \tilde{Q}$ | $e_0, j$ | $2$ | yes, $\cong \mathbb{D}$ | $Q_0^2$, split complex; real part $(2,0)$, Hermitian form $(1,1)$ |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | $\bar{\tilde{Q}} = \tilde{Q}$ | $e_0,e_1,e_2,e_3$ | $4$ | yes, $\cong \mathbb{H}$ | $q_0^2+q_1^2+q_2^2+q_3^2$, definite positive |
| $\mathbb{M}_+$ | $\tilde{Q}^{*} = \tilde{Q}$ | $e_0,je_1,je_2,je_3$ | $4$ | no, Jordan | definite positive $(4,0)$; Hermitian form $(1,3)$ |
| $\mathbb{M}_-$ | $\tilde{Q}^{\flat} = \tilde{Q}$ | $je_0,e_1,e_2,e_3$ | $4$ | no, Lie | definite positive $(4,0)$; Hermitian form $(3,1)$ |

Only two of the four are closed under multiplication; of the remaining two, exactly one is closed under the commutator and exactly one under the symmetrized product, so one of the four is a Lie algebra and one is a Jordan algebra. A structural difference from the biquaternion family of six subspaces is the behaviour of the split-biquaternion norm: there the two sectors $\mathbb{M}_\pm$ carry an **indefinite** norm of signature $(1,3)$ and $(3,1)$, while here the central unit $j$ satisfies $j^2 = +1$ and the split-biquaternion norm is **definite positive** on both sectors. The indefinite form on the sectors here is the Hermitian form, of signature $(1,3)$ and $(3,1)$ respectively.

## The Four Coordinate Blocks

The eight real coordinates of $\mathbb{H}_{\mathbb{D}}$ are $(q_0,q_1,q_2,q_3,q'_0,q'_1,q'_2,q'_3)$. They group into four real subspaces, each of dimension one or three, and each block is the simultaneous intersection of two of the four subspaces:

| block | basis | $\dim_{\mathbb{R}}$ | as an intersection |
|---|---|---|---|
| the real scalar line | $e_0$ | $1$ | $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{H}_{\mathbb{H}_{\mathbb{D}}} = \mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{M}_+ = \mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{M}_+$ |
| the split-imaginary scalar line | $je_0$ | $1$ | $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{M}_-$ |
| the real vector triple | $e_1,e_2,e_3$ | $3$ | $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{M}_-$ |
| the split-imaginary vector triple | $je_1,je_2,je_3$ | $3$ | — (not an intersection of two of the four) |

The four subspaces are sums of blocks:

$$
\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} = \langle e_0 \rangle \oplus \langle je_0\rangle, \qquad \mathbb{H}_{\mathbb{H}_{\mathbb{D}}} = \langle e_0 \rangle \oplus \langle e_1,e_2,e_3\rangle,
$$

$$
\mathbb{M}_+ = \langle e_0 \rangle \oplus \langle je_1,je_2,je_3\rangle, \qquad \mathbb{M}_- = \langle je_0 \rangle \oplus \langle e_1,e_2,e_3\rangle.
$$

The two anti-fixed spaces that complete the pattern are also sums of blocks, $\mathrm{Vect}(\mathbb{H}_{\mathbb{D}}) = \langle e_1,e_2,e_3\rangle \oplus \langle je_1,je_2,je_3\rangle$ and $j\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} = \langle je_0\rangle \oplus \langle je_1,je_2,je_3\rangle$. Every intersection below is a sum of blocks, which is why the dimension arithmetic is so simple: two subspaces meet in a block if they share a block, in a sum of blocks if they share two, and in the origin if they share none. The split-imaginary vector triple is the one block that is not the intersection of two of the four subspaces; it is $\mathbb{M}_+ \cap \mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$.

## The Intersections

The pairwise intersections, with dimensions:

| | $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
|---|---|---|---|---|
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | $2$ | $1$ | $1$ | $1$ |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | $1$ | $4$ | $1$ | $3$ |
| $\mathbb{M}_+$ | $1$ | $1$ | $4$ | $0$ |
| $\mathbb{M}_-$ | $1$ | $3$ | $0$ | $4$ |

The diagonal carries the dimensions of the subspaces themselves. Three features deserve to be isolated, because they are the relations the individual articles use:

- the two members of each decomposition meet in the origin, and of the four subspaces only the pair $(\mathbb{M}_+,\mathbb{M}_-)$ is a decomposition, so it is the only pair with intersection $0$;
- the centre $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ meets each of the others in one of the two scalar lines, $e_0$ for the quaternion and Hermitian spaces and $je_0$ for the anti-Hermitian space;
- the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ meets the Hermitian subspace in the scalar line and the anti-Hermitian subspace in the real vector triple.

The last two rows encode the same information as the block table: $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ and $\mathbb{M}_-$ share the real vector triple, while $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ and $\mathbb{M}_-$ share the split-imaginary scalar line.

## The Sums

The sums of the pairs, with the same ordering:

| | $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
|---|---|---|---|---|
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | $2$ | $5$ | $5$ | $5$ |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | $5$ | $4$ | $7$ | $5$ |
| $\mathbb{M}_+$ | $5$ | $7$ | $4$ | $8$ |
| $\mathbb{M}_-$ | $5$ | $5$ | $8$ | $4$ |

The dimension of a sum is the sum of the dimensions minus the dimension of the intersection. Exactly one pair has sum $8$ and so spans the algebra: the Hermitian pair $(\mathbb{M}_+,\mathbb{M}_-)$. The pair $(\mathbb{H}_{\mathbb{H}_{\mathbb{D}}},\mathbb{M}_+)$ has dimension $7$, the pairs whose intersection is a scalar line have dimension $5$, and the pair $(\mathbb{H}_{\mathbb{H}_{\mathbb{D}}},\mathbb{M}_-)$ has intersection a vector triple and sum $4+4-3=5$. Note that the centre and the quaternion subspace together span only a five-dimensional subspace, so neither the scalar–vector nor the split complex decomposition is obtained from the four subspaces alone.

## The Involutions as Sign Patterns

Each of the four involutions preserves each of the four subspaces, and its restriction to a subspace is diagonal in the displayed bases, with signs $+1$ and $-1$ only. The following table records the multiplicity of the sign $-1$ on each subspace, in the basis of the article of that subspace:

| involution | $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
|---|---|---|---|---|
| ${}^{\natural}$ | $0$ of $2$ | $3$ of $4$ | $3$ of $4$ | $3$ of $4$ |
| $\bar{\cdot}$ | $1$ of $2$ | $0$ of $4$ | $3$ of $4$ | $1$ of $4$ |
| ${}^{*}$ | $1$ of $2$ | $3$ of $4$ | $0$ of $4$ | $4$ of $4$ |
| $\flat$ | $1$ of $2$ | $1$ of $4$ | $4$ of $4$ | $0$ of $4$ |

The vanishing entries are the definitions: ${}^{\natural}$ acts as the identity exactly on the centre, $\bar{\cdot}$ exactly on the quaternion subspace, ${}^{*}$ exactly on $\mathbb{M}_+$, and $\flat$ exactly on $\mathbb{M}_-$; the full multiplicities are the definitions of the complementary spaces, with $\flat$ acting as minus the identity exactly on $\mathbb{M}_+$ and ${}^{*}$ as minus the identity exactly on $\mathbb{M}_-$, as the last column shows.

Two consequences follow from the table alone. First, no subspace other than the centre is fixed pointwise by more than one of the four involutions, and the four subspaces are pairwise distinct as sets. Second, the composition rule ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ is visible row by row: the coordinates negated by ${}^{*}$ are exactly those negated by one of $\bar{\cdot}$ and ${}^{\natural}$ but not by both, so the multiplicities compose by symmetric difference. On $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, for instance, $\bar{\cdot}$ negates none and ${}^{\natural}$ negates the three real vector units, so ${}^{*}$ negates the same three; on $\mathbb{M}_+$, $\bar{\cdot}$ and ${}^{\natural}$ negate the same three split-imaginary vector units, and those cancel, leaving multiplicity $0$. The counterpart in $\mathbb{B}$ has a six-column table, the two extra columns being the vector subspace $\mathrm{Vect}(\mathbb{B})$ and the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, and this is the reduction discussed below.

## How the Operations Act on the Splits

Since the centre is central and the four subspaces are the fixed spaces of involutions, the product, the commutator and the symmetrized product distribute through the splits in a way that can be tabulated.

### The Product and the Brackets

| pair | product lies in | symmetrized product | commutator |
|---|---|---|---|
| $\mathbb{M}_+, \mathbb{M}_+$ | $\mathbb{R} \oplus \mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
| $\mathbb{M}_-, \mathbb{M}_-$ | $\mathbb{R} \oplus \mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
| $\mathbb{M}_+, \mathbb{M}_-$ | $j\mathbb{R} \oplus \mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$ | $\mathbb{M}_-$ | $\mathrm{span}\{je_1,je_2,je_3\}$ |

The entries are read off the expansions of the product. For $\tilde{Q} = q_0 e_0 + j\mathbf{u}$ and $\tilde{R} = r_0 e_0 + j\mathbf{v}$ in $\mathbb{M}_+$,

$$
\tilde{Q}\tilde{R} = q_0 r_0 - \mathbf{u}\cdot\mathbf{v} + \mathbf{u}\times\mathbf{v} + j(q_0\mathbf{v}+r_0\mathbf{u}),
$$

which has real scalar part, real vector part $\mathbf{u}\times\mathbf{v}$ and split-imaginary vector part $j(q_0\mathbf{v}+r_0\mathbf{u})$, hence lies in $\mathbb{R}\oplus\mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$; the commutator keeps only $2\,\mathbf{u}\times\mathbf{v}$, a real vector, so it lies in $\mathbb{M}_-$, and the symmetrized product drops $\mathbf{u}\times\mathbf{v}$, leaving a real scalar and a split-imaginary vector, which is $\mathbb{M}_+$. The other rows follow from the analogous expansion for $\mathbb{M}_-$ and from the mixed expansion. In words: the symmetrized products respect the sectors (Hermitian stays Hermitian, anti-Hermitian goes to Hermitian, mixed goes to anti-Hermitian), while the commutators leave the sector in the Hermitian direction and give $\mathrm{SO}(3)$ for the pure units. The centre multiplies into every subspace without change, and the quaternion subspace acts on the algebra by multiplication.

### The Reduction from Six Subspaces to Four

In $\mathbb{B}$ the fixed spaces of ${}^{\natural}, \bar{\cdot}, {}^{*}, {}^{\flat}$ are complemented by naming the two **anti-fixed** spaces of ${}^{\natural}$ and $\bar{\cdot}$, namely $\mathrm{Vect}(\mathbb{B})$ and $i\mathbb{H}_{\mathbb{B}}$, which gives six distinguished subspaces. In $\mathbb{H}_{\mathbb{D}}$ only four are named. The reason is the sign in the central square:

- $\mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$ is the six-dimensional complement of the centre in the scalar–vector split; it is treated inside the algebra article rather than as a subspace of its own, because it is larger than the other members and is not a fixed space of any of the four involutions.
- $j\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, the anti-fixed space of split complex conjugation, is the image of $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ under the central scalar $j$. Since $j^2 = +1$, multiplication by $j$ **preserves** the split-biquaternion norm, $N(j\tilde{Q}) = j^2 N(\tilde{Q}) = N(\tilde{Q})$, so $j\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ is isometric to $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ and carries no new structure. In $\mathbb{B}$ the corresponding multiplication by the central unit $i$ **negates** the split-biquaternion norm, $N(i\tilde{Q}) = i^2 N(\tilde{Q}) = -N(\tilde{Q})$, so the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ is negative definite and is genuinely distinct from $\mathbb{H}_{\mathbb{B}}$.

The four named subspaces are therefore the four fixed spaces of the four involutions, and the two anti-fixed spaces are omitted: one because it is a degenerate six-dimensional object, the other because it is isometric to a named subspace.

## Worked Verifications

### An Intersection of Dimension Three

The element $e_1$ has real coefficients, so it lies in $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, and it has real vector part with zero scalar part, so it lies in $\mathbb{M}_-$; hence it lies in the intersection $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{M}_-$, which is the three-dimensional space $\mathrm{span}\{e_1,e_2,e_3\}$. The same holds for $e_2$ and $e_3$, and no element of the intersection has a nonzero real scalar part, by the defining conditions $Q_0 = 0$ and $Q_k$ real.

### The Hermitian Decomposition

For an arbitrary element, $\tfrac{1}{2}(\tilde{Q} + \tilde{Q}^{*})$ is Hermitian and $\tfrac{1}{2}(\tilde{Q} - \tilde{Q}^{*})$ is anti-Hermitian — these being fixed by ${}^{*}$ and by $\flat = -{}^{*}$ respectively — and they sum to $\tilde{Q}$. For instance $e_0 \in \mathbb{M}_+$ and $j = je_0 \in \mathbb{M}_-$; therefore $\mathbb{M}_+ + \mathbb{M}_- = \mathbb{H}_{\mathbb{D}}$, and since the two meet only at the origin, the sum is direct.

### A Mixed Element and Its Blocks

For the element $\tilde{Q} = (1 + j) + e_1 + je_2$ the four coordinate blocks are the real scalar part $1$, the split-imaginary scalar part $j$, the real vector part $e_1$ and the split-imaginary vector part $je_2$. Its Hermitian conjugate is $\tilde{Q}^{*} = (1 - j) - e_1 + je_2$, so

$$
\tfrac{1}{2}(\tilde{Q} + \tilde{Q}^{*}) = 1 + je_2 \in \mathbb{M}_+, \qquad \tfrac{1}{2}(\tilde{Q} - \tilde{Q}^{*}) = j + e_1 \in \mathbb{M}_-,
$$

the two parts lying in the two sectors of the Hermitian decomposition, as the general statement requires.

## The Four Readings Compared

The four distinguished subspaces are read in four ways, and the comparison is the content of this section.

### The Algebra

The quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ is the only subalgebra, and it is a division algebra; the centre $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ is a commutative subalgebra with zero divisors; $\mathbb{M}_+$ is a Jordan algebra with respect to the symmetrized product; and $\mathbb{M}_-$ is a Lie algebra with respect to the commutator. The product of two elements closes inside a subspace exactly for the quaternion subspace and the centre, and the two Hermitian sectors instead exchange under the product.

### The Topology

The Euclidean norm restricts to a positive definite form of signature $(4,0)$ on the quaternion subspace, on $\mathbb{M}_+$ and on $\mathbb{M}_-$, and to $(2,0)$ on the centre, so its unit level set is compact on every subspace. The Hermitian scalar form $g$ agrees with the Euclidean form on the quaternion subspace, is $(2,0)$ on the centre, and is indefinite on the two Hermitian sectors, of signature $(1,3)$ on $\mathbb{M}_+$ and $(3,1)$ on $\mathbb{M}_-$, so its level sets there are non-compact. These restrictions are tabulated in *Split-Biquaternion Norm and Invertibility* and *Split-Biquaternion Rotations and the Lorentz Group*.

### The Analysis

The quaternion subspace carries the elliptic quaternion analysis of *Quaternion Analysis* and the centre the hyperbolic split complex analysis of *Split Complex Analysis*; the two Hermitian sectors are not subalgebras and carry only the restricted ambient analysis, governed respectively by a wave operator of signature $(1,3)$ and $(3,1)$. The distinction follows the sign of the restricted Hermitian form: elliptic where that form is definite, hyperbolic where it is Lorentzian.

### The Geometry

Geometrically the four subspaces are the four invariant planes of the four conjugations: the centre is the axis of quaternion conjugation, the quaternion subspace the axis of split complex conjugation, and the two Hermitian sectors the positive and negative eigenspaces of Hermitian conjugation. The quaternion subspace carries the round sphere $S^3$, the centre the pair of null lines and a pair of hyperbolas, and the two Hermitian sectors the null cones of the two real Lorentzian forms of signature $(1,3)$ and $(3,1)$; the motions carried are the rotations $SO(4)$ on the first and the Lorentz group $SO(1,3)$ on the last two, as in *Split-Biquaternions and Hyperbolic Geometry*.

## Summary

The four distinguished subspaces of $\mathbb{H}_{\mathbb{D}}$ are the fixed spaces of the four involutions: the centre $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ of dimension $2$, and the quaternion, Hermitian and anti-Hermitian subspaces of dimension $4$. Three of the involutions give direct-sum decompositions — the scalar–vector, the split complex and the Hermitian decomposition, of which only the last is a decomposition into two of the four named subspaces. The eight real coordinates split into four blocks: the real and split-imaginary scalar lines and the real and split-imaginary vector triples; two subspaces meet in a sum of the blocks they share, and the intersection and sum tables are computed from these. The centre meets the others in a scalar line, the quaternion subspace meets the Hermitian subspace in the scalar line and the anti-Hermitian subspace in the real vector triple, and only the Hermitian pair $(\mathbb{M}_+,\mathbb{M}_-)$ spans the algebra. Each involution acts diagonally on each subspace with signs $\pm 1$, its multiplicities of $-1$ composing by symmetric difference under ${}^{*} = \bar{\cdot}\circ{}^{\natural}$. The product of two Hermitian or two anti-Hermitian elements lies in $\mathbb{R}\oplus\mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$, a mixed product lies in $j\mathbb{R}\oplus\mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$; the symmetrized products respect the sectors, while the commutators give pure quaternions and the algebra $\mathrm{SO}(3)$. The family reduces from the six subspaces of $\mathbb{B}$ to four because $\mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$ is a six-dimensional non-fixed space and $j\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ is isometric to $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ under $j^2 = +1$, whereas in $\mathbb{B}$ the corresponding anti-fixed space $i\mathbb{H}_{\mathbb{B}}$ is negative definite and genuinely new.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ | Split biquaternion algebra, real dimension $8$ |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$, $Q_\mu = q_\mu + j q'_\mu$ | General split biquaternion |
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | Split complex subspace, fixed space of ${}^{\natural}$, dimension $2$ |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | Quaternion subspace, fixed space of $\bar{\cdot}$, dimension $4$ |
| $\mathbb{M}_+, \mathbb{M}_-$ | Hermitian and anti-Hermitian subspaces, dimension $4$ |
| $\mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$ | Vector subspace, anti-fixed space of ${}^{\natural}$, dimension $6$ |
| $j\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | Anti-fixed space of $\bar{\cdot}$, dimension $4$ |
| $\langle e_0\rangle, \langle je_0\rangle, \langle e_1,e_2,e_3\rangle, \langle je_1,je_2,je_3\rangle$ | The four coordinate blocks |
| ${}^{\natural}, \bar{\cdot}, {}^{*}, {}^{\flat}$ | The four conjugations |
| $\mathbb{R}\oplus\mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$, $j\mathbb{R}\oplus\mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$ | Target spaces of the sector products |
| $\mathrm{SO}(3)$ | Bracket image of the pure units, $\mathrm{span}\{e_1,e_2,e_3\}$ |

## Further Reading

- I. L. Kantor and A. S. Solodovnikov, *Hypercomplex Numbers: An Elementary Introduction to Algebras* (Springer, 1989), for decompositions of an algebra of split signature along its involutions.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, 1997), for the two quaternion halves of the split biquaternion algebra and its sectors.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for coordinate-block decompositions of Clifford algebras and the fixed spaces of their grade involutions.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Dover, 1995), for the general theory of the Jordan and Lie structures carried by the symmetric and antisymmetric parts of an algebra with an involution.
