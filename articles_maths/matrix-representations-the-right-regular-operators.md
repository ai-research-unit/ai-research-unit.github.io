# __Matrix Representations : The Right Regular Operators__

## Introduction

Right multiplication is the mirror of left multiplication. It is an anti-representation, its kernel is the left annihilator, its image is a left ideal, and its matrix is the transpose of the left matrix. The two families nevertheless have the same trace, determinant, rank and spectrum. The differences are in the law, in the side of the ideals and in one sign, the sign of the $y$ generator.

This article computes the right regular matrix in the Peirce and coefficient frames, verifies the exchange with the left family on the four generators, and compares the two families. It is the second of the three articles on the regular operator families; the left family is *Matrix Representations : The Left Regular Operators* and the two-sided family is *Matrix Representations : The Two-Sided Operators*.

**Conventions.** The algebra, the displays and the element are those of *Matrix Representations : The Left Regular Operators*. The $2\times2$ block is
$$
B=\mathsf M_2(\tilde Q)=
\begin{pmatrix}
Q_t-iQ_z&-iQ_x-Q_y\\
-iQ_x+Q_y&Q_t+iQ_z
\end{pmatrix},
\qquad
\det B=\langle\tilde Q\rangle_{\natural}.
$$
The Peirce frame is $\mathcal P=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$, so that $\mathsf M_4^{L}(\tilde Q)=I_2\otimes B$ and $\mathsf M_4^{R}(\tilde Q)=B^{\mathsf T}\otimes I_2$. The coefficient frame is $\mathcal B=(e_t,\vec e_x,\vec e_y,\vec e_z)$.

**Boundaries.** The operator statements are *The Right Regular Operators on the Biquaternion Algebra*; the left matrix is *Matrix Representations : The Left Regular Operators*; the commutant of the two images is *Matrix Representations : The Centraliser and the Double Centraliser*; the two-sided family is *Matrix Representations : The Two-Sided Operators*.

## Common Aspects

### The Operator

**The definition.**
$$
R_{\tilde Q}:\mathbb{B}\longrightarrow\mathbb{B},
\qquad
R_{\tilde Q}(\tilde X)=\tilde X\tilde Q.
$$
It is complex-linear and depends linearly on $\tilde Q$.

**The anti-representation law.**
$$
R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q},
\qquad
R_{e_t}=\mathrm{id}.
$$
The order is reversed because the element multiplying on the right acts first. The map $\tilde Q\mapsto R_{\tilde Q}$ is injective, because $R_{\tilde Q}=0$ gives $\tilde Q=R_{\tilde Q}(e_t)=0$.

**The kernel and the image.** The kernel is the left annihilator,
$$
\ker R_{\tilde Q}=\{\tilde X:\tilde X\tilde Q=0\}=\operatorname{Ann}_l(\tilde Q),
$$
and the image is the left ideal
$$
\operatorname{im}R_{\tilde Q}=\mathbb{B}\tilde Q.
$$
The kernel and the image have the same dimensions as for the left family, because the two operators are exchanged by the flip below.

**The rank and the spectrum.**
$$
\operatorname{rank}R_{\tilde Q}=2\operatorname{rank}B,
\qquad
\operatorname{spec}R_{\tilde Q}=\{\lambda_+,\lambda_+,\lambda_-,\lambda_-\}.
$$
The rank trichotomy is $4,2,0$, and the characteristic polynomial is $\chi_B(\lambda)^2$. The minimal polynomial is that of $B$, not its square.

**The invariant statement.** The trace, the determinant, the rank and the spectrum depend on the element, not on the side:
$$
\operatorname{tr}R_{\tilde Q}=4Q_t,
\qquad
\det R_{\tilde Q}=\langle\tilde Q\rangle_{\natural}^2.
$$
The reason is the exchange of §*The Exchange*: the right matrix is the transpose of the left one up to a conjugation, and transposition preserves all four invariants.

