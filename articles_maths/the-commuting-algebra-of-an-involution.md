
# __The Commuting Algebra of an Involution__

## Introduction

An involutive automorphism $\alpha$ of a group $G$ has a fixed subgroup $G^{\alpha}$, and it also has a larger set of elements with which it is compatible in a weaker sense: those whose inner automorphism commutes with $\alpha$. That set is a subgroup, it contains the fixed subgroup and the centre, and it is exactly the set of elements whose conjugacy defect under $\alpha$ is central. It is the group-level form of the centraliser of the involution, and it is what this article calls the commuting algebra of the involution; the name is justified at the end, where the group algebra is mentioned, and the group itself is the object throughout. The article is the fourth of the involutive `*`-articles; the fixed subgroup is owned by *Involutions and the Fixed-Point Subgroup*, the semidirect product by *Involutive Groups*, §9, and the inner automorphism group by *The Conjugation Representation*.

Throughout, $(G,\sigma)$ is an involutive group, $\alpha=\sigma\iota$ is the associated involutive automorphism, $\iota$ is the inversion, $c_g$ is the inner automorphism $x\mapsto gxg^{-1}$, and the action of a subgroup on the fixed subgroup follows *Involutive Group Actions*.

## The Commuting Subgroup

**Definition.** An element $g\in G$ **commutes with the involutive automorphism** $\alpha$ if the inner automorphism $c_g$ commutes with $\alpha$ as a map, $c_g\alpha=\alpha c_g$. The **commuting set** is

$$
C_G(\alpha)=\{g\in G : c_g\alpha=\alpha c_g\}.
$$

**Proposition (the commuting condition is centrality of the defect).** For $g\in G$,

$$
c_g\alpha=\alpha c_g \quad\Longleftrightarrow\quad g\,\alpha(g)^{-1}\in Z(G) \quad\Longleftrightarrow\quad \alpha(g)\,g^{-1}\in Z(G).
$$

**Proof.** Writing the composition out, $c_g\alpha(x)=g\alpha(x)g^{-1}$ and $\alpha c_g(x)=\alpha(gxg^{-1})=\alpha(g)\alpha(x)\alpha(g)^{-1}$ for all $x$; the two are equal for all $x$ exactly when $g^{-1}\alpha(g)$ centralises $\alpha(G)=G$, that is $g^{-1}\alpha(g)\in Z(G)$. The second form is the inverse of the first.

**Theorem (the commuting set is a subgroup).** $C_G(\alpha)$ is a subgroup of $G$ containing $Z(G)$ and $G^{\alpha}$.

**Proof.** The identity commutes with $\alpha$. If $g\in C_G(\alpha)$ then $\alpha(g^{-1})=\alpha(g)^{-1}=(z g)^{-1}=g^{-1}z^{-1}$ for some $z\in Z(G)$, so $g^{-1}\alpha(g^{-1})^{-1}=g^{-1}\alpha(g)=g^{-1}zg\in Z(G)$, and $g^{-1}\in C_G(\alpha)$. If $g,h\in C_G(\alpha)$, write $\alpha(g)=z_1g$ and $\alpha(h)=z_2h$ with $z_1,z_2\in Z(G)$; then $\alpha(gh)=z_1z_2\,gh$, so $(gh)\alpha(gh)^{-1}=(z_1z_2)^{-1}\in Z(G)$ and $gh\in C_G(\alpha)$. The centre is contained because a central $g$ has $c_g=\mathrm{id}$, which commutes with everything; the fixed subgroup is contained because $\alpha(g)=g$ gives $g\alpha(g)^{-1}=e$.

**Proposition (the form of $\alpha$ on the commuting subgroup).** The restriction $\alpha|_{C_G(\alpha)}$ multiplies by a central element: the map

$$
z : C_G(\alpha)\longrightarrow Z(G), \qquad z(g)=\alpha(g)\,g^{-1},
$$

is a homomorphism whose kernel is the fixed subgroup $G^{\alpha}$, and $\alpha(g)=z(g)g$ for every $g\in C_G(\alpha)$.

**Proof.** The containment in $Z(G)$ is the proposition above. The multiplicativity follows from the central value: $z(gh)=\alpha(gh)(gh)^{-1}=\alpha(g)\alpha(h)h^{-1}g^{-1}=\alpha(g)z(h)g^{-1}=z(h)\alpha(g)g^{-1}=z(h)z(g)$, using that $z(h)$ is central. The kernel is $\{g:\alpha(g)g^{-1}=e\}=\{g:\alpha(g)=g\}=G^{\alpha}$.

