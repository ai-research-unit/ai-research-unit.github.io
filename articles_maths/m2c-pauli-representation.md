# __$M_2(\mathbb{C})$ Pauli Representation__

## Introduction

**The question.** *$M_4(\mathbb{C})$ Pauli Representation* writes the two regular matrices of an element in the standard Peirce frame and finds the same $2\times2$ block twice in each:
$$
L(\tilde Q)=\mathrm I_2\otimes A,\qquad
R(\tilde Q)=A^{\mathsf T}\otimes\mathrm I_2,\qquad
A=\mathsf M_2(\tilde Q),
$$
with the same block $A$ twice on the diagonal of $L$ and $A^{\mathsf T}$ twice on the diagonal of $R$, in the order that pairs the two nilpotents (§*The Left Family* and §*The Right Family* of that article). The second block is a copy of the first, so the $4\times4$ display says nothing that one block does not say. This article asks what one block says on its own: which statements of the $4\times4$ article are statements about $A$, and which are statements about the repetition.

**The compression.** Keeping the block and dropping the repetition gives the $2\times2$ model of the algebra itself. It is not a smaller regular representation: the regular matrices act on the four-dimensional algebra, while the $2\times2$ matrices act on one Peirce plane. The compression is the reading of each action on one plane, and it is exact because the two planes of a copy carry the same matrix.

**The left and the right.** The left/right split survives, but not as two commuting families on one space. The left action on the left ideal
$$
S_+=\mathbb{B}\tilde\Pi_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+
$$
has matrix $A$ in the basis $(\tilde\Pi_+,\vec\Upsilon_+)$. The right action on the right ideal
$$
T_+=\tilde\Pi_+\mathbb{B}=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_-
$$
has matrix $A^{\mathsf T}$ in the basis $(\tilde\Pi_+,\vec\Upsilon_-)$. The two matrices are transposes, and the transpose is the stitch. The two actions live on two different planes, so there is no statement that $A$ and $A^{\mathsf T}$ commute.

**What is kept and what is lost.** The root, the two idempotents, the Peirce frame, the two ideals, the left and right matrices, the stitch, the product, the trace, the determinant and the six subspaces all compress. The axis-free basis switch of the $4\times4$ article does not: the $2\times2$ model is already the matrix-unit frame, so the surviving switch is the identity. The sign matrix of the axis-free basis stitch and the swap matrix of the Peirce stitch are invisible on one block; the swap only exchanges the two nilpotent labels. The commutation of the two $4\times4$ families and the mixed trace $4Q_{1t}Q_{2t}$ do not compress, because they are statements about the two tensor factors at once.

**The algebra.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, with $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$; the central scalar imaginary is $i$. Write $Q_\mu=q_\mu+iq'_\mu$ with $q_\mu,q'_\mu\in\mathbb{R}$, and put $B^2=Q_x^2+Q_y^2+Q_z^2$ and $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2=Q_t^2+Q_x^2+Q_y^2+Q_z^2$.

**The result in one line.** The left matrix is the $2\times2$ image, $L(\tilde Q)=\mathsf M_2(\tilde Q)=A$; the right matrix is its transpose, $R(\tilde Q)=A^{\mathsf T}$. The trace is $2Q_t$. The determinant is $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$. The eigenvalues are $Q_t\pm iB$.

The standard pair and the mixed units are
$$
\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z),\qquad
\vec\Upsilon_+=\tfrac12(i\vec e_x+\vec e_y),\qquad
\vec\Upsilon_-=\tfrac12(i\vec e_x-\vec e_y).
$$
The labels of the Peirce-coordinates article are $\vec\Upsilon_x=\vec\Upsilon_-$ and $\vec\Upsilon_y=\vec\Upsilon_+$. The matrix units are $E_{ij}$, the Pauli matrices are $\sigma_1,\sigma_2,\sigma_3$, and $\operatorname{Tr}$ is the $2\times2$ trace.

**The order of the article.** The article follows the $4\times4$ one step by step, at the size of one block. The root and its two idempotents come first, as the compression of §*The Root and the Peirce Frame* of the $4\times4$ article (§*The Root and the Two Idempotents*), then the Peirce basis in the two orders that the two sides need (§*The Peirce Basis and the Two Orders*). The left and the right matrices are read on the two ideals (§*The Left and Right Matrices*, against §*The Left Family* and §*The Right Family*), then the images of the four units (§*The Images of the Four Units*) and the stitch between the two sides (§*The Stitch Between the Left and the Right*, against §*The Stitch Between the Two Families*). The compression maps and the surviving switch follow (§*The Compression and the Switch*, against §*Every Frame Is a Conjugate of This One*), and then the entry-size quantities: the product, the trace and the determinant (§*The Product*, §*The Trace*, §*The Determinant*). The spectral projectors, the diagonalising matrix, the adjugate and the inverse, and the four norms are new at the element size, with no section of their own in the $4\times4$ article (§*The Spectral Projectors*, §*The Adjugate and the Inverse*, §*The Four Norms*). The six subspaces close the article in their compressed form (§*The Six Subspaces*), and what fails to compress is named at the end of §*The Compression and the Switch*.

**Boundaries.** This article is the continuation of *$M_4(\mathbb{C})$ Pauli Representation*: it takes the block of §*The Left Family* and §*The Right Family* there and follows it to the end. The algebra and the multiplication table are *The Biquaternion Algebra*; the element, its coordinates and the four conjugations are *The Element, the Coordinates and the Conjugations*. The matrix units and the two Peirce planes are *The Polarized Module of the Biquaternion Algebra*. The six subspaces are defined in *Subspaces and Decompositions of the Biquaternion Algebra* and tabulated here in §*The Six Subspaces*.

## The Root and the Two Idempotents

**The root.** The element
$$
\vec\Xi=i\vec e_z
$$
is a vector, and its square is the unit,
$$
\vec\Xi^2=i^2\vec e_z^2=(-1)(-e_t)=e_t .
$$
The two idempotents are the two spectral projections of the root,
$$
\tilde\Pi_\pm=\frac{e_t\pm\vec\Xi}{2}=\tfrac12(e_t\pm i\vec e_z),
$$
with
$$
\tilde\Pi_+^2=\tilde\Pi_+,\qquad
\tilde\Pi_-^2=\tilde\Pi_-,\qquad
\tilde\Pi_+\tilde\Pi_-=0,\qquad
\tilde\Pi_++\tilde\Pi_-=e_t,\qquad
\tilde\Pi_+-\tilde\Pi_-=\vec\Xi .
$$
The root is not central, and the choice of the $z$ direction is a genuine choice.

**The images.** The compression sends the root and the two idempotents to the grading matrix and the two coordinate projections:
$$
\mathsf M_2(\vec\Xi)=\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
\mathsf M_2(\tilde\Pi_+)=E_{11}=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
\mathsf M_2(\tilde\Pi_-)=E_{22}=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
$$
The Peirce decomposition is therefore the spectral decomposition of $\sigma_3$: the abstract pair becomes the row/column pair of $\mathbb{C}^2$. This is the first sense in which the $2\times2$ model is the compressed Pauli representation.

**The two planes.** Put
$$
S_\pm=\mathbb{B}\tilde\Pi_\pm,\qquad
T_\pm=\tilde\Pi_\pm\mathbb{B}.
$$
The $S_\pm$ are the minimal left ideals, the $T_\pm$ are the minimal right ideals, and
$$
S_+\oplus S_-=\mathbb{B}=T_+\oplus T_-.
$$
Left multiplication preserves each $S_\pm$; right multiplication preserves each $T_\pm$. The star maps $S_\pm$ to $T_\pm$,
$$
S_\pm^{*}=T_\pm,
$$
as in *The Polarized Module of the Biquaternion Algebra*, §*The Two Spinor Spaces*.

**The two blocks.** The left action on $S_+$ and the left action on $S_-$ have the same matrix; these are the two diagonal blocks of $L$. The right action on $T_+$ and the right action on $T_-$ have the same matrix; these are the two diagonal blocks of $R$. Keeping one block from each copy gives the $2\times2$ model. The other block is a copy, and no information is lost.

