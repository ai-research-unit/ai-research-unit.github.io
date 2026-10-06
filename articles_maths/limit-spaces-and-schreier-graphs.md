# __Limit Spaces and Schreier Graphs__

## Introduction

A group acting on a regular rooted tree acts on every level, and the action on the level $n$ is recorded by a finite graph: the vertices are the $d^n$ words of length $n$, the edges join a word to its images under the generators, and the labels are the generators. These are the **Schreier graphs** of the action. They are not independent of one another: the projection that deletes the last letter of a word is equivariant, so it is a morphism of labelled graphs $\Gamma_{n+1} \to \Gamma_n$, and the sequence of finite graphs forms an **inverse spectrum**. The graph of the action on the boundary $X^{\omega}$ is the inverse limit of the spectrum, and the graph of the orbit of a boundary point is the limit of the pointed finite graphs in the local topology. The self-similarity of the group is thus the self-similarity of a family of finite graphs, and the wreath recursion of *Self-Similar Groups* becomes a **graph substitution**, one finite graph replacing another.

The second object of the article is the **limit space**. For a contracting action, the space $X^{-\omega}$ of sequences infinite to the left carries the **asymptotic equivalence**: two sequences are equivalent when they differ by the action of finitely many group elements, one at each depth, and the quotient is a compact metrisable space $\mathcal{J}_G$, finite-dimensional and, in the level-transitive case, connected. The limit space is built from **tiles** $T_v$, the images of the cylinders, which form a self-similar cover of $\mathcal{J}_G$ and a Markov partition for the map induced by the shift; the tiles of level $n$ meet exactly when the corresponding words are related by an element of the nucleus of *Automaton and Contracting Groups*, so the graph whose vertices are the tiles of level $n$ is a Schreier graph of the nucleus. The limit space is at once the limit of those finite graphs and the Gromov boundary of the **self-similarity complex**, a hyperbolic graph built from the Schreier graphs of the levels. It is the space that a self-similar group produces, and the standard examples are a circle, a segment, a dendrite and the Sierpiński gasket.

The article assumes *Self-Similar Groups* for the tree, its boundary, the sections, the wreath recursion, the level-transitive and recurrent actions and the standard examples; *Automaton and Contracting Groups*, written before it, for the automata, the contracting actions and the nucleus; *Graph Theory* for graphs, labelled graphs and their limits; *Combinatorial Group Theory* for the Schreier graph of a subgroup, which is extended here to the action on a level of the tree; *Topological Spaces* for the quotient topology, the Cantor space and compactness; and *Dimension Theory* for the covering dimension and the idea that dimension is bounded by a rank. The hyperbolicity of the self-similarity complex and its boundary at infinity are those of *Hyperbolic Groups*, and the covering dimension of the limit space is measured by *Dimension Theory*.

The boundaries are these. The convergence of the finite graphs to the limit space in the **Gromov–Hausdorff metric** and the **asymptotic dimension** of the orbital graphs are named but not used: their metric definition belongs to *Metric Geometry* in Part IV, and the present article keeps to the homeomorphism statements that need only the topology. The **spectra** of the Schreier graphs, the eigenvalues of the graph Laplacians and their limits, the invariant measures on the boundary and the groupoid and operator algebra of the action are Part III's, where the Hilbert space and the measure are available; the article says which sequence of operators is meant and stops. The **Julia sets** appear as limit spaces of the iterated monodromy groups, but the complex dynamics that produces them is Part III's, and the **fractal dimension** of the limit space is Part IV's, where the Hausdorff dimension is defined. No physics is invoked.

## Schreier Graphs of a Self-Similar Action

### Graphs and Schreier Graphs

A **Schreier graph** records a group action on a set. Let $G$ be a group with a symmetric generating set $S$, and let $M$ be a set on which $G$ acts on the left. The **Schreier graph** $\Gamma(G,S,M)$ is the graph with vertex set $M$ and with an edge labelled $s$ joining $m$ to $sm$ for every $m \in M$ and $s \in S$; it is a labelled graph in the sense of *Graph Theory*, with the labels in $S$ and with the convention that an edge and its inverse carry inverse labels. The connected components of $\Gamma(G,S,M)$ are exactly the orbits of $G$ on $M$, the graph $\Gamma(G,S,x)$ of the orbit of a point $x$ is the **orbit Schreier graph** at $x$, and for the action of $G$ on itself by left multiplication the graph is the **Cayley graph**. When $G$ acts transitively and $H$ is the stabiliser of a point, the Schreier graph $\Gamma(G,S,M)$ is the graph of the cosets $H\backslash G$ with the edges $Hg \to Hgs$, the coset graph that occurs in the Nielsen–Schreier theorem of *Combinatorial Group Theory*. The general Schreier graph here is that of an action, which is the form the theory of this article needs; the coset graph is the special case of a transitive action.

**Example (the Schreier graph of a subgroup).** The definition specialises to the one of *Combinatorial Group Theory*: for $H \leq G = \langle S\rangle$, the action of $G$ on the right cosets by right multiplication has the coset graph for its Schreier graph, and the subgroup $H$ is the fundamental group of that graph. The reader should keep the two pictures in mind, the algebraic coset graph of that article and the graph of a self-similar action below, since they share the definition and nothing else.

