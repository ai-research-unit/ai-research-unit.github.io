# __Matrix Representations Conventions__

## Introduction

The algebra is read in matrices in two ways: the $2\times2$ isomorphism and the $4\times4$ regular representation. This article carries both. It assumes the base of *Algebra and Element Conventions* and the products of *Product and Form Conventions*.

The order is deliberate. The $2\times2$ isomorphism comes first because it is the representation of the element, the one the numerical checks use and the one whose four images are forced. The $4\times4$ regular representation comes second because it is the representation of the operator of multiplication, and it is read only after the frame is named. The Clifford structure closes the article: it is the algebra of the two-sided operators, the gamma matrices are one basis of it, and the Clifford reading is its real-linear link to the even subalgebra.

## The Matrix Representations

The algebra is read in matrices in two ways, and the two answer different questions. The **2×2 reading** is the isomorphism $\mathsf{M}_2 : \mathbb{B} \to M_2(\mathbb{C})$: the elements themselves become complex matrices, and this is the only reading whose matrices are of the algebra's own size. The **4×4 reading** is the regular representation $\rho_L : \mathbb{B} \to \mathrm{End}_{\mathbb{C}}(\mathbb{B}) = M_4(\mathbb{C})$: an element becomes the operator of left multiplication on the algebra taken as a complex vector space, and its matrix acts on the coordinate column of the frame. The image is the four-dimensional subspace $\mathbb{B}_L$ of $M_4(\mathbb{C})$, not the ambient algebra: the two readings are different representations, not two sizes of one, and only $\mathsf{M}_2$ is an isomorphism of the algebra onto matrices of its own size.

### General Matrix Conventions

**A matrix carries no tilde, and the ban is absolute.** The tilde marks an element of the algebra, not its image. The identity is $I_n$, with $\mathsf{M}_2(e_t)=I_2$ and $\mathsf{M}_4^{L}(e_t)=I_4$, and the image of an element is written $\mathsf{M}_2(\tilde Q)$ or $\mathsf{M}_4^{L}(\tilde Q)$, with the tilde inside the argument. **An array of biquaternions carries no tilde either.** A matrix whose entries are biquaternions is written $\mathsf{Q}=(\tilde Q_{\lambda\rho})\in\mathbb{B}^{n\times m}$: the tildes sit on the entries, and the array that holds them has none, whatever its size and whatever its entries. The identity matrix never takes a tilde; nor do the regular matrices $\mathsf{M}_4^{L}$ and $\mathsf{M}_4^{R}$, whose subscript gives the size and whose superscript gives the side of the multiplication. The same ban covers a matrix of biquaternions and a colour matrix.

**The ban is on the array, not on its argument.** The writings $\mathsf{M}_2(\tilde Q)$ and $\mathsf{M}_4^{L}(\tilde Q)$ are correct because the tilde stays inside the argument. A tilde on the array — $\tilde I_n$, $\tilde{\mathsf{M}}_2$, $\tilde{\mathcal Q}$, or $\tilde Q$ where the matrix $\mathsf{M}_2(\tilde Q)$ is meant — is forbidden and is a defect to be rewritten, not a variant to be read: no object is behind it, and the element it would name is already named by the argument.

**The letter $M$ belongs to matrices.** It names a matrix and nothing else: the images $\mathsf{M}_2(\tilde Q)$ and $\mathsf{M}_4^{L}(\tilde Q)$, the matrix algebras $M_2(\mathbb{C})$ and $M_4(\mathbb{C})$, and an entrywise matrix in a proof. No element of the algebra is written $M$, with or without a tilde.

**The copy is named, the ambient is not.** The left copy is $\mathbb{B}_L=\rho_L(\mathbb{B})$, also written $M_4(\mathbb{C})_{\mathbb{B}_L}$, and the right copy is $\mathbb{B}_R=\rho_R(\mathbb{B})$, also written $M_4(\mathbb{C})_{\mathbb{B}_R}$. Each is a subalgebra of $M_4(\mathbb{C})$ isomorphic to $M_2(\mathbb{C})$, and each is the commutant of the other. $M_4(\mathbb{C})=\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ is the ambient operator algebra and is never called a biquaternion algebra. The writing $M_4(\mathbb{C})_L$, read as the name of an algebra, is retired and is read here as $M_4(\mathbb{C})_{\mathbb{B}_L}$; the same holds on the right. The convention is stated here.

