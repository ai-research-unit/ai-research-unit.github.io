
# __Transformation Groups__

## Introduction

A group is an abstract object: a set with an associative multiplication, an identity and inverses. The reason groups occur throughout mathematics is that they are *realised*: the elements of a group can be exhibited as transformations of some set, and the group multiplication then becomes composition of transformations. This article develops that realisation, which is the common thread running through the whole category. We treat transformations of a bare set, automorphisms of a set carrying structure, group actions as homomorphisms into a symmetric group, and the three levels at which a group is realised: as permutations of a set, as invertible linear maps of a module, and as invertible linear maps preserving a form.

Throughout, $R$ denotes a commutative ring with identity $1 \neq 0$ and $F$, $K$ denote fields, unless a statement says otherwise; $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$ when only those two are meant. The corpus default base is the commutative ring, so module statements below are made over $R$; where a field, characteristic zero, or the invertibility of $2$ is needed, this is said explicitly. No physics is invoked: a symmetry group here is a group of transformations of a mathematical object, never of a physical system.

The elementary theory of groups — associativity, order and powers, subgroups, homomorphisms, cosets, normal subgroups and the isomorphism theorems — is assumed from *Groups*, and the notation of that article is kept. Two companion articles, *Group Actions and Structure* and *Generators, Presentations and Free Products*, are being written in parallel with this one and deepen, respectively, the orbit-theoretic and the combinatorial sides of the material introduced here.

## Transformations of a Set

### Transformations and Composition

**Definition.** A **transformation** of a set $X$ is a function $f : X \to X$. Transformations compose: if $f$ and $g$ are transformations of $X$, then so is $g \circ f$, defined by $(g \circ f)(x) = g(f(x))$. Composition of functions is associative,

$$
h \circ (g \circ f) = (h \circ g) \circ f,
$$

and the identity map $\mathrm{id}_X$ satisfies $\mathrm{id}_X \circ f = f \circ \mathrm{id}_X = f$.

**Definition.** A transformation $f$ is **invertible** if there is a transformation $g$ with $g \circ f = \mathrm{id}_X = f \circ g$, and $g$ is then unique, written $f^{-1}$.

**Proposition.** A transformation is invertible if and only if it is bijective.

**Proof.** If $f$ is invertible with inverse $g$, then $f(x) = f(y)$ gives $x = g(f(x)) = g(f(y)) = y$, so $f$ is injective, and for any $z$ one has $z = f(g(z))$, so $f$ is surjective. Conversely, if $f$ is bijective, define $g(z)$ to be the unique $x$ with $f(x) = z$; then $g \circ f = \mathrm{id}_X$ and $f \circ g = \mathrm{id}_X$. $\square$

**Proposition.** If $f$ and $g$ are invertible, then $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$.

**Proof.** $(f^{-1} \circ g^{-1}) \circ (g \circ f) = f^{-1} \circ (g^{-1} \circ g) \circ f = f^{-1} \circ f = \mathrm{id}_X$, and similarly on the other side. $\square$

The reversal of order is the reason a group of transformations acts on the left in one convention and on the right in another; the point is taken up again after the symmetric group is defined.

### The Symmetric Group

**Definition.** For a set $X$, the **symmetric group** $\operatorname{Sym}(X)$ is the set of all bijections $X \to X$ with composition as the operation and $\mathrm{id}_X$ as identity.

That $\operatorname{Sym}(X)$ is a group is the content of the propositions above: composition is associative, the identity is invertible, and the inverse of an invertible transformation is invertible. When $X = \{1, 2, \ldots, n\}$ we write $S_n = \operatorname{Sym}(\{1, \ldots, n\})$, of order $n!$.

**Proposition.** $\operatorname{Sym}(X)$ is abelian if and only if $|X| \leq 2$.

**Proof.** If $|X| \leq 2$ there are at most two bijections and they commute. If $X$ contains three distinct elements $a, b, c$, let $f$ interchange $a$ and $b$ and fix $c$, and let $g$ interchange $b$ and $c$ and fix $a$. Then $g(f(a)) = g(b) = c$ while $f(g(a)) = f(a) = b$, so $f \circ g \neq g \circ f$. $\square$

