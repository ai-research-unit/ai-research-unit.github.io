
# __Homological Algebra__

## Introduction

Exact sequences measure the failure of a sequence to split and the failure of a functor to be exact, but they compute nothing by themselves. The instrument that computes is the chain complex: a graded module with a square-zero endomorphism, whose homology measures by how much the graded module fails to be exact. A resolution of a module by projective or injective modules is a chain complex that is exact except in one degree, and it is the object on which a functor is evaluated when its failure of exactness is to be measured. Homological algebra is the theory of these complexes, of the maps between them, and of the two facts that make the theory invariant — that maps of resolutions exist and are unique up to chain homotopy, and that a short exact sequence of complexes produces a long exact sequence in homology.

This article develops chain and cochain complexes, their morphisms, chain homotopies and mapping cones, the homology functor and the long exact sequence, projective and injective resolutions, the comparison theorem and the horseshoe lemma, and the tensor product and hom complexes that are used later. It is the foundation on which the homological articles of this category rest, and it supplies the categorical machinery that they apply to algebras.

Throughout, $\mathcal{A}$ is an abelian category, most often $R\text{-}\mathbf{Mod}$ for a commutative ring $R$ with $1 \neq 0$; chain complexes are written with lower indices and cochain complexes with upper indices, and the translation between them is the rule $C^n=C_{-n}$. The article uses the exactness language of *Exact Sequences*, the splitting lemma and the snake lemma, and the abelian-category framework of *Abelian and Grothendieck Categories*. It contains no topology: the words *complex*, *resolution*, *boundary* and *cycle* are algebraic throughout. The applications of the theory to sheaf cohomology and to algebraic topology need a space, and they are therefore deferred to Part II; the article states the results in their algebraic form and says explicitly where the geometric form is treated.

## Chain Complexes

### Complexes and Their Morphisms

**Definition.** A **chain complex** $(C_\bullet,d_\bullet)$ in an abelian category $\mathcal{A}$ consists of objects $C_n$ for $n \in \mathbb{Z}$ and morphisms $d_n:C_n\to C_{n-1}$ with $d_{n-1}d_n=0$ for every $n$. The maps $d_n$ are the **differentials** or **boundary maps**. A **cochain complex** $(C^\bullet,d^\bullet)$ consists of objects $C^n$ and maps $d^n:C^n\to C^{n+1}$ with $d^{n+1}d^n=0$; the two notions are the same under $C^n=C_{-n}$ and $d^n=d_{-n}$.

**Definition.** A **morphism of chain complexes** $f:(C_\bullet,d)\to(D_\bullet,e)$ is a family of morphisms $f_n:C_n\to D_n$ with $f_{n-1}d_n=e_n f_n$ for every $n$. The complexes and their morphisms form an abelian category $\mathbf{Ch}(\mathcal{A})$, with kernels, cokernels and exactness computed degreewise.

**Example.** The **Koszul complex** of a sequence $x_1,\dots,x_r$ in a commutative ring $R$ on a free module of rank $r$ has $K_p$ the $p$-th exterior power of $R^r$, and $d_p$ the contraction with $(x_1,\dots,x_r)$; the square-zero identity follows from the alternation of the wedge product. Its homology measures the failure of the sequence to be regular, and the exterior powers it uses are those of *Multilinear Spaces*.

**Example.** The **bar complex** of an algebra $A$ has $C_n=A^{\otimes n}$ with a differential built from the multiplication; its homology is the Hochschild homology , where the convention for the differential is fixed.

### Cycles, Boundaries and Homology

**Definition.** For a chain complex $C_\bullet$ the **cycles** are $Z_n=\ker d_n \subseteq C_n$, the **boundaries** are $B_n=\operatorname{im}d_{n+1}\subseteq C_n$, and the **homology** is

$$
H_n(C_\bullet)=\frac{Z_n}{B_n}=\frac{\ker(d_n:C_n\to C_{n-1})}{\operatorname{im}(d_{n+1}:C_{n+1}\to C_n)} .
$$

