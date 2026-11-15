# __The Topology of $M_2(\mathbb{C})$__

## Introduction

**The matrix algebra is a real vector space of dimension eight with its Euclidean topology, hence contractible; the singular matrices form a closed cone, of real codimension two over the complex field and of codimension one over the real field, and the invertible matrices are its open dense complement.**

The article sets the topology of the matrix algebra, compares the norms that define it, describes the rank strata and the zero set of the determinant, proves that the invertible elements are dense and that the bounded closed sets are compact, and computes the dimensions of the strata. It assumes *The Matrix Algebra $M_2(\mathbb{C})$*, *The Element: Rank, Trace, Determinant, Characteristic Polynomial at $n=2$* and *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$*.

It defers the homotopy of the invertible group to *The Homotopy of $\mathrm{GL}_2(\mathbb{C})$ and of the Two Halves* and the measure theory to *The Analysis on $M_2(\mathbb{C})$*.

## The Underlying Space

**The matrix algebra is the real vector space of dimension eight, and its topology is the Euclidean one.**

**Proposition.** The identification of a matrix with its four complex entries is a linear isomorphism onto $\mathbb{C}^{4}$, and composing with the real and imaginary parts gives a linear isomorphism onto $\mathbb{R}^{8}$.

**Proof.** The four entries determine the matrix and are determined by it, and each complex entry is a pair of real numbers.

**Corollary.** The matrix algebra is contractible, hence connected and simply connected, and all its homotopy groups vanish.

**Proof.** A vector space is contracted to the origin by the homotopy $Z\mapsto(1-t)Z$.

**Corollary.** The matrix algebra is locally compact, metrisable and second countable, and it is complete for the Euclidean metric.

**Proof.** These properties hold for every finite-dimensional real vector space.

## The Norms

**All norms on the matrix algebra are equivalent, and the operator norm, the Hilbert–Schmidt norm and the maximum norm define the same topology.**

**Proposition.** The three norms are mutually bounded by constants depending only on the dimension.

**Proof.** The maximum of the entries bounds the Hilbert–Schmidt norm, which bounds the operator norm times two; the operator norm bounds twice the maximum of the entries, because the image of a unit vector has two coordinates, each a sum of two terms.

**Corollary.** The convergence of a sequence of matrices is the entrywise convergence, and the limit operations of the algebra are continuous.

**Proof.** Entrywise convergence is convergence for the maximum norm, and the sum and the product are polynomial in the entries.

**Corollary.** The group of invertible matrices is a topological group with the induced topology, and the inversion is continuous on it.

**Proof.** The determinant is a continuous polynomial that does not vanish on the group, and the inverse is given by the adjugate divided by the determinant, which is continuous there.

## The Rank Strata

**The sets of matrices of rank at most $k$ are closed algebraic cones, and the set of matrices of rank two is their open complement.**

**Proposition.** The set of matrices of rank at most one is the zero set of the determinant, a real algebraic cone of real dimension six, and it has a singularity only at the origin.

**Proof.** The determinant is a single polynomial equation on a real space of dimension eight, the cone is parametrised by two vectors, and the derivative of the determinant vanishes exactly at the zero matrix.

**Corollary.** The set of matrices of rank two is open, dense and connected.

**Proof.** It is the complement of a closed set with empty interior, so it is open and dense; and it is the orbit of the identity under the group of invertible matrices, which is connected.

**Corollary.** The strata are the two sets: rank two of real dimension eight, and rank at most one of real dimension six, the second being the boundary of the first.

**Proof.** The dimensions are those of the manifold and of its boundary hypersurface.

## The Determinant and Its Zero Set

**Theorem.** The determinant is a continuous function whose zero set separates the matrix algebra over the real field, and over the complex field its zero set has real codimension two.

**Proof.** Over the real field the determinant is a quadratic form of signature $(2,2)$ on the eight real coordinates, so its zero set is a cone that separates the space; over the complex field the determinant is a complex-valued polynomial, and its zero set is a complex hypersurface, of real codimension two.

