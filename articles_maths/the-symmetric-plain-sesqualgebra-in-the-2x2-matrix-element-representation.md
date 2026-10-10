# __The Symmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$__

## Introduction

The symmetric plain sesqualgebra is the operation $\tilde P\star\tilde Q = \tfrac12\bigl(\tilde P\tilde Q^{*} + (\tilde P\tilde Q^{*})^{\natural}\bigr) = \mathrm{Sc}(\tilde P\tilde Q^{*})e_0 = H(\tilde P,\tilde Q)e_0$ (*Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*). This article reads the block in the $2\times2$ realization $\mathsf{M}_2$ of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*; it is the first of the two representation articles of the block, and its companion *The Symmetric Plain Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* repeats the reading on the left regular representation.

The result that organises the article is that the block is a **scalar matrix** in the model. The value of the product is $\mathsf{M}_2(\tilde P\star\tilde Q) = H(\tilde P,\tilde Q)\,I_2$, and the symmetrisation that produces it is the one that replaces the matrix product $\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}$ by the half-sum with its adjugate: for a $2\times2$ matrix the identity $M + \operatorname{adj}M = (\operatorname{Tr}M)I$ converts the symmetrisation into the **trace-halving** $\tfrac12\operatorname{Tr}(M)I$, and the trace identity $\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}\bigr) = H(\tilde P,\tilde Q)$ turns it into the Hermitian form.

**Boundaries.** The model, the realization $\mathsf{M}_2$, the Hilbert and Schmidt pairing and the tables of the model are *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*; they are cited here and not restated, and this article owns only the image of the block in the model. The form $H$ is *Biquaternion Norm and Invertibility* and *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra*; the multiplication operators as abstract operators are *The Multiplication Operators of the Symmetric Plain Sesqualgebra*. Nothing topological and nothing metric appears; positivity is stated as the positivity of the diagonal of $H$ and no norm of positive real values is named.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$; natural conjugation ${}^{\natural}$ negating $e_1,e_2,e_3$, coefficientwise conjugation $\overline{\cdot}$, Hermitian conjugation ${}^{*} = \overline{\cdot}\circ{}^{\natural}$. The realization is $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ with $\mathsf{M}_2(e_0) = I_2$, $\mathsf{M}_2(e_k) = -i\sigma_k$, so that $\mathsf{M}_2$ is multiplicative, $\mathsf{M}_2(\tilde Q^{\natural}) = \operatorname{adj}\mathsf{M}_2(\tilde Q)$, $\mathsf{M}_2(\tilde Q^{*}) = \mathsf{M}_2(\tilde Q)^{\dagger}$ and $\operatorname{Tr}\mathsf{M}_2(\tilde Q) = 2Q_0$ (*The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*). The block is $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$.

## The Block in the Model

**Theorem (the value is a scalar matrix).** For all $\tilde P,\tilde Q$,

$$
\mathsf{M}_2(\tilde P\star\tilde Q) = H(\tilde P,\tilde Q)\,I_2 ,
$$

a scalar multiple of the identity matrix; its trace is $2H(\tilde P,\tilde Q)$, its determinant $H(\tilde P,\tilde Q)^{2}$, and the rank of the matrix, as a linear map, is $2$ when $H\neq0$ and $0$ when $H = 0$. Read as an element of the block the value spans the one-dimensional centre.

*Proof.* $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ and $\mathsf{M}_2(e_0) = I_2$, so the value is $H I_2$; its trace is $2H$, its determinant $H^{2}$, and the rank of the nonzero scalar matrix $H I_2$ is the size, $2$, unless $H = 0$; as a central element the value spans the centre, of complex dimension one. Verified on the model. $\square$

**Theorem (the symmetrisation and the trace-halving).** Write $X = \mathsf{M}_2(\tilde P)$ and $Y = \mathsf{M}_2(\tilde Q)$, so that the general plain sesquilinear product has the matrix $XY^{\dagger}$. Then the block is the symmetrisation with the adjugate,

$$
\mathsf{M}_2(\tilde P\star\tilde Q) = \tfrac12\bigl(XY^{\dagger} + \operatorname{adj}(XY^{\dagger})\bigr) = \tfrac12\operatorname{Tr}(XY^{\dagger})\,I_2 ,
$$

and the trace identity $\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}\bigr) = H(\tilde P,\tilde Q)$ exhibits the operation as the scalar multiple of the identity read as the Hermitian form.

