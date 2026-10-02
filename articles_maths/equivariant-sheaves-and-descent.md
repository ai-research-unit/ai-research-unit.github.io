
# __Equivariant Sheaves and Descent__

## Introduction

A group $G$ acting on a space $X$ acts also on the sheaves on $X$: a sheaf that is stable under the action, up to coherent isomorphisms, is an **equivariant sheaf**, and the descent problem is to reconstruct it from the quotient $X/G$. An **equivariant sheaf**, or $G$-sheaf, is a sheaf $\mathcal{F}$ on $X$ together with a family of isomorphisms $\varphi_g:g_*\mathcal{F}\to\mathcal{F}$ indexed by the elements of $G$, compatible with the composition in $G$: the isomorphisms are the **descent data** of the action, and the cocycle they satisfy is the associative law of $G$. The category of equivariant sheaves sits over the quotient by the pullback $q^*$ along the quotient map $q:X\to X/G$, and the descent theorem states when the pullback is an equivalence: for a free and properly discontinuous action, every equivariant sheaf descends to a sheaf on the quotient, and the descent is effective.

This article fixes the notion of an equivariant sheaf, the category $\mathrm{Sh}_G(X)$ of equivariant sheaves and their morphisms, the **fixed sheaf** of invariants of an equivariant sheaf, and the descent theorem for a free properly discontinuous action. It is the first article of the involutive layer of the category: the two-element group case is the involution on a space, developed in *Sheaves with a Real Structure* and in *The Involution on the Structure Sheaf*; the field-theoretic Galois case is *Galois Descent for Sheaves*; and the derived category of equivariant sheaves is *Equivariant Derived Categories*. The category of sheaves and its exactness are *Presheaves and Sheaves*; the Čech cohomology and the descent in the categorical sense are *Čech Cohomology* and *Descent Theory*, and the group actions on a space, the quotient and the covering space action are *Transformation Groups* and *The Fundamental Group and Covering Spaces*.

The article uses no analysis and no geometry: the quotient is taken in the sense of the orbit space of a group action, no form and no norm occurs, and the descent is the topological descent of sheaves along a covering. Throughout, $G$ is a group acting on the space $X$ on the left by homeomorphisms, $g:X\to X$ is the homeomorphism given by an element $g$, $q:X\to X/G$ is the quotient map, $\mathcal{F}$ is a sheaf of abelian groups or of $\mathcal{O}_X$-modules on $X$, and $\mathcal{F}^G$ denotes the sheaf of invariant sections. When the descent theorem is used, the action is assumed free and properly discontinuous: every point has a neighbourhood $W$ with the translates $gW$, $g\in G$, pairwise disjoint, so that $q$ is a covering map with deck group $G$.

## Group Actions on a Space

**Definition.** A **$G$-space** is a space $X$ with an action of $G$ by homeomorphisms; the **orbit space** $X/G$ is the set of orbits $Gx=\{gx:g\in G\}$ with the quotient topology, and the **quotient map** $q:X\to X/G$, $q(x)=Gx$, is continuous. The action is **free** if $gx=x$ implies $g=e$, and **properly discontinuous** if every point has a neighbourhood $W$ whose translates $gW$ are pairwise disjoint; a free properly discontinuous action makes $q$ a covering map with group of deck transformations $G$.

**Proposition.** A free properly discontinuous action of $G$ on a locally connected space $X$ has quotient $X/G$ whose points correspond to the orbits, and the quotient map is open; every point of $X/G$ has an evenly covered neighbourhood $V$ with $q^{-1}(V)=\bigsqcup_{g\in G}gW$ for a sheet $W$ over $V$.

*Proof.* The quotient map of a group action is open because the saturation of an open set is open; the evenly covered neighbourhood is the image $V=q(W)$ of a neighbourhood $W$ with pairwise disjoint translates, and the preimage is the disjoint union of the translates by the definition of the quotient.

**Example (the antipodal action).** The group $G=\mathbb{Z}/2$ acts on the sphere $S^n$ by the antipodal map $x\mapsto-x$; the action is free and properly discontinuous and the quotient is the real projective space $\mathbb{RP}^n$. The quotient map is the double cover $S^n\to\mathbb{RP}^n$ of *The Fundamental Group and Covering Spaces*.

