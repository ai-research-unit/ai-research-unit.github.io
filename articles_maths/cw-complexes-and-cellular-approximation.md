
# __CW Complexes and Cellular Approximation__

## Introduction

A CW complex is a topological space assembled from discs, one dimension at a time: one starts with a discrete set of points, glues on copies of the interval, then copies of the disc, and so on, taking the union with the topology in which a set is open exactly when its intersection with every closed disc is closed. The definition is combinatorial — it is a recipe in terms of attaching maps — and the resulting spaces carry two structures at once. They are general enough to include every space a geometer meets in this corpus, namely the spheres, the projective spaces, the Grassmannians, the classical groups, the surfaces and the simplicial complexes; and they are rigid enough that their algebraic invariants can be computed from the combinatorial data alone.

The companion article *The Fundamental Group and Covering Spaces* supplies homotopy, the fundamental group and the covering theory. The present article adds the assembling procedure, the **homotopy extension property** that makes the gluing homotopically well behaved, the **cellular approximation theorem** that lets a map be deformed until it respects the cell structure, and the **cellular chain complex** that computes the homology of a CW complex from its cells. The homology theory itself, simplicial and singular, is not covered here; it is used here only in the form of the standard facts that $H_n(S^n) \cong \mathbb{Z}$ and that a map of spheres has an integral degree, both of which are standard mathematics quoted with a citation and are developed in their own place there.

Throughout, $D^n = \{x \in \mathbb{R}^n : |x| \leq 1\}$ is the closed unit disc, $S^{n-1} = \partial D^n$ its boundary, and $D^n \setminus S^{n-1}$ its interior, written $\mathring D^n$. A map means a continuous map. No measure, integral or derivative is used; the theory is combinatorial and topological, and where a smooth statement would be natural it is deferred.

## CW Complexes

### The Construction

**Definition.** A **CW complex** is a pair $(X, \mathcal{E})$ where $X$ is a topological space and $\mathcal{E} = \coprod_{n \geq 0} \mathcal{E}_n$ is a family of maps, the **attaching maps**,

$$
\varphi_\alpha : D^n \longrightarrow X, \qquad \alpha \in \mathcal{E}_n,
$$

such that, writing $e^n_\alpha = \varphi_\alpha(\mathring D^n)$ for the associated **open $n$-cell**:

1. the restriction $\varphi_\alpha|_{\mathring D^n}$ is a homeomorphism onto $e^n_\alpha$, and $X$ is the disjoint union of the cells $e^n_\alpha$;
2. the **closure finiteness** condition: for each $n$ and $\alpha$ the closure $\overline{e^n_\alpha}$ meets only finitely many cells;
3. the **weak topology** condition: a subset $A \subseteq X$ is closed if and only if $A \cap \overline{e^n_\alpha}$ is closed for every cell, equivalently $\varphi_\alpha^{-1}(A)$ is closed in $D^n$ for every attaching map.

The **$n$-skeleton** is $X^n = \bigcup_{k \leq n} \bigcup_{\alpha \in \mathcal{E}_k} e^k_\alpha$, a closed subspace; the space is **finite-dimensional** of dimension $n$ if $\mathcal{E}_k = \varnothing$ for $k > n$ and $\mathcal{E}_n \neq \varnothing$, and **finite** if $\mathcal{E}$ is finite. The **dimension** of $X$ is the supremum of the dimensions of its cells.

Condition (3) is the substantive one. It says that the topology of $X$ is determined by the closed discs and their attaching maps, and it is the reason a function out of $X$ is continuous exactly when its restrictions to the closed cells are. Conditions (1) and (2) say that the cell decomposition is discrete in the sense that each cell's closure meets only finitely many cells; they do not bound the total number of cells, which may be uncountable, and a CW complex with countably many cells may be enumerated cell by cell in order of dimension.

**Proposition (the pushout square).** The square

$$
\coprod_{\alpha \in \mathcal{E}_n} S^{n-1} \longrightarrow X^{n-1}, \qquad \coprod_{\alpha \in \mathcal{E}_n} D^n \longrightarrow X^n,
$$

in which the left vertical map is the inclusion of the boundary and the upper horizontal map is the restriction of the attaching maps, is a pushout in the category of topological spaces: $X^n$ is the quotient of the disjoint union $X^{n-1} \sqcup \coprod_\alpha D^n$ by the identification $x \sim \varphi_\alpha(x)$ for $x \in S^{n-1}$, and the topology is the quotient topology.