### The 2×2 Matrix Representation

The algebra is read as the complex $2 \times 2$ matrices, under the isomorphism

$$
\mathsf{M}_2 : \mathbb{B} \to M_2(\mathbb{C}),
$$

in *The Element and Operator Representations*, and this is the representation every numerical check in the series is performed with. The four unit images are fixed here, once, because every article depends on them agreeing. The three vector units are the Pauli matrices times $-i$:

$$
\mathsf{M}_2(e_t) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2, \qquad
\mathsf{M}_2(\vec e_x) = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix} = -i\sigma_1, \qquad
\mathsf{M}_2(\vec e_y) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = -i\sigma_2, \qquad
\mathsf{M}_2(\vec e_z) = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix} = -i\sigma_3,
$$

with the Pauli matrices

$$
\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad
\sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad
\sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},
$$

and the central scalar mapping to $\mathsf{M}_2(i) = iI_2$. Because $\mathsf{M}_2$ is $\mathbb{C}$-linear, the Hermitian units require no separate choice, $\mathsf{M}_2(i\vec e_k) = i\,\mathsf{M}_2(\vec e_k)$.

**The trace is the trace of this image.** The Hermitian form is defined on the algebra and needs no matrix. The trace is defined only here, on the image, and it is a reading of the Hermitian form in this presentation, not a second pairing. The series writes

$$
\operatorname{Tr}(\tilde{Q}) := \operatorname{Tr}\mathsf{M}_2(\tilde{Q}).
$$

On the units $\operatorname{Tr}(e_t) = 2$ and $\operatorname{Tr}(\vec e_k) = 0$, so on a general element $2\,\mathrm{Sc}(\tilde{Q}) = \operatorname{Tr}(\tilde{Q})$. That factor $2$ is not a normalisation but a consequence of $\mathsf{M}_2(e_t) = I_2$: it comes with the four images above and cannot be divided out. The probability pairing is written in the Hermitian form and read in the trace where the $2\times2$ image is used, the Born rule among them,

$$
2\langle\tilde Q_1,\tilde Q_2\rangle_{*}=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\operatorname{Tr}(\tilde Q_1\tilde Q_2^{*}),\qquad 2\,\mathrm{Sc}(\tilde Q)=\operatorname{Tr}(\tilde Q),
$$

and this is the only place in the section where the trace appears. An unsubscripted trace means this one; a regular matrix has its own, written with its subscript. The identity $2\,\operatorname{Sc}(\tilde{Q}_1\tilde{Q}_2) = \operatorname{Tr}(\tilde{Q}_1\tilde{Q}_2)$ is the same reading applied to the plain form, not a probability statement. The same element in the regular $4\times4$ representation has trace $4\,\mathrm{Sc}(\tilde{Q})$, twice the trace of the $2\times2$ image: the factor belongs to the presentation, not to the element.

**The determinant is the norm.** The determinant of the image is the biquaternion norm, $\det\mathsf{M}_2(\tilde{Q})=\langle\tilde{Q}\rangle_{\natural}$, and it is multiplicative, which is what makes the matrix model compute every norm in the series. The invertibility criterion, the group of units and the unit-norm group are read from it; the derivations are *Introduction to the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})_{\mathbb{H}}$ of Quaternions*.

**The assignment is forced, not chosen.** $\vec e_k^2 = -e_t$ requires the factor $i$ and $\vec e_x \vec e_y = \vec e_z$ fixes the sign, so neither the factor nor the sign in the three vector images could have been otherwise. A reviewer must not "correct" the assignment by making the three images real, nor by negating all three. *Introduction to the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})_{\mathbb{H}}$ of Quaternions* derives both.

**Never conjugate the matrix entries on their own.** Conjugating the entries of $\mathsf{M}_2(\tilde{Q})$ is *not* the image of any involution of the algebra: it negates the images of $\vec e_x$ and $\vec e_z$ while leaving $\mathsf{M}_2(\vec e_y)$, which has real entries, untouched, and so it destroys the sector dictionary. The four conjugations $\natural$, $\bar{\phantom{Q}}$, ${}^{*}$ and $\flat$ are evaluated through the matrix formulas recorded in *The Element and Operator Representations*, never by conjugating entries.

