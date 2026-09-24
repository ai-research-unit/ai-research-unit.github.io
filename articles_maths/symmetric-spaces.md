
# __Symmetric Spaces__

## Introduction

A **symmetric space** is a Riemannian manifold in which every point is the isolated fixed point of an involutive isometry: from each point the space can be reflected, and the reflection is an isometry of the whole space. The plane, the sphere, the hyperbolic plane, every Grassmannian, the space of positive definite matrices, the projective spaces over the four division algebras and the group manifolds of compact Lie groups all have this property, and the class is exactly the class of the **locally symmetric** manifolds — the manifolds with $\nabla R = 0$, the curvature tensor parallel. Symmetry is the geometric case of an algebraic condition on the Lie algebra of the isometry group, and this is what makes the theory complete: Élie Cartan classified the symmetric spaces by classifying the symmetric pairs of semisimple Lie algebras, and the classification is finite and explicit.

Symmetric spaces are the meeting point of three theories. In geometry they are the homogeneous spaces whose curvature has a sign and whose isotropy is a symmetric pair; in Lie theory they are the quotients of a semisimple Lie group by the fixed group of an involution; and in analysis they are the symmetric spaces on which the harmonic analysis, the spherical functions and the invariant differential operators live. They are also the ambient spaces of the classification of the Riemannian holonomy groups: the irreducible simply connected Riemannian manifolds that are not locally symmetric have restricted holonomy in a short list, while the symmetric ones carry the holonomy of their isotropy representation, and the Hermitian, Kähler and quaternionic symmetric spaces are the boundary of this article with *Kähler Geometry*, *Hermitian Geometry and Almost Complex Structures* and *Quaternionic Geometry*, written in parallel.

This article defines symmetric spaces by the geodesic symmetry, proves the equivalence of the three characterisations (involutive isometry at each point, $\nabla R = 0$, the symmetric pair condition), and develops the Cartan theory: the decomposition $\mathfrak{g} = \mathfrak{h}\oplus\mathfrak{m}$ with $[\mathfrak{m},\mathfrak{m}]\subseteq\mathfrak{h}$; the curvature formula $R(X,Y)Z = -[[X,Y],Z]$ and the sign of the curvature in the two types; the Cartan duality; the rank, the flats and the restricted root system; Cartan's theorem that the exponential map of $\mathfrak{m}$ is a diffeomorphism for the noncompact type, so a noncompact symmetric space is a solvable-group parametrisation; the classification of the irreducible symmetric spaces in the four infinite families and the exceptional list; the rank-one spaces; and the relation to the holonomy and to the locally symmetric spaces. The examples are read off from *Grassmannians and Stiefel Manifolds*, *Homogeneous Spaces*, *Spherical Geometry*, *Hyperbolic Geometry* and *Pseudo-Riemannian and Lorentzian Geometry*.

The article assumes *Smooth Manifolds and Differential Geometry* for manifolds; *Homogeneous Spaces* for the quotient manifold theorem, invariant metrics, the canonical connection and the isotropy representation; *Riemannian Geometry* and *Curvature and Geodesics* for the geodesics, the curvature, the Jacobi equation and the holonomy; *Fibre Bundles, Connections and Curvature* for the parallel transport and the curvature form; the Lie theory of *Lie Groups*, *The Lie Algebra and the Exponential Map*, *The Lie Correspondence and the Adjoint Representation* and *Matrix Groups and Classical Groups*, cited and not re-derived; and the quadratic form theory of *Bilinear Forms* and *Isometries and Orthogonal Transformations* for the symmetric bilinear forms and the Cartan involution. The analysis of the invariant differential operators and the spherical functions is Part III's; the harmonic analysis on a symmetric space is cited rather than developed. No physics is invoked.

## The Geodesic Symmetry

### Definition and the Basic Example

**Definition.** A Riemannian manifold $(M, g)$ is **symmetric** at $p \in M$ if there is an isometry $\sigma_p : M \to M$ with $\sigma_p(p) = p$ and $d\sigma_p|_p = -\mathrm{id}_{T_pM}$. The isometry $\sigma_p$ is the **geodesic symmetry** at $p$. The manifold is a **symmetric space** if it is connected and symmetric at every point.

