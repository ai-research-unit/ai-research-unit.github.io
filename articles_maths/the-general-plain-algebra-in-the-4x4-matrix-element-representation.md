
# __The General Plain Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$__

## Introduction

The left regular representation $\mathsf{M}_4$ of *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* realises the algebra on the coefficient space $\mathbb{C}^4$ by left multiplication, so that the regular matrix $\mathsf{M}_4(\tilde{Q})$ is the carrier of the element acting on the algebra itself. This article is the companion of *The General Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, and it reads the same reading group *Topology on the Introduction to the General Plain Algebra of Biquaternions* on the regular matrices instead of on the $2\times2$ matrices: the plain product becomes the product of the regular matrices, and the general plain bilinear form $\langle\tilde{P},\tilde{Q}\rangle=\mathrm{Sc}(\tilde{P}\tilde{Q})$ becomes the plain trace pairing of the regular matrices, with the factor $2$ that the dimension of the module brings.

The regular representation is the more faithful of the two carrier spaces, because it sees the algebra act and not only the algebra: it carries the left and right multiplications as two commuting copies, the natural conjugation as the transposition, and the two blocks of the fundamental decomposition as invariant subspaces. The trace pairing of the regular matrices is twice the general plain bilinear form, and the determinant of the regular matrix is the square of the determinant of the element, the two factors being the two copies of the simple module in $\mathbb{B}$.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the identity and $e_k^2=-e_0$; $\tilde{Q}=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; scalar part $\mathrm{Sc}$, sign vector $\varepsilon=(1,-1,-1,-1)$ and sign matrix $E=\operatorname{diag}(1,-1,-1,-1)$; natural conjugation ${}^{\natural}$ negating $e_1,e_2,e_3$, Hermitian conjugation ${}^{*}={}^{\natural}\circ\bar{\cdot}$.

## The Representation

**Definition.** The **left regular matrix** is the isomorphism written $\mathsf{M}_4$. It converts a biquaternion into a $4 \times 4$ complex matrix,

$$
\mathsf{M}_4:\mathbb{B}\longrightarrow M_4(\mathbb{C}),
$$

and it is fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity: in the basis $e_0,e_1,e_2,e_3$ its $m$-th column is the coordinate column of the product $\tilde{Q}e_m$. The **right regular matrix** $\mathsf{M}_4^{R}(\tilde{Q})$ is defined the same way with the product in the opposite order, its $m$-th column being the coordinate column of $e_m\tilde{Q}$. The two representation matrices satisfy

$$
\mathsf{M}_4(\tilde{P})\mathsf{M}_4(\tilde{Q})=\mathsf{M}_4(\tilde{P}\tilde{Q}),\qquad \mathsf{M}_4^{R}(\tilde{Q})=E\,\mathsf{M}_4(\tilde{Q})^{\mathsf{T}}E,\qquad \mathsf{M}_4(\tilde{Q}^{\natural})=\mathsf{M}_4(\tilde{Q})^{\mathsf{T}},
$$

and the two invariants of the regular matrix are

$$
\operatorname{Tr}\mathsf{M}_4(\tilde{Q})=4Q_0,\qquad \det\mathsf{M}_4(\tilde{Q})=\langle\tilde{Q},\tilde{Q}\rangle_{\natural}^2 .
$$

## The Plain Product in the Representation

**Theorem (the product is the product of the regular matrices).** For all biquaternions,

$$
\mathsf{M}_4(\tilde{P})\mathsf{M}_4(\tilde{Q})=\mathsf{M}_4(\tilde{P}\tilde{Q}),
$$

so the plain product of the algebra is the product of the regular matrices, and the composition of the two one-sided operators is the operator of the product, $L_{\tilde{P}}\circ L_{\tilde{Q}}=\mathsf{M}_4(\tilde{P}\tilde{Q})$.

*Proof.* The representation is defined by $L_{\tilde{Q}}(\tilde{R})=\tilde{Q}\tilde{R}$ and the associativity of the algebra: $\mathsf{M}_4(\tilde{P})L_{\tilde{Q}}(\tilde{R})=\tilde{P}(\tilde{Q}\tilde{R})=(\tilde{P}\tilde{Q})\tilde{R}$.

