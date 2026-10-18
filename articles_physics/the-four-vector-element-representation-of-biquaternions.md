# __The Four-Vector Element Representation of Biquaternions__

## Introduction

The **four-vector representation** is the coordinate form of a biquaternion, and the form that carries the physical dictionary: the element read as four complex coefficients, holding a material four-vector and an informational four-vector. Algebraically it is the interpretation of an element of the algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ as its four complex coefficients,

$$
\tilde{Q} = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu, \qquad Q_\mu \in \mathbb{C},
$$

which identifies $\mathbb{B}$ with the coordinate space $\mathbb{C}^4$. The realization supplies a space and no action: the action is the $4 \times 4$ matrix of left multiplication in *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* and the $2 \times 2$ matrices of *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*. This article treats the coefficient space, the column and the dual row, the component form of the product, the four conjugations in coordinates, the remarkable subspaces as coordinate conditions, and the biquaternion norm with its two real restrictions.

The conventions are those of *Conventions in the Biquaternion Universe*, and none is redefined. The basis is $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $e_k^2 = -e_t$ and $\vec e_x \vec e_y = \vec e_z$, the scalar imaginary $i$ commutes with every unit, and the conjugations are ${}^{\natural}$, $\bar{\cdot}$, ${}^{*} = {}^{\natural}\circ\bar{\cdot}$ and ${}^{\flat} = -{}^{*}$. The biquaternion norm is $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$. The physical dictionary writes a general element as a material coordinate plus an informational coordinate,

