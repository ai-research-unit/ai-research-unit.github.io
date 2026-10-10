# __The Symmetric Quaternionic Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$__

## Introduction

The symmetric quaternionic multiplication is the central-valued operation $\tilde P\star\tilde Q=B(\tilde P,\tilde Q)e_0$ (*Introduction to the Symmetric Quaternionic Algebra of Biquaternions*). This article reads the operation in the $4\times4$ left regular model, the left regular matrix $\mathsf{M}_4$ of *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*; it is the second of the two representation articles of the block, and its companion *The Symmetric Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* reads the same operation on the realisation $\mathsf{M}_2$. In the model the product of two elements becomes the symmetrisation of a product of left multiplications, the transpose carries the quaternion conjugation, and the value is a scalar matrix whose coefficient is the quaternion form $B$; the article records the trace and the rank of the resulting endomorphism and the matrix form of the form.

The model itself, the regular matrix $\mathsf{M}_4$, the trace $\operatorname{Tr}\mathsf{M}_4(\tilde Q)=4Q_0$, the determinant $\det\mathsf{M}_4(\tilde Q)=N(\tilde Q)^2$ and the matrix of the conjugation as the transpose are those of the cited articles and are used here, not restated. The form $B$ and its Gram matrix are *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*; the operators are *The Multiplication Operators of the Symmetric Quaternionic Algebra*; the normal forms of the singular matrices are *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*. Nothing of the enriched layer is used.

**Conventions.** The product is $\tilde P\star\tilde Q=B(\tilde P,\tilde Q)e_0$ with $B(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$; the left regular matrix is $\mathsf{M}_4(\tilde P)$, whose $m$-th column is the coordinate column of the product $\tilde P e_m$, with $\mathsf{M}_4(\tilde P^\natural)=\mathsf{M}_4(\tilde P)^{\mathsf T}$ in the basis and $\mathsf{M}_2(e_k)=-i\sigma_k$ in the companion model.

## The Symmetrisation of the Left Multiplications

**Proposition (the symmetrisation of the left multiplications).** In the basis $e_0,e_1,e_2,e_3$ the
left-regular representation satisfies $\mathsf{M}_4(\tilde P^\natural)=\mathsf{M}_4(\tilde P)^{\mathsf T}$, and for all
$\tilde P,\tilde Q$,

$$
\tfrac12\Bigl(\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)
+ \mathsf{M}_4(\tilde Q)^{\mathsf T}\mathsf{M}_4(\tilde P)\Bigr)
= \mathsf{M}_4\bigl(\tilde P\star\tilde Q\bigr) = B(\tilde P,\tilde Q)\,I_4 .
$$

*Proof.* The left-regular representation is multiplicative, so
$\mathsf{M}_4(\tilde P^{\natural}\tilde Q)=\mathsf{M}_4(\tilde P^\natural)\mathsf{M}_4(\tilde Q)=\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)$; the half-sum is $\mathsf{M}_4$ of the product, and the value is
central, so the matrix is the scalar matrix $B(\tilde P,\tilde Q)I_4$. The transpose identity is read on the
basis: for $\tilde P=e_1$ the matrix $\mathsf{M}_4(e_1)$ and its transpose are opposite, $\mathsf{M}_4(e_1)^{\mathsf T}=-\mathsf{M}_4(e_1)=\mathsf{M}_4(e_1^\natural)$,
and the general case follows by linearity. Verified on random pairs. $\square$

**Corollary (trace of the value).** Taking the trace of the display,

$$
\operatorname{Tr}\mathsf{M}_4\bigl(\tilde P\star\tilde Q\bigr) = 4\,B(\tilde P,\tilde Q),
$$

so the quaternion form is a quarter of the trace of the matrix of the value, and the value is recovered from its
trace as $\mathsf{M}_4(\tilde P\star\tilde Q)=\tfrac14\operatorname{Tr}\mathsf{M}_4(\tilde P\star\tilde Q)\,I_4$. Verified on the model.

**Corollary (the regular endomorphism).** Fix $\tilde A$ and let $A=\mathsf{M}_4(\tilde A)$. On the image of the
regular representation — the matrices $\mathsf{M}_4(\tilde Q)$ — the map is the transport of the multiplication
$L^{\star}_{\tilde A}$:

