# __The Spectrally Regular Sector and Eigenbasis of a Biquaternion in Matrix Element Representations__

## Introduction

The eigenbasis of a biquaternion $\tilde Q=Q_te_t+\vec Q$ is the basis
$$
\tilde\Pi_+,\qquad \vec\Upsilon_-,\qquad \vec\Upsilon_+,\qquad \tilde\Pi_-
$$
of the Peirce decomposition of its eigenprojections, in which the left regular matrix of $\tilde Q$ is diagonal with eigenvalues $\lambda_+,\lambda_+,\lambda_-,\lambda_-$. The basis and the construction of the nilpotents are *The Spectrally Regular Sector and Construction of the Eigenbasis of a Biquaternion*; the spectral criterion is *Spectral Regularity and Degeneracy in the Biquaternion Algebra*; the eigenvalue decomposition is *The Biquaternion Eigenvalue Decomposition*, §*The Eigenprojectors*.

This article owns the **$4\times4$ left and right regular representations** $\mathsf{M}_4^{L},\mathsf{M}_4^{R}:\mathbb{B}\to M_4(\mathbb{C})$ of *Introduction to the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*. The regular matrices carry the multiplication on the four-vector space; in the eigenbasis order they are Kronecker products of the $2\times2$ Peirce matrix with an identity, and for $\tilde Q$ itself they are diagonal with the eigenvalues repeated twice.

The $2\times2$ model $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ was formerly treated in this article. It is now treated in the articles of the $M_2(\mathbb{C})$ group: *$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure* for the assignment and the isomorphism, *$M_2(\mathbb{C})$ Representation : The Spectral Projectors and the Nilpotents* for the eigenprojectors and the mixed corners, and *$M_2(\mathbb{C})$ Representation : The Eigenbasis and the Diagonalising Matrix* for the diagonalising matrix and its freedom. This article retains the $2\times2$ statements only where the $4\times4$ matrices use them, and it refers to those articles for their proofs.

| Question | $4\times4$ answer |
|---|---|
| left regular matrix | $\mathsf{M}_4^{L}(\tilde Q)$, columns $\tilde Q e_\mu$ |
| right regular matrix | $\mathsf{M}_4^{R}(\tilde Q)$, columns $e_\mu\tilde Q$ |
| eigenbasis order | $[L_{\tilde Q_{\mathrm{sp}}}]_{\mathrm Q}=\mathsf{M}_2^{Q}(\tilde Q_{\mathrm{sp}})\otimes \mathrm I_2$, $[R_{\tilde Q_{\mathrm{sp}}}]_{\mathrm Q}=\mathrm I_2\otimes \mathsf{M}_2^{Q}(\tilde Q_{\mathrm{sp}})^{\mathsf T}$ |
| diagonal form | $\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$ for $L_{\tilde Q}$ and $\operatorname{diag}(\lambda_+,\lambda_-,\lambda_+,\lambda_-)$ for $R_{\tilde Q}$ |
| multiplicity | each eigenvalue of the $2\times2$ matrix occurs twice |

**Conventions.** The base and the elements are those of *Conventions in Mathematics*: $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, $B=\sqrt{Q_x^2+Q_y^2+Q_z^2}$, $\vec\Xi=-i\vec Q/B$, $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$, $\lambda_\pm=Q_t\pm iB$. A general element distinct from $\tilde Q$ is written $\tilde Q_{\mathrm{sp}}$. The fixed $2\times2$ model is $\mathsf{M}_2$; the eigenbasis model is $\mathsf{M}_2^{Q}$; the regular matrices are $\mathsf{M}_4^{L}$ and $\mathsf{M}_4^{R}$, with the shorter $\mathsf{M}_4=\mathsf{M}_4^{L}$.

