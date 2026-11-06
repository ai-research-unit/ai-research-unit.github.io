# __$M_4(\mathbb{C})$ Axis-Free Representation : Operators__

## Introduction

**The question.** The axis-free article computes the left matrix $L_{\mathrm{axf}}(\tilde Q)$ and the right matrix $R_{\mathrm{axf}}(\tilde Q_2)$ of a biquaternion, their product, their trace, their determinant and their values on the six subspaces. This article asks the operator question that follows: which endomorphisms of $\mathbb{B}$ arise from multiplication, what are their matrices in the axis-free basis, and how is the matrix algebra organised by the two-sided products?

**The three answers.** The answers sit at three levels.

- A general endomorphism is any matrix in $M_4(\mathbb{C})$. The axis-free basis gives a linear isomorphism $\operatorname{End}_{\mathbb{C}}(\mathbb{B})\to M_4(\mathbb{C})$, and every $4\times4$ matrix is the matrix of exactly one operator. The space has sixteen complex dimensions, and a general operator need not be a single product.
- A one-sided operator is a left or a right multiplication. The left matrices fill the four-dimensional copy $\mathbb{B}_L=\{L_{\mathrm{axf}}(\tilde Q)\}$, and the right matrices fill the four-dimensional copy $\mathbb{B}_R=\{R_{\mathrm{axf}}(\tilde Q_2)\}$. These are the two subsets of the axis-free basis article, and their intersection is the scalars.
- A two-sided operator is a product $L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)$. The products fill a seven-dimensional cone in $M_4(\mathbb{C})$, not a subspace, and they are exactly the matrices whose coefficient matrix has rank at most one.

**The matrix side.** The sixteen products $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$ form an orthogonal basis of $M_4(\mathbb{C})$, of Hilbert–Schmidt norm two. In the axis-free basis every one of them is a real signed permutation matrix: four nonzero entries, one in each row and each column, every entry $0$, $+1$ or $-1$. The real span of the sixteen is $M_4(\mathbb{R})$, so the axis-free basis is the frame in which the real structure of the operator algebra is visible. The coefficient matrix $c(M)$ turns the product condition into a rank condition, and the cone of products into the cone over the Segre variety $\mathbb{P}^3\times\mathbb{P}^3$ in complex projective space. The article records these constructions, and closes with the open questions.

**The result in one line.** Every matrix is a sum of at most four two-sided products; the products themselves are the matrices of coefficient rank at most one; and the least number of products is the coefficient rank.

**Boundaries.** The frame and the one-sided matrices are *$M_4(\mathbb{C})$ Axis-Free Representation*. The same operators in another frame are *$M_4(\mathbb{C})$ Pauli Representation : Operators*. The abstract family is *Two-Sided Operators on the Biquaternion Algebra*. The ambient endomorphisms are *The Endomorphisms of the Biquaternion Algebra*. The enveloping algebra is *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*. The Hermitian sandwich is Part V and is not treated here.

**Conventions.** The basis is
$$
\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z),
$$
with $e_t$ the unit and
$$
\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t,\qquad
\vec e_x\vec e_y=\vec e_z,\quad
\vec e_y\vec e_z=\vec e_x,\quad
\vec e_z\vec e_x=\vec e_y,
$$
and the reverse products negated. An element is $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, with $Q_\mu\in\mathbb{C}$; write $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ for its vector part. Its coefficient column is
$$
[Q]=(Q_t,Q_x,Q_y,Q_z)^{\mathsf T}.
$$
Write $B^2=Q_x^2+Q_y^2+Q_z^2$. The quaternionic norm is
$$
\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2=Q_t^2+Q_x^2+Q_y^2+Q_z^2,
$$
the scalar part of $\tilde Q\tilde Q^{\natural}$. An element is a unit exactly when $\langle\tilde Q\rangle_{\natural}\neq0$, and then $\tilde Q^{-1}=\tilde Q^{\natural}/\langle\tilde Q\rangle_{\natural}$. The natural conjugation is the $\mathbb{C}$-linear map
$$
\tilde Q^{\natural}=Q_t-Q_x\vec e_x-Q_y\vec e_y-Q_z\vec e_z.
$$
The coefficientwise conjugation is $\bar{\tilde Q}=\bar Q_te_t+\bar Q_x\vec e_x+\bar Q_y\vec e_y+\bar Q_z\vec e_z$, and the Hermitian conjugation is
$$
\tilde Q^{*}=\bar{\tilde Q}^{\natural}
=\bar Q_t-\bar Q_x\vec e_x-\bar Q_y\vec e_y-\bar Q_z\vec e_z,
$$
which is conjugate-linear. The flat conjugation is $\tilde Q^{\flat}=-\tilde Q^{*}$. The switch matrix is
$$
D=\begin{pmatrix}1&0&0&0\\0&-1&0&0\\0&0&-1&0\\0&0&0&-1\end{pmatrix},
\qquad D^2=\mathrm I_4,\quad \det D=-1,
$$
and the plain form is
$$
\langle X,Y\rangle=\operatorname{Sc}(XY),
$$
whose Gram matrix in the axis-free basis is $\operatorname{diag}(1,-1,-1,-1)$; here $\operatorname{Sc}$ is the $e_t$ coefficient. The matrix rank is written $\operatorname{rank}$, and it is the rank over $\mathbb{C}$ unless a real field is named.

## The Three Correspondences

**The ambient space.** The algebra $\mathbb{B}$ has complex dimension four, and $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ is the algebra $M_4(\mathbb{C})$ of complex dimension sixteen. The axis-free basis $\mathcal{E}$ gives a linear isomorphism
$$
\operatorname{End}_{\mathbb{C}}(\mathbb{B})\longrightarrow M_4(\mathbb{C}),\qquad
M\longmapsto[M]_{\mathcal{E}},
$$
and it is an isomorphism of algebras. The left matrix is $L_{\mathrm{axf}}(\tilde Q)$ and the right matrix is $R_{\mathrm{axf}}(\tilde Q_2)$; the two are the matrices of the operators $X\mapsto\tilde QX$ and $X\mapsto X\tilde Q_2$.

### General Endomorphisms

**The whole space.** Every $4\times4$ matrix is the matrix of exactly one endomorphism, and every endomorphism has exactly one matrix in the axis-free basis. The level is the whole ambient space, of sixteen complex dimensions. A general matrix need not be a left multiplication, a right multiplication or a two-sided product; the product set is the subject of the rest of the article.

### The One-Sided Copies

**The left copy.** The left multiplications fill the image
$$
\mathbb{B}_L=\{L_{\mathrm{axf}}(\tilde Q):\tilde Q\in\mathbb{B}\}.
$$
It is a four-dimensional complex subalgebra of $M_4(\mathbb{C})$, isomorphic to $\mathbb{B}$, and its unit is $\mathrm I_4$. The map $\tilde Q\mapsto L_{\mathrm{axf}}(\tilde Q)$ is injective, so the four matrices $L_{\mathrm{axf},e_\mu}$ are a basis of it.

**The right copy.** The right multiplications fill
$$
\mathbb{B}_R=\{R_{\mathrm{axf}}(\tilde Q_2):\tilde Q_2\in\mathbb{B}\}.
$$
It is a four-dimensional complex subalgebra, isomorphic to the opposite algebra $\mathbb{B}_{\mathrm{opp}}$, the same vector space with the reversed product, and its unit is $\mathrm I_4$. The map $\tilde Q_2\mapsto R_{\mathrm{axf}}(\tilde Q_2)$ is injective, so the four matrices $R_{\mathrm{axf},e_\nu}$ are a basis of it.

**The two copies are different.** $\mathbb{B}_L$ and $\mathbb{B}_R$ are two different four-dimensional subspaces of $M_4(\mathbb{C})$, not two bases of one space. The axis-free basis displays them as the two families of matrices below.

### The Two-Sided Products

**The operator.** A left multiplication and a right multiplication combine into one operator,
$$
L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)(X)=\tilde QX\tilde Q_2.
$$
The two factors commute, so $L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)=R_{\mathrm{axf}}(\tilde Q_2)L_{\mathrm{axf}}(\tilde Q)$ as well. The pair $(\tilde Q,\tilde Q_2)$ has eight complex parameters, and the scaling $(\tilde Q,\tilde Q_2)\mapsto(\lambda\tilde Q,\lambda^{-1}\tilde Q_2)$ leaves the operator unchanged, so the image has seven effective parameters. The image is a cone, not a subspace. It is exactly the set of matrices whose coefficient matrix $c(M)$, the matrix of coordinates in the basis $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$, has rank at most one, by the criterion of §*The Criterion for a Single Product*.

### The Table of Levels

**The table.** The three levels and the two one-sided copies are collected in one table. The coefficient matrix $c(M)$ is the matrix of coordinates of $M$ in the sixteen-dimensional basis $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$; its formula is in §*The Coefficient Matrix $c(M)$*. The intersection of the one-sided copies is the scalar line $\mathbb{C}\cdot\mathrm I_4$, by §*The Intersection of the Two Copies*.

