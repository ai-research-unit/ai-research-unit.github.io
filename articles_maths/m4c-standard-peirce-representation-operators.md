# __$M_4(\mathbb{C})$ Standard Peirce Representation : Operators__

## Introduction

**The question.** The Standard Peirce article computes the left matrix $L^{P}(\tilde Q)$ and the right matrix $R^{P}(\tilde P)$ of a biquaternion, their product, their trace, their determinant and their values on the six subspaces. This article asks the operator question that follows: which endomorphisms of $\mathbb{B}$ arise from multiplication, what are their matrices inside $M_4(\mathbb{C})$, and how is the matrix algebra organised by the two-sided products?

**The three answers.** The answers sit at three levels.

- A general endomorphism is any matrix in $M_4(\mathbb{C})$. The frame gives a linear isomorphism $\operatorname{End}_{\mathbb{C}}(\mathbb{B})\to M_4(\mathbb{C})$, and every $4\times4$ matrix is the matrix of exactly one operator. The space has sixteen complex dimensions, and a general operator need not be a single product.
- A one-sided operator is a left or a right multiplication. The left matrices fill the four-dimensional copy $\mathbb{B}_L=\{\mathrm I_2\otimes A\}$, and the right matrices fill the four-dimensional copy $\mathbb{B}_R=\{B^{\mathsf T}\otimes\mathrm I_2\}$. These are exactly the two subsets of the Standard Peirce article, and their intersection is the scalars.
- A two-sided operator is a product $T_{\tilde Q,\tilde P}=L^{P}(\tilde Q)R^{P}(\tilde P)$. The products fill a seven-dimensional cone in $M_4(\mathbb{C})$, not a subspace, and they are exactly the matrices whose coefficient matrix has rank at most one.

**The matrix side.** The sixteen products $T_{\mu\nu}=L_\mu^{P}R_\nu^{P}$ form an orthogonal basis of $M_4(\mathbb{C})$, of Hilbert–Schmidt norm two. The Pauli evaluation writes each of them as a $4\times4$ Kronecker product of two $2\times2$ matrices. One Clifford frame, built from a pair $(\beta,\delta)$ of orthogonal spatial directions, gives five cell multiples and the Clifford relations. The coefficient matrix $c(M)$ turns the product condition into a rank condition, and the cone of products into the cone over the Segre variety $\mathbb{P}^3\times\mathbb{P}^3$. The article records these constructions, and closes with the open questions.

**The result in one line.** Every matrix is a sum of at most four two-sided products; the products themselves are the matrices of coefficient rank at most one; and the least number of products is the coefficient rank.

**Boundaries.** The frame and the one-sided matrices are *$M_4(\mathbb{C})$ Standard Peirce Representation*. The same operators in the canonical frame are *$M_4(\mathbb{C})_{\mathcal{T}}$ Representation : The Two-Sided Operators on the Biquaternion Algebra*. The abstract family is *Two-Sided Operators on the Biquaternion Algebra*. The ambient endomorphisms are *$M_4(\mathbb{C})$ Representation : The General Endomorphisms*. The enveloping algebra is *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*. The Hermitian sandwich is Part V and is not treated here.

**Conventions.** The basis is $e_t,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$. The frame is the standard Peirce frame
$$
\mathcal{P}=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-),\qquad
\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z),\qquad
\vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y),
$$
and a matrix written without a superscript is in this frame. The coefficient coordinates are $(t,x,y,z)$. The quaternionic norm is $\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$, the determinant of $\mathsf M_2(\tilde Q)$, the natural conjugate is $\tilde Q^{\natural}=Q_t-\vec Q$, and the Hermitian conjugate is $\tilde Q^{*}=\bar{\tilde Q}^{\natural}$. The $2\times2$ model is $\mathsf M_2(\tilde Q)$, with
$$
\mathsf M_2(e_t)=\mathrm I_2,\qquad
\mathsf M_2(\vec e_x)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\qquad
\mathsf M_2(\vec e_y)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
\mathsf M_2(\vec e_z)=\begin{pmatrix}-i&0\\0&i\end{pmatrix},
$$
and the Pauli matrices are
$$
\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad
\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
$$
so that $\mathsf M_2(e_k)=-i\sigma_k$ and $\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$, $\operatorname{tr}\mathsf M_2(\tilde Q)=2Q_t$. The exchange $\mathsf S$ is the permutation of the second and third coordinates; in the frame it satisfies
$$
R^{P}(\tilde Q)=\mathsf S\,L^{P}(\tilde Q)^{\mathsf T}\mathsf S^{-1}.
$$

## The Three Correspondences

**The ambient space.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the basis above. Its complex dimension is four, and $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ is the algebra $M_4(\mathbb{C})$ of complex dimension sixteen. Every endomorphism is written in the frame $\mathcal{P}$. The left matrix is $L^{P}(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q)$ and the right matrix is $R^{P}(\tilde P)=\mathsf M_2(\tilde P)^{\mathsf T}\otimes\mathrm I_2$; the two are the operators of left and right multiplication on $\mathbb{B}$.

**General endomorphisms.** Fixing the frame gives a linear isomorphism
$$
\operatorname{End}_{\mathbb{C}}(\mathbb{B})\longrightarrow M_4(\mathbb{C}),\qquad
M\longmapsto [M]_{\mathcal{P}},
$$
and it is an isomorphism of algebras. Every $4\times4$ matrix is the matrix of exactly one endomorphism, and every endomorphism has exactly one matrix in the frame. The level is the whole ambient space, of sixteen complex dimensions. A general matrix need not be a left multiplication, a right multiplication or a two-sided product; the product set is the subject of the rest of the article.

**One-sided operators.** The left multiplications fill the image
$$
\mathbb{B}_L=\{L^{P}(\tilde Q):\tilde Q\in\mathbb{B}\}
=\{\mathrm I_2\otimes A:A\in M_2(\mathbb{C})\},
$$
and the right multiplications fill
$$
\mathbb{B}_R=\{R^{P}(\tilde P):\tilde P\in\mathbb{B}\}
=\{B^{\mathsf T}\otimes\mathrm I_2:B\in M_2(\mathbb{C})\}.
$$
These are exactly the two four-dimensional subsets of the Standard Peirce article. Each is a subalgebra: $\mathbb{B}_L\cong\mathbb{B}$ and $\mathbb{B}_R\cong\mathbb{B}^{\mathrm{opp}}$. Their intersection is the line of scalars $\mathbb{C}\cdot\mathrm I_4$, and each is the commutant of the other.

**Two-sided operators.** The product of a left and a right multiplication is the operator
$$
T_{\tilde Q,\tilde P}=L^{P}(\tilde Q)R^{P}(\tilde P),\qquad
T_{\tilde Q,\tilde P}(X)=\tilde QX\tilde P .
$$
The two factors commute, so $T_{\tilde Q,\tilde P}=R^{P}(\tilde P)L^{P}(\tilde Q)$ as well. The pair $(\tilde Q,\tilde P)$ has eight complex parameters, and the scaling $(\tilde Q,\tilde P)\mapsto(\lambda\tilde Q,\lambda^{-1}\tilde P)$ leaves the operator unchanged, so the image has seven effective parameters. The image is a cone, not a subspace. It is exactly the set of matrices whose coefficient matrix has rank at most one.

**The table.** The three levels and the two one-sided copies are collected in one table. The coefficient matrix is defined in §*The Coefficient Matrix $c(M)$*.

| Level | Operator | Subset of $M_4(\mathbb{C})$ | Complex dimension | Test |
|---|---|---|---|---|
| general endomorphism | $M$ | all of $M_4(\mathbb{C})$ | $16$ | none |
| one-sided left | $L^{P}(\tilde Q)$ | $\{\mathrm I_2\otimes A\}$ | $4$ | two equal diagonal blocks |
| one-sided right | $R^{P}(\tilde P)$ | $\{B^{\mathsf T}\otimes\mathrm I_2\}$ | $4$ | scalar blocks |
| intersection of the one-sided copies | $\lambda\mathrm I_4$ | the scalars | $1$ | both conditions |
| two-sided | $T_{\tilde Q,\tilde P}$ | $\{\operatorname{rank}c(M)\le1\}$ | $7$ (cone) | rank-one coefficient matrix |

The table is the answer to the operator question. The general level is the whole space; the one-sided levels are two linear subspaces; the two-sided level is a cone inside the whole space, of dimension seven.

## The One-Sided Operators

**The left copy.** The left matrix is
$$
L^{P}(\tilde Q)=\mathrm I_2\otimes A=\operatorname{diag}(A,A),\qquad
A=\mathsf M_2(\tilde Q).
$$
Its image is the four-dimensional subalgebra $\mathbb{B}_L$. The composition law is $L^{P}(\tilde Q)L^{P}(\tilde R)=L^{P}(\tilde Q\tilde R)$, and the map $\tilde Q\mapsto L^{P}(\tilde Q)$ is injective. The rank is $2\operatorname{rank}A$, the trace is $2\operatorname{Tr}A=4Q_t$, and the determinant is $(\det A)^2=\langle\tilde Q\rangle_{\natural}^2$. The four basis matrices $L_\mu^{P}$ are the images of the four units, and they are the four matrices of the Standard Peirce article.

