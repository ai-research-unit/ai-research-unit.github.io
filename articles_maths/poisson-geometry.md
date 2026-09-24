
# __Poisson Geometry__

## Introduction

A **Poisson manifold** is a smooth manifold whose algebra of smooth functions carries a bracket that is a derivation in each argument and satisfies the Jacobi identity. The bracket is determined by a **bivector field** $\pi$ on the manifold, and the two conditions become the single equation $[\pi, \pi] = 0$ for the Schouten–Nijenhuis bracket. The subject sits between symplectic geometry and the theory of Lie algebras: every symplectic manifold is Poisson, the bivector being the inverse of the symplectic form; every Lie algebra has a Poisson structure on the dual of its underlying vector space; and a general Poisson manifold is decomposed into symplectic pieces, its leaves, glued along a singular foliation.

**The boundary of this article is the distinction between three uses of the word *Poisson*, and it is stated here once.** The **linear-algebraic** theory — the alternating bilinear form on a vector space, the standard form on $k^{2n}$ and its Darboux normal form, the symplectic group, the isotropic and Lagrangian subspaces, the Pfaffian, and the bracket on the polynomial functions of a symplectic vector space together with its Weyl–Moyal deformation — is the subject of the companion article *Symplectic Forms and Poisson Brackets*, and is assumed. The **abstract algebraic** theory — a Poisson algebra as a commutative algebra with a bracket satisfying skew-symmetry, the Leibniz rule and the Jacobi identity, its derivations, its deformations and the Gerstenhaber algebras — belongs to Part I and is the subject of the companion article *Poisson and Gerstenhaber Algebras*, being written in parallel; that article owns the algebra, this one owns the manifold. What is new here is that the algebra is the algebra of smooth functions on a manifold, so that the bracket comes from a tensor field, the tensor field satisfies a differential equation, and the manifold can be cut into symplectic pieces. The **symplectic manifold** itself is the subject of *Symplectic Geometry*, and is the nondegenerate case of what follows.

Manifolds, charts, vector fields and the Lie bracket of vector fields are those of *Smooth Manifolds and Differential Geometry* and *Differential Topology*, being written in parallel; the exterior algebra of multivector fields and the interior product are those of *Exterior Powers* and *The Exterior Algebra*; differential forms and the de Rham cohomology those of *Differential Forms and Stokes' Theorem*; bundles and the tangent bundle those of *Fibre Bundles, Connections and Curvature*; Lie algebras those of Part I and Lie groups those of *Lie Groups*. The dynamics of a Hamiltonian vector field belongs to Part III, where the differential equation of a flow is treated; this article uses the vector field itself and the foliation it generates. The base field is $\mathbb{R}$ and no physics is invoked.

## Poisson Manifolds and the Poisson Tensor

**Definition.** A **Poisson structure** on a smooth manifold $M$ is an $\mathbb{R}$-bilinear map

$$
\{\cdot, \cdot\} : C^\infty(M)\times C^\infty(M) \longrightarrow C^\infty(M)
$$

such that for all $f, g, h \in C^\infty(M)$:

**(a)** $\{f, g\} = -\{g, f\}$ (skew-symmetry);

**(b)** $\{f, gh\} = \{f, g\}\,h + g\,\{f, h\}$ (the Leibniz rule, or derivation property);

**(c)** $\{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\} = 0$ (the Jacobi identity).

A **Poisson manifold** is a pair $(M, \{\cdot, \cdot\})$ of a manifold and a Poisson structure on it.

The Leibniz rule in each argument says that the bracket is a **biderivation** of the commutative algebra $C^\infty(M)$: it is a derivation in each slot separately, and it is not assumed to be a derivation of the bracket itself. By the universal property of the exterior algebra, a skew-symmetric biderivation is the same thing as a section of the bundle $\Lambda^2 TM$: there is a unique bivector field $\pi \in \Gamma(\Lambda^2TM)$ with

$$
\{f, g\} = \pi(df, dg) = \sum_{i, j} \pi^{ij}\, \partial_i f\, \partial_j g
$$

in local coordinates, where $\pi = \frac{1}{2}\sum_{i,j}\pi^{ij}\partial_i\wedge\partial_j$ with $\pi^{ij} = -\pi^{ji}$. The passage from the bracket to the tensor uses only the Leibniz rule; the Jacobi identity imposes a differential condition on $\pi$, which is the subject of the next section.

