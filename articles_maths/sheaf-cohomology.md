
# __Sheaf Cohomology__

## Introduction

The functor $\Gamma(X,-)$ of global sections of a sheaf is left exact: a short exact sequence of sheaves $0 \to \mathcal{F} \to \mathcal{G} \to \mathcal{H} \to 0$ gives an exact sequence

$$
0 \to \mathcal{F}(X) \to \mathcal{G}(X) \to \mathcal{H}(X)
$$

of abelian groups, and the last map need not be surjective; the exponential sequence of *Presheaves and Sheaves* exhibits the failure, since a nowhere-zero continuous function on $\mathbb{C}^*$ need not be a continuous exponential. **Sheaf cohomology** is the derived functor theory that repairs the failure: it produces groups $H^i(X,\mathcal{F})$ for $i \geq 0$ with $H^0(X,\mathcal{F}) = \Gamma(X,\mathcal{F})$ and a long exact sequence

$$
0 \to H^0(X,\mathcal{F}) \to H^0(X,\mathcal{G}) \to H^0(X,\mathcal{H}) \to H^1(X,\mathcal{F}) \to H^1(X,\mathcal{G}) \to H^1(X,\mathcal{H}) \to H^2(X,\mathcal{F}) \to \cdots
$$

extending the exact sequence of sections to the right, so that the obstruction to lifting a section of $\mathcal{H}$ to $\mathcal{G}$ becomes a class in $H^1(X,\mathcal{F})$. The theory is the topological reading of the derived functors of Part I: the general definitions of injective resolutions, of right derived functors, of $\delta$-functors and of the long exact sequence are the subject of the companion articles *Homological Algebra* and *Derived Functors* of Part I, and this article takes them as given, developing the instances that the topology requires — the abundance of flabby and soft resolutions, the comparison with singular cohomology, and the spectral sequence of a continuous map.

The article is organised around the two theorems that make sheaf cohomology computable. The first is that **flabby sheaves are acyclic**: cohomology may be computed from any resolution by flabby sheaves, and such resolutions exist for every sheaf on every space, since every sheaf embeds in a flabby sheaf. The second is the **comparison with singular cohomology**: for a locally contractible paracompact space $X$ — in particular for a CW complex or a manifold — there is an isomorphism $H^i(X,\underline{A}) \cong H^i(X;A)$ between the sheaf cohomology of the constant sheaf and the singular cohomology of *Cohomology and the Universal Coefficient Theorem*, so that the computations of the earlier articles are computations of sheaf cohomology and the two theories are one. Between them, the two theorems give the means of computation, and the further constructions — cohomology with support, higher direct images and the spectral sequence of a map — give the means of organisation.

The analytic constructions are deferred as usual. The de Rham complex is a resolution of the constant sheaf $\underline{\mathbb{R}}$ for a smooth manifold; the statement is made here and proved, where the differential forms and the exterior derivative are those of the *Differential Forms and Stokes' Theorem*. The sheaf-theoretic methods that require completeness, a limit of test functions or a measure — the theory of $D$-modules and the analytic cohomology of complex manifolds — belong to Part III. Sheaves on a Grothendieck site, and the derived category of sheaves used for the general theory of direct images, are Part I's *Sheaves on Sites* and *Derived Categories*.

Throughout, $X$ is a topological space, $\mathcal{F}$ a sheaf of abelian groups on $X$ unless another coefficient category is named, and the cohomology is written $H^i(X,\mathcal{F})$ with a comma, as fixed in *Presheaves and Sheaves*, in deliberate contrast with the semicolon of the singular notation $H^i(X;G)$.

## The Derived Functor Definition

**Theorem (enough injectives).** The abelian category $\mathrm{Sh}(X,\mathbf{Ab})$ of sheaves of abelian groups on $X$ has enough injectives: every sheaf $\mathcal{F}$ admits a monomorphism $\mathcal{F} \hookrightarrow \mathcal{I}$ into an injective sheaf. The same holds for the category of sheaves of $R$-modules on a ringed space $(X,\mathcal{O}_X)$.

