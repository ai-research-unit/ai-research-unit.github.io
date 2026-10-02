
# __The Coboundary Operator__

## Introduction

A **complex of sheaves** on a space $X$ is a sequence of sheaves $\mathcal{F}^i$ and morphisms

$$
\cdots\to\mathcal{F}^{i-1}\xrightarrow{\ d^{i-1}\ }\mathcal{F}^{i}\xrightarrow{\ d^{i}\ }\mathcal{F}^{i+1}\to\cdots
$$

with $d^i\circ d^{i-1}=0$ for every $i$. The morphisms $d^i$ are the **coboundary operators** of the complex, and the identity $d\circ d=0$ — the **square-zero property** — is what makes the cohomology sheaves $\mathcal{H}^i(\mathcal{F}^\bullet)=\ker d^i/\operatorname{im}d^{i-1}$ defined. The coboundary is the single operator from which every cohomological construction of the category is built: the sheaf cohomology $H^i(X,\mathcal{F})$ is the cohomology of the complex of global sections of an acyclic resolution of $\mathcal{F}$, the Čech groups of *Čech Cohomology* are the cohomology of a complex of sheaves, and the comparison theorems of *Sheaf Cohomology* identify these complexes by showing that their coboundaries define the same cohomology.

This article develops the coboundary operator in the form in which it is used on a space: complexes of sheaves, the square-zero identity and its consequences, the cohomology sheaves and their stalks, the relation to the cohomology of the complex of global sections and to the hypercohomology, and the connecting homomorphism of a short exact sequence of complexes. The general theory of complexes and their derived categories, of spectral sequences and of derived functors is Part I's, in *Homological Algebra*, *Derived Functors*, *Spectral Sequences* and *Derived Categories*, and it is cited rather than reproduced; the sheaf-theoretic instances are what is developed. The particular complexes attached to the geometry of a space — the Čech complex of a cover, the singular cochain complex, the Godement resolution — have their coboundaries computed in *Čech Cohomology*, in *Sheaf Cohomology* and in *Simplicial and Singular Homology*, and they are cited here rather than recomputed.

The conventions are those of *Presheaves and Sheaves* for sheaves and stalks and of *Sheaf Cohomology* for the cohomology $H^i(X,\mathcal{F})$ and the derived functors. The de Rham complex of a manifold is a complex of sheaves whose coboundary is the exterior derivative; the exterior derivative belongs to *Differential Forms and Stokes' Theorem* in Part III, and the de Rham complex is developed in *Sheaves and the de Rham Complex*, so no exterior derivative occurs here. Nothing analytic and nothing geometric is used. Throughout, $(\mathcal{F}^\bullet,d)$ is a complex of sheaves of abelian groups on $X$, or of $\mathcal{O}_X$-modules, bounded below or unbounded as stated, and the differentials are written $d$ when the degree is clear and $d^i:\mathcal{F}^i\to\mathcal{F}^{i+1}$ otherwise.

## Complexes of Sheaves

**Definition.** A **cochain complex of sheaves** on $X$ is a family $(\mathcal{F}^i)_{i\in\mathbb{Z}}$ of sheaves and morphisms $d^i:\mathcal{F}^i\to\mathcal{F}^{i+1}$ with $d^{i+1}d^i=0$ for every $i$. A **morphism of complexes** $\varphi:(\mathcal{F}^\bullet,d)\to(\mathcal{G}^\bullet,e)$ is a family of morphisms $\varphi^i:\mathcal{F}^i\to\mathcal{G}^i$ with $e^i\varphi^i=\varphi^{i+1}d^i$, that is, commuting with the coboundaries; a morphism is a **quasi-isomorphism** if it induces isomorphisms on all the cohomology sheaves defined below.

**Definition.** The **shift** $\mathcal{F}^\bullet[1]$ of a complex is the complex with $(\mathcal{F}^\bullet[1])^i=\mathcal{F}^{i+1}$ and differential $-d^{i+1}$; the iterated shifts $\mathcal{F}^\bullet[k]$ with differential $(-1)^kd$ are defined in the same way. The complexes of sheaves on $X$ and their morphisms form the category $\mathbf{C}(\mathrm{Sh}(X))$, which is additive, and an abelian category when the coefficient category is the category of abelian groups or of modules.

**Definition.** If $\mathcal{F}$ is a single sheaf and $T:\mathcal{F}\to\mathcal{F}$ an operator with $T^2=0$, the pair $(\mathcal{F},T)$ is the **two-term complex** with $\mathcal{F}^0=\mathcal{F}^1=\mathcal{F}$, $d^0=T$ and $d^i=0$ for $i\ne 0$. More generally a **graded sheaf** $\mathcal{F}^\bullet=\bigoplus_i\mathcal{F}^i$ carries the operator $d=\bigoplus_i d^i$ of degree one, and the square-zero property is the single identity $d^2=0$ on the graded sheaf.