**The two-sided structure.** The right multiplications act on the same space and commute with the left ones, so the regular module carries the two commuting copies $\mathsf{M}_4(\mathbb{B})$ and $\mathsf{M}_4^{R}(\mathbb{B})$; the double centralizer theorem identifies each with the full commutant of the other, and the algebra decomposes as the direct sum $I_1\oplus I_2$ of two minimal left ideals. The elements of $\mathsf{M}_4^{R}(\mathbb{B})$ are exactly the conjugates of the transposes of $\mathsf{M}_4(\mathbb{B})$ by the sign matrix, by the second identity above.

## The General Plain Bilinear Form in the Representation

**Theorem (the trace pairing of the regular matrices).** For all biquaternions,

$$
\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde{P})\mathsf{M}_4(\tilde{Q})\bigr) = 2\,\langle\tilde{P},\tilde{Q}\rangle ,
$$

so the plain trace pairing of the regular matrices is twice the general plain bilinear form of the algebra.

*Proof.* The representation is a homomorphism, so $\operatorname{Tr}(\mathsf{M}_4(\tilde{P})\mathsf{M}_4(\tilde{Q}))=\operatorname{Tr}\mathsf{M}_4(\tilde{P}\tilde{Q})=4\,\mathrm{Sc}(\tilde{P}\tilde{Q})$, and the factor $2$ follows.

**Theorem (the diagonal).** On the diagonal,

$$
\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde{Q})^2\bigr) = 2\sum_\mu\varepsilon_\mu Q_\mu^2 ,
$$

the general plain bilinear invariant of the regular matrix.

**The Gram matrix, the congruence and the signature.** In the coefficient basis the Gram matrix of the pairing is the sign matrix $E=\operatorname{diag}(1,-1,-1,-1)$, and a change of basis with matrix $S$ replaces it by $S^{\mathsf T}ES$; over $\mathbb{C}$ the form is determined up to congruence by its rank alone. Over $\mathbb{R}$ the form has signature $(4,4)$ on the eight real coordinates of the coefficient space, and it is indefinite.

**The null set.** The pairing vanishes on the cone $\sum_\mu\varepsilon_\mu Q_\mu^2=0$ of real dimension $6$, the same cone as in the $2\times2$ representation; the two representations carry the same null set, because the form is transported by the two realizations of the same element.

**The automorphisms.** A matrix preserves the trace pairing exactly when $T^{\mathsf T}ET=E$, so the automorphism group on the coefficient space is $\{T\in GL_4(\mathbb{C}):T^{\mathsf T}ET=E\}=O_4(\mathbb{C})$, of complex dimension $6$ and real dimension $12$, its Lie algebra $\{X:X^{\mathsf T}E+EX=0\}$ being of real dimension $12$; its real forms $O(4)$ and $O(1,3)$ are cut out by the Hermitian and the complex conjugation on the Hermitian and the quaternion subspace. The group of real-linear automorphisms of the realified form is the larger $O(4,4)$, not the group the form defines over $\mathbb{C}$. Two operators act on the regular matrix from the algebra: the transposition $\mathsf{M}_4(\tilde{Q})\mapsto\mathsf{M}_4(\tilde{Q}^{\natural})$ carries the natural conjugation, and the conjugation $\mathsf{M}_4(\tilde{Q})\mapsto\mathsf{M}_4(\tilde{A})\mathsf{M}_4(\tilde{Q})\mathsf{M}_4(\tilde{A})^{-1}$ carries the inner automorphism of a unit; both are automorphisms of the pairing.

## Worked Examples

**The identity.** Let $\tilde{Q}=e_0$. Then $\mathsf{M}_4(e_0)=I_4$, $\operatorname{Tr}\mathsf{M}_4(e_0)=4$ and $\det\mathsf{M}_4(e_0)=1$, while $\langle e_0,e_0\rangle=1$ and $\tfrac12\operatorname{Tr}(I_4^2)=2=2\langle e_0,e_0\rangle$.

**A basis element.** Let $\tilde{Q}=e_1$. Then $\mathsf{M}_4(e_1)$ is the matrix of left multiplication by $e_1$, a signed permutation matrix of trace $0$ and determinant $1$; since $\langle e_1,e_1\rangle=-1$, the diagonal identity reads $\tfrac12\operatorname{Tr}(\mathsf{M}_4(e_1)^2)=-2=2\langle e_1,e_1\rangle$.

**A zero divisor.** Let $\tilde{Q}=e_0+ie_1$. Then $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=0$, so $\det\mathsf{M}_4(\tilde{Q})=0$ and the regular matrix is singular of rank two; the diagonal of the plain pairing is $\tfrac12\operatorname{Tr}(\mathsf{M}_4(\tilde{Q})^2)=2\langle\tilde{Q},\tilde{Q}\rangle=4$, so the singular matrix is not isotropic for the general plain bilinear form.

