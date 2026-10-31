# __Matrix Representations : The Models and the Change of Frame__

## Introduction

**The subject.** This article fixes the three displays of the corpus and the change between two of them: the $2\times2$ entry model $\mathsf M_2$, the $4\times4$ coefficient frame, and the $4\times4$ block frame. It is the reference article of the series. Every other article names one of these displays, and inherits from here the bracket, the change law and the frame change $C_{\Pi}$.

**Three displays, two objects.** The $2\times2$ model displays an element. The two $4\times4$ frames display an operator. The distinction is the one that governs the whole series: an element has one $2\times2$ matrix and no frame; an operator has a $4\times4$ matrix in each frame and no $2\times2$ matrix at all.

**What it defines.** Three glyphs are fixed here for the whole operator group: the bracket $[F]_{\mathcal{B}}$, the matrix units $E_{ij}$ in the coefficient frame, and the frame change $C_{\Pi}$. The bracket is new; the units are the matrix units of the conventions, written here in the coefficient frame; the change is the fixed matrix defined in §*The Change $C_{\Pi}$* below. The article fixes their use in the operator space and repeats no definition that the earlier articles already give.

**What it does not do.** It states no property of the four families $L$, $R$, $T$, $\Theta$. It does not prove that a family is closed under anything, that it has a dimension, or that it sits inside another. The closing section counts the defining data of the four families and stops at the count. The definitions and the properties are the subject of Parts II, III, IV and V.

**The matrix is not canonical.** A matrix is the display of an operator in a frame. There is no frame-free matrix, and this article never writes "the matrix of $F$" without a frame. The invariants of §*Trace, Determinant, Spectrum, Rank* are the exception that proves the rule: they are read on a matrix and belong to the operator.

**Boundaries.** The algebra and its basis are *The Biquaternion Algebra*; the operator space is the complex vector space of linear maps of $\mathbb{B}$ into itself, introduced here; the $2\times2$ model and the coefficient frame are fixed in this article; the block decomposition is fixed by the standard pair of *Matrix Representations Conventions*, §*The Matrix Models*.

## Common Aspects

The bracket, the change law, the invariants and the unit table are statements about operators and frames, not about one display. They are fixed here once and used in all three displays below.

### The Matrix in a Basis

**The Four Columns.**

**The frame.** A **frame** of the carrier is an ordered basis $\mathcal{B}=(b_1,b_2,b_3,b_4)$. The coefficient frame is the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ in that order. Every matrix in this article is written in a declared frame, and the frame is part of the display.

**Definition (the bracket).** Let $F\in\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ and let $\mathcal{B}$ be a frame. The **matrix of $F$ in $\mathcal{B}$** is the $4\times4$ complex matrix $[F]_{\mathcal{B}}$ whose $j$-th column is the coordinate column of $F(b_j)$ in $\mathcal{B}$:

$$
[F]_{\mathcal{B}}=\Bigl(\,[F(b_1)]_{\mathcal{B}}\ \ [F(b_2)]_{\mathcal{B}}\ \ [F(b_3)]_{\mathcal{B}}\ \ [F(b_4)]_{\mathcal{B}}\,\Bigr).
$$

**Reading the bracket.** The bracket carries an operator and a frame. The operator is on the left of the bracket, the frame is the subscript, and the result is a matrix. The bracket is written on an element only for the coordinate column, never for a matrix in this sense: the coordinate column of $x$ is written $[x]_{\mathcal{B}}$, with the same bracket and the element inside. The two uses are distinguished by the object, an operator or an element.

**The defining property.** For every $x\in\mathbb{B}$,

$$
[F(x)]_{\mathcal{B}}=[F]_{\mathcal{B}}\,[x]_{\mathcal{B}}.
$$

The matrix acts on coordinate columns by the usual product. This is the reason the columns are the images of the basis: the $j$-th column is the image of the $j$-th basis vector, and the coordinate column of $x$ is the list of its coefficients.

**Elementary properties.** For operators $F,G$ and scalars $\lambda,\mu$,

