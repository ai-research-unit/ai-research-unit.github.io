
# __The Restriction and Extension Operators__

## Introduction

Let $j:\Omega\hookrightarrow X$ be the inclusion of an open subset of a topological space. There are three ways of passing between the sheaves on $\Omega$ and the sheaves on $X$, and they are related by adjunction: the **restriction** $j^*$, which sends a sheaf on $X$ to its restriction to $\Omega$; the **extension by zero** $j_!$, which sends a sheaf on $\Omega$ to the smallest sheaf on $X$ with the same sections over $\Omega$ and no sections off $\Omega$; and the **direct image** $j_*$, which sends a sheaf on $\Omega$ to the sheaf on $X$ whose sections over an open set $V$ are the sections over $V\cap \Omega$. Restriction is left adjoint to the direct image and right adjoint to the extension by zero, so the three form an adjoint chain

$$
j_!\ \dashv\ j^*\ \dashv\ j_* .
$$

The article studies the two ends of the chain as operators between the categories of sheaves on $\Omega$ and on $X$: restriction, which is a ring homomorphism on endomorphisms and preserves every limit and every colimit; the extension by zero, which is left adjoint to restriction and is exact; and the exactness each of the three functors preserves and each fails to preserve. The middle functor, the direct image, is the one already used in *Presheaves and Sheaves* for an arbitrary continuous map, and it is recalled here only as the right adjoint of restriction.

The restriction and the extension by zero are the functors from which the cohomological machinery of the category is built: the compactly supported cohomology of an open set is the cohomology of its extension by zero, and the sequences relating the cohomology of a space, of an open set and of its complement are the long exact sequences of these functors. The conventions and the notation for sheaves, stalks, restrictions and the sheaf $\mathcal{H}om$ are those of *Presheaves and Sheaves*; the cohomology $H^i(X,\mathcal{F})$ and the direct image $f_*$ are those of *Sheaf Cohomology* and *Derived Functors and Sheaf Cohomology*. Nothing analytic and nothing geometric is used: the extension by zero is a topological operation on the open subsets of $X$, and no form, no norm and no derivative occurs. Throughout, $j:\Omega\hookrightarrow X$ is an open immersion, $i:Z=X\setminus \Omega\hookrightarrow X$ is the complementary closed immersion, $\mathcal{F},\mathcal{G},\mathcal{H}$ are sheaves on $X$ and $\mathcal{M},\mathcal{N}$ are sheaves on $\Omega$, in the category of abelian groups or of $\mathcal{O}_X$-modules.

## The Restriction Functor

**Definition.** The **restriction** of a sheaf $\mathcal{F}$ on $X$ to the open set $\Omega$ is the sheaf $j^*\mathcal{F}$ on $\Omega$ with

$$
(j^*\mathcal{F})(V)=\mathcal{F}(V),\qquad V\subseteq \Omega \text{ open},
$$

and the restriction maps inherited from $\mathcal{F}$; it is also written $\mathcal{F}|_\Omega$. On morphisms, $j^*$ is the assignment $\varphi\mapsto\varphi|_\Omega$, and it is a functor $\mathrm{Sh}(X)\to\mathrm{Sh}(\Omega)$, the **restriction functor**.

**Proposition (stalks and exactness).** For every $x\in \Omega$, $(j^*\mathcal{F})_x=\mathcal{F}_x$, and the restriction functor is **exact**: it preserves kernels, cokernels, images, limits and colimits, the operations being computed sectionwise over the opens of $\Omega$.

*Proof.* The stalk formula is the identity of the filtered systems of open neighbourhoods of $x$ inside $\Omega$ and inside $X$, which coincide for $x\in \Omega$ because $\Omega$ is open. Exactness in each variable is the fact that the kernel, the cokernel and the image of a morphism of sheaves are computed open by open, as recorded in *Presheaves and Sheaves*; a functor that is computed open by open preserves all the diagrammatic constructions.