The complex is **exact** at $C_n$ if $H_n=0$, and **acyclic** if $H_n=0$ for every $n$. For a cochain complex the same definitions are written $Z^n$, $B^n$ and $H^n$.

Because $d_{n-1}d_n=0$, the inclusion $B_n\subseteq Z_n$ holds, so the quotient is defined; homology is precisely the obstruction to exactness.

**Proposition.** Homology is a functor: a morphism $f:C_\bullet\to D_\bullet$ of complexes induces $H_n(f):H_n(C)\to H_n(D)$ for every $n$, with $H_n(\operatorname{id})=\operatorname{id}$ and $H_n(gf)=H_n(g)H_n(f)$. The functor $H_n:\mathbf{Ch}(\mathcal{A})\to\mathcal{A}$ is additive.

*Proof.* A chain map carries $d_n$-cycles to $e_n$-cycles, because $d_n x=0$ implies $e_nf_n(x)=f_{n-1}d_nx=0$, and carries boundaries to boundaries, because $f_n d_{n+1}=e_{n+1}f_{n+1}$; hence it induces a map on the quotients. Functoriality is immediate from the definition. $\square$

**Proposition.** $H_n(C_\bullet)=0$ for all $n$ if and only if the complex is exact; the complex is exact at $C_n$ if and only if $\ker d_n=\operatorname{im}d_{n+1}$.

**Example (homology of a short exact sequence).** For a short exact sequence of modules $0\to A\xrightarrow{f}B\xrightarrow{g}C\to0$, regarded as a three-term complex concentrated in degrees $2,1,0$, the homology is $H_2=0$, $H_1=\ker g/\operatorname{im}f=0$, $H_0=C/\operatorname{im}g=0$, so the complex is acyclic: exactness is the vanishing of homology.

### The Euler Characteristic

Over a ring in which the relevant ranks are defined, the alternating sum of the ranks of the terms of a bounded complex computes the alternating sum of the homology.

**Proposition.** Let $C_\bullet$ be a complex of finitely generated free modules over a field $F$, nonzero in only finitely many degrees, and suppose $H_n(C_\bullet)$ is finite-dimensional for every $n$. Then

$$
\sum_n(-1)^n\dim_F C_n=\sum_n(-1)^n\dim_F H_n(C_\bullet).
$$

*Proof.* The short exact sequences $0\to Z_n\to C_n\to B_{n-1}\to0$ and $0\to B_n\to Z_n\to H_n\to0$ give $\dim C_n=\dim Z_n+\dim B_{n-1}$ and $\dim Z_n=\dim B_n+\dim H_n$. Substituting and summing with alternating signs telescopes, because the boundary contributions enter with opposite signs. $\square$

The number $\sum_n(-1)^n\dim_FC_n$ is the **Euler characteristic** and the identity is its invariance under homology. The corresponding statement for modules over a ring uses the rank of a finitely generated module and holds over a domain when the homology is free of finite rank.

## Exact Sequences of Complexes

### Short Exact Sequences of Complexes

**Definition.** A sequence of complexes $0\to A_\bullet\xrightarrow{f}B_\bullet\xrightarrow{g}C_\bullet\to0$ is **short exact** if for each $n$ the sequence $0\to A_n\to B_n\to C_n\to0$ is short exact in $\mathcal{A}$.

The snake lemma applied degreewise does not by itself produce a long exact sequence in homology, because the diagram of the lemma is only the first two rows of a larger diagram; the connecting map is constructed from the differentials of the three complexes together.

**Theorem.** For a short exact sequence of complexes $0\to A_\bullet\to B_\bullet\to C_\bullet\to0$ there is a long exact sequence in homology

$$
\cdots \longrightarrow H_n(A) \longrightarrow H_n(B) \longrightarrow H_n(C) \xrightarrow{\ \partial_n\ } H_{n-1}(A) \longrightarrow H_{n-1}(B) \longrightarrow \cdots,
$$

natural in the short exact sequence, with $\partial_n$ the connecting morphism.

*Proof.* The degreewise snake lemma applied to the map of complexes, in which the rows are the short exact sequences and the vertical maps are the differentials, gives the diagram

