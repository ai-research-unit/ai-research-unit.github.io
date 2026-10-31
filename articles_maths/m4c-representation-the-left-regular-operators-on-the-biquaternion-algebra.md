# __$M_4(\mathbb{C})$ Representation : The Left Regular Operators on the Biquaternion Algebra__

## Introduction

**The subject.** *The Left Regular Operators on the Biquaternion Algebra* proves the operator statements for the family $L_{\tilde Q}(X)=\tilde QX$: the law, the kernel and the image, the rank trichotomy and the invertibility criterion. This article computes the same family in a frame. It gives the matrix of $L_{\tilde Q}$ in the Peirce frame, the four basis matrices, the three invariants, the spectrum and the matrix in the coefficient frame.

**The frame.** All matrices are written in the Peirce frame

$$
\mathcal{P}=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-),
$$

unless a display says otherwise. The frame is the canonical frame of *Matrix Representations Conventions*, §*The Matrix Models*, and it is fixed in *The Coefficient Basis and the Peirce Basis* of *$M_4(\mathbb{C})$ Representation : The General Endomorphisms*. The coefficient frame is used only in the last section.

**What the article proves.** The matrix is $I_2\otimes\mathsf M_2(\tilde Q)$, block diagonal with two copies of the $2\times2$ model. Its trace is $4Q_t$, its determinant $N(\tilde Q)^2$, its rank twice the rank of $\mathsf M_2(\tilde Q)$, and its spectrum the spectrum of $\mathsf M_2(\tilde Q)$ with every eigenvalue doubled. The coefficient frame is the conjugate of the Peirce display by $C_{\Pi}$.

**What the article does not do.** It does not reprove the operator statements: the law, the kernel, the image and the criterion are in the operator article. It does not treat the right family, whose matrix is the transpose, nor the two-sided family. The two frames and the change $C_{\Pi}$ are fixed in the general article; this article uses them.

**Boundaries.** The $2\times2$ model, its product, its trace and its determinant are *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*; the left regular operator is *The Left Regular Operators on the Biquaternion Algebra*; the frame and the change are *$M_4(\mathbb{C})$ Representation : The General Endomorphisms*; the norm is *Norm and Unitary Conventions*.

## The Matrix $I_2\otimes\mathsf M_2(\tilde Q)$

### The Rule

**Theorem (the matrix).** In the Peirce frame,

$$
\mathsf M_4^{L}(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q).
$$

*Proof.* The Peirce coordinates of an element are the four numbers $\tilde Q_{ij}$ of the decomposition, with the left index first. Left multiplication by $\tilde Q$ acts on the left index and fixes the right index: for fixed $j$, the column $(\tilde X_{1j},\tilde X_{2j})$ is transformed by $\mathsf M_2(\tilde Q)$, and the column $j$ is not mixed with the other column. The matrix is therefore the identity on the right index and $\mathsf M_2(\tilde Q)$ on the left index, which is the tensor product written, with the right index as the first factor.

**The order of the factors.** The identity factor is the right Peirce index, the column of the Peirce table. The $\mathsf M_2(\tilde Q)$ factor is the left Peirce index, the row. The two factors are written in that order, $I_2\otimes\mathsf M_2(\tilde Q)$, and the order is the order of the tensor basis. A display that writes $\mathsf M_2(\tilde Q)\otimes I_2$ has exchanged the two indices and is not the left matrix.

**The reading of the rule.** The rule says that the left family is the $2\times2$ model applied to each Peirce column, with the same matrix in both columns. The element $\tilde Q$ enters only through $\mathsf M_2(\tilde Q)$, and the two copies of the model are the two columns of the Peirce table.

### The Block-Diagonal Display

**The display.** Written out in the Peirce frame,

$$
\mathsf M_4^{L}(\tilde Q)=
\begin{pmatrix}
\mathsf M_2(\tilde Q)&0\\
0&\mathsf M_2(\tilde Q)
\end{pmatrix}.
$$

