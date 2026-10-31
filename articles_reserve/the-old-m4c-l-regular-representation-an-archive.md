# __The Old $M_4(\mathbb{C})_L$ Regular Representation : An Archive__

## Introduction

**The old $M_4(\mathbb{C})_L$ representation is the left regular matrix of the biquaternion algebra written in the coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, and this article preserves it.** The current corpus writes the same operator in the canonical Peirce frame, where the matrix is $I_2\otimes\mathsf M_2(\tilde Q)$. The two displays are the same representation in two frames, but the entries, the block structure and the transpose dictionary differ, and a computation copied from an old article cannot be read without the frame that produced it.

**What is preserved.** The explicit left and right matrices, the sixteen two-sided matrices $T_{\mu\nu}$, the transpose and dagger identities, the old block decomposition, the two changes of frame that appear in the old material, and the entries of the gamma frame read in the old basis. The article also records why the label and the frame were retired, and what a reader must change when moving a computation to the current frame.

**Status.** This is a reserve article. It documents a retired display and is not a statement of the current convention. The label $M_4(\mathbb{C})_L$ is retired by *Conventions in Mathematics*, §*The Matrix Models*: an old article that writes it is read as $M_4(\mathbb{C})_{\mathbb{B},L}$. The matrices below are the old matrices, not the current default. The algebra, the trace, the determinant and the operator identities are unchanged; only the frame is archived.

## The Retired Label

**The old label named a matrix set, and the new label names an algebra.** In the old articles $M_4(\mathbb{C})_L$ was the set of matrices $\mathsf M_4^{L}(\tilde Q)$ in the coefficient basis, a four-dimensional subspace of $M_4(\mathbb{C})$. The same symbol therefore denoted a different set after a change of basis. The current writing separates the two objects: $\mathbb{B}_L=M_4(\mathbb{C})_{\mathbb{B},L}=\rho_L(\mathbb{B})$ is the image algebra, and $\mathsf M_4^{L}(\tilde Q)$ is its matrix in the frame an article names.

| old writing | current reading |
|---|---|
| $M_4(\mathbb{C})_L$ | $M_4(\mathbb{C})_{\mathbb{B},L}=\mathbb{B}_L$ |
| $M_4(\mathbb{C})_R$ | $M_4(\mathbb{C})_{\mathbb{B},R}=\mathbb{B}_R$ |
| $\mathsf M_4(\tilde Q)$ for the left matrix | $\mathsf M_4^{L}(\tilde Q)$ |
| $M_4(\mathbb{C})_L$ Model : $X$ | $M_4(\mathbb{C})$ Model : $X$ |

**The old matrix is the coefficient display.** In the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ the left regular matrix has one coefficient per entry, with a sign and no sum. That is the display archived here. It is not the matrix of the element in the abstract sense: the element is $\tilde Q$, the operator is $\rho_L(\tilde Q)$, and the matrix depends on the frame.

## The Left Matrix

**Definition.** The left regular matrix $\mathsf M_4^{L}(\tilde Q)$ is the $4\times4$ matrix whose $\mu$-th column is the coordinate column of $\tilde Q e_\mu$ in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$. For $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$,

$$
\mathsf M_4^{L}(\tilde Q)=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&-Q_z&Q_y\\
Q_y&Q_z&Q_t&-Q_x\\
Q_z&-Q_y&Q_x&Q_t
\end{pmatrix}.
$$

Every entry is a single coefficient with a sign; no entry is a sum.

**Example.** For $\tilde Q=(2+i)e_t+(1-i)\vec e_x+3\vec e_y+i\vec e_z$,

$$
\mathsf M_4^{L}(\tilde Q)=
\begin{pmatrix}
2+i&-1+i&-3&-i\\
1-i&2+i&-i&3\\
3&i&2+i&-1+i\\
i&-3&1-i&2+i
\end{pmatrix}.
$$

The trace is $8+4i=4(2+i)$ and the determinant is $117+44i=(11+2i)^2$, with $\langle\tilde Q\rangle_{\natural}=11+2i$. The column of $e_t+\vec e_x$ is the sum of the first two columns, $(1+2i,\,3,\,3+i,\,-3+i)$, which is the coordinate column of $\tilde Q(e_t+\vec e_x)$.

