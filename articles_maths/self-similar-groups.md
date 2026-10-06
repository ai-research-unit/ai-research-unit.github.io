# __Self-Similar Groups__

## Introduction

A **regular rooted tree** is the tree whose vertices are the finite words in a finite alphabet $X$, the empty word $\varnothing$ being the root and the word $vx$ being the child of $v$ reached by the letter $x$. Every vertex $v$ carries a subtree $\mathcal{T}_v$ rooted at it, and $\mathcal{T}_v$ is isomorphic to the whole tree $\mathcal{T}$ by the map $vw \mapsto w$. An **automorphism** of the tree is a bijection of the vertices fixing the root and preserving adjacency, hence preserving the level of a vertex; the group of them is written $\operatorname{Aut}(\mathcal{T})$.

Such an automorphism $g$ acts on the subtree $\mathcal{T}_v$ by carrying it isomorphically onto the subtree $\mathcal{T}_{g(v)}$, and once the two subtrees are read as copies of $\mathcal{T}$ the action becomes an automorphism of $\mathcal{T}$, the **section** $g|_v$. A subgroup $G \leq \operatorname{Aut}(\mathcal{T})$ is **self-similar** if the section of every element of $G$ at every vertex is again an element of $G$. The condition is a closure property, and it says that the group reproduces itself inside every subtree: the image of $G$ under the section at $v$ lies in $G$, so that $G$ acts on the subtree $\mathcal{T}_v$ through its own automorphisms. Written as a recursion, an element is determined by its permutation of the first level and its one section per letter, and the self-similar group therefore embeds in its own wreath product, $G \hookrightarrow G \wr \operatorname{Sym}(X)$.

The article develops the tree and its boundary, the automorphisms and their sections, the wreath recursion and the portrait of an element, the definition of a self-similar action and the equivalent formulations, the level-transitive, self-replicating and recurrent actions, the standard examples — the adding machine, the infinite dihedral group, the Grigorchuk group, the lamplighter group, the groups of the Sierpiński gasket and the Gupta–Sidki groups — and the branch and weakly branch groups with their rigid stabilizers. It states which of these groups are torsion, amenable or just infinite, and it records the growth of the Grigorchuk group, which is the intermediate-growth example of *Geometric Group Theory*.

The article assumes *Graph Theory*, above it in the menu, for the tree, the graph distance and the level of a vertex; *Groups*, *Transformation Groups* and *Infinite Groups* for group actions, permutation groups and the wreath product; *Combinatorial Group Theory* for the Schreier graph of a subgroup, which is not rebuilt here but extended below to the action on a level of the tree; *Metric, Uniform and Complete Spaces* for the ultrametric of the boundary; *Topological Spaces* for the Cantor set; and *Profinite Groups and the Krull Topology* for the profinite topology, which is the topology that $\operatorname{Aut}(\mathcal{T})$ carries.

The article is the first of three. The **automata** that generate the self-similar actions, the **contracting** actions and their nuclei, and the **word and conjugacy problems** of the groups so generated are the subject of *Automaton and Contracting Groups*, written after this one. The **Schreier graphs** of the action on the levels, the **limit spaces** and the limit dynamical system are the subject of *Limit Spaces and Schreier Graphs*, written after that. The spectral theory of the Schreier graphs and the group algebra, the invariant measures on the boundary and the Perron–Frobenius theory of the recursion are Part III's, where the measure and the operator are available; the fractal dimension of a limit space is Part IV's. No physics is invoked.

## The Regular Rooted Tree

### The Tree

**Definition.** Let $X$ be a finite set, the **alphabet**, with $d = |X| \geq 2$ elements called **letters**. The set $X^*$ of finite words, including the **empty word** $\varnothing$, is the vertex set of the **regular rooted tree** $\mathcal{T} = \mathcal{T}(X)$: two words $v$ and $w$ are joined by an edge when $w = vx$ for a letter $x$, so that each word $v$ has the $d$ children $vx$, $x \in X$. The **root** is $\varnothing$, the **length** $|v|$ of a word is its distance from the root, and the **level** $n$, written $X^n$, is the set of words of length $n$. The **subtree** at $v$ is the tree $\mathcal{T}_v$ on the words with prefix $v$, with root $v$.

The tree, its classification as a graph, its distance and its automorphisms as a graph are those of *Graph Theory*. The **shift** at $v$ is the map $vw \mapsto w$; it is an isomorphism of rooted trees $\mathcal{T}_v \to \mathcal{T}$, and its inverse $w \mapsto vw$ identifies $\mathcal{T}$ with the subtree at $v$. This is the self-similarity of the tree itself, and it is what makes the sections below possible.

