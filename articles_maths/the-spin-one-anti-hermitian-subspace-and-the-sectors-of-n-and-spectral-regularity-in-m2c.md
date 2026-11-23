# __The Spin-One Anti-Hermitian Subspace and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$__

## Introduction

**The question.** Which of the four sectors does the carrier $\mathfrak{su}(2)$ meet, and which does its closure $\mathfrak{u}(2)$ meet?

**Why it is the same statement.** This is the in-depth matrix reading of [The Spin-One Anti-Hermitian Subspace and the Sectors of N and Spectral Regularity](the-spin-one-anti-hermitian-subspace-and-the-sectors-of-n-and-spectral-regularity.html). There the closures are $\mathfrak{k}$ and $\mathbb{R}(ie_t)\oplus\mathfrak{k}$ with the predicates $N$ and $B^2$; here they are $\mathfrak{su}(2)$ and $\mathfrak{u}(2)$ with the predicates $\det$ and $\Delta$. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. That on the carrier the two predicates vanish together, so the carrier meets two sectors. The sector table of the carrier. That on the closure the two predicates separate, and the closure meets all four. The witnesses. The orbit-space picture, in which the sector is read from the pair $(\lambda,|v|)$ in a half-plane. That the closure meets $\Sigma_{10}$ only in scalar matrices and contains no non-zero nilpotent. The comparison with the other two closures.

**What the article does not do.** It does not treat either predicate on its own, which are [The Spin-One Anti-Hermitian Subspace and N Norm Regularity in $M_2(\mathbb{C})$](the-spin-one-anti-hermitian-subspace-and-n-norm-regularity-in-m2c.html) and [The Spin-One Anti-Hermitian Subspace and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-one-anti-hermitian-subspace-and-spectral-regularity-in-m2c.html).

**Conventions.** $A=i\lambda\mathrm I_2+v\cdot E$ with real $\lambda$ and $v$, $E_k=-i\sigma_k$. Then $\tau=2i\lambda$, $\det=|v|^2-\lambda^2$ and $\Delta=-4|v|^2$. The sector $\Sigma_{ij}$ has $\det\neq0$ for $i=1$ and $\Delta\neq0$ for $j=1$.

