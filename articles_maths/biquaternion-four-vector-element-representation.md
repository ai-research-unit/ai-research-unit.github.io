
# __Biquaternion Four-Vector Element Representation__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is the four-dimensional complex algebra with basis $e_0 = 1, e_1, e_2, e_3$, where $e_k^2 = -e_0$ and $e_j e_k = -e_k e_j$ for $j \neq k$, and with a central scalar imaginary $i$ satisfying $i^2 = -1$ and commuting with every $e_\mu$. A general element is written

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3 = \sum_{\mu = 0}^{3} Q_\mu e_\mu, \qquad Q_\mu \in \mathbb{C}.
$$

The algebra, its four conjugations, its six distinguished subspaces and its biquaternion norm are those of the companion article *Biquaternions as a Vector Space over $\mathbb{C}$*, and nothing of that structure is re-derived here except where the coordinate realization requires it.

This article presents the **four-vector realization** of $\mathbb{B}$: the biquaternion read off as its list of four complex coefficients. The word *representation* is used here in the sense of a concrete realization of the algebra as computable objects, the sense in which the companion article *The Clifford Algebra Representation* uses it, and not in the technical sense of a vector space carrying an algebra homomorphism into its endomorphisms. The technical sense is the subject of *Modules over the General Plain Algebra of Biquaternions*. The distinction matters for the articles of this group: the present article is a realization only, because it supplies a space and no action, while the companion articles *Biquaternion 2×2 Matrix Element Representation $M_2(\mathbb{C})$* and *Biquaternion 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$*, below this article, are realizations and representations at once, because each comes with an action on a vector space. This article supplies the coordinate space on which the operator of the third article is written.

The article owns the coefficient space, the column and the row, the component form of the product, the conjugations in coordinates, the six distinguished subspaces as coordinate conditions, and the biquaternion norm with its two real restrictions. It deliberately does not treat the matrix of multiplication on this space, which belongs to *Biquaternion 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$*, below this article; it does not treat the polar forms, which are the subject of *Biquaternion Partial Polar Element Representations*; and it introduces no physical vocabulary. The components below are complex numbers, the scalar and vector components are named for the algebra, and the words *time* and *space* would name an analogy with the four-vector of a physical theory and nothing more.

## The Coefficient Space

**Definition.** The **four-vector** of a biquaternion $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ is the ordered quadruple

$$
Q^\mu = (Q^0, Q^1, Q^2, Q^3), \qquad Q^0 = Q_0, \quad (Q^1, Q^2, Q^3) = (Q_1, Q_2, Q_3).
$$

The coefficient of the unit is written $Q^0$ and the coefficients of the three quaternion units are written $Q^1, Q^2, Q^3$; the position of the index is fixed by this definition, and no lowering or raising of indices is introduced anywhere in this article. The component $Q^0$ is the **scalar component** and $Q^1, Q^2, Q^3$ are the **vector components**; these are the honest names, because they are the coefficients of the scalar and vector parts of $\tilde{Q}$ and nothing else.

Every component is a **complex number**. The realization therefore carries four complex coordinates, equivalently eight real coordinates, and it is the most direct reading of the developed form of $\tilde{Q}$. Two remarks fix the interpretation. First, the scalar component $Q^0$ is a complex number, not a real number; the decomposition of $\tilde{Q}$ into a real and an imaginary part is the decomposition into the quaternion subspace and its multiple by $i$, and it is not the decomposition into scalar and vector components. Second, the quadruple is not an element of a space with a fixed form: the biquaternion norm introduced below has all four signs positive on $\mathbb{C}^4$, so it carries no indefinite pairing on the coefficient space itself. An indefinite form appears only after restriction to a real subspace, and it is treated in its place.

**Proposition.** The map $\tilde{Q} \mapsto Q^\mu$ is a $\mathbb{C}$-linear isomorphism from $\mathbb{B}$ onto $\mathbb{C}^4$. Consequently the coefficient space has complex dimension $4$ and real dimension $8$.

**Proof.** The map sends the basis $e_0, e_1, e_2, e_3$ to the standard basis of $\mathbb{C}^4$ and is extended by linearity; it is bijective on bases, and the scalar action of $\mathbb{C}$ is the action on the coefficients, which is the same on both sides.

