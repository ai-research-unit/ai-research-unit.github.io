
# __Involutive Group Actions__

## Introduction

When a group acts on a group that carries an involution, the action and the involution may be compatible, and then the involution descends to the invariants of the action and to the quotients the action defines. This article fixes that compatibility, proves that the fixed sets of the two structures are stable under the other, and follows the induced involutions to the quotient. It is the second of the involutive `*`-articles. The involution, its fixed and inverted sets, the induced involution on a quotient and the action of $\operatorname{Aut}(G)$ on the set of involutions are owned by *Involutive Groups*; the actions themselves, the orbits, the kernels and the equivariant maps are *Transformation Groups*.

Throughout, $(G,\sigma)$ is an involutive group, $\alpha=\sigma\iota$ is the associated involutive automorphism, and a **group of operators** is a group $\Gamma$ acting on $G$ by automorphisms, $\Gamma\to\operatorname{Aut}(G)$, written $\gamma\cdot g$.

## Actions Preserving an Involution

**Definition.** An action of $\Gamma$ on $G$ **preserves the involution** $\sigma$, or is **$\sigma$-compatible**, if

$$
\gamma\cdot\sigma(g)=\sigma(\gamma\cdot g) \qquad\text{for all } \gamma\in\Gamma,\ g\in G ,
$$

that is, if every operator commutes with $\sigma$. Equivalently, the image of $\Gamma\to\operatorname{Aut}(G)$ lies in the centraliser $C_{\operatorname{Aut}(G)}(\sigma)$.

**Proposition (the associated automorphism).** The action preserves $\sigma$ if and only if it preserves $\alpha=\sigma\iota$; and it then preserves the fixed set $G^{\sigma}$ and the inverted set $I(\sigma)$ setwise.

**Proof.** An operator $\gamma$ commutes with $\sigma$ if and only if it commutes with $\alpha=\sigma\iota$, because it commutes with the inversion automatically: $\gamma(g^{-1})=\gamma(g)^{-1}$ for an automorphism. If $\gamma$ commutes with $\sigma$ and $\sigma(g)=g$ then $\sigma(\gamma\cdot g)=\gamma\cdot\sigma(g)=\gamma\cdot g$, so $\gamma\cdot g$ is fixed; and if $\sigma(g)=g^{-1}$ then $\sigma(\gamma\cdot g)=\gamma\cdot\sigma(g)=(\gamma\cdot g)^{-1}$, so $\gamma\cdot g$ is inverted. Hence both sets are stable.

**Definition.** With the action preserving $\sigma$, the pair $(G,\sigma)$ is an **involutive $\Gamma$-group**, and the structures form a category whose objects are the involutive groups with a $\sigma$-compatible $\Gamma$-action; a **morphism** to $(H,\tau)$ is a group homomorphism $f:G\to H$ with $f\sigma=\tau f$ and $f(\gamma\cdot g)=\gamma\cdot f(g)$, a $\Gamma$-equivariant involution-preserving map.

**Remark (actions by anti-automorphisms).** An operator may also act by an anti-automorphism, and then the compatibility is read with a twist: if $\gamma$ acts by $\beta$, the requirement that $\beta\sigma$ be an involution forces the map $\gamma\mapsto\beta\sigma\beta^{-1}$ to agree with $\sigma$ up to the parity of $\gamma$. Such a twisted action is the group form of the semilinear maps of *Involutive Linear Spaces*; it is not needed here and is mentioned only to record that the untwisted case treated below is a choice.

## The Fixed Points of the Two Structures

The involution and the action each have their own fixed set, and each set is stable under the other structure.

**Proposition (the constants of the action are $\sigma$-stable).** The set of $\Gamma$-fixed points

$$
G^{\Gamma}=\{g\in G : \gamma\cdot g=g \ \text{for all } \gamma\in\Gamma\}
$$

is stable under $\sigma$, and $\sigma$ restricts to an involution of $G^{\Gamma}$.

**Proof.** If $g$ is fixed by every $\gamma$ then $\gamma\cdot\sigma(g)=\sigma(\gamma\cdot g)=\sigma(g)$, so $\sigma(g)$ is fixed; the restriction is an involution because $\sigma^{2}=\mathrm{id}$. The set $G^{\Gamma}$ is a subgroup because the $\gamma$ act by automorphisms, and the restriction is an involution of it.

**Corollary (the two fixed sets).** The intersection $G^{\sigma}\cap G^{\Gamma}$ is the set of points fixed by both; it is a subgroup whenever either of $G^{\sigma}$ or $G^{\Gamma}$ is one, and it is stable under both structures. If in addition the action preserves $\sigma$, then $\Gamma$ acts on $(G^{\sigma},\sigma|_{G^{\sigma}})$ and $\sigma$ acts on $(G^{\Gamma},\text{trivial})$, and the two orbits of a point $g\in G^{\sigma}\cap G^{\Gamma}$ under the two structures lie in the intersection.

