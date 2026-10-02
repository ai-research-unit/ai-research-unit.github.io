# __The Curvature Operator__

## Introduction

The curvature tensor of a Riemannian manifold has two faces. Read with three vectors it is the endomorphism $R(X, Y)$ of the tangent space; read with four, and with the metric, it is a $(0, 4)$-tensor with exactly the symmetries of a curvature form. The second reading has a third form, which this article develops: the curvature is a **self-adjoint endomorphism of the second exterior power** $\Lambda^2T_pM$, the **curvature operator** $\mathcal{R}$. In this form the curvature is a single linear operator at each point, its eigenvalues and eigenvectors carry the curvature information, and its traces are the Ricci and the scalar curvatures.

The article develops the operator picture. It defines the inner product on bivectors and the curvature operator, and proves that the operator is self-adjoint and that it carries exactly the information of the curvature tensor; it shows that the **sectional curvature** is the quadratic form of the operator on the decomposable bivectors; it shows that the **Ricci curvature** is the contraction of the operator with a frame, and that the **scalar curvature** is twice its trace; it gives the decomposition of the operator into its scalar, traceless-Ricci and Weyl parts, which is the decomposition of the curvature into its irreducible pieces under the orthogonal group; and it reads off the constant-curvature metrics as the operators that are scalar multiples of the identity, with the sphere and the hyperbolic space as the two signs.

The article assumes the metric, the Levi-Civita connection and the curvature tensor of *Curvature and Geodesics* and *Riemannian Geometry*, and the exterior algebra and the exterior power $\Lambda^2$ of Part I. The Hodge star and its splitting of the Weyl part in dimension four are *The Involution on the Curvature Operator*, later in this category; the curvature of the complex and Hermitian metrics, and the Kähler identities, are the Hermitian and Kähler geometry of later categories of this Part, and are cited rather than developed. The operator $R(X, Y)$ on the tangent space, which *Riemannian Geometry* calls the curvature operator, is the curvature tensor read on a pair of vectors and is not the object of this article. No physics is invoked.

## Bivectors and the Exterior Square

### The Inner Product on Bivectors

**Definition.** For a Euclidean vector space $(V, g)$ the **second exterior power** $\Lambda^2V$ is spanned by the **bivectors** $X\wedge Y$ subject to $X\wedge Y = -Y\wedge X$, with the inner product

$$
\langle X\wedge Y,\, Z\wedge W\rangle = g(X, Z)\,g(Y, W) - g(X, W)\,g(Y, Z),
$$

extended bilinearly. The form is symmetric and positive definite; if $e_1, \ldots, e_n$ is an orthonormal basis of $V$ then $\{e_i\wedge e_j\}_{i < j}$ is an orthonormal basis of $\Lambda^2V$, of dimension $N = \frac{1}{2}n(n-1)$. The **Gram determinant** of a decomposable bivector is

$$
|X\wedge Y|^2 = |X|^2|Y|^2 - g(X, Y)^2 \geq 0,
$$

which is the Cauchy–Schwarz deficit, and it vanishes exactly when $X$ and $Y$ are proportional.

**Proposition.** A bivector $\omega \in \Lambda^2V$ is **decomposable**, that is $\omega = X\wedge Y$ for vectors $X, Y$, if and only if $\omega\wedge\omega = 0$ in $\Lambda^4V$; for $n = 3$ every bivector is decomposable, and for $n \geq 4$ the decomposable bivectors form the cone over the Grassmannian $\mathrm{Gr}_2(V)$ of the two-planes of $V$.

**Proof.** For $\omega = X\wedge Y$ one has $\omega\wedge\omega = 0$ by the antisymmetry of the exterior product; conversely a bivector with vanishing square is of rank two and is a wedge of two vectors, which is the standard characterisation of the decomposable elements of an exterior power. The identification of the rays of the decomposable cone with the two-planes is the definition of the Grassmannian, whose geometry is *Grassmannians and Stiefel Manifolds* later in this Part.

### The Curvature Operator

