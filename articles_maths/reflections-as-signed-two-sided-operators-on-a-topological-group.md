
# __Reflections as Signed Two-Sided Operators on a Topological Group__

## Introduction

A reflection of a topological group is an operator of the signed two-sided form $x \mapsto a\,\alpha(x)\,a^{-1}$ that is its own inverse: it is an involution of the group produced by the multiplication, the continuous grade involution and the inverse, and the topology makes its fixed set closed and its carrying elements a closed set. This article reads the reflections of a graded topological group as operators on the group, identifies the elements that carry them, computes their fixed subgroups, and records the degenerate cases — the grade involution inner, the group abelian, or the carrying element failing the centrality that makes the operator an involution.

The article assumes the continuous involutive automorphism, the fixed and inverted subgroups and the dictionary between them from *Involutive Topological Groups*; the abstract reflections, their squares, their fixed subgroups, the coset description of the carrying elements and the degenerate cases from *Reflections as Signed Two-Sided Operators on a Group*; the signed sandwich and its composition laws from *The Signed Sandwich on a Topological Group*; and the translations, the homeomorphism group and the compact-open topology from *Operators on a Topological Group*. The adjoint of a reflection is *The Signed Adjoint of the Reflection on a Topological Group*. A reflection in the geometric sense — in a hyperplane, preserving a form — needs a form and belongs to the later categories; a reflection here is only a continuous operator on the underlying group of order two.

Throughout, $G$ is a Hausdorff topological group with identity $e$, $\alpha$ is a continuous involutive automorphism, $\sigma = \iota\alpha$ is the associated topological involution, $G^\alpha$ is the fixed subgroup of $\alpha$, $I(\sigma) = G^\alpha$ is the inverted subgroup of $\sigma$, and $Z(G)$ is the centre.

## The Signed Conjugation

**Definition.** For $a \in G$ the **signed conjugation** by $a$ is the signed sandwich $\rho_a = \Sigma^{\alpha}_{a,a^{-1}}$, that is

$$
\rho_a : G \longrightarrow G, \qquad \rho_a(x) = a\,\alpha(x)\,a^{-1} .
$$

**Proposition (it is a continuous automorphism).** $\rho_a = c_a \circ \alpha$, a composite of continuous automorphisms of $G$, hence a continuous automorphism; its inverse is $\alpha \circ c_{a^{-1}} = c_{\alpha(a^{-1})}\circ\alpha$, and its square is the inner conjugation

$$
\rho_a^2 = c_{a\alpha(a)} = \Sigma_{a\alpha(a),\,(a\alpha(a))^{-1}} .
$$

Consequently $\rho_a$ is an involution of the set $G$ exactly when $a\alpha(a) \in Z(G)$.

**Proof.** $c_a(\alpha(x)) = a\alpha(x)a^{-1}$ is the definition, and a composite of continuous automorphisms is a continuous automorphism. The square is the computation of *The Signed Sandwich on a Topological Group*, and an inner conjugation is the identity exactly on the central elements.

**Corollary.** $\rho_a$ is a homeomorphism of $G$ of order two when $a\alpha(a)$ is central, and otherwise its order is the order of the inner automorphism $c_{a\alpha(a)}$, which is the order of the coset $a\alpha(a)Z(G)$ in $G/Z(G)$.

**Proof.** $\rho_a^2 = c_{a\alpha(a)}$ and $\rho_a$ is a homeomorphism; the order of an inner conjugation $c_u$ is the order of the class of $u$ in the group of inner automorphisms $G/Z(G)$.

## Reflections

**Definition.** A **reflection** of the graded topological group $(G,\alpha)$ is a signed conjugation that is an involution,

$$
\rho_a \text{ is a reflection} \iff \rho_a^2 = \mathrm{id} \iff a\,\alpha(a) \in Z(G) .
$$

A reflection is thus a continuous involutive automorphism of $G$, that is a topological involution in the sense of *Involutive Topological Groups*, and it is a homeomorphism of order two.

**Theorem (the fixed subgroup is closed).** Let $\rho_a$ be a reflection. Its fixed set

