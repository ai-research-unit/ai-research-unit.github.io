# __Eigenbasis of a Split-Complex Number in Matrix Elements Representations__

## Introduction

The eigenbasis of a split-complex number $Q=q+jq'$ is the pair
$$
\Pi_+=\tfrac12(1+j),\qquad \Pi_-=\tfrac12(1-j),
$$
in which multiplication by $Q$ is diagonal with eigenvalues $\lambda_+=q+q'$ and $\lambda_-=q-q'$. The eigenvalue decomposition, the eigenprojections and the Peirce decomposition are the subject of *Eigenbasis of a Split-Complex Number*. This article reads the same objects in the matrix element representations of the algebra.

The algebra $\mathbb{D}$ is two-dimensional over $\mathbb{R}$, and its **$2\times2$ matrix element representation** is the left regular representation in the basis $1,j$,
$$
\mathsf{M}_2:\mathbb{D}\longrightarrow M_2(\mathbb{R}),
\qquad
\mathsf{M}_2(Q)=\begin{pmatrix}q&q'\\q'&q\end{pmatrix},
$$
the Cayley matrix of *Split-Complex Regular Element Representation*. In the eigenbasis the same element becomes the diagonal matrix $\operatorname{diag}(\lambda_+,\lambda_-)$; the passage between the two is the change of basis $\mathsf{C}$ of §*Base Changes*. The **$4\times4$ representation** is not a representation of $\mathbb{D}$ itself — the regular representation of a two-dimensional algebra is $2\times2$ — but the real regular representation of its complexification $\mathbb{D}_{\mathbb{C}}\cong\mathbb{C}\times\mathbb{C}$, of real dimension four. It is the matrix form of the complexified eigenbasis and is the exact split-complex analogue of the $4\times4$ regular matrices of the biquaternion case.

The article is organised around three questions. **Which matrices are the eigenprojections?** They are the two rank-one spectral projectors $\rho_\pm=\mathsf{M}_2(\Pi_\pm)$ of $\mathsf{M}_2(Q)$. **What does a change of basis do?** It conjugates every matrix, leaves the trace, the determinant and the spectrum unchanged, and carries the regular model to the diagonal model; the change is unique up to the two independent scales of the eigenvectors. **What happens in the $4\times4$ representation?** The complexified regular matrix is the realification of the $2\times2$ complex matrix, it is block diagonal in the idempotent coordinates, and the realified $\mathsf{C}$ block-diagonalises it.

| Question | Answer |
|---|---|
| $2\times2$ regular model | $\mathsf{M}_2(Q)=\begin{pmatrix}q&q'\\q'&q\end{pmatrix}$ |
| Eigenprojections | $\rho_+=\tfrac12\begin{pmatrix}1&1\\1&1\end{pmatrix}$, $\rho_-=\tfrac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$ |
| Eigenbasis model | $\mathsf{M}_2^{\Pi}(Q)=\operatorname{diag}(\lambda_+,\lambda_-)$ |
| Base change | $\mathsf{C}=\tfrac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, $\mathsf{C}^{-1}=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ |
| Change law | $\mathsf{M}_2^{\Pi}(X)=\mathsf{C}^{-1}\mathsf{M}_2(X)\mathsf{C}$ |
| Spinor spaces | $S_+=\mathbb{R}\Pi_+$, $S_-=\mathbb{R}\Pi_-$, the two columns |
| $4\times4$ model | realification of the complexified $2\times2$ model, on the real basis $1,i,j,ij$ |
| $4\times4$ diagonal | block diagonal with the real $2\times2$ blocks of $\lambda_+$ and $\lambda_-$; over $\mathbb{C}$, $\operatorname{diag}(\lambda_+,\overline{\lambda_+},\lambda_-,\overline{\lambda_-})$ |

