# __The Antisymmetric Plain Sesqualgebra in the Matrix Representations__

## Introduction

The block has two matrix readings, those of *The General Plain Sesqualgebra in the $2\times2$ Matrix Representation* and *The General Plain Sesqualgebra in the $4\times4$ Matrix Representation*, and this article computes the operation $\tilde P\diamond\tilde Q=\mathrm{Vect}(\tilde P\tilde Q^{*})$ in both. The starting point is the same in the two models: the product of the row is the matrix product with the **conjugate transpose** of the second factor, and the block is its **vector part**, so the operation is read by the trace. In the $2\times2$ model the vector part of an element is its **traceless part**, and the block is

$$
\Phi(\tilde P\diamond\tilde Q)=M-\tfrac12\operatorname{Tr}(M)\,I
=\tfrac12\bigl(M-\operatorname{adj}(M)\bigr),
\qquad
M=\Phi(\tilde P)\Phi(\tilde Q)^{\dagger},
$$

half the difference of the conjugate-transposed product and its **adjoint matrix**, the model of the natural conjugation. In the $4\times4$ model the same statement reads $\operatorname{mat}_4(\tilde P\diamond\tilde Q)=M-\tfrac14\operatorname{Tr}(M)I$ with $M=\operatorname{mat}_4(\tilde P)\operatorname{mat}_4(\tilde Q)^{\dagger}$, and the two models agree on the invariants.

The one difference between the two readings is the shape of the image. In the $2\times2$ model the image is the **traceless** matrices, of complex dimension three, the **traceless skew-Hermitian** matrices among them, a real three-dimensional space, being the image of the real vector triple; in the $4\times4$ model the image is the image of the vector subspace under the regular representation, again of complex dimension three, and the rank of a value is four, two or zero according to the **isotropy** of the value for the complex bilinear norm form, not according to the vanishing of the value. The two ranks are computed, and the distinction between the two forms carried by the block is the point of the article: the positive definite form $H(\tilde P\diamond\tilde Q,\tilde P\diamond\tilde Q)$ vanishes only on the zero value, while the determinant of the matrix of the value, which is the complex bilinear form $\sum_\mu V_\mu^2$, vanishes on the whole isotropic cone.

The setting and the notation are those of *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions*; the $2\times2$ model and its invariants are *Introduction to the 2×2 Matrix Representation of Biquaternions* and *The General Plain Sesqualgebra in the $2\times2$ Matrix Representation*; the regular model is *Introduction to the 4×4 Matrix Representation $M_4(\mathbb{C})_L$ of Biquaternions* and *The General Plain Sesqualgebra in the $4\times4$ Matrix Representation*; the form $H$, the norm $N$ and the zero divisors are *Biquaternion Norm and Invertibility*; the operator whose invariants appear here is *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra*, above in this block; and the invariants of a linear map are *Linear Maps and Matrices*, §*Rank* and §*The Trace and the Determinant of a Matrix*. The purity list of the pass is respected: the matrix invariants are the rank, the trace and the determinant, and no word of distance, of limit or of continuity occurs.

## The Models

**Recall (the $2\times2$ realization).** The matrix realization of *Introduction to the 2×2 Matrix Representation of Biquaternions* is the $\mathbb{C}$-linear isomorphism

$$
\Phi:\mathbb{B}\longrightarrow M_2(\mathbb{C}),\qquad
\Phi(e_0)=I,\qquad \Phi(e_k)=-i\sigma_k,
$$

with $\Phi(\tilde Q^{\natural})=\operatorname{adj}\Phi(\tilde Q)$, $\Phi(\tilde Q^{*})=\Phi(\tilde Q)^{\dagger}$, $\operatorname{Tr}\Phi(\tilde Q)=2Q_0$ and $\det\Phi(\tilde Q)=N(\tilde Q)=\sum_\mu Q_\mu^2$. It is a $*$-isomorphism, and it carries the Hermitian conjugation of the algebra to the conjugate transpose of the matrices.