The matrix is block diagonal, with two identical $2\times2$ blocks. Each block is the $2\times2$ model of the same element $\tilde Q$, and the zero blocks record that the two Peirce columns are not mixed.

**The entries.** With $\mathsf M_2(\tilde Q)$ written entrywise,

$$
\mathsf M_2(\tilde Q)=
\begin{pmatrix}
Q_t-iQ_z&-iQ_x-Q_y\\
-iQ_x+Q_y&Q_t+iQ_z
\end{pmatrix},
$$

the $4\times4$ matrix is

$$
\mathsf M_4^{L}(\tilde Q)=
\begin{pmatrix}
Q_t-iQ_z&-iQ_x-Q_y&0&0\\
-iQ_x+Q_y&Q_t+iQ_z&0&0\\
0&0&Q_t-iQ_z&-iQ_x-Q_y\\
0&0&-iQ_x+Q_y&Q_t+iQ_z
\end{pmatrix}.
$$

Each entry is one coefficient, or the sum of two off-diagonal coefficients. The factor $-i$ is the one of the $2\times2$ model, where the vector units are $-i\sigma_k$; it is not a choice of this article.

**What the display shows.** The block diagonal form shows that each of the two Peirce columns is invariant under $L_{\tilde Q}$: the operator maps each column into itself. The two columns are the two Peirce planes, and the invariance is read again in §*The Peirce Diagonal Form*.

## The Four Basis Matrices

### The Peirce Frame

**The four matrices.** Write $L_\mu=\mathsf M_4^{L}(e_\mu)$. The four units go to

$$
L_t=\mathrm I_4,\qquad
L_x=-i\,\mathrm I_2\otimes\sigma_1,\qquad
L_y=-i\,\mathrm I_2\otimes\sigma_2,\qquad
L_z=-i\,\mathrm I_2\otimes\sigma_3 .
$$

**The table.** Explicitly,

| Unit | Matrix $L_\mu$ | Square | Determinant |
|---|---|---|---|
| $e_t$ | $L_t=\mathrm I_4$ | $\mathrm I_4$ | $1$ |
| $\vec e_x$ | $L_x=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix}$ | $-\mathrm I_4$ | $1$ |
| $\vec e_y$ | $L_y=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix}$ | $-\mathrm I_4$ | $1$ |
| $\vec e_z$ | $L_z=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix}$ | $-\mathrm I_4$ | $1$ |

**The squares.** The three vector units square to $-\mathrm I_4$, because their $2\times2$ models square to $-\mathrm I_2$ and the identity factor squares to itself. The sign is the one of the quaternion units, and it is the reason the exponential of a vector unit is a rotation and not a hyperbolic factor.

**The determinants.** Each of the four matrices has determinant $1$. For $L_t$ it is clear. For a vector unit, $\det L_\mu=N(e_\mu)^2=1$, because the norm of a unit is $1$; the table records the value and §*The Determinant* gives the general formula.

### The Pauli Form

**The form.** With $\sigma_1,\sigma_2,\sigma_3$ the Pauli matrices,

$$
L_t=\mathrm I_2\otimes\mathrm I_2,\qquad
L_k=-i\,\mathrm I_2\otimes\sigma_k\quad(k=x,y,z).
$$

The notation $L_k$ is the one of the table, with $k$ running over the three vector directions; the direction is read from the letter, and the index is not a row index.

**The factor $-i$.** The vector units of the $2\times2$ model are $-i\sigma_k$, not $\sigma_k$. The factor is fixed in *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*, and it is carried here by the tensor product. A display that writes $I_2\otimes\sigma_k$ without the factor is the matrix of another operator, and the sign is not a convention of this article.

**The anticommutation.** The four matrices satisfy

$$
L_\mu L_\nu+L_\nu L_\mu=2\eta_{\mu\nu}\mathrm I_4,
$$

