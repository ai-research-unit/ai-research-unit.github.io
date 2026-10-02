
# __Free Involutions and the Quotient__

## Introduction

An involution of a group always fixes the identity, and it is **free** when it fixes nothing else. A free involution generates an action of the two-element group on the underlying set whose orbits are all of size two, so the orbit space is a quotient over which the involution is invisible, and the projection is a two-to-one map. This article fixes the notion, constructs the quotient and the double cover, and treats the two standard instances: the inversion on a group with no element of order two, whose extension is dihedral, and the negation on the additive group of a field of characteristic not two. It is the third of the involutive `*`-articles; the involution, its fixed set, the associated involutive automorphism and the split extension are owned by *Involutive Groups*, and the action of a group on an involutive group by *Involutive Group Actions*.

Throughout, $(G,\sigma)$ is an involutive group with $\sigma$ an anti-automorphism of order two, $\alpha=\sigma\iota$ is the associated involutive automorphism, $G^{\sigma}=\{g:\sigma(g)=g\}$ and $I(\sigma)=\{g:\sigma(g)=g^{-1}\}$ are the fixed and inverted sets, and $\iota$ is the inversion.

## Free Involutions and Their Dual

**Definition.** The involution $\sigma$ is **free**, or **fixed-point-free**, if $G^{\sigma}=\{e\}$. The involutive automorphism $\alpha$ is **free** if $G^{\alpha}=\{e\}$.

**Proposition (the two fixed sets in dual form).** $G^{\sigma}=I(\alpha)$ and $G^{\alpha}=I(\sigma)$. Hence $\sigma$ is free if and only if $I(\alpha)=\{e\}$, and $\alpha$ is free if and only if $I(\sigma)=\{e\}$.

**Proof.** $g\in G^{\sigma}$ means $\sigma(g)=g$; applying $\iota$ and using $\alpha=\sigma\iota$ gives $\alpha(g)=g^{-1}$, that is $g\in I(\alpha)$. The second statement is the same with the roles of $\sigma$ and $\alpha$ exchanged, and the versions for freeness follow. Both identities are recorded in *Involutive Groups*, §4.

**Remark (the two notions are dual and not equivalent).** Freeness of $\sigma$ and freeness of $\alpha$ are different conditions, and neither implies the other. On the cyclic group $C_3=\langle r\rangle$ the inversion $\sigma=\iota$, which is an automorphism because $C_3$ is abelian, is free: $\sigma(r)=r^{-1}\neq r$ and $\sigma(r^{2})=r\neq r^{2}$. Its associated automorphism is $\alpha=\sigma\iota=\mathrm{id}$, which fixes every element and is as far from free as possible. So a free involution may have an associated automorphism that is not free. The asymmetry is exactly the asymmetry between the fixed and the inverted sets.

**Proposition (the canonical free involution).** The inversion $\iota$ is free if and only if $G$ has no element of order two; for a finite group this is the condition that $\lvert G\rvert$ is odd.

