
# __Sheaves and the de Rham Complex__

## Introduction

The differential forms of a smooth manifold $M$, together with the exterior derivative, form a complex

$$
0 \to \Omega^0(M) \xrightarrow{\ d\ } \Omega^1(M) \xrightarrow{\ d\ } \Omega^2(M) \xrightarrow{\ d\ } \cdots \xrightarrow{\ d\ } \Omega^n(M) \to 0,
$$

with $n = \dim M$, whose cohomology $H^k_{dR}(M)$ is the de Rham cohomology of the written *Differential Forms and Stokes' Theorem*, where the forms, the exterior derivative, the identity $d^2 = 0$, the Poincaré lemma, the integration of top forms and Stokes' theorem are developed. That article also states the theorem of de Rham, $H^k_{dR}(M)\cong H^k(M;\mathbb{R})$, and its proof is sketched there by the Mayer–Vietoris comparison of the two theories. The present article gives the **sheaf-theoretic** account of the same theorem, which is not a second proof but a second organisation of it, and which is the reason the de Rham complex appears wherever sheaf cohomology is used. The object studied is not the complex of global forms but the **complex of sheaves** of forms, and the single local statement on which everything rests is the Poincaré lemma.

The argument has three steps. First, the presheaf assigning to an open set $U\subseteq M$ the forms $\Omega^k(U)$ is a sheaf $\Omega^k$ of $C^\infty$-modules, the exterior derivative is a morphism of sheaves $d : \Omega^k\to\Omega^{k+1}$ with $d^2 = 0$, and the complex of sheaves

$$
0 \to \underline{\mathbb{R}} \to \Omega^0 \xrightarrow{\ d\ } \Omega^1 \xrightarrow{\ d\ } \Omega^2 \to \cdots
$$

has $\underline{\mathbb{R}}$ in degree $0$: the kernel of $d$ on functions consists of the locally constant functions, which are exactly the constant sheaf. Second, the Poincaré lemma is precisely the statement that this complex is *exact*, because exactness of a sequence of sheaves is a local and stalkwise condition, and the stalk of $\Omega^k$ at $x$ is computed from the forms on the contractible open neighbourhoods of $x$. The de Rham complex is therefore a **resolution of the constant sheaf** $\underline{\mathbb{R}}$. Third, the sheaves $\Omega^k$ are fine — they are modules over the sheaf of smooth functions, which possesses partitions of unity — and fine sheaves are acyclic, so the resolution is an acyclic resolution and computes the cohomology of what it resolves:

$$
H^k_{dR}(M) \cong H^k(M,\underline{\mathbb{R}}) \cong H^k(M;\mathbb{R}).
$$

The first isomorphism is the sheaf-theoretic form of the theorem of de Rham in its version with local coefficients; the second is the comparison of sheaf and singular cohomology of *Sheaf Cohomology*. The article also records the two further structures that the de Rham complex carries: the wedge product, which turns it into a resolution by a sheaf of differential graded algebras and makes the isomorphism an isomorphism of graded rings, so that the wedge product of forms corresponds to the cup product; and the compactly supported variant, which computes cohomology with compact support and gives the integration pairing behind Poincaré duality.

The article cites the written *Differential Forms and Stokes' Theorem* for everything about forms themselves — the pullback, the exterior derivative and its characterisation, the Poincaré lemma, integration and Stokes' theorem, the Hodge star, the Laplace–de Rham operator and the harmonic representatives — and the written *Fibre Bundles, Connections and Curvature* for the curvature of a connection and for the Chern and Pontryagin forms, which are the de Rham representatives of the characteristic classes. Neither is restated. The abstract machinery is article 19's; the Čech comparison is article 18's. The complex-manifold refinement, in which the de Rham complex is replaced by the Dolbeault complex, belongs to the complex and Kähler geometry of *Hermitian Geometry and Almost Complex Structures* and *Kähler Geometry*.

## The Sheaf of Differential Forms