## The Matrices

**The generators.** The regular model is fixed on the basis by four matrices, and the whole dictionary of the chapter is a read of them:

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

The general element has trace $4Q_0$ and determinant $N(\tilde Q)^2$. The matrix is the matrix of the left multiplication $\tilde X\mapsto\tilde Q\tilde X$ on the coefficients, its $m$-th column being the coefficient vector of $\tilde Qe_m$; the two diagonal blocks $A$ carry the scalar and $e_1$ directions, the two off-diagonal blocks $B$ the $e_2$ and $e_3$ directions.

**The product, entry by entry.** The relation $e_1e_2=e_3$ is the matrix identity

$$
\mathsf{M}_4(e_1)\mathsf{M}_4(e_2)=
\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix}
\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix}
=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}=\mathsf{M}_4(e_3),
$$

and the reversed order returns $-\mathsf{M}_4(e_3)$; on a unit the square is the scalar matrix, $\mathsf{M}_4(e_1)^2=-I_4$.

**The invariants of a regular matrix.** The trace of the regular matrix of $\tilde Q$ is four times the scalar part, $\operatorname{Tr}\mathsf{M}_4(\tilde Q)=4Q_0$, its determinant is the square of the generic norm, $\det\mathsf{M}_4(\tilde Q)=N(\tilde Q)^2$, and its characteristic polynomial is the square of the two-by-two one,

$$
\det\bigl(\lambda I_4-\mathsf{M}_4(\tilde Q)\bigr)=\bigl(\lambda^2-2Q_0\lambda+N(\tilde Q)\bigr)^2,
$$

equivalently $\mathsf{M}_4(\tilde Q)^2-2Q_0\mathsf{M}_4(\tilde Q)+N(\tilde Q)I_4=0$. The transposition is the inverse up to the norm,

$$
\mathsf{M}_4(\tilde Q)^{\mathsf T}\mathsf{M}_4(\tilde Q)=N(\tilde Q)I_4,
$$

so off the isotropic cone the regular matrix is a scalar multiple of an orthogonal matrix, of inverse $N(\tilde Q)^{-1}\mathsf{M}_4(\tilde Q)^{\mathsf T}$.

**The four words.** The twelve operations of the two chapters are built from four products, and each product is a word in the two matrices $X=\mathsf{M}_4(\tilde P)$ and $Y=\mathsf{M}_4(\tilde Q)$ and in the two involutions of the model, the transposition and the conjugate transpose:

| product | first slot | second slot | the word |
|---|---|---|---|
| general plain | $X$ | $Y$ | $XY$ |
| general quaternionic | $X^{\mathsf T}$ | $Y$ | $X^{\mathsf T}Y$ |
| general plain sesquilinear | $X$ | $Y^{\dagger}$ | $XY^{\dagger}$ |
| general quaternionic sesquilinear | $X^{\mathsf T}$ | $Y^{\dagger}$ | $X^{\mathsf T}Y^{\dagger}$ |

The symmetric part of a product is the half-sum of its word and of the word with the two slots exchanged, and the antisymmetric part is the half-difference: the transposition replaces the adjugate of the two-by-two model, and the two words agree on the trace.

**The four traces.** The four products are four matrix traces, and the four forms of the algebra are read from them:

$$
\tfrac14\operatorname{Tr}(XY)=\langle\tilde P,\tilde Q\rangle,\qquad
\tfrac14\operatorname{Tr}(X^{\mathsf T}Y)=B(\tilde P,\tilde Q),\qquad
\tfrac14\operatorname{Tr}(XY^{\dagger})=H(\tilde P,\tilde Q),\qquad
\tfrac14\operatorname{Tr}(X^{\mathsf T}Y^{\dagger})=K(\tilde P,\tilde Q),
$$

the plain, the quaternionic, the Hermitian and the Krein form; the factor is $\tfrac14$ where the two-by-two model has $\tfrac12$, because the regular trace is four times the scalar part where the two-by-two trace is twice it.

## The Peirce Spaces in the Representation

The four elements $\tilde\Pi_1, \hat\Upsilon_1, \hat\Upsilon_2, \tilde\Pi_2$ of *Ideals and Peirce Decomposition of the General Plain Algebra* carry the Peirce decomposition, and their regular matrices are

