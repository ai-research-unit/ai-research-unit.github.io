# __$M_4(\mathbb{C})_{\mathcal{T}}$ Representation : The Two-Sided Operators on the Biquaternion Algebra__

## Introduction

**The model.** The biquaternion algebra $\mathbb{B}$ is a complex vector space of dimension four, and the canonical frame identifies it with $\mathbb{C}^4$. Left multiplication by $\tilde Q$ is the $4\times4$ matrix $L_{\tilde Q}=\mathsf M_4^{L}(\tilde Q)$ of *$M_4(\mathbb{C})_{\mathbb{B}_L}$ Representation : The Left Regular Operators on the Biquaternion Algebra*; right multiplication is the $4\times4$ matrix $R_{\tilde Q}$ of *$M_4(\mathbb{C})_{\mathbb{B}_R}$ Representation : The Right Regular Operators on the Biquaternion Algebra*. This article computes the matrix side of the two-sided operators of *Two-Sided Operators on the Biquaternion Algebra*:

$$
T_{\tilde Q,\tilde P}=L_{\tilde Q}R_{\tilde P},\qquad T_{\tilde Q,\tilde P}(X)=\tilde QX\tilde P .
$$

**The sixteen matrices.** For $\mu,\nu\in\{t,x,y,z\}$ the sixteen matrices

$$
T_{\mu\nu}=L_\mu R_\nu
$$

are the sixteen basis matrices of the family. They are a basis of $M_4(\mathbb{C})$, by the generation theorem of *Two-Sided Operators on the Biquaternion Algebra*, §*The Sixteen Products as a Basis*. The article records their table in four families, their composition, their trace and determinant, and their orthogonality; then it answers the Kronecker question, builds one gamma frame, and reads the cone of products through the coefficient matrix.

**The Kronecker question.** Three products must be kept apart. The ordinary product $L_{\tilde Q}R_{\tilde P}$ of two $4\times4$ matrices is the matrix of the operator. The Kronecker product of two $2\times2$ matrices is a $4\times4$ matrix and is the evaluation of the ordinary product in the model $\mathbb{B}\cong M_2(\mathbb{C})$. The Kronecker product of two $4\times4$ matrices is a $16\times16$ matrix acting on $\mathbb{C}^4\otimes\mathbb{C}^4$; it is not the operator, and it is not the construction.

**The gamma frame.** The article records one frame, not the frame. The five Dirac generators are unit multiples of five cells in a reference frame; the general normal form is indexed by a pair $(\beta,\delta)$ of orthogonal spatial directions, and nothing in the Clifford relations selects the pair. The frame is a slice through the set of frames, not a conjugacy class.

**The cone of products.** Every $M\in M_4(\mathbb{C})$ has a unique coefficient matrix $c(M)$ in the basis $T_{\mu\nu}$. The matrix $M$ is a single two-sided operator exactly when $c(M)$ has rank at most one; the least number of products summing to $M$ is $\operatorname{rank}c(M)$; every matrix is a sum of at most four products. The product set is the cone over the Segre variety $\mathbb{P}^3\times\mathbb{P}^3$, of complex dimension seven, inside the complex sixteen-dimensional algebra.

**Boundaries.** The abstract family, its composition, its adjoint and its criteria are *Two-Sided Operators on the Biquaternion Algebra*. The left and right matrices are the two matrix articles of Parts II and III. The Peirce change $C_{\Pi}$ and the operator-space matrix units are *$M_4(\mathbb{C})$ Representation : The General Endomorphisms*. The canonical frame and the left matrices are *$M_4(\mathbb{C})_{\mathbb{B}_L}$ Model : The Product, the Trace and the Determinant*. The Hermitian sandwich is Part V and is not treated here.

**Conventions.** The basis is $e_t,\vec e_x,\vec e_y,\vec e_z$; the canonical frame is the Peirce frame $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$; a matrix written without a superscript is in the canonical frame. The coefficient coordinates are $(t,x,y,z)$; the quaternionic norm is $\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$, the determinant of $\mathsf M_2(\tilde Q)$. The Pauli matrices are $\sigma_1,\sigma_2,\sigma_3$; the $2\times2$ model is $\mathsf M_2(\tilde Q)$. The exchange $\mathsf S$ is the involution of the carrier that fixes $\tilde\Pi_\pm$ and exchanges $\vec\Upsilon_+,\vec\Upsilon_-$; in the canonical frame it is the permutation of the second and third coordinates, and $R_{\tilde Q}=\mathsf S L_{\tilde Q}^{\mathsf T}\mathsf S^{-1}$.

