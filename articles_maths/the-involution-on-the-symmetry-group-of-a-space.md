
# __The Involution on the Symmetry Group of a Space__

## Introduction

An **involution** of a symmetry group is an automorphism of order two, $\sigma : G \to G$ with $\sigma^2 = \mathrm{id}$, and it is the structure of the group `- * Theory` of this category: the group is read together with an involution on its **elements**. When the group acts on a space, the involution induces a map of the space — the action of $\sigma$ transported through the action — and that induced map is again an involution, an isometry when $\sigma$ preserves the chosen form, whose fixed points are the geometric trace of the group involution. The base point of a symmetric space is the fixed point of the geodesic symmetry, the real points of a complex space are the fixed points of the conjugation, and in each case the fixed set is a totally geodesic subspace of the space the group acts on. The article reads the involution at the group level and follows it to the space.

The article treats the involution on the symmetry group, the induced action on the space, the fixed points of the induced map and the fixed subgroup with its action on the fixed set. The group-level involution, the fixed-point subgroup and the involutive action are *Involutions and the Fixed-Point Subgroup*, *Involutive Groups*, *The Fixed-Point Subgroup of a Continuous Involution* and *Involutive Group Actions on a Space*, in Parts I and II, and are cited, not restated; the homogeneous space and the isotropy representation are *Transformation Groups*; the symmetric space, the symmetric pair, the Cartan involution and the geodesic symmetry are *Riemannian Symmetric Spaces and the Involution*; the fixed-point set of an isometric involution on a Riemannian manifold, its totally geodesic components and the real structures are *Isometric Involutions and the Fixed-Point Set*, *Isometric Involutions and the Two-Fold Quotient of a Riemannian Manifold* and *Real Structures on a Riemannian Manifold*, in *Foundations of Geometry*, and *Hermitian Manifolds and the Geodesic Involution*; the unitary and orthogonal involutions are the previous articles of this group. The **adjoint** of an operator, which the involution defines, is the group `- * Operator Theory` and is not taken here.

The article has five sections: the involution on the symmetry group; the induced action on the space; the fixed points; the fixed subgroup and the coset space; and the worked cases. Throughout, $G$ is a symmetry group of a space $X$ with a chosen distance or form, $\sigma$ an involutive automorphism of $G$ preserving the chosen structure, and $G^{\sigma} = \{g : \sigma(g) = g\}$ the fixed-point subgroup.

## The Involution on a Symmetry Group

### The Involutive Automorphism

**Definition.** An **involution** of the group $G$ is an automorphism $\sigma$ with $\sigma^2 = \mathrm{id}$; its **fixed-point subgroup** is $G^{\sigma} = \{g \in G : \sigma(g) = g\}$, and the pair $(G, \sigma)$ is an **involutive group**. The involution is **inner** when $\sigma = \operatorname{Ad}(h)$ for some $h \in G$, and **central** when $h$ lies in the centre.

**Proposition.** The fixed-point subgroup $G^{\sigma}$ is a subgroup of $G$, closed when $\sigma$ is continuous; the map $g \mapsto g\,\sigma(g)^{-1}$ is a crossed homomorphism whose image is the set of elements reversed by $\sigma$, and the set of elements with $\sigma(g) = g^{-1}$ is the **symmetric set** $\{g : g\sigma(g) = e\}$. The involution is determined by its fixed subgroup together with its action on a complement, and every involution of $G$ gives an involutive action of $G$ on itself, *Involutions and the Fixed-Point Subgroup* and *Involutive Groups*.

**Proof.** The fixed set of an automorphism is a subgroup; the crossed-homomorphism property is $g\sigma(g)^{-1}\cdot \sigma(g)\sigma^2(g)^{-1}$ computed with $\sigma^2 = \mathrm{id}$; the remaining statements are the elementary theory of the Part I articles, cited.

### Examples of Involutions

**Example (the Cartan involution).** For the unitary group $U(p,q)$ the involution $\theta(g) = JgJ^{-1}$ has fixed subgroup $K = U(p)\times U(q)$ and is central when $J$ is central for the pair; it is the Cartan involution, *Unitary Groups and Their Involution*, and its analogue for the orthogonal group is *The Orthogonal Group and the Involutive Automorphism*, the previous article.

**Example (the conjugation of a real structure).** For the complex general linear group with the conjugating involution $\sigma(g) = \overline{g}$ of the matrix entries, the fixed subgroup is $GL_n(\mathbb{R})$, the **real points**; the general theory of the fixed subgroup here is Part I, and the geometric reading is the real forms of *Real Forms of a Complex Lie Group and the Cartan Involution*.

