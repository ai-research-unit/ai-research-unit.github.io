# __$M_4(\mathbb{C})$ Representation : The Right Regular Operators on the Biquaternion Algebra__

## Introduction

**The subject.** *The Right Regular Operators on the Biquaternion Algebra* proves the operator statements for the family $R_{\tilde Q}(X)=X\tilde Q$: the anti-representation law, the kernel and the image, the rank trichotomy, the invertibility criterion and the exchange. This article computes the same family in a frame. It gives the matrix of $R_{\tilde Q}$ in the Peirce frame, the four basis matrices, the verification of the exchange on the four generators, the invariants, the spectrum and the comparison with the left family.

**The frame.** All matrices are written in the Peirce frame

$$
\mathcal{P}=(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-),
$$

unless a display says otherwise. The frame, its order and the change $C_{\Pi}$ are fixed in *$M_4(\mathbb{C})$ Representation : The General Endomorphisms*; the left matrix in the same frame is the subject of *$M_4(\mathbb{C})$ Representation : The Left Regular Operators on the Biquaternion Algebra*, and this article uses its display as the left-hand side of the exchange.

**What the article proves.** The matrix is $\mathsf M_2(\tilde Q)^{\mathsf T}\otimes I_2$, with scalar blocks $M_{ij}(\tilde Q)I_2$. Its trace is $4Q_t$, its determinant $N(\tilde Q)^2$, its rank twice the rank of $\mathsf M_2(\tilde Q)$, and its spectrum the spectrum of $\mathsf M_2(\tilde Q)$ with every eigenvalue doubled. The exchange $R_{\tilde Q}=S L_{\tilde Q}^{\mathsf T}S^{-1}$ is verified on the four generators, entry by entry, and the sign on the $y$ generator is positive, $R_{\vec e_y}=+i\sigma_2\otimes I_2$.

**What the article does not do.** It does not reprove the operator statements: the law, the kernel, the image, the criterion and the exchange are in the operator article. It does not treat the two-sided family, which is Part IV, nor the commutant, which is *The Commutant of the Two Regular Families*. It does not restate the Peirce frame, the coefficient frame or the change $C_{\Pi}$; those are fixed once, in the general article.

**Boundaries.** The $2\times2$ model, its product, its trace and its determinant are *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*; the right regular operator is *The Right Regular Operators on the Biquaternion Algebra*; the frame and the change are *$M_4(\mathbb{C})$ Representation : The General Endomorphisms*; the norm is *Norm and Unitary Conventions*.

## The Matrix $\mathsf M_2(\tilde Q)^{\mathsf T}\otimes I_2$

### The Rule

**Theorem (the matrix).** In the Peirce frame,

$$
\mathsf M_4^{R}(\tilde Q)=\mathsf M_2(\tilde Q)^{\mathsf T}\otimes\mathrm I_2 .
$$

*Proof.* The Peirce coordinates of an element are the four numbers $\tilde Q_{ij}$, with the left index first. Right multiplication by $\tilde Q$ acts on the right index and fixes the left index: $(X\tilde Q)_{ij}=\sum_kX_{ik}\tilde Q_{kj}$. In the frame order the four-vector is the list of the two columns of the $2\times2$ matrix $X$, and the $j$-th column of $X\tilde Q$ is $\sum_iX_{*i}\tilde Q_{ij}$. The matrix whose $(j,i)$ block is $\tilde Q_{ij}I_2$ does exactly this, and that matrix is $\mathsf M_2(\tilde Q)^{\mathsf T}\otimes I_2$, whose $(j,i)$ block is $(\mathsf M_2(\tilde Q)^{\mathsf T})_{ji}I_2=\tilde Q_{ij}I_2$.

**The order of the factors.** The identity factor is the left Peirce index, the factor $\mathsf M_2(\tilde Q)^{\mathsf T}$ the right Peirce index. The two factors are written in that order, $\mathsf M_2(\tilde Q)^{\mathsf T}\otimes I_2$, and the order is the order of the tensor basis. A display that writes $I_2\otimes\mathsf M_2(\tilde Q)^{\mathsf T}$ has exchanged the two indices and is not the right matrix.

**The reading of the rule.** The rule says that the right family is the $2\times2$ model applied to each Peirce row, with the transposed matrix in both rows. The element enters only through $\mathsf M_2(\tilde Q)$, and the transpose is the one of the $2\times2$ model, not a transpose of the $4\times4$ matrix.

