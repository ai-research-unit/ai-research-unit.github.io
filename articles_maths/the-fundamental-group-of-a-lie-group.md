
# __The Fundamental Group of a Lie Group__

## Introduction

A Lie group is a group and a manifold at once, and the two structures constrain each other sharply: the multiplication is smooth, so the group acts on itself by diffeomorphisms, and every local question can be translated to the identity. The first topological invariant of a Lie group is its fundamental group, and the theory of *The Fundamental Group and Covering Spaces* applies with an extra rigidity. The fundamental group of any topological group is **abelian**; the universal cover of a connected Lie group carries a Lie group structure, so that every connected Lie group is a quotient $\tilde G \to G$ of a simply connected Lie group by a discrete central subgroup isomorphic to $\pi_1(G)$; and for a compact connected Lie group the fundamental group is finite and computable from the combinatorial data of a maximal torus and its roots. The classical groups are the standard examples: $\pi_1(U(n)) \cong \mathbb{Z}$, $\pi_1(SU(n)) = 0$, $\pi_1(SO(n)) \cong \mathbb{Z}/2$ for $n \geq 3$, and the double cover $SU(2) \to SO(3)$ is the first case of the spin cover of *The Clifford, Pin and Spin Groups*.

The Lie theory itself — the correspondence between Lie groups and Lie algebras, the exponential map, the closed subgroup theorem, the maximal torus theory — is assumed from the companion article *Lie Groups* of Part I, and the topological group theory from *Topological Groups* and *Abelian Topological Groups*. What this article supplies is the topological computation: the abelianness of $\pi_1$ and its consequences, the classification of connected coverings of a Lie group and the universal covering group, the reduction of $\pi_1(G)$ to the fundamental group of a maximal compact subgroup, the computation of $\pi_1$ for a compact connected group from the coroot lattice of a maximal torus, and the long exact sequence of a homogeneous space, which relates $\pi_1$ of a Lie group to $\pi_1$ of the quotients by closed subgroups. The higher homotopy groups of Lie groups and their homogeneous spaces, and the homology computations that follow from them, are not covered here; the covering-space correspondence is that of *The Fundamental Group and Covering Spaces*, and the classification of coverings by subgroups of $\pi_1$ is used throughout.

Throughout, $G$ is a topological group or a Lie group, $\mathfrak{g}$ its Lie algebra, $G_0$ the identity component, $\pi_0(G) = G/G_0$ the group of components, $\tilde G$ the universal cover, and $\exp : \mathfrak{g} \to G$ the exponential map. The symbol $K$ denotes a maximal compact subgroup of a connected Lie group and $T$ a maximal torus of a compact connected Lie group.

## The Fundamental Group is Abelian

### The Eckmann–Hilton Argument

**Theorem.** Let $G$ be a topological group with basepoint the identity. Then $\pi_1(G, e)$ is abelian, and more generally the fundamental group of any group object in the category of pointed topological spaces is abelian.

*Proof.* Let $\mu : G \times G \to G$ be the multiplication and let $\alpha, \beta : (S^1, 1) \to (G,e)$ be two loops. On the product $S^1 \times S^1$ consider the four maps obtained by inserting the constant loop in one variable; the two loop structures on $S^1\times S^1$ — the one from the first coordinate and the one from the second — are interchanged by the transposition of the factors, and $\mu$ is a map of pointed spaces. Concatenation in the first coordinate followed by $\mu$ gives the composite $\alpha \ast \beta$, and concatenation in the second coordinate gives $\beta \ast \alpha$. Both are homotopic, by the interchange of coordinates in the square, to the map $S^1\times S^1 \to G$ that is $\mu(\alpha,\beta)$ after collapsing the boundary, whence $\alpha\ast\beta \simeq \beta\ast\alpha$. $\square$

