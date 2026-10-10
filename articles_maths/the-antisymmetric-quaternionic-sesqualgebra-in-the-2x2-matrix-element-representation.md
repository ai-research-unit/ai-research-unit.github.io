# __The Antisymmetric Quaternionic Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$__

## Introduction

The block $\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural})=\mathbf{P}\times\overline{\mathbf{Q}}$ of *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions* is read here in the $2\times2$ realization of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, in which the natural conjugation is the **adjugate** and the Hermitian conjugation is the **conjugate transpose**. In the model the block is the **half-difference of the two twisted matrix products**: the product with the matrix of one conjugation in the first slot and the conjugate transpose in the second, minus the same product with the two orders exchanged. The value is the matrix form of the conjugate cross product, of trace zero because the block is pure vector, and its square at the named witness is the diagonal matrix of the value $-2ie_3$. The pairing of the block with the form is the adjugated conjugate-transposed trace form. This article is the first of the two representation articles of the block, and its companion *The Antisymmetric Quaternionic Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* reads the same half-difference on the regular model, with the transpose in the first slot.

The product the block splits is *The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*; the form is *The Krein Gram Matrix and the Restrictions of the Form*; the general construction of a part is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*; the diagonal and the failure of the Jacobi identity are *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra*; and the operators are *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*. This article owns the reading of the block in the realization.

**Conventions.** As in the block: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$, $e_k^2=-e_0$; a generic element $\tilde Q=Q_0e_0+\mathbf{Q}$; natural conjugation ${}^{\natural}$ and Hermitian conjugation ${}^{*}={}^{\natural}\circ\bar{\cdot}$; form $K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ with $\varepsilon=(1,-1,-1,-1)$, linear in the first argument and conjugate-linear in the second. In the model the realization is $\mathsf{M}_2(e_0)=I$, $\mathsf{M}_2(e_k)=-i\sigma_k$.

## The Model and Its Conjugations

**Definition.** The **$2\times2$ realization** is the isomorphism written $\mathsf{M}_2$,
$$
\mathsf{M}_2:\mathbb{B}\longrightarrow M_2(\mathbb{C}),
$$
fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity: $\mathsf{M}_2(e_0)=I$ and $\mathsf{M}_2(e_k)=-i\sigma_k$, with $\mathsf{M}_2(\tilde Q^{\natural})=\operatorname{adj}\mathsf{M}_2(\tilde Q)$ and $\mathsf{M}_2(\tilde Q^{*})=\mathsf{M}_2(\tilde Q)^{\dagger}$, where $\operatorname{adj}$ is the adjugate and ${}^{\dagger}$ the conjugate transpose.

*Proof.* The model, its multiplicativity and the two conjugation identities are those of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*; they are used, not re-derived. Verified on the generators and on general elements. $\square$

## The Matrix Form of the Block

**Theorem (the block is the half-difference of the two twisted products).** For all biquaternions,

$$
\mathsf{M}_2\bigl(\tilde P\diamond\tilde Q\bigr)
=\tfrac12\Bigl(\operatorname{adj}\mathsf{M}_2(\tilde P)\,\mathsf{M}_2(\tilde Q)^{\dagger}
-\mathsf{M}_2(\tilde Q)^{\dagger}\operatorname{adj}\mathsf{M}_2(\tilde P)\Bigr),
$$

the half-difference of the matrix product with the adjugate in the first slot and the conjugate transpose in the second, and of the same product with the two factors in the other order.

*Proof.* The product $\tilde P^{\natural}\tilde Q^{*}$ reads $\operatorname{adj}\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}$ in the model, and the product $\tilde Q^{*}\tilde P^{\natural}$ reads $\mathsf{M}_2(\tilde Q)^{\dagger}\operatorname{adj}\mathsf{M}_2(\tilde P)$; the rule of the block is the half-difference of the two, and $\mathsf{M}_2$ is linear. Verified on general elements. $\square$

**Remark (the matrix of the natural conjugation).** The adjugation is the matrix of ${}^{\natural}$, and the conjugate transpose is the matrix of ${}^{*}$; the block is therefore written on a general pair with the **matrix of the natural conjugation** in the first slot and the **conjugate transpose** in the second, in the two orders. The two factors of the half-difference are the two readings of that pair, and their difference is the matrix form of the conjugate cross product.

