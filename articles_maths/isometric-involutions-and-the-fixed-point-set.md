# __Isometric Involutions and the Fixed-Point Set__

## Introduction

An isometric involution is the same thing as its fixed set together with the way it acts transversally to it. The fixed set is a union of **totally geodesic submanifolds**, and at each of its points the involution is the identity along the submanifold and the reflection $-1$ on the normal directions; this is the content of the fixed-set theorem, and it is the reason an involution is called a **mirror** or a **reflection** and its fixed set a **mirror** in the manifold. The article develops the fixed set as an object in its own right: the tube around it, the reflection in a totally geodesic submanifold, the uniqueness of the reflection, the way the fixed set sits inside a symmetric space, and the relation of the fixed set to the two-fold quotient, where it becomes the singular locus.

The article is the second half of the pair formed with *Isometric Involutions and the Two-Fold Quotient of a Riemannian Manifold*: that article divides the manifold by the involution, and this one studies the set that the division marks. It proves that a connected component of the fixed set is a totally geodesic submanifold of codimension equal to the multiplicity of the eigenvalue $-1$ of the differential; it establishes the tube theorem, that the normal exponential map is a diffeomorphism onto a tubular neighbourhood and carries the involution to the reflection of the normal bundle; it defines a **reflective submanifold** as a connected totally geodesic submanifold carrying a reflection, proves that the reflection is unique when it exists and that it is determined by the submanifold, and gives the cases in which the reflection exists; it reads the fixed set of an involution of a symmetric space as a homogeneous totally geodesic submanifold; and it identifies the fixed set with the singular locus of the quotient.

The article assumes the fixed-set theorem and the isometry groups of *Isometries as Operators*, the geodesic symmetry and the locally symmetric spaces of *The Geodesic Symmetry and Locally Symmetric Spaces*, the symmetric spaces and the involution of *Riemannian Symmetric Spaces and the Involution*, and the two-fold quotient of *Isometric Involutions and the Two-Fold Quotient of a Riemannian Manifold*, all in this category; the tube theorem and the normal bundle are Part III's. The real structures are *Real Structures on a Riemannian Manifold*, later in this category, and the reflection groups and the mirrors of a space form are elsewhere in this Part. No physics is invoked.

## The Fixed Set as a Totally Geodesic Submanifold

### The Local Structure

**Definition.** Let $\sigma$ be an isometric involution of a Riemannian manifold $(M, g)$. Its **fixed set** is

$$
\Sigma = \operatorname{Fix}(\sigma) = \{x \in M : \sigma(x) = x\},
$$

a closed subset of $M$, and the **fixed component** of a point $p \in \Sigma$ is the connected component of $\Sigma$ containing $p$.

**Theorem.** Each fixed component is a **totally geodesic** submanifold of $M$: if $x \in \Sigma$ and $v \in T_x\Sigma$, the geodesic of $M$ with $\gamma(0) = x$ and $\gamma'(0) = v$ lies in $\Sigma$.