**Definition.** Let $(M, g)$ be a Riemannian manifold with curvature tensor $R(X, Y)Z$ and $R(X, Y, Z, W) = g(R(X, Y)Z, W)$. The **curvature operator** at $p$ is the endomorphism

$$
\mathcal{R} : \Lambda^2T_pM \longrightarrow \Lambda^2T_pM
$$

characterised by

$$
\bigl\langle \mathcal{R}(X\wedge Y),\, Z\wedge W\bigr\rangle = R(X, Y, W, Z)
$$

for all $X, Y, Z, W \in T_pM$. The definition is consistent: the right-hand side is alternating in $X, Y$ and in $Z, W$, hence depends on the bivectors alone, and it is $\mathbb{R}$-bilinear, so it defines a bilinear form on $\Lambda^2T_pM$, which by nondegeneracy of the inner product is given by a unique endomorphism.

**Theorem (self-adjointness).** The curvature operator is self-adjoint: $\langle \mathcal{R}\omega, \eta\rangle = \langle \omega, \mathcal{R}\eta\rangle$ for all bivectors $\omega, \eta$. Equivalently, the bilinear form $(X, Y, Z, W) \mapsto R(X, Y, W, Z)$ is symmetric under the exchange of the pair $(X, Y)$ with $(Z, W)$.

**Proof.** For decomposable bivectors the statement is

$$
R(X, Y, W, Z) = R(Z, W, Y, X),
$$

which is the pair symmetry $R(a, b, c, d) = R(c, d, a, b)$ of the curvature tensor applied twice: $R(X,Y,W,Z) = R(W,Z,X,Y)$, and then $R(W,Z,X,Y) = R(Z,W,Y,X)$ by the antisymmetry in each pair. Both sides are bilinear in the decomposable generators and the decomposable bivectors span $\Lambda^2T_pM$, so the identity extends to all bivectors.

## The Curvature Tensor and the Operator

**Theorem.** The assignment $R \mapsto \mathcal{R}$ is a linear isomorphism between the $(0, 4)$-tensors at $p$ that are alternating in the first pair and in the second pair and symmetric under the exchange of the pairs, and the self-adjoint endomorphisms of $\Lambda^2T_pM$.

**Proof.** Given a self-adjoint endomorphism $\mathcal{R}$ of $\Lambda^2T_pM$, define $R(X,Y,Z,W) = \langle \mathcal{R}(X\wedge Y), W\wedge Z\rangle$. The right-hand side is alternating in $X, Y$ and in $Z, W$ because the bivectors are, and it is symmetric under exchanging the pairs by the self-adjointness. The two constructions are inverse: substituting one into the other returns the original object, since a bilinear form on $\Lambda^2T_pM$ determines and is determined by its endomorphism. Both spaces have dimension $\frac{1}{2}N(N+1)$ with $N = \frac{1}{2}n(n-1)$, so the linear map is injective and hence an isomorphism.

**Definition.** The **first Bianchi identity** is the vanishing of the cyclic sum

$$
R(X, Y, Z, W) + R(Y, Z, X, W) + R(Z, X, Y, W) = 0 .
$$

It is a single linear condition on the symmetric endomorphisms of $\Lambda^2T_pM$, cutting out the subspace of the **algebraic curvature tensors**, of dimension $\frac{1}{12}n^2(n^2-1)$, the count left by the symmetries of the curvature tensor.

**Proposition.** The curvature operator of a Riemannian metric satisfies the first Bianchi identity.

**Proof.** The curvature of the Levi-Civita connection is the curvature of a torsion-free connection, and for the $(0,4)$-form of a torsion-free connection the first Bianchi identity is the Jacobi identity of the Lie bracket read on three vector fields; it is derived in *Riemannian Geometry* from the structure equation and is quoted here.

The proposition is the one place where the metric enters the algebraic classification: an arbitrary self-adjoint endomorphism of $\Lambda^2T_pM$ has more freedom than a curvature operator, and the Bianchi condition selects the curvature ones.

## The Sectional Curvature

