# __Subspaces and Decompositions of the Biquaternion Algebra__

## Introduction

The biquaternion algebra $\mathbb{B}$ carries four conjugations, and each of them is an involution. Each one splits $\mathbb{B}$ into the elements it fixes and the elements it reverses, and the eight spaces so obtained reduce to six distinct subspaces, the **remarkable subspaces** of $\mathbb{B}$. Three of the four conjugations give decompositions distinct in the sense that no one reproduces another, and each of the three pairs two of the six: the halves have real dimensions $2+6$, $4+4$ and $4+4$.

This article is the single article of the group for the remarkable subspaces and for the three decompositions they cut out. It defines the six subspaces one to a section, introduces the four coordinate blocks out of which they are built, establishes the three decompositions with their projection formulas, and collects the relations between the subspaces: the intersections, the sums, the action of the conjugations by signs, the lattice of the fixed spaces and the action of the complex structure. The decompositions are vector-space decompositions: they are read off the conjugations, and no product is needed. The table is the summary; the sections are the detail.

The conjugations themselves are not defined here: their formulas, the coordinates and the linear or antilinear character are in *The Element, the Coordinates and the Conjugations* and *The Biquaternion Algebra*, and the group they form is *The Group of Involutions*. What the subspaces carry beyond their linear algebra — the product, the four general products, the forms and the norms — is treated in *Remarkable Subspaces and the Four General Products, Forms and Norms*, *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra* and the *Remarkable Subspaces under ...* articles.

Nothing below is a physical statement. The elements are written $\tilde{Q}, \tilde{Q}_1, \tilde{Q}_2, \dots$, their complex coefficients $Q_t, Q_x, Q_y, Q_z$, and the real and imaginary parts of a coefficient $Q_\mu = q_\mu + i q'_\mu$; no other coordinates are used.

## The Six Remarkable Subspaces

The six subspaces are listed in the table, with their defining conditions, real bases, real dimensions and roles; each condition names the conjugation that cuts the subspace out. Each subspace is then derived in its own section.

| subspace | defining condition | real basis | $\dim_{\mathbb{R}}$ | role |
|---|---|---|---|---|
| the centre $\mathbb{C}_{\mathbb{B}}$ | $\tilde{Q}^{\natural} = \tilde{Q}$ | $e_t, ie_t$ | $2$ | the centre of the algebra, a field |
| the vector subspace $\mathrm{Vect}(\mathbb{B})$ | $\tilde{Q}^{\natural} = -\tilde{Q}$ | $\vec e_x, \vec e_y, \vec e_z, i\vec e_x, i\vec e_y, i\vec e_z$ | $6$ | the kernel of the scalar part, a Lie algebra |
| the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ | $\bar{\tilde{Q}} = \tilde{Q}$ | $e_t, \vec e_x, \vec e_y, \vec e_z$ | $4$ | a division algebra |
| the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ | $\bar{\tilde{Q}} = -\tilde{Q}$ | $ie_t, i\vec e_x, i\vec e_y, i\vec e_z$ | $4$ | $i$ times the quaternion subspace |
| the Hermitian subspace $\mathbb{M}_+$ | $\tilde{Q}^{*} = \tilde{Q}$ | $e_t, i\vec e_x, i\vec e_y, i\vec e_z$ | $4$ | the fixed space of ${}^{*}$, not a subalgebra |
| the anti-Hermitian subspace $\mathbb{M}_-$ | $\tilde{Q}^{\flat} = \tilde{Q}$ | $ie_t, \vec e_x, \vec e_y, \vec e_z$ | $4$ | a Lie algebra |

Exactly two of the remarkable subspaces are closed under the product, the centre and the quaternion subspace. The six are pairwise distinct. Their relations are read off the four coordinate blocks, which come next.

### The Centre Subspace

**Definition.** The **centre subspace** $\mathbb{C}_{\mathbb{B}}$ is the fixed space of quaternion conjugation,

$$
\mathbb{C}_{\mathbb{B}} = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{\natural} = \tilde{Q} \right\} .
$$

**Coordinate condition.** Writing $\tilde{Q} = Q_te_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$ and comparing the two sides of $\tilde{Q}^{\natural} = \tilde{Q}$ coefficient by coefficient, the coefficient of $e_t$ gives no condition while the coefficient of $\vec e_k$ gives $-Q_k = Q_k$, that is $Q_k = 0$, for $k = 1, 2, 3$. The subspace is therefore the set of elements with **vanishing vector part**,

$$
\tilde{Q} = Q_te_t , \qquad Q_t \in \mathbb{C} .
$$

**Basis and dimension.** The real basis is $e_t, ie_t$ and $\dim_{\mathbb{R}}\mathbb{C}_{\mathbb{B}} = 2$. In the eight real coordinates it is the coordinate plane $q_x = q_y = q_z = q'_x = q'_y = q'_z = 0$.

**Role.** It is the centre of the algebra, the set of elements that commute with every element, and it is a commutative subalgebra isomorphic to $\mathbb{C}$; it is one of the two remarkable subspaces closed under the product. Its elements are the **central elements**, written $Ae_t$ with $A \in \mathbb{C}$.

### The Vector Subspace

**Definition.** The **vector subspace** $\mathrm{Vect}(\mathbb{B})$ is the anti-fixed space of quaternion conjugation,

$$
\mathrm{Vect}(\mathbb{B}) = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{\natural} = -\tilde{Q} \right\} .
$$

**Coordinate condition.** Comparing coefficients, the condition is $Q_t = 0$: the scalar part vanishes, and the subspace is the kernel of the scalar-part functional $\operatorname{Sc}(\tilde{Q}) = Q_t = \tfrac{1}{2}(\tilde{Q} + \tilde{Q}^{\natural})$,

