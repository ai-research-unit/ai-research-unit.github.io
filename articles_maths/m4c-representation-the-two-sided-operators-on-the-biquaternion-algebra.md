# __$M_4(\mathbb{C})$ Representation : The Two-Sided Operators on the Biquaternion Algebra__

## Introduction

The $4\times4$ model reads each biquaternion $\tilde Q$ as one $4\times4$ matrix, its left regular matrix $\mathsf{M}_4^{L}(\tilde Q)$, whose image is the four-dimensional copy $M_4(\mathbb{C})_{\mathbb{B},L}$. This article is one of a series; it records the construction and one choice of gamma set, and it takes the frame of the corpus from *Matrix Representations Conventions*, §*The Matrix Models*. That is a representation of the algebra $\mathbb{B}$ on itself by left multiplication: the image has complex dimension four, and the product is preserved.

The operator $\tilde Q_3\mapsto\tilde Q_1\,\tilde Q_3\,\tilde Q_2$ is not a left multiplication when $\tilde Q_2$ is not a scalar. It needs the right multiplication as well. The pair $(\tilde Q_1,\tilde Q_2)$ defines the **two-sided operator**

$$
T_{\tilde Q_1,\tilde Q_2}(\tilde Q_3)=\tilde Q_1\,\tilde Q_3\,\tilde Q_2 .
$$

The operators $T_{\tilde Q_1,\tilde Q_2}$ span the whole matrix algebra $M_4(\mathbb{C})$, of complex dimension sixteen. This article builds that representation and its sixteen basis matrices. The construction is the case $n=2$ of $M_n(\mathbb{C})\otimes M_n(\mathbb{C})^{\mathrm{opp}}\cong M_{n^2}(\mathbb{C})$; it is recorded as one construction route in *The Matrix Algebra $M_4(\mathbb{C})$*, §*A Construction from the Two-Sided Operators*.

**Three objects, three dimensions.** The carrier is the biquaternion algebra $\mathbb{B}$, of complex dimension four. Its left regular image $L(\mathbb{B})=M_4(\mathbb{C})_{\mathbb{B},L}=\{\mathsf{M}_4^{L}(\tilde Q)\}$ is a four-dimensional subalgebra of $M_4(\mathbb{C})$. The operator algebra is the tensor product

$$
\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\;\cong\;\operatorname{End}_{\mathbb{C}}(\mathbb{B}),
$$

of complex dimension sixteen; its **matrix representation** in the canonical frame is $M_4(\mathbb{C})$. The sixteen basis matrices are the images of the sixteen elementary tensors $e_\mu\otimes e_\nu^{\mathrm{opp}}$.

**The tensor-product question.** Three products must be kept apart. The Kronecker product $L_\mu\otimes L_\nu$ of two $4\times4$ matrices is a $16\times16$ matrix acting on $\mathbb{C}^4\otimes\mathbb{C}^4$; it is *not* the matrix of $\tilde Q_3\mapsto e_\mu\tilde Q_3 e_\nu$. The Kronecker product of two $2\times2$ matrices *is* a $4\times4$ matrix, and in the canonical frame it gives the two-sided operators through the identification $\mathbb{B}\cong M_2(\mathbb{C})$; that display is the Pauli form recorded in the remark of §*The Four Right Matrices* and evaluated in the displays marked *Pauli form* below. The construction used here is the ordinary product $T_{\mu\nu}=L_\mu R_\nu$ of two $4\times4$ matrices, with $R_\nu$ read from $L_\nu$ by transposition and one exchange. The product that builds the sixteen is the tensor product of algebras, $e_\mu\otimes e_\nu^{\mathrm{opp}}\mapsto L_\mu R_\nu$, and in matrices it is the ordinary product of two $4\times4$ matrices.

**Conventions.** The algebra, the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ and the matrix $\mathsf{M}_4^{L}$ are those of *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant*. Write $L_{\tilde Q}=\mathsf{M}_4^{L}(\tilde Q)$ for left multiplication by $\tilde Q$, and $R_{\tilde Q}$ for right multiplication, $R_{\tilde Q}(\tilde Q_3)=\tilde Q_3\tilde Q$; write $L_\mu=L_{e_\mu}$ and $R_\mu=R_{e_\mu}$ for the four basis matrices. A matrix written without a superscript is in the canonical frame; in the coefficient basis the same operators are $L_{\tilde Q}^{\mathrm{coef}}=C_{\Pi}L_{\tilde Q}C_{\Pi}^{-1}$ and $R_{\tilde Q}^{\mathrm{coef}}=C_{\Pi}R_{\tilde Q}C_{\Pi}^{-1}$, with $C_{\Pi}$ the Peirce change of *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant*. Matrices are written in the canonical frame of *Matrix Representations Conventions*, §*The Matrix Models*, the Peirce frame, where

$$
L_{\tilde Q}=\mathrm I_2\otimes\mathsf M_2(\tilde Q),
$$
with $\mathsf M_2$ the $2\times2$ model; the four basis matrices are displayed in the next section.

The notation $e_\mu$ is the unit of the basis in the direction $\mu$, so $e_k=\vec e_k$ for $k=x,y,z$. The coefficient coordinates $(t,x,y,z)$, that is, the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, are used only where they are named; there the matrix of quaternion conjugation is $D=\operatorname{diag}(1,-1,-1,-1)$, and $\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ is the quaternionic norm.

**Boundaries.** The abstract algebra, its two regular representations and its double centraliser are *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*. The family $\{T_{\tilde Q_1,\tilde Q_2}\}$, its composition, its adjoint and its type criteria are *Two-Sided Operators on the Biquaternion Algebra*. The model and its four-dimensional image are *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant*. The one-sided families are *One-Sided Operators on the Biquaternion Algebra*. The congruence is *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Sandwich*, and the $2\times2$ model is *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*.

## The Four Left Matrices

**Definition.** The left regular matrix $L_{\tilde Q}=\mathsf{M}_4^{L}(\tilde Q)$ is the $4\times4$ matrix of $\tilde Q_3\mapsto\tilde Q\,\tilde Q_3$ in the canonical frame. Its $j$-th column is the coordinate column of $\tilde Q\,P_j$, with $(P_1,P_2,P_3,P_4)=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$; in the coefficient basis, where $P_j=e_j$, this is the coordinate column of $\tilde Q\,e_j$.

The four basis matrices are

$$
L_t=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
L_x=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix},
$$

$$
L_y=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
L_z=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix}.
$$

**Pauli form.** With $\sigma_1,\sigma_2,\sigma_3$ the Pauli matrices, the same four matrices are
$$
L_t=\mathrm I_2\otimes\mathrm I_2,\qquad
L_k=-i\,\mathrm I_2\otimes\sigma_k .
$$
The Kronecker factors are $2\times2$; the product is $4\times4$.

A general element is

$$
L_{\tilde Q}=\mathrm I_2\otimes\mathsf M_2(\tilde Q)=
\begin{pmatrix}
Q_t-iQ_z&-iQ_x-Q_y&0&0\\
-iQ_x+Q_y&Q_t+iQ_z&0&0\\
0&0&Q_t-iQ_z&-iQ_x-Q_y\\
0&0&-iQ_x+Q_y&Q_t+iQ_z
\end{pmatrix}.
$$

**The image is four-dimensional.** The matrices $L_\mu$ are linearly independent, and every product $L_{\tilde Q_1}L_{\tilde Q_2}=L_{\tilde Q_1\tilde Q_2}$ stays in their span. So $L(\mathbb{B})$ is a copy of $\mathbb{B}$, not the whole of $M_4(\mathbb{C})$.

## The Four Right Matrices

**Definition.** The right multiplication is $R_{\tilde Q}(\tilde Q_3)=\tilde Q_3\tilde Q$. Its matrix is not $\mathsf{M}_4^{L}(\tilde Q)$: the two families commute, and $R_{\tilde Q}$ is the commuting partner of $L_{\tilde Q}$.

**Proposition (the right matrix is a transpose of the left one).** Let $\mathsf S$ be the linear involution of the carrier that fixes the two idempotents and exchanges the two mixed Peirce units,

$$
\mathsf S\tilde\Pi_\pm=\tilde\Pi_\pm,\qquad
\mathsf S\vec\Upsilon_+=\vec\Upsilon_-,\qquad
\mathsf S\vec\Upsilon_-=\vec\Upsilon_+ .
$$

**The matrix.** In the canonical frame
$$
\mathsf S=\begin{pmatrix}1&0&0&0\\0&0&1&0\\0&1&0&0\\0&0&0&1\end{pmatrix},
$$
the permutation of the second and third coordinates. It is symmetric and involutive, $\mathsf S^{\mathsf T}=\mathsf S=\mathsf S^{-1}$, of trace $2$ and determinant $-1$; in the coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ the same operator is the reflection $\operatorname{diag}(1,1,-1,1)$, which fixes $e_t,\vec e_x,\vec e_z$ and negates $\vec e_y$. It is a linear involution of the carrier, not an algebra map, not one of the sixteen cells and not a one-sided multiplication.

