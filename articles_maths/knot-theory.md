
# __Knot Theory__

## Introduction

A knot is a circle embedded in the three-sphere, and knot theory is the study of the equivalence classes of knots under ambient isotopy and of the invariants that distinguish them. The subject sits at the meeting point of three-dimensional topology, algebra and the theory of the braid and mapping class groups, and its invariants come in three broad families: the **fundamental group** and the geometric structure of the complement; the **algebraic invariants** of the complement — the Alexander module, the Conway polynomial, the signature, the torsion of the infinite cyclic cover; and the **quantum invariants** — the Jones, HOMFLY and Kauffman polynomials, constructed from the Temperley–Lieb and Hecke algebras and from the representation theory of the quantum groups. Two categorifications complete the picture: **knot Floer homology**, which categorifies the Alexander polynomial and detects the genus, and **Khovanov homology**, which categorifies the Jones polynomial and gives the Rasmussen concordance invariant.

The article develops the combinatorial and algebraic theory in order: the diagrams and the Reidemeister moves that encode ambient isotopy; the knot group, the complement and the peripheral structure; the Seifert surfaces, the Seifert matrix and the Alexander polynomial; the signatures and the concordance invariants; the skein-theoretic quantum invariants and the Tait conjectures; the categorifications and their detection theorems; and the hyperbolic geometry of knot complements, where the figure-eight knot and the torus knots are the two extreme examples. The concordance group and its homomorphisms are treated as the algebraic frame in which the invariants are compared; the general surgery theory and the four-dimensional invariants are cited to the neighbouring articles.

**The boundaries of the article.** The three-manifold topology of complements — the prime and torus decompositions, the geometrisation theorem, the hyperbolic Dehn surgery theorem, the Gordon–Luecke theorem and the concordance-theoretic frame — is that of *Low-Dimensional Topology*, and the present article uses it as given. The hyperbolic structures on knot complements and their volumes are those of *Hyperbolic Geometry*. The lens spaces that arise as surgeries on knots are those of *Lens Spaces*; the general surgery, the $s$-cobordism theorem and the concordance groups in the topological category are those, which follows. Knot Floer homology and the concordance invariants $\tau$ and $s$ are those of *Floer Homology*; they are stated here and not constructed. The Legendrian invariants of knots and the Bennequin inequality are those of *Symplectic and Contact Topology*. The braid groups and the mapping class groups of surfaces — the algebraic home of the Markov and Birman–Hilden theorems and of the Temperley–Lieb and Hecke algebras — are those of *Mapping Class Groups*, the final article of this half. The homology, the infinite cyclic covers, the torsion and the cup products are those of *Algebraic Topology*, being written by another agent: the invariants of this article are topological and low-dimensional, and the homological machinery is that article's. The quantum group representations that give the Jones polynomial their structural explanation belong to the representation theory of Lie algebras in Part I, and the analytic content of the gauge-theoretic and Floer-theoretic constructions belongs to Part III, where the measure and the limit are available. No physics is invoked.

## Knots, Links and Diagrams

**Definition.** A **knot** is an embedded circle $K\subseteq S^3$; a **link** is an embedded disjoint union of circles, its **components**. Two knots are **equivalent** if there is an orientation-preserving homeomorphism of $S^3$ carrying one to the other; equivalently if they are related by an ambient isotopy. A knot is **tame** if it is isotopic to a polygonal one; the wild knots are excluded from the theory. The **connected sum** $K_1\# K_2$ is formed by cutting each knot and gluing the four ends crosswise; the unknot is the identity, and a knot is **prime** if it is not the unknot and every connected sum decomposition is trivial.

**Definition.** A **diagram** of a knot is the image of a generic projection onto a plane, with the over- and under-crossings marked; it is **reduced** if it has no nugatory crossings, and **alternating** if the crossings alternate over and under along each component.

**Theorem (Reidemeister).** Two diagrams represent equivalent knots if and only if they are related by a finite sequence of ambient isotopies of the plane and the three **Reidemeister moves**: the twist move $R_1$, the poke move $R_2$ and the slide move $R_3$. Consequently every knot invariant that is computable from a diagram and unchanged by the three moves is an invariant of the knot.

