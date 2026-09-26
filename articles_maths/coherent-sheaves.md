
# __Coherent Sheaves__

## Introduction

A sheaf of modules over the structure sheaf of a scheme is the algebraic analogue of a vector bundle with its sections: it is the object that the geometry of the scheme acts on, and on a general scheme the two classes that behave well are the quasi-coherent sheaves, which are locally modules over the coordinate rings, and the coherent sheaves, which are locally finitely generated. The distinction matters as soon as the base ring is not Noetherian, and the abelian-category properties that hold for one class fail for the other, so both are defined here and the hypotheses are stated at every theorem. The sheaves themselves, the equivalence with modules on an affine scheme and the cohomology of the twisting sheaves on projective space have been used in *Sheaves in Algebraic Geometry*; the present article develops the theory on a general scheme, where the affine description is no longer available, and concentrates on the four structures that make the theory work: the exactness and the non-exactness of the operations, the glueing of sheaves by descent, the cohomology and its finiteness properties under a proper morphism, and the derived functors relating the global cohomology of a sheaf to the local Ext sheaves.

The organising theorems are these. On an affine scheme the category of quasi-coherent sheaves is equivalent to the category of modules over the ring, and the global sections functor is exact; already on the projective line this fails, and the failure is measured by the cohomology groups $H^i(X,\mathcal{F})$, which are the right derived functors of global sections of *Derived Functors and Sheaf Cohomology*. For a coherent sheaf on a projective scheme over a Noetherian ring the cohomology is finitely generated, vanishes above the relative dimension, and vanishes in positive degree after twisting — the finiteness, vanishing and Serre theorems. For a proper morphism of locally Noetherian schemes the higher direct images of a coherent sheaf are coherent, which is the **finiteness theorem** of Grothendieck and the scheme-theoretic form of the finiteness of the cohomology of the fibres of a fibration; and the derived restrictions of the finiteness theorem — the base change theorem, the semicontinuity of the cohomology of the fibres, the projection formula — are what make the cohomology of a family a tool for the study of the family. The Ext groups of sheaves are related to the cohomology by the local-to-global spectral sequence, and the duality theory of *Sheaves in Algebraic Geometry* is the case of a smooth projective morphism.

Two boundaries are stated at once. The homological algebra — derived functors, spectral sequences, Ext and Tor, derived categories, the abelian and Grothendieck categories, and the sheaves on sites with their descent theory — is Part I's, in *Homological Algebra*, *Derived Functors*, *Spectral Sequences*, *Derived Categories*, *Abelian and Grothendieck Categories*, *Sheaves on Sites* and *Descent Theory*; the present article is the geometric instance, and the general theorems are cited rather than reproved. The vector-bundle side — locally free sheaves, their transition functions, connections and curvature, and the characteristic classes that live on them — is the written *Fibre Bundles, Connections and Curvature*, whose notation for a bundle and a connection is not repeated here. The chain of articles of this category — *Presheaves and Sheaves*, *Sheaf Cohomology*, *Čech Cohomology*, *Derived Functors and Sheaf Cohomology*, *Sheaves and the de Rham Complex*, *Sheaves in Algebraic Geometry* — supplies the topological theory that is compared with the algebraic one throughout.

## Quasi-Coherent and Coherent Sheaves

**Definition.** Let $(X,\mathcal{O}_X)$ be a scheme. An $\mathcal{O}_X$-**module** is a sheaf $\mathcal{F}$ of abelian groups with a multiplication $\mathcal{O}_X(U)\times\mathcal{F}(U)\to\mathcal{F}(U)$ making each $\mathcal{F}(U)$ a module over the ring $\mathcal{O}_X(U)$ compatibly with restriction. A morphism of $\mathcal{O}_X$-modules is a morphism of sheaves compatible with the multiplications; the category is abelian with kernels, cokernels and images formed on sections, by *Presheaves and Sheaves*. An $\mathcal{O}_X$-module $\mathcal{F}$ is:

1. **quasi-coherent** if every point of $X$ has an affine open neighbourhood $U = \operatorname{Spec} A$ with $\mathcal{F}|_U\cong\widetilde M$ for an $A$-module $M$;
2. **of finite type** if in addition every point has an affine neighbourhood on which $\mathcal{F}|_U$ is a quotient of a finite free $\mathcal{O}_U$-module;
3. **coherent** if it is of finite type and for every open $U$ and every morphism $\mathcal{O}_U^n\to\mathcal{F}|_U$ the kernel is of finite type;
4. **locally free** of rank $r$ if every point has a neighbourhood $U$ with $\mathcal{F}|_U\cong\mathcal{O}_U^r$.

The categories are written $\mathbf{QCoh}(X)$, $\mathbf{Coh}(X)$, and $\mathbf{Mod}(\mathcal{O}_X)$ for all modules.

**Theorem (coherence and finite type).** Let $X$ be a scheme.

1. $\mathbf{QCoh}(X)$ is an abelian subcategory of $\mathbf{Mod}(\mathcal{O}_X)$ closed under kernels, cokernels, images, extensions, direct sums, tensor products over $\mathcal{O}_X$ and under the inverse image functor $f^*$ for every morphism $f : X'\to X$.
2. If $X$ is locally Noetherian, the coherent sheaves are exactly the quasi-coherent sheaves of finite type, $\mathbf{Coh}(X)$ is abelian and closed under the same operations, and the sheaf hom $\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F},\mathcal{G})$ of two coherent sheaves is coherent; without the Noetherian hypothesis the kernel of a morphism of finite-type sheaves need not be of finite type, which is exactly what the definition of coherence above is designed to exclude.
3. If $X$ is Noetherian, a quasi-coherent sheaf is coherent if and only if it is of finite type, and every quasi-coherent sheaf is the filtered colimit of its coherent subsheaves.

*Proof.* Local on $X$, so reduce to $X = \operatorname{Spec} A$: the statements become the corresponding statements for $A$-modules under the equivalence of categories, together with the exactness of the localisation, and (2)'s counterexample is the classical one of a non-finitely-generated kernel over a non-Noetherian ring. (3) every quasi-coherent sheaf on a Noetherian scheme is the filtered colimit of its coherent subsheaves, since a module over a Noetherian ring is the filtered union of its finitely generated submodules and the finitely generated submodules generate finitely generated ones under localisation. $\square$

**Example (the ideal sheaf and the conormal sheaf).** For a closed subscheme $i : Z\to X$ defined by a sheaf of ideals $\mathcal{I}\subseteq\mathcal{O}_X$, the sheaf $\mathcal{I}$ is quasi-coherent, and it is coherent when $X$ is locally Noetherian; the quotient $i^*\mathcal{I} = \mathcal{I}/\mathcal{I}^2$ is the **conormal sheaf** of $Z$ in $X$, a quasi-coherent sheaf on $Z$ whose dual, when $Z$ is smooth inside a smooth $X$, is the normal bundle. The cotangent sheaf of a smooth $k$-scheme of dimension $d$ is locally free of rank $d$, and its top exterior power is the canonical sheaf $\omega_X$ of *Sheaves in Algebraic Geometry*; a locally free sheaf of rank $r$ is the sheaf of sections of a vector bundle in the sense of the written *Fibre Bundles, Connections and Curvature*, and the two languages — a locally free sheaf and a vector bundle with its transition functions — are equivalent, an equivalence stated once and used without remark in the rest of the article.

**Example (a coherent sheaf that is not locally free).** On $X = \operatorname{Spec} k[x,y]$ the ideal sheaf $(x,y)$ is coherent and not locally free: it has rank one at the generic point and its fibre at the origin is two-dimensional. The example is the reason the theory of coherent sheaves is not the theory of vector bundles: the rank of a coherent sheaf is defined only at the points where it is locally free, and the locus where a coherent sheaf is locally free of a given rank is open but not closed, the failure being measured by the local Ext sheaves of the next sections.