$$
\mathsf{M}_4(\tilde\Pi_1)=\tfrac12\begin{pmatrix}1&0&0&-i\\0&1&-i&0\\0&i&1&0\\i&0&0&1\end{pmatrix},\qquad
\mathsf{M}_4(\tilde\Pi_2)=\tfrac12\begin{pmatrix}1&0&0&i\\0&1&i&0\\0&-i&1&0\\-i&0&0&1\end{pmatrix},
$$

$$
\mathsf{M}_4(\hat\Upsilon_1)=\tfrac12\begin{pmatrix}0&-i&1&0\\i&0&0&-1\\-1&0&0&-i\\0&1&i&0\end{pmatrix},\qquad
\mathsf{M}_4(\hat\Upsilon_2)=\tfrac12\begin{pmatrix}0&-i&-1&0\\i&0&0&1\\1&0&0&-i\\0&-1&i&0\end{pmatrix}.
$$

The two idempotents are orthogonal projectors, $\mathsf{M}_4(\tilde\Pi_1)\mathsf{M}_4(\tilde\Pi_2)=0$ and $\mathsf{M}_4(\tilde\Pi_1)+\mathsf{M}_4(\tilde\Pi_2)=I_4$, each of trace $2$ and rank $2$; the two nilpotents are square-zero, $\mathsf{M}_4(\hat\Upsilon_1)^2=\mathsf{M}_4(\hat\Upsilon_2)^2=0$, with

$$
\mathsf{M}_4(\hat\Upsilon_1)\mathsf{M}_4(\hat\Upsilon_2)=\mathsf{M}_4(\tilde\Pi_1),\qquad \mathsf{M}_4(\hat\Upsilon_2)\mathsf{M}_4(\hat\Upsilon_1)=\mathsf{M}_4(\tilde\Pi_2).
$$

The four therefore form a system of $2\times2$ matrix units inside $M_4(\mathbb{C})$, of diagonal rank $2$ where the units of $M_2(\mathbb{C})$ have rank $1$, and the Peirce decomposition of the algebra is the decomposition of the four-dimensional image $\mathsf{M}_4(\mathbb{B})$ into the four complex lines

$$
\mathsf{M}_4(\mathbb{B}) = \mathbb{C}\mathsf{M}_4(\tilde\Pi_1)\oplus\mathbb{C}\mathsf{M}_4(\hat\Upsilon_1)\oplus\mathbb{C}\mathsf{M}_4(\hat\Upsilon_2)\oplus\mathbb{C}\mathsf{M}_4(\tilde\Pi_2).
$$

An element has the same Peirce coordinates in this model as in the $2\times2$ model, because they are its coordinates in the same four-element basis of the algebra:

$$
\mathsf{M}_4(\tilde Q)=a_{11}\mathsf{M}_4(\tilde\Pi_1)+a_{12}\mathsf{M}_4(\hat\Upsilon_1)+a_{21}\mathsf{M}_4(\hat\Upsilon_2)+a_{22}\mathsf{M}_4(\tilde\Pi_2),
$$

with $a_{11}=Q_0-iQ_3$, $a_{12}=-iQ_1-Q_2$, $a_{21}=-iQ_1+Q_2$, $a_{22}=Q_0+iQ_3$ (*Ideals and Peirce Decomposition of the General Plain Algebra*, §*The Peirce Coordinates*). A corner of the Peirce decomposition is the two-sided compression of the regular matrix by the corresponding projectors,

$$
\mathsf{M}_4(\tilde\Pi_i\mathbb{B}\tilde\Pi_j)=\mathsf{M}_4(\tilde\Pi_i)\,\mathsf{M}_4(\mathbb{B})\,\mathsf{M}_4(\tilde\Pi_j),
$$

and it is the line spanned by the corresponding regular matrix; for instance the $(1,2)$ corner is $\mathsf{M}_4(\tilde\Pi_1\tilde Q\tilde\Pi_2)=a_{12}\mathsf{M}_4(\hat\Upsilon_1)$.

**The two models compared.** In the $2\times2$ model the four Peirce matrices are the four matrix units, a basis of the whole of $M_2(\mathbb{C})$, because the realization is a bijection. In the regular model they are four matrices of $M_4(\mathbb{C})$ spanning only the four-dimensional image $\mathsf{M}_4(\mathbb{B})$, a subspace of the sixteen-dimensional $M_4(\mathbb{C})$; they are the images of the same four elements of the algebra, so the two readings differ in the carrier and not in the coordinates. The two rank-two projectors are the left multiplications by $\tilde\Pi_1$ and $\tilde\Pi_2$, with images the two minimal left ideals $\mathbb{B}\tilde\Pi_1$ and $\mathbb{B}\tilde\Pi_2$ of the splitting $\mathbb{B}=I_1\oplus I_2$ of *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*.