**Definition.** Let $M$ be a smooth manifold of dimension $n$. For $k \geq 0$ let $\Omega^k$ denote the **sheaf of differential $k$-forms** on $M$: its sections over an open set $U \subseteq M$ are the smooth $k$-forms on $U$ in the sense of the written *Differential Forms and Stokes' Theorem*, and its restriction maps are the restrictions of forms. The sheaf axioms hold because being a smooth form is a local condition on the coefficients in the charts of the manifold, and the global sections of $\Omega^k$ are the forms $\Omega^k(M)$ of that article; the notation

$$
\Gamma(M,\Omega^k) = \Omega^k(M)
$$

is used throughout, so that the sheaf $\Omega^k$ and the space of forms over $M$ are distinguished in print without changing the written article's symbol for the latter. One has $\Omega^0(U) = C^\infty(U)$, so that $\Omega^0$ is the sheaf of smooth functions, and $\Omega^k = 0$ for $k > n$ as sheaves, since the bundles vanish there.

**Theorem (the de Rham complex of sheaves).** The exterior derivative is a morphism of sheaves

$$
d : \Omega^k \to \Omega^{k+1}
$$

for each $k$, natural with respect to the restriction of forms to open subsets, satisfying $d\circ d = 0$. The sequence of sheaves

$$
0 \to \underline{\mathbb{R}} \to \Omega^0 \xrightarrow{\ d\ } \Omega^1 \xrightarrow{\ d\ } \Omega^2 \xrightarrow{\ d\ } \cdots \xrightarrow{\ d\ } \Omega^n \to 0
$$

is a complex of sheaves on $M$, whose differential is the exterior derivative and whose degree-zero map is the inclusion of the constant functions into the smooth functions.

*Proof.* The exterior derivative is defined locally, on the forms over each open set, and commutes with restriction: the pullback of $d\omega$ along the inclusion of an open subset is $d$ of the pullback of $\omega$, since the definition of $d$ in a chart involves only the partial derivatives of the coefficients of $\omega$ in that chart. Hence $d$ is a morphism of presheaves and, the target being a sheaf, a morphism of sheaves; $d^2 = 0$ is a local computation already performed in the written article. The constant functions are smooth and have zero derivative, and the map $\underline{\mathbb{R}}\to\Omega^0$ is injective as a map of sheaves because it is injective on sections over every connected open set. $\square$

**Theorem (the kernel of $d$ on functions).** The sequence

$$
0 \to \underline{\mathbb{R}} \to \Omega^0 \xrightarrow{\ d\ } \Omega^1
$$

is exact: the kernel of $d$ on smooth functions on a connected open subset is the constant functions.

*Proof.* A smooth function with vanishing exterior derivative has vanishing partial derivatives in every chart, hence is locally constant; on a connected open set it is constant, and the stalks of $\ker(d:\Omega^0\to\Omega^1)$ are therefore $\mathbb{R}$, since every point has connected open neighbourhoods. $\square$

**Remark (why the sheaf version is the right one).** The complex of global forms $\Omega^\bullet(M)$ is not exact in positive degree, and its cohomology is the whole point of the construction; the complex of sheaves, by contrast, is exact, as the next section shows. The passage from the false exactness of the global complex to the true exactness of the sheaf complex is exactly the passage measured by sheaf cohomology, and it is the reason cohomology is unavoidable in the statement of the de Rham theorem.

## The Poincaré Lemma as a Local Statement

**Theorem (Poincaré lemma).** Let $U\subseteq\mathbb{R}^n$ be a star-shaped open set, in particular an open ball. Then every closed form of positive degree on $U$ is exact: $H^k_{dR}(U) = 0$ for $k\geq 1$, and $H^0_{dR}(U) = \mathbb{R}$. This is the written article's Poincaré lemma, with its proof by the homotopy operator $h$ satisfying $dh + hd = \mathrm{id}$; it is quoted here and not reproved.

**Theorem (the de Rham complex is a resolution of the constant sheaf).** Let $M$ be a smooth manifold. The complex of sheaves

$$
0 \to \underline{\mathbb{R}} \to \Omega^0 \xrightarrow{\ d\ } \Omega^1 \xrightarrow{\ d\ } \Omega^2 \to \cdots
$$

is exact: its cohomology sheaves vanish in positive degree, so it is a **resolution** of the constant sheaf $\underline{\mathbb{R}}$ by the sheaves of forms.