**Proposition (the restriction of operators).** Restriction is a functor, so it carries an operator $T\in\operatorname{End}(\mathcal{F})$ to the operator $T|_\Omega=j^*(T)\in\operatorname{End}(\mathcal{F}|_\Omega)$, and

$$
j^*:\operatorname{End}(\mathcal{F})\longrightarrow\operatorname{End}(j^*\mathcal{F}),\qquad T\mapsto T|_\Omega,
$$

is a unital ring homomorphism; for sheaves of $\mathcal{O}_X$-modules it is a homomorphism of $\mathcal{O}_X(X)$-algebras whose target is an $\mathcal{O}_X(X)$-algebra through the restriction $\mathcal{O}_X(X)\to\mathcal{O}_X(\Omega)$. The kernel consists of the operators vanishing on $\Omega$, that is, of the operators factoring through the quotient $\mathcal{F}\to i_*(\mathcal{F}|_Z)$ of the closed-complement sequence recalled below.

*Proof.* A functor carries endomorphisms to endomorphisms and preserves composition and identities; the linearity of $j^*$ on hom-groups gives the additivity, and the compatibility with scalars is the definition of the restriction of a module morphism. An operator is zero on $\Omega$ exactly when its image in $\mathcal{F}|_\Omega$ is zero, which by the universal property of the cokernel is the statement that it factors through the cokernel of the inclusion $j_!(\mathcal{F}|_\Omega)\hookrightarrow\mathcal{F}$.

**Remark (restriction is not full).** Restriction is faithful, since a morphism of sheaves is determined by its restriction to an open cover, but it is not full: an operator on $\mathcal{F}|_\Omega$ need not extend to an operator on $\mathcal{F}$. The obstruction to the extension of operators is the subject of the extension by zero and of the adjunction of the next two sections.

## The Extension by Zero

**Definition.** The **extension by zero** of a sheaf $\mathcal{M}$ on $\Omega$ is the sheaf $j_!\mathcal{M}$ on $X$ obtained by sheafifying the presheaf

$$
V\longmapsto \begin{cases}\mathcal{M}(V), & V\subseteq \Omega,\\ 0, & V\not\subseteq \Omega.\end{cases}
$$

It is a functor $j_!:\mathrm{Sh}(\Omega)\to\mathrm{Sh}(X)$, and it is a subsheaf of the direct image $j_*\mathcal{M}$, namely the subsheaf of sections whose support is contained in $\Omega$, with support in the sense of *Presheaves and Sheaves*.

**Proposition (stalks and support).** For every $x\in X$,

$$
(j_!\mathcal{M})_x= \begin{cases}\mathcal{M}_x, & x\in \Omega,\\ 0, & x\notin \Omega,\end{cases}
$$

so that $\operatorname{Supp}(j_!\mathcal{M})$ is a closed subset of $X$ contained in $\Omega$, and $j_!\mathcal{M}$ is the unique sheaf on $X$ with these stalks and with a morphism $j_!\mathcal{M}\to j_*\mathcal{M}$ that is an isomorphism over $\Omega$. In particular $j_!\mathcal{M}$ is a subsheaf of $j_*\mathcal{M}$ and the quotient $j_*\mathcal{M}/j_!\mathcal{M}$ is supported in $X\setminus \Omega$.

*Proof.* The stalk of the sheafification at $x$ is the stalk of the presheaf, which is the colimit over the open neighbourhoods $V$ of $x$ of the values displayed; for $x\in \Omega$ the cofinal system of the $V\subseteq \Omega$ contributes $\mathcal{M}_x$, and for $x\notin \Omega$ every $V$ in the system contains points outside $\Omega$ and the colimit is $0$. The support statement is the complement of the vanishing locus, which is open by the first part. The identification with a subsheaf of $j_*\mathcal{M}$ is the universal property of the sheafification, and the stalk computation identifies the quotient.

**Proposition (exactness).** The extension by zero is exact.

