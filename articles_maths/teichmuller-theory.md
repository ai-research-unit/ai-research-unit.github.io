
# __Teichmüller Theory__

## Introduction

Teichmüller theory is the study of the deformations of the complex structure of a surface. Fix a closed oriented surface $S$ of genus $g$ and let $n$ be the number of marked points; the **Teichmüller space** $\mathcal{T}(S)$ is the set of the complex structures on $S$ — equivalently, by the uniformisation theorem, the hyperbolic structures — together with a marking that fixes the topological type, modulo the deformations isotopic to the identity. It is a contractible domain of dimension $6g-6+2n$ over the reals, the quotient by the mapping class group is the **moduli space** of the Riemann surfaces of the given topological type, and the quotient map is the universal family of the marked surfaces over the moduli problem. The space carries a natural distance, the **Teichmüller metric**, defined by the least dilatation of a homeomorphism between two marked structures; the distance is realised by a unique extremal homeomorphism, the Teichmüller map, and its geodesics are described by the quadratic differentials. The second natural metric, the **Weil–Petersson metric**, is the Kähler metric induced by the pairing of the quadratic differentials, and it is the other standard structure on the space.

The theory has three faces. Analytically it is the theory of the quasiconformal maps and of the Beltrami equation, and its main existence theorem, the measurable Riemann mapping theorem, produces the complex structures; this analytic face rests on results that lie earlier in this Part — the measure in *Measure Theory and Integration*, the singular integrals that solve the Beltrami equation in *Fourier Analysis on Euclidean Spaces*, the weak differentiability in *Sobolev Spaces and Weak Solutions* — and no article of the corpus develops the quasiconformal maps themselves. The present article uses these results as statements. Geometrically it is the theory of the hyperbolic structures and of the lengths of the closed geodesics, with the Fenchel–Nielsen coordinates and the Bers embedding as the principal charts; this face rests on the hyperbolic geometry of *Hyperbolic Geometry*. Topologically it is the theory of the action of the mapping class group, of the Nielsen realisation and of the classification of the surface diffeomorphisms, and this face is that of *Mapping Class Groups*, the companion article. The present article treats the space itself, its distance, its coordinates, its compactifications and its quotient by the group, and it states the rigidity and finiteness theorems that make the quotient a finite-volume orbifold.

**The boundaries of the article.** The hyperbolic structures, the models $\mathbb{H}^2$ and $\mathbb{H}^3$, Mostow rigidity, the volumes, the geodesic laminations and the convex cores are those of *Hyperbolic Geometry*, being written in parallel; the hyperbolic 3-manifolds that arise as the quotients of the deformation of the surface group are those of *Low-Dimensional Topology*. The mapping class group, its action, the Nielsen realisation, the Thurston classification of the surface diffeomorphisms and the Dehn twists are those of *Mapping Class Groups*, which precedes this article; the present article states the quotient of the Teichmüller space by the group and defers the group theory. The moduli space of the Riemann surfaces and its Deligne–Mumford compactification lie at the boundary with complex algebraic geometry, and the Kähler structures of the moduli spaces are those of *Kähler Geometry*. The quadratic differentials and the holomorphic forms are those of *Hermitian Geometry and Almost Complex Structures* for their linear-algebraic properties, and the Beltrami equation, the measurable Riemann mapping theorem, the theory of the quasiconformal maps and the extremal length are analytic, and belong to this Part. The fundamental groups, the covering spaces and the homology of the surfaces are those of *Algebraic Topology*, written by another agent. The quotient singularities and the orbifolds are treated as the spaces they are, and no physics is invoked.

## The Teichmüller Space

**Definition.** Let $S$ be a closed oriented surface of genus $g$ with $n$ marked points removed, and suppose $2g-2+n>0$, so that $S$ carries a hyperbolic structure and is not a sphere with fewer than three punctures nor a torus without punctures. A **marked hyperbolic structure** on $S$ is a pair $(X,f)$ of a complete hyperbolic surface $X$ of finite area and an orientation-preserving homeomorphism $f : S\to X$; two pairs $(X,f)$ and $(Y,h)$ are **equivalent** if $h\circ f^{-1} : X\to Y$ is isotopic to an isometry. The **Teichmüller space** $\mathcal{T}(S)$ is the set of the equivalence classes of the marked hyperbolic structures; the equivalence class is written $[X,f]$ and the point is also described by the complex structure it determines on $S$.