*Proof.* Exactness of a sequence of sheaves is checked on stalks. The stalk of $\Omega^k$ at $x\in M$ is $\varinjlim_{U\ni x}\Omega^k(U)$, the colimit over the open neighbourhoods of $x$, and the complex of stalks is the colimit of the complexes of the sections over the neighbourhoods. Suppose a germ of a closed $k$-form is given, $k\geq 1$, represented by a closed form $\omega$ on a neighbourhood $V$ of $x$. Choose an open coordinate ball $B\subseteq V$ containing $x$; the restriction $\omega|_B$ is closed on the star-shaped set $B$, hence by the Poincaré lemma $\omega|_B = d\eta$ for a form $\eta$ on $B$, so the germ of $\omega$ is a coboundary in the stalk complex. Hence the cohomology sheaf vanishes in degree $k\geq 1$. In degree $0$ the cohomology sheaf is the kernel of $d$ on $\Omega^0$, which is $\underline{\mathbb{R}}$ by the previous theorem. $\square$

**Corollary (local triviality of the de Rham complex).** For every point $x\in M$ there is a neighbourhood $U$ of $x$ such that $H^k_{dR}(U) = 0$ for $k\geq 1$ and $H^0_{dR}(U) = \mathbb{R}$; that is, the de Rham complex of $M$ is locally a resolution of the constants. Consequently $\Omega^\bullet$ is a **fine resolution** of $\underline{\mathbb{R}}$ in the sense of the next section, and the local statement of the Poincaré lemma, and not any global statement, is what the sheaf-theoretic proof of the de Rham theorem uses.

**Remark (the failure of the global statement).** On a non-contractible manifold the global Poincaré lemma fails, and the failure is measured by the cohomology: for the circle, $H^1_{dR}(S^1) = \mathbb{R}$ and the closed form $d\theta$ on each of the two arcs does not extend to a global form on the circle, which is the sheaf-theoretic statement that the sequence of global sections is not surjective at $\Omega^1$. The example is the de Rham analogue of the exponential sequence of *Presheaves and Sheaves*, and it is the reason the obstruction is a class in $H^1$ rather than a failure of exactness.

## Fine Sheaves and the Acyclicity of the Forms

**Definition.** Let $\mathcal{R}$ be a sheaf of commutative rings on $M$. A sheaf $\mathcal{F}$ of $\mathcal{R}$-modules is **fine** if for every locally finite open cover $\{U_i\}$ of $M$ there is a partition of unity subordinate to it: elements $\eta_i \in \mathcal{R}(M)$ with $\operatorname{Supp}\eta_i \subseteq U_i$, the family of supports locally finite, and $\sum_i\eta_i = 1$. A sheaf of $\mathcal{R}$-modules is fine as soon as the structure sheaf $\mathcal{R}$ is fine and $\mathcal{F}$ is a module over it, since the $\eta_i$ act by multiplication.

**Theorem (the sheaves of forms are fine).** Let $M$ be a smooth manifold and let $C^\infty = \Omega^0$ be the sheaf of smooth functions, a sheaf of commutative rings. Then:

1. $C^\infty$ is a fine sheaf: for every locally finite open cover there is a smooth partition of unity subordinate to it, by the construction of partitions of unity on a manifold of the written *Differential Forms and Stokes' Theorem*.
2. Each $\Omega^k$ is a sheaf of $C^\infty$-modules, so each $\Omega^k$ is fine.
3. Fine sheaves are soft and soft sheaves on a paracompact space are acyclic; hence

    $$
    H^i(M,\Omega^k) = 0 \qquad \text{for all } i > 0 \text{ and all } k.
    $$

*Proof.* (1) is the existence of smooth partitions of unity subordinate to a locally finite cover of a manifold, which uses the smooth Urysohn lemma; the cover of a manifold may be taken locally finite because a manifold is paracompact and locally compact. (2) the product of a $k$-form by a smooth function is a $k$-form, compatibly with restriction, so $\Omega^k$ is a $C^\infty$-module, and the multiplication by the $\eta_i$ of a partition of unity exhibits the fineness. (3) is the theorem of *Sheaf Cohomology* that fine sheaves are soft and that soft sheaves on a paracompact space are acyclic. $\square$

