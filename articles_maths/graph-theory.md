
# __Graph Theory__

## Introduction

A graph is the simplest structure that a set can carry beyond its own equality: a **relation** on it, read as adjacency. Everything in this article is a consequence of that one observation, and the article is the corpus's first purely combinatorial subject — the first place where the objects counted are configurations rather than algebraic operations, and where the standard questions are existence, connectivity and extremality rather than closure. It is placed at the end of *Foundations of Topology* because its only prerequisites are behind it: the sets, functions and relations of *Sets, Functions and Relations* of Part I, and the metric space of *Metric, Uniform and Complete Spaces*, an earlier entry of this category. A graph is not a topological space here, and no topology beyond the metric is used.

The reason a topological category holds a combinatorial article is the **graph distance**, the number of edges on a shortest path between two vertices. It is a metric, it is the structure through which the group-theoretic articles of *Topology on Groups* read a Cayley graph, and it is the reason this article is placed where it is: the combinatorial objects come first, and the metric attached to them comes next. The **Cayley graph**, the **word metric** and the **Bass–Serre tree** are constructed in *Topology on Groups*, where a group acts on them; this article supplies the graph and its distance and does not attach them to an algebraic object.

Two boundaries are held throughout. First, no algebra is imported: a graph is a set with a relation, not a module or an algebra, and the adjacency matrix as a linear operator, the graph Laplacian and graph homology belong to the articles that own linear and homological structure, if they belong to the corpus at all. Second, no topology beyond the metric appears: compactness, continuity of an invariant and limits are not available in this Part, and nothing below is stated in those terms. The standing convention of the corpus — a commutative ring with identity, modules on the left — is not needed here; the only structures are sets, relations and the metric space of *Metric, Uniform and Complete Spaces*.

Throughout, a graph is **simple** unless the contrary is said explicitly: no loops and at most one edge between a pair of vertices. The graph is written $\Gamma$, its vertex set $V(\Gamma)$ and its edge set $E(\Gamma)$, the letters $u,v,w,x,y$ denote vertices, $e$ an edge, and $n = |V(\Gamma)|$ and $m = |E(\Gamma)|$ are the order and the size. Where an argument needs a finite graph this is stated at the start of the result, so that the finite and the infinite cases are not confused.

## Graphs and Morphisms

### Graphs as Sets with a Relation

**Definition.** A **graph** $\Gamma$ consists of a set $V(\Gamma)$, the **vertices**, and a set $E(\Gamma)$ of two-element subsets of $V(\Gamma)$, the **edges**. An edge $\{u,v\}$ is written $uv$, and $u$ and $v$ are its **ends**; the vertices $u$ and $v$ are then **adjacent** or **neighbours**, written $u \sim v$, and the edge is **incident** with each of them. Equivalently, the adjacency relation is a symmetric, irreflexive relation $E(\Gamma) \subseteq V(\Gamma) \times V(\Gamma)$, and the passage between the two descriptions identifies such a relation with the family of two-element sets $\{u,v\}$ for which $(u,v) \in E(\Gamma)$. The number of vertices is the **order** of $\Gamma$ and the number of edges its **size**.

**Definition.** A **directed graph**, or **digraph**, is a pair $D = (U,A)$ with $A \subseteq U \times U$ an arbitrary relation; its elements are **arcs** and are written $(u,v)$ with $u$ the **tail** and $v$ the **head**. A digraph is **symmetric** if $(u,v) \in A$ implies $(v,u) \in A$, and the symmetric digraphs with no loops correspond exactly to the graphs above, with $U = V(\Gamma)$. The undirected theory is the one developed here; the directed case is named where it differs, and an orientation of an undirected graph is a digraph whose arcs are ordered pairs of vertices joined in the graph, one pair for each edge.

**Remark (what is excluded, and why).** A **loop** is an edge with equal ends and a **multigraph** allows several edges between the same pair. Neither occurs in a simple graph, and the restriction is not cosmetic: loops make the degree count of the handshake lemma below false, and multiple edges make the distance and the enumeration of cycles behave differently. Where a result needs one of them it is stated for the wider class and the class is named.

**Example (the standard families).** The **complete graph** $K_n$ has $n$ vertices and every pair joined. The **path** $P_n$ has vertices $1, \ldots, n$ and edges $\{i,i+1\}$. The **cycle** $C_n$ for $n \geq 3$ is the path $P_n$ with the additional edge $\{n,1\}$. The **empty graph**, or **edgeless graph**, $\overline{K_n}$ has $n$ vertices and no edges; the notation records that it is the complement of $K_n$, taken in the two-element subsets of its vertex set. The **complete bipartite graph** $K_{m,n}$ has a bipartition $V(\Gamma) = X \sqcup Y$ with $|X| = m$, $|Y| = n$ and all $mn$ edges between $X$ and $Y$. The counts are $|E(K_n)| = \binom n2$, $|E(P_n)| = n-1$, $|E(C_n)| = n$ and $|E(K_{m,n})| = mn$.

### Morphisms and Isomorphisms

**Definition.** A **graph morphism** $f : \Gamma \to \Lambda$ is a map $f : V(\Gamma) \to V(\Lambda)$ of vertex sets carrying every edge of $\Gamma$ to an edge of $\Lambda$: if $uv \in E(\Gamma)$ then $f(u)f(v) \in E(\Lambda)$. The morphism is an **isomorphism** if $f$ is a bijection and $f^{-1}$ is also a morphism, in which case $\Gamma$ and $\Lambda$ are **isomorphic**, written $\Gamma \cong \Lambda$; it is an **endomorphism** if $\Gamma = \Lambda$, and an **automorphism** if in addition it is an isomorphism. The set of automorphisms of $\Gamma$ is a group $\operatorname{Aut}(\Gamma)$ under composition, and it is a subgroup of the symmetric group on $V(\Gamma)$.