The coefficient space $\mathbb{C}^4$ is **not** the simple module of $\mathbb{B}$. The simple module has complex dimension $2$ and is the subject of *Biquaternion 2×2 Matrix Element Representation $M_2(\mathbb{C})$*, below this article; the coefficient space is the algebra itself, of complex dimension $4$, and the two dimensions are different objects, not two views of one. The number $4$ recurs in *Biquaternion 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$* as the size of the matrix of the regular action, and it is the same four for a different reason: the algebra has complex dimension $4$, so the matrix of its left action on itself is $4 \times 4$.

### Real and Imaginary Parts of the Components

Each complex component splits into its real and imaginary parts, $Q^\mu = a^\mu + i b^\mu$ with $a^\mu, b^\mu \in \mathbb{R}$, and the real coordinates $a^0, a^1, a^2, a^3, b^0, b^1, b^2, b^3$ identify the coefficient space with $\mathbb{R}^8$. This is the coordinate form of the real vector space underlying $\mathbb{B}$. Two of the six distinguished subspaces are read directly from the split: the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ is the set of quadruples with $b^\mu = 0$, and its multiple $i\mathbb{H}_{\mathbb{B}}$ is the set with $a^\mu = 0$. The other four subspaces mix the real and imaginary parts, because the involutions that define them combine with the scalar imaginary in different ways.

The decomposition $\tilde{Q} = \tilde{Q}_r + i\tilde{Q}_i$ with $\tilde{Q}_r = \sum_\mu a^\mu e_\mu$ and $\tilde{Q}_i = \sum_\mu b^\mu e_\mu$ both in $\mathbb{H}_{\mathbb{B}}$ is the decomposition into the quaternion and anti-quaternion parts, and it is the real-linear splitting $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$ of the coordinate space. The biquaternion norm does not decompose over the real coordinates: its real part is $\sum_\mu \bigl( (a^\mu)^2 - (b^\mu)^2 \bigr)$ and its imaginary part is $2\sum_\mu a^\mu b^\mu$, both real quadratic forms in eight variables, and the squared Euclidean length of the quadruple is $\sum_\mu |Q^\mu|^2 = \sum_\mu \bigl( (a^\mu)^2 + (b^\mu)^2 \bigr)$, a positive definite quadratic form on $\mathbb{R}^8$. The definite form is the scalar part of the general plain sesquilinear form of the biquaternion, treated in *Biquaternion 2×2 Matrix Element Representation $M_2(\mathbb{C})$*, below this article.

## The Column and the Row

**Definition.** The **column** of $\tilde{Q}$ is the $4 \times 1$ matrix

$$
Q = \begin{pmatrix} Q^0 \\ Q^1 \\ Q^2 \\ Q^3 \end{pmatrix},
$$

the transpose of the four-vector. The **row** of $\tilde{Q}$ is the $1 \times 4$ matrix

$$
Q^{\mathsf{T}} = \begin{pmatrix} Q^0 & Q^1 & Q^2 & Q^3 \end{pmatrix}.
$$

The column is the transcribed form of the same object, and it is convenient because the product of biquaternions is bilinear. For a fixed $\tilde{Q}$, the map $\tilde{R} \mapsto \tilde{Q} \tilde{R}$ sends coefficients linearly to coefficients, so it is a $\mathbb{C}$-linear endomorphism of the coefficient space, and with the column convention it is written as a $4 \times 4$ matrix acting on the column of $\tilde{R}$,

$$
\tilde{Q} \tilde{R} \longleftrightarrow \operatorname{mat}_4(\tilde{Q}) \, R .
$$

The matrix $\operatorname{mat}_4(\tilde{Q})$ is the matrix of left multiplication, each entry of which is a single coefficient of $\tilde{Q}$ carrying a sign and none of which is a sum of coefficients, and it is constructed and verified in *Biquaternion 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$*, below this article. The present article records only that the product rule admits this reading; the operator itself is not developed here.

