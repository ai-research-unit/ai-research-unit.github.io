
# __Low-Dimensional Topology__

## Introduction

Low-dimensional topology is the topology of manifolds of dimension two, three and four, where the general machinery of surgery and handle cancellation that classifies manifolds in high dimensions breaks down and where the phenomena are correspondingly richer. In dimension two the classification is complete and elementary; in dimension three the classification was completed by Thurston's geometrisation theorem, proved by Perelman, so that every closed three-manifold is assembled from pieces carrying one of eight model geometries; in dimension four neither classification nor uniqueness holds in the smooth category — a fixed topological manifold may carry infinitely many smooth structures, and $\mathbb{R}^4$ is the only Euclidean space with this property — while the topological classification of simply connected four-manifolds is known by the theorems of Freedman, and the smooth classification is obstructed by the gauge-theoretic invariants of Donaldson and Seiberg–Witten.

The article develops the four strata in order. The classification of surfaces is recalled for the language it supplies — genus, Euler characteristic, connected sum, boundary — and the uniformisation of surfaces is cited to *Hyperbolic Geometry*. The prime decomposition of three-manifolds and the torus decomposition reduce the study of a three-manifold to its Seifert fibred and hyperbolic pieces, and the eight geometries of Thurston organise the closed case; the statements of geometrisation, the spherical space form problem and the Poincaré conjecture are given, together with the hyperbolic Dehn surgery theorem and the rigidity phenomena that make the hyperbolic pieces computable. The Heegaard splittings and the surgery descriptions of three-manifolds supply the combinatorial models in which computations are made. Four-manifolds enter through their intersection forms, whose algebraic classification, combined with the theorems of Freedman and Donaldson, gives simultaneously the topological classification in the simply connected case and the obstruction to smoothing it. The article closes with the exotic phenomena — exotic smooth structures on $\mathbb{R}^4$ and on other four-manifolds, and the failure of the $h$-cobordism theorem in dimension four — that make the dimension-four theory exceptional.

**The boundaries of the article.** Hyperbolic geometry, the models $\mathbb{H}^n$ and the volume computations of hyperbolic manifolds are those of *Hyperbolic Geometry*, and the hyperbolic 3-manifolds of this article are built on it. Surfaces and their mapping class groups are those of *Mapping Class Groups*, the final article of this half; the Teichmüller spaces of their complex structures are not developed in this Part, and the moduli-theoretic facts are taken as standard. Knots, their invariants and their complements are those, and the lens spaces of the classification are those of *Lens Spaces*, both of which follow. The cobordism groups, the surgery exact sequence and the $h$-cobordism theorem are those; the four-dimensional phenomena are stated here and the general theory is there. The symplectic and contact structures on three- and four-manifolds, and the tight–overtwisted dichotomy, are those of *Symplectic and Contact Topology*; the Floer-theoretic invariants — the instanton, Heegaard Floer and contact homologies — are those of *Floer Homology*, and are used here as statements. The homology, cohomology, intersection forms, cup products and the homology of cell complexes are those of *Algebraic Topology*, being written by another agent. The Sobolev and elliptic analysis behind the gauge-theoretic invariants, the Ricci flow and the analytic content of geometrisation belong to Part III, where the measure and the limit are available; the results are stated and cited. Lie groups and homogeneous spaces are those of Part I. No physics is invoked.

## Surfaces

**Theorem (classification of compact surfaces).** Every compact connected surface is homeomorphic to exactly one of:

**(a)** the sphere $S^2$; the connected sums $T^2\#\cdots\# T^2$ of $g$ copies of the torus, $g\geq1$ (**orientable of genus $g$**); the connected sum $\mathbb{RP}^2\#\cdots\#\mathbb{RP}^2$ of $k$ copies of the projective plane, $k\geq1$ (**non-orientable of genus $k$**); and the compact surfaces with boundary are the closed surfaces with finitely many open discs removed.

The invariants are the orientability, the Euler characteristic $\chi$, the number of boundary components $b$ and the genus, related by

$$
\chi = 2 - 2g - b \quad\text{(orientable)}, \qquad \chi = 2 - k - b \quad\text{(non-orientable)} .
$$

**Proof sketch.** A triangulated surface is reduced by cutting along non-separating curves and collapsing the resulting discs; the reduction terminates because each cut lowers $-3\chi$ or the number of simplices, and the normal form is reached. The uniqueness follows from the classification of the fundamental groups or from the Euler characteristic together with orientability and the boundary count. $\square$