**Proposition.** Isomorphism is an equivalence relation on graphs.

*Proof.* The identity map is a morphism, the inverse of an isomorphism is an isomorphism by definition, and a composite of bijective edge-preserving maps is again one. $\square$

**Remark.** A graph morphism is more permissive than the drawing suggests: it need not be injective, and it may create adjacencies, since $u \not\sim w$ does not prevent $f(u) \sim f(w)$. It cannot, however, collapse an edge to a vertex: if $uv \in E(\Gamma)$ then $f(u)f(v) \in E(\Lambda)$, and a simple graph has no loops, so $f(u) \neq f(v)$ whenever $u \sim v$. An isomorphism, by contrast, preserves adjacency and non-adjacency both, since $uv \notin E(\Gamma)$ forces $f(u)f(v) \notin E(\Lambda)$ when $f^{-1}$ is a morphism; isomorphism is therefore the correct notion of "the same graph", and every invariant introduced below is an isomorphism invariant.

### Subgraphs and Induced Subgraphs

**Definition.** A **subgraph** $\Lambda \subseteq \Gamma$ is a graph with $V(\Lambda) \subseteq V(\Gamma)$ and $E(\Lambda) \subseteq E(\Gamma)$; it is **spanning** if $V(\Lambda) = V(\Gamma)$, and it is an **induced subgraph** on a set $W \subseteq V(\Gamma)$ if $V(\Lambda) = W$ and $E(\Lambda)$ consists of exactly those edges of $\Gamma$ with both ends in $W$, written $\Gamma[W]$. Thus a subgraph is obtained by deleting vertices and edges, and an induced subgraph by deleting vertices only, the edges among the survivors being kept. A **proper** subgraph is one with $V(\Lambda) \neq V(\Gamma)$ or $E(\Lambda) \neq E(\Gamma)$, and the deletion of a set of vertices is written $\Gamma - S = \Gamma[V(\Gamma) \setminus S]$, with $\Gamma - v$ for a single vertex.

**Example.** In $K_4$ with vertex set $\{1,2,3,4\}$, the subgraph with edges $\{12, 23, 34\}$ is the path $P_4$, a spanning subgraph; the induced subgraph on $\{1,2,3\}$ is $K_3$, and the induced subgraph on $\{1,2,3\}$ of the cycle $C_4 = K_{2,2}$ is the path $P_3$. Inducedness is not inherited by a spanning subgraph: $K_4$ contains $P_4$ as a spanning subgraph and contains no induced $P_4$, since every induced subgraph of a complete graph is complete.

### Degree and the Handshake Lemma

**Definition.** The **degree** $\deg v$ of a vertex $v$ is the number of its neighbours, $\deg v = |\{u : u \sim v\}|$; a vertex of degree $0$ is **isolated** and one of degree $1$ is a **leaf**. The graph is **locally finite** if every degree is finite, and **$d$-regular** if $\deg v = d$ for every $v$. The **maximum degree** and **minimum degree** are written $\Delta(\Gamma)$ and $\delta(\Gamma)$. In a digraph the **out-degree** and **in-degree** count the arcs with tail and head at the vertex.

**Theorem (handshake lemma).** For every finite graph $\Gamma$,

$$
\sum_{v \in V(\Gamma)} \deg v = 2\,|E(\Gamma)|.
$$

*Proof.* Count the pairs $(v,e)$ with $v$ an end of $e$. Each vertex $v$ contributes exactly $\deg v$ such pairs and each edge contributes exactly two, one for each of its ends, so the two counts are equal; no loop occurs, which is why every edge contributes two and not one. $\square$

**Corollary.** In every finite graph the number of vertices of odd degree is even.

*Proof.* The sum $\sum_v \deg v = 2|E(\Gamma)|$ is even, and it is congruent modulo $2$ to the number of odd-degree vertices. $\square$

**Corollary.** Every $d$-regular finite graph satisfies $d\,|V(\Gamma)| = 2|E(\Gamma)|$, so $d|V(\Gamma)|$ is even. In particular, there is no $d$-regular finite graph on $n$ vertices when $d$ and $n$ are both odd.

## Paths, Cycles and Connectedness

### Walks, Paths and Cycles

**Definition.** A **walk** in $\Gamma$ from $u$ to $v$ is a finite sequence $v_0, v_1, \ldots, v_k$ with $v_0 = u$, $v_k = v$ and $v_i \sim v_{i+1}$ for each $i$; its **length** is $k$, the number of edges traversed, and $u$ and $v$ are its **endpoints**. A walk is **closed** if $u = v$; a **path** is a walk with all vertices distinct; a **cycle** is a closed walk of length at least three with $v_0, \ldots, v_{k-1}$ distinct. A graph is **acyclic** if it contains no cycle. The **girth** $\operatorname{gir}\Gamma$ of a graph with a cycle is the least length of a cycle, and $\operatorname{gir}\Gamma = \infty$ if the graph is acyclic.

**Proposition.** If there is a walk from $u$ to $v$, there is a path from $u$ to $v$.

*Proof.* Choose a walk of least length among those from $u$ to $v$. If two of its vertices coincided, say $v_i = v_j$ with $i < j$, deleting the segment $v_{i+1}, \ldots, v_j$ would produce a shorter walk from $u$ to $v$, a contradiction; hence all vertices are distinct and the walk is a path. $\square$

**Example.** The girth of $C_n$ is $n$, of $K_n$ is $3$ for $n \geq 3$, and of $K_{m,n}$ is $4$ when $m, n \geq 2$. A graph with girth $\infty$ is exactly an acyclic graph.

### Connectedness and Components