$$
\tilde{Q} = Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z , \qquad Q_x, Q_y, Q_z \in \mathbb{C} .
$$

**Basis and dimension.** The real basis is $\vec e_x, \vec e_y, \vec e_z, i\vec e_x, i\vec e_y, i\vec e_z$ and $\dim_{\mathbb{R}}\mathrm{Vect}(\mathbb{B}) = 6$. It is the largest of the remarkable subspaces, and the only one of dimension $6$.

**Role.** It is not a subalgebra, since the product of two pure vectors has a scalar part; it is closed under the commutator, the bracket of two pure vectors being twice their cross product. It splits into the real vector triple $\operatorname{span}\{\vec e_x,\vec e_y,\vec e_z\}$ and the imaginary vector triple $\operatorname{span}\{i\vec e_x,i\vec e_y,i\vec e_z\}$, and its elements are the **pure vectors**, written $\vec Q$.

### The Quaternion Subspace

**Definition.** The **quaternion subspace** $\mathbb{H}_{\mathbb{B}}$ is the fixed space of complex conjugation,

$$
\mathbb{H}_{\mathbb{B}} = \left\{ \tilde{Q} \in \mathbb{B} : \bar{\tilde{Q}} = \tilde{Q} \right\} .
$$

**Coordinate condition.** The condition is that each coefficient be fixed by complex conjugation, that is, that each be real, $Q_\mu = q_\mu$ for $\mu = 0, 1, 2, 3$.

**Basis and dimension.** The real basis is $e_t, \vec e_x, \vec e_y, \vec e_z$ and $\dim_{\mathbb{R}}\mathbb{H}_{\mathbb{B}} = 4$. It is the copy of the real quaternion algebra inside $\mathbb{B}$.

**Role.** It is a subalgebra, one of the two remarkable subspaces closed under the product, and it is a division algebra: every non-zero element is a unit. It is the only one of the remarkable subspaces that is non-commutative, and it is the image of the structure map $\mathbb{H} \to \mathbb{B}$, $h \mapsto he_t$.

### The Anti-Quaternion Subspace

**Definition.** The **anti-quaternion subspace** $i\mathbb{H}_{\mathbb{B}}$ is the anti-fixed space of complex conjugation,

$$
i\mathbb{H}_{\mathbb{B}} = \left\{ \tilde{Q} \in \mathbb{B} : \bar{\tilde{Q}} = -\tilde{Q} \right\} .
$$

**Coordinate condition.** The condition is that each coefficient be negated by complex conjugation, that is, that each be purely imaginary, $Q_\mu = iq'_\mu$ for $\mu = 0, 1, 2, 3$.

**Basis and dimension.** The real basis is $ie_t, i\vec e_x, i\vec e_y, i\vec e_z$ and $\dim_{\mathbb{R}}i\mathbb{H}_{\mathbb{B}} = 4$.

**Role.** Its elements are exactly the products $i\tilde{Q}$ with $\tilde{Q} \in \mathbb{H}_{\mathbb{B}}$, so the subspace is the image of $\mathbb{H}_{\mathbb{B}}$ under multiplication by the central imaginary unit. It is not a subalgebra — the product of two of its elements lands in the quaternion subspace — but it is stable under multiplication by $\mathbb{H}_{\mathbb{B}}$ on both sides. It splits into the imaginary scalar line $\mathbb{R}(ie_t)$ and the imaginary vector triple $\operatorname{span}\{i\vec e_x,i\vec e_y,i\vec e_z\}$.

### The Hermitian Subspace

**Definition.** The **Hermitian subspace** $\mathbb{M}_+$ is the fixed space of Hermitian conjugation,

$$
\mathbb{M}_+ = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{*} = \tilde{Q} \right\} , \qquad \tilde{Q}^{*} = \bar{\tilde{Q}}^{\natural} .
$$

**Coordinate condition.** Since ${}^{*} = \bar{\cdot}\circ{}^{\natural}$, the condition is that the scalar coefficient be real while the three vector coefficients be purely imaginary,

$$
\tilde{Q} = q_te_t + iq'_x\vec e_x + iq'_y\vec e_y + iq'_z\vec e_z , \qquad q_t, q'_x, q'_y, q'_z \in \mathbb{R} .
$$

**Basis and dimension.** The real basis is $e_t, i\vec e_x, i\vec e_y, i\vec e_z$ and $\dim_{\mathbb{R}}\mathbb{M}_+ = 4$.

**Role.** It is not a subalgebra: the plain product of two of its elements need not lie in it, while the symmetrized combination $\tfrac{1}{2}(\tilde{Q}_1\tilde{Q}_2+\tilde{Q}_2\tilde{Q}_1)$ of two of its elements does. It is the set of elements with real scalar part and purely imaginary vector part.

### The Anti-Hermitian Subspace

**Definition.** The **anti-Hermitian subspace** $\mathbb{M}_-$ is the anti-fixed space of Hermitian conjugation, which is also the fixed space of the reversal $\flat = -{}^{*}$,

$$
\mathbb{M}_- = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{*} = -\tilde{Q} \right\} = \left\{ \tilde{Q} \in \mathbb{B} : \tilde{Q}^{\flat} = \tilde{Q} \right\} .
$$

**Coordinate condition.** The condition is the reverse of the Hermitian one: the scalar coefficient is purely imaginary and the three vector coefficients are real,

$$
\tilde{Q} = iq'_te_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z , \qquad q'_t, q_x, q_y, q_z \in \mathbb{R} .
$$

**Basis and dimension.** The real basis is $ie_t, \vec e_x, \vec e_y, \vec e_z$ and $\dim_{\mathbb{R}}\mathbb{M}_- = 4$.

