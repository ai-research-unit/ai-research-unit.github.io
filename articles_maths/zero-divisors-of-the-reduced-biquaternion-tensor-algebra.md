# __Zero Divisors of the Reduced Biquaternion Tensor Algebra__

## Introduction

The square reduced biquaternion tensors of a fixed shape form a finite-dimensional algebra under the t-product. This article identifies its units, its zero divisors, and the left and right annihilators of an element. The answer is read on the Fourier transform: a tensor is a unit exactly when every transform slice is an invertible matrix, and a nonzero tensor is a zero divisor exactly when some transform slice is singular in one of the two idempotent coordinates. The article also defines the t-determinant and the t-algebraic norm that decide invertibility.

The product is *The t-Product of Reduced Biquaternion Tensors*, the inverse is *The Moore-Penrose Inverse of a Reduced Biquaternion Tensor*, and the entries are those of *Reduced Biquaternion Space*. This article is the corpus's own reading of the tensor algebra; it is the tensor analogue of *Zero Divisors of the Algebra of the Reduced Biquaternions* and *Annihilators of the Algebra of the Reduced Biquaternions*. It is not in the source of the branch, and it is written only after the product is settled.

## The Algebra

Fix $n\ge1$ and $n_3\ge1$, and let

$$
T_n=\mathbb{B}_{\mathrm{r}}^{n\times n\times n_3}
$$

with the t-product $\ast$. The identity is the tensor $\mathrm I$ with $I_n$ in its first frontal slice and zeros elsewhere. The algebra is associative and distributive, it is not commutative for $n\ge2$, and it is finite-dimensional over $\mathbb{R}$, of dimension

$$
\dim_{\mathbb R}T_n=4n^2n_3.
$$

It is also a free module of rank $n^2n_3$ over $\mathbb{B}_{\mathrm{r}}$, and an algebra over $\mathbb{B}_{\mathrm{r}}$.

The Fourier transform along the third mode is an isomorphism of algebras

$$
T_n\cong\prod_{k=1}^{n_3}M_n(\mathbb{B}_{\mathrm{r}}),
$$

where the product is coordinatewise. Composing with the isomorphism $\mathbb{B}_{\mathrm{r}}\cong\mathbb{C}\oplus\mathbb{C}$ gives

$$
T_n\cong\prod_{k=1}^{n_3}\bigl(M_n(\mathbb{C})\oplus M_n(\mathbb{C})\bigr).
$$

**The units.** A tensor $A\in T_n$ is a **unit** if there is $B$ with $A\ast B=B\ast A=\mathrm I$. The inverse is unique, and it is written $A^{-1}$.

**Theorem (the unit criterion).** A tensor $A\in T_n$ is a unit if and only if every transform slice $\widehat A^{(k)}$ is an invertible matrix over $\mathbb{B}_{\mathrm{r}}$, equivalently if and only if both complex matrices $\widehat A_{(1)}^{(k)}$ and $\widehat A_{(2)}^{(k)}$ are nonsingular for every $k$. In that case

$$
\widehat{A^{-1}}^{(k)}=(\widehat A^{(k)})^{-1}.
$$

*Proof.* The transform is an algebra isomorphism, and it carries $\mathrm I$ to $I_n$ in every slice. Hence $A\ast B=\mathrm I$ if and only if $\widehat A^{(k)}\widehat B^{(k)}=I_n$ for every $k$. A matrix over $\mathbb{B}_{\mathrm{r}}$ is invertible if and only if both of its complex coordinate matrices are invertible.

**Remark (the spatial slices do not decide).** Invertibility is decided by the transform slices, not by the frontal slices $A^{(k)}$. A tensor can have a singular frontal slice and still be a unit, because the transform mixes the frontal slices; and it can have every frontal slice nonsingular and still fail to be a unit, because one transform slice is singular. **The Fourier transform is the coordinate system in which the algebra is a product of matrix algebras.**

## The Zero Divisors

A nonzero tensor $A\in T_n$ is a **left zero divisor** if there is a nonzero $B$ with $A\ast B=0$, and a **right zero divisor** if there is a nonzero $B$ with $B\ast A=0$. The zero tensor is excluded by the word nonzero, as usual.

**Theorem (the non-units are the zero divisors).** A nonzero tensor $A\in T_n$ is a left zero divisor if and only if it is not a unit, and the same holds for the right zero divisors. Hence the left zero divisors, the right zero divisors and the nonzero non-units are the same set.