**Definition.** Two vertices $u$ and $v$ are **connected** if there is a path from $u$ to $v$; equivalently, by the proposition above, if there is a walk from $u$ to $v$. The graph is **connected** if every two vertices are connected, and a **component** is an equivalence class of the relation of being connected.

**Theorem.** The relation "$u$ is connected to $v$" is an equivalence relation on $V(\Gamma)$.

*Proof.* The one-vertex walk $v_0 = v$ is a path of length zero, so the relation is reflexive; reversing a path gives a path in the opposite direction, so it is symmetric; and concatenating a walk from $u$ to $v$ with a walk from $v$ to $w$ gives a walk from $u$ to $w$, so it is transitive. $\square$

**Corollary.** The components partition $V(\Gamma)$, and a graph is connected if and only if it has exactly one component. Writing $c(\Gamma)$ for the number of components and $\Gamma_1, \ldots, \Gamma_{c}$ for the components, every edge lies within one $\Gamma_i$, so $E(\Gamma)$ is the disjoint union of the edge sets $E(\Gamma_i)$.

**Lemma (edge lower bound).** Every connected finite graph on $n$ vertices has at least $n-1$ edges.

*Proof.* Induct on $n$; the case $n = 1$ is vacuous. Let $v$ be a vertex and let $\Gamma_1, \ldots, \Gamma_k$ be the components of $\Gamma - v$, of orders $n_1, \ldots, n_k$ with $n_1 + \cdots + n_k = n-1$. By induction $|E(\Gamma_i)| \geq n_i - 1$, so $|E(\Gamma-v)| \geq (n-1) - k$. Each $\Gamma_i$ contains a neighbour of $v$: otherwise no edge of $\Gamma$ would join $\Gamma_i$ to $v$ or to any $\Gamma_j$, and $\Gamma$ would be disconnected. Hence $\deg v \geq k$, and

$$
|E(\Gamma)| \geq (n-1-k) + k = n-1. \qquad \square
$$

**Corollary.** For every finite graph $\Gamma$, $|E(\Gamma)| \geq n - c(\Gamma)$.

*Proof.* Apply the lemma to each component and add. $\square$

**Lemma (edge count of a forest).** Every finite acyclic graph with $n$ vertices, $m$ edges and $c$ components satisfies $m = n - c$.

*Proof.* Induct on $m$. If $m = 0$ then $c = n$ and both sides are zero. Otherwise choose an edge $e = uv$. Since the graph is acyclic, $e$ is the unique path in it from $u$ to $v$: a second path together with $e$ would form a cycle. Removing $e$ therefore separates $u$ from $v$ and leaves every other pair of vertices joined as before, so the graph with $e$ removed has $n$ vertices, $m-1$ edges and $c+1$ components, and is still acyclic. By induction $m - 1 = n - (c+1)$, so $m = n-c$. $\square$

**Corollary.** A tree on $n$ vertices has exactly $n-1$ edges.

### The Graph Distance

**Definition.** Let $\Gamma$ be connected. The **distance** between $u$ and $v$ is the least length of a path from $u$ to $v$,

$$
d(u,v) = \min\{k : \text{there is a path of length } k \text{ from } u \text{ to } v\},
$$

which exists by connectedness and is attained because the set of admissible lengths is a nonempty subset of the nonnegative integers. For a disconnected graph the distance is defined between vertices in the same component and taken to be $\infty$ between different components.

**Theorem.** On each component of a graph, $d$ is a metric: $d(u,v) \geq 0$ with equality if and only if $u = v$; $d(u,v) = d(v,u)$; and $d(u,w) \leq d(u,v) + d(v,w)$.

*Proof.* The distance is a nonnegative integer, and $d(u,v) = 0$ says there is a path of length zero, which is a path whose only vertex is both $u$ and $v$, so $u = v$. Symmetry is the reversal of paths. For the triangle inequality, concatenate a shortest path from $u$ to $v$ with a shortest path from $v$ to $w$; the result is a walk from $u$ to $w$ of length $d(u,v) + d(v,w)$, and a shortest path is no longer than any walk, so $d(u,w) \leq d(u,v) + d(v,w)$. $\square$

**Remark.** This is the distance of *Metric, Uniform and Complete Spaces* applied to the graph, and it is the sense in which a graph is a metric space. A vertex and the graph are the only objects of the article; the metric language is inherited, and nothing topological beyond the metric — no compactness, no continuity of an invariant — is used in what follows.

**Definition.** Let $\Gamma$ be a finite connected graph. The **eccentricity** of $v$ is $\operatorname{ecc}(v) = \max_{u \in V(\Gamma)} d(v,u)$; the **diameter** is the greatest distance,

$$
\operatorname{diam}\Gamma = \max_{u,v \in V(\Gamma)} d(u,v) = \max_{v} \operatorname{ecc}(v),
$$

and the **radius** is the least eccentricity, $\operatorname{rad}\Gamma = \min_v \operatorname{ecc}(v)$. A **centre** of $\Gamma$ is a vertex attaining the radius, and a finite connected graph has one because its finite set of eccentricities has a minimum. For an infinite connected graph the two maxima become suprema, which may be infinite, and no centre need exist: on the integer line of the growth example below every eccentricity is infinite. The **diameter of a disconnected graph** is infinite if one insists on a single value for all pairs, and is defined componentwise otherwise.

**Proposition.** For every finite connected graph, $\operatorname{rad}\Gamma \leq \operatorname{diam}\Gamma \leq 2\operatorname{rad}\Gamma$.

*Proof.* The first inequality is immediate from the definitions. For the second, let $z$ be a centre and let $u, v$ be vertices with $d(u,v) = \operatorname{diam}\Gamma$. Two applications of the triangle inequality through $z$ give