$$
\operatorname{Fix}(a) = \{x \in G : \alpha(x) = a^{-1}xa\}
$$

is closed in $G$, it is a subgroup of $G$ containing $e$, it reduces to the centraliser $C_G(a)$ when $\alpha = \mathrm{id}$, and it is a left coset of the fixed subgroup $G^\alpha$ whenever it is nonempty. If $G$ is compact then $\operatorname{Fix}(a)$ is compact, and if $G$ is connected and $\operatorname{Fix}(a)$ is open then $\operatorname{Fix}(a) = G$.

**Proof.** $\operatorname{Fix}(a)$ is the equalizer of the continuous maps $\alpha$ and $c_{a^{-1}}$, hence closed because $G$ is Hausdorff. It is a subgroup and a coset of $G^\alpha$ by *Reflections as Signed Two-Sided Operators on a Group*. A closed subset of a compact space is compact, and an open subgroup of a connected group is the whole group by the connectedness theorem of *Topological Groups*.

**Theorem (the carrying elements form a closed set).** Put

$$
C = \{a \in G : a\,\alpha(a) \in Z(G)\},
$$

the set of elements that carry a reflection. Then $C$ is closed in $G$, it is symmetric under $a \mapsto a^{-1}$ and under $a \mapsto \alpha(a)$, and it contains $I(\sigma) = G^\alpha$.

**Proof.** The map $\varphi : a \mapsto a\,\alpha(a)$ is continuous, being a product of continuous maps, and $Z(G)$ is closed in a Hausdorff group, being the equalizer of the continuous maps $(x,y)\mapsto xg$ and $(x,y)\mapsto gx$ or equivalently the intersection of the centralisers $C_G(g)$; hence $C = \varphi^{-1}(Z(G))$ is closed. If $a\alpha(a)$ is central then so is its inverse $a^{-1}\alpha(a^{-1}) = (a\alpha(a))^{-1}$, and so is $\alpha(a)\alpha(\alpha(a)) = \alpha(a\alpha(a))$, which gives the two symmetries. For $a \in G^\alpha$ the dictionary gives $\alpha(a) = a^{-1}$, so $a\alpha(a) = e \in Z(G)$.

**Theorem (the carrying elements and the cosets).** Two elements $a, a'$ carry the same reflection if and only if $a' \in aZ(G)$, so the reflections are parametrised by the cosets $aZ(G)$ of the elements $a \in C$, and the map

$$
G \longrightarrow \operatorname{Homeo}(G), \qquad a \mapsto \rho_a ,
$$

factors through $G/Z(G)$ as a continuous injection on the carriers.