*Proof.* The quotient description is a restatement of the construction; the quotient topology is the weak topology because a set is closed in the quotient exactly when its preimage in each $D^n$ and in $X^{n-1}$ is closed. $\square$

**Definition.** A CW complex is a **subcomplex** of $(X,\mathcal{E})$ if it is a union of cells whose closures are contained in it; a subcomplex is a closed subspace and is itself a CW complex with the induced cells. The **$k$-skeleton** $X^k$ is the basic example.

**Definition.** A **CW pair** is a pair $(X, A)$ with $A$ a subcomplex of the CW complex $X$; the **quotient** $X/A$ is then a CW complex whose cells are the cells of $X$ not in $A$, together with one new basepoint cell.

### Examples

**Example (spheres).** $S^n$ has a CW structure with one $0$-cell $e^0 = \{N\}$ and one $n$-cell, attached by the constant map $S^{n-1} \to \{N\}$; the $S^{n-1}$ maps to the point, so the $n$-disc closes up into the sphere. Equivalently $S^n$ is the one-point compactification of $\mathbb{R}^n$, and the complement of the point is the open cell.

**Example (projective spaces).** $\mathbb{RP}^n$ has one cell in each dimension $0, 1, \ldots, n$, the cell $e^k$ being the set of lines whose last nonzero coordinate is in position $k+1$; the attaching map of $e^k$ is the quotient $S^{k-1} \to \mathbb{RP}^{k-1}$, of degree $0$ for odd $k$ and degree $2$ for even $k$ in the sense of the cellular boundary formula below. Similarly $\mathbb{CP}^n$ has one cell in each even dimension $0, 2, \ldots, 2n$, and $\mathbb{HP}^n$ one cell in each dimension divisible by $4$, up to $4n$.

**Example (Grassmannians).** The Grassmannian $G_k(\mathbb{R}^n)$ of $k$-planes in $\mathbb{R}^n$ carries the **Schubert cell decomposition**: for a fixed complete flag $0 = V_0 \subset V_1 \subset \cdots \subset V_n = \mathbb{R}^n$, the cells are the sets of $k$-planes with prescribed intersection dimensions $\dim(W \cap V_i)$, indexed by partitions $\lambda$ with at most $k$ parts each at most $n-k$. This is the cell structure behind **Schubert calculus** and the article *Grassmannians and Stiefel Manifolds*; it is recorded here as the source of the CW structures on the classical groups.

**Example (surfaces).** Every closed surface has a CW structure: the torus has one $0$-cell, two $1$-cells and one $2$-cell, the $2$-cell attached along the commutator $aba^{-1}b^{-1}$; the real projective plane has one cell in each dimension, the $2$-cell attached along $a^2$.

**Example (graphs).** A connected graph is a CW complex of dimension $1$; a finite connected graph with $V$ vertices and $E$ edges has $\pi_1$ free of rank $E - V + 1$, by van Kampen applied to the wedge decomposition.

## Homotopy-Theoretic Properties

### The Homotopy Extension Property

**Definition.** A pair $(X,A)$ has the **homotopy extension property (HEP)** if, for every space $Y$, every homotopy $H : A \times I \to Y$ and every map $f : X \to Y$ with $f|_A = H(\cdot, 0)$, there exists a homotopy $\tilde H : X \times I \to Y$ with $\tilde H|_{A \times I} = H$ and $\tilde H(\cdot, 0) = f$. Equivalently, every pair of maps $X \times \{0\} \cup A \times I \to Y$ extends to $X \times I$.

**Theorem.** A CW pair $(X,A)$ has the homotopy extension property.

*Proof sketch.* It suffices to construct a retraction of $X \times I$ onto $X \times \{0\} \cup A \times I$; the extension is then obtained by composition. For a single cell, $D^n \times I$ retracts onto $D^n \times \{0\} \cup S^{n-1} \times I$ by radial projection from a point outside, and the retractions for the cells assemble, using the weak topology, into a retraction for the pair. $\square$

**Definition.** A pair with the HEP is a **cofibration**; a map $A \hookrightarrow X$ is a cofibration exactly when it has the HEP. Cofibrations are, up to homotopy, the inclusions one may quotient by and attach along without changing the homotopy type.