**Conventions.** $Q=q+jq'$, $Q_2=q_2+jq_2'$, $\lambda_\pm=q\pm q'$, and a general element in the eigenbasis is $X=\xi_+\Pi_++\xi_-\Pi_-$ with $\xi_\pm=x_0\pm x_1$. The matrix $\mathsf{M}_2$ is the regular matrix in the basis $1,j$; the matrix $\mathsf{M}_2^{\Pi}$ is the matrix in the eigenbasis $(\Pi_+,\Pi_-)$. The change matrix is $\mathsf{C}$, with columns the coordinates of $\Pi_+,\Pi_-$ in the basis $1,j$. The complexification is $\mathbb{D}_{\mathbb{C}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{D}$, with the central complex unit written $i$ and the real basis $1,i,j,ij$. The two representation articles cited above own the assignments and the invariants; this article owns their reading in the eigenbasis and the changes of basis.

**Boundaries.** The spectrum, the eigenprojections and the eigenvalue decomposition are *Eigenbasis of a Split-Complex Number*. The regular matrix, its multiplicativity and its determinant are *Split-Complex Regular Element Representation*; the two-component and the other representations are *Split-Complex Two-Component Element Representation* and *Split-Complex Element Representations*. The change of basis of an endomorphism is *Matrix Algebras*, §*Change of Basis*; the realification is *The Realification and the Effect of the Change of Scalars*.

## The $2\times2$ Matrix Element Representation

**The regular matrix has the two coefficients on the diagonal and the same coefficient off the diagonal, and its determinant is the norm.**

In the basis $1,j$ the left multiplication $L_X(Y)=XY$ has the matrix
$$
\mathsf{M}_2(X)=
\begin{pmatrix}x_0&x_1\\x_1&x_0\end{pmatrix},
\qquad X=x_0+x_1j.
$$
The columns are the images of the basis,
$$
L_X(1)=X=x_0+x_1j,\qquad L_X(j)=Xj=x_1+x_0j,
$$
which gives the two columns $(x_0,x_1)^{\mathsf T}$ and $(x_1,x_0)^{\mathsf T}$. The assignment on the basis is
$$
\mathsf{M}_2(1)=\mathrm I_2,\qquad
\mathsf{M}_2(j)=\begin{pmatrix}0&1\\1&0\end{pmatrix}=\sigma_1.
$$
The matrix is symmetric, and the two columns are exchanged by the reflection $j$. The map is an injective homomorphism of $\mathbb{R}$-algebras,
$$
\mathsf{M}_2(XY)=\mathsf{M}_2(X)\mathsf{M}_2(Y),
\qquad
\mathsf{M}_2(1)=\mathrm I_2,
$$
whose image is the two-dimensional commutative subalgebra of matrices of the form $\begin{pmatrix}a&b\\b&a\end{pmatrix}$, not the whole of $M_2(\mathbb{R})$.

**Invariants and inverse.** The trace and the determinant are
$$
\operatorname{tr}\mathsf{M}_2(X)=2x_0,\qquad
\det\mathsf{M}_2(X)=x_0^2-x_1^2=\langle X\rangle_{*}=XX^{\dagger},
$$
where $X^{\dagger}=x_0-x_1j$ is the conjugation. When $x_0^2\neq x_1^2$,
$$
\mathsf{M}_2(X)^{-1}=\frac{1}{x_0^2-x_1^2}
\begin{pmatrix}x_0&-x_1\\-x_1&x_0\end{pmatrix}
=\mathsf{M}_2(X^{-1}),
\qquad
X^{-1}=\frac{x_0-x_1j}{x_0^2-x_1^2}.
$$
The determinant vanishes exactly on the two null lines $x_0=\pm x_1$, which are the zero divisors; the matrix is singular exactly there. The elements of the image are simultaneously diagonalisable, because they commute and are symmetric.

**The basis matrices.** The table collects the four elements of the standard basis and their matrices.

| Element | Matrix $\mathsf{M}_2$ | Square | Determinant |
|---|---|---|---|
| $1$ | $\mathrm I_2$ | $\mathrm I_2$ | $1$ |
| $j$ | $\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ | $\mathrm I_2$ | $-1$ |
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
\mathsf{M}_2(Q)\rho_+=\lambda_+\rho_+,\qquad
\mathsf{M}_2(Q)\rho_-=\lambda_-\rho_-.
$$
Each has rank one when $q'\neq0$; at $q'=0$ the two projectors are still the rank-one matrices above, but they are no longer the spectral projectors of a matrix with distinct eigenvalues, because $\mathsf{M}_2(Q)=q\mathrm I_2$ and every projector is spectral.

