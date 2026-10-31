# __Matrix Representations : The Left Regular Operators__

## Introduction

Left multiplication by an element is a linear operator on the four-dimensional algebra. Its matrix is the regular matrix, and its properties are the properties of the element read on the carrier. The operator has two displays. In the Peirce frame it is block diagonal, with two equal copies of the $2\times2$ model. In the coefficient frame it is the matrix of the structure constants, with sixteen entries and no zero block.

This article states the operator law once, then computes the matrix in both frames: the four basis matrices, the trace, the determinant, the rank, the kernel and the image, and the spectrum. It is the first of the three articles on the regular operator families; the right family is *Matrix Representations : The Right Regular Operators* and the two-sided family is *Matrix Representations : The Two-Sided Operators*.

**Conventions.** The algebra and the displays are those of *Matrix Representations : The Models and the Change of Frame*. The element is $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, with $2\times2$ matrix
$$
B=\mathsf M_2(\tilde Q)=
\begin{pmatrix}
Q_t-iQ_z&-iQ_x-Q_y\\
-iQ_x+Q_y&Q_t+iQ_z
\end{pmatrix},
\qquad
\det B=\langle\tilde Q\rangle_{\natural}.
$$
The Peirce frame is written in the corpus order
$$
\mathcal P=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-),
$$
so that the $4\times4$ regular matrix is $\mathsf M_4^{L}(\tilde Q)=I_2\otimes B$. The coefficient frame is $\mathcal B=(e_t,\vec e_x,\vec e_y,\vec e_z)$.

**Boundaries.** The operator statements are *The Left Regular Operators on the Biquaternion Algebra*; the Peirce change is *Matrix Representations : The Models and the Change of Frame*; the $2\times2$ model is *Matrix Representations : The Product, the Trace and the Determinant*; the right family is *Matrix Representations : The Right Regular Operators*; the rank stratification is *Matrix Representations : Rank-One Matrices and the Determinantal Variety*.

## Common Aspects

### The Operator

**The definition.** For $\tilde Q\in\mathbb{B}$, the left regular operator is
$$
L_{\tilde Q}:\mathbb{B}\longrightarrow\mathbb{B},
\qquad
L_{\tilde Q}(\tilde X)=\tilde Q\tilde X.
$$
It is complex-linear, and it depends linearly on $\tilde Q$.

**The law.**
$$
L_{\tilde Q}L_{\tilde P}=L_{\tilde Q\tilde P},
\qquad
L_{e_t}=\mathrm{id}.
$$
The map $\tilde Q\mapsto L_{\tilde Q}$ is therefore an injective representation of the algebra on itself. It is injective because $L_{\tilde Q}=0$ gives $\tilde Q=L_{\tilde Q}(e_t)=0$.

**The kernel and the image.** The kernel is the right annihilator of $\tilde Q$,
$$
\ker L_{\tilde Q}=\{\tilde X:\tilde Q\tilde X=0\}=\operatorname{Ann}_r(\tilde Q),
$$
and the image is the right ideal
$$
\operatorname{im}L_{\tilde Q}=\tilde Q\mathbb{B}.
$$
The rank is the dimension of the image, and the nullity is the dimension of the kernel; their sum is four.

**The rank trichotomy.** The rank of $B$ takes the three values $2$, $1$, $0$:
$$
\operatorname{rank}L_{\tilde Q}=2\operatorname{rank}B=
\begin{cases}
4, & \langle\tilde Q\rangle_{\natural}\neq0,\\
2, & \langle\tilde Q\rangle_{\natural}=0,\ \tilde Q\neq0,\\
0, & \tilde Q=0.
\end{cases}
$$
In the first case $L_{\tilde Q}$ is invertible and the kernel is zero. In the second it has a two-dimensional kernel and a two-dimensional image, and it is not invertible. In the third it is the zero operator.