### The Four Blocks $M_{ij}(\tilde Q)I_2$

**The block display.** Write $\mathsf M_2(\tilde Q)=\begin{pmatrix}M_{11}&M_{12}\\M_{21}&M_{22}\end{pmatrix}$. Then

$$
\mathsf M_4^{R}(\tilde Q)=
\begin{pmatrix}
M_{11}I_2&M_{21}I_2\\
M_{12}I_2&M_{22}I_2
\end{pmatrix}.
$$

The four blocks are scalar multiples of the $2\times2$ identity, and the two off-diagonal blocks carry the entries $M_{21}$ and $M_{12}$ in the exchanged positions.

**What the display shows.** The matrix is not block diagonal: the two Peirce columns are mixed. What is preserved is the pair of rows: each row of $X$ is multiplied on the right by $\tilde Q$, so the two rows are transformed independently and are not mixed. The block display is the column-stacked reading of that row action, and the scalar blocks are the price of reading rows in a frame ordered by columns.

**The contrast with the left matrix.** The left matrix is $I_2\otimes\mathsf M_2(\tilde Q)$, block diagonal with two equal blocks $\mathsf M_2(\tilde Q)$; the right matrix is $\mathsf M_2(\tilde Q)^{\mathsf T}\otimes I_2$, with four scalar blocks. The two displays are different matrices, and they are different operators; they agree only at the scalars.

**The explicit display.** Written out,

$$
\mathsf M_4^{R}(\tilde Q)=
\begin{pmatrix}
Q_t-iQ_z&-iQ_x-Q_y&0&0\\
-iQ_x+Q_y&Q_t+iQ_z&0&0\\
0&0&Q_t-iQ_z&-iQ_x-Q_y\\
0&0&-iQ_x+Q_y&Q_t+iQ_z
\end{pmatrix}^{\mathsf T}
=
\begin{pmatrix}
Q_t-iQ_z&-iQ_x+Q_y&0&0\\
-iQ_x-Q_y&Q_t+iQ_z&0&0\\
0&0&Q_t-iQ_z&-iQ_x+Q_y\\
0&0&-iQ_x-Q_y&Q_t+iQ_z
\end{pmatrix}.
$$

The transpose exchanges the two off-diagonal entries of each block, and it does not move the block diagonal.

## The Four Basis Matrices

### The Peirce Frame

**The four matrices.** Write $R_\mu=\mathsf M_4^{R}(e_\mu)$. The four units go to

| Unit | Matrix $R_\mu$ | Square | Determinant |
|---|---|---|---|
| $e_t$ | $R_t=\mathrm I_4$ | $\mathrm I_4$ | $1$ |
| $\vec e_x$ | $R_x=\begin{pmatrix}0&0&-i&0\\0&0&0&-i\\-i&0&0&0\\0&-i&0&0\end{pmatrix}$ | $-\mathrm I_4$ | $1$ |
| $\vec e_y$ | $R_y=\begin{pmatrix}0&0&1&0\\0&0&0&1\\-1&0&0&0\\0&-1&0&0\end{pmatrix}$ | $-\mathrm I_4$ | $1$ |
| $\vec e_z$ | $R_z=\begin{pmatrix}-i&0&0&0\\0&-i&0&0\\0&0&i&0\\0&0&0&i\end{pmatrix}$ | $-\mathrm I_4$ | $1$ |

**The squares.** The three vector matrices square to $-\mathrm I_4$, because their $2\times2$ models square to $-\mathrm I_2$ and the identity factor squares to itself. The sign is the one of the quaternion units.

**The determinants.** Each of the four matrices has determinant $1$. For $R_t$ it is clear; for a vector unit, $\det R_\mu=N(e_\mu)^2=1$, and §*The Three Invariants* gives the general formula.

**The two middle coordinates.** The $z$ generator is the one that shows the exchange in the simplest case: $L_z=\operatorname{diag}(-i,i,-i,i)$ while $R_z=\operatorname{diag}(-i,-i,i,i)$. The two matrices have the same entries in a different order, and the exchange moves the second and third entries.

### The Pauli Form and the Sign on $R_y$

**The form.** With $\sigma_1,\sigma_2,\sigma_3$ the Pauli matrices,

