
# __Sheaves in Algebraic Geometry__

## Introduction

Algebraic geometry replaces the open sets of a manifold by a coarser and more rigid topology — the Zariski topology, in which the closed sets are the zero sets of ideals — and compensates for the poverty of the open sets by carrying a rich structure sheaf. On an affine scheme there are few open sets and no interesting locally constant sheaves, but there are as many sheaves of modules as there are modules over the coordinate ring, and the sheaf-theoretic operations reproduce the algebra exactly: kernels, cokernels, tensor products and homomorphisms of sheaves of modules over the structure sheaf correspond to the same operations on modules over the ring. This article develops the sheaf theory of an affine and a projective scheme, states the theorems that make it computable — the vanishing of the higher cohomology of a quasi-coherent sheaf on an affine scheme, the computation of the cohomology of the twisting sheaves on projective space, the finiteness theorem and Serre duality — and records how the results of the previous articles of this category are transported to the algebraic setting.

The order of the corpus requires that the objects be introduced here as far as they are needed. An **affine scheme** is the set $\operatorname{Spec} A$ of prime ideals of a commutative ring $A$ with the Zariski topology, equipped with the **structure sheaf** $\mathcal{O}_X$ whose sections over the distinguished open set $D(f)$, $f\in A$, are the localisation $A_f$, and a **projective scheme** $\operatorname{Proj} S$ is constructed from a graded ring $S$ in the same manner with the homogeneous ideals. Both constructions are stated here as standard mathematics, with their categorical and functorial properties, because the general theory of schemes and their morphisms belongs, written in this same batch, and the systematic theory of coherent and quasi-coherent sheaves, also written in this batch. What is developed here is the sheaf-cohomological content: the equivalence between modules and quasi-coherent sheaves, the vanishing and finiteness theorems, the explicit computations, the sheaf of Kähler differentials with the de Rham complex it generates, and duality.

There are two structural differences from the topological theory of articles 16–20, and both are stated at the outset. First, the Zariski topology is far from locally acyclic: the constant sheaf $\underline{\mathbb{Z}}$ on a complex algebraic variety has a cohomology that is *not* the singular cohomology, and the comparison of algebraic with topological or analytic cohomology requires a finer topology than the Zariski one. Second, the sheaves that occur are quasi-coherent rather than locally constant, and the functor of global sections is *exact* on the quasi-coherent sheaves over an affine scheme, so that the higher cohomology vanishes and all the interest passes to the projective case, where the sheaves $\mathcal{O}(d)$ replace the constant sheaf as the simplest coefficients and their cohomology is computed by a Čech complex of a finite cover whose terms are localisations. The computational engine is the Čech cohomology of *Čech Cohomology*, which on the covers used here coincides with the sheaf cohomology by the Leray theorem because the distinguished open sets and their intersections are acyclic for quasi-coherent sheaves.

Throughout, $A$ is a commutative ring with identity, $X = \operatorname{Spec} A$, $S$ is a graded ring positively graded over $S_0 = A$, and $\mathbb{P}^n_A = \operatorname{Proj} A[x_0,\ldots,x_n]$. The Zariski topology, the localisation $A_f$, the ideals of $A$ and the modules over it are those of Part I's *Localization and the Fraction Field*, *Ideals and Quotients of Algebras*, *Rings*, *Polynomial Algebras* and *Module Categories*; the sheaf theory is that of articles 16–20; the algebra of a graded ring and of the Hilbert polynomial of a graded module is standard and is quoted where used, with the references given at the end.

## The Zariski Topology and the Structure Sheaf

**Definition.** Let $A$ be a commutative ring with identity. The **spectrum** $\operatorname{Spec} A$ is the set of prime ideals of $A$; for an ideal $\mathfrak{a}\subseteq A$ one writes

$$
V(\mathfrak{a}) = \{\mathfrak{p}\in\operatorname{Spec} A : \mathfrak{a}\subseteq\mathfrak{p}\},
$$

and the **Zariski topology** on $\operatorname{Spec} A$ is the topology whose closed sets are the $V(\mathfrak{a})$. For $f\in A$ the **distinguished open set** is

$$
D(f) = \{\mathfrak{p} : f\notin\mathfrak{p}\} = \operatorname{Spec} A\setminus V(fA), \qquad D(f)\cap D(g) = D(fg),
$$

and the distinguished open sets form a basis of the topology closed under finite intersections.

**Theorem (the structure sheaf).** There is a unique sheaf of commutative rings $\mathcal{O}_X$ on $X = \operatorname{Spec} A$ with

$$
\mathcal{O}_X(D(f)) = A_f, \qquad f\in A,
$$

the localisation of $A$ in the multiplicative set $\{1,f,f^2,\ldots\}$, the restriction $A_f\to A_{fg}$ being the localisation map; its stalks are the local rings

$$
\mathcal{O}_{X,\mathfrak{p}} = A_{\mathfrak{p}}, \qquad \mathfrak{p}\in X,
$$

and $(X,\mathcal{O}_X)$ is a locally ringed space in the sense of *Presheaves and Sheaves*.