## The Sixteen Matrices $T_{\mu\nu}=L_\mu R_\nu$

### The Table in Four Families

**Definition.** For $\mu,\nu\in\{t,x,y,z\}$,

$$
T_{\mu\nu}=L_\mu R_\nu,\qquad L_\mu=L_{e_\mu},\quad R_\nu=R_{e_\nu}.
$$

The matrix $T_{\mu\nu}$ is the matrix of $X\mapsto e_\mu Xe_\nu$. A general two-sided operator is the linear combination

$$
T_{\tilde Q,\tilde P}=\sum_{\mu,\nu}Q_\mu P_\nu\,T_{\mu\nu}.
$$

**The table.** The sixteen matrices fall into the four families

| | $\nu=t$ | $\nu=x$ | $\nu=y$ | $\nu=z$ |
|---|---|---|---|---|
| $\mu=t$ | $T_{tt}=\mathrm I_4$ | $T_{tx}=R_x$ | $T_{ty}=R_y$ | $T_{tz}=R_z$ |
| $\mu=x$ | $T_{xt}=L_x$ | $T_{xx}=L_xR_x$ | $T_{xy}=L_xR_y$ | $T_{xz}=L_xR_z$ |
| $\mu=y$ | $T_{yt}=L_y$ | $T_{yx}=L_yR_x$ | $T_{yy}=L_yR_y$ | $T_{yz}=L_yR_z$ |
| $\mu=z$ | $T_{zt}=L_z$ | $T_{zx}=L_zR_x$ | $T_{zy}=L_zR_y$ | $T_{zz}=L_zR_z$ |

The first row is the right family, the first column the left family, the diagonal entry $T_{tt}$ the identity, and the remaining nine the genuinely two-sided cells. The table is the matrix form of the four families of *Two-Sided Operators on the Biquaternion Algebra*, §*The Operator $T_{\tilde Q,\tilde P}$*.

**The Pauli evaluation.** In the $2\times2$ model,

$$
L_{\tilde Q}=\mathrm I_2\otimes\mathsf M_2(\tilde Q),\qquad
R_{\tilde P}=\mathsf M_2(\tilde P)^{\mathsf T}\otimes\mathrm I_2,
$$

so that

$$
T_{\tilde Q,\tilde P}=\mathsf M_2(\tilde P)^{\mathsf T}\otimes\mathsf M_2(\tilde Q).
$$

On the four families this reads

$$
T_{tt}=\mathrm I_4,\qquad
T_{tk}=-i\,\sigma_k^{\mathsf T}\otimes\mathrm I_2,\qquad
T_{kt}=-i\,\mathrm I_2\otimes\sigma_k,\qquad
T_{jk}=-\sigma_k^{\mathsf T}\otimes\sigma_j,
$$

with $j,k\in\{x,y,z\}$ and $\mathsf M_2(e_k)=-i\sigma_k$. The evaluation is a $4\times4$ Kronecker product of two $2\times2$ matrices; it is not a $4\times4$ Kronecker product of two $4\times4$ matrices, and §*The Kronecker Question* separates the two.

**One entry.** The table gives $T_{xy}=L_xR_y=L_x\mathsf S L_y^{\mathsf T}\mathsf S^{-1}$,
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

**The basis.** The sixteen matrices are linearly independent and span $M_4(\mathbb{C})$, by *Two-Sided Operators on the Biquaternion Algebra*, §*The Sixteen Products as a Basis*. The expansion of a general matrix in this basis is unique, and the coefficient matrix is the subject of §*The Cone of Products*.

### Composition, Trace, Determinant

**Composition.** The product of two basis matrices is a signed basis matrix:

$$
T_{\mu\nu}T_{\rho\sigma}=T_{e_\mu e_\rho,\ e_\sigma e_\nu}=\epsilon\epsilon'\,T_{\mu'\nu'},
$$

