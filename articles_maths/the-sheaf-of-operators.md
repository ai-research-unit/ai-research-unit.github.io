
# __The Sheaf of Operators__

## Introduction

The sheaf of operators $\mathcal{E}nd(\mathcal{F})=\mathcal{H}om(\mathcal{F},\mathcal{F})$ of a sheaf $\mathcal{F}$ was introduced in *Operators on a Sheaf*, together with the ring $\operatorname{End}(\mathcal{F})=\Gamma(X,\mathcal{E}nd(\mathcal{F}))$ of global operators and the comparison of the stalks of the sheaf with the endomorphism ring of the stalk. This article takes the sheaf of operators itself as the object of study, rather than the ring of its global sections: it develops the sections of $\mathcal{E}nd(\mathcal{F})$ over the open sets, the sheaf of units, which is the automorphism sheaf, and the **local structure** of $\mathcal{E}nd(\mathcal{F})$, that is, its description on a cover by open sets over which $\mathcal{F}$ is trivial and the resulting matrix model. The two articles divide the material cleanly: *Operators on a Sheaf* owns the ring and the stalks, and the present article owns the sections and the local structure.

The local structure is the content of the article. If $\mathcal{F}$ is locally free of finite rank $r$, then over a trivializing open set the operators are the $r\times r$ matrices of local functions, the sheaf of operators is locally the matrix algebra $M_r(\mathcal{O}_X)$, and the automorphism sheaf is locally the general linear group $\mathrm{GL}_r(\mathcal{O}_X)$; the sheaf of operators is therefore a twisted form of a matrix algebra, its centre is the structure sheaf, its two-sided ideals are pulled back from the centre, and it carries a trace and a determinant, the trace being the invariant of an operator that does not depend on the trivialization. If $\mathcal{F}$ is not locally free the local model is the endomorphism ring of the stalk, which need not be a matrix ring, and the support of the operator sheaf is the support of the sheaf.

The article uses the notation of *Operators on a Sheaf* throughout and does not repeat its identifications; the restriction and the extension by zero, which compare the operators on different opens, are *The Restriction and Extension Operators*; the Čech cocycles of a trivializing cover are those of *Čech Cohomology*, and the descent of the local models is *Descent Theory*. Nothing analytic and nothing geometric is used: the local structure is matrix algebra over the structure sheaf, and no form, no norm and no derivative occurs. Throughout, $(X,\mathcal{O}_X)$ is a ringed space, $\mathcal{F}$ is a sheaf of $\mathcal{O}_X$-modules of finite presentation (in particular locally free of finite rank or coherent when so stated), and $\mathcal{E}nd(\mathcal{F})=\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F},\mathcal{F})$.

## The Sections of the Sheaf of Operators

**Proposition (sections and their gluing).** For every open $U\subseteq X$ the sections of the sheaf of operators are the operators on the restriction,

$$
\Gamma(U,\mathcal{E}nd(\mathcal{F}))=\operatorname{End}(\mathcal{F}|_U),
$$

and an operator on $\mathcal{F}$ over $U$ is the same thing as a compatible family of operators over the members of an open cover of $U$: if $U=\bigcup_iU_i$ and $T_i\in\operatorname{End}(\mathcal{F}|_{U_i})$ satisfy $T_i|_{U_i\cap U_j}=T_j|_{U_i\cap U_j}$ for all $i,j$, then there is a unique $T\in\operatorname{End}(\mathcal{F}|_U)$ restricting to $T_i$ on each $U_i$.

*Proof.* The first identity and the gluing are the sheaf property of $\mathcal{E}nd(\mathcal{F})$ established in *Operators on a Sheaf*; they are restated here only to fix the reading of the sections as operators on the restriction.