**Proposition.** The assignment is an injective algebra homomorphism:
$$
\mathsf M_4^{L}(\tilde Q_1)\mathsf M_4^{L}(\tilde Q_2)=\mathsf M_4^{L}(\tilde Q_1\tilde Q_2),\qquad
\mathsf M_4^{L}(\tilde Q)=0\iff\tilde Q=0.
$$
The first column alone recovers $\tilde Q$, so the map is injective. The image is a four-dimensional complex subalgebra of $M_4(\mathbb{C})$, and its unit is $\mathrm I_4$.

**The invariants.** For every $\tilde Q$,
$$
\operatorname{Tr}\mathsf M_4^{L}(\tilde Q)=4Q_t,\qquad
\det\mathsf M_4^{L}(\tilde Q)=\langle\tilde Q\rangle_{\natural}^{2}.
$$
The determinant is the square of the $2\times2$ determinant, because the regular model is two copies of the $2\times2$ model.

## The Right Matrix

**Definition.** The right regular matrix $\mathsf M_4^{R}(\tilde Q)$ has $\mu$-th column the coordinate column of $e_\mu\tilde Q$. In the same basis,

$$
\mathsf M_4^{R}(\tilde Q)=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&Q_z&-Q_y\\
Q_y&-Q_z&Q_t&Q_x\\
Q_z&Q_y&-Q_x&Q_t
\end{pmatrix}.
$$

**Proposition.** The right matrix is anti-multiplicative,
$$
\mathsf M_4^{R}(\tilde Q_1)\mathsf M_4^{R}(\tilde Q_2)=\mathsf M_4^{R}(\tilde Q_2\tilde Q_1),
$$
and it commutes with the left matrix, $\mathsf M_4^{L}(a)\mathsf M_4^{R}(b)=\mathsf M_4^{R}(b)\mathsf M_4^{L}(a)$.

**The relation between the two.** Let
$$
D=\operatorname{diag}(1,-1,-1,-1),
$$
the matrix of the quaternion conjugate in this basis: the coordinate column of $\tilde Q^{\natural}$ is $D$ times the coordinate column of $\tilde Q$. Then
$$
\mathsf M_4^{R}(\tilde Q)=D\,\mathsf M_4^{L}(\tilde Q)^{\mathsf T}D
=D\,\mathsf M_4^{L}(\tilde Q^{\natural})\,D .
$$
The old articles used $D=\operatorname{diag}(-1,1,1,1)$, which gives the same product because the two sign changes cancel; the sign of $D$ is immaterial. The relation is a statement about the coefficient basis, not about the operator.

**The commutator.** The $\mu$-th column of $\mathsf M_4^{L}(\tilde Q)-\mathsf M_4^{R}(\tilde Q)$ is the coordinate column of $[\tilde Q,e_\mu]$. The difference vanishes exactly when $\tilde Q$ is central, that is, when $\tilde Q=Q_te_t$.

## The Sixteen Two-Sided Matrices

**Definition.** For $\mu,\nu\in\{t,x,y,z\}$ set
$$
T_{\mu\nu}=L_\mu R_\nu,\qquad L_\mu=\mathsf M_4^{L}(e_\mu),\quad R_\nu=\mathsf M_4^{R}(e_\nu).
$$
The matrix $T_{\mu\nu}$ is the matrix of $x\mapsto e_\mu xe_\nu$. A general two-sided operator is $T_{a,b}=\sum_{\mu,\nu}a_\mu b_\nu T_{\mu\nu}$.

**The four left matrices.** With $L_t=\mathrm I_4$,
$$
L_x=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\quad
L_y=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\quad
L_z=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
$$

**The four right matrices.** With $R_t=\mathrm I_4$,
$$
R_x=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix},\quad
R_y=\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\1&0&0&0\\0&1&0&0\end{pmatrix},\quad
R_z=\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix}.
$$

**Proposition (the sixteen are a basis).** The matrices $T_{\mu\nu}$ are distinct, invertible, of determinant $1$ and rank $4$, and linearly independent. They are a basis of $M_4(\mathbb{C})$. Each is a signed permutation matrix, because the four left and the four right matrices are signed permutations.