**Corollary (the exact sequence).** The homomorphism $z$ realises the commuting subgroup as an extension of the fixed subgroup by a subgroup of the centre, and the image of $G\to\operatorname{Inn}(G)$ on $C_G(\alpha)$ is exactly the centraliser $C_{\operatorname{Inn}(G)}(\alpha)$ of $\alpha$ in the inner automorphism group. Consequently

$$
C_G(\alpha)/Z(G)\ \cong\ C_{\operatorname{Inn}(G)}(\alpha),
\qquad\text{and}\qquad C_G(\alpha)/G^{\alpha}\ \cong\ \operatorname{im}z\ \leq Z(G).
$$

**Proof.** The first isomorphism is that the kernel of $G\to\operatorname{Inn}(G)$ is $Z(G)$ and the image on $C_G(\alpha)$ is the set of inner automorphisms commuting with $\alpha$. The second is the first isomorphism theorem applied to $z$.

## Relation to the Fixed Subgroup

**Proposition (the containment and its failure to be an equality).** $G^{\alpha}\subseteq C_G(\alpha)$, and the inclusion is in general strict. It is an equality exactly when every element commuting with $\alpha$ is fixed by it, that is when $\alpha$ has no central defect on $C_G(\alpha)$.

**Proof.** The containment is the theorem. For the strictness, in the dihedral group $D_4=\langle r,s\mid r^{4}=s^{2}=e,\ srs=r^{-1}\rangle$ take $\alpha=c_s$, the conjugation by the reflection $s$; then $G^{\alpha}=C_{D_4}(s)=\{e,r^{2},s,sr^{2}\}$ has four elements, while $r\notin G^{\alpha}$ yet $r\alpha(r)^{-1}=r\cdot r=r^{2}\in Z(D_4)=\{e,r^{2}\}$, so $r\in C_G(\alpha)$ and the containment is strict.

**Proposition (the commuting subgroup of the identity and of the inversion).** If $\alpha=\mathrm{id}$ then $C_G(\alpha)=G$; if $\alpha=\iota$ then $C_G(\alpha)=\{g:g^{2}\in Z(G)\}$, the elements whose square is central.

**Proof.** For the identity the defect is $g\alpha(g)^{-1}=e$ for every $g$. For the inversion, $\alpha(g)g^{-1}=g^{-1}g^{-1}=g^{-2}$, which is central exactly when $g^{2}$ is central.

**Corollary (two degenerate cases).** On an abelian group the commuting subgroup of the inversion is the whole group; on a group of exponent two the commuting subgroup of every involutive automorphism is the whole group.

**Proof.** On an abelian group every square is central, so the criterion of the proposition holds for every element. On a group of exponent two every element satisfies $g^{2}=e$, hence $g=g^{-1}$, and for an involutive automorphism $\alpha$ one has $\alpha(g)=g^{-1}=g$; the defect $g\alpha(g)^{-1}$ is $e$ for every $g$, so $C_G(\alpha)=G$.

## The Commuting Subgroup and the Semidirect Product

Let $t$ be the element of order two acting on $G$ by $\alpha$ in the semidirect product $G\rtimes\langle t\rangle$ of *Involutive Groups*, §9, so that $tgt^{-1}=\alpha(g)$.

**Proposition (the commutation with $t$).** For $g\in G$ the commutator with $t$ is $[g,t]=g\alpha(g)^{-1}$, and

$$
C_G(\alpha)=\{g\in G : [g,t]\in Z(G)\}.
$$

**Proof.** $[g,t]=gtg^{-1}t^{-1}=g\,\alpha(g)^{-1}\,t t^{-1}=g\alpha(g)^{-1}$, using $t^{-1}=t$ and $tg^{-1}t^{-1}=\alpha(g^{-1})=\alpha(g)^{-1}$. The description of $C_G(\alpha)$ is then the proposition above.

**Proposition (the centraliser of $t$).** In $G\rtimes\langle t\rangle$ the centraliser of $t$ meets $G$ in $G^{\alpha}$: $C_{G\rtimes\langle t\rangle}(t)\cap G=G^{\alpha}$. Hence the elements commuting with $\alpha$ are the elements whose commutator with $t$ is central, and the elements fixed by $\alpha$ are the elements commuting with $t$.

**Proof.** $g t=t g$ is $tgt^{-1}=g$, that is $\alpha(g)=g$; so $C_{G\rtimes\langle t\rangle}(t)\cap G=G^{\alpha}$. The second statement restates the description of $C_G(\alpha)$.