**Remark.** The group $\operatorname{Sym}(X)$ depends only on the cardinality of $X$: a bijection $\varphi : X \to Y$ induces an isomorphism $\operatorname{Sym}(X) \to \operatorname{Sym}(Y)$, $f \mapsto \varphi \circ f \circ \varphi^{-1}$. Consequently the labelling of a finite set is a convention and carries no group-theoretic content, a fact used silently whenever one writes $S_n$.

### Right Actions and the Opposite Group

Composition is written on the left, so that $g \circ f$ means "first $f$, then $g$". With this convention a transformation group acts on the left of $X$. If instead one writes functions on the right, $x f$ for $f(x)$, then $(x f) g = x (f \circ g)$, and the multiplication is read in the opposite order. This is the difference between a **left action** and a **right action**, and it is a convention rather than a mathematical distinction: the **opposite group** $G^{\mathrm{op}}$ has the same underlying set as $G$ and multiplication $a \cdot b = b a$, and a right action of $G$ is a left action of $G^{\mathrm{op}}$. All actions in this article are left actions, and all products are read from left to right in the usual group notation.

## Automorphisms of a Structure

### Structures and Their Automorphisms

A **structure** on a set $X$ is any collection of distinguished data attached to $X$: distinguished elements, distinguished subsets, operations, or relations. The bijections of $X$ that preserve all of the data form the **automorphism group** of the structure.

**Definition.** Let $X$ carry a structure. A bijection $\sigma : X \to X$ is an **automorphism** of the structure if $\sigma$ and $\sigma^{-1}$ preserve every piece of the data. The automorphisms form a group under composition, written $\operatorname{Aut}(X)$, and $\operatorname{Aut}(X) \leq \operatorname{Sym}(X)$.

The verification that $\operatorname{Aut}(X)$ is a subgroup of $\operatorname{Sym}(X)$ is formal: the identity preserves the data, a composition of two bijections preserving the data preserves the data, and the inverse of a preserving bijection preserves the data by definition. The content lies in the examples, where "preserve the data" is spelled out.

**Example.** Let $X$ be a set with a single relation, say a partial order $\leq$. An automorphism is a bijection $\sigma$ with $x \leq y \iff \sigma(x) \leq \sigma(y)$, the **order automorphisms**. For a chain such as $\mathbb{Q}$ with its order, the order automorphisms are far more numerous than the identity.

**Example.** Let $X$ be a graph, a set with a set of two-element subsets, the edges. An automorphism is a bijection permuting vertices that maps edges to edges and non-edges to non-edges. For the complete graph on $n$ vertices every bijection qualifies, so $\operatorname{Aut}(K_n) = S_n$, whereas for a path with $n \geq 2$ vertices there are exactly two automorphisms.

**Example.** Let $X = G$ be a group. An automorphism of the group structure is a bijection $\sigma$ with $\sigma(ab) = \sigma(a)\sigma(b)$ for all $a, b \in G$, and these form the group $\operatorname{Aut}(G)$ of *Groups*, §5. For each $u \in G$ the conjugation $c_u(x) = u x u^{-1}$ is an automorphism, the map $u \mapsto c_u$ has image the normal subgroup $\operatorname{Inn}(G)$ of inner automorphisms, and $\operatorname{Inn}(G) \cong G / Z(G)$.

**Example.** Let $X = V$ be a left $R$-module. An automorphism of the module structure is a bijective $R$-linear map $V \to V$; the group is written $\operatorname{Aut}_R(V)$ and is the general linear group $GL(V)$ of the module. Its elements preserve addition and scalar multiplication and nothing more.

**Example.** Let $X$ be a topological space. An automorphism of the topology is a bijection $\sigma$ with $\sigma(U)$ open for every open $U$ and $\sigma^{-1}(U)$ open for every open $U$, that is, a **homeomorphism** of $X$ onto itself.

