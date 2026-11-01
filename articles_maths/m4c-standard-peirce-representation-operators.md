# __$M_4(\mathbb{C})$ Standard Peirce Representation : Operators__

## Introduction

**The question.** The Standard Peirce article computes the left matrix $L^{P}(\tilde Q)$ and the right matrix $R^{P}(\tilde P)$ of a biquaternion, their product, their trace, their determinant and their values on the six subspaces. This article asks the operator question that follows: which endomorphisms of $\mathbb{B}$ arise from multiplication, and what are their matrices inside $M_4(\mathbb{C})$?

**The three answers.** The answers sit at three levels.

- A general endomorphism is any matrix in $M_4(\mathbb{C})$. The frame gives a linear isomorphism $\operatorname{End}_{\mathbb{C}}(\mathbb{B})\to M_4(\mathbb{C})$, and every $4\times4$ matrix is the matrix of exactly one operator. The space has sixteen complex dimensions, and a general operator need not be a single product.
- A one-sided operator is a left or a right multiplication. The left matrices fill the four-dimensional copy $\mathbb{B}_L=\{\mathrm I_2\otimes A\}$, and the right matrices fill the four-dimensional copy $\mathbb{B}_R=\{B^{\mathsf T}\otimes\mathrm I_2\}$. These are exactly the two subsets of the Standard Peirce article, and their intersection is the scalars.
- A two-sided operator is a product $T_{\tilde Q,\tilde P}=L^{P}(\tilde Q)R^{P}(\tilde P)$. The products fill a seven-dimensional cone in $M_4(\mathbb{C})$, not a subspace, and they are exactly the matrices whose coefficient matrix has rank at most one.

**The result in one line.** Every matrix is a sum of at most four two-sided products; the products themselves are the matrices of coefficient rank at most one; and the least number of products is the coefficient rank.

**The two-sided part.** The long section on the two-sided operators is the Standard Peirce reading of *$M_4(\mathbb{C})_{\mathcal{T}}$ Representation : The Two-Sided Operators on the Biquaternion Algebra*. It records the factorisation, the cone, the coefficient criterion, the composition, the failure of additivity, the length, the two ranks, the adjoint and the type criteria, the one-sided boundaries and the structural reading as pure tensors.

**Boundaries.** The frame and the one-sided matrices are *$M_4(\mathbb{C})$ Standard Peirce Representation*. The abstract family is *Two-Sided Operators on the Biquaternion Algebra*. The enveloping algebra is *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*. The Hermitian sandwich is Part V and is not treated here.

## The Three Correspondences

**The ambient space.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, with $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$. Its complex dimension is four, and $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ is the algebra $M_4(\mathbb{C})$ of complex dimension sixteen. Every endomorphism is written in the standard Peirce frame
$$
\mathcal{P}=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-),\qquad
\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z),\qquad
\vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y).
$$
A matrix written without a superscript is in this frame. The left matrix is $L^{P}(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q)$ and the right matrix is $R^{P}(\tilde P)=\mathsf M_2(\tilde P)^{\mathsf T}\otimes\mathrm I_2$; the two are the operators of left and right multiplication on $\mathbb{B}$.

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

**The coefficient matrix.** For the test in the table, write $T_{\mu\nu}=L_\mu^{P}R_\nu^{P}$ and expand $M=\sum_{\mu,\nu}c_{\mu\nu}T_{\mu\nu}$; the matrix $c(M)=(c_{\mu\nu})$ is the **coefficient matrix**. The basis and the Hilbert–Schmidt formula for its entries are in §*The General Endomorphisms*.

**The table.** The three levels and the two one-sided copies are collected in one table.

| Level | Operator | Subset of $M_4(\mathbb{C})$ | Complex dimension | Test |
|---|---|---|---|---|
| general endomorphism | $M$ | all of $M_4(\mathbb{C})$ | $16$ | none |
| one-sided left | $L^{P}(\tilde Q)$ | $\{\mathrm I_2\otimes A\}$ | $4$ | two equal diagonal blocks |
| one-sided right | $R^{P}(\tilde P)$ | $\{B^{\mathsf T}\otimes\mathrm I_2\}$ | $4$ | scalar blocks |
| intersection of the one-sided copies | $\lambda\mathrm I_4$ | the scalars | $1$ | both conditions |
| two-sided | $T_{\tilde Q,\tilde P}$ | $\{\operatorname{rank}c(M)\le1\}$ | $7$ (cone) | rank-one coefficient matrix |