$$
\tilde{Q} = \underbrace{(ict)\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z}_{\in\,\mathbb{M}_-} \;+\; \underbrace{(ct')\,e_t + i(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z)}_{\in\,\mathbb{M}_+},
\qquad (x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = xe_1 + ye_2 + ze_3, \quad (x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z) = x'\vec e_x + y'\vec e_y + z'\vec e_z,
$$

with the eight real parameters $q'_0 = c\,t$, $(q_x, q_y, q_z) = (x, y, z)$, $q_t = c\,t'$, $(q'_1, q'_2, q'_3) = (x', y', z')$, and with $c$ the speed of light in the medium.

## The Coefficient Space

**Definition.** The **four-vector** of a biquaternion $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ is the ordered quadruple of its coefficients,

$$
Q^\mu = (Q^t, Q^x, Q^y, Q^z), \qquad Q^t = Q_t, \quad (Q^x, Q^y, Q^z) = (Q_x, Q_y, Q_z).
$$

The index position is fixed by this definition. The component $Q^t$ is the **scalar component** and $Q^x, Q^y, Q^z$ are the **vector components**, the coefficients of the scalar and vector parts of $\tilde{Q}$ and nothing else. No raising or lowering of indices is introduced anywhere in this article, and the reason is stated below: on $\mathbb{C}^4$ there is no pairing with which to move an index.

**Proposition.** The map $\tilde{Q} \mapsto Q^\mu$ is a $\mathbb{C}$-linear isomorphism from $\mathbb{B}$ onto $\mathbb{C}^4$. The coefficient space therefore has complex dimension $4$ and real dimension $8$.

**Proof.** The map sends the basis $e_t, \vec e_x, \vec e_y, \vec e_z$ to the standard basis of $\mathbb{C}^4$ and is extended by linearity; it is bijective on bases, and the action of a complex scalar on the coefficients is the same on both sides.

The coefficient space is **not** the simple module of the algebra. The simple module has complex dimension $2$ and is the carrier of the spinor of the corpus; it is treated in *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*. The number $4$ recurs there and in *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* for two different reasons, and neither is a coincidence: the coefficient space is the algebra itself, of complex dimension $4$, and the regular representation is the algebra acting on itself, so its matrix is $4 \times 4$ for the same count.

### The Real and Imaginary Parts

Each complex component splits into a real part and $i$ times a real part,

$$
Q^\mu = q^\mu + i {q'}^\mu, \qquad q^\mu, {q'}^\mu \in \mathbb{R},
$$

and the eight real numbers so obtained identify the coefficient space with $\mathbb{R}^8$. The split is the coefficient split of the algebra: the quadruple with ${q'}^\mu = 0$ is an element of the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the quadruple with $q^\mu = 0$ is an element of its multiple $i\mathbb{H}_{\mathbb{B}}$, and

$$
\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}
$$

is the real-and-imaginary split of the coefficients read coordinate by coordinate. The other four remarkable subspaces mix the real and imaginary parts, because the involutions that define them combine with the scalar imaginary in different ways; they are tabulated below.

The biquaternion norm does not decompose over these eight real coordinates. Its real part is $\sum_\mu \big( (q^\mu)^2 - ({q'}^\mu)^2 \big)$ and its imaginary part is $2\sum_\mu q^\mu {q'}^\mu$, both real quadratic forms in eight variables, and the positive-definite form $\sum_\mu \big( (q^\mu)^2 + ({q'}^\mu)^2 \big)$ is the squared Euclidean length of the quadruple. That last form is the Hermitian form $\sum_\mu |Q^\mu|^2$ of the algebra, and it is a different object from the biquaternion norm: the biquaternion norm is general plain bilinear and can vanish on a nonzero element, while the Hermitian form is positive definite.

### The Physical Dictionary

The informational and material writings of the Introduction are matched coefficient by coefficient: the four complex coefficients, in physical terms, are

$$
Q^t = c t' + i c t, \qquad Q^x = x + i x', \qquad Q^y = y + i y', \qquad Q^z = z + i z'.
$$

Every complex coefficient therefore carries **one material coordinate and one informational coordinate**: the scalar coefficient carries the two times, and each vector coefficient carries one spatial coordinate of each sector. Read by real and imaginary part, the quadruple $(q^t, q^x, q^y, q^z) = (ct', x, y, z)$ is the informational time together with the material space, and the quadruple $({q'}^0, {q'}^1, {q'}^2, {q'}^3) = (ct, x', y', z')$ is the material time together with the informational space. This is the same mixed ownership that the prime convention records, and it is why the scalar component of a physical four-vector is the one that carries the time.

**The material four-vector.** An element of the material sector has a purely imaginary scalar coefficient and real vector coefficients. Writing its real time parameter as $q'_0$ and its real spatial parameters as $q_x, q_y, q_z$, the element and its four-vector are

$$
\tilde{Q} = iq'_0e_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z \in \mathbb{M}_-, \qquad (Q^t, Q^x, Q^y, Q^z) = (iq'_0, q_x, q_y, q_z).
$$

The four-vectors of relativistic physics are of exactly this shape: the four-position has $q'_0 = ct$ and $(q_x, q_y, q_z) = (x,y,z)$, so its scalar coefficient is $ict = iq'_0$ and its four-vector is $(ict, x, y, z)$, while the four-momentum has $q'_0 = E/c$ and $(q_x, q_y, q_z) = \vec p$.

**The informational four-vector.** An element of the informational sector has a real scalar coefficient and purely imaginary vector coefficients. Writing its real parameters as $q_t$ and $q'_1, q'_2, q'_3$, the element and its four-vector are

$$
\tilde{Q} = q_te_t + iq'_1\vec e_x + iq'_2\vec e_y + iq'_3\vec e_z \in \mathbb{M}_+, \qquad (Q^t, Q^x, Q^y, Q^z) = (q_t, iq'_1, iq'_2, iq'_3).
$$

The informational coordinate is the case $q_t = ct'$ and $(q'_1, q'_2, q'_3) = (x', y', z')$, so its four-vector is $(ct', ix', iy', iz')$.

## The Column and the Dual Row

**Definition.** The **column** of $\tilde{Q}$ is the $4 \times 1$ matrix

$$
Q = \begin{pmatrix} Q^t \\ Q^x \\ Q^y \\ Q^z \end{pmatrix},
$$

and the **row** of $\tilde{Q}$ is its transpose,

$$
Q^{\mathsf{T}} = \begin{pmatrix} Q^t & Q^x & Q^y & Q^z \end{pmatrix}.
$$

The column is the transcribed form of the quadruple, and it is convenient because the product of biquaternions is bilinear. For a fixed $\tilde{Q}$ the map $\tilde{Q}_1 \mapsto \tilde{Q}\tilde{Q}_1$ sends the coefficients of $\tilde{Q}_1$ linearly to the coefficients of the product, so with the column convention it is written as a $4 \times 4$ matrix acting on the column of $\tilde{Q}_1$: the product is the matrix product $\mathsf{M}_4^{L}(\tilde{Q})\,R$, whose four entries are the coefficients of $\tilde{Q}\tilde{Q}_1$, the column of $\tilde{Q}_1$ being written $R$. The matrix $\mathsf{M}_4^{L}(\tilde{Q})$ is the matrix of left multiplication; its entries are the coefficients of $\tilde{Q}$ with signs and no additions, and it is constructed and verified in *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*. The present article records only that the product admits this interpretation.

**The row is the dual, not a further representation.** The row $Q^{\mathsf{T}}$ is the element of the dual space paired with the column by the standard pairing, and the dual of a left module is a right module: it carries the *right* action, $(\varphi\cdot\tilde{Q})(\tilde{Q}_1) = \varphi(\tilde{Q}\tilde{Q}_1)$. The transpose that relates the column picture to the row picture is dressed with quaternion conjugation, so that the transpose of the left matrix of $\tilde{Q}$ is the left matrix of the quaternion conjugate,

$$
\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}} = \mathsf{M}_4^{L}(\tilde{Q}^{\natural}),
$$

which is proved in *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*. A column and a row are the same four complex numbers written in two layouts, and a change of layout is a change of bookkeeping, not a change of representation. The corpus counts three objects in this group — the coefficient space, the algebra acting on its simple module, and the algebra acting on itself — and it does not count the two layouts separately.

## Multiplication in Four-Vector Form

The product of two biquaternions is computed from the basis and separates into a scalar component and three vector components.

**Proposition (the product in components).** Let $\tilde{Q}$ and $\tilde{Q}_1$ be biquaternions with four-vectors $Q^\mu$ and $R^\mu$. Then the four-vector of the product has components

$$
(\tilde{Q}\tilde{Q}_1)^0 = Q^t R^0 - \sum_{k\in\{x,y,z\}} Q^k R^k,
$$

$$
(\tilde{Q}\tilde{Q}_1)^i = Q^t R^i + R^0 Q^i + \sum_{j,k\in\{x,y,z\}} \epsilon^{ijk} Q^j R^k, \qquad i = 1, 2, 3,
$$

where $\epsilon^{ijk}$ is the Levi-Civita symbol on the indices $1, 2, 3$.

**Proof.** Expand the product in the basis, using $e_t e_\mu = e_\mu$ and $e_k^2 = -e_t$. The scalar component collects the terms in which both factors contribute the scalar unit or both contribute the same quaternion unit, $Q^tR^0 e_t + \sum_k Q^kR^k e_k^2 = \big( Q^tR^0 - \sum_k Q^kR^k \big)e_t$, and the terms with two different quaternion units contribute no scalar component. The coefficient of $e_i$ collects $Q^tR^i e_i$ and $Q^iR^0 e_i$ from the mixed scalar–vector pairs, together with the products $Q^jR^k e_je_k$ over the ordered pairs with $\{j,k\} = \{1,2,3\}\setminus\{i\}$. For those, $e_je_k = \epsilon^{ijk}e_i$, the basis being oriented so that $\vec e_x \vec e_y = \vec e_z$, $\vec e_y \vec e_z = \vec e_x$ and $\vec e_z \vec e_x = \vec e_y$; the sum over $j,k$ therefore runs over both orderings and gives the displayed Levi-Civita term.

**Corollary (the commutator).** The commutator of two biquaternions is twice the cross product of their vector components,

$$
\tilde{Q}\tilde{Q}_1 - \tilde{Q}_1\tilde{Q} = 2 \sum_{i\in\{x,y,z\}} \Big( \sum_{j,k\in\{x,y,z\}} \epsilon^{ijk} Q^j R^k \Big) e_i .
$$

The scalar component and the symmetric part $Q^tR^i + R^0Q^i$ of each vector component are unchanged by exchanging the factors; the Levi-Civita term is the only part that changes sign, and it is therefore the only trace of non-commutativity visible in this realization. In particular the commutator always has zero scalar component, so it lies in the vector subspace $\mathrm{Vect}(\mathbb{B})$ — the derived subspace of the algebra, which is the complex space sector — and it vanishes exactly when the vector parts of the two factors are linearly dependent over $\mathbb{C}$.

**Example.** For $\tilde{Q} = e_t + \vec e_x$ and $\tilde{Q}_1 = e_t + \vec e_y$ the four-vectors are $Q^\mu = (1,1,0,0)$ and $R^\mu = (1,0,1,0)$. The product formula gives $(\tilde{Q}\tilde{Q}_1)^\mu = (1,1,1,1)$, that is, $\tilde{Q}\tilde{Q}_1 = e_t + \vec e_x + \vec e_y + \vec e_z$, while the reversed product gives $(\tilde{Q}_1\tilde{Q})^\mu = (1,1,1,-1)$, since the only nonzero Levi-Civita term changes sign. The two products differ by $2\vec e_z$, which is twice the cross product of the vector parts.

### The Multiplication Table of the Basis

The product formula is the row-by-row interpretation of the multiplication table of the basis, displayed once for reference; the entry in row $\mu$ and column $\nu$ is $e_\mu e_\nu$.

| $e_\mu \backslash e_\nu$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $-e_t$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $\vec e_y$ | $-\vec e_z$ | $-e_t$ | $\vec e_x$ |
| $\vec e_z$ | $\vec e_z$ | $\vec e_y$ | $-\vec e_x$ | $-e_t$ |

The first row and the first column reproduce the basis, since $e_t$ is the identity. In the remaining $3 \times 3$ block the table is skew off the diagonal, $e_je_k = -e_ke_j$ for distinct $j,k$, while its diagonal entries are $-e_t$. The scalar component of a product is read from the diagonal of the table, which is why it carries $Q^tR^0 - \sum_k Q^kR^k$, and the vector components are read from the off-diagonal entries, which is why they carry both the symmetric scalar–vector part and the antisymmetric Levi-Civita term. The same table read as a map on the coefficient space is the regular matrix of *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*.

## The Conjugations in Coordinates

The algebra carries the quaternion conjugation ${}^{\natural}$, the complex conjugation $\bar{\cdot}$, the Hermitian conjugation ${}^{*} = {}^{\natural}\circ\bar{\cdot}$ and the anti-Hermitian conjugation ${}^{\flat} = -{}^{*}$. In coordinates, quaternion conjugation negates the vector components, complex conjugation conjugates every component, and Hermitian conjugation does both.

**Proposition (conjugations in coordinates).** For a biquaternion with four-vector $Q^\mu$,

$$
(\tilde{Q}^{\natural})^\mu = (Q^t, -Q^x, -Q^y, -Q^z),
$$

$$
(\tilde{Q}^{*})^\mu = \big( (Q^t)^{*}, (Q^x)^{*}, (Q^y)^{*}, (Q^z)^{*} \big),
$$

$$
(\tilde{Q}^{*})^\mu = \big( (Q^t)^{*}, -(Q^x)^{*}, -(Q^y)^{*}, -(Q^z)^{*} \big), \qquad (\tilde{Q}^{\flat})^\mu = -(\tilde{Q}^{*})^\mu .
$$

**Proof.** Quaternion conjugation fixes $e_t$ and sends $e_k$ to $-e_k$ while leaving every coefficient untouched, so it acts on the coefficients by $(Q^t, Q^x, Q^y, Q^z) \mapsto (Q^t, -Q^x, -Q^y, -Q^z)$. Complex conjugation fixes every basis element and conjugates the central scalar $i$, hence conjugates each coefficient. Hermitian conjugation is their composite, and $\flat$ is its negative.

The three involutions ${}^{\natural}$, $\bar{\cdot}$ and ${}^{*}$ commute and generate a Klein four-group with the identity; the fourth involution $\flat$ is not independent of them, since $\flat = -{}^{*}$. This is why the fixed-point subspaces come in three pairs and not four.

**Example.** For the element

$$
\tilde{Q} = (2+i)e_t + (1-i)\vec e_x + 3\vec e_y + ie_3, \qquad Q^\mu = (2+i, \, 1-i, \, 3, \, i),
$$

the four conjugations have four-vectors

$$
\tilde{Q}^{\natural} \leftrightarrow (2+i, \, -1+i, \, -3, \, -i), \qquad \tilde{Q}^{*} \leftrightarrow (2-i, \, 1+i, \, 3, \, -i),
$$

$$
\tilde{Q}^{*} \leftrightarrow (2-i, \, -1-i, \, -3, \, i), \qquad \tilde{Q}^{\flat} \leftrightarrow (-2+i, \, 1+i, \, 3, \, -i),
$$

and each is an involution. The Hermitian part $\tfrac12(\tilde{Q} + \tilde{Q}^{*})$ has four-vector $(2, -i, 0, i)$: a real scalar component and purely imaginary vector components, as the table of subspaces requires. In physical terms this element carries the informational time $ct' = 2$ on the scalar component together with the material time $ct = 1$, and its real vector components are the material spatial coordinates $(x,y,z) = (1,3,0)$ while its imaginary ones are the informational $(x',y',z') = (-1,0,1)$.

**Consequences for the physical coordinates.** The conjugation rules are the coordinate form of the statement that the material coordinates are the imaginary part of the quadruple and the informational ones its real part. Quaternion conjugation keeps the material scalar and negates the material vector; complex conjugation conjugates every coefficient and so exchanges the role of informational and material in each slot; Hermitian conjugation does both, and its fixed quadruples are exactly those with a real scalar component and purely imaginary vector components, the informational four-vectors. The anti-fixed quadruples of ${}^{*}$ are the material four-vectors, and this is the sense in which $\flat$ is the real structure of the framework.

## Remarkable Subspaces

Each involution cuts out a fixed subspace and an anti-fixed subspace, and the three involutions together produce the remarkable real subspaces of $\mathbb{B}$.

Each of the remarkable subspaces is displayed below as a chain of three quadruples: in the complex coefficients $Q^t, Q^x, Q^y, Q^z$; in the real parameters $q_\mu, q'_\mu$ of the split $Q_\mu = q_\mu + iq'_\mu$; and in the physical coordinates. The dictionary from the real parameters to the physical names is one and the same for all six,

$$
q_t = ct', \quad q'_0 = ct, \quad q_x = x, \quad q_y = y, \quad q_z = z, \quad q'_1 = x', \quad q'_2 = y', \quad q'_3 = z' ,
$$

the unprimed slot carrying the informational time $ct'$ and the material space $x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$, the primed slot the material time $ct$ and the informational space $x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z$.

**Definition.** The **remarkable subspaces** are

$$
\mathbb{C}_{\mathbb{B}} = \{\tilde{Q} : \tilde{Q}^{\natural} = \tilde{Q}\}, \qquad \mathrm{Vect}(\mathbb{B}) = \{\tilde{Q} : \tilde{Q}^{\natural} = -\tilde{Q}\},
$$

$$
\mathbb{H}_{\mathbb{B}} = \{\tilde{Q} : \tilde{Q}^{*} = \tilde{Q}\}, \qquad i\mathbb{H}_{\mathbb{B}} = \{\tilde{Q} : \tilde{Q}^{*} = -\tilde{Q}\},
$$

$$
\mathbb{M}_+ = \{\tilde{Q} : \tilde{Q}^{*} = \tilde{Q}\}, \qquad \mathbb{M}_- = \{\tilde{Q} : \tilde{Q}^{\flat} = \tilde{Q}\}.
$$

**Proposition (coordinate conditions).** In terms of the four-vector $Q^\mu$ the remarkable subspaces are characterized as follows.

| Subspace | Coordinate condition | Algebraic name | Physical name | real dim |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $Q^x = Q^y = Q^z = 0$ | centre | complex time sector | $2$ |
| $\mathrm{Vect}(\mathbb{B})$ | $Q^t = 0$ | vector | complex space sector | $6$ |
| $\mathbb{H}_{\mathbb{B}}$ | $Q^t, Q^x, Q^y, Q^z \in \mathbb{R}$ | quaternion | real sector | $4$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $Q^t, Q^x, Q^y, Q^z \in i\mathbb{R}$ | antiquaternion | imaginary sector | $4$ |
| $\mathbb{M}_+$ | $Q^t \in \mathbb{R}$, $Q^x, Q^y, Q^z \in i\mathbb{R}$ | Hermitian | informational sector | $4$ |
| $\mathbb{M}_-$ | $Q^t \in i\mathbb{R}$, $Q^x, Q^y, Q^z \in \mathbb{R}$ | anti-Hermitian | material sector | $4$ |

**Proof.** The conditions are the componentwise interpretation of the four conjugation rules of the preceding section. For $\mathbb{C}_{\mathbb{B}}$ and $\mathrm{Vect}(\mathbb{B})$, quaternion conjugation fixes the scalar component and negates each vector component. For $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, complex conjugation fixes or negates each coefficient according to whether it is real or purely imaginary. For $\mathbb{M}_+$ and $\mathbb{M}_-$, Hermitian conjugation conjugates and then negates the vector components, so the fixed quadruples have a real scalar component and purely imaginary vector components, and the anti-fixed quadruples have a purely imaginary scalar component and real vector components.

The table shows that the three decompositions of the algebra read in coordinates as the splitting of the quadruple into its real and imaginary parts in three different ways:

$$
\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B}) = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}} = \mathbb{M}_+ \oplus \mathbb{M}_- .
$$