**The four left matrices.** With $L_\mu^{P}=L^{P}(e_\mu)$,
$$
L_t^{P}=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
L_x^{P}=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix},
$$
$$
L_y^{P}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
L_z^{P}=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix},
$$
and a general element is $L^{P}(\tilde Q)=Q_tL_t^{P}+Q_xL_x^{P}+Q_yL_y^{P}+Q_zL_z^{P}$. In the Pauli form $L_t^{P}=\mathrm I_2\otimes\mathrm I_2$ and $L_k^{P}=-i\,\mathrm I_2\otimes\sigma_k$.

**The right copy.** The right matrix is
$$
R^{P}(\tilde P)=B^{\mathsf T}\otimes\mathrm I_2,\qquad
B=\mathsf M_2(\tilde P),
$$
a block matrix whose four blocks are scalar multiples of $\mathrm I_2$. Its image is the four-dimensional subalgebra $\mathbb{B}_R$. The composition law is anti-multiplicative, $R^{P}(\tilde P)R^{P}(\tilde S)=R^{P}(\tilde S\tilde P)$, and the map $\tilde P\mapsto R^{P}(\tilde P)$ is injective. The rank is $2\operatorname{rank}B$, the trace is $2\operatorname{Tr}B=4P_t$, and the determinant is $(\det B)^2=\langle\tilde P\rangle_{\natural}^2$. The four basis matrices $R_\mu^{P}$ are the images of the four units.

**The four right matrices.** With $R_\nu^{P}=R^{P}(e_\nu)$,
$$
R_t^{P}=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
R_x^{P}=\begin{pmatrix}0&0&-i&0\\0&0&0&-i\\-i&0&0&0\\0&-i&0&0\end{pmatrix},
$$
$$
R_y^{P}=\begin{pmatrix}0&0&1&0\\0&0&0&1\\-1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
R_z^{P}=\begin{pmatrix}-i&0&0&0\\0&-i&0&0\\0&0&i&0\\0&0&0&i\end{pmatrix}.
$$
In the Pauli form $R_t^{P}=\mathrm I_4$, $R_x^{P}=-i\,\sigma_1\otimes\mathrm I_2$, $R_y^{P}=+i\,\sigma_2\otimes\mathrm I_2$ and $R_z^{P}=-i\,\sigma_3\otimes\mathrm I_2$. The signs differ from those of the left family because the transpose exchanges $\sigma_2$ with $-\sigma_2$ and fixes $\sigma_1,\sigma_3$.

**The exchange.** The two copies are exchanged by the transpose and the permutation $\mathsf S$ of the second and third coordinates:
$$
R^{P}(\tilde Q)=\mathsf S\,L^{P}(\tilde Q)^{\mathsf T}\mathsf S^{-1},\qquad
L^{P}(\tilde Q)=\mathsf S\,R^{P}(\tilde Q)^{\mathsf T}\mathsf S^{-1}.
$$
The two identities are the frame form of the stitch between the left and the right. They will be used for the entry $T_{xy}$ and for the basis matrices. The subscript names the action, not the tensor slot: in this frame the left copy is the second factor and the right copy the first. The matrix of the exchange is
$$
\mathsf S=\begin{pmatrix}1&0&0&0\\0&0&1&0\\0&1&0&0\\0&0&0&1\end{pmatrix},
$$
symmetric and involutive, $\mathsf S^{\mathsf T}=\mathsf S=\mathsf S^{-1}$, of trace $2$ and determinant $-1$. In the coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ the same operator is the reflection $\operatorname{diag}(1,1,-1,1)$, which fixes $e_t,\vec e_x,\vec e_z$ and negates $\vec e_y$.

**The intersection.** A matrix that is both block-diagonal with two equal blocks and block-scalar with four scalar blocks is a scalar matrix:
$$
\mathbb{B}_L\cap\mathbb{B}_R=\mathbb{C}\cdot\mathrm I_4 .
$$
The left copy is the commutant of the right copy, and the right copy is the commutant of the left copy; the two copies are mutual centralisers. The intersection is the centre of each.

**The commutant of one element.** The two copies are the commutants of each other; the commutant of a single matrix is smaller. For a non-scalar element, the commutant of $\mathrm I_2\otimes\mathsf M_2(\tilde Q)$ in $M_4(\mathbb{C})$ is
$$
M_2(\mathbb{C})\otimes\mathbb{C}\bigl[\mathsf M_2(\tilde Q)\bigr],
$$
of complex dimension $2\cdot4=8$: the first slot is free, and the second is spanned by $\mathrm I_2$ and the matrix itself, by Cayley–Hamilton. For a scalar element the commutant is all of $M_4(\mathbb{C})$, of dimension sixteen. The minimal polynomial is the one of the entry matrix in both cases, of degree two, and it does not square: the regular matrix is never nonderogatory, although its characteristic polynomial has degree four.

**The compression.** In the $2\times2$ model the left matrix compresses to $A$ and the right matrix compresses to $B^{\mathsf T}$. The two-sided product does not compress to a single $2\times2$ matrix: it is the $4\times4$ product $B^{\mathsf T}\otimes A$, and the two tensor factors are both needed. The one-sided actions compress one at a time; the two-sided operator is the product of the two uncompressed actions. The pair description, with one matrix per side and a pair for the product, is the subject of *$M_2(\mathbb{C})$ Standard Peirce Representation : Operators*.

**The general level.** A matrix of $M_4(\mathbb{C})$ that is neither in $\mathbb{B}_L$ nor in $\mathbb{B}_R$ is still an endomorphism, and the frame gives its matrix. Such a matrix is a sum of two-sided products, but not necessarily a single one. The next sections compute the sixteen basis matrices of the product family, then measure how far a general matrix is from being a single product, through the coefficient matrix.

## The Sixteen Matrices $T_{\mu\nu}=L_\mu^{P}R_\nu^{P}$

### The Table in Four Families

**Definition.** For $\mu,\nu\in\{t,x,y,z\}$ put
$$
T_{\mu\nu}=L_\mu^{P}R_\nu^{P},\qquad
L_\mu^{P}=L^{P}(e_\mu),\qquad
R_\nu^{P}=R^{P}(e_\nu).
$$
The matrix $T_{\mu\nu}$ is the matrix of $X\mapsto e_\mu Xe_\nu$. A general two-sided operator is the linear combination
$$
T_{\tilde Q,\tilde P}=\sum_{\mu,\nu}Q_\mu P_\nu\,T_{\mu\nu}.
$$

**The table.** The sixteen matrices fall into four families.

| $T_{\mu\nu}$ | $\nu=t$ | $\nu=x$ | $\nu=y$ | $\nu=z$ |
|---|---|---|---|---|
| $\mu=t$ | $T_{tt}=\mathrm I_4$ | $T_{tx}=R_x^{P}$ | $T_{ty}=R_y^{P}$ | $T_{tz}=R_z^{P}$ |
| $\mu=x$ | $T_{xt}=L_x^{P}$ | $T_{xx}=L_x^{P}R_x^{P}$ | $T_{xy}=L_x^{P}R_y^{P}$ | $T_{xz}=L_x^{P}R_z^{P}$ |
| $\mu=y$ | $T_{yt}=L_y^{P}$ | $T_{yx}=L_y^{P}R_x^{P}$ | $T_{yy}=L_y^{P}R_y^{P}$ | $T_{yz}=L_y^{P}R_z^{P}$ |
| $\mu=z$ | $T_{zt}=L_z^{P}$ | $T_{zx}=L_z^{P}R_x^{P}$ | $T_{zy}=L_z^{P}R_y^{P}$ | $T_{zz}=L_z^{P}R_z^{P}$ |

The first row is the right family, the first column the left family, the diagonal entry $T_{tt}$ the identity, and the remaining nine the genuinely two-sided cells. The table is the matrix form of the four families of *Two-Sided Operators on the Biquaternion Algebra*, §*The Operator $T_{\tilde Q,\tilde P}$*.

### The Sixteen, Entry by Entry

**The display.** In the Peirce frame, grouped by the left index $\mu$,
$$
T_{tt}=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
T_{tx}=\begin{pmatrix}0&0&-i&0\\0&0&0&-i\\-i&0&0&0\\0&-i&0&0\end{pmatrix},
$$
$$
T_{ty}=\begin{pmatrix}0&0&1&0\\0&0&0&1\\-1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
T_{tz}=\begin{pmatrix}-i&0&0&0\\0&-i&0&0\\0&0&i&0\\0&0&0&i\end{pmatrix},
$$
$$
T_{xt}=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix},\qquad
T_{xx}=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix},
$$
$$
T_{xy}=\begin{pmatrix}0&0&0&-i\\0&0&-i&0\\0&i&0&0\\i&0&0&0\end{pmatrix},\qquad
T_{xz}=\begin{pmatrix}0&-1&0&0\\-1&0&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix},
$$
$$
T_{yt}=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
T_{yx}=\begin{pmatrix}0&0&0&i\\0&0&-i&0\\0&i&0&0\\-i&0&0&0\end{pmatrix},
$$
$$
T_{yy}=\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&1&0&0\\-1&0&0&0\end{pmatrix},\qquad
T_{yz}=\begin{pmatrix}0&i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&i&0\end{pmatrix},
$$
$$
T_{zt}=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix},\qquad
T_{zx}=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\-1&0&0&0\\0&1&0&0\end{pmatrix},
$$
$$
T_{zy}=\begin{pmatrix}0&0&-i&0\\0&0&0&i\\i&0&0&0\\0&-i&0&0\end{pmatrix},\qquad
T_{zz}=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&-1\end{pmatrix}.
$$