*Proof.* On stalks, $(j_!\varphi)_x$ is $\varphi_x$ for $x\in \Omega$ and $0$ for $x\notin \Omega$ by the previous proposition; a sequence of sheaves on $\Omega$ is exact if and only if it is exact on every stalk, and each of the induced maps of stalks is either the corresponding map of the exact sequence or the zero map between zero groups. Hence an exact sequence on $\Omega$ extends to an exact sequence on $X$, and $j_!$ preserves kernels and cokernels.

**Example (the extension is not the direct image).** For $\Omega=(0,1)\subset X=\mathbb{R}$ and the constant sheaf $\underline{\mathbb{Z}}_\Omega$, the direct image $j_*\underline{\mathbb{Z}}_\Omega$ has global sections $\mathbb{Z}$ and the extension by zero $j_!\underline{\mathbb{Z}}_\Omega$ has global sections $0$: a nonzero locally constant function on $(0,1)$ has support $(0,1)$, which is not closed in $\mathbb{R}$, so it is not a section of the extension. The two functors differ exactly on the sections near the boundary of $\Omega$.

## The Adjunction $j_!\dashv j^*\dashv j_*$

**Theorem (the adjoint chain).** For an open immersion $j:\Omega\hookrightarrow X$ there are natural bijections, for $\mathcal{M}$ on $\Omega$ and $\mathcal{F}$ on $X$,

$$
\operatorname{Hom}_X(j_!\mathcal{M},\mathcal{F})\cong\operatorname{Hom}_\mathrm{U}(\mathcal{M},j^*\mathcal{F}),\qquad \operatorname{Hom}_\Omega(j^*\mathcal{F},\mathcal{M})\cong\operatorname{Hom}_X(\mathcal{F},j_*\mathcal{M}),
$$

so that $j_!$ is left adjoint to $j^*$, and $j^*$ is left adjoint to $j_*$.

*Proof.* A morphism $j_!\mathcal{M}\to\mathcal{F}$ is determined by its restriction to the opens contained in $\Omega$, since those opens generate $j_!\mathcal{M}$; its restriction to $\Omega$ is a morphism $\mathcal{M}\to\mathcal{F}|_\Omega$, and conversely such a morphism extends uniquely to $j_!\mathcal{M}$ by the universal property of the sheafification. This is the first adjunction. The second is the adjunction $f^*\dashv f_*$ of *Presheaves and Sheaves* for the continuous map $j$, with $f^*=f^{-1}=j^*$ for an open immersion.

**Corollary (units and counits).** The unit $\eta:\mathrm{id}\to j^*j_!$ and the counit $\varepsilon:j_!j^*\to\mathrm{id}$ of the first adjunction satisfy: $\eta_{\mathcal{M}}:\mathcal{M}\to j^*(j_!\mathcal{M})$ is an isomorphism for every $\mathcal{M}$, and $\varepsilon_{\mathcal{F}}:j_!(j^*\mathcal{F})\to\mathcal{F}$ is the inclusion of the subsheaf of sections of $\mathcal{F}$ supported in $\Omega$. The unit $\eta':\mathrm{id}\to j^*j_*$ and the counit $\varepsilon':j_*j^*\to\mathrm{id}$ of the second satisfy: $\eta'_{\mathcal{M}}:\mathcal{M}\to j^*(j_*\mathcal{M})$ is an isomorphism for every $\mathcal{M}$, and $\varepsilon'_{\mathcal{F}}:j_*(j^*\mathcal{F})\to\mathcal{F}$ is the natural restriction map.

*Proof.* The two statements on the units are the stalk identities $(j^*j_!\mathcal{M})_x=\mathcal{M}_x$ for $x\in \Omega$ and $(j^*j_*\mathcal{M})_x=\mathcal{M}_x$ for $x\in \Omega$, which hold for every $x\in \Omega$; the statements on the counits are the descriptions of $j_!\mathcal{M}$ and $j_*\mathcal{M}$ in the previous section.

**Corollary (the three functors preserve limits and colimits).** $j_!$ preserves colimits, being a left adjoint; $j_*$ preserves limits, being a right adjoint; $j^*$ preserves both limits and colimits, being both a left and a right adjoint. Equivalently, $j_!$ is right exact, $j_*$ is left exact, and $j^*$ is exact, in agreement with the direct computations above.