$$
H_n(A)\to H_n(B)\to H_n(C)\xrightarrow{\partial_n}H_{n-1}(A)\to H_{n-1}(B)\to H_{n-1}(C),
$$

and the construction of $\partial_n$ is the snake-lemma construction on the square with vertices $B_n$, $C_n$, $B_{n-1}$, $C_{n-1}$. Concretely, for a class $[c]\in H_n(C)$ choose $b \in B_n$ with $g_nb=c$; then $g_{n-1}(d_nb)=d_n^C g_n b=0$, so $d_nb=f_{n-1}(a)$ for a unique $a \in A_{n-1}$, and $\partial_n[c]=[a]$ in $H_{n-1}(A)$. The class is independent of the lift $b$ and of the representative $c$, and exactness at each term is the snake lemma. Naturality is immediate from the construction. $\square$

**Corollary.** If two of the three complexes are acyclic then so is the third; if $H_n(A)=H_n(B)=0$ then $H_n(C)=0$, and similarly in the other positions.

### The Mapping Cone

The connecting morphism can be packaged as the homology of a single complex.

**Definition.** For a morphism of complexes $f:A_\bullet\to B_\bullet$ the **mapping cone** $\operatorname{Cone}(f)$ is the complex with $(\operatorname{Cone}f)_n=B_n\oplus A_{n-1}$ and differential

$$
d(b,a)=(d_B b+f(a),-d_A a).
$$

It satisfies $d^2=0$ because $f$ is a chain map.

**Proposition.** There is a long exact sequence

$$
\cdots\to H_n(A)\xrightarrow{H_n(f)}H_n(B)\to H_n(\operatorname{Cone}f)\xrightarrow{}H_{n-1}(A)\to\cdots,
$$

so the homology of the cone is the obstruction to $f$ being a quasi-isomorphism, where a **quasi-isomorphism** is a chain map inducing isomorphisms on all homology groups.

*Proof.* The cone fits into a short exact sequence of complexes $0\to B_\bullet\to\operatorname{Cone}(f)\to A_{\bullet-1}\to0$ by the inclusions $b\mapsto(b,0)$ and the projections $(b,a)\mapsto a$, where $A_{\bullet-1}$ denotes $A$ with degrees shifted by one. The long exact sequence of the theorem, with the identification $H_n(A_{\bullet-1})=H_{n-1}(A)$, is the displayed sequence. $\square$

## Chain Homotopy

### Definition and First Properties

**Definition.** Let $f,g:C_\bullet\to D_\bullet$ be morphisms of complexes. A **chain homotopy** $s:f\simeq g$ is a family of morphisms $s_n:C_n\to D_{n+1}$ with

$$
g_n-f_n = e_{n+1}s_n + s_{n-1}d_n
$$

for every $n$. Two maps are **homotopic** if such an $s$ exists, and a map is a **homotopy equivalence** if it has an inverse up to homotopy.

**Proposition.** Homotopic chain maps induce the same map on homology.

*Proof.* Let $z \in Z_n(C)$, so $d_nz=0$. Then $g_n(z)-f_n(z)=e_{n+1}s_n(z)$, which lies in $B_n(D)=\operatorname{im}e_{n+1}$. Hence $g_n$ and $f_n$ agree on cycles modulo boundaries, that is, $H_n(f)=H_n(g)$. $\square$

**Corollary.** A homotopy equivalence is a quasi-isomorphism. The converse fails: the acyclic complex

$$
0\longrightarrow \mathbb{Z} \xrightarrow{\ \cdot 2\ } \mathbb{Z} \xrightarrow{\ \pi\ } \mathbb{Z}/2\mathbb{Z} \longrightarrow 0,
$$

concentrated in degrees $2,1,0$, has all homology zero, so its map to the zero complex is a quasi-isomorphism; but a contraction of the complex would provide a section of the surjection $\mathbb{Z}\to\mathbb{Z}/2\mathbb{Z}$, and none exists. Over a field every acyclic complex is contractible, so the distinction is a phenomenon of the general ring.

### Split Exact Sequences