$$
\operatorname{diam}\Gamma = d(u,v) \leq d(u,z) + d(z,v) \leq 2 \operatorname{ecc}(z) = 2\operatorname{rad}\Gamma. \qquad \square
$$

**Proposition.** A connected graph is finite if and only if it is locally finite and of finite diameter.

*Proof.* A finite graph is locally finite and of finite diameter. Conversely let $\Gamma$ be connected, locally finite and of finite diameter $D$, and fix a vertex $v$. By induction on $r$ the set of vertices at distance at most $r$ from $v$ is finite: for $r = 0$ it is $\{v\}$, and at each step it is enlarged by the neighbour sets of its finitely many vertices, each of them finite by local finiteness. The set of vertices at distance at most $D$ is therefore finite, and it is all of $V(\Gamma)$ because no distance exceeds $D$. $\square$

**Example.** $\operatorname{diam} K_n = 1$ for $n \geq 2$, $\operatorname{diam} P_n = n-1$, $\operatorname{diam} C_n = \lfloor n/2 \rfloor$, $\operatorname{diam} K_{1,1} = 1$, and $\operatorname{diam} K_{m,n} = 2$ for $m+n \geq 3$. In the cycle, a vertex has exactly one vertex at distance $\lfloor n/2\rfloor$ from it when $n$ is even and exactly two when $n$ is odd.

### Geodesics and the Geodesic Property

**Definition.** A **geodesic** from $u$ to $v$ is a path of length $d(u,v)$; a metric space is **geodesic** if every two of its points are joined by a geodesic. A shortest path, rather than any path, is a geodesic, and a graph can have several geodesics between the same pair.

**Proposition.** A connected graph, with its distance, is a geodesic metric space.

*Proof.* Let $u \neq v$ and let $k = d(u,v)$. By the definition of the distance as a minimum over a nonempty set of path lengths, there is a path of length $k$ from $u$ to $v$, and this path is a geodesic by definition. $\square$

**Definition.** A graph is **geodesic** if it is connected and every pair of vertices is joined by a geodesic; by the proposition every connected graph is geodesic. The metric space of a Cayley graph, constructed in *Topology on Groups*, is read through this property, and the choice of the geodesic is what carries the information there.

**Remark (uniqueness).** A geodesic between two vertices of a graph need not be unique, and the failure of uniqueness is measured by the number of shortest paths. In the cycle $C_n$ two distinct vertices at distance $k$ with $2k < n$ are joined by exactly two geodesics, one in each direction; in the complete graph $K_n$ with $n \geq 3$ the two ends of an edge are joined by a unique geodesic, while a non-adjacent pair is joined by one geodesic of length two through each of the $n-2$ remaining vertices.

## Trees and Forests

### Definitions

**Definition.** A **forest** is an acyclic graph, and a **tree** is a connected forest. A **leaf** of a tree is a vertex of degree one, and a tree is **trivial** if it has one vertex and no edges. A **spanning tree** of a connected graph $\Gamma$ is a spanning subgraph that is a tree. The components of a forest are trees.

**Proposition.** Every tree with at least two vertices has at least two leaves.

*Proof.* Let $P = v_0, \ldots, v_k$ be a longest path in the tree, so that all its vertices are distinct. Then $v_0$ has no neighbour outside $P$ by maximality of the length, and its only neighbour in $P$ is $v_1$ by distinctness, so $\deg v_0 = 1$; the same argument applies to $v_k$. $\square$

### Characterisations of a Tree

**Theorem.** Let $\Gamma$ be a finite graph with $n \geq 1$ vertices. The following are equivalent:

**(a)** $\Gamma$ is a tree;

**(b)** any two vertices of $\Gamma$ are joined by exactly one path;

**(c)** $\Gamma$ is connected and $|E(\Gamma)| = n-1$;

**(d)** $\Gamma$ is acyclic and $|E(\Gamma)| = n-1$;

**(e)** $\Gamma$ is acyclic, and adding any edge between two non-adjacent vertices creates a cycle;

**(f)** $\Gamma$ is connected, and deleting any edge disconnects it.

*Proof.* (a) $\Rightarrow$ (b): connectedness gives at least one path. Two distinct paths from $u$ to $v$ would contain a cycle: traversing the first path and then the reverse of the second, the first place at which the two paths separate and the next place at which they meet bound a closed walk with distinct interior vertices, hence a cycle. This contradicts acyclicity.

(b) $\Rightarrow$ (c): $\Gamma$ is connected by hypothesis, and (b) implies acyclicity, since two distinct paths between the same pair of vertices would contradict the uniqueness. Hence $\Gamma$ is a tree. Induct on $n$; the case $n = 1$ is immediate. For $n \geq 2$ the tree has a leaf $x$ by the proposition above. The graph $\Gamma - x$ satisfies (b): a path in $\Gamma$ between two vertices of $\Gamma - x$ cannot pass through $x$, since $x$ has degree one and a path entering $x$ along its only incident edge could not leave. Hence by induction $|E(\Gamma-x)| = (n-1)-1 = n-2$, and $|E(\Gamma)| = n-1$ because $x$ has exactly one incident edge.

(c) $\Rightarrow$ (d): it suffices to show acyclicity. If $\Gamma$ contained a cycle, deleting an edge of that cycle would leave a connected spanning subgraph with $n-2$ edges, contradicting the edge lower bound of a connected graph on $n$ vertices. Hence $\Gamma$ is acyclic.

(d) $\Rightarrow$ (e): the edge count of a forest gives $n - c(\Gamma) = |E(\Gamma)| = n-1$, so $c(\Gamma) = 1$ and $\Gamma$ is connected; by (a) $\Rightarrow$ (b) any two vertices are joined by a unique path. Now let $u$ and $v$ be non-adjacent; they lie in the one component, so a path joins them, and that path together with the added edge $uv$ is a cycle.

