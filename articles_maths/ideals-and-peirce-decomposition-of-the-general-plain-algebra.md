# __Ideals and Peirce Decomposition of the General Plain Algebra__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is four-dimensional over $\mathbb{C}$ and eight-dimensional over $\mathbb{R}$, as established in the article on biquaternion algebra. This article studies the ideal structure of $\mathbb{B}$ and the decomposition of $\mathbb{B}$ relative to a family of idempotents.

Two facts organize the discussion. The algebra $\mathbb{B}$ is **simple**: its only two-sided ideals are $0$ and $\mathbb{B}$. Its ideal theory is therefore a theory of one-sided ideals: the main results are the classification of the left ideals — $0$, the minimal ones, and $\mathbb{B}$ — and the Peirce decomposition into four one-dimensional corners relative to a pair of orthogonal idempotents. The Peirce decomposition is developed in detail below: it is read in coordinates, and the coordinates turn out to be the four entries of the matrix element representation of the algebra; it is a grading by the parity of the corners; the three conjugations of the algebra act on it; and it is rigid, in the sense that all systems of matrix units that realise it are conjugate.

Because the biquaternions carry both a complex and a real structure, every statement is tagged with the field over which it is made. The sections before the last work over $\mathbb{C}$; §*The Real Structure* discusses the $\mathbb{R}$-view, where the ideal lattice itself is unchanged but the real structure leaves further traces. The notation follows the article on biquaternion algebra: $e_0$ is the unit, $e_1, e_2, e_3$ are the quaternion units with $e_1 e_2 = e_3$, $i$ is the central scalar imaginary, and a general element is $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$. The definitions of the article on rings apply to the noncommutative algebra $\mathbb{B}$, where "left" and "right" must be distinguished.

## Ideals in an Algebra

Let $A$ be an associative unital algebra over a field $k$. An additive subgroup $I \subseteq A$ is a **left ideal** if $A I \subseteq I$, a **right ideal** if $I A \subseteq I$, and a **two-sided ideal** if it is both. The distinction matters only when $A$ is noncommutative; for $\mathbb{B}$ the three notions genuinely differ. The ideals $0$ and $A$ are called trivial.

A base-field remark will be used repeatedly. If $A I \subseteq I$, then $I$ is automatically a $k$-subspace, since $\lambda \tilde Q = (\lambda 1) \tilde Q \in I$ for $\lambda \in k$, $\tilde Q \in I$, as $\lambda 1 \in A$. So the left ideals of a unital algebra do not depend on which field of scalars inside the centre is used to view it; in particular the ideal lattice of $\mathbb{B}$ is the same in the $\mathbb{C}$-view and the $\mathbb{R}$-view (§*The Real Structure*).

For a two-sided ideal $I$, the **quotient algebra** $A/I$ is the set of cosets with the induced operations, well defined precisely because $I$ absorbs multiplication on both sides. Kernels of algebra homomorphisms are two-sided ideals, and the first isomorphism theorem gives $A/\ker\varphi \cong \operatorname{im}\varphi$. For a left ideal only, $A/I$ is still a left $A$-module but not in general an algebra. Thus the left ideals govern module theory and the two-sided ideals govern quotient algebras.

## The Two-Sided Ideals: Simplicity of $\mathbb{B}$

**Theorem.** Over $\mathbb{C}$, the only two-sided ideals of $\mathbb{B}$ are $0$ and $\mathbb{B}$. Equivalently, $\mathbb{B}$ is a **simple** $\mathbb{C}$-algebra.

**Proof.** Let $I \neq 0$ be a two-sided ideal. It is a $\mathbb{C}$-subspace, because multiplication by the central element $i$ is left multiplication by an element of $\mathbb{B}$. Fix $0 \neq \tilde{Q} = \sum_\mu Q_\mu e_\mu \in I$. For every unit $\tilde B \in \mathbb{B}$ the conjugate $\tilde B\tilde{Q}\tilde B^{-1}$ lies in $I$, since $I$ is two-sided.

Average the conjugates over the finite group $\{\pm e_0, \pm e_1, \pm e_2, \pm e_3\}$. Conjugation by $e_\mu$ fixes $e_0$ and $e_\mu$ and reverses $e_\nu$ for $\nu \neq \mu$, so the elements $e_\mu$ and $-e_\mu$ give the same conjugate, and the sum over the four representatives $e_0, e_1, e_2, e_3$ is

$$
\tilde Q + \big(Q_0 e_0 + Q_1 e_1 - Q_2 e_2 - Q_3 e_3\big) + \big(Q_0 e_0 - Q_1 e_1 + Q_2 e_2 - Q_3 e_3\big) + \big(Q_0 e_0 - Q_1 e_1 - Q_2 e_2 + Q_3 e_3\big) = 4 Q_0 e_0,
$$

the sum over all eight is twice this, and the average is that sum divided by $8$, giving $Q_0 e_0 \in I$. If $Q_0 \neq 0$ then $e_0 = Q_0^{-1}(Q_0 e_0) \in I$ and $I = \mathbb{B}$. If $Q_0 = 0$ then $\tilde{Q}$ is a nonzero element of the vector subspace, and conjugating it by the real unit quaternions rotates it: the conjugates run over the real unit vectors in $\mathrm{Vect}(\mathbb{B})$, whose real span is all of $\mathrm{Vect}(\mathbb{B})$, so $\mathrm{Vect}(\mathbb{B}) \subseteq I$. In particular $e_1 \in I$, hence $e_1^2 = -e_0 \in I$ and again $I = \mathbb{B}$.

Consequences over $\mathbb{C}$:

- The only quotient algebras of $\mathbb{B}$ are $\mathbb{B}$ and $0$.
- Every nonzero element generates $\mathbb{B}$ as a two-sided ideal.
- The centre of $\mathbb{B}$ is the scalar copy of $\mathbb{C}$, so $\mathbb{B}$ is a **central simple** $\mathbb{C}$-algebra; in particular it is not a product $A_1 \times A_2$ of nonzero algebras, since each factor would give a nontrivial two-sided ideal.
- The many one-sided ideals of §*Minimal Left and Right Ideals* and §*The Lattice of Left Ideals* are all non-two-sided, so they do not contradict simplicity.

## Artinian, Semisimple, and Length Two

A nonzero module is **simple** if it has no submodules other than $0$ and itself. A **composition series** is a finite strictly increasing chain $0 = M_0 \subset M_1 \subset \cdots \subset M_r = M$ with simple successive quotients $M_i/M_{i-1}$; the number $r$ is the **length** of $M$. A ring is **left artinian** if every descending chain of left ideals stabilizes, and **semisimple** if its left regular module is a direct sum of simple modules.