A **rooted tree** in general is a tree with a distinguished vertex, its vertices being partitioned into levels by their distance from the root; it is **spherically homogeneous** when all vertices of a level have the same number of children, and it is then determined by its **spherical index** $(d_0, d_1, \dots)$, where $d_n$ is the number of children of a vertex at level $n$. The regular tree $\mathcal{T}(X)$ is the spherically homogeneous tree of constant spherical index $(d, d, d, \dots)$. The weakly branch groups below live on spherically homogeneous trees; the sequel on limit spaces uses the regular case, and the tree is written $\mathcal{T}$ throughout.

### The Boundary of the Tree

**Definition.** The **boundary** $\partial\mathcal{T}$ is the set $X^{\omega}$ of infinite words $\xi = x_1x_2x_3\cdots$ in the alphabet $X$. For a finite word $v$ the **cylinder** is

$$
[v] = \{\xi \in X^{\omega} : \xi\ \text{begins with } v\},
$$

and the boundary is given the topology whose basis is the family of cylinders; a sequence of infinite words converges exactly when, for every bound $n$, the length-$n$ prefixes are eventually constant. The **level** of the boundary at a vertex $v$ is the cylinder $[v]$, and the cylinders $[v]$ over the words of a fixed length $n$ form a partition of $X^{\omega}$ into $d^n$ closed open sets.

**Proposition.** The boundary $\partial\mathcal{T}$ is a compact, perfect, totally disconnected metrisable space, hence a **Cantor space**: for $d \geq 2$ it is homeomorphic to the middle-thirds Cantor set of *Topological Spaces*. The cylinders are closed and open, they form a basis of cardinality $\aleph_0$, and the intersection $\bigcap_{n}[x_1\cdots x_n]$ of the cylinders along an infinite word is the single point $x_1x_2\cdots$.

**Proof sketch.** Given a covering of $X^{\omega}$ by cylinders, the finite intersection property applied to the complementary cylinders shows that finitely many already cover, so the space is compact; the complement of a cylinder is a finite union of cylinders, so a cylinder is closed and open, which gives total disconnectedness; and a cylinder with two distinct points contains a proper subcylinder, so the space is perfect. The comparison with the Cantor set is the standard result that a compact perfect totally disconnected metrisable space is a Cantor space, and the middle-thirds set is one.

**Definition.** The **ultrametric** of the boundary is

$$
d(\xi, \eta) = 2^{-n(\xi,\eta)}, \qquad n(\xi,\eta) = \sup\{n : x_i = y_i\ \text{for } i \leq n\},
$$

where $n(\xi,\eta)$ is the length of the longest common prefix, with $d(\xi,\xi) = 0$. It satisfies the ultrametric inequality $d(\xi,\zeta) \leq \max\{d(\xi,\eta), d(\eta,\zeta)\}$, its balls are the cylinders, and it is complete.

The distance of *Metric, Uniform and Complete Spaces* is placed on the boundary here; the ultrametric form is the one the tree supplies, and the two properties used below are that the balls are exactly the cylinders and that the space is compact. The boundary with its measure — the uniform measure that assigns to a cylinder $[v]$ the mass $d^{-|v|}$ — is a probability space, and the action of a self-similar group on it by measure-preserving transformations is the object whose ergodic theory and whose group-measure-space algebra belong to Part III; this article uses the boundary only as a compact topological space with the group action.

## Automorphisms and Sections

**Definition.** An **automorphism** of $\mathcal{T}$ is a bijection $g$ of $X^*$ with $g(\varnothing) = \varnothing$ that carries the edge $v \to vx$ to the edge $g(v) \to g(vx)$; then $g$ preserves the length, $|g(v)| = |v|$, and it carries the level $X^n$ onto itself. The automorphisms form a group $\operatorname{Aut}(\mathcal{T})$ under composition, written as a left action: $(gh)(v) = g(h(v))$.

**Definition (section).** Let $g \in \operatorname{Aut}(\mathcal{T})$ and let $v \in X^*$. Since $g$ maps the subtree $\mathcal{T}_v$ onto the subtree $\mathcal{T}_{g(v)}$ and the two are identified with $\mathcal{T}$ by the shifts, the map

$$
g|_v = \text{(shift at } g(v)) \circ g \circ \text{(shift at } v)^{-1}
$$

is an automorphism of $\mathcal{T}$, the **section** of $g$ at $v$. It is characterised by the identity

$$
g(vw) = g(v)\cdot g|_v(w) \qquad \text{for all } v, w \in X^*,
$$

the product being the concatenation of the words, and by the letter $x \in X$ read as the word of length one one has $g(xw) = g(x)\,g|_x(w)$.

**Proposition (the multiplication rule).** For $g, h \in \operatorname{Aut}(\mathcal{T})$ and $v \in X^*$,

$$
(gh)|_v = g|_{h(v)}\,h|_v .
$$

