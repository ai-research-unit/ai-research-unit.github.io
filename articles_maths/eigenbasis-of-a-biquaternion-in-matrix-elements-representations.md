# __Eigenbasis of a Biquaternion in Matrix Elements Representations__

## Introduction

The eigenbasis of a biquaternion $\tilde Q=Q_te_t+\vec Q$ is the basis
$$
\tilde\Pi_+,\qquad \vec\Upsilon_-,\qquad \vec\Upsilon_+,\qquad \tilde\Pi_-
$$
of the Q-adapted Peirce decomposition, in which multiplication by $\tilde Q$ is diagonal with eigenvalues $\lambda_+,\lambda_+,\lambda_-,\lambda_-$. The basis itself, the construction of the nilpotents $\vec\Upsilon_\pm$ from the two mixed Peirce corners, and the eigenvalue decomposition are the subject of *Eigenbasis of a Biquaternion*. This article reads the same objects in the two matrix element representations of the algebra.

The first is the **$2\times2$ matrix element representation** $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$, the fixed isomorphism of *Introduction to the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*. Every biquaternion becomes a $2\times2$ complex matrix, the two minimal left ideals become the two columns, and the eigenbasis becomes a basis of matrix units. The second is the **$4\times4$ left regular representation** $\mathsf{M}_4^{L}:\mathbb{B}\to M_4(\mathbb{C})$ of *Introduction to the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*, with its right companion $\mathsf{M}_4^{R}$. The $4\times4$ matrices carry the multiplication on the four-vector space; in the Q-adapted order they are Kronecker products of the $2\times2$ matrix with an identity.

The article is organised around three questions. **Which matrices are the eigenprojections and the nilpotents?** They are the spectral projectors $\rho_\pm=\mathsf{M}_2(\tilde\Pi_\pm)$ and the two off-diagonal matrix units, and the Q-adapted model $\mathsf{M}_2^{Q}$ is the map that sends them to the four matrix units. **What does a change of basis do?** The fixed model, the eigenbasis of the standard root $i\vec e_z$, and the Q-adapted eigenbasis are three bases of the same four-dimensional space; the passage between them is a conjugation, and the diagonalising matrix $\mathsf{C}_Q$ is determined by the eigenvectors up to the rescaling of the nilpotents. **What happens in the $4\times4$ representation?** The left and right regular matrices are block matrices built from the $2\times2$ Peirce matrix, and the Q-adapted order diagonalises both.

| Question | Answer |
|---|---|
| $2\times2$ model | $\mathsf{M}_2(\tilde Q)=\begin{pmatrix}Q_t-iQ_z&-iQ_x-Q_y\\-iQ_x+Q_y&Q_t+iQ_z\end{pmatrix}$ |
| Eigenprojections | $\rho_\pm=\mathsf{M}_2(\tilde\Pi_\pm)$, rank-one spectral projectors of $\mathsf{M}_2(\tilde Q)$ |
| Nilpotents | $\mathsf{M}_2(\vec\Upsilon_-)$ and $\mathsf{M}_2(\vec\Upsilon_+)$ in the two mixed corners, square-zero |
| Q-adapted model | $\mathsf{M}_2^{Q}(\tilde Q_2)=\mathsf{C}_Q^{-1}\mathsf{M}_2(\tilde Q_2)\mathsf{C}_Q$ |
| Diagonal form | $\mathsf{M}_2^{Q}(\tilde Q)=\operatorname{diag}(\lambda_+,\lambda_-)$ |
| Base change | conjugation by $\mathsf{C}_Q$; $\mathsf{C}_Q$ unique up to the rescaling of its two columns |
| $4\times4$ left regular | $\mathsf{M}_4^{L}(\tilde Q_2)$, columns $\tilde Q_2e_\mu$ |
| $4\times4$ Q-order | $[L_{\tilde Q_2}]_{\mathrm Q}=\mathsf{M}_2^{Q}(\tilde Q_2)\otimes \mathrm I_2$, $[R_{\tilde Q_2}]_{\mathrm Q}=\mathrm I_2\otimes \mathsf{M}_2^{Q}(\tilde Q_2)^{\mathsf T}$ |
| $4\times4$ diagonal | $\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$ for $L_{\tilde Q}$ and $\operatorname{diag}(\lambda_+,\lambda_-,\lambda_+,\lambda_-)$ for $R_{\tilde Q}$ |

**Conventions.** The base and the elements are those of *Conventions in Mathematics*: $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, $B=\sqrt{Q_x^2+Q_y^2+Q_z^2}$, $\vec\Xi=-i\vec Q/B$, $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$, $\lambda_\pm=Q_t\pm iB$. A general element distinct from $\tilde Q$ is written $\tilde Q_2$ or $\tilde Q_3$. The fixed $2\times2$ model is $\mathsf{M}_2$; the Q-adapted model is $\mathsf{M}_2^{Q}$; the regular matrices are $\mathsf{M}_4^{L}$ and $\mathsf{M}_4^{R}$, with the shorter $\mathsf{M}_4=\mathsf{M}_4^{L}$. The two matrix assignments are those of the two introduction articles cited above and are not redefined here.

**Boundaries.** The eigenvalue decomposition, the Peirce decomposition and the construction of the nilpotents are *Eigenbasis of a Biquaternion*. The $2\times2$ assignment, its invertibility and its invariants are *Introduction to the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*; the $4\times4$ assignment, its multiplicativity and its remarkable subspaces are *Introduction to the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*. The matrix algebra is *Matrix Algebras*, the spectral projections of a general matrix are *The Eigenvalue Decomposition of a Matrix*, and the change of basis of an endomorphism is *Matrix Algebras*, §*Change of Basis*.

## The $2\times2$ Matrix Element Representation

**The fixed model sends the four units to four matrices and the four coefficients to a $2\times2$ complex matrix.**