| Level | Operator | Subset of $M_4(\mathbb{C})$ | Complex dimension | Test |
|---|---|---|---|---|
| general endomorphism | $M$ | all of $M_4(\mathbb{C})$ | $16$ | none |
| one-sided left | $L_{\mathrm{axf}}(\tilde Q)$ | $\mathbb{B}_L$ | $4$ | the left display |
| one-sided right | $R_{\mathrm{axf}}(\tilde Q_2)$ | $\mathbb{B}_R$ | $4$ | the right display |
| intersection of the one-sided copies | $\lambda\mathrm I_4$ | the scalars | $1$ | both displays |
| two-sided | $L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)$ | $\{\operatorname{rank}c(M)\le1\}$ | $7$ (cone) | rank-one coefficient matrix |

The table is the answer to the operator question. The general level is the whole space; the one-sided levels are two linear subspaces; the two-sided level is a cone inside the whole space, of dimension seven.

## The One-Sided Operators

### The Left Copy

**The left matrix.** The left matrix is the $4\times4$ matrix whose $\mu$-th column is the coordinate column of $\tilde Qe_\mu$. In the axis-free basis,
$$
L_{\mathrm{axf}}(\tilde Q)=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&-Q_z&Q_y\\
Q_y&Q_z&Q_t&-Q_x\\
Q_z&-Q_y&Q_x&Q_t
\end{pmatrix}.
$$
The first column is $[Q]$, so the map recovers $\tilde Q$. The composition law is
$$
L_{\mathrm{axf}}(\tilde Q_1\tilde Q_2)=L_{\mathrm{axf}}(\tilde Q_1)L_{\mathrm{axf}}(\tilde Q_2),
$$
and the map is injective. The image is the four-dimensional subalgebra $\mathbb{B}_L$.

**The invariants.** The trace is $4Q_t$ and the determinant is
$$
\det L_{\mathrm{axf}}(\tilde Q)=\langle\tilde Q\rangle_{\natural}^2,
$$
with the eigenvalues $Q_t\pm iB$, each twice, where $B^2=Q_x^2+Q_y^2+Q_z^2$; see §*The Quadratic Relation*. The rank is $4$ for a unit, $2$ for a nonzero zero divisor and $0$ for the zero element; the proof is in §*The Rank of a One-Sided Operator*.

### The Four Left Matrices

**The display.** With $L_{\mathrm{axf},e_\mu}=L_{\mathrm{axf}}(e_\mu)$,
$$
L_{\mathrm{axf},e_t}=\mathrm I_4,\qquad
L_{\mathrm{axf},\vec e_x}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},
$$
$$
L_{\mathrm{axf},\vec e_y}=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
L_{\mathrm{axf},\vec e_z}=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
$$
Each is a real signed permutation matrix. Each has determinant $1$; the identity has trace $4$, and the three vector matrices have trace $0$. The four are linearly independent and span $\mathbb{B}_L$: they are a basis of the left copy.

**The products.** The left matrices follow the order of the units:
$$
(L_{\mathrm{axf},\vec e_x})^2=(L_{\mathrm{axf},\vec e_y})^2=(L_{\mathrm{axf},\vec e_z})^2=-\mathrm I_4,\qquad
L_{\mathrm{axf},\vec e_x}L_{\mathrm{axf},\vec e_y}=L_{\mathrm{axf},\vec e_z},\qquad
L_{\mathrm{axf},\vec e_y}L_{\mathrm{axf},\vec e_x}=-L_{\mathrm{axf},\vec e_z}.
$$
The set of the four matrices together with their negatives is the quaternion group of order eight. A complex linear combination need not be invertible: $L_{\mathrm{axf},\vec e_x}+iL_{\mathrm{axf},\vec e_z}$ has rank $2$, for example. The algebra is simple and has zero divisors, and the invertibility of each basis matrix does not extend to the span.

### The Right Copy

**The right matrix.** The right matrix has $\mu$-th column the coordinate column of $e_\mu\tilde Q$. In the axis-free basis,
$$
R_{\mathrm{axf}}(\tilde Q)=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&Q_z&-Q_y\\
Q_y&-Q_z&Q_t&Q_x\\
Q_z&Q_y&-Q_x&Q_t
\end{pmatrix}.
$$
The composition law is anti-multiplicative,
$$
R_{\mathrm{axf}}(\tilde Q_1\tilde Q_2)=R_{\mathrm{axf}}(\tilde Q_2)R_{\mathrm{axf}}(\tilde Q_1),
$$
and the map is injective. The image is the four-dimensional subalgebra $\mathbb{B}_R$. The right matrix commutes with every left matrix:
$$
L_{\mathrm{axf}}(\tilde Q_1)R_{\mathrm{axf}}(\tilde Q_2)=R_{\mathrm{axf}}(\tilde Q_2)L_{\mathrm{axf}}(\tilde Q_1).
$$
The invariants are the same: trace $4Q_t$, determinant $\langle\tilde Q\rangle_{\natural}^2$, eigenvalues $Q_t\pm iB$ each twice, and the same ranks.

### The Four Right Matrices

**The display.** With $R_{\mathrm{axf},e_\nu}=R_{\mathrm{axf}}(e_\nu)$,
$$
R_{\mathrm{axf},e_t}=\mathrm I_4,\qquad
R_{\mathrm{axf},\vec e_x}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},
$$
$$
R_{\mathrm{axf},\vec e_y}=\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
R_{\mathrm{axf},\vec e_z}=\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix}.
$$
Each is a real signed permutation matrix, of determinant $1$ and trace $4\delta_{\nu t}$; the four are a basis of $\mathbb{B}_R$. The right products reverse the order:
$$
(R_{\mathrm{axf},\vec e_x})^2=(R_{\mathrm{axf},\vec e_y})^2=(R_{\mathrm{axf},\vec e_z})^2=-\mathrm I_4,\qquad
R_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y}=-R_{\mathrm{axf},\vec e_z},\qquad
R_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_x}=R_{\mathrm{axf},\vec e_z}.
$$
The set of the four together with their negatives is again the quaternion group.

### The Stitch Between the Copies

**The switch matrix.** The natural conjugation acts on a coordinate column by $D$:
$$
D=\begin{pmatrix}1&0&0&0\\0&-1&0&0\\0&0&-1&0\\0&0&0&-1\end{pmatrix},
\qquad D^2=\mathrm I_4,\quad \det D=-1.
$$
Its entries are the signs of $e_\mu^{\natural}=s_\mu e_\mu$, with $s_t=1$ and $s_x=s_y=s_z=-1$. It is not an algebra map, not one of the sixteen cells and not a one-sided multiplication; it is the linear involution of the coefficient space that changes the signs of the three vector coordinates.

**The stitch.** The right matrix is obtained from the left by transposition and a sign on each side:
$$
R_{\mathrm{axf}}(\tilde Q)=D\,L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}D
=D\,L_{\mathrm{axf}}(\tilde Q^{\natural})\,D.
$$
The second form uses the transpose identity
$$
L_{\mathrm{axf}}(\tilde X)^{\mathsf T}=L_{\mathrm{axf}}(\tilde X^{\natural}).
$$
The Hermitian adjoint is
$$
L_{\mathrm{axf}}(\tilde X)^{\dagger}=L_{\mathrm{axf}}(\tilde X^{*}),
$$
and the same identities hold for $R_{\mathrm{axf}}$. The first is the transpose dictionary of the axis-free basis: natural conjugation is transposition. The second is the conjugate transpose: the dagger is the Hermitian conjugation. Both are checked on the four units and extended by linearity. At the operator level the same transposition carries the parameter through the natural conjugation, and the flip of the two mixed units conjugates the two families, $SL_{\tilde Q}S^{-1}=R_{S\tilde Q}$; both statements are proved in *The One-Sided Operators on the Biquaternion Algebra*, §*The Matrix Identity*, where the two frames are set side by side.

### The Intersection of the Two Copies

**The intersection.** A matrix that is both a left matrix and a right matrix is a scalar matrix:
$$
\mathbb{B}_L\cap\mathbb{B}_R=\mathbb{C}\cdot\mathrm I_4.
$$
*Proof.* Suppose $L_{\mathrm{axf}}(\tilde Q)=R_{\mathrm{axf}}(\tilde Q_2)$. The first column of each is the coordinate column of the element, so $\tilde Q_2=\tilde Q$. Compare the entries $(2,3)$ and $(3,2)$: the left matrix has $-Q_z$ and $Q_z$, the right matrix has $Q_z$ and $-Q_z$, so $Q_z=0$. Compare $(2,4)$ and $(4,2)$: the left matrix has $Q_y$ and $-Q_y$, the right matrix has $-Q_y$ and $Q_y$, so $Q_y=0$. Compare $(3,4)$ and $(4,3)$: the left matrix has $-Q_x$ and $Q_x$, the right matrix has $Q_x$ and $-Q_x$, so $Q_x=0$. Hence $\tilde Q=Q_te_t$ and the matrix is $Q_t\mathrm I_4$. The converse is immediate.