**Proposition (the complex is a dg-object).** The data of a complex of sheaves is equivalent to the data of a graded sheaf $\mathcal{F}^\bullet$ with an endomorphism $d$ of degree one and square zero. The morphisms of complexes are the morphisms of graded sheaves commuting with $d$; the shift is the regrading with the signed differential. This is the sheaf-theoretic case of the graded objects of *Homological Algebra*, and it is recorded so that the operator language and the index language agree.

*Proof.* The equivalence is the collection of the degree-one components of $d$ into the maps $d^i$; the identity $d^2=0$ collects into $d^{i+1}d^i=0$ for all $i$; and a morphism of graded sheaves respecting $d$ is exactly a family of morphisms commuting with the differentials.

## The Square-Zero Property

**Proposition (the induced map on cohomology is zero).** If $d^i:\mathcal{F}^i\to\mathcal{F}^{i+1}$ is a coboundary of a complex, then $d^i$ carries the cocycles $\ker d^i$ into the coboundaries $\operatorname{im}d^i$, and consequently the map induced by $d^i$ on the cohomology sheaves is zero:

$$
d^i(\ker d^i)\subseteq\operatorname{im}d^i,\qquad \mathcal{H}^i(\mathcal{F}^\bullet)\to\mathcal{H}^{i+1}(\mathcal{F}^\bullet)\ \text{induced by}\ d^i\ \text{is}\ 0 .
$$

*Proof.* If $s\in\ker d^i$, then $d^i(s)\in\operatorname{im}d^i$ by definition of the image, and $d^i(s)\in\ker d^{i+1}$ because $d^{i+1}d^i=0$; so $d^i(s)$ is a coboundary, and its class in $\mathcal{H}^{i+1}$ is zero.

**Proposition (square zero is a local condition).** For a complex of sheaves the identity $d^2=0$ holds if and only if it holds on every stalk; for a complex of sheaves of $\mathcal{O}_X$-modules it suffices that it hold on the sections over a basis of the topology.

*Proof.* A morphism of sheaves is zero if and only if its stalk maps are zero, and the composite $d^{i+1}d^i$ is a morphism of sheaves; the second statement is the sheaf condition applied to the morphism $d^{i+1}d^i$ and a basis of the topology.

**Proposition (the concrete complexes).** The coboundary of the Čech complex of a cover in the alternating convention, the singular coboundary of a locally contractible space, and the differential of the Godement resolution all satisfy $d^2=0$; the proofs are the standard cancellations recorded in *Čech Cohomology*, in *Simplicial and Singular Homology* and in *Sheaf Cohomology* respectively. The exterior derivative of the de Rham complex, which is the coboundary of the complex of sheaves of differential forms, satisfies $d^2=0$ by the equality of mixed partial derivatives, and is *Sheaves and the de Rham Complex* of Part III, cited here and not used.

*Proof.* The statements are the cited computations; the general mechanism in each case is that $d$ is the alternating sum of face maps, or the transpose of a boundary, and the compositions cancel in pairs. No computation is repeated here.

## The Cohomology Sheaves

**Definition.** The **cohomology sheaves** of the complex $(\mathcal{F}^\bullet,d)$ are the sheaves

$$
\mathcal{H}^i(\mathcal{F}^\bullet)=\ker d^i/\operatorname{im}d^{i-1},
$$

the quotient in the abelian category of sheaves; the kernel and the image are the sheaf-theoretic ones of *Presheaves and Sheaves*, and the quotient is well defined because $\operatorname{im}d^{i-1}\subseteq\ker d^i$ is a subsheaf, by the square-zero property. A complex is **exact** at $\mathcal{F}^i$ if $\mathcal{H}^i(\mathcal{F}^\bullet)=0$, and **exact** if it is exact at every degree; a **resolution** of a sheaf $\mathcal{F}$ is an exact complex with $\mathcal{F}$ in degree zero.

**Proposition (stalks of the cohomology sheaves).** For every $x\in X$ and every $i$,

$$
\mathcal{H}^i(\mathcal{F}^\bullet)_x\cong H^i(\mathcal{F}^\bullet_x),
$$

the cohomology of the complex of stalks; and a morphism of complexes is a quasi-isomorphism if and only if it induces an isomorphism on the complexes of stalks at every point.