where $e_\mu e_\rho=\epsilon e_{\mu'}$ and $e_\sigma e_\nu=\epsilon' e_{\nu'}$, with $\epsilon,\epsilon'\in\{\pm1\}$. For general parameters,

$$
T_{\tilde Q,\tilde P}T_{\tilde R,\tilde S}=T_{\tilde Q\tilde R,\ \tilde S\tilde P}.
$$

The sixteen are closed under multiplication up to sign, with unit $T_{tt}=\mathrm I_4$; they are not a group, because $-T_{\mu\nu}$ is not one of the sixteen.

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
T_{tt}+T_{xx}=\mathrm I_4+L_xR_x=
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

**The coefficient basis.** In the coefficient basis the same sixteen are the signed permutation matrices $T_{\mu\nu}^{\mathrm{coef}}=C_{\Pi}T_{\mu\nu}C_{\Pi}^{-1}$, with $C_{\Pi}$ the Peirce change of *$M_4(\mathbb{C})$ Representation : The General Endomorphisms*, §*The Change $C_{\Pi}$*. The conjugation changes the entries, not the algebra; the canonical frame is the one in which the gamma construction closes.

## The Kronecker Question

### The Pauli Evaluation

**The two one-sided evaluations.** In the $2\times2$ model,

$$
L_{\tilde Q}=\mathrm I_2\otimes\mathsf M_2(\tilde Q),\qquad
R_{\tilde P}=\mathsf M_2(\tilde P)^{\mathsf T}\otimes\mathrm I_2.
$$

The first factor of $L_{\tilde Q}$ is the copy index, the second the spinor index; the right matrix acts on the copy index and is the transpose of the left matrix of $\tilde P$, in the exchanged frame. The product is

$$
T_{\tilde Q,\tilde P}=L_{\tilde Q}R_{\tilde P}
=\mathsf M_2(\tilde P)^{\mathsf T}\otimes\mathsf M_2(\tilde Q).
$$

**On the basis.** With $\mathsf M_2(e_k)=-i\sigma_k$,

$$
T_{tk}=-i\,\sigma_k^{\mathsf T}\otimes\mathrm I_2,\qquad
T_{kt}=-i\,\mathrm I_2\otimes\sigma_k,\qquad
T_{jk}=-\sigma_k^{\mathsf T}\otimes\sigma_j.
$$

The evaluation is a $4\times4$ matrix, the Kronecker product of two $2\times2$ matrices, and it is the ordinary product $L_{\tilde Q}R_{\tilde P}$ written in the model.

### Why the $4\times4$ Kronecker Product Is Not the Operator

**The dimensions.** $L_{\tilde Q}$ and $R_{\tilde P}$ are $4\times4$ matrices. Their Kronecker product $L_{\tilde Q}\otimes R_{\tilde P}$ is a $16\times16$ matrix. It acts on $\mathbb{C}^4\otimes\mathbb{C}^4$, a complex space of dimension sixteen; the operator $T_{\tilde Q,\tilde P}$ acts on $\mathbb{B}\cong\mathbb{C}^4$, of complex dimension four. The two cannot be the same matrix, and the $16\times16$ matrix does not represent the operator on the carrier.

**The correct product.** The matrix of the operator is the ordinary product $L_{\tilde Q}R_{\tilde P}$, of size $4\times4$. The algebra-level construction is the tensor product of algebras

$$
\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\longrightarrow\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\qquad
\tilde Q\otimes\tilde P^{\mathrm{opp}}\longmapsto L_{\tilde Q}R_{\tilde P},
$$

and the sixteen elementary tensors $e_\mu\otimes e_\nu^{\mathrm{opp}}$ map to the sixteen matrices $T_{\mu\nu}$. The Kronecker product of the matrices is a different construction: it is the matrix of the tensor product of the two operators on the tensor product of the carriers, not the matrix of their composite on one carrier.

**The three products.** The ordinary product $L_{\tilde Q}R_{\tilde P}$ is $4\times4$ and is the operator. The Kronecker product of two $2\times2$ matrices is $4\times4$ and is the evaluation of the ordinary product in the model $\mathbb{B}\cong M_2(\mathbb{C})$. The Kronecker product of two $4\times4$ matrices is $16\times16$ and is neither. The three are related by the identifications of the model, not by an equality of matrices.

**The coefficient basis.** In the coefficient basis the sixteen are signed permutation matrices; in the canonical frame they are the products of a left matrix and a right matrix. The Pauli evaluation is a statement in the canonical frame and in the $2\times2$ model; the coefficient basis is the conjugate display. Neither changes the operator.

## The Gamma Frame

### The Five Cells

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

**The values.** In the canonical frame,

$$
\gamma_0=
\begin{pmatrix}
0&0&1&0\\
0&0&0&1\\
1&0&0&0\\
0&1&0&0
\end{pmatrix},
\qquad
\gamma_5=
\begin{pmatrix}
-1&0&0&0\\
0&-1&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix}.
$$

Each has trace $0$, determinant $1$ and rank $4$. The five are unit multiples of five cells of the table of §*The Table in Four Families*; the choice of the five is the choice of a frame.

**The cells.** The five are supported on single cells because the pair of directions is a pair of coordinate axes; a general frame of the normal form below is not supported on cells. The cell property is a property of the pair, not of the construction.

### The Normal Form and the Pair $(\beta,\delta)$

**The pair.** Let $\beta,\delta$ be unit spatial directions, orthogonal:

$$
\beta^2=\delta^2=-e_t,\qquad \beta\delta=-\delta\beta.
$$

Define

$$
\gamma_0=iL_{e_t}R_\delta,\qquad
\gamma_k=iL_{e_k}R_\beta,\qquad k=x,y,z.
$$

For the reference frame $(\beta,\delta)=(e_y,e_x)$, the five are the cells of §*The Five Cells*; in that frame $\beta\delta=-e_z$ and $\gamma_5=iT_{e_t,\beta\delta}$.

**The normal form.** Every pair $(\beta,\delta)$ gives a frame with the Clifford relations of §*The Clifford Relations*, and the five operators determine the pair: $\delta$ is the right factor of $\gamma_0$, and $\beta$ is the right factor of $\gamma_1$. Distinct pairs give distinct frames, not two descriptions of one frame.

**The free parameter.** Nothing selects the pair. The relations use only $\beta^2=\delta^2=-e_t$ and $\beta\delta=-\delta\beta$; no Clifford relation mentions $\beta$ or $\delta$. The three spatial directions enter in three roles: $\beta$ as the common right factor of the three spatial generators, $\delta$ as the right factor of the time generator, and $\beta\delta$ as the right factor of the pseudoscalar. The algebra assigns no direction to any role. What changes with the pair is the list of operators, whether they are cells, the sign of $\gamma_5$, and the grade column.

**Cells only for axes.** If $\beta$ is not one of $e_x,e_y,e_z$, the spatial generators are not cells: $\gamma_k=iT_{e_k,\beta}=i\sum_\nu\beta_\nu T_{k\nu}$ is a single product of coefficient rank one, supported on several cells. If $\delta$ is not a coordinate axis, $\gamma_0$ is not a cell either. The cell table of §*The Clifford Relations* is the table of the reference pair.

**Conjugacy.** For a unit $\tilde u$ and $U=L_{\tilde u}R_{\tilde u^{-1}}$, one has $U T_{\tilde Q,\tilde P}U^{-1}=T_{\tilde u\tilde Q\tilde u^{-1},\tilde u\tilde P\tilde u^{-1}}$. This is the matrix of an inner automorphism, and it carries frames to frames. It does not preserve the normal form, because it rotates the left factors as well as the right factors; the normal form is a slice through the set of frames, not a conjugacy class.

### The Clifford Relations

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

*Proof.* $(\gamma_0)^2=-R_{\delta^2}=\mathrm I_4$; $(\gamma_k)^2=-L_{e_k^2}R_{\beta^2}=-\mathrm I_4$; $\gamma_0\gamma_k+\gamma_k\gamma_0=-L_{e_k}(R_{\delta\beta}+R_{\beta\delta})=0$; $\gamma_j\gamma_k+\gamma_k\gamma_j=-L_{e_je_k+e_ke_j}R_{\beta^2}=0$. For the pseudoscalar, the left factor is $L_{e_te_xe_ye_z}=L_{-e_t}$ and the right factor is $R_{\beta^3\delta}=R_{-\beta\delta}$; the two signs cancel, so the product is $T_{e_t,\beta\delta}$.

**The sixteen products.** In the reference frame the products of the five are the sixteen cells up to units:

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

### The Chiral Reading

**The pseudoscalar.** In the canonical frame,

$$
\gamma_5=\operatorname{diag}(-1,-1,1,1).
$$

Its two eigenspaces are the two chiral blocks, each of complex dimension two. The four generators exchange them; the pseudoscalar is their sign.

**The projectors.** The chirality projectors are

$$
P_\pm=\tfrac12(\mathrm I_4\pm\gamma_5)=\tfrac12\bigl(T_{tt}\pm iT_{e_t,\beta\delta}\bigr)=T_{e_t/2,\ e_t\pm i\beta\delta}.
$$

In the canonical frame $P_+=\operatorname{diag}(0,0,1,1)$ and $P_-=\operatorname{diag}(1,1,0,0)$. Both have rank two, and the second parameter has quaternionic norm zero. They are single two-sided operators, but not cells: a single product can be singular, and a single product need not be a cell.

**The two Weyl blocks.** The canonical frame is block diagonal for the left family, $L_{\tilde Q}=\operatorname{diag}(\mathsf M_2(\tilde Q),\mathsf M_2(\tilde Q))$, so the left image preserves the two chiral blocks. The four generators are not in the left image: they exchange the blocks. The Dirac algebra needs the two-sided operators; the left regular model cannot hold it.

**Types.** In the reference frame, $\gamma_0$ and $\gamma_5$ lie in the right family $R(\mathbb{B})$, because their left factor is $e_t$; the three spatial generators lie in neither one-sided family. The distinction is a property of the pair, not of the Clifford relations.

**The Dirac operator.** With $\partial_\mu=\partial/\partial Q_\mu$,

$$
i\gamma_\mu\partial_\mu=-\bigl(T_{e_t,e_x}\partial_0+T_{e_x,e_y}\partial_1+T_{e_y,e_y}\partial_2+T_{e_z,e_y}\partial_3\bigr).
$$

On $\tilde Q\in\mathbb{B}$,

$$
\tilde Q\longmapsto-\bigl(\partial_0\tilde Q\,e_x+e_x\,\partial_1\tilde Q\,e_y+e_y\,\partial_2\tilde Q\,e_y+e_z\,\partial_3\tilde Q\,e_y\bigr).
$$

The mass term is $-mT_{tt}$. This is the matrix Dirac operator of the frame; it is not the biquaternionic gradient $\tilde\nabla$, which is a left multiplication. The dictionary relates the two; it does not identify them as operators on the same carrier.

## The Cone of Products

### The Coefficient Matrix $c(M)$

**Definition.** By §*The Sixteen Matrices $T_{\mu\nu}=L_\mu R_\nu$*, every $M\in M_4(\mathbb{C})$ has a unique expansion

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

**The two intersections.** The product set meets the left family in the left family and the right family in the right family: $T_{\tilde Q,e_t}=L_{\tilde Q}$ and $T_{e_t,\tilde P}=R_{\tilde P}$. The two intersections are distinct; they meet in the scalars, by *The Commutant of the Two Regular Families*. The product set is larger than either, and the generic product lies in neither.

**The parametrisation.** The map $(\tilde Q,\tilde P)\mapsto T_{\tilde Q,\tilde P}$ is bilinear and surjective onto the cone. Its fibre over a nonzero product is the scaling orbit $(\lambda\tilde Q,\lambda^{-1}\tilde P)$ of *Two-Sided Operators on the Biquaternion Algebra*, §*The Scaling Orbit*; the cone has complex dimension $8-1=7$. The kernel and the image of the Hermitian sandwich are a different question, treated in Part V.

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

### $E_{11}$ as a Worked Case

**The matrix.** Let $E_{11}$ be the first matrix unit in the canonical frame. Its coefficient matrix is

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

**The check.** The coefficient matrix of the right side is $[Q][P]^{\mathsf T}=c(E_{11})$, and the expansion in the basis $T_{\mu\nu}$ is unique, so the two matrices are equal. Direct multiplication in the canonical frame confirms the identity entry by entry: the only nonzero entry of $E_{11}$ is the $(1,1)$ entry, and the product $T_{Q,P}$ has the same matrix.

**The reading.** $E_{11}$ has matrix rank one and length one. The two ranks agree here, but they need not: the matrix $M_1$ above has matrix rank one and length four, and $P_+$ has matrix rank two and length one. The length is read from the coefficient matrix, not from the matrix rank. The example also shows that a matrix unit is a product, and that its factors can be null: $e_t+i\vec e_z$ has quaternionic norm zero.

## Open Questions

- The classification of gamma frames in $M_4(\mathbb{C})$: is every frame of the normal form above, and what is the stabiliser of the cell frame?
- The choice of frame as a choice of Clifford structure: which gradings the algebra admits, and how they are related.
- A dictionary, frame by frame, between the explicit gamma matrices of the physics articles and the tensor basis. The corpus has many explicit representations, and they need not use the same pair $(\beta,\delta)$.
- Which physical statements are frame-independent, and which are artefacts of a table. The mass bilinear, the axial current and the chiral projectors are the first candidates.
- The sign of $\gamma_5$ and the choice of the second central root of $-1$; the two conventions must not be mixed inside one computation.
- The Peirce image of a general frame, and the spinor-basis change that relates two frames.
- The Segre length in physics: the matrices of length at most $r$ are the locus $\operatorname{rank}c\le r$, cut out by the $(r+1)\times(r+1)$ minors; what is not known is which physical operators have length two or three, and why.
- The two-sided Dirac operator against the left gradient: the dictionary at the level of differential operators, not only of matrices.

## Summary

The two-sided operators on $\mathbb{B}$ are the matrices $T_{\tilde Q,\tilde P}=L_{\tilde Q}R_{\tilde P}$, and the sixteen $T_{\mu\nu}=L_\mu R_\nu$ are a basis of $M_4(\mathbb{C})$. They fall into the four families $T_{tt}=\mathrm I_4$, $T_{tk}=R_k$, $T_{kt}=L_k$ and $T_{jk}=L_jR_k$; they compose up to sign, with the second slot reversed; their trace is $4Q_tP_t$, their determinant is $\langle\tilde Q\rangle_{\natural}^2\langle\tilde P\rangle_{\natural}^2$, and they are orthogonal of Hilbert–Schmidt norm two.

The Pauli evaluation is $T_{\tilde Q,\tilde P}=\mathsf M_2(\tilde P)^{\mathsf T}\otimes\mathsf M_2(\tilde Q)$, a $4\times4$ Kronecker product of two $2\times2$ matrices. The Kronecker product of two $4\times4$ matrices is $16\times16$ and is not the operator; the matrix of the operator is the ordinary product $L_{\tilde Q}R_{\tilde P}$.

The gamma frame is generated by a pair $(\beta,\delta)$ of orthogonal spatial directions: $\gamma_0=iL_{e_t}R_\delta$, $\gamma_k=iL_{e_k}R_\beta$, with the Clifford relations $\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}$ and $\gamma_5=iT_{e_t,\beta\delta}$. The reference pair $(e_y,e_x)$ gives five cell multiples; a general pair gives five single products of coefficient rank one, spread over several cells. The frame is a slice, not a conjugacy class; nothing selects the pair. The chiral reading is $\gamma_5=\operatorname{diag}(-1,-1,1,1)$, the two projectors $P_\pm=T_{e_t/2,e_t\pm ie_z}$, and the two Weyl blocks exchanged by the generators. The left regular model cannot hold the Dirac algebra.

