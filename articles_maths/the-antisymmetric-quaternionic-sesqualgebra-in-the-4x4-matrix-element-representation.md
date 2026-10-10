# __The Antisymmetric Quaternionic Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$__

## Introduction

The block $\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural})=\mathbf{P}\times\overline{\mathbf{Q}}$ of *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions* is read here in the $4\times4$ left regular representation of *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*, in which the natural conjugation is the **transpose** and the Hermitian conjugation is the **conjugate transpose**. In the model the block is the **half-difference of the two twisted matrix products**: the product with the matrix of one conjugation in the first slot and the conjugate transpose in the second, minus the same product with the two orders exchanged. The value is traceless because the block is pure vector, and the pairing is the trace form of the regular matrix. This article is the second of the two representation articles of the block, and its companion *The Antisymmetric Quaternionic Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* reads the same half-difference on the realization, with the adjugate in the first slot; the two models differ only in the matrix of the natural conjugation.

The product the block splits is *The General Quaternionic Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$*; the form is *The Krein Gram Matrix and the Restrictions of the Form*; the general construction of a part is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*; the diagonal and the failure of the Jacobi identity are *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra*; and the operators are *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*. This article owns the reading of the block in the regular model.

**Conventions.** As in the block: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$, $e_k^2=-e_0$; a generic element $\tilde Q=Q_0e_0+\mathbf{Q}$; natural conjugation ${}^{\natural}$ and Hermitian conjugation ${}^{*}={}^{\natural}\circ\bar{\cdot}$; form $K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ with $\varepsilon=(1,-1,-1,-1)$, linear in the first argument and conjugate-linear in the second. In the model the realization $\mathsf{M}_4$ is the left multiplication $\tilde R\mapsto\tilde Q\tilde R$ of the plain product.

## The Model and Its Conjugations

**Definition.** The **left regular matrix** is the isomorphism written $\mathsf{M}_4$,
$$
\mathsf{M}_4:\mathbb{B}\longrightarrow M_4(\mathbb{C}),
$$
its $m$-th column being the coordinate column of the left multiplication $\tilde R\mapsto\tilde Q\tilde R$ of the plain product in the basis $e_0,e_1,e_2,e_3$; it is fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity, and it satisfies $\mathsf{M}_4(\tilde Q^{\natural})=\mathsf{M}_4(\tilde Q)^{\mathsf T}$, $\mathsf{M}_4(\tilde Q^{*})=\mathsf{M}_4(\tilde Q)^{\dagger}$, and $\operatorname{Tr}\mathsf{M}_4(\tilde Q)=4Q_0$.

*Proof.* The regular representation of an associative algebra is multiplicative, and the two conjugations are the transpose and the conjugate transpose of the matrix, as in *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*. Verified on the generators. $\square$

## The Matrix Form of the Block

**Theorem.** For all biquaternions,

$$
\mathsf{M}_4\bigl(\tilde P\diamond\tilde Q\bigr)
=\tfrac12\Bigl(\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)^{\dagger}
-\mathsf{M}_4(\tilde Q)^{\dagger}\mathsf{M}_4(\tilde P)^{\mathsf T}\Bigr),
$$

the half-difference of the two twisted regular products, with the transpose in the first slot and the conjugate transpose in the second.

*Proof.* The products $\tilde P^{\natural}\tilde Q^{*}$ and $\tilde Q^{*}\tilde P^{\natural}$ read $\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)^{\dagger}$ and $\mathsf{M}_4(\tilde Q)^{\dagger}\mathsf{M}_4(\tilde P)^{\mathsf T}$ in the model, and the block is their half-difference. Verified on general elements. $\square$

**Proposition (the value is traceless).** $\operatorname{Tr}\mathsf{M}_4(\tilde P\diamond\tilde Q)=0$ for all biquaternions, the block being pure vector.

*Proof.* The trace of the regular matrix is $4Q_0$, and the block has scalar coordinate zero. Verified on general elements. $\square$