With this exchange,

$$
\boxed{\;R_{\tilde Q}=\mathsf S\,L_{\tilde Q}^{\mathsf T}\,\mathsf S^{-1}\;}
$$

for every $\tilde Q$.

*Proof.* Left multiplication is $L_{\tilde Q}=\mathrm I_2\otimes\mathsf M_2(\tilde Q)$, so it acts on the second tensor factor; transposition gives $L_{\tilde Q}^{\mathsf T}=\mathrm I_2\otimes\mathsf M_2(\tilde Q)^{\mathsf T}$. The permutation $\mathsf S$ exchanges the two tensor factors, the copy index and the spinor index, so $\mathsf S L_{\tilde Q}^{\mathsf T}\mathsf S^{-1}=\mathsf M_2(\tilde Q)^{\mathsf T}\otimes\mathrm I_2$. Right multiplication acts on the first factor: if $X=\mathsf M_2(\tilde Q_3)$ is the $2\times2$ matrix of $\tilde Q_3$, then $\mathsf M_2(\tilde Q_3\tilde Q)=X\mathsf M_2(\tilde Q)$, and on the vectorised matrix $\operatorname{vec}X$ the map is $\operatorname{vec}X\mapsto(\mathsf M_2(\tilde Q)^{\mathsf T}\otimes\mathrm I_2)\operatorname{vec}X$. Hence the boxed identity.

For the basis, $\mathsf S L_t^{\mathsf T}\mathsf S^{-1}=L_t$, and $R_k=\mathsf S L_k^{\mathsf T}\mathsf S^{-1}$; since $L_x$ and $L_z$ are symmetric and $L_y$ is antisymmetric,

$$
R_x=\mathsf S L_x\mathsf S^{-1},\qquad
R_y=-\mathsf S L_y\mathsf S^{-1},\qquad
R_z=\mathsf S L_z\mathsf S^{-1}.
$$

Explicitly,

$$
R_t=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
R_x=\begin{pmatrix}0&0&-i&0\\0&0&0&-i\\-i&0&0&0\\0&-i&0&0\end{pmatrix},
$$

$$
R_y=\begin{pmatrix}0&0&1&0\\0&0&0&1\\-1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
R_z=\begin{pmatrix}-i&0&0&0\\0&-i&0&0\\0&0&i&0\\0&0&0&i\end{pmatrix}.
$$

In the coefficient basis the same operator reads $R_{\tilde Q}^{\mathrm{coef}}=D L_{\tilde Q^{\natural}}^{\mathrm{coef}}D$ with $D=\operatorname{diag}(1,-1,-1,-1)$, the matrix of quaternion conjugation there. The formula is a statement about that basis, not about the operator: in the canonical frame it becomes $R_{\tilde Q}=\mathsf S L_{\tilde Q}^{\mathsf T}\mathsf S^{-1}$.

**The two families commute.** $L_{\tilde Q_1}R_{\tilde Q_2}=R_{\tilde Q_2}L_{\tilde Q_1}$, because both sides send $\tilde Q_3$ to $\tilde Q_1\tilde Q_3\tilde Q_2$. This is why the sixteen products below need no ordering convention. The right image is $R(\mathbb{B})=M_4(\mathbb{C})_{\mathbb{B},R}$.

**Remark (the Pauli shorthand, legacy).** The earlier articles display the same matrices in the Pauli shorthand. With $\sigma_1,\sigma_2,\sigma_3$ the Pauli matrices,

$$
L_k=-i\,\mathrm I_2\otimes\sigma_k,\qquad
R_x=-i\,\sigma_1\otimes\mathrm I_2,\quad
R_y=+i\,\sigma_2\otimes\mathrm I_2,\quad
R_z=-i\,\sigma_3\otimes\mathrm I_2,
$$

and for general parameters $R_{\tilde Q}=\mathsf M_2(\tilde Q)^{\mathsf T}\otimes\mathrm I_2$. These are evaluations of the L-based identities above; they are kept as a dictionary, not used in the construction of $R$ and $T$. The same shorthand is used, once per section, for the complementary displays marked *Pauli form* in §*The Four Left Matrices*, §*The Sixteen Basis Matrices* and §*The Gamma Set, and the Choice Behind It*; in each case the definition stands above in $L$, $R$ and $T$, and the Pauli line is its evaluation.

## The Sixteen Basis Matrices

**Definition.** For $\mu,\nu\in\{t,x,y,z\}$ set

$$
T_{\mu\nu}=L_\mu\,R_\nu .
$$

The matrix $T_{\mu\nu}$ is the matrix of the operator $\tilde Q_3\mapsto e_\mu\,\tilde Q_3\,e_\nu$. A general two-sided operator is the linear combination

$$
T_{\tilde Q_1,\tilde Q_2}=\sum_{\mu,\nu}Q_{1\mu}Q_{2\nu}\,T_{\mu\nu},
$$

and conversely every element of the family $\{T_{\tilde Q_1,\tilde Q_2}\}$ is obtained this way.

**Proposition (they are a basis).** The sixteen matrices $T_{\mu\nu}$ are distinct, invertible, of determinant $1$ and rank $4$, and are linearly independent. They are a basis of $M_4(\mathbb{C})$.

*Proof.* By the theorem of *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*, the map $\tilde Q_1\otimes\tilde Q_2^{\mathrm{opp}}\mapsto L_{\tilde Q_1}R_{\tilde Q_2}$ is an isomorphism $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B})$. The sixteen elementary tensors $e_\mu\otimes e_\nu^{\mathrm{opp}}$ are a basis of the left side, so their images $T_{\mu\nu}$ are a basis of the right side. Each is $T_{\mu\nu}=L_\mu R_\nu$, with $L_\mu$ invertible and $R_\nu=\mathsf S L_\nu^{\mathsf T}\mathsf S^{-1}$ invertible, so it is invertible, of determinant $\det L_\mu\det R_\nu=1$ and rank $4$. Distinct pairs give distinct products, because the map is injective on the sixteen elementary tensors.

**The rule.** Column $j$ of $T_{\mu\nu}$ is the coordinate column of $e_\mu\,P_j\,e_\nu$ in the canonical frame $P_j=\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-$. In the coefficient basis, where the $j$-th basis vector is $e_j$, that column is the coordinate column of $e_\mu e_j e_\nu$.

**The table.** The right matrices are read from the left ones,

| $\nu$ | $t$ | $x$ | $y$ | $z$ |
|---|---|---|---|---|
| $R_\nu$ | $L_t$ | $\mathsf S L_x\mathsf S^{-1}$ | $-\mathsf S L_y\mathsf S^{-1}$ | $\mathsf S L_z\mathsf S^{-1}$ |

and the sixteen are the ordinary products

$$
T_{\mu\nu}=L_\mu R_\nu=L_\mu\,\mathsf S\,L_\nu^{\mathsf T}\,\mathsf S^{-1}.
$$

No tensor product of $4\times4$ matrices enters, and no change of basis is needed.

**One entry, checked.** The table gives $T_{xy}=L_xR_y=-L_x\mathsf S L_y\mathsf S^{-1}$,
$$
T_{xy}=\begin{pmatrix}0&0&0&-i\\0&0&-i&0\\0&i&0&0\\i&0&0&0\end{pmatrix}.
$$
Its first column is the coordinate column of $e_x\tilde\Pi_+e_y=i\tilde\Pi_-$, because $\tilde\Pi_+e_y=-\vec\Upsilon_-$ and $e_x\vec\Upsilon_-=-i\tilde\Pi_-$.

**The sixteen, in four families.** The four families are
$$
T_{tt}=L_t,\qquad
T_{tk}=R_k,\qquad
T_{kt}=L_k,\qquad
T_{jk}=L_jR_k .
$$
In the Pauli form these are
$$
T_{tt}=\mathrm I_4,\qquad
T_{tk}=-i\,\sigma_k^{\mathsf T}\otimes\mathrm I_2,\qquad
T_{kt}=-i\,\mathrm I_2\otimes\sigma_k,\qquad
T_{jk}=-\sigma_k^{\mathsf T}\otimes\sigma_j .
$$