**Example (the translation action).** The group $G=\mathbb{Z}$ acts on the real line by $n\cdot x=x+n$; the action is free and properly discontinuous and the quotient is the circle $S^1$; a sheaf on the circle pulls back to a $\mathbb{Z}$-equivariant sheaf on the line, and the equivariant structure is the monodromy of the pulled-back sheaf.

## Equivariant Sheaves

**Definition.** A **$G$-equivariant sheaf**, or $G$-sheaf, on a $G$-space $X$ is a sheaf $\mathcal{F}$ on $X$ together with, for every $g\in G$, an isomorphism

$$
\varphi_g:g_*\mathcal{F}\longrightarrow\mathcal{F},
$$

subject to the **cocycle condition** $\varphi_{gh}=\varphi_g\circ g_*(\varphi_h)$ and the unit condition $\varphi_e=\mathrm{id}_{\mathcal{F}}$. A **morphism** of $G$-sheaves is a morphism of sheaves $\psi:\mathcal{F}\to\mathcal{G}$ with $\varphi^{\mathcal{G}}_g\circ g_*(\psi)=\psi\circ\varphi^{\mathcal{F}}_g$ for every $g$; the $G$-sheaves and their morphisms form the category $\mathrm{Sh}_G(X)$.

**Remark (the cocycle is the associative law).** The condition $\varphi_{gh}=\varphi_g\circ g_*(\varphi_h)$ is the associativity of the action: the two ways of comparing $\mathcal{F}$ with $(gh)_*\mathcal{F}=g_*h_*\mathcal{F}$ agree. It is exactly the descent cocycle of *Descent Theory* for the covering $X\to X/G$, read with the group of the covering in place of the covering family.

**Proposition (the abelian structure).** The category $\mathrm{Sh}_G(X)$ is abelian; kernels, cokernels and images are computed on the underlying sheaves, with the induced equivariant structures, and the forgetful functor to $\mathrm{Sh}(X)$ is exact and faithful. When $G$ is discrete the category $\mathrm{Sh}_G(X)$ is a Grothendieck category, a category of sheaves on the action groupoid $X/\!/G$, and it has enough injectives.

*Proof.* A kernel of a morphism of $G$-sheaves is the kernel of the underlying morphism, and it inherits the equivariant structure because the $\varphi_g$ commute with the morphism; the same for cokernels; the forgetful functor preserves them by construction. For discrete $G$ the action groupoid $X/\!/G$ has object space $X$ and morphism space $G\times X$, and its category of sheaves is $\mathrm{Sh}_G(X)$; the general theory of *Sheaves on Sites* and *Descent Theory* applies.

**Definition.** The **constant $G$-sheaf** attached to a $G$-module $A$ is the constant sheaf $\underline{A}$ with the equivariant structure induced by the action of $G$ on $A$: $\varphi_g$ is the identity when $A$ has the trivial action, giving the trivial $G$-sheaf. A $G$-sheaf with the structure sheaf $\mathcal{O}_X$ as coefficients is a **$G$-equivariant $\mathcal{O}_X$-module** if the isomorphisms are $\mathcal{O}_X$-linear, and the category of these is written $\mathrm{Sh}_G(X,\mathcal{O}_X)$.

**Example (the pullback of a sheaf on the quotient).** For a sheaf $\mathcal{G}$ on $X/G$ the pullback $q^{-1}\mathcal{G}$ on $X$ carries a canonical $G$-equivariant structure: since $q\circ g=q$ for every $g$, the two pullbacks $g^*(q^{-1}\mathcal{G})$ and $q^{-1}\mathcal{G}$ are canonically isomorphic, and the isomorphisms are the $\varphi_g$. The assignment $\mathcal{G}\mapsto q^{-1}\mathcal{G}$ is a functor $q^*:\mathrm{Sh}(X/G)\to\mathrm{Sh}_G(X)$, the **pullback along the quotient**.

## The Fixed Sheaf and the Invariants

**Definition (invariants of a $G$-module).** For a $G$-module $M$ the **invariants** are $M^{G}=\{\,m\in M: gm=m\ \text{for every}\ g\in G\,\}$; they are the equalizer of the identity and the composite of the action, $M\rightrightarrows\prod_{g\in G}M$, so the functor $(-)^{G}$ on $G$-modules is left exact.

**Definition (the fixed sheaf).** Let $\mathcal{F}$ be a $G$-sheaf on $X$. For an open $V\subseteq X/G$ the preimage $q^{-1}V$ is a $G$-invariant open set, and the equivariant structure makes $\mathcal{F}(q^{-1}V)$ a $G$-module; define