$$
R_t=\mathrm I_2\otimes\mathrm I_2,\qquad
R_x=(-i\sigma_1)\otimes\mathrm I_2,\qquad
R_y=(+i\sigma_2)\otimes\mathrm I_2,\qquad
R_z=(-i\sigma_3)\otimes\mathrm I_2 .
$$

The matrices $\sigma_1$ and $\sigma_3$ are symmetric, so the transpose leaves their factors unchanged; $\sigma_2$ is antisymmetric, so the transpose changes the sign of the factor $-i$.

**The sign.** With $\mathsf M_2(\vec e_y)=-i\sigma_2=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$,

$$
\mathsf M_2(\vec e_y)^{\mathsf T}=+i\sigma_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad
R_{\vec e_y}=+i\sigma_2\otimes\mathrm I_2 .
$$

There is no minus in front of the $y$ generator. The minus that older displays carried came from transposing the Pauli matrix while keeping the factor $-i$; the factor is part of the generator and is transposed with it, and $-i\sigma_2^{\mathsf T}=+i\sigma_2$. The correction is uniform across the corpus, and §*The Verification Entry by Entry* checks it on the entries.

**The anticommutation.** The four matrices satisfy

$$
R_\mu R_\nu+R_\nu R_\mu=2\eta_{\mu\nu}\mathrm I_4,
$$

with $\eta=\operatorname{diag}(1,-1,-1,-1)$ in the order $(t,x,y,z)$, because the $2\times2$ generators satisfy the same relation and the transpose preserves it. The relation is the matrix form of the squares and the anticommutation of the units, and it is the same relation as for the left family.

## The Exchange Verified

### The Four Generators

**The statement.** With $S$ the exchange of *The Right Regular Operators on the Biquaternion Algebra*, §*The Operator $S$*, the identity to verify is

$$
R_\mu=S\,L_\mu^{\mathsf T}\,S^{-1},\qquad \mu=t,x,y,z.
$$

The four left matrices are the ones of *$M_4(\mathbb{C})$ Representation : The Left Regular Operators on the Biquaternion Algebra*, §*The Peirce Frame*. The identity is a matrix identity in the Peirce frame; the operator $S$ is the flip of the two mixed Peirce units, and its matrix there is the permutation of the second and third coordinates.

**The four checks.** The generators fall into three types:

- $t$: $L_t=\mathrm I_4$ is symmetric, and $S\mathrm I_4S^{-1}=\mathrm I_4=R_t$;
- $x$: $L_x$ is symmetric, and $S L_xS^{-1}=R_x$;
- $y$: $L_y$ is not symmetric, and the transpose is the step that produces the sign;
- $z$: $L_z$ is diagonal and symmetric, and $S L_zS^{-1}=R_z$.

The only generator whose left matrix is not symmetric is $\vec e_y$, and it is the only one where a sign can go wrong. The next subsection computes it entry by entry and checks the other three in the same table.

### The Verification Entry by Entry

**The $y$ generator.** The left matrix is

$$
L_y=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},
\qquad
L_y^{\mathsf T}=\begin{pmatrix}0&1&0&0\\-1&0&0&0\\0&0&0&1\\0&0&-1&0\end{pmatrix}.
$$

Conjugating by $S$, which exchanges the second and third rows and columns, gives

$$
S L_y^{\mathsf T}S^{-1}=
\begin{pmatrix}0&0&1&0\\0&0&0&1\\-1&0&0&0\\0&-1&0&0\end{pmatrix}=R_y .
$$

The four nonzero entries are $+1$ in the first row, third column, and in the second row, fourth column, and $-1$ in the third row, first column, and in the fourth row, second column. The top-right block is $+I_2$, not $-I_2$; the sign is the one of $+i\sigma_2\otimes I_2$.

**The other three.** The same conjugation gives

$$
S L_t^{\mathsf T}S^{-1}=\mathrm I_4=R_t,\qquad
S L_x^{\mathsf T}S^{-1}=R_x,\qquad
S L_z^{\mathsf T}S^{-1}=R_z .
$$

For $t$ the identity is clear. For $x$, $L_x$ is symmetric and $S L_xS^{-1}$ is the matrix $R_x$ displayed in §*The Peirce Frame*. For $z$, $L_z=\operatorname{diag}(-i,i,-i,i)$ and the exchange of the second and third coordinates gives $\operatorname{diag}(-i,-i,i,i)=R_z$.

**The check in one table.** The four identities, read on the nonzero entries, are

