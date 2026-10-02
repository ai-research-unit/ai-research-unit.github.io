
# __Operators on a Sheaf__

## Introduction

An **operator on a sheaf** is an endomorphism of that sheaf: a morphism $\mathcal{F}\to\mathcal{F}$ in the category of sheaves on a topological space $X$. The operators on $\mathcal{F}$ are therefore the elements of the hom-set $\operatorname{End}(\mathcal{F})=\operatorname{Hom}(\mathcal{F},\mathcal{F})$, and composition of morphisms makes this set a unital associative ring, commutative only in the degenerate cases; its group of units is the group $\operatorname{Aut}(\mathcal{F})$ of automorphisms of the sheaf. The operators on a sheaf are the sheaf-theoretic instance of the endomorphisms of an object of a category, and this article develops the three things the operator layer of the category is built on: the ring $\operatorname{End}(\mathcal{F})$ of global operators, the action of that ring on the sections of $\mathcal{F}$, and the **sheaf of operators** $\mathcal{E}nd(\mathcal{F})$, whose sections over an open set $U$ are the operators on the restriction $\mathcal{F}|_U$.

The article fixes the notation of the operator layer and proves the elementary structure: the ring and its opposite, the left and the right multiplications and the sandwich, the sheaf of operators and the comparison of its stalks with the endomorphism rings of the stalks, and the central role of the scalars of a structure sheaf. Its companion *The Sheaf of Operators*, below this article, develops the sheaf $\mathcal{E}nd(\mathcal{F})$ as a sheaf of rings in its own right, with its sections, its sheaf of units and its local structure; *The Restriction and Extension Operators*, below this article, treats the functors by which the operators on different opens are compared.

The assumptions are those of *Presheaves and Sheaves*, which fixes the category of sheaves, the stalks, the sheafification and the sheaf $\mathcal{H}om_{\mathcal{O}_X}$, and of *Sheaf Cohomology*, which fixes the notation $H^i(X,\mathcal{F})$. Nothing analytic and nothing geometric is used. In particular the operators carry no form here: the adjoint of an operator, which a pairing alone makes meaningful, is the subject of *Hermitian Pairings of Sheaves* and of the involution articles of the present category, below this article. Throughout, $\mathcal{F}$ is a sheaf of abelian groups on $X$, or a sheaf of $\mathcal{O}_X$-modules for a structure sheaf $\mathcal{O}_X$, and the two cases are named whenever they differ.

## The Ring of Operators

**Definition.** An **operator on $\mathcal{F}$** is a morphism $T:\mathcal{F}\to\mathcal{F}$. The operators form the set $\operatorname{End}(\mathcal{F})=\operatorname{Hom}(\mathcal{F},\mathcal{F})$, with the **product** $ST=S\circ T$ and the addition inherited from the abelian-group structure on the hom-sets; the identity operator is $\mathrm{id}_{\mathcal{F}}$.

**Proposition (the endomorphism ring).** $\operatorname{End}(\mathcal{F})$ is a unital associative ring, the **endomorphism ring** of $\mathcal{F}$, and its group of units is $\operatorname{Aut}(\mathcal{F})$; when $\mathcal{F}$ is a sheaf of $\mathcal{O}_X$-modules, $\operatorname{End}(\mathcal{F})$ is an $\mathcal{O}_X(X)$-algebra, the addition and the product being $\mathcal{O}_X(X)$-bilinear.

*Proof.* Composition is associative at the level of morphisms, and it distributes over the addition of morphisms because both operations are computed sectionwise; the identity satisfies $\mathrm{id}\,T=T\,\mathrm{id}=T$. A morphism of sheaves is invertible exactly when it is an isomorphism, since an inverse morphism is a two-sided inverse, so the units are the automorphisms. For $\mathcal{O}_X$-modules, a scalar $a\in\mathcal{O}_X(X)$ acts by $T\mapsto m_a\circ T$, and $S\circ m_a = m_a\circ S$ for $\mathcal{O}_X$-linear $S$, giving the bilinearity.

