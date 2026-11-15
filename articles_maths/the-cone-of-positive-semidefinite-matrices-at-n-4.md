# __The Cone of Positive Semidefinite Matrices at $n=4$__

## Introduction

**The set $\operatorname{Herm}_4^{+}$ of positive semidefinite matrices is the set of products $A^{\ast}A$, it is a closed convex pointed cone with nonempty interior in the real space of dimension $16$, it is self-dual for the Hilbert–Schmidt form, its faces correspond one-to-one to the subspaces and hence to the Hermitian idempotents and the Grassmannians, its boundary stratifies by rank, its trace sections are compact, and it is attached to the Hermitian involution rather than to the plain transpose.**

The article proves the description as a set of products, the four convex-geometric properties, the self-duality, the correspondence between faces, subspaces, idempotents and Grassmannians, the rank stratification, the compactness of the trace sections, and the reason the cone uses the Hermitian involution: the plain transpose gives the indefinite biquaternion norm, which has no cone.

It assumes *The Positive Cone and Its Boundary at $n=4$* for the open cone, *The Space of Idempotents and the Flag Varieties at $n=4$* for the Grassmannians and *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric* for the real comparison. The model at order two is *The Cone of Positive Semidefinite $2\times2$ Matrices*.

## The Cone as the Set of Products

**Definition.** $\operatorname{Herm}_4^{+}=\{A:A^{\ast}=A,\ \langle Ax,x\rangle\ge0\text{ for all }x\}$.

**Theorem.** $\operatorname{Herm}_4^{+}=\{B^{\ast}B:B\in M_4(\mathbb{C})\}$, and the interior is $\{B^{\ast}B:B\text{ invertible}\}$.

**Proof.** $B^{\ast}B$ is Hermitian and $\langle B^{\ast}Bx,x\rangle=\lVert Bx\rVert^{2}\ge0$; conversely a positive semidefinite $A$ is $A^{1/2}A^{1/2}$ by the spectral theorem, and it is positive definite exactly when $A^{1/2}$ is invertible.

**Corollary.** The cone is the image of the polynomial map $B\mapsto B^{\ast}B$, which is surjective and has the unitary orbits as fibres.

**Proof.** $B^{\ast}B=(UB)^{\ast}(UB)$ for unitary $U$, and the map is constant on those orbits; conversely $B^{\ast}B=C^{\ast}C$ forces $C=UB$ for a unitary $U$ on the image.

**Corollary.** The cone is invariant under congruence $A\mapsto g^{\ast}Ag$, and the action of $\mathrm{GL}_4$ is transitive on the interior.

**Proof.** $g^{\ast}(B^{\ast}B)g=(Bg)^{\ast}(Bg)$.

**The extreme case.** The rank-one elements of the cone are the $vv^{\ast}$ with $v\neq0$, and they generate the cone as a convex hull.

**Proof.** The spectral decomposition of a positive semidefinite matrix as a sum of rank-one terms.

## Closed, Convex, Pointed, Full

**Proposition.** $\operatorname{Herm}_4^{+}$ is closed, convex, pointed and has nonempty interior in $\operatorname{Herm}_4$.

**Proof.** Closed: the limit of positive semidefinite matrices is positive semidefinite. Convex: a convex combination of two positive semidefinite forms is positive semidefinite. Pointed: $A$ and $-A$ in the cone force $A=0$. Interior: the positive definite matrices are open and nonempty in the sixteen-dimensional space.

**Corollary.** The cone defines a partial order by $A\ge B$ iff $A-B\ge0$, compatible with addition and with congruence.

**Proof.** The four properties.

**Corollary.** The order is antisymmetric: $A\ge B$ and $B\ge A$ together force $A=B$.

**Proof.** Pointedness of the cone.

**The section.** The intersection of the cone with the affine hyperplane $\{\operatorname{tr}A=1\}$ is a compact convex set of real dimension $15$, and every nonzero element of the cone is a positive multiple of an element of the section.

**Proof.** The eigenvalues are bounded by the trace, so the section is closed and bounded in a finite-dimensional space; scaling gives the second statement.

## Self-Duality