### The Exchange

**The statement.** Let $S$ be the permutation of the second and third Peirce coordinates. Then
$$
R_{\tilde Q}=S\,L_{\tilde Q}^{\mathsf T}\,S^{-1}
$$
for every $\tilde Q$.

**The matrix of $S$.** In the Peirce frame,
$$
S=\begin{pmatrix}
1&0&0&0\\
0&0&1&0\\
0&1&0&0\\
0&0&0&1
\end{pmatrix},
\qquad
S^2=\mathrm I_4,\qquad
\det S=-1.
$$
It is symmetric, so $S^{-1}=S$.

**The verification on the generators.** For $e_t$ the identity is clear. For the vector units, the only non-symmetric left matrix is the $y$ one:
$$
L_y^{\mathsf T}=\begin{pmatrix}
0&1&0&0\\
-1&0&0&0\\
0&0&0&1\\
0&0&-1&0
\end{pmatrix},
\qquad
S L_y^{\mathsf T}S^{-1}=
\begin{pmatrix}
0&0&1&0\\
0&0&0&1\\
-1&0&0&0\\
0&-1&0&0
\end{pmatrix}=R_y.
$$
The matrices $L_x$ and $L_z$ are symmetric, and the conjugation by $S$ only reorders their second and third coordinates, giving $R_x$ and $R_z$.

**The reason.** The exchange is the flip of the two mixed Peirce units. Left multiplication acts on the row index and right multiplication on the column index; the flip interchanges the two indices, and the matrix of the operator is transposed. The identity on the four generators extends to every element by linearity.

**The consequence.** Since transposition preserves the trace, the determinant, the rank and the spectrum, the two families have the same invariants. The exchange is also the precise sense in which the right image is the transpose of the left image.

### The Two Families Side by Side

**What they share.** The trace $4Q_t$, the determinant $\langle\tilde Q\rangle_{\natural}^2$, the rank $2\operatorname{rank}B$ and the spectrum $\{\lambda_+,\lambda_+,\lambda_-,\lambda_-\}$ are the same. Both maps are injective and complex-linear, and both contain the identity.

**Where they differ.**

| Property | Left family | Right family |
|---|---|---|
| Law | $L_{\tilde Q}L_{\tilde P}=L_{\tilde Q\tilde P}$ | $R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q}$ |
| Peirce matrix | $I_2\otimes B$ | $B^{\mathsf T}\otimes I_2$ |
| Block form | two equal blocks $B$ | four scalar blocks |
| Invariant subspace | the two columns | the two rows |
| Kernel | right annihilator | left annihilator |
| Image | right ideal $\tilde Q\mathbb{B}$ | left ideal $\mathbb{B}\tilde Q$ |
| $y$ generator | $-i\sigma_2\otimes I_2$ | $+i\sigma_2\otimes I_2$ |
| Algebra | a copy of $\mathbb{B}$ | a copy of $\mathbb{B}^{\mathrm{opp}}$ |

**The side of the ideals.** The image of $L_{\tilde Q}$ is the set of products with $\tilde Q$ on the left, a right ideal. The image of $R_{\tilde Q}$ is the set of products with $\tilde Q$ on the right, a left ideal. The two ideals coincide only when $\tilde Q$ is central or when the algebra is commutative, which it is not.

**The centraliser.** The left image and the right image are mutual centralisers:
$$
C\bigl(M_4(\mathbb{C})_{\mathbb{B}_L}\bigr)=M_4(\mathbb{C})_{\mathbb{B}_R},
\qquad
C\bigl(M_4(\mathbb{C})_{\mathbb{B}_R}\bigr)=M_4(\mathbb{C})_{\mathbb{B}_L}.
$$
The statement is proved in *Matrix Representations : The Centraliser and the Double Centraliser*.

## The Coefficient Frame

### The Coefficient Display