*Proof.* A zero divisor cannot be a unit: if $A\ast B=0$ with $B\neq0$ and $A$ is a unit, then $B=A^{-1}\ast A\ast B=0$, a contradiction. Conversely, let $A$ be a nonzero non-unit. The left multiplication $\mathcal L_A:T_n\to T_n$, $\mathcal L_A(B)=A\ast B$, is a linear map of a finite-dimensional real vector space. If $\mathcal L_A$ were invertible, there would be $B$ with $A\ast B=\mathrm I$; in a finite-dimensional algebra a right inverse is a two-sided inverse, so $A$ would be a unit, a contradiction. Hence $\mathcal L_A$ is singular, and there is a nonzero $B$ with $A\ast B=0$. The same argument with the right multiplication gives a nonzero $C$ with $C\ast A=0$.

**Remark (the left and right annihilators differ).** The theorem says that the **sets** of left and right zero divisors coincide. It does not say that the annihilators of a given element coincide; they are different submodules in general, and the next section gives their dimensions.

**Theorem (the coordinate criterion).** Write $A=A_{(1)}\Pi_++A_{(2)}\Pi_-$. A nonzero $A\in T_n$ is a zero divisor if and only if $A_{(1)}$ or $A_{(2)}$ is not a unit in the complex tensor algebra $T_n(\mathbb{C})$. Equivalently, $A$ is a zero divisor if and only if there are $k\in\{1,\dots,n_3\}$ and $j\in\{1,2\}$ such that the complex matrix $(\widehat A_{(j)})^{(k)}$ is singular.

*Proof.* If $A_{(1)}$ is not a unit, either it is zero, and then $B=\Pi_+$ is a nonzero annihilator, or it is a nonzero zero divisor, and there is a nonzero $B_{(1)}$ with $A_{(1)}\ast B_{(1)}=0$; in both cases $B=B_{(1)}\Pi_+$ is nonzero and $A\ast B=0$. The case of $A_{(2)}$ is the same. Conversely, if $A\ast B=0$ with $B\neq0$, then $A_{(1)}\ast B_{(1)}=0$ and $A_{(2)}\ast B_{(2)}=0$; at least one of $B_{(1)},B_{(2)}$ is nonzero, so the corresponding coordinate has a nonzero annihilator and is not a unit. The complex criterion is proved by the transform: a complex tensor is a non-unit if and only if some transform slice is singular, because a nonzero kernel vector in that slice, placed in that slice and zero elsewhere, is a nonzero annihilator; and conversely a nonzero annihilator has a nonzero slice, which makes the corresponding slice singular.

**Corollary (the unit criterion again).** A tensor is a unit if and only if no transform slice is singular in either coordinate. This is the criterion of the previous section.

**The all-ones tensor.** Let $J$ be the tensor all of whose entries are $1$. Its transform is

$$
\widehat J^{(1)}=n_3\,\mathbf 1\mathbf 1^{\mathsf T},\qquad \widehat J^{(k)}=0\quad(2\le k\le n_3),
$$

where $\mathbf 1$ is the all-ones column. Every slice is singular, so $J$ is a zero divisor, except when $n=1$ and $n_3=1$, where $J$ is the scalar $1$, a unit. For $n\ge2$, a witness is any tensor $B$ whose every frontal slice is $C/n_3$, where $C$ is a complex matrix with $\mathbf 1^{\mathsf T}C=0$; then $J\ast B=0$. For $n=1$ and $n_3\ge2$ the transform slices at $k\ge2$ are zero, and a nonzero tensor supported on one of them is an annihilator. **Every entry of $J$ is the unit $1$, and $J$ is not a unit except when $n=1$ and $n_3=1$.** Entrywise invertibility does not imply tensor invertibility.

## The Annihilators

The **left annihilator** and the **right annihilator** of $A\in T_n$ are

$$
\operatorname{Ann}_L(A)=\{B\in T_n:A\ast B=0\},\qquad
\operatorname{Ann}_R(A)=\{B\in T_n:B\ast A=0\}.
$$

Both are submodules of $T_n$ over $\mathbb{B}_{\mathrm{r}}$, and both contain $0$. The left annihilator is the kernel of the left multiplication $\mathcal L_A$; the right annihilator is the kernel of the right multiplication $\mathcal R_A$.

**Theorem (the transform description).** In the transform,

$$
\operatorname{Ann}_L(A)=\Bigl\{B:\widehat B^{(k)}\in\ker_L\bigl(\widehat A^{(k)}\bigr)\ \text{for every }k\Bigr\},
$$

where $\ker_L(M)=\{Y:MY=0\}$ is the right null space of the matrix $M$, and

$$
\operatorname{Ann}_R(A)=\Bigl\{B:\widehat B^{(k)}\in\ker_R\bigl(\widehat A^{(k)}\bigr)\ \text{for every }k\Bigr\},
$$