*Proof.* The stalk functor is exact, as recorded in *Presheaves and Sheaves*, so it commutes with the formation of kernels, images and quotients; applying it to the defining quotient gives the isomorphism, and the second statement is the first applied to the induced maps.

**Corollary (exactness is a local condition).** A complex of sheaves is exact if and only if its complex of stalks at every point is exact; equivalently, if and only if every point has a neighbourhood over which the complex is exact.

*Proof.* By the proposition $\mathcal{H}^i(\mathcal{F}^\bullet)=0$ if and only if every stalk vanishes, and a sheaf with zero stalks is zero.

**Corollary (the degree-zero cohomology).** $\mathcal{H}^0(\mathcal{F}^\bullet)=\ker d^0$, and if the complex is a resolution of $\mathcal{F}$, then $\mathcal{H}^0(\mathcal{F}^\bullet)\cong\mathcal{F}$ and $\mathcal{H}^i(\mathcal{F}^\bullet)=0$ for $i\ne0$.

*Proof.* In degree zero there is no incoming differential, so the quotient defining $\mathcal{H}^0$ is $\ker d^0$; exactness in the other degrees is the definition of a resolution.

## Global Sections and Hypercohomology

**Definition.** The **global sections of the complex** are the complex of abelian groups

$$
\Gamma(X,\mathcal{F}^\bullet)=\Bigl(\cdots\to\Gamma(X,\mathcal{F}^{i-1})\xrightarrow{\ d^{i-1}\ }\Gamma(X,\mathcal{F}^i)\xrightarrow{\ d^i\ }\Gamma(X,\mathcal{F}^{i+1})\to\cdots\Bigr),
$$

whose coboundary is the coboundary of $\mathcal{F}^\bullet$ applied to sections, and whose cohomology is written $H^i\bigl(\Gamma(X,\mathcal{F}^\bullet)\bigr)$.

**Theorem (the abstract de Rham theorem).** If $(\mathcal{F}^\bullet,d)$ is a resolution of a sheaf $\mathcal{F}$ by acyclic sheaves, $H^j(X,\mathcal{F}^i)=0$ for $j>0$, then there is a natural isomorphism

$$
H^i\bigl(\Gamma(X,\mathcal{F}^\bullet)\bigr)\cong H^i(X,\mathcal{F})
$$

for every $i$. More generally, any resolution whose complex of sections is effaceable computes the cohomology.

*Proof.* This is the abstract de Rham theorem of *Derived Functors and Sheaf Cohomology*, where the effaceability argument is given; it is quoted here as the reason the coboundary of a resolution computes the cohomology of the resolved sheaf.

**Definition.** The **hypercohomology** of a bounded below complex $\mathcal{F}^\bullet$ is

$$
\mathbb{H}^i(X,\mathcal{F}^\bullet)=R^i\Gamma(X,\mathcal{F}^\bullet),
$$

the right derived functors of global sections applied to the complex, computed by replacing $\mathcal{F}^\bullet$ by a quasi-isomorphic complex of injective sheaves; when $\mathcal{F}^\bullet$ is a resolution of a single sheaf $\mathcal{F}$ in degree zero, $\mathbb{H}^i(X,\mathcal{F}^\bullet)\cong H^i(X,\mathcal{F})$ by the theorem.

**Proposition (the two spectral sequences).** The filtration of the total complex of a bounded below complex by the first and by the second degree gives the two spectral sequences

$$
{}^{\mathrm{I}}E_1^{p,q}=H^q\bigl(X,\mathcal{F}^p\bigr)\Longrightarrow\mathbb{H}^{p+q}(X,\mathcal{F}^\bullet),\qquad {}^{\mathrm{II}}E_2^{p,q}=H^p\bigl(X,\mathcal{H}^q(\mathcal{F}^\bullet)\bigr)\Longrightarrow\mathbb{H}^{p+q}(X,\mathcal{F}^\bullet),
$$

whose construction is *Spectral Sequences* and *Derived Functors and Sheaf Cohomology*; they are recorded here because they express the coboundary of a complex of sheaves in terms of the cohomology of its cohomology sheaves, and they are not used further in this article.

## The Connecting Homomorphism

**Theorem (the long exact sequence of a short exact sequence of complexes).** A short exact sequence of complexes

$$
0\to\mathcal{F}^\bullet\xrightarrow{\ \varphi\ }\mathcal{G}^\bullet\xrightarrow{\ \psi\ }\mathcal{H}^\bullet\to0
$$

gives a long exact sequence of cohomology sheaves

