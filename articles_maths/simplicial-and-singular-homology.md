
# __Simplicial and Singular Homology__

## Introduction

The fundamental group of *The Fundamental Group and Covering Spaces* is an invariant of a space that is easy to define and hard to compute, and it is not abelian. **Homology** replaces it by a sequence of abelian groups, one in each degree, which are computable from a chain complex and which are the natural home of the machinery — exact sequences, excision, the Künneth formula — that makes algebraic topology a computational subject. A chain complex is an algebraic object of Part I: a sequence of abelian groups with maps $\partial_n$ satisfying $\partial_{n-1}\partial_n = 0$, exactly as in *Exact Sequences* and the planned *Homological Algebra*. Homology is its derived invariant, and the present article attaches such a complex to a space, first combinatorially and then, in full generality, by taking chains to be formal sums of continuous maps of simplices.

Two constructions are given. **Simplicial homology** is defined for a simplicial complex, a space built from genuine simplices glued along faces, and it is finite and computable: the chain groups are free of rank equal to the number of $n$-simplices, and the boundary is read from incidence. **Singular homology** is defined for every topological space: the $n$-chains are the formal sums of all continuous maps $\Delta_n \to X$, so the construction is manifestly invariant, at the cost of enormous chain groups; the reward is that functoriality, homotopy invariance, excision and the long exact sequence of a pair are all formal consequences of the definitions. The two theories agree on the spaces where both are defined, and for a CW complex both agree with the cellular homology of *CW Complexes and Cellular Approximation*.

The companion article *CW Complexes and Cellular Approximation* supplies the cell structures, the homotopy extension property and the cellular boundary formula, all of which are used here. The homological algebra — exact sequences, the snake lemma, the five lemma, chain homotopy — is that of *Exact Sequences*, and the general theory of chain complexes over a ring is the planned *Homological Algebra* of Part I, written in parallel; it is cited for the algebraic constructions and not restated. Coefficients are taken in a commutative ring $R$ with identity $1 \neq 0$, so that $H_n(X;R)$ is an $R$-module; the default $R = \mathbb{Z}$ gives abelian groups, and the case of a general coefficient module is not covered here. **Reduced homology** is written $\tilde H_n$.

## Simplicial Complexes

### Simplices and Complexes

**Definition.** Let $v_0, \ldots, v_n$ be points of $\mathbb{R}^N$ in general position, meaning that the vectors $v_1 - v_0, \ldots, v_n - v_0$ are linearly independent. The **$n$-simplex** they span is the convex set

$$
\sigma = [v_0, \ldots, v_n] = \Bigl\{\textstyle\sum_{i=0}^n t_i v_i : t_i \geq 0, \ \sum_{i=0}^n t_i = 1\Bigr\},
$$

and the $v_i$ are its **vertices**. A **face** of $\sigma$ is the simplex spanned by a nonempty subset of the vertices, and a **proper face** is one spanned by a proper subset; the faces of dimension $n-1$ are the **facets**. The **standard $n$-simplex** is

$$
\Delta_n = [e_0, \ldots, e_n] \subseteq \mathbb{R}^{n+1},
$$

spanned by the standard basis vectors.

The barycentric coordinates $t_i$ are unique, so a point of $\sigma$ determines the $t_i$, and a continuous map out of a simplex is continuous exactly when it is continuous in these coordinates.

**Definition.** A **simplicial complex** is a set $K$ of simplices in some $\mathbb{R}^N$ such that every face of a simplex of $K$ is in $K$, and the intersection of two simplices of $K$ is either empty or a common face of both. The **underlying space** $|K|$ is the union of the simplices with the subspace topology, and its **dimension** is the supremum of the dimensions of the simplices of $K$. A simplicial complex is **finite** when it has finitely many simplices.

Condition on intersections is what prevents two simplices from meeting in a partial face; it makes $|K|$ a CW complex whose cells are the interiors of the simplices.

