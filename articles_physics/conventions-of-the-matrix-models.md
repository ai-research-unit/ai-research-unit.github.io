# __Conventions of the Matrix Models__

## Introduction

The algebra is read in matrices in two ways: the $2\times2$ isomorphism and the $4\times4$ regular representation. This article carries both. It assumes the base of *Conventions in the Biquaternion Universe* and the products of *Conventions of the Products and the Forms*.

The order is deliberate. The $2\times2$ isomorphism comes first because it is the representation of the element, the one the numerical checks use and the one whose four images are forced. The $4\times4$ regular representation comes second because it is the representation of the operator of multiplication, and it is read only after the frame is named. The Clifford map closes the article, and it is neither of the two.

## The Matrix Representations

The algebra is read in matrices in two ways, and the two answer different questions. The **2×2 reading** is the isomorphism $\mathsf{M}_2 : \mathbb{B} \to M_2(\mathbb{C})$: the elements themselves become complex matrices, and this is the only reading whose matrices are of the algebra's own size. The **4×4 reading** is the regular representation $\rho_L : \mathbb{B} \to \mathrm{End}_{\mathbb{C}}(\mathbb{B}) = M_4(\mathbb{C})$: an element becomes the operator of left multiplication on the algebra taken as a complex vector space, and its matrix acts on the coordinate column of the frame. The image is the four-dimensional subspace $\mathbb{B}_L$ of $M_4(\mathbb{C})$, not the ambient algebra: the two readings are different representations, not two sizes of one, and only $\mathsf{M}_2$ is an isomorphism of the algebra onto matrices of its own size.

### General Matrix Conventions

**A matrix carries no tilde, and the ban is absolute.** The tilde marks an element of the algebra, not its image. The identity is $I_n$, with $\mathsf{M}_2(e_t)=I_2$ and $\mathsf{M}_4^{L}(e_t)=I_4$, and the image of an element is written $\mathsf{M}_2(\tilde Q)$ or $\mathsf{M}_4^{L}(\tilde Q)$, with the tilde inside the argument. **An array of biquaternions carries no tilde either.** A matrix whose entries are biquaternions is written $\mathsf{Q}=(\tilde Q_{\lambda\rho})\in\mathbb{B}^{n\times m}$: the tildes sit on the entries, and the array that holds them has none, whatever its size and whatever its entries. The identity matrix never takes a tilde; nor do the regular matrices $\mathsf{M}_4^{L}$ and $\mathsf{M}_4^{R}$, whose subscript gives the size and whose superscript gives the side of the multiplication. The same ban covers a matrix of biquaternions and a colour matrix.

**The ban is on the array, not on its argument.** The writings $\mathsf{M}_2(\tilde Q)$ and $\mathsf{M}_4^{L}(\tilde Q)$ are correct because the tilde stays inside the argument. A tilde on the array — $\tilde I_n$, $\tilde{\mathsf{M}}_2$, $\tilde{\mathcal Q}$, or $\tilde Q$ where the matrix $\mathsf{M}_2(\tilde Q)$ is meant — is forbidden and is a defect to be rewritten, not a variant to be read: no object is behind it, and the element it would name is already named by the argument.

**The letter $M$ belongs to matrices.** It names a matrix and nothing else: the images $\mathsf{M}_2(\tilde Q)$ and $\mathsf{M}_4^{L}(\tilde Q)$, the matrix algebras $M_2(\mathbb{C})$ and $M_4(\mathbb{C})$, and an entrywise matrix in a proof. No element of the algebra is written $M$, with or without a tilde.

**The copy is named, the ambient is not.** The left copy is $\mathbb{B}_L=\rho_L(\mathbb{B})$, also written $M_4(\mathbb{C})_{\mathbb{B},L}$, and the right copy is $\mathbb{B}_R=\rho_R(\mathbb{B})$, also written $M_4(\mathbb{C})_{\mathbb{B},R}$. Each is a subalgebra of $M_4(\mathbb{C})$ isomorphic to $M_2(\mathbb{C})$, and each is the commutant of the other. $M_4(\mathbb{C})=\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ is the ambient operator algebra and is never called a biquaternion algebra. The writing $M_4(\mathbb{C})_L$, read as the name of an algebra, is retired and is read here as $M_4(\mathbb{C})_{\mathbb{B},L}$; the same holds on the right. The convention is stated here.

