# __The Spin-One Anti-Hermitian Subspace and Spectral Regularity in $M_2(\mathbb{C})$__

## Introduction

**The question.** Where on the skew-adjoint space $\mathfrak{u}(2)$, and on its carrier $\mathfrak{su}(2)$, do the two eigenvalues of a matrix coincide?

**Why it is the same statement.** This is the in-depth matrix reading of [The Spin-One Anti-Hermitian Subspace and Spectral Regularity](the-spin-one-anti-hermitian-subspace-and-spectral-regularity.html). The source's predicate is $B^2=Q_x^2+Q_y^2+Q_z^2\neq0$; in the display it is $\Delta=\tau^2-4\det\neq0$, and on the skew space $\Delta=-4|v|^2$. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. That $B^2(i\lambda\mathrm I_2+v\cdot E)=|v|^2$, so the degenerate locus of the space is the trace line. That the spectrum is the purely imaginary pair $i(\lambda\pm|v|)$. That the carrier is spectrally regular away from the origin. That the degenerate and the singular loci of the space meet only at the origin. That the space meets all four sectors while no carrier meets more than one. The comparison with the Hermitian half.

**What the article does not do.** It does not treat the determinant on the same space, which is [The Spin-One Anti-Hermitian Subspace and N Norm Regularity in $M_2(\mathbb{C})$](the-spin-one-anti-hermitian-subspace-and-n-norm-regularity-in-m2c.html); it does not treat the sectors in full, which is [The Spin-One Anti-Hermitian Subspace and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-one-anti-hermitian-subspace-and-the-sectors-of-n-and-spectral-regularity-in-m2c.html).

**Conventions.** $A=i\lambda\mathrm I_2+v\cdot E$, $\lambda\in\mathbb{R}$, $v\in\mathbb{R}^3$, $E_k=-i\sigma_k$, $|v|^2=v_1^2+v_2^2+v_3^2$. Then $\tau=2i\lambda$ and $B^2=\det A-\tfrac14\tau^2$.

**The sign of $\Delta$.** On the skew space $\Delta=-4|v|^2\le0$: the discriminant is real and non-positive, so a repeated eigenvalue can only be a real double root.