**Example (the grading involution).** For a graded group the grade involution $\alpha(g) = \varepsilon(g)g$ is an involutive automorphism with fixed subgroup the even part $G_0$, *The Signed Sandwich on a Symmetry Group*; it is distinct from the Cartan involution, and the two together generate the Hermitian conjugation of the Clifford algebra there.

**Remark.** An involution is a property of the **elements** of $G$, not of the operators on $G$. The distinction is the whole sense of the group `- * Theory`: the same underlying group carries many involutions, and the involution chosen — the form, the real structure, the grading — is what determines the geometry.

## The Induced Action on the Space

### The Involution on a Homogeneous Space

**Definition.** Let $X = G/K$ be a homogeneous space for the symmetry group $G$, and let $\sigma$ be an involution of $G$ with $\sigma(K) = K$. The **induced involution** on $X$ is

$$
\sigma_X : X \longrightarrow X, \qquad \sigma_X(gK) = \sigma(g)K .
$$

**Proposition.** The induced map $\sigma_X$ is well defined, it is a bijection of $X$ with $\sigma_X^2 = \mathrm{id}$, and it fixes the base point $o = eK$; it is the unique map of $X$ making the projection $G \to G/K$ equivariant for $\sigma$ on the group and $\sigma_X$ on the space. When $X$ carries the chosen form and $\sigma$ preserves it, $\sigma_X$ is an isometry of $X$.