**Proof.** The tangent space of the fixed component at a fixed point is the fixed subspace $V_+$ of $d\sigma_x$, so $d\sigma_x(v) = v$. The map $t \mapsto \sigma(\gamma(t))$ is then a geodesic, since $\sigma$ is an isometry, and its initial velocity is $d\sigma_x(\gamma'(0)) = v$, so by the uniqueness of the geodesic with a given initial condition it equals $\gamma$; hence $\sigma(\gamma(t)) = \gamma(t)$ for all $t$, the geodesic is fixed by the involution, and it lies in $\Sigma$. A submanifold every one of whose geodesics is a geodesic of the ambient is totally geodesic.

**Corollary.** The fixed set is a disjoint union of connected totally geodesic submanifolds, the manifold is the union of the fixed set and its complement, and the complement is an open set on which the involution acts freely. Every component of the fixed set is closed in $M$, and the components are separated by positive distance on a compact manifold.

### The Normal Bundle and the Normal Exponential

**Definition.** At a point $p$ of the fixed set the tangent space splits as $T_pM = V_+\oplus V_-$ with $V_+ = T_p\Sigma$ and $V_-$ the **normal direction**; the **normal bundle** is $\nu\Sigma$, the union of the $V_-$, and the **normal exponential map** is

$$
\exp^{\perp} : \nu\Sigma \longrightarrow M, \qquad \exp^{\perp}(p, \xi) = \exp_p(\xi).
$$

**Theorem (the tube theorem).** The normal exponential map is a diffeomorphism of a neighbourhood of the zero section of $\nu\Sigma$ onto a tubular neighbourhood of $\Sigma$ in $M$; in the coordinates it defines, the metric splits along $\Sigma$ as

$$
g = g_\Sigma(y) + \sum_a dy^a\,dy^a, \qquad g_\Sigma(y) = g_\Sigma + O(|y|^2),
$$

where $y$ are the normal coordinates and $g_\Sigma$ is the induced metric of $\Sigma$; the involution acts as $\sigma(y, p) = (-y, p)$ in these coordinates, and the geodesics orthogonal to $\Sigma$ are the images of the straight lines of the normal fibres.

**Proof.** The differential of $\exp^\perp$ at the zero section is the identity from $\nu\Sigma$ to the normal bundle of $\Sigma$ in $M$, which is invertible, so the inverse function theorem gives the diffeomorphism onto a tubular neighbourhood; the splitting of the metric is the statement of the Gauss lemma for the geodesics orthogonal to $\Sigma$, and the evenness $g_\Sigma(y) = g_\Sigma(-y) + O(|y|^3)$ along the normal directions is the vanishing of the first-order term because the normal geodesics are orthogonal to $\Sigma$ and $\Sigma$ is totally geodesic. The involution fixes $\Sigma$ pointwise and acts as $-d\sigma = -1$ on the normal directions, so its action in the normal coordinates is $y \mapsto -y$; this is the fixed-set theorem read in the tubular neighbourhood.

## Mirrors and Reflections

### Reflection in a Totally Geodesic Submanifold

**Definition.** A connected totally geodesic submanifold $\Sigma$ of $(M, g)$ is **reflective** if there is an isometric involution $\sigma$ of $M$ whose fixed set contains $\Sigma$ and whose differential is $-\mathrm{id}$ on the normal bundle $\nu\Sigma$; such an involution is a **reflection** in $\Sigma$, and $\Sigma$ is a **mirror**. A point $p$ is a mirror in the trivial sense: the geodesic symmetry at $p$ is a reflection in the zero-dimensional submanifold $\{p\}$.

**Theorem.** A reflection in $\Sigma$, when it exists, is unique, and it is determined by $\Sigma$: the involution fixes $\Sigma$ pointwise and acts as $-\mathrm{id}$ on the normal bundle, and any two isometric involutions with these two properties coincide.

**Proof.** Let $\sigma_1, \sigma_2$ be two such involutions and let $\tau = \sigma_1^{-1}\sigma_2$. Then $\tau$ fixes every point of $\Sigma$, and at a point $p \in \Sigma$ its differential is $d\tau_p = (d\sigma_1)_p^{-1}(d\sigma_2)_p$, which is $\mathrm{id}$ on $V_+$ and $(-\mathrm{id})^{-1}(-\mathrm{id}) = \mathrm{id}$ on $V_-$, hence the identity on $T_pM$. An isometry with a fixed point and identity differential there is the identity on the connected manifold $M$, by the faithfulness of *Isometries as Operators*; hence $\sigma_1=\sigma_2$.

**Proposition.** A reflection in $\Sigma$ commutes with the geodesic symmetries of the points of $\Sigma$ when those exist, and it preserves the normal bundle; conversely a reflection is determined by the involution it induces on the normal bundle, that is by the local action $\xi\mapsto-\xi$. In a space of constant curvature every connected totally geodesic submanifold is reflective, the reflection in a great subsphere of the sphere, in a hyperbolic subspace or in a Euclidean subspace being the restriction of the linear reflection of the ambient model space.

**Proof.** If $\Sigma$ contains $p$ and $\sigma$ is a reflection in $\Sigma$, then at the fixed point $p$ both $\sigma$ and the geodesic symmetry $\sigma_p$ are involutions with differential $-\mathrm{id}$ and both fix $p$; the composition $\sigma\sigma_p$ then fixes $p$ with differential $\mathrm{id}$, so it is constant on the connected component, and the local symmetries therefore commute with the reflection where both are defined. The constant-curvature statement is the reflection of the model space, which is an isometry of the model and fixes its subspace pointwise with the normal action $-1$.

### When a Submanifold is a Mirror

**Theorem.** Let $\Sigma$ be a connected totally geodesic submanifold and let $M$ be simply connected. Then $\Sigma$ is reflective if and only if the normal reflection of the local model, $\exp^\perp(p, \xi)\mapsto\exp^\perp(p, -\xi)$, is a local isometry of $M$ near $\Sigma$; equivalently, if and only if the metric in the normal coordinates is an even function of the normal coordinates along $\Sigma$. This fails in general: there are totally geodesic submanifolds of a Riemannian manifold that are not reflective.

**Proof.** The normal reflection is defined on a tubular neighbourhood of $\Sigma$ by the formula, and it is an isometry there exactly when the metric coefficients are even in the normal coordinates, which is the condition of the tube theorem. If the normal reflection is a local isometry then it extends to a global isometry of the simply connected complete manifold $M$ by the monodromy argument of *The Geodesic Symmetry and Locally Symmetric Spaces*, and it is the reflection. The failure in general is the same as the failure of the local symmetry for a general metric, and the classical counterexamples are the non-symmetric spaces; the details are in the references.

**Corollary.** The fixed set of an isometric involution is the union of its mirrors, and the pair $(\Sigma, \nu\Sigma)$ with the normal reflection is a complete local invariant of the involution near $\Sigma$: two involutions with isometric mirrors and isometric normal bundles with the reflection are locally conjugate.

## The Components and Their Dimensions

**Theorem.** For a fixed component $\Sigma$ and a point $p \in \Sigma$, the codimension of $\Sigma$ near $p$ is the multiplicity of the eigenvalue $-1$ of $d\sigma_p$, and the dimension is the multiplicity of $+1$; the component is a hypersurface exactly when $-1$ has multiplicity one, a point exactly when $d\sigma_p = -\mathrm{id}$, and the whole manifold exactly when $\sigma = \mathrm{id}$.

**Proof.** The tangent space of $\Sigma$ at $p$ is the fixed subspace $V_+$ of $d\sigma_p$, and the differential is an orthogonal involution, so the tangent space has dimension equal to the multiplicity of $+1$ and the normal space the multiplicity of $-1$; the three named cases are the multiplicities $1$, $\dim M$ and $0$.

**Corollary.** The dimension of a fixed component at a point is the multiplicity of the eigenvalue $+1$ of $d\sigma$, and it is constant on the component because the multiplicity of an eigenvalue of a continuously varying family of orthogonal involutions is locally constant.

## The Fixed Set of an Involution of a Symmetric Space

**Theorem.** Let $(M, g)$ be a symmetric space and let $\sigma$ be an isometric involution. Then each fixed component $\Sigma$ is a totally geodesic submanifold, and the subgroup $G^\sigma$ of the isometries of $M$ commuting with $\sigma$ acts transitively on $\Sigma$; consequently $\Sigma$ is a homogeneous totally geodesic submanifold, and it is itself a symmetric space when it is connected and the symmetries of $M$ at its points preserve it.

**Proof sketch.** The fixed set is totally geodesic by the first theorem. For the transitivity, the fixed-point subgroup of the involution in the transitive group of isometries acts on the fixed set: if $p\in\Sigma$ and $q\in\Sigma$, the symmetries of $M$ at the midpoint of a geodesic from $p$ to $q$ can be used, or the fixed-point subgroup is transitive by the standard theorem on the fixed points of an automorphism of a homogeneous space, which is the "symmetric subgroup" theorem; the details are in *Symmetric Spaces* and in the references. The symmetry of $\Sigma$ at a point is the restriction of the symmetry of $M$ at that point when the symmetry commutes with $\sigma$, which holds in the reductive case; where it does not, the component is a totally geodesic homogeneous submanifold but not necessarily a symmetric space.

**Corollary.** For the geodesic symmetry $\sigma_p$ of a symmetric space, the fixed set is the single point $p$; for the reflection in a totally geodesic submanifold of a space form, the fixed set is that submanifold; for the involution of the pair $(G, K)$ at the identity coset, the fixed set contains the images of the fixed subgroup and is the "symmetric subspace" attached to the involution. The tangent space splitting $V_+\oplus V_-$ is the Cartan decomposition at the fixed point when the involution is the Cartan involution.

## Examples

**Example (the reflection of the Euclidean space).** The reflection of $\mathbb{R}^n$ in a hyperplane has the hyperplane as its fixed set, of codimension one; the reflection in a subspace of dimension $k$ has that subspace as fixed set, of codimension $n-k$; and the central symmetry $x\mapsto -x$ has the point $0$ as fixed set, the zero-dimensional mirror. These are the three cases of the dimension theorem.

**Example (the fixed set of the antipodal map).** The antipodal map of the sphere has no fixed point, so its fixed set is empty and it is a free involution; the fixed set of the reflection in a great subsphere is that subsphere; the fixed set of the reflection in a great hypersphere is the hypersphere, and the fixed set of the reflection in a great circle of $S^3$ is that circle. The mirrors of the sphere are exactly the great subspheres, which are the totally geodesic submanifolds.

**Example (the symmetric square).** On the product $M\times M$ the exchange involution has the diagonal $\Delta = \{(x,x)\}$ as its fixed set, a totally geodesic submanifold isometric to $M$ and of codimension $\dim M$; the quotient is the symmetric square and the diagonal is the singular locus. On a product $M_1\times \mathsf{M}_2$ with a reflection $\sigma_1$ of the first factor, the fixed set is $\Sigma_1\times \mathsf{M}_2$ and the involution is $\sigma_1\times\mathrm{id}$; the fixed set of a product involution is the product of the fixed sets.

## Summary

The **fixed set** $\Sigma$ of an isometric involution $\sigma$ is a disjoint union of **totally geodesic submanifolds**: a geodesic with initial velocity in the fixed subspace $V_+$ of $d\sigma_p$ is fixed by the involution and therefore lies in $\Sigma$. At a fixed point the tangent space splits as $V_+\oplus V_-$ into the fixed and the normal directions, the differential being $+\mathrm{id}$ and $-\mathrm{id}$ on the two, and the codimension of the component is the multiplicity of $-1$. The **tube theorem** makes the normal exponential map a diffeomorphism onto a tubular neighbourhood and gives the metric the form $g = g_\Sigma(y)+\sum dy^a dy^a$ with $g_\Sigma(y) = g_\Sigma+O(|y|^2)$, the involution acting as $y\mapsto -y$.

A connected totally geodesic submanifold carrying a reflection is a **mirror** or **reflective** submanifold; the reflection, when it exists, is unique and determined by the submanifold, and it exists exactly when the normal reflection of the local model is a local isometry, equivalently when the metric is even in the normal coordinates. In a space of constant curvature every totally geodesic submanifold is a mirror, the mirror of a point being the geodesic symmetry and the mirror of a hypersphere being the reflection; in a general manifold there are totally geodesic submanifolds that are not mirrors. For a symmetric space the fixed components of an isometric involution are homogeneous totally geodesic submanifolds, acted on transitively by the isometries commuting with the involution, and the splitting $V_+\oplus V_-$ is the Cartan decomposition when the involution is the Cartan involution. The fixed set is the singular locus of the two-fold quotient, and on the complement the involution acts freely.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$, $\sigma^2=\mathrm{id}$ | Isometric involution |
| $\Sigma = \operatorname{Fix}(\sigma)$ | Fixed set; disjoint union of totally geodesic submanifolds |
| $V_+ = T_p\Sigma$, $V_-$ | Fixed and normal directions; $d\sigma_p = +\mathrm{id}$, $-\mathrm{id}$ |
| $\nu\Sigma$, $\exp^\perp$ | Normal bundle and the normal exponential map |
| $g = g_\Sigma(y)+\sum_a dy^ady^a$ | Metric in the normal coordinates of the tube |
| $\sigma(y,p) = (-y,p)$ | The involution as the reflection of the normal coordinates |
| Reflective submanifold, mirror | Totally geodesic submanifold carrying a reflection |
| Codimension $=$ multiplicity of $-1$ | Dimension of the component $=$ multiplicity of $+1$ |
| $G^\sigma$ | Isometries commuting with the involution; transitive on $\Sigma$ when $M$ is symmetric |

## Further Reading

- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume I* (Interscience, 1963), for the totally geodesic submanifolds and the fixed sets of isometries.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the fixed sets of the automorphisms of a symmetric space and the symmetric subgroups.
- Bang-Yen Chen and Tadashi Nagano, "Totally geodesic submanifolds of symmetric spaces", *Duke Mathematical Journal* (1977), for the classification of the reflective submanifolds.
- Shoshichi Kobayashi, *Transformation Groups in Differential Geometry* (Springer, 1972), for the fixed-point sets of the transformation groups and the fixed-point subgroup.