## The Peirce Basis and the Two Orders

**The frame.** The standard Peirce frame is the ordered basis
$$
\mathcal{P}=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-),
\qquad
\vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y).
$$
The multiplication table is
$$
\tilde\Pi_+\tilde\Pi_+=\tilde\Pi_+,\qquad
\tilde\Pi_-\tilde\Pi_-=\tilde\Pi_-,\qquad
\tilde\Pi_+\tilde\Pi_-=\tilde\Pi_-\tilde\Pi_+=0,
$$
$$
\tilde\Pi_+\vec\Upsilon_-=\vec\Upsilon_-,\qquad
\tilde\Pi_-\vec\Upsilon_+=\vec\Upsilon_+,\qquad
\tilde\Pi_+\vec\Upsilon_+=\tilde\Pi_-\vec\Upsilon_-=0,
$$
$$
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,\qquad
\vec\Upsilon_+^2=\vec\Upsilon_-^2=0,
$$
$$
\vec\Upsilon_+\tilde\Pi_+=\vec\Upsilon_+,\qquad
\vec\Upsilon_-\tilde\Pi_-=\vec\Upsilon_-,\qquad
\vec\Upsilon_+\tilde\Pi_-=\vec\Upsilon_-\tilde\Pi_+=0 .
$$
The two mixed units are nilpotent, and each pair multiplies to one of the idempotents.

**The coordinates.** An element written in the frame is
$$
\tilde Q=P_+\tilde\Pi_++X_+\vec\Upsilon_++X_-\vec\Upsilon_-+P_-\tilde\Pi_-,
\qquad P_\pm,X_\pm\in\mathbb{C},
$$
with
$$
P_+=Q_t-iQ_z,\qquad
X_+=-iQ_x+Q_y,\qquad
X_-=-iQ_x-Q_y,\qquad
P_-=Q_t+iQ_z .
$$
The four coordinates are the four entries of the $2\times2$ image,
$$
A=\begin{pmatrix}P_+&X_-\\X_+&P_-\end{pmatrix}=\mathsf M_2(\tilde Q).
$$
This is the coordinate identity, read in the standard pair.

**The matrix-unit order.** The second order is
$$
\mathcal{P}'=(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-).
$$
The images of the four frame vectors are the four matrix units:
$$
\mathsf M_2(\tilde\Pi_+)=E_{11},\qquad
\mathsf M_2(\vec\Upsilon_-)=E_{12},\qquad
\mathsf M_2(\vec\Upsilon_+)=E_{21},\qquad
\mathsf M_2(\tilde\Pi_-)=E_{22}.
$$
In the order $\mathcal{P}$ the images are $(E_{11},E_{21},E_{12},E_{22})$; in the order $\mathcal{P}'$ they are $(E_{11},E_{12},E_{21},E_{22})$, the standard matrix-unit order. The two orders differ by the swap of the two nilpotents,
$$
\vec\Upsilon_+\longleftrightarrow\vec\Upsilon_-,
$$
which is the swap $\mathsf P$ of the $4\times4$ stitch. This is the only frame exchange that survives the compression.

**The two ideal bases.** The left ideals and the right ideals have the bases
$$
S_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+,\qquad
S_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi_-,
$$
$$
T_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_-,\qquad
T_-=\mathbb{C}\vec\Upsilon_+\oplus\mathbb{C}\tilde\Pi_-.
$$
The left bases are the two pairs of $\mathcal{P}$; the right bases are the two pairs of $\mathcal{P}'$. This is the origin of the transpose: the left matrix is read in the $\mathcal{P}$ pairing, the right matrix in the $\mathcal{P}'$ pairing, and the two pairings differ by the exchange of the nilpotents.

## The Left and Right Matrices

**The left matrix.** On $S_+$, in the basis $(\tilde\Pi_+,\vec\Upsilon_+)$, left multiplication by $\tilde Q$ has the matrix $A$. On $S_-$, in the basis $(\vec\Upsilon_-,\tilde\Pi_-)$, it has the same matrix. The two columns in the first basis are
$$
\tilde Q\tilde\Pi_+=P_+\tilde\Pi_++X_+\vec\Upsilon_+,\qquad
\tilde Q\vec\Upsilon_+=X_-\tilde\Pi_++P_-\vec\Upsilon_+,
$$
and the two columns in the second are
$$
\tilde Q\vec\Upsilon_-=P_+\vec\Upsilon_-+X_+\tilde\Pi_-,\qquad
\tilde Q\tilde\Pi_-=X_-\vec\Upsilon_-+P_-\tilde\Pi_- .
$$
In both bases the columns are $(P_+,X_+)$ and $(X_-,P_-)$, so
$$
L(\tilde Q)=\begin{pmatrix}P_+&X_-\\X_+&P_-\end{pmatrix}=A.
$$
The computation in the first basis is the left action on a couple; the second basis repeats it.

**The right matrix.** On $T_+$, in the basis $(\tilde\Pi_+,\vec\Upsilon_-)$, right multiplication by $\tilde Q$ has the matrix $A^{\mathsf T}$. On $T_-$, in the basis $(\vec\Upsilon_+,\tilde\Pi_-)$, it has the same matrix. The two columns in the first basis are
$$
\tilde\Pi_+\tilde Q=P_+\tilde\Pi_++X_-\vec\Upsilon_-,\qquad
\vec\Upsilon_-\tilde Q=X_+\tilde\Pi_++P_-\vec\Upsilon_-,
$$
and the two columns in the second are
$$
\vec\Upsilon_+\tilde Q=P_+\vec\Upsilon_++X_-\tilde\Pi_-,\qquad
\tilde\Pi_-\tilde Q=X_+\vec\Upsilon_++P_-\tilde\Pi_- .
$$
In both bases the columns are $(P_+,X_-)$ and $(X_+,P_-)$, so
$$
R(\tilde Q)=\begin{pmatrix}P_+&X_+\\X_-&P_-\end{pmatrix}=A^{\mathsf T}.
$$
The right matrix is the transpose of the left matrix. This is the whole content of the compression: the left action reads the columns of $A$, the right action reads the rows, and a row written as a column is the transpose.

**The example.** For
$$
\tilde Q=(2+i)e_t+(1-i)\vec e_x+3\vec e_y+i\vec e_z,
$$
the two matrices are
$$
A=\begin{pmatrix}3+i&-4-i\\2-i&1+i\end{pmatrix},\qquad
A^{\mathsf T}=\begin{pmatrix}3+i&2-i\\-4-i&1+i\end{pmatrix}.
$$
The trace is $4+2i=2(2+i)=2Q_t$, and the determinant is
$$
(2+i)^2+(1-i)^2+3^2+i^2=(3+4i)+(-2i)+9-1=11+2i=\langle\tilde Q\rangle_{\natural}.
$$

**A note on the element.** The matrix $A$ is the matrix of the element itself, not a regular matrix on a larger space. The left action is the multiplication by $A$ on the column space of the left ideal; the right action is the multiplication by $A^{\mathsf T}$ on the row space of the right ideal. There is no ambient $4\times4$ space in the compressed model, and the two actions are not two operators on one space.

**Against the $4\times4$ article.** There the same two matrices are §*The Left Family* and §*The Right Family*, displayed as the Kronecker products $\mathrm I_2\otimes A$ and $A^{\mathsf T}\otimes\mathrm I_2$. The compression keeps the block and drops the identity factor. The two bases used above are the two columns of that repeated block: the first block acts on $(\tilde\Pi_+,\vec\Upsilon_+)$, the second on $(\vec\Upsilon_-,\tilde\Pi_-)$, and the two orders $\mathcal{P}$ and $\mathcal{P}'$ of §*The Peirce Basis and the Two Orders* differ by the swap of the two nilpotents.

## The Images of the Four Units