| Generator | Nonzero entries of $L_\mu$ | After $S(\cdot)^{\mathsf T}S^{-1}$ | Nonzero entries of $R_\mu$ |
|---|---|---|---|
| $e_t$ | $(1,1),(2,2),(3,3),(4,4)$ at $1$ | unchanged | $(1,1),(2,2),(3,3),(4,4)$ at $1$ |
| $\vec e_x$ | $(1,2),(2,1),(3,4),(4,3)$ at $-i$ | $(1,3),(3,1),(2,4),(4,2)$ at $-i$ | $(1,3),(3,1),(2,4),(4,2)$ at $-i$ |
| $\vec e_y$ | $(1,2)$ at $-1$, $(2,1)$ at $1$, $(3,4)$ at $-1$, $(4,3)$ at $1$ | $(1,3)$ at $1$, $(2,4)$ at $1$, $(3,1)$ at $-1$, $(4,2)$ at $-1$ | $(1,3)$ at $1$, $(2,4)$ at $1$, $(3,1)$ at $-1$, $(4,2)$ at $-1$ |
| $\vec e_z$ | $(1,1)$ at $-i$, $(2,2)$ at $i$, $(3,3)$ at $-i$, $(4,4)$ at $i$ | $(1,1)$ at $-i$, $(2,2)$ at $-i$, $(3,3)$ at $i$, $(4,4)$ at $i$ | $(1,1)$ at $-i$, $(2,2)$ at $-i$, $(3,3)$ at $i$, $(4,4)$ at $i$ |

The rows agree, and the $y$ row is the one that fixes the sign. The table is a verification, not a second proof: the proof of the identity for a general element is in the operator article, and the linearity in $\tilde Q$ extends the four checks to every element.

## Trace, Determinant, Rank, Spectrum

### The Three Invariants

**Theorem (the invariants).** For every $\tilde Q\in\mathbb{B}$,

$$
\operatorname{tr}R_{\tilde Q}=4Q_t,\qquad
\det R_{\tilde Q}=N(\tilde Q)^2,\qquad
\operatorname{rank}R_{\tilde Q}=2\operatorname{rank}\mathsf M_2(\tilde Q).
$$

*Proof.* The trace of a tensor product is the product of the traces, and $\operatorname{tr}\mathsf M_2(\tilde Q)^{\mathsf T}=\operatorname{tr}\mathsf M_2(\tilde Q)=2Q_t$, so $\operatorname{tr}R_{\tilde Q}=2Q_t\cdot2=4Q_t$. The determinant is $\det(\mathsf M_2(\tilde Q)^{\mathsf T})^2\det(I_2)^2=N(\tilde Q)^2$, by the determinant of a tensor product. The rank is the product of the ranks, and $\operatorname{rank}I_2=2$.

**The three values of the rank.** The $2\times2$ model has rank $2$ for a unit, rank $1$ for a nonzero zero divisor and rank $0$ for zero. The right matrix therefore has rank $4$, $2$ and $0$ in the three cases, in agreement with the operator article.

**The determinant and the criterion.** The determinant is a square, so $\det R_{\tilde Q}=0$ exactly when $N(\tilde Q)=0$. The criterion $N(\tilde Q)\neq0$ is therefore the criterion $\det R_{\tilde Q}\neq0$, as it is for the left family.

**The basis matrices.** The four traces are $4,0,0,0$, the four determinants are $1,1,1,1$, and the four ranks are $4,4,4,4$. The trace separates the unit from the vector units; the determinant and the rank do not.

### The Spectrum

**Theorem (the spectrum).** The spectrum of $R_{\tilde Q}$ is the spectrum of $\mathsf M_2(\tilde Q)$ with every eigenvalue doubled:

$$
\operatorname{spec}R_{\tilde Q}=\{\lambda_+,\lambda_+,\lambda_-,\lambda_-\},
$$

where $\lambda_+,\lambda_-$ are the two eigenvalues of $\mathsf M_2(\tilde Q)$, counted with multiplicity.

*Proof.* The eigenvalues of $A\otimes I_2$ are the eigenvalues of $A$, each with multiplicity $2$, and the eigenvalues of $\mathsf M_2(\tilde Q)^{\mathsf T}$ are the eigenvalues of $\mathsf M_2(\tilde Q)$. The spectrum of $R_{\tilde Q}=\mathsf M_2(\tilde Q)^{\mathsf T}\otimes I_2$ is therefore the spectrum of $\mathsf M_2(\tilde Q)$, doubled.

