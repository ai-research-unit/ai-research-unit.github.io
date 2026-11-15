# __The Positive Cone and Its Boundary at $n=4$__

## Introduction

**The set $\operatorname{Herm}_4^{++}$ of positive definite Hermitian matrices is an open convex cone of real dimension $16$, homogeneous under the congruence action of $\mathrm{GL}_4(\mathbb{C})$, self-dual for the Hilbert–Schmidt form, with a boundary stratified by rank into pieces of dimensions $15$, $12$, $7$ and $0$ and with faces indexed by the subspaces of $\mathbb{C}^{4}$; the logarithm of the determinant is concave on it, and the real symmetric cone of dimension $10$ is the fixed part of the conjugation.**

The article establishes openness, convexity and the dimension, describes the closure as the set of positive semidefinite matrices and the order it defines, computes the rank strata and their dimensions, identifies the faces with the subspaces and the extremal rays with the projective space, proves the concavity of $\log\det$, identifies the automorphism group with the congruence action of the general linear group, and compares with the real symmetric cone and with the Jordan reading of the same set inside $\operatorname{Sym}_4$.

It assumes *The Exponential of the Symmetric Part: Stretches and the Positive Cone at $n=4$*, *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric* and *The Cone of Positive Semidefinite Matrices at $n=4$*. The model at order two is *The Positive Cone in $\operatorname{Herm}_2$ and Its Boundary*.

## The Open Cone

**Definition.** $\operatorname{Herm}_4^{++}=\{A:A^{\ast}=A,\ \langle Ax,x\rangle>0\text{ for }x\neq0\}$.

**Proposition.** $\operatorname{Herm}_4^{++}$ is open in $\operatorname{Herm}_4$, convex, and of real dimension $16$.

**Proof.** The set of Hermitian matrices with all eigenvalues positive is defined by the inequalities $\lambda_{\min}>0$, and the smallest eigenvalue is continuous, so the set is open; a convex combination of two positive definite forms is positive definite; the ambient Hermitian space has real dimension $16$.

**Corollary.** The cone is invariant under congruence by invertible matrices: if $A$ is positive definite then $g^{\ast}Ag$ is positive definite for every invertible $g$, and the action is transitive.

**Proof.** $\langle g^{\ast}Agx,x\rangle=\langle A(gx),gx\rangle>0$ for $x\neq0$, and every positive definite $A$ is $g^{\ast}g$ for $g=A^{1/2}$.

**Corollary.** The cone is homogeneous under $\mathrm{GL}_4(\mathbb{C})$ and stable under the unitary group, so it is a symmetric cone.

**Proof.** Transitivity and the existence of an involution at each point, given by the stabiliser of the point.

**Corollary.** The exponential is a diffeomorphism $\operatorname{Herm}_4\to\operatorname{Herm}_4^{++}$, so the cone is also the set of exponentials of Hermitian matrices.

**Proof.** The spectral theorem and the logarithm of the eigenvalues.

**The set of squares.** The cone is exactly the set of products $B^{\ast}B$ with $B$ invertible, and the closure is the set of $B^{\ast}B$ with $B$ arbitrary.

**Proof.** $B^{\ast}B$ is positive semidefinite, and every positive semidefinite $A$ is $B^{\ast}B$ with $B=A^{1/2}$.

## The Closure and the Order

**Proposition.** The closure $\operatorname{Herm}_4^{+}$ is the set of positive semidefinite matrices, that is the set of Hermitian matrices with all eigenvalues nonnegative.

**Proof.** The limit of a sequence of positive definite matrices is positive semidefinite by continuity of the eigenvalues; conversely a positive semidefinite matrix is a limit of $A+\varepsilon\mathrm I$.

**Corollary.** The interior of the closure is the open cone, and the closure is a closed convex cone which is pointed: it contains no line.

**Proof.** Interior by the eigenvalue criterion; pointed because $A$ and $-A$ both positive semidefinite forces $A=0$.

**Corollary.** The cone defines a partial order by $A\ge B$ iff $A-B$ is positive semidefinite, and the order is compatible with addition and with congruence.

**Proof.** The cone is closed under addition and under congruence.

**Corollary.** $\operatorname{tr}A>0$ and $\det A\ge0$ on the closure, with equality in the determinant exactly on the boundary.

**Proof.** Sum and product of nonnegative eigenvalues.

## The Strata

