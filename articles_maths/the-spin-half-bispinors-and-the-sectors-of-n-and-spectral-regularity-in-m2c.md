# __The Spin-Half Bispinors and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$__

## Introduction

**The question.** The spin-half family has three levels: the plane, the ideal it generates, and the sum of the two ideals. Which of the four sectors cut by $\det\neq0$ and $\Delta\neq0$ does each level meet?

**Why it is the same statement.** This is the in-depth matrix reading of [The Spin-Half Bispinors and the Sectors of N and Spectral Regularity](the-spin-half-bispinors-and-the-sectors-of-n-and-spectral-regularity.html). The dictionary is $N=\det A$ and $B^2=\det A-\tfrac14(\operatorname{tr}A)^2$; the three levels are $\mathbb{C}P\subset M_2P\subset M_2$. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. The two predicates and the four sectors in matrix terms. The plane: two sectors, the punctured plane in $\Sigma_{01}$ and the origin in $\Sigma_{00}$. The ideal: the same two sectors, with a real plane of square-zero elements in $\Sigma_{00}$. The bispinor: all four sectors, with explicit matrices and dimensions. That the two indices come from two different places. That the axis is a parameter and the pattern is the same at every axis.

**What the article does not do.** It does not treat the determinant or the discriminant on these spaces one at a time, which are [The Spin-Half Bispinors and N Norm Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinors-and-n-norm-regularity-in-m2c.html) and [The Spin-Half Bispinors and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinors-and-spectral-regularity-in-m2c.html); it does not treat the Dirac decomposition of a general element, which is [Spinors and Dirac Spinors in the Biquaternion Algebra in $M_2(\mathbb{C})$](spinors-and-dirac-spinors-in-the-biquaternion-algebra-in-m2c.html).

**Conventions.** $Q_t=\tfrac12\tau$, $N=\det$, $B^2=\det-\tfrac14\tau^2$, $\Delta=-4B^2$. The sector $\Sigma_{ij}$ has $\det\neq0$ for $i=1$ and $\Delta\neq0$ for $j=1$. The axis is a unit complex vector $n$ and $P=\tfrac12(\mathrm I_2+n\cdot\sigma)$.