**The characteristic polynomial.** The theorem gives

$$
\chi_{R_{\tilde Q}}(\lambda)=\chi_{\mathsf M_2(\tilde Q)}(\lambda)^2,
$$

the square of the $2\times2$ characteristic polynomial. The minimal polynomial is the minimal polynomial of $\mathsf M_2(\tilde Q)$, not its square.

**The degenerate cases.** For a unit, the eigenvalues are the two roots of $\lambda^2-2Q_t\lambda+N(\tilde Q)$, each doubled. For a nonzero zero divisor, one eigenvalue is zero and the other is $2Q_t$, each doubled. For the zero element, the only eigenvalue is zero, with multiplicity four.

**The same spectrum as the left family.** The left matrix has the spectrum $\{\lambda_+,\lambda_+,\lambda_-,\lambda_-\}$ by *$M_4(\mathbb{C})$ Representation : The Left Regular Operators on the Biquaternion Algebra*, §*The Eigenvalues of $\mathsf M_2(\tilde Q)$, Doubled*, and the right matrix has the same spectrum. The two operators are different, but the spectrum does not see the side.

## The Two Families Side by Side

### What They Share

**The common values.** The two matrices $L_{\tilde Q}$ and $R_{\tilde Q}$ have the same trace $4Q_t$, the same determinant $N(\tilde Q)^2$, the same rank $2\operatorname{rank}\mathsf M_2(\tilde Q)$ and the same spectrum, doubled. The values depend on the element and not on the side, and the two families are indistinguishable by these invariants.

**The common structure.** Both families are images of injective complex-linear maps from the four-dimensional algebra, both contain the identity, and both have complex dimension four. The identity is the value at $e_t$ in both cases, $L_{e_t}=R_{e_t}=\mathrm{id}$.

**Why the invariants agree.** The exchange writes $R_{\tilde Q}=S L_{\tilde Q}^{\mathsf T}S^{-1}$: the right matrix is the transpose of the left one, conjugated by an involution, and the transpose preserves the trace, the determinant, the rank and the spectrum. The agreement is therefore a consequence of the exchange, not a coincidence of the four units.

### Where They Differ

**The law.** The left map is a representation, $L_{\tilde Q}L_{\tilde P}=L_{\tilde Q\tilde P}$; the right map is an anti-representation, $R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q}$. The images are a copy of the algebra and a copy of the opposite algebra.

**The display.** The left matrix is block diagonal with two equal blocks $\mathsf M_2(\tilde Q)$; the right matrix has four scalar blocks $M_{ij}(\tilde Q)I_2$ and mixes the two Peirce columns. The left matrix preserves the two columns, the right matrix preserves the two rows.

**The $y$ sign.** The left matrix is $L_y=-i\sigma_2\otimes I_2=\begin{pmatrix}0&0&-i&0\\0&0&0&-i\\-i&0&0&0\\0&-i&0&0\end{pmatrix}$; the right matrix is $R_y=+i\sigma_2\otimes I_2=\begin{pmatrix}0&0&1&0\\0&0&0&1\\-1&0&0&0\\0&-1&0&0\end{pmatrix}$. The two differ by the transpose of the generator, and the difference is a sign, not a convention.

**The side of the ideals.** The image of $L_{\tilde Q}$ is the right ideal $\tilde Q\mathbb{B}$; the image of $R_{\tilde Q}$ is the left ideal $\mathbb{B}\tilde Q$. The two ideals are different in general, and the side of each is opposite to the side of the multiplication that produces it.

### The Comparison Table