**Remark (the module side).** On $X = \operatorname{Spec} A$ the functor $M\mapsto\widetilde M$ is an equivalence of categories from $A$-modules to quasi-coherent sheaves, exact and commuting with tensor products and homs, and the coherent sheaves correspond to the finitely generated modules when $A$ is Noetherian, as in *Sheaves in Algebraic Geometry*; the whole content of the present article is therefore invisible on an affine scheme, and its theorems are statements about what happens when the affine charts are glued. The general statement of the passage from local to global for sheaves of modules is the descent theorem of Part I's *Descent Theory*: quasi-coherent sheaves form a stack on the Zariski site of $X$, so that specifying one is the same as specifying modules on the charts together with the descent datum, the compatibility isomorphisms over the overlaps satisfying the cocycle condition.

## Glueing and the Graded Case

**Theorem (glueing of sheaves).** Let $X$ be a scheme with affine charts $U_i = \operatorname{Spec} A_i$ and intersections $U_{ij} = U_i\cap U_j = \operatorname{Spec} A_{ij}$, the $A_{ij}$ being the localisations of the $A_i$. The data of a quasi-coherent sheaf $\mathcal{F}$ on $X$ are equivalent to the data of $A_i$-modules $M_i$ with isomorphisms $\varphi_{ij} : M_i\otimes_{A_i}A_{ij}\to M_j\otimes_{A_j}A_{ij}$ satisfying $\varphi_{ii} = \mathrm{id}$ and the cocycle condition $\varphi_{ik} = \varphi_{jk}\circ\varphi_{ij}$ on the triple overlaps. The same statement holds for coherent sheaves with finitely generated modules, and for locally free sheaves with the $M_i$ free.

*Proof.* Given $\mathcal{F}$, take $M_i = \Gamma(U_i,\mathcal{F})$, and the $\varphi_{ij}$ are the comparison isomorphisms on the overlaps, which satisfy the cocycle condition because restriction maps do. Conversely, given the data, glue the sheaves $\widetilde{M_i}$ on the $U_i$ by the glueing lemma for sheaves, the cocycle condition being exactly the compatibility required; the resulting sheaf is an $\mathcal{O}_X$-module, and it is quasi-coherent because it is locally isomorphic to the $\widetilde{M_i}$. $\square$

**Theorem (the graded case).** Let $S$ be a graded ring, $X = \operatorname{Proj} S$, and $M$ a graded $S$-module. Then there is a quasi-coherent sheaf $\widetilde M$ on $X$ with $\widetilde M|_{D_+(f)} = (M_f)_0$ for homogeneous $f$, the assignment is exact and takes the shifted modules $M(d)$ to the twists $\widetilde M(d)$, and:

1. the functor $M\mapsto\widetilde M$ is essentially surjective onto the quasi-coherent sheaves and its kernel is the category of graded modules whose localisation vanishes, the **torsion** graded modules of $X$;
2. if $S$ is Noetherian and $M$ is finitely generated then $\widetilde M$ is coherent, and every coherent sheaf on the projective scheme $\operatorname{Proj} S$ arises this way from a finitely generated graded module;
3. consequently the coherent sheaves on a projective scheme over a Noetherian ring are the finitely generated graded modules modulo the torsion ones, and the cohomology of $\widetilde M$ is computed from the graded module by the Čech complex of the standard cover.

*Proof.* Local on the $D_+(f)$, where the construction is the affine one of the localisation of a graded module; the exactness of localisation gives the exactness of the assignment, and the identification of the kernel with the torsion modules is the theorem that a graded module whose localisations at all homogeneous $f$ vanish is torsion. (2) is the graded Hilbert basis theorem, Part I's *Noetherian and Artinian Rings*, together with the finite generation of the submodule of the relations. (3) assembles (1) and (2) and applies the Čech computation of *Sheaves in Algebraic Geometry*. $\square$

