# __The Singular Value Decomposition of a Reduced Biquaternion Tensor__

## Introduction

Every matrix has a singular value decomposition, and every third-order tensor has one under the t-product. This article proves the existence of the decomposition $A=U\ast S\ast V^{\mathsf H}$ for a reduced biquaternion tensor, gives the algorithm that computes it from the two complex idempotent coordinates, and records the norm identity that makes the decomposition useful for approximation. The middle factor $S$ is f-diagonal, and the two outer factors are $*$-unitary under the t-product.

The product is *The t-Product of Reduced Biquaternion Tensors*, and the tensor space is *Reduced Biquaternion Tensors as a Vector Space*. The matrix case is the singular value decomposition of *Least Squares and Total Least Squares over the Reduced Biquaternions*. The decomposition is used by *The Rank of a Reduced Biquaternion Tensor and its Low-Rank Approximation*, by *The Moore-Penrose Inverse of a Reduced Biquaternion Tensor* and by *Color Video Compression and Deblurring with Reduced Biquaternion Tensors*.

The source is Cui-E Yu, Xin Liu, Hui Luo and Yang Zhang, "Reduced biquaternion tensors and applications in color video processing", where the decomposition is called the Ht-SVD. The complex and real t-SVD it extends are those of Kilmer and Martin and of Qin, Ming and Zhang.

## The f-Diagonal and $*$-Unitary Tensors

A tensor $S\in\mathbb{B}_{\mathrm{r}}^{n_1\times n_2\times n_3}$ is **f-diagonal** if every frontal slice $S^{(k)}$ is a diagonal matrix. It need not be square: the diagonal has $\min(n_1,n_2)$ entries, and the entries off the diagonal are zero in every slice. The **diagonal tubes** are the vectors

$$
S(i,i,:)=(S(i,i,1),\dots,S(i,i,n_3)),\qquad 1\le i\le\min(n_1,n_2),
$$

each an element of $\mathbb{B}_{\mathrm{r}}^{n_3}$.

A tensor $U\in\mathbb{B}_{\mathrm{r}}^{n\times n\times n_3}$ is **$*$-unitary** if

$$
U^{\mathsf H}\ast U=U\ast U^{\mathsf H}=\mathrm I.
$$

The conjugate transpose is the bar-transpose with the reversal of the slices $2,\dots,n_3$ fixed in *The t-Product of Reduced Biquaternion Tensors*. By the transform criterion, $U$ is $*$-unitary if and only if every frontal slice $\widehat U^{(k)}$ is a $*$-unitary matrix over $\mathbb{B}_{\mathrm{r}}$, equivalently if and only if both complex matrices $\widehat U_{(1)}^{(k)}$ and $\widehat U_{(2)}^{(k)}$ are $*$-unitary for every $k$.

**Remark (the identity is f-diagonal).** The identity tensor $\mathrm I$ is f-diagonal and $*$-unitary: its first frontal slice is $I_n$, its other slices are zero, and its transform is $I_n$ in every slice.

## The Matrix Decomposition over the Reduced Biquaternions

The t-SVD is built from the matrix SVD over $\mathbb{B}_{\mathrm{r}}$. For a matrix $M\in\mathbb{B}_{\mathrm{r}}^{m\times n}$, write $M=M_{(1)}\Pi_++M_{(2)}\Pi_-$ with $M_{(1)},M_{(2)}\in\mathbb{C}^{m\times n}$, and take the complex singular value decompositions

$$
M_{(1)}=U_{(1)}\Sigma_{(1)}V_{(1)}^{\mathsf H_{\mathbb C}},\qquad
M_{(2)}=U_{(2)}\Sigma_{(2)}V_{(2)}^{\mathsf H_{\mathbb C}}.
$$

Set

$$
U=U_{(1)}\Pi_++U_{(2)}\Pi_-,\qquad
\Sigma=\Sigma_{(1)}\Pi_++\Sigma_{(2)}\Pi_-,\qquad
V=V_{(1)}\Pi_++V_{(2)}\Pi_-.
$$

Then

$$
M=U\Sigma V^{\mathsf H},
$$