**Remark (the row is the dual).** The row $Q^{\mathsf{T}}$ is the element of the dual space associated with $Q$ by the standard pairing, and it is **not** a further realization of the algebra. The dual of a left module is a right module, so the row carries the *right* action: an element $\varphi \in \operatorname{Hom}_{\mathbb{C}}(\mathbb{B}, \mathbb{C})$ is multiplied on the right by the rule $(\varphi \cdot \tilde{Q})(\tilde{R}) = \varphi(\tilde{Q}\tilde{R})$. The row associated with $\tilde{Q}$ and the column associated with $\tilde{R}$ are related by transposition dressed with quaternion conjugation: the transpose of the left matrix is the left matrix of the quaternion conjugate, so transposition carries the row picture to the column picture of the conjugate. This is the one place where the row must be stated, and it is stated once; the identity, and the sense in which the right action is the contragredient of the left one, are proved in *Biquaternion 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$*, below this article.

**Remark (what is and is not a representation).** A column and a row are the same four complex numbers written in two layouts. Reading the row as a new representation, and the $4 \times 4$ operator as a further one, would multiply three objects into a larger count with no mathematical content. The count is of **objects**: the coefficient space, the matrix algebra acting on the simple module, and the algebra acting on itself. A change of layout is a change of bookkeeping, not a change of representation.

## Multiplication in Four-Vector Form

The product of two biquaternions is computed from the basis, and it separates into a scalar component and three vector components.

**Proposition (the product in components).** Let $\tilde{Q}$ and $\tilde{R}$ be biquaternions with four-vectors $Q^\mu$ and $R^\mu$. Then the four-vector $(\tilde{Q}\tilde{R})^\mu$ of the product has components

$$
(\tilde{Q}\tilde{R})^0 = Q^0 R^0 - \sum_{k=1}^{3} Q^k R^k,
$$

$$
(\tilde{Q}\tilde{R})^i = Q^0 R^i + R^0 Q^i + \sum_{j,k=1}^{3} \epsilon^{ijk} Q^j R^k, \qquad i = 1, 2, 3,
$$

where $\epsilon^{ijk}$ is the Levi-Civita symbol on the indices $1, 2, 3$.

**Proof.** Expand the product in the basis, using $e_0 e_\mu = e_\mu$ and $e_k^2 = -e_0$. The scalar component collects the terms in which both factors contribute the scalar unit or both contribute the same quaternion unit,

$$
Q^0 R^0 e_0 + \sum_{k=1}^{3} Q^k R^k e_k e_k = \Bigl( Q^0 R^0 - \sum_{k=1}^{3} Q^k R^k \Bigr) e_0,
$$

since $e_k e_k = -e_0$, and the terms with two different quaternion units contribute no scalar component. The coefficient of $e_i$ collects the terms $Q^0 R^i e_i$ and $Q^i R^0 e_i$ from the mixed scalar-vector pairs, together with the products $Q^j R^k e_j e_k$ with $\{j, k\} = \{1, 2, 3\} \setminus \{i\}$. For those last, $e_j e_k = \epsilon^{ijk} e_i$: the basis is oriented so that $e_1 e_2 = e_3$, $e_2 e_3 = e_1$ and $e_3 e_1 = e_2$, which is the stated sign once the two indices are ordered. Hence the coefficient of $e_i$ is the displayed vector component.

**Corollary (non-commutativity in this realization).** The commutator of two biquaternions is twice the cross product of their vector components:

$$
\tilde{Q}\tilde{R} - \tilde{R}\tilde{Q} = 2 \sum_{i=1}^{3} \Bigl( \sum_{j,k=1}^{3} \epsilon^{ijk} Q^j R^k \Bigr) e_i .
$$

The scalar component of the product and the symmetric part $Q^0 R^i + R^0 Q^i$ of each vector component are unchanged by exchanging the factors; the Levi-Civita term is the only part that changes sign. It is therefore the only trace of non-commutativity visible in the four-vector realization. In particular the commutator always has zero scalar component and so lies in the vector subspace spanned by $e_1, e_2, e_3$, and it vanishes exactly when the vector parts $(Q^1, Q^2, Q^3)$ and $(R^1, R^2, R^3)$ are linearly dependent over $\mathbb{C}$.