**The sixteen, entry by entry.** In the canonical frame, grouped by the left index $\mu$,
$$
T_{tt}=L_tR_t=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
T_{tx}=L_tR_x=\begin{pmatrix}0&0&-i&0\\0&0&0&-i\\-i&0&0&0\\0&-i&0&0\end{pmatrix},
$$
$$
T_{ty}=L_tR_y=\begin{pmatrix}0&0&1&0\\0&0&0&1\\-1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
T_{tz}=L_tR_z=\begin{pmatrix}-i&0&0&0\\0&-i&0&0\\0&0&i&0\\0&0&0&i\end{pmatrix},
$$
$$
T_{xt}=L_xR_t=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix},\qquad
T_{xx}=L_xR_x=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix},
$$
$$
T_{xy}=L_xR_y=\begin{pmatrix}0&0&0&-i\\0&0&-i&0\\0&i&0&0\\i&0&0&0\end{pmatrix},\qquad
T_{xz}=L_xR_z=\begin{pmatrix}0&-1&0&0\\-1&0&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix},
$$
$$
T_{yt}=L_yR_t=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
T_{yx}=L_yR_x=\begin{pmatrix}0&0&0&i\\0&0&-i&0\\0&i&0&0\\-i&0&0&0\end{pmatrix},
$$
$$
T_{yy}=L_yR_y=\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&1&0&0\\-1&0&0&0\end{pmatrix},\qquad
T_{yz}=L_yR_z=\begin{pmatrix}0&i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&i&0\end{pmatrix},
$$
$$
T_{zt}=L_zR_t=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix},\qquad
T_{zx}=L_zR_x=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\-1&0&0&0\\0&1&0&0\end{pmatrix},
$$
$$
T_{zy}=L_zR_y=\begin{pmatrix}0&0&-i&0\\0&0&0&i\\i&0&0&0\\0&-i&0&0\end{pmatrix},\qquad
T_{zz}=L_zR_z=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&-1\end{pmatrix}.
$$

Each has four nonzero entries, one in each row and each column, and the nonzero entries are $\pm1$ or $\pm i$. The coefficient basis is the conjugate display: there the same sixteen are the signed permutation matrices $T_{\mu\nu}^{\mathrm{coef}}=C_{\Pi}\,T_{\mu\nu}\,C_{\Pi}^{-1}$.

**Composition.** The product of two basis operators is a signed basis operator:
$$
T_{\mu\nu}\,T_{\rho\sigma}=T_{e_\mu e_\rho,\;e_\sigma e_\nu}=\epsilon\,\epsilon'\,T_{\mu'\nu'},
$$
where $e_\mu e_\rho=\epsilon\,e_{\mu'}$ and $e_\sigma e_\nu=\epsilon'\,e_{\nu'}$. For general parameters,
$$
T_{\tilde Q_1,\tilde Q_2}\,T_{\tilde Q_3,\tilde Q_4}=T_{\tilde Q_1\tilde Q_3,\,\tilde Q_4\tilde Q_2}.
$$
The sixteen are therefore closed under multiplication up to sign, with the unit $T_{tt}=\mathrm{I}_4$. They are not a group: $-T_{\mu\nu}$ is not one of the sixteen.

**Inverse, trace and determinant.** For $\tilde Q_1,\tilde Q_2$ with $\langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_2\rangle_{\natural}\neq0$,
$$
T_{\tilde Q_1,\tilde Q_2}^{-1}=T_{\tilde Q_1^{-1},\tilde Q_2^{-1}},\qquad
\operatorname{Tr}T_{\tilde Q_1,\tilde Q_2}=4\,Q_{1t}Q_{2t},\qquad
\det T_{\tilde Q_1,\tilde Q_2}=\langle\tilde Q_1\rangle_{\natural}^2\langle\tilde Q_2\rangle_{\natural}^2 .
$$
At $\tilde Q_2=e_t$ this is the model display: $T_{\tilde Q,e_t}=L_{\tilde Q}$, of trace $4Q_t$ and determinant $\langle\tilde Q\rangle_{\natural}^2$.
In particular every basis matrix is invertible, with inverse $\pm$ one of the sixteen; the trace is $4$ only for $T_{tt}$ and $0$ for the other fifteen, and the determinant is $1$ for all sixteen.

**Orthogonality.** For the Hilbert–Schmidt inner product $\langle A,B\rangle=\operatorname{Tr}(A^{\dagger}B)$,
$$
\operatorname{Tr}\bigl(T_{\mu\nu}^{\dagger}T_{\rho\sigma}\bigr)=4\,\delta_{\mu\rho}\,\delta_{\nu\sigma}.
$$
The sixteen are an orthogonal basis, each of norm $2$. The normalization is the same $4$ as the trace of a left multiplication, because the carrier has four dimensions.

**The basis consists of units, its span does not.** Every $T_{\mu\nu}$ is invertible, but a sum need not be. For example
$$
T_{tt}+T_{xx}=\mathrm I_4+L_xR_x=
\begin{pmatrix}1&0&0&-1\\0&1&-1&0\\0&-1&1&0\\-1&0&0&1\end{pmatrix},
$$
of rank two. The algebra is simple and has many zero divisors; a basis of invertible matrices does not change that.

## The Tensor Product

**The Kronecker product of the sixteen is not the construction.** The Kronecker product $T_{\mu\nu}\otimes T_{\rho\sigma}$ is a $16\times16$ matrix. It acts on $\mathbb{C}^4\otimes\mathbb{C}^4$, a space of dimension sixteen, not on the carrier $\mathbb{C}^4$. It does not represent $\tilde Q_3\mapsto\tilde Q_1\tilde Q_3\tilde Q_2$.

**The construction is the ordinary matrix product.** The two one-sided matrices are known, and

$$
\boxed{\;T_{\tilde Q_1,\tilde Q_2}=L_{\tilde Q_1}R_{\tilde Q_2}=L_{\tilde Q_1}\,\mathsf S\,L_{\tilde Q_2}^{\mathsf T}\,\mathsf S^{-1}\;}
$$

for all $\tilde Q_1,\tilde Q_2$; in particular $T_{\mu\nu}=L_\mu\mathsf S L_\nu^{\mathsf T}\mathsf S^{-1}$. The product is the ordinary product of two $4\times4$ matrices. The first factor is the left matrix of $\tilde Q_1$; the second is the right matrix of $\tilde Q_2$, the transpose of the left matrix of $\tilde Q_2$ in the exchanged Peirce frame. The Pauli–Kronecker form $T_{\mu\nu}=\mathsf M_2(e_\nu)^{\mathsf T}\otimes\mathsf M_2(e_\mu)$ is the legacy evaluation of this identity, recorded in the remark of §*The Four Right Matrices*.

**The coefficient basis is the conjugate display.** The Peirce change $C_{\Pi}$ of *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant*,
$$
C_{\Pi}=\begin{pmatrix}
\tfrac12&0&0&\tfrac12\\
0&\tfrac{i}{2}&\tfrac{i}{2}&0\\
0&\tfrac12&-\tfrac12&0\\
\tfrac{i}{2}&0&0&-\tfrac{i}{2}
\end{pmatrix},
\qquad
\det C_{\Pi}=-\tfrac14,
$$
has the Peirce elements $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$ as columns. In that basis the same operators read
$$
L_{\tilde Q_1}^{\mathrm{coef}}=C_{\Pi}L_{\tilde Q_1}C_{\Pi}^{-1},\qquad
R_{\tilde Q_2}^{\mathrm{coef}}=C_{\Pi}R_{\tilde Q_2}C_{\Pi}^{-1},
\qquad
T_{\tilde Q_1,\tilde Q_2}^{\mathrm{coef}}=C_{\Pi}T_{\tilde Q_1,\tilde Q_2}C_{\Pi}^{-1},
$$
and the sixteen are the signed permutation matrices $T_{\mu\nu}^{\mathrm{coef}}=C_{\Pi}\,T_{\mu\nu}\,C_{\Pi}^{-1}$. The conjugation changes the entries, not the algebra.

**In the canonical frame the sixteen are not matrix units.** Each $T_{\mu\nu}=L_\mu R_\nu$ is a product of two invertible matrices and is not a $4\times4$ matrix unit. The matrix units are the sixteen products $L_{P_i}R_{P_j}$ of the four Peirce elements $P_i$, not the sixteen $T_{\mu\nu}$. The canonical frame is adapted to both the chiral blocks and the tensor basis, and this is why the gamma construction closes on it.

**Another basis conjugates the sixteen.** A change of basis $U$ of $\mathbb{B}$ replaces each $T_{\mu\nu}$ by $U\,T_{\mu\nu}\,U^{-1}$. The sixteen matrices change, the algebra they span does not. The coefficient basis is the one in which they are signed permutations; the canonical frame is the one in which they are the products of the left matrices and the exchange above.

## The Sandwich Inside the Sixteen

The **bilinear sandwich** is the member of the family whose two parameters are tied:

$$
\Theta_{\tilde Q}=T_{\tilde Q,\tilde Q^{*}} .
$$

It is not a generic two-sided operator. The second slot is $\tilde Q^{*}$, not an independent $\tilde Q_2$; the sandwich has one complex parameter, and it is quadratic in it,
$$
\Theta_{\lambda\tilde Q}=\lvert\lambda\rvert^{2}\Theta_{\tilde Q} .
$$

**The family and the algebra.** The sixteen-dimensional algebra is the span of $\{T_{\tilde Q_1,\tilde Q_2}\}$ by linear combination. The family itself is the set of **decomposable tensors** $\tilde Q_1\otimes\tilde Q_2^{\mathrm{opp}}$: an affine cone of complex dimension seven, the cone over the Segre variety $\mathbb{P}^3\times\mathbb{P}^3\subset\mathbb{P}^{15}$. The sandwich is the graph $\tilde Q_2=\tilde Q_1^{*}$ inside it: a real cone of dimension seven, because the phase of $\tilde Q$ cancels,
$$
(e^{i\theta}\tilde Q)\,\tilde Q_3\,(e^{i\theta}\tilde Q)^{*}=\tilde Q\,\tilde Q_3\,\tilde Q^{*}.
$$

**Two values.** $\tilde Q=e_t$ gives $\Theta_{e_t}=\mathrm{I}_4$. $\tilde Q=\vec e_y$ gives $\tilde Q^{*}=-\vec e_y$ and
$$
\Theta_{\vec e_y}=T_{\vec e_y,-\vec e_y}=-T_{yy}=
\begin{pmatrix}0&0&0&1\\0&0&-1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix}.
$$

**The gamma matrices are not sandwiches.** They are $i$ times five cells of the tensor basis in the reference frame, and the pair of directions in those cells is free; §*The Gamma Set, and the Choice Behind It* treats them.

## The Gamma Set, and the Choice Behind It

**Status.** This section records one frame, not the frame. The Clifford relations hold for every frame of the normal form below; the cell table holds for one frame only.

**The five operators.** In the reference frame the Dirac generators are five cells multiplied by $i$:
$$
\boxed{\;\gamma_0=iT_{e_t,e_x},\qquad
\gamma_1=iT_{e_x,e_y},\qquad
\gamma_2=iT_{e_y,e_y},\qquad
\gamma_3=iT_{e_z,e_y},\qquad
\gamma_5=-iT_{e_t,e_z}\;}
$$
In the canonical frame they are
$$
\gamma_0=iT_{e_t,e_x}=\begin{pmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
\gamma_1=iT_{e_x,e_y}=\begin{pmatrix}0&0&0&1\\0&0&1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix},
$$
$$
\gamma_2=iT_{e_y,e_y}=\begin{pmatrix}0&0&0&-i\\0&0&i&0\\0&i&0&0\\-i&0&0&0\end{pmatrix},\qquad
\gamma_3=iT_{e_z,e_y}=\begin{pmatrix}0&0&1&0\\0&0&0&-1\\-1&0&0&0\\0&1&0&0\end{pmatrix},
$$
$$
\gamma_5=-iT_{e_t,e_z}=\begin{pmatrix}-1&0&0&0\\0&-1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}.
$$
Each has trace $0$, determinant $1$ and rank $4$. In the Pauli form the same five are
$$
\gamma_0=\sigma_1\otimes\mathrm I_2,\qquad
\gamma_k=i\,\sigma_2\otimes\sigma_k,\qquad
\gamma_5=-\sigma_3\otimes\mathrm I_2 .
$$