**Proposition.** If $K$ is a simplicial complex, then $|K|$ is a CW complex with one cell for each simplex of $K$, and the weak topology of the CW structure agrees with the subspace topology of $|K|$ inside $\mathbb{R}^N$.

*Proof.* A simplex is homeomorphic to a disc, and its faces are its boundary; the intersection condition ensures that the attaching maps agree on overlaps, and the subspace topology is the weak topology because a closed subset of a finite union of simplices is closed in each. $\square$

### Oriented Simplices and the Boundary

**Definition.** An **orientation** of an $n$-simplex $\sigma = [v_0,\ldots,v_n]$ is an equivalence class of orderings of its vertices, two orderings being equivalent when they differ by an even permutation. An **oriented simplex** is written $[v_0,\ldots,v_n]$ with the given ordering, and $[v_{\pi(0)},\ldots,v_{\pi(n)}] = \operatorname{sgn}(\pi)[v_0,\ldots,v_n]$.

**Definition.** For $n \geq 1$ the **boundary** of an oriented $n$-simplex is the formal sum of its oriented facets

$$
\partial[v_0,\ldots,v_n] = \sum_{i=0}^n (-1)^i [v_0,\ldots,\hat v_i,\ldots,v_n],
$$

where the hat omits the vertex; for $n = 0$ the boundary is $0$.

**Lemma.** $\partial \partial = 0$ on oriented simplices.

*Proof.* The terms of $\partial\partial[v_0,\ldots,v_n]$ are indexed by ordered pairs $i < j$; omitting $v_i$ then $v_j$ gives sign $(-1)^i(-1)^j$ and omitting $v_j$ then $v_i$ gives sign $(-1)^{j-1}(-1)^i$, and the two terms are the same oriented simplex with opposite signs, so they cancel. $\square$

This is the single computation that makes homology a functor; it is the simplicial instance of the general fact that a chain complex is a differential graded module, treated in the planned *Differential Graded Algebras* of Part I.

### Simplicial Homology

**Definition.** Let $K$ be a simplicial complex and $R$ a commutative ring with $1 \neq 0$. The **simplicial chain module** $C_n(K;R)$ is the free $R$-module on the oriented $n$-simplices of $K$, with the relation that reversing an orientation negates the generator; the boundary extends $R$-linearly to $\partial_n : C_n(K;R) \to C_{n-1}(K;R)$, and $\partial^2 = 0$. The **simplicial homology** is

$$
H_n^{\Delta}(K;R) = \ker \partial_n / \operatorname{im}\partial_{n+1},
$$

and its elements are **homology classes**; a chain with zero boundary is a **cycle**, a chain in the image of $\partial$ is a **boundary**, so homology is cycles modulo boundaries.

**Example.** For the boundary of a triangle, $K$ the three edges of a $2$-simplex, $C_1$ is free on three oriented edges and $C_0$ on three vertices. The cycle $[v_0v_1] + [v_1v_2] + [v_2v_0]$ has zero boundary and is not a boundary, so $H_1 \cong R$; the space is a circle.

**Example.** For the torus realised as a simplicial complex, the minimal triangulation has $7$ vertices, $21$ edges and $14$ triangles, so the chain groups have ranks $7$, $21$, $14$; the alternating sum is $7 - 21 + 14 = 0 = \chi$, twice the number of edges is thrice the number of triangles, as a closed surface requires, and the homology is $H_0 \cong R$, $H_1 \cong R^2$, $H_2 \cong R$. In the minimal cell structure instead, with one $0$-cell, two $1$-cells and one $2$-cell, the count is $1 - 2 + 1 = 0$; the two computations agree because the Euler characteristic is an invariant of the space.

**Remark.** Simplicial homology is computable but not invariant by construction: two simplicial complexes with homeomorphic underlying spaces need not have the same chain complex. The invariance is supplied by passing to singular homology, to which the article now turns, and then by the theorem that the two agree.

## Singular Homology

### Singular Chains