**Theorem (the complex structure and the hyperbolic structure).** The descriptions of the marked structures agree: the assignment of a complex structure on $S$ determines a unique complete conformal hyperbolic metric in the same conformal class, and conversely; the two spaces of the marked structures coincide, and $\mathcal{T}(S)$ is a complex manifold of dimension $3g-3+n$ and a real manifold of dimension $6g-6+2n$.

**Proof sketch.** The passage from the complex structure to the hyperbolic metric is the uniformisation theorem of *Hyperbolic Geometry*: the universal cover of the surface is conformally equivalent to the disc, the deck transformations are Möbius transformations, and the metric is the pull-back of the hyperbolic metric. The passage back is the statement that a hyperbolic metric determines a complex structure through its conformal class. The dimension count is the Riemann–Roch count of the deformations of the complex structure, or the count of the Fenchel–Nielsen lengths and twists below. $\square$

**Example (the low cases).** For the once-punctured torus, $g=1$, $n=1$, the space is $\mathcal{T} = \mathbb{H}$, the upper half-plane: a marked hyperbolic structure on the once-punctured torus is determined by its modulus $\tau$, the complete hyperbolic metric having area $2\pi$ by Gauss–Bonnet. For the torus without punctures the Teichmüller space is again $\mathbb{H}$ with the modulus parameter, of real dimension $2$. For the sphere with three punctures, $g=0$, $n=3$, the space is a single point: the hyperbolic structure on the thrice-punctured sphere is unique up to isometry, and the space has dimension $6\cdot0-6+2\cdot3 = 0$. For the sphere with four punctures, $g=0$, $n=4$, the space is the upper half-plane with the cross-ratio parameter, of real dimension $2 = 6\cdot0-6+2\cdot4$. The dimension formula $\dim_{\mathbb{R}}\mathcal{T}(S) = 6g-6+2n$ holds whenever $2g-2+n>0$, the unpunctured torus with its real dimension $2$ being the one further exception; the complex dimension is one half of it, $3g-3+n$.

**Definition.** The **mapping class group** $\mathrm{Mod}(S)$ is the group of the isotopy classes of the orientation-preserving homeomorphisms of $S$; it acts on $\mathcal{T}(S)$ by composition of the markings, the action is by biholomorphisms, and the quotient

$$
\mathcal{M}(S) = \mathcal{T}(S)/\mathrm{Mod}(S)
$$

is the **moduli space** of the Riemann surfaces of the topological type of $S$. It is a complex orbifold of dimension $3g-3+n$, and the quotient map exhibits it as the coarse moduli space of the marked surfaces.

**Theorem (Fricke, Nielsen; the holonomy parametrisation).** The holonomy representation $\rho : \pi_1(S)\to PSL_2(\mathbb{R})$ of the marked hyperbolic structure is discrete, faithful and of the prescribed type, and the Teichmüller space is a connected component of the quotient

$$
\mathrm{Hom}^{\mathrm{df}}(\pi_1(S), PSL_2(\mathbb{R}))/PSL_2(\mathbb{R})
$$

of the space of discrete faithful representations by conjugation. By the Fricke–Nielsen theory of the Fuchsian groups, the marked structure is determined by its holonomy representation: the holonomy map is injective, and its image is an open dense subset of the character variety $\mathrm{Hom}(\pi_1(S),PSL_2(\mathbb{R}))/\!/PSL_2(\mathbb{R})$ described by the Fricke polynomial.

**Proof sketch.** The holonomy of a hyperbolic structure is a discrete faithful representation because the deck transformations are isometries of the disc; the injectivity of the holonomy map is the statement that a marked structure is determined by its holonomy, proved by the two-dimensional analogue of the argument of Mostow: a quasiconformal conjugacy between two such representations has vanishing dilatation and is therefore conformal. The connectedness and the identification of the image with the smooth points of the character variety are the theorems of Fricke and of the deformation theory. $\square$

## The Teichmüller Metric