Every matrix $M$ has a unique coefficient matrix $c(M)$ with $c_{\mu\nu}=\tfrac14\operatorname{Tr}(T_{\mu\nu}^{\dagger}M)$. The matrix is a single product exactly when $\operatorname{rank}c(M)\le1$, and the least number of products is $\operatorname{rank}c(M)$; every matrix is a sum of at most four, and a generic matrix needs four. The product set is the cone over $\mathbb{P}^3\times\mathbb{P}^3$, of complex dimension seven. Matrix rank and length are independent: $M_1$ has rank one and length four, $P_+$ has rank two and length one, and $E_{11}$ has rank one and length one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\tilde Q}=\mathsf M_4^{L}(\tilde Q)$ | left multiplication, $L_\mu=L_{e_\mu}$ |
| $R_{\tilde Q}$ | right multiplication, $R_\mu=R_{e_\mu}$, $R_{\tilde Q}=\mathsf S L_{\tilde Q}^{\mathsf T}\mathsf S^{-1}$ |
| $\mathsf S$ | the exchange of $\vec\Upsilon_+$ and $\vec\Upsilon_-$ fixing $\tilde\Pi_\pm$; the second-third coordinate permutation in the canonical frame |
| $T_{\tilde Q,\tilde P}=L_{\tilde Q}R_{\tilde P}$ | the two-sided operator $X\mapsto\tilde QX\tilde P$ |
| $T_{\mu\nu}=L_\mu R_\nu$ | the sixteen basis matrices |
| $\mathsf M_2(\tilde Q)$ | the $2\times2$ model, $\det=\langle\tilde Q\rangle_{\natural}$ |
| $C_{\Pi}$ | the Peirce change from the canonical frame to the coefficient basis |
| $\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ | the quaternionic norm |
| $\beta,\delta$ | the two right directions of a frame, $\beta^2=\delta^2=-e_t$, $\beta\delta=-\delta\beta$ |
| $\gamma_0,\gamma_1,\gamma_2,\gamma_3,\gamma_5$ | one Dirac frame; five cell multiples in the reference frame |
| $\Sigma_{\mu\nu}=\tfrac{i}{2}[\gamma_\mu,\gamma_\nu]$ | the Lorentz generators, six even cells |
| $c(M)$ | the coefficient matrix, $c(M)_{\mu\nu}=\tfrac14\operatorname{Tr}(T_{\mu\nu}^{\dagger}M)$ |
| $\ell(M)$ | the least number of products summing to $M$; equal to $\operatorname{rank}c(M)$ |
| $[Q]=(Q_t,Q_x,Q_y,Q_z)^{\mathsf T}$ | the coordinate column of $\tilde Q$ |