(e) $\Rightarrow$ (f): first, $\Gamma$ is connected: if $u$ and $v$ lay in different components, the edge $uv$ could be added between two non-adjacent vertices and would create no cycle, since no path joins $u$ to $v$. So $\Gamma$ is acyclic and connected, hence a tree, and deleting an edge of a tree disconnects it: the edge is the unique path between its ends, and any path in $\Gamma - e$ between them would be a second such path, hence would close a cycle in $\Gamma$.

(f) $\Rightarrow$ (a): the graph is connected, so it remains to show acyclicity. If $\Gamma$ contained a cycle, deleting an edge of that cycle would leave $\Gamma$ connected, since the cycle provides an alternative route between its ends, contradicting (f). $\square$

**Theorem (Cayley).** The number of labelled trees on $n \geq 2$ vertices is $n^{n-2}$.

*Proof sketch.* A **Prüfer sequence** of a labelled tree on $\{1, \ldots, n\}$ is obtained by repeatedly deleting the smallest leaf and recording its unique neighbour, until two vertices remain: this produces a sequence of $n-2$ elements of $\{1,\ldots,n\}$. Conversely, given a sequence $(a_1, \ldots, a_{n-2})$, let $d_i = 1 + |\{j : a_j = i\}|$; the smallest $x$ with $d_x = 1$ is the first vertex deleted, it is joined to $a_1$, and the counts are updated by lowering $d_x$ and $d_{a_1}$; repeating recovers the tree. The two constructions are inverse to one another, so the number of labelled trees on $n$ vertices is the number of sequences of length $n-2$ in an $n$-element set, namely $n^{n-2}$. $\square$

**Remark.** The values of $n^{n-2}$ for $n = 2, 3, 4, 5$ are $1, 3, 16, 125$, and they agree with the direct enumeration of the labelled trees on those few vertices; the number of unlabelled trees on $n$ vertices grows far more slowly and has no comparable closed form.

### Spanning Trees

**Theorem.** Every finite connected graph contains a spanning tree.

*Proof.* Let $\Lambda$ be a spanning subgraph of $\Gamma$ that is connected and has as few edges as possible; such a $\Lambda$ exists because $\Gamma$ itself is a connected spanning subgraph and $\Gamma$ is finite. If $\Lambda$ contained a cycle, deleting an edge of that cycle would keep $\Lambda$ connected, by the same argument as in the characterisation above, contradicting minimality; hence $\Lambda$ is acyclic, and a connected acyclic spanning subgraph is a spanning tree. $\square$

**Corollary.** A connected graph on $n$ vertices has at least $n-1$ edges, with equality exactly for the trees.

**Remark.** The number of spanning trees of a graph is an invariant of considerable interest; for the complete graph $K_n$ it is $n^{n-2}$ by Cayley's theorem, and for a general graph it is given by the matrix-tree theorem, as a determinant of a matrix built from the graph, which belongs to the linear-algebraic layer of Part I and is not used here.

### The Metric Structure of a Tree

**Proposition.** In a tree, the geodesic between two vertices is unique: for any two vertices $u$ and $v$, the path of part (b) of the characterisation theorem is the unique path of length $d(u,v)$.

*Proof.* Part (b) gives uniqueness among all paths, and a geodesic is a path. $\square$

**Proposition (four-point condition for trees).** Let $T$ be a tree with distance $d$. For any four vertices $x_1, x_2, x_3, x_4$, of the three sums

$$
s_{12|34} = d(x_1,x_2)+d(x_3,x_4), \quad
s_{13|24} = d(x_1,x_3)+d(x_2,x_4), \quad
s_{14|23} = d(x_1,x_4)+d(x_2,x_3),
$$

the two largest are equal.

*Proof.* Let $S$ be the minimal subtree spanning $x_1,x_2,x_3,x_4$. If there is a vertex $m$ of $S$ whose removal leaves the four points in four distinct components, put $r_i = d(m,x_i)$; then $m$ lies on the path $x_ix_j$ for every pair, so $d(x_i,x_j) = r_i + r_j$ and all three sums equal $r_1+r_2+r_3+r_4$. Otherwise there is an edge $uv$ of $S$ whose removal separates the four points into two pairs, and after relabelling $x_1,x_2$ lie on the $u$-side and $x_3,x_4$ on the $v$-side. Put $a_i = d(x_i,u)$ for $i = 1,2$, $b_j = d(x_j,v)$ for $j = 3,4$ and $L = d(u,v) \geq 1$; then $d(x_1,x_2) = a_1+a_2$, $d(x_3,x_4) = b_3+b_4$ and $d(x_i,x_j) = a_i + L + b_j$ for $i \leq 2 < j$. Hence

$$
s_{12|34} = a_1+a_2+b_3+b_4, \qquad s_{13|24} = s_{14|23} = a_1+a_2+b_3+b_4+2L,
$$

so the two largest of the three sums are equal. $\square$

**Remark.** The four-point condition characterises, among metrics, those that embed isometrically in a tree. The two cases of the proof are the two shapes of the minimal subtree: a star, where all three sums are equal, and a pair of cherries joined by an edge, where the sum pairing the cherries is strictly the smallest and the other two coincide. The condition is the metric shadow of the acyclicity of the tree, and it is the form in which a tree metric is recognised when only the distances are given.

### Balls, Spheres and Growth