$$
X=\mathsf{M}_4(\tilde Q)\quad\Longrightarrow\quad
\tfrac12\bigl(A^{\mathsf T}X+X^{\mathsf T}A\bigr)
= \mathsf{M}_4\bigl(\tilde A\star\tilde Q\bigr) = B(\tilde A,\tilde Q)\,I_4 ,
$$

because $X^{\mathsf T}=\mathsf{M}_4(\tilde Q)^\natural$ on the image of $\mathsf{M}_4$ by the transpose identity above. On
that four-dimensional space the map has image the line $\mathbb{C}I_4$ of the scalar matrices, rank $1$ for
$\tilde A\ne0$ and trace $\tilde A_0$. The same formula read on the whole of $M_4(\mathbb{C})$ is a larger map:
there $X^{\mathsf T}$ is not the conjugation of an element of $\mathbb{B}$, the image leaves the scalar
matrices, and the rank is larger than one (it is $5$ for $\tilde A=e_1$ and $7$ for a generic $\tilde A$). The
two models differ here because the $2\times2$ realisation is onto $M_2(\mathbb{C})$ — there "all matrices" and
"the image of the realisation" are the same set — while $\mathsf{M}_4(\mathbb{B})$ is a four-dimensional subspace of
the sixteen-dimensional $M_4(\mathbb{C})$. The rank-one statement is a statement about the transport of the
multiplication, not about the formula on arbitrary matrices.

*Proof.* For $X=\mathsf{M}_4(\tilde Q)$ one has $A^{\mathsf T}X=\mathsf{M}_4(\tilde A^\natural)\mathsf{M}_4(\tilde Q)=\mathsf{M}_4(\tilde A^\natural\tilde Q)$
and $X^{\mathsf T}A=\mathsf{M}_4(\tilde Q^\natural)\mathsf{M}_4(\tilde A)=\mathsf{M}_4(\tilde Q^\natural\tilde A)$, so the
half-sum is $\mathsf{M}_4(\tilde A\star\tilde Q)=B(\tilde A,\tilde Q)I_4$. The rank is $1$ because the image is a
nonzero line for $\tilde A\ne0$ (the image of $X=\mathsf{M}_4(e_\mu)$ is $\tilde A_\mu I_4$) and the trace on the
image of $\mathsf{M}_4$ is the coefficient of $\mathsf{M}_4(e_0)$, namely $B(\tilde A,e_0)=\tilde A_0$. On the whole of
$M_4(\mathbb{C})$ the map is larger: on the sixteen matrix units its rank is $5$ for $\tilde A=e_1$ and $7$ for
a generic $\tilde A$, so the rank-one statement must not be read on arbitrary matrices. Verified on the model
and on the sixteen matrix units. $\square$

**Remark (the regular model explains the centrality).** The regular model exhibits the reason for the
centrality more plainly than the realisation: the four-dimensional regular representation is faithful, and the
transpose of a left multiplication is the left multiplication by the conjugate, which is the identity
$\mathsf{M}_4(\tilde P^\natural)=\mathsf{M}_4(\tilde P)^{\mathsf T}$ that makes the symmetrisation central.

## The Matrix Form of the Form

**Proposition (the form as a trace pairing).** The quaternion form reads

$$
B(\tilde P,\tilde Q) = \tfrac14\operatorname{Tr}\Bigl(\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)\Bigr),
$$

so the form in the model is a quarter of the trace pairing $\operatorname{Tr}(\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q))$.

*Proof.* The identity is the trace of $\mathsf{M}_4(\tilde P^{\natural}\tilde Q)$, whose trace is
$4\operatorname{Sc}(\tilde P^{\natural}\tilde Q)=4B(\tilde P,\tilde Q)$. Verified on random pairs. $\square$

**Proposition (the isotropic cone).** An element is isotropic, $N(\tilde Q)=0$, exactly when its image is singular:

$$
N(\tilde Q)=0 \quad\Longleftrightarrow\quad \det\mathsf{M}_4(\tilde Q)=0 ,
$$

the determinant being $N(\tilde Q)^2$. The Gram matrix of $B$ in the basis is $I_4$.