**Theorem (the de Rham resolution computes the cohomology).** On a smooth manifold $M$ there is a natural isomorphism

$$
H^k\bigl(\Omega^\bullet(M)\bigr) = H^k_{dR}(M) \cong H^k(M,\underline{\mathbb{R}})
$$

for every $k$, and the isomorphism is induced by the comparison of the de Rham resolution with an injective resolution of $\underline{\mathbb{R}}$.

*Proof.* The de Rham complex of sheaves is a resolution of $\underline{\mathbb{R}}$ whose terms are acyclic by the previous theorem, and the global sections of the resolution form precisely the de Rham complex $\Omega^\bullet(M)$. The abstract de Rham theorem of *Derived Functors and Sheaf Cohomology* — the statement that an acyclic resolution computes the derived functors of the functor of sections — gives the isomorphism $H^k(\Omega^\bullet(M)) = H^k(\Gamma(M,\Omega^\bullet))\cong R^k\Gamma(M,\underline{\mathbb{R}}) = H^k(M,\underline{\mathbb{R}})$. Alternatively, and without invoking the general theorem, the acyclicity of the $\Omega^k$ and the dimension-shifting exact sequence obtained by splitting the resolution into short exact sequences $0\to Z^k\to\Omega^k\to Z^{k+1}\to 0$, with $Z^k$ the sheaf of closed $k$-forms, give the same isomorphism by induction on $k$. $\square$

## The Theorem of de Rham

**Theorem (de Rham).** Let $M$ be a smooth manifold. There are natural isomorphisms

$$
H^k_{dR}(M) \cong H^k(M,\underline{\mathbb{R}}) \cong H^k(M;\mathbb{R})
$$

for every $k$, natural with respect to smooth maps, where the second is the comparison of sheaf and singular cohomology of *Sheaf Cohomology*. In particular $H^k_{dR}(M)$ is a homotopy invariant of $M$, is finite-dimensional with dimension the $k$-th Betti number when $M$ is a closed manifold, and a closed form on a closed oriented manifold is exact if and only if all of its periods over singular cycles vanish.

*Proof.* The first isomorphism is the theorem of the previous section. The second is the comparison theorem: a smooth manifold is paracompact and locally contractible, and for such a space the sheaf cohomology of the constant sheaf is the singular cohomology. The stated corollaries are the corollaries of the theorem of de Rham recorded in the written article, now obtained as properties of sheaf cohomology, which is homotopy invariant because the pullback of a constant sheaf along a homotopy equivalence is an isomorphism and the cohomology of the sheaf is transported along it. $\square$

**Corollary (the two spectral-sequence proofs agree).** On a manifold the de Rham theorem may also be obtained from the Čech–de Rham double complex $K^{p,q} = \check C^p(\mathcal{U},\Omega^q)$ of *Čech Cohomology*, for a cover $\mathcal{U}$ with all finite intersections contractible. Since the sheaves $\Omega^q$ are acyclic and the cover is good, the Čech cohomology of the cover with coefficients in $\Omega^q$ vanishes in positive degree, so the filtration by $q$ has

$$
E_1^{p,q} = H^p\bigl(\check C^\bullet(\mathcal{U},\Omega^q)\bigr) = \begin{cases} \Omega^q(M), & p = 0,\\ 0, & p > 0,\end{cases}
$$

with $d_1$ the exterior derivative; hence $E_2^{0,q} = H^q_{dR}(M)$ on the axis $p=0$, and the double complex computes the hypercohomology of the de Rham resolution, so $H^q_{dR}(M)\cong\mathbb{H}^q(M,\Omega^\bullet) = H^q(M,\underline{\mathbb{R}})$. The filtration by $p$ has instead $E_1^{p,q} = \check C^p(\mathcal{U},\mathcal{H}^q_{dR})$, with $\mathcal{H}^q_{dR}$ the presheaf $U\mapsto H^q_{dR}(U)$, and the induced differential is the Čech differential; on a good cover this presheaf is concentrated in degree $q=0$, so $E_2^{p,0} = \check H^p(\mathcal{U},\underline{\mathbb{R}})$ on the bottom row, and Leray's theorem identifies it with $H^p(M,\underline{\mathbb{R}})$. The two filtrations of the same double complex have the same abutment, and their comparison is the de Rham theorem; the construction uses the hypercohomology of a complex of sheaves described in *Derived Functors and Sheaf Cohomology*.

