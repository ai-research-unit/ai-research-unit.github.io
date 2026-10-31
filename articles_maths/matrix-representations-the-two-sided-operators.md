# __Matrix Representations : The Two-Sided Operators__

## Introduction

The two-sided operator sends $X$ to $\tilde QX\tilde P$. It is the most general product of a left and a right multiplication, and its matrix is the product of the left and right matrices. The sixteen operators obtained from the four units in each slot form a basis of the whole algebra $M_4(\mathbb{C})$. The basis is orthogonal for the Hilbert–Schmidt form, every basis matrix is invertible, and yet the span contains matrices of every rank.

This article computes the two-sided family in the two displays. It gives the sixteen basis matrices, their composition, trace, determinant and orthogonality, the coefficient matrix of a general $4\times4$ matrix in this basis, the gamma frame built from five cells, and the cone of products with the rank criterion. It also draws the consequences of the factorization: the parameter map is bilinear with a one-dimensional fibre, so the image is a seven-dimensional cone and not a subspace; the cone is a monoid and not an additive semigroup; under $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}\cong M_4(\mathbb{C})$ it is the set of pure tensors; and the adjoints, the isometries and the multiplicative members are read from the pair. It is the third of the three articles on the regular operator families; the left family is *Matrix Representations : The Left Regular Operators* and the right family is *Matrix Representations : The Right Regular Operators*.

**Conventions.** The algebra and the displays are those of *Matrix Representations : The Models and the Change of Frame*. The element is $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, and $B=\mathsf M_2(\tilde Q)$ is its $2\times2$ matrix, with $\det B=\langle\tilde Q\rangle_{\natural}$. The Peirce frame is $\mathcal P=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$, so that $L_{\tilde Q}=I_2\otimes B$ and $R_{\tilde P}=B_P^{\mathsf T}\otimes I_2$. The coefficient frame is $\mathcal B=(e_t,\vec e_x,\vec e_y,\vec e_z)$.

**Boundaries.** The operator statements are *Two-Sided Operators on the Biquaternion Algebra*; the two one-sided families are *Matrix Representations : The Left Regular Operators* and *Matrix Representations : The Right Regular Operators*; the Hermitian sandwich is *Matrix Representations : The Hermitian Sandwich*; the frame change is *Matrix Representations : The Models and the Change of Frame*; the gamma frame in the coefficient display is *The Two-Sided Operators and the Spin Group*.

## The Operator

**The definition.**
$$
T_{\tilde Q,\tilde P}:M_4(\mathbb{C})\longrightarrow M_4(\mathbb{C}),
\qquad
T_{\tilde Q,\tilde P}(X)=\tilde QX\tilde P.
$$
On the carrier it is the composition $L_{\tilde Q}R_{\tilde P}$.

**The law.** The family is multiplicative in the pair,
$$
T_{\tilde Q,\tilde P}T_{\tilde R,\tilde S}=T_{\tilde Q\tilde R,\ \tilde S\tilde P},
$$
with identity $T_{e_t,e_t}$. The order in the second slot is reversed, because the right multiplication by $\tilde P$ acts first. By induction, $(T_{\tilde Q,\tilde P})^n=T_{\tilde Q^n,\tilde P^n}$ for every $n\geq1$.

**The matrix.** In the Peirce frame,
$$
\mathsf T(\tilde Q,\tilde P)=\mathsf M_4^{L}(\tilde Q)\mathsf M_4^{R}(\tilde P)
=\bigl(B_P^{\mathsf T}\otimes I_2\bigr)\bigl(I_2\otimes B_Q\bigr)
=B_P^{\mathsf T}\otimes B_Q .
$$
The Kronecker product is of two $2\times2$ matrices and gives the $4\times4$ matrix of the operator. It is not a Kronecker product of two $4\times4$ matrices; the $16\times16$ object belongs to a different space.

**The invariants.**
$$
\operatorname{Tr}\mathsf T(\tilde Q,\tilde P)=4Q_tP_t,
\qquad
\det\mathsf T(\tilde Q,\tilde P)=\langle\tilde Q\rangle_{\natural}^2\langle\tilde P\rangle_{\natural}^2,
\qquad
\operatorname{rank}\mathsf T(\tilde Q,\tilde P)=\operatorname{rank}B_Q\cdot\operatorname{rank}B_P .
$$
The trace is the product of the traces of the two one-sided matrices divided by the dimension of the carrier: $4Q_tP_t= (4Q_t)(4P_t)/4$. The determinant is the product of the two determinants of the one-sided matrices, because each is already a square. The rank is the product of the two $2\times2$ ranks, so it takes the values $4,2,1,0$ and never $3$.