**Proof.** For every word $w$, $(gh)(vw) = g(h(vw)) = g\bigl(h(v)\,h|_v(w)\bigr) = g(h(v))\,g|_{h(v)}(h|_v(w))$, and the left side is $(gh)(v)\,(gh)|_v(w) = g(h(v))\,(gh)|_v(w)$; comparing gives the identity.

**Definition (the root permutation and the recursion).** Write $\sigma(g) \in \operatorname{Sym}(X)$ for the permutation of the letters that $g$ induces on the first level, $\sigma(g)(x) = g(x)$. Then

$$
g(xw) = \sigma(g)(x)\cdot g|_x(w) \qquad \text{for every } x \in X,\ w \in X^*,
$$

and $g$ is determined by the permutation $\sigma(g)$ and the $d$ sections $g|_x$, $x \in X$. One writes the **wreath recursion**

$$
g = \bigl(g|_0, g|_1, \dots, g|_{d-1}\bigr)\,\sigma(g),
$$

and the multiplication rule reads

$$
(gh)|_x = g|_{\sigma(h)(x)}\,h|_x, \qquad \sigma(gh) = \sigma(g)\,\sigma(h).
$$

**Example (the identity and the root swap).** The identity has $\sigma = \mathrm{id}$ and all sections equal to the identity. The automorphism $\varepsilon$ with $\sigma(\varepsilon)$ the transposition of the two letters of a binary alphabet and all sections the identity interchanges the two halves of the tree and is an involution: $\varepsilon^2 = \mathrm{id}$.

**Definition (portrait).** Let $\alpha_v = \sigma(g|_v) \in \operatorname{Sym}(X)$ be the permutation induced by the section at $v$. The family $(\alpha_v)_{v \in X^*}$ is the **portrait** of $g$; it determines $g$, since the action on an infinite word is read letter by letter,

$$
(a_1a_2a_3\cdots)^{\,g} = \alpha_{\varnothing}(a_1)\,\alpha_{a_1}(a_2)\,\alpha_{a_1a_2}(a_3)\cdots,
$$

and conversely every labelling of $X^*$ by permutations is the portrait of exactly one automorphism. The portraits therefore identify $\operatorname{Aut}(\mathcal{T})$ with the inverse limit of the groups $\operatorname{Aut}(\mathcal{T}_n)$ of automorphisms of the tree truncated at level $n$, the maps of the system being the restrictions; the **level-$n$ stabiliser** $\operatorname{St}_n$, the kernel of the restriction $\operatorname{Aut}(\mathcal{T}) \to \operatorname{Aut}(\mathcal{T}_n)$, is the set of automorphisms whose portrait vanishes on levels below $n$.

**Theorem.** With the topology of the inverse limit, $\operatorname{Aut}(\mathcal{T})$ is a profinite group; the level-$n$ stabilisers $\operatorname{St}_n$ are open normal subgroups of finite index forming a neighbourhood basis of the identity, and $\operatorname{Aut}(\mathcal{T})$ acts continuously on the boundary $\partial\mathcal{T}$.

**Proof sketch.** The restrictions $\operatorname{Aut}(\mathcal{T}) \to \operatorname{Aut}(\mathcal{T}_n)$ are onto, because a permutation of the words of a finite rooted tree extends to the tree by acting trivially below level $n$; the kernels $\operatorname{St}_n$ are nested with trivial intersection, so $\operatorname{Aut}(\mathcal{T})$ is a subdirect product of the finite groups $\operatorname{Aut}(\mathcal{T}_n)$ and hence a closed subgroup of their product. The topology is that of *Profinite Groups and the Krull Topology*, and continuity of the action on $X^{\omega}$ is the statement that the stabiliser of a cylinder is open.

**Remark.** Because of the portrait, an automorphism of the tree is not a mysterious object: it is a labelling of the tree by permutations of the alphabet, and the composition is the rule $\alpha$ of the left vertex followed by the $\sigma(h)$-image of the label of the right one. Everything below is a condition on the portraits of the elements of a subgroup.

## Self-Similar Actions

**Definition.** A subgroup $G \leq \operatorname{Aut}(\mathcal{T})$ is **self-similar** if $g|_v \in G$ for every $g \in G$ and every $v \in X^*$. Equivalently: the action of $G$ on $X^*$ by automorphisms is **self-similar** if the set of all sections of its elements is contained in $G$; by the multiplication rule it is enough to check the sections $s|_x$ of the elements $s$ of a generating set, and it is enough to check the vertices of length one at every level, that is, that each section of each generator lies in $G$.

**Theorem (the wreath recursion).** Let $G \leq \operatorname{Aut}(\mathcal{T})$ be self-similar. The map

$$
G \to G \wr \operatorname{Sym}(X) = G^{X} \rtimes \operatorname{Sym}(X), \qquad g \mapsto \bigl((g|_x)_{x \in X}, \sigma(g)\bigr),
$$