**Definition.** The **anchor** of a Poisson structure is the bundle map

$$
\pi^{\sharp} : T^*M \longrightarrow TM, \qquad \beta(\pi^{\sharp}(\alpha)) = \pi(\alpha, \beta).
$$

The **Hamiltonian vector field** of $f \in C^\infty(M)$ is $X_f = -\pi^{\sharp}(df)$, so that the bracket is recovered as $\{f, g\} = X_g(f) = -X_f(g)$, the convention of *Symplectic Geometry*. The **rank** of the Poisson structure at $x \in M$ is the rank of the linear map $\pi^{\sharp}_x : T^*_xM \to T_xM$; the structure is **nondegenerate** at $x$ when this map is an isomorphism.

**Remark.** The sign in $X_f = -\pi^{\sharp}(df)$ is forced by the convention $\{f,g\} = X_g(f)$ adopted in *Symplectic Geometry*: since $\beta(\pi^{\sharp}\alpha) = \pi(\alpha,\beta)$ for all $\beta$, one has $\pi^{\sharp}(dg) = -X_g$ and hence $\pi^{\sharp}(df) = -X_f$. A reader using the opposite sign for the Hamiltonian field must reverse every occurrence of $\pi^{\sharp}$ in the formulas below.

**Proposition.** For each $f$ the map $X_f$ is a derivation of $C^\infty(M)$, and the assignment $f \mapsto X_f$ is a homomorphism of Lie algebras from $(C^\infty(M), -\{\cdot,\cdot\})$ onto the **Hamiltonian vector fields**, whose kernel is the space of **Casimir functions**, that is, of the functions constant on each symplectic leaf; on a connected **nondegenerate** Poisson manifold that kernel is exactly the space of constants.

**Proof.** The Leibniz rule (b) says that $f \mapsto X_f(g) = -\{f, g\}$ is a derivation in $g$; the Jacobi identity (c) gives $[X_f, X_g] = -X_{\{f,g\}} = X_{-\{f,g\}}$, which is the statement that the assignment preserves the bracket once the bracket $-\{\cdot,\cdot\}$ is placed on the functions. A function $f$ with $X_f = 0$ satisfies $\{f, g\} = 0$ for every $g$, which is exactly the condition that $f$ be a **Casimir function**, that is, locally constant on the symplectic leaves below. On a connected **nondegenerate** Poisson manifold the anchor is an isomorphism, so $X_f=0$ forces $df=0$ and the kernel is exactly the constants; the converse can fail, since a structure may degenerate on a set of empty interior and still have no nonconstant global Casimir, as the affine example below shows. $\square$

**Remark.** The comparison with *Symplectic Geometry* is exact and worth recording. If $\omega$ is a symplectic form, the bundle isomorphism $\omega^{\flat} : TM \to T^*M$ has an inverse, and the bivector $\pi$ defined by $\pi^{\sharp} = -\omega^{\sharp}$, read as a section of $\Lambda^2TM$, satisfies the Poisson condition; the bracket it defines is the bracket of *Symplectic Geometry*, and the Poisson structure is nondegenerate everywhere. In Darboux coordinates $\omega = \sum_i dx^i\wedge dy^i$ and the corresponding bivector is $\pi = \sum_i \partial_{x^i}\wedge\partial_{y^i}$, whose coefficients are constant. Conversely, a Poisson structure that is nondegenerate at every point is the inverse of a symplectic form, with the sign above, and the closedness of that form is exactly the Jacobi identity. A Poisson manifold is thus a symplectic manifold with the nondegeneracy allowed to fail along a singular locus, and the geometry of the failure is what makes the subject. The identity $[X_f,X_g] = -X_{\{f,g\}}$ is the one of *Symplectic Geometry* and is kept here deliberately.

## The Schouten Bracket and the Jacobi Identity

**Definition.** A **multivector field** of degree $k$ on $M$ is a section of $\Lambda^kTM$; the space of multivector fields is the graded algebra

$$
\mathfrak{X}^\bullet(M) = \bigoplus_{k \geq 0} \Gamma(\Lambda^kTM) = \bigoplus_{k\ge0}\mathfrak{X}^k(M),
$$