**The grading construction.** The frame is generated by the left action and one grading of the multiplicity factor. Take
$$
G=-iT_{ty},\qquad \Gamma_t=iT_{e_t,e_x},
$$
where $\Gamma_t$ is the exchange of the two copies; it is $iT_{e_t,e_x}=iR_x$, a right multiplication of the reference frame, and set
$$
\Gamma_k=L_{i\vec e_k}G .
$$
The grading $G$ acts on the copy index and $L_{i\vec e_k}$ on the spinor index, so the product acts on the two indices separately: no rotation is needed, and no change of spinor basis. The four $\Gamma_\mu$ all square to $+\mathrm I_4$ and anticommute in pairs. The Lorentzian generators are the same frame with the spatial generators multiplied by $i$,
$$
\gamma_0=\Gamma_t,\qquad \gamma_k=i\Gamma_k,
$$
so that $(\gamma_0)^2=\mathrm I_4$ and $(\gamma_k)^2=-\mathrm I_4$. The pseudoscalar is $\gamma_5=-iT_{e_t,e_z}$.

**What the rotation was.** The same left action with the grading read along the third spatial direction instead gives
$$
\Gamma_k=L_{i\vec e_k}G_z,\qquad G_z=+iT_{tz},
$$
the Peirce grading. The two frames use the same left action and the same left matrices $L_k$; they differ only by the choice of direction in the multiplicity plane. That choice is a basis change of the copy label, not an algebraic obstruction.

**The invariant.** No change of basis removes the $-i$. The unit $\vec e_k$ acts as an operator of square $-\mathrm I_4$, so its eigenvalues are $\pm i$; a gamma-like matrix with $\Gamma_k^2=+\mathrm I_4$ cannot represent $\vec e_k$. The unit $i\vec e_k$ has square $+\mathrm I_4$, and its left matrix $L_{i\vec e_k}$ is the gamma-like square root in the spinor factor: the frame uses $\Gamma_k=L_{i\vec e_k}G$, and $\gamma_k=i\Gamma_k$ is the Lorentzian generator. The coefficient basis, where the four left matrices are real signed permutations, is the same representation with the $i$ hidden in the change of basis $C_{\Pi}$.

**The gamma-built set is another representation.** The four matrices
$$
\mathrm I_4,\qquad \Gamma_t\Gamma_1,\qquad \Gamma_t\Gamma_2,\qquad -\Gamma_1\Gamma_2
$$
square to $-\mathrm I_4$ in the three vector slots, anticommute, and multiply as the quaternion units. They are a valid representation of $\mathbb{B}$, and they are not the left action: the two diagonal blocks of $\Gamma_t\Gamma_1$ differ by a sign, whereas those of $L_{i\vec e_x}$ are equal. Choosing this block as the gamma set is a choice of representation, not the only one; it is the choice that makes the generators of the frame the left matrices times one grading.

**The frame is a choice of two directions.** The following normal form gives a frame for every orthogonal pair. Let $\beta,\delta$ be unit spatial directions, orthogonal:
$$
\beta^2=\delta^2=-e_t,\qquad \beta\delta=-\delta\beta,
$$
and set
$$
\gamma_0=iL_{e_t}R_{\delta},\qquad
\gamma_k=iL_{e_k}R_{\beta},\qquad k=x,y,z .
$$
Then
$$
\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}\mathrm{I}_4,\qquad
(\gamma_5)^2=\mathrm{I}_4,\qquad
\gamma_5\gamma_\mu=-\gamma_\mu\gamma_5,\qquad
\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3=iT_{e_t,\beta\delta}.
$$
*Proof.* $(\gamma_0)^2=-R_{\delta^2}=\mathrm{I}_4$; $(\gamma_k)^2=-L_{e_k^2}R_{\beta^2}=-\mathrm{I}_4$; $\gamma_0\gamma_k+\gamma_k\gamma_0=-L_{e_k}(R_{\delta\beta}+R_{\beta\delta})=0$; $\gamma_j\gamma_k+\gamma_k\gamma_j=-L_{e_je_k+e_ke_j}R_{\beta^2}=0$. For the pseudoscalar the left factor is $L_{e_te_xe_ye_z}=L_{-e_t}$ and the right factor is $R_{\beta^3\delta}=R_{-\beta\delta}$; the two signs cancel, so the product is $T_{e_t,\beta\delta}$.

The reference frame is $(\beta,\delta)=(e_y,e_x)$, so $\beta\delta=-e_z$. It is the frame the physics articles use, and in the canonical frame it is the one displayed above. The earlier articles wrote the same five matrices after the Peirce change; the change is now the identity.

**The pair is the choice.** The five operators determine the pair: $\delta$ is the right factor of $\gamma_0$, and $\beta$ is the right factor of $\gamma_1$. Distinct pairs therefore give distinct frames, not two descriptions of one frame. For the corpus pair $(e_y,e_x)$ the five are cells. If $\beta$ is not one of $e_x,e_y,e_z$, the three spatial generators are not cells: $\gamma_k=iT_{e_k,\beta}=i\sum_\nu\beta_\nu T_{k\nu}$ is a single product of coefficient rank one, supported on several cells. If $\delta$ is not a coordinate axis, $\gamma_0$ is not a cell either. The cell property is a property of the pair, not of the construction.

