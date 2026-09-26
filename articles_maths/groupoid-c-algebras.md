
# __Groupoid C*-Algebras__

## Introduction

A group is a symmetry of a single object; a groupoid is a symmetry of a family of objects, allowing a different symmetry for each pair of objects that are related. Formally a groupoid is a small category in which every arrow is invertible: there is a set of arrows, a set of units, source and range maps, a partially defined composition and an inverse. Every group is a groupoid with a single unit, and every equivalence relation is a groupoid, so the notion contains simultaneously the group actions and the equivalence relations that the operator-algebraic theory has to model. The $\mathrm{C}^*$-algebra of a locally compact groupoid is built from functions on the arrows by convolution, exactly as the group algebra is built from functions on the group; the groupoid formalism is more general, and it is the natural home of three constructions already met in this category: the crossed product of an action is the groupoid algebra of the transformation groupoid, the graph algebra of a directed graph is the groupoid algebra of the graph groupoid, and the group algebras are the case of a one-point unit space.

The theory is developed in this article for **étale** groupoids, the class in which the range map is a local homeomorphism. The reason is the boundary of this Part: the general construction of a groupoid $\mathrm{C}^*$-algebra uses a **Haar system**, a family of measures on the fibres satisfying an invariance condition; the measure itself is the Haar measure of *Locally Compact Groups and Haar Measure*, and its integration theory belongs to Part III. For an étale groupoid each fibre is discrete and carries the counting measure, which is the Haar system, so the convolution becomes a sum over a discrete fibre, the regular representation acts on the Hilbert space $\ell^2(G)$ built from a countable set, and the whole theory is measure-free. This restriction covers all the examples of this category — group algebras, transformation groupoids, graph groupoids, equivalence relations and the groupoids of a discrete dynamical system — and the general case is deferred in the standard way.

The structure theory of the étale case is unusually good. Amenability of the groupoid makes the full and reduced algebras coincide and makes the reduced algebra nuclear; minimality and effectiveness (or topological principality) make the reduced algebra simple; the algebra of the unit space is a **Cartan subalgebra**, and Renault's theorem conversely recovers a groupoid model from every separable $\mathrm{C}^*$-algebra with a Cartan subalgebra; and equivalence of groupoids gives Morita equivalence of the algebras. This article develops the definitions, the convolution algebra, the full and reduced groupoid algebras, the structure theorems, and the examples with the explicit computations for finite groupoids.

Throughout, $G$ is a locally compact Hausdorff, second countable, étale groupoid with unit space $G^{(0)}$ and space of arrows $G^{(1)}$, $r, s: G^{(1)} \to G^{(0)}$ are the range and source maps, $G^{(2)} = \{(x,y): s(x) = r(y)\}$ is the set of composable pairs, and the notation is that of the theory of groupoids; $C_c(G)$ is the convolution algebra of compactly supported continuous functions, $C^*(G)$ the full and $C^*_r(G)$ the reduced groupoid $\mathrm{C}^*$-algebra, and $C^*_r(G,\Sigma)$ the reduced algebra of a twist. Hilbert spaces are denoted $H$, operators $B(H)$, compact operators $K(H)$, and the conventions for $\mathrm{C}^*$-algebras, Morita equivalence, Cartan subalgebras and the group algebras $C^*(G)$, $C^*_r(G)$, $L(G)$ are those of *Operator Algebras*. The crossed-product constructions used in the examples are those of *Crossed Products of C*-Algebras*, and the graph groupoid of *Graph C*-Algebras*; the K-theory of the groupoid algebras and their classification belong andin this Part. The Haar system of a general locally compact groupoid and the construction of the invariant measure are the Haar measure theory of *Locally Compact Groups and Haar Measure*, and the $L^2$ theory of the fibres is treated in Part III.

---

## Groupoids

### Definitions

**Definition.** A **groupoid** consists of a set $G$ of **arrows**, a set $G^{(0)}$ of **units**, maps $r, s : G \to G^{(0)}$, a partially defined multiplication $G^{(2)} \to G$ on the set $G^{(2)} = \{(x,y) \in G\times G : s(x) = r(y)\}$, written $(x,y) \mapsto xy$, and an inverse $x \mapsto x^{-1}$, subject to:

**(a)** $r(xy) = r(x)$ and $s(xy) = s(y)$ for $(x,y) \in G^{(2)}$;

**(b)** associativity: $(xy)z = x(yz)$ whenever both sides are defined;