The assignment is fixed by its values on the basis,
$$
\mathsf{M}_2(e_t)=\mathrm I_2,\qquad
\mathsf{M}_2(\vec e_x)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\qquad
\mathsf{M}_2(\vec e_y)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
\mathsf{M}_2(\vec e_z)=\begin{pmatrix}-i&0\\0&i\end{pmatrix},
$$
and extended by $\mathbb{C}$-linearity. A general element therefore has the matrix
$$
\mathsf{M}_2(\tilde Q_2)=
\begin{pmatrix}
Q_{2t}-iQ_{2z}&-iQ_{2x}-Q_{2y}\\
-iQ_{2x}+Q_{2y}&Q_{2t}+iQ_{2z}
\end{pmatrix}.
$$
The map is an isomorphism of $\mathbb{C}$-algebras, so products, inverses, powers and conjugates are read in the matrices without loss. The inverse map is
$$
\mathsf{M}_2^{-1}:\begin{pmatrix}a&b\\c&d\end{pmatrix}\longmapsto
Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,
\qquad
Q_t=\tfrac{a+d}{2},\quad
Q_x=\tfrac{i(b+c)}{2},\quad
Q_y=\tfrac{c-b}{2},\quad
Q_z=\tfrac{i(a-d)}{2}.
$$
The invariants are
$$
\operatorname{tr}\mathsf{M}_2(\tilde Q_2)=2Q_{2t},\qquad
\det\mathsf{M}_2(\tilde Q_2)=\langle\tilde Q_2\rangle_{\natural}=Q_{2t}^2+Q_{2x}^2+Q_{2y}^2+Q_{2z}^2.
$$
The four basis matrices are collected in the table.

| Element | Matrix $\mathsf{M}_2$ | Square | Determinant |
|---|---|---|---|
| $e_t$ | $\mathrm I_2$ | $\mathrm I_2$ | $1$ |
| $\vec e_x$ | $\begin{pmatrix}0&-i\\-i&0\end{pmatrix}$ | $-\mathrm I_2$ | $1$ |
| $\vec e_y$ | $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ | $-\mathrm I_2$ | $1$ |
| $\vec e_z$ | $\begin{pmatrix}-i&0\\0&i\end{pmatrix}$ | $-\mathrm I_2$ | $1$ |

**A general element is not a matrix unit.** The entries of $\mathsf{M}_2(\tilde Q_2)$ are linear combinations of two coefficients each, so the four matrix entries and the four biquaternion coefficients carry the same data in two different arrangements. The arrangement is fixed and is not a choice of basis: it is the assignment above. A different isomorphism differs from this one by conjugation by an invertible matrix, which is the subject of §*Base Changes*.

**The image of the algebra is everything.** Since $\mathbb{B}$ and $M_2(\mathbb{C})$ have complex dimension four and $\mathsf{M}_2$ is injective, the image is the whole of $M_2(\mathbb{C})$. This is the structural difference with the split-complex and reduced biquaternion cases, where the image is a proper commutative subalgebra. The whole matrix algebra is available: every $2\times2$ complex matrix is a biquaternion, and every matrix identity is a biquaternion identity.

## The Eigenprojections in the Model

**The eigenprojections become the spectral projectors of the matrix, and the two eigenvalues become its two diagonal entries in the eigenbasis.**

For the standard root $\vec\Xi_0=i\vec e_z$ the idempotents are $\tilde\Pi_{\pm,0}=\tfrac12(e_t\pm i\vec e_z)$, and their matrices are the two diagonal matrix units:
$$
\rho_+^{(0)}=\mathsf{M}_2(\tilde\Pi_{+,0})=\begin{pmatrix}1&0\\0&0\end{pmatrix}=E_{11},
\qquad
\rho_-^{(0)}=\mathsf{M}_2(\tilde\Pi_{-,0})=\begin{pmatrix}0&0\\0&1\end{pmatrix}=E_{22}.
$$
For a general element, with $\vec\Xi=-i\vec Q/B$,
$$
\rho_\pm=\mathsf{M}_2(\tilde\Pi_\pm)=\frac{1}{2}\left(\mathrm I_2\pm\mathsf{M}_2(\vec\Xi)\right),
\qquad
\mathsf{M}_2(\vec\Xi)=\frac{1}{B}
\begin{pmatrix}
-Q_z&-Q_x+iQ_y\\
-Q_x-iQ_y&Q_z
\end{pmatrix}.
$$
Written out,
$$
\rho_+=\frac{1}{2B}
\begin{pmatrix}
B-Q_z&-Q_x+iQ_y\\
-Q_x-iQ_y&B+Q_z
\end{pmatrix},
\qquad
\rho_-=\frac{1}{2B}
\begin{pmatrix}
B+Q_z&Q_x-iQ_y\\
Q_x+iQ_y&B-Q_z
\end{pmatrix}.
$$
The two matrices are the **spectral projectors** of $\mathsf{M}_2(\tilde Q)$:
$$
\rho_\pm^2=\rho_\pm,\qquad
\rho_+\rho_-=\rho_-\rho_+=0,\qquad
\rho_++\rho_-=\mathrm I_2,\qquad
\operatorname{tr}\rho_\pm=1,\qquad
\mathsf{M}_2(\tilde Q)\rho_\pm=\lambda_\pm\rho_\pm.
$$
Each has rank one; its image is the line of the corresponding eigenvector. The columns of $\rho_+$ are eigenvectors of eigenvalue $\lambda_+$, and the columns of $\rho_-$ eigenvectors of eigenvalue $\lambda_-$. Every nonzero column is one, and the two columns of one projector are proportional.

**The nilpotents in the model.** The symmetric closed form of *Eigenbasis of a Biquaternion*, §*The Peirce Corners and the Nilpotents*, is, with $\Sigma=Q_x+Q_y+Q_z$,
$$
\vec\Upsilon_\pm=\frac{B\,\vec w-\dfrac{\Sigma}{B}\,\vec Q\pm\dfrac{i}{2}\,[\vec Q,\vec w]}{2\sqrt{\Sigma^2-3B^2}},
\qquad \vec w=\vec e_x+\vec e_y+\vec e_z,
$$
and its image is
$$
\mathsf{M}_2(\vec\Upsilon_\pm)=\frac{N_\pm}{2\sqrt{\Sigma^2-3B^2}},
$$
where
$$
N_\pm=
\begin{pmatrix}
i\left(\dfrac{\Sigma Q_z}{B}-B\right)\pm(Q_x-Q_y)
&
-B(1+i)+\dfrac{\Sigma}{B}(iQ_x+Q_y)\pm\bigl[(Q_y-Q_z)-i(Q_z-Q_x)\bigr]\\[6pt]
B(1-i)+\dfrac{\Sigma}{B}(iQ_x-Q_y)\pm\bigl[(Q_y-Q_z)+i(Q_z-Q_x)\bigr]
&
-i\left(\dfrac{\Sigma Q_z}{B}-B\right)\mp(Q_x-Q_y)
\end{pmatrix}.
$$
Both matrices are rank one and trace zero, and
$$
\mathsf{M}_2(\vec\Upsilon_+)\mathsf{M}_2(\vec\Upsilon_-)=\rho_-,\qquad
\mathsf{M}_2(\vec\Upsilon_-)\mathsf{M}_2(\vec\Upsilon_+)=\rho_+,\qquad
\mathsf{M}_2(\vec\Upsilon_\pm)^2=0,
$$
with
$$
\rho_+\mathsf{M}_2(\vec\Upsilon_-)\rho_-=\mathsf{M}_2(\vec\Upsilon_-),\qquad
\rho_-\mathsf{M}_2(\vec\Upsilon_+)\rho_+=\mathsf{M}_2(\vec\Upsilon_+).
$$
The entries are not symmetric in $x,y,z$ even though the elements are, because the fixed model $\mathsf{M}_2$ itself singles out $\vec e_z$: it is the representation in which $\mathsf{M}_2(\vec e_z)$ is diagonal. The symmetric formula is a statement in the algebra; its matrix image inherits the asymmetry of the representation.