**Boundaries.** The spectral criterion and the cone are *Spectral Regularity and Degeneracy in the Biquaternion Algebra*; the construction of the basis is *The Spectrally Regular Sector and Construction of the Eigenbasis of a Biquaternion*; the Peirce decomposition is *Ideals and Peirce Decompositions of the Biquaternion Algebra*. The $2\times2$ assignment is *$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure*; the projectors and nilpotents are *$M_2(\mathbb{C})$ Representation : The Spectral Projectors and the Nilpotents*; the diagonalising matrix is *$M_2(\mathbb{C})$ Representation : The Eigenbasis and the Diagonalising Matrix*. The $4\times4$ assignment is *Introduction to the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*; the matrix algebra is *Matrix Algebras*.

## The $2\times2$ Matrix Element Representation

The $2\times2$ model is the fixed isomorphism of *$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure*. The spectral projectors are $\rho_\pm=\mathsf{M}_2(\tilde\Pi_\pm)$ and the spectral nilpotents are $\mathsf{M}_2(\vec\Upsilon_\pm)$; their construction and their Peirce products are *$M_2(\mathbb{C})$ Representation : The Spectral Projectors and the Nilpotents*. The eigenbasis model $\mathsf{M}_2^{Q}$ and the diagonalising matrix $\mathsf{C}_Q$ are *$M_2(\mathbb{C})$ Representation : The Eigenbasis and the Diagonalising Matrix*, and the columns and the spinor module are *$M_2(\mathbb{C})$ Representation : The Columns, the Rows and the Spinor Module*.

The only $2\times2$ statements used below are the assignment itself, the four matrix units, and the multiplication table of the eigenbasis. They are recalled where they enter, and they are not reproved.

## The $4\times4$ Matrix Element Representation

**The left and right regular matrices carry the multiplication on the four-vector space, and in the eigenbasis order they are Kronecker products of the $2\times2$ Peirce matrix with an identity.**

### The Regular Matrices

In the fixed basis $e_t,\vec e_x,\vec e_y,\vec e_z$, the **left regular matrix** $\mathsf{M}_4^{L}(\tilde Q_{\mathrm{sp}})$ has as $\mu$-th column the coordinate column of $\tilde Q_{\mathrm{sp}}e_\mu$:
$$
\mathsf{M}_4^{L}(\tilde Q_{\mathrm{sp}})=
\begin{pmatrix}
Q_{\mathrm{sp},t}&-Q_{\mathrm{sp},x}&-Q_{\mathrm{sp},y}&-Q_{\mathrm{sp},z}\\
Q_{\mathrm{sp},x}&Q_{\mathrm{sp},t}&-Q_{\mathrm{sp},z}&Q_{\mathrm{sp},y}\\
Q_{\mathrm{sp},y}&Q_{\mathrm{sp},z}&Q_{\mathrm{sp},t}&-Q_{\mathrm{sp},x}\\
Q_{\mathrm{sp},z}&-Q_{\mathrm{sp},y}&Q_{\mathrm{sp},x}&Q_{\mathrm{sp},t}
\end{pmatrix}.
$$
The **right regular matrix** $\mathsf{M}_4^{R}(\tilde Q_{\mathrm{sp}})$ has as $\mu$-th column the coordinate column of $e_\mu\tilde Q_{\mathrm{sp}}$:
$$
\mathsf{M}_4^{R}(\tilde Q_{\mathrm{sp}})=
\begin{pmatrix}
Q_{\mathrm{sp},t}&-Q_{\mathrm{sp},x}&-Q_{\mathrm{sp},y}&-Q_{\mathrm{sp},z}\\
Q_{\mathrm{sp},x}&Q_{\mathrm{sp},t}&Q_{\mathrm{sp},z}&-Q_{\mathrm{sp},y}\\
Q_{\mathrm{sp},y}&-Q_{\mathrm{sp},z}&Q_{\mathrm{sp},t}&Q_{\mathrm{sp},x}\\
Q_{\mathrm{sp},z}&Q_{\mathrm{sp},y}&-Q_{\mathrm{sp},x}&Q_{\mathrm{sp},t}
\end{pmatrix}.
$$
They satisfy
$$
\mathsf{M}_4^{L}(\tilde Q_{\mathrm{sp}})\mathsf{M}_4^{L}(\tilde Q_3)=\mathsf{M}_4^{L}(\tilde Q_{\mathrm{sp}}\tilde Q_3),
\qquad
\mathsf{M}_4^{R}(\tilde Q_{\mathrm{sp}})\mathsf{M}_4^{R}(\tilde Q_3)=\mathsf{M}_4^{R}(\tilde Q_3\tilde Q_{\mathrm{sp}}),
$$
and
$$
\operatorname{Tr}\mathsf{M}_4^{L}(\tilde Q_{\mathrm{sp}})=4Q_{\mathrm{sp},t},
\qquad
\det\mathsf{M}_4^{L}(\tilde Q_{\mathrm{sp}})=\langle\tilde Q_{\mathrm{sp}}\rangle_{\natural}^2.
$$
The left matrix is multiplicative and the right matrix is anti-multiplicative; both are injective, and the left one alone is the regular representation of the algebra.