**Theorem.** For a two-plane $\sigma \subseteq T_pM$ with a basis $X, Y$ the sectional curvature is the Rayleigh quotient of the curvature operator at the bivector $X\wedge Y$:

$$
K(\sigma) = \frac{R(X, Y, Y, X)}{|X\wedge Y|^2} = \frac{\bigl\langle \mathcal{R}(X\wedge Y),\, X\wedge Y\bigr\rangle}{|X\wedge Y|^2}.
$$

Consequently the sectional curvature is the restriction of the quadratic form $\omega \mapsto \langle \mathcal{R}\omega, \omega\rangle$ to the decomposable bivectors of unit length, and the values of the sectional curvature at $p$ determine the whole curvature tensor at $p$.

**Proof.** The first equality is the definition of the sectional curvature and the second is the definition of $\mathcal{R}$ with $Z = X$, $W = Y$. The sectional curvatures determine the quadratic form on the decomposable bivectors; they span $\Lambda^2T_pM$, and a quadratic form is determined by its values on a spanning set, by the polarisation identity; hence the form, and with it the operator and the tensor, is determined.

**Theorem (positivity).** If the curvature operator is positive semidefinite, $\langle \mathcal{R}\omega, \omega\rangle \geq 0$ for every bivector $\omega$, then the sectional curvature is nonnegative. If the operator is positive definite the sectional curvature is positive.

**Proof.** A decomposable bivector $X\wedge Y$ is a bivector, so the hypothesis gives $\langle \mathcal{R}(X\wedge Y), X\wedge Y\rangle \geq 0$, and division by $|X\wedge Y|^2 > 0$ gives $K \geq 0$.

**Remark (the converse fails in dimension at least four).** The inequality $\langle \mathcal{R}\omega,\omega\rangle \geq 0$ is required on the whole of $\Lambda^2T_pM$, while the sectional curvature sees only the decomposable cone. In dimension three every bivector is decomposable, so the two conditions coincide; in dimension at least four the decomposable cone is a proper closed cone, and a quadratic form that is nonnegative on it need not be nonnegative on the whole space, since a quadratic form is not monotone on a non-convex cone. A metric whose curvature operator has a negative eigenvalue therefore need not have a negative sectional curvature, and such metrics exist. The point is the one the article records throughout: the operator is a strictly finer object than the collection of its values on the decomposable bivectors, even though those values determine it.

## The Ricci Curvature and the Scalar Curvature

**Theorem (the Ricci contraction).** For any $X, Y \in T_pM$ and any orthonormal basis $e_1, \ldots, e_n$ of $T_pM$,

$$
\operatorname{Ric}(X, Y) = \sum_{i=1}^{n} \bigl\langle \mathcal{R}(X\wedge e_i),\, Y\wedge e_i\bigr\rangle .
$$

The Ricci tensor is therefore the **contraction** of the curvature operator with the metric on one factor of each bivector.

**Proof.** With the definition of $\mathcal{R}$, the summand is $\langle \mathcal{R}(X\wedge e_i), Y\wedge e_i\rangle = R(X, e_i, e_i, Y)$. Using the antisymmetry in each pair, $R(X,e_i,e_i,Y) = -R(X,e_i,Y,e_i) = R(e_i,X,Y,e_i)$, so the sum is $\sum_iR(e_i,X,Y,e_i)$, which is the definition of the Ricci tensor.

**Corollary (the trace).** The trace of the curvature operator over the orthonormal basis $\{e_i\wedge e_j\}_{i<j}$ of $\Lambda^2T_pM$ is one half of the scalar curvature:

$$
\operatorname{tr}\mathcal{R} = \sum_{i<j} \bigl\langle \mathcal{R}(e_i\wedge e_j),\, e_i\wedge e_j\bigr\rangle = \tfrac{1}{2}S .
$$