**Definition.** A short exact sequence $0\to A\xrightarrow{f}B\xrightarrow{g}C\to0$ of complexes **splits** if it splits degreewise, that is, if there are morphisms $B_n\to A_n$ with composite the identity on $A_n$.

**Proposition.** If a short exact sequence of complexes splits degreewise then the connecting morphism $\partial_n$ vanishes and the long exact sequence breaks into short exact sequences $0\to H_n(A)\to H_n(B)\to H_n(C)\to0$.

*Proof.* With a degreewise retraction $r$, the element $a$ constructed in the snake argument can be taken to be a boundary, since $d_nb=f_{n-1}(a)$ and $r_n d_n b=d_{n-1}r nb$ lies in $B_{n-1}(A)$; hence $\partial_n=0$. Exactness of the remaining pieces is then the statement that the long exact sequence splits into short exact sequences at the points where $\partial$ is zero. $\square$

## Resolutions

### Projective and Injective Resolutions

**Definition.** A **left resolution** of an object $M$ of $\mathcal{A}$ is an exact sequence

$$
\cdots \longrightarrow P_2 \xrightarrow{d_2} P_1 \xrightarrow{d_1} P_0 \xrightarrow{\varepsilon} M \longrightarrow 0,
$$

written $P_\bullet\to M$, where $\varepsilon$ is the **augmentation**. It is a **projective resolution** if every $P_n$ is projective, a **free resolution** if every $P_n$ is free, and of **finite length** if $P_n=0$ for all large $n$. A **right resolution** is a cochain complex

$$
0\longrightarrow M\xrightarrow{\eta} I^0\xrightarrow{d^0} I^1\xrightarrow{d^1}\cdots,
$$

an **injective resolution** if every $I^n$ is injective.

**Examples.** Over a principal ideal domain every module has a free resolution of length one, $0\to K\to F\to M\to0$ with $F$ free, because submodules of free modules are free. Over $R=k[x_1,\dots,x_n]$ the module $k=R/(x_1,\dots,x_n)$ has the Koszul resolution of length $n$. Every module over every ring has a free, hence projective, resolution, by the article *Projective and Injective Modules*, and every module over every ring embeds in an injective module, so injective resolutions exist; in a Grothendieck category the latter holds by the theorem of *Abelian and Grothendieck Categories*.

### The Comparison Theorem

The reason resolutions are computable is that they are unique up to homotopy, so any two choices give the same answer.

**Theorem (comparison).** Let $P_\bullet\xrightarrow{\varepsilon}M$ be a projective resolution and $Q_\bullet\xrightarrow{\eta}N$ an exact sequence with $Q_n$ projective. Every morphism $u:M\to N$ lifts to a morphism of complexes $\varphi:P_\bullet\to Q_\bullet$ with $\eta\varphi_0=u\varepsilon$, and any two such lifts are chain homotopic.

*Proof.* Since $Q_0\to N$ is surjective and $P_0$ is projective, the map $u\varepsilon:P_0\to N$ lifts to $\varphi_0:P_0\to Q_0$. Suppose $\varphi_{n-1}$ has been constructed. The composite $d^Q_{n-1}\varphi_{n-1}:P_n\to Q_{n-1}$ has image in $\ker(Q_{n-1}\to Q_{n-2})=\operatorname{im}(Q_n\to Q_{n-1})$ by exactness and the commuting relation already established; since $P_n$ is projective, it lifts along the surjection $Q_n\to\operatorname{im}(Q_n\to Q_{n-1})$ to $\varphi_n$. This produces the chain map. For the uniqueness up to homotopy, given two lifts $\varphi,\psi$, the differences $\varphi_n-\psi_n$ satisfy $(\varphi_0-\psi_0)\varepsilon=0$, so $\varphi_0-\psi_0$ lands in $\operatorname{im}(Q_1\to Q_0)$; the projectivity of $P_0$ gives $s_0:P_0\to Q_1$ with $d^Q_1s_0=\varphi_0-\psi_0$. Then $\varphi_1-\psi_1-s_0d^P_1$ has image killed by $d^Q_1$, hence lands in $\operatorname{im}(Q_2\to Q_1)$, and projectivity of $P_1$ gives $s_1$; the induction produces the homotopy. $\square$