**The left matrices.** The four left matrices are the images of the four units under the model:
$$
\mathsf M_2(e_t)=\mathrm I_2,\qquad
\mathsf M_2(\vec e_x)=-i\sigma_1,\qquad
\mathsf M_2(\vec e_y)=-i\sigma_2,\qquad
\mathsf M_2(\vec e_z)=-i\sigma_3,
$$
that is,
$$
\mathrm I_2,\qquad
-i\sigma_1=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\qquad
-i\sigma_2=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
-i\sigma_3=\begin{pmatrix}-i&0\\0&i\end{pmatrix}.
$$
Each has determinant $1$; the identity has trace $2$ and the three others trace $0$. The four are linearly independent and form a basis of $M_2(\mathbb{C})$.

**Why the factor $i$, and why the signs.** The images must reproduce the two relations that define the algebra. The first is the square,
$$
\mathsf M_2(\vec e_k)^2=\mathsf M_2(\vec e_k^2)=\mathsf M_2(-e_t)=-\mathrm I_2 .
$$
The Pauli matrices are Hermitian and satisfy $\sigma_k^2=\mathrm I_2$, so the image must be $i$ times a Pauli matrix: the factor $i$ is exactly what turns $+\mathrm I_2$ into $-\mathrm I_2$, and without it the image of $\vec e_k$ would square to the image of $e_t$. The second relation is the cross-product,
$$
\vec e_x\vec e_y=\vec e_z .
$$
Since $\sigma_1\sigma_2=i\sigma_3$, the product of the two images is
$$
(-i\sigma_1)(-i\sigma_2)=(-i)^2\sigma_1\sigma_2=-\sigma_1\sigma_2=-i\sigma_3=\mathsf M_2(\vec e_z),
$$
and the signs of the three images are fixed by this line. With the opposite overall sign the same product would give $-i\sigma_3$ while the image of $\vec e_z$ would be $+i\sigma_3$, and the cross-relation would be lost. The factor and the signs are not conventions laid on the algebra: they are the algebra read in matrices.

**The right matrices.** The four right matrices are the transposes:
$$
\mathsf M_2(e_t)^{\mathsf T}=\mathrm I_2,\qquad
\mathsf M_2(\vec e_x)^{\mathsf T}=-i\sigma_1,\qquad
\mathsf M_2(\vec e_y)^{\mathsf T}=i\sigma_2,\qquad
\mathsf M_2(\vec e_z)^{\mathsf T}=-i\sigma_3 .
$$
The matrices $\sigma_1$ and $\sigma_3$ are symmetric, and $\sigma_2$ is antisymmetric, so transposition fixes $\mathrm I_2$, $-i\sigma_1$ and $-i\sigma_3$ and negates $-i\sigma_2$. The right family differs from the left by the sign of the second matrix alone. Each has determinant $1$; the identity has trace $2$ and the three others trace $0$. The four are a basis of $M_2(\mathbb{C})$.

**The two families in one space.** In the $4\times4$ article the left and right families are bases of two different four-dimensional subspaces of $M_4(\mathbb{C})$. In the compressed model both are bases of the same space $M_2(\mathbb{C})$. This is not an identification of the two copies: the left family is read on $S_\pm$, the right family on $T_\pm$, and the two actions remain different. It is the compression of the two copies to the one algebra that carries both.

**The products.** The four left matrices multiply as the four units do,
$$
\mathsf M_2(\vec e_x)\mathsf M_2(\vec e_y)=\mathsf M_2(\vec e_z),\qquad
\mathsf M_2(\vec e_y)\mathsf M_2(\vec e_x)=-\mathsf M_2(\vec e_z),
$$
$$
\mathsf M_2(\vec e_z)\mathsf M_2(\vec e_x)=\mathsf M_2(\vec e_y),\qquad
\mathsf M_2(\vec e_x)^2=\mathsf M_2(\vec e_y)^2=\mathsf M_2(\vec e_z)^2=-\mathrm I_2 .
$$
For the right family the two factors are exchanged,
$$
\mathsf M_2(\vec e_x)^{\mathsf T}\mathsf M_2(\vec e_y)^{\mathsf T}=-\mathsf M_2(\vec e_z)^{\mathsf T},\qquad
\mathsf M_2(\vec e_y)^{\mathsf T}\mathsf M_2(\vec e_x)^{\mathsf T}=\mathsf M_2(\vec e_z)^{\mathsf T}.
$$
The sign of $\sigma_2$ is the only difference between the two families, and it is the matrix form of the anti-automorphism.

**Trace and determinant.** Every matrix of the two families is invertible, with determinant $1$; the identity has trace $2$ and the other matrices trace $0$. The algebra is simple and has zero divisors, and the invertibility of the four units does not extend to the complex span.

## The Stitch Between the Left and the Right

**The transpose.** For every $\tilde Q$,
$$
R(\tilde Q)=L(\tilde Q)^{\mathsf T},\qquad
L(\tilde Q)=R(\tilde Q)^{\mathsf T}.
$$
The stitch is the plain transpose. There is no sign matrix and no swap matrix in the compressed formula.

**In full.** For a matrix written entrywise,
$$
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
A^{\mathsf T}=\begin{pmatrix}a&c\\b&d\end{pmatrix}.
$$
The diagonal entries are fixed, and the two off-diagonal entries are exchanged. In the Peirce coordinates $a=P_+$, $d=P_-$, $b=X_-$, $c=X_+$, so the exchange is
$$
X_+\longleftrightarrow X_- .
$$
The transpose is the exchange of the two nilpotent coordinates, with the two idempotent coordinates fixed.

**Why the transpose.** The left ideal is a space of columns: the first column of $A$ is the image of $\tilde\Pi_+$, the second the image of $\vec\Upsilon_+$. The right ideal is a space of rows: the first row of $A$ is the image of $\tilde\Pi_+$, the second the image of $\vec\Upsilon_-$. Writing a row as a column transposes the matrix. The two bases differ by the exchange of $\vec\Upsilon_+$ and $\vec\Upsilon_-$, and the exchange of the two nilpotents is exactly the exchange of the row index and the column index.

**Against the $4\times4$ article.** There the stitch is
$$
R(\tilde Q)=\mathsf P\,L(\tilde Q)^{\mathsf T}\mathsf P,
$$
with $\mathsf P$ the permutation of the second and third coordinates (§*The Stitch Between the Two Families*). The permutation exchanges the two tensor slots, and one of the two slots is the identity factor: $\mathsf P(\mathrm I_2\otimes A^{\mathsf T})\mathsf P=A^{\mathsf T}\otimes\mathrm I_2$, which is $R$. On one block there is no slot left to exchange, the permutation acts as the identity, and the stitch is the plain transpose $R=A^{\mathsf T}$. The $4\times4$ statement is a transpose conjugated; the $2\times2$ statement is the transpose; the conjugation is invisible here because the two slots it swaps are one block and one identity.

**The anti-automorphism.** The transpose is an anti-automorphism of $M_2(\mathbb{C})$:
$$
(A_1A_2)^{\mathsf T}=A_2^{\mathsf T}A_1^{\mathsf T},\qquad
(A^{\mathsf T})^{\mathsf T}=A .
$$
It preserves the trace and the determinant,
$$
\operatorname{Tr}A^{\mathsf T}=\operatorname{Tr}A,\qquad
\det A^{\mathsf T}=\det A,
$$
so the two matrices of the same element have the same invariants.

**The element-level reading.** The transpose is the image of the anti-automorphism $\varrho$ of $\mathbb{B}$ that fixes $e_t,\vec e_x,\vec e_z$ and negates $\vec e_y$:
$$
\varrho(Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z)
=Q_te_t+Q_x\vec e_x-Q_y\vec e_y+Q_z\vec e_z,\qquad
\mathsf M_2(\varrho(\tilde Q))=\mathsf M_2(\tilde Q)^{\mathsf T}.
$$
The map $\varrho$ is an anti-automorphism, not an automorphism, and it is not the quaternion conjugation $\natural$, which negates all three vector coefficients. The transpose of the matrix is the image of this reflection of the $y$ axis.

