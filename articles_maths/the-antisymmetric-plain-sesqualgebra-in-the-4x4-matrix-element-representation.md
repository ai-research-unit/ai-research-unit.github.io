# __The Antisymmetric Plain Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$__

## Introduction

The block computes the operation $\tilde P\diamond\tilde Q=\mathrm{Vect}(\tilde P\tilde Q^{*})$ in the $4\times4$ left regular model of *The General Plain Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*. The starting point is the product of the row: it is the matrix product with the **conjugate transpose** of the second factor, and the block is its **vector part**, so the operation is read by the trace. In the $4\times4$ model the vector part of an element is its **traceless part**, and the block is

$$
\mathsf{M}_4(\tilde P\diamond\tilde Q)=\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)^{\dagger}
-\tfrac14\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)^{\dagger}\bigr)\,I .
$$

This article is the second of the two representation articles of the block, and its companion *The Antisymmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* reads the same operation on the realization.

The difference between the two readings is the shape of the image. In the $4\times4$ model the image is the image of the vector subspace under the regular representation, of complex dimension three, and the rank of a value is four, two or zero according to the **isotropy** of the value for the complex bilinear norm form, not according to the vanishing of the value: the two ranks are computed, and the distinction between the two forms carried by the block is the point of the article — the positive definite form $H(\tilde P\diamond\tilde Q,\tilde P\diamond\tilde Q)$ vanishes only on the zero value, while the determinant of the matrix of the value, which is the complex bilinear form $\sum_\mu V_\mu^2$, vanishes on the whole isotropic cone.

The setting and the notation are those of *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions*; the regular model and its invariants are *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* and *The General Plain Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*; the form $H$, the norm $N$ and the zero divisors are *Biquaternion Norm and Invertibility*; the operator whose invariants appear here is *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra*; and the invariants of a linear map are *Linear Maps and Matrices*, §*Rank* and §*The Trace and the Determinant of a Matrix*. The purity list of the pass is respected: the matrix invariants are the rank, the trace and the determinant, and no word of distance, of limit or of continuity occurs.

## The Regular Model

**Recall (the left regular matrix).** The left regular matrix of *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* is $\mathsf{M}_4(\tilde Q)$, whose $m$-th column is the coordinate column of the product $\tilde Q e_m$ in the basis $e_0,e_1,e_2,e_3$; it is fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity, and it satisfies

$$
\mathsf{M}_4(\tilde Q^{*})=\mathsf{M}_4(\tilde Q)^{\dagger},\qquad
\operatorname{Tr}\mathsf{M}_4(\tilde Q)=4Q_0,\qquad
\det\mathsf{M}_4(\tilde Q)=N(\tilde Q)^{2}.
$$

**The vector part.** In the model the vector part of an element is read by the trace,

$$
\mathsf{M}_4\bigl(\mathrm{Vect}(\tilde X)\bigr)=\mathsf{M}_4(\tilde X)-\tfrac14\operatorname{Tr}\mathsf{M}_4(\tilde X)\,I ,
$$

the **traceless part** of the regular matrix.

*Proof.* $\mathsf{M}_4(e_0)=I$ and $\operatorname{Tr}\mathsf{M}_4(\tilde X)=4X_0$, so subtracting $\tfrac14\operatorname{Tr}\mathsf{M}_4(\tilde X)I=X_0I$ leaves $\mathsf{M}_4(\tilde X-X_0e_0)=\mathsf{M}_4(\mathrm{Vect}\tilde X)$. $\square$

## The Block in the Regular Model

**Theorem (the block in the regular model).** For all biquaternions,

$$
\mathsf{M}_4(\tilde P\diamond\tilde Q)=\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)^{\dagger}
-\tfrac14\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)^{\dagger}\bigr)\,I,
$$

the **traceless part** of the conjugate-transposed product of the regular matrices; in particular $\operatorname{Tr}\mathsf{M}_4(\tilde P\diamond\tilde Q)=0$.