with $\mathfrak{X}^0(M) = C^\infty(M)$ and $\mathfrak{X}^1(M) = \mathfrak{X}(M)$, graded-commutative under the wedge product. The **Schouten–Nijenhuis bracket** is the unique $\mathbb{R}$-bilinear map

$$
[\cdot, \cdot] : \mathfrak{X}^p(M)\times\mathfrak{X}^q(M) \longrightarrow \mathfrak{X}^{p+q-1}(M)
$$

that extends the Lie bracket of vector fields $[X, Y] \in \mathfrak{X}^1(M)$, satisfies $[X, f] = X(f)$ for $X \in \mathfrak{X}(M)$ and $f \in C^\infty(M)$, annihilates pairs of functions, and satisfies the graded Leibniz rule

$$
[X, Y\wedge Z] = [X, Y]\wedge Z + (-1)^{(p-1)q}\, Y\wedge[X, Z]
$$

for $X$ of degree $p$, $Y$ of degree $q$ and $Z$ arbitrary. It makes $\mathfrak{X}^\bullet(M)$ a graded Lie algebra of degree $-1$: it is graded-antisymmetric, $[Q,P] = -(-1)^{(p-1)(q-1)}[P,Q]$ for $P$ of degree $p$ and $Q$ of degree $q$ — which for two vector fields is the ordinary antisymmetry $[Y,X]=-[X,Y]$ — and it satisfies the graded Jacobi identity.

**Proposition (coordinate formula).** Let $\pi = \frac{1}{2}\sum_{i,j}\pi^{ij}\partial_i\wedge\partial_j$ be a bivector field. Then $[\pi,\pi]$ is the trivector field

$$
[\pi,\pi]^{ijk} = \sum_{l=1}^{n}\Bigl(\pi^{il}\,\partial_l\pi^{jk} + \pi^{jl}\,\partial_l\pi^{ki} + \pi^{kl}\,\partial_l\pi^{ij}\Bigr).
$$

**Proof.** This is the coordinate expansion of the graded Leibniz rule applied to the decomposition of $\pi$ into the basis vectors $\partial_i$; the terms in which the coefficient function is differentiated come from $[\partial_i, \pi^{jk}\partial_j\wedge\partial_k]$ and the terms of the form $\pi^{il}\partial_l\pi^{jk}$ from the Leibniz rule, while the bracket of two coordinate vector fields vanishes. $\square$

**Theorem.** Let $\pi$ be a bivector field and let $\{f,g\} = \pi(df,dg)$. Then the bracket satisfies the Jacobi identity if and only if $[\pi,\pi] = 0$. More precisely,

$$
\{f,\{g,h\}\} + \{g,\{h,f\}\} + \{h,\{f,g\}\} = [\pi,\pi](df, dg, dh)
$$

for all $f, g, h \in C^\infty(M)$.

**Proof.** Both sides are alternating trilinear over $\mathbb{R}$ and are derivations in each argument, and both annihilate any argument that is a constant; a trilinear derivation with these properties is determined by its values on the coordinate functions $x^1,\ldots,x^n$. Evaluating the two sides at $(x^i, x^j, x^k)$ gives, on the right, the coordinate formula for $[\pi,\pi]^{ijk}$ because $dx^i\wedge dx^j\wedge dx^k$ pairs with $\partial_l$ as displayed, and on the left

$$
\{x^i, \{x^j, x^k\}\} + \{x^j, \{x^k, x^i\}\} + \{x^k, \{x^i, x^j\}\} = \sum_l\bigl(\pi^{il}\partial_l\pi^{jk} + \pi^{jl}\partial_l\pi^{ki} + \pi^{kl}\partial_l\pi^{ij}\bigr),
$$

obtained by substituting $\{x^a, x^b\} = \pi^{ab}$ and using the Leibniz rule in the outer bracket. The two expressions agree, so the identity holds. $\square$

**Corollary.** A bivector field defines a Poisson structure precisely when $[\pi, \pi] = 0$; the Jacobi identity for the bracket is thus a finite system of polynomial differential equations of the first order on the coefficients of the tensor.