is an injective group homomorphism, so that $G$ embeds in its own permutational wreath product. Iterating the recursion one has, for every $n$, an embedding

$$
G \hookrightarrow G \wr \operatorname{Aut}(\mathcal{T}_n),
$$

where the finite group $\operatorname{Aut}(\mathcal{T}_n)$ acts on the level $X^n$.

**Proof.** The multiplication rules of the sections and of the root permutation are exactly the multiplication in the semidirect product $G^{X} \rtimes \operatorname{Sym}(X)$, with $\operatorname{Sym}(X)$ acting on the $d$ coordinates $G$; injectivity holds because an element with all sections trivial and trivial root permutation acts trivially, which is read on the portraits. The iterated statement follows by applying the recursion to the sections, which are again elements of $G$.

The wreath product is that of *Infinite Groups*. The recursion is what the name records: a self-similar group is a subgroup of its own wreath product, and the elements of $G$ are obtained from the elements in the subtrees by the same rule that defines the group.

**Definition (virtual endomorphism and recurrence).** Let $G$ be self-similar and let $x \in X$. Let $\operatorname{St}(x) = \{g \in G : g(x) = x\}$ be the stabiliser of the vertex $x$. The map

$$
\varphi_x : \operatorname{St}(x) \to G, \qquad \varphi_x(g) = g|_x,
$$

is a group homomorphism, the **virtual endomorphism** of the action at $x$, from a finite-index subgroup of $G$ into $G$. The action is **recurrent** if $\varphi_x$ is onto for every $x$; it is **self-replicating** if for every $x, y \in X$ and every $h \in G$ there is $g \in G$ with $g(x) = y$ and $g|_x = h$.

**Proposition.** A self-replicating action is recurrent, and it is level-transitive: for every $n$ the action of $G$ on $X^n$ is transitive. Conversely a level-transitive self-similar action in which every $\varphi_x$ is onto is self-replicating.

**Proof.** Given $x$ and $h$, self-replication with $y = x$ gives $g \in \operatorname{St}(x)$ with $g|_x = h$, so $\varphi_x$ is onto. For transitivity, self-replication with $h$ the identity gives an element carrying $x$ to $y$; applying this at each level gives a word of elements carrying a given vertex to a prescribed one. The converse is the same unfolding, using that the stabiliser of a vertex acts transitively on its children by recurrence.

**Remark.** The hypotheses are not automatic. A self-similar group need not be level-transitive — the trivial group is self-similar — and it need not be recurrent. The classes that carry the theory are the level-transitive self-replicating self-similar groups, and they are the **fractal groups**: the group is determined by the recursion at every level, acts transitively on each level, and its sections reproduce the whole group. All the examples below are level-transitive; the adding machine, the dihedral group, the Grigorchuk group and the group of the Sierpiński gasket are in addition recurrent and self-replicating, while the lamplighter group below is level-transitive and self-similar yet not contracting.

**Definition (level-transitivity and spherical homogeneity).** A self-similar group $G$ is **level-transitive** if its action on $X^n$ is transitive for every $n$. When the tree is only spherically homogeneous, the definition is the same verbatim and the letter set varies from level to level; a spherically homogeneous tree with spherical index $(d_n)$ carries the same theory, and the level-$n$ stabilisers and the rigid stabilizers below are defined in the same way. The regular case is the one whose boundary is a Cantor space with the uniform measure of Part III, and the sequel restricts to it where a limit space is built.

## The Standard Examples

### The Adding Machine

**Definition.** On the binary alphabet $X = \{0,1\}$ let $a$ be the automorphism with

$$
a(0w) = 1\,w, \qquad a(1w) = 0\,a(w) \qquad (w \in X^*),
$$

that is, $a = (\mathrm{id}, a)\,\varepsilon$ in the recursion, with $\varepsilon$ the transposition of the letters and sections the identity at $0$ and $a$ at $1$. The group $\langle a \rangle$ is the **adding machine** group, also called the **odometer**.

**Theorem.** The group $\langle a\rangle$ is infinite cyclic, and the action is level-transitive and self-replicating. The power $a^k$ acts trivially on the level $n$ exactly when $2^n$ divides $k$; in particular $a^{2^n}$ is the first power that fixes the level $n$, and $a$ has infinite order.

**Proof sketch.** Reading $\xi \in X^{\omega}$ as the dyadic number $\sum_i x_i 2^{i-1}$, the recursion gives $a(\xi) = \xi + 1$ in the $2$-adic integers, whence the statement about the powers: adding $1$ exactly $2^n$ times is adding $2^n$, which changes nothing modulo $2^n$, that is, on the first $n$ digits, while $a^{k}$ with $0 < k < 2^n$ moves some word of length $n$ by the standard carry. Transitivity on $X^n$ is the statement that the residues modulo $2^n$ are all reached, and self-replication is by the recursion. The computations quoted were verified on the levels up to six.

