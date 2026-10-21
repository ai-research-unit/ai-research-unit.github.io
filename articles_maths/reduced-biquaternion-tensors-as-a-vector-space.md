# __Reduced Biquaternion Tensors as a Vector Space__

## Introduction

A reduced biquaternion tensor is a rectangular array of reduced biquaternions indexed by three modes. This article fixes the set of such arrays, its slices, its four real coefficient tensors, its two complex readings, its module structure, its transpose and conjugate transpose, and its norms. It is the first article of the tensor branch: no product of tensors is defined here.

The algebra of the entries is *Reduced Biquaternion Space*, and the notation is *Conventions in Mathematics*. The Einstein product is *The Einstein Product of Reduced Biquaternion Tensors*; the t-product, which uses the conjugate transpose fixed here together with a reversal of the frontal slices, is *The t-Product of Reduced Biquaternion Tensors*. The matrix case, in which the third mode has length one, is the matrix theory of *Least Squares and Total Least Squares over the Reduced Biquaternions*.

## The Set of Tensors

Let $n_1,n_2,n_3$ be positive integers. A **third-order reduced biquaternion tensor** is an array

$$
A=(a_{i_1i_2i_3}),\qquad 1\le i_1\le n_1,\quad 1\le i_2\le n_2,\quad 1\le i_3\le n_3,
$$

with entries $a_{i_1i_2i_3}\in\mathbb{B}_{\mathrm r}$. The set of these arrays is written $\mathbb{B}_{\mathrm r}^{n_1\times n_2\times n_3}$. The **order** is three and is carried by the type; the three **modes** have lengths $n_1,n_2,n_3$. The **horizontal**, **lateral** and **frontal** slices are

$$
A(i,:,:),\qquad A(:,j,:),\qquad A(:,:,k),
$$

and the frontal slice $A(:,:,k)$ is written $A^{(k)}$. A frontal slice is an $n_1\times n_2$ matrix over $\mathbb{B}_{\mathrm r}$; the tensor is the stack of its $n_3$ frontal slices.

Each entry has a real four-coordinate form and two complex forms. With the basis $1,i,j,ij$ of *Reduced Biquaternion Space*,

$$
a_{i_1i_2i_3}=a_{0,i_1i_2i_3}+a_{1,i_1i_2i_3}i+a_{2,i_1i_2i_3}j+a_{3,i_1i_2i_3}ij,
$$

with real coefficients. Collecting the coefficients gives four real tensors $A_0,A_1,A_2,A_3$ of the same shape,

$$
A=A_0+A_1i+A_2j+A_3ij.
$$

The split into a complex part and a hyperbolic part is

$$
A=A_{1,i}+jA_{j,k},\qquad A_{1,i}=A_0+A_1i,\qquad A_{j,k}=A_2+A_3i,
$$

where $A_{1,i}$ and $A_{j,k}$ are complex tensors. The subscripts $1,i$ and $j,k$ name the units that build the two complex tensors; they are the notation of the source and are kept here. The idempotent form is

$$
A=A_{(1)}\Pi_++A_{(2)}\Pi_-,\qquad \Pi_\pm=\tfrac12(1\pm j),
$$

with

$$
A_{(1)}=A_{1,i}+A_{j,k}=A_0+A_2+i(A_1+A_3),\qquad
A_{(2)}=A_{1,i}-A_{j,k}=A_0-A_2+i(A_1-A_3).
$$

The two complex tensors $A_{(1)}$ and $A_{(2)}$ are the **idempotent coordinates** of $A$. They are the components written $X^+$ and $X^-$ in *Least Squares and Total Least Squares over the Reduced Biquaternions*, and they satisfy $\Pi_+\Pi_-=0$, $\Pi_\pm^2=\Pi_\pm$, $\Pi_++\Pi_-=1$. The element convention of *Conventions in Mathematics* writes the idempotent coordinates with the sign, $Q_{+},Q_{-}$; the tensor branch keeps the parentheses $A_{(1)},A_{(2)}$ and the signs $+,-$ for the idempotents $\Pi_\pm$. The two notations name the same two complex tensors, and the parentheses avoid a collision with the entry indices.

