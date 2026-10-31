# __Matrix Representations : The Product, the Trace and the Determinant__

## Introduction

**The subject.** The product, the trace and the determinant of a biquaternion, read in the three displays of the series: the $2\times2$ entry model, the $4\times4$ coefficient frame and the $4\times4$ block frame.

**The result in one line.** The product is multiplicative in every display. The trace doubles from $2Q_t$ to $4Q_t$. The determinant squares from $\langle\tilde Q\rangle_{\natural}$ to $\langle\tilde Q\rangle_{\natural}^2$.

**Why the numbers double.** The $4\times4$ operator is two copies of the $2\times2$ element. A block-diagonal matrix with two equal blocks has the trace of one doubled and the determinant of one squared. Every doubling in this article has that single cause.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$ and $\vec e_k^2=-e_t$. An element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu\in\mathbb{C}$ and $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. The central scalar is $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ with $B^2=Q_x^2+Q_y^2+Q_z^2$. The bracket, the change law and the frame change $C_{\Pi}$ are those of *Matrix Representations : The Models and the Change of Frame*.

**Boundaries.** The multiplication table is *The Biquaternion Algebra*; the six subspaces are *The Six Subspaces*; the displays and their frames are fixed in this article and in *Matrix Representations : The Models and the Change of Frame*.

## Common Aspects

The element and the operator are different objects, and the numbers attached to them differ for one reason: the operator is two copies of the element. The product is multiplicative in every display, the trace doubles from $2Q_t$ to $4Q_t$, and the determinant squares from $\langle\tilde Q\rangle_{\natural}$ to $\langle\tilde Q\rangle_{\natural}^2$. The laws of this section are stated once, without a display; the three sections below write the matrices.

**Multiplicativity.** For all elements $\tilde Q_1,\tilde Q_2$ and every integer $n$,

$$
\mathsf M(\tilde Q_1\tilde Q_2)=\mathsf M(\tilde Q_1)\mathsf M(\tilde Q_2),
\qquad
\mathsf M(\tilde Q^n)=\mathsf M(\tilde Q)^n,
\qquad
\mathsf M(\tilde Q^{-1})=\mathsf M(\tilde Q)^{-1},
$$

the last when $\tilde Q$ is invertible. The identity holds in the entry model because that model is an algebra isomorphism, and in either operator frame because left multiplication is a representation. It is the same law in all three displays.

**The trace sees the scalar part.** The trace is $2Q_t$ for the element and $4Q_t$ for the operator. The three vector coefficients do not enter. The trace is the matrix reading of the projection onto $\mathbb{C}e_t$, and it vanishes exactly on the traceless part $\vec Q$. The factor is exactly two, because $4Q_t=2\cdot2Q_t$.

**The determinant sees the whole element.** The determinant is $\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ for the element and $\langle\tilde Q\rangle_{\natural}^2$ for the operator. It vanishes exactly on the null cone, and its zero set is the null cone. The squaring is the determinant of two equal blocks.

**The eigenvalues.** The element has the two eigenvalues $\lambda_\pm=Q_t\pm iB$, with $B^2=Q_x^2+Q_y^2+Q_z^2$. The operator has each of them twice. Every multiplicity in the operator is double, and the determinant is $\lambda_+^2\lambda_-^2$.

**The invertibility criterion.** The following are equivalent: $\tilde Q$ is invertible; $\langle\tilde Q\rangle_{\natural}\neq0$; $\mathsf M_2(\tilde Q)$ is invertible; $\mathsf M_4^{L}(\tilde Q)$ is invertible. The first three agree because $\mathsf M_2$ is an isomorphism and $\det\mathsf M_2=\langle\tilde Q\rangle_{\natural}$; the fourth agrees with the third because $\det\mathsf M_4^{L}=\langle\tilde Q\rangle_{\natural}^2$ and the two blocks are equal.

**The rank is even.** When $\langle\tilde Q\rangle_{\natural}=0$ the element is singular and both matrices are singular. The rank of the operator is $0$, $2$ or $4$, never $1$ or $3$, because its two blocks are equal; it is twice the rank of the element.

