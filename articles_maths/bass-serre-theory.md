
# __Bass–Serre Theory__

## Introduction

Bass–Serre theory is the dictionary between the two ways of decomposing a group: the algebraic way, by a presentation as a **fundamental group of a graph of groups** — an amalgamated free product $A *_C B$ or an HNN extension $A*_C$ with its attached subgroups — and the geometric way, by an **action on a tree** without inversions. A group acts on a tree if and only if it is the fundamental group of a graph of groups, and the quotient graph of groups can be recovered from the action: the vertex stabilisers are the conjugates of the vertex groups and the edge stabilisers are the conjugates of the edge groups. This makes the existence of a nontrivial splitting equivalent to the existence of an action on a tree with no global fixed point, and it turns questions about decompositions — the normal form, the word problem, the subgroups, the ends — into questions about the geometry of a tree.

The theory gives the structure theorem for amalgamated free products and HNN extensions, the normal form theorem and Britton's lemma, the subgroup theory of a group acting on a tree, the finiteness and word-problem statements, and the classification of the ends. Its most famous application is Stallings' theorem: a finitely generated group has infinitely many ends if and only if it splits nontrivially over a finite subgroup, which translates the combinatorial notion of an end into a statement about an action on a tree. The dictionary is also the organising principle for the classification of groups by their splittings, for the JSJ decomposition of a finitely presented group, and for the arithmetic examples: $SL_2(\mathbb{Z})$ is the amalgam $\mathbb{Z}/4 *_{\mathbb{Z}/2}\mathbb{Z}/6$ acting on its tree, and $SL_2(\mathbb{Z}[1/p])$ is the amalgam of two copies of $SL_2(\mathbb{Z})$ along a congruence subgroup, acting on the Bruhat–Tits tree of $SL_2(\mathbb{Q}_p)$.

The article develops graphs of groups and their fundamental groups, the Bass–Serre tree and the structure theorem, the normal form theorems, the subgroup theory, the fixed-point theorems and Serre's property (FA), the ends and the Stallings theorem, the accessibility theorem of Dunwoody, and the arithmetic examples. The input from above is the theory of graphs, trees, ends, growth and quasi-isometry of *Geometric Group Theory*, and the hyperbolic boundary of *Hyperbolic Groups*; the input from Part I is the theory of free groups, free products, presentations, the Kurosh subgroup theorem and group cohomology, all of *Groups* and *Combinatorial Group Theory*. The **graph of groups** and its **fundamental group** are defined in line, since no earlier article introduces them, and the tree is the topological space of *Metric, Uniform and Complete Spaces* with the graph structure of *Geometric Group Theory*.

The boundary with Part III is the one fixed for this block. What is developed here is the combinatorial and topological content: graphs of groups, the fundamental group, the tree, the structure theorem, normal forms, subgroups, fixed points, ends and the accessibility theory. What is deferred is the **analytic** theory: the measure-theoretic study of the boundary of the tree, the harmonic analysis and the random walks on trees, the spectral theory of the Laplacian of a graph of groups, the Patterson–Sullivan type measures on the ends, and the ergodic theory of the action, all of which belong to *Analysis on Groups* and the harmonic analysis of Part III, where the measure and the limit are available. The **Bruhat–Tits tree** of a reductive group over a local field, which is the arithmetic source of the examples, is not covered here, and so are the buildings that generalise the tree. No physics is invoked.

## Graphs of Groups

### Graphs, Trees and Ends

**Definition.** A **graph** $\Gamma$ consists of a vertex set $V(\Gamma)$, an edge set $E(\Gamma)$ and two maps $E(\Gamma)\to V(\Gamma)$ giving the endpoints; the graph is **finite** if both sets are finite, and the **realisation** of a graph is the topological space obtained by joining the two endpoints of each edge by a unit interval, so that a graph is a one-dimensional CW-complex. A graph is a **tree** if its realisation is connected and simply connected, equivalently if it is connected and contains no reduced cycle; a tree is a $0$-hyperbolic metric space in the graph distance, and the **ends** of a locally finite graph are the connected components at infinity, the number of ends of a finitely generated group being the number of ends of its Cayley graph, as in *Geometric Group Theory*.