**The realisation is a convention of presentation, not of content.** The isomorphisms that preserve the subspace dictionary are the $\mathsf{M}_{2,\mathrm{S}} = S\mathsf{M}_2 S^{-1}$ with $S$ $*$-unitary up to a nonzero complex scalar, and an arbitrary invertible $S$ destroys the dictionary. The practical consequence is that a mistake of translation between the algebra and its matrices is repaired **here** — by correcting the assignment or the explicit factors of $i$ — and never by altering the biquaternion norm, the $ict'$ assignment or the sector split.

**A bare $\mathsf{M}_2$ means this isomorphism and nothing else.** A plain $\mathsf{M}_2$, with no subscript, superscript or tilde, is reserved throughout the series for this isomorphism alone. The other uses a reader may meet are marked differently: $\varphi$ is an abstract homomorphism on the mathematics pages and an angle in the Thomas-precession exercise, $\tilde{\Phi} = \varphi\,e_t$ is the central scalar field of the Higgs articles, and $\Phi_{\tilde{U}}$ is the quantum channel of the gates article. None of these is the isomorphism, and a bare $\mathsf{M}_2$ is not any of them.

### The 4×4 Matrix Representation

**The reading.** The $4\times4$ reading is the regular representation, and it answers a different question from the $2\times2$ isomorphism: it reads an element as the operator of multiplication on the algebra taken as a complex vector space. Left multiplication is $\rho_L:\mathbb{B}\to\mathrm{End}_{\mathbb{C}}(\mathbb{B})=M_4(\mathbb{C})$,
$$
\rho_L(\tilde Q_1)(\tilde Q_2)=\tilde Q_1\tilde Q_2,
$$
and right multiplication is $\rho_R(\tilde Q_1)(\tilde Q_2)=\tilde Q_2\tilde Q_1$. The image is the four-dimensional subspace $\mathbb{B}_L=\rho_L(\mathbb{B})$ of the ambient $M_4(\mathbb{C})$, not the ambient algebra, and likewise $\mathbb{B}_R$ on the right. Each copy is a subalgebra isomorphic to $M_2(\mathbb{C})$, and each is the commutant of the other.

**The canonical frame.** The frame is fixed here: the standard pair and the mixed units
$$
\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z),\qquad
\vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y),
$$
with $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$ and $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$, in the order $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$. Another gauge or another order of the four basis elements gives another matrix of the same operator; the formulas below hold in this frame.

**The block formula.** In the canonical frame the regular matrix is the $2\times2$ image taken twice, once per tensor factor:
$$
\mathsf{M}_4^{L}(\tilde Q)=I_2\otimes\mathsf{M}_2(\tilde Q),\qquad
\mathsf{M}_4^{R}(\tilde Q)=\mathsf{M}_2(\tilde Q)^{\mathsf T}\otimes I_2 .
$$
The first factor is the multiplicity and the second the matrix of the element. The left copy is the set of matrices $I_2\otimes A$ and the right copy the set $B\otimes I_2$: in the $4\times4$ matrix of an element the four blocks are $\mathsf{M}_2(\tilde Q)$, $0$, $0$, $\mathsf{M}_2(\tilde Q)$ on the left, and $M_{11}I_2$, $M_{21}I_2$, $M_{12}I_2$, $M_{22}I_2$ on the right, where $M_{ij}$ are the entries of $\mathsf{M}_2(\tilde Q)$.

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

**The invariants.** With $\det\mathsf{M}_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ and $\operatorname{tr}\mathsf{M}_2(\tilde Q)=2Q_t$,
$$
\det\mathsf{M}_4^{L}(\tilde Q)=\det\mathsf{M}_4^{R}(\tilde Q)=\langle\tilde Q\rangle_{\natural}^{2},
\qquad
\operatorname{tr}\mathsf{M}_4^{L}(\tilde Q)=\operatorname{tr}\mathsf{M}_4^{R}(\tilde Q)=4\,\mathrm{Sc}(\tilde Q).
$$
The determinant is the square of the biquaternion norm and the trace is four times the scalar part; both are properties of the element, read in the regular representation. The explicit frame, the product, the determinant and the volume identity are *The General Quaternionic Algebra in the $4\times4$ Left Regular Representation* in the mathematics corpus, and the operator reading is *The Element and Operator Representations*.

