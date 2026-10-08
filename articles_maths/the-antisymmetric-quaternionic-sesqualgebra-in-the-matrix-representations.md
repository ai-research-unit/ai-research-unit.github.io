# __The Antisymmetric Quaternionic Sesqualgebra in the Matrix Representations__

## Introduction

The block $\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}-\tilde Q^{*}\tilde P^{\natural})=\mathbf{P}\times\overline{\mathbf{Q}}$ of *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions* is read here in the two matrix models of the algebra: the $2\times2$ realization of *Introduction to the 2×2 Matrix Representation of Biquaternions*, in which the natural conjugation is the **adjugate** and the Hermitian conjugation is the **conjugate transpose**, and the $4\times4$ left regular representation of *Introduction to the 4×4 Regular Matrix Representation of Biquaternions*, in which the natural conjugation is the **transpose** and the Hermitian conjugation is again the **conjugate transpose**. In both models the block is the **half-difference of the two twisted matrix products**: the product with the matrix of one conjugation in the first slot and the conjugate transpose in the second, minus the same product with the two orders exchanged. The value is the matrix form of the conjugate cross product, of trace zero because the block is pure vector, and its square at the named witness is the diagonal matrix of the value $-2ie_3$. The pairing of the block with the form is the adjugated conjugate-transposed trace form in the $2\times2$ model, and the same trace form in the regular model. The reading is parallel to the model articles of the two general sesqualgebras and of the two blocks of the plain row, and it is the representation side of the multiplication.

The product the block splits is *The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Representation* and its regular companion; the form is *The Krein Gram Matrix and the Restrictions of the Form*; the general construction of a part is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*; the diagonal and the failure of the Jacobi identity are *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra*; and the operators are *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*. This article owns the reading of the block in the two matrix models.

**Conventions.** As in the block: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$, $e_k^2=-e_0$; a generic element $\tilde Q=Q_0e_0+\mathbf{Q}$; natural conjugation ${}^{\natural}$ and Hermitian conjugation ${}^{*}={}^{\natural}\circ\bar{\cdot}$; form $K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ with $\varepsilon=(1,-1,-1,-1)$, linear in the first argument and conjugate-linear in the second. In the $2\times2$ model the realization is $\Phi(e_0)=I$, $\Phi(e_k)=-i\sigma_k$; in the $4\times4$ model the realization $\rho_L$ is the left multiplication $\tilde R\mapsto\tilde Q\tilde R$ of the plain product.

## The Two-by-Two Model

### The Model and Its Conjugations

**Definition.** The **$2\times2$ realization** is the $\mathbb{C}$-linear isomorphism

$$
\Phi:\mathbb{B}\longrightarrow M_2(\mathbb{C}),\qquad
\Phi(e_0)=I,\qquad\Phi(e_k)=-i\sigma_k,
$$

with $\Phi(\tilde Q^{\natural})=\operatorname{adj}\Phi(\tilde Q)$ and $\Phi(\tilde Q^{*})=\Phi(\tilde Q)^{\dagger}$, where $\operatorname{adj}$ is the adjugate and ${}^{\dagger}$ the conjugate transpose.

*Proof.* The model, its multiplicativity and the two conjugation identities are those of *Introduction to the 2×2 Matrix Representation of Biquaternions*; they are used, not re-derived. Verified on the generators and on general elements.

### The Matrix Form of the Block

**Theorem (the block is the half-difference of the two twisted products).** For all biquaternions,

$$
\Phi\bigl(\tilde P\diamond\tilde Q\bigr)
=\tfrac12\Bigl(\operatorname{adj}\Phi(\tilde P)\,\Phi(\tilde Q)^{\dagger}
-\Phi(\tilde Q)^{\dagger}\operatorname{adj}\Phi(\tilde P)\Bigr),
$$

the half-difference of the matrix product with the adjugate in the first slot and the conjugate transpose in the second, and of the same product with the two factors in the other order.