**Example (the twisting sheaves as the universal case).** For $S = A[x_0,\ldots,x_n]$ and $M = S(d)$ one recovers the twisting sheaves $\mathcal{O}(d)$ with the cohomology computed in *Sheaves in Algebraic Geometry*: $H^0 = S_d$, $H^i = 0$ for $0<i<n$, and $H^n$ dual to $S_{-d-n-1}$, the ranks being the binomial coefficients $\binom{d+n}{n}$ and $\binom{-d-1}{n}$. The computation is the basic case from which the cohomology of any coherent sheaf on projective space is obtained, since every such sheaf has a finite resolution by finite direct sums of twisting sheaves — the graded Hilbert syzygy theorem — and the cohomology is then computed by a spectral sequence of a double complex, as in *Derived Functors and Sheaf Cohomology*.

## Cohomology and its Finiteness

**Definition.** Let $\mathcal{F}$ be an $\mathcal{O}_X$-module. The **cohomology** of $\mathcal{F}$ is

$$
H^i(X,\mathcal{F}) = R^i\Gamma(X,-)(\mathcal{F}),
$$

the right derived functors of the global sections functor, so that $H^0(X,\mathcal{F}) = \Gamma(X,\mathcal{F})$ and there is a long exact sequence in $i$ for every short exact sequence of sheaves, as in *Sheaf Cohomology*. For a morphism $f : X\to Y$ the **higher direct images** are the sheaves associated with the presheaves

$$
U\mapsto H^i(f^{-1}U,\mathcal{F}), \qquad R^if_*\mathcal{F} = \mathcal{O}_Y\text{-module associated with } \bigl(U\mapsto H^i(f^{-1}U,\mathcal{F})\bigr),
$$

and they are quasi-coherent when $\mathcal{F}$ is, for $f$ quasicompact and quasiseparated; the Leray spectral sequence $E_2^{p,q} = H^p(Y,R^qf_*\mathcal{F})\Rightarrow H^{p+q}(X,\mathcal{F})$ is that of *Derived Functors and Sheaf Cohomology*.

**Theorem (the Čech computation on a separated scheme).** Let $X$ be a separated scheme, $\mathcal{U} = \{U_i\}$ an affine open cover and $\mathcal{F}$ a quasi-coherent sheaf on $X$. Then the Čech complex

$$
\check C^\bullet(\mathcal{U},\mathcal{F}) : \prod_i\mathcal{F}(U_i)\to\prod_{i,j}\mathcal{F}(U_i\cap U_j)\to\cdots
$$

computes the cohomology: $\check H^i(\mathcal{U},\mathcal{F})\cong H^i(X,\mathcal{F})$ for all $i$. Consequently the cohomology of a quasi-coherent sheaf on a separated scheme is computed by an explicit complex of modules, and for a separated scheme of finite type over a Noetherian ring the cohomology groups are finitely generated when $\mathcal{F}$ is coherent.

*Proof.* The intersections $U_{i_0\cdots i_p}$ are affine, since $X$ is separated and the intersection of affines in a separated scheme is affine; a quasi-coherent sheaf on an affine scheme has no higher cohomology by the affine vanishing theorem of *Sheaves in Algebraic Geometry*, so $\mathcal{F}$ is acyclic on every intersection and the Leray theorem of *Čech Cohomology* applies to the cover. The finite generation follows because the Čech complex is then a finite complex of finitely generated modules over a Noetherian ring in the presence of a finite affine cover. $\square$

**Theorem (finiteness and vanishing).** Let $f : X\to Y$ be a proper morphism of locally Noetherian schemes and $\mathcal{F}$ a coherent sheaf on $X$.

