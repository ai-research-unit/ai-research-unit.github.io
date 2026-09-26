
# __Transformation Groups__

## Introduction

A group is an abstract object: a set with an associative multiplication, an identity and inverses. The reason groups occur throughout mathematics is that they are *realised*: the elements of a group can be exhibited as transformations of some set, and the group multiplication then becomes composition of transformations. This article develops that realisation, which is the common thread running through the whole category. We treat transformations of a bare set, automorphisms of a set carrying structure, group actions as homomorphisms into a symmetric group, and the principle that a group of automorphisms is determined by what it is required to preserve.

Throughout, $R$ denotes a commutative ring with identity $1 \neq 0$ and $F$, $K$ denote fields, unless a statement says otherwise. No physics is invoked: a transformation group here is a group of transformations of a mathematical object, never of a physical system.

The elementary theory of groups — associativity, order and powers, subgroups, homomorphisms, cosets, normal subgroups and the isomorphism theorems — is assumed from *Groups*, and the notation of that article is kept. Two companion articles are written with this one and deepen, respectively, the orbit-theoretic and the combinatorial sides of the material introduced here.

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

**Example.** Let $X$ be a set with a single relation, say a partial order $\leq$. An automorphism is a bijection $\sigma$ with $x \leq y \iff \sigma(x) \leq \sigma(y)$, the **order automorphisms**. For a chain such as $\mathbb{Z}$ with its order, the order automorphisms are far more numerous than the identity.

**Example.** Let $X$ be a graph, a set with a set of two-element subsets, the edges. An automorphism is a bijection permuting vertices that maps edges to edges and non-edges to non-edges. For the complete graph on $n$ vertices every bijection qualifies, so $\operatorname{Aut}(K_n) = S_n$, whereas for a path with $n \geq 2$ vertices there are exactly two automorphisms.

**Example.** Let $X = G$ be a group. An automorphism of the group structure is a bijection $\sigma$ with $\sigma(ab) = \sigma(a)\sigma(b)$ for all $a, b \in G$, and these form the group $\operatorname{Aut}(G)$ of *Groups*, §5. For each $u \in G$ the conjugation $c_u(x) = u x u^{-1}$ is an automorphism, the map $u \mapsto c_u$ has image the normal subgroup $\operatorname{Inn}(G)$ of inner automorphisms, and $\operatorname{Inn}(G) \cong G / Z(G)$.

**Example.** Let $X$ be a set with no structure at all. Every bijection is an automorphism, so $\operatorname{Aut}(X) = \operatorname{Sym}(X)$. The symmetric group is thus the automorphism group of the weakest structure and the largest group of transformations of $X$.

**Remark.** Adding structure can only shrink the group of automorphisms:

$$
\operatorname{Aut}(X, \text{structure}) \leq \operatorname{Sym}(X).
$$

This monotonicity in the structure is the organising principle of the article.

### Automorphisms and Endomorphisms

Dropping invertibility gives a larger object. An **endomorphism** of a structure $X$ is a map $X \to X$ preserving the data, and the endomorphisms form a monoid under composition, written $\operatorname{End}(X)$: composition is associative and $\mathrm{id}_X$ is a two-sided identity, but a general endomorphism need not be invertible. The invertible elements of a monoid form a group, and

$$
\operatorname{Aut}(X) = \operatorname{End}(X)^\times.
$$

Invertibility is not automatic for a self-map of a set: for a finite set a self-map is injective exactly when it is surjective, whereas for an infinite set injectivity is strictly weaker, the map $x \mapsto x + 1$ of $\mathbb{N}$ being injective and not surjective, hence an endomorphism of $\mathbb{N}$ that is not an automorphism.

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

**Example.** The action of a group $G$ on the set of its subgroups by conjugation, $a \cdot H = a H a^{-1}$, and its induced action on the set of subgroups of any fixed order.

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

If $X$ has a single orbit the action is **transitive**; if in addition every point stabiliser is trivial, so that $G$ acts on $X$ freely as well as transitively, the action is **sharply transitive**, and then $X$ may be identified with the underlying set of $G$. The systematic theory of orbits and stabilisers, the orbit–stabiliser theorem and its consequences for the structure of a finite group, is not covered here.

### Equivariant Maps and Isomorphism of Actions

**Definition.** Let $X$ and $Y$ be $G$-sets. A map $\varphi : X \to Y$ is **$G$-equivariant**, or a **map of $G$-sets**, if $\varphi(a \cdot x) = a \cdot \varphi(x)$ for all $a \in G$, $x \in X$. An invertible equivariant map is an **isomorphism of $G$-sets**.

The $G$-sets and their equivariant maps form a category, and the structural theorem of the category is that every transitive $G$-set is isomorphic to a coset $G$-set $G/H$: choose $x \in X$, let $H = \operatorname{Stab}(x)$, and let $\varphi : G/H \to X$ be $\varphi(a H) = a \cdot x$. This map is well defined, equivariant and bijective, the last by transitivity and the injectivity computation of the orbit–stabiliser theorem. An arbitrary $G$-set is the disjoint union of its orbits, each of which is such a coset space; thus the $G$-sets are exactly the disjoint unions of coset spaces $G/H$.

## Cayley's Theorem and the Permutation Representation

**Theorem (Cayley).** Every group $G$ is isomorphic to a subgroup of $\operatorname{Sym}(G)$. In particular, every finite group of order $n$ embeds in $S_n$.