**Example.** For $\tilde{Q} = e_0 + e_1$ and $\tilde{R} = e_0 + e_2$, the components are $Q^\mu = (1, 1, 0, 0)$ and $R^\mu = (1, 0, 1, 0)$. The product formula gives $(\tilde{Q}\tilde{R})^\mu = (1, 1, 1, 1)$, that is, $\tilde{Q}\tilde{R} = e_0 + e_1 + e_2 + e_3$, while the reversed product gives $(\tilde{R}\tilde{Q})^\mu = (1, 1, 1, -1)$, since the only nonzero Levi-Civita term changes sign. The two products differ by $2 e_3$.

### The Multiplication Table of the Basis

The product formula is the row-by-row reading of the multiplication table of the basis, which is displayed once for reference. The entry in row $\mu$ and column $\nu$ is the product $e_\mu e_\nu$.

| $e_\mu \backslash e_\nu$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
| $e_1$ | $e_1$ | $-e_0$ | $e_3$ | $-e_2$ |
| $e_2$ | $e_2$ | $-e_3$ | $-e_0$ | $e_1$ |
| $e_3$ | $e_3$ | $e_2$ | $-e_1$ | $-e_0$ |

The first row and the first column reproduce the basis, since $e_0$ is the identity. In the remaining $3 \times 3$ block the table is skew off the diagonal, $e_j e_k = -e_k e_j$ for distinct $j, k \in \{1, 2, 3\}$, while its diagonal entries are $-e_0$: each quaternion unit squares to $-e_0$, and the corner $\mu = \nu = 0$ carries $e_0$ because $e_0^2 = e_0$. The scalar component of a product is read from the diagonal of the table, which is why it carries the expression $Q^0R^0 - \sum_k Q^kR^k$, and the vector components are read from the off-diagonal entries, which is why they carry both the symmetric scalar-vector part and the antisymmetric Levi-Civita term. This is the table read in the four-vector realization; the same table read as a map on the coefficient space is the regular matrix of *Biquaternion 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$*, below this article.

## The Conjugations in Coordinates

The biquaternion algebra carries the quaternion conjugation ${}^{\natural}$, the complex conjugation $\bar{\cdot}$, the Hermitian conjugation ${}^{*} = {}^{\natural} \circ \bar{\cdot}$, and the anti-Hermitian conjugation ${}^{\flat} = -{}^{*}$. In coordinates, quaternion conjugation negates the vector components, complex conjugation conjugates every component, and Hermitian conjugation does both.

**Proposition (conjugations in coordinates).** For a biquaternion with four-vector $Q^\mu$,

$$
(\tilde{Q}^{\natural})^\mu = (Q^0, -Q^1, -Q^2, -Q^3),
$$

$$
(\bar{\tilde{Q}})^\mu = \bigl( (Q^0)^{*}, (Q^1)^{*}, (Q^2)^{*}, (Q^3)^{*} \bigr),
$$

$$
(\tilde{Q}^{*})^\mu = \bigl( (Q^0)^{*}, -(Q^1)^{*}, -(Q^2)^{*}, -(Q^3)^{*} \bigr), \qquad (\tilde{Q}^{\flat})^\mu = -(\tilde{Q}^{*})^\mu .
$$

**Proof.** Quaternion conjugation fixes $e_0$ and sends $e_k$ to $-e_k$, while leaving every coefficient untouched, so it acts on the coefficients by $(Q^0, Q^1, Q^2, Q^3) \mapsto (Q^0, -Q^1, -Q^2, -Q^3)$. Complex conjugation fixes every basis element $e_\mu$ and conjugates the central scalar $i$, hence conjugates each coefficient and acts componentwise by $\bar{\cdot}$. Hermitian conjugation is their composite, and $\flat$ is its negative.

**Remark.** The three involutions ${}^{\natural}$, $\bar{\cdot}$ and ${}^{*}$ commute and generate a Klein four-group with the identity; the fourth involution $\flat$ is not independent, since $\flat = -{}^{*}$ and ${}^{*}\flat = -1$ on each component. This is the coordinate form of the Klein group of conjugations of *The Group of Involutions*, and it is the reason the fixed-point subspaces below come in three pairs and not four.

**Example.** For the element

$$
\tilde{Q} = (2+i)e_0 + (1-i)e_1 + 3e_2 + ie_3, \qquad Q^\mu = (2+i, \, 1-i, \, 3, \, i),
$$