**Recall (the left regular representation).** The left regular representation of *Introduction to the 4×4 Matrix Representation $M_4(\mathbb{C})_L$ of Biquaternions* is $\operatorname{mat}_4(\tilde Q)(\tilde R)=\tilde Q\tilde R$ read in the basis $e_0,e_1,e_2,e_3$, with

$$
\operatorname{mat}_4(\tilde Q^{*})=\operatorname{mat}_4(\tilde Q)^{\dagger},\qquad
\operatorname{Tr}\operatorname{mat}_4(\tilde Q)=4Q_0,\qquad
\det\operatorname{mat}_4(\tilde Q)=N(\tilde Q)^{2}.
$$

**The two vector parts.** In each model the vector part of an element is read by the trace: in the $2\times2$ model

$$
\Phi\bigl(\mathrm{Vect}(\tilde X)\bigr)=\Phi(\tilde X)-\tfrac12\operatorname{Tr}\Phi(\tilde X)\,I ,
$$

the **traceless part** of the matrix, and in the $4\times4$ model

$$
\operatorname{mat}_4\bigl(\mathrm{Vect}(\tilde X)\bigr)=\operatorname{mat}_4(\tilde X)-\tfrac14\operatorname{Tr}\operatorname{mat}_4(\tilde X)\,I .
$$

*Proof.* In the $2\times2$ model, $\Phi(\tilde X)=X_0I-i(X_1\sigma_1+X_2\sigma_2+X_3\sigma_3)$ and $\operatorname{Tr}\Phi(\tilde X)=2X_0$, so subtracting $\tfrac12\operatorname{Tr}\Phi(\tilde X)I=X_0I$ leaves $-i\sum_kX_k\sigma_k=\Phi(\mathrm{Vect}\tilde X)$; the regular case is the same with $\operatorname{mat}_4(e_0)=I$ and $\operatorname{Tr}\operatorname{mat}_4(\tilde X)=4X_0$. $\square$

## The Block in the $2\times2$ Model

**Theorem (the block is the traceless part of the conjugate-transposed product).** For all biquaternions,

$$
\Phi(\tilde P\diamond\tilde Q)=\Phi(\tilde P)\Phi(\tilde Q)^{\dagger}
-\tfrac12\operatorname{Tr}\bigl(\Phi(\tilde P)\Phi(\tilde Q)^{\dagger}\bigr)\,I
=\tfrac12\bigl(M-\operatorname{adj}(M)\bigr),
\qquad M=\Phi(\tilde P)\Phi(\tilde Q)^{\dagger}.
$$

*Proof.* $\Phi$ is multiplicative and carries ${}^{*}$ to the conjugate transpose, so $\Phi(\tilde P\tilde Q^{*})=\Phi(\tilde P)\Phi(\tilde Q)^{\dagger}=M$; the block is the vector part, so the proposition of §*The Models* gives the first display, and the second is the identity $\operatorname{adj}(M)=\operatorname{Tr}(M)I-M$ of the $2\times2$ matrices. $\square$

**Corollary (the two halves of the product).** The product and the block are the two terms of the split of the matrix product,

$$
M=\Phi(\tilde P)\Phi(\tilde Q)^{\dagger}
=\tfrac12\operatorname{Tr}(M)\,I+\Phi(\tilde P\diamond\tilde Q),
$$

the scalar matrix $\tfrac12\operatorname{Tr}(M)I=\Phi(\mathrm{SPS}(\tilde P,\tilde Q))$ and the traceless matrix of the block; the split of *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra* is read here as the split of a matrix into its scalar part and its traceless part.

**Corollary (the adjoint matrix is the natural conjugation).** Because $\overline{\tilde Q\tilde P^{*}}=\mathrm{Nat}(\tilde P\tilde Q^{*})$ for the natural conjugation ${}^{\natural}$, and $\Phi(\tilde X^{\natural})=\operatorname{adj}\Phi(\tilde X)$, the second term of the half-difference is the image of the conjugate-transposed product under the natural conjugation,

$$
\Phi\bigl(\overline{\tilde Q\tilde P^{*}}\bigr)=\operatorname{adj}(M),
$$