**No entry is read without the frame.** Another gauge or another order of the four basis elements gives another matrix of the same operator; the block formula holds in the canonical frame alone. The explicit matrices of the mathematics model articles are in the canonical frame unless an article names the coefficient basis; the Peirce change $C_{\Pi}$ carries the canonical display to the coefficient display, and the physics articles use the canonical frame. The copy and the element are what the frame does not change.

### The Clifford Structure and the Gamma Matrices

**The Clifford algebra is the two-sided operator algebra.** The sixteen cells $T_{\mu\nu}=L_\mu R_\nu$ are linearly independent, and their complex span is all of $M_4(\mathbb{C})$. They multiply by $T_{\mu\nu}T_{\rho\sigma}=T_{e_\mu e_\rho,\,e_\sigma e_\nu}$, so the assignment $e_\mu\otimes e_\nu^{\mathrm{opp}}\mapsto T_{\mu\nu}$ is an algebra isomorphism
$$
\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\longrightarrow M_4(\mathbb{C})\cong\mathrm{Cl}_{1,3}(\mathbb{C}).
$$
The sixteen gamma products span over $\mathbb{R}$ the algebra $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$, of real dimension $16$, and the sixteen cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$, the opposite real form. The full Clifford structure, odd part included, is a structure of the two-sided operators themselves. It is not an external tool, and the even part is not a limitation.

**The gamma set.** The five Dirac matrices are two-sided operators of the frame, built from the left and right multiplications of *Operator and Calculus Conventions*, §*The Operators*: the left factor is a unit and the right factor a spatial unit,
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
They satisfy $\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_4$, $(\gamma_k)^2=-I_4$ and $\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3$.

**These are the generators of the $\mathbb{M}_-$ frame.** In the $\mathbb{B}$ frame of the series, whose material case is $Q_t=ict'$, the four generators that all square to $+I_4$ are
$$
\gamma_0(Q)=\gamma_0(x),\qquad \gamma_k(Q)=i\,\gamma_k(x),\quad k=1,2,3 .
$$
The printed matrices above are the ones of the $\mathbb{M}_-$ frame; the $\mathbb{B}$-frame matrices are obtained from them by multiplying the three spatial entries by $i$.

**Remark (the two coordinate frames, $\mathbb{B}$ and $\mathbb{M}_-$).** The series has exactly two coordinate frames, and they are not to be mixed. Both are fixed, with their metrics and their table, in *Frame Conventions*.

- The **$\mathbb{B}$ frame** is the biquaternion space read in its own coordinate, $Q_\mu\in\mathbb{C}$; on the material case $Q_t=ict'$ and $Q_k=q_k$, so $Q_t^2=-(ct')^2$. Its metric is $(1,1,1,1)$: every generator squares to $+I_4$.
- The **$\mathbb{M}_-$ frame** is the material real frame, $x_0=ct'$ and $x_k=q_k$, with $Q_t=ix_0$. Its metric is $(1,-1,-1,-1)$.

The d'Alembertian is one operator, $\Box=\partial^2/\partial Q_t^2+\Delta_Q=\Delta-\partial^2/\partial x_0^2$, and only its reading in the frame changes. A contraction stays inside one frame, $\gamma_\mu[\mathbb{B}]\partial/\partial Q_\mu$ or $i\gamma_\mu[\mathbb{M}_-]\partial/\partial x_\mu$; the mixed $\gamma_\mu[\mathbb{M}_-]\partial/\partial Q_\mu$ belongs to neither and is never written. A gamma display here is in the $\mathbb{M}_-$ frame unless it says otherwise. The other uses of the word are not coordinate frames: the five generators are the image of the Clifford map and are not a frame, the **canonical** and **Peirce** frames are bases that fix the matrix display, and a **rest frame** is a physical observer.

**The gamma index is written low in both frames.** The notation is $\gamma_\mu$: the position is a label for the component, and the gamma index is never raised or lowered, in either frame.

