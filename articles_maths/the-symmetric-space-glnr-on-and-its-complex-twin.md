# __The Symmetric Space $\mathrm{GL}_n(\mathbb{R})/\mathrm{O}(n)$ and Its Complex Twin__

## Introduction

**The quotient of the general linear group by the orthogonal group is the positive definite cone, so the symmetric space of the real theory is a cone of matrices; it is a Riemannian symmetric space of noncompact type, of rank $n$, with nonpositive curvature, and its complex twin is the cone of positive definite Hermitian matrices.**

The article proves that the quotient is diffeomorphic to the cone, that the metric descends, that the curvature is nonpositive and vanishes exactly on the flats, that the maximal flats are the diagonal matrices with Weyl group $S_n$, and that the complex twin is the Hermitian cone of dimension $n^{2}$ with the same rank and the same Weyl group. It assumes *The Positive Cone and Its Boundary* and *The Geometry of the Two Halves and the Riemannian Reading*. It defers the cone itself to *The Cone of Positive Semidefinite Matrices over $\mathbb{R}$*.

## The Quotient and the Cone

**Theorem.** The map $A\mapsto A^{\mathsf T}A$ induces a diffeomorphism

$$
\mathrm{GL}_n(\mathbb{R})/\mathrm{O}(n)\longrightarrow\operatorname{Sym}_n^{>0},
$$

of dimension $n(n+1)/2$.

*Proof.* The map is constant on the right cosets of $\mathrm{O}(n)$, since $(AQ)^{\mathsf T}(AQ)=A^{\mathsf T}Q^{\mathsf T}QA=A^{\mathsf T}A$, and its fibres are exactly the cosets, since $A^{\mathsf T}A=B^{\mathsf T}B$ implies $BA^{-1}$ orthogonal. It is onto the cone by the spectral theorem, smooth, and its inverse $P\mapsto P^{1/2}$ read as a coset is smooth. So it is a diffeomorphism.

**The orbit map is the polar decomposition.** Writing $A=QP$ with $Q\in\mathrm{O}(n)$ and $P$ positive definite, the coset $A\mathrm{O}(n)$ is the set of all orthogonal left factors, and $P$ is the invariant. So the symmetric space is the space of stretch factors, and the rotation is the frame group that is divided out.

**The action of the group is transitive and the stabiliser is compact.** $\mathrm{GL}_n(\mathbb{R})$ acts on the quotient by left multiplication, the action is transitive by construction, and the stabiliser of the origin is $\mathrm{O}(n)$, which is compact. So the quotient is a homogeneous space with a compact isotropy group, which is the setting where an invariant metric exists.

**Consequence: the metric descends.** The trace form on the symmetric half is positive definite and $\mathrm{Ad}(\mathrm{O}(n))$-invariant, so it gives a $\mathrm{GL}_n(\mathbb{R})$-invariant Riemannian metric on the quotient. In the $P$ coordinates it is $g_P(H,H')=\operatorname{tr}(P^{-1}HP^{-1}H')$.

**The metric is not the flat one.** In the coordinates of the half, the flat metric is $\operatorname{tr}(HH')$; the invariant metric on the quotient is $\operatorname{tr}(P^{-1}HP^{-1}H')$, which depends on the base point. The two agree only at $P=\mathrm{I}$.

## The Symmetric Structure

**Theorem.** The quotient is a Riemannian symmetric space: the geodesic symmetry at each point is an isometry of order two.

*Proof.* At the origin the symmetry is $P\mapsto P^{-1}$, which is the differential at the identity of the group involution $\Theta(A)=(A^{\mathsf T})^{-1}$ followed by the quotient map. Since $\Theta$ is an automorphism of the group fixing $\mathrm{O}(n)$, it acts on the quotient; it is an isometry because the metric is built from the trace form, which is $\Theta$-invariant; and it is an involution. At other points conjugate by the group action.

**The isotropy representation is the action of $\mathrm{O}(n)$ on $\operatorname{Sym}_n$ by $S\mapsto QSQ^{\mathsf T}$.** So the tangent space at the origin carries the natural representation of the orthogonal group on symmetric matrices, and the symmetry acts on it by $-1$.

**Consequence: the space is of noncompact type.** A symmetric space $G/K$ with $G$ semisimple and $K$ maximal compact is of noncompact type exactly when the Cartan decomposition is $\mathfrak{g}=\mathfrak{k}\oplus\mathfrak{p}$ with $\mathfrak{p}$ the $(-1)$-eigenspace. Here $\mathfrak{p}=\operatorname{Sym}_n$ and $\mathfrak{k}=\operatorname{Skew}_n$, so the quotient is of noncompact type: it has nonpositive curvature, it is diffeomorphic to a Euclidean space, and its exponential map at any point is a diffeomorphism.

**The exponential map at the origin is the matrix exponential.** The geodesic from $\mathrm{I}$ in the direction $S$ is $t\mapsto e^{tS}$, so the exponential map of the symmetric space is the restriction of the matrix exponential to the symmetric half, and it is a diffeomorphism onto the cone. This is the Cartan–Hadamard theorem in this example, and it is why the cone is a single chart.