**The pattern.** Each matrix has four nonzero entries, one in each row and each column, and every nonzero entry is $\pm1$ or $\pm i$. The first row and the first column are the four left and the four right matrices; the nine remaining entries are the genuinely two-sided cells. The display is the matrix form of the sixteen products $T_{\mu\nu}=L_\mu^{P}R_\nu^{P}$ of *Matrix Representations Conventions*, §*The 4×4 Regular Representation*.

**The Pauli evaluation on the families.** With $\mathsf M_2(e_t)=\mathrm I_2$ and $\mathsf M_2(e_k)=-i\sigma_k$,
$$
T_{tt}=\mathrm I_4,\qquad
T_{tk}=-i\,\sigma_k^{\mathsf T}\otimes\mathrm I_2,\qquad
T_{kt}=-i\,\mathrm I_2\otimes\sigma_k,\qquad
T_{jk}=-\sigma_k^{\mathsf T}\otimes\sigma_j,
$$
with $j,k\in\{x,y,z\}$. The first family is the identity, the second the right copy, the third the left copy, and the fourth the nine genuinely two-sided cells. The evaluation is a $4\times4$ Kronecker product of two $2\times2$ matrices; §*The Kronecker Question* separates it from the $16\times16$ Kronecker product of two $4\times4$ matrices.

**One entry.** The table gives $T_{xy}=L_x^{P}R_y^{P}=L_x^{P}\mathsf S\,(L_y^{P})^{\mathsf T}\mathsf S^{-1}$,
$$
T_{xy}=
\begin{pmatrix}
0&0&0&-i\\
0&0&-i&0\\
0&i&0&0\\
i&0&0&0
\end{pmatrix},
$$
whose first column is the coordinate column of $e_x\tilde\Pi_+e_y=i\tilde\Pi_-$. The entry is the check that the family rule and the exchange agree.

**The basis.** The sixteen matrices are linearly independent and span $M_4(\mathbb{C})$, by the orthogonality theorem of §*Orthogonality* and the dimension count. The span of the products is the whole algebra: the generation theorem of *Two-Sided Operators on the Biquaternion Algebra*, §*The Sixteen Products as a Basis*, read in this frame. The expansion of a general matrix in this basis is unique, and the coefficient matrix is the subject of §*The Cone of Products*.

### Composition, Trace, Determinant