**Proposition (the value is traceless).** For all biquaternions, $\operatorname{Tr}\mathsf{M}_2(\tilde P\diamond\tilde Q)=0$ and $\det\mathsf{M}_2(\tilde P\diamond\tilde Q)$ is the sum of the squares of the coordinates of the conjugate cross product.

*Proof.* The trace of the realization is $2Q_0$, and the block is pure vector, so $Q_0=0$ and the trace vanishes; the determinant of the realization is $\sum_\mu Q_\mu^{2}$, the value of the block, whose scalar coordinate is zero. Verified on general elements. $\square$

## The Diagonal in the Model

**Proposition (the witness).** At $\tilde P=\tilde Q=e_1+ie_2$,

$$
\mathsf{M}_2\bigl(\tilde P\diamond\tilde Q\bigr)=\mathsf{M}_2\bigl(-2ie_3\bigr)=\operatorname{diag}(-2,2)
=\begin{pmatrix}-2&0\\0&2\end{pmatrix},
$$

and $\mathsf{M}_2(e_1+ie_2)=\begin{pmatrix}0&-2i\\0&0\end{pmatrix}$.

*Proof.* Direct evaluation of the model on $e_1+ie_2$ and on the value $-2ie_3$. Verified on the witness. $\square$

**Remark (the diagonal is visible in the trace-zero matrices).** The block is pure vector, so its matrices are traceless; the diagonal element $\operatorname{diag}(-2,2)$ is the model form of $-2ie_3$, of determinant $-4$, the sum of the squares of the coordinates of the value. On the real basis the block is the ordinary cross product, and its matrices are the traceless matrices of the cross product; off the real basis the value is the conjugate cross product, and the model keeps the trace zero.

## The Conjugate-Linearity in the Model

**Proposition.** The right-hand side of the matrix form is $\mathbb{C}$-linear in $\mathsf{M}_2(\tilde P)$ and conjugate-linear in $\mathsf{M}_2(\tilde Q)$:

$$
\mathsf{M}_2\bigl((A\tilde P)\diamond\tilde Q\bigr)=A\,\mathsf{M}_2(\tilde P\diamond\tilde Q),\qquad
\mathsf{M}_2\bigl(\tilde P\diamond(A\tilde Q)\bigr)=\overline{A}\,\mathsf{M}_2(\tilde P\diamond\tilde Q)\qquad(A\in\mathbb{C}).
$$

*Proof.* The adjugate is linear and the conjugate transpose is conjugate-linear in the entries, so the first slot enters linearly and the second through the conjugate transpose, which carries the conjugate. Verified on general elements. $\square$

**Remark (the model expresses the class).** The class of the block is visible in the model as the split between the adjugate, which is linear, and the conjugate transpose, which is conjugate-linear; the half-difference of the two twisted products is again of that class, and this is the matrix form of the sesquilinearity of the block.

## The Pairing in the Model

**Theorem (the adjugated conjugate-transposed trace form).** For all biquaternions,

$$
K(\tilde P,\tilde Q)=\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\mathsf{M}_2(\tilde P)\,\mathsf{M}_2(\tilde Q)^{\dagger}\bigr),
$$

the pairing in which the conjugate transpose of the second argument is adjugated in the first, and the pairing of the block is the same trace form read on the value,

$$
K\bigl(\tilde P\diamond\tilde Q,\tilde R\bigr)
=\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\mathsf{M}_2(\tilde P\diamond\tilde Q)\,\mathsf{M}_2(\tilde R)^{\dagger}\bigr)
=-\bigl(\mathbf{P}\times\overline{\mathbf{Q}},\overline{\mathbf{R}}\bigr).
$$

*Proof.* The trace form of the model is the Krein form, by *The Krein Gram Matrix and the Restrictions of the Form* and *The Symmetric Quaternionic Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, $\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}\bigr)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$; the block is pure vector, so the trace reads the vector part with the sign $-1$ and the conjugation on the third argument. Verified on general elements. $\square$

## The Comparison with the Plain Row

**Remark (the two sesquilinear antisymmetric parts).** The two sesqualgebras carry the antisymmetric parts $\mathrm{APS}$ and $\mathrm{AQS}$, both sesquilinear, and their matrix forms are the half-differences of a product with one conjugation in each slot and the same product in the other order: for $\mathrm{APS}$ the first slot is unadorned and the second is the conjugate transpose, while for $\mathrm{AQS}$ the first slot carries the matrix of the natural conjugation — the **adjugate** here — and the second the conjugate transpose. The block is therefore the $\mathrm{AQS}$ of the table, the half-difference with the adjugate in the first slot, and this single distinction from $\mathrm{APS}$ is the whole difference between the two sesquilinear antisymmetric parts in the model.