**Remark.** The equation $[\pi,\pi]=0$ is the classical **Poisson condition**, and it is a condition of a different nature from the closedness of a form: it is quadratic, not linear, in the coefficients of $\pi$, whereas $d\omega=0$ is linear in the coefficients of $\omega$. This quadraticity is the reason the deformation theory of a Poisson structure is nontrivial, and it is what makes reduction, linearisation and the local normal form of a Poisson structure genuinely harder than their symplectic counterparts. The bivector formulation is also the one that survives on an arbitrary algebra: a commutative algebra with an abstract biderivation that is skew-symmetric and satisfies the Jacobi identity is a Poisson algebra in the sense of Part I, and the manifold statement above is read there as a statement about the algebra of functions, as in *Poisson and Gerstenhaber Algebras*.

## Examples

**Example (symplectic manifolds).** If $(M, \omega)$ is symplectic then the bivector $\pi$ defined by $\pi^{\sharp} = -\omega^{\sharp}$ is nondegenerate and satisfies $[\pi,\pi]=0$, because in Darboux coordinates $\omega = \sum_i dx^i\wedge dy^i$ and $\pi = \sum_i \partial_{x^i}\wedge\partial_{y^i}$ has constant coefficients, so $[\pi,\pi]=0$ by the coordinate formula. The associated bracket is the one of *Symplectic Geometry*, and this is the fundamental class of examples.

**Example (constant Poisson structures).** On $\mathbb{R}^n$ fix a constant alternating matrix $(\pi^{ij})$ and define $\{f,g\} = \sum_{ij}\pi^{ij}\partial_i f\,\partial_j g$. The coordinate formula gives $[\pi,\pi]=0$ because every coefficient has zero derivative. The rank of the structure is the rank of the matrix, which is even, say $2r$; after a linear change of coordinates the matrix takes the normal form of *Symplectic Forms and Poisson Brackets*, and the structure is the product of a symplectic structure on $2r$ coordinates with the zero structure on the remaining $n-2r$. The Casimirs are the coordinates on the kernel.

**Example (the affine structure on the plane).** On $\mathbb{R}^2$ with coordinates $x, y$ put

$$
\{f, g\} = x\,(f_x g_y - f_y g_x), \qquad \pi = x\,\partial_x\wedge\partial_y .
$$

The Jacobi identity holds, and for a structural reason: on a surface every trivector field vanishes, since $\Lambda^3TM = 0$ in dimension two, so $[\pi,\pi]=0$ for every bivector and every bivector on a surface is Poisson. Here the bracket is also the Lie–Poisson structure of the two-dimensional nonabelian Lie algebra, whose Jacobi identity is the Jacobi identity of that Lie algebra: on the linear coordinates $\{x,y\} = x$. The rank is two away from the line $x = 0$ and zero on it, the symplectic leaves are the two open half-planes $x>0$, $x<0$ and the individual points of the line $x=0$, and there is no nonconstant Casimir: a Casimir would be constant on each leaf, hence locally constant on the dense open set $x\neq0$, hence locally constant on $M$. This is the simplest example of a Poisson structure that is symplectic off a singular locus.

**Example (Lie–Poisson structures).** Let $\mathfrak{g}$ be a finite-dimensional Lie algebra with bracket $[\cdot,\cdot]$, and let $\mathfrak{g}^*$ be its dual. For $f \in C^\infty(\mathfrak{g}^*)$ and $\xi \in \mathfrak{g}^*$ the differential $df_\xi$ is an element of $(\mathfrak{g}^*)^* \cong \mathfrak{g}$, and one defines

$$
\{f, g\}(\xi) = \langle \xi, [df_\xi, dg_\xi]\rangle .
$$

The Jacobi identity for this bracket is exactly the Jacobi identity of $\mathfrak{g}$, and the resulting structure is the **Lie–Poisson structure** on $\mathfrak{g}^*$. On linear coordinates $\{x_i, x_j\} = \sum_k c^k_{ij}x_k$, where $c^k_{ij}$ are the structure constants; the structure is **linear**, and a linear Poisson structure on $\mathfrak{g}^*$ is the same thing as a Lie algebra structure on $\mathfrak{g}$. The symplectic leaves are the coadjoint orbits, and the symplectic form on each orbit is the Kirillov–Kostant–Souriau form of *Symplectic Geometry*; the Casimirs are the invariants of the coadjoint representation. The Lie algebras and their structure constants are those of Part I, and the coadjoint action those of *Lie Groups*.