Over $\mathbb{C}$, every descending chain of left ideals of $\mathbb{B}$ is a descending chain of $\mathbb{C}$-subspaces, so it stabilizes; thus $\mathbb{B}$ is artinian. By Wedderburn–Artin, a unital ring is semisimple if and only if it is artinian with zero Jacobson radical, and every simple artinian ring is semisimple. Hence $\mathbb{B}$ is **semisimple**, and every left ideal is a direct sum of minimal left ideals.

All simple left $\mathbb{B}$-modules are isomorphic, since a simple artinian ring has a unique simple module up to isomorphism. With the idempotents $\tilde\Pi_1, \tilde\Pi_2$ of §*Idempotents and Orthogonal Idempotents*, the algebra as a left module over itself reads $\mathbb{B} = \mathbb{B}\tilde\Pi_1 \oplus \mathbb{B}\tilde\Pi_2$, with $\mathbb{B}\tilde\Pi_1$ and $\mathbb{B}\tilde\Pi_2$ both minimal left ideals. Hence $0 \subset \mathbb{B}\tilde\Pi_1 \subset \mathbb{B}$ is a composition series, and the **length of $\mathbb{B}$ as a left module over itself is $2$**, with both factors isomorphic. The right regular module has length $2$ as well. All of this is over $\mathbb{C}$.

## Idempotents and Orthogonal Idempotents

Let $A$ be an associative unital algebra. An element $e \in A$ is an **idempotent** if $e^2 = e$, and two idempotents $e, f$ are **orthogonal** if $ef = fe = 0$. A nonzero idempotent $e$ is **primitive** if it is not a sum of two nonzero orthogonal idempotents, and for a semisimple algebra

$$
e \text{ primitive} \iff Ae \text{ is a minimal left ideal} \iff eAe \text{ is a division ring}.
$$

Over $\mathbb{C}$, the idempotents

$$
\tilde\Pi_1 = \frac{e_0 + i e_3}{2}, \qquad \tilde\Pi_2 = \frac{e_0 - i e_3}{2}
$$

satisfy $\tilde\Pi_1^2 = \tilde\Pi_1$, $\tilde\Pi_2^2 = \tilde\Pi_2$, $\tilde\Pi_1\tilde\Pi_2 = \tilde\Pi_2\tilde\Pi_1 = 0$ and $\tilde\Pi_1 + \tilde\Pi_2 = e_0$. They are primitive, and they generate the off-diagonal elements of the next section.

The classification of the idempotents of $\mathbb{B}$ — the trivial idempotents, the bijection with the roots of $-1$, the Hermitian projections and the dimension of the idempotent set — is the subject of *Idempotents of the General Plain Algebra*.

## The Off-Diagonal Elements

The two off-diagonal corners are spanned by the elements

$$
\tilde\Upsilon_1 = \frac{i e_1 - e_2}{2}, \qquad \tilde\Upsilon_2 = \frac{i e_1 + e_2}{2}.
$$

Then $\{\tilde\Pi_1, \tilde\Upsilon_1, \tilde\Upsilon_2, \tilde\Pi_2\}$ is a $\mathbb{C}$-basis of $\mathbb{B}$, and the multiplication is

$$
\tilde\Pi_1\tilde\Upsilon_1 = \tilde\Upsilon_1 = \tilde\Upsilon_1\tilde\Pi_2, \qquad \tilde\Pi_2\tilde\Upsilon_2 = \tilde\Upsilon_2 = \tilde\Upsilon_2\tilde\Pi_1, \qquad \tilde\Upsilon_1\tilde\Upsilon_2 = \tilde\Pi_1, \qquad \tilde\Upsilon_2\tilde\Upsilon_1 = \tilde\Pi_2,
$$

together with $\tilde\Upsilon_1\tilde\Pi_1 = \tilde\Pi_2\tilde\Upsilon_1 = \tilde\Pi_1\tilde\Upsilon_2 = 0$, $\tilde\Upsilon_2\tilde\Pi_2 = 0$, and $\tilde\Upsilon_1^2 = \tilde\Upsilon_2^2 = 0$.

## The Peirce Decomposition

The **Peirce decomposition** is the decomposition of an algebra relative to a family of orthogonal idempotents; it is the algebraic form of a block decomposition of a matrix.

### One Idempotent

Let $e \in A$ be idempotent and $f = 1-e$. Every $a \in A$ expands as $a = eae + eaf + fae + faf$, giving the direct sum

$$
A = eAe \oplus eAf \oplus fAe \oplus fAf,
$$

whose summands are the **Peirce spaces**. The corner $eAe$ is a subalgebra with identity $e$; the other corners are only one-sided pieces. The expansion, the directness of the four terms and the product rule below are proved in *Unital Algebras*, §*Idempotents and the Peirce Decomposition*, where the case of a **central** idempotent is also separated: for a central $e$ the off-diagonal corners vanish and the sum is a product of algebras. That special case does not arise here, since the idempotents of this article lie in a simple algebra and no nontrivial idempotent of $\mathbb{B}$ is central.

### A Complete Orthogonal Family

If $\{e_1, \dots, e_n\}$ is complete and pairwise orthogonal, the same expansion gives

$$
A = \bigoplus_{i,j=1}^{n} e_i A e_j, \qquad (e_i A e_j)(e_k A e_l) \subseteq \delta_{jk}\, e_i A e_l.
$$

Each diagonal corner $e_i A e_i$ is an algebra with identity $e_i$, and each off-diagonal piece is a bimodule over the corresponding corners.

**The mixed spaces are square-zero subalgebras.** For the mixed space $eAf$ and $a, a' \in A$ one has $(eaf)(ea'f) = e\,af e\,a'f = 0$, since $fe = 0$; so $eAf \cdot eAf = 0$, and likewise $fAe \cdot fAe = 0$. A mixed Peirce space is therefore closed under the product, but with the identically zero product: it is a subalgebra without a unit, and it carries no algebra structure that could enter a decomposition of $A$ as a product. In the biquaternion case this is the nilpotence of the two mixed basis elements, $\tilde\Upsilon_1^2 = \tilde\Upsilon_2^2 = 0$ (§*The Off-Diagonal Elements*).

**Rows and columns.** The sums of a row and of a column of the table are the one-sided ideals generated by the idempotents,

$$
\bigoplus_{j=1}^n e_i A e_j = e_i A, \qquad \bigoplus_{i=1}^n e_i A e_j = A e_j ,
$$