**The table.** The four families are
$$
T_{t\nu}=R_\nu,\qquad T_{\mu t}=L_\mu,\qquad T_{jk}=L_jR_k\quad(j,k=x,y,z).
$$
For example
$$
T_{tx}=R_x,\qquad
T_{xy}=L_xR_y=
\begin{pmatrix}0&0&0&1\\0&0&-1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix}.
$$

**Trace, determinant, inverse.** For $a,b$ with $\langle a\rangle_{\natural}\langle b\rangle_{\natural}\neq0$,
$$
\operatorname{Tr}T_{a,b}=4a_tb_t,\qquad
\det T_{a,b}=\langle a\rangle_{\natural}^{2}\langle b\rangle_{\natural}^{2},\qquad
T_{a,b}^{-1}=T_{a^{-1},b^{-1}}.
$$
Hence $\operatorname{Tr}T_{\mu\nu}=4$ only for $T_{tt}$, and $0$ for the other fifteen; every basis matrix has determinant $1$.

**Composition.** The product of two basis matrices is a basis matrix up to sign. Writing $e_\mu e_\rho=\varepsilon e_{\mu'}$ and $e_\sigma e_\nu=\varepsilon' e_{\nu'}$, with $\varepsilon,\varepsilon'=\pm1$,
$$
T_{\mu\nu}T_{\rho\sigma}=\varepsilon\varepsilon'\,T_{\mu'\nu'}.
$$
Half of the $256$ products carry a minus sign: $T_{tx}^2=-T_{tt}$, for instance. The sixteen are therefore not closed under multiplication and are not a group; the group they generate is the extraspecial group $Q_8\circ Q_8$, of order $32$, and $-T_{\mu\nu}$ is one of its elements but not one of the sixteen.

**Orthogonality.** For the Hilbert–Schmidt form $\langle A,B\rangle=\operatorname{Tr}(A^{\dagger}B)$,
$$
\operatorname{Tr}\bigl(T_{\mu\nu}^{\dagger}T_{\rho\sigma}\bigr)=4\,\delta_{\mu\rho}\delta_{\nu\sigma}.
$$
The sixteen are an orthogonal basis, each of norm $2$.

**A singular sum.** Every basis matrix is invertible, but a sum need not be:
$$
T_{tt}+T_{xx}=\operatorname{diag}(0,0,2,2),
$$
of rank two. The algebra is simple and has many zero divisors.

**Products and length.** The old frame supports the same product test as the current one. Every $M\in M_4(\mathbb{C})$ has a unique expansion $M=\sum c_{\mu\nu}T_{\mu\nu}$, with
$$
c(M)_{\mu\nu}=\tfrac14\operatorname{Tr}\bigl(T_{\mu\nu}^{\dagger}M\bigr).
$$
Then $M=L_aR_b$ exactly when $c(M)=ab^{\mathsf T}$ has rank one, and the least number of products summing to $M$ is $\operatorname{rank}c(M)$. The current article proves the statement; the old frame changes the entries of $c$, not the criterion.

## The Old Block Decomposition

**The old articles obtained the two copies from a basis adapted to a minimal left ideal, not from the Peirce matrix.** Let
$$
\tilde\Pi=\tfrac12(e_t+i\vec e_x),\qquad f=e_t-\tilde\Pi=\tfrac12(e_t-i\vec e_x),
$$
and let $\tilde Q_4=\vec e_z+i\vec e_y$, $\tilde Q_7=\vec e_z-i\vec e_y$. The four vectors
$$
(\tilde\Pi,\ \tilde Q_4,\ f,\ \tilde Q_7)
$$
are a basis of $\mathbb{B}$, adapted to the splitting $\mathbb{B}=\mathbb{B}\tilde\Pi\oplus\mathbb{B}f$ into two minimal left ideals. In this basis the regular matrix is block diagonal,
$$
\mathsf M_4^{L}(\tilde Q)=
\begin{pmatrix}A_+&0\\0&A_-\end{pmatrix},
$$
where $A_+$ and $A_-$ are conjugate to $\mathsf M_2(\tilde Q)$. Each block has trace $2Q_t$ and determinant $\langle\tilde Q\rangle_{\natural}$; the total trace is $4Q_t$ and the total determinant is $\langle\tilde Q\rangle_{\natural}^{2}$.

**The ideal basis.** The two vectors $\tilde\Pi,\tilde Q_4$ span $\mathbb{B}\tilde\Pi$, because $\tilde Q_4=2e_z\tilde\Pi$, and $f,\tilde Q_7$ span $\mathbb{B}f$, because $\tilde Q_7=2e_zf$. Left multiplication preserves each ideal, so the matrix is block diagonal in this basis. The old article used this basis; the current canonical frame uses the standard pair $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ and $\vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y)$ instead.

## Two Changes of Frame

**The old change matrix.** The old product article displayed
$$
T_{\mathrm{old}}=\frac12
\begin{pmatrix}
1&0&0&1\\
0&i&i&0\\
0&-1&1&0\\
i&0&0&-i
\end{pmatrix},
\qquad
\det T_{\mathrm{old}}=\tfrac14,
$$
whose columns are $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$. In that order the coefficient matrix becomes the $2\times2$ block matrix whose $(i,j)$ block is $A_{ij}\mathrm I_2$,
$$
T_{\mathrm{old}}^{-1}\mathsf M_4^{L}(\tilde Q)T_{\mathrm{old}}
=
\begin{pmatrix}
A_{11}&0&A_{12}&0\\
0&A_{11}&0&A_{12}\\
A_{21}&0&A_{22}&0\\
0&A_{21}&0&A_{22}
\end{pmatrix},
\qquad A=\mathsf M_2(\tilde Q).
$$
This is $A\otimes\mathrm I_2$ in the convention in which the element factor is first.

**The current change matrix.** The canonical frame orders the columns as $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$ and uses
$$
S=\frac12
\begin{pmatrix}
1&0&0&1\\
0&i&i&0\\
0&1&-1&0\\
i&0&0&-i
\end{pmatrix},
\qquad
\det S=-\tfrac14,
$$
with
$$
S^{-1}\mathsf M_4^{L}(\tilde Q)S
=\operatorname{diag}\bigl(\mathsf M_2(\tilde Q),\mathsf M_2(\tilde Q)\bigr)
=\mathrm I_2\otimes\mathsf M_2(\tilde Q).
$$
This is the display the current articles use.

**The relation.** The two changes differ by the swap of the two mixed columns:
$$
T_{\mathrm{old}}=S\,P,\qquad
P=\begin{pmatrix}1&0&0&0\\0&0&1&0\\0&1&0&0\\0&0&0&1\end{pmatrix},\qquad \det P=-1.
$$
The determinants therefore have opposite signs, $+\tfrac14$ and $-\tfrac14$. The two displays carry the same two copies, in opposite tensor orders: the old order puts the element factor first, the current order puts it second and makes the two copies literal diagonal blocks.

**A warning.** An old display with determinant $+\tfrac14$ is read with $T_{\mathrm{old}}$; a current display with determinant $-\tfrac14$ is read with $S$. Mixing the two orders swaps the two mixed columns and changes the sign of every mixed entry.

## What the Old Frame Reads Directly

**The remarkable subspaces.** In the coefficient basis the images of the six subspaces are entrywise conditions.

| subspace | image under $\mathsf M_4^{L}$ | condition |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | the scalar matrices | $M=A\mathrm I_4$ |
| $\mathrm{Vect}(\mathbb{B})$ | the traceless matrices | $\operatorname{Tr}M=0$ |
| $\mathbb{H}_{\mathbb{B}}$ | the real matrices | every entry real |
| $i\mathbb{H}_{\mathbb{B}}$ | the purely imaginary matrices | every entry in $i\mathbb{R}$ |
| $\mathbb{M}_+$ | the Hermitian matrices | $M=M^{\dagger}$ |
| $\mathbb{M}_-$ | the anti-Hermitian matrices | $M=-M^{\dagger}$ |

The first two rows use $\operatorname{Tr}\mathsf M_4^{L}(\tilde Q)=4Q_t$; the middle two use that the entries are the coefficients up to sign; the last two use that $\mathsf M_4^{L}(\vec e_k)$ is real and skew-symmetric, so a Hermitian element $a e_t+i\vec b\cdot\vec e$ has matrix $a\mathrm I_4+i\sum_kb_k\mathsf M_4^{L}(\vec e_k)$, which is Hermitian.

**The transpose and the dagger.** In this basis,
$$
\mathsf M_4^{L}(\tilde Q)^{\mathsf T}=\mathsf M_4^{L}(\tilde Q^{\natural}),
\qquad
\mathsf M_4^{L}(\tilde Q)^{\dagger}=\mathsf M_4^{L}(\tilde Q^{*}).
$$
The first identity is the reason the coefficient basis is kept for the transpose dictionary; the second holds in the canonical frame as well, because both bases are orthogonal with all four vectors of one norm. The difference between the frames is the transpose, not the dagger.

**The gamma frame in the old display.** The five operators of the current gamma frame are the same five cells in either frame:
$$
\gamma^0=iT_{tx}=iR_x,\qquad
\gamma^1=iT_{xy}=iL_xR_y,\qquad
\gamma^2=iT_{yy}=iL_yR_y,\qquad
\gamma^3=iT_{zy}=iL_zR_y,\qquad
\gamma_5=-iT_{tz}=-iR_z .
$$
In the coefficient basis they are $i$ times signed permutations. In the canonical frame the same operators read
$$
\gamma^0=\sigma_1\otimes\mathrm I_2,\qquad
\gamma^k=i\sigma_2\otimes\sigma_k\quad(k=1,2,3),\qquad
\gamma_5=-\sigma_3\otimes\mathrm I_2 .
$$
The Clifford relations and the product $\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3$ hold in both displays; the matrices are conjugates of one another, not different operators.

## What the Canonical Frame Changes

| object | old coefficient basis | canonical Peirce frame |
|---|---|---|
| $\mathsf M_4^{L}(\tilde Q)$ | the explicit matrix above | $\mathrm I_2\otimes\mathsf M_2(\tilde Q)$ |
| $\mathsf M_4^{R}(\tilde Q)$ | $D\mathsf M_4^{L}(\tilde Q)^{\mathsf T}D$ | $\mathsf M_2(\tilde Q)^{\mathsf T}\otimes\mathrm I_2$ |
| $T_{a,b}$ | $L_aR_b$, a signed permutation | $\mathsf M_2(b)^{\mathsf T}\otimes\mathsf M_2(a)$ |
| transpose | $\mathsf M_4^{L}(\tilde Q)^{\mathsf T}=\mathsf M_4^{L}(\tilde Q^{\natural})$ | $\mathsf M_4^{L}(\tilde Q)^{\mathsf T}=K\,\mathsf M_4^{L}(\tilde Q^{\natural})\,K$ |
| dagger | $\mathsf M_4^{L}(\tilde Q)^{\dagger}=\mathsf M_4^{L}(\tilde Q^{*})$ | the same |
| block form | $A\otimes\mathrm I_2$ in the old order, or two conjugate blocks in the ideal basis | $\operatorname{diag}(A,A)$ |
| quaternion subspace | the real matrices | not an entrywise condition |

In the transpose row,
$$
K=\begin{pmatrix}0&0&0&1\\0&0&-1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix},\qquad K^2=\mathrm I_4,
$$
is the signed reversal of the four Peirce coordinates, and $K=2S^{\mathsf T}S$. The identity is the canonical-frame form of the old transpose; it is not a different involution.