**Boundaries.** The predicates are defined in [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html). The strata inside each sector are [The N-Degenerate, Spectrally Regular Sector](the-n-degenerate-spectrally-regular-sector.html) and [The N-Degenerate, Spectrally Degenerate Sector](the-n-degenerate-spectrally-degenerate-sector.html). The same question on the centre is [The Spin-Zero Centre Subspace and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-and-the-sectors-of-n-and-spectral-regularity-in-m2c.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** $\alpha,\beta$ the coordinates of an element of the ideal in the basis $(P,\nu)$; $\tau$ the trace; $\Delta$ the discriminant; $\nu=E_2P$.

## The Two Predicates and the Four Sectors

**The predicates.**
$$
\det A=0\iff A\ \text{singular},\qquad \Delta(A)=\tau(A)^2-4\det A=0\iff A\ \text{has a repeated eigenvalue}.
$$

**The four sectors.**

| sector | conditions | name |
|---|---|---|
| $\Sigma_{11}$ | $\det\neq0$, $\Delta\neq0$ | doubly regular |
| $\Sigma_{10}$ | $\det\neq0$, $\Delta=0$ | invertible, repeated eigenvalue |
| $\Sigma_{01}$ | $\det=0$, $\Delta\neq0$ | singular, distinct eigenvalues |
| $\Sigma_{00}$ | $\det=0$, $\Delta=0$ | nilpotent shifted to trace zero |

**The collapsing lemma.** On a set where the determinant vanishes only the two sectors with first index zero occur. The plane and the ideals are such sets.

## The Plane and the Sectors

**The plane.** $\mathbb{C}P$, real dimension two, with $P=\tfrac12(\mathrm I_2+n_1E_1+n_2E_2+n_3E_3)$.

**The two values.**
$$
\det(\lambda P)=0,\qquad \Delta(\lambda P)=\lambda^2,\qquad B^2(\lambda P)=-\frac{\lambda^2}{4},
$$
verified exactly.

**The intersections.**

| sector | condition on $\lambda$ | intersection | $\dim_\mathbb{R}$ |
|---|---|---|---|
| $\Sigma_{11}$ | impossible | $\varnothing$ | — |
| $\Sigma_{10}$ | impossible | $\varnothing$ | — |
| $\Sigma_{01}$ | $\lambda\neq0$ | $\mathbb{C}^{\times}P$ | $2$ |
| $\Sigma_{00}$ | $\lambda=0$ | $\{0\}$ | $0$ |

**The two exclusions are one.** Both regular sectors need an invertible element, and no multiple of a rank-one projection is invertible.

**The spectrum.** For $\lambda\neq0$ the spectrum is $\{0,\lambda\}$: distinct, with eigenvector $P$ for $\lambda$.

**The apex.** The origin is the only doubly degenerate point of the plane. The null cone meets the plane in the whole plane and the spectral cone in one point of it.

## The Ideal and the Sectors

**The coordinates.** $Y=\alpha P+\beta\nu$ with $\nu=E_2P$; $\tau(Y)=\alpha$ because $\tau(\nu)=0$.

**The two values.**
$$
\det Y=0,\qquad \Delta(Y)=\alpha^2,\qquad B^2(Y)=-\frac{\alpha^2}{4}.
$$

**One number decides the sector.** $Y\in\Sigma_{01}$ when $\alpha\neq0$ and $Y\in\Sigma_{00}$ when $\alpha=0$.

| sector | condition on $\alpha$ | intersection | $\dim_\mathbb{R}$ |
|---|---|---|---|
| $\Sigma_{11}$ | impossible | $\varnothing$ | — |
| $\Sigma_{10}$ | impossible | $\varnothing$ | — |
| $\Sigma_{01}$ | $\alpha\neq0$ | the ideal minus the line $\mathbb{C}\nu$ | $4$ |
| $\Sigma_{00}$ | $\alpha=0$ | $\mathbb{C}\nu$ | $2$ |

**The degenerate line is the square-zero locus.** On the ideal $Y^2=\tau(Y)Y$, so $Y^2=0$ exactly when $\alpha=0$. Verified on a hundred elements to $9\cdot10^{-16}$.

**The degenerate line is not the carrier.** $\mathbb{C}P$ is spanned by a projection of trace one and $\mathbb{C}\nu$ by a nilpotent of trace zero, so they meet only at the origin.

**The closure repairs invariance and not invertibility.** The ideal is a left ideal, invariant under every left multiplication; it stays inside the singular locus.

## The Bispinor and the Sectors

**The bispinor is the algebra.** $M_2=M_2P\oplus M_2P_{\perp}$, and the determinant is the pairing: $\det X=2B(X_+,X_-)$.

**Witnesses.** Verified:

| sector | witness | $\tau$ | $\det$ | $\Delta$ |
|---|---|---|---|---|
| $\Sigma_{11}$ | $\mathrm I_2+2E_1=\begin{pmatrix}1&-2i\\-2i&1\end{pmatrix}$ | $2$ | $5$ | $-16$ |
| $\Sigma_{10}$ | $\mathrm I_2$ | $2$ | $1$ | $0$ |
| $\Sigma_{01}$ | $P$ | $1$ | $0$ | $1$ |
| $\Sigma_{00}$ | $\begin{pmatrix}0&1\\0&0\end{pmatrix}$ | $0$ | $0$ | $0$ |

**The dimensions.** $\Sigma_{11}$ is open and dense, of real dimension $8$; $\Sigma_{10}$ and $\Sigma_{01}$ are of real dimension $6$; $\Sigma_{00}$ is of real dimension $4$.

**The sector $\Sigma_{10}$ in matrix terms.** An invertible matrix with a repeated eigenvalue is
$$
A=\lambda\left(\mathrm I_2+N\right),\qquad \lambda\neq0,\quad N^2=0,
$$
with $N$ arbitrary of square zero, including $N=0$. The eigenvalues are $\lambda$ twice, and $\det A=\lambda^2$. This is the Jordan block $\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix}$ and its conjugates, together with the scalars.

**The sector $\Sigma_{00}$ in matrix terms.** $\det=0$ and $\tau=0$ are $X^2=0$ by Cayley–Hamilton, so $\Sigma_{00}$ is the nilpotent cone, a single conjugacy class together with the origin, of complex dimension two.

**The sector $\Sigma_{01}$ in matrix terms.** The singular matrices with distinct eigenvalues: rank one with non-zero trace, that is $A=uv^{\dagger}$ with $v^{\dagger}u\neq0$.

## The Pairing Decides the First Index

**The statement.** The first index is $\det X=2B(X_+,X_-)$ and the second is $\Delta(X)$.

**Three pairs of witnesses.** $P$ and $3\nu$ have the same first index (zero) and different second ($1$ and $0$). $\mathrm I_2$ and $\mathrm I_2+2E_1$ have the same first index (non-zero) and different second ($0$ and $-16$).

**The pairing at the carrier.** On the plane the two parts are $\lambda P$ and $0$: one part is absent, and the pairing vanishes with it.

## The Axis Is a Parameter

**The invariance.** For unitary $U$, $\det(UAU^{\dagger})=\det A$ and $\tau(UAU^{\dagger})=\tau(A)$, so $\Delta$ is preserved and each sector is carried to itself. Since any two axes are related by a unitary element, the pattern is the same at every axis.