**Definition.** Let $X$ be a topological space and let $\Delta_n = [e_0,\ldots,e_n]$ be the standard $n$-simplex. A **singular $n$-simplex** of $X$ is a continuous map $\sigma : \Delta_n \to X$; it is singular in that it need not be injective or piecewise linear. The **singular $n$-chain module** with coefficients in $R$ is the free $R$-module on the set of singular $n$-simplices,

$$
C_n(X;R) = \bigoplus_{\sigma : \Delta_n \to X} R\,\sigma,
$$

the direct sum over all continuous maps.

**Definition.** The $i$-th **face map** is $\delta^i : \Delta_{n-1} \to \Delta_n$, the affine map sending $e_j$ to $e_j$ for $j < i$ and to $e_{j+1}$ for $j \geq i$; it identifies $\Delta_{n-1}$ with the facet opposite $e_i$. The **boundary** of a singular simplex is

$$
\partial_n(\sigma) = \sum_{i=0}^n (-1)^i\, \sigma \circ \delta^i,
$$

extended $R$-linearly, and $\partial_0 = 0$.

**Lemma.** $\partial_{n-1} \circ \partial_n = 0$.

*Proof.* The composite is the sum over pairs $i,j$ of $(-1)^{i+j}\sigma \circ \delta^i \circ \delta^j$. The identities $\delta^i \delta^j = \delta^j \delta^{i-1}$ for $j < i$ pair the terms with $j < i$ against those with $j > i$, and the signs are opposite; the terms with $i = j$ do not occur since $\delta^i \delta^i$ is not defined. $\square$

**Definition.** The **singular chain complex** is the pair $(C_*(X;R), \partial_*)$; the **singular homology** is

$$
H_n(X;R) = \ker\partial_n / \operatorname{im}\partial_{n+1}.
$$

A space $X$ with $H_n(X;R) = 0$ for all $n \geq 1$ and $H_0(X;R) \cong R$ is **acyclic** over $R$.

**Definition (reduced homology).** Let $\varepsilon : C_0(X;R) \to R$ be the **augmentation** sending every singular $0$-simplex to $1$. The **reduced chain complex** is obtained by adjoining $R$ in degree $-1$ with $\varepsilon$ as the boundary, and its homology is the **reduced homology** $\tilde H_n(X;R)$, so $\tilde H_n = H_n$ for $n \geq 1$ and $\tilde H_0 \cong H_0 \oplus R / (\text{image of } \varepsilon)$; for nonempty $X$, $\tilde H_0(X;R)$ is the kernel of $\varepsilon$ on cycles.

### Functoriality

**Theorem.** A continuous map $f : X \to Y$ induces a chain map $f_\# : C_*(X;R) \to C_*(Y;R)$ by $f_\#(\sigma) = f \circ \sigma$, and hence homomorphisms $f_* : H_n(X;R) \to H_n(Y;R)$. The assignments satisfy $(g \circ f)_* = g_* f_*$ and $(\mathrm{id}_X)_* = \mathrm{id}$, so $H_n(-;R)$ is a functor from topological spaces to $R$-modules.

*Proof.* The chain map property is $f_\# \partial(\sigma) = \sum_i (-1)^i f \sigma \delta^i = \partial f_\#(\sigma)$, an identity of maps; a chain map induces a map on homology because it carries cycles to cycles and boundaries to boundaries. The functorial identities are immediate from associativity of composition. $\square$

**Definition.** A **chain homotopy** between chain maps $\varphi, \psi : C_* \to D_*$ is a family of maps $P_n : C_n \to D_{n+1}$ with $\psi_n - \varphi_n = \partial^D_{n+1} P_n + P_{n-1}\partial^C_n$. Chain-homotopic chain maps induce the same map on homology, since $P$ carries cycles to boundaries.

**Theorem (homotopy invariance).** If $f, g : X \to Y$ are homotopic then the induced chain maps are chain homotopic, so $f_* = g_*$; consequently a homotopy equivalence induces an isomorphism on homology.