**Example (the portraits).** The portrait of $a$ has the transposition at the root, the identity along the left spine, and the transposition again at every vertex of the right spine; the adding machine is thus the automorphism that adds one, and it is the standard example of *Metric, Uniform and Complete Spaces* for the $p$-adic integers specialised to the boundary of the binary tree.

### The Infinite Dihedral Group

**Definition.** On the binary alphabet let $t(0w) = 1w$ and $t(1w) = 0w$, the root swap with trivial sections, and let $b$ be defined by

$$
b(0w) = 0\,a(w), \qquad b(1w) = 1\,b(w),
$$

that is, $b = (a, b)$ in the recursion, where $a$ is the adding machine. The group $\langle t, b\rangle$ is the **infinite dihedral group** generated by the two involutions $t$ and $b$.

**Theorem.** $t^2 = b^2 = 1$, the product $tb$ has infinite order, and $\langle t,b\rangle \cong D_{\infty} = \mathbb{Z} \rtimes \mathbb{Z}/2$; the action is level-transitive and self-replicating.

**Proof sketch.** The recursion gives $b^2 = (a^2, b^2)$ and $a^2 = 1$, so $b^2$ acts trivially and $b$ is an involution; $t$ is an involution by definition; and the section of $tb$ at a letter is a conjugate of $a$, so no power of $tb$ is trivial on a sufficiently deep level. The verification on the levels up to six confirms the relations.

The dihedral group is the second standard example and reappears as a limit space in the third article, where its limit space is the segment.

### The Grigorchuk Group

**Definition.** On the binary alphabet let $a$ be the root swap with trivial sections, and let $b, c, d$ be the automorphisms with trivial root permutation and sections

$$
b = (a, c), \qquad c = (a, d), \qquad d = (\mathrm{id}, b).
$$

The **Grigorchuk group** is $G = \langle a, b, c, d\rangle \leq \operatorname{Aut}(\mathcal{T})$.

**Theorem (relations).** The elements $a, b, c, d$ satisfy

$$
a^2 = b^2 = c^2 = d^2 = 1, \qquad bc = d, \qquad bd = c, \qquad cd = b ,
$$

so that $\langle b, c, d\rangle \cong (\mathbb{Z}/2)^2$; the group is generated by $a$ and any two of $b, c, d$, for instance $G = \langle a, b, c\rangle$; and $b, c, d$ fix the first level while $a$ interchanges the two subtrees.

**Proof sketch.** Each of the four recursions is checked directly: $a^2 = 1$ because the swap squares to the identity and its sections are trivial; $b^2 = (a^2, c^2) = (1, c^2)$ and $c^2 = (a^2, d^2) = (1, d^2)$ and $d^2 = (1, b^2)$, which iterate to the identity; and $bc = (a\cdot a, c\cdot d) = (1, d) = d$ with the same computation for the other products. The verification on the levels up to six confirms all of them, together with $bcd = 1$.

**Theorem (properties).** The Grigorchuk group is infinite, it is a torsion group in which every element has order a power of two, it is residually finite and just infinite, it is amenable but not elementary amenable, and it is not finitely presented. Its action is level-transitive and self-replicating, and it is a branch group in the sense of the last section.

The growth of the group is intermediate, which is what makes it the counterexample to the generalised Milnor problem. With respect to a finite generating set the volume growth function of *Geometric Group Theory*, $v_{G,S}(n) = \#\{g \in G : |g|_S \leq n\}$, is neither polynomial nor exponential, and

$$
\lim_{n \to \infty} \frac{\log\log v_{G,S}(n)}{\log n} = \alpha_0 = \frac{\log 2}{\log\lambda_0} \approx 0.7674,
$$

where $\lambda_0$ is the positive root of $X^3 - X^2 - 2X - 4 \approx 2.4675$; this is the theorem of Erschler and Zheng, and the corresponding upper bound is due to Bartholdi. The growth is therefore $\exp\bigl(n^{\alpha_0 + o(1)}\bigr)$, strictly between polynomial and exponential, and it is the same for every finite generating set because the growth type is a quasi-isometry invariant. The intermediate growth is visible from the tree: a section of a long word is shorter than the word, because the four sections of the generators lie in the five-element set $\{1, a, b, c, d\}$, and the recursion therefore shrinks the word length — the **contraction** that the next article turns into an algorithm. The amenability and the failure of elementary amenability are those of *Amenable Groups*, where the group is the example showing that the class of elementary amenable groups is strictly smaller than the amenable class.

**Remark.** The Grigorchuk group shows that the portrait description is not an ornament. The relations have no interpretation in the abstract presentation of the group — the group is not finitely presented, and its defining relations of Lysënok form an infinite recursive family — while in the recursion they are three lines, because the recursion is the structure that makes the group act on the tree.