### The Eigenbasis Order

Write $M=\mathsf{M}_2^{Q}(\tilde Q_{\mathrm{sp}})$. In the eigenbasis order
$$
(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)
$$
the two regular matrices are block matrices:
$$
[L_{\tilde Q_{\mathrm{sp}}}]_{\mathrm Q}=
\begin{pmatrix}
Q_{\mathrm{sp},11}&0&Q_{\mathrm{sp},12}&0\\
0&Q_{\mathrm{sp},11}&0&Q_{\mathrm{sp},12}\\
Q_{\mathrm{sp},21}&0&Q_{\mathrm{sp},22}&0\\
0&Q_{\mathrm{sp},21}&0&Q_{\mathrm{sp},22}
\end{pmatrix}
=M\otimes\mathrm I_2,
$$
$$
[R_{\tilde Q_{\mathrm{sp}}}]_{\mathrm Q}=
\begin{pmatrix}
Q_{\mathrm{sp},11}&Q_{\mathrm{sp},21}&0&0\\
Q_{\mathrm{sp},12}&Q_{\mathrm{sp},22}&0&0\\
0&0&Q_{\mathrm{sp},11}&Q_{\mathrm{sp},21}\\
0&0&Q_{\mathrm{sp},12}&Q_{\mathrm{sp},22}
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
[L_{\tilde Q_{\mathrm{sp}}}]_{\mathrm{col}}=
\begin{pmatrix}M&0\\0&M\end{pmatrix}
=\mathrm I_2\otimes M,
\qquad
[R_{\tilde Q_{\mathrm{sp}}}]_{\mathrm{col}}=
\begin{pmatrix}
Q_{\mathrm{sp},11}\mathrm I_2&Q_{\mathrm{sp},21}\mathrm I_2\\
Q_{\mathrm{sp},12}\mathrm I_2&Q_{\mathrm{sp},22}\mathrm I_2
\end{pmatrix}
=M^{\mathsf T}\otimes\mathrm I_2.
$$
Left multiplication preserves each left ideal $S_\pm$ and acts on each by $M$, so $[L]_{\mathrm{col}}$ is block diagonal. Right multiplication does not preserve the left ideals; it mixes $S_+$ and $S_-$ according to the entries of $M$, so $[R]_{\mathrm{col}}$ is not block diagonal. The two orders differ by the permutation of the second and third basis vectors. In the eigenbasis order the blocks are the right ideals and the right matrix is block diagonal; in the column order the blocks are the left ideals and the left matrix is block diagonal. The two block forms record the right-ideal decomposition $\mathbb{B}=\tilde\Pi_+\mathbb{B}\oplus\tilde\Pi_-\mathbb{B}$ and the left-ideal decomposition $\mathbb{B}=S_+\oplus S_-$, which are different groupings of the same four basis vectors.