In the Pauli form the same five are
$$
\gamma_0=\sigma_1\otimes I_2,\qquad
\gamma_k=i\,\sigma_2\otimes\sigma_k,\qquad
\gamma_5=-\sigma_3\otimes I_2 .
$$

**The sixteen products are the sixteen cells.** The five generators are five cells up to a factor $i$, and the sixteen products of the five, in increasing grade, are the sixteen cells $T_{\mu\nu}=L_\mu R_\nu$:

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

Each row reads $T_{\mu\nu}$ as a unit coefficient times the $\gamma$-product; the inverse reading carries the conjugate coefficient, since $c\in\{1,-1,i,-i\}$. The cells are labelled by the frame units, not by spacetime indices: $L_\mu R_\nu$ with $\mu,\nu\in\{t,x,y,z\}$ is not the stress–energy tensor $T_{\mu\nu}$ of the physics articles. The proof, and the freedom in the choice of frame, are §*The Gamma Set, and the Choice Behind It* of *$M_4(\mathbb{C})_{\mathcal{T}}$ Representation : The Two-Sided Operators on the Biquaternion Algebra*. The gamma set is one set among many: another orthogonal pair gives another set of five matrices, the relations survive, and the cell labels do not.

**A gamma matrix is a coordinate, not an object.** The Dirac, Weyl and Majorana matrices are three bases of the same algebra, related by $S\gamma_\mu S^{-1}$ with $S$ invertible. A change of gamma basis is a change of basis, and the normal forms are those of *$M_4(\mathbb{C})_{\mathcal{T}}$ Representation : The Two-Sided Operators on the Biquaternion Algebra*, §*The Gamma Set, and the Choice Behind It*. No statement of the corpus depends on the basis written.

**The presentation is the stronger one for the corpus's purpose.** Four things are carried by the algebra and not by the gamma matrices. The state is an element of $\mathbb{B}$, and the left regular module is the Dirac spinor space, so no column and no minimal left ideal has to be chosen. The pairing $\operatorname{Tr}(\tilde Q_1\tilde Q_2^{*})$ and the three involutions are fixed by the algebra, whereas the Dirac adjoint needs a chosen $\gamma_0$. The two real sectors $\mathbb{M}_\pm$ and the $ict'$ metric are part of the data. The frame is internal: it is a set of cells, not an array of matrices carried from outside. The gamma algebra is recovered from these data; the data are not recovered from the gamma algebra.

**The Clifford reading.** The eight real units of $\mathbb{B}$ read as gamma products:
$$
e_t\mapsto I_4,\qquad
\vec e_x\mapsto\gamma_2\gamma_3,\qquad
\vec e_y\mapsto\gamma_3\gamma_1,\qquad
\vec e_z\mapsto\gamma_1\gamma_2,\qquad
i\mapsto-\gamma_0\gamma_1\gamma_2\gamma_3 .
$$
The reading is $\mathbb{R}$-linear, and in the canonical frame it is read entirely in cells, $e_\mu\mapsto T_{\mu t}$ and $i\mapsto T_{tz}$, so its image is the real span of the eight cells $T_{\mu t}$ and $T_{\mu z}$, of real dimension $8$. It agrees with left multiplication on the four real units and sends the scalar imaginary to right multiplication by $\vec e_z$: $i\tilde Q$ reads as $T_{tz}$ times the image of $\tilde Q$, not as $i$ times that image. That is the one place where it differs from $\mathsf{M}_4^{L}$: it is $\mathbb{R}$-linear, not $\mathbb{C}$-linear. It is the comparison with the even subalgebra of $\mathrm{Cl}_{1,3}$, written for a reader of the gamma literature. It is not a second representation of the complex algebra, and no gamma relation is a reason to change a convention. A bare $\mathsf{M}_4$ is written for neither; the regular matrices carry $L$ or $R$, and the reading carries no symbol of its own.

**The basis, read in cells.** On the eight real units the reading is