**The centre.** The centre of the algebra is $\mathbb{C}e_t$, and its image is $\mathbb{C}\mathrm I_2$ in the entry model and $\mathbb{C}\mathrm I_4$ in either operator frame. The matrices commuting with the image form a larger space, of complex dimension four; the centre is the intersection of the image with that space.

## The Coefficient Frame

**The coefficient frame.** The frame is $\mathcal{B}=(e_t,\vec e_x,\vec e_y,\vec e_z)$, the frame of the structure constants. The identity is $L_t=\mathrm I_4$, and the three vector units act by signed permutations:

$$
L_x=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},
\qquad
L_y=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},
\qquad
L_z=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
$$

Each column is one unit times $e_\mu$, so the signs are the signs of the multiplication table and nothing else. The matrix of a general element is $L_{\tilde Q}=Q_t\mathrm I_4+Q_xL_x+Q_yL_y+Q_zL_z$.

**The product.** The product of two signed permutations is a signed permutation, and this is the coefficient-frame form of multiplicativity. No factor $i$ and no complex entry appears: the coefficient display is real in the signed sense, and its entries are the four coefficients with signs.

**The trace and the determinant.** The trace is $\operatorname{tr}L_{\tilde Q}=4Q_t$, the sum of the four diagonal entries of the display. The determinant is $\langle\tilde Q\rangle_{\natural}^2$. The coefficient frame agrees with the block frame on both numbers, because the change $C_{\Pi}$ contributes $\det C_{\Pi}$ and $\det C_{\Pi}^{-1}$, which cancel.

**The inverse.** The inverse in the coefficient frame is the conjugate of the block inverse,

$$
[L_{\tilde Q}^{-1}]_{\mathrm{coef}}=C_{\Pi}\,\bigl(\mathrm I_2\otimes\mathsf M_2(\tilde Q)^{-1}\bigr)\,C_{\Pi}^{-1},
$$

which is the display of the operator of $\tilde Q^{-1}$ by multiplicativity.

## The Entry Model

**The assignment.** On the basis, with $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$,

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

The standard basis of $M_2(\mathbb{C})$ is the matrix-unit basis, so the four entries are the coordinates of the matrix in that basis: two diagonal and two off-diagonal.

**Why the factor $i$ is forced.** The images of the vector units must square to $-\mathrm I_2$ and obey the cross-relations. The real matrices $\sigma_1,\sigma_2,\sigma_3$ square to $+\mathrm I_2$; the factor $i$ is the only scalar that repairs the sign. The cross-relations then fix the three matrices up to one common conjugation. Any two isomorphisms $\mathbb{B}\to M_2(\mathbb{C})$ differ by conjugation by an element of $GL_2(\mathbb{C})$, and the display above is the representative in which the standard pair is diagonal.

**The product.** The assignment is an algebra isomorphism, so $\mathsf M_2$ carries the product, the powers and the inverse of the algebra to the same operations on matrices. Since the four images are linearly independent over $\mathbb{C}$ and both spaces have dimension four, the isomorphism is onto as well.

**The trace and the determinant.** The trace is $2Q_t$ and the determinant is

$$
\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}
=(Q_t-iB)(Q_t+iB)=Q_t^2+B^2 .
$$

The two eigenvalues of the display are $\lambda_\pm=Q_t\pm iB$.

**The inverse and the adjugate.** When $\langle\tilde Q\rangle_{\natural}\neq0$,

$$
\mathsf M_2(\tilde Q)^{-1}=\frac{\operatorname{adj}\mathsf M_2(\tilde Q)}{\langle\tilde Q\rangle_{\natural}},
\qquad
\operatorname{adj}\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}d&-b\\-c&a\end{pmatrix}.
$$

The identity $\mathsf M_2(\tilde Q)\operatorname{adj}\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}\mathrm I_2$ is the matrix form of $\tilde Q\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}e_t$. The adjugate is the image of ${}^{\natural}$, and division by the determinant is the matrix form of division by the central scalar.

**The centre.** A matrix commuting with every matrix is scalar, so the centre of the image is $\mathbb{C}\mathrm I_2$, the image of $\mathbb{C}e_t$.

