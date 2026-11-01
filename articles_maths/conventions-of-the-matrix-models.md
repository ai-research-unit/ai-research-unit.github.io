# __Matrix Representations Conventions__

## Introduction

The algebra is read in matrices in two ways, and the two answer different questions. The **$2\times2$ isomorphism** $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ reads the element itself as a complex matrix of the algebra's own size; the **$4\times4$ regular representation** reads multiplication as a linear map on the algebra taken as a complex vector space, and its image is a four-dimensional subalgebra of the ambient $M_4(\mathbb{C})$.

The algebra is $M_2(\mathbb{C})$ and it is never $M_4(\mathbb{C})$. The ambient $M_4(\mathbb{C})=\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ is the operator algebra, it carries no biquaternion structure and takes no biquaternion name; the left and right copies are named $\mathbb{B}_L$ and $\mathbb{B}_R$, and the retired label $M_4(\mathbb{C})_L$ is read as $\mathbb{B}_L$.

The order is: the table of objects, the $2\times2$ isomorphism with its four forced images and its trace and determinant, the $4\times4$ regular representation in the canonical Peirce frame with the four left matrices $L_\mu$, the four right matrices $R_\nu$ and the sixteen basis matrices $T_{\mu\nu}=L_\mu R_\nu$, and the Clifford structure of the cells that closes it. The article assumes the base of *Algebra and Element Conventions* and the Peirce convention of *Special Element and Peirce Conventions*, whose standard pair fixes the frame.

## The Matrix Models

**The biquaternion algebra is $M_2(\mathbb{C})$, and it is never $M_4(\mathbb{C})$.** Two kinds of matrix model read it, and they answer different questions. The **isomorphism** $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ reads the element itself as a $2\times2$ complex matrix, of the algebra's own size. The **regular representation** reads multiplication as a linear map on the algebra taken as a complex vector space, and its target is $\mathrm{End}_{\mathbb{C}}(\mathbb{B})=M_4(\mathbb{C})$; its image is a four-dimensional subspace of that ambient algebra, not the ambient algebra. The two are different representations, not two sizes of one.

| object | writing | meaning |
|---|---|---|
| the algebra | $\mathbb{B}$ | $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$ |
| the isomorphism | $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ | the element read as a $2\times2$ matrix |
| the ambient | $M_4(\mathbb{C})=\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ | operators on the algebra as a vector space |
| the left copy | $\mathbb{B}_L=M_4(\mathbb{C})_{\mathbb{B}_L}=\rho_L(\mathbb{B})$ | four-dimensional subalgebra |
| the right copy | $\mathbb{B}_R=M_4(\mathbb{C})_{\mathbb{B}_R}=\rho_R(\mathbb{B})$ | the commutant of $\mathbb{B}_L$ |
| the matrix of an element | $\mathsf{M}_4^{L}(\tilde Q)$, $\mathsf{M}_4^{R}(\tilde Q)$ | the matrices of $\rho_L(\tilde Q)$, $\rho_R(\tilde Q)$ in the frame the article names; canonical by default |

### The 2×2 Isomorphism

**The map.** The isomorphism is $\mathbb{C}$-linear, multiplicative and bijective,
$$
\mathsf{M}_2:\mathbb{B}\longrightarrow M_2(\mathbb{C}),\qquad
\mathsf{M}_2(\tilde Q_1+\tilde Q_2)=\mathsf{M}_2(\tilde Q_1)+\mathsf{M}_2(\tilde Q_2),\qquad
\mathsf{M}_2(\tilde Q_1\tilde Q_2)=\mathsf{M}_2(\tilde Q_1)\mathsf{M}_2(\tilde Q_2),
$$
and it is the reading every numerical check in the corpus is performed with.

**The four unit images.** The images of the units are fixed once, because every article depends on them agreeing:
$$
\mathsf{M}_2(e_t)=I_2,\qquad
\mathsf{M}_2(\vec e_x)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix}=-i\sigma_1,\qquad
\mathsf{M}_2(\vec e_y)=\begin{pmatrix}0&-1\\1&0\end{pmatrix}=-i\sigma_2,\qquad
\mathsf{M}_2(\vec e_z)=\begin{pmatrix}-i&0\\0&i\end{pmatrix}=-i\sigma_3,
$$
with $\sigma_1,\sigma_2,\sigma_3$ the Pauli matrices,
$$
\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad
\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$
The central scalar is $\mathsf{M}_2(i)=iI_2$, and $\mathbb{C}$-linearity gives the Hermitian units, $\mathsf{M}_2(i\vec e_k)=i\,\mathsf{M}_2(\vec e_k)$.