*Proof.* The product $\tilde P^{\natural}\tilde Q^{*}$ reads $\operatorname{adj}\Phi(\tilde P)\Phi(\tilde Q)^{\dagger}$ in the model, and the product $\tilde Q^{*}\tilde P^{\natural}$ reads $\Phi(\tilde Q)^{\dagger}\operatorname{adj}\Phi(\tilde P)$; the rule of the block is the half-difference of the two, and $\Phi$ is linear. Verified on general elements.

**Remark (the matrix of the natural conjugation).** The adjugation is the matrix of ${}^{\natural}$, and the conjugate transpose is the matrix of ${}^{*}$; the block is therefore written on a general pair with the **matrix of the natural conjugation** in the first slot and the **conjugate transpose** in the second, in the two orders. The two factors of the half-difference are the two readings of that pair, and their difference is the matrix form of the conjugate cross product.

**Proposition (the value is traceless).** For all biquaternions, $\operatorname{Tr}\Phi(\tilde P\diamond\tilde Q)=0$ and $\det\Phi(\tilde P\diamond\tilde Q)$ is the sum of the squares of the coordinates of the conjugate cross product.

*Proof.* The trace of the realization is $2Q_0$, and the block is pure vector, so $Q_0=0$ and the trace vanishes; the determinant of the realization is $\sum_\mu Q_\mu^{2}$, the value of the block, whose scalar coordinate is zero. Verified on general elements.

### The Diagonal in the Model

**Proposition (the witness).** At $\tilde P=\tilde Q=e_1+ie_2$,

$$
\Phi\bigl(\tilde P\diamond\tilde Q\bigr)=\Phi\bigl(-2ie_3\bigr)=\operatorname{diag}(-2,2)
=\begin{pmatrix}-2&0\\0&2\end{pmatrix},
$$

and $\Phi(e_1+ie_2)=\begin{pmatrix}0&-2i\\0&0\end{pmatrix}$.

*Proof.* Direct evaluation of the model on $e_1+ie_2$ and on the value $-2ie_3$. Verified on the witness.

**Remark (the diagonal is visible in the trace-zero matrices).** The block is pure vector, so its matrices are traceless; the diagonal element $\operatorname{diag}(-2,2)$ is the model form of $-2ie_3$, of determinant $-4$, the sum of the squares of the coordinates of the value. On the real basis the block is the ordinary cross product, and its matrices are the traceless matrices of the cross product; off the real basis the value is the conjugate cross product, and the model keeps the trace zero.

### The Conjugate-Linearity in the Model

**Proposition.** The right-hand side of the matrix form is $\mathbb{C}$-linear in $\Phi(\tilde P)$ and conjugate-linear in $\Phi(\tilde Q)$:

$$
\Phi\bigl((A\tilde P)\diamond\tilde Q\bigr)=A\,\Phi(\tilde P\diamond\tilde Q),\qquad
\Phi\bigl(\tilde P\diamond(A\tilde Q)\bigr)=\overline{A}\,\Phi(\tilde P\diamond\tilde Q)\qquad(A\in\mathbb{C}).
$$

*Proof.* The adjugate is linear and the conjugate transpose is conjugate-linear in the entries, so the first slot enters linearly and the second through the conjugate transpose, which carries the conjugate. Verified on general elements.

**Remark (the model expresses the class).** The class of the block is visible in the model as the split between the adjugate, which is linear, and the conjugate transpose, which is conjugate-linear; the half-difference of the two twisted products is again of that class, and this is the matrix form of the sesquilinearity of the block.

### The Pairing in the Model

**Theorem (the adjugated conjugate-transposed trace form).** For all biquaternions,

$$
K(\tilde P,\tilde Q)=\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\Phi(\tilde P)\,\Phi(\tilde Q)^{\dagger}\bigr),
$$

the pairing in which the conjugate transpose of the second argument is adjugated in the first, and the pairing of the block is the same trace form read on the value,

$$
K\bigl(\tilde P\diamond\tilde Q,\tilde R\bigr)
=\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\Phi(\tilde P\diamond\tilde Q)\,\Phi(\tilde R)^{\dagger}\bigr)
=-\bigl(\mathbf{P}\times\overline{\mathbf{Q}},\overline{\mathbf{R}}\bigr).
$$