$$
[\mathrm{id}]_{\mathcal{B}}=\mathrm{I}_4,\qquad [\lambda F+\mu G]_{\mathcal{B}}=\lambda[F]_{\mathcal{B}}+\mu[G]_{\mathcal{B}},\qquad [FG]_{\mathcal{B}}=[F]_{\mathcal{B}}[G]_{\mathcal{B}}.
$$

The three identities are read column by column, and they say that the bracket is an algebra map. The order in the product is the order of composition: $[FG]$ is $[F]$ times $[G]$, with $G$ applied first.

**An operator is determined by its matrix.** If $[F]_{\mathcal{B}}=[G]_{\mathcal{B}}$, then $F$ and $G$ agree on the four basis vectors, hence everywhere. The bracket is therefore injective for a fixed frame, and a matrix in a frame names at most one operator.

**The Isomorphism with $M_4(\mathbb{C})$.**

**Theorem (the matrix representation).** For every frame $\mathcal{B}$, the map

$$
\Phi_{\mathcal{B}}:\operatorname{End}_{\mathbb{C}}(\mathbb{B})\longrightarrow M_4(\mathbb{C}),\qquad F\longmapsto[F]_{\mathcal{B}},
$$

is an isomorphism of complex algebras.

*Proof.* The map is linear by the elementary properties and multiplicative by $[FG]=[F][G]$; it is unital because $[\mathrm{id}]=\mathrm{I}_4$. It is injective because an operator is determined by its matrix. It is surjective because every $4\times4$ matrix $A$ defines an operator by $[F(b_j)]_{\mathcal{B}}=A e_j$, and then $[F]_{\mathcal{B}}=A$. Both spaces have complex dimension $16$, so injectivity alone would also give the conclusion.

