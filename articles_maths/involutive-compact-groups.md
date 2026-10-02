
# __Involutive Compact Groups__

## Introduction

A compact group is the one kind of topological group for which the involution theory is not merely structural but representation-theoretic, because a compact group has enough unitary representations and its closed subgroups are again compact. The added content of a continuous involution of a compact group is threefold: the fixed and inverted sets are compact as well as closed, the quotient by the fixed subgroup is a compact homogeneous space, and the involution acts on the unitary dual by twisting a representation with the involution, so that the representation theory of the group is organised by the action of the involution on its irreducible representations.

The article assumes the continuous involution, the dictionary and the coset theorem from *Involutive Topological Groups*; the criterion for the fixed-point set to be a subgroup and the quotient structure from *The Fixed-Point Subgroup of a Continuous Involution*; the compactness theorems, the closed-subgroup and quotient theorems and the connected-component structure from *Topological Groups*; and the unitary representations of a locally compact group and the unitary dual from *Representation Theory of Locally Compact Groups*. The decomposition of $L^2(G)$ into matrix coefficients, the Peter–Weyl theorem and the invariant integral are Part III, *Analysis on Compact Groups* and *The Peter–Weyl Theorem*; they are named once and not used.

Throughout, $G$ is a compact Hausdorff topological group with identity $e$, $\sigma$ is a continuous involution, $\alpha = \sigma\iota$ is the associated continuous involutive automorphism, $G^\sigma$ and $I(\sigma) = G^\alpha$ are the fixed and inverted sets, and the unitary dual of $G$ is written $\operatorname{Irr}(G)$.

## The Fixed Subgroup of a Compact Involution

**Theorem (compactness of the sets).** In a compact group the fixed-point set $G^\sigma$ and the fixed subgroup $G^\alpha = I(\sigma)$ are compact as well as closed, and every closed subgroup on which the involution acts by the inversion is contained in $G^\alpha$.

**Proof.** Both sets are closed, by the equalizer argument for the continuous maps $\sigma$ and $\mathrm{id}$ and for $\alpha$ and $\mathrm{id}$; a closed subset of a compact space is compact. The maximality of $G^\alpha$ is the theorem on the fixed subgroup.

**Theorem (the subgroup criterion in the compact case).** The fixed-point set $G^\sigma$ is a subgroup of $G$ if and only if it is abelian; it is then compact and abelian, hence a compact abelian subgroup, and it carries the Pontryagin duality of *Abelian Topological Groups* when the involution is the inversion.

**Proof.** The criterion is proved for every Hausdorff group and applies verbatim; the compactness follows from the previous theorem, and a compact abelian subgroup is the object of the duality theory, whose applicability is asserted and not used here.

**Theorem (the connected component).** The identity component $G_0$ is stable under $\sigma$ and under $\alpha$, so the involution restricts to $G_0$ and descends to the totally disconnected quotient $G/G_0$; the fixed subgroup of the restriction is $G^\alpha\cap G_0$ and the fixed-point set of the restriction is $G^\sigma\cap G_0$, and the identity component $(G^\alpha)_0$ of $G^\alpha$ is contained in $G^\alpha\cap G_0$ and equals it when $G^\alpha\cap G_0$ is connected.

**Proof.** A continuous automorphism or anti-automorphism carries the identity component, which is the unique connected component containing the identity, to itself. The fixed sets of the restriction are the intersections with $G_0$ by definition; $(G^\alpha)_0$ is connected, contains $e$ and lies in $G^\alpha\cap G_0$, and it equals that group when the group is connected. The reverse inclusion is not asserted, because the intersection of a closed subgroup with $G_0$ need not be connected.

**Corollary (the profinite case).** If $G$ is profinite then $G_0 = \{e\}$, the whole group is totally disconnected, and the involution is determined by its action on the open normal subgroups; this is the compact case of *Involutive Profinite Groups*, and no separate statement is needed here.

**Proof.** A profinite group is compact totally disconnected, so $G_0 = \{e\}$; an open normal subgroup $N$ gives a finite quotient on which $\sigma$ acts, and the compatible system of these actions determines $\sigma$ because the open normal subgroups form a neighbourhood base.

## The Quotient

**Definition.** For the fixed subgroup $H = G^\alpha = I(\sigma)$ the involution carries the left coset $gH$ to the right coset $H\sigma(g)$, and the induced map

$$
\bar\sigma : G/H \longrightarrow H\backslash G , \qquad \bar\sigma(gH) = H\sigma(g) ,
$$

is a homeomorphism by the general quotient theorem; when $H$ is normal it is a continuous involution of the compact quotient group $G/H$.

**Theorem (the quotient is compact and homogeneous).** $G/H$ is compact Hausdorff, it carries the transitive continuous action of $G$ by left translation, and the induced involution $\bar\sigma$ is a homeomorphism of order two in the sense that it coincides with its own inverse after the identification of $G/H$ with $H\backslash G$; the fixed set of $\bar\sigma$, when $H$ is normal, contains the image of $G^\sigma$ and may be strictly larger.

