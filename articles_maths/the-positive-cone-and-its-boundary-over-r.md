# __The Positive Cone and Its Boundary__

## Introduction

**The positive definite symmetric matrices form an open convex cone, and that cone is the whole of the noncompact geometry of the general linear group: it is a single orbit under congruence, it is self-dual for the trace form, and its boundary is stratified by the rank.**

The article proves openness, convexity and the congruence transitivity of the cone, identifies its closure with the positive semidefinite matrices, proves self-duality, describes the face lattice as the lattice of subspaces, identifies the extreme rays with the Veronese variety, computes the dimension $r(n-r)+r(r+1)/2$ of the stratum of rank $r$, and proves that the cone is a symmetric cone of rank $n$ with the Jordan algebra $\operatorname{Sym}_n$. It assumes *The Spectral Theorem: the Symmetric Case* and *The Exponential of the Symmetric Part: Stretches and the Positive Cone*. It defers the global geometry to *The Symmetric Space $\mathrm{GL}_n(\mathbb{R})/\mathrm{O}(n)$ and Its Complex Twin*.

## The Open Cone

**Definition.**

$$
\operatorname{Sym}_n^{>0}=\{X\in\operatorname{Sym}_n:v^{\mathsf T}Xv>0\ \text{for every}\ v\ne0\}.
$$

**Theorem.** $\operatorname{Sym}_n^{>0}$ is open in $\operatorname{Sym}_n$, convex, and invariant under congruence $X\mapsto A^{\mathsf T}XA$ for every invertible $A$.

*Proof.* Openness: the smallest eigenvalue is a continuous function of the entries, by the min-max characterisation, and the set is $\{\lambda_{\min}>0\}$. Convexity: if $X,Y$ are positive definite and $t\in[0,1]$ then $v^{\mathsf T}(tX+(1-t)Y)v=t\,v^{\mathsf T}Xv+(1-t)v^{\mathsf T}Yv>0$ for $v\ne0$ as a convex combination of two positive numbers. Invariance: $v^{\mathsf T}A^{\mathsf T}XAv=(Av)^{\mathsf T}X(Av)>0$ for $v\ne0$, since $Av\ne0$.

**Theorem.** $\mathrm{GL}_n(\mathbb{R})$ acts transitively on $\operatorname{Sym}_n^{>0}$ by congruence, and the stabiliser of $\mathrm{I}$ is $\mathrm{O}(n)$.

*Proof.* The spectral theorem writes $X=Q\Lambda Q^{\mathsf T}$ with $Q$ orthogonal and $\Lambda$ diagonal positive; then $X=(Q\Lambda^{1/2})^{\mathsf T}(Q\Lambda^{1/2})$, so $X=A^{\mathsf T}\mathrm{I}A$ with $A=\Lambda^{1/2}Q^{\mathsf T}$ invertible. The stabiliser: $A^{\mathsf T}A=\mathrm{I}$ is the definition of orthogonality.

**Consequence: the cone is a homogeneous space.** $\operatorname{Sym}_n^{>0}\cong\mathrm{GL}_n(\mathbb{R})/\mathrm{O}(n)$, of dimension $n(n+1)/2$. The identification $A\mapsto A^{\mathsf T}A$ is a diffeomorphism, and it is the polar decomposition read as a quotient map.

**The cone is the exponential image of the whole half.** $\exp:\operatorname{Sym}_n\to\operatorname{Sym}_n^{>0}$ is a bijection with inverse $\log$, so the cone is also a vector space in the logarithm coordinates. The two readings, congruence and exponential, are the two structures the cone carries.

## The Closure and the Boundary

**The closure is the cone of positive semidefinite matrices.**

$$
\overline{\operatorname{Sym}_n^{>0}}=\{X\in\operatorname{Sym}_n:v^{\mathsf T}Xv\ge0\ \text{for every}\ v\}=\{X\in\operatorname{Sym}_n:\lambda_{\min}\ge0\}.
$$

The equality of the three descriptions is the spectral theorem plus the continuity of the smallest eigenvalue.

**The boundary is the set of positive semidefinite matrices with a nonzero kernel.** It is the union of the strata of rank $r<n$, and its dimension is one less than the dimension of the cone.

**The strata are manifolds.** Let $\Sigma_r$ be the symmetric matrices of rank exactly $r$. Then $\Sigma_r$ is a smooth manifold of dimension

$$
\dim\Sigma_r=r(n-r)+\frac{r(r+1)}{2},
$$