## The Matrices

**The generators.** The realization is fixed on the basis by four matrices:

$$
\mathsf{M}_2(e_0)=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad
\mathsf{M}_2(e_1)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\qquad
\mathsf{M}_2(e_2)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
\mathsf{M}_2(e_3)=\begin{pmatrix}-i&0\\0&i\end{pmatrix}.
$$

with the natural conjugation carried to the adjugate and the Hermitian conjugation to the conjugate transpose.

**The half-difference, entry by entry.** At the witness $\tilde P=\tilde Q=e_1+ie_2$, of matrix $\mathsf{M}_2(\tilde P)=\begin{pmatrix}0&-2i\\0&0\end{pmatrix}$, the two twisted products are the two nilpotent halves of $-4I$,

$$
\operatorname{adj}\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde P)^{\dagger}=\begin{pmatrix}-4&0\\0&0\end{pmatrix},
\qquad
\mathsf{M}_2(\tilde P)^{\dagger}\operatorname{adj}\mathsf{M}_2(\tilde P)=\begin{pmatrix}0&0\\0&-4\end{pmatrix},
$$

and the half-difference is the diagonal matrix of the value,

$$
\mathsf{M}_2(\tilde P\diamond\tilde P)=\tfrac12\begin{pmatrix}-4&0\\0&4\end{pmatrix}=\begin{pmatrix}-2&0\\0&2\end{pmatrix}=\operatorname{diag}(-2,2)=\mathsf{M}_2(-2ie_3),
$$

traceless of determinant $-4$; **the two products differ only in which diagonal entry carries the $-4$**, and the antisymmetrisation moves it to the difference of the two.

## Summary

In the $2\times2$ realization the block is the half-difference of the two twisted matrix products, $\mathsf{M}_2(\tilde P\diamond\tilde Q)=\tfrac12(\operatorname{adj}\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}-\mathsf{M}_2(\tilde Q)^{\dagger}\operatorname{adj}\mathsf{M}_2(\tilde P))$, with the matrix of the natural conjugation, the adjugate, in the first slot and the conjugate transpose in the second. The value is traceless, because the block is pure vector, and at the witness $e_1+ie_2$ the value $-2ie_3$ has matrix $\operatorname{diag}(-2,2)$, of determinant $-4$. The block is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second, the model split being the one between the adjugate and the conjugate transpose. The pairing of the block is the adjugated conjugate-transposed trace form, reading the form $K$ on the value. The comparison with the plain row isolates the block as the half-difference with the natural conjugation in the first slot, the difference of the two sesquilinear antisymmetric parts in the model.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2(e_0)=I$, $\mathsf{M}_2(e_k)=-i\sigma_k$ | the $2\times2$ realization |
| $\mathsf{M}_2(\tilde Q^{\natural})=\operatorname{adj}\mathsf{M}_2(\tilde Q)$, $\mathsf{M}_2(\tilde Q^{*})=\mathsf{M}_2(\tilde Q)^{\dagger}$ | the two conjugations in the model |
| $\mathsf{M}_2(\tilde P\diamond\tilde Q)=\tfrac12(\operatorname{adj}\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}-\mathsf{M}_2(\tilde Q)^{\dagger}\operatorname{adj}\mathsf{M}_2(\tilde P))$ | the block in the model |
| $\operatorname{diag}(-2,2)$ | the value $-2ie_3$ at $e_1+ie_2$ |
| trace $0$ | the value is pure vector |
| $\tfrac12\operatorname{Tr}(\operatorname{adj}\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger})$ | the trace form of the pairing |

## Further Reading

- *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-element-representation-of-biquaternions.md`), for the model, its multiplicativity and the two conjugations.
- *The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-general-quaternionic-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the product the block splits in the model.
- *The Antisymmetric Quaternionic Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/the-antisymmetric-quaternionic-sesqualgebra-in-the-4x4-matrix-element-representation.md`), for the reading on the regular model.
- *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the block.
- *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/the-conjugate-cross-product-and-the-jacobi-failure-of-the-antisymmetric-quaternionic-sesqualgebra.md`), for the diagonal and its cone.
- *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra* (`articles_maths/the-adjoint-operators-of-the-antisymmetric-quaternionic-sesqualgebra.md`), for the operators of the block.
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the form $K$.