**The inverse.** The operator is invertible exactly when both parameters are units, and on the invertible locus
$$
\mathsf T(\tilde Q,\tilde P)^{-1}=\mathsf T(\tilde Q^{-1},\tilde P^{-1}).
$$

## The Sixteen Basis Matrices

**The definition.** For $\mu,\nu\in\{t,x,y,z\}$ put
$$
T_{\mu\nu}=\mathsf T(e_\mu,e_\nu)=\mathsf M_4^{L}(e_\mu)\mathsf M_4^{R}(e_\nu).
$$
The sixteen matrices are linearly independent and span $M_4(\mathbb{C})$.

**The table in four families.**

| | $\nu=t$ | $\nu=x$ | $\nu=y$ | $\nu=z$ |
|---|---|---|---|---|
| $\mu=t$ | $T_{tt}=\mathrm I_4$ | $T_{tx}=R_x$ | $T_{ty}=R_y$ | $T_{tz}=R_z$ |
| $\mu=x$ | $T_{xt}=L_x$ | $T_{xx}=L_xR_x$ | $T_{xy}=L_xR_y$ | $T_{xz}=L_xR_z$ |
| $\mu=y$ | $T_{yt}=L_y$ | $T_{yx}=L_yR_x$ | $T_{yy}=L_yR_y$ | $T_{yz}=L_yR_z$ |
| $\mu=z$ | $T_{zt}=L_z$ | $T_{zx}=L_zR_x$ | $T_{zy}=L_zR_y$ | $T_{zz}=L_zR_z$ |

The first row is the right family and the first column the left family; the identity is $T_{tt}$; the remaining nine cells are genuinely two-sided.

**The Pauli evaluation.** With $\mathsf M_2(e_t)=\mathrm I_2$ and $\mathsf M_2(\vec e_k)=-i\sigma_k$,
$$
T_{tt}=\mathrm I_4,\qquad
T_{tk}=-i\,\sigma_k^{\mathsf T}\otimes\mathrm I_2,\qquad
T_{kt}=-i\,I_2\otimes\sigma_k,\qquad
T_{jk}=-\sigma_k^{\mathsf T}\otimes\sigma_j .
$$
The last display covers $j,k\in\{x,y,z\}$. The transpose on the right factor is the only place where the side of the multiplication shows in the $2\times2$ model.

**An entry.** The matrix $T_{xy}=L_xR_y$ is
$$
T_{xy}=
\begin{pmatrix}
0&0&0&-i\\
0&0&-i&0\\
0&i&0&0\\
i&0&0&0
\end{pmatrix},
$$
and its first column is $i$ times the coordinate column of $\tilde\Pi_-$. The entry is the check that the two-sided table agrees with the exchange.