**Corollary.** The complement of the zero set has two connected components over the real field and one over the complex field.

**Proof.** The signature computation of *The Two-Sided Operators and the Segre Cone at $n=2$* gives the two real components, and the connectedness of the nonzero complex numbers gives the single complex component.

**Corollary.** Over the complex field a path of matrices can avoid the singular set, because the codimension is two.

**Proof.** A path in a space of real dimension eight can be perturbed off a set of codimension two.

## Density and Approximation

**Proposition.** Every matrix is the limit of invertible matrices, and the approximation can be chosen along the ray $Z+\varepsilon I$.

**Proof.** The determinant of $Z+\varepsilon I$ is a polynomial in $\varepsilon$ of degree two whose roots are the negated eigenvalues of $Z$; there are at most two roots, so for all but finitely many small values the matrix is invertible.

**Corollary.** The group of invertible matrices is dense in the matrix algebra, and its complement has empty interior.

**Proof.** The approximation shows density, and a set with dense complement has empty interior.

**Corollary.** A continuous function that vanishes on the invertible matrices vanishes everywhere, because the singular set has empty interior.

**Proof.** A continuous function is determined by its values on a dense subset, and the invertibles are dense.

## The Distance to the Singular Set

**Proposition.** The distance from a matrix $Z$ to the singular set, measured with the Hilbert–Schmidt norm, is the smallest singular value of $Z$.

**Proof.** A singular matrix has rank at most one, and the nearest matrix of rank at most one is obtained by deleting the smallest singular value of $Z$ from its singular value decomposition, so the distance is that singular value.

**Corollary.** For a normal matrix the distance to the singular set is the smallest modulus of an eigenvalue.

**Proof.** The singular values of a normal matrix are the moduli of its eigenvalues.

**Corollary.** The distance to the singular set is a continuous function on the matrix algebra, it is positive exactly on the invertible matrices, and it vanishes exactly on the singular ones.

**Proof.** The smallest singular value depends continuously on the matrix, since the singular values do.

## Compactness

**Proposition.** A subset of the matrix algebra is compact exactly when it is closed and bounded, and the closed balls are compact.

**Proof.** The space is a finite-dimensional Euclidean space, where the two notions agree.

**Corollary.** The unitary group and the set of idempotents of bounded norm are compact.

**Proof.** The unitary group is closed and bounded by one, and the idempotents of norm at most one are closed and bounded.

**Corollary.** A continuous function on a compact set of matrices attains its maximum and its minimum.

**Proof.** This is the extreme value theorem in a metric space.

## Summary

The matrix algebra is a real vector space of dimension eight, so it is contractible, locally compact and complete, and all its norms define the same topology. The sets of matrices of bounded rank are closed algebraic cones: the determinant vanishes on the cone of rank at most one, of real dimension six, and its complement of rank two is open, dense and connected.

Over the real field the zero set of the determinant separates the space into two components; over the complex field it has real codimension two and does not separate. The invertible matrices are dense, and the closed bounded sets are compact.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{R}^{8}$ | the real coordinates of the matrix algebra |
| $\det$ | the continuous polynomial defining the singular set |
| $\operatorname{rank}\le 1$ | the singular cone of real dimension six |
| $\overline{Z}$ | the closure of a set of matrices |
| $\|\cdot\|$ | any of the equivalent norms |

## Further Reading

- James R. Munkres, *Topology* (Pearson, 2000), for the topology of Euclidean spaces.
- John W. Milnor and James D. Stasheff, *Characteristic Classes* (Princeton University Press, 1974), for determinantal varieties and their codimensions.
- [The Matrix Algebra $M_2(\mathbb{C})$](the-matrix-algebra-m2c.html), for the space whose topology is studied here.
- [The Element: Rank, Trace, Determinant, Characteristic Polynomial at $n=2$](the-element-rank-trace-determinant-characteristic-polynomial-at-n-2.html), for the determinant and the rank used here.
- [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), for the cone over the singular set.
