
# __The Graded Adjoint Action on a Module over a Topological Group__

## Introduction

The graded module of the category carries a grading, a form and an action, and the adjoint of the action is a second action: the group acts on the endomorphisms of the module by conjugation, on the dual module by the contragredient, and on the forms by transport. What makes the construction graded is that the grading involution is part of the data, and the adjoint action turns its compatibility with the action into a compatibility with the grade involution; the sign rule then attaches a parity to every operator and a sign to every transpose, exactly as the graded action of *The Graded Action on a Module over a Topological Group* attaches a sign to every product.

The article assumes the graded module, the grading involution, the sign rule and the compatibility $\varepsilon g\varepsilon = \alpha(g)$ from *The Graded Action on a Module over a Topological Group*; the continuous involution, the associated involutive automorphism and the fixed subgroup from *Involutive Topological Groups*; and the continuity of a group action on a discrete set and the openness of stabilisers from *Topological Groups*. The topological module in the sense of a topological vector space is *Topology on Linear Spaces*, later in this part, and the adjoint of a convolution operator is Part III; neither is used.

Throughout, $G$ is a topological group, $\sigma$ is a continuous involution, $\alpha = \sigma\iota$ is the associated continuous involutive automorphism, $M = M_{\bar0}\oplus M_{\bar1}$ is a graded $k$-module over $(G,\alpha)$ with grading involution $\varepsilon$, the action is written $\pi(g)$, and the module is finite-dimensional over $k$ so that adjoints exist; the graded module and the grading involution are those of *The Graded Action on a Module over a Topological Group*.

## Graded Forms and Transposes

**Definition.** A **graded form** on $M$ is a bilinear form $B$ with $B(\varepsilon v,\varepsilon w) = B(v,w)$, equivalently $B(M_i,M_j) = 0$ for $i\neq j$, an **even** or **grading-preserving** form; it is **odd** when $B(M_i,M_i) = 0$ and $B$ pairs $M_{\bar0}$ with $M_{\bar1}$, equivalently $B(\varepsilon v,\varepsilon w) = -B(v,w)$. A graded form is **nondegenerate** when its radical vanishes.

**Proposition (the grading involution and the transpose).** Let $B$ be a nondegenerate graded form and let $T^\#$ be the transpose of an operator $T$ on $M$, defined by $B(Tv,w) = B(v,T^\#w)$. Then the grading involution is self-adjoint for an even form and anti-self-adjoint for an odd form,

$$
\varepsilon^\# = \varepsilon \ \text{(} B \text{ even)}, \qquad \varepsilon^\# = -\varepsilon \ \text{(} B \text{ odd)} ,
$$

and for a homogeneous operator $T$ of parity $|T|$ the transpose has the same parity, $\varepsilon T^\#\varepsilon = (-1)^{|T|}T^\#$.

**Proof.** For homogeneous $v,w$, $B(\varepsilon v,w) = (-1)^{|v|}B(v,w)$ and $B(v,\varepsilon w) = (-1)^{|w|}B(v,w)$. If $B$ is even then $B(v,w)$ vanishes unless $|v| = |w|$, so the two expressions are equal and $\varepsilon^\# = \varepsilon$; if $B$ is odd then $B(v,w)$ vanishes unless $|v|\neq|w|$, so the two expressions differ by a sign and $\varepsilon^\# = -\varepsilon$. For the parity of the transpose, $B(\varepsilon Tv,w) = (-1)^{|v|+|T|}B(Tv,w) = (-1)^{|T|}B(v,T^\#w)$ and also $B(\varepsilon Tv,w) = B(Tv,\varepsilon^\#w) = \pm B(Tv,\varepsilon w) = \pm B(v,T^\#\varepsilon w)$, which gives the displayed relation.

**Corollary (the sign rule for the transpose).** For a homogeneous operator $T$ and a homogeneous form, the transpose is characterised by the graded symmetry