### The 2×2 Matrix Representation

The algebra is read as the complex $2 \times 2$ matrices, under the isomorphism

$$
\mathsf{M}_2 : \mathbb{B} \to M_2(\mathbb{C}),
$$

in *The Element and Operator Representations*, and this is the representation every numerical check in the series is performed with. The four unit images are fixed here, once, because every article depends on them agreeing. The three vector units are the Pauli matrices times $-i$:

$$
\mathsf{M}_2(e_t) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2, \qquad
\mathsf{M}_2(\vec e_x) = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix}, \qquad
\mathsf{M}_2(\vec e_y) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad
\mathsf{M}_2(\vec e_z) = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix},
$$

with the central scalar mapping to $\mathsf{M}_2(i) = iI_2$. Because $\mathsf{M}_2$ is $\mathbb{C}$-linear, the Hermitian units require no separate choice, $\mathsf{M}_2(i\vec e_k) = i\,\mathsf{M}_2(\vec e_k)$.

**The trace is the trace of this image.** The Hermitian form is defined on the algebra and needs no matrix. The trace is defined only here, on the image, and it is a reading of the Hermitian form in this presentation, not a second pairing. The series writes

$$
\operatorname{Tr}(\tilde{Q}) := \operatorname{Tr}\mathsf{M}_2(\tilde{Q}).
$$

On the units $\operatorname{Tr}(e_t) = 2$ and $\operatorname{Tr}(\vec e_k) = 0$, so on a general element $2\,\mathrm{Sc}(\tilde{Q}) = \operatorname{Tr}(\tilde{Q})$. That factor $2$ is not a normalisation but a consequence of $\mathsf{M}_2(e_t) = I_2$: it comes with the four images above and cannot be divided out. The probability pairing is written in the Hermitian form and read in the trace where the $2\times2$ image is used, the Born rule among them,

$$
2\langle\tilde Q_1,\tilde Q_2\rangle_{*}=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\operatorname{Tr}(\tilde Q_1\tilde Q_2^{*}),\qquad 2\,\mathrm{Sc}(\tilde Q)=\operatorname{Tr}(\tilde Q),
$$

and this is the only place in the section where the trace appears. An unsubscripted trace means this one; a regular matrix has its own, written with its subscript. The identity $2\,\operatorname{Sc}(\tilde{Q}_1\tilde{Q}_2) = \operatorname{Tr}(\tilde{Q}_1\tilde{Q}_2)$ is the same reading applied to the plain form, not a probability statement. The same element in the regular $4\times4$ representation has trace $4\,\mathrm{Sc}(\tilde{Q})$, twice the trace of the $2\times2$ image: the factor belongs to the presentation, not to the element.

**The determinant is the norm.** The determinant of the image is the biquaternion norm, $\det\mathsf{M}_2(\tilde{Q})=\langle\tilde{Q}\rangle_{\natural}$, and it is multiplicative, which is what makes the matrix model compute every norm in the series. The invertibility criterion, the group of units and the unit-norm group are read from it; the derivations are *The $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*.

**The assignment is forced, not chosen.** $\vec e_k^2 = -e_t$ requires the factor $i$ and $\vec e_x \vec e_y = \vec e_z$ fixes the sign, so neither the factor nor the sign in the three vector images could have been otherwise. A reviewer must not "correct" the assignment by making the three images real, nor by negating all three. *The $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* derives both.

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

**The four unit matrices.** The left images of the four units are
$$
\mathsf{M}_4^{L}(e_t)=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
\mathsf{M}_4^{L}(\vec e_x)=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix},
$$
$$
\mathsf{M}_4^{L}(\vec e_y)=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\qquad
\mathsf{M}_4^{L}(\vec e_z)=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix}.
$$
Each is $I_2\otimes\mathsf{M}_2(\vec e_k)$ with the $2\times2$ images of §*The 2×2 Matrix Representation*, and a general element is the linear combination
$$
\mathsf{M}_4^{L}(\tilde Q)=Q_t\,\mathsf{M}_4^{L}(e_t)+Q_x\,\mathsf{M}_4^{L}(\vec e_x)+Q_y\,\mathsf{M}_4^{L}(\vec e_y)+Q_z\,\mathsf{M}_4^{L}(\vec e_z).
$$