**Boundaries.** The space is [Introduction to the Spin-One Anti-Hermitian Subspace in $M_2(\mathbb{C})$](the-spin-one-anti-hermitian-subspace-in-m2c.html). The predicate in general is [The Spectrum](the-spectrum-of-a-biquaternion.html). The sectors are [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** $\lambda$ the trace coordinate, $v$ the carrier coordinates, $\Delta$ the discriminant, $E_k$ the generators.

## The Predicate on the Closure

**The array.** With $E_1=-i\sigma_1$, $E_2=-i\sigma_2$, $E_3=-i\sigma_3$,
$$
i\lambda\mathrm I_2+v\cdot E=
\begin{pmatrix}i\lambda-iv_3 & -iv_1-v_2\\ -iv_1+v_2 & i\lambda+iv_3\end{pmatrix},
$$
whose determinant is $v_1^2+v_2^2+v_3^2-\lambda^2$ and whose trace is $2i\lambda$, verified.

**The formula.**
$$
B^2(i\lambda\mathrm I_2+v\cdot E)=|v|^2,\qquad \Delta=-4|v|^2,
$$
verified on a hundred random real pairs to $3.6\cdot10^{-15}$ and $1.4\cdot10^{-14}$.

**The degenerate locus is the trace line.**
$$
\mathfrak{u}(2)\cap\{\Delta=0\}=\mathbb{R}(i\mathrm I_2),
$$
of real dimension one. Every element of the line has the single eigenvalue $i\lambda$ twice; every element off it has distinct eigenvalues.

**The spectrum.**
$$
\operatorname{spec}(i\lambda\mathrm I_2+v\cdot E)=\{i(\lambda-|v|),\,i(\lambda+|v|)\},
$$
purely imaginary, symmetric about $i\lambda$. Verified: $i\mathrm I_2+E_1$ has eigenvalues $0$ and $2i$.

**Why the spectrum is imaginary.** The matrix is $i$ times a Hermitian one, and a Hermitian matrix has real eigenvalues; multiplying by $i$ rotates them onto the imaginary axis. The reality of $v$ is what makes $|v|$ real, and the reality of $|v|$ is what makes the eigenvalues purely imaginary.

## The Predicate on the Carrier

**The carrier.** $\operatorname{spec}(v\cdot E)=\{\pm i|v|\}$, distinct for every $v\neq0$.

**The carrier avoids the degenerate locus.** $\mathfrak{su}(2)\cap\{\Delta=0\}=\{0\}$.

**The decisive criterion.** On the carrier the predicate is the non-vanishing of a positive definite quadratic form, so it is decided by one number and not by a spectral computation.

## The Two Degenerate Loci Are Disjoint

**The statement.** On the skew space the singular locus is $|v|=|\lambda|$ and the degenerate locus is $v=0$:
$$
\{|v|=|\lambda|\}\cap\{v=0\}=\{0\}.
$$

**The reading.** The singular elements of the skew space are the rank-one skew matrices with a non-zero trace $2i\lambda$; the spectrally degenerate ones are the multiples of $i\mathrm I_2$. The two families meet only at the origin.

**The contrast with the plane.** On the plane the two loci are the whole plane and the origin, so one contains the other. On the skew space they are a cone and a line, and neither contains the other.

## The Four Sectors Inside the Space

**The partition.** On $\mathfrak{u}(2)$ the two predicates are $\det=|v|^2-\lambda^2$ and $\Delta=-4|v|^2$:
$$
\Sigma_{11}:\ v\neq0,\ |v|\neq|\lambda|;\qquad
\Sigma_{10}:\ v=0,\ \lambda\neq0;\qquad
\Sigma_{01}:\ v\neq0,\ |v|=|\lambda|;\qquad
\Sigma_{00}:\ v=0,\ \lambda=0 .
$$
Verified on witnesses: $i\mathrm I_2+2E_1$ is in $\Sigma_{11}$, $i\mathrm I_2$ in $\Sigma_{10}$, $i\mathrm I_2+E_1$ in $\Sigma_{01}$, and the origin in $\Sigma_{00}$.

**The reading.** The space meets all four sectors, which no single carrier does.

## The Partner Half

**The Hermitian half.** On $\lambda\mathrm I_2+v\cdot\sigma$ with real $\lambda,v$,
$$
B^2=-\lvert v\rvert^2,\qquad \operatorname{spec}=\{\lambda-|v|,\lambda+|v|\},
$$
verified to $3.6\cdot10^{-15}$. The spectrum is real and symmetric about $\lambda$; the degenerate locus is the same line $\mathbb{R}\mathrm I_2$.

**The predicate is the same and the spectrum is not.** The degenerate locus is decided by the vanishing of the vector part in both halves; where the eigenvalues lie is decided by which half. The predicate reads $\Delta$ and not the location of the spectrum.

## The Three Carriers Compared

| carrier | $\Delta$ on it | degenerate locus in it |
|---|---|---|
| centre $\mathbb{C}\mathrm I_2$ | $0$ | the whole centre |
| plane $\mathbb{C}P$ | $\lambda^2$ | $\{0\}$ |
| carrier $\mathfrak{su}(2)$ | $-4\lvert v\rvert^2$ | $\{0\}$ |

**The pattern.** Away from the origin the centre is in $\Sigma_{10}$, the plane in $\Sigma_{01}$, the carrier in $\Sigma_{11}$. No carrier away from the origin is in $\Sigma_{00}$.

**Why the carrier is the last one.** The line has the determinant and loses the spectrum; the plane has the spectrum and loses the determinant; the carrier has both.

## Where $n=2$ Differs

**The discriminant.** At $n=2$ the discriminant is a real non-positive number on the skew space, so the degenerate locus is a line and the criterion is one inequality. At order $n$ the eigenvalues of a skew matrix are purely imaginary and come in conjugate pairs; the degenerate locus is a union of strata indexed by the multiplicities, and "distinct eigenvalues" is the complement of a discriminant hypersurface of codimension one but not a single number.

**The carrier.** At $n=2$ the carrier is three-dimensional and the degenerate locus inside it is the origin. At order $n$ the traceless skew part has dimension $n^2-1$ and its degenerate locus is the union of the skew matrices with a repeated eigenvalue, a hypersurface inside it.

**What does not differ.** The spectrum of a skew matrix is purely imaginary at every order, and the trace line is the degenerate locus of $\mathfrak{u}(n)$ exactly when all the eigenvalues coincide, that is on the centre.

## Summary

On the skew-adjoint space $B^2=|v|^2$ and $\Delta=-4|v|^2$, so the degenerate locus is the trace line $\mathbb{R}(i\mathrm I_2)$ and the spectrum of $i\lambda\mathrm I_2+v\cdot E$ is the purely imaginary pair $i(\lambda\pm|v|)$. On the carrier the spectrum is $\pm i|v|$, distinct for every non-zero $v$, so the carrier is spectrally regular away from the origin.

The singular locus $|v|=|\lambda|$ and the degenerate locus $v=0$ of the space meet only at the origin, and the space meets all four sectors while no carrier meets more than one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathfrak{u}(2)=\mathbb{R}(i\mathrm I_2)\oplus\mathfrak{su}(2)$ | the skew-adjoint space |
| $\lambda,\ v$ | real coordinates of the trace line and of the carrier |
| $\Delta=\tau^2-4\det$ | the discriminant, $-4\lvert v\rvert^2$ |
| $|v|^2$ | the positive definite form on the carrier |

## Further Reading

- [The Spin-One Anti-Hermitian Subspace and Spectral Regularity](the-spin-one-anti-hermitian-subspace-and-spectral-regularity.html), for the source's eigenvalue computation.
- [The Spin-One Anti-Hermitian Subspace and N Norm Regularity in $M_2(\mathbb{C})$](the-spin-one-anti-hermitian-subspace-and-n-norm-regularity-in-m2c.html), for the determinant on the same space.
- [The Spin-One Anti-Hermitian Subspace and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-one-anti-hermitian-subspace-and-the-sectors-of-n-and-spectral-regularity-in-m2c.html), for the sector table.
- [The Spectrum](the-spectrum-of-a-biquaternion.html), for the quadratic relation.
- [The N-Regular, Spectrally Regular Sector](the-n-regular-spectrally-regular-sector.html), for the sector in which the carrier lies.