## Summary

The left regular representation turns the plain product of the algebra into the product of the regular matrices, $\mathsf{M}_4(\tilde{P})\mathsf{M}_4(\tilde{Q})=\mathsf{M}_4(\tilde{P}\tilde{Q})$, and carries the two commuting copies $\mathsf{M}_4(\mathbb{B})$ and $\mathsf{M}_4^{R}(\mathbb{B})$ of the algebra, related by the transposition identities $\mathsf{M}_4^{R}(\tilde{Q})=E\mathsf{M}_4(\tilde{Q})^{\mathsf{T}}E$ and $\mathsf{M}_4(\tilde{Q}^{\natural})=\mathsf{M}_4(\tilde{Q})^{\mathsf{T}}$. The general plain bilinear form of the group is the plain trace pairing $\tfrac12\operatorname{Tr}(\mathsf{M}_4(\tilde{P})\mathsf{M}_4(\tilde{Q}))=2\langle\tilde{P},\tilde{Q}\rangle$, with the coefficient Gram matrix $E$, of real signature $(4,4)$, with the isotropic cone $\sum_\mu\varepsilon_\mu Q_\mu^2=0$ of real dimension $6$ as null set, and with automorphism group $O_4(\mathbb{C})$ on the coefficients and $O(4,4)$ on the realification. The invariants of the regular matrix are the trace $4Q_0$ and the determinant $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}^2$, the square of the determinant of the element because the regular module is the direct sum of two copies of the simple module. The Peirce spaces are the four complex lines spanned by the regular matrices of $\tilde\Pi_1,\hat\Upsilon_1,\hat\Upsilon_2,\tilde\Pi_2$: the two idempotents give orthogonal rank-two projectors and the two nilpotents square-zero matrices, and the four together are a system of $2\times2$ matrix units inside $M_4(\mathbb{C})$ whose coordinates are the Peirce coordinates.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_4(\tilde{Q})$ | the $4\times4$ regular matrix of left multiplication, $\operatorname{Tr}\mathsf{M}_4(\tilde{Q})=4Q_0$ |
| $\mathsf{M}_4^{R}(\tilde{Q})=E\mathsf{M}_4(\tilde{Q})^{\mathsf{T}}E$ | the right regular matrix, the transpose of the left one conjugated by the sign matrix $E$ |
| $\mathsf{M}_4(\tilde{P})\mathsf{M}_4(\tilde{Q})=\mathsf{M}_4(\tilde{P}\tilde{Q})$ | the plain product is the product of the regular matrices |
| $\tfrac12\operatorname{Tr}(\mathsf{M}_4(\tilde{P})\mathsf{M}_4(\tilde{Q}))=2\langle\tilde{P},\tilde{Q}\rangle$ | the general plain bilinear form as the trace pairing of the regular matrices |
| $\det\mathsf{M}_4(\tilde{Q})=\langle\tilde{Q},\tilde{Q}\rangle_{\natural}^2$ | the determinant of the regular matrix |
| $O_4(\mathbb{C})$, $O(4,4)$ | the automorphism group and its realification |
| $\mathsf{M}_4(\tilde\Pi_i)$, $\mathsf{M}_4(\hat\Upsilon_k)$ | the regular matrices of the Peirce basis: orthogonal rank-two projectors and square-zero nilpotents, a system of $2\times2$ matrix units with diagonal rank $2$ |

## Further Reading

- *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_maths/introduction-to-the-4x4-matrix-element-representation-of-biquaternions.md`), for the representation and its first properties
- *The 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_maths/the-4x4-matrix-element-representation-of-biquaternions.md`), for the further reading of the regular representation
- *The General Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-general-plain-algebra-in-the-2x2-matrix-element-representation.md`), for the companion reading of the group
- *Remarkable Subspaces under the General Plain Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-plain-algebra-of-biquaternions.md`), for the restriction theory of the form
- *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternion-c-space.md`), for the four forms read side by side
- *Ideals and Peirce Decomposition of the General Plain Algebra* (`articles_maths/ideals-and-peirce-decomposition-of-the-general-plain-algebra.md`), for the Peirce decomposition read here on the matrices