The four basis elements of the Q-adapted basis therefore have the following matrices in the fixed model.

| Element | $\mathsf{M}_2$ | Rank | Square |
|---|---|---|---|
| $\tilde\Pi_+$ | $\dfrac{1}{2B}\begin{pmatrix}B-Q_z&-Q_x+iQ_y\\-Q_x-iQ_y&B+Q_z\end{pmatrix}$ | $1$ | itself |
| $\vec\Upsilon_-$ | $\dfrac{N_-}{2\sqrt{\Sigma^2-3B^2}}$ | $1$ | $0$ |
| $\vec\Upsilon_+$ | $\dfrac{N_+}{2\sqrt{\Sigma^2-3B^2}}$ | $1$ | $0$ |
| $\tilde\Pi_-$ | $\dfrac{1}{2B}\begin{pmatrix}B+Q_z&Q_x-iQ_y\\Q_x+iQ_y&B-Q_z\end{pmatrix}$ | $1$ | itself |

On the cone $\Sigma^2=3B^2$ the symmetric formula is singular; there the chart of *Eigenbasis of a Biquaternion*, §*The Exceptional Cone and the Chart*, applies, and the matrices are its $\mathsf{M}_2$.

**The standard case.** For $\vec Q=Q_z\vec e_z$ the matrix is diagonal, $\mathsf{M}_2(\tilde Q)=\operatorname{diag}(Q_t-iQ_z,Q_t+iQ_z)$, and the projectors are $E_{11}$ and $E_{22}$. The general formula reduces to them when the sign of $B$ is chosen so that $B=-Q_z$; the other sign exchanges the two labels. This is the sign freedom of the root, read in the model.

**The spectral reading.** The matrices $\rho_\pm$ are the images of the eigenprojections, so the eigenvalue decomposition $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ becomes
$$
\mathsf{M}_2(\tilde Q)=\lambda_+\rho_++\lambda_-\rho_-.
$$
The trace is $\lambda_++\lambda_-=2Q_t$, the determinant is $\lambda_+\lambda_-=\langle\tilde Q\rangle_{\natural}$, and the characteristic polynomial of the matrix is $(X-\lambda_+)(X-\lambda_-)$. The two facts are the matrix form of the eigenvalue decomposition of the element.

## The Q-Adapted Basis in the Model

**The four elements of the Q-adapted Peirce basis become the four matrix units, and the Peirce matrix of $\tilde Q$ becomes diagonal.**

The Q-adapted basis is
$$
\tilde\Pi_+,\qquad \vec\Upsilon_-,\qquad \vec\Upsilon_+,\qquad \tilde\Pi_-,
\qquad
\vec\Upsilon_+\in\mathbb{B}_{-+},\quad \vec\Upsilon_-\in\mathbb{B}_{+-},
$$
with the normalisation
$$
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,\qquad
\vec\Upsilon_\pm^2=0.
$$
The model $\mathsf{M}_2^{Q}$ is defined by the assignment
$$
\tilde\Pi_+\longmapsto E_{11},\qquad
\vec\Upsilon_-\longmapsto E_{12},\qquad
\vec\Upsilon_+\longmapsto E_{21},\qquad
\tilde\Pi_-\longmapsto E_{22}.
$$
It is the composition of $\mathsf{M}_2$ with the change of basis that carries the Q-adapted basis to the matrix units. Every element has a unique expansion
$$
\tilde Q_2=a_{11}\tilde\Pi_++a_{12}\vec\Upsilon_-+a_{21}\vec\Upsilon_++a_{22}\tilde\Pi_-,
\qquad a_{ij}\in\mathbb{C},
$$
and is represented by
$$
\mathsf{M}_2^{Q}(\tilde Q_2)=
\begin{pmatrix}
a_{11}&a_{12}\\
a_{21}&a_{22}
\end{pmatrix}.
$$
For $\tilde Q$ itself the coordinates are $a_{11}=\lambda_+$, $a_{22}=\lambda_-$, $a_{12}=a_{21}=0$, so
$$
\mathsf{M}_2^{Q}(\tilde Q)=
\begin{pmatrix}
\lambda_+&0\\
0&\lambda_-
\end{pmatrix}.
$$
The four basis elements and the general element are collected in the table.

| Element | Coordinates in the Q-adapted basis | Matrix $\mathsf{M}_2^{Q}$ |
|---|---|---|
| $\tilde\Pi_+$ | $(1,0,0,0)$ | $E_{11}$ |
| $\vec\Upsilon_-$ | $(0,1,0,0)$ | $E_{12}$ |
| $\vec\Upsilon_+$ | $(0,0,1,0)$ | $E_{21}$ |
| $\tilde\Pi_-$ | $(0,0,0,1)$ | $E_{22}$ |
| $e_t$ | $(1,0,0,1)$ | $\mathrm I_2$ |
| $\tilde Q$ | $(\lambda_+,0,0,\lambda_-)$ | $\operatorname{diag}(\lambda_+,\lambda_-)$ |
| $\tilde Q_2$ | $(a_{11},a_{12},a_{21},a_{22})$ | $\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}$ |