*Proof sketch.* For each $x \in X$ choose a monomorphism $\mathcal{F}_x \hookrightarrow I_x$ of $\mathcal{F}_x$ into an injective abelian group, which exists because the category of abelian groups has enough injectives, and consider the sheaf $\mathcal{G} = \prod_{x\in X}(i_x)_*I_x$ of *Presheaves and Sheaves*. The canonical map $\mathcal{F} \to \mathcal{G}$ is a monomorphism, since it is injective on stalks, and $\mathcal{G}$ is flabby; a flabby sheaf that is a product of skyscrapers over injective values is injective, because the functor $\mathcal{H}om(-,\mathcal{G})$ is exact: sections over $U$ of $(i_x)_*I_x$ form the group $I_x$ or $0$, and injectivity of the $I_x$ gives the extension of morphisms. Passing to the module case replaces abelian groups by $R$-modules throughout. $\square$

**Definition.** Let $\mathcal{F}$ be a sheaf of abelian groups on $X$ and let $\mathcal{F} \to \mathcal{I}^\bullet$ be an injective resolution: a complex $0 \to \mathcal{I}^0 \to \mathcal{I}^1 \to \mathcal{I}^2 \to \cdots$ exact except at $\mathcal{I}^0$, with each $\mathcal{I}^j$ injective. The **sheaf cohomology** of $\mathcal{F}$ is

$$
H^i(X,\mathcal{F}) = R^i\Gamma(X,\mathcal{F}) = H^i\bigl(\Gamma(X,\mathcal{I}^\bullet)\bigr),
$$

the $i$-th cohomology of the complex of abelian groups obtained by applying global sections to the resolution; in particular $H^0(X,\mathcal{F}) = \Gamma(X,\mathcal{F})$ and $H^i(X,\mathcal{F}) = 0$ for $i < 0$. The definition does not depend on the chosen injective resolution, by the comparison theorem for resolutions in *Derived Functors* of Part I, and is functorial in both variables: a morphism $\varphi : \mathcal{F} \to \mathcal{G}$ induces $\varphi_* : H^i(X,\mathcal{F}) \to H^i(X,\mathcal{G})$ naturally, and a continuous map $f : X \to Y$ induces $f^* : H^i(Y,\mathcal{F}) \to H^i(X,f^{-1}\mathcal{F})$ from the natural transformation $\Gamma(Y,-) \to \Gamma(X, f^{-1}(-))$.

**Theorem (the long exact sequence).** Let $0 \to \mathcal{F} \to \mathcal{G} \to \mathcal{H} \to 0$ be a short exact sequence of sheaves of abelian groups on $X$. There is a long exact sequence of abelian groups

$$
0 \to H^0(X,\mathcal{F}) \to H^0(X,\mathcal{G}) \to H^0(X,\mathcal{H}) \xrightarrow{\ \delta\ } H^1(X,\mathcal{F}) \to H^1(X,\mathcal{G}) \to H^1(X,\mathcal{H}) \xrightarrow{\ \delta\ } H^2(X,\mathcal{F}) \to \cdots,
$$

natural in the short exact sequence, the **connecting homomorphism** $\delta$ being constructed by the snake lemma from a commutative ladder of injective resolutions.

*Proof.* This is the long exact sequence of a short exact sequence under a left exact functor, *Homological Algebra* and *Derived Functors* of Part I; the point specific to sheaves is that a short exact sequence of sheaves is exact on stalks by *Presheaves and Sheaves*, and hence its injective resolutions form the required ladder. $\square$

**Theorem (dimension shifting and the vanishing of higher cohomology of injectives).** If $\mathcal{I}$ is injective then $H^i(X,\mathcal{I}) = 0$ for $i > 0$, and for every short exact sequence as above the connecting maps give isomorphisms

$$
H^i(X,\mathcal{H}) \cong H^{i+1}(X,\mathcal{F}) \qquad (i \geq 1),
$$

the **dimension shifting** isomorphisms, and an exact sequence $0 \to H^1(X,\mathcal{F}) \to H^1(X,\mathcal{G}) \to H^1(X,\mathcal{H}) \to H^2(X,\mathcal{F}) \to 0$. Consequently $H^i(X,\mathcal{F})$ may be computed from a resolution of $\mathcal{F}$ by acyclic sheaves: if $0 \to \mathcal{F} \to \mathcal{A}^0 \to \mathcal{A}^1 \to \cdots$ is exact and $H^j(X,\mathcal{A}^i) = 0$ for $j > 0$ and all $i$, then $H^i(X,\mathcal{F}) \cong H^i(\Gamma(X,\mathcal{A}^\bullet))$.

*Proof.* The vanishing on injectives is the definition of injectivity applied to the functor $\Gamma$; the shifting isomorphisms are read off from the long exact sequence, the groups $H^i(X,\mathcal{G})$ with $i \geq 1$ being the successive images and kernels of the exact sequence, and the acyclicity statement is the standard comparison theorem for acyclic resolutions. $\square$