**Remark.** The argument is the **Eckmann–Hilton argument**: two monoid structures on the same set that distribute over one another coincide and are commutative. The two structures here are the two concatenations of loops, and the interchange law is the compatibility of the concatenations with the product in $G$. The same argument shows that $\pi_n(G)$ is abelian for $n \geq 2$ for *any* pointed space, by the two-coordinate interchange on $S^n$; the content of the present theorem is that for a group the abelianness descends to $n=1$.

### Consequences

**Proposition.** For a Lie group $G$:

1. $\pi_1(G) \cong \pi_1(G_0)$, and the inclusion $G_0 \hookrightarrow G$ induces isomorphisms $\pi_n(G_0) \to \pi_n(G)$ for every $n \geq 1$ and isomorphisms on homology in every degree.
2. $H_1(G;\mathbb{Z}) \cong \pi_1(G)$ by the Hurewicz theorem of *Homotopy Groups and Fibrations*, so the first homology of a Lie group is free abelian or torsion as $\pi_1$ is.
3. $\pi_1(G)$ acts trivially on $\pi_n(G)$ for every $n \geq 1$, and the action of $\pi_1$ on the fibre homology in any fibration with connected fibre over a Lie group is trivial, so local coefficients are unnecessary in the computations of this article.

*Proof.* (1) The projection $G \to \pi_0(G)$ is a covering, since $\pi_0(G)$ is discrete and $G$ is locally connected, so $G$ is a disjoint union of the cosets of $G_0$, each homeomorphic to $G_0$. (2) is the Hurewicz theorem, applicable since $\pi_1$ is abelian and $G$ is connected when restricted to $G_0$. (3) The action of a loop $\gamma$ based at $e$ on $\pi_n(G)$ is by the map induced from translation along $\gamma$; but translation by $\gamma(1) = e$ is the identity, and the homotopy $x \mapsto \gamma(t)x$ deforms translation along the loop to the identity through homotopy equivalences, so the action is trivial. The statement for local coefficients follows. $\square$

**Remark.** The triviality of the $\pi_1$-action makes the Lie group case cleaner than the general case of *Homotopy Groups and Fibrations*: the Serre spectral sequence of a fibration of Lie groups has constant coefficients, and the homology of a homogeneous space can be computed with ordinary coefficients.

## The Universal Covering Group

### Coverings of a Lie Group

**Theorem (covering groups).** Let $G$ be a connected Lie group and $p : \hat G \to G$ a connected covering space. Then $\hat G$ carries a unique Lie group structure making $p$ a homomorphism of Lie groups and a local diffeomorphism; the subgroup $p_*\pi_1(\hat G) \leq \pi_1(G)$ determines the covering up to isomorphism, and every subgroup of $\pi_1(G)$ arises.

*Proof.* Fix the basepoint $\hat e$ over $e$ and define $\hat\mu : \hat G\times\hat G \to \hat G$ as the lift of $\mu \circ (p\times p) : \hat G\times \hat G\to G$ sending $(\hat e,\hat e)$ to $\hat e$; the lift exists and is unique because $\hat G \times \hat G$ is simply connected when $\hat G$ is, and the group axioms follow by uniqueness of lifts of the corresponding maps on the simply connected cover. The statement for a general connected covering follows by factoring through the universal cover. The correspondence between coverings and subgroups is that of *The Fundamental Group and Covering Spaces*. $\square$

**Corollary (the universal covering group).** Let $G$ be a connected Lie group with universal cover $\tilde G$. Then $\tilde G$ is a simply connected Lie group, and

$$
1 \to \pi_1(G) \to \tilde G \xrightarrow{\ p\ } G \to 1
$$

is an exact sequence of Lie groups in which $\pi_1(G) \cong p^{-1}(e)$ is a discrete central subgroup.

*Proof.* The group structure is that of the theorem. The kernel $p^{-1}(e)$ is discrete, being a fibre of a covering, and is central because $\tilde G$ is connected and the conjugation action of $\tilde G$ on the discrete kernel is continuous, hence trivial. $\square$