The table is the answer to the operator question. The general level is the whole space; the one-sided levels are two linear subspaces; the two-sided level is a cone inside the whole space, of dimension seven.

## The General Endomorphisms

**The sixteen matrices.** For $\mu,\nu\in\{t,x,y,z\}$ put
$$
T_{\mu\nu}=L_\mu^{P}R_\nu^{P},\qquad
L_\mu^{P}=L^{P}(e_\mu),\qquad
R_\nu^{P}=R^{P}(e_\nu).
$$
In the $2\times2$ model, with $A_\mu=\mathsf M_2(e_\mu)$,
$$
T_{\mu\nu}=A_\nu^{\mathsf T}\otimes A_\mu .
$$
The sixteen matrices are orthogonal in the Hilbert–Schmidt inner product:
$$
\operatorname{Tr}\bigl(T_{\mu\nu}^{\dagger}T_{\rho\sigma}\bigr)
=4\,\delta_{\mu\rho}\delta_{\nu\sigma}.
$$
The proof is the product rule for Kronecker products and the orthogonality of the four matrices $A_\mu$, which satisfy $\operatorname{Tr}(A_\mu^{\dagger}A_\rho)=2\delta_{\mu\rho}$. The sixteen are independent; since $M_4(\mathbb{C})$ has complex dimension sixteen, they are a basis.

**The coefficient matrix.** Every $M\in M_4(\mathbb{C})$ has a unique expansion
$$
M=\sum_{\mu,\nu}c_{\mu\nu}T_{\mu\nu},
$$
and orthogonality gives the coefficients directly:
$$
c(M)_{\mu\nu}=\tfrac14\operatorname{Tr}\bigl(T_{\mu\nu}^{\dagger}M\bigr).
$$
The $4\times4$ matrix $c(M)=(c_{\mu\nu})$ is the **coefficient matrix** of $M$. The map $M\mapsto c(M)$ is a linear isomorphism of $M_4(\mathbb{C})$ onto itself. It is a coordinate, not a normal form: it does not diagonalise $M$ and it does not select a representative of a conjugacy class.

**No canonical form.** The matrix $[M]_{\mathcal{P}}$ depends on the frame, and conjugation is the only freedom. The trace, the determinant, the rank and the characteristic polynomial are invariant, but they do not classify the operator. The coefficient matrix is a second coordinate, adapted to the product set; it is not a classification either.

**The length, stated.** Every matrix is a sum of at most four products $T_{\tilde Q,\tilde P}$, and the least number is the rank of $c(M)$. The proof is in §*The Span and the Length*. The general endomorphism is therefore a sum of at most four two-sided operators, not a single one in general. The product set is the cone of coefficient rank at most one.

## The One-Sided Operators

**The left copy.** The left matrix is
$$
L^{P}(\tilde Q)=\mathrm I_2\otimes A=\operatorname{diag}(A,A),\qquad
A=\mathsf M_2(\tilde Q).
$$
Its image is the four-dimensional subalgebra $\mathbb{B}_L$. The composition law is $L^{P}(\tilde Q)L^{P}(\tilde R)=L^{P}(\tilde Q\tilde R)$, and the kernel is zero. The rank is $2\operatorname{rank}A$, the trace is $2\operatorname{Tr}A=4Q_t$, and the determinant is $(\det A)^2=\langle\tilde Q\rangle_{\natural}^2$. The four basis matrices $L_\mu^{P}$ are the images of the four units, and they are the four matrices of the Standard Peirce article.

**The right copy.** The right matrix is
$$
R^{P}(\tilde P)=B^{\mathsf T}\otimes\mathrm I_2,\qquad
B=\mathsf M_2(\tilde P),
$$
a block matrix whose four blocks are scalar multiples of $\mathrm I_2$. Its image is the four-dimensional subalgebra $\mathbb{B}_R$. The composition law is anti-multiplicative, $R^{P}(\tilde P)R^{P}(\tilde S)=R^{P}(\tilde S\tilde P)$, and the kernel is zero. The rank is $2\operatorname{rank}B$, the trace is $2\operatorname{Tr}B=4P_t$, and the determinant is $(\det B)^2=\langle\tilde P\rangle_{\natural}^2$. The four basis matrices $R_\mu^{P}$ are the images of the four units.