**Definition.** A sheaf $\mathcal{F}$ is **acyclic** if $H^i(X,\mathcal{F}) = 0$ for all $i > 0$. The theorem says that acyclic resolutions compute cohomology; the rest of the article identifies the acyclic sheaves that occur.

## Flabby, Soft and Acyclic Sheaves

**Definition.** A sheaf $\mathcal{F}$ on $X$ is **flabby** (or **flasque**) if every section of $\mathcal{F}$ over an open subset $U \subseteq X$ extends to a section over $X$: the restriction map $\mathcal{F}(X) \to \mathcal{F}(U)$ is surjective for every open $U$.

**Theorem (flabby sheaves are acyclic).** Let $0 \to \mathcal{F} \to \mathcal{G} \to \mathcal{H} \to 0$ be a short exact sequence of sheaves of abelian groups with $\mathcal{F}$ flabby. Then:

1. $\mathcal{G}$ is flabby if and only if $\mathcal{H}$ is flabby.
2. The sequence of global sections $0 \to \mathcal{F}(X) \to \mathcal{G}(X) \to \mathcal{H}(X) \to 0$ is exact.
3. Flabby sheaves are acyclic: if $\mathcal{F}$ is flabby then $H^i(X,\mathcal{F}) = 0$ for all $i > 0$.

*Proof.* (1) Suppose first that $\mathcal{F}$ and $\mathcal{G}$ are flabby and let $t \in \mathcal{H}(U)$. Choose a cover of $U$ by open sets $U_i$ on which $t$ lifts, say to $s_i \in \mathcal{G}(U_i)$, and extend each $s_i$ to an element $\tilde s_i \in \mathcal{G}(X)$ using the flabbiness of $\mathcal{G}$. On $U_i \cap U_j$ the difference $\tilde s_i - \tilde s_j$ has zero image in $\mathcal{H}$ and hence lies in $\mathcal{F}(U_i\cap U_j)$; by the flabbiness of $\mathcal{F}$ this element extends to an element $f_{ij} \in \mathcal{F}(X)$, and replacing $\tilde s_i$ by $\tilde s_i - f_{ij}$ on the cover makes the local lifts agree on overlaps; they glue to a global lift of $t$. Conversely, suppose $\mathcal{F}$ and $\mathcal{H}$ are flabby and let $s \in \mathcal{G}(U)$. The image of $s$ in $\mathcal{H}(U)$ extends to $X$ by the flabbiness of $\mathcal{H}$; on a cover of $X$ on which that extension lifts to $\mathcal{G}$, the differences of two lifts lie in $\mathcal{F}$, and the flabbiness of $\mathcal{F}$ corrects them as before, producing a global extension of $s$. (2) Given $t \in \mathcal{H}(X)$, choose a cover of $X$ by open sets $U_i$ on which $t$ lifts to $s_i \in \mathcal{G}(U_i)$ and set $s_{ij} = s_i - s_j \in \mathcal{F}(U_i\cap U_j)$. By the flabbiness of $\mathcal{F}$ each $s_{ij}$ extends to an element $f_{ij} \in \mathcal{F}(X)$, and the sections $s_i - f_{ij}$ of $\mathcal{G}(U_i)$ agree on overlaps $U_i \cap U_j$, so they glue to $s \in \mathcal{G}(X)$ with the same image as $t$ in $\mathcal{H}(X)$. (3) Embed $\mathcal{F}$ in an injective sheaf $\mathcal{I}$, which is flabby: given $s \in \mathcal{I}(U)$, the morphism of sheaves $\underline{\mathbb{Z}}_U \hookrightarrow \underline{\mathbb{Z}}_X$ of extension by zero induces an extension of the corresponding morphism into $\mathcal{I}$ by injectivity, exhibiting an extension of $s$ to $X$. The quotient $\mathcal{Q} = \mathcal{I}/\mathcal{F}$ is flabby by (1), and (2) applied to $0 \to \mathcal{F} \to \mathcal{I} \to \mathcal{Q} \to 0$ gives $H^1(X,\mathcal{F}) = \operatorname{coker}(\mathcal{I}(X)\to\mathcal{Q}(X)) = 0$; the long exact sequence gives $H^{i+1}(X,\mathcal{F}) \cong H^i(X,\mathcal{Q})$ for $i \geq 1$, and $\mathcal{Q}$ is again flabby, so induction gives the vanishing in all positive degrees. $\square$

