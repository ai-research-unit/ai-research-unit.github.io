# __The Orbit Space of a Free Involution__

## Introduction

A **free** involution is one with no fixed point, so that every orbit has exactly two points, and the orbit map of a free involution pairs the two points of each orbit and is otherwise a local homeomorphism. This article proves the precise form of that statement: for a free continuous involution of a Hausdorff space the orbit map is a **two-fold covering**, and it classifies the two-fold coverings of a connected space as the orbit maps of free involutions. The orbit space of a free involution is therefore the base of a covering, the involution is its **deck transformation**, and the whole of the covering theory of the later articles applies. The **two-fold coverings and the Borel construction** of the next article take the construction one step further, to a space on which the involution acts in a way that survives the passage to the quotient, and the classification of the two-fold coverings by a cohomology group is the subject of the algebraic topology of this Part.

The article begins with a free involution and constructs a neighbourhood that the orbit map identifies with a product, the **trivializing neighbourhood**; it then reviews the definition of a covering map, proves that the orbit map of a free involution of a Hausdorff space is a two-fold covering, computes the group of deck transformations, and proves that a connected two-fold covering is, up to equivalence, the orbit map of a free involution. It continues *Spaces with an Involution and the Orbit Space*, whose functoriality and quotient results are used, and it precedes *Two-Fold Coverings and the Borel Construction*.

Nothing analytic and nothing geometric is used. The circle and the sphere occur with the involutions $z \mapsto -z$ and $x \mapsto -x$, and the covering they define is named; no distance, length or angle is read from them.

## Free Involutions

### Free Involution and the Trivializing Neighbourhood

**Definition.** The continuous involution $\sigma$ of $X$ is **free** when $X^{\sigma} = \emptyset$, that is, when $\sigma(x) \neq x$ for every $x$. Then every orbit $\{x, \sigma(x)\}$ has exactly two points.

**Theorem (trivializing neighbourhood).** Let $\sigma$ be a free continuous involution of a Hausdorff space $X$, and let $x \in X$. Then there is an open neighbourhood $U$ of $x$ with

$$
U \cap \sigma(U) = \emptyset .
$$

Moreover $U$ can be chosen so that the image $\pi(U)$ is open in $X/\sigma$ and $\pi^{-1}(\pi(U)) = U \cup \sigma(U)$ is the disjoint union of two homeomorphic copies of $U$.

**Proof.** For the single element $g = \sigma \neq \mathrm{id}$ the points $x$ and $\sigma(x)$ are distinct, so by the Hausdorff property there are open sets $O \ni x$ and $P \ni \sigma(x)$ with $O \cap P = \emptyset$. Put $U = O \cap \sigma^{-1}(P)$; then $U$ is open and contains $x$, because $\sigma^{-1}(P)$ contains $\sigma^{-1}(\sigma(x)) = x$, and

$$
U \cap \sigma(U) = (O \cap \sigma^{-1}P) \cap \sigma(O \cap \sigma^{-1}P) \subseteq O \cap P = \emptyset ,
$$

since $\sigma(U) \subseteq P$. The image $\pi(U)$ is open because $\pi$ is open, and its preimage is $U \cup \sigma(U)$ because the orbits are the two-point sets, and the two members are disjoint by the first part. The involution restricts to a homeomorphism $U \to \sigma(U)$.

The neighbourhood is the two-fold analogue of the disjoint neighbourhoods of the two points of an orbit; it exists because a finite group action on a Hausdorff space has only finitely many translates to separate. For a general group the corresponding statement can fail, and the orbit space can fail to be a covering even when the action is free.

### Local Injectivity of the Orbit Map

**Corollary.** Under the hypotheses of the theorem the orbit map is a local homeomorphism: on the trivializing neighbourhood $U$ it restricts to a homeomorphism $U \to \pi(U)$.

**Proof.** The restriction is continuous, injective because $\pi$ is injective on a set disjoint from its translate, and open because $\pi$ is open; hence it is a homeomorphism onto its image.

## The Orbit Map as a Two-Fold Covering

### Covering Maps

**Definition.** A continuous surjection $p : E \to B$ is a **covering map** when every point of $B$ has an open neighbourhood $V$ that is **evenly covered**: there is a discrete space $F$ and a homeomorphism

$$
\varphi : p^{-1}(V) \longrightarrow V \times F
$$

over $V$, that is, $\mathrm{pr}_{V} \circ \varphi = p$ on $p^{-1}(V)$. The space $F$ is the **fibre**, and the covering is **$n$-fold** when $F$ has $n$ points. A **two-fold covering** is a covering with two points in the fibre.

For a two-fold covering the preimage of an evenly covered $V$ is the disjoint union of two open sets each homeomorphic to $V$ under $p$. When $B$ is connected the fibre is the same finite cardinal over every point, and the covering is $n$-fold for a fixed $n$; the two-fold case is $n = 2$.

### The Orbit Map is a Two-Fold Covering

**Theorem.** Let $\sigma$ be a free continuous involution of a Hausdorff space $X$. Then the orbit map

$$
\pi : X \longrightarrow X/\sigma
$$