**Remark (the relative case).** The theorem is not a statement about forms alone: the same argument applies to any resolution of $\underline{\mathbb{R}}$ by acyclic sheaves on $M$, and gives the comparison of the cohomology of the resolution with the cohomology of $M$ with real coefficients. The characteristic classes of a vector bundle over $M$ are represented by the Chern and Pontryagin forms built from the curvature of a connection, as in the written *Fibre Bundles, Connections and Curvature*; the de Rham theorem then identifies the cohomology classes they define with the singular characteristic classes, and the resulting comparison of the graded rings is the Chern–Weil theory, which is not developed here.

### The Algebra Structure

**Theorem (the de Rham complex as a differential graded algebra).** The direct sum $\Omega^\bullet = \bigoplus_{k}\Omega^k$, with the wedge product and the exterior derivative, is a sheaf of commutative differential graded algebras over the constant sheaf $\underline{\mathbb{R}}$: the wedge product is graded-commutative and associative and $d$ is a derivation, $d(\alpha\wedge\beta) = d\alpha\wedge\beta + (-1)^k\alpha\wedge d\beta$ for $\alpha\in\Omega^k$. The same structure holds on global sections, and the isomorphisms of the de Rham theorem are isomorphisms of graded algebras in the sense that the wedge product on forms corresponds to the cup product on cohomology:

$$
[\alpha]\smile[\beta] = [\alpha\wedge\beta] \in H^{k+l}_{dR}(M)\cong H^{k+l}(M;\mathbb{R}).
$$

*Proof.* The graded-commutativity and the derivation property of $d$ are the local computations of the written article; the final statement follows because the comparison of the de Rham resolution with an injective resolution of $\underline{\mathbb{R}}$ is a comparison of resolutions by sheaves of differential graded algebras: injective resolutions may be taken to carry a compatible product by the standard construction, and the induced map on cohomology respects the products up to the homotopy that makes the comparison unique. Equivalently, the wedge product of closed forms is closed and the product of exact forms with closed forms is exact, so the product descends to cohomology; the identification with the cup product follows from the naturality of the comparison and its agreement with the algebra structures on the level of the complexes. $\square$

**Corollary (the cohomology ring is computable from forms).** For a smooth manifold $M$ the real cohomology ring $(H^\bullet(M;\mathbb{R}),\smile)$ is computed by the differential graded algebra $(\Omega^\bullet(M),d,\wedge)$ of global forms: its cohomology ring is the real cohomology ring of $M$. In particular the de Rham representatives of the characteristic classes of a bundle multiply as the classes do, and the Chern classes of a complex vector bundle over $M$ generate a subring of $H^\bullet(M;\mathbb{R})$ computed from the curvature forms of any connection on the bundle. The differential graded algebras themselves, as objects of algebra, are those of Part I's *Differential Graded Categories* and *Operads*.

### The Compactly Supported de Rham Complex

**Definition.** Let $\Omega^k_c(M)$ denote the space of smooth $k$-forms on $M$ with compact support, and let $\Omega^\bullet_c(M)$ be the resulting complex with the exterior derivative. Its cohomology is the **compactly supported de Rham cohomology** $H^k_{c,dR}(M)$.

**Theorem (compactly supported de Rham theorem).** Let $M$ be a smooth $n$-manifold.

1. There is a natural isomorphism $H^k_{c,dR}(M)\cong H^k_c(M;\mathbb{R})$ between the cohomology of the compactly supported de Rham complex and the compactly supported singular cohomology of *Sheaf Cohomology*.
2. If $M$ is a closed oriented $n$-manifold, integration gives a nondegenerate pairing
   $$H^k_{dR}(M)\times H^{n-k}_{c,dR}(M)\to\mathbb{R}, \qquad ([\alpha],[\beta])\mapsto\int_M\alpha\wedge\beta,$$
 which is the de Rham form of the Poincaré duality of *Poincaré Duality*, and which identifies the compactly supported cohomology with the dual of the de Rham cohomology.