*Proof.* $\mathsf{M}_4(\tilde P\tilde Q^{*})=\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)^{\dagger}$ by the $*$-representation property, and the vector part is the traceless part. Verified on random pairs. $\square$

**Theorem (the invariants in the regular model).** For every value $\tilde V$ of the block,

$$
\operatorname{Tr}\mathsf{M}_4(\tilde V)=0,
\qquad
\det\mathsf{M}_4(\tilde V)=N(\tilde V)^{2},
\qquad
\operatorname{rank}\mathsf{M}_4(\tilde V)=
\begin{cases}
4, & N(\tilde V)\neq0,\\
2, & N(\tilde V)=0,\ \tilde V\neq0,\\
0, & \tilde V=0.
\end{cases}
$$

*Proof.* The trace vanishes because $\operatorname{Tr}\mathsf{M}_4(\tilde X)=4\mathrm{Sc}(\tilde X)$ and the value is a pure vector; the determinant is $N(\tilde X)^2$ for every $\tilde X$, by the invariants of the model. For the rank, $\det\mathsf{M}_4(\tilde V)=N(\tilde V)^2$, so the regular matrix is invertible exactly when $N(\tilde V)\neq0$; for $N(\tilde V)=0$ and $\tilde V\neq0$ the left regular representation of a central simple algebra has rank a multiple of the degree two, and the value is a zero divisor, so the rank is two. Verified on the model. $\square$

**Remark (the image and the rank in the regular model).** The image of the block in the regular model is the image of the vector subspace under $\mathsf{M}_4$, of complex dimension three: the value $\tilde V=e_0\diamond\tilde R=\mathbf R$ has regular matrix $\mathsf{M}_4(\mathbf R)$ of rank four whenever $N(\mathbf R)\neq0$, so the image meets the invertible matrices, while a zero divisor $\mathbf R$ has rank two. The $2\times2$ model reads the same image by the traceless matrices, again of complex dimension three, and the two models have the same rank pattern on the values through the factor two, $\operatorname{rank}\mathsf{M}_4=2\operatorname{rank}\mathsf{M}_2$ on the values, which is the ratio of the sizes of the two matrix algebras.

**Remark (the two-sided antisymmetrised operator).** The regular model also carries the **two-sided** antisymmetrisation

$$
\tfrac12\bigl(\mathsf{M}_4(\tilde P)\mathsf{M}_4^{R}(\tilde Q^{*})-\mathsf{M}_4(\tilde Q)\mathsf{M}_4^{R}(\tilde P^{*})\bigr),
$$

the matrix of the map $\tilde X\mapsto\tfrac12\bigl(\tilde P\tilde X\tilde Q^{*}-\tilde Q\tilde X\tilde P^{*}\bigr)$ on the module, with $\mathsf{M}_4^{R}(\tilde X)$ the right multiplication by $\tilde X$. It is alternating in its two parameters, so it vanishes identically at $\tilde P=\tilde Q$; its trace is $4i\,\mathrm{Im}\bigl(P_0\overline{Q_0}\bigr)$, not zero, and its rank is four for generic parameters, two on the real basis pairs such as $(e_0,e_1)$, and one on special complex pairs such as $(e_0+ie_1,\,ie_0-e_1)$, where the trace is $-4i$. It is not the block's element in the model, which is the traceless part of the one-sided product and has trace zero; and its vanishing diagonal is the opposite of the block's, whose diagonal is the vector part of the square. The distinction is the one of the symmetric row: the block's element is the matrix of the value, and the two-sided operator is the action of the two factors on the module, one-sided in the first case and two-sided in the second.

## The Matrix Form of the Pairing

**Theorem (the Hilbert–Schmidt pairing).** In the model the form $H$ is the Hilbert–Schmidt pairing of the matrices,

$$
H(\tilde P,\tilde Q)=\tfrac14\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)^{\dagger}\bigr).
$$

*Proof.* $\operatorname{Tr}\mathsf{M}_4(\tilde X)=4X_0$; hence $\operatorname{Tr}(\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)^{\dagger})=\operatorname{Tr}\mathsf{M}_4(\tilde P\tilde Q^{*})=4H(\tilde P,\tilde Q)$. Verified on random pairs. $\square$