**Composition.** The product of two basis matrices is a signed basis matrix:
$$
T_{\mu\nu}T_{\rho\sigma}=T_{e_\mu e_\rho,\ e_\sigma e_\nu}=\epsilon\epsilon'\,T_{\mu'\nu'},
$$
where $e_\mu e_\rho=\epsilon e_{\mu'}$ and $e_\sigma e_\nu=\epsilon' e_{\nu'}$, with $\epsilon,\epsilon'\in\{\pm1\}$. For general parameters,
$$
T_{\tilde Q,\tilde P}T_{\tilde R,\tilde S}=T_{\tilde Q\tilde R,\ \tilde S\tilde P}.
$$
The sixteen are closed under multiplication up to sign, with unit $T_{tt}=\mathrm I_4$; they are not a group, because $-T_{\mu\nu}$ is not one of the sixteen. The full product family contains the signs, since $-T_{\mu\nu}=T_{-e_\mu,e_\nu}$.

**Trace and determinant.** For $\tilde Q,\tilde P$ with $\langle\tilde Q\rangle_{\natural}\langle\tilde P\rangle_{\natural}\neq0$,
$$
\operatorname{Tr}T_{\tilde Q,\tilde P}=4\,Q_tP_t,\qquad
\det T_{\tilde Q,\tilde P}=\langle\tilde Q\rangle_{\natural}^{2}\langle\tilde P\rangle_{\natural}^{2},
\qquad
T_{\tilde Q,\tilde P}^{-1}=T_{\tilde Q^{-1},\tilde P^{-1}}.
$$
*Proof.* In the Pauli evaluation $T_{\tilde Q,\tilde P}=\mathsf M_2(\tilde P)^{\mathsf T}\otimes\mathsf M_2(\tilde Q)$. The trace of a Kronecker product is the product of the traces, $\operatorname{Tr}\mathsf M_2(\tilde P)^{\mathsf T}=2P_t$ and $\operatorname{Tr}\mathsf M_2(\tilde Q)=2Q_t$; the determinant is $\det(\mathsf M_2(\tilde P))^{2}\det(\mathsf M_2(\tilde Q))^{2}$, and $\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$. The inverse is the inverse of each factor.

**The basis values.** Every basis matrix is invertible, of determinant $1$ and rank $4$; the trace is $4$ only for $T_{tt}$ and $0$ for the other fifteen. The basis consists of units, but its span does not: for example
$$
T_{tt}+T_{xx}=\mathrm I_4+L_x^{P}R_x^{P}=
\begin{pmatrix}
1&0&0&-1\\
0&1&-1&0\\
0&-1&1&0\\
-1&0&0&1
\end{pmatrix}
$$
has rank two. A basis of invertible matrices does not make the algebra a division algebra; the algebra is $M_4(\mathbb{C})$ and has many zero divisors.

### Orthogonality

**Theorem (orthogonality).** For the Hilbert–Schmidt inner product $\langle A,B\rangle=\operatorname{Tr}(A^{\dagger}B)$,
$$
\operatorname{Tr}\bigl(T_{\mu\nu}^{\dagger}T_{\rho\sigma}\bigr)=4\,\delta_{\mu\rho}\,\delta_{\nu\sigma}.
$$
The sixteen basis matrices are orthogonal, each of Hilbert–Schmidt norm $2$.

*Proof.* In the Pauli evaluation, $T_{\mu\nu}=\mathsf M_2(e_\nu)^{\mathsf T}\otimes\mathsf M_2(e_\mu)$. The Hilbert–Schmidt inner product of two Kronecker products is the product of the inner products of the factors. In the $2\times2$ model the four matrices $\mathsf M_2(e_\mu)$ are orthogonal of norm $\sqrt2$, because $\mathsf M_2(e_\mu)=-i\sigma_\mu$ for $\mu=x,y,z$ and $\mathsf M_2(e_t)=\mathrm I_2$; hence the product is $2\cdot2=4$ exactly when both indices agree, and $0$ otherwise.

**The coefficient formula.** If $M=\sum c_{\mu\nu}T_{\mu\nu}$, then orthogonality gives
$$
c_{\mu\nu}=\tfrac14\operatorname{Tr}\bigl(T_{\mu\nu}^{\dagger}M\bigr).
$$
The map $M\mapsto c(M)$ is a linear isomorphism of $M_4(\mathbb{C})$ onto itself. It is the coordinate chart used in §*The Cone of Products*.

**The coefficient basis.** In the coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ the same sixteen are signed permutation matrices, the conjugates $C_{\Pi}T_{\mu\nu}C_{\Pi}^{-1}$ by the Peirce change of *$M_4(\mathbb{C})$ Representation : The General Endomorphisms*, §*The Change $C_{\Pi}$*; in the Peirce frame they are the products of a left matrix and a right matrix. The conjugation changes the entries, not the algebra; the Peirce frame is the display in which the Clifford construction closes.

## The Kronecker Question

### The Pauli Evaluation

**The two one-sided evaluations.** In the $2\times2$ model,
$$
L^{P}(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q),\qquad
R^{P}(\tilde P)=\mathsf M_2(\tilde P)^{\mathsf T}\otimes\mathrm I_2.
$$
The first factor of $L^{P}(\tilde Q)$ is the copy index, the second the spinor index; the right matrix acts on the copy index and is the transpose of the left matrix of $\tilde P$, in the exchanged frame. The product is
$$
T_{\tilde Q,\tilde P}=L^{P}(\tilde Q)R^{P}(\tilde P)
=\mathsf M_2(\tilde P)^{\mathsf T}\otimes\mathsf M_2(\tilde Q).
$$

**On the basis.** The evaluation reproduces the four family formulas of §*The Table in Four Families*: the identity, the right copy, the left copy and the nine cells. It is a $4\times4$ matrix, the Kronecker product of two $2\times2$ matrices, and it is the ordinary product $L^{P}(\tilde Q)R^{P}(\tilde P)$ written in the model.

### Why the $4\times4$ Kronecker Product Is Not the Operator

**The dimensions.** $L^{P}(\tilde Q)$ and $R^{P}(\tilde P)$ are $4\times4$ matrices. Their Kronecker product $L^{P}(\tilde Q)\otimes R^{P}(\tilde P)$ is a $16\times16$ matrix. It acts on $\mathbb{C}^4\otimes\mathbb{C}^4$, a complex space of dimension sixteen; the operator $T_{\tilde Q,\tilde P}$ acts on $\mathbb{B}\cong\mathbb{C}^4$, of complex dimension four. The two cannot be the same matrix, and the $16\times16$ matrix does not represent the operator on the carrier.

**The correct product.** The matrix of the operator is the ordinary product $L^{P}(\tilde Q)R^{P}(\tilde P)$, of size $4\times4$. The algebra-level construction is the tensor product of algebras
$$
\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\longrightarrow\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\qquad
\tilde Q\otimes\tilde P^{\mathrm{opp}}\longmapsto L^{P}(\tilde Q)R^{P}(\tilde P),
$$
with $\mathbb{B}^{\mathrm{opp}}$ the opposite algebra (the reversed product); the sixteen elementary tensors $e_\mu\otimes e_\nu^{\mathrm{opp}}$ map to the sixteen matrices $T_{\mu\nu}$. The Kronecker product of the matrices is a different construction: it is the matrix of the tensor product of the two operators on the tensor product of the carriers, not the matrix of their composite on one carrier.

**The three products.** The ordinary product $L^{P}(\tilde Q)R^{P}(\tilde P)$ is $4\times4$ and is the operator. The Kronecker product of two $2\times2$ matrices is $4\times4$ and is the evaluation of the ordinary product in the model $\mathbb{B}\cong M_2(\mathbb{C})$. The Kronecker product of two $4\times4$ matrices is $16\times16$ and is neither. The three are related by the identifications of the model, not by an equality of matrices.

**The two displays.** The Peirce frame is the canonical frame of the Standard Peirce article, and the Pauli evaluation is its display. The coefficient basis, reached by the Peirce change $C_{\Pi}$, is the conjugate display: the sixteen are signed permutation matrices, and a general endomorphism is an arbitrary matrix. Neither display changes the operator; the frame changes the entries, the basis changes the coordinates, and the algebra stays $M_4(\mathbb{C})$.

## The Dirac Operator of the Frame

**The operator.** With $\partial_\mu=\partial/\partial Q_\mu$,
$$
D=-\bigl(T_{e_t,e_x}\partial_0+T_{e_x,e_y}\partial_1+T_{e_y,e_y}\partial_2+T_{e_z,e_y}\partial_3\bigr).
$$
On $\tilde Q\in\mathbb{B}$,
$$
\tilde Q\longmapsto-\bigl(\partial_0\tilde Q\,e_x+e_x\,\partial_1\tilde Q\,e_y+e_y\,\partial_2\tilde Q\,e_y+e_z\,\partial_3\tilde Q\,e_y\bigr).
$$
The mass term is $-mT_{tt}$. For a momentum $p$, the same operator reads
$$
D(p)=i\bigl(T_{tx}p_t+T_{xy}p_x+T_{yy}p_y+T_{zy}p_z\bigr),
$$
so the frame is visible in the formula: another pair $(\beta,\delta)$ replaces the four cells by four single products spread over several cells. This is the matrix Dirac operator of the frame; it is not the biquaternionic gradient $\tilde\nabla$, which is a left multiplication. The dictionary relates the two; it does not identify them as operators on the same carrier.

## The Cone of Products

### The Factorization Map

**The map.** The assignment
$$
\Phi:\mathbb{B}\times\mathbb{B}\longrightarrow\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\qquad
\Phi(\tilde Q,\tilde P)=T_{\tilde Q,\tilde P}
$$
is the factorisation map. Its image is the set of two-sided operators, and this section records what the factorisation does and does not imply.

**Bilinearity.** The map is complex-bilinear, not complex-linear:
$$
T_{a\tilde Q+b\tilde Q',\tilde P}=aT_{\tilde Q,\tilde P}+bT_{\tilde Q',\tilde P},\qquad
T_{\tilde Q,a\tilde P+b\tilde P'}=aT_{\tilde Q,\tilde P}+bT_{\tilde Q,\tilde P'}.
$$
Consequently the image is a cone, not a subspace: for $\lambda\in\mathbb{C}$,
$$
\lambda T_{\tilde Q,\tilde P}=T_{\lambda\tilde Q,\tilde P}=T_{\tilde Q,\lambda\tilde P}.
$$

**The scaling orbit.** For $\lambda\in\mathbb{C}^{\times}$,
$$
T_{\lambda\tilde Q,\lambda^{-1}\tilde P}=T_{\tilde Q,\tilde P}.
$$
The group $\mathbb{C}^{\times}$ acts on $\mathbb{B}\times\mathbb{B}$ by $(\tilde Q,\tilde P)\mapsto(\lambda\tilde Q,\lambda^{-1}\tilde P)$, and the factorisation map is constant on every orbit.

**The zero set.** The product vanishes exactly when one parameter vanishes:
$$
T_{\tilde Q,\tilde P}=0\iff \tilde Q=0\ \text{or}\ \tilde P=0 .
$$
If both are nonzero, write $A=\mathsf M_2(\tilde Q)$ and $B=\mathsf M_2(\tilde P)$. Choose indices $a,b,c,d$ with $A_{ab}\neq0$ and $B_{cd}\neq0$, and take the matrix unit $E_{bc}$; then
$$
(AE_{bc}B)_{ad}=A_{ab}B_{cd}\neq0,
$$
so the operator is nonzero. The zero operator is the image of every pair with a zero parameter, and it is the vertex of the cone.

**The two slots.** With the other parameter a unit, the map is injective in each slot:
$$
T_{\tilde Q,e_t}=L^{P}(\tilde Q),\qquad
T_{e_t,\tilde P}=R^{P}(\tilde P).
$$
The first is the left copy, the second the right copy, and both parametrisations are injective. More generally, $T_{\tilde Q,\tilde P}(e_t)=\tilde Q\tilde P$; if $\tilde P$ is a unit, $\tilde Q$ is recovered from this value, and if $\tilde Q$ is a unit, $\tilde P$ is recovered.

**The fibres.** For a nonzero product the fibre of the factorisation map is exactly one scaling orbit:
$$
T_{\tilde Q,\tilde P}=T_{\tilde R,\tilde S}
\iff
\tilde R=\lambda\tilde Q,\quad
\tilde S=\lambda^{-1}\tilde P
\quad\text{for some }\lambda\in\mathbb{C}^{\times}.
$$
Suppose all four parameters are nonzero and $T_{\tilde Q,\tilde P}=T_{\tilde R,\tilde S}$. Write $A=\mathsf M_2(\tilde Q)$, $B=\mathsf M_2(\tilde P)$, $C=\mathsf M_2(\tilde R)$, $D=\mathsf M_2(\tilde S)$. In the matrix model, $AXB=CXD$ for every $X\in M_2(\mathbb{C})$. On the matrix units $X=E_{ij}$ this reads $A_{ki}B_{jl}=C_{ki}D_{jl}$ for all $i,j,k,l$. Choose $(k_0,i_0)$ with $A_{k_0i_0}\neq0$ and $(j_0,l_0)$ with $B_{j_0l_0}\neq0$, and put $\lambda=C_{k_0i_0}/A_{k_0i_0}$. The identity with $i=i_0$ and $k=k_0$ gives $D_{jl}=\lambda^{-1}B_{jl}$ for all $j,l$; the identity with $j=j_0$ and $l=l_0$ gives $C_{ki}=\lambda A_{ki}$ for all $k,i$. Hence $C=\lambda A$ and $D=\lambda^{-1}B$, which is the claimed orbit. The converse is the scaling identity.

**The dimension.** The parameter space has complex dimension eight. The generic fibre has complex dimension one, so the image has complex dimension
$$
8-1=7.
$$
The zero operator is the vertex, where the two four-dimensional subspaces $\tilde Q=0$ and $\tilde P=0$ collapse. The image is the seven-dimensional cone of the next subsections.

### The Coefficient Matrix $c(M)$

**Definition.** By §*The Sixteen Matrices $T_{\mu\nu}=L_\mu^{P}R_\nu^{P}$*, every $M\in M_4(\mathbb{C})$ has a unique expansion
$$
M=\sum_{\mu,\nu}c_{\mu\nu}T_{\mu\nu}.
$$
The $4\times4$ matrix $c(M)=(c_{\mu\nu})$ is the **coefficient matrix** of $M$. Orthogonality gives it directly:
$$
c(M)_{\mu\nu}=\tfrac14\operatorname{Tr}\bigl(T_{\mu\nu}^{\dagger}M\bigr).
$$
The map $M\mapsto c(M)$ is a linear isomorphism of $M_4(\mathbb{C})$ onto itself.

**The coordinate column.** For $\tilde Q\in\mathbb{B}$ write $[Q]=(Q_t,Q_x,Q_y,Q_z)^{\mathsf T}$ for the column of its coefficients in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$.

**The expansion of a product.** If $M=T_{\tilde Q,\tilde P}$, then
$$
M=\sum_{\mu,\nu}Q_\mu P_\nu\,T_{\mu\nu},
$$
so $c(M)=[Q][P]^{\mathsf T}$. The coefficient matrix of a product is a rank-one matrix, and every rank-one matrix arises this way. This is the source of the criterion of §*The Criterion for a Single Product*.

### The Length $\ell(M)=\operatorname{rank}c(M)$

**Definition.** The **length** $\ell(M)$ is the least $r\ge0$ such that $M$ is a sum of $r$ products; $\ell(0)=0$.

**Theorem (length is the rank).** For every $M\in M_4(\mathbb{C})$,
$$
\ell(M)=\operatorname{rank}c(M).
$$

*Proof.* If $M=\sum_{i\le r}T_{\tilde Q_i,\tilde P_i}$, then $c(M)=\sum_{i\le r}[Q_i][P_i]^{\mathsf T}$ is a sum of $r$ rank-one matrices, so $\operatorname{rank}c(M)\le r$ and $\ell(M)\ge\operatorname{rank}c(M)$. Conversely, let $\operatorname{rank}c=r$ and factor $c=UV$ with $U$ of size $4\times r$ and $V$ of size $r\times4$; the $i$-th column of $U$ is $[Q_i]$ and the $i$-th row of $V$ is $[P_i]^{\mathsf T}$, so $M=\sum_{i\le r}T_{\tilde Q_i,\tilde P_i}$ and $\ell(M)\le r$.

**The count.** Every matrix is a sum of at most four products; $\ell(M)=4$ exactly when $\det c(M)\neq0$. The condition $\det c(M)\neq0$ is open and dense, so a generic matrix needs four products and none needs five.

### The Criterion for a Single Product

**Theorem (the product criterion).** Let $M\in M_4(\mathbb{C})$ and $c=c(M)$. Then
$$
M=T_{\tilde Q,\tilde P}\ \text{for some }\tilde Q,\tilde P
\iff c=[Q][P]^{\mathsf T}
\iff \operatorname{rank}c\le1.
$$
For $M\neq0$ the rank is exactly one; the zero matrix has $c=0$ and rank zero.

*Proof.* The first equivalence is §*The Coefficient Matrix $c(M)$*. The second is the rank-one criterion: a matrix is $[Q][P]^{\mathsf T}$ exactly when it has rank at most one, and the zero matrix is the case $Q=0$ or $P=0$.

**The cone.** The product set is the closed algebraic cone $\{M:\operatorname{rank}c(M)\le1\}$, cut out by the $2\times2$ minors of $c(M)$. Its projectivisation is the Segre variety $\mathbb{P}^3\times\mathbb{P}^3$, of complex dimension six; the cone has complex dimension seven in the complex sixteen-dimensional algebra. It is closed under multiplication and under inverses on its invertible part, and it is not a subspace: $T_{tt}+T_{xx}$ is not a product, because its coefficient matrix is $\operatorname{diag}(1,1,0,0)$ of rank two.

**The two intersections.** The product set meets the left family in the left family and the right family in the right family: $T_{\tilde Q,e_t}=L^{P}(\tilde Q)$ and $T_{e_t,\tilde P}=R^{P}(\tilde P)$. The two intersections are distinct; they meet in the scalars, by §*The Two One-Sided Boundaries*. The product set is larger than either, and the generic product lies in neither.

**The parametrisation.** The map $(\tilde Q,\tilde P)\mapsto T_{\tilde Q,\tilde P}$ is bilinear and surjective onto the cone. Its fibre over a nonzero product is the scaling orbit $(\lambda\tilde Q,\lambda^{-1}\tilde P)$ of §*The Factorization Map*; the cone has complex dimension $8-1=7$. The kernel and the image of the Hermitian sandwich are a different question, treated in Part V.

### Matrix Rank Against Length

**Theorem (the rank of a product).** For $M=T_{\tilde Q,\tilde P}$,
$$
\operatorname{rank}M=\operatorname{rank}\mathsf M_2(\tilde Q)\cdot\operatorname{rank}\mathsf M_2(\tilde P)\in\{0,1,2,4\}.
$$
In particular $\operatorname{rank}M=4$ exactly when both parameters are units, and no product has rank three.

*Proof.* In the Pauli evaluation $T_{\tilde Q,\tilde P}=\mathsf M_2(\tilde P)^{\mathsf T}\otimes\mathsf M_2(\tilde Q)$. The rank of a Kronecker product is the product of the ranks, and the rank of $\mathsf M_2(\tilde Q)$ is $2$ when $\langle\tilde Q\rangle_{\natural}\neq0$, $1$ when $\tilde Q\neq0$ and $\langle\tilde Q\rangle_{\natural}=0$, and $0$ when $\tilde Q=0$.

**The two ranks are independent.** Neither $\operatorname{rank}M$ nor $\ell(M)$ determines the other. The matrix
$$
M_1=(u_2+u_3)(u_2+u_3)^{\mathsf T}=
\begin{pmatrix}
0&0&0&0\\
0&1&1&0\\
0&1&1&0\\
0&0&0&0
\end{pmatrix},
$$
with $u_i$ the $i$-th standard column, has $\operatorname{rank}M_1=1$ and coefficient matrix $c(M_1)=\tfrac12\operatorname{diag}(1,-1,1,1)$, of rank four, so $\ell(M_1)=4$. The projector $P_+$ has $\operatorname{rank}P_+=2$ and $\ell(P_+)=1$. Among the rank-one matrices, those of length four form a dense open subset.

**The table.**

| $M$ | $\operatorname{rank}M$ | $\operatorname{rank}c(M)$ | $\ell(M)$ | decomposition |
|---|---|---|---|---|
| $T_{tt}+T_{tz}$ | $4$ | $1$ | $1$ | $T_{e_t,\,e_t+e_z}$ |
| $P_+$ | $2$ | $1$ | $1$ | $T_{e_t/2,\,e_t-ie_z}$ |
| $T_{\tilde Q,\tilde P}$ with $\tilde Q,\tilde P\neq0$ and $\langle\tilde Q\rangle_{\natural}=\langle\tilde P\rangle_{\natural}=0$ | $1$ | $1$ | $1$ | by construction |
| $T_{tt}+T_{xx}$ | $2$ | $2$ | $2$ | $T_{e_t,e_t}+T_{e_x,e_x}$ |
| $M_1=(u_2+u_3)(u_2+u_3)^{\mathsf T}$ | $1$ | $4$ | $4$ | $\tfrac12(T_{tt}-T_{xx}+T_{yy}+T_{zz})$ |
| generic $M$ | $4$ | $4$ | $4$ | four terms, none removable |

**How to decide.** Compute the sixteen numbers $\tfrac14\operatorname{Tr}(T_{\mu\nu}^{\dagger}M)$ and form $c$. If $\operatorname{rank}c=1$, take $[Q]$ to be a nonzero column of $c$; choose a nonzero entry $Q_i$ of that column and take $[P]^{\mathsf T}$ to be the $i$-th row of $c$ divided by $Q_i$. If $\operatorname{rank}c=r>1$, a rank factorization $c=UV$ gives the $r$ terms. No test on $\operatorname{rank}M$ alone decides the question.

### The Two One-Sided Boundaries

**The two boundary cases.** The left and right copies are the two boundary cases of the cone:
$$
T_{\tilde Q,e_t}=L^{P}(\tilde Q),\qquad
T_{e_t,\tilde P}=R^{P}(\tilde P).
$$
Both are single products, and both are contained in the cone. Their intersection is the scalars $\mathbb{C}\cdot\mathrm I_4$, by §*The One-Sided Operators*.

**The cone is larger.** A generic pair has neither parameter a scalar multiple of $e_t$, and its operator is neither a left nor a right multiplication. The cone is strictly larger than the union of the two copies. The two copies are four-dimensional linear subspaces inside the seven-dimensional cone, and the cone itself is not a subspace.

**The Hermitian subcone.** The Hermitian sandwich is the subcone $\tilde P=\tilde Q^{*}$, a real seven-dimensional cone inside the complex seven-dimensional cone. It is the subject of Part V and is not developed here.

### $E_{11}$ as a Worked Case

**The matrix.** Let $E_{11}$ be the first matrix unit in the frame. Its coefficient matrix is
$$
c(E_{11})=\frac14
\begin{pmatrix}
1&0&0&i\\
0&0&0&0\\
0&0&0&0\\
i&0&0&-1
\end{pmatrix}
=\frac14\begin{pmatrix}1\\0\\0\\i\end{pmatrix}\begin{pmatrix}1&0&0&i\end{pmatrix}.
$$
It has rank one, so $E_{11}$ is a single product. The factorization reads
$$
[Q]=\frac14\begin{pmatrix}1\\0\\0\\i\end{pmatrix},\qquad
[P]=\begin{pmatrix}1\\0\\0\\i\end{pmatrix},
$$
that is $Q=(e_t+i\vec e_z)/4$ and $P=e_t+i\vec e_z$, and
$$
E_{11}=T_{(e_t+i\vec e_z)/4,\ e_t+i\vec e_z}.
$$

**The check.** The coefficient matrix of the right side is $[Q][P]^{\mathsf T}=c(E_{11})$, and the expansion in the basis $T_{\mu\nu}$ is unique, so the two matrices are equal. Direct multiplication in the frame confirms the identity entry by entry: the only nonzero entry of $E_{11}$ is the $(1,1)$ entry, and the product $T_{Q,P}$ has the same matrix.

**The reading.** $E_{11}$ has matrix rank one and length one. The two ranks agree here, but they need not: the matrix $M_1$ above has matrix rank one and length four, and $P_+$ has matrix rank two and length one. The length is read from the coefficient matrix, not from the matrix rank. The example also shows that a matrix unit is a product, and that its factors can be null: $e_t+i\vec e_z$ has quaternionic norm zero.

**Where the frame question is answered.** The coefficient array $c(M)$ is computed from the sixteen products of four *basis elements*, so its entries move with the frame while its rank does not: a change of the element basis sends $c$ to $C^{-1}cC^{-\mathsf T}$, and a change of the display alone leaves $c$ untouched. The proof, the two frames of the corpus and the sixteen lengths of the matrix units are §*The Change of Frame Is a Congruence* and §*The Sixteen Lengths* of *$M_4(\mathbb{C})$ Standard Peirce Representation : The Matrix Product, the Trace and the Determinant*. What the length theorem needs from that is one line: the rank of a congruence is the rank of the array.

## The Plain Adjoint and the Types

**The plain form.** On $\mathbb{B}$ use the plain bilinear form
$$
\langle X,Y\rangle=\mathrm{Sc}(XY).
$$
Its Gram matrix in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ is $\operatorname{diag}(1,-1,-1,-1)$, and the form is non-degenerate and symmetric. It is not positive definite, and it is not the Hilbert–Schmidt form on the matrix model.

**The adjoint.** The adjoint of a two-sided operator is the swap of the two parameters:
$$
\bigl(T_{\tilde Q,\tilde P}\bigr)^{\approx}=T_{\tilde P,\tilde Q}.
$$
The proof is the cyclicity of the scalar part:
$$
\bigl\langle T_{\tilde Q,\tilde P}X,Y\bigr\rangle
=\mathrm{Sc}(\tilde QX\tilde PY)
=\mathrm{Sc}(X\tilde PY\tilde Q)
=\bigl\langle X,T_{\tilde P,\tilde Q}Y\bigr\rangle.
$$
The adjoint exchanges the two slots and conjugates neither parameter.

**The self-adjoint pairs.** For $\tilde Q\neq0$,
$$
\bigl(T_{\tilde Q,\tilde P}\bigr)^{\approx}=T_{\tilde Q,\tilde P}
\iff
\tilde P=\lambda\tilde Q
\quad\text{for some }\lambda\in\mathbb{C}.
$$
The self-adjoint two-sided operators are the scalar multiples of the diagonal operators $T_{\tilde Q,\tilde Q}$, together with the zero operator. The proof writes $A=\mathsf M_2(\tilde Q)$ and $B=\mathsf M_2(\tilde P)$ and tests $AXB=BXA$ on the matrix units; it uses no inverse and covers the zero divisors.

**The skew sector.** No nonzero two-sided operator is skew-adjoint:
$$
\bigl(T_{\tilde Q,\tilde P}\bigr)^{\approx}=-T_{\tilde Q,\tilde P}
\iff
T_{\tilde Q,\tilde P}=0.
$$
The plain form has a self-adjoint sector and no skew-adjoint sector among the nonzero products.

**The isometries.** The operator preserves the plain form,
$$
\bigl\langle T_{\tilde Q,\tilde P}X,T_{\tilde Q,\tilde P}Y\bigr\rangle
=\langle X,Y\rangle
\quad\text{for all }X,Y,
$$
exactly when
$$
\tilde P\tilde Q=\pm e_t .
$$
Then $\tilde Q$ is a unit and $\tilde P=\pm\tilde Q^{-1}$, and the operator is $\pm\mathrm{Ad}_{\tilde Q}$, where $\mathrm{Ad}_{\tilde Q}(X)=\tilde Q X\tilde Q^{-1}$ is the inner automorphism. The isometry group is
$$
\{\pm\mathrm{Ad}_{\tilde Q}\}\cong(\mathbb{B}^{\times}/\mathbb{C}^{\times})\times\{\pm1\},
$$
of complex dimension three. It is not the full orthogonal group, which has dimension six.

**The multiplicative members.** A nonzero operator $T_{\tilde Q,\tilde P}$ is multiplicative,
$$
T_{\tilde Q,\tilde P}(XY)=T_{\tilde Q,\tilde P}(X)T_{\tilde Q,\tilde P}(Y)
\quad\text{for all }X,Y,
$$
exactly when
$$
\tilde P\tilde Q=e_t .
$$
Then $\tilde P=\tilde Q^{-1}$ and $T_{\tilde Q,\tilde P}=\mathrm{Ad}_{\tilde Q}$, an automorphism of the algebra. The zero operator is multiplicative but is excluded by the nonzero condition.

**No pin group.** The quadratic form $\mathfrak{Q}(\tilde Q)=\mathrm{Sc}(\tilde Q^2)$ is not multiplicative. For example,
$$
\mathfrak{Q}\!\left(\frac{5e_t+4\vec e_x}{3}\right)
=\mathfrak{Q}\!\left(\frac{5e_t+4\vec e_y}{3}\right)=1,
\qquad
\mathfrak{Q}\!\left(\frac{(5e_t+4\vec e_x)(5e_t+4\vec e_y)}{9}\right)
=-\frac{431}{81}.
$$
The level set $\{\mathfrak{Q}=\pm1\}$ is not closed under multiplication, and no scalar condition on one parameter cuts a subgroup out of the family. The isometry group of the family is only $\{\pm\mathrm{Ad}_{\tilde Q}\}$, of complex dimension three; it is not a pin group. The isometry condition is a condition on the pair, $\tilde P\tilde Q=\pm e_t$, not on either parameter alone.

**The two adjoints.** The coefficient formula uses the Hilbert–Schmidt adjoint $\dagger$ of the $4\times4$ matrix; the plain adjoint $\approx$ is the adjoint for the form $\mathrm{Sc}(XY)$ on $\mathbb{B}$. They are different involutions. The identity $(T_{\tilde Q,\tilde P})^{\approx}=T_{\tilde P,\tilde Q}$ is a statement about the operator, not about the coefficient matrix.

## The Structural Reading

**The enveloping algebra.** The map
$$
\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}
\longrightarrow\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\qquad
\tilde Q\otimes\tilde P^{\mathrm{opp}}
\longmapsto L^{P}(\tilde Q)R^{P}(\tilde P)
$$
is an isomorphism of complex algebras. The sixteen elementary tensors $e_\mu\otimes e_\nu^{\mathrm{opp}}$ map to the sixteen matrices $T_{\mu\nu}$, which are a basis; the isomorphism is the generation theorem in algebra form.

**The pure tensors.** Under this isomorphism the two-sided operators are exactly the decomposable tensors $\tilde Q\otimes\tilde P^{\mathrm{opp}}$, that is the image of the Segre cone $\mathbb{P}^3\times\mathbb{P}^3$ in $\mathbb{P}^{15}$. The abstract identity $T_{\tilde Q,\tilde P}=L^{P}(\tilde Q)R^{P}(\tilde P)$ is the same statement as "the element is a pure tensor in $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}$". The seven-dimensional cone of §*The Criterion for a Single Product* is exactly the cone of pure tensors inside the sixteen-dimensional algebra.

## What the Factorization Buys and Does Not

**It gives.**
- An explicit parametrisation by two biquaternions, eight complex parameters modulo the $\mathbb{C}^{\times}$ scaling, hence seven effective parameters.
- A product formula, hence powers, inverses and the monoid structure.
- A rank-one coefficient criterion, hence a decisive test for "is this matrix a single two-sided operator?"
- The length formula $\ell(M)=\operatorname{rank}c(M)$ with $0\le\ell(M)\le4$.
- The commutant of one element: $M_2\otimes\mathbb{C}[A]$, of dimension eight, and a minimal polynomial of degree two.
- The plain adjoint and the type criteria: $(T_{\tilde Q,\tilde P})^{\approx}=T_{\tilde P,\tilde Q}$; self-adjoint exactly when $\tilde P=\lambda\tilde Q$; isometry exactly when $\tilde P\tilde Q=\pm e_t$; multiplicative exactly when $\tilde P\tilde Q=e_t$.

**It does not give.**
- Additivity: the set is not a subspace, and the sum of two products is generally not a product.
- Universality: not every matrix is a single product; four products may be needed, and four are always enough.
- A division algebra: the basis matrices are invertible, but the span has zero divisors, for example $T_{tt}+T_{xx}$ of rank two.
- A pin group: the quadratic form $\mathrm{Sc}(\tilde Q^2)$ is not multiplicative, and the isometry group of the family is only $\{\pm\mathrm{Ad}_{\tilde Q}\}$, of complex dimension three, with no skew-adjoint sector.

## Open Questions

- The classification of Clifford frames in $M_4(\mathbb{C})$: is every frame of the normal form above, and what is the stabiliser of the cell frame?
- The choice of frame as a choice of Clifford structure: which gradings the algebra admits, and how they are related.
- A dictionary, frame by frame, between the explicit matrix frames of the physics articles and the tensor basis. The corpus has many explicit representations, and they need not use the same pair $(\beta,\delta)$.
- Which physical statements are frame-independent, and which are artefacts of a table. The mass bilinear, the axial current and the chiral projectors are the first candidates.
- The sign of the pseudoscalar cell and the choice of the second central root of $-1$; the two conventions must not be mixed inside one computation.
- The Peirce image of a general frame, and the spinor-basis change that relates two frames.
- The Segre length in physics: the matrices of length at most $r$ are the locus $\operatorname{rank}c\le r$, cut out by the $(r+1)\times(r+1)$ minors; what is not known is which physical operators have length two or three, and why.
- The two-sided Dirac operator against the left gradient: the dictionary at the level of differential operators, not only of matrices.

## Summary

The operators on the biquaternion algebra sit at three levels. Every endomorphism has a matrix in $M_4(\mathbb{C})$, and the frame gives an isomorphism of sixteen-dimensional algebras. The one-sided operators fill the two four-dimensional copies $\mathbb{B}_L=\{\mathrm I_2\otimes A\}$ and $\mathbb{B}_R=\{B^{\mathsf T}\otimes\mathrm I_2\}$; their intersection is the scalars and each is the commutant of the other. The two-sided operators are the products $T_{\tilde Q,\tilde P}=L^{P}(\tilde Q)R^{P}(\tilde P)=B^{\mathsf T}\otimes A$.

The sixteen products $T_{\mu\nu}=L_\mu^{P}R_\nu^{P}$ are an orthogonal basis of $M_4(\mathbb{C})$, of Hilbert–Schmidt norm two. They compose up to sign with the second slot reversed, their trace is $4Q_tP_t$, and their determinant is $\langle\tilde Q\rangle_{\natural}^2\langle\tilde P\rangle_{\natural}^2$. Every basis matrix is a unit of determinant one and rank four; the span is not a division algebra, since $T_{tt}+T_{xx}$ has rank two. In the Peirce frame each of the sixteen is a monomial matrix, with one nonzero entry in each row and column, of modulus one; the first row is the right family and the first column the left family.

The Pauli evaluation is $T_{\tilde Q,\tilde P}=\mathsf M_2(\tilde P)^{\mathsf T}\otimes\mathsf M_2(\tilde Q)$, a $4\times4$ Kronecker product of two $2\times2$ matrices. The Kronecker product of two $4\times4$ matrices is $16\times16$ and is not the operator; the matrix of the operator is the ordinary product $L^{P}(\tilde Q)R^{P}(\tilde P)$.

The frame is generated by a pair $(\beta,\delta)$ of orthogonal spatial directions. The reference pair $(e_y,e_x)$ gives five cell multiples; a general pair gives five single products of coefficient rank one, spread over several cells. Nothing selects the pair, and the normal form is a slice through the set of frames, not a conjugacy class. The chiral reading is the pseudoscalar cell $iT_{e_t,\beta\delta}$, with eigenvalues $\pm1$, the projectors $P_\pm=T_{e_t/2,e_t\pm i\beta\delta}$, and the two Weyl blocks exchanged by the four generators. The left regular model cannot hold the Dirac algebra.

The product set is the seven-dimensional Segre cone of pure tensors in $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}=M_4(\mathbb{C})$. It is not a subspace. The factorisation map has eight parameters, one scaling orbit, and the zero operator as vertex. The coefficient matrix $c(M)$ turns the product condition into the rank condition $\operatorname{rank}c(M)\le1$. The length is the coefficient rank, $\ell(M)=\operatorname{rank}c(M)$, and it takes the values $0,1,2,3,4$; every matrix is a sum of at most four products, and a generic matrix needs four. The matrix rank of a product is in $\{0,1,2,4\}$ and is independent of the length: matrix rank one can have length four, and matrix rank two can have length one. The matrix unit $E_{11}$ has rank one and length one, and all sixteen units have length one in this frame and length four in the e-basis, because the two arrays name different operators. The length is frame-invariant: a change of the element basis sends $c$ to $C^{-1}cC^{-\mathsf T}$, of the same rank, and a change of the display alone leaves $c$ unchanged.