**Proof.** Each summand is $R(e_i, e_j, e_j, e_i)$, and by the pair symmetry this equals $R(e_j, e_i, e_i, e_j)$. The scalar curvature is $S = \sum_{i}\operatorname{Ric}(e_i, e_i) = \sum_{i,j}R(e_j, e_i, e_i, e_j)$, the diagonal terms vanishing because the curvature is alternating; hence $S = \sum_{i\neq j}R(e_j,e_i,e_i,e_j) = 2\sum_{i<j}R(e_i,e_j,e_j,e_i) = 2\operatorname{tr}\mathcal{R}$, since each unordered pair occurs twice with the same value.

**Remark.** The two traces are the first two of the chain $R \to \mathcal{R} \to \operatorname{Ric} \to S$: the operator is the curvature, its contraction with one factor is the Ricci tensor, and its trace is half the scalar curvature. Each step is a contraction and each loses information, exactly as in the tensor picture.

## The Decomposition of the Curvature Operator

### The Scalar and the Traceless Ricci Parts

**Definition.** The **traceless Ricci tensor** is $\operatorname{Ric}_0 = \operatorname{Ric} - \frac{1}{n}S\,g$. The **Weyl tensor** is

$$
W = R - \frac{1}{n-2}\Bigl(\operatorname{Ric} - \frac{1}{2(n-1)}S\,g\Bigr)\owedge g,
$$

where the **Kulkarni–Nomizu product** of symmetric $(0,2)$-tensors $h, k$ is

$$
(h\owedge k)(X, Y, Z, W) = h(X, Z)k(Y, W) + h(Y, W)k(X, Z) - h(X, W)k(Y, Z) - h(Y, Z)k(X, W).
$$

The Weyl tensor has the symmetries of the curvature, it satisfies the first Bianchi identity, and it is **totally trace-free**: every contraction of two of its slots with the metric vanishes. In dimension $n \leq 3$ it vanishes identically, and in dimension $n \geq 4$ it vanishes exactly for the locally conformally flat metrics.

**Theorem.** The curvature operator decomposes as a sum of three self-adjoint endomorphisms, orthogonal with respect to the trace pairing,

$$
\mathcal{R} = \frac{S}{n(n-1)}\,\mathrm{id} + \mathcal{R}_0 + \mathcal{W},
$$

where the first summand is scalar, the second is the image of the traceless Ricci tensor $\operatorname{Ric}_0$ under the identification of the previous section applied to the tensor $\operatorname{Ric}_0 \owedge g$, and the third, the **Weyl operator**, is the image of the Weyl tensor. The three summands are the isotypic components of $\mathcal{R}$ under the orthogonal group $O(T_pM, g_p)$: the trivial representation, the traceless symmetric square, and the Weyl module.

**Proof sketch.** The identification of the previous section is $O(T_pM,g_p)$-equivariant, so it carries the decomposition of the curvature tensors into irreducible representations to a decomposition of the operators. The tensor decomposition $R = \frac{S}{2n(n-1)}g\owedge g + \frac{1}{n-2}\operatorname{Ric}_0\owedge g + W$ is a direct computation in the tensor calculus: the scalar multiple of $g\owedge g$ has scalar curvature $S$ and vanishing traceless Ricci and Weyl parts, the product $\operatorname{Ric}_0\owedge g$ has traceless Ricci part $\operatorname{Ric}_0$ and vanishing Weyl part, and the remainder is totally trace-free, hence the Weyl tensor. The image of $g\owedge g$ under the identification is a multiple of the identity: $g\owedge g(X,Y,Z,W) = 2\langle X\wedge Y, Z\wedge W\rangle$, and the constant is fixed by matching the trace, $2\operatorname{tr}\mathcal{R} = S$, which gives the coefficient $\frac{S}{n(n-1)}$.

### The Weyl Operator and the Hodge Star

**Corollary.** The scalar part of $\mathcal{R}$ is the identity with eigenvalue $\frac{S}{n(n-1)}$; the traceless Ricci part is obtained by the contraction of the operator with the metric and carries the same information as $\operatorname{Ric}_0$; and the Weyl part is the totally trace-free part, invisible to both the Ricci and the scalar curvatures. In dimension three the Weyl part vanishes, so the curvature operator is determined by the Ricci tensor; in dimension two the whole operator is the scalar multiple $\mathcal{R} = K\,\mathrm{id}$ of the identity on the one-dimensional $\Lambda^2T_pM$, with $K$ the Gaussian curvature.