**Definition.** For a vertex $v$ of a connected graph and an integer $r \geq 0$, the **ball** of radius $r$ is $B(v,r) = \{u : d(v,u) \leq r\}$ and the **sphere** is $S(v,r) = \{u : d(v,u) = r\}$, so that $B(v,r)$ is the disjoint union of $S(v,0), \ldots, S(v,r)$. The **growth function** of $\Gamma$ at $v$ is $r \mapsto |B(v,r)|$, and $\Gamma$ has **exponential growth** if there are constants $C > 0$ and $\lambda > 1$ with $|B(v,r)| \geq C\lambda^r$ for all $r$, and **polynomial growth of degree at most $q$** if $|B(v,r)| \leq C r^q$ for all $r$. A locally finite graph has finite balls, so the function is finite-valued.

**Proposition.** Let $T_d$ be the infinite $(d+1)$-regular tree with $d \geq 1$. Then for every vertex $v$, $|S(v,0)| = 1$, $|S(v,1)| = d+1$, and $|S(v,r)| = (d+1)d^{r-1}$ for $r \geq 1$. Consequently $|B(v,r)| = 1 + (d+1)\dfrac{d^r-1}{d-1}$ for $d \geq 2$, and $T_d$ has exponential growth.

*Proof.* In a tree a vertex of $S(v,r)$ with $r \geq 1$ has exactly one neighbour at distance $r-1$ from $v$, namely its predecessor on the unique path to $v$, and the neighbours at distance $r$ of distinct vertices of $S(v,r-1)$ are distinct, since a common successor of two of them would give two paths from that successor to $v$. Hence $S(v,r)$ is in bijection with the set of pairs consisting of a vertex of $S(v,r-1)$ and one of its $d$ neighbours at distance $r$: each vertex of $S(v,r-1)$ has, for $r \geq 2$, exactly one neighbour in $S(v,r-2)$ and $d+1$ neighbours in all, so exactly $d$ of them lie in $S(v,r)$. Summing the geometric series gives the ball count, and it exceeds $d^{r}$ up to a constant, so the growth is exponential. $\square$

**Example (the number systems as graphs).** The integer line $\mathbb{Z}$ with edges $\{i, i+1\}$ is the infinite $2$-regular tree and has $|B(v,r)| = 2r+1$, so it has polynomial growth of degree one. A cycle has bounded balls, since its diameter is finite, and a finite graph has polynomial growth of degree zero: its ball of radius at least the diameter is the whole vertex set. The exponential growth of the regular tree is the property that the group-theoretic articles read on the Cayley graph of a free group, which is that tree; the construction belongs to *Topology on Groups*.

## Bipartite Graphs, Matchings and Colourings

### Bipartite Graphs

**Definition.** A graph $\Gamma$ is **bipartite** if $V(\Gamma)$ admits a partition $V(\Gamma) = X \sqcup Y$ such that every edge has one end in $X$ and the other in $Y$; the pair $(X,Y)$ is a **bipartition**. A bipartite graph with a fixed bipartition is written $\Gamma = (X \sqcup Y, E(\Gamma))$. The graph is **complete bipartite** if every $x \in X$ and $y \in Y$ are adjacent, which is the graph $K_{|X|,|Y|}$ of the standard families.

**Theorem.** A graph is bipartite if and only if it contains no cycle of odd length.

*Proof.* Suppose $(X,Y)$ is a bipartition. Along a closed walk the sides $X$ and $Y$ alternate, so the walk has even length; hence every cycle, being a closed walk, has even length.

Conversely, assume every cycle is even and define a colouring by fixing a vertex $v$ in each component and setting $\chi(u) = d(v,u) \bmod 2$. Adjacent vertices have distances from $v$ differing by at most one. If the colouring failed to be proper there would be an edge $uw$ with $d(v,u)$ and $d(v,w)$ of the same parity; then a geodesic from $v$ to $u$ and a geodesic from $v$ to $w$, followed by the edge $wu$, form a closed walk of length $d(v,u)+d(v,w)+1$, which is odd, and a closed walk of odd length contains a cycle of odd length, since it decomposes into cycles whose lengths sum to its own length. This contradicts the hypothesis; hence the colouring is proper, and the two colour classes form a bipartition. $\square$

**Corollary.** Every forest is bipartite, and every tree is bipartite.

### Matchings and Hall's Theorem

**Definition.** A **matching** in $\Gamma$ is a set of pairwise disjoint edges, that is, a set $\mathcal{M} \subseteq E(\Gamma)$ no two of whose members share an end. A matching is **maximum** if it has the greatest possible size, **saturates** a set $Z \subseteq V(\Gamma)$ when every vertex of $Z$ is an end of a member of $\mathcal{M}$, and **perfect** if it saturates $V(\Gamma)$. In a bipartite graph $\Gamma = (X \sqcup Y, E(\Gamma))$ and a set $S \subseteq X$, the **neighbourhood** is $N(S) = \{y \in Y : xy \in E(\Gamma) \text{ for some } x \in S\}$.

**Theorem (Hall).** Let $\Gamma = (X \sqcup Y, E(\Gamma))$ be a finite bipartite graph. There is a matching saturating $X$ if and only if $|N(S)| \geq |S|$ for every $S \subseteq X$.

*Proof.* If a matching saturating $X$ exists, its edges inject $S$ into $N(S)$ for every $S \subseteq X$, so $|N(S)| \geq |S|$.

For the converse, argue by induction on $|X|$, the case $X = \emptyset$ being vacuous. If some nonempty proper $S \subsetneq X$ satisfies $|N(S)| = |S|$, then $\Gamma[S \cup N(S)]$ has a matching saturating $S$ by induction, and the remaining graph on $(X \setminus S) \cup (Y \setminus N(S))$ satisfies Hall's condition: if $T \subseteq X \setminus S$ had $|N(T)| < |T|$, then $N(S \cup T) \subseteq N(S) \cup N(T)$ and $|N(S \cup T)| \leq |S| + |N(T)| < |S| + |T| = |S \cup T|$, a violation on $S \cup T$. Induction applies to both parts, and their matchings combine. If no such $S$ exists, then $|N(S)| > |S|$ for every nonempty proper $S$. Choose $a \in X$ and $b \in N(\{a\})$, and remove $a$ and $b$; Hall's condition persists on $X \setminus \{a\}$: for $T \subseteq X \setminus \{a\}$, the set $T$ is a proper subset of $X$, so $|N_\Gamma(T)| > |T|$ and hence $|N_{\Gamma-\{a,b\}}(T)| \geq |N_\Gamma(T)| - 1 \geq |T|$. Induction gives a matching saturating $X \setminus \{a\}$ in the smaller graph, and adjoining the edge $ab$ saturates $X$. $\square$