with $\eta=\operatorname{diag}(1,-1,-1,-1)$ in the order $(t,x,y,z)$. The relation records $L_t^2=\mathrm I_4$ and $L_k^2=-\mathrm I_4$, and the vanishing of the anticommutator of two different units. It is a matrix identity of the left family, not a second definition of the Clifford map of *Frame Conventions*.

## Trace, Determinant, Rank

### The Trace $4Q_t$

**Theorem (the trace).** $\operatorname{tr}L_{\tilde Q}=4Q_t$.

*Proof.* The trace of a tensor product is the product of the traces, and $\operatorname{tr}\mathrm I_2=2$, so $\operatorname{tr}L_{\tilde Q}=2\operatorname{tr}\mathsf M_2(\tilde Q)=2\cdot2Q_t=4Q_t$.

**The reading.** The trace sees only the coefficient of the unit $e_t$. It does not see the vector part, so it does not separate two elements that differ in their vector coefficients. The trace of the operator is four times the coefficient $Q_t$, and the factor four is the dimension of the carrier, not a normalisation.

**The basis matrices.** The four traces are $4,0,0,0$ in the order $(t,x,y,z)$. The three vector matrices are traceless, as the Pauli matrices are.

### The Determinant $N(\tilde Q)^2$

**Theorem (the determinant).** $\det L_{\tilde Q}=N(\tilde Q)^2$.

*Proof.* $\det(A\otimes B)=(\det A)^m(\det B)^n$ for an $m\times m$ and an $n\times n$ matrix, with $m=n=2$ here. Hence $\det L_{\tilde Q}=(\det\mathrm I_2)^2(\det\mathsf M_2(\tilde Q))^2=N(\tilde Q)^2$, because $\det\mathsf M_2(\tilde Q)=N(\tilde Q)$ in the $2\times2$ model.

**The square.** The determinant is a square, so it is a square of a complex number and is not a signed quantity. In particular $\det L_{\tilde Q}=0$ exactly when $N(\tilde Q)=0$, which is the operator form of the invertibility criterion of *The Left Regular Operators on the Biquaternion Algebra*.

**The basis matrices.** The four determinants are $1,1,1,1$, since $N(e_\mu)^2=1$ for every unit. The determinant does not distinguish the four units; the trace does, and the spectrum does more finely.

### The Rank

**Theorem (the rank).** $\operatorname{rank}L_{\tilde Q}=2\operatorname{rank}\mathsf M_2(\tilde Q)$.

*Proof.* The rank of a tensor product $A\otimes B$ is the product of the ranks, and $\operatorname{rank}\mathrm I_2=2$. Hence $\operatorname{rank}L_{\tilde Q}=2\operatorname{rank}\mathsf M_2(\tilde Q)$.

**The three values.** The $2\times2$ model has rank $2$ for a unit, rank $1$ for a nonzero zero divisor and rank $0$ for zero. The left matrix therefore has rank $4$, $2$ and $0$ in the three cases, in agreement with the operator article. The middle value is the double of the rank of the element's matrix, not the rank of the element.

**The rank and the determinant.** The rank is four exactly when the determinant is nonzero, by the theorem and the criterion. The determinant does not separate the rank two from the rank zero; the rank does, and it is the finer invariant.

## The Spectrum

### The Eigenvalues of $\mathsf M_2(\tilde Q)$, Doubled

**Theorem (the spectrum).** The spectrum of $L_{\tilde Q}$ is the spectrum of $\mathsf M_2(\tilde Q)$ with every eigenvalue doubled:

$$
\operatorname{spec}L_{\tilde Q}=\{\lambda_+,\lambda_+,\lambda_-,\lambda_-\},
$$

where $\lambda_+,\lambda_-$ are the two eigenvalues of $\mathsf M_2(\tilde Q)$, counted with multiplicity.