**Example.** The dual of the rotation Lie algebra $\mathfrak{so}(3)$ carries $\{x,y\} = z$, $\{y,z\} = x$, $\{z,x\} = y$, which is a Poisson structure: the coordinate formula gives $[\pi,\pi] = 0$ because the structure constants are those of a Lie algebra, and, directly, $\{x,\{y,z\}\} + \{y,\{z,x\}\} + \{z,\{x,y\}\} = \{x,x\} + \{y,y\} + \{z,z\} = 0$. The Casimir is $x^2+y^2+z^2$, and the symplectic leaves are the concentric spheres and the origin.

**Example (a bivector that is not Poisson).** The bivector $\pi = x\,\partial_x\wedge\partial_y + y\,\partial_y\wedge\partial_z$ on $\mathbb{R}^3$, that is $\{x,y\} = x$, $\{y,z\} = y$, $\{z,x\} = 0$, does **not** satisfy the Jacobi identity: the triple $(x,y,z)$ gives

$$
\{x,\{y,z\}\} + \{y,\{z,x\}\} + \{z,\{x,y\}\} = \{x,y\} + 0 + 0 = x \neq 0 .
$$

The example shows that the Leibniz rule alone does not produce a Poisson structure, and it isolates the Jacobi identity as the substantive condition.

## Casimirs and Symplectic Leaves

**Definition.** A **Casimir function** of a Poisson manifold $(M, \pi)$ is a function $f$ with $\{f, g\} = 0$ for all $g$; equivalently $df$ lies in the kernel of the anchor $\pi^{\sharp}$, or $f$ is constant on the symplectic leaves. The Casimirs form the **centre** of the Poisson algebra $C^\infty(M)$, and on a connected symplectic manifold they are the constants.

**Definition.** For $x \in M$, the **symplectic leaf** through $x$ is the set of points reachable from $x$ by a piecewise smooth path each of whose segments is an integral curve of a Hamiltonian vector field: the orbit of $x$ under the pseudogroup generated by all the flows of Hamiltonian vector fields.

**Theorem.** The manifold $M$ is the disjoint union of its symplectic leaves; the leaf through $x$ is an immersed submanifold of dimension equal to the rank of $\pi$ at $x$; the rank is constant along a leaf; and the restriction of the Poisson tensor to a leaf is nondegenerate, so that the leaf carries a symplectic form. The leaves are the maximal integral manifolds of the singular distribution $x \mapsto \pi^{\sharp}_x(T^*_xM)$, and this distribution is involutive in the sense that it is spanned by Hamiltonian vector fields.

**Proof sketch.** The flows of the Hamiltonian vector fields are complete only locally, so the reachable set is a countable union of images of charts and is therefore an immersed submanifold; it is connected by construction. The tangent space to the leaf at $x$ is spanned by the values $X_f(x) = -\pi^{\sharp}_x(df_x)$, hence equals $\pi^{\sharp}_x(T^*_xM)$, of dimension the rank. Since $\{f,g\}$ is constant along the flows, the rank is constant along the leaf. The anchor identifies $T^*_xM/\ker\pi^\sharp_x$ with $T_xL$, and the bracket, read on functions of the leaf, defines a nondegenerate Poisson structure; the inverse of a nondegenerate Poisson structure is a symplectic form, as in *Symplectic Geometry*. $\square$

**Theorem (Weinstein splitting).** Let $(M, \pi)$ be a Poisson manifold and let $x$ have rank $2r$. Then there is a chart centred at $x$ with coordinates

$$
q_1, \ldots, q_r, \; p_1, \ldots, p_r, \; y_1, \ldots, y_{n-2r}
$$

in which

$$
\pi = \sum_{i=1}^{r} \partial_{q_i}\wedge\partial_{p_i} + \frac{1}{2}\sum_{j,k} \phi_{jk}(y)\, \partial_{y_j}\wedge\partial_{y_k}, \qquad \phi_{jk}(0) = 0 .
$$

Consequently the Poisson structure is locally the product of a symplectic structure of dimension $2r$ and a Poisson structure whose rank vanishes at the origin, and the symplectic leaf through $x$ is locally the slice $y = 0$.