**Proof.** The quotient of a compact group by a closed subgroup is compact Hausdorff and homogeneous by *Topological Groups*; the induced map is a homeomorphism by the general theory; the statement about the fixed set is the strictness theorem for quotients, whose standard witness is $\mathbb{Z}/4\mathbb{Z}$.

**Theorem (the double coset space).** The fixed subgroup acts on both sides, the involution descends to the double coset space $H\backslash G/H$, and this space is compact Hausdorff; the induced involution of the double coset space has a closed fixed set, and the orbit map $g\mapsto HgH$ is continuous, proper and $G$-equivariant for the two-sided action.

**Proof.** The double cosets are the orbits of the compact group $H\times H$ acting by $(h,k)\cdot g = hgk^{-1}$; the orbit space of a compact group action on a compact Hausdorff space is compact Hausdorff, and $\sigma$ permutes the orbits because $\sigma(H) = H$. The fixed set of the induced involution is closed by the equalizer argument, and the orbit map is continuous and proper because the acting group is compact.

**Remark (the compact abelian case).** If $G$ is compact abelian then every anti-automorphism is an automorphism, the fixed subgroup and the fixed-point set coincide, and the involution is a continuous automorphism of order two of the compact abelian group; on the character group $G^\vee$ it acts contravariantly by $\chi\mapsto\chi\circ\sigma$, and the fixed characters are exactly the characters of the quotient $G/G^\sigma$. This is the compact case of *Involutions and Pontryagin Duality*, and the duality language is used there.

## The Dual and the Twisted Representation

**Definition.** Let $\pi : G \to U(V)$ be a continuous unitary representation on a Hilbert space $V$, with contragredient $\check\pi$ on the dual space $V^*$ given by $\check\pi(g) = \pi(g^{-1})^t$. The **involution twist** of $\pi$ is the representation

$$
\pi^\sigma : G \longrightarrow U(V^*) , \qquad \pi^\sigma(g) = \pi(\sigma(g))^t ,
$$

the transpose of the anti-homomorphism $\pi\circ\sigma$ acting on $V^*$.

**Theorem (the twist is a representation and an involution).** $\pi^\sigma$ is a continuous unitary representation on $V^*$, the assignment $\pi\mapsto\pi^\sigma$ is an involution of the set of continuous unitary representations, it respects unitary equivalence and irreducibility, so it acts as an involution of the unitary dual $\operatorname{Irr}(G)$, and its fixed points are the **self-conjugate** irreducible representations, those with $\pi^\sigma\cong\pi$.

**Proof.** For $g, h$ one has $\pi^\sigma(gh) = \pi(\sigma(gh))^t = \pi(\sigma(h)\sigma(g))^t = (\pi(\sigma(h))\pi(\sigma(g)))^t = \pi(\sigma(g))^t\pi(\sigma(h))^t = \pi^\sigma(g)\pi^\sigma(h)$, so $\pi^\sigma$ is multiplicative; it is continuous because $\sigma$ is and the transpose is an isometry of the unitary group; applying the construction twice gives $(\pi^\sigma)^\sigma = \pi$ up to the canonical identification $V^{**}\cong V$. A conjugate of $\pi$ has a conjugate twist, and an invariant subspace of $\pi$ gives an invariant subspace of $\pi^\sigma$ by transposition, so irreducibility is preserved.

**Theorem (extension to the semidirect product).** The representations of $G$ that are fixed by the twist are exactly the restrictions of the representations of the split extension $G\rtimes_\alpha C_2$ in which the generator of $C_2$ acts by the transposition on $V^*$; equivalently, a self-conjugate irreducible $\pi$ carries a $C_2$-action making it a representation of the extension, and the two possible extensions are classified by the self-intertwiners of $\pi$.

**Proof.** The extension $G\rtimes_\alpha C_2$ is a topological group exactly when $\alpha$ is continuous, by *Involutive Topological Groups*; a representation of the extension restricts to a representation of $G$ and to an operator $T$ with $T\pi(g)T^{-1} = \pi(\alpha(g))$, which is the condition that $\pi$ be fixed by the twist after the identification of the contragredient. The classification of the extensions by the self-intertwiners is the abstract statement about the representations of a semidirect product by $C_2$, stated here and not developed.

**Corollary (the character).** If $\pi$ is finite-dimensional with character $\chi_\pi$ then the character of the twist is $\chi_{\pi^\sigma}(g) = \overline{\chi_\pi(\sigma(g))}$, and the fixed irreducibles are those whose character is real on the fixed-point set and satisfies $\chi_\pi(\sigma(g)) = \overline{\chi_\pi(g)}$.

**Proof.** The character of the contragredient is the complex conjugate, and transposition does not change the trace; the identity follows from the definition of the twist.

## The Fixed Subgroup and the Restriction