**The mutual commutants.** The left copy is the commutant of the right copy, and the right copy is the commutant of the left copy. The inclusion $\mathbb{B}_L\subseteq\mathbb{B}_R'$ is the commutation law. The reverse inclusion is the double commutant theorem: the commutant of $\mathbb{B}_L$ is four-dimensional and contains $\mathbb{B}_R$, so the two coincide. The intersection is the centre of each copy.

## The Sixteen Matrices $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$

### The Table in Four Families

**Definition.** For $\mu,\nu\in\{t,x,y,z\}$ put
$$
L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu},\qquad
L_{\mathrm{axf},e_\mu}=L_{\mathrm{axf}}(e_\mu),\qquad
R_{\mathrm{axf},e_\nu}=R_{\mathrm{axf}}(e_\nu).
$$
The matrix $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$ is the matrix of $X\mapsto e_\mu Xe_\nu$. A general two-sided operator is the linear combination
$$
L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)=\sum_{\mu,\nu}Q_\mu P_\nu\,L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}.
$$

**The table.** The sixteen matrices fall into four families.

| $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}=\mathrm I_4$ | $L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x}=R_{\mathrm{axf},\vec e_x}$ | $L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_y}=R_{\mathrm{axf},\vec e_y}$ | $L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z}=R_{\mathrm{axf},\vec e_z}$ |
| $\vec e_x$ | $L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},e_t}=L_{\mathrm{axf},\vec e_x}$ | $L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_x}$ | $L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y}$ | $L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_z}$ |
| $\vec e_y$ | $L_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},e_t}=L_{\mathrm{axf},\vec e_y}$ | $L_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_x}$ | $L_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}$ | $L_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_z}$ |
| $\vec e_z$ | $L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},e_t}=L_{\mathrm{axf},\vec e_z}$ | $L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_x}$ | $L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}$ | $L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_z}$ |

Each row is labelled by its left unit and each column by its right unit, so each entry is the product of the two labels, left factor first. The first row is the right family, the first column the left family, the diagonal entry $L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}$ the identity, and the remaining nine the genuinely two-sided cells. The table is the matrix form of the four families of *Two-Sided Operators on the Biquaternion Algebra*, §*The Operator $L_{\tilde Q}R_{\tilde Q_2}$*.

### The Sixteen, Entry by Entry

**The display.** In the axis-free basis, grouped by the left index $\mu$,
$$
L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},
$$
$$
L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_y}=\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z}=\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix},
$$
$$
L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},e_t}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_x}=\begin{pmatrix}-1&0&0&0\\0&-1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},
$$
$$
L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y}=\begin{pmatrix}0&0&0&1\\0&0&-1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix},\qquad
L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_z}=\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\-1&0&0&0\\0&-1&0&0\end{pmatrix},
$$
$$
L_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},e_t}=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
L_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_x}=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix},
$$
$$
L_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\0&0&-1&0\\0&0&0&1\end{pmatrix},\qquad
L_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_z}=\begin{pmatrix}0&1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&-1&0\end{pmatrix},
$$
$$
L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},e_t}=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix},\qquad
L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_x}=\begin{pmatrix}0&0&1&0\\0&0&0&-1\\1&0&0&0\\0&-1&0&0\end{pmatrix},
$$
$$
L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}=\begin{pmatrix}0&-1&0&0\\-1&0&0&0\\0&0&0&-1\\0&0&-1&0\end{pmatrix},\qquad
L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_z}=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&-1\end{pmatrix}.
$$

**The pattern.** Each matrix has four nonzero entries, one in each row and each column, and every nonzero entry is $\pm1$. No entry is imaginary: the axis-free basis makes the sixteen products real. The first row and the first column are the four right and the four left matrices; the nine remaining entries are the genuinely two-sided cells. A cell with exactly one index equal to $t$ is skew-symmetric; a cell with both indices equal to $t$ or with neither equal to $t$ is symmetric. The display is the matrix form of the sixteen products $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$ of *Matrix Representations Conventions*, §*The 4×4 Regular Representation*, read in the axis-free basis.

**One entry.** The table gives, for example,
$$
L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y}=
\begin{pmatrix}
0&0&0&1\\
0&0&-1&0\\
0&-1&0&0\\
1&0&0&0
\end{pmatrix}.
$$
The first column is the coordinate column of $\vec e_x\vec e_y=\vec e_z$, and the entry is the check that the family rule and the multiplication table agree.

**The basis.** The sixteen matrices are linearly independent and span $M_4(\mathbb{C})$, by the orthogonality theorem of §*Orthogonality* and the dimension count. The span of the products is the whole algebra: the generation theorem of *Two-Sided Operators on the Biquaternion Algebra*, §*The Sixteen Products as a Basis*, read in the axis-free basis. The expansion of a general matrix in this basis is unique, and the coefficient matrix is the subject of §*The Cone of Products*.

**The real basis.** All sixteen matrices are real. They are linearly independent over $\mathbb{C}$, hence over $\mathbb{R}$, and their real span is a sixteen-real-dimensional subspace of $M_4(\mathbb{C})$ consisting of real matrices. That subspace is $M_4(\mathbb{R})$. The axis-free basis is therefore the frame in which the real form of the operator algebra is the real span of the products.

### Composition, Trace, Determinant

**Composition.** The product of two basis matrices is a signed basis matrix:
$$
L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}L_{\mathrm{axf},e_\rho}R_{\mathrm{axf},e_\sigma}
=\varepsilon\varepsilon'\,L_{\mathrm{axf},e_{\mu'}}R_{\mathrm{axf},e_{\nu'}},
$$
where $e_\mu e_\rho=\varepsilon e_{\mu'}$ and $e_\sigma e_\nu=\varepsilon' e_{\nu'}$, with $\varepsilon,\varepsilon'\in\{\pm1\}$. For general parameters,
$$
L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)L_{\mathrm{axf}}(\tilde Q_3)R_{\mathrm{axf}}(\tilde Q_4)
=L_{\mathrm{axf}}(\tilde Q\tilde Q_3)R_{\mathrm{axf}}(\ \tilde Q_4\tilde Q_2).
$$
The sixteen are closed under multiplication up to sign, with unit $L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}=\mathrm I_4$; they are not a group, because $-L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$ is not one of the sixteen. The full product family contains the signs, since $-L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}=L_{\mathrm{axf},-\tilde e_\mu}R_{\mathrm{axf},\tilde e_\nu}$.

**Trace and determinant.** For $\tilde Q,\tilde Q_2$ with $\langle\tilde Q\rangle_{\natural}\langle\tilde Q_2\rangle_{\natural}\neq0$,
$$
\operatorname{Tr}L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)=4\,Q_tP_t,\qquad
\det L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)
=\langle\tilde Q\rangle_{\natural}^{2}\langle\tilde Q_2\rangle_{\natural}^{2},
\qquad
\bigl(L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)\bigr)^{-1}
=L_{\mathrm{axf}}(\tilde Q^{-1})R_{\mathrm{axf}}(\tilde Q_2^{-1}).
$$
*Proof.* The trace is bilinear in the pair, and only $L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}$ has nonzero trace, equal to $4$; hence the trace is $4Q_tP_t$. The determinant is multiplicative, and $\det L_{\mathrm{axf}}(\tilde Q)=\langle\tilde Q\rangle_{\natural}^2$ and $\det R_{\mathrm{axf}}(\tilde Q_2)=\langle\tilde Q_2\rangle_{\natural}^2$. The inverse is the inverse of each factor.

**The basis values.** Every basis matrix is invertible, of determinant $1$ and rank $4$; the trace is $4$ only for $L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}$ and $0$ for the other fifteen. The basis consists of units, but its span does not: for example
$$
L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}+L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_x}
=\mathrm I_4+L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_x}
=\operatorname{diag}(0,0,2,2)
$$
has rank two. A basis of invertible matrices does not make the algebra a division algebra; the algebra is $M_4(\mathbb{C})$ and has many zero divisors.

### Orthogonality

**Theorem (orthogonality).** For the Hilbert–Schmidt inner product $\langle A,B\rangle_{\mathrm{HS}}=\operatorname{Tr}(A^{\dagger}B)$,
$$
\operatorname{Tr}\bigl((L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu})^{\dagger}L_{\mathrm{axf},e_\rho}R_{\mathrm{axf},e_\sigma}\bigr)
=4\,\delta_{\mu\rho}\,\delta_{\nu\sigma}.
$$
The sixteen basis matrices are orthogonal, each of Hilbert–Schmidt norm $2$. Because the matrices are real, the dagger is the transpose.

