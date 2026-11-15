# __The Exponential of a $2\times2$ Matrix and Its Image__

## Introduction

**The exponential of a $2\times2$ complex matrix converges everywhere, always has nonzero determinant, satisfies $\det e^{X}=e^{\operatorname{tr}X}$, and its image is the whole of $\mathrm{GL}_2(\mathbb{C})$.**

The article defines the exponential series at order two, proves the determinant formula, computes the derivative at the origin, proves the surjectivity onto the invertible matrices, describes the period lattice of the exponential and the fibres, and states what the image becomes on the two halves and on the Hermitian space. It assumes *The Spectrum of a $2\times2$ Matrix*, *The Minimal Polynomial and the Two Jordan Regimes of $M_2(\mathbb{C})$* and *The Element: Rank, Trace, Determinant, Characteristic Polynomial at $n=2$*.

It follows the biquaternion account of *The Polar Decomposition of a Biquaternion* for the split into a length and a direction.

## The Series

**Definition.** The **exponential** of a matrix $X$ is

$$
e^{X}=\sum_{k\ge0}\frac{X^{k}}{k!}.
$$

**Proposition.** The series converges for every complex matrix, and the convergence is absolute and uniform on every bounded set of matrices.

**Proof.** With $\|X\|\le R$ the norm of the $k$-th term is at most $R^{k}/k!$, whose sum converges; the comparison is uniform on the set where the bound holds.

**Corollary.** The exponential is a continuous map from the eight-dimensional real space $M_2(\mathbb{C})$ into itself.

**Proof.** It is the uniform limit of the continuous partial sums on every bounded set.

**Corollary.** The exponential of a scalar matrix is the scalar exponential, and the exponential of a diagonal matrix is the diagonal of the exponentials.

**Proof.** The powers of a diagonal matrix are the diagonal powers, and the series is applied entry by entry.

## The Determinant Formula

**Theorem.** For every matrix, $\det e^{X}=e^{\operatorname{tr}X}$.

**Proof.** In a basis where $X$ is upper triangular, $e^{X}$ is upper triangular with the exponentials of the diagonal entries on the diagonal, so the determinant is the product $e^{\lambda_{1}}e^{\lambda_{2}}=e^{\lambda_{1}+\lambda_{2}}=e^{\operatorname{tr}X}$; and by *The Minimal Polynomial and the Two Jordan Regimes of $M_2(\mathbb{C})$* such a basis exists over $\mathbb{C}$.

**Corollary.** The exponential of a matrix is always invertible, and its inverse is the exponential of the negative.

**Proof.** The determinant is a nonzero exponential, and $e^{X}e^{-X}=e^{X-X}=I$ because $X$ commutes with $-X$.

**Corollary.** The exponential lands in $\mathrm{GL}_2(\mathbb{C})$, and it lands in $\mathrm{SL}_2(\mathbb{C})$ on the matrices whose trace lies in $2\pi i\mathbb{Z}$, in particular on every traceless matrix.

**Proof.** The determinant of $e^{X}$ is $e^{\operatorname{tr}X}$, which is one exactly when the trace is a multiple of $2\pi i$, and that holds for every traceless $X$.

## The Derivative at the Origin

**Proposition.** The derivative of the exponential at the origin is the identity, so the exponential is a local diffeomorphism near the zero matrix.

**Proof.** The series is $I+X+O(X^{2})$, so the linear part at the origin is $X\mapsto X$; the inverse function theorem then applies in the eight real dimensions.

**Corollary.** Every matrix near the identity has a unique logarithm near zero.

**Proof.** The local inverse of the exponential at the identity is the logarithm series $\log(I+Y)=Y-\tfrac12Y^{2}+\cdots$, which converges for $\|Y\|<1$.

**Corollary.** The exponential restricted to a small ball around the zero matrix is a homeomorphism onto a neighbourhood of the identity, with the logarithm as its inverse.

**Proof.** The derivative at the origin is the identity, and the logarithm series converges on the open ball of radius one; the two maps are inverse on the two balls by the identity $\exp(\log(I+Y))=I+Y$.

## The Image

**Theorem.** The exponential maps $M_2(\mathbb{C})$ onto $\mathrm{GL}_2(\mathbb{C})$.

**Proof.** Let $A$ be invertible. Over $\mathbb{C}$ it has a basis in which it is diagonal or a single Jordan block, by *The Minimal Polynomial and the Two Jordan Regimes of $M_2(\mathbb{C})$*. In the diagonal case with eigenvalues $\lambda_{1},\lambda_{2}\ne0$ take $X$ diagonal with entries $\log\lambda_{1},\log\lambda_{2}$; in the Jordan case with the eigenvalue $\lambda\ne0$ take $X=(\log\lambda)I+N/\lambda$, and then $e^{X}=\lambda\bigl(I+N/\lambda\bigr)=\lambda I+N$ because $N^{2}=0$. In both cases $e^{X}=A$.