**Proposition (the bifunctor).** The sheaf hom $\mathcal{H}om(-,-)$ is a bifunctor on sheaves of $\mathcal{O}_X$-modules, contravariant in the first variable and covariant in the second, so that a morphism $\varphi:\mathcal{F}\to\mathcal{G}$ induces $\mathcal{H}om(\varphi,\mathcal{G}):\mathcal{H}om(\mathcal{G},\mathcal{G})\to\mathcal{H}om(\mathcal{F},\mathcal{G})$ and $\mathcal{H}om(\mathcal{F},\varphi):\mathcal{H}om(\mathcal{F},\mathcal{G})\to\mathcal{H}om(\mathcal{F},\mathcal{G})$. For the operator sheaf this gives, for every isomorphism $\varphi:\mathcal{F}\to\mathcal{G}$, an isomorphism of sheaves of rings

$$
\mathcal{E}nd(\varphi):\mathcal{E}nd(\mathcal{F})\longrightarrow\mathcal{E}nd(\mathcal{G}),\qquad T\mapsto\varphi\,T\,\varphi^{-1},
$$

and $\mathcal{E}nd$ is a functor on the groupoid of sheaves and isomorphisms.

*Proof.* The bifunctoriality of $\mathcal{H}om$ is the functoriality of morphism sets, contravariant in the source and covariant in the target, sheafified. For an isomorphism the pair of variances composes to the conjugation displayed, which is a ring isomorphism with the displayed inverse $\mathcal{E}nd(\varphi^{-1})$.

**Remark (the operator sheaf of a subsheaf).** A monomorphism $\mathcal{F}\to\mathcal{G}$ induces a restriction $\mathcal{E}nd(\mathcal{G})\to\mathcal{E}nd(\mathcal{F})$ on the operators that preserve $\mathcal{F}$, but not every operator on $\mathcal{F}$ extends; $\mathcal{E}nd$ is not a functor on all morphisms, and the failure of the extension of operators is the restriction phenomenon of *The Restriction and Extension Operators*.

## The Sheaf of Units and the Automorphisms

**Definition.** The **sheaf of units** of the operator sheaf is the sheaf of groups

$$
\mathcal{G}L(\mathcal{F})=\mathcal{E}nd(\mathcal{F})^{\times},\qquad \Gamma(U,\mathcal{G}L(\mathcal{F}))=\operatorname{Aut}(\mathcal{F}|_U),
$$

the subsheaf of the locally invertible operators; it is also written $\mathcal{A}ut(\mathcal{F})$ and called the **automorphism sheaf**. Its global sections form the group $\operatorname{Aut}(\mathcal{F})=\mathcal{G}L(\mathcal{F})(X)$ of *Operators on a Sheaf*.

**Proposition (units sectionwise).** An operator $T\in\operatorname{End}(\mathcal{F}|_U)$ is a unit of the ring $\operatorname{End}(\mathcal{F}|_U)$ if and only if its germ $T_x$ is a unit of $\operatorname{End}(\mathcal{F}_x)$ for every $x\in U$; the property of being invertible is local, and $\mathcal{G}L(\mathcal{F})$ is a subsheaf of $\mathcal{E}nd(\mathcal{F})$.

*Proof.* If $T$ has a two-sided inverse $S$ on $U$ then the germs invert one another, so the condition is necessary. Conversely if every germ is invertible then the germs of the inverse operator are defined locally and agree on overlaps, so they glue to an inverse of $T$ over $U$ by the sheaf property of $\mathcal{E}nd(\mathcal{F})$. The gluing of the inverses uses the uniqueness of an inverse in a ring.

**Proposition (the matrices of automorphisms).** If $\mathcal{F}$ is locally free of finite rank $r$, then on a trivializing open set $U$ there is an isomorphism $\mathcal{G}L(\mathcal{F})|_U\cong\mathrm{GL}_r(\mathcal{O}_X)|_U$, the sheaf of $r\times r$ matrices with invertible determinant, and $\mathcal{G}L(\mathcal{F})$ is a twisted form of the general linear group, with twisting cocycle the Čech 1-cocycle of the trivialization in $\mathrm{GL}_r(\mathcal{O}_X)$.