the matrices $U$ and $V$ are $*$-unitary over $\mathbb{B}_{\mathrm{r}}$, and $\Sigma$ is diagonal with entries

$$
\sigma_i=\sigma_{i,(1)}\Pi_++\sigma_{i,(2)}\Pi_-,\qquad 1\le i\le\min(m,n),
$$

where $\sigma_{i,(j)}$ are the nonnegative complex singular values of $M_{(j)}$. The **singular values of $M$** are the elements $\sigma_i$; they are not real numbers in general, and they may be zero divisors when one complex coordinate vanishes and the other does not. The **rank** of $M$ is the larger of the two complex ranks of $M_{(1)}$ and $M_{(2)}$. In an SVD whose two coordinates are ordered with the nonzero values in the same initial positions, it is the number of indices $i$ for which $\sigma_i\neq0$.

*Proof.* The two complex decompositions hold by the matrix SVD. Multiplying by the orthogonal idempotents and using $\Pi_\pm^2=\Pi_\pm$ and $\Pi_+\Pi_-=0$ gives $M=U\Sigma V^{\mathsf H}$. The unitarity of $U$ and $V$ is coordinatewise, and $\Sigma$ is diagonal because each $\Sigma_{(j)}$ is diagonal.

**Remark (the singular values are pairs).** A singular value of a reduced biquaternion matrix is a pair of complex singular values, one in each idempotent coordinate. **The pair need not be ordered**, and the two coordinates may order their singular values differently. The rank counts a pair as nonzero when at least one of its two members is nonzero.

## The t-SVD

**Theorem (the t-SVD).** For every $A\in\mathbb{B}_{\mathrm{r}}^{n_1\times n_2\times n_3}$ there are $*$-unitary tensors $U\in\mathbb{B}_{\mathrm{r}}^{n_1\times n_1\times n_3}$ and $V\in\mathbb{B}_{\mathrm{r}}^{n_2\times n_2\times n_3}$ and an f-diagonal tensor $S\in\mathbb{B}_{\mathrm{r}}^{n_1\times n_2\times n_3}$ such that

$$
\boxed{\;
A=U\ast S\ast V^{\mathsf H}
\;}.
$$

*Proof.* Transform $A$ along the third mode. For each $k$, apply the matrix decomposition over $\mathbb{B}_{\mathrm{r}}$ to $\widehat A^{(k)}$:

$$
\widehat A^{(k)}=U_kS_kV_k^{\mathsf H},\qquad 1\le k\le n_3,
$$

with $U_k$ and $V_k$ $*$-unitary and $S_k$ diagonal. Define $\widehat U$, $\widehat S$ and $\widehat V$ by these slices, and let $U,S,V$ be their inverse transforms. By the transform criterion, $U$ and $V$ are $*$-unitary and $S$ is f-diagonal. By the product theorem of *The t-Product of Reduced Biquaternion Tensors*,

$$
\widehat{A}^{(k)}=\widehat U^{(k)}\widehat S^{(k)}(\widehat V^{(k)})^{\mathsf H},
$$

and inverting the transform gives $A=U\ast S\ast V^{\mathsf H}$.

The decomposition is the **t-SVD** of $A$. The source calls it the Ht-SVD and writes the conjugate transpose with a star; here the mark is $\mathsf H$, because the star of the algebra is the Hermitian conjugation of an element.

**Remark (existence does not give uniqueness).** The complex SVD of a matrix is unique up to the phases of the singular vectors when the singular values are simple, and it is not unique when they coincide. The t-SVD inherits both failures, and it has a third one: the two idempotent coordinates may order their singular values differently, so the pairing of the two coordinate values into an element $\sigma_i$ depends on the ordering chosen in each coordinate. **The decomposition exists for every tensor, and it is not unique.** The singular values of each transform slice are determined as multisets in each coordinate; the diagonal tubes depend on the pairing and on the ordering.

## The Algorithm

The proof is an algorithm. Write the two idempotent coordinates $A_{(1)}$ and $A_{(2)}$, which are complex tensors.