*Proof.* The trace form of the model is the Krein form, by *The Krein Gram Matrix and the Restrictions of the Form* and *The Symmetric Quaternionic Sesqualgebra in the Matrix Representations*, $\tfrac12\operatorname{Tr}\bigl(\operatorname{adj}\Phi(\tilde P)\Phi(\tilde Q)^{\dagger}\bigr)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$; the block is pure vector, so the trace reads the vector part with the sign $-1$ and the conjugation on the third argument. Verified on general elements.

## The Four-by-Four Regular Model

### The Model and Its Conjugations

**Definition.** The **left regular representation** $\rho_L$ sends $\tilde Q$ to the matrix of the left multiplication $\tilde R\mapsto\tilde Q\tilde R$ of the plain product, with $\rho_L(\tilde Q^{\natural})=\rho_L(\tilde Q)^{T}$, $\rho_L(\tilde Q^{*})=\rho_L(\tilde Q)^{\dagger}$, and $\operatorname{Tr}\rho_L(\tilde Q)=4Q_0$.

*Proof.* The regular representation of an associative algebra is multiplicative, and the two conjugations are the transpose and the conjugate transpose of the matrix, as in *Introduction to the 4×4 Regular Matrix Representation of Biquaternions*. Verified on the generators.

### The Matrix Form of the Block

**Theorem.** For all biquaternions,

$$
\rho_L\bigl(\tilde P\diamond\tilde Q\bigr)
=\tfrac12\Bigl(\rho_L(\tilde P)^{T}\rho_L(\tilde Q)^{\dagger}
-\rho_L(\tilde Q)^{\dagger}\rho_L(\tilde P)^{T}\Bigr),
$$

again the half-difference of the two twisted regular products, with the transpose in the first slot and the conjugate transpose in the second.

*Proof.* The products $\tilde P^{\natural}\tilde Q^{*}$ and $\tilde Q^{*}\tilde P^{\natural}$ read $\rho_L(\tilde P)^{T}\rho_L(\tilde Q)^{\dagger}$ and $\rho_L(\tilde Q)^{\dagger}\rho_L(\tilde P)^{T}$ in the model, and the block is their half-difference. Verified on general elements.

**Proposition (the value is traceless).** $\operatorname{Tr}\rho_L(\tilde P\diamond\tilde Q)=0$ for all biquaternions, the block being pure vector.

*Proof.* The trace of the regular matrix is $4Q_0$, and the block has scalar coordinate zero. Verified on general elements.

**Remark (the two models agree on the block).** The half-difference is the same expression in the two models, with the adjugate in the $2\times2$ model and the transpose in the regular model, both being the matrices of the natural conjugation; the conjugate transpose is the second operation in both. The two models therefore carry the same theorem, and the value is traceless in both because the block is pure vector.

## The Comparison with the Two Algebras and the Plain Row

**Remark (the four blocks in the models).** The two algebras of the corpus carry the antisymmetric parts $\mathrm{AQA}$ and $\mathrm{APA}$, both $\mathbb{C}$-bilinear and therefore linear in the second argument, and their matrix forms are the half-differences of two ordinary matrix products, $\tfrac12(\operatorname{adj}\Phi(\tilde P)\Phi(\tilde Q)-\operatorname{adj}\Phi(\tilde Q)\Phi(\tilde P))$ for $\mathrm{AQA}$ and the commutator for $\mathrm{APA}$. The two sesqualgebras carry the antisymmetric parts $\mathrm{APS}$ and $\mathrm{AQS}$, both sesquilinear, and their matrix forms are the half-differences of a product with one conjugation in each slot and the same product in the other order: for $\mathrm{APS}$ the first slot is unadorned and the second is the conjugate transpose, and for $\mathrm{AQS}$ the first slot carries the matrix of the natural conjugation and the second the conjugate transpose. The block is therefore the $\mathrm{AQS}$ of the table, the half-difference with the **adjugate in the first slot** in the $2\times2$ model and the **transpose in the first slot** in the regular model, and this single distinction from $\mathrm{APS}$ is the whole difference between the two sesquilinear antisymmetric parts in the models.