the four conjugations have four-vectors

$$
\tilde{Q}^{\natural} \leftrightarrow (2+i, \, -1+i, \, -3, \, -i), \qquad \bar{\tilde{Q}} \leftrightarrow (2-i, \, 1+i, \, 3, \, -i),
$$

$$
\tilde{Q}^{*} \leftrightarrow (2-i, \, -1-i, \, -3, \, i), \qquad \tilde{Q}^{\flat} \leftrightarrow (-2+i, \, 1+i, \, 3, \, -i),
$$

and each is an involution. The Hermitian part $\tfrac{1}{2}(\tilde{Q} + \tilde{Q}^{*})$ has four-vector $(2, \, -i, \, 0, \, i)$, a real scalar component and purely imaginary vector components, as the table of subspaces requires.

## The Six Distinguished Subspaces

Each involution cuts out a fixed subspace and an anti-fixed subspace, and the three involutions together produce six real subspaces of $\mathbb{B}$. Each of the six has its own article in the **Focus on Subspaces** group of the series, where its algebra, norm and intersections are developed; the present section records only the coordinate form, which is what the four-vector reading makes visible.

**Definition.** The six **distinguished subspaces** are

$$
\mathbb{C}_{\mathbb{B}} = \{\tilde{Q} : \tilde{Q}^{\natural} = \tilde{Q}\}, \qquad \mathrm{Vect}(\mathbb{B}) = \{\tilde{Q} : \tilde{Q}^{\natural} = -\tilde{Q}\},
$$

$$
\mathbb{H}_{\mathbb{B}} = \{\tilde{Q} : \bar{\tilde{Q}} = \tilde{Q}\}, \qquad i\mathbb{H}_{\mathbb{B}} = \{\tilde{Q} : \bar{\tilde{Q}} = -\tilde{Q}\},
$$

$$
\mathbb{M}_+ = \{\tilde{Q} : \tilde{Q}^{*} = \tilde{Q}\}, \qquad \mathbb{M}_- = \{\tilde{Q} : \tilde{Q}^{\flat} = \tilde{Q}\}.
$$

The scalar subspace $\mathbb{C}_{\mathbb{B}}$ is the centre, $\mathrm{Vect}(\mathbb{B})$ is the vector subspace, $\mathbb{H}_{\mathbb{B}}$ is the subspace of real quaternions and $i\mathbb{H}_{\mathbb{B}}$ its multiple by the scalar imaginary.

**Proposition (coordinate conditions).** In terms of the four-vector $Q^\mu$, the six subspaces are characterized as follows.

| Subspace | Coordinate condition | Name |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $Q^1 = Q^2 = Q^3 = 0$ | scalar subspace |
| $\mathrm{Vect}(\mathbb{B})$ | $Q^0 = 0$ | vector subspace |
| $\mathbb{H}_{\mathbb{B}}$ | $Q^0, Q^1, Q^2, Q^3 \in \mathbb{R}$ | quaternion subspace |
| $i\mathbb{H}_{\mathbb{B}}$ | $Q^0, Q^1, Q^2, Q^3 \in i\mathbb{R}$ | anti-quaternion subspace |
| $\mathbb{M}_+$ | $Q^0 \in \mathbb{R}$, $Q^1, Q^2, Q^3 \in i\mathbb{R}$ | Hermitian subspace |
| $\mathbb{M}_-$ | $Q^0 \in i\mathbb{R}$, $Q^1, Q^2, Q^3 \in \mathbb{R}$ | anti-Hermitian subspace |

**Proof.** The conditions are the componentwise reading of the four displayed conjugation rules of the previous section. For $\mathbb{C}_{\mathbb{B}}$ and $\mathrm{Vect}(\mathbb{B})$, quaternion conjugation fixes the scalar component and negates each vector component. For $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, complex conjugation fixes or negates each coefficient according to whether it is real or purely imaginary. For $\mathbb{M}_+$ and $\mathbb{M}_-$, Hermitian conjugation conjugates and then negates the vector components, so the fixed vectors have a real scalar component and purely imaginary vector components, and the anti-fixed vectors have a purely imaginary scalar component and real vector components.