## The Eigenbasis in the Model

**In the eigenbasis the matrix of every element is diagonal, and the diagonal entries are its two idempotent coordinates.**

The assignment
$$
\Pi_+\longmapsto\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
\Pi_-\longmapsto\begin{pmatrix}0&0\\0&1\end{pmatrix},\qquad
1\longmapsto\mathrm I_2,\qquad
j\longmapsto\begin{pmatrix}1&0\\0&-1\end{pmatrix}
$$
is an isomorphism of $\mathbb{R}$-algebras from $\mathbb{D}$ onto the diagonal subalgebra of $M_2(\mathbb{R})$. For a general element
$$
X=x_0+x_1j=\xi_+\Pi_++\xi_-\Pi_-,
\qquad
\xi_\pm=x_0\pm x_1,
$$
the matrix is
$$
\mathsf{M}_2^{\Pi}(X)=
\begin{pmatrix}\xi_+&0\\0&\xi_-\end{pmatrix}.
$$
For $Q$ itself,
$$
\mathsf{M}_2^{\Pi}(Q)=
\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}.
$$
The basis elements and the general element are collected in the table.

| Element | Coordinates in $(\Pi_+,\Pi_-)$ | Matrix $\mathsf{M}_2^{\Pi}$ |
|---|---|---|
| $1$ | $(1,1)$ | $\mathrm I_2$ |
| $j$ | $(1,-1)$ | $\operatorname{diag}(1,-1)$ |
| $\Pi_+$ | $(1,0)$ | $\operatorname{diag}(1,0)$ |
| $\Pi_-$ | $(0,1)$ | $\operatorname{diag}(0,1)$ |
| $X=x_0+x_1j$ | $(x_0+x_1,x_0-x_1)$ | $\operatorname{diag}(x_0+x_1,x_0-x_1)$ |
| $Q=q+jq'$ | $(\lambda_+,\lambda_-)$ | $\operatorname{diag}(\lambda_+,\lambda_-)$ |

**The eigenbasis model is the Peirce-coordinate model.** The two coordinates are the two Peirce coordinates of the element, and the matrix is diagonal because the two Peirce corners of the split-complex algebra vanish. The model is not the regular model: the regular model has the off-diagonal entries $x_1$, while the eigenbasis model has them zero. The two are related by the change of basis of §*Base Changes*.

**The algebra in matrix form.** For two elements $X=\xi_+\Pi_++\xi_-\Pi_-$ and $Y=\eta_+\Pi_++\eta_-\Pi_-$,
$$
XY\longleftrightarrow
\begin{pmatrix}\xi_+\eta_+&0\\0&\xi_-\eta_-\end{pmatrix},
\qquad
X^{-1}\longleftrightarrow
\operatorname{diag}(\xi_+^{-1},\xi_-^{-1}),
\qquad
X^n\longleftrightarrow
\operatorname{diag}(\xi_+^n,\xi_-^n).
$$
The trace and the determinant are
$$
\operatorname{tr}=\xi_++\xi_-=2x_0,\qquad
\det=\xi_+\xi_-=x_0^2-x_1^2=\langle X\rangle_{*}.
$$
Conjugation exchanges the two coordinates,
$$
X^{\dagger}=\xi_-\Pi_++\xi_+\Pi_-
\longleftrightarrow
\operatorname{diag}(\xi_-,\xi_+),
$$
which is the matrix form of $j\mapsto-j$. The element is a unit exactly when both diagonal entries are nonzero, and a zero divisor exactly when exactly one of them is zero. There is no nonzero nilpotent: a diagonal matrix over $\mathbb{R}$ with square zero is zero, and the off-diagonal matrix units are not in the image.

## Base Changes

**The regular model and the eigenbasis model are two bases of the same plane, and the passage between them is the conjugation by the matrix of the two idempotents.**

