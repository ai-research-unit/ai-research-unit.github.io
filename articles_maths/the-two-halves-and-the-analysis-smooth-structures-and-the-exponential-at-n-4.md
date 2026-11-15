# __The Two Halves and the Analysis: Smooth Structures and the Exponential at $n=4$__

## Introduction

**The Hermitian half and the skew-Hermitian half are real manifolds of dimension $16$, each is the tangent space of the other at every point through the exponential, the maps $A\mapsto A^{\ast}$, $\operatorname{tr}A$ and $\det A$ are analytic with computable derivatives, the derivative of the determinant at $A$ being $B\mapsto\det(A)\operatorname{tr}(A^{-1}B)$, and the polar decomposition is a diffeomorphism $\mathrm{GL}_4\to\operatorname{Herm}_4^{++}\times U(4)$; the article separates what is genuine analysis from what is algebra written in analytic language.**

The article describes the two halves as smooth submanifolds and their tangent spaces, treats the exponential on each half and the image it reaches, computes the differentials of the elementary analytic maps, proves the polar decomposition is a diffeomorphism with a smooth inverse, reads the symmetric half through the Jordan algebra, and marks the boundary between analysis and algebra.

It assumes *The Exponential and the Lie Group Structure at $n=4$*, *The Exponential of the Symmetric Part: Stretches and the Positive Cone at $n=4$* and *The Positive Cone and Its Boundary at $n=4$*. The model at order two is *The Two Halves and the Analysis: Smooth Structures at $n=2$*.

## The Two Halves as Manifolds

**Proposition.** $\operatorname{Herm}_4$ is a real submanifold of $M_4(\mathbb{C})$ of dimension $16$, cut out by the linear equations $A=A^{\ast}$, and $\mathfrak{u}(4)$ is a real submanifold of the same dimension cut out by $A=-A^{\ast}$.

**Proof.** The two conditions are real linear, so each half is a linear subspace of the real vector space of dimension $32$.

**Corollary.** The tangent space of each half at every point is the half itself, and the two tangent spaces are complementary at every point.

**Proof.** A linear subspace is its own tangent space.

**Corollary.** The two halves are closed subsets of the matrix space, and they are the images of the projections $\tfrac12(A+A^{\ast})$ and $\tfrac12(A-A^{\ast})$, which are smooth.

**Proof.** Linearity and closedness of the conditions.

**The submanifold of the group.** $\operatorname{Herm}_4^{++}$ is an open submanifold of $\operatorname{Herm}_4$, and $U(4)$ is a closed submanifold of $\mathrm{GL}_4(\mathbb{C})$ of dimension $16$.

**Proof.** The openness of the positivity condition and the closedness of the unitary condition in the group.

## The Exponential on Each Half

**Theorem.** The exponential restricts to an analytic diffeomorphism $\operatorname{Herm}_4\to\operatorname{Herm}_4^{++}$ with analytic inverse, and to a surjective analytic map $\mathfrak{u}(4)\to U(4)$ whose fibres are discrete.

**Proof.** For Hermitian $H$ the eigenvalues are real and $e^{H}$ has positive eigenvalues; the inverse sends a positive definite $A$ to $\sum\log\lambda_k\,P_k$ in its spectral decomposition, which is analytic. For skew-Hermitian $K$ the exponential is unitary and every unitary has a skew-Hermitian logarithm; two logarithms of the same unitary differ by $2\pi i$ times an integral matrix in the eigenbasis, so the fibres are discrete.

**Corollary.** The image of the Hermitian half is exactly the open cone, so the exponential identifies the two halves as manifolds of the same dimension and the cone as a model of the linear space.

**Proof.** The two halves have dimension sixteen and the exponential is a diffeomorphism onto the cone.

**Corollary.** The image of the skew half is the compact group $U(4)$, so the same exponential is injective-up-to-discrete on one half and a covering-like surjection on the other.

**Proof.** The unitary group is compact and of dimension sixteen, equal to the dimension of the skew half.

**The derivative of the exponential.** The differential of $\exp$ at $A$ is $B\mapsto e^{A}\sum_{k\ge0}\frac{(-1)^{k}}{(k+1)!}(\operatorname{ad}_A)^{k}(B)$, which is the identity at $A=0$ and is singular whenever two eigenvalues of $A$ differ by $2\pi i n$.

