# __Eigenbasis of a Reduced Biquaternion in Matrix Elements Representations__

## Introduction

The eigenbasis of a reduced biquaternion $\breve Q=Q_\blacktriangle+jQ_\blacktriangledown$ is the pair
$$
\Pi_+=\tfrac12(1+j),\qquad \Pi_-=\tfrac12(1-j),
$$
in which multiplication by $\breve Q$ is diagonal with eigenvalues
$$
Q_+=Q_\blacktriangle+Q_\blacktriangledown,\qquad
Q_-=Q_\blacktriangle-Q_\blacktriangledown.
$$
The eigenvalue decomposition, the eigenprojections and the Peirce decomposition are the subject of *Eigenvalue Decomposition and Eigenbasis of a Reduced Biquaternion*. This article reads the same objects in the matrix element representations of the algebra.

The algebra $\mathbb{B}_{\mathrm r}$ is two-dimensional over $\mathbb{C}$, commutative and associative, with $j^2=1$ and $i$ central. Its **$2\times2$ matrix element representation** is the left regular representation in the complex basis $1,j$,
$$
\varphi:\mathbb{B}_{\mathrm r}\longrightarrow M_2(\mathbb{C}),
\qquad
\varphi(\breve Q)=
\begin{pmatrix}Q_\blacktriangle&Q_\blacktriangledown\\ Q_\blacktriangledown&Q_\blacktriangle\end{pmatrix},
$$
the model of *Introduction to the $2\times2$ Matrix Element Representation of the Reduced Biquaternions*. In the eigenbasis the same element becomes the diagonal matrix $\operatorname{diag}(Q_+,Q_-)$; the passage between the two is the change of basis $\mathsf{C}$ of §*Base Changes*. The **$4\times4$ representation** is the real regular representation of $\mathbb{B}_{\mathrm r}$ on the real basis $1,i,j,ij$; it is the realification of the $2\times2$ complex model and is the model of *Introduction to the $2\times2$ Matrix Element Representation of the Reduced Biquaternions*, §*The Real-Entry Model*.

The article is organised around three questions. **Which matrices are the eigenprojections?** They are the two rank-one spectral projectors $\rho_\pm=\varphi(\Pi_\pm)$ of $\varphi(\breve Q)$. **What does a change of basis do?** It conjugates every matrix, leaves the trace, the determinant and the spectrum unchanged, and carries the regular model to the diagonal model; the change is unique up to the two independent scales of the eigenvectors. **What happens in the $4\times4$ representation?** The real regular matrix is the realification of the $2\times2$ complex matrix, it is block diagonal in the idempotent coordinates, and the realified $\mathsf{C}$ block-diagonalises it with the two complex eigenvalues.

| Question | Answer |
|---|---|
| $2\times2$ model | $\varphi(\breve Q)=\begin{pmatrix}Q_\blacktriangle&Q_\blacktriangledown\\ Q_\blacktriangledown&Q_\blacktriangle\end{pmatrix}$ |
| Eigenprojections | $\rho_\pm=\tfrac12\begin{pmatrix}1&\pm1\\ \pm1&1\end{pmatrix}$ |
| Eigenbasis model | $\varphi^{\Pi}(\breve Q)=\operatorname{diag}(Q_+,Q_-)$ |
| Base change | $\mathsf{C}=\tfrac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, $\mathsf{C}^{-1}=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ |
| Change law | $\varphi^{\Pi}(\breve Q_2)=\mathsf{C}^{-1}\varphi(\breve Q_2)\mathsf{C}$ |
| Spinor spaces | $S_+=\mathbb{C}\Pi_+$, $S_-=\mathbb{C}\Pi_-$, the two columns |
| $4\times4$ model | realification of the $2\times2$ complex model, on the real basis $1,i,j,ij$ |
| $4\times4$ diagonal | block diagonal with the real $2\times2$ blocks of $Q_+$ and $Q_-$; over $\mathbb{C}$, $\operatorname{diag}(Q_+,\overline{Q_+},Q_-,\overline{Q_-})$ |