**Theorem (uniformisation of surfaces).** Every compact connected surface without boundary admits a complete Riemannian metric of constant curvature $+1$, $0$ or $-1$, according to the sign of $\chi$: the sphere and the projective plane have $\chi>0$ and carry the spherical geometry, the torus and the Klein bottle have $\chi=0$ and carry the Euclidean geometry, and all the remaining surfaces have $\chi<0$ and carry a hyperbolic structure; the structure is unique up to isometry only in the spherical case, while the hyperbolic structures on a surface of genus $g$ form the Teichmüller space of real dimension $6g-6$, and the flat structures on the torus form a two-dimensional family as well.

**Proof sketch.** The statement is that of *Hyperbolic Geometry*, where the hyperbolic structures are constructed by realising the surface as the quotient of $\mathbb{H}^2$ by a discrete group of isometries; the existence is the uniformisation theorem, each conformal class on a surface of negative Euler characteristic containing exactly one complete hyperbolic metric, and the hyperbolic case is the one in which the analogue of Mostow rigidity fails, so that the metrics of a fixed topology form the Teichmüller space. $\square$

**Remark.** The terminology of the surface theory — genus, connected sum, boundary components, Euler characteristic, incompressible curves — is the language in which the higher-dimensional theory is stated, and the classification above is the model that the three- and four-dimensional classifications generalise incompletely. In dimension three the analogue of the genus is defeated: Mostow rigidity makes the hyperbolic structure of a closed manifold unique, so that the geometry is determined by the fundamental group and the volume is a topological invariant, while the topological type is not determined by the homology; in dimension four the analogue fails outright in the smooth category.

## Three-Manifolds: Prime Decomposition and the Torus Decomposition

**Definition.** A connected sum decomposition $M\cong M_1\# M_2$ is **trivial** if one factor is $S^3$. A closed three-manifold is **prime** if it is not $S^3$ and every connected sum decomposition is trivial. A three-manifold is **irreducible** if every embedded $2$-sphere bounds a ball; irreducible implies prime, and the only prime manifold that is not irreducible is $S^2\times S^1$.

**Theorem (Kneser; Milnor; prime decomposition).** Every compact oriented three-manifold $M$ is a connected sum

$$
M \cong P_1\#\cdots\# P_k
$$

of prime manifolds, and the collection $\{P_i\}$ is unique up to order and homeomorphism. A prime manifold with finite fundamental group is a spherical space form; the remaining prime manifolds are either Seifert fibred or hyperbolic, and this is the trichotomy of the geometrisation theorem below.

**Proof sketch.** Existence is Kneser's argument: a maximal collection of disjoint non-parallel essential $2$-spheres has a complement that is a union of punctured prime manifolds, and the decomposition is obtained by filling the boundary spheres with balls. Uniqueness is the theorem of Milnor, proved by an analysis of the fundamental group and its actions on trees, with the refinement that the splitting is detected by the Grushko decomposition of $\pi_1$ together with the peripheral structure. $\square$

**Theorem (Jaco–Shalen, Johannson; the torus decomposition).** Let $M$ be a compact oriented irreducible three-manifold. There is a canonical (up to isotopy) minimal collection of disjoint incompressible tori that splits $M$ into pieces that are either **atoroidal** — every essential torus is boundary-parallel — or **Seifert fibred**. The decomposition is unique, and it is natural with respect to homeomorphism.

**Proof sketch.** The tori in the decomposition are characterised by the property that they carry a nontrivial annulus or torus in the complement; the proof proceeds by the theory of the characteristic submanifold, in which the splitting tori form the boundary of the maximal Seifert fibred submanifold, and the uniqueness is a consequence of the uniqueness of the characteristic submanifold. $\square$

**Definition.** A **Seifert fibred space** is a three-manifold that is a union of disjoint circles — the fibres — with a local model of a solid torus fibred by curves of slope $p/q$ about the core, so that the manifold is the total space of a fibration over a surface with finitely many exceptional fibres. A Seifert fibred space is classified by its base orbifold, its multiplicity tuple $(p_1,q_1),\ldots,(p_k,q_k)$ and the Euler number of the fibration.

