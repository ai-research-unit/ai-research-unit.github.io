# __The Involution on the Curvature Operator__

## Introduction

The curvature tensor of a Riemannian manifold is a tensor of four arguments with a rigid pattern of symmetries, and the pattern is best described by two **involutions**. The first is the **skew-symmetry**: the tensor is alternating in the first pair of arguments and in the second pair separately, so it is a two-form in each pair and lives in $\Lambda^2\otimes\Lambda^2$. The second is the **pair symmetry**: the tensor is unchanged when the two pairs are exchanged, and this is exactly the statement that the **curvature operator** $\mathcal{R}$ of *The Curvature Operator* is a self-adjoint operator on the space of the bivectors $\Lambda^2$. The two involutions, together with the first Bianchi identity, characterise the curvature tensors among all the symmetric bilinear forms on the bivectors. A third involution enters in even dimension, the Hodge star on $\Lambda^2$, and its $\pm1$-eigenspaces decompose the curvature operator into the **self-dual** and the **anti-self-dual** parts, the decomposition that organises the curvature of a four-manifold.

The article develops the involutions that the curvature tensor carries. It reads the skew-symmetry of the curvature as the statement that the tensor is a section of $\Lambda^2\otimes\Lambda^2$; it proves that the pair symmetry is the self-adjointness of the curvature operator and that the first Bianchi identity is the vanishing of the Bianchi map, so that the curvature tensors are the self-adjoint operators lying in the kernel of the Bianchi map; it proves that the curvature operator is diagonalisable with real eigenvalues and that the sectional curvature is the quadratic form it defines; it develops the Hodge star as an involution of $\Lambda^2$ in even dimension and the self-dual and anti-self-dual splitting it induces on the curvature operator; and it shows how an isometric involution, a real structure and a complex structure act on the curvature operator by an involution that preserves its symmetries.

The article assumes the curvature, the curvature tensor and the sectional curvature of *Curvature and Geodesics* and *Riemannian Geometry*, the curvature operator $\mathcal R$ on the bivectors and its expression in an orthonormal frame from *The Curvature Operator*, and the isometric involutions from the preceding articles of this category; the Hodge star and the exterior algebra are Part III's. The Einstein condition, the Ricci flow and the four-dimensional geometry are *Ricci Flow* and *Curvature and Geodesics* elsewhere in this Part, and the Kähler geometry is the Hermitian article of this group. No physics is invoked.

## The Symmetries of the Curvature Tensor

### The Skew-Symmetry

**Definition.** The curvature tensor of a Riemannian manifold is the tensor

$$
R(X, Y, Z, W) = \bigl\langle R(X, Y)Z,\, W\bigr\rangle,
$$

and it is **alternating in each pair**: for all vectors $X, Y, Z, W$,

$$
R(X, Y, Z, W) = -R(Y, X, Z, W), \qquad R(X, Y, Z, W) = -R(X, Y, W, Z).
$$

Equivalently, the curvature is a section of $\Lambda^2T^*M\otimes\Lambda^2T^*M$: it is a two-form in the pair $(X, Y)$ and a two-form in the pair $(Z, W)$.

**Proof.** The first identity is $R(X,Y) = -R(Y,X)$, which is the antisymmetry of the curvature operator of *The Curvature Operator*, proved from the antisymmetry of the Lie bracket and the connection. The second is the metricity of the connection read on the curvature, $R(X,Y,Z,W) = -R(X,Y,W,Z)$, which follows because $R(X,Y)$ is a skew-adjoint endomorphism of the tangent space for the metric; the skew-adjointness is the identity $\langle R(X,Y)Z,W\rangle = -\langle Z,R(X,Y)W\rangle$, which is the definition of the curvature of the Levi-Civita connection as a metric connection.

### The Pair Symmetry and the Bianchi Identity

**Theorem.** The curvature tensor has the **pair symmetry**

$$
R(X, Y, Z, W) = R(Z, W, X, Y),
$$

and satisfies the **first Bianchi identity**

$$
R(X, Y)Z + R(Y, Z)X + R(Z, X)Y = 0,
$$