The plain adjoint swaps the two parameters, and the type criteria are $\tilde P=\lambda\tilde Q$ for self-adjoint, $\tilde P\tilde Q=\pm e_t$ for isometry and $\tilde P\tilde Q=e_t$ for multiplicative. The isometry group is $\{\pm\mathrm{Ad}_{\tilde Q}\}$, of complex dimension three, and it is not a pin group.

In one line: every two-sided operator is a single product of one left and one right multiplication; the set of such products is the seven-dimensional cone of pure tensors, characterised by a rank-one coefficient matrix, closed under composition but not under addition, with length the coefficient rank and matrix rank in $\{0,1,2,4\}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, $\dim_{\mathbb{C}}=4$ |
| $\mathcal{P}=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$ | the standard Peirce frame |
| $\mathsf S$ | the permutation of the second and third coordinates; $R^{P}(\tilde Q)=\mathsf S L^{P}(\tilde Q)^{\mathsf T}\mathsf S^{-1}$ |
| $L^{P}(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q)$ | the left matrix |
| $R^{P}(\tilde P)=\mathsf M_2(\tilde P)^{\mathsf T}\otimes\mathrm I_2$ | the right matrix |
| $L_\mu^{P}=L^{P}(e_\mu)$, $R_\nu^{P}=R^{P}(e_\nu)$ | the four basis matrices of each copy |
| $T_{\tilde Q,\tilde P}=L^{P}(\tilde Q)R^{P}(\tilde P)$ | the two-sided operator, $X\mapsto\tilde QX\tilde P$ |
| $T_{\mu\nu}=L_\mu^{P}R_\nu^{P}$ | the sixteen basis matrices |
| $[Q]=(Q_t,Q_x,Q_y,Q_z)^{\mathsf T}$ | the coefficient column of $\tilde Q$ |
| $\mathsf M_2(\tilde Q)$ | the $2\times2$ model, $\det=\langle\tilde Q\rangle_{\natural}$ |
| $\sigma_1,\sigma_2,\sigma_3$ | the Pauli matrices, $\mathsf M_2(\vec e_k)=-i\sigma_k$ |
| $c(M)$ | the coefficient matrix, $c(M)_{\mu\nu}=\tfrac14\operatorname{Tr}(T_{\mu\nu}^{\dagger}M)$ |
| $\ell(M)$ | the least number of products summing to $M$; equal to $\operatorname{rank}c(M)$ |
| $\Phi(\tilde Q,\tilde P)=T_{\tilde Q,\tilde P}$ | the factorisation map |
| $\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ | the quaternionic norm, $\det\mathsf M_2(\tilde Q)$ |
| $\tilde Q^{\natural}=Q_t-\vec Q$ | the natural conjugate |
| $\tilde Q^{*}=\bar{\tilde Q}^{\natural}$ | the Hermitian conjugate |
| $\mathrm{Ad}_{\tilde Q}(X)=\tilde Q X\tilde Q^{-1}$ | the inner automorphism |
| $\mathbb{B}^{\mathrm{opp}}$ | the opposite algebra, with the reversed product |
| $\beta,\delta$ | the two right directions of a frame, $\beta^2=\delta^2=-e_t$, $\beta\delta=-\delta\beta$ |
| $T_{e_t,\beta\delta}$ | the pseudoscalar cell, the fifth generator of the frame |
| $\Sigma_{\mu\nu}$ | the Lorentz generators, six even cells |
| $P_\pm=T_{e_t/2,e_t\pm i\beta\delta}$ | the chirality projectors |
| $C_{\Pi}$ | the Peirce change from the Peirce frame to the coefficient basis |
| $\mathrm{Sc}$ | the scalar part, the $e_t$ coefficient |
| $\approx$ | the plain adjoint for $\langle X,Y\rangle=\mathrm{Sc}(XY)$ |
| $\dagger$ | the Hilbert–Schmidt adjoint of a $4\times4$ matrix |
| $\operatorname{rank}$ | the matrix rank, on matrices and on $c(M)$ |