3. For $M = \mathbb{R}^n$, $H^k_{c,dR}(\mathbb{R}^n) = \mathbb{R}$ for $k = n$ and $0$ otherwise; for the compact manifold $S^n$ the compactly supported cohomology coincides with the ordinary de Rham cohomology, so $H^k_{c,dR}(S^n) = \mathbb{R}$ for $k = 0$ and $k = n$ and $0$ otherwise, in agreement with the compactly supported groups of *Sheaf Cohomology*.

*Proof.* (1) The compactly supported forms are exactly the sections over $M$ of the sheaf obtained by extending by zero the sheaf of forms on the open subsets: the presheaf $U\mapsto\Omega^k_c(U)$ is not a sheaf, but its sheafification is $\Omega^k$, and the compactly supported cohomology is computed by the complex of sections with support in a family, in the sense of *Sheaf Cohomology*; comparing with the compactly supported singular cochains, which compute $H^k_c$, gives the isomorphism. (2) The wedge product of a closed form and a compactly supported closed form is compactly supported and closed, and the integral depends only on the classes by Stokes' theorem; the pairing is nondegenerate by the Poincaré duality of the written article's Hodge-theoretic corollary, the harmonic representatives of the two cohomologies pairing by the integral of their wedge product. (3) is the computation of the compactly supported cohomology of $\mathbb{R}^n$ and of the sphere recorded in *Sheaf Cohomology*, together with (1). $\square$

### Two Further Instances

**The Dolbeault complex.** On a complex manifold the decomposition of forms into types gives a bicomplex

$$
0 \to \Omega^{p,0} \xrightarrow{\ \bar\partial\ } \Omega^{p,1} \xrightarrow{\ \bar\partial\ } \Omega^{p,2} \to \cdots,
$$

whose exactness on small polydiscs — the $\bar\partial$-Poincaré lemma — is the complex-geometric form of the Poincaré lemma, and which is therefore a resolution of the sheaf $\Omega^p$ of holomorphic $p$-forms by fine sheaves. The same argument then gives the **Dolbeault theorem** $H^q(M,\Omega^p)\cong H^{p,q}_{\bar\partial}(M)$, and on a Kähler manifold the Hodge decomposition refines the de Rham theorem into bidegrees. The complex manifolds, the operators $\partial,\bar\partial$ and the Kähler metrics are those of *Hermitian Geometry and Almost Complex Structures* and *Kähler Geometry*, where the statements are made; the Hodge star and the Laplace–de Rham operator used in the elliptic version of the argument are those of the written *Differential Forms and Stokes' Theorem*, and the analytic theory of the elliptic operator is Part III's.

**The relative de Rham complex of a fibration.** Let $\pi : E\to B$ be a fibre bundle with fibre $F$, and filter the de Rham complex of $E$ by the number of differentials along the fibre; the first term of the resulting spectral sequence is the de Rham complex of $B$ with coefficients in the cohomology of the fibre, and the sequence degenerates when the monodromy is trivial and the base is simply connected. The construction yields the **Leray–Serre spectral sequence** of *The Leray–Serre Spectral Sequence* in its de Rham form,

$$
E_2^{p,q} = H^p(B;\underline{H}^q(F;\mathbb{R})) \Longrightarrow H^{p+q}(E;\mathbb{R}),
$$

and the **Leray–Hirsch theorem** that $H^\bullet(E;\mathbb{R})\cong H^\bullet(B;\mathbb{R})\otimes H^\bullet(F;\mathbb{R})$ for a trivial monodromy and a cohomologically trivial base; the Chern classes of the bundle are then computed by the transgression in this sequence, as in *Fibre Bundles, Connections and Curvature*.

## Summary