**The algebra in matrix form.** The Peirce identities of the eigenbasis read as the matrix-unit identities:
$$
E_{11}^2=E_{11},\qquad E_{22}^2=E_{22},\qquad E_{11}E_{22}=0,
$$
$$
E_{12}^2=0,\qquad E_{21}^2=0,\qquad E_{12}E_{21}=E_{11},\qquad E_{21}E_{12}=E_{22},
$$
together with
$$
E_{11}E_{12}=E_{12}=E_{12}E_{22},\qquad
E_{22}E_{21}=E_{21}=E_{21}E_{11}.
$$
These are the corner relations of the Peirce decomposition, read as matrix multiplication. The two diagonal units are the identity elements of the two minimal left ideals, and the two off-diagonal units are the nilpotents.

**General objects.** For two elements with matrices $A=\mathsf{M}_2^{Q}(\tilde Q_2)$ and $B=\mathsf{M}_2^{Q}(\tilde Q_3)$, the product, inverse and invariants are
$$
\mathsf{M}_2^{Q}(\tilde Q_2\tilde Q_3)=AB,\qquad
\mathsf{M}_2^{Q}(\tilde Q_2^{-1})=A^{-1}\quad(\det A\neq0),
$$
$$
\det\mathsf{M}_2^{Q}(\tilde Q_2)=a_{11}a_{22}-a_{12}a_{21}=\langle\tilde Q_2\rangle_{\natural},
\qquad
\operatorname{tr}\mathsf{M}_2^{Q}(\tilde Q_2)=a_{11}+a_{22}=2Q_{2t}.
$$
Quaternion conjugation is the adjugate,
$$
\mathsf{M}_2^{Q}(\tilde Q_2^{\natural})=
\begin{pmatrix}a_{22}&-a_{12}\\-a_{21}&a_{11}\end{pmatrix},
\qquad
\mathsf{M}_2^{Q}(\tilde Q_2\tilde Q_2^{\natural})=\langle\tilde Q_2\rangle_{\natural}\,\mathrm I_2.
$$
The identity is $\mathrm I_2$, and a power is the power of the matrix. The model is an isomorphism, so no information is lost and no relation is added: the Q-adapted basis is a choice of coordinates on the same algebra.

## Base Changes

**The fixed model, the standard eigenbasis and the Q-adapted eigenbasis are three bases of the same matrix space, and the passage between them is a conjugation by an invertible matrix.**

### The Change of Basis of a Matrix Model

Let $P\in GL_2(\mathbb{C})$ be the matrix whose columns are the coordinates of a new basis in the old one. The matrix of the same endomorphism in the new basis is
$$
M'=P^{-1}MP.
$$
The trace and the determinant are unchanged,
$$
\operatorname{tr}M'=\operatorname{tr}M,\qquad
\det M'=\det M,
$$
and so are the characteristic polynomial, the spectrum, the rank and the Jordan form. The idempotents and the nilpotents are not unchanged as matrices: they are conjugated,
$$
\rho\longmapsto P^{-1}\rho P,
\qquad
N\longmapsto P^{-1}NP,
$$
and they remain idempotent and square-zero respectively. The two columns of $P$ are the new basis vectors; a column of $P$ that is an eigenvector of $M$ produces a column of $P^{-1}MP$ with the eigenvalue on the diagonal.

**The two normal forms.** The fixed model and the Q-adapted model are the two ends of one change. The fixed model is $\mathsf{M}_2$; the Q-adapted model is
$$
\mathsf{M}_2^{Q}(\tilde Q_2)=\mathsf{C}_Q^{-1}\mathsf{M}_2(\tilde Q_2)\mathsf{C}_Q,
$$
where $\mathsf{C}_Q$ is the matrix whose columns are the coordinates of a $\lambda_+$-eigenvector and a $\lambda_-$-eigenvector in the fixed basis. The first column is a nonzero column of $\rho_+$ and the second a nonzero column of $\rho_-$. The matrix $\mathsf{C}_Q$ is invertible because the two columns are independent: $\rho_+\rho_-=0$ and both are nonzero.

### The Explicit Diagonalising Matrix

For $B-Q_z\neq0$ put
$$
\mathsf{C}_Q=
\begin{pmatrix}
B-Q_z&Q_x-iQ_y\\
-Q_x-iQ_y&B-Q_z
\end{pmatrix},
\qquad
\det\mathsf{C}_Q=-2Q_z(B-Q_z)\neq0.
$$
The first column is the first column of $2B\rho_+$, the second is the second column of $2B\rho_-$, and the two are eigenvectors of $\mathsf{M}_2(\tilde Q)$ with eigenvalues $\lambda_+$ and $\lambda_-$ respectively. Therefore
$$
\mathsf{C}_Q^{-1}\mathsf{M}_2(\tilde Q)\mathsf{C}_Q=\operatorname{diag}(\lambda_+,\lambda_-).
$$
When $Q_z=0$ or $B=Q_z$ the first formula is singular: at $B=Q_z$ one of the two chosen columns of the spectral projectors vanishes, and at $Q_z=0$ the two chosen columns are proportional. The other pair of nonzero columns gives
$$
\mathsf{C}_Q'=
\begin{pmatrix}
-Q_x+iQ_y&B+Q_z\\
B+Q_z&Q_x+iQ_y
\end{pmatrix},
\qquad
\det\mathsf{C}_Q'=-2B(B+Q_z)\neq0,
$$
with columns the second column of $2B\rho_+$ and the first column of $2B\rho_-$. It satisfies the same diagonalisation. Since $B\neq0$, the determinants $-2Q_z(B-Q_z)$ and $-2B(B+Q_z)$ cannot both vanish, so one of the two formulas applies. When $Q_x=Q_y=0$, the sign $B=-Q_z$ is the first case, $\mathsf{C}_Q=-2Q_z\,\mathrm I_2$, and the sign $B=Q_z$ is the second, $\mathsf{C}_Q'=2Q_z\begin{pmatrix}0&1\\1&0\end{pmatrix}$; both are invertible because $Q_z\neq0$ when $B\neq0$. The scalar case $B=0$ is excluded, as in the eigenbasis article. The matrix $\mathsf{C}_Q$ is not the most general diagonaliser: it is the one whose columns are the two columns of the spectral projectors.