**The relation to the $4\times4$ stitch.** The $4\times4$ stitch is
$$
R(\tilde Q)=\mathsf P\,L(\tilde Q)^{\mathsf T}\mathsf P,
$$
with $\mathsf P$ the swap of the two nilpotents. The compression keeps one block from each tensor factor. On that block the swap $\mathsf P$ exchanges the two nilpotent labels, and the two labels index the row and the column of the block; the block of the stitched matrix is therefore the transpose of the block of $L$. The sign matrix of the axis-free basis stitch and the swap matrix of the Peirce stitch have no separate $2\times2$ image: the axis-free basis display is not compressed, and the swap acts on the tensor factors, of which the block keeps one at a time. The only trace of the swap is the exchange $X_+\leftrightarrow X_-$.

## The Compression and the Switch

**The two blocks.** In the order $\mathcal{P}$,
$$
L(\tilde Q)=\mathrm I_2\otimes A,\qquad
R(\tilde Q)=A^{\mathsf T}\otimes\mathrm I_2 .
$$
In the order $\mathcal{P}'$,
$$
L(\tilde Q)=A\otimes\mathrm I_2,\qquad
R(\tilde Q)=\mathrm I_2\otimes A^{\mathsf T}.
$$
The left copy is block diagonal in $\mathcal{P}$ with the block $A$ twice; the right copy is block diagonal in $\mathcal{P}'$ with the block $A^{\mathsf T}$ twice. The two orders differ by the swap of the nilpotents. Each copy therefore has one block, repeated twice, and the compression keeps one copy of it.

**The compression maps.** Define the inflations
$$
\iota_L(A)=\mathrm I_2\otimes A\quad\text{in }\mathcal{P},\qquad
\iota_R(B)=\mathrm I_2\otimes B\quad\text{in }\mathcal{P}'.
$$
They are algebra isomorphisms onto the left and right copies. Their inverses on the copies are the compressions $\kappa_L$ and $\kappa_R$. Then
$$
\kappa_L\bigl(L(\tilde Q)\bigr)=\mathsf M_2(\tilde Q)=A,\qquad
\kappa_R\bigl(R(\tilde Q)\bigr)=\mathsf M_2(\tilde Q)^{\mathsf T}=A^{\mathsf T}.
$$
Equivalently,
$$
\kappa_L\circ L=\mathsf M_2,\qquad
\kappa_R\circ R=\Theta\circ\mathsf M_2,
$$
where $\Theta(A)=A^{\mathsf T}$. The first composition is an algebra isomorphism; the second is an anti-isomorphism, because $R$ is anti-multiplicative and $\Theta$ is an anti-automorphism.

**The fixed-order extraction is not multiplicative.** The block extraction in a fixed order is not an algebra map on the ambient $M_4(\mathbb{C})$. Let $\kappa_0$ be the extraction of the block in rows and columns $1,2$ of the matrix-unit order, and let $F_{ij}$ be the $4\times4$ matrix units. Then $\kappa_0(F_{13})=\kappa_0(F_{31})=0$, while $F_{13}F_{31}=F_{11}$ has block $E_{11}$:
$$
\kappa_0(F_{13}F_{31})=E_{11}\neq0=\kappa_0(F_{13})\kappa_0(F_{31}).
$$
The compression is defined on the two copies, in their own orders, not on the ambient.

**The invariants under compression.** The tensor forms give
$$
\operatorname{Tr}L(\tilde Q)=2\operatorname{Tr}A=4Q_t,\qquad
\det L(\tilde Q)=(\det A)^2=\langle\tilde Q\rangle_{\natural}^2,
$$
$$
\operatorname{Tr}R(\tilde Q)=2\operatorname{Tr}A^{\mathsf T}=4Q_t,\qquad
\det R(\tilde Q)=(\det A)^2=\langle\tilde Q\rangle_{\natural}^2,
$$
and
$$
\operatorname{rank}L(\tilde Q)=2\operatorname{rank}A,\qquad
\operatorname{rank}R(\tilde Q)=2\operatorname{rank}A .
$$
The factors $2$ and the square are the only changes from the $2\times2$ invariants.

**No axis-free basis switch remains.** The $4\times4$ article has a change matrix $C_{\Pi}$ between the Peirce frame and the axis-free basis,
$$
C_{\Pi}=\frac12\begin{pmatrix}1&0&0&1\\0&i&i&0\\0&1&-1&0\\i&0&0&-i\end{pmatrix},
\qquad
\det C_{\Pi}=-\tfrac14 .
$$
The matrix $C_{\Pi}$ mixes the two Peirce pairs: its columns are the four frame vectors, and the compression keeps one pair, so $C_{\Pi}$ has no $2\times2$ image. The $2\times2$ model is already in the matrix-unit frame: $\mathsf M_2(\tilde Q)$ is the matrix of the left action in the basis $(\tilde\Pi_+,\vec\Upsilon_+)$, and its transpose is the matrix of the right action in the basis $(\tilde\Pi_+,\vec\Upsilon_-)$. The switch of the compressed model is the identity. The only surviving exchange is the swap of the two nilpotents, $\mathcal{P}\leftrightarrow\mathcal{P}'$, which is what makes the right block the transpose of the left; that transpose is already the stitch.

**What does not compress.** The two $4\times4$ families commute, $L(\tilde Q_1)R(\tilde Q_2)=R(\tilde Q_2)L(\tilde Q_1)$, because they act on the two tensor factors. The two $2\times2$ matrices need not commute, and they are not operators on one space. The mixed trace
$$
\operatorname{Tr}\bigl(L(\tilde Q_1)R(\tilde Q_2)\bigr)=4Q_{1t}Q_{2t}
$$
is a trace over both factors; it does not descend to a trace of $A_1A_2^{\mathsf T}$. The two bases are two bases of the same $2\times2$ space, not bases of two different subspaces. These are the three places where the compression changes the statement, and they are the reason the $2\times2$ article is not a verbatim copy of the $4\times4$ one.

## The Product

**The left product.** For all $\tilde Q_1,\tilde Q_2$,
$$
L(\tilde Q_1\tilde Q_2)=L(\tilde Q_1)L(\tilde Q_2),\qquad
L(\tilde Q^n)=L(\tilde Q)^n,\qquad
L(\tilde Q^{-1})=L(\tilde Q)^{-1},
$$
the last when either side exists, that is when $\langle\tilde Q\rangle_{\natural}\neq0$. In the matrix model this is the multiplicativity of $\mathsf M_2$.

**The right product.** The right action is anti-multiplicative:
$$
R(\tilde Q_1\tilde Q_2)=R(\tilde Q_2)R(\tilde Q_1),\qquad
R(\tilde Q^n)=R(\tilde Q)^n,\qquad
R(\tilde Q^{-1})=R(\tilde Q)^{-1}.
$$
The reversal is the reversal of the order of the factors in the product $X\tilde Q$.

**No commutation.** The matrices $A$ and $A^{\mathsf T}$ need not commute. For $\tilde Q=\vec\Upsilon_+$,
$$
A=E_{21}=\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad
A^{\mathsf T}=E_{12}=\begin{pmatrix}0&1\\0&0\end{pmatrix},
$$
and
$$
AA^{\mathsf T}=E_{22}\neq E_{11}=A^{\mathsf T}A .
$$
The two matrices are the left and right matrices of the same element, but they act on the two different planes $S_+$ and $T_+$. There is no product of the two actions in the compressed model, and no commutation theorem to state.

**Against the $4\times4$ article.** The three identities above are §*The Product* of the $4\times4$ article with the identity factor removed: $\mathrm I_2\otimes A$ makes the left product a product of blocks, and $A^{\mathsf T}\otimes\mathrm I_2$ makes the right product the reversed product of blocks. The reversal is the reversal of the element order in both sizes; the only difference is that the $4\times4$ display carries the identity factor and this one does not.