$$
\cdots\to\mathcal{H}^i(\mathcal{F}^\bullet)\xrightarrow{\ \varphi\ }\mathcal{H}^i(\mathcal{G}^\bullet)\xrightarrow{\ \psi\ }\mathcal{H}^i(\mathcal{H}^\bullet)\xrightarrow{\ \delta\ }\mathcal{H}^{i+1}(\mathcal{F}^\bullet)\to\cdots
$$

with connecting morphisms $\delta$ natural in the sequence; applying global sections gives the same long exact sequence for the cohomology $H^i(\Gamma(X,-))$ of the complexes.

*Proof.* The proof is the snake lemma applied degreewise to the diagram of the two adjacent coboundaries; the connecting map sends the class of a cocycle $h\in\ker d_{\mathcal{H}}^i$ to the class of $d_{\mathcal{G}}^i(\tilde h)$ for a lift $\tilde h$ of $h$, which is a cocycle in $\mathcal{F}^{i+1}$ because $d^2=0$, and which is well defined modulo coboundaries by exactness of the rows. This is the general homological algebra of *Homological Algebra*, applied to the complexes of sheaves; the instance for the sheaf cohomology of a short exact sequence of a single sheaf is the long exact sequence of *Sheaf Cohomology*.

**Remark (the coboundary and the connecting map are different operators).** The coboundary $d$ is the differential of the complex and raises the internal degree of the grading; the connecting map $\delta$ is defined only in the presence of a short exact sequence of complexes and shifts the cohomological degree. Both are written with symbols suggesting a boundary, and in the classical complexes of topology the connecting map of the sequence of a pair is the transpose of the coboundary of the quotient complex; the article keeps the two apart, $d$ for the differential and $\delta$ for the connecting map.

**Proposition (functoriality of the coboundary).** A morphism of complexes commutes with the coboundary and induces morphisms $\mathcal{H}^i(\varphi)$ and $H^i(\Gamma(X,\varphi))$ on the cohomology; the inverse image $f^{-1}$ of a continuous map $f$ is exact and carries a complex of sheaves on $Y$ to a complex of sheaves on $X$ with $f^{-1}\mathcal{H}^i(\mathcal{F}^\bullet)=\mathcal{H}^i(f^{-1}\mathcal{F}^\bullet)$, while the direct image $f_*$ carries a complex on $X$ to a complex on $Y$ and commutes with the coboundary degreewise.

*Proof.* A morphism of complexes is defined by $e\varphi=\varphi d$, which is exactly the compatibility of $\varphi$ with the coboundaries; the induced maps on cohomology exist because $\varphi$ carries cocycles to cocycles and coboundaries to coboundaries, and the functoriality of $f^{-1}$ and $f_*$ makes the coboundary commute with them.

## Worked Cases

### The Čech Complex

The alternating Čech complex of an open cover is a complex of sheaves with coboundary the alternating sum of the restriction maps; the square-zero identity is the cancellation recorded in *Čech Cohomology*, and the cohomology sheaves of the Čech complex of a cover by acyclic sets are the cohomology sheaves of the coefficient sheaf. The article's general statements apply verbatim to this complex, and the computations belong to *Čech Cohomology*.

### The Singular Cochain Complex

On a locally contractible paracompact space the sheafified singular cochain complex is a complex of sheaves whose coboundary is the singular coboundary applied to the cochain coefficients; its cohomology sheaves are $\underline{A}$ in degree zero and zero above, and its global cohomology is the singular cohomology. The comparison with the constant sheaf is the comparison theorem of *Sheaf Cohomology*, and the square-zero identity is the standard cancellation of the singular theory.

### A Square-Zero Operator on a Single Sheaf

Let $\mathcal{F}$ be a sheaf and let $T:\mathcal{F}\to\mathcal{F}$ be an operator with $T^2=0$, with no grading. Then $T$ defines the two-term complex $0\to\mathcal{F}\xrightarrow{T}\mathcal{F}\to0$ with $\mathcal{H}^0=\ker T$ and $\mathcal{H}^1=\mathcal{F}/\operatorname{im}T$, and the exactness of the complex is the statement $\ker T=\operatorname{im}T$. The example shows that the coboundary operator of a complex with two terms is exactly the square-zero operator on a single sheaf, and that the cohomology sheaves are the kernel and the cokernel of $T$; the operators with $T^2=0$ are the simplest instances of a differential.

### The Mapping Cone

For a morphism of complexes $\varphi:\mathcal{F}^\bullet\to\mathcal{G}^\bullet$, the **mapping cone** is the complex with terms $\mathcal{G}^i\oplus\mathcal{F}^{i+1}$ and coboundary $d(g,f)=(dg+\varphi(f),-df)$; the sign $-1$ on the second component is what makes the square of the coboundary vanish, and the resulting long exact sequence is that of the contravariant triangle of $\varphi$. The construction is the standard one of *Derived Categories* and *Homological Algebra*; it is recorded here as the basic operation of the operator $d$ on complexes and is not developed.