**Corollary (the pairing of the block).** For the block,

$$
H\bigl(\tilde P\diamond\tilde Q,\tilde R\bigr)
=\tfrac14\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde P\diamond\tilde Q)\,\mathsf{M}_4(\tilde R)^{\dagger}\bigr),
$$

with $\mathsf{M}_4(\tilde P\diamond\tilde Q)$ the traceless part displayed above; the pairing is computed on the values, and it agrees with the coordinate formula of *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*, §*The Pairing with the Form*.

**Theorem (the invariant form in the model).** The unique invariant form of the block, up to a scalar, is the **scalar-slot form**

$$
\beta(\tilde X,\tilde Y)=X_0\overline{Y_0}=\tfrac1{16}\operatorname{Tr}\mathsf{M}_4(\tilde X)\;\overline{\operatorname{Tr}\mathsf{M}_4(\tilde Y)},
$$

and the invariance $\beta(\tilde P\diamond\tilde Q,\tilde R)=-\overline{\beta(\tilde P,\tilde Q\diamond\tilde R)}$ holds **degenerately**, both members vanishing with the trace of the value; no invariant form is non-degenerate.

*Proof.* $\operatorname{Tr}\mathsf{M}_4(\tilde X)=4X_0$, so $\tfrac1{16}\operatorname{Tr}\mathsf{M}_4(\tilde X)\overline{\operatorname{Tr}\mathsf{M}_4(\tilde Y)}=X_0\overline{Y_0}$, which is the invariant form of *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*, §*The Invariance Forms*; the degeneracy is the vanishing of the trace of a block value. $\square$

**Remark (the invariants of the operator in the model).** The operator $L^{\diamond}_{\tilde A}$ of *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra* acts on the model by $\mathsf{M}_4(\tilde X)\mapsto\mathsf{M}_4(\tilde A)\mathsf{M}_4(\tilde X)^{\dagger}-\tfrac14\operatorname{Tr}(\cdot)I$, a map of the traceless part of the conjugate-transposed product; its invariants are those computed there, trace zero and characteristic polynomial $\lambda^{2}(\lambda^{2}-1)^{3}$ at $\tilde A=e_0$ and $\lambda^{4}(\lambda^{2}+1)^{2}$ at $\tilde A=e_k$, and they are unchanged by the model, the regular representation being a $*$-representation through the conjugate transpose.

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

The general element has trace $4Q_0$ and determinant $N(\tilde Q)^2$.

**The block, entry by entry.** The block is the traceless part of the conjugate-transposed product of the regular matrices,

$$
\mathsf{M}_4(\tilde P\diamond\tilde Q)=M-\tfrac14\operatorname{Tr}(M)I_4=\tfrac12\bigl(M-M^{\mathsf T}\bigr),\qquad M=\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)^{\dagger},
$$

the transposition, which is the natural conjugation in the regular model, playing the part the adjugate plays in the realization; the trace term is the halved trace of the regular model, because $\operatorname{Tr}\mathsf{M}_4(\tilde X)=4X_0$ where $\operatorname{Tr}\mathsf{M}_2(\tilde X)=2X_0$.

**The witness, entry by entry.** At the pair $e_0,e_1$ the conjugate-transposed product is $M=\mathsf{M}_4(e_1)^{\dagger}=-\mathsf{M}_4(e_1)$ and its transpose is $M^{\mathsf T}=\mathsf{M}_4(e_1)$, so the half-difference is the matrix itself,

$$
\mathsf{M}_4(e_0\diamond e_1)=\tfrac12\bigl(-\mathsf{M}_4(e_1)-\mathsf{M}_4(e_1)\bigr)=-\mathsf{M}_4(e_1)=\mathsf{M}_4(-e_1),
$$