**The complete product table.** The product of two basis matrices is again a basis matrix up to sign,
$$
T_{\mu\nu}T_{\rho\sigma}=\epsilon\epsilon'\,T_{\mu'\nu'},
\qquad
e_\mu e_\rho=\epsilon e_{\mu'},\quad e_\sigma e_\nu=\epsilon' e_{\nu'}.
$$
The sixteen are closed under multiplication up to sign and contain the identity, but they do not form a group: the product of two cells is a cell only up to sign, and $-T_{\mu\nu}$ is not one of the sixteen. It is nevertheless a product, $-T_{\mu\nu}=T_{-e_\mu,e_\nu}$, because the parameter map is bilinear. The full family is a monoid and not a group, since it contains singular products.

**All sixteen are units.** Every basis matrix has determinant $1$ and rank $4$. The algebra is nevertheless $M_4(\mathbb{C})$, which has many zero divisors; a basis of invertible matrices does not make an algebra a division algebra. For instance,
$$
T_{tt}+T_{xx}=\mathrm I_4+L_xR_x=
\begin{pmatrix}
1&0&0&-1\\
0&1&-1&0\\
0&-1&1&0\\
-1&0&0&1
\end{pmatrix}
$$
has rank two.

## Orthogonality and the Coefficient Matrix

**The orthogonality theorem.** For the Hilbert–Schmidt form $\langle A,B\rangle=\operatorname{Tr}(A^{\dagger}B)$,
$$
\operatorname{Tr}\bigl(T_{\mu\nu}^{\dagger}T_{\rho\sigma}\bigr)=4\,\delta_{\mu\rho}\delta_{\nu\sigma},
$$
so the sixteen are orthogonal and each has Hilbert–Schmidt norm $2$.

**The coefficient matrix.** Every $M\in M_4(\mathbb{C})$ has a unique expansion
$$
M=\sum_{\mu,\nu}c_{\mu\nu}T_{\mu\nu},
\qquad
c_{\mu\nu}=\tfrac14\operatorname{Tr}\bigl(T_{\mu\nu}^{\dagger}M\bigr).
$$
The $4\times4$ matrix $c(M)=(c_{\mu\nu})$ is the coefficient matrix, and $M\mapsto c(M)$ is a linear isomorphism of $M_4(\mathbb{C})$ onto itself.

**The coefficient of a product.** For $M=T_{\tilde Q,\tilde P}$,
$$
c(M)=[Q]\,[P]^{\mathsf T},
$$
where $[Q]=(Q_t,Q_x,Q_y,Q_z)^{\mathsf T}$ is the coefficient column. The coefficient matrix of a product is therefore a rank-one matrix, and every rank-one matrix arises from a product. This is the criterion of §*The Cone of Products*.

**The coefficient display.** In the coefficient frame the sixteen are signed permutation matrices,
$$
T_{\mu\nu}^{\mathrm{coef}}=C_{\Pi}T_{\mu\nu}C_{\Pi}^{-1},
$$
with $C_{\Pi}$ the Peirce change. Conjugation changes the entries and not the algebra; the trace, the determinant, the rank and the orthogonality are unchanged.

## The Gamma Frame

**The five cells.** In the Peirce frame define
$$
\gamma_0=iT_{e_t,e_x},\quad
\gamma_1=iT_{e_x,e_y},\quad
\gamma_2=iT_{e_y,e_y},\quad
\gamma_3=iT_{e_z,e_y},\quad
\gamma_5=-iT_{e_t,e_z}.
$$
In the $2\times2$ evaluation,
$$
\gamma_0=\sigma_1\otimes I_2,\qquad
\gamma_k=i\sigma_2\otimes\sigma_k,\qquad
\gamma_5=-\sigma_3\otimes I_2 .
$$

**The Clifford relations.**
$$
\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}\mathrm I_4,\qquad
(\gamma_5)^2=\mathrm I_4,\qquad
\gamma_5\gamma_\mu=-\gamma_\mu\gamma_5,
$$
with $g=\operatorname{diag}(1,-1,-1,-1)$, and
$$
\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3 .
$$
The sixteen products of the five are the sixteen cells up to units, so the frame identifies the span with $\mathrm{Cl}_{1,3}(\mathbb{C})$ and with $M_4(\mathbb{C})$.

**The normal form.** Let $\beta,\delta$ be orthogonal unit spatial directions. Then
$$
\gamma_0=iL_{e_t}R_\delta,\qquad
\gamma_k=iL_{e_k}R_\beta,\qquad
\gamma_5=iT_{e_t,\beta\delta}
$$
satisfy the same relations. The reference frame is $(\beta,\delta)=(e_y,e_x)$. Nothing in the Clifford relations selects the pair: $\beta$ is the common right factor of the three spatial generators, $\delta$ the right factor of the time generator, and $\beta\delta$ the right factor of the pseudoscalar. The free pair is a genuine parameter of the frame, not a choice of notation.

**The chirality projectors.**
$$
P_\pm=\tfrac12(\mathrm I_4\pm\gamma_5)=\tfrac12\bigl(T_{tt}\pm iT_{e_t,\beta\delta}\bigr).
$$
In the reference frame $P_+=\operatorname{diag}(0,0,1,1)$ and $P_-=\operatorname{diag}(1,1,0,0)$, both of rank two. They are single two-sided operators, but not cells: a single product can be singular.

**The left image does not hold the frame.** The left image is block diagonal in the Peirce frame and preserves the two chiral blocks; the four generators exchange them. The Dirac algebra needs the two-sided family.

## The Cone of Products

**The bilinear map.** Put
$$
\Phi:\mathbb{B}\times\mathbb{B}\longrightarrow M_4(\mathbb{C}),
\qquad
\Phi(\tilde Q,\tilde P)=\mathsf T(\tilde Q,\tilde P).
$$
The map is complex-bilinear, and it is not complex-linear on the product:
$$
\mathsf T(a\tilde Q+b\tilde Q',\tilde P)=a\,\mathsf T(\tilde Q,\tilde P)+b\,\mathsf T(\tilde Q',\tilde P),
$$
and the same in the second slot. Its image is therefore a cone, not a subspace: for $\lambda\in\mathbb{C}$,
$$
\lambda\,\mathsf T(\tilde Q,\tilde P)
=\mathsf T(\lambda\tilde Q,\tilde P)
=\mathsf T(\tilde Q,\lambda\tilde P).
$$

**The zero set.** $\mathsf T(\tilde Q,\tilde P)=0$ exactly when $\tilde Q=0$ or $\tilde P=0$. If one parameter is zero the product is zero. If both are nonzero, choose entries $Q_{ab}\neq0$ and $P_{cd}\neq0$ in the $2\times2$ model and put $X=E_{bc}$; then $(QX P)_{ad}=Q_{ab}P_{cd}\neq0$.

**The two slices.** $T_{\tilde Q,e_t}=L_{\tilde Q}$ and $T_{e_t,\tilde P}=R_{\tilde P}$. The evaluation at the unit is $T_{\tilde Q,\tilde P}(e_t)=\tilde Q\tilde P$; if $\tilde P$ is a unit, $\tilde Q=T_{\tilde Q,\tilde P}(e_t)\tilde P^{-1}$, and if $\tilde Q$ is a unit, $\tilde P=\tilde Q^{-1}T_{\tilde Q,\tilde P}(e_t)$. Each slot is therefore injective once the other is a unit.

**The fibre.** For nonzero pairs,
$$
\mathsf T(\tilde Q,\tilde P)=\mathsf T(\tilde R,\tilde S)
\iff
\tilde R=\lambda\tilde Q,\quad \tilde S=\lambda^{-1}\tilde P
\quad(\lambda\in\mathbb{C}^{\times}).
$$
One direction is the scaling identity. The converse is the injectivity of the tensor map of §*The Tensor Reading*: a pure tensor has a one-dimensional space of decompositions. The fibre is a complex line, the parameter map is constant on it, and it is injective on the quotient.

**The dimension.** The parameter space has complex dimension eight and the generic fibre has dimension one, so the image has complex dimension seven. The zero operator is the image of every pair with a zero parameter; it is the vertex of the cone.

**Not closed under addition.** The sum of two products is not a product in general. The simplest case is
$$
\mathrm I_4+T_{\tilde e_x,\tilde e_x},
$$
which is not of the form $T_{\tilde Q,\tilde P}$.

*Proof.* Suppose $\mathrm I_4+T_{\tilde e_x,\tilde e_x}=T_{\tilde Q,\tilde P}$. At $X=e_t$ the left side is $e_t+\tilde e_xe_t\tilde e_x=e_t-e_t=0$, so $\tilde Q\tilde P=0$. Both parameters are nonzero: if one were zero the right side would vanish, while at $X=\tilde e_y$ the left side is $\tilde e_y+\tilde e_x\tilde e_y\tilde e_x=2\tilde e_y\neq0$. In the $2\times2$ model, $\tilde Q\tilde P=0$ with both factors nonzero forces both to have rank one. At $X=\tilde e_y$ the left side is $2\tilde e_y$, of rank two, while $\tilde Q\tilde e_y\tilde P$ has rank at most one. Contradiction.

The family is therefore a multiplicative monoid and not an additive semigroup. Its linear span is the whole $M_4(\mathbb{C})$, by the generation theorem of §*The Sixteen Basis Matrices*; the family is the cone inside that span, not the span.

**The length.** The length $\ell(M)$ is the least number of products whose sum is $M$. Then
$$
\ell(M)=\operatorname{rank}c(M).
$$
Indeed a sum of $r$ products has coefficient matrix a sum of $r$ rank-one matrices, and conversely a rank factorization $c=UV$ gives $r$ products from the columns of $U$ and the rows of $V$. The length takes the values $0,1,2,3,4$; it is $1$ exactly on the nonzero cone, and it is $4$ exactly when $\det c(M)\neq0$, which is the generic case.

**The criterion.** For $M\neq0$,
$$
M=T_{\tilde Q,\tilde P}\ \text{for some }\tilde Q,\tilde P
\iff
\operatorname{rank}c(M)=1 .
$$
The product set is the affine cone cut out by the $2\times2$ minors of $c(M)$; its projectivisation is the Segre variety $\mathbb{P}^3\times\mathbb{P}^3$, of complex dimension six, and the cone has complex dimension seven in the sixteen-dimensional algebra.

**The two ranks are independent.** Here $u_i$ is the $i$-th standard column of $\mathbb{C}^4$, so $M_1$ is the matrix with a $2\times2$ block of ones in the middle:
$$
M_1=(u_2+u_3)(u_2+u_3)^{\mathsf T}
=\begin{pmatrix}
0&0&0&0\\
0&1&1&0\\
0&1&1&0\\
0&0&0&0
\end{pmatrix}.
$$

| $M$ | $\operatorname{rank}M$ | $\ell(M)$ |
|---|---|---|
| $T_{tt}+T_{tz}=T_{e_t,e_t+e_z}$ | $4$ | $1$ |
| $P_+$ | $2$ | $1$ |
| $T_{\tilde Q,\tilde P}$ with both parameters zero divisors | $1$ | $1$ |
| $T_{tt}+T_{xx}$ | $2$ | $2$ |
| $M_1$ | $1$ | $4$ |
| generic $M$ | $4$ | $4$ |

The matrix $M_1$ has coefficient matrix $\tfrac12\operatorname{diag}(1,-1,1,1)$, of rank four, so it needs four products although it has rank one. The projector $P_+$ has rank two and needs one. The matrix rank of a product is $\operatorname{rank}B_Q\operatorname{rank}B_P\in\{0,1,2,4\}$; no product has rank three. Neither rank determines the other.

**The boundary slices.** The left family is the slice $\tilde P=e_t$ and the right family is the slice $\tilde Q=e_t$; both are contained in the cone and each has complex dimension four. They meet in the scalars $\mathbb{C}\mathrm I_4$, because $L_{\tilde Q}=R_{\tilde P}$ exactly when $\tilde Q=\tilde P$ is central. The cone is strictly larger than the two slices: a generic pair has neither parameter equal to $e_t$, and its operator is neither a left nor a right multiplication.

**How to decide.** Compute the sixteen numbers $\tfrac14\operatorname{Tr}(T_{\mu\nu}^{\dagger}M)$ and form $c$. If $\operatorname{rank}c=1$, take a nonzero column of $c$ for $[Q]$ and the corresponding row, divided by the pivot, for $[P]^{\mathsf T}$. If the rank is $r>1$, a rank factorization of $c$ gives the $r$ terms.

## The Tensor Reading

**The isomorphism.** The bilinear map
$$
\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}
\longrightarrow
\operatorname{End}_{\mathbb{C}}(\mathbb{B}),
\qquad
\tilde Q\otimes\tilde P^{\mathrm{opp}}
\longmapsto
L_{\tilde Q}R_{\tilde P}
$$
is an isomorphism of complex algebras. It is well defined because the pair map is bilinear; it is multiplicative because
$$
(\tilde Q\otimes\tilde P^{\mathrm{opp}})(\tilde R\otimes\tilde S^{\mathrm{opp}})
=\tilde Q\tilde R\otimes(\tilde S\tilde P)^{\mathrm{opp}}
\longmapsto
L_{\tilde Q\tilde R}R_{\tilde S\tilde P}
=L_{\tilde Q}R_{\tilde P}L_{\tilde R}R_{\tilde S},
$$
using $R_{\tilde P}L_{\tilde R}=L_{\tilde R}R_{\tilde P}$; and it is bijective because the sixteen elementary tensors $e_\mu\otimes e_\nu^{\mathrm{opp}}$ map to the basis $T_{\mu\nu}$.