*Proof.* A left adjoint preserves colimits and a right adjoint preserves limits, by the general adjoint functor theorem; $j^*$ has a left adjoint $j_!$ and a right adjoint $j_*$, so it preserves colimits and limits.

**Remark (the closed complement).** The complementary closed immersion $i:Z\hookrightarrow X$ gives a direct image $i_*$ that is exact and fully faithful, and there is a short exact sequence of sheaves on $X$

$$
0\to j_!(\mathcal{F}|_\Omega)\to\mathcal{F}\to i_*(\mathcal{F}|_Z)\to 0 ,
$$

the **open-closed sequence**, whose exactness is the stalk computation of the previous section; its long exact sequence in cohomology is derived in *Sheaf Cohomology*, where the cohomology with support in a closed set is defined, and it is the basic exact sequence relating the cohomology of $X$, of $\Omega$ and of $Z$. The present article supplies the operator-theoretic content of the sequence — the three functors and their adjunctions — and does not repeat the cohomological construction.

## The Exactness Preserved

**Theorem (exactness).** Let $j:\Omega\hookrightarrow X$ be an open immersion.

1. $j^*$ is exact: it preserves kernels, cokernels, images and all limits and colimits.
2. $j_!$ is exact: it preserves kernels and cokernels, and it preserves colimits because it is a left adjoint.
3. $j_*$ is left exact and not right exact in general: it preserves kernels and finite limits, and it does not preserve cokernels.

*Proof.* (1) is the sectionwise computation of *The Restriction Functor* and the adjoint-chain corollary. (2) is the stalk computation of *The Extension by Zero* and the left-adjoint property. (3) The preservation of limits is the right-adjoint property; the failure of right exactness is the failure of the direct image to commute with cokernels, recorded for a general continuous map in *Presheaves and Sheaves*, and exhibited there by the exponential sequence.

**Corollary (derived functors).** Since $j_!$ is exact, $R^p j_!=0$ for $p>0$, and the derived functors of the extension by zero are trivial; in particular the cohomology of $X$ with coefficients in $j_!\mathcal{M}$ is computed by the naive complex, $H^i(X,j_!\mathcal{M})=H^i\bigl(\Gamma(X,j_!\mathcal{M}^\bullet)\bigr)$ for any resolution $\mathcal{M}^\bullet$ of $\mathcal{M}$ by sheaves on $\Omega$. Since $j_*$ is left exact and not right exact, it has higher direct images $R^p j_*$, the sheaves on $X$ with stalk $(R^pj_*\mathcal{M})_x=\varinjlim_{V\ni x}H^p(V\cap \Omega,\mathcal{M})$, computed in *Sheaf Cohomology* and *Derived Functors and Sheaf Cohomology*.

**Example (the failure of right exactness of the direct image).** Let $X=\mathbb{C}^*$ and let $\Omega\subset X$ be a simply connected open subset; let $\mathcal{O}$ be the sheaf of continuous complex-valued functions on $\Omega$ and $\mathcal{O}^*$ the sheaf of nowhere-zero ones. The exponential map is a surjection of sheaves on $\Omega$, and $j_*$ preserves its kernel; but a global section of $j_*\mathcal{O}^*$ over $X$ need not lie in the image of $j_*\mathcal{O}\to j_*\mathcal{O}^*$, since the identity function of $X$ has no continuous logarithm. Hence $j_*$ does not preserve the cokernel of the first map, and it is not right exact.

## The Operators Induced on Cohomology

**Proposition (extension preserves cohomology of the open set).** The exactness of $j_!$ gives, for every $i$,

$$
H^i(X,j_!\mathcal{M})\cong H^i_c(\Omega,\mathcal{M}),
$$

the cohomology of $\Omega$ with support in the family of closed subsets of $X$ contained in $\Omega$; the identification is the one of *Sheaf Cohomology* for sections with support in a family, and for a compact space, or when every closed subset of $X$ contained in $\Omega$ is compact, these are the compactly supported sections.