*Proof.* The eigenvalues of $A\otimes I_2$ are the eigenvalues of $A$, each with multiplicity $2$, and $L_{\tilde Q}=\mathrm I_2\otimes\mathsf M_2(\tilde Q)$ has the same spectrum as $\mathsf M_2(\tilde Q)\otimes\mathrm I_2$ after the swap of the two tensor factors. The swap is a relabelling of the tensor basis and does not change the spectrum.

**The characteristic polynomial.** The theorem gives

$$
\chi_{L_{\tilde Q}}(\lambda)=\chi_{\mathsf M_2(\tilde Q)}(\lambda)^2,
$$

the square of the $2\times2$ characteristic polynomial. The eigenvalues are the two roots of the $2\times2$ polynomial, each twice; the minimal polynomial is the minimal polynomial of $\mathsf M_2(\tilde Q)$, not its square.

**The degenerate cases.** For a unit, the two eigenvalues are the roots of $\lambda^2-2Q_t\lambda+N(\tilde Q)$, each doubled. For a nonzero zero divisor, one eigenvalue is zero and the other is $2Q_t$, each doubled; the operator is not diagonalisable in general. For the zero element, the only eigenvalue is zero, with multiplicity four.

**The trace and the determinant, read on the spectrum.** The sum of the four eigenvalues is $2(\lambda_++\lambda_-)=4Q_t$, and the product is $(\lambda_+\lambda_-)^2=N(\tilde Q)^2$. The two identities recover the trace and the determinant from the spectrum and show that the four eigenvalues carry exactly the two symmetric functions, not more.

## The Two Frames

### The Peirce Diagonal Form

**The form.** In the Peirce frame the matrix is block diagonal,

$$
\mathsf M_4^{L}(\tilde Q)=\operatorname{diag}\bigl(\mathsf M_2(\tilde Q),\mathsf M_2(\tilde Q)\bigr),
$$

and the two blocks are equal. The display is the **Peirce diagonal form** of the left matrix.

**The invariant subspaces.** The two blocks are the two Peirce columns, the pairs $(\tilde\Pi_+,\vec\Upsilon_+)$ and $(\vec\Upsilon_-,\tilde\Pi_-)$ in the order of the frame. Each column is invariant under $L_{\tilde Q}$, and the operator acts on each by the same $2\times2$ matrix. This is the geometric content of the block form: the two Peirce planes are preserved, and the same $2\times2$ model acts on both.

**The diagonalisation.** The Peirce frame does not diagonalise $L_{\tilde Q}$ unless $\mathsf M_2(\tilde Q)$ is diagonal. What it does is reduce the $4\times4$ problem to two copies of the same $2\times2$ problem, and that reduction is the content of the display. A diagonalisation of the $4\times4$ matrix requires a diagonalisation of $\mathsf M_2(\tilde Q)$, which exists when the element is spectrally regular, and it is the subject of the eigenbasis articles of the $2\times2$ model.

### The Coefficient Conjugate $C_{\Pi}L_{\tilde Q}C_{\Pi}^{-1}$

**The conjugate display.** In the coefficient frame,

$$
[L_{\tilde Q}]_{\mathcal{B}}=C_{\Pi}\,\bigl(\mathrm I_2\otimes\mathsf M_2(\tilde Q)\bigr)\,C_{\Pi}^{-1}.
$$

The display is the conjugate of the Peirce matrix by the change $C_{\Pi}$ of *$M_4(\mathbb{C})$ Representation : The General Endomorphisms*, §*The Change $C_{\Pi}$*. It is the same operator, read in the coefficient frame.

**What changes and what does not.** The trace, the determinant, the rank and the spectrum are unchanged, because they are invariants of the operator. The entries change: the block diagonal form is a property of the Peirce frame, not of the operator. A statement about a zero entry of the Peirce display is a statement about the Peirce frame, and it is not a statement about the coefficient display.

**The two readings.** The Peirce reading shows the two copies of the $2\times2$ model; the coefficient reading shows the action on the four units $e_t,\vec e_x,\vec e_y,\vec e_z$. The first is the frame of the regular representation, the second the frame of the structure constants. Both are the same operator, and the change between them is fixed once, in the general article.

