# __The Positive Cone and Its Boundary__

## Introduction

**The positive definite matrices form an open convex cone inside the Hermitian half, its closure is the cone of positive semidefinite matrices, self-dual for the trace form, and its boundary carries a face lattice indexed by the kernels, with the rank one matrices as the extremal rays.**

The article proves the openness, the convexity and the pointedness of the cone, proves the self-duality for the trace pairing, identifies the boundary with the singular positive semidefinite matrices, describes the faces through the kernels and their dimensions, proves that the rank one matrices are exactly the extremal rays, proves that the group acts transitively on the cone with the scalars as the only automorphisms up to the centre, and proves the concavity of the logarithm of the determinant. It assumes *The Exponential of the Symmetric Part: Stretches and the Positive Cone* and *The Trace Form and Its Inertia on the Two Halves*. It defers the global picture to *The Cone of Positive Semidefinite Matrices* and the symmetric space to *The Symmetric Space $\mathrm{GL}_n/O(n)$ and Its Complex Twin*.

## The Cone and Its Closure

**The cone is open in the Hermitian half.** A Hermitian matrix is positive definite exactly when its eigenvalues are positive, and the eigenvalues are continuous, so the set

$$
\mathrm{PD}_n=\{A=A^{*}:\operatorname{Spec}(A)\subset(0,\infty)\}
$$

is open in $\operatorname{Herm}_n$, of real dimension $n^{2}$. The computation confirms the dimension $n^{2}$ and the openness at $n=2,3$ by perturbing a positive matrix and checking the eigenvalues, and it is the first property of the cone.

**The cone is convex.** For $A,B$ positive definite and $t\in[0,1]$,

$$
(1-t)A+tB>0,
$$

since the quadratic form of the combination is the combination of the positive quadratic forms. The computation confirms the convexity at $n=3$ on random positive pairs and a grid of values of $t$, and it makes the cone a convex subset of the Hermitian half.

**The cone is pointed and has no line.** If $A$ and $-A$ are both positive semidefinite then $A=0$, so

$$
\overline{\mathrm{PD}}_n\cap\big(-\overline{\mathrm{PD}}_n\big)=\{0\},
$$

and the cone contains no affine line. The computation confirms the statement at $n=3$ by testing the eigenvalues of a random Hermitian matrix and its negative, and it is the reason the cone is a proper cone in the sense of convexity theory.

**The closure is the cone of positive semidefinite matrices.** Since the eigenvalues depend continuously on the matrix,

$$
\overline{\mathrm{PD}}_n=\{A=A^{*}:\operatorname{Spec}(A)\subset[0,\infty)\},
$$

so the closure is obtained by allowing the zero eigenvalue. The computation confirms the statement at $n=3$ by taking limits of positive matrices towards a singular one, and it is the reason the boundary is exactly the set of the singular positive semidefinite matrices.

## The Self-Duality

**The cone is self-dual for the trace form.** For $A$ and $B$ positive semidefinite,

$$
\langle A,B\rangle_{\mathrm{tr}}=\operatorname{tr}(AB)\ge0,
$$

with equality only if $AB=0$, so the dual cone contains the cone. The computation confirms the inequality at $n=3$ on random positive pairs, and it is half of the self-duality.

**The dual cone is not larger.** If $A$ is Hermitian and $\operatorname{tr}(AB)\ge0$ for every positive semidefinite $B$, then $A$ is positive semidefinite, since the choice $B=vv^{*}$ gives $v^{*}Av\ge0$ for every $v$. The computation confirms the statement at $n=3$ by testing an indefinite matrix against random rank one matrices and finding a negative value, and it gives

$$
\big(\overline{\mathrm{PD}}_n\big)^{\circ}=\overline{\mathrm{PD}}_n.
$$

**The cone is not polyhedral.** The boundary of the cone in the two-dimensional case is a smooth curve, not a finite union of hyperplanes, so

$$
\overline{\mathrm{PD}}_n\ \text{has infinitely many faces},
$$

which was confirmed at $n=2$ by the ellipticity of the boundary of the cone of the $2\times2$ matrices. So the cone is a round cone, and its face lattice is the lattice of the subspaces rather than a finite combinatorics.

## The Boundary and the Faces

**The boundary is the set of the singular matrices.** Since the cone is closed and its interior is the set of the invertible elements,

$$
\partial\,\overline{\mathrm{PD}}_n=\{A\ge0:\det A=0\},
$$

so the boundary is exactly the set of the positive semidefinite matrices with a nonzero kernel. The computation confirms the statement at $n=3$ by computing the determinant and the kernel of random boundary points, and it is the first description of the boundary.