## The Block Frame

**The block form.** In the block frame the left regular matrix is one object,

$$
\mathsf M_4^{L}(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q)
=\operatorname{diag}\bigl(\mathsf M_2(\tilde Q),\mathsf M_2(\tilde Q)\bigr).
$$

The carrier is two copies of the $2\times2$ space, and the element acts by the same block on each copy. The coefficient display is the conjugate of this matrix by $C_{\Pi}$ and is written in the section above.

**The product.** The Kronecker product multiplies block by block:

$$
\bigl(\mathrm I_2\otimes\mathsf M_2(\tilde Q_1)\bigr)\bigl(\mathrm I_2\otimes\mathsf M_2(\tilde Q_2)\bigr)
=\mathrm I_2\otimes\bigl(\mathsf M_2(\tilde Q_1)\mathsf M_2(\tilde Q_2)\bigr).
$$

The product of two regular operators is the regular operator of the product, and the block identity is the entry identity read twice.

**The trace and the determinant.** The trace is $4Q_t$, the sum of the traces of the two equal blocks. The determinant is $\det(\mathrm I_2\otimes\mathsf M_2)=\det(\mathsf M_2)^2=\langle\tilde Q\rangle_{\natural}^2$. The four eigenvalues are $\lambda_\pm$, each twice, and $\lambda_+^2\lambda_-^2=\langle\tilde Q\rangle_{\natural}^2$.

**The inverse and the rank.** The inverse is $\mathrm I_2\otimes\mathsf M_2(\tilde Q)^{-1}$, the block-diagonal copy of the entry inverse, and it exists exactly when $\langle\tilde Q\rangle_{\natural}\neq0$. When it does not, the rank is $0$ or $2$, because the two blocks are equal; it is never $1$ or $3$.

**The centre.** The centre of the image is $\mathbb{C}\mathrm I_4$. It is not larger than the centre of the ambient $M_4(\mathbb{C})$, which is also $\mathbb{C}\mathrm I_4$: the image meets the ambient centre in the scalars and has no other central matrix.

## Summary

The element has one $2\times2$ matrix and the operator has a $4\times4$ matrix in each frame. The product is multiplicative in all three displays. The trace is $2Q_t$ in the entry model and $4Q_t$ in either operator frame. The determinant is $\langle\tilde Q\rangle_{\natural}$ in the entry model and $\langle\tilde Q\rangle_{\natural}^2$ in either operator frame. The doubling and the squaring have one cause: the operator is two copies of the element.

The invertibility criterion is the same in every display: $\langle\tilde Q\rangle_{\natural}\neq0$. The inverse is the adjugate over the central scalar in the entry model, and the block-diagonal copy of that inverse in the block frame. The rank of the operator is even, $0$, $2$ or $4$, and it is twice the rank of the element.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf M_2(\tilde Q)$ | the $2\times2$ entry model of the element |
| $\mathsf M_4^{L}(\tilde Q)$ | the $4\times4$ left regular matrix of the element |
| $[\mathsf M_4^{L}]_{\mathrm{coef}}$ | the same operator in the coefficient frame |
| $C_{\Pi}$ | the frame change, $\det C_{\Pi}=-\tfrac14$ |
| $\langle\tilde Q\rangle_{\natural}$ | the central scalar $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ |
| $B^2$ | $Q_x^2+Q_y^2+Q_z^2$ |
| $\lambda_\pm$ | $Q_t\pm iB$, the eigenvalues |
| $\operatorname{adj}$ | the classical adjugate, the image of ${}^{\natural}$ |
| $L_\mu$ | $\mathsf M_4^{L}(e_\mu)$, the matrix of a unit |

## Further Reading

- [Matrix Representations : The Models and the Change of Frame](matrix-representations-the-models-and-the-change-of-frame.html), for the bracket, the two frames and $C_{\Pi}$.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the multiplication table.
- [Matrix Algebras](matrix-algebras.html), for the structure of $M_n(\mathbb{C})$.
- [Matrix Representations : The Six Subspaces as Matrix Conditions](matrix-representations-the-six-subspaces-as-matrix-conditions.html), for the subspaces read on the matrix.