**Proof.** The first statement is the previous proposition together with the $\Gamma$-stability of $G^{\sigma}$. The action on $G^{\sigma}$ is the restriction of the $\Gamma$-action, and it is $\sigma$-compatible because the ambient action is; the restriction of $\sigma$ to $G^{\Gamma}$ is the involution just constructed.

**Remark.** The two stabilities are reciprocal and both are consequences of the compatibility: $\Gamma$ preserves $G^{\sigma}$ because it preserves $\sigma$, and $\sigma$ preserves $G^{\Gamma}$ because $G^{\Gamma}$ is defined by equations the action satisfies. This reciprocality is the structural reason the invariants of an involutive group action carry an involution.

## The Induced Involution on Quotients

Let $N\trianglelefteq G$ be a $\sigma$-stable normal subgroup, so that $\sigma$ induces an involution $\bar\sigma$ of $G/N$ by $\bar\sigma(gN)=\sigma(g)N$; this is the induced involution of *Involutive Groups*, §7.

**Proposition (the action descends when the subgroup is stable).** Suppose $N$ is both $\sigma$-stable and $\Gamma$-stable. Then the action of $\Gamma$ descends to $G/N$, it preserves the induced involution $\bar\sigma$, and $(G/N,\bar\sigma)$ is an involutive $\Gamma$-group.

**Proof.** The action descends because $N$ is $\Gamma$-stable, giving $\gamma\cdot(gN)=(\gamma\cdot g)N$. For the compatibility, $\gamma\cdot\bar\sigma(gN)=\gamma\cdot(\sigma(g)N)=(\gamma\cdot\sigma(g))N=\sigma(\gamma\cdot g)N=\bar\sigma(\gamma\cdot gN)$ using that the ambient action preserves $\sigma$. So the descended action commutes with $\bar\sigma$.

**Proposition (the fixed points of the quotient).** With $N$ as above, the image of $G^{\sigma}$ in $G/N$ is contained in the fixed set $(G/N)^{\bar\sigma}$, and the containment can be strict. When $\sigma$ is an automorphism of $G$ and $N$ is a central subgroup of order two on which $\sigma$ acts trivially, the quotient of the two fixed sets is $N$ itself,

$$
(G/N)^{\bar\sigma}\big/\pi(G^{\sigma})\;\cong\;N/2N=N ,
$$

so the containment is strict, the image having index two in the fixed set of the quotient.

**Proof.** An element $\sigma(g)=g$ has image $\bar\sigma(gN)=\sigma(g)N=gN$, so $\pi(G^{\sigma})\subseteq(G/N)^{\bar\sigma}$; the containment is the one of *Involutive Groups*, §7, and the strict example $\mathbb{Z}/4\mathbb{Z}$ with its subgroup of order two, recorded there, shows it can be strict. A class $gN$ fixed by $\bar\sigma$ has $\sigma(g)=g\,n$ for some $n\in N$; replacing $g$ by $g\,n'$ with $n'\in N$ changes $n$ to $n'^{2}n$, because $N$ is central and $\sigma$ acts trivially on it, so the defect $n$ is fixed exactly up to the squares $N^{2}$ of $N$. For a central $N$ with trivial action the squares are $2N$ and the cokernel is the group $N/2N$ of coinvariants of the two-element group with coefficients in $N$; for $N$ of order two this is $N$ again, so the image has index two in the fixed set of the quotient. The $\mathbb{Z}/4\mathbb{Z}$ example of *Involutive Groups*, §7 is the case $N$ of order two inside the cyclic group of order four.

## The Equivariant Maps and the Quotient Category

**Proposition (the functoriality of the fixed points).** The constructions $G\mapsto G^{\sigma}$ and $G\mapsto G^{\Gamma}$ are functorial on the category of involutive $\Gamma$-groups: an equivariant involution-preserving map $f:(G,\sigma)\to(H,\tau)$ carries $G^{\sigma}$ to $H^{\tau}$ and $G^{\Gamma}$ to $H^{\Gamma}$.

**Proof.** If $\sigma(g)=g$ then $\tau(f(g))=f(\sigma(g))=f(g)$, so $f(G^{\sigma})\subseteq H^{\tau}$; and if $\gamma\cdot g=g$ then $\gamma\cdot f(g)=f(\gamma\cdot g)=f(g)$, so $f(G^{\Gamma})\subseteq H^{\Gamma}$. Composition and identity maps are preserved.

**Corollary (the quotient by a stable subgroup).** If $N$ is $\sigma$-stable and $\Gamma$-stable, the projection $\pi:G\to G/N$ is a morphism of involutive $\Gamma$-groups, and it factors every morphism whose kernel contains $N$. Hence the involutive $\Gamma$-groups are the objects of a category with kernels and quotients, and the fixed-point functors are left exact.

**Proof.** The projection preserves both structures by the descent proposition and is equivariant by construction; the factorisation is the universal property of the quotient in the category of groups. The left exactness is that $G^{\sigma}$ and $G^{\Gamma}$ are computed by equations that are preserved under taking kernels, so the corresponding sequences of fixed points are exact at the terms written.

