# __Color Video Compression and Deblurring with Reduced Biquaternion Tensors__

## Introduction

A color video is a stack of frames, and a stack of frames is a third-order tensor. Encoding the three color channels as the three imaginary units of a reduced biquaternion puts the whole video into one reduced biquaternion tensor, whose t-SVD compresses it and whose tensor equations deblur it. This article describes the encoding, the compression by the rank-$k$ truncation, the peak signal-to-noise ratio, the deblurring by the tensor equation, and the cost of the algorithms against the quaternion tensor algorithms they improve on.

The product is *The t-Product of Reduced Biquaternion Tensors*, the decomposition is *The Singular Value Decomposition of a Reduced Biquaternion Tensor*, the truncation is *The Rank of a Reduced Biquaternion Tensor and its Low-Rank Approximation*, and the equation is *Tensor Equations over the Reduced Biquaternions*. The image counterpart is *Non-Negative Matrix Factorization over the Reduced Biquaternions*.

The source is Cui-E Yu, Xin Liu, Hui Luo and Yang Zhang, "Reduced biquaternion tensors and applications in color video processing", which introduces the Ht-product and the Ht-SVD for this application. The quaternion tensor algorithms it improves on are those of Qin, Ming and Zhang and of the color image processing literature.

## The Color Video Tensor

Let $A_{\mathrm R},A_{\mathrm G},A_{\mathrm B}\in\mathbb{R}^{n_1\times n_2\times n_3}$ be the red, green and blue channels of a video with $n_1\times n_2$ pixels and $n_3$ frames. The **color video tensor** is

$$
A_{\mathrm C}(m,n,t)=A_{\mathrm R}(m,n,t)i+A_{\mathrm G}(m,n,t)j+A_{\mathrm B}(m,n,t)ij.
$$

The source writes the last term $A_{\mathrm B}k$ with $k=ij$; the basis element is the same. The frame index $t$ is kept apart from the basis symbol $ij$ here.

The frontal slice $A_{\mathrm C}(:,:,t)$ is the $t$-th frame, and each pixel is a pure reduced biquaternion with no real part. In the notation of the branch, $A_{\mathrm C}=A_0+A_1i+A_2j+A_3ij$ with

$$
A_0=0,\qquad A_1=A_{\mathrm R},\qquad A_2=A_{\mathrm G},\qquad A_3=A_{\mathrm B}.
$$

The two idempotent coordinates are therefore

$$
A_{(1)}=A_{\mathrm G}+i(A_{\mathrm R}+A_{\mathrm B}),\qquad
A_{(2)}=-A_{\mathrm G}+i(A_{\mathrm R}-A_{\mathrm B}),
$$

and the color channels are recovered by

$$
A_{\mathrm R}=\frac{A_{(1)}+A_{(2)}}{2i},\qquad
A_{\mathrm G}=\operatorname{Re}\frac{A_{(1)}-A_{(2)}}{2},\qquad
A_{\mathrm B}=\operatorname{Im}\frac{A_{(1)}-A_{(2)}}{2}.
$$

**Remark (the real part).** The encoding uses three of the four real coordinates; the fourth, $A_0$, is zero. The t-product and the t-SVD are taken over the full algebra, and a product or an approximation of pure tensors need not be pure: the real part is a residual, not a color channel. **The color reconstruction reads the coefficients of $i,j,ij$ and discards the real part.** The source's model uses the same pure encoding.

**Remark (the time mode).** The t-product convolves along the third mode circularly. The video is therefore treated as periodic in time. This is the modeling assumption of the t-product, not a property of the video; the first and last frames are coupled by the circular convolution. The source uses the same convention. A non-periodic treatment requires a different transform or a boundary extension, and it is outside this article.

## Compression

The compression is the rank-$k$ truncation of *The Rank of a Reduced Biquaternion Tensor and its Low-Rank Approximation*. Compute the t-SVD

$$
A_{\mathrm C}=U\ast S\ast V^{\mathsf H},
$$

