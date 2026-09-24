
# __Čech Cohomology__

## Introduction

Sheaf cohomology, as constructed in *Sheaf Cohomology*, is defined by injective resolutions and is therefore not immediately computable. **Čech cohomology** is the computable approximation: for an open cover $\mathcal{U} = \{U_i\}_{i\in I}$ of a space $X$ and a sheaf $\mathcal{F}$, one forms the cochain complex

$$
0 \to \prod_i \mathcal{F}(U_i) \to \prod_{i<j}\mathcal{F}(U_i\cap U_j) \to \prod_{i<j<k}\mathcal{F}(U_i\cap U_j\cap U_k) \to \cdots,
$$

whose cohomology $\check H^p(\mathcal{U},\mathcal{F})$ is read off from the sections of $\mathcal{F}$ on the members of the cover and their finite intersections, and whose failure to be exact measures the failure of the local sections to glue. The complex is finite when the cover is finite, its terms are groups of sections rather than abstract derived objects, and in degree one its cohomology is exactly the obstruction to gluing: $\check H^1(\mathcal{U},\mathcal{F})$ is the quotient of the group of gluing data on the cover by the gluing data that come from local sections, so that a class in $\check H^1$ is a "twisted" piece of the sheaf. Passing to all refinements of the cover removes the dependence on $\mathcal{U}$ and produces an invariant $\check H^p(X,\mathcal{F})$ of the pair $(X,\mathcal{F})$, which for a good cover coincides with the sheaf cohomology, and for a paracompact space coincides with it always.

The article develops the theory in the order in which it is used. The first section defines the Čech complex of a cover, verifies that it is a complex, identifies its degree-zero cohomology with the global sections of a sheaf, and interprets degree one as gluing data. The second section describes refinements and the direct limit over them, with the computations on a basis that make Čech cohomology the working tool of the subject. The third section proves the **Leray theorem**: if every nonempty finite intersection of members of the cover is acyclic for $\mathcal{F}$, the Čech cohomology of the cover is the sheaf cohomology of $\mathcal{F}$, a statement whose proof is the degeneration of the Čech-to-derived spectral sequence, and which is the reason the theorem is stated in every account of the subject. The fourth section identifies the Čech complex of a cover by acyclic sets with the cochain complex of its **nerve**, which places the computations of *Simplicial and Singular Homology* and of *CW Complexes and Cellular Approximation* at the disposal of sheaf theory and explains why the Čech complex sees the cohomology of the space rather than of the cover. The fifth section collects the applications: to the cohomology of spheres and projective spaces, to the exponential sequence and the Picard group, to the classification of torsors, and to the double complex that compares the Čech and de Rham complexes.

The general homological algebra used — complexes, derived functors, spectral sequences — is Part I's *Homological Algebra*, *Derived Functors* and *Spectral Sequences*; the sheaf-theoretic results used — stalks, sheafification, flabby and soft sheaves, the comparison with singular cohomology — are *Presheaves and Sheaves* and *Sheaf Cohomology*. The Grothendieck topologies for which the Čech construction is one among several are Part I's *Sheaves on Sites*, and the descent-theoretic interpretation is *Descent Theory* of Part I; here the site is the poset of open sets with its open covers, as in the previous two articles.

Throughout, $\mathcal{U} = \{U_i\}_{i\in I}$ is an open cover of $X$, $\mathcal{F}$ is a sheaf of abelian groups on $X$, and for a finite subset $I' = \{i_0 < i_1 < \cdots < i_p\} \subseteq I$ one writes

$$
U_{i_0\ldots i_p} = U_{i_0}\cap\cdots\cap U_{i_p}, \qquad \mathcal{F}(U_{i_0\ldots i_p}) = \Gamma(U_{i_0\ldots i_p},\mathcal{F}),
$$

with the convention that $\mathcal{F}(\emptyset) = 0$. The cohomology with a comma is sheaf cohomology, as fixed in *Sheaves and Cohomology*; the Čech groups are written with a check, $\check H^p$.

## The Čech Complex of a Cover

**Definition.** Let $\mathcal{U} = \{U_i\}_{i\in I}$ be an open cover, ordered by a fixed total order on $I$, which exists by the well-ordering of $I$ but has no further significance. The **Čech complex** of $\mathcal{U}$ with coefficients in $\mathcal{F}$ is the cochain complex $\check C^\bullet(\mathcal{U},\mathcal{F})$ of abelian groups