**The inverse and the conjugation.** For the first matrix, with $D=-2Q_z(B-Q_z)$,
$$
\mathsf{C}_Q^{-1}=\frac{1}{D}
\begin{pmatrix}
B-Q_z&-(Q_x-iQ_y)\\
Q_x+iQ_y&B-Q_z
\end{pmatrix}.
$$
The second matrix has the analogous inverse. In either case the conjugation $\Phi(M)=\mathsf{C}_Q^{-1}M\mathsf{C}_Q$, with $\mathsf{C}_Q$ the chosen matrix, sends
$$
\rho_+\longmapsto E_{11},\qquad
\rho_-\longmapsto E_{22},\qquad
\mathsf{M}_2(\tilde Q)\longmapsto\operatorname{diag}(\lambda_+,\lambda_-).
$$
It sends each mixed corner onto the mixed corner with the same indices,
$$
\mathsf{M}_2(\mathbb{B}_{+-})\longmapsto\mathbb{C}E_{12},
\qquad
\mathsf{M}_2(\mathbb{B}_{-+})\longmapsto\mathbb{C}E_{21},
$$
and it is the algebra isomorphism $\mathsf{M}_2^{Q}$.

### The Nilpotents in the Change

The two nilpotents are recovered from the matrix units by the inverse conjugation:
$$
\mathsf{M}_2(\vec\Upsilon_-)=\mathsf{C}_Q E_{12}\mathsf{C}_Q^{-1},
\qquad
\mathsf{M}_2(\vec\Upsilon_+)=\mathsf{C}_Q E_{21}\mathsf{C}_Q^{-1}.
$$
They are square-zero and satisfy
$$
\mathsf{M}_2(\vec\Upsilon_+)\mathsf{M}_2(\vec\Upsilon_-)=E_{22},
\qquad
\mathsf{M}_2(\vec\Upsilon_-)\mathsf{M}_2(\vec\Upsilon_+)=E_{11}
$$
after the conjugation, which is the normalisation $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$ and $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$. The construction fixes the two matrices, not merely the corner lines: the normalisation of the pair is exactly the condition that the off-diagonal entries of the Q-adapted matrix be $1$ rather than an arbitrary nonzero scalar.

### The Freedom of the Change

The diagonalising matrix is not unique. If $\mathsf{C}_Q$ diagonalises $\mathsf{M}_2(\tilde Q)$, then so does $\mathsf{C}_Q D$ for every invertible diagonal $D=\operatorname{diag}(\alpha,\beta)$:
$$
(\mathsf{C}_Q D)^{-1}\mathsf{M}_2(\tilde Q)(\mathsf{C}_Q D)
=D^{-1}\operatorname{diag}(\lambda_+,\lambda_-)D
=\operatorname{diag}(\lambda_+,\lambda_-).
$$
The two scales are the two independent rescalings of the eigenvectors. A common scale $\alpha=\beta$ leaves the conjugation unchanged, because $(\alpha \mathsf{C}_Q)^{-1}M(\alpha \mathsf{C}_Q)=\mathsf{C}_Q^{-1}M\mathsf{C}_Q$. A relative scale multiplies the two off-diagonal entries by $\alpha^{-1}\beta$ and $\alpha\beta^{-1}$, which is the reciprocal rescaling
$$
\vec\Upsilon_+\longmapsto\mu\vec\Upsilon_+,\qquad
\vec\Upsilon_-\longmapsto\mu^{-1}\vec\Upsilon_-,\qquad
\mu\in\mathbb{C}^{\times},
$$
of the nilpotents. The normalised pair is the choice $\alpha=\beta=1$ in the chosen matrix $\mathsf{C}_Q$ above; the general diagonaliser is $\mathsf{C}_Q\operatorname{diag}(\alpha,\beta)$.

**What depends on $\tilde Q$.** The matrix $\mathsf{C}_Q$, the projectors $\rho_\pm$, the nilpotents $\mathsf{M}_2(\vec\Upsilon_\pm)$ and the diagonal matrix $\operatorname{diag}(\lambda_+,\lambda_-)$ depend on $\tilde Q$. The fixed model $\mathsf{M}_2$, the matrix units $E_{ij}$ and the assignment $\mathsf{M}_2^{Q}$ as a map from the Q-adapted basis do not: they are the same for every $\tilde Q$ for which the construction exists. The dependence is carried by the basis, not by the algebra.

### Changing from One Element to Another

