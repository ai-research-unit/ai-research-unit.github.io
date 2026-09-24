
# __Geometric Group Theory__

## Introduction

Geometric group theory studies a finitely generated group by turning it into a metric space. The construction is the **Cayley graph**: fix a finite generating set $S$ and draw a vertex for each group element and an edge between $g$ and $gs$ for each $s \in S$; the graph carries the graph distance, and the group acts on it by left translation. The distance between two vertices is the **word metric** — the length of the shortest word in $S \cup S^{-1}$ representing the element — and it depends on the generating set only up to a **quasi-isometry**: a map that distorts distances by a bounded multiplicative and additive error. Quasi-isometry is the equivalence relation under which a group is studied, and it is coarse: it forgets the finite structure, the actual generating set and the local geometry, and retains the growth of balls, the number of ends, the large-scale connectivity and the behaviour at infinity.

The subject begins with two theorems attributed to Švarc and Milnor: a group acting properly and cocompactly by isometries on a proper geodesic metric space is finitely generated and quasi-isometric to the space, so a uniform lattice in a Lie group is quasi-isometric to the symmetric space it acts on, and its large-scale geometry is the geometry of that space. The subject then asks which properties of a group are quasi-isometry invariants — the growth type, the number of ends, amenability, hyperbolicity, virtual nilpotency — and how far a group is determined by its large-scale geometry, the question of quasi-isometric rigidity.

The article develops the Cayley graph and the word metric, the Švarc–Milnor lemma, the definition and the invariants of quasi-isometry, the growth of groups with the theorems of Milnor, Wolf and Gromov, the theory of ends with the theorem of Hopf and the splitting theorem of Stallings, and the principal rigidity theorems. The input from Part I is the theory of group presentations and free groups of *Groups*; the metric input is the distance of *Metric, Uniform and Complete Spaces* in Foundations of Topology, which is the one structure this Part adds; the Lie-theoretic input — symmetric spaces, lattices — is that of the written Lie-group articles, *Lattices in Lie Groups* and *Property (T)*. The **Cayley graph** and the **quasi-isometry** are constructed here, since no article above attaches a graph to a group; the underlying graph, its distance and the tree are those of *Graph Theory*, above this article in the menu, and the graph theory is elementary and standard.

The boundary with Part III is the one fixed for this block. What is developed here is the metric and coarse structure: the word metric, quasi-isometry, the growth function, the ends, and the rigidity statements. What is deferred is the **analytic** theory: the asymptotic cones, whose construction requires the limits of Part III; the harmonic analysis and the spectral theory on the boundary at infinity, the Patterson–Sullivan measures and the ergodic theory of the geodesic flow, all of which belong to *Analysis on Groups*. The **hyperbolic groups** and the detailed structure of the boundary at infinity are not covered here, as are the **amenable groups** and the splittings of the Stallings theorem. No physics is invoked.

## Cayley Graphs and Word Metrics

### Graphs and the Cayley Graph

**Definition.** A **graph** $\mathcal{G}$ consists of a set $V$ of **vertices**, a set $E$ of **edges** and two maps $E \to V$ assigning to each edge its two **endpoints**; the graph is **locally finite** if every vertex is the endpoint of finitely many edges, and **connected** if any two vertices are joined by a chain of edges. The **graph distance** $d_\mathcal{G}(u,v)$ is the least number of edges in a chain from $u$ to $v$, or $+\infty$ if there is none; it is a distance when the graph is connected. An **isometry** of graphs is a bijection of the vertices preserving adjacency. A graph is a **tree** if it is connected and has no closed chain of distinct edges beyond the trivial ones.

**Definition (Cayley graph).** Let $G$ be a group and let $S \subseteq G$ be a subset. The **Cayley graph** $\operatorname{Cay}(G,S)$ has vertex set $G$ and, for each $g \in G$ and each $s \in S$, an edge from $g$ to $gs$; the graph is locally finite exactly when $S$ is finite, and connected exactly when $S$ generates $G$. When $S$ is symmetric ($S = S^{-1}$) and does not contain the identity, the graph is undirected and $G$ acts on it by left translation, $g\cdot v = gv$, by isometries. Two such graphs for different finite generating sets are quasi-isometric, by the word-metric comparison below.

