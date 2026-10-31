# __Matrix Representations : The Product, the Trace and the Determinant__

## Introduction

**The subject.** The product, the trace and the determinant of a biquaternion, read in the three displays of the series: the $2\times2$ entry model, the $4\times4$ coefficient frame and the $4\times4$ Peirce frame.

**The result in one line.** The product is multiplicative in every display. The trace doubles from $2Q_t$ to $4Q_t$. The determinant squares from $\langle\tilde Q\rangle_{\natural}$ to $\langle\tilde Q\rangle_{\natural}^2$.

**Why the numbers double.** The $4\times4$ operator is two copies of the $2\times2$ element. A block-diagonal matrix with two equal blocks has the trace of one doubled and the determinant of one squared. Every doubling in this article has that single cause.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$ and $\vec e_k^2=-e_t$. An element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu\in\mathbb{C}$ and $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. The central scalar is $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ with $B^2=Q_x^2+Q_y^2+Q_z^2$. The bracket, the change law and the Peirce change $C_{\Pi}$ are those of *Matrix Representations : The Models and the Change of Frame*.

**Boundaries.** The four products and the four traces are *Matrix Representations : The Four Words and the Four Traces*; the characteristic polynomial and the norms are *Matrix Representations : Trace, Determinant and the Biquaternion Norm*; the units and the group are *Matrix Representations : $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant*.

## The Element and the Operator

**One element, two displays.** The element $\tilde Q$ has one $2\times2$ matrix and no frame. The operator $L_{\tilde Q}$ has a $4\times4$ matrix in each frame and no $2\times2$ matrix. This article writes both, and it keeps them apart by the glyph.

**The entry model.** On the basis,

$$
\mathsf M_2(e_t)=\mathrm I_2,\qquad
\mathsf M_2(\vec e_x)=-i\sigma_1,\qquad
\mathsf M_2(\vec e_y)=-i\sigma_2,\qquad
\mathsf M_2(\vec e_z)=-i\sigma_3,
$$

so that

$$
\mathsf M_2(\tilde Q)
=\begin{pmatrix}Q_t-iQ_z&-iQ_x-Q_y\\-iQ_x+Q_y&Q_t+iQ_z\end{pmatrix}.
$$

**The operator model.** In the Peirce frame,

$$
\mathsf M_4^{L}(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q)
=\operatorname{diag}\bigl(\mathsf M_2(\tilde Q),\mathsf M_2(\tilde Q)\bigr),
$$

and in the coefficient frame,

$$
[\mathsf M_4^{L}(\tilde Q)]_{\mathrm{coef}}
=C_{\Pi}\,\bigl(\mathrm I_2\otimes\mathsf M_2(\tilde Q)\bigr)\,C_{\Pi}^{-1}.
$$

Both displays are the same operator. The second is the first with its entries rewritten, not a second operator.

## The Product

**The entry model.** The assignment is an algebra isomorphism, so for all elements

$$
\mathsf M_2(\tilde Q_1\tilde Q_2)=\mathsf M_2(\tilde Q_1)\mathsf M_2(\tilde Q_2),
\qquad
\mathsf M_2(\tilde Q^n)=\mathsf M_2(\tilde Q)^n,
\qquad
\mathsf M_2(\tilde Q^{-1})=\mathsf M_2(\tilde Q)^{-1},
$$

the last when $\langle\tilde Q\rangle_{\natural}\neq0$. The proof is the multiplication table: the three vector images square to $-\mathrm I_2$ and multiply cyclically, which are the relations of the algebra. Since the four images are linearly independent over $\mathbb{C}$ and both spaces have dimension four, the isomorphism is onto as well.

**The operator model.** Left multiplication is a representation, so

$$
\mathsf M_4^{L}(\tilde Q_1\tilde Q_2)=\mathsf M_4^{L}(\tilde Q_1)\mathsf M_4^{L}(\tilde Q_2).
$$

In the Peirce frame the identity is the Kronecker product of two copies of the entry identity:

$$
\bigl(\mathrm I_2\otimes\mathsf M_2(\tilde Q_1)\bigr)\bigl(\mathrm I_2\otimes\mathsf M_2(\tilde Q_2)\bigr)
=\mathrm I_2\otimes\bigl(\mathsf M_2(\tilde Q_1)\mathsf M_2(\tilde Q_2)\bigr).
$$

**The coefficient frame.** In the unit basis the matrices of the units are signed permutations. For the three vector units,

$$
L_x=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},
\qquad
L_y=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},
\qquad
L_z=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix},
$$

and $L_t=\mathrm I_4$. Each column is one unit times $e_\mu$, so the signs are the signs of the multiplication table and nothing else. The product of two signed permutations is a signed permutation, which is the coefficient-frame statement of multiplicativity.

**What the coefficient display shows.** The signs. The Peirce display shows the two copies. Neither shows the other, and the product rule is the same rule in both.

## The Trace

**Definition.** The trace of the element is the trace of its $2\times2$ matrix; the trace of the operator is the trace of its $4\times4$ matrix in any frame.

**The entry model.**

$$
\operatorname{tr}\mathsf M_2(\tilde Q)=2Q_t .
$$

**The operator model.**

$$
\operatorname{tr}\mathsf M_4^{L}(\tilde Q)=4Q_t,
$$

in either frame, because the trace is invariant under $C_{\Pi}^{-1}(\cdot)C_{\Pi}$ and in the Peirce frame it is the trace of two equal blocks.

**What the trace sees.** The scalar part, and only the scalar part. The three vector coefficients do not enter. The trace is therefore the matrix reading of the projection onto $\mathbb{C}e_t$, and it vanishes exactly on the traceless part $\vec Q$.

**The factor two.** $4Q_t=2\cdot2Q_t$: the operator trace is the element trace read twice. No other factor appears, and the doubling is the only content of the comparison.

## The Determinant

**The entry model.** The determinant is the central scalar:

$$
\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}
=Q_t^2+Q_x^2+Q_y^2+Q_z^2 .
$$

It is the product of the two eigenvalues $Q_t\pm iB$:

$$
(Q_t-iB)(Q_t+iB)=Q_t^2+B^2=\langle\tilde Q\rangle_{\natural}.
$$

**The operator model.** The determinant is the square:

$$
\det\mathsf M_4^{L}(\tilde Q)=\langle\tilde Q\rangle_{\natural}^2 .
$$

In the Peirce frame it is $\det\bigl(\mathrm I_2\otimes\mathsf M_2(\tilde Q)\bigr)=\det\bigl(\mathsf M_2(\tilde Q)\bigr)^2$; the coefficient frame agrees because $\det C_{\Pi}$ and $\det C_{\Pi}^{-1}$ cancel.

**The four eigenvalues.** The operator has $\lambda_\pm=Q_t\pm iB$, each twice, so its determinant is $\lambda_+^2\lambda_-^2=\langle\tilde Q\rangle_{\natural}^2$. The element has each eigenvalue once. The spectrum of the operator is the spectrum of the element with every multiplicity doubled.

**What the determinant sees.** The whole element, scalar and vector part together. It vanishes exactly on the null cone, and it is the polynomial whose zero set is the singular locus.

## The Unit Criterion

**The criterion.** The following are equivalent: $\tilde Q$ is a unit; $\langle\tilde Q\rangle_{\natural}\neq0$; $\mathsf M_2(\tilde Q)$ is invertible; $\mathsf M_4^{L}(\tilde Q)$ is invertible.

*Proof.* The first three are equivalent because $\mathsf M_2$ is an isomorphism and $\det\mathsf M_2=\langle\tilde Q\rangle_{\natural}$. The fourth is equivalent to the third because $\det\mathsf M_4^{L}=\langle\tilde Q\rangle_{\natural}^2$, which vanishes exactly when $\langle\tilde Q\rangle_{\natural}$ does, and because the two blocks are equal.

**The inverses.** In the entry model,

$$
\mathsf M_2(\tilde Q)^{-1}=\frac{\operatorname{adj}\mathsf M_2(\tilde Q)}{\langle\tilde Q\rangle_{\natural}},
\qquad
\operatorname{adj}\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}d&-b\\-c&a\end{pmatrix}.
$$

In the operator model, in the Peirce frame,