### The Lamplighter Group

**Definition.** On the binary alphabet let $p$ and $q$ be the automorphisms

$$
p = (q, p)\,\varepsilon, \qquad q = (q, p),
$$

with $\varepsilon$ the root swap. Then $p$ is the root swap with sections $q$ at $0$ and $p$ at $1$, and $q$ fixes the root with sections $q$ at $0$ and $p$ at $1$.

**Theorem.** The group $\langle p, q\rangle$ is the **lamplighter group** $(\mathbb{Z}/2)^{\mathbb{Z}} \rtimes \mathbb{Z}$ of *Infinite Groups*; the action is self-similar and level-transitive, and it is not contracting. It is the standard example showing that self-similarity and level-transitivity alone do not force the contraction of the next article.

**Proof sketch.** The identification with the lamplighter group is that of *From fractal groups to fractal sets*: the boundary is read as the formal power series $\xi = x_1x_2\cdots \mapsto \sum_i x_i t^{i-1}$ over $\mathbb{Z}/2$, the generators act on it as the addition of $1$ together with the shift of the base, and the group generated is the semidirect product of the finitely supported configurations with that shift. Level-transitivity is visible one level down: $p$ is the transposition at the root, so on the second level it is the four-cycle $(00\ 10\ 01\ 11)$, and the transitivity on the levels up to six was verified directly. The action is not contracting: the sections of a product are products of sections, so the sections of the elements of the group generate new elements and no finite set can contain them all, which is what the criterion of the next article asks.

The verification of the recursion confirms that $p$ and $q$ have infinite order; the failure of level-transitivity is read off the action on the $2$-adic integers, where the coordinate $x_1$ is preserved by both generators.

### The Group of the Sierpiński Gasket

**Definition.** Let the alphabet be $X = \{0,1,2\}$ and let $\sigma_{ij}$ be the transposition of the letters $i$ and $j$. Let

$$
b_0 = (b_0, 1, 1)\,\sigma_{12}, \qquad b_1 = (1, b_1, 1)\,\sigma_{02}, \qquad b_2 = (1, 1, b_2)\,\sigma_{01},
$$

the identity being written $1$ in the sections.

**Theorem.** Each $b_i$ is an involution, the three act transitively on the first level, and the group $G_{\triangle} = \langle b_0, b_1, b_2\rangle$ is level-transitive and self-replicating. Its limit space is the Sierpiński gasket, the object computed in *Limit Spaces and Schreier Graphs*.

The verification on the ternary tree confirms the three relations $b_i^2 = 1$ on the levels up to four; the transitivity on the first level is the definition of the root permutations, which are the three transpositions, and self-replication is read from the sections, each of which is a generator or the identity. The group is one of the standard examples of the theory, and its portrait is the pattern of the gasket: the letter that a generator fixes has trivial section, the two others have the generator itself on the diagonal.

### The Gupta–Sidki Groups

**Definition.** Let $p$ be a prime and let the alphabet have $p$ letters. The **Gupta–Sidki groups** are the groups generated by a cyclic permutation of the first level and one automorphism with trivial root permutation whose sections are powers of the first generator; the smallest case is the $2$-generated group on the ternary tree.

**Theorem.** The Gupta–Sidki groups are infinite finitely generated torsion groups, they are level-transitive, self-replicating, branch and just infinite, and they are contracting. They are the earliest examples, after the Grigorchuk group, of the phenomena above, and they are the source of the standard counterexamples on the Burnside problem.

The exact recursion is a convention of the literature and is not reproduced here; the properties quoted are those of Gupta and Sidki, and the contraction is the one used in *Automaton and Contracting Groups*, where the group reappears as the automaton generating it.

## Branch Groups

**Definition.** Let $G \leq \operatorname{Aut}(\mathcal{T})$ act by automorphisms of a spherically homogeneous tree and be level-transitive. The **vertex stabiliser** of a vertex $v$ is $G_v = \{g \in G : g(v) = v\}$, and the **rigid stabiliser** $\operatorname{Rist}_G(v)$ is the set of elements of $G$ that fix every vertex outside the subtree $\mathcal{T}_v$:

$$
\operatorname{Rist}_G(v) = \{g \in G : g(w) = w\ \text{for every } w \notin X^*v\}.
$$

The **level-$n$ rigid stabiliser** is the subgroup $\operatorname{Rist}_G(n)$ generated by the rigid stabilisers of the vertices of level $n$; it is their direct product, because the subtrees of the level are disjoint.

**Definition.** The group $G$ is

**(a)** **weakly branch** if no rigid stabiliser $\operatorname{Rist}_G(v)$ is trivial;

**(b)** **branch** if $\operatorname{Rist}_G(n)$ has finite index in $G$ for every $n$;

