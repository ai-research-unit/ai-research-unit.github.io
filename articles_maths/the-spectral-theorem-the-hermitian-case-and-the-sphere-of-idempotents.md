# __The Spectral Theorem: the Hermitian Case and the Sphere of Idempotents__

## Introduction

**A Hermitian $2\times2$ matrix is $X=aI+r\,\vec n\cdot\vec\sigma$ with $a$ real, $r\ge0$ and $\vec n$ a unit vector, its eigenvalues are $a\pm r$, and its two spectral projections are $\tfrac12(I\pm\vec n\cdot\vec\sigma)$; the rank-one Hermitian idempotents are exactly the matrices $\tfrac12(I+\vec n\cdot\vec\sigma)$ with $\vec n\in S^{2}$, so they form a two-sphere.**

The article proves the spectral theorem for Hermitian matrices at order two, gives the Pauli parametrisation with its three real parameters, identifies the sphere of idempotents, reads the ordering of the eigenvalues as the choice of a hemisphere, and describes the positive semidefinite cone inside the Hermitian space. It assumes *Normal $2\times2$ Matrices and the Common Spectral Theorem*, *The Spectrum of a $2\times2$ Matrix* and *The Two Halves over $\mathbb{C}$: Hermitian and Skew-Hermitian at $n=2$*.

It keeps to the spectral statement; the exponential of the symmetric half belongs to the analysis of the two halves.

## The Hermitian Matrices as a Real Space

**The Hermitian matrices form a real vector space of dimension four, spanned by the identity and the three Pauli matrices.**

**Definition.** The **Pauli matrices** are

$$
\sigma_{1}=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\sigma_{2}=\begin{pmatrix}0&-i\\ i&0\end{pmatrix},\qquad
\sigma_{3}=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

**Proposition.** Every Hermitian matrix is $aI+x\sigma_{1}+y\sigma_{2}+z\sigma_{3}$ with $a,x,y,z$ real, and the four matrices $I,\sigma_{1},\sigma_{2},\sigma_{3}$ are a real basis of the Hermitian space.

**Proof.** A Hermitian matrix has real diagonal entries and conjugate off-diagonal entries, which is four real parameters; the four displayed matrices are Hermitian and independent, and the expansion reproduces any such matrix.

**Corollary.** The imaginary multiples of the Pauli matrices span the traceless Hermitian matrices, and the identity spans the trace line.

**Proof.** The Pauli matrices are traceless, and the trace of $aI$ is $2a$.

**Corollary.** The Pauli matrices satisfy $\sigma_{j}^{2}=I$ and $\sigma_{j}\sigma_{k}=-\sigma_{k}\sigma_{j}$ for $j\ne k$, with $\sigma_{1}\sigma_{2}=i\sigma_{3}$ and its cyclic permutations.

**Proof.** Direct multiplication of the three matrices.

## The Spectral Theorem

**Theorem.** A Hermitian matrix has real eigenvalues and an orthonormal basis of eigenvectors, and it is

$$
X=\lambda_{+}\rho_{+}+\lambda_{-}\rho_{-},\qquad \rho_{\pm}=\tfrac12\bigl(I\pm\vec n\cdot\vec\sigma\bigr),
$$

with $\rho_{\pm}$ Hermitian orthogonal idempotents of rank one and $\lambda_{\pm}\in\mathbb{R}$.

**Proof.** The matrix is normal, so it is unitarily diagonalisable by *Normal $2\times2$ Matrices and the Common Spectral Theorem*; its eigenvalues are real because $\lambda=v^{*}Xv=\bar\lambda$; the two spectral projections of *The Spectrum of a $2\times2$ Matrix* are Hermitian because they are polynomials in $X$ with real coefficients.

**Corollary.** The two projections are the projections onto the two orthogonal eigenlines, and their sum is the identity.

**Proof.** The reconstruction $X=\lambda_{+}\rho_{+}+\lambda_{-}\rho_{-}$ with $\rho_{+}+\rho_{-}=I$ gives $\rho_{+}=(X-\lambda_{-}I)/(\lambda_{+}-\lambda_{-})$, which projects onto the first eigenline along the second.

**Corollary.** A Hermitian matrix with a double eigenvalue is a real scalar, and its projections are not determined by the matrix.

**Proof.** A double eigenvalue forces the matrix to be the scalar, and every pair of orthogonal lines gives a pair of projections summing to the identity.

## The Pauli Form and the Three Parameters

**Theorem.** Every Hermitian matrix is $X=aI+r\,\vec n\cdot\vec\sigma$ with $a=\tfrac12\operatorname{tr}X$, $r=\sqrt{a^{2}-\det X}\ge0$ and $\vec n\in S^{2}$, and its eigenvalues are $a\pm r$.

**Proof.** Write $X=aI+Y$ with $Y$ traceless Hermitian; then $Y=x\sigma_{1}+y\sigma_{2}+z\sigma_{3}$ and $r=\sqrt{x^{2}+y^{2}+z^{2}}$ is the length of the vector $(x,y,z)$, with $\vec n$ its direction when $r\ne0$. The identity $(\vec n\cdot\vec\sigma)^{2}=I$ for a unit vector gives the eigenvalues $a\pm r$ by the spectral theorem.

**Corollary.** The four real parameters are the trace, the length of the traceless part and the two angles of the direction, and the spectrum depends only on the first two.

**Proof.** The pair $(a,r)$ is the unordered pair of eigenvalues up to the translation by $a$, and the direction does not enter the spectrum.

**Corollary.** The determinant is $a^{2}-r^{2}$, so the Hermitian matrix is singular exactly when $r=|a|$.