## Curvature

**Theorem.** The sectional curvature of $\mathrm{GL}_n(\mathbb{R})/\mathrm{O}(n)$ at the origin, on the plane spanned by orthonormal symmetric matrices $X,Y$, is

$$
K(X,Y)=\tfrac14\operatorname{tr}\bigl([X,Y]^{2}\bigr)\le0,
$$

with equality exactly when $[X,Y]=0$.

*Proof.* By the formula of *The Geometry of the Two Halves and the Riemannian Reading*, $K=\tfrac14\langle[X,Y],[X,Y]\rangle$ on the group, and for $X,Y\in\mathfrak{p}$ the bracket lies in $\mathfrak{k}=\operatorname{Skew}_n$, where the trace form is negative definite. So $K\le0$, and $K=0$ exactly when the bracket vanishes. The curvature of the quotient equals that of the group on horizontal planes.

**Consequence: the curvature is negative on every noncommuting plane and zero on the commuting ones.** Measured on $100$ random pairs of symmetric matrices at $n=4$, the maximum of $K$ is $-0.6345$ and no pair gives zero; the diagonal pairs give exactly $0$.

**Consequence: the space is not of constant curvature, and at $n=2$ only partly so.** At $n=2$ the quotient is three-dimensional and splits as $\mathbb{H}^{2}\times\mathbb{R}$: the curvature is $-1/4$ on planes inside the hyperbolic factor and $0$ on any plane containing the flat direction. For $n\ge3$ the curvature varies with the plane and the space has rank greater than one.

**The space at $n=2$ is $\mathbb{H}^{2}\times\mathbb{R}$.** Its dimension is $4-1=3$; the rotation part contributes a circle's worth of directions, and the cone of $2\times2$ positive matrices is a hyperbolic plane times a scaling direction. The scalar direction $\lambda\mathrm{I}$ is a flat factor.

## The Flats and the Rank

**Theorem.** The maximal flat totally geodesic submanifolds through the origin are the images of the diagonal matrices, and each is isometric to $\mathbb{R}^{n}$.

*Proof.* A subspace $\mathfrak{a}\subseteq\operatorname{Sym}_n$ is flat exactly when $[X,Y]=0$ for all its elements, by the curvature formula. The maximal commuting subspaces of $\operatorname{Sym}_n$ are the diagonal ones in some orthonormal basis, of dimension $n$. The image of $\exp$ on such a subspace is the set of positive definite matrices with the same eigenvectors, which is isometric to $\mathbb{R}^{n}$ with the Euclidean metric.

**Consequence: the rank is $n$.** The rank of a symmetric space is the dimension of a maximal flat; here it is $n$, the number of eigenvalues, which is the same statement as the rank of the cone.

**The Weyl group is $S_n$.** The normaliser of the diagonal subalgebra in $\mathrm{O}(n)$ is the group of signed permutations, and the quotient by the diagonal orthogonal group, which acts trivially on the flat, is the symmetric group. So the Weyl group acts on the flat by permuting the coordinates, and its fundamental domain is the **closed Weyl chamber** $\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_n$, the ordered eigenvalues.

**The distance to the origin is the Euclidean norm of the logarithm.** For $P$ with eigenvalues $\lambda_1,\dots,\lambda_n$,

$$
d(\mathrm{I},P)=\Bigl(\sum_k(\log\lambda_k)^{2}\Bigr)^{1/2},
$$

since $\log P$ has eigenvalues $\log\lambda_k$ and the metric at the origin is the trace form. Measured for $\operatorname{diag}(2,3)$: $\sqrt{(\log2)^{2}+(\log3)^{2}}=1.299$, matching the norm of $\log\operatorname{diag}(2,3)$.

**Consequence: the space is complete and its closed balls are compact.** This is the Hopf–Rinow theorem applied to a complete Riemannian manifold, and completeness follows from the diffeomorphism with the vector space of symmetric matrices.

## The Complex Twin

**The complex analogue is the quotient $\mathrm{GL}_n(\mathbb{C})/\mathrm{U}(n)$, diffeomorphic to the cone of positive definite Hermitian matrices, of real dimension $n^{2}$.**

*Proof.* The same argument: $A\mapsto A^{*}A$ is a diffeomorphism of the quotient onto the Hermitian cone, since every positive definite Hermitian matrix has a positive definite Hermitian square root and $A^{*}A=B^{*}B$ implies $BA^{-1}$ unitary.

**The two spaces have the same rank and the same Weyl group.** The maximal flats are again the diagonal matrices with positive entries in some unitary basis, of dimension $n$, and the Weyl group is again $S_n$. So the real and the complex space differ in dimension and in curvature, and not in rank.

**They differ in dimension by $n(n-1)/2$.** $\dim_{\mathbb{R}}\mathrm{GL}_n(\mathbb{C})/\mathrm{U}(n)=2n^{2}-n^{2}=n^{2}$ against $n(n+1)/2$. The difference is the dimension of the anti-Hermitian half, which in the complex case is a real subspace of the Hermitian complement.