**Theorem (classification of Seifert fibred spaces).** Two closed orientable Seifert fibred spaces with infinite fundamental group are homeomorphic if and only if their Seifert fibration data agree up to the obvious equivalences; the finite fundamental group cases are the spherical space forms, classified by the same data together with the classification of the free actions of finite groups on $S^3$. In particular the geometric Seifert fibred spaces carry one of the six geometries $S^3$, $E^3$, $S^2\times\mathbb{R}$, $H^2\times\mathbb{R}$, $\widetilde{SL_2(\mathbb{R})}$ and $\mathrm{Nil}$; the two remaining geometries of the list, $H^3$ and $\mathrm{Sol}$, are not carried by Seifert fibred spaces.

**Proof sketch.** The classification reduces to the classification of circle actions on three-manifolds, which is the classification of the associated orbifold data; the geometric statements are read off from the possible total spaces of the six Seifert fibred geometries. $\square$

**Example.** The lens spaces $L(p,q)$ — the quotients of $S^3$ by the free cyclic action of order $p$ — are Seifert fibred over $S^2$ with at most two exceptional fibres and carry the spherical geometry; their classification, their fundamental groups and their role in the classification of free group actions are the subject of *Lens Spaces*. The three-torus $T^3$ is Seifert fibred in many ways and carries the Euclidean geometry; $S^2\times S^1$ is Seifert fibred and carries the $S^2\times\mathbb{R}$ geometry; the unit tangent bundle of a hyperbolic surface is Seifert fibred and carries the $\widetilde{SL_2(\mathbb{R})}$ geometry; the Heisenberg nilmanifold is Seifert fibred, carries $\mathrm{Nil}$ and is the model for the Kodaira–Thurston manifold of *Kähler Geometry*.

## Geometrisation and the Eight Model Geometries

**Definition.** A **model geometry** is a pair $(X,G)$ of a simply connected Riemannian manifold $X$ and a Lie group $G$ acting transitively on $X$ with compact point stabilisers, such that $G$ is maximal among the groups acting thus; a three-manifold is **geometric** if it is the quotient of $X$ by a discrete subgroup of $G$ acting freely and properly discontinuously. There are exactly eight maximal model geometries in dimension three:

| Geometry | $X$ | $\dim$ of the isometry group | Examples |
|---|---|---|---|
| $S^3$ | $S^3$ | 6 | lens spaces, spherical space forms |
| $E^3$ | $\mathbb{R}^3$ | 6 | $T^3$, flat manifolds |
| $H^3$ | $\mathbb{H}^3$ | 6 | hyperbolic manifolds, knot complements |
| $S^2\times\mathbb{R}$ | $S^2\times\mathbb{R}$ | 4 | $S^2\times S^1$, $\mathbb{RP}^2\times S^1$ |
| $H^2\times\mathbb{R}$ | $\mathbb{H}^2\times\mathbb{R}$ | 4 | products of surfaces with $S^1$ |
| $\widetilde{SL_2(\mathbb{R})}$ | the universal cover of $SL_2(\mathbb{R})$ | 4 | unit tangent bundles of hyperbolic surfaces |
| $\mathrm{Nil}$ | the Heisenberg group | 4 | nilmanifolds, the Kodaira–Thurston manifold |
| $\mathrm{Sol}$ | the solvable group of the plane | 3 | mapping tori of Anosov torus maps |

**Theorem (Thurston; geometrisation; Perelman).** Let $M$ be a compact oriented three-manifold whose boundary components are tori, with the torus decomposition into pieces $M_1,\ldots,M_m$. Then each $M_i$ is geometric: it is either hyperbolic of finite volume or Seifert fibred, the Seifert fibration carrying one of the six geometries $S^3$, $E^3$, $S^2\times\mathbb{R}$, $H^2\times\mathbb{R}$, $\widetilde{SL_2(\mathbb{R})}$ and $\mathrm{Nil}$. Equivalently, a compact oriented three-manifold with toroidal boundary and trivial torus decomposition is geometric; every closed oriented three-manifold is a connected sum of geometric pieces.

**Proof sketch.** The proof is the Ricci flow with surgery of Hamilton and Perelman: the Ricci flow on a three-manifold develops singularities that are modelled on the shrinking solutions of the flow, and the surgery removes the singular regions along $2$-spheres, replacing each with a pair of caps whose geometry is controlled. The flow is run to extinction or convergence; the pieces that remain are the geometric ones, and the topological decomposition produced by the surgeries agrees with the prime and torus decompositions. The analysis of the singularities, the canonical neighbourhood theorem and the no-local-collapsing theorem are the analytic content, and they belong to Part III. $\square$