**Corollary.** Any two projective resolutions of $M$ are homotopy equivalent, and hence their homologies are isomorphic; the same holds for injective resolutions by the dual argument.

**Corollary.** The identity of $M$ lifts to a chain map between any two projective resolutions, unique up to homotopy. Therefore any construction applied to a projective resolution and invariant under chain homotopy is an invariant of $M$. This is the invariance that the derived functors use.

### The Horseshoe Lemma

When a module is an extension of two others, resolutions of the two ends assemble into a resolution of the middle.

**Lemma (horseshoe).** Let $0\to A\to B\to C\to0$ be a short exact sequence and let $P_\bullet\to A$, $R_\bullet\to C$ be projective resolutions. Then there is a projective resolution $Q_\bullet\to B$ with $Q_n=P_n\oplus R_n$, and a short exact sequence of complexes $0\to P_\bullet\to Q_\bullet\to R_\bullet\to0$ whose degreewise splittings are the direct-sum projections.

*Proof.* Put $Q_0=P_0\oplus R_0$, mapped to $B$ by the sum of the augmentation of $P_0$ and a lift of the augmentation of $R_0$ along $B\to C$; the lift exists by projectivity of $R_0$. The map is surjective because $P_0\to A\to B$ and $R_0\to C$ jointly cover $B$, and its kernel is an extension of $\ker(R_0\to C)$ by $\ker(P_0\to A)$, on which the induction repeats. The resulting complex is exact by construction, and each $Q_n$ is projective as a direct sum of projectives. $\square$

**Corollary.** Every short exact sequence $0\to A\to B\to C\to0$ with $A$ and $C$ admitting finite projective resolutions of lengths at most $m$ and $n$ has $B$ admitting a finite projective resolution of length at most $\max(m,n)$.

## The Tensor Product and Hom Complexes

### The Tensor Product of Complexes

**Definition.** For complexes $C_\bullet,D_\bullet$ of modules over a commutative ring the **tensor product complex** has

$$
(C\otimes_RD)_n=\bigoplus_{p+q=n}C_p\otimes_RD_q, \qquad d(x\otimes y)=d_Cx\otimes y+(-1)^px\otimes d_Dy \ \text{ for } x \in C_p .
$$

**Proposition.** The differential is square-zero and the construction is associative and commutative up to the usual natural isomorphisms of the tensor product, with the Koszul sign $(-1)^p$ inserted to make the differential commute with the symmetry.

*Proof.* Apply the differential twice: the terms $d_C^2\otimes\operatorname{id}$ and $\operatorname{id}\otimes d_D^2$ vanish, and the two mixed terms $d_C\otimes d_D$ occur with signs $(-1)^p$ and $(-1)^{p-1}$ from the two orderings, so they cancel. $\square$

The tensor product complex is the input to the definition of $\operatorname{Tor}$ , and to the Künneth formula, and its homology is computed by the spectral sequences .

### The Hom Complex

**Definition.** For complexes $C_\bullet,D_\bullet$ the **hom complex** has

$$
\operatorname{Hom}^n(C,D)=\prod_{p \in \mathbb{Z}}\operatorname{Hom}(C_p,D_{p+n}),
$$

an element of which is a family $f=(f_p)_p$ of morphisms $f_p:C_p\to D_{p+n}$, with differential

$$
(df)_p = d^D_{p+n} f_p - (-1)^n f_{p-1} d^C_p .
$$

The differential is square-zero because $f_p$ is compared with $f_{p-1}$ through the differentials of $C$ and $D$, and the sign $(-1)^n$ makes the two orderings cancel.

**Proposition.** The **cycles** of the hom complex in degree $0$ are exactly the chain maps $C\to D$, and the **homology** $H^0(\operatorname{Hom}(C,D))$ is the group of chain maps modulo chain homotopy. More generally $H^n(\operatorname{Hom}(C,D))$ is the group of maps of degree $n$ modulo homotopy.