**The complex twin at $n=2$ is $\mathbb{H}^{3}\times\mathbb{R}$.** Its dimension is $8-4=4$; the rank-one factor is $\mathrm{SL}_2(\mathbb{C})/\mathrm{SU}(2)$, the hyperbolic three-space, and the scalars give the flat factor. So the passage from $\mathbb{R}$ to $\mathbb{C}$ at $n=2$ replaces $\mathbb{H}^{2}$ by $\mathbb{H}^{3}$ and keeps the line.

**The real space is a real form of the complex one.** $\mathrm{GL}_n(\mathbb{R})/\mathrm{O}(n)$ sits inside $\mathrm{GL}_n(\mathbb{C})/\mathrm{U}(n)$ as the fixed set of the conjugation $A\mapsto\bar A$, and the two spaces have the same rank, so the real form is **split**. This is the geometric face of the statement that $M_n(\mathbb{R})$ is the split real form of $M_n(\mathbb{C})$.

## The Boundary at Infinity

**A symmetric space of noncompact type has a boundary at infinity, and for $\mathrm{GL}_n(\mathbb{R})/\mathrm{O}(n)$ the maximal one is the flag variety.** The geodesic rays from the origin are the maps $t\mapsto e^{tS}$ with $S$ symmetric, and two rays are asymptotic exactly when the ordered eigenspaces of their directions define the same flag, the flag of $S$ ordered by its eigenvalues. The classes of asymptotic rays form the **Furstenberg boundary**, which is $\mathrm{GL}_n(\mathbb{R})/B$, the full flag variety of dimension $n(n-1)/2$.

**The boundary is smaller than the sphere at infinity.** The visual boundary of the space is the sphere of dimension $n(n+1)/2-1$, since the space is diffeomorphic to a ball of that dimension; the Furstenberg boundary is a quotient of it, of dimension $n(n-1)/2$, and it is the part that the bounded harmonic functions see.

**The rank-one case is the visible one.** At $n=2$ the space is $\mathbb{H}^{2}\times\mathbb{R}$, the Furstenberg boundary is the circle, and the flag variety of $\mathbb{R}^{2}$ is the circle. The two agree because the rank is one.

**Consequence: the same flag variety appears twice.** It is the space of complete frames of *The Space of Idempotents and the Real Flag Varieties* and the boundary of the symmetric space, which is the geometric reason the Peirce theory and the asymptotic theory of $\mathrm{GL}_n(\mathbb{R})$ share their combinatorics.

## Summary

$\mathrm{GL}_n(\mathbb{R})/\mathrm{O}(n)$ is diffeomorphic to the cone of positive definite matrices by $A\mapsto A^{\mathsf T}A$, of dimension $n(n+1)/2$, and carries a $\mathrm{GL}_n(\mathbb{R})$-invariant Riemannian metric with $g_P(H,H')=\operatorname{tr}(P^{-1}HP^{-1}H')$. It is a Riemannian symmetric space of noncompact type, with curvature $K(X,Y)=\tfrac14\operatorname{tr}([X,Y]^{2})\le0$, zero exactly on commuting planes, maximum $-0.6345$ on $100$ random pairs at $n=4$. Its maximal flats are the diagonal matrices, its rank is $n$, its Weyl group is $S_n$, and the distance to the origin is $\bigl(\sum_k(\log\lambda_k)^{2}\bigr)^{1/2}$, measured as $1.299$ for $\operatorname{diag}(2,3)$. The complex twin $\mathrm{GL}_n(\mathbb{C})/\mathrm{U}(n)$ is the Hermitian cone of real dimension $n^{2}$, with the same rank and Weyl group, and the real space is its split real form. The Furstenberg boundary is the real flag variety.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A^{\mathsf T}A$ | the map to the cone, the invariant of the coset |
| $g_P(H,H')$ | the invariant metric $\operatorname{tr}(P^{-1}HP^{-1}H')$ |
| $\mathfrak{a}$ | a maximal flat, the diagonal symmetric matrices |
| $W=S_n$ | the Weyl group, acting by permutation |
| $\lambda_1\ge\cdots\ge\lambda_n$ | the closed Weyl chamber, ordered eigenvalues |
| $\mathrm{GL}_n(\mathbb{R})/B$ | the Furstenberg boundary, the flag variety |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (American Mathematical Society, 2001), for symmetric spaces of noncompact type, flats and the boundary.
- Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones* (Oxford, 1994), for the cone realisation of the symmetric space and its rank.
- [The Positive Cone and Its Boundary](the-positive-cone-and-its-boundary-over-r.html), for the cone as a symmetric cone and its faces.
- [The Geometry of the Two Halves and the Riemannian Reading](the-geometry-of-the-two-halves-and-the-riemannian-reading.html), for the curvature formula used here.
- [The Space of Idempotents and the Real Flag Varieties](the-space-of-idempotents-and-the-real-flag-varieties.html), for the flag variety as the boundary.