the first being the right ideal generated by $e_i$ and the second the left ideal generated by $e_j$. The Peirce decomposition therefore contains the right-ideal decomposition as its rows and the left-ideal decomposition as its columns, and the two groupings of the same spaces differ exactly as the two groupings of §*The Decomposition into Minimal Left and Right Ideals* differ.

### The Biquaternion Case

Take $e_1 = \tilde\Pi_1$, $e_2 = \tilde\Pi_2$ from §*Idempotents and Orthogonal Idempotents*. The Peirce decomposition of $\mathbb{B}$ is

$$
\mathbb{B} = \tilde\Pi_1\mathbb{B}\tilde\Pi_1 \oplus \tilde\Pi_1\mathbb{B}\tilde\Pi_2 \oplus \tilde\Pi_2\mathbb{B}\tilde\Pi_1 \oplus \tilde\Pi_2\mathbb{B}\tilde\Pi_2,
$$

and by the multiplication table of §*The Off-Diagonal Elements* each summand is one-dimensional over $\mathbb{C}$:

$$
\tilde\Pi_1\mathbb{B}\tilde\Pi_1 = \mathbb{C}\tilde\Pi_1, \qquad \tilde\Pi_1\mathbb{B}\tilde\Pi_2 = \mathbb{C}\tilde\Upsilon_1, \qquad \tilde\Pi_2\mathbb{B}\tilde\Pi_1 = \mathbb{C}\tilde\Upsilon_2, \qquad \tilde\Pi_2\mathbb{B}\tilde\Pi_2 = \mathbb{C}\tilde\Pi_2.
$$

So the Peirce decomposition of $\mathbb{B}$ is

$$
\mathbb{B} = \mathbb{C}\tilde\Pi_1 \oplus \mathbb{C}\tilde\Upsilon_1 \oplus \mathbb{C}\tilde\Upsilon_2 \oplus \mathbb{C}\tilde\Pi_2.
$$

### The Peirce Table

The four products of the basis elements are collected in the table whose entry in row $S$ and column $T$ is the space containing the products of an element of $S$ with an element of $T$:

| $\cdot$ | $\mathbb{C}\tilde\Pi_1$ | $\mathbb{C}\tilde\Upsilon_1$ | $\mathbb{C}\tilde\Upsilon_2$ | $\mathbb{C}\tilde\Pi_2$ |
|---|---|---|---|---|
| $\mathbb{C}\tilde\Pi_1$ | $\mathbb{C}\tilde\Pi_1$ | $\mathbb{C}\tilde\Upsilon_1$ | $0$ | $0$ |
| $\mathbb{C}\tilde\Upsilon_1$ | $0$ | $0$ | $\mathbb{C}\tilde\Pi_1$ | $\mathbb{C}\tilde\Upsilon_1$ |
| $\mathbb{C}\tilde\Upsilon_2$ | $\mathbb{C}\tilde\Upsilon_2$ | $\mathbb{C}\tilde\Pi_2$ | $0$ | $0$ |
| $\mathbb{C}\tilde\Pi_2$ | $0$ | $0$ | $\mathbb{C}\tilde\Upsilon_2$ | $\mathbb{C}\tilde\Pi_2$ |

The table is the rule $\delta_{jk}$ of §*A Complete Orthogonal Family* read on the basis, and it is sparser than the rule suggests: the products $\tilde\Upsilon_1^2$ and $\tilde\Upsilon_2^2$ vanish, so the diagonal entries of the two mixed rows and columns are zero, and the surviving entries are the four basis elements themselves. Reading the table by rows gives the two right ideals and by columns the two left ideals, as in §*A Complete Orthogonal Family*.

### The Peirce Coordinates

The decomposition is read in coordinates. Write $\tilde Q = \sum_{\mu=0}^{3}Q_\mu e_\mu$, and let $a_{ij}$ be the coefficient of the one-dimensional corner $\tilde\Pi_i\mathbb{B}\tilde\Pi_j$ in the expansion of $\tilde Q$; then

$$
a_{11} = Q_0 - iQ_3, \qquad a_{12} = -iQ_1 - Q_2, \qquad a_{21} = -iQ_1 + Q_2, \qquad a_{22} = Q_0 + iQ_3,
$$

so that

$$
\tilde Q = a_{11}\tilde\Pi_1 + a_{12}\tilde\Upsilon_1 + a_{21}\tilde\Upsilon_2 + a_{22}\tilde\Pi_2 ,
$$

and conversely

$$
Q_0 = \tfrac12(a_{11}+a_{22}), \qquad Q_1 = \tfrac{i}{2}(a_{12}+a_{21}), \qquad Q_2 = \tfrac12(a_{21}-a_{12}), \qquad Q_3 = \tfrac{i}{2}(a_{11}-a_{22}).
$$

The four numbers $a_{ij}$ are the **Peirce coordinates** of $\tilde Q$. They are linear functions of $\tilde Q$; the scalar part is their mean, and their determinant is the biquaternion norm,

$$
a_{11}a_{22} - a_{12}a_{21} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = N(\tilde Q)
$$

(*Norm and Invertibility in the General Plain Algebra*). The coordinates are nothing but the four entries of the corpus's fixed matrix element representation: the isomorphism $\mathsf{M}_2 : \mathbb{B}\to M_2(\mathbb{C})$ of *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, §*The Representation*, is

$$
\mathsf{M}_2(\tilde Q) = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} = \begin{pmatrix} Q_0 - iQ_3 & -iQ_1 - Q_2 \\ -iQ_1 + Q_2 & Q_0 + iQ_3 \end{pmatrix}.
$$

The Peirce decomposition therefore supplies the matrix element representation directly: the four spaces are the four matrix units, and the coordinate functions are the entries. §*The Peirce Coordinates and the Matrix Model* below develops that reading.

### The Decomposition as a Grading

The Peirce decomposition of a complete orthogonal family carries a second structure, the parity of the indices. Let $A_0$ be the sum of the diagonal corners and $A_1$ the sum of the mixed ones; the rule $(e_iAe_j)(e_kAe_l)\subseteq\delta_{jk}e_iAe_l$ says that a product of two Peirce spaces vanishes unless the two inner indices agree, and that when they agree the outer indices combine. Reading the label $i+j$ modulo two, so that $A_0$ carries the even class and $A_1$ the odd one, the rule becomes

$$
A_0A_0 \subseteq A_0, \qquad A_0A_1 \subseteq A_1, \qquad A_1A_0 \subseteq A_1, \qquad A_1A_1 \subseteq A_0 ,
$$