**Role.** It is not a subalgebra and it is not closed under the symmetrized product; it is closed under the commutator, and it is a real Lie algebra of dimension four whose centre is the line $\mathbb{R}(ie_t)$. It is the set of elements with purely imaginary scalar part and real vector part, and it is the anti-fixed space of ${}^{*}$ as well as the fixed space of $\flat$.

## The Four Coordinate Blocks

The relations between the remarkable subspaces are read off from four subspaces of $\mathbb{B}$, the **coordinate blocks**, into which the eight real coordinates group.

**Definition.** The **coordinate blocks** are the four real subspaces

$$
A_1 = \mathbb{R}e_t , \qquad A_2 = \mathbb{R}(ie_t) , \qquad
B_1 = \operatorname{span}_{\mathbb{R}}\{\vec e_x, \vec e_y, \vec e_z\} , \qquad B_2 = \operatorname{span}_{\mathbb{R}}\{i\vec e_x, i\vec e_y, i\vec e_z\} ,
$$

the two **scalar blocks** $A_1, A_2$ of dimension $1$ and the two **vector blocks** $B_1, B_2$ of dimension $3$. They are the pieces into which the eight real coordinates of $\mathbb{B}$ group: the two scalar blocks carry the two real coordinates of the scalar coefficient $Q_t$, and the two vector blocks the six real coordinates of the vector part.

Under the identification $\mathbb{B}\cong\mathrm{Cl}_{3,0}$, $\gamma_k\mapsto i\vec e_k$, the four blocks are the four Clifford grades:

| block | $A_1$ | $B_2$ | $B_1$ | $A_2$ |
|---|---|---|---|---|
| grade | $0$ | $1$ | $2$ | $3$ |
| basis | $e_t$ | $i\vec e_x,i\vec e_y,i\vec e_z$ | $\vec e_x,\vec e_y,\vec e_z$ | $ie_t$ |

grade zero is the real scalar line, grade one the imaginary pure quaternions, grade two the real pure quaternions and grade three the imaginary scalar line, so that the quaternion vector part is the grade-two part while the geometric vectors of the Clifford reading are the grade-one part; the two names do not agree, and the literature on the algebra records the trap. The table of sums below is therefore a table of sums of grades,

$$
\boxed{\; \mathbb{C}_{\mathbb{B}}=\text{grade }0\oplus\text{grade }3, \quad \mathrm{Vect}(\mathbb{B})=\text{grade }1\oplus\text{grade }2, \quad \mathbb{H}_{\mathbb{B}}=\text{grade }0\oplus\text{grade }2 \;},
$$
$$
\boxed{\; i\mathbb{H}_{\mathbb{B}}=\text{grade }1\oplus\text{grade }3, \quad \mathbb{M}_+=\text{grade }0\oplus\text{grade }1, \quad \mathbb{M}_-=\text{grade }2\oplus\text{grade }3 \;}.
$$

Each block is the intersection of the three subspaces that contain it:

| block | basis | $\dim_{\mathbb{R}}$ | it is the intersection |
|---|---|---|---|
| $A_1$ | $e_t$ | $1$ | $\mathbb{C}_{\mathbb{B}} \cap \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+$ |
| $A_2$ | $ie_t$ | $1$ | $\mathbb{C}_{\mathbb{B}} \cap i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$ |
| $B_1$ | $\vec e_x, \vec e_y, \vec e_z$ | $3$ | $\mathrm{Vect}(\mathbb{B}) \cap \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$ |
| $B_2$ | $i\vec e_x, i\vec e_y, i\vec e_z$ | $3$ | $\mathrm{Vect}(\mathbb{B}) \cap i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+$ |

**Theorem.** Each of the remarkable subspaces is the sum of two blocks:

| subspace | blocks | $\dim_{\mathbb{R}}$ |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $A_1 \oplus A_2$ | $2$ |
| $\mathrm{Vect}(\mathbb{B})$ | $B_1 \oplus B_2$ | $6$ |
| $\mathbb{H}_{\mathbb{B}}$ | $A_1 \oplus B_1$ | $4$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $A_2 \oplus B_2$ | $4$ |
| $\mathbb{M}_+$ | $A_1 \oplus B_2$ | $4$ |
| $\mathbb{M}_-$ | $A_2 \oplus B_1$ | $4$ |

**Proof.** Each subspace is defined by conditions on the real coordinates: the centre by the vanishing of the six vector coordinates, the vector subspace by the vanishing of the two scalar ones, the quaternion subspace by the vanishing of the three imaginary parts of the vector coordinates and of the imaginary part of the scalar one, and the other three by the corresponding sign choices. Reading the conditions block by block gives the table.

## The Three Decompositions

Each conjugation is an involution, so each divides $\mathbb{B}$ into its fixed space and its anti-fixed space, and the two are complementary. The three pairwise commuting conjugations $\bar{\cdot}$, ${}^{*}$ and ${}^{\natural}$ give the three decompositions of the algebra:

| involution | fixed space | anti-fixed space | decomposition |
|---|---|---|---|
| quaternion conjugation ${}^{\natural}$ | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$ |
| complex conjugation $\bar{\cdot}$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$ |
| Hermitian conjugation ${}^{*}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ | $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ |

The reversal $\flat = -{}^{*}$ gives no fourth: its two spaces are those of ${}^{*}$ in the other order, and the argument is in §*Why There Are Exactly Three*.

### The Centre and Vector Decomposition

The quaternion conjugation ${}^{\natural}$ is one of the three commuting involutions. Its fixed space is the centre $\mathbb{C}_{\mathbb{B}}$ and its anti-fixed space is the vector subspace $\mathrm{Vect}(\mathbb{B})$, of real dimensions 2 and 6. Every biquaternion therefore decomposes uniquely as a scalar plus a pure vector part:

$$
\tilde{Q} = \tilde{Q}_{\mathrm{c}} + \tilde{Q}_{\mathrm{v}}, \qquad \tilde{Q}_{\mathrm{c}} = Q_t e_t \in \mathbb{C}_{\mathbb{B}}, \quad \tilde{Q}_{\mathrm{v}} = Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z \in \mathrm{Vect}(\mathbb{B}),
$$

with

$$
\tilde{Q}_{\mathrm{c}} = \frac{1}{2}(\tilde{Q} + \tilde{Q}^{\natural}), \qquad \tilde{Q}_{\mathrm{v}} = \frac{1}{2}(\tilde{Q} - \tilde{Q}^{\natural}).
$$

This gives the direct sum decomposition

$$
\boxed{\; \mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B}) \;},
$$

the two summands being of real dimensions 2 and 6. It is the decomposition into scalar and vector parts, and it is the one with summands of unequal dimension: the other two decompositions split $\mathbb{B}$ into two halves of dimension 4.

### The Quaternion Decomposition

The complex conjugation $\bar{\cdot}$ is an involution, and the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ are its fixed and anti-fixed spaces: $\mathbb{H}_{\mathbb{B}}$ is fixed and $i\mathbb{H}_{\mathbb{B}}$ is reversed. Both have real dimension 4, and they are independent, so $\mathbb{B}$ splits as a direct sum of the two.

Every biquaternion can be written uniquely as

$$
\tilde{Q} = \tilde{Q}_r + i \tilde{Q}_i,
$$

where $\tilde{Q}_r$ and $\tilde{Q}_i$ are **ordinary quaternions** (elements of $\mathbb{H}$ embedded in $\mathbb{B}$), with real coefficients. The two components are

$$
\tilde{Q}_r = \frac{1}{2}(\tilde{Q} + \bar{\tilde{Q}}), \qquad \tilde{Q}_i = \frac{1}{2i}(\tilde{Q} - \bar{\tilde{Q}}).
$$

Indeed, $\tilde{Q}_r$ is fixed by complex conjugation, so it lies in the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, and $\tilde{Q}_i$ is also fixed by complex conjugation. To see the latter, compute

$$
\bar{\tilde{Q}_i} = \overline{\left(\frac{1}{2i}(\tilde{Q} - \bar{\tilde{Q}})\right)} = \frac{-1}{2i}\left(\bar{\tilde{Q}} - \tilde{Q}\right) = \frac{1}{2i}\left(\tilde{Q} - \bar{\tilde{Q}}\right) = \tilde{Q}_i,
$$

so $\tilde{Q}_i$ lies in $\mathbb{H}_{\mathbb{B}}$ as well. The sum is $\tilde{Q}_r + i \tilde{Q}_i = \tilde{Q}$.

This gives the direct sum decomposition

$$
\boxed{\; \mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i \mathbb{H}_{\mathbb{B}} \;},
$$

where $i\mathbb{H}_{\mathbb{B}}$ is the set of biquaternions of the form $i \tilde{Q}$ with $\tilde{Q} \in \mathbb{H}_{\mathbb{B}}$. Both are real vector spaces of dimension 4, and their direct sum is the full algebra $\mathbb{B}$ of real dimension 8.

This is the **quaternion decomposition** of a biquaternion. It expresses $\tilde{Q}$ as a quaternion plus the scalar imaginary times another quaternion. It is the natural decomposition when we think of $\mathbb{B}$ as the complexification of $\mathbb{H}$: the first summand is the "real part" and the second is the "imaginary part" of the complexification.

### The Hermitian Decomposition

The Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$ are the fixed and anti-fixed spaces of the Hermitian conjugation ${}^{*}$. Every biquaternion decomposes uniquely as the sum of a Hermitian part and an anti-Hermitian part:

$$
\tilde{Q} = \tilde{Q}_+ + \tilde{Q}_-, \qquad \tilde{Q}_+ \in \mathbb{M}_+, \quad \tilde{Q}_- \in \mathbb{M}_-.
$$

The two components are obtained from the Hermitian conjugation:

$$
\tilde{Q}_+ = \frac{1}{2}(\tilde{Q} + \tilde{Q}^{*}), \qquad \tilde{Q}_- = \frac{1}{2}(\tilde{Q} - \tilde{Q}^{*}).
$$

Indeed, $\tilde{Q}_+$ is fixed by Hermitian conjugation, so it lies in $\mathbb{M}_+$, and $\tilde{Q}_-$ satisfies $\tilde{Q}_-^{*} = -\tilde{Q}_-$, so it lies in $\mathbb{M}_-$. The sum is $\tilde{Q}_+ + \tilde{Q}_- = \tilde{Q}$.

This gives the direct sum decomposition

$$
\boxed{\; \mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_- \;},
$$

where $\mathbb{M}_+$ is the Hermitian subspace and $\mathbb{M}_-$ is the anti-Hermitian subspace. Both are real vector spaces of dimension 4, and their direct sum is the full algebra $\mathbb{B}$ of real dimension 8.

The decomposition is the algebraic analogue of writing a complex number as the sum of its real and imaginary parts. Here, however, both components are biquaternions, and the two subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$ are not subalgebras of $\mathbb{B}$; the decomposition is a vector-space decomposition, not an algebra decomposition.

## Why There Are Exactly Three

The three commuting involutions $\bar{\cdot}$, ${}^{*}$ and ${}^{\natural}$ give the three decompositions above. The fourth conjugation, the reversal $\flat = -{}^{*}$, adds no fourth: its fixed space is $\mathbb{M}_-$ and its anti-fixed space is $\mathbb{M}_+$, the two spaces of ${}^{*}$ with the signs exchanged, so it cuts the algebra along the same pair.