**(c)** **tough** if it is not weakly branch; and

**(d)** **regular branch** if there is a subgroup $K \leq G$ of finite index with $K^X \leq K$ under the inclusion induced by the sections, and **regular weakly branch** if such a $K \neq 1$ exists without the finite-index requirement.

**Proposition.** In a weakly branch group every rigid stabiliser is infinite, and in a tough group the level-$n$ rigid stabiliser is trivial for all sufficiently large $n$. A branch group is weakly branch.

**Proof sketch.** A branch group is weakly branch: $\operatorname{Rist}_G(n)$ has finite index in the infinite group $G$, hence is nontrivial, so some $\operatorname{Rist}_G(v)$ is nontrivial, and the conjugates of that stabilizer under the level-transitive action are the rigid stabilizers of the other vertices of the level, the same argument applied inside the subtree at $v$ giving the nontriviality below $v$. In a weakly branch group a nontrivial rigid stabilizer is infinite, because it contains a copy of a nontrivial rigid stabilizer of a deeper level; and a tough group has all sufficiently deep rigid stabilizers trivial, since otherwise the disjoint supports give an infinite direct sum of nontrivial subgroups with a finite-index intersection, which the next section's finite-index condition forbids.

**Theorem.** The Grigorchuk group is a branch group; so are the Gupta–Sidki groups and the group of the Sierpiński gasket. Every branch group is just infinite, and the rigid stabilisers of a branch group are infinite.

**Proof sketch.** The Grigorchuk group is level-transitive, and its recursion shows that the level-$n$ rigid stabilizer is large: it contains the $n$-th level stabiliser of a finite-index subgroup, so its index in $G$ is finite; the argument is by induction on the recursion and is the one that proves the congruence subgroup property of the group. The just-infiniteness is then a general theorem on branch groups, quoted.

**Remark.** The definitions line up with the recursion: a branch group is a group that is self-similar in a strong sense, namely one in which the product of the groups acting on the subtrees of a level has finite index in the group. The weakly branch groups are the same without the finite index, and the example of the next article — the Basilica group — is weakly branch without being branch. The classes are the natural home of the intermediate-growth example, and their theory is the algebraic side of the tree that the sequel turns into Schreier graphs, automata and limit spaces.

## Summary

A regular rooted tree on an alphabet $X$ has for vertices the finite words in $X$, and an automorphism of it is determined by a permutation of the first level and one section at each letter, the **wreath recursion** $g = (g|_0,\dots,g|_{d-1})\,\sigma(g)$. The sections multiply by $(gh)|_v = g|_{h(v)}h|_v$, and the portrait of an automorphism is the labelling of the tree by the permutations of its sections; with the inverse limit topology $\operatorname{Aut}(\mathcal{T})$ is a profinite group acting on the Cantor space $X^{\omega}$ of infinite words. A subgroup $G$ is **self-similar** when the section of every element at every vertex lies in $G$, which is exactly the condition that $G$ embeds in its own permutational wreath product $G \wr \operatorname{Sym}(X)$; the action is level-transitive when it is transitive on each level, recurrent when the virtual endomorphisms $\varphi_x(g) = g|_x$ are onto, and self-replicating when the sections at a vertex fill the whole group. A level-transitive recurrent self-similar group is a **fractal group**.

The examples are the adding machine $\langle a\rangle \cong \mathbb{Z}$, whose power $a^k$ fixes the level $n$ exactly when $2^n$ divides $k$; the infinite dihedral group $\langle t, b\rangle$, generated by two involutions whose product has infinite order; the Grigorchuk group $G = \langle a, b, c, d\rangle$ with $a^2 = b^2 = c^2 = d^2 = 1$ and $bc = d$, $bd = c$, $cd = b$, a branch, just infinite, amenable but not elementary amenable torsion group of intermediate growth, whose volume growth satisfies $\lim_{n}\log\log v(n)/\log n = \log2/\log\lambda_0 \approx 0.7674$ with $\lambda_0$ the positive root of $X^3-X^2-2X-4$; the lamplighter group $(\mathbb{Z}/2)^{\mathbb{Z}} \rtimes \mathbb{Z}$, self-similar and level-transitive but not contracting; the group of the Sierpiński gasket, generated by three involutions on the ternary tree; and the Gupta–Sidki groups, the torsion groups that establish the Burnside counterexamples.