*Proof.* The distinguished opens form a basis closed under finite intersections, and $A_f$ is a functor of $f$ in the sense that $A_f\to A_{fg}$ is defined for every $g$ and the maps are compatible; by the theorem on sheaves on a basis of *Presheaves and Sheaves* it suffices to verify the sheaf condition for covers of $D(f)$ by distinguished opens, which reduces to the exactness of the sequence

$$
0 \to A_f \to \prod_i A_{f_i} \to \prod_{i,j}A_{f_if_j}
$$

for a family $f_i$ with $(f_i) = (f)$ in $A_f$, a standard consequence of the characterisation of the localisation as a filtered colimit and of the finite character of the ideal generated by the $f_i$. The stalk at $\mathfrak{p}$ is the colimit of the $A_f$ over the $f$ not in $\mathfrak{p}$, which is $A_{\mathfrak{p}}$; the maximal ideal of $A_{\mathfrak{p}}$ is $\mathfrak{p}A_{\mathfrak{p}}$, so the ringed space is locally ringed. $\square$

**Example (the classical varieties).** If $A = k[x_1,\ldots,x_n]$ with $k$ algebraically closed, the maximal ideals of $A$ are the points of affine $n$-space and the closed points of $\operatorname{Spec} A$ are the points of the affine variety defined by any ideal $\mathfrak{a}$, with the structure sheaf restricting to the sheaf of regular functions on the variety; if $A$ is a finitely generated reduced $k$-algebra, the closed points of $\operatorname{Spec} A$ with their Zariski topology are the points of an affine variety over $k$ and $A$ is its coordinate ring, the dictionary between the two descriptions being the Nullstellensatz. The affine and projective varieties, their morphisms and their rational maps are the subject, written in this same batch; the graded case and the projective schemes are.

**Definition.** A **morphism** of affine schemes $f: \operatorname{Spec} B\to\operatorname{Spec} A$ is a morphism of locally ringed spaces; it is equivalently given by a ring homomorphism $\varphi: A\to B$, the map on points being $\mathfrak{q}\mapsto\varphi^{-1}(\mathfrak{q})$ and the map on structure sheaves being induced by the localisation maps $A_f\to B_{\varphi(f)}$. This contravariant equivalence — equivalently, the functor $\operatorname{Hom}_{\mathbf{Ring}}(A,B)\cong\operatorname{Hom}(\operatorname{Spec} B,\operatorname{Spec} A)$ — is the categorical content of the construction and is developed.

## Modules and Quasi-Coherent Sheaves

**Definition.** An $\mathcal{O}_X$-**module** on a locally ringed space $X$ is a sheaf $\mathcal{F}$ of abelian groups with a multiplication $\mathcal{O}_X(U)\times\mathcal{F}(U)\to\mathcal{F}(U)$ for every open $U$, compatible with restriction and making $\mathcal{F}(U)$ a module over the ring $\mathcal{O}_X(U)$. A morphism of $\mathcal{O}_X$-modules is a morphism of sheaves respecting the multiplication; the category $\mathcal{O}_X\text{-}\mathbf{Mod}$ is abelian by *Presheaves and Sheaves*, and the tensor product $\mathcal{F}\otimes_{\mathcal{O}_X}\mathcal{G}$ and the sheaf hom $\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F},\mathcal{G})$ are defined by sheafification.

**Definition.** Let $X = \operatorname{Spec} A$. For an $A$-module $M$ define the sheaf $\widetilde{M}$ on $X$ by the prescription

$$
\widetilde M(D(f)) = M_f = M\otimes_A A_f, \qquad f\in A,
$$

with the evident restriction maps; the sheaf axioms hold by the same exactness used for the structure sheaf. The construction is functorial in $M$ and exact: the localisation functor $M\mapsto M_f$ is exact, the direct sums and products in the definition commute with the kernels and cokernels of the localisations, and a sequence of $A$-modules is exact if and only if it is exact after localising at every $f$. A sheaf of $\mathcal{O}_X$-modules is **quasi-coherent** if it is isomorphic to some $\widetilde M$, and **coherent** if in addition $M$ is finitely generated — for a Noetherian $A$ this agrees with the usual notion of a coherent sheaf of finite type.

**Theorem (modules and quasi-coherent sheaves).** For $X = \operatorname{Spec} A$ the functor $M\mapsto\widetilde M$ is an equivalence of categories

$$
\mathbf{Mod}(A)\ \xrightarrow{\ \sim\ }\ \mathbf{QCoh}(X), \qquad M\mapsto\widetilde M, \qquad \mathcal{F}\mapsto\Gamma(X,\mathcal{F}),
$$

with quasi-inverse the global sections functor. The equivalence commutes with kernels, cokernels, images and finite direct sums, with the tensor product, with the sheaf hom, and with the localisation $A\to A_f$ in the sense that $\widetilde M|_{D(f)} = \widetilde{M_f}$ on $\operatorname{Spec} A_f$.