**Example (free groups and trees).** Let $F_n$ be the free group on the generators $x_1,\dots,x_n$ and let $S = \{x_1^{\pm1}, \dots, x_n^{\pm1}\}$. The Cayley graph $\operatorname{Cay}(F_n,S)$ is the **regular tree** of degree $2n$: a word in the generators is reduced exactly when the corresponding edge path never immediately backtracks, and the free group's normal form theorem says that each vertex is reached by a unique reduced word. The tree is locally finite and has exponential growth.

**Example (free abelian groups and grids).** For $G = \mathbb{Z}^n$ and $S$ the standard basis with inverses, the Cayley graph is the integer lattice in $\mathbb{R}^n$ with the standard edges, the $n$-dimensional grid: each vertex has $2n$ neighbours, the balls grow polynomially of degree $n$, and the graph is quasi-isometric to $\mathbb{R}^n$ with the Euclidean distance.

### The Word Metric

**Definition.** Let $G$ be generated by a symmetric set $S$ containing the identity, and let

$$
|g|_S = \min\{k : g = s_1\cdots s_k, \ s_i \in S\}
$$

be the **word length** of $g$; then $d_S(g,h) = |g^{-1}h|_S$ is the **word metric**, the graph distance in $\operatorname{Cay}(G,S)$. It is left-invariant: $d_S(kg,kh) = d_S(g,h)$, because $|(kg)^{-1}(kh)|_S = |g^{-1}h|_S$. Two finite symmetric generating sets $S, T$ give equivalent word metrics:

$$
\tfrac{1}{C}d_S(g,h) \leq d_T(g,h) \leq C\,d_S(g,h) \qquad \text{for all } g,h,
$$

with $C = \max\{\max_{s\in S}|s|_T, \max_{t\in T}|t|_S\}$, so that the identity map $\operatorname{Cay}(G,S)\to\operatorname{Cay}(G,T)$ is a **bi-Lipschitz** equivalence.

**Proof.** Writing $g^{-1}h$ as a word in $T$ of length $d_T(g,h)$ and then each $t$ as a word in $S$ of length at most $C$ gives $d_S \leq C d_T$; the other inequality is symmetric. $\square$

**Remark.** The word metric is well defined only after a generating set is fixed, and the identity map between two Cayley graphs of the same group is bi-Lipschitz, hence in particular a quasi-isometry. This is why the coarse statements of the subject are properties of the group and not of the presentation, and why a *finite* generating set is required: without finiteness the word metric can be distorted arbitrarily.

### The Švarc–Milnor Lemma

**Definition.** A metric space $X$ is **proper** if its closed bounded subsets are compact, and **geodesic** if for all $x,y\in X$ there is an isometric embedding of the interval $[0,d(x,y)]$ into $X$ with endpoints $x, y$. A group $G$ acts **properly discontinuously** on $X$ if for every bounded set $B$ the set $\{g : gB\cap B \neq \emptyset\}$ is finite, and **cocompactly** if $X/G$ is compact.

**Theorem (Švarc–Milnor).** Let $X$ be a proper geodesic metric space and let $G$ act on $X$ by isometries, properly discontinuously with compact quotient. Then $G$ is finitely generated and for any $x_0 \in X$ the orbit map $g \mapsto gx_0$ is a quasi-isometry $G \to X$ with respect to any word metric on $G$.

**Proof sketch.** Choose $x_0 \in X$ and $R > 0$ such that the balls $gB(x_0,R)$ cover $X$, possible by compactness of $X/G$; let $S = \{g : gB(x_0,2R)\cap B(x_0,2R)\neq\emptyset\}$, which is finite by proper discontinuity. The set $S$ generates: for any $g$, the geodesic from $x_0$ to $gx_0$ can be divided into a chain of points $x_0 = y_0, y_1, \dots, y_k = gx_0$ with $d(y_i, y_{i+1}) \leq R$, each $y_i$ lies in some $g_iB(x_0,R)$, and the elements $g_i^{-1}g_{i+1}$ lie in $S$, since $d(x_0, g_i^{-1}g_{i+1}x_0) \leq 3R \leq 4R$, so $g$ is a product of at most $k$ elements of $S$; the number $k$ is bounded above by a constant times $d(x_0,gx_0)/R$, which gives $|g|_S \leq C d(x_0,gx_0)$. Conversely, each $s\in S$ moves $x_0$ by at most $4R$, so $d(x_0,gx_0) \leq |g|_S\cdot\max_{s\in S}d(x_0,sx_0)$, giving the other inequality with the multiplicative constant $\max_{s\in S}d(x_0,sx_0)$. Hence the orbit map is a quasi-isometry; the details of the choice of the covering radius are standard. $\square$

