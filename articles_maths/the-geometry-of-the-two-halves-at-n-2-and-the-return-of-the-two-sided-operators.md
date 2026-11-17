# __The Geometry of the Two Halves at $n=2$, and the Return of the Two-Sided Operators__

## Introduction

**The trace form gives the symmetric half a positive definite metric of inertia $(3,0)$ and the antisymmetric half a negative definite metric of inertia $(0,1)$, the determinant gives the symmetric half a Lorentz metric of inertia $(1,2)$, and the two-sided operators act on the matrix algebra as the group $\mathrm{GL}_2\times\mathrm{GL}_2$ whose orbits are the three rank strata.**

The article collects the geometric data of the halves, computes the isometry groups of the two metrics, describes the orbits of the two-sided action, relates the cone of the symmetric half to its Lorentz metric, describes the geodesics, and interprets the two-sided operators as geometric transformations preserving the rank. It assumes *The Two Halves and the Analysis: Smooth Structures at $n=2$*, *The Trace Form and Its Inertia on the Two Halves of $M_2(\mathbb{R})$* and *The Two-Sided Operators and the Segre Cone at $n=2$*.

It follows the biquaternion article *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra* for the same metric data in the biquaternion coordinates.

## The Metric on the Halves

**The trace form is a positive definite metric on the symmetric half and a negative definite metric on the antisymmetric half.**

**Proposition.** On the symmetric half the trace form has the eigenvalues one, one and two, and on the antisymmetric half it has the single eigenvalue minus two; both are nondegenerate.

**Proof.** The Gram matrix of the trace form on the symmetric half in the basis of the two diagonal units and the off-diagonal unit is diagonal with entries one, one and two; on the antisymmetric half the single basis element has squared trace minus two.

**Corollary.** The matrix algebra carries a metric of inertia $(4,4)$ split as three plus one in the real halves and as four plus four in the complex halves.

**Proof.** The trace form is positive definite on the Hermitian half and negative definite on the anti-Hermitian half, and the real halves split the same way by the symmetric and antisymmetric parts.

**Corollary.** The orthogonal complement of a half is the other half, so the halves are the eigenspaces of the transposition with the two signs.

**Proof.** The trace of the product of a symmetric with an antisymmetric matrix is zero, and the dimensions add to the total.

## The Isometry Groups

**Proposition.** The isometries of the trace metric on the matrix algebra form the unitary group of the four-dimensional complex space of matrices, which contains the conjugation by unitary matrices and the two-sided action with unitary parameters.

**Proof.** The trace metric is the standard Hermitian form on the four complex coordinates, whose linear isometries are the unitary matrices of order four; the conjugation and the two-sided action with unitary parameters are unitary for that form.

**Corollary.** The isometries preserving each half are the conjugation by orthogonal matrices on the real halves and by unitary matrices on the complex ones.

**Proof.** An isometry that preserves the symmetric half also preserves its orthogonal complement, which is the antisymmetric half.

**Corollary.** The cone of the symmetric half is preserved by the Lorentz group of inertia $(1,2)$, which is larger than the orthogonal group.

**Proof.** The determinant on the symmetric half is a form of inertia $(1,2)$, and its automorphism group is the Lorentz group of that inertia.

## The Orbits of the Two-Sided Action

**Theorem.** The group $\mathrm{GL}_2(\mathbb{C})\times\mathrm{GL}_2(\mathbb{C})$ acts on the matrix algebra by $(X,Y)\cdot Z=XZY$, and its orbits are the origin, the rank-one matrices and the invertible matrices.

**Proof.** The action preserves the rank by the product formula, and conversely two matrices of the same rank are carried to each other by choosing bases in their images and kernels.

**Corollary.** The orbit of the identity is the group itself, of real dimension eight, and it is open and dense.

**Proof.** The orbit of the identity is the set of invertible matrices, which is open and dense.

**Corollary.** The orbit of a rank-one matrix is the cone of decomposable elements, of real dimension six, with the origin deleted.

**Proof.** A rank-one matrix is carried to any other by the action, and the set of rank-one matrices is the decomposable cone.

## The Cone and the Metric