**The assignment is forced.** $\vec e_k^2=-e_t$ requires the factor $i$, and $\vec e_x\vec e_y=\vec e_z$ fixes the sign. The three images cannot be made real, nor all three negated; *Introduction to the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})_{\mathbb{H}}$ of Quaternions* derives both.

**No frame is needed.** The isomorphism is a map of algebras and does not depend on a frame of $\mathbb{B}$. The four matrices above are the images of the units, not the entries of a matrix read in a basis, and no Peirce family enters. The frame enters only in the regular representation of §*The 4×4 Regular Representation*, which reads an operator on the algebra.

**The invariants.** The determinant of the image is the biquaternion norm and its trace is twice the scalar part,
$$
\det\mathsf{M}_2(\tilde Q)=\langle\tilde Q\rangle_{\natural},\qquad
\operatorname{tr}\mathsf{M}_2(\tilde Q)=2Q_t .
$$
The determinant is multiplicative, which is what makes the matrix model compute every norm in the corpus; the invertibility criterion, the group of units and the unit-norm group are read from it.

### The 4×4 Regular Representation

**The maps.** Left multiplication is the linear map $\rho_L:\mathbb{B}\to\mathrm{End}_{\mathbb{C}}(\mathbb{B})$, $\rho_L(\tilde Q_1)(\tilde Q_2)=\tilde Q_1\tilde Q_2$, and right multiplication is $\rho_R(\tilde Q_1)(\tilde Q_2)=\tilde Q_2\tilde Q_1$. The target is the ambient operator algebra $M_4(\mathbb{C})=\mathrm{End}_{\mathbb{C}}(\mathbb{B})$.

**The copy is named, the ambient is not.** The left copy is $\mathbb{B}_L=\rho_L(\mathbb{B})$, also written $M_4(\mathbb{C})_{\mathbb{B}_L}$, and the right copy is $\mathbb{B}_R=\rho_R(\mathbb{B})$, also written $M_4(\mathbb{C})_{\mathbb{B}_R}$. Each is a subalgebra of $M_4(\mathbb{C})$ isomorphic to $M_2(\mathbb{C})$, and $\mathbb{B}_R$ is the commutant of $\mathbb{B}_L$ in $M_4(\mathbb{C})$.

The subscript names the copy: $M_4(\mathbb{C})_{\mathbb{B}_L}$ is the left copy, $M_4(\mathbb{C})_{\mathbb{B}_R}$ the right, and $M_4(\mathbb{C})_{\mathbb{B}_L,\mathbb{B}_R}$ both. A bare $M_4(\mathbb{C})$ is the ambient, $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$; it carries no biquaternion structure and takes no biquaternion name. The two cones are written $M_4(\mathbb{C})_{\mathcal{T}}$ for the two-sided operators and $M_4(\mathbb{C})_{\Theta}$ for the sandwiches, whose names are in *Conventions of the Operator Families*.

**The subscript names the action, not a tensor slot.** $L$ is left multiplication and $R$ is right multiplication, read as on $L_{\tilde Q}$ and $R_{\tilde Q}$ in *Operator and Calculus Conventions*, §*The Operators*. In the canonical frame below the left copy is the second tensor factor and the right copy the first, and another choice of frame exchanges the two slots without exchanging the two actions. A subscript naming a slot would therefore change meaning with the frame, and the action does not.

**The canonical frame is the Peirce frame of the standard pair.** The matrix model fixes the family and the two mixed units,
$$
\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z),\qquad
\vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y),
$$
which satisfy
$$
\tilde\Pi_+^2=\tilde\Pi_+,\quad \tilde\Pi_-^2=\tilde\Pi_-,\quad \tilde\Pi_+\tilde\Pi_-=0,\quad
\vec\Upsilon_\pm^2=0,\quad \vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\quad \vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+ .
$$
So $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$ is a Peirce basis, and the frame is that basis in that order: the two elements of $\mathbb{B}\tilde\Pi_+$ first and those of $\mathbb{B}\tilde\Pi_-$ second. This is the frame of the $\mathsf{M}_2$ model, and it is a choice of frame inside the matrix model. The Peirce convention fixes no family (*Special Element and Peirce Conventions*, §*The Biquaternion Peirce Convention*), and the choice here is not a preferred pair: it is the frame the matrix model is written in.