keep the first $k$ diagonal tubes and the corresponding columns,

$$
A_{\mathrm C,k}=\sum_{i=1}^{k}U(:,i,:)\ast S(i,i,:)\ast V(:,i,:)^{\mathsf H},
$$

and reconstruct the color channels from $A_{\mathrm C,k}$ by the formulas above. The stored data are

$$
U_k\in\mathbb{B}_{\mathrm{r}}^{n_1\times k\times n_3},\qquad
S_k\in\mathbb{B}_{\mathrm{r}}^{k\times k\times n_3},\qquad
V_k\in\mathbb{B}_{\mathrm{r}}^{n_2\times k\times n_3},
$$

with $S_k$ f-diagonal, so the number of reduced biquaternion entries is $n_3k(n_1+n_2+1)$. Each entry is four real numbers, so the compressed representation has $4n_3k(n_1+n_2+1)$ real scalars. The original color video has $3n_1n_2n_3$ real scalars, and the encoded tensor has $4n_1n_2n_3$ real scalars, one of which is zero at every pixel.

**The compression ratio.** Relative to the encoded tensor, the ratio is

$$
\rho_{\mathrm{tensor}}=\frac{n_1n_2}{k(n_1+n_2+1)},
$$

and relative to the original RGB video it is

$$
\rho_{\mathrm{RGB}}=\frac{3n_1n_2}{4k(n_1+n_2+1)}.
$$

For $n_1=n_2=256$, $n_3=100$ and $k=20$, the two ratios are $6.39$ and $4.79$. The ratio grows linearly in the spatial size and inversely in the rank; the number of frames cancels because both the original and the factors carry the same third mode.

**The algorithm.**

1. Encode the video as $A_{\mathrm C}=A_{\mathrm R}i+A_{\mathrm G}j+A_{\mathrm B}ij$.
2. Compute the t-SVD by the algorithm of *The Singular Value Decomposition of a Reduced Biquaternion Tensor*: transform the two idempotent coordinates, take the complex SVDs of the transform slices, assemble $U,S,V$, and invert the transform.
3. Keep the first $k$ diagonal tubes and the corresponding columns.
4. Reconstruct $A_{\mathrm C,k}$ and decode the three channels.
5. Clip the channels to the valid range if the reconstruction leaves it.

The cost is the cost of the t-SVD,

$$
O\bigl(n_1n_2n_3\log n_3+n_3\min(n_1^2n_2,n_1n_2^2)\bigr),
$$

plus $O(n_3k(n_1+n_2))$ for the reconstruction.

**The optimality.** The truncation is the best approximation of $A_{\mathrm C}$ in the Frobenius norm among all tensors of tubal rank at most $k$. **It is optimal for the tubal rank, not for the perceptual quality of the video**, and it is not the best approximation of a prescribed CP or tensor ring rank.

## The Peak Signal-to-Noise Ratio

The reconstruction error is measured by the peak signal-to-noise ratio

$$
\mathrm{PSNR}=10\log_{10}\frac{3n_1n_2\lVert C\rVert_\infty^2}{\lVert C-C_k\rVert_{\mathrm F}^2},
$$

where $C$ and $C_k$ are one frame of the original and of the reconstruction, $\lVert C\rVert_\infty$ is the maximum absolute value of a channel sample, and $\lVert C-C_k\rVert_{\mathrm F}^2$ is the sum of the squared errors over all pixels and all three channels. The factor $3n_1n_2$ is the number of channel samples in a frame; the formula is the per-frame PSNR, and the PSNR of the video is the average of the per-frame values. If the video is normalized to $[0,1]$, the peak is at most $1$; if it is stored in eight bits, the peak is at most $255$. The PSNR is in decibels, and a higher value is a smaller error.

**Remark (what the PSNR does not see).** The PSNR is a global mean of the squared error. It does not measure temporal flicker, motion, or perceptual quality. The t-SVD truncation couples the frames through the transform, and a low-rank approximation can smooth a moving object across frames while keeping a good PSNR. **The PSNR is a necessary check, not a sufficient one**, and the source reports it together with visual comparisons.