**Corollary.** If $(X,A)$ has the HEP then the quotient map $X \to X/A$ induces an isomorphism on homology and cohomology of the pair in the sense of the excision statement recorded: the pair $(X,A)$ and the pair $(X/A, \ast)$ have isomorphic relative invariants. Consequently $H_n(X,A) \cong \tilde H_n(X/A)$.

*Proof.* By the HEP the inclusion $A \subseteq X$ is a cofibration and the collapse $X \to X/A$ is a homotopy equivalence of pairs. $\square$

### Cellular Approximation

**Definition.** A map $f : X \to Y$ of CW complexes is **cellular** if $f(X^n) \subseteq Y^n$ for every $n$: it sends the $n$-skeleton into the $n$-skeleton.

**Theorem (cellular approximation).** Every map $f : X \to Y$ of CW complexes is homotopic to a cellular map; if $f$ is already cellular on a subcomplex $A \subseteq X$, the homotopy may be taken relative to $A$.

*Proof sketch.* Induct on the skeleta. Suppose $f(X^{n-1}) \subseteq Y^{n-1}$ after a homotopy relative to $A$; the obstruction to pushing $f(X^n)$ into $Y^n$ lies in the cells of $Y$ of dimension $> n$. For a single $n$-cell, the image $f(D^n)$ meets the interior of a $Y$-cell of dimension $k > n$, and by a general position argument in the interior of a disc of dimension $k$ the image can be pushed off the interior by a homotopy relative to the boundary, because a map $D^n \to D^k$ with $k > n$ is homotopic rel boundary to a map into the boundary $S^{k-1}$ — the complement of the image of a disc in a higher-dimensional disc is path-connected and the tube around the image can be pushed out. Since cells are attached by the weak topology, the local homotopies assemble. $\square$

**Corollary (connectivity of skeleta).** If a connected CW complex $X$ has no cells of dimension $1, \ldots, n$, then $X^n$ is a single point and the pair $(X, X^n)$ has $\pi_k(X, X^n) = 0$ for $k \leq n$; more generally the pair $(X^n, X^{n-1})$ has vanishing homotopy groups in degrees below $n$ and $\pi_n$ free on the $n$-cells.

**Corollary (low-dimensional homotopy of spheres).** Cellular approximation applied to maps $S^k \to S^n$ shows that every such map is null-homotopic when $k < n$. Equivalently, $\pi_k(S^n) = 0$ for $k < n$, and the inclusion $S^n \hookrightarrow S^{n+1}$ induces an isomorphism $\pi_k(S^n) \to \pi_k(S^{n+1})$ for $k \leq n - 1$, both groups being trivial there. This is a first instance of a stability phenomenon, whose sharp form is the **Freudenthal suspension theorem** , written in this batch: the suspension $\sigma: \pi_k(S^n) \to \pi_{k+1}(S^{n+1})$ is an isomorphism for $k < 2n-1$ and a surjection for $k = 2n-1$, which extends the isomorphism far beyond the trivial range obtained here.

**Remark.** Cellular approximation is the reason a CW complex is a homotopically economical model: its homotopy type is determined by the attaching data of its cells up to homotopy, and maps may always be assumed to respect that data. The same argument, in the smooth category, produces the statement that a map of manifolds is homotopic to a smooth one; the smooth version needs the approximation theory of Part III and is deferred there.

## Cellular Homology

### The Cellular Chain Complex

Let $X$ be a CW complex. The cellular chain group in degree $n$ is the free abelian group on the $n$-cells,

$$
C_n^{\mathrm{CW}}(X) = \mathbb{Z}\bigl[\mathcal{E}_n\bigr] = \bigoplus_{\alpha \in \mathcal{E}_n} \mathbb{Z}\, e^n_\alpha,
$$

zero when there are no $n$-cells. The boundary is defined from the attaching maps.

**Definition (degree).** Let $f: S^n \to S^n$ be a map. The induced homomorphism $f_*: H_n(S^n) \to H_n(S^n)$ on the top homology is multiplication by an integer, written $\deg f$, because $H_n(S^n) \cong \mathbb{Z}$; the integer is the **degree** of $f$. It depends only on the homotopy class of $f$, and $\deg(f \circ g) = \deg f \cdot \deg g$, $\deg \mathrm{id} = 1$. This is standard mathematics, quoted here; the systematic treatment of the degree, including its integral representation and the Lefschetz and Brouwer theorems, is the subject , written in this batch.