$$
\mathsf M_4^{L}(\tilde Q)^{-1}=\mathrm I_2\otimes\mathsf M_2(\tilde Q)^{-1}
=\mathrm I_2\otimes\frac{\operatorname{adj}\mathsf M_2(\tilde Q)}{\langle\tilde Q\rangle_{\natural}},
$$

and in the coefficient frame it is the conjugate of that matrix. The inverse of the operator is the operator of the inverse, by multiplicativity.

**The adjugate is the conjugation.** The identity
$$
\mathsf M_2(\tilde Q)\operatorname{adj}\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}\mathrm I_2
$$
is the matrix form of $\tilde Q\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}e_t$. The adjugate is the image of ${}^{\natural}$, and the division by the determinant is the matrix form of dividing by the norm.

**The zero divisors.** When $\langle\tilde Q\rangle_{\natural}=0$ the element is a zero divisor, the $2\times2$ matrix is singular, and the $4\times4$ matrix is singular of rank $0$ or $2$. The rank can never be $1$ or $3$, because the two blocks are equal; the rank stratification of the operator is the even refinement of the element's.

## The Centre

**The entry model.** A matrix commuting with every matrix is scalar, so the centre of $M_2(\mathbb{C})$ is $\mathbb{C}\mathrm I_2$, the image of $\mathbb{C}e_t$.

**The operator model.** The centre of the image is $\mathbb{C}\mathrm I_4$. It is not the centre of $M_4(\mathbb{C})$, which is also $\mathbb{C}\mathrm I_4$: the image meets the ambient centre in the scalars and has no other central matrix.

**The centraliser is larger.** The matrices commuting with the whole image are the right regular matrices, of complex dimension four. The centre is the intersection of the left and right images. The statement is proved in *Matrix Representations : The Centraliser and the Double Centraliser*.

## Summary

The element has one $2\times2$ matrix and the operator has a $4\times4$ matrix in each frame. The product is multiplicative in all three displays. The trace is $2Q_t$ in the entry model and $4Q_t$ in either operator frame. The determinant is $\langle\tilde Q\rangle_{\natural}$ in the entry model and $\langle\tilde Q\rangle_{\natural}^2$ in either operator frame. The doubling and the squaring have one cause: the operator is two copies of the element.

The unit criterion is the same in every display: $\langle\tilde Q\rangle_{\natural}\neq0$. The inverse is the adjugate over the norm in the entry model, and the block-diagonal copy of that inverse in the Peirce frame. The rank of the operator is even, $0$, $2$ or $4$, and the rank stratification is the even refinement of the element's.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf M_2(\tilde Q)$ | the $2\times2$ entry model of the element |
| $\mathsf M_4^{L}(\tilde Q)$ | the $4\times4$ left regular matrix of the element |
| $[\mathsf M_4^{L}]_{\mathrm{coef}}$ | the same operator in the coefficient frame |
| $C_{\Pi}$ | the Peirce change, $\det C_{\Pi}=-\tfrac14$ |
| $\langle\tilde Q\rangle_{\natural}$ | the central scalar $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ |
| $B^2$ | $Q_x^2+Q_y^2+Q_z^2$ |
| $\lambda_\pm$ | $Q_t\pm iB$, the eigenvalues |
| $\operatorname{adj}$ | the classical adjugate, the image of ${}^{\natural}$ |
| $L_\mu$ | $\mathsf M_4^{L}(e_\mu)$, the matrix of a unit |

## Further Reading

- [Matrix Representations : The Models and the Change of Frame](matrix-representations-the-models-and-the-change-of-frame.html), for the bracket, the two frames and $C_{\Pi}$.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the multiplication table and the norm.
- [Matrix Algebras](matrix-algebras.html), for the structure of $M_n(\mathbb{C})$.
- [Matrix Representations : The Six Subspaces as Matrix Conditions](matrix-representations-the-six-subspaces-as-matrix-conditions.html), for the subspaces read on the matrix.
- [Matrix Representations : Trace, Determinant and the Biquaternion Norm](matrix-representations-trace-determinant-and-the-biquaternion-norm.html), for the characteristic polynomial and the norms.