**The intersection.** A matrix that is both block-diagonal with two equal blocks and block-scalar with four scalar blocks is a scalar matrix:
$$
\mathbb{B}_L\cap\mathbb{B}_R=\mathbb{C}\cdot\mathrm I_4 .
$$
The left copy is the commutant of the right copy, and the right copy is the commutant of the left copy; the two copies are mutual centralisers. The intersection is the centre of each.

**The compression.** In the $2\times2$ model the left matrix compresses to $A$ and the right matrix compresses to $B^{\mathsf T}$. The two-sided product does not compress to a single $2\times2$ matrix: it is the $4\times4$ product $B^{\mathsf T}\otimes A$, and the two tensor factors are both needed. The one-sided actions compress one at a time; the two-sided operator is the product of the two uncompressed actions.

## The Two-Sided Operators

### The Operator $T_{\tilde Q,\tilde P}$

**The definition.** For $\tilde Q,\tilde P\in\mathbb{B}$ the **two-sided operator** of the pair is
$$
T_{\tilde Q,\tilde P}=L^{P}(\tilde Q)R^{P}(\tilde P),\qquad
T_{\tilde Q,\tilde P}(X)=\tilde QX\tilde P .
$$
The first parameter is the left multiplier, the second the right multiplier, and the argument is the third slot. The definition contains the one-sided operators at the two boundary cases $\tilde P=e_t$ and $\tilde Q=e_t$.

**The Pauli evaluation.** With $A=\mathsf M_2(\tilde Q)$ and $B=\mathsf M_2(\tilde P)$,
$$
T_{\tilde Q,\tilde P}=B^{\mathsf T}\otimes A .
$$
The ordinary product $L^{P}(\tilde Q)R^{P}(\tilde P)$ is a $4\times4$ matrix, and the Kronecker product is of two $2\times2$ matrices. The Kronecker product of the two $4\times4$ matrices $L^{P}(\tilde Q)$ and $R^{P}(\tilde P)$ is a $16\times16$ matrix acting on $\mathbb{C}^4\otimes\mathbb{C}^4$; it is not the operator on $\mathbb{B}$.

**The sixteen cells.** The sixteen matrices $T_{\mu\nu}=L_\mu^{P}R_\nu^{P}$ fall into four families. The first row is the right family, the first column is the left family, the corner entry $T_{tt}$ is the identity, and the remaining nine cells are genuinely two-sided.

| $T_{\mu\nu}$ | $\nu=t$ | $\nu=x$ | $\nu=y$ | $\nu=z$ |
|---|---|---|---|---|
| $\mu=t$ | $\mathrm I_4$ | $R_x^{P}$ | $R_y^{P}$ | $R_z^{P}$ |
| $\mu=x$ | $L_x^{P}$ | $L_x^{P}R_x^{P}$ | $L_x^{P}R_y^{P}$ | $L_x^{P}R_z^{P}$ |
| $\mu=y$ | $L_y^{P}$ | $L_y^{P}R_x^{P}$ | $L_y^{P}R_y^{P}$ | $L_y^{P}R_z^{P}$ |
| $\mu=z$ | $L_z^{P}$ | $L_z^{P}R_x^{P}$ | $L_z^{P}R_y^{P}$ | $L_z^{P}R_z^{P}$ |

The table is the matrix form of the four families of the abstract two-sided article. The first row is the right copy, the first column the left copy, and the diagonal cell $T_{tt}$ the identity.

### The Factorization Map

**The map.** The assignment
$$
\beta:\mathbb{B}\times\mathbb{B}\longrightarrow\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\qquad
\beta(\tilde Q,\tilde P)=T_{\tilde Q,\tilde P}
$$
is the factorisation map. Its image is the set of two-sided operators, and the rest of this section records what the factorisation does and does not imply.

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
If both are nonzero, write $A=\mathsf M_2(\tilde Q)$ and $B=\mathsf M_2(\tilde P)$, and choose matrix units $E_{bc}$ of the $2\times2$ model with $A_{ab}\neq0$ and $B_{cd}\neq0$; then
$$
(AE_{bc}B)_{ad}=A_{ab}B_{cd}\neq0,
$$
so the operator is nonzero. The zero operator is the image of every pair with a zero parameter, and it is the vertex of the cone.

**The two slots.** With the other parameter a unit, the map is injective in each slot:
$$
T_{\tilde Q,e_t}=L^{P}(\tilde Q),\qquad
T_{e_t,\tilde P}=R^{P}(\tilde P).
$$
The first is the left copy, the second the right copy, and both maps are injective. More generally, $T_{\tilde Q,\tilde P}(e_t)=\tilde Q\tilde P$; if $\tilde P$ is a unit, $\tilde Q$ is recovered from this value, and if $\tilde Q$ is a unit, $\tilde P$ is recovered.

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
The zero operator is the vertex, the image of the two four-dimensional subspaces $\tilde Q=0$ and $\tilde P=0$. The image is the seven-dimensional cone of the next subsections.