**Conventions.** $\breve Q=Q_\blacktriangle+jQ_\blacktriangledown$, $\breve Q_2=Q_{2\blacktriangle}+jQ_{2\blacktriangledown}$, $Q_\pm=Q_\blacktriangle\pm Q_\blacktriangledown$, and a general element in the eigenbasis is $\breve X=\xi_+\Pi_++\xi_-\Pi_-$ with $\xi_\pm=Q_\blacktriangle\pm Q_\blacktriangledown$. The matrix $\varphi$ is the regular matrix in the basis $1,j$; the matrix $\varphi^{\Pi}$ is the matrix in the eigenbasis $(\Pi_+,\Pi_-)$. The change matrix is $\mathsf{C}$, with columns the coordinates of $\Pi_+,\Pi_-$ in the basis $1,j$. The realification is written $L_{\breve Q}$ in the basis $1,i,j,ij$. The two representation articles cited above own the assignments and the invariants; this article owns their reading in the eigenbasis and the changes of basis.

**Boundaries.** The spectrum, the eigenprojections and the eigenvalue decomposition are *Eigenvalue Decomposition and Eigenbasis of a Reduced Biquaternion*. The $2\times2$ assignment, its multiplicativity and its invariants are *Introduction to the $2\times2$ Matrix Element Representation of the Reduced Biquaternions*; the algebra in that model is *The Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions*; the four-vector form is *The Four-Vector Element Representation of the Reduced Biquaternions*. The change of basis of an endomorphism is *Matrix Algebras*, §*Change of Basis*; the realification is *The Realification and the Effect of the Change of Scalars*.

## The $2\times2$ Matrix Element Representation

**The regular matrix has the two complex coordinates on the diagonal and the same coordinate off the diagonal, and its determinant is the algebraic norm.**

In the complex basis $1,j$ the left multiplication $L_{\breve X}(\breve Y)=\breve X\breve Y$ has the matrix
$$
\varphi(\breve X)=
\begin{pmatrix}Q_\blacktriangle&Q_\blacktriangledown\\ Q_\blacktriangledown&Q_\blacktriangle\end{pmatrix},
\qquad
\breve X=Q_\blacktriangle+jQ_\blacktriangledown.
$$
The columns are the images of the basis,
$$
L_{\breve X}(1)=\breve X,\qquad
L_{\breve X}(j)=\breve Xj=Q_\blacktriangledown+jQ_\blacktriangle,
$$
which gives the columns $(Q_\blacktriangle,Q_\blacktriangledown)^{\mathsf T}$ and $(Q_\blacktriangledown,Q_\blacktriangle)^{\mathsf T}$. The assignment on the real basis is
$$
\varphi(1)=\mathrm I_2,\qquad
\varphi(i)=i\mathrm I_2,\qquad
\varphi(j)=\begin{pmatrix}0&1\\1&0\end{pmatrix}=\sigma_1,\qquad
\varphi(ij)=i\sigma_1.
$$
The map is an injective homomorphism of $\mathbb{C}$-algebras,
$$
\varphi(\breve X\breve Y)=\varphi(\breve X)\varphi(\breve Y),
\qquad
\varphi(1)=\mathrm I_2,
$$
whose image is the two-dimensional commutative subalgebra of matrices of the form $\begin{pmatrix}a&b\\b&a\end{pmatrix}$, not the whole of $M_2(\mathbb{C})$.

