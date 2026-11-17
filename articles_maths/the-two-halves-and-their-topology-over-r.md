# __The Two Halves and Their Topology__

## Introduction

**Both halves of $M_n(\mathbb{R})$ are contractible, so the topology of the algebra is not in the halves but in their strata.** $\operatorname{Sym}_n$ and $\operatorname{Skew}_n$ are Euclidean spaces of dimensions $n(n+1)/2$ and $n(n-1)/2$, and each contracts to a point. The interesting spaces are the sets of a fixed rank, the positive definite cone, and the intersections with the group of invertibles.

The article proves the two homeomorphisms, the contractibility of the two halves and of the positive definite cone, computes the dimensions of the rank strata, describes the determinant on each half at odd and even $n$, and reads the two halves as the kernel and the image of the symmetrisation map. It assumes *The Topology of $M_n(\mathbb{R})$ and the Sign of the Determinant* for the group of invertibles and its two components.

Throughout $n\ge2$ and $M_n=M_n(\mathbb{R})$.

## The Two Halves

**Definition.** $\operatorname{Sym}_n=\{S:S^{\mathsf T}=S\}$ and $\operatorname{Skew}_n=\{K:K^{\mathsf T}=-K\}$.

**Each half is a linear subspace, and together they are the algebra.** Both sets are closed under addition and under scalar multiplication, and

$$
M_n=\operatorname{Sym}_n\oplus\operatorname{Skew}_n,\qquad A=\tfrac12(A+A^{\mathsf T})+\tfrac12(A-A^{\mathsf T}),
$$

with the two summands in the two halves. So the algebra is the direct sum of the halves, and the projection on each is the symmetrisation and the antisymmetrisation.

**Theorem.** $\operatorname{Sym}_n$ is homeomorphic to $\mathbb{R}^{n(n+1)/2}$ and $\operatorname{Skew}_n$ to $\mathbb{R}^{n(n-1)/2}$.

*Proof.* A symmetric matrix is determined by its entries on and above the diagonal, of number $n(n+1)/2$, and an antisymmetric one by its entries strictly above the diagonal, of number $n(n-1)/2$, since the diagonal of an antisymmetric matrix vanishes. Listing those entries is a linear bijection onto the corresponding Euclidean space.

## The Two Halves Are Contractible

**Corollary.** Both halves are contractible, and so is the algebra.

*Proof.* Each half is a Euclidean space by the theorem above, and $A\mapsto(1-t)A$ contracts it to $0$. The same path contracts the algebra, and it preserves each half because a linear subspace is closed under scaling.

**The linear structure carries no topology.** Every invariant of $\operatorname{Sym}_n$ or of $\operatorname{Skew}_n$ is trivial: both are simply connected and both are homeomorphic to Euclidean spaces. So any interesting topology must come from a condition on the elements, that is from a subset defined by a polynomial or by a rank.

## The Positive Definite Cone

**Definition.** $\operatorname{Sym}_n^{>0}=\{S\in\operatorname{Sym}_n:S>0\}$ is the set of positive definite matrices.

**Theorem.** $\operatorname{Sym}_n^{>0}$ is open and convex in $\operatorname{Sym}_n$, hence contractible.

*Proof.* For $S>0$ the quadratic form $x^{\mathsf T}Sx$ has a positive minimum on the unit sphere, and that minimum depends continuously on the entries, so a small perturbation of $S$ stays positive definite: the set is open. If $S>0$ and $T>0$ then $x^{\mathsf T}((1-t)S+tT)x=(1-t)x^{\mathsf T}Sx+t\,x^{\mathsf T}Tx>0$ for $x\ne0$, so the set is convex, and a convex set is contractible.

**The cone is the orbit of the identity under congruence.** Every positive definite $S$ is $P^{\mathsf T}P$ for an invertible $P$, by the Cholesky factorisation or by the spectral theorem, and conversely $P^{\mathsf T}P>0$. So $\operatorname{Sym}_n^{>0}=\{P^{\mathsf T}P:P\in\mathrm{GL}_n(\mathbb{R})\}$ is a single orbit of the congruence action, of dimension $n(n+1)/2$.

**The boundary is the degenerate cone.** The closure of $\operatorname{Sym}_n^{>0}$ is the set of positive semidefinite matrices, and its boundary is the set of those of rank below $n$, so the topology of the boundary is the topology of the lower strata.

**Measured.** A convex combination of two random positive definite matrices is positive definite to machine precision. A random symmetric matrix is positive definite with probability strictly between $0$ and $1$: measured as $0.16$ at $n=2$ and $0.02$ at $n=3$.

## The Strata of the Symmetric Half

**Theorem.** The symmetric matrices of rank exactly $r$ form a manifold of dimension

$$
r(n-r)+\frac{r(r+1)}{2}=\frac{r(2n-r+1)}{2}.
$$

*Proof.* A symmetric matrix of rank at most $r$ is a symmetric bilinear form whose radical contains a fixed $(n-r)$-plane $W^{\perp}$. It is determined by its values on $W\times W$, of number $r(r+1)/2$, and on $W\times W^{\perp}$, of number $r(n-r)$, and it vanishes on $W^{\perp}\times W^{\perp}$. Hence