**Theorem (Poincaré conjecture; Perelman).** A closed simply connected three-manifold is homeomorphic to $S^3$. More generally, a closed three-manifold with finite fundamental group is a spherical space form, so the closed three-manifolds of constant positive curvature are exactly the quotients of $S^3$ by finite groups acting freely; and a closed three-manifold with trivial fundamental group but with no assumption of smoothness is homeomorphic to $S^3$.

**Proof sketch.** In the geometrisation picture, a simply connected three-manifold has a trivial prime decomposition and a trivial torus decomposition, and is therefore geometric; the only geometry with positive curvature and finite volume is $S^3$, so the manifold is a spherical space form, and the spherical space form problem gives the classification of the free finite actions on $S^3$. The analytic input is the extinction of the Ricci flow for a simply connected manifold. $\square$

**Theorem (Mostow rigidity).** Let $M, N$ be closed hyperbolic three-manifolds. Then every isomorphism $\pi_1(M)\cong\pi_1(N)$ is induced by an isometry, and consequently the hyperbolic structure on a closed hyperbolic three-manifold is unique: the volume is a topological invariant, and there is no continuous deformation of a hyperbolic structure.

**Proof sketch.** The rigidity is proved by the ergodicity of the geodesic flow and the resulting invariance of the boundary map at infinity; a quasiconformal conjugacy between the two boundary actions has derivative of distortion zero, hence is conformal, and the conformal boundary map extends to an isometry by the extension theorem of *Hyperbolic Geometry*. $\square$

**Theorem (hyperbolic Dehn surgery; Thurston).** Let $M$ be a cusped hyperbolic three-manifold of finite volume with $h$ cusps, and let $p_i/q_i$ be a slope on each cusp. Then for all but finitely many choices of the slopes, the Dehn filled manifold $M(p_1/q_1,\ldots,p_h/q_h)$ is hyperbolic; the volume of the filled manifold tends to the volume of $M$ as the slopes tend to infinity; and the set of exceptional slopes is finite and computable in principle.

**Proof sketch.** The existence of a hyperbolic structure on the filled manifold is obtained by deforming the complete hyperbolic structure on $M$ to a structure in which the holonomy of the peripheral curves becomes parabolic at the required slope; the resulting representation is shown to be discrete and faithful by a geometric limit argument, and the finite set of exceptional slopes consists of those where the holonomy of the core of the filling has become elliptic. $\square$

**Example.** The complement of the figure-eight knot in $S^3$ is a cusped hyperbolic three-manifold of finite volume, the union of two regular ideal tetrahedra; its volume is

$$
\mathrm{vol}(S^3\setminus 4_1) = 2\cdot 1.0149416\ldots = 2.0298832\ldots ,
$$

twice the volume of the regular ideal simplex; the knot is the simplest hyperbolic knot, and all but finitely many of its Dehn surgeries produce closed hyperbolic manifolds. The exceptional slopes include $\infty$, which returns $S^3$, and $0$, whose surgery is the torus bundle over the circle with Anosov monodromy carrying the $\mathrm{Sol}$ geometry, since the knot complement fibres over the circle with a once-punctured torus as fibre and a pseudo-Anosov monodromy. The Gieseking manifold, the non-orientable cusped hyperbolic three-manifold, has volume equal to that of one regular ideal tetrahedron, $1.0149416\ldots$, and is the minimal volume cusped hyperbolic three-manifold.

**Theorem (Weeks manifold; Gabai–Meyerhoff–Milley).** The Weeks manifold, the hyperbolic three-manifold obtained by surgery on the Whitehead link, is the unique closed hyperbolic three-manifold of minimal volume, and

$$
\mathrm{vol}(\text{Weeks manifold}) = 0.94270736\ldots .
$$

**Proof sketch.** The proof combines the computation of the volumes of the hyperbolic three-manifolds with bounded volume obtained by the Mom technology of Gabai, Meyerhoff and Milley, the list of the cusped manifolds of small volume, and the enumeration of the fillings; the minimality is established by exhausting all the candidates below the bound. $\square$