The reason the count is three and not four is visible over the four coordinate blocks. Each four-dimensional remarkable subspace takes one scalar block and one vector block, and the centre and the vector subspace take the two scalar and the two vector blocks. The three decompositions are exactly the three ways of splitting the four blocks into two complementary pairs: $\{A_1, B_1\}$ against $\{A_2, B_2\}$ gives the quaternion decomposition, $\{A_1, B_2\}$ against $\{A_2, B_1\}$ gives the Hermitian one, and $\{A_1, A_2\}$ against $\{B_1, B_2\}$ gives the centre–vector one. A four-element set has exactly three pairings into two pairs, which is why there are exactly three decompositions. The six subspaces are the two sums of two like blocks, the centre and the vector subspace, and the four sums of one scalar and one vector block.

The same count is read from the tables below: the pairs of distinct subspaces that meet in the origin, and the pairs whose sum is the whole algebra, are exactly the three decomposition pairs, and no other pair has either property.

## The Intersections

**Theorem.** Two distinct remarkable subspaces meet in the blocks they have in common; consequently the dimension of their intersection is $0$, $1$ or $3$, and never $2$, $4$, $5$ or $6$.

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
- The centre meets each of the other four subspaces in a scalar line: $A_1 = \mathbb{R}e_t$ with the quaternion and Hermitian subspaces, $A_2 = \mathbb{R}(ie_t)$ with the anti-quaternion and anti-Hermitian ones.
- The vector subspace meets each of the other four in a vector triple: $B_1$ with the quaternion and anti-Hermitian subspaces, $B_2$ with the anti-quaternion and Hermitian ones.

In particular, no two of the remarkable subspaces are equal, since equal subspaces would meet in their common dimension, and no off-diagonal entry of the table is $2$, $4$ or $6$.

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

## The Involutions as Sign Patterns

Each of the four conjugations preserves each of the remarkable subspaces, since it commutes with the three commuting involutions that define them, and its restriction to a subspace is diagonal in the real basis of that subspace with signs $+1$ and $-1$ only. The following table records, for each conjugation and each subspace, the multiplicity of the sign $-1$, written as a fraction of the dimension.

| conjugation | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
|---|---|---|---|---|---|---|
| ${}^{\natural}$ | $0$ of $2$ | $6$ of $6$ | $3$ of $4$ | $3$ of $4$ | $3$ of $4$ | $3$ of $4$ |
| $\bar{\cdot}$ | $1$ of $2$ | $3$ of $6$ | $0$ of $4$ | $4$ of $4$ | $3$ of $4$ | $1$ of $4$ |
| ${}^{*}$ | $1$ of $2$ | $3$ of $6$ | $3$ of $4$ | $1$ of $4$ | $0$ of $4$ | $4$ of $4$ |
| $\flat$ | $1$ of $2$ | $3$ of $6$ | $1$ of $4$ | $3$ of $4$ | $4$ of $4$ | $0$ of $4$ |

The eight cells in which the restriction is the identity or its negative are the definitions of the remarkable subspaces read back: ${}^{\natural}$ acts as the identity exactly on the centre and as its negative exactly on the vector subspace; $\bar{\cdot}$ exactly on the quaternion subspace and its negative exactly on the anti-quaternion one; ${}^{*}$ exactly on $\mathbb{M}_+$ and its negative exactly on $\mathbb{M}_-$; and $\flat$ exactly on $\mathbb{M}_-$ and its negative exactly on $\mathbb{M}_+$. The mixed cells, which are neither $0$ nor the full dimension, are the restrictions that are neither the identity nor its negative; each of them is fixed by the block membership of the subspace, since a conjugation negates a block as a whole.

The table also exhibits the composition rule ${}^{*} = \bar{\cdot}\circ{}^{\natural}$. The coordinates negated by ${}^{*}$ are exactly those negated by one of $\bar{\cdot}$ and ${}^{\natural}$ but not by both, so the multiplicities compose by symmetric difference. On the quaternion subspace, for instance, $\bar{\cdot}$ negates none of the four coordinates and ${}^{\natural}$ negates the three vector ones, so ${}^{*}$ negates the same three and the multiplicity is $3$; on $\mathbb{M}_+$, $\bar{\cdot}$ and ${}^{\natural}$ negate the same three coordinates, and those cancel, leaving multiplicity $0$.

Two consequences follow from the table alone. First, no subspace other than the centre is fixed pointwise by more than one of the four conjugations, and the remarkable subspaces are pairwise distinct as sets. Second, a subspace is fixed pointwise by exactly those conjugations whose multiplicity of $-1$ on it vanishes.

## The Lattice of the Fixed Spaces

The three decompositions of §*The Three Decompositions* come from the three involutions ${}^{\natural}$, $\bar{\cdot}$ and ${}^{*}$. Including the reversal $\flat=-{}^{*}$ gives four involutions and, for each, a fixed and an anti-fixed space; the reversal has the same two spaces as ${}^{*}$ with the signs exchanged, so eight labelled spaces reduce to the remarkable subspaces.

| involution | fixed space | anti-fixed space | generated by |
|---|---|---|---|
| ${}^{\natural}$ | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}(\mathbb{B})$ | the complex structure and the vector structure |
| $\bar{\cdot}$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | the real structure |
| ${}^{*}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ | the Hermitian structure |
| $\flat$ | $\mathbb{M}_-$ | $\mathbb{M}_+$ | the reversal |

Only the Hermitian pair is counted twice, since $\{\tilde Q:\tilde Q^{\flat}=\tilde Q\}=\mathbb{M}_-$ and $\{\tilde Q:\tilde Q^{\flat}=-\tilde Q\}=\mathbb{M}_+$ are the fixed and anti-fixed equations of ${}^{*}$ read with the opposite labels.

Over the coordinate blocks the subspaces sit at the following levels of dimension, ordered from the whole algebra down to the origin:

| level | subspaces |
|---|---|
| $\mathbb{B}$ | the whole algebra, dimension $8$ |
| the sums | $\mathbb{C}_{\mathbb{B}}+\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}+i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_++\mathbb{M}_-$ — all equal to $\mathbb{B}$ |
| the four-dimensional spaces | $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ |
| the three-dimensional triples | $\langle \vec e_x,\vec e_y,\vec e_z\rangle=\mathrm{Vect}\cap\mathbb{H}_{\mathbb{B}}$, $\langle i\vec e_x,i\vec e_y,i\vec e_z\rangle=\mathrm{Vect}\cap\mathbb{M}_+$ |
| the two-dimensional centre | $\mathbb{C}_{\mathbb{B}}=\langle e_t\rangle\oplus\langle ie_t\rangle$ |
| the one-dimensional lines | $\langle e_t\rangle$, $\langle ie_t\rangle$ |
| the origin | $0$ |

The object is not a chain, and it is not closed under sum, being the union of the three decompositions of $\mathbb{B}$ rather than a single distributive lattice: the intersections of §*The Intersections* are its meets, and the sums of §*The Sums* are its joins wherever the sum does not reach the top. Its skeleton is the block table, that is, the three decompositions of the four coordinate blocks, and the levels record how the remarkable subspaces sit over those blocks.

## The Complex Structure and the Remarkable Subspaces