**Proposition.** The geodesic symmetry, when it exists, is unique, is an involution, and reverses every geodesic through $p$: if $\gamma$ is a geodesic with $\gamma(0) = p$ then $\sigma_p(\gamma(t)) = \gamma(-t)$.

**Proof.** An isometry is determined by its value and its differential at one point, so $d\sigma_p = -\mathrm{id}$ determines $\sigma_p$; then $d(\sigma_p^2)|_p = \mathrm{id}$, so $\sigma_p^2$ is an isometry with identity differential at $p$, hence the identity on the connected manifold $M$; and the curve $t \mapsto \sigma_p(\gamma(-t))$ is a geodesic with the same initial point and velocity as $\gamma$, so it equals $\gamma$ by uniqueness of geodesics. $\square$

**Example (the elementary cases).** The Euclidean space $\mathbb{R}^n$ is symmetric at each point with $\sigma_p(x) = 2p - x$, the point reflection. The round sphere $S^n$ is symmetric with $\sigma_p$ the restriction of the reflection of $\mathbb{R}^{n+1}$ in the line through $p$ and the origin. The hyperbolic space $\mathbb{H}^n$ is symmetric with $\sigma_p$ the reflection of the hyperboloid model in the line through $p$, an element of $O(1,n)^+$. In each of the three model geometries the reflection in a point is an isometry, which is the geometric form of the fact that the three constant-curvature geometries are symmetric.

### Equivalence of the Characterisations

**Theorem.** For a connected Riemannian manifold $(M, g)$ the following are equivalent:

**(a)** $(M, g)$ is a symmetric space;

**(b)** the curvature tensor is parallel, $\nabla R = 0$;

**(c)** $(M, g)$ is locally symmetric: for every $p$ there is a neighbourhood with a geodesic symmetry, equivalently the geodesic symmetry at $p$ is defined on a neighbourhood of $p$ and is an isometry there.

Moreover, a simply connected locally symmetric space is symmetric.

**Proof sketch.** (a) $\Rightarrow$ (b): the symmetry $\sigma_p$ is an isometry, so it preserves $\nabla$ and $R$; at $p$ it acts on tensors by the differential $-\mathrm{id}$, which acts on a tensor of type $(0, r)$ by $(-1)^r$ up to signs, and the transported curvature at $p$ equals the curvature at $p$, giving $\nabla R = 0$ after differentiating the equivariance relation along geodesics. (b) $\Rightarrow$ (c): the geodesic symmetry is constructed by reversing geodesics along a normal neighbourhood, and $\nabla R = 0$ is what makes the reversal an isometry; the construction is the Cartan local symmetry. (c) $\Rightarrow$ (a) on a simply connected manifold: the local symmetries can be continued along curves, and simple connectivity makes the continuation path-independent, so the local symmetry at $p$ extends globally. $\square$

**Corollary.** A symmetric space is complete, homogeneous and a homogeneous space of its isometry group; the isometry group acts transitively, because for $p, q$ the composition of the symmetries and the geodesic flow carries $p$ to $q$.

**Proof.** The geodesic symmetry at $p$ is defined everywhere, so the exponential map at $p$ is defined everywhere and $M$ is complete; then every $q$ lies on a geodesic from $p$, and along a geodesic the symmetry and the parallel transport generate a one-parameter family of isometries moving $p$ to $q$. $\square$

## The Symmetric Pair

### The Lie Algebra Decomposition

**Definition.** A **symmetric pair** is a pair $(\mathfrak{g}, \sigma)$ with $\mathfrak{g}$ a Lie algebra and $\sigma$ an involutive automorphism of $\mathfrak{g}$. Writing $\mathfrak{h}$ and $\mathfrak{m}$ for the $+1$- and $-1$-eigenspaces of $\sigma$, one has