| Property | Left family $L_{\tilde Q}$ | Right family $R_{\tilde Q}$ |
|---|---|---|
| Matrix in the Peirce frame | $I_2\otimes\mathsf M_2(\tilde Q)$ | $\mathsf M_2(\tilde Q)^{\mathsf T}\otimes I_2$ |
| Block form | two blocks $\mathsf M_2(\tilde Q)$, off-diagonal $0$ | four blocks $M_{ij}(\tilde Q)I_2$ |
| Law | $L_{\tilde Q}L_{\tilde P}=L_{\tilde Q\tilde P}$ | $R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q}$ |
| Image | a copy of $\mathbb{B}$ | a copy of $\mathbb{B}^{\mathrm{opp}}$ |
| Kernel | $\operatorname{Ann}_r(\tilde Q)$ | $\operatorname{Ann}_l(\tilde Q)$ |
| Image of one operator | the right ideal $\tilde Q\mathbb{B}$ | the left ideal $\mathbb{B}\tilde Q$ |
| Trace | $4Q_t$ | $4Q_t$ |
| Determinant | $N(\tilde Q)^2$ | $N(\tilde Q)^2$ |
| Rank | $2\operatorname{rank}\mathsf M_2(\tilde Q)$ | $2\operatorname{rank}\mathsf M_2(\tilde Q)$ |
| Spectrum | $\mathsf M_2(\tilde Q)$, doubled | $\mathsf M_2(\tilde Q)$, doubled |
| Pauli form of the $y$ generator | $-i\sigma_2\otimes I_2$ | $+i\sigma_2\otimes I_2$ |

## Summary

In the Peirce frame the right regular matrix is $\mathsf M_4^{R}(\tilde Q)=\mathsf M_2(\tilde Q)^{\mathsf T}\otimes I_2$, with four scalar blocks $M_{ij}(\tilde Q)I_2$. The four basis matrices are $R_t=I_4$, $R_x=(-i\sigma_1)\otimes I_2$, $R_y=(+i\sigma_2)\otimes I_2$ and $R_z=(-i\sigma_3)\otimes I_2$; the three vector matrices square to $-I_4$, all four have determinant $1$, and the sign on $y$ is positive.

The invariants are $\operatorname{tr}R_{\tilde Q}=4Q_t$, $\det R_{\tilde Q}=N(\tilde Q)^2$ and $\operatorname{rank}R_{\tilde Q}=2\operatorname{rank}\mathsf M_2(\tilde Q)$, giving the ranks four, two and zero. The spectrum is the spectrum of $\mathsf M_2(\tilde Q)$ with each eigenvalue doubled. The exchange $R_{\tilde Q}=S L_{\tilde Q}^{\mathsf T}S^{-1}$ is verified on the four generators, entry by entry, and the $y$ row fixes the sign.

The two families share the trace, the determinant, the rank and the spectrum, and differ in the law, in the block form, in the side of the ideals and in the sign of the $y$ generator. The commutant of the two is the subject of *The Commutant of the Two Regular Families*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf M_4^{R}(\tilde Q)$ | The right regular matrix, $\mathsf M_2(\tilde Q)^{\mathsf T}\otimes I_2$ |
| $\mathsf M_2(\tilde Q)$ | The $2\times2$ model of the element |
| $R_\mu$ | The matrix of the unit $e_\mu$, $\mathsf M_2(e_\mu)^{\mathsf T}\otimes I_2$ |
| $M_{ij}(\tilde Q)$ | The entries of $\mathsf M_2(\tilde Q)$ |
| $S$ | The exchange, the permutation of the second and third Peirce coordinates |
| $\operatorname{tr}R_{\tilde Q}$ | $4Q_t$ |
| $\det R_{\tilde Q}$ | $N(\tilde Q)^2$ |
| $\operatorname{rank}R_{\tilde Q}$ | $2\operatorname{rank}\mathsf M_2(\tilde Q)$ |
| $\operatorname{spec}R_{\tilde Q}$ | The spectrum of $\mathsf M_2(\tilde Q)$, doubled |
| $\mathcal{P}$ | The Peirce frame |

## Further Reading

- [The Right Regular Operators on the Biquaternion Algebra](the-right-regular-operators-on-the-biquaternion-algebra.html), for the operator statements that this article computes.
- [$M_4(\mathbb{C})$ Representation : The Left Regular Operators on the Biquaternion Algebra](m4c-representation-the-left-regular-operators-on-the-biquaternion-algebra.html), for the left matrix transposed here.
- [$M_4(\mathbb{C})$ Representation : The General Endomorphisms](m4c-representation-the-general-endomorphisms.html), for the Peirce frame, the coefficient frame and the change.
- [$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant](m2c-model-the-product-the-trace-and-the-determinant.html), for the $2\times2$ model, the factor $-i$ and the determinant.
- [The Commutant of the Two Regular Families](the-commutant-of-the-two-regular-families.html), for the commutation and the two centralisers.
- [Operator Family Conventions](conventions-of-the-operator-families.html), for the letter $R$, the slots and the matrix letters.
