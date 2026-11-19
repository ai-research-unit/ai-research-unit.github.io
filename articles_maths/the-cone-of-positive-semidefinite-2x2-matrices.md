# __The Cone of Positive Semidefinite $2\times2$ Matrices__

## Introduction

**In dimension two the positive semidefinite cone is described by three scalar inequalities, it is the set of squares of symmetric matrices, it is a spectrahedron cut out by one linear matrix inequality, and its ranks stratify it into the origin, the extreme rays and the interior; the function minus the logarithm of the determinant is a barrier with parameter two.**

The article gives the minor description of the cone, identifies it with the cone of squares, writes it as the feasible set of a linear matrix inequality, describes the stratification by rank, examines the determinant barrier and the analytic centre, and states the semidefinite programme of order two. It assumes *The Positive Cone in $\mathrm{Herm}_2$ and Its Boundary*, *The Jordan Algebra $\operatorname{Sym}_2$* and *The Elementary Symmetric Functions: $\operatorname{tr}$ and $\det$ in Dimension Two*.

It follows the biquaternion article *The Square Roots of One and the Idempotents of the Biquaternion Algebra* for the rank-one extreme rays of the same cone.

## The Description by Minors

**Proposition.** A real symmetric matrix is positive semidefinite exactly when its two diagonal entries and its determinant are nonnegative.

**Proof.** The eigenvalues of a symmetric matrix of order two are the roots of a quadratic with the given trace and determinant, and the two conditions say that both roots are nonnegative; the converse is immediate from the spectral theorem.

**Corollary.** The cone is a basic semialgebraic set defined by one linear inequality in each diagonal entry and one quadratic inequality in the three coordinates.

**Proof.** The determinant is $ac-b^{2}$, a quadratic function of the three coordinates.

**Corollary.** Over the region of positive diagonal entries the cone is described by the convex inequality $c\ge b^{2}/a$, so it is the epigraph of a convex quadratic function of the off-diagonal coordinate.

**Proof.** The condition $ac\ge b^{2}$ with positive diagonal entries is the stated inequality, and the function $b^{2}/a$ is convex in $b$.

## The Cone of Squares

**Theorem.** The positive semidefinite cone is exactly the set of squares $B^{2}$ of symmetric matrices $B$, and it is exactly the set of products $CC^{\mathsf T}$.

**Proof.** The square of a symmetric matrix has the squared eigenvalues, which are nonnegative, and the spectral theorem writes every positive semidefinite matrix as the square of its own square root; the product $CC^{\mathsf T}$ is positive semidefinite because its quadratic form is a squared norm.

**Corollary.** The cone of squares is closed under addition, and it is the smallest closed convex cone containing the squares of the symmetric matrices.

**Proof.** A sum of squares of symmetric matrices is a positive semidefinite matrix, and every positive semidefinite matrix is a single square.

**Corollary.** The squares of the antisymmetric matrices are negative semidefinite, so they meet the cone only at the origin.

**Proof.** The square of an antisymmetric matrix of order two is a negative multiple of the identity, whose eigenvalues are nonpositive.

## The Spectrahedron Description

**Proposition.** The cone is the feasible set of a single linear matrix inequality: the matrix $\sum x_{i}A_{i}$ is positive semidefinite for three fixed symmetric matrices $A_{i}$ forming a basis.

**Proof.** Writing the matrix in the basis of the three symmetric units gives a linear matrix-valued function of the coordinates, and the inequality is the positive semidefinite condition.

**Corollary.** The cone is a spectrahedron, and in dimension two every spectrahedron defined by one inequality of order two is a cone of this type up to an affine change of coordinates.

**Proof.** A linear matrix inequality of order two is a linear family of symmetric matrices, whose positive semidefinite set is the preimage of the cone under an affine map.

**Corollary.** The dual cone is again a cone of the same type, defined by the dual inequalities.

**Proof.** The cone is self-dual for the trace form, so its dual is itself up to the linear identification.

## The Stratification by Rank

**Proposition.** The cone is the disjoint union of the origin, the two-dimensional set of rank-one matrices, and the three-dimensional interior of positive definite matrices.