so the block is literally $\tfrac12\bigl(\Phi(\tilde P\tilde Q^{*})-\Phi(\overline{\tilde Q\tilde P^{*}})\bigr)$, the model of the definition. The adjoint matrix is **not** the conjugate transpose of $M$; the conjugate transpose is the model of ${}^{*}$, and the two coincide only on the special pairs, as the remark below records.

*Proof.* $\overline{\tilde Q\tilde P^{*}}=\mathrm{Nat}(\tilde P\tilde Q^{*})$, since the natural conjugation of a Hermitian element is its coefficientwise conjugate; applying $\Phi$ and the identity $\Phi(\tilde X^{\natural})=\operatorname{adj}\Phi(\tilde X)$ gives the display. $\square$

**Remark (the matrix reading of the two conjugations).** In the $2\times2$ model the four conjugations of the block are three distinct matrix operations: the coefficientwise conjugation of the algebra is $\operatorname{adj}\circ{}^{\dagger}$ in the model, since $\overline{\tilde X}=\mathrm{Nat}(\tilde X^{*})$ and $\Phi(\tilde X^{*})=\Phi(\tilde X)^{\dagger}$; the natural conjugation is $\operatorname{adj}$; and the Hermitian conjugation is the conjugate transpose ${}^{\dagger}$. The block uses the first and the second, through the identity of the corollary, and not the third alone.

**Remark (the conjugate-transposed commutator is not the block).** Read with the conjugate transpose in both slots, the antisymmetrisation of the conjugate-transposed product would be the matrix commutator $\tfrac12\bigl(\Phi(\tilde P)\Phi(\tilde Q)^{\dagger}-\Phi(\tilde Q)^{\dagger}\Phi(\tilde P)\bigr)$. Since $\Phi$ is multiplicative and $\Phi(\tilde Q)^{\dagger}=\Phi(\tilde Q^{*})$, this is $\Phi\bigl(\mathrm{APA}(\tilde P,\tilde Q^{*})\bigr)$, the model of the plain commutator $\tfrac12(\tilde P\tilde Q^{*}-\tilde Q^{*}\tilde P)$ of the first argument with the star of the second: a traceless matrix, hence a value of the block for some element, but not the value $\Phi(\tilde P\diamond\tilde Q)$. The conjugation in the second term of the block is the **coefficientwise** one, which is $\operatorname{adj}\circ{}^{\dagger}$ in the model, and it is what replaces the conjugate transpose of the swapped product; the two expressions differ on general pairs, as at $(\tilde P,\tilde Q)=(e_0,e_1)$, where the block gives the matrix of $-e_1$, that is $i\sigma_1$, and the commutator vanishes.

## The Image and its Invariants

**Theorem (the image is the traceless matrices).** The image of the block in the $2\times2$ model is

$$
\Phi\bigl(\mathrm{Vect}(\mathbb{B})\bigr)
=\bigl\{X\in M_2(\mathbb{C}):\ \operatorname{Tr}X=0\bigr\},
$$

the **traceless** matrices, of complex dimension three; the **traceless skew-Hermitian** matrices among them, the real three-dimensional space spanned over $\mathbb{R}$ by $-i\sigma_1,-i\sigma_2,-i\sigma_3$, are the image of the real vector triple $\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$.

*Proof.* The value $\tilde P\diamond\tilde Q$ is a pure vector, so its matrix is traceless, by §*The Models*; the three matrices $-i\sigma_k$ are $\mathbb{C}$-linearly independent and have zero trace, so the image is the whole traceless space, of complex dimension three, which is the complex dimension of $\mathrm{Vect}(\mathbb{B})$. Each $-i\sigma_k$ is skew-Hermitian, $(-i\sigma_k)^{\dagger}=i\sigma_k=-(-i\sigma_k)$, so a real combination of the three is skew-Hermitian; a combination with a non-real coefficient has a Hermitian part and is not, so the traceless skew-Hermitian matrices are exactly the image of the real vector triple. $\square$

**Theorem (the invariants).** For every value $\tilde V=\tilde P\diamond\tilde Q$ of the block,