which is $e_0\diamond e_1=-e_1$; the regular matrix is traceless, of rank four since $N(-e_1)=1\neq0$, in agreement with the rank pattern $\operatorname{rank}\mathsf{M}_4=2\operatorname{rank}\mathsf{M}_2$ on the values.

## Summary

In the $4\times4$ model the block is the traceless part of the conjugate-transposed product, $\mathsf{M}_4(\tilde P\diamond\tilde Q)=M-\tfrac14\operatorname{Tr}(M)I$ with $M=\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde Q)^{\dagger}$, with trace zero and determinant $N(\tilde V)^2$, and rank four, two or zero according as $N\neq0$, $N=0$ with $\tilde V\neq0$, or $\tilde V=0$; the image is the image of the vector subspace under the regular representation, of complex dimension three. The form is the Hilbert–Schmidt pairing, $\tfrac14\operatorname{Tr}$ in the regular model, and the unique invariant form is the scalar-slot form $X_0\overline{Y_0}=\tfrac1{16}\operatorname{Tr}\mathsf{M}_4(\tilde X)\overline{\operatorname{Tr}\mathsf{M}_4(\tilde Y)}$, degenerate on every value. The two-sided antisymmetrised operator $\tfrac12\bigl(\mathsf{M}_4(\tilde P)\mathsf{M}_4^{R}(\tilde Q^{*})-\mathsf{M}_4(\tilde Q)\mathsf{M}_4^{R}(\tilde P^{*})\bigr)$ is a different object: it is alternating, with trace $4i\,\mathrm{Im}(P_0\overline{Q_0})$ and generic rank four. The positive definite form $H$ vanishes only on the zero value, while the determinant vanishes on the whole isotropic cone, with $e_1+ie_2$ a nonzero value of rank two.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_4$ | the left regular representation, $\mathsf{M}_4(\tilde Q^{*})=\mathsf{M}_4(\tilde Q)^{\dagger}$, $\operatorname{Tr}\mathsf{M}_4(\tilde Q)=4Q_0$ |
| $\mathsf{M}_4(\tilde P\diamond\tilde Q)=M-\tfrac14\operatorname{Tr}(M)I$ | the block in the regular model, the traceless part |
| $N(\tilde X)=\sum_\mu X_\mu^2$ | the complex bilinear norm, the square root of the determinant |
| $\operatorname{Tr}=0$, rank $4/2/0$ | the invariants of the regular value |
| $H=\tfrac14\operatorname{Tr}\mathsf{M}_4(\cdot)\mathsf{M}_4(\cdot)^{\dagger}$ | the form as the Hilbert–Schmidt pairing |
| $X_0\overline{Y_0}=\tfrac1{16}\operatorname{Tr}\mathsf{M}_4(\cdot)\overline{\operatorname{Tr}\mathsf{M}_4(\cdot)}$ | the unique invariant form, degenerate |
| $\tfrac12\bigl(\mathsf{M}_4(\tilde P)\mathsf{M}_4^{R}(\tilde Q^{*})-\mathsf{M}_4(\tilde Q)\mathsf{M}_4^{R}(\tilde P^{*})\bigr)$ | the two-sided antisymmetrised operator, alternating, trace $4i\,\mathrm{Im}(P_0\overline{Q_0})$ |

## Further Reading

- *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-sesqualgebra-of-biquaternions.md`), for the operation and its two conjugations
- *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-sesquilinear-pairing-of-the-antisymmetric-plain-sesqualgebra.md`), for the pairing, the trace form and the invariant forms computed here in the model
- *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-adjoint-operators-and-the-sandwich-of-the-antisymmetric-plain-sesqualgebra.md`), for the operator whose invariants the model carries
- *The General Plain Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/the-general-plain-sesqualgebra-in-the-4x4-matrix-element-representation.md`), for the product of the row and the form in the model
- *The Antisymmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-antisymmetric-plain-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the reading on the realization
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the two forms, the norm, the zero divisors and the isotropic cone
- *Linear Maps and Matrices* (`articles_maths/linear-maps-and-matrices.md`), for the matrix of a linear map and its invariants