$$
\mathcal{F}^{G}(V)=\mathcal{F}\bigl(q^{-1}V\bigr)^{G}.
$$

This is a sheaf on the quotient $X/G$, the **fixed sheaf** of $\mathcal{F}$, also written $q_*^{G}\mathcal{F}$ and called the **descent** of $\mathcal{F}$; the assignment $\mathcal{F}\mapsto\mathcal{F}^{G}$ is a functor $\mathrm{Sh}_G(X)\to\mathrm{Sh}(X/G)$. For a $G$-invariant open $U\subseteq X$ the same formula with $U$ in place of $q^{-1}V$ gives the invariants of the $G$-module $\mathcal{F}(U)$, which is the local description of the fixed sheaf.

**Proposition (the fixed sheaf is a sheaf, and left exact).** The presheaf $V\mapsto\mathcal{F}(q^{-1}V)^{G}$ on $X/G$ is a sheaf, and the functor $(-)^{G}$ is left exact.

*Proof.* Let $V=\bigcup_iV_i$ be a cover and let $s_i\in\mathcal{F}(q^{-1}V_i)^{G}$ be a matching family. The preimages $q^{-1}V_i$ cover $q^{-1}V$, and the $s_i$ are matching sections of $\mathcal{F}$; they glue to a section $s$ of $\mathcal{F}(q^{-1}V)$, which is invariant because each of its restrictions $s_i$ is invariant and the action is compatible with restriction, and which is unique because $\mathcal{F}$ is a sheaf. Left exactness is the left exactness of the invariants of a $G$-module, which is a limit.

**Proposition (adjunction).** The pullback along the quotient and the invariants are an adjoint pair, $q^*\dashv q_*^{G}$: for $\mathcal{G}$ on $X/G$ and $\mathcal{F}$ a $G$-sheaf on $X$,

$$
\operatorname{Hom}_{\mathrm{Sh}_G(X)}\bigl(q^*\mathcal{G},\mathcal{F}\bigr)\cong\operatorname{Hom}_{\mathrm{Sh}(X/G)}\bigl(\mathcal{G},q_*^{G}\mathcal{F}\bigr).
$$

*Proof.* A morphism $q^{-1}\mathcal{G}\to\mathcal{F}$ of sheaves on $X$ is $G$-equivariant exactly when its adjunct $\mathcal{G}\to q_*\mathcal{F}$ lands in the invariant sections, since the pullback $q^{-1}\mathcal{G}$ has the equivariant structure forced by the identities $q\circ g=q$; this is the adjunction $q^{-1}\dashv q_*$ of *Presheaves and Sheaves* restricted to the invariant part.

## The Descent Theorem

**Theorem (descent for a covering action).** Let $G$ act freely and properly discontinuously on $X$, so that $q:X\to X/G$ is a covering. Then the pullback $q^*:\mathrm{Sh}(X/G)\to\mathrm{Sh}_G(X)$ is an equivalence of categories, with quasi-inverse the invariants $q_*^{G}$; equivalently, every $G$-sheaf on $X$ descends to a sheaf on the quotient, the descent is effective, and

$$
\mathrm{Sh}(X/G)\simeq\mathrm{Sh}_G(X).
$$

*Proof.* The unit $\mathcal{G}\to q_*^{G}(q^*\mathcal{G})$ and the counit $q^*(q_*^{G}\mathcal{F})\to\mathcal{F}$ are the natural maps of the adjunction; both are isomorphisms, and it suffices to check the counit over an evenly covered neighbourhood. Let $V$ be evenly covered with $q^{-1}(V)=\bigsqcup_{g}gW$ a disjoint union of sheets. A section of $q^*(q_*^{G}\mathcal{F})$ over $q^{-1}(V)$ is a family of sections $s_g\in\mathcal{F}(gW)$ that is invariant under the action, and the action permutes the sheets; a $G$-invariant family is determined by its component $s_e\in\mathcal{F}(W)$, because $s_g=\varphi_g(s_e)$ on $gW$. The counit sends such a family to its component on $W$, and is therefore an isomorphism onto $\mathcal{F}(W)$ after restriction; the two functors are inverse. The unit is the same computation read on the quotient.