**In this frame the two copies are the two tensor factors.**
$$
\rho_L(\tilde Q)=I_2\otimes\mathsf{M}_2(\tilde Q),\qquad
\rho_R(\tilde Q)=\mathsf{M}_2(\tilde Q)^{\mathsf T}\otimes I_2 .
$$
So the left copy is the set of matrices $I_2\otimes A$ and the right copy the set $B\otimes I_2$: in the $4\times4$ matrix of an element the four blocks are $\mathsf{M}_2(\tilde Q)$, $0$, $0$, $\mathsf{M}_2(\tilde Q)$ on the left, and $M_{11}I_2$, $M_{21}I_2$, $M_{12}I_2$, $M_{22}I_2$ on the right, where $M_{ij}$ are the entries of $\mathsf{M}_2(\tilde Q)$. The regular matrix is the $2\times2$ matrix taken twice.

**The four left matrices.** Write $L_\mu=\mathsf M_4^{L}(e_\mu)$ for the four units in the canonical frame. They are
$$
L_t=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
L_x=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix},
$$
$$
L_y=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
L_z=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix},
$$
each equal to $I_2\otimes\mathsf M_2(\vec e_k)$, with $\mathsf M_2(\vec e_k)=-i\sigma_k$. A general element is their linear combination,
$$
\mathsf M_4^{L}(\tilde Q)=Q_tL_t+Q_xL_x+Q_yL_y+Q_zL_z=I_2\otimes\mathsf M_2(\tilde Q).
$$

**The four right matrices.** Write $R_\nu=\mathsf M_4^{R}(e_\nu)$. Right multiplication is the transpose of left multiplication in the exchanged Peirce frame. Let $\mathsf S$ be the linear involution of the carrier that fixes the two idempotents and exchanges the two mixed Peirce units,
$$
\mathsf S\tilde\Pi_\pm=\tilde\Pi_\pm,\qquad
\mathsf S\vec\Upsilon_+=\vec\Upsilon_-,\qquad
\mathsf S\vec\Upsilon_-=\vec\Upsilon_+,
$$
the permutation of the second and third coordinates of the canonical frame. Its matrix there is
$$
\mathsf S=\begin{pmatrix}1&0&0&0\\0&0&1&0\\0&1&0&0\\0&0&0&1\end{pmatrix},
$$
symmetric and involutive, $\mathsf S^{\mathsf T}=\mathsf S=\mathsf S^{-1}$, of trace $2$ and determinant $-1$; in the coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ the same operator is the reflection $\operatorname{diag}(1,1,-1,1)$, which fixes $e_t,\vec e_x,\vec e_z$ and negates $\vec e_y$. It is a linear involution of the carrier, not an algebra map, not one of the sixteen cells and not a one-sided multiplication. The right matrix is then
$$
\mathsf M_4^{R}(\tilde Q)=\mathsf S\,\mathsf M_4^{L}(\tilde Q)^{\mathsf T}\mathsf S^{-1},\qquad
R_\nu=\mathsf S\,L_\nu^{\mathsf T}\,\mathsf S^{-1}.
$$
Explicitly,
$$
R_t=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
R_x=\begin{pmatrix}0&0&-i&0\\0&0&0&-i\\-i&0&0&0\\0&-i&0&0\end{pmatrix},
$$
$$
R_y=\begin{pmatrix}0&0&1&0\\0&0&0&1\\-1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
R_z=\begin{pmatrix}-i&0&0&0\\0&-i&0&0\\0&0&i&0\\0&0&0&i\end{pmatrix},
$$
and a general element is $\mathsf M_4^{R}(\tilde Q)=Q_tR_t+Q_xR_x+Q_yR_y+Q_zR_z=\mathsf M_2(\tilde Q)^{\mathsf T}\otimes I_2$.

**The Pauli form of the two families.** With $\sigma_1,\sigma_2,\sigma_3$ the Pauli matrices and $\mathsf M_2(\vec e_k)=-i\sigma_k$,
$$
L_t=I_2\otimes I_2,\qquad
L_k=-i\,I_2\otimes\sigma_k,\qquad
R_t=L_t,\qquad
R_x=-i\,\sigma_1\otimes I_2,\quad
R_y=+i\,\sigma_2\otimes I_2,\quad
R_z=-i\,\sigma_3\otimes I_2 .
$$
The Pauli line is the evaluation of the $L$-based definition, never its replacement.