**Corollary.** For a connected Lie group $G$, the connected coverings of $G$ stand in bijection with the subgroups of $\pi_1(G)$; since $\pi_1(G)$ is abelian, every subgroup is normal, and every connected covering of $G$ is again a Lie group with the covering map a homomorphism. In particular, every connected covering of a connected Lie group is a covering *group*.

**Example.** For $G = U(1)$ the universal cover is $\mathbb{R} \to U(1)$, $t \mapsto e^{2\pi i t}$, with kernel $\mathbb{Z} \cong \pi_1(U(1))$; the connected coverings are the maps $z \mapsto z^n$. For $G = SO(3) \cong \mathbb{RP}^3$ the universal cover is $SU(2) \cong S^3$ and $\pi_1(SO(3)) \cong \mathbb{Z}/2$; this is the case $n = 3$ of the spin cover $\mathrm{Spin}(n) \to SO(n)$ of *The Clifford, Pin and Spin Groups*.

### The Case of Finite Fundamental Group

**Theorem.** Let $G$ be a compact connected Lie group. Then $\pi_1(G)$ is finitely generated and abelian, and:

1. $\tilde G$ is compact if and only if $\pi_1(G)$ is finite.
2. If $\pi_1(G)$ is finite then $G = \tilde G/N$ with $N$ a finite central subgroup, and every finite-dimensional representation of $G$ is a representation of $\tilde G$ on which $N$ acts trivially.
3. The simply connected cover $\tilde G$ of a compact connected Lie group is compact and is a product of a torus and simply connected simple compact factors.

*Proof.* (1) If $\tilde G$ is compact then $\pi_1(G) = p^{-1}(e)$ is a discrete closed subset of a compact space, hence finite. Conversely, if $\pi_1(G)$ is finite then $\tilde G$ is a finite covering of a compact space, hence compact. (2) is the exact sequence of the corollary applied to a compact group. (3) is the structure theory of compact connected Lie groups (the classification of *Lie Groups*): $\tilde G$ is a product of a torus and simply connected simple compact Lie groups, and the splitting follows from the theory of maximal tori. $\square$

**Example ($SO(n)$ and the spin groups).** For $n \geq 3$ the group $SO(n)$ is compact connected with $\pi_1 \cong \mathbb{Z}/2$ and universal cover $\mathrm{Spin}(n)$, so $\mathrm{Spin}(n) \to SO(n)$ is a double cover and $\mathrm{Spin}(n)$ is compact simply connected; for $n \geq 7$, $\mathrm{Spin}(n)$ is simple. For $n = 2$, $SO(2) \cong U(1)$ has $\pi_1 \cong \mathbb{Z}$ and universal cover $\mathbb{R}$; for $n = 1$, $SO(1)$ is trivial.

**Remark.** The universal cover of a connected Lie group is a Lie group, but not necessarily a group of matrices: the universal cover of $SL(2,\mathbb{R})$ has no faithful finite-dimensional representation, while its quotient $SL(2,\mathbb{R})$ does. The passage to the universal cover therefore cannot always be performed inside the category of linear groups, although it can always be performed among Lie groups.

## Reduction to the Compact Case

### Maximal Compact Subgroups

**Theorem (Malcev, Iwasawa).** Let $G$ be a connected Lie group. Then $G$ contains maximal compact subgroups, any two of them are conjugate in $G$, and the inclusion $K \hookrightarrow G$ of a maximal compact subgroup is a homotopy equivalence. Consequently

$$
\pi_n(G) \cong \pi_n(K) \quad\text{for all } n \geq 0, \qquad H_n(G;\mathbb{Z}) \cong H_n(K;\mathbb{Z}) \quad\text{for all } n \geq 0,
$$

and $\pi_1(G)$ is finitely generated.