**Example.** Let $X$ be a set with no structure at all. Every bijection is an automorphism, so $\operatorname{Aut}(X) = \operatorname{Sym}(X)$. The symmetric group is thus the automorphism group of the weakest structure and the largest group of transformations of $X$.

**Remark.** Adding structure can only shrink the group of automorphisms:

$$
\operatorname{Aut}(X, \text{structure}) \leq \operatorname{Sym}(X).
$$

This monotonicity in the structure is the organising principle of the three levels treated later in the article.

### Automorphisms and Endomorphisms

Dropping invertibility gives a larger object. An **endomorphism** of a structure $X$ is a map $X \to X$ preserving the data, and the endomorphisms form a monoid under composition, written $\operatorname{End}(X)$: composition is associative and $\mathrm{id}_X$ is a two-sided identity, but a general endomorphism need not be invertible. The invertible elements of a monoid form a group, and

$$
\operatorname{Aut}(X) = \operatorname{End}(X)^\times.
$$

For a module $V$ this reads $\operatorname{Aut}_R(V) = \operatorname{End}_R(V)^\times$: the invertible linear maps are the units of the endomorphism ring. Invertibility is not automatic for a self-map of a set: for a finite set a self-map is injective exactly when it is surjective, whereas for an infinite set injectivity is strictly weaker, the map $x \mapsto x + 1$ of $\mathbb{N}$ being injective and not surjective, hence an endomorphism of $\mathbb{N}$ that is not an automorphism.

## Actions of Groups

### Definition

The abstract group and the concrete transformation group are related by the notion of an action.

**Definition.** Let $G$ be a group and $X$ a set. A **(left) action** of $G$ on $X$ is a function

$$
G \times X \to X, \qquad (a, x) \mapsto a \cdot x,
$$

such that $e \cdot x = x$ and $(a b) \cdot x = a \cdot (b \cdot x)$ for all $a, b \in G$ and all $x \in X$. One says that $G$ **acts on** $X$, or that $X$ is a $G$-set.

**Proposition.** An action of $G$ on $X$ is the same thing as a homomorphism $\rho : G \to \operatorname{Sym}(X)$.

**Proof.** Given an action, define $\rho(a)(x) = a \cdot x$. For fixed $a$, the map $\rho(a)$ is bijective with inverse $\rho(a^{-1})$, since $\rho(a^{-1})\rho(a)(x) = (a^{-1}a)\cdot x = x$ and likewise on the other side. The action axiom says exactly that $\rho(ab) = \rho(a) \circ \rho(b)$, so $\rho$ is a homomorphism. Conversely, given a homomorphism $\rho$, put $a \cdot x = \rho(a)(x)$; then $e \cdot x = \mathrm{id}_X(x) = x$ and $(ab)\cdot x = \rho(ab)(x) = \rho(a)(\rho(b)(x)) = a \cdot (b \cdot x)$. $\square$

The homomorphism $\rho$ is the **permutation representation** attached to the action, or the **transformation group** that the action realises. The image $\rho(G) \leq \operatorname{Sym}(X)$ is a group of transformations of $X$, and the action is precisely a way of presenting an abstract group as such a group; this is the sense in which every action is a concrete realisation.

**Example.** The **trivial action** $a \cdot x = x$ has image $\{e\}$.

**Example.** The **left regular action** of $G$ on its underlying set is $a \cdot x = a x$. The homomorphism $G \to \operatorname{Sym}(G)$ it defines is injective, as is shown below.

**Example.** The **conjugation action** of $G$ on itself is $a \cdot x = a x a^{-1}$. Its image is $\operatorname{Inn}(G)$.

**Example.** The **coset action** on $G/H$ for a subgroup $H$ is $a \cdot (x H) = (a x) H$; it is defined for any subgroup $H$, normal or not, and the formula is independent of the representative: if $x' = x h$ with $h \in H$, then $a x' H = a x h H = a x H$.

**Example.** The **natural action** of $S_n$ on $\{1, \ldots, n\}$, and its induced action on $k$-element subsets.

**Example.** The action of $GL(V)$ on the module $V$ by evaluation, and its induced action on the set of lines, that is, on the one-dimensional submodules, and on the set of subspaces of any fixed dimension.