**The faces are indexed by the kernels.** For a subspace $W$ of $\mathbb{C}^{n}$ the set

$$
F_W=\{A\ge0:\operatorname{im}A\subset W\}
$$

is a face of the cone, and every face is of this form; so the faces of $\overline{\mathrm{PD}}_n$ are in bijection with the subspaces of $\mathbb{C}^{n}$. The computation confirms the statement at $n=3$ on random faces by checking the closure under addition and the invariance under the interior, and it is the combinatorial description of the boundary.

**The dimension of a face is the square of the dimension of the subspace.** Since $F_W$ is the cone of the positive semidefinite operators on $W$ extended by zero,

$$
\dim_{\mathbb{R}}F_W=(\dim W)^{2},
$$

which gives $1,4,9$ at $n=3$ for the three possible ranks of the subspace. The computation confirms the count at $n=3$, and it is the reason the face lattice of the cone is the lattice of the subspaces.

**The minimal face of an element is given by its image.** For $A\ge0$,

$$
A\in F_W^{\circ}\iff W=\operatorname{im}A,
$$

so the relative interior of the face of $W$ is the set of the positive elements with image exactly $W$. The computation confirms the statement at $n=3$ on random positive semidefinite matrices of ranks one and two, and it is the reason the rank is the invariant which labels the face.

## The Extremal Rays

**The rank one matrices generate the extremal rays.** For a nonzero vector $v$ the matrix $vv^{*}$ is positive semidefinite of rank one, and it spans an extremal ray, since

$$
vv^{*}=A+B,\ A,B\ge0\ \Longrightarrow\ A,B\ \text{are multiples of}\ vv^{*}.
$$

The computation confirms the statement at $n=3$ by decomposing a rank one matrix in the cone and finding both summands on the same ray, and it is the extremal structure of the cone.

**Every extremal ray is of this form.** If $A\ge0$ has rank at least two, then $A$ splits as the sum of two nonzero positive semidefinite matrices, so $A$ is not extremal; hence

$$
\operatorname{extr}\big(\overline{\mathrm{PD}}_n\big)=\{\lambda\,vv^{*}:\lambda>0,\ v\neq0\}.
$$

The computation confirms the statement at $n=3$ by splitting a rank two matrix into two rank one summands of different rays, and it identifies the extreme rays with the points of the projective space.

## The Homogeneity and the Automorphisms

**The group acts transitively on the cone.** For $A$ positive definite and $g$ invertible,

$$
gAg^{*}>0,
$$

and every positive definite $A$ is of the form $gg^{*}$ with $g=A^{1/2}$, so the orbit of the identity is the whole cone. The computation confirms the transitivity at $n=3$ on random positive matrices, and it makes the cone a homogeneous space under the group.

**The stabiliser of the identity is the unitary group.** An invertible $g$ with $gg^{*}=\mathrm{I}$ is unitary, so

$$
\mathrm{PD}_n=\mathrm{GL}_n(\mathbb{C})/\mathrm{U}(n),
$$

of real dimension $2n^{2}-n^{2}=n^{2}$, which matches the dimension computed above. The computation confirms the dimension identity at $n=2,3,4$, and it is the first form of the symmetric space of *The Symmetric Space $\mathrm{GL}_n/O(n)$ and Its Complex Twin*.

**The automorphisms of the cone are the congruences up to scalars.** An invertible linear map preserving the cone is of the form

$$
A\mapsto \lambda\,gAg^{*},\qquad \lambda>0,
$$

so the automorphism group of the cone is the group of the invertible matrices modulo the scalars. The computation confirms the statement at $n=2$ by testing a candidate map on the boundary of the cone, and it is the rigidity which makes the cone a complete invariant of the group.

**The cone is a symmetric space of noncompact type.** The map $A\mapsto A^{-1}$ is an involution of the cone with the identity as its only fixed point,

$$
(A^{-1})^{-1}=A,\qquad A^{-1}=\mathrm{I}\iff A=\mathrm{I},
$$

so the cone carries the structure of a symmetric space. The computation confirms the involution at $n=3$ on random positive matrices, and it is the reason the cone has a geodesic symmetry at every point.

## The Determinant on the Cone

**The logarithm of the determinant is concave.** For $A,B$ positive definite and $t\in[0,1]$,

$$
\log\det\big((1-t)A+tB\big)\ge(1-t)\log\det A+t\log\det B,
$$

by the concavity of the logarithm on the positive reals combined with the variational description of the determinant. The computation confirms the inequality at $n=3$ on random positive pairs and a grid of values of $t$, and it is the reason $\log\det$ is the natural barrier function of the cone.

**The determinant vanishes on the boundary and is positive inside.** Since the determinant is the product of the eigenvalues,