### The Change of Basis of a Matrix Model

Let $P\in GL_2(\mathbb{R})$ have as columns the coordinates of a new basis in the old one. The matrix of the same endomorphism in the new basis is
$$
M'=P^{-1}MP.
$$
The trace and the determinant are unchanged,
$$
\operatorname{tr}M'=\operatorname{tr}M,\qquad
\det M'=\det M,
$$
and so are the characteristic polynomial, the spectrum, the rank and the Jordan form. An idempotent is conjugated to an idempotent, a nilpotent to a nilpotent, and the two eigenspaces to the two coordinate axes. The columns of $P$ are the new basis vectors; a column that is an eigenvector of $M$ produces a column of $P^{-1}MP$ with the eigenvalue on the diagonal.

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
Its columns are eigenvectors of $\mathsf{M}_2(Q)$:
$$
\mathsf{M}_2(Q)\begin{pmatrix}1/2\\1/2\end{pmatrix}
=\lambda_+\begin{pmatrix}1/2\\1/2\end{pmatrix},
\qquad
\mathsf{M}_2(Q)\begin{pmatrix}1/2\\-1/2\end{pmatrix}
=\lambda_-\begin{pmatrix}1/2\\-1/2\end{pmatrix}.
$$
Therefore
$$
\mathsf{C}^{-1}\mathsf{M}_2(Q)\mathsf{C}
=\operatorname{diag}(\lambda_+,\lambda_-)
=\mathsf{M}_2^{\Pi}(Q),
$$
and, for every element $X$,
$$
\mathsf{M}_2^{\Pi}(X)=\mathsf{C}^{-1}\mathsf{M}_2(X)\mathsf{C}.
$$
The first column of $\mathsf{C}$ is the first column of $\rho_+$; the second is the negative of the second column of $\rho_-$. The columns are the nonzero columns of the two spectral projectors, normalised to have entries $\pm\tfrac12$.

**The inverse change.** The inverse matrix has integer entries and determinant $-2$:
$$
\mathsf{C}^{-1}=
\begin{pmatrix}1&1\\1&-1\end{pmatrix}
=2\mathsf{C}.
$$
It sends the diagonal model back to the regular one, and its columns are the coordinates of $1,j$ in the eigenbasis.

### The Freedom of the Change

The diagonalising matrix is not unique. If $\mathsf{C}$ diagonalises $\mathsf{M}_2(Q)$, then so does $\mathsf{C}D$ for every invertible diagonal $D=\operatorname{diag}(\alpha,\beta)$:
$$
(\mathsf{C}D)^{-1}\mathsf{M}_2(Q)(\mathsf{C}D)
=D^{-1}\operatorname{diag}(\lambda_+,\lambda_-)D
=\operatorname{diag}(\lambda_+,\lambda_-).
$$
The two scales are the two independent rescalings of the eigenvectors. A common scale leaves the conjugation unchanged; a relative scale multiplies the two columns by $\alpha$ and $\beta$, and the diagonal model is unchanged because diagonal matrices commute with $D$. In the algebra, the general eigenbasis is
$$
(\alpha\Pi_+,\beta\Pi_-),
\qquad
\alpha,\beta\in\mathbb{R}^{\times},
$$
and the normalised pair is $\alpha=\beta=1$. When $q'=0$ the eigenvalues coincide, every nonzero vector is an eigenvector, every basis is an eigenbasis, and the change matrix is an arbitrary invertible matrix.

**What depends on $Q$.** The change matrix $\mathsf{C}$ and the diagonal matrix $\operatorname{diag}(\lambda_+,\lambda_-)$ depend on $Q$ through $q'$: the two eigenvectors are fixed only when the two eigenvalues are distinct. The regular model $\mathsf{M}_2$ and the assignment on the basis do not depend on $Q$. The eigenbasis model is the same assignment for every $Q$ with $q'\neq0$; the dependence is carried by the eigenvalues, not by the basis. This is the structural difference with the biquaternion case, where the eigenbasis itself depends on the element.

### The Two Normal Forms