1. Compute $\widehat A_{(1)}=\mathcal F_3(A_{(1)})$ and $\widehat A_{(2)}=\mathcal F_3(A_{(2)})$ by the fast Fourier transform along the third mode, with $\mathcal F_3$ the transform of *The t-Product of Reduced Biquaternion Tensors*.
2. For each $k=1,\dots,n_3$, compute the complex SVDs
    $$
    \widehat A_{(1)}^{(k)}=U_{1,k}S_{1,k}V_{1,k}^{\mathsf H_{\mathbb C}},\qquad
    \widehat A_{(2)}^{(k)}=U_{2,k}S_{2,k}V_{2,k}^{\mathsf H_{\mathbb C}}.
    $$
3. Assemble the transform slices $\widehat U^{(k)}=U_{1,k}\Pi_++U_{2,k}\Pi_-$, $\widehat S^{(k)}=S_{1,k}\Pi_++S_{2,k}\Pi_-$, $\widehat V^{(k)}=V_{1,k}\Pi_++V_{2,k}\Pi_-$.
4. Apply the inverse transform to each of $\widehat U,\widehat S,\widehat V$.

The output is $U\in\mathbb{B}_{\mathrm{r}}^{n_1\times n_1\times n_3}$, $S\in\mathbb{B}_{\mathrm{r}}^{n_1\times n_2\times n_3}$ and $V\in\mathbb{B}_{\mathrm{r}}^{n_2\times n_2\times n_3}$, with $A=U\ast S\ast V^{\mathsf H}$. In practice the thin SVDs of the slices are computed and the factors are completed to $*$-unitary matrices by orthonormal bases of the orthogonal complements; the added columns carry zero singular values and do not change the product.

**The cost.** The two forward transforms cost $O(n_1n_2n_3\log n_3)$ and $O(n_1n_2n_3\log n_3)$; the $n_3$ slicewise complex SVDs cost $O(n_3\min(n_1^2n_2,n_1n_2^2))$; the inverse transforms cost $O(n_1^2n_3\log n_3+n_2^2n_3\log n_3)$. The dominant term is

$$
O\bigl(n_1n_2n_3\log n_3+n_3\min(n_1^2n_2,n_1n_2^2)\bigr),
$$

the expression of the source. The algorithm is embarrassingly parallel in the two idempotent coordinates and in the $n_3$ transform slices.

## The Norm Identity

**Theorem.** For every $A\in\mathbb{B}_{\mathrm{r}}^{n_1\times n_2\times n_3}$,

$$
\boxed{\;
\|A\|_{\mathrm F}=\frac1{\sqrt{n_3}}\|\operatorname{diag}(\widehat A)\|_{\mathrm F}
\;},
$$

where $\operatorname{diag}(\widehat A)$ is the block diagonal matrix with blocks $\widehat A^{(1)},\dots,\widehat A^{(n_3)}$.

*Proof.* The Frobenius norm of the block diagonal is the square root of the sum of the squared Frobenius norms of its blocks. The unnormalised Fourier transform along a mode of length $n_3$ satisfies the Parseval identity

$$
\sum_{k=1}^{n_3}\|\widehat A^{(k)}\|_{\mathrm F}^2=n_3\|A\|_{\mathrm F}^2,
$$

because each entry of $A$ is transformed by a vector of squared norm $n_3$ and the transforms of different entries are orthogonal in the sum. Dividing by $n_3$ and taking square roots gives the identity.

**Corollary.** For the t-SVD $A=U\ast S\ast V^{\mathsf H}$,

$$
\boxed{\;
\|A\|_{\mathrm F}=\|S\|_{\mathrm F}
\;}.
$$

*Proof.* In the transform, $\widehat A^{(k)}=\widehat U^{(k)}\widehat S^{(k)}(\widehat V^{(k)})^{\mathsf H}$, and the Frobenius norm is invariant under multiplication by the $*$-unitary matrices $\widehat U^{(k)}$ and $\widehat V^{(k)\mathsf H}$. Thus $\|\widehat A^{(k)}\|_{\mathrm F}=\|\widehat S^{(k)}\|_{\mathrm F}$ for every $k$; summing and using the theorem gives the identity.