## Further Reading

- [$M_4(\mathbb{C})$ Standard Peirce Representation](m4c-standard-peirce-representation-the-matrix-product-the-trace-and-the-determinant.html), for the frame, the left and right matrices and the six subspaces.
- [$M_2(\mathbb{C})$ Standard Peirce Representation](m2c-standard-peirce-representation-the-matrix-product-the-trace-and-the-determinant.html), for the compression of the two one-sided actions.
- [$M_2(\mathbb{C})$ Standard Peirce Representation : Operators](m2c-standard-peirce-representation-operators.html), for the same operators compressed to one matrix per side and a pair for the product.
- [$M_4(\mathbb{C})$ e-basis Representation](m4c-e-basis-representation.html), for the same operators in the e-basis.
- [$M_4(\mathbb{C})_{\mathcal{T}}$ Representation : The Two-Sided Operators on the Biquaternion Algebra](m4c-representation-the-two-sided-operators-on-the-biquaternion-algebra.html), for the same family in the canonical frame.
- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the abstract family, the generation theorem, the composition, the adjoint and the type criteria.
- [$M_4(\mathbb{C})$ Representation : The General Endomorphisms](m4c-representation-the-general-endomorphisms.html), for the Peirce change $C_{\Pi}$ and the operator-space matrix units.
- [The Matrix Algebra $M_4(\mathbb{C})$](the-matrix-algebra-m4c.html), for the construction of $M_4(\mathbb{C})$ from the sandwich map and the change to the matrix-unit basis.
- [$M_4(\mathbb{C})_{\mathbb{B}_L}$ Representation : The Left Regular Operators on the Biquaternion Algebra](m4c-representation-the-left-regular-operators-on-the-biquaternion-algebra.html), for $L^{P}$ and the four left matrices.
- [$M_4(\mathbb{C})_{\mathbb{B}_R}$ Representation : The Right Regular Operators on the Biquaternion Algebra](m4c-representation-the-right-regular-operators-on-the-biquaternion-algebra.html), for $R^{P}$ and the four right matrices.
- [The Endomorphisms of the Biquaternion Algebra](the-endomorphisms-of-the-biquaternion-algebra.html), for the ambient operator space and its coordinate column.
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for the algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$ and the pure tensors.
- [The Commutant of the Two Regular Families](the-commutant-of-the-two-regular-families.html), for the intersection of the two one-sided copies.
- [The Four Adjoints of the Biquaternion Algebra in Examples](the-four-adjoints-of-the-biquaternion-algebra-in-examples.html), for the plain adjoint and its comparison with the other adjoints.
- [The Hermitian Sandwich: Definition and Multiplicativity](the-hermitian-sandwich-definition-and-multiplicativity.html), for the real subcone $\tilde P=\tilde Q^{*}$.
- [Matrix Representations Conventions](conventions-of-the-matrix-models.html), for the $2\times2$ unit images, the four left and four right matrices, the exchange $\mathsf S$ and the sixteen cells entry by entry.
- [Conventions of the Matrix Models](../articles_physics/conventions-of-the-matrix-models.html), for the explicit chiral matrices of one frame, the Peirce match and the chirality.