A level-transitive group is **weakly branch** when no rigid stabiliser is trivial and **branch** when the product of the rigid stabilisers of a level has finite index; the Grigorchuk group, the Gupta–Sidki groups and the group of the Sierpiński gasket are branch, and every branch group is just infinite. What is deferred is stated: the automata, the contraction and the word problem are the subject of *Automaton and Contracting Groups*; the Schreier graphs and the limit spaces are the subject of *Limit Spaces and Schreier Graphs*; the measures on the boundary, the spectral theory and the operator algebras are Part III's, and the fractal dimension of a limit space is Part IV's.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X$, $d = \vert X\vert$, $x$ | The alphabet, its cardinality and a letter |
| $X^*$, $\varnothing$, $X^n$ | Finite words, the empty word and the root, the level $n$ |
| $\mathcal{T}$, $\mathcal{T}_v$ | The regular rooted tree and the subtree at the vertex $v$ |
| $\partial\mathcal{T} = X^{\omega}$ | The boundary of the tree, a Cantor space |
| $[v]$ | The cylinder of infinite words with prefix $v$ |
| $d(\xi,\eta) = 2^{-n(\xi,\eta)}$ | The ultrametric of the boundary, $n$ the length of the longest common prefix |
| $\operatorname{Aut}(\mathcal{T})$, $\operatorname{Aut}(\mathcal{T}_n)$ | The automorphisms of the tree and of its truncation at level $n$ |
| $g\|_v$ | The section of $g$ at $v$, with $g(vw) = g(v)\,g\|_v(w)$ |
| $(gh)\|_v = g\|_{h(v)}h\|_v$ | The multiplication rule of the sections |
| $\sigma(g)$, $\alpha_v$ | The root permutation of $g$; the portrait permutation at $v$ |
| $g = (g\|_0,\dots,g\|_{d-1})\,\sigma(g)$ | The wreath recursion |
| $G \hookrightarrow G \wr \operatorname{Sym}(X)$ | A self-similar group is a subgroup of its own wreath product |
| $\operatorname{St}(x)$, $\operatorname{St}_n$ | The stabiliser of the vertex $x$ and of the level $n$ |
| $\varphi_x(g) = g\|_x$ | The virtual endomorphism at $x$; the action is recurrent when it is onto |
| self-replicating | For all $x,y,h$ there is $g$ with $g(x) = y$ and $g\|_x = h$ |
| $G_v$, $\operatorname{Rist}_G(v)$, $\operatorname{Rist}_G(n)$ | Vertex stabiliser; rigid stabiliser of $v$; level-$n$ rigid stabiliser |
| weakly branch, branch, regular branch | No trivial rigid stabiliser; $\operatorname{Rist}_G(n)$ of finite index; the subgroup $K$ with $K^X \leq K$ |
| $G = \langle a,b,c,d\rangle$ | The Grigorchuk group, with $b = (a,c)$, $c = (a,d)$, $d = (\mathrm{id},b)$ |
| $a = (\mathrm{id},a)\varepsilon$, $t = (\mathrm{id},\mathrm{id})\varepsilon$ | The adding machine and the root swap |
| $G_{\triangle} = \langle b_0,b_1,b_2\rangle$ | The group of the Sierpiński gasket on the ternary tree |

## Further Reading

- Rostislav I. Grigorchuk, *On the Milnor problem of group growth*, Doklady Akademii Nauk SSSR **271** (1983), 30–33, for the group of intermediate growth.
- Rostislav I. Grigorchuk, *Just infinite branch groups*, in *New Horizons in pro-$p$ Groups* (Birkhäuser, 2000), 121–179, for the branch and weakly branch groups and their rigid stabilizers.
- Rostislav I. Grigorchuk, *Degrees of growth of finitely generated groups and the theory of invariant means*, Izvestiya Akademii Nauk SSSR **48** (1984), 939–985, for the amenability and the growth.
- Narain Gupta and Said Sidki, *On the Burnside problem for periodic groups*, Mathematische Zeitschrift **182** (1983), 385–388, for the Gupta–Sidki groups.
- Igor G. Lysënok, *A set of defining relations for the Grigorchuk group*, Matematicheskie Zametki **38** (1985), 503–516, for the infinite presentation of the group.
- Volodymyr Nekrashevych, *Self-similar groups*, Mathematical Surveys and Monographs **117** (American Mathematical Society, 2005), for the systematic treatment of sections, wreath recursions, portraits, branch groups and the limit spaces.
- Rostislav Grigorchuk, Volodymyr Nekrashevych and Vitaly Sushchansky, *From fractal groups to fractal sets*, in *Fractals in Graz 2001* (Birkhäuser, 2003), 25–118, for the survey that fixes the definitions of the self-similar action, the branch group and the limit space.
- Anna Erschler and Tianyi Zheng, *Growth of periodic Grigorchuk groups*, Inventiones Mathematicae **219** (2020), 1069–1155, for the existence and the value of the growth exponent.
- Laurent Bartholdi, *The growth of Grigorchuk's torsion group*, International Mathematics Research Notices **1998** (1998), 1049–1054, for the upper bound on the growth.
- James E. Humphreys, *A Course in the Theory of Groups*, 2nd ed. (Springer, 1996), for the wreath products and the profinite completions used here.
