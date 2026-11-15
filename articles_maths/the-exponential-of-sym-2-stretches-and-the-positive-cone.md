# __The Exponential of $\operatorname{Sym}_2$: Stretches and the Positive Cone__

## Introduction

**The exponential maps the three-dimensional space $\operatorname{Sym}_2(\mathbb{R})$ onto the cone of positive definite symmetric matrices, it is a diffeomorphism there, and along each eigenaxis it is a pure stretch with factor the exponential of the eigenvalue.**

The article proves that the exponential of a symmetric matrix is symmetric and positive definite, that the eigenvalues of the image are the exponentials of the eigenvalues, that the logarithm is the inverse and is symmetric, and that the image is exactly the cone. It computes the action on the determinant, describes the one-parameter stretches, and identifies the boundary of the image, where a positive semidefinite matrix is singular. It assumes *The Jordan Algebra $\operatorname{Sym}_2$*, *The Exponential of a $2\times2$ Matrix and Its Image* and *The Spectral Theorem: the Hermitian Case and the Sphere of Idempotents*.

It follows the biquaternion article *The Polar Decomposition of a Biquaternion* for the positive factor of the split.

## The Symmetric Half

**The symmetric matrices form a real vector space of dimension three, and their exponential stays inside that space.**

**Definition.** Let $\operatorname{Sym}_2(\mathbb{R})$ be the real vector space of real symmetric $2\times2$ matrices.

**Proposition.** The symmetric matrices have dimension three, and the exponential of a symmetric matrix is symmetric.

**Proof.** A symmetric matrix has three independent entries; and if $X^{\mathsf T}=X$ then $(e^{X})^{\mathsf T}=e^{X^{\mathsf T}}=e^{X}$.

**Corollary.** The exponential of a real symmetric matrix is real and symmetric, so the exponential is a map of the half into itself.

**Proof.** The series has real coefficients and the transpose computation is closed.

**Corollary.** The exponential of the symmetric half is diagonalised by the same orthogonal frame as the matrix.

**Proof.** A symmetric matrix is orthogonally diagonalisable, and the exponential of a polynomial in a matrix is the same polynomial in the eigenvalues.

## The Eigenvalues

**Theorem.** If $X$ has the eigenvalues $\lambda_{1},\lambda_{2}$ then $e^{X}$ has the eigenvalues $e^{\lambda_{1}},e^{\lambda_{2}}$, so the exponential of a symmetric matrix is positive definite.

**Proof.** The spectral mapping of *The Spectrum of a $2\times2$ Matrix* gives the eigenvalues of the image; the exponentials of real numbers are positive, so both eigenvalues are positive; and a symmetric matrix with positive eigenvalues is positive definite.

**Corollary.** The determinant of the image is $e^{\operatorname{tr}X}$, which is positive, and the trace of the image is $e^{\lambda_{1}}+e^{\lambda_{2}}$.

**Proof.** The determinant formula and the sum of the eigenvalues.

**Corollary.** The trace of the image is at least twice the square root of its determinant, with equality exactly when the two eigenvalues are equal.

**Proof.** The inequality $e^{a}+e^{b}\ge2e^{(a+b)/2}=2\sqrt{e^{a+b}}$ is the arithmetic and geometric mean inequality, with equality exactly when $a=b$.

## The Stretch along an Axis

**Proposition.** The exponential of the matrix $t\,vv^{\mathsf T}$ with $v$ a unit vector is $I+(e^{t}-1)vv^{\mathsf T}$, the stretch by $e^{t}$ along the axis $v$ and by one along the perpendicular axis.

**Proof.** The matrix $t\,vv^{\mathsf T}$ has the eigenvalues $t$ and $0$ with the eigenvectors $v$ and a perpendicular unit vector, so its exponential has the eigenvalues $e^{t}$ and $1$ on the same axes.

**Corollary.** The one-parameter family $t\mapsto e^{t\,vv^{\mathsf T}}$ is a family of stretches, and its determinant is $e^{t}$.

**Proof.** The determinant is the product $e^{t}\cdot1$.

**Corollary.** Every positive definite symmetric matrix is a stretch along two orthogonal axes, with factors the two eigenvalues.

**Proof.** The spectral theorem gives the orthogonal axes and the positive eigenvalues, and the exponential of the diagonal matrix of the logarithms gives the factors.

## The Logarithm

**Theorem.** Every positive definite symmetric matrix $A$ has a unique symmetric logarithm, given by the logarithm of its eigenvalues on its own orthonormal frame.

