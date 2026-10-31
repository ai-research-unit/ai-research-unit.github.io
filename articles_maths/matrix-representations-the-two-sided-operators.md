# __Matrix Representations : The Two-Sided Operators__

## Introduction

The two-sided operator sends $X$ to $\tilde QX\tilde P$. It is the most general product of a left and a right multiplication, and its matrix is the product of the left and right matrices. The sixteen operators obtained from the four units in each slot form a basis of the whole algebra $M_4(\mathbb{C})$. The basis is orthogonal for the Hilbert–Schmidt form, every basis matrix is invertible, and yet the span contains matrices of every rank.

This article computes the two-sided family in the two displays. It gives the sixteen basis matrices, their composition, trace, determinant and orthogonality, the coefficient matrix of a general $4\times4$ matrix in this basis, the gamma frame built from five cells, and the cone of products with the rank criterion. It is the third of the three articles on the regular operator families; the left family is *Matrix Representations : The Left Regular Operators* and the right family is *Matrix Representations : The Right Regular Operators*.

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
with identity $T_{e_t,e_t}$. The order in the second slot is reversed, because the right multiplication by $\tilde P$ acts first.

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

**The inverse.** On the invertible locus,
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
and its first column is $-i$ times the coordinate column of $\tilde\Pi_-$. The entry is the check that the two-sided table agrees with the exchange.

**The complete product table.** The product of two basis matrices is again a basis matrix up to sign,
$$
T_{\mu\nu}T_{\rho\sigma}=\epsilon\epsilon'\,T_{\mu'\nu'},
\qquad
e_\mu e_\rho=\epsilon e_{\mu'},\quad e_\sigma e_\nu=\epsilon' e_{\nu'}.
$$
The sixteen are closed under multiplication up to sign and contain the identity, but they do not form a group, because $-T_{\mu\nu}$ is not among them.

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

**The length.** The length $\ell(M)$ is the least number of products whose sum is $M$. Then
$$
\ell(M)=\operatorname{rank}c(M).
$$
Indeed a sum of $r$ products has coefficient matrix a sum of $r$ rank-one matrices, and conversely a rank factorization $c=UV$ gives $r$ products from the columns of $U$ and the rows of $V$. Every matrix is a sum of at most four products, and $\ell(M)=4$ exactly when $\det c(M)\neq0$, which is the generic case.

**The criterion.** For $M\neq0$,
$$
M=T_{\tilde Q,\tilde P}\ \text{for some }\tilde Q,\tilde P
\iff
\operatorname{rank}c(M)=1 .
$$
The product set is the closed cone cut out by the $2\times2$ minors of $c(M)$; its projectivisation is the Segre variety $\mathbb{P}^3\times\mathbb{P}^3$, of complex dimension six, and the cone has complex dimension seven in the sixteen-dimensional algebra.

**The parametrisation.** The map $(\tilde Q,\tilde P)\mapsto T_{\tilde Q,\tilde P}$ is bilinear and onto the cone. Its fibre over a nonzero product is the scaling orbit $(\lambda\tilde Q,\lambda^{-1}\tilde P)$, which is why the cone has dimension $8-1=7$.

**The intersections.** The cone meets the left family in the left family and the right family in the right family, and the two meet in the scalars. The generic product lies in neither one-sided family.

**The two ranks are independent.**

| $M$ | $\operatorname{rank}M$ | $\ell(M)$ |
|---|---|---|
| $T_{tt}+T_{tz}=T_{e_t,e_t+e_z}$ | $4$ | $1$ |
| $P_+$ | $2$ | $1$ |
| $T_{\tilde Q,\tilde P}$ with both parameters zero divisors | $1$ | $1$ |
| $T_{tt}+T_{xx}$ | $2$ | $2$ |
| $M_1=(u_2+u_3)(u_2+u_3)^{\mathsf T}$ | $1$ | $4$ |
| generic $M$ | $4$ | $4$ |

The matrix $M_1$ has coefficient matrix $\tfrac12\operatorname{diag}(1,-1,1,1)$, of rank four, so it needs four products although it has rank one. The projector $P_+$ has rank two and needs one. Neither rank determines the other.

**How to decide.** Compute the sixteen numbers $\tfrac14\operatorname{Tr}(T_{\mu\nu}^{\dagger}M)$ and form $c$. If $\operatorname{rank}c=1$, take a nonzero column of $c$ for $[Q]$ and the corresponding row, divided by the pivot, for $[P]^{\mathsf T}$. If the rank is $r>1$, a rank factorization of $c$ gives the $r$ terms.

## Summary

The two-sided operator $T_{\tilde Q,\tilde P}(X)=\tilde QX\tilde P$ has matrix $B_P^{\mathsf T}\otimes B_Q$ in the Peirce frame, with trace $4Q_tP_t$, determinant $\langle\tilde Q\rangle_{\natural}^2\langle\tilde P\rangle_{\natural}^2$ and rank the product of the two $2\times2$ ranks. The sixteen basis matrices $T_{\mu\nu}=L_\mu R_\nu$ are a basis of $M_4(\mathbb{C})$, orthogonal for the Hilbert–Schmidt form with $\operatorname{Tr}(T_{\mu\nu}^{\dagger}T_{\rho\sigma})=4\delta_{\mu\rho}\delta_{\nu\sigma}$, and every one of them is invertible. The coefficient matrix $c(M)$ in this basis is a linear coordinate on $M_4(\mathbb{C})$; for a product it is the rank-one matrix $[Q][P]^{\mathsf T}$, and the length of $M$ is $\operatorname{rank}c(M)$, at most four. The product set is the cone over the Segre variety, of complex dimension seven. Five cells give a gamma frame whose Clifford relations fix the algebra but not the pair of spatial directions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_{\tilde Q,\tilde P}$ | the operator $X\mapsto\tilde QX\tilde P$ |
| $\mathsf T(\tilde Q,\tilde P)$ | its matrix, $B_P^{\mathsf T}\otimes B_Q$ |
| $T_{\mu\nu}$ | the matrix of the unit pair $(e_\mu,e_\nu)$ |
| $c(M)$ | the coefficient matrix in the basis $T_{\mu\nu}$ |
| $\ell(M)=\operatorname{rank}c(M)$ | the least number of products |
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
- [The Coefficient Matrix of a Two-Sided Operator : A Worked Computation](the-coefficient-matrix-of-a-two-sided-operator-a-worked-computation.html), for a full computation
- [The Two-Sided Operators and the Spin Group](the-two-sided-operators-and-the-spin-group.html), for the gamma frame and the spin group
- [The Extraspecial Group of the Two-Sided Matrices of $M_4(\mathbb{C})$](the-extraspecial-group-of-the-two-sided-matrices-of-m4c.html), for the finite group of cells