*Proof.* Let $F : X \times I \to Y$ be the homotopy. For a singular $n$-simplex $\sigma$, the maps $\Delta_n \to X \times I$, $x \mapsto (\sigma(x), 0)$ and $x \mapsto (\sigma(x),1)$, and the prism $\Delta_n \times I$ is triangulated into $(n+1)$-simplices; the standard subdivision determines $P_n(\sigma)$ as the alternating sum of the restrictions of $F \circ (\sigma \times \mathrm{id})$, and the identity $\partial P + P \partial = g_\# - f_\#$ is checked simplex by simplex. $\square$

**Remark.** Homotopy invariance is what makes homology an invariant of the homotopy type, as the fundamental group is; the two are related by the Hurewicz theorem.

## The Long Exact Sequence and Excision

### Relative Homology

**Definition.** For a subspace $A \subseteq X$ the **relative chain complex** is the quotient $C_*(X,A;R) = C_*(X;R)/C_*(A;R)$, and the **relative homology** is $H_n(X,A;R) = H_n(C_*(X,A;R))$. The short exact sequence of complexes

$$
0 \longrightarrow C_*(A;R) \longrightarrow C_*(X;R) \longrightarrow C_*(X,A;R) \longrightarrow 0
$$

produces, by the snake lemma of *Exact Sequences*, the **long exact sequence of a pair**

$$
\cdots \to H_n(A;R) \to H_n(X;R) \to H_n(X,A;R) \xrightarrow{\ \partial\ } H_{n-1}(A;R) \to \cdots .
$$

The connecting map $\partial$ is the snake-lemma map, and it lowers degree by one.

**Corollary.** If $A$ is a deformation retract of $X$ then $H_n(X,A;R) = 0$ for all $n$, and $H_n(A) \to H_n(X)$ is an isomorphism.

### Excision

**Theorem (excision).** Let $Z \subseteq A \subseteq X$ with the closure of $Z$ contained in the interior of $A$. Then the inclusion $(X \setminus Z, A \setminus Z) \hookrightarrow (X,A)$ induces isomorphisms

$$
H_n(X \setminus Z, A \setminus Z; R) \xrightarrow{\ \cong\ } H_n(X,A;R)
$$

for all $n$.

*Proof sketch.* Every relative cycle in $H_n(X,A;R)$ is represented by a chain whose simplices are small in the sense that each is contained in $X \setminus Z$ or in $A$: subdivide by iterated barycentric subdivision, using that each singular simplex is a compact subset of $X$ and that the interiors of the sets in the cover $\{X \setminus Z, \operatorname{int}(A)\}$ cover $X$, together with the Lebesgue number lemma. Chains of this form are chains in $C_*(X\setminus Z, A \setminus Z)$, so the inclusion is surjective on homology; the same argument on chains bounding shows injectivity. $\square$

**Corollary (excision, symmetric form).** If $A, B$ are subspaces with $X = \operatorname{int}(A) \cup \operatorname{int}(B)$ then the inclusion $(B, A \cap B) \hookrightarrow (X,A)$ induces isomorphisms in homology.

**Corollary.** For a CW pair $(X,A)$ the collapse $X \to X/A$ induces $H_n(X,A;R) \cong \tilde H_n(X/A;R)$, so the cellular computation of the previous article is a homology computation. In particular, for the $n$-disc pair $(D^n, S^{n-1})$,

$$
H_k(D^n, S^{n-1};R) \cong \begin{cases} R, & k = n, \\ 0, & k \neq n,\end{cases}
$$

and hence $H_n(S^n;R) \cong R$ and $H_k(S^n;R) = 0$ for $0 < k < n$.

### Mayer–Vietoris

**Theorem (Mayer–Vietoris).** Let $X = \operatorname{int}(A) \cup \operatorname{int}(B)$ for subspaces $A, B$. Then there is a long exact sequence

$$
\cdots \to H_n(A \cap B) \to H_n(A) \oplus H_n(B) \to H_n(X) \xrightarrow{\ \partial\ } H_{n-1}(A \cap B) \to \cdots,
$$