**Notation.** The product is written by juxtaposition, $ST=S\circ T$, so that $S$ acts after $T$ and the order of the factors is read from right to left. The opposite convention $S\cdot T = T\circ S$ is not used.

**Proposition (the opposite ring and the bimodule).** The **opposite ring** $\operatorname{End}(\mathcal{F})^{\mathrm{op}}$ has the same underlying abelian group and the product $S\cdot_{\mathrm{op}}T=TS$. The identity map on the underlying sets is an anti-isomorphism $\operatorname{End}(\mathcal{F})\to\operatorname{End}(\mathcal{F})^{\mathrm{op}}$. The group $\Gamma(X,\mathcal{F})$ of global sections is a left $\operatorname{End}(\mathcal{F})$-module by $T\cdot s=T(s)$ and a right $\operatorname{End}(\mathcal{F})^{\mathrm{op}}$-module by $s\cdot T=T(s)$.

*Proof.* Reversing the order of the factors in the ring axioms gives the opposite ring, and the identity map reverses products by construction. The module axioms are the associativity of composition applied to sections, $S\cdot(T\cdot s)=(ST)(s)$, and the linearity of a morphism of sheaves.

**Definition.** For $a\in\operatorname{End}(\mathcal{F})$ the **left multiplication** and the **right multiplication** by $a$ are the endomorphisms of the abelian group $\operatorname{End}(\mathcal{F})$

$$
L_a(T)=aT,\qquad R_a(T)=Ta .
$$

**Proposition (commutation and the sandwich).** $L_aR_b=R_bL_a$ for all $a,b\in\operatorname{End}(\mathcal{F})$, so $L$ and $R$ are commuting representations of $\operatorname{End}(\mathcal{F})$ and of $\operatorname{End}(\mathcal{F})^{\mathrm{op}}$ on $\operatorname{End}(\mathcal{F})$. If $u\in\operatorname{Aut}(\mathcal{F})$ then the **sandwich**

$$
\Sigma_u(T)=uTu^{-1}
$$

is a ring automorphism of $\operatorname{End}(\mathcal{F})$, and $u\mapsto\Sigma_u$ is a homomorphism $\operatorname{Aut}(\mathcal{F})\to\operatorname{Aut}(\operatorname{End}(\mathcal{F}))$ whose kernel is the intersection of the centre $Z(\operatorname{End}(\mathcal{F}))$ with $\operatorname{Aut}(\mathcal{F})$.

*Proof.* $L_aR_b(T)=aTb=R_bL_a(T)$. For the sandwich, $\Sigma_u(ST)=uSTu^{-1}=(uSu^{-1})(uTu^{-1})=\Sigma_u(S)\Sigma_u(T)$, and $\Sigma_u$ is bijective with inverse $\Sigma_{u^{-1}}$; the kernel consists of the $u$ with $uTu^{-1}=T$ for all $T$, that is $u\in Z(\operatorname{End}(\mathcal{F}))$.

**Proposition (the scalars and the centre).** Let $\mathcal{F}$ be a sheaf of $\mathcal{O}_X$-modules. The assignment $a\mapsto m_a$ sending a global function $a\in\mathcal{O}_X(X)$ to the multiplication $m_a(s)=as$ is a ring homomorphism $\mathcal{O}_X(X)\to\operatorname{End}(\mathcal{F})$ whose image lies in the centre. If $\mathcal{F}$ is locally free of rank $r\geq 1$, the scalars exhaust the centre,

$$
Z(\operatorname{End}(\mathcal{F}))\cong\mathcal{O}_X(X).
$$

*Proof.* The map is a homomorphism because $\mathcal{O}_X$ is commutative: $m_{ab}=m_a\circ m_b$. For centrality, $m_aT=Tm_a$ holds for $\mathcal{O}_X$-linear $T$ by the definition of linearity. For local freeness, the centre of a matrix ring $M_r(R)$ over a commutative ring $R$ is the scalar matrices, $Z(M_r(R))\cong R$ for $r\geq 1$; the local identifications $Z(\mathcal{E}nd(\mathcal{F})|_{U_i})\cong\mathcal{O}_X(U_i)$ glue to $Z(\mathcal{E}nd(\mathcal{F}))\cong\mathcal{O}_X$, and taking global sections gives the statement.