**The sixteen basis matrices.** The sixteen cells are the ordinary products
$$
T_{\mu\nu}=L_\mu R_\nu=L_\mu\,\mathsf S\,L_\nu^{\mathsf T}\,\mathsf S^{-1},
$$
in four families,
$$
T_{tt}=L_tR_t=L_t,\qquad
T_{tk}=L_tR_k=R_k,\qquad
T_{kt}=L_kR_t=L_k,\qquad
T_{jk}=L_jR_k ,
$$
which is the $L\leftrightarrow R$ correspondence of the basis: the mixed cell with left unit $\mu$ and right unit $t$ is the left matrix of $\mu$, the mixed cell with left unit $t$ and right unit $\nu$ is the right matrix of $\nu$, and the purely spatial cells $T_{jk}$ are the only ones that are neither. In the Pauli form,
$$
T_{tt}=I_4,\qquad
T_{tk}=-i\,\sigma_k^{\mathsf T}\otimes I_2,\qquad
T_{kt}=-i\,I_2\otimes\sigma_k,\qquad
T_{jk}=-\sigma_k^{\mathsf T}\otimes\sigma_j .
$$

The sixteen, with their left and right factors, are
$$
\boxed{\;\begin{aligned}
&T_{tt}=L_tR_t,\quad T_{tx}=L_tR_x,\quad T_{ty}=L_tR_y,\quad T_{tz}=L_tR_z,\\
&T_{xt}=L_xR_t,\quad T_{xx}=L_xR_x,\quad T_{xy}=L_xR_y,\quad T_{xz}=L_xR_z,\\
&T_{yt}=L_yR_t,\quad T_{yx}=L_yR_x,\quad T_{yy}=L_yR_y,\quad T_{yz}=L_yR_z,\\
&T_{zt}=L_zR_t,\quad T_{zx}=L_zR_x,\quad T_{zy}=L_zR_y,\quad T_{zz}=L_zR_z.
\end{aligned}\;}
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

**The invariants.** With $\det\mathsf{M}_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ and $\operatorname{tr}\mathsf{M}_2(\tilde Q)=2Q_t$, the block form gives
$$
\det\mathsf{M}_4^{L}(\tilde Q)=\langle\tilde Q\rangle_{\natural}^{2},\qquad
\operatorname{tr}\mathsf{M}_4^{L}(\tilde Q)=4Q_t .
$$
The same values hold for $R$, because transposition and the permutation $\mathsf S$ change neither a determinant nor a trace.

**The frame is not the object.** Another gauge, another order of the four basis elements, or another Peirce family gives another matrix of the same operator; the two formulas above hold in the canonical frame alone. An article that uses another frame says so and gives the change of frame. What the frame does not change is the copy and the element: the matrix is an image of the element, never the element and never the algebra.

**The explicit matrices are written in the canonical frame.** The model articles display $\mathsf{M}_4^{L}(\tilde Q)=I_2\otimes\mathsf{M}_2(\tilde Q)$ in the canonical Peirce frame. The coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ is the conjugate display $C_{\Pi}(I_2\otimes\mathsf{M}_2)C_{\Pi}^{-1}$, with the Peirce change $C_{\Pi}$. The articles whose subject is the transpose dictionary use the coefficient basis, because quaternion conjugation is transposition there, and each declares it. An article that uses another frame declares it; an entry is read only with the frame that produced it.

**The label $M_4(\mathbb{C})_L$ is retired.** It named a matrix set rather than an algebra, and it changed meaning with the basis. An older article that writes $M_4(\mathbb{C})_L$ is read as $M_4(\mathbb{C})_{\mathbb{B}_L}$, and one that writes $M_4(\mathbb{C})_R$ as $M_4(\mathbb{C})_{\mathbb{B}_R}$. The same rule governs the matrices: a bare $\mathsf{M}_4$ is not written for a regular matrix, which carries the superscript $L$ or $R$.

### The Clifford Structure

**The Clifford algebra is the cell algebra.** The sixteen cells $T_{\mu\nu}=L_\mu R_\nu$ are linearly independent, and their complex span is all of $M_4(\mathbb{C})$. They multiply by $T_{\mu\nu}T_{\rho\sigma}=T_{e_\mu e_\rho,\,e_\sigma e_\nu}$, so the assignment $e_\mu\otimes e_\nu^{\mathrm{opp}}\mapsto T_{\mu\nu}$ is an algebra isomorphism
$$
\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\longrightarrow M_4(\mathbb{C})\cong\mathrm{Cl}_{1,3}(\mathbb{C}).
$$
The sixteen products of the five frame cells span over $\mathbb{R}$ the algebra $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$, of real dimension $16$, and the sixteen cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$, the opposite real form. The Dirac, Weyl and Majorana matrices are three presentations of the same complex algebra, related by a change of frame; a change of frame is a change of basis, not a change of object.