1. **Finiteness theorem** (Grothendieck): the higher direct images $R^if_*\mathcal{F}$ are coherent $\mathcal{O}_Y$-modules for all $i$, and $R^if_*\mathcal{F} = 0$ for $i>d$, where $d$ is the supremum of the dimensions of the fibres of $f$.
2. **Serre's vanishing theorem**: if $f$ is projective, with $\mathcal{O}_X(1)$ a relatively ample invertible sheaf, then there is $d_0$ with $R^if_*(\mathcal{F}(d)) = 0$ for all $i>0$ and $d\geq d_0$.
3. **Base change**: for a cartesian square with $g : Y'\to Y$ flat, or with $Y$ the spectrum of a local ring and $Y'$ its residue field, the natural maps $g^*R^if_*\mathcal{F}\to R^if'_*(g'^*\mathcal{F})$ are isomorphisms for all $i$; more generally there is a base-change spectral sequence.
4. **Semicontinuity**: the function $y\mapsto\dim_{\kappa(y)}H^i(X_y,\mathcal{F}_y)$ is upper semicontinuous for each $i$ when $f$ is proper and $\mathcal{F}$ coherent, and it is locally constant when the base-change maps are isomorphisms.

*Proof.* (1) reduces to the projective case by Chow's lemma and the fact that a proper morphism is dominated by a projective one, and then to the computation of the cohomology of the twisting sheaves via the Čech complex of the theorem above; the vanishing above the relative dimension is the length of that complex. (2) is the graded Hilbert syzygy theorem together with the same computation. (3) and (4) are the standard consequences of (1) and (2) with the base-change spectral sequence of *Derived Functors and Sheaf Cohomology*; the upper semicontinuity is the statement that the dimensions can only jump up on closed subsets, the jump being governed by the connecting homomorphisms. $\square$

**Remark (the relation to the topological theory).** Every statement of this section is the algebraic counterpart of a statement about sheaves on a topological space: the Leray spectral sequence is the same sequence, the finiteness theorem corresponds to the finiteness of the cohomology of a proper map of locally compact spaces, the base change theorem to the continuity of the cohomology of the fibres, and the semicontinuity to the same phenomenon for a family of spaces. What differs is the source of the finiteness: in the topological case it comes from compactness and from the local structure of the space, in the algebraic case from the Noetherian hypothesis and from the explicit Čech computation with twisting sheaves. The comparison for a complex variety between the algebraic cohomology of a coherent sheaf and the cohomology of the associated analytic sheaf is the theorem of GAGA, whose analytic side requires the theory of Part III.

## Ext and the Local-to-Global Spectral Sequence

**Definition.** Let $\mathcal{F},\mathcal{G}$ be $\mathcal{O}_X$-modules. The **Ext sheaves** are the right derived functors of the sheaf hom,

$$
\mathcal{E}xt^i_{\mathcal{O}_X}(\mathcal{F},\mathcal{G}) = R^i\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F},-)(\mathcal{G}),
$$

and the **Ext groups** are the right derived functors of the hom functor on the abelian category of $\mathcal{O}_X$-modules,

$$
\operatorname{Ext}^i_{\mathcal{O}_X}(\mathcal{F},\mathcal{G}) = R^i\operatorname{Hom}_{\mathcal{O}_X}(\mathcal{F},-)(\mathcal{G}),
$$

both of which exist because the categories have enough injectives, as in Part I's *Derived Functors* and *Homological Algebra*.

**Theorem (the local-to-global spectral sequence).** For $\mathcal{O}_X$-modules $\mathcal{F},\mathcal{G}$ with $\mathcal{F}$ of finite type over a locally Noetherian $X$ there is a convergent spectral sequence

$$
E_2^{p,q} = H^p\bigl(X,\mathcal{E}xt^q_{\mathcal{O}_X}(\mathcal{F},\mathcal{G})\bigr)\Longrightarrow\operatorname{Ext}^{p+q}_{\mathcal{O}_X}(\mathcal{F},\mathcal{G}),
$$

natural in both variables. In particular there is an exact sequence