**Definition (cellular boundary).** For an $n$-cell $e^n_\alpha$ let $q_\beta : X^{n-1} \to X^{n-1}/(X^{n-2} \cup \text{other } (n-1)\text{-cells}) \cong S^{n-1}$ be the collapse onto the closed $(n-1)$-cell $e^{n-1}_\beta$, a sphere because the cell is a disc modulo its boundary. The **cellular boundary** of $e^n_\alpha$ is

$$
\partial_n(e^n_\alpha) = \sum_{\beta \in \mathcal{E}_{n-1}} \deg\bigl(q_\beta \circ \varphi_\alpha|_{S^{n-1}}\bigr)\, e^{n-1}_\beta,
$$

the sum being finite by closure finiteness. For $n = 0$ the boundary is zero, and for $n = 1$ the sum counts signed endpoints, the degree of a map $S^0 \to S^0$ being $+1$ or $-1$ according as the map preserves or interchanges the two points.

**Theorem.** $\partial_{n-1} \circ \partial_n = 0$, so $(C_*^{\mathrm{CW}}(X), \partial_*)$ is a chain complex; and its homology is the singular homology,

$$
H_n^{\mathrm{CW}}(X) = \ker \partial_n / \operatorname{im} \partial_{n+1} \cong H_n(X).
$$

*Proof sketch.* The composite vanishes because it computes the degree of a map $S^{n-1} \to S^{n-1}$ factoring through the contractible space $D^{n-1}$ after accounting for the two collapses, and a map factoring through a contractible space has degree $0$ when $n-1 \geq 1$. The identification with singular homology is by comparing both with the homology of the pair $(X^n, X^{n-1})$; the boundary above is by construction the connecting map of that pair, and the comparison uses the five lemma on the diagram of skeleta. $\square$

### The Boundary Formula

**Theorem (cellular boundary formula).** For an $n$-cell $e^n_\alpha$ with attaching map $\varphi_\alpha$ and an $(n-1)$-cell $e^{n-1}_\beta$, the coefficient of $e^{n-1}_\beta$ in $\partial_n e^n_\alpha$ is the degree of the composite

$$
S^{n-1} \xrightarrow{\ \varphi_\alpha|_{S^{n-1}}\ } X^{n-1} \xrightarrow{\ q_\beta\ } S^{n-1},
$$

where $q_\beta$ collapses $X^{n-1} \setminus e^{n-1}_\beta$ to a point.

This is the single formula that makes the homology of every CW complex in the corpus computable. It is stated here in the generality in which it is used; its proof is the proof of the preceding theorem.

**Corollary.** If $X$ has no two cells of consecutive dimensions, all cellular boundaries vanish and $H_n(X) \cong C_n^{\mathrm{CW}}(X)$ is free on the $n$-cells. This applies to the spheres, the complex projective spaces and the quaternionic projective spaces.

**Example (real projective space).** For $\mathbb{RP}^n$ with one cell in each dimension, the degree of the attaching map of $e^k$ is $1 + (-1)^k$: it is the degree of the quotient $S^{k-1} \to \mathbb{RP}^{k-1}$ composed with the collapse of the unique $(k-1)$-cell, and the antipodal identification contributes $(-1)^k$. Hence $C_k^{\mathrm{CW}} \cong \mathbb{Z}$ for $0 \leq k \leq n$ and the boundary $\partial_k$ is multiplication by $1+(-1)^k$, that is, $0$ for odd $k$ and $2$ for even $k$. The homology is therefore

$$
H_k(\mathbb{RP}^n) \cong \begin{cases} \mathbb{Z}, & k = 0 \text{ or } k = n \text{ with } n \text{ odd},\\ \mathbb{Z}/2\mathbb{Z}, & k \text{ odd}, \ 0 < k < n,\\ 0, & \text{otherwise}.\end{cases}
$$

**Example (complex projective space).** For $\mathbb{CP}^n$ with one cell in each even dimension, all boundaries vanish, so $H_{2k}(\mathbb{CP}^n) \cong \mathbb{Z}$ for $0 \leq k \leq n$ and the odd-dimensional homology vanishes.

### The Euler Characteristic