**Theorem.** The set of positive semidefinite matrices of rank exactly $r$ has real dimension $r(8-r)$: the values are $16$, $15$, $12$, $7$ and $0$ for $r=4,3,2,1,0$.

**Proof.** A positive semidefinite matrix of rank $r$ is $B^{\ast}B$ with $B$ a $4\times r$ matrix of rank $r$; the map $B\mapsto B^{\ast}B$ has fibres the unitary group of order $r$, so the dimension is $2\cdot4r-r^{2}=r(8-r)$.

**Corollary.** The boundary of the open cone is the union of the strata of rank at most three, of dimensions $15$, $12$, $7$ and $0$, and the stratum of rank three is the smooth part of the boundary of largest dimension.

**Proof.** The dimensions and the rank stratification.

**Corollary.** The boundary is a hypersurface in the ambient space, smooth on the rank-three stratum, and its singular locus is the set of matrices of rank at most two, of dimension $12$, of codimension three in the boundary.

**Proof.** The rank-three stratum has dimension $15$, one less than the ambient space, and the determinant has a nonzero derivative there; the singular part drops to $12$.

**Corollary.** The cone is not polyhedral, since a polyhedral cone in a space of dimension $16$ has finitely many extremal rays, whereas the extremal rays here form the three-dimensional projective space.

**Proof.** A polyhedral cone is the convex hull of finitely many rays.

## The Faces and the Extremal Rays

**Definition.** A **face** of the cone is a subset $F$ such that $A+B\in F$ with $A,B$ in the cone forces $A,B\in F$.

**Proposition.** The faces are exactly the sets
$$
F_W=\{A\ge0:\ker A\supset W\}
$$
for a subspace $W\subset\mathbb{C}^{4}$, and $F_W$ is isomorphic to the cone of positive semidefinite operators on $\mathbb{C}^{4}/W$.

**Proof.** If $A+B$ vanishes on $W$ then each summand does, since each is positive semidefinite; conversely each $F_W$ is a face by the same argument.

**Corollary.** The faces are indexed by the subspaces, so there are faces of each dimension $\dim F_W=(4-\dim W)^{2}$, and the face lattice is the lattice of subspaces.

**Proof.** The cone on a space of dimension $4-\dim W$ has real dimension $(4-\dim W)^{2}$.

**Corollary.** The extremal rays are the faces of dimension one, that is the rank-one positive semidefinite matrices, and they are parametrised by the projective space $\mathbb{P}^{3}$.

**Proof.** A rank-one positive semidefinite matrix is $vv^{\ast}$ for a nonzero vector $v$, and two vectors give the same matrix exactly when they are proportional.

**The dual cone.** The cone is self-dual for the Hilbert–Schmidt form: $A$ is positive semidefinite exactly when $\langle A,B\rangle\ge0$ for every positive semidefinite $B$.

**Proof.** For $B=vv^{\ast}$ the pairing is $\langle Av,v\rangle$, so the condition is positivity on every vector; conversely a positive semidefinite $A$ pairs nonnegatively with every positive semidefinite $B$ by the spectral decomposition of $B$.

## The Concavity of the Logarithm

**Theorem.** The function $A\mapsto\log\det A$ is concave on $\operatorname{Herm}_4^{++}$ and tends to $-\infty$ at the boundary.

**Proof.** Concavity follows from the variational formula $\log\det A=\min_{B>0}\{\operatorname{tr}(AB)-\log\det B-4\}$, a minimum of affine functions; the boundary behaviour follows from the vanishing of the determinant.

**Corollary.** The function $\log\det$ is strictly concave along any line segment joining two distinct points of the cone unless the two points are proportional.

**Proof.** The equality case in the variational formula.

**Corollary.** $\log\det$ is invariant under congruence by matrices of determinant of modulus one, and shifts by $2\log|\det g|$ under a general congruence.

**Proof.** $\det(g^{\ast}Ag)=|\det g|^{2}\det A$.

**The trace functional.** $\operatorname{tr}$ is linear and positive on the closure, and its level sets are the compact sections of the cone; the section $\{\operatorname{tr}A=1\}$ is a compact convex set of dimension $15$.

**Proof.** Positivity on the cone, and the eigenvalues bounded by the trace, giving compactness.

**Corollary.** The cone is the cone over the compact section, and every ray meets the section exactly once.

**Proof.** Scaling.

## The Automorphism Group