**The pure tensors.** Under this isomorphism the two-sided operators are the decomposable tensors $\tilde Q\otimes\tilde P^{\mathrm{opp}}$. In $\mathbb{P}^{15}$ they form the Segre variety $\mathbb{P}^3\times\mathbb{P}^3$; the affine cone over it is the seven-dimensional cone of §*The Cone of Products*. The fibre theorem is the statement that a pure tensor has a one-dimensional space of decompositions,
$$
\tilde Q\otimes\tilde P^{\mathrm{opp}}
=(\lambda\tilde Q)\otimes(\lambda^{-1}\tilde P)^{\mathrm{opp}}.
$$

**The coordinates.** The coefficient matrix $c(M)$ is the coordinate matrix of $M$ in the basis $T_{\mu\nu}$, hence the coordinate matrix of the corresponding tensor; a product has $c=[Q][P]^{\mathsf T}$, of rank one.

**The reading.** "The operator is a single product" and "the tensor is pure" are the same statement. The length is the tensor rank: the least number of decomposable tensors whose sum is the given tensor. The generation theorem says that this tensor rank is at most four. This is the structural content of the factorization, and it is where the number four comes from.

## The Adjoints and the Three Criteria

**The two adjoints.** The Hilbert–Schmidt adjoint is
$$
\mathsf T(\tilde Q,\tilde P)^{\dagger}=\mathsf T(\tilde Q^{*},\tilde P^{*}),
$$
because $(B_P^{\mathsf T}\otimes B_Q)^{\dagger}=(B_P^{*})^{\mathsf T}\otimes B_Q^{*}$ and $\mathsf M_2$ is a $*$-homomorphism. The plain adjoint, for the bilinear form $\langle X,Y\rangle=\operatorname{Sc}(XY)$, is
$$
\bigl(T_{\tilde Q,\tilde P}\bigr)^{\approx}=T_{\tilde P,\tilde Q},
$$
with no conjugation. The dagger keeps the sides and conjugates both parameters; the plain adjoint swaps the sides and conjugates neither. The two are different and are not to be identified.