| $\tilde Q$ | Clifford image | cell |
|---|---|---|
| $e_t$ | $I_4$ | $T_{tt}$ |
| $\vec e_x$ | $\gamma_2\gamma_3$ | $T_{xt}$ |
| $\vec e_y$ | $\gamma_3\gamma_1$ | $T_{yt}$ |
| $\vec e_z$ | $\gamma_1\gamma_2$ | $T_{zt}$ |
| $i$ | $-\omega$ | $T_{tz}$ |
| $i\vec e_x$ | $\gamma_0\gamma_1$ | $T_{xz}$ |
| $i\vec e_y$ | $\gamma_0\gamma_2$ | $T_{yz}$ |
| $i\vec e_z$ | $\gamma_0\gamma_3$ | $T_{zz}$ |

The three quaternion units become the three spacelike bivectors and the three imaginary units the three timelike bivectors, all with positive coefficients. The only minus in the reading sits on $i$ itself, $i\mapsto-\omega$, and it is the freedom the correspondence carries: the sign of the pseudoscalar is a convention, and it fixes the sign of every entry in the last four rows.

**The odd part.** The reading lands in the even part. Multiplication by the fixed generator $\gamma_0$ reaches the odd part, and the two real sectors separate: $\gamma_0$ times the image of $\mathbb{M}_+$ is the vector space, and $\gamma_0$ times the image of $\mathbb{M}_-$ the trivector space. So a four-vector is $\gamma_0$ times the image of $w\in\mathbb{M}_+$, and a trivector is $\gamma_0$ times the image of $w\in\mathbb{M}_-$. The frame $\gamma_0$ is the one choice in the odd half of the reading, and it is fixed by the representation.

**Lorentz generators.** For $\mu\neq\nu$ the commutator is $\gamma_\mu\gamma_\nu-\gamma_\nu\gamma_\mu=2\gamma_\mu\gamma_\nu$, so

$$
\sigma_{\mu\nu}=\tfrac14[\gamma_\mu,\gamma_\nu]=\tfrac12\gamma_\mu\gamma_\nu
$$

is half a bivector. Read in cells and in biquaternions,

| generator | cell | biquaternion |
|---|---|---|
| $\sigma^{23}$ | $\tfrac12T_{xt}$ | $\tfrac12\vec e_x$ |
| $\sigma^{31}$ | $\tfrac12T_{yt}$ | $\tfrac12\vec e_y$ |
| $\sigma^{12}$ | $\tfrac12T_{zt}$ | $\tfrac12\vec e_z$ |
| $\sigma^{01}$ | $\tfrac12T_{xz}$ | $\tfrac12 i\vec e_x$ |
| $\sigma^{02}$ | $\tfrac12T_{yz}$ | $\tfrac12 i\vec e_y$ |
| $\sigma^{03}$ | $\tfrac12T_{zz}$ | $\tfrac12 i\vec e_z$ |

The spacelike generators are the half quaternion units and the boosts the half imaginary units, again with positive signs. The half is not removable: $\gamma_\mu\gamma_\nu$ is the bivector and the Lorentz generator is half of it.

**Reversal, conjugation and the two traces.** Clifford reversal, $\mathrm{rev}(\gamma_{\mu_1}\cdots\gamma_{\mu_k})=\gamma_{\mu_k}\cdots\gamma_{\mu_1}$, is quaternion conjugation under the reading: reversing the image of $\tilde Q$ gives the image of $\tilde Q^{\natural}$, checked on the eight real units, where both sides carry $+$ on $e_t$ and $i$ and $-$ on the six vector units. Hence the biquaternion norm is the Clifford norm built with the reversal: the image of $\tilde Q\tilde Q^{\natural}$ is the product of the image of $\tilde Q$ with its reversal.

Two traces must not be confused. The trace of the corpus formula is the $2\times2$ one, $\operatorname{Tr}_2$, and it equals twice the scalar part. The $4\times4$ trace of the image is twice the real part of that trace,

$$
2\,\mathrm{Re}\operatorname{Tr}_2(\tilde Q)=4\,\mathrm{Re}\,\mathrm{Sc}(\tilde Q).
$$

The last equality uses $\operatorname{Tr}_2(\tilde Q)=2\,\mathrm{Sc}(\tilde Q)$, which is the trace formula above. Both were checked on a general element with complex coefficients.

