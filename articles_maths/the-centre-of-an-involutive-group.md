
# __The Centre of an Involutive Group__

## Introduction

The centre of a group is defined by commutation with everything, and an involution, being a bijection preserving the product up to order, cannot disturb it: the centre is stable, and it inherits an involution of its own. What is less immediate is the interaction of the involution with the two groups the centre is read against, its own fixed set and the derived subgroup, and the way the centre of the semidirect product by the involution is computed. This article treats the centre as an involutive group in its own right and records the compatibility of the involution with centrality and with the commutator subgroup. It is the fifth of the involutive `*`-articles; the involution, its induced map on the abelianisation and the fixed and inverted sets are owned by *Involutive Groups*, and the centre itself by *Groups*.

Throughout, $(G,\sigma)$ is an involutive group, $\alpha=\sigma\iota$ is the associated involutive automorphism, $Z(G)$ is the centre, $[G,G]$ is the derived subgroup, and $G^{\mathrm{ab}}=G/[G,G]$ is the abelianisation.

## The Centre Is Stable and Inherits an Involution

**Proposition (stability of the centre).** $\sigma(Z(G))=Z(G)$ and $\alpha(Z(G))=Z(G)$; the restrictions $\sigma|_{Z(G)}$ and $\alpha|_{Z(G)}$ are involutions of the abelian group $Z(G)$.

**Proof.** If $g$ is central and $x\in G$ then $\sigma(g)\,x=\sigma(g\,\sigma^{-1}(x))=\sigma(\sigma^{-1}(x)\,g)=x\,\sigma(g)$, so $\sigma(g)$ is central; applying $\sigma$ again gives the reverse inclusion, hence equality. The same argument with $\alpha$ in place of $\sigma$ uses that $\alpha$ is an automorphism with inverse $\alpha$. The restrictions are involutions because the ambient maps are, and they are involutions of the abelian group $Z(G)$.

**Remark (the restrictions are two involutions).** On the abelian group $Z(G)$ the two restrictions $\sigma|_{Z(G)}$ and $\alpha|_{Z(G)}$ satisfy $\sigma|_{Z(G)}=\iota_{Z(G)}\,\alpha|_{Z(G)}$ and are related by the inversion of $Z(G)$; on an abelian group an anti-automorphism is an automorphism as soon as the group is abelian, so both are automorphisms of order two.

**Proposition (the fixed and inverted sets of the restriction).** For the restricted involution,

$$
Z(G)^{\sigma|_{Z(G)}}=Z(G)\cap G^{\sigma}=Z(G)\cap I(\alpha)=I(\alpha)\cap Z(G),
$$
$$
I(\sigma|_{Z(G)})=Z(G)\cap I(\sigma)=Z(G)\cap G^{\alpha}=G^{\alpha}\cap Z(G).
$$

**Proof.** Each equality is the definition of the fixed or inverted set restricted to the centre, together with the dual identities $G^{\sigma}=I(\alpha)$ and $I(\sigma)=G^{\alpha}$ of *Involutions and the Fixed-Point Subgroup*.

**Corollary (the central fixed points).** The fixed points of the involution on the centre are the central elements inverted by $\alpha$; the inverted points of the involution on the centre are the central elements fixed by $\alpha$. In particular $Z(G)\subseteq G^{\sigma}$ if and only if $\alpha$ inverts every central element.

**Proof.** The first two statements are the proposition; the third is its first identity read with $Z(G)\subseteq Z(G)\cap G^{\sigma}$ as $Z(G)\subseteq G^{\sigma}$.

## Compatibility with Centrality

**Proposition (the involution preserves central elements and centralisers).** $\sigma$ carries central elements to central elements and the centraliser of $x$ onto the centraliser of $\sigma(x)$; equivalently $c_{\sigma(x)}=\sigma c_x\sigma^{-1}$ under the action of $\sigma$ by conjugation on the automorphisms. The same holds for $\alpha$.

**Proof.** The first statement is the stability of the centre. For the centralisers, $y\in C_G(x)$ means $yx=xy$; applying $\sigma$ gives $\sigma(x)\sigma(y)=\sigma(y)\sigma(x)$, that is $\sigma(y)\in C_G(\sigma(x))$, and $\sigma$ is a bijection. The conjugation form is the definition of the conjugate automorphism.