**Proposition (the two complex readings).** The map $A\mapsto(A_{(1)},A_{(2)})$ is a bijection from $\mathbb{B}_{\mathrm r}^{n_1\times n_2\times n_3}$ onto the pairs of complex tensors of the same shape. Its inverse is

$$
A_{1,i}=\tfrac12(A_{(1)}+A_{(2)}),\qquad A_{j,k}=\tfrac12(A_{(1)}-A_{(2)}),
$$

and the real coefficients are recovered by

$$
A_0=\tfrac14(A_{(1)}+A_{(2)}+A_{(1)}^{\mathbb C}+A_{(2)}^{\mathbb C}),\qquad
A_2=\tfrac14(A_{(1)}-A_{(2)}+A_{(1)}^{\mathbb C}-A_{(2)}^{\mathbb C}),
$$

$$
A_1=\tfrac1{4i}(A_{(1)}+A_{(2)}-A_{(1)}^{\mathbb C}-A_{(2)}^{\mathbb C}),\qquad
A_3=\tfrac1{4i}(A_{(1)}-A_{(2)}-A_{(1)}^{\mathbb C}+A_{(2)}^{\mathbb C}),
$$

where $A_{(j)}^{\mathbb C}$ is the entrywise complex conjugate of $A_{(j)}$.

*Proof.* The idempotents $\Pi_+$ and $\Pi_-$ are orthogonal and sum to $1$, so $A\Pi_+=A_{(1)}\Pi_+$ and $A\Pi_-=A_{(2)}\Pi_-$. The formulas for $A_{1,i}$ and $A_{j,k}$ follow by adding and subtracting. The real formulas follow from $A_{1,i}=A_0+A_1i$ and $A_{j,k}=A_2+A_3i$, using that $A_0,A_1,A_2,A_3$ are real.

**Remark (the coordinates are independent).** A tensor is zero if and only if both $A_{(1)}$ and $A_{(2)}$ are zero. The two coordinates carry the same amount of information as the four real tensors, and no relation between them is imposed by the algebra: every pair of complex tensors of the given shape occurs. **The two coordinates are independent**; the product later acts on them separately, and the zero divisors later are exactly the nonzero tensors with one coordinate a non-unit.

Addition and scalar multiplication are entrywise:

$$
(A+B)_{i_1i_2i_3}=a_{i_1i_2i_3}+b_{i_1i_2i_3},\qquad (cA)_{i_1i_2i_3}=c\,a_{i_1i_2i_3},
$$

for $c\in\mathbb{B}_{\mathrm r}$. With these operations $\mathbb{B}_{\mathrm r}^{n_1\times n_2\times n_3}$ is a **free left module of rank $n_1n_2n_3$** over $\mathbb{B}_{\mathrm r}$, and also a free right module of the same rank because the algebra is commutative. Its real dimension is $4n_1n_2n_3$; its complex dimension is $2n_1n_2n_3$.

A real basis is given by the arrays $E_{i_1i_2i_3}$, $iE_{i_1i_2i_3}$, $jE_{i_1i_2i_3}$, $ijE_{i_1i_2i_3}$, where $E_{i_1i_2i_3}$ has entry $1$ at $(i_1,i_2,i_3)$ and $0$ elsewhere. A complex basis is given by $E_{i_1i_2i_3}$ and $jE_{i_1i_2i_3}$, because $\mathbb{B}_{\mathrm r}$ is two-dimensional over $\mathbb{C}$ with basis $1,j$. The module is finite-dimensional over $\mathbb{R}$ and over $\mathbb{C}$, hence complete in the Frobenius norm below.

**Remark (the matrix case).** For $n_3=1$ the tensor is an $n_1\times n_2$ matrix over $\mathbb{B}_{\mathrm r}$, and the frontal slice is the matrix itself. For $n_3\ge2$ the tensor is not a matrix: the $n_3$ frontal slices are matrices, and the product later couples them by a circular convolution. **The third mode is a mode of its own**, not a bookkeeping index for a family of matrices.