The table shows that the three decompositions of $\mathbb{B}$ recorded in *Decompositions Along the Six Subspaces* read in coordinates as the splitting of a quadruple into its real and imaginary parts in each of three ways:

$$
\mathbb{B} = \mathbb{C}_{\mathbb{B}} \oplus \mathrm{Vect}(\mathbb{B}) = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}} = \mathbb{M}_+ \oplus \mathbb{M}_- .
$$

As real vector spaces, $\mathbb{C}_{\mathbb{B}}$ and $\mathrm{Vect}(\mathbb{B})$ have dimensions $2$ and $6$, the subspaces $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ have dimension $4$, and $\mathbb{M}_+$ and $\mathbb{M}_-$ have dimension $4$.

## The Biquaternion Norm

**Definition.** The **biquaternion norm** of a biquaternion is the central element

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q} \tilde{Q}^{\natural} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = (Q^0)^2 + (Q^1)^2 + (Q^2)^2 + (Q^3)^2 \in \mathbb{C}.
$$

In four-vector form the biquaternion norm has **all four signs positive**.

**Proposition (why all four signs are positive).** For every biquaternion $\tilde{Q}$, $\tilde{Q}\tilde{Q}^{\natural} = \sum_{\mu=0}^{3} Q_\mu^2$, a complex scalar.

**Proof.** Expand $\tilde{Q}\tilde{Q}^{\natural} = \bigl(\sum_\mu Q_\mu e_\mu\bigr)\bigl(Q_0 e_0 - \sum_k Q_k e_k\bigr)$. The cross terms between $e_0$ and $e_k$ cancel against each other in the two orders. The remaining terms are $Q_0^2 e_0$ together with $\sum_{k} Q_k^2 e_k^2 = -\sum_k Q_k^2 e_0$ and the mixed terms $-Q_j Q_k e_j e_k$ over the ordered pairs with $j \neq k$. The two ordered pairs $(j,k)$ and $(k,j)$ carry the same coefficient $Q_jQ_k$ and the two basis products are negatives of one another, so the pair contributes a multiple of $e_j e_k + e_k e_j = 0$ and cancels. Hence the only surviving terms are scalar, and collecting them gives $Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2$.

The two consequences of this computation are the ones that matter. First, the biquaternion norm is a quadratic form on the coefficient space with all four signs positive, so it is **not** an indefinite form on $\mathbb{C}^4$; it is the determinant of the matrix model of *Biquaternion 2×2 Matrix Element Representation $M_2(\mathbb{C})$*, below this article, and it is multiplicative, $\langle\tilde{P}\tilde{Q},\tilde{P}\tilde{Q}\rangle_{\natural} = \langle\tilde{P},\tilde{P}\rangle_{\natural}\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$, as proved in *Biquaternion Norm and Invertibility*. Second, the biquaternion norm can vanish on a nonzero element: the zero divisors of $\mathbb{B}$ are exactly the nonzero solutions of $Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = 0$, so $N$ is a quadratic form and not a multiplicative norm. The invertibility criterion and the group of units are the subject of *Biquaternion Norm and Invertibility*, and the classification of the zero divisors is the subject of *Biquaternion Zero Divisors*; the coordinate form of the criterion is what the four-vector realization adds.

### The Two Real Restrictions

The indefinite form is not on the coefficient space but on the two real subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$, where the four complex coordinates become eight real coordinates and the biquaternion norm becomes real-valued.

**Proposition (the real restrictions).** On the anti-Hermitian subspace $\mathbb{M}_-$, writing $Q^0 = i a^0$ and $Q^k = a^k$ with $a^0, a^1, a^2, a^3 \in \mathbb{R}$, the biquaternion norm restricts to

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = -(a^0)^2 + (a^1)^2 + (a^2)^2 + (a^3)^2,
$$

a real quadratic form of signature $(3, 1)$. On the Hermitian subspace $\mathbb{M}_+$, writing $Q^0 = a^0$ and $Q^k = i a^k$ with real $a^\mu$, it restricts to

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = (a^0)^2 - (a^1)^2 - (a^2)^2 - (a^3)^2,
$$

a real quadratic form of signature $(1, 3)$.

