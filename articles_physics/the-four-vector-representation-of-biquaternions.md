# __The Four-Vector Representation of Biquaternions__

## Introduction

The **four-vector representation** of a biquaternion is the reading of an element of the algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ as its four complex coefficients,

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3 = \sum_{\mu = 0}^{3} Q_\mu e_\mu, \qquad Q_\mu \in \mathbb{C},
$$

which identifies $\mathbb{B}$ with the coordinate space $\mathbb{C}^4$. The realization supplies a space and no action: the action is the $4 \times 4$ matrix of left multiplication in *The 4×4 Regular Matrix Representation of Biquaternions* and the $2 \times 2$ matrices of *The 2×2 Matrix Representation of Biquaternions*. This article treats the coefficient space, the column and the dual row, the component form of the product, the four conjugations in coordinates, the six distinguished subspaces as coordinate conditions, and the norm form with its two real restrictions.

The conventions are those of *Conventions in the Biquaternion Universe*, and none is redefined. The basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_1e_2 = e_3$, the scalar imaginary $i$ commutes with every unit, and the conjugations are $\bar{\cdot}$, ${}^{*}$, ${}^{\dagger} = \bar{\cdot}\circ{}^{*}$ and ${}^{\flat} = -\dagger$. The norm form is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$. The physical dictionary writes a general element as a material coordinate plus an informational coordinate,

$$
\tilde{Q} = \underbrace{(ict)\,e_0 + \mathbf{x}}_{\in\,\mathbb{M}_-} \;+\; \underbrace{(ct')\,e_0 + i\mathbf{x}'}_{\in\,\mathbb{M}_+},
\qquad \mathbf{x} = xe_1 + ye_2 + ze_3, \quad \mathbf{x}' = x'e_1 + y'e_2 + z'e_3,
$$

with the eight real parameters $q'_0 = c\,t$, $(q_1, q_2, q_3) = (x, y, z)$, $q_0 = c\,t'$, $(q'_1, q'_2, q'_3) = (x', y', z')$, and with $c$ the speed of light in the medium.

## The Coefficient Space

**Definition.** The **four-vector** of a biquaternion $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ is the ordered quadruple of its coefficients,

$$
Q^\mu = (Q^0, Q^1, Q^2, Q^3), \qquad Q^0 = Q_0, \quad (Q^1, Q^2, Q^3) = (Q_1, Q_2, Q_3).
$$

The index position is fixed by this definition. The component $Q^0$ is the **scalar component** and $Q^1, Q^2, Q^3$ are the **vector components**, the coefficients of the scalar and vector parts of $\tilde{Q}$ and nothing else. No raising or lowering of indices is introduced anywhere in this article, and the reason is stated below: on $\mathbb{C}^4$ there is no pairing with which to move an index.

**Proposition.** The map $\tilde{Q} \mapsto Q^\mu$ is a $\mathbb{C}$-linear isomorphism from $\mathbb{B}$ onto $\mathbb{C}^4$. The coefficient space therefore has complex dimension $4$ and real dimension $8$.

**Proof.** The map sends the basis $e_0, e_1, e_2, e_3$ to the standard basis of $\mathbb{C}^4$ and is extended by linearity; it is bijective on bases, and the action of a complex scalar on the coefficients is the same on both sides.

The coefficient space is **not** the simple module of the algebra. The simple module has complex dimension $2$ and is the carrier of the spinor of the corpus; it is treated in *The 2×2 Matrix Representation of Biquaternions*. The number $4$ recurs there and in *The 4×4 Regular Matrix Representation of Biquaternions* for two different reasons, and neither is a coincidence: the coefficient space is the algebra itself, of complex dimension $4$, and the regular representation is the algebra acting on itself, so its matrix is $4 \times 4$ for the same count.

### The Real and Imaginary Parts

Each complex component splits into a real part and $i$ times a real part,

$$
Q^\mu = q^\mu + i q'^\mu, \qquad q^\mu, q'^\mu \in \mathbb{R},
$$

and the eight real numbers so obtained identify the coefficient space with $\mathbb{R}^8$. The split is the coefficient split of the algebra: the quadruple with $q'^\mu = 0$ is an element of the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the quadruple with $q^\mu = 0$ is an element of its multiple $i\mathbb{H}_{\mathbb{B}}$, and

$$
\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}
$$

is the real-and-imaginary split of the coefficients read coordinate by coordinate. The other four distinguished subspaces mix the real and imaginary parts, because the involutions that define them combine with the scalar imaginary in different ways; they are tabulated below.

