# __Riemannian Symmetric Spaces and the Involution__

## Introduction

A symmetric space is a Riemannian manifold in which the geodesic symmetry at every point extends to a global isometry. The local equation $\nabla R = 0$ of the preceding article makes the curvature parallel; the global symmetries make the manifold homogeneous, and a homogeneous space with a symmetry is described by its isometry group and by one **involution** of that group, the conjugation by the symmetry at a point. The involution is the algebraic residue of the geodesic symmetry: its fixed subgroup is the isotropy, its eigenspace decomposition of the Lie algebra is the **Cartan decomposition**, and the curvature is the bracket of the two pieces.

The article develops the involution picture. It proves that a symmetric space is homogeneous, so that it is the quotient $G/K$ of a Lie group of isometries by the isotropy subgroup of a point; it shows that the conjugation by the geodesic symmetry is an involution of $G$ whose fixed subgroup contains $K$, and that the differential of the involution is the Cartan involution of the Lie algebra; it develops the Cartan decomposition $\mathfrak{g} = \mathfrak{k}\oplus\mathfrak{p}$ with the bracket relations $[\mathfrak{k},\mathfrak{k}]\subseteq\mathfrak{k}$, $[\mathfrak{k},\mathfrak{p}]\subseteq\mathfrak{p}$, $[\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{k}$; it proves that the geodesics through the base point are the images of the one-parameter subgroups of $\mathfrak{p}$ and computes the curvature by $R(X,Y)Z = -[[X,Y],Z]$; and it reads the sign of the curvature off the compact, the noncompact and the Euclidean type, with the duality linking the two nondegenerate types.

The article assumes the geodesic symmetry and the locally symmetric spaces of *The Geodesic Symmetry and Locally Symmetric Spaces* and the curvature operator of *The Curvature Operator*, both in this category; the Lie group and the Lie algebra, the exponential map and the homogeneous space are Part III's and are used in the sense of *Smooth Manifolds and Differential Geometry* and of the Lie theory of Part III. The Cartan classification, the rank, the restricted root systems and the duality in its full form are *Symmetric Spaces* of a later category of this Part, and the homogeneous-space constructions are *Homogeneous Spaces* of that category; both are cited rather than developed. The involution itself, its fixed set and its quotient are the subject of the following articles of this category. No physics is invoked.

## The Symmetric Space and Its Isometries

### Homogeneity

Recall that $(M, g)$ is **symmetric** when it is connected and, for every $p$, there is an isometry $\sigma_p$ with $\sigma_p(p) = p$ and $d(\sigma_p)_p = -\mathrm{id}$; then $\sigma_p$ is the geodesic symmetry at $p$, it reverses every geodesic through $p$, and it is an involution.

**Theorem.** A symmetric space is homogeneous: for every pair of points $p, q \in M$ there is an isometry carrying $p$ to $q$. If $p$ and $q$ are joined by a geodesic arc and $m$ is its midpoint, then $\sigma_m(p) = q$.

**Proof.** A symmetric space is complete, since the symmetries extend the geodesics beyond every point, so a pair of points is joined by a geodesic arc $\gamma$ with $\gamma(0) = p$ and $\gamma(1)=q$, by Hopf–Rinow. Let $m = \gamma(1/2)$. The symmetry $\sigma_m$ reverses $\gamma$, so $\sigma_m(\gamma(1)) = \gamma(0)$, that is $\sigma_m(q) = p$, and since $\sigma_m$ is an involution, $\sigma_m(p) = q$. Hence the isometry group acts transitively.

**Corollary.** A symmetric space is the quotient $M = G/K$ of a Lie group $G$ of isometries by the isotropy subgroup $K = G_p$ of a point, and $K$ is compact when $M$ is; the isotropy representation of $K$ on $T_pM$ is the linear isotropy, and it is the representation-theoretic data of the symmetric space. The manifold is the homogeneous space of *Homogeneous Spaces*, with the invariant metric one of whose symmetries is $\sigma_p$.

### The Involution on the Group

**Theorem.** Let $G = \operatorname{Isom}(M, g)^0$ be the identity component of the isometry group and $K = G_p$ the isotropy at $p$. The conjugation by the geodesic symmetry at $p$,

$$
\Phi : G \longrightarrow G, \qquad \Phi(g) = \sigma_p\,g\,\sigma_p,
$$

is an involutive automorphism of $G$ whose fixed subgroup contains the identity component of $K$, and the differential at the identity,

$$
\theta = d\Phi_e : \mathfrak{g} \longrightarrow \mathfrak{g},
$$

is an involutive automorphism of the Lie algebra, the **Cartan involution** of the pair $(G, K)$.

**Proof.** Since $\sigma_p$ is an involutive isometry, conjugation by it is an involutive automorphism of the group of isometries; it preserves $G$ because it is continuous and fixes the identity. If $g \in K$ then $g(p)=p$ and $\sigma_pg\sigma_p(p) = \sigma_pg(p) = \sigma_p(p) = p$, so $\Phi(g)\in K$; hence $\Phi$ preserves $K$ and its fixed subgroup contains the identity component of $K$, with equality when the pair is effective and the space is not of the Euclidean type. The differential of an involutive automorphism is an involutive automorphism of the Lie algebra, which is the definition of $\theta$.

## The Cartan Decomposition

### The Eigenspaces of the Involution

**Theorem.** Let $\theta$ be the Cartan involution of the symmetric pair $(G, K)$. The Lie algebra decomposes as the sum of the eigenspaces of $\theta$,

$$
\mathfrak{g} = \mathfrak{k}\oplus\mathfrak{p}, \qquad
\theta = +\mathrm{id} \ \text{on}\ \mathfrak{k}, \qquad \theta = -\mathrm{id}\ \text{on}\ \mathfrak{p},
$$

where $\mathfrak{k}$ is the Lie algebra of $K$; the decomposition is orthogonal for the Killing form and satisfies

$$
[\mathfrak{k}, \mathfrak{k}] \subseteq \mathfrak{k}, \qquad
[\mathfrak{k}, \mathfrak{p}] \subseteq \mathfrak{p}, \qquad
[\mathfrak{p}, \mathfrak{p}] \subseteq \mathfrak{k} .
$$

The subspace $\mathfrak{p}$ is identified with the tangent space at the base point by the evaluation at the identity of the infinitesimal action, and the isotropy representation of $K$ on $\mathfrak{p}$ is the adjoint action. The decomposition and the bracket relations are the **Cartan decomposition** of the symmetric pair.

**Proof.** An involutive automorphism has the eigenvalues $+1$ and $-1$, and the decomposition is direct; the eigenspaces are orthogonal for the Killing form $B$, because $B(\theta X,\theta Y) = B(X,Y)$ and hence $B(\mathfrak{k},\mathfrak{p}) = B(\theta\mathfrak{k},\mathfrak{p}) = B(\mathfrak{k},-\mathfrak{p}) = -B(\mathfrak{k},\mathfrak{p})$, forcing the vanishing of the pairing when $B$ is nondegenerate. The bracket relations follow from the eigenvalue of $\theta$ on a bracket: $\theta[A,B] = [\theta A,\theta B]$, so the $(-1)$-eigenvalue of $\theta$ on $[A,B]$ is the product of the eigenvalues of $A$ and $B$; this gives the three inclusions by inspecting the signs. The identification of $\mathfrak{p}$ with the tangent space is the orbit map of the homogeneous space, and the adjoint action of $K$ on $\mathfrak{p}$ is the isotropy representation, as in *Homogeneous Spaces*.

### The Geodesics and the Curvature

**Theorem.** Under the identification $\mathfrak{p}\cong T_pM$ the geodesics of the symmetric space through the base point are the curves

$$
t \longmapsto \exp(tX)\cdot p, \qquad X \in \mathfrak{p},
$$

and the curvature is

$$
R(X, Y)Z = -[[X, Y], Z] \qquad (X, Y, Z \in \mathfrak{p}),
$$

with the sectional curvature

$$
K(X, Y) = \frac{\bigl\langle [X, Y],\, [X, Y]\bigr\rangle}{|X|^2|Y|^2 - \langle X, Y\rangle^2}
$$

for the invariant metric whose inner product on $\mathfrak{p}$ is the negative of the Killing form in the compact type and the Killing form in the noncompact type. Consequently the curvature of a symmetric space is parallel, in agreement with $\nabla R=0$, and the algebraic curvature operator is read from the bracket of the two pieces of the Cartan decomposition.

**Proof sketch.** The one-parameter subgroup $t\mapsto\exp(tX)$ is a geodesic of the group with a bi-invariant metric when the metric is the Killing form, and it projects to a geodesic of the quotient through the base point; the geodesic symmetry at the base point reverses it, so the geodesics through the point are exactly these curves. The curvature is computed from the Maurer–Cartan equation: for the canonical connection of a homogeneous space the curvature at the base point is $R(X,Y)Z = -[[X,Y],Z]$ for $X, Y, Z \in \mathfrak{p}$, the components of a bracket of two elements of $\mathfrak{p}$ lying in $\mathfrak{k}$ by the Cartan decomposition. The invariance of the metric makes $[[X,Y],Z]$ skew in $X,Y$ and in $Z$, so this is the curvature tensor of a metric connection, and it is parallel because the brackets are constant on the Lie algebra. The sign of the sectional curvature is computed from the invariance of the inner product: for the negative of the Killing form, $\langle[[X,Y],Y],X\rangle = -\langle[X,Y],[X,Y]\rangle$, so the numerator is $\langle[X,Y],[X,Y]\rangle \geq 0$.

## The Three Types

**Definition.** A symmetric space is of **compact type** if the Killing form is negative definite on $\mathfrak{p}$, equivalently if the isometry group is compact and the space is compact; of **noncompact type** if the Killing form is positive definite on $\mathfrak{p}$, equivalently if the isometry group has no compact factor and the space is simply connected and noncompact; and of **Euclidean type** if the bracket $[\mathfrak{p},\mathfrak{p}]$ vanishes, equivalently if the space is a Euclidean space and the symmetric pair is that of a vector group.

**Theorem.** A symmetric space is the Riemannian product of a flat Euclidean factor, a compact-type factor and a noncompact-type factor, and the sectional curvature is nonnegative on the compact factor, nonpositive on the noncompact factor and zero on the flat factor; the space is of pure type exactly when it is irreducible. The **duality** associates to a symmetric space $G/K$ of noncompact type the dual compact symmetric space $G^{*}/K$ of the same complexified Lie algebra and the opposite Killing form, and the two have the opposite curvature and the same isotropy representation.

**Proof sketch.** The product statement is the de Rham decomposition applied to the invariant metrics, or the corresponding splitting of the Lie algebra into ideals on which the Killing form has a fixed sign; the curvature sign is the previous formula and the sign of the inner product on $\mathfrak{p}$. The duality is the passage to the compact real form of the complexified Lie algebra, which preserves the Cartan decomposition and reverses the sign of the Killing form on $\mathfrak{p}$, hence reverses the curvature; the isotropy representation is the same because the involution and the bracket relations are unchanged. The classification of the irreducible cases is *Symmetric Spaces* of a later category of this Part.

## Examples

**Example (the rank-one spaces).** For the sphere $S^n = \mathrm{SO}(n+1)/\mathrm{SO}(n)$ the involution is $\theta(A) = I_{1,n}A\,I_{1,n}$ with the diagonal matrix of signature $(1,n)$, the space $\mathfrak{p}$ is the set of the matrices with a single nonzero row and column, the geodesics through the base point are the great circles, and the sectional curvature is the constant $+1$. For the hyperbolic space $\mathbb{H}^n = \mathrm{SO}(n,1)^0/\mathrm{SO}(n)$ the same construction with the signature $(n,1)$ gives the constant curvature $-1$. For Euclidean space $\mathbb{R}^n$ the pair is the semidirect product of the translations with $\mathrm{SO}(n)$, the space $\mathfrak{p}$ is the translation part, the bracket vanishes, and the curvature is zero; these are the three rank-one models.

**Example (the Grassmannians).** The Grassmannian $\mathrm{Gr}_k(\mathbb{R}^n) = \mathrm{O}(n)/(\mathrm{O}(k)\times\mathrm{O}(n-k))$ is symmetric, the geodesic symmetry at a subspace $W$ being induced by the reflection $v\mapsto v$ on $W$ and $v\mapsto -v$ on $W^{\perp}$; it is of compact type, of rank $\min(k, n-k)$, and its curvature is computed from the brackets of the corresponding matrices. The complex and the quaternionic Grassmannians and the exceptional spaces are constructed the same way, and their geometry is *Grassmannians and Stiefel Manifolds* and *Symmetric Spaces* elsewhere in this Part.

**Example (the noncompact group manifolds).** The space $\mathrm{SL}(n, \mathbb{R})/\mathrm{SO}(n)$ of the positive definite symmetric matrices of determinant one, with the metric $\operatorname{tr}(H^{-1}dH)^2$, is a symmetric space of noncompact type; the involution is $g\mapsto (g^{-1})^{\top}$, that is $\theta(X) = -X^{\top}$ on the Lie algebra, the Cartan decomposition is the split of a traceless matrix into its antisymmetric part $\mathfrak{k} = \mathfrak{so}(n)$ and its symmetric traceless part $\mathfrak{p}$, and the geodesics through the identity are $t\mapsto e^{tX}$ with $X$ symmetric traceless. The curvature is nonpositive, and the space is the model of the symmetric spaces of noncompact type in the same way that the sphere is the model of the compact ones.

## Summary

A **symmetric space** is a connected Riemannian manifold with, at every point $p$, an involutive isometry $\sigma_p$ fixing $p$ with $d(\sigma_p)_p=-\mathrm{id}$; such a space is complete, and it is **homogeneous**, the symmetry at the midpoint of a geodesic joining $p$ to $q$ carrying $p$ to $q$. It is therefore the quotient $G/K$ of a Lie group of isometries by the isotropy at a point, and the conjugation by $\sigma_p$ is an involutive automorphism of $G$ with fixed subgroup containing the isotropy; its differential is the **Cartan involution** $\theta$ of the pair.

The Cartan involution gives the **Cartan decomposition** $\mathfrak{g}=\mathfrak{k}\oplus\mathfrak{p}$, orthogonal for the Killing form, with $[\mathfrak{k},\mathfrak{k}]\subseteq\mathfrak{k}$, $[\mathfrak{k},\mathfrak{p}]\subseteq\mathfrak{p}$ and $[\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{k}$; the subspace $\mathfrak{p}$ is identified with the tangent space at the base point, the isotropy representation of $K$ on it is the adjoint action, the geodesics through the base point are the images of the one-parameter subgroups of $\mathfrak{p}$, and the curvature is $R(X,Y)Z=-[[X,Y],Z]$ for $X, Y, Z\in\mathfrak{p}$, with the sectional curvature $K(X,Y)=\langle[X,Y],[X,Y]\rangle/|X\wedge Y|^2$. The curvature is parallel, in agreement with the local condition $\nabla R=0$. A symmetric space splits into a flat Euclidean factor, a **compact type** factor of nonnegative curvature and a **noncompact type** factor of nonpositive curvature, the two nondegenerate types being linked by the **duality** that passes to the compact real form and reverses the sign of the curvature while preserving the isotropy representation. The sphere, the hyperbolic space and Euclidean space are the rank-one models; the Grassmannians are the compact classical examples; the space of the positive definite symmetric matrices of determinant one is the noncompact model. The classification, the rank and the restricted roots are *Symmetric Spaces* of a later category of this Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma_p$ | Geodesic symmetry at $p$; involutive isometry with $d\sigma_p=-\mathrm{id}$ |
| $G$, $K=\operatorname{Isom}_p$ | Isometry group and isotropy; symmetric space $M=G/K$ |
| $\Phi(g)=\sigma_pg\sigma_p$ | Involution of $G$ given by conjugation by the symmetry |
| $\theta = d\Phi_e$ | Cartan involution of the Lie algebra |
| $\mathfrak{g}=\mathfrak{k}\oplus\mathfrak{p}$ | Cartan decomposition; $(+1)$ and $(-1)$ eigenspaces of $\theta$ |
| $[\mathfrak{k},\mathfrak{k}]\subseteq\mathfrak{k}$, $[\mathfrak{k},\mathfrak{p}]\subseteq\mathfrak{p}$, $[\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{k}$ | Bracket relations of the decomposition |
| $\mathfrak{p}\cong T_pM$ | Tangent space at the base point |
| $R(X,Y)Z=-[[X,Y],Z]$ | Curvature from the bracket, $X,Y,Z\in\mathfrak{p}$ |
| Compact, noncompact, Euclidean type | Sign of the Killing form on $\mathfrak{p}$; sign of the curvature |
| Duality $G/K \leftrightarrow G^{*}/K$ | Compact real form; opposite curvature, same isotropy representation |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the symmetric space as a homogeneous space, the Cartan involution, the Cartan decomposition and the duality.
- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume II* (Interscience, 1969), for the curvature of a symmetric space and the pair $(G, K)$.
- Séminaire Sophus Lie, *Théorie des algèbres de Lie: Topologie des groupes de Lie* (Secrétariat mathématique, Paris, 1955), for the classification of the symmetric spaces.
- Ottmar Loos, *Symmetric Spaces I: General Theory* (Benjamin, 1969), for the algebraic approach to the symmetric spaces and the involution.
- Arthur L. Besse, *Einstein Manifolds* (Springer, 1987), for the symmetric spaces of compact and noncompact type, their curvature and their classification in the Einstein context.