### The Schreier Graphs of the Levels

Let $G$ be a self-similar group generated by the finite symmetric set $S$, acting on the regular tree $\mathcal{T}(X)$. The levels $X^n$ are invariant under $G$, so the action defines, for each $n$, the finite labelled graph

$$
\Gamma_n(G,S) = \Gamma(G,S,X^n),
$$

whose vertex set is $X^n$ and whose edges are the pairs $v \to sv$, $s \in S$.

**Theorem (the inverse spectrum).** For each $n \geq 1$ the map

$$
\pi_n : \Gamma_{n+1}(G,S) \to \Gamma_n(G,S), \qquad \pi_n(x_1\cdots x_nx_{n+1}) = x_1\cdots x_n
$$

is a surjective morphism of labelled graphs. The labelled Schreier graph of the action on the whole tree is the disjoint union of the graphs $\Gamma_n(G,S)$ over $n$, and the labelled Schreier graph of the action on the boundary is their inverse limit

$$
\Gamma(G,S,X^{\omega}) = \varprojlim_n \Gamma_n(G,S).
$$

**Proof.** The projection deletes the last letter and commutes with the action, because an automorphism of the tree carries a word $x_1x_2\cdots x_{n+1}$ to a word of the same length whose prefix is the image of $x_1\cdots x_n$: the recursion $g(x_1\cdots x_nx_{n+1}) = g(x_1\cdots x_n)\,g|_{x_1\cdots x_n}(x_{n+1})$ exhibits the projection as equivariant. An edge $v \to sv$ of $\Gamma_{n+1}$ is carried to the edge $\pi_n(v) \to s\pi_n(v)$ of $\Gamma_n$, and every vertex and every edge of $\Gamma_n$ is the image of one of $\Gamma_{n+1}$, because a word of length $n$ has children and the projection is onto. The graph on $X^*$ is the disjoint union by the invariance of the levels, and the graph on $X^{\omega}$ is the inverse limit of the labelled graphs because the cylinder $[x_1\cdots x_n]$ is the inverse image of the vertex $x_1\cdots x_n$ and the action is continuous. $\square$

The inverse limit of finite labelled graphs is a **profinite graph**, and the theorem is the graph-theoretic form of the wreath recursion: the recursion at each vertex is the statement that the fibre of the projection over a vertex splits into the $d$ subtrees of its children, and the labelled edges of the finer graph record the sections.

**Example (the substitution of the levels).** For the Grigorchuk group the passage from $\Gamma_{n-1}(G,S)$ to $\Gamma_n(G,S)$ is a graph substitution that can be read off the recursion: the labels $b,c,d$ are renamed cyclically, and every edge labelled $a$ is replaced by a fixed small graph, so that the family of finite graphs reproduces itself level after level. The Schreier graphs of the levels are thus determined by a single substitution rule, and the whole family is obtained from the labelled graph of the first level by iterating it. The same phenomenon holds for every self-similar group: the wreath recursion is the substitution, and the substitution is the reason the graphs are self-similar.

### The Local Topology and the Orbit Schreier Graphs

The finite graphs $\Gamma_n(G,S)$ do not converge to the boundary graph $\Gamma(G,S,X^{\omega})$ as graphs, since their vertex sets are disjoint; what converges is the orbit of a point, as a pointed graph.

**Definition (the local topology).** On the set of isomorphism classes of **pointed graphs** $(\Gamma,v)$, with $\Gamma$ a locally finite labelled graph and $v$ a vertex, the **local topology** is the topology of the metric

$$
d\bigl((\Gamma_1,v_1),(\Gamma_2,v_2)\bigr) = 2^{-R},
$$

where $R$ is the largest integer for which the ball of radius $R$ about $v_1$ in $\Gamma_1$ and the ball of radius $R$ about $v_2$ in $\Gamma_2$ are isomorphic by a labelled isomorphism carrying $v_1$ to $v_2$, with the convention that $d = 1$ when the balls of radius $0$ are not isomorphic. The space of pointed graphs is compact when the graphs have uniformly bounded degree, which the Schreier graphs do.

**Theorem (the orbit graph is a limit).** Let $G$ be finitely generated and act on the tree by automorphisms, let $\xi = x_1x_2x_3\cdots \in X^{\omega}$, and write $\xi_n = x_1\cdots x_n$. Then the pointed orbit Schreier graph $(\Gamma(G,S,\xi),\xi)$ is the limit, in the local topology, of the pointed finite graphs $(\Gamma_n(G,S),\xi_n)$.

**Proof sketch.** The ball of radius $R$ about $\xi$ in the orbit graph is determined by the finitely many images $g\xi$ of the elements $g$ of the Cayley ball of radius $R$, together with the pairs of them that a generator joins. Two elements $g,h$ of the Cayley ball with $|g|,|h| \leq R$ give the same image at level $n$ exactly when $h^{-1}g$ fixes the prefix $\xi_n$, and the finitely many nontrivial elements of the Cayley ball of radius $2R$ each act nontrivially at some level, so there is $N(R)$ beyond which the action on the prefix $\xi_n$ separates all of them. For $n \geq N(R)$ the ball of radius $R$ about $\xi$ in $\Gamma(G,S,\xi)$ and the ball of radius $R$ about $\xi_n$ in $\Gamma_n(G,S)$ are therefore isomorphic, and the radius of agreement tends to infinity with $n$. $\square$