$$
\operatorname{Tr}\Phi(\tilde V)=0,
\qquad
\det\Phi(\tilde V)=\sum_\mu V_\mu^2=N(\tilde V),
$$

and the rank of the matrix is

$$
\operatorname{rank}\Phi(\tilde V)=
\begin{cases}
2, & N(\tilde V)\neq0,\\
1, & N(\tilde V)=0,\ \tilde V\neq0,\\
0, & \tilde V=0.
\end{cases}
$$

*Proof.* The trace vanishes because the value is a pure vector, by the preceding theorem; the determinant is $\det\Phi(\tilde X)=N(\tilde X)$ for every $\tilde X$, by the invariants of the model. For the rank, $\det\Phi(\tilde V)=N(\tilde V)$, so the rank is two exactly when the determinant is nonzero; otherwise the matrix is nonzero and traceless — hence of rank one — or it is zero. $\square$

**Corollary (the two forms of the value).** The two forms attached to a value are read differently in the model: the **positive definite** form of the block is

$$
H\bigl(\tilde V,\tilde V\bigr)=\tfrac12\operatorname{Tr}\bigl(\Phi(\tilde V)\Phi(\tilde V)^{\dagger}\bigr)
=\tfrac12\sum_{i,j}\bigl\lvert\Phi(\tilde V)_{ij}\bigr\rvert^{2},
$$

which vanishes only at $\tilde V=0$, while the **complex bilinear** form is the determinant $\det\Phi(\tilde V)=\sum_\mu V_\mu^2$, which vanishes on the isotropic cone $N(\tilde V)=0$, a quadric that contains the nonzero values, for instance $\tilde V=e_1+ie_2$. The block therefore has a value of rank one, $e_1+ie_2$, whose matrix is traceless and has zero determinant; the rank of the matrix reads the bilinear form, and the positivity of the Hilbert–Schmidt pairing reads the definite one.

**Remark (the isotropic value).** The value $e_1+ie_2$ has $N=1+i^2=1-1=0$, so its matrix is a nonzero traceless matrix of determinant zero, of rank one; the value $e_1+e_2$ has $N=1+1=2\neq0$, so its matrix has rank two. The determinant of the matrix of the value is therefore not a definitive test of the vanishing of the value, and the definite form $H$ is needed for that; the distinction is the same as the one of *Biquaternion Norm and Invertibility*, §*The Euclidean Norm and the Hermitian Form*.

## The Block in the $4\times4$ Regular Model

**Theorem (the block in the regular model).** For all biquaternions,

$$
\operatorname{mat}_4(\tilde P\diamond\tilde Q)=\operatorname{mat}_4(\tilde P)\operatorname{mat}_4(\tilde Q)^{\dagger}
-\tfrac14\operatorname{Tr}\bigl(\operatorname{mat}_4(\tilde P)\operatorname{mat}_4(\tilde Q)^{\dagger}\bigr)\,I,
$$

the **traceless part** of the conjugate-transposed product of the regular matrices; in particular $\operatorname{Tr}\operatorname{mat}_4(\tilde P\diamond\tilde Q)=0$.

*Proof.* $\operatorname{mat}_4(\tilde P\tilde Q^{*})=\operatorname{mat}_4(\tilde P)\operatorname{mat}_4(\tilde Q)^{\dagger}$ by the $*$-representation property, and the vector part is the traceless part by §*The Models*. $\square$

**Theorem (the invariants in the regular model).** For every value $\tilde V$ of the block,

$$
\operatorname{Tr}\operatorname{mat}_4(\tilde V)=0,
\qquad
\det\operatorname{mat}_4(\tilde V)=N(\tilde V)^{2},
\qquad
\operatorname{rank}\operatorname{mat}_4(\tilde V)=
\begin{cases}
4, & N(\tilde V)\neq0,\\
2, & N(\tilde V)=0,\ \tilde V\neq0,\\
0, & \tilde V=0.
\end{cases}
$$