*Proof.* The global sections of $j_!\mathcal{M}$ are the sections of $\mathcal{M}$ over $\Omega$ whose support is closed in $X$; the functor $\Gamma(X,j_!-)$ is therefore the functor of sections with support in the family of closed subsets contained in $\Omega$, and its right derived functors are the cohomology with support in that family. The derived functors are computed by an injective resolution of $\mathcal{M}$, which $j_!$ carries to an exact functor's image, giving the identification.

**Proposition (restriction on cohomology).** Restriction induces, for every $i$, a natural map

$$
H^i(X,\mathcal{F})\longrightarrow H^i(\Omega,\mathcal{F}|_\Omega),
$$

the **restriction map on cohomology**, obtained by applying the functor of global sections of $\Omega$ to an acyclic resolution of $\mathcal{F}$ and restricting its terms; it is the edge map of the adjoint chain, and its kernel and cokernel are described by the open-closed sequence of the previous sections. The extension by zero is the left adjoint of the restriction on the level of the operator categories, and its effect on cohomology is the isomorphism of the preceding proposition.

*Proof.* An acyclic resolution of $\mathcal{F}$ restricts to an acyclic resolution of $\mathcal{F}|_\Omega$, since the restriction functor is exact and carries injective sheaves to injective sheaves; applying $\Gamma(\Omega,-)$ and comparing with the complex of $\Gamma(X,-)$ gives the map. The description of its kernel and cokernel is the long exact sequence of the open-closed sequence.

## Worked Cases

### The Constant Sheaf on an Open Interval

Let $X=\mathbb{R}$ and $\Omega=(0,1)$ with the constant sheaf $\underline{\mathbb{Z}}_\Omega$. Every section of $j_!\underline{\mathbb{Z}}_\Omega$ over $\mathbb{R}$ is a locally constant function on $(0,1)$ with support closed in $\mathbb{R}$; a nonzero constant function on $(0,1)$ has support $(0,1)$, which is not closed in $\mathbb{R}$, so

$$
\Gamma(\mathbb{R},j_!\underline{\mathbb{Z}}_\Omega)=0,\qquad H^i(\mathbb{R},j_!\underline{\mathbb{Z}}_\Omega)=0 \text{ for all } i,
$$

while $\Gamma(X,j_*\underline{\mathbb{Z}}_\Omega)=\mathbb{Z}$ and $\Gamma(\Omega,\underline{\mathbb{Z}}_\Omega)=\mathbb{Z}$. The example separates the three functors on the simplest space.

### The Two-Point Space

Let $X=\{p,q\}$ be discrete and let $\Omega=\{p\}$. A sheaf on $\Omega$ is an abelian group $A$, and $j_!A$ is the skyscraper at $p$ with value $A$ studied in *Operators on a Sheaf*; the direct image $j_*A$ is the same skyscraper, since $p$ is also closed and open. Restriction $j^*$ is the functor taking a sheaf to its stalk at $p$. The adjunction $j_!\dashv j^*$ reads $\operatorname{Hom}(j_!A,\mathcal{F})\cong\operatorname{Hom}(A,\mathcal{F}_p)$, which is the universal property of the skyscraper, and $j^*$ is exact on a discrete space.

### The Complement of a Point

Let $X=S^1$ and $\Omega=S^1\setminus\{x\}$, an open interval. The open-closed sequence attaches to every sheaf $\mathcal{F}$ on $X$ the sequence $0\to j_!(\mathcal{F}|_\Omega)\to\mathcal{F}\to (i_x)_*\mathcal{F}_x\to 0$; the two ends are the extension by zero, the simplest sheaf with no section off $\Omega$, and the skyscraper at $x$, the simplest sheaf concentrated at a point. The intermediate extension $j_!j^*\to\mathrm{id}$ is the counit, and the sequence exhibits it as the subsheaf of sections carried by $\Omega$.

## Summary