is a two-fold covering. The fibre over the orbit of $x$ is the two-point set $\{x, \sigma(x)\}$, and the trivializing neighbourhood of the previous section provides the evenly covered neighbourhood of its image.

**Proof.** Let $y \in X/\sigma$ and let $x$ be a point of the orbit $y$, so that $y = \{x, \sigma(x)\}$. By the trivializing theorem there is an open $U \ni x$ with $U \cap \sigma(U) = \emptyset$ and $\pi^{-1}(\pi(U)) = U \cup \sigma(U)$. The set $V = \pi(U)$ is open in $X/\sigma$ and

$$
\pi^{-1}(V) = U \sqcup \sigma(U) ,
$$

a disjoint union of two open sets, and $\pi$ restricts to a homeomorphism on each of them by the local injectivity. Hence $V$ is evenly covered with fibre $\{0,1\}$, and $y$ was arbitrary, so $\pi$ is a covering. The fibre over $y$ is $\{x,\sigma(x)\}$, two points.

**Corollary.** The orbit space of a free involution of a Hausdorff space is the base of a two-fold covering with total space $X$; the covering is surjective, open and closed when $X$ is compact, and the orbit space is Hausdorff when $X$ is.

**Proof.** The covering statement is the theorem; the orbit map is surjective and open; it is closed for a finite group action on a compact space, and the orbit space inherits Hausdorffness by *Spaces with an Involution and the Orbit Space*.

### Deck Transformations

**Definition.** Let $p : E \to B$ be a covering. A **deck transformation** is a homeomorphism $\varphi : E \to E$ with $p \circ \varphi = p$. The deck transformations form a group under composition, the **deck group** of the covering.

**Theorem.** Let $\sigma$ be a free continuous involution of a connected Hausdorff space $X$. Then the deck group of $\pi : X \to X/\sigma$ is $\{1, \sigma\} \cong \mathbb{Z}/2$, and it acts transitively on every fibre.

**Proof.** The involution satisfies $\pi \circ \sigma = \pi$, so it is a deck transformation, and it is not the identity because $\sigma(x) \neq x$ for every $x$. Every deck transformation permutes the two points of each fibre, so the action on a fixed fibre defines a homomorphism from the deck group to the symmetric group on two letters. Its kernel consists of the deck transformations that fix the two points of that fibre. A deck transformation with a fixed point is the identity when $X$ is connected: the set of its fixed points is nonempty, closed, and open, since near a fixed point it must agree with the identity on a trivializing neighbourhood, so by connectedness it is all of $X$. Hence the kernel is trivial, the deck group embeds in the two-element symmetric group, and since it contains the non-identity element $\sigma$ it has exactly two elements. Transitivity on the fibre $\{x,\sigma(x)\}$ is that $\sigma$ carries $x$ to the other point.

**Remark.** The connectedness of $X$ is used, and the deck group can be larger without it. If $X$ is the disjoint union of two copies of a space and $\sigma$ acts freely on each copy separately, then the orbit map is still a two-fold covering, but a deck transformation may act as the identity on one copy and as the involution on the other, and the deck group then has four elements. The obstruction disappears when $X$ is connected.

**Remark.** A covering whose deck group acts transitively on each fibre is **regular**, or **normal**, and the theorem says that the orbit map of a free involution is a regular two-fold covering. Conversely a regular covering with deck group $G$ is the orbit map of the action of $G$ on the total space, which is the content of the converse below in the two-fold case.

## The Converse

### Two-Fold Coverings of a Connected Base

**Theorem.** Let $p : E \to B$ be a two-fold covering with $B$ connected. Then the deck group of $p$ has two elements, the action of the nontrivial deck transformation on $E$ is a free involution, $E/\sigma$ is homeomorphic to $B$ in such a way that $\pi$ becomes $p$, and the covering is regular.

**Proof sketch.** The deck group permutes the two points of each fibre, so it embeds in the two-element symmetric group once a fibre is fixed, and the standard theory of covering spaces shows that the image is transitive on the fibre when $B$ is connected: a loop in $B$ based at the point under the fibre either returns the two points to themselves or exchanges them, and the exchanging loops form the complement of the image of the fundamental group of $E$, a subgroup of index two and hence normal. Regularity, and the transitivity of the deck group on the fibre, follow. The nontrivial deck transformation $\sigma$ then has no fixed point, since a fixed point would lie in a fibre whose two points it interchanges; the universal property gives a continuous bijection $E/\sigma \to B$, which is a homeomorphism because $p$ is a covering and hence open, and $\pi$ becomes $p$ under this identification.

**Remark.** The proof sketch invokes the covering-space theory that is developed later in this Part, in *Covering Spaces* and *Simplicial and Singular Homology*; the reader may read the forward direction of this article, that a free involution gives a two-fold covering, without it, and return to the converse after the covering theory. The two-fold case is simpler than the general one because a subgroup of index two is normal, so a two-fold covering of a connected base is always regular.

**Corollary.** For a connected base the two-fold coverings are exactly the orbit maps of free involutions, up to homeomorphism over the base; and the correspondence is natural in the base.