**Proof sketch.** The two diagrams are the projections of two polygonal representatives; putting the two representatives in general position in $S^3$, the images of the crossings sweep out a finite set of elementary events — a crossing moving past another crossing, or a crossing appearing and disappearing, or a strand passing over a vertex — and each event corresponds to one of the three moves or to an isotopy of the plane. $\square$

**Definition.** The **crossing number** $c(K)$ is the minimal number of crossings in a diagram of $K$; the **unknotting number** $u(K)$ is the minimal number of crossing changes needed to turn a diagram of $K$ into one of the unknot; the **bridge number** and the **braid index** are defined analogously from the diagrams and from the braid representatives.

**Example.** The knots of small crossing number are the trefoil $3_1$ (the torus knot $T(2,3)$), the figure-eight knot $4_1$, the cinquefoil $5_1$ ($T(2,5)$) and the knot $5_2$, then the six-, seven- and eight-crossing knots. The trefoil is chiral — it is not equivalent to its mirror image — while the figure-eight is amphichiral; the alternating knots of up to eight crossings were tabulated by Tait and Little, and the tables are complete and correct, a fact whose verification required the proof of the Tait conjectures below.

**Remark.** The prime decomposition of knots is unique, by the theorem of Schubert, and every knot is a connected sum of prime knots; the satellite construction — taking a knot in a solid torus and embedding the torus as a tubular neighbourhood of a companion knot — produces the non-prime examples in a different sense, the satellite knots, which carry the geometry of both the companion and the pattern. The theory of these decompositions is the analogue for knots of the prime and torus decompositions of three-manifolds, and the two are related by the geometry of the complement.

## The Knot Group, the Complement and the Peripheral Structure

**Definition.** The **knot group** is $\pi_K = \pi_1(S^3\setminus K)$. It is finitely presented: a diagram with $n$ crossings gives the **Wirtinger presentation** with $n$ generators, one meridian for each arc of the diagram, and $n$ relations, one for each crossing, of the form $x_{i+1} = x_k x_i x_k^{-1}$ or its inverse; the abelianisation of $\pi_K$ is $\mathbb{Z}$, generated by the image of a meridian.

**Theorem (Gordon–Luecke).** Knots are determined by their complements: if $S^3\setminus K_1$ and $S^3\setminus K_2$ are homeomorphic, then $K_1$ and $K_2$ are equivalent. Consequently the knot group, and every invariant of the complement, is a complete invariant of the knot up to equivalence.

**Proof sketch.** The proof uses the theory of the characteristic submanifold of the complement, together with the fact that the boundary torus is the unique incompressible torus up to isotopy in the generic case; the detailed argument is that of the low-dimensional topology of *Low-Dimensional Topology*. $\square$

**Definition.** A **Seifert surface** for a knot $K$ is a compact oriented surface $F\subseteq S^3$ with $\partial F = K$; such a surface exists by the Seifert algorithm applied to any diagram, which produces one of genus equal to the genus of the diagram. The **genus** $g(K)$ is the minimal genus of a Seifert surface, and the **Seifert matrix** $V$ of a Seifert surface is the matrix of the linking form $V_{ij} = \mathrm{lk}(a_i, a_j^+)$ of a basis of $H_1(F;\mathbb{Z})$ with the positive push-off $a_j^+$ in a normal direction.

**Theorem (the Seifert matrix and the Alexander polynomial).** Let $V$ be a Seifert matrix of the knot $K$. Then

$$
\Delta_K(t) \doteq \det(t^{1/2}V - t^{-1/2}V^{\mathsf{T}})
$$

up to multiplication by a unit $\pm t^{k}$, where $\Delta_K$ is the **Alexander polynomial**; it satisfies $\Delta_K(t)\doteq\Delta_K(t^{-1})$ and $\Delta_K(1) = \pm1$, and the determinant of the knot is $|\Delta_K(-1)|$. The **signature** $\sigma(K)$ is the signature of the symmetric matrix $V + V^{\mathsf{T}}$, an even integer, and it is a concordance invariant.