**Proof sketch.** The first term is the symplectic normal form along the leaf, produced by the symplectic Darboux theorem applied to the restriction of $\pi$ to the leaf and a complementary choice of coordinates; the remaining part is the **transverse Poisson structure**, defined on a complement to the leaf, and it is Poisson because the bracket of two functions of the transverse coordinates is again a function of them. The vanishing $\phi_{jk}(0)=0$ is the statement that the rank at the origin is exactly $2r$, so the transverse structure vanishes there. $\square$

**Remark.** The splitting theorem is the sharp local statement of Poisson geometry, and it is the reason a Poisson manifold is described as a foliation by symplectic leaves with a transverse singular structure. In the nondegenerate case $r = n/2$ it reduces to the Darboux theorem of *Symplectic Geometry*; in the Lie–Poisson case the leaves are the coadjoint orbits and the splitting is the theorem of Lie–Weinstein on the linearisation of a Poisson structure at a point. The local normal form is not a classification: the transverse factor $\phi$ has no linear term and its higher terms are arbitrary solutions of the Poisson condition, so two Poisson structures of the same rank at a point need not be locally isomorphic, and the classification of Poisson structures in dimension three is already a nontrivial problem.

## Poisson Maps and Poisson Cohomology

**Definition.** Let $(M, \pi)$ and $(N, \sigma)$ be Poisson manifolds. A **Poisson map** is a smooth map $F : M \to N$ with

$$
\{f\circ F, g\circ F\}_\pi = \{f, g\}_\sigma \circ F
$$

for all $f, g \in C^\infty(N)$; the Poisson structures are **compatible** when such a map is a diffeomorphism. A submanifold $C \subseteq M$ is **coisotropic** if the ideal of functions vanishing on $C$ is closed under the bracket, equivalently if $\pi^{\sharp}(TC^{\circ}) \subseteq TC$, where $TC^{\circ} \subseteq T^*M|_C$ is the annihilator of $TC$.

**Proposition.** The Poisson condition is preserved by the maps that are compatible with it, and a Darboux chart of *Symplectic Geometry* is exactly a local Poisson diffeomorphism onto a constant structure.

**Definition.** The **Poisson cohomology** of $(M, \pi)$ is the cohomology of the complex of multivector fields with the differential

$$
d_\pi = [\pi, \cdot] : \mathfrak{X}^k(M) \longrightarrow \mathfrak{X}^{k+1}(M),
$$

which satisfies $d_\pi^2 = 0$ because of the graded Jacobi identity and $[\pi,\pi]=0$. Its groups are written $H^k_\pi(M)$.

**Proposition.** The low-dimensional groups have interpretations in terms of the structure: $H^0_\pi(M)$ is the space of Casimir functions, $H^1_\pi(M)$ is the quotient of the Poisson vector fields (those $X$ with $\mathcal{L}_X\pi = 0$) by the Hamiltonian vector fields, and $H^2_\pi(M)$ controls the infinitesimal deformations of the Poisson structure modulo those generated by diffeomorphisms.

**Proof.** A multivector $P$ of degree zero is a function and $[\pi, f] = X_f$, so $d_\pi f$ vanishes exactly when the Hamiltonian field $X_f$ does, so $H^0_\pi$ is the kernel of $f\mapsto X_f$, namely the Casimirs. A vector field $X$ is a cocycle exactly when $[\pi, X]=0$, which is $\mathcal{L}_X\pi = 0$; a coboundary is a Hamiltonian field, since $[\pi, f] = X_f$ and the fields $-X_f$ span the same space as the $X_f$, giving the stated quotient for $H^1_\pi$. For $H^2_\pi$, a bivector $P$ with $[\pi,P]=0$ is a first-order deformation of the Poisson condition, since $[\pi+\epsilon P, \pi+\epsilon P] = 2\epsilon[\pi,P] + \epsilon^2[P,P]$ vanishes to first order, and the coboundaries $[\pi,X]$ are the deformations induced by the flow of $X$. $\square$

**Theorem.** If $\pi$ is nondegenerate, so that $(M,\omega)$ is symplectic with $\pi^{\sharp} = -\omega^{\sharp}$, then the anchor is an isomorphism and the Poisson cohomology is isomorphic to the de Rham cohomology: $H^k_\pi(M) \cong H^k_{dR}(M)$.