### Faithful Actions and the Kernel

**Definition.** The **kernel** of an action of $G$ on $X$ is the kernel of the associated homomorphism $\rho : G \to \operatorname{Sym}(X)$:

$$
\ker \rho = \{a \in G : a \cdot x = x \ \text{for all } x \in X\}.
$$

The action is **faithful**, or **effective**, if $\ker \rho = \{e\}$, that is, if $\rho$ is injective.

By the first isomorphism theorem the image $\rho(G)$ is isomorphic to $G / \ker \rho$, so an action with kernel $K$ gives a faithful action of $G/K$ on the same set. Every action therefore decomposes into a trivially-acting normal subgroup and a faithful action of the quotient, and the study of actions reduces at once to the faithful case.

**Example.** The left regular action is faithful. Indeed, if $a \cdot x = x$ for all $x$, taking $x = e$ gives $a = e$.

**Example.** The conjugation action has kernel $Z(G)$, and its image is $\operatorname{Inn}(G) \cong G/Z(G)$. In particular, the conjugation action is faithful if and only if $G$ has trivial centre, as for $S_n$ with $n \geq 3$.

**Example.** The action of $GL_n(F)$ on $F^n$ has kernel the scalar matrices $\{a I : a \in F^\times\}$, so the projective general linear group is $PGL_n(F) = GL_n(F)/F^\times$, the group acting faithfully on the lines of $F^n$.

### Orbits and Stabilisers

Two notions are attached to a $G$-set $X$ and a point $x \in X$.

**Definition.** The **orbit** of $x$ is $\operatorname{Orb}(x) = \{a \cdot x : a \in G\}$, and the **stabiliser** of $x$ is

$$
\operatorname{Stab}(x) = \{a \in G : a \cdot x = x\}.
$$

The orbit is a subset of $X$; the stabiliser is a subgroup of $G$. The relation $x \sim y$ defined by $y \in \operatorname{Orb}(x)$ is an equivalence relation, since $x = e \cdot x$, since $y = a \cdot x$ gives $x = a^{-1} \cdot y$, and since $y = a \cdot x$, $z = b \cdot y$ give $z = (ba) \cdot x$. Hence the orbits partition $X$, and $X$ is the disjoint union of its orbits.

If $X$ has a single orbit the action is **transitive**; if in addition every point stabiliser is trivial, so that $G$ acts on $X$ freely as well as transitively, the action is **sharply transitive**, and then $X$ may be identified with the underlying set of $G$. The systematic theory of orbits and stabilisers, the orbit–stabiliser theorem and its consequences for the structure of a finite group, is the subject of the companion article *Group Actions and Structure*.

### Equivariant Maps and Isomorphism of Actions

**Definition.** Let $X$ and $Y$ be $G$-sets. A map $\varphi : X \to Y$ is **$G$-equivariant**, or a **map of $G$-sets**, if $\varphi(a \cdot x) = a \cdot \varphi(x)$ for all $a \in G$, $x \in X$. An invertible equivariant map is an **isomorphism of $G$-sets**.

The $G$-sets and their equivariant maps form a category, and the structural theorem of the category is that every transitive $G$-set is isomorphic to a coset $G$-set $G/H$: choose $x \in X$, let $H = \operatorname{Stab}(x)$, and let $\varphi : G/H \to X$ be $\varphi(a H) = a \cdot x$. This map is well defined, equivariant and bijective, the last by transitivity and the injectivity computation of the orbit–stabiliser theorem. An arbitrary $G$-set is the disjoint union of its orbits, each of which is such a coset space; thus the $G$-sets are exactly the disjoint unions of coset spaces $G/H$.

## Cayley's Theorem and the Permutation Representation

**Theorem (Cayley).** Every group $G$ is isomorphic to a subgroup of $\operatorname{Sym}(G)$. In particular, every finite group of order $n$ embeds in $S_n$.