**Remark (the model invariants of the block).** In the $2\times2$ model the invariants of the block are its vanishing trace, the determinant of its value, which is the sum of the squares of the coordinates of the conjugate cross product, and the trace form of the pairing; the determinant is not a norm and changes sign on the cone of the diagonal. In the regular model the block is carried to the traceless matrices, and the pairing is the trace form of the regular matrix. The two readings agree, and the operator-side statement of the same facts is *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*.

## Summary

In the $2\times2$ realization the block is the half-difference of the two twisted matrix products, $\Phi(\tilde P\diamond\tilde Q)=\tfrac12(\operatorname{adj}\Phi(\tilde P)\Phi(\tilde Q)^{\dagger}-\Phi(\tilde Q)^{\dagger}\operatorname{adj}\Phi(\tilde P))$, with the matrix of the natural conjugation, the adjugate, in the first slot and the conjugate transpose in the second; in the $4\times4$ regular representation it is the same half-difference with the transpose in the first slot, $\rho_L(\tilde P\diamond\tilde Q)=\tfrac12(\rho_L(\tilde P)^{T}\rho_L(\tilde Q)^{\dagger}-\rho_L(\tilde Q)^{\dagger}\rho_L(\tilde P)^{T})$. In both models the value is traceless, because the block is pure vector, and at the witness $e_1+ie_2$ the value $-2ie_3$ has matrix $\operatorname{diag}(-2,2)$. The block is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second, the model split being the one between the adjugate or transpose and the conjugate transpose. The pairing of the block is the adjugated conjugate-transposed trace form of the $2\times2$ model and the trace form of the regular model, both reading the form $K$ on the value. The comparison with the plain row isolates the block as the half-difference with the natural conjugation in the first slot, the difference of the two sesquilinear antisymmetric parts in the models.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi(e_0)=I$, $\Phi(e_k)=-i\sigma_k$ | the $2\times2$ realization |
| $\Phi(\tilde Q^{\natural})=\operatorname{adj}\Phi(\tilde Q)$, $\Phi(\tilde Q^{*})=\Phi(\tilde Q)^{\dagger}$ | the two conjugations in the model |
| $\Phi(\tilde P\diamond\tilde Q)=\tfrac12(\operatorname{adj}\Phi(\tilde P)\Phi(\tilde Q)^{\dagger}-\Phi(\tilde Q)^{\dagger}\operatorname{adj}\Phi(\tilde P))$ | the block in the $2\times2$ model |
| $\rho_L(\tilde Q^{\natural})=\rho_L(\tilde Q)^{T}$, $\rho_L(\tilde Q^{*})=\rho_L(\tilde Q)^{\dagger}$ | the two conjugations in the regular model |
| $\rho_L(\tilde P\diamond\tilde Q)=\tfrac12(\rho_L(\tilde P)^{T}\rho_L(\tilde Q)^{\dagger}-\rho_L(\tilde Q)^{\dagger}\rho_L(\tilde P)^{T})$ | the block in the regular model |
| $\operatorname{diag}(-2,2)$ | the value $-2ie_3$ at $e_1+ie_2$ |
| trace $0$ | the value is pure vector |
| $\tfrac12\operatorname{Tr}(\operatorname{adj}\Phi(\tilde P)\Phi(\tilde Q)^{\dagger})$ | the trace form of the pairing |

## Further Reading

- *Introduction to the 2×2 Matrix Representation of Biquaternions*, for the model, its multiplicativity and the two conjugations.
- *Introduction to the 4×4 Regular Matrix Representation of Biquaternions*, for the regular model and its conjugations.
- *The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Representation* and *The General Quaternionic Sesqualgebra in the $4\times4$ Regular Matrix Representation*, for the product the block splits in the two models.
- *Introduction to the Antisymmetric Quaternionic Sesqualgebra of Biquaternions*, for the block.
- *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra*, for the diagonal and its cone.
- *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*, for the operators of the block.