**Definition.** A CW complex $X$ is **of finite type** if it has finitely many cells in each dimension. For such an $X$ the **Euler characteristic** is

$$
\chi(X) = \sum_{n \geq 0} (-1)^n \#\mathcal{E}_n,
$$

the alternating sum of the numbers of cells.

**Theorem.** If $X$ has finite type and finitely many nonzero homology groups of finite rank, then

$$
\chi(X) = \sum_{n \geq 0} (-1)^n \operatorname{rk} H_n(X),
$$

and the number is independent of the CW structure.

*Proof.* The alternating sum of the ranks of the terms of a finite chain complex of free abelian groups equals the alternating sum of the ranks of its homology, by the rank–nullity theorem applied to each $\partial_n$. Independence of the structure follows because the right-hand side depends only on $X$. $\square$

**Example.** For the torus the cell count gives $\chi = 1 - 2 + 1 = 0$; from homology, $\operatorname{rk}H_0 - \operatorname{rk}H_1 + \operatorname{rk}H_2 = 1 - 2 + 1 = 0$. For the sphere $S^n$, $\chi = 1 + (-1)^n$. For $\mathbb{RP}^2$, $\chi = 1 - 1 + 1 = 1$, matching $1 - 0 + 0$ from the ranks of $H_*(\mathbb{RP}^2) = (\mathbb{Z}, \mathbb{Z}/2, 0)$: a $\mathbb{Z}/2$ contributes rank $0$.

**Remark.** The Euler characteristic of a finite CW complex may be computed without knowing the homology, and this is how it is used in practice; the identity with the alternating sum of Betti numbers is a theorem, and it is the reason the two definitions agree.

## Operations on CW Complexes

**Proposition (quotients and products).** Let $X$ be a CW complex.

1. If $A\subseteq X$ is a subcomplex, then $X/A$ is a CW complex whose cells are the cells of $X$ not in $A$ together with the collapsed image of $A$ as a single $0$-cell, and the quotient map $X\to X/A$ is cellular.
2. The product $X\times Y$ of two CW complexes, topologised by the **weak topology** on the product's cells — the topology whose closed subsets are those meeting each closed cell in a closed set, in general finer than the product topology — is a CW complex whose $n$-cells are the products of a $p$-cell with a $q$-cell, $p+q = n$. The two topologies agree when $X$ or $Y$ is locally compact, and the identity map between them is a homotopy equivalence in general.
3. The smash product $X\wedge Y = (X\times Y)/(X\vee Y)$, the mapping cylinder of a cellular map, the mapping cone and the reduced suspension $\Sigma X = S^1\wedge X$ are CW complexes, and the reduced suspension is the based suspension restricted to complexes.
4. If $p : Y\to X$ is a covering map of a path-connected CW complex, then $Y$ carries a CW structure whose cells are the cells of $X$ lifted along the covering, and the cellular chain complex of $Y$ is the chain complex of $X$ tensored with the free module on the fibre, with the local system of *The Fundamental Group and Covering Spaces* twisting the differentials; in particular $Y$ has the same dimension as $X$.

*Proof.* (1) The characteristic maps of the cells not in $A$ compose with the quotient, and the boundary of the collapsed image inherits a cell structure from the filtration. (2) The weak topology on the product is the standard one making the product of CW complexes a CW complex; that it agrees with the product topology when one factor is locally compact is the usual theorem, and the difference in general is repaired by the homotopy equivalence of the two topologies. (3) Each construction is given its cells by the description of the maps involved, and the reduced suspension is the case $Y = S^1$. (4) The cells of $X$ lift to cells of $Y$ after a subdivision or a cellular approximation of the attaching maps, and the identification of the chain complexes is the standard computation of the cellular chains of a covering space. $\square$

**Example.** The quotient $D^n/S^{n-1}\cong S^n$ exhibits the sphere as the quotient of a disc by a subcomplex whose image is one point; the product $S^p\times S^q$ has four cells by (2), which gives the homology of a product directly in the cellular picture; and the universal cover of a graph is the tree whose $0$-cells are the vertices of a chosen lifting, which is the cellular form of the correspondence between free groups and trees used in *The Fundamental Group and Covering Spaces*.

## Summary