**Proof sketch.** The Alexander polynomial is computed from a presentation of the Alexander module $H_1$ of the infinite cyclic cover of the complement, obtained from a Seifert surface by the Fox calculus; the Seifert matrix computes the linking form on the surface, and the determinant formula for the Alexander polynomial is the resulting statement. The symmetry and the value at $1$ are formal properties of the determinant. $\square$

**Example.** The torus knot $T(p,q)$ with $p,q$ coprime has Alexander polynomial

$$
\Delta_{T(p,q)}(t) \doteq \frac{(t^{pq}-1)(t-1)}{(t^p-1)(t^q-1)} ,
$$

so that $\Delta_{3_1}(t) = t^2-t+1$, $\Delta_{5_1}(t) = t^4-t^3+t^2-t+1$, and $|\Delta_{T(p,q)}(-1)| = 3$ for $(p,q)=(2,3)$, $5$ for $(2,5)$ and $3$ for $(3,4)$, computed by the formula; the determinants of these knots are $3$, $5$ and $3$ respectively. The figure-eight knot has $\Delta_{4_1}(t) \doteq t^2-3t+1$, so its determinant is $\Delta_{4_1}(-1) = 5$. The Conway polynomial $\nabla_K(z)$ is the normalisation $\nabla_K(z) = \Delta_K(t)$ with $t^{1/2}-t^{-1/2} = z$, so that $\nabla_{3_1}(z) = z^2+1$ and $\nabla_{4_1}(z) = 1-z^2$; the coefficients $a_n$ of $\nabla$ are the **Conway coefficients**, and the coefficient $a_2$ is the Arf invariant of the knot modulo $2$.

**Theorem (fibered knots).** A knot $K$ is **fibered** if its complement fibres over the circle with the Seifert surface as fibre; equivalently $S^3\setminus K$ is a surface bundle over $S^1$ with fibre a once-punctured surface. Then the monodromy of the bundle is a diffeomorphism of the fibre, well defined up to isotopy and conjugation, and the Alexander polynomial is the characteristic polynomial of the induced map on the homology of the fibre; the pseudo-Anosov monodromies give the hyperbolic fibered knots, whose geometry is that of the mapping torus of *Mapping Class Groups*.

**Proof sketch.** The fibration is obtained from a Seifert surface that is incompressible and whose complement in $S^3\setminus K$ is an open interval bundle; the monodromy is the return map of the flow transverse to the surface, and its homology action computes the Alexander polynomial. The classification of the monodromies is that of the mapping class group of the fibre, treated in the final article of this half. $\square$

## The Jones, HOMFLY and Kauffman Invariants

**Definition.** The **Jones polynomial** $V_L(t)$ is the Laurent polynomial in $t^{1/2}$ determined by the skein relation

$$
t^{-1}V_{L_+}(t) - t\,V_{L_-}(t) = (t^{1/2} - t^{-1/2})\,V_{L_0}(t)
$$

together with the normalisation $V_{\text{unknot}}(t) = 1$, where $L_+,L_-,L_0$ are the three links obtained from a local crossing by the positive, negative and smoothed resolutions. The **HOMFLY polynomial** $P_L(a,z)$ is the two-variable refinement defined by $a^{-1}P_{L_+} - aP_{L_-} = zP_{L_0}$ with $P_{\text{unknot}}=1$, and the **Kauffman polynomial** is the two-variable invariant defined from the Kauffman bracket and the writhe.

**Theorem (Kauffman; the bracket and the writhe).** The **Kauffman bracket** $\langle D\rangle$ of a diagram is the state sum

$$
\langle D\rangle = \sum_{s} A^{a(s)-b(s)}(-A^2-A^{-2})^{|s|-1},
$$

over the states $s$ of the diagram, where $a(s)$ and $b(s)$ count the two kinds of smoothing, $|s|$ the number of resulting circles and $A$ the bracket variable; it is invariant under the second and third Reidemeister moves and changes by $-A^{\pm3}$ under the first. Consequently the normalised invariant