$$
0\to H^1\bigl(X,\mathcal{H}om(\mathcal{F},\mathcal{G})\bigr)\to\operatorname{Ext}^1(\mathcal{F},\mathcal{G})\to H^0\bigl(X,\mathcal{E}xt^1(\mathcal{F},\mathcal{G})\bigr)\to H^2(X,\mathcal{H}om(\mathcal{F},\mathcal{G}))\to\cdots,
$$

so that the obstruction to extending a homomorphism lies partly in the global sections of the local Ext sheaf and partly in the first cohomology of the sheaf hom. When $\mathcal{F}$ is locally free the $\mathcal{E}xt^q$ vanish for $q>0$ and the spectral sequence collapses to the isomorphism $\operatorname{Ext}^i(\mathcal{F},\mathcal{G})\cong H^i(X,\mathcal{F}^\vee\otimes\mathcal{G})$.

*Proof.* The functor $\mathcal{H}om(\mathcal{F},-)$ takes injectives to injectives when $\mathcal{F}$ is of finite type over a locally Noetherian scheme, and the Grothendieck spectral sequence for the composite $\operatorname{Hom}(\mathcal{F},-)\cong\Gamma(X,\mathcal{H}om(\mathcal{F},-))$ is the stated sequence, by *Derived Functors and Sheaf Cohomology*. The local vanishing for locally free $\mathcal{F}$ is the exactness of $\mathcal{H}om(\mathcal{F},-)$ in that case. $\square$

**Corollary (Serre duality as an Ext statement).** Let $X$ be a smooth projective scheme of dimension $n$ over a field and $\omega_X$ its canonical sheaf. Then

$$
H^i(X,\mathcal{F})^{\vee}\cong\operatorname{Ext}^{n-i}_{\mathcal{O}_X}(\mathcal{F},\omega_X)
$$

for coherent $\mathcal{F}$, and the local Ext sheaves vanish for $q>0$ when $\mathcal{F}$ is locally free, so that the duality of *Sheaves in Algebraic Geometry* is the collapse of the local-to-global sequence in the smooth case. The general statement, in which $\omega_X$ is replaced by the dualising complex of a proper morphism, is Grothendieck duality and requires the derived category of Part I's *Derived Categories* and *Derived Functors*; the topological model of the same phenomenon is Verdier duality, recorded in *Derived Functors and Sheaf Cohomology*.

**Remark (deformations).** The Ext groups are the natural home of deformation theory: for a coherent sheaf $\mathcal{F}$ on a scheme $X$ and a square-zero extension of the base by an ideal $I$, the deformations of $\mathcal{F}$ are a torsor under $\operatorname{Ext}^1$, the obstructions lie in $\operatorname{Ext}^2$, and the infinitesimal automorphisms are $\operatorname{Ext}^0 = \operatorname{Hom}(\mathcal{F},\mathcal{F})$; for a subscheme $Z\subseteq X$ the tangent space to the Hilbert scheme at $Z$ is $H^0(Z,\mathcal{N}_{Z/X})$ and the obstructions are in $H^1(Z,\mathcal{N}_{Z/X})$, with $\mathcal{N}$ the normal sheaf. The formal theory of these statements belongs to Part I's *Deformation Theory*; their geometric application, the construction of the spaces that parametrise the objects, belongs .

## Summary

A quasi-coherent sheaf on a scheme is a sheaf of modules that is locally the sheaf associated with a module over the coordinate ring of an affine chart, and a coherent sheaf is a quasi-coherent sheaf of finite type with the additional requirement that its sheaf of relations is of finite type as well. On a locally Noetherian scheme the two notions of coherence and finite type agree, the coherent sheaves form an abelian subcategory closed under kernels, cokernels, extensions and tensor products, and the sheaf hom of two coherent sheaves is coherent; over a general base the kernel of a morphism of finite-type sheaves need not be of finite type, which is precisely what the definition of coherence is designed to exclude. On an affine scheme the theory collapses to the module theory: the quasi-coherent sheaves are the modules, the global sections functor is exact and the higher cohomology vanishes. The content of the general theory is the glueing: quasi-coherent sheaves on a scheme are the descent data of modules on the affine charts, and on a projective scheme the coherent sheaves are the finitely generated graded modules modulo the torsion ones, so that the computation of cohomology reduces to the Čech complex of the standard cover and to the cohomology of the twisting sheaves.