A CW complex is a space built from discs by attaching maps, with the closure finiteness and weak topology conditions; its $n$-skeleton is obtained from the previous one by a pushout along the boundaries of the $n$-discs, and every sphere, projective space, Grassmannian, surface and simplicial complex carries such a structure. The weak topology makes continuity checkable cell by cell, and closure finiteness makes each cell meet only finitely many others.

CW pairs have the homotopy extension property, equivalently the inclusion of a subcomplex is a cofibration; consequently collapsing a subcomplex is a homotopy equivalence of pairs and computes relative invariants. Cellular approximation says every map of CW complexes is homotopic to a cellular one, relative to a subcomplex on which it is already cellular, so maps may be assumed to respect skeleta and the low-dimensional homotopy of a CW complex is read from its cells.

The cellular chain complex is free on the cells in each degree, with boundary given by the degrees of the composites of the attaching maps with the collapses onto the cells of one dimension less; its homology is the singular homology, and when no two cells have consecutive dimensions the boundaries vanish and the homology is free on the cells. The Euler characteristic is the alternating sum of the numbers of cells, equal to the alternating sum of the ranks of the homology groups, and independent of the cell structure. Quotients by subcomplexes, products with the weak topology, smash products, mapping cylinders and covering spaces of CW complexes are again CW complexes, and the cellular chain complex of a covering space is the chain complex of the base with coefficients in the local system of the covering.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $D^n$, $S^{n-1} = \partial D^n$, $\mathring D^n$ | Closed disc, its boundary sphere, its interior |
| $\varphi_\alpha : D^n \to X$ | Attaching map of a cell |
| $e^n_\alpha = \varphi_\alpha(\mathring D^n)$ | Open $n$-cell |
| $X^n$ | $n$-skeleton; $\bigcup_{k \leq n} X^k$ |
| $X/A$ | Quotient by a subcomplex; collapsible when $(X,A)$ has the HEP |
| $(X,A)$ has the HEP | Homotopy extension property; equivalently the inclusion is a cofibration |
| $\deg f$, $f : S^n \to S^n$ | Degree; the integer with $f_* = \deg f \cdot \mathrm{id}$ on $H_n(S^n)$ |
| $C_n^{\mathrm{CW}}(X) = \mathbb{Z}[\mathcal{E}_n]$ | Cellular chains, free on the $n$-cells |
| $\partial_n$ | Cellular boundary; $\partial_n e^n_\alpha = \sum_\beta \deg(q_\beta \varphi_\alpha) e^{n-1}_\beta$ |
| $q_\beta$ | Collapse of $X^{n-1}$ onto the cell $e^{n-1}_\beta$ |
| $H_n^{\mathrm{CW}}(X)$ | Homology of the cellular complex, $\cong H_n(X)$ |
| $\chi(X) = \sum_n (-1)^n \#\mathcal{E}_n$ | Euler characteristic; equals $\sum_n(-1)^n\operatorname{rk}H_n(X)$ |
| $X/A$ | Quotient by a subcomplex; cells of $X$ not in $A$ plus one $0$-cell |
| $X\wedge Y = (X\times Y)/(X\vee Y)$ | Smash product of based complexes |
| $\Sigma X = S^1\wedge X$ | Reduced suspension |
| $G_k(\mathbb{R}^n)$, $\mathbb{RP}^n$, $\mathbb{CP}^n$, $\mathbb{HP}^n$ | Grassmannian and projective spaces with their cell structures |
| $\operatorname{rk}$ | Rank of a finitely generated abelian group |





## Further Reading

- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for CW complexes, the homotopy extension property, cellular approximation and cellular homology.
- Glen E. Bredon, *Topology and Geometry* (Springer, 1993), for the cell structures of the classical groups and homogeneous spaces.
- Albrecht Dold, *Lectures on Algebraic Topology* (Springer, 2nd ed. 1980), for cofibrations and the homotopy extension property in the general categorical setting.
- Allen Hatcher, *Vector Bundles and K-Theory* (self-published, 2009), for the Schubert cell decomposition of the Grassmannians.
- Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology* (Springer, 1982), for the cell-count computation of the Euler characteristic and its differential-geometric counterpart.
- William S. Massey, *A Basic Course in Algebraic Topology* (Springer, 1991), for the cellular boundary formula and its use in computations.
- Edwin H. Spanier, *Algebraic Topology* (McGraw–Hill, 1966), for CW complexes as cofibrant objects and the general homotopy theory of cell attachments.