**The mixed trace.** The product $A_1A_2^{\mathsf T}$ is a matrix product, not the compression of $L(\tilde Q_1)R(\tilde Q_2)$. Its trace is
$$
\operatorname{Tr}(A_1A_2^{\mathsf T})=2\operatorname{Sc}\bigl(\tilde Q_1\varrho(\tilde Q_2)\bigr),
$$
which involves the vector parts through the reflection $\varrho$. The $4\times4$ mixed trace $4Q_{1t}Q_{2t}$ is the trace over the two tensor factors, and it is not the trace of this $2\times2$ product. The $2\times2$ mixed trace reduces to $2Q_{1t}Q_{2t}$ when the vector parts vanish, so the two differ by the factor $2$ and by the vector terms.

## The Trace

**Twice the scalar part.** For
$$
A=\begin{pmatrix}Q_t-iQ_z&-iQ_x-Q_y\\-iQ_x+Q_y&Q_t+iQ_z\end{pmatrix},
$$
the diagonal entries are $Q_t-iQ_z$ and $Q_t+iQ_z$, so
$$
\operatorname{Tr}A=2Q_t,\qquad
Q_t=\tfrac12\operatorname{Tr}A .
$$
The trace kills the vector part. A matrix is traceless exactly when $Q_t=0$, and the traceless matrices are the image of the vector subspace.

**The trace of a product.** For two elements,
$$
\operatorname{Tr}(A_1A_2)=2\operatorname{Sc}(\tilde Q_1\tilde Q_2)
=2(Q_{1t}Q_{2t}-Q_{1x}Q_{2x}-Q_{1y}Q_{2y}-Q_{1z}Q_{2z}).
$$
The trace pairing
$$
\langle\tilde P,\tilde Q\rangle=\tfrac12\operatorname{Tr}(A_PA_Q)
$$
is the plain bilinear form of the algebra. Its Gram matrix on the coefficient basis is
$$
\mathrm E=\begin{pmatrix}1&0&0&0\\0&-1&0&0\\0&0&-1&0\\0&0&0&-1\end{pmatrix},
$$
and it is non-degenerate. The factor is $\tfrac12$ in the $2\times2$ model and $\tfrac14$ in the $4\times4$ model, because the $4\times4$ trace is twice the $2\times2$ trace.

**The trace of the regular matrices.** The compression gives
$$
\operatorname{Tr}L(\tilde Q)=2\operatorname{Tr}A=4Q_t,\qquad
\operatorname{Tr}R(\tilde Q)=2\operatorname{Tr}A^{\mathsf T}=4Q_t,
$$
which is the $4Q_t$ of §*The Trace* of the $4\times4$ article. The factor $2$ is the number of blocks.

**The trace is not the norm.** The trace is additive and complex-valued; it does not detect the vector part. The statement is the matrix form of the split
$$
\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B}).
$$

## The Determinant

**The norm.** The determinant of the general matrix is
$$
\det A=(Q_t-iQ_z)(Q_t+iQ_z)-(-iQ_x-Q_y)(-iQ_x+Q_y)
=Q_t^2+Q_z^2+Q_x^2+Q_y^2=\langle\tilde Q\rangle_{\natural}.
$$
The determinant is the quaternionic norm, not its square. The $4\times4$ determinant of §*The Determinant* of that article is the square of this one, because the block is repeated twice.

**Multiplicativity.** The determinant is multiplicative,
$$
\det(A_1A_2)=\det A_1\det A_2,
$$
which is the multiplicativity of the norm. It is invariant under conjugation and under transposition,
$$
\det(PAP^{-1})=\det A,\qquad
\det A^{\mathsf T}=\det A .
$$
Each matrix in the two families has determinant $1$, so the four left matrices and the four right matrices lie in $SL_2(\mathbb{C})$.

**The characteristic polynomial.** The characteristic polynomial is
$$
\chi_A(\lambda)=\lambda^2-(\operatorname{Tr}A)\lambda+\det A
=\lambda^2-2Q_t\lambda+\langle\tilde Q\rangle_{\natural}
=(\lambda-Q_t)^2+B^2 .
$$
The eigenvalues are
$$
\lambda_\pm=Q_t\pm iB,
$$
each once. The trace is their sum and the determinant is their product. In the $4\times4$ model each eigenvalue occurs twice; the compression removes the repetition.

**Invertibility and rank.** A matrix is invertible exactly when
$$
\det A=\langle\tilde Q\rangle_{\natural}\neq0,
$$
so the units of the algebra are the matrices of nonzero norm. The rank of $A$ is $2$ when $A$ is invertible, $1$ when $A$ is nonzero and singular, and $0$ when $A=0$. The compression gives
$$
\det L(\tilde Q)=(\det A)^2=\langle\tilde Q\rangle_{\natural}^2,\qquad
\operatorname{rank}L(\tilde Q)=2\operatorname{rank}A,
$$
and the same for $R$.

**The square.** The determinant of the $2\times2$ matrix is the norm; the determinant of the $4\times4$ matrix is the square of the norm. The trace of the $2\times2$ matrix is half the trace of the $4\times4$ matrix. These two factors are the quantitative content of the compression.

**Cayley–Hamilton.** The matrix satisfies its characteristic polynomial:
$$
A^2-(\operatorname{Tr}A)A+(\det A)\mathrm I_2
=A^2-2Q_tA+\langle\tilde Q\rangle_{\natural}\mathrm I_2=0 .
$$
The identity is the matrix form of $\tilde Q^2-2Q_t\tilde Q+\langle\tilde Q\rangle_{\natural}e_t=0$ in the coefficient basis. Its consequence is the one used elsewhere: for a non-scalar element,
$$
\mathbb{C}[A]=\operatorname{span}\{\mathrm I_2,A\},
$$
of complex dimension two, so every polynomial in $A$ of degree at least two is a linear combination of $\mathrm I_2$ and $A$. The minimal polynomial is $t^2-2Q_tt+\langle\tilde Q\rangle_{\natural}$ for a non-scalar element and $t-Q_t$ for a scalar. Its degree stays two in the first case even when the two eigenvalues coincide, which is why the centraliser of a spectrally regular element is two-dimensional, as in *The Centraliser*.

## The Spectral Projectors

**The element's own root.** The root of §*The Root and the Two Idempotents* is fixed, $\vec\Xi=i\vec e_z$, and the standard frame is adapted to it. A general element carries its own root, in the direction of its vector part, and its own pair of idempotents. The construction is the one already given, with the axis replaced by the element.

### The Two Projectors of an Element

**The root.** Let $B^2=Q_x^2+Q_y^2+Q_z^2\neq0$ and let $B$ be a square root. Then
$$
\vec\Xi=-\frac{i}{B}\vec Q,\qquad
\vec\Xi^2=\frac{i^2}{B^2}\vec Q^2=\frac{(-1)(-B^2e_t)}{B^2}=e_t ,
$$
using $\vec Q^2=-B^2e_t$. The two spectral projectors are
$$
\rho_\pm=\tfrac12\bigl(\mathrm I_2\pm\mathsf M_2(\vec\Xi)\bigr),
$$
and with
$$
\mathsf M_2(\vec\Xi)=\frac1B\begin{pmatrix}-Q_z&-Q_x+iQ_y\\-Q_x-iQ_y&Q_z\end{pmatrix}
$$
they are
$$
\rho_+=\frac{1}{2B}\begin{pmatrix}B-Q_z&-Q_x+iQ_y\\-Q_x-iQ_y&B+Q_z\end{pmatrix},\qquad
\rho_-=\frac{1}{2B}\begin{pmatrix}B+Q_z&Q_x-iQ_y\\Q_x+iQ_y&B-Q_z\end{pmatrix}.
$$

The choice of square root $B$ exchanges the two labels, since $\vec\Xi$ changes sign with $B$.

**Proposition.** The two matrices are idempotents of rank one and trace one, they are complementary, they annihilate one another, and they commute with $A$:
$$
\rho_+^2=\rho_+,\quad
\rho_-^2=\rho_-,\quad
\rho_+\rho_-=\rho_-\rho_+=0,\quad
\rho_++\rho_-=\mathrm I_2,\quad
\operatorname{Tr}\rho_\pm=1,\quad
\det\rho_\pm=0,\quad
A\rho_\pm=\rho_\pm A .
$$