**Definition.** Let $[X,f], [Y,h]\in\mathcal{T}(S)$ and let $k : X\to Y$ range over the homeomorphisms with $h^{-1}\circ k\circ f : S\to S$ isotopic to the identity. If $k$ is quasiconformal, its **dilatation** is

$$
K(k) = \operatorname*{ess\,sup}_{p\in X}\frac{\text{maximal stretch of }dk_p}{\text{minimal stretch of }dk_p} \ \in [1,\infty] ,
$$

the essential supremum of the ratio of the principal stretches of the differential, and the **Teichmüller distance** is

$$
d_T([X,f],[Y,h]) = \tfrac12\inf_{k}\log K(k) ,
$$

the infimum over the homeomorphisms compatible with the markings up to isotopy. The function $d_T$ is a complete metric on $\mathcal{T}(S)$, called the **Teichmüller metric**; it is invariant under the action of the mapping class group, so it descends to a metric on the moduli space.

**Theorem (Teichmüller; existence and uniqueness of the extremal map).** Let $[X,f],[Y,h]\in\mathcal{T}(S)$ and let $K$ be the value of the infimum above. Then the infimum is attained: there is a homeomorphism $k : X\to Y$ with $K(k) = K$ realising the distance, and it is unique up to composition with a conformal automorphism of $Y$. The extremal map is the **Teichmüller map**, and it is characterised by the existence of a holomorphic quadratic differential $\phi$ on $X$ such that the Beltrami coefficient of $k$ is

$$
\mu = k_0\,\frac{\bar\phi}{|\phi|}, \qquad k_0 = \frac{K-1}{K+1} ,
$$

a Beltrami differential of constant modulus $k_0$ determined by the direction field of $\phi$. In the natural coordinates of $\phi$ on $X$ and of the push-forward quadratic differential on $Y$, the map $k$ is affine, with the same constant stretch: it multiplies the horizontal coordinate by a fixed factor and the vertical coordinate by the reciprocal factor.

**Proof sketch.** The existence and the uniqueness of the extremal quasiconformal map are the theorems of Teichmüller, proved by the reduction to the Beltrami equation with the coefficient of constant modulus determined by an extremal quadratic differential; the analytic content — the measurable Riemann mapping theorem, the solvability of the Beltrami equation and the extremal length — belongs elsewhere in the corpus (*Measure Theory and Integration*, *Fourier Analysis on Euclidean Spaces*, *Sobolev Spaces and Weak Solutions*), where the measure and the limit are available; the quasiconformal maps themselves are not developed anywhere in it. The explicit form of the extremal map in the coordinates of the quadratic differential is the computation that gives both the existence and the uniqueness. $\square$

**Theorem (Teichmüller geodesics; the distance formula).** The Teichmüller metric is a Finsler metric, whose infinitesimal norm is the infimum of the essential sup norms of the Beltrami coefficients modulo the trivial ones; it is not Riemannian for $g\geq2$. The geodesic ray determined by a holomorphic quadratic differential $\phi$ is the family of the extremal maps with Beltrami coefficients $k_0(t)\,\bar\phi/|\phi|$ as the modulus $k_0(t)$ increases from $0$, and every geodesic is of this form; two points are joined by a unique geodesic. The distance has the extremal-length formulation of Kerckhoff: the metric is also given by

$$
d_T([X,f],[Y,h]) = \tfrac12\log\inf_{\gamma}\frac{\mathrm{Ext}_Y(\gamma)}{\mathrm{Ext}_X(\gamma)} ,
$$

the infimum over the simple closed curves $\gamma$ on $S$, where $\mathrm{Ext}$ is the extremal length of the curve in the corresponding structure.

**Proof sketch.** The Finsler structure is read off from the infinitesimal form of the dilatation; the geodesics are obtained by integrating the constant-modulus Beltrami differentials of the quadratic differentials, and the uniqueness is the uniqueness of the extremal map. The extremal-length formula of Kerckhoff is proved by comparing the dilatation of a quasiconformal map with the ratio of the extremal lengths and then applying the Teichmüller existence theorem to produce the equality. The extremal length is analytic and is treated in Part III. $\square$