**The five cells of the frame.** Write
$$
\boxed{\;\mathsf C_0=iR_x=iT_{tx},\qquad
\mathsf C_1=iL_xR_y=iT_{xy},\qquad
\mathsf C_2=iL_yR_y=iT_{yy},\qquad
\mathsf C_3=iL_zR_y=iT_{zy},\qquad
\mathsf C_5=-iR_z=-iT_{tz}\;}
$$
Each is a unit multiple of a cell; the left factor is a unit and the right factor a spatial unit. In the canonical frame the five are monomial matrices, written out in the appendix together with the Pauli evaluation.

**The Clifford relations.** They satisfy
$$
\{\mathsf C_\mu,\mathsf C_\nu\}=2g_{\mu\nu}I_4,\qquad
(\mathsf C_k)^2=-I_4,\qquad
\mathsf C_5=i\mathsf C_0\mathsf C_1\mathsf C_2\mathsf C_3,
$$
with $g=\operatorname{diag}(1,-1,-1,-1)$. No index is raised or lowered: the metric is the sign vector inside the product, not a tensor in the display.

**The sixteen products are the sixteen cells.** The five frame cells are five cells up to a factor $i$, and the sixteen products of the five are the sixteen cells:

| grade | cells |
|---|---|
| $0$ | $T_{tt}$ |
| $1$ | $T_{tx}$, $T_{xy}$, $T_{yy}$, $T_{zy}$ |
| $2$ | $T_{xt}$, $T_{xz}$, $T_{yt}$, $T_{yz}$, $T_{zt}$, $T_{zz}$ |
| $3$ | $T_{ty}$, $T_{xx}$, $T_{yx}$, $T_{zx}$ |
| $4$ | $T_{tz}$ |

Each row lists the cells of one grade, and the counts are $1+4+6+4+1=16$. The frame is one frame among many: another orthogonal pair $(\beta,\delta)$ gives another five cells, the relations survive, and the cell labels do not. The proof, and the freedom in the choice of frame, are in the appendix of *Two-Sided Operators on the Biquaternion Algebra*.

**The opposite algebra is written with three letters.** The opposite of an algebra, with the product reversed, carries the superscript $\mathrm{opp}$: the reversed product is $a\cdot_{\mathrm{opp}}b=ba$, and the opposite of $\mathbb{B}$ is $\mathbb{B}^{\mathrm{opp}}$. The two-letter form $\mathrm{op}$ is not used at all, neither for the opposite algebra nor for the operator norm, which is written $\lVert A\rVert$; the reason is that one letter out of three, at superscript size, does not separate the two meanings (*Index, Notation and Corpus Conventions*, §*The Superscripts*). Every place in this series where $\mathrm{op}$ once marked a norm now writes the norm bare, and the competing norms keep their own labels, $\lVert A\rVert_{\mathrm{HS}}$, $\lVert A\rVert_{\mathrm{nuc}}$, $\lVert A\rVert_F$, $\lVert A\rVert_*$.

**The comparison map.** The $\mathbb{R}$-linear map $\iota_{\mathrm{Cl}}$ of the Dirac articles is read in cells as $\iota_{\mathrm{Cl}}(e_\mu)=T_{\mu t}$ and $\iota_{\mathrm{Cl}}(i)=T_{tz}$. Its image is the real span of the eight cells $T_{\mu t}$ and $T_{\mu z}$, of real dimension $8$, and it satisfies $\iota_{\mathrm{Cl}}(i\tilde Q)=T_{tz}\,\iota_{\mathrm{Cl}}(\tilde Q)$. It is $\mathbb{R}$-linear and not $\mathbb{C}$-linear: it is the comparison with the even subalgebra of $\mathrm{Cl}_{1,3}$, not a second representation of $\mathbb{B}$.

**The slash is not used.** The Dirac slash is not part of the notation of the matrix models.
A contraction is written out with the index repeated in the same position, as the cell sum below for a momentum.
A derivative contraction is $i\mathsf C_\mu\partial/\partial x_\mu$ with $x_0=q'_t$,
in the $\mathbb{M}_-$ frame fixed in *Frame Conventions*.
If the $\mathbb{B}$ frame is used, it is written $\mathsf C_\mu(Q)\partial/\partial Q_\mu$ with the $\mathbb{B}$-frame generators $\mathsf C_0(Q)=\mathsf C_0(x)$ and $\mathsf C_k(Q)=i\mathsf C_k(x)$,
and never with the generators of the $\mathbb{M}_-$ frame: the mixed form $i\mathsf C_\mu(x)\partial/\partial Q_\mu$ belongs to neither frame.
No index is raised or lowered and no metric tensor enters: the metric of the series is the sign vector $\varepsilon$ inside the product, and the metric each frame carries is separated in *Frame Conventions*.
In the canonical frame the momentum contraction is a cell sum,
$$
\mathsf C_\mu p_\mu=i\bigl(T_{tx}p_t+T_{xy}p_x+T_{yy}p_y+T_{zy}p_z\bigr),
$$
so the frame is visible in the formula.

