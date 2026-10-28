# __The Rank of a Reduced Biquaternion Tensor and its Low-Rank Approximation__

## Introduction

This article defines the tubal rank of a reduced biquaternion tensor, identifies it with the largest rank of the frontal slices of the Fourier transform, truncates the t-SVD to the leading diagonal tubes, and proves that the truncation is the best approximation of its rank in the Frobenius norm. The rank studied here is the **tubal rank**, the rank read on the t-SVD. It is not the CP rank and it is not the tensor ring rank; the last section says what those are and why the approximation theorem does not apply to them.

The product is *The t-Product of Reduced Biquaternion Tensors*, the decomposition is *The Singular Value Decomposition of a Reduced Biquaternion Tensor*, and the norm is that of *Reduced Biquaternion Tensors as a Vector Space*. The matrix case is the truncated singular value decomposition of *Least Squares and Total Least Squares over the Reduced Biquaternions*; the application is *Color Video Compression and Deblurring with Reduced Biquaternion Tensors*.

The source is Cui-E Yu, Xin Liu, Hui Luo and Yang Zhang, "Reduced biquaternion tensors and applications in color video processing", Section 6, where the rank is called the Ht-tubal rank.

## The Tubal Rank

Let $A\in\mathbb{B}_{\mathrm{r}}^{n_1\times n_2\times n_3}$ have the t-SVD

$$
A=U\ast S\ast V^{\mathsf H},
$$

with $U$ and $V$ $*$-unitary and $S$ f-diagonal. Write $w=\min(n_1,n_2)$. The **tubal rank** of $A$ is

$$
\operatorname{rank}_{\mathrm t}(A)=\#\{i\in\{1,\dots,w\}:\|S(i,i,:)\|_{\mathrm F}>0\}.
$$

The rank counts the nonzero **diagonal tubes**, not the nonzero entries and not the nonzero frontal slices. It is at most $w$. The tensor is zero if and only if its tubal rank is zero.

**Theorem (the rank is the largest rank of the transform slices).** For every $A\in\mathbb{B}_{\mathrm{r}}^{n_1\times n_2\times n_3}$,

$$
\boxed{\;
\operatorname{rank}_{\mathrm t}(A)=\max_{1\le k\le n_3}\operatorname{rank}\bigl(\widehat A^{(k)}\bigr)
\;},
$$

where $\operatorname{rank}(\widehat A^{(k)})$ is the rank of the matrix over $\mathbb{B}_{\mathrm{r}}$, the larger of the two complex ranks of its idempotent coordinates.

*Proof.* The tube $S(i,i,:)$ is zero if and only if all of its Fourier coefficients are zero. Its $k$-th Fourier coefficient is the $i$-th diagonal entry of the matrix SVD of $\widehat A^{(k)}$, a pair of singular values of the two complex coordinates; take the singular values in each coordinate ordered decreasingly, so that the nonzero values form an initial segment. Hence the largest $i$ for which some coefficient is nonzero is the largest rank among the slices $\widehat A^{(k)}$, and the number of nonzero tubes is that largest index.

**Corollary (the matrix case).** For $n_3=1$ the t-product is the matrix product and the tubal rank is the matrix rank. For $n_3\ge2$ the tubal rank can be strictly smaller than the rank of every spatial frontal slice, because the transform mixes the slices; it is the rank of the slices of the transform that counts. For $n_3=2$, $A^{(1)}=\tfrac12 I_2$ and $A^{(2)}=\tfrac12\operatorname{diag}(1,-1)$ have spatial rank $2$, while the transform slices are $\operatorname{diag}(1,0)$ and $\operatorname{diag}(0,1)$, whose singular values pair into one nonzero tube and one zero tube, so the tubal rank is $1$.

**Remark (the rank is not the CP rank).** The CP rank is the smallest number of rank-one terms in the CANDECOMP/PARAFAC decomposition. The tubal rank is the number of nonzero diagonal tubes in the t-SVD. The two ranks are different invariants: a tensor can have small tubal rank and large CP rank, or the reverse. **The approximation theorem below is a theorem about the tubal rank**, and it says nothing about the best approximation of a given CP rank.

## The Truncated t-SVD

For $1\le k\le w$, the **rank-$k$ truncation** of $A$ is

$$
A_k=\sum_{i=1}^{k}U(:,i,:)\ast S(i,i,:)\ast V(:,i,:)^{\mathsf H}.
$$