equivalently $R(X,Y,Z,W) + R(Y,Z,X,W) + R(Z,X,Y,W) = 0$. The pair symmetry is the statement that the curvature operator $\mathcal{R} : \Lambda^2 T_pM \to \Lambda^2 T_pM$ is self-adjoint for the induced metric on the bivectors, and the Bianchi identity is the statement that the value of $\mathcal{R}$ lies in the kernel of the **Bianchi map** $b : \Lambda^2\otimes\Lambda^2 \to \Lambda^4$.

**Proof.** The pair symmetry is the classical identity of the curvature tensor, proved from the symmetry of the second covariant derivatives or, equivalently, from the fact that the holonomy argument of *The Parallel Transport Operator* makes the curvature the bracket of two connection forms and the pairing symmetric. In the bivector language it is the self-adjointness of $\mathcal{R}$: the identity $\langle\mathcal{R}(\omega),\eta\rangle = \langle\omega,\mathcal{R}(\eta)\rangle$ for the bivectors $\omega = X\wedge Y$ and $\eta = Z\wedge W$ is exactly the pair symmetry. The Bianchi identity is the Jacobi identity of the Lie bracket transported to the curvature, $R(X,Y)Z = [\nabla_X,\nabla_Y]Z - \nabla_{[X,Y]}Z$, together with the vanishing of the curvature of the flat connection of the coordinate frame; the identification with the kernel of the Bianchi map is the definition of the map.

### The Algebraic Curvature Tensors

**Definition.** An **algebraic curvature tensor** at a point is a tensor with the symmetries of the curvature: alternating in each pair, with the pair symmetry, and satisfying the first Bianchi identity. Equivalently, it is a self-adjoint operator $\mathcal{R} : \Lambda^2 \to \Lambda^2$ lying in the kernel of the Bianchi map, $\mathcal{R}\in S^2(\Lambda^2)\cap\ker b$.

**Theorem.** The space of the algebraic curvature tensors is exactly the space $S^2(\Lambda^2)\cap\ker b$ of the self-adjoint operators lying in the kernel of the Bianchi map, and the **Ricci contraction** maps it onto the space of the symmetric two-tensors; the kernel of the contraction is the space of the **Weyl tensors**, and the orthogonal decomposition of the algebraic curvature tensor into the **Ricci part** and the **Weyl part** is the orthogonal decomposition of this space under the action of the orthogonal group. The Bianchi identity is the only linear relation imposed on an otherwise arbitrary self-adjoint operator on the bivectors, so the algebraic curvature tensors are a linear subspace of $S^2(\Lambda^2)$ defined by it.

**Proof sketch.** The symmetries are those of the previous two theorems, which identify the algebraic curvature tensors with the self-adjoint operators satisfying the Bianchi identity; the Ricci contraction is the contraction of the tensor in the first and last arguments and is equivariant for the orthogonal group, its kernel being the trace-free part of the curvature, which is the Weyl tensor; the decomposition follows from the equivariance and the orthogonal splitting of the space of the tensors. The details of the Ricci–Weyl decomposition are in *The Curvature Operator*, *Curvature and Geodesics* and the references.

## The Curvature Operator

### Self-Adjointness

**Theorem.** The curvature operator is self-adjoint for the metric on the bivectors,

$$
\mathcal{R}^{*} = \mathcal{R}, \qquad \langle\mathcal{R}(\omega),\eta\rangle = \langle\omega,\mathcal{R}(\eta)\rangle \quad (\omega,\eta\in\Lambda^2T_pM),
$$

so it is diagonalisable with real eigenvalues and an orthonormal eigenbasis of the bivectors; the eigenvalues are the **principal curvatures** of the curvature operator, and the sectional curvature of a unit bivector is the quadratic form

$$
K(\omega) = \langle\mathcal{R}(\omega), \omega\rangle .
$$

If the operator is positive semidefinite then all the sectional curvatures are nonnegative, and if it is negative semidefinite then they are nonpositive; the converse fails in dimension at least four, where the decomposable bivectors form a proper cone and the curvature operator is a strictly finer invariant than the sectional curvature, as in *The Curvature Operator*. The **Einstein** condition is the statement that the Ricci contraction of $\mathcal{R}$ is a multiple of the metric.

