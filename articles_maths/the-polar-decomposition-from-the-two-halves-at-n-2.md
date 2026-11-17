# __The Polar Decomposition from the Two Halves at $n=2$__

## Introduction

**Every invertible $2\times2$ complex matrix is a unitary matrix times a positive definite Hermitian matrix, the two factors are unique, and the positive factor is the square root of $A^{*}A$, so the decomposition is built from the Hermitian half and the unitary group.**

The article states the polar decomposition, constructs the positive factor from $A^{*}A$, proves the unitarity of the other factor, proves uniqueness, treats the singular case where the factors are not unique, and lists the real, symmetric and complex variants. It assumes *The Exponential of $\operatorname{Sym}_2$: Stretches and the Positive Cone*, *The Spectral Theorem: the Hermitian Case and the Sphere of Idempotents* and *Normal $2\times2$ Matrices and the Common Spectral Theorem*.

It follows the biquaternion article *The Polar Decomposition of a Biquaternion* for the same split written with the unit $e_t$ and the algebraic norm $N$.

## The Statement

**Theorem.** Every invertible matrix $A$ is $A=UP$ with $U$ unitary and $P$ positive definite Hermitian, and the two factors are unique.

**Proof.** The construction and the uniqueness are proved in the two sections below.

**Corollary.** The polar decomposition is a bijection between the group of invertible matrices and the product of the unitary group with the positive definite cone.

**Proof.** The decomposition gives the map from the product to the group, and the uniqueness gives its injectivity.

**Corollary.** The determinant of $A$ is the determinant of $U$ times the positive number $\det P$, so the modulus of the determinant is $\det P$ and the phase is $\det U$.

**Proof.** The determinant is multiplicative, and a positive definite matrix has a positive determinant.

## The Construction

**Proposition.** Let $P=(A^{*}A)^{1/2}$ be the positive definite square root. Then $U=AP^{-1}$ is unitary.

**Proof.** The matrix $A^{*}A$ is Hermitian, and it is positive definite because $v^{*}A^{*}Av=\|Av\|^{2}>0$ for a nonzero $v$ when $A$ is invertible; its square root $P$ is therefore positive definite and invertible. Then $U^{*}U=P^{-1}A^{*}AP^{-1}=P^{-1}P^{2}P^{-1}=I$, so $U$ is unitary.

**Corollary.** The matrix $A$ is the product $UP$, and the factor $P$ is Hermitian and positive definite.

**Proof.** The definition of $U$ gives $A=UP$, and $P$ was chosen Hermitian and positive definite.

**Corollary.** The factors are obtained from the two eigenvalues of $A^{*}A$, which are the squares of the singular values.

**Proof.** The square root is taken on the eigenvalues, and the singular values are their square roots, so the eigenvalues of $P$ are the singular values.

## Uniqueness

**Proposition.** If $A=U_{1}P_{1}=U_{2}P_{2}$ with unitary $U_{j}$ and positive definite $P_{j}$, then $U_{1}=U_{2}$ and $P_{1}=P_{2}$.

**Proof.** Taking adjoints in $U_{1}P_{1}=U_{2}P_{2}$ and multiplying gives $P_{1}^{2}=A^{*}A=P_{2}^{2}$. Two positive definite matrices with equal squares are equal, because each is the unique positive definite square root of its square, so $P_{1}=P_{2}$. Then $U_{1}P_{1}=U_{2}P_{1}$ with $P_{1}$ invertible gives $U_{1}=U_{2}$.

**Corollary.** The decomposition is unique, so the notation $U(A)$ and $P(A)$ is well defined.

**Proof.** The two factors are determined by $A$.

**Corollary.** The positive factor depends only on $A$ through $A^{*}A$, so two matrices have the same positive factor exactly when they have the same $A^{*}A$.

**Proof.** The positive factor is the square root of $A^{*}A$, and the square root is unique.

## The Two Halves

**Proposition.** The positive factor lies in the Hermitian half and the unitary factor lies in the exponential of the anti-Hermitian half, so both factors come from the two halves.

**Proof.** A positive definite matrix is Hermitian, and a unitary matrix is the exponential of an anti-Hermitian matrix by *The Exponential of a $2\times2$ Matrix and Its Image*.

**Corollary.** The polar decomposition writes the group as the product of the exponential of the anti-Hermitian half with the exponential of the Hermitian half.

**Proof.** The unitary factor is the exponential of an anti-Hermitian matrix, and the positive factor is the exponential of a Hermitian matrix, by the logarithm of *The Exponential of $\operatorname{Sym}_2$: Stretches and the Positive Cone*.

