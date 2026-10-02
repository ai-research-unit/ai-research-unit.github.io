
# __Reflections as Signed Two-Sided Operators on a Group__

## Introduction

A reflection of a group is an operator of the signed two-sided form $x\mapsto a\,\alpha(x)\,a^{-1}$ that is its own inverse: it is an involution of the set $G$ produced by the multiplication, the grade involution and the inverse. This article defines the reflections of a graded group in that way, identifies the elements that carry them, computes their fixed subgroups, and records the cases in which the construction degenerates — the grade involution inner, the group abelian, or the carrying element failing to satisfy the centrality that makes the operator an involution.

The article assumes the elementary theory of groups from *Groups*, the definition of an involutive automorphism, the associated involution $\sigma=\iota\alpha$, the inverted set and the fixed set from *Involutive Groups*, the inner conjugation and its square $c_a^2=c_{a^2}$ from *Inner Conjugation and the Class Operator*, the left and right translations from *Left and Right Multiplication in a Group*, and the signed sandwich, its factorisation and the square of the signed conjugation from *The Signed Sandwich on a Group*. The adjoint of a reflection is *The Signed Adjoint of the Reflection on a Group*. A reflection in the geometric sense — in a hyperplane, preserving a form — belongs to the later categories and requires a form, which this article never uses; a reflection here is only an operator on the underlying set.

## The Signed Conjugation

**Definition.** For $a\in G$ the **signed conjugation** by $a$ is the signed sandwich $\Sigma^{\alpha}_{a,a^{-1}}(x)=a\,\alpha(x)\,a^{-1}$.

**Proposition.** The signed conjugation is the automorphism $c_a\circ\alpha$ of $G$, with inverse $\Sigma^{\alpha}_{a^{-1},a}=\alpha\circ c_{a^{-1}}=c_{\alpha(a^{-1})}\circ\alpha$; its square is the inner conjugation by $a\alpha(a)$,

$$
\bigl(\Sigma^{\alpha}_{a,a^{-1}}\bigr)^2 = c_{a\alpha(a)} ,
$$

and it is an involution of the set $G$ exactly when $a\alpha(a)\in Z(G)$.

**Proof.** $c_a(\alpha(x))=a\alpha(x)a^{-1}$ is the definition, and it is an automorphism as a composite of automorphisms. The square was computed in *The Signed Sandwich on a Group*: the composition law gives $(\Sigma^{\alpha}_{a,a^{-1}})^2=\Sigma_{a\alpha(a),(a\alpha(a))^{-1}}=c_{a\alpha(a)}$. The inner conjugation $c_u$ is the identity exactly when $u$ is central, so the square is the identity exactly when $a\alpha(a)\in Z(G)$.

**Proposition (the fixed subgroup).** The fixed set of the signed conjugation is

$$
\operatorname{Fix}(a) = \{ x\in G : \alpha(x) = a^{-1}xa \} = \{ x\in G : \alpha(x)=c_{a^{-1}}(x) \},
$$

and it is a subgroup of $G$, nonempty because it contains an element $x$ with $\alpha(x)=a^{-1}xa$ exactly when the operator has a fixed point; when it is nonempty it is a coset of the fixed subgroup $G^{\alpha}=\{x:\alpha(x)=x\}$ of the grade involution.

**Proof.** An automorphism has a fixed set that is a subgroup, and $\Sigma^{\alpha}_{a,a^{-1}}$ is an automorphism, so $\operatorname{Fix}(a)$ is a subgroup; explicitly, if $x,y$ are fixed then $\alpha(xy)=\alpha(x)\alpha(y)=a^{-1}xa\cdot a^{-1}ya=a^{-1}xya$ and $\alpha(x^{-1})=(a^{-1}xa)^{-1}=a^{-1}x^{-1}a$, so the set is closed under multiplication and inversion. If $x_0$ is a fixed point and $h\in G^{\alpha}$ then $\alpha(x_0h)=\alpha(x_0)\alpha(h)=a^{-1}x_0a\,h=a^{-1}x_0ha$, so $x_0h$ is fixed; conversely the quotient of two fixed points is fixed by $\alpha$, so lies in $G^{\alpha}$.