**Proof.** The derivative of $t\mapsto e^{A+tB}$ at $t=0$, computed by the series and regrouped in terms of the commutator.

## The Analytic Maps and Their Derivatives

**Theorem.** The following maps are analytic with the displayed derivatives:
$$
d(A\mapsto A^{\ast})(B)=B^{\ast},\qquad d(\operatorname{tr})(B)=\operatorname{tr}B,\qquad d(\det)_{A}(B)=\det(A)\operatorname{tr}(A^{-1}B),
$$
and, on the invertible set,
$$
d(A\mapsto A^{-1})_{A}(B)=-A^{-1}BA^{-1}.
$$

**Proof.** The first is antilinear and real-linear; the second is linear; for the third, $\det(A+tB)=\det(A)\det(\mathrm I+tA^{-1}B)=\det(A)(1+t\operatorname{tr}(A^{-1}B)+O(t^{2}))$; for the fourth, differentiate $A(t)A(t)^{-1}=\mathrm I$.

**Corollary.** The determinant is a local diffeomorphism nowhere, since its derivative has a one-dimensional image; the trace has the same property.

**Proof.** Both derivatives take values in a one-dimensional space, so neither is surjective onto the sixteen-dimensional space.

**Corollary.** The derivative of $A\mapsto A^{\ast}A$ at $A$ is $B\mapsto B^{\ast}A+A^{\ast}B$, whose image is the Hermitian half, so the map is a submersion onto $\operatorname{Herm}_4$.

**Proof.** The derivative is real-linear into the Hermitian space, and for $A$ invertible it is onto, since every Hermitian $H$ is $B^{\ast}A+A^{\ast}B$ with $B=\tfrac12AH$.

**Corollary.** The map $A\mapsto A^{\ast}A$ is a submersion and its fibres are the orbits of the unitary group on the left, so the quotient is the open cone.

**Proof.** The fibres of the map are the sets $\{UA:U\in U(4)\}$, and the quotient by these fibres is the cone of positive definite matrices.

**The eigenvalues.** The map sending a matrix to its characteristic polynomial is analytic and its derivative is the sum of the principal minors with signs; the eigenvalues are analytic functions only locally, and only where they are simple.

**Proof.** The coefficients are polynomial, while the eigenvalue functions branch at multiple eigenvalues.

## The Polar Decomposition as a Diffeomorphism

**Theorem.** The map $A\mapsto(H,U)=((AA^{\ast})^{1/2},(AA^{\ast})^{-1/2}A)$ is an analytic diffeomorphism $\mathrm{GL}_4(\mathbb{C})\to\operatorname{Herm}_4^{++}\times U(4)$ with analytic inverse $(H,U)\mapsto HU$.

**Proof.** The map is a bijection by the polar decomposition; it is analytic because the square root of a positive definite matrix is analytic in the matrix; the inverse is the product, which is analytic; a bijective analytic map with analytic inverse is a diffeomorphism.

**Corollary.** The two halves together with the compact group give a global product decomposition of the group, and the dimension count $32=16+16$ is exact.

**Proof.** The product of the two manifolds has dimension $16+16$.

**Corollary.** The differential of the polar map at the identity is the direct sum of the identity on the Hermitian half and the identity on the skew half.

**Proof.** Near the identity, $H=\mathrm I+\tfrac12(A+A^{\ast})$ and $U=\mathrm I+\tfrac12(A-A^{\ast})$ to first order.

**The real analogue.** Over $\mathbb{R}$ the same construction gives $\mathrm{GL}_4(\mathbb{R})\to\operatorname{Sym}_4^{++}\times O(4)$, with dimensions $16=10+6$.

**Proof.** The real polar decomposition.

## The Jordan Reading

**Proposition.** On $\operatorname{Sym}_4$ the product $A\circ B=\tfrac12(AB+BA)$ is analytic, and the exponential satisfies $e^{A}\circ e^{B}\neq e^{A\circ B}$ in general, so the Jordan structure is not the Lie structure.

**Proof.** The Jordan product is a symmetric bilinear map; the failure of the exponential identity follows from the nonassociativity of the Jordan product and the associativity of the matrix exponential.

**Corollary.** The cone of squares of the Jordan algebra is the positive semidefinite cone, and its interior is the image of the exponential of the same half.

