
# __Comparison of Subspaces and Involutions__

## Introduction

This article compares the involutions of the eight algebras $\mathbb{R}, \mathbb{C}, \mathbb{D}, \mathbb{D}', \mathbb{H}, \mathbb{H}_{\mathrm{s}}, \mathbb{B}, \mathbb{H}_{\mathbb{D}}$ and the real vector subspaces those involutions cut out. It states the involution group of each algebra and its rank, the fixed and anti-fixed subspaces and their dimensions, the lattice of distinguished subspaces and the inclusion relations among them, which of the subspaces are subalgebras and which are not, and the centre, vector, quaternion and Hermitian subspaces of the two biquaternion systems, in tables with the eight algebras as columns in the fixed order of *The Eight Algebras Compared*. Every entry restates a result of the subspace articles cited in the explanations, and the empty places of $\mathbb{R}$, which has no non-trivial involution, are stated and explained rather than omitted.

The organising thread is the **number of involutions**: one for $\mathbb{R}$ (the identity alone), two for each of the two-dimensional algebras, three for the quaternion systems, and four for the two biquaternion systems. The subspace family grows with it: a two-element decomposition in $\mathbb{C}$, $\mathbb{D}$ and $\mathbb{D}'$, a two-subspace decomposition in $\mathbb{H}$, a four-subspace family in $\mathbb{H}_{\mathrm{s}}$, a six-subspace lattice in $\mathbb{B}$ and a four-subspace family in $\mathbb{H}_{\mathbb{D}}$. The last rung is where the family does **not** grow further, because the split complex scalar line and the isometric copy of the quaternion subspace replace the complex scalar line and the negative-definite anti-quaternion subspace of $\mathbb{B}$.

## The Involution Groups

The following table compares the involutions of the eight algebras and the group they generate: the number of conjugations, the abstract group, its rank, a generating set and whether the conjugations commute. The eight algebras are the columns, in the fixed order.

| datum | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|---|---|---|---|
| conjugations | $1$ | $2$ | $2$ | $2$ | $3$ | $3$ | $4$ | $4$ |
| involution group | trivial | $\mathbb{Z}/2$ | $\mathbb{Z}/2$ | $\mathbb{Z}/2$ | $(\mathbb{Z}/2)^2$ | $(\mathbb{Z}/2)^2$ | $(\mathbb{Z}/2)^2$ | $(\mathbb{Z}/2)^2$ |
| rank | $0$ | $1$ | $1$ | $1$ | $2$ | $2$ | $2$ | $2$ |
| generators | — | $\bar{\cdot}$ | $\bar{\cdot}$ | $\bar{\cdot}$ | $\bar{\cdot},-\mathrm{id}$ | $\alpha,\rho$ | $\bar{\cdot},{}^{*}$ | $\bar{\cdot},{}^{*}$ |
| commuting | trivial | yes | yes | yes | yes | yes | yes | yes |

The table records the first structural change of the category. In $\mathbb{R}$ the only conjugation is the identity, so the involution group is trivial and all the subspace rows below are empty for this column. Each two-dimensional algebra carries exactly one non-trivial involution: complex conjugation in $\mathbb{C}$ (*Complex Subspaces*, §*The Involutions and the Two Decompositions*), the conjugation $\bar Z = a-jb$ in $\mathbb{D}$, which coincides with the idempotent conjugation (*Split-Complex Subspaces*, §*The Two Involutions*), and dual conjugation in $\mathbb{D}'$ (*Dual-Number Subspaces*, §*The Decompositions*). The quaternion algebra carries three conjugations — quaternion conjugation $\bar{\cdot}$, vector conjugation $-\bar{\cdot}$ and total conjugation $-\mathrm{id}$ — and they generate the Klein four-group, so that the rank jumps to $2$ (*The Scalar and Vector Subspaces of $\mathbb{H}$*, §*Definition and Basis*). The split quaternions carry three involutions in a different configuration: the conjugation $\bar{\cdot}$, the principal involution $\alpha$ and the reversal $\rho$, related by $\bar{\cdot}=\alpha\rho$, so that $\alpha$ and $\rho$ generate and the group is again $(\mathbb{Z}/2)^2$ (*Split-Quaternion Involution Lattice*, §*The Group They Generate*). The last two columns carry four conjugations each — $\bar{\cdot}$, ${}^{*}$, ${}^{\dagger}$ and $\flat$ — of which the first three generate a Klein four-group and the fourth is the negative of ${}^{\dagger}$, so that four listed conjugations still give a group of order four (*The Group of Involutions*; *Split-Biquaternion Involution Lattice*, §*The Four Conjugations*). In the last two columns the conjugation group is the same abstract group as in $\mathbb{H}$ and $\mathbb{H}_{\mathrm{s}}$; what grows is not the group but the number of fixed spaces it cuts out, and the scalar line ceases to be the whole centre.