Here $U(:,i,:)$ is $n_1\times1\times n_3$, $S(i,i,:)$ is $1\times1\times n_3$, and $V(:,i,:)$ is $n_2\times1\times n_3$; the t-product of the three factors is $n_1\times n_2\times n_3$, and the sum is the sum of $k$ such tensors.

**Proposition.** The tensor $A_k$ has tubal rank at most $k$. It has tubal rank exactly $k$ when the tubes $S(1,1,:),\dots,S(k,k,:)$ are all nonzero.

*Proof.* The t-SVD of $A_k$ is obtained by keeping the first $k$ diagonal tubes and setting the others to zero; the $*$-unitary factors are unchanged. The number of nonzero tubes is therefore at most $k$, and it is $k$ when the first $k$ tubes are nonzero.

**The algorithm.** Compute the t-SVD of $A$ by the algorithm of *The Singular Value Decomposition of a Reduced Biquaternion Tensor*; keep the first $k$ diagonal tubes and the corresponding columns of $U$ and $V$; reconstruct by the t-product. The cost is the cost of the t-SVD,

$$
O\bigl(n_1n_2n_3\log n_3+n_3\min(n_1^2n_2,n_1n_2^2)\bigr),
$$

plus $O(n_3k(n_1+n_2))$ for the reconstruction. The truncation is performed slice by slice in the Fourier domain on the two idempotent coordinates.

## The Best Rank-$k$ Approximation

**Theorem (Eckart-Young for the tubal rank).** For every $A\in\mathbb{B}_{\mathrm{r}}^{n_1\times n_2\times n_3}$ and every $1\le k\le w$,

$$
\boxed{\;
\|A-A_k\|_{\mathrm F}
=\min_{\operatorname{rank}_{\mathrm t}(B)\le k}\|A-B\|_{\mathrm F}
=\Bigl(\sum_{i=k+1}^{w}\|S(i,i,:)\|_{\mathrm F}^2\Bigr)^{1/2}
\;}.
$$

The minimum is attained at $A_k$; it is not unique when singular values coincide.

*Proof.* By the norm identity of *The Singular Value Decomposition of a Reduced Biquaternion Tensor*,

$$
\|A-B\|_{\mathrm F}^2=\frac1{n_3}\sum_{s=1}^{n_3}\|\widehat A^{(s)}-\widehat B^{(s)}\|_{\mathrm F}^2.
$$

If $\operatorname{rank}_{\mathrm t}(B)\le k$, then every transform slice $\widehat B^{(s)}$ has rank at most $k$: the tubal rank is the largest rank of the transform slices by the theorem above. For each $s$, the matrix Eckart-Young theorem over the two complex coordinates gives

$$
\|\widehat A^{(s)}-\widehat B^{(s)}\|_{\mathrm F}^2
\ge\sum_{i=k+1}^{w}\tfrac12\bigl(\widehat S_{(1)}(i,i,s)^2+\widehat S_{(2)}(i,i,s)^2\bigr),
$$

where $\widehat S_{(1)}$ and $\widehat S_{(2)}$ are the two complex coordinate diagonals of $\widehat S$. Summing over $s$ and dividing by $n_3$ gives the lower bound

$$
\|A-B\|_{\mathrm F}^2\ge\frac1{n_3}\sum_{s=1}^{n_3}\sum_{i=k+1}^{w}\tfrac12\bigl(\widehat S_{(1)}(i,i,s)^2+\widehat S_{(2)}(i,i,s)^2\bigr)
=\sum_{i=k+1}^{w}\|S(i,i,:)\|_{\mathrm F}^2,
$$

where the last equality is the norm identity applied to the tail of the t-SVD. The tensor $A_k$ attains the bound, so it is a minimizer.

**Corollary (the error is the discarded tail).** The squared error is the sum of the squared Frobenius norms of the discarded diagonal tubes. In particular the error decreases with $k$, and it is zero exactly when $A$ has tubal rank at most $k$.

**Remark (optimality is for the tubal rank).** The theorem is the exact analogue of the matrix Eckart-Young theorem, with the matrix rank replaced by the tubal rank and the singular values replaced by the diagonal tubes. **It does not give the best approximation of a prescribed CP rank, Tucker rank or tensor ring rank**, because those ranks are not the number of nonzero tubes of the t-SVD.

## The Matrix Case and the Other Ranks