**Proof.** Let $\rho : G \to \operatorname{Sym}(G)$ be the left regular representation, $\rho(a)(x) = a x$. It is a homomorphism by associativity, and it is injective because $\rho(a) = \mathrm{id}$ forces $a = a e = e$. Hence $G \cong \rho(G) \leq \operatorname{Sym}(G)$. Labelling the $n$ elements of a finite $G$ gives $\operatorname{Sym}(G) \cong S_n$. $\square$

Cayley's theorem is the precise sense in which abstract groups and transformation groups are the same subject: the data of an abstract group is nothing more than the data of a set with a sharply transitive group of transformations, but the abstract axioms are what make the notion portable between different sets. The theorem also has a practical role: any statement about groups that can be phrased in terms of permutations may be proved by embedding the group in a symmetric group, the standard route to Cauchy's theorem and to the Sylow theorems.

**Remark.** Two cautions attach to Cayley's theorem. First, the embedding $G \hookrightarrow S_{|G|}$ is far from efficient: $S_{|G|}$ has order $|G|!$, and a much smaller faithful permutation representation often exists, the smallest degree being a genuine invariant of $G$. Second, Cayley's theorem concerns the *underlying set* of $G$ and uses no structure: the left regular action is free, so it forgets the internal structure of $G$ entirely, which is why it proves general facts but computes nothing.

**Remark.** The permutation representation is not the only realisation. The **right regular action** $a \cdot x = x a$ is a right action, equivalently a left action of the opposite group; and for any subgroup $H$ the coset action realises $G$ as a group of permutations of the smaller set $G/H$, with kernel the **core** $\bigcap_{a \in G} a H a^{-1}$, the largest subgroup of $H$ normal in $G$.

## Symmetry Groups of Figures

### Figures and Their Symmetries

A **figure** in $\mathbb{K}^n$ is a subset $\Phi \subseteq \mathbb{K}^n$; for instance a polygon, a curve, or a finite point set. Its symmetries are the transformations of the ambient space preserving both the figure and the relevant structure of the space.

**Definition.** The **linear symmetry group** of a figure $\Phi \subseteq \mathbb{K}^n$ is

$$
G_\Phi = \{A \in O(n, \mathbb{K}) : A\Phi = \Phi\},
$$

where $O(n, \mathbb{K})$ is the group of invertible linear maps preserving the standard bilinear form $g(x, y) = \sum_i x_i y_i$, in the real case $O(n) = O(n, \mathbb{R})$. This is a subgroup of $O(n, \mathbb{K})$, being the stabiliser of the subset $\Phi$ under the action of $O(n, \mathbb{K})$ on the power set of $\mathbb{K}^n$; the subscript keeps the notation apart from the symmetric group $\operatorname{Sym}(X)$ of bijections of a set.

Symmetries that involve translations, such as the reflections of a figure not containing the origin, are isometries of an affine space; these are treated with the affine group in the companion category and are not needed here. Every figure may be translated so that its centroid is at the origin, after which its symmetry group is the linear one above.

### The Symmetry Group of the Regular Polygon

Let $n \geq 3$ and let $P_n \subseteq \mathbb{R}^2$ be the regular $n$-gon with vertices on the unit circle at angles $2\pi k / n$. Its linear symmetry group is the **dihedral group** $D_n$.

**Proposition.** The symmetry group of $P_n$ consists of $n$ rotations and $n$ reflections, so $|D_n| = 2n$.

**Proof.** A linear symmetry $A$ preserves the centre, which is the origin, and preserves the set of vertices, the extreme points of the convex hull. The vertices form a regular $n$-gon, and a symmetry is determined by the image of one vertex together with the orientation. There are $n$ possible images for a chosen vertex and two possible orientations, so $|D_n| \leq 2n$; the $n$ rotations of the circle group preserving the vertex set and the $n$ reflections $\theta \mapsto 2\pi k/n - \theta$ supply $2n$ distinct elements. $\square$

The rotations form the cyclic subgroup $C_n \cong \mathbb{Z}/n\mathbb{Z}$, normal of index $2$. Writing $r$ for the rotation through $2\pi/n$ and $s$ for the reflection in the $x$-axis,

$$
D_n = \langle r, s \mid r^n = s^2 = e, \ s r s = r^{-1} \rangle,
$$