The regular model and the eigenbasis model are the two normal forms of the same matrix under conjugation. The first is the **element model**: the matrix entries are the coefficients of the element in the basis $1,j$. The second is the **spectral model**: the matrix entries are the two eigenvalues. The two are related by $\mathsf{C}$, and the relation is the diagonalisation of every element at once, because the algebra is commutative. In the biquaternion case no single change diagonalises every element, and the corresponding matrix $\mathsf{C}_Q$ depends on $Q$.

**The complexified change.** After extension of scalars, the same matrix $\mathsf{C}$ has complex entries (in fact real entries), and it diagonalises the complexified regular matrix. The complexified eigenbasis is the pair of complex lines $\mathbb{C}\Pi_+$ and $\mathbb{C}\Pi_-$, and the change is the same $\mathsf{C}$ read over $\mathbb{C}$. The determinant is still $-\tfrac12$, and the inverse is still $2\mathsf{C}$.

## Spinors and the Columns

**The two columns of the eigenbasis model are the two spinor spaces, and a spinor is one real coefficient on one of them.**

Since $\mathbb{D}$ is commutative, the left, right and two-sided ideals coincide. The minimal nonzero ideals are
$$
S_+=\mathbb{D}\Pi_+=\mathbb{R}\Pi_+,
\qquad
S_-=\mathbb{D}\Pi_-=\mathbb{R}\Pi_-,
$$
each one-dimensional, and $\mathbb{D}=S_+\oplus S_-$. In the eigenbasis model they are the two columns:
$$
S_+\longleftrightarrow\left\{\begin{pmatrix}\alpha&0\\0&0\end{pmatrix}:\alpha\in\mathbb{R}\right\},
\qquad
S_-\longleftrightarrow\left\{\begin{pmatrix}0&0\\0&\beta\end{pmatrix}:\beta\in\mathbb{R}\right\}.
$$
A spinor of first chirality is $\xi_+=\alpha\Pi_+$ and is represented by the first column $(\alpha,0)^{\mathsf T}$; a spinor of second chirality is $\xi_-=\beta\Pi_-$ and is represented by the second column $(0,\beta)^{\mathsf T}$. The general element is the sum of one spinor of each chirality, and its two coordinates are the two diagonal entries.

Under multiplication by $Q$ the two columns are scaled independently:
$$
Q\xi_+=\lambda_+\xi_+
\longleftrightarrow
\begin{pmatrix}\lambda_+&0\\0&0\end{pmatrix}
\begin{pmatrix}\alpha\\0\end{pmatrix}
=
\begin{pmatrix}\lambda_+\alpha\\0\end{pmatrix},
\qquad
Q\xi_-=\lambda_-\xi_-
\longleftrightarrow
\begin{pmatrix}0&0\\0&\lambda_-\end{pmatrix}
\begin{pmatrix}0\\\beta\end{pmatrix}
=
\begin{pmatrix}0\\\lambda_-\beta\end{pmatrix}.
$$
The same diagonal matrix $\operatorname{diag}(\lambda_+,\lambda_-)$ acts on both columns; on the first column only the first entry survives, on the second only the second. This is the precise sense in which the two spinor spaces are the two eigenspaces.

**Right multiplication.** Since the algebra is commutative, right multiplication by $Q$ acts exactly as left multiplication, and the rows are the same two lines. The matrix is symmetric, so the row picture and the column picture coincide. This is the split-complex difference with the biquaternion case, where the rows are the two minimal right ideals and the columns the two minimal left ideals, and the two pictures are different.

## The $4\times4$ Matrix Element Representation

**The $4\times4$ matrix is the real regular representation of the complexification $\mathbb{D}_{\mathbb{C}}$, not of $\mathbb{D}$ itself.**