**Proof.** The self-adjointness is the pair symmetry of the previous theorem; a self-adjoint operator on a finite-dimensional inner product space is diagonalisable with real eigenvalues by the spectral theorem; the sectional curvature is the quadratic form by the definition of the curvature operator and the identification of the bivectors. The sign statements follow because a semidefinite quadratic form is nonnegative, respectively nonpositive, on the decomposable cone contained in the whole space; the converse is the dimension count recorded in *The Curvature Operator*. The Einstein condition is the trace statement, developed in the references.

### The Symmetry and the Skew-Symmetry Together

**Proposition.** The two involutions of the curvature are the antisymmetry and the symmetry of the same object seen in the two tensor factors: the antisymmetry is the sign of the exchange of the order inside a factor, and the pair symmetry is the exchange of the two factors. The curvature operator is the same datum as the pair-symmetric, factor-alternating tensor, and the two involutions generate the group of the symmetries of the curvature tensor.

**Proof.** The identification is the equivalence between the tensor $R(X,Y,Z,W)$ and the operator $\mathcal{R}$, with the metric raising and lowering the indices; the antisymmetry is the definition of $\Lambda^2$, and the pair symmetry is the self-adjointness. The group generated by the two involutions is the group of the permutations of the arguments that preserves the curvature identities.

## The Hodge Involution and the Self-Dual Splitting

### The Star Involution on Λ²

**Definition.** On an oriented Riemannian manifold of even dimension $n = 2m$ the **Hodge star** is the operator $\star : \Lambda^k \to \Lambda^{n-k}$ defined by $\alpha\wedge\star\beta = \langle\alpha,\beta\rangle\mathrm{vol}$, and on the bivectors it is an involution up to sign,

$$
\star^2 = (-1)^{k(n-k)}\mathrm{id} = \mathrm{id}\quad\text{on}\ \Lambda^2\ (k=2),
$$

for every even $n$; it is an isometry of the exterior algebra, and it commutes with the metric. In dimension four it is an involution of $\Lambda^2$ onto itself and it splits the bivectors into the **self-dual** and the **anti-self-dual** parts,

$$
\Lambda^2 = \Lambda^2_+\oplus\Lambda^2_-, \qquad \star = +\mathrm{id}\ \text{on}\ \Lambda^2_+, \qquad \star = -\mathrm{id}\ \text{on}\ \Lambda^2_-,
$$

the two eigenspaces of the involution, of dimension three each in the four-dimensional case.

**Proof.** The identity $\star^2 = (-1)^{k(n-k)}$ is the classical computation in an oriented orthonormal basis, and on $\Lambda^2$ in even dimension $(-1)^{2(n-2)} = +1$; the star is an isometry because the pairing defining it is the metric pairing. In dimension four $\star$ maps $\Lambda^2$ to itself and its eigenvalues $\pm1$ have the eigenspaces of dimension $\binom{4}{2}/2 = 3$; the two eigenspaces are the self-dual and the anti-self-dual bivectors.

### The Self-Dual and Anti-Self-Dual Parts

**Theorem.** In dimension four the curvature operator commutes with the Hodge involution exactly when the curvature is **self-dual** or **anti-self-dual** in the appropriate sense; in general the operator splits into the four blocks $\Lambda^2_{\pm}\to\Lambda^2_{\pm}$ and $\Lambda^2_{\pm}\to\Lambda^2_{\mp}$, and the **Weyl tensor** splits into the self-dual and the anti-self-dual parts $W = W_+ + W_-$. A four-manifold is **Einstein** exactly when the two mixed blocks of the curvature operator vanish at every point, and it is **self-dual** (or anti-self-dual) when in addition the corresponding diagonal block of the Weyl part vanishes.

**Proof sketch.** The self-duality and the anti-self-duality are the invariance or the anti-invariance of the curvature under $\star$, which is the vanishing of the mixed blocks of the operator; the Einstein condition reduces the Ricci part to a multiple of the metric and kills the traceless Ricci, which is the vanishing of the mixed blocks; the Weyl splitting is the decomposition of the trace-free part under the star involution. The four-dimensional geometry, the self-dual metrics and the conformal geometry are *Curvature and Geodesics*, *Ricci Flow* and the references.