**The isomorphism depends on the frame.** A different frame gives a different map $\Phi_{\mathcal{B}'}$, and the two differ by the change of §*Change of Basis*. There is no frame-free identification of the operator algebra with $M_4(\mathbb{C})$, and an article that writes the identification writes the frame beside it. The identification is canonical only after the frame is fixed, and no frame is canonical in the algebra.

**What the theorem gives.** The theorem is the licence to compute with matrices in every article of Parts I to V: an operator statement can be read entry by entry after a frame is declared. It gives no canonical form and no preferred matrix, and it does not say that two operators with the same trace or determinant are equal.

### Change of Basis

**The Conjugation Law $C^{-1}[F]C$.**

**The change of frame.** Let $\mathcal{B}=(b_1,\dots,b_4)$ and $\mathcal{B}'=(b'_1,\dots,b'_4)$ be two frames, and let $C\in GL_4(\mathbb{C})$ be the matrix of the change, with

$$
b'_j=\sum_{i=1}^{4}b_i\,C_{ij}.
$$

The columns of $C$ are the new basis vectors in the old frame, so $[x]_{\mathcal{B}}=C\,[x]_{\mathcal{B}'}$ for every element.

**Theorem (the conjugation law).** For every operator $F$,

$$
[F]_{\mathcal{B}'}=C^{-1}[F]_{\mathcal{B}}\,C .
$$

*Proof.* For every $x$, $[F(x)]_{\mathcal{B}'}=C^{-1}[F(x)]_{\mathcal{B}}=C^{-1}[F]_{\mathcal{B}}[x]_{\mathcal{B}}=C^{-1}[F]_{\mathcal{B}}C[x]_{\mathcal{B}'}$. The matrix $C^{-1}[F]_{\mathcal{B}}C$ therefore acts on every coordinate column as $[F]_{\mathcal{B}'}$ does, and the two matrices are equal.

**Similar matrices.** Two matrices are **similar** when they differ by $C^{-1}(\cdot)C$ for some invertible $C$. The theorem says that the matrices of one operator in two frames are similar, and conversely every matrix similar to $[F]_{\mathcal{B}}$ is the matrix of $F$ in some frame. Similarity is therefore the equivalence relation of the display, and the orbit of $[F]_{\mathcal{B}}$ is the set of all displays of $F$.

**The invariant reading.** The trace, the determinant, the characteristic polynomial, the spectrum and the rank are unchanged by $C^{-1}(\cdot)C$, so they are functions of the operator and not of the frame. Conversely, none of them separates all operators: two non-similar matrices can share all five. The invariants are necessary data, not a complete invariant.

**Orbits and the Missing Canonical Form.**

**The orbit is the operator.** The similarity orbit of a matrix is the operator, read in all frames. To know the operator is to know the orbit, and to write one matrix is to choose a point of the orbit. The choice is a choice of frame and has no algebraic content.

**No canonical representative.** There is no rule that selects one matrix from each orbit without further choices. A canonical form selects a matrix, but it depends on the order of the blocks and on the scaling of the eigenvectors, and it exists as a canonical display only after those choices are fixed. The rational canonical form is canonical for the operator, but its display still requires an ordered decomposition of the carrier. The corpus therefore does not write "the matrix" of a general operator, and it does not treat a canonical form as a property of the operator.

**What is canonical.** The characteristic polynomial is canonical: it is the same for every matrix of $F$ and needs no choice. The spectrum is canonical as a multiset. The trace, the determinant and the rank are canonical numbers. Beyond them, a statement about entries is a statement about a frame, and it must say which frame.

**The warning.** An entry of $[F]_{\mathcal{B}}$ is not a function of $F$. A statement such as "the upper-right entry vanishes" is a statement about the pair $(F,\mathcal{B})$, and it becomes a statement about $F$ only when the frame is fixed by the algebra, as the coefficient frame and the block frame are. Every display in Parts I to V declares its frame for this reason.

### Trace, Determinant, Spectrum, Rank

**The Trace and the Determinant.**

**The trace.** The **trace** of an operator is the sum of the diagonal entries of any of its matrices:

$$
\operatorname{tr}F=\sum_{i=1}^{4}[F]_{\mathcal{B},ii}.
$$

The sum is independent of the frame, because $\operatorname{tr}(C^{-1}AC)=\operatorname{tr}A$. The trace is linear, $\operatorname{tr}(\lambda F+\mu G)=\lambda\operatorname{tr}F+\mu\operatorname{tr}G$, and it satisfies $\operatorname{tr}(FG)=\operatorname{tr}(GF)$.

**The determinant.** The **determinant** of an operator is the determinant of any of its matrices. It is multiplicative, $\det(FG)=\det F\det G$, and $\det(\mathrm{id})=1$. An operator is invertible exactly when $\det F\neq0$, and then $\det(F^{-1})=(\det F)^{-1}$.

**Not the invariants of an element.** The trace and the determinant are written of an operator. An element of the algebra has its coefficients and its determinant, and they are different objects: the trace of an operator is a complex number attached to a map, and no coefficient of an element is called a trace here. The two readings are kept apart by the symbol the word is applied to.

**The Characteristic Polynomial.**

**Definition.** The **characteristic polynomial** of $F$ is

$$
\chi_F(\lambda)=\det\bigl(\lambda\,\mathrm{I}_4-[F]_{\mathcal{B}}\bigr).
$$

It is a monic polynomial of degree four with complex coefficients, and it is independent of the frame because the determinant is.

**The coefficients.** Written out,

$$
\chi_F(\lambda)=\lambda^4-\operatorname{tr}(F)\,\lambda^3+c_2\lambda^2-c_3\lambda+\det(F),
$$

where $c_2$ and $c_3$ are the elementary symmetric functions of the eigenvalues, and $c_3$ is the trace of the adjugate. The four coefficients are polynomial functions of the entries and are invariant under similarity.

**The spectrum.** The **spectrum** of $F$ is the multiset of the four roots of $\chi_F$, counted with multiplicity. Over $\mathbb{C}$ the polynomial splits, so the spectrum always has four elements counted with multiplicity, and it is a set only when the four roots are distinct. The eigenvalues are the roots, and an eigenvector of $\lambda$ is a nonzero element of $\ker(\lambda\,\mathrm{id}-F)$.

**Cayley–Hamilton.** $\chi_F(F)=0$ as an operator. The identity is read in any frame, where it is the Cayley–Hamilton theorem for the matrix $[F]_{\mathcal{B}}$. It gives the powers $F^4,\dots$ in terms of the lower ones, and it is the reason the minimal polynomial divides the characteristic polynomial.

**The minimal polynomial.** The **minimal polynomial** of $F$ is the monic polynomial of least degree with $m_F(F)=0$. It divides $\chi_F$ and has the same roots; the operator is diagonalisable exactly when $m_F$ has distinct roots. The minimal polynomial is canonical and is a finer invariant than the characteristic polynomial.

**The Rank and the Image.**

**Definition (rank).** The **rank** of an operator is the complex dimension of its image,

$$
\operatorname{rank}F=\dim_{\mathbb{C}}\operatorname{im}F .
$$

It is the rank of any of its matrices, and it is invariant under similarity. It is the size of the largest invertible square submatrix, and it is not the number of nonzero entries: a matrix with many nonzero entries can have rank one.

**Rank and nullity.** The kernel and the image are subspaces of the carrier, and

$$
\dim_{\mathbb{C}}\ker F+\operatorname{rank}F=4 .
$$

The operator is injective exactly when $\ker F=0$, exactly when $\operatorname{rank}F=4$, exactly when $\det F\neq0$. For an operator of a finite-dimensional space the three conditions are equivalent, and they are equivalent to surjectivity and to invertibility.

**The image and the kernel are not frames.** The image is a subspace of $\mathbb{B}$ and the kernel is a subspace of $\mathbb{B}$; neither is a subspace of the matrix space. A matrix has a column space and a null space in $\mathbb{C}^4$, and those are the coordinate readings of the image and the kernel in the frame. The two pairs are the same object only after the frame is declared.

**The rank is not the length.** The word **length** is reserved for a two-sided operator and is fixed in *Operator Family Conventions*. It is not an alternative name for the rank, and an article that identifies the two proves it there.

### The Units

**The Unit Table.**

**The units.** The **matrix units** are the operators $E_{ij}$ with $i,j\in\{1,2,3,4\}$, where $E_{ij}$ sends the $j$-th basis vector to the $i$-th and the other basis vectors to zero:

$$
E_{ij}(b_j)=b_i,\qquad E_{ij}(b_k)=0\quad(k\neq j).
$$

The glyph is the matrix unit of the conventions: a matrix unit, $1$-based, written only in a matrix model. The definition above is its reading in the frame $\mathcal{B}$.

**The table.** The sixteen units, by row and column:

| | $j=1$ | $j=2$ | $j=3$ | $j=4$ |
|---|---|---|---|---|
| $i=1$ | $E_{11}$ | $E_{12}$ | $E_{13}$ | $E_{14}$ |
| $i=2$ | $E_{21}$ | $E_{22}$ | $E_{23}$ | $E_{24}$ |
| $i=3$ | $E_{31}$ | $E_{32}$ | $E_{33}$ | $E_{34}$ |
| $i=4$ | $E_{41}$ | $E_{42}$ | $E_{43}$ | $E_{44}$ |

**The matrix of a unit.** In the frame $\mathcal{B}$, $[E_{ij}]_{\mathcal{B}}$ has the entry $1$ in row $i$ and column $j$, and $0$ elsewhere. It is the matrix unit of $M_4(\mathbb{C})$ in the same sense, and the bracket and the matrix unit agree under the isomorphism of §*The Isomorphism with M_4(C)*.

**The products.** The units multiply by

$$
E_{ij}E_{kl}=\delta_{jk}E_{il},
$$

with $\delta_{jk}$ the Kronecker delta. In particular $E_{ii}^2=E_{ii}$ and $E_{ii}E_{jj}=0$ for $i\neq j$, so the four diagonal units are projections, and

$$
\sum_{i=1}^{4}E_{ii}=\mathrm{I}_4 .
$$

The sixteen units are a basis of the operator space, and the product rule is the multiplication table of $M_4(\mathbb{C})$ in that basis.

**The frame dependence.** The units are defined in the frame $\mathcal{B}$. Another frame gives another family of sixteen operators, and the two families are related by the change of §*Change of Basis*. The notation $E_{ij}$ without a frame is read in the frame declared by the article, and no article inherits it from another.

**The Algebra's Units and the Operator's Units.**

**Two alphabets.** The algebra has its units $e_t,\vec e_x,\vec e_y,\vec e_z$, four elements. The operator space has its units $E_{ij}$, sixteen operators. The two alphabets are distinct, and no glyph of one stands for a glyph of the other.

**The two identities.** The identity of the algebra is $e_t$; the identity of the operator algebra is $\mathrm{I}_4=\sum_iE_{ii}$. The first is an element and the second is an operator, and the words "the unit" and "the identity" are qualified: the unit of the algebra, the identity operator.

**The index is not a direction.** The index of $e_\mu$ is a direction of the algebra, running over $t,x,y,z$. The indices of $E_{ij}$ are a row and a column, running over $1,2,3,4$. A direction index is never a row index, and $e_1$ is not written for $e_t$.

**The diagonal units are not the standard idempotents.** $E_{ii}$ is a projection of the carrier, an operator; the standard idempotents $\tilde\Pi_1,\tilde\Pi_2$ are elements of the algebra. The two are read in different frames and belong to different spaces, and neither glyph stands for the other.

### The General Matrix and the Four Families

**Sixteen Entries.**

**The general matrix.** In a frame, a general operator is a $4\times4$ complex matrix, with sixteen entries and no condition. The sixteen entries are sixteen complex numbers; they are not sixteen invariants, and no one of them is a function of the operator alone. A statement about an entry is a statement about the operator and the frame together.

**No preferred entry.** The diagonal, the upper triangle and the lower triangle are not canonical subsets of the entries: a change of frame mixes them. The only subsets of entries that survive every frame are the empty set and the whole matrix, and the only functions of the entries that survive are the symmetric ones, of which the trace and the determinant are the first and the last.

**No canonical form.** A general operator has no canonical matrix. A canonical form, such as the rational canonical form, is a canonical display only after choices, and this article does not use them. The general matrix is therefore written with its frame and with its sixteen entries, and nothing more is asserted about it.

**The Four Subsets.**

**The count.** The four families are four subsets of the operator space. Their defining data are counted here, and nothing else is asserted:

| Subset | Glyph | Defining data | Complex parameters |
|---|---|---|---|
| $\operatorname{End}_L(\mathbb{B})$ | $L_{\tilde Q}$ | one element $\tilde Q$ | $4$ |
| $\operatorname{End}_R(\mathbb{B})$ | $R_{\tilde Q}$ | one element $\tilde Q$ | $4$ |
| $\operatorname{End}_{LR}(\mathbb{B})$ | $T_{\tilde Q,\tilde P}$ | two elements $\tilde Q,\tilde P$ | $8$ |
| $\operatorname{End}_{LR\ast}(\mathbb{B})$ | $\Theta_{\tilde Q}$ | one element $\tilde Q$ | $4$ |

**The counts are not dimensions.** A count of parameters is not the dimension of a set. The two-sided family is described by two elements, eight complex numbers, and the descriptions overlap, so the count of parameters exceeds the number of independent data. The resolution of the overlap is the subject of Parts II to V, and no number in the table is a dimension.

**The counts are not disjoint.** The four parameter counts add to $20$, while a general operator has $16$ complex parameters. The excess is the redundancy of the four descriptions, not a theorem about the four families. The table says how many complex numbers each description uses, and it stops there: it asserts no inclusion, no closure, no properness and no dimension.

**What the section proves.** Nothing. It fixes the place of the four families in the general matrix by counting their defining data, and it leaves every property to the article that owns it: the left family to Part II, the right family to Part III, the two-sided family to Part IV, and the sandwich to Part V.

**Two frames, two readings.** The coefficient frame reads the multiplication as signed permutations of the four units. The block frame reads it as a $2\times2$ block structure with two copies of $M_2(\mathbb{C})$. Neither frame is preferred by the algebra, and each article declares the one it uses.

## The Coefficient Frame

The coefficient frame is the frame of the structure constants. It is where the signed entries, the explicit display of the regular operator and the frame change $C_{\Pi}$ are read.

**The coefficient frame.** The **coefficient frame** is the ordered basis

$$
\mathcal{B}=(e_t,\vec e_x,\vec e_y,\vec e_z).
$$

It is the frame of the structure constants: the product of two units is a signed unit, and every element is a coefficient column in this frame. It is fixed by the algebra and by the order of the units, and it is the frame of the coefficient matrices of Parts II to V.

### The Change $C_{\Pi}$

**Definition (the frame change).** The **frame change** $C_{\Pi}$ is the matrix whose columns are the four block elements, in the order $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$, written in coefficient coordinates:

$$
C_{\Pi}=\begin{pmatrix}
\tfrac12&0&0&\tfrac12\\
0&\tfrac{i}{2}&\tfrac{i}{2}&0\\
0&\tfrac12&-\tfrac12&0\\
\tfrac{i}{2}&0&0&-\tfrac{i}{2}
\end{pmatrix}.
$$

Its inverse is

$$
C_{\Pi}^{-1}=\begin{pmatrix}
1&0&0&-i\\
0&-i&1&0\\
0&-i&-1&0\\
1&0&0&i
\end{pmatrix},
$$

and $\det C_{\Pi}=-\tfrac14$. The change is the one of *Matrix Representations : The Product, the Trace and the Determinant*, §*The Element and the Operator*; the display is repeated here because every operator article uses it.

**The direction.** The columns of $C_{\Pi}$ are the block elements in coefficient coordinates, so $C_{\Pi}$ carries a block coordinate column to a coefficient coordinate column:

$$
[x]_{\mathcal{B}}=C_{\Pi}\,[x]_{\mathcal{P}} .
$$

The inverse carries the other way.

**The conjugation by the change.** For an operator $F$,

$$
[F]_{\mathcal{B}}=C_{\Pi}\,[F]_{\mathcal{P}}\,C_{\Pi}^{-1},
\qquad
[F]_{\mathcal{P}}=C_{\Pi}^{-1}[F]_{\mathcal{B}}\,C_{\Pi}.
$$

The two displays are the same operator in the two frames. The change is a fixed matrix, not a similarity chosen for the operator: it is the same $C_{\Pi}$ for every $F$, and it is the reason the two frames are comparable at all.

**The determinant of the change.** $\det C_{\Pi}=-\tfrac14$ is not $\pm1$, so the change is not a permutation of the frame up to sign. A determinant computed in the coefficient frame and one computed in the block frame agree as determinants of the operator, because the two factors $C_{\Pi}$ and $C_{\Pi}^{-1}$ cancel; entries and minors need not agree. The rule is the one of §*Change of Basis*: invariants agree, entries do not.

**The regular operator in the coefficient frame.** The coefficient display is

$$
[\mathsf M_4^{L}(\tilde Q)]_{\mathrm{coef}}=C_{\Pi}\,\bigl(\mathrm I_2\otimes\mathsf M_2(\tilde Q)\bigr)\,C_{\Pi}^{-1}.
$$

Every entry is a signed combination of the four coefficients, and no $2\times2$ block of the display equals $\mathsf M_2(\tilde Q)$ or its negative. The change $C_{\Pi}$ below is the only matrix needed to pass from this display to the block display.

## The Entry Model

The entry model displays an element, not an operator. Its entries are the block coordinates at size two: the two diagonal entries are the idempotent coordinates and the two off-diagonal ones the mixed coordinates.

### The Assignment $\mathsf M_2$

**Definition.** On the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, the **entry model** is the assignment

$$
\mathsf M_2(e_t)=\mathrm I_2,\qquad
\mathsf M_2(\vec e_x)=-i\sigma_1,\qquad
\mathsf M_2(\vec e_y)=-i\sigma_2,\qquad
\mathsf M_2(\vec e_z)=-i\sigma_3,
$$

extended linearly:

$$
\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-iQ_x\sigma_1-iQ_y\sigma_2-iQ_z\sigma_3
=\begin{pmatrix}Q_t-iQ_z&-iQ_x-Q_y\\-iQ_x+Q_y&Q_t+iQ_z\end{pmatrix}.
$$

**What it displays.** The four entries are $Q_t-iQ_z$, $-iQ_x-Q_y$, $-iQ_x+Q_y$ and $Q_t+iQ_z$: the coefficients themselves, two on the diagonal and two off it. The model is an isomorphism of algebras onto $M_2(\mathbb{C})$. It displays an element rather than an operator, and its standard basis is the standard pair at $z$, so its four entries are the $z$-block coordinates. Its invariants are $\operatorname{tr}\mathsf M_2(\tilde Q)=2Q_t$ and $\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$.

**The chosen direction.** The display singles out $\vec e_z$, because $\sigma_3$ is the diagonal one. The other two directions sit in the off-diagonal entries, and a relabelling of $x,y,z$ carries the model to a conjugate display. The choice is a choice of axis in the model, not a property of the algebra, and the series names the axis whenever an entry is read.

## The Block Frame

The block frame displays the operator as two copies of the entry model, $\mathrm I_2\otimes\mathsf M_2$, and is the only frame in which a $2\times2$ block of the $4\times4$ matrix equals the entry matrix.

### The Operator Model $\mathsf M_4^{L}$

**Definition.** The **left regular matrix** $\mathsf M_4^{L}(\tilde Q)$ is the matrix of left multiplication by $\tilde Q$ in a declared frame. In the block frame it is one object,

$$
\mathsf M_4^{L}(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q),
$$

and in the coefficient frame it is the conjugate display,

$$
[\mathsf M_4^{L}(\tilde Q)]_{\mathrm{coef}}=C_{\Pi}\,\bigl(\mathrm I_2\otimes\mathsf M_2(\tilde Q)\bigr)\,C_{\Pi}^{-1}.
$$

**What it displays.** The $4\times4$ matrix displays the operator $L_{\tilde Q}$. It has sixteen entries and four eigenvalues $\lambda_\pm=Q_t\pm iB$, each twice. It is not the element: the element has four coefficients and its own matrix $\mathsf M_2(\tilde Q)$. The series keeps the two objects apart by the size of the display and by the letter: $\mathsf M_2$ for the element, $\mathsf M_4^{L}$ for the operator.

### The Compression

**The block structure.** In the block frame the left regular matrix is a block-diagonal matrix with the same block twice:

$$
C_{\Pi}^{-1}\,[\mathsf M_4^{L}(\tilde Q)]_{\mathrm{coef}}\,C_{\Pi}
=\operatorname{diag}(B,B),\qquad B=\mathsf M_2(\tilde Q).
$$

The identity is the definition of the block frame read backwards: the frame is chosen so that the carrier splits into two copies of the $2\times2$ space, and the element acts by $B$ on each copy.

**What the compression is not.** The $2\times2$ block is not a compression in the coefficient frame. No $2\times2$ block of $[\mathsf M_4^{L}]_{\mathrm{coef}}$ equals $B$ or $-B$, and the coefficient matrix is not $I_2\otimes B$ for any ordering of the four units. The two statements are not in conflict: the identity holds after the fixed change $C_{\Pi}$, and a fixed change of frame is not a compression of the entries. An article that writes "the $2\times2$ is a block of the $4\times4$" must name the block frame in the same sentence.

**The consequence for the series.** Only the block frame exhibits the entry model inside the operator model. The coefficient frame exhibits the signs, the transpose and the real forms. The two frames are therefore not interchangeable, and each article says which of the two it uses and what the other adds.

**The block frame.** The **block frame** is the ordered basis

$$
\mathcal{P}=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-),
$$

with the standard pair and its mixed units

$$
\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z),\qquad \vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y).
$$

It is the canonical frame of the matrix models: in it the left and the right regular matrices take their block form, and the block coordinates are the coordinates of the decomposition. The pair is a choice of frame, owned by *Matrix Representations Conventions*, §*The Matrix Models*, and it fixes nothing in the algebra.

## Summary

The matrix of an operator is written $[F]_{\mathcal{B}}$, and its $j$-th column is the coordinate column of $F(b_j)$. For a fixed frame the bracket is an algebra isomorphism $\operatorname{End}_{\mathbb{C}}(\mathbb{B})\to M_4(\mathbb{C})$, of complex dimension sixteen on both sides. A change of frame $C$ conjugates the matrix, $[F]_{\mathcal{B}'}=C^{-1}[F]_{\mathcal{B}}C$, and the similarity orbit is the operator read in all frames.

The trace, the determinant, the characteristic polynomial, the spectrum, the minimal polynomial and the rank are invariants of the operator and are read on any of its matrices. The trace is linear and cyclic, the determinant is multiplicative, and the rank is the dimension of the image. The characteristic polynomial is monic of degree four and splits over $\mathbb{C}$; the minimal polynomial divides it and is the finer invariant. There is no canonical matrix for a general operator, and an entry is a function of the operator and the frame together.

The units $E_{ij}$ are the matrix units in the coefficient frame, with $E_{ij}E_{kl}=\delta_{jk}E_{il}$ and $\sum_iE_{ii}=\mathrm{I}_4$. The algebra's units $e_t,\vec e_x,\vec e_y,\vec e_z$ are elements and the operator's units are operators; the two alphabets are not exchanged. The coefficient frame and the block frame are the two frames of the corpus, and the frame change $C_{\Pi}$ carries one coordinate column to the other, with $[F]_{\mathcal{B}}=C_{\Pi}[F]_{\mathcal{P}}C_{\Pi}^{-1}$. The $2\times2$ entry model displays an element and the two $4\times4$ frames display an operator; in the block frame the left regular matrix is $I_2\otimes\mathsf M_2$, so the entry model sits inside the operator model there and only there.

A general operator has sixteen entries and no canonical form. The four families are four subsets of the operator space, counted here by their defining data, four, four, eight and four complex parameters; the counts overlap, add to twenty and are not dimensions. The section asserts no inclusion, no closure and no property of the four families, and every such statement belongs to Parts II to V.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{B}$, $\mathcal{P}$ | The coefficient frame and the block frame |
| $[F]_{\mathcal{B}}$ | The matrix of the operator $F$ in the frame $\mathcal{B}$ |
| $[x]_{\mathcal{B}}$ | The coordinate column of the element $x$ |
| $C$, $C^{-1}$ | The change of frame and its inverse, $[F]_{\mathcal{B}'}=C^{-1}[F]_{\mathcal{B}}C$ |
| $\operatorname{tr}$, $\det$ | The trace and the determinant of an operator |
| $\chi_F$, $m_F$ | The characteristic and the minimal polynomial |
| $\operatorname{spec}F$ | The spectrum, a multiset of four roots |
| $\operatorname{rank}F$ | The dimension of the image |
| $E_{ij}$ | The matrix unit, $1$-based, $E_{ij}E_{kl}=\delta_{jk}E_{il}$ |
| $\mathrm{I}_4$ | The identity operator, $\sum_iE_{ii}$ |
| $\mathsf M_2$ | The $2\times2$ entry model of an element |
| $\mathsf M_4^{L}$ | The left regular matrix of an element |
| $C_{\Pi}$ | The frame change, columns $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$ |
| $\det C_{\Pi}$ | $-\tfrac14$ |
| $\operatorname{End}_L$, $\operatorname{End}_R$, $\operatorname{End}_{LR}$, $\operatorname{End}_{LR\ast}$ | The four subsets, counted in the closing section |

## Further Reading

- [The Endomorphisms of the Biquaternion Algebra](the-endomorphisms-of-the-biquaternion-algebra.html), for the operator space and its dimension.
- [The Matrix Algebra $M_4(\mathbb{C})$](the-matrix-algebra-m4c.html), for the algebra of matrices and its units.
- [Matrix Representations Conventions](conventions-of-the-matrix-models.html), for the two frames and the regular representation.
- [Matrix Representations : The Product, the Trace and the Determinant](matrix-representations-the-product-the-trace-and-the-determinant.html), for the product, the trace and the determinant in the two sizes.
- [The Left Regular Operators on the Biquaternion Algebra](the-left-regular-operators-on-the-biquaternion-algebra.html), for the first family and its matrix.
- [The Right Regular Operators on the Biquaternion Algebra](the-right-regular-operators-on-the-biquaternion-algebra.html), for the second family and its matrix.
- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the third family and its criteria.
- [The Hermitian Sandwich: Definition and Multiplicativity](the-hermitian-sandwich-definition-and-multiplicativity.html), for the fourth family and its matrix.
- [Operator Family Conventions](conventions-of-the-operator-families.html), for the bracket, the units and the four letters.