and every element is uniquely $r^i s^j$ with $0 \leq i < n$, $j \in \{0, 1\}$; the group is the semidirect product $C_n \rtimes C_2$ with $C_2$ acting by inversion. The finite dihedral groups are treated again, with their conjugacy classes and subgroups, in the applications article *Finite Groups and Symmetry*.

### The Symmetry Groups of the Platonic Solids

The linear symmetry group of each Platonic solid may be computed by permuting the vertices it is the convex hull of, and the rotation group acts faithfully on the vertex set. The identification with the symmetric or alternating group is read off from a faithful action on four or five objects: the rotations of the tetrahedron permute the four vertices, those of the cube permute the four space diagonals, and those of the icosahedron permute the five tetrahedra inscribed in it, dual to the five cubes inscribed in the dodecahedron.

| Solid | Vertex set | Rotations | Full symmetry group |
|---|---|---|---|
| Tetrahedron | $4$ vertices | $12 \cong A_4$ | $24 \cong S_4$ |
| Cube, octahedron | dual; $8$ and $6$ vertices | $24 \cong S_4$ | $48 \cong S_4 \times C_2$ |
| Dodecahedron, icosahedron | dual; $20$ and $12$ vertices | $60 \cong A_5$ | $120 \cong A_5 \times C_2$ |

The orders are the numbers of signed permutation matrices preserving the corresponding figure in suitable coordinates; for the cube the rotations are the $24$ signed permutation matrices of determinant $1$. The finite rotation groups of $\mathbb{R}^3$ are exactly the rotational symmetry groups of these solids together with the cyclic and dihedral groups, a classification stated and used in *Finite Groups and Symmetry*.

### Finite Subgroups of $O(2)$

The classification of the planar case is short enough to give in full, and it exhibits the two families that recur in the applications.

**Theorem.** A finite subgroup of $O(2)$ is cyclic $C_n$ or dihedral $D_n$.

**Proof.** Let $G \leq O(2)$ be finite and let $H = G \cap SO(2)$, the subgroup of elements of determinant $1$. Under the identification of $SO(2)$ with the unit circle $\{e^{i\theta}\}$, a finite subgroup is cyclic: if $\theta_0$ is the smallest positive angle occurring, then for any angle $\theta$ in $H$, division with remainder gives $\theta = k\theta_0 + \rho$ with $0 \leq \rho < \theta_0$, and $\rho \in H$ because $e^{i\theta}(e^{i\theta_0})^{-k} \in H$, so $\rho = 0$ by minimality of $\theta_0$. Hence $H = C_n$ for some $n \geq 1$, generated by the rotation through $\theta_0 = 2\pi/n$. If $G = H$ the group is cyclic. Otherwise $G$ contains a reflection $s$; the composite $s \cdot h$ has determinant $-1$, so the determinant homomorphism $G \to \{\pm 1\}$ is surjective, $H$ is its kernel and therefore normal of index $2$, and $G = H \rtimes \langle s \rangle$ with $s^2 = e$. Conjugation by $s$ inverts the rotation, so $G \cong D_n$. $\square$

## The Three Levels

The realisation of a group as a transformation group is always with respect to a choice of structure on the set $X$, and the richer the structure, the smaller the group. There are three levels that matter for the later articles of the corpus.

### Transformations of a Set

At the first level $X$ is a bare set and the structure is empty, so every bijection is an automorphism, the group is $\operatorname{Sym}(X)$, and by Cayley's theorem every group occurs. This level is universal and has no invariant theory: there is nothing for a transformation to preserve, so no classification beyond the cardinality of $X$ is possible.

### Transformations of a Linear Space

At the second level $X = V$ is a left $R$-module and the structure consists of addition and the action of $R$, so an automorphism is a bijective $R$-linear map and the group is

$$
GL(V) = \operatorname{Aut}_R(V) \leq \operatorname{Sym}(V).
$$