**Remark.** The realisation of a tree is a contractible topological space, and this is the reason the theory belongs to this Part: the tree a group acts on is a topological space with an intrinsic metric, and the geometric invariants of the action — the fixed points, the axes, the ends, the quasi-isometry type — are the structure of the group.

### Graphs of Groups

**Definition.** A **graph of groups** $(\Gamma, \mathcal{G}_\bullet)$ consists of a connected graph $\Gamma$, a group $\mathcal{G}_v$ for every vertex $v$, a group $\mathcal{G}_e$ for every edge $e$, and for every edge $e$ with endpoints $u$ and $v$ two injective homomorphisms

$$
\alpha_e : \mathcal{G}_e \longrightarrow \mathcal{G}_u , \qquad \omega_e : \mathcal{G}_e \longrightarrow \mathcal{G}_v ,
$$

the **boundary monomorphisms**, identifying the edge group with subgroups of its two vertex groups. The graph of groups is **finite** if $\Gamma$ is finite and all the groups are finitely generated; it is **reduced** if the edge maps are isomorphisms whenever one of the endpoint vertex groups is trivial.

**Definition (the fundamental group).** Choose a maximal tree $T \subseteq \Gamma$ and, for every vertex $v$, a presentation of $\mathcal{G}_v$ in generators and relators. The **fundamental group** $\pi_1(\Gamma,\mathcal{G}_\bullet)$ is the group generated by the generators of all the vertex groups together with one generator $t_e$ for every edge $e \notin T$, subject to the relators of the vertex groups, the relations

$$
\alpha_e(g) = \omega_e(g) \qquad \text{for every } e \in E(T),\ g \in \mathcal{G}_e ,
$$

and, for each $e \notin T$ with endpoints $u, v$, the relations expressing conjugation by $t_e$: $t_e\,\alpha_e(g)\,t_e^{-1} = \omega_e(g)$ for all $g \in \mathcal{G}_e$. The resulting group is independent of the choice of the maximal tree $T$ and of the presentations, up to isomorphism, and it is the **graph of groups** given by the data.

**Example (amalgamated free products).** Let $\Gamma$ be a single edge with endpoints $u,v$ and vertex groups $A,B$, the edge group $C$ mapping injectively into both. Then $\pi_1(\Gamma,\mathcal{G}_\bullet)$ is the **free product of $A$ and $B$ amalgamated over $C$**,

$$
A *_C B = \langle A, B \mid \alpha(g) = \omega(g) \text{ for } g\in C\rangle ,
$$

which for $C = 1$ reduces to the free product $A * B$, the group of *Combinatorial Group Theory*.

**Example (HNN extensions).** Let $\Gamma$ be a single loop with one vertex $v$ and one edge $e$, with vertex group $A$ and edge group $C$ mapping by two monomorphisms $\alpha, \omega : C \to A$. Then $\pi_1(\Gamma,\mathcal{G}_\bullet)$ is the **HNN extension**

$$
A*_C = \langle A, t \mid t\,\alpha(c)\,t^{-1} = \omega(c) \text{ for } c\in C\rangle ,
$$

the stable letter $t$ conjugating one copy of $C$ to the other; when $C = 1$ the group is $A * \mathbb{Z}$.

### The Bass–Serre Tree

**Definition.** Let $(\Gamma,\mathcal{G}_\bullet)$ be a graph of groups and let $G = \pi_1(\Gamma,\mathcal{G}_\bullet)$. The **Bass–Serre tree** $T$ is the graph whose vertices are the left cosets $g\mathcal{G}_v$ of the vertex groups, one family for each vertex $v$ of $\Gamma$, with an edge from $g\mathcal{G}_v$ to $g t_e\,\mathcal{G}_w$ for every edge $e$ of $\Gamma$ with endpoints $v$ and $w$ and every $g \in G$, where $t_e$ is the chosen stable letter, and for edges of the tree $T$ the stable letter is taken to be $1$. The group $G$ acts on $T$ by left translation, and the quotient $T/G$ is isomorphic to the realisation of $\Gamma$.