**Invariants and inverse.** The trace and the determinant are
$$
\boxed{\;
\operatorname{tr}\varphi(\breve X)=2Q_\blacktriangle,\qquad
\det\varphi(\breve X)=Q_\blacktriangle^2-Q_\blacktriangledown^2
=\langle\breve X\rangle_{\mathrm{ts}}=Q_+Q_-
\;}.
$$
When $Q_+Q_-\neq0$,
$$
\varphi(\breve X)^{-1}
=\frac{1}{Q_+Q_-}
\begin{pmatrix}Q_\blacktriangle&-Q_\blacktriangledown\\ -Q_\blacktriangledown&Q_\blacktriangle\end{pmatrix}
=\varphi(\breve X^{-1}),
\qquad
\breve X^{-1}=\frac{Q_\blacktriangle-jQ_\blacktriangledown}{Q_+Q_-}.
$$
The matrix is singular exactly on the two complex lines $Q_+=0$ and $Q_-=0$, which are the two zero-divisor components.

**The basis matrices.** The table collects the basis elements and the two idempotents.

| Element | Matrix $\varphi$ | Square | Determinant |
|---|---|---|---|
| $1$ | $\mathrm I_2$ | $\mathrm I_2$ | $1$ |
| $i$ | $i\mathrm I_2$ | $-\mathrm I_2$ | $1$ |
| $j$ | $\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ | $\mathrm I_2$ | $-1$ |
| $ij$ | $i\sigma_1$ | $-\mathrm I_2$ | $-1$ |
| $\Pi_+$ | $\tfrac12\begin{pmatrix}1&1\\1&1\end{pmatrix}$ | itself | $0$ |
| $\Pi_-$ | $\tfrac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$ | itself | $0$ |

**The two idempotents are the two spectral projectors.** They satisfy
$$
\rho_+^2=\rho_+,\qquad
\rho_-^2=\rho_-,\qquad
\rho_+\rho_-=0,\qquad
\rho_++\rho_-=\mathrm I_2,
$$
and
$$
\varphi(\breve Q)\rho_+ = Q_+\rho_+,\qquad
\varphi(\breve Q)\rho_- = Q_-\rho_-.
$$
Each has rank one when $Q_+\neq Q_-$, that is when $Q_\blacktriangledown\neq0$. At $Q_\blacktriangledown=0$ the matrix is scalar, the two eigenvalues coincide, and every projector is spectral.

## The Eigenbasis in the Model

**In the eigenbasis the matrix of every element is diagonal, and the diagonal entries are its two idempotent coordinates.**

The assignment
$$
\Pi_+\longmapsto\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
\Pi_-\longmapsto\begin{pmatrix}0&0\\0&1\end{pmatrix},\qquad
1\longmapsto\mathrm I_2,\qquad
j\longmapsto\begin{pmatrix}1&0\\0&-1\end{pmatrix}
$$
is an isomorphism of $\mathbb{C}$-algebras from $\mathbb{B}_{\mathrm r}$ onto the diagonal subalgebra of $M_2(\mathbb{C})$. For a general element
$$
\breve X=Q_\blacktriangle+jQ_\blacktriangledown=\xi_+\Pi_++\xi_-\Pi_-,
\qquad
\xi_\pm=Q_\blacktriangle\pm Q_\blacktriangledown,
$$
the matrix is
$$
\boxed{\;
\varphi^{\Pi}(\breve X)=
\begin{pmatrix}\xi_+&0\\0&\xi_-\end{pmatrix}
\;}.
$$
For $\breve Q$ itself,
$$
\varphi^{\Pi}(\breve Q)=
\begin{pmatrix}Q_+&0\\0&Q_-\end{pmatrix}.
$$
The basis elements and the general element are collected in the table.

| Element | Coordinates in $(\Pi_+,\Pi_-)$ | Matrix $\varphi^{\Pi}$ |
|---|---|---|
| $1$ | $(1,1)$ | $\mathrm I_2$ |
| $i$ | $(i,i)$ | $i\mathrm I_2$ |
| $j$ | $(1,-1)$ | $\operatorname{diag}(1,-1)$ |
| $ij$ | $(i,-i)$ | $\operatorname{diag}(i,-i)$ |
| $\breve X=Q_\blacktriangle+jQ_\blacktriangledown$ | $(Q_+,Q_-)$ | $\operatorname{diag}(Q_+,Q_-)$ |
| $\breve Q$ | $(Q_+,Q_-)$ | $\operatorname{diag}(Q_+,Q_-)$ |