## The Transpose and the Conjugate Transpose

The **frontal transpose** $A^{\mathsf T}$ is defined slicewise by

$$
(A^{\mathsf T})^{(k)}=(A^{(k)})^{\mathsf T},\qquad 1\le k\le n_3,
$$

that is, $(A^{\mathsf T})_{i_2i_1i_3}=a_{i_1i_2i_3}$. It transposes the first two modes and leaves the third mode in place. It is an involution, $(A^{\mathsf T})^{\mathsf T}=A$, and it is $\mathbb{B}_{\mathrm r}$-linear.

The **conjugate transpose** $A^{\mathsf H}$ is the tensor reading of the bar conjugation and the frontal transpose, with the order of the frontal slices $2,\dots,n_3$ reversed:

$$
(A^{\mathsf H})^{(1)}=(A^{(1)})^{\mathsf H},\qquad
(A^{\mathsf H})^{(k)}=(A^{(n_3+2-k)})^{\mathsf H}\quad(2\le k\le n_3),
$$

where for a matrix $X$ over $\mathbb{B}_{\mathrm r}$ the **bar-transpose** is $X^{\mathsf H}=\bar X^{\mathsf T}$, with the bar acting entrywise. In the two idempotent coordinates it is the pair of the complex conjugate transposes, $X^{\mathsf H}=X_{(1)}^{\mathsf H_{\mathbb C}}\Pi_++X_{(2)}^{\mathsf H_{\mathbb C}}\Pi_-$. The reversal is the convention that makes $A^{\mathsf H}$ the adjoint of the t-product; without it the transform identity of *The t-Product of Reduced Biquaternion Tensors* fails. For $n_3=1$ the reversal is empty and $A^{\mathsf H}$ is the matrix conjugate transpose. The source writes this operation $A^{*}$; the corpus writes $A^{\mathsf H}$ here, because the star $^{*}$ of *Conventions in Mathematics* is the Hermitian conjugation of an element, not the bar. On an entry the conjugate transpose acts by the bar, $a\mapsto\bar a$, not by the star.

**Proposition.** The conjugate transpose is an involution and is bar-antilinear:

$$
(A^{\mathsf H})^{\mathsf H}=A,\qquad (aA+bB)^{\mathsf H}=\bar a\,A^{\mathsf H}+\bar b\,B^{\mathsf H},
$$

for $a,b\in\mathbb{B}_{\mathrm r}$.

*Proof.* The bar is an involution and the reversal of the slices $2,\dots,n_3$ is an involution, so applying $A^{\mathsf H}$ twice returns $A$. The bar is additive and $\overline{ab}=\bar a\bar b$; the reversal and the transpose are linear over the coefficients, so the second identity follows.

**Proposition (the transform of the conjugate transpose).** For every $k$,

$$
\widehat{A^{\mathsf H}}^{(k)}=(\widehat A^{(k)})^{\mathsf H}.
$$

*Proof.* The $k$-th transform slice is $\sum_{t=1}^{n_3}\omega^{(k-1)(t-1)}(A^{\mathsf H})^{(t)}$, with $\omega=e^{-2\pi i/n_3}$. The first term is $(A^{(1)})^{\mathsf H}$. In the sum over $t\ge2$ put $s=n_3+2-t$, so that $(A^{\mathsf H})^{(t)}=(A^{(s)})^{\mathsf H}$ and $\omega^{(k-1)(t-1)}=\omega^{-(k-1)(s-1)}$. The sum becomes $\sum_{s=2}^{n_3}\omega^{-(k-1)(s-1)}(A^{(s)})^{\mathsf H}$, which together with the first term is $\bigl(\sum_{s=1}^{n_3}\omega^{(k-1)(s-1)}A^{(s)}\bigr)^{\mathsf H}=(\widehat A^{(k)})^{\mathsf H}$.

The two operations are distinct for $n_3\ge3$. For $n_3=2$ the reversal of the slices $2,\dots,n_3$ is the identity on the second slice, so $A^{\mathsf H}$ is the slicewise conjugate transpose. The frontal transpose and the conjugate transpose agree on real tensors only when $n_3\le2$.