**Theorem (the Bass–Serre tree).** The graph $T$ is a tree, the action of $G$ is without inversions (no element interchanges the two endpoints of an edge), the quotient is $\Gamma$, the stabiliser of a vertex $g\mathcal{G}_v$ is $g\mathcal{G}_vg^{-1}$ and the stabiliser of an edge is the corresponding conjugate of an edge group. The construction is inverse to the passage from an action to the quotient graph of groups described below.

**Proof sketch.** The quotient computation is immediate from the construction. That $T$ is a tree is proved by the normal form theorem: a reduced path in $T$ that returns to its starting point yields a nontrivial relation in $G$ of a normal form, which is impossible; the argument is the same as the proof that the Cayley graph of a free product is a tree, generalised along the edge groups. The details are the theorem of Bass and Serre and are quoted from the literature. $\square$

## The Structure Theorem

### Statement

**Theorem (structure theorem of Bass–Serre).** 

**(a)** If a group $G$ acts on a tree $T$ without inversions, then $G$ is the fundamental group of the **quotient graph of groups** $(\Gamma,\mathcal{G}_\bullet)$, where $\Gamma = T/G$, the vertex group at a vertex $v$ of $\Gamma$ is the stabiliser $G_{\tilde v}$ of a lift $\tilde v$, and the edge group at an edge $e$ is the stabiliser $G_{\tilde e}$ of a lift, with the boundary monomorphisms induced by the inclusions $G_{\tilde e}\hookrightarrow G_{\tilde v}$.

**(b)** Conversely, if $G$ is the fundamental group of a finite graph of groups $(\Gamma,\mathcal{G}_\bullet)$, then $G$ acts without inversions on the Bass–Serre tree $T$ with quotient $\Gamma$ and with the stated stabilisers.

**(c)** The action is minimal (no proper invariant subtree) exactly when the graph of groups is reduced in the appropriate sense, and the tree $T$ is the minimal subtree when the action is minimal; every action on a tree without inversions has a minimal invariant subtree, unique up to the action.

**(d)** If $G$ is finitely generated and acts without inversions on a tree with finite quotient, then the vertex groups are finitely generated; conversely, if $\Gamma$ is finite and the vertex groups are finitely generated, then $G$ is finitely generated.

**Proof sketch.** (a) The quotient map $T\to\Gamma$ is a graph morphism, and the stabiliser of a vertex of $T$ maps onto the vertex group at its image; a choice of lift for each vertex of $\Gamma$ and of an edge path between lifts produces the stable letters and the boundary monomorphisms, and the presentation of the fundamental group is read from the action. The construction is well defined because the translates of a lift exhaust the vertices over a given one, and because the tree has no circuits. (b) is the previous theorem. (c) The minimal subtree is the union of the axes of the elements and the geodesics joining them; it is invariant and unique. (d) Finite generation in the presence of a finite quotient follows because finitely many generators suffice modulo the vertex stabilisers, and a finite set of generators of $G$ is a finite set of generators for each vertex group modulo the edge groups; the converse is immediate from the presentation. The details are the theorem of Bass and Serre and are quoted from the literature. $\square$

### Amalgamated Products and HNN Extensions

**Corollary (Kurosh-type normal form for $A *_C B$).** Every element of $A *_C B$ is uniquely of the form

$$
g = a_0 b_1 a_1 b_2 \cdots b_n a_n ,
$$

with each $a_i \in A$, each $b_i \in B$, the elements $a_1,\dots,a_{n-1}$ and $b_1,\dots,b_n$ not in $C$ and, if $n \geq 1$, the elements $b_i \notin C$ and $a_i\notin C$ for $1 \leq i \leq n-1$; uniqueness is up to the ambiguity of replacing a factor by a product of elements of $C$ on the appropriate side. Consequently $A$ and $B$ embed in $A *_C B$, and killing the image of $C$ gives the free product $A/C * B/C$ as a quotient.

**Proof.** The normal form is the statement that the Bass–Serre tree of the segment with vertex groups $A, B$ and edge group $C$ is a tree; a word that is reduced in the sense of the statement gives a reduced path in the tree, and a reduced path cannot be closed unless the word is trivial. $\square$

