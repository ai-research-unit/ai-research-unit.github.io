# __The Spin-Zero Centre Subspace and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$__

## Introduction

**The question.** The two predicates are $\det A\neq0$ and $\Delta\neq0$. Which of the four sectors cut by them does the centre meet, in what stratum, and why is the pattern the same as in the biquaternion algebra?

**Why it is the same statement.** This is the in-depth matrix reading of [The Spin-Zero Centre Subspace and the Sectors of N and Spectral Regularity](the-spin-zero-centre-subspace-and-the-sectors-of-n-and-spectral-regularity.html). There the predicates are $N\neq0$ and $B^2\neq0$; here they are $\det A\neq0$ and $\Delta\neq0$, with $N=\det A$ and $B^2=-\tfrac14\Delta$. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. The identity $N-B^2=Q_t^2$, read as $\det A-\left(\det A-\tfrac14\tau^2\right)=\tfrac14\tau^2$. The four intersections of the centre with the four sectors. That the intersection with $\Sigma_{10}$ is exactly the scalar stratum, so no central element is a Jordan element. The table of $N-B^2$ across the three carriers. Invariance of the sectors under scaling and under unitary conjugation, and the orbit reading. The carrier table.

**What the article does not do.** It does not re-derive the two predicates separately, which are [The Spin-Zero Centre Subspace and N Norm Regularity in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-and-n-norm-regularity-in-m2c.html) and [The Spin-Zero Centre Subspace and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-and-spectral-regularity-in-m2c.html); it does not treat the sectors on the other two carriers, which are [The Spin-Half Bispinors and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinors-and-the-sectors-of-n-and-spectral-regularity-in-m2c.html) and [The Spin-One Anti-Hermitian Subspace and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-one-anti-hermitian-subspace-and-the-sectors-of-n-and-spectral-regularity-in-m2c.html).

**Conventions.** $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$; $Q_t=\tfrac12\operatorname{tr}A=\tfrac12\tau$; $N=\det A$; $B^2=\det A-\tfrac14\tau^2$; $\Delta=\tau^2-4\det A=-4B^2$. The sector $\Sigma_{ij}$ is given by $\det\neq0$ for $i=1$ and $\Delta\neq0$ for $j=1$.

**Boundaries.** The subspace is [Introduction to the Spin-Zero Centre Subspace in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-in-m2c.html). The definitions of the sectors are [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html). The dictionary is [The Pauli Representation : Operators](m2c-pauli-representation-operators.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html).

**Letters.** $A$ a matrix, $\tau$ its trace, $\lambda=\tau/2$ the scalar coordinate, $N$ a nilpotent matrix, $P$ a rank-one projection.

## The Predicates, in the $2\times2$ Display

**The norm and the square of the traceless part.**
$$
N(A)=\det A,\qquad B^2(A)=\det A-\tfrac14(\operatorname{tr}A)^2,\qquad \Delta=-4B^2 .
$$
All three are polynomials in the two elementary symmetric functions $\tau$ and $\delta=\det A$.

**The arrays of the two strata.**
$$
\lambda\mathrm I_2=\begin{pmatrix}\lambda&0\\0&\lambda\end{pmatrix},
\qquad
\lambda(\mathrm I_2+N)=\begin{pmatrix}\lambda&\lambda\\0&\lambda\end{pmatrix},
\qquad
N=\begin{pmatrix}0&1\\0&0\end{pmatrix},
$$
with $N^2=0$ and $N\neq0$, so the second array has minimal polynomial $(x-\lambda)^2$ and is not diagonalisable.

**The identity.**
$$
N-B^2=\tfrac14\tau^2=Q_t^2 ,
$$
verified on a hundred random matrices to better than $10^{-14}$.

**The sectors.**

| sector | condition | name |
|---|---|---|
| $\Sigma_{11}$ | $\det\neq0$, $\Delta\neq0$ | doubly regular |
| $\Sigma_{10}$ | $\det\neq0$, $\Delta=0$ | invertible with repeated eigenvalue |
| $\Sigma_{01}$ | $\det=0$, $\Delta\neq0$ | singular, distinct eigenvalues |
| $\Sigma_{00}$ | $\det=0$, $\Delta=0$ | doubly degenerate |

**The strata of $\Sigma_{10}$.** The **scalar stratum** is $\Sigma_{10}^{\mathrm s}=\{\lambda\mathrm I_2:\lambda\neq0\}$: minimal polynomial of degree one. The **Jordan stratum** is $\Sigma_{10}^{\mathrm J}=\{\lambda(\mathrm I_2+N):\lambda\neq0,\ N\neq0,\ N^2=0\}$: minimal polynomial $(x-\lambda)^2$.