$$
V_L(t) = (-A^3)^{-w(D)}\langle D\rangle\Big|_{A = t^{-1/4}} ,
$$

with $w(D)$ the writhe of the diagram, is invariant under all three moves, and it is the Jones polynomial.

**Proof sketch.** The state sum is computed by an induction on the crossings, and the invariance under $R_2$ and $R_3$ is a direct check of the state sums; the failure of the invariance under $R_1$ is exactly measured by the writhe, so that the normalised quantity is invariant. The identification with the skein-theoretic Jones polynomial is the skein relation satisfied by the bracket. $\square$

**Example.** The Jones polynomial of the trefoil and of the figure-eight knot are

$$
V_{3_1}(t) = -t^{-4} + t^{-3} + t^{-1}, \qquad V_{4_1}(t) = t^{-2} - t^{-1} + 1 - t + t^2 ,
$$

for the right-handed orientation of the trefoil; the mirror image of the trefoil has $V_{\bar{3_1}}(t) = V_{3_1}(t^{-1}) = -t^4+t^3+t$, which is different, so the Jones polynomial detects the chirality of the trefoil; the figure-eight satisfies $V_{4_1}(t^{-1}) = V_{4_1}(t)$, in agreement with its amphichirality. The evaluations are consistent with the general identities $V_L(1) = 1$ for a knot, $V_L'(1) = 0$ and $V_L''(1) = -6a_2(L)$, where $a_2$ is the coefficient of $z^2$ in the Conway polynomial: for the trefoil $a_2 = 1$ and $V_{3_1}''(1) = -6$, and for the figure-eight $a_2 = -1$ and $V_{4_1}''(1) = 6$.

**Theorem (Tait conjectures; Kauffman, Murasugi, Thistlethwaite).** Let $D$ be a reduced alternating diagram of a link $L$. Then:

**(a)** the number of crossings of $D$ is the crossing number of $L$, so a reduced alternating diagram is minimal;

**(b)** two reduced alternating diagrams of the same link have the same writhe and the same number of crossings;

**(c)** the crossing number of $D$ is the span of the Kauffman bracket and, after the change of variable, the span of the Jones polynomial, where the span is the difference between the maximal and the minimal degree.

**Proof sketch.** All three statements are proved by the analysis of the Kauffman bracket state sum at the two extreme states: the maximum and minimum degrees of the bracket are attained by the two constant states, and the difference of the degrees is the number of crossings for a reduced alternating diagram. The first statement then follows from the invariance of the bracket up to the writhe, together with the fact that no diagram of a link can have fewer crossings than the span of its bracket. $\square$

**Example.** The span of the Jones polynomial of the trefoil is $-1-(-4) = 3$, equal to its crossing number; the span for the figure-eight is $2-(-2)=4$, equal to its crossing number; and the cinquefoil $5_1=T(2,5)$ has Jones polynomial

$$
V_{5_1}(t) = -t^{-7} + t^{-6} - t^{-5} + t^{-4} + t^{-2},
$$

whose span is $-2-(-7) = 5$, equal to its crossing number. In each case the Tait conjecture computes the crossing number from the Jones polynomial, and the identities $V_{5_1}(1)=1$ and $V_{5_1}''(1) = -6a_2 = -18$ hold, with $a_2=3$ the coefficient of $z^2$ in the Conway polynomial $\nabla_{5_1}(z) = z^4+3z^2+1$.

**Remark (the structural explanation).** The Jones polynomial is not merely a skein-theoretic curiosity: it is the invariant of the quantum group $U_q(\mathfrak{sl}_2)$ at a root of unity, obtained from the representation theory of the quantum deformation by the Reshetikhin–Turaev construction, and the HOMFLY polynomial arises from $U_q(\mathfrak{gl}_n)$ in the same way. The Temperley–Lieb algebra, the Hecke algebra and their representations are the algebraic home of the bracket and the skein relations, and the braid group representations thereby obtained are the source of the quantum invariants; the braid groups and their representations are treated in *Mapping Class Groups*, and the Lie-theoretic background in Part I.

## Categorification and the Detection Theorems