**Corollary.** Let $\Gamma$ be a uniform lattice in a connected Lie group $G$ and let $X = K\backslash G$ be the associated homogeneous space with a $G$-invariant proper distance, where $K$ is a maximal compact subgroup. Then $\Gamma$ is finitely generated and quasi-isometric to $X$. In particular two uniform lattices in the same $G$ are quasi-isometric, and a uniform lattice in $G$ is quasi-isometric to every other cocompact discrete group of isometries of $X$.

**Proof.** The action of $\Gamma$ on $X$ is by isometries, properly discontinuous because $\Gamma$ is discrete, and cocompact because $\Gamma$ is uniform; the hypotheses of Švarc–Milnor are satisfied. $\square$

**Example (the case of a cusp).** For a **non-uniform** lattice the lemma does not apply, because the quotient $X/\Gamma$ is not compact: the quotient has cusps, its diameter is infinite, and the orbit map is not a quasi-isometry. The modular group $PSL_2(\mathbb{Z})$ is the standard witness: it is virtually free, hence quasi-isometric to a tree, while the upper half-plane is not quasi-isometric to a tree. This is the reason the geometric group theory of lattices develops differently according to whether the lattice is uniform.

## Quasi-Isometries

### Definition and Basic Properties

**Definition.** A map $f : X \to Y$ between metric spaces is a **quasi-isometric embedding** if there are constants $\lambda \geq 1$ and $C \geq 0$ with