### The Coefficient Matrix

**The basis and the coefficients.** The sixteen matrices $T_{\mu\nu}$ are a basis of $M_4(\mathbb{C})$, orthogonal of Hilbert–Schmidt norm two. Every $M$ has a unique coefficient matrix $c(M)$ with
$$
c(M)_{\mu\nu}=\tfrac14\operatorname{Tr}\bigl(T_{\mu\nu}^{\dagger}M\bigr),
\qquad
M=\sum_{\mu,\nu}c(M)_{\mu\nu}T_{\mu\nu}.
$$
The map $M\mapsto c(M)$ is a linear isomorphism. The coefficient matrix is the coordinate adapted to the product set: the product condition becomes a rank condition.

**The coefficient matrix of a product.** Write $[Q]=(Q_t,Q_x,Q_y,Q_z)^{\mathsf T}$ for the column of coefficients of $\tilde Q$ in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$. Since
$$
T_{\tilde Q,\tilde P}=\sum_{\mu,\nu}Q_\mu P_\nu\,T_{\mu\nu},
$$
the coefficient matrix is the rank-one matrix
$$
c\bigl(T_{\tilde Q,\tilde P}\bigr)=[Q][P]^{\mathsf T}.
$$
Every rank-one matrix arises in this way, and the zero matrix is the case $\tilde Q=0$ or $\tilde P=0$.

**The criterion.** A matrix $M$ is a single two-sided operator exactly when its coefficient matrix has rank at most one:
$$
M=T_{\tilde Q,\tilde P}\ \text{for some }\tilde Q,\tilde P
\iff
c(M)=[Q][P]^{\mathsf T}
\iff
\operatorname{rank}c(M)\le1.
$$
The zero matrix is the rank-zero case. The criterion is a test on the sixteen coefficients, not on the matrix rank.

**The cone.** The product set is the closed algebraic cone
$$
\{M\in M_4(\mathbb{C}):\operatorname{rank}c(M)\le1\},
$$
cut out by the $2\times2$ minors of $c(M)$. Its projectivisation is the Segre variety $\mathbb{P}^3\times\mathbb{P}^3$ of the decomposable tensors, and the cone has complex dimension seven inside the complex sixteen-dimensional algebra.

### Composition

**The law.** The product of two two-sided operators is a two-sided operator, with the second slot reversed:
$$
T_{\tilde Q,\tilde P}T_{\tilde R,\tilde S}=T_{\tilde Q\tilde R,\ \tilde S\tilde P}.
$$
The proof is one line:
$$
X\longmapsto \tilde Q(\tilde RX\tilde S)\tilde P
=(\tilde Q\tilde R)X(\tilde S\tilde P).
$$
The left parameters multiply in the order, and the right parameters multiply in the reverse order.

**Powers and inverses.** For $n\ge1$,
$$
\bigl(T_{\tilde Q,\tilde P}\bigr)^n=T_{\tilde Q^n,\tilde P^n},
$$
and, when $\tilde Q$ and $\tilde P$ are units,
$$
\bigl(T_{\tilde Q,\tilde P}\bigr)^{-1}=T_{\tilde Q^{-1},\tilde P^{-1}}.
$$
The identity is $T_{e_t,e_t}=\mathrm I_4$.