For two elements $\tilde Q$ and $\tilde Q'$ with distinct eigenvalues, the two Q-adapted bases are related by a further change of basis,
$$
\mathsf{C}_{Q'}=\mathsf{C}_Q\,\mathsf{D}_{Q,Q'},
$$
where $\mathsf{D}_{Q,Q'}$ is the matrix of the Q'-adapted basis in the Q-adapted basis. The matrix $\mathsf{D}_{Q,Q'}$ is generally full, not diagonal, because the two bases have different idempotents and different nilpotents. The composite change satisfies the cocycle relation
$$
\mathsf{D}_{Q,Q''}=\mathsf{D}_{Q,Q'}\mathsf{D}_{Q',Q''},
$$
and the eigenvalues are unchanged by it. This is the matrix form of the fact that the eigenbasis is attached to the element: there is no single eigenbasis of the whole algebra.

**The standard eigenbasis as a special case.** For $\tilde Q'$ commuting with $\vec e_z$, the Q'-adapted basis is the standard one up to the exchange of the two labels and the reciprocal rescaling, and $\mathsf{C}_{Q'}$ is the fixed matrix of §*The Fixed Change in the $4\times4$ Model*, composed with the exchange when the labels are exchanged. The general $\mathsf{C}_Q$ reduces to it when $Q_x=Q_y=0$ with the sign of $B$ chosen so that the root is $\pm i\vec e_z$. The reduction is the statement that the standard idempotents are the Q-adapted idempotents of the elements on the $e_z$ axis, up to the exchange.

## Spinors and the Columns

**The two columns of the $2\times2$ model are the two minimal left ideals, and a spinor is a column.**

The matrices with zero second column are the image of $S_+=\mathbb{B}\tilde\Pi_+$, and the matrices with zero first column are the image of $S_-=\mathbb{B}\tilde\Pi_-$:
$$
S_+\longleftrightarrow\left\{\begin{pmatrix}a&0\\b&0\end{pmatrix}:a,b\in\mathbb{C}\right\},
\qquad
S_-\longleftrightarrow\left\{\begin{pmatrix}0&c\\0&d\end{pmatrix}:c,d\in\mathbb{C}\right\}.
$$
A spinor of first chirality is an element of $S_+$,
$$
\xi_+=\alpha\tilde\Pi_++\beta\vec\Upsilon_+,
$$
and is represented by the first column, that is, by the matrix
$$
\xi_+\longleftrightarrow
\begin{pmatrix}\alpha&0\\ \beta&0\end{pmatrix},
\qquad
\xi_+\longleftrightarrow
\begin{pmatrix}\alpha\\ \beta\end{pmatrix}
\text{ in column }1.
$$
A spinor of second chirality is an element of $S_-$,
$$
\xi_-=\gamma\vec\Upsilon_-+\delta\tilde\Pi_-,
$$
and is represented by the second column,
$$
\xi_-\longleftrightarrow
\begin{pmatrix}0&\gamma\\ 0&\delta\end{pmatrix},
\qquad
\xi_-\longleftrightarrow
\begin{pmatrix}\gamma\\ \delta\end{pmatrix}
\text{ in column }2.
$$
The two spinor spaces and the column correspondence are collected in the table.

| Spinor space | Eigenbasis | Spinor | Coordinates | Matrix representative |
|---|---|---|---|---|
| $S_+=\mathbb{B}\tilde\Pi_+$ | $(\tilde\Pi_+,\vec\Upsilon_+)$ | $\alpha\tilde\Pi_++\beta\vec\Upsilon_+$ | $(\alpha,\beta)$ | $\begin{pmatrix}\alpha&0\\ \beta&0\end{pmatrix}$ |
| $S_-=\mathbb{B}\tilde\Pi_-$ | $(\vec\Upsilon_-,\tilde\Pi_-)$ | $\gamma\vec\Upsilon_-+\delta\tilde\Pi_-$ | $(\gamma,\delta)$ | $\begin{pmatrix}0&\gamma\\ 0&\delta\end{pmatrix}$ |

Under left multiplication by $\tilde Q$ the matrix is multiplied on the left by $\operatorname{diag}(\lambda_+,\lambda_-)$:
$$
\tilde Q\xi_+\longleftrightarrow
\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}
\begin{pmatrix}\alpha\\ \beta\end{pmatrix}
\text{ in column }1,
\qquad
\tilde Q\xi_-\longleftrightarrow
\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}
\begin{pmatrix}\gamma\\ \delta\end{pmatrix}
\text{ in column }2.
$$
The same matrix acts on both columns. This is the precise sense in which the two spinor spaces are two copies of the same module.

**Right multiplication and the rows.** Right multiplication by $\tilde Q$ sends $\mathsf{M}_2^{Q}(\tilde Q_2)$ to $\mathsf{M}_2^{Q}(\tilde Q_2)\operatorname{diag}(\lambda_+,\lambda_-)$; it scales the first column by $\lambda_+$ and the second by $\lambda_-$. The two rows are the two minimal right ideals: the first row is $\tilde\Pi_+\mathbb{B}$, the second is $\tilde\Pi_-\mathbb{B}$. Left multiplication scales the first row by $\lambda_+$ and the second by $\lambda_-$. The rows and the columns are the two-sided Peirce structure read in the matrix.

## The $4\times4$ Matrix Element Representation

**The left and right regular matrices carry the multiplication on the four-vector space, and in the Q-adapted order they are Kronecker products of the $2\times2$ Peirce matrix with an identity.**

### The Regular Matrices

In the fixed basis $e_t,\vec e_x,\vec e_y,\vec e_z$, the **left regular matrix** $\mathsf{M}_4^{L}(\tilde Q_2)$ has as $\mu$-th column the coordinate column of $\tilde Q_2e_\mu$:
$$
\mathsf{M}_4^{L}(\tilde Q_2)=
\begin{pmatrix}
Q_{2t}&-Q_{2x}&-Q_{2y}&-Q_{2z}\\
Q_{2x}&Q_{2t}&-Q_{2z}&Q_{2y}\\
Q_{2y}&Q_{2z}&Q_{2t}&-Q_{2x}\\
Q_{2z}&-Q_{2y}&Q_{2x}&Q_{2t}
\end{pmatrix}.
$$
The **right regular matrix** $\mathsf{M}_4^{R}(\tilde Q_2)$ has as $\mu$-th column the coordinate column of $e_\mu\tilde Q_2$:
$$
\mathsf{M}_4^{R}(\tilde Q_2)=
\begin{pmatrix}
Q_{2t}&-Q_{2x}&-Q_{2y}&-Q_{2z}\\
Q_{2x}&Q_{2t}&Q_{2z}&-Q_{2y}\\
Q_{2y}&-Q_{2z}&Q_{2t}&Q_{2x}\\
Q_{2z}&Q_{2y}&-Q_{2x}&Q_{2t}
\end{pmatrix}.
$$
They satisfy
$$
\mathsf{M}_4^{L}(\tilde Q_2)\mathsf{M}_4^{L}(\tilde Q_3)=\mathsf{M}_4^{L}(\tilde Q_2\tilde Q_3),
\qquad
\mathsf{M}_4^{R}(\tilde Q_2)\mathsf{M}_4^{R}(\tilde Q_3)=\mathsf{M}_4^{R}(\tilde Q_3\tilde Q_2),
$$
and
$$
\operatorname{Tr}\mathsf{M}_4^{L}(\tilde Q_2)=4Q_{2t},
\qquad
\det\mathsf{M}_4^{L}(\tilde Q_2)=\langle\tilde Q_2\rangle_{\natural}^2.
$$
The left matrix is multiplicative and the right matrix is anti-multiplicative; both are injective, and the left one alone is the regular representation of the algebra.

### The Q-Adapted Order

Write $M=\mathsf{M}_2^{Q}(\tilde Q_2)$. In the Q-adapted order
$$
(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)
$$
the two regular matrices are block matrices:
$$
[L_{\tilde Q_2}]_{\mathrm Q}=
\begin{pmatrix}
a_{11}&0&a_{12}&0\\
0&a_{11}&0&a_{12}\\
a_{21}&0&a_{22}&0\\
0&a_{21}&0&a_{22}
\end{pmatrix}
=M\otimes\mathrm I_2,
$$
$$
[R_{\tilde Q_2}]_{\mathrm Q}=
\begin{pmatrix}
a_{11}&a_{21}&0&0\\
a_{12}&a_{22}&0&0\\
0&0&a_{11}&a_{21}\\
0&0&a_{12}&a_{22}
\end{pmatrix}
=\mathrm I_2\otimes M^{\mathsf T}.
$$
In this order the two blocks of two coordinates are the two minimal right ideals $\tilde\Pi_+\mathbb{B}$ and $\tilde\Pi_-\mathbb{B}$. Left multiplication acts on each block by $M$, which is the block form $M\otimes\mathrm I_2$; right multiplication preserves each block and acts on it by $M^{\mathsf T}$, which is the block form $\mathrm I_2\otimes M^{\mathsf T}$. The two blocks are the rows of the $2\times2$ model, and the correspondence between the rows and the right ideals is the one stated in §*The Eigenbasis of Left Multiplication*.

In the column order
$$
(\tilde\Pi_+,\vec\Upsilon_+\,;\,\vec\Upsilon_-,\tilde\Pi_-),
$$
which groups the two vectors of $S_+$ and then the two of $S_-$, the left matrix is block diagonal and the right matrix is not:
$$
[L_{\tilde Q_2}]_{\mathrm{col}}=
\begin{pmatrix}M&0\\0&M\end{pmatrix}
=\mathrm I_2\otimes M,
\qquad
[R_{\tilde Q_2}]_{\mathrm{col}}=
\begin{pmatrix}
a_{11}\mathrm I_2&a_{21}\mathrm I_2\\
a_{12}\mathrm I_2&a_{22}\mathrm I_2
\end{pmatrix}
=M^{\mathsf T}\otimes\mathrm I_2.
$$
Left multiplication preserves each left ideal $S_\pm$ and acts on each by $M$, so $[L]_{\mathrm{col}}$ is block diagonal. Right multiplication does not preserve the left ideals; it mixes $S_+$ and $S_-$ according to the entries of $M$, so $[R]_{\mathrm{col}}$ is not block diagonal. The two orders differ by the permutation of the second and third basis vectors. In the Q-adapted order the blocks are the right ideals and the right matrix is block diagonal; in the column order the blocks are the left ideals and the left matrix is block diagonal. The two block forms record the right-ideal decomposition $\mathbb{B}=\tilde\Pi_+\mathbb{B}\oplus\tilde\Pi_-\mathbb{B}$ and the left-ideal decomposition $\mathbb{B}=S_+\oplus S_-$, which are different groupings of the same four basis vectors.

### The Diagonal Form

For $\tilde Q_2=\tilde Q$ the Peirce matrix is $M=\operatorname{diag}(\lambda_+,\lambda_-)$, and the two regular matrices become diagonal:
$$
[L_{\tilde Q}]_{\mathrm Q}=\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-),
\qquad
[R_{\tilde Q}]_{\mathrm Q}=\operatorname{diag}(\lambda_+,\lambda_-,\lambda_+,\lambda_-).
$$
These are the matrices of the eigenbasis of left multiplication and of right multiplication of *Eigenbasis of a Biquaternion*, read in the $4\times4$ representation. The eigenvalues of $L_{\tilde Q}$ are $\lambda_+,\lambda_+,\lambda_-,\lambda_-$; the eigenvalues of $R_{\tilde Q}$ are $\lambda_+,\lambda_-,\lambda_+,\lambda_-$. The two multiplicities are the dimensions of the two spinor spaces.