### The Four Basis Elements in the Eigenbasis

**The four elements of the eigenbasis order have the four elementary matrices for left multiplication, and the fixed basis has four constant matrices in the standard eigenbasis.**

In the order $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ the left regular matrices are the Kronecker products $\mathsf M_2^{Q}(P)\otimes\mathrm I_2$ of the four matrices of the $2\times2$ table with the identity:
$$
[L_{\tilde\Pi_+}]_{\mathrm Q}=\operatorname{diag}(1,1,0,0),
\qquad
[L_{\tilde\Pi_-}]_{\mathrm Q}=\operatorname{diag}(0,0,1,1),
$$
$$
[L_{\vec\Upsilon_-}]_{\mathrm Q}=
\begin{pmatrix}
0&0&1&0\\
0&0&0&1\\
0&0&0&0\\
0&0&0&0
\end{pmatrix},
\qquad
[L_{\vec\Upsilon_+}]_{\mathrm Q}=
\begin{pmatrix}
0&0&0&0\\
0&0&0&0\\
1&0&0&0\\
0&1&0&0
\end{pmatrix}.
$$
The right regular matrices are the same units on the other factor:
$$
[R_{\tilde\Pi_+}]_{\mathrm Q}=\operatorname{diag}(1,0,1,0),
\qquad
[R_{\tilde\Pi_-}]_{\mathrm Q}=\operatorname{diag}(0,1,0,1),
$$
$$
[R_{\vec\Upsilon_-}]_{\mathrm Q}=
\begin{pmatrix}
0&0&0&0\\
1&0&0&0\\
0&0&0&0\\
0&0&1&0
\end{pmatrix},
\qquad
[R_{\vec\Upsilon_+}]_{\mathrm Q}=
\begin{pmatrix}
0&1&0&0\\
0&0&0&0\\
0&0&0&1\\
0&0&0&0
\end{pmatrix}.
$$
These eight matrices are the multiplication table of the four basis elements. The four left matrices reproduce the Peirce relations
$$
[L_{\vec\Upsilon_+}][L_{\vec\Upsilon_-}]=[L_{\tilde\Pi_-}],
\qquad
[L_{\vec\Upsilon_-}][L_{\vec\Upsilon_+}]=[L_{\tilde\Pi_+}],
\qquad
[L_{\vec\Upsilon_\pm}]^2=0,
\qquad
[L_{\tilde\Pi_+}]+[L_{\tilde\Pi_-}]=\mathrm I_4,
$$
and the four right matrices satisfy the same relations with the two factors in the reverse order, because $[R_P][R_{P'}]$ is the matrix of $P'P$.

**The fixed basis in the standard eigenbasis.** At $Q_x=Q_y=0$ with the standard root $i\vec e_z$, that is $B=-Q_z$, the change matrix of §*The Fixed Change in the $4\times4$ Model* is
$$
\mathsf C_4^{(0)}=
\frac12
\begin{pmatrix}
1&0&0&1\\
0&i&i&0\\
0&-1&1&0\\
i&0&0&-i
\end{pmatrix},
\qquad
(\mathsf C_4^{(0)})^{-1}=
\begin{pmatrix}
1&0&0&-i\\
0&-i&-1&0\\
0&-i&1&0\\
1&0&0&i
\end{pmatrix}.
$$
The columns of $(\mathsf C_4^{(0)})^{-1}$ are the coordinate columns of the fixed basis in the eigenbasis:
$$
[e_t]=(1,0,0,1),\quad
[\vec e_x]=(0,-i,-i,0),\quad
[\vec e_y]=(0,-1,1,0),\quad
[\vec e_z]=(-i,0,0,i).
$$
Conjugating the fixed regular matrices gives the four matrices of the fixed basis in the eigenbasis:
$$
(\mathsf C_4^{(0)})^{-1}\mathsf M_4^{L}(e_t)\mathsf C_4^{(0)}=\mathrm I_4,
$$
$$
(\mathsf C_4^{(0)})^{-1}\mathsf M_4^{L}(\vec e_x)\mathsf C_4^{(0)}=
\begin{pmatrix}
0&0&-i&0\\
0&0&0&-i\\
-i&0&0&0\\
0&-i&0&0
\end{pmatrix},
\qquad
(\mathsf C_4^{(0)})^{-1}\mathsf M_4^{L}(\vec e_y)\mathsf C_4^{(0)}=
\begin{pmatrix}
0&0&-1&0\\
0&0&0&-1\\
1&0&0&0\\
0&1&0&0
\end{pmatrix},
$$
$$
(\mathsf C_4^{(0)})^{-1}\mathsf M_4^{L}(\vec e_z)\mathsf C_4^{(0)}=
\begin{pmatrix}
-i&0&0&0\\
0&-i&0&0\\
0&0&i&0\\
0&0&0&i
\end{pmatrix}.
$$
In the $2\times2$ model the same four elements are
$$
\mathsf M_2^{Q}(e_t)=\mathrm I_2,\qquad
\mathsf M_2^{Q}(\vec e_x)=
\begin{pmatrix}0&-i\\-i&0\end{pmatrix},
\qquad
\mathsf M_2^{Q}(\vec e_y)=
\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
\mathsf M_2^{Q}(\vec e_z)=
\begin{pmatrix}-i&0\\0&i\end{pmatrix},
$$
and $[L_{P}]_{\mathrm Q}=\mathsf M_2^{Q}(P)\otimes\mathrm I_2$ returns the four $4\times4$ matrices above. In the standard case the eigenbasis model is the fixed model itself: the assignment of *$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure* already sends $\tilde\Pi_{\pm,0}$ to $\operatorname{diag}(1,0)$ and $\operatorname{diag}(0,1)$, and the standard nilpotents to the two off-diagonal matrices with a single $1$, so the four matrices above are the four matrices displayed there. They satisfy
$$
\mathsf M_2^{Q}(\vec e_x)^2=\mathsf M_2^{Q}(\vec e_y)^2=\mathsf M_2^{Q}(\vec e_z)^2=-\mathrm I_2,
\qquad
\mathsf M_2^{Q}(\vec e_x)\mathsf M_2^{Q}(\vec e_y)=\mathsf M_2^{Q}(\vec e_z),
$$
which are the relations $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ of the fixed basis. Off the axis the identity $[L_P]_{\mathrm Q}=\mathsf M_2^{Q}(P)\otimes\mathrm I_2$ holds with $\mathsf M_2^{Q}(\vec e_\mu)$ the Peirce matrix of $\vec e_\mu$ in the general eigenbasis model, which is full.

### The Diagonal Form

For $\tilde Q_{\mathrm{sp}}=\tilde Q$ the Peirce matrix is $M=\operatorname{diag}(\lambda_+,\lambda_-)$, and the two regular matrices become diagonal:
$$
\boxed{\; [L_{\tilde Q}]_{\mathrm Q}=\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-),
\qquad
[R_{\tilde Q}]_{\mathrm Q}=\operatorname{diag}(\lambda_+,\lambda_-,\lambda_+,\lambda_-) \;}
$$
These are the matrices of the eigenbasis of left multiplication and of right multiplication of *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*The Eigenbasis of Left Multiplication*, read in the $4\times4$ representation. The eigenvalues of $L_{\tilde Q}$ are $\lambda_+,\lambda_+,\lambda_-,\lambda_-$; the eigenvalues of $R_{\tilde Q}$ are $\lambda_+,\lambda_-,\lambda_+,\lambda_-$. The two multiplicities are the dimensions of the two spinor spaces.

**The trace and the determinant in the diagonal form.** The trace of $L_{\tilde Q}$ is $2(\lambda_++\lambda_-)=4Q_t$, the trace of $R_{\tilde Q}$ is the same, the determinant of $L_{\tilde Q}$ is $\lambda_+^2\lambda_-^2=\langle\tilde Q\rangle_{\natural}^2$, and the determinant of $R_{\tilde Q}$ is the same product in the other order. The two matrices have the same characteristic polynomial,
$$
(X-\lambda_+)^2(X-\lambda_-)^2,
$$
which is the square of the characteristic polynomial of $\mathsf{M}_2(\tilde Q)$. The doubling is the doubling of the module: the regular representation is two copies of the $2\times2$ one.

### The Fixed Change in the $4\times4$ Model

The eigenbasis order is reached from the fixed basis by the change-of-basis matrix whose columns are the coordinates of $\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-$ in the fixed basis. For the standard root $i\vec e_z$ and the standard nilpotents of the fixed model, this matrix is
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
when $\tilde Q$ commutes with $\vec e_z$ and the sign of $B$ is chosen so that the root of the eigenbasis is the standard root $i\vec e_z$; for $Q_x=Q_y=0$ this means $B=-Q_z$, so that $\lambda_\pm=Q_t\mp iQ_z$. The four columns are the coordinate columns of the four matrices
$$
\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
\begin{pmatrix}0&0\\1&0\end{pmatrix},\quad
\begin{pmatrix}0&0\\0&1\end{pmatrix}
$$
read back through the inverse of $\mathsf{M}_2^{Q}$. The matrix is fixed because the standard root and the standard nilpotents are fixed.

For a general $\tilde Q$ the change matrix $\mathsf{C}_4(\tilde Q)$ is not fixed: its columns are the coordinates of the eigenbasis, which depends on $\tilde Q$. It satisfies
$$
\mathsf{C}_4(\tilde Q)^{-1}\mathsf{M}_4^{L}(\tilde Q)\mathsf{C}_4(\tilde Q)
=\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-),
$$
$$
\mathsf{C}_4(\tilde Q)^{-1}\mathsf{M}_4^{R}(\tilde Q)\mathsf{C}_4(\tilde Q)
=\operatorname{diag}(\lambda_+,\lambda_-,\lambda_+,\lambda_-).
$$
The two diagonalisations use the same change of basis, because the eigenbasis order diagonalises both the left and the right multiplication. This is the $4\times4$ statement that the eigenbasis is a basis of eigenvectors for both operators.