**The eigenbasis model is the Peirce-coordinate model.** The two coordinates are the two Peirce coordinates of the element, and the matrix is diagonal because the two Peirce corners of the reduced biquaternion algebra vanish. The model is not the regular model: the regular model has the off-diagonal entries $Q_\blacktriangledown$, while the eigenbasis model has them zero. The two are related by the change of basis of §*Base Changes*.

**The algebra in matrix form.** For two elements $\breve X=\xi_+\Pi_++\xi_-\Pi_-$ and $\breve Y=\eta_+\Pi_++\eta_-\Pi_-$,
$$
\breve X\breve Y\longleftrightarrow
\begin{pmatrix}\xi_+\eta_+&0\\0&\xi_-\eta_-\end{pmatrix},
\qquad
\breve X^{-1}\longleftrightarrow
\operatorname{diag}(\xi_+^{-1},\xi_-^{-1}),
\qquad
\breve X^n\longleftrightarrow
\operatorname{diag}(\xi_+^n,\xi_-^n).
$$
The trace and the determinant are
$$
\operatorname{tr}=\xi_++\xi_-=2Q_\blacktriangle,\qquad
\det=\xi_+\xi_-=Q_\blacktriangle^2-Q_\blacktriangledown^2=\langle\breve X\rangle_{\mathrm{ts}}.
$$
The element is a unit exactly when both diagonal entries are nonzero, and a zero divisor exactly when exactly one of them is zero. There is no nonzero nilpotent: a diagonal matrix with square zero is zero, and the off-diagonal matrix units are not in the image. The conjugation is
$$
\breve X^{\dagger}=\xi_-\Pi_++\xi_+\Pi_-
\longleftrightarrow
\operatorname{diag}(\xi_-,\xi_+),
$$
where $\dagger$ is the Hermitian conjugation of the reduced biquaternion algebra.

## Base Changes

**The regular model and the eigenbasis model are two bases of the same complex plane, and the passage between them is the conjugation by the matrix of the two idempotents.**

### The Change of Basis of a Matrix Model

Let $P\in GL_2(\mathbb{C})$ have as columns the coordinates of a new basis in the old one. The matrix of the same endomorphism in the new basis is
$$
M'=P^{-1}MP.
$$
The trace and the determinant are unchanged,
$$
\operatorname{tr}M'=\operatorname{tr}M,\qquad
\det M'=\det M,
$$
and so are the characteristic polynomial, the spectrum, the rank and the Jordan form. An idempotent is conjugated to an idempotent, the two eigenspaces to the two coordinate axes, and the eigenvalues are unchanged. The columns of $P$ are the new basis vectors; a column that is an eigenvector of $M$ produces a column of $P^{-1}MP$ with the eigenvalue on the diagonal.

### The Explicit Change

The change matrix has as columns the coordinates of $\Pi_+,\Pi_-$ in the basis $1,j$:
$$
\mathsf{C}=\frac12
\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
\mathsf{C}^{-1}=
\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
\det\mathsf{C}=-\frac12.
$$
Its columns are eigenvectors of $\varphi(\breve Q)$:
$$
\varphi(\breve Q)\begin{pmatrix}1/2\\1/2\end{pmatrix}
=Q_+\begin{pmatrix}1/2\\1/2\end{pmatrix},
\qquad
\varphi(\breve Q)\begin{pmatrix}1/2\\-1/2\end{pmatrix}
=Q_-\begin{pmatrix}1/2\\-1/2\end{pmatrix}.
$$
Therefore
$$
\mathsf{C}^{-1}\varphi(\breve Q)\mathsf{C}
=\operatorname{diag}(Q_+,Q_-)
=\varphi^{\Pi}(\breve Q),
$$
and, for every element $\breve X$,
$$
\varphi^{\Pi}(\breve X)=\mathsf{C}^{-1}\varphi(\breve X)\mathsf{C}.
$$
The first column of $\mathsf{C}$ is the first column of $\rho_+$; the second is the negative of the second column of $\rho_-$. The columns are the nonzero columns of the two spectral projectors, normalised to have entries $\pm\tfrac12$. The sibling article *Introduction to the $2\times2$ Matrix Element Representation of the Reduced Biquaternions* uses the unnormalised matrix $P=2\mathsf{C}=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$; the two changes differ by the common scale $2$, which leaves the conjugation unchanged.