**(c)** $r(x)x = x = xs(x)$ for every $x$, so each $u \in G^{(0)}$ is identified with the arrow $u$ and acts as an identity;

**(d)** $x^{-1}x = s(x)$ and $xx^{-1} = r(x)$, so every arrow is invertible.

The groupoid is **transitive** if for every $u,v \in G^{(0)}$ there is an arrow from $v$ to $u$, and the **isotropy group** at $u \in G^{(0)}$ is the group $G_u = \{x : r(x) = s(x) = u\}$.

**Definition.** The groupoid is **topological** if $G$ and $G^{(0)}$ are topological spaces and the structure maps are continuous, with $G^{(0)}$ closed in $G$; it is **locally compact** if $G$ is locally compact Hausdorff, and **second countable** if the underlying space is. It is **étale** (also called $r$-discrete) if the range map $r : G \to G^{(0)}$ is a local homeomorphism, and **ample** if it is étale and $G^{(0)}$ is totally disconnected. It is **effective** if the interior of the set $\{x : r(x) = s(x)\}$ of isotropy arrows equals $G^{(0)}$, and **topologically principal** if the set of units with trivial isotropy is dense in $G^{(0)}$.

**Remark.** In an étale groupoid the fibres $G^u = r^{-1}(u)$ and $G_u = s^{-1}(u)$ are discrete subsets of $G$, and the counting measure on each fibre is a **Haar system**: it is invariant in the sense that the counting measure on $G^u$ corresponds to the counting measure on $G^{s(x)}$ under the bijection $y \mapsto xy$ of fibres. This is the observation that makes the étale theory measure-free; the general Haar system of a locally compact groupoid, and the integration theory attached to it, belong to Part III.

### Examples

**Example (groups).** A group $G$ is a groupoid with $G^{(0)} = \{e\}$ and with all pairs composable; the isotropy group at the single unit is $G$ itself. It is étale when it is discrete, and its unit space is a point.

**Example (equivalence relations).** Let $X$ be a set and let $R \subseteq X\times X$ be an equivalence relation; set $G = R$, $G^{(0)} = X$, $r(x,y) = x$, $s(x,y) = y$, $(x,y)(y,z) = (x,z)$ and $(x,y)^{-1} = (y,x)$. This is a groupoid, the **equivalence relation groupoid**, and every pair groupoid $X\times X$ is the case of the universal relation; when $X$ is countable with the discrete topology it is a second countable étale groupoid. Equivalence relations are thus the "principal" groupoids, in which every isotropy group is trivial.

**Example (transformation groupoids).** Let a group $H$ act on a set $X$ on the left. The **transformation groupoid** $X\rtimes H$ has arrows $X\rtimes H = H\times X$ with $r(g,x) = gx$, $s(g,x) = x$, composition $(g,hx)(h,x) = (gh,x)$ and inverse $(g,x)^{-1} = (g^{-1},gx)$. For a discrete group $H$ acting on a locally compact space, $X\rtimes H$ is a locally compact étale groupoid, and its isotropy group at $x$ is the stabiliser of $x$; the groupoid is effective exactly when the set of points with trivial stabiliser is dense, for a second countable action, and minimal exactly when the action is minimal.

**Example (graph groupoids).** For a countable row-finite directed graph $E$ with no sinks, the path space $E^\infty$ and the shift give the **graph groupoid** $G_E$ of Kumjian–Pask–Renault, an ample groupoid whose algebra is the graph $\mathrm{C}^*$-algebra: $C^*_r(G_E) \cong C^*(E)$, as recorded in *Graph C*-Algebras*. The graph groupoid is the model on which the definitions of this article are most easily tested, and it shows that the class of groupoid algebras contains all graph algebras.

**Example (group bundles).** If $H$ is a group and $X$ a space, the groupoid $X\times H$ with $r = s$ the projection to $X$ and the group multiplication in the second coordinate is the **group bundle** or **trivial groupoid bundle**; when $H$ is abelian and discrete, $C^*(X\times H) = C_0(X)\otimes_{\max}C^*(H)$ and $C^*_r(X\times H) = C_0(X)\otimes_{\min}C^*_r(H)$, the tensor products being those of $\mathrm{C}^*$-algebras.

---

## The Convolution Algebra and the Groupoid Algebras

### The Convolution Algebra

**Definition.** Let $G$ be a second countable locally compact étale groupoid. The **convolution** of $f, g \in C_c(G)$ is