**Boundaries.** The space is [Introduction to the Spin-One Anti-Hermitian Subspace in $M_2(\mathbb{C})$](the-spin-one-anti-hermitian-subspace-in-m2c.html). The strata of $\Sigma_{10}$ are [The N-Regular, Spectrally Degenerate Sector](the-n-regular-spectrally-degenerate-sector.html). The same question on the plane is [The Spin-Half Bispinors and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinors-and-the-sectors-of-n-and-spectral-regularity-in-m2c.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** $\lambda$ the trace coordinate, $v$ the carrier coordinates, $r=|v|$.

## The Carrier: Two Sectors

**The two predicates coincide.** On $\mathfrak{su}(2)$,
$$
\det(v\cdot E)=|v|^2,\qquad \Delta(v\cdot E)=-4|v|^2 .
$$
Both vanish exactly at $v=0$. The constant of proportionality is $-4$, and no value of $v$ separates the two vanishings.

**The table.**

| sector | condition on $v$ | intersection | $\dim_\mathbb{R}$ |
|---|---|---|---|
| $\Sigma_{11}$ | $v\neq0$ | $\mathfrak{su}(2)\setminus\{0\}$ | $3$ |
| $\Sigma_{10}$ | impossible | $\varnothing$ | — |
| $\Sigma_{01}$ | impossible | $\varnothing$ | — |
| $\Sigma_{00}$ | $v=0$ | $\{0\}$ | $0$ |

**Why the mixed sectors are empty.** They are defined by the disagreement of the two predicates, and on the carrier the two agree.

**The spectrum on the carrier.** $\{\pm i|v|\}$, distinct for $v\neq0$: invertible with a separated spectrum.

**The carrier is the positive one.** It is the only one of the three carriers on which both predicates are definite; the sector test there is the test of a length.

## The Closure: Four Sectors

**The two predicates.**
$$
\det(i\lambda\mathrm I_2+v\cdot E)=|v|^2-\lambda^2,\qquad \Delta=-4|v|^2 .
$$
The second sees $v$ alone; the first sees the difference of the two squares.

**The table.**

| sector | condition on $(\lambda,v)$ | intersection | $\dim_\mathbb{R}$ |
|---|---|---|---|
| $\Sigma_{11}$ | $v\neq0$, $\lvert v\rvert\neq\lvert\lambda\rvert$ | off both loci | $4$ |
| $\Sigma_{10}$ | $v=0$, $\lambda\neq0$ | $\mathbb{R}(i\mathrm I_2)\setminus\{0\}$ | $1$ |
| $\Sigma_{01}$ | $\lvert v\rvert=\lvert\lambda\rvert$, $v\neq0$ | null cone minus apex | $3$ |
| $\Sigma_{00}$ | $\lambda=0$, $v=0$ | $\{0\}$ | $0$ |

**The witnesses.** Verified:

| witness | $\det$ | $\Delta$ | sector |
|---|---|---|---|
| $2i\mathrm I_2+E_1$ | $-3$ | $-4$ | $\Sigma_{11}$ |
| $i\mathrm I_2$ | $-1$ | $0$ | $\Sigma_{10}$ |
| $i\mathrm I_2+E_1$ | $0$ | $-4$ | $\Sigma_{01}$ |
| $0$ | $0$ | $0$ | $\Sigma_{00}$ |

**The null cone.** $\{|v|=|\lambda|\}$ is a cone of real dimension three with two nappes; each nappe meets a sphere of radius $r$ in a two-sphere.

**The degenerate locus is the line.** $\Delta=0$ is $v=0$, the trace line $\mathbb{R}(i\mathrm I_2)$.

## The Sector Reads Two Numbers

**The pair.** On the closure both predicates are functions of $(\lambda,r)$ with $r=|v|$:
$$
\det=r^2-\lambda^2,\qquad \Delta=-4r^2 .
$$
The pair labels the unitary orbits, so the sector is a function of the orbit.

**The picture.** In the half-plane $\{(\lambda,r):r\ge0\}$ the vanishing of $\Delta$ is the line $r=0$, the vanishing of $\det$ is the V $r=|\lambda|$, and the two cross at the origin. The line and the V cut the half-plane into eight connected pieces, and the pieces collect into the four sectors:

| piece | sector |
|---|---|
| the origin | $\Sigma_{00}$ |
| the two rays of $r=0$ away from the origin | $\Sigma_{10}$ |
| the two rays of the V away from the origin | $\Sigma_{01}$ |
| the three open pieces | $\Sigma_{11}$ |

**The reading.** Eight pieces and four sectors: a sector is a pair of truth values and not a connected set.

## Two Singular Facts About the Closure

**The closure meets $\Sigma_{10}$ in scalar matrices alone.** $\Sigma_{10}$ has a scalar stratum and a Jordan stratum. The Jordan stratum needs a non-zero nilpotent, and the closure has none: for $A=i\lambda\mathrm I_2+v\cdot E$,
$$
A^2=-(\lambda^2+|v|^2)\mathrm I_2+2i\lambda\,(v\cdot E),
$$
verified, which vanishes only when $\lambda=0$ and $v=0$. So
$$
\mathfrak{u}(2)\cap\Sigma_{10}=\{i\lambda\mathrm I_2:\lambda\neq0\},
$$
the scalar stratum only.

**No non-zero square-zero element.** The same display: a real vector of zero length is the zero vector, and the scalar part adds a positive square. The non-zero nilpotents of $M_2(\mathbb{C})$ lie outside the skew space.

## The Closure Meets All Four

| space | $\dim_\mathbb{R}$ | sectors met |
|---|---|---|
| centre $\mathbb{C}\mathrm I_2$ | $2$ | $\Sigma_{10}$, $\Sigma_{00}$ |
| plane $\mathbb{C}P$ | $2$ | $\Sigma_{01}$, $\Sigma_{00}$ |
| ideal $M_2P$ | $4$ | $\Sigma_{01}$, $\Sigma_{00}$ |
| skew space $\mathfrak{u}(2)$ | $4$ | all four |

**Why the closure and not a carrier.** On each carrier the two conditions are dependent: on the centre $\Delta$ vanishes identically, on the plane $\det$ does, and on the carrier they are proportional. Four cells need two independent conditions, and the closure supplies them.

**The two loci cross once.** The null cone and the trace line meet at the origin alone, which is why the count of sectors is four and not fewer.

## Worked Example

**The axis-free pair.** $A=2i\mathrm I_2+E_1=\begin{pmatrix}2i&-i\\-i&2i\end{pmatrix}$: $\det=-3$, $\tau=4i$, $\Delta=-4$, sector $\Sigma_{11}$; eigenvalues $i(2\pm1)$, that is $i$ and $3i$.

**The same matrix with the trace halved.** $A=i\mathrm I_2+E_1$: $\det=0$, $\Delta=-4$, eigenvalues $0$ and $2i$, sector $\Sigma_{01}$.

**A scalar.** $A=i\mathrm I_2$: $\det=-1$, $\Delta=0$, eigenvalue $i$ twice, sector $\Sigma_{10}$.

## Where $n=2$ Differs

**The orbit space.** At $n=2$ the orbit space of the conjugation on $\mathfrak{u}(2)$ is the half-plane of the pair $(\lambda,r)$, and the sector picture is a half-plane cut by a line and a V. At order $n$ the orbit invariants are the $n$ eigenvalues on the imaginary axis, the orbit space has dimension $n-1$, and the two loci are two hypersurfaces in it; the count of connected pieces grows with $n$.

**The absence of nilpotents.** At $n=2$ a non-zero nilpotent in the skew space is impossible. At order $n$ the same argument holds with the sum of $n$ squares, and the skew space of a real form of signature $(p,q)$ does contain non-zero nilpotents when both $p$ and $q$ are positive; the real skew matrices are the case where none occurs.

**What does not differ.** The coincidence of the two predicates on the traceless part holds at every order only in the sense that both are decided by the vector part; the proportionality by a constant is particular to $n=2$.

## Summary

On the carrier $\det=|v|^2$ and $\Delta=-4|v|^2$ vanish together, so the carrier meets only $\Sigma_{11}$ away from the origin and $\Sigma_{00}$ at it. On the closure $\det=|v|^2-\lambda^2$ and $\Delta=-4|v|^2$ separate, and all four sectors occur: the open rest in $\Sigma_{11}$, the trace line minus the origin in $\Sigma_{10}$, the null cone minus its apex in $\Sigma_{01}$, and the origin in $\Sigma_{00}$, of real dimensions $4,1,3,0$.

The closure meets $\Sigma_{10}$ in scalar matrices alone and contains no non-zero nilpotent, since $A^2=-(\lambda^2+|v|^2)\mathrm I_2+2i\lambda(v\cdot E)$. In the orbit half-plane the sector is read from the pair $(\lambda,|v|)$ cut by the line $r=0$ and the V $r=|\lambda|$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathfrak{su}(2)$ | the carrier, the skew traceless part |
| $\mathfrak{u}(2)=\mathbb{R}(i\mathrm I_2)\oplus\mathfrak{su}(2)$ | the closure |
| $\lambda,\ v,\ r=\lvert v\rvert$ | the orbit coordinates of the closure |
| $\Delta=\tau^2-4\det$ | the discriminant, $-4\lvert v\rvert^2$ |
| $\Sigma_{ij}$ | the sector with $\det\neq0$ for $i=1$ and $\Delta\neq0$ for $j=1$ |

## Further Reading

- [The Spin-One Anti-Hermitian Subspace and the Sectors of N and Spectral Regularity](the-spin-one-anti-hermitian-subspace-and-the-sectors-of-n-and-spectral-regularity.html), for the source's half-plane picture.
- [Introduction to the Spin-One Anti-Hermitian Subspace in $M_2(\mathbb{C})$](the-spin-one-anti-hermitian-subspace-in-m2c.html), for the space.
- [The Spin-One Anti-Hermitian Subspace and N Norm Regularity in $M_2(\mathbb{C})$](the-spin-one-anti-hermitian-subspace-and-n-norm-regularity-in-m2c.html), for the determinant alone.
- [The Spin-One Anti-Hermitian Subspace and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-one-anti-hermitian-subspace-and-spectral-regularity-in-m2c.html), for the discriminant alone.
- [The N-Regular, Spectrally Degenerate Sector](the-n-regular-spectrally-degenerate-sector.html), for the strata of $\Sigma_{10}$.
- [The Spin-Zero Centre Subspace and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-and-the-sectors-of-n-and-spectral-regularity-in-m2c.html), for the same question on the centre.