*Proof sketch.* The **Iwasawa decomposition** writes a connected semisimple Lie group as $G = KAN$ with $K$ compact, $A$ a vector group and $N$ nilpotent, and $AN$ is diffeomorphic to a Euclidean space; hence the inclusion $K \to G$ is a homotopy equivalence. The general case is reduced to the semisimple case modulo the centre and the solvable radical, and the conjugacy of maximal compact subgroups is the **Malcev theorem**, proved by applying the Cartan fixed point theorem to the action on the symmetric space $G/K$. $\square$

**Example.** $GL_n(\mathbb{R})$ has maximal compact $O(n)$; $SL_n(\mathbb{R})$ has maximal compact $SO(n)$; $GL_n(\mathbb{C})$ has maximal compact $U(n)$; $SL_n(\mathbb{C})$ has maximal compact $SU(n)$; $Sp_{2n}(\mathbb{R})$ has maximal compact $U(n)$. Each inclusion is a homotopy equivalence, so the homotopy of the real and complex groups is that of the corresponding compact groups; the complex case is the more transparent, since $\pi_1(U(n)) \cong \mathbb{Z}$ and $\pi_1(SU(n)) = 0$.

**Example.** For $G = \mathbb{R}^n$ the maximal compact subgroup is trivial and $\pi_1(\mathbb{R}^n) = 0$; for $G = \mathbb{R}^*_+ \cong \mathbb{R}$ it is trivial; for $G = GL_n(\mathbb{R})$ with $n \geq 3$ it is $O(n)$, giving $\pi_1(GL_n(\mathbb{R})) \cong \pi_1(O(n)) \cong \mathbb{Z}/2$ for $n \geq 3$.

### The Homotopy Sequence of a Homogeneous Space

**Theorem.** Let $G$ be a Lie group and $H$ a closed subgroup. Then $G/H$ has a unique smooth structure making the projection $G \to G/H$ a submersion, the projection is a fibre bundle with fibre $H$, and the **homotopy sequence of the fibration**

$$
\cdots \to \pi_n(H) \to \pi_n(G) \to \pi_n(G/H) \to \pi_{n-1}(H) \to \cdots \to \pi_0(H) \to \pi_0(G) \to 0
$$

is exact.

*Proof sketch.* The quotient $G/H$ is a manifold by the closed subgroup theorem and the slice theorem of *Lie Groups*; the projection is a locally trivial fibre bundle by the existence of local sections obtained from a slice at the identity. The long exact sequence is that of a fibration, *Homotopy Groups and Fibrations*. $\square$

**Corollary.** In low degrees the sequence gives an exact sequence

$$
\pi_1(H) \xrightarrow{\ i_*\ } \pi_1(G) \xrightarrow{\ } \pi_1(G/H) \xrightarrow{\ \partial\ } \pi_0(H) \xrightarrow{\ } \pi_0(G) \to 0 .
$$

In particular:

1. If $G$ is connected, $\pi_1(G/H) \cong \pi_1(G)/i_*\pi_1(H)$ whenever $H$ is connected; the quotient is by the image of $\pi_1(H)$.
2. If $G$ is simply connected and $H$ is connected, then $G/H$ is simply connected.
3. If $H$ is discrete then $\pi_1(G/H)$ is an extension of $\ker(\pi_0(H)\to\pi_0(G))$ by the cokernel of $i_*$, and if in addition $G$ is connected and simply connected then $\pi_1(G/H) \cong \pi_0(H)$.

*Proof.* These are the immediate consequences of exactness at the relevant terms. $\square$

**Example ($SO(3)$ again).** Take $G = SU(2)$, $H = \{\pm I\} = \pi_0(H) = \mathbb{Z}/2$, so $G/H = SO(3)$; the corollary with $G$ simply connected and $H$ discrete gives $\pi_1(SO(3)) \cong \mathbb{Z}/2$, recovering the computation of the previous section from the fibre bundle $SU(2)\to SO(3)$ with fibre $\mathbb{Z}/2$.

