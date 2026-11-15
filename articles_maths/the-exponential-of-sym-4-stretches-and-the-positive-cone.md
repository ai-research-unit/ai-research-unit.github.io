# __The Exponential of the Symmetric Part: Stretches and the Positive Cone at $n=4$__

## Introduction

**The exponential maps the sixteen-dimensional real space $\operatorname{Herm}_4$ of Hermitian matrices diffeomorphically onto the open cone $\operatorname{Herm}_4^{++}$ of positive definite ones, with inverse the principal logarithm; the cone is both the image of the map and the set of squares $A^{\ast}A$, the boundary is the set of matrices of rank less than four, and every invertible matrix is the product of a stretch and a rotation.**

The article proves that the exponential stays in the Hermitian half, that its eigenvalues are the exponentials of the eigenvalues, that it is injective with the logarithm as inverse, that it is a diffeomorphism onto the open cone, that the cone is the set of squares, and that the boundary is the closed complement stratified by rank. It then reads the polar decomposition as the product of the stretch and the rotation, computes the determinant and the trace of the image, and identifies the ten symmetric matrices of the axis-free basis as the coordinates of the stretch.

It assumes *The Spectral Theorem: the Hermitian Case at $n=4$* and *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric*. The model at order two is *The Exponential of $\operatorname{Sym}_2$: Stretches and the Positive Cone*; the cone and its faces are *The Positive Cone and Its Boundary at $n=4$*.

## The Exponential on Hermitian Matrices

**Proposition.** $H^{\ast}=H$ implies $(e^{H})^{\ast}=e^{H}$, so the exponential maps $\operatorname{Herm}_4$ into itself, and its image is positive definite.

**Proof.** The transpose of the series is the series of the adjoint, and the eigenvalues of $e^{H}$ are $e^{\lambda_k}>0$.

**Corollary.** $e^{H}$ is the sum $\sum_ke^{\lambda_k}P_k$ of its spectral projectors, so the exponential acts on each eigenspace by the scalar multiple.

**Proof.** The spectral resolution and the functional calculus for the exponential.

**Corollary.** $\det e^{H}=e^{\operatorname{tr}H}$ and $\operatorname{tr}e^{H}=\sum_ke^{\lambda_k}$.

**Proof.** The determinant is the product of the eigenvalues and the trace their sum.

**The stretch along a line.** For a unit vector $v$ the matrix $t\,vv^{\ast}$ has the exponential $\mathrm I_4+(e^{t}-1)vv^{\ast}$, the stretch by $e^{t}$ along $v$ and by one on the orthogonal complement.

**Proof.** $vv^{\ast}$ has the eigenvalue one on the line and zero on the complement, so $t\,vv^{\ast}$ has eigenvalues $t$ and $0$.

**Corollary.** Every element of the open cone is a stretch along four orthogonal axes with the positive factors $\lambda_k$, and the logarithm is the sum $\sum_k(\log\lambda_k)P_k$.

**Proof.** The spectral resolution of the element and the spectral resolution of the logarithm.

## The Inverse Logarithm

**Theorem.** The exponential is injective on $\operatorname{Herm}_4$, with inverse $\log A=\sum_k(\log\lambda_k)P_k$ on the open cone.