## Further Reading

- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the abstract family, the generation theorem, the composition, the adjoint and the type criteria.
- [$M_4(\mathbb{C})_{\mathbb{B}_L}$ Representation : The Left Regular Operators on the Biquaternion Algebra](m4c-representation-the-left-regular-operators-on-the-biquaternion-algebra.html), for $L_{\tilde Q}$ and the four left matrices.
- [$M_4(\mathbb{C})_{\mathbb{B}_R}$ Representation : The Right Regular Operators on the Biquaternion Algebra](m4c-representation-the-right-regular-operators-on-the-biquaternion-algebra.html), for $R_{\tilde Q}$, the exchange $\mathsf S L_{\tilde Q}^{\mathsf T}\mathsf S^{-1}$ and the $+i\sigma_2$ form of the $y$ generator.
- [$M_4(\mathbb{C})$ Representation : The General Endomorphisms](m4c-representation-the-general-endomorphisms.html), for the Peirce change $C_{\Pi}$ and the operator-space matrix units.
- [$M_4(\mathbb{C})_{\mathbb{B}_L}$ Model : The Product, the Trace and the Determinant](m4c-model-the-product-the-trace-and-the-determinant.html), for the canonical frame and the left matrices.
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for the algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$ and the bi-module structure.
- [The Matrix Algebra $M_4(\mathbb{C})$](the-matrix-algebra-m4c.html), for the construction of $M_4(\mathbb{C})$ from the sandwich map and the change to the matrix-unit basis.
- [The Commutant of the Two Regular Families](the-commutant-of-the-two-regular-families.html), for the intersection of the two one-sided families used in the cone.
- [Conventions of the Matrix Models](../articles_physics/conventions-of-the-matrix-models.html), for the explicit chiral matrices of one frame, the Peirce match and the chirality.