with coefficients suppressed and the connecting map $\partial$ defined from the snake lemma applied to the short exact sequence of complexes $0 \to C_*(A \cap B) \to C_*(A)\oplus C_*(B) \to C_*(A+B) \to 0$, where $C_*(A+B)$ denotes chains that are sums of chains in $A$ and in $B$; excision identifies $H_*(A+B)$ with $H_*(X)$.

*Proof.* The given sequence of complexes is exact by the definition of the maps, and the identification $C_*(A)+C_*(B) = C_*(X)$ follows from the subdivision argument of excision. The snake lemma then produces the sequence. $\square$

**Example.** The sphere $S^n$ for $n \geq 1$ is the union of two open discs whose intersection deformation retracts to $S^{n-1}$. Induction with the Mayer–Vietoris sequence gives $H_k(S^n;R) \cong R$ for $k = 0, n$ and $0$ otherwise.

## The Homology of Spheres and Graphs

### Spheres and the Suspension

**Theorem.** For $n \geq 0$, $H_k(S^n;R) \cong R$ for $k = 0$ and $k = n$, and $H_k(S^n;R) = 0$ otherwise; in reduced homology, $\tilde H_k(S^n;R) \cong R$ for $k = n$ and $0$ otherwise.

*Proof.* The case $n = 0$ is $S^0$, two points, with $H_0$ free of rank two and nothing else. For $n \geq 1$ use the Mayer–Vietoris sequence of the two hemispheres, whose intersection is a neighbourhood of the equator, deformation retracting to $S^{n-1}$. The sequence reads $\tilde H_k(S^{n-1}) \to \tilde H_k(S^n) \to 0$ for $k \geq 1$ and $0 \to \tilde H_n(S^n)\to \tilde H_{n-1}(S^{n-1}) \to 0$ in degree $n$, giving the result by induction. $\square$

**Corollary.** The degree of a self-map of $S^n$ is well defined by $f_* = \deg(f)\cdot \mathrm{id}$ on $H_n(S^n) \cong \mathbb{Z}$, and the properties quoted in *CW Complexes and Cellular Approximation* hold by functoriality.

### Graphs

**Definition.** A finite connected graph is a CW complex of dimension one; write $V$ for its $0$-cells and $E$ for its $1$-cells.

**Theorem.** For a connected graph $X$, $H_0(X;R) \cong R$, $H_1(X;R)$ is free of rank $E - V + 1$, and $H_n(X;R) = 0$ for $n \geq 2$.

*Proof.* The cellular chain complex is $0 \to R^{E} \xrightarrow{\partial_1} R^{V} \to 0$. The map $\partial_1$ sends an edge $e$ from $v$ to $w$ to $w - v$, so its image is the submodule of tuples with coordinate sum zero, of rank $V-1$; hence $H_0 \cong R$ and $H_1 \cong \ker\partial_1$ has rank $E - (V-1)$. $\square$

**Corollary.** The rank $E - V + 1$ equals the rank of the free group $\pi_1(X)$, by the Hurewicz theorem; the case of a wedge of circles was computed directly there by van Kampen.

### Equivalence of Simplicial and Singular Homology

**Theorem.** Let $K$ be a simplicial complex with underlying space $|K|$. Then there is a natural isomorphism

$$
H_n^{\Delta}(K;R) \cong H_n(|K|;R)
$$

for all $n$.

*Proof sketch.* Both theories are computed by the same chain complex after subdivision. A **simplicial map** $K \to L$ is a map of underlying spaces linear on each simplex; a map $f : |K| \to |L|$ between finite complexes is homotopic to a simplicial map after sufficiently fine subdivision, by the **simplicial approximation theorem**, and the simplicial chain map it induces agrees with the singular chain map up to chain homotopy. Applying this with $L = \Delta_n$ identifies the singular chains of $|K|$ with the simplicial chains of a subdivision, which have isomorphic homology. $\square$

**Remark.** This is the theorem that makes simplicial homology a topological invariant; it also shows that the cellular homology of the previous article agrees with both, since a CW complex with a simplicial structure carries the three chain complexes, linked by subdivision and by the collapse isomorphisms.

