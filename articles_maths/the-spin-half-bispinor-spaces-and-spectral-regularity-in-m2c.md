# __The Spin-Half Bispinors and Spectral Regularity in $M_2(\mathbb{C})$__

## Introduction

**The question.** The spin-half carrier is a null plane. Is it also spectrally degenerate, and where inside an ideal do the two eigenvalues coincide?

**Why it is the same statement.** This is the in-depth matrix reading of [The Spin-Half Bispinors and Spectral Regularity](the-spin-half-bispinor-spaces-and-spectral-regularity.html). The source's second predicate is $B^2=Q_x^2+Q_y^2+Q_z^2\neq0$; in the display it is $\Delta=\tau^2-4\det=-4B^2\neq0$, and the carrier is $\mathbb{C}P$. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. That $B^2(\lambda P)=-\lambda^2/4$, so the plane is spectrally regular away from the origin. That the spectrum of $\lambda P$ is $\{0,\lambda\}$ and that of $P$ is $\{0,1\}$. That every element of an ideal has spectrum $\{0,\tau\}$, that the degenerate elements are those of trace zero, that they form a complex line, and that they are exactly the square-zero elements. The comparison with the centre and the vector part.

**What the article does not do.** It does not treat the determinant on the same spaces, which is [The Spin-Half Bispinors and N Norm Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinor-spaces-and-n-norm-regularity-in-m2c.html); it does not treat the sector table in full, which is [The Spin-Half Bispinors and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinor-spaces-and-the-sectors-of-n-and-spectral-regularity-in-m2c.html).

**Conventions.** $Q_t=\tfrac12\operatorname{tr}A$, $N=\det A$, $B^2=\det A-\tfrac14(\operatorname{tr}A)^2$, $\Delta=-4B^2$. The eigenvalues are $\lambda_\pm=\tfrac12\tau\pm\tfrac12\sqrt{\Delta}$. The basis of the ideal is $(P,E_2P)$ with $E_2=-i\sigma_2$, and $E_2P$ at the axis $e_3$ is the matrix with the single entry $i$ in position $(2,1)$.

**The trace is the scalar coordinate.** $Q_t(A)=\tfrac12\tau(A)$; the source's "$Q_t=0$" is "$\tau=0$" in the display.