## Appendix — The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a separate algebra; the body writes the cells.

### The gamma frame

#### The five cells

**The reference frame.** Define
$$
\gamma_0=iT_{e_t,e_x},\qquad
\gamma_1=iT_{e_x,e_y},\qquad
\gamma_2=iT_{e_y,e_y},\qquad
\gamma_3=iT_{e_z,e_y},\qquad
\gamma_5=-iT_{e_t,e_z}.
$$
Each is a unit multiple of one cell of the sixteen, and each is a single two-sided operator. In the Pauli evaluation,
$$
\gamma_0=\sigma_1\otimes\mathrm I_2,\qquad
\gamma_k=i\,\sigma_2\otimes\sigma_k,\qquad
\gamma_5=-\sigma_3\otimes\mathrm I_2.
$$

**The values.** In the frame,
$$
\gamma_0=\begin{pmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
\gamma_1=\begin{pmatrix}0&0&0&1\\0&0&1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix},
$$
$$
\gamma_2=\begin{pmatrix}0&0&0&-i\\0&0&i&0\\0&i&0&0\\-i&0&0&0\end{pmatrix},\qquad
\gamma_3=\begin{pmatrix}0&0&1&0\\0&0&0&-1\\-1&0&0&0\\0&1&0&0\end{pmatrix},
$$
$$
\gamma_5=\begin{pmatrix}-1&0&0&0\\0&-1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}.
$$
Each has trace $0$, determinant $1$ and rank $4$. The five are unit multiples of five cells of the table of §*The Table in Four Families*; the choice of the five is the choice of a frame.