**The slash is not used.** The Dirac slash is not part of the notation of this corpus.
A contraction is written out with the index repeated in the same position, $\gamma_\mu p_\mu$ for a momentum.
A derivative contraction is written in one frame and never across two: $i\gamma_\mu\partial/\partial x_\mu$ with the generators of the $\mathbb{M}_-$ frame,
or $\gamma_\mu(Q)\partial/\partial Q_\mu$ with the $\mathbb{B}$-frame generators $\gamma_0(Q)=\gamma_0$, $\gamma_k(Q)=i\gamma_k$.
The mixed form $i\gamma_\mu\partial/\partial Q_\mu$ belongs to neither frame and is not used.
No index is raised or lowered and no metric tensor enters: the metric of the series is the sign vector $\varepsilon$ inside the product,
and $Q_t=ict'$ is substituted only on the material sector $\mathbb{M}_-$.
In the canonical frame the momentum contraction is a cell sum,
$$
\gamma_\mu p_\mu=iT_{tx}p_t-i\bigl(T_{xy}p_x+T_{yy}p_y+T_{zy}p_z\bigr),
$$
so the frame is visible in the formula.

## Summary

The $2\times2$ isomorphism $\mathsf{M}_2$ is fixed by four images: $e_t\mapsto I_2$, and the three vector units to $-i$ times the Pauli matrices, with $\mathsf{M}_2(i)=iI_2$ on the central scalar. The assignment is forced by $\vec e_k^2=-e_t$ and by $\vec e_x\vec e_y=\vec e_z$. The trace is twice the scalar part, the determinant is the biquaternion norm, and conjugating entries on their own is not an involution of the algebra. A bare $\mathsf{M}_2$ names this isomorphism and nothing else, and the realisation is fixed up to a star-unitary change of basis and a central scalar.

The $4\times4$ representation is the regular one, $\rho_L$ and $\rho_R$, and its image is a four-dimensional subalgebra of the ambient $M_4(\mathbb{C})$, not the ambient algebra. In the canonical Peirce frame the left matrix is $I_2\otimes\mathsf{M}_2(\tilde Q)$ and the right is $\mathsf{M}_2(\tilde Q)^{\mathsf T}\otimes I_2$. The four left matrices $L_\mu$ and the four right matrices $R_\nu$ are written out, the right ones in the $L\leftrightarrow R$ correspondence $R_\nu=\mathsf S L_\nu^{\mathsf T}\mathsf S^{-1}$, the five gamma matrices are two-sided operators of that frame, and their sixteen products are the sixteen cells $T_{\mu\nu}=L_\mu R_\nu$, written out entry by entry and tabulated against the gamma products. The determinant is the square of the norm and the trace is four times the scalar part. No entry is read without its frame, and no frame changes the element or the copy.