**Boundaries.** The spaces are [Introduction to the Spin-Half Bispinors Spaces in $M_2(\mathbb{C})$](the-spin-half-bispinor-spaces-in-m2c.html). The general spectral theory is [The Spectrum](the-spectrum-of-a-biquaternion.html). The nilpotent classification of matrices is used in [The Spin-Zero Centre Subspace and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-and-spectral-regularity-in-m2c.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** $\tau$ the trace, $\Delta$ the discriminant, $Y$ an element of an ideal, $\nu=E_2P$ the square-zero generator.

## The Two Eigenvalues

**The quadratic relation.** Every $2\times2$ matrix satisfies $A^2-\tau A+\det A\,\mathrm I_2=0$, so
$$
\lambda_\pm=\tfrac12\left(\tau\pm\sqrt{\Delta}\right),\qquad \Delta=\tau^2-4\det A .
$$
Spectral regularity is $\Delta\neq0$, that is $B^2\neq0$.

**The sum and the product.** The pair is fixed by the sum $\tau$ and the product $\det$; coincident roots are exactly $\tau^2=4\det$.

## The Plane

**The square of the vector part.** For every $\lambda$,
$$
B^2(\lambda P)=-\frac{\lambda^2}{4},\qquad \Delta(\lambda P)=\lambda^2,
$$
verified exactly. In coordinates $\lambda P=\tfrac\lambda2\mathrm I_2+\tfrac{\lambda i}{2}E_3$, so $B^2=(\tfrac{\lambda i}{2})^2=-\tfrac{\lambda^2}{4}$.

**The plane is spectrally regular away from the origin.** $\Delta=\lambda^2$ vanishes only at $\lambda=0$, so $\mathbb{C}P\cap\{\Delta=0\}=\{0\}$.

**The spectrum.** $\operatorname{spec}(\lambda P)=\{0,\lambda\}$ for $\lambda\neq0$, with distinct eigenvalues: the eigenvector of $\lambda$ is $P$ itself, and the eigenvector of $0$ is any vector killed by $P$.

**The sharp reading.** Every non-zero element of the plane is singular and spectrally regular, hence in $\Sigma_{01}$: the two predicates fail at opposite elements.

## The Projection

**The spectrum of $P$.** $\{0,1\}$, verified: trace one and determinant zero, and the roots are $0$ and $1$.

**The idempotent relation read spectrally.** A pair with sum $\tau=1$ and product $\det=0$ is $\{0,1\}$. The spectral content of $P^2=P$ is that one eigenvalue is zero and the other one; the splitting of the module as $M_2=M_2P\oplus M_2P_{\perp}$ is the same statement in another language.

**The same element is singular.** $\det P=0$ with distinct eigenvalues: a product vanishes when one factor does.

## Inside the Ideal

**One eigenvalue always vanishes.** For $Y\in M_2P$, $\det Y=0$, so
$$
\operatorname{spec}(Y)=\{0,\tau(Y)\}.
$$

**The degenerate elements.** An element of the ideal is spectrally degenerate exactly when $\tau(Y)=0$, since $\Delta=\tau^2$.

**The degenerate locus is a complex line.** In the basis $(P,\nu)$ of the ideal, with $\nu=E_2P$,
$$
Y=\alpha P+\beta\nu,\qquad \tau(Y)=\alpha,
$$
because $\tau(\nu)=0$. So the degenerate elements are the multiples of $\nu$:
$$
S_+\cap\{\Delta=0\}=\mathbb{C}\nu,\qquad \nu=\begin{pmatrix}0&0\\ i&0\end{pmatrix}\ (n=e_3),
$$
a real plane, verified: $\tau(\nu)=0$, $\nu^2=0$, $\det\nu=0$.

**The degenerate elements are exactly the square-zero elements.** On the ideal the quadratic relation reduces to $Y^2=\tau(Y)Y$, so $Y^2=0$ exactly when $\tau(Y)=0$. Verified on a hundred random elements of the ideal: the residual of $Y^2-\tau(Y)Y$ is below $9\cdot10^{-16}$.

**The carrier is not the degenerate locus.** $\mathbb{C}P$ is spanned by an element of trace one, $\mathbb{C}\nu$ by an element of trace zero, so the two lines meet only at the origin.

**One line per axis, two families.** The carriers and the degenerate lines are different families, both indexed by the axis; the generator of the degenerate line is nilpotent and the generator of the carrier is a projection.

## The Bispinor Space

**The predicate.** $X$ is spectrally degenerate exactly when $\Delta(X)=0$. This is one complex equation in the four complex coordinates, hence two real equations, and its zero set has real dimension $6$ in the real eight.

**The degenerate set is not small.** It contains both ideals, every element with a vanishing part, and the nilpotent cone. What it does not contain is a generic element of $M_2$.

**The bispinor read is the regular case.** For a generic matrix the two eigenvalues differ, and that is the case the full algebra supplies.

## The Three Carriers Compared

| carrier | $\Delta$ on it | degenerate locus in it |
|---|---|---|
| centre $\mathbb{C}\mathrm I_2$ | $0$ | the whole centre |
| plane $\mathbb{C}P$ | $\lambda^2$ | $\{0\}$ |
| skew-adjoint part $\mathfrak{su}(2)$, real $v$ | $-4\lvert v\rvert^2$ | $\{0\}$ |

**Where the carriers sit.** The plane away from the origin is $\Sigma_{01}$, the centre is $\Sigma_{10}$, the vector part is $\Sigma_{11}$. The sector $\Sigma_{00}$ is met by no carrier except at the origin, but the degenerate line of each ideal lies in it, except at the origin.

## Worked Example

**The axis $e_3$.** $\nu=E_2P=\begin{pmatrix}0&0\\ i&0\end{pmatrix}$, and $Y=2P+3\nu=\begin{pmatrix}2&0\\3i&0\end{pmatrix}$: $\tau=2$, $\det=0$, spectrum $\{0,2\}$, spectrally regular.

**The degenerate element.** $Y=3\nu$: $\tau=0$, $\det=0$, spectrum $\{0,0\}$, and $Y^2=0$.

**A bispinor.** $X=\operatorname{diag}(2,3)$: $\tau=5$, $\det=6$, $\Delta=1$, distinct eigenvalues $2$ and $3$.

## Where $n=2$ Differs

**The number of eigenvalues.** At $n=2$ there are two eigenvalues and $\Delta$ is a single complex number. At order $n$ there are $n$ eigenvalues, the discriminant is replaced by the full characteristic polynomial, and "spectrally regular" becomes "distinct roots", a condition of codimension one in the coefficient space but of a different nature: the discriminant is the resultant of the polynomial and its derivative.

**The degenerate locus of an ideal.** At $n=2$ the elements of an ideal with $\tau=0$ are exactly the square-zero ones, because the ideal has dimension two and one eigenvalue is always zero. At order $n$ an element of a minimal left ideal has rank one, so $n-1$ eigenvalues vanish, and the remaining one is the trace; the square-zero condition is again $\tau=0$, and the degenerate locus has complex dimension $n-1$.

**What does not differ.** On the plane $\Delta=\lambda^2$ at every order: a rank-one projection scaled by $\lambda$ has eigenvalues $\lambda$ and zeros.

## Summary

On the plane $B^2=-\lambda^2/4$ and $\Delta=\lambda^2$, so the plane is spectrally regular at every point except the origin, while its determinant vanishes everywhere. The spectrum of $\lambda P$ is $\{0,\lambda\}$ and that of $P$ is $\{0,1\}$.

Inside an ideal every element has spectrum $\{0,\tau\}$; the degenerate elements are those with $\tau=0$, they form the complex line $\mathbb{C}E_2P$ (a real plane), and they are exactly the square-zero elements, since on the ideal $Y^2=\tau(Y)Y$. The carrier and the degenerate line meet only at the origin.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tau(A)$ | the trace, twice the scalar coordinate |
| $\Delta=\tau^2-4\det$ | the discriminant, $-4B^2$ |
| $P,\ P_{\perp}$ | a rank-one projection and its complement |
| $\nu=E_2P$ | the nilpotent generator of the degenerate line of $S_+$ |
| $\alpha,\beta$ | coordinates in the basis $(P,\nu)$ |

## Further Reading

- [The Spin-Half Bispinors and Spectral Regularity](the-spin-half-bispinor-spaces-and-spectral-regularity.html), for the source's eigenvalue computation.
- [The Spin-Half Bispinors and N Norm Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinor-spaces-and-n-norm-regularity-in-m2c.html), for the determinant on the same spaces.
- [The Spin-Half Bispinors and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinor-spaces-and-the-sectors-of-n-and-spectral-regularity-in-m2c.html), for the sector table.
- [The Spectrum](the-spectrum-of-a-biquaternion.html), for the quadratic relation in the biquaternion algebra.
- [The Spin-Zero Centre Subspace and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-and-spectral-regularity-in-m2c.html), for the opposite extreme, where the whole carrier is degenerate.