The scalar imaginary $i$ gives the real-linear map $J : \tilde{Q} \mapsto i\tilde{Q}$ with $J^2 = -\mathrm{id}$, the complex structure carried by every complex vector space, defined for $\mathbb{B}$ in *The Biquaternion Algebra*. It is not one of the four conjugations, and its action on the remarkable subspaces is read directly from the block table; no product is invoked. Since $i(q + iq') = -q' + iq$ on the coefficients, $J$ exchanges the two scalar blocks and the two vector blocks:

$$
J(A_1) = A_2, \qquad J(A_2) = A_1, \qquad J(B_1) = B_2, \qquad J(B_2) = B_1.
$$

A subspace made of a block together with its image is therefore stable, and a subspace made of the images of the blocks of another is exchanged with it:

$$
J(\mathbb{C}_{\mathbb{B}}) = \mathbb{C}_{\mathbb{B}}, \qquad J(\mathrm{Vect}(\mathbb{B})) = \mathrm{Vect}(\mathbb{B}), \qquad J(\mathbb{H}_{\mathbb{B}}) = i\mathbb{H}_{\mathbb{B}}, \qquad J(i\mathbb{H}_{\mathbb{B}}) = \mathbb{H}_{\mathbb{B}},
$$

$$
\boxed{\; J(\mathbb{M}_+) = \mathbb{M}_-, \qquad J(\mathbb{M}_-) = \mathbb{M}_+ \;}.
$$

The centre and the vector subspace are stable, the quaternion subspace is carried onto the anti-quaternion subspace and conversely, and the Hermitian subspace onto the anti-Hermitian one and conversely. The contrast with the conjugations is the point: each of the four preserves each of the remarkable subspaces, whereas $J$ pairs them, exchanging $\mathbb{H}_{\mathbb{B}}$ with $i\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_+$ with $\mathbb{M}_-$ and leaving the other two alone. Under the group generated by the four conjugations together with $J$, the remarkable subspaces therefore fall into four classes: the centre, the vector subspace, and the two exchanged pairs. It is the complex structure, and not quaternion conjugation, that makes the pairs, and it is a fact about the linear space alone.

## Worked Examples

**An element and its blocks.** Take $\tilde{Q} = 3\vec e_x + i\vec e_y$. Its real part $3\vec e_x$ lies in the real vector block $B_1$ and its imaginary part $i\vec e_y$ in the imaginary vector block $B_2$, while both scalar blocks carry nothing. Every subspace containing $\tilde{Q}$ must then contain both $B_1$ and $B_2$, and the only sum of two blocks that does so is $\mathrm{Vect}(\mathbb{B}) = B_1 \oplus B_2$: the element lies in the vector subspace and in none of the other five. Its two parts lie in the two three-dimensional intersections $B_1 = \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$ and $B_2 = i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+$, which is the block reading of the entries $3$ of the intersection table.

**An intersection of dimension three.** The quaternion subspace is $A_1 \oplus B_1$ and the anti-Hermitian subspace is $A_2 \oplus B_1$, so they share the single block $B_1$ and meet in it:

$$
\boxed{\;\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_- = B_1 = \operatorname{span}_{\mathbb{R}}\{\vec e_x, \vec e_y, \vec e_z\}, \qquad \dim_{\mathbb{R}} = 3\;}.
$$

The same answer follows from the defining conditions: an element of $\mathbb{H}_{\mathbb{B}}$ has real coefficients, and an element of $\mathbb{M}_-$ has a purely imaginary scalar coefficient and real vector coefficients, so the scalar coefficient must vanish and the element is a real vector. The element $\vec e_x + 2\vec e_y$ is a concrete member, and $3$ is the entry of this pair in the intersection table.

**An element in the three decompositions.** Take the element

$$
\tilde{Q} = (2+i)e_t + 3\vec e_x + i\vec e_y - 4\vec e_z .
$$

Its three readings, one per decomposition, follow from the projection formulas above:

$$
\tilde{Q} = \underbrace{(2+i)e_t}_{\mathbb{C}_{\mathbb{B}}} + \underbrace{3\vec e_x + i\vec e_y - 4\vec e_z}_{\mathrm{Vect}(\mathbb{B})},
$$

$$
\tilde{Q} = \underbrace{2e_t + 3\vec e_x - 4\vec e_z}_{\mathbb{H}_{\mathbb{B}}} + \underbrace{ie_t + i\vec e_y}_{i\mathbb{H}_{\mathbb{B}}},
$$

$$
\tilde{Q} = \underbrace{2e_t + i\vec e_y}_{\mathbb{M}_+} + \underbrace{ie_t + 3\vec e_x - 4\vec e_z}_{\mathbb{M}_-}.
$$

The three lines add up to the same element, as they must, since each is a direct sum decomposition of the same eight real coordinates $(2, 3, 0, -4, 1, 0, 1, 0)$. The scalar–vector reading takes the whole scalar coefficient $2+i$ against the whole vector part $3\vec e_x + i\vec e_y - 4\vec e_z$. The quaternion reading splits each coefficient into its real and imaginary parts and puts the real parts $2e_t + 3\vec e_x - 4\vec e_z$ in $\mathbb{H}_{\mathbb{B}}$ and the imaginary parts $ie_t + i\vec e_y$ in $i\mathbb{H}_{\mathbb{B}}$. The Hermitian reading pairs the real scalar part and the imaginary vector part, $2e_t + i\vec e_y$, against the imaginary scalar part and the real vector part, $ie_t + 3\vec e_x - 4\vec e_z$. No one of the three readings can be recovered from another: the same eight coordinates are cut along three different planes.

## Summary

The biquaternion algebra $\mathbb{B}$ carries four conjugations whose fixed and anti-fixed spaces reduce to six distinct subspaces, the remarkable subspaces. The centre $\mathbb{C}_{\mathbb{B}}$, fixed by ${}^{\natural}$, is the set of elements with vanishing vector part, of real basis $e_t, ie_t$ and dimension $2$; it is the centre of the algebra and a field. The vector subspace $\mathrm{Vect}(\mathbb{B})$, anti-fixed by ${}^{\natural}$, is the kernel of the scalar part, of real basis $\vec e_x, \vec e_y, \vec e_z, i\vec e_x, i\vec e_y, i\vec e_z$ and dimension $6$; it is closed under the commutator and not under the product. The quaternion subspace $\mathbb{H}_{\mathbb{B}}$, fixed by $\bar{\cdot}$, is the set of elements with real coefficients, of real basis $e_t, \vec e_x, \vec e_y, \vec e_z$ and dimension $4$; it is a division subalgebra. The anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, anti-fixed by $\bar{\cdot}$, is $i$ times the quaternion subspace, of real basis $ie_t, i\vec e_x, i\vec e_y, i\vec e_z$ and dimension $4$; it is not a subalgebra and is stable under multiplication by $\mathbb{H}_{\mathbb{B}}$ on both sides. The Hermitian subspace $\mathbb{M}_+$, fixed by ${}^{*}$, is the set of elements with real scalar part and purely imaginary vector part, of real basis $e_t, i\vec e_x, i\vec e_y, i\vec e_z$ and dimension $4$; the symmetrized product of two of its elements stays in it. The anti-Hermitian subspace $\mathbb{M}_-$, anti-fixed by ${}^{*}$ and fixed by $\flat$, is the set of elements with purely imaginary scalar part and real vector part, of real basis $ie_t, \vec e_x, \vec e_y, \vec e_z$ and dimension $4$; it is a real Lie algebra. Exactly two of the six are closed under the product, the centre and the quaternion subspace.

The relations are read off the four coordinate blocks $A_1 = \mathbb{R}e_t$, $A_2 = \mathbb{R}(ie_t)$, $B_1 = \operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ and $B_2 = \operatorname{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}$, each the intersection of the three subspaces containing it. Every remarkable subspace is a sum of two blocks: the centre of the two scalar blocks, the vector subspace of the two vector blocks, and each four-dimensional subspace of one scalar and one vector block, in the four possible ways. Two distinct subspaces meet in the blocks they share, so the fifteen intersections have dimension $0$, $1$ or $3$: the members of a decomposition meet in the origin, the centre meets each other subspace in a scalar line, and the vector subspace in a vector triple. Exactly the three decomposition pairs sum to the whole algebra; the pairs sharing a vector triple sum to a subspace of dimension $7$, and those sharing a scalar line to one of dimension $5$.

The three decompositions are $\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$, $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$ and $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$, of real dimensions $2+6$, $4+4$ and $4+4$. In each case the two halves are the fixed and the anti-fixed space of the conjugation; the component in the fixed space is the halved sum of the element and its image, and the component in the anti-fixed space is the halved difference, divided by $i$ in the quaternion case so that it lands in $\mathbb{H}_{\mathbb{B}}$. The first is the split into scalar and pure vector parts, the only one with halves of unequal dimension; the second writes a biquaternion as a real quaternion plus $i$ times another, the real and imaginary parts of the complexification; the third is the algebraic analogue of the real and imaginary parts of a complex number. There are exactly three: the reversal $\flat = -{}^{*}$ reproduces the two spaces of ${}^{*}$ with the signs exchanged, and the three decompositions are the three pairings of the four coordinate blocks into two complementary pairs.

Each of the four conjugations preserves each remarkable subspace and acts on it by signs $+1$ and $-1$; the vanishing multiplicities of $-1$ identify the subspace fixed by each conjugation, and the table of multiplicities exhibits ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ as a symmetric difference. The complex structure $J : \tilde{Q} \mapsto i\tilde{Q}$ preserves the centre and the vector subspace and exchanges $\mathbb{H}_{\mathbb{B}}$ with $i\mathbb{H}_{\mathbb{B}}$ and $\mathbb{M}_+$ with $\mathbb{M}_-$. The element $\tilde{Q} = (2+i)e_t + 3\vec e_x + i\vec e_y - 4\vec e_z$ reads as $\tilde{Q}_{\mathrm{c}} + \tilde{Q}_{\mathrm{v}}$, as $\tilde{Q}_r + i\tilde{Q}_i$ and as $\tilde{Q}_+ + \tilde{Q}_-$, the same eight real coordinates cut along three different planes.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ |
| $e_t, \vec e_x, \vec e_y, \vec e_z$ | the basis, with $e_t$ the unit and $\vec e_k^2 = -e_t$ |
| $i$ | the central imaginary unit, $i^2 = -1$, commuting with every element |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | a general biquaternion |
| $Q_\mu = q_\mu + i q'_\mu$ | the complex coefficient of $e_\mu$, with $q_\mu, q'_\mu \in \mathbb{R}$ |
| ${}^{\natural}, \bar{\cdot}, {}^{*}, \flat$ | quaternion, complex, Hermitian conjugation and reversal, $\flat = -{}^{*}$ |
| $\operatorname{Sc}(\tilde{Q})$ | the scalar part $Q_t$, equal to $\tfrac{1}{2}(\tilde{Q} + \tilde{Q}^{\natural})$ |
| $\mathbb{C}_{\mathbb{B}}$ | the centre, fixed space of ${}^{\natural}$; basis $e_t, ie_t$, dimension $2$ |
| $\mathrm{Vect}(\mathbb{B})$ | the vector subspace, anti-fixed space of ${}^{\natural}$; basis $\vec e_x, \vec e_y, \vec e_z, i\vec e_x, i\vec e_y, i\vec e_z$, dimension $6$ |
| $\mathbb{H}_{\mathbb{B}}$ | the quaternion subspace, fixed space of $\bar{\cdot}$; basis $e_t, \vec e_x, \vec e_y, \vec e_z$, dimension $4$ |
| $i\mathbb{H}_{\mathbb{B}}$ | the anti-quaternion subspace, anti-fixed space of $\bar{\cdot}$; basis $ie_t, i\vec e_x, i\vec e_y, i\vec e_z$, dimension $4$ |
| $\mathbb{M}_+$ | the Hermitian subspace, fixed space of ${}^{*}$; basis $e_t, i\vec e_x, i\vec e_y, i\vec e_z$, dimension $4$ |
| $\mathbb{M}_-$ | the anti-Hermitian subspace, anti-fixed space of ${}^{*}$ and fixed space of $\flat$; basis $ie_t, \vec e_x, \vec e_y, \vec e_z$, dimension $4$ |
| $A_1, A_2$ | the scalar blocks $\mathbb{R}e_t$ and $\mathbb{R}(ie_t)$ |
| $B_1, B_2$ | the vector blocks $\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ and $\operatorname{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}$ |
| $\tilde{Q}_{\mathrm{c}}, \tilde{Q}_{\mathrm{v}}$ | scalar and vector components, in $\mathbb{C}_{\mathbb{B}}$ and $\mathrm{Vect}(\mathbb{B})$ |
| $\tilde{Q}_r, \tilde{Q}_i$ | quaternion and imaginary-quaternion components, both in $\mathbb{H}_{\mathbb{B}}$ |
| $\tilde{Q}_+, \tilde{Q}_-$ | Hermitian and anti-Hermitian components, in $\mathbb{M}_+$ and $\mathbb{M}_-$ |
| $\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B})$ | centre–vector decomposition, from ${}^{\natural}$ |
| $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$ | quaternion decomposition, from $\bar{\cdot}$ |
| $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ | Hermitian decomposition, from ${}^{*}$ |
| $J$ | complex structure $J : \tilde{Q} \mapsto i\tilde{Q}$, $J^2 = -\mathrm{id}$ |
| $\tilde{Q}_1 \bullet \tilde{Q}_2$ | symmetrized product $\tfrac{1}{2}(\tilde{Q}_1\tilde{Q}_2 + \tilde{Q}_2\tilde{Q}_1)$ |
| fixed space, anti-fixed space | the elements fixed, or reversed, by an involution |
| lattice of the fixed spaces | the remarkable subspaces under inclusion, intersections as meets, sums as joins |