**The monoid.** The family is a multiplicative monoid: it contains the identity, and it is closed under composition. It is not a group. It contains nonzero zero divisors, for example $T_{\tilde Q,\tilde P}$ with $\tilde Q$ and $\tilde P$ nonzero and of quaternionic norm zero; such an operator has rank one and no inverse. The sixteen basis matrices compose to a signed basis matrix,
$$
T_{\mu\nu}T_{\rho\sigma}=T_{e_\mu e_\rho,\ e_\sigma e_\nu}=\varepsilon\varepsilon'\,T_{\mu'\nu'},
$$
where $e_\mu e_\rho=\varepsilon e_{\mu'}$ and $e_\sigma e_\nu=\varepsilon' e_{\nu'}$, so the set of sixteen is closed only up to sign. The full family contains the signs, because $-T_{\mu\nu}=T_{-e_\mu,e_\nu}$; the set of sixteen does not.

### No Additive Closure

**The sum of two products.** The coefficient matrix of a sum is the sum of the coefficient matrices:
$$
c\bigl(T_{\tilde Q,\tilde P}+T_{\tilde R,\tilde S}\bigr)
=[Q][P]^{\mathsf T}+[R][S]^{\mathsf T}.
$$
It is a sum of two rank-one matrices, of rank at most two, and of rank exactly two for a generic pair. A sum of two rank-one matrices that are not proportional has rank two, so the sum is generally not a two-sided operator.

**The simplest failure.** The sum
$$
T_{tt}+T_{xx}=\mathrm I_4+L_x^{P}R_x^{P}
$$
has coefficient matrix $\operatorname{diag}(1,1,0,0)$, of rank two, so it is not a single product. Its value at $e_t$ is $e_t+\vec e_x e_t\vec e_x=e_t-e_t=0$, so it is neither a nonzero left multiplication nor a nonzero right multiplication; the coefficient matrix decides the two-sided question as well.

**The cone, not a subspace.** The product set is closed under scalar multiplication, because $\lambda T_{\tilde Q,\tilde P}=T_{\lambda\tilde Q,\tilde P}$, but it is not closed under addition. It is a cone with vertex the zero operator, not a linear subspace.

### The Span and the Length

**The generation theorem.** The sixteen products span the whole algebra:
$$
\operatorname{span}_{\mathbb{C}}\{T_{\tilde Q,\tilde P}:\tilde Q,\tilde P\in\mathbb{B}\}
=M_4(\mathbb{C}),
$$
and the span needs no more than the sixteen basis matrices. Every endomorphism is a finite sum of two-sided operators.

**At most four.** The coefficient matrix is a $4\times4$ matrix, of rank $r\le4$. Factor it as $c=UV$ with $U$ of size $4\times r$ and $V$ of size $r\times4$; the columns of $U$ are the columns $[Q_i]$, and the rows of $V$ are the rows $[P_i]^{\mathsf T}$. Then
$$
M=\sum_{i=1}^{r}T_{\tilde Q_i,\tilde P_i}.
$$
Every matrix is a sum of at most four products, and four are always enough.

**The length.** The **length** $\ell(M)$ is the least $r\ge0$ such that $M$ is a sum of $r$ products; $\ell(0)=0$. The length is the coefficient rank:
$$
\ell(M)=\operatorname{rank}c(M).
$$
If $M=\sum_{i\le r}T_{\tilde Q_i,\tilde P_i}$, then $c(M)=\sum_{i\le r}[Q_i][P_i]^{\mathsf T}$ is a sum of $r$ rank-one matrices, so $\operatorname{rank}c(M)\le r$ and $\ell(M)\ge\operatorname{rank}c(M)$. Conversely, the rank factorisation above gives $\ell(M)\le\operatorname{rank}c(M)$. The two inequalities prove the equality.

**The consequences.** The length takes the five values $0,1,2,3,4$. The value $0$ is the zero matrix; the value $1$ is the cone of single products; the value $4$ is exactly the open dense set $\det c(M)\neq0$. A generic matrix needs four products, and no matrix needs five. The length is not the matrix rank; the next subsection separates the two.

**The algorithm.** Compute the sixteen coefficients $\tfrac14\operatorname{Tr}(T_{\mu\nu}^{\dagger}M)$ and form $c(M)$. If $\operatorname{rank}c=1$, take a nonzero column of $c$ as $[Q]$; if its $i$-th entry is nonzero, the $i$-th row of $c$ divided by that entry is $[P]^{\mathsf T}$. If $\operatorname{rank}c=r>1$, a rank factorisation $c=UV$ gives the $r$ terms. No test on the matrix rank alone decides the question.

### The Two Ranks

**The rank of a product.** In the Pauli evaluation $T_{\tilde Q,\tilde P}=B^{\mathsf T}\otimes A$, and the rank of a Kronecker product is the product of the ranks:
$$
\operatorname{rank}T_{\tilde Q,\tilde P}
=\operatorname{rank}\mathsf M_2(\tilde Q)\operatorname{rank}\mathsf M_2(\tilde P)
\in\{0,1,2,4\}.
$$
The rank of $\mathsf M_2(\tilde Q)$ is $2$ when $\langle\tilde Q\rangle_{\natural}\neq0$, $1$ when $\tilde Q\neq0$ and $\langle\tilde Q\rangle_{\natural}=0$, and $0$ when $\tilde Q=0$. No product has matrix rank three, and a product has matrix rank four exactly when both parameters are units.

**The trace and the determinant.** In the same evaluation,
$$
\operatorname{Tr}T_{\tilde Q,\tilde P}=4Q_tP_t,\qquad
\det T_{\tilde Q,\tilde P}
=\langle\tilde Q\rangle_{\natural}^{2}\langle\tilde P\rangle_{\natural}^{2}.
$$
The trace is the product of the two scalar parts, and the determinant is the square of each quaternionic norm. The inverse is $T_{\tilde Q^{-1},\tilde P^{-1}}$ when both parameters are units.

**The two ranks are independent.** The matrix rank and the length are different invariants. In the table, $P_+=\operatorname{diag}(0,0,1,1)$ is the projector, $u_2,u_3$ are the second and third standard columns in the Peirce frame, and "null" means $\langle\tilde Q\rangle_{\natural}=0$, the vanishing of the quaternionic norm, equivalently $\det\mathsf M_2(\tilde Q)=0$. The table collects the examples.

| $M$ | $\operatorname{rank}M$ | $\operatorname{rank}c(M)=\ell(M)$ |
|---|---|---|
| $T_{tt}+T_{tz}$ | $4$ | $1$ |
| $P_+$ | $2$ | $1$ |
| $T_{\tilde Q,\tilde P}$, $\tilde Q,\tilde P$ nonzero and null | $1$ | $1$ |
| $T_{tt}+T_{xx}$ | $2$ | $2$ |
| $M_1=(u_2+u_3)(u_2+u_3)^{\mathsf T}$ | $1$ | $4$ |
| generic $M$ | $4$ | $4$ |

**The rows.** The sum $T_{tt}+T_{tz}$ is the single product $T_{e_t,e_t+e_z}$, of matrix rank four. The projector $P_+=\operatorname{diag}(0,0,1,1)$ is the single product $T_{e_t/2,\ e_t-ie_z}$, of matrix rank two. A product of two nonzero null parameters has matrix rank one and length one. The sum $T_{tt}+T_{xx}$ has coefficient matrix $\operatorname{diag}(1,1,0,0)$, of rank two, and length two. The matrix $M_1=(u_2+u_3)(u_2+u_3)^{\mathsf T}$, with $u_2,u_3$ the second and third standard columns in the Peirce frame, has matrix rank one and coefficient matrix $\tfrac12\operatorname{diag}(1,-1,1,1)$, of rank four, so its length is four. A generic matrix has both ranks four.

**The reading.** Matrix rank one does not force length one, and matrix rank two does not force length greater than one. Only the coefficient matrix decides the length. The two ranks answer different questions: the matrix rank is the size of the image, and the length is the least number of products in a decomposition.

**A matrix unit.** The first matrix unit $E_{11}$ has coefficient matrix
$$
c(E_{11})=\frac14
\begin{pmatrix}
1&0&0&i\\
0&0&0&0\\
0&0&0&0\\
i&0&0&-1
\end{pmatrix}
=\frac14\begin{pmatrix}1\\0\\0\\i\end{pmatrix}\begin{pmatrix}1&0&0&i\end{pmatrix},
$$
of rank one, so $E_{11}$ is a single product:
$$
E_{11}=T_{(e_t+i\vec e_z)/4,\ e_t+i\vec e_z}.
$$
The two parameters have quaternionic norm zero; the factors can be null while the product is a matrix unit.

### The Plain Adjoint and the Types

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
Then $\tilde Q$ is a unit and $\tilde P=\pm\tilde Q^{-1}$, and the operator is $\pm\mathrm{Ad}_{\tilde Q}$. The isometry group is
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

### The One-Sided Boundaries

**The two boundary cases.** The left and right copies are the two boundary cases of the cone:
$$
T_{\tilde Q,e_t}=L^{P}(\tilde Q),\qquad
T_{e_t,\tilde P}=R^{P}(\tilde P).
$$
Both are single products, and both are contained in the cone. Their intersection is the scalars $\mathbb{C}\cdot\mathrm I_4$, by §*The One-Sided Operators*.

**The cone is larger.** A generic pair has neither parameter a scalar multiple of $e_t$, and its operator is neither a left nor a right multiplication. The cone is strictly larger than the union of the two copies. The two copies are four-dimensional linear subspaces inside the seven-dimensional cone, and the cone itself is not a subspace.

**The Hermitian subcone.** The Hermitian sandwich is the subcone $\tilde P=\tilde Q^{*}$, a real seven-dimensional cone inside the complex seven-dimensional cone. It is the subject of Part V and is not developed here.

### The Structural Reading

**The enveloping algebra.** The map
$$
\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}
\longrightarrow\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\qquad
\tilde Q\otimes\tilde P^{\mathrm{opp}}
\longmapsto L^{P}(\tilde Q)R^{P}(\tilde P)
$$
is an isomorphism of complex algebras. The sixteen elementary tensors $e_\mu\otimes e_\nu^{\mathrm{opp}}$ map to the sixteen matrices $T_{\mu\nu}$, which are a basis; the isomorphism is the generation theorem in algebra form.

**The pure tensors.** Under this isomorphism the two-sided operators are exactly the decomposable tensors $\tilde Q\otimes\tilde P^{\mathrm{opp}}$, that is the image of the Segre cone $\mathbb{P}^3\times\mathbb{P}^3$ in $\mathbb{P}^{15}$. The abstract identity $T_{\tilde Q,\tilde P}=L^{P}(\tilde Q)R^{P}(\tilde P)$ is the same statement as "the element is a pure tensor in $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}$". The seven-dimensional cone of §*The Coefficient Matrix* is exactly the cone of pure tensors inside the sixteen-dimensional algebra.

### What the Factorization Buys and Does Not

**It gives.**
- An explicit parametrisation by two biquaternions, eight complex parameters modulo the $\mathbb{C}^{\times}$ scaling, hence seven effective parameters.
- A product formula, hence powers, inverses and the monoid structure.
- A rank-one coefficient criterion, hence a decisive test for "is this matrix a single two-sided operator?"
- The length formula $\ell(M)=\operatorname{rank}c(M)$ with $0\le\ell(M)\le4$.
- The plain adjoint and the type criteria: $(T_{\tilde Q,\tilde P})^{\approx}=T_{\tilde P,\tilde Q}$; self-adjoint exactly when $\tilde P=\lambda\tilde Q$; isometry exactly when $\tilde P\tilde Q=\pm e_t$; multiplicative exactly when $\tilde P\tilde Q=e_t$.

**It does not give.**
- Additivity: the set is not a subspace, and the sum of two products is generally not a product.
- Universality: not every matrix is a single product; four products may be needed, and four are always enough.
- A division algebra: the basis matrices are invertible, but the span has zero divisors, for example $T_{tt}+T_{xx}$ of rank two.
- A pin group: the quadratic form $\mathrm{Sc}(\tilde Q^2)$ is not multiplicative, and the isometry group of the family is only $\{\pm\mathrm{Ad}_{\tilde Q}\}$, of complex dimension three, with no skew-adjoint sector.

## Summary

The operators on the biquaternion algebra sit at three levels. Every endomorphism is a matrix in $M_4(\mathbb{C})$, and the frame gives an isomorphism of sixteen-dimensional algebras. The one-sided operators fill the two four-dimensional copies $\mathbb{B}_L=\{\mathrm I_2\otimes A\}$ and $\mathbb{B}_R=\{B^{\mathsf T}\otimes\mathrm I_2\}$, the same two subsets as the Standard Peirce article; their intersection is the scalars. The two-sided operators are the products $T_{\tilde Q,\tilde P}=L^{P}(\tilde Q)R^{P}(\tilde P)=B^{\mathsf T}\otimes A$.

The product set is the seven-dimensional Segre cone of pure tensors in $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}=M_4(\mathbb{C})$. It is not a subspace. The factorisation map has eight parameters, one scaling orbit, and the zero operator as vertex. The coefficient matrix $c(M)$, defined by the sixteen orthogonal matrices $T_{\mu\nu}$, turns the product condition into the rank condition $\operatorname{rank}c(M)\le1$.

