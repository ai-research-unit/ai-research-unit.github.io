# __The Spin-Zero Centre Subspace and Spectral Regularity in $M_2(\mathbb{C})$__

## Introduction

**The question.** On the centre of $M_2(\mathbb{C})$, are the two eigenvalues of an element distinct, and where does the centre sit in the spectral-degenerate locus?

**Why it is the same statement.** This is the in-depth matrix reading of [The Spin-Zero Centre Subspace and Spectral Regularity](the-spin-zero-centre-subspace-and-spectral-regularity.html). The source's predicate is $B^2=Q_x^2+Q_y^2+Q_z^2\neq0$; under the display $B^2=\det A-\tfrac14(\operatorname{tr}A)^2=-\tfrac14\Delta$, so the predicate is $\Delta\neq0$, distinct eigenvalues. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. The Cayley–Hamilton relation and the two eigenvalues. That every central element has $\Delta=0$, one eigenvalue of algebraic multiplicity two, and that it is nevertheless diagonalisable. That the double eigenvalue is the multiplicity of the space, not a defect. That the degenerate locus is far larger than the centre, with the nilpotent example $A=-(\sigma_3+i\sigma_2)$. That the centre is exactly the part of the locus with zero traceless part. The carrier table and the sector of the centre.

**What the article does not do.** It does not treat the determinant on the centre, which is [The Spin-Zero Centre Subspace and N Norm Regularity in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-and-n-norm-regularity-in-m2c.html); it does not treat the four sectors in general, which is [The Spin-Zero Centre Subspace and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-and-the-sectors-of-n-and-spectral-regularity-in-m2c.html).

**Conventions.** $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$, so $Q_t=\tfrac12\operatorname{tr}A$ and $B^2=\det A-\tfrac14(\operatorname{tr}A)^2$. The discriminant is $\Delta=(\operatorname{tr}A)^2-4\det A=-4B^2$. Spectral-regular means $\Delta\neq0$; spectral-degenerate means $\Delta=0$.

**Boundaries.** The carrier is [Introduction to the Spin-Zero Centre Subspace in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-in-m2c.html). The dictionary is [The Pauli Representation : Operators](m2c-pauli-representation-operators.html). The element-level spectrum is [The Spectrum](the-spectrum-of-a-biquaternion.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html).

**Letters.** $A$ a matrix, $\tau=\operatorname{tr}A$, $\delta=\det A$, $\Delta=\tau^2-4\delta$, $P$ a rank-one projection.

## The Two Eigenvalues

**The relation.** Every $2\times2$ matrix satisfies
$$
A^2-\tau A+\delta\mathrm I_2=0,
$$
the Cayley–Hamilton relation, verified on a hundred random matrices to better than $10^{-14}$.

**The eigenvalues.** The roots are
$$
\lambda_\pm=\frac{\tau\pm\sqrt{\Delta}}{2}=\frac{\tau}{2}\pm iB,
$$
with $\lambda_++\lambda_-=\tau$ and $\lambda_+\lambda_-=\delta$. With $Q_t=\tau/2$ this is the source's $Q_t\pm iB$.

**The predicate.** Spectral-regular is $\Delta\neq0$, two distinct eigenvalues; spectral-degenerate is $\Delta=0$, one eigenvalue repeated. The zero locus is the **spectral-degenerate cone** $\mathcal S=\{\Delta=0\}$.

**The two spectra.** The eigenvalues of $A$ are computed from $A$. The weights of a carrier are eigenvalues of the operator of the action and belong to the carrier. The word spectrum alone will not say which is meant.

## The Predicate on the Centre

**The square of the traceless part.** For $A=\lambda\mathrm I_2$,
$$
A-\tfrac12(\operatorname{tr}A)\mathrm I_2=0,\qquad B^2=-\tfrac14\Delta=0 .
$$
So the centre lies in the degenerate locus, $\mathbb{C}\mathrm I_2\subseteq\mathcal S$.

**The spectrum.** $\operatorname{spec}(\lambda\mathrm I_2)=\{\lambda,\lambda\}$: one value, algebraic multiplicity two.

**The geometric multiplicity.** The eigenspace is the whole of $\mathbb{C}^2$, so the geometric multiplicity is two as well and the matrix is diagonal, hence diagonalisable. The word degenerate names the repetition of the eigenvalue and not a defect of the matrix.

**Why there is nothing to separate.** The minimal polynomial of $\lambda\mathrm I_2$ is $x-\lambda$, of degree one. A matrix with a minimal polynomial of degree one moves no direction at all, so no two directions can be independent.

**The count.** One distinct eigenvalue, complex dimension one, real dimension two. The identity $2s+1=\dim_\mathbb{R}$ is a statement about the carrier $\mathbb{R}\mathrm I_2$, of real dimension one, where $s=0$; it is not a statement about the closure.

## The Centre Is Not the Whole Degenerate Locus

**A nilpotent outside the centre.** With $A=-(\sigma_3+i\sigma_2)$,
$$
A^2=\sigma_3^2-\sigma_2^2+i\left(\sigma_2\sigma_3+\sigma_3\sigma_2\right)=0,
$$
since $\sigma_2^2=\sigma_3^2=\mathrm I_2$ and the two anticommute. Verified: $A^2=0$, $\operatorname{tr}A=0$, $\det A=0$ and $\operatorname{spec}(A)=\{0,0\}$.