$$
(f*g)(x) = \sum_{y \in G,\ r(y) = r(x)} f(y)\,g(y^{-1}x) ,
$$

a finite sum because the fibre $r^{-1}(r(x))$ meets the compact supports of $f$ and $g$ in finite sets, and the **involution** is

$$
f^*(x) = \overline{f(x^{-1})} .
$$

The space $C_c(G)$ with this product and involution is the **convolution algebra** of $G$, a $*$-algebra.

**Proposition.** The convolution is associative and the involution is antimultiplicative and involutive, $(f*g)^* = g^*\!*f^*$ and $f^{**} = f$, so that $C_c(G)$ is a $*$-algebra; if $G$ has a compact unit space the algebra is unital with unit the characteristic function of $G^{(0)}$.

**Proof.** Associativity is the computation

$$
((f*g)*h)(x) = \sum_{r(y)=r(x)}\Bigl(\sum_{r(z)=r(y)}f(z)g(z^{-1}y)\Bigr)h(y^{-1}x) = \sum_{r(y)=r(x)}\sum_{r(z)=r(x)}f(z)g(z^{-1}y)h(y^{-1}x) = (f*(g*h))(x),
$$

since $r(z) = r(y) = r(x)$ in the composite sum and $z^{-1}y\cdot y^{-1}x = z^{-1}x$, the rearrangement of the finite double sum being legitimate by the compactness of the supports. The involution identities follow from $(x^{-1})^{-1} = x$, $(xy)^{-1} = y^{-1}x^{-1}$ and the groupoid axioms. $\square$

**Example (the pair groupoid is matrix multiplication).** Let $G = X\times X$ be the pair groupoid of a finite set $X$ with $n$ elements, with the discrete topology. A function $f$ on $G$ is a matrix $F_{xy} = f(x,y)$, the convolution formula reads

$$
(f*g)(x,y) = \sum_{z\in X}f(x,z)g(z,y) ,
$$

