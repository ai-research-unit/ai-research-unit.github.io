# __The Antisymmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$__

## Introduction

The block computes the operation $\tilde P\diamond\tilde Q=\mathrm{Vect}(\tilde P\tilde Q^{*})$ in the $2\times2$ realization of *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*. The starting point is the product of the row: it is the matrix product with the **conjugate transpose** of the second factor, and the block is its **vector part**, so the operation is read by the trace. In the $2\times2$ model the vector part of an element is its **traceless part**, and the block is

$$
\mathsf{M}_2(\tilde P\diamond\tilde Q)=M-\tfrac12\operatorname{Tr}(M)\,I
=\tfrac12\bigl(M-\operatorname{adj}(M)\bigr),
\qquad
M=\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger},
$$

half the difference of the conjugate-transposed product and its **adjoint matrix**, the model of the natural conjugation. This article is the first of the two representation articles of the block, and its companion *The Antisymmetric Plain Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* reads the same operation on the regular model.

The image is the **traceless** matrices, of complex dimension three, the **traceless skew-Hermitian** matrices among them, a real three-dimensional space, being the image of the real vector triple; the rank of a value is two, one or zero according to the **isotropy** of the value for the complex bilinear norm form, not according to the vanishing of the value. The distinction between the two forms carried by the block is the point of the article: the positive definite form $H(\tilde P\diamond\tilde Q,\tilde P\diamond\tilde Q)$ vanishes only on the zero value, while the determinant of the matrix of the value, which is the complex bilinear form $\sum_\mu V_\mu^2$, vanishes on the whole isotropic cone.

The setting and the notation are those of *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions*; the model and its invariants are *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* and *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*; the form $H$, the norm $N$ and the zero divisors are *Biquaternion Norm and Invertibility*; the operator whose invariants appear here is *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra*; and the invariants of a linear map are *Linear Maps and Matrices*, §*Rank* and §*The Trace and the Determinant of a Matrix*. The purity list of the pass is respected: the matrix invariants are the rank, the trace and the determinant, and no word of distance, of limit or of continuity occurs.

## The Model

**Recall (the $2\times2$ realization).** The matrix realization of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* is the isomorphism written $\mathsf{M}_2$,
$$
\mathsf{M}_2:\mathbb{B}\longrightarrow M_2(\mathbb{C}),
$$
fixed by its values on the basis, the rest following by $\mathbb{C}$-linearity: $\mathsf{M}_2(e_0)=I$ and $\mathsf{M}_2(e_k)=-i\sigma_k$, with $\mathsf{M}_2(\tilde Q^{\natural})=\operatorname{adj}\mathsf{M}_2(\tilde Q)$, $\mathsf{M}_2(\tilde Q^{*})=\mathsf{M}_2(\tilde Q)^{\dagger}$, $\operatorname{Tr}\mathsf{M}_2(\tilde Q)=2Q_0$ and $\det\mathsf{M}_2(\tilde Q)=N(\tilde Q)=\sum_\mu Q_\mu^2$. It is a $*$-isomorphism, and it carries the Hermitian conjugation of the algebra to the conjugate transpose of the matrices.

**The vector part.** In the model the vector part of an element is read by the trace,

$$
\mathsf{M}_2\bigl(\mathrm{Vect}(\tilde X)\bigr)=\mathsf{M}_2(\tilde X)-\tfrac12\operatorname{Tr}\mathsf{M}_2(\tilde X)\,I ,
$$

the **traceless part** of the matrix.

*Proof.* $\mathsf{M}_2(\tilde X)=X_0I-i(X_1\sigma_1+X_2\sigma_2+X_3\sigma_3)$ and $\operatorname{Tr}\mathsf{M}_2(\tilde X)=2X_0$, so subtracting $\tfrac12\operatorname{Tr}\mathsf{M}_2(\tilde X)I=X_0I$ leaves $-i\sum_kX_k\sigma_k=\mathsf{M}_2(\mathrm{Vect}\tilde X)$. $\square$

## The Block in the Model

**Theorem (the block is the traceless part of the conjugate-transposed product).** For all biquaternions,