**Nothing selects the pair.** The proof above uses only $\beta^2=\delta^2=-e_t$ and $\beta\delta=-\delta\beta$: every such pair gives a frame, and every identity in the frame follows from those two lines. No Clifford relation mentions $\beta$ or $\delta$. The three spatial directions enter in three roles — $\beta$ as the common right factor of $\gamma_1,\gamma_2,\gamma_3$, $\delta$ as the right factor of $\gamma_0$, and $\beta\delta$ as the right factor of $\gamma_5$ — and the algebra assigns no direction to any role. What changes with the pair is the list of operators: the five matrices, whether they are cells, the sign of $\gamma_5$ through $\beta\delta$, and the grade column. The pair is a free parameter of the construction, not a consequence of it.

**A remark on conjugacy.** For a unit $\tilde u$ and $U=L_{\tilde u}R_{\tilde u^{-1}}$ one has $U\,T_{\tilde Q_1,\tilde Q_2}\,U^{-1}=T_{\tilde u\tilde Q_1\tilde u^{-1},\,\tilde u\tilde Q_2\tilde u^{-1}}$. This is the matrix of the inner automorphism $\tilde Q_3\mapsto\tilde u\tilde Q_3\tilde u^{-1}$, and it carries frames to frames. It does not preserve the normal form, because it rotates the left factors $e_k$ as well as the right factors: the image of $\gamma_k=iT_{e_k,\beta}$ is $iT_{\tilde u e_k\tilde u^{-1},\tilde u\beta\tilde u^{-1}}$, whose left factor is no longer a coordinate axis. The normal form is therefore a slice through the set of frames, not a conjugacy class. Which frames of $M_4(\mathbb{C})$ are of this form is not settled here; the classification is listed among the open questions.

**What the frame fixes and what it does not.** Every frame of the normal form has: the relations $\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}$; the identity $\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3=iT_{e_t,\beta\delta}$ and the anticommutation of $\gamma_5$ with the four generators; the property that the products span $M_4(\mathbb{C})$; the isomorphism with $\mathrm{Cl}_{1,3}(\mathbb{C})$; the abstract Lorentz algebra generated by the commutators; and the type of each generator, $\gamma_0,\gamma_5\in R(\mathbb{B})$ and $\gamma_1,\gamma_2,\gamma_3\in M_4(\mathbb{C})\setminus\bigl(L(\mathbb{B})\cup R(\mathbb{B})\bigr)$. What the frame does not fix: the individual matrices, the cell labels, the grade column of the table, the Peirce images (for the corpus frame, the chiral Dirac matrices up to a change of spinor basis), the sign of $\gamma_5$, and every table that identifies a gamma with a named operator.

**In this frame the sixteen products are the sixteen cells.** The products of the frame, in increasing grade, are

| Grade | $\gamma$-product | Cell | $c$ | Conversion |
|---|---|---|---|---|
| $0$ | $1$ | $T_{tt}$ | $1$ | $T_{tt}=\mathrm I_4$ |
| $1$ | $\gamma_0$ | $T_{tx}$ | $i$ | $T_{tx}=-i\,\gamma_0$ |
| $1$ | $\gamma_1$ | $T_{xy}$ | $i$ | $T_{xy}=-i\,\gamma_1$ |
| $1$ | $\gamma_2$ | $T_{yy}$ | $i$ | $T_{yy}=-i\,\gamma_2$ |
| $1$ | $\gamma_3$ | $T_{zy}$ | $i$ | $T_{zy}=-i\,\gamma_3$ |
| $2$ | $\gamma_0\gamma_1$ | $T_{xz}$ | $1$ | $T_{xz}=\gamma_0\gamma_1$ |
| $2$ | $\gamma_0\gamma_2$ | $T_{yz}$ | $1$ | $T_{yz}=\gamma_0\gamma_2$ |
| $2$ | $\gamma_0\gamma_3$ | $T_{zz}$ | $1$ | $T_{zz}=\gamma_0\gamma_3$ |
| $2$ | $\gamma_1\gamma_2$ | $T_{zt}$ | $1$ | $T_{zt}=\gamma_1\gamma_2$ |
| $2$ | $\gamma_1\gamma_3$ | $T_{yt}$ | $-1$ | $T_{yt}=-\gamma_1\gamma_3$ |
| $2$ | $\gamma_2\gamma_3$ | $T_{xt}$ | $1$ | $T_{xt}=\gamma_2\gamma_3$ |
| $3$ | $\gamma_0\gamma_1\gamma_2$ | $T_{zx}$ | $i$ | $T_{zx}=-i\,\gamma_0\gamma_1\gamma_2$ |
| $3$ | $\gamma_0\gamma_1\gamma_3$ | $T_{yx}$ | $-i$ | $T_{yx}=i\,\gamma_0\gamma_1\gamma_3$ |
| $3$ | $\gamma_0\gamma_2\gamma_3$ | $T_{xx}$ | $i$ | $T_{xx}=-i\,\gamma_0\gamma_2\gamma_3$ |
| $3$ | $\gamma_1\gamma_2\gamma_3$ | $T_{ty}$ | $-i$ | $T_{ty}=i\,\gamma_1\gamma_2\gamma_3$ |
| $4$ | $\gamma_0\gamma_1\gamma_2\gamma_3$ | $T_{tz}$ | $-1$ | $T_{tz}=i\,\gamma_5=-\gamma_0\gamma_1\gamma_2\gamma_3$ |

The fourth column is $c$, the coefficient that makes the product equal $c\,T_{\mu\nu}$; the fifth writes $T_{\mu\nu}$ in terms of the product. Since $c\in\{1,-1,i,-i\}$, the inverse coefficient is $\bar c$.

*Proof.* Direct multiplication with $T_{\mu\nu}T_{\rho\sigma}=T_{e_\mu e_\rho,\,e_\sigma e_\nu}$; the sixteen entries are distinct, so the products are the sixteen cells in some order, each with a unit coefficient. The pseudoscalar is the last row multiplied by $i$, which is the identity $\gamma_5=iT_{e_t,\beta\delta}$ with $\beta\delta=-e_z$.

**In the canonical frame: the Dirac representation.** In the Pauli shorthand of the remark, for this frame,
$$
\gamma_0=\begin{pmatrix}0&\mathrm{I}_2\\\mathrm{I}_2&0\end{pmatrix},\qquad
\gamma_k=\begin{pmatrix}0&\sigma_k\\-\sigma_k&0\end{pmatrix},\qquad
\gamma_5=\operatorname{diag}(-1,-1,1,1).
$$
These are entry for entry the matrices of *Matrix Representations Conventions*, §*The Clifford Structure and the Gamma Matrices*, and no change of spinor basis is needed. In the coefficient basis the same matrices are $C_{\Pi}\,\gamma_\mu\,C_{\Pi}^{-1}$. The two blocks are the two Weyl spinors; $\gamma_5$ is their sign; the four generators exchange them.

**The projectors are products, not cells.** The chirality projectors are
$$
P_\pm=\tfrac12(\mathrm{I}_4\pm\gamma_5)=\tfrac12\bigl(T_{tt}\pm iT_{e_t,\beta\delta}\bigr)=T_{e_t/2,\;e_t\pm i\beta\delta}.
$$
In the canonical frame $P_+=\operatorname{diag}(0,0,1,1)$ and $P_-=\operatorname{diag}(1,1,0,0)$. Both have rank two, and the second parameter has quaternionic norm zero. They are single two-sided operators, but not cells: a single product can be singular, and a single product need not be a cell.

**Why the left regular model cannot hold them.** A product $L_{\tilde Q_1}R_{\tilde Q_2}$ lies in the left image $L(\mathbb{B})$ only when $\tilde Q_2$ is a scalar, since $L(\mathbb{B})\cap R(\mathbb{B})=\mathbb{C}\mathrm{I}_4$. The right factors here are $\delta$, $\beta$ and $\beta\delta$, all spatial, so no gamma and no $\gamma_5$ lies in $L(\mathbb{B})$. The left image is block diagonal in the canonical frame, $L_{\tilde Q}=\operatorname{diag}(\mathsf{M}_2(\tilde Q),\mathsf{M}_2(\tilde Q))$, so it preserves the two chiral blocks; the four generators exchange them. The Dirac algebra is not contained in $M_4(\mathbb{C})_{\mathbb{B},L}$; it needs the two-sided operators.