*Proof.* Transposition reverses the two indices through the inverse units:
$$
(L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu})^{\mathsf T}=L_{\mathrm{axf},e_{\mu^{-1}}}R_{\mathrm{axf},e_{\nu^{-1}}},
$$
where $e_\mu^{-1}=e_t$ for $\mu=t$ and $e_\mu^{-1}=-e_\mu$ for $\mu=x,y,z$. The composition law then gives
$$
(L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu})^{\mathsf T}L_{\mathrm{axf},e_\rho}R_{\mathrm{axf},e_\sigma}
=L_{\mathrm{axf},e_{\mu^{-1}}}R_{\mathrm{axf},e_{\nu^{-1}}}L_{\mathrm{axf},e_\rho}R_{\mathrm{axf},e_\sigma}
=\varepsilon\varepsilon'\,L_{\mathrm{axf},e_{\mu'}}R_{\mathrm{axf},e_{\nu'}},
$$
The trace of $L_{\mathrm{axf},e_{\mu'}}R_{\mathrm{axf},e_{\nu'}}$ is $4$ exactly when $\mu'=\nu'=t$ and $0$ otherwise. The condition $\mu^{-1}\rho=t$ is $\rho=\mu$, and the condition $\sigma\nu^{-1}=t$ is $\sigma=\nu$; in that case the two signs are $+1$. Hence the inner product is $4$ exactly when $\mu=\rho$ and $\nu=\sigma$, and $0$ otherwise.

**The coefficient formula.** If $M=\sum c_{\mu\nu}L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$, then orthogonality gives
$$
c_{\mu\nu}=\tfrac14\operatorname{Tr}\bigl((L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu})^{\mathsf T}M\bigr).
$$
The map $M\mapsto c(M)$ is a linear isomorphism of $M_4(\mathbb{C})$ onto itself. It is the coordinate chart used in §*The Cone of Products*.

**No change of frame is needed.** In the axis-free basis the coefficient matrix is computed from the matrix $M$ by the sixteen traces above, with no conjugation and no change-of-frame matrix. The sixteen cells are real, so for a real matrix $M$ the coefficient matrix is real and its rank is the same over $\mathbb{R}$ and over $\mathbb{C}$.

## The Rank of a One-Sided Operator

### The Quadratic Relation

**The relation.** Write $\tilde Q=Q_te_t+\vec Q$, with $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. Since $\vec Q^2=-B^2e_t$,
$$
\tilde Q^2=(Q_t^2-B^2)e_t+2Q_t\vec Q,
$$
and therefore
$$
\tilde Q^2-2Q_t\tilde Q+\langle\tilde Q\rangle_{\natural}e_t=0.
$$
Applying $L_{\mathrm{axf}}$ gives
$$
(L_{\mathrm{axf}}(\tilde Q))^2-2Q_tL_{\mathrm{axf}}(\tilde Q)
+\langle\tilde Q\rangle_{\natural}\mathrm I_4=0,
$$
and the same relation holds for $R_{\mathrm{axf}}(\tilde Q)$.

**The eigenvalues and the determinant.** Every eigenvalue $\lambda$ satisfies $\lambda^2-2Q_t\lambda+\langle\tilde Q\rangle_{\natural}=0$, so $\lambda=Q_t\pm iB$. The trace is $4Q_t$. When $B\neq0$ the two roots are distinct, and the trace forces multiplicity two for each; when $B=0$ the only root is $Q_t$. In both cases the characteristic polynomial is
$$
\bigl((\lambda-Q_t)^2+B^2\bigr)^2,
$$
and the determinant is $\langle\tilde Q\rangle_{\natural}^2$. The same holds for $R_{\mathrm{axf}}(\tilde Q)$.

### The Rank of $L_{\mathrm{axf}}$ and $R_{\mathrm{axf}}$

**The form.** The bilinear form
$$
\beta(X,Y)=\operatorname{Sc}(XY^{\natural})
$$
has $\beta(X,X)=\langle X\rangle_{\natural}$ and Gram matrix $\mathrm I_4$ in the axis-free basis. It is the polar form of the norm, not the plain form $\operatorname{Sc}(XY)$ of §*The Plain Form*; it is symmetric and nondegenerate over $\mathbb{C}$. A linear subspace on which $\beta$ vanishes identically is totally isotropic; in a nondegenerate four-dimensional space over $\mathbb{C}$ such a subspace has dimension at most two.

**The theorem.** The rank of $L_{\mathrm{axf}}(\tilde Q)$ is $4$ when $\langle\tilde Q\rangle_{\natural}\neq0$, it is $2$ when $\tilde Q\neq0$ and $\langle\tilde Q\rangle_{\natural}=0$, and it is $0$ when $\tilde Q=0$. The same values hold for $R_{\mathrm{axf}}(\tilde Q)$.

*Proof.* If $\langle\tilde Q\rangle_{\natural}\neq0$, the determinant is $\langle\tilde Q\rangle_{\natural}^2\neq0$ and the rank is $4$. If $\tilde Q=0$, the matrix is zero. Suppose $\tilde Q\neq0$ and $\langle\tilde Q\rangle_{\natural}=0$.

Let $X$ lie in the kernel of $L_{\mathrm{axf}}(\tilde Q)$, so that $\tilde QX=0$. If $X$ were a unit, then $\tilde Q=(\tilde QX)X^{-1}=0$, against the hypothesis; hence $X$ is not a unit and $\langle X\rangle_{\natural}=0$. The kernel is therefore a linear subspace of the null cone, hence totally isotropic for $\beta$, of dimension at most two. This gives $\operatorname{rank}L_{\mathrm{axf}}(\tilde Q)\ge2$.

For the other bound, split on $Q_t$. If $Q_t\neq0$, the relation reads $L(L-2Q_t\mathrm I_4)=0$, so the minimal polynomial divides $\lambda(\lambda-2Q_t)$, whose roots are distinct; the matrix is diagonalizable with eigenvalues $0$ and $2Q_t$. The trace is $4Q_t$, so $2Q_t$ has multiplicity two and $0$ has multiplicity two; the rank is $2$. If $Q_t=0$, the relation reads $L^2=0$, so the image lies in the kernel and $\operatorname{rank}L\le4-\operatorname{rank}L$, hence the rank is at most two. With the lower bound, the rank is two.

The argument for $R_{\mathrm{axf}}$ is the same, with the kernel read on the other side.

### The Rank of a Product

**The bound.** For every pair,
$$
\operatorname{rank}L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)
\le\min\bigl(\operatorname{rank}L_{\mathrm{axf}}(\tilde Q),
\operatorname{rank}R_{\mathrm{axf}}(\tilde Q_2)\bigr).
$$
If one parameter is a unit, the bound is attained, and the rank of the product is the rank of the other one-sided factor. Hence a product is invertible exactly when both parameters are units.

*Proof.* The operator is the composite $L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)$; the rank of a composite is at most the rank of either factor. A unit $\tilde Q_2$ makes $R_{\mathrm{axf}}(\tilde Q_2)$ invertible, so $\operatorname{rank}(L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2))=\operatorname{rank}L_{\mathrm{axf}}(\tilde Q)$; a unit $\tilde Q$ does the same on the other side.

**The possible ranks.** The one-sided ranks are $0$, $2$ and $4$. If a parameter is zero the product is zero. If both parameters are nonzero zero divisors, the product has rank at most two. If both are units, the product is invertible of rank four. Hence a product has rank $0$, $1$, $2$ or $4$, and never rank three.

**The drop.** For $\tilde Q=\tilde Q_2=e_t+i\vec e_z$,
$$
L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)
=2\begin{pmatrix}
1&0&0&-i\\
0&0&0&0\\
0&0&0&0\\
i&0&0&1
\end{pmatrix},
$$
of rank one, while each one-sided factor has rank two.

## The Ordinary Product

**The dimensions.** The matrix of the composite is the ordinary $4\times4$ product $L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)$. The Kronecker product $L_{\mathrm{axf}}(\tilde Q)\otimes R_{\mathrm{axf}}(\tilde Q_2)$ is a $16\times16$ matrix acting on the tensor square of the carrier, a space of dimension sixteen; it is the matrix of the tensor product of the two operators, not of their composite on the four-dimensional algebra.

## The Cone of Products

**The product set.** The image of the factorisation map of §*The Factorization Map* is the set of two-sided operators. It is a cone, not a subspace, and its coordinate description is the subject of this section. The coordinate chart is the coefficient matrix of §*The Coefficient Matrix $c(M)$*, and it turns the product condition into a rank condition.

### The Coefficient Matrix $c(M)$

**Definition.** By §*Orthogonality*, every $M\in M_4(\mathbb{C})$ has a unique expansion
$$
M=\sum_{\mu,\nu}c_{\mu\nu}L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}.
$$
The $4\times4$ matrix $c(M)=(c_{\mu\nu})$ is the **coefficient matrix** of $M$. Orthogonality gives it directly:
$$
c(M)_{\mu\nu}
=\tfrac14\operatorname{Tr}\bigl((L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu})^{\mathsf T}M\bigr).
$$
The map $M\mapsto c(M)$ is a linear isomorphism of $M_4(\mathbb{C})$ onto itself.