**Proof.** If $e^{H}=e^{H'}$ then the spectral projectors of the two sides agree, since they are determined by the values of the exponential; the eigenvalues satisfy $e^{\lambda}=e^{\mu}$ with $\lambda,\mu$ real, hence $\lambda=\mu$, so $H=H'$.

**Corollary.** The logarithm is real-analytic on the open cone and satisfies $\exp\log=\mathrm{id}$ and $\log\exp=\mathrm{id}$ there.

**Proof.** The two compositions, computed on the spectral resolutions.

**Corollary.** $A^{t}=\exp(t\log A)$ is defined for every positive definite $A$ and every real $t$, and $A^{1/2}$ is the unique positive definite square root.

**Proof.** The functional calculus on the spectrum, and the uniqueness of the positive square root.

**The derivative.** The differential of the exponential at $H$ is invertible, so the map is a local diffeomorphism at every point of $\operatorname{Herm}_4$.

**Proof.** The differential of the exponential at $H$ is the map $X\mapsto\sum_{k,l}\frac{e^{\lambda_k}-e^{\lambda_l}}{\lambda_k-\lambda_l}P_kXP_l$, whose eigenvalues are the divided differences, all positive for real $\lambda_k$; the derivative is therefore an isomorphism of the sixteen-dimensional space.

**Corollary.** $\exp:\operatorname{Herm}_4\to\operatorname{Herm}_4^{++}$ is a diffeomorphism: bijective, smooth, with smooth inverse.

**Proof.** Injectivity and surjectivity with the smooth logarithm of the previous theorem, and invertibility of the differential at every point.

## The Cone as Image and as Squares

**Theorem.** $\operatorname{Herm}_4^{++}=\{A^{\ast}A:A\in GL_4(\mathbb{C})\}$, the set of all products of a matrix with its adjoint.

**Proof.** If $A$ is invertible then $A^{\ast}A$ is Hermitian with eigenvalues the squared singular values, all positive. Conversely a positive definite $B$ has the positive definite square root $B^{1/2}$, and $B=(B^{1/2})^{\ast}B^{1/2}$.

**Corollary.** The open cone is the image of the exponential, the set of squares of invertible matrices, and the interior of the set of squares of all matrices.

**Proof.** The two descriptions and the closure statement of the next section.

**Corollary.** The cone is invariant under congruence $A\mapsto S^{\ast}AS$ for invertible $S$, and the group acts transitively on it.

**Proof.** $(SA)^{\ast}(SA)=A^{\ast}S^{\ast}SA$ is again a square, and transitivity follows from the spectral theorem: every positive definite matrix is $U\operatorname{diag}(\lambda)U^{\ast}$, which is the image of $\operatorname{diag}(\lambda)$.

**The Jordan reading.** In the Jordan algebra $\operatorname{Herm}_4$ under the anticommutator the cone is the set of squares, and the exponential is the Jordan-theoretic exponential.

**Proof.** $A\circ A=A^{2}$ for the anticommutator, and the exponential of a Hermitian element in the Jordan sense agrees with the matrix exponential because the element and its powers commute.

## The Boundary

**Theorem.** The boundary of the cone is $\{A\in\operatorname{Herm}_4:\lambda_4(A)=0\}$, the set of positive semidefinite matrices of rank at most three.

**Proof.** A positive semidefinite matrix is a limit of positive definite ones by adding $\varepsilon\mathrm I_4$; it fails to be interior exactly when it has a zero eigenvalue, since then a small negative perturbation in that eigendirection leaves the cone.

**Corollary.** The boundary is stratified by rank,
$$
\partial\operatorname{Herm}_4^{++}=\bigcup_{k=0}^{3}\{A:\operatorname{rank}A=k\},
$$
with the stratum of rank $k$ of real dimension $2k(4-k)+k^{2}$ inside $\operatorname{Herm}_4$.

**Proof.** A rank-$k$ Hermitian matrix is $U\operatorname{diag}(\lambda_1,\dots,\lambda_k,0,\dots,0)U^{\ast}$ with the $k$ positive eigenvalues and the unitary of the $k$-plane; the dimension count is $k$ for the eigenvalues, $2k(4-k)$ for the plane and $k^{2}$ for the unitary inside it.

**Corollary.** The extreme stratum is the origin, of dimension zero; the largest is the rank-three stratum, of real dimension $2\cdot3\cdot1+9=15$.

**Proof.** The formula at $k=0$ and $k=3$.

**The faces.** A face of the cone is the set of matrices whose kernel contains a fixed subspace, and the faces are in bijection with the subspaces of $\mathbb{C}^{4}$.

**Proof.** If $A$ and $B$ are positive semidefinite and $A+B$ vanishes on a vector, both do; so the vanishing sets of a face are nested, and conversely a fixed subspace defines a face by the condition that the matrix vanish on it.

## The Polar Decomposition

**Theorem.** Every invertible $A$ is uniquely $A=HU$ with $H$ positive definite Hermitian and $U$ unitary.

**Proof.** Put $H=(AA^{\ast})^{1/2}$, which is positive definite, and $U=H^{-1}A$; then $U^{\ast}U=A^{\ast}H^{-2}A=A^{\ast}(AA^{\ast})^{-1}A=\mathrm I_4$, so $U$ is unitary. Uniqueness: $AA^{\ast}=H^{2}$ determines $H$ as the positive square root, and then $U$.

**Corollary.** The multiplication map $\operatorname{Herm}_4^{++}\times U(4)\to GL_4(\mathbb{C})$ is a diffeomorphism.

**Proof.** The polar decomposition gives a bijection, and the inverse $A\mapsto((AA^{\ast})^{1/2},(AA^{\ast})^{-1/2}A)$ is smooth.

**Corollary.** $GL_4(\mathbb{C})$ is homeomorphic to $\operatorname{Herm}_4^{++}\times U(4)$, and since the first factor is convex it is homotopy equivalent to $U(4)$.

**Proof.** The diffeomorphism, and a convex set is contractible.

**The stretch and the rotation.** In the polar form $H$ is the stretch, with the singular values of $A$ on its diagonal in a suitable frame, and $U$ is the rotation part; the exponential of the symmetric part is the stretch factor of the decomposition.

**Proof.** The singular values of $A$ are the eigenvalues of $H$.

## The Axis-Free Reading

**Theorem.** In the axis-free basis the symmetric matrices are the ten elements $T_{\mu\nu}$ with $\operatorname{tr}(T_{\mu\nu}T_{\rho\sigma})=+4\delta$, and a Hermitian element is $\sum c_{\mu\nu}T_{\mu\nu}$ with real coefficients on the ten and purely imaginary on the six.

**Proof.** The trace pairing takes the value $+4$ exactly on the symmetric set and $-4$ on the antisymmetric one, and a matrix is Hermitian exactly when the coefficients of the antisymmetric part are purely imaginary.

**Corollary.** The exponential of a Hermitian element has the logarithm $\sum c_{\mu\nu}T_{\mu\nu}$ on the ten directions, so the stretch is read in the same ten coordinates as the cone.

**Proof.** The logarithm of a positive definite element is Hermitian, hence has real coefficients on the ten.

**Corollary.** $\operatorname{tr}H=4c_{tt}$ and $\det e^{H}=e^{4c_{tt}}$, so the coordinate $c_{tt}$ alone controls the volume factor of the stretch.

**Proof.** Only $T_{tt}=\mathrm I_4$ has nonzero trace, and the determinant formula.

**The ten are the stretch.** The ten symmetric basis elements are the coordinate directions of the stretch, and the six antisymmetric ones are the directions of the rotation; the two halves are the two factors of the polar decomposition at the level of the Lie algebra.

**Proof.** The Hermitian part is the stretch and the skew-Hermitian part is the rotation generator, and the split is the split of the two halves.

## Summary

The exponential maps the sixteen-dimensional Hermitian space diffeomorphically onto the open cone of positive definite matrices, with the principal logarithm as inverse; the differential is invertible everywhere, given by divided differences of the eigenvalues.

The image is the set of squares $A^{\ast}A$ of invertible matrices, invariant under congruence, and the boundary is the set of matrices of rank at most three, stratified by rank with the stratum of rank $k$ of real dimension $2k(4-k)+k^{2}$. The faces are indexed by subspaces.

The polar decomposition writes every invertible matrix as a stretch times a rotation, so $GL_4$ is diffeomorphic to the product of the open cone and $U(4)$. In the axis-free basis the stretch uses the ten symmetric elements, the rotation the six antisymmetric ones, and the coefficient $c_{tt}$ alone gives the volume factor.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Herm}_4^{++}$ | the open cone of positive definite matrices |
| $\log A$ | the principal logarithm on the cone |
| $A^{1/2}$ | the positive definite square root |
| $2k(4-k)+k^{2}$ | the real dimension of the rank-$k$ stratum |
| $A=HU$ | the polar decomposition |
| $c_{tt}$ | the coefficient of the identity, with $\operatorname{tr}H=4c_{tt}$ |

## Further Reading

- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the exponential, the logarithm and the polar decomposition.
- [The Positive Cone and Its Boundary at $n=4$](the-positive-cone-and-its-boundary-at-n-4.html), for the cone, its faces and its automorphisms.
- [The Spectral Theorem: the Hermitian Case at $n=4$](the-spectral-theorem-the-hermitian-case-at-n-4.html), for the spectral resolution used throughout.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric](the-two-halves-over-r-symmetric-and-antisymmetric-at-n-4.html), for the two halves and their dimensions.
- [The Exponential of $\operatorname{Sym}_2$: Stretches and the Positive Cone](the-exponential-of-sym-2-stretches-and-the-positive-cone.html), for the case at order two.