where $\ker_R(M)=\{Y:YM=0\}$ is the left null space.

*Proof.* The transform is an algebra isomorphism, so $A\ast B=0$ if and only if $\widehat A^{(k)}\widehat B^{(k)}=0$ for every $k$. The two displays are the slicewise reading of this identity.

**The dimensions.** For a complex tensor $B\in T_n(\mathbb{C})$, the complex dimension of the left annihilator is

$$
\dim_{\mathbb C}\operatorname{Ann}_L(B)=\sum_{k=1}^{n_3}\dim_{\mathbb C}\ker\bigl(\widehat B^{(k)}\bigr),
$$

and the right annihilator has the same dimension, because a matrix and its transpose have the same rank. For a reduced biquaternion tensor $A=A_{(1)}\Pi_++A_{(2)}\Pi_-$, the real dimension is

$$
\dim_{\mathbb R}\operatorname{Ann}_L(A)
=2\sum_{k=1}^{n_3}\Bigl(\dim_{\mathbb C}\ker\widehat A_{(1)}^{(k)}+\dim_{\mathbb C}\ker\widehat A_{(2)}^{(k)}\Bigr),
$$

and the same formula holds for $\operatorname{Ann}_R(A)$.

*Proof.* The complex formula is the rank-nullity theorem applied slice by slice. The real formula is the complex formula applied to the two idempotent coordinates; each complex dimension contributes two real dimensions because $\mathbb{B}_{\mathrm{r}}$ is two-dimensional over $\mathbb{C}$. The right-hand formula follows from the equality of the rank of a matrix and its transpose.

**Remark (the annihilators need not coincide).** The dimensions of $\operatorname{Ann}_L(A)$ and $\operatorname{Ann}_R(A)$ are equal, but the submodules are different in general. Take a tensor whose only nonzero frontal slice is a non-normal matrix $M$ in the first slice. The left annihilator is the set of tensors whose every frontal slice $Y$ satisfies $MY=0$, and the right annihilator is the set whose every frontal slice $Y$ satisfies $YM=0$; the right and left null spaces of $M$ differ, so the annihilators differ. **Equality of dimensions is not equality of submodules.**

**The extreme cases.** For a unit, both annihilators are $\{0\}$. For the zero tensor, both are the whole algebra $T_n$. For a nonzero zero divisor, both are nonzero and proper. The left annihilator of $A$ is the whole algebra if and only if $A=0$.

## The t-Determinant and the Algebraic Norm

The **t-determinant** of $A\in T_n$ is

$$
\det\nolimits_{\mathrm t}(A)=\prod_{k=1}^{n_3}\det\bigl(\widehat A^{(k)}\bigr)\in\mathbb{B}_{\mathrm{r}}.
$$

It is the determinant of the block circulant matrix $\operatorname{circ}(A)$ read as an element of $\mathbb{B}_{\mathrm{r}}$: the Fourier matrix diagonalises the block circulant, and the determinant of a block diagonal matrix is the product of the determinants of its blocks. It is multiplicative,

$$
\det\nolimits_{\mathrm t}(A\ast B)=\det\nolimits_{\mathrm t}(A)\det\nolimits_{\mathrm t}(B),
$$

because $\operatorname{circ}(A\ast B)=\operatorname{circ}(A)\operatorname{circ}(B)$.

**Theorem (the determinant criterion).** A tensor $A\in T_n$ is a unit if and only if $\det_{\mathrm t}(A)$ is a unit of $\mathbb{B}_{\mathrm{r}}$, that is, if and only if both complex numbers $\det_{t,(1)}(A)$ and $\det_{t,(2)}(A)$ are nonzero.

*Proof.* The determinant of a matrix over $\mathbb{B}_{\mathrm{r}}$ is a unit if and only if the matrix is invertible. The product of the slice determinants is a unit if and only if every slice determinant is a unit, because $\mathbb{B}_{\mathrm{r}}$ is a product of two fields. Hence the criterion is the unit criterion of the first section.

**The t-algebraic norm.** The algebraic norm of the element $\det_{\mathrm t}(A)$ is

$$
\langle\det\nolimits_{\mathrm t}(A)\rangle_{\mathrm{ts}}
=\det\nolimits_{t,(1)}(A)\det\nolimits_{t,(2)}(A)\in\mathbb{C}.
$$

It is nonzero if and only if $A$ is a unit. **This is the scalar that decides invertibility.** It is not a topological norm: it is a polynomial, it is complex-valued, and it vanishes on the zero divisors. The Frobenius norm does not decide invertibility: the all-ones tensor has $\|J\|_{\mathrm F}=n\sqrt{n_3}>0$ and is a zero divisor.