*Proof.* The trace vanishes because $\operatorname{Tr}\operatorname{mat}_4(\tilde X)=4\mathrm{Sc}(\tilde X)$ and the value is a pure vector; the determinant is $N(\tilde X)^2$ for every $\tilde X$, by the invariants of the model. For the rank, $\det\operatorname{mat}_4(\tilde V)=N(\tilde V)^2$, so the regular matrix is invertible exactly when $N(\tilde V)\neq0$; for $N(\tilde V)=0$ and $\tilde V\neq0$ the left regular representation of a central simple algebra has rank a multiple of the degree two, and the value is a zero divisor, so the rank is two. $\square$

**Remark (the image and the rank in the regular model).** The image of the block in the regular model is the image of the vector subspace under $\operatorname{mat}_4$, of complex dimension three: the value $\tilde V=e_0\diamond\tilde R=\mathbf R$ has regular matrix $\operatorname{mat}_4(\mathbf R)$ of rank four whenever $N(\mathbf R)\neq0$, so the image meets the invertible matrices, while a zero divisor $\mathbf R$ has rank two. The $2\times2$ model reads the same image by the traceless matrices, again of complex dimension three, and the two models have the same rank pattern on the values through the factor two, $\operatorname{rank}\operatorname{mat}_4=2\operatorname{rank}\Phi$ on the values, which is the ratio of the sizes of the two matrix algebras.

**Remark (the two-sided antisymmetrised operator).** The regular model also carries the **two-sided** antisymmetrisation

$$
\tfrac12\bigl(\operatorname{mat}_4(\tilde P)\operatorname{mat}_4^{R}(\tilde Q^{*})-\operatorname{mat}_4(\tilde Q)\operatorname{mat}_4^{R}(\tilde P^{*})\bigr),
$$

the matrix of the map $\tilde X\mapsto\tfrac12\bigl(\tilde P\tilde X\tilde Q^{*}-\tilde Q\tilde X\tilde P^{*}\bigr)$ on the module, with $\operatorname{mat}_4^{R}(\tilde X)$ the right multiplication by $\tilde X$. It is alternating in its two parameters, so it vanishes identically at $\tilde P=\tilde Q$; its trace is $4i\,\mathrm{Im}\bigl(P_0\overline{Q_0}\bigr)$, not zero, and its rank is four for generic parameters, two on the real basis pairs such as $(e_0,e_1)$, and one on special complex pairs such as $(e_0+ie_1,\,ie_0-e_1)$, where the trace is $-4i$. It is not the block's element in the model, which is the traceless part of the one-sided product and has trace zero; and its vanishing diagonal is the opposite of the block's, whose diagonal is the vector part of the square. The distinction is the one of the symmetric row: the block's element is the matrix of the value, and the two-sided operator is the action of the two factors on the module, one-sided in the first case and two-sided in the second.

## The Matrix Form of the Pairing

**Theorem (the Hilbert–Schmidt pairing).** In the two models the form $H$ is the Hilbert–Schmidt pairing of the matrices,

$$
H(\tilde P,\tilde Q)=\tfrac12\operatorname{Tr}\bigl(\Phi(\tilde P)\Phi(\tilde Q)^{\dagger}\bigr)
=\tfrac14\operatorname{Tr}\bigl(\operatorname{mat}_4(\tilde P)\operatorname{mat}_4(\tilde Q)^{\dagger}\bigr).
$$

*Proof.* $\operatorname{Tr}\Phi(\tilde X)=2X_0$ and $\operatorname{Tr}\operatorname{mat}_4(\tilde X)=4X_0$; hence $\operatorname{Tr}(\Phi(\tilde P)\Phi(\tilde Q)^{\dagger})=\operatorname{Tr}\Phi(\tilde P\tilde Q^{*})=2H(\tilde P,\tilde Q)$ and $\operatorname{Tr}(\operatorname{mat}_4(\tilde P)\operatorname{mat}_4(\tilde Q)^{\dagger})=\operatorname{Tr}\operatorname{mat}_4(\tilde P\tilde Q^{*})=4H(\tilde P,\tilde Q)$. $\square$

**Corollary (the pairing of the block).** For the block,