*Proof.* Choose a trivialization $\mathcal{F}|_U\cong\mathcal{O}_U^r$; conjugation by it identifies the operators on $\mathcal{F}|_U$ with the matrices, by the bifunctoriality above, and the units with the invertible matrices. On the overlaps two trivializations differ by an element of $\mathrm{GL}_r(\mathcal{O}_{U\cap V})$, giving the transition cocycle; the cocycle condition on the triple overlaps is the associativity of the transition isomorphisms, and it is the Čech cocycle of *Čech Cohomology*.

**Remark (the classification by the cocycle).** Two trivializations of a locally free $\mathcal{F}$ over a cover give two matrix descriptions of the same operator; the two cocycles differ by a coboundary, and conversely two cocycles differing by a coboundary define isomorphic sheaves, by gluing the local free sheaves along the coboundary. This is the descent of the local models in the sense of *Descent Theory*, and the Čech computation belongs to *Čech Cohomology*.

## The Local Structure of the Operator Sheaf

**Theorem (the local matrix model).** Let $\mathcal{F}$ be locally free of finite rank $r$ on the ringed space $(X,\mathcal{O}_X)$. Then $\mathcal{E}nd(\mathcal{F})$ is a sheaf of $\mathcal{O}_X$-algebras satisfying:

1. $\mathcal{E}nd(\mathcal{F})$ is locally free of finite rank $r^2$ over $\mathcal{O}_X$, and on a trivializing open set $U$ for $\mathcal{F}$ there is an isomorphism of sheaves of $\mathcal{O}_U$-algebras $\mathcal{E}nd(\mathcal{F})|_U\cong M_r(\mathcal{O}_U)$;
2. $\mathcal{E}nd(\mathcal{F})\cong\mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{F}^{\vee}$, and taking global sections on an open $U$ gives $\operatorname{End}(\mathcal{F}|_U)\cong(\mathcal{F}\otimes\mathcal{F}^{\vee})(U)$;
3. the centre of $\mathcal{E}nd(\mathcal{F})$ is $\mathcal{O}_X$, and the scalar morphism $\mathcal{O}_X\to\mathcal{E}nd(\mathcal{F})$ is an isomorphism onto the centre.

*Proof.* (1) On a trivialization $\mathcal{F}|_U\cong\mathcal{O}_U^r$ the conjugation isomorphism of the previous section identifies the operator sheaf with $\mathcal{H}om(\mathcal{O}_U^r,\mathcal{O}_U^r)=M_r(\mathcal{O}_U)$, which is free of rank $r^2$. (2) The identification $\mathcal{H}om(\mathcal{F},\mathcal{G})\cong\mathcal{F}^{\vee}\otimes_{\mathcal{O}_X}\mathcal{G}$ for locally free $\mathcal{F}$ of finite rank is the standard adjunction of tensor and hom; with $\mathcal{G}=\mathcal{F}$ it gives $\mathcal{E}nd(\mathcal{F})\cong\mathcal{F}^{\vee}\otimes\mathcal{F}$, and the symmetry of the tensor product for the order of the factors is immaterial. (3) On a trivialization the centre of $M_r(\mathcal{O}_U)$ is the scalar matrices for $r\geq1$; the local identifications glue, giving $Z(\mathcal{E}nd(\mathcal{F}))=\mathcal{O}_X$, and the scalar morphism is a sectionwise isomorphism onto it.

**Proposition (the two-sided ideals).** If $\mathcal{F}$ is locally free of finite rank $r\geq1$, every two-sided ideal of $\mathcal{E}nd(\mathcal{F})$ is of the form $\mathcal{J}\cdot\mathcal{E}nd(\mathcal{F})$ for a unique ideal $\mathcal{J}$ of $\mathcal{O}_X$; equivalently, the two-sided ideals of the operator sheaf are the ideals pulled back from its centre.