**The spectrum.** The eigenvalues are the eigenvalues of $B$, each counted twice:
$$
\operatorname{spec}L_{\tilde Q}=\{\lambda_+,\lambda_+,\lambda_-,\lambda_-\},
\qquad
\lambda_\pm=Q_t\pm iB_Q,
$$
where $B_Q^2=Q_x^2+Q_y^2+Q_z^2$. The characteristic polynomial is the square of the $2\times2$ characteristic polynomial,
$$
\chi_{L_{\tilde Q}}(\lambda)=\chi_B(\lambda)^2.
$$
The minimal polynomial is the minimal polynomial of $B$, not its square, because the two copies are equal.

## The Coefficient Frame

### The Coefficient Display

**The matrix.** In the coefficient frame,
$$
[L_{\tilde Q}]_{\mathcal B}=C_{\Pi}\,\bigl(I_2\otimes B\bigr)\,C_{\Pi}^{-1}.
$$
Written out,
$$
[L_{\tilde Q}]_{\mathcal B}=
\begin{pmatrix}
Q_t&-Q_x&-Q_y&-Q_z\\
Q_x&Q_t&-Q_z&Q_y\\
Q_y&Q_z&Q_t&-Q_x\\
Q_z&-Q_y&Q_x&Q_t
\end{pmatrix}.
$$
The first column is the element itself. The other three are the products with the three vector units, read in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$.

**The trace and the determinant.** The trace is $4Q_t$ and the determinant is $\langle\tilde Q\rangle_{\natural}^2$, as in the Peirce display, because a change of frame preserves both. The entries are not preserved: no $2\times2$ block of the coefficient matrix equals $B$ or $-B$.

**The four units.** At $Q=e_t$ the matrix is $\mathrm I_4$. At a vector unit it is the corresponding monomial matrix, with nonzero entries in $\{\pm1,\pm i\}$. All four have determinant $1$, and their traces are $4,0,0,0$.

**The image and the kernel in the frame.** The image is the column space of the coefficient matrix, of dimension $2\operatorname{rank}B$. The kernel is its null space, of dimension $4-2\operatorname{rank}B$. For a unit the columns span $\mathbb{C}^4$; for a nonzero zero divisor they span a two-dimensional right ideal; for zero they span nothing.

## The Entry Model

### The $2\times2$ Reading

**The block.** The $2\times2$ matrix $B$ is not a separate display of the operator; it is the block of the Peirce display. The operator lives on the four-dimensional carrier, and the $2\times2$ model lives on the defining module. The Peirce frame is the only frame in which the operator is a block diagonal matrix with two copies of the element's matrix.

**What the block gives.** The block gives the rank, the trace, the determinant and the spectrum of the operator by the rules of the tensor product:
$$
\operatorname{rank}L_{\tilde Q}=2\operatorname{rank}B,\qquad
\operatorname{tr}L_{\tilde Q}=2\operatorname{tr}B,\qquad
\det L_{\tilde Q}=(\det B)^2,
$$
and the spectrum is the spectrum of $B$, doubled. The factor two is the dimension of the Peirce column.

**What the block does not give.** The block does not give the kernel or the image as subspaces of the coefficient space. The kernel and the image are subspaces of the carrier; the block only gives their dimensions. The subspaces themselves require the frame change to the coefficient display, or the operator statement in the algebra.

## The Peirce Frame

### The Peirce Display

**The matrix.**
$$
\mathsf M_4^{L}(\tilde Q)=I_2\otimes B=
\begin{pmatrix}
B&0\\
0&B
\end{pmatrix}.
$$
The first factor is the column index of the Peirce table and the second is the row index; the left multiplication acts on the row and fixes the column.

**The entries.**
$$
\mathsf M_4^{L}(\tilde Q)=
\begin{pmatrix}
Q_t-iQ_z&-iQ_x-Q_y&0&0\\
-iQ_x+Q_y&Q_t+iQ_z&0&0\\
0&0&Q_t-iQ_z&-iQ_x-Q_y\\
0&0&-iQ_x+Q_y&Q_t+iQ_z
\end{pmatrix}.
$$
The two blocks are equal, and the two Peirce columns are invariant.