## The Sheaf of Operators

**Definition.** The **presheaf of operators** of $\mathcal{F}$ assigns to an open $U\subseteq X$ the ring $\operatorname{End}(\mathcal{F}|_U)$ and to an inclusion $V\subseteq U$ the restriction $T\mapsto T|_V$. It is a sheaf of rings, the **sheaf of operators** of $\mathcal{F}$,

$$
\mathcal{E}nd(\mathcal{F})=\mathcal{H}om(\mathcal{F},\mathcal{F}),
$$

with $\mathcal{H}om$ the sheaf hom of *Presheaves and Sheaves*; for sheaves of $\mathcal{O}_X$-modules it is the sheaf of $\mathcal{O}_X$-algebras $\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F},\mathcal{F})$.

**Proposition (the sheaf axiom for operators).** The presheaf of operators is a sheaf: for every open $U$, every open cover $U=\bigcup_{i\in I}U_i$ and every family $T_i\in\operatorname{End}(\mathcal{F}|_{U_i})$ with $T_i|_{U_i\cap U_j}=T_j|_{U_i\cap U_j}$ for all $i,j$, there is a unique $T\in\operatorname{End}(\mathcal{F}|_U)$ with $T|_{U_i}=T_i$.

*Proof.* Uniqueness: two morphisms agreeing on every member of a cover agree on their union, since a morphism of sheaves is determined by its values on any cover. Existence: for a section $s\in\mathcal{F}(W)$ with $W\subseteq U$, the sections $T_i(s|_{W\cap U_i})$ are defined on $W\cap U_i$ and agree on the double overlaps, by the compatibility and the functoriality of $T_i$; they glue to a section $T(s)\in\mathcal{F}(W)$ by the sheaf condition of $\mathcal{F}$. The assignment $s\mapsto T(s)$ is a morphism, because each $T_i$ is, and it restricts to $T_i$.

**Proposition (sections and restrictions).** For every open $U\subseteq X$,

$$
\Gamma(U,\mathcal{E}nd(\mathcal{F}))=\operatorname{End}(\mathcal{F}|_U),\qquad \operatorname{End}(\mathcal{F})=\Gamma(X,\mathcal{E}nd(\mathcal{F})),
$$

and the restriction map $\mathcal{E}nd(\mathcal{F})(U)\to\mathcal{E}nd(\mathcal{F})(V)$ for $V\subseteq U$ is $T\mapsto T|_V$. For $\mathcal{F}$ a sheaf of $\mathcal{O}_X$-modules, these are isomorphisms of $\mathcal{O}_X(U)$-algebras and of $\mathcal{O}_X(X)$-algebras respectively.

*Proof.* The first identity is the definition of the presheaf; the sheaf property makes it the sheaf. The algebra structure is inherited sectionwise from $\mathcal{O}_X(U)$.

**Proposition (action on the sheaf).** $\mathcal{E}nd(\mathcal{F})$ acts on $\mathcal{F}$: for $U$ open, $T\in\mathcal{E}nd(\mathcal{F})(U)$ and $s\in\mathcal{F}(U)$, the evaluation $T(s)$ is a section of $\mathcal{F}(U)$, and the action is compatible with restrictions. Consequently $\mathcal{F}$ is a sheaf of left $\mathcal{E}nd(\mathcal{F})$-modules, and $\Gamma(U,\mathcal{F})$ is a left $\Gamma(U,\mathcal{E}nd(\mathcal{F}))$-module for every $U$.

*Proof.* The evaluation is the morphism $\mathcal{E}nd(\mathcal{F})(U)\to\operatorname{End}(\mathcal{F}|_U)$ followed by the application of an operator to a section; compatibility with restrictions is the defining property of the restriction of a morphism.

## The Stalks of the Sheaf of Operators