obtained by writing $X=USU^{\mathsf T}$ with $U$ an orthonormal $n\times r$ frame and $S$ an invertible symmetric $r\times r$ matrix: the frame contributes $r(n-r)$ after quotienting by $\mathrm{O}(r)$ and the matrix contributes $r(r+1)/2$. The dimension is verified as the rank of the tangent map at $\operatorname{diag}(\mathrm{I}_r,0)$, giving $2,3,3,5,6,4,7,9,10$ at $(n,r)=(2,1),(2,2),(3,1),(3,2),(3,3),(4,1),(4,2),(4,3),(4,4)$, matching the formula.

**The top stratum is the open cone and the bottom stratum is the origin.** At $r=n$ the formula gives $n(n+1)/2$, the dimension of the whole space; at $r=0$ it gives $0$. The dimension increases with $r$, so the boundary has codimension at least one everywhere.

**The positive semidefinite cone with rank bound is the closure of the stratum.** $\overline{\Sigma_{\le r}}=\{X\ge0:\operatorname{rk}X\le r\}$, and the interior of that set inside $\operatorname{Sym}_n$ is empty for $r<n$; its relative interior is $\Sigma_r$.

## The Faces

**Theorem.** The faces of the closed cone $\overline{\operatorname{Sym}_n^{>0}}$ are exactly the sets

$$
F_U=\{X\ge0:\operatorname{im}X\subseteq U\},
$$

one for each subspace $U\subseteq\mathbb{R}^{n}$, and $\dim F_U=(\dim U)(\dim U+1)/2$.

*Proof.* A face is a convex subset $F$ with the property that $X+Y\in F$ and $X,Y\ge0$ imply $X,Y\in F$. If $X\in F$ and $\operatorname{im}X\subseteq U$ then every summand of $X$ in a decomposition into positive semidefinite parts also has image in $U$, since the images add. So $F_U$ is a face. Conversely, if $F$ is a face and $X\in F$ is in its relative interior, then every $Y\ge0$ with $\operatorname{im}Y\subseteq\operatorname{im}X$ lies in $F$, by a rank-one perturbation argument; hence $F=F_U$ with $U=\operatorname{im}X$.

**The face lattice is the lattice of subspaces.** $F_U\subseteq F_W$ exactly when $U\subseteq W$, and $F_{U\cap W}=F_U\cap F_W$, $F_{U+W}=F_U+F_W$. So the face lattice of the cone is isomorphic to the lattice of subspaces of $\mathbb{R}^{n}$, with the cone itself for $U=\mathbb{R}^{n}$ and the origin for $U=0$.

**The faces come in continua.** A face of dimension $d(d+1)/2$ corresponds to a $d$-dimensional subspace, so the faces of a given dimension are parametrised by the Grassmannian, which is a manifold of positive dimension for $0<d<n$. At $n=3$ there is the origin, a circle's worth of one-dimensional faces indexed by the lines, a circle's worth of three-dimensional faces indexed by the planes, and the cone itself.

**The extreme rays are the rank-one matrices $vv^{\mathsf T}$.** A ray is a one-dimensional face, and the one-dimensional faces correspond to the lines $U$, that is to $v$ up to sign; the positive semidefinite matrix with image in the line and trace one is $vv^{\mathsf T}/\|v\|^{2}$. So the extreme rays are parametrised by the projective space $\mathbb{RP}^{n-1}$, and the set of them is the **Veronese variety**, the image of $\mathbb{RP}^{n-1}$ under $[v]\mapsto[vv^{\mathsf T}]$.

**Consequence: the cone is the convex hull of the Veronese variety.** Every positive semidefinite matrix is a sum of rank-one ones, $X=\sum_k\lambda_ku_ku_k^{\mathsf T}$, and the sum is a convex combination after normalising. So the cone is the convex hull of its extreme rays, as it must be for a closed convex cone with a compact base.

## Self-Duality

**Theorem.** The cone is self-dual for the trace form:

$$
X\in\overline{\operatorname{Sym}_n^{>0}}\iff\operatorname{tr}(XY)\ge0\ \text{for every}\ Y\in\overline{\operatorname{Sym}_n^{>0}}.
$$

*Proof.* If $X\ge0$ and $Y\ge0$ then $X=A^{\mathsf T}A$ and $Y=B^{\mathsf T}B$, so $\operatorname{tr}(XY)=\operatorname{tr}(A^{\mathsf T}AB^{\mathsf T}B)=\operatorname{tr}\bigl((AB^{\mathsf T})(AB^{\mathsf T})^{\mathsf T}\bigr)=\|AB^{\mathsf T}\|_{2}^{2}\ge0$. Conversely, if $X$ has a negative eigenvalue with eigenvector $v$, take $Y=vv^{\mathsf T}\ge0$; then $\operatorname{tr}(XY)=v^{\mathsf T}Xv<0$, so $X$ is not in the dual cone.