The cone is closed under composition, with the second slot reversed, but not under addition. The length is the coefficient rank, $\ell(M)=\operatorname{rank}c(M)$, and it takes the values $0,1,2,3,4$; every matrix is a sum of at most four products, and a generic matrix needs four. The matrix rank of a product is the product of the two matrix ranks, in $\{0,1,2,4\}$, and it is independent of the length: matrix rank one can have length four, and matrix rank two can have length one.

The plain adjoint swaps the two parameters, and the type criteria are $\tilde P=\lambda\tilde Q$ for self-adjoint, $\tilde P\tilde Q=\pm e_t$ for isometry and $\tilde P\tilde Q=e_t$ for multiplicative. The isometry group is $\{\pm\mathrm{Ad}_{\tilde Q}\}$, of complex dimension three, and it is not a pin group.

In one line: every two-sided operator is a single product of one left and one right multiplication; the set of such products is the seven-dimensional cone of pure tensors, characterised by a rank-one coefficient matrix, closed under composition but not under addition, with length the coefficient rank and matrix rank in $\{0,1,2,4\}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, $\dim_{\mathbb{C}}=4$ |
| $\mathcal{P}=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$ | the standard Peirce frame |
| $L^{P}(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q)$ | the left matrix |
| $R^{P}(\tilde P)=\mathsf M_2(\tilde P)^{\mathsf T}\otimes\mathrm I_2$ | the right matrix |
| $L_\mu^{P}=L^{P}(e_\mu)$, $R_\nu^{P}=R^{P}(e_\nu)$ | the four basis matrices of each copy |
| $T_{\tilde Q,\tilde P}=L^{P}(\tilde Q)R^{P}(\tilde P)$ | the two-sided operator, $X\mapsto\tilde QX\tilde P$ |
| $T_{\mu\nu}=L_\mu^{P}R_\nu^{P}$ | the sixteen basis matrices |
| $[Q]=(Q_t,Q_x,Q_y,Q_z)^{\mathsf T}$ | the coefficient column of $\tilde Q$ |
| $c(M)$ | the coefficient matrix, $c(M)_{\mu\nu}=\tfrac14\operatorname{Tr}(T_{\mu\nu}^{\dagger}M)$ |
| $\ell(M)$ | the least number of products summing to $M$; equal to $\operatorname{rank}c(M)$ |
| $\beta(\tilde Q,\tilde P)=T_{\tilde Q,\tilde P}$ | the factorisation map |
| $\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ | the quaternionic norm |
| $\mathrm{Sc}$ | the scalar part, the $e_t$ coefficient |
| $\approx$ | the plain adjoint for $\langle X,Y\rangle=\mathrm{Sc}(XY)$ |
| $\dagger$ | the Hilbert–Schmidt adjoint of a $4\times4$ matrix |
| $\operatorname{rank}$ | the matrix rank, on matrices and on $c(M)$ |