$$
\frac{r(r+1)}{2}+r(n-r)=r(n-r)+\frac{r(r+1)}{2},
$$

and the matrices of rank exactly $r$ are an open dense subset of those of rank at most $r$, so the two sets have the same dimension.

**The two ends of the count.** At $r=n$ the formula gives $n(n+1)/2$, the whole half; at $r=1$ it gives $n$, the rank-one cone $\pm aa^{\mathsf T}$. At $n=3$ the values are $3,5,6$; at $n=4$ they are $4,7,9,10$.

**The strata are the orbits of the congruence action.** $\mathrm{GL}_n(\mathbb{R})$ acts on $\operatorname{Sym}_n$ by $S\mapsto P^{\mathsf T}SP$, and the orbit of a matrix of rank $r$ is the set of matrices of rank $r$ with the same inertia. The stratum of rank $r$ is a union of $r+1$ orbits, indexed by the inertia $(p,q)$ with $p+q=r$, and each orbit has the dimension of the stratum. At $n=4$ the stratum of rank $2$ has dimension $7$ and three orbits, of inertias $(2,0)$, $(1,1)$ and $(0,2)$.

## The Strata of the Antisymmetric Half

**Theorem.** An antisymmetric matrix has even rank, and the antisymmetric matrices of rank exactly $2s$ form a manifold of dimension

$$
2s(n-s)-s=s(2n-2s-1).
$$

*Proof.* The rank of an antisymmetric matrix is even. An alternating form has $x^{\mathsf T}Kx=0$ for every $x$, so every vector is isotropic; the restriction to a line is zero, the form descends to the quotient by that line with the same alternating type, and induction on the dimension gives the evenness. For the dimension, an antisymmetric matrix of rank at most $2s$ is an alternating form whose radical contains a fixed $(n-2s)$-plane: it is determined by its values on $W\times W$, of number $2s(2s-1)/2$, and on $W\times W^{\perp}$, of number $2s(n-2s)$, and it vanishes on $W^{\perp}\times W^{\perp}$. Hence

$$
\frac{2s(2s-1)}{2}+2s(n-2s)=2s(n-s)-s .
$$

**The two ends of the count.** At $s=0$ the dimension is $0$, the zero matrix. At $2s=n$, for even $n$, it is $n(n-1)/2$, the whole half. At $n=4$ the values are $0,5,6$ and at $n=5$ they are $0,7,10$. The stratum of rank $2$ at $n=4$ has codimension $1$, bounded by $\{\operatorname{pf}=0\}$.

**The rank is the only invariant of a stratum.** Two antisymmetric matrices of the same rank are congruent, since an alternating form has a normal form determined by its rank alone: $s$ hyperbolic planes and a radical. So each stratum is a single orbit, and the antisymmetric half has no inertia, which is the difference between the two halves.

## The Determinant on the Two Halves

**Theorem.** For odd $n$ the determinant vanishes identically on $\operatorname{Skew}_n$. For even $n$ it is the square of the Pfaffian, hence nonnegative.

*Proof.* $\det K=\det K^{\mathsf T}=\det(-K)=(-1)^{n}\det K$, so for odd $n$ the determinant equals its own negative. For even $n$, $\det K=\operatorname{pf}(K)^{2}$ with $\operatorname{pf}$ the Pfaffian, a polynomial of degree $n/2$.

**Measured.** With $300$ samples of unit-normal entries above the diagonal, the largest value of $|\det K|$ on $\operatorname{Skew}_n$ was $0$ at $n=3$ and $n=5$, and about $10$ at $n=2$ (measured $9.61$) and $40$ at $n=4$ (measured $42.4$ and $47.37$ on two samples). The zeros at odd $n$ are exact, and the nonzero values at even $n$ show the determinant is not identically zero there.

**The determinant on the symmetric half is the discriminant of the form.** $\det S$ vanishes exactly on the degenerate symmetric matrices, among them the boundary of the positive definite cone, and a symmetric matrix of inertia $(p,q)$ has determinant of sign $(-1)^{q}$. So the symmetric half meets both components of the group of invertibles.

**The zero sets are hypersurfaces.** On $\operatorname{Sym}_n$ the set $\{\det=0\}$ has dimension $n(n+1)/2-1$; on $\operatorname{Skew}_n$ with $n$ even the set $\{\operatorname{pf}=0\}$ has dimension $n(n-1)/2-1$; on $\operatorname{Skew}_n$ with $n$ odd it is the whole half.

## The Symmetrisation Map

**Definition.** The **symmetrisation** is $\sigma(A)=\tfrac12(A+A^{\mathsf T})$, and the **antisymmetrisation** is $\alpha(A)=\tfrac12(A-A^{\mathsf T})$.

**Theorem.** $\sigma$ is a linear surjection $M_n\to\operatorname{Sym}_n$ with kernel $\operatorname{Skew}_n$, and $\alpha$ is a linear surjection $M_n\to\operatorname{Skew}_n$ with kernel $\operatorname{Sym}_n$.

