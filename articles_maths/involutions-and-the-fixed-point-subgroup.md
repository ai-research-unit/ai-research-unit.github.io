
# __Involutions and the Fixed-Point Subgroup__

## Introduction

An involution of a group carries a set of elements it fixes, and that set is the first invariant the involution defines. For an automorphism the fixed set is always a subgroup, because an automorphism is multiplicative; for an anti-automorphism it need not be, because a product of two fixed elements is fixed only when the two commute. This article develops the fixed set as an object: the exact criterion under which it is a subgroup, the properties of the fixed-point subgroup when it exists, and the canonical case of the inversion, whose fixed set is the set of elements of order at most two. The article is the first of the involutive `*`-articles; the involution itself, the bijection between involutions and involutive automorphisms, the inverted set and the induced involution on a quotient are owned by *Involutive Groups* and are used, not restated.

Throughout, $(G,\sigma)$ is an involutive group as in *Involutive Groups*: $\sigma$ is an anti-automorphism with $\sigma^2=\mathrm{id}$, the fixed set is $G^{\sigma}=\{g:\sigma(g)=g\}$, the inverted set is $I(\sigma)=\{g:\sigma(g)=g^{-1}\}$, and $\alpha=\sigma\iota$ is the involutive automorphism associated with $\sigma$ by the bijection $\sigma\mapsto\sigma\iota$.

## The Fixed Set and the Subgroup Criterion

**Proposition (the fixed set contains the identity and is inversion-closed).** $e\in G^{\sigma}$, and if $g\in G^{\sigma}$ then $g^{-1}\in G^{\sigma}$; the same holds for $G^{\alpha}$.

**Proof.** $\sigma(e)=e$ because $\sigma$ is a bijection preserving the identity; and $\sigma(g^{-1})=\sigma(g)^{-1}=g^{-1}$ for $g$ fixed, the first equality holding for every anti-automorphism.

So the only question is closure under multiplication, and there the anti-automorphism shows itself.

**Proposition (the closure computation).** For $a,b\in G^{\sigma}$ one has $\sigma(ab)=ba$. Hence $ab\in G^{\sigma}$ if and only if $a$ and $b$ commute. For an involutive automorphism $\alpha$ the same computation gives $\alpha(ab)=\alpha(a)\alpha(b)$, and no commutation is required.

**Proof.** For the involution, $\sigma(ab)=\sigma(b)\sigma(a)=ba$ because $a$ and $b$ are fixed. So $ab$ is fixed exactly when $ba=ab$. For the automorphism, multiplicativity gives the second statement. The contrast is the whole content of the next two sections.

**Theorem (the criterion).** The fixed set $G^{\sigma}$ is a subgroup of $G$ if and only if its elements commute pairwise; equivalently, if and only if $G^{\sigma}$ is abelian. When this holds, $G^{\sigma}$ is an abelian subgroup of $G$, and it is the largest subgroup of $G$ on which $\sigma$ acts as the identity.

**Proof.** $G^{\sigma}$ contains $e$ and is inversion-closed. It is closed under multiplication if and only if $ab\in G^{\sigma}$ for all $a,b\in G^{\sigma}$, which by the closure computation is exactly the pairwise commutation. If $H\leq G$ is fixed pointwise by $\sigma$ then $H\subseteq G^{\sigma}$ by definition, so $G^{\sigma}$ is the largest such subgroup, and it is abelian because it is a subgroup whose elements commute pairwise. This is the criterion stated in *Involutive Groups*, §4.

**Remark (the two sources of failure).** The criterion can fail in two visibly different ways: the fixed set may be a subgroup that is not central, or it may not be a subgroup at all. The involution on $S_3$ given by $\sigma=\iota\alpha$ with $\alpha$ the conjugation by a transposition has $G^{\sigma}=\{e,(1\,2),(1\,2\,3),(1\,3\,2)\}$, four elements that do not close, so the fixed set is not a subgroup; the inversion on $A_4$ has fixed set the Klein four group $V_4=\{e,(1\,2)(3\,4),(1\,3)(2\,4),(1\,4)(2\,3)\}$, which is a subgroup and is not central in $A_4$.

## The Fixed-Point Subgroup

When the criterion holds, $G^{\sigma}$ is a subgroup with several forced properties.

**Proposition (the fixed-point subgroup is abelian and self-centralising in the sense of elements).** Let $H=G^{\sigma}$ be a subgroup. Then $H$ is abelian, $\sigma|_H=\mathrm{id}$, and $H\subseteq C_G(H)$; the normaliser $N_G(H)$ contains $H$ and is $\sigma$-stable.