**The coefficient column.** For $\tilde Q\in\mathbb{B}$ write $[Q]=(Q_t,Q_x,Q_y,Q_z)^{\mathsf T}$ for the column of its coefficients in the axis-free basis.

**The expansion of a product.** If $M=L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)$, then
$$
M=\sum_{\mu,\nu}Q_\mu P_\nu\,L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu},
$$
so $c(M)=[Q][P]^{\mathsf T}$. The coefficient matrix of a product is a rank-one matrix, and every rank-one matrix arises this way. This is the source of the criterion of §*The Criterion for a Single Product*.

**The coefficient matrix is not the matrix.** The notation is easy to confuse and the two objects must be kept apart. The matrix $M$ is the $4\times4$ matrix of an endomorphism in the axis-free basis; the coefficient matrix $c(M)$ is the $4\times4$ array of its coordinates in the sixteen-dimensional basis $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$. The map $c$ is linear and bijective, not an algebra map.

### The Factorization Map

**The map.** The assignment
$$
\Phi:\mathbb{B}\times\mathbb{B}\longrightarrow\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\qquad
\Phi(\tilde Q,\tilde Q_2)=L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)
$$
is the factorisation map. Its image is the set of two-sided operators, and this section records what the factorisation does and does not imply.

**Bilinearity.** The map is complex-bilinear, not complex-linear:
$$
L_{\mathrm{axf}}(a\tilde Q+b\tilde Q')R_{\mathrm{axf}}(\tilde Q_2)
=aT_{\mathrm{axf},\tilde Q,\tilde Q_2}+bT_{\mathrm{axf},\tilde Q',\tilde Q_2},\qquad
L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(a\tilde Q_2+b\tilde Q_2')
=aT_{\mathrm{axf},\tilde Q,\tilde Q_2}+bT_{\mathrm{axf},\tilde Q,\tilde Q_2'}.
$$
Consequently the image is a cone, not a subspace: for $\lambda\in\mathbb{C}$,
$$
\lambda L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)
=L_{\mathrm{axf}}(\lambda\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)
=L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\lambda\tilde Q_2).
$$

**The scaling orbit.** For $\lambda\in\mathbb{C}^{\times}$,
$$
L_{\mathrm{axf}}(\lambda\tilde Q)R_{\mathrm{axf}}(\lambda^{-1}\tilde Q_2)
=L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2).
$$
The group $\mathbb{C}^{\times}$ acts on $\mathbb{B}\times\mathbb{B}$ by $(\tilde Q,\tilde Q_2)\mapsto(\lambda\tilde Q,\lambda^{-1}\tilde Q_2)$, and the factorisation map is constant on every orbit.

**The zero set.** The product vanishes exactly when one parameter vanishes:
$$
L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)=0
\iff \tilde Q=0\ \text{or}\ \tilde Q_2=0.
$$
*Proof.* The coefficient matrix of the product is $[Q][P]^{\mathsf T}$, by §*The Coefficient Matrix $c(M)$*; it is zero exactly when one of the two columns is zero, and $c$ is injective.

**The two slots.** With the other parameter a unit, the map is injective in each slot:
$$
L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(e_t)=L_{\mathrm{axf}}(\tilde Q),\qquad
L_{\mathrm{axf}}(e_t)R_{\mathrm{axf}}(\tilde Q_2)=R_{\mathrm{axf}}(\tilde Q_2).
$$
The first is the left copy, the second the right copy, and both parametrisations are injective.

**The fibres.** For a nonzero product the fibre of the factorisation map is exactly one scaling orbit:
$$
L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)=L_{\mathrm{axf}}(\tilde Q_3)R_{\mathrm{axf}}(\tilde Q_4)
\iff
\tilde Q_3=\lambda\tilde Q,\quad
\tilde Q_4=\lambda^{-1}\tilde Q_2
\quad\text{for some }\lambda\in\mathbb{C}^{\times}.
$$
*Proof.* The coefficient matrices are equal, $[Q][P]^{\mathsf T}=[R][S]^{\mathsf T}$, and both are nonzero of rank one. A nonzero column of the left side is a nonzero scalar multiple of a nonzero column of the right side, which gives $[R]=\lambda[Q]$; comparing the rows gives $[S]=\lambda^{-1}[P]$. The converse is the scaling identity.

**The dimension.** The parameter space has complex dimension eight. The generic fibre has complex dimension one, so the image has complex dimension
$$
8-1=7.
$$
The zero operator is the vertex, where the two four-dimensional subspaces $\tilde Q=0$ and $\tilde Q_2=0$ collapse. The image is the seven-dimensional cone of the next subsections.

### The Length $\ell(M)=\operatorname{rank}c(M)$

**Definition.** The **length** $\ell(M)$ is the least $r\ge0$ such that $M$ is a sum of $r$ products; $\ell(0)=0$.

**Theorem (length is the rank).** For every $M\in M_4(\mathbb{C})$,
$$
\ell(M)=\operatorname{rank}c(M).
$$

*Proof.* If $M=\sum_{i\le r}L_{\mathrm{axf}}(\tilde Q_i)R_{\mathrm{axf}}(\tilde Q_2_i)$, then $c(M)=\sum_{i\le r}[Q_i][P_i]^{\mathsf T}$ is a sum of $r$ rank-one matrices, so $\operatorname{rank}c(M)\le r$ and $\ell(M)\ge\operatorname{rank}c(M)$. Conversely, let $\operatorname{rank}c=r$ and factor $c=UV$ with $U$ of size $4\times r$ and $V$ of size $r\times4$; the $i$-th column of $U$ is $[Q_i]$ and the $i$-th row of $V$ is $[P_i]^{\mathsf T}$, so $M=\sum_{i\le r}L_{\mathrm{axf}}(\tilde Q_i)R_{\mathrm{axf}}(\tilde Q_2_i)$ and $\ell(M)\le r$.

**The count.** Every matrix is a sum of at most four products; $\ell(M)=4$ exactly when $\det c(M)\neq0$. The condition $\det c(M)\neq0$ is open and dense, so a generic matrix needs four products and none needs five.

### The Criterion for a Single Product

**Theorem (the product criterion).** Let $M\in M_4(\mathbb{C})$ and $c=c(M)$. Then
$$
M=L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)\ \text{for some }\tilde Q,\tilde Q_2
\iff c=[Q][P]^{\mathsf T}
\iff \operatorname{rank}c\le1.
$$
For $M\neq0$ the rank is exactly one; the zero matrix has $c=0$ and rank zero.

*Proof.* The first equivalence is §*The Coefficient Matrix $c(M)$*. The second is the rank-one criterion: a matrix is $[Q][P]^{\mathsf T}$ exactly when it has rank at most one, and the zero matrix is the case $Q=0$ or $P=0$.

**The cone.** The product set is the closed algebraic cone $\{M:\operatorname{rank}c(M)\le1\}$, cut out by the minors of order two of $c(M)$. Its projectivisation is the Segre variety $\mathbb{P}^3\times\mathbb{P}^3$, of complex dimension six; the cone has complex dimension seven in the complex sixteen-dimensional algebra. It is closed under multiplication and under inverses on its invertible part, and it is not a subspace: $L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}+L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_x}$ is not a product, because its coefficient matrix is $\operatorname{diag}(1,1,0,0)$ of rank two.

**The parametrisation.** The map $(\tilde Q,\tilde Q_2)\mapsto L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)$ is bilinear and surjective onto the cone. Its fibre over a nonzero product is the scaling orbit $(\lambda\tilde Q,\lambda^{-1}\tilde Q_2)$ of §*The Factorization Map*; the cone has complex dimension $8-1=7$. The kernel and the image of the Hermitian sandwich are a different question, treated in Part V.

### Matrix Rank Against Length

**The two ranks.** The matrix rank and the length are different invariants of the same matrix. The matrix rank of a product lies in $\{0,1,2,4\}$ by §*The Rank of a Product*, and it is four exactly when both parameters are units. The length is the coefficient rank, which can be four while the matrix rank is one. Neither invariant determines the other.

**The examples.** The matrix unit $E_{11}$ has matrix rank one and coefficient rank four; the product $L_{\mathrm{axf}}(e_t+\vec e_x)R_{\mathrm{axf}}(e_t+\vec e_y)$ has matrix rank four and coefficient rank one; the product $L_{\mathrm{axf}}(e_t+i\vec e_z)R_{\mathrm{axf}}(e_t+i\vec e_z)$ has matrix rank one and coefficient rank one; the matrix $L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}+L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_x}$ has matrix rank two and coefficient rank two.