**The inverse change.** The inverse matrix has integer entries and determinant $-2$:
$$
\mathsf{C}^{-1}=
\begin{pmatrix}1&1\\1&-1\end{pmatrix}
=2\mathsf{C}.
$$
It sends the diagonal model back to the regular one, and its columns are the coordinates of $1,j$ in the eigenbasis.

### The Freedom of the Change

The diagonalising matrix is not unique. If $\mathsf{C}$ diagonalises $\varphi(\breve Q)$, then so does $\mathsf{C}D$ for every invertible diagonal $D=\operatorname{diag}(\alpha,\beta)$:
$$
(\mathsf{C}D)^{-1}\varphi(\breve Q)(\mathsf{C}D)
=D^{-1}\operatorname{diag}(Q_+,Q_-)D
=\operatorname{diag}(Q_+,Q_-).
$$
The two scales are the two independent rescalings of the eigenvectors. A common scale leaves the conjugation unchanged; a relative scale multiplies the two columns by $\alpha$ and $\beta$, and the diagonal model is unchanged because diagonal matrices commute with $D$. In the algebra, the general eigenbasis is
$$
(\alpha\Pi_+,\beta\Pi_-),
\qquad
\alpha,\beta\in\mathbb{C}^{\times},
$$
and the normalised pair is $\alpha=\beta=1$. When $Q_\blacktriangledown=0$ the eigenvalues coincide, every nonzero vector is an eigenvector, every basis is an eigenbasis, and the change matrix is an arbitrary invertible matrix.

**What depends on $\breve Q$.** The change matrix $\mathsf{C}$ and the diagonal matrix $\operatorname{diag}(Q_+,Q_-)$ depend on $\breve Q$ through $Q_\blacktriangledown$: the two eigenvectors are fixed only when the two eigenvalues are distinct. The regular model $\varphi$ and the assignment on the basis do not depend on $\breve Q$. The eigenbasis model is the same assignment for every $\breve Q$ with $Q_\blacktriangledown\neq0$; the dependence is carried by the eigenvalues, not by the basis. This is the structural difference with the biquaternion case, where the eigenbasis itself depends on the element.

### The Two Normal Forms

The regular model and the eigenbasis model are the two normal forms of the same matrix under conjugation. The first is the **element model**: the matrix entries are the coefficients of the element in the basis $1,j$. The second is the **spectral model**: the matrix entries are the two eigenvalues. The two are related by $\mathsf{C}$, and the relation is the diagonalisation of every element at once, because the algebra is commutative. In the biquaternion case no single change diagonalises every element, and the corresponding matrix $\mathsf{C}_Q$ depends on $Q$.

**The real change.** The same change, read on the real four-dimensional space, is the realification of $\mathsf{C}$:
$$
\mathsf{C}_4=
\begin{pmatrix}
\tfrac12&0&\tfrac12&0\\
0&\tfrac12&0&\tfrac12\\
\tfrac12&0&-\tfrac12&0\\
0&\tfrac12&0&-\tfrac12
\end{pmatrix},
$$
in the real basis $1,i,j,ij$, whose columns are the coordinate columns of $\Pi_+,i\Pi_+,\Pi_-,i\Pi_-$. Its determinant is $(\det\mathsf{C})^2=\tfrac14$. The determinant of the complex change is $-\tfrac12$, and the determinant of the real change is the square of its modulus, $\tfrac14$.