**Corollary.** Every $d$-regular bipartite graph with $d \geq 1$ has a perfect matching.

*Proof.* For $S \subseteq X$, count the edges between $S$ and $N(S)$: there are $d|S|$ of them, and each vertex of $N(S)$ is incident with at most $d$ of them, so $d|S| \leq d|N(S)|$ and $|N(S)| \geq |S|$. Hall gives a matching saturating $X$, and the same argument with the roles of $X$ and $Y$ exchanged gives one saturating $Y$; $d$-regularity forces $d|X| = |E(\Gamma)| = d|Y|$, so $|X| = |Y|$ and a matching saturating $X$ is perfect. $\square$

**Example.** In the complete bipartite graph $K_{m,n}$ every nonempty subset of the $m$-side has the whole $n$-side as its neighbourhood, so Hall's condition holds exactly when $m \leq n$ and the matching is an injection; in the cycle $C_{2k}$ the two sides alternate along the cycle, and a subset of one side that is a union of consecutive blocks has a neighbourhood one vertex larger.

### Colourings

**Definition.** A **proper $k$-colouring** of $\Gamma$ is a map $\chi : V(\Gamma) \to \{1, \ldots, k\}$ with $\chi(u) \neq \chi(v)$ whenever $u \sim v$; the **chromatic number** $\chi(\Gamma)$ is the least $k$ for which a proper $k$-colouring exists, and $\Gamma$ is **$k$-colourable** if $\chi(\Gamma) \leq k$. A bipartite graph is exactly a graph with $\chi(\Gamma) \leq 2$, by the theorem above.

**Proposition.** For every finite graph, $\chi(\Gamma) \leq \Delta(\Gamma) + 1$.

*Proof.* Colour the vertices one at a time in any order. A vertex has at most $\Delta(\Gamma)$ neighbours, so among $\Delta(\Gamma)+1$ colours at least one is unused by its already coloured neighbours; assign it that colour. Every edge is properly coloured when its second end is assigned, and so at the end. $\square$