**Proof.** $\iota(g)=g$ is $g^{-1}=g$, that is $g^{2}=e$; so the fixed set of the inversion is the $2$-torsion of $G$, which is $\{e\}$ exactly when no element of order two exists. A finite group has an element of order two exactly when its order is even (Cauchy's theorem).

**Proposition (the injectivity of the conjugate product).** If $\sigma$ is free, the map

$$
\varphi : G\longrightarrow G, \qquad \varphi(g)=g^{-1}\sigma(g),
$$

is injective. If $G$ is finite it is therefore a bijection, and every element of $G$ is the conjugate product of a unique pair $(g^{-1},\sigma(g))$.

**Proof.** If $\varphi(g)=\varphi(h)$ then $g^{-1}\sigma(g)=h^{-1}\sigma(h)$, so $hg^{-1}=\sigma(h)\sigma(g)^{-1}=\sigma(hg^{-1})$, and $hg^{-1}\in G^{\sigma}$; freeness gives $hg^{-1}=e$ and $g=h$. Finiteness makes injective bijective.

## The Quotient and the Double Cover

**Definition.** The **orbit quotient** of a free involution $\sigma$ is the set of orbits

$$
G/\langle\sigma\rangle = \{\,\{g,\sigma(g)\} : g\in G\,\} ,
\qquad \pi : G\longrightarrow G/\langle\sigma\rangle, \quad \pi(g)=\{g,\sigma(g)\}.
$$

**Proposition (the projection is a double cover).** The projection $\pi$ is surjective, every fibre has exactly two elements, and $\sigma$ is its nontrivial deck transformation: $\pi\sigma=\pi$ and $\sigma(g)\neq g$ for $g\neq e$. For finite $G$, $\lvert G/\langle\sigma\rangle\rvert=\lvert G\rvert/2$.

**Proof.** The fibre over $\{g,\sigma(g)\}$ is that orbit, of size two because $\sigma(g)=g$ forces $g=e$ and an orbit of a non-identity element has two members. And $\pi(\sigma(g))=\{\sigma(g),\sigma^{2}(g)\}=\{g,\sigma(g)\}=\pi(g)$. The count is the orbit-counting of a free action of a two-element group (*Transformation Groups*).

**Proposition (the quotient is not a group in the natural way).** For $G\neq\{e\}$ the quotient $G/\langle\sigma\rangle$ carries no group structure for which $\pi$ is a homomorphism.

**Proof.** A homomorphism with trivial kernel is injective: if $\pi(g)=\pi(h)$ then $\pi(gh^{-1})=\pi(g)\pi(h)^{-1}=e$, so $gh^{-1}\in\ker\pi=\{e\}$ and $g=h$. But $\pi$ is two-to-one on the non-identity elements, so it is not injective; no such group structure exists.

**Definition.** The quotient is the **base** and $\pi$ the **double cover**. The **group-theoretic double cover** attached to the involutive automorphism $\alpha$ is the split extension

$$
1\longrightarrow G\longrightarrow G\rtimes\langle t\rangle\longrightarrow \langle t\rangle\longrightarrow 1,
\qquad t^{2}=e,
$$

of *Involutive Groups*, §9, a group of order $2\lvert G\rvert$ in which $G$ is normal of index two and conjugation by $t$ realises $\alpha$.

**Remark (which involution is free).** The set-theoretic quotient and double cover are built from the involution $\sigma$ and only need it to be an involution. The group-theoretic extension is built from the involutive automorphism $\alpha$, which is the datum that acts on $G$ by automorphisms; the two agree when $\sigma$ is itself an automorphism, that is when $G$ is abelian.

## The Finite Case

**Theorem.** A finite abelian group admitting a free involutive automorphism is of odd order, and the automorphism is the inversion. Hence its group-theoretic double cover is the dihedral group of the group.

**Proof.** Let $G$ be finite abelian and $\alpha$ a free involutive automorphism. The map $\psi(g)=\alpha(g)g^{-1}$ is an endomorphism of $G$, and its kernel is $G^{\alpha}=\{e\}$; being injective on a finite group, it is bijective. Now

$$
\psi(\alpha(g))=\alpha^{2}(g)\alpha(g)^{-1}=g\,\alpha(g)^{-1}=\bigl(\alpha(g)g^{-1}\bigr)^{-1}=\psi(g)^{-1}=\psi(g^{-1}),
$$

so $\psi(\alpha(g))=\psi(g^{-1})$; injectivity of $\psi$ gives $\alpha(g)=g^{-1}$ for every $g$. Finally $\alpha(g)=g^{-1}$ has fixed set the $2$-torsion, which is $\{e\}$ exactly when the order is odd.

**Corollary (the general finite statement).** A finite group admitting a free involutive automorphism is abelian of odd order with the inversion as the automorphism. The abelian case is proved above; the general case is a theorem of the finite-group literature and is stated here without proof.

## The Standard Examples

**Example (the dihedral example).** Let $G=C_n=\langle r\rangle$ with $n$ odd and let $\sigma=\iota$ be the inversion, which is an automorphism because $C_n$ is abelian and is free because $n$ is odd. The orbits are the pairs $\{r^{k},r^{-k}\}$, the quotient has $(n+1)/2$ elements, and the group-theoretic double cover is the dihedral group $D_n=C_n\rtimes C_2$ of *Involutive Groups*, §9, in which the complement acts by the inversion $r\mapsto r^{-1}$. In $D_n$ the rotations are the paired elements and the reflections are the added coset; the double cover $C_n\to C_n/\langle\iota\rangle$ is the shadow of the split extension on the underlying sets.

**Example (the antipodal example).** Let $F$ be a field of characteristic different from two and let $G=(F,+)$ be its additive group with $\sigma(x)=-x$. The involution is free, since $-x=x$ is $2x=0$ and $2$ is invertible in $F$; the orbits are the antipodal pairs $\{x,-x\}$, and the quotient has one point for each pair. The group-theoretic double cover is the semidirect product $F\rtimes C_2$ in which the complement acts by negation. Over a field of characteristic two the negation is the identity, which is not free, so freeness is a property of the pair (group, field) and not of the additive group alone.

**Example (the infinite case).** Let $G=(\mathbb{Z},+)$ with $\sigma(n)=-n$. The involution is free, the quotient has countably many pairs, and the extension is the infinite dihedral group $\mathbb{Z}\rtimes C_2$. The conjugate-product map of the first section is $\varphi(n)=-2n$ in additive notation, a bijection of $\mathbb{Z}$; the finite theorem does not apply, but the quotient and the double cover are constructed in the same way.

**Remark (the two examples in one).** The dihedral and antipodal examples are the same construction read on two free involutions: the inversion of a cyclic group of odd order, and the negation of the additive group of a field of characteristic different from two. Both are free, both give a two-to-one quotient, and both extend to a semidirect product by the two-element group; they differ in the size and in the nature of the group, one finite and cyclic, the other the additive group of a field.

## Summary

An involution $\sigma$ of $G$ is **free** when $G^{\sigma}=\{e\}$, and the associated automorphism $\alpha=\sigma\iota$ is free when $G^{\alpha}=\{e\}$; by the dual identities $G^{\sigma}=I(\alpha)$ and $G^{\alpha}=I(\sigma)$ the two notions are the vanishing of the two inverted sets, and neither implies the other, as $C_3$ with its free inversion and its identity automorphism shows. The canonical free involution is the inversion on a group with no element of order two; on a finite group this is odd order.

A free involution generates a free action of the two-element group on the underlying set, so every orbit has two elements and the **orbit quotient** $G/\langle\sigma\rangle$ is a set with a **two-to-one projection** $\pi$, the **double cover**, whose nontrivial deck transformation is $\sigma$ and whose cardinality is $\lvert G\rvert/2$ for finite $G$. The projection carries no group structure, because a homomorphism with trivial kernel is injective and $\pi$ is two-to-one. The group-theoretic double cover uses the involutive automorphism $\alpha$ and is the split extension $G\rtimes C_2$ of *Involutive Groups*, §9.

A finite abelian group with a free involutive automorphism has odd order and the automorphism is the inversion, the abelian case being proved by the bijectivity of $g\mapsto\alpha(g)g^{-1}$; the general finite case, without the abelian hypothesis, is a theorem of the literature. The standard free involutions are the inversion of a cyclic group of odd order, whose extension is the dihedral group, and the negation of the additive group of a field of characteristic different from two, the antipodal involution.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| free, $G^{\sigma}=\{e\}$ | the involution fixes only the identity |
| $G^{\sigma}=I(\alpha)$ | dual identity for the fixed and inverted sets |
| $\varphi(g)=g^{-1}\sigma(g)$ | injective map of a free involution |
| $G/\langle\sigma\rangle$ | orbit quotient, the base of the double cover |
| $\pi(g)=\{g,\sigma(g)\}$ | two-to-one projection, the double cover |
| $\lvert G/\langle\sigma\rangle\rvert=\lvert G\rvert/2$ | orbit count for a finite free involution |
| $G\rtimes C_2$ | group-theoretic double cover, the split extension |
| $\psi(g)=\alpha(g)g^{-1}$ | bijective endomorphism proving $\alpha=\iota$ in the abelian case |

## Further Reading

- Joseph J. Rotman, *An Introduction to the Theory of Groups* (Springer, fourth edition, 1995), for free actions, orbit counting and the dihedral and infinite dihedral groups.
- Derek J. S. Robinson, *A Course in the Theory of Groups* (Springer, second edition, 1996), for fixed-point-free automorphisms and the structure they force.
- Daniel Gorenstein, *Finite Groups* (Harper and Row, 1968), for the theorem that a finite group with a fixed-point-free automorphism of order two is abelian.
- John D. Dixon and Brian Mortimer, *Permutation Groups* (Springer, Graduate Texts in Mathematics 163, 1996), for free permutation actions and their quotients.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for involutions and their quotients.