**Proof.** The anchor extends to a map of graded algebras $\mathfrak{X}^\bullet(M) \to \Omega^\bullet(M)$ that sends a multivector field to the form obtained by lowering indices with $\omega$; it is an isomorphism of vector spaces. Pulling back the differential along the anchor gives $d_\pi \mapsto d$ and $d_\pi = [\pi,\cdot]$ corresponds to the de Rham differential. $\square$

**Remark.** For a general Poisson structure the anchor is not an isomorphism and the Poisson cohomology is genuinely larger than the de Rham cohomology of the leaves; it is the natural home of the invariants of a Poisson manifold, and it was introduced as the cohomology of the algebra of functions with the Hamiltonian differential. Its algebraic counterpart for an abstract Poisson algebra is the subject of *Poisson and Gerstenhaber Algebras*, and the deformation theory it controls — the passage from a Poisson structure to a noncommutative associative multiplication — is Kontsevich's theorem, stated below.

## Deformation Quantisation

**Definition.** Let $(M, \pi)$ be a Poisson manifold. A **star product** is an associative $\mathbb{R}[[\hbar]]$-bilinear product on $C^\infty(M)[[\hbar]]$ of the form

$$
f * g = fg + \hbar\,\{f,g\} + \sum_{r \geq 2}\hbar^{\,r}\, C_r(f, g),
$$

where the $C_r$ are bidifferential operators and $\hbar$ is a formal parameter, with unit the constant function $1$. The deformation is **trivial** if it is isomorphic to the undeformed product by an $\mathbb{R}[[\hbar]]$-linear isomorphism of the form $\mathrm{id} + \hbar(\cdots)$.

**Theorem (Kontsevich).** Every Poisson manifold admits a star product; more precisely, the equivalence classes of star products are in bijection with the equivalence classes of Poisson structures under the action of formal diffeomorphisms, so that the formality of the little discs operad identifies the deformation of the commutative product with the Poisson structure itself.

**Proof sketch.** The statement is the formality theorem for the operad of little discs: the chain complex of the operad is quasi-isomorphic to its homology, which is the operad governing Poisson structures, and the quasi-isomorphism can be chosen to intertwine the deformation complexes. The resulting star products are constructed by explicit integrals over configuration spaces, the weights being those of the formality morphism. $\square$

**Remark.** Deformation quantisation belongs to the interface of algebra, geometry and analysis: the star product is an algebraic object, its existence is a theorem of formal geometry, and the interpretation of the deformation as a Weyl-type calculus requires the analytic setting of Part III. The constant-coefficient case on a symplectic vector space is the Weyl–Moyal product of *Symplectic Forms and Poisson Brackets*, and the algebraic framework of the deformation is that of *Poisson and Gerstenhaber Algebras*; this article records the result for the manifold case and refers the analytic theory forward.

## Summary

A Poisson manifold is a manifold whose algebra of smooth functions carries a bracket that is skew-symmetric, a derivation in each argument, and satisfies the Jacobi identity. The Leibniz rule makes the bracket the contraction of a bivector field $\pi$ with the differentials, the Hamiltonian vector field of a function is $X_f = -\pi^{\sharp}(df)$, and the Jacobi identity is equivalent to the Poisson condition $[\pi,\pi]=0$ for the Schouten–Nijenhuis bracket. Every symplectic manifold is Poisson with $\pi$ the inverse of the symplectic form, so a Poisson manifold is a symplectic manifold with controlled degeneracy.

The examples are the symplectic manifolds, the constant structures on $\mathbb{R}^n$, the affine structure $\{x,y\}=x$ on the plane, and the Lie–Poisson structures on the dual of a Lie algebra, whose leaves are the coadjoint orbits; the bivector $x\,\partial_x\wedge\partial_y + y\,\partial_y\wedge\partial_z$ shows that the Jacobi identity is a genuine restriction. A Poisson manifold is a disjoint union of symplectic leaves, of dimension the rank at a point, and the Weinstein splitting theorem puts the structure locally into the product of a symplectic factor and a transverse singular factor.