which is the multiplication law of the group $\mathbb{Z}/2$: the decomposition $A = A_0\oplus A_1$ is a **grading** of the algebra, $A_0$ is a subalgebra and $A_1$ is a module over it. In the biquaternion case $A_0$ is the diagonal part of the paragraph below and $A_1 = \mathbb{C}\tilde\Upsilon_1 \oplus \mathbb{C}\tilde\Upsilon_2$, and the four inclusions are the laws $\tilde\Upsilon_1\tilde\Upsilon_2 = \tilde\Pi_1$ and $\tilde\Upsilon_2\tilde\Upsilon_1 = \tilde\Pi_2$ together with $\tilde\Upsilon_1^2 = \tilde\Upsilon_2^2 = 0$. The grading is the checkerboard of a $2\times2$ matrix: two cells of like colour multiply into the diagonal part and two of unlike colour into the mixed part.

### The Involutions on the Peirce Spaces

Each of the three conjugations permutes the four spaces, with a sign on the two mixed elements:

| | $\tilde\Pi_1$ | $\tilde\Upsilon_1$ | $\tilde\Upsilon_2$ | $\tilde\Pi_2$ |
|---|---|---|---|---|
| natural ${}^{\natural}$ | $\tilde\Pi_2$ | $-\tilde\Upsilon_1$ | $-\tilde\Upsilon_2$ | $\tilde\Pi_1$ |
| bar $\bar{\cdot}$ | $\tilde\Pi_2$ | $-\tilde\Upsilon_2$ | $-\tilde\Upsilon_1$ | $\tilde\Pi_1$ |
| Hermitian ${}^{*}$ | $\tilde\Pi_1$ | $\tilde\Upsilon_2$ | $\tilde\Upsilon_1$ | $\tilde\Pi_2$ |

the bar being the coefficient conjugation, which is the map $\sigma$ of §*The Real Structure*, and the Hermitian conjugation the composite ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ (*Conventions in Mathematics*). All three preserve the set of the four Peirce spaces, and they act on it differently. The natural sign exchanges the two diagonal corners and preserves each mixed space, on which it acts as $-\mathrm{id}$. The bar exchanges the two diagonal corners and also exchanges the two mixed spaces. The Hermitian conjugation fixes each of the two diagonal corners and exchanges the two mixed spaces. The last statement is the general exchange theorem of *Hermitian Idempotents and the Peirce Decomposition*, §*The Involution on the Peirce Spaces*, read on $\mathbb{B}$: the standard idempotents are Hermitian, $\tilde\Pi_1^{*} = \tilde\Pi_1$ and $\tilde\Pi_2^{*} = \tilde\Pi_2$, so the involution carries each corner to itself and the mixed space $\tilde\Pi_1\mathbb{B}\tilde\Pi_2$ onto $\tilde\Pi_2\mathbb{B}\tilde\Pi_1$, exchanging $\tilde\Upsilon_1$ and $\tilde\Upsilon_2$ and giving the pairing of the two nilpotents recorded in *Conventions in Mathematics*, §*The nilpotent convention*. The bar and the natural sign are the two factors of the composite, and each of them fails to fix the standard idempotents; the Hermitian conjugation is the one that respects them.

The diagonal part $\tilde\Pi_1\mathbb{B}\tilde\Pi_1 \oplus \tilde\Pi_2\mathbb{B}\tilde\Pi_2 = \mathbb{C}\tilde\Pi_1 \oplus \mathbb{C}\tilde\Pi_2$ is a two-dimensional commutative subalgebra isomorphic to $\mathbb{C} \times \mathbb{C}$. Each diagonal corner is a division ring, namely $\mathbb{C}$, which is the primitivity criterion of §*Idempotents and Orthogonal Idempotents*.

A **null (light-cone) variant** of the same split is used in *The Chiral Algebra of Biquaternions and the Cyclic Representation of the Dirac Equation*. The idempotents there are the uniform nullquaternions $N = \tfrac12(1, \mathbf n)$ and $\bar N = \tfrac12(1, -\mathbf n)$, and the two Peirce components of a biquaternion are its **signed parts**, whose sign the source reads as the chirality of the Weyl spinor. The pair is orthogonal and complete in the article's own product — the **outer** product, for which $N \odot N = N$, $\bar N \odot \bar N = \bar N$, $N \odot \bar N = 0$ and $N + \bar N = e_0$ — and the article's matrix isomorphism carries the outer product to the ordinary matrix product and $N, \bar N$ to the two standard diagonal idempotents. It is the same orthogonal pair as above, transported to the light-cone coordinates with the product changed; these same elements are **not** idempotent under the Hamilton product of this article, so the chiral split is naturally stated in that paper's algebra rather than in this one.

## The Peirce Coordinates and the Matrix Model

### The Matrix Model

The Peirce coordinates of §*The Peirce Coordinates* do more than parametrise the elements: read as a matrix, they carry the whole multiplication.

**Proposition.** The map that sends $\tilde Q$ to the matrix $\begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22}\end{pmatrix}$ of its Peirce coordinates is an isomorphism of $\mathbb{C}$-algebras $\mathbb{B}\to M_2(\mathbb{C})$, and it carries the four Peirce spaces onto the four matrix units,

$$
\tilde\Pi_1 \mapsto E_{11}, \qquad \tilde\Upsilon_1 \mapsto E_{12}, \qquad \tilde\Upsilon_2 \mapsto E_{21}, \qquad \tilde\Pi_2 \mapsto E_{22}.
$$

*Proof.* The map is $\mathbb{C}$-linear and bijective, since the four basis elements of $\mathbb{B}$ go to the four basis matrices of $M_2(\mathbb{C})$; it is multiplicative because the four Peirce basis elements multiply as the four matrix units do — the Peirce table of §*The Peirce Table* is the table $E_{ij}E_{kl} = \delta_{jk}E_{il}$ of *Matrix Algebras*, §*Matrix Units* — and both multiplications are bilinear.