**Proof.** If $gK = g'K$ then $g' = gk$ with $k \in K$, so $\sigma(g') = \sigma(g)\sigma(k) \in \sigma(g)K$ by $\sigma(K) = K$, and the value is well defined; $\sigma_X^2(gK) = \sigma^2(g)K = gK$; the base point is fixed because $\sigma(e) = e$. The equivariance is the definition, and the isometry statement is that $\sigma$ preserves the form, hence carries the isometry group into itself and the orbit metric into itself.

### The Differential at the Base Point

**Proposition.** When $\sigma(K) = K$, the differential of $\sigma_X$ at $o$ is the restriction to $\mathfrak{p} = T_oX$ of $d\sigma$, the differential of the involution at the identity, and $d\sigma$ acts by $+1$ on $\mathfrak{k} = \mathrm{Lie}\,K$ and $-\mathrm{id}$ on $\mathfrak{p}$ when $\sigma$ is a Cartan involution; in general the differential is the linear map induced by $d\sigma$ on the quotient $\mathfrak{g}/\mathfrak{k}$, which is an involution of $\mathfrak{p}$.

**Proof.** The differential of $\sigma_X$ at $o$ is the map induced by $d\sigma$ on $\mathfrak{g}/\mathfrak{k}$; for a Cartan involution the Lie algebra splits into the $\pm1$-eigenspaces $\mathfrak{k}$ and $\mathfrak{p}$, so the induced map is $-\mathrm{id}$ on $\mathfrak{p}$, *Riemannian Symmetric Spaces and the Involution*. This is the sense in which the involution $\sigma$ is the "reflection" of the space at the base point.

## The Fixed Points of the Induced Involution

### The Fixed Set

**Definition.** The **fixed-point set** of the induced involution is

$$
X^{\sigma} = \{x \in X : \sigma_X(x) = x\} = \{gK : g^{-1}\sigma(g) \in K\},
$$

the set of points fixed by $\sigma_X$.

**Theorem (the fixed set is totally geodesic).** Let $X$ be a Riemannian manifold and $\sigma_X$ an involutive isometry. Then each connected component of the fixed-point set $X^{\sigma}$ is a **totally geodesic submanifold** of $X$: a geodesic tangent to $X^{\sigma}$ at a point lies entirely in $X^{\sigma}$, and the component through a fixed point is the geodesic saturation of its tangent space. The map $\sigma_X$ is determined in a neighbourhood of each component by its action on the normal bundle, and the component is the fixed set of the linear involution $d\sigma_X$ on the tangent space at a fixed point.

**Proof.** Let $x \in X^{\sigma}$ and let $\gamma$ be the geodesic with $\gamma(0) = x$ and $\dot\gamma(0) \in T_xX^{\sigma}$. The isometry $\sigma_X$ fixes $x$ and its differential fixes $\dot\gamma(0)$, so $\sigma_X\circ\gamma$ is the geodesic with the same initial point and velocity, hence equals $\gamma$; therefore $\gamma$ lies in $X^{\sigma}$ and $X^{\sigma}$ is totally geodesic. The rest is the exponential map and the linearisation. This is *Isometric Involutions and the Fixed-Point Set*, in *Foundations of Geometry*.

**Corollary.** The fixed set $X^{\sigma}$ is a disjoint union of totally geodesic submanifolds, one through each of its points; at a fixed point $x$ the tangent space $T_xX^{\sigma}$ is the $+1$-eigenspace of $d\sigma_X$ acting on $T_xX$, and the normal space is the $(-1)$-eigenspace.

**Proof.** The tangent space of the fixed set is the fixed space of the differential, a linear involution; the connected component is the image under the exponential map of the fixed subspace, by the theorem, and distinct components correspond to the distinct fixed points modulo the geodesic saturation.

### The Real Points

**Proposition.** Let $X = G/K$ be the complex Grassmannian with the conjugation of a real structure, that is, the involution of $G$ induced by the complex conjugation of the matrix entries. Then the fixed set $X^{\sigma}$ is the **real Grassmannian**, the manifold of real $q$-planes of $\mathbb{R}^{p+q}$, identified with $O(p+q)/(O(p)\times O(q))$, and the inclusion is totally geodesic; the complexification of the fixed set is $X$ itself.

**Proof.** A complex $q$-plane is fixed by the conjugation exactly when it has a basis of real vectors, so the fixed set is the set of real $q$-planes; the real Grassmannian is the compact dual of *The Orthogonal Group and the Involutive Automorphism*, and its inclusion is totally geodesic by the general theorem. This is the geometric content of the real form: the real points of the complex space.

**Remark.** The fixed set is the geometric realisation of the **fixed subgroup**: for the conjugation the fixed subgroup is the real form of the group, and the fixed set of the induced involution is the corresponding real form of the space. The two are the group-level and the space-level readings of the same involution.

## The Fixed Subgroup and the Coset Space

**Proposition.** The fixed subgroup $G^{\sigma}$ acts on the fixed set $X^{\sigma}$, and the action makes each connected component of $X^{\sigma}$ a homogeneous space for the identity component of $G^{\sigma}$. When $X = G/K$ is a symmetric space and $\sigma$ is its Cartan involution, $G^{\sigma} = K$ and the induced map is the **geodesic symmetry** at the base point, $s_o(gK) = \theta(g)K$; conversely every symmetric space arises this way from its Cartan involution, so the symmetric spaces of a symmetry group are exactly the coset spaces of its involutions.

**Proof.** The fixed subgroup preserves the fixed set because $\sigma_X(g\cdot x) = \sigma(g)\cdot\sigma_X(x) = g\cdot x$ for $g \in G^{\sigma}$ and $x \in X^{\sigma}$; for the Cartan involution the fixed subgroup is $K$ by definition and the induced map is $gK \mapsto \theta(g)K = s_o(gK)$; the converse is the general construction of a symmetric space from a symmetric pair, *Riemannian Symmetric Spaces and the Involution*.

**Proposition (the base point and the isolated case).** The base point $o$ is fixed by $\sigma_X$; when $X$ is a symmetric space of noncompact type and $\sigma_X$ is the geodesic symmetry at $o$, the fixed set is the single point $\{o\}$, the exponential map being a diffeomorphism and the geodesic symmetry reversing every geodesic through $o$; for a symmetric space of compact type the fixed set may be larger, and for the round sphere it is the equator.

**Proof.** For a fixed point $y \neq o$ of a geodesic symmetry at $o$, the geodesic $\gamma$ through $o$ and $y$ is reversed by $\sigma_X$, so $\gamma(d)$ maps to $\gamma(-d)$ with $o = \gamma(0)$; a fixed point $y = \gamma(d)$ would need $\gamma(-d) = \gamma(d)$, which forces $d = 0$ in a noncompact symmetric space, where the geodesic is injective. On the round sphere $S^n$ the geodesic symmetry at the pole is the reflection in the equator, whose fixed set is the equator $S^{n-1}$, a totally geodesic hypersurface.

## Worked Cases

**Example (the sphere).** Let $S^n = SO(n+1)/SO(n)$ with the involution $\theta(g) = I_{1,n}gI_{1,n}^{-1}$, $I_{1,n} = \operatorname{diag}(-1,I_n)$; the fixed subgroup is $SO(n)$, the induced map is the reflection in the equator, $\sigma_X(x) = -I_{1,n}x$, and its fixed set is the equator $S^{n-1}$, a totally geodesic submanifold. The equator is the symmetric subspace $SO(n)/SO(n-1)$, and the example shows that the fixed set of an isometric involution can be a whole submanifold.

**Example (the Cartan involution).** Let $X = U(p,q)/(U(p)\times U(q))$ with the Cartan involution $\theta(g) = JgJ^{-1}$; the induced map is the geodesic symmetry $s_o$, the fixed set is the single point $\{o\}$, and the fixed subgroup is $K = U(p)\times U(q)$. The example is the noncompact case, where the geodesic symmetry has the isolated fixed point the symmetric space is built on.

**Example (the complex conjugation).** Let $X = SU(p,q)/S(U(p)\times U(q))$ with the conjugation of a real structure; the fixed set is the real Grassmannian of negative $q$-planes, a totally geodesic submanifold of the complex symmetric space, and the fixed subgroup is the real form $SO(p,q)$ of $SU(p,q)$. The induced involution is the **real structure** of the space, and its fixed set is the real locus.

**Example (an inner involution).** Let $z$ be an element of the centre of the isotropy of a symmetric pair, so that the Cartan involution is $\theta = \operatorname{Ad}(z)$; this is the Hermitian case of *Hermitian Symmetric Spaces and the Group Involution*. The induced involution on $X = G/K$ is then the action of the element $z$ itself, and it is the rotation by $\pi$ in the invariant complex structure: the geodesic symmetry of a Hermitian symmetric space is the action of the central element, so the involution on the elements is realised by a single element of the group, and its fixed set is the base point.

## Summary

An involution of a symmetry group is an automorphism $\sigma$ with $\sigma^2 = \mathrm{id}$ and fixed-point subgroup $G^{\sigma}$; it is the structure of the group `- * Theory`, an involution on the elements of the group. When $G$ acts on a homogeneous space $X = G/K$ and $\sigma(K) = K$, the involution induces a map $\sigma_X(gK) = \sigma(g)K$, which is an involution of $X$, fixes the base point, and is an isometry when $\sigma$ preserves the chosen form; its differential at the base point is the map induced by $d\sigma$ on $\mathfrak{p} = T_oX$, equal to $-\mathrm{id}$ for a Cartan involution. The fixed-point set $X^{\sigma}$ is a union of totally geodesic submanifolds, the $+1$-eigenspace of $d\sigma_X$ giving the tangent space at each fixed point; for the conjugation of a real structure the fixed set is the real Grassmannian, for the Cartan involution of a noncompact symmetric space it is the single base point, and for the round sphere it is the equator. The fixed subgroup $G^{\sigma}$ acts on $X^{\sigma}$, and the symmetric spaces of the group are exactly the coset spaces of its involutions, the geodesic symmetry being $s_o(gK) = \sigma(g)K$; the fixed set of the induced involution is the geometric trace of the involution on the elements. The manifold-level theory of the fixed set is *Isometric Involutions and the Fixed-Point Set*, in *Foundations of Geometry*; no adjoint is taken.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$ | an involution of the symmetry group, $\sigma^2 = \mathrm{id}$ |
| $G^{\sigma}$ | the fixed-point subgroup of the involution |
| $X = G/K$ | the homogeneous space the group acts on |
| $\sigma_X(gK) = \sigma(g)K$ | the induced involution on the space |
| $o = eK$ | the base point, fixed by $\sigma_X$ |
| $X^{\sigma}$ | the fixed-point set; a union of totally geodesic submanifolds |
| $d\sigma_X$ | the differential; $-\mathrm{id}$ on $\mathfrak{p}$ for a Cartan involution |
| $s_o$ | the geodesic symmetry, $s_o(gK) = \theta(g)K$ |
| $\theta(g) = JgJ^{-1}$ | the Cartan involution of a classical group |
| $\overline{g}$ | the conjugation of a real structure; fixed subgroup the real form |
| $\alpha(g) = \varepsilon(g)g$ | the grade involution of a graded group |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the involution of a symmetric pair, the geodesic symmetry and the fixed sets.
- Shoshichi Kobayashi, *Transformation Groups in Differential Geometry* (Springer, 1972), for the fixed-point set of an isometric involution and the totally geodesic components.
- Armand Borel, *Semisimple Groups and Riemannian Symmetric Spaces* (Hindustan Book Agency, 1998), for the correspondence between the involutions of a group and the symmetric spaces.
- Joseph A. Wolf, *Spaces of Constant Curvature* (American Mathematical Society, sixth edition, 2011), for the symmetric spaces, their symmetric subspaces and the fixed sets of the geodesic symmetries.
- Marcel Berger, *A Panoramic View of Riemannian Geometry* (Springer, 2003), for the fixed-point sets of involutions and their role in the geometry of the symmetric spaces.