**The four basis matrices.** Write $L_\mu=\mathsf M_4^{L}(e_\mu)$. Then
$$
L_t=\mathrm I_4,\qquad
L_x=-i\,I_2\otimes\sigma_1,\qquad
L_y=-i\,I_2\otimes\sigma_2,\qquad
L_z=-i\,I_2\otimes\sigma_3.
$$
The three vector matrices square to $-\mathrm I_4$, and all four have determinant $1$. They satisfy the Clifford relations
$$
L_\mu L_\nu+L_\nu L_\mu=2\eta_{\mu\nu}\mathrm I_4,
\qquad
\eta=\operatorname{diag}(1,-1,-1,-1),
$$
in the order $(t,x,y,z)$.

**The trace and the determinant.** The trace of a tensor product is the product of the traces:
$$
\operatorname{tr}L_{\tilde Q}=2\operatorname{tr}B=4Q_t.
$$
The determinant of a tensor product is
$$
\det L_{\tilde Q}=(\det B)^2=\langle\tilde Q\rangle_{\natural}^2.
$$
The determinant vanishes exactly when $B$ is not invertible, which is the criterion $\langle\tilde Q\rangle_{\natural}\neq0$.

**The spectrum in the display.** The eigenvalues of $I_2\otimes B$ are the eigenvalues of $B$, each twice, by the same tensor argument. The trace is the sum of the four eigenvalues, $2(\lambda_++\lambda_-)=4Q_t$, and the determinant is their product, $(\lambda_+\lambda_-)^2=\langle\tilde Q\rangle_{\natural}^2$.

## Summary

The left regular operator $L_{\tilde Q}(\tilde X)=\tilde Q\tilde X$ is an injective representation of the algebra on itself. Its kernel is the right annihilator, its image is the right ideal $\tilde Q\mathbb{B}$, and its rank is twice the rank of $B$, giving the trichotomy $4,2,0$. In the Peirce frame its matrix is $I_2\otimes B$, block diagonal with two equal copies of the $2\times2$ model; the four basis matrices are $L_t=I_4$ and $L_k=-iI_2\otimes\sigma_k$, with determinant $1$ and Clifford relations of signature $(1,3)$. The trace is $4Q_t$, the determinant is $\langle\tilde Q\rangle_{\natural}^2$, and the spectrum is the spectrum of $B$ with each eigenvalue doubled. In the coefficient frame the matrix is $C_{\Pi}(I_2\otimes B)C_{\Pi}^{-1}$, with the same invariants and different entries. The $2\times2$ block is a Peirce-frame compression, not a display of the operator.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\tilde Q}$ | left multiplication by $\tilde Q$ |
| $\mathsf M_4^{L}(\tilde Q)$ | its regular matrix, $I_2\otimes B$ in the Peirce frame |
| $B=\mathsf M_2(\tilde Q)$ | the $2\times2$ block |
| $L_\mu$ | the matrix of the unit $e_\mu$ |
| $\operatorname{Ann}_r(\tilde Q)$ | the right annihilator, the kernel |
| $\tilde Q\mathbb{B}$ | the right ideal, the image |
| $4Q_t$ | the trace |
| $\langle\tilde Q\rangle_{\natural}^2$ | the determinant |
| $2\operatorname{rank}B$ | the rank, equal to $4,2,0$ |
| $\{\lambda_+,\lambda_+,\lambda_-,\lambda_-\}$ | the spectrum |
| $C_{\Pi}$ | the Peirce change |
| $\eta=\operatorname{diag}(1,-1,-1,-1)$ | the Clifford signature |

## Further Reading

- [Matrix Representations : The Models and the Change of Frame](matrix-representations-the-models-and-the-change-of-frame.html), for the frames and the change
- [Matrix Representations : The Right Regular Operators](matrix-representations-the-right-regular-operators.html), for the transpose family
- *Matrix Representations : The Two-Sided Operators*, for the products $L_\mu R_\nu$
- *Matrix Representations : Rank-One Matrices and the Determinantal Variety*, for the rank stratification
- [The Left Regular Operators on the Biquaternion Algebra](the-left-regular-operators-on-the-biquaternion-algebra.html), for the operator statements
- [The Left and Right Multiplication Operators on a Jordan Algebra](the-left-and-right-multiplication-operators-on-a-jordan-algebra.html), for the multiplication operators in the Jordan setting
- [Operator Family Conventions](conventions-of-the-operator-families.html), for the letter $L$ and the matrix letters