**The self-adjoint pairs.** For $\tilde Q\neq0$,
$$
\bigl(T_{\tilde Q,\tilde P}\bigr)^{\approx}=T_{\tilde Q,\tilde P}
\iff
\tilde P=\lambda\tilde Q\quad(\lambda\in\mathbb{C}).
$$
The proof is the matrix-unit computation: self-adjointness is $\tilde QX\tilde P=\tilde PX\tilde Q$ for every $X$, and on the matrix units this forces the two matrices to be proportional. The diagonal operators $T_{\tilde Q,\tilde Q}$ are self-adjoint for every $\tilde Q$, including the zero divisors.

**The isometries.** For the plain form, $T_{\tilde Q,\tilde P}$ preserves it exactly when
$$
\tilde P\tilde Q=\pm e_t.
$$
Then both parameters are units, $\tilde P=\pm\tilde Q^{-1}$, and the operator is $\pm\mathrm{Ad}_{\tilde Q}$. The group is $\{\pm\mathrm{Ad}_{\tilde Q}\}\cong(\mathbb{B}^{\times}/\mathbb{C}^{\times})\times\{\pm1\}$, of complex dimension three.

*Proof.* An isometry is injective, because the form is non-degenerate, so both parameters are units. Then $T^{\approx}T=\mathrm{id}$ reads
$$
T_{\tilde P,\tilde Q}T_{\tilde Q,\tilde P}
=T_{\tilde P\tilde Q,\ \tilde P\tilde Q}
=T_{e_t,e_t}.
$$
The fibre theorem, applied to the nonzero pairs $(\tilde P\tilde Q,\tilde P\tilde Q)$ and $(e_t,e_t)$, gives $\tilde P\tilde Q=\lambda e_t$ and $\tilde P\tilde Q=\lambda^{-1}e_t$; hence $\lambda^2=1$ and $\tilde P\tilde Q=\pm e_t$. Then $\tilde Q\tilde P=\pm e_t$ as well. Conversely, $\tilde P=\pm\tilde Q^{-1}$ makes the operator $\pm\mathrm{Ad}_{\tilde Q}$, which preserves the scalar part.