**Theorem (the comparison map).** Let $\mathcal{F}$ and $\mathcal{G}$ be sheaves of $\mathcal{O}_X$-modules on a ringed space, and let $x\in X$. There is a natural homomorphism

$$
(\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F},\mathcal{G}))_x\longrightarrow\operatorname{Hom}_{\mathcal{O}_{X,x}}(\mathcal{F}_x,\mathcal{G}_x)
$$

sending the germ of a local morphism to its stalk map. It is injective; it is an isomorphism when $\mathcal{F}$ is of finite presentation over $\mathcal{O}_X$, in particular when $\mathcal{F}$ is locally free of finite rank or coherent. For such $\mathcal{F}$,

$$
\mathcal{E}nd(\mathcal{F})_x\cong\operatorname{End}_{\mathcal{O}_{X,x}}(\mathcal{F}_x).
$$

*Proof.* The stalk of the hom sheaf is the filtered colimit $\varinjlim_{x\in U}\operatorname{Hom}(\mathcal{F}|_U,\mathcal{G}|_U)$, and passing to the colimit of the stalk maps is the comparison map, since a morphism sends germs to germs. If the stalk map of a local morphism vanishes, the morphism is zero on a neighbourhood of $x$, so the germ is zero: the map is injective. For finite presentation, the restriction and the colimit are inverse: an element of $\operatorname{Hom}(\mathcal{F}_x,\mathcal{G}_x)$ is represented on a small open $U$ by a morphism $\mathcal{F}|_U\to\mathcal{G}|_U$ because $\mathcal{F}$ admits a local presentation by finitely many generators and relations, and two representatives agree on a smaller open set. When $\mathcal{G}=\mathcal{F}$ the source is $\mathcal{E}nd(\mathcal{F})_x$ and the target is $\operatorname{End}_{\mathcal{O}_{X,x}}(\mathcal{F}_x)$.

**Corollary (locally free sheaves).** If $\mathcal{F}$ is locally free of rank $r$ over $\mathcal{O}_X$, then

$$
\mathcal{E}nd(\mathcal{F})_x\cong M_r(\mathcal{O}_{X,x}),\qquad \mathcal{E}nd(\mathcal{F})\cong\mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{F}^{\vee},
$$

with $\mathcal{F}^{\vee}=\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F},\mathcal{O}_X)$ the dual sheaf; $\mathcal{E}nd(\mathcal{F})$ is locally free of rank $r^2$.

*Proof.* For a free module of finite rank over a ring, $\operatorname{End}(A^r)\cong M_r(A)$ and $A^r\otimes_A(A^r)^{\vee}\cong M_r(A)$; the statements are these identifications on stalks, read as sheaves through the comparison map.

**Remark (the hypothesis is needed).** For a sheaf that is not of finite presentation the comparison map need not be surjective. On a space whose structure sheaf is a ring of functions and with $\mathcal{F}=\bigoplus_{n\geq 0}\mathcal{O}_X$ of infinite countable rank, an endomorphism of the stalk $\mathcal{F}_x$ is an infinite matrix over the local ring $\mathcal{O}_{X,x}$, and such a matrix need not come from a morphism defined on a neighbourhood of $x$; the colimit sees only the matrices that are locally defined. Finite generation is the condition that the local definition is automatic, and it is exactly what the theorem uses.

**Example (the comparison on a locally free sheaf of rank one).** If $\mathcal{F}$ is locally free of rank one then $\mathcal{E}nd(\mathcal{F})\cong\mathcal{O}_X$ and $\mathcal{E}nd(\mathcal{F})_x\cong\mathcal{O}_{X,x}$, in agreement with the corollary; the operators on an invertible sheaf are the multiplications by the local functions.

**Example (the constant sheaf).** Let $A$ be an abelian group and $\mathcal{F}=\underline{A}$ the constant sheaf on a connected space $X$; then $\mathcal{E}nd(\mathcal{F})\cong\underline{\operatorname{End}(A)}$ and $\operatorname{End}(\mathcal{F})\cong\operatorname{End}(A)$, since a morphism of constant sheaves is the same thing on each connected component and there is one component. On a space with $\pi_0(X)$ the set of connected components, $\operatorname{End}(\underline{A})\cong\operatorname{End}(A)^{\pi_0(X)}$.