## Summary

In the Peirce frame the left regular matrix is $\mathsf M_4^{L}(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q)$, block diagonal with two equal copies of the $2\times2$ model. The four basis matrices are $L_t=\mathrm I_4$ and $L_k=-i\,\mathrm I_2\otimes\sigma_k$; the three vector matrices square to $-\mathrm I_4$ and all four have determinant $1$, and they satisfy the Clifford relations of the coefficient frame.

The invariants are $\operatorname{tr}L_{\tilde Q}=4Q_t$, $\det L_{\tilde Q}=N(\tilde Q)^2$ and $\operatorname{rank}L_{\tilde Q}=2\operatorname{rank}\mathsf M_2(\tilde Q)$, giving the ranks four, two and zero. The spectrum is the spectrum of $\mathsf M_2(\tilde Q)$ with each eigenvalue doubled, and the characteristic polynomial is the square of the $2\times2$ one. The Peirce frame reduces the $4\times4$ problem to two copies of the same $2\times2$ problem without diagonalising it.

In the coefficient frame the matrix is $C_{\Pi}(I_2\otimes\mathsf M_2(\tilde Q))C_{\Pi}^{-1}$. The invariants are unchanged and the entries are not; the block form is a property of the Peirce frame.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf M_4^{L}(\tilde Q)$ | The left regular matrix, $I_2\otimes\mathsf M_2(\tilde Q)$ |
| $\mathsf M_2(\tilde Q)$ | The $2\times2$ model of the element |
| $L_\mu$ | The matrix of the unit $e_\mu$, $I_2\otimes\mathsf M_2(e_\mu)$ |
| $\sigma_1,\sigma_2,\sigma_3$ | The Pauli matrices, with $\mathsf M_2(\vec e_k)=-i\sigma_k$ |
| $\operatorname{tr}L_{\tilde Q}$ | $4Q_t$ |
| $\det L_{\tilde Q}$ | $N(\tilde Q)^2$ |
| $\operatorname{rank}L_{\tilde Q}$ | $2\operatorname{rank}\mathsf M_2(\tilde Q)$ |
| $\operatorname{spec}L_{\tilde Q}$ | The spectrum of $\mathsf M_2(\tilde Q)$, doubled |
| $\mathcal{P}$, $\mathcal{B}$ | The Peirce frame and the coefficient frame |
| $C_{\Pi}$ | The Peirce change, $[L_{\tilde Q}]_{\mathcal{B}}=C_{\Pi}[L_{\tilde Q}]_{\mathcal{P}}C_{\Pi}^{-1}$ |

## Further Reading

- [The Left Regular Operators on the Biquaternion Algebra](the-left-regular-operators-on-the-biquaternion-algebra.html), for the operator statements that this article computes.
- [$M_4(\mathbb{C})$ Representation : The General Endomorphisms](m4c-representation-the-general-endomorphisms.html), for the Peirce frame, the coefficient frame and the change.
- [$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant](m2c-model-the-product-the-trace-and-the-determinant.html), for the $2\times2$ model, the factor $-i$ and the determinant.
- [The Right Regular Operators on the Biquaternion Algebra](the-right-regular-operators-on-the-biquaternion-algebra.html), for the transpose family and the exchange.
- [$M_4(\mathbb{C})$ Representation : The Right Regular Operators on the Biquaternion Algebra](m4c-representation-the-right-regular-operators-on-the-biquaternion-algebra.html), for the matrix $\mathsf M_2(\tilde Q)^{\mathsf T}\otimes I_2$.
- [Matrix Representations Conventions](conventions-of-the-matrix-models.html), for the canonical frame and the regular representation.
- [Norm and Unitary Conventions](conventions-of-the-norms-and-the-unitary-convention.html), for the norm and the invertibility criterion.
- [Operator Family Conventions](conventions-of-the-operator-families.html), for the letter $L$, the slots and the matrix letters.