*Proof.* For $n=0$ the differential is $(df)_p=d^D_p f_p - f_{p-1}d^C_p$, and $df=0$ is exactly the chain-map condition. An element $f$ of degree $0$ with $df=0$ is a boundary precisely when there is a family $s=(s_p)$ with $s_p:C_p\to D_{p+1}$ and $f_p=d^D_{p+1}s_p+s_{p-1}d^C_p$, which is the definition of a chain homotopy from $0$ to $f$. The general degree is the same computation with the shift. $\square$

**Proposition.** If $C$ is a bounded-below complex of projective objects and $D$ is exact, then $\operatorname{Hom}^\bullet(C,D)$ is exact; in particular the homology in every degree vanishes. Dually, if $D$ is bounded-above and consists of injectives and $C$ is exact then $\operatorname{Hom}^\bullet(C,D)$ is exact.

*Proof.* The argument is the comparison theorem in degree one at a time: given a family $g$ with $dg=0$ and a partial lift $s$ defined in degrees below $p$, exactness of $D$ exhibits each $g_p - s_{p-1}d^C_p$ as factoring through the surjection $D_{p+n+1}\to\ker(d^D_{p+n})$, and projectivity of $C_p$ lifts it to $s_p$. The induction over the bounded-below degrees produces the required homotopy. $\square$

These statements are the homological form of the comparison theorem, and they are the reason the derived category, can be described by localising the homotopy category at the quasi-isomorphisms.

## Bicomplexes and Total Complexes

### Double Complexes

**Definition.** A **bicomplex** or **double complex** $C_{\bullet\bullet}$ is a family of objects $C_{p,q}$ with two commuting families of differentials $d^h_{p,q}:C_{p,q}\to C_{p-1,q}$ and $d^v_{p,q}:C_{p,q}\to C_{p,q-1}$ satisfying $(d^h)^2=0$, $(d^v)^2=0$ and $d^hd^v+d^vd^h=0$. The **total complex** $\operatorname{Tot}(C)_n=\bigoplus_{p+q=n}C_{p,q}$ carries the differential $d=d^h+d^v$, and $d^2=0$ is the anticommutation.

**Example.** For complexes $C_\bullet,D_\bullet$ the tensor product bicomplex with $C_{p,q}=C_p\otimes_RD_q$, horizontal differential $d_C\otimes\operatorname{id}$ and vertical $\operatorname{id}\otimes d_D$, has total complex the tensor product complex $(C\otimes_RD)_n$ above, with the Koszul sign carried into the vertical differential so that the anticommutation holds.

### Filtration and Computation

**Definition.** A **filtration** of a complex $C_\bullet$ is an increasing family of subcomplexes $\cdots\subseteq F_{p-1}C\subseteq F_pC\subseteq\cdots$ with union $C$ and intersection $0$ in each degree. A filtration is **bounded** if for each $n$ only finitely many $F_pC_n$ are nonzero.

The homology of a filtered complex is computed from the homologies of the successive quotients by the spectral sequences of: a filtration of a complex produces a spectral sequence converging to the homology of the complex with $E^1$-page the homology of the quotients. That article develops the construction; here only the definitions of bicomplex, total complex and filtration are recorded, since they are the input to the spectral-sequence machinery and to the derived-category constructions.

## Where the Applications Belong

The theory above is algebraic: it concerns an abelian category, complexes in it, and the homology functor. Two of its most important applications lie outside this Part by the ordering rules of the corpus.

The first is **sheaf cohomology**. For a sheaf of abelian groups on a site, or on a topological space, the global-section functor is left exact, and its derived functors — the cohomology of the sheaf — are computed from an injective resolution in the Grothendieck category of sheaves. The algebraic input is exactly the abelian-category theory of this article and the derived-functor theory of the next; the geometric input, which is a space or a site with a topology, belongs to Part II, where it is treated in *Sheaves and Cohomology*.

The second is **algebraic topology**. For a topological space, or a simplicial set, the singular chain complex computes the homology of the space, and the long exact sequence of a pair or a fibration is the long exact sequence of a short exact sequence of complexes; the algebraic machinery is the present article, while the space, its topology and the homotopy invariants built from it belong to Part II, where they are treated in *Algebraic Topology*. The same holds for the Hochschild and cyclic complexes: they are algebraic complexes, and they are developed later in this category.