**Example (spheres as homogeneous spaces).** $S^{n-1} = SO(n)/SO(n-1) = \mathrm{Spin}(n)/\mathrm{Spin}(n-1)$; since $\mathrm{Spin}(n)$ is simply connected and $\mathrm{Spin}(n-1)$ is connected, the corollary gives $\pi_1(S^{n-1}) = 0$ for $n \geq 3$. For $n = 2$ the group $\mathrm{Spin}(1) = \mathbb{Z}/2$ is disconnected, and it is cleaner to take the stabiliser to be $SO(1)$, which is trivial: the fibration $SO(1) \to SO(2) \to S^1$ gives $\pi_1(S^1) \cong \pi_1(SO(2)) \cong \mathbb{Z}$ directly. The case distinction is exactly the failure of connectedness of the stabiliser.

## The Fundamental Group of a Compact Group

### Maximal Tori and the Coroot Lattice

**Definition.** Let $G$ be a compact connected Lie group, $T \leq G$ a **maximal torus**, that is, a maximal connected abelian closed subgroup, and $\mathfrak{t} \subseteq \mathfrak{g}$ its Lie algebra. The **root system** $\Phi(\mathfrak{g},\mathfrak{t})$ consists of the nonzero weights of the adjoint action of $\mathfrak{t}$ on $\mathfrak{g}_{\mathbb{C}}$; for each root $\alpha$ there is a **coroot** $\alpha^\vee : S^1 \to T$, the unique homomorphism whose differential is the element of $\mathfrak{t}$ dual to $\alpha$ under the Killing form normalisation. The subgroup generated by the coroots,

$$
Q^\vee = \langle \alpha^\vee(S^1) : \alpha \in \Phi\rangle \leq T,
$$

is the **coroot lattice** in $T$, and the coweight lattice is

$$
X_*(T) = \operatorname{Hom}(U(1), T) \cong \pi_1(T) \cong \mathbb{Z}^{\dim T}.
$$

**Theorem (Bott).** Let $G$ be a compact connected Lie group with maximal torus $T$. Then the inclusion $T \hookrightarrow G$ induces a surjection $\pi_1(T) \to \pi_1(G)$ whose kernel is the coroot lattice, so that

$$
\pi_1(G) \cong X_*(T)/Q^\vee \cong \pi_1(T)/\langle \alpha^\vee\rangle .
$$

In particular $\pi_1(G)$ is a finite group of order equal to the index of the coroot lattice in the coweight lattice, $G$ is simply connected if and only if $X_*(T) = Q^\vee$, and for the **adjoint group** $G_{\mathrm{ad}} = G_{\mathrm{sc}}/Z(G_{\mathrm{sc}})$ — the quotient of the simply connected cover by its centre — there is an isomorphism

$$
\pi_1(G_{\mathrm{ad}}) \cong Z(G_{\mathrm{sc}}),
$$

the centre of the simply connected cover.

*Proof sketch.* The quotient $G/T$ admits a cell decomposition into **Schubert cells**, one for each element of the Weyl group, all of even real dimension; consequently $G/T$ has no cells in odd dimensions, and a CW complex with no odd-dimensional cells is simply connected, so $\pi_1(G/T) = 0$. The homotopy sequence of the fibration $T \to G \to G/T$ then reads $\pi_1(T) \xrightarrow{i_*} \pi_1(G) \to 0$, so $\pi_1(G) \cong \pi_1(T)/\ker i_*$. It remains to identify the kernel: $G$ is obtained from $T$ by attaching the cells of $G/T$, the two-dimensional Schubert cells are attached along the coroot circles $\alpha^\vee(S^1) \subseteq T$, and the cells of dimension $\neq 2$ contribute nothing to $\pi_1$; hence $\ker i_*$ is generated by the coroots, and $\pi_1(G) \cong \pi_1(T)/Q^\vee$. The final statement follows because the coverings of $G_{\mathrm{ad}}$ are classified by the subgroups of $Z(G_{\mathrm{sc}})$, whose simply connected total space is $G_{\mathrm{sc}}$. $\square$