**Proof.** Substitute the coordinate conditions of the table above into $(Q^0)^2 + (Q^1)^2 + (Q^2)^2 + (Q^3)^2$. On $\mathbb{M}_-$ the scalar term is $(ia^0)^2 = -(a^0)^2$ and the three vector terms are $(a^k)^2$; on $\mathbb{M}_+$ the scalar term is $(a^0)^2$ and the three vector terms are $(ia^k)^2 = -(a^k)^2$.

The two forms are exchanged by multiplication by the scalar imaginary, since $\langle i\tilde{Q},i\tilde{Q}\rangle_{\natural} = \sum_\mu (iQ_\mu)^2 = -\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$ on every element, and $i\mathbb{M}_- = \mathbb{M}_+$ and $i\mathbb{M}_+ = \mathbb{M}_-$. The signature is therefore a property of the restriction to one of the real subspaces and not of the coefficient space, and the two signatures are opposite for that reason.

**Remark (the group of the form).** The $\mathbb{R}$-linear automorphisms of $\mathbb{M}_-$ preserving its quadratic form are the elements of the orthogonal group $O(3,1)$, and those of $\mathbb{M}_+$ are the elements of $O(1,3)$. These are groups of linear transformations of a real vector space preserving a quadratic form, and that is the whole of the statement made here. No indefinite form is available in the four-vector realization: the biquaternion norm has all four signs positive on $\mathbb{C}^4$, so it cannot raise or lower the index fixed in the definition of $Q^\mu$, and the index position recorded there is a convention of the corpus and not a consequence of a pairing.

### The Unit Criterion in Coordinates

The criterion of invertibility, that $\tilde{Q}$ is a unit exactly when $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} \neq 0$, is that of *Biquaternion Norm and Invertibility*; what the four-vector realization adds is the coordinate form of the inverse.

**Proposition (the inverse in coordinates).** For an invertible biquaternion $\tilde{Q}$,

$$
\tilde{Q}^{-1} = \frac{\tilde{Q}^{\natural}}{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}}, \qquad \bigl(\tilde{Q}^{-1}\bigr)^\mu = \Bigl( \frac{Q^0}{N}, \, -\frac{Q^1}{N}, \, -\frac{Q^2}{N}, \, -\frac{Q^3}{N} \Bigr), \qquad N = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}.
$$

**Proof.** With $N = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} \neq 0$, the element $\tilde{Q}^{\natural}/N$ is a two-sided inverse because $\tilde{Q}\tilde{Q}^{\natural} = \tilde{Q}^{\natural}\tilde{Q} = N$ is central, so $\tilde{Q}(\tilde{Q}^{\natural}/N) = (\tilde{Q}^{\natural}/N)\tilde{Q} = e_0$. Its coordinate form is the vector $\tilde{Q}^{\natural}$, whose components are $(Q^0, -Q^1, -Q^2, -Q^3)$, divided by the complex scalar $N$.

**Example.** For the element $\tilde{Q} = (2+i)e_0 + (1-i)e_1 + 3e_2 + ie_3$ of the preceding example, the biquaternion norm is

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = (2+i)^2 + (1-i)^2 + 3^2 + i^2 = (3+4i) + (-2i) + 9 - 1 = 11 + 2i \neq 0,
$$

so $\tilde{Q}$ is a unit, with four-vector inverse $\tfrac{1}{11+2i}(2+i, -1+i, -3, -i)$. Under conjugation the biquaternion norm becomes

$$
\langle\tilde{Q}^{\natural},\tilde{Q}^{\natural}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 11+2i, \qquad \langle\bar{\tilde{Q}},\bar{\tilde{Q}}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}^{*} = 11-2i, \qquad \langle\tilde{Q}^{*},\tilde{Q}^{*}\rangle_{\natural} = 11-2i,
$$