**Theorem (Ozsváth–Szabó; knot Floer homology).** To a knot $K\subseteq S^3$ one attaches a bigraded homology $\widehat{HFK}(K)$, the **knot Floer homology**, whose Euler characteristic with respect to one of the gradings is the Alexander polynomial:

$$
\sum_{i,j}(-1)^i\,\mathrm{rk}\,\widehat{HFK}_i(K,j)\,t^j = \Delta_K(t) .
$$

Knot Floer homology detects the Seifert genus, the fibredness and the unknot: $g(K)$ is the maximal $j$ with $\widehat{HFK}(K,j)\neq0$, the knot is fibered if and only if the top grading has rank one, and $K$ is the unknot if and only if $\widehat{HFK}(K)$ has rank one. The construction is the Lagrangian Floer theory of the symmetric product of a Heegaard surface, in the sense of *Floer Homology*.

**Proof sketch.** The knot Floer complex is constructed from a Heegaard diagram adapted to the knot, with the knot traced on the Heegaard surface as an extra curve; the Euler characteristic computation is the theorem of Ozsváth–Szabó identifying the Euler characteristic of the complex with the Alexander polynomial, and the detection statements are proved by the adjunction inequalities of the theory and the surgery exact triangle. $\square$

**Theorem (Khovanov; Lee; Rasmussen).** To a link diagram one attaches a bigraded chain complex whose homology $\mathrm{Kh}(L)$ — the **Khovanov homology** — is an invariant of the link, categorifies the Jones polynomial, in the sense that its graded Euler characteristic is

$$
\sum_{i,j}(-1)^i\,\mathrm{rk}\,\mathrm{Kh}^{i,j}(L)\,q^j = (q+q^{-1})\,V_L(q^{-2}) ,
$$

and is functorial under link cobordisms. The Lee deformation of the complex has homology of rank $2^{|L|}$ concentrated in the two extremal gradings, and the **Rasmussen invariant** $s(K)$ extracted from it satisfies

$$
|s(K)| \leq 2g_4(K)
$$

for the **smooth slice genus** $g_4(K)$, the minimal genus of a smoothly embedded oriented surface in the four-ball with boundary $K$. Consequently $s$ and the knot Floer invariant $\tau$ of *Floer Homology* give lower bounds for the slice genus, and $s$ is a homomorphism from the concordance group to $\mathbb{Z}$.

**Proof sketch.** The Khovanov complex is built from the Kauffman bracket by replacing each state sum with a chain group and each smoothing with a map; the invariance under the Reidemeister moves is a chain-homotopy computation, and the graded Euler characteristic is the bracket by construction. The Lee deformation introduces a filtered differential whose homology is computed explicitly, and the Rasmussen invariant is its evaluation on the generator; the slice-genus inequality follows from the functoriality applied to a slice surface for $K$, whose induced map must respect the filtration. $\square$

**Theorem (Milnor conjecture; Kronheimer–Mrowka; Rasmussen).** For the torus knot $T(p,q)$ the Seifert genus equals the smooth slice genus,

$$
g_4(T(p,q)) = g(T(p,q)) = \frac{(p-1)(q-1)}{2},
$$

and the unknotting number is $u(T(p,q)) = \frac{(p-1)(q-1)}{2}$. The equality of the Seifert genus and the smooth slice genus, and the unknotting number formula, were proved by Kronheimer and Mrowka by gauge theory, using the analysis of the moduli spaces of the Seiberg–Witten equations of Part III; Rasmussen gave a second proof of the slice-genus statement by the $s$-invariant of Khovanov homology.

**Proof sketch.** The lower bound for the slice genus is supplied by the Rasmussen invariant, which evaluates to $s(T(p,q)) = (p-1)(q-1)$ for the standard orientation, so that $g_4\geq(p-1)(q-1)/2$; the Seifert surface of the torus knot realises the genus, so the bound is sharp, and the same argument applied to the unknotting inequality gives the unknotting number. The gauge-theoretic proof of Kronheimer–Mrowka uses the property that the Seiberg–Witten invariant of the knot complement detects the minimal genus of a surface representing a given class. $\square$