**Theorem (the Godement resolution).** Let $C^0(\mathcal{A})$ denote the sheaf $U \mapsto \prod_{x\in U}\mathcal{A}_x$ with restriction maps the projections; it is flabby. For a sheaf $\mathcal{F}$ set $\mathcal{G}^{-1} = \mathcal{F}$ and define, for $k \geq 0$,

$$
\mathcal{G}^0 = C^0(\mathcal{F}), \qquad \mathcal{G}^{k+1} = C^0\bigl(\operatorname{coker}(\mathcal{G}^{k-1} \to \mathcal{G}^k)\bigr),
$$

the cokernel being taken in sheaves; then $0 \to \mathcal{F} \to \mathcal{G}^0 \to \mathcal{G}^1 \to \cdots$ is an exact resolution of $\mathcal{F}$ by flabby sheaves, functorial in $\mathcal{F}$. Consequently every sheaf on every topological space admits a flabby resolution and the derived functors $H^i(X,\mathcal{F})$ are computable from it; and if the cohomological dimension of $X$ is a finite number $n$, then $\mathrm{Sh}(X,\mathbf{Ab})$ has global dimension $n$.

*Proof sketch.* Each $\mathcal{G}^k$ is flabby, since the restriction $\prod_{x\in U}\mathcal{A}_x \to \prod_{x\in V}\mathcal{A}_x$ is a projection onto a subproduct and the section over $U$ may be extended by zero outside $V$ on the remaining factors. The exactness at $\mathcal{G}^0$ is the injectivity of the map $\mathcal{F}\to\mathcal{G}^0$ on stalks, and the exactness at $\mathcal{G}^{k}$ for $k \geq 1$ is a diagram chase using the functoriality of the construction. $\square$