**Remark (the conjugate transpose is not the star).** The star of the algebra is $a^{*}=\bar a^{\natural}$; the conjugate transpose of the tensor uses the bar alone. The two coincide on a real scalar but not on a general reduced biquaternion. **The tensor adjoint of the t-product is the bar-transpose**, and the star is used in this branch only when the Hermitian conjugation of an element is meant.

## The Norms

The **Frobenius norm** of a tensor is

$$
\|A\|_{\mathrm F}^2=\sum_{i_1=1}^{n_1}\sum_{i_2=1}^{n_2}\sum_{i_3=1}^{n_3}|a_{i_1i_2i_3}|^2,
\qquad |a|^2=a_0^2+a_1^2+a_2^2+a_3^2.
$$

It is the Euclidean norm of the $4n_1n_2n_3$ real coordinates, and it is positive definite. In terms of the real coefficient tensors and of the two complex readings,

$$
\|A\|_{\mathrm F}^2=\|A_0\|_{\mathrm F}^2+\|A_1\|_{\mathrm F}^2+\|A_2\|_{\mathrm F}^2+\|A_3\|_{\mathrm F}^2
=\tfrac12\bigl(\|A_{(1)}\|_{\mathrm F}^2+\|A_{(2)}\|_{\mathrm F}^2\bigr).
$$

The second identity uses $|a|^2=\tfrac12(|a_{(1)}|^2+|a_{(2)}|^2)$, which follows from the definitions of $a_{(1)}$ and $a_{(2)}$.

The algebra carries four algebraic norms, and each has a tensor reading obtained by summing the norm of the entries. With the notation of *Conventions in Mathematics*,

$$
\langle A\rangle=\sum_{i_1i_2i_3}\langle a_{i_1i_2i_3}\rangle,\qquad
\langle A\rangle_\natural=\sum_{i_1i_2i_3}\langle a_{i_1i_2i_3}\rangle_\natural,\qquad
\langle A\rangle_*=\sum_{i_1i_2i_3}\langle a_{i_1i_2i_3}\rangle_*,\qquad
\langle A\rangle_{\natural*}=\sum_{i_1i_2i_3}\langle a_{i_1i_2i_3}\rangle_{\natural*}.
$$

In the idempotent coordinates the four sums are

$$
\langle A\rangle=\tfrac12\sum\bigl(a_{(1)}^2+a_{(2)}^2\bigr),\qquad
\langle A\rangle_\natural=\sum a_{(1)}a_{(2)},
$$

$$
\langle A\rangle_*=\sum\operatorname{Re}\bigl(a_{(1)}\overline{a_{(2)}}\bigr),\qquad
\langle A\rangle_{\natural*}=\tfrac12\sum\bigl(|a_{(1)}|^2+|a_{(2)}|^2\bigr)=\|A\|_{\mathrm F}^2.
$$

The first sum is complex, the second is complex, the third is real, and the fourth is the square of the Frobenius norm. **Only the fourth is positive definite.** The quaternionic sum vanishes on the tensors with one idempotent coordinate zero, the plain sum vanishes on some nonzero tensors, and the Hermitian sum is indefinite; none of the first three is a norm in the topological sense. The fourth is the Frobenius norm squared, and it is the norm used throughout the branch.

**Remark (the algebraic norms are not multiplicative).** The four sums are additive over the entries but not multiplicative under any of the tensor products of the branch. The Frobenius norm is submultiplicative for the Einstein product, and for the t-product up to a constant that depends on the shape; the algebraic sums are not. **The algebraic norms describe the algebra of the entries, not the metric of the tensor space.**

## Verification

The identities of this article were recomputed on random tensors of sizes $2\times2\times2$, $3\times2\times3$ and $3\times3\times2$, with at most $54$ entries. The four-coordinate form and the two idempotent coordinates agreed to $2.8\times10^{-16}$; the inverse formulas of the two complex readings agreed to $2.2\times10^{-16}$; the Frobenius norm agreed with the sum of the four real coefficient norms and with the half-sum of the two complex coordinate norms to $7.1\times10^{-15}$; the four algebraic norm sums agreed with their idempotent formulas to $7.1\times10^{-15}$; the frontal transpose and the conjugate transpose were involutions exactly; the transform of the conjugate transpose agreed with the slicewise bar-transpose exactly, for $n_3=2,3,5$; and the bar-antilinearity of the conjugate transpose held exactly.