**Proposition (the conjugate-linearity in the model).** The right-hand side is $\mathbb{C}$-linear in $\mathsf{M}_4(\tilde P)$ and conjugate-linear in $\mathsf{M}_4(\tilde Q)$:

$$
\mathsf{M}_4\bigl((A\tilde P)\diamond\tilde Q\bigr)=A\,\mathsf{M}_4(\tilde P\diamond\tilde Q),\qquad
\mathsf{M}_4\bigl(\tilde P\diamond(A\tilde Q)\bigr)=\overline{A}\,\mathsf{M}_4(\tilde P\diamond\tilde Q)\qquad(A\in\mathbb{C}).
$$

*Proof.* The transpose is linear and the conjugate transpose is conjugate-linear in the entries, so the first slot enters linearly and the second through the conjugate transpose, which carries the conjugate. Verified on general elements. $\square$

**Remark (the two models agree on the block).** The half-difference is the same expression in the two models, with the adjugate in the $2\times2$ model and the transpose in the regular model, both being the matrices of the natural conjugation; the conjugate transpose is the second operation in both. The two models therefore carry the same theorem, and the value is traceless in both because the block is pure vector. On the real basis the block is the ordinary cross product and the value is traceless; off the real basis the value is the conjugate cross product, and the model keeps the trace zero.

## The Pairing in the Regular Model

**Theorem (the trace form).** For all biquaternions, the form $K$ is read from the trace of the regular matrices,

$$
K(\tilde P,\tilde Q)=\tfrac14\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)^{\dagger}\bigr),
$$

and the pairing of the block is the same trace form read on the value,

$$
K\bigl(\tilde P\diamond\tilde Q,\tilde R\bigr)
=\tfrac14\operatorname{Tr}\bigl(\mathsf{M}_4(\tilde P\diamond\tilde Q)^{\mathsf T}\,\mathsf{M}_4(\tilde R)^{\dagger}\bigr)
=-\bigl(\mathbf{P}\times\overline{\mathbf{Q}},\overline{\mathbf{R}}\bigr).
$$

*Proof.* $\operatorname{Tr}\mathsf{M}_4(\tilde P)=4P_0$, so $\operatorname{Tr}(\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)^{\dagger})=\operatorname{Tr}\mathsf{M}_4(\tilde P^{\natural}\tilde Q^{*})=4K(\tilde P,\tilde Q)$, which is the form of *The Krein Gram Matrix and the Restrictions of the Form*; the block is pure vector, so the trace reads the vector part with the sign $-1$ and the conjugation on the third argument. The transpose on the first factor is the matrix of the natural conjugation, as for the form of the row. Verified on general elements. $\square$

## The Comparison with the Plain Row

**Remark (the two sesquilinear antisymmetric parts).** The two sesqualgebras carry the antisymmetric parts $\mathrm{APS}$ and $\mathrm{AQS}$, both sesquilinear, and their matrix forms are the half-differences of a product with one conjugation in each slot and the same product in the other order: for $\mathrm{APS}$ the first slot is unadorned and the second is the conjugate transpose, while for $\mathrm{AQS}$ the first slot carries the matrix of the natural conjugation — the **transpose** here — and the second the conjugate transpose. The block is therefore the $\mathrm{AQS}$ of the table, the half-difference with the transpose in the first slot, and this single distinction from $\mathrm{APS}$ is the whole difference between the two sesquilinear antisymmetric parts in the regular model.

**Remark (the model invariants of the block).** In the regular model the block is carried to the traceless matrices, and the pairing is the trace form of the regular matrix; the trace form $\operatorname{Tr}(\operatorname{adj}\mathsf{M}_2(\tilde P\diamond\tilde Q)\mathsf{M}_2(\tilde R)^{\dagger})$ of the $2\times2$ companion reads the same form $K$ on the value. The operator-side statement of the same facts is *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*.

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