**Proposition (the involution on a central subgroup).** A subgroup $H\leq Z(G)$ is $\sigma$-stable if and only if it is $\alpha$-stable, and then $\sigma$ restricts to an involution of the abelian group $H$. In particular the fixed subgroup $G^{\sigma}$ meets the centre in the elements of order at most two that $\sigma$ fixes, and the inverted set meets it in the elements of order at most two that $\sigma$ inverts.

**Proof.** By the proposition above, a central element is fixed by $\sigma$ exactly when it is inverted by $\alpha$, and it is inverted by $\sigma$ exactly when it is fixed by $\alpha$; for central elements the two structures are exchanged by the inversion. A central element fixed by $\sigma$ and inverted by it is its own inverse, that is of order at most two.

## Compatibility with the Commutator Subgroup

**Proposition (the derived subgroup is stable).** $[G,G]$ is $\sigma$-stable, and more precisely

$$
\sigma([a,b])=\bigl[\sigma(b)^{-1},\,\sigma(a)^{-1}\bigr]=[\sigma(a),\sigma(b)],
$$

Consequently $\sigma$ induces an involution $\sigma^{\mathrm{ab}}$ of the abelianisation $G^{\mathrm{ab}}$, and for the inversion the induced map is the inversion of the abelian group $G^{\mathrm{ab}}$.

**Proof.** Writing $[a,b]=aba^{-1}b^{-1}$ and using that $\sigma$ reverses products, $\sigma([a,b])=\sigma(b)^{-1}\sigma(a)^{-1}\sigma(b)\sigma(a)=[\sigma(b)^{-1},\sigma(a)^{-1}]$, a commutator; the identity $[\sigma(b)^{-1},\sigma(a)^{-1}]=[\sigma(a),\sigma(b)]$ is the general one $[y^{-1},x^{-1}]=[x,y]$. The subgroup generated by the commutators is therefore carried into itself, and the reverse inclusion follows by applying $\sigma$ again. The induced map on $G/[G,G]$ is well defined because the subgroup is stable, and it is an involution because $\sigma$ is. For the inversion, $\iota([a,b])=[b,a]=[a,b]^{-1}$, so the induced map inverts every commutator and hence every class, that is the inversion of the abelian group $G^{\mathrm{ab}}$, as recorded in *Involutive Groups*, §3.

**Proposition (the centre of the abelianisation).** The image of the centre lies in the centre of the abelianisation and is $\sigma^{\mathrm{ab}}$-stable: $Z(G)\,[G,G]/[G,G]\subseteq Z(G^{\mathrm{ab}})$, and $\sigma^{\mathrm{ab}}$ restricts to the image of $\sigma|_{Z(G)}$.

**Proof.** A central element commutes with every element of $G$, so its class commutes with every class in $G^{\mathrm{ab}}$; the stability is the stability of the centre under the induced map, since $\sigma([G,G])=[G,G]$ and $\sigma(Z(G))=Z(G)$.

**Corollary (centrality descends).** The induced involution $\sigma^{\mathrm{ab}}$ of $G^{\mathrm{ab}}$ has fixed set containing the image of $G^{\sigma}$ and inverted set containing the image of $I(\sigma)$; both containments can be strict.

**Proof.** An element fixed by $\sigma$ maps to a class fixed by $\sigma^{\mathrm{ab}}$, by functoriality of the abelianisation; the strictness is the general strictness of the image of a fixed set in a quotient, recorded in *Involutive Groups*, §7, on $\mathbb{Z}/4\mathbb{Z}$ with the inversion.

## The Centre of the Extension

Let $t$ act on $G$ by $\alpha$ in the semidirect product $G\rtimes\langle t\rangle$ of *Involutive Groups*, §9, so that $(g,t^{i})(x,t^{j})=(g\,\alpha^{i}(x),\,t^{i+j})$.

**Proposition (the central elements of the extension).** The centre of the extension is described in two parts:

$$
Z\bigl(G\rtimes\langle t\rangle\bigr)\cap G = Z(G)\cap G^{\alpha},
$$

and an element $(g,t)$ with a nontrivial $t$-component is central if and only if $\alpha$ is inner and $c_{g}=\alpha$. Hence the centre is $\bigl(Z(G)\cap G^{\alpha}\bigr)\times\langle t\rangle$ when $\alpha=\mathrm{id}$, it is $\bigl(Z(G)\cap G^{\alpha}\bigr)$ together with the single coset $(g_{0}\,Z(G)\cap G^{\alpha},\,t)$ when $\alpha$ is an inner involution $c_{g_{0}}\neq\mathrm{id}$, and it has no element outside $G$ when $\alpha$ is not inner.