**Remark.** The theorem reduces a topological computation to a purely combinatorial one: $\pi_1$ of a compact connected Lie group is the quotient of the coweight lattice of a maximal torus by the coroot lattice, which can be read off from the root system and the Dynkin diagram. The same data classify the compact connected Lie groups, so $\pi_1$ is determined by the root system together with the lattice $X_*(T)$, that is, by the **root datum**.

### Computations for the Classical Groups

**Theorem.** The fundamental groups of the classical compact groups are:

| $G$ | $\pi_1(G)$ |
|---|---|
| $U(n)$, $n \geq 1$ | $\mathbb{Z}$ |
| $SU(n)$, $n \geq 1$ | $0$ |
| $SO(2) \cong U(1)$ | $\mathbb{Z}$ |
| $SO(n)$, $n \geq 3$ | $\mathbb{Z}/2$ |
| $O(n)$, $n \geq 3$ | $\mathbb{Z}/2$ |
| $\mathrm{Spin}(n)$, $n \geq 3$ | $0$ |
| $Sp(n)$, $n \geq 1$ | $0$ |
| $GL_n(\mathbb{C})$, $n \geq 1$ | $\mathbb{Z}$ |
| $GL_n(\mathbb{R})$, $n \geq 3$ | $\mathbb{Z}/2$ |

*Proof.* For $U(n)$ the determinant $\det : U(n) \to U(1)$ is a fibre bundle with fibre $SU(n)$, and the homotopy sequence $0 = \pi_1(SU(n)) \to \pi_1(U(n)) \to \pi_1(U(1)) = \mathbb{Z} \to \pi_0(SU(n)) = 0$ gives $\pi_1(U(n)) \cong \mathbb{Z}$ once $SU(n)$ is known simply connected. For $SU(n)$ the theorem of Bott applies: with the standard maximal torus $T = \{ \operatorname{diag}(z_1,\ldots,z_n) : \prod z_i = 1\}$, the coweight lattice is $\{ (m_1,\ldots,m_n)\in\mathbb{Z}^n : \sum m_i = 0\}$, the roots are $z_i z_j^{-1}$ with coroots $z \mapsto (1,\ldots,z,\ldots,z^{-1},\ldots,1)$, and these generate exactly the coweight lattice, so $\pi_1(SU(n)) = 0$. For $SO(n)$, $n \geq 3$, the coroot lattice of the root system $B_{(n-1)/2}$ or $D_{n/2}$ has index $2$ in the coweight lattice, giving $\pi_1 \cong \mathbb{Z}/2$; alternatively $SO(n) = \mathrm{Spin}(n)/\{\pm1\}$ with $\mathrm{Spin}(n)$ simply connected by the theorem, since the coweight lattice of $\mathrm{Spin}(n)$ is the coroot lattice. $O(n)$ has two components and $\pi_1(O(n)) \cong \pi_1(SO(n))$. For $Sp(n)$ the root system $C_n$ has coweight lattice equal to the coroot lattice, so $\pi_1 = 0$. The general linear groups reduce to the compact ones by the Malcev–Iwasawa theorem: $GL_n(\mathbb{C})$ has maximal compact $U(n)$ and $GL_n(\mathbb{R})$ has maximal compact $O(n)$. $\square$

**Example ($\pi_1(U(n))$ and the determinant).** The determinant exhibits $\pi_1(U(n)) \cong \mathbb{Z}$ with a canonical generator, the class of $z \mapsto \operatorname{diag}(z,1,\ldots,1)$; this generator is the one that appears in the first Chern class of a complex line bundle, and it underlies the identification of $\pi_1(U(n))$ with the degree of the determinant.