**Theorem (König's edge-colouring theorem).** Every finite bipartite graph has a proper edge colouring with $\Delta(\Gamma)$ colours, where edges with a common end receive distinct colours.

*Proof sketch.* Decompose a $d$-regular bipartite graph into $d$ perfect matchings by iterating the corollary above, and reduce a general bipartite graph to a regular one by adjoining a suitable number of vertices and edges; each perfect matching is one colour class, so $\Delta(\Gamma)$ colours suffice, and the lower bound is $\Delta(\Gamma)$ because the edges at a vertex of maximum degree are pairwise adjacent. $\square$

**Remark.** The two fundamental bounds are sharp in the expected places: $\chi(K_n) = n = \Delta(K_n)+1$ attains the greedy bound, and for a cycle $\chi(C_n) = 2$ for even $n$ and $3$ for odd $n$, so the greedy bound is far from sharp there. The refinement of the greedy bound for connected graphs — Brooks' theorem, that $\chi(\Gamma) \leq \Delta(\Gamma)$ unless $\Gamma$ is complete or an odd cycle — is standard and is quoted here rather than proved.

## Graphs with Additional Structure

### Cayley Graphs

**Definition (stated for the record; constructed in *Topology on Groups*, below).** Let $G$ be a group and $S \subseteq G$ a generating set with $S = S^{-1}$ and $1 \notin S$. The **Cayley graph** $\operatorname{Cay}(G,S)$ has vertex set $G$ and an edge joining $g$ and $gs$ for every $g \in G$ and $s \in S$. Its graph distance from $1$ to $g$ is the **word metric** with respect to $S$, namely the least length of an expression of $g$ as a word in the elements of $S$, and its growth function at $1$ is the growth of $G$ with respect to $S$. The construction and the metric it carries belong and to the group-theoretic articles of *Topology on Groups*, both, where a group acts on the graph; only the graph and its distance, as defined here, are used there.

**Example.** The Cayley graph of $\mathbb{Z}$ with $S = \{\pm 1\}$ is the integer line of the growth example, and the Cayley graph of the free group $F_d$ on $d$ generators with respect to the symmetric generating set is the infinite $2d$-regular tree $T_{2d-1}$. This is the point at which the combinatorial material of this article is consumed by the group-theoretic articles, and it is the reason the graph distance is defined here rather than there.

### The Dynkin Diagrams as Graphs

The classification of *Root Systems and Classification* attaches to an irreducible reduced root system a **Dynkin diagram**: the graph whose vertices are the simple roots, with $a_{ij}a_{ji}$ edges between the vertices $i$ and $j$ and an arrow on a double or triple edge from the longer root to the shorter one. The diagram is defined there as a graph, and the graph-theoretic reading of it is useful here.

**Proposition.** The underlying graph of a connected Dynkin diagram of finite type is a tree, hence bipartite; it has at most one double or triple edge, and removing the arrow and suppressing multiple edges makes it simply laced, that is, a graph all of whose edges are single.

*Proof.* The diagram is connected and finite. The constraints on a connected diagram of finite type — no cycles, no vertex of degree at least four, and a subdiagram argument for multiple edges — are exactly the exclusions proved in the classification of *Root Systems and Classification*, and they say that the underlying graph is a tree. A tree is bipartite by the corollary above. The second claim is the corresponding constraint on the number of double and triple edges, also part of the same classification; on contracting the multiple edges to single ones the result is a graph with the same connected tree structure and no multiple edges. $\square$

**Example.** The diagram $A_n$ is the path $P_n$, the diagram $D_n$ is the tree obtained from $P_{n-2}$ by attaching two leaves at an end, and the exceptional diagrams $E_6, E_7, E_8$ are the trees drawn in *Root Systems and Classification*. The diagrams $B_n$, $C_n$ and $F_4$ carry a double edge and $G_2$ a triple edge, so they are not simply laced; the simply-laced types are exactly $A_n, D_n, E_6, E_7, E_8$. The affine Dynkin diagrams, whose underlying graphs may contain a cycle and are the Coxeter diagrams of the affine Coxeter groups, are treated in *Coxeter Groups*, where the Coxeter matrix is the defining datum.

**Remark.** The Dynkin diagram is the graph-theoretic shadow of the root system: its connectedness is the irreducibility of the root system, its bipartite colouring is the parity of the roots' expression in the simple roots, and its automorphism group is the group of diagram automorphisms appearing in the classification of the finite simple groups of Lie type of *Finite Simple Groups of Lie Type*. No algebra is used here beyond what the citation of *Root Systems and Classification* supplies; the graph-theoretic facts used are the proposition above and the characterisation of trees.

## Summary

A graph is a set with a symmetric irreflexive relation, and a morphism is a map preserving the relation; subgraphs are obtained by deletion, induced subgraphs by deleting vertices only. The degree sequence obeys the handshake lemma $\sum_v \deg v = 2|E(\Gamma)|$, and the relation "joined by a walk" is an equivalence relation whose classes are the components. In a connected graph the least path length is a metric, the graph distance $d(u,v)$; it makes the graph a geodesic metric space and gives the eccentricity, the diameter, the radius and the centre, with $\operatorname{rad}\Gamma \leq \operatorname{diam}\Gamma \leq 2\operatorname{rad}\Gamma$. A tree is a connected acyclic graph, characterised equivalently by uniqueness of paths, by connectivity together with $|E(\Gamma)| = |V(\Gamma)|-1$, by acyclicity together with $|E(\Gamma)| = |V(\Gamma)|-1$, and by the extremality properties of adding and deleting edges; every finite connected graph has a spanning tree, and the labelled trees on $n$ vertices number $n^{n-2}$. In a tree the geodesic is unique and the tree metric satisfies the four-point condition. Balls and spheres define the growth function, linear on $\mathbb{Z}$ and exponential on the regular tree. Bipartite graphs are exactly the graphs without an odd cycle; matchings are governed by Hall's theorem and, in the regular bipartite case, by the existence of perfect matchings; colourings begin with the greedy bound $\chi(\Gamma) \leq \Delta(\Gamma)+1$. The graph distance is the structure that *Topology on Groups* attaches to a group through the Cayley graph, and the Dynkin diagrams of *Root Systems and Classification* are read here as trees.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Gamma$ | A graph, with vertex set $V(\Gamma)$ and edge set $E(\Gamma)$ |
| $n = |V(\Gamma)|$, $m = |E(\Gamma)|$ | Order and size of $\Gamma$ |
| $u \sim v$, $uv$ | Adjacency of $u$ and $v$, and the edge between them |
| $D = (U,A)$ | Directed graph, with vertex set $U$ and arc set $A$ |
| $\Gamma[W]$ | Induced subgraph on $W \subseteq V(\Gamma)$ |
| $\deg v$, $\Delta(\Gamma)$, $\delta(\Gamma)$ | Degree, maximum degree, minimum degree |
| $K_n$, $P_n$, $C_n$, $\overline{K_n}$, $K_{m,n}$ | Complete, path, cycle, empty and complete bipartite graphs |
| $c(\Gamma)$ | Number of connected components |
| $d(u,v)$ | Graph distance: fewest edges on a path from $u$ to $v$ |
| $\operatorname{ecc}(v)$, $\operatorname{diam}\Gamma$, $\operatorname{rad}\Gamma$ | Eccentricity, diameter, radius |
| $\operatorname{gir}\Gamma$ | Girth: least length of a cycle, $\infty$ if acyclic |
| $B(v,r)$, $S(v,r)$ | Ball and sphere of radius $r$ about $v$ |
| $T_d$ | The infinite $(d+1)$-regular tree |
| $(X,Y)$, $N(S)$ | The two sides of a bipartition; neighbourhood of $S$ |
| $\mathcal{M}$ | A matching: a set of pairwise disjoint edges |
| $\chi(\Gamma)$ | Chromatic number |
| $\operatorname{Aut}(\Gamma)$ | Automorphism group of $\Gamma$ |
| $\operatorname{Cay}(G,S)$ | Cayley graph of a group $G$; constructed in *Topology on Groups*, below |





## Further Reading

- Béla Bollobás, *Modern Graph Theory* (Springer, 1998), for connectivity, trees, matchings, colourings and the growth of graphs.
- Reinhard Diestel, *Graph Theory* (5th edition, Springer, 2017), for the characterisations of trees, Hall's theorem and the combinatorial treatment of connectivity.
- John Adrian Bondy and U. S. R. Murty, *Graph Theory* (Springer, 2008), for spanning trees, Prüfer sequences and Cayley's formula.
- Frank Harary, *Graph Theory* (Addison-Wesley, 1969), for the standard families, the diameter and radius relations and the centre of a graph.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras, Chapters 4–6* (Springer, 2002), for the Dynkin diagram as a graph and the constraints on its shape.