The first separates the scalar component from the three vector components, the second separates the real coefficients from the imaginary ones, and the third separates the material quadruples from the informational ones. The three splits are different, none is a refinement of another, and how they cross is the subject of *Relations Between Subspaces*.

### The Centre Subspace $\mathbb{C}_{\mathbb{B}}$

Two-dimensional and purely temporal, without a single spatial coordinate. The scalar coefficient is an arbitrary complex number carrying the two times, and the quadruple is $(Q_t, 0, 0, 0)$:

$$
\tilde{Q} = Q_te_t \longleftrightarrow (Q^t, Q^x, Q^y, Q^z) = (Q_t,\ 0,\ 0,\ 0) = (q_t + iq'_0,\ 0,\ 0,\ 0) = (ct' + ict,\ 0,\ 0,\ 0),
$$

with $Q_t = q_t + iq'_0$, $q_t = ct'$ and $q'_0 = ct$, and the biquaternion norm $\langle\tilde{Q}\rangle_{\natural} = Q_t^2 = c^2(t')^2 - c^2t^2 + 2i\,c^2t't$. It is the fixed space of quaternion conjugation, so quaternion conjugation acts on it as the identity — the axis of $\mathbb{B}$.

### The Vector Subspace $\mathrm{Vect}(\mathbb{B})$