$$
\mathsf{M}_2(\tilde P\diamond\tilde Q)=\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}
-\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}\bigr)\,I
=\tfrac12\bigl(M-\operatorname{adj}(M)\bigr),
\qquad M=\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}.
$$

*Proof.* $\mathsf{M}_2$ is multiplicative and carries ${}^{*}$ to the conjugate transpose, so $\mathsf{M}_2(\tilde P\tilde Q^{*})=\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}=M$; the block is the vector part, so the vector part of the model gives the first display, and the second is the identity $\operatorname{adj}(M)=\operatorname{Tr}(M)I-M$ of the $2\times2$ matrices. Verified on random pairs. $\square$

**Corollary (the two halves of the product).** The product and the block are the two terms of the split of the matrix product,

$$
M=\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}
=\tfrac12\operatorname{Tr}(M)\,I+\mathsf{M}_2(\tilde P\diamond\tilde Q),
$$

the scalar matrix $\tfrac12\operatorname{Tr}(M)I=\mathsf{M}_2(\mathrm{SPS}(\tilde P,\tilde Q))$ and the traceless matrix of the block; the split of *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra* is read here as the split of a matrix into its scalar part and its traceless part.

**Corollary (the adjoint matrix is the natural conjugation).** Because $\overline{\tilde Q\tilde P^{*}}=\mathrm{Nat}(\tilde P\tilde Q^{*})$ for the natural conjugation ${}^{\natural}$, and $\mathsf{M}_2(\tilde X^{\natural})=\operatorname{adj}\mathsf{M}_2(\tilde X)$, the second term of the half-difference is the image of the conjugate-transposed product under the natural conjugation,

$$
\mathsf{M}_2\bigl(\overline{\tilde Q\tilde P^{*}}\bigr)=\operatorname{adj}(M),
$$

so the block is literally $\tfrac12\bigl(\mathsf{M}_2(\tilde P\tilde Q^{*})-\mathsf{M}_2(\overline{\tilde Q\tilde P^{*}})\bigr)$, the model of the definition. The adjoint matrix is **not** the conjugate transpose of $M$; the conjugate transpose is the model of ${}^{*}$, and the two coincide only on the special pairs.

*Proof.* $\overline{\tilde Q\tilde P^{*}}=\mathrm{Nat}(\tilde P\tilde Q^{*})$, since the natural conjugation of a Hermitian element is its coefficientwise conjugate; applying $\mathsf{M}_2$ and the identity $\mathsf{M}_2(\tilde X^{\natural})=\operatorname{adj}\mathsf{M}_2(\tilde X)$ gives the display. $\square$

**Remark (the matrix reading of the two conjugations).** In the model the conjugations of the block are three distinct matrix operations: the coefficientwise conjugation of the algebra is $\operatorname{adj}\circ{}^{\dagger}$ in the model, since $\overline{\tilde X}=\mathrm{Nat}(\tilde X^{*})$ and $\mathsf{M}_2(\tilde X^{*})=\mathsf{M}_2(\tilde X)^{\dagger}$; the natural conjugation is $\operatorname{adj}$; and the Hermitian conjugation is the conjugate transpose ${}^{\dagger}$. The block uses the first and the second, through the identity of the corollary, and not the third alone.

**Remark (the conjugate-transposed commutator is not the block).** Read with the conjugate transpose in both slots, the antisymmetrisation of the conjugate-transposed product would be the matrix commutator $\tfrac12\bigl(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}-\mathsf{M}_2(\tilde Q)^{\dagger}\mathsf{M}_2(\tilde P)\bigr)$. Since $\mathsf{M}_2$ is multiplicative and $\mathsf{M}_2(\tilde Q)^{\dagger}=\mathsf{M}_2(\tilde Q^{*})$, this is $\mathsf{M}_2\bigl(\mathrm{APA}(\tilde P,\tilde Q^{*})\bigr)$, the model of the plain commutator $\tfrac12(\tilde P\tilde Q^{*}-\tilde Q^{*}\tilde P)$ of the first argument with the star of the second: a traceless matrix, hence a value of the block for some element, but not the value $\mathsf{M}_2(\tilde P\diamond\tilde Q)$. The conjugation in the second term of the block is the **coefficientwise** one, which is $\operatorname{adj}\circ{}^{\dagger}$ in the model, and it is what replaces the conjugate transpose of the swapped product; the two expressions differ on general pairs, as at $(\tilde P,\tilde Q)=(e_0,e_1)$, where the block gives the matrix of $-e_1$, that is $i\sigma_1$, and the commutator vanishes.