## Summary

Simplicial homology is defined from a simplicial complex by the free module on oriented simplices with the alternating boundary, and it is computable; singular homology is defined for every space by the free module on all continuous maps of standard simplices, with the boundary given by the alternating sum of face restrictions. Both satisfy $\partial\partial = 0$, so both are chain complexes, and homology is cycles modulo boundaries. With coefficients in a commutative ring $R$, the homology groups are $R$-modules, and the default is $R = \mathbb{Z}$.

Singular homology is functorial in the strongest sense: a continuous map induces a chain map and hence a map on homology, composition is respected, homotopic maps induce chain-homotopic chain maps and therefore the same map on homology, and a homotopy equivalence induces an isomorphism. The relative homology of a pair fits in a long exact sequence with the homology of the subspace and of the whole space, and excision allows the relative groups to be computed after removing a closed subset from the interior of the subspace. Mayer–Vietoris assembles the homology of a space from that of two open pieces, and with these tools the homology of the spheres, of graphs and of any CW complex — via the cellular complex of the previous article — is computable. Simplicial and singular homology agree on the underlying space of a simplicial complex, by subdivision and simplicial approximation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | commutative ring with identity $1 \neq 0$; the coefficient ring |
| $\Delta_n = [e_0,\ldots,e_n]$ | Standard $n$-simplex in $\mathbb{R}^{n+1}$ |
| $[v_0,\ldots,v_n]$ | Oriented simplex; reversal negates |
| $\delta^i : \Delta_{n-1} \to \Delta_n$ | $i$-th face map |
| $C_n(K;R)$, $C_n(X;R)$ | Simplicial chains on $K$; singular chains on $X$ |
| $\partial_n$ | Boundary; $\partial_{n-1}\partial_n = 0$ |
| $Z_n = \ker\partial_n$, $B_n = \operatorname{im}\partial_{n+1}$ | Cycles, boundaries |
| $H_n(X;R) = Z_n/B_n$ | Singular homology |
| $H_n^\Delta(K;R)$ | Simplicial homology |
| $\tilde H_n(X;R)$ | Reduced homology; $\varepsilon$ the augmentation |
| $H_n(X,A;R)$ | Relative homology of a pair $A \subseteq X$ |
| $f_\#$, $f_*$ | Induced chain map and induced map on homology |
| $P_n$, chain homotopy | $\psi-\varphi = \partial P + P\partial$; homotopic maps induce equal maps on homology |
| $\partial : H_n(X,A) \to H_{n-1}(A)$ | Connecting map of the long exact sequence of a pair |
| Excision | $H_n(X\setminus Z, A\setminus Z) \cong H_n(X,A)$ for $\overline Z \subseteq \operatorname{int}A$ |
| Mayer–Vietoris | Long exact sequence of $A$, $B$ and $A \cap B$ when $X = \operatorname{int}A \cup \operatorname{int}B$ |
| $\chi(X)$ | Euler characteristic; alternating sum of ranks of $H_n$ |
| Acyclic | $\tilde H_n = 0$ for all $n$ |





## Further Reading

- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for singular homology, excision, Mayer–Vietoris, and simplicial approximation.
- James R. Munkres, *Elements of Algebraic Topology* (Addison-Wesley, 1984), for simplicial homology and the proof that it agrees with the singular theory.
- Samuel Eilenberg and Norman Steenrod, *Foundations of Algebraic Topology* (Princeton University Press, 1952), for the axiomatic characterisation of homology and the role of excision.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, 2nd ed. 2009), for chain complexes, chain homotopy and the algebraic machinery used here.
- Edwin H. Spanier, *Algebraic Topology* (McGraw–Hill, 1966), for the relative theory and the exact sequences of a pair and a triple.
- Glen E. Bredon, *Topology and Geometry* (Springer, 1993), for singular homology with a view to the manifolds of this corpus.
- Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology* (Springer, 1982), for the comparison with de Rham theory developed in the sheaf articles.