**Corollary (Britton's lemma).** Let $G = A*_C$ be an HNN extension with stable letter $t$. Call a word $a_0t^{\varepsilon_1}a_1\cdots t^{\varepsilon_n}a_n$ with $a_i \in A$ and $\varepsilon_i = \pm1$ **reduced** if $n \geq 1$, if $a_i \neq 1$ for $1 \leq i \leq n-1$, and if it contains no subword $t\,\alpha(c)\,t^{-1}$ or $t^{-1}\,\omega(c)\,t$ with $c \in C$. Britton's lemma states that a reduced word of this form represents an element different from the identity of $G$. Hence $A$ embeds in $G$, every element of $G$ has a reduced expression, and the normal form of an element is unique.

**Proof.** Britton's lemma is the normal form theorem for the HNN extension, proved by the same path argument in the Bass–Serre tree of the loop: a reduced word representing the identity gives a closed reduced path in the tree, which is impossible unless a cancellation of the forbidden type occurs. $\square$

## Groups Acting on Trees

### Fixed Points and Serre's Property (FA)

**Definition.** A group $G$ has **property (FA)** if every action of $G$ on a tree without inversions has a global fixed point — a vertex fixed by every element of $G$ — and the group has **(FA')** if every such action fixes a vertex or an edge. The property is a **Serre property**; the fixed-point theorems for actions on trees are the geometric content of the structure theorem.

**Theorem (fixed-point criteria).** Let $G$ act on a tree $T$ without inversions.

**(a)** If $G$ is finitely generated and has a bounded orbit, then $G$ has a fixed vertex (or a fixed edge in the case of a single edge interchanged, which cannot happen without inversions).

**(b)** If $G$ has property (T), then $G$ has property (FA): every action of $G$ on a tree without inversions has a global fixed point. More generally a group with (T) acting on a tree fixes a vertex.

**(c)** If $G$ is amenable and acts on a tree, then $G$ fixes a vertex or an end of the tree.

**Proof sketch.** (a) The set of vertices fixed by a single element of $G$ is a subtree (the axis or the fixed-point set), and the intersection of the fixed-point subtrees of a generating set is non-empty by the Helly property of subtrees; a bounded orbit forces the intersection to be non-empty. (b) Property (T) applied to the affine isometric action of $G$ on the Hilbert space of functions of finite Dirichlet energy on the vertex set of the tree — the action associated with the graph Laplacian — gives a fixed point, and a fixed point of that action is an invariant finite-energy harmonic function on the tree, which is constant, whence a fixed vertex; this is the implication (T) $\Rightarrow$ (FA) and it uses the Delorme–Guichardet characterisation of *Property (T)*. (c) An amenable group acting on a tree has a fixed point in the tree or a fixed end; this is the fixed-point characterisation of amenability of *Amenable Groups* applied to the convex set of means on the ends. The statements are standard and are quoted from the literature. $\square$

**Corollary.** A group with property (T) does not split nontrivially over any subgroup: it is the fundamental group of no graph of groups with a single edge whose edge group is a proper subgroup of each vertex group in which it sits. In particular the higher-rank semisimple groups and their lattices, such as $SL_n(\mathbb{Z})$ for $n \geq 3$, act on no tree without a fixed point, and the free products, the amalgams and the HNN extensions are not (T) groups.

### Subgroups and the Induced Tree

**Theorem (subgroup theorem).** Let $G$ act on a tree $T$ without inversions and let $H \leq G$ be a subgroup. Then $H$ acts on the induced subtree $T_H$ — the minimal subtree of $T$ invariant under $H$, which consists of the axes of the hyperbolic elements of $H$ and the geodesics joining them — and $H$ is the fundamental group of the quotient graph of groups $T_H/H$, whose vertex groups are the intersections of $H$ with the conjugates of the vertex groups of the original graph of groups and whose edge groups are the analogous intersections with the conjugates of the edge groups.

**Proof sketch.** The action of $H$ on the minimal subtree is without inversions, so the structure theorem applies; the vertex stabilisers for the action of $H$ are the intersections of $H$ with the vertex stabilisers of $G$, which are conjugates of the vertex groups, and similarly for the edges. If $H$ fixes a vertex, the minimal subtree is a point and $H$ is contained in a vertex stabiliser. The theorem is Serre's and is quoted from the literature. $\square$

**Corollary (Kurosh).** A subgroup of a free product $G = *_{i\in I}G_i$ is a free product of a free group and of conjugates of subgroups of the factors. In particular every subgroup of a free group is free (the Nielsen–Schreier theorem) and the rank of a subgroup of finite index $k$ in a free group of rank $n$ is $k(n-1)+1$.

**Proof sketch.** The subgroup acts on the Bass–Serre tree of the free product, which is the tree whose vertices are the cosets of the free factors; the quotient graph has vertex groups that are the intersections with the conjugates of the free factors and trivial edge groups, so the fundamental group is a free product of the stated groups and the free group on the cycles of the quotient graph. The index formula is the computation of the Euler characteristic of the quotient. The Kurosh theorem is stated in *Combinatorial Group Theory* in Part I, and the geometric proof is Serre's. $\square$

### Finiteness and the Word Problem

**Theorem.** Let $G$ be the fundamental group of a finite graph of groups $(\Gamma,\mathcal{G}_\bullet)$.

**(a)** $G$ is finitely presented if and only if the vertex groups are finitely presented and the edge groups are finitely generated; $G$ is finitely generated if and only if the vertex groups are.

**(b)** The word problem for $G$ is solvable if the word problem for the vertex groups is solvable, and the conjugacy problem is solvable if it is solvable in the vertex groups, by the reduction of a word to normal form along the tree.

**(c)** If all the vertex groups are finite, then $G$ acts on a tree with finite stabilisers and finite quotient; such a group is virtually free and hyperbolic, and it has infinitely many ends unless it is an amalgam $A *_C B$ with $C$ of index $2$ in both $A$ and $B$, in which case it has two ends and is virtually $\mathbb{Z}$. The graph of groups is then the decomposition of the group into finite pieces.

**Proof sketch.** (a) The presentation of the fundamental group uses the presentations of the vertex groups and finitely many stable letters, so finite generation and finite presentation are read off from the data, with the edge generators giving the finite generation of the edge groups in the finitely presented case. (b) A word in the generators can be reduced along the tree by successively replacing subwords lying in a vertex group by their normal forms; the process terminates because the length of the reduced path in the tree strictly decreases. (c) is the case of finite vertex groups of the structure theorem, and the virtual freeness follows from the classification of the groups with infinitely many ends of *Geometric Group Theory*. The statements are standard and are quoted from the literature. $\square$

## Ends and Splittings

### The Stallings Theorem

**Definition.** Let $G$ be a finitely generated group. The **number of ends** $e(G)$ is the number of ends of its Cayley graph, defined in *Geometric Group Theory* and independent of the generating set. A group **splits over a subgroup** $C$ if it is the fundamental group of a graph of groups with a single edge whose edge group is $C$ and whose edge maps are not isomorphisms, that is, if it is a nontrivial amalgam $A *_C B$ with $C \neq A$ and $C \neq B$, or an HNN extension $A*_C$ with $C \neq A$.

**Theorem (Stallings).** Let $G$ be a finitely generated group. Then $G$ has infinitely many ends if and only if it splits nontrivially over a finite subgroup: $G$ is either $A *_C B$ with $C$ finite and $A,B$ proper, or $A*_C$ with $C$ finite. In particular a finitely generated group with infinitely many ends is either virtually free with infinitely many ends or contains a free subgroup of rank two, and it is not amenable.

**Proof sketch.** If $G$ splits over a finite subgroup, the Bass–Serre tree of the splitting has infinitely many ends and the group acts on it with finite edge stabilisers and two-or-more vertex orbits, which produces the infinite end space. Conversely, the hypothesis of infinitely many ends supplies a nontrivial partition of the ends of the Cayley graph invariant under the group, and the theory of the action on the tree of the ends produces the splitting over a finite subgroup; the construction of the tree from the ends is the technical core of Stallings' theorem, refined by Dunwoody into the theory of the accessibility of finitely presented groups. The theorem is quoted from the literature. $\square$

### Accessibility

**Theorem (Dunwoody).** Every finitely presented group has a **terminal splitting** over finite subgroups: there is a graph of groups decomposition over finite edge groups with finite graph whose vertex groups have no further nontrivial splitting over a finite subgroup. Consequently the graph of groups decompositions of a finitely presented group over finite subgroups are governed by finitely many "pieces", and the groups with infinitely many ends admit a canonical decomposition over finite subgroups.

**Proof sketch.** The theorem is Dunwoody's accessibility theorem: one considers the splittings of $G$ over finite subgroups as partitions of the ends of the Cayley graph and shows that a sequence of successively finer splittings cannot be infinite for a finitely presented group, because each splitting uses a finite amount of the presentation; the terminal object of the resulting finite chain is the terminal splitting. The theorem is quoted from the literature. $\square$

## Examples

### The Modular Group

**Example ($SL_2(\mathbb{Z})$).** The modular group $SL_2(\mathbb{Z})$, modulo its centre $\{\pm I\}$, is the amalgam

$$
PSL_2(\mathbb{Z}) \cong \mathbb{Z}/2 * \mathbb{Z}/3 ,
$$

and $SL_2(\mathbb{Z})$ itself is the amalgam $\mathbb{Z}/4 *_{\mathbb{Z}/2} \mathbb{Z}/6$ over the common centre: the vertex groups are generated by the matrices of order $4$ and $6$, and the edge group is the centre. The Bass–Serre tree has quotient the segment joining the two vertex groups, and the action on it is the tree-theoretic form of the decomposition of the modular group into its two torsion pieces; it exhibits the group as acting on a tree with finite stabilisers, hence as hyperbolic and virtually free, and the decomposition makes its subgroup structure and its abelianisation immediately computable. By the Kurosh theorem a subgroup of $PSL_2(\mathbb{Z})$ is free modulo its torsion, and this is the classical source of the noncongruence subgroups of *Arithmetic Groups*.

**Example (the congruence amalgam).** Let $p$ be a prime and let $\Gamma_0(p)$ be the congruence subgroup of matrices in $SL_2(\mathbb{Z})$ whose lower-left entry is divisible by $p$. Then

$$
SL_2(\mathbb{Z}[1/p]) \cong SL_2(\mathbb{Z}) *_{\Gamma_0(p)} SL_2(\mathbb{Z}) ,
$$

the two vertex groups being the two copies of $SL_2(\mathbb{Z})$ distinguished by the two embeddings at the two ends of the Bruhat–Tits tree of $SL_2(\mathbb{Q}_p)$, and the edge group being the congruence subgroup stabilising an edge. This is the arithmetic example on which the analysis of the groups $SL_2(\mathcal{O}_S)$ rests; the tree is the Bruhat–Tits tree, and the amalgam is the explicit form in which the $S$-arithmetic lattice of *Arithmetic Groups* is presented.

### The Euler Characteristic and the Hierarchy

**Definition.** Let $G$ be a group with a finite classifying space or with a graph of groups decomposition into groups of finite cohomological dimension. The **Euler characteristic** $\chi(G)$ is the number $\sum_i(-1)^i\operatorname{rank}H_i(G;\mathbb{Z})$ in the appropriate sense, when it is defined.

**Theorem (Bass–Serre Euler characteristic).** Let $G = \pi_1(\Gamma,\mathcal{G}_\bullet)$ be the fundamental group of a finite graph of groups with vertex groups $\mathcal{G}_v$ and edge groups $\mathcal{G}_e$ of finite Euler characteristic, and suppose the higher Euler characteristics of the pieces vanish. Then

$$
\chi(G) = \sum_{v\in V(\Gamma)}\chi(\mathcal{G}_v) - \sum_{e\in E(\Gamma)}\chi(\mathcal{G}_e) .
$$

**Proof sketch.** The formula is the Mayer–Vietoris sequence applied to the action on the Bass–Serre tree with the equivariant decomposition of the tree into the vertices and the edges; the finite quotient gives a finite complex whose Euler characteristic is computed from the cells modulo the stabilisers, and the vanishing of the higher Euler characteristics makes the sum a group-theoretic invariant. The formula is standard and is quoted from the literature. $\square$

**Example.** For a free product $A * B$ with both Euler characteristics defined, $\chi(A * B) = \chi(A) + \chi(B) - 1$; for a free product of $n$ groups the correction is $1-n$. For $PSL_2(\mathbb{Z}) = \mathbb{Z}/2 * \mathbb{Z}/3$, the formula gives $\chi = \tfrac12 + \tfrac13 - 1 = -\tfrac{1}{6}$, and the Euler characteristic of a finite-index subgroup is the index times this quantity, which recovers the genus formulas for the modular curve; the computation is verified directly from the formula and is the classical test of the theory.

**Remark (the JSJ decomposition).** The theory of splittings over finite and free subgroups produces a canonical decomposition of a finitely presented group: the **JSJ decomposition**, with the terminal splitting of Dunwoody over finite subgroups and the analogous canonical decomposition over cyclic subgroups for the groups with infinitely many ends relative to a family of subgroups. The existence of this canonical decomposition is the entry point of the rigidity theory for outer automorphism groups and for the structure of the fundamental groups of three-manifolds, where the decomposition of Kneser and Milnor and the JSJ decomposition of the manifold correspond to splittings of the fundamental group over finite and cyclic subgroups.

## The Boundary with Analysis

The theory of this article is combinatorial and topological; the analysis of the tree and of its boundary is Part III.

- The **measure-theoretic boundary** of the Bass–Serre tree, the **harmonic analysis** of the action of the fundamental group, the **random walks** on the tree and the **Poisson boundary** are *Analysis on Groups* .
- The **spectral theory** of the graph Laplacian of a quotient graph of groups, the **zeta functions** of a graph and the **prime geodesic** counting for a tree are Part III.
- The **measured group theory** of the splittings, the **orbit equivalence** of the actions and the **cost** are.
- The **Bruhat–Tits tree** and the **buildings** areand with this article; the tree is the rank-one case of the building and the dictionary of this article is the genus-one case of the building dictionary.
- What is *not* deferred: graphs of groups and their fundamental groups; the Bass–Serre tree and the structure theorem; the normal form theorems and Britton's lemma; the subgroup theorem and the Kurosh theorem as consequences; the fixed-point criteria and property (FA); the finiteness and word-problem statements; the ends and the Stallings and Dunwoody theorems; and the arithmetic examples with the Euler characteristic formula.

## Summary

A graph of groups assigns a group to every vertex and every edge of a connected graph together with injective boundary maps from each edge group into its endpoint vertex groups, and its fundamental group is defined by a presentation relative to a spanning tree, with one stable letter for each edge outside the tree. An amalgamated free product $A *_C B$ is the graph of groups of a segment and an HNN extension $A*_C$ that of a loop. Every such group acts without inversions on its Bass–Serre tree, whose vertices are the cosets of the vertex groups, whose quotient is the graph, and whose vertex and edge stabilisers are the conjugates of the vertex and edge groups.

The structure theorem says that the construction is a bijection: a group acting on a tree without inversions is the fundamental group of the quotient graph of groups, and the quotient records the stabilisers. The normal form theorem for an amalgam and Britton's lemma for an HNN extension are the tree-is-a-tree statements, and they give the embedding of the pieces in the fundamental group. A subgroup of a group acting on a tree acts on the minimal subtree, and the quotient graph of groups has the intersections with the vertex and edge stabilisers as pieces; the Kurosh theorem for subgroups of a free product is the special case with trivial edge groups. A group with property (T) has property (FA) and acts on no tree without a fixed point, so it splits nontrivially over nothing, and an amenable group acting on a tree fixes a vertex or an end.

A finitely generated group has infinitely many ends exactly when it splits nontrivially over a finite subgroup (Stallings), and a finitely presented group has a terminal splitting over finite subgroups (Dunwoody). The formula $\chi(G) = \sum_v\chi(\mathcal{G}_v)-\sum_e\chi(\mathcal{G}_e)$ computes the Euler characteristic from a graph of groups, and the arithmetic examples $PSL_2(\mathbb{Z}) \cong \mathbb{Z}/2 * \mathbb{Z}/3$ and $SL_2(\mathbb{Z}[1/p]) \cong SL_2(\mathbb{Z}) *_{\Gamma_0(p)} SL_2(\mathbb{Z})$ are the classical splittings of the modular groups. The measure-theoretic and ergodic theory of the tree and its boundary belongs to Part III, and the generalised trees of the buildings to the companion articles of this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\Gamma,\mathcal{G}_\bullet)$ | Graph of groups: vertex groups $\mathcal{G}_v$, edge groups $\mathcal{G}_e$ |
| $\alpha_e, \omega_e : \mathcal{G}_e \to \mathcal{G}_u,\mathcal{G}_v$ | Boundary monomorphisms |
| $T$, spanning tree | Maximal subtree of $\Gamma$ used to define the fundamental group |
| $t_e$ | Stable letter for an edge $e \notin T$ |
| $\pi_1(\Gamma,\mathcal{G}_\bullet)$ | Fundamental group of the graph of groups |
| $A *_C B$ | Amalgamated free product over $C$ |
| $A*_C$, $t$ | HNN extension with associated subgroups and stable letter $t$ |
| Bass–Serre tree $T$ | Tree of cosets of vertex groups; $T/G = \Gamma$ |
| $G_{\tilde v}, G_{\tilde e}$ | Vertex and edge stabilisers in the tree |
| FA, FA' | Serre's fixed-point properties for actions on trees |
| $e(G)$ | Number of ends (see *Geometric Group Theory*) |
| Splitting over $C$ | Amalgam or HNN extension with edge group $C$ and proper edge maps |
| $\chi(G)$ | Euler characteristic; $\chi(G) = \sum_v\chi(\mathcal{G}_v)-\sum_e\chi(\mathcal{G}_e)$ |
| $PSL_2(\mathbb{Z}) = \mathbb{Z}/2 * \mathbb{Z}/3$ | The modular amalgam |
| $\Gamma_0(p)$ | Congruence subgroup; edge group of the $SL_2(\mathbb{Z}[1/p])$ amalgam |
| Minimal subtree $T_H$ | For $H\leq G$, the smallest $H$-invariant subtree |
| Terminal splitting (Dunwoody) | Canonical decomposition over finite subgroups |







## Further Reading

- Jean-Pierre Serre, *Trees* (Springer, 1980), for the original account of the theory of groups acting on trees.
- Hyman Bass, *Covering theory for graphs of groups*, Journal of Pure and Applied Algebra 89 (1993), 3–47, for the Bass–Serre tree and the covering theory.
- Warren Dicks and M. J. Dunwoody, *Groups Acting on Graphs* (Cambridge University Press, 1989), for the systematic treatment of graphs of groups and accessibility.
- John Stallings, *On torsion-free groups with infinitely many ends*, Annals of Mathematics 88 (1968), 312–334, for the splitting theorem over finite subgroups.
- M. J. Dunwoody, *The accessibility of finitely presented groups*, Inventiones Mathematicae 81 (1985), 449–457, for the terminal splitting theorem.
- Roger C. Lyndon and Paul E. Schupp, *Combinatorial Group Theory* (Springer, 1977), for the normal form theorems, Britton's lemma and the Kurosh theorem.
- Alexandre Kurosh, *Die Untergruppen der freien Produkte von beliebigen Gruppen*, Mathematische Annalen 109 (1934), 637–660, for the subgroup theorem.
- Graham A. Niblo and Martin A. Roller (eds.), *Geometric Group Theory*, LMS Lecture Notes 181 (Cambridge University Press, 1993), for surveys of the applications.
- Jean-Pierre Serre, *Arbres, amalgames, $SL_2$*, Astérisque 46 (1977), for the arithmetic examples and the Bruhat–Tits tree.
- Martin R. Bridson and André Haefliger, *Metric Spaces of Non-Positive Curvature* (Springer, 1999), for the metric form of the theory and the $\mathbb{R}$-trees.