## Summary

A chain complex is a graded object with a square-zero differential; its cycles, boundaries and homology $H_n=\ker d_n/\operatorname{im}d_{n+1}$ measure its failure to be exact, and homology is an additive functor. A short exact sequence of complexes yields, through the snake lemma applied to the differential squares, a long exact sequence in homology with a natural connecting morphism; the mapping cone packages the connecting morphism as the homology of a single complex and detects quasi-isomorphisms. Chain homotopic maps induce the same map on homology, and homotopy equivalence implies quasi-isomorphism, though not conversely.

A projective resolution of $M$ is an exact complex of projective modules with augmentation onto $M$, and an injective resolution is the dual. Every module has both. The comparison theorem produces a lift of any morphism of the resolved objects to a morphism of resolutions, unique up to chain homotopy; consequently any two projective resolutions of $M$ are homotopy equivalent, and constructions invariant under homotopy are invariants of $M$. The horseshoe lemma assembles resolutions of the ends of a short exact sequence into a resolution of the middle. The tensor product of complexes, with the Koszul sign, and the hom complex, whose $H^0$ is chain maps modulo homotopy, are the two constructions on complexes that the derived functors and the derived category use; double complexes, their total complexes and filtrations are the input to spectral sequences.

Every result is algebraic. The applications to sheaf cohomology and to algebraic topology require a space or a site and belong to Part II, where they are developed in *Sheaves and Cohomology* and *Algebraic Topology*; the algebraic complexes of Hochschild and cyclic homology lie outside this article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{A}$, $\mathbf{Ch}(\mathcal{A})$ | an abelian category, its category of chain complexes |
| $(C_\bullet,d_\bullet)$, $d_n:C_n\to C_{n-1}$ | chain complex and differentials, $d^2=0$ |
| $(C^\bullet,d^\bullet)$, $d^n:C^n\to C^{n+1}$ | cochain complex and differentials |
| $Z_n=\ker d_n$, $B_n=\operatorname{im}d_{n+1}$ | cycles and boundaries |
| $H_n(C)=Z_n/B_n$ | homology; $H^n$ for cohomology |
| $f_\bullet:C_\bullet\to D_\bullet$ | morphism of complexes |
| $\varphi\simeq\psi$, $s$ | chain homotopy and the homotopy $s_n:C_n\to D_{n+1}$ |
| $\operatorname{Cone}(f)$ | mapping cone of a chain map |
| $P_\bullet\to M$, $M\to I^\bullet$ | projective and injective resolutions |
| $\varepsilon$, $\eta$ | augmentation of a resolution |
| $(C\otimes_RD)_\bullet$, $\operatorname{Hom}^\bullet(C,D)$ | tensor product and hom complexes |
| $\operatorname{Tot}(C)$ | total complex of a bicomplex |
| $F_pC$ | filtration of a complex |
| $R$ | commutative ring with identity $1\neq0$ unless stated |









## Further Reading

- Henri Cartan and Samuel Eilenberg, *Homological Algebra* (Princeton University Press, 1956), for chain complexes, resolutions and the comparison theorem.
- Pierre Gabriel, "Des catégories abéliennes", *Bulletin de la Société Mathématique de France* 90 (1962), 323–448, for complexes and resolutions in an abelian category.
- Alexander Grothendieck, "Sur quelques points d'algèbre homologique", *Tohoku Mathematical Journal* 9 (1957), 119–221, for the homological algebra of abelian categories and the long exact sequence.
- Thomas W. Hungerford, *Algebra* (Springer, 1974), for the elementary theory of complexes and resolutions.
- Saunders Mac Lane, *Homology* (Springer, 1995), for chain complexes, homotopy and the comparison theorem.
- Barry Mitchell, "The full imbedding theorem", *American Journal of Mathematics* 86 (1964), 619–637, for the categorical formulation of the diagram lemmas.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, 2nd ed. 2009), for resolutions, the horseshoe lemma and the derived functors.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for complexes, the comparison theorem and the tensor and hom complexes.