**Corollary.** Every invertible matrix is the exponential of some matrix, so the exponential is surjective onto the group of units.

**Proof.** The theorem treats an arbitrary invertible matrix.

**Corollary.** The exponential is not injective, and its fibres are infinite.

**Proof.** The matrices $X$ and $X+2\pi i\,I$ have the same exponential because the scalar $2\pi i\,I$ commutes with $X$; iterating gives infinitely many preimages of each point.

## The Period Lattice

**Proposition.** The set of matrices $P$ with $e^{P}=I$ is the set of matrices with all eigenvalues in $2\pi i\mathbb{Z}$ and no Jordan part, that is, the diagonalisable matrices whose eigenvalues lie in $2\pi i\mathbb{Z}$.

**Proof.** If $e^{P}=I$ then every eigenvalue of $e^{P}$ is one, so every eigenvalue of $P$ lies in $2\pi i\mathbb{Z}$, and $P$ must be diagonalisable because a Jordan block with a nonzero eigenvalue gives a nontrivial unipotent factor; conversely such a $P$ has $e^{P}=I$ by the spectral mapping.

**Corollary.** The kernel contains the lattice $2\pi i\mathbb{Z}\,I$ and no nonzero nilpotent, so the kernel is not a linear subspace of the space of matrices.

**Proof.** The scalar $2\pi i n\,I$ has $e^{2\pi i n I}=I$; and for $N\ne0$ with $N^{2}=0$ the exponential is $I+2\pi iN$, which differs from $I$. The sum of a matrix in the kernel and a nilpotent is therefore outside the kernel in general.

**Corollary.** If $P$ commutes with $X$ and has all eigenvalues in $2\pi i\mathbb{Z}$ with no Jordan part, then $e^{X+P}=e^{X}$, so the ambiguity of the logarithm contains the addition of every such $P$.

**Proof.** A commuting pair satisfies $e^{X+P}=e^{X}e^{P}$, and $e^{P}=I$ for such a $P$ by the proposition.

## The Two Halves and the Hermitian Space

**Proposition.** The exponential of a Hermitian matrix is Hermitian and positive definite, and the exponential of an anti-Hermitian matrix is unitary.

**Proof.** If $X^{*}=\pm X$ then $(e^{X})^{*}=e^{X^{*}}=e^{\pm X}$, which is $e^{X}$ in the Hermitian case and $(e^{X})^{-1}$ in the anti-Hermitian case; and the eigenvalues of $e^{X}$ in the Hermitian case are the exponentials of the real eigenvalues, hence positive.

**Corollary.** The exponential of a real symmetric matrix is real symmetric positive definite, and the exponential of a real antisymmetric matrix is a rotation.

**Proof.** The real symmetric case is the Hermitian case under conjugation by a real basis, and the real antisymmetric matrix is anti-Hermitian with a real form.

**Corollary.** The exponential carries the Hermitian space onto the positive definite cone, and the map is a homeomorphism onto that cone.

**Proof.** The logarithm of a positive definite matrix is Hermitian, and the two maps are continuous and inverse to each other on the cone.

## Summary

The exponential of a $2\times2$ complex matrix is defined by an everywhere convergent series, and it satisfies $\det e^{X}=e^{\operatorname{tr}X}$, so its values are always invertible. Its derivative at the origin is the identity, so it is a local diffeomorphism near zero, and it is surjective onto $\mathrm{GL}_2(\mathbb{C})$: the logarithm is built from the diagonal case and the Jordan case.

The exponential is far from injective: the scalar $2\pi iI$ lies in its kernel together with the diagonal matrices with integer imaginary eigenvalues, and adding $2\pi iI$ to any matrix does not change its exponential. On the Hermitian space the exponential is a homeomorphism onto the positive definite cone, and on the anti-Hermitian space it lands in the unitary group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e^{X}$ | the exponential series |
| $\mathrm{GL}_2(\mathbb{C})$ | the invertible matrices |
| $\mathrm{SL}_2(\mathbb{C})$ | the matrices of determinant one |
| $N$ | a nilpotent with $N^{2}=0$ |
| $\ker\exp$ | the matrices whose exponential is the identity |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge University Press, 1991), for the matrix exponential and the determinant formula.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for the exponential map and its local inverse.
- [The Minimal Polynomial and the Two Jordan Regimes of $M_2(\mathbb{C})$](the-minimal-polynomial-and-the-two-jordan-regimes-of-m2c.html), for the diagonal and Jordan cases used in the proof of surjectivity.
- [The Element: Rank, Trace, Determinant, Characteristic Polynomial at $n=2$](the-element-rank-trace-determinant-characteristic-polynomial-at-n-2.html), for the trace and the determinant.
- [The Polar Decomposition of a Biquaternion](the-polar-decomposition-of-a-biquaternion.html), for the length and direction factors that the exponential produces.