## Spinors and the Columns

**The two columns of the eigenbasis model are the two spinor spaces, and a spinor is one complex coefficient on one of them.**

Since $\mathbb{B}_{\mathrm r}$ is commutative, the left, right and two-sided ideals coincide. The minimal nonzero ideals are
$$
S_+=\mathbb{B}_{\mathrm r}\Pi_+=\mathbb{C}\Pi_+,
\qquad
S_-=\mathbb{B}_{\mathrm r}\Pi_-=\mathbb{C}\Pi_-,
$$
each one-dimensional over $\mathbb{C}$, and $\mathbb{B}_{\mathrm r}=S_+\oplus S_-$. In the eigenbasis model they are the two columns:
$$
S_+\longleftrightarrow\left\{\begin{pmatrix}A_1&0\\0&0\end{pmatrix}:A_1\in\mathbb{C}\right\},
\qquad
S_-\longleftrightarrow\left\{\begin{pmatrix}0&0\\0&A_2\end{pmatrix}:A_2\in\mathbb{C}\right\}.
$$
A spinor of the first Peirce copy is $\xi_+=A_1\Pi_+$ and is represented by the first column $(A_1,0)^{\mathsf T}$; a spinor of the second Peirce copy is $\xi_-=A_2\Pi_-$ and is represented by the second column $(0,A_2)^{\mathsf T}$. The general element is the sum of one spinor of each Peirce copy, and its two coordinates are the two diagonal entries.

Under multiplication by $\breve Q$ the two columns are scaled independently:
$$
\breve Q\xi_+ = Q_+\xi_+
\longleftrightarrow
\begin{pmatrix}Q_+&0\\0&0\end{pmatrix}
\begin{pmatrix}A_1\\0\end{pmatrix}
=
\begin{pmatrix}Q_+A_1\\0\end{pmatrix},
\qquad
\breve Q\xi_- = Q_-\xi_-
\longleftrightarrow
\begin{pmatrix}0&0\\0&Q_-\end{pmatrix}
\begin{pmatrix}0\\A_2\end{pmatrix}
=
\begin{pmatrix}0\\Q_-A_2\end{pmatrix}.
$$
The same diagonal matrix $\operatorname{diag}(Q_+,Q_-)$ acts on both columns; on the first column only the first entry survives, on the second only the second. This is the precise sense in which the two spinor spaces are the two eigenspaces.

**Right multiplication.** Since the algebra is commutative, right multiplication by $\breve Q$ acts exactly as left multiplication, and the rows are the same two lines. The matrix is symmetric, so the row picture and the column picture coincide. This is the reduced-biquaternion difference with the biquaternion case, where the rows are the two minimal right ideals and the columns the two minimal left ideals, and the two pictures are different.

## The $4\times4$ Matrix Element Representation

**The $4\times4$ real matrix is the regular representation on the real basis $1,i,j,ij$, and it is the realification of the $2\times2$ complex model.**