**Theorem.** The cone is self-dual: $A\in\operatorname{Herm}_4^{+}$ if and only if $\langle A,B\rangle=\operatorname{tr}(AB)\ge0$ for every $B\in\operatorname{Herm}_4^{+}$.

**Proof.** If $A$ is positive semidefinite then so is every summand in the spectral decomposition of $B$, and each pairing with a rank-one $vv^{\ast}$ is $\langle Av,v\rangle\ge0$. Conversely if the pairing is nonnegative against every $vv^{\ast}$, then $\langle Av,v\rangle\ge0$ for all $v$, so $A$ is positive semidefinite.

**Corollary.** The dual cone is the cone itself, so the cone is the set of linear functionals nonnegative on it, read through the inner product.

**Proof.** The definition of the dual and the theorem.

**Corollary.** The trace functional is interior to the dual cone, and it is the sum of the four coordinate functionals in any orthonormal eigenbasis.

**Proof.** The trace is positive on every nonzero element of the cone.

**The automorphism group.** The linear automorphisms of the cone form the congruence action of $\mathrm{GL}_4$ modulo the scalars of modulus one, of real dimension $32$.

**Proof.** The automorphism group of a self-dual homogeneous cone.

## The Faces, the Idempotents and the Grassmannians

**Theorem.** The faces of the cone are the sets $F_W=\{A\ge0:AW=0\}$ for subspaces $W\subset\mathbb{C}^{4}$, and the map $W\mapsto F_W$ is a bijection onto the faces reversing inclusions.

**Proof.** If $A+B$ vanishes on $W$ then both do, since each is positive semidefinite and their sum vanishes on a vector only if each vanishes there; conversely each $F_W$ is a face.

**Corollary.** Writing $E$ for the orthogonal projection onto $W^{\perp}$, the face is $F_W=\{A\ge0:A=EAE\}$, so the faces correspond one-to-one to the Hermitian idempotents.

**Proof.** $AW=0$ means the image of $A$ is orthogonal to $W$, hence inside $W^{\perp}$, hence $A=EA$.

**Corollary.** The faces of dimension one are the extremal rays, and they are parametrised by $\mathbb{P}^{3}$; the faces of dimension $(4-\dim W)^{2}$ correspond to the Grassmannians, so the face lattice is the lattice of subspaces.

**Proof.** Rank-one positive semidefinite matrices up to positive scaling, and the dimension of the cone on a space of dimension $4-\dim W$.

**Corollary.** The relative interior of the face $F_W$ is the set of matrices of rank $4-\dim W$ with image exactly $W^{\perp}$, and the cone is the disjoint union of these relative interiors.

**Proof.** The rank and the image determine the stratum.

## The Boundary Strata

**Proposition.** The set of positive semidefinite matrices of rank $r$ has real dimension $r(8-r)$, giving $16$, $15$, $12$, $7$ and $0$; the boundary is the union of the strata with $r\le3$.

**Proof.** The dimension count from the factorisation $B^{\ast}B$ with $B$ of size $4\times r$ of rank $r$.

**Corollary.** The boundary is a hypersurface whose smooth part is the rank-three stratum, and it is singular along the stratum of rank two, of dimension $12$.

**Proof.** The comparison of the dimensions with the ambient sixteen.

**Corollary.** Each stratum is a homogeneous space of $\mathrm{GL}_4$, and the strata are the orbits of the congruence action on the cone.

**Proof.** Transitivity on each rank.

**The faces against the strata.** A face is a union of strata, and its relative interior is one stratum, so the two decompositions are coarser and finer readings of the same cone.

**Proof.** The face $F_W$ is the union of the strata of rank at most $4-\dim W$ with image inside $W^{\perp}$.

## Trace Sections

**Proposition.** The section $\{\operatorname{tr}A=1\}$ is a compact convex set whose extreme points are the rank-one elements $vv^{\ast}$ with $\lVert v\rVert=1$.

**Proof.** Compactness from the bound on the eigenvalues; an extreme point of the section must be of rank one, since a sum of two positive semidefinite matrices of rank at least one can be split.

**Corollary.** The cone is the cone over the section, so it is the convex hull of its extremal rays, of which there are as many as points of $\mathbb{P}^{3}$.

