# __The Cone of Positive Semidefinite Matrices over $\mathbb{R}$__

## Introduction

**The positive semidefinite matrices form a closed convex cone in $\operatorname{Sym}_n$ that is pointed, full-dimensional, self-dual and not polyhedral; it defines a partial order on the symmetric matrices, it is the set of sums of squares, and its base is a round body whose boundary is the set of singular matrices.**

The article proves the conic and order-theoretic properties, identifies the dual cone with the cone, gives the three equivalent descriptions by quadratic forms, by principal minors, and by sums of squares, computes the base and its extreme rays at $n=2$ and $n=3$, proves that the cone is not polyhedral and has infinitely many extreme rays, and locates it among the spectrahedra. It assumes *The Positive Cone and Its Boundary* and *The Spectral Theorem: the Symmetric Case*. It defers the global picture to *Coda: $M_n(\mathbb{R})$, the Split Form, and the Passage to $M_n(\mathbb{C})$*.

## Three Descriptions

**The cone is defined by quadratic forms.**

$$
\mathcal{P}_n=\{X\in\operatorname{Sym}_n:v^{\mathsf T}Xv\ge0\ \text{for every}\ v\in\mathbb{R}^{n}\}.
$$

**The cone is defined by principal minors.** $X\succeq0$ if and only if every principal minor of $X$ is nonnegative. For $n=2$ this is the pair of conditions $X_{11}\ge0$ and $\det X\ge0$; for larger $n$ the conditions are $2^{n}-1$ in number, one for each nonempty subset of the index set.

**The cone is the set of sums of squares.** $X\succeq0$ if and only if $X=A^{\mathsf T}A$ for some $A$, and then $X=\sum_ka_ka_k^{\mathsf T}$ is a sum of squares of rank-one matrices. The factor $A$ can always be taken $n\times n$, and of rank $r$ exactly when $X$ has rank $r$.

**Theorem.** The three descriptions agree.

*Proof.* Quadratic forms imply principal minors: the minor on a subset $S$ is $v_S^{\mathsf T}X_Sv_S$ rearranged, so it is nonnegative. Principal minors of all orders imply the eigenvalues are nonnegative: the characteristic polynomial has all coefficients of alternating sign, which by Descartes' rule forces all roots nonnegative. Nonnegative eigenvalues give $X=A^{\mathsf T}A$ with $A$ the positive semidefinite square root. And $A^{\mathsf T}A\succeq0$ because $v^{\mathsf T}A^{\mathsf T}Av=\|Av\|^{2}\ge0$.

**Consequence: the cone is closed, convex, pointed and full-dimensional.** Closed because the conditions are non-strict; convex because the quadratic form condition is linear in $X$ for each $v$; pointed because $X\succeq0$ and $-X\succeq0$ force $v^{\mathsf T}Xv=0$ for all $v$, which for symmetric $X$ forces $X=0$; full-dimensional because it contains the open cone $\operatorname{Sym}_n^{>0}$.

## The Löwner Order

**Definition.** $X\preceq Y$ means $Y-X\in\mathcal{P}_n$.

**Theorem.** $\preceq$ is a partial order on $\operatorname{Sym}_n$, it is compatible with addition, and it is invariant under congruence.

*Proof.* Reflexivity: $X-X=0\succeq0$. Antisymmetry: $Y-X\succeq0$ and $X-Y\succeq0$ give $Y-X=0$ by pointedness. Transitivity: the sum of two positive semidefinite matrices is positive semidefinite. Addition: if $X\preceq Y$ then $X+Z\preceq Y+Z$ for every symmetric $Z$. Congruence: $A^{\mathsf T}(Y-X)A\succeq0$ when $Y-X\succeq0$.

**The order is not total from $n=2$ on.** For $X=\begin{pmatrix}1&0\\0&0\end{pmatrix}$ and $Y=\begin{pmatrix}0&0\\0&1\end{pmatrix}$ neither $Y-X=\operatorname{diag}(-1,1)$ nor $X-Y$ is positive semidefinite, since both have a negative eigenvalue. So the symmetric matrices form a partially ordered set with incomparable pairs, and the cone is not a half-space.

**The order is the order of the eigenvalues.** $X\preceq Y$ implies $\lambda_k(X)\le\lambda_k(Y)$ for every $k$, by the min-max characterisation, and the converse fails. So the order is finer than the order on the spectrum, which is the reason the cone is not polyhedral.

**Consequence: the order is compatible with positive scaling.** $X\preceq Y$ and $t\ge0$ give $tX\preceq tY$, since $t(Y-X)\succeq0$. So the cone is a proper cone in the sense of convex analysis: closed, convex, pointed and full-dimensional.