**Proof.** The abelian property is the criterion. Every element of $H$ is fixed, so $\sigma$ restricts to the identity of $H$. The centraliser contains $H$ exactly because $H$ is abelian. For the normaliser, if $g\in N_G(H)$ then $\sigma(g)\in N_G(\sigma(H))=N_G(H)$ because $\sigma$ is an automorphism of the subgroup lattice (*Involutive Groups*, §3), so $N_G(H)$ is $\sigma$-stable.

**Proposition (the pairing with the inverted set).** The fixed set and the inverted set meet in the $\sigma$-fixed elements of order at most two: $G^{\sigma}\cap I(\sigma)=\{g:g=g^{-1},\ \sigma(g)=g\}=\{g\in G^{\sigma}:g^{2}=e\}$. In particular, when $G^{\sigma}$ is a subgroup its intersection with $I(\sigma)$ is the $2$-torsion of $G^{\sigma}$.

**Proof.** $g\in G^{\sigma}\cap I(\sigma)$ means $\sigma(g)=g$ and $\sigma(g)=g^{-1}$, hence $g=g^{-1}$; conversely $g=g^{-1}$ and $\sigma(g)=g$ give both memberships. The last statement restricts to the subgroup $G^{\sigma}$.

**Proposition (the fixed-point subgroup of the inversion of a subgroup).** Let $H\leq G$ be $\sigma$-stable, so that $\sigma$ restricts to an involution $\sigma|_H$ of $H$. Then $H^{\sigma|_H}=H\cap G^{\sigma}$ and $I(\sigma|_H)=H\cap I(\sigma)$.

**Proof.** Both statements unwind the definitions; the first says that an element of $H$ fixed by the restriction is fixed by $\sigma$, and the second that it is inverted by the restriction exactly when it is inverted by $\sigma$.

## The Canonical Involution

The inversion $\iota(g)=g^{-1}$ is the involution every group carries, and its fixed set is the set of elements of order at most two.

**Proposition (the fixed set of the inversion).** $G^{\iota}=\{g\in G:g^{2}=e\}$, the $2$-torsion set of $G$; $I(\iota)=G$.

**Proof.** $\iota(g)=g$ is $g^{-1}=g$, which is $g^{2}=e$; and $\iota(g)=g^{-1}$ holds identically.

**Proposition (when the $2$-torsion is a subgroup, and when it is central).** The $2$-torsion set $G^{\iota}$ is a subgroup if and only if the elements of order at most two commute pairwise; it is central if and only if every element of order at most two is central. The two conditions are independent: $G^{\iota}$ may be a non-central subgroup, and it may be central without being the whole group.

**Proof.** The subgroup criterion is the theorem above applied to $\iota$. The fixed set is central exactly when $G^{\iota}\subseteq Z(G)$ by the definition of the centre. The two conditions are independent by the examples below.

**Example ($A_4$: a subgroup that is not central).** In $A_4$ the elements of order at most two are the identity and the three double transpositions, which form the Klein four group $V_4$. The subgroup $V_4$ is normal in $A_4$ and is not central, since $Z(A_4)=\{e\}$. So the fixed set of the inversion is a non-central subgroup.

**Example ($S_3$: not a subgroup).** In $S_3$ the elements of order at most two are $e$ and the three transpositions, four elements in all. The product $(1\,2)(1\,3)=(1\,3\,2)$ has order three, so the set is not closed; the fixed set of the inversion is not a subgroup. Its elements do not commute pairwise, the transpositions $(1\,2)$ and $(1\,3)$ failing.

**Example ($Q_8$: a central subgroup).** In $Q_8$ the only elements of order at most two are $1$ and $-1$, so $G^{\iota}=\{1,-1\}=Z(Q_8)$ is a central subgroup of order two. The inversion here fixes the centre and inverts the six elements of order four.

**Example (elementary abelian groups).** If $G$ has exponent dividing two then $G^{\iota}=G$ and $G$ is abelian of exponent two, so every element is central; the fixed set is the whole group and it is central.

**Remark (the word "central" in the menu).** The fixed set of the inversion is not central in general, and the correct statement is the one proved here: it is a subgroup exactly when the involutions commute pairwise, and it is central exactly when every element of order at most two is central. The two are independent, and $A_4$ separates them. This is a point at which the article's statement departs from the phrase in the source that prompted it.

## The Fixed Set and the Centre

**Proposition (the fixed set of an involution on the centre).** The centre $Z(G)$ is $\sigma$-stable, and $\sigma$ restricts to an involution $\sigma|_{Z(G)}$ of the abelian group $Z(G)$; its fixed set is $Z(G)\cap G^{\sigma}$ and its inverted set is $Z(G)\cap I(\sigma)$.