| $M$ | $\operatorname{rank}M$ | $\operatorname{rank}c(M)$ | $\ell(M)$ | decomposition |
|---|---|---|---|---|
| $L_{\mathrm{axf}}(e_t+\vec e_x)R_{\mathrm{axf}}(e_t+\vec e_y)$ | $4$ | $1$ | $1$ | by construction |
| $L_{\mathrm{axf}}(e_t+i\vec e_z)R_{\mathrm{axf}}(e_t+i\vec e_z)$ | $1$ | $1$ | $1$ | by construction |
| $R_{\mathrm{axf}}(e_t+i\vec e_z)$ | $2$ | $1$ | $1$ | $L_{\mathrm{axf}}(e_t)R_{\mathrm{axf}}(e_t+i\vec e_z)$ |
| $L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}+L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_x}$ | $2$ | $2$ | $2$ | $L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}+L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_x}$ |
| $E_{11}$ | $1$ | $4$ | $4$ | $\tfrac14(L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}-L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_x}-L_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}-L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_z})$ |
| generic $M$ | $4$ | $4$ | $4$ | four terms, none removable |

**How to decide.** Compute the sixteen numbers $\tfrac14\operatorname{Tr}((L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu})^{\mathsf T}M)$ and form $c$. If $\operatorname{rank}c=1$, take $[Q]$ to be a nonzero column of $c$; choose a nonzero entry $Q_i$ of that column and take $[P]^{\mathsf T}$ to be the $i$-th row of $c$ divided by $Q_i$. If $\operatorname{rank}c=r>1$, a rank factorization $c=UV$ gives the $r$ terms. No test on $\operatorname{rank}M$ alone decides the question.

### The Two One-Sided Boundaries

**The two boundary cases.** The left and right copies are the two boundary cases of the cone:
$$
L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(e_t)=L_{\mathrm{axf}}(\tilde Q),\qquad
L_{\mathrm{axf}}(e_t)R_{\mathrm{axf}}(\tilde Q_2)=R_{\mathrm{axf}}(\tilde Q_2).
$$
Both are single products, and both are contained in the cone. Their intersection is the scalars $\mathbb{C}\cdot\mathrm I_4$, by §*The Intersection of the Two Copies*.

**The cone is larger.** A generic pair has neither parameter a scalar multiple of $e_t$, and its operator is neither a left nor a right multiplication. The cone is strictly larger than the union of the two copies. The two copies are four-dimensional linear subspaces inside the seven-dimensional cone, and the cone itself is not a subspace.

**The Hermitian subcone.** The Hermitian sandwich is the subcone $\tilde Q_2=\tilde Q^{*}$, a real seven-dimensional cone inside the complex seven-dimensional cone. It is the subject of Part V and is not developed here.

### A Worked Case: The Matrix Unit $E_{11}$

**The matrix.** Let $E_{11}$ be the first matrix unit in the axis-free basis, the matrix with $1$ in the $(1,1)$ entry and $0$ elsewhere. Its coefficient matrix is
$$
c(E_{11})=\frac14
\begin{pmatrix}
1&0&0&0\\
0&-1&0&0\\
0&0&-1&0\\
0&0&0&-1
\end{pmatrix}
=\frac14 D.
$$
It has rank four, so $E_{11}$ is not a single product. The expansion is
$$
E_{11}=\frac14\bigl(L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}-L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_x}-L_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}-L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_z}\bigr),
$$
which is a sum of four products. The four coefficient terms are the four diagonal entries of $c(E_{11})$, and no sum of fewer than four rank-one matrices can produce $c(E_{11})$.

**The check.** The right side is
$$
\frac14\Bigl(\mathrm I_4-\operatorname{diag}(-1,-1,1,1)
-\operatorname{diag}(-1,1,-1,1)
-\operatorname{diag}(-1,1,1,-1)\Bigr)
=\operatorname{diag}(1,0,0,0)=E_{11}.
$$
The matrix rank of $E_{11}$ is one, and its length is four.

**The reading.** $E_{11}$ is the projection $X\mapsto\operatorname{Sc}(X)e_t$: it keeps the scalar coordinate and discards the three vector coordinates. It has matrix rank one, trace one, and determinant zero. It is not a single product, because a single product has coefficient rank at most one, and $c(E_{11})$ has rank four. The example shows that the matrix rank and the length are independent: rank one can have length four.

**A single product for contrast.** The product
$$
L_{\mathrm{axf}}(e_t+\vec e_x)R_{\mathrm{axf}}(\ e_t+\vec e_y)
=L_{\mathrm{axf}}(e_t+\vec e_x)R_{\mathrm{axf}}(e_t+\vec e_y)
=
\begin{pmatrix}
1&-1&-1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&1&1&1
\end{pmatrix}
$$
has matrix rank four and coefficient matrix
$$
c=\begin{pmatrix}1\\1\\0\\0\end{pmatrix}
\begin{pmatrix}1&0&1&0\end{pmatrix}
=\begin{pmatrix}
1&0&1&0\\
1&0&1&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix},
$$
of rank one. It is a unit of determinant $16$ and length one. The two examples together show that neither matrix rank nor determinant decides the length.

**Where the frame question is answered.** The coefficient array $c(M)$ is computed from the sixteen products of four *basis elements*, so its entries move with the frame while its rank does not: a change of the element basis sends $c$ to $C^{-1}cC^{-\mathsf T}$, and a change of the display alone leaves $c$ untouched. The proof, the two frames of the corpus and the sixteen lengths of the matrix units are §*The Change of Frame Is a Congruence* and §*The Sixteen Lengths* of *$M_4(\mathbb{C})$ Pauli Representation : Operators*. What the length theorem needs from that is one line: the rank of a congruence is the rank of the array.

## The Plain Adjoint and the Types

### The Plain Form

**The form.** On $\mathbb{B}$ use the plain bilinear form
$$
\langle X,Y\rangle=\operatorname{Sc}(XY).
$$
Its Gram matrix in the axis-free basis is $\operatorname{diag}(1,-1,-1,-1)$, and the form is non-degenerate and symmetric. It is not positive definite, and it is not the Hilbert–Schmidt form on the matrix model.

### The Adjoint

**The adjoint.** The adjoint of a two-sided operator is the swap of the two parameters:
$$
\bigl(L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)\bigr)^{\approx}
=L_{\mathrm{axf}}(\tilde Q_2)R_{\mathrm{axf}}(\tilde Q).
$$
The proof is the cyclicity of the scalar part:
$$
\bigl\langle L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)X,Y\bigr\rangle
=\operatorname{Sc}(\tilde QX\tilde Q_2Y)
=\operatorname{Sc}(X\tilde Q_2Y\tilde Q)
=\bigl\langle X,L_{\mathrm{axf}}(\tilde Q_2)R_{\mathrm{axf}}(\tilde Q)Y\bigr\rangle.
$$
The adjoint exchanges the two slots and conjugates neither parameter.

### The Self-Adjoint Pairs

**The criterion.** For $\tilde Q\neq0$,
$$
\bigl(L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)\bigr)^{\approx}
=L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)
\iff
\tilde Q_2=\lambda\tilde Q
\quad\text{for some }\lambda\in\mathbb{C}.
$$
The self-adjoint two-sided operators are the scalar multiples of the diagonal operators $L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q)$, together with the zero operator. The proof is the fibre theorem of §*The Factorization Map*: equality of the two products gives $(\tilde Q_2,\tilde Q)=\lambda(\tilde Q,\tilde Q_2)$, hence $\tilde Q_2=\lambda\tilde Q$. The argument uses no inverse and covers the zero divisors.

### The Skew Sector

**No nonzero skew-adjoint.** No nonzero two-sided operator is skew-adjoint:
$$
\bigl(L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)\bigr)^{\approx}
=-L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)
\iff
L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)=0.
$$
*Proof.* If the operator is nonzero, its coefficient matrix is $[Q][P]^{\mathsf T}$ of rank one, and the coefficient matrix of its negative adjoint is $-[P][Q]^{\mathsf T}$. Equality of two nonzero rank-one matrices gives $[P]=\mu[Q]$, and then $\mu[Q][Q]^{\mathsf T}=-\mu[Q][Q]^{\mathsf T}$, so $\mu=0$, a contradiction. Hence the operator is zero.

### The Isometries

**The criterion.** The operator preserves the plain form,
$$
\bigl\langle L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)X,L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)Y\bigr\rangle
=\langle X,Y\rangle
\quad\text{for all }X,Y,
$$
exactly when
$$
\tilde Q_2\tilde Q=\pm e_t.
$$
Then $\tilde Q$ is a unit and $\tilde Q_2=\pm\tilde Q^{-1}$, and the operator is $\pm\mathrm{Ad}_{\tilde Q}$, where $\mathrm{Ad}_{\tilde Q}(X)=\tilde QX\tilde Q^{-1}$ is the inner automorphism. The isometry group is
$$
\{\pm\mathrm{Ad}_{\tilde Q}\}
\cong\bigl(\mathbb{B}^{\times}/\mathbb{C}^{\times}\bigr)\times\{\pm1\},
$$
of complex dimension three, where $\mathbb{B}^{\times}$ is the group of units. It is not the full orthogonal group, which has dimension six.