**The Lorentz generators.** For this frame the six commutators
$$
\Sigma^{\mu\nu}=\tfrac{i}{2}[\gamma_\mu,\gamma_\nu]
$$
are again cells:
$$
\Sigma^{01}=iT_{xz},\quad
\Sigma^{02}=iT_{yz},\quad
\Sigma^{03}=iT_{zz},\quad
\Sigma^{12}=iT_{zt},\quad
\Sigma^{13}=-iT_{yt},\quad
\Sigma^{23}=iT_{xt}.
$$
They are even, of grade two; the three $\Sigma^{0k}$ are anti-Hermitian and the three $\Sigma^{jk}$ Hermitian; they are linearly independent and close under commutation on the same six. They generate the spinor representation of $\mathfrak{so}(1,3)$ on $\mathbb{B}\cong\mathbb{C}^4$. The sandwich $\Theta_{\tilde Q}$ is the vector representation on the four-dimensional real subspace of anti-Hermitian elements; the two are different representations of the same group, and the tensor basis carries both. The cell labels are those of this frame.

**The Dirac operator.** With $\partial_\mu=\partial/\partial Q_\mu$,
$$
i\gamma_\mu\partial_\mu=-\bigl(T_{e_t,e_x}\partial_0+T_{e_x,e_y}\partial_1+T_{e_y,e_y}\partial_2+T_{e_z,e_y}\partial_3\bigr),
$$
so on $\tilde Q\in\mathbb{B}$,
$$
\tilde Q\mapsto-\bigl(\partial_0\tilde Q\,e_x+e_x\,\partial_1\tilde Q\,e_y+e_y\,\partial_2\tilde Q\,e_y+e_z\,\partial_3\tilde Q\,e_y\bigr).
$$
The mass term is $-mT_{tt}$. This is the matrix Dirac operator of the dictionary, written in this frame and in the canonical frame. It is not the biquaternionic gradient $\tilde\nabla$ of the physics articles: the gradient is the left multiplication $L_{\tilde\nabla}$, while the matrix operator is two-sided. The dictionary relates the two; it does not identify them as operators on the same carrier.

## Products of a Left Matrix and a Right Matrix

**The question.** For which $M\in M_4(\mathbb{C})$ do there exist $\tilde Q_1,\tilde Q_2\in\mathbb{B}$ with $M=L_{\tilde Q_1}R_{\tilde Q_2}$?

**The map.** Define
$$
\Phi:\mathbb{B}\times\mathbb{B}\longrightarrow M_4(\mathbb{C}),\qquad \Phi(\tilde Q_1,\tilde Q_2)=L_{\tilde Q_1}R_{\tilde Q_2}=T_{\tilde Q_1,\tilde Q_2} .
$$
It is $\mathbb{C}$-bilinear: $L$ is linear in $\tilde Q_1$, $R$ is linear in $\tilde Q_2$, and the matrix product is bilinear.

**Lemma 1 (expansion).** For all $\tilde Q_1,\tilde Q_2$,
$$
\Phi(\tilde Q_1,\tilde Q_2)=\sum_{\mu,\nu}Q_{1\mu}\,Q_{2\nu}\,T_{\mu\nu}.
$$
*Proof.* Write $\tilde Q_1=\sum_\mu Q_{1\mu} e_\mu$ and $\tilde Q_2=\sum_\nu Q_{2\nu} e_\nu$. By bilinearity, $\Phi(\tilde Q_1,\tilde Q_2)=\sum_{\mu,\nu}Q_{1\mu}Q_{2\nu}\,\Phi(e_\mu,e_\nu)$, and $\Phi(e_\mu,e_\nu)=T_{\mu\nu}$.

**Definition (coefficient matrix).** By §*The Sixteen Basis Matrices*, every $M\in M_4(\mathbb{C})$ has a unique expansion $M=\sum_{\mu,\nu}c_{\mu\nu}T_{\mu\nu}$. The matrix $c(M)=(c_{\mu\nu})$ is the **coefficient matrix** of $M$. The orthogonality relation gives it directly from $M$:
$$
c(M)_{\mu\nu}=\tfrac14\operatorname{Tr}\bigl(T_{\mu\nu}^{\dagger}M\bigr).
$$
Hence $M\mapsto c(M)$ is a linear isomorphism of $M_4(\mathbb{C})$ onto itself.

**Notation (coordinate column).** For $\tilde Q\in\mathbb{B}$ write $[Q]=(Q_t,Q_x,Q_y,Q_z)^{\mathsf T}$ for the column of its four coefficients in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$.

**Theorem 1 (which matrices are products).** Let $M\in M_4(\mathbb{C})$ and $c=c(M)$. Then
$$
M=L_{\tilde Q_1}R_{\tilde Q_2}\ \text{for some }\tilde Q_1,\tilde Q_2 \iff c=[Q_1]\,[Q_2]^{\mathsf T}.
$$
The product set is therefore $\{M:\operatorname{rank}c(M)\le1\}$.

*Proof.* If $M=\Phi(\tilde Q_1,\tilde Q_2)$, Lemma 1 gives the expansion of $M$ with coefficients $Q_{1\mu}Q_{2\nu}$; uniqueness of the expansion gives $c=[Q_1][Q_2]^{\mathsf T}$. Conversely, if $c=[Q_1][Q_2]^{\mathsf T}$ then $\sum c_{\mu\nu}T_{\mu\nu}=\sum Q_{1\mu}Q_{2\nu}T_{\mu\nu}=\Phi(\tilde Q_1,\tilde Q_2)$ by Lemma 1, and this is $M$.

**Lemma 2 (the factors are unique up to scale).** Let $\tilde Q_1,\tilde Q_2,\tilde P_1,\tilde P_2$ be units. Then $\Phi(\tilde Q_1,\tilde Q_2)=\Phi(\tilde P_1,\tilde P_2)$ if and only if $\tilde P_1=\lambda\tilde Q_1$ and $\tilde P_2=\lambda^{-1}\tilde Q_2$ for some $\lambda\in\mathbb{C}^{\times}$.

*Proof.* If $\tilde P_1=\lambda\tilde Q_1$ and $\tilde P_2=\lambda^{-1}\tilde Q_2$ the products are equal. Conversely, evaluating at $e_t$ gives $\tilde Q_1\tilde Q_2=\tilde P_1\tilde P_2$. For every $\tilde Q_3$, $\tilde Q_1\tilde Q_3\tilde Q_2=\tilde P_1\tilde Q_3\tilde P_2$; multiplying on the left by $\tilde Q_1^{-1}$ and on the right by $\tilde Q_2^{-1}$ gives
$$
\tilde Q_3=(\tilde Q_1^{-1}\tilde P_1)\,\tilde Q_3\,(\tilde P_2\tilde Q_2^{-1}),
$$
that is $L_{\tilde P}R_{\tilde R}=\mathrm{I}_4$ with $\tilde P=\tilde Q_1^{-1}\tilde P_1$ and $\tilde R=\tilde P_2\tilde Q_2^{-1}$. Then $L_{\tilde P}=R_{\tilde R^{-1}}$, so $\tilde P\tilde Q_3=\tilde Q_3\tilde R^{-1}$ for all $\tilde Q_3$; at $\tilde Q_3=e_t$ this gives $\tilde P=\tilde R^{-1}$, hence $\tilde P\tilde Q_3=\tilde Q_3\tilde P$ for all $\tilde Q_3$, and $\tilde P$ is central. The centre of $\mathbb{B}\cong M_2(\mathbb{C})$ is $\mathbb{C}$, so $\tilde P=\lambda e_t$ and $\tilde R=\lambda^{-1}e_t$, that is $\tilde P_1=\lambda\tilde Q_1$ and $\tilde P_2=\lambda^{-1}\tilde Q_2$.

**Definition (length).** The **length** $\ell(M)$ is the least $r\ge0$ such that $M=\Phi(\tilde Q_{1,1},\tilde Q_{2,1})+\cdots+\Phi(\tilde Q_{1,r},\tilde Q_{2,r})$; $\ell(0)=0$.

**Theorem 2 (length is the rank of the coefficient matrix).** For every $M\in M_4(\mathbb{C})$,
$$
\ell(M)=\operatorname{rank}c(M).
$$

*Proof.* If $M=\sum_{i\le r}\Phi(\tilde Q_{1,i},\tilde Q_{2,i})$, then $c(M)=\sum_{i\le r}[Q_{1,i}][Q_{2,i}]^{\mathsf T}$ is a sum of $r$ matrices of rank one, so $\operatorname{rank}c(M)\le r$; hence $\ell(M)\ge\operatorname{rank}c(M)$. Conversely, let $\operatorname{rank}c=r$ and write $c=UV$ with $U$ of size $4\times r$ and $V$ of size $r\times4$ of rank $r$; let $[Q_{1,i}]$ be the $i$-th column of $U$ and let $[Q_{2,i}]^{\mathsf T}$ be the $i$-th row of $V$. Then $c=\sum_{i\le r}[Q_{1,i}][Q_{2,i}]^{\mathsf T}$, so $M=\sum_{i\le r}\Phi(\tilde Q_{1,i},\tilde Q_{2,i})$ by Lemma 1, and $\ell(M)\le r$.