**Example.** For the once-punctured torus, $\mathcal{T} = \mathbb{H}$, and the Teichmüller metric is exactly the hyperbolic metric of the upper half-plane multiplied by the appropriate normalisation: the distance between two marked structures is the hyperbolic distance between the moduli, and the Teichmüller geodesics are the hyperbolic geodesics. For the four-punctured sphere, the space is the upper half-plane with the modulus variable, and again the Teichmüller metric is up to a factor the hyperbolic metric; for the higher genus the metric differs from the hyperbolic metric and the space is not symmetric.

**Remark (the two metrics).** The other canonical metric, the **Weil–Petersson metric**, is defined by the pairing of the holomorphic quadratic differentials

$$
\langle\phi,\psi\rangle_{\mathrm{WP}} = \int_X \phi\,\overline{\psi}\,\lambda^{-2},
$$

where the hyperbolic metric of $X$ is written $\lambda^2|dz|^2$ in a conformal coordinate, and it is a Kähler metric of negative scalar curvature which is incomplete; it is the metric appearing in the Ahlfors–Bers theory of the deformation spaces and in the Weil–Petersson volumes of the moduli spaces. The analytic definition of the integral and the Kähler properties of the metric belong to Part III and to *Kähler Geometry* respectively; the two metrics are distinct, the Teichmüller metric being Finsler and the Weil–Petersson metric Riemannian, and the comparison of their geodesics and their boundaries is one of the standard themes of the theory.

## Coordinates and the Bers Embedding

**Theorem (Fenchel–Nielsen coordinates).** Let $S$ have genus $g$ and $n$ punctures with $2g-2+n>0$. Fix a maximal collection of disjoint simple closed curves $\gamma_1,\ldots,\gamma_{3g-3+n}$ that decomposes $S$ into pairs of pants. Then the map

$$
\mathcal{T}(S)\longrightarrow (\mathbb{R}_{>0}\times\mathbb{R})^{3g-3+n}, \qquad [X,f]\longmapsto \big(\ell_{\gamma_i}(X),\tau_i(X)\big)_{i=1}^{3g-3+n},
$$

sending a marked structure to the hyperbolic lengths of the curves and to the Fenchel–Nielsen twist parameters along them, is a real-analytic diffeomorphism onto the product. Consequently $\mathcal{T}(S)$ is diffeomorphic to $\mathbb{R}^{6g-6+2n}$, hence contractible.

**Proof sketch.** A pair of pants with the geodesic boundary components has a unique hyperbolic structure, so a marked structure is determined by the gluing data along the pants decomposition; the gluing is determined by a length and a twist at each curve, and the resulting coordinates are global. The contractibility follows from the diffeomorphism to a Euclidean space. $\square$

**Theorem (Bers; the embedding in the space of the quadratic differentials).** Let $S$ be a closed surface of genus $g\geq2$ and let $X\in\mathcal{T}(S)$. The space $\mathcal{T}(S)$ embeds biholomorphically, as a bounded domain, into the complex vector space $Q(X)$ of the holomorphic quadratic differentials on $X$, of complex dimension $3g-3$. The image is the **Bers embedding**; the boundary of the image contains the Riemann surfaces whose holonomy representation is not discrete or not faithful, and the closure of the image in $Q(X)$ is compact.

**Proof sketch.** The domain of discontinuity of the holonomy of a Kleinian group uniformising a hyperbolic 3-manifold provides the boundary map of the surface group into $\mathbb{CP}^1$, and the Schwarzian derivative of the boundary map is a holomorphic quadratic differential; the assignment of the Schwarzian to the marked structure is holomorphic and injective, and the boundedness follows from the compactness of the boundary map. The hyperbolic 3-manifolds supplying the domains belong to *Hyperbolic Geometry*. $\square$

**Theorem (the Dehn–Nielsen–Baer theorem; the quotient).** The action of the mapping class group on $\mathcal{T}(S)$ is properly discontinuous, its quotient $\mathcal{M}(S)$ is a complex orbifold of dimension $3g-3+n$ whose orbifold fundamental group is $\mathrm{Mod}(S)$, and the stabiliser of a point of $\mathcal{T}(S)$ with $3g-3+n>0$ is the finite group of the conformal automorphisms of the corresponding surface. Consequently the moduli space is the quotient of a contractible space by the group, and its rational cohomology is the group cohomology of $\mathrm{Mod}(S)$.