**Proof.** The spectral theorem writes $A=U\Lambda U^{\mathsf T}$ with $\Lambda$ diagonal and positive; then $X=U(\log\Lambda)U^{\mathsf T}$ is symmetric and $e^{X}=A$. Uniqueness follows because a symmetric logarithm must share the eigenspaces of $A$ and its eigenvalues must be the logarithms of those of $A$.

**Corollary.** The exponential is a bijection from the symmetric half onto the positive definite cone, with the symmetric logarithm as its inverse.

**Proof.** The two maps are inverse by the theorem and by the spectral mapping.

**Corollary.** The exponential is a diffeomorphism of the symmetric half onto the cone, and its derivative is everywhere invertible there.

**Proof.** The logarithm is smooth, and the two maps are inverse with smooth expressions in the eigenvalues.

## The Cone

**Proposition.** The image of the symmetric half is the interior of the cone of positive semidefinite matrices, and the boundary of the cone is not attained.

**Proof.** The image consists of the symmetric matrices with both eigenvalues positive, which is the interior of the cone; a positive semidefinite matrix with a zero eigenvalue is not the exponential of any real symmetric matrix, because the exponential has positive eigenvalues.

**Corollary.** The boundary of the cone consists of the positive semidefinite matrices of rank one, which are the nonnegative multiples of the rank-one symmetric idempotents.

**Proof.** A positive semidefinite matrix of rank one has one positive eigenvalue and one zero eigenvalue, and it is a multiple of the projection onto its image.

**Corollary.** The exponential approaches the boundary as one eigenvalue of the argument tends to minus infinity, and the cone is not closed in the image.

**Proof.** The eigenvalue $e^{\lambda}$ tends to zero as $\lambda$ tends to minus infinity, and the logarithm of a matrix with a zero eigenvalue does not exist.

## The Action on the Trace and the Norm

**Proposition.** The exponential does not preserve the trace, but it preserves the ordering of the eigenvalues and the identity of the eigenaxes.

**Proof.** The trace of the image is the sum of the exponentials, which is not the exponential of the trace in general; the eigenaxes are the same because the exponential is a function of the matrix.

**Corollary.** The exponential is order preserving for the Loewner order: if $X\le Y$ then $e^{X}\le e^{Y}$.

**Proof.** Put $Z=Y-X$, which is positive semidefinite. Then $e^{Y}-e^{X}=\int_{0}^{1}\dfrac{d}{dt}e^{X+tZ}\,dt$ and $\dfrac{d}{dt}e^{X+tZ}=\int_{0}^{1}e^{(1-s)(X+tZ)}Ze^{s(X+tZ)}\,ds$, which is positive semidefinite for every $t$ because it is a positive combination of conjugates of $Z$.

**Corollary.** The logarithm is order preserving in the same sense, so the exponential is an order isomorphism from the symmetric half onto the cone.

**Proof.** For positive definite $A\le B$ the derivative $\dfrac{d}{dt}\log(A+tZ)=\int_{0}^{\infty}(A+tZ+s)^{-1}Z(A+tZ+s)^{-1}\,ds$ is positive semidefinite for $Z=B-A$, and the same integral argument applies.

## Summary

The exponential of a real symmetric matrix is symmetric and positive definite, and its eigenvalues are the exponentials of the eigenvalues of the matrix. Along an eigenaxis with the unit vector $v$ the exponential of $t\,vv^{\mathsf T}$ is the stretch by $e^{t}$, and every positive definite symmetric matrix is a stretch along two orthogonal axes.

The exponential is a bijection from the symmetric half onto the positive definite cone, with the symmetric logarithm as its inverse, and it is a diffeomorphism. The boundary of the cone, the rank-one positive semidefinite matrices, is not in the image, and it is approached as an eigenvalue of the argument tends to minus infinity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Sym}_2(\mathbb{R})$ | the real symmetric matrices |
| $e^{X}$ | the exponential of a symmetric matrix |
| $vv^{\mathsf T}$ | the rank-one projection on the axis $v$ |
| $\log A$ | the symmetric logarithm of a positive definite matrix |
| $\le$ | the Loewner order |

## Further Reading

- Rajendra Bhatia, *Positive Definite Matrices* (Princeton University Press, 2007), for the exponential and the logarithm on the cone.
- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge University Press, 1991), for the matrix logarithm.
- [The Jordan Algebra $\operatorname{Sym}_2$](the-jordan-algebra-sym-2.html), for the symmetric half with its Jordan product.
- [The Exponential of a $2\times2$ Matrix and Its Image](the-exponential-of-a-2x2-matrix-and-its-image.html), for the general exponential used here.
- [The Polar Decomposition of a Biquaternion](the-polar-decomposition-of-a-biquaternion.html), for the positive factor in the biquaternion picture.