## The Image and its Invariants

**Theorem (the image is the traceless matrices).** The image of the block in the model is

$$
\mathsf{M}_2\bigl(\mathrm{Vect}(\mathbb{B})\bigr)
=\bigl\{X\in M_2(\mathbb{C}):\ \operatorname{Tr}X=0\bigr\},
$$

the **traceless** matrices, of complex dimension three; the **traceless skew-Hermitian** matrices among them, the real three-dimensional space spanned over $\mathbb{R}$ by $-i\sigma_1,-i\sigma_2,-i\sigma_3$, are the image of the real vector triple $\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$.

*Proof.* The value $\tilde P\diamond\tilde Q$ is a pure vector, so its matrix is traceless; the three matrices $-i\sigma_k$ are $\mathbb{C}$-linearly independent and have zero trace, so the image is the whole traceless space, of complex dimension three, which is the complex dimension of $\mathrm{Vect}(\mathbb{B})$. Each $-i\sigma_k$ is skew-Hermitian, $(-i\sigma_k)^{\dagger}=i\sigma_k=-(-i\sigma_k)$, so a real combination of the three is skew-Hermitian; a combination with a non-real coefficient has a Hermitian part and is not, so the traceless skew-Hermitian matrices are exactly the image of the real vector triple. Verified on the model. $\square$

**Theorem (the invariants).** For every value $\tilde V=\tilde P\diamond\tilde Q$ of the block,

$$
\operatorname{Tr}\mathsf{M}_2(\tilde V)=0,
\qquad
\det\mathsf{M}_2(\tilde V)=\sum_\mu V_\mu^2=N(\tilde V),
$$

and the rank of the matrix is

$$
\operatorname{rank}\mathsf{M}_2(\tilde V)=
\begin{cases}
2, & N(\tilde V)\neq0,\\
1, & N(\tilde V)=0,\ \tilde V\neq0,\\
0, & \tilde V=0.
\end{cases}
$$

*Proof.* The trace vanishes because the value is a pure vector, by the preceding theorem; the determinant is $\det\mathsf{M}_2(\tilde X)=N(\tilde X)$ for every $\tilde X$, by the invariants of the model. For the rank, $\det\mathsf{M}_2(\tilde V)=N(\tilde V)$, so the rank is two exactly when the determinant is nonzero; otherwise the matrix is nonzero and traceless — hence of rank one — or it is zero. Verified on the model. $\square$

**Corollary (the two forms of the value).** The two forms attached to a value are read differently in the model: the **positive definite** form of the block is

$$
H\bigl(\tilde V,\tilde V\bigr)=\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde V)\mathsf{M}_2(\tilde V)^{\dagger}\bigr)
=\tfrac12\sum_{i,j}\bigl\lvert\mathsf{M}_2(\tilde V)_{ij}\bigr\rvert^{2},
$$

which vanishes only at $\tilde V=0$, while the **complex bilinear** form is the determinant $\det\mathsf{M}_2(\tilde V)=\sum_\mu V_\mu^2$, which vanishes on the isotropic cone $N(\tilde V)=0$, a quadric that contains the nonzero values, for instance $\tilde V=e_1+ie_2$. The block therefore has a value of rank one, $e_1+ie_2$, whose matrix is traceless and has zero determinant; the rank of the matrix reads the bilinear form, and the positivity of the Hilbert–Schmidt pairing reads the definite one.

**Remark (the isotropic value).** The value $e_1+ie_2$ has $N=1+i^2=1-1=0$, so its matrix is a nonzero traceless matrix of determinant zero, of rank one; the value $e_1+e_2$ has $N=1+1=2\neq0$, so its matrix has rank two. The determinant of the matrix of the value is therefore not a definitive test of the vanishing of the value, and the definite form $H$ is needed for that; the distinction is the same as the one of *Biquaternion Norm and Invertibility*, §*The Euclidean Norm and the Hermitian Form*.

## The Matrix Form of the Pairing