*Proof.* On a trivializing open set the two-sided ideals of $M_r(\mathcal{O}_U)$ are the ideals $\mathcal{J}\,M_r(\mathcal{O}_U)$ with $\mathcal{J}$ an ideal of $\mathcal{O}_U$, by the standard description of the ideals of a full matrix ring; the local ideals and the local generators glue because the trivializations on overlaps conjugate the matrix algebras and preserve the two-sided ideals, and the ideal $\mathcal{J}$ is the pullback of the ideal to the centre.

**Proposition (the trace).** Let $\mathcal{F}$ be locally free of finite rank $r$. There is a morphism of sheaves $\operatorname{tr}:\mathcal{E}nd(\mathcal{F})\to\mathcal{O}_X$, the **trace**, characterised on a trivialization by the matrix trace; it is $\mathcal{O}_X$-linear, satisfies $\operatorname{tr}(TS)=\operatorname{tr}(ST)$ and $\operatorname{tr}(\mathrm{id})=r$, and an operator is **traceless** when $\operatorname{tr}T=0$. If $r$ is invertible in $\mathcal{O}_X(X)$ the **reduced trace** $\frac1r\operatorname{tr}$ is defined and $\operatorname{tr}(T)=0$ is equivalent to the tracelessness of $T-\frac1r\operatorname{tr}(T)\,\mathrm{id}$.

*Proof.* On a trivialization the matrix trace is invariant under conjugation, $\operatorname{tr}(PTP^{-1})=\operatorname{tr}(T)$, so the local traces agree on overlaps and glue; the identities are those of the matrix trace, and the last statement is the elementary computation with the reduced trace.

**Proposition (the determinant).** For a locally free $\mathcal{F}$ of rank $r$ the determinant of a local operator is well defined on the units,

$$
\det:\mathcal{G}L(\mathcal{F})\longrightarrow\mathcal{O}_X^{\times},
$$

and it is a morphism of sheaves of groups; it does not extend to a morphism $\mathcal{E}nd(\mathcal{F})\to\mathcal{O}_X$ in general, since the determinant of a non-invertible matrix need not be invertible and there is no sheaf map to $\mathcal{O}_X$ that is natural in the trivialization.

*Proof.* On a trivialization the determinant of an invertible matrix is invariant under conjugation and multiplicative; the local determinants glue along the transition cocycle because $\det(PAP^{-1})=\det(A)$, and the multiplicativity is that of the determinant of matrices.

**Remark (the Azumaya structure).** For $\mathcal{F}$ locally free of finite rank $r\geq1$, the operator sheaf $\mathcal{E}nd(\mathcal{F})$ is a sheaf of $\mathcal{O}_X$-algebras locally isomorphic to $M_r(\mathcal{O}_X)$, locally free of rank $r^2$, with centre $\mathcal{O}_X$; when $X$ is a scheme these are exactly the conditions for $\mathcal{E}nd(\mathcal{F})$ to be an **Azumaya algebra**, the twisted forms of the matrix algebra classified by the Čech cohomology of the automorphism sheaf, as described in *Sheaves in Algebraic Geometry*. The classification and the associated Brauer-type invariants belong to that article and are cited, not repeated.

## The General Case

**Proposition (finite presentation).** If $\mathcal{F}$ is coherent then $\mathcal{E}nd(\mathcal{F})$ is coherent and its stalk at $x$ is the endomorphism ring $\operatorname{End}_{\mathcal{O}_{X,x}}(\mathcal{F}_x)$ of the stalk, a finitely generated $\mathcal{O}_{X,x}$-module; the comparison map of *Operators on a Sheaf* is an isomorphism in this case.

*Proof.* The stalk statement is the comparison theorem of *Operators on a Sheaf* with the finite-presentation hypothesis; the coherence of $\mathcal{E}nd(\mathcal{F})$ follows from the local presentation of $\mathcal{F}$ and the coherence of $\mathcal{O}_X$, since $\mathcal{E}nd$ is locally a cokernel of a map of finitely generated free sheaves.