$$
\check C^p(\mathcal{U},\mathcal{F}) = \prod_{i_0<\cdots<i_p}\mathcal{F}(U_{i_0\ldots i_p}), \qquad p \geq 0,
$$

whose differential $\delta : \check C^p \to \check C^{p+1}$ is

$$
(\delta s)_{i_0\ldots i_{p+1}} = \sum_{k=0}^{p+1}(-1)^k\, s_{i_0\ldots \hat{i_k}\ldots i_{p+1}}\Big|_{U_{i_0\ldots i_{p+1}}},
$$

the hat meaning that the index is omitted and the vertical bar meaning restriction of a section of $\mathcal{F}$. The **Čech cohomology of the cover** is $\check H^p(\mathcal{U},\mathcal{F}) = H^p(\check C^\bullet(\mathcal{U},\mathcal{F}))$.

**Proposition.** $\delta \circ \delta = 0$, so that the Čech groups are defined.

*Proof.* The terms of $(\delta\delta s)_{i_0\ldots i_{p+2}}$ are indexed by ordered pairs of omissions $(\hat{i_k},\hat{i_l})$ with $k<l$, and the pair occurs once as $\hat{i_k}$ followed by $\hat{i_l}$ in $\delta$ applied to $(\delta s)$ with sign $(-1)^k(-1)^{l-1}$ and once in the other order with sign $(-1)^l(-1)^k$; the signs are opposite, and the restrictions agree because restriction maps commute, so the sum cancels. $\square$

**Theorem (degree zero and degree one).** Let $\mathcal{U}$ be an open cover.

1. If $\mathcal{F}$ is a sheaf then $\check H^0(\mathcal{U},\mathcal{F}) = \Gamma(X,\mathcal{F})$, and the identification is the map sending a global section to the family of its restrictions. For a presheaf the same formula holds with $\Gamma$ denoting the presheaf sections, and the degree-zero Čech group is then the group of matching families.
2. $\check H^1(\mathcal{U},\mathcal{F})$ is the quotient of the group
   $$Z^1 = \Bigl\{(s_{ij}) \in \prod_{i<j}\mathcal{F}(U_{ij}) : s_{jk}|_{U_{ijk}} - s_{ik}|_{U_{ijk}} + s_{ij}|_{U_{ijk}} = 0 \text{ for all } i<j<k\Bigr\}$$
   by the subgroup of **coboundaries** $s_{ij} = t_j|_{U_{ij}} - t_i|_{U_{ij}}$ for a family $(t_i) \in \prod_i\mathcal{F}(U_i)$. The class of a cocycle $(s_{ij})$ vanishes if and only if the gluing data it represents are trivial, in the sense that the locally defined sections can be adjusted on the members of the cover to a global section; if $\mathcal{U}$ is a cover by two sets with connected intersection and $\mathcal{F}$ is a sheaf, then $\check H^1(\mathcal{U},\mathcal{F}) = \operatorname{coker}\bigl(\mathcal{F}(U_0)\oplus\mathcal{F}(U_1)\to\mathcal{F}(U_{01})\bigr)$.

*Proof.* (1) The kernel of $\delta : \check C^0 \to \check C^1$ consists of families $(s_i)$ with $s_i|_{U_{ij}} = s_j|_{U_{ij}}$, which by the sheaf condition is exactly $\Gamma(X,\mathcal{F})$, the existence and uniqueness clauses of *Presheaves and Sheaves* giving surjectivity and injectivity respectively. (2) is the definition unwound, the cocycle condition being $\delta s = 0$ in degree two and the coboundaries being the image of $\delta$ in degree zero. $\square$

**Example (the two-set cover of the circle).** Let $X = S^1 = U_0\cup U_1$ with $U_0, U_1$ open arcs whose intersection is the disjoint union $W_1\sqcup W_2$ of two intervals. Then $\check C^0 = \mathbb{Z}\oplus\mathbb{Z}$ and $\check C^1 = \mathbb{Z}\oplus\mathbb{Z}$, the differential in the alternating convention being $\delta(a_0,a_1) = (a_1-a_0, a_1-a_0)$ on the two components of the intersection, since a constant restricts to the same constant on each component. Hence