**Corollary 1 (four products suffice, and four are needed generically).** Every $M$ is a sum of at most four products, and $\ell(M)=4$ exactly when $\det c(M)\neq0$. The condition $\det c(M)\neq0$ is open and dense, so a generic matrix needs four products and none needs five.

**Theorem 3 (the product set, as a subset of $M_4(\mathbb{C})$).**
(i) $\Phi(\mathbb{B}\times\mathbb{B})=\{M:\operatorname{rank}c(M)\le1\}$ is a closed algebraic cone, cut out by all $2\times2$ minors of $c(M)$, that is, by the quadratic equations
$$
\operatorname{Tr}\bigl(T_{\mu\nu}^{\dagger}M\bigr)\operatorname{Tr}\bigl(T_{\rho\sigma}^{\dagger}M\bigr)
=\operatorname{Tr}\bigl(T_{\mu\sigma}^{\dagger}M\bigr)\operatorname{Tr}\bigl(T_{\rho\nu}^{\dagger}M\bigr)
$$
for all $\mu,\nu,\rho,\sigma$.
(ii) Its image in $\mathbb{P}^{15}$ is the Segre variety $\mathbb{P}^3\times\mathbb{P}^3$, of dimension $6$; the cone has dimension $7$, in an ambient space of dimension $16$.
(iii) It is closed under multiplication and under inverses on its invertible part, and not under addition; it is a proper subset of $M_4(\mathbb{C})$.

*Proof.* (i) is Theorem 1 and the standard rank-one criterion. (ii) The map $(\tilde Q_1,\tilde Q_2)\mapsto[Q_1][Q_2]^{\mathsf T}$ descends to an injective map $\mathbb{P}^3\times\mathbb{P}^3\to\mathbb{P}^{15}$, the Segre embedding, of dimension $3+3=6$; the affine cone adds one dimension. Equivalently, $\Phi$ is defined on $\mathbb{C}^8$, its fibre over a product of units is the scaling orbit of Lemma 2, of dimension $1$, and $8-1=7$. (iii) $\Phi(\tilde Q_1,\tilde Q_2)\Phi(\tilde Q_3,\tilde Q_4)=\Phi(\tilde Q_1\tilde Q_3,\tilde Q_4\tilde Q_2)$ and $\Phi(\tilde Q_1,\tilde Q_2)^{-1}=\Phi(\tilde Q_1^{-1},\tilde Q_2^{-1})$; $T_{tt}+T_{xx}$ is not a product by (i), since its coefficient matrix is $\operatorname{diag}(1,1,0,0)$; and $7<16$.

**Theorem 4 (matrix rank of a single product).** For $M=\Phi(\tilde Q_1,\tilde Q_2)$,
$$
\operatorname{rank}M=\operatorname{rank}\mathsf{M}_2(\tilde Q_1)\cdot\operatorname{rank}\mathsf{M}_2(\tilde Q_2)\in\{0,1,2,4\}.
$$
In particular $\operatorname{rank}M=4$ exactly when $\tilde Q_1$ and $\tilde Q_2$ are units, and no product has rank $3$.

*Proof.* By the Pauli form of §*The Four Right Matrices*, $T_{\tilde Q_1,\tilde Q_2}=\mathsf{M}_2(\tilde Q_2)^{\mathsf T}\otimes\mathsf{M}_2(\tilde Q_1)$. The singular values of a Kronecker product are the pairwise products of the singular values of the factors, so its rank is the product of the ranks. For $\mathsf{M}_2(\tilde Q_1)$ the determinant is $\langle\tilde Q_1\rangle_{\natural}$, so the rank is $2$ when $\langle\tilde Q_1\rangle_{\natural}\neq0$, $1$ when $\tilde Q_1\neq0$ and $\langle\tilde Q_1\rangle_{\natural}=0$, and $0$ when $\tilde Q_1=0$; the same holds for $\tilde Q_2$.

**Theorem 5 (the two ranks are independent).** Neither $\operatorname{rank}M$ nor $\operatorname{rank}c(M)$ determines the other.
(i) The rank-one matrix $M_1=(u_2+u_3)(u_2+u_3)^{\mathsf T}$, with $u_i$ the $i$-th standard column of $\mathbb{C}^4$, has $\operatorname{rank}M_1=1$ and $\ell(M_1)=4$.
(ii) $P_+$ has $\operatorname{rank}P_+=2$ and $\ell(P_+)=1$.
(iii) Among the matrices of rank one, those of length four form a dense open subset.

*Proof.* (i) The matrix is
$$
M_1=\begin{pmatrix}0&0&0&0\\0&1&1&0\\0&1&1&0\\0&0&0&0\end{pmatrix},
$$
of rank one. Its coefficient matrix is
$$
c(M_1)=\tfrac12\operatorname{diag}(1,-1,1,1),
$$
of determinant $-\tfrac1{16}$ and rank $4$, so Theorem 2 gives $\ell(M_1)=4$ and the decomposition
$$
M_1=\tfrac12\bigl(T_{tt}-T_{xx}+T_{yy}+T_{zz}\bigr).
$$
(ii) $P_+=\tfrac12(T_{tt}-iT_{tz})=T_{e_t/2,\,e_t-ie_z}$, so $c(P_+)$ has rank $1$, while $P_+$ has rank $2$ (it is a projector onto a plane).
(iii) The condition $\ell\le3$ is $\operatorname{rank}c\le3$, which is closed. It is proper, by (i). The variety of rank-one matrices is the irreducible Segre variety, so a proper closed subset has dense open complement.

**The two ranks on examples.**

| $M$ | $\operatorname{rank}M$ | $\operatorname{rank}c(M)$ | $\ell(M)$ | decomposition |
|---|---|---|---|---|
| $T_{tt}+T_{tz}$ | $4$ | $1$ | $1$ | $T_{e_t,\,e_t+e_z}$ |
| $P_+$ | $2$ | $1$ | $1$ | $T_{e_t/2,\,e_t-ie_z}$ |
| $T_{\tilde Q_1,\tilde Q_2}$, $\tilde Q_1,\tilde Q_2\neq0$, $\langle\tilde Q_1\rangle_{\natural}=\langle\tilde Q_2\rangle_{\natural}=0$ | $1$ | $1$ | $1$ | by construction |
| $T_{tt}+T_{xx}$ | $2$ | $2$ | $2$ | $T_{e_t,e_t}+T_{e_x,e_x}$ |
| $M_1=(u_2+u_3)(u_2+u_3)^{\mathsf T}$ | $1$ | $4$ | $4$ | $\tfrac12(T_{tt}-T_{xx}+T_{yy}+T_{zz})$ |
| generic $M$ | $4$ | $4$ | $4$ | four terms, none removable |

**How to decide, and how to decompose.** Compute the sixteen numbers $\tfrac14\operatorname{Tr}(T_{\mu\nu}^{\dagger}M)$ and form the $4\times4$ array $c$. If $\operatorname{rank}c=1$, then $M$ is a product: take $\tilde Q_1$ to be the element whose coordinate column $[Q_1]$ is any nonzero column of $c$, and $\tilde Q_2$ the element whose coordinate column $[Q_2]$ is the corresponding row divided by the entry where that column is nonzero. If $\operatorname{rank}c=r>1$, then $M$ is a sum of $r$ products and of no fewer; a rank factorisation $c=UV$ of the array gives the $r$ terms, as in the proof of Theorem 2. No test on $\operatorname{rank}M$ alone decides the question, by Theorem 5.

**Remark (the invertible products).** By Lemma 2 and the composition law, the invertible products form a subgroup of $\mathrm{GL}_4(\mathbb{C})$ isomorphic to $\bigl(\mathbb{B}^{\times}\times\mathbb{B}^{\times}\bigr)/\mathbb{C}^{\times}$, of dimension $7$. It is a small subgroup of a group of dimension $16$, and it is not the set of all invertible matrices: an invertible matrix is a product exactly when its coefficient matrix has rank one.

**The answer in one line.** A matrix is a left times a right matrix exactly when its coefficient matrix has rank one; the product set is a closed cone of dimension $7$ inside a space of dimension $16$, and every matrix is a sum of at most four of its elements.

## Worked Example

Take
$$
\tilde Q_1=(2+i)e_t+(1-i)\vec e_x+3\vec e_y+i\vec e_z,\qquad \tilde Q_2=\vec e_x .
$$
Then $T_{\tilde Q_1,\tilde Q_2}=L_{\tilde Q_1}R_x$. In the basis,
$$
T_{\tilde Q_1,\tilde Q_2}=(2+i)T_{tx}+(1-i)T_{xx}+3T_{yx}+iT_{zx},
$$
and the four matrices are read off the display above. The sum is
$$
T_{\tilde Q_1,\tilde Q_2}=
\begin{pmatrix}
0&0&1-3i&-1+4i\\
0&0&-1-2i&1-i\\
1-3i&-1+4i&0&0\\
-1-2i&1-i&0&0
\end{pmatrix}.
$$
Column $j$ is the coordinate column of $\tilde Q_1\,P_j\,e_x$ in the canonical frame; the matrix is block anti-diagonal, the two blocks carrying the two Peirce planes.