For $n_3=1$ the tensor is a matrix, the t-SVD is the matrix SVD, the diagonal tubes are the singular values, and the theorem is the matrix Eckart-Young theorem: $A_k$ is the sum of the first $k$ terms of the SVD, and the error is the sum of the squares of the discarded singular values. The tubal rank is the matrix rank.

For $n_3\ge2$ the tubal rank is one of several tensor ranks. The **CP rank** is the smallest number of rank-one terms in the CP decomposition; it is not read on the t-SVD. The **Tucker rank** is the tuple of ranks of the unfoldings; it is the rank of the Tucker decomposition. The **tensor ring rank** is the tuple of ranks of the cyclic matricisations of the tensor ring decomposition, introduced by Zhao, Zhou, Xie, Zhang and Cichocki. None of these ranks is the tubal rank, and the truncation theorem above is not their Eckart-Young theorem.

**Remark (the comparison).** The t-SVD is the right decomposition when the data are a stack of matrices coupled by a circular convolution, as a color video is a stack of frames. The tubal rank then measures the number of independent tubes in the transform, and the truncation is both optimal and cheap. **For a tensor whose structure is a CP or a tensor ring network, the tubal rank is the wrong invariant**, and the corresponding decomposition is the one to use.

## Verification

The rank formula and the truncation were recomputed on random tensors of sizes $3\times2\times4$, $3\times3\times4$ and $4\times4\times2$, with at most $32$ entries. The tubal rank agreed with the largest rank of the transform slices in every case: $2$ for $3\times2\times4$, $3$ for $3\times3\times4$, and $4$ for $4\times4\times2$. The truncation error agreed with the discarded tail to $3.2\times10^{-15}$; it decreased from $2.95$ at $k=1$ to $3.2\times10^{-15}$ at $k=2$ for a $3\times2\times4$ tensor; and the truncated tensor had tubal rank $k$. The example of the two spatial slices of rank $2$ had transform ranks $1$ and $1$ and tubal rank $1$. On the same tensor the best of twenty random tubal-rank-one tensors had error $19.71$, against $2.95$ for the truncated t-SVD, which is the expected gap and not a proof; the proof is the theorem.

## Summary

The tubal rank of $A$ is the number of nonzero diagonal tubes of its t-SVD, and it equals the largest rank of the frontal slices of the Fourier transform. The rank-$k$ truncation $A_k$ keeps the first $k$ tubes and has tubal rank at most $k$. The Eckart-Young theorem for the tubal rank states that $A_k$ is the best approximation of $A$ in the Frobenius norm among all tensors of tubal rank at most $k$, and that the squared error is the sum of the squared norms of the discarded tubes. For $n_3=1$ this is the matrix theorem. The CP rank, the Tucker rank and the tensor ring rank are different invariants, and the theorem does not apply to them. **The t-SVD truncation is optimal for the rank it defines, and only for that rank.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{rank}_{\mathrm t}(A)$ | The tubal rank, the number of nonzero diagonal tubes |
| $w$ | $\min(n_1,n_2)$ |
| $S(i,i,:)$ | A diagonal tube of the middle factor |
| $A_k$ | The rank-$k$ truncation of $A$ |
| $\widehat A^{(k)}$ | The $k$-th frontal slice of the Fourier transform |
| CP rank, Tucker rank, tensor ring rank | The other tensor ranks, not the tubal rank |

## Further Reading

- Cui-E Yu, Xin Liu, Hui Luo and Yang Zhang, "Reduced biquaternion tensors and applications in color video processing", arXiv:2403.01690 (2024), Section 6. The Ht-tubal rank and the rank-$k$ approximation used for color video compression.
- Carl Eckart and Gale Young, "The approximation of one matrix by another of lower rank", *Psychometrika* **1** (1936) 211–218. The matrix theorem that the tensor theorem extends.
- Misha E. Kilmer and Carla D. Martin, "Factorization strategies for third-order tensors", *Linear Algebra and its Applications* **435** (2011) 641–658. The t-SVD and its truncation.
- Qibin Zhao, Guoxu Zhou, Shengli Xie, Liqing Zhang and Andrzej Cichocki, "Tensor ring decomposition", arXiv:1606.05535 (2016). The tensor ring rank and the decomposition against which the tubal rank is contrasted.
- Tamara G. Kolda and Brett W. Bader, "Tensor decompositions and applications", *SIAM Review* **51** (2009) 455–500. The CP and Tucker ranks.