**Corollary.** The orbit of a boundary point is a limit of the orbits of the finite words, and the structure of the orbit graph is the limit of the structures of the finite Schreier graphs. In particular the questions about the orbit graph reduce to questions about the finite graphs of the spectrum, which is the reason the family of Schreier graphs is the computable side of the theory.

**Remark.** The proof uses that the generators of a self-similar group carry a word of length $n$ to a word of length $n$, so the ball of radius $R$ about $\xi_n$ stabilises in the spectrum. For an arbitrary group acting on a tree this is false; it is the self-similar hypothesis that makes the levels a spectrum rather than an arbitrary family.

### Graph Contractions and Self-Similar Graphs

**Definition (graph contraction).** A **graph contraction** from a graph $\Gamma = (V,E)$ to a graph $\Gamma' = (V',E')$ is a pair of maps $f_V: V \to V'$ and $f_E: E \to E' \cup \{\eth\}$ such that every edge $e$ with $f_E(e) \neq \eth$ maps to an edge whose endpoints are the $f_V$-images of the endpoints of $e$, and $f_E$ is a bijection from $f_E^{-1}(E')$ to $E'$. In words: some edges are deleted, the others map bijectively onto the edges of the target. A graph is **self-similar** if it is infinite, it admits a graph contraction to itself, and it is the union of the inverse images of a finite set of vertices under the iterates of the contraction.

**Theorem.** Let $G$ be a self-similar group generated by a finite set $S$ such that the sections $s|_x$ of the generators lie in $S$. Then for every $n$ the shift $x_1\cdots x_n \mapsto x_1\cdots x_{n-1}$ extends to a graph contraction of $\Gamma_n(G,S)$ onto $\Gamma_{n-1}(G,S)$.

**Proof sketch.** The shift carries the $d$ subtrees attached to a vertex to that vertex; an edge of $\Gamma_n$ that joins a word in the subtree at $v$ to a word in another subtree is deleted, an edge that stays inside the subtree at $v$ is carried to the edge of $\Gamma_{n-1}$ obtained by applying the sections $s|_x$, and the hypothesis that the sections of the generators lie in $S$ makes the target a well-defined edge. The edges that stay are exactly the edges over the edges of the coarser graph, so the restriction of $f_E$ is a bijection. $\square$

The hypothesis that $S$ is closed under sections is satisfied by the nucleus of a contracting action, and the theorem is the reason the graphs of a contracting action form a self-similar family: the contraction of the graph is the graph-theoretic shadow of the contraction of the group.

**Remark (the growth of the orbit graphs).** The orbit Schreier graphs carry the growth of the action: the number of vertices of $\Gamma_n$ is $d^n$, and the size of the ball of radius $R$ in the orbit graph is the growth of the orbit of a point under the action. The growth of a finitely generated group and of its orbits, the number of ends and the large-scale geometry of the graphs are the subject of *Geometric Group Theory*; what is added here is that the orbit graphs of a self-similar group come with the substitution above, so their growth can be computed from the substitution, and the orbit graphs of the Grigorchuk group are the standard example of intermediate growth. The spectrum of the adjacency operator of the graphs, and its limit for a sequence of levels, is an object of Part III and is not computed here.

## The Limit Space

### The Asymptotic Equivalence

Let the self-similar action of $G$ on $\mathcal{T}(X)$ be contracting, with nucleus $N$, as in *Automaton and Contracting Groups*. The **space of sequences infinite to the left** is

$$
X^{-\omega} = \{\cdots x_3x_2x_1 : x_i \in X\},
$$

with the product topology; it is again a Cantor space, and the shift $s(\cdots x_3x_2x_1) = \cdots x_4x_3x_2$ is a covering-like map, every point having exactly $d$ preimages.

**Definition (asymptotic equivalence).** Two sequences $\cdots x_3x_2x_1$ and $\cdots y_3y_2y_1$ in $X^{-\omega}$ are **asymptotically equivalent** with respect to the action of $G$ if there is a finite set $K \subset G$ and a sequence $g_k \in K$, $k \geq 1$, such that

$$
g_k(x_kx_{k-1}\cdots x_1) = y_ky_{k-1}\cdots y_1 \qquad \text{for every } k \geq 1 .
$$

**Proposition.** Asymptotic equivalence is an equivalence relation, and it is closed as a subset of $X^{-\omega} \times X^{-\omega}$. The relation and the quotient depend on the action and not on the choice of the finite set $K$.

**Proof sketch.** The relation is reflexive, symmetric and transitive because the products of finitely many elements of $K$ lie in a finite set depending on $K$; closedness follows from the compactness of $X^{-\omega} \times X^{-\omega}$ together with the finiteness of the choices. $\square$

**Theorem (the nucleus criterion).** Two sequences $\cdots x_2x_1$ and $\cdots y_2y_1$ are asymptotically equivalent if and only if there is a sequence $h_n$ of elements of the nucleus $N$ such that

$$
h_n(x_n) = y_n, \qquad h_n|_{x_n} = h_{n-1} \qquad \text{for every } n \geq 1
$$