$$
H\bigl(\tilde P\diamond\tilde Q,\tilde R\bigr)
=\tfrac12\operatorname{Tr}\bigl(\Phi(\tilde P\diamond\tilde Q)\,\Phi(\tilde R)^{\dagger}\bigr)
=\tfrac14\operatorname{Tr}\bigl(\operatorname{mat}_4(\tilde P\diamond\tilde Q)\,\operatorname{mat}_4(\tilde R)^{\dagger}\bigr),
$$

with $\Phi(\tilde P\diamond\tilde Q)$ and $\operatorname{mat}_4(\tilde P\diamond\tilde Q)$ the traceless parts displayed above; the pairing is computed on the values, and it agrees with the coordinate formula of *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*, §*The Pairing with the Form*.

**Theorem (the invariant form in the model).** The unique invariant form of the block, up to a scalar, is the **scalar-slot form**

$$
\beta(\tilde X,\tilde Y)=X_0\overline{Y_0}=\tfrac14\operatorname{Tr}\Phi(\tilde X)\;\overline{\operatorname{Tr}\Phi(\tilde Y)},
$$

and the invariance $\beta(\tilde P\diamond\tilde Q,\tilde R)=-\overline{\beta(\tilde P,\tilde Q\diamond\tilde R)}$ holds **degenerately**, both members vanishing with the trace of the value; no invariant form is non-degenerate.

*Proof.* $\operatorname{Tr}\Phi(\tilde X)=2X_0$, so $\tfrac14\operatorname{Tr}\Phi(\tilde X)\overline{\operatorname{Tr}\Phi(\tilde Y)}=X_0\overline{Y_0}$, which is the invariant form of *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*, §*The Invariance Forms*; the degeneracy is the vanishing of the trace of a block value. $\square$

**Remark (the invariants of the operator in the model).** The operator $L^{\diamond}_{\tilde A}$ of *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra* acts on the model by $\Phi(\tilde X)\mapsto\Phi(\tilde A)\Phi(\tilde X)^{\dagger}-\tfrac12\operatorname{Tr}(\cdot)I$, a map of the traceless part of the conjugate-transposed product; its invariants are those computed there, trace zero and characteristic polynomial $\lambda^{2}(\lambda^{2}-1)^{3}$ at $\tilde A=e_0$ and $\lambda^{4}(\lambda^{2}+1)^{2}$ at $\tilde A=e_k$, and they are unchanged by the model, the $2\times2$ realization being a $*$-isomorphism.

## Summary