After a choice of basis of a free module of rank $n$, this is the group of invertible $n \times n$ matrices, and the determinant is a homomorphism $\det : GL_n(F) \to F^\times$ for $V = F^n$ with $F$ a field. The linear structure is enough to make the group computable: kernels, images, eigenvalues and the rank–nullity theorem are available. The linear groups themselves, and the determinant, belong to the companion category on linear spaces; here only their place in the three-level picture is needed.

### Transformations Preserving a Form

At the third level the module carries, besides its linear structure, a form: a bilinear form $g$, a Hermitian form $h$, or an alternating form $\omega$. An automorphism must then preserve both the module structure and the form, so the group is smaller again.

**Definition.** Let $V$ be a free $F$-module of finite rank and let $g$ be a bilinear form on $V$. The **orthogonal group** of $g$ is

$$
O(V, g) = \{A \in GL(V) : g(Au, Av) = g(u, v) \ \text{for all } u, v \in V\}.
$$

If instead $h$ is a Hermitian form on a complex vector space, the **unitary group** is $U(V, h) = \{A \in GL(V) : h(Au, Av) = h(u, v)\}$; and if $\omega$ is a nondegenerate alternating form, the **symplectic group** is $Sp(V, \omega) = \{A \in GL(V) : \omega(Au, Av) = \omega(u, v)\}$. Each is a subgroup of $GL(V)$ because the form is preserved by a composite and by an inverse when it is preserved by a map.

For a quadratic form $q$ on $V$, whose associated bilinear form is $g_q(u, v) = q(u + v) - q(u) - q(v)$, preserving $q$ is the stronger condition, and the corresponding group is written $O(V, q)$; over a field of characteristic different from $2$ one has $q(u) = \tfrac{1}{2} g_q(u, u)$ and the two conditions agree, so that this is exactly where the invertibility of $2$ is required. In matrix form, with $\Gamma$ the matrix of the form in a basis, the defining condition is

$$
A^{*} \Gamma A = \Gamma
$$

in all three cases, the star being transposition for the bilinear forms on a real or general field and conjugate transposition for the Hermitian form; $\Gamma$ is symmetric, Hermitian or alternating according to the case. The three families $O$, $U$, $Sp$, and the low-dimensional isomorphisms among them such as $Sp(1) \cong SU(2)$, are the subject of the companion applications article *Matrix Groups and Classical Groups*, written in parallel; the point here is only their position at the third level.

### The Three Levels Compared

| Level | Structure on the object | Group | What is preserved |
|---|---|---|---|
| $1$ | none; $X$ a set | $\operatorname{Sym}(X)$ | nothing but the cardinality |
| $2$ | linear; $V$ an $R$-module | $GL(V) = \operatorname{Aut}_R(V)$ | addition and scalar multiplication |
| $3$ | linear plus a form | $O(V, g)$, $U(V, h)$, $Sp(V, \omega)$ | the linear structure and the form |

The inclusions

$$
O(V, g),\ U(V, h),\ Sp(V, \omega) \ \leq \ GL(V) \ \leq \ \operatorname{Sym}(V)
$$

and, for an abstract group $G$, the Cayley embedding $G \hookrightarrow \operatorname{Sym}(G)$, are all instances of one principle: a transformation group is determined by what it is required to preserve, and more structure means fewer automorphisms. The three levels are those at which the corpus uses the principle: permutations of a set, invertible linear maps, and isometries of a form.

## Summary

A transformation of a set $X$ is a function $X \to X$, and the invertible transformations form the symmetric group $\operatorname{Sym}(X)$ under composition. A structure on $X$ selects a subgroup $\operatorname{Aut}(X) \leq \operatorname{Sym}(X)$ of automorphisms, and $\operatorname{Aut}(X) = \operatorname{End}(X)^\times$ is the group of units of the endomorphism monoid. Adding structure shrinks the group.

An action of a group $G$ on $X$ is a function $G \times X \to X$ with $e \cdot x = x$ and $(ab)\cdot x = a \cdot (b \cdot x)$, equivalently a homomorphism $\rho : G \to \operatorname{Sym}(X)$, the permutation representation. The action is faithful when $\rho$ is injective; in general the image is $G/\ker\rho$, so every action is a faithful action of a quotient. The orbits partition $X$, the stabilisers are subgroups, and every transitive $G$-set is isomorphic to a coset space $G/H$ with $H$ a point stabiliser.