**The gamma frame.** The five Dirac generators are two-sided operators of the frame, built from the left and right multiplications $L_{\tilde Q}$ and $R_{\tilde Q}$ of *Conventions of the Operators and the Calculus*, §*The Operators*: the left factor is a unit and the right factor a spatial unit,
$$
\gamma^0=iR_{\vec e_x},\qquad
\gamma^1=iL_{\vec e_x}R_{\vec e_y},\qquad
\gamma^2=iL_{\vec e_y}R_{\vec e_y},\qquad
\gamma^3=iL_{\vec e_z}R_{\vec e_y},\qquad
\gamma_5=-iR_{\vec e_z}.
$$
In the canonical frame they are the Dirac matrices
$$
\gamma^0=\begin{pmatrix}0&0&1&0\\0&0&0&1\\1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
\gamma^1=\begin{pmatrix}0&0&0&1\\0&0&1&0\\0&-1&0&0\\-1&0&0&0\end{pmatrix},
$$
$$
\gamma^2=\begin{pmatrix}0&0&0&-i\\0&0&i&0\\0&i&0&0\\-i&0&0&0\end{pmatrix},\qquad
\gamma^3=\begin{pmatrix}0&0&1&0\\0&0&0&-1\\-1&0&0&0\\0&1&0&0\end{pmatrix},\qquad
\gamma_5=\begin{pmatrix}-1&0&0&0\\0&-1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}.
$$
They obey the Clifford relations and the chirality identity
$$
\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I_4,\qquad
(\gamma^0)^2=I_4,\quad(\gamma^k)^2=-I_4,\qquad
\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3,\qquad
\gamma_5\gamma^\mu=-\gamma^\mu\gamma_5 .
$$

**The sixteen products are the sixteen cells.** With $\mu,\nu\in\{t,x,y,z\}$ the cell is the two-sided operator $L_{e_\mu}R_{e_\nu}$, left multiplication by $e_\mu$ followed by right multiplication by $e_\nu$. The sixteen products of the gamma frame are these cells, each with a coefficient of unit modulus:

| grade | $\gamma$-product | cell $L_{e_\mu}R_{e_\nu}$ | cell in the $\gamma$'s |
|---|---|---|---|
| $0$ | $1$ | $L_{e_t}R_{e_t}$ | $L_{e_t}R_{e_t}=1$ |
| $1$ | $\gamma^0$ | $L_{e_t}R_{e_x}$ | $L_{e_t}R_{e_x}=-i\gamma^0$ |
| $1$ | $\gamma^1$ | $L_{e_x}R_{e_y}$ | $L_{e_x}R_{e_y}=-i\gamma^1$ |
| $1$ | $\gamma^2$ | $L_{e_y}R_{e_y}$ | $L_{e_y}R_{e_y}=-i\gamma^2$ |
| $1$ | $\gamma^3$ | $L_{e_z}R_{e_y}$ | $L_{e_z}R_{e_y}=-i\gamma^3$ |
| $2$ | $\gamma^0\gamma^1$ | $L_{e_x}R_{e_z}$ | $L_{e_x}R_{e_z}=\gamma^0\gamma^1$ |
| $2$ | $\gamma^0\gamma^2$ | $L_{e_y}R_{e_z}$ | $L_{e_y}R_{e_z}=\gamma^0\gamma^2$ |
| $2$ | $\gamma^0\gamma^3$ | $L_{e_z}R_{e_z}$ | $L_{e_z}R_{e_z}=\gamma^0\gamma^3$ |
| $2$ | $\gamma^1\gamma^2$ | $L_{e_z}R_{e_t}$ | $L_{e_z}R_{e_t}=\gamma^1\gamma^2$ |
| $2$ | $\gamma^1\gamma^3$ | $L_{e_y}R_{e_t}$ | $L_{e_y}R_{e_t}=-\gamma^1\gamma^3$ |
| $2$ | $\gamma^2\gamma^3$ | $L_{e_x}R_{e_t}$ | $L_{e_x}R_{e_t}=\gamma^2\gamma^3$ |
| $3$ | $\gamma^0\gamma^1\gamma^2$ | $L_{e_z}R_{e_x}$ | $L_{e_z}R_{e_x}=-i\gamma^0\gamma^1\gamma^2$ |
| $3$ | $\gamma^0\gamma^1\gamma^3$ | $L_{e_y}R_{e_x}$ | $L_{e_y}R_{e_x}=i\gamma^0\gamma^1\gamma^3$ |
| $3$ | $\gamma^0\gamma^2\gamma^3$ | $L_{e_x}R_{e_x}$ | $L_{e_x}R_{e_x}=-i\gamma^0\gamma^2\gamma^3$ |
| $3$ | $\gamma^1\gamma^2\gamma^3$ | $L_{e_t}R_{e_y}$ | $L_{e_t}R_{e_y}=i\gamma^1\gamma^2\gamma^3$ |
| $4$ | $\gamma^0\gamma^1\gamma^2\gamma^3$ | $L_{e_t}R_{e_z}$ | $L_{e_t}R_{e_z}=i\gamma_5=-\gamma^0\gamma^1\gamma^2\gamma^3$ |