In the $2\times2$ model the block is the traceless part of the conjugate-transposed product, $\Phi(\tilde P\diamond\tilde Q)=M-\tfrac12\operatorname{Tr}(M)I=\tfrac12(M-\operatorname{adj}M)$ with $M=\Phi(\tilde P)\Phi(\tilde Q)^{\dagger}$, half the difference of $M$ and its adjoint matrix; the adjoint matrix is the model of the natural conjugation, and the conjugate transpose in the model is the model of ${}^{*}$. The image is the traceless matrices, of complex dimension three, and the traceless skew-Hermitian ones, spanned by $-i\sigma_1,-i\sigma_2,-i\sigma_3$, are the image of the real vector triple; every value has trace zero and determinant $N(\tilde V)=\sum_\mu V_\mu^2$, and the rank is two, one or zero according as $N\neq0$, $N=0$ with $\tilde V\neq0$, or $\tilde V=0$; the positive definite form $H$ vanishes only on the zero value, while the determinant vanishes on the whole isotropic cone, with $e_1+ie_2$ a nonzero value of rank one. In the $4\times4$ model the block is the traceless part of $\operatorname{mat}_4(\tilde P)\operatorname{mat}_4(\tilde Q)^{\dagger}$, with trace zero and determinant $N(\tilde V)^2$, and rank four, two or zero on the same three cases; the form is the Hilbert–Schmidt pairing, $\tfrac12\operatorname{Tr}$ in the $2\times2$ model and $\tfrac14\operatorname{Tr}$ in the regular one, and the unique invariant form is the scalar-slot form $X_0\overline{Y_0}=\tfrac14\operatorname{Tr}\Phi(\tilde X)\overline{\operatorname{Tr}\Phi(\tilde Y)}$, degenerate on every value. The two-sided antisymmetrised operator $\tfrac12\bigl(\operatorname{mat}_4(\tilde P)\operatorname{mat}_4^{R}(\tilde Q^{*})-\operatorname{mat}_4(\tilde Q)\operatorname{mat}_4^{R}(\tilde P^{*})\bigr)$ is a different object: it is alternating, with trace $4i\,\mathrm{Im}(P_0\overline{Q_0})$ and generic rank four.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi$ | the $2\times2$ realization, $\Phi(e_0)=I$, $\Phi(e_k)=-i\sigma_k$, $\Phi(\tilde Q^{*})=\Phi(\tilde Q)^{\dagger}$ |
| $\operatorname{mat}_4$ | the left regular representation, $\operatorname{mat}_4(\tilde Q^*)=\operatorname{mat}_4(\tilde Q)^{\dagger}$, $\operatorname{Tr}\operatorname{mat}_4(\tilde Q)=4Q_0$ |
| $\operatorname{adj}$ | the adjoint matrix, the model of the natural conjugation, $\Phi(\tilde Q^{\natural})=\operatorname{adj}\Phi(\tilde Q)$ |
| $\Phi(\tilde P\diamond\tilde Q)=M-\tfrac12\operatorname{Tr}(M)I$ | the block in the $2\times2$ model, the traceless part |
| $\operatorname{mat}_4(\tilde P\diamond\tilde Q)=M-\tfrac14\operatorname{Tr}(M)I$ | the block in the regular model, the traceless part |
| $N(\tilde X)=\sum_\mu X_\mu^2$ | the complex bilinear norm, the determinant of the matrix |
| $\operatorname{Tr}=0$, rank $2/1/0$ | the invariants of the $2\times2$ value |
| $\operatorname{Tr}=0$, rank $4/2/0$ | the invariants of the $4\times4$ value |
| $H=\tfrac12\operatorname{Tr}\Phi(\cdot)\Phi(\cdot)^{\dagger}=\tfrac14\operatorname{Tr}\operatorname{mat}_4(\cdot)\operatorname{mat}_4(\cdot)^{\dagger}$ | the form as the Hilbert–Schmidt pairing |
| $X_0\overline{Y_0}$ | the unique invariant form, degenerate |
| $\tfrac12\bigl(\operatorname{mat}_4(\tilde P)\operatorname{mat}_4^{R}(\tilde Q^{*})-\operatorname{mat}_4(\tilde Q)\operatorname{mat}_4^{R}(\tilde P^{*})\bigr)$ | the two-sided antisymmetrised operator, alternating, trace $4i\,\mathrm{Im}(P_0\overline{Q_0})$ |

## Further Reading

- *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-sesqualgebra-of-biquaternions.md`), for the operation and its two conjugations
- *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-sesquilinear-pairing-of-the-antisymmetric-plain-sesqualgebra.md`), for the pairing, the trace form and the invariant forms computed here in the models
- *The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-adjoint-operators-and-the-sandwich-of-the-antisymmetric-plain-sesqualgebra.md`), for the operator whose invariants the models carry
- *The General Plain Sesqualgebra in the $2\times2$ Matrix Representation* (`articles_maths/the-general-plain-sesqualgebra-in-the-2x2-matrix-representation.md`) and *The General Plain Sesqualgebra in the $4\times4$ Matrix Representation* (`articles_maths/the-general-plain-sesqualgebra-in-the-4x4-matrix-representation.md`), for the product of the row and the form in the two models
- *Introduction to the 2×2 Matrix Representation of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-representation-of-biquaternions.md`) and *Introduction to the 4×4 Matrix Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_maths/introduction-to-the-4x4-matrix-representation-of-biquaternions.md`), for the realizations and their invariants
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the two forms, the norm, the zero divisors and the isotropic cone
- *Linear Maps and Matrices* (`articles_maths/linear-maps-and-matrices.md`), for the matrix of a linear map and its invariants