**Remark (virtual fibring and the classification programme).** The hyperbolic pieces of a three-manifold have a rich structure beyond their geometry: Agol's theorem, building on Wise's work, states that a closed hyperbolic three-manifold has a finite cover that fibres over the circle, so that every such manifold is virtually fibred; the surface bundles over $S^1$ are thereby the universal building blocks of the hyperbolic three-manifolds, and the theory of *Mapping Class Groups* and the pseudo-Anosov dynamics of the monodromy control the geometry of the bundle. The classification of closed hyperbolic three-manifolds up to homeomorphism is thus reduced to the geometry of their fundamental groups, and by Mostow rigidity the geometry is unique, so that the classification problem is a group-theoretic one.

## Heegaard Splittings and Dehn Surgery

**Definition.** A **Heegaard splitting** of a closed oriented three-manifold $M$ is a decomposition $M = H_0\cup_\Sigma H_1$ into two handlebodies of genus $g$ glued along their common boundary surface $\Sigma$ of genus $g$; the **Heegaard genus** is the minimal $g$ for which a splitting exists. Every closed oriented three-manifold admits one: take a triangulation, take the union of the simplices of dimension $\leq1$ as one handlebody and the complement as the other, after regular neighbourhoods.

**Theorem (Reidemeister; Singer).** Any two Heegaard splittings of a closed oriented three-manifold become isotopic after stabilisation by adding cancelling pairs of handles, and the Heegaard genus is an invariant of the manifold.

**Proof sketch.** The two splittings are put in general position, and their intersection is analysed as a collection of curves on the common surface; the isotopies and the stabilisations reduce one to the other by the standard moves on the disc system of the handlebodies. $\square$

**Definition.** Let $K\subseteq S^3$ be a knot, let $N(K)$ be a tubular neighbourhood and let $\partial N(K)$ be its boundary torus with the standard meridian-longitude basis. Cutting out the interior of $N(K)$ and gluing it back by the homeomorphism of the torus sending the meridian to a curve of slope $p/q$ gives the manifold $S^3_{p/q}(K)$ obtained by **Dehn surgery** on $K$ with surgery coefficient $p/q\in\mathbb{Q}\cup\{\infty\}$. The slope $\infty$ returns $S^3$.

**Theorem (Lickorish; Wallace).** Every closed oriented three-manifold is obtained from $S^3$ by Dehn surgery on a link, and the surgery description can be chosen so that the surgery coefficients are integers. Consequently every closed oriented three-manifold is the boundary of a four-dimensional handlebody obtained by attaching $2$-handles to the four-ball along the link with the prescribed framings.

**Proof sketch.** A Heegaard splitting of the manifold is a union of two handlebodies whose spine is a graph; the attaching spheres of the handlebodies are realised as a framed link in $S^3$, and the operation of replacing one handlebody by a solid torus is exactly surgery along the link. The integrality of the coefficients is achieved by Rolfsen twists, which change the framings by integers. $\square$

**Theorem (Kirby calculus).** Two framed links in $S^3$ give homeomorphic closed oriented three-manifolds by Dehn surgery if and only if they are related by the Kirby moves: the blow-up and blow-down of a $\pm1$-framed unknot, and the resulting handle slides. Consequently the classification of three-manifolds by surgery presentations is decidable modulo the Kirby moves, and the moves are the calculational tool for the invariants.

**Proof sketch.** The moves correspond to the elementary operations on the $4$-dimensional handlebodies filling the manifolds, and every homeomorphism of the boundaries extends over the handlebodies after a sequence of the moves; the proof is a statement about the mapping class group of the boundary of a $4$-handlebody, and the details belong. $\square$

**Example.** The Poincaré homology sphere $\Sigma(2,3,5)$ is the boundary of the $E_8$ plumbing, the Seifert fibred space with base $S^2$ and three exceptional fibres of multiplicities $2,3,5$, the quotient of $S^3$ by the binary icosahedral group of order $120$, and a homology sphere with perfect fundamental group; by the Casson invariant of *Floer Homology* it is a nontrivial element of the homology cobordism group, and it is the standard example that distinguishes the homology three-spheres from $S^3$. Its Casson invariant is $\lambda(\Sigma(2,3,5)) = -1$ for the standard orientation and normalisation.

## Four-Manifolds and the Intersection Form

**Definition.** Let $M$ be a closed oriented four-manifold. The **intersection form** is the symmetric bilinear form

$$
Q_M : H^2(M;\mathbb{Z})/\mathrm{torsion}\times H^2(M;\mathbb{Z})/\mathrm{torsion}\to\mathbb{Z}, \qquad Q_M(a,b) = \langle a\cup b,[M]\rangle ,
$$