**Proof sketch.** The proper discontinuity follows from the discreteness of the isometry groups of the hyperbolic structures and the finiteness of the automorphism groups; the identification of the orbifold fundamental group with the mapping class group is the definition of the quotient. The realisation of the mapping classes by homeomorphisms is the theorem of Nielsen, treated in *Mapping Class Groups*. $\square$

**Theorem (Hurwitz; the order of the automorphism group).** Let $X$ be a closed hyperbolic surface of genus $g\geq2$. Then the group of the orientation-preserving isometries of $X$ is finite of order at most $84(g-1)$; the orbit space of a point of $\mathcal{T}(S)$ has cardinality at most $84(g-1)$, and the bound is attained exactly when the quotient of $X$ by its full automorphism group is the orbifold of the $(2,3,7)$ triangle group, of orbifold Euler characteristic $-1/42$.

**Proof sketch.** The quotient $X/\mathrm{Aut}(X)$ is a hyperbolic orbifold, and the Gauss–Bonnet theorem computes its area as $2\pi$ times the sum of the singular contributions; the orbifold of the smallest area is that of the $(2,3,7)$ triangle group with the orbifold Euler characteristic $1/2+1/3+1/7-1 = -1/42$, so that the order of the automorphism group is at most $(2g-2)/(1/42) = 84(g-1)$. $\square$

## The Compactification and the Boundary

**Theorem (Deligne–Mumford; the compactification of the moduli space).** The moduli space $\mathcal{M}(S)$ of the smooth curves of genus $g$ with $n$ marked points is not compact; it admits a unique compactification $\overline{\mathcal{M}}_{g,n}$, the **Deligne–Mumford compactification**, which is a projective algebraic orbifold, whose points are the stable curves: the projective nodal curves of arithmetic genus $g$ with $n$ smooth marked points and with finitely many automorphisms. The compactification is obtained by adjoining the boundary divisors of the curves with a node; a degenerating family of smooth curves is completed by the stable curve obtained when the curves whose hyperbolic length tends to zero are pinched, and the universal curve extends to the boundary.

**Proof sketch.** The boundary of the moduli space is described by the degenerations of the hyperbolic structures: a family of curves degenerating in $\mathcal{M}(S)$ develops a curve whose length tends to zero, which is pinched into a node in the limit. The algebraic construction of the stable curves and the projectivity of the compactification are those of the moduli theory of the curves, and the comparison with the quotient of the Thurston compactification uses the description of the limit points by the projective measured laminations. $\square$

**Remark (the Thurston compactification).** The Teichmüller space has a compactification $\overline{\mathcal{T}}(S) = \mathcal{T}(S)\cup \mathcal{PML}(S)$ whose boundary is the space of the **projective measured laminations** on $S$, the space of the laminations with a transverse invariant measure up to scale; the compactification is a closed ball of dimension $6g-6+2n$, and the action of the mapping class group extends to it. The boundary encodes the degenerations of the hyperbolic structures: a sequence of structures leaving every compact set converges in the compactification to a projective measured lamination, and a mapping class acts on the boundary by its action on the lamination space. The measure carried by a lamination is a transverse invariant measure, and the analytic theory of the measured laminations belongs to Part III; the laminations themselves and the action of the group are treated in *Hyperbolic Geometry* and *Mapping Class Groups*.

**Remark (the boundary of the Teichmüller space and the Bers boundary).** The boundary of the Bers embedding and the Thurston boundary are two different compactifications of the same space, and the comparison between them is a central theme of the deformation theory: the Bers boundary is a fractal subset of the space of the quadratic differentials, and the Thurston boundary is a sphere of the measured laminations. The identification of the two boundaries in the appropriate sense, and the study of the analytic properties of the boundary of the Bers embedding, belong to the modern theory of the deformation spaces of the Kleinian groups, and its analytic content is Part III's.

## Examples, Computations and Applications