The algebra $\mathbb{D}$ has real dimension two, so its faithful regular representation is the $2\times2$ model. The complexification
$$
\mathbb{D}_{\mathbb{C}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{D}
\cong\mathbb{C}[j]/(j^2-1)
\cong\mathbb{C}\times\mathbb{C}
$$
has complex dimension two, hence real dimension four, and its real regular representation is a $4\times4$ real matrix. On the real basis
$$
1,\qquad i,\qquad j,\qquad ij,
$$
with $i$ the central complex unit, an element is
$$
X=q+jq',\qquad q=a+ib,\quad q'=c+id,
$$
and left multiplication has the matrix
$$
\mathsf{M}_4(X)=
\begin{pmatrix}
a&-b&c&-d\\
b&a&d&c\\
c&-d&a&-b\\
d&c&b&a
\end{pmatrix}.
$$
The matrix is the realification of the complex $2\times2$ matrix
$$
\mathsf{M}_2^{\mathbb{C}}(X)=
\begin{pmatrix}q&q'\\q'&q\end{pmatrix}
\in M_2(\mathbb{C}),
$$
in the real basis $1,i,j,ij$: each complex entry $q=a+ib$ becomes the real block $\begin{pmatrix}a&-b\\b&a\end{pmatrix}$, and the two diagonal blocks are the two copies of $q$ and $q'$. The map is an injective homomorphism of $\mathbb{R}$-algebras, and
$$
\operatorname{tr}\mathsf{M}_4(X)=4a,\qquad
\det\mathsf{M}_4(X)=\lvert q^2-q'^2\rvert^2
=\lvert\lambda_+\lambda_-\rvert^2.
$$
The determinant is the square of the complex modulus of the norm, because the $4\times4$ matrix is the realification of the $2\times2$ complex matrix.

**The idempotent coordinates.** In the complexified eigenbasis, the element is
$$
X=\xi_+\Pi_++\xi_-\Pi_-,
\qquad
\xi_\pm=q\pm q',
$$
and the $2\times2$ complex matrix is $\operatorname{diag}(\xi_+,\xi_-)$. The realification of this diagonal matrix is block diagonal,
$$
\mathsf{M}_4(X)\sim
\begin{pmatrix}
\operatorname{Re}\xi_+&-\operatorname{Im}\xi_+&0&0\\
\operatorname{Im}\xi_+&\operatorname{Re}\xi_+&0&0\\
0&0&\operatorname{Re}\xi_-&-\operatorname{Im}\xi_-\\
0&0&\operatorname{Im}\xi_-&\operatorname{Re}\xi_-
\end{pmatrix},
$$
in the real basis adapted to the two complex lines. For $X=Q$ the two blocks are the two complex eigenvalues $\lambda_\pm$, each read as a real $2\times2$ rotation-dilation block. The four real eigenvalues are $\lambda_+,\overline{\lambda_+},\lambda_-,\overline{\lambda_-}$, with the bar the complex conjugation of the complexified scalar, not the split-complex conjugation.

**The change of basis.** The real change matrix is the realification of $\mathsf{C}$ written in the real basis $1,i,j,ij$:
$$
\mathsf{C}_4=
\begin{pmatrix}
\tfrac12&0&\tfrac12&0\\
0&\tfrac12&0&\tfrac12\\
\tfrac12&0&-\tfrac12&0\\
0&\tfrac12&0&-\tfrac12
\end{pmatrix},
$$
whose columns are the coordinate columns of $\Pi_+,i\Pi_+,\Pi_-,i\Pi_-$. It satisfies
$$
\mathsf{C}_4^{-1}\mathsf{M}_4(Q)\mathsf{C}_4
=
\begin{pmatrix}
\operatorname{Re}\lambda_+&-\operatorname{Im}\lambda_+&0&0\\
\operatorname{Im}\lambda_+&\operatorname{Re}\lambda_+&0&0\\
0&0&\operatorname{Re}\lambda_-&-\operatorname{Im}\lambda_-\\
0&0&\operatorname{Im}\lambda_-&\operatorname{Re}\lambda_-
\end{pmatrix}.
$$
Over $\mathbb{C}$ this block matrix is diagonalised by the further change with columns $(1,-i)$ and $(1,i)$ in each block, giving $\operatorname{diag}(\lambda_+,\overline{\lambda_+},\lambda_-,\overline{\lambda_-})$. The determinant of $\mathsf{C}_4$ is $(\det\mathsf{C})^2=\tfrac14$, the square of the determinant of the complex change, which is the general rule for the realification: $\det\mathsf{C}_4=\lvert\det\mathsf{C}\rvert^2$.

**What the $4\times4$ model adds.** The $4\times4$ model does not add a new representation of $\mathbb{D}$: it is the $2\times2$ complex model read over $\mathbb{R}$, and its eigenbasis is the realified complex eigenbasis. It adds the real geometry of the two complex eigenvalues: each eigenvalue becomes a $2\times2$ block, the two blocks are independent, and the four real eigenvalues are the two complex eigenvalues together with their complex conjugates. This is the split-complex analogue of the $4\times4$ regular matrices of the biquaternion case, where the four eigenvalues are the two $\lambda_\pm$, each repeated twice.

## Summary

**The $2\times2$ model.** The regular matrix is $\mathsf{M}_2(X)=\begin{pmatrix}x_0&x_1\\x_1&x_0\end{pmatrix}$, with determinant the norm and trace twice the scalar part. The eigenprojections are the two rank-one matrices $\rho_\pm=\tfrac12\begin{pmatrix}1&\pm1\\ \pm1&1\end{pmatrix}$, and the eigenbasis model is
$$
\mathsf{M}_2^{\Pi}(Q)=\operatorname{diag}(\lambda_+,\lambda_-).
$$

**The base change.** The two models are related by
$$
\mathsf{M}_2^{\Pi}(X)=\mathsf{C}^{-1}\mathsf{M}_2(X)\mathsf{C},
\qquad
\mathsf{C}=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
\mathsf{C}^{-1}=\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
$$
The change is unique up to the two independent rescalings of the two eigenvectors. It is the same matrix for every element, because the algebra is commutative and the eigenbasis is fixed by $j$.

**The $4\times4$ model.** The real regular matrix of the complexification is the realification of the complex $2\times2$ matrix; in the idempotent coordinates it is block diagonal with the two complex eigenvalues, and the realified $\mathsf{C}$ block-diagonalises it. The four real eigenvalues are $\lambda_+,\overline{\lambda_+},\lambda_-,\overline{\lambda_-}$.

**The limits.** For $q'=0$ the two eigenvalues coincide, the eigenbasis is not unique, every basis is an eigenbasis, and the change matrix is an arbitrary invertible matrix. For $q'=\pm q$ one eigenvalue vanishes, the element is a zero divisor, and the corresponding spectral projector has rank one with one zero eigenvalue; the matrices remain diagonalisable. There is no nonzero nilpotent in any regime, so the nilpotent construction of the biquaternion case has no analogue here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2$ | Left regular matrix in the basis $1,j$ |
| $\mathsf{M}_2^{\Pi}$ | Matrix in the eigenbasis $(\Pi_+,\Pi_-)$ |
| $\mathsf{M}_2^{\mathbb{C}}$ | Complexified $2\times2$ regular matrix |
| $\mathsf{M}_4$ | Real regular matrix of $\mathbb{D}_{\mathbb{C}}$ in the basis $1,i,j,ij$ |
| $\mathsf{C}$ | Change matrix from $1,j$ to $\Pi_+,\Pi_-$ |
| $\mathsf{C}_4$ | Realification of $\mathsf{C}$, the $4\times4$ change |
| $\rho_\pm$ | Spectral projectors $\mathsf{M}_2(\Pi_\pm)$ |
| $S_\pm=\mathbb{R}\Pi_\pm$ | The two spinor spaces, the two columns |
| $\lambda_\pm=q\pm q'$ | The two eigenvalues |
| $\langle X\rangle_{*}=x_0^2-x_1^2$ | The split-complex norm, the determinant of $\mathsf{M}_2(X)$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for idempotents, Peirce decompositions and the matrix units of a Peirce decomposition.
- Fuzhen Zhang, *Matrix Theory: Basic Results and Techniques*, 2nd edition (Springer, 2011), for the change of basis, the spectral projectors and the realification of a complex matrix.