**Theorem.** The identity component of the automorphism group of the cone is the image of $\mathrm{GL}_4(\mathbb{C})$ acting by congruence $A\mapsto g^{\ast}Ag$, modulo the scalars of modulus one.

**Proof.** A linear automorphism of the cone preserves the cone and hence the order and the faces; the classical theorem of the symmetric cone identifies the automorphism group with the conformal group of the underlying form, which for the Hermitian cone is the congruence action of the general linear group, with the scalars of modulus one acting trivially.

**Corollary.** The group acts transitively on the interior and on each rank stratum, so each stratum is a homogeneous space.

**Proof.** Transitivity on the interior by the square root; on a stratum of rank $r$ by the reduction to a fixed projection.

**Corollary.** The stabiliser of the identity is the unitary group, so the interior is $\mathrm{GL}_4/U(4)$, of real dimension $16$.

**Proof.** $g^{\ast}g=\mathrm I$ exactly for unitary $g$.

## The Jordan Reading and the Real Contrast

**Proposition.** Inside the Jordan algebra $\operatorname{Sym}_4$ of the real symmetric matrices the set of squares is the closed cone of positive semidefinite symmetric matrices, of real dimension $10$, and it is a symmetric cone of rank $4$.

**Proof.** The square of a real symmetric matrix is positive semidefinite, and every positive semidefinite symmetric matrix is a square; the dimension is the number of independent entries.

**Corollary.** The Hermitian cone is not a Jordan-algebra cone over $\mathbb{C}$: over $\mathbb{C}$ the set of squares of symmetric complex matrices is the whole space, since every complex number is a square.

**Proof.** A complex symmetric matrix $S$ has $S=T^{2}$ for a complex symmetric $T$ because the eigenvalues have square roots over $\mathbb{C}$.

**Corollary.** The two cones agree over the reals as the fixed part of the conjugation, and the complex cone is the Hermitian one, which is not the complexification of the real one.

**Proof.** The Hermitian involution and the plain transpose have different fixed sets.

**The count.** Real dimensions: Hermitian cone $16$, real symmetric cone $10$.

**Proof.** The dimensions of the two ambient spaces.

## Summary

The positive definite Hermitian matrices form an open convex cone of real dimension sixteen, homogeneous under congruence by the general linear group, self-dual for the Hilbert–Schmidt form, and equal to the set of squares $B^{\ast}B$ of invertible matrices. Its closure is the set of positive semidefinite matrices and defines the Loewner order.

The boundary is stratified by rank with dimensions $15$, $12$, $7$ and $0$; the faces are indexed by subspaces with dimension $(4-\dim W)^{2}$, so the extremal rays are parametrised by $\mathbb{P}^{3}$. The logarithm of the determinant is concave, and the trace is a positive linear functional with compact sections.

The automorphism group is the congruence action of $\mathrm{GL}_4(\mathbb{C})$ modulo the scalars of modulus one, the stabiliser of the identity is $U(4)$, and the interior is $\mathrm{GL}_4/U(4)$. The real symmetric cone of dimension ten is the fixed part of the conjugation and the set of squares in the Jordan algebra; over $\mathbb{C}$ the set of squares of symmetric matrices is everything, so the Hermitian cone is genuinely a different object.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Herm}_4^{++}$ | the open cone, real dimension $16$ |
| $\operatorname{Herm}_4^{+}$ | the closure, positive semidefinite |
| $r(8-r)$ | the dimension of the rank-$r$ stratum |
| $F_W=\{A\ge0:\ker A\supset W\}$ | a face |
| $\mathbb{P}^{3}$ | the extremal rays |
| $g^{\ast}Ag$ | the congruence action |

## Further Reading

- Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones* (Oxford, 1994), for symmetric cones, faces and the automorphism group.
- [The Exponential of the Symmetric Part: Stretches and the Positive Cone at $n=4$](the-exponential-of-sym-4-stretches-and-the-positive-cone.html), for the exponential onto the cone.
- [The Cone of Positive Semidefinite Matrices at $n=4$](the-cone-of-positive-semidefinite-matrices-at-n-4.html), for the self-duality and the faces in detail.
- [The Positive Cone in $\operatorname{Herm}_2$ and Its Boundary](the-positive-cone-in-herm-2-and-its-boundary.html), for the case at order two.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric](the-two-halves-over-r-symmetric-and-antisymmetric-at-n-4.html), for the real symmetric cone.