**Example (the skyscraper sheaf).** Let $i:\{x\}\hookrightarrow X$ and let $\mathcal{F}=i_*A$ be the skyscraper sheaf at $x$ with value the abelian group $A$; then $\mathcal{E}nd(\mathcal{F})=i_*\operatorname{End}(A)$ and $\operatorname{End}(\mathcal{F})\cong\operatorname{End}(A)$, with stalk $\operatorname{End}(A)$ at $x$ and zero elsewhere. The example shows that the operator sheaf of a sheaf concentrated at a point is concentrated there, and that its stalk is computed directly from the value.

## The Structure Sheaf

**Proposition (operators on the structure sheaf).** For a ringed space $(X,\mathcal{O}_X)$,

$$
\mathcal{E}nd_{\mathcal{O}_X}(\mathcal{O}_X)\cong\mathcal{O}_X,\qquad \operatorname{End}_{\mathcal{O}_X}(\mathcal{O}_X)\cong\mathcal{O}_X(X),
$$

as sheaves of rings and as rings. The inverse map is evaluation at the unit section: the operator $T$ is sent to $T(1)$.

*Proof.* An $\mathcal{O}_X$-linear endomorphism $T$ of $\mathcal{O}_X$ is determined by $T(1)$ because $T(a)=T(a\cdot 1)=a\,T(1)$ for a local function $a$; conversely a local function $b$ defines the operator $a\mapsto ab$, which is $\mathcal{O}_X$-linear. The two assignments are inverse, and they are compatible with restrictions.

**Corollary (the units).** $\operatorname{Aut}_{\mathcal{O}_X}(\mathcal{O}_X)\cong\mathcal{O}_X(X)^{\times}$, the group of invertible global functions, and the sheaf of operators of $\mathcal{O}_X$ has sheaf of units $\mathcal{O}_X^{\times}$, the sheaf of invertible functions whose Čech classes are the Picard group of *Čech Cohomology*.

*Proof.* The units of $\mathcal{O}_X(X)$ are the invertible functions, and they correspond to the invertible operators by the proposition; the identification of the invertible functions with the units of the structure sheaf is the definition of $\mathcal{O}_X^{\times}$.

**Proposition (the centre in the module case).** Let $\mathcal{F}$ be a sheaf of $\mathcal{O}_X$-modules and let $m:\mathcal{O}_X(X)\to\operatorname{End}(\mathcal{F})$ be the scalar homomorphism. Its kernel is the annihilator of $\mathcal{F}$ in $\mathcal{O}_X(X)$. If $\mathcal{F}$ is locally free of rank $r\geq 1$ then $m$ is injective and its image is the centre.

*Proof.* $m_a=0$ means $as=0$ for every local section $s$, which is the definition of the annihilator; for locally free of positive rank the annihilator is zero because the stalk $\mathcal{F}_x$ is a free $\mathcal{O}_{X,x}$-module of positive rank. The centrality is the previous proposition, and the exhaustion of the centre is the same proposition.

## Summary

An operator on a sheaf $\mathcal{F}$ is an endomorphism of $\mathcal{F}$; the operators form the endomorphism ring $\operatorname{End}(\mathcal{F})$, a unital associative ring whose units are the automorphisms of $\mathcal{F}$, an $\mathcal{O}_X(X)$-algebra when $\mathcal{F}$ is a sheaf of modules, and the global sections of the sheaf of operators $\mathcal{E}nd(\mathcal{F})=\mathcal{H}om(\mathcal{F},\mathcal{F})$. The opposite ring reverses the order of composition, the left and right multiplications commute and give the sandwich $T\mapsto uTu^{-1}$ by a unit, and the scalar multiplications of a structure sheaf always lie in the centre, which they exhaust for a locally free sheaf of positive rank.