**Proposition (the support).** The support of the operator sheaf is the support of the sheaf,

$$
\operatorname{Supp}(\mathcal{E}nd(\mathcal{F}))=\operatorname{Supp}(\mathcal{F}),
$$

and over an open set where $\mathcal{F}$ vanishes the operator sheaf vanishes; over a point $x$ where the stalk $\mathcal{F}_x$ is a free module of rank $r$ over the local ring, the operator sheaf is locally free of rank $r^2$ near $x$.

*Proof.* If $\mathcal{F}$ vanishes on an open set then so does $\mathcal{E}nd(\mathcal{F})$, since the only operator on the zero sheaf is zero; conversely a nonzero operator has a nonzero value on some section, hence a nonzero germ at some point of the support. The local-freeness statement is the matrix model at $x$.

**Example (a torsion sheaf).** Let $\mathcal{F}$ be a sheaf supported at a closed subset, for instance the skyscraper $i_*A$ of *Operators on a Sheaf*; then $\mathcal{E}nd(\mathcal{F})=i_*\operatorname{End}(A)$ is supported at the same closed set, and its stalks are matrix rings only at the points where the stalk of $\mathcal{F}$ is free of finite positive rank over the local ring. The example shows that the local matrix model is a statement about the points where $\mathcal{F}$ has constant finite rank, and fails where it does not.

**Example (a non-free stalk).** Let $X$ be a space with structure sheaf a ring of functions and let $\mathcal{F}$ be the ideal sheaf of a point in a ringed space of dimension at least one, so that the stalk of $\mathcal{F}$ at the point is the maximal ideal of the local ring, which is not free as a module over itself. Then $\mathcal{E}nd(\mathcal{F})_x=\operatorname{End}(\mathfrak{m}_x)$, which is not a matrix ring over the local ring; the operator sheaf is still coherent, but its local structure is that of the endomorphism ring of a non-free module.

## Worked Cases

### The Free Sheaf of Rank $r$

For $\mathcal{F}=\mathcal{O}_X^r$ the operator sheaf is $\mathcal{E}nd(\mathcal{O}_X^r)=M_r(\mathcal{O}_X)$, the free sheaf of $r\times r$ matrices over the structure sheaf; the automorphism sheaf is $\mathrm{GL}_r(\mathcal{O}_X)$, the trace is the matrix trace and the determinant is the matrix determinant. This is the untwisted local model of every locally free sheaf of rank $r$.

### The Invertible Sheaf

For a locally free $\mathcal{F}$ of rank one the operator sheaf is $\mathcal{E}nd(\mathcal{F})\cong\mathcal{O}_X$, by the tensor formula and $\mathcal{F}\otimes\mathcal{F}^{\vee}\cong\mathcal{O}_X$, and the automorphism sheaf is $\mathcal{O}_X^{\times}$. All operators commute, the trace is the identity, and the local structure is the simplest possible: the operators on a line are the functions.

### The Locally Free Sheaf of Rank Two

For a locally free $\mathcal{F}$ of rank two the operator sheaf is locally free of rank four and locally $M_2(\mathcal{O}_X)$; on a trivializing cover an operator is a two-by-two matrix of local functions, its trace is a function and its determinant is defined on the units. The sheaf $\mathcal{E}nd(\mathcal{F})$ is an Azumaya algebra of degree two when $X$ is a scheme, and over the complex numbers the reduction modulo the trace gives the traceless part, a locally free sheaf of rank three; the traceless operators are the local structure of the Lie algebra $\mathfrak{sl}_2$ attached to the rank-two bundle.

## Summary

The sections of the operator sheaf over an open set are the operators on the restriction, and they glue on covers; the sheaf hom is a bifunctor, so the operator sheaf is a functor on isomorphisms by conjugation. The units of the operator sheaf form the automorphism sheaf, whose sections are the invertible operators on the restriction; invertibility is a local condition, and for a locally free sheaf the automorphism sheaf is a twisted form of the general linear group, with the twisting given by the Čech cocycle of a trivializing cover.