**Example (the dimensions).** The dimension of the Teichmüller space is $3g-3+n$ over $\mathbb{C}$ and $6g-6+2n$ over $\mathbb{R}$; the low cases are

| $g$ | $n$ | $\dim_{\mathbb{C}}$ | $\dim_{\mathbb{R}}$ |
|---|---|---|---|
| 0 | 3 | 0 | 0 |
| 0 | 4 | 1 | 2 |
| 1 | 1 | 1 | 2 |
| 1 | 2 | 2 | 4 |
| 2 | 0 | 3 | 6 |
| 3 | 0 | 6 | 12 |

verified by the formula, and the spaces of the sphere with three punctures and of the closed torus are the two degenerate cases: the first is a point, and the second needs the Euclidean rather than the hyperbolic description, its space being $\mathbb{H}$ of real dimension $2$ rather than the value $6\cdot1-6+0=0$ of the formula, which does not apply to the torus.

**Example (the once-punctured torus and the modular curve).** For the once-punctured torus, $\mathcal{T} = \mathbb{H}$ and the mapping class group acts through $PSL_2(\mathbb{Z})$; the moduli space is the modular curve $\mathbb{H}/PSL_2(\mathbb{Z})$, an orbifold with one cusp and two elliptic points of orders $2$ and $3$, and the Teichmüller metric is the hyperbolic metric of $\mathbb{H}$ up to normalisation. The example is the simplest in which the quotient by the group is visible and in which the elliptic points realise the automorphism groups: the square and hexagonal tori.

**Application (the uniformisation of the moduli problems).** The Teichmüller space is the solution of the moduli problem of the complex structures on a surface in the marked category: the marked structures are parametrised bijectively by a contractible complex manifold, the unmarked structures by the quotient, and the obstructions to the existence of a universal family are the automorphisms of the surfaces, which make the quotient an orbifold rather than a manifold. The algebraic construction of the moduli space of the curves, its compactification by the stable curves and the intersection theory on the compactification are the algebraic-geometric side of the same object, and the two descriptions agree by the GAGA-type theorems.

**Application (the monodromy and the rigidity).** A family of curves over a base $B$ determines a monodromy representation $\pi_1(B)\to\mathrm{Mod}(S)$ and a holonomy map $B\to\mathcal{T}(S)$; the geometry of the family is controlled by the two, and the rigidity of the hyperbolic structures makes the holonomy map locally determined by the monodromy in the appropriate sense. The virtual fibring theorem of *Low-Dimensional Topology* and the classification of the mapping classes of *Mapping Class Groups* supply the structure of the monodromies, and the arithmetic theory of the holonomy representations — the arithmetic and the trace fields of the surface groups — is one of the standard applications of the Teichmüller theory.

## Summary

The Teichmüller space of a surface $S$ of genus $g$ with $n$ punctures, $2g-2+n>0$, is the space of the marked complex — equivalently, hyperbolic — structures on $S$ modulo the isotopies: it is a contractible complex manifold of dimension $3g-3+n$, equipped with the Fenchel–Nielsen coordinates and with the Bers embedding into the holomorphic quadratic differentials, and its points are determined by their holonomy representations. The Teichmüller metric $d_T = \frac12\inf\log K$ is the Finsler metric of the extremal quasiconformal dilatation; by the theorems of Teichmüller the infimum is attained by a unique extremal map, affine in the coordinates of an extremal holomorphic quadratic differential, and by Kerckhoff the metric is also given by the extremal-length ratio of the simple closed curves. The geodesics are the Teichmüller geodesics through the quadratic differentials, and the metric is not Riemannian for $g\geq2$; the Weil–Petersson metric is the alternative Kähler metric, defined by the pairing of the quadratic differentials, incomplete and of negative scalar curvature.