## The Fixed and Anti-Fixed Subspaces

The following table compares the fixed and anti-fixed subspaces of the main conjugation of each algebra: the subspace, its real dimension, and whether the two together span the algebra. The eight algebras are the columns, in the fixed order.

| datum | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|---|---|---|---|
| fixed subspace | $\mathbb{R}$ | $\mathbb{R}_{\mathbb{C}}$ | $\mathbb{R}_{\mathbb{D}}$ | $\mathbb{R}_{\mathbb{D}'}$ | $\mathbb{R}_{\mathbb{H}}$ | $S$ | $\mathbb{C}_{\mathbb{B}}$ | $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ |
| anti-fixed subspace | $\{0\}$ | $i\mathbb{R}_{\mathbb{C}}$ | $j\mathbb{R}_{\mathbb{D}}$ | $\varepsilon\mathbb{R}_{\mathbb{D}'}$ | $\operatorname{Im}\mathbb{H}$ | $V$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$ |
| dimension of the fixed space | $1$ | $1$ | $1$ | $1$ | $1$ | $1$ | $2$ | $2$ |
| dimension of the anti-fixed space | $0$ | $1$ | $1$ | $1$ | $3$ | $3$ | $6$ | $6$ |
| the two span the algebra | yes | yes | yes | yes | yes | yes | yes | yes |

The table shows the shape of the main decomposition of each algebra. In $\mathbb{R}$, $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$, $\mathbb{H}$ and $\mathbb{H}_{\mathrm{s}}$ the fixed space is one-dimensional, the scalar line; the anti-fixed space is the imaginary line in $\mathbb{C}$, $\mathbb{D}$ and $\mathbb{D}'$ and the three-dimensional vector space in $\mathbb{H}$ (*Complex Subspaces*, §*The Two Subspaces at a Glance*; *Split-Complex Subspaces*, §*The Distinguished Subspaces at a Glance*; *Dual-Number Subspaces*, §*The Two Submodules at a Glance*; *The Scalar and Vector Subspaces of $\mathbb{H}$*, §*The Two-Subspace Lattice and the Absence of the Full Lattice*). The last two columns are where the fixed space grows: the centre of $\mathbb{B}$ is the complex line $\mathbb{C}_{\mathbb{B}}$, of real dimension two, and the centre of $\mathbb{H}_{\mathbb{D}}$ is the split complex line $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, also of dimension two; correspondingly the anti-fixed space of $\mathbb{H}$ and $\mathbb{H}_{\mathrm{s}}$, of dimension three, is replaced by the complex vector space $\mathrm{Vect}(\mathbb{B})$ of real dimension six in $\mathbb{B}$ and by the split complex vector space $\mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$ of the same real dimension six in $\mathbb{H}_{\mathbb{D}}$ (*Introduction to the Six Subspaces*; *Split-Biquaternion Relations Between Subspaces*, §*The Four Subspaces at a Glance*). The anti-fixed spaces of $\mathbb{B}$ and $\mathbb{H}_{\mathbb{D}}$ are the largest of the table, of real dimension six, because the complex or split complex coefficients double each vector coordinate. The empty cell of the anti-fixed row in the column $\mathbb{R}$ is genuine: the identity involution has no anti-fixed element but the origin, and $\mathbb{R}$ has no non-trivial involution from which a second decomposition could be drawn.

## The Distinguished Subspaces

The following table compares the lattice of distinguished subspaces of the eight algebras: one row per family and the dimension of the subspace in parentheses, with the marker **—** where the family does not occur. The eight algebras are the columns, in the fixed order.

| subspace | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|---|---|---|---|
| scalar / centre | $\mathbb{R}$ (1) | $\mathbb{R}_{\mathbb{C}}$ (1) | $\mathbb{R}_{\mathbb{D}}$ (1) | $\mathbb{R}_{\mathbb{D}'}$ (1) | $\mathbb{R}_{\mathbb{H}}$ (1) | $S$ (1) | $\mathbb{C}_{\mathbb{B}}$ (2) | $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ (2) |
| vector | — | $i\mathbb{R}_{\mathbb{C}}$ (1) | $j\mathbb{R}_{\mathbb{D}}$ (1) | $\varepsilon\mathbb{R}_{\mathbb{D}'}$ (1) | $\operatorname{Im}\mathbb{H}$ (3) | $V$ (3) | $\mathrm{Vect}(\mathbb{B})$ (6) | $\mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$ (6) |
| quaternion | — | — | — | — | $\mathbb{H}$ (4) | $\mathbb{H}_{\mathrm{s}}$ (4) | $\mathbb{H}_{\mathbb{B}}$ (4) | $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ (4) |
| anti-quaternion | — | — | — | — | — | — | $i\mathbb{H}_{\mathbb{B}}$ (4) | $j\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ (4) |
| Hermitian | — | — | — | — | — | — | $\mathbb{M}_+$ (4) | $\mathbb{M}_+$ (4) |
| anti-Hermitian | — | — | — | — | — | — | $\mathbb{M}_-$ (4) | $\mathbb{M}_-$ (4) |
| extra split-complex subspaces | — | — | $\mathbb{R}\Pi_1,\mathbb{R}\Pi_2$ (1,1) | — | — | $\mathbb{D}_2,\mathbb{D}_3$ (2,2) | — | — |

The table is the lattice of the category, and it has two halves. The lower-dimensional columns carry only the scalar–vector pair, or, in $\mathbb{D}$ and $\mathbb{H}_{\mathrm{s}}$, additional split-complex planes that are not fixed spaces of any involution: in $\mathbb{D}$ the two isotropic lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$, which refine the eigenline decomposition $\mathbb{R}_{\mathbb{D}}\oplus j\mathbb{R}_{\mathbb{D}}$ (*Split-Complex Subspaces*, §*The Four Coordinate Lines*), and in $\mathbb{H}_{\mathrm{s}}$ the two planes $\mathbb{D}_2=\langle 1,e_2\rangle$ and $\mathbb{D}_3=\langle 1,e_3\rangle$, each isomorphic to $\mathbb{D}$, alongside the scalar line $S$ and the vector space $V$ (*Split-Quaternion Relations Between Subspaces*, §*The Four Subspaces at a Glance*). The four- and eight-dimensional columns carry a quaternion and a Hermitian family as well: in $\mathbb{H}$ and $\mathbb{H}_{\mathrm{s}}$ the whole algebra plays the role of the quaternion space, while in $\mathbb{B}$ the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ is the fixed space of ${}^{*}$ and the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ its anti-fixed space, and the Hermitian and anti-Hermitian subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$ are the fixed and anti-fixed spaces of ${}^{\dagger}$ (*Introduction to the Six Subspaces*). The reduction of the family at the last rung is stated in the table: $\mathbb{H}_{\mathbb{D}}$ names four distinguished subspaces and not six, its vector space $\mathrm{Vect}(\mathbb{H}_{\mathbb{D}})$ being the six-dimensional complement of the centre, fixed by none of the four involutions, and its anti-quaternion space $j\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ being isometric to the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ under $j^2=+1$, whereas the corresponding space $i\mathbb{H}_{\mathbb{B}}$ of $\mathbb{B}$ is negative definite and genuinely new (*Split-Biquaternion Involution Lattice*, §*The Lattice of Fixed Spaces*). The empty cells of $\mathbb{R}$ are the lattice consequence of the trivial involution group: with no non-trivial involution there is no anti-fixed space, no vector space and no Hermitian family, and only the scalar row is occupied.

## Subalgebras, Ideals and Products

The following table compares which of the distinguished subspaces are subalgebras, which are ideals and which are neither, with the marker **—** where the family does not occur and "not closed" for a subspace whose product leaves it. The eight algebras are the columns, in the fixed order.

| status | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|---|---|---|---|
| scalar / centre | subalgebra | subalgebra | subalgebra | subalgebra | subalgebra | subalgebra | subalgebra | subalgebra |
| vector | — | not closed | not closed | ideal, not subalgebra | not closed | not closed | not closed | not closed |
| quaternion | — | — | — | — | subalgebra | subalgebra | subalgebra | subalgebra |
| Hermitian | — | — | — | — | — | — | not closed | not closed |
| anti-Hermitian | — | — | — | — | — | — | not closed | not closed |
| extra split-complex subspaces | — | — | subalgebra, ideal | — | — | subalgebra | — | — |

The table shows that the scalar line is a subalgebra in every column and is the only family that is one throughout. The vector subspace is closed under multiplication in no column: in $\mathbb{C}$, $\mathbb{D}$, $\mathbb{H}$ and $\mathbb{H}_{\mathrm{s}}$ the product of two anti-fixed elements is real or scalar, the fundamental instances being $(ib)(ic)=-bc$ in $\mathbb{C}$ and $\mathbf{p}\mathbf{q}=-\langle\mathbf{p},\mathbf{q}\rangle+\mathbf{p}\times\mathbf{q}$ in $\operatorname{Im}\mathbb{H}$ (*Complex Subspaces*, §*How the Operations Act on the Splits*; *The Scalar and Vector Subspaces of $\mathbb{H}$*, §*Algebra and Module Structure*). The dual case is the exception of a kind: the infinitesimal submodule $\varepsilon\mathbb{R}_{\mathbb{D}'}$ is closed under multiplication because $\varepsilon^2=0$, but it contains no identity and is the maximal ideal $\mathrm{M}$, so it is an ideal and not a subalgebra (*Dual-Number Subspaces*, §*How the Operations Act on the Splits*). The quaternion subspace is a subalgebra wherever it is a proper subspace, a copy of $\mathbb{H}$ in $\mathbb{B}$ and in $\mathbb{H}_{\mathbb{D}}$; the Hermitian and anti-Hermitian subspaces of the two biquaternion systems are not closed, their products landing in $\mathbb{R}\oplus\mathrm{Vect}$ or in $j\mathbb{R}\oplus\mathrm{Vect}$, but each is closed under the symmetrised product and so carries a Jordan algebra structure (*The Six Subspaces and the Four Complex Products*; *Split-Biquaternion Relations Between Subspaces*, §*How the Operations Act on the Splits*). The additional split-complex planes of $\mathbb{D}$ and $\mathbb{H}_{\mathrm{s}}$ are subalgebras isomorphic to $\mathbb{D}$, and those of $\mathbb{D}$ are in addition the two minimal ideals, the algebra being $\mathbb{R}\oplus\mathbb{R}$ (*Split-Complex Algebra*, §*The Idempotent Decomposition*; *Split-Quaternion Relations Between Subspaces*, §*How the Product and the Commutator Act*).

## The Two Biquaternion Systems

The two biquaternion columns of the lattice are the ones that carry the full family, and their contrast is the content of the last rung. In $\mathbb{B}$ the four conjugations cut out six subspaces over four coordinate blocks — the two scalar lines $\langle e_0\rangle$ and $\langle ie_0\rangle$ and the two vector triples $\langle e_1,e_2,e_3\rangle$ and $\langle ie_1,ie_2,ie_3\rangle$ — and the intersections of the six subspaces are sums of the blocks, of dimension $0$, $1$ or $3$ (*Comparison of the Six Subspaces*, §*The Six Subspaces and the Coordinate Blocks*; §*The Intersections*). In $\mathbb{H}_{\mathbb{D}}$ the same conjugation group cuts out four named subspaces over the analogous four blocks, the real and split-imaginary scalar lines and the real and split-imaginary vector triples, and two subspaces meet in the sum of the blocks they share (*Split-Biquaternion Relations Between Subspaces*, §*The Four Coordinate Blocks*; §*The Intersections*). Multiplication by the central unit acts differently in the two systems: in $\mathbb{B}$ multiplication by $i$ preserves the centre and the vector subspace and exchanges the quaternion with the anti-quaternion subspace and the two sectors, while in $\mathbb{H}_{\mathbb{D}}$ the split complex unit $j$ satisfies $j^2=+1$ and the anti-quaternion space is the isometric copy $j\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ of the quaternion space rather than a new sector. This is the single place where the lattice of the last rung is smaller than the lattice of the rung below, and it is the lattice form of the difference between the central units $i$ and $j$: a complex central unit gives a negative-definite anti-quaternion subspace, a split central unit does not.

## Summary

The eight algebras carry a ladder of involution groups: the trivial group for $\mathbb{R}$, a $\mathbb{Z}/2$ for each of $\mathbb{C}, \mathbb{D}, \mathbb{D}'$, and a Klein four-group $(\mathbb{Z}/2)^2$ for $\mathbb{H}, \mathbb{H}_{\mathrm{s}}, \mathbb{B}, \mathbb{H}_{\mathbb{D}}$, generated in the quaternion case by $\bar{\cdot}$ and $-\mathrm{id}$, in the split quaternion case by $\alpha$ and $\rho$, and in the biquaternion cases by $\bar{\cdot}$ and ${}^{*}$, with ${}^{\dagger}={}^{*}\circ\bar{\cdot}$ and $\flat=-{}^{\dagger}$ in both. The fixed space of the main conjugation is one-dimensional up to $\mathbb{H}_{\mathrm{s}}$ and two-dimensional in the two biquaternion systems, where it is the complex and the split complex centre; the anti-fixed space grows from $0$ in $\mathbb{R}$ through $1$ in the two-dimensional systems and $3$ in $\mathbb{H}$ and $\mathbb{H}_{\mathrm{s}}$ to $6$ in $\mathbb{B}$ and $\mathbb{H}_{\mathbb{D}}$. The lattice of distinguished subspaces has two members in $\mathbb{C}$, $\mathbb{D}$ and $\mathbb{D}'$ (with the two isotropic lines of $\mathbb{D}$ refining them), two in $\mathbb{H}$, four in $\mathbb{H}_{\mathrm{s}}$, six in $\mathbb{B}$ and four in $\mathbb{H}_{\mathbb{D}}$, the last rung being smaller than the one below because the split anti-quaternion space is isometric to the quaternion space. The scalar line is a subalgebra in every column, the vector subspace is closed in none, the dual infinitesimal submodule is an ideal rather than a subalgebra, the quaternion subspace is a subalgebra wherever it is proper, and the Hermitian and anti-Hermitian subspaces of the two biquaternion systems are not subalgebras but each carries a symmetrised-product Jordan structure. The empty places of $\mathbb{R}$ — the anti-fixed space, the vector subspace and every higher family — are the consequence of its trivial involution group and are stated in each table.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\sigma$ | a general involution, an order-two linear or anti-linear map |
| $\operatorname{id}$ | the identity, the sole conjugation of $\mathbb{R}$ |
| $\bar{\cdot}$ | quaternion or complex conjugation, negating the vector part |
| ${}^{*}$ | complex or split complex conjugation of coefficients |
| ${}^{\dagger}=\bar{\cdot}\circ{}^{*}$ | Hermitian conjugation |
| $\flat=-{}^{\dagger}$ | reversal, the negative of Hermitian conjugation |
| $\alpha$ | the principal involution of $\mathbb{H}_{\mathrm{s}}$ |
| $\rho$ | the reversal of $\mathbb{H}_{\mathrm{s}}$, $\bar{\cdot}=\alpha\rho$ |
| $\mathbb{R}_{\mathbb{C}},i\mathbb{R}_{\mathbb{C}}$ | real and imaginary subspaces of $\mathbb{C}$ |
| $\mathbb{R}_{\mathbb{D}},j\mathbb{R}_{\mathbb{D}},\mathbb{R}\Pi_{1,2}$ | real, split imaginary and idempotent lines of $\mathbb{D}$ |
| $\mathbb{R}_{\mathbb{D}'},\varepsilon\mathbb{R}_{\mathbb{D}'},\mathrm{M}$ | real and infinitesimal submodules of $\mathbb{D}'$ and its maximal ideal |
| $\mathbb{R}_{\mathbb{H}},\operatorname{Im}\mathbb{H}$ | scalar and vector subspaces of $\mathbb{H}$ |
| $S,V,\mathbb{D}_2,\mathbb{D}_3$ | scalar, vector and split-complex subspaces of $\mathbb{H}_{\mathrm{s}}$ |
| $\mathbb{C}_{\mathbb{B}},\mathrm{Vect}(\mathbb{B}),\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}},\mathbb{M}_\pm$ | the six subspaces of $\mathbb{B}$ |
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}},\mathrm{Vect}(\mathbb{H}_{\mathbb{D}}),\mathbb{H}_{\mathbb{H}_{\mathbb{D}}},j\mathbb{H}_{\mathbb{H}_{\mathbb{D}}},\mathbb{M}_\pm$ | the subspaces of $\mathbb{H}_{\mathbb{D}}$ |
| $(\mathbb{Z}/2)^2$ | the Klein four-group generated by the conjugations |
| `—` | an empty cell, stated and never filled |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the decomposition of an algebra into the eigenspaces of an involution and the Peirce decomposition of it.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras*, American Mathematical Society Colloquium Publications 39 (1968), for the symmetrised product and the Jordan structure of a subspace that is not a subalgebra.
- John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288 (Springer, 2021), for the scalar–vector decomposition, conjugation and the subalgebras of a quaternion algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the grading and the involutions of the low-dimensional Clifford algebras.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the subspace lattices of the split and complexified forms.