**The proof uses only the factorisation $X=A^{\mathsf T}A$, which is the spectral theorem.** The self-duality is therefore a consequence of positivity of the Hilbert–Schmidt norm, and it is the reason the cone is the natural domain of semidefinite programming.

**The dual of the open cone is the closed cone, and the dual of a face is a face.** The duality exchanges $F_U$ with $F_{U^{\perp}}$: a positive semidefinite $Y$ pairs nonnegatively with every element of $F_U$ exactly when its image lies in $U^{\perp}$.

**Self-duality is a real phenomenon.** Over $\mathbb{C}$ the analogue is the cone of positive definite Hermitian matrices, self-dual for the Hermitian form $\operatorname{tr}(X^{*}Y)$; the statement survives, and what changes is the dimension, from $n(n+1)/2$ to $n^{2}$.

## The Symmetric Cone and the Jordan Algebra

**Definition.** A cone is **symmetric** when it is open, convex, self-dual, and homogeneous under its linear automorphism group.

**Theorem.** $\operatorname{Sym}_n^{>0}$ is a symmetric cone, of rank $n$ and dimension $n(n+1)/2$.

*Proof.* Open, convex and self-dual are proved above; homogeneous under $\mathrm{GL}_n(\mathbb{R})$ modulo the scalars, which act trivially on the cone. The **rank** of a symmetric cone is the length of a maximal chain of faces, minus one: the chain runs from the origin through the faces of dimensions $1,3,\dots,n(n+1)/2$, so it has $n+1$ elements and the rank is $n$.

**The cone is the cone of squares of the Jordan algebra $\operatorname{Sym}_n$.** In the Jordan product $X\circ Y=\tfrac12(XY+YX)$ one has $X\circ X=X^{2}$, so the cone is $\{X^{2}:X\in\operatorname{Sym}_n\}$, and the interior is the set of squares of invertible elements. This is the definition of the symmetric cone of a formally real Jordan algebra.

**The determinant is the characteristic function of the cone.** $\det$ is a polynomial that is positive exactly on the cone, homogeneous of degree $n$, and it satisfies $\det(A^{\mathsf T}XA)=\det(A)^{2}\det X$, which is the transformation law of the characteristic function. Its logarithm is strictly concave on the cone, and that concavity is the analytic expression of the self-duality.

**The automorphism group of the cone is $\mathrm{GL}_n(\mathbb{R})/\{\pm\mathrm{I}\}$.** A linear map preserving the cone preserves the cone of squares, hence the Jordan algebra structure, hence is a congruence by an invertible matrix, by the fundamental theorem of the geometry of symmetric cones. So the cone determines the algebra up to isomorphism.

## Summary

The positive definite symmetric matrices form an open convex cone of dimension $n(n+1)/2$, a single orbit under congruence by $\mathrm{GL}_n(\mathbb{R})$ with stabiliser $\mathrm{O}(n)$, and the exponential image of $\operatorname{Sym}_n$. Its closure is the positive semidefinite cone, self-dual for the trace form, with faces the sets $F_U$ indexed by the subspaces of $\mathbb{R}^{n}$ and extreme rays the Veronese variety of rank-one matrices $vv^{\mathsf T}$. The stratum of rank $r$ is a manifold of dimension $r(n-r)+r(r+1)/2$, measured as $2,3$ at $n=2$ and $3,5,6$ at $n=3$. The cone is symmetric of rank $n$, it is the cone of squares of the Jordan algebra $\operatorname{Sym}_n$, and its characteristic function is the determinant.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Sym}_n^{>0}$ | the open cone of positive definite matrices |
| $\Sigma_r$ | the symmetric matrices of rank exactly $r$ |
| $F_U$ | the face of matrices with image in $U$ |
| $vv^{\mathsf T}$ | an extreme ray, a rank-one positive semidefinite matrix |
| $\det$ | the characteristic function of the cone, homogeneous of degree $n$ |
| $\operatorname{rank}$ of the cone | $n$, the length of a maximal chain of faces |

## Further Reading

- Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones* (Oxford, 1994), for symmetric cones, their faces and their Jordan algebras.
- Stephen Boyd and Lieven Vandenberghe, *Convex Optimization* (Cambridge, 2004), for the positive semidefinite cone, self-duality and the rank strata.
- [The Spectral Theorem: the Symmetric Case](the-spectral-theorem-the-symmetric-case.html), for the factorisation $X=A^{\mathsf T}A$ used throughout.
- [The Exponential of the Symmetric Part: Stretches and the Positive Cone](the-exponential-of-the-symmetric-part-stretches-and-the-positive-cone.html), for the exponential parametrisation.
- [The Cone of Positive Semidefinite Matrices over $\mathbb{R}$](the-cone-of-positive-semidefinite-matrices-over-r.html), for the cone as an object of the geometry section.