The isomorphism is the corpus's $\mathsf{M}_2$ of *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, written there as an assignment on the basis; what the Peirce decomposition adds is the reading of its four entries as the coordinates of the four corners. Its trace and its determinant are the two invariants of the Peirce decomposition, $\operatorname{tr} = a_{11}+a_{22} = 2Q_0$ and $\det = a_{11}a_{22}-a_{12}a_{21} = N(\tilde Q)$, so that the scalar part and the norm of the algebra are the two symmetric functions of the corner coordinates (§*The Peirce Coordinates*). In this model the left ideals are the columns and the right ideals the rows, which is the content of §*The Decomposition into Minimal Left and Right Ideals* read on the matrix side: $\mathbb{B}\tilde\Pi_1$ is the first column $\mathbb{C}E_{11}\oplus\mathbb{C}E_{21}$ and $\tilde\Pi_1\mathbb{B}$ is the first row $\mathbb{C}E_{11}\oplus\mathbb{C}E_{12}$, the two groupings of the four matrix units that *Matrix Algebras*, §*The Case $n = 2$* distinguishes.

### Systems of Matrix Units

**Definition.** A **system of $2\times2$ matrix units** in $\mathbb{B}$ is a family $\{E_{11}, E_{12}, E_{21}, E_{22}\}$ of elements of $\mathbb{B}$ with

$$
E_{ij}E_{kl} = \delta_{jk}E_{il}, \qquad E_{11} + E_{22} = e_0, \qquad E_{11} \neq 0 .
$$

The definition is the abstract form of the multiplication of the coordinate matrices, and it is redundant on purpose: the relations already give $E_{11}^2 = E_{11}$, $E_{22}^2 = E_{22}$ and $E_{11}E_{22} = E_{22}E_{11} = 0$, so that $E_{11}$ and $E_{22}$ are orthogonal idempotents summing to the unit, and the two off-diagonal elements are nilpotent, $E_{12}^2 = E_{21}^2 = 0$.

**Proposition.** A system of matrix units is the same data as a Peirce decomposition with two primitive idempotents, together with a basis of each of the two mixed spaces normalised by $E_{12}E_{21} = E_{11}$. The standard system is the one of §*The Off-Diagonal Elements*,

$$
E_{11} = \tilde\Pi_1, \qquad E_{12} = \tilde\Upsilon_1, \qquad E_{21} = \tilde\Upsilon_2, \qquad E_{22} = \tilde\Pi_2 .
$$

**Theorem (the Peirce decomposition is unique up to conjugation).** Every system of $2\times2$ matrix units of $\mathbb{B}$ is the image of the standard system under an inner automorphism: there is a unit $\tilde G \in \mathbb{B}$ with $E_{ij} = \tilde G\,\tilde E_{ij}\,\tilde G^{-1}$ for the standard system $\{\tilde E_{ij}\}$. Consequently all Peirce decompositions of $\mathbb{B}$ with two primitive idempotents are conjugate, and a statement about one of them is a statement about all.

*Proof.* By the matrix model of §*The Matrix Model* the question is the corresponding statement for $M_2(\mathbb{C})$, and there it is proved by change of basis. A primitive idempotent $P$ of $M_2(\mathbb{C})$ is the projector onto a line $\ell$ along another line $m$, $\ell$ being its image and $m$ its kernel; choosing a basis with first vector in $\ell$ and second in $m$, and letting $G$ be the matrix of that basis, gives $GPG^{-1} = E_{11}$. The stabiliser of $E_{11}$ is the diagonal torus, since a conjugation that fixes $E_{11}$ must preserve its image and its kernel; conjugating by the diagonal matrix $\operatorname{diag}(a,d)$ fixes $E_{11}$ and $E_{22}$ and multiplies $E_{12}$ by $a/d$ and $E_{21}$ by $d/a$. In a system of matrix units with $E_{11}$ and $E_{22}$ fixed, the two off-diagonal elements are determined by a single scalar, because they lie in the one-dimensional mixed spaces and satisfy $E_{12}E_{21} = E_{11}$; the diagonal conjugation is transitive on that scalar, so the system is carried to the standard one. The unit group of $\mathbb{B}$ acts by algebra automorphisms, since every automorphism of $\mathbb{B}$ is inner (*Biquaternion Automorphisms and Derivations*, §*Automorphisms over $\mathbb{C}$*), and an automorphism carries a system of matrix units to a system of matrix units.

The theorem is the rigidity of the Peirce decomposition, and it should be read with two counts that it does not contradict. The **idempotents** that occur are not unique: every primitive idempotent of $\mathbb{B}$ appears, and these form the real four-dimensional idempotent manifold of *Idempotents of the General Plain Algebra*, §*The Bijection With the Roots of Minus One*, not the two points $\tilde\Pi_1, \tilde\Pi_2$. The **left ideals** that occur are not unique either: they form the projective line $\mathbb{P}^1(\mathbb{C})$ of §*The Lattice of Left Ideals*. What is unique is the decomposition up to conjugation: the idempotent may be carried anywhere by a unit, and the unit conjugation carries the decomposition with it. Equivalently, $\mathbb{B}$ has one Peirce decomposition of this shape modulo the inner automorphisms — the statement that the algebra has a single block structure, namely the $2\times2$ block structure of a matrix algebra, and that all the decompositions of §*The Peirce Decomposition* are that structure seen in different bases.

## The Decomposition into Minimal Left and Right Ideals

The two idempotents group the basis into one-sided ideals in a second way. The two **left ideals** $\mathbb{B}\tilde\Pi_1, \mathbb{B}\tilde\Pi_2$ and the two **right ideals** $\tilde\Pi_1\mathbb{B}, \tilde\Pi_2\mathbb{B}$ are one-sided, and

$$
\mathbb{B} = \mathbb{B}\tilde\Pi_1 \oplus \mathbb{B}\tilde\Pi_2 = (\mathbb{C}\tilde\Pi_1 \oplus \mathbb{C}\tilde\Upsilon_2) \oplus (\mathbb{C}\tilde\Upsilon_1 \oplus \mathbb{C}\tilde\Pi_2),
$$

$$
\mathbb{B} = \tilde\Pi_1\mathbb{B} \oplus \tilde\Pi_2\mathbb{B} = (\mathbb{C}\tilde\Pi_1 \oplus \mathbb{C}\tilde\Upsilon_1) \oplus (\mathbb{C}\tilde\Upsilon_2 \oplus \mathbb{C}\tilde\Pi_2).
$$

The first exhibits $\mathbb{B}$ as a direct sum of the two minimal left ideals; the second exhibits it as a direct sum of the two minimal right ideals. The two groupings of the same four basis elements differ: the Peirce decomposition groups $\tilde\Pi_1$ with $\tilde\Upsilon_1$ and $\tilde\Pi_2$ with $\tilde\Upsilon_2$, whereas the left-ideal decomposition groups $\tilde\Pi_1$ with $\tilde\Upsilon_2$ and $\tilde\Pi_2$ with $\tilde\Upsilon_1$. Each left ideal is two-dimensional over $\mathbb{C}$; each right ideal is its dual. Since $\mathbb{B}$ is simple, a one-sided ideal is never two-sided; for instance $\mathbb{B}\tilde\Pi_1$ is not stable under right multiplication by $\tilde\Upsilon_1$.