## Why the Corpus Moved

**Three reasons, and one cost.** The canonical frame makes the two Peirce planes literal diagonal blocks, so the module structure is visible in the matrix. It makes the gamma cells simple tensor products, so the Clifford construction closes without a change of basis. It removes the label ambiguity: the copy is the algebra $\mathbb{B}_L$, not a matrix set tied to a basis. The cost is the transpose: quaternion conjugation is no longer transposition, and the old transpose identity must be replaced by conjugation with $K$.

**What the old frame remains good for.** The coefficient basis is the frame in which the entries are the coefficients, the real forms are entrywise, and the transpose is the natural involution. An article whose subject is the transpose dictionary or the entrywise real structure keeps it, and says so. An article whose subject is the Peirce planes, the gamma frame or the block decomposition uses the canonical frame. The two are the same representation, and an entry is read only with the frame that produced it.

## Verification

The identities of this article were recomputed on random elements and on the sixteen basis matrices. The checks were: multiplicativity and anti-multiplicativity; the transpose and dagger identities; the relation $\mathsf M_4^{R}=D\mathsf M_4^{L\mathsf T}D$; the trace and determinant; the orthogonality, determinant, composition and trace of the sixteen $T_{\mu\nu}$; the two changes of frame and the relation $T_{\mathrm{old}}=SP$; the old block decomposition; and the two displays of the five gamma operators. The discrepancies were zero to machine precision.