Cayley's theorem, that $G$ embeds in $\operatorname{Sym}(G)$ by the left regular representation, identifies abstract groups with transformation groups of their own underlying sets. The symmetry group of a figure is the stabiliser of that figure in the relevant transformation group; for the regular $n$-gon it is the dihedral group of order $2n$, and the finite subgroups of $O(2)$ are exactly the cyclic and dihedral groups. Finally, groups of transformations occur at three levels — permutations of a set, invertible linear maps of a module, and invertible linear maps preserving a form — and the groups $GL$, then $O$, $U$, $Sp$, are obtained by successively requiring more to be preserved.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X$, $Y$ | Sets, or structured sets, on which transformations act |
| $\mathrm{id}_X$ | Identity transformation of $X$ |
| $\operatorname{Sym}(X)$ | Symmetric group of all bijections $X \to X$ |
| $G_\Phi$ | Linear symmetry group of a figure $\Phi \subseteq \mathbb{K}^n$, a subgroup of $O(n, \mathbb{K})$ |
| $S_n$ | $\operatorname{Sym}(\{1, \ldots, n\})$; order $n!$ |
| $G^{\mathrm{op}}$ | Opposite group, multiplication $a \cdot b = b a$ |
| $\operatorname{Aut}(X)$ | Group of automorphisms of a structure on $X$ |
| $\operatorname{End}(X)$ | Monoid of endomorphisms; $\operatorname{Aut}(X) = \operatorname{End}(X)^\times$ |
| $\operatorname{Aut}(G)$, $\operatorname{Inn}(G)$ | Group automorphisms, inner automorphisms; $\operatorname{Inn}(G) \cong G/Z(G)$ |
| $G \times X \to X$, $a \cdot x$ | Left action of $G$ on $X$ |
| $\rho : G \to \operatorname{Sym}(X)$ | Permutation representation of an action |
| $\ker \rho$ | Kernel of an action; trivial precisely when the action is faithful |
| $\operatorname{Orb}(x)$ | Orbit of $x$ |
| $\operatorname{Stab}(x)$ | Stabiliser of $x$; $x \sim y \iff y \in \operatorname{Orb}(x)$ partitions $X$ |
| $G/H$ | Coset space, a transitive $G$-set |
| $P_n$, $D_n$ | Regular $n$-gon and its symmetry group, of order $2n$ |
| $O(n, \mathbb{K})$, $O(n)$ | Orthogonal group of the standard bilinear form; $O(n) = O(n, \mathbb{R})$ |
| $g$, $q$, $h$, $\omega$ | Bilinear form, quadratic form, Hermitian form, alternating form |
| $GL(V) = \operatorname{Aut}_R(V)$ | General linear group of a module |
| $O(V, g)$, $U(V, h)$, $Sp(V, \omega)$ | Groups of invertible linear maps preserving a form |
| $G \hookrightarrow \operatorname{Sym}(G)$ | Cayley embedding by the left regular action |

## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991), for transformation groups and the symmetry of figures treated concretely.
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004), for group actions, Cayley's theorem and the standard examples.
- Joseph J. Rotman, *An Introduction to the Theory of Groups* (Springer, 4th ed. 1995), for a systematic treatment of permutation representations and group actions.
- John S. Rose, *A Course on Group Theory* (Dover, 1994), for the orbit decomposition and coset spaces developed from first principles.
- Derek J. S. Robinson, *A Course in the Theory of Groups* (Springer, 2nd ed. 1996), for group actions as a structural tool.
- John D. Dixon and Brian Mortimer, *Permutation Groups* (Springer, Graduate Texts in Mathematics 163, 1996), for faithful actions of small degree and permutation group theory.
- Larry C. Grove, *Classical Groups and Geometric Algebra* (American Mathematical Society, Graduate Studies in Mathematics 39, 2002), for the groups $O$, $U$, $Sp$ defined by forms.