**Proposition.** The positive semidefinite cone of the symmetric half is a cone of the Lorentz metric of inertia $(1,2)$, and its boundary is the set of null directions of the rank-one form.

**Proof.** The determinant vanishes exactly on the rank-one matrices, which are the null directions of the Lorentz form, and the cone is one of its two time cones.

**Corollary.** The geodesics of the Lorentz metric that stay inside the cone are the rays through the origin and the curves of constant Lorentz length.

**Proof.** The rays are the null geodesics of the cone, and the curves of constant length are the geodesics through the interior points.

**Corollary.** The cone is homogeneous for the Lorentz group of the half, which acts transitively on its interior.

**Proof.** The Lorentz group acts transitively on the interior of its time cone, and the stabiliser of a point is compact.

## Geodesics and the Exponential

**Proposition.** The trace metric on the symmetric half is flat, its geodesics are the straight lines, and its Riemannian exponential at a point $A$ is $S\mapsto A+S$.

**Proof.** The metric is constant in the coordinates of the entries, so the Levi-Civita connection vanishes and the geodesics are the straight lines.

**Proposition.** The matrix exponential is a diffeomorphism from the symmetric half onto the positive definite cone, and it is not the Riemannian exponential of the trace metric.

**Proof.** The exponential of a symmetric matrix is positive definite, its inverse is the logarithm, and the two maps are smooth; it is a different map from the affine displacement of the flat metric.

**Corollary.** The positive definite cone is convex in the flat metric, and every pair of its points is joined by a unique geodesic inside it.

**Proof.** The cone is convex as a set, and the geodesics of the flat metric are the straight segments.

**Corollary.** The exponential map is a diffeomorphism from the symmetric half onto the positive definite cone.

**Proof.** The exponential has the identity as derivative at the origin, is injective on symmetric matrices, and its image is the cone.

## The Return of the Two-Sided Operators

**Proposition.** The two-sided operators that preserve the trace metric are exactly those with unitary parameters, and they form the group of isometries preserving the rank strata.

**Proof.** The two-sided operator multiplies the trace of $Z^{*}Z$ by the product of the squared norms of the parameters, and the isometry condition forces both parameters to be unitary.

**Corollary.** The two-sided operators act by similarities of the trace metric, with ratio the product of the two lengths, so the conformal group of the matrix space contains the group of two-sided operators.

**Proof.** The metric is scaled by the product of the squared norms, which is a single scalar.

**Corollary.** The two-sided operators preserve the Segre cone and act transitively on each rank stratum, so the geometry of the strata is homogeneous.

**Proof.** The orbits of the action are the rank strata, and each is a single orbit.

## Summary

The trace form gives the symmetric half a positive definite metric with the eigenvalues one, one and two and the antisymmetric half a negative definite metric; the matrix algebra carries a metric of inertia $(4,4)$. The isometry group is the unitary group of the Hilbert–Schmidt form, acting by conjugation and by the two-sided action.

The group of two-sided operators has the origin, the rank-one cone and the invertible matrices as its orbits, so its geometry is the geometry of the rank strata. The positive cone of the symmetric half is a Lorentz cone whose null directions are the rank-one matrices, and the two-sided operators act by conformal similarities of the trace metric.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle Z,W\rangle=\operatorname{tr}(Z^{*}W)$ | the trace metric on the algebra |
| $(4,4)$ | its inertia on the whole algebra |
| $(1,2)$ | the inertia of the determinant on the symmetric half |
| $\mathrm{GL}_2\times\mathrm{GL}_2$ | the group of two-sided operators |
| $Z\mapsto XZY$ | the two-sided action |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for symmetric spaces and their geodesics.
- Barrett O'Neill, *Semi-Riemannian Geometry* (Academic Press, 1983), for Lorentz cones and their null directions.
- [The Two Halves and the Analysis: Smooth Structures at $n=2$](the-two-halves-and-the-analysis-smooth-structures-at-n-2.html), for the smooth structures used here.
- [The Trace Form and Its Inertia on the Two Halves of $M_2(\mathbb{R})$](the-trace-form-and-its-signature-on-the-two-halves-of-m2r.html), for the metric of the halves.
- [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), for the operators whose geometry is described here.