The sheaf of operators is a sheaf of rings, or of $\mathcal{O}_X$-algebras, whose sections over an open set are the operators on the restriction of $\mathcal{F}$; it acts on $\mathcal{F}$, making $\mathcal{F}$ a sheaf of modules over it. The stalk of the sheaf of operators maps injectively to the endomorphism ring of the stalk, and the map is an isomorphism exactly when the sheaf is of finite presentation, in particular when it is locally free of finite rank or coherent; then $\mathcal{E}nd(\mathcal{F})_x\cong M_r(\mathcal{O}_{X,x})$ and $\mathcal{E}nd(\mathcal{F})\cong\mathcal{F}\otimes\mathcal{F}^{\vee}$ for a locally free $\mathcal{F}$ of rank $r$. The structure sheaf is the basic case: $\mathcal{E}nd(\mathcal{O}_X)\cong\mathcal{O}_X$ and $\operatorname{End}(\mathcal{O}_X)\cong\mathcal{O}_X(X)$, with units the invertible global functions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{End}(\mathcal{F})=\operatorname{Hom}(\mathcal{F},\mathcal{F})$ | ring of operators on $\mathcal{F}$ |
| $ST=S\circ T$ | composition of operators; the factor on the right acts first |
| $\operatorname{Aut}(\mathcal{F})$ | group of invertible operators, the units of $\operatorname{End}(\mathcal{F})$ |
| $\operatorname{End}(\mathcal{F})^{\mathrm{op}}$ | opposite ring, product $S\cdot_{\mathrm{op}}T=TS$ |
| $L_a$, $R_a$ | left and right multiplication by $a$; $L_aR_b=R_bL_a$ |
| $\Sigma_u(T)=uTu^{-1}$ | sandwich by a unit $u$; an automorphism of $\operatorname{End}(\mathcal{F})$ |
| $m_a$ | multiplication by a scalar $a\in\mathcal{O}_X(X)$, in the centre |
| $Z(\operatorname{End}(\mathcal{F}))$ | centre; $\cong\mathcal{O}_X(X)$ for $\mathcal{F}$ locally free of rank $\geq 1$ |
| $\mathcal{E}nd(\mathcal{F})=\mathcal{H}om(\mathcal{F},\mathcal{F})$ | sheaf of operators; a sheaf of rings, of $\mathcal{O}_X$-algebras in the module case |
| $\Gamma(U,\mathcal{E}nd(\mathcal{F}))=\operatorname{End}(\mathcal{F}\rvert_U)$ | sections of the sheaf of operators |
| $\mathcal{E}nd(\mathcal{F})_x\to\operatorname{End}(\mathcal{F}_x)$ | comparison map; injective, an isomorphism for finite presentation |
| $\mathcal{F}^{\vee}$ | dual sheaf $\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F},\mathcal{O}_X)$ |

## Further Reading

- Alexander Grothendieck and Jean Dieudonné, *Éléments de géométrie algébrique I* (Publications Mathématiques de l'IHÉS 4, 1960), for the sheaves $\mathcal{H}om$ and $\mathcal{E}nd$ and the structure sheaf of a ringed space.
- Robin Hartshorne, *Algebraic Geometry* (Springer, 1977), for the endomorphism sheaf of a locally free sheaf and the identification $\mathcal{E}nd\cong\mathcal{F}\otimes\mathcal{F}^{\vee}$.
- Glen E. Bredon, *Sheaf Theory* (Springer, second edition, 1997), for sheaves of rings, the internal hom and the properties of the stalk functor.
- Roger Godement, *Topologie algébrique et théorie des faisceaux* (Hermann, 1958), for the sheaf-theoretic foundations used throughout.
- Saunders Mac Lane and Ieke Moerdijk, *Sheaves in Geometry and Logic* (Springer, 1992), for the internal hom in a category of sheaves and the corresponding universal property.
- Nicolas Bourbaki, *Algèbre commutative* (Hermann, then Springer), for the centre of a matrix ring and the module-theoretic facts used on the stalks.