*Proof.* The element $\vec\Xi$ squares to the unit, so $\tfrac12(e_t\pm\vec\Xi)$ are idempotent, complementary and orthogonal; applying the isomorphism $\mathsf M_2$ gives the first four identities. The trace of $\rho_\pm$ is $\tfrac12(2\pm0)=1$, and an idempotent of trace one has rank one, hence determinant zero. For the commutation, use
$$
A=Q_t\mathrm I_2+\mathsf M_2(\vec Q)=Q_t\mathrm I_2+iB\,\mathsf M_2(\vec\Xi),
$$
which exhibits $A$ as a polynomial in $\mathsf M_2(\vec\Xi)$.

**The spectral decomposition.** From the same identity,
$$
A-\lambda_-\mathrm I_2=2iB\rho_+,\qquad
A-\lambda_+\mathrm I_2=-2iB\rho_-,
$$
so the projectors are the Lagrange interpolating matrices of the two eigenvalues,
$$
\rho_+=\frac{A-\lambda_-\mathrm I_2}{\lambda_+-\lambda_-},\qquad
\rho_-=\frac{A-\lambda_+\mathrm I_2}{\lambda_--\lambda_+},
$$
and
$$
A=\lambda_+\rho_++\lambda_-\rho_-,\qquad
\lambda_\pm=Q_t\pm iB .
$$
The trace and the determinant of §*The Trace* and §*The Determinant* are the symmetric functions of the pair: $\operatorname{Tr}A=\lambda_++\lambda_-=2Q_t$ and $\det A=\lambda_+\lambda_-=\langle\tilde Q\rangle_{\natural}$. The two sections are therefore the spectral theorem of this article, read without naming the projectors.

**The standard pair is one case.** On the axis $\vec Q=-B\vec e_z$, that is $Q_x=Q_y=0$ and $Q_z=-B$, the root is $\vec\Xi=i\vec e_z$ and the two projectors are $E_{11}$ and $E_{22}$. The standard pair is the spectral pair of the element $Q_te_t-B\vec e_z$; for $Q_z=+B$ the two labels are exchanged. The fixed root of the Peirce frame is one point of the family, not a separate construction.

**When they are Hermitian.** The projectors satisfy $\rho_\pm^{\dagger}=\rho_\pm$ exactly when $\mathsf M_2(\vec\Xi)$ is Hermitian. This holds on the Hermitian strata: if $\tilde Q^{*}=\tilde Q$ then $A=A^{\dagger}$ and $B^2=-\lvert\vec q'\rvert^2$, so $iB$ is real and $\mathsf M_2(\vec\Xi)=(A-Q_t\mathrm I_2)/(iB)$ is Hermitian. There the two projectors are the orthogonal projectors of the Hermitian matrix. For a general complex element they are not, and $\rho_\pm^{\dagger}$ is the projector of the conjugate direction: the spectral projectors of a complex element are not orthogonal projectors.

**The degenerate case.** When $B^2=0$ the two eigenvalues coincide and the formula has no limit. The element is then either scalar, with minimal polynomial $t-Q_t$, or non-scalar with a single eigenvalue and a nontrivial Jordan block, and the two projectors do not exist. The rest of this section is about the regular case $B^2\neq0$.

### The Diagonalising Matrix

**The eigenbasis.** The two projectors give two eigenvectors: every nonzero column of $\rho_+$ is an eigenvector for $\lambda_+$, and every nonzero column of $\rho_-$ for $\lambda_-$. The diagonalising matrix collects one column of each,
$$
\mathsf C_Q=\begin{pmatrix}B-Q_z&Q_x-iQ_y\\-Q_x-iQ_y&B-Q_z\end{pmatrix},
$$
the first column of $2B\rho_+$ and the second column of $2B\rho_-$.

**The determinant.** Expanding,
$$
\det\mathsf C_Q=(B-Q_z)^2+Q_x^2+Q_y^2=2B(B-Q_z).
$$
It vanishes exactly when $B=Q_z$, that is on the axis of the frame, where the two chosen columns both vanish and this chart degenerates.

**Theorem (diagonalisation).**
$$
\mathsf C_Q^{-1}A\,\mathsf C_Q=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix},
\qquad
\mathsf C_Q^{-1}=\frac{1}{2B(B-Q_z)}\begin{pmatrix}B-Q_z&-(Q_x-iQ_y)\\Q_x+iQ_y&B-Q_z\end{pmatrix},
$$
whenever $B\neq Q_z$.

*Proof.* The two columns are eigenvectors for distinct eigenvalues, so the matrix of eigenvectors diagonalises $A$, and the diagonal entries are the eigenvalues. The inverse is the adjugate over the determinant, computed in §*The Adjugate and the Inverse*.

**The second chart.** When $B=Q_z$ the first chart is singular. The second chart is
$$
\mathsf C_Q'=\begin{pmatrix}-Q_x+iQ_y&B+Q_z\\B+Q_z&Q_x+iQ_y\end{pmatrix},
\qquad
\det\mathsf C_Q'=-2B(B+Q_z),
$$
with the same diagonalisation whenever $B\neq-Q_z$. The two determinants cannot both vanish: $B\neq0$, and $B=Q_z$ with $B=-Q_z$ would give $B=0$.

**The freedom.** The changes that keep the diagonalisation are
$$
\mathsf C_Q\mapsto\lambda\,\mathsf C_Q D,\qquad \lambda\neq0,\qquad D\text{ invertible and diagonal},
$$
because a diagonal matrix commutes with a diagonal matrix. The scalar $\lambda$ cancels from $\mathsf C_Q^{-1}A\mathsf C_Q$, so the freedom is the two parameters of $D$.

**Not the frame change of this article.** The matrix $\mathsf C_Q$ is not the change between the axis-free basis and the Peirce frame of §*The Peirce Basis and the Two Orders*; that change is fixed by the algebra, while $\mathsf C_Q$ moves inside the element. The first is a change of basis of the algebra, the second a change of basis adapted to one element, and only the second depends on $\tilde Q$.

## The Adjugate and the Inverse

**The adjugate.** For $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ the classical adjugate is
$$
\operatorname{adj}A=\begin{pmatrix}d&-b\\-c&a\end{pmatrix}=(\operatorname{Tr}A)\mathrm I_2-A .
$$
For the image of an element,
$$
\operatorname{adj}\mathsf M_2(\tilde Q)=(\operatorname{Tr}A)\mathrm I_2-A
=Q_t\mathrm I_2-\mathsf M_2(\vec Q)=\mathsf M_2(\tilde Q^{\natural}),
$$
so the adjugate is the matrix of the quaternion conjugation $\natural$. It is not the transpose: the transpose of $A$ is the image of $\varrho$, the reflection that fixes $e_t,\vec e_x,\vec e_z$ and negates $\vec e_y$.

**The identities.**
$$
A\operatorname{adj}A=\operatorname{adj}A\,A=(\det A)\mathrm I_2
$$
is the matrix form of $\tilde Q\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}e_t$. The adjugate is linear, it is an anti-automorphism of the product,
$$
\operatorname{adj}(A_1A_2)=\operatorname{adj}A_2\operatorname{adj}A_1,
$$
and it preserves the determinant at this size, $\det(\operatorname{adj}A)=\det A$.

**It is an involution here.** Since $\natural$ is an involution and $\mathsf M_2$ is injective,
$$
\operatorname{adj}(\operatorname{adj}A)=A .
$$
This is a property of the entry size. At the regular size the adjugate has degree three and the iteration is $\operatorname{adj}(\operatorname{adj}M)=\langle\tilde Q\rangle_{\natural}^4M$, as in the doubling rule of *$M_4(\mathbb{C})$ Axis-Free Representation*, §*The Determinant*.