**What the invariance does not say.** The plane is not invariant under the whole group; only under the rotations about its own axis. That is why the closure exists.

## The Three Levels Compared

| level | $\dim_\mathbb{R}$ | sectors met | $\Sigma_{01}$ | $\Sigma_{00}$ |
|---|---|---|---|---|
| plane $\mathbb{C}P$ | $2$ | two | $\mathbb{C}^{\times}P$ | $\{0\}$ |
| ideal $M_2P$ | $4$ | two | $\tau\neq0$ | $\mathbb{C}\nu$ |
| algebra $M_2$ | $8$ | four | $\det=0$, $\Delta\neq0$ | $X^2=0$ |

**The growth.** The first closure enlarges the doubly degenerate part from a point to a real plane, and it removes exactly that plane from $\Sigma_{01}$. The second closure restores invertibility and with it the two regular sectors.

## Worked Example

**The axis $e_3$.** $P=\operatorname{diag}(1,0)$, $\nu=\begin{pmatrix}0&0\\ i&0\end{pmatrix}$.

**The plane.** $2P=\operatorname{diag}(2,0)$: $\det=0$, $\Delta=4$, sector $\Sigma_{01}$.

**The ideal.** $Y=2P+3\nu=\begin{pmatrix}2&0\\3i&0\end{pmatrix}$: $\det=0$, $\tau=2$, sector $\Sigma_{01}$. And $3\nu$: sector $\Sigma_{00}$, $Y^2=0$.

**The bispinor.** $X=\begin{pmatrix}2&1\\0&2\end{pmatrix}$: $\tau=4$, $\det=4$, $\Delta=0$, sector $\Sigma_{10}$, and indeed $X=2(\mathrm I_2+N)$ with $N=\begin{pmatrix}0&1/2\\0&0\end{pmatrix}$, $N^2=0$.

## Where $n=2$ Differs

**The number of sectors.** At $n=2$ the two predicates are two scalar conditions on four complex coordinates, and the four sectors have real dimensions $8,6,6,4$. At order $n$ the second predicate is no longer a single number: distinct eigenvalues are the complement of the discriminant variety, of codimension one, and the doubly degenerate locus splits into many strata indexed by the Jordan type.

**The dimensions.** At $n=2$ the singular locus has complex dimension three and the repeated-eigenvalue locus has complex dimension three as well; their intersection, the nilpotent cone, has complex dimension two. At order $n$ the same three dimensions are $n^2-1$, $n^2-1$ and $n^2-n$.

**What does not differ.** On the plane and on the ideal the pattern is the same at every order: the determinant vanishes, and the sector is decided by whether the trace vanishes.

## Summary

The plane meets two sectors: the punctured plane lies in $\Sigma_{01}$ and the origin in $\Sigma_{00}$. The ideal meets the same two, with the degenerate part a real plane $\mathbb{C}E_2P$ that is exactly the square-zero locus, since on the ideal $Y^2=\tau(Y)Y$. The bispinor is the algebra and meets all four, with witnesses $\mathrm I_2+2E_1$, $\mathrm I_2$, $P$ and the nilpotent unit, and real dimensions $8,6,6,4$.

The first index is the pairing $\det X=2B(X_+,X_-)$ and the second is $\Delta$; the two are independent, and the sector $\Sigma_{10}$ is the set of matrices $\lambda(\mathrm I_2+N)$ with $N^2=0$. Both predicates are invariant under conjugation by a unitary element, so the description is the same at every axis.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P=\tfrac12(\mathrm I_2+n\cdot\sigma)$ | the rank-one projection, generator of the plane |
| $\nu=E_2P$ | the nilpotent generator of the degenerate line |
| $\alpha,\beta$ | coordinates of an ideal element in $(P,\nu)$ |
| $\Delta=\tau^2-4\det$ | the discriminant |
| $\Sigma_{ij}$ | the sector with $\det\neq0$ for $i=1$ and $\Delta\neq0$ for $j=1$ |

## Further Reading

- [The Spin-Half Bispinors and the Sectors of N and Spectral Regularity](the-spin-half-bispinors-and-the-sectors-of-n-and-spectral-regularity.html), for the source's three-level treatment.
- [Introduction to the Spin-Half Bispinors Spaces in $M_2(\mathbb{C})$](the-spin-half-bispinor-spaces-in-m2c.html), for the definition of the three levels.
- [The Spin-Half Bispinors and N Norm Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinors-and-n-norm-regularity-in-m2c.html), for the determinant alone.
- [The Spin-Half Bispinors and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinors-and-spectral-regularity-in-m2c.html), for the discriminant alone.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html), for the strata inside the sectors.
- [The Spin-One Anti-Hermitian Subspace and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-one-anti-hermitian-subspace-and-the-sectors-of-n-and-spectral-regularity-in-m2c.html), for the same question on the vector part.