**Theorem (the Hilbert–Schmidt pairing).** In the model the form $H$ is the Hilbert–Schmidt pairing of the matrices,

$$
H(\tilde P,\tilde Q)=\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}\bigr).
$$

*Proof.* $\operatorname{Tr}\mathsf{M}_2(\tilde X)=2X_0$; hence $\operatorname{Tr}(\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger})=\operatorname{Tr}\mathsf{M}_2(\tilde P\tilde Q^{*})=2H(\tilde P,\tilde Q)$. Verified on random pairs. $\square$

**Corollary (the pairing of the block).** For the block,

$$
H\bigl(\tilde P\diamond\tilde Q,\tilde R\bigr)
=\tfrac12\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde P\diamond\tilde Q)\,\mathsf{M}_2(\tilde R)^{\dagger}\bigr),
$$

with $\mathsf{M}_2(\tilde P\diamond\tilde Q)$ the traceless part displayed above; the pairing is computed on the values, and it agrees with the coordinate formula of *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*, §*The Pairing with the Form*.

**Theorem (the invariant form in the model).** The unique invariant form of the block, up to a scalar, is the **scalar-slot form**

$$
\beta(\tilde X,\tilde Y)=X_0\overline{Y_0}=\tfrac14\operatorname{Tr}\mathsf{M}_2(\tilde X)\;\overline{\operatorname{Tr}\mathsf{M}_2(\tilde Y)},
$$

and the invariance $\beta(\tilde P\diamond\tilde Q,\tilde R)=-\overline{\beta(\tilde P,\tilde Q\diamond\tilde R)}$ holds **degenerately**, both members vanishing with the trace of the value; no invariant form is non-degenerate.

*Proof.* $\operatorname{Tr}\mathsf{M}_2(\tilde X)=2X_0$, so $\tfrac14\operatorname{Tr}\mathsf{M}_2(\tilde X)\overline{\operatorname{Tr}\mathsf{M}_2(\tilde Y)}=X_0\overline{Y_0}$, which is the invariant form of *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*, §*The Invariance Forms*; the degeneracy is the vanishing of the trace of a block value. $\square$

**Remark (the invariants of the operator in the model).** The operator $L^{\diamond}_{\tilde A}$ of *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra* acts on the model by $\mathsf{M}_2(\tilde X)\mapsto\mathsf{M}_2(\tilde A)\mathsf{M}_2(\tilde X)^{\dagger}-\tfrac12\operatorname{Tr}(\cdot)I$, a map of the traceless part of the conjugate-transposed product; its invariants are those computed there, trace zero and characteristic polynomial $\lambda^{2}(\lambda^{2}-1)^{3}$ at $\tilde A=e_0$ and $\lambda^{4}(\lambda^{2}+1)^{2}$ at $\tilde A=e_k$, and they are unchanged by the model, the realization being a $*$-isomorphism.

## The Matrices

**The generators.** The realization is fixed on the basis by four matrices:

$$
\mathsf{M}_2(e_0)=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad
\mathsf{M}_2(e_1)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\qquad
\mathsf{M}_2(e_2)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
\mathsf{M}_2(e_3)=\begin{pmatrix}-i&0\\0&i\end{pmatrix}.
$$

with the involution of the natural conjugation carried to the adjugate, $\operatorname{adj}X=(\operatorname{Tr}X)I-X$, and the involution of the Hermitian conjugation to the conjugate transpose.

**The block, entry by entry.** The block is the traceless part of the conjugate-transposed product, that is half the difference of the product and its adjugate,

$$
\mathsf{M}_2(\tilde P\diamond\tilde Q)=M-\tfrac12\operatorname{Tr}(M)I_2=\tfrac12\bigl(M-\operatorname{adj}(M)\bigr),\qquad M=XY^{\dagger},
$$

both models splitting $M$ into the scalar matrix $\tfrac12\operatorname{Tr}(M)I_2$ and the traceless matrix of the block.

**The witness, entry by entry.** At the pair $e_0,e_1$ the conjugate-transposed product is $\mathsf{M}_2(e_1)^{\dagger}=\begin{pmatrix}0&i\\i&0\end{pmatrix}$ and the block is that matrix itself,