**The multiplicative members.** A nonzero $T_{\tilde Q,\tilde P}$ is multiplicative,
$$
T_{\tilde Q,\tilde P}(XY)=T_{\tilde Q,\tilde P}(X)\,T_{\tilde Q,\tilde P}(Y)
\quad\text{for all }X,Y,
$$
exactly when $\tilde P=\tilde Q^{-1}$, equivalently $\tilde Q\tilde P=\tilde P\tilde Q=e_t$; then $T_{\tilde Q,\tilde P}=\mathrm{Ad}_{\tilde Q}$.

*Proof.* The identity reads
$$
\tilde QX\tilde P\,\tilde QY\tilde P=\tilde QXY\tilde P,
$$
that is $\tilde QX(\tilde P\tilde Q-e_t)Y\tilde P=0$ for all $X,Y$. Since $\tilde Q$ and $\tilde P$ are nonzero, the matrix units force $\tilde P\tilde Q=e_t$; then $\tilde P=\tilde Q^{-1}$ and $\tilde Q\tilde P=e_t$. Conversely, $\tilde P=\tilde Q^{-1}$ gives $T(X)=QXQ^{-1}$, which is multiplicative.

**The three criteria.**

| property | criterion on the pair | operator |
|---|---|---|
| self-adjoint for the plain form | $\tilde P=\lambda\tilde Q$ | $T_{\tilde Q,\lambda\tilde Q}$ |
| isometry of the plain form | $\tilde P\tilde Q=\pm e_t$ | $\pm\mathrm{Ad}_{\tilde Q}$ |
| multiplicative, nonzero | $\tilde P=\tilde Q^{-1}$ | $\mathrm{Ad}_{\tilde Q}$ |