**The inverse.** For $\langle\tilde Q\rangle_{\natural}\neq0$,
$$
A^{-1}=\frac{\operatorname{adj}A}{\det A}=\frac{\mathsf M_2(\tilde Q^{\natural})}{\langle\tilde Q\rangle_{\natural}},
$$
which is the inverse of an element, in contrast with the pair inverse of *$M_2(\mathbb{C})$ Pauli Representation : Operators*, §*The Inverse*. On the null cone the determinant vanishes, the adjugate is nonzero whenever $A\neq0$, and the inverse does not exist.

## The Four Norms

**Four quadratic invariants.** The determinant of §*The Determinant* is one of four quadratic invariants of the element. Each is a trace of a word in $A$, its adjugate and its dagger.

| Norm | Algebra value | Matrix formula | Value ring | Definite |
|---|---|---|---|---|
| Plain $P$ | $Q_t^2-B^2$ | $\tfrac12\operatorname{Tr}(A^2)$ | $\mathbb{C}$ | no |
| Quaternionic $N$ | $Q_t^2+B^2$ | $\det A$ | $\mathbb{C}$ | no |
| Hermitian $H$ | $\sum_\mu\lvert Q_\mu\rvert^2$ | $\tfrac12\operatorname{Tr}(A^{\dagger}A)$ | $\mathbb{R}$ | yes |
| Krein $K$ | $\lvert Q_t\rvert^2-\sum_k\lvert Q_k\rvert^2$ | $\tfrac12\operatorname{Tr}(\operatorname{adj}(A)A^{\dagger})$ | $\mathbb{R}$ | no |

**The plain norm.** Since $A=Q_t\mathrm I_2+\mathsf M_2(\vec Q)$ with a traceless second term,
$$
A^2=Q_t^2\mathrm I_2+2Q_t\mathsf M_2(\vec Q)+\mathsf M_2(\vec Q)^2,
\qquad
\operatorname{Tr}\bigl(\mathsf M_2(\vec Q)^2\bigr)=-2B^2,
$$
so $\tfrac12\operatorname{Tr}(A^2)=Q_t^2-B^2=P$. The word is the square of the matrix, closed by a trace; it is the bilinear form of §*The Trace* read on one element.

**The quaternionic norm.** The determinant is $N=Q_t^2+B^2$, and it is the only one of the four that is multiplicative. On the trace pairing of §*The Trace* it is the quadratic form of the plain pairing with the sign of the vector part reversed.

**The Hermitian norm.** Since $\operatorname{Tr}(A^{\dagger}A)=\sum_{ij}\lvert A_{ij}\rvert^2$,
$$
\tfrac12\operatorname{Tr}(A^{\dagger}A)
=\tfrac12\Bigl(\lvert Q_t-iQ_z\rvert^2+\lvert -iQ_x-Q_y\rvert^2
+\lvert -iQ_x+Q_y\rvert^2+\lvert Q_t+iQ_z\rvert^2\Bigr)
=\sum_\mu\lvert Q_\mu\rvert^2=H .
$$
It is half the square of the Hilbert–Schmidt norm of $A$, and it is the only one of the four that is positive definite on the complex algebra.

**The Krein norm.** Since $\operatorname{adj}A=Q_t\mathrm I_2-\mathsf M_2(\vec Q)$ and $A^{\dagger}=\overline{Q_t}\mathrm I_2-\mathsf M_2(\overline{\vec Q})$, the two traceless parts contribute only through their product, whose trace is $-2\sum_k\lvert Q_k\rvert^2$, and
$$
\tfrac12\operatorname{Tr}(\operatorname{adj}(A)A^{\dagger})
=\lvert Q_t\rvert^2-\sum_k\lvert Q_k\rvert^2=K .
$$
It is positive on the centre and negative on the vector subspace, of signature $(2,6)$ on the real algebra.

**Two pairings, not one.** The trace pairing of §*The Trace* is $\tfrac12\operatorname{Tr}(A_PA_Q)$, the plain word; the Hermitian product is $\tfrac12\operatorname{Tr}(A_P^{\dagger}A_Q)$. The first is complex bilinear and indefinite, the second is a Hilbert–Schmidt product and positive definite, and the four norms are the four ways of reading one element against the two.

## The Six Subspaces

**The table.** The six subspaces are defined in *Subspaces and Decompositions of the Biquaternion Algebra*. In the $2\times2$ model each condition is a condition on $A$ alone. Put
$$
A_{\mathbb{H}}(a,b)=\begin{pmatrix}a&b\\-\bar b&\bar a\end{pmatrix},\qquad
A_{i\mathbb{H}}(a,b)=\begin{pmatrix}a&b\\ \bar b&-\bar a\end{pmatrix},
$$
and write $\vec q=(q_x,q_y,q_z)$, $\vec q'=(q'_x,q'_y,q'_z)$. In the first row $\lambda=Q_t$. In the quaternion row $a=q_t-iq_z$, $b=-iq_x-q_y$; in the anti-quaternion row $a=q'_z+iq'_t$, $b=q'_x-iq'_y$.

| Subspace | Defining condition | Condition on $A$ | Real dim. | Trace | $\det A$ |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\tilde Q^{\natural}=\tilde Q$ | $A=\lambda\mathrm I_2$ | $2$ | $2Q_t$ | $Q_t^2$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\tilde Q^{\natural}=-\tilde Q$ | $\operatorname{Tr}A=0$ | $6$ | $0$ | $B^2$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\overline{\tilde Q}=\tilde Q$ | $A=A_{\mathbb{H}}(a,b)$ | $4$ | $2q_t$ | $\sum q_\mu^2$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $\overline{\tilde Q}=-\tilde Q$ | $A=A_{i\mathbb{H}}(a,b)$ | $4$ | $2iq'_t$ | $-\sum(q'_\mu)^2$ |
| $\mathbb{M}_+$ | $\tilde Q^{*}=\tilde Q$ | $A=A^{\dagger}$ | $4$ | $2q_t$ | $q_t^2-\lvert\vec q'\rvert^2$ |
| $\mathbb{M}_-$ | $\tilde Q^{\flat}=\tilde Q$ | $A=-A^{\dagger}$ | $4$ | $2iq'_t$ | $-(q'_t)^2+\lvert\vec q\rvert^2$ |

**No warning is needed.** In the $4\times4$ article the conditions in the third column are exact only inside the image, because the ambient $M_4(\mathbb{C})$ contains matrices that are not left regular matrices. In the $2\times2$ model the image is the whole of $M_2(\mathbb{C})$, so every condition is exact on the whole matrix algebra. The table is the compression of the $4\times4$ table, and the warning of the $4\times4$ article disappears.

### The Centre Subspace

**The scalar line.** The centre is the line of scalar matrices, of real dimension $2$. The image of the centre is the commutative line $\mathbb{C}\mathrm I_2$.

### The Vector Subspace

**The traceless matrices.** The vector subspace is the trace-zero matrices, a complex subspace of dimension $3$ and real dimension $6$. The trace is the only condition, and the determinant is $B^2$. The image of the vector subspace is closed under the commutator and not under the product.

### The Quaternion Subspace

**The quaternion-shaped matrices.** The quaternion subspace is the space of matrices
$$
A_{\mathbb{H}}(a,b)=\begin{pmatrix}a&b\\-\bar b&\bar a\end{pmatrix},
\qquad a=q_t-iq_z,\quad b=-iq_x-q_y,
$$
of real dimension $4$. The determinant is $\sum q_\mu^2$, positive definite, and vanishes only at $\tilde Q=0$; the subspace is a division algebra.

### The Anti-Quaternion Subspace