## The Centre and the Two Predicates

**The determinant.** $\det(\lambda\mathrm I_2)=\lambda^2$, non-zero exactly for $\lambda\neq0$.

**The discriminant.** $\Delta(\lambda\mathrm I_2)=(2\lambda)^2-4\lambda^2=0$ identically, because the traceless part vanishes.

**The spectrum.** $\{\lambda,\lambda\}$: one value, algebraic multiplicity two, eigenspace all of $\mathbb{C}^2$.

## The Four Intersections

### The Sector $\Sigma_{11}$

**The statement.** $\mathbb{C}\mathrm I_2\cap\Sigma_{11}=\varnothing$, since $\Delta=0$ at every central matrix, the identity included. The identity of the algebra is not a generic element: it has a double eigenvalue.

### The Sector $\Sigma_{10}$

**The statement.** $\mathbb{C}\mathrm I_2\cap\Sigma_{10}=\mathbb{C}^{\times}\mathrm I_2$.

**The split.** $\mathbb{C}\mathrm I_2=\mathbb{C}^{\times}\mathrm I_2\sqcup\{0\}$: the punctured line in $\Sigma_{10}$ and the origin in $\Sigma_{00}$.

**A group inside one sector.** The punctured centre is closed under multiplication and inversion, with inverse $\lambda^{-1}\mathrm I_2$. It is the only carrier on which the elements of one sector form a group.

### The Sector $\Sigma_{01}$

**The statement.** $\mathbb{C}\mathrm I_2\cap\Sigma_{01}=\varnothing$: $\det=0$ forces $\lambda=0$, and there $\Delta=0$ too.

**The reason.** On the centre one predicate is identically false, so the simultaneous conditions of this sector cannot hold.

### The Sector $\Sigma_{00}$

**The statement.** $\mathbb{C}\mathrm I_2\cap\Sigma_{00}=\{0\}$, the zero matrix alone.

**The origin in every closure.** The zero matrix lies in the closure of each sector, since each sector is the complement of a zero locus of a polynomial that vanishes at the origin.

**The table.**

| sector | condition on $\lambda$ | intersection | $\dim_\mathbb{R}$ |
|---|---|---|---|
| $\Sigma_{11}$ | impossible | $\varnothing$ | — |
| $\Sigma_{10}$ | $\lambda\neq0$ | $\mathbb{C}^{\times}\mathrm I_2$ | $2$ |
| $\Sigma_{01}$ | impossible | $\varnothing$ | — |
| $\Sigma_{00}$ | $\lambda=0$ | $\{0\}$ | $0$ |

## The Intersection with the Scalar Stratum

**The identity of the two sets.** $\mathbb{C}\mathrm I_2\cap\Sigma_{10}=\Sigma_{10}^{\mathrm s}$.

**No Jordan element.** The Jordan stratum $\Sigma_{10}^{\mathrm J}$ is met in no point: a central matrix has no nilpotent part, and its minimal polynomial is $x-\lambda$, of degree one.

**The centre is the vertex of the discriminant.** The locus $\{\Delta=0\}$ is a complex hypersurface, singular exactly along $\{\tau^2=4\delta\}$ with zero traceless part, which is the scalar line. So the centre minus the origin is the smooth locus of the hypersurface along the scalar direction.

**Why the stratum and not the sector.** The sector $\Sigma_{10}$ has complex dimension three and two strata. The centre occupies one stratum completely and is the smallest complex subspace that does. A statement that a central matrix lies in $\Sigma_{10}$ would leave open whether it can be defective; it cannot.

## The Difference of the Two Conditions

**On the centre.** $N-B^2=\lambda^2=N$: one predicate is the whole determinant and the other is identically zero.

**On the other two carriers.**

| carrier | $\tau/2$ | $N=\det$ | $B^2$ | $N-B^2$ |
|---|---|---|---|---|
| centre $\mathbb{C}\mathrm I_2$ | $\lambda$ | $\lambda^2$ | $0$ | $\lambda^2$ |
| ideal $M_2P$ | $\lambda$ | $0$ | $-\lambda^2/4$ | $\lambda^2/4$ |
| vector part $\mathfrak{su}(2)$ | $0$ | $\lvert v\rvert^2$ | $\lvert v\rvert^2$ | $0$ |

**The three readings.** On the centre the two predicates are disjoint, one being a square and the other zero; on the ideal they are opposite in sign; on the vector part they coincide. All three are the identity $N-B^2=(\tau/2)^2$ read at three subspaces.

**The check.** Verified on a hundred random elements per carrier: the residuals of $\det(Y\!P)=0$, of $B^2(Y\!P)+\lambda^2/4=0$ and of $\det=|v|^2$ with $\operatorname{tr}=0$ are at the $10^{-15}$ level.