**Proof.** Every element is a positive multiple of an element of the section, and each element of the section is a convex combination of extreme points.

**Corollary.** The section is a spectrahedron, cut out by infinitely many linear inequalities, namely one per unit vector.

**Proof.** Positive semidefiniteness is $\langle Av,v\rangle\ge0$ for every $v$, and $v$ and $-v$ give the same inequality, so one per point of $\mathbb{P}^{3}$.

## The Biquaternion Comparison

**Proposition.** The cone uses the Hermitian involution: the form $A\mapsto\operatorname{tr}(A^{\ast}A)$ is positive definite, whereas the plain form $A\mapsto\operatorname{tr}(A^{\mathsf T}A)$ is indefinite and equal to $4(Q_t^{2}+B^{2})$, a complex number.

**Proof.** $\operatorname{tr}(A^{\ast}A)$ is the sum of the squared moduli of the entries; and $\operatorname{tr}(A^{\mathsf T}A)$ is the biquaternion norm, whose value on the element with coordinates $Q_t$ and vector part of length $B$ is $4(Q_t^{2}+B^{2})$.

**Corollary.** Over $\mathbb{C}$ the plain form has no cone, since it takes both signs and complex values; a cone requires a real form of the algebra and a definite quadratic form on it.

**Proof.** $Q_t^{2}+B^{2}$ vanishes on the light cone $B=\pm iQ_t$ and changes sign across it.

**Corollary.** The Hermitian involution is the one compatible with the real structure of the matrix space, which is the reason the cone is defined with it and not with the transpose.

**Proof.** The positive definiteness of the Hilbert–Schmidt form and the indefiniteness of the trace form.

**The real symmetric cone.** The fixed part of the conjugation inside the cone is the cone of positive semidefinite real symmetric matrices, of real dimension $10$, cut out inside $\operatorname{Herm}_4$ by the reality of the entries.

**Proof.** The real symmetric matrices are the Hermitian matrices with real entries.

**Corollary.** The Hermitian cone is not the complexification of the real symmetric cone, since complexification would destroy the positivity.

**Proof.** A complexification contains $iA$ for $A$ in the cone, and $iA$ is not in the cone.

## Summary

The positive semidefinite cone is the image of $B\mapsto B^{\ast}B$, closed, convex, pointed, of full dimension sixteen, and self-dual for the Hilbert–Schmidt form. Its faces correspond to the subspaces, hence to the Hermitian idempotents and the Grassmannians, with the extremal rays parametrised by $\mathbb{P}^{3}$; its boundary stratifies by rank with dimensions $15$, $12$, $7$ and $0$.

The trace sections are compact convex spectrahedra with the rank-one elements as extreme points, and the cone is the cone over the section.

The cone exists because the Hilbert–Schmidt form is positive definite; the plain form is the indefinite biquaternion norm $4(Q_t^{2}+B^{2})$, which has no cone over $\mathbb{C}$. The real symmetric cone of dimension ten is the fixed part of the conjugation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Herm}_4^{+}=\{B^{\ast}B\}$ | the cone |
| $F_W=\{A\ge0:AW=0\}$ | a face |
| $r(8-r)$ | the dimension of the rank-$r$ stratum |
| $\{\operatorname{tr}A=1\}$ | the compact section |
| $4(Q_t^{2}+B^{2})$ | the indefinite plain form |
| real dimension $10$ | the real symmetric cone |

## Further Reading

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization* (Cambridge, 2004), for spectrahedra and semidefinite cones.
- [The Positive Cone and Its Boundary at $n=4$](the-positive-cone-and-its-boundary-at-n-4.html), for the open cone, the boundary and the automorphisms.
- [The Space of Idempotents and the Flag Varieties at $n=4$](the-space-of-idempotents-and-the-flag-varieties-at-n-4.html), for the Grassmannians attached to the faces.
- [The Four Forms and Their Algebraic Norms at $n=4$](the-four-forms-and-their-algebraic-norms-at-n-4.html), for the indefinite forms that have no cone.
- [The Cone of Positive Semidefinite $2\times2$ Matrices](the-cone-of-positive-semidefinite-2x2-matrices.html), for the case at order two.