## Summary

The **$2\times2$ isomorphism** $\mathsf{M}_2$ is fixed by four images: $e_t\mapsto I_2$, the three vector units to $-i$ times the Pauli matrices, and $\mathsf{M}_2(i)=iI_2$ on the central scalar. The assignment is forced by $\vec e_k^2=-e_t$ and by $\vec e_x\vec e_y=\vec e_z$. The trace of the image is twice the scalar part, the determinant is the biquaternion norm $\langle\tilde Q\rangle_{\natural}$, and the determinant is multiplicative, which is what makes the matrix model compute every norm in the corpus.

The **$4\times4$ regular representation** is $\rho_L(\tilde Q_1)(\tilde Q_2)=\tilde Q_1\tilde Q_2$ and $\rho_R(\tilde Q_1)(\tilde Q_2)=\tilde Q_2\tilde Q_1$. The image of $\rho_L$ is the four-dimensional subalgebra $\mathbb{B}_L=M_4(\mathbb{C})_{\mathbb{B}_L}$ of the ambient $M_4(\mathbb{C})$, and $\mathbb{B}_R=M_4(\mathbb{C})_{\mathbb{B}_R}$ is its commutant; the ambient is an operator algebra and takes no biquaternion name. The side is $L$ unless written.

The **canonical frame** is the Peirce frame of the standard pair: $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ and $\vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y)$, with the four Peirce components in the order $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$. In it the left matrix is $I_2\otimes\mathsf{M}_2(\tilde Q)$ and the right matrix is $\mathsf{M}_2(\tilde Q)^{\mathsf T}\otimes I_2$, with the left coupling to the second tensor factor and the right to the first; the transpose is what makes right multiplication act on the first factor.

The label $M_4(\mathbb{C})_L$ is retired: it named a matrix set rather than an algebra, and it changed meaning with the basis. An older article that writes it is read as $\mathbb{B}_L$, and an older $M_4(\mathbb{C})_R$ as $\mathbb{B}_R$.

The **four left matrices** $L_\mu=\mathsf{M}_4^{L}(e_\mu)$ and the **four right matrices** $R_\nu=\mathsf{M}_4^{R}(e_\nu)$ are written out, with the $L\leftrightarrow R$ correspondence $R_\nu=\mathsf S L_\nu^{\mathsf T}\mathsf S^{-1}$, that is $\mathsf{M}_4^{R}(\tilde Q)=\mathsf S\mathsf{M}_4^{L}(\tilde Q)^{\mathsf T}\mathsf S^{-1}$.

The **sixteen basis matrices** are the products $T_{\mu\nu}=L_\mu R_\nu$, in four families: $T_{tt}=L_t$, $T_{tk}=R_k$, $T_{kt}=L_k$ and $T_{jk}=L_jR_k$. They are written entry by entry in the canonical frame, and the grade table reads each of them as a unit coefficient times a product of the five frame cells.