*Proof.* $\det\mathsf{M}_4(\tilde Q)=N(\tilde Q)^2$ is the determinant of the left regular representation
(*The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*), so the determinant vanishes together with $N$. The Gram matrix is the table of
*The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*. $\square$

**Remark (the definite rows in the model).** Under $\mathsf{M}_4$ the definite rows are read through the subspace
conditions of the representation articles: the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the fixed
space of complex conjugation, is the set of elements with real coefficients, on which the form is positive
definite, and the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ is its image under the multiplication by
$i$, on which the form is negative definite. The regular matrix of an element of $\mathbb{H}_{\mathbb{B}}$ is a real
$4\times4$ matrix, and the regular matrix of an element of $i\mathbb{H}_{\mathbb{B}}$ is purely imaginary; the
correspondence is the one of *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*, which owns the subspace conditions.

## Worked Examples

**The unit and a vector.** For $\tilde P=e_0$ and $\tilde Q=e_1$ the product is $B(e_0,e_1)e_0=0$, and the
matrix identity reads $\tfrac12(\mathsf{M}_4(e_1)^{\mathsf T}+\mathsf{M}_4(e_1))=0$, the two summands being opposite
because $\mathsf{M}_4(e_1)^{\mathsf T}=-\mathsf{M}_4(e_1)=\mathsf{M}_4(e_1^\natural)$.

**A central pair.** For $\tilde P=e_0$, $\tilde Q=ie_0$ the product is $ie_0$ and the coefficient is $B=i$;
the matrix of the value is $iI_4$, of trace $4i$ and determinant $i^4=1=N(ie_0)^2$.

**A vector square.** For $\tilde P=\tilde Q=e_1$ the product is $e_0$, and the identity gives
$\mathsf{M}_4(e_1)^{\mathsf T}\mathsf{M}_4(e_1)=I_4$, since $\mathsf{M}_4(e_1)$ is invertible of determinant $N(e_1)^2=1$; the
symmetrisation of the product with itself is the product itself and equals $I_4$.

**An isotropic element.** For $\tilde Q=e_0+ie_1$ the norm is $N=1+i^2=0$, so $\mathsf{M}_4(\tilde Q)$ is singular of
rank two and the matrix identity gives
$\tfrac12(\mathsf{M}_4(\tilde Q)^{\mathsf T}\mathsf{M}_4(\tilde Q)+\mathsf{M}_4(\tilde Q)^{\mathsf T}\mathsf{M}_4(\tilde Q))=0$,
the zero scalar matrix, although $\mathsf{M}_4(\tilde Q)\ne0$.

**A pair with a real coefficient.** For $\tilde P=e_0+e_1$ and $\tilde Q=e_0-e_1$ the coefficient is
$B=1-1=0$, so the symmetrised matrix product vanishes: two nonzero matrices symmetrise to $0$. The two are the
images of conjugate directions, and their images are related by the transpose, which is why the cross terms
cancel in the symmetrisation.

## The Matrices

**The generators.** The regular model is fixed on the basis by four matrices:

$$
\mathsf{M}_4(e_0)=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},\qquad
\mathsf{M}_4(e_1)=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},
$$
$$
\mathsf{M}_4(e_2)=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\qquad
\mathsf{M}_4(e_3)=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
$$

A general element is the block matrix

$$
\mathsf{M}_4(\tilde Q)=\begin{pmatrix}A&B\\-B&A\end{pmatrix},\qquad
A=\begin{pmatrix}Q_0&-Q_1\\Q_1&Q_0\end{pmatrix},\qquad
B=\begin{pmatrix}-Q_2&-Q_3\\-Q_3&Q_2\end{pmatrix},
$$

with $\operatorname{Tr}\mathsf{M}_4(\tilde Q)=4Q_0$ and $\det\mathsf{M}_4(\tilde Q)=N(\tilde Q)^2$.

**The value, entry by entry.** The transposition is the trace-complement of the regular matrix, $X^{\mathsf T}=\tfrac12(\operatorname{Tr}X)I_4-X$, and the symmetrisation of the two transposed products reduces to the same scalar-plus-anticommutator expression as in the realization,