**The anti-quaternion-shaped matrices.** The anti-quaternion subspace is
$$
A_{i\mathbb{H}}(a,b)=\begin{pmatrix}a&b\\ \bar b&-\bar a\end{pmatrix},
\qquad a=q'_z+iq'_t,\quad b=q'_x-iq'_y,
$$
also of real dimension $4$. Its determinant is $-\sum(q'_\mu)^2$, non-positive and vanishing only at $\tilde Q=0$; it is not closed under multiplication, and the product of two anti-quaternion matrices is quaternion-shaped.

### The Hermitian Subspace

**The Hermitian matrices.** The Hermitian subspace is the set of matrices $A=A^{\dagger}$, of real dimension $4$. For
$$
\tilde Q=q_te_t+iq'_x\vec e_x+iq'_y\vec e_y+iq'_z\vec e_z,
$$
the matrix is
$$
A=\begin{pmatrix}q_t+q'_z&q'_x-iq'_y\\ q'_x+iq'_y&q_t-q'_z\end{pmatrix},
\qquad
\det A=q_t^2-\lvert\vec q'\rvert^2 .
$$
The determinant is indefinite.

### The Anti-Hermitian Subspace

**The anti-Hermitian matrices.** The anti-Hermitian subspace is the set of matrices $A=-A^{\dagger}$, also of real dimension $4$. For
$$
\tilde Q=iq'_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z,
$$
the matrix is
$$
A=\begin{pmatrix}i(q'_t-q_z)&-iq_x-q_y\\ -iq_x+q_y&i(q'_t+q_z)\end{pmatrix},
\qquad
\det A=-(q'_t)^2+\lvert\vec q\rvert^2 .
$$
The determinant is indefinite with the opposite sign. Neither subspace is a subalgebra; the anti-Hermitian subspace is a Lie algebra under the commutator.

### The Three Splits

**The three decompositions.** The six subspaces pair into
$$
\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B})
=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}
=\mathbb{M}_+\oplus\mathbb{M}_-,
$$
of real dimensions $2+6$, $4+4$ and $4+4$. The first is the scalar–vector split, the second the real–imaginary split, the third the Hermitian–anti-Hermitian split. No one refines another.

**The intersections.** The centre meets $\mathbb{M}_+$ in the real line $\mathbb{R}\mathrm I_2$ and $\mathbb{M}_-$ in the imaginary line $i\mathbb{R}\mathrm I_2$. The vector subspace meets $\mathbb{H}_{\mathbb{B}}$ in the real pure quaternions, of real dimension $3$, and $i\mathbb{H}_{\mathbb{B}}$ in the imaginary pure quaternions, of real dimension $3$. It meets $\mathbb{M}_+$ in $i$ times the real vector triple and $\mathbb{M}_-$ in the real vector triple. The quaternion and anti-quaternion subspaces meet only at $0$, and so do the Hermitian and anti-Hermitian subspaces.

**The closure.** The centre and the quaternion subspace are subalgebras. The vector subspace is a Lie subalgebra under the commutator, not a subalgebra under the product. The anti-quaternion subspace and the two Hermitian subspaces are neither. Multiplication by $i$ exchanges $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$, and it exchanges $\mathbb{M}_+$ and $\mathbb{M}_-$.

## Summary

The $2\times2$ Pauli representation is the compression of the $4\times4$ one, and its continuation at the element size. The left regular matrix is $\mathrm I_2\otimes A$ and the right regular matrix is $A^{\mathsf T}\otimes\mathrm I_2$; the block $A=\mathsf M_2(\tilde Q)$ occurs twice in the left and the block $A^{\mathsf T}$ occurs twice in the right, and the second block is a copy. Keeping one block gives the $2\times2$ model.

The left/right split survives on two different planes. The left action on $S_+=\mathbb{B}\tilde\Pi_+$, in the basis $(\tilde\Pi_+,\vec\Upsilon_+)$, has matrix $A$; the right action on $T_+=\tilde\Pi_+\mathbb{B}$, in the basis $(\tilde\Pi_+,\vec\Upsilon_-)$, has matrix $A^{\mathsf T}$. The stitch is the transpose. The two matrices need not commute, because they are not operators on one space.

The compression keeps the product, the trace, the determinant and the six subspaces. The normal forms of this article are entry-size statements: the spectral projectors $\rho_\pm$ and the diagonalising matrix $\mathsf C_Q$ of the element, the adjugate and the inverse, and the four norms, each of them the $2\times2$ form of a $4\times4$ object. The left product is multiplicative, the right product is anti-multiplicative, the trace is $2Q_t$, the determinant is $\langle\tilde Q\rangle_{\natural}$, and the eigenvalues are $Q_t\pm iB$, each once. The $4\times4$ quantities are the doubled ones: trace $4Q_t$, determinant $\langle\tilde Q\rangle_{\natural}^2$, each eigenvalue twice, rank twice. The axis-free basis switch does not compress: the $2\times2$ model is already the matrix-unit frame, and the switch is the identity. The only surviving exchange is the swap of the two nilpotents, which is what makes the right block the transpose of the left.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis; $e_t$ the unit, $\vec e_k^2=-e_t$ |
| $\tilde Q=Q_te_t+\vec Q$ | an element, $Q_\mu=q_\mu+iq'_\mu$ |
| $B^2$, $\langle\tilde Q\rangle_{\natural}$ | $Q_x^2+Q_y^2+Q_z^2$ and $Q_t^2+B^2$ |
| $\vec\Xi=i\vec e_z$ | the root, $\vec\Xi^2=e_t$ |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ | the standard idempotents |
| $\vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y)$ | the standard nilpotents |
| $\mathcal{P}=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$ | the Peirce frame |
| $\mathcal{P}'=(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ | the matrix-unit order |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the minimal left ideals |
| $T_\pm=\tilde\Pi_\pm\mathbb{B}$ | the minimal right ideals |
| $P_\pm,X_\pm$ | the Peirce coordinates |
| $A=\mathsf M_2(\tilde Q)=\begin{pmatrix}P_+&X_-\\X_+&P_-\end{pmatrix}$ | the $2\times2$ image |
| $L(\tilde Q)=A$, $R(\tilde Q)=A^{\mathsf T}$ | the left and right matrices |
| $\mathsf M_2(e_\mu)$ | the images of the four units: $\mathrm I_2$ and $-i\sigma_k$ |
| $\sigma_1,\sigma_2,\sigma_3$ | the Pauli matrices, $\mathsf M_2(\vec e_k)=-i\sigma_k$ |
| $\varrho$ | the anti-automorphism fixing $e_t,\vec e_x,\vec e_z$ and negating $\vec e_y$ |
| $\Theta$ | the matrix transpose, $\Theta(A)=A^{\mathsf T}$ |
| $\iota_L,\iota_R$ | the inflations $\mathrm I_2\otimes A$ and $\mathrm I_2\otimes B$ |
| $\kappa_L,\kappa_R$ | the compressions, the inverses of $\iota_L,\iota_R$ on the copies |
| $\rho_\pm=\tfrac12(\mathrm I_2\pm\mathsf M_2(\vec\Xi))$ | the spectral projectors of the element, $\vec\Xi=-i\vec Q/B$ |
| $\mathsf C_Q$ | the diagonalising matrix, $\mathsf C_Q^{-1}A\mathsf C_Q=\operatorname{diag}(\lambda_+,\lambda_-)$ |
| $\operatorname{adj}A=(\operatorname{Tr}A)\mathrm I_2-A$ | the adjugate, the image of $\tilde Q^{\natural}$ |
| $P,N,H,K$ | the four norms: plain, quaternionic, Hermitian, Krein |
| $E_{ij}$ | the matrix units |

## Further Reading

- [$M_4(\mathbb{C})$ Pauli Representation](m4c-pauli-representation.html), for the uncompressed representation, the two blocks, the stitch and the axis-free basis switch.
- [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html), for the operators on the algebra, the one-matrix and pair descriptions, and the Kronecker display.
- [$M_4(\mathbb{C})$ Axis-Free Representation](m4c-axis-free-representation.html), for the same element in the axis-free basis.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the algebra and the multiplication table.
- [The Element, the Coordinates and the Conjugations](the-element-the-coordinates-and-the-conjugations.html), for the coefficient form of the element and the four conjugations.
- [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html), for the six subspaces and the three splits.
- [Matrix Representations Conventions](matrix-representations-conventions.html), for the fixed model and the conventions of the matrix models.