For an open immersion $j:\Omega\hookrightarrow X$ there are three functors between the sheaves on $\Omega$ and the sheaves on $X$: the restriction $j^*=(-)|_\Omega$, the extension by zero $j_!$, and the direct image $j_*$. Restriction is exact, its stalks at the points of $\Omega$ are the stalks of the sheaf, and on operators it is a ring homomorphism $\operatorname{End}(\mathcal{F})\to\operatorname{End}(\mathcal{F}|_\Omega)$. The extension by zero is the sheafification of the padded presheaf, it has the same stalks as the original sheaf on $\Omega$ and zero stalks off $\Omega$, its support is closed and contained in $\Omega$, and it is a subsheaf of the direct image whose quotient is supported off $\Omega$; it is exact because an exact sequence can be checked on the stalks.

The three functors form the adjoint chain $j_!\dashv j^*\dashv j_*$: extension is left adjoint to restriction, restriction is left adjoint to the direct image. The unit $\mathrm{id}\to j^*j_!$ is an isomorphism, the counit $j_!j^*\to\mathrm{id}$ is the inclusion of the sections supported in $\Omega$, and dually for the second adjunction. Consequently $j_!$ preserves colimits and is exact, $j^*$ preserves limits and colimits and is exact, and $j_*$ preserves limits and is left exact but not right exact. The derived functors of the extension by zero vanish in positive degree, and its cohomology is the cohomology of the open set with support in $\Omega$; the higher direct images $R^pj_*$ organise the cohomology of the open subset into a sheaf on $X$. The open-closed sequence $0\to j_!(\mathcal{F}|_\Omega)\to\mathcal{F}\to i_*(\mathcal{F}|_Z)\to0$ is the basic exact sequence, whose cohomological consequences belong to *Sheaf Cohomology*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $j:\Omega\hookrightarrow X$ | open immersion; $i:Z=X\setminus \Omega\hookrightarrow X$ its closed complement |
| $j^*\mathcal{F}=\mathcal{F}\rvert_\Omega$ | restriction to the open set; exact |
| $j_!\mathcal{M}$ | extension by zero of a sheaf on $\Omega$; exact |
| $j_*\mathcal{M}$ | direct image; left exact, the right adjoint of $j^*$ |
| $j_!\dashv j^*\dashv j_*$ | the adjoint chain of the three functors |
| $\eta,\varepsilon$ | unit and counit of $j_!\dashv j^*$ |
| $\eta',\varepsilon'$ | unit and counit of $j^*\dashv j_*$ |
| $\operatorname{Supp}(j_!\mathcal{M})$ | closed set contained in $\Omega$; $j_!\mathcal{M}$ vanishes off $\Omega$ |
| $R^pj_!$, $R^pj_*$ | derived functors; $R^pj_!=0$ for $p>0$, $R^pj_*$ the higher direct images |
| $H^i(X,j_!\mathcal{M})=H^i_c(\Omega,\mathcal{M})$ | cohomology with support in the closed subsets of $\Omega$ |
| $0\to j_!(\mathcal{F}\rvert_\Omega)\to\mathcal{F}\to i_*(\mathcal{F}\rvert_Z)\to0$ | the open-closed sequence |

## Further Reading

- Robin Hartshorne, *Algebraic Geometry* (Springer, 1977), for the adjoint pairs $j_!\dashv j^*\dashv j_*$ and the extension by zero for the open immersions of schemes.
- Glen E. Bredon, *Sheaf Theory* (Springer, second edition, 1997), for the extension by zero, the open-closed sequence and cohomology with support.
- Roger Godement, *Topologie algébrique et théorie des faisceaux* (Hermann, 1958), for the direct and inverse images, their adjunction and their exactness.
- Birger Iversen, *Cohomology of Sheaves* (Springer, 1986), for the adjoint chain and the exceptional functors attached to an immersion.
- Saunders Mac Lane, *Categories for the Working Mathematician*, 2nd ed. (Springer, 1998), for the general adjoint functor theorem and the preservation of limits and colimits by adjoints.
- Masaki Kashiwara and Pierre Schapira, *Sheaves on Manifolds* (Springer, 1990), for the six operations and the role of the extension by zero among them.