$$
\tfrac12\Bigl(\mathsf{M}_4(\tilde P)^{\mathsf{T}}\mathsf{M}_4(\tilde Q)+\mathsf{M}_4(\tilde Q)^{\mathsf{T}}\mathsf{M}_4(\tilde P)\Bigr)
=P_0Y+Q_0X-\tfrac12\bigl\{X,Y\bigr\}
=B(\tilde P,\tilde Q)\,I_4,
$$

the two models sharing the expression with the transposition in the place of the adjugation. At the pair $e_1,e_1$ it reads $\mathsf{M}_4(e_1)^{\mathsf{T}}\mathsf{M}_4(e_1)=-(-\mathsf{M}_4(e_1)^2)=I_4=B(e_1,e_1)I_4$.

**The trace of the value, entry by entry.** The trace of the value is four times the form, $\operatorname{Tr}\mathsf{M}_4(\tilde P\star\tilde Q)=4B(\tilde P,\tilde Q)$; at the isotropic element $e_0+ie_1$ the regular matrix is singular of rank two and the value is the zero scalar matrix.

**The rank of the transported operator.** On the image of the regular representation the map $X\mapsto\tfrac12(X^{\mathsf T}A+A^{\mathsf T}X)$ has rank one for $\tilde A\neq0$, the image being the scalar line; on the whole of $M_4(\mathbb{C})$ the same formula has rank larger than one, because the transposition there is not the involution of an element of $\mathbb{B}$ and the image leaves the scalar matrices.

## Summary

In the $4\times4$ regular model the symmetric quaternionic multiplication reads
$\tfrac12(\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)+\mathsf{M}_4(\tilde Q)^{\mathsf T}\mathsf{M}_4(\tilde P))=B(\tilde P,\tilde Q)I_4$,
the transpose being the matrix of the quaternion conjugation, and the trace of the value is $4B(\tilde P,\tilde Q)$;
the transport of the multiplication on the image of
$\mathsf{M}_4$, $X=\mathsf{M}_4(\tilde Q)\mapsto\tfrac12(\mathsf{M}_4(\tilde A)^{\mathsf T}X+X^{\mathsf T}\mathsf{M}_4(\tilde A))$, has
image the scalar matrices, rank $1$ and trace $\tilde A_0$, while on the whole of $M_4(\mathbb{C})$ the same
formula is a larger map (rank $5$ at $\tilde A=e_1$ and $7$ generically). The form is a quarter of the trace of
the twisted matrix product, $B=\tfrac14\operatorname{Tr}(\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q))$; the isotropic elements are exactly the
singular matrices, the determinant of the model being $N(\tilde Q)^2$; the Gram matrix in the basis is $I_4$; and
the definite rows are read through the subspace conditions of the representation articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_4(\tilde P)$ | the left regular matrix, $\det\mathsf{M}_4(\tilde Q)=N(\tilde Q)^2$ |
| $\mathsf{M}_4(\tilde P^\natural)=\mathsf{M}_4(\tilde P)^{\mathsf T}$ | the conjugation as the transpose in the model |
| $\tfrac12(\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)+\mathsf{M}_4(\tilde Q)^{\mathsf T}\mathsf{M}_4(\tilde P))=B(\tilde P,\tilde Q)I_4$ | the product in the model |
| $\operatorname{Tr}\mathsf{M}_4(\tilde P\star\tilde Q)=4B(\tilde P,\tilde Q)$ | the trace of the value |
| $B=\tfrac14\operatorname{Tr}(\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q))$ | the form as a trace pairing |
| $N(\tilde Q)=0\Longleftrightarrow\det\mathsf{M}_4(\tilde Q)=0$ | the isotropic cone as the singular matrices |

## Further Reading

- *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_maths/introduction-to-the-4x4-matrix-element-representation-of-biquaternions.md`), for the construction of the regular model
- *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_maths/the-4x4-matrix-element-representation-of-biquaternions.md`), for the regular model and its determinant
- *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra* (`articles_maths/the-quaternion-form-as-a-product-on-the-symmetric-quaternionic-algebra.md`), for the form $B$ and its Gram matrix
- *The Multiplication Operators of the Symmetric Quaternionic Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-algebra.md`), for the operators transported by the model
- *The Symmetric Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-symmetric-quaternionic-algebra-in-the-2x2-matrix-element-representation.md`), for the reading on the realisation
- *Introduction to the Symmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-biquaternions.md`), for the operation itself