*Proof.* $\mathsf{M}_2(\tilde P\tilde Q^{*}) = XY^{\dagger}$ because $\mathsf{M}_2$ is multiplicative and $\mathsf{M}_2(\tilde Q^{*}) = \mathsf{M}_2(\tilde Q)^{\dagger}$; and $\mathsf{M}_2\bigl((\tilde P\tilde Q^{*})^{\natural}\bigr) = \operatorname{adj}\bigl(XY^{\dagger}\bigr)$ because $(\,\cdot\,)^{\natural}$ is carried to the adjugate. The identity $M + \operatorname{adj}M = (\operatorname{Tr}M)I$ for a $2\times2$ matrix $M$ gives the middle expression; and $\operatorname{Tr}(XY^{\dagger}) = \operatorname{Tr}\mathsf{M}_2(\tilde P\tilde Q^{*}) = 2\,\mathrm{Sc}(\tilde P\tilde Q^{*}) = 2H(\tilde P,\tilde Q)$, giving the last. Verified on random pairs. $\square$

**Remark (the two involutions in the model).** The realization carries the two involutions of the product to the two operations of the model: the Hermitian conjugation ${}^{*}$ to the conjugate transpose, $\mathsf{M}_2(\tilde Q^{*}) = \mathsf{M}_2(\tilde Q)^{\dagger}$, and the natural conjugation ${}^{\natural}$ to the adjugate, $\mathsf{M}_2(\tilde Q^{\natural}) = \operatorname{adj}\mathsf{M}_2(\tilde Q)$. The product $\tilde P\tilde Q^{*}$ is the matrix product with the conjugate transpose in the second slot, and its symmetrisation is the half-sum with the adjugate; the pairing of the two involutions is what makes the value central, since $M + \operatorname{adj}M$ is the scalar $(\operatorname{Tr}M)I$ while $M + M^{\dagger}$ is not.

**Proposition (the form and its positivity in the model).** For all $\tilde P,\tilde Q$,

$$
H(\tilde P,\tilde Q) = \tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}\bigr) , \qquad H(\tilde Q,\tilde Q) = \tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde Q)^{\dagger}\mathsf{M}_2(\tilde Q)\bigr) > 0 \ \ (\tilde Q\neq0) ,
$$

so the form is the Hilbert and Schmidt pairing of the matrices, positive definite, and its Gram matrix on the basis is the identity.

*Proof.* The trace identity above and the positivity of the Hilbert and Schmidt pairing, which is the sum $\sum_\mu\lvert Q_\mu\rvert^{2}$ (*The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*). Verified on the model. $\square$

## The Invariance of the Symmetric Part

**Theorem (the value is invariant under the adjoint operation).** For all $\tilde P,\tilde Q$,

$$
\mathsf{M}_2(\tilde P\star\tilde Q)^{\dagger} = \mathsf{M}_2(\tilde Q\star\tilde P),
$$

and the scalar matrix $\mathsf{M}_2(\tilde P\star\tilde Q) = HI_2$ is fixed by conjugation by every invertible matrix of the model; a scalar matrix has no preferred basis, and the symmetric part of the block is therefore invariant under the choice of coordinates in the model.

*Proof.* $\mathsf{M}_2(\tilde P\star\tilde Q)^{\dagger} = \overline{H}I_2 = \mathsf{M}_2(\tilde Q\star\tilde P)$ because $H(\tilde Q,\tilde P) = \overline{H(\tilde P,\tilde Q)}$; and $U(HI_2)U^{-1} = HI_2$ for every invertible $U$. Verified on the model. $\square$

**Remark (the value is central).** The scalar matrix is the image of the block in the model, so the block is a **central** element of the matrix algebra $M_2(\mathbb{C})$: its image lies in the centre, which is the scalars. The invariance of the symmetric part is the statement that the image is central, and it is the model form of the central image of the product.

## Worked Examples

**The basis in the model.** $\mathsf{M}_2(e_\mu\star e_\nu) = \delta_{\mu\nu}I_2$; the sixteen products of the basis are the scalar matrices $I_2$ on the diagonal of the table and $0$ off it.

**A Hermitian element.** For $\tilde Q = e_0 + ie_3$ one has $H(\tilde Q,\tilde Q) = 1 + 1 = 2$, so $\mathsf{M}_2(\tilde Q\star\tilde Q) = 2I_2$, of trace $4$ and determinant $4$, the determinant being $H^{2} = 4$ as required. Here $\mathsf{M}_2(\tilde Q) = \begin{pmatrix}2&0\\0&0\end{pmatrix}$, not a scalar, while its symmetrised square is the scalar $2I_2$.

**A non-real value.** For $\tilde P = e_0$, $\tilde Q = ie_0$, $H = -i$, so $\mathsf{M}_2(\tilde P\star\tilde Q) = -iI_2$, of trace $-2i$ and determinant $-1$; the matrix is scalar and non-real, and its conjugate transpose is $\mathsf{M}_2(\tilde Q\star\tilde P) = iI_2$.

## The Matrices

**The generators.** The realization is fixed on the basis by four matrices:

$$
\mathsf{M}_2(e_0)=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad
\mathsf{M}_2(e_1)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\qquad
\mathsf{M}_2(e_2)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
\mathsf{M}_2(e_3)=\begin{pmatrix}-i&0\\0&i\end{pmatrix}.
$$

with the general element of matrix $\mathsf{M}_2(\tilde Q)$ of trace $2Q_0$ and determinant $N(\tilde Q)$.

**The trace-halving, entry by entry.** The two involutions of the model are the conjugate transpose and the adjugate, and the value is the half-sum of the conjugate-transposed product with its adjugate; for a two-by-two matrix the identity $M+\operatorname{adj}M=(\operatorname{Tr}M)I_2$ halves the trace, so the value is the scalar matrix

$$
\mathsf{M}_2(\tilde P\star\tilde Q)=\tfrac12\bigl(XY^{\dagger}+\operatorname{adj}(XY^{\dagger})\bigr)
=\tfrac12\operatorname{Tr}(XY^{\dagger})\,I_2
=H(\tilde P,\tilde Q)\,I_2 .
$$

At the pair $e_1,e_1$ the conjugate-transposed product is the identity, $XY^{\dagger}=\mathsf{M}_2(e_1)\mathsf{M}_2(e_1)^{\dagger}=\begin{pmatrix}0&-i\\-i&0\end{pmatrix}\begin{pmatrix}0&i\\i&0\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}$, of trace two, so the value is $I_2=H(e_1,e_1)I_2$: the conjugate-transposed square of the anti-Hermitian unit $e_1$ is the identity, and the value of the block at that pair is the identity of the model.

## Summary

In the $2\times2$ realization the block is the scalar matrix $\mathsf{M}_2(\tilde P\star\tilde Q) = H(\tilde P,\tilde Q)I_2$, obtained as the symmetrisation $\tfrac12\bigl(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger} + \operatorname{adj}(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger})\bigr)$ of the general plain sesquilinear product with the adjugate — the half-sum being the trace-halving $\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}\bigr)I_2$ by the $2\times2$ identity $M + \operatorname{adj}M = (\operatorname{Tr}M)I$ — and identified with the Hermitian form through the trace identity $\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}\bigr) = H(\tilde P,\tilde Q)$. Its trace is $2H$, its determinant $H^{2}$ and its rank $2$ as a matrix ($1$ as a central coordinate); the Hermitian conjugation is the conjugate transpose and the natural conjugation is the adjugate, and the pairing of the two involutions is what makes the value central. The block is **central** in the matrix algebra, so its image is a scalar matrix, invariant under the change of coordinates; the form $H$ is the Hilbert and Schmidt pairing, with positive definite diagonal $\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde Q)^{\dagger}\mathsf{M}_2(\tilde Q)\bigr) = \sum_\mu\lvert Q_\mu\rvert^{2}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$, $\mathsf{M}_2(e_0)=I_2$, $\mathsf{M}_2(e_k)=-i\sigma_k$ | the $2\times2$ realization |
| $\mathsf{M}_2(\tilde Q^{\natural}) = \operatorname{adj}\mathsf{M}_2(\tilde Q)$, $\mathsf{M}_2(\tilde Q^{*}) = \mathsf{M}_2(\tilde Q)^{\dagger}$ | the two involutions in the model |
| $\mathsf{M}_2(\tilde P\star\tilde Q) = H(\tilde P,\tilde Q)I_2$ | the block in the model |
| $\tfrac12\bigl(XY^{\dagger} + \operatorname{adj}(XY^{\dagger})\bigr) = \tfrac12\operatorname{Tr}(XY^{\dagger})I_2$ | the symmetrisation is the trace-halving |
| $\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}\bigr) = H(\tilde P,\tilde Q)$ | the trace identity |
| $\mathsf{M}_2(\tilde P\star\tilde Q)^{\dagger}=\mathsf{M}_2(\tilde Q\star\tilde P)$ | the invariance of the symmetric part |
| $HI_2$ central | the value is a scalar matrix |

## Further Reading

- *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the product and its central image.
- *The Multiplication Operators of the Symmetric Plain Sesqualgebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-plain-sesqualgebra.md`), for the abstract operators of which the regular reading is the companion article's.
- *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-general-plain-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the realization $\mathsf{M}_2$, the Hilbert and Schmidt pairing and the model tables.
- *The Symmetric Plain Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/the-symmetric-plain-sesqualgebra-in-the-4x4-matrix-element-representation.md`), for the reading on the left regular representation.
- *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-element-representation-of-biquaternions.md`), for the realization and the two involutions in it.
- *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra* (`articles_maths/the-hermitian-form-as-a-product-on-the-symmetric-plain-sesqualgebra.md`), for the form $H$, its Gram matrix and its positivity.