**Example ($SU(2) \to SO(3)$).** Here $SU(2)$ has root system $A_1$, coweight lattice $\mathbb{Z}$ and coroot lattice $\mathbb{Z}$, so $\pi_1(SU(2)) = 0$; $SO(3)$ has the same root system with coweight lattice $\mathbb{Z}$ and coroot lattice $2\mathbb{Z}$, so $\pi_1(SO(3)) \cong \mathbb{Z}/2$; the quotient is realised by the double cover $SU(2) \to SO(3)$, the adjoint group of type $A_1$, and $\pi_1(SO(3)) \cong Z(SU(2)) = \{\pm I\}$.

**Remark.** The computations identify $\pi_1$ with the cokernel of the coroot inclusion, and dualising gives the finite group $P/Q$ of weights modulo roots, the **fundamental group of the root system** in the classical terminology; for the adjoint group it is isomorphic to the centre of the simply connected cover, and for the simply connected group it vanishes. The simply connected simple compact groups — $SU(n)$, $\mathrm{Spin}(n)$, $Sp(n)$, $E_6$, $E_7$, $E_8$, $F_4$, $G_2$ — are exactly those with vanishing $\pi_1$; the corresponding adjoint groups have $\pi_1$ equal to the centre of the simply connected group, so the possible nontrivial fundamental groups of simple compact groups are $\mathbb{Z}/n$ for $SU(n)$, $\mathbb{Z}/2$ or $\mathbb{Z}/4$ or $\mathbb{Z}/2\oplus\mathbb{Z}/2$ for the spin groups, $\mathbb{Z}/2$ for $Sp(n)$ and $E_7$, $\mathbb{Z}/3$ for $E_6$, and trivial for $E_8$, $F_4$ and $G_2$.

### Spin Covers and the General Theory of Coverings

**Theorem.** For $n \geq 3$ the double cover $\mathrm{Spin}(n) \to SO(n)$ is the universal cover, and the connected coverings of $SO(n)$ are $\mathrm{Spin}(n) \to SO(n)$ and the identity; for $n = 2$ the connected coverings of $SO(2)$ are the maps $z \mapsto z^m$ of $U(1)$. The coverings of a compact connected Lie group correspond to the subgroups of the finite group $\pi_1(G)$, hence are finite in number and all compact.

*Proof.* The coverings of a connected space correspond to the subgroups of its fundamental group by *The Fundamental Group and Covering Spaces*; the fundamental group of a compact connected Lie group is finite by the theorem of Bott, since the coroot lattice has finite index in the coweight lattice. Comparing indices gives the stated covers and the finiteness. $\square$

**Remark.** The finite coverings of a compact connected Lie group are the quotients of the simply connected cover $\tilde G$ by the subgroups of its centre; the simply connected cover is compact by the theorem of the previous section, so this is a classification internal to compact groups.

## Summary

The fundamental group of a topological group is abelian, by the Eckmann–Hilton interchange argument; for a Lie group, $\pi_1$ depends only on the identity component, equals $H_1$ by Hurewicz, and acts trivially on all the higher homotopy groups, so the local coefficients of the general fibration theory are constant in this setting. Every connected covering of a connected Lie group is again a Lie group, by lifting the multiplication to the covering, and the connected coverings are classified by the subgroups of $\pi_1(G)$; in particular the universal cover $\tilde G$ is a simply connected Lie group and $G \cong \tilde G/N$ with $N \cong \pi_1(G)$ discrete central. For a compact connected $G$ the fundamental group is finite, $\tilde G$ is compact, and $G$ is a quotient of $\tilde G$ by a finite central subgroup.