## The Sector Is a Property of the Orbit

**Scaling.** $\det(cA)=c^2\det A$ and $\Delta(cA)=c^2\Delta(A)$ for complex $c$: each sector is a cone with its apex removed, except $\Sigma_{00}$.

**Unitary conjugation.** For $U$ unitary, $\det(UAU^{\dagger})=\det A$ and $\operatorname{tr}(UAU^{\dagger})=\operatorname{tr}A$, so both predicates are preserved. The adjoint action of $\mathrm U(2)$ therefore preserves every sector.

**The orbit of a central matrix.** It is a point, because every unitary fixes a scalar matrix. The sector of a central matrix is a property of the matrix alone.

## The Centre Against the Other Two Carriers

| carrier | sectors met | in $\Sigma_{11}$ | in $\Sigma_{10}$ | in $\Sigma_{01}$ | in $\Sigma_{00}$ |
|---|---|---|---|---|---|
| centre $\mathbb{C}\mathrm I_2$ | two | $\varnothing$ | $\mathbb{C}^{\times}\mathrm I_2$ | $\varnothing$ | $\{0\}$ |
| ideal $M_2P$ | two | $\varnothing$ | $\varnothing$ | $M_2P\setminus\{0\}$ | $\{0\}$ |
| vector part $\mathfrak{su}(2)$ | two | $\mathfrak{su}(2)\setminus\{0\}$ | $\varnothing$ | $\varnothing$ | $\{0\}$ |

**The pattern.** Each carrier meets two sectors, the three regular sectors receive one carrier each, and the only sector all three meet is $\Sigma_{00}$, at the origin.

**The two cones.** The centre lies in the discriminant locus at every point; the ideal lies in the singular locus $\{\det=0\}$ at every point; the vector part lies in neither.

## Where $n=2$ Differs

**The discriminant.** At $n=2$ the discriminant is one complex number and its zero locus is one hypersurface. At order $n$ it is the discriminant of the characteristic polynomial, and the sector structure is stratified by the partitions of $n$.

**The strata.** At $n=2$ the sector $\Sigma_{10}$ has two strata, the scalar one and one Jordan type (a single block). At order $n$ it has $n$ Jordan types, and the scalar stratum is one of them.

**What does not differ.** The identity $N-B^2=(\tau/2)^2$, the four sectors, and the fact that a central element lies in $\Sigma_{10}$ away from the origin are the same at every order.

## Summary

The centre meets only two sectors: the punctured line in $\Sigma_{10}$ and the origin in $\Sigma_{00}$. The determinant on the centre is $\lambda^2$ and the discriminant is zero identically, because the traceless part vanishes.

The intersection with $\Sigma_{10}$ is exactly the scalar stratum: no central matrix is a Jordan matrix. In the identity $N-B^2=(\tau/2)^2$ the centre is the case where the two predicates are farthest apart, one being the whole determinant and the other zero; on the ideal they are opposite in sign, and on the vector part they coincide.

Both predicates are homogeneous of degree two and invariant under unitary conjugation, so each sector is a union of adjoint orbits. The adjoint orbit of a central matrix is a point.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tau,\ \delta=\det A$ | the two elementary symmetric functions |
| $\lambda=\tau/2$ | the scalar coordinate |
| $\Delta=\tau^2-4\delta$ | the discriminant |
| $\Sigma_{ij}$ | the sector with $\det\neq0$ iff $i=1$ and $\Delta\neq0$ iff $j=1$ |
| $\Sigma_{10}^{\mathrm s},\ \Sigma_{10}^{\mathrm J}$ | the scalar and Jordan strata |
| $N$ | a nilpotent matrix, $N^2=0$ |

## Further Reading

- [The Spin-Zero Centre Subspace and the Sectors of N and Spectral Regularity](the-spin-zero-centre-subspace-and-the-sectors-of-n-and-spectral-regularity.html), for the source's four intersections and its stratum argument.
- [The Spin-Zero Centre Subspace and N Norm Regularity in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-and-n-norm-regularity-in-m2c.html), for the determinant on the centre.
- [The Spin-Zero Centre Subspace and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-and-spectral-regularity-in-m2c.html), for the discriminant on the centre.
- [The Spin-Half Bispinors and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinors-and-the-sectors-of-n-and-spectral-regularity-in-m2c.html), for the sector $\Sigma_{01}$ and the ideal.
- [The Spin-One Anti-Hermitian Subspace and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-one-anti-hermitian-subspace-and-the-sectors-of-n-and-spectral-regularity-in-m2c.html), for the sector $\Sigma_{11}$ and the vector part.