**The change as a Kronecker product.** In the matrix-unit order the change from the fixed model to the eigenbasis model is the conjugation $X\mapsto\mathsf{C}_Q^{-1}X\mathsf{C}_Q$ on $M_2(\mathbb{C})$. On the four coordinates, with the column-major order
$$
\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
\begin{pmatrix}0&0\\1&0\end{pmatrix},\quad
\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad
\begin{pmatrix}0&0\\0&1\end{pmatrix},
$$
this conjugation is the Kronecker product
$$
\mathsf{C}_Q^{\mathsf T}\otimes\mathsf{C}_Q^{-1}.
$$
The fixed change $\mathsf{C}_4^{(0)}$ is the same construction for the standard root, composed with the fixed passage from the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ to the matrix units. The composition is the reason the $4\times4$ change is not a single Kronecker product in the order of the fixed basis: the fixed basis is not the matrix-unit basis, and the permutation between them is the one displayed in $\mathsf{C}_4^{(0)}$.

### Base Changes in the $4\times4$ Model

A change of basis $P\in GL_4(\mathbb{C})$ acts on the regular matrices by
$$
\mathsf{M}_4^{L}(\tilde Q_{\mathrm{sp}})\longmapsto P^{-1}\mathsf{M}_4^{L}(\tilde Q_{\mathrm{sp}})P,
\qquad
\mathsf{M}_4^{R}(\tilde Q_{\mathrm{sp}})\longmapsto P^{-1}\mathsf{M}_4^{R}(\tilde Q_{\mathrm{sp}})P.
$$
The trace, the determinant, the characteristic polynomial and the spectrum are unchanged. The eigenbasis change is the particular $P=\mathsf{C}_4(\tilde Q)$ that diagonalises both matrices. The basis is fixed by the Peirce conditions: the two idempotents $\tilde\Pi_\pm$ must remain idempotent, so their scales are $1$, and the two nilpotents satisfy $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$ and $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$, so their scales are reciprocal. The only remaining freedom is
$$
\vec\Upsilon_+\longmapsto\mu\vec\Upsilon_+,\qquad
\vec\Upsilon_-\longmapsto\mu^{-1}\vec\Upsilon_-,\qquad
\mu\in\mathbb{C}^{\times},
$$
which leaves the diagonal form and the Peirce multiplication table unchanged. This is the $4\times4$ form of the relative scale of *$M_2(\mathbb{C})$ Representation : The Eigenbasis and the Diagonalising Matrix*, §*The Freedom of the Change*; the common scale of the $2\times2$ diagonaliser is the part that leaves the conjugation unchanged.