Six-real-dimensional and purely spatial, the only one of the remarkable subspaces that is not four- or two-dimensional. The scalar coefficient vanishes and each of the three vector coefficients is one material spatial coordinate together with one informational coordinate:

$$
\tilde{Q} = Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z \longleftrightarrow (Q^t, Q^x, Q^y, Q^z) = (0,\ Q_x,\ Q_y,\ Q_z) = (0,\ q_x + iq'_1,\ q_y + iq'_2,\ q_z + iq'_3) = (0,\ x + ix',\ y + iy',\ z + iz'),
$$

where $Q_k = q_k + iq'_k$ with $q_k = x_k$ and $q'_k = x'_k$, and the biquaternion norm is $\langle\tilde{Q}\rangle_{\natural} = (x+ix')^2 + (y+iy')^2 + (z+iz')^2$. It is the anti-fixed space of quaternion conjugation and the spatial counterpart of the centre: the centre has the two times in one complex number, the vector subspace the two spaces in three.

### The Quaternion Subspace $\mathbb{H}_{\mathbb{B}}$

The fixed space of complex conjugation: all four coefficients real, so the scalar imaginary plays no role at all, and the quadruple mixes the informational time with the material space,

$$
\tilde{Q} = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu \longleftrightarrow (Q^t, Q^x, Q^y, Q^z) = (Q_t,\ Q_x,\ Q_y,\ Q_z) = (q_t,\ q_x,\ q_y,\ q_z) = (ct',\ x,\ y,\ z),
$$

with $Q_\mu = q_\mu$ real, $q_t = ct'$ and $q_k = x_k$, and the biquaternion norm $\langle\tilde{Q}\rangle_{\natural} = c^2(t')^2 +x^2+y^2+z^2$. The biquaternion norm is a sum of four squares with no minus sign, so it is positive definite and vanishes only at the zero element; the unit elements of this subspace are the rotation rotors.