Read a row from the left: the product is $c$ times the cell, with $c\in\{1,-1,i,-i\}$. Read it from the right: the cell is $\bar c$ times the product. The last row is the pseudoscalar, $\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3=-iL_{e_t}R_{e_z}$. The cells are labelled by the frame units, not by spacetime indices: $L_{e_\mu}R_{e_\nu}$ with $\mu,\nu\in\{t,x,y,z\}$ is not the stress–energy tensor $T_{\mu\nu}$ of the physics articles. The full table, with the proof and the choice of frame, is §*A Gamma Frame, and the Choice Behind It* of *$M_4(\mathbb{C})$ Representation : The Two-Sided Operators on the Biquaternion Algebra* in the mathematics corpus.

**The invariants.** With $\det\mathsf{M}_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ and $\operatorname{tr}\mathsf{M}_2(\tilde Q)=2Q_t$,
$$
\det\mathsf{M}_4^{L}(\tilde Q)=\det\mathsf{M}_4^{R}(\tilde Q)=\langle\tilde Q\rangle_{\natural}^{2},
\qquad
\operatorname{tr}\mathsf{M}_4^{L}(\tilde Q)=\operatorname{tr}\mathsf{M}_4^{R}(\tilde Q)=4\,\mathrm{Sc}(\tilde Q).
$$
The determinant is the square of the biquaternion norm and the trace is four times the scalar part; both are properties of the element, read in the regular representation. The explicit frame, the product, the determinant and the volume identity are *The General Quaternionic Algebra in the $4\times4$ Left Regular Representation* in the mathematics corpus, and the operator reading is *The Element and Operator Representations*.

**No entry is read without the frame.** Another gauge or another order of the four basis elements gives another matrix of the same operator; the block formula holds in the canonical frame alone. The explicit matrices of the mathematics model articles are in the coefficient basis, and $S$ carries them to the canonical frame; the physics articles use the canonical frame. The copy and the element are what the frame does not change.

### The Clifford Map

**The Clifford map is $\iota_{\mathrm{Cl}}$, and it is not a regular matrix.** The articles on the Dirac algebra identify the biquaternion algebra with the even subalgebra of $\mathrm{Cl}_{1,3}$ by

$$
\iota_{\mathrm{Cl}}(e_t)=I_4,\qquad
\iota_{\mathrm{Cl}}(\vec e_x)=\gamma^2\gamma^3,\qquad
\iota_{\mathrm{Cl}}(\vec e_y)=\gamma^3\gamma^1,\qquad
\iota_{\mathrm{Cl}}(\vec e_z)=\gamma^1\gamma^2,\qquad
\iota_{\mathrm{Cl}}(i)=-\gamma^0\gamma^1\gamma^2\gamma^3 .
$$
The five generators are the matrices of §*The 4×4 Matrix Representation*, read in the same frame.