## Summary

A complex of sheaves is a graded sheaf with a degree-one operator $d$ of square zero, equivalently a family of coboundaries $d^i$ with $d^{i+1}d^i=0$; the square-zero property is a local condition and holds on the concrete complexes of the category — the Čech, the singular, the Godement and the de Rham complexes — by the cancellations proved in the articles that own them. The cohomology sheaves $\mathcal{H}^i(\mathcal{F}^\bullet)=\ker d^i/\operatorname{im}d^{i-1}$ are computed on the stalks, $\mathcal{H}^i(\mathcal{F}^\bullet)_x\cong H^i(\mathcal{F}^\bullet_x)$, so that exactness of a complex is a local condition; the degree-zero cohomology is $\ker d^0$, and a resolution of $\mathcal{F}$ is a complex whose cohomology sheaves are $\mathcal{F}$ in degree zero and zero elsewhere.

Applying global sections to the complex gives the complex $\Gamma(X,\mathcal{F}^\bullet)$ with the same coboundary, and the abstract de Rham theorem identifies its cohomology with $H^i(X,\mathcal{F})$ when the complex is a resolution by acyclic sheaves; the hypercohomology $\mathbb{H}^i(X,\mathcal{F}^\bullet)$ is the derived functor of global sections on the complex, and its two spectral sequences express it in terms of the cohomology of the terms and of the cohomology sheaves. A short exact sequence of complexes gives a long exact sequence whose connecting map $\delta$ is not the coboundary $d$ but the map induced on the quotient by the pair of adjacent coboundaries; a morphism of complexes commutes with $d$ and induces maps on cohomology, and the inverse image is exact while the direct image commutes with $d$ degreewise. The mapping cone assembles a morphism of complexes into a square-zero operator on the sum.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\mathcal{F}^\bullet,d)$ | complex of sheaves with coboundary $d$ |
| $d^i:\mathcal{F}^i\to\mathcal{F}^{i+1}$ | the coboundary in degree $i$; $d^{i+1}d^i=0$ |
| $\mathcal{F}^\bullet[1]$, $\mathcal{F}^\bullet[k]$ | shift of a complex; differential $(-1)^kd$ |
| $\mathbf{C}(\mathrm{Sh}(X))$ | category of complexes of sheaves and their morphisms |
| $\mathcal{H}^i(\mathcal{F}^\bullet)=\ker d^i/\operatorname{im}d^{i-1}$ | cohomology sheaves |
| $\mathcal{H}^i(\mathcal{F}^\bullet)_x\cong H^i(\mathcal{F}^\bullet_x)$ | stalks of the cohomology sheaves |
| quasi-isomorphism | morphism inducing isomorphisms on all $\mathcal{H}^i$ |
| $\Gamma(X,\mathcal{F}^\bullet)$ | complex of global sections; coboundary applied to sections |
| $H^i(\Gamma(X,\mathcal{F}^\bullet))\cong H^i(X,\mathcal{F})$ | abstract de Rham theorem for an acyclic resolution |
| $\mathbb{H}^i(X,\mathcal{F}^\bullet)=R^i\Gamma(X,\mathcal{F}^\bullet)$ | hypercohomology |
| $\delta$ | connecting map of a short exact sequence of complexes |
| mapping cone | complex $\mathcal{G}^i\oplus\mathcal{F}^{i+1}$, coboundary $d(g,f)=(dg+\varphi(f),-df)$ |

## Further Reading

- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for complexes, the snake lemma, the connecting map and the derived-category constructions quoted here.
- Alexander Grothendieck, "Sur quelques points d'algèbre homologique", *Tohoku Mathematical Journal* 9 (1957), 119–221, for the abstract de Rham theorem and the effaceable functors.
- Glen E. Bredon, *Sheaf Theory* (Springer, second edition, 1997), for complexes of sheaves, their cohomology sheaves and hypercohomology.
- Roger Godement, *Topologie algébrique et théorie des faisceaux* (Hermann, 1958), for the canonical flabby resolution and its differential.
- Birger Iversen, *Cohomology of Sheaves* (Springer, 1986), for the mapping cone, the shift and the triangulated operations on complexes of sheaves.
- Masaki Kashiwara and Pierre Schapira, *Sheaves on Manifolds* (Springer, 1990), for the differential graded language and its sheaf-theoretic form.