**Proof.** The first clause is the theorem; the naturality is that a map of bases that lifts to the total spaces commutes with the involutions, and every equivalence of coverings over the base is such a lift.

**Remark.** The converse uses that a subgroup of index two is normal, so that a two-fold covering of a connected base is automatically regular; for a covering of degree greater than two the deck group need not act transitively on the fibre, and the orbit map of the deck group is then only a quotient of the total space, not the total space itself. The two-fold case is the case in which the orbit description is complete.

## Examples

**Example (the antipodal involution).** On the sphere $S^{n}$ the antipodal map is a free involution and the orbit map $S^{n} \to \mathbb{RP}^{n}$ is a two-fold covering; the deck group is generated by the antipodal map.

**Example (the squaring cover of the circle).** On the circle $S^{1}$, read as the set of complex numbers of modulus one, the involution $z \mapsto -z$ is free; the orbit space is again a circle under $z \mapsto z^{2}$, and the orbit map $S^{1} \to S^{1}$, $z \mapsto z^{2}$, is a two-fold covering. This is the standard example of a nontrivial two-fold covering and of the free involution that defines it.

**Example (the punctured line).** On $\mathbb{R} \setminus \{0\}$ the involution $x \mapsto -x$ is free, and the orbit map onto $(0,\infty)$ is a two-fold covering; the involution is the restriction of the map $x \mapsto -x$ of the line to the punctured line. The same map on the whole line is not free, and its orbit map is not a covering, because the fixed point $0$ has no evenly covered neighbourhood: the preimage of a connected neighbourhood of the class of $0$ is a single interval, not two.

**Example (the split covering).** On $X \times \{0,1\}$ the exchange of the two copies is a free involution, the orbit map is the projection $X \times \{0,1\} \to X$, which is a two-fold covering with two disjoint sheets; the covering is **trivial**, and its deck group is $\mathbb{Z}/2$.

**Example (a nonfree involution fails to cover).** On $[0,1]$ the involution $x \mapsto 1-x$ has the fixed point $\tfrac12$, so it is not free and its orbit map is not a covering: the preimage of a connected neighbourhood of the class of $\tfrac12$ is connected. The failure is local at the fixed set, and it is the reason the covering theory of a nonfree involution must be replaced by the Borel construction of the next article.

## Summary

A free continuous involution of a Hausdorff space has, at each point, an open neighbourhood $U$ with $U \cap \sigma(U) = \emptyset$, obtained by separating $x$ from $\sigma(x)$ and intersecting with a translate; the image $\pi(U)$ is then evenly covered, and the orbit map is a **two-fold covering**. Its fibres are the two-point orbits, its deck group is $\mathbb{Z}/2$ generated by the involution, and it acts transitively on each fibre, so the covering is regular. Conversely every two-fold covering of a connected base has deck group $\mathbb{Z}/2$, and the nontrivial deck transformation is a free involution whose orbit map is the covering; hence for a connected base the two-fold coverings are exactly the orbit maps of free involutions, up to homeomorphism over the base. The examples are the antipodal covering of projective space, the squaring cover of the circle, and the covering of the half-line by the punctured line; a nonfree involution has no such covering, and its fixed set is the obstruction.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| free involution | $\sigma(x) \neq x$ for all $x$; every orbit has two points |
| trivializing neighbourhood | Open $U$ with $U \cap \sigma(U) = \emptyset$ |
| covering map $p : E \to B$ | Every point of $B$ has an evenly covered neighbourhood |
| evenly covered, fibre | $p^{-1}(V) \cong V \times F$ over $V$; $F$ the fibre |
| two-fold covering | A covering with a two-point fibre |
| $\pi : X \to X/\sigma$ | The orbit map; a two-fold covering for free $\sigma$ and Hausdorff $X$ |
| deck transformation | Homeomorphism $\varphi$ of $E$ with $p\varphi = p$ |
| deck group | The group of deck transformations; $\mathbb{Z}/2$ for the orbit map |
| regular covering | Deck group acts transitively on each fibre |
| $z \mapsto z^{2}$ | The squaring cover $S^{1} \to S^{1}$, the orbit map of $z \mapsto -z$ |
| $S^{n} \to \mathbb{RP}^{n}$ | The antipodal two-fold covering |

## Further Reading

- Glen E. Bredon, *Topology and Geometry* (Springer, 1993), for covering maps, deck transformations and the orbit map of a free finite group action.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for covering spaces, the classification of coverings and the deck group.
- William S. Massey, *Algebraic Topology: An Introduction* (Springer, 1967; reprinted 1977), for two-fold coverings and the classification of coverings by the fundamental group.
- Tammo tom Dieck, *Transformation Groups* (de Gruyter, 1987), for free actions, principal bundles and the orbit map as a covering.
- Nicolas Bourbaki, *General Topology*, Chapters 1–4 (Springer, 1995), for the existence of invariant neighbourhoods and the quotient by a finite group action.
- John L. Kelley, *General Topology* (Van Nostrand, 1955; reprinted Springer, 1975), for coverings and the local structure of a quotient map.