(with $h_0$ arbitrary). Equivalently, the Moore diagram of the nucleus contains a path $\cdots e_2e_1$ in which the edge $e_n$ carries the label $(x_n, y_n)$.

**Proof sketch.** Given the sequence $g_k$ of the definition, the element $g_k$ maps the prefix $x_k\cdots x_1$ to the prefix $y_k\cdots y_1$; the section relation of *Self-Similar Groups* applied at the last letter gives, from $g_k$, a section of $g_k$ at $x_k$ which maps $x_{k-1}\cdots x_1$ to $y_{k-1}\cdots y_1$, and the deep sections of a contracting action lie in the nucleus; iterating gives the sequence $h_n$, and conversely a sequence $h_n$ in the nucleus builds the elements $g_k$ of the definition. The Moore diagram statement is the same equation read as an edge with the label $(\text{input}, \text{output}) = (x_n,y_n)$ from the state $h_n$ to the state $h_{n-1}$. $\square$

**Example (the criterion in the standard groups).** For the adding machine the nucleus is $\{a^{-1},1,a\}$ and the criterion reproduces the dyadic identification: $\cdots1111 \sim \cdots0000$, because the constant sequence $h_n = a$ satisfies $a(1) = 0$ and $a|_1 = a$, and $\cdots0111 \sim \cdots1000$ for the same reason; but $\cdots0001$ is not equivalent to $\cdots0000$, because no element of the nucleus sends $0$ to $1$ and has its section at $0$ equal to the element solving the last place. For the Grigorchuk group the criterion, with the nucleus $\{1,a,b,c,d\}$ of the previous article, gives the equivalence

$$
\cdots 111101 w \sim \cdots 111100 w \qquad (w \in X^*)
$$

and no others: the chain of sections is $a, b, d, c, b, d, c, b, \dots$, which is the cycle $b \to d \to c \to b$ of the nuclear automaton. Both computations were verified on the nucleus tables to a large depth, with the negative cases checked as well.

### The Limit Space and the Shift

**Definition (limit space).** The **limit space** of the contracting self-similar action is the quotient

$$
\mathcal{J}_G = X^{-\omega}/\!\sim
$$

of the space of sequences infinite to the left by the asymptotic equivalence, with the quotient topology.

**Theorem.** The limit space $\mathcal{J}_G$ is a compact metrisable space of covering dimension at most $|N|-1$, and it is connected when the action is level-transitive and $G$ is finitely generated. The shift $s$ of the sequences descends to a surjective continuous map $s: \mathcal{J}_G \to \mathcal{J}_G$ in which every point has at most $d = |X|$ preimages.

**Proof sketch.** The quotient of a compact space by a closed equivalence relation is compact and metrisable, and the asymptotic equivalence is closed by the proposition above; the bound on the number of equivalent points, and hence the bound on the dimension, is the nucleus criterion, each point being determined by the states of the finite nuclear automaton through which its sequences can be read, with the covering dimension of *Dimension Theory* bounded by the rank of the data. Connectivity uses that the level-transitive action moves the cylinders of a level among themselves, so the images of adjacent cylinders meet, and the tiles of a level form a connected finite graph when the group is finitely generated. The statement about the shift is immediate from the shift on $X^{-\omega}$, which is surjective with exactly $d$ preimages. $\square$

The pair $(\mathcal{J}_G, s)$ is the **limit dynamical system** of the action, and the map $s$ is a self-cover: it is a surjective local homeomorphism in the cases from complex dynamics, where $\mathcal{J}_G$ is a Julia set and $s$ is the rational map. The **dynamics** of $s$ — the periodic points, the invariant measures, the topological entropy and the ergodic theory — is the subject of Part III, and this article confines itself to the space and the single map.

**Remark.** The hypothesis of level-transitivity in the connectivity statement is not removable. The trivial group has the one-element nucleus $\{1\}$, is contracting, and has limit space $X^{-\omega}$ itself, a Cantor set and totally disconnected; the connectivity statement is about the level-transitive actions, which are the ones the theory is about.

### Tiles and the Markov Partition

**Definition (tiles).** For a finite word $v \in X^*$ the **tile** $T_v$ is the image in $\mathcal{J}_G$ of the set of sequences infinite to the left that end in $v$, that is, of $X^{-\omega}v = \{\cdots x_2x_1v\}$, under the quotient map.

**Theorem (the tiling).** The tiles have the following properties.

**(a)** $T_{\varnothing} = \mathcal{J}_G$, and $T_v = \bigcup_{x \in X} T_{xv}$, so the tiles of level $n+1$ subdivide the tiles of level $n$.