**Proof.** The determinant is the product of the eigenvalues, $(a+r)(a-r)=a^{2}-r^{2}$.

## The Sphere of Idempotents

**Theorem.** The rank-one Hermitian idempotents are exactly the matrices $\tfrac12(I+\vec n\cdot\vec\sigma)$ with $\vec n\in S^{2}$, and the set of them is a two-sphere.

**Proof.** A Hermitian idempotent has the eigenvalues $0$ and $1$ or is the identity or zero; the non-trivial ones have $a=\tfrac12$ and $r=\tfrac12$, so they are $\tfrac12(I+\vec n\cdot\vec\sigma)$ with $\vec n$ a unit vector. Conversely such a matrix is Hermitian with the eigenvalues $1$ and $0$, hence an idempotent of rank one.

**Corollary.** The map $\vec n\mapsto\tfrac12(I+\vec n\cdot\vec\sigma)$ is a bijection from the unit sphere onto the set of rank-one Hermitian idempotents.

**Proof.** The direction $\vec n$ is recovered from the idempotent as $2\rho-I$, which is Hermitian of square $I$ and trace zero, and such a matrix is $\vec n\cdot\vec\sigma$ for exactly one unit vector.

**Corollary.** The two idempotents of a frame are antipodal points of the sphere, and a frame is a pair of antipodal points together with a phase.

**Proof.** The complementary idempotent of $\tfrac12(I+\vec n\cdot\vec\sigma)$ is $\tfrac12(I-\vec n\cdot\vec\sigma)$, which is the antipodal point.

## The Ordering and the Hemisphere

**Proposition.** The spectral projections of $X=aI+r\,\vec n\cdot\vec\sigma$ are the two antipodal idempotents of the direction $\vec n$, and the assignment of the larger eigenvalue to one of them is the choice of a hemisphere.

**Proof.** The projection onto the eigenvalue $a+r$ is $\tfrac12(I+\vec n\cdot\vec\sigma)$, and the two projections are exchanged when $\vec n$ is replaced by $-\vec n$; the larger eigenvalue goes with the $+\vec n$ side, which is one of the two hemispheres.

**Corollary.** The unordered spectrum of a Hermitian matrix is the pair $(a-r,a+r)$, and the ordered spectrum requires the extra choice of a sign.

**Proof.** The unordered pair is determined by $a$ and $r$, and the ordering is decided by which of the two antipodal idempotents carries the larger value.

**Corollary.** The set of Hermitian matrices with a fixed unordered spectrum is a sphere, and the set with a fixed ordered spectrum is a hemisphere pair identified along the boundary.

**Proof.** The direction $\vec n$ runs over the sphere, and the ordering adds the choice of the positive side, whose boundary is the discriminant locus $r=0$.

## The Positive Semidefinite Cone

**Proposition.** A Hermitian matrix is positive semidefinite exactly when $a\ge r$, and positive definite exactly when $a>r$.

**Proof.** The eigenvalues are $a\pm r$, so both are nonnegative exactly when $a-r\ge0$; strict positivity of both is $a>r$.

**Corollary.** The positive semidefinite cone is a circular cone over the sphere of idempotents, of opening angle a quarter turn at the apex.

**Proof.** In the coordinates $(a,r)$ with the direction $\vec n$, the cone is $a\ge r\ge0$, which is a cone of revolution whose section at $a=1$ is the ball $r\le1$; the slice at $a=r$ is the sphere of the directions.

**Corollary.** The rank-one positive semidefinite matrices are the boundary rays of the cone, and each is a nonnegative multiple of a Hermitian idempotent.

**Proof.** Rank one with both eigenvalues nonnegative means the smaller eigenvalue is zero, which is $a=r$, and the matrix is then $2a\,\rho$ with $\rho$ the idempotent of the direction.

## Summary

A Hermitian $2\times2$ matrix is $aI+r\,\vec n\cdot\vec\sigma$ with $a$ real, $r\ge0$ and $\vec n$ a unit vector, and its eigenvalues are $a\pm r$; the determinant is $a^{2}-r^{2}$. The spectral projections are $\tfrac12(I\pm\vec n\cdot\vec\sigma)$, and the rank-one Hermitian idempotents are exactly the matrices $\tfrac12(I+\vec n\cdot\vec\sigma)$, which form a two-sphere with antipodal points for complementary idempotents.

The ordering of the spectrum is the choice of a hemisphere, and the positive semidefinite cone is $a\ge r$, a cone of revolution over the sphere of idempotents, whose boundary rays are the rank-one positive semidefinite matrices.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma_{1},\sigma_{2},\sigma_{3}$ | the Pauli matrices |
| $a$ | half the trace |
| $r$ | the length of the traceless part |
| $\vec n$ | a unit vector in $\mathbb{R}^{3}$ |
| $\rho_{\pm}$ | the Hermitian spectral projections |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the spectral theorem for Hermitian matrices.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, volume 1 (Cambridge University Press, 1984), for the Pauli matrices and the Bloch sphere.
- [Normal $2\times2$ Matrices and the Common Spectral Theorem](normal-2x2-matrices-and-the-common-spectral-theorem.html), for the unitary diagonalisation used here.
- [Spinors as Peirce Coordinates in Two Dimensions](spinors-as-peirce-coordinates-in-two-dimensions.html), for the Hopf fibration over the sphere of idempotents.
- [The Polar Decomposition of a Biquaternion](the-polar-decomposition-of-a-biquaternion.html), for the positive factor that the cone provides in the biquaternion language.