When $\alpha=\mathrm{id}$ the fixed subgroup is the centraliser, $\operatorname{Fix}(a)=C_G(a)$; the general fixed subgroup is the set of $x$ on which the two automorphisms $\alpha$ and $c_{a^{-1}}$ agree.

## Reflections

**Definition.** A **reflection** of the graded group $(G,\alpha)$ is a signed conjugation that is an involution of $G$,

$$
\rho_a := \Sigma^{\alpha}_{a,a^{-1}}, \qquad \rho_a^2=\mathrm{id} \iff a\alpha(a)\in Z(G).
$$

**Proposition (the carrying elements).** Two elements $a,a'$ carry the same reflection if and only if $a'=az$ for some $z\in Z(G)$; the reflections are therefore the cosets $aZ(G)$ of those elements for which $a\alpha(a)$ is central, and the reflection attached to $a$ depends only on this coset.

**Proof.** $\rho_a=\rho_{a'}$ if and only if $a\alpha(x)a^{-1}=a'\alpha(x)a'^{-1}$ for every $x$, that is $(a'^{-1}a)\alpha(x)=\alpha(x)(a'^{-1}a)$ for every $x$; since $\alpha$ is surjective this says $a'^{-1}a$ commutes with every element of $G$, so $a'^{-1}a\in Z(G)$.

**Proposition (the elements inverted by the grade involution).** Let $I(\alpha)=\{a\in G : \alpha(a)=a^{-1}\}$ be the inverted set of $\alpha$, equivalently the fixed set $G^{\sigma}$ of the associated involution $\sigma=\iota\alpha$. Then $I(\alpha)$ is a subgroup of $G$, and for every $a\in I(\alpha)$ one has $a\alpha(a)=e$, so the signed conjugation $\rho_a$ is automatically an involution and its square is $\mathrm{id}$.

**Proof.** That $I(\alpha)=G^{\sigma}$ is a subgroup is established in *Involutive Groups*; the identification of the two sets is $\alpha(a)=a^{-1}\iff \iota\alpha(a)=a\iff\sigma(a)=a$. If $a\in I(\alpha)$ then $\alpha(a)=a^{-1}$, so $a\alpha(a)=a a^{-1}=e$ is central and the criterion of the previous section applies.

**Remark (the correspondence).** A reflection is carried by an element $a$, and it is an involution exactly when the element $a\alpha(a)$ acts trivially by conjugation, that is when $a\alpha(a)$ is central. The elements of the subgroup $I(\alpha)$ satisfy this automatically, and they are the elements on which the grade involution agrees with the inversion. In the geometric realisation the signed conjugations by the elements of $I(\alpha)$ are the reflections in the walls perpendicular to those elements; the geometric statement requires a form and belongs to the later categories.

## The Degenerate Cases

The construction degenerates in three ways, and they are distinguished by which of the two families of sandwiches collapses.

**Proposition (inner grade involution).** If $\alpha$ is an inner automorphism, say $\alpha=c_z$, then the signed conjugations are the unsigned ones, $\rho_a=c_a\circ c_z=c_{az}$, and the reflection is not distinguished from an ordinary inner conjugation; every reflection is an inner automorphism, and a reflection is an involution exactly when $(az)^2\in Z(G)$.

**Proof.** That $\alpha$ inner forces $\mathfrak{S}^\alpha=\mathfrak{S}$ is *The Signed Sandwich on a Group*; hence $\rho_a=c_a\circ\alpha=c_a c_z=c_{az}$. An inner conjugation is an involution exactly when the conjugating element squares to a central element.

**Proposition (abelian group).** If $G$ is abelian then every inner conjugation is the identity, so every signed conjugation is the grade involution,

$$
\rho_a = c_a\circ\alpha = \alpha \quad\text{for every } a,
$$

and the reflections of $(G,\alpha)$ are the single operator $\alpha$. In particular, if $\alpha=\mathrm{id}$ as well then the only reflection is the identity.

**Proof.** On an abelian group $c_a=\mathrm{id}$ for every $a$, so $\rho_a=\alpha$; and $\alpha^2=\mathrm{id}$ makes $\alpha$ an involution, consistent with $a\alpha(a)=a^2\in Z(G)=G$. The statement about $\alpha=\mathrm{id}$ follows.

**Proposition (non-central carrying product).** If $a\alpha(a)\notin Z(G)$ then the signed conjugation is not an involution: its square is a nontrivial inner conjugation. The elements with this property are the degenerate carriers, the analogue of the vectors of vanishing square in the geometric case.

**Proof.** The square is $c_{a\alpha(a)}$, which is the identity exactly on the central elements; if $a\alpha(a)$ is not central the square is a non-identity automorphism, so $\rho_a$ has infinite order or order divisible by the order of $c_{a\alpha(a)}$.

The three cases exhaust the ways in which a signed conjugation can fail to be a reflection: the involution may be inner, so that the signed operator carries no information beyond conjugation; the group may be abelian, so that every reflection is the identity; or the carrying element may have a non-central product $a\alpha(a)$, so that the operator is not an involution at all.

## Summary

The **signed conjugation** by $a$ is the automorphism $\rho_a(x)=a\alpha(x)a^{-1}=c_a\alpha$; its square is the inner conjugation by the element $a\alpha(a)$, so it is an **involution of the set $G$** exactly when $a\alpha(a)\in Z(G)$, and a signed conjugation that is an involution is a **reflection** of the graded group. The fixed subgroup of $\rho_a$ is $\operatorname{Fix}(a)=\{x:\alpha(x)=a^{-1}xa\}$, a subgroup that reduces to the centraliser $C_G(a)$ when $\alpha=\mathrm{id}$, and a coset of the fixed subgroup $G^\alpha$ when it is nonempty. Two elements carry the same reflection exactly when they differ by a central element, so the reflections are the cosets $aZ(G)$ of the elements with $a\alpha(a)$ central. The elements of the inverted set $I(\alpha)=G^{\sigma}$ of the grade involution satisfy $\alpha(a)=a^{-1}$, hence $a\alpha(a)=e$, and they carry involutions automatically; they are the group analogue of the vectors that carry the geometric reflections.

The construction degenerates when the grade involution is inner, in which case the reflections are inner automorphisms; when the group is abelian, in which case every reflection is the single grade involution $\alpha$; and when the carrying element has non-central product $a\alpha(a)$, in which case the signed conjugation is not an involution.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho_a=\Sigma^{\alpha}_{a,a^{-1}}$ | the signed conjugation by $a$, $x\mapsto a\alpha(x)a^{-1}$ |
| $\rho_a=c_a\alpha$ | its expression as an automorphism |
| $\rho_a^2=c_{a\alpha(a)}$ | its square, an inner conjugation |
| $a\alpha(a)\in Z(G)$ | the criterion for $\rho_a$ to be a reflection |
| $\operatorname{Fix}(a)=\{x:\alpha(x)=a^{-1}xa\}$ | the fixed subgroup of $\rho_a$ |
| $G^{\alpha}$ | the fixed subgroup of the grade involution |
| $aZ(G)$ | the coset of carrying elements of a reflection |
| $I(\alpha)=G^{\sigma}=\{a:\alpha(a)=a^{-1}\}$ | the inverted set, whose elements carry reflections automatically |
| $\alpha$ inner | degenerate case, reflections reduce to inner conjugations |
| $a\alpha(a)\notin Z(G)$ | degenerate carrier, $\rho_a$ not an involution |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the generation of the orthogonal group by reflections, each carried by a vector and realised by a signed conjugation.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, second edition, 2001), for the reflection as a sandwich operator and its fixed hyperplane.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for involutive automorphisms, inverted elements and fixed subgroups.
- Derek J. S. Robinson, *A Course in the Theory of Groups* (Springer, second edition, 1996), for automorphisms of order two, centralisers and the structure of the automorphism group.