and multiplication by $i$ reverses its sign, $\langle i\tilde{Q},i\tilde{Q}\rangle_{\natural} = -\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = -11-2i$. The element is neither Hermitian nor anti-Hermitian, since its scalar component $2+i$ is neither real nor purely imaginary; its Hermitian part, computed above, has four-vector $(2, -i, 0, i)$ and lies in $\mathbb{M}_+$, where the restriction of the biquaternion norm is $(a^0)^2 - (a^1)^2 - (a^2)^2 - (a^3)^2$ with $(a^0, a^1, a^2, a^3) = (2, -1, 0, 1)$, that is, $4 - 1 - 0 - 1 = 2$. An element of $\mathbb{M}_-$ is written $Q^\mu = (i a^0, a^1, a^2, a^3)$ with real $a^\mu$, and on it the same restriction is the indefinite expression $- (a^0)^2 + (a^1)^2 + (a^2)^2 + (a^3)^2$ of the previous proposition.

## Summary

The four-vector realization reads a biquaternion $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ as its quadruple of complex coefficients $Q^\mu = (Q^0, Q^1, Q^2, Q^3)$, with $Q^0 = Q_0$ and $(Q^1, Q^2, Q^3) = (Q_1, Q_2, Q_3)$. It is a $\mathbb{C}$-linear isomorphism onto $\mathbb{C}^4$, and it supplies the space on which the operator of *Biquaternion 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$* acts. The column is the transcribed form of the quadruple, the row is the dual carrying the right action and is not a further representation, and the transpose that relates the two is dressed with quaternion conjugation.

The product in components has scalar part $Q^0 R^0 - \sum_k Q^k R^k$ and vector part $Q^0 R^i + R^0 Q^i + \sum_{j,k} \epsilon^{ijk} Q^j R^k$; the Levi-Civita term is the only trace of non-commutativity. The three conjugations act by negating the vector components, conjugating every component, and doing both; the six distinguished subspaces are the resulting coordinate conditions, three fixed spaces and three anti-fixed spaces. The biquaternion norm is $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = (Q^0)^2 + (Q^1)^2 + (Q^2)^2 + (Q^3)^2$, with all four signs positive because each quaternion unit squares to $-e_0$ and the cross terms cancel; it is a complex quadratic form in general, and it becomes a real indefinite form of signature $(3,1)$ on $\mathbb{M}_-$ and $(1,3)$ on $\mathbb{M}_+$, the two exchanged by $\langle i\tilde{Q},i\tilde{Q}\rangle_{\natural} = -\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | Biquaternion algebra |
| $e_0, e_1, e_2, e_3$ | Algebra basis, $e_0 = 1$, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ | Developed form, $Q_\mu \in \mathbb{C}$ |
| $Q^\mu = (Q^0, Q^1, Q^2, Q^3)$ | Four-vector; $Q^0 = Q_0$, $(Q^1, Q^2, Q^3) = (Q_1, Q_2, Q_3)$ |
| $Q$, $Q^{\mathsf{T}}$ | Column and row of the four-vector |
| $a^\mu, b^\mu$ | Real and imaginary parts of the components, $Q^\mu = a^\mu + i b^\mu$ |
| $\operatorname{mat}_4(\tilde{Q})$ | Matrix of left multiplication on the coefficient space, constructed in *Biquaternion 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$* |
| $\epsilon^{ijk}$ | Levi-Civita symbol on the indices $1, 2, 3$ |
| ${}^{\natural}$ | Quaternion conjugation, negates the vector components |
| $\bar{\cdot}$ | Complex conjugation, conjugates every component |
| ${}^{*} = {}^{\natural} \circ \bar{\cdot}$ | Hermitian conjugation |
| ${}^{\flat} = -{}^{*}$ | Anti-Hermitian conjugation |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B}), \mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}, \mathbb{M}_+, \mathbb{M}_-$ | The six distinguished subspaces |
| $\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ | Biquaternion norm, multiplicative |
| $O(1,3)$, $O(3,1)$ | Orthogonal groups of the restrictions to $\mathbb{M}_+$, $\mathbb{M}_-$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Dublin, 1853), for the origin of the quaternion coordinates and the scalar and vector parts.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions", *Proceedings of the London Mathematical Society* **4** (1873) 381–395, for the first systematic treatment of the complexified quaternions.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), Chapter 3, for the coordinate form of the biquaternion product and its conjugations.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the four-vector realization in applied form.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition (Cambridge University Press, 2001), for the quadratic forms and signatures attached to the biquaternion algebra.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the computation with quaternion and biquaternion coordinates.