**(b)** Every tile is compact, every point of $\mathcal{J}_G$ lies in at most $|N|$ tiles of a given level, and each $T_v$ is the image of a tile of the next level under the shift, $s(T_v) = T_{v'}$ for the word $v'$ obtained by deleting the last letter of $v$.

**(c)** $T_u \cap T_v \neq \emptyset$ for $u,v \in X^n$ if and only if there is $h \in N$ with $h(v) = u$.

**Proof sketch.** (a) is the definition and the partition of the sequences by their last letter; (b) is compactness together with the bound on the number of equivalent points of the nucleus criterion; (c) is the criterion itself read at the words $u$ and $v$: a sequence ending in $u$ and a sequence ending in $v$ have the same image exactly when an element of the nucleus carries $v$ to $u$, by the section chain of the criterion. $\square$

The family $\{T_v : v \in X^n\}$ is a finite closed cover of $\mathcal{J}_G$ whose members meet according to the action of the nucleus; such a cover is a **Markov partition** for the map $s$, because $s$ maps each tile onto a tile and the intersections of the images are governed by the finite data of the nucleus. The symbolic dynamics that the Markov partition produces — the subshift of finite type that codes the itineraries of the map, and its entropy — is Part III's, and the tiles are introduced here because they are the topological units of the limit space.

## The Limit Space as a Limit of Graphs and as a Boundary

### The Graphs $J_n$ and the Approximation Theorem

**Definition.** Let $J_n(G)$ be the simplicial graph whose vertices are the tiles $T_v$, $v \in X^n$, two vertices being joined when the tiles meet.

**Corollary.** The map $v \mapsto T_v$ is an isomorphism of simplicial graphs between the Schreier graph $\Gamma(\langle N\rangle, N, X^n)$ of the action of the group generated by the nucleus on the level $n$, with generating set $N$, and the graph $J_n(G)$. If the action is recurrent, then the nucleus generates $G$, and the graphs $J_n(G)$ are the Schreier graphs of the group itself.

**Proof.** The vertices correspond bijectively to the words of length $n$ and, by (c) of the tiling theorem, two vertices are adjacent exactly when an element of $N$ carries one word to the other, which is the edge relation of the Schreier graph of the nucleus acting on $X^n$. The recurrence hypothesis identifies $\langle N\rangle$ with $G$ by the theorem on the nucleus of *Automaton and Contracting Groups*. $\square$

**Theorem (approximation of the limit space).** A compact Hausdorff space $X$ is homeomorphic to the limit space $\mathcal{J}_G$ if and only if there is a family $\{U_v : v \in X^*\}$ of closed subsets of $X$ such that

**(a)** $U_{\varnothing} = X$ and $U_v = \bigcup_{x \in X} U_{xv}$ for every $v$;

**(b)** for every infinite sequence $\cdots x_3x_2x_1$ the intersection $\bigcap_{n} U_{x_nx_{n-1}\cdots x_1}$ is a single point;

**(c)** $U_u \cap U_v$ is nonempty exactly when there is $h \in N$ with $h(v) = u$.

In particular, if for some positive numbers $R_n$ the metric spaces $(J_n(G), d/R_n)$ converge to a metric space $X$ in the Gromov–Hausdorff metric, then $X$ is homeomorphic to $\mathcal{J}_G$. If $X$ is a metric space then condition (b) may be replaced by $\lim_{n\to\infty}\max_{v \in X^n}\operatorname{diam}(U_v) = 0$.

The theorem is Nekrashevych's, and it is the exact sense in which the limit space is a limit of the Schreier graphs: the graphs $J_n(G)$ are the finite approximations, and the limit is taken by rescaling the graph distance so that the diameters shrink. The Gromov–Hausdorff metric in the statement is defined in *Metric Geometry* in Part IV, and the metric form of the theorem is therefore forward-referenced; the topological form, which is the content, needs only the tiles and their intersections. The same theorem justifies the computations of the examples below, where the limit space is identified by producing the tiles.

### The Limit Space as a Gromov Boundary

**Definition (self-similarity complex).** Let $G$ be a finitely generated self-similar group with finite generating set $S$. The **self-similarity complex** $\Sigma(G,S)$ is the $1$-complex with vertex set $X^*$ in which two vertices $v_1, v_2$ are joined by an edge when either $v_i = xv_j$ for a letter $x$, an edge of the first type, or $s(v_i) = v_j$ for a generator $s$, an edge of the second type, the generators acting on the tree as automorphisms. The edges of the first type join consecutive levels and make the complex a tree above the root; the edges of the second type span the disjoint union of the finite Schreier graphs $\Gamma_n(G,S)$.

**Theorem (the limit space is a boundary).** If the action of the finitely generated group $G$ is contracting, then the self-similarity complex $\Sigma(G,S)$ is a Gromov-hyperbolic space, and the limit space is homeomorphic to its boundary at infinity:

$$
\mathcal{J}_G \cong \partial\Sigma(G,S),
$$

by a homeomorphism compatible with the projection $X^{-\omega} \to \mathcal{J}_G$, the boundary point of a sequence being the limit of the sequence of its finite prefixes read as vertices of the complex.

The theorem is Nekrashevych's. Hyperbolicity, the boundary at infinity and its topology are defined and studied in *Hyperbolic Groups*; the statement here is that the limit space, which was built as a quotient of a Cantor space, is also the boundary of a hyperbolic space, and the two descriptions agree. This second description is the source of the dimension theorem below and of the quasi-isometric invariants of the action; it is the analogue for self-similar groups of the boundary of a hyperbolic group, and it is why the limit space of a self-similar group sits in the same family of objects as the visual boundaries of the group theory of *Hyperbolic Groups*.

### The Dimension of the Limit Space

**Theorem (dimension).** Let the action of the finitely generated group $G$ be contracting. The covering dimension of the limit space $\mathcal{J}_G$ equals the asymptotic dimension of its orbital graphs, and equals the dynamical asymptotic dimension of the groupoid of germs of the action. The limit space is one-dimensional if and only if $G$ is the faithful quotient of a contracting self-similar virtually free group. In particular, if the action is by a bounded automaton, in the sense of *Automaton and Contracting Groups*, then the limit space is post-critically finite and one-dimensional.

The first equalities are Nekrashevych's. The covering dimension is that of *Dimension Theory*; the asymptotic dimension of a graph is the coarse invariant defined in *Metric Geometry* in Part IV and is used here only as a name; the groupoid of germs and its dynamical asymptotic dimension are Part III's objects and are named for the completeness of the statement. The final sentence combines the theorem of Bondarenko and Nekrashevych on bounded automata with the dimension theorem, and it explains the shapes of the examples: the segment and the dendrite of the next section are one-dimensional, while the Sierpiński gasket group also has a one-dimensional limit space in the covering dimension, the familiar two-dimensional appearance of the gasket being a statement about a different dimension, the Hausdorff dimension, which is Part IV's.

**Remark.** The dimension is the first invariant of the limit space that is a number, and it is a number the action controls: the covering dimension is bounded by $|N|-1$, it is computed from the nucleus, and it is one for the bounded automata, which are the majority of the classical examples. The Hausdorff dimension of a self-similar space is computed from the contractions of the self-similar set and the open set condition; that computation is *Fractal Geometry*'s, and it is not carried out here.

## Examples of Limit Spaces

### The Adding Machine: the Circle

**Theorem.** The limit space of the adding machine is the circle, and the shift is the two-fold covering $s(x) = 2x \pmod 1$.

**Proof sketch.** The nucleus is $\{a^{-1},1,a\}$ and the criterion of the asymptotic equivalence identifies two sequences when they are equal or are of the form $\cdots 0001x_m\cdots x_1$ and $\cdots 1110x_m\cdots x_1$, which is the usual identification of the two dyadic expansions of a real number in $[0,1]$, $0.x_1x_2\cdots x_m0111\cdots = 0.x_1x_2\cdots x_m1000\cdots$. The quotient is therefore the segment with its two endpoints glued, that is, the circle; the endpoints $\cdots0000$ and $\cdots1111$ are glued because the constant sequence $h_n = a^{-1}$ gives $a^{-1}(0)=1$ and $a^{-1}|_0 = a^{-1}$; and the shift is the doubling map, because deleting the last digit of a dyadic expansion divides the number by two modulo the identification. $\square$

The example is the first and the smallest: the limit space of the odometer is the circle, the shift is the doubling map, and the limit dynamical system is the doubling map on the circle of the dynamical systems of Part III. The orbit Schreier graphs of the adding machine on the levels are the cyclic graphs of length $2^n$, and their limit in the local topology is the orbit graph of a boundary point, which for the circle is an infinite line whose balls grow linearly.

### The Grigorchuk Group: the Segment

**Theorem.** The limit space of the Grigorchuk group is homeomorphic to the real segment $[0,1]$, and the shift is the tent map $s(x) = 1 - |2x-1|$ folding the interval.

**Proof sketch.** The nucleus is $\{1,a,b,c,d\}$ and the criterion gives the equivalence $\cdots 111101w \sim \cdots 111100w$ for $w \in X^*$ and no others; this is the relation of the adding machine transported by the homeomorphism $F$ of $X^{-\omega}$ that sends $\cdots x_3x_2x_1$ to $\cdots y_3y_2y_1$ with $y_i = (1+x_1)+\cdots+(1+x_i) \pmod 2$, except that the two points $\cdots1111$ and $\cdots11110$ are not equivalent while their images are, so that the identification of the endpoints of the circle is undone and the quotient is the segment rather than the circle. The shift on the segment is the folding map, which is the map induced by the shift on the circle under the quotient. $\square$

The limit space of the Grigorchuk group is the object that replaces the Julia set: the group has no complex dynamical model, and the segment, with its tiling by the images of the dyadic intervals and the folding map, is the self-similar space the group produces. The finite Schreier graphs $\Gamma_n$ of the levels, with their substitution, approximate the segment by the theorem of approximation, and the tiles are the dyadic subintervals; the covering dimension is one, as the dimension theorem requires, since the Grigorchuk group is generated by a bounded automaton, and the limit space is post-critically finite.

### The Infinite Dihedral Group: the Segment

**Theorem.** The limit space of the infinite dihedral group of *Self-Similar Groups* is a segment, and the asymptotic equivalence relation is the same as that of the Grigorchuk group.

The group $\mathrm{IMG}(z^2-2)$ is the infinite dihedral group and its Julia set is the segment $[-2,2]$; the limit space is that segment, and the same computation as for the Grigorchuk group identifies it, because the two equivalence relations coincide. The example separates two phenomena: the dihedral group is virtually free and has a tree as its Cayley graph, while the Grigorchuk group is a branch group of intermediate growth, and the two share a limit space. The limit space is therefore an invariant of the action and not of the coarse geometry of the group, and it does not determine the group.

### The Fabrykowski–Gupta Group: the Dendrite

**Theorem.** The limit space of the Fabrykowski–Gupta group is the dendrite fractal: a compact connected, locally connected, one-dimensional space that is a union of arcs with branching, pictured by the tiles of its Schreier graphs.

The group is generated by a finite automaton of the classical family, and its Schreier graphs are planar graphs built from triangles; the tiling theorem identifies their limit with the dendrite. The example is the first in which the limit space is not a manifold but a tree-like fractal, and it is post-critically finite because the group is generated by a bounded automaton, so its dimension is one by the dimension theorem. The dendrite is one of the tree-like Julia sets of the quadratic family of the next example, and the two computations agree.

### The Group of the Sierpiński Gasket: the Gasket

**Theorem.** The limit space of the group $G_{\triangle} = \langle b_0,b_1,b_2\rangle$ of *Self-Similar Groups* is the Sierpiński gasket.

**Proof sketch.** The nucleus is the generating set, and the tiles of level $n$ are the three pieces of the gasket at scale $n$: the tile $T_v$ meets the tile $T_u$ exactly when $u$ and $v$ are related by a generator, which is the incidence rule of the gasket, and the approximation theorem then identifies the limit with the standard self-similar set with the three contractions of ratio one half at the vertices of a triangle. $\square$

The Sierpiński gasket is the example that shows the difference between the covering dimension and the Hausdorff dimension: the covering dimension of the gasket is one, by the dimension theorem, while its Hausdorff dimension is $\log 3/\log 2$, a number which is Part IV's and which is computed from the three contractions; the two dimensions are different and both are invariants of the space, at different levels of structure. The orbit Schreier graphs of the gasket group are the prefractal graphs of the gasket, and the limit in the local topology is the orbit graph of a boundary point, as in the general theorem.

### The Julia Sets of Rational Maps

**Theorem.** Let $f$ be a sub-hyperbolic rational map, in particular a post-critically finite one, of degree $d$, and let $\mathrm{IMG}(f)$ be its iterated monodromy group on the $d$-ary tree. Then $\mathrm{IMG}(f)$ is contracting, and its limit space is homeomorphic to the Julia set of $f$; under the homeomorphism the shift is the map $f$ itself on the Julia set, up to conjugation.

The theorem is Nekrashevych's, and the examples are the circle for $z^2$, whose group is the adding machine; the segment $[-2,2]$ for $z^2-2$, whose group is the infinite dihedral group; the Julia set of $z^2-1$, whose group has exponential growth and solvable word and conjugacy problems, as *Automaton and Contracting Groups* records; the dendrite of $z^2+i$ for the Misiurewicz parameters, whose Schreier graphs are trees; and the Julia sets of $z^2+c$ for the parameters of the airplane and the rabbit. The complex dynamics that produces the map $f$, the Julia set and its properties are Part III's; the fractal dimension of the Julia set is Part IV's. The contribution of this article to the family is the group-theoretic construction of the space: the limit space of a self-similar group is defined without any rational map, and a rational map with a post-critically finite critical orbit supplies a self-similar group whose limit space is its Julia set. The dictionary is not a bijection: the same limit space can arise from different actions and different groups, and the classification of the contracting self-similar groups by their limit spaces is not known.

## Summary

The action of a self-similar group on the level $n$ is recorded by the finite labelled Schreier graph $\Gamma_n(G,S)$, and the projections $\Gamma_{n+1} \to \Gamma_n$ make the levels an inverse spectrum; the graph of the action on the boundary is the inverse limit, a profinite graph, and the pointed orbit Schreier graph of a boundary point is the limit of the pointed finite graphs in the local topology, with $d((\Gamma_1,v_1),(\Gamma_2,v_2)) = 2^{-R}$ for the largest radius of agreement. A graph contraction deletes some edges and maps the others bijectively, and the shift of the tree extends to a contraction of $\Gamma_n$ onto $\Gamma_{n-1}$ when the generating set is closed under sections; the family of Schreier graphs is thus self-similar, and the wreath recursion is the substitution rule that generates it.

For a contracting action the space $X^{-\omega}$ of sequences infinite to the left carries the asymptotic equivalence, defined by a finite set of group elements one at each depth and computed by the nucleus: two sequences are equivalent exactly when there are $h_n \in N$ with $h_n(x_n) = y_n$ and $h_n|_{x_n} = h_{n-1}$, equivalently a path of the nuclear Moore diagram with labels $(x_n,y_n)$. The quotient $\mathcal{J}_G$ is the **limit space**: compact, metrisable, of covering dimension at most $|N|-1$, connected for a level-transitive action of a finitely generated group, and carrying the shift $s$ with at most $|X|$ preimages, the limit dynamical system. The **tiles** $T_v$ are the images of the cylinders; they satisfy $T_v = \bigcup_x T_{xv}$, $s(T_v) = T_{v'}$, every point lies in at most $|N|$ of them, and $T_u \cap T_v \neq \emptyset$ exactly when $h(v) = u$ for some $h \in N$. The graph $J_n(G)$ on the tiles of level $n$ is the Schreier graph of the nucleus, and the limit space is the limit of the graphs $J_n(G)$ rescaled, in the sense of the approximation theorem; it is also the Gromov boundary of the self-similarity complex, a hyperbolic space built from the Schreier graphs of the levels. Its covering dimension equals the asymptotic dimension of the orbital graphs, and it is one exactly when the group is the faithful quotient of a contracting self-similar virtually free group; in particular the limit space of a bounded automaton group is post-critically finite and one-dimensional.

The examples are the circle, for the adding machine, with shift the doubling map; the segment, for the Grigorchuk group, with the equivalence $\cdots111101w \sim \cdots111100w$ and shift the tent map; the segment, for the infinite dihedral group, with the same equivalence relation; the dendrite, for the Fabrykowski–Gupta group; the Sierpiński gasket, whose covering dimension is one and whose Hausdorff dimension is $\log 3/\log 2$; and the Julia sets of the sub-hyperbolic rational maps, whose self-similar groups are the iterated monodromy groups. The spectra of the Schreier graphs and the measures on the boundary are Part III's; the Gromov–Hausdorff convergence and the asymptotic dimension are Part IV's, and the fractal dimension of the limit space is Part IV's as well.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Gamma(G,S,M)$ | The Schreier graph of the action of $G = \langle S\rangle$ on $M$ |
| $\Gamma(G,S,x)$ | The orbit Schreier graph at $x$ |
| $\Gamma_n(G,S) = \Gamma(G,S,X^n)$ | The Schreier graph of the action on the level $n$ |
| $\pi_n : \Gamma_{n+1} \to \Gamma_n$ | The projection deleting the last letter; a surjective morphism |
| $\Gamma(G,S,X^{\omega}) = \varprojlim \Gamma_n$ | The profinite graph of the action on the boundary |
| $d((\Gamma_1,v_1),(\Gamma_2,v_2)) = 2^{-R}$ | The metric of the local topology on pointed graphs |
| graph contraction, self-similar graph | Edge deletion plus a bijection on the surviving edges; an infinite graph contracted to itself |
| $X^{-\omega}$ | The space of sequences infinite to the left, a Cantor space |
| $\sim$ | The asymptotic equivalence, given by a finite set one element at each depth |
| $h_n(x_n) = y_n$, $h_n\|_{x_n} = h_{n-1}$, $h_n \in N$ | The nucleus criterion for the equivalence |
| $\mathcal{J}_G = X^{-\omega}/\!\sim$ | The limit space of the contracting action |
| $s$ | The shift on $\mathcal{J}_G$; the limit dynamical system $(\mathcal{J}_G,s)$ |
| $T_v$ | The tile at the word $v$, the image of the sequences ending in $v$ |
| $T_u \cap T_v \neq \emptyset$ | Exactly when $h(v) = u$ for some $h$ in the nucleus |
| $J_n(G)$ | The graph on the tiles of level $n$, isomorphic to $\Gamma(\langle N\rangle,N,X^n)$ |
| $\Sigma(G,S)$ | The self-similarity complex; its boundary is $\mathcal{J}_G$ |
| $\dim$ | The covering dimension of *Dimension Theory* |

## Further Reading

- Volodymyr Nekrashevych, *Self-similar groups*, Mathematical Surveys and Monographs **117** (American Mathematical Society, 2005), for the Schreier graphs of the levels, the asymptotic equivalence, the limit space, the tiles, the approximation theorem by the graphs $J_n(G)$ and the boundary of the self-similarity complex.
- Rostislav Grigorchuk, Volodymyr Nekrashevych and Vitaly Sushchansky, *From fractal groups to fractal sets*, in *Fractals in Graz 2001* (Birkhäuser, 2003), 25–118, for the survey treatment of the limit spaces, the substitution rules of the Schreier graphs and the tables of the limit spaces of the classical groups.
- Laurent Bartholdi and Rostislav Grigorchuk, *On the spectrum of Hecke type operators related to some fractal groups*, Trudy Matematicheskogo Instituta imeni V. A. Steklova **231** (2000), 5–45, for the Schreier graphs of the Grigorchuk group and of the other examples, with their substitution rules and their spectra, which are Part III's subject.
- Rostislav Grigorchuk and Andrzej Żuk, *The lamplighter group as a group generated by a 2-state automaton, and its spectrum*, Geometriae Dedicata **87** (2001), 209–244, for the level Schreier graphs of the lamplighter group and the spectral problem attached to them.
- Volodymyr Nekrashevych, *Self-similar groups and topological dimension*, Transactions of the American Mathematical Society **358** (2006), 2751–2777, for the equality of the covering dimension of the limit space with the asymptotic dimension of the orbital graphs and the one-dimensionality criterion.
- Ievgen Bondarenko and Volodymyr Nekrashevych, *Post-critically finite self-similar groups*, Algebra and Discrete Mathematics (2003), 21–32, for the identification of the post-critically finite limit spaces with the bounded automata and the one-dimensionality of the post-critically finite limit space.
- Jacek Fabrykowski and Narain Gupta, *On groups with sub-exponential growth functions*, Journal of the Indian Mathematical Society **54** (1989), 249–256, for the group whose limit space is the dendrite.
- Volodymyr Nekrashevych, *Iterated monodromy groups*, in *Groups and Dynamics* (London Mathematical Society Lecture Note Series **387**, 2011), 1–46, for the construction of the iterated monodromy groups and the theorem that the limit space of a sub-hyperbolic rational map is its Julia set.