*Proof.* An isometry of a non-degenerate form on a finite-dimensional space is injective: if $FX=0$, then $\langle X,Y\rangle=\langle FX,FY\rangle=0$ for all $Y$, so $X=0$ by non-degeneracy. Hence it is invertible, and the isometry condition is equivalent to $F^{\approx}F=\mathrm I$. With $F=L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)$ and $F^{\approx}=L_{\mathrm{axf}}(\tilde Q_2)R_{\mathrm{axf}}(\tilde Q)$,
$$
F^{\approx}F
=L_{\mathrm{axf}}(\tilde Q_2\tilde Q)R_{\mathrm{axf}}(\ \tilde Q_2\tilde Q).
$$
The identity is $L_{\mathrm{axf}}(e_t)R_{\mathrm{axf}}(e_t)$. The fibre theorem gives $\tilde Q_2\tilde Q=\lambda e_t$ in both slots; then $F^{\approx}F=\lambda^2\mathrm I$, so $\lambda^2=1$. Hence $\tilde Q_2\tilde Q=\pm e_t$. The converse is immediate. The dimension is the dimension of the unit group modulo the central scalars, four minus one; the two signs are discrete.

### The Multiplicative Members

**The criterion.** A nonzero operator $L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)$ is multiplicative,
$$
L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)(XY)
=L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)(X)L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)(Y)
\quad\text{for all }X,Y,
$$
exactly when
$$
\tilde Q_2\tilde Q=e_t.
$$
Then $\tilde Q_2=\tilde Q^{-1}$ and $L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)=\mathrm{Ad}_{\tilde Q}$, an automorphism of the algebra. The zero operator is multiplicative but is excluded by the nonzero condition.

*Proof.* The condition is
$$
\tilde QX\bigl(e_t-\tilde Q_2\tilde Q\bigr)Y\tilde Q_2=0
\quad\text{for all }X,Y.
$$
Put $\tilde Q_3=e_t-\tilde Q_2\tilde Q$. If $\tilde Q_3\neq0$, the products $X\tilde Q_3Y$ span the two-sided ideal generated by $\tilde Q_3$, which is the whole algebra because $\mathbb{B}$ is simple. Then $\tilde Q\tilde Z\tilde Q_2=0$ for all $\tilde Z$. The map $(\tilde Q,\tilde Q_2)\mapsto L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)$ is bilinear and sends the sixteen basis pairs to the basis $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$, so it is injective: $L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)=0$ forces $\tilde Q=0$ or $\tilde Q_2=0$, against the nonzero hypothesis. Hence $\tilde Q_3=0$ and $\tilde Q_2\tilde Q=e_t$. The converse is immediate.

### No Pin Group

**The definition.** A pin group is the group generated by the reflections in the nonzero vectors of a quadratic space; the question is whether the isometry group of the family is such a group.

**The quadratic form.** The quadratic form $\mathfrak{Q}(\tilde Q)=\operatorname{Sc}(\tilde Q^2)$ is not multiplicative. For example,
$$
\mathfrak{Q}\!\left(\frac{5e_t+4\vec e_x}{3}\right)
=\mathfrak{Q}\!\left(\frac{5e_t+4\vec e_y}{3}\right)=1,
\qquad
\mathfrak{Q}\!\left(\frac{(5e_t+4\vec e_x)(5e_t+4\vec e_y)}{9}\right)
=-\frac{431}{81}.
$$
The level set $\{\mathfrak{Q}=\pm1\}$ is not closed under multiplication, and no scalar condition on one parameter cuts a subgroup out of the family. The isometry group of the family is only $\{\pm\mathrm{Ad}_{\tilde Q}\}$, of complex dimension three; it is not a pin group. The isometry condition is a condition on the pair, $\tilde Q_2\tilde Q=\pm e_t$, not on either parameter alone.

**The two adjoints.** The coefficient formula uses the Hilbert–Schmidt adjoint $\dagger$ of the $4\times4$ matrix; the plain adjoint $\approx$ is the adjoint for the form $\operatorname{Sc}(XY)$ on $\mathbb{B}$. They are different involutions. The identity $(L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2))^{\approx}=L_{\mathrm{axf}}(\tilde Q_2)R_{\mathrm{axf}}(\tilde Q)$ is a statement about the operator, not about the coefficient matrix.

## The Structural Reading

### The Enveloping Algebra

**The isomorphism.** The map
$$
\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}_{\mathrm{opp}}
\longrightarrow\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\qquad
\tilde Q\otimes\tilde Q_{2,\mathrm{opp}}
\longmapsto L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)
$$
is an isomorphism of complex algebras. The sixteen elementary tensors $e_\mu\otimes e_{\mathrm{opp},\nu}$ map to the sixteen matrices $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$, which are a basis; the isomorphism is the generation theorem in algebra form.

### The Pure Tensors

**The cone of pure tensors.** Under this isomorphism the two-sided operators are exactly the decomposable tensors $\tilde Q\otimes\tilde Q_{2,\mathrm{opp}}$, that is the affine cone over the Segre variety $\mathbb{P}^3\times\mathbb{P}^3\subset\mathbb{P}^{15}$. The correspondence $L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)\leftrightarrow\tilde Q\otimes\tilde Q_{2,\mathrm{opp}}$ is the same statement as "the element is a pure tensor in $\mathbb{B}\otimes\mathbb{B}_{\mathrm{opp}}$". The seven-dimensional cone of §*The Criterion for a Single Product* is exactly the cone of pure tensors inside the sixteen-dimensional algebra.

### The Real Slice

**The real form.** All sixteen matrices $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$ are real, and their real span is $M_4(\mathbb{R})$. For real parameters $\tilde Q,\tilde Q_2$ with real coefficients, the operator $L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)$ is real, and its coefficient matrix is real of rank at most one. The real products form the real Segre cone, of real dimension seven, inside the complex cone. The real slice is the intersection of the complex cone with $M_4(\mathbb{R})$, and every real matrix in it has a real factorisation: a real rank-one coefficient matrix has a real nonzero column and a real nonzero row.

**The length over the reals.** For a real matrix $M$, the coefficient matrix $c(M)$ is real, and its rank over $\mathbb{R}$ equals its rank over $\mathbb{C}$. Hence the least number of real products summing to $M$ equals the least number of complex products. The length is the same over the two fields.

**The frame.** In the axis-free frame the real structure is the real span of the products. The sixteen cells are real signed permutations, and the real form is read directly from the entries. A complex linear combination of the cells is in $M_4(\mathbb{R})$ exactly when its sixteen coefficients are real, because the cells are a real basis.

## What the Factorization Buys and Does Not

**It gives.**
- An explicit parametrisation by two biquaternions, eight complex parameters modulo the $\mathbb{C}^{\times}$ scaling, hence seven effective parameters.
- A product formula, hence powers, inverses and the monoid structure.
- A rank-one coefficient criterion, hence a decisive test for "is this matrix a single two-sided operator?"
- The length formula $\ell(M)=\operatorname{rank}c(M)$ with $0\le\ell(M)\le4$.
- The plain adjoint and the type criteria: $(L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2))^{\approx}=L_{\mathrm{axf}}(\tilde Q_2)R_{\mathrm{axf}}(\tilde Q)$; self-adjoint exactly when $\tilde Q_2=\lambda\tilde Q$; isometry exactly when $\tilde Q_2\tilde Q=\pm e_t$; multiplicative exactly when $\tilde Q_2\tilde Q=e_t$.
- A real basis of $M_4(\mathbb{R})$ and a coefficient matrix computed by real traces, with the real and complex lengths equal.

**It does not give.**
- Additivity: the set is not a subspace, and the sum of two products is generally not a product.
- Universality: not every matrix is a single product; four products may be needed, and four are always enough.
- A division algebra: the basis matrices are invertible, but the span has zero divisors, for example $L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}+L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_x}$ of rank two.
- A pin group: the quadratic form $\operatorname{Sc}(\tilde Q^2)$ is not multiplicative, and the isometry group of the family is only $\{\pm\mathrm{Ad}_{\tilde Q}\}$, of complex dimension three, with no nonzero skew-adjoint sector.

## Open Questions

- The length stratification: which matrices have length two or three, and what are the frame equations cutting out each stratum? The length is the rank of $c(M)$, so the strata are the determinantal varieties of the coefficient matrix; their images under the inverse map $c^{-1}$ are the matrix strata.
- The normal form of the cone under the automorphism group: the orbit of a pure tensor, its stabiliser, and the relation between the two tensor factors.
- The real slice: the real Segre cone, the real length, and the real forms of the complex cone. Does every real matrix of length $r$ have a real decomposition of length $r$? The rank argument says yes, but the explicit factors are not classified.
- The physical operators of the corpus: which have length two or three, and whether the real structure of the axis-free basis makes their statements frame-independent.