## Further Reading

- [$M_4(\mathbb{C})$ Standard Peirce Representation](m4c-standard-peirce-representation-the-matrix-product-the-trace-and-the-determinant.html), for the frame, the left and right matrices and the six subspaces.
- [$M_2(\mathbb{C})$ Standard Peirce Representation](m2c-standard-peirce-representation-the-matrix-product-the-trace-and-the-determinant.html), for the compression of the two one-sided actions.
- [$M_4(\mathbb{C})$ e-basis Representation : The Matrix Product, the Trace and the Determinant](m4c-e-basis-representation-the-matrix-product-the-trace-and-the-determinant.html), for the same operators in the e-basis.
- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the abstract family, the generation theorem, the composition, the adjoint and the type criteria.
- [$M_4(\mathbb{C})_{\mathcal{T}}$ Representation : The Two-Sided Operators on the Biquaternion Algebra](m4c-representation-the-two-sided-operators-on-the-biquaternion-algebra.html), for the matrix form of the same family in the canonical frame.
- [$M_4(\mathbb{C})_{\mathbb{B}_L}$ Representation : The Left Regular Operators on the Biquaternion Algebra](m4c-representation-the-left-regular-operators-on-the-biquaternion-algebra.html), for $L^{P}$ and the four left matrices.
- [$M_4(\mathbb{C})_{\mathbb{B}_R}$ Representation : The Right Regular Operators on the Biquaternion Algebra](m4c-representation-the-right-regular-operators-on-the-biquaternion-algebra.html), for $R^{P}$ and the four right matrices.
- [The Endomorphisms of the Biquaternion Algebra](the-endomorphisms-of-the-biquaternion-algebra.html), for the ambient operator space and its coordinate column.
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for the algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$ and the pure tensors.
- [The Commutant of the Two Regular Families](the-commutant-of-the-two-regular-families.html), for the intersection of the two one-sided copies.
- [The Four Adjoints of the Biquaternion Algebra in Examples](the-four-adjoints-of-the-biquaternion-algebra-in-examples.html), for the plain adjoint and its comparison with the other adjoints.
- [The Hermitian Sandwich: Definition and Multiplicativity](the-hermitian-sandwich-definition-and-multiplicativity.html), for the real subcone $\tilde P=\tilde Q^{*}$.