**The cells.** The five are supported on single cells because the pair of directions is a pair of coordinate axes; a general frame of the normal form below is not supported on cells. The cell property is a property of the pair, not of the construction.

#### The normal form and the Pair $(\beta,\delta)$

**The pair.** Let $\beta,\delta$ be unit spatial directions, orthogonal:
$$
\beta^2=\delta^2=-e_t,\qquad \beta\delta=-\delta\beta.
$$
Define
$$
\gamma_0=iL^{P}(e_t)R^{P}(\delta),\qquad
\gamma_k=iL^{P}(e_k)R^{P}(\beta),\qquad k=x,y,z.
$$
For the reference frame $(\beta,\delta)=(e_y,e_x)$, the five are the cells of §*The Five Cells*; in that frame $\beta\delta=-e_z$ and $\gamma_5=iT_{e_t,\beta\delta}$.

**The normal form.** Every pair $(\beta,\delta)$ gives a frame with the Clifford relations of §*The Clifford Relations*, and the five operators determine the pair: $\delta$ is the right factor of $\gamma_0$, and $\beta$ is the right factor of $\gamma_1$. Distinct pairs give distinct frames, not two descriptions of one frame.

**The free parameter.** Nothing selects the pair. The relations use only $\beta^2=\delta^2=-e_t$ and $\beta\delta=-\delta\beta$; no Clifford relation mentions $\beta$ or $\delta$. The three spatial directions enter in three roles: $\beta$ as the common right factor of the three spatial generators, $\delta$ as the right factor of the time generator, and $\beta\delta$ as the right factor of the pseudoscalar. The algebra assigns no direction to any role. What changes with the pair is the list of operators, whether they are cells, the sign of $\gamma_5$, and the grade table.

**Cells only for axes.** If $\beta$ is not one of $e_x,e_y,e_z$, the spatial generators are not cells:
$$
\gamma_k=iT_{e_k,\beta}=i\sum_\nu\beta_\nu\,T_{k\nu}
$$
is a single product of coefficient rank one, supported on several cells. If $\delta$ is not a coordinate axis, $\gamma_0$ is not a cell either. The cell table of §*The Sixteen Products of the Frame* is the table of the reference pair.

**Conjugacy.** For a unit $\tilde u$ and $U=L^{P}(\tilde u)R^{P}(\tilde u^{-1})$,
$$
U\,T_{\tilde Q,\tilde P}\,U^{-1}=T_{\tilde u\tilde Q\tilde u^{-1},\ \tilde u\tilde P\tilde u^{-1}}.
$$
This is the matrix of an inner automorphism, and it carries frames to frames. It does not preserve the normal form, because it rotates the left factors as well as the right factors; the normal form is a slice through the set of frames, not a conjugacy class.

#### The Clifford relations

**Theorem (the Clifford relations).** For the normal form of §*The Normal Form and the Pair $(\beta,\delta)$*,
$$
\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}\mathrm I_4,\qquad
(\gamma_5)^2=\mathrm I_4,\qquad
\gamma_5\gamma_\mu=-\gamma_\mu\gamma_5,
$$
with $g=\operatorname{diag}(1,-1,-1,-1)$, and
$$
\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3=iT_{e_t,\beta\delta}.
$$

*Proof.* $(\gamma_0)^2=-R^{P}(\delta^2)=\mathrm I_4$; $(\gamma_k)^2=-L^{P}(e_k^2)R^{P}(\beta^2)=-\mathrm I_4$; $\gamma_0\gamma_k+\gamma_k\gamma_0=-L^{P}(e_k)(R^{P}(\delta\beta)+R^{P}(\beta\delta))=0$; $\gamma_j\gamma_k+\gamma_k\gamma_j=-L^{P}(e_je_k+e_ke_j)R^{P}(\beta^2)=0$. For the pseudoscalar, the left factor is $L^{P}(e_te_xe_ye_z)=L^{P}(-e_t)$ and the right factor is $R^{P}(\beta^3\delta)=R^{P}(-\beta\delta)$; the two signs cancel, so the product is $T_{e_t,\beta\delta}$.

#### The sixteen products of the frame

**The table.** In the reference frame the products of the five are the sixteen cells up to units.

| Grade | Product | Cell | Coefficient |
|---|---|---|---|
| $0$ | $1$ | $T_{tt}$ | $1$ |
| $1$ | $\gamma_0$ | $T_{tx}$ | $i$ |
| $1$ | $\gamma_1$ | $T_{xy}$ | $i$ |
| $1$ | $\gamma_2$ | $T_{yy}$ | $i$ |
| $1$ | $\gamma_3$ | $T_{zy}$ | $i$ |
| $2$ | $\gamma_0\gamma_1$ | $T_{xz}$ | $1$ |
| $2$ | $\gamma_0\gamma_2$ | $T_{yz}$ | $1$ |
| $2$ | $\gamma_0\gamma_3$ | $T_{zz}$ | $1$ |
| $2$ | $\gamma_1\gamma_2$ | $T_{zt}$ | $1$ |
| $2$ | $\gamma_1\gamma_3$ | $T_{yt}$ | $-1$ |
| $2$ | $\gamma_2\gamma_3$ | $T_{xt}$ | $1$ |
| $3$ | $\gamma_0\gamma_1\gamma_2$ | $T_{zx}$ | $i$ |
| $3$ | $\gamma_0\gamma_1\gamma_3$ | $T_{yx}$ | $-i$ |
| $3$ | $\gamma_0\gamma_2\gamma_3$ | $T_{xx}$ | $i$ |
| $3$ | $\gamma_1\gamma_2\gamma_3$ | $T_{ty}$ | $-i$ |
| $4$ | $\gamma_0\gamma_1\gamma_2\gamma_3$ | $T_{tz}$ | $-1$ |

The products are distinct, so they are the sixteen cells in some order, each with a coefficient in $\{1,-1,i,-i\}$. The table is the multiplication table of the frame read in the cell basis.

**The algebra.** The relations identify the span of the five with the Clifford algebra $\mathrm{Cl}_{1,3}(\mathbb{C})$; the sixteen products are a basis of $M_4(\mathbb{C})$. The Lorentz generators are the six commutators
$$
\Sigma_{\mu\nu}=\tfrac{i}{2}[\gamma_\mu,\gamma_\nu],
$$
which are again cells: $\Sigma^{01}=iT_{xz}$, $\Sigma^{02}=iT_{yz}$, $\Sigma^{03}=iT_{zz}$, $\Sigma^{12}=iT_{zt}$, $\Sigma^{13}=-iT_{yt}$, $\Sigma^{23}=iT_{xt}$. They are even, of grade two, and they generate the spinor representation of $\mathfrak{so}(1,3)$ on $\mathbb{B}\cong\mathbb{C}^4$.

#### The chiral reading

**The pseudoscalar.** In the frame,
$$
\gamma_5=\operatorname{diag}(-1,-1,1,1).
$$
Its two eigenspaces are the two chiral blocks, each of complex dimension two. The four generators exchange them; the pseudoscalar is their sign.

**The projectors.** The chirality projectors are
$$
P_\pm=\tfrac12(\mathrm I_4\pm\gamma_5)=\tfrac12\bigl(T_{tt}\pm iT_{e_t,\beta\delta}\bigr)=T_{e_t/2,\ e_t\pm i\beta\delta}.
$$
In the frame $P_+=\operatorname{diag}(0,0,1,1)$ and $P_-=\operatorname{diag}(1,1,0,0)$. Both have rank two, and the second parameter has quaternionic norm zero. They are single two-sided operators, but not cells: a single product can be singular, and a single product need not be a cell.

**The two Weyl blocks.** The frame is block diagonal for the left family, $L^{P}(\tilde Q)=\operatorname{diag}(\mathsf M_2(\tilde Q),\mathsf M_2(\tilde Q))$, so the left image preserves the two chiral blocks. The four generators are not in the left image: they exchange the blocks. The Dirac algebra needs the two-sided operators; the left regular model cannot hold it.

**Types.** In the reference frame, $\gamma_0$ and $\gamma_5$ lie in the right family $\mathbb{B}_R$, because their left factor is $e_t$; the three spatial generators lie in neither one-sided family. The distinction is a property of the pair, not of the Clifford relations.

Over $\mathbb{R}$ the dictionary is complex-linear: the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.