unimodular over $\mathbb{Z}$ by Poincaré duality; it is **even** if $Q_M(a,a)$ is even for all $a$ and **odd** otherwise, and its signature is the **signature $\sigma(M)$** of the manifold.

**Theorem (classification of unimodular forms).** An indefinite unimodular symmetric bilinear form over $\mathbb{Z}$ is determined by its rank and its signature together with its parity: the odd indefinite forms are the orthogonal sums of copies of $\langle1\rangle$ and $\langle-1\rangle$, and the even indefinite forms are the sums of copies of the hyperbolic form $H = \begin{pmatrix}0&1\\1&0\end{pmatrix}$ and of the forms $\pm E_8$, the signature of an even form being divisible by $8$. The definite forms are not classified by these three invariants: the number of classes of definite forms grows with the rank, and the classification is known only in low rank.

**Proof sketch.** The indefinite case is reduced by the theory of quadratic forms over $\mathbb{Z}$: an indefinite form with rank at least three splits off a hyperbolic summand, and the reduction terminates; the definite case is the hard one, where the number of classes grows with the rank and the classification is known only in low rank. The form $E_8$ is the unique even unimodular positive definite form of rank $8$. $\square$

**Theorem (Milnor; the homotopy type).** Simply connected closed four-manifolds are homotopy equivalent if and only if their intersection forms are isometric. Consequently the intersection form is the complete homotopy invariant of a simply connected four-manifold.

**Proof sketch.** The intersection form determines the cup-product structure of $H^2$ and hence, by the Whitehead theorem applied to the Postnikov tower, the homotopy type; the construction of the homotopy equivalence from the isometry uses the fact that the attaching maps of the $3$-cells of a cell decomposition realise the form. $\square$

**Theorem (Freedman; topological classification).** Let $Q$ be a unimodular symmetric bilinear form over $\mathbb{Z}$. If $Q$ is even, there is a closed simply connected topological four-manifold with intersection form $Q$ and with Kirby–Siebenmann invariant determined by the signature of $Q$; if $Q$ is odd, there is a closed simply connected topological four-manifold with intersection form $Q$ with either value of the Kirby–Siebenmann invariant. Consequently the closed simply connected topological four-manifolds are classified by their intersection forms together with the Kirby–Siebenmann invariant, and $E_8$ is realised by a topological four-manifold, the **$E_8$ manifold**, which is not smoothable.

**Proof sketch.** The construction is by a topological handle decomposition, in which the Whitney trick for cancelling intersections of surfaces is replaced by the disc-embedding theorems of Freedman; the failure of the Whitney trick in the smooth case is exactly the source of the smooth obstruction. The proofs are analytic-topological and belong to the circle of ideas of Part III. $\square$

**Theorem (Donaldson; Rokhlin; the smooth obstruction).** Let $M$ be a closed smooth four-manifold. If $M$ is simply connected and $Q_M$ is negative definite, then $Q_M$ is diagonalisable over $\mathbb{Z}$, that is $Q_M\cong\langle-1\rangle^{\oplus b_2}$; and if $M$ is spin, the signature $\sigma(M)$ is divisible by $16$ (Rokhlin). Consequently the $E_8$ form is realised by no smooth four-manifold, and the topological classification does not pass to the smooth category.

**Proof sketch.** The Donaldson theorem is proved by the study of the moduli space of anti-self-dual $\mathrm{SU}(2)$-connections, whose dimension and compactness properties force the intersection form to be diagonal; it is the first of the gauge-theoretic obstructions. Rokhlin's theorem is an index-theoretic statement about the signature of a spin four-manifold. $\square$

**Theorem (Seiberg–Witten; Furuta; the $10/8$ conjecture).** The Seiberg–Witten invariants of a closed smooth four-manifold constrain the intersection form. For a closed smooth spin four-manifold Furuta's theorem gives

$$
b_2(M) \geq \tfrac{10}{8}\,|\sigma(M)| + 2 ,
$$

and the conjectured refinement with the coefficient $\tfrac{11}{8}$ is verified for the known examples and open in general. Furuta's inequality already excludes the form $E_8\oplus E_8$: the form has $b_2 = 16$ and $\sigma = 16$, while the bound requires $b_2\geq 22$.