The **Clifford structure** is the algebra of the cells: $e_\mu\otimes e_\nu^{\mathrm{opp}}\mapsto T_{\mu\nu}$ is an isomorphism onto $M_4(\mathbb{C})\cong\mathrm{Cl}_{1,3}(\mathbb{C})$, the sixteen products of the five frame cells span $\mathrm{Cl}_{1,3}(\mathbb{R})$ and the sixteen cells span $\mathrm{Cl}_{3,1}(\mathbb{R})$. The five generators of the canonical frame are the cells $\mathsf C_0=iT_{tx}$, $\mathsf C_1=iT_{xy}$, $\mathsf C_2=iT_{yy}$, $\mathsf C_3=iT_{zy}$ and $\mathsf C_5=-iT_{tz}$; a change of frame is a change of basis. The map $\iota_{\mathrm{Cl}}$ is the $\mathbb{R}$-linear comparison with the even subalgebra, $\iota_{\mathrm{Cl}}(e_\mu)=T_{\mu t}$ and $\iota_{\mathrm{Cl}}(i)=T_{tz}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ | The isomorphism of the element; $\mathsf{M}_2(e_t)=I_2$, $\mathsf{M}_2(\vec e_k)=-i\sigma_k$ |
| $\operatorname{Tr}\tilde Q=\operatorname{tr}\mathsf{M}_2(\tilde Q)$ | The trace, twice the scalar part |
| $\det\mathsf{M}_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ | The determinant, the biquaternion norm |
| $\rho_L,\rho_R$ | Left and right multiplication as linear maps |
| $\mathbb{B}_L=M_4(\mathbb{C})_{\mathbb{B}_L}$ | The left copy, $\rho_L(\mathbb{B})$; $\mathbb{B}_R$ is its commutant |
| $\mathsf{M}_4^{L}(\tilde Q)=I_2\otimes\mathsf{M}_2(\tilde Q)$ | The left regular matrix in the canonical frame |
| $\mathsf{M}_4^{R}(\tilde Q)=\mathsf{M}_2(\tilde Q)^{\mathsf T}\otimes I_2=\mathsf S\mathsf{M}_4^{L}(\tilde Q)^{\mathsf T}\mathsf S^{-1}$ | The right regular matrix in the canonical frame |
| $\mathsf S$ | The exchange of $\vec\Upsilon_+$ and $\vec\Upsilon_-$ fixing $\tilde\Pi_\pm$; the swap of the second and third canonical coordinates, $\operatorname{diag}(1,1,-1,1)$ in the coefficient basis |
| $L_\mu=\mathsf M_4^{L}(e_\mu)$, $R_\mu=\mathsf M_4^{R}(e_\mu)$ | The four left and the four right matrices; the correspondence is $R_\nu=\mathsf S L_\nu^{\mathsf T}\mathsf S^{-1}$ |
| $T_{\mu\nu}=L_\mu R_\nu$ | The sixteen basis matrices; $T_{tt}=L_t$, $T_{tk}=R_k$, $T_{kt}=L_k$, $T_{jk}=L_jR_k$; their complex span is $M_4(\mathbb{C})\cong\mathrm{Cl}_{1,3}(\mathbb{C})$ |
| $\mathsf C_\mu,\mathsf C_5$ | The five cells of the canonical frame, $\mathsf C_0=iT_{tx}$, $\mathsf C_1=iT_{xy}$, $\mathsf C_2=iT_{yy}$, $\mathsf C_3=iT_{zy}$, $\mathsf C_5=-iT_{tz}$ |
| $\iota_{\mathrm{Cl}}$ | The $\mathbb{R}$-linear comparison with the even subalgebra; $\iota_{\mathrm{Cl}}(e_\mu)=T_{\mu t}$, $\iota_{\mathrm{Cl}}(i)=T_{tz}$ |
| $\tilde\Pi_\pm$, $\vec\Upsilon_\pm$ | The standard pair and its two mixed units, which fix the frame |

## Further Reading

- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636. The biquaternion conjugations and the conventions of the complexified algebra in the applied literature.
- Soo-Chang Pei, Ja-Han Chang and Jian-Jiun Ding, "Commutative reduced biquaternions and their Fourier transform for signal and image processing applications", *IEEE Transactions on Signal Processing* **52** (2004) 2012–2022. The reduced biquaternion algebra of the engineering literature, its idempotent decomposition, its ring-valued norm and its transform.
- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the sixteen cells, the frame and the proof of the cell table.
- [Conventions of the Matrix Models](../articles_physics/conventions-of-the-matrix-models.html), for the comparison with the even subalgebra and the five-cell frame.

## Appendix — The Gamma Formulation

The gammas are the five-cell frame of the body written as matrices; the body writes the cells.

**The five gammas.** The five Dirac matrices are two-sided operators of the frame,
$$
\boxed{\;\gamma_0=iR_x=iT_{tx},\qquad
\gamma_1=iL_xR_y=iT_{xy},\qquad
\gamma_2=iL_yR_y=iT_{yy},\qquad
\gamma_3=iL_zR_y=iT_{zy},\qquad
\gamma_5=-iR_z=-iT_{tz}\;}
$$
In the canonical frame their matrices are
$$
\gamma_0=\begin{pmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
\gamma_1=\begin{pmatrix}0&0&0&1\\0&0&1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix},
$$
$$
\gamma_2=\begin{pmatrix}0&0&0&-i\\0&0&i&0\\0&i&0&0\\-i&0&0&0\end{pmatrix},\qquad
\gamma_3=\begin{pmatrix}0&0&1&0\\0&0&0&-1\\-1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
\gamma_5=\begin{pmatrix}-1&0&0&0\\0&-1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}.
$$
They satisfy $\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_4$, $(\gamma_k)^2=-I_4$ and $\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3$. In the Pauli form the same five are
$$
\gamma_0=\sigma_1\otimes I_2,\qquad
\gamma_k=i\,\sigma_2\otimes\sigma_k,\qquad
\gamma_5=-\sigma_3\otimes I_2 .
$$