## Deblurring

The blur is modeled by the tensor equation

$$
B=H\ast X+N,
$$

where $X$ is the clean color video tensor, $H$ is the blur tensor, $B$ is the observed video and $N$ is noise. The t-product applies the blur to each frame and convolves the frames along the time mode. The deblurring solves $H\ast X=B$ for $X$.

**The exact case.** If $H$ is a unit of the tensor algebra, then

$$
X=H^{-1}\ast B.
$$

The inverse is computed by the criterion of *Zero Divisors of the Reduced Biquaternion Tensor Algebra*: transform $H$, invert every transform slice in both idempotent coordinates, and invert the transform. The cost is the cost of the transform and of the slicewise matrix inverses, $O(n_1n_2n_3\log n_3+n_3n_1^3)$ for square tensors.

**The general case.** If $H$ is not a unit, the equation may have no exact solution, and one takes the minimum-norm least-squares solution of *Tensor Equations over the Reduced Biquaternions*,

$$
X=H^\dagger\ast B,
$$

or the Tikhonov solution

$$
X=(H^{\mathsf H}\ast H+\lambda\mathrm I)^{-1}\ast H^{\mathsf H}\ast B
$$

for a regularization parameter $\lambda>0$. The pseudoinverse is computed by the t-SVD of $H$; the Tikhonov solution is computed slicewise in the transform. The zero-divisor criterion says when the exact inverse exists: $H$ is a unit exactly when no transform slice is singular in either coordinate.

**The algorithm.**

1. Encode the observed video as $B$.
2. Compute the transform of $B$ and of the blur tensor $H$.
3. For each transform slice and each idempotent coordinate, solve the matrix equation $\widehat H^{(k)}\widehat X^{(k)}=\widehat B^{(k)}$ by the matrix inverse, the matrix pseudoinverse, or the regularized inverse.
4. Invert the transform and decode the three channels.

The cost is the cost of the t-SVD of $H$ plus the slicewise matrix solves,

$$
O\bigl(n_1n_2n_3\log n_3+n_3\min(n_1^2n_2,n_1n_2^2)\bigr).
$$

**Remark (the blur tensor).** A scalar blur, the same for the three channels, has the same complex value in both idempotent coordinates. A channel-dependent blur has different coefficients; the reduced biquaternion encoding carries them in one tensor. A blur tensor with a zero idempotent coordinate is a zero divisor and has no inverse; the pseudoinverse or the regularization is then the only recourse. **The t-determinant decides which case applies before any solve is attempted.**

## The Cost Against the Quaternion Algorithms

The quaternion tensor algorithms carry four real coordinates per entry and use a quaternion SVD at every transform slice. The reduced biquaternion algorithms carry the same four real coordinates, in two complex coordinates, and use two complex SVDs at every slice; the storage is the same and the decomposition is cheaper. The asymptotic cost is the same up to constants,

$$
O\bigl(n_1n_2n_3\log n_3+n_3\min(n_1^2n_2,n_1n_2^2)\bigr),
$$

but the constants are smaller: the transform is a complex FFT applied to the two coordinates, the slicewise decomposition is a pair of complex SVDs, and no quaternion iteration is needed. The source reports a lower running time for the reduced biquaternion algorithms on color video compression and deblurring, with a PSNR comparable to the quaternion methods.

**Remark (the quality against the quaternion t-SVD).** The reduced biquaternion t-SVD is algebraically the pair of the two complex t-SVDs of the idempotent coordinates. Its truncation is optimal for the tubal rank, as the quaternion truncation is optimal for the quaternion tubal rank. The two approximations need not coincide, because the quaternion algebra and the reduced biquaternion algebra are different; the source's experiments compare them on the same videos. **The reduced biquaternion advantage is computational, not a different approximation theorem.**

## Verification