**Corollary (the commuting subgroup as a preimage).** $C_G(\alpha)$ is the largest subgroup $H$ of $G$ containing $Z(G)$ with $[H,t]\subseteq Z(G)$; it is the full preimage under $G\to G/Z(G)$ of the centraliser of the coset $tZ(G)$ in $(G\rtimes\langle t\rangle)/Z(G)$.

**Proof.** The first statement is the definition read through the commutator description and the closure proved in the theorem. The second is the exact sequence, since the image of $G$ in $(G\rtimes\langle t\rangle)/Z(G)$ centralises the coset of $t$ exactly when $[g,t]\in Z(G)$.

## The Name and the Group Algebra

**Remark (why "algebra").** In the group $G$ the object defined here is a subgroup, and the word "algebra" in the title refers to its linearisation. The involutive automorphism $\alpha$ extends linearly to an automorphism of the group algebra $k[G]$, the fixed set $k[G]^{\alpha}=\{a:\alpha(a)=a\}$ is a subalgebra of $k[G]$, and the commuting subgroup is the preimage of the centraliser of $\alpha$ in the inner automorphism group computed in the previous section. The full treatment of $k[G]$, of the fixed subalgebra and of the skew group algebra belongs to *Group Algebras* and to the representation theory of later parts; nothing of it is used here.

**Remark (the term for the working reader).** The name "commuting algebra" is used here with the reading fixed by the scope of the article: the elements of the group commuting with the involutive automorphism in the sense that their inner automorphisms commute with it. A sibling reading of the same name, the fixed subalgebra of the group algebra, is the second object of this section and is cited, not developed.

## Summary

For an involutive automorphism $\alpha$ of $G$ the **commuting set** $C_G(\alpha)=\{g\in G : c_g\alpha=\alpha c_g\}$ consists of the elements whose **conjugate defect** $g\alpha(g)^{-1}$ is central, and it is a subgroup containing $Z(G)$ and the fixed subgroup $G^{\alpha}$. On it, $\alpha$ multiplies by the central element $z(g)=\alpha(g)g^{-1}$, the map $z$ is a homomorphism $C_G(\alpha)\to Z(G)$ with kernel $G^{\alpha}$, and

$$
C_G(\alpha)/Z(G)\cong C_{\operatorname{Inn}(G)}(\alpha), \qquad C_G(\alpha)/G^{\alpha}\cong\operatorname{im}z\leq Z(G).
$$

The fixed subgroup is contained and the containment is strict in general, the dihedral group $D_4$ with the conjugation by a reflection giving $G^{\alpha}$ of order four inside $C_G(\alpha)=G$ of order eight. For $\alpha=\mathrm{id}$ the commuting set is all of $G$, and for $\alpha=\iota$ it is the set of elements whose square is central.

In the semidirect product $G\rtimes\langle t\rangle$ with $t$ acting by $\alpha$, the commutator is $[g,t]=g\alpha(g)^{-1}$, so $C_G(\alpha)=\{g:[g,t]\in Z(G)\}$, the centraliser of $t$ meets $G$ in $G^{\alpha}$, and $C_G(\alpha)$ is the full preimage of the centraliser of the coset of $t$ in the quotient by the centre. The name "commuting algebra" refers to the linearisation: $\alpha$ extends to the group algebra $k[G]$, whose fixed subalgebra is cited to *Group Algebras*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $c_g\alpha=\alpha c_g$ | $g$ commutes with the involutive automorphism |
| $C_G(\alpha)$ | commuting subgroup, the commuting algebra of $\alpha$ |
| $g\alpha(g)^{-1}\in Z(G)$ | centrality of the conjugate defect |
| $z(g)=\alpha(g)g^{-1}$ | homomorphism $C_G(\alpha)\to Z(G)$, kernel $G^{\alpha}$ |
| $C_G(\alpha)/Z(G)\cong C_{\operatorname{Inn}(G)}(\alpha)$ | the exact sequence |
| $[g,t]=g\alpha(g)^{-1}$ | commutator in the semidirect product |
| $k[G]^{\alpha}$ | fixed subalgebra of the group algebra, the linearisation |

## Further Reading

- Derek J. S. Robinson, *A Course in the Theory of Groups* (Springer, second edition, 1996), for centralisers, commutators and semidirect products.
- Joseph J. Rotman, *An Introduction to the Theory of Groups* (Springer, fourth edition, 1995), for inner automorphism groups and the calculation of centralisers in the small groups.
- I. Martin Isaacs, *Finite Group Theory* (American Mathematical Society, Graduate Studies in Mathematics 92, 2008), for centralisers of automorphisms and their extensions.
- Donald S. Passman, *The Algebraic Structure of Group Rings* (Wiley, 1977), for the group algebra, its fixed subalgebra under an automorphism and the skew group algebra.