$$
\mathsf{M}_2(e_0\diamond e_1)=\tfrac12\Bigl(\begin{pmatrix}0&i\\i&0\end{pmatrix}-\begin{pmatrix}0&-i\\-i&0\end{pmatrix}\Bigr)=\begin{pmatrix}0&i\\i&0\end{pmatrix}=i\sigma_1=\mathsf{M}_2(-e_1),
$$

which is $e_0\diamond e_1=\mathrm{Vect}(e_0e_1^{*})=\mathrm{Vect}(-e_1)=-e_1$; the matrix is traceless, skew-Hermitian of rank two, and its determinant is $N(-e_1)=1$.

## Summary

In the $2\times2$ model the block is the traceless part of the conjugate-transposed product, $\mathsf{M}_2(\tilde P\diamond\tilde Q)=M-\tfrac12\operatorname{Tr}(M)I=\tfrac12(M-\operatorname{adj}M)$ with $M=\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}$, half the difference of $M$ and its adjoint matrix; the adjoint matrix is the model of the natural conjugation, and the conjugate transpose in the model is the model of ${}^{*}$. The image is the traceless matrices, of complex dimension three, and the traceless skew-Hermitian ones, spanned by $-i\sigma_1,-i\sigma_2,-i\sigma_3$, are the image of the real vector triple; every value has trace zero and determinant $N(\tilde V)=\sum_\mu V_\mu^2$, and the rank is two, one or zero according as $N\neq0$, $N=0$ with $\tilde V\neq0$, or $\tilde V=0$; the positive definite form $H$ vanishes only on the zero value, while the determinant vanishes on the whole isotropic cone, with $e_1+ie_2$ a nonzero value of rank one. The form is the Hilbert–Schmidt pairing, $\tfrac12\operatorname{Tr}$ in this model, and the unique invariant form is the scalar-slot form $X_0\overline{Y_0}=\tfrac14\operatorname{Tr}\mathsf{M}_2(\tilde X)\overline{\operatorname{Tr}\mathsf{M}_2(\tilde Y)}$, degenerate on every value.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2$ | the $2\times2$ realization, $\mathsf{M}_2(e_0)=I$, $\mathsf{M}_2(e_k)=-i\sigma_k$, $\mathsf{M}_2(\tilde Q^{*})=\mathsf{M}_2(\tilde Q)^{\dagger}$ |
| $\operatorname{adj}$ | the adjoint matrix, the model of the natural conjugation, $\mathsf{M}_2(\tilde Q^{\natural})=\operatorname{adj}\mathsf{M}_2(\tilde Q)$ |
| $\mathsf{M}_2(\tilde P\diamond\tilde Q)=M-\tfrac12\operatorname{Tr}(M)I$ | the block in the model, the traceless part |
| $N(\tilde X)=\sum_\mu X_\mu^2$ | the complex bilinear norm, the determinant of the matrix |
| $\operatorname{Tr}=0$, rank $2/1/0$ | the invariants of the value |
| $H=\tfrac12\operatorname{Tr}\mathsf{M}_2(\cdot)\mathsf{M}_2(\cdot)^{\dagger}$ | the form as the Hilbert–Schmidt pairing |
| $X_0\overline{Y_0}=\tfrac14\operatorname{Tr}\mathsf{M}_2(\cdot)\overline{\operatorname{Tr}\mathsf{M}_2(\cdot)}$ | the unique invariant form, degenerate |

## Further Reading

- *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-sesqualgebra-of-biquaternions.md`), for the operation and its two conjugations
- *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-sesquilinear-pairing-of-the-antisymmetric-plain-sesqualgebra.md`), for the pairing, the trace form and the invariant forms computed here in the model
- *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-adjoint-operators-and-the-sandwich-of-the-antisymmetric-plain-sesqualgebra.md`), for the operator whose invariants the model carries
- *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-general-plain-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the product of the row and the form in the model
- *The Antisymmetric Plain Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/the-antisymmetric-plain-sesqualgebra-in-the-4x4-matrix-element-representation.md`), for the reading on the regular model
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the two forms, the norm, the zero divisors and the isotropic cone
- *Linear Maps and Matrices* (`articles_maths/linear-maps-and-matrices.md`), for the matrix of a linear map and its invariants