**Theorem (restriction to the fixed subgroup).** Let $H = G^\alpha = I(\sigma)$ and let $\pi$ be a continuous unitary representation of $G$. Then the restriction $\pi|_H$ is a continuous unitary representation of the compact group $H$, and the twist of the restriction is the restriction of the twist, $(\pi|_H)^\sigma = \pi^\sigma|_H$; in particular the restriction of a self-conjugate representation is self-conjugate.

**Proof.** The restriction of a continuous representation to a closed subgroup is continuous, and the two constructions commute because both are given by the same formula $g\mapsto\pi(\sigma(g))^t$ on the subgroup.

**Theorem (representations of the quotient).** Let $H$ be normal. The continuous unitary representations of $G/H$ are exactly the continuous unitary representations of $G$ that are trivial on $H$, and the twist of such a representation corresponds to the twist by the induced involution $\bar\sigma$ of $G/H$; the self-conjugate representations of the quotient are the self-conjugate representations of $G$ trivial on $H$.

**Proof.** A representation of $G/H$ pulls back to a representation of $G$ trivial on $H$, and conversely a representation trivial on a normal subgroup factors through the quotient; the twist statement is the identity $\pi^\sigma(g) = \pi(\sigma(g))^t$ computed modulo $H$, where $\sigma$ induces $\bar\sigma$.

**Remark (the analytic consequences).** The action of the involution on the dual organises the decomposition of $L^2(G)$ into the eigenspaces of the induced involution, and the multiplicities of the self-conjugate representations carry the extra structure of their self-intertwiners; both statements require the invariant integral and the Peter–Weyl theorem and belong to Part III, *Analysis on Compact Groups* and *The Peter–Weyl Theorem*. This article stops at the abstract action on the dual and the extension to the semidirect product.

## Summary

In a compact group a continuous involution has compact fixed and inverted sets, the fixed subgroup $H = G^\alpha = I(\sigma)$ is compact, and the fixed-point set is a subgroup exactly when it is abelian. The identity component is stable, so the involution descends to the totally disconnected quotient and restricts to the identity component; for a profinite group the whole theory is the finite-quotient theory of *Involutive Profinite Groups*. The involution carries left cosets of $H$ to right cosets and induces a homeomorphism $G/H\to H\backslash G$, a compact homogeneous space, an involution of the quotient group when $H$ is normal, and an involution of the double coset space $H\backslash G/H$; the fixed set of the quotient involution contains the image of $G^\sigma$ and may be strictly larger. On the unitary dual the involution acts by the twist $\pi^\sigma(g) = \pi(\sigma(g))^t$ on the contragredient, an involution of $\operatorname{Irr}(G)$ whose fixed points are the self-conjugate irreducibles; a representation is self-conjugate exactly when it extends to the split extension $G\rtimes_\alpha C_2$, and the extensions are classified by the self-intertwiners. Restriction to the fixed subgroup and passage to the quotient both commute with the twist, the character of the twist is $\chi_{\pi^\sigma}(g) = \overline{\chi_\pi(\sigma(g))}$, and the analytic decomposition that these structures organise is Part III and is named only.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G_0$ | the identity component, stable under $\sigma$ and $\alpha$ |
| $G^\sigma$ | the fixed-point set, compact; a subgroup iff abelian |
| $H = G^\alpha = I(\sigma)$ | the fixed subgroup, compact, the largest inverted subgroup |
| $\bar\sigma(gH) = H\sigma(g)$ | the induced homeomorphism $G/H \to H\backslash G$ |
| $H\backslash G/H$ | the compact double coset space with its induced involution |
| $\operatorname{Irr}(G)$ | the unitary dual of the compact group |
| $\pi^\sigma(g) = \pi(\sigma(g))^t$ | the involution twist, an involution of $\operatorname{Irr}(G)$ |
| $\check\pi(g) = \pi(g^{-1})^t$ | the contragredient representation |
| $G\rtimes_\alpha C_2$ | the split extension, a topological group because $\alpha$ is continuous |
| self-conjugate | $\pi^\sigma\cong\pi$; equivalently $\pi$ extends to the extension |
| $\chi_{\pi^\sigma}(g) = \overline{\chi_\pi(\sigma(g))}$ | the character of the twist |

## Further Reading

- Theodor Bröcker and Tammo tom Dieck, *Representations of Compact Lie Groups* (Springer, 1985), for the unitary dual of a compact group and the twisting of representations by an automorphism.
- Karl H. Hofmann and Sidney A. Morris, *The Structure of Compact Groups* (De Gruyter, third edition, 2013), for the closed-subgroup and quotient theorems, the identity component and the automorphism group of a compact group.
- Lev S. Pontryagin, *Topological Groups* (Gordon and Breach, second edition, 1966), for compactness, the quotient topology and the connected-component structure.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978; reprinted AMS, 2001), for the fixed subgroup of an involution inside a compact group, whose symmetric-space geometry belongs to Part IV.
- Jean-Pierre Serre, *Linear Representations of Finite Groups* (Springer, 1977), for the twisting of representations by an automorphism and the classification of the extensions by $C_2$.