## The Involution on the Curvature Operator

### Commutation with the Isometric Involution

**Theorem.** Let $\sigma$ be an isometric involution of $(M, g)$, with the conjugation $\mathrm{ad}_\sigma$ on the operator layer of *Isometric Involutions on the Operator Layer*, the preceding article. Then the conjugation acts on the curvature tensor and on the curvature operator by the induced involutions of the tangent space,

$$
\mathrm{ad}_\sigma(R)(X,Y,Z,W) = R(d\sigma X, d\sigma Y, d\sigma Z, d\sigma W), \qquad
\mathrm{ad}_\sigma(\mathcal{R}) = \mathcal{R},
$$

so the curvature operator is a **fixed operator** of the involution, and it commutes with the involution of the bivectors induced by $d\sigma$; the two involutions of the curvature tensor — the skew-symmetry and the pair symmetry — are preserved by $\sigma$, and the Hodge involution is preserved by an orientation-preserving $\sigma$ and conjugated by an orientation-reversing one.

**Proof.** The conjugation by an isometry carries the curvature to the curvature by the naturality of the curvature under an isometry, which is the formula displayed; the curvature operator is therefore fixed under the conjugation, which is the statement of *Isometric Involutions on the Operator Layer*. The symmetry of the curvature is preserved because $\sigma$ is a metric isometry, hence preserves the two involutions of the tensor; the Hodge involution is built from the metric and the orientation, so an orientation-preserving $\sigma$ commutes with it and an orientation-reversing one conjugates it by the sign.

### The Kähler Invariance

**Proposition.** On a Kähler manifold the complex structure is parallel and the curvature operator commutes with the induced involution $J$ on the bivectors: the curvature tensor is $J$-invariant, $R(JX, JY) = R(X, Y)$ as an identity of endomorphisms, and the curvature operator preserves the decomposition of $\Lambda^2\otimes\mathbb{C}$ into the $(+i)$- and $(-i)$-eigenspaces of $J$; the **holomorphic sectional curvature** is the quadratic form of $\mathcal R$ on the bivectors of type $(1,1)$. The Hermitian and Kähler case is *Hermitian Manifolds and the Geodesic Involution* of this category and *Hermitian Geometry and Almost Complex Structures* of a later category.

**Proof.** The complex structure is parallel on a Kähler manifold, so it is a parallel endomorphism of the tangent bundle and it acts on the curvature tensor by the naturality of the curvature; the invariance $R(JX,JY) = R(X,Y)$ follows because $J$ is a parallel isometry of the tangent bundle. The decomposition statement is the spectral decomposition of $J$ on the complexified bivectors, and the holomorphic sectional curvature is the restriction of the quadratic form to the $(1,1)$-bivectors.

## Examples

**Example (the flat space).** In Euclidean space the curvature tensor vanishes, the curvature operator is the zero operator, and both involutions act on the zero tensor; the Bianchi map and the star involution are the algebraic framework in which the vanishing is expressed.

**Example (the space forms).** For a space of constant curvature $\lambda$ the curvature tensor is $R(X,Y,Z,W) = \lambda(\langle X,Z\rangle\langle Y,W\rangle - \langle X,W\rangle\langle Y,Z\rangle)$ and the curvature operator is $\mathcal{R} = \lambda\,\mathrm{id}$ on the bivectors: it is a multiple of the identity, self-adjoint, and it commutes with every involution of the bivectors, including the Hodge star. The sphere and the hyperbolic space have $\lambda>0$ and $\lambda<0$, and the eigenvalues of $\mathcal{R}$ are all $\lambda$.

**Example (the complex projective space).** On $\mathbb{CP}^n$ with the Fubini–Study metric the curvature operator leaves the $(1,1)$-bivectors invariant and the holomorphic sectional curvature is the constant positive value; the curvature is not a multiple of the identity unless $n=1$, and the invariant decomposition of the bivectors into the $(1,1)$ and the $(2,0)+(0,2)$ parts is the one that organises the curvature. In dimension four the real projective space, the complex projective space and the other symmetric spaces exhibit the self-dual and the anti-self-dual splitting of the curvature and the Einstein condition.