$$
\check H^0(\mathcal{U},\underline{\mathbb{Z}}) = \mathbb{Z}, \qquad \check H^1(\mathcal{U},\underline{\mathbb{Z}}) = \mathbb{Z}, \qquad \check H^p(\mathcal{U},\underline{\mathbb{Z}}) = 0 \ (p \geq 2),
$$

in agreement with $H^*(S^1;\mathbb{Z})$. The example shows that a cover by two sets meeting in two components computes the cohomology correctly: the acyclicity hypothesis of the Leray theorem below is satisfied, each of $U_0$, $U_1$ and each component of their intersection being contractible, so the theorem applies and predicts exactly this answer. The point of the example is that the intersections in a Čech cover need not be connected, and that the *alternating* convention is what handles this, since each component of an intersection contributes its own coordinate to $\check C^1$.

**Remark (the ordered and the alternating complex).** One may also form the complex with $\tilde C^p(\mathcal{U},\mathcal{F}) = \prod_{(i_0,\ldots,i_p)\in I^{p+1}}\mathcal{F}(U_{i_0\ldots i_p})$ over all ordered tuples, with the same differential; the inclusion of the alternating subcomplex is a quasi-isomorphism, since the extra terms with repeated indices are contractible by a "normalisation" homotopy. The alternating convention is used throughout this article because it is the one whose terms are indexed by the *cells of the nerve*, as the fourth section explains.

## Refinements and the Direct Limit

**Definition.** A cover $\mathfrak{V} = \{V_j\}_{j\in J}$ **refines** $\mathcal{U} = \{U_i\}_{i\in I}$, written $\mathfrak{V} \preceq \mathcal{U}$, if there is a map $\varphi : J \to I$ with $V_j \subseteq U_{\varphi(j)}$ for every $j$. The choice of $\varphi$ gives a **refinement map** of complexes

$$
\check C^\bullet(\mathcal{U},\mathcal{F}) \to \check C^\bullet(\mathfrak{V},\mathcal{F}), \qquad (s_{i_0\ldots i_p}) \mapsto \Bigl(\varphi: (j_0<\cdots<j_p) \mapsto s_{\varphi(j_0)\ldots\varphi(j_p)}\big|_{V_{j_0\ldots j_p}}\Bigr),
$$

which is a morphism of complexes; two choices of $\varphi$ are chain homotopic, so the induced map on cohomology depends only on the refinement relation.

**Definition.** The **Čech cohomology of $X$** with coefficients in $\mathcal{F}$ is the filtered colimit

$$
\check H^p(X,\mathcal{F}) = \varinjlim_{\mathcal{U}}\check H^p(\mathcal{U},\mathcal{F})
$$

over the directed set of open covers of $X$ ordered by refinement. The natural maps $\check H^p(\mathcal{U},\mathcal{F})\to\check H^p(X,\mathcal{F})$ are compatible with the refinement maps, and $\check H^0(X,\mathcal{F}) = \Gamma(X,\mathcal{F})$ for a sheaf $\mathcal{F}$ by the first theorem.

**Theorem (properties of the limit).** Let $\mathcal{F}$ be a sheaf of abelian groups on $X$.

1. $\check H^p(X,\mathcal{F})$ depends only on the sheaf associated with a presheaf: for a presheaf $\mathcal{P}$ with associated sheaf $\mathcal{P}^{+}$ there is a natural isomorphism $\check H^p(X,\mathcal{P}) \cong \check H^p(X,\mathcal{P}^{+})$, since the two presheaves have the same stalks, a Čech class is represented by data on a cover, and the two complexes agree after refining.
2. A short exact sequence $0\to\mathcal{F}\to\mathcal{G}\to\mathcal{H}\to 0$ of sheaves induces a long exact sequence
   $$\cdots \to \check H^p(X,\mathcal{F}) \to \check H^p(X,\mathcal{G}) \to \check H^p(X,\mathcal{H}) \to \check H^{p+1}(X,\mathcal{F}) \to \cdots,$$
 because for a fixed cover the Čech construction is a complex of exact functors in the sheaf variable, and filtered colimits are exact in the category of abelian groups.