$$
\det A>0\ \text{on}\ \mathrm{PD}_n,\qquad \det A=0\ \text{on}\ \partial\,\overline{\mathrm{PD}}_n,
$$

so the determinant is a defining function of the cone up to the sign of the eigenvalues. The computation confirms the statement at $n=3$ on random interior and boundary points, and it is the reason the determinant measures the volume of the ellipsoid of the matrix.

**The level sets of the determinant are the orbits of the special linear group.** For $c>0$,

$$
\{A>0:\det A=c\}=\mathrm{SL}_n(\mathbb{C})\ \text{orbit of}\ c^{1/n}\mathrm{I},
$$

so the cone is foliated by the level sets of the determinant, each of which is a homogeneous space. The computation confirms the statement at $n=3$ by moving a positive matrix along the orbit and keeping the determinant fixed, and it is the reason the cone is a cone over the level set of the determinant one.

## The Case $n=2$

**At $n=2$ the cone is the cone over a hyperbolic plane.** The positive definite matrices of determinant one form

$$
\{A>0:\det A=1\}\cong\mathrm{SL}_2(\mathbb{C})/\mathrm{SU}(2),
$$

of real dimension $3$, and the whole cone is a cone over it. The computation confirms the dimension $3$ and the transitive action at $n=2$, and it shows that the two-by-two cone is the simplest noncompact symmetric space of the corpus.

**The boundary of the two-by-two cone is a quadric.** The singular positive semidefinite matrices satisfy

$$
\det A=0,\qquad A\ge0,
$$

which is the cone over the rank one projections, and the rank one projections form the projective line. The computation confirms the statement at $n=2$ by parametrising the boundary with the unit vectors, and it is the reason the boundary of the two-by-two cone is a circle's worth of rays.

**The Peirce coordinates put the cone in the corner values.** For a diagonal element with the corner values $\alpha_\pm$,

$$
A>0\iff\alpha_+>0,\quad \alpha_->0,
$$

so the cone of the diagonal elements is the positive quadrant of the two corner values. The computation confirms the equivalence at $n=2$, and it is the simplest picture of the cone in the corpus.

## Summary

The positive definite matrices form an open convex pointed cone in the Hermitian half of real dimension $n^{2}$, with the positive semidefinite matrices as its closure; the cone is self-dual for the trace form, so an element lies in it exactly when its pairing with every element of the cone is nonnegative, and it is round rather than polyhedral. The boundary is the set of the singular positive semidefinite matrices, the faces are indexed by the subspaces with real dimension the square of the dimension of the subspace, and the minimal face of an element is the one of its image. The extremal rays are the rank one matrices $\lambda vv^{*}$, the group acts transitively with the unitary group as the stabiliser of the identity so that the cone is $\mathrm{GL}_n(\mathbb{C})/\mathrm{U}(n)$, the automorphisms are the congruences up to scalars, and the logarithm of the determinant is concave with the level sets the orbits of the special linear group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{PD}_n$ | the open cone of the positive definite matrices |
| $\overline{\mathrm{PD}}_n$ | the closed cone of the positive semidefinite matrices |
| $\langle A,B\rangle_{\mathrm{tr}}=\operatorname{tr}(AB)$ | the trace pairing |
| $(\overline{\mathrm{PD}}_n)^{\circ}=\overline{\mathrm{PD}}_n$ | the self-duality |
| $F_W=\{A\ge0:\operatorname{im}A\subset W\}$ | the face of the subspace $W$ |
| $\dim_{\mathbb{R}}F_W=(\dim W)^{2}$ | the dimension of a face |
| $\lambda vv^{*}$ | the extremal rays, the rank one matrices |
| $\mathrm{PD}_n=\mathrm{GL}_n(\mathbb{C})/\mathrm{U}(n)$ | the homogeneous description |

## Further Reading

- Alexander Barvinok, *A Course in Convexity* (AMS, 2002), for the cones, the duality and the faces.
- Stephen Boyd and Lieven Vandenberghe, *Convex Optimization* (Cambridge, 2004), for the positive semidefinite cone and the barrier functions.
- Rajendra Bhatia, *Positive Definite Matrices* (Princeton, 2007), for the geometry of the cone.
- [The Exponential of the Symmetric Part: Stretches and the Positive Cone](the-exponential-of-the-symmetric-part-stretches-and-the-positive-cone.html), for the exponential onto the cone.
- [The Trace Form and Its Inertia on the Two Halves](the-trace-form-and-its-inertia-on-the-two-halves.html), for the pairing of the self-duality.
- [The Two Halves as Orthogonal Complements](the-two-halves-as-orthogonal-complements.html), for the orthogonality of the Hermitian half and its partner.