### The Antiquaternion Subspace $i\mathbb{H}_{\mathbb{B}}$

The anti-fixed space of complex conjugation: all four coefficients purely imaginary, so the quadruple takes the other assignment of the two times and the two spaces,

$$
\tilde{Q} = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu \longleftrightarrow (Q^t, Q^x, Q^y, Q^z) = (Q_t,\ Q_x,\ Q_y,\ Q_z) = (iq'_0,\ iq'_1,\ iq'_2,\ iq'_3) = (ict,\ ix',\ iy',\ iz'),
$$

with $Q_\mu = iq'_\mu$, $q'_0 = ct$ and $q'_k = x'_k$, and the biquaternion norm $\langle\tilde{Q}\rangle_{\natural} = -\big( c^2t^2 +x'^2+y'^2+z'^2 \big)$. It is $i$ times the quaternion subspace, and the biquaternion norm is the negative of a sum of four squares, so it too vanishes only at the zero element.

### The Material Subspace $\mathbb{M}_-$

The anti-fixed space of Hermitian conjugation: a purely imaginary scalar coefficient and three real vector coefficients, three real components and one imaginary one,

$$
\tilde{R} = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu \longleftrightarrow (Q^t, Q^x, Q^y, Q^z) = (Q_t,\ Q_x,\ Q_y,\ Q_z) = (iq'_0,\ q_x,\ q_y,\ q_z) = (ict,\ x,\ y,\ z),
$$

with $Q_t = iq'_0$, $Q_k = q_k$, $q'_0 = ct$ and $q_k = x_k$, and the biquaternion norm $\langle\tilde{Q}\rangle_{\natural} = -c^2t^2 +x^2+y^2+z^2$. The single minus sign is the $ict$ convention, and the signature $(3,1)$ of the biquaternion norm is the Minkowski one: this is the home of the four-vectors of relativistic physics.

### The Informational Subspace $\mathbb{M}_+$

The fixed space of Hermitian conjugation: a real scalar coefficient and three purely imaginary vector coefficients,

$$
\tilde{Q} = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu \longleftrightarrow (Q^t, Q^x, Q^y, Q^z) = (Q_t,\ Q_x,\ Q_y,\ Q_z) = (q_t,\ iq'_1,\ iq'_2,\ iq'_3) = (ct',\ ix',\ iy',\ iz'),
$$

with $Q_t = q_t$, $Q_k = iq'_k$, $q_t = ct'$ and $q'_k = x'_k$, and the biquaternion norm $\langle\tilde{Q}\rangle_{\natural} = c^2(t')^2 -(x'^2+y'^2+z'^2)$, the transpose of the material condition, of signature $(1,3)$. The two sectors are exchanged by multiplication by $i$: $i\mathbb{M}_- = \mathbb{M}_+$, since $i\,(ict, x, y, z) = (-ct, ix, iy, iz)$ has the informational shape.

## The Biquaternion Norm

**Definition.** The **biquaternion norm** of a biquaternion is the central element

$$
\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2 = (Q^t)^2 + (Q^x)^2 + (Q^y)^2 + (Q^z)^2 \in \mathbb{C}.
$$

In four-vector form the biquaternion norm has **all four signs positive**, and the Gram matrix of its polar form is the identity $\mathrm{diag}(+1,+1,+1,+1)$.

**Proposition (why all four signs are positive).** For every biquaternion $\tilde{Q}$, $\tilde{Q}\tilde{Q}^{\natural} = \sum_{\mu\in\{t,x,y,z\}} Q_\mu^2$, a complex scalar.

**Proof.** Expand $\tilde{Q}\tilde{Q}^{\natural} = \big(\sum_\mu Q_\mu e_\mu\big)\big(Q_te_t - \sum_k Q_k e_k\big)$. The cross terms between $e_t$ and the vector units cancel between the two orders. The remaining terms are $Q_t^2e_t$ together with $\sum_k Q_k^2 e_k^2 = -\sum_k Q_k^2e_t$ and the mixed terms $-Q_jQ_ke_je_k$ over ordered pairs with $j \neq k$. The pairs $(j,k)$ and $(k,j)$ carry the same coefficient $Q_jQ_k$ and their basis products are negatives, so the pair contributes a multiple of $e_je_k + e_ke_j = 0$ and cancels. Collecting the surviving scalar terms gives $Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2$.

Two consequences matter. First, the biquaternion norm is a **general plain bilinear** form of rank four, multiplicative, $\langle\tilde{P}\tilde{Q}\rangle_{\natural} = \langle\tilde{P}\rangle_{\natural}\langle\tilde{Q}\rangle_{\natural}$, and its Gram matrix on the coefficient space is the identity, so no minus sign of a spacetime signature is in it. Second, it is nevertheless not a definite form: it can vanish on a nonzero element, and it does so exactly on the nonzero solutions of $\sum_\mu Q_\mu^2 = 0$, which are the zero divisors of the algebra. The biquaternion norm is therefore not a norm in the analytic sense, and the set of its zeros is the algebra's null cone.

### The Two Real Restrictions

The indefinite form is not on the coefficient space but on the two real sectors, where the four complex coordinates become four real coordinates and the biquaternion norm becomes real-valued.

**Proposition (the real restrictions).** On the material sector $\mathbb{M}_-$, writing $Q^t = i a^0$ and $Q^k = a^k$ with $a^\mu \in \mathbb{R}$, the biquaternion norm restricts to

$$
\langle\tilde{Q}\rangle_{\natural} = -(a^0)^2 + (a^1)^2 + (a^2)^2 + (a^3)^2,
$$

a real quadratic form of signature $(3,1)$; with $a^0 = ct$ and $a^k = x_k$ it is the Minkowski interval $-c^2t^2 +x^2+y^2+z^2$. On the informational sector $\mathbb{M}_+$, writing $Q^t = a^0$ and $Q^k = i a^k$ with $a^\mu \in \mathbb{R}$, it restricts to

$$
\langle\tilde{Q}\rangle_{\natural} = (a^0)^2 - (a^1)^2 - (a^2)^2 - (a^3)^2,
$$

a real quadratic form of signature $(1,3)$; with $a^0 = ct'$ and $a^k = x'_k$ it is $c^2(t')^2 -(x'^2+y'^2+z'^2)$.

**Proof.** Substitute the coordinate conditions of the table above into $\sum_\mu (Q^\mu)^2$. On $\mathbb{M}_-$ the scalar term is $(ia^0)^2 = -(a^0)^2$ and the three vector terms are $(a^k)^2$; on $\mathbb{M}_+$ the scalar term is $(a^0)^2$ and the three vector terms are $(ia^k)^2 = -(a^k)^2$.

The real sector $\mathbb{H}_{\mathbb{B}}$ is the case in which no coefficient carries the $i$, and its biquaternion norm is the positive-definite $q_t^2 + q_x^2 + q_y^2 + q_z^2$ of signature $(4,0)$. The two forms are exchanged by multiplication by the scalar imaginary, since $\langle i\tilde{Q}\rangle_{\natural} = -\langle\tilde{Q}\rangle_{\natural}$ on every element and $\mathbb{M}_+ = i\mathbb{M}_-$, $\mathbb{M}_- = i\mathbb{M}_+$. The Lorentzian signature is therefore an **output** of the framework and not an input to it: the four coefficients start on an equal footing with all four signs positive, and the minus sign of the interval appears only when a real coordinate is placed on a direction whose coefficient carries the factor $i$.

**The null cone and the causal classes.** The zeros of the biquaternion norm are the light cone of the framework. On $\mathbb{M}_-$ the condition $\langle\tilde{Q}\rangle_{\natural} = 0$ is $-c^2t^2 +x^2+y^2+z^2 = 0$, the null cone of Minkowski space, and on the algebra at large it is the set of zero divisors. The interval is invariant under the rotor conjugation $\tilde{Q} \mapsto \tilde U\tilde{Q}\tilde U^{*}$ with $\langle\tilde U\rangle_{\natural} = e_t$, so no element of the restricted Lorentz group can move a displacement from one causal class to another; the causal structure of the framework and the orbit decomposition of the cone are developed in the companion articles on causality and on the Lorentz group.

### The Inverse in Coordinates

The invertibility criterion, that $\tilde{Q}$ is a unit exactly when $\langle\tilde{Q}\rangle_{\natural} \neq 0$, is that of the mathematics corpus; what the four-vector realization adds is the coordinate form of the inverse.

**Proposition (the inverse in coordinates).** For an invertible biquaternion $\tilde{Q}$,

$$
\tilde{Q}^{-1} = \frac{\tilde{Q}^{\natural}}{\langle\tilde{Q}\rangle_{\natural}}, \qquad \big(\tilde{Q}^{-1}\big)^\mu = \Big( \frac{Q^t}{\langle\tilde{Q}\rangle_{\natural}}, \, -\frac{Q^x}{\langle\tilde{Q}\rangle_{\natural}}, \, -\frac{Q^y}{\langle\tilde{Q}\rangle_{\natural}}, \, -\frac{Q^z}{\langle\tilde{Q}\rangle_{\natural}} \Big).
$$

**Proof.** With $\langle\tilde{Q}\rangle_{\natural} \neq 0$, the element $\tilde{Q}^{\natural}/\langle\tilde{Q}\rangle_{\natural}$ is a two-sided inverse because $\tilde{Q}\tilde{Q}^{\natural} = \tilde{Q}^{\natural}\tilde{Q} = \langle\tilde{Q}\rangle_{\natural}$ is central. Its coordinate form is the vector $\tilde{Q}^{\natural}$, whose components are $(Q^t, -Q^x, -Q^y, -Q^z)$, divided by the complex scalar $\langle\cdot\rangle_{\natural}$.

**Example.** For the element $\tilde{Q} = (2+i)e_t + (1-i)\vec e_x + 3\vec e_y + ie_3$ of the preceding example,

$$
\langle\tilde{Q}\rangle_{\natural} = (2+i)^2 + (1-i)^2 + 3^2 + i^2 = (3+4i) + (-2i) + 9 - 1 = 11 + 2i \neq 0,
$$

so $\tilde{Q}$ is a unit, with four-vector inverse $\tfrac{1}{11+2i}(2+i, -1+i, -3, -i)$. Under the conjugations the biquaternion norm becomes $\langle\tilde{Q}^{\natural}\rangle_{\natural} = 11+2i$, $\langle\tilde{Q}^{*}\rangle_{\natural} = 11-2i$ and $\langle\bar{\tilde{Q}}\rangle_{\natural} = 11-2i$, and multiplication by $i$ reverses its sign, $\langle i\tilde{Q}\rangle_{\natural} = -11-2i$.

## The Four-Vectors of Relativistic Physics

The material sector is the home of the four-vectors, and the four-vector representation makes each of them a quadruple with a purely imaginary scalar entry and three real vector entries. The four-vectors below are the standard ones; the algebra's contribution is the uniform shape of their quadruples and the fact that the interval is the biquaternion norm.

**The four-position.**

$$
\tilde{R} = ict\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z, \qquad \langle\tilde{R}\rangle_{\natural} = -c^2t^2 +x^2+y^2+z^2,
$$

which is the Minkowski interval. The four-position is the element whose biquaternion norm vanishes on the light cone through the origin, and it is the object acted on by the rotor conjugation.

**The four-velocity.** With $\gamma$ the Lorentz factor of a particle of velocity $\vec v$,

$$
\tilde{V} = i\gamma c\,e_t + \gamma\vec v, \qquad \langle\tilde{V}\rangle_{\natural} = -\gamma^2\big( c^2 - \vec v^2 \big) = -c^2 .
$$

The biquaternion norm of the four-velocity is **constant**, $-c^2$, on every timelike world line, which is the coordinate form of the statement that $\mathrm{d}\tau = \sqrt{-\mathrm{d}s^2}/c$ is the proper time.

**The four-momentum.**

$$
\tilde{P} = i\frac{E}{c}e_t + \vec p, \qquad \langle\tilde{P}\rangle_{\natural} = -\frac{E^2}{c^2} + \vec p^y .
$$

For an on-shell particle the dispersion relation $E^2 = c^2\vec p^y + m^2c^4$ gives

$$
\langle\tilde{P}\rangle_{\natural} = -\Big( \frac{E^2}{c^2} - \vec p^y \Big) = -m^2c^2 ,
$$

so the mass-shell condition is the statement that the four-momentum lies on the sphere of radius $mc$ in the biquaternion norm, and the mass is read off the biquaternion norm of the four-momentum. The dispersion relation itself, in biquaternionic form, is the subject of the wave-mechanics articles.

**The four-current and the four-potential.** The electric four-current is

$$
\tilde{J} = ic\rho\,e_t + \vec J, \qquad \langle\tilde{J}\rangle_{\natural} = -\rho^2c^2 + \vec J^2 ,
$$

and the four-potential is

$$
\tilde{A} = i\frac{\phi}{c}e_t + \vec A, \qquad \langle\tilde{A}\rangle_{\natural} = -\frac{\phi^2}{c^2} + \vec A^2 .
$$

Neither biquaternion norm is fixed on general configurations; what is invariant is the transformation law, which is the rotor conjugation, and the gauge freedom, which is the addition of a gradient.

**The gradient.** The biquaternionic gradient has the shape of a material four-vector whose entries are derivatives,

$$
\tilde{\nabla} = e_t\,\partial/\partial Q_t + \vec e_x\,\partial/\partial Q_x + \vec e_y\,\partial/\partial Q_y + \vec e_z\,\partial/\partial Q_z, \qquad \tilde{\nabla} \in \mathbb{M}_- ,
$$

with quadruple $(\partial/\partial Q_t, \partial/\partial Q_x, \partial/\partial Q_y, \partial/\partial Q_z)$. Its biquaternion norm is the d'Alembertian,

$$
\langle\tilde{\nabla}\rangle_{\natural} = \tilde{\nabla}\tilde{\nabla}^{\natural} = \partial^2/\partial Q_t^2 + \partial^2/\partial Q_x^2 + \partial^2/\partial Q_y^2 + \partial^2/\partial Q_z^2 = \Box ,
$$

the all-plus sign of the biquaternion norm being exactly what makes the spatial part of the d'Alembertian positive with the $ict$ convention. The gradient is the case in which the material four-vector is an operator, and the wave equation $\Box\tilde{\Psi} = 0$ is the statement that the biquaternion norm of the gradient annihilates the field.

**No index is raised or lowered.** The quadruple is written $Q^\mu$ with an upper index, and the index stays where it is: on $\mathbb{C}^4$ no metric is fixed, so the index is never lowered, and the biquaternion norm cannot serve as one because it is general plain bilinear — symmetric and non-degenerate, of rank four, but neither Hermitian nor positive definite. Physically, the $ict$ convention is what puts the metric into the **coefficient** instead of into a contraction rule: the material four-vector is $(ict, x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$ rather than $(ct, x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$, and the interval is then the sum of squares with no explicit scalar product. The corpus's metric $\eta = \mathrm{diag}(-1,+1,+1,+1)$ is the level-2 interpretation of the same object, used when a contraction of four-vectors is written explicitly; the level-1 object is the identity Gram matrix on $\mathbb{C}^4$, and the minus sign appears only when the material real coordinates are put on the quadruple.

## Physical Readings

The four coefficients read as four coordinates, and the article's own interpretation is the four-vector. Read on the clock, the scalar coefficient is the central coordinate and the three vector coefficients are the spatial part, so the representation is the framework's temporal/spatial split at the level of coordinates. Read on the four conjugations, the real and the imaginary parts of a coefficient are the two sectors, so a coordinate and a sector are two interpretations of one number, which is the dictionary the physics articles use without restating it.

The four complex coordinates are read as a **spacetime event carrying an internal state**: the eight real parameters are the four coordinates the $ict$ convention realises together with the four internal data on which the phase and the sector act, so one element is a point of spacetime and its internal label at once.

## Summary

The four-vector representation reads a biquaternion $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ as its quadruple of complex coefficients $Q^\mu = (Q^t, Q^x, Q^y, Q^z)$, with $Q^t = Q_t$ the scalar component and $(Q^x, Q^y, Q^z) = (Q_x, Q_y, Q_z)$ the vector components. It is a $\mathbb{C}$-linear isomorphism onto $\mathbb{C}^4$, of complex dimension four and real dimension eight, and it supplies the space on which the regular operator of *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* is written. Physically, each complex coefficient carries one material and one informational coordinate: $Q^t = ct' + ict$ and $Q^k = x_k + ix'_k$, so that the material four-vector is the quadruple $(ict, x, y, z)$ with a purely imaginary scalar entry, that is $Q^t = iq'_0$ with $q'_0 = ct$.

The product in components has scalar part $Q^tR^0 - \sum_k Q^kR^k$ and vector part $Q^tR^i + R^0Q^i + \sum_{j,k}\epsilon^{ijk}Q^jR^k$, and the Levi-Civita term is the only trace of non-commutativity; the commutator is twice the cross product of the vector parts and lies in the complex space sector. The three involutions ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ act by negating the vector components, conjugating every component, and doing both, and the remarkable subspaces are the resulting coordinate conditions: the informational sector is the quadruples with real scalar component and purely imaginary vector components, the material sector the transpose of that condition. The biquaternion norm is $\sum_\mu (Q^\mu)^2$, with all four signs positive on $\mathbb{C}^4$ because each quaternion unit squares to $-e_t$ and the cross terms cancel; it restricts to signature $(3,1)$ on the material sector, where it is the Minkowski interval $-c^2t^2 +x^2+y^2+z^2$, and to signature $(1,3)$ on the informational sector, and it vanishes exactly on the zero divisors, which are the light cone.

The four-vectors of relativistic physics are the material elements: the four-position with biquaternion norm the interval, the four-velocity with biquaternion norm the constant $-c^2$, the four-momentum with biquaternion norm $-m^2c^2$ on the mass shell, the four-current and four-potential with their respective biquaternion norms, and the gradient, whose biquaternion norm is the d'Alembertian $\Box = \partial^2/\partial Q_t^2 + \Delta$. The index on $Q^\mu$ is never raised or lowered, because the coefficient space carries no metric of its own; the $ict$ convention carries the metric in the coefficient, and the explicit metric $\eta = \mathrm{diag}(-1,+1,+1,+1)$ is the level-2 form used when a contraction is written out.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | The biquaternion algebra, isomorphic to $M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $e_k^2 = -e_t$, $\vec e_x \vec e_y = \vec e_z$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\tilde{Q} = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu$ | Developed form, $Q_\mu \in \mathbb{C}$ |
| $Q^\mu = (Q^t, Q^x, Q^y, Q^z)$ | The four-vector; $Q^t = Q_t$ the scalar component, $(Q^x,Q^y,Q^z) = (Q_x,Q_y,Q_z)$ the vector components |
| $Q^\mu = q^\mu + i{q'}^\mu$ | Real and imaginary parts of each component |
| $Q$, $Q^{\mathsf{T}}$ | The column and the dual row of the four-vector |
| $\mathsf{M}_4^{L}(\tilde{Q})$, $\mathsf{M}_4^{R}(\tilde{Q})$ | Matrices of left and right multiplication, constructed in *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*; $\mathsf{M}_4^{L}(\tilde{Q})^{\mathsf{T}} = \mathsf{M}_4^{L}(\tilde{Q}^{\natural})$ |
| $\epsilon^{ijk}$ | Levi-Civita symbol on the indices $1, 2, 3$ |
| $\tilde{Q}^{\natural}, \tilde{Q}^{*}, \tilde{Q}^{*}, \tilde{Q}^{\flat} = -\tilde{Q}^{*}$ | Quaternion, complex, Hermitian and anti-Hermitian conjugation |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B}), \mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}, \mathbb{M}_+, \mathbb{M}_-$ | The remarkable subspaces; coordinate conditions in the table above |
| $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ | The biquaternion norm, the diagonal of the general quaternionic bilinear form and multiplicative; Gram matrix $\mathrm{diag}(+1,+1,+1,+1)$ on $\mathbb{C}^4$, signature $(3,1)$ on $\mathbb{M}_-$ and $(1,3)$ on $\mathbb{M}_+$ |
| $\tilde{Q}^{-1} = \tilde{Q}^{\natural}/\langle\tilde{Q}\rangle_{\natural}$ | The inverse in coordinates |
| $c$, $c_0$ | Speed of light in the medium, $c = 1/\sqrt{\epsilon\mu}$, and its vacuum value |
| $ict$, $x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ | The material coordinate; the four-position is $(ict, x, y, z)$ |
| $ct'$, $i(x'\,\vec e_x+y'\,\vec e_y+z'\,\vec e_z) = i x'\vec e_x + iy'\vec e_y + iz'\vec e_z$ | The informational coordinate |
| $q'_0, q_x, q_y, q_z$ | Real parameters of a material four-vector, $\tilde{Q} = iq'_0e_t + q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$; $q'_0 = ct$, $(q_x,q_y,q_z) = (x,y,z)$ for the four-position |
| $q_t, q'_1, q'_2, q'_3$ | Real parameters of an informational four-vector, $\tilde{Q} = q_te_t + iq'_1\vec e_x + iq'_2\vec e_y + iq'_3\vec e_z$; $q_t = ct'$, $(q'_1,q'_2,q'_3) = (x',y',z')$ |
| $\tilde{V}$, $\tilde{P}$, $\tilde{J}$, $\tilde{A}$ | Four-velocity, four-momentum, four-current, four-potential; $\langle\tilde{V}\rangle_{\natural} = -c^2$, $\langle\tilde{P}\rangle_{\natural} = -m^2c^2$ on shell |
| $\tilde{\nabla} = e_t\,\partial/\partial Q_t + \vec e_x\,\partial/\partial Q_x + \vec e_y\,\partial/\partial Q_y + \vec e_z\,\partial/\partial Q_z$ | Biquaternionic gradient; $\langle\tilde{\nabla}\rangle_{\natural} = \Box$ |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \partial^2/\partial Q_t^2 + \Delta$ | d'Alembertian, series convention |
| $\eta = \mathrm{diag}(-1,+1,+1,+1)$ | The $ict$-coordinate metric of the explicit contractions (level 2) |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Dublin, 1853), for the origin of the quaternion coordinates and for the scalar and vector parts of a quaternion.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions", *Proceedings of the London Mathematical Society* **4** (1873) 381–395, for the first systematic treatment of the complexified quaternions.
- Hermann Minkowski, "Raum und Zeit" (1909), for the four-vector formulation of spacetime and the invariant interval.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), Chapter 3, for the coordinate form of the biquaternion product and its conjugations.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the four-vector realization in applied form.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition (Cambridge University Press, 2001), for the quadratic forms and signatures attached to the biquaternion algebra.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the computation with quaternion and biquaternion coordinates.
- John David Jackson, *Classical Electrodynamics*, 3rd edition (Wiley, 1999), for the covariant four-vector formalism of the four-current and four-potential and for the $ict$ convention in its historical use.