$$
\tfrac{1}{\lambda}d_X(x,x') - C \;\leq\; d_Y(f(x),f(x')) \;\leq\; \lambda\,d_X(x,x') + C \qquad \text{for all } x,x' \in X .
$$

A **quasi-isometry** is a quasi-isometric embedding with a quasi-isometric inverse: a map $g : Y \to X$ and a constant $C'$ with $d_X(gf(x),x) \leq C'$ and $d_Y(fg(y),y) \leq C'$ for all $x,y$. The relation "there is a quasi-isometry $X \to Y$" is an equivalence relation on metric spaces, and a property preserved by quasi-isometry is a **quasi-isometry invariant**. A map is **coarsely Lipschitz**, or a **quasi-isometric embedding on the large scale**, when the second inequality holds with some $\lambda, C$.

**Proposition (elementary invariants).** Quasi-isometry preserves:

**(a)** the property of having finite diameter, and more generally the statement that two spaces have finite **Hausdorff distance**;

**(b)** the growth type of a space, that is, the equivalence class of the function $r \mapsto |B(x_0,r)|$ up to the relation $f \asymp g$ meaning $f(r) \leq Cg(\lambda r + C)$ and conversely;

**(c)** the number of ends of a locally finite graph, and hence of a finitely generated group;

**(d)** coarse connectivity and the finiteness of the number of connected components of the complement of a bounded set.

**Proof.** (a) and (b) are immediate from the inequalities in the definition: a ball of radius $r$ in $X$ is carried into a ball of radius $\lambda r + C$ in $Y$, and the inverse gives the reverse inclusion up to constants. (c) the number of ends counts the components of $X\smallsetminus B(x_0,r)$ that are unbounded, a number which is unchanged when $X$ is replaced by a space at finite Hausdorff distance and which is stabilised for $r$ large; the quasi-isometry gives a bijection of the components of the complements of two sufficiently large balls. (d) is (c) applied to the complement. $\square$

### Examples and Non-Examples

**Example (the free groups).** The free groups $F_m$ and $F_n$ are quasi-isometric for all $m,n \geq 2$: each is quasi-isometric to its Cayley tree, a regular tree of degree $2m$ or $2n$, and any two regular trees of degree at least $3$ are quasi-isometric, since one constructs a quasi-isometry by mapping a base vertex to a base vertex, one infinite ray to an infinite ray, and extending over the levels. The groups are not isomorphic for $m \neq n$, so quasi-isometry is strictly coarser than isomorphism.

**Example (the Euclidean spaces and their lattices).** $\mathbb{Z}^n$ is quasi-isometric to $\mathbb{R}^n$; $\mathbb{Z}^n$ and $\mathbb{Z}^m$ are quasi-isometric exactly when $n = m$, since the growth is polynomial of degree $n$ and the degree is a quasi-isometry invariant. Similarly $\mathbb{R}^n$ and $\mathbf{H}^n$ are not quasi-isometric for any $n$, since the growth of balls is polynomial in the first and exponential in the second.

**Example (the rank-one hyperbolic spaces).** The real hyperbolic space $\mathbf{H}^n$ and the complex hyperbolic space $\mathbf{H}^n_{\mathbb{C}} = SU(n,1)/S(U(n)\times U(1))$ are both of exponential growth. They have the same topological dimension when $n$ is replaced by $2n$ in the first, so the coarse dimension does not separate them; yet $\mathbf{H}^{2n}$ and $\mathbf{H}^n_{\mathbb{C}}$ are not quasi-isometric for $n \geq 2$, because the asymptotic cone of the first is the Euclidean space $\mathbb{R}^{2n-1}$ while that of the second is the Heisenberg group of dimension $2n-1$, and these are not quasi-isometric by the rigidity theorem of Pansu. The refinement of the invariants needed to separate negatively curved symmetric spaces of the same dimension — the Carnot structure of the asymptotic cone and the conformal structure of the boundary at infinity — is part of the subject.

**Example (a finite group).** A finite group is quasi-isometric to a point, so its quasi-isometry class carries no information; this is a general feature: quasi-isometry sees only the large scale, and the finite groups are invisible to it. Consequently the statements of the subject always concern infinite finitely generated groups, and the theory is stated up to finite-index phenomena and finite normal subgroups.

### Quasi-Isometry Invariants

**Theorem.** The following properties of finitely generated groups are quasi-isometry invariants:

**(a)** the growth type, polynomial, exponential or intermediate;

**(b)** the number of ends;

**(c)** amenability and the Følner condition, in the sense that a group is amenable if and only if any group quasi-isometric to it is;

**(d)** hyperbolicity in the sense of Gromov, so that a group quasi-isometric to a hyperbolic group is hyperbolic;

**(e)** being virtually nilpotent, more precisely, the degree of polynomial growth;

**(f)** being virtually free.

**Proof sketch.** (a) and (b) are the content of the previous proposition. (c) is the theorem of Rosenblatt: amenability of a finitely generated group is characterised by the Følner condition, which is a statement about the existence of large finite sets with small boundary and is therefore a coarse property of the Cayley graph; a quasi-isometry carries a Følner sequence to a Følner sequence. (d) is the quasi-isometry invariance of hyperbolicity, proved by the four-point condition and the stability of geodesics; it is the central result. (e) is Gromov's polynomial growth theorem together with the invariance of the growth degree. (f) is the theorem of Stallings and Dunwoody: a quasi-isometry preserves the number of ends, so a group quasi-isometric to a free group has the ends of a free group; the splitting theorem for groups with infinitely many ends then produces a decomposition over finite subgroups from which virtual freeness follows by induction. The details are standard and are quoted from the literature. $\square$

**Corollary.** Among the finitely generated groups, the quasi-isometry class of $\mathbb{Z}^n$ contains exactly the groups that are virtually $\mathbb{Z}^n$; the class of a free group of rank at least two contains exactly the virtually free groups which are not virtually cyclic; and the class of a group of exponential growth contains no group of polynomial growth.

**Proof.** A group quasi-isometric to $\mathbb{Z}^n$ has polynomial growth of degree $n$, hence is virtually nilpotent by Gromov's theorem; a virtually nilpotent group quasi-isometric to $\mathbb{Z}^n$ is virtually $\mathbb{Z}^n$, by the structure theory of finitely generated nilpotent groups. The growth degree alone does not suffice here: the discrete Heisenberg group has growth degree $4$ and is not quasi-isometric to $\mathbb{Z}^4$, since its asymptotic cone is the Heisenberg group rather than $\mathbb{R}^4$. The second statement is the invariance of virtual freeness. The third is the invariance of the growth type. $\square$

## Growth of Groups

### Growth Functions

**Definition.** Let $G$ be generated by a finite symmetric set $S$ and let $a_n = |\{g : |g|_S \leq n\}|$ be the number of elements of word length at most $n$. The **growth function** is $n \mapsto a_n$, and the **growth type** of $G$ is the class of $a_n$ up to the equivalence $f \asymp g$ of the previous section. The group has **polynomial growth** if $a_n \leq C n^d$ for some constants, **exponential growth** if $a_n \geq c\,\lambda^n$ for some $\lambda > 1$, and **intermediate growth** otherwise: $a_n$ grows faster than every polynomial and slower than every exponential.

**Proposition.** The growth type is independent of the finite generating set, and it is a quasi-isometry invariant of the group.

**Proof.** A change of generating set changes the word metric by a bi-Lipschitz map as above, which changes the counting function $a_n$ by the substitution $n \mapsto Cn$, and the relation $\asymp$ absorbs this. A quasi-isometry between groups carries an orbit to a quasi-dense subset and converts balls to balls with $\lambda n + C$ in place of $n$, which again preserves the equivalence class. $\square$

**Example.** $\mathbb{Z}^n$ has polynomial growth of degree $n$: the counting function is asymptotically the volume of the ball of radius $n$ in $\mathbb{R}^n$, a constant times $n^n$. A free group $F_n$ with $n \geq 2$ has exponential growth, since each reduced word of length $k$ extends in $2n-1$ ways, so $a_k \geq c(2n-1)^k$; equivalently, the Cayley tree has exponential volume growth, and this is the quantitative form of the failure of amenability of the free group. A finite group has constant growth.

### The Milnor–Wolf Theorem and Gromov's Theorem

**Theorem (Milnor–Wolf).** Let $G$ be a finitely generated solvable group. Then $G$ has polynomial growth if and only if it is virtually nilpotent. Consequently a finitely generated solvable group has either polynomial growth or exponential growth, and no intermediate growth.

**Proof sketch.** A virtually nilpotent group has polynomial growth: the lower central series of a finitely generated nilpotent group exhausts the group by finitely many cyclic extensions, and each extension multiplies the growth by at most a polynomial factor. Conversely, a solvable group of polynomial growth is virtually nilpotent: one argues by induction on the derived length, using that a finitely generated abelian group of subexponential growth is finite and that a quotient of polynomial growth with a finite kernel forces the kernel to be finite. The theorem is due to Milnor in the general case and to Wolf for the solvable case, and is quoted from the literature. $\square$

**Theorem (Gromov).** A finitely generated group of polynomial growth is virtually nilpotent, and the degree of growth equals the integer $\sum_{k\geq1} k\,\operatorname{rank}(G_k/G_{k+1})$ computed from the lower central series of the finite-index nilpotent subgroup.

**Proof sketch.** The proof is Gromov's theorem on groups of polynomial growth, one of the landmarks of the subject: a group of polynomial growth has a Cayley graph with a finite-dimensional asymptotic cone, the asymptotic cone is locally compact and has a Lie-group structure, and the group is shown to act on the cone in a way that forces a finite-index subgroup to be nilpotent by Hilbert's fifth problem (the locally Euclidean topological group is a Lie group, by *Hilbert's Fifth Problem and Infinite-Dimensional Lie Theory*) and the structure theory of Lie groups. The explicit degree formula is the computation of Bass and Guivarc'h. The asymptotic cone is constructed with the limits of Part III, and the theorem is quoted from the literature. $\square$

**Corollary (the trichotomy).** A finitely generated group of polynomial growth is virtually nilpotent; a finitely generated group of intermediate growth is neither virtually nilpotent nor of exponential growth; and a finitely generated group containing a non-abelian free subgroup has exponential growth. In particular the three classes — polynomial, intermediate, exponential growth — are non-empty and mutually exclusive, and they are quasi-isometry invariants.

### Intermediate Growth

**Example (the Grigorchuk group).** There exist finitely generated groups of intermediate growth. The first example is the **Grigorchuk group**, a group of automorphisms of the binary rooted tree, generated by four involutions with the relations of a self-similar action; its growth function satisfies

$$
e^{c_1 n^{\alpha_1}} \;\leq\; a_n \;\leq\; e^{c_2 n^{\alpha_2}} \qquad \text{for some } 0 < \alpha_1 \leq \alpha_2 < 1 ,
$$

so the group is neither of polynomial nor of exponential growth; the best known bounds place the growth exponent $\alpha = \lim \log\log a_n/\log n$, when it exists, between approximately $0.51$ and $0.77$, and its exact value is not known. The group is amenable and residually finite, and it is the standard counterexample to the generalised Milnor conjecture that every finitely generated group of subexponential growth is virtually nilpotent. The construction and the bounds are quoted as standard from the literature of Grigorchuk and of Bartholdi–Erschler.

## Ends of Groups

### The Number of Ends

**Definition.** Let $G$ be a finitely generated group and let $\operatorname{Cay}(G,S)$ be a Cayley graph. The **number of ends** $e(G)$ is the number of connected components of $\operatorname{Cay}(G,S)\smallsetminus B(e,n)$ that are unbounded, for $n$ large; the number is independent of $n$ and of $S$, and is a quasi-isometry invariant. Equivalently, $e(G)$ is the number of ends of the group as the number of ways the group can go to infinity.

**Theorem (Hopf).** A finitely generated group has $0$, $1$, $2$ or infinitely many ends. The number is $0$ exactly when the group is finite, $2$ exactly when the group is virtually $\mathbb{Z}$, and $\infty$ exactly when the group splits as a nontrivial amalgamated free product or HNN extension over a finite group; the remaining case, $1$ end, is the generic one and contains the groups $\mathbb{Z}^n$ with $n \geq 2$, the lattices in higher-rank semisimple groups, and the hyperbolic groups of dimension at least two.

**Proof sketch.** The number of ends is a quasi-isometry invariant, and the possible values are $0,1,2,\infty$ because the space of ends is compact and totally disconnected when the graph is locally finite. The case $2$ is Hopf's theorem: a group with two ends contains a subgroup of finite index that is infinite cyclic, by considering the action on the two-ended graph and its translation length. The infinitely-many-ends case is the content of the Stallings theorem stated; the one-end case is the complement. $\square$

**Theorem (Stallings).** A finitely generated group has infinitely many ends if and only if it splits nontrivially over a finite subgroup: it is either an amalgamated free product $A*_C B$ with $C$ finite and both $A$ and $B$ proper, or an HNN extension $A*_C$ with $C$ finite. In particular a finitely generated group with infinitely many ends is virtually free if and only if the vertex groups can be chosen finite, and this holds exactly for the virtually free groups.

**Proof sketch.** The theorem is proved by the theory of the action of $G$ on its Cayley graph and on the ends: a group with infinitely many ends acts on the tree of its ends with finite stabilisers of the edges, and the quotient graph of groups gives the splitting; conversely a splitting over a finite group produces the ends from the two vertex groups. The full proof is the theorem of Stallings, and the tree on which the group acts is the object. $\square$

## Quasi-Isometric Rigidity

### Rigidity Statements

**Definition.** A group $G$ is **quasi-isometrically rigid** if every finitely generated group quasi-isometric to $G$ is virtually isomorphic to $G$, that is, contains a finite-index subgroup isomorphic to a finite-index subgroup of $G$; more generally the **quasi-isometry classification** of a class of groups asks for the groups in the quasi-isometry class of a given one.

**Theorem (rigidity).** 

**(a)** $\mathbb{Z}^n$ is quasi-isometrically rigid: a group quasi-isometric to $\mathbb{Z}^n$ is virtually $\mathbb{Z}^n$. This combines Gromov's polynomial growth theorem with the structure theory of nilpotent groups, since the asymptotic cone of such a group is $\mathbb{R}^n$ and a virtually nilpotent group with that cone is virtually abelian.

**(b)** A free group of rank at least two is quasi-isometrically rigid among finitely generated groups: a group quasi-isometric to $F_n$, $n \geq 2$, is virtually free. This follows from the invariance of the number of ends and the Stallings splitting, with an induction on the complexity of the splitting.

**(c)** A uniform lattice in a connected semisimple Lie group with trivial centre, no compact factors and all simple factors of real rank at least two is quasi-isometrically rigid: quasi-isometries between such lattices are at bounded distance from isometries, by the theorem of Kleiner and Leeb in its lattice form. This is the quasi-isometric form of Mostow rigidity, and it extends to the quasi-isometric classification of the higher-rank lattices.

**(d)** The nilpotent groups are quasi-isometrically rigid in the graded sense: the quasi-isometry class of the asymptotic cone of a nilpotent group determines the group up to commensurability and rescaling, by the theorem of Pansu, and quasi-isometries between lattices in nilpotent Lie groups are at bounded distance from affine maps composed with translations.

**Proof sketch.** (a) and (b) are assembled from the invariants developed above. (c) and (d) are the rigidity theorems of Kleiner–Leeb and Pansu, whose proofs use the structure of the boundary and of the asymptotic cone; the asymptotic cone is constructed with the limits of Part III. The statements are quoted from the literature. $\square$

**Remark (the limits of rigidity).** Quasi-isometric rigidity fails in general, and it fails badly in rank one. Every uniform lattice in $PSL_2(\mathbb{R})$ is quasi-isometric to the hyperbolic plane, so any two of them are quasi-isometric to each other although they are in general incommensurable; every non-uniform lattice in $PSL_2(\mathbb{R})$ is virtually free, hence quasi-isometric to a tree; and the two families are not quasi-isometric to one another. For the lattices in $SO(n,1)$, $n \geq 3$, the quasi-isometry classification is governed by the quasi-conformal maps of the boundary sphere, a problem solved in the cocompact and in the cusped cases by Schwartz and by others; the boundary theory is developed and the conformal and measure-theoretic part belongs to Part III. The general problem of classifying finitely generated groups up to quasi-isometry is open.

## The Boundary with Analysis

- The **asymptotic cones** of a metric space, the **Gromov–Hausdorff distance** and the convergence of metric spaces are constructed with the limits of Part III and with the metric geometry of the later Part II slots; the article uses only the statements of the theorems that need them.
- The **Patterson–Sullivan measures**, the **quasi-conformal measures** on the boundary at infinity, the **ergodic theory of the geodesic flow** and the spectral theory of the Laplacian on a hyperbolic quotient areand *Analysis on Groups* in Part III.
- The **hyperbolic groups** and the **boundary at infinity** with its topology are not covered here; the **amenable groups** and the Følner condition are standard; and the splittings of the Stallings theorem are those.
- What is *not* deferred: the Cayley graph and the word metric; the Švarc–Milnor lemma and its lattice corollary; the definition and invariants of quasi-isometry; the growth classification with the Milnor–Wolf and Gromov theorems at the level of statements; the number of ends and the Hopf and Stallings theorems; and the rigidity statements.

## Summary

A finitely generated group is turned into a metric space by its Cayley graph, whose graph distance is the word metric $d_S(g,h) = |g^{-1}h|_S$. Different finite generating sets give bi-Lipschitz equivalent metrics, so the group has a well-defined coarse geometry, studied up to quasi-isometry: a map distorting distances by at most a multiplicative factor $\lambda$ and an additive constant $C$. The Švarc–Milnor lemma states that a group acting properly discontinuously and cocompactly by isometries on a proper geodesic space is finitely generated and quasi-isometric to the space; consequently a uniform lattice in a Lie group is quasi-isometric to the associated symmetric space, while a non-uniform lattice is not, the cusp being the obstruction.

Quasi-isometry preserves the growth type, the number of ends, amenability, hyperbolicity, virtual nilpotency and virtual freeness. The growth theorem of Milnor and Wolf states that a finitely generated solvable group has polynomial growth exactly when it is virtually nilpotent, and Gromov's theorem extends this to all finitely generated groups: polynomial growth implies virtually nilpotent, with the degree given by the Bass–Guivarc'h formula. The Grigorchuk group has intermediate growth and shows that the three growth types are distinct. A finitely generated group has $0$, $1$, $2$ or infinitely many ends by Hopf's theorem; two ends mean virtually $\mathbb{Z}$, and infinitely many ends mean a nontrivial splitting over a finite subgroup by Stallings' theorem, which is the theme .

Quasi-isometric rigidity holds for $\mathbb{Z}^n$, for the free groups of rank at least two, for the higher-rank lattices by the theorem of Kleiner and Leeb in the lattice form of Mostow rigidity, and for the nilpotent groups in the graded sense of Pansu. The limits of the theory — the asymptotic cones, the boundary measures and the ergodic theory — belong to Part III. The Cayley graph, the word metric and the quasi-isometry are the constructions that make all of this a chapter of topology on groups.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Cay}(G,S)$ | Cayley graph of $G$ with respect to $S \subseteq G$ |
| $d_\mathcal{G}$, $d_S$ | Graph distance; word metric $d_S(g,h) = \vert g^{-1}h\vert _S$ |
| $\vert g\vert _S$ | Word length with respect to $S$ |
| $S$ symmetric | $S = S^{-1}$, so that the Cayley graph is undirected |
| quasi-isometry | Map with $\lambda^{-1}d_X - C \leq d_Y(fx,fx') \leq \lambda d_X + C$ and a quasi-inverse |
| $\lambda$, $C$ | Multiplicative and additive constants of a quasi-isometry |
| $f \asymp g$ | Equivalence of growth functions: $f(r) \leq C g(\lambda r+C)$ and conversely |
| proper metric space | Closed bounded sets are compact |
| geodesic metric space | Every pair joined by an isometric image of an interval |
| properly discontinuous action | $\{g : gB\cap B\neq\emptyset\}$ finite for every bounded $B$ |
| Švarc–Milnor lemma | Proper cocompact isometric action $\Rightarrow$ $G$ finitely generated and quasi-isometric to $X$ |
| $a_n$, growth function | Number of elements of word length $\leq n$ |
| polynomial/exponential/intermediate growth | Growth type of $a_n$ |
| Milnor–Wolf | Finitely generated solvable: polynomial growth $\Leftrightarrow$ virtually nilpotent |
| Gromov's theorem | Polynomial growth $\Leftrightarrow$ virtually nilpotent |
| Grigorchuk group | Group of intermediate growth; $a_n \asymp e^{n^{\alpha}}$, $\alpha \approx 0.767$ |
| $e(G)$ | Number of ends: $0$, $1$, $2$ or $\infty$ (Hopf) |
| Stallings' theorem | Infinitely many ends $\Leftrightarrow$ splitting over a finite subgroup |
| quasi-isometric rigidity | Every group quasi-isometric to $G$ is virtually isomorphic to $G$ |
| $\mathbb{Z}^n$, $F_n$, $\mathbf{H}^n$ | The basic models: grid, tree, hyperbolic space |
| asymptotic cone | Blow-down limit of a metric space; constructed with Part III limits |









## Further Reading

- John Milnor, *A note on curvature and the fundamental group*, Journal of Differential Geometry 2 (1968), 1–7, for the Švarc–Milnor lemma and the growth of groups.
- Albert S. Švarc, *A volume invariant of coverings*, Doklady Akademii Nauk SSSR 105 (1955), 32–34, for the original cocompactness lemma.
- Mikhael Gromov, *Groups of polynomial growth and expanding maps*, Publications Mathématiques de l'IHÉS 53 (1981), 53–73, for the polynomial growth theorem.
- Joseph A. Wolf, *Growth of finitely generated solvable groups and curvature of Riemannian manifolds*, Journal of Differential Geometry 2 (1968), 421–446, for the solvable case.
- Hyman Bass, *The degree of polynomial growth of finitely generated nilpotent groups*, Proceedings of the London Mathematical Society 25 (1972), 603–614, for the degree formula.
- Rostislav Grigorchuk, *On the Milnor problem of group growth*, Doklady Akademii Nauk SSSR 271 (1983), 30–33, for the group of intermediate growth.
- John Stallings, *On torsion-free groups with infinitely many ends*, Annals of Mathematics 88 (1968), 312–334, for the splitting theorem.
- Heinz Hopf, *Enden offener Räume und unendliche diskontinuierliche Gruppen*, Commentarii Mathematici Helvetici 16 (1944), 81–100, for the number of ends.
- Martin Bridson and André Haefliger, *Metric Spaces of Non-Positive Curvature* (Springer, 1999), for the systematic treatment of the Cayley graph, quasi-isometry and rigidity.
- Pierre de la Harpe, *Topics in Geometric Group Theory* (University of Chicago Press, 2000), for a textbook introduction with the growth theory.
- Bruce Kleiner and Bernhard Leeb, *Rigidity of quasi-isometries for symmetric spaces and Euclidean buildings*, Publications Mathématiques de l'IHÉS 86 (1997), 115–197, for the quasi-isometric rigidity of higher-rank lattices.
- Pierre Pansu, *Métriques de Carnot–Carathéodory et quasiisométries des espaces symétriques de rang un*, Annals of Mathematics 129 (1989), 1–60, for the rigidity of the asymptotic cone.