**Proof.** The eigenvector statement is the definition of the scalar summand. In dimension three, $\Lambda^2T_pM$ has dimension three and the Weyl module is zero, so the traceless Ricci part exhausts the traceless part; in dimension two, $\Lambda^2T_pM$ is spanned by a single bivector and $S = 2K$, so $\mathcal{R} = K\,\mathrm{id}$ by the trace computation.

**Remark (the dimension-four refinement).** In dimension four the exterior square splits as $\Lambda^2 = \Lambda^2_+\oplus\Lambda^2_-$ into the self-dual and anti-self-dual bivectors, the eigenspaces of the Hodge star; the Weyl operator respects this splitting only when the metric is Einstein, and the components $\mathcal{W}_\pm$ and the mixed part carry the conformal curvature. The splitting and the involution of the Hodge star on the curvature operator are *The Involution on the Curvature Operator*, later in this category.

## Constant Curvature and the Sign of the Operator

**Theorem.** The metric has constant sectional curvature $\lambda$ at $p$ if and only if

$$
\mathcal{R} = \lambda\,\mathrm{id}_{\Lambda^2T_pM}.
$$

**Proof.** If the sectional curvature is the constant $\lambda$ then the curvature tensor is $R(X,Y)Z = \lambda(g(Y,Z)X - g(X,Z)Y)$, so $R(X,Y,W,Z) = \lambda(g(Y,W)g(X,Z)-g(X,W)g(Y,Z)) = \lambda\langle X\wedge Y, Z\wedge W\rangle$, and the operator is $\lambda\,\mathrm{id}$. Conversely if $\mathcal{R} = \lambda\,\mathrm{id}$ then $R(X,Y,W,Z) = \lambda\langle X\wedge Y, Z\wedge W\rangle = \lambda(g(Y,W)g(X,Z)-g(X,W)g(Y,Z))$, which gives $R(X,Y)Z = \lambda(g(Y,Z)X-g(X,Z)Y)$ and $K = \lambda$ on every plane.

**Example (the model spaces).** On the round sphere of radius $r$ the operator is $\frac{1}{r^2}\mathrm{id}$; on Euclidean space it is $0$; on hyperbolic space of curvature $-1/r^2$ it is $-\frac{1}{r^2}\mathrm{id}$. The sphere is the operator with all eigenvalues equal and positive, the hyperbolic space the one with all eigenvalues equal and negative, and the flat space the one with all eigenvalues zero, which is the operator form of the three model geometries.

**Example (a product).** For a Riemannian product $M_1\times M_2$ the curvature vanishes on the bivectors that mix the two factors, and on the bivectors inside one factor it is the operator of that factor; so the curvature operator is block diagonal with the two operators $\mathcal{R}_1, \mathcal{R}_2$ and a zero block. On $\mathbb{R}\times S^n$ the operator is positive semidefinite with a one-dimensional kernel, on the mixed bivectors, and the sectional curvature is nonnegative but vanishes on the planes spanned by the flat direction and a tangent vector of the sphere.

## Summary

The curvature of a Riemannian manifold is a self-adjoint endomorphism $\mathcal{R}$ of the second exterior power $\Lambda^2T_pM$, defined by $\langle\mathcal{R}(X\wedge Y), Z\wedge W\rangle = R(X,Y,W,Z)$ with the inner product $\langle X\wedge Y, Z\wedge W\rangle = g(X,Z)g(Y,W)-g(X,W)g(Y,Z)$. Self-adjointness is the pair symmetry of the curvature tensor, and the assignment is a linear isomorphism from the symmetric endomorphisms of $\Lambda^2T_pM$ onto the curvature-type tensors; the first Bianchi identity is the single extra linear condition, automatically satisfied by the curvature of the Levi-Civita connection, and it cuts out the algebraic curvature tensors.