**Remark.** The two categorifications are not independent: the Khovanov homology categorifies the Jones polynomial and the knot Floer homology categorifies the Alexander polynomial, and there is a spectral sequence from the Khovanov homology to the knot Floer homology, constructed by Ozsváth–Szabó and by Rasmussen; the spectral sequence is the structural bridge between the quantum and the Floer-theoretic invariants. The detection theorems at the two ends are the sharpest known applications of the categorified invariants: the unknot detection and the genus detection at the Floer end, the slice-genus bound and the smooth four-ball genus at the Khovanov end.

## The Geometry of Knot Complements

**Theorem (JSJ decomposition and the geometrisation of knot complements).** Let $K\subseteq S^3$ be a knot with complement $M_K = S^3\setminus K$, a compact three-manifold with torus boundary. Then $M_K$ has a unique torus decomposition into pieces that are Seifert fibred or hyperbolic. A knot is

**(a)** a **torus knot** if and only if $M_K$ is Seifert fibred, and then $M_K$ carries the $\widetilde{SL_2(\mathbb{R})}$ geometry: equivalently the universal cover of $S^3\setminus T(p,q)$ is $\widetilde{SL_2(\mathbb{R})}$, the universal cover of $SL_2(\mathbb{R})$;

**(b)** a **satellite** knot if and only if $M_K$ contains an essential torus that is not boundary-parallel;

**(c)** a **hyperbolic knot** if and only if $M_K$ is hyperbolic of finite volume, and then the hyperbolic structure is unique by Mostow rigidity.

**Proof sketch.** The decomposition is the Jaco–Shalen–Johannson theorem applied to the knot complement, whose torus boundary is the peripheral torus; the Seifert fibred case is classified by the Seifert invariants, and the hyperbolic case is the subject of *Low-Dimensional Topology* and *Hyperbolic Geometry*. $\square$

**Example.** The figure-eight knot $4_1$ is the simplest hyperbolic knot: its complement is the union of two regular ideal tetrahedra and has volume $2.0298832\ldots$, and it is the orientable cusped hyperbolic three-manifold with one cusp of minimal volume. The trefoil and the cinquefoil are torus knots and their complements are Seifert fibred; a satellite or composite knot is exactly a knot whose complement contains an essential torus that is not boundary-parallel; so by the torus decomposition the complement of a knot is Seifert fibred, or hyperbolic, or contains an essential torus, according as the knot is a torus knot, a hyperbolic knot, or a satellite or composite knot. The list of hyperbolic knots begins with $4_1$, $5_2$, $6_1$, $6_2$, $6_3$, and the tabulation of the hyperbolic volume against the crossing number is one of the standard computations of the low-dimensional theory.

**Remark (the hyperbolic volume as an invariant).** The volume of a hyperbolic knot complement is a topological invariant of the knot by Mostow rigidity, and the volumes of the hyperbolic knots form a well-ordered subset of the positive reals (Jørgensen–Thurston): every nonempty set of volumes has a least element, so that for each bound there are only finitely many hyperbolic knots below it. The volume is thus a subtle invariant that separates knots which the polynomial invariants do not, and the figure-eight knot complement is the cusped hyperbolic three-manifold with one cusp of minimal volume (Meyerhoff; Gabai–Meyerhoff–Milley), so the figure-eight knot is the unique knot of minimal volume. The computation of the volumes is the union of the Neumann–Zagier formula, which expresses the volume as an analytic function of the cusp shape, and the arithmetic of the resulting ideal triangulations.

## Concordance and the Slice Genus

**Definition.** Two knots $K_0, K_1$ are **concordant** if there is a smoothly embedded annulus $S^1\times I\subseteq S^3\times I$ meeting the boundary spheres in the knots; the set of concordance classes forms an abelian group $\mathcal{C}$ under connected sum, the **concordance group**, with the **slice knots** — those bounding a smoothly embedded disc in the four-ball — as the identity class. The smooth slice genus $g_4(K)$, the minimal genus of a smoothly embedded oriented surface in the four-ball with boundary $K$, vanishes exactly on the identity class, and the classical invariants factor through $\mathcal{C}$: the signature $\sigma$, the Alexander polynomial of the connected sum and the Conway coefficients are concordance invariants, and $\mathcal{C}$ has infinite rank by the arguments of Fox–Milnor and Tristram using the signature and the Alexander polynomial.