**Proof.** If $g$ is central and $x\in G$ then $\sigma(g)x=\sigma(g\sigma^{-1}(x))=\sigma(\sigma^{-1}(x)g)=x\sigma(g)$, so $\sigma(g)$ is central; hence $Z(G)$ is $\sigma$-stable and the restriction is an involution. The fixed and inverted sets of the restriction are the intersections with $Z(G)$.

**Proposition (central fixed points and the involutive automorphism).** An element $g$ lies in $Z(G)\cap G^{\sigma}$ if and only if $g$ is central and $\alpha(g)=g^{-1}$; hence the central fixed points of $\sigma$ are the central elements inverted by $\alpha$. In particular $G^{\sigma}$ contains $I(\alpha)\cap Z(G)$, and $G^{\sigma}\cap Z(G)=I(\alpha)\cap Z(G)$.

**Proof.** $g\in G^{\sigma}$ and $\sigma=\iota\alpha$ give $g=\sigma(g)=\alpha(g)^{-1}$, that is $\alpha(g)=g^{-1}$; conversely $\alpha(g)=g^{-1}$ gives $\sigma(g)=\iota(\alpha(g))=\iota(g^{-1})=g$. Intersecting with the centre gives both inclusions.

**Remark.** The proposition is the compatibility of an involution with centrality in its sharpest form: on the centre, the involution $\sigma$ and the involutive automorphism $\alpha$ differ by the inversion, and the central fixed points of $\sigma$ are read off from $\alpha$ as the central elements it inverts. The next article, *The Centre of an Involutive Group*, develops the centre as an involutive group in its own right.

## Summary

For an involutive group $(G,\sigma)$ the **fixed set** $G^{\sigma}=\{g:\sigma(g)=g\}$ contains $e$, is closed under inversion, and is a **subgroup if and only if its elements commute pairwise**, equivalently if and only if $G^{\sigma}$ is abelian; the obstruction is the anti-multiplicativity, $\sigma(ab)=ba$, so that a product of two fixed elements is fixed exactly when they commute. When $G^{\sigma}$ is a subgroup it is the largest subgroup fixed pointwise by $\sigma$, it is abelian, and it is contained in its own centraliser and normaliser; for a $\sigma$-stable subgroup $H$ the fixed and inverted sets of the restriction are $H\cap G^{\sigma}$ and $H\cap I(\sigma)$.

The **inversion** is the canonical involution, and its fixed set is the $2$-torsion $G^{\iota}=\{g:g^{2}=e\}$. It is a subgroup exactly when the elements of order at most two commute pairwise and it is central exactly when those elements are central; the conditions are independent, $A_4$ giving a non-central subgroup $V_4$ and $S_3$ giving a set that is not a subgroup.

The centre $Z(G)$ is $\sigma$-stable and inherits an involution; its fixed points are $Z(G)\cap G^{\sigma}=I(\alpha)\cap Z(G)$, the central elements inverted by the associated involutive automorphism $\alpha=\sigma\iota$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$ | involution of $G$, an anti-automorphism with $\sigma^{2}=\mathrm{id}$ |
| $\alpha=\sigma\iota$ | the involutive automorphism associated with $\sigma$ |
| $G^{\sigma}$ | fixed set, a subgroup iff its elements commute pairwise |
| $I(\sigma)$ | inverted set, always a subgroup |
| $\sigma(ab)=\sigma(b)\sigma(a)$ | anti-multiplicativity, the source of the criterion |
| $G^{\iota}=\{g:g^{2}=e\}$ | $2$-torsion set, the fixed set of the inversion |
| $Z(G)\cap G^{\sigma}=I(\alpha)\cap Z(G)$ | central fixed points of $\sigma$ |
| $H^{\sigma|_H}=H\cap G^{\sigma}$ | fixed set of the restriction to a stable subgroup |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for involutions, their fixed points and the associated symmetric and alternating forms.
- Derek J. S. Robinson, *A Course in the Theory of Groups* (Springer, second edition, 1996), for the centre, the centraliser, the normaliser and automorphisms of order two.
- Joseph J. Rotman, *An Introduction to the Theory of Groups* (Springer, fourth edition, 1995), for involutions, the $2$-torsion and the small examples $S_3$, $A_4$, $Q_8$.
- I. Martin Isaacs, *Finite Group Theory* (American Mathematical Society, Graduate Studies in Mathematics 92, 2008), for fixed-point sets of automorphisms and their local properties.