## The Semidirect Product and the Extension

**Proposition (an involution on the semidirect product).** Let $\Gamma$ act on $G$ preserving $\sigma$, and let $\Gamma$ carry an involution $\tau$. If the action is $\tau$-twisted, that is $\tau(\gamma)\cdot\tau(g)=\tau(\gamma\cdot g)$ for all $\gamma,g$, then

$$
\Theta(g,\gamma)=\bigl(\sigma(g),\ \tau(\gamma)\bigr)
$$

is an involution of the semidirect product $G\rtimes\Gamma$, and its restriction to $G$ is $\sigma$. If $\tau=\mathrm{id}$ this reduces to $\Theta(g,\gamma)=(\sigma(g),\gamma)$.

**Proof.** That $\Theta$ is a bijection with $\Theta^{2}=\mathrm{id}$ is immediate from $\sigma^{2}=\tau^{2}=\mathrm{id}$. It is anti-multiplicative on the semidirect product, using that $\Gamma$ acts by automorphisms of $G$:

$$
\Theta\bigl((g,\gamma)(g',\gamma')\bigr)=\Theta\bigl(g\,(\gamma\cdot g'),\gamma\gamma'\bigr)
=\bigl(\sigma(g\,(\gamma\cdot g')),\ \tau(\gamma\gamma')\bigr)
=\bigl(\sigma(\gamma\cdot g')\sigma(g),\ \tau(\gamma')\tau(\gamma)\bigr),
$$

while

$$
\Theta(g',\gamma')\Theta(g,\gamma)=\bigl(\sigma(g')\,(\tau(\gamma')\cdot\sigma(g)),\ \tau(\gamma')\tau(\gamma)\bigr).
$$

The two are equal when $\sigma(\gamma\cdot g')=\tau(\gamma')\cdot\sigma(g)$, which is the twisted compatibility applied to $\gamma\cdot g'$ and rearranged; with $\tau=\mathrm{id}$ it is the plain compatibility $\sigma(\gamma\cdot g')=\gamma'\cdot\sigma(g)$.

**Remark (the two roles of the action).** The construction reads the action twice: once to form the semidirect product, and once through the compatibility that makes the involution of the extension. When the action is trivial, $G\rtimes\Gamma=G\times\Gamma$ and the involution is the componentwise one of *Involutive Groups*, §8.

## Summary

An action of $\Gamma$ on an involutive group $(G,\sigma)$ **preserves the involution** when every operator commutes with $\sigma$, equivalently when the image of $\Gamma\to\operatorname{Aut}(G)$ lies in $C_{\operatorname{Aut}(G)}(\sigma)$; it then preserves $\sigma$, the associated automorphism $\alpha$, the fixed set $G^{\sigma}$ and the inverted set $I(\sigma)$. The **$\Gamma$-fixed points** $G^{\Gamma}$ are $\sigma$-stable, so $\sigma$ restricts to an involution of $G^{\Gamma}$, and the two fixed sets $G^{\sigma}$ and $G^{\Gamma}$ are mutually stable; their intersection carries both structures.

For a normal subgroup $N$ that is both $\sigma$-stable and $\Gamma$-stable the involution and the action both descend to $G/N$, the descended action preserves the induced involution, and the projection is a morphism of involutive $\Gamma$-groups; the image of $G^{\sigma}$ lies in the fixed set of the quotient and the containment can be strict. The fixed-point constructions $G\mapsto G^{\sigma}$ and $G\mapsto G^{\Gamma}$ are functorial and left exact. Finally, an involutive group $\Gamma$ acting with a compatible involution $\tau$ makes $G\rtimes\Gamma$ an involutive group by $\Theta(g,\gamma)=(\sigma(g),\tau(\gamma))$, an extension of the involution of $G$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\gamma\cdot\sigma(g)=\sigma(\gamma\cdot g)$ | compatibility of the action with the involution |
| $C_{\operatorname{Aut}(G)}(\sigma)$ | operators commuting with $\sigma$ |
| $G^{\Gamma}=\{g:\gamma\cdot g=g\}$ | $\Gamma$-fixed points, stable under $\sigma$ |
| $G^{\sigma}\cap G^{\Gamma}$ | points fixed by both structures |
| $\bar\sigma(gN)=\sigma(g)N$ | induced involution on $G/N$, $N$ $\sigma$-stable |
| $f\sigma=\tau f$ | involution-preserving equivariant map |
| $\Theta(g,\gamma)=(\sigma(g),\tau(\gamma))$ | involution of the semidirect product |

## Further Reading

- Derek J. S. Robinson, *A Course in the Theory of Groups* (Springer, second edition, 1996), for group actions and invariance under automorphisms of the acting group.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for involutions compatible with a group action and the semilinear case.
- Joseph J. Rotman, *An Introduction to the Theory of Groups* (Springer, fourth edition, 1995), for semidirect products and actions by automorphisms.
- Nathan Jacobson, *Lie Algebras* (Interscience, 1962), for the twisted action of a group with an involution on an algebra with one.