## Summary

A third-order reduced biquaternion tensor is an array $A\in\mathbb{B}_{\mathrm r}^{n_1\times n_2\times n_3}$. It has four real coefficient tensors $A_0,A_1,A_2,A_3$, two complex tensors $A_{1,i}=A_0+A_1i$ and $A_{j,k}=A_2+A_3i$, and two idempotent coordinates $A_{(1)}=A_{1,i}+A_{j,k}$ and $A_{(2)}=A_{1,i}-A_{j,k}$, with $A=A_{(1)}\Pi_++A_{(2)}\Pi_-$. The set is a free module of rank $n_1n_2n_3$ over $\mathbb{B}_{\mathrm r}$, of real dimension $4n_1n_2n_3$ and complex dimension $2n_1n_2n_3$. The frontal transpose transposes the first two modes; the conjugate transpose also conjugates the entries and reverses the slices $2,\dots,n_3$, and it is the adjoint used by the t-product. The Frobenius norm is the Euclidean norm of the real coordinates and equals the square root of the Krein algebraic norm; the plain, quaternionic and Hermitian algebraic sums are not positive definite. **The two complex readings are independent, and the Frobenius norm is the metric of the branch.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}_{\mathrm r}$ | The reduced biquaternions, $\mathbb{C}\otimes_{\mathbb R}\mathbb{C}$ |
| $A\in\mathbb{B}_{\mathrm r}^{n_1\times n_2\times n_3}$ | A third-order reduced biquaternion tensor |
| $A^{(k)}$ | The $k$-th frontal slice $A(:,:,k)$, an $n_1\times n_2$ matrix |
| $A_0,A_1,A_2,A_3$ | The four real coefficient tensors, $A=A_0+A_1i+A_2j+A_3ij$ |
| $A_{1,i},A_{j,k}$ | The complex tensors $A_0+A_1i$ and $A_2+A_3i$ |
| $A_{(1)},A_{(2)}$ | The idempotent coordinates, $A=A_{(1)}\Pi_++A_{(2)}\Pi_-$ |
| $\Pi_+,\Pi_-$ | The idempotents $\tfrac12(1\pm j)$ |
| $A^{\mathsf T}$ | The frontal transpose, $(A^{\mathsf T})^{(k)}=(A^{(k)})^{\mathsf T}$ |
| $A^{\mathsf H}$ | The conjugate transpose, with the slices $2,\dots,n_3$ reversed |
| $\|A\|_{\mathrm F}$ | The Frobenius norm, the Euclidean norm of the real coordinates |
| $\langle A\rangle,\langle A\rangle_\natural,\langle A\rangle_*,\langle A\rangle_{\natural*}$ | The four algebraic norm sums of the entries |

## Further Reading

- Ting-Ting Liu and Shao-Wen Yu, "Some properties of reduced biquaternion tensors", *Symmetry* **16** (2024) 1260. The real and complex representations, the Einstein product and the slices of a reduced biquaternion tensor.
- Soo-Chang Pei, Ja-Han Chang, Jian-Jiun Ding and Ming-Yang Chen, "Eigenvalues and singular value decompositions of reduced biquaternion matrices", *IEEE Transactions on Circuits and Systems I* **55** (2008) 2673–2685. The matrix case and the two idempotent coordinates.
- Tamara G. Kolda and Brett W. Bader, "Tensor decompositions and applications", *SIAM Review* **51** (2009) 455–500. The vocabulary of modes, slices and tensor operations.
- Misha E. Kilmer and Carla D. Martin, "Factorization strategies for third-order tensors", *Linear Algebra and its Applications* **435** (2011) 641–658. The third-order tensor operations and the transform along the third mode that the t-product uses.