The norm form does not decompose over these eight real coordinates. Its real part is $\sum_\mu \big( (q^\mu)^2 - (q'^\mu)^2 \big)$ and its imaginary part is $2\sum_\mu q^\mu q'^\mu$, both real quadratic forms in eight variables, and the positive-definite form $\sum_\mu \big( (q^\mu)^2 + (q'^\mu)^2 \big)$ is the squared Euclidean length of the quadruple. That last form is the Hermitian form $\sum_\mu |Q^\mu|^2$ of the algebra, and it is a different object from the norm form: the norm form is complex bilinear and can vanish on a nonzero element, while the Hermitian form is positive definite.

### The Physical Dictionary

The informational and material writings of the Introduction are matched coefficient by coefficient: the four complex coefficients, in physical terms, are

$$
Q^0 = c t' + i c t, \qquad Q^1 = x + i x', \qquad Q^2 = y + i y', \qquad Q^3 = z + i z'.
$$

Every complex coefficient therefore carries **one material coordinate and one informational coordinate**: the scalar coefficient carries the two times, and each vector coefficient carries one spatial coordinate of each sector. Read by real and imaginary part, the quadruple $(q^0, q^1, q^2, q^3) = (ct', x, y, z)$ is the informational time together with the material space, and the quadruple $(q'^0, q'^1, q'^2, q'^3) = (ct, x', y', z')$ is the material time together with the informational space. This is the same mixed ownership that the prime convention records, and it is why the scalar component of a physical four-vector is the one that carries the time.

**The material four-vector.** An element of the material sector has a purely imaginary scalar coefficient and real vector coefficients. Writing its real time parameter as $q'_0$ and its real spatial parameters as $q_1, q_2, q_3$, the element and its four-vector are

$$
\tilde{Q} = iq'_0e_0 + q_1e_1 + q_2e_2 + q_3e_3 \in \mathbb{M}_-, \qquad (Q^0, Q^1, Q^2, Q^3) = (iq'_0, q_1, q_2, q_3).
$$

The four-vectors of relativistic physics are of exactly this shape: the four-position has $q'_0 = ct$ and $(q_1, q_2, q_3) = (x,y,z)$, so its scalar coefficient is $ict = iq'_0$ and its four-vector is $(ict, x, y, z)$, while the four-momentum has $q'_0 = E/c$ and $(q_1, q_2, q_3) = \mathbf{p}$.

**The informational four-vector.** An element of the informational sector has a real scalar coefficient and purely imaginary vector coefficients. Writing its real parameters as $q_0$ and $q'_1, q'_2, q'_3$, the element and its four-vector are

$$
\tilde{Q} = q_0e_0 + iq'_1e_1 + iq'_2e_2 + iq'_3e_3 \in \mathbb{M}_+, \qquad (Q^0, Q^1, Q^2, Q^3) = (q_0, iq'_1, iq'_2, iq'_3).
$$

The informational coordinate is the case $q_0 = ct'$ and $(q'_1, q'_2, q'_3) = (x', y', z')$, so its four-vector is $(ct', ix', iy', iz')$.

## The Column and the Dual Row

**Definition.** The **column** of $\tilde{Q}$ is the $4 \times 1$ matrix

$$
Q = \begin{pmatrix} Q^0 \\ Q^1 \\ Q^2 \\ Q^3 \end{pmatrix},
$$

and the **row** of $\tilde{Q}$ is its transpose,

$$
Q^{\mathsf{T}} = \begin{pmatrix} Q^0 & Q^1 & Q^2 & Q^3 \end{pmatrix}.
$$

The column is the transcribed form of the quadruple, and it is convenient because the product of biquaternions is bilinear. For a fixed $\tilde{Q}$ the map $\tilde{R} \mapsto \tilde{Q}\tilde{R}$ sends the coefficients of $\tilde{R}$ linearly to the coefficients of the product, so it is a $\mathbb{C}$-linear endomorphism of the coefficient space, and with the column convention it is written as a $4 \times 4$ matrix acting on the column of $\tilde{R}$:

$$
\widetilde{\tilde{Q}\tilde{R}} \longleftrightarrow \rho_L(\tilde{Q})\, R .
$$

The matrix $\rho_L(\tilde{Q})$ is the matrix of left multiplication; its entries are the coefficients of $\tilde{Q}$ with signs and no additions, and it is constructed and verified in *The 4×4 Regular Matrix Representation of Biquaternions*. The present article records only that the product admits this reading.

**The row is the dual, not a further representation.** The row $Q^{\mathsf{T}}$ is the element of the dual space paired with the column by the standard pairing, and the dual of a left module is a right module: it carries the *right* action, $(\varphi\cdot\tilde{Q})(\tilde{R}) = \varphi(\tilde{Q}\tilde{R})$. The transpose that relates the column picture to the row picture is dressed with quaternion conjugation, so that the transpose of the left matrix of $\tilde{Q}$ is the left matrix of the quaternion conjugate,

$$
\rho_L(\tilde{Q})^{\mathsf{T}} = \rho_L(\bar{\tilde{Q}}),
$$

which is proved in *The 4×4 Regular Matrix Representation of Biquaternions*. A column and a row are the same four complex numbers written in two layouts, and a change of layout is a change of bookkeeping, not a change of representation. The corpus counts three objects in this group — the coefficient space, the algebra acting on its simple module, and the algebra acting on itself — and it does not count the two layouts separately.

## Multiplication in Four-Vector Form

The product of two biquaternions is computed from the basis and separates into a scalar component and three vector components.

**Proposition (the product in components).** Let $\tilde{Q}$ and $\tilde{R}$ be biquaternions with four-vectors $Q^\mu$ and $R^\mu$. Then the four-vector of the product has components

$$
(\tilde{Q}\tilde{R})^0 = Q^0 R^0 - \sum_{k=1}^{3} Q^k R^k,
$$

$$
(\tilde{Q}\tilde{R})^i = Q^0 R^i + R^0 Q^i + \sum_{j,k=1}^{3} \epsilon^{ijk} Q^j R^k, \qquad i = 1, 2, 3,
$$

where $\epsilon^{ijk}$ is the Levi-Civita symbol on the indices $1, 2, 3$.

**Proof.** Expand the product in the basis, using $e_0 e_\mu = e_\mu$ and $e_k^2 = -e_0$. The scalar component collects the terms in which both factors contribute the scalar unit or both contribute the same quaternion unit, $Q^0R^0 e_0 + \sum_k Q^kR^k e_k^2 = \big( Q^0R^0 - \sum_k Q^kR^k \big)e_0$, and the terms with two different quaternion units contribute no scalar component. The coefficient of $e_i$ collects $Q^0R^i e_i$ and $Q^iR^0 e_i$ from the mixed scalar–vector pairs, together with the products $Q^jR^k e_je_k$ over the ordered pairs with $\{j,k\} = \{1,2,3\}\setminus\{i\}$. For those, $e_je_k = \epsilon^{ijk}e_i$, the basis being oriented so that $e_1e_2 = e_3$, $e_2e_3 = e_1$ and $e_3e_1 = e_2$; the sum over $j,k$ therefore runs over both orderings and gives the displayed Levi-Civita term.

**Corollary (the commutator).** The commutator of two biquaternions is twice the cross product of their vector components,

$$
\tilde{Q}\tilde{R} - \tilde{R}\tilde{Q} = 2 \sum_{i=1}^{3} \Big( \sum_{j,k=1}^{3} \epsilon^{ijk} Q^j R^k \Big) e_i .
$$

The scalar component and the symmetric part $Q^0R^i + R^0Q^i$ of each vector component are unchanged by exchanging the factors; the Levi-Civita term is the only part that changes sign, and it is therefore the only trace of non-commutativity visible in this realization. In particular the commutator always has zero scalar component, so it lies in the vector subspace $\mathrm{Vect}(\mathbb{B})$ — the derived subspace of the algebra, which is the complex space sector — and it vanishes exactly when the vector parts of the two factors are linearly dependent over $\mathbb{C}$.

**Example.** For $\tilde{Q} = e_0 + e_1$ and $\tilde{R} = e_0 + e_2$ the four-vectors are $Q^\mu = (1,1,0,0)$ and $R^\mu = (1,0,1,0)$. The product formula gives $(\tilde{Q}\tilde{R})^\mu = (1,1,1,1)$, that is, $\tilde{Q}\tilde{R} = e_0 + e_1 + e_2 + e_3$, while the reversed product gives $(\tilde{R}\tilde{Q})^\mu = (1,1,1,-1)$, since the only nonzero Levi-Civita term changes sign. The two products differ by $2e_3$, which is twice the cross product of the vector parts.

### The Multiplication Table of the Basis

The product formula is the row-by-row reading of the multiplication table of the basis, displayed once for reference; the entry in row $\mu$ and column $\nu$ is $e_\mu e_\nu$.

| $e_\mu \backslash e_\nu$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
| $e_1$ | $e_1$ | $-e_0$ | $e_3$ | $-e_2$ |
| $e_2$ | $e_2$ | $-e_3$ | $-e_0$ | $e_1$ |
| $e_3$ | $e_3$ | $e_2$ | $-e_1$ | $-e_0$ |

The first row and the first column reproduce the basis, since $e_0$ is the identity. In the remaining $3 \times 3$ block the table is skew off the diagonal, $e_je_k = -e_ke_j$ for distinct $j,k$, while its diagonal entries are $-e_0$. The scalar component of a product is read from the diagonal of the table, which is why it carries $Q^0R^0 - \sum_k Q^kR^k$, and the vector components are read from the off-diagonal entries, which is why they carry both the symmetric scalar–vector part and the antisymmetric Levi-Civita term. The same table read as a map on the coefficient space is the regular matrix of *The 4×4 Regular Matrix Representation of Biquaternions*.

## The Conjugations in Coordinates

The algebra carries the quaternion conjugation $\bar{\cdot}$, the complex conjugation ${}^{*}$, the Hermitian conjugation ${}^{\dagger} = \bar{\cdot}\circ{}^{*}$ and the anti-Hermitian conjugation ${}^{\flat} = -\dagger$. In coordinates, quaternion conjugation negates the vector components, complex conjugation conjugates every component, and Hermitian conjugation does both.

**Proposition (conjugations in coordinates).** For a biquaternion with four-vector $Q^\mu$,

$$
(\bar{\tilde{Q}})^\mu = (Q^0, -Q^1, -Q^2, -Q^3),
$$

$$
(\tilde{Q}^{*})^\mu = \big( (Q^0)^{*}, (Q^1)^{*}, (Q^2)^{*}, (Q^3)^{*} \big),
$$

$$
(\tilde{Q}^{\dagger})^\mu = \big( (Q^0)^{*}, -(Q^1)^{*}, -(Q^2)^{*}, -(Q^3)^{*} \big), \qquad (\tilde{Q}^{\flat})^\mu = -(\tilde{Q}^{\dagger})^\mu .
$$

**Proof.** Quaternion conjugation fixes $e_0$ and sends $e_k$ to $-e_k$ while leaving every coefficient untouched, so it acts on the coefficients by $(Q^0, Q^1, Q^2, Q^3) \mapsto (Q^0, -Q^1, -Q^2, -Q^3)$. Complex conjugation fixes every basis element and conjugates the central scalar $i$, hence conjugates each coefficient. Hermitian conjugation is their composite, and $\flat$ is its negative.

The three involutions $\bar{\cdot}$, ${}^{*}$ and ${}^{\dagger}$ commute and generate a Klein four-group with the identity; the fourth involution $\flat$ is not independent of them, since $\flat = -\dagger$. This is why the fixed-point subspaces come in three pairs and not four.

**Example.** For the element

$$
\tilde{Q} = (2+i)e_0 + (1-i)e_1 + 3e_2 + ie_3, \qquad Q^\mu = (2+i, \, 1-i, \, 3, \, i),
$$

the four conjugations have four-vectors

$$
\bar{\tilde{Q}} \leftrightarrow (2+i, \, -1+i, \, -3, \, -i), \qquad \tilde{Q}^{*} \leftrightarrow (2-i, \, 1+i, \, 3, \, -i),
$$

$$
\tilde{Q}^{\dagger} \leftrightarrow (2-i, \, -1-i, \, -3, \, i), \qquad \tilde{Q}^{\flat} \leftrightarrow (-2+i, \, 1+i, \, 3, \, -i),
$$

and each is an involution. The Hermitian part $\tfrac12(\tilde{Q} + \tilde{Q}^{\dagger})$ has four-vector $(2, -i, 0, i)$: a real scalar component and purely imaginary vector components, as the table of subspaces requires. In physical terms this element carries the informational time $ct' = 2$ on the scalar component together with the material time $ct = 1$, and its real vector components are the material spatial coordinates $(x,y,z) = (1,3,0)$ while its imaginary ones are the informational $(x',y',z') = (-1,0,1)$.

**Consequences for the physical coordinates.** The conjugation rules are the coordinate form of the statement that the material coordinates are the imaginary part of the quadruple and the informational ones its real part. Quaternion conjugation keeps the material scalar and negates the material vector; complex conjugation conjugates every coefficient and so exchanges the role of informational and material in each slot; Hermitian conjugation does both, and its fixed quadruples are exactly those with a real scalar component and purely imaginary vector components, the informational four-vectors. The anti-fixed quadruples of $\dagger$ are the material four-vectors, and this is the sense in which $\flat$ is the real structure of the framework.

## The Six Distinguished Subspaces

Each involution cuts out a fixed subspace and an anti-fixed subspace, and the three involutions together produce six real subspaces of $\mathbb{B}$.

Each of the six is displayed below as a chain of three quadruples: in the complex coefficients $Q^0, Q^1, Q^2, Q^3$; in the real parameters $q_\mu, q'_\mu$ of the split $Q_\mu = q_\mu + iq'_\mu$; and in the physical coordinates. The dictionary from the real parameters to the physical names is one and the same for all six,

$$
q_0 = ct', \quad q'_0 = ct, \quad q_1 = x, \quad q_2 = y, \quad q_3 = z, \quad q'_1 = x', \quad q'_2 = y', \quad q'_3 = z' ,
$$

the unprimed slot carrying the informational time $ct'$ and the material space $\mathbf{x}$, the primed slot the material time $ct$ and the informational space $\mathbf{x}'$.

**Definition.** The six **distinguished subspaces** are

$$
\mathbb{C}_{\mathbb{B}} = \{\tilde{Q} : \bar{\tilde{Q}} = \tilde{Q}\}, \qquad \mathrm{Vect}(\mathbb{B}) = \{\tilde{Q} : \bar{\tilde{Q}} = -\tilde{Q}\},
$$

$$
\mathbb{H}_{\mathbb{B}} = \{\tilde{Q} : \tilde{Q}^{*} = \tilde{Q}\}, \qquad i\mathbb{H}_{\mathbb{B}} = \{\tilde{Q} : \tilde{Q}^{*} = -\tilde{Q}\},
$$

$$
\mathbb{M}_+ = \{\tilde{Q} : \tilde{Q}^{\dagger} = \tilde{Q}\}, \qquad \mathbb{M}_- = \{\tilde{Q} : \tilde{Q}^{\flat} = \tilde{Q}\}.
$$

**Proposition (coordinate conditions).** In terms of the four-vector $Q^\mu$ the six subspaces are characterized as follows.

| Subspace | Coordinate condition | Algebraic name | Physical name | real dim |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $Q^1 = Q^2 = Q^3 = 0$ | center | complex time sector | $2$ |
| $\mathrm{Vect}(\mathbb{B})$ | $Q^0 = 0$ | vector | complex space sector | $6$ |
| $\mathbb{H}_{\mathbb{B}}$ | $Q^0, Q^1, Q^2, Q^3 \in \mathbb{R}$ | quaternion | real sector | $4$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $Q^0, Q^1, Q^2, Q^3 \in i\mathbb{R}$ | antiquaternion | imaginary sector | $4$ |
| $\mathbb{M}_+$ | $Q^0 \in \mathbb{R}$, $Q^1, Q^2, Q^3 \in i\mathbb{R}$ | Hermitian | informational sector | $4$ |
| $\mathbb{M}_-$ | $Q^0 \in i\mathbb{R}$, $Q^1, Q^2, Q^3 \in \mathbb{R}$ | anti-Hermitian | material sector | $4$ |

**Proof.** The conditions are the componentwise reading of the four conjugation rules of the preceding section. For $\mathbb{C}_{\mathbb{B}}$ and $\mathrm{Vect}(\mathbb{B})$, quaternion conjugation fixes the scalar component and negates each vector component. For $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, complex conjugation fixes or negates each coefficient according to whether it is real or purely imaginary. For $\mathbb{M}_+$ and $\mathbb{M}_-$, Hermitian conjugation conjugates and then negates the vector components, so the fixed quadruples have a real scalar component and purely imaginary vector components, and the anti-fixed quadruples have a purely imaginary scalar component and real vector components.

The table shows that the three decompositions of the algebra read in coordinates as the splitting of the quadruple into its real and imaginary parts in three different ways:

$$
\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B}) = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}} = \mathbb{M}_+ \oplus \mathbb{M}_- .
$$