**Remark (the singular value tubes).** The norm of the tensor is also the Euclidean norm of the diagonal tubes,

$$
\|A\|_{\mathrm F}^2=\sum_{i=1}^{\min(n_1,n_2)}\|S(i,i,:)\|_{\mathrm F}^2.
$$

The tubes are the objects the rank and the low-rank approximation read. **The decomposition concentrates the norm on the diagonal tubes**, and the truncation of the tubes is the approximation of the next article.

## Verification

The decomposition was recomputed on random tensors of sizes $2\times2\times2$, $3\times2\times4$ and $3\times3\times4$, with at most $36$ entries. The reconstruction $U\ast S\ast V^{\mathsf H}$ agreed with $A$ to $1.4\times10^{-15}$; the unitarity of $U$ and $V$ held to $5.6\times10^{-16}$; the norm identity of the theorem held to $1.3\times10^{-15}$; and the identity $\|A\|_{\mathrm F}=\|S\|_{\mathrm F}$ held to $1.1\times10^{-15}$. The singular values of each complex coordinate were the singular values returned by the complex SVD of the transform slices, and the idempotent reduction reproduced the decomposition coordinate by coordinate. Completing a thin SVD to $*$-unitary factors by orthonormal complements reproduced the slice to $7.5\times10^{-16}$.

## Summary

Every reduced biquaternion tensor $A\in\mathbb{B}_{\mathrm{r}}^{n_1\times n_2\times n_3}$ has a t-SVD $A=U\ast S\ast V^{\mathsf H}$, with $U$ and $V$ $*$-unitary and $S$ f-diagonal. The decomposition is computed by transforming along the third mode, taking the matrix SVD over $\mathbb{B}_{\mathrm{r}}$ of every transform slice, and inverting the transform. The singular values are pairs of complex singular values, one in each idempotent coordinate; they need not be real, they may be zero divisors, and the decomposition is not unique. The Frobenius norm satisfies $\|A\|_{\mathrm F}=n_3^{-1/2}\|\operatorname{diag}(\widehat A)\|_{\mathrm F}$ and equals $\|S\|_{\mathrm F}$, so the norm is concentrated on the diagonal tubes $S(i,i,:)$. **The t-SVD is the matrix SVD applied slice by slice in the Fourier domain, with the two idempotent coordinates taken separately.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A=U\ast S\ast V^{\mathsf H}$ | The t-SVD of $A$ |
| $S$ | The f-diagonal middle tensor |
| $S(i,i,:)$ | A diagonal tube of $S$ |
| $U,V$ | $*$-Unitary tensors, $U^{\mathsf H}\ast U=U\ast U^{\mathsf H}=\mathrm I$ |
| $\widehat A$ | The Fourier transform of $A$ along the third mode |
| $\operatorname{diag}(\widehat A)$ | The block diagonal matrix of the transform slices |
| $\sigma_i=\sigma_{i,(1)}\Pi_++\sigma_{i,(2)}\Pi_-$ | A singular value of a matrix over $\mathbb{B}_{\mathrm{r}}$ |

## Further Reading

- Cui-E Yu, Xin Liu, Hui Luo and Yang Zhang, "Reduced biquaternion tensors and applications in color video processing", arXiv:2403.01690 (2024). The Ht-SVD, its algorithm and its applications.
- Misha E. Kilmer and Carla D. Martin, "Factorization strategies for third-order tensors", *Linear Algebra and its Applications* **435** (2011) 641–658. The t-SVD over the reals and the norm identity.
- Z. Qin, Z. Ming and L. Zhang, "Singular value decomposition of third order quaternion tensors", *Applied Mathematics Letters* **123** (2022) 107597. The quaternion t-SVD and the slicewise transform.
- Soo-Chang Pei, Ja-Han Chang, Jian-Jiun Ding and Ming-Yang Chen, "Eigenvalues and singular value decompositions of reduced biquaternion matrices", *IEEE Transactions on Circuits and Systems I* **55** (2008) 2673–2685. The matrix decomposition over the reduced biquaternions.
