# __The Two Halves and the Analysis: Smooth Structures at $n=2$__

## Introduction

**The four halves are smooth vector spaces, the trace, the determinant and the projections onto the halves are smooth functions, the invertible group and the manifold of rank-one idempotents are smooth submanifolds, and the distribution defined by the symmetric half is not integrable: the bracket of two symmetric directions is antisymmetric.**

The article equips the halves with their smooth structures, examines the smoothness of the elementary functions, computes the critical set of the determinant, describes the smooth manifolds inside the matrix algebra, and tests the Frobenius condition for the distribution carried by a half. It assumes *The Two Halves and Their Topology at $n=2$*, *The Analysis on $M_2(\mathbb{C})$* and *The Space of Idempotents and the Flag Variety $\mathbb{P}^1$*.

It follows the biquaternion article *Subspaces and Decompositions of the Biquaternion Algebra* for the same submanifolds in the eight real coordinates.

## The Halves as Smooth Manifolds

**Each half is a smooth manifold without boundary, and the four smooth structures agree on the intersections.**

**Proposition.** Each half is a smooth manifold diffeomorphic to a Euclidean space, and the inclusions are smooth embeddings with closed image.

**Proof.** A finite-dimensional real vector space has a smooth structure with a single chart, the identity is a diffeomorphism onto the space of coordinates, and a linear subspace is a closed embedded submanifold.

**Corollary.** The projections onto the halves are smooth surjections, and they are the identity on their own half and zero on the other.

**Proof.** The projections are linear maps defined by the traces against the basis elements, so they are smooth.

**Corollary.** A map into the matrix algebra is smooth exactly when its four compositions with the projections onto coordinate directions are smooth.

**Proof.** The matrix algebra is the direct sum of its coordinate lines, and a map into a product is smooth exactly when its components are.

## Smooth Functions

**The trace, the determinant and the cofactor map are smooth functions on the matrix algebra.**

**Proposition.** The trace is linear and the determinant is a polynomial of degree two in the eight real coordinates, so both are smooth everywhere.

**Proof.** The trace is the sum of the two complex diagonal entries, and the determinant is a product minus a product of the entries.

**Corollary.** Every polynomial in the entries is smooth, and the algebra of smooth functions is closed under composition with smooth maps of the target.

**Proof.** Polynomials are smooth, and the composition of smooth maps is smooth.

**Corollary.** The map sending a matrix to its cofactor matrix is polynomial and hence smooth, and it vanishes exactly on the matrices of rank at most one.

**Proof.** Each cofactor is a single entry up to sign, and all of them vanish when the rank is at most one.

## The Determinant and Its Critical Set

**Theorem.** The determinant is a submersion at every matrix of rank two, and its critical set is exactly the cone of matrices of rank at most one.**

**Proof.** The derivative is the cofactor pairing, whose matrix is the cofactor matrix; that matrix is invertible exactly when the matrix has rank two, and it vanishes identically for rank at most one, where the derivative is also zero.

**Corollary.** The zero set of the determinant is a smooth hypersurface away from the origin, and it has a cone singularity at the origin.

**Proof.** The gradient does not vanish on the cone except at the origin, and the cone is the zero set of a quadratic form.

**Corollary.** The level sets of the determinant away from the critical set are smooth submanifolds of real codimension one.

**Proof.** The preimage of a regular value of a submersion is a submanifold of the codimension of the target.

## The Smooth Group

**Proposition.** The invertible matrices form an open smooth submanifold of the matrix algebra of real dimension eight, and the group operations are smooth.

**Proof.** An open subset of a smooth manifold is a smooth manifold, and the product and the inverse are given by polynomial and rational expressions.

**Corollary.** The exponential is a smooth map from the algebra to the group, and its derivative is smooth in the base point.

**Proof.** The exponential is given by a norm-convergent series of polynomials.

**Corollary.** The group acts smoothly on the matrix algebra by conjugation, and the orbits are the similarity classes.

**Proof.** The conjugation is the restriction of a bilinear map, which is smooth.

## The Smooth Retraction

**Proposition.** The multiplication map from the product of the unitary group with the positive definite cone to the invertible group is a diffeomorphism.