$$
B(Tv,w) = (-1)^{|T|\,q}\,B(v,T^\#w)
$$

with $q = 0$ for an even form and $q = 1$ for an odd form; the sign is the product of the parity of the operator and the parity of the form.

**Proof.** The case $q = 0$ is the definition. For $q = 1$ the identity follows from the anti-self-adjointness of $\varepsilon$ by the computation above, and the general homogeneous case follows by linearity.

## The Adjoint Action on the Endomorphisms

**Definition.** The **adjoint action** of $G$ on the module $\operatorname{End}_k(M)$ is

$$
g\cdot T = \pi(g)\,T\,\pi(g)^{-1} .
$$

**Theorem (it is an action preserving the parity).** The adjoint action is a group action on $\operatorname{End}_k(M)$, it preserves the $\mathbb{Z}/2$-grading of the endomorphism module, and the grading involution conjugates the action of $g$ to the action of $\alpha(g)$:

$$
\varepsilon\,(g\cdot T)\,\varepsilon = \alpha(g)\cdot(\varepsilon\,T\,\varepsilon) , \qquad\text{equivalently}\qquad \varepsilon\,(g\cdot T)\,\varepsilon = (\alpha(g))\cdot T^{\varepsilon} ,
$$

where $T^\varepsilon = \varepsilon T\varepsilon$ is the $\varepsilon$-conjugate of $T$.

**Proof.** $g\cdot(h\cdot T) = \pi(g)\pi(h)T\pi(h)^{-1}\pi(g)^{-1} = \pi(gh)T\pi(gh)^{-1} = (gh)\cdot T$, and $e\cdot T = T$, so it is an action. If $\pi(g)$ has parity $p$ in the sense that $\pi(g)M_j\subseteq M_{j+p}$, then $g\cdot T$ carries $M_j$ to $M_{j+p}\to M_{j+p+|T|}\to M_{j+|T|}$, so its parity is $|T|$; hence the action preserves the grading. For the conjugation identity, the compatibility $\varepsilon\pi(g)\varepsilon = \pi(\alpha(g))$ from the graded action gives $\varepsilon\pi(g)T\pi(g)^{-1}\varepsilon = \pi(\alpha(g))(\varepsilon T\varepsilon)\pi(\alpha(g))^{-1}$, which is the displayed statement.

**Corollary (the sign rule of the adjoint action).** For a homogeneous element $g$ of the group algebra and a homogeneous operator $T$,

$$
\varepsilon\,(g\cdot T)\,\varepsilon = \alpha(g)\cdot T^{\varepsilon} , \qquad \varepsilon\,(T^{\varepsilon})\,\varepsilon = T ,
$$

so the grading involution intertwines the adjoint action of $g$ with the adjoint action of the grade involution of $g$, and the parity of the operator is unchanged; the sign of the adjoint action is entirely carried by the grade involution.

**Proof.** The first identity is the theorem, and the second is $\varepsilon^2 = \mathrm{id}$.

## Compatibility with the Form

**Theorem (unitary actions transpose to inverse actions).** Suppose the action is unitary for the graded form, $\pi(g)^\# = \pi(g)^{-1}$ for every $g$. Then the adjoint action commutes with the transpose,

$$
(g\cdot T)^\# = g\cdot T^\# ,
$$

and the adjoint action preserves the submodule of self-adjoint operators and the submodule of skew-adjoint operators. The parity of the form enters only in the sign rule for the transpose of a homogeneous operator recorded above, $B(Tv,w) = (-1)^{|T|q}B(v,T^\#w)$, and not in the commutation of the transpose with the adjoint action.

**Proof.** $(g\cdot T)^\# = (\pi(g)T\pi(g)^{-1})^\# = \pi(g)^{-\#}T^\#\pi(g)^\#$; unitarity gives $\pi(g)^{-\#} = \pi(g)$ and $\pi(g)^\# = \pi(g)^{-1}$, whence the identity. The parity statement follows because the transpose preserves the parity and the adjoint action preserves it too, and the sign rule is the graded symmetry proved in the section on graded forms.

**Corollary (the invariant forms).** The adjoint action restricts to the space of $G$-invariant forms: a form $B$ is invariant exactly when $B(g\cdot T\,v,w) = B(v,g\cdot T\,w)$ for every operator $T$, equivalently when the action is unitary for $B$; the invariant graded forms of even type are the fixed points of the adjoint action on the space of even forms, and those of odd type the fixed points on the space of odd forms.

**Proof.** $B$ is invariant under the action of $g$ when $B(\pi(g)v,\pi(g)w) = B(v,w)$ for all $v,w$, which is unitarity; the equivalence with the condition on all $T$ is the uniqueness of the transpose under a nondegenerate form. The fixed-point description is the definition of the adjoint action on the space of forms.

## The Adjoint Action on the Dual Module

**Definition.** The **coadjoint action** of $G$ on the dual module $M^*$ is

$$
(g\cdot\xi)(m) = \xi\bigl(\pi(g)^{-1}m\bigr) ,
$$

the contragredient of the action on $M$; the dual module is graded by $(M^*)_i = (M_i)^*$.

**Theorem.** The coadjoint action is a group action, it is compatible with the grading, $(g\cdot\xi)(M_j)\subseteq$ the component paired with $M_j$, and the grading involution acts on the dual by its transpose, which is itself for an even form and its negative for an odd form. The sign rule relating the pairing to the action is

$$
\langle g\cdot\xi,\,m\rangle = \bigl\langle \xi,\,\pi(g)^{-1}m\bigr\rangle , \qquad
\varepsilon(g\cdot\xi) = (-1)^{q}\,\bigl(\alpha(g)\cdot(\varepsilon\xi)\bigr) ,
$$

with $q$ the parity of the form.

**Proof.** The action property is the contragredience, $\langle g\cdot(h\cdot\xi),m\rangle = \langle\xi,\pi(h)^{-1}\pi(g)^{-1}m\rangle = \langle(gh)\cdot\xi,m\rangle$. The grading statement is that the dual pairing respects the parity, so $(g\cdot\xi)$ evaluated on $M_j$ pairs with $M_j$; the transposition of the grading involution is computed from $\varepsilon^\# = \pm\varepsilon$. The sign rule is the conjugation identity transported to the dual by the transpose.

## Continuity

**Theorem (continuity of the adjoint action).** Let $M$ carry the discrete topology and let the adjoint action on $\operatorname{End}_k(M)$ carry the discrete topology. Then the adjoint action is continuous if and only if every stabiliser

$$
G_T = \{g\in G : \pi(g)T\pi(g)^{-1} = T\}, \qquad T\in\operatorname{End}_k(M),
$$

is open in $G$; when the action of $G$ on $M$ has open stabilisers, the adjoint action has open stabilisers and is continuous. The grading involution and the transpose are continuous maps of the discrete endomorphism module.

**Proof.** A map into a discrete space is continuous exactly when it is locally constant; the orbit map $g\mapsto g\cdot T$ is locally constant exactly when $G_T$ is open. If the stabiliser $G_m$ of each $m\in M$ is open then $G_T$ contains the intersection of finitely many $G_m$ for $m$ running over a basis, an open subgroup, so $G_T$ is open. On a discrete module every map is continuous.

**Corollary (the topological form of the sign rule).** For a continuous action the identities $\varepsilon(g\cdot T)\varepsilon = \alpha(g)\cdot T^\varepsilon$ and $(g\cdot T)^\# = g\cdot T^\#$ hold at every point, and the coadjoint action is continuous whenever the action on $M$ is; the transpose and the grading involution are homeomorphisms of the discrete endomorphism module.

**Proof.** The identities are the algebraic ones, already proved pointwise; continuity of the coadjoint action and of the transposition follows from the discrete topology.

## Summary

A graded module over $(G,\alpha)$ with a nondegenerate graded form has a transpose for every operator, the grading involution being self-adjoint for an even form and anti-self-adjoint for an odd form, and the transpose of a homogeneous operator obeys the sign rule $B(Tv,w) = (-1)^{|T|q}B(v,T^\#w)$ with $q$ the parity of the form. The adjoint action $g\cdot T = \pi(g)T\pi(g)^{-1}$ is a group action on the endomorphism module that preserves the parity and is conjugated by the grading involution into the adjoint action of the grade involution, $\varepsilon(g\cdot T)\varepsilon = \alpha(g)\cdot T^\varepsilon$, which is the topological form of the sign rule: the parity is carried by the grade involution and not by the operator. When the action is unitary the adjoint action commutes with the transpose and preserves the self-adjoint and the skew-adjoint operators, and the invariant forms are exactly the fixed points of the induced action on the space of forms; for an odd form the transpose carries the sign of the parity. On the dual module the coadjoint action is the contragredient, compatible with the grading, and the sign rule pairs the action of the group with the inverse action on the dual. With the discrete topology, continuity of the adjoint action is equivalent to the openness of the stabilisers, and the grading involution and the transpose are homeomorphisms; the topological module in the sense of a topological vector space is *Topology on Linear Spaces* and is not used.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M = M_{\bar0}\oplus M_{\bar1}$, $\varepsilon$ | the graded module and its grading involution |
| $\pi(g)$ | the action of $g$ on $M$ |
| $B$, $q$ | a graded form and its parity, $q = 0$ even, $q = 1$ odd |
| $T^\#$ | the transpose, $B(Tv,w) = B(v,T^\#w)$ |
| $\varepsilon^\# = \varepsilon$ or $-\varepsilon$ | $\varepsilon$ self-adjoint for even $B$, anti-self-adjoint for odd $B$ |
| $B(Tv,w) = (-1)^{\lvert T\rvert q}B(v,T^\#w)$ | the sign rule for the transpose |
| $g\cdot T = \pi(g)T\pi(g)^{-1}$ | the adjoint action on the endomorphisms |
| $\varepsilon(g\cdot T)\varepsilon = \alpha(g)\cdot T^\varepsilon$ | the sign rule of the adjoint action |
| $(g\cdot T)^\# = g\cdot T^\#$ | the unitary case, transpose and adjoint action commute |
| $(g\cdot\xi)(m) = \xi(\pi(g)^{-1}m)$ | the coadjoint action on the dual module |
| $G_T$ | the stabiliser of $T$; the action is continuous iff every $G_T$ is open |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for graded modules, forms of even and odd type, and their adjoints.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for graded algebras and modules, bilinear forms and transposes.
- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Wiley, 1962), for the contragredient representation and the adjoint action on endomorphisms.
- Lev S. Pontryagin, *Topological Groups* (Gordon and Breach, second edition, 1966), for the continuity of a group action and the openness of the stabilisers.
- Alexander Arhangel'skii and Mikhail Tkachenko, *Topological Groups and Related Structures* (Atlantis Press, 2008), for group actions on discrete sets and the associated quotient and orbit structures.