**The absence of a pin group.** The quadratic form $\mathfrak Q(\tilde Q)=\operatorname{Sc}(\tilde Q^2)$ is not multiplicative:
$$
\mathfrak Q\!\left(\frac{5e_t+4\tilde e_x}{3}\right)
=\mathfrak Q\!\left(\frac{5e_t+4\tilde e_y}{3}\right)=1,
\qquad
\mathfrak Q\!\left(\frac{(5e_t+4\tilde e_x)(5e_t+4\tilde e_y)}{9}\right)
=-\frac{431}{81}.
$$
Hence no level set is a subgroup, and the family carries no pin group. The isometry group is only $\{\pm\mathrm{Ad}_{\tilde Q}\}$, of dimension three, not the full orthogonal group of dimension six; the pin group of the quadratic space is built in the Clifford algebra and is not contained in the family. There is also no nonzero skew-adjoint member: $(T_{\tilde Q,\tilde P})^{\approx}=-T_{\tilde Q,\tilde P}$ forces $T_{\tilde Q,\tilde P}=0$.

## What the Factorization Buys

**It gives.** The factorization gives five things at once: a parametrisation of the cone by two biquaternions, eight complex parameters modulo the scaling, hence seven effective parameters; a composition law, hence powers, inverses and the monoid structure; the rank-one criterion for a single product; the length formula $\ell(M)=\operatorname{rank}c(M)$, with length at most four; and a type theory, the two adjoints and the three criteria of §*The Adjoints and the Three Criteria*.

**It does not give.** It gives no additivity: the image is a cone, not a subspace, and the sum of two products is generally not a product. It gives no universality: not every matrix in $M_4(\mathbb{C})$ is a single product, four are needed generically, and four always suffice. It gives no division algebra: the sixteen cells are units, but the cone contains singular products and the span contains zero divisors. It gives no pin group: the form $\operatorname{Sc}(\tilde Q^2)$ is not multiplicative, and the isometry group of the family is only $\{\pm\mathrm{Ad}_{\tilde Q}\}$, of dimension three.

**The one-line form.** Every two-sided operator is one product $T_{\tilde Q,\tilde P}=L_{\tilde Q}R_{\tilde P}=B_P^{\mathsf T}\otimes B_Q$; the set of products is the seven-dimensional cone of pure tensors in $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}=M_4(\mathbb{C})$, cut out by $\operatorname{rank}c(M)\le1$, closed under composition with the second slot reversed and not under addition, with length $\operatorname{rank}c(M)\in\{0,1,2,3,4\}$ and matrix rank in $\{0,1,2,4\}$.

## Summary