**Proof.** Every positive definite symmetric matrix is the square of one, and also the exponential of one.

**Corollary.** The exponential is a diffeomorphism of the symmetric half onto its cone, and the Jordan product is the algebraic shadow of the same cone.

**Proof.** The two descriptions of the same open set.

**The trace form.** The trace form $\operatorname{tr}(A\circ B)=\operatorname{tr}(AB)$ is the associative trace form of the Jordan algebra, and it is positive definite on the real symmetric half.

**Proof.** $\operatorname{tr}(S^{2})$ is the sum of the squares of the entries.

## Analysis against Algebra

**Proposition.** The statements that are analysis: the convergence of the exponential series, the inverse and implicit function theorems, the concavity of $\log\det$, the smoothness of the square root and the logarithm, and the discreteness of the fibres of the exponential on the skew half.

**Proof.** Each uses a limit, a derivative or a completeness argument.

**Corollary.** The statements that are algebra: the identity $\det e^{A}=e^{\operatorname{tr}A}$, the decomposition $M_4=\operatorname{Herm}\oplus\mathfrak{u}$, the polar decomposition as a bijection, the structure of the cone as a set of squares, and the eigenvalues $Q_t\pm iB$.

**Proof.** Each is an identity between algebraic expressions, valid for all matrices without any limit.

**Corollary.** The analysis enters through the positivity of the real numbers and the completeness of $\mathbb{C}$, and nowhere else.

**Proof.** The square root, the logarithm and the concavity all use the order of the reals; the algebraic identities hold over any field of characteristic zero with the appropriate square roots.

**The moral.** The two halves are one object seen through two structures: the algebra sees the split and the identities, the analysis sees the cone, the smooth structure and the exponential as a map of manifolds.

**Proof.** The two lists.

## Summary

The Hermitian and skew-Hermitian halves are linear subspaces of real dimension sixteen, complementary at every point, and each is its own tangent space. The exponential is a diffeomorphism from the Hermitian half onto the open cone and a surjection with discrete fibres from the skew half onto the unitary group.

The maps $A\mapsto A^{\ast}$, $\operatorname{tr}$, $\det$ and $A\mapsto A^{-1}$ are analytic, with derivatives $B^{\ast}$, $\operatorname{tr}B$, $\det(A)\operatorname{tr}(A^{-1}B)$ and $-A^{-1}BA^{-1}$; the map $A\mapsto A^{\ast}A$ is a submersion onto the Hermitian half with the unitary orbits as fibres.

The polar decomposition is a global analytic diffeomorphism $\mathrm{GL}_4\to\operatorname{Herm}_4^{++}\times U(4)$, over the reals $\mathrm{GL}_4(\mathbb{R})\to\operatorname{Sym}_4^{++}\times O(4)$. The Jordan structure sits on the symmetric half as the algebraic shadow of the same cone, and the analysis enters only through positivity and completeness.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Herm}_4$, $\mathfrak{u}(4)$ | the halves, dimension $16$ each |
| $d(\det)_{A}(B)=\det(A)\operatorname{tr}(A^{-1}B)$ | the derivative of the determinant |
| $B\mapsto B^{\ast}A+A^{\ast}B$ | the derivative of $A\mapsto A^{\ast}A$ |
| $\mathrm{GL}_4\to\operatorname{Herm}_4^{++}\times U(4)$ | the polar diffeomorphism |
| $A\circ B$ | the Jordan product on $\operatorname{Sym}_4$ |

## Further Reading

- John W. Milnor, *Topology from the Differentiable Viewpoint* (Princeton, 1965), for submersions and diffeomorphisms.
- [The Exponential and the Lie Group Structure at $n=4$](the-exponential-and-the-lie-group-structure-at-n-4.html), for the exponential and its differential.
- [The Positive Cone and Its Boundary at $n=4$](the-positive-cone-and-its-boundary-at-n-4.html), for the image of the Hermitian half.
- [The Jordan Algebra $\operatorname{Sym}_4$](the-jordan-algebra-sym-4.html), for the Jordan structure on the symmetric half.
- [The Two Halves and the Analysis: Smooth Structures at $n=2$](the-two-halves-and-the-analysis-smooth-structures-at-n-2.html), for the case at order two.