## What Remains Open

The following are candidate articles, not results. None of them is written, and the frame question is not settled by this article.

- The classification of gamma sets in $M_4(\mathbb{C})$: is every frame of the normal form above, and what is the stabiliser of the cell frame?
- The choice of frame as a choice of Clifford structure: which gradings the algebra admits, and how they are related.
- A dictionary, frame by frame, between the explicit gamma matrices of the physics articles and the tensor basis. The corpus has eighteen explicit representations, and they need not use the same $(\beta,\delta)$.
- Which physical statements are frame-independent, and which are artefacts of a table. The mass bilinear, the axial current and the chiral projectors are the first candidates.
- The $\gamma_5$ sign and the choice of the second central root of $-1$, the sign $\chi=i\tilde\Xi_{\mathrm{ad}}$; the two conventions must not be mixed inside one computation.
- The Peirce image of a general frame, and the spinor-basis change that relates two frames.
- The Segre length in physics: the equations are known, since the matrices of length at most $r$ are the locus $\operatorname{rank}c\le r$, cut out by the $(r+1)\times(r+1)$ minors; what is not known is which physical operators have length two or three, and why.
- The two-sided Dirac operator against the left gradient: the dictionary at the level of differential operators, not only of matrices.
- The odd sector, the module structure and the reality conditions in a frame that is not the reference frame.

## Summary

The two-sided operators on $\mathbb{B}$ form the algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\cong\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, whose matrix representation in the canonical frame is $M_4(\mathbb{C})$. The sixteen matrices $T_{\mu\nu}=L_\mu R_\nu$ are a basis. They are built from the four left matrices and the four right matrices, each right matrix read from the corresponding left one by one fixed exchange of the two mixed Peirce units: $R_\nu=\mathsf S L_\nu^{\mathsf T}\mathsf S^{-1}$ and $T_{\mu\nu}=L_\mu R_\nu=L_\mu\mathsf S L_\nu^{\mathsf T}\mathsf S^{-1}$, by ordinary matrix multiplication. The Pauli–Kronecker display $T_{\mu\nu}=\mathsf M_2(e_\nu)^{\mathsf T}\otimes\mathsf M_2(e_\mu)$ is the legacy evaluation of the same identity. They are invertible, of determinant $1$, orthogonal for the Hilbert–Schmidt form, closed under multiplication up to sign, and their span contains singular matrices. The correct product is at the algebra level, and in matrices it is the ordinary product of a left matrix and a right matrix; the Kronecker product of two $4\times4$ matrices is not the construction, and the $M_2$ Kronecker display is its legacy form. The bilinear sandwich is one member of the family, with the second parameter tied to the first. The Dirac gammas are $i$ times the five products $L_{e_t}R_\delta$ and $L_{e_k}R_\beta$ for a pair $(\beta,\delta)$ of orthogonal spatial directions; the reference frame takes $(e_y,e_x)$. Nothing selects the pair. Only pairs of coordinate axes make the five into cells; a generic pair gives five single products of coefficient rank one, each spread over several cells. The pair is a free parameter of the construction: no Clifford relation mentions it. What survives a change of pair are the relations, the isomorphism with $\mathrm{Cl}_{1,3}(\mathbb{C})$, and the type of each generator (right multiplication or two-sided); what does not survive is the matrices, the cell labels, the grade column and the sign of $\gamma_5$. In the corpus frame the sixteen products of the five gammas are the sixteen cells up to units.

For the product question, write $M=\sum c_{\mu\nu}T_{\mu\nu}$ with $c(M)_{\mu\nu}=\tfrac14\operatorname{Tr}(T_{\mu\nu}^{\dagger}M)$. Then $M=L_{\tilde Q_1}R_{\tilde Q_2}$ exactly when $c(M)=[Q_1][Q_2]^{\mathsf T}$, that is, exactly when $c(M)$ has rank one. The least number of products in a sum is $\operatorname{rank}c(M)$; every matrix is a sum of at most four, and a generic matrix needs four. The product set is the closed cone over the Segre $\mathbb{P}^3\times\mathbb{P}^3$, of dimension seven, not the algebra of dimension sixteen. Matrix rank does not decide the question: the rank-one block $M_1=(u_2+u_3)(u_2+u_3)^{\mathsf T}$ needs four products, while $P_+$ has rank two and is one product.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, complex dimension $4$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the coefficient basis |
| $L_{\tilde Q}=\mathsf{M}_4^{L}(\tilde Q)$ | left multiplication, the $M_4(\mathbb{C})_{\mathbb{B},L}$ matrix, $L_\mu=L_{e_\mu}$ |
| $R_{\tilde Q}$ | right multiplication, $\tilde Q_3\mapsto\tilde Q_3\tilde Q$, $R_\mu=R_{e_\mu}$ |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | quaternion conjugation in the coefficient basis |
| $T_{\tilde Q_1,\tilde Q_2}=L_{\tilde Q_1}R_{\tilde Q_2}$ | the two-sided operator $\tilde Q_3\mapsto\tilde Q_1\tilde Q_3\tilde Q_2$ |
| $[Q]=(Q_t,Q_x,Q_y,Q_z)^{\mathsf T}$ | the coordinate column of $\tilde Q$ |
| $T_{\mu\nu}=L_\mu R_\nu$ | the sixteen basis matrices |
| $\mathsf S$ | the exchange of $\vec\Upsilon_+$ and $\vec\Upsilon_-$ fixing $\tilde\Pi_\pm$; the swap of the second and third canonical coordinates, $\operatorname{diag}(1,1,-1,1)$ in the coefficient basis; $R_{\tilde Q}=\mathsf S L_{\tilde Q}^{\mathsf T}\mathsf S^{-1}$ |
| $C_{\Pi}$ | the Peirce change, $\det C_{\Pi}=-\tfrac14$, from the canonical frame to the coefficient basis |
| $\Theta_{\tilde Q}=T_{\tilde Q,\tilde Q^{*}}$ | the bilinear sandwich |
| $\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ | the quaternionic norm, the determinant of $\mathsf M_2(\tilde Q)$ |
| $\beta,\delta$ | the two right directions of a frame, $\beta^2=\delta^2=-e_t$, $\beta\delta=-\delta\beta$ |
| $G=-iT_{ty}$ | the grading in the multiplicity factor of the gamma set |
| $\Gamma_t,\Gamma_1,\Gamma_2,\Gamma_3$ | $\Gamma_t=iT_{e_t,e_x}$, $\Gamma_k=L_{i\vec e_k}G$ |
| $\gamma_0,\gamma_1,\gamma_2,\gamma_3,\gamma_5$ | one Dirac frame; five cells multiplied by $i$ in the reference frame |
| $c(M)$ | the coefficient matrix, $c(M)_{\mu\nu}=\tfrac14\operatorname{Tr}(T_{\mu\nu}^{\dagger}M)$ |
| $\ell(M)$ | the least number of products summing to $M$; equal to $\operatorname{rank}c(M)$ |
| $\Sigma^{\mu\nu}=\tfrac{i}{2}[\gamma_\mu,\gamma_\nu]$ | the Lorentz generators, six even cells |

## Further Reading

- [$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant](m4c-model-the-product-the-trace-and-the-determinant.html), for the left matrices and the model
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for the abstract algebra and the theorem that it is the endomorphism algebra
- [The Matrix Algebra $M_4(\mathbb{C})$](the-matrix-algebra-m4c.html), for the construction of $M_4(\mathbb{C})$ from the sandwich map and the change to the matrix-unit basis
- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the family, its composition, its adjoint and its type criteria
- [One-Sided Operators on the Biquaternion Algebra](one-sided-operators-on-the-biquaternion-algebra.html), for the two regular families
- [$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Sandwich](the-sandwich-in-the-m4c-l-model.html), for the congruence $MXM^{\dagger}$
- [$M_4(\mathbb{C})_{\mathbb{B}}$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes](m4c-model-the-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the Peirce basis, the chiral blocks and the matrix units $L_{P_i}R_{P_j}$
- [$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant](m2c-model-the-product-the-trace-and-the-determinant.html), for the $2\times2$ model and the Kronecker factors
- [Conventions of the Matrix Models](../articles_physics/conventions-of-the-matrix-models.html), for the explicit chiral matrices of one frame, the Peirce match and the chirality