**The half-difference, entry by entry.** At the witness $\tilde P=\tilde Q=e_1+ie_2$, whose regular matrix is

$$
\mathsf{M}_4(e_1+ie_2)=\begin{pmatrix}0&-1&-i&0\\1&0&0&i\\i&0&0&-1\\0&-i&1&0\end{pmatrix},
$$

the two twisted products are the two matrices

$$
\operatorname{adj}\mathsf{M}_4(\tilde P)\mathsf{M}_4(\tilde P)^{\dagger}=\begin{pmatrix}-2&0&0&2i\\0&-2&2i&0\\0&-2i&-2&0\\-2i&0&0&-2\end{pmatrix},
\qquad
\mathsf{M}_4(\tilde P)^{\dagger}\operatorname{adj}\mathsf{M}_4(\tilde P)=\begin{pmatrix}-2&0&0&-2i\\0&-2&-2i&0\\0&2i&-2&0\\2i&0&0&-2\end{pmatrix},
$$

differing in the signs of the off-diagonal entries, and the half-difference is the regular matrix

$$
\mathsf{M}_4(\tilde P\diamond\tilde P)=\begin{pmatrix}0&0&0&2i\\0&0&2i&0\\0&-2i&0&0\\-2i&0&0&0\end{pmatrix}=\mathsf{M}_4(-2ie_3),
$$

**which is the same element $-2ie_3$ the realization reaches as $\operatorname{diag}(-2,2)$**: the two models carry the same value, traceless in both because the block is pure vector.

## Summary

In the $4\times4$ regular representation the block is the half-difference of the two twisted matrix products, $\mathsf{M}_4(\tilde P\diamond\tilde Q)=\tfrac12(\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)^{\dagger}-\mathsf{M}_4(\tilde Q)^{\dagger}\mathsf{M}_4(\tilde P)^{\mathsf T})$, with the transpose, the matrix of the natural conjugation, in the first slot and the conjugate transpose in the second. The value is traceless, because the block is pure vector, and the block is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second. The pairing of the block is the trace form of the regular model, reading the form $K$ on the value, $K(\tilde P\diamond\tilde Q,\tilde R)=-(\mathbf{P}\times\overline{\mathbf{Q}},\overline{\mathbf{R}})$. The comparison with the plain row isolates the block as the half-difference with the natural conjugation in the first slot, the difference of the two sesquilinear antisymmetric parts in the regular model.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_4(\tilde Q^{\natural})=\mathsf{M}_4(\tilde Q)^{\mathsf T}$, $\mathsf{M}_4(\tilde Q^{*})=\mathsf{M}_4(\tilde Q)^{\dagger}$ | the two conjugations in the regular model |
| $\mathsf{M}_4(\tilde P\diamond\tilde Q)=\tfrac12(\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)^{\dagger}-\mathsf{M}_4(\tilde Q)^{\dagger}\mathsf{M}_4(\tilde P)^{\mathsf T})$ | the block in the regular model |
| trace $0$ | the value is pure vector |
| $\tfrac14\operatorname{Tr}(\mathsf{M}_4(\tilde P)^{\mathsf T}\mathsf{M}_4(\tilde Q)^{\dagger})$ | the trace form of the pairing |

## Further Reading

- *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_maths/introduction-to-the-4x4-matrix-element-representation-of-biquaternions.md`), for the regular model and its conjugations.
- *The General Quaternionic Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/the-general-quaternionic-sesqualgebra-in-the-4x4-matrix-element-representation.md`), for the product the block splits in the model.
- *The Antisymmetric Quaternionic Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-antisymmetric-quaternionic-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the reading on the realization.
- *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the block.
- *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/the-conjugate-cross-product-and-the-jacobi-failure-of-the-antisymmetric-quaternionic-sesqualgebra.md`), for the diagonal and its cone.
- *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/the-adjoint-operators-of-the-antisymmetric-quaternionic-sesqualgebra.md`), for the operators of the block.
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the form $K$.