**The two models compared.** The $2\times2$ model and the $4\times4$ model carry the same element but different linear objects. The $2\times2$ matrix is the element; the $4\times4$ matrix is the operator of left or right multiplication by the element. The $2\times2$ model is irreducible, the $4\times4$ model is the direct sum of two copies of it, and the eigenvalues of the $4\times4$ matrix are the eigenvalues of the $2\times2$ matrix, each repeated twice. The $2\times2$ model has the two columns for the two spinor spaces; the $4\times4$ model has the two blocks for the two copies, and the eigenbasis order interleaves them.


## Summary

**The $4\times4$ model.** In the eigenbasis order the left and right regular matrices are
$$
[L_{\tilde Q_{\mathrm{sp}}}]_{\mathrm Q}=M\otimes\mathrm I_2,
\qquad
[R_{\tilde Q_{\mathrm{sp}}}]_{\mathrm Q}=\mathrm I_2\otimes M^{\mathsf T},
$$
with $M=\mathsf{M}_2^{Q}(\tilde Q_{\mathrm{sp}})$; for $\tilde Q_{\mathrm{sp}}=\tilde Q$ they are diagonal, with eigenvalues $(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$ and $(\lambda_+,\lambda_-,\lambda_+,\lambda_-)$. The $4\times4$ change of basis is the eigenbasis change, read on the four-vector space.

**The four basis elements.** In the eigenbasis order the four basis elements of the eigenbasis have the four elementary regular matrices,
$$
[L_{\tilde\Pi_+}]_{\mathrm Q}=\operatorname{diag}(1,1,0,0),\quad
[L_{\tilde\Pi_-}]_{\mathrm Q}=\operatorname{diag}(0,0,1,1),\quad
[L_{\vec\Upsilon_-}]_{\mathrm Q}=\begin{pmatrix}0&0&1&0\\0&0&0&1\\0&0&0&0\\0&0&0&0\end{pmatrix},\quad
[L_{\vec\Upsilon_+}]_{\mathrm Q}=\begin{pmatrix}0&0&0&0\\0&0&0&0\\1&0&0&0\\0&1&0&0\end{pmatrix},
$$
and the right matrices are the same units on the other factor. In the standard eigenbasis the fixed basis has the constant matrices
$$
[L_{e_t}]_{\mathrm Q}=\mathrm I_4,\quad
[L_{\vec e_x}]_{\mathrm Q}=\begin{pmatrix}0&0&-i&0\\0&0&0&-i\\-i&0&0&0\\0&-i&0&0\end{pmatrix},\quad
[L_{\vec e_y}]_{\mathrm Q}=\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\1&0&0&0\\0&1&0&0\end{pmatrix},\quad
[L_{\vec e_z}]_{\mathrm Q}=\operatorname{diag}(-i,-i,i,i),
$$
which are the conjugates of the fixed regular matrices by $\mathsf C_4^{(0)}$.

**The limits.** For $Q_x^2+Q_y^2+Q_z^2=0$ the eigenbasis construction fails: there is no spectral projector of rank one attached to $\tilde Q$, no eigenbasis attached to $\tilde Q$, and no diagonal form. The fixed $4\times4$ matrices still exist and still satisfy their multiplicativity; they are not diagonalisable when the nilpotent part is nonzero. The scalar case $\vec Q=0$ has $\mathsf{M}_2(\tilde Q)=Q_t\mathrm I_2$, every basis is an eigenbasis, and the construction from the root is absent although an eigenbasis exists.

**The $2\times2$ counterpart.** The $2\times2$ statements are now in *$M_2(\mathbb{C})$ Representation : The Spectral Projectors and the Nilpotents* and *$M_2(\mathbb{C})$ Representation : The Eigenbasis and the Diagonalising Matrix*. The $4\times4$ matrices are two copies of the $2\times2$ one, and the eigenvalues are doubled accordingly.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2$ | Fixed $2\times2$ matrix element representation $\mathbb{B}\to M_2(\mathbb{C})$ |
| $\mathsf{M}_2^{Q}$ | eigenbasis $2\times2$ model, $\mathsf{M}_2^{Q}(\tilde Q_{\mathrm{sp}})=\mathsf{C}_Q^{-1}\mathsf{M}_2(\tilde Q_{\mathrm{sp}})\mathsf{C}_Q$ |
| $\mathsf{C}_4^{(0)}$ | Fixed change to the standard eigenbasis order in the $4\times4$ model |
| $\mathsf{C}_4(\tilde Q)$ | Change to the eigenbasis order for a general $\tilde Q$ |
| $\mathsf{M}_4^{L},\mathsf{M}_4^{R}$ | Left and right regular matrices in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ |
| $[L_{\tilde Q_{\mathrm{sp}}}]_{\mathrm Q},[R_{\tilde Q_{\mathrm{sp}}}]_{\mathrm Q}$ | Regular matrices in the eigenbasis order |
| $[L_{\tilde Q_{\mathrm{sp}}}]_{\mathrm{col}},[R_{\tilde Q_{\mathrm{sp}}}]_{\mathrm{col}}$ | Regular matrices in the column order |
| $\otimes$ | Kronecker product |

## Further Reading

- [Introduction to the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions](introduction-to-the-4x4-matrix-element-representation-of-biquaternions.html), for the assignment
- [$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure](m2c-representation-the-matrix-product-and-the-algebra-structure.html), for the $2\times2$ assignment
- [$M_2(\mathbb{C})$ Representation : The Spectral Projectors and the Nilpotents](m2c-representation-the-spectral-projectors-and-the-nilpotents.html), for $\rho_\pm$ and the nilpotents
- [$M_2(\mathbb{C})$ Representation : The Eigenbasis and the Diagonalising Matrix](m2c-representation-the-eigenbasis-and-the-diagonalising-matrix.html), for $\mathsf{C}_Q$ and the freedom of the change
- [The Spectrally Regular Sector and Construction of the Eigenbasis of a Biquaternion](the-spectrally-regular-sector-and-construction-of-the-eigenbasis-of-a-biquaternion.html), for the basis and the nilpotents
- [The Spectrally Degenerate Sector](the-spectrally-degenerate-sector.html), for the sector as a whole: the equation, the three strata, the geometry and the failure of the construction.
- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the criterion
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for idempotents, Peirce decompositions and the matrix units of a Peirce decomposition.
- Fuzhen Zhang, *Matrix Theory: Basic Results and Techniques*, 2nd edition (Springer, 2011), for the change of basis, the spectral projectors and the Kronecker product.