**The trace and the determinant in the diagonal form.** The trace of $L_{\tilde Q}$ is $2(\lambda_++\lambda_-)=4Q_t$, the trace of $R_{\tilde Q}$ is the same, the determinant of $L_{\tilde Q}$ is $\lambda_+^2\lambda_-^2=\langle\tilde Q\rangle_{\natural}^2$, and the determinant of $R_{\tilde Q}$ is the same product in the other order. The two matrices have the same characteristic polynomial,
$$
(X-\lambda_+)^2(X-\lambda_-)^2,
$$
which is the square of the characteristic polynomial of $\mathsf{M}_2(\tilde Q)$. The doubling is the doubling of the module: the regular representation is two copies of the $2\times2$ one.

### The Fixed Change in the $4\times4$ Model

The Q-adapted order is reached from the fixed basis by the change-of-basis matrix whose columns are the coordinates of $\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-$ in the fixed basis. For the standard root $i\vec e_z$ and the standard nilpotents of the fixed model, this matrix is
$$
\mathsf{C}_4^{(0)}=
\begin{pmatrix}
\tfrac12&0&0&\tfrac12\\
0&\tfrac{i}{2}&\tfrac{i}{2}&0\\
0&-\tfrac12&\tfrac12&0\\
\tfrac{i}{2}&0&0&-\tfrac{i}{2}
\end{pmatrix},
\qquad
(\mathsf{C}_4^{(0)})^{-1}\mathsf{M}_4^{L}(\tilde Q)\mathsf{C}_4^{(0)}
=\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-)
$$
when $\tilde Q$ commutes with $\vec e_z$ and the sign of $B$ is chosen so that the Q-adapted root is the standard root $i\vec e_z$; for $Q_x=Q_y=0$ this means $B=-Q_z$, so that $\lambda_\pm=Q_t\mp iQ_z$. The four columns are the coordinate columns of $E_{11},E_{12},E_{21},E_{22}$ read back through the inverse of $\mathsf{M}_2^{Q}$. The matrix is fixed because the standard root and the standard nilpotents are fixed.

For a general $\tilde Q$ the change matrix $\mathsf{C}_4(\tilde Q)$ is not fixed: its columns are the coordinates of the Q-adapted basis, which depends on $\tilde Q$. It satisfies
$$
\mathsf{C}_4(\tilde Q)^{-1}\mathsf{M}_4^{L}(\tilde Q)\mathsf{C}_4(\tilde Q)
=\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-),
$$
$$
\mathsf{C}_4(\tilde Q)^{-1}\mathsf{M}_4^{R}(\tilde Q)\mathsf{C}_4(\tilde Q)
=\operatorname{diag}(\lambda_+,\lambda_-,\lambda_+,\lambda_-).
$$
The two diagonalisations use the same change of basis, because the Q-adapted order diagonalises both the left and the right multiplication. This is the $4\times4$ statement that the eigenbasis is a basis of eigenvectors for both operators.

**The change as a Kronecker product.** In the matrix-unit order the change from the fixed model to the Q-adapted model is the conjugation $X\mapsto\mathsf{C}_Q^{-1}X\mathsf{C}_Q$ on $M_2(\mathbb{C})$. On the four coordinates, with the column-major order $(E_{11},E_{21},E_{12},E_{22})$, this conjugation is the Kronecker product
$$
\mathsf{C}_Q^{\mathsf T}\otimes\mathsf{C}_Q^{-1}.
$$
The fixed change $\mathsf{C}_4^{(0)}$ is the same construction for the standard root, composed with the fixed passage from the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ to the matrix units. The composition is the reason the $4\times4$ change is not a single Kronecker product in the order of the fixed basis: the fixed basis is not the matrix-unit basis, and the permutation between them is the one displayed in $\mathsf{C}_4^{(0)}$.