The two are different objects: $\mathsf{M}_4^{L}$ is the matrix of left multiplication on $\mathbb{B}$, in the canonical frame, while $\iota_{\mathrm{Cl}}$ identifies $\mathbb{B}$ with the even subalgebra of $\mathrm{Cl}_{1,3}$. Their images are both $4\times4$ matrices, and that is all they share. A bare $\mathsf{M}_4$ is written for neither. The regular matrices carry $L$ or $R$, and the Clifford map carries $\iota_{\mathrm{Cl}}$; the dictionary is *The Dirac Algebra and Biquaternions — A Dictionary*.

## Summary

The $2\times2$ isomorphism $\mathsf{M}_2$ is fixed by four images: $e_t\mapsto I_2$, and the three vector units to $-i$ times the Pauli matrices, with $\mathsf{M}_2(i)=iI_2$ on the central scalar. The assignment is forced by $\vec e_k^2=-e_t$ and by $\vec e_x\vec e_y=\vec e_z$. The trace is twice the scalar part, the determinant is the biquaternion norm, and conjugating entries on their own is not an involution of the algebra. A bare $\mathsf{M}_2$ names this isomorphism and nothing else, and the realisation is fixed up to a star-unitary change of basis and a central scalar.

The $4\times4$ representation is the regular one, $\rho_L$ and $\rho_R$, and its image is a four-dimensional subalgebra of the ambient $M_4(\mathbb{C})$, not the ambient algebra. In the canonical Peirce frame the left matrix is $I_2\otimes\mathsf{M}_2(\tilde Q)$ and the right is $\mathsf{M}_2(\tilde Q)^{\mathsf T}\otimes I_2$. The four unit matrices are written out, the five gamma matrices are two-sided operators of that frame, and their sixteen products are the sixteen cells $L_{e_\mu}R_{e_\nu}$, each with a coefficient of unit modulus. The determinant is the square of the norm and the trace is four times the scalar part. No entry is read without its frame, and no frame changes the element or the copy.

The Clifford map $\iota_{\mathrm{Cl}}$ identifies the algebra with the even subalgebra of $\mathrm{Cl}_{1,3}$. It is not a regular matrix, and the two share only the size of their images.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ | The isomorphism of the element; $\mathsf{M}_2(e_t)=I_2$, $\mathsf{M}_2(\vec e_k)=-i\sigma_k$ |
| $\operatorname{Tr}\tilde Q=\operatorname{tr}\mathsf{M}_2(\tilde Q)$ | The trace, twice the scalar part |
| $\det\mathsf{M}_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ | The determinant, the biquaternion norm |
| $\rho_L,\rho_R$ | Left and right multiplication as linear maps, $\rho_L(\tilde Q_1)(\tilde Q_2)=\tilde Q_1\tilde Q_2$, $\rho_R(\tilde Q_1)(\tilde Q_2)=\tilde Q_2\tilde Q_1$ |
| $\mathbb{B}_L=M_4(\mathbb{C})_{\mathbb{B},L}$ | The left copy, $\rho_L(\mathbb{B})$; $\mathbb{B}_R$ is its commutant |
| $\mathsf{M}_4^{L}(\tilde Q)=I_2\otimes\mathsf{M}_2(\tilde Q)$ | The regular matrix in the canonical frame |
| $\gamma^0,\dots,\gamma^3,\gamma_5$ | The five Dirac generators of the canonical frame |
| $\iota_{\mathrm{Cl}}$ | The identification with the even subalgebra of $\mathrm{Cl}_{1,3}$; not a regular matrix |

## Further Reading

- [Conventions in the Biquaternion Universe](conventions-in-the-biquaternion-universe.html), for the algebra and the element glyphs.
- [Conventions of the Products and the Forms](conventions-of-the-products-and-the-forms.html), for the products the matrix product mirrors.
- [Conventions of the Operators and the Calculus](conventions-of-the-operators-and-the-calculus.html), for the left and right multiplications these matrices represent.
- [Element and Operator Representations: The Three Actions](the-element-and-operator-representations.html), companion article, for the coefficient space and the three actions.
- [$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant](../articles_maths/m4c-model-the-product-the-trace-and-the-determinant.html), for the change of frame between the coefficient basis and the canonical frame.
- [The Dirac Algebra and Biquaternions — A Dictionary](the-dirac-algebra-and-biquaternions-a-dictionary.html), for the Clifford map.