$$
\mathfrak{g} = \mathfrak{h}\oplus\mathfrak{m}, \qquad [\mathfrak{h},\mathfrak{h}]\subseteq\mathfrak{h}, \qquad [\mathfrak{h},\mathfrak{m}]\subseteq\mathfrak{m}, \qquad [\mathfrak{m},\mathfrak{m}]\subseteq\mathfrak{h}.
$$

The subalgebra $\mathfrak{h}$ is the **isotropy algebra** and $\mathfrak{m}$ the **isotropy complement**; the last inclusion is the algebraic form of symmetry.

**Theorem.** Let $(M, g)$ be a symmetric space, $G = \operatorname{Isom}(M,g)_0$ the identity component of its isometry group, $H$ the stabiliser of a point $o$, and $\sigma$ the differential at $o$ of the geodesic symmetry, acting on $\mathfrak{g} = \operatorname{Lie}(G)$. Then $\sigma$ is an involutive automorphism of $\mathfrak{g}$, the pair $(\mathfrak{g}, \sigma)$ is a symmetric pair, $\mathfrak{h} = \operatorname{Lie}(H)$ is the $+1$-eigenspace, the isotropy complement $\mathfrak{m}$ is identified with $T_oM$, and the isotropy representation of $H$ on $T_oM$ is the adjoint action of $H$ on $\mathfrak{m}$.

**Proof sketch.** The conjugation by the geodesic symmetry is an automorphism of $G$ whose differential is $\sigma$; it fixes $H$ pointwise, so $\mathfrak{h}$ is the $+1$-eigenspace; and the isotropy representation is the derivative of the action of $H$ at the fixed point $o$, which is the adjoint action on the complement. $\square$

**Corollary.** The tangent bundle of a symmetric space satisfies $TM = G\times_H\mathfrak{m}$, and the curvature tensor is $G$-invariant, corresponding to the $\operatorname{Ad}(H)$-invariant tensor on $\mathfrak{m}$.

### The Curvature

**Theorem.** On a symmetric space, with $\mathfrak{g} = \mathfrak{h}\oplus\mathfrak{m}$ the symmetric pair and the metric induced from an $\operatorname{Ad}(G)$-invariant inner product on $\mathfrak{g}$, the Riemann curvature tensor at $o$ is, for $X, Y, Z \in \mathfrak{m}$,

$$
R(X, Y)Z = -[[X, Y], Z], \qquad \text{and hence} \qquad K(X\wedge Y) = \bigl\|[X, Y]\bigr\|^2 \geq 0
$$

for the compact type, with the opposite sign

$$
R(X, Y)Z = [[X, Y], Z], \qquad K(X\wedge Y) = -\bigl\|[X,Y]\bigr\|^2 \leq 0
$$

for the noncompact type, where the bracket is that of $\mathfrak{g}$ and $\|[X,Y]\|$ is computed in the invariant inner product.

**Proof sketch.** For the compact type, the geodesic symmetry argument gives the formula $R(X,Y)Z = -[[X,Y],Z]$ (the curvature of a symmetric space with the canonical connection, which is the Levi-Civita connection), and the contraction with the invariant inner product, using the identity $\langle[[X,Y],Y],X\rangle = -\|[X,Y]\|^2$ that follows from $\operatorname{Ad}$-invariance, gives the sectional curvature. The noncompact type is the sign reversal of the duality, explained below. $\square$

**Corollary (constancy of the curvature invariants).** On a symmetric space the curvature tensor, the Ricci tensor and the scalar curvature are parallel; the Ricci tensor is a multiple of the restriction to $\mathfrak{m}$ of the Killing form of $\mathfrak{g}$, with the sign of the type, and the space is Einstein precisely when the isotropy representation is irreducible, by Schur's lemma applied to the invariant bilinear form $\mathrm{Ric}$.