The sectional curvature is the Rayleigh quotient of the operator at the decomposable bivectors, and the sectional curvatures determine the whole curvature tensor. A positive (semi)definite operator gives positive (nonnegative) sectional curvature; the converse fails in dimension at least four, because the decomposable bivectors form a proper cone and a quadratic form nonnegative on a cone need not be nonnegative on the span. The Ricci tensor is the contraction of the operator with a frame, $\operatorname{Ric}(X,Y) = \sum_i\langle\mathcal{R}(X\wedge e_i), Y\wedge e_i\rangle$, and the scalar curvature is twice its trace, $\operatorname{tr}\mathcal{R} = S/2$.

The operator decomposes into three orthogonal self-adjoint parts, $\mathcal{R} = \frac{S}{n(n-1)}\mathrm{id} + \mathcal{R}_0 + \mathcal{W}$, the scalar part, the traceless-Ricci part and the Weyl part, which are the isotypic components for the orthogonal group; the Weyl part is totally trace-free and vanishes in dimension at most three. The metric has constant curvature $\lambda$ exactly when the operator is the scalar $\lambda\,\mathrm{id}$, so the three model geometries are the three signs of the identity operator; a Riemannian product has a block-diagonal operator with a zero block on the mixed bivectors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Lambda^2T_pM$, $X\wedge Y$ | Second exterior power and its decomposable bivectors |
| $\langle X\wedge Y, Z\wedge W\rangle = g(X,Z)g(Y,W)-g(X,W)g(Y,Z)$ | Inner product on bivectors |
| $\vert X\wedge Y\vert^2$ | Gram determinant; vanishes iff $X, Y$ proportional |
| $\mathcal{R}$ | Curvature operator, self-adjoint on $\Lambda^2T_pM$ |
| $\langle\mathcal{R}(X\wedge Y), Z\wedge W\rangle = R(X,Y,W,Z)$ | Defining identity of $\mathcal{R}$ |
| $K(\sigma)$ | Sectional curvature, the Rayleigh quotient of $\mathcal{R}$ |
| $\operatorname{Ric}(X,Y) = \sum_i\langle\mathcal{R}(X\wedge e_i), Y\wedge e_i\rangle$ | Ricci contraction of the operator |
| $S$, $\operatorname{tr}\mathcal{R} = S/2$ | Scalar curvature and the operator trace |
| $\operatorname{Ric}_0 = \operatorname{Ric} - \frac1nSg$ | Traceless Ricci tensor |
| $h\owedge k$ | Kulkarni–Nomizu product of symmetric $(0,2)$-tensors |
| $W$ | Weyl tensor; totally trace-free, zero in dimension $\leq 3$ |
| $\mathcal{R}_0$, $\mathcal{W}$ | Traceless-Ricci and Weyl parts of $\mathcal{R}$ |
| $\Lambda^2 = \Lambda^2_+\oplus\Lambda^2_-$ | Self-dual and anti-self-dual bivectors in dimension four |
| $\mathcal{R} = \lambda\,\mathrm{id}$ | Constant curvature $\lambda$ |

## Further Reading

- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume I* (Interscience, 1963), for the curvature tensor, its symmetries and the holonomy.
- Manfredo P. do Carmo, *Riemannian Geometry* (Birkhäuser, 1992), for the sectional, Ricci and scalar curvatures and Schur's theorem.
- Sylvestre Gallot, Dominique Hulin and Jacques Lafontaine, *Riemannian Geometry*, 3rd ed. (Springer, 2004), for the curvature operator on $\Lambda^2$, its spectrum and its decomposition.
- Peter Petersen, *Riemannian Geometry*, 3rd ed. (Springer, 2016), for the curvature operator, the Bochner technique and the positivity conditions.
- Gerard Walschap, *Metric Structures in Differential Geometry* (Springer, 2004), for the curvature operator, the Kulkarni–Nomizu product and the decomposition of the curvature tensor.
- Hermann Weyl, "Reine Infinitesimalgeometrie", *Mathematische Zeitschrift* 2 (1918), 384–411, for the conformal curvature tensor and the local conformal flatness in dimension at least four.