Two questions listed here in earlier editions are answered in *$M_4(\mathbb{C})$ Pauli Representation : Operators*. The frame dependence of $c$ is §*The Change of Frame Is a Congruence* there, and the lengths of the sixteen units are §*The Sixteen Lengths* there. So only the identification of physical operators inside a stratum remains open.

## Summary

The operators on the biquaternion algebra sit at three levels. Every endomorphism has a matrix in $M_4(\mathbb{C})$, and the axis-free basis gives an isomorphism of sixteen-dimensional algebras. The one-sided operators fill the two four-dimensional copies $\mathbb{B}_L=\{L_{\mathrm{axf}}(\tilde Q)\}$ and $\mathbb{B}_R=\{R_{\mathrm{axf}}(\tilde Q_2)\}$; their intersection is the scalars and each is the commutant of the other. The two-sided operators are the products $L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)$.

The left matrix is the structure-constant display with $Q_t$ on the diagonal and the three vector coefficients in the off-diagonal positions; the right matrix differs by the signs of the stitch $R_{\mathrm{axf}}=D(L_{\mathrm{axf}})^{\mathsf T}D$, with $D=\operatorname{diag}(1,-1,-1,-1)$. The four left matrices and the four right matrices are real signed permutations, each family a basis of its copy.

The sixteen products $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$ are real signed permutations and an orthogonal basis of $M_4(\mathbb{C})$, of Hilbert–Schmidt norm two. They compose up to sign with the second slot reversed, their trace is $4Q_tP_t$, and their determinant is $\langle Q\rangle_{\natural}^2\langle P\rangle_{\natural}^2$. Every basis matrix is a unit of determinant one and rank four; the span is not a division algebra, since $L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}+L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_x}=\operatorname{diag}(0,0,2,2)$ has rank two. The first row of the table is the right family, the first column the left family, and the nine remaining cells are genuinely two-sided.

The coefficient matrix $c(M)$ is the coordinate matrix of $M$ in the sixteen-dimensional basis $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$, computed by $c_{\mu\nu}=\frac14\operatorname{Tr}((L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu})^{\mathsf T}M)$. It is a linear isomorphism of $M_4(\mathbb{C})$ onto itself, and it is not the matrix $M$. The product set is the seven-dimensional Segre cone of pure tensors in $\mathbb{B}\otimes\mathbb{B}_{\mathrm{opp}}\cong M_4(\mathbb{C})$. It is not a subspace. The factorisation map has eight parameters, one scaling orbit, and the zero operator as vertex. The product condition is the rank condition $\operatorname{rank}c(M)\le1$.

The length is the coefficient rank, $\ell(M)=\operatorname{rank}c(M)$, and it takes the values $0,1,2,3,4$; every matrix is a sum of at most four products, and a generic matrix needs four. A one-sided operator has rank four for a unit, two for a nonzero zero divisor, and zero for zero. A product has rank $0$, $1$, $2$ or $4$, never three; it is invertible exactly when both parameters are units, and its rank can drop to one when both are zero divisors. The matrix rank and the length are independent: the matrix unit $E_{11}$ has matrix rank one and length four, and the product $L_{\mathrm{axf}}(e_t+\vec e_x)R_{\mathrm{axf}}(e_t+\vec e_y)$ has matrix rank four and length one. All sixteen units have length four. The length is frame-invariant: a change of the element basis sends $c$ to $C^{-1}cC^{-\mathsf T}$, which has the same rank, and a change of the display alone leaves $c$ unchanged, so the length belongs to the operator and not to the array that displays it.

The plain adjoint swaps the two parameters, and the type criteria are $\tilde Q_2=\lambda\tilde Q$ for self-adjoint, $\tilde Q_2\tilde Q=\pm e_t$ for isometry and $\tilde Q_2\tilde Q=e_t$ for multiplicative. The isometry group is $\{\pm\mathrm{Ad}_{\tilde Q}\}$, of complex dimension three, and it is not a pin group.

In one line: every two-sided operator is a single product of one left and one right multiplication; the set of such products is the seven-dimensional cone of pure tensors, characterised by a rank-one coefficient matrix, closed under composition but not under addition, with length the coefficient rank, product matrix rank in $\{0,1,2,4\}$, and the real form $M_4(\mathbb{R})$ visible as the real span of the sixteen real cells.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, $\dim_{\mathbb{C}}=4$ |
| $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$ | the axis-free basis |
| $\mathrm{axf}$ | the label of the frame, on the family: $L_{\mathrm{axf}}$, $R_{\mathrm{axf}}$, $T_{\mathrm{axf},\mu\nu}$ |
| $[Q]=(Q_t,Q_x,Q_y,Q_z)^{\mathsf T}$ | coefficient column of $\tilde Q$ |
| $L_{\mathrm{axf}}(\tilde Q)$ | left matrix, $X\mapsto\tilde QX$ |
| $R_{\mathrm{axf}}(\tilde Q)$ | right matrix, $X\mapsto X\tilde Q$ |
| $\mathbb{B}_L,\mathbb{B}_R$ | the left and right copies in $M_4(\mathbb{C})$ |
| $L_{\mathrm{axf},e_\mu},R_{\mathrm{axf},e_\nu}$ | the four basis matrices of each copy |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | the switch, $R_{\mathrm{axf}}=D(L_{\mathrm{axf}})^{\mathsf T}D$ |
| $L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)$ | two-sided operator, $X\mapsto\tilde QX\tilde Q_2$ |
| $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$ | the sixteen basis matrices |
| $c(M)$ | coefficient matrix, $c_{\mu\nu}=\frac14\operatorname{Tr}((L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu})^{\mathsf T}M)$ |
| $\ell(M)$ | length, the least number of products summing to $M$; equal to $\operatorname{rank}c(M)$ |
| $\Phi(\tilde Q,\tilde Q_2)=L_{\mathrm{axf}}(\tilde Q)R_{\mathrm{axf}}(\tilde Q_2)$ | factorisation map |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the squared vector part |
| $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ | quaternionic norm, the scalar of $\tilde Q\tilde Q^{\natural}$ |
| $\tilde Q^{\natural}=Q_t-\vec Q$ | natural conjugation |
| $\tilde Q^{*}=\bar{\tilde Q}^{\natural}$ | Hermitian conjugation |
| $\mathrm{Ad}_{\tilde Q}(X)=\tilde QX\tilde Q^{-1}$ | inner automorphism |
| $\mathbb{B}_{\mathrm{opp}}$ | the opposite algebra |
| $\mathbb{B}^{\times}$ | the unit group |
| $\operatorname{Sc}$ | scalar part, the $e_t$ coefficient |
| $\approx$ | plain adjoint for $\langle X,Y\rangle=\operatorname{Sc}(XY)$ |
| $\dagger$ | Hilbert–Schmidt adjoint |
| $\operatorname{rank}M$ | the matrix rank of $M$; the coefficient rank is written $\operatorname{rank}c(M)$ |
| $E_{11}$ | the first matrix unit in the axis-free basis |
| $M_4(\mathbb{R})$ | the real matrices, the real span of the sixteen cells |

## Further Reading

- [$M_4(\mathbb{C})$ Axis-Free Representation](m4c-axis-free-representation.html), for the frame, the left and right matrices and the six subspaces.
- [$M_4(\mathbb{C})$ Pauli Representation : Operators](m4c-pauli-representation-operators.html), for the same operators in the standard Peirce frame.
- [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html), for the Peirce frame where a two-sided operator is a pair of $2\times2$ matrices and the display is $B^{\mathsf T}\otimes A$.
- [$M_4(\mathbb{C})$ Pauli Representation](m4c-pauli-representation.html), for the frame, the pure swap stitch and the tensor displays.
- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the abstract family, the generation theorem, the composition, the adjoint and the type criteria.
- [The Matrix Algebra $M_4(\mathbb{C})$](the-matrix-algebra-m4c.html), for the construction of $M_4(\mathbb{C})$ from the sandwich map and the change to the matrix-unit basis.
- [The One-Sided Operators on the Biquaternion Algebra](the-one-sided-operators-on-the-biquaternion-algebra.html), for $L_{\mathrm{axf}}$, $R_{\mathrm{axf}}$ and the four matrices of each side.
- [The Endomorphisms of the Biquaternion Algebra](the-endomorphisms-of-the-biquaternion-algebra.html), for the ambient operator space and its coordinate column.
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for the algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}_{\mathrm{opp}}$ and the pure tensors.
- [The Four Adjoints of the Biquaternion Algebra in Examples](the-four-adjoints-of-the-biquaternion-algebra-in-examples.html), for the plain adjoint and its comparison with the other adjoints.
- [The Hermitian Sandwich: Definition and Multiplicativity](the-hermitian-sandwich-definition-and-multiplicativity.html), for the real subcone $\tilde Q_2=\tilde Q^{*}$.
- [Matrix Representations Conventions](matrix-representations-conventions.html), for the four left and four right matrices and the sixteen cells entry by entry.