The cohomology of a quasi-coherent sheaf is the derived functor of global sections, and on a separated scheme it is computed by the Čech complex of any affine open cover, the affines being acyclic. For a coherent sheaf under a proper morphism of locally Noetherian schemes the higher direct images are coherent, vanish above the relative dimension of the fibres and vanish in positive degree after twisting, and the base-change theorem and the upper semicontinuity of the dimensions of the cohomology of the fibres make the cohomology of a family a well-behaved tool; these statements are the algebraic counterparts of the finiteness and continuity theorems for the cohomology of the fibres of a proper map of spaces. The Ext sheaves and the Ext groups of sheaves are related by the local-to-global spectral sequence, whose collapse for locally free coefficients gives the identification of the Ext groups with the cohomology of the tensor product and whose smooth projective case is Serre duality; the deformations of a sheaf are governed by $\operatorname{Ext}^1$ and obstructed by $\operatorname{Ext}^2$, and the application of the same machinery to the construction of the parametrising spaces is the theory .

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{O}_X$-module | sheaf of modules over the structure sheaf |
| $\mathbf{QCoh}(X)$, $\mathbf{Coh}(X)$ | quasi-coherent sheaves; coherent sheaves |
| $\mathcal{F}$ of finite type | locally a quotient of a finite free module |
| coherent | finite type with finitely generated kernels of maps from free modules |
| $\widetilde M$ | sheaf associated with a module $M$ over an affine chart |
| $f^*\mathcal{F}$, $f_*\mathcal{F}$, $R^if_*\mathcal{F}$ | inverse and direct image; higher direct images |
| $H^i(X,\mathcal{F}) = R^i\Gamma(X,-)(\mathcal{F})$ | cohomology of a sheaf |
| $\check C^\bullet(\mathcal{U},\mathcal{F})$ | Čech complex; $\check H^i\cong H^i$ for separated $X$ and affine $\mathcal{U}$ |
| $\mathcal{O}_X(1)$, $\mathcal{F}(d)$ | relatively ample invertible sheaf; twist |
| $\mathcal{E}xt^i$, $\operatorname{Ext}^i$ | Ext sheaves and Ext groups of $\mathcal{O}_X$-modules |
| $\mathcal{H}om$ | sheaf hom; $\mathcal{F}^\vee = \mathcal{H}om(\mathcal{F},\mathcal{O}_X)$ |
| $\mathcal{I}$, $\mathcal{N}_{Z/X}$ | ideal sheaf; normal sheaf of a subscheme |



## Further Reading

- Alexander Grothendieck and Jean Dieudonné, *Éléments de géométrie algébrique III, IV* (Publications Mathématiques de l'IHÉS, 1961–1967), for the finiteness, base-change and semicontinuity theorems.
- Robin Hartshorne, *Algebraic Geometry* (Springer, 1977), for quasi-coherent and coherent sheaves, the Čech computation and the cohomological theorems on projective schemes.
- Jean-Pierre Serre, *Faisceaux algébriques cohérents* (Annals of Mathematics 61, 1955), for the original coherent-sheaf theory and the vanishing theorem.
- Robin Hartshorne, *Residues and Duality* (Springer, 1966), for Ext of sheaves, the local-to-global sequence and Grothendieck duality.
- Amnon Neeman, *Triangulated Categories* (Princeton, 2001), for the derived-category setting of the finiteness and base-change theorems.
- Alexander Grothendieck, *Technique de descente et théorèmes d'existence en géométrie algébrique* (Séminaire Bourbaki, 1959–1962), for the descent theory of quasi-coherent sheaves.