## The Base and the Extreme Rays

**Definition.** The base of the cone is $\mathcal{B}_n=\{X\in\mathcal{P}_n:\operatorname{tr}X=1\}$, a compact convex set.

**Theorem.** $\mathcal{B}_2$ is a closed disk of radius $1/2$ centred at $\operatorname{diag}(1/2,1/2)$.

*Proof.* Write $X=\begin{pmatrix}a&b\\ b&1-a\end{pmatrix}$; the trace condition fixes the diagonal. Positive semidefiniteness is $a\ge0$, $1-a\ge0$ and $a(1-a)-b^{2}\ge0$, and the last is $(a-1/2)^{2}+b^{2}\le1/4$. So the base is the disk stated.

**Consequence: the extreme points of $\mathcal{B}_2$ are a circle.** They are the rank-one matrices with trace one, that is

$$
X(\theta)=\tfrac12\begin{pmatrix}1+\cos\theta&\sin\theta\\ \sin\theta&1-\cos\theta\end{pmatrix},
$$

which has trace $1$, determinant $0$ and rank $1$ for every $\theta$, verified at $\theta=0,1,2.5$. The boundary of the base is this circle and the interior is the set of positive definite matrices.

**At $n=3$ the base is a five-dimensional body.** Its dimension is $n(n+1)/2-1=5$; its boundary contains the rank-one points, which form a copy of $\mathbb{RP}^{2}$ embedded by $[v]\mapsto vv^{\mathsf T}/\|v\|^{2}$, the Veronese surface of dimension $2$, and the intersection with the rank-two stratum, which has dimension $5-1=4$.

**Consequence: the cone has infinitely many extreme rays.** The rays through the rank-one matrices are the extreme rays, and they are parametrised by $\mathbb{RP}^{n-1}$, which is a manifold of dimension $n-1$; for $n\ge2$ that is infinite. A polyhedral cone has finitely many extreme rays, so the cone is not polyhedral.

**The cone is a spectrahedron and not a polyhedron.** It is described by infinitely many linear inequalities $v^{\mathsf T}Xv\ge0$, one for each $v$, and no finite subset suffices for $n\ge2$. So it is an intersection of infinitely many half-spaces, hence not a polyhedron, and it is the model example of a spectrahedron defined by a linear matrix inequality.

## Self-Duality and the Automorphisms

**Theorem.** $\mathcal{P}_n$ is self-dual: $\mathcal{P}_n=\{X:\operatorname{tr}(XY)\ge0\ \text{for every}\ Y\in\mathcal{P}_n\}$.

*Proof.* One inclusion is Cauchy–Schwarz for the factorisation $X=A^{\mathsf T}A$, $Y=B^{\mathsf T}B$, giving $\operatorname{tr}(XY)=\|AB^{\mathsf T}\|_{2}^{2}\ge0$. The other: if $X$ has a negative eigenvalue with eigenvector $v$ then $\operatorname{tr}(Xvv^{\mathsf T})=v^{\mathsf T}Xv<0$ while $vv^{\mathsf T}\in\mathcal{P}_n$.

**Consequence: the cone is the domain of a duality that fixes it.** The polar of the cone is the cone, so the linear programmes over the cone have dual programmes over the same cone; this is why semidefinite programming is a self-dual theory and why the duality gap is controlled by the cone itself.

**Theorem.** The linear automorphisms of $\mathcal{P}_n$ are the congruences $X\mapsto A^{\mathsf T}XA$ with $A$ invertible, and the group is $\mathrm{GL}_n(\mathbb{R})/\{\pm\mathrm{I}\}$.

*Proof.* A congruence preserves the cone by the invariance of positive semidefiniteness. Conversely an automorphism preserves the extreme rays, hence induces a projective transformation of $\mathbb{RP}^{n-1}$ preserving the Veronese surface, and such a transformation is induced by an invertible linear map; the kernel of the map to the projective group is $\{\pm\mathrm{I}\}$.

**The dimension of the automorphism group is $n^{2}$ and the action is transitive on the interior.** The stabiliser of $\mathrm{I}$ is $\mathrm{O}(n)$, so the interior is the quotient of dimension $n^{2}-n(n-1)/2=n(n+1)/2$; the action on the boundary is transitive on each rank stratum.

## The Boundary as the Singular Set

**The boundary of the cone is the set of singular positive semidefinite matrices.** It is $\{X\succeq0:\det X=0\}$, the intersection of the cone with the singular hypersurface, and it is the union of the strata $\Sigma_r$ for $r<n$.