**Example (the four families of rank-one).** The compact rank-one symmetric spaces are $S^n = SO(n+1)/SO(n)$ and $\mathbb{RP}^n = S^n/\{\pm1\}$ of constant curvature $+1$; the complex projective spaces $\mathbb{CP}^m = S^{2m+1}/S^1 = SU(m+1)/S(U(m)\times U(1))$ of real dimension $2m$; the quaternionic projective spaces $\mathbb{HP}^m = S^{4m+3}/Sp(1) = Sp(m+1)/(Sp(m)\times Sp(1))$ of real dimension $4m$; and the Cayley projective plane $\mathbb{OP}^2 = F_4/\mathrm{Spin}(9)$ of dimension $16$. Their curvature is positive but, except in the real case, not constant, and together with the four hyperbolic spaces they are the simply connected symmetric spaces of rank one. The Cayley plane is the only one not obtained from an associative division algebra, and its geometry is that of the octonions.

## The Two Types and Cartan Duality

### Compact and Noncompact Type

**Definition.** A symmetric space $M = G/H$ is of **compact type** if $G$ is compact and the Ricci curvature is nonnegative (indeed $M$ has nonnegative sectional curvature); it is of **noncompact type** if it is simply connected, has nonpositive sectional curvature, and is not a product with a Euclidean factor; it is **of Euclidean type** if it is flat, hence a quotient of $\mathbb{R}^n$ by a discrete group of translations. The **Cartan duality** assigns to a symmetric pair of noncompact type its **compact dual**, obtained by replacing the isotropy complement $\mathfrak{m}$ by $i\mathfrak{m}$ in the complexification, which yields a symmetric pair of compact type with the same isotropy algebra.

**Theorem (Cartan).** Every symmetric space whose isometry group is semisimple decomposes uniquely as a Riemannian product

$$
M = M_c \times M_n \times M_e
$$

of a compact-type factor, a noncompact-type factor and a Euclidean factor; the decomposition is orthogonal in the metric and the factors are the images of the distinct types of simple ideals in the symmetric pair.

**Proof sketch.** The Killing form of a semisimple Lie algebra is negative definite on a compact form and splits the simple factors into the compact and the noncompact ones; the Euclidean factor is the centre, and the product structure is the decomposition into the corresponding $G$-invariant distributions. $\square$

**Example.** The compact duals: the sphere is dual to the hyperbolic space, $\mathbb{CP}^m$ to $\mathbb{CH}^m$, $\mathbb{HP}^m$ to $\mathbb{HH}^m$, and $\mathrm{Gr}_k(\mathbb{R}^n) = O(n)/(O(k)\times O(n-k))$ to the noncompact Grassmannian $O(k,n-k)/(O(k)\times O(n-k))$ of positive definite $k$-planes in a form of signature $(k, n-k)$. The duality exchanges the sign of the curvature and the type of the exponential map: on a noncompact space the exponential map is a diffeomorphism, while on the compact dual it is not injective.

### Cartan's Theorem and the Flats

**Theorem (Cartan).** Let $M = G/H$ be a symmetric space of noncompact type, with $\mathfrak{g} = \mathfrak{h}\oplus\mathfrak{m}$ and the Cartan involution $\sigma$. Then the map

$$
\exp : \mathfrak{m} \longrightarrow M, \qquad \exp(X) = \exp_G(X)\cdot o,
$$

is a diffeomorphism; consequently $M$ is diffeomorphic to a Euclidean space, and the exponential map of the metric coincides with the group exponential along $\mathfrak{m}$.

**Proof sketch.** The differential of $\exp$ at $0$ is the identity, and the computation of its differential elsewhere, using the Jacobi equation for the geodesics of a space of nonpositive curvature, gives that it is everywhere nonsingular; injectivity follows from the nonpositivity of the curvature and the absence of conjugate points on a simply connected manifold of nonpositive curvature (Cartan–Hadamard). $\square$

**Definition.** A **flat** of a symmetric space is a totally geodesic submanifold of vanishing curvature; a **maximal flat** is one of the largest dimension. The **rank** of a symmetric space is the dimension of a maximal flat, equal to the dimension of a maximal abelian subspace of $\mathfrak{m}$. The set of maximal flats is a single orbit of $G$, and the **restricted root system** is the set of nonzero weights of the adjoint action of a maximal abelian subalgebra $\mathfrak{a}\subseteq\mathfrak{m}$ on $\mathfrak{g}$, with the **Weyl group** the finite group generated by the reflections in the root hyperplanes.