**Theorem (Grothendieck's vanishing theorem).** If $X$ is a Noetherian topological space of dimension $n$ — for instance a Noetherian scheme with the Zariski topology — then

$$
H^i(X,\mathcal{F}) = 0 \qquad \text{for all } i > n \text{ and all sheaves } \mathcal{F},
$$

so the cohomological dimension of $X$ is at most $n$. For sheaves on a paracompact space, a vanishing statement of the same kind holds with the covering dimension of $X$ in the place of $n$.

*Proof sketch.* Let $0 \to \mathcal{F} \to \mathcal{G}^0 \to \mathcal{G}^1 \to \cdots$ be the canonical flabby resolution of $\mathcal{F}$ obtained by iterating the construction $\mathcal{A} \mapsto \mathcal{A}^{*}$ with $\mathcal{A}^{*}(U) = \prod_{x\in U}\mathcal{A}_x$; on a Noetherian space of dimension $n$ this resolution may be truncated after $n$ steps, because the successive quotients are concentrated on closed subsets of strictly decreasing dimension, by the definition of the dimension as the supremum of the lengths of chains of closed irreducible subsets. Applying the functor $\Gamma$ to the truncated resolution and using the acyclicity of flabby sheaves gives the vanishing above degree $n$. $\square$

**Definition.** A sheaf $\mathcal{F}$ on a paracompact space $X$ is **soft** if every section over a closed set extends to a section over $X$: the restriction map $\Gamma(X,\mathcal{F}) \to \Gamma(Z,\mathcal{F}|_Z)$ is surjective for every closed $Z \subseteq X$, where $\Gamma(Z,\mathcal{F}|_Z)$ denotes the sections over $Z$ defined as germs admitting local extensions. A sheaf $\mathcal{F}$ of modules over a sheaf of rings is **fine** if for every locally finite open cover of $X$ there is a partition of unity subordinate to it: endomorphisms $1 = \sum \eta_i$ with $\operatorname{Supp}\eta_i$ refined by the cover, the sum being locally finite.

**Theorem (soft and fine sheaves).** Let $X$ be a paracompact space.

1. Flabby sheaves are soft.
2. Soft sheaves are acyclic for the functor of sections with support in a fixed closed set; in particular, on a paracompact space, soft sheaves are acyclic and may be used to compute $H^i(X,\mathcal{F})$.
3. Fine sheaves are soft. Consequently the sheaf of continuous real-valued functions, the sheaf of smooth functions on a smooth manifold and the sheaves $\Omega^p$ of differential forms are fine, hence soft, hence acyclic, and they compute the cohomology of the constant sheaf in their resolutions.

*Proof sketch.* (1) Let $s$ be a section of $\mathcal{F}$ over the closed set $Z$. By the definition of the restriction sheaf, $s$ is locally, near each point of $Z$, the restriction of a section of $\mathcal{F}$ on an open neighbourhood of that point; on a paracompact space the local germs extend to open neighbourhoods of the points of $Z$ and the local data glue on an open neighbourhood $U \supseteq Z$, producing a section $\tilde s \in \mathcal{F}(U)$ with $\tilde s|_Z = s$ (this is the extension lemma for sections over closed subsets of a paracompact space). Flabbiness then supplies the extension from the open set $U$ to $X$: the restriction $\mathcal{F}(X)\to\mathcal{F}(U)$ is surjective, so $s$ extends to a global section and $\mathcal{F}$ is soft. No partition of unity enters, flabbiness alone being responsible for the second step. (2) One shows that a soft sheaf is acyclic by the same argument as for flabby sheaves, replacing the extension from an open set by the extension from a closed set; the sections with support in a closed set form a left exact functor whose derived functors agree with those of $\Gamma$ when the space is paracompact, since a locally finite cover by closed sets may be refined and the extensions combined. (3) Given a locally finite open cover and a section over a closed set, the partition of unity makes the extension local: one multiplies a locally defined extension by the $\eta_i$ and sums, the local finiteness making the sum a section of $\mathcal{F}$ — here the $\mathcal{O}_X$-module structure is what the multiplication uses, and this is exactly why the argument applies to fine sheaves and not to arbitrary ones. $\square$

**Example (the skyscraper sheaf is flabby).** Let $i_x : \{x\} \hookrightarrow X$ be the inclusion of a point and let $A$ be an abelian group. The sheaf $(i_x)_*A$ has $(i_x)_*A(U) = A$ if $x \in U$ and $0$ otherwise, with restriction the identity or the zero map; a section over $U$ (either an element of $A$ or $0$) extends to $X$ (to the same element, or to $0$), so the sheaf is flabby. Hence

$$
H^0(X,(i_x)_*A) = A, \qquad H^i(X,(i_x)_*A) = 0 \quad (i > 0).
$$

The same computation applies to any sheaf concentrated on a finite set of points.

## The Comparison with Singular Cohomology

**Theorem (sheaf cohomology of the constant sheaf).** Let $X$ be a paracompact space that is locally contractible — every neighbourhood of every point contains a contractible neighbourhood — for instance a CW complex, a manifold or a simplicial complex. Then for every abelian group $A$ and every $i \geq 0$ there is a natural isomorphism

$$
H^i(X,\underline{A}) \cong H^i(X;A),
$$

between the sheaf cohomology of the constant sheaf $\underline{A}$ and the singular cohomology with coefficients in $A$.

*Proof sketch.* Let $\mathcal{S}^i$ be the sheaf associated with the presheaf $U \mapsto C^i(U;A)$ of singular cochains of the subspace $U$, and let $\mathcal{S}^\bullet$ be the resulting complex of sheaves. By local contractibility, every point has arbitrarily small contractible neighbourhoods, and for a contractible $U$ the complex $C^\bullet(U;A)$ has cohomology $A$ in degree $0$ and zero in positive degrees, so the cohomology sheaves of $\mathcal{S}^\bullet$ are $\underline{A}$ in degree $0$ and $0$ elsewhere: the complex is a resolution of $\underline{A}$. Each $\mathcal{S}^i$ is flabby, since a cochain on $U$ extends to $X$ by declaring it zero on the simplices not contained in $U$; hence the resolution is acyclic and computes $H^i(X,\underline{A}) = H^i(\Gamma(X,\mathcal{S}^\bullet))$. The canonical comparison map $C^\bullet(X;A) \to \Gamma(X,\mathcal{S}^\bullet)$ from the singular cochain complex of $X$ into the complex of sections of the resolution is a quasi-isomorphism, by the comparison theorem for two resolutions of the same sheaf, and it induces the required isomorphism $H^i(X;A)\to H^i(X,\underline{A})$. $\square$

**Corollary (the computations of the earlier articles are sheaf-theoretic).** For the sphere, the projective spaces and the tori, the cohomology computed by the cellular and simplicial methods of *Simplicial and Singular Homology*, *Cup and Cap Products* and *Poincaré Duality* is the sheaf cohomology of the constant sheaf; in particular $H^0(S^n,\underline{\mathbb{Z}}) = H^n(S^n,\underline{\mathbb{Z}}) = \mathbb{Z}$ for $n \geq 1$, the other groups vanishing, and $H^0(\mathbb{C}^*,\underline{\mathbb{Z}}) = H^1(\mathbb{C}^*,\underline{\mathbb{Z}}) = \mathbb{Z}$ with all higher groups zero. The exponential sequence of *Presheaves and Sheaves* is thereby a computation of $H^1(\mathbb{C}^*,\underline{\mathbb{Z}})$.

**Remark (coefficients in a local system).** The comparison theorem extends to cohomology with coefficients in a locally constant sheaf, a **local system** of abelian groups, which for a path-connected, locally simply connected $X$ is the same as a representation of the fundamental group $\pi_1(X,x_0)$ of *The Fundamental Group and Covering Spaces*: the sheaf of sections of the covering space associated with the representation is locally constant, and $H^1(X,\mathcal{L})$ classifies the torsors under $\mathcal{L}$. The cap product with the fundamental class gives the **twisted Poincaré duality**

$$
H^k(M,\mathcal{L}) \cong H_{n-k}(M,\mathcal{L}^{\vee})^{\vee},
$$

for a closed oriented $n$-manifold $M$ and a local system $\mathcal{L}$, with $\mathcal{L}^{\vee} = \mathcal{H}om(\mathcal{L},\underline{\mathbb{Z}})$; the untwisted case is the duality of *Poincaré Duality*, and the orientation sheaf is the local system attached to the representation of $\pi_1(M)$ by the sign of the monodromy on $H_n$.

## Cohomology with Support and Higher Direct Images

### Cohomology with Support

**Definition.** Let $\Phi$ be a family of closed subsets of $X$ closed under finite unions and under passage to closed subsets, such that every member of $\Phi$ has a closed neighbourhood in $\Phi$; the standard examples are the family of all closed subsets, the family of compact subsets when $X$ is locally compact and Hausdorff, and the family of closed subsets of a fixed closed set. For a sheaf $\mathcal{F}$, the group of **sections with support in $\Phi$** is

$$
\Gamma_\Phi(X,\mathcal{F}) = \{s \in \Gamma(X,\mathcal{F}) : \operatorname{Supp}s \in \Phi\},
$$

and the **cohomology with support in $\Phi$** is $H^i_\Phi(X,\mathcal{F}) = R^i\Gamma_\Phi(X,\mathcal{F})$. When $\Phi$ is the family of compact subsets of a locally compact space, one writes $H^i_c(X,\mathcal{F})$ and speaks of **cohomology with compact support**; when $\Phi$ is the family of closed subsets of a closed $Z \subseteq X$, one writes $H^i_Z(X,\mathcal{F})$.

**Theorem (the sequence of a closed subspace).** Let $i : Z \hookrightarrow X$ be the inclusion of a closed subset and $j : U = X\setminus Z \hookrightarrow X$ the inclusion of its complement. For every sheaf $\mathcal{F}$ on $X$ the sequence of sheaves on $X$

$$
0 \to j_!(\mathcal{F}|_U) \to \mathcal{F} \to i_*(\mathcal{F}|_Z) \to 0
$$

is exact, and the associated long exact sequence reads

$$
\cdots \to H^i_c(U,\mathcal{F}) \to H^i(X,\mathcal{F}) \to H^i(Z,\mathcal{F}|_Z) \to H^{i+1}_c(U,\mathcal{F}) \to \cdots,
$$

where the first group is the cohomology of $X$ with support in the family of closed subsets of $U$ that are compact and the last identification uses that $i_*$ is exact for a closed immersion and that $\Gamma(X,j_!(\mathcal{F}|_U)) = \Gamma_c(U,\mathcal{F})$.

*Proof.* The exactness of the sequence of sheaves is a stalk computation: at a point of $U$ the map $j_!(\mathcal{F}|_U)\to\mathcal{F}$ is an isomorphism and $i_*(\mathcal{F}|_Z)$ has zero stalk, while at a point of $Z$ the first sheaf has zero stalk and the second map is an isomorphism. The identification of the global sections of $j_!$ with the compactly supported sections and of those of $i_*$ with the sections of $\mathcal{F}|_Z$ is the universal property of extension by zero and of the direct image; applying $H^i(X,-)$ to the short exact sequence gives the long exact sequence through the identification $H^i(X,i_*(\mathcal{F}|_Z)) \cong H^i(Z,\mathcal{F}|_Z)$. $\square$

**Corollary (compactly supported duality).** For a closed oriented $n$-manifold $M$ and a local system $\mathcal{L}$ there is a **Poincaré duality with compact support**,

$$
H^k_c(M,\mathcal{L}) \cong H_{n-k}(M,\mathcal{L}^{\vee})^{\vee},
$$

which for the constant sheaf $\mathcal{L} = \underline{\mathbb{Z}}$ is the pairing of *Poincaré Duality* between compactly supported cohomology and homology; the identification of the top compactly supported group with $\mathbb{Z}$ for a connected $M$ is the existence of the fundamental class.

**Example.** For $M = S^n$ with the constant sheaf, $H^n_c(S^n,\underline{\mathbb{Z}}) = \mathbb{Z}$ and $H^i_c(S^n,\underline{\mathbb{Z}}) = 0$ otherwise; for $\mathbb{R}^n$, $H^n_c(\mathbb{R}^n,\underline{\mathbb{Z}}) = \mathbb{Z}$ and all other compactly supported groups vanish. Applying the sequence of the closed subspace to the inclusion of a point in $\mathbb{R}^n$ gives the local cohomology of the point, $H^n_{\{x\}}(\mathbb{R}^n,\underline{\mathbb{Z}}) = \mathbb{Z}$ and $H^i_{\{x\}}(\mathbb{R}^n,\underline{\mathbb{Z}}) = 0$ for $i \neq n$, in agreement with the local homology computed in *Poincaré Duality*.

### Higher Direct Images

**Definition.** Let $f : X \to Y$ be continuous. The **higher direct images** of a sheaf $\mathcal{F}$ on $X$ are the sheaves on $Y$

$$
R^q f_*\mathcal{F} = \text{the sheaf associated with } V \mapsto H^q(f^{-1}(V), \mathcal{F}),
$$

the **Leray presheaf** $\underline{H}^q(\mathcal{F}) : V \mapsto H^q(f^{-1}(V),\mathcal{F})$, whose sheafification defines $R^qf_*\mathcal{F}$; they form the derived functors of the left exact functor $f_*$, and $R^0f_* = f_*$.

**Theorem (the Leray spectral sequence).** For a continuous map $f : X \to Y$ and a sheaf $\mathcal{F}$ on $X$ there is a spectral sequence of cohomological type

$$
E_2^{p,q} = H^p(Y, R^qf_*\mathcal{F}) \Longrightarrow H^{p+q}(X,\mathcal{F}),
$$

natural in $f$ and $\mathcal{F}$. It is the Grothendieck spectral sequence of the composite $\Gamma(Y,-)\circ f_* = \Gamma(X,-)$, in the sense of *Spectral Sequences* of Part I, and its fibre-bundle case — the **Leray–Serre spectral sequence** with $E_2^{p,q} = H^p(B,\underline{H}^q(F;A))$ for a fibration $F \to E \to B$ — is the computational tool of *The Leray–Serre Spectral Sequence*. In particular, if $R^qf_*\mathcal{F} = 0$ for $q > 0$ then $H^p(Y,f_*\mathcal{F}) \cong H^p(X,\mathcal{F})$, the **Leray degeneration** used in the proof of the comparison with singular cohomology for a covering map.

*Proof.* The Grothendieck spectral sequence of the composite of the left exact functors $f_*$ and $\Gamma(Y,-)$ converges to the derived functors of the composite; the identification $R^q f_*\mathcal{F}$ with the sheafification of the Leray presheaf is the definition of the higher direct image as a sheaf, and the identification of the edge terms uses that $f_*$ is left exact. $\square$

**Example (a covering map).** Let $p : \tilde X \to X$ be a covering map of a locally contractible, locally connected space $X$ with discrete fibre $F$. Every point of $X$ has a basis of open neighbourhoods $V$ that are contractible and evenly covered, so $p^{-1}(V) \cong V\times F$; by the Künneth formula of *Cup and Cap Products* for a discrete factor, $H^q(p^{-1}(V),\underline{A}) \cong \prod_{F}H^q(V,\underline{A}) = 0$ for $q > 0$ since $V$ is contractible. Hence the Leray presheaf of $\underline{A}$ vanishes above degree $0$ and $R^qp_*\underline{A} = 0$ for $q > 0$, while $p_*\underline{A}$ is the local system of locally constant $A$-valued functions on $X$. The Leray degeneration gives

$$
H^p(X,p_*\underline{A}) \cong H^p(\tilde X,\underline{A}),
$$

which is the sheaf-theoretic Shapiro lemma for the covering, and for a finite covering of a connected $X$ is the spectral-sequence form of the transfer isomorphism of *The Fundamental Group and Covering Spaces*.

## Summary

Sheaf cohomology is the right derived functor of the global sections functor: $H^i(X,\mathcal{F}) = R^i\Gamma(X,\mathcal{F})$, defined by injective resolutions, which exist because the category of sheaves of abelian groups has enough injectives, exhibited by products of skyscraper sheaves over injective stalks. The general theory of derived functors, $\delta$-functors, dimension shifting and the long exact sequence is Part I's; this article supplies the topological instances: the long exact sequence of a short exact sequence of sheaves, the dimension-shifting isomorphisms, and the computability of cohomology from acyclic resolutions.

A sheaf is acyclic when its higher cohomology vanishes; flabby sheaves — those whose sections over any open set extend to the space — are acyclic, and every sheaf has a flabby resolution, the Godement resolution of discontinuous sections, so that flabby resolutions compute cohomology and the higher cohomology vanishes above the dimension of the space for Noetherian spaces. On paracompact spaces the soft sheaves, those whose sections over closed sets extend, are acyclic and include the fine sheaves, which possess partitions of unity; this is the mechanism by which the sheaf of continuous functions, the sheaf of smooth functions and the sheaves of differential forms become acyclic and compute the cohomology of their resolutions. For a locally contractible paracompact space the sheaf cohomology of the constant sheaf is singular cohomology, so the computations of the earlier articles of this Part are computations of sheaf cohomology, and the exponential sequence of $\mathbb{C}^*$ is the computation of $H^1(\mathbb{C}^*,\underline{\mathbb{Z}})$. Cohomology with support and with compact support, and the twisted Poincaré duality with local system coefficients, extend the theory to the relative setting; the higher direct images $R^qf_*$ organise the cohomology of the fibres of a map, and the Leray spectral sequence $E_2^{p,q} = H^p(Y,R^qf_*\mathcal{F}) \Rightarrow H^{p+q}(X,\mathcal{F})$, whose fibration case is the Leray–Serre sequence, is the principal structural tool that follows.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Gamma(X,-)$ | global sections functor; left exact, its right derived functors are sheaf cohomology |
| $H^i(X,\mathcal{F}) = R^i\Gamma(X,\mathcal{F})$ | sheaf cohomology, comma convention distinct from $H^i(X;G)$ |
| $\delta$ | connecting homomorphism of the long exact sequence |
| $\mathcal{I}$ | injective sheaf; $H^i(X,\mathcal{I}) = 0$ for $i > 0$ |
| flabby (flasque) | sections over open sets extend to $X$; flabby $\Rightarrow$ acyclic |
| $\mathcal{A}^{*}$, $\mathcal{G}^\bullet$ | sheaf of discontinuous sections; Godement flabby resolution |
| soft, fine | sections over closed sets extend; partitions of unity exist; fine $\Rightarrow$ soft $\Rightarrow$ acyclic |
| $\underline{A}$, $H^i(X,\underline{A})\cong H^i(X;A)$ | constant sheaf; comparison with singular cohomology |
| $\mathcal{L}$, $\mathcal{L}^{\vee}$ | local system and its dual; representation of $\pi_1$ |
| $\Gamma_\Phi$, $H^i_\Phi$, $H^i_c$ | sections and cohomology with support in a family; compact support |
| $R^qf_*$, $\underline{H}^q(\mathcal{F})$ | higher direct images; Leray presheaf |
| $E_2^{p,q} = H^p(Y,R^qf_*\mathcal{F})$ | Leray spectral sequence, converging to $H^{p+q}(X,\mathcal{F})$ |



## Further Reading

- Roger Godement, *Topologie algébrique et théorie des faisceaux* (Hermann, 1958), for the flabby resolution, the sheaf-theoretic foundations and the comparison with singular cohomology.
- Alexander Grothendieck, *Sur quelques points d'algèbre homologique* (Tohoku Mathematical Journal 9, 1957), for the derived functors, the existence of injectives and the vanishing theorem for finite-dimensional spaces.
- Glen E. Bredon, *Sheaf Theory* (Springer, second edition, 1997), for the systematic treatment of flabby, soft and fine sheaves and of cohomology with support.
- Alexandru Dimca, *Sheaves in Topology* (Springer, 2004), for the modern treatment with derived categories and local systems.
- Jean Leray, *L'anneau d'homologie d'une représentation* (Comptes Rendus de l'Académie des Sciences 222, 1946), for the original spectral sequence of a continuous map.
- Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology* (Springer, 1982), for the de Rham and Čech computations and the Leray spectral sequence in their geometric setting.