**Proof.** Let $\rho : G \to \operatorname{Sym}(G)$ be the left regular representation, $\rho(a)(x) = a x$. It is a homomorphism by associativity, and it is injective because $\rho(a) = \mathrm{id}$ forces $a = a e = e$. Hence $G \cong \rho(G) \leq \operatorname{Sym}(G)$. Labelling the $n$ elements of a finite $G$ gives $\operatorname{Sym}(G) \cong S_n$. $\square$

Cayley's theorem is the precise sense in which abstract groups and transformation groups are the same subject: the data of an abstract group is nothing more than the data of a set with a sharply transitive group of transformations, but the abstract axioms are what make the notion portable between different sets. The theorem also has a practical role: any statement about groups that can be phrased in terms of permutations may be proved by embedding the group in a symmetric group, the standard route to Cauchy's theorem and to the Sylow theorems.

**Remark.** Two cautions attach to Cayley's theorem. First, the embedding $G \hookrightarrow S_{|G|}$ is far from efficient: $S_{|G|}$ has order $|G|!$, and a much smaller faithful permutation representation often exists, the smallest degree being a genuine invariant of $G$. Second, Cayley's theorem concerns the *underlying set* of $G$ and uses no structure: the left regular action is free, so it forgets the internal structure of $G$ entirely, which is why it proves general facts but computes nothing.

**Remark.** The permutation representation is not the only realisation. The **right regular action** $a \cdot x = x a$ is a right action, equivalently a left action of the opposite group; and for any subgroup $H$ the coset action realises $G$ as a group of permutations of the smaller set $G/H$, with kernel the **core** $\bigcap_{a \in G} a H a^{-1}$, the largest subgroup of $H$ normal in $G$.

## Structure and the Size of the Automorphism Group

The realisation of a group as a transformation group is always with respect to a choice of structure on the set $X$, and the richer the structure, the smaller the group:

$$
\operatorname{Aut}(X, \text{structure}) \ \leq \ \operatorname{Sym}(X).
$$

At the level of a bare set the structure is empty, so every bijection is an automorphism, the group is $\operatorname{Sym}(X)$, and by Cayley's theorem every group occurs. This level is universal and has no invariant theory: there is nothing for a transformation to preserve, so no classification beyond the cardinality of $X$ is possible.

Each further piece of structure placed on $X$ cuts the group of automorphisms down to those bijections that preserve it. The two further levels that the corpus uses are the linear structure, where $X$ is a module over a ring and an automorphism is a bijective linear map, giving the general linear group; and a linear structure together with a form, where an automorphism must preserve the form as well, giving the orthogonal, unitary and symplectic groups. Both are stated in terms of structures that this category has not reached — the scalars, the modules and the forms are introduced later — and both are developed where those structures are available: *The General Linear Group*, in the Linear Spaces slot of this Part, treats the first, and *Isometries and Orthogonal Transformations* treats the second in Part II, where a form and a distance are available. They are named here only to record the position of this article in the sequence.

The principle in one sentence: a transformation group is determined by what it is required to preserve, and more structure means fewer automorphisms.

## Summary

A transformation of a set $X$ is a function $X \to X$, and the invertible transformations form the symmetric group $\operatorname{Sym}(X)$ under composition. A structure on $X$ selects a subgroup $\operatorname{Aut}(X) \leq \operatorname{Sym}(X)$ of automorphisms, and $\operatorname{Aut}(X) = \operatorname{End}(X)^\times$ is the group of units of the endomorphism monoid. Adding structure shrinks the group.

An action of a group $G$ on $X$ is a function $G \times X \to X$ with $e \cdot x = x$ and $(ab)\cdot x = a \cdot (b \cdot x)$, equivalently a homomorphism $\rho : G \to \operatorname{Sym}(X)$, the permutation representation. The action is faithful when $\rho$ is injective; in general the image is $G/\ker\rho$, so every action is a faithful action of a quotient. The orbits partition $X$, the stabilisers are subgroups, and every transitive $G$-set is isomorphic to a coset space $G/H$ with $H$ a point stabiliser.

Cayley's theorem, that $G$ embeds in $\operatorname{Sym}(G)$ by the left regular representation, identifies abstract groups with transformation groups of their own underlying sets. The group of automorphisms of a structure is determined by what it preserves, and adding structure can only shrink it: at the level of a bare set the group is $\operatorname{Sym}(X)$. The further levels — a module over a ring, and a module carrying a form — require the scalars, the modules and the forms of later categories, and are developed there.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X$, $Y$ | Sets, or structured sets, on which transformations act |
| $\mathrm{id}_X$ | Identity transformation of $X$ |
| $\operatorname{Sym}(X)$ | Symmetric group of all bijections $X \to X$ |
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
| $G \hookrightarrow \operatorname{Sym}(G)$ | Cayley embedding by the left regular action |







## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991), for transformation groups treated concretely.
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004), for group actions, Cayley's theorem and the standard examples.
- Joseph J. Rotman, *An Introduction to the Theory of Groups* (Springer, 4th ed. 1995), for a systematic treatment of permutation representations and group actions.
- John S. Rose, *A Course on Group Theory* (Dover, 1994), for the orbit decomposition and coset spaces developed from first principles.
- Derek J. S. Robinson, *A Course in the Theory of Groups* (Springer, 2nd ed. 1996), for group actions as a structural tool.
- John D. Dixon and Brian Mortimer, *Permutation Groups* (Springer, Graduate Texts in Mathematics 163, 1996), for faithful actions of small degree and permutation group theory.