The Malcev–Iwasawa theorem reduces the homotopy of a connected Lie group to that of a maximal compact subgroup, so $\pi_1(GL_n(\mathbb{R})) \cong \pi_1(O(n))$ and $\pi_1(GL_n(\mathbb{C})) \cong \pi_1(U(n))$. For a compact connected group with maximal torus $T$, Bott's theorem identifies $\pi_1(G) \cong X_*(T)/Q^\vee$ with the quotient of the coweight lattice by the coroot lattice; this gives $\pi_1(U(n)) \cong \mathbb{Z}$, $\pi_1(SU(n)) = \pi_1(Sp(n)) = 0$ and $\pi_1(SO(n)) \cong \mathbb{Z}/2$ for $n \geq 3$, and identifies $\pi_1$ of the adjoint group with the centre of the simply connected cover, so that the double cover $SU(2)\to SO(3)$ is the first case of the spin covers. Finally, the long exact homotopy sequence of the fibration $H \to G \to G/H$ computes $\pi_1$ of a homogeneous space from that of the group and the stabiliser; a quotient of a simply connected group by a connected closed subgroup is simply connected.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $G_0$, $\pi_0(G) = G/G_0$ | Lie group; identity component; component group |
| $\mathfrak{g}$, $\mathfrak{t}$, $\exp$ | Lie algebra, Cartan subalgebra of $\mathfrak{t}$, exponential map |
| $\tilde G$, $p : \tilde G \to G$ | Universal covering group and its projection |
| $\pi_1(G)$, $H_1(G;\mathbb{Z})$ | Fundamental group of a Lie group; abelian, equals $H_1$ |
| $\mu$ | Multiplication $G\times G \to G$; the H-space structure |
| $K$ | Maximal compact subgroup; $G \simeq K$ (Malcev–Iwasawa) |
| $T$, $X_*(T) = \operatorname{Hom}(U(1),T)$ | Maximal torus; coweight lattice $\cong \pi_1(T)$ |
| $\Phi(\mathfrak{g},\mathfrak{t})$, $\alpha$, $\alpha^\vee$ | Root system, roots, coroots |
| $Q^\vee = \langle \alpha^\vee\rangle$ | Coroot lattice; $\pi_1(G) \cong X_*(T)/Q^\vee$ (Bott) |
| $G_{\mathrm{sc}}$, $G_{\mathrm{ad}} = G_{\mathrm{sc}}/Z(G_{\mathrm{sc}})$ | Simply connected cover; adjoint group |
| $Z(G)$ | Centre; $\pi_1(G_{\mathrm{ad}}) \cong Z(G_{\mathrm{sc}})$ |
| $SO(n)$, $SU(n)$, $U(n)$, $Sp(n)$, $O(n)$ | Classical compact groups |
| $\mathrm{Spin}(n)$ | Simply connected double cover of $SO(n)$, $n \geq 3$ |
| $GL_n(\mathbb{R})$, $GL_n(\mathbb{C})$ | General linear groups; maximal compact $O(n)$, $U(n)$ |
| $G/H$, $\pi_n(G/H)$ | Homogeneous space and its homotopy groups |
| $P/Q$ | Weights modulo roots; dual to $\pi_1$ of the adjoint group |





## Further Reading

- Armand Borel, *Topology of Lie Groups and Characteristic Classes* (Bulletin of the American Mathematical Society 61, 1955), for the fundamental group and the coroot lattice.
- Raoul Bott, *An Application of the Morse Theory to the Topology of Lie Groups* (Bulletin de la Société Mathématique de France 84, 1956), for the proof that $\pi_1(G) \cong X_*(T)/Q^\vee$.
- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (Academic Press, 1978), for the Iwasawa decomposition and the Malcev theorem.
- J. Frank Adams, *Lectures on Lie Groups* (University of Chicago Press, 1969), for the structure theory, maximal tori and the exponential map.
- Theodor Bröcker and Tammo tom Dieck, *Representations of Compact Lie Groups* (Springer, 1985), for the root datum and the classification of compact connected Lie groups.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the covering-space correspondence and the homotopy sequences used here.
- Morris W. Hirsch, *Differential Topology* (Springer, 1976), for the closed subgroup theorem and the quotient manifold structure of $G/H$.