### Base Changes in the $4\times4$ Model

A change of basis $P\in GL_4(\mathbb{C})$ acts on the regular matrices by
$$
\mathsf{M}_4^{L}(\tilde Q_2)\longmapsto P^{-1}\mathsf{M}_4^{L}(\tilde Q_2)P,
\qquad
\mathsf{M}_4^{R}(\tilde Q_2)\longmapsto P^{-1}\mathsf{M}_4^{R}(\tilde Q_2)P.
$$
The trace, the determinant, the characteristic polynomial and the spectrum are unchanged. The Q-adapted change is the particular $P=\mathsf{C}_4(\tilde Q)$ that diagonalises both matrices. The basis is fixed by the Peirce conditions: the two idempotents $\tilde\Pi_\pm$ must remain idempotent, so their scales are $1$, and the two nilpotents satisfy $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$ and $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$, so their scales are reciprocal. The only remaining freedom is
$$
\vec\Upsilon_+\longmapsto\mu\vec\Upsilon_+,\qquad
\vec\Upsilon_-\longmapsto\mu^{-1}\vec\Upsilon_-,\qquad
\mu\in\mathbb{C}^{\times},
$$
which leaves the diagonal form and the Peirce multiplication table unchanged. This is the $4\times4$ form of the relative scale of §*The Freedom of the Change*; the common scale of the $2\times2$ diagonaliser is the part that leaves the conjugation unchanged.

**The two models compared.** The $2\times2$ model and the $4\times4$ model carry the same element but different linear objects. The $2\times2$ matrix is the element; the $4\times4$ matrix is the operator of left or right multiplication by the element. The $2\times2$ model is irreducible, the $4\times4$ model is the direct sum of two copies of it, and the eigenvalues of the $4\times4$ matrix are the eigenvalues of the $2\times2$ matrix, each repeated twice. The $2\times2$ model has the two columns for the two spinor spaces; the $4\times4$ model has the two blocks for the two copies, and the Q-adapted order interleaves them.

## Summary

**The eigenbasis in the $2\times2$ model.** The eigenprojections are the spectral projectors $\rho_\pm=\mathsf{M}_2(\tilde\Pi_\pm)$, the nilpotents are the two square-zero matrices $\mathsf{M}_2(\vec\Upsilon_\pm)$ in the two mixed corners, and the Q-adapted model $\mathsf{M}_2^{Q}$ sends them to the four matrix units. The element is diagonal in that model, $\mathsf{M}_2^{Q}(\tilde Q)=\operatorname{diag}(\lambda_+,\lambda_-)$, and a general element has a full $2\times2$ matrix.

**The base change.** The fixed model and the Q-adapted model are related by
$$
\mathsf{M}_2^{Q}(\tilde Q_2)=\mathsf{C}_Q^{-1}\mathsf{M}_2(\tilde Q_2)\mathsf{C}_Q,
$$
with $\mathsf{C}_Q$ the eigenvector matrix of §*Base Changes*. The change is unique up to the rescaling of its two columns, and the relative scale is the reciprocal rescaling of the nilpotents. The change is attached to the element, not to the algebra: two elements with different roots have different Q-adapted bases, related by a further change of basis.

**The $4\times4$ model.** In the Q-adapted order the left and right regular matrices are
$$
[L_{\tilde Q_2}]_{\mathrm Q}=M\otimes\mathrm I_2,
\qquad
[R_{\tilde Q_2}]_{\mathrm Q}=\mathrm I_2\otimes M^{\mathsf T},
$$
with $M=\mathsf{M}_2^{Q}(\tilde Q_2)$; for $\tilde Q_2=\tilde Q$ they are diagonal, with eigenvalues $(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$ and $(\lambda_+,\lambda_-,\lambda_+,\lambda_-)$. The $4\times4$ change of basis is the same eigenbasis change, read on the four-vector space.

**The limits.** For $Q_x^2+Q_y^2+Q_z^2=0$ the construction fails: there is no spectral projector of rank one attached to $\tilde Q$, no Q-adapted basis, no nilpotent normalisation and no diagonal form. The fixed model still exists, and the matrix of $\tilde Q$ is a Jordan block when $Q_t\neq0$ and a nonzero nilpotent when $Q_t=0$. The fixed $4\times4$ matrices still exist and still satisfy their multiplicativity; they are not diagonalisable. The scalar case $\vec Q=0$ has $\mathsf{M}_2(\tilde Q)=Q_t\mathrm I_2$, every basis is an eigenbasis, and the Q-adapted construction is absent while an eigenbasis is not.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2$ | Fixed $2\times2$ matrix element representation $\mathbb{B}\to M_2(\mathbb{C})$ |
| $\mathsf{M}_2^{Q}$ | Q-adapted $2\times2$ model, $\mathsf{M}_2^{Q}(\tilde Q_2)=\mathsf{C}_Q^{-1}\mathsf{M}_2(\tilde Q_2)\mathsf{C}_Q$ |
| $E_{ij}$ | Matrix unit with $1$ in row $i$, column $j$ |
| $\rho_\pm=\mathsf{M}_2(\tilde\Pi_\pm)$ | Spectral projectors of $\mathsf{M}_2(\tilde Q)$ |
| $\mathsf{C}_Q$ | Eigenvector matrix, columns a $\lambda_+$- and a $\lambda_-$-eigenvector |
| $\mathsf{C}_4^{(0)}$ | Fixed change to the standard Q-adapted order in the $4\times4$ model |
| $\mathsf{C}_4(\tilde Q)$ | Change to the Q-adapted order for a general $\tilde Q$ |
| $\mathsf{M}_4^{L},\mathsf{M}_4^{R}$ | Left and right regular matrices in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ |
| $[L_{\tilde Q_2}]_{\mathrm Q},[R_{\tilde Q_2}]_{\mathrm Q}$ | Regular matrices in the Q-adapted order |
| $[L_{\tilde Q_2}]_{\mathrm{col}},[R_{\tilde Q_2}]_{\mathrm{col}}$ | Regular matrices in the column order |
| $\otimes$ | Kronecker product |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | The two spinor spaces, the two columns of the $2\times2$ model |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for idempotents, Peirce decompositions and the matrix units of a Peirce decomposition.
- Fuzhen Zhang, *Matrix Theory: Basic Results and Techniques*, 2nd edition (Springer, 2011), for the change of basis, the spectral projectors and the Kronecker product.