*Proof.* Both maps are linear, $\sigma(A)$ is symmetric and $\alpha(A)$ is antisymmetric, and $A=\sigma(A)+\alpha(A)$. So $\sigma$ is onto (it fixes every symmetric matrix), and its kernel is the set of $A$ with $A+A^{\mathsf T}=0$, which is $\operatorname{Skew}_n$. The statement for $\alpha$ is the same with the sign changed.

**The two halves are the coimage and the kernel.** $\operatorname{Sym}_n$ is the image of $\sigma$, that is the coimage, and $\operatorname{Skew}_n$ is its kernel, that is the fibre over $0$. The short exact sequence $0\to\operatorname{Skew}_n\to M_n\to\operatorname{Sym}_n\to0$ splits by the inclusion of $\operatorname{Sym}_n$, and the splitting is the direct sum. So the halves are the two ends of one linear map, the fibre of $0$ and the quotient.

**The same map reads the transpose involution.** $\sigma=\tfrac12(\mathrm{id}+\sigma_{\mathsf T})$ and $\alpha=\tfrac12(\mathrm{id}-\sigma_{\mathsf T})$, where $\sigma_{\mathsf T}(A)=A^{\mathsf T}$. So $\sigma$ and $\alpha$ are the spectral projections of the transpose, and the dimensions of the halves are the multiplicities of its two eigenvalues.

## Where the Topology Lives

**The symmetric half meets the group of invertibles in $n+1$ components.** By Sylvester's law of inertia the invertible symmetric matrices fall into $n+1$ classes, indexed by the inertia $(p,q)$ with $p+q=n$. Each class is a single orbit of the congruence action, and since $-P$ acts by the same congruence as $P$, each class is an orbit of the connected group $\mathrm{GL}_n^{+}$, hence connected. At $n=2$ the three are the positive definite, the negative definite and the indefinite matrices.

**The antisymmetric half meets the group of invertibles only for even $n$.** For odd $n$ every antisymmetric matrix is singular, since an odd-order alternating form is degenerate; for even $n$ the invertible ones form the stratum of rank $n$, an open subset of the half whose complement is $\{\operatorname{pf}=0\}$.

**The topology is the topology of the strata.** The symmetric half is contractible but its intersection with the group of invertibles has $n+1$ components, and the antisymmetric half is contractible but its rank strata have the dimensions of §*The Strata of the Antisymmetric Half*. So the invariants live in the stratification.

**The two halves together add nothing.** $M_n$ is the direct sum and is contractible, so no homotopy invariant distinguishes the halves. What distinguishes them is the algebra of the product: $\operatorname{Skew}_n$ is closed under the commutator and $\operatorname{Sym}_n$ is not, as in *The Matrix Algebra $M_n(\mathbb{R})$*.

## Summary

$\operatorname{Sym}_n$ and $\operatorname{Skew}_n$ are Euclidean spaces of dimensions $n(n+1)/2$ and $n(n-1)/2$, and both are contractible, so the algebra $M_n(\mathbb{R})$ carries no topology beyond that of a point. The positive definite cone is open, convex and a single congruence orbit, hence contractible, and its boundary is stratified by rank. The symmetric matrices of rank $r$ form a manifold of dimension $r(n-r)+r(r+1)/2$, and the antisymmetric matrices of rank $2s$ one of dimension $2s(n-s)-s$; the rank is even on the antisymmetric half, and that half has no inertia. The determinant vanishes on $\operatorname{Skew}_n$ for odd $n$, is the square of the Pfaffian for even $n$, and on $\operatorname{Sym}_n$ has the sign of the negative index. The two halves are the kernel and the coimage of the symmetrisation map, and the topology of each is the topology of its stratification.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Sym}_n$, $\operatorname{Skew}_n$ | the two halves, of dimensions $n(n+1)/2$ and $n(n-1)/2$ |
| $\operatorname{Sym}_n^{>0}$ | the positive definite cone, open, convex and contractible |
| $r(n-r)+r(r+1)/2$ | the dimension of the symmetric matrices of rank $r$ |
| $2s(n-s)-s$ | the dimension of the antisymmetric matrices of rank $2s$ |
| $\operatorname{pf}(K)$ | the Pfaffian, with $\det K=\operatorname{pf}(K)^{2}$ for even $n$ |
| $\sigma(A)=\tfrac12(A+A^{\mathsf T})$ | the symmetrisation, with kernel $\operatorname{Skew}_n$ |
| $\alpha(A)=\tfrac12(A-A^{\mathsf T})$ | the antisymmetrisation, with kernel $\operatorname{Sym}_n$ |
| inertia $(p,q)$ | the inertia of a symmetric matrix, an invariant of its congruence class |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the symmetric and antisymmetric matrices, the inertia and the Pfaffian.
- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the positive definite cone and the congruence action.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the two halves, their dimensions and their products.
- [The Topology of $M_n(\mathbb{R})$ and the Sign of the Determinant](the-topology-of-mnr-and-the-sign-of-the-determinant.html), for the group of invertibles and its two components.
- [The Symmetric and Antisymmetric Parts of the Operator Space](the-symmetric-and-antisymmetric-parts-of-the-operator-space-over-r.html), for the same split one level up.