On the real basis $1,i,j,ij$, an element is
$$
\breve X=Q_\blacktriangle+jQ_\blacktriangledown,
\qquad
Q_\blacktriangle=q_\blacktriangle+iq'_\blacktriangle,\quad
Q_\blacktriangledown=q_\blacktriangledown+iq'_\blacktriangledown,
$$
and left multiplication has the real matrix
$$
L_{\breve X}=
\begin{pmatrix}
q_\blacktriangle&-q'_\blacktriangle&q_\blacktriangledown&-q'_\blacktriangledown\\
q'_\blacktriangle&q_\blacktriangle&q'_\blacktriangledown&q_\blacktriangledown\\
q_\blacktriangledown&-q'_\blacktriangledown&q_\blacktriangle&-q'_\blacktriangle\\
q'_\blacktriangledown&q_\blacktriangledown&q'_\blacktriangle&q_\blacktriangle
\end{pmatrix}
=
\begin{pmatrix}A_+&A_-\\ A_-&A_+\end{pmatrix},
$$
with
$$
A_+=\begin{pmatrix}q_\blacktriangle&-q'_\blacktriangle\\ q'_\blacktriangle&q_\blacktriangle\end{pmatrix},
\qquad
A_-=\begin{pmatrix}q_\blacktriangledown&-q'_\blacktriangledown\\ q'_\blacktriangledown&q_\blacktriangledown\end{pmatrix}.
$$
The matrix is the realification of the complex $2\times2$ matrix $\varphi(\breve X)$: each complex entry becomes its real $2\times2$ block, and the two diagonal blocks are $A_+$ and the two off-diagonal blocks are $A_-$. It is an injective homomorphism of $\mathbb{R}$-algebras, and
$$
\boxed{\;
\operatorname{tr}L_{\breve X}=4q_\blacktriangle,\qquad
\det L_{\breve X}=\lvert Q_+Q_-\rvert^2
\;}.
$$
The determinant is the squared modulus of the complex determinant, which is the general rule for the realification.

**The idempotent coordinates.** In the complexified eigenbasis the element is
$$
\breve X=\xi_+\Pi_++\xi_-\Pi_-,
\qquad
\xi_\pm=Q_\blacktriangle\pm Q_\blacktriangledown,
$$
and the complex $2\times2$ matrix is $\operatorname{diag}(\xi_+,\xi_-)$. The realification of this diagonal matrix is block diagonal,
$$
L_{\breve X}\sim
\begin{pmatrix}
\operatorname{Re}\xi_+&-\operatorname{Im}\xi_+&0&0\\
\operatorname{Im}\xi_+&\operatorname{Re}\xi_+&0&0\\
0&0&\operatorname{Re}\xi_-&-\operatorname{Im}\xi_-\\
0&0&\operatorname{Im}\xi_-&\operatorname{Re}\xi_-
\end{pmatrix},
$$
in the real basis $(\Pi_+,i\Pi_+,\Pi_-,i\Pi_-)$. For $\breve X=\breve Q$ the two blocks are the two complex eigenvalues $Q_\pm$, each read as a real $2\times2$ rotation-dilation block. Over $\mathbb{C}$, the four eigenvalues are $Q_+,\overline{Q_+},Q_-,\overline{Q_-}$, with the bar the complex conjugation of the complexified scalar, not the Hermitian conjugation of the reduced biquaternion.

**The change of basis.** The real change matrix is
$$
\mathsf{C}_4=
\begin{pmatrix}
\tfrac12&0&\tfrac12&0\\
0&\tfrac12&0&\tfrac12\\
\tfrac12&0&-\tfrac12&0\\
0&\tfrac12&0&-\tfrac12
\end{pmatrix},
$$
whose columns are the coordinate columns of $\Pi_+,i\Pi_+,\Pi_-,i\Pi_-$ in the real basis $1,i,j,ij$. It satisfies
$$
\mathsf{C}_4^{-1}L_{\breve Q}\mathsf{C}_4
=
\begin{pmatrix}
\operatorname{Re}Q_+&-\operatorname{Im}Q_+&0&0\\
\operatorname{Im}Q_+&\operatorname{Re}Q_+&0&0\\
0&0&\operatorname{Re}Q_-&-\operatorname{Im}Q_-\\
0&0&\operatorname{Im}Q_-&\operatorname{Re}Q_-
\end{pmatrix}.
$$
Over $\mathbb{C}$ this block matrix is diagonalised by the further change with columns $(1,-i)$ and $(1,i)$ in each block, giving $\operatorname{diag}(Q_+,\overline{Q_+},Q_-,\overline{Q_-})$. The determinant of $\mathsf{C}_4$ is $(\det\mathsf{C})^2=\tfrac14$, as in the $2\times2$ model.