**Theorem (concordance invariants).** The map $K\mapsto\sigma(K)$ is a homomorphism $\mathcal{C}\to\mathbb{Z}$; the Alexander polynomial satisfies $\Delta_{K_1\#K_2} = \Delta_{K_1}\Delta_{K_2}$; the Fox–Milnor condition $\Delta_K(t)\doteq f(t)f(t^{-1})$ is necessary for $K$ to be slice; and the invariants $\tau$ of knot Floer homology and $s$ of Khovanov homology are concordance homomorphisms giving the bounds $|\tau(K)|\leq g_4(K)$ and $|s(K)|\leq 2g_4(K)$.

**Proof sketch.** The additivity of the signature and of the Alexander polynomial under connected sum is a Seifert-matrix computation; the Fox–Milnor condition follows from the fact that a slice disc has a complement with the homology of a circle, so that the infinite cyclic cover of the slice-disc complement gives a factorisation of the Alexander polynomial; the bounds from $\tau$ and $s$ are the slice-genus inequalities of the categorified invariants, applied to a slice surface. $\square$

**Theorem (the slice-ribbon conjecture; open).** Every slice knot bounds a ribbon disc, that is, a smoothly embedded disc whose singularities are of the simplest possible type — a self-transverse immersed disc with only ribbon singularities. The conjecture is open in general; it has been verified for large families, in particular for all the knots of up to a substantial number of crossings and for the two-bridge and the alternating families with the appropriate hypotheses.

**Proof sketch.** The known cases are obtained by the classification of the slice discs in the relevant families and by the computation of the concordance invariants; the general statement remains one of the central open problems of the concordance theory, and its failure would produce a slice knot with no ribbon representative. $\square$

## Summary

A knot is a circle in $S^3$; knots are studied through their diagrams and the Reidemeister moves, through the complement and its fundamental group, and through the invariants computed from Seifert surfaces and from skein relations. The complement determines the knot by Gordon–Luecke, and the knot group, the Seifert genus and the Seifert matrix are the classical invariants of the complement; the Alexander polynomial is the determinant of the Seifert matrix, the signature is the signature of $V+V^{\mathsf{T}}$, and the Conway coefficients encode the same information. The Jones, HOMFLY and Kauffman polynomials are the quantum invariants, obtained from the Kauffman bracket by the writhe normalisation and structurally from the representations of the quantum groups; the Tait conjectures, proved from the bracket, compute the crossing number of a reduced alternating diagram and confirm the tabulation of the alternating knots.

The two categorifications dominate the modern theory: the knot Floer homology categorifies the Alexander polynomial and detects the genus, the fibredness and the unknot; the Khovanov homology categorifies the Jones polynomial, is functorial for cobordisms, and produces the Rasmussen invariant whose bound $|s|\leq2g_4$ proves the Milnor conjecture on the slice genus and the unknotting number of the torus knots, $g_4(T(p,q)) = u(T(p,q)) = (p-1)(q-1)/2$. Geometrically, a knot complement is Seifert fibred exactly when the knot is a torus knot, is a satellite exactly when it contains an essential torus, and is hyperbolic otherwise; the figure-eight knot is the simplest hyperbolic knot, of volume $2.0298832\ldots$, and the hyperbolic volume is a topological invariant which by Mostow rigidity admits no deformation. The concordance group organises the invariants into homomorphisms, and the slice-ribbon conjecture remains open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$, $L$, $S^3$ | Knot or link in the three-sphere; components of a link |
| $c(K)$, $u(K)$, $g(K)$ | Crossing number, unknotting number, Seifert genus |
| $M_K = S^3\setminus K$ | Knot complement; $\pi_K = \pi_1(M_K)$ the knot group |
| Wirtinger presentation | Generators the arcs, relations the crossings of a diagram |
| Seifert surface $F$, Seifert matrix $V$ | Oriented surface with $\partial F=K$; $V_{ij}=\mathrm{lk}(a_i,a_j^+)$ |
| $\Delta_K(t)$, $\nabla_K(z)$ | Alexander polynomial; Conway polynomial, $\nabla_K(z)=\Delta_K$ with $t^{1/2}-t^{-1/2}=z$ |
| $|\Delta_K(-1)|$, $\sigma(K)$ | Knot determinant; signature of $V+V^{\mathsf{T}}$ |
| $V_L(t)$, $P_L(a,z)$ | Jones polynomial; HOMFLY polynomial |
| $\langle D\rangle$, $A$, $w(D)$ | Kauffman bracket, bracket variable, writhe; $V=(-A^3)^{-w}\langle D\rangle$ |
| $T(p,q)$ | Torus knot; $\Delta_{T(p,q)}\doteq(t^{pq}-1)(t-1)/((t^p-1)(t^q-1))$ |
| $L_+,L_-,L_0$ | Positive, negative and smoothed resolutions in the skein relations |
| $\widehat{HFK}(K)$ | Knot Floer homology; Euler characteristic $\Delta_K$, detects $g$, fibredness, the unknot |
| $\mathrm{Kh}(L)$, $s(K)$ | Khovanov homology categorifying $V_L$; Rasmussen invariant, $|s(K)|\leq2g_4(K)$ |
| $\mathcal{C}$, $g_4(K)$ | Concordance group; smooth slice genus; $\sigma,\tau,s$ the concordance homomorphisms |
| $T(p,q)$ slice genus | $g_4(T(p,q))=(p-1)(q-1)/2$ (Milnor conjecture; Kronheimer–Mrowka, Rasmussen) |



## Further Reading

- Kurt Reidemeister, *Knotentheorie* (Springer, 1932), for the diagrams and the three moves and the tabulation of the small knots.
- Cameron Gordon and John Luecke, "Knots Are Determined by Their Complements", *Topology* 28 (1989), 533–541, for the completeness of the complement as an invariant.
- Ralph Fox, "A Quick Trip Through Knot Theory", in *Topology of 3-Manifolds and Related Topics* (Prentice-Hall, 1962), 120–167, for the Fox calculus, the Alexander module and the Seifert matrix.
- Vaughan Jones, "A Polynomial Invariant for Knots via von Neumann Algebras", *Bulletin of the American Mathematical Society* 12 (1985), 103–111, for the Jones polynomial; and Louis Kauffman, "State Models and the Jones Polynomial", *Topology* 26 (1987), 395–407, for the bracket and the proof of the Tait conjectures.
- Morwen Thistlethwaite, "A Spanning Tree Expansion of the Jones Polynomial", *Topology* 26 (1987), 297–309, and Kunio Murasugi, "Jones Polynomials and Classical Conjectures in Knot Theory", *Topology* 26 (1987), 187–194, for the crossing number of alternating links.
- Peter Ozsváth and Zoltán Szabó, "Holomorphic Disks and Genus Bounds", *Geometry and Topology* 8 (2004), 615–637, for knot Floer homology and the genus and fibring detection.
- Mikhail Khovanov, "A Categorification of the Jones Polynomial", *Duke Mathematical Journal* 101 (2000), 359–426, and Eun Soo Lee, "An Endomorphism of the Khovanov Invariant", *Advances in Mathematics* 200 (2006), 303–324, and Jacob Rasmussen, "Khovanov Homology and the Slice Genus", *Proceedings of the National Academy of Sciences* 101 (2004), 570–574, for Khovanov homology, its Lee deformation and the slice-genus bound.
- Peter Kronheimer and Tomasz Mrowka, "Gauge Theory for Embedded Surfaces I–II", *Topology* 32 (1993), 773–826 and 34 (1995), 37–97, for the gauge-theoretic proof of the Milnor conjecture on the genus of the torus knots.
- Akio Kawauchi, *A Survey of Knot Theory* (Birkhäuser, 1996), for the concordance group, the satellite construction and the slice-ribbon problem.