**Proof.** An element $(g,e)$ commutes with $(x,e)$ for all $x$ exactly when $g\in Z(G)$, and it commutes with $(e,t)$ exactly when $g\in G^{\alpha}$; so $(g,e)$ is central exactly for $g\in Z(G)\cap G^{\alpha}$. An element $(g,t)$ commutes with $(x,e)$ exactly when $g\,\alpha(x)=x\,g$ for all $x$, that is $c_g\alpha=\mathrm{id}$, or $\alpha=c_{g^{-1}}$; and it then commutes with $(e,t)$ automatically, since $c_{g^{-1}}(g)=g$, which is the condition $g=\alpha(g)$ already contained in $\alpha=c_{g^{-1}}$ evaluated at $g$. So a central element with $t$-component exists exactly when $\alpha$ is inner, and then all such elements are $(g\,z,t)$ with $z\in Z(G)\cap G^{\alpha}$, one coset.

**Corollary (the two extreme cases).** If $\alpha=\mathrm{id}$ the extension is the direct product $G\times C_2$ and its centre is $Z(G)\times C_2$. If $\alpha=\iota$, so that the extension is dihedral when $G$ is cyclic, then $\alpha$ is inner only when $G$ has exponent two, and $Z(G\rtimes\langle t\rangle)=Z(G)\cap G^{\alpha}=Z(G)$ otherwise.

**Proof.** For $\alpha=\mathrm{id}$ the semidirect product is the direct product and the centre is the product of the centres. For $\alpha=\iota$ the inner condition $c_{g}=\iota$ means $x g x^{-1}=g^{-1}$ for every $x$, which for abelian $G$ forces $g=g^{-1}$ and hence exponent two; when it fails, no $(g,t)$ is central, and the centre is $Z(G)\cap G^{\alpha}=Z(G)$ because $\alpha=\iota$ fixes the central elements of order at most two, which for the abelian $Z(G)$ is all of them only in the exponent-two case already excluded.

## Summary

The centre of an involutive group is stable under the involution, $\sigma(Z(G))=Z(G)$, so the centre is an abelian involutive group in its own right; its fixed and inverted sets are $Z(G)\cap G^{\sigma}=Z(G)\cap I(\alpha)$ and $Z(G)\cap I(\sigma)=Z(G)\cap G^{\alpha}$, exchanged by the inversion. The involution carries centralisers to centralisers and central elements to central elements, so a central element is fixed by $\sigma$ exactly when the associated automorphism $\alpha$ inverts it and inverted by $\sigma$ exactly when $\alpha$ fixes it; a central element both fixed and inverted has order at most two.

The derived subgroup is stable, with $\sigma([a,b])=[\sigma(b)^{-1},\sigma(a)^{-1}]$, so the involution descends to the abelianisation and the image of the centre lies in its centre, stabilizing under the descended involution. Finally, in the semidirect product $G\rtimes\langle t\rangle$ the centre meets $G$ in $Z(G)\cap G^{\alpha}$, and it has an element outside $G$ exactly when $\alpha$ is inner, in which case the elements $(g,t)$ with $c_g=\alpha$ form one coset.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma(Z(G))=Z(G)$ | the centre is stable under the involution |
| $Z(G)\cap G^{\sigma}=Z(G)\cap I(\alpha)$ | fixed points of the involution on the centre |
| $Z(G)\cap I(\sigma)=Z(G)\cap G^{\alpha}$ | inverted points of the involution on the centre |
| $\sigma([a,b])=[\sigma(b)^{-1},\sigma(a)^{-1}]$ | the derived subgroup is stable |
| $\sigma^{\mathrm{ab}}$ | induced involution on $G^{\mathrm{ab}}$ |
| $Z(G\rtimes\langle t\rangle)$ | centre of the extension |

## Further Reading

- Derek J. S. Robinson, *A Course in the Theory of Groups* (Springer, second edition, 1996), for the centre, the derived subgroup, the abelianisation and central series.
- Joseph J. Rotman, *An Introduction to the Theory of Groups* (Springer, fourth edition, 1995), for centres of semidirect products and the calculation of $Z(G)$ in the small groups.
- I. Martin Isaacs, *Finite Group Theory* (American Mathematical Society, Graduate Studies in Mathematics 92, 2008), for the centre and the commutator structure under automorphisms.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for involutions and centrality in the algebraic setting.