The two-sided operator $T_{\tilde Q,\tilde P}(X)=\tilde QX\tilde P$ has matrix $B_P^{\mathsf T}\otimes B_Q$ in the Peirce frame, with trace $4Q_tP_t$, determinant $\langle\tilde Q\rangle_{\natural}^2\langle\tilde P\rangle_{\natural}^2$ and rank the product of the two $2\times2$ ranks. The sixteen basis matrices $T_{\mu\nu}=L_\mu R_\nu$ are a basis of $M_4(\mathbb{C})$, orthogonal for the Hilbert–Schmidt form with $\operatorname{Tr}(T_{\mu\nu}^{\dagger}T_{\rho\sigma})=4\delta_{\mu\rho}\delta_{\nu\sigma}$, and every one of them is invertible. The coefficient matrix $c(M)$ in this basis is a linear coordinate on $M_4(\mathbb{C})$; for a product it is the rank-one matrix $[Q][P]^{\mathsf T}$, and the length of $M$ is $\operatorname{rank}c(M)$, at most four. The product set is the seven-dimensional cone over the Segre variety. Five cells give a gamma frame whose Clifford relations fix the algebra but not the pair of spatial directions. The parameter map is bilinear with one-dimensional fibres, so the product set is a cone and not a subspace, a monoid and not an additive semigroup; under $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}\cong M_4(\mathbb{C})$ it is the cone of pure tensors. The Hilbert–Schmidt adjoint is $\mathsf T(\tilde Q,\tilde P)^{\dagger}=\mathsf T(\tilde Q^{*},\tilde P^{*})$ and the plain adjoint is $(T_{\tilde Q,\tilde P})^{\approx}=T_{\tilde P,\tilde Q}$; self-adjointness is $\tilde P=\lambda\tilde Q$, isometry is $\tilde P\tilde Q=\pm e_t$, multiplicativity is $\tilde P=\tilde Q^{-1}$, and the family contains no pin group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_{\tilde Q,\tilde P}$ | the operator $X\mapsto\tilde QX\tilde P$ |
| $\mathsf T(\tilde Q,\tilde P)$ | its matrix, $B_P^{\mathsf T}\otimes B_Q$ |
| $T_{\mu\nu}$ | the matrix of the unit pair $(e_\mu,e_\nu)$ |
| $c(M)$ | the coefficient matrix in the basis $T_{\mu\nu}$ |
| $\ell(M)=\operatorname{rank}c(M)$ | the least number of products |
| $\Phi$ | the bilinear map $(\tilde Q,\tilde P)\mapsto\mathsf T(\tilde Q,\tilde P)$ |
| $(\cdot)^{\approx}$ | the plain adjoint for $\operatorname{Sc}(XY)$ |
| $\tilde Q^{*}$ | the Hermitian conjugate, $\mathsf M_2(\tilde Q^{*})=\mathsf M_2(\tilde Q)^{\dagger}$ |
| $\operatorname{Sc}$ | the scalar part, $\operatorname{Sc}(X)=\tfrac12\operatorname{Tr}\mathsf M_2(X)$ |
| $\mathrm{Ad}_{\tilde Q}$ | the inner automorphism $X\mapsto\tilde QX\tilde Q^{-1}$ |
| $[Q]$ | the coefficient column of $\tilde Q$ |
| $\gamma_0,\gamma_1,\gamma_2,\gamma_3,\gamma_5$ | the gamma frame |
| $\beta,\delta$ | the free orthogonal pair of the frame |
| $P_\pm$ | the chirality projectors |
| $C_{\Pi}$ | the Peirce change |

## Further Reading

- [Matrix Representations : The Left Regular Operators](matrix-representations-the-left-regular-operators.html), for the left family
- [Matrix Representations : The Right Regular Operators](matrix-representations-the-right-regular-operators.html), for the right family
- [Matrix Representations : The Hermitian Sandwich](matrix-representations-the-hermitian-sandwich.html), for $\tilde QX\tilde Q^{*}$
- [Matrix Representations : The Models and the Change of Frame](matrix-representations-the-models-and-the-change-of-frame.html), for the frames
- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the operator statements
- [The Four Adjoints of the Biquaternion Algebra in Examples](the-four-adjoints-of-the-biquaternion-algebra-in-examples.html), for the plain adjoint and the one-sided identities
- [The Coefficient Matrix of a Two-Sided Operator : A Worked Computation](the-coefficient-matrix-of-a-two-sided-operator-a-worked-computation.html), for a full computation
- [The Two-Sided Operators and the Spin Group](the-two-sided-operators-and-the-spin-group.html), for the gamma frame and the spin group
- [The Extraspecial Group of the Two-Sided Matrices of $M_4(\mathbb{C})$](the-extraspecial-group-of-the-two-sided-matrices-of-m4c.html), for the finite group of cells