**The matrix.**
$$
[R_{\tilde Q}]_{\mathcal B}=C_{\Pi}\,\bigl(B^{\mathsf T}\otimes I_2\bigr)\,C_{\Pi}^{-1}
=D\,[L_{\tilde Q}]_{\mathcal B}^{\mathsf T}\,D,
\qquad
D=\operatorname{diag}(1,-1,-1,-1).
$$
The sign matrix $D$ relates the coefficient display to the transpose of the left coefficient display.

**The entries.**
$$
[R_{\tilde Q}]_{\mathcal B}=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&Q_z&-Q_y\\
Q_y&-Q_z&Q_t&Q_x\\
Q_z&Q_y&-Q_x&Q_t
\end{pmatrix}.
$$
The first column is again the element itself, because $e_t\tilde Q=\tilde Q$. The other columns are the products $\vec e_k\tilde Q$, which differ from $\tilde Q\vec e_k$ in the signs of the imaginary units.

**The invariants.** The trace is $4Q_t$ and the determinant is $\langle\tilde Q\rangle_{\natural}^2$. The rank is twice the rank of $B$. The entries are different from the left coefficient matrix, and the eigenvalues are the same.

## The Entry Model

**The block.** Right multiplication is not a separate $2\times2$ display of the operator. The operator lives on the four-dimensional algebra; the entry model supplies the block $B$, and right multiplication on the defining module is $X\mapsto XB$, whose matrix in the matrix-unit basis is $B^{\mathsf T}\otimes\mathrm I_2$ — the Peirce display again. The block $B^{\mathsf T}$ is the compression of the right operator to one Peirce column, just as $B$ is the compression of the left operator to one Peirce row.

**The invariants from the block.** The block gives
$$
\operatorname{tr}(B^{\mathsf T})=2Q_t,\qquad
\det(B^{\mathsf T})=\langle\tilde Q\rangle_{\natural},\qquad
\operatorname{rank}(B^{\mathsf T})=\operatorname{rank}B,
\qquad
\operatorname{spec}(B^{\mathsf T})=\{\lambda_+,\lambda_-\}.
$$
The regular invariants are obtained from these by doubling the trace and the spectrum and squaring the determinant: $4Q_t$, $\{\lambda_+,\lambda_+,\lambda_-,\lambda_-\}$ and $\langle\tilde Q\rangle_{\natural}^2$. The factor two is the dimension of the Peirce column, the multiplicity space of the right action.

**The anti-law.** On the defining module right multiplication satisfies $(XB)C=X(BC)$: the order of the factors is reversed, which is the entry-model form of the anti-representation law $R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q}$. The transpose $B^{\mathsf T}$ is the matrix of the right action on the module, and transposition is the reason the right family has the same invariants as the left.

## The Peirce Frame

### The Peirce Display

**The matrix.**
$$
\mathsf M_4^{R}(\tilde Q)=B^{\mathsf T}\otimes I_2=
\begin{pmatrix}
M_{11}I_2&M_{21}I_2\\
M_{12}I_2&M_{22}I_2
\end{pmatrix},
\qquad
B=\begin{pmatrix}M_{11}&M_{12}\\M_{21}&M_{22}\end{pmatrix}.
$$
The identity factor is the left Peirce index and $B^{\mathsf T}$ acts on the right index. The matrix has four scalar blocks, not two matrix blocks.

**The entries.**
$$
\mathsf M_4^{R}(\tilde Q)=
\begin{pmatrix}
Q_t-iQ_z&0&-iQ_x+Q_y&0\\
0&Q_t-iQ_z&0&-iQ_x+Q_y\\
-iQ_x-Q_y&0&Q_t+iQ_z&0\\
0&-iQ_x-Q_y&0&Q_t+iQ_z
\end{pmatrix}.
$$
The two Peirce columns are mixed; the two rows are preserved. That is the opposite behaviour to the left matrix, which preserves the columns.