**What the example shows.** $A$ is degenerate, non-zero, singular, non-central and not diagonalisable: the eigenspace is one-dimensional. The degenerate locus therefore contains a whole nilpotent orbit, the conjugates of $A$ by $\mathrm{GL}_2(\mathbb{C})$.

**The intersection.**
$$
\mathcal S\cap\left\{A-\tfrac12(\operatorname{tr}A)\mathrm I_2=0\right\}=\mathbb{C}\mathrm I_2,
$$
because a matrix with zero traceless part is scalar.

**How big the locus is.** $\Delta$ is one complex equation in the four complex entries, so $\mathcal S$ has complex dimension three: it is the discriminant hypersurface, the set of matrices with a repeated eigenvalue.

## The Centre Against the Other Carriers

| carrier | $B^2=-\tfrac14\Delta$ on it | degenerate locus in it |
|---|---|---|
| centre $\mathbb{C}\mathrm I_2$ | $0$ | the whole centre |
| minimal left ideal $M_2P$ | $-\lambda^2/4$ | $\{0\}$ |
| vector part $\mathfrak{su}(2)$ | $\lvert v\rvert^2$ | $\{0\}$ |

**The two extremes.** On the centre the predicate fails everywhere; on the ideal and on the vector part it holds everywhere except at the origin. An element of the ideal has rank at most one, so its determinant is zero and $B^2=-\tfrac14(\operatorname{tr}A)^2$; on the vector part the trace is zero and the determinant is $|v|^2$, so $B^2=|v|^2$.

**The sectors.** Away from the origin, the centre lies in $\Sigma_{10}$: the determinant is non-zero, the discriminant is zero. The ideal away from the origin lies in $\Sigma_{01}$, and the vector part away from the origin in $\Sigma_{11}$. The sector $\Sigma_{00}$ is met only at the origin.

## Worked Examples

**A central element.** $A=(2+3i)\mathrm I_2$: $\tau=4+6i$, $\delta=(2+3i)^2=-5+12i$, $\Delta=0$, both eigenvalues $2+3i$.

**A non-central element with the same spectrum.** $A=\operatorname{diag}(2+3i,\,2+3i)$ is central; $A'=\begin{pmatrix}2+3i&1\\0&2+3i\end{pmatrix}$ has the same eigenvalues and is not diagonalisable. Both are degenerate; only the first is central. So the predicate separates nothing inside the degenerate locus, and a second reading, the diagonalisability, separates the Jordan blocks.

**A spectrally regular element.** $A=\sigma_3$: $\tau=0$, $\delta=-1$, $\Delta=4$, eigenvalues $\pm1$, $B^2=-1$.

## Where $n=2$ Differs

**The predicate.** At $n=2$ the predicate is one complex number $\Delta=\tau^2-4\delta$, and the degenerate locus is one hypersurface. At order $n$ the discriminant is a polynomial in $n$ coefficients and the degenerate locus is the discriminant variety, of codimension one.

**The centre.** At $n=2$ every central element is degenerate, because $\lambda\mathrm I_2$ has one eigenvalue repeated twice. At order $n$ the same holds: $\lambda\mathrm I_n$ has one eigenvalue of multiplicity $n$.

**What does differ.** At $n=2$ the centre is exactly the intersection of the degenerate locus with the zero traceless part, and the nilpotent orbit is one family. At order $n$ the nilpotent orbits form a finite list indexed by partitions of $n$.

## Summary

Every element of the centre has $\Delta=0$: its traceless part vanishes, $B^2=0$ and its spectrum is the single value $\lambda$ repeated twice. The minimal polynomial is $x-\lambda$, of degree one, and the matrix is diagonalisable, so the repetition is the multiplicity of the space and not a defect.

The degenerate locus $\{\Delta=0\}$ is a complex hypersurface, far larger than the centre; the nilpotent $A=-(\sigma_3+i\sigma_2)$, with $A^2=0$, is degenerate and non-central. The centre is exactly the part of the locus with zero traceless part, and away from the origin it lies in the sector $\Sigma_{10}$: determinant non-zero, discriminant zero.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tau=\operatorname{tr}A$ | the trace |
| $\delta=\det A$ | the determinant |
| $\Delta=\tau^2-4\delta=-4B^2$ | the discriminant |
| $\mathcal S=\{\Delta=0\}$ | the spectral-degenerate locus |
| $\lambda_\pm=(\tau\pm\sqrt\Delta)/2$ | the two eigenvalues |
| $\Sigma_{ij}$ | the sector with $\det\neq0$ for $i=1$ and $\Delta\neq0$ for $j=1$ |

## Further Reading

- [The Spin-Zero Centre Subspace and Spectral Regularity](the-spin-zero-centre-subspace-and-spectral-regularity.html), for the source's reading of the predicate on the centre.
- [Introduction to the Spin-Zero Centre Subspace in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-in-m2c.html), for the carrier and the closure.
- [The Spin-Zero Centre Subspace and N Norm Regularity in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-and-n-norm-regularity-in-m2c.html), for the other predicate on the same space.
- [The Spin-Zero Centre Subspace and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-and-the-sectors-of-n-and-spectral-regularity-in-m2c.html), for the sector $\Sigma_{10}$.
- [The Spectrum](the-spectrum-of-a-biquaternion.html), for the characteristic polynomial of an element.