The differential forms on a manifold assemble into a complex of sheaves $\Omega^\bullet$, the **de Rham complex**, whose differential is the exterior derivative and whose kernel in degree zero is the constant sheaf $\underline{\mathbb{R}}$ of locally constant functions. By the Poincaré lemma, a closed form of positive degree on a star-shaped open set is exact, and since exactness of a sequence of sheaves is a stalkwise condition, the de Rham complex of sheaves is exact: it is a resolution of the constant sheaf. The sheaves of forms are modules over the sheaf $C^\infty$ of smooth functions, which possesses partitions of unity subordinate to locally finite covers, so they are fine, hence soft, hence acyclic on the paracompact manifold; the de Rham resolution is therefore an acyclic resolution of $\underline{\mathbb{R}}$ and computes the cohomology of the constant sheaf, giving $H^k_{dR}(M)\cong H^k(M,\underline{\mathbb{R}})$, and composing with the comparison of sheaf with singular cohomology gives the theorem of de Rham $H^k_{dR}(M)\cong H^k(M;\mathbb{R})$, with the corollaries of homotopy invariance and finite dimensionality that the written article records.

The de Rham complex is moreover a sheaf of commutative differential graded algebras under the wedge product, the product descending to cohomology and corresponding to the cup product, so that the de Rham theorem is an isomorphism of graded rings and the real cohomology ring of the manifold is computable from forms; the characteristic classes of the written *Fibre Bundles, Connections and Curvature* are the de Rham representatives of the singular classes in this isomorphism. The Čech–de Rham double complex recovers the same comparison from the two spectral sequences, in which form the theorem is the prototype of the comparison theorems relating a resolution to the cohomology it computes; the compactly supported variant, whose cohomology is the compactly supported cohomology of the space, carries the integration pairing that realises Poincaré duality on a closed oriented manifold; and the Dolbeault complex on a complex manifold, and the filtered de Rham complex of a fibre bundle, are the two instances that carry the theory into the complex and the fibred settings.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Omega^k$ | sheaf of differential $k$-forms; $\Omega^k(U)$ = forms on $U$ |
| $\Omega^k(M) = \Gamma(M,\Omega^k)$ | global $k$-forms, as in the written *Differential Forms and Stokes' Theorem* |
| $d$ | exterior derivative, a morphism of sheaves; $d^2 = 0$ |
| $\underline{\mathbb{R}}$ | constant sheaf of locally constant real functions; kernel of $d$ on $\Omega^0$ |
| de Rham resolution | $0\to\underline{\mathbb{R}}\to\Omega^0\xrightarrow{d}\Omega^1\to\cdots\to\Omega^n\to 0$, exact |
| $H^k_{dR}(M) = H^k(\Omega^\bullet(M))$ | de Rham cohomology; $\cong H^k(M,\underline{\mathbb{R}})\cong H^k(M;\mathbb{R})$ |
| fine sheaf | module over a structure sheaf with partitions of unity; fine $\Rightarrow$ soft $\Rightarrow$ acyclic |
| $\wedge$ | wedge product, graded-commutative; $[\alpha]\smile[\beta] = [\alpha\wedge\beta]$ |
| $\Omega^k_c$, $H^k_{c,dR}$ | compactly supported forms and their cohomology; $\cong H^k_c(M;\mathbb{R})$ |
| $\Omega^{p,q}$, $\bar\partial$ | forms of type $(p,q)$ and the Dolbeault operator; Dolbeault complex |
| $Z^k$ | sheaf of closed $k$-forms; $0\to Z^k\to\Omega^k\to Z^{k+1}\to 0$ |



## Further Reading

- Georges de Rham, *Differentiable Manifolds: Forms, Currents, Harmonic Forms* (Springer, 1984), for the original sheaf-theoretic proof of the theorem and the currents.
- Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology* (Springer, 1982), for the Čech–de Rham double complex, the Leray–Hirsch theorem and the spectral sequences.
- Werner Greub, Stephen Halperin and Ray Vanstone, *Connections, Curvature and Cohomology I* (Academic Press, 1972), for the sheaf-theoretic de Rham theorem and its differential-graded-algebra refinement.
- Roger Godement, *Topologie algébrique et théorie des faisceaux* (Hermann, 1958), for fine and soft resolutions and the acyclicity of the sheaves of forms.
- Phillip A. Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the Dolbeault complex, the $\bar\partial$-Poincaré lemma and the Hodge decomposition.
- Frank W. Warner, *Foundations of Differentiable Manifolds and Lie Groups* (Springer, 1983), for the de Rham complex, the Poincaré lemma and harmonic forms.