## Summary

The curvature tensor carries two **involutions**: the **skew-symmetry**, alternating in each of its two pairs of arguments, which makes it a section of $\Lambda^2\otimes\Lambda^2$, and the **pair symmetry**, the exchange of the two pairs, which is exactly the **self-adjointness** of the curvature operator $\mathcal{R}$ on the bivectors. The **first Bianchi identity** is the additional relation that characterises the curvature among the self-adjoint operators: the curvature tensors are the self-adjoint operators in the kernel of the Bianchi map, $\mathcal R\in S^2(\Lambda^2)\cap\ker b$, and they decompose into the Ricci and the Weyl parts under the orthogonal group.

The curvature operator is self-adjoint, hence diagonalisable with real eigenvalues, and the sectional curvature is its quadratic form $K(\omega) = \langle\mathcal R(\omega),\omega\rangle$: a positive semidefinite operator gives nonnegative sectional curvature and a negative semidefinite one gives nonpositive sectional curvature, the converse failing in dimension at least four, and the Einstein condition is the trace statement. In even dimension the **Hodge star** is an involution of the bivectors, $\star^2=+1$ on $\Lambda^2$, and in dimension four it splits them into the **self-dual** and the **anti-self-dual** parts $\Lambda^2_\pm$; the curvature operator splits into the four blocks, the Einstein condition is the vanishing of the mixed blocks, and the Weyl tensor splits into the self-dual and the anti-self-dual parts. An isometric involution fixes the curvature operator, and the conjugation by $\sigma$ preserves the two symmetries of the curvature and commutes with or conjugates the Hodge involution according to the orientation; on a Kähler manifold the complex structure is a parallel involution whose curvature invariance organises the curvature into the $(1,1)$ and the $(2,0)+(0,2)$ parts.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R(X,Y,Z,W) = \langle R(X,Y)Z,W\rangle$ | Curvature tensor as a four-linear form |
| $R(X,Y,Z,W)=-R(Y,X,Z,W)$, $=-R(X,Y,W,Z)$ | Skew-symmetry: a two-form in each pair |
| $R(X,Y,Z,W)=R(Z,W,X,Y)$ | Pair symmetry: self-adjointness of $\mathcal R$ |
| $R(X,Y)Z+R(Y,Z)X+R(Z,X)Y=0$ | First Bianchi identity |
| $\mathcal{R} : \Lambda^2\to\Lambda^2$, $\mathcal{R}^{*}=\mathcal{R}$ | Self-adjoint curvature operator on the bivectors |
| $K(\omega)=\langle\mathcal{R}(\omega),\omega\rangle$ | Sectional curvature as the quadratic form |
| $b : \Lambda^2\otimes\Lambda^2\to\Lambda^4$ | Bianchi map; curvature tensors in $\ker b$ |
| $\star^2=\mathrm{id}$ on $\Lambda^2$; $\Lambda^2=\Lambda^2_+\oplus\Lambda^2_-$ | Hodge involution; self-dual and anti-self-dual parts |
| $\mathrm{ad}_\sigma(\mathcal R)=\mathcal R$ | The curvature operator is fixed by an isometric involution |
| $R(JX,JY)=R(X,Y)$ | Kähler invariance of the curvature |

## Further Reading

- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume I* (Interscience, 1963), for the curvature tensor, its symmetries and the Bianchi identities.
- Manfredo P. do Carmo, *Riemannian Geometry* (Birkhäuser, 1992), for the curvature tensor, the sectional curvature and the algebraic structure.
- Robert Osserman, "Curvature in the eighties", *American Mathematical Monthly* 97 (1990), 731–756, for the curvature operator, the algebraic curvature tensors and the decomposition of the curvature.
- Arthur L. Besse, *Einstein Manifolds* (Springer, 1987), for the curvature operator, the self-dual and anti-self-dual splitting and the Einstein condition.
- Michael Spivak, *A Comprehensive Introduction to Differential Geometry, Volume 2* (Publish or Perish, 1979), for the symmetries of the curvature tensor and the Bianchi identities.