**Why the sum is direct, and the dimensions.** Every $\tilde{Q} \in \mathbb{B}$ satisfies $\tilde{Q} = \tilde{Q}(\tilde\Pi_1 + \tilde\Pi_2) = \tilde{Q}\tilde\Pi_1 + \tilde{Q}\tilde\Pi_2$, so the two left ideals span. Their intersection is zero: if $\tilde{Q}\tilde\Pi_1 = \tilde{P}\tilde\Pi_2$, then multiplying on the right by $\tilde\Pi_1$ and using $\tilde\Pi_1^2 = \tilde\Pi_1$ and $\tilde\Pi_2\tilde\Pi_1 = 0$ gives $\tilde{Q}\tilde\Pi_1 = 0$. The basis above reads $\mathbb{B}\tilde\Pi_1 = \mathbb{C}\tilde\Pi_1 \oplus \mathbb{C}\tilde\Upsilon_2$, of dimension $2$ over $\mathbb{C}$ and $4$ over $\mathbb{R}$, with $\mathbb{B}\tilde\Pi_2 = \mathbb{C}\tilde\Upsilon_1 \oplus \mathbb{C}\tilde\Pi_2$ for the second; together they account for $4 + 4 = 8 = \dim_{\mathbb{R}} \mathbb{B}$. Each is a minimal left ideal, by the primitivity of $\tilde\Pi_1$ and $\tilde\Pi_2$ (§*Idempotents and Orthogonal Idempotents*, §*Minimal Left and Right Ideals*).

**The module structure.** With the basis $\{\tilde\Pi_1, \tilde\Upsilon_2\}$ the left $\mathbb{B}$-module $\mathbb{B}\tilde\Pi_1$ is $\mathbb{C}^2$, and the central element $i$ acts on it as the scalar $i$:
$$
i\,(\alpha \tilde\Pi_1 + \beta \tilde\Upsilon_2) = (i\alpha)\tilde\Pi_1 + (i\beta)\tilde\Upsilon_2 .
$$
So the simple module underlying each minimal left ideal is the standard two-dimensional one, with $i$ acting by the identity matrix.

## Minimal Left and Right Ideals

A **minimal left ideal** is a nonzero left ideal containing no nonzero proper left ideal; equivalently, a simple submodule of the left regular module. A **minimal right ideal** is defined the same way on the right.

Over $\mathbb{C}$, since $\mathbb{B}$ is semisimple, every left ideal of $\mathbb{B}$ is a direct sum of minimal left ideals, and every minimal left ideal is of the form $\mathbb{B}e$ for a primitive idempotent $e$. The examples are the left ideals $\mathbb{B}\tilde\Pi_1$ and $\mathbb{B}\tilde\Pi_2$ of §*The Decomposition into Minimal Left and Right Ideals*, and all minimal left ideals are isomorphic as left $\mathbb{B}$-modules: a general one is obtained from $\mathbb{B}\tilde\Pi_1$ by an algebra automorphism, so it has the same shape in a suitable basis. Dually, every minimal right ideal is isomorphic to $\tilde\Pi_1\mathbb{B}$. Thus there is one isomorphism class of simple left modules and one of simple right modules. Being nonzero proper one-sided ideals, none of them is two-sided — which is exactly why their abundance is compatible with §*The Two-Sided Ideals: Simplicity of $\mathbb{B}$*.

## The Lattice of Left Ideals

Over $\mathbb{C}$, every left ideal of the simple artinian algebra $\mathbb{B}$ is a direct sum of minimal left ideals, so the left ideals are exactly $0$, the minimal ones, and $\mathbb{B}$. The minimal left ideals form the middle layer of the lattice,

$$
0 \;\subset\; \{\, L : L \text{ a minimal left ideal} \,\} \;\subset\; \mathbb{B},
$$

the elements of the middle layer being pairwise incomparable, each covering $0$ and covered by $\mathbb{B}$. Because the length of $\mathbb{B}$ as a left module over itself is $2$, every minimal left ideal is also a **maximal** left ideal, nothing lying strictly between it and $\mathbb{B}$. The minimal left ideals are parametrized by the projective line $\mathbb{P}^1(\mathbb{C})$. Right ideals admit the same description, with the dual parametrization.

The parameter space deserves a caution. In the Wedderburn–Artin decomposition $M_n(D)$ of a simple artinian algebra, the minimal one-sided ideals are parametrized by the projective space $\mathbb{P}^{n-1}(D)$ over the **division ring** $D$, not over an arbitrary base field. Here $D = \mathbb{C}$ and $n = 2$, so the parameter space is $\mathbb{P}^1(\mathbb{C})$. In particular, regarding $\mathbb{B}$ as an $\mathbb{R}$-algebra does not replace this by $\mathbb{P}^1(\mathbb{R})$: the one-sided ideals are still parametrized by $\mathbb{P}^1(\mathbb{C})$. The real projective line appears only as the subfamily that the real structure preserves, not as a set of fixed minimal left ideals: §*The Real Structure* shows that no minimal left ideal is stable under coefficient conjugation.

## The Radical

The **Jacobson radical** $J(A)$ is the intersection of all maximal left ideals of $A$, equivalently of all maximal right ideals; it is a two-sided ideal. For an artinian ring, $J(A)$ is the largest nilpotent ideal and $A/J(A)$ is semisimple; an artinian ring is semisimple if and only if its radical is zero.

Over $\mathbb{C}$, the radical of $\mathbb{B}$ vanishes:

$$
J(\mathbb{B}) = 0.
$$

Indeed $J(\mathbb{B})$ is a two-sided ideal, hence by simplicity is $0$ or $\mathbb{B}$; it cannot be $\mathbb{B}$, since in a unital algebra the radical is proper. This restates the semisimplicity of §*Artinian, Semisimple, and Length Two* in terms of the radical. Consequences over $\mathbb{C}$:

- $\mathbb{B}$ has no nonzero **nilpotent two-sided ideals**; the nilradical is zero.
- It has no nonzero nilpotent left or right ideals either, since such an ideal generates a nonzero nilpotent two-sided ideal.
- The absence of a radical is not the absence of nilpotent **elements**: $\tilde\Upsilon_1^2 = \tilde\Upsilon_2^2 = 0$ (§*The Off-Diagonal Elements*) — nilpotents of the biquaternion layer, written $\tilde\Upsilon_1$ and $\tilde\Upsilon_2$ for the two particular units and $\tilde\Upsilon$ where the class is what is meant (§*The nilpotent convention* of *Conventions in Mathematics*) — yet the left ideal generated by $\tilde\Upsilon_1$ is not nilpotent.
- Every left $\mathbb{B}$-module is semisimple.

## The Real Structure

Everything so far was stated over $\mathbb{C}$. We now regard the same set $\mathbb{B}$ as an eight-dimensional algebra over $\mathbb{R}$ and record what changes.

**(a) The ideal lattice does not change.** By the base-field remark of §*Ideals in an Algebra*, an additive subgroup closed under left multiplication by $\mathbb{B}$ is automatically a complex subspace, because multiplication by $i$ is left multiplication by the central element $i e_0$. So an $\mathbb{R}$-left ideal is the same thing as a $\mathbb{C}$-left ideal, and the same holds on the right and for two-sided ideals. In particular, over $\mathbb{R}$: $\mathbb{B}$ is still simple, with two-sided ideals only $0$ and $\mathbb{B}$; the minimal left ideals are the same subsets, parametrized by $\mathbb{P}^1(\mathbb{C})$; the radical is still zero; and the length as a module over itself is still $2$.

**(b) The algebra is not central over $\mathbb{R}$.** The centre of $\mathbb{B}$ is the copy of $\mathbb{C}$ spanned by $e_0$ and $i e_0$ — the **complex subspace** $\mathbb{C}_{\mathbb{B}}$ — a proper field extension of $\mathbb{R}$ of degree $2$. Thus $\mathbb{B}$ is a simple $\mathbb{R}$-algebra but not a **central simple** one. In the Wedderburn–Artin description $\mathbb{B} \cong M_n(D)$ over $\mathbb{R}$, one has $n = 2$ and $D = \mathbb{C}$.

**(c) The enrichment appears after extension of scalars.** The complexification of the real algebra $\mathbb{B}$ is

$$
\mathbb{B} \otimes_{\mathbb{R}} \mathbb{C} \cong (\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}) \otimes_{\mathbb{R}} \mathbb{C} \cong (\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C}) \otimes_{\mathbb{R}} \mathbb{H} \cong (\mathbb{C} \oplus \mathbb{C}) \otimes_{\mathbb{R}} \mathbb{H} \cong \mathbb{B} \oplus \mathbb{B},
$$

using $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C} \cong \mathbb{C} \oplus \mathbb{C}$ and the associativity and commutativity of $\otimes_{\mathbb{R}}$. The algebra on the right is **not simple**: its two-sided ideals are $0$, the two summands, and the whole ring. So the real biquaternion algebra is **not absolutely simple**: simple over $\mathbb{R}$, but with a complexification that splits as a product of two simple algebras. This is the precise sense in which the real structure carries a richer two-sided ideal theory — not in the lattice of $\mathbb{B}$ itself, which is $\{0, \mathbb{B}\}$ in both views, but in the lattice produced by base change. In contrast, $\mathbb{H} \otimes_{\mathbb{R}} \mathbb{C} \cong \mathbb{B}$ is simple: it is the real biquaternion algebra, not $\mathbb{H}$, whose complexification splits.

**(d) The action of complex conjugation on the lattice.** Complex conjugation $\tilde{Q} \mapsto \bar{\tilde{Q}} = \sum_\mu \bar{Q}_\mu e_\mu$ is an $\mathbb{R}$-algebra automorphism of $\mathbb{B}$ (it is $\mathbb{C}$-antilinear); write $\sigma$ for it. It permutes the left ideals, $\sigma(\mathbb{B}\tilde{\chi}) = \mathbb{B}\sigma(\tilde{\chi})$. Since $\sigma(\tilde\Pi_1) = \tilde\Pi_2$ and $\sigma(\tilde\Pi_2) = \tilde\Pi_1$, it **interchanges the two standard left ideals**:

$$
\sigma(\mathbb{B}\tilde\Pi_1) = \mathbb{B}\tilde\Pi_2, \qquad \sigma(\mathbb{B}\tilde\Pi_2) = \mathbb{B}\tilde\Pi_1.
$$

On the parametrizing projective line the induced map $t \mapsto -1/\bar{t}$ has no fixed point, so **no minimal left ideal is stable under complex conjugation**. The **real lines** still form the real projective line $\mathbb{P}^1(\mathbb{R}) \subset \mathbb{P}^1(\mathbb{C})$, which $\sigma$ preserves and acts on as the antipodal map. So although the lattice of left ideals is unchanged from $\mathbb{C}$ to $\mathbb{R}$, the real structure does not mark out conjugation-stable minimal left ideals; what it marks out is the subfamily $\mathbb{P}^1(\mathbb{R})$ that it preserves.

**(e) The real structure on the Peirce spaces.** Each of the four Peirce spaces of §*The Peirce Decomposition* is a complex line, hence a real plane of dimension $2$; the decomposition into four real planes is what the real view adds to the complex statement. The coefficient conjugation $\sigma$ acts on the four spaces as in §*The Involutions on the Peirce Spaces*: it exchanges the two diagonal corners, $\sigma(\mathbb{C}\tilde\Pi_1) = \mathbb{C}\tilde\Pi_2$, and it exchanges the two mixed corners, $\sigma(\mathbb{C}\tilde\Upsilon_1) = \mathbb{C}\tilde\Upsilon_2$. It therefore preserves the Peirce grading of §*The Decomposition as a Grading* as a pair of subspaces — it fixes $A_0$ and $A_1$ — while permuting the two summands inside each, and it fixes none of the four spaces individually. The Hermitian conjugation, the composite of $\sigma$ with the natural sign, is the conjugation that respects the standard idempotents: it fixes each diagonal corner and exchanges the two mixed ones, the exchange of *Hermitian Idempotents and the Peirce Decomposition*, §*The Involution on the Peirce Spaces*. So the real structure does not single out a Peirce space; what it singles out is the pair of Hermitian idempotents $\tilde\Pi_1, \tilde\Pi_2$ whose corners it fixes, and it is by that pair that the real and the complex Peirce decompositions are matched.

## Summary