**Corollary (descent data are equivariant structures).** The descent data of *Descent Theory* for the covering $X\to X/G$ are exactly the equivariant structures of the present article: an object of the descent category is a family of sections over the sheets with compatible isomorphisms over the intersections, and these are the $\varphi_g$ and their cocycle.

*Proof.* On an evenly covered neighbourhood the sheets are the translates $gW$ and the double intersections are $gW\cap hW'$, which are empty unless $W=W'$ up to translation; the descent isomorphisms are therefore the $\varphi_g$, and the cocycle condition on the triple intersections is the associativity $\varphi_{gh}=\varphi_g g_*(\varphi_h)$.

**Remark (the descent fails for a non-free action).** If the action is not free the quotient map is not a covering, the counit of the adjunction is not an isomorphism over the points with a nontrivial stabiliser, and the equivariant sheaves are strictly more than the sheaves on the orbit space: the correct quotient is the stack quotient $[X/G]$, whose sheaves are the equivariant sheaves by definition. The orbit space retains only the sheaves with a trivial stabiliser action, and the distinction is the reason the descent theorem needs freeness and proper discontinuity.

## Cohomological Form

**Proposition (the descent isomorphism in cohomology).** Under the descent equivalence, the cohomology of a sheaf on the quotient is the cohomology of the invariant sections of its pullback,

$$
H^i(X/G,\mathcal{G})\cong H^i\bigl(X/G,q_*^{G}q^*\mathcal{G}\bigr)\cong H^i\bigl(X,(q^{-1}\mathcal{G})^{G}\bigr),
$$

and the pullback $q^*$ is exact and induces isomorphisms on the stalks at the points of a sheet.

*Proof.* The equivalence of categories carries injective resolutions to injective resolutions and the global sections over the quotient to the invariant sections; the identification is the isomorphism of the two derived functors under the equivalence, and the exactness of $q^{-1}$ is that of *Presheaves and Sheaves*.

**Proposition (obstructions for a general descent).** For a covering $X\to X/G$ with group $G$ and a $G$-sheaf $\mathcal{F}$, the twisted forms of $\mathcal{F}$ — the $G$-sheaves locally isomorphic to $\mathcal{F}$ on the quotient — are classified by the first cohomology $H^1(G,\mathcal{A}ut(\mathcal{F}))$ of the group with coefficients in the automorphism sheaf of $\mathcal{F}^G$ when the action is free; the computation is the Čech computation of *Čech Cohomology* for the covering, and the group cohomology is that of *Group Cohomology*.

*Proof.* A twisted form is described on the sheets of the covering by a cocycle with values in the automorphisms of $\mathcal{F}$ and by the cocycle condition of the equivariant structure, which is the group cocycle condition; two descriptions give the same form exactly when the cocycles differ by a coboundary. The identification of the cocycle classes with $H^1(G,\mathcal{A}ut(\mathcal{F}))$ is the standard computation of the Čech cohomology of a covering by a group action.

## Worked Cases

### The Antipodal Action and the Projective Space

For $G=\mathbb{Z}/2$ acting on $S^n$ by the antipodal map, the descent theorem gives $\mathrm{Sh}(\mathbb{RP}^n)\simeq\mathrm{Sh}_{\mathbb{Z}/2}(S^n)$: a sheaf on the projective space is the same thing as an antipodally equivariant sheaf on the sphere. The constant sheaf on $\mathbb{RP}^n$ pulls back to the constant sheaf on $S^n$ with the trivial equivariant structure; a local system of rank one on $\mathbb{RP}^n$ pulls back to a local system on $S^n$ with monodromy $\pm1$ on the antipodal loop, and the two local systems correspond to the two actions of $\mathbb{Z}/2$ on the fibre.

### The Translation Action and the Circle

For $G=\mathbb{Z}$ acting on $\mathbb{R}$ by translation, the descent gives $\mathrm{Sh}(S^1)\simeq\mathrm{Sh}_{\mathbb{Z}}(\mathbb{R})$; a sheaf on the circle is a translation-equivariant sheaf on the line, and the equivariant structure is the monodromy of the sheaf around the circle. The invariants of a $\mathbb{Z}$-equivariant sheaf on $\mathbb{R}$ are the sections fixed by the translation, which are the sections of the descended sheaf on the circle, and the cohomology $H^1(S^1,\mathcal{G})$ is computed by the invariant part of the cohomology of the pullback.

### The Trivial Group