3. If $X$ has a basis $\mathcal{B}$ closed under finite intersections, the covers by members of $\mathcal{B}$ are cofinal in the directed set of all covers, so $\check H^p(X,\mathcal{F})$ may be computed from covers by members of $\mathcal{B}$. In particular, for a manifold the covers by domains of charts are cofinal, and for a ringed space the covers by distinguished open sets are cofinal.
4. $\check H^0(X,\mathcal{F}) = \Gamma(X,\mathcal{F})$ and there is a natural map $\check H^p(X,\mathcal{F}) \to H^p(X,\mathcal{F})$, which is an isomorphism for $p = 0$, injective for $p = 1$, and an isomorphism in all degrees when $X$ is paracompact.

*Proof.* (1) The canonical map $\mathcal{P}\to\mathcal{P}^{+}$ is an isomorphism on stalks, hence its cone has zero cohomology as a map of complexes after refining the cover; passing to the limit over refinements gives the isomorphism. (2) For a fixed cover the Čech construction is a complex of exact functors in the sheaf variable, and the filtered colimit over refinements is exact in the category of abelian groups, so a short exact sequence of sheaves gives a long exact sequence of limit Čech groups. (3) Every open set is a union of members of $\mathcal{B}$ and, $\mathcal{B}$ being closed under finite intersections, the intersections of members of the refined cover are members of $\mathcal{B}$. (4) The first statement is (1) of the previous theorem; the comparison map exists because the Čech complex of a flabby resolution computes the sheaf cohomology, and its properties in low degrees and the paracompact case are Godement's theorem, quoted. $\square$

**Remark (the degree-one statement).** The injectivity of $\check H^1(X,\mathcal{F}) \to H^1(X,\mathcal{F})$ is the precise form of the statement that every Čech class of a refinement-stable cocycle is a genuine cohomology class; it is used to identify the Picard group with a Čech $H^1$ in the applications below. Surjectivity in degree one requires the existence of enough sections and holds, for instance, when $X$ is paracompact.

## The Leray Theorem and the Spectral Sequence

**Theorem (the Čech-to-derived spectral sequence).** Let $\mathcal{U}$ be an open cover of $X$ and let $\underline{H}^q(\mathcal{F})$ denote the **presheaf** $U\mapsto H^q(U,\mathcal{F})$ of sheaf cohomology, with $\underline{H}^0(\mathcal{F}) = \mathcal{F}$. There is a spectral sequence of cohomological type

$$
E_2^{p,q} = \check H^p\bigl(\mathcal{U}, \underline{H}^q(\mathcal{F})\bigr) \Longrightarrow H^{p+q}(X,\mathcal{F}),
$$

natural in $\mathcal{U}$ and $\mathcal{F}$, converging to the sheaf cohomology of $\mathcal{F}$; it is a spectral sequence of a double complex, the **Čech–de Rham double complex**, and its first-quadrant form is that of *Spectral Sequences* of Part I.

*Proof sketch.* Form the double complex $K^{p,q} = \check C^p(\mathcal{U}, \mathcal{Q}^q)$ for a resolution $\mathcal{Q}^\bullet$ of $\mathcal{F}$ by injectives, with the Čech differential in $p$ and the resolution differential in $q$. The spectral sequence of the double complex filtered by the total degree has $E_1^{p,q} = \check C^p(\mathcal{U},\mathcal{Q}^q)$; taking the cohomology in $q$ first uses that a section of $H^q(\mathcal{Q}^\bullet)$ over a member of the cover computes $H^q(U_i,\mathcal{F})$, giving $E_2^{p,q} = \check H^p(\mathcal{U},\underline{H}^q(\mathcal{F}))$, and the other filtration converges to the cohomology of the total complex, which is $H^*(X,\mathcal{F})$ because the rows are resolutions and the Čech complex of an injective resolution computes the derived functors. $\square$