**Proof.** The polar decomposition gives a bijection with a continuous inverse, and each of the three maps involved is smooth, so the bijection is a diffeomorphism.

**Corollary.** The invertible group is diffeomorphic to the product of a compact manifold with a convex open set, so its smooth structure splits into a compact part and a flat part.

**Proof.** The unitary group is compact without boundary, and the positive definite cone is an open convex set.

**Corollary.** The logarithm is a smooth inverse for the exponential on the positive definite cone, so the exponential is a diffeomorphism there.

**Proof.** A positive definite matrix has positive eigenvalues, and the logarithm of a positive number is smooth, so the logarithm of the matrix is a smooth function of the matrix.

## Smooth Submanifolds

**Proposition.** The set of rank-one idempotents is a smooth submanifold of the matrix algebra of real dimension four, and the set of all idempotents is the union of that manifold with two isolated points.

**Proof.** The rank-one idempotents form the complement of the incidence divisor in the surface $\mathbb{P}^{1}\times\mathbb{P}^{1}$, which is smooth of complex dimension two, hence real dimension four; the two trivial idempotents are isolated.

**Corollary.** The Hermitian idempotents form a smooth submanifold diffeomorphic to the two-sphere, of real dimension two.

**Proof.** They are the image of the unit sphere under a smooth injective map with smooth inverse.

**Corollary.** The positive definite cone is a smooth open submanifold of the Hermitian half, diffeomorphic to the product of the positive reals with the open ball of trace-one positive definite matrices.

**Proof.** Every positive definite matrix is a positive scalar times a trace-one positive definite matrix, and the trace-one set is the open ball of the Bloch section.

## The Distribution of a Half

**Proposition.** The assignment of the symmetric half as a subspace of the tangent space at every point is a smooth distribution of rank three whose bracket of two sections is antisymmetric, so the distribution is not integrable.

**Proof.** The distribution is constant, hence smooth; the bracket of two symmetric matrices is antisymmetric, so it leaves the distribution, and the Frobenius condition fails.

**Corollary.** There is no foliation of the matrix algebra whose leaves have the symmetric half as tangent space.

**Proof.** A foliation would require the distribution to be closed under the bracket.

**Corollary.** The distribution carried by the antisymmetric half is integrable, since that half is one-dimensional and the bracket of its sections vanishes.

**Proof.** A one-dimensional distribution is always integrable because the bracket of two multiples of a single vector field is again a multiple of it.

## Summary

The four halves are smooth vector spaces, and the trace, the determinant and the cofactor map are smooth functions on the matrix algebra. The determinant is a submersion exactly on the matrices of full rank, and its zero set is a smooth hypersurface away from the origin.

The invertible group is an open smooth submanifold, the rank-one idempotents form a smooth manifold of real dimension four, and the Hermitian idempotents form the two-sphere. The distribution carried by the symmetric half is not integrable, because the bracket of two symmetric directions is antisymmetric, while the distribution of the antisymmetric half is integrable.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Sym}_2$, $\operatorname{Skew}_2$ | the two real halves as smooth subspaces |
| $d\det$ | the cofactor pairing |
| $\mathbb{P}^{1}\times\mathbb{P}^{1}$ | the surface of rank-one idempotents |
| $S^{2}$ | the manifold of Hermitian idempotents |
| $[\cdot,\cdot]$ | the bracket testing integrability |

## Further Reading

- John M. Lee, *Introduction to Smooth Manifolds* (Springer, 2012), for submanifolds, submersions and foliations.
- Shlomo Sternberg, *Lectures on Differential Geometry* (AMS Chelsea, 1999), for distributions and the Frobenius theorem.
- [The Two Halves and Their Topology at $n=2$](the-two-halves-and-their-topology-at-n-2.html), for the halves as topological spaces.
- [The Analysis on $M_2(\mathbb{C})$](the-analysis-on-m2c.html), for the measure and the calculus used here.
- [The Space of Idempotents and the Flag Variety $\mathbb{P}^1$](the-space-of-idempotents-and-the-flag-variety-p1.html), for the manifold of idempotents.