The Clifford structure is the algebra of the two-sided operators: $e_\mu\otimes e_\nu^{\mathrm{opp}}\mapsto T_{\mu\nu}$ is an isomorphism onto $M_4(\mathbb{C})\cong\mathrm{Cl}_{1,3}(\mathbb{C})$, the sixteen gamma products span $\mathrm{Cl}_{1,3}(\mathbb{R})$ and the sixteen cells span $\mathrm{Cl}_{3,1}(\mathbb{R})$. The five generators are cells of the canonical frame, $\gamma_0=iT_{tx}$, $\gamma_1=iT_{xy}$, $\gamma_2=iT_{yy}$, $\gamma_3=iT_{zy}$, $\gamma_5=-iT_{tz}$, and a change of gamma basis is a change of basis. The biquaternion presentation carries the spinor module, the pairing, the involutions and the two sectors without a chosen gamma basis. The Clifford reading is the $\mathbb{R}$-linear comparison with the even subalgebra; in the canonical frame $e_\mu\mapsto T_{\mu t}$ and $i\mapsto T_{tz}$. On the eight real units it sends the three vector units to the spacelike bivectors and the three imaginary units to the timelike ones, and the odd part is reached by the fixed generator: $\gamma_0$ times the image of $\mathbb{M}_+$ is the vector space, and $\gamma_0$ times the image of $\mathbb{M}_-$ the trivector space. The Lorentz generators are half the corresponding bivectors, $\sigma_{\mu\nu}=\tfrac12\gamma_\mu\gamma_\nu$ for $\mu\neq\nu$, Clifford reversal is quaternion conjugation, and the $4\times4$ trace is $2\,\mathrm{Re}\operatorname{Tr}_2=4\,\mathrm{Re}\,\mathrm{Sc}$, twice the real part of the $2\times2$ trace of the corpus formula.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ | The isomorphism of the element; $\mathsf{M}_2(e_t)=I_2$, $\mathsf{M}_2(\vec e_k)=-i\sigma_k$ |
| $\operatorname{Tr}\tilde Q=\operatorname{tr}\mathsf{M}_2(\tilde Q)$ | The trace, twice the scalar part |
| $\det\mathsf{M}_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ | The determinant, the biquaternion norm |
| $\rho_L,\rho_R$ | Left and right multiplication as linear maps, $\rho_L(\tilde Q_1)(\tilde Q_2)=\tilde Q_1\tilde Q_2$, $\rho_R(\tilde Q_1)(\tilde Q_2)=\tilde Q_2\tilde Q_1$ |
| $\mathbb{B}_L=M_4(\mathbb{C})_{\mathbb{B}_L}$ | The left copy, $\rho_L(\mathbb{B})$; $\mathbb{B}_R$ is its commutant |
| $\mathsf{M}_4^{L}(\tilde Q)=I_2\otimes\mathsf{M}_2(\tilde Q)$ | The left regular matrix in the canonical frame |
| $\mathsf{M}_4^{R}(\tilde Q)=\mathsf{M}_2(\tilde Q)^{\mathsf T}\otimes I_2=\mathsf S\mathsf{M}_4^{L}(\tilde Q)^{\mathsf T}\mathsf S^{-1}$ | The right regular matrix in the canonical frame |
| $\mathsf S$ | The exchange of $\vec\Upsilon_+$ and $\vec\Upsilon_-$ fixing $\tilde\Pi_\pm$; the swap of the second and third canonical coordinates, $\operatorname{diag}(1,1,-1,1)$ in the coefficient basis |
| $L_\mu=\mathsf M_4^{L}(e_\mu)$, $R_\mu=\mathsf M_4^{R}(e_\mu)$ | The four left and the four right matrices; the correspondence is $R_\nu=\mathsf S L_\nu^{\mathsf T}\mathsf S^{-1}$ |
| $T_{\mu\nu}=L_\mu R_\nu$ | The sixteen basis matrices; $T_{tt}=L_t$, $T_{tk}=R_k$, $T_{kt}=L_k$, $T_{jk}=L_jR_k$; their complex span is $M_4(\mathbb{C})\cong\mathrm{Cl}_{1,3}(\mathbb{C})$ |
| $\gamma_0,\dots,\gamma_3,\gamma_5$ | The five Dirac generators of the canonical frame, $\gamma_0=iT_{tx}$, $\gamma_1=iT_{xy}$, $\gamma_2=iT_{yy}$, $\gamma_3=iT_{zy}$, $\gamma_5=-iT_{tz}$ |
| $\sigma_{\mu\nu}=\tfrac12\gamma_\mu\gamma_\nu$ ($\mu\neq\nu$) | The Lorentz generators; half the bivectors of the table |

## Further Reading

- [Conventions in the Biquaternion Universe](conventions-in-the-biquaternion-universe.html), for the algebra and the element glyphs.
- [Conventions of the Products and the Forms](conventions-of-the-products-and-the-forms.html), for the products the matrix product mirrors.
- [Conventions of the Operators and the Calculus](conventions-of-the-operators-and-the-calculus.html), for the left and right multiplications these matrices represent.
- [Element and Operator Representations: The Three Actions](the-element-and-operator-representations.html), companion article, for the coefficient space and the three actions.
- [$M_4(\mathbb{C})_{\mathbb{B}_L}$ Model : The Product, the Trace and the Determinant](../articles_maths/m4c-model-the-product-the-trace-and-the-determinant.html), for the change of frame between the coefficient basis and the canonical frame.
- [$M_4(\mathbb{C})_{\mathcal{T}}$ Representation : The Two-Sided Operators on the Biquaternion Algebra](../articles_maths/m4c-representation-the-two-sided-operators-on-the-biquaternion-algebra.html), for the sixteen cells, the frames of the normal form and the proof of the cell table.