**The sixteen products.** The five generators are five cells up to a factor $i$, and the sixteen products of the five, in increasing grade, are the sixteen cells:

| grade | $\gamma$-product | cell | equality |
|---|---|---|---|
| $0$ | $1$ | $T_{tt}$ | $T_{tt}=I_4$ |
| $1$ | $\gamma_0$ | $T_{tx}$ | $T_{tx}=-i\,\gamma_0$ |
| $1$ | $\gamma_1$ | $T_{xy}$ | $T_{xy}=-i\,\gamma_1$ |
| $1$ | $\gamma_2$ | $T_{yy}$ | $T_{yy}=-i\,\gamma_2$ |
| $1$ | $\gamma_3$ | $T_{zy}$ | $T_{zy}=-i\,\gamma_3$ |
| $2$ | $\gamma_0\gamma_1$ | $T_{xz}$ | $T_{xz}=\gamma_0\gamma_1$ |
| $2$ | $\gamma_0\gamma_2$ | $T_{yz}$ | $T_{yz}=\gamma_0\gamma_2$ |
| $2$ | $\gamma_0\gamma_3$ | $T_{zz}$ | $T_{zz}=\gamma_0\gamma_3$ |
| $2$ | $\gamma_1\gamma_2$ | $T_{zt}$ | $T_{zt}=\gamma_1\gamma_2$ |
| $2$ | $\gamma_1\gamma_3$ | $T_{yt}$ | $T_{yt}=-\gamma_1\gamma_3$ |
| $2$ | $\gamma_2\gamma_3$ | $T_{xt}$ | $T_{xt}=\gamma_2\gamma_3$ |
| $3$ | $\gamma_0\gamma_1\gamma_2$ | $T_{zx}$ | $T_{zx}=-i\,\gamma_0\gamma_1\gamma_2$ |
| $3$ | $\gamma_0\gamma_1\gamma_3$ | $T_{yx}$ | $T_{yx}=i\,\gamma_0\gamma_1\gamma_3$ |
| $3$ | $\gamma_0\gamma_2\gamma_3$ | $T_{xx}$ | $T_{xx}=-i\,\gamma_0\gamma_2\gamma_3$ |
| $3$ | $\gamma_1\gamma_2\gamma_3$ | $T_{ty}$ | $T_{ty}=i\,\gamma_1\gamma_2\gamma_3$ |
| $4$ | $\gamma_0\gamma_1\gamma_2\gamma_3$ | $T_{tz}$ | $T_{tz}=i\,\gamma_5=-\gamma_0\gamma_1\gamma_2\gamma_3$ |

Each row reads $T_{\mu\nu}$ as a unit coefficient times the $\gamma$-product; the inverse reading carries the conjugate coefficient, since $c\in\{1,-1,i,-i\}$.

**The comparison map.** The $\mathbb{R}$-linear map $\iota_{\mathrm{Cl}}$ reads in gammas as $\iota_{\mathrm{Cl}}(\vec e_x)=\gamma_2\gamma_3$, $\iota_{\mathrm{Cl}}(\vec e_y)=\gamma_3\gamma_1$, $\iota_{\mathrm{Cl}}(\vec e_z)=\gamma_1\gamma_2$ and $\iota_{\mathrm{Cl}}(i)=-\gamma_0\gamma_1\gamma_2\gamma_3$, the same map as $\iota_{\mathrm{Cl}}(e_\mu)=T_{\mu t}$ and $\iota_{\mathrm{Cl}}(i)=T_{tz}$ of the body.

**The contractions.** In gamma notation a momentum contraction is $\gamma_\mu p_\mu=i(T_{tx}p_t+T_{xy}p_x+T_{yy}p_y+T_{zy}p_z)$, a derivative contraction is $i\gamma_\mu\partial/\partial x_\mu$ with $x_0=q'_t$, and a $\mathbb{B}$-frame contraction is $\gamma_\mu[\mathbb{B}]\partial/\partial Q_\mu$. The mixed form $i\gamma_\mu[\mathbb{M}_-]\partial/\partial Q_\mu$ belongs to neither frame.

Over $\mathbb{R}$ the products of the five span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.