The first separates the scalar component from the three vector components, the second separates the real coefficients from the imaginary ones, and the third separates the material quadruples from the informational ones. The three splits are different, none is a refinement of another, and how they cross is the subject of *Relations Between Subspaces*.

### The Centre Subspace $\mathbb{C}_{\mathbb{B}}$

Two-dimensional and purely temporal, without a single spatial coordinate. The scalar coefficient is an arbitrary complex number carrying the two times, and the quadruple is $(Q_0, 0, 0, 0)$:

$$
\tilde{Q} = Q_0e_0 \longleftrightarrow (Q^0, Q^1, Q^2, Q^3) = (Q_0,\ 0,\ 0,\ 0) = (q_0 + iq'_0,\ 0,\ 0,\ 0) = (ct' + ict,\ 0,\ 0,\ 0),
$$

with $Q_0 = q_0 + iq'_0$, $q_0 = ct'$ and $q'_0 = ct$, and the norm form $N = Q_0^2 = c^2t'^2 - c^2t^2 + 2i\,c^2t't$. It is the fixed space of quaternion conjugation, so quaternion conjugation acts on it as the identity — the axis of $\mathbb{B}$.

### The Vector Subspace $\mathrm{Vect}(\mathbb{B})$

Six-real-dimensional and purely spatial, the only one of the six that is not four- or two-dimensional. The scalar coefficient vanishes and each of the three vector coefficients is one material spatial coordinate together with one informational coordinate:

$$
\tilde{Q} = Q_1e_1 + Q_2e_2 + Q_3e_3 \longleftrightarrow (Q^0, Q^1, Q^2, Q^3) = (0,\ Q_1,\ Q_2,\ Q_3) = (0,\ q_1 + iq'_1,\ q_2 + iq'_2,\ q_3 + iq'_3) = (0,\ x + ix',\ y + iy',\ z + iz'),
$$

where $Q_k = q_k + iq'_k$ with $q_k = x_k$ and $q'_k = x'_k$, and the norm form is $N = (x+ix')^2 + (y+iy')^2 + (z+iz')^2$. It is the anti-fixed space of quaternion conjugation and the spatial counterpart of the centre: the centre has the two times in one complex number, the vector subspace the two spaces in three.

### The Quaternion Subspace $\mathbb{H}_{\mathbb{B}}$

The fixed space of complex conjugation: all four coefficients real, so the scalar imaginary plays no role at all, and the quadruple mixes the informational time with the material space,

$$
\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu \longleftrightarrow (Q^0, Q^1, Q^2, Q^3) = (Q_0,\ Q_1,\ Q_2,\ Q_3) = (q_0,\ q_1,\ q_2,\ q_3) = (ct',\ x,\ y,\ z),
$$

with $Q_\mu = q_\mu$ real, $q_0 = ct'$ and $q_k = x_k$, and the norm form $N = c^2t'^2 + \mathbf{x}^2$. The norm form is a sum of four squares with no minus sign, so it is positive definite and vanishes only at the zero element; the unit elements of this subspace are the rotation rotors.

### The Antiquaternion Subspace $i\mathbb{H}_{\mathbb{B}}$

The anti-fixed space of complex conjugation: all four coefficients purely imaginary, so the quadruple takes the other assignment of the two times and the two spaces,

$$
\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu \longleftrightarrow (Q^0, Q^1, Q^2, Q^3) = (Q_0,\ Q_1,\ Q_2,\ Q_3) = (iq'_0,\ iq'_1,\ iq'_2,\ iq'_3) = (ict,\ ix',\ iy',\ iz'),
$$

with $Q_\mu = iq'_\mu$, $q'_0 = ct$ and $q'_k = x'_k$, and the norm form $N = -\big( c^2t^2 + \mathbf{x}'^2 \big)$. It is $i$ times the quaternion subspace, and the norm form is the negative of a sum of four squares, so it too vanishes only at the zero element.

### The Material Subspace $\mathbb{M}_-$

The anti-fixed space of Hermitian conjugation: a purely imaginary scalar coefficient and three real vector coefficients, three real components and one imaginary one,

$$
\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu \longleftrightarrow (Q^0, Q^1, Q^2, Q^3) = (Q_0,\ Q_1,\ Q_2,\ Q_3) = (iq'_0,\ q_1,\ q_2,\ q_3) = (ict,\ x,\ y,\ z),
$$

with $Q_0 = iq'_0$, $Q_k = q_k$, $q'_0 = ct$ and $q_k = x_k$, and the norm form $N = -c^2t^2 + \mathbf{x}^2$. The single minus sign is the $ict$ convention, and the signature $(3,1)$ of the norm form is the Minkowski one: this is the home of the four-vectors of relativistic physics.

### The Informational Subspace $\mathbb{M}_+$

The fixed space of Hermitian conjugation: a real scalar coefficient and three purely imaginary vector coefficients,

$$
\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu \longleftrightarrow (Q^0, Q^1, Q^2, Q^3) = (Q_0,\ Q_1,\ Q_2,\ Q_3) = (q_0,\ iq'_1,\ iq'_2,\ iq'_3) = (ct',\ ix',\ iy',\ iz'),
$$

with $Q_0 = q_0$, $Q_k = iq'_k$, $q_0 = ct'$ and $q'_k = x'_k$, and the norm form $N = c^2t'^2 - \mathbf{x}'^2$, the transpose of the material condition, of signature $(1,3)$. The two sectors are exchanged by multiplication by $i$: $i\mathbb{M}_- = \mathbb{M}_+$, since $i\,(ict, x, y, z) = (-ct, ix, iy, iz)$ has the informational shape.

## The Norm Form

**Definition.** The **norm form** of a biquaternion is the central element

$$
N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = (Q^0)^2 + (Q^1)^2 + (Q^2)^2 + (Q^3)^2 \in \mathbb{C}.
$$

In four-vector form the norm form has **all four signs positive**, and the Gram matrix of its polar form is the identity $\mathrm{diag}(+1,+1,+1,+1)$.

**Proposition (why all four signs are positive).** For every biquaternion $\tilde{Q}$, $\tilde{Q}\bar{\tilde{Q}} = \sum_{\mu=0}^{3} Q_\mu^2$, a complex scalar.

**Proof.** Expand $\tilde{Q}\bar{\tilde{Q}} = \big(\sum_\mu Q_\mu e_\mu\big)\big(Q_0e_0 - \sum_k Q_k e_k\big)$. The cross terms between $e_0$ and the vector units cancel between the two orders. The remaining terms are $Q_0^2e_0$ together with $\sum_k Q_k^2 e_k^2 = -\sum_k Q_k^2e_0$ and the mixed terms $-Q_jQ_ke_je_k$ over ordered pairs with $j \neq k$. The pairs $(j,k)$ and $(k,j)$ carry the same coefficient $Q_jQ_k$ and their basis products are negatives, so the pair contributes a multiple of $e_je_k + e_ke_j = 0$ and cancels. Collecting the surviving scalar terms gives $Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2$.

Two consequences matter. First, the norm form is a **complex bilinear** form of rank four, multiplicative, $N(\tilde{P}\tilde{Q}) = N(\tilde{P})N(\tilde{Q})$, and on the coefficient space itself it is not indefinite: the minus signs of a spacetime signature are not in it. Second, it can vanish on a nonzero element, and it does so exactly on the nonzero solutions of $\sum_\mu Q_\mu^2 = 0$, which are the zero divisors of the algebra. The norm form is therefore not a norm in the analytic sense, and the set of its zeros is the algebra's null cone.

### The Two Real Restrictions

The indefinite form is not on the coefficient space but on the two real sectors, where the four complex coordinates become four real coordinates and the norm form becomes real-valued.

**Proposition (the real restrictions).** On the material sector $\mathbb{M}_-$, writing $Q^0 = i a^0$ and $Q^k = a^k$ with $a^\mu \in \mathbb{R}$, the norm form restricts to

$$
N(\tilde{Q}) = -(a^0)^2 + (a^1)^2 + (a^2)^2 + (a^3)^2,
$$

a real quadratic form of signature $(3,1)$; with $a^0 = ct$ and $a^k = x_k$ it is the Minkowski interval $-c^2t^2 + \mathbf{x}^2$. On the informational sector $\mathbb{M}_+$, writing $Q^0 = a^0$ and $Q^k = i a^k$ with $a^\mu \in \mathbb{R}$, it restricts to

$$
N(\tilde{Q}) = (a^0)^2 - (a^1)^2 - (a^2)^2 - (a^3)^2,
$$

a real quadratic form of signature $(1,3)$; with $a^0 = ct'$ and $a^k = x'_k$ it is $c^2t'^2 - \mathbf{x}'^2$.

**Proof.** Substitute the coordinate conditions of the table above into $\sum_\mu (Q^\mu)^2$. On $\mathbb{M}_-$ the scalar term is $(ia^0)^2 = -(a^0)^2$ and the three vector terms are $(a^k)^2$; on $\mathbb{M}_+$ the scalar term is $(a^0)^2$ and the three vector terms are $(ia^k)^2 = -(a^k)^2$.

The real sector $\mathbb{H}_{\mathbb{B}}$ is the case in which no coefficient carries the $i$, and its norm form is the positive-definite $q_0^2 + q_1^2 + q_2^2 + q_3^2$ of signature $(4,0)$. The two forms are exchanged by multiplication by the scalar imaginary, since $N(i\tilde{Q}) = -N(\tilde{Q})$ on every element and $\mathbb{M}_+ = i\mathbb{M}_-$, $\mathbb{M}_- = i\mathbb{M}_+$. The Lorentzian signature is therefore an **output** of the framework and not an input to it: the four coefficients start on an equal footing with all four signs positive, and the minus sign of the interval appears only when a real coordinate is placed on a direction whose coefficient carries the factor $i$.

**The null cone and the causal classes.** The zeros of the norm form are the light cone of the framework. On $\mathbb{M}_-$ the condition $N(\tilde{Q}) = 0$ is $-c^2t^2 + \mathbf{x}^2 = 0$, the null cone of Minkowski space, and on the algebra at large it is the set of zero divisors. The interval is invariant under the rotor conjugation $\tilde{Q} \mapsto \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{\dagger}$ with $N(\tilde{\Lambda}) = e_0$, so no element of the restricted Lorentz group can move a displacement from one causal class to another; the causal structure of the framework and the orbit decomposition of the cone are developed in the companion articles on causality and on the Lorentz group.

### The Inverse in Coordinates

The invertibility criterion, that $\tilde{Q}$ is a unit exactly when $N(\tilde{Q}) \neq 0$, is that of the mathematics corpus; what the four-vector realization adds is the coordinate form of the inverse.

**Proposition (the inverse in coordinates).** For an invertible biquaternion $\tilde{Q}$,

$$
\tilde{Q}^{-1} = \frac{\bar{\tilde{Q}}}{N(\tilde{Q})}, \qquad \big(\tilde{Q}^{-1}\big)^\mu = \Big( \frac{Q^0}{N}, \, -\frac{Q^1}{N}, \, -\frac{Q^2}{N}, \, -\frac{Q^3}{N} \Big), \qquad N = N(\tilde{Q}).
$$

**Proof.** With $N \neq 0$, the element $\bar{\tilde{Q}}/N$ is a two-sided inverse because $\tilde{Q}\bar{\tilde{Q}} = \bar{\tilde{Q}}\tilde{Q} = N$ is central. Its coordinate form is the vector $\bar{\tilde{Q}}$, whose components are $(Q^0, -Q^1, -Q^2, -Q^3)$, divided by the complex scalar $N$.

**Example.** For the element $\tilde{Q} = (2+i)e_0 + (1-i)e_1 + 3e_2 + ie_3$ of the preceding example,

$$
N(\tilde{Q}) = (2+i)^2 + (1-i)^2 + 3^2 + i^2 = (3+4i) + (-2i) + 9 - 1 = 11 + 2i \neq 0,
$$

so $\tilde{Q}$ is a unit, with four-vector inverse $\tfrac{1}{11+2i}(2+i, -1+i, -3, -i)$. Under the conjugations the norm form becomes $N(\bar{\tilde{Q}}) = 11+2i$, $N(\tilde{Q}^{*}) = 11-2i$ and $N(\tilde{Q}^{\dagger}) = 11-2i$, and multiplication by $i$ reverses its sign, $N(i\tilde{Q}) = -11-2i$.

## The Four-Vectors of Relativistic Physics

The material sector is the home of the four-vectors, and the four-vector representation makes each of them a quadruple with a purely imaginary scalar entry and three real vector entries. The four-vectors below are the standard ones; the algebra's contribution is the uniform shape of their quadruples and the fact that the interval is the norm form.

**The four-position.**

$$
\tilde{Q} = ict\,e_0 + \mathbf{x}, \qquad N(\tilde{Q}) = -c^2t^2 + \mathbf{x}^2,
$$

which is the Minkowski interval. The four-position is the element whose norm form vanishes on the light cone through the origin, and it is the object acted on by the rotor conjugation.

**The four-velocity.** With $\gamma$ the Lorentz factor of a particle of velocity $\mathbf{v}$,

$$
\tilde{U} = i\gamma c\,e_0 + \gamma\mathbf{v}, \qquad N(\tilde{U}) = -\gamma^2\big( c^2 - \mathbf{v}^2 \big) = -c^2 .
$$

The norm form of the four-velocity is **constant**, $-c^2$, on every timelike world line, which is the coordinate form of the statement that $\mathrm{d}\tau = \sqrt{-\mathrm{d}s^2}/c$ is the proper time.

**The four-momentum.**

$$
\tilde{P} = i\frac{E}{c}e_0 + \mathbf{p}, \qquad N(\tilde{P}) = -\frac{E^2}{c^2} + \mathbf{p}^2 .
$$

For an on-shell particle the dispersion relation $E^2 = c^2\mathbf{p}^2 + m^2c^4$ gives

$$
N(\tilde{P}) = -\Big( \frac{E^2}{c^2} - \mathbf{p}^2 \Big) = -m^2c^2 ,
$$

so the mass-shell condition is the statement that the four-momentum lies on the sphere of radius $mc$ in the norm form, and the mass is read off the norm form of the four-momentum. The dispersion relation itself, in biquaternionic form, is the subject of the wave-mechanics articles.

**The four-current and the four-potential.** The electric four-current is

$$
\tilde{J} = i\rho c\,e_0 + \mathbf{J}, \qquad N(\tilde{J}) = -\rho^2c^2 + \mathbf{J}^2 ,
$$

and the four-potential is

$$
\tilde{A} = i\frac{\phi}{c}e_0 + \mathbf{A}, \qquad N(\tilde{A}) = -\frac{\phi^2}{c^2} + \mathbf{A}^2 .
$$

Neither norm form is fixed on general configurations; what is invariant is the transformation law, which is the rotor conjugation, and the gauge freedom, which is the addition of a gradient.

**The gradient.** The biquaternionic gradient has the shape of a material four-vector whose entries are derivatives,

$$
\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z, \qquad \tilde{\nabla} \in \mathbb{M}_- ,
$$

with quadruple $(\partial_{ict}, \partial_x, \partial_y, \partial_z)$. Its norm form is the d'Alembertian,

$$
N(\tilde{\nabla}) = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2 + \partial_x^2 + \partial_y^2 + \partial_z^2 = \Box ,
$$

the all-plus sign of the norm form being exactly what makes the spatial part of the d'Alembertian positive with the $ict$ convention. The gradient is the case in which the material four-vector is an operator, and the wave equation $\Box\tilde{\Psi} = 0$ is the statement that the norm form of the gradient annihilates the field.

**No index is raised or lowered.** The quadruple is written $Q^\mu$ with an upper index, and the index stays where it is: on $\mathbb{C}^4$ no metric is fixed, so the index is never lowered, and the norm form cannot serve as one because it is complex bilinear — symmetric and non-degenerate, of rank four, but neither Hermitian nor positive definite. Physically, the $ict$ convention is what puts the metric into the **coefficient** instead of into a contraction rule: the material four-vector is $(ict, \mathbf{x})$ rather than $(ct, \mathbf{x})$, and the interval is then the sum of squares with no explicit scalar product. The corpus's metric $\eta = \mathrm{diag}(-1,+1,+1,+1)$ is the level-2 reading of the same object, used when a contraction of four-vectors is written explicitly; the level-1 object is the identity Gram matrix on $\mathbb{C}^4$, and the minus sign appears only when the material real coordinates are put on the quadruple.

## Summary

The four-vector representation reads a biquaternion $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ as its quadruple of complex coefficients $Q^\mu = (Q^0, Q^1, Q^2, Q^3)$, with $Q^0 = Q_0$ the scalar component and $(Q^1, Q^2, Q^3) = (Q_1, Q_2, Q_3)$ the vector components. It is a $\mathbb{C}$-linear isomorphism onto $\mathbb{C}^4$, of complex dimension four and real dimension eight, and it supplies the space on which the regular operator of *The 4×4 Regular Matrix Representation of Biquaternions* is written. Physically, each complex coefficient carries one material and one informational coordinate: $Q^0 = ct' + ict$ and $Q^k = x_k + ix'_k$, so that the material four-vector is the quadruple $(ict, x, y, z)$ with a purely imaginary scalar entry, that is $Q^0 = iq'_0$ with $q'_0 = ct$.

The product in components has scalar part $Q^0R^0 - \sum_k Q^kR^k$ and vector part $Q^0R^i + R^0Q^i + \sum_{j,k}\epsilon^{ijk}Q^jR^k$, and the Levi-Civita term is the only trace of non-commutativity; the commutator is twice the cross product of the vector parts and lies in the complex space sector. The three involutions $\bar{\cdot}$, ${}^{*}$, ${}^{\dagger}$ act by negating the vector components, conjugating every component, and doing both, and the six distinguished subspaces are the resulting coordinate conditions: the informational sector is the quadruples with real scalar component and purely imaginary vector components, the material sector the transpose of that condition. The norm form is $\sum_\mu (Q^\mu)^2$, with all four signs positive on $\mathbb{C}^4$ because each quaternion unit squares to $-e_0$ and the cross terms cancel; it restricts to signature $(3,1)$ on the material sector, where it is the Minkowski interval $-c^2t^2 + \mathbf{x}^2$, and to signature $(1,3)$ on the informational sector, and it vanishes exactly on the zero divisors, which are the light cone.

The four-vectors of relativistic physics are the material elements: the four-position with norm form the interval, the four-velocity with norm form the constant $-c^2$, the four-momentum with norm form $-m^2c^2$ on the mass shell, the four-current and four-potential with their respective norm forms, and the gradient, whose norm form is the d'Alembertian $\Box = \partial_{ict}^2 + \Delta$. The index on $Q^\mu$ is never raised or lowered, because the coefficient space carries no metric of its own; the $ict$ convention carries the metric in the coefficient, and the explicit metric $\eta = \mathrm{diag}(-1,+1,+1,+1)$ is the level-2 form used when a contraction is written out.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | The biquaternion algebra, isomorphic to $M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_1e_2 = e_3$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ | Developed form, $Q_\mu \in \mathbb{C}$ |
| $Q^\mu = (Q^0, Q^1, Q^2, Q^3)$ | The four-vector; $Q^0 = Q_0$ the scalar component, $(Q^1,Q^2,Q^3) = (Q_1,Q_2,Q_3)$ the vector components |
| $Q^\mu = q^\mu + iq'^\mu$ | Real and imaginary parts of each component |
| $Q$, $Q^{\mathsf{T}}$ | The column and the dual row of the four-vector |
| $\rho_L(\tilde{Q})$, $\rho_R(\tilde{Q})$ | Matrices of left and right multiplication, constructed in *The 4×4 Regular Matrix Representation of Biquaternions*; $\rho_L(\tilde{Q})^{\mathsf{T}} = \rho_L(\bar{\tilde{Q}})$ |
| $\epsilon^{ijk}$ | Levi-Civita symbol on the indices $1, 2, 3$ |
| $\bar{\tilde{Q}}, \tilde{Q}^{*}, \tilde{Q}^{\dagger}, \tilde{Q}^{\flat} = -\tilde{Q}^{\dagger}$ | Quaternion, complex, Hermitian and anti-Hermitian conjugation |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B}), \mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}, \mathbb{M}_+, \mathbb{M}_-$ | The six distinguished subspaces; coordinate conditions in the table above |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | The norm form, complex bilinear and multiplicative; Gram matrix $\mathrm{diag}(+1,+1,+1,+1)$ on $\mathbb{C}^4$, signature $(3,1)$ on $\mathbb{M}_-$ and $(1,3)$ on $\mathbb{M}_+$ |
| $\tilde{Q}^{-1} = \bar{\tilde{Q}}/N(\tilde{Q})$ | The inverse in coordinates |
| $c$, $c_0$ | Speed of light in the medium, $c = 1/\sqrt{\epsilon\mu}$, and its vacuum value |
| $ict$, $\mathbf{x} = x e_1 + y e_2 + z e_3$ | The material coordinate; the four-position is $(ict, x, y, z)$ |
| $ct'$, $i\mathbf{x}' = i x'e_1 + iy'e_2 + iz'e_3$ | The informational coordinate |
| $q'_0, q_1, q_2, q_3$ | Real parameters of a material four-vector, $\tilde{Q} = iq'_0e_0 + q_1e_1 + q_2e_2 + q_3e_3$; $q'_0 = ct$, $(q_1,q_2,q_3) = (x,y,z)$ for the four-position |
| $q_0, q'_1, q'_2, q'_3$ | Real parameters of an informational four-vector, $\tilde{Q} = q_0e_0 + iq'_1e_1 + iq'_2e_2 + iq'_3e_3$; $q_0 = ct'$, $(q'_1,q'_2,q'_3) = (x',y',z')$ |
| $\tilde{U}$, $\tilde{P}$, $\tilde{J}$, $\tilde{A}$ | Four-velocity, four-momentum, four-current, four-potential; $N(\tilde{U}) = -c^2$, $N(\tilde{P}) = -m^2c^2$ on shell |
| $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$ | Biquaternionic gradient; $N(\tilde{\nabla}) = \Box$ |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2 + \Delta$ | d'Alembertian, series convention |
| $\eta = \mathrm{diag}(-1,+1,+1,+1)$ | The $ict$-coordinate metric of the explicit contractions (level 2) |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Dublin, 1853), for the origin of the quaternion coordinates and for the scalar and vector parts of a quaternion.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions", *Proceedings of the London Mathematical Society* **4** (1873) 381–395, for the first systematic treatment of the complexified quaternions.
- Hermann Minkowski, "Raum und Zeit" (1909), for the four-vector formulation of spacetime and the invariant interval.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), Chapter 3, for the coordinate form of the biquaternion product and its conjugations.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the four-vector realization in applied form.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition (Cambridge University Press, 2001), for the quadratic forms and signatures attached to the biquaternion algebra.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the computation with quaternion and biquaternion coordinates.
- John David Jackson, *Classical Electrodynamics*, 3rd edition (Wiley, 1999), for the covariant four-vector formalism of the four-current and four-potential and for the $ict$ convention in its historical use.