**The four basis matrices.**
$$
R_t=\mathrm I_4,\qquad
R_x=(-i\sigma_1)\otimes I_2,\qquad
R_y=(+i\sigma_2)\otimes I_2,\qquad
R_z=(-i\sigma_3)\otimes I_2.
$$
The signs need care. The matrices $\sigma_1$ and $\sigma_3$ are symmetric, so their transposes are themselves. The matrix $\sigma_2$ is antisymmetric, so
$$
(-i\sigma_2)^{\mathsf T}=+i\sigma_2.
$$
There is no minus in front of $R_y$: the factor $-i$ is part of the generator and is transposed with it.

**The squares and the relations.** The three vector matrices square to $-\mathrm I_4$, all four have determinant $1$, and they satisfy
$$
R_\mu R_\nu+R_\nu R_\mu=2\eta_{\mu\nu}\mathrm I_4,
\qquad
\eta=\operatorname{diag}(1,-1,-1,-1).
$$
The relations are the same as for the left family, because transposition preserves them.

**The traces and determinants.** The four traces are $4,0,0,0$ and the four determinants are $1,1,1,1$. The trace distinguishes the unit from the vector units; the determinant does not.

## Summary

The right regular operator $R_{\tilde Q}(\tilde X)=\tilde X\tilde Q$ is an injective anti-representation. Its kernel is the left annihilator, its image is the left ideal $\mathbb{B}\tilde Q$, and its rank is twice the rank of $B$. In the Peirce frame its matrix is $B^{\mathsf T}\otimes I_2$, with four scalar blocks; the four basis matrices are $R_t=I_4$, $R_x=-i\sigma_1\otimes I_2$, $R_y=+i\sigma_2\otimes I_2$ and $R_z=-i\sigma_3\otimes I_2$. The trace is $4Q_t$, the determinant is $\langle\tilde Q\rangle_{\natural}^2$, and the spectrum is the spectrum of $B$, doubled. The exchange $R_{\tilde Q}=S L_{\tilde Q}^{\mathsf T}S^{-1}$ holds on the four generators and hence on every element, and it explains why the two families share the four invariants while differing in the law, in the side of the ideals and in the sign of the $y$ generator. The two images are mutual centralisers.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R_{\tilde Q}$ | right multiplication by $\tilde Q$ |
| $\mathsf M_4^{R}(\tilde Q)$ | its regular matrix, $B^{\mathsf T}\otimes I_2$ in the Peirce frame |
| $R_\mu$ | the matrix of the unit $e_\mu$ |
| $S$ | the exchange of the second and third Peirce coordinates |
| $\operatorname{Ann}_l(\tilde Q)$ | the left annihilator, the kernel |
| $\mathbb{B}\tilde Q$ | the left ideal, the image |
| $4Q_t$ | the trace |
| $\langle\tilde Q\rangle_{\natural}^2$ | the determinant |
| $2\operatorname{rank}B$ | the rank, equal to $4,2,0$ |
| $\{\lambda_+,\lambda_+,\lambda_-,\lambda_-\}$ | the spectrum |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | the sign matrix of the coefficient display |

## Further Reading

- [Matrix Representations : The Left Regular Operators](matrix-representations-the-left-regular-operators.html), for the transpose family
- [Matrix Representations : The Centraliser and the Double Centraliser](matrix-representations-the-centraliser-and-the-double-centraliser.html), for the mutual centralisers
- [Matrix Representations : The Models and the Change of Frame](matrix-representations-the-models-and-the-change-of-frame.html), for the frames and the change
- [The Right Regular Operators on the Biquaternion Algebra](the-right-regular-operators-on-the-biquaternion-algebra.html), for the operator statements
- [The Left and Right Multiplication Operators on a Jordan Algebra](the-left-and-right-multiplication-operators-on-a-jordan-algebra.html), for the multiplication operators in the Jordan setting
- [Operator Family Conventions](conventions-of-the-operator-families.html), for the letter $R$ and the matrix letters