**Theorem (Leray's theorem).** Let $\mathcal{U}$ be an open cover of $X$ such that $\underline{H}^q(\mathcal{F})(U_{i_0\ldots i_p}) = H^q(U_{i_0\ldots i_p},\mathcal{F}) = 0$ for every nonempty finite intersection and every $q > 0$, that is, every nonempty finite intersection is **acyclic** for $\mathcal{F}$. Then the natural map

$$
\check H^p(\mathcal{U},\mathcal{F}) \to H^p(X,\mathcal{F})
$$

is an isomorphism for every $p \geq 0$.

*Proof.* Under the hypothesis the presheaf $\underline{H}^q(\mathcal{F})$ vanishes on each finite intersection of members of $\mathcal{U}$ for $q > 0$; hence every term of the Čech complex $\check C^p(\mathcal{U},\underline{H}^q(\mathcal{F}))$ is a product of zero groups, so $E_2^{p,q} = 0$ for $q > 0$ and the spectral sequence has $E_2^{p,0} = \check H^p(\mathcal{U},\mathcal{F})$ concentrated on the bottom row; the spectral sequence therefore degenerates, and its $E_\infty$ terms are already the $E_2$ terms, giving $\check H^p(\mathcal{U},\mathcal{F}) \cong H^p(X,\mathcal{F})$. $\square$

**Corollary (good covers).** A cover $\mathcal{U}$ by open sets with all nonempty finite intersections contractible is called a **good cover**. For a locally contractible space, a good cover with respect to the constant sheaf $\underline{A}$ satisfies $\check H^p(\mathcal{U},\underline{A}) \cong H^p(X;A)$. Good covers exist for manifolds — refine any cover by geodesically convex open sets of a complete Riemannian metric, so that all intersections are convex, hence contractible — and for simplicial complexes, the open stars of the vertices forming a good cover.

**Example (a good cover of the sphere).** The sphere $S^2$ has a good cover by four open discs centred at the vertices of a regular tetrahedron: the pairwise intersections are discs around the midpoints of the edges, the triple intersections are discs around the centres of the faces, and the fourfold intersection is empty. The Čech complex of this cover for the constant sheaf $\underline{\mathbb{Z}}$ is the simplicial cochain complex of the boundary of the tetrahedron, which is a triangulation of $S^2$; hence $\check H^0 = \check H^2 = \mathbb{Z}$ and $\check H^1 = 0$, in agreement with the cohomology of the sphere and with the cellular computation of *CW Complexes and Cellular Approximation*. **No good cover of $S^2$ by three contractible sets exists.** If the triple intersection were nonempty, the nerve would be a $2$-simplex and the nerve theorem would give $S^2\simeq *$; if it were empty, the nerve would be a graph and the nerve theorem would give $S^2\simeq$ a graph. Both conclusions are false, so the three-set cover is impossible; the Čech complex of a cover of $S^2$ by contractible sets with contractible intersections must therefore have a term in degree two.

## The Nerve of a Cover

**Definition.** The **nerve** of the cover $\mathcal{U} = \{U_i\}_{i\in I}$ is the simplicial complex $N(\mathcal{U})$ with vertex set $I$, in which a finite subset $\{i_0,\ldots,i_p\}$ spans a $p$-simplex if and only if the intersection $U_{i_0\ldots i_p}$ is nonempty. Its geometric realisation is written $|N(\mathcal{U})|$.

**Theorem (the nerve theorem).** Let $X$ be a paracompact space and $\mathcal{U}$ an open cover such that every nonempty finite intersection $U_{i_0\ldots i_p}$ is contractible. Then the geometric realisation of the nerve is homotopy equivalent to $X$:

$$
|N(\mathcal{U})| \simeq X.
$$

*Proof sketch.* The homotopy equivalence is realised by a map sending the vertex $i$ to a point of $U_i$ and extending over the simplices using the contractibility of the intersections; the inverse is a partition-of-unity map, which exists because the cover may be taken locally finite on a paracompact space, sending $x$ to the barycentric coordinates of the set of members of the cover containing $x$. The two composites are homotopic to the identity by a straight-line homotopy in the simplex of the nerve, the partitions of unity providing the continuity. $\square$

**Corollary (Čech cohomology is the cohomology of the nerve).** For a cover $\mathcal{U}$ with all nonempty finite intersections acyclic for the constant sheaf $\underline{A}$, the Čech complex of $\mathcal{U}$ with coefficients in $\underline{A}$ is the simplicial cochain complex of the nerve with coefficients in $A$:

$$
\check H^p(\mathcal{U},\underline{A}) \cong H^p(N(\mathcal{U});A),
$$

the simplicial cohomology of *Simplicial and Singular Homology*. If in addition the intersections are contractible, then $\check H^p(\mathcal{U},\underline{A}) \cong H^p(X;A)$ by the nerve theorem and the Leray theorem.

*Proof.* The alternation convention of the Čech complex makes $\check C^p(\mathcal{U},\underline{A})$ the group of functions on the $p$-simplices of the nerve with values in $A$, and the Čech differential is the simplicial coboundary; the identification of the two complexes is then tautological. $\square$

**Example (the circle, the torus and the classifying space).** The circle $S^1$ has a good cover by three arcs $U_0, U_1, U_2$ such that each pairwise intersection is an arc (nonempty and contractible) and the triple intersection is empty; the nerve is the boundary of a triangle, a circle, and $\check H^\bullet(\mathcal{U},\underline{\mathbb{Z}}) = (\mathbb{Z},\mathbb{Z},0) = H^\bullet(S^1;\mathbb{Z})$, in agreement with the two-set computation above. The good cover of the torus $T^2 = S^1\times S^1$ obtained by taking the product of the three-arc covers of the two factors has nine members, and its nerve is the product of the two triangle nerves, a triangulation of $T^2$; hence $\check H^\bullet = (\mathbb{Z},\mathbb{Z}^2,\mathbb{Z})$. The nerve of a good cover of $\mathbb{RP}^2$ may be taken to be the six-vertex triangulation of the projective plane, whose cohomology with $\mathbb{F}_2$ coefficients is $(\mathbb{F}_2,\mathbb{F}_2,\mathbb{F}_2)$. The construction is the prototype of the **classifying space** $BG$, whose general theory is that of *Classifying Spaces and Cohomology Operations*, above this article: for a discrete group $G$ acting freely and properly discontinuously on a contractible space $EG$, the quotient $BG$ has a good cover whose nerve is a model for the simplicial set $EG/G$, and $\check H^*(BG;A)$ is the group cohomology $H^*(G;A)$ of $G$ with coefficients in the trivial module $A$.

## Applications

### The Exponential Sequence and the Picard Group

**Theorem.** Let $(X,\mathcal{O}_X)$ be a ringed space with sheaf of units $\mathcal{O}_X^*$, and let $\underline{\mathbb{Z}}$ be the constant sheaf, so that the exponential sequence

$$
0 \to \underline{\mathbb{Z}} \to \mathcal{O}_X \xrightarrow{\ \exp\ } \mathcal{O}_X^* \to 0
$$

is exact when the exponential is locally surjective. Then the degree-one comparison of Čech and sheaf cohomology gives an isomorphism

$$
\operatorname{Pic}(X) := \check H^1(X,\mathcal{O}_X^*) \cong H^1(X,\mathcal{O}_X^*),
$$

the **Picard group** of isomorphism classes of invertible sheaves on $X$, and

$$
0 \to H^1(X,\underline{\mathbb{Z}}) \to H^1(X,\mathcal{O}_X) \to \operatorname{Pic}(X) \to H^2(X,\underline{\mathbb{Z}}) \to H^2(X,\mathcal{O}_X)
$$

is exact. In particular, for a complex manifold the exponential sequence computes the first Chern class $c_1 : \operatorname{Pic}(X)\to H^2(X;\mathbb{Z})$ of *Fibre Bundles, Connections and Curvature*, and for $\mathbb{C}^*$ the exactness of the sequence of global sections fails at the middle as in *Presheaves and Sheaves*, the failure being measured by $H^1(\mathbb{C}^*,\underline{\mathbb{Z}}) = \mathbb{Z}$.

*Proof.* An invertible sheaf is a locally free $\mathcal{O}_X$-module of rank one, and it is determined by its transition functions on a cover, which are a Čech $1$-cocycle with values in $\mathcal{O}_X^*$; the sheaf is trivial exactly when the cocycle is a coboundary, so the classes of invertible sheaves are exactly the elements of $\check H^1(X,\mathcal{O}_X^*)$, and the comparison with $H^1$ in degree one is the theorem above. The long exact sequence is that of the exponential sequence in Čech cohomology, with the identification of the Čech and sheaf groups supplied by the theorem. $\square$

### Torsors and the Classification of Cocycles

**Theorem (classification of torsors).** Let $A$ be a sheaf of abelian groups on $X$. The classes in $\check H^1(X,A)$ are in natural bijection with the isomorphism classes of **$A$-torsors** on $X$, that is, of sheaves $\mathcal{L}$ of sets on $X$ with a free and transitive action of $A$, and the class $0$ corresponds to the trivial torsor $A$ itself.

*Proof.* A torsor is trivialised by a cover $\{U_i\}$: choose local sections $s_i \in \mathcal{L}(U_i)$, and let $a_{ij}$ be the unique element of $A(U_{ij})$ with $a_{ij}\cdot s_j = s_i$ on the overlap; the transition elements satisfy the cocycle condition $a_{ij}a_{jk} = a_{ik}$ and define a class in $\check H^1(\mathcal{U},A)$. Changing the local sections changes the cocycle by a coboundary, and refining the cover does not change the class in the limit; conversely a cocycle with values in $A$ defines a torsor by gluing the local pieces $A|_{U_i}$ along the translations determined by the cocycle. $\square$

**Example.** For a covering space $p : \tilde X\to X$ with group of deck transformations $A$, the sheaf of local sections of $p$ is an $A$-torsor; when $p$ is the universal cover of a connected space with fundamental group $G$, the class of the torsor in $\check H^1(X,\underline{G})$ corresponds to the class of the covering in $\operatorname{Hom}(\pi_1(X),G)$ modulo conjugation, which is the classification of *The Fundamental Group and Covering Spaces* read through Čech cohomology. For $A = \mathcal{O}_X^*$ the torsors are the invertible sheaves, recovering the Picard group; for $A = \underline{\mathbb{Z}}$ on $\mathbb{C}^*$, the torsor of the multi-valued logarithm is the nonzero class of $H^1(\mathbb{C}^*,\underline{\mathbb{Z}})$.

### The Čech–de Rham Double Complex

**Definition.** Let $M$ be a smooth manifold and let $\Omega^\bullet$ be the de Rham complex of sheaves, a resolution of the constant sheaf $\underline{\mathbb{R}}$. For an open cover $\mathcal{U}$ of $M$ with all finite intersections contractible, the **Čech–de Rham double complex** is

$$
K^{p,q} = \check C^p(\mathcal{U},\Omega^q),
$$

with the Čech differential $\delta$ in the horizontal direction and the exterior derivative $d$ in the vertical direction; the two commute, $\delta d = d\delta$, so that $K^{\bullet,\bullet}$ is a double complex, and the two spectral sequences of the filtration by total degree both converge to the hypercohomology of $\Omega^\bullet$: the first has $E_2^{p,q} = \check H^p(\mathcal{U},\mathcal{H}^q(\Omega^\bullet))$ with $\mathcal{H}^0(\Omega^\bullet) = \underline{\mathbb{R}}$ and $\mathcal{H}^q = 0$ for $q>0$ by the Poincaré lemma, and the second has $E_1^{p,q} = \Omega^q(U_{(p)})$ computing $H^q_{dR}(M)$. The comparison of the two degenerations is the **de Rham theorem**,

$$
H^p_{dR}(M) \cong H^p(M;\mathbb{R}),
$$

and the construction is the model for the comparison theorems of the subject. The section is recorded here because it is the Čech complex, not the de Rham complex, that provides the second index; the differential forms themselves are those of the written *Differential Forms and Stokes' Theorem*, and are not redefined here.

## Summary

The Čech complex of an open cover $\mathcal{U}$ of a space $X$ with coefficients in a sheaf $\mathcal{F}$ has as its $p$-th term the product of the groups of sections of $\mathcal{F}$ over the $(p+1)$-fold intersections of the members of $\mathcal{U}$, with the alternating-sum differential; it is a complex, its degree-zero cohomology is the group of global sections when $\mathcal{F}$ is a sheaf, and its degree-one cohomology is the quotient of the gluing data on the cover by the trivial ones. Refinements of covers induce morphisms of complexes, well defined on cohomology, and the direct limit over all covers gives an invariant $\check H^p(X,\mathcal{F})$ which coincides with the sheaf cohomology in degree zero, is injected into it in degree one, and coincides with it in all degrees when $X$ is paracompact; it may be computed from covers by members of any basis closed under finite intersections, and it is a cohomological functor, so a short exact sequence of sheaves gives a long exact sequence of Čech groups.

The Čech-to-derived spectral sequence $E_2^{p,q} = \check H^p(\mathcal{U},\underline{H}^q(\mathcal{F})) \Rightarrow H^{p+q}(X,\mathcal{F})$, in which the coefficients in the Čech direction are the presheaves of cohomology of the members of the cover, is the precise comparison between the two theories; it degenerates when every nonempty finite intersection of members of the cover is acyclic for $\mathcal{F}$, and this degeneration is **Leray's theorem**, $\check H^p(\mathcal{U},\mathcal{F}) \cong H^p(X,\mathcal{F})$. For the constant sheaf the Čech complex of such a cover is the simplicial cochain complex of the nerve, so that the cohomology of the space may be read off from the combinatorics of the cover; the nerve theorem identifies the realisation of the nerve with the space when all intersections are contractible. The applications are the identification of the Picard group of a ringed space with $\check H^1(X,\mathcal{O}_X^*)$ and the computation of the exact sequence of the exponential; the classification of torsors by $\check H^1$; and the Čech–de Rham double complex, whose two degenerations give the de Rham theorem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{U} = \{U_i\}_{i\in I}$ | open cover of $X$; $U_{i_0\ldots i_p}$ its $(p+1)$-fold intersection |
| $\check C^p(\mathcal{U},\mathcal{F}) = \prod_{i_0<\cdots<i_p}\mathcal{F}(U_{i_0\ldots i_p})$ | Čech cochains of degree $p$, alternating convention |
| $\delta$ | Čech differential, alternating sum with restrictions |
| $\check H^p(\mathcal{U},\mathcal{F})$ | cohomology of the Čech complex of the cover |
| $\check H^p(X,\mathcal{F}) = \varinjlim_{\mathcal{U}}\check H^p(\mathcal{U},\mathcal{F})$ | Čech cohomology, over all covers by refinement |
| $\mathfrak{V} \preceq \mathcal{U}$ | refinement; a refinement map on cochain complexes |
| $\underline{H}^q(\mathcal{F}) : U\mapsto H^q(U,\mathcal{F})$ | presheaf of cohomology, coefficients of the Čech-to-derived sequence |
| $E_2^{p,q} = \check H^p(\mathcal{U},\underline{H}^q(\mathcal{F}))$ | Čech-to-derived spectral sequence, converging to $H^{p+q}(X,\mathcal{F})$ |
| good cover | all nonempty finite intersections contractible; Leray applies |
| $N(\mathcal{U})$, $|N(\mathcal{U})|$ | nerve of the cover and its realisation; $|N(\mathcal{U})|\simeq X$ |
| $\operatorname{Pic}(X) = \check H^1(X,\mathcal{O}_X^*)$ | Picard group of invertible sheaves; $c_1$ to $H^2(X;\mathbb{Z})$ |
| $K^{p,q} = \check C^p(\mathcal{U},\Omega^q)$ | Čech–de Rham double complex; $\delta d = d\delta$ |





## Further Reading

- Jean Leray, *Sur la forme des espaces topologiques et sur les points fixes des représentations* (Journal de Mathématiques Pures et Appliquées 24, 1945), for the original Čech construction and the theorem on acyclic covers.
- Roger Godement, *Topologie algébrique et théorie des faisceaux* (Hermann, 1958), for the comparison of Čech and derived cohomology and the paracompact case.
- Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology* (Springer, 1982), for good covers, the Čech–de Rham complex and the computation of the cohomology of spheres and projective spaces.
- Glen E. Bredon, *Sheaf Theory* (Springer, second edition, 1997), for the nerve theorem and the comparison of the two cohomology theories.
- Robin Hartshorne, *Algebraic Geometry* (Springer, 1977), for the Čech computation of the cohomology of coherent sheaves on projective space and for the Picard group.
- Alexander Grothendieck and Jean Dieudonné, *Éléments de géométrie algébrique III* (Publications Mathématiques de l'IHÉS 11, 1961), for the Čech-to-derived spectral sequence in its general form.