| Statement | Over $\mathbb{C}$ | Over $\mathbb{R}$ |
|---|---|---|
| Dimension | $4$ | $8$ |
| Algebra type | simple $\mathbb{C}$-algebra, $\dim 4$ | simple $\mathbb{R}$-algebra, $\dim 8$ |
| Two-sided ideals | $0$, $\mathbb{B}$ (simple) | $0$, $\mathbb{B}$ (simple) |
| Central simple? | yes, centre $\mathbb{C}$ | no, centre $\mathbb{C} \neq \mathbb{R}$ |
| Left ideals | $0$, the $\mathbb{P}^1(\mathbb{C})$ of minimal ones, $\mathbb{B}$ | same lattice |
| Minimal left ideals | all isomorphic | same; $\sigma$ pairs them, none stable |
| Minimal right ideals | all isomorphic | same |
| Peirce decomposition | $\mathbb{C}\tilde\Pi_1 \oplus \mathbb{C}\tilde\Upsilon_1 \oplus \mathbb{C}\tilde\Upsilon_2 \oplus \mathbb{C}\tilde\Pi_2$, four one-dimensional corners | the same four real planes; $\sigma$ permutes them in pairs |
| Peirce coordinates | the entries of $\mathsf{M}_2(\tilde Q)$; $a_{11}a_{22}-a_{12}a_{21} = N(\tilde Q)$ | the same, over $\mathbb{R}$ |
| Matrix units | the standard system $\tilde\Pi_1, \tilde\Upsilon_1, \tilde\Upsilon_2, \tilde\Pi_2$ | the same; every system is conjugate to it |
| Grading | $A_0 \oplus A_1$, $A_0 = \mathbb{C}\tilde\Pi_1\oplus\mathbb{C}\tilde\Pi_2 \cong \mathbb{C}\times\mathbb{C}$, $A_1 = \mathbb{C}\tilde\Upsilon_1\oplus\mathbb{C}\tilde\Upsilon_2$ | the same; $\sigma$ preserves both parts |
| Jacobson radical | $0$ | $0$ |
| Length as module over itself | $2$ | $2$ |
| Base change $\otimes_{\mathbb{R}}\mathbb{C}$ | — | not simple; splits into two simple factors |

The Peirce decomposition is the second reading of the same four-dimensional space, and it carries four structures that the lattice of ideals alone does not show. It is a decomposition into four one-dimensional corners, of which the two diagonal ones are the division ring $\mathbb{C}$ and the two mixed ones are square-zero subalgebras. It is the table of a $2\times2$ matrix, and its four coordinate functions are the entries of the corpus's matrix element representation, so that the scalar part is their mean and the biquaternion norm is their determinant. It is a $\mathbb{Z}/2$-grading, whose even part is the diagonal subalgebra $\mathbb{C}\times\mathbb{C}$ and whose odd part carries the two mixed spaces and the products $\tilde\Upsilon_1\tilde\Upsilon_2 = \tilde\Pi_1$ and $\tilde\Upsilon_2\tilde\Upsilon_1 = \tilde\Pi_2$. And it is acted on by the three conjugations, the natural sign and the bar exchanging the diagonal corners and the Hermitian conjugation fixing them and exchanging the mixed ones. The decomposition is rigid in the only sense available: every system of $2\times2$ matrix units is the image of the standard one under an inner automorphism, so the algebra has a single block structure, and the choices that remain are the idempotent manifold and the projective line of minimal left ideals of the earlier sections.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | Biquaternion algebra; dimension $4$ over $\mathbb{C}$, $8$ over $\mathbb{R}$ |
| $e_0, e_1, e_2, e_3$ | Algebra basis, $e_0 = 1$, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary; $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the centre |
| $\tilde\Pi_1, \tilde\Pi_2$ | Orthogonal idempotents, $\tilde\Pi_1+\tilde\Pi_2 = e_0$, $\tilde\Pi_1\tilde\Pi_2 = \tilde\Pi_2\tilde\Pi_1 = 0$ |
| $\tilde\Upsilon_1, \tilde\Upsilon_2$ | Nilpotent off-diagonal elements, $\tilde\Upsilon_1 = \tfrac{i e_1 - e_2}{2}$, $\tilde\Upsilon_2 = \tfrac{i e_1 + e_2}{2}$, $\tilde\Upsilon_1^2 = \tilde\Upsilon_2^2 = 0$ |
| $\mathbb{B}\tilde\Pi_1 \cong \mathbb{C}^2$ | The minimal left ideal, a simple left $\mathbb{B}$-module, $i$ acting as the scalar $i$ |
| $\mathbb{P}^1(\mathbb{C})$ | The projective line parameterising the minimal left ideals |
| $a_{ij}$ | Peirce coordinate, the coefficient of the corner $\tilde\Pi_i\mathbb{B}\tilde\Pi_j$; the $(i,j)$ entry of $\mathsf{M}_2(\tilde Q)$ |
| $\mathsf{M}_2$ | The matrix element representation $\mathbb{B} \cong M_2(\mathbb{C})$, whose entries are the Peirce coordinates |
| $E_{ij}$ | A system of $2\times2$ matrix units, $E_{ij}E_{kl} = \delta_{jk}E_{il}$, $E_{11}+E_{22} = e_0$ |
| $A_0, A_1$ | The diagonal and the mixed parts of the Peirce decomposition, the two graded components |
| $\natural, \bar{\cdot}, {}^{*}$ | The natural, the bar (coefficient) and the Hermitian conjugations, with ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ |
| $\sigma$ | The real structure, pairing the two standard minimal left ideals and the Peirce corners |
| $\mathcal{J}$ | Jacobson radical; it is $0$ for $\mathbb{B}$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982). The standard reference for the Peirce decomposition and the structure theory of finite-dimensional algebras.
- T. Y. Lam, *A First Course in Noncommutative Rings*, Graduate Texts in Mathematics 131 (Springer, 2nd ed. 2001). Simplicity, semisimplicity, the Jacobson radical, and matrix rings.
- Nathan Jacobson, *Basic Algebra II* (Dover, 2nd ed. 2009). Wedderburn–Artin theory and the radical.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002). Ring and module theory, central simple algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001). The algebraic structure of the biquaternion algebra.
- The companion articles of the Peirce theory: *Unital Algebras* (the general Peirce decomposition and the central case), *Matrix Algebras* (the matrix units, the matrix algebra and the Skolem–Noether theorem), *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (the isomorphism of which the Peirce coordinates are the entries), *Idempotents of the General Plain Algebra* (the idempotent manifold), *Hermitian Idempotents and the Peirce Decomposition* (the involution on the Peirce spaces) and *Biquaternion Automorphisms and Derivations* (the inner automorphisms that make the decomposition rigid).