**Proof.** The rank of a symmetric matrix is zero, one or two; the rank-one positive semidefinite matrices form the cone over the circle of directions, of real dimension two, and the interior has the dimension of the symmetric half.

**Corollary.** The rank-one stratum is the boundary of the cone, and it is a smooth manifold away from the origin.

**Proof.** A rank-one matrix is on the boundary because it is singular, and the rank-one set is the cone over the circle of directions.

**Corollary.** The rank function is upper semicontinuous, and its jumps define the strata.

**Proof.** The rank can only drop in a limit, and the strata are the level sets of the rank.

**Corollary.** The closure of the interior is the whole cone, and the closure of the rank-one stratum is the rank-one stratum with the origin added.

**Proof.** Every semidefinite matrix is a limit of positive definite matrices, and every rank-one matrix is a limit of rank-one matrices.

## The Determinant Barrier

**Proposition.** The function $F(X)=-\log\det X$ is smooth, convex and strictly convex on the interior of the cone, and it tends to infinity at the boundary.

**Proof.** The determinant is positive on the interior, its logarithm is concave there by the matrix analogue of the logarithmic inequality, and the divergence at the boundary follows from the vanishing of an eigenvalue.

**Corollary.** The function is a self-concordant barrier with parameter two, and its minimiser over a bounded section is the analytic centre.

**Proof.** The barrier parameter of minus the logarithm of the determinant on the cone of positive definite matrices of order two is two, the order of the matrices.

**Corollary.** The gradient of the barrier at a matrix is minus the inverse, and the Hessian is the quadratic form of the inverse on both sides.

**Proof.** The derivative of the logarithm of the determinant is the trace of the inverse times the increment, and the second derivative follows by differentiating again.

## Semidefinite Programming

**Proposition.** A semidefinite programme of order two minimises a linear function over an affine slice of the cone, and its dual is another such programme over the dual slice.

**Proof.** The primal problem is the minimisation of a linear functional over the intersection of the cone with an affine subspace, and the Lagrangian dual is obtained by pairing with a dual matrix.

**Corollary.** Strong duality holds when the two programmes have strictly feasible points, and the optimal values then agree.

**Proof.** Slater's condition for a convex programme with a nonempty interior gives strong duality.

**Corollary.** The optimal set, when it is nonempty, is a face of the feasible slice, and the complementary slackness conditions couple the primal and the dual matrices.

**Proof.** The optimum of a linear function over a convex set is attained on a face, and the slackness conditions are the equality case of the duality inequality.

## Summary

In dimension two the positive semidefinite cone is defined by the nonnegativity of the two diagonal entries and of the determinant, and it is exactly the set of squares of symmetric matrices and of products of a matrix with its transpose. It is a spectrahedron cut out by one linear matrix inequality of order two, self-dual for the trace form.

Its strata are the origin, the rank-one boundary and the positive definite interior, and the negative logarithm of the determinant is a self-concordant barrier of parameter two whose gradient is minus the inverse. Semidefinite programmes of order two obey strong duality under Slater's condition.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Sym}_2^{+}$ | the positive semidefinite cone |
| $B^{2}$, $CC^{\mathsf T}$ | the descriptions as squares and products |
| $-\log\det X$ | the determinant barrier |
| $\nu=2$ | the barrier parameter |
| $\langle C,X\rangle$ | the objective of the semidefinite programme |

## Further Reading

- Stephen Boyd and Lieven Vandenberghe, *Convex Optimization* (Cambridge University Press, 2004), for semidefinite programmes and barriers.
- Yurii Nesterov and Arkadii Nemirovski, *Interior-Point Polynomial Algorithms in Convex Programming* (SIAM, 1994), for self-concordant barriers.
- [The Positive Cone in $\mathrm{Herm}_2$ and Its Boundary](the-positive-cone-in-herm-2-and-its-boundary.html), for the complex analogue of the cone.
- [The Jordan Algebra $\operatorname{Sym}_2$](the-jordan-algebra-sym-2.html), for the algebra in which the cone is the cone of squares.
- [The Elementary Symmetric Functions: $\operatorname{tr}$ and $\det$ in Dimension Two](the-elementary-symmetric-functions-trace-and-determinant-in-dimension-two.html), for the two invariants defining the cone.