For $G=\{e\}$ the action is trivial, the quotient is $X$, and the descent theorem reduces to the identity $\mathrm{Sh}(X)\simeq\mathrm{Sh}_{\{e\}}(X)$: the equivariant structure is the identity and the fixed sheaf is the sheaf itself. The case is the degenerate end of the theory and the check that the definitions have been made with the correct signs and directions.

## Summary

A group $G$ acting on a space $X$ acts on the sheaves on $X$ through equivariant structures: a $G$-sheaf is a sheaf $\mathcal{F}$ with isomorphisms $\varphi_g:g_*\mathcal{F}\to\mathcal{F}$ satisfying the cocycle $\varphi_{gh}=\varphi_g\circ g_*(\varphi_h)$, which is the descent datum of the covering $X\to X/G$ and the associative law of the action. The $G$-sheaves form an abelian category $\mathrm{Sh}_G(X)$, with exact forgetful functor to $\mathrm{Sh}(X)$; the fixed sheaf $\mathcal{F}^G$ is the sheaf of invariant sections, a left exact functor, and the invariants on the quotient $q_*^{G}\mathcal{F}=(q_*\mathcal{F})^{G}$ form its descent, right adjoint to the pullback $q^*$ along the quotient map.

For a free and properly discontinuous action the quotient map is a covering, and the descent theorem states that the pullback and the invariants are inverse equivalences, $\mathrm{Sh}(X/G)\simeq\mathrm{Sh}_G(X)$: every $G$-sheaf descends to the quotient and the descent is effective. The proof compares the two functors over an evenly covered neighbourhood, where the sheets are the translates of a sheet and an invariant family of sections is determined by one component; the descent data are the equivariant structures. For a non-free action the quotient is the stack quotient, not the orbit space, and the descent fails at the points with a nontrivial stabiliser; the classification of the twisted forms is by the group cohomology $H^1(G,\mathcal{A}ut(\mathcal{F}))$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$ acting on $X$; $g:X\to X$ | a group of homeomorphisms of the space |
| $X/G$, $q:X\to X/G$ | orbit space and quotient map; a covering for a free properly discontinuous action |
| $g_*\mathcal{F}$ | direct image of a sheaf along the homeomorphism $g$ |
| $\varphi_g:g_*\mathcal{F}\to\mathcal{F}$ | equivariant structure; $\varphi_{gh}=\varphi_g\circ g_*(\varphi_h)$ |
| $\mathrm{Sh}_G(X)$ | abelian category of $G$-equivariant sheaves |
| $\mathcal{F}^G$ | fixed sheaf of invariant sections; a left exact functor |
| $q_*^{G}\mathcal{F}=(q_*\mathcal{F})^{G}$ | invariants on the quotient; the descent functor |
| $q^*:\mathrm{Sh}(X/G)\to\mathrm{Sh}_G(X)$ | pullback along the quotient; the canonical equivariant structure |
| $q^*\dashv q_*^{G}$ | adjunction of pullback and invariants |
| $\mathrm{Sh}(X/G)\simeq\mathrm{Sh}_G(X)$ | descent equivalence for a free properly discontinuous action |
| $H^1(G,\mathcal{A}ut(\mathcal{F}))$ | obstruction classes for the twisted forms |

## Further Reading

- Glen E. Bredon, *Sheaf Theory* (Springer, second edition, 1997), for equivariant sheaves, the fixed sheaf and the descent along a group action.
- Alexander Grothendieck, *Théorie des topos et cohomologie étale des schémas (SGA 4)* (Springer Lecture Notes in Mathematics 269, 270, 305, 1972–1973), for the equivariant sheaves as sheaves on the action groupoid and the descent theory.
- Michael Artin, Alexander Grothendieck and Jean-Louis Verdier, *Théorie des topos et cohomologie étale des schémas*, op. cit., for the stack quotient of a non-free action.
- Peter T. Johnstone, *Sketches of an Elephant: A Topos Theory Compendium* (Oxford University Press, 2002), for the descent of sheaves along a covering and the internal invariants.
- Joseph Bernstein and Valery Lunts, *Equivariant Sheaves and Functors* (Springer Lecture Notes in Mathematics 1578, 1994), for the derived category of equivariant sheaves and the functors between the equivariant and the ordinary categories.
- Saunders Mac Lane and Ieke Moerdijk, *Sheaves in Geometry and Logic* (Springer, 1992), for the equivariant sheaves as sheaves on the action groupoid.