A Poisson map preserves the bracket, a coisotropic submanifold is one whose vanishing ideal is a subalgebra, and the Poisson cohomology $H^\bullet_\pi(M)$ is the cohomology of the complex with differential $d_\pi = [\pi,\cdot]$; its degree zero is the Casimirs, its degree one the Poisson vector fields modulo Hamiltonian ones, and its degree two the infinitesimal deformations. For a nondegenerate structure it coincides with the de Rham cohomology, and in general it controls the deformation quantisation whose existence is Kontsevich's theorem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M$ | Smooth manifold; $T_xM$, $TM$, $T^*M$ the tangent and cotangent objects |
| $\mathfrak{X}(M)$, $\Omega^k(M)$ | Smooth vector fields and $k$-forms |
| $\{\cdot,\cdot\}$ | The Poisson bracket on $C^\infty(M)$; skew, Leibniz, Jacobi |
| $\pi \in \Gamma(\Lambda^2TM)$ | Poisson bivector; $\{f,g\} = \pi(df,dg)$ |
| $\pi^{ij}$ | Coefficients in $\pi = \frac12\sum_{ij}\pi^{ij}\partial_i\wedge\partial_j$, $\pi^{ij}=-\pi^{ji}$ |
| $\pi^{\sharp} : T^*M\to TM$ | Anchor, $\beta(\pi^{\sharp}\alpha)=\pi(\alpha,\beta)$ |
| $X_f = -\pi^{\sharp}(df)$ | Hamiltonian vector field of $f$ |
| $\operatorname{rank}_x\pi$ | Rank of $\pi^{\sharp}_x$; even, constant on leaves |
| $[\cdot,\cdot]$ | Schouten–Nijenhuis bracket on multivector fields, degree $-1$ |
| $[\pi,\pi]=0$ | The Poisson condition; equivalent to the Jacobi identity |
| Casimir | $f$ with $\{f,g\}=0$ for all $g$; centre of $C^\infty(M)$ |
| Symplectic leaf | Orbit under the Hamiltonian flows; carries a symplectic form |
| $(q_i, p_i, y_j)$ | Weinstein splitting coordinates; $\pi = \sum\partial_{q_i}\wedge\partial_{p_i} + \frac12\sum\phi_{jk}(y)\partial_{y_j}\wedge\partial_{y_k}$ |
| $\mathfrak{g}^*$, $\{f,g\}(\xi)=\langle\xi,[df,dg]\rangle$ | Lie–Poisson structure on the dual of a Lie algebra |
| Poisson map $F$ | $\{f\circ F, g\circ F\} = \{f,g\}\circ F$ |
| Coisotropic submanifold | Vanishing ideal closed under the bracket; $\pi^{\sharp}(TC^{\circ})\subseteq TC$ |
| $d_\pi = [\pi,\cdot]$, $H^\bullet_\pi(M)$ | Poisson differential and Poisson cohomology |
| $f * g = fg + \hbar\{f,g\} + \cdots$ | Star product; Kontsevich's deformation quantisation |

## Further Reading

- André Lichnerowicz, "Les variétés de Poisson et leurs algèbres de Lie associées", *Journal of Differential Geometry* 12 (1977), 253–300, for the Poisson tensor, the Poisson condition and Poisson cohomology.
- Alan Weinstein, "The Local Structure of Poisson Manifolds", *Journal of Differential Geometry* 18 (1983), 523–557, for the splitting theorem and the local theory of the leaves.
- Izu Vaisman, *Lectures on the Geometry of Poisson Manifolds* (Birkhäuser, 1994), for a complete account of the Poisson tensor, the Schouten bracket and the foliation.
- Pierre Laurent-Gengoux, Anne Pichereau and Pol Vanhaecke, *Poisson Structures* (Springer, 2013), for the Schouten–Nijenhuis bracket, the Jacobi identity and the local normal form.
- Jerrold Marsden and Tudor Ratiu, *Introduction to Mechanics and Symmetry* (Springer, 2nd ed. 1999), for Lie–Poisson structures, coadjoint orbits and reduction.
- Maxim Kontsevich, "Deformation Quantization of Poisson Manifolds", *Letters in Mathematical Physics* 66 (2003), 157–216, for the formality theorem and the existence of star products.
- Jean-Paul Dufour and Nguyen Tien Zung, *Poisson Structures and Their Normal Forms* (Birkhäuser, 2005), for the classification of Poisson structures in low dimensions.