**Corollary.** The unitary group is the compact factor and the positive cone is the noncompact factor, and the multiplication map from their product to the group of invertible matrices is a bijection.

**Proof.** The decomposition supplies the map, the uniqueness makes it injective, and every invertible matrix is the image of its own pair of factors.

## The Singular Case

**Proposition.** A matrix $A$ of rank one is $A=UP$ with $U$ unitary and $P$ positive semidefinite of rank one, and the factors are not unique.

**Proof.** The matrix $A^{*}A$ is positive semidefinite of rank one and its square root $P$ is defined. On the range of $P$, which is a line, the factor $U$ is forced by $U(Pv)=Av$, and that rule is an isometry there; it extends to the orthogonal complement, which is the kernel of $P$, in a circle of ways, so the factors are not unique.

**Corollary.** The polar decomposition exists for every matrix with $P$ positive semidefinite, and it is unique exactly when the matrix is invertible.

**Proof.** The kernel of $A$ is nonzero exactly when the matrix is singular, and the freedom in $U$ is precisely the freedom on that kernel.

**Corollary.** At rank one the freedom is a circle, the choice of a unitary on the kernel line.

**Proof.** The kernel is a line, and the unitary group of a line is a circle.

## The Real and Symmetric Cases

**Proposition.** A real invertible matrix has a real polar decomposition with an orthogonal factor and a positive definite symmetric factor.

**Proof.** The matrix $A^{\mathsf T}A$ is real symmetric positive definite, its square root is real symmetric, and the factor $U=A P^{-1}$ satisfies $U^{\mathsf T}U=I$.

**Corollary.** A real matrix with positive determinant has the decomposition with a rotation factor, and one with negative determinant has a reflection factor.

**Proof.** The determinant of $U$ is the sign of the determinant of $A$, and the orthogonal group splits into rotations and reflections accordingly.

**Corollary.** The decomposition of a self-adjoint matrix is trivial on the positive part and gives the sign on the negative part.

**Proof.** For a Hermitian $A$ the matrix $A^{*}A=A^{2}$ has the square root $|A|$, and $U$ is the unitary that is the identity on the positive eigenspace and minus the identity on the negative one.

## The Biquaternion Comparison

**Proposition.** In the biquaternion language the polar decomposition is the split of an element into its norm and its direction, and the algebraic norm $N$ is the determinant of the positive factor.

**Proof.** The algebraic norm $N$ of inertia $(2,2)$ restricts to the determinant on the matrix model, and the positive factor has the determinant equal to $N$ of the element.

**Corollary.** The biquaternion polar decomposition of *The Polar Decomposition of a Biquaternion* is the same statement under the identification of the two algebras.

**Proof.** The two decompositions agree under the matrix model, and both are unique on the invertible elements.

**Corollary.** The unitary factor carries the direction and the positive factor carries the length, so the four-dimensional unitary group and the three-dimensional cone account for the seven real dimensions of the invertible set.

**Proof.** The unitary group has real dimension four, the positive cone has dimension three, and the product covers the seven-dimensional complement of the singular set inside the eight-dimensional algebra.

## Summary

Every invertible $2\times2$ complex matrix is $A=UP$ with $U$ unitary and $P$ positive definite Hermitian, and the factors are unique. The positive factor is the square root of $A^{*}A$ and its eigenvalues are the singular values, while the unitary factor is $AP^{-1}$.

Both factors come from the two halves: the positive factor is the exponential of a Hermitian matrix and the unitary factor is the exponential of an anti-Hermitian matrix. For a singular matrix the decomposition survives with a positive semidefinite factor but is not unique, the freedom being the choice of a unitary on the kernel.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A=UP$ | the polar decomposition |
| $U$ | the unitary factor |
| $P$ | the positive definite (or semidefinite) factor |
| $A^{*}A$ | the Hermitian matrix whose square root is $P^{2}$ |
| $N$ | the algebraic norm, the determinant on the model |

## Further Reading

- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the polar decomposition and the singular values.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the existence and uniqueness statements.
- [The Exponential of $\operatorname{Sym}_2$: Stretches and the Positive Cone](the-exponential-of-sym-2-stretches-and-the-positive-cone.html), for the positive factor as an exponential.
- [Normal $2\times2$ Matrices and the Common Spectral Theorem](normal-2x2-matrices-and-the-common-spectral-theorem.html), for the unitary diagonalisation used here.
- [The Polar Decomposition of a Biquaternion](the-polar-decomposition-of-a-biquaternion.html), for the same split in the biquaternion language.