**Proof sketch.** The Seiberg–Witten equations of Part III are solved on a spin four-manifold, and the dimension of their moduli space together with the adjunction inequalities give the constraints; the proof of the $\tfrac{10}{8}$ bound is a careful analysis of the Seiberg–Witten moduli space for the connected sum of $M$ with copies of $S^2\times S^2$ and the application of the Furuta and Fintushel–Stern methods, while the expected $\tfrac{11}{8}$ bound requires the analysis of the higher-dimensional moduli spaces of the theory. $\square$

**Remark.** The theorems of Freedman and Donaldson together produce the exotic phenomena of dimension four: because $E_8$ has signature $8$ and a smooth spin four-manifold has signature divisible by $16$, the $E_8$ manifold is a topological four-manifold with no smooth structure; and because the simply connected topological classification is so fine, the smooth structures it carries can be infinitely many. The dimension-four theory is the unique dimension in which the topological and the smooth classification diverge so sharply at the level of the simply connected manifolds.

## Exotic Phenomena in Dimension Four

**Theorem (exotic $\mathbb{R}^4$; Freedman; Donaldson; Gompf; Taubes).** There are uncountably many pairwise non-diffeomorphic smooth manifolds homeomorphic to $\mathbb{R}^4$. Every Euclidean space $\mathbb{R}^n$ with $n\neq4$ has a unique smooth structure up to diffeomorphism.

**Proof sketch.** The construction begins with a compact smooth four-manifold whose intersection form is odd and which is not spin (for instance a Dolgachev surface, obtained by logarithmic transforms from a rational surface), whose topological classification by Freedman gives a homeomorphism to a standard connected sum of $\mathbb{CP}^2$'s and $\overline{\mathbb{CP}^2}$'s, while the gauge-theoretic invariants of Donaldson distinguish the smooth structures; an exotic $\mathbb{R}^4$ is obtained as the interior of a compact manifold with boundary a homology sphere whose end is not smoothly standard. The uncountability comes from the infinite families of the distinguished manifolds. $\square$

**Theorem (failure of the $h$-cobordism theorem in dimension four).** The smooth $h$-cobordism theorem is false in dimension four: there are compact smooth four-dimensional $h$-cobordisms, between three-manifolds, that are not products. The topological $h$-cobordism theorem holds in dimension four for good fundamental groups by the disc-embedding theorems of Freedman.

**Proof sketch.** The failure is inherited from the failure of the Whitney trick: the cancellation of intersections of surfaces in a four-dimensional handlebody is obstructed by the fundamental group and by the gauge-theoretic invariants, and the obstruction can be nonzero. The general statement of the $h$-cobordism theorem and its high-dimensional proof are not covered here. $\square$

**Remark (the smooth Poincaré conjecture in dimension four).** The smooth four-dimensional Poincaré conjecture — that a closed smooth four-manifold homeomorphic to $S^4$ is diffeomorphic to $S^4$ — is open; the topological statement is a theorem of Freedman, and the smooth statement is the boundary case of the disc-embedding problem. The failure of the Whitney trick and the richness of the gauge-theoretic invariants make dimension four the exceptional case in the classification of manifolds, and it is the reason the low-dimensional theory is a subject of its own.

## Summary

In dimension two the compact surfaces are classified by orientability, Euler characteristic and the number of boundary components, and by uniformisation they carry the spherical, Euclidean or hyperbolic geometry according to the sign of $\chi$; the moduli of the hyperbolic structures are not developed here and their symmetries belong to *Mapping Class Groups*. In dimension three the Kneser–Milnor theorem gives the unique prime decomposition, the Jaco–Shalen–Johannson theorem the unique torus decomposition, and the geometrisation theorem — proved by Perelman's Ricci flow — gives each piece one of the eight model geometries $S^3$, $E^3$, $H^3$, $S^2\times\mathbb{R}$, $H^2\times\mathbb{R}$, $\widetilde{SL_2(\mathbb{R})}$, $\mathrm{Nil}$ and $\mathrm{Sol}$; the Poincaré conjecture and the spherical space form problem follow, Mostow rigidity makes the hyperbolic structure unique on a closed manifold, and the hyperbolic Dehn surgery theorem makes the hyperbolic manifolds computable, with the figure-eight complement of volume $2.0298832\ldots$ and the Weeks manifold of minimal volume $0.94270736\ldots$ as the standard examples.