*Proof.* The global sections of $\widetilde M$ recover $M$: $\Gamma(X,\widetilde M)$ is the equaliser of the maps $\prod_i M_{f_i}\to\prod_{i,j}M_{f_if_j}$ for any family generating the unit ideal, and this equaliser is $M$ by the same exactness used above. The functor is fully faithful because a morphism $\widetilde M\to\widetilde N$ is determined by its global sections and every $A$-linear map $M\to N$ induces one; it is essentially surjective by the definition of quasi-coherence. The remaining statements are the commutation of the localisation with the respective operations, which is Part I's *Localization and Completion of Modules*. $\square$

**Corollary (exactness of global sections on an affine scheme).** The functor $\Gamma(X,-)$ is exact on quasi-coherent sheaves: if

$$
0 \to \mathcal{F}'\to\mathcal{F}\to\mathcal{F}''\to 0
$$

is a short exact sequence of quasi-coherent sheaves on $X = \operatorname{Spec} A$, then $0\to\Gamma(X,\mathcal{F}')\to\Gamma(X,\mathcal{F})\to\Gamma(X,\mathcal{F}'')\to 0$ is exact, and indeed the original sequence is exact if and only if its sequence of global sections is. Consequently

$$
H^i(X,\mathcal{F}) = 0 \qquad \text{for } i > 0
$$

for every quasi-coherent $\mathcal{F}$ on an affine scheme $X$.

*Proof.* The equivalence of categories carries the short exact sequence to a short exact sequence of $A$-modules $0\to M'\to M\to M''\to 0$ and the functor $\Gamma$ to $M\mapsto M$, which is exact; for the vanishing, apply the long exact sequence of *Sheaf Cohomology*: the cohomology of a quasi-coherent sheaf can be computed on the open affine pieces of a cover by distinguished opens, and by the exactness just proved the Čech complex of such a cover is exact in positive degree, so the Čech cohomology vanishes and by the Leray theorem of *Čech Cohomology* so does the sheaf cohomology. $\square$

**Theorem (coherence).** Let $A$ be Noetherian and $X = \operatorname{Spec} A$. The coherent sheaves on $X$ form an abelian subcategory of $\mathbf{QCoh}(X)$ closed under kernels, cokernels, extensions, tensor products and $\mathcal{H}om$; it corresponds under the equivalence to the finitely generated $A$-modules, and for a closed subscheme $Z\subseteq X$ the direct image $i_*$ of a coherent sheaf on $Z$ is coherent on $X$, while $i_*$ of a quasi-coherent sheaf is quasi-coherent.

*Proof.* The equivalence of categories preserves the abelian structure, so the closedness properties reduce to the corresponding properties of finitely generated modules over a Noetherian ring; the last statement is that $i_*$ corresponds to the restriction of scalars $A\to A/\mathfrak{a}$ along a surjection, which preserves finite generation. $\square$

## Coherent Sheaves on a Projective Scheme

**Definition.** Let $S = \bigoplus_{d\geq0}S_d$ be a graded ring with $S_0 = A$ generated as an $A$-algebra by $S_1$. The **projective spectrum** $\operatorname{Proj} S$ is the set of homogeneous prime ideals $\mathfrak{p}$ with $\mathfrak{p}\not\supseteq S_+ = \bigoplus_{d>0}S_d$, with the Zariski topology generated by the sets $D_+(f) = \{\mathfrak{p} : f\notin\mathfrak{p}\}$ for homogeneous $f$, and with the structure sheaf $\mathcal{O}_X$ defined on the basis by

$$
\mathcal{O}_X(D_+(f)) = S_{(f)},
$$

the degree-zero part of the localisation $S_f$. The **twisting sheaves** are

$$
\mathcal{O}_X(d) = \widetilde{S(d)}, \qquad S(d)_m = S_{d+m},
$$

the sheaf associated with the graded $S$-module with degrees shifted by $d$; they satisfy $\mathcal{O}_X(d)\otimes_{\mathcal{O}_X}\mathcal{O}_X(e)\cong\mathcal{O}_X(d+e)$ and $\mathcal{O}_X(0) = \mathcal{O}_X$. For $S = A[x_0,\ldots,x_n]$ one writes $\mathbb{P}^n_A = \operatorname{Proj} S$; it is covered by the $n+1$ open affines $U_i = D_+(x_i)\cong\operatorname{Spec} A[x_0/x_i,\ldots,\widehat{x_i/x_i},\ldots]$, whose intersections are again affine, $U_{i_0\ldots i_p} = \operatorname{Spec} A[x_{j_0}/x_{i_0},\ldots]$, so the standard cover is a cover by affine schemes with affine intersections.

**Theorem (the cohomology of the twisting sheaves).** Let $A$ be a ring and let $\mathcal{O}(d)$ be the twisting sheaf on $\mathbb{P}^n_A$.

1. $H^0(\mathbb{P}^n_A,\mathcal{O}(d))$ is the degree-$d$ part $S_d$ of $S = A[x_0,\ldots,x_n]$, a free $A$-module of rank $\binom{d+n}{n}$ for $d\geq0$ and $0$ for $d<0$.
2. $H^i(\mathbb{P}^n_A,\mathcal{O}(d)) = 0$ for $0<i<n$ and every $d$.
3. $H^n(\mathbb{P}^n_A,\mathcal{O}(d)) = 0$ for $d\geq-n$, and for $d\leq-n-1$ it is a free $A$-module of rank $\binom{-d-1}{n}$, dual to $S_{-d-n-1}$.

*Proof sketch.* The standard cover $\{U_i\}$ has affine intersections, so $\mathcal{O}(d)$ is acyclic on every intersection — its higher cohomology there vanishes by the affine vanishing theorem — and by the Leray theorem of *Čech Cohomology* the cohomology of $\mathcal{O}(d)$ on $\mathbb{P}^n_A$ is the cohomology of the Čech complex

$$
\check C^p = \prod_{i_0<\cdots<i_p}\mathcal{O}(d)(U_{i_0\ldots i_p}) = \prod_{i_0<\cdots<i_p}\bigl(S(d)_{x_{i_0}\cdots x_{i_p}}\bigr)_0,
$$

whose terms are the degree-zero parts of localisations of the graded module $S(d)$. The computation is the standard one: an element of such a localisation is a finite sum of Laurent monomials in the $x_i$, each of total degree $d$, and the subcomplex spanned by a single monomial is the cochain complex of a simplex, hence acyclic except in one degree; summing over the monomials of degree $d$ gives the three statements, the ranks being the binomial coefficients that count the monomials of the relevant degrees. The case $n=1$ is carried out in full in the example below, and the general case is Hartshorne III.5.1. $\square$

**Example (the projective line, computed).** For $n=1$, $S = A[x_0,x_1]$, and the cover $\{U_0,U_1\}$ gives the two-term complex

$$
0 \to \mathcal{O}(d)(U_0)\oplus\mathcal{O}(d)(U_1) \xrightarrow{\ \delta\ } \mathcal{O}(d)(U_0\cap U_1) \to 0,
$$

with $\mathcal{O}(d)(U_0) = x_0^dA[t]$ for $t = x_1/x_0$, $\mathcal{O}(d)(U_1) = x_1^dA[t^{-1}]$, and $\delta(f x_0^d, g x_1^d) = (f - t^d g(t^{-1}))x_0^d$ in the common basis $x_0^d$ of $A[t,t^{-1}]$, using $x_1^d = t^dx_0^d$. Hence

$$
H^0 = \bigl\{(f,g) : f(t) = t^dg(t^{-1})\bigr\} = \Bigl\{\sum_{k=0}^{d}g_kt^{d-k} : d\geq0\Bigr\},
$$

of rank $d+1$ for $d\geq0$ and rank $0$ for $d<0$, and

$$
H^1 = A[t,t^{-1}]\big/\bigl(A[t] + t^dA[t^{-1}]\bigr),
$$

which is $0$ for $d\geq-1$ and has rank $-d-1$ for $d\leq-2$: the classes of the monomials $t^{k}$ with $d+1\leq k\leq-1$, which are exactly those missing from the image $A[t] + t^dA[t^{-1}]$. This is the case $n=1$ of the theorem, and it is the computation on which the Riemann–Roch theorem for curves, in Part I's *The Riemann–Roch Theorem for Curves*, rests. The Euler characteristic is $\chi(\mathcal{O}(d)) = (d+1) - 0 = d+1$ for $d\geq-1$ and $0 - (-d-1) = d+1$ for $d\leq-2$, so in this case it is the linear polynomial $d+1$ in every degree.

**Theorem (Serre's finiteness and vanishing).** Let $A$ be Noetherian, let $X$ be a projective scheme over $A$ of relative dimension $n$, and let $\mathcal{F}$ be a coherent sheaf on $X$.

1. Each $H^i(X,\mathcal{F})$ is a finitely generated $A$-module, and $H^i(X,\mathcal{F}) = 0$ for $i>n$.
2. **Serre's vanishing theorem**: there is an integer $d_0$ such that $H^i(X,\mathcal{F}(d)) = 0$ for all $i>0$ and all $d\geq d_0$.
3. The Euler characteristic $\chi(\mathcal{F}(d)) = \sum_i(-1)^i\operatorname{length}_AH^i(X,\mathcal{F}(d))$ is a polynomial in $d$ of degree at most $n$ for $d$ large, the **Hilbert polynomial** of $\mathcal{F}$.

*Proof sketch.* For (1) one uses the finite cover by the $U_i$ with affine intersections, the affine vanishing theorem and the fact that the Čech complex of a coherent sheaf with respect to a finite cover of a Noetherian scheme has finitely generated cohomology, being the cohomology of a complex of finitely generated modules; the vanishing above degree $n$ follows because the Čech complex of the standard cover has length $n$. For (2) one reduces to the twisting sheaves by a resolution of $\mathcal{F}$ by sums of $\mathcal{O}(d)$ — the existence of such resolutions is the content of the graded Hilbert syzygy theorem — and applies the computation of the cohomology of $\mathcal{O}(d)$ above. For (3) the vanishing of (2) makes the alternating sum the Euler characteristic of a finite complex of finitely generated modules whose Hilbert function is eventually polynomial, which is Part I's Hilbert polynomial for a graded module. $\square$

**Corollary (the cohomology of the structure sheaf).** For a projective scheme over a field $k$ one has $H^0(X,\mathcal{O}_X) = k$ when $X$ is connected and **geometrically connected**, that is, when $X\times_k\bar k$ is connected for an algebraic closure $\bar k$ of $k$; connectedness alone does not suffice, and neither does connectedness together with geometric reducedness, as $X = \operatorname{Spec}\mathbb{C}$ over $k = \mathbb{R}$ shows, where $H^0(X,\mathcal{O}_X) = \mathbb{C}$. In the general case $H^0(X,\mathcal{O}_X)$ is a finite-dimensional $k$-algebra of the form $\prod_i K_i$ with the $K_i$ finite field extensions of $k$, one for each connected component of $X\times_k\bar k$. The higher cohomology of the structure sheaf is the obstruction to the exactness of the global sections functor; for $\mathbb{P}^n_k$ the only nonvanishing groups of $\mathcal{O}_X$ are $H^0 = k$ and $H^n = k$, the projective-space analogue of the cohomology of the sphere. In particular the Zariski topology sees the dimension of the projective space, since the top cohomology of the structure sheaf is nonzero exactly in degree $n$.

## Kähler Differentials

**Definition.** Let $A$ be a commutative $k$-algebra and let $I = \ker(A\otimes_kA\to A)$ be the kernel of the multiplication. The **module of Kähler differentials** of $A$ over $k$ is $\Omega^1_{A/k} = I/I^2$, with the **universal derivation** $d : A\to\Omega^1_{A/k}$ given by $da = a\otimes1 - 1\otimes a$. The map $d$ is $k$-linear and satisfies the Leibniz rule $d(ab) = a\,db + b\,da$, and it is universal: every $k$-derivation $D : A\to M$ into an $A$-module factors uniquely as $D = \varphi\circ d$ with $\varphi : \Omega^1_{A/k}\to M$ $A$-linear. Equivalently, $\Omega^1_{A/k}$ is generated as an $A$-module by the symbols $da$, $a\in A$, subject to the relations $d(a+a') = da + da'$, $d(aa') = a\,da' + a'\,da$ and $dc = 0$ for $c\in k$. For $A = k[x_1,\dots,x_n]$ it is free with basis $dx_1,\dots,dx_n$, and for a localisation $A_g$ it is $\Omega^1_{A/k}\otimes_AA_g$. The module and its identification with the first Hochschild homology $HH_1(A,A)$ are Part I's, in *Hochschild Homology*.

**Definition.** Let $X$ be a scheme of finite type over $k$. The **sheaf of Kähler differentials** $\Omega^1_{X/k}$ is the quasi-coherent sheaf whose value on an affine open $\operatorname{Spec} A\subseteq X$ is the module $\Omega^1_{A/k}$ above, the universal derivations gluing over the intersections of an affine cover; its **exterior powers** are $\Omega^p_{X/k} = \Lambda^p_{\mathcal{O}_X}\Omega^1_{X/k}$, the sheaf of degree-$p$ differential forms, and $\Omega^1_{X/k}$ is coherent when $X$ is of finite type over a Noetherian $k$. The **algebraic de Rham complex** $\Omega^\bullet_{X/k}$ is

$$
\mathcal{O}_X\xrightarrow{\ d\ }\Omega^1_{X/k}\xrightarrow{\ d\ }\Omega^2_{X/k}\to\cdots ,
$$

with $d$ the $k$-linear extension of the universal derivation, characterised by $d(\omega\wedge\eta) = d\omega\wedge\eta + (-1)^{\deg\omega}\omega\wedge d\eta$ and $d^2 = 0$.

**Proposition (the cotangent space).** Let $P\in X$ and let $\mathfrak{m}_P\subseteq\mathcal{O}_{X,P}$ be the maximal ideal of the local ring at $P$. The fibre $\Omega^1_{X/k}\otimes_{\mathcal{O}_X}k(P)$ is the **cotangent space** at $P$, equal to $\mathfrak{m}_P/\mathfrak{m}_P^2$ when $P$ is a rational point, and it is the $k(P)$-dual of the tangent space $T_PX$; the pairing is the evaluation of the universal derivation along a derivation $\mathcal{O}_{X,P}\to k(P)$.

**Theorem (differentials and smoothness).** Let $X$ be of finite type over $k$ of relative dimension $n$ at $P\in X$. Then $X$ is smooth at $P$ if and only if $\Omega^1_{X/k}$ is locally free of rank $n$ in a neighbourhood of $P$; consequently, for $X$ smooth of relative dimension $n$ over $k$ the sheaf $\Omega^1_{X/k}$ is locally free of rank $n$, the sheaf $\Omega^p_{X/k}$ is locally free of rank $\binom np$, and the de Rham complex is a resolution of the constant sheaf $k$ in the analytic topology, though not in the Zariski one.

**Example (projective space).** For $X = \mathbb{P}^n_k$ the Euler sequence $0\to\Omega^1_{\mathbb{P}^n_k/k}\to\mathcal{O}(-1)^{n+1}\to\mathcal{O}\to0$ exhibits $\Omega^1_{X/k}$ as a locally free sheaf of rank $n$, and taking determinants gives the canonical sheaf $\omega_{\mathbb{P}^n_k} = \Omega^n_{X/k}\cong\mathcal{O}(-n-1)$, which is the computation underlying the cohomology of $\omega_X$ used in the duality below. For a smooth projective curve the sheaf $\Omega^1_{X/k}$ is the sheaf of regular differentials of *The Riemann–Roch Theorem for Curves*.

## Serre Duality

**Definition.** Let $X$ be a smooth projective scheme of relative dimension $n$ over a field $k$, with the sheaf of Kähler differentials $\Omega^1_{X/k}$ and its top exterior power $\Omega^n_{X/k}$ of the previous section; the **canonical sheaf** is

$$
\omega_X = \Lambda^n\Omega^1_{X/k} = \Omega^n_{X/k}.
$$

**Theorem (Serre duality).** Let $X$ be a smooth projective scheme of dimension $n$ over a field $k$, and let $\mathcal{F}$ be a coherent sheaf on $X$. There are natural isomorphisms

$$
H^i(X,\mathcal{F}) \cong H^{n-i}\bigl(X,\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F},\omega_X)\bigr)^{\vee},
$$

where ${}^{\vee}$ denotes the $k$-dual, and the top group is $H^n(X,\omega_X)\cong k$; equivalently, the pairing

$$
H^i(X,\mathcal{F})\times H^{n-i}(X,\mathcal{F}^{\vee}\otimes_{\mathcal{O}_X}\omega_X)\to H^n(X,\omega_X)\cong k
$$

induced by the cup product and the trace map is nondegenerate. When $\mathcal{F} = \mathcal{O}_X$ this reads $H^i(X,\mathcal{O}_X)\cong H^{n-i}(X,\omega_X)^{\vee}$.

*Proof sketch.* The statement is the $\operatorname{Ext}$-duality $H^i(X,\mathcal{F})^{\vee}\cong\operatorname{Ext}^{n-i}(\mathcal{F},\omega_X)$, whose proof resolves $\mathcal{F}$ by locally free sheaves of finite rank and uses that the functor $\mathcal{H}om(\mathcal{O}_X,\omega_X)\cong\omega_X$ is injective as a module over the structure sheaf, so that $\operatorname{Ext}^{n-i}(\mathcal{F},\omega_X)$ may be computed as $H^{n-i}(X,\mathcal{F}^{\vee}\otimes\omega_X)$; the nondegeneracy of the pairing is the statement that the resulting map $H^i(X,\mathcal{F})\to H^{n-i}(X,\mathcal{F}^{\vee}\otimes\omega_X)^{\vee}$ is an isomorphism, verified on locally free sheaves by reducing to the case of $\mathcal{O}_X(-d)$ on projective space, where it is the duality of the computation of the twisting sheaves. $\square$

**Corollary (duality on the projective line, and Riemann–Roch).** For $X = \mathbb{P}^1_k$, $\omega_X = \mathcal{O}(-2)$ and Serre duality reads $H^0(\mathbb{P}^1,\mathcal{O}(d))^{\vee}\cong H^1(\mathbb{P}^1,\mathcal{O}(-d-2))$; comparing the ranks $\binom{d+1}{1}$ and $\binom{-(-d-2)-1}{1} = d+1$, which agrees with the computation above, and the Euler characteristic

$$
\chi(\mathcal{O}(d)) = \dim H^0 - \dim H^1 = (d+1) - 0 = d+1 \quad (d\geq0)
$$

is the linear Hilbert polynomial of the projective line. For a smooth projective curve $C$ of genus $g$ Serre duality gives $\chi(\mathcal{F}) = \deg\mathcal{F} + \operatorname{rank}\mathcal{F}(1-g)$ for a locally free $\mathcal{F}$, which is the scheme-theoretic form of the Riemann–Roch theorem; the classical theorem for divisors on a curve, with its proof and its arithmetic applications, is Part I's *The Riemann–Roch Theorem for Curves* and *Algebraic Curves*, and the general Grothendieck–Riemann–Roch theorem requires the characteristic classes of *Fibre Bundles, Connections and Curvature* and the K-theory of *Higher Algebraic K-Theory*.

**Remark (duality as a form of Poincaré duality).** Serre duality is the algebraic counterpart of the Poincaré duality of *Poincaré Duality*: the canonical sheaf plays the role of the orientation sheaf, the top cohomology $H^n(X,\omega_X)\cong k$ the role of the fundamental class, and the cup product with the trace the role of the integration pairing. The uniform statement behind both is Verdier duality, recorded in *Derived Functors and Sheaf Cohomology*: for the structure map $f : X\to\operatorname{Spec} k$ the dualising complex is $f^!k = \omega_X[n]$, and the duality is the adjunction between $Rf_*$ and $f^!$. The manifold case with constant coefficients is the twisted duality of *Sheaf Cohomology*.

## The Comparison with the Topological Theory

**The constant sheaf is the wrong coefficient system.** The Zariski topology of an algebraic variety over $\mathbb{C}$ has very few open sets, and the functor $\Gamma$ of sections of the constant sheaf is far from identifying local and global data: a nonconstant algebraic function on an irreducible variety has no zeros and no poles on a nonempty Zariski open set, so the only locally constant sheaves on an irreducible scheme are constant, and the sheaf cohomology of $\underline{\mathbb{Z}}$ in the Zariski topology differs from the singular cohomology of the same variety. The comparison of algebraic with topological cohomology therefore requires a finer topology: the **étale topology**, whose sheaves and cohomology are Part I's *Sheaves on Sites* and *Descent Theory*, and the analytic topology, for which the comparison theorems of GAGA type require the analytic theory of Part III. What transfers directly from the topological theory is the cohomology of the *coherent* sheaves, which is computed by the Čech complexes of algebraic covers, and the de Rham-type comparisons: for a smooth scheme over a field of characteristic zero the **algebraic de Rham complex** $\Omega^\bullet_{X/k}$ of the Kähler differentials above is a complex of quasi-coherent sheaves whose hypercohomology in the sense of *Derived Functors and Sheaf Cohomology* is the algebraic de Rham cohomology, and the Poincaré lemma for it holds only in the étale or the formal setting — a strictly algebraic residue of the failure of the Zariski topology to be locally contractible.

**Direct and inverse images.** A morphism of schemes $f : X\to Y$ induces the adjoint pair $f^{-1}\dashv f_*$ on sheaves of modules with $f^* = f^{-1}\otimes_{f^{-1}\mathcal{O}_Y}\mathcal{O}_X$, exactly as in the topological case; for a quasi-coherent sheaf $\mathcal{F}$ on $Y$ the inverse image $f^*\mathcal{F}$ is quasi-coherent, and for $f$ affine the direct image $f_*\mathcal{F}$ of a quasi-coherent sheaf is quasi-coherent, its global sections over an affine open $\operatorname{Spec} B\subseteq Y$ being $\Gamma(X\times_Y\operatorname{Spec} B,\mathcal{F})$ regarded as a $B$-module. The higher direct images $R^qf_*$ are quasi-coherent for $f$ proper, which is the **finiteness theorem of Grothendieck** and the reason the cohomology of a proper morphism behaves like the cohomology of a fibration: the Leray spectral sequence of *Sheaf Cohomology* applies verbatim, and the base-change theorem for a proper morphism is the algebraic form of the continuity of the cohomology of the fibres recorded in *Derived Functors and Sheaf Cohomology*.

**Moduli.** The cohomology of coherent sheaves is the tool with which families of algebro-geometric objects are parametrised: the tangent space to a moduli problem at a point is the cohomology $H^0$ of the sheaf of infinitesimal automorphisms, the obstructions lie in $H^1$, and the deformation theory of Part I's *Deformation Theory* is the formal version of the same statement; the moduli of curves and of vector bundles, and the formation of quotients, are not covered here.

## Summary

An affine scheme is the spectrum of a commutative ring with the Zariski topology and the structure sheaf whose sections over a distinguished open set $D(f)$ are the localisation $A_f$; it is a locally ringed space whose stalks are the local rings $A_{\mathfrak{p}}$, and its ringed-space morphisms are contravariantly the ring homomorphisms. The sheaves of modules over the structure sheaf are governed by an equivalence of categories: a module $M$ over $A$ determines a quasi-coherent sheaf $\widetilde M$ with $\widetilde M(D(f)) = M_f$, and every quasi-coherent sheaf arises this way, with the global sections functor as quasi-inverse and with kernels, cokernels, tensor products and sheaf homs corresponding on the two sides. The immediate consequence is the exactness of global sections on an affine scheme and the **affine vanishing theorem**: the higher cohomology of every quasi-coherent sheaf on $\operatorname{Spec} A$ vanishes, so the interest passes to the projective case.

A projective scheme is built from a graded ring by the same construction with homogeneous ideals, and carries the twisting sheaves $\mathcal{O}(d)$; on projective space the standard cover by the open affines $U_i$ has affine intersections, so the Leray theorem reduces the computation of cohomology to a Čech complex of localisations, and an explicit monomial computation gives $H^0(\mathcal{O}(d)) = S_d$, the vanishing of the intermediate cohomology, and $H^n(\mathcal{O}(d))$ as the dual of $S_{-d-n-1}$; on the projective line the computation is carried out in full and recovers the ranks $d+1$ and $-d-1$. For a coherent sheaf on a projective scheme over a Noetherian ring the cohomology is finitely generated, vanishes above the relative dimension, and vanishes in positive degree after twisting by a large $\mathcal{O}(d)$, so that the Euler characteristic is eventually a polynomial. **Serre duality** identifies $H^i(X,\mathcal{F})$ with the dual of $H^{n-i}(X,\mathcal{F}^{\vee}\otimes\omega_X)$ for a smooth projective $X$ of dimension $n$, with $\omega_X$ the canonical sheaf, and is the algebraic counterpart of Poincaré duality and the curve case of the Riemann–Roch theorem; it is the degreewise shadow of Verdier duality. The differential forms on which the duality depends are the exterior powers of the sheaf of Kähler differentials $\Omega^1_{X/k}$, the quasi-coherent sheaf associated to the module $\Omega^1_{A/k} = I/I^2$ of Part I's *Hochschild Homology*: its fibre at a point is the cotangent space, dual to the tangent space, it is locally free of rank $n$ exactly when $X$ is smooth of relative dimension $n$, and the algebraic de Rham complex it generates computes the algebraic de Rham cohomology. The Zariski topology, finally, is too coarse for the constant sheaf, and the comparison of algebraic with topological cohomology requires the étale and the analytic topologies, while the coherent cohomology, the direct and inverse images, the finiteness theorem for proper morphisms and the deformation-theoretic uses of $H^0$ and $H^1$ pass directly to the algebraic setting and are the foundation of the theory of moduli.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Spec} A$ | spectrum of $A$: prime ideals with the Zariski topology |
| $V(\mathfrak{a})$, $D(f)$ | closed set of an ideal; distinguished open, $D(f)\cap D(g) = D(fg)$ |
| $\mathcal{O}_X$, $\mathcal{O}_X(D(f)) = A_f$ | structure sheaf; stalk $\mathcal{O}_{X,\mathfrak{p}} = A_{\mathfrak{p}}$ |
| $\mathbf{Mod}(A)$, $\mathbf{QCoh}(X)$, $\widetilde M$ | modules; quasi-coherent sheaves; the equivalence $M\mapsto\widetilde M$ |
| coherent | quasi-coherent with finitely generated module; abelian subcategory for Noetherian $A$ |
| $\operatorname{Proj} S$, $D_+(f)$, $S_{(f)}$ | projective spectrum; homogeneous distinguished open; degree-zero localisation |
| $\mathcal{O}_X(d)$ | twisting sheaf; $\mathcal{O}(d)\otimes\mathcal{O}(e)\cong\mathcal{O}(d+e)$ |
| $\mathbb{P}^n_A$, $U_i$ | projective space and its standard affine cover |
| $\bar k$ | an algebraic closure of the field $k$; geometric connectedness of $X$ means $X\times_k\bar k$ connected |
| $\omega_X = \Lambda^n\Omega^1_{X/k}$ | canonical sheaf; Serre duality $\mathcal{F}\leftrightarrow\mathcal{F}^{\vee}\otimes\omega_X$ |
| $\Omega^1_{A/k} = I/I^2$, $\Omega^1_{X/k}$ | module of Kähler differentials, $I=\ker(A\otimes_kA\to A)$, universal derivation $d$; the associated sheaf |
| $\Omega^p_{X/k} = \Lambda^p\Omega^1_{X/k}$ | sheaf of degree-$p$ differential forms; locally free of rank $\binom np$ for $X$ smooth of relative dimension $n$ |
| $T_PX$, $\mathfrak{m}_P/\mathfrak{m}_P^2$ | tangent space; cotangent space $\Omega^1_{X/k}\otimes_{\mathcal{O}_X}k(P)$, its dual |
| $\chi(\mathcal{F})$, Hilbert polynomial | alternating sum of lengths of cohomology; polynomial in $d$ for large $d$ |
| $\Omega^\bullet_{X/k}$ | algebraic de Rham complex; hypercohomology for smooth $X$ over a field |





## Further Reading

- Robin Hartshorne, *Algebraic Geometry* (Springer, 1977), for the structure sheaf of a scheme, quasi-coherent and coherent sheaves, the cohomology of the twisting sheaves, and Serre duality.
- Alexander Grothendieck and Jean Dieudonné, *Éléments de géométrie algébrique II, III, IV* (Publications Mathématiques de l'IHÉS, 1961–1967), for the foundational treatment of quasi-coherent sheaves, the finiteness and vanishing theorems and the duality.
- Jean-Pierre Serre, *Faisceaux algébriques cohérents* (Annals of Mathematics 61, 1955), for the original coherent-sheaf cohomology, the vanishing theorem and the duality.
- David Mumford, *The Red Book of Varieties and Schemes* (Springer, second edition, 1999), for the geometric intuition behind the spectrum and the structure sheaf.
- Robin Hartshorne, *Residues and Duality* (Springer, 1966), for the general Grothendieck duality of which Serre duality is the smooth projective case.
- Qing Liu, *Algebraic Geometry and Arithmetic Curves* (Oxford, 2002), for the systematic scheme-theoretic development with the algebraic applications.