**Theorem.** For a symmetric space of compact or noncompact type, every maximal flat is a finite covering of the image of $\exp(\mathfrak{a})$; the rank is at least one, and it is one exactly for the spaces of constant curvature and the projective spaces over $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ and $\mathbb{O}$. Each geodesic lies in a maximal flat, so the geometry of the space is the geometry of its flats glued along the restricted root hyperplanes.

**Proof sketch.** The bracket condition $[\mathfrak{a},\mathfrak{a}] = 0$ with $\mathfrak{a}\subseteq\mathfrak{m}$ makes $\exp(\mathfrak{a})$ totally geodesic and flat; maximality is the maximality of the abelian subspace; and each geodesic direction lies in a maximal abelian subspace by the standard extension argument. $\square$

**Example (the rank of the Grassmannians).** The rank of $\mathrm{Gr}_k(\mathbb{R}^n)$ is $\min(k, n-k)$, of $\mathrm{Gr}_k(\mathbb{C}^n)$ the same, and of the hyperbolic space $\mathbb{H}^n$ it is one; the rank-one symmetric spaces are precisely the spaces of the previous section, and they are the spaces whose curvature has one sign in each two-plane and whose geodesics are all conjugate.

## The Classification

### The Symmetric Pairs

**Theorem (Cartan's classification).** The irreducible symmetric spaces, up to finite covering and up to the type, are classified by the irreducible symmetric pairs $(\mathfrak{g}, \sigma)$ of real semisimple Lie algebras, equivalently by the classification of the real semisimple Lie algebras together with an involution. In the compact type the classical families are the following:

| Type | Compact symmetric space | Isotropy algebra |
|---|---|---|
| A I | $SU(n)/SO(n)$ | $\mathfrak{so}(n)$ |
| A II | $SU(2n)/Sp(n)$ | $\mathfrak{sp}(n)$ |
| A III | $SU(p+q)/S(U(p)\times U(q))$ | $\mathfrak{su}(p)\oplus\mathfrak{su}(q)\oplus\mathfrak{u}(1)$ |
| B I, D I | $SO(p+q)/(SO(p)\times SO(q))$ | $\mathfrak{so}(p)\oplus\mathfrak{so}(q)$ |
| C I | $Sp(n)/U(n)$ | $\mathfrak{u}(n)$ |
| C II | $Sp(p+q)/(Sp(p)\times Sp(q))$ | $\mathfrak{sp}(p)\oplus\mathfrak{sp}(q)$ |
| D III | $SO(2n)/U(n)$ | $\mathfrak{u}(n)$ |

and the exceptional entries, in the Cartan notation, are

| Type | Compact symmetric space | Type | Compact symmetric space |
|---|---|---|---|
| E I | $E_6/Sp(4)$ | E VI | $E_7/(\mathrm{Spin}(12)\cdot SU(2))$ |
| E II | $E_6/(SU(6)\cdot SU(2))$ | E VII | $E_7/(E_6\cdot SO(2))$ |
| E III | $E_6/(\mathrm{Spin}(10)\cdot SO(2))$ | E VIII | $E_8/SO(16)$ |
| E IV | $E_6/F_4$ | E IX | $E_8/(E_7\cdot SU(2))$ |
| E V | $E_7/(SU(8)/\mathbb{Z}_2)$ | F I, F II | $F_4/(Sp(3)\cdot SU(2))$, $F_4/\mathrm{Spin}(9)$ |

together with the single entry $G_2/SO(4)$; each compact entry has a noncompact dual obtained by the Cartan duality.

**Proof sketch.** The classification reduces to the classification of the real simple Lie algebras with an involution, equivalently to the classification of the real forms and of the maximal compact subalgebras, which is Cartan's classification of the real semisimple Lie algebras together with the theory of the restricted root systems; the list is finite because the Dynkin diagrams are classified. The excluded cases are the products of irreducible factors, the flat Euclidean factor and the centre. $\square$

**Remark.** The list has four classical infinite families — the Grassmannians over $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ and the symplectic Lagrangian Grassmannians — and the exceptional entries of the $E_6$, $E_7$, $E_8$, $F_4$ and $G_2$ types, whose complexifications are the exceptional simple Lie algebras. The projective planes over the four division algebras appear as the rank-one members of the families: $\mathbb{CP}^m$ in $A$ III, $\mathbb{HP}^m$ in $C$ I, the real projective plane in $B$ I, and the Cayley plane $\mathbb{OP}^2 = F_4/\mathrm{Spin}(9)$ in the exceptional list. The structure of the division algebra, and the three two-dimensional algebras of *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*, is what organises the first three of these.

### The Hermitian Symmetric Spaces

**Definition.** A symmetric space is **Hermitian** (or is of **Hermitian type**) if it carries a $G$-invariant almost complex structure $J$ compatible with the metric and parallel for the Levi-Civita connection; equivalently, if the isotropy representation of a maximal compact subgroup has a central circle factor acting by an almost complex structure.

**Theorem.** A symmetric space is Hermitian if and only if its isotropy algebra $\mathfrak{h}$ has a one-dimensional central factor; equivalently, if the symmetric space is a Kähler manifold. The irreducible Hermitian symmetric spaces are exactly the symmetric spaces in which the isotropy representation is not irreducible but is a sum of two irreducible complex pieces; they are the four families of bounded symmetric domains in the noncompact case and of projective or Grassmannian varieties in the compact case, together with the two exceptional domains in dimensions $16$ and $27$.

**Proof sketch.** The invariant almost complex structure exists precisely when the isotropy representation admits a central circle, since an invariant complex structure is a $J$ commuting with the isotropy action; the metric compatibility and the parallel condition are automatic for a symmetric space, and the integrability follows from the closedness of the Kähler form, which is the obstruction computed from the bracket. The classification is the case $K_M$ in the Cartan list. $\square$

**Remark.** The complex structure $J$ and the complex geometry of the Hermitian symmetric spaces — the Bergman metric, the Harish-Chandra embedding of the bounded domain, the tube domains and the Shilov boundary — are the subject of *Kähler Geometry* and *Hermitian Geometry and Almost Complex Structures*, written in parallel, and of the analysis of Part III. This article supplies only the symmetric-space structure: the involutive isometry, the symmetric pair, the parallel curvature and the classification.

### Locally Symmetric Spaces and Holonomy

**Definition.** A Riemannian manifold is **locally symmetric** if it is locally isometric to a symmetric space; equivalently, by the theorem of the first section, if $\nabla R = 0$. A **locally symmetric space** is the quotient of a symmetric space by a discrete group of isometries acting freely and properly discontinuously.

**Theorem (Cartan–Ambrose–Hicks).** Let $M$ and $N$ be complete simply connected Riemannian manifolds and let $F : T_pM \to T_qN$ be a linear isometry. Then $F$ is the differential of an isometry $M \to N$ if and only if $F$ intertwines the curvature tensors and all their covariant derivatives. In particular a complete simply connected manifold is symmetric if and only if $\nabla R = 0$, and its isometry group is determined by the curvature tensor at a single point.

**Proof sketch.** Necessity is the naturality of the curvature under isometries; sufficiency constructs the isometry by parallel transport along geodesics and applies the Cartan lemma, the curvature condition being exactly what makes the construction independent of the path. $\square$

**Corollary (local structure and holonomy).** A complete manifold is locally symmetric if and only if its curvature tensor is parallel, equivalently if the holonomy group of the Levi-Civita connection at a point fixes the curvature tensor at that point; its universal cover is then a symmetric space, and the locally symmetric space is the quotient of that symmetric space by a discrete group of isometries acting freely and properly discontinuously.

**Corollary (the holonomy classification).** The irreducible simply connected Riemannian manifolds that are not locally symmetric have restricted holonomy one of

$$
SO(n), \quad U(n), \quad SU(n), \quad Sp(n), \quad Sp(n)\cdot Sp(1), \quad G_2, \quad \mathrm{Spin}(7) ,
$$

by the Berger classification of the holonomy groups; the locally symmetric manifolds are the remaining equality cases, in which the holonomy is the compact part of the isotropy representation of the symmetric pair. The special holonomy manifolds themselves — Calabi–Yau, hyperkähler, quaternionic Kähler, $G_2$ and $\mathrm{Spin}(7)$ — are *Kähler Geometry*, *Calabi–Yau Manifolds*, *Quaternionic Geometry*, *$G_2$ and $\mathrm{Spin}(7)$ Manifolds*, written in parallel, and the holonomy classification is cited there.

**Example (locally symmetric but not symmetric).** A compact Riemann surface of genus $g \geq 2$ is locally symmetric of noncompact type — its universal cover is the hyperbolic plane, which is symmetric — but a generic such surface is not itself symmetric: the geodesic symmetries do not descend, and the moduli space of hyperbolic structures has positive dimension. This is the same phenomenon as the failure of Mostow rigidity in dimension two, and it lies outside this article. In dimension at least three the local symmetric structures are rigid, and a finite-volume locally symmetric space of noncompact type is determined by its fundamental group.

## Summary

A symmetric space is a connected Riemannian manifold in which every point is the isolated fixed point of an involutive isometry, the geodesic symmetry. This is equivalent to the parallelism of the curvature, $\nabla R = 0$, and, on a simply connected manifold, to local symmetry; a symmetric space is complete, homogeneous and a quotient of the identity component of its isometry group by the stabiliser of a point. The pair $(\mathfrak{g}, \sigma)$ of the Lie algebra of the isometry group and the differential of the geodesic symmetry is a symmetric pair: with $\mathfrak{g} = \mathfrak{h}\oplus\mathfrak{m}$ the $\pm1$-eigenspaces, the brackets satisfy $[\mathfrak{h},\mathfrak{h}]\subseteq\mathfrak{h}$, $[\mathfrak{h},\mathfrak{m}]\subseteq\mathfrak{m}$ and $[\mathfrak{m},\mathfrak{m}]\subseteq\mathfrak{h}$, and this last inclusion is the algebraic form of symmetry.

The curvature of a symmetric space is computed from the bracket: $R(X,Y)Z = -[[X,Y],Z]$ and $K(X\wedge Y) = \|[X,Y]\|^2$ in the compact type, with the sign reversed in the noncompact type; the curvature tensor, the Ricci tensor and the scalar curvature are parallel, and the space is Einstein exactly when the isotropy representation is irreducible. Every symmetric space splits as a product of a compact-type factor, a noncompact-type factor and a Euclidean factor, and the Cartan duality pairs a noncompact symmetric space with a compact one of the same isotropy algebra and opposite curvature. On the noncompact type the exponential map of the isotropy complement is a diffeomorphism, by Cartan's theorem, so the space is a Euclidean space in exponential coordinates.

The classification of the irreducible symmetric spaces is Cartan's, and reduces to the classification of the irreducible symmetric pairs of real semisimple Lie algebras: four infinite families — the Grassmannians over $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ and the symplectic Lagrangian Grassmannians — and the exceptional entries of the $E_6$, $E_7$, $E_8$, $F_4$ and $G_2$ types. The rank of a symmetric space is the dimension of a maximal flat, equal to the dimension of a maximal abelian subspace of $\mathfrak{m}$; the rank-one spaces are the spaces of constant curvature and the projective planes over the four division algebras. The Hermitian symmetric spaces are those with a parallel invariant complex structure, equivalently those whose isotropy algebra has a central circle; their complex geometry belongs to the Kähler and Hermitian articles written in parallel. A complete manifold is locally symmetric exactly when its curvature is parallel, and the locally symmetric spaces are the quotients of symmetric spaces by free proper discontinuous isometric actions, with the holonomy of the isotropy representation; the classification of the holonomy groups places the symmetric spaces as the equality cases, the remainder being the manifolds of special holonomy.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma_p : M \to M$ | Geodesic symmetry at $p$; $\sigma_p(p)=p$, $d\sigma_p|_p = -\mathrm{id}$ |
| $\nabla R = 0$ | Local symmetry; equivalent to symmetry on a simply connected manifold |
| $(\mathfrak{g}, \sigma)$, $\sigma^2 = \mathrm{id}$ | Symmetric pair; $\sigma$ the Cartan/geodesic involution on the Lie algebra |
| $\mathfrak{g} = \mathfrak{h}\oplus\mathfrak{m}$ | $+1$ and $-1$ eigenspaces; $\mathfrak{h}$ isotropy algebra, $\mathfrak{m}$ isotropy complement |
| $[\mathfrak{h},\mathfrak{h}]\subseteq\mathfrak{h}$, $[\mathfrak{h},\mathfrak{m}]\subseteq\mathfrak{m}$, $[\mathfrak{m},\mathfrak{m}]\subseteq\mathfrak{h}$ | Symmetric pair brackets |
| $R(X,Y)Z = -[[X,Y],Z]$ | Curvature, compact type; sign reversed for noncompact type |
| $K(X\wedge Y) = \|[X,Y]\|^2$ | Sectional curvature, compact type; $\leq 0$ for the dual |
| $\mathrm{Ric}(X,Y) = -\tfrac12\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y)$ | Ricci tensor on $\mathfrak{m}$, compact type |
| $M = M_c\times M_n\times M_e$ | Decomposition into compact, noncompact and Euclidean factors |
| Cartan duality | $\mathfrak{m}\mapsto i\mathfrak{m}$; compact dual, opposite curvature sign |
| $\exp : \mathfrak{m}\to M$ | Diffeomorphism for the noncompact type (Cartan) |
| $\mathfrak{a}\subseteq\mathfrak{m}$, rank, Weyl group | Maximal abelian subspace; dimension of a maximal flat; reflection group |
| Restricted root system | Nonzero weights of $\mathfrak{a}$ on $\mathfrak{g}$ |
| $S^n$, $\mathbb{KP}^m$, $\mathbb{OP}^2$ | Rank-one symmetric spaces of compact type |
| $\mathrm{Gr}_k(\mathbb{R}^n)$, $\mathrm{Gr}_k(\mathbb{C}^n)$ | Symmetric spaces of rank $\min(k,n-k)$ |
| Hermitian symmetric space, $J$ | Parallel invariant almost complex structure; central circle in $\mathfrak{h}$ |
| Locally symmetric space | Complete manifold with $\nabla R=0$; quotient of a symmetric space |
| $\mathrm{Hol}$, special holonomy | Holonomy of the Levi-Civita connection; $U(n)$, $SU(n)$, $Sp(n)$, $G_2$, $\mathrm{Spin}(7)$ |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the equivalence of the characterisations, the symmetric pair and the curvature.
- Ottmar Loos, *Symmetric Spaces I: General Theory* (Benjamin, 1969), for the algebraic theory of symmetric spaces and the Jordan-theoretic approach.
- Élie Cartan, *Œuvres Complètes* (Gauthier-Villars, 1952), for the original classification of the symmetric spaces.
- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume II* (Interscience, 1969), for the curvature formula, the flats and the rank.
- Armand Borel and Jacques Tits, "Groupes réductifs", *Publications Mathématiques de l'IHÉS* 27 (1965), 55–150, for the classification of the symmetric pairs and the restricted root systems.
- Marcel Berger, "Sur les groupes d'holonomie homogène des variétés à connexion affine et des variétés riemanniennes", *Bulletin de la Société Mathématique de France* 83 (1955), 279–330, for the holonomy classification and the place of the symmetric spaces.
- Sigurdur Helgason, *Groups and Geometric Analysis* (Academic Press, 1984), for the invariant differential operators and the spherical functions on a symmetric space.