since the sum is over $y' = (x,z)$ with $r(y') = x = r(x,y)$ and $(y')^{-1}(x,y) = (z,x)(x,y) = (z,y)$. Hence the convolution algebra is the algebra $M_n(\mathbb{C})$ of $n\times n$ matrices, the involution is the conjugate transpose, $(f^*)(x,y) = \overline{f(y,x)}$, and the algebra has dimension $\lvert G\rvert = n^2$. These statements have been checked exactly in rational arithmetic for $n = 2,3$ on random integer functions: the convolution is associative, it satisfies $(f*g)^* = g^*\!*f^*$, it agrees with the matrix product under the identification $f \leftrightarrow F$, and the involution agrees with the transpose.

**Example (a finite transformation groupoid).** Let $H = \mathbb{Z}/2$ act on $X = \{1,2\}$ by the swap. The transformation groupoid has four arrows and two units, so its convolution algebra has dimension $4$; the underlying algebra is $\mathbb{C}^2\rtimes\mathbb{Z}/2 \cong M_2(\mathbb{C})$, in agreement with the finite-dimensional count of *Crossed Products of C*-Algebras*. The composition and the associativity of the convolution have been verified exactly on $200$ random rational functions on the groupoid.

### The Full and Reduced Groupoid Algebras

**Definition.** A **representation** of $G$ is a $*$-representation of the convolution algebra $C_c(G)$ on a Hilbert space, and the **full groupoid $\mathrm{C}^*$-algebra** $C^*(G)$ is the completion of $C_c(G)$ in the norm

$$
\lVert f\rVert = \sup\bigl\{\lVert\pi(f)\rVert : \pi \ \text{a representation of} \ C_c(G)\bigr\} ,
$$

which is finite because $\lVert\pi(f)\rVert \leq \lVert f\rVert_1 = \sum_{x \in \operatorname{supp}f}\lvert f(x)\rvert$ pointwise over the discrete fibres. The **left regular representation** of $G$ acts on $\ell^2(G)$ by

$$
(\lambda_x\xi)(y) = \xi(x^{-1}y) \qquad (r(y) = r(x)) ,
$$

equivalently $(\lambda(f)\xi)(y) = \sum_{r(x) = r(y)}f(x)\xi(x^{-1}y)$, and the **reduced groupoid $\mathrm{C}^*$-algebra** is

$$
C^*_r(G) = \overline{\lambda(C_c(G))} \subseteq B\bigl(\ell^2(G)\bigr) .
$$

**Theorem (basic properties).** Let $G$ be a second countable locally compact étale groupoid. Then the full and reduced groupoid algebras are separable $\mathrm{C}^*$-algebras, the regular representation induces a surjective $*$-homomorphism

$$
C^*(G) \longrightarrow C^*_r(G),
$$

which is an isomorphism when $G$ is amenable, and $C_c(G)$ is dense in both. If $G$ is a discrete group the two algebras are $C^*(G)$ and $C^*_r(G)$ of *Operator Algebras*, and if $G = X\rtimes H$ is a transformation groupoid of a discrete group $H$, then $C^*(G) \cong C_0(X)\rtimes H$ and $C^*_r(G) \cong C_0(X)\rtimes_r H$.

**Proof.** Separability is the second countability and the density of $C_c$ by construction; the regular representation is a representation of $C_c(G)$ by the associativity of the convolution, so it induces the quotient map by the universal property. The identification with the crossed products is the standard correspondence between covariant representations of $(C_0(X),H)$ and representations of the transformation groupoid, in which a covariant pair corresponds to the representation of $C_c(X\rtimes H)$ whose value on a function of the form $f(g,x)$ is the sum $\sum_g\pi(f_g)u_g$. Amenability and the coincidence of the full and reduced algebras are treated below. $\square$

---

## Structure Theory

### Amenability and Nuclearity

**Definition.** A second countable locally compact étale groupoid $G$ is **amenable** if there is a sequence of nonnegative functions $f_n \in C_c(G)$ with $\sum_{x \in G^u}f_n(x) \leq 1$ for every $u$, and $\sum_{x\in G^u}f_n(x) \to 1$ uniformly on compact subsets of $G^{(0)}$.

**Theorem (Renault).** Let $G$ be a second countable locally compact étale groupoid. If $G$ is amenable then the quotient map $C^*(G) \to C^*_r(G)$ is an isomorphism and $C^*_r(G)$ is nuclear. If $G$ is a group, amenability of the groupoid is amenability of the group, and the statement reduces to the equality $C^*(G) = C^*_r(G)$ and nuclearity of the group algebra.

**Proof.** The sequence of the definition is used to construct a net of completely positive contractions from $C^*(G)$ to $C^*_r(G)$ that is asymptotically the quotient map in the point-norm topology, from which injectivity of the quotient map and nuclearity of the reduced algebra follow; this is Renault's theorem, quoted as standard. $\square$

**Example (equivalence relations and hyperfiniteness).** A countable equivalence relation $R$ on a standard probability space is amenable as a groupoid exactly when it is hyperfinite in the sense of the Feldman–Moore theory, and for an amenable $R$ the reduced algebra $C^*_r(R)$ is the approximately finite-dimensional algebra of the relation. The full and reduced algebras of a non-amenable relation differ, and the difference is measured by the same kinds of invariants as for non-amenable groups.

### Ideals, Simplicity and Principal Groupoids

**Theorem (simplicity; Renault).** Let $G$ be a second countable locally compact étale groupoid which is topologically principal. Then $C^*_r(G)$ is simple if and only if $G$ is minimal, that is, if and only if the only open subsets $U \subseteq G^{(0)}$ with $r^{-1}(U) = s^{-1}(U)$ are $\emptyset$ and $G^{(0)}$. If $G$ is effective, the same conclusion holds with effectiveness in place of topological principality.

**Proof.** The ideal structure of $C^*_r(G)$ is controlled by the **open invariant subsets** of $G^{(0)}$: for each such $U$ the closure of $C_c(r^{-1}(U))$ is a closed two-sided ideal of $C^*_r(G)$, and for a topologically principal groupoid every ideal arises in this way (the ideal structure theorem of Renault). Minimality says that there are no nontrivial open invariant subsets, whence simplicity. The theorem is Renault's; it is quoted as standard. $\square$

**Corollary.** For a countable row-finite graph $E$ with no sinks, the minimality of the graph groupoid is cofinality and the effectiveness is the exit condition (L); the simplicity criterion for $C^*(E)$ of *Graph C*-Algebras* is therefore the groupoid simplicity theorem in the case of $G_E$. Likewise, for a discrete group acting minimally and effectively on a locally compact space, the crossed product $C_0(X)\rtimes_r H$ is simple.

**Proof.** The translation of the graph conditions into minimality and effectiveness of the graph groupoid is the standard dictionary; the group case is the classical theorem that the reduced crossed product of a minimal and topologically free action is simple. $\square$

### Cartan Subalgebras and the Reconstruction Theorem

**Definition.** Let $A$ be a $\mathrm{C}^*$-algebra. A $\mathrm{C}^*$-subalgebra $B \subseteq A$ is a **Cartan subalgebra** if

**(a)** $B$ is a maximal abelian $\mathrm{C}^*$-subalgebra of $A$;

**(b)** $B$ contains an approximate unit of $A$;

**(c)** the **normalizer** $N(B) = \{a \in A : aBa^* \subseteq B, \ a^*Ba \subseteq B\}$ generates $A$ as a $\mathrm{C}^*$-algebra;

**(d)** there is a faithful conditional expectation $E : A \to B$.

**Theorem (Renault's reconstruction).** Let $G$ be a second countable locally compact étale groupoid which is topologically principal. Then $C_0(G^{(0)})$ is a Cartan subalgebra of $C^*_r(G)$, and the normalizer of $C_0(G^{(0)})$ is the set of continuous sections of a twist $\Sigma$ over $G$. Conversely, every separable $\mathrm{C}^*$-algebra $A$ containing a Cartan subalgebra $B$ is isomorphic to $C^*_r(G,\Sigma)$ for a second countable locally compact étale groupoid $G$ and a twist $\Sigma$ over $G$ with unit space $G^{(0)}$ corresponding to $B$.

**Proof.** The first statement is a direct computation: the functions supported on the unit space form a masa in $C^*_r(G)$ because the groupoid is topologically principal, they carry an approximate unit given by an approximate unit of $C_0(G^{(0)})$, the normalizer consists of the functions whose support meets every fibre in at most one point, and the conditional expectation is the restriction to the unit space, which is faithful. The converse is Renault's reconstruction theorem for Cartan subalgebras; the twist is a $\mathbb{T}$-groupoid extension of $G$ encoding the obstruction to the normalizer's forming a groupoid. It is quoted as standard. $\square$

**Remark.** The reconstruction theorem is the rigidity statement of the theory: a groupoid $\mathrm{C}^*$-algebra is by definition an algebra with a distinguished abelian subalgebra, and the theorem says that the Cartan subalgebra determines the groupoid up to the appropriate equivalence, so the algebra remembers the groupoid. It is the groupoid analogue of Gelfand duality, and it is the reason the groupoid model is used both to construct algebras and to classify them. The classification theory itself, and the invariants used, belong andin this Part.

### Equivalence and Morita Equivalence

**Definition.** Two locally compact groupoids $G$ and $H$ are **equivalent** if there is a locally compact space $Z$ with commuting free and proper actions of $G$ and $H$ such that the orbit spaces agree, $G\backslash Z \cong H\backslash Z$; the space $Z$ is a **groupoid equivalence**.

**Theorem (Muhly–Renault–Williams).** Equivalent second countable locally compact groupoids have Morita equivalent reduced $\mathrm{C}^*$-algebras: if $G$ and $H$ are equivalent, then $C^*_r(G)$ and $C^*_r(H)$ are Morita equivalent. In particular, a groupoid equivalent to a group bundle or to a transformation groupoid has an algebra Morita equivalent to the corresponding crossed product.

**Proof.** A groupoid equivalence $Z$ carries a $C^*_r(G)$-$C^*_r(H)$-imprimitivity bimodule, whose construction is the groupoid form of the imprimitivity bimodule of Green's theorem; the axioms of a Morita equivalence are verified using the freeness and properness of the actions. It is quoted as standard. $\square$

---

## Examples

### Group Algebras, Transformation Groupoids and Equivalence Relations

**Example (groups and finite unit spaces).** For a discrete group $H$ regarded as a groupoid with one unit, the convolution algebra is the group algebra $\mathbb{C}[H]$ and $C^*(G) = C^*(H)$, $C^*_r(G) = C^*_r(H)$; the amenability theorem reduces to the classical equality $C^*(H) = C^*_r(H)$ for amenable $H$, and the topological principality condition holds trivially while minimality holds exactly when $H$ is trivial, in agreement with the simplicity of $C^*_r(H)$ exactly for the trivial group.

**Example (transformation groupoids).** For a discrete group $H$ acting on a locally compact space $X$, $C^*_r(X\rtimes H) \cong C_0(X)\rtimes_r H$: the groupoid model of the crossed product. Minimality of the groupoid is minimality of the action, topological principality is the topological freeness of the action, and the simplicity theorem becomes the classical criterion for the simplicity of the reduced crossed product of a minimal and topologically free action.

**Example (equivalence relations and matrix algebras).** For the pair groupoid on a finite set with $n$ points, $C^*(G) = C^*_r(G) \cong M_n(\mathbb{C})$, as computed above; for the equivalence relation on a countable set that is the universal relation, $C^*_r(G) \cong K(\ell^2(X))$, the compacts. Both are the $\mathrm{C}^*$-algebraic form of the observation that a principal groupoid records only the cardinality of the equivalence classes; for a general countable equivalence relation the reduced algebra is the approximately finite-dimensional algebra assembled from the finite-dimensional matrix algebras over the classes, and the full and reduced algebras differ exactly for the non-amenable relations.

### Graph Groupoids and Dynamical Groupoids

**Example (graph groupoids).** The graph groupoid $G_E$ of a countable row-finite graph $E$ with no sinks is ample, and $C^*_r(G_E) \cong C^*(E)$; the gauge action of *Graph C*-Algebras* is the action of the circle dual to the "period" cocycle of the groupoid, and the core is the algebra of the groupoid's isotropy-free part. The simplicity, ideal structure and AF/purely infinite dichotomy of graph algebras are the groupoid theorems of the preceding section in this particular case.

**Example (Deaconu–Renault groupoids and Cuntz algebras).** Let $X$ be a locally compact space and let $\sigma : X \to X$ be a local homeomorphism. The **Deaconu–Renault groupoid** has arrows the pairs $(x,n,y)$ with $\sigma^n(x) = y$ and $n \geq 0$ together with their inverses, with the topology inherited from $X$; when $\sigma$ is the one-sided full shift on $\{0,1\}^{\mathbb{N}}$ the resulting algebra is the Cuntz algebra $\mathcal{O}_2$, and more generally the Cuntz–Krieger algebras arise from the groupoids of subshifts of finite type. The examples show that the class of groupoid algebras contains the Cuntz algebras, which are not crossed products of a group action; they are the natural common generalisation of the graph algebras and the crossed products.

**Example (the Weyl groupoid and the rotation algebra).** The rotation algebra $A_\theta$ of *Crossed Products of C*-Algebras* is the groupoid algebra of the transformation groupoid of the rotation action of $\mathbb{Z}$ on $\mathbb{T}$; its unit space is $\mathbb{T}$, its isotropy groups are trivial for irrational $\theta$ and are finite cyclic for rational $\theta$, and the Cartan subalgebra $C(\mathbb{T})$ is the diagonal of the noncommutative torus. The Morita classification of the rotation algebras by $\theta$ up to sign is the classification of their groupoids up to equivalence.

**Remark (the groupoid dictionary).** The following table collects the correspondence between groupoid data and algebra data, as used throughout this article.

| Groupoid data | Algebra data |
|---|---|
| Units $G^{(0)}$ | Cartan subalgebra $C_0(G^{(0)})$ |
| Arrows $G^{(1)}$ | Normalizer of the Cartan subalgebra |
| Fibres $r^{-1}(u)$ | Fibres of the conditional expectation |
| Isotropy groups | Twist and the rigidity data |
| Minimality | Simplicity of $C^*_r(G)$ |
| Effectiveness / topological principality | Faithfulness of the conditional expectation |
| Amenability | $C^*(G) = C^*_r(G)$ and nuclearity |
| Equivalence of groupoids | Morita equivalence of algebras |

---

## Summary

A **groupoid** $G$ is a small category with all arrows invertible: it has a unit space $G^{(0)}$, source and range maps $r,s$, a partially defined associative multiplication on the composable pairs and an inverse, with $x^{-1}x = s(x)$ and $xx^{-1} = r(x)$; a group is the case of one unit, an equivalence relation is the case of trivial isotropy, and the **transformation groupoid** $X\rtimes H$ of a group action and the graph groupoid $G_E$ are the two constructions through which crossed products and graph algebras are recovered. A groupoid is **étale** when the range map is a local homeomorphism; then the fibres are discrete, the counting measure on each fibre is a Haar system, and no measure theory is needed. The **convolution** on $C_c(G)$ is $(f*g)(x) = \sum_{r(y)=r(x)}f(y)g(y^{-1}x)$ with involution $f^*(x) = \overline{f(x^{-1})}$, and this $*$-algebra completes to the **full groupoid algebra** $C^*(G)$, universal for the representations of $C_c(G)$, and to the **reduced groupoid algebra** $C^*_r(G)$ generated by the left regular representation $(\lambda_x\xi)(y) = \xi(x^{-1}y)$, $r(y) = r(x)$, on $\ell^2(G)$; the regular representation induces a quotient map $C^*(G) \to C^*_r(G)$, which is an isomorphism exactly when $G$ is amenable, and $C^*_r(G)$ is then nuclear.

For a topologically principal étale groupoid, $C_0(G^{(0)})$ is a **Cartan subalgebra** of $C^*_r(G)$, the ideals correspond to the open invariant subsets of the unit space, and $C^*_r(G)$ is simple exactly when $G$ is minimal; Renault's reconstruction theorem conversely recovers every separable $\mathrm{C}^*$-algebra with a Cartan subalgebra as the reduced algebra $C^*_r(G,\Sigma)$ of a twisted groupoid. Equivalent groupoids have Morita equivalent algebras. The fundamental computations are the pair groupoid $X\times X$ of a finite set with $n$ elements, whose convolution algebra is $M_n(\mathbb{C})$ with the matrix product and the transpose — verified exactly — the transformation groupoid of a finite action, the quotient relation with $K(\ell^2(X))$, the graph groupoids with $C^*_r(G_E) \cong C^*(E)$, the Deaconu–Renault groupoids with the Cuntz algebras, and the rotation algebras with their Cartan diagonal $C(\mathbb{T})$. The general Haar system and the invariant integration are Part III; the K-theory and classification of groupoid algebras belong .

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $G^{(0)}$, $G^{(2)}$ | Groupoid, unit space, composable pairs |
| $r$, $s$, $x^{-1}$, $xy$ | Range, source, inverse, composition |
| $G_u$, $G^u$ | Isotropy group at $u$; $r$-fibre over $u$ |
| $X\rtimes H$, $G_E$ | Transformation groupoid; graph groupoid |
| $(f*g)$, $f^*$ | Convolution and involution on $C_c(G)$ |
| $C^*(G)$, $C^*_r(G)$ | Full and reduced groupoid $\mathrm{C}^*$-algebras |
| $\lambda$ | Left regular representation on $\ell^2(G)$ |
| $C^*_r(G,\Sigma)$ | Reduced algebra of a twisted groupoid |
| $N(B)$, $E : A \to B$ | Normalizer of a subalgebra; conditional expectation |
| $C_0(G^{(0)})$ | Cartan subalgebra of $C^*_r(G)$ |
| $K(\ell^2(X))$ | Compact operators on a countable set $X$ |



## Further Reading

- Jean Renault, *A Groupoid Approach to $\mathrm{C}^*$-Algebras* (Springer Lecture Notes in Mathematics 793, 1980), for the construction of groupoid $\mathrm{C}^*$-algebras, Haar systems and the amenability theory.
- Jean Renault, "Cartan subalgebras in $\mathrm{C}^*$-algebras", *Irish Mathematical Society Bulletin* **61** (2008), 29–63, for the Cartan subalgebra theory and the reconstruction theorem.
- Alan L. T. Paterson, *Groupoids, Inverse Semigroups, and their Operator Algebras* (Birkhäuser, 1999), for the systematic theory and the inverse-semigroup approach.
- Paul S. Muhly, Jean Renault and Dana P. Williams, "Equivalence and isomorphism for groupoid $\mathrm{C}^*$-algebras", *Journal of Operator Theory* **17** (1987), 3–22, for the equivalence theorem and the Morita theory.
- Alex Kumjian, David Pask and Jean Renault, "Cuntz–Krieger algebras of directed graphs and groupoids", *Houston Journal of Mathematics* **32** (2006), 101–124, for the graph groupoids.
- Valentin Deaconu, "Groupoids associated with endomorphisms", *Transactions of the American Mathematical Society* **347** (1995), 1779–1786, for the Deaconu–Renault groupoids and the Cuntz algebras.
- Dana P. Williams, *A Tool Kit for Groupoid $\mathrm{C}^*$-Algebras* (American Mathematical Society, 2019), for the modern account of the theory, including the twisted case.
- Ronald Brown, *Topology and Groupoids* (BookSurge, 2006), for the general theory of groupoids, their topology and their covering theory.