## Further Reading

- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the algebra, its basis, its conjugations and its coordinate systems
- [The Element, the Coordinates and the Conjugations in the Biquaternion Algebra](the-element-the-coordinates-and-the-conjugations.html), for the formulas of the conjugations and their linear or antilinear character
- [The Group of Involutions of the Biquaternion Algebra](the-group-of-involutions.html), for the four conjugations as an abstract group
- [Remarkable Subspaces and the Four General Products, Forms and Norms](remarkable-subspaces-and-the-four-general-products-forms-and-norms.html), for the four general products brought to the remarkable subspaces together, the product of two elements of the remarkable subspaces, and the Jordan and the Lie algebra each subspace carries
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the four forms on the remarkable subspaces side by side, the only orthogonal pair and the comparison of the two readings
- [Remarkable Subspaces under the General Quaternionic Algebra](remarkable-subspaces-under-the-general-quaternionic-algebra.html), [Remarkable Subspaces under the General Plain Sesqualgebra](remarkable-subspaces-under-the-general-plain-sesqualgebra.html), [Remarkable Subspaces under the General Quaternionic Sesqualgebra](remarkable-subspaces-under-the-general-quaternionic-sesqualgebra.html), for the restrictions themselves, subspace by subspace and form by form, and for the isotropic lines and the minimal ideals the remarkable subspaces determine
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the norm, the inverse formula, the unit group and the zero divisors of the whole algebra
- [Square Roots of an Element](square-roots-of-an-element.html), for the three classifications in the whole algebra
- [Idempotents](idempotents.html), for the classification of the idempotents of the whole algebra, the bijection with the roots of minus one and the projection reading
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the Peirce decomposition in the whole algebra
- [The Category of Modules](the-category-of-modules.html), for the simple module $S$, the minimal left ideals and the Morita equivalence
- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the product and its scalar–vector form
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the two parts into which the product splits
- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- Nicolas Bourbaki, *Algebra I* (Springer, 1998), for the decomposition of a vector space into the fixed and reversed parts of an involution.