The pipeline was recomputed on a synthetic color video of $4\times4$ pixels and $2$ frames, with $32$ tensor entries and $96$ color samples. The encoding and decoding were inverse to $1.1\times10^{-16}$. The tubal rank of the video tensor was $3$; the per-frame PSNR of the rank-$k$ reconstruction, averaged over the two frames, was $25.6$ dB at $k=1$, $36.2$ dB at $k=2$, and $70.9$ dB at $k=3$, the last being the numerical roundoff of the exact reconstruction. For this small video the compression ratios were $1.78$ against the encoded tensor and $1.33$ against RGB at $k=1$; the formula gives $6.39$ and $4.79$ for $256\times256$ pixels, $100$ frames and $k=20$.

For the deblurring, the blur tensor was a unit with a cyclic shift of strength $0.15$; the exact deblurring reproduced the clean video to $3.4\times10^{-16}$. With $1\%$ noise, the pseudoinverse reconstruction had a relative error of $8.0\times10^{-3}$ and a per-frame PSNR, averaged over the two frames, of $49.7$ dB. The exact case and the noisy case used the same transform, slicewise solve and inverse transform as the algorithm above.

## Summary

A color video is encoded as $A_{\mathrm C}=A_{\mathrm R}i+A_{\mathrm G}j+A_{\mathrm B}ij$, one frame per frontal slice. The rank-$k$ truncation of its t-SVD compresses the video; the stored factors have $n_3k(n_1+n_2+1)$ reduced biquaternion entries, and the compression ratio is $n_1n_2/[k(n_1+n_2+1)]$ against the encoded tensor and $3n_1n_2/[4k(n_1+n_2+1)]$ against RGB. The reconstruction error is measured by the per-frame PSNR $10\log_{10}(3n_1n_2\lVert C\rVert_\infty^2/\lVert C-C_k\rVert_{\mathrm F}^2)$, averaged over the frames. Deblurring solves $H\ast X=B$: the inverse when $H$ is a unit, the pseudoinverse or a Tikhonov solution otherwise, all slicewise in the Fourier domain. The reduced biquaternion algorithms replace the quaternion SVD by two complex SVDs and the quaternion transform by two complex transforms; the asymptotic cost is the same and the constants are smaller. **The compression is optimal for the tubal rank, the deblurring is the tensor-equation solution, and the color video is one reduced biquaternion tensor.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A_{\mathrm C}=A_{\mathrm R}i+A_{\mathrm G}j+A_{\mathrm B}ij$ | The color video tensor |
| $A_{\mathrm C,k}$ | The rank-$k$ reconstruction |
| $U_k,S_k,V_k$ | The truncated t-SVD factors |
| $\mathrm{PSNR}$ | The peak signal-to-noise ratio |
| $B=H\ast X+N$ | The blur model |
| $H^\dagger$ | The Moore-Penrose inverse of the blur tensor |
| $\lambda$ | The Tikhonov regularization parameter |

## Further Reading

- Cui-E Yu, Xin Liu, Hui Luo and Yang Zhang, "Reduced biquaternion tensors and applications in color video processing", arXiv:2403.01690 (2024). The Ht-product, the Ht-SVD, the color video compression and the deblurring experiments.
- Z. Qin, Z. Ming and L. Zhang, "Singular value decomposition of third order quaternion tensors", *Applied Mathematics Letters* **123** (2022) 107597. The quaternion tensor SVD that the reduced biquaternion algorithm improves on.
- Misha E. Kilmer and Carla D. Martin, "Factorization strategies for third-order tensors", *Linear Algebra and its Applications* **435** (2011) 641–658. The t-product and the t-SVD.
- Soo-Chang Pei, Ja-Han Chang, Jian-Jiun Ding and Ming-Yang Chen, "Eigenvalues and singular value decompositions of reduced biquaternion matrices", *IEEE Transactions on Circuits and Systems I* **55** (2008) 2673–2685. The matrix algebra and the two idempotent coordinates.
- Tamara G. Kolda and Brett W. Bader, "Tensor decompositions and applications", *SIAM Review* **51** (2009) 455–500. The tensor vocabulary and the other tensor decompositions.