The mapping class group $\mathrm{Mod}(S)$ acts properly discontinuously by biholomorphisms and the quotient is the moduli space $\mathcal{M}(S)$, a complex orbifold of dimension $3g-3+n$ whose orbifold fundamental group is the group and whose points have finite stabilisers of order at most $84(g-1)$ by the Hurwitz bound. The moduli space is noncompact, and its Deligne–Mumford compactification by the stable curves is projective; the Teichmüller space is compactified by the Thurston boundary of the projective measured laminations, and the comparison of the two compactifications, together with the description of the Bers boundary, is the boundary theory of the deformation spaces. The analytic foundation — the Beltrami equation, the measurable Riemann mapping theorem, the quasiconformal maps and the extremal length — belongs to Part III; the hyperbolic structures to *Hyperbolic Geometry*; the action of the group and the classification of its elements to *Mapping Class Groups*; and the moduli spaces to the algebraic-geometric theory of the curves.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S$ | Closed oriented surface of genus $g$ with $n$ marked points removed |
| $\mathcal{T}(S)$ | Teichmüller space of the marked hyperbolic/complex structures |
| $[X,f]$, $X$ | Marked hyperbolic surface; $f : S\to X$ the marking |
| $\mathcal{M}(S)$ | Moduli space $\mathcal{T}(S)/\mathrm{Mod}(S)$ |
| $\mathrm{Mod}(S)$ | Mapping class group of the orientation-preserving homeomorphisms up to isotopy |
| $6g-6+2n$, $3g-3+n$ | Real and complex dimensions of $\mathcal{T}(S)$ |
| $\gamma_i$, $\ell_{\gamma}$, $\tau_i$ | Curves of a pants decomposition; the length and Fenchel–Nielsen twist coordinates |
| $d_T$, $K(k)$ | Teichmüller distance, $\frac12\inf\log K$; dilatation of a quasiconformal homeomorphism |
| $\mu = k_0\bar\phi/\vert\phi\vert$ | Beltrami coefficient of the Teichmüller map, $k_0=(K-1)/(K+1)$; $\phi$ the extremal holomorphic quadratic differential |
| $Q(X)$, $\mathrm{Ext}_X(\gamma)$ | Holomorphic quadratic differentials on $X$; extremal length of a curve |
| $\langle\cdot,\cdot\rangle_{\mathrm{WP}}$ | Weil–Petersson pairing of quadratic differentials; $\lambda$ the hyperbolic metric density |
| $\overline{\mathcal{M}}_{g,n}$ | Deligne–Mumford compactification by the stable curves |
| $\mathcal{PML}(S)$ | Thurston boundary of the projective measured laminations |
| $84(g-1)$ | Hurwitz bound on the order of the automorphism group of a genus-$g$ surface |

## Further Reading

- Oswald Teichmüller, "Extremale quasikonforme Abbildungen und quadratische Differentiale", *Abhandlungen der Preussischen Akademie der Wissenschaften* 22 (1939), 1–197, for the extremal maps, the quadratic differentials and the metric.
- Lipman Bers, "Spaces of Riemann Surfaces as Bounded Domains", *Annals of Mathematics* 72 (1960), 558–583, and "On Moduli of Riemann Surfaces", *Proceedings of the National Academy of Sciences* 46 (1960), 1163–1165, for the Bers embedding and the complex structure of the space.
- Lars Ahlfors and Lipman Bers, "Riemann's Mapping Theorem for Variable Metrics", *Annals of Mathematics* 72 (1960), 385–404, for the measurable Riemann mapping theorem and the analytic foundation of the theory.
- Steven Kerckhoff, "The Asymptotic Geometry of Teichmüller Space", *Topology* 19 (1980), 23–41, for the extremal-length formula for the Teichmüller metric.
- Albert Fathi, François Laudenbach and Valentin Poénaru, *Thurston's Work on Surfaces* (Princeton University Press, 2012), for the compactification by the projective measured laminations and the classification of the mapping classes.
- William Thurston, "On the Geometry and Dynamics of Diffeomorphisms of Surfaces", *Bulletin of the American Mathematical Society* 19 (1988), 417–431, for the boundary of the Teichmüller space and the geometry of the deformation.
- Pierre Deligne and David Mumford, "The Irreducibility of the Space of Curves of Given Genus", *Publications Mathématiques de l'IHÉS* 36 (1969), 75–109, for the Deligne–Mumford compactification and the stable curves.
- Scott Wolpert, "The Weil–Petersson Metric Geometry", in *Handbook of Teichmüller Theory II* (European Mathematical Society, 2009), 47–64, for the Weil–Petersson metric and its comparison with the Teichmüller metric.