**What the $4\times4$ model adds.** The $4\times4$ model does not add a new representation of $\mathbb{B}_{\mathrm r}$ over $\mathbb{C}$: it is the $2\times2$ complex model read over $\mathbb{R}$, and its eigenbasis is the realified complex eigenbasis. It adds the real geometry of the two complex eigenvalues: each eigenvalue becomes a $2\times2$ block, the two blocks are independent, and the four real eigenvalues are the two complex eigenvalues together with their complex conjugates. This is the reduced-biquaternion analogue of the $4\times4$ regular matrices of the biquaternion case, with the difference that the biquaternion $4\times4$ model is over $\mathbb{C}$ and has the eigenvalues $Q_+,Q_+,Q_-,Q_-$ without the complex conjugates.

## Summary

**The $2\times2$ model.** The regular matrix is $\varphi(\breve X)=\begin{pmatrix}Q_\blacktriangle&Q_\blacktriangledown\\ Q_\blacktriangledown&Q_\blacktriangle\end{pmatrix}$, with determinant the algebraic norm and trace twice the complex scalar part. The eigenprojections are the two rank-one matrices $\rho_\pm=\tfrac12\begin{pmatrix}1&\pm1\\ \pm1&1\end{pmatrix}$, and the eigenbasis model is
$$
\varphi^{\Pi}(\breve Q)=\operatorname{diag}(Q_+,Q_-).
$$

**The base change.** The two models are related by
$$
\varphi^{\Pi}(\breve X)=\mathsf{C}^{-1}\varphi(\breve X)\mathsf{C},
\qquad
\mathsf{C}=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
\mathsf{C}^{-1}=\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
$$
The change is unique up to the two independent rescalings of the two eigenvectors. It is the same matrix for every element, because the algebra is commutative and the eigenbasis is fixed by $j$.

**The $4\times4$ model.** The real regular matrix is the realification of the complex $2\times2$ matrix; in the idempotent coordinates it is block diagonal with the two complex eigenvalues, and the realified $\mathsf{C}$ block-diagonalises it. Over $\mathbb{C}$ the four eigenvalues are $Q_+,\overline{Q_+},Q_-,\overline{Q_-}$.

**The limits.** For $Q_\blacktriangledown=0$ the two eigenvalues coincide, the eigenbasis is not unique, every basis is an eigenbasis, and the change matrix is an arbitrary invertible matrix. For $Q_+=0$ or $Q_-=0$ one eigenvalue vanishes, the element is a zero divisor, and the corresponding spectral projector has rank one with one zero eigenvalue; the matrices remain diagonalisable. There is no nonzero nilpotent in any regime, so the nilpotent construction of the biquaternion case has no analogue here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\varphi$ | Left regular matrix in the complex basis $1,j$ |
| $\varphi^{\Pi}$ | Matrix in the eigenbasis $(\Pi_+,\Pi_-)$ |
| $L_{\breve X}$ | Real regular matrix in the basis $1,i,j,ij$ |
| $\mathsf{C}$ | Change matrix from $1,j$ to $\Pi_+,\Pi_-$ |
| $\mathsf{C}_4$ | Realification of $\mathsf{C}$, the $4\times4$ change |
| $Q_\pm=Q_\blacktriangle\pm Q_\blacktriangledown$ | The two eigenvalues |
| $\rho_\pm=\varphi(\Pi_\pm)$ | Spectral projectors |
| $S_\pm=\mathbb{C}\Pi_\pm$ | The two spinor spaces, the two columns |
| $\langle\breve X\rangle_{\mathrm{ts}}=Q_\blacktriangle^2-Q_\blacktriangledown^2$ | The algebraic norm, the determinant of $\varphi(\breve X)$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for idempotents, Peirce decompositions and the matrix units of a Peirce decomposition.
- Fuzhen Zhang, *Matrix Theory: Basic Results and Techniques*, 2nd edition (Springer, 2011), for the change of basis, the spectral projectors and the realification of a complex matrix.