The combinatorial models of a three-manifold are the Heegaard splittings, unique up to stabilisation by Reidemeister–Singer, and the Dehn surgery presentations, which by Lickorish–Wallace realise every closed oriented three-manifold and which are related by the Kirby moves. In dimension four the classification is controlled by the intersection form, which classifies the simply connected topological manifolds by Freedman and their homotopy types by Milnor, and which is obstructed in the smooth category by the theorems of Donaldson and Rokhlin: the $E_8$ form is topological and not smooth, the signature of a smooth spin four-manifold is divisible by $16$ by Rokhlin's theorem, and the $10/8$ inequality of Furuta constrains the spin case, while the expected $11/8$ bound remains open. The exotic phenomena are the corollary: $\mathbb{R}^4$ has uncountably many smooth structures, the smooth $h$-cobordism theorem fails in dimension four, and the smooth Poincaré conjecture in dimension four is open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M$, $N$ | Compact (usually closed oriented) manifolds of dimension two, three or four |
| $g$, $k$, $b$, $\chi$ | Genus of an orientable surface, genus of a non-orientable surface, boundary count, Euler characteristic $\chi=2-2g-b$ |
| $M_1\# M_2$ | Connected sum; prime and irreducible three-manifolds |
| $L(p,q)$ | Lens space $S^3/(\mathbb{Z}/p)$; Seifert fibred over $S^2$ |
| $T^2\times I$, $\Sigma$ | Splitting tori of the JSJ decomposition; Heegaard surface |
| $H_i$, $\Sigma_g$ | Handlebodies; genus-$g$ Heegaard splitting $M=H_0\cup_\Sigma H_1$ |
| $S^3_{p/q}(K)$ | Dehn surgery on a knot with rational coefficient $p/q$ |
| $E_8$, $H$ | Even unimodular positive definite form of rank $8$; hyperbolic form $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ |
| $Q_M$, $\sigma(M)$ | Intersection form and signature of a closed oriented four-manifold |
| $b_2$, $b_2^\pm$ | Second Betti number and the dimensions of the positive and negative parts |
| Kirby moves | Blow-up/blow-down and handle slides relating surgery presentations |
| $S^3\setminus 4_1$ | Figure-eight knot complement, volume $2.0298832\ldots$ |
| Weeks manifold | Closed hyperbolic three-manifold of minimal volume $0.94270736\ldots$ |





## Further Reading

- Hellmuth Kneser, "Geschlossene Flächen in dreidimensionalen Mannigfaltigkeiten", *Jahresbericht der Deutschen Mathematiker-Vereinigung* 38 (1929), 248–260, and John Milnor, "A Unique Decomposition Theorem for 3-Manifolds", *American Journal of Mathematics* 84 (1962), 1–7, for the prime decomposition.
- William Jaco and Peter Shalen, "Seifert Fibered Spaces in 3-Manifolds", *Memoirs of the American Mathematical Society* 21 (1979), and Klaus Johannson, *Homotopy Equivalences of 3-Manifolds with Boundary* (Springer, 1979), for the torus decomposition.
- William Thurston, "Three-Dimensional Manifolds, Kleinian Groups and Hyperbolic Geometry", *Bulletin of the American Mathematical Society* 6 (1982), 357–381, for the geometrisation conjecture and the hyperbolic Dehn surgery theorem.
- Michael Freedman, "The Topology of Four-Dimensional Manifolds", *Journal of Differential Geometry* 17 (1982), 357–453, for the topological classification of simply connected four-manifolds.
- Simon Donaldson, "An Application of Gauge Theory to Four-Dimensional Topology", *Journal of Differential Geometry* 18 (1983), 279–315, for the obstruction to smoothing the definite intersection forms.
- John Morgan, *The Seiberg–Witten Equations and Applications to the Topology of Smooth Four-Manifolds* (Princeton University Press, 1996), for the Seiberg–Witten constraints, the $10/8$ problem and the exotic phenomena.
- Mikio Furuta, "Monopole Equation and the $\frac{11}{8}$-Conjecture", *Mathematical Research Letters* 8 (2001), 279–291, for the $\frac{10}{8}$ inequality for spin four-manifolds.
- David Gabai, Robert Meyerhoff and Peter Milley, "Minimum Volume Cusped Hyperbolic Three-Manifolds", *Journal of the American Mathematical Society* 22 (2009), 1157–1215, for the minimal volume closed hyperbolic three-manifold and the Weeks manifold.
- Ian Agol, "The Virtual Haken Conjecture", *Documenta Mathematica* 18 (2013), 1045–1087, for the virtual fibring of hyperbolic three-manifolds.