For a locally free sheaf of finite rank $r$ the local structure is the matrix algebra: the operator sheaf is locally free of rank $r^2$, locally isomorphic to $M_r(\mathcal{O}_X)$, isomorphic to $\mathcal{F}\otimes\mathcal{F}^{\vee}$, with centre $\mathcal{O}_X$ and with two-sided ideals pulled back from the centre. It carries a trace, invariant under conjugation and giving a morphism to the structure sheaf, and a determinant on its units; over a scheme it is an Azumaya algebra. Off the locally free locus the local model is the endomorphism ring of the stalk, coherent when the sheaf is, with support the support of the sheaf; the matrix model holds exactly where the stalk is free of constant finite rank.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Gamma(U,\mathcal{E}nd(\mathcal{F}))=\operatorname{End}(\mathcal{F}\rvert_U)$ | sections of the operator sheaf are the operators on the restriction |
| $\mathcal{H}om(-,-)$ | bifunctor, contravariant in the source and covariant in the target |
| $\mathcal{E}nd(\varphi)(T)=\varphi T\varphi^{-1}$ | functoriality on isomorphisms by conjugation |
| $\mathcal{G}L(\mathcal{F})=\mathcal{E}nd(\mathcal{F})^{\times}$ | sheaf of units, the automorphism sheaf $\mathcal{A}ut(\mathcal{F})$ |
| $\mathrm{GL}_r(\mathcal{O}_X)$ | local model of the automorphism sheaf for a rank-$r$ locally free sheaf |
| $M_r(\mathcal{O}_X)$ | local model of the operator sheaf; locally free of rank $r^2$ |
| $\mathcal{E}nd(\mathcal{F})\cong\mathcal{F}\otimes\mathcal{F}^{\vee}$ | operator sheaf of a locally free sheaf |
| $Z(\mathcal{E}nd(\mathcal{F}))=\mathcal{O}_X$ | centre; the two-sided ideals are pulled back from it |
| $\operatorname{tr}:\mathcal{E}nd(\mathcal{F})\to\mathcal{O}_X$ | trace; $\operatorname{tr}(TS)=\operatorname{tr}(ST)$, $\operatorname{tr}(\mathrm{id})=r$ |
| $\det:\mathcal{G}L(\mathcal{F})\to\mathcal{O}_X^{\times}$ | determinant of an automorphism |
| $\operatorname{Supp}(\mathcal{E}nd(\mathcal{F}))=\operatorname{Supp}(\mathcal{F})$ | support of the operator sheaf |
| Azumaya algebra | sheaf of algebras locally $M_r(\mathcal{O}_X)$ with centre $\mathcal{O}_X$ |

## Further Reading

- Robin Hartshorne, *Algebraic Geometry* (Springer, 1977), for the sheaf $\mathcal{E}nd$ of a locally free sheaf, its trace and the identification with $\mathcal{F}\otimes\mathcal{F}^{\vee}$.
- Alexander Grothendieck and Jean Dieudonné, *Éléments de géométrie algébrique I* (Publications Mathématiques de l'IHÉS 4, 1960), for the sheaves of algebras, their local structure and the ideals of a matrix algebra over a sheaf of rings.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991), for Azumaya algebras, their trace and their classification by Čech cocycles.
- Glen E. Bredon, *Sheaf Theory* (Springer, second edition, 1997), for the sheaf hom, its sections and the support of a sheaf of algebras.
- Saunders Mac Lane and Ieke Moerdijk, *Sheaves in Geometry and Logic* (Springer, 1992), for the internal hom and the group of units of a sheaf of rings.
- Gunter Tamme, *Introduction to Étale Cohomology* (Springer, 1994), for the descent of the matrix model and the Azumaya algebras over a scheme.