## Summary

The old $M_4(\mathbb{C})_L$ representation is the left regular matrix in the coefficient basis. Its entries are the coefficients of the element with signs; its trace is $4Q_t$; its determinant is $\langle\tilde Q\rangle_{\natural}^{2}$; its transpose is the matrix of the quaternion conjugate; and its right partner is $D\mathsf M_4^{L\mathsf T}D$. The sixteen matrices $T_{\mu\nu}=L_\mu R_\nu$ are a signed-permutation basis of $M_4(\mathbb{C})$, orthogonal for the Hilbert–Schmidt form. The old change matrix $T_{\mathrm{old}}$ has determinant $+\tfrac14$ and gives $A\otimes\mathrm I_2$; the current change $S$ has determinant $-\tfrac14$ and gives $\mathrm I_2\otimes A$. The two differ by the swap of the two mixed columns. The label $M_4(\mathbb{C})_L$ is retired; the algebra is $\mathbb{B}_L$, and the matrix is read in the frame an article names. The canonical frame is the current default; this coefficient display is archived because the transpose, the real forms and the old computations are read in it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, complex dimension $4$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the coefficient basis |
| $\mathsf M_4^{L}(\tilde Q)$ | the left regular matrix in the coefficient basis |
| $\mathsf M_4^{R}(\tilde Q)$ | the right regular matrix in the coefficient basis |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | the quaternion conjugation matrix in this basis |
| $T_{\mu\nu}=L_\mu R_\nu$ | the sixteen two-sided basis matrices |
| $T_{a,b}=L_aR_b$ | the two-sided operator $x\mapsto axb$ |
| $T_{\mathrm{old}}$ | the old change matrix, columns $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$, $\det=\tfrac14$ |
| $S$ | the current change matrix, columns $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$, $\det=-\tfrac14$ |
| $K$ | the signed reversal, $K=2S^{\mathsf T}S$, the canonical-frame transpose carrier |
| $\gamma^0,\gamma^1,\gamma^2,\gamma^3,\gamma_5$ | the five cells of the gamma frame, read in either display |
| $\langle\tilde Q\rangle_{\natural}$ | the central scalar $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ |

## Further Reading

- [Conventions in Mathematics](../articles_maths/conventions-in-mathematics), §*The Matrix Models*, for the current labels, the canonical frame and the retirement of $M_4(\mathbb{C})_L$
- [$M_4(\mathbb{C})$ Model : The Product, the Trace and the Determinant](../articles_maths/m4c-model-the-product-the-trace-and-the-determinant), for the current display and the change $S$
- [$M_4(\mathbb{C})$ Representation : The Two-Sided Operators on the Biquaternion Algebra](../articles_maths/m4c-representation-the-two-sided-operators-on-the-biquaternion-algebra), for the sixteen cells and the gamma frame
- [$M_4(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes](../articles_maths/m4c-model-the-peirce-coordinates-matrix-units-and-the-spinor-planes), for the Peirce table and the two planes
- [$M_4(\mathbb{C})$ Representation : The Conjugations and the Adjoints](../articles_maths/m4c-representation-the-conjugations-and-the-adjoints), for the transpose and dagger dictionaries in the coefficient basis
- [The Sandwich in the $M_4(\mathbb{C})_L$ Model](../articles_maths/the-sandwich-in-the-m4c-l-model), for the congruence and its frame statement