**The strata are smooth and their dimensions add up to the dimension of the boundary.** $\dim\Sigma_r=r(n-r)+r(r+1)/2$, measured as $2,3$ at $n=2$ and $3,5,6$ at $n=3$; the largest proper stratum is $\Sigma_{n-1}$, of dimension $n(n+1)/2-1$, which is the smooth part of the boundary.

**The boundary is smooth exactly on the top stratum.** A point of rank $r$ has a neighbourhood in the boundary modelled on $\Sigma_r$ times the cone over $\mathcal{P}_{n-r}$, so the boundary is a smooth hypersurface only where $r=n-1$; at lower rank it has a conical singularity whose link is a positive semidefinite cone of the complementary size.

**Consequence: the boundary is a stratified space with the face lattice of the subspaces.** Each stratum retracts to the flag-like data of its image and kernel, and the incidence of the strata is the incidence of subspaces. This is the geometric form of the Peirce decomposition.

## Inner and Outer Approximation

**The cone is the intersection of a nested family of polyhedral cones, and it is the limit of both an increasing and a decreasing family.** The outer approximations are given by finitely many vectors $v_1,\dots,v_N$: the set $\{X:v_i^{\mathsf T}Xv_i\ge0\}$ contains $\mathcal{P}_n$ and decreases to it as the $v_i$ become dense. The inner approximations are the polyhedral cones spanned by finitely many rank-one matrices, which increase to $\mathcal{P}_n$.

**Consequence: every semidefinite constraint is a limit of linear constraints.** This is the reason the cone is the natural relaxation of a combinatorial constraint: the rank-one cone is the nonconvex object, its convex hull is $\mathcal{P}_n$, and the polyhedral approximations interpolate between the two.

**The cone is the convex hull of the Veronese variety.** $\mathcal{P}_n=\operatorname{cone}\{vv^{\mathsf T}:v\in\mathbb{R}^{n}\}$, since every element is a sum of rank-one ones. So the cone is the conic hull of a real algebraic variety of dimension $n-1$, and its extreme rays are that variety.

**The slack in the hull is the rank.** The convex combination of $r$ extreme rays has rank at most $r$, so a matrix of rank $r$ is a combination of exactly $r$ extreme rays and no fewer; the cone's stratification by rank is the stratification by the number of extreme rays needed.

## Summary

The positive semidefinite matrices form a closed, convex, pointed, full-dimensional cone in $\operatorname{Sym}_n$, described equivalently by quadratic forms, by principal minors and by sums of squares $A^{\mathsf T}A$. It defines the Löwner order, which is partial, compatible with addition and congruence-invariant. Its base is compact and convex, a disk of radius $1/2$ at $n=2$ and a five-dimensional body at $n=3$, and its extreme rays are the rank-one matrices $vv^{\mathsf T}$ parametrised by $\mathbb{RP}^{n-1}$, so the cone has infinitely many of them and is not polyhedral. It is self-dual for the trace form, its automorphism group is $\mathrm{GL}_n(\mathbb{R})/\{\pm\mathrm{I}\}$, its boundary is the singular set stratified by rank, and it is the convex hull of the Veronese variety.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{P}_n$ | the cone of positive semidefinite symmetric matrices |
| $\preceq$ | the Löwner order, $X\preceq Y$ iff $Y-X\succeq0$ |
| $\mathcal{B}_n$ | the base $\{X\succeq0:\operatorname{tr}X=1\}$ |
| $\Sigma_r$ | the stratum of rank $r$, of dimension $r(n-r)+r(r+1)/2$ |
| $vv^{\mathsf T}$ | an extreme ray, a point of the Veronese variety |
| $A^{\mathsf T}A$ | the sum-of-squares factorisation of an element |

## Further Reading

- Stephen Boyd and Lieven Vandenberghe, *Convex Optimization* (Cambridge, 2004), for the cone, its base, its duality and the linear matrix inequalities.
- Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones* (Oxford, 1994), for the cone as the symmetric cone of $\operatorname{Sym}_n$.
- [The Positive Cone and Its Boundary](the-positive-cone-and-its-boundary-over-r.html), for the open cone, its faces and its self-duality.
- [The Spectral Theorem: the Symmetric Case](the-spectral-theorem-the-symmetric-case.html), for the factorisation used in every proof.
- [The Symmetric Space $\mathrm{GL}_n(\mathbb{R})/\mathrm{O}(n)$ and Its Complex Twin](the-symmetric-space-glnr-on-and-its-complex-twin.html), for the cone as a symmetric space.