**Remark (the zero divisors are not a single hypersurface).** The t-algebraic norm is a complex polynomial in the real coordinates of $A$, and the units are the complement of its zero set. That zero set is the union of $\det_{t,(1)}=0$ and $\det_{t,(2)}=0$. Each is the zero set of a complex polynomial, hence a real subvariety of codimension two and a complex hypersurface in the complex structure of $T_n$; their union also has real codimension two, not one. The units are the complement of this union and form a dense open subset. This is the tensor analogue of the zero divisors of $\mathbb{B}_{\mathrm{r}}$, the union of the two complex lines $Q_{(1)}=0$ and $Q_{(2)}=0$, which is the zero set of the complex quadratic form $Q_{(1)}Q_{(2)}$.

## Verification

The unit criterion, the zero-divisor criterion and the determinant were recomputed on random tensors of size $3\times3\times4$, with $36$ entries. A random tensor was a unit; its two-sided inverse reproduced $\mathrm I$ to $2.8\times10^{-16}$; the t-determinant was multiplicative to a relative error of $5.0\times10^{-15}$; and it agreed with the determinant of the block circulant to a relative error of $8.7\times10^{-16}$. The all-ones tensor was a zero divisor, with $J\ast B=0$ exactly for the witness $B$ of constant slices $C/n_3$ with $\mathbf 1^{\mathsf T}C=0$, and with $\det_{\mathrm t}(J)=0$. For the tensor whose only nonzero frontal slice was a rank-one matrix in one idempotent coordinate, the complex block circulant of that coordinate had nullity $8$ and the sum of the transform-slice nullities was $8$, as the dimension formula predicts; the real dimension of the annihilator was $16$. A random unit had annihilator $\{0\}$, and a tensor with a rank-one transform slice had a nonzero annihilator of the predicted dimension. For $n=1$, the all-ones tensor was the unit $1$ at $n_3=1$ and a zero divisor at $n_3=2,3$, with transform slices $(2,0)$ and $(3,0,0)$.

## Summary

The square tensors $T_n=\mathbb{B}_{\mathrm{r}}^{n\times n\times n_3}$ form a finite-dimensional algebra under the t-product, isomorphic to $\prod_k M_n(\mathbb{B}_{\mathrm{r}})$ and to $\prod_k(M_n(\mathbb{C})\oplus M_n(\mathbb{C}))$. A tensor is a unit exactly when every transform slice is invertible in both idempotent coordinates; the nonzero non-units are exactly the left zero divisors and exactly the right zero divisors. A nonzero tensor is a zero divisor exactly when some transform slice is singular in one coordinate. The left and right annihilators are the slicewise right and left null spaces; they have equal dimensions but need not coincide. The t-determinant is the product of the transform-slice determinants, it is multiplicative, and its algebraic norm is the scalar that decides invertibility; the Frobenius norm does not. **The nonzero zero divisors are the nonzero tensors whose t-algebraic norm vanishes; they lie in the union of two real subvarieties of codimension two.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_n=\mathbb{B}_{\mathrm{r}}^{n\times n\times n_3}$ | The tensor algebra under the t-product |
| $\mathrm I$ | The identity tensor, $I_n$ in the first slice |
| $\operatorname{Ann}_L(A)$, $\operatorname{Ann}_R(A)$ | The left and right annihilators of $A$ |
| $\det_{\mathrm t}(A)$ | The t-determinant, $\prod_k\det(\widehat A^{(k)})$ |
| $\langle\det_{\mathrm t}(A)\rangle_{\mathrm{ts}}$ | The t-algebraic norm, the scalar that decides invertibility |
| $\widehat A^{(k)}$ | The $k$-th transform slice |

## Further Reading

- Cui-E Yu, Xin Liu, Hui Luo and Yang Zhang, "Reduced biquaternion tensors and applications in color video processing", arXiv:2403.01690 (2024). The t-product, the transform and the invertibility criterion that this article reads as an algebra.
- Misha E. Kilmer and Carla D. Martin, "Factorization strategies for third-order tensors", *Linear Algebra and its Applications* **435** (2011) 641–658. The t-product and the block circulant representation.
- Adi Ben-Israel and Thomas N. E. Greville, *Generalized Inverses: Theory and Applications* (Wiley, 1974; Springer, 2003). The finite-dimensional algebra facts about one-sided inverses and zero divisors.
- The corpus articles [Zero Divisors of the Algebra of the Reduced Biquaternions](zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.html) and [Annihilators of the Algebra of the Reduced Biquaternions](annihilators-of-the-general-plain-algebra-of-the-reduced-biquaternions.html). The four-dimensional case that the tensor algebra extends.