**Proof.** The coset description is *Reflections as Signed Two-Sided Operators on a Group*: $\rho_a = \rho_{a'}$ if and only if $a'^{-1}a$ commutes with every element of the image of $\alpha$, hence lies in $Z(G)$. Continuity of $a \mapsto \rho_a$ is the continuity of the inner automorphism map composed with the fixed $\alpha$; the factorisation through $G/Z(G)$ is exactly the coset statement, and injectivity on $C/Z(G)$ follows.

**Corollary (compact case).** If $G$ is compact then $C$ is compact and the set of reflections is the continuous image of the compact quotient $C/Z(G)$, hence is compact, and in particular closed, in the group $\operatorname{Homeo}(G)$ of homeomorphisms with the compact-open topology.

**Proof.** $C$ is closed in the compact group $G$, hence compact; $Z(G)$ is closed and normal, so $C/Z(G)$ is compact; the image of a compact space under the continuous map $a \mapsto \rho_a$ is compact, and a compact subspace of a Hausdorff space is closed.

## The Correspondence with the Elements acting by an Involution

The abstract theory reads an involution of $G$ as a pair — the anti-automorphism $\sigma$ or, equivalently, the involutive automorphism $\alpha = \sigma\iota$ — and the reflections are the signed conjugations that happen to be involutions. In the topological setting the correspondence acquires a closedness statement.

**Theorem (the correspondence).** The following sets are in explicit bijection:

**(a)** the reflections $\rho_a$ with $a \in C$;

**(b)** the cosets $aZ(G)$ with $a\alpha(a)$ central;

**(c)** the elements $u = a\alpha(a) \in Z(G)$ that arise as such a product, up to the relation generated by the choice of $a$.

The bijection (a) $\leftrightarrow$ (b) is $a \mapsto aZ(G)$ with inverse $aZ(G) \mapsto \rho_a$, and it is a homeomorphism of the set of carriers modulo $Z(G)$ onto the set of reflections when $G$ is compact.

**Proof.** (a) $\leftrightarrow$ (b) is the theorem above. For (c), the product $u = a\alpha(a)$ is central for a carrier and is determined by the coset $aZ(G)$ only up to conjugacy by $Z(G)$, which is trivial because $Z(G)$ is central; the map $aZ(G) \mapsto a\alpha(a)$ is well defined and its image is a subset of $Z(G)$. The homeomorphism statement is the compact corollary above.

**Corollary (the inverted subgroup carries reflections).** Every element of the inverted subgroup $I(\sigma) = G^\alpha$ carries a reflection, and the subgroup $G^\alpha$ is closed, so its image in the reflection family is a compact (when $G$ is compact) closed set of reflections. The elements of $G^\alpha$ are exactly those on which the grade involution and the inversion agree.

**Proof.** For $a \in G^\alpha$ one has $\alpha(a) = a^{-1}$, so $a\alpha(a) = e$ is central and $\rho_a$ is a reflection; the dictionary and the closedness of the fixed set of a continuous involution are those of *Involutive Topological Groups*.

**Remark (the reflection of an abelian group).** On an abelian topological group every inner conjugation is the identity, so every signed conjugation equals the grade involution, $\rho_a = \alpha$ for every $a \in G$, and the reflections of $(G,\alpha)$ are the single topological involution $\alpha$; when $\alpha = \mathrm{id}$ the only reflection is the identity. The correspondence (a) $\leftrightarrow$ (b) then collapses: every coset $aZ(G) = G$ maps to the same reflection.

## The Degenerate Cases

The construction degenerates in three ways, and the topology does not repair any of them; it only makes the degenerate sets closed.

**Theorem (inner grade involution).** If the grade involution is inner, say $\alpha = c_z$ with $z^2$ central, then every signed conjugation is an ordinary inner conjugation,

$$
\rho_a = c_a \circ c_z = c_{az},
$$

so no signed operator is distinguished from an inner automorphism; the reflection $\rho_a$ is an involution exactly when $(az)^2 \in Z(G)$, in which case it is the inner automorphism of order two $c_{az}$.

**Proof.** That an inner grade involution forces $\mathfrak{S}^\alpha = \mathfrak{S}$ is *The Signed Sandwich on a Topological Group*; hence $\rho_a = c_a\alpha = c_ac_z = c_{az}$, and an inner conjugation is an involution exactly when its conjugating element squares to a central element. The conjugating element $az$ is a product of continuous elements, so the map $a \mapsto c_{az}$ is continuous.

**Theorem (abelian group).** If $G$ is abelian then every reflection is the grade involution,

$$
\rho_a = \alpha \qquad \text{for every } a \in G ,
$$

and the reflection family has a single element. The map $a \mapsto \rho_a$ is constant, and its image is the point $\alpha$ of $\operatorname{Homeo}(G)$.

**Proof.** On an abelian group $c_a = \mathrm{id}$ for every $a$, so $\rho_a = \alpha$; and $\alpha^2 = \mathrm{id}$ makes $\alpha$ a reflection, consistently with $a\alpha(a) = a^2 \in G = Z(G)$.

**Theorem (non-central carrying product).** If $a\alpha(a) \notin Z(G)$ then the signed conjugation is not an involution: it is a homeomorphism of $G$ whose square is the nontrivial inner conjugation $c_{a\alpha(a)}$. Its order is the order of the class of $a\alpha(a)$ in $G/Z(G)$, which is finite exactly when that class has finite order; if $G$ is compact then every such class has finite order, so every signed conjugation has finite order, and the order divides the order of the finite group $G/Z(G)$ when $G/Z(G)$ is finite.

**Proof.** The square is $c_{a\alpha(a)}$, which is the identity exactly on the central elements. The order statement is the corollary of the first section. For compact $G$ the quotient $G/Z(G)$ need not be finite in general, but the stabiliser statement used here is the finiteness of the order of a single class; the exact order is the order of $a\alpha(a)Z(G)$ in $G/Z(G)$.

The three cases exhaust the ways a signed conjugation can fail to be a reflection: the grade involution may be inner, so the signed operator carries no information beyond conjugation; the group may be abelian, so every reflection is the same operator; or the carrying element may have a non-central product $a\alpha(a)$, so the operator is a homeomorphism of order greater than two rather than an involution.

## Summary

For a graded topological group $(G,\alpha)$ the **signed conjugation** $\rho_a(x) = a\alpha(x)a^{-1} = c_a\alpha$ is a continuous automorphism whose square is the inner conjugation by $a\alpha(a)$; it is an involution of the topological group, a **reflection**, exactly when $a\alpha(a) \in Z(G)$, and the set $C$ of such carriers is closed in $G$ and stable under inversion and under $\alpha$. The fixed set $\operatorname{Fix}(a) = \{x : \alpha(x) = a^{-1}xa\}$ of a reflection is closed, is a subgroup, is the centraliser $C_G(a)$ when $\alpha = \mathrm{id}$, and is a coset of the fixed subgroup $G^\alpha$ when nonempty; it is compact when $G$ is, and it forces $\rho_a = \mathrm{id}$ when it is open and $G$ is connected. Two elements carry the same reflection exactly when they differ by a central element, so the reflections are parametrised by the cosets $aZ(G)$ of the carriers, and this parametrisation is a homeomorphism when $G$ is compact. Every element of the inverted subgroup $I(\sigma) = G^\alpha$ carries a reflection automatically. The construction degenerates exactly as in the abstract theory: when $\alpha$ is inner the reflections are inner automorphisms; when $G$ is abelian they collapse to the single operator $\alpha$; and when $a\alpha(a)$ is not central the signed conjugation is a homeomorphism of order the order of the class of $a\alpha(a)$ in $G/Z(G)$ rather than an involution.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho_a = \Sigma^{\alpha}_{a,a^{-1}}$ | the signed conjugation $x \mapsto a\alpha(x)a^{-1}$, a continuous automorphism |
| $\rho_a = c_a\alpha$ | its expression as a composite of continuous automorphisms |
| $\rho_a^2 = c_{a\alpha(a)}$ | its square, an inner conjugation |
| $a\alpha(a) \in Z(G)$ | the criterion for $\rho_a$ to be a reflection |
| $C = \{a : a\alpha(a) \in Z(G)\}$ | the closed set of carriers |
| $\operatorname{Fix}(a) = \{x : \alpha(x) = a^{-1}xa\}$ | the closed fixed subgroup of $\rho_a$ |
| $G^\alpha = I(\sigma)$ | the fixed subgroup of $\alpha$; every element carries a reflection |
| $aZ(G)$ | the coset of carriers of one reflection |
| $\alpha$ inner | degenerate case, reflections are inner automorphisms |
| $G$ abelian | degenerate case, the only reflection is $\alpha$ |
| $a\alpha(a) \notin Z(G)$ | degenerate carrier, $\rho_a$ not an involution |

## Further Reading

- Lev S. Pontryagin, *Topological Groups* (Gordon and Breach, second edition, 1966), for the continuous automorphisms, the fixed subgroups and the compact-open topology on $\operatorname{Homeo}(G)$.
- Karl H. Hofmann and Sidney A. Morris, *The Structure of Compact Groups* (De Gruyter, third edition, 2013), for the automorphism group of a compact group, its topology and the conjugacy classes.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the generation of an orthogonal group by reflections, each carried by an element and realised by a signed conjugation.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for involutive automorphisms, inverted elements and fixed subgroups.
- Derek J. S. Robinson, *A Course in the Theory of Groups* (Springer, second edition, 1996), for automorphisms of order two, centralisers and the structure of the automorphism group.
