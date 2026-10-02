# __Equivariant Homotopy Theory__

## Introduction

Equivariant homotopy theory is the homotopy theory of spaces with a group action, in which the equivalences are the equivariant maps that are invertible up to equivariant homotopy. It is a finer theory than the ordinary homotopy theory of the underlying space: the circle with the reflection of $\mathbb{Z}/2$ and the circle with the trivial action are equivariantly distinct although both are weak homotopy equivalent to $S^1$, because their fixed sets differ. The objects that make the theory computable are the **fixed-point functors** $X\mapsto X^H$ for the closed subgroups $H$ of the group; the classes of the theory are the **$G$-CW complexes**, built from cells of the form $G/H\times D^n$; the fundamental theorem is the **equivariant Whitehead theorem**, which says that a $G$-map between $G$-CW complexes is a $G$-homotopy equivalence exactly when it is one on the fixed sets of all the subgroups; and the theory is a model category in which the weak equivalences are the maps inducing weak equivalences on all the fixed sets.

The article develops the theory. It introduces the orbit category and the fixed-point functors, defines the $G$-CW complexes and their cellular approximation, defines the equivariant homotopy groups $\pi_n^H$ and proves the equivariant Whitehead theorem, records the equivariant fibrations, cofibrations and coverings, describes the model structure on $G\text{-}\mathbf{Top}$ and contrasts it with the coarse theory of the Borel construction, and closes with the Burnside ring and the tom Dieck splitting. The point-set theory of equivariant maps, equivariant homotopies, the orbit space and the equivariant homotopy extension property is that of *Spaces with an Involution and the Orbit Space* and *Equivariant Maps and Equivariant Homotopy*, and is used freely; the model category of the ordinary homotopy theory, its axioms and its Quillen adjunctions are those of *Model Categories and Homotopy Theory*, whose formalism this article applies to the equivariant setting; the obstruction theory with Bredon coefficients is that of *Equivariant Obstruction Theory* of this category, and the Borel and Bredon cohomology theories are those of *Equivariant Cohomology*. The stable equivariant theory, the equivariant spectra and the equivariant $K$-theory are those of *Stable Homotopy Theory* and *Equivariant K-Theory*, named here only where the unstable category is compared with them.

Nothing analytic and nothing geometric is used. The group is a topological group, discrete in the combinatorial statements and compact Lie when the orbit types and the slices are discussed; the cells are cones on orbits, the homotopy theory is combinatorial, and no distance, no norm and no measure is chosen. Throughout, $G$ is a topological group acting on the left on a space, $H$ and $K$ are closed subgroups with $H$ ranging over the closed subgroups of $G$ when the fixed-set conditions are stated, $X^H$ is the **fixed set** of $H$, $G/H$ is the orbit, and $G\text{-}\mathbf{Top}$ is the category of $G$-spaces and $G$-maps. The orbit category is written $\mathcal{O}_G$, the equivariant homotopy groups $\pi_n^H(X,x)$, and the classifying spaces and the Borel construction are those of *Classifying Spaces and Cohomology Operations* and *Equivariant Cohomology*.

## The Orbit Category and the Fixed-Point Functors

### The Orbit Category

**Definition.** The **orbit category** $\mathcal{O}_G$ has as objects the homogeneous spaces $G/H$ for the closed subgroups $H$, and as morphisms the $G$-maps between them; a morphism $G/H \to G/K$ is determined by the image of the coset $H$, a point $gK$ with $g^{-1}Hg \subseteq K$, and the correspondences are the conjugations.

**Proposition.** The orbit category is small when the group is compact Lie and the subgroups are taken up to conjugacy and the homogeneous spaces are taken with the compact-open topology; it carries the isotropy information of every $G$-space, because every orbit of a $G$-space is a homogeneous space $G/H$, and a $G$-space is assembled from its orbits. The functors on $\mathcal{O}_G$ are the coefficient systems of the Bredon theory used in *Equivariant Obstruction Theory*.

*Proof.* An orbit $G\cdot x$ is the image of $G/H$ for $H$ the isotropy group of $x$, and the assignment is a homeomorphism of the orbit; a coefficient system is by definition a contravariant functor on $\mathcal{O}_G$. $\square$

### The Fixed-Point Functors

**Definition.** For a $G$-space $X$ and a closed subgroup $H$, the **fixed set** is

$$
X^H = \{x \in X : h\cdot x = x \text{ for all } h \in H\},
$$

with the subspace topology; the assignment $X\mapsto X^H$ is the **fixed-point functor** of $H$, and on a $G$-map it is the restriction.

**Proposition.** The fixed-point functors are homotopy functors and they detect the isotropy: the fixed set of the whole group is $X^G$, for $H \leq K$ one has $X^K \subseteq X^H$, and a $G$-homotopy $X\times I\to Y$ restricts to an ordinary homotopy $X^H\times I\to Y^H$, so each $X^H$ is an invariant of the equivariant homotopy type.

*Proof.* If $h\cdot x = x$ for all $h\in K$ then for all $h \in H\le K$, so $X^K\subseteq X^H$; the restriction of a $G$-homotopy is continuous and its endpoint conditions are the restrictions of the maps. $\square$

The collection of the functors $X\mapsto X^H$, one for each conjugacy class of subgroups, is the totality of the invariants of the equivariant homotopy theory: an equivariant map is an equivariant homotopy equivalence exactly when all of them are homotopy equivalences, which is the theorem of the section on the Whitehead theorem below.

## $G$-CW Complexes

### The Cells and the Attaching Maps

**Definition.** A **$G$-CW complex** is a $G$-space $X$ together with a filtration

$$
X^{-1} = \varnothing \subseteq X^0 \subseteq X^1 \subseteq \cdots \subseteq X, \qquad X = \bigcup_n X^n ,
$$

such that $X^n$ is obtained from $X^{n-1}$ by attaching **equivariant $n$-cells** $G/H_\alpha\times D^n$ along equivariant attaching maps $\varphi_\alpha : G/H_\alpha\times S^{n-1}\to X^{n-1}$, and such that a subset of $X$ is closed exactly when its preimage in every cell is closed (the weak topology). The space $X^n$ is the **$n$-skeleton**, and the $G$-CW complex is **finite** when there are finitely many cells.

Every orbit $G/H$ is a $G$-CW complex with one cell in dimension zero, and the **equivariant sphere** $S^n$ with a linear action of a finite group is a $G$-CW complex whose cells are indexed by the orbit types of the stabilisers.

**Proposition.** The quotient $X/G$ of a $G$-CW complex is a CW complex with one cell for each equivariant cell, and the fixed set $X^H$ is a CW complex; for $H\leq K$ the fixed sets are related by $X^K\subseteq X^H$. Consequently the ordinary homotopy type of every fixed set is that of a CW complex, and the invariants of the equivariant theory are computable by the ordinary cellular methods of *CW Complexes and Cellular Approximation*.

*Proof.* An equivariant cell $G/H_\alpha\times D^n$ has quotient $D^n$ and $H$-fixed set $G/H_\alpha^H\times D^n$, a disjoint union of cells or empty; the quotient and the fixed sets inherit the filtrations and the weak topology, so they are CW complexes with the stated cells. $\square$

### The Equivariant Cellular Approximation

**Theorem.** Every $G$-map between $G$-CW complexes is equivariantly homotopic to a cellular $G$-map, that is one carrying the $n$-skeleton to the $n$-skeleton for every $n$; and every equivariant homotopy between cellular $G$-maps is equivariantly homotopic rel the ends to a cellular homotopy.

*Proof.* The equivariant cellular approximation is the ordinary cellular approximation of *CW Complexes and Cellular Approximation* applied to the fixed sets and the orbits; the equivariant cells correspond to the cells of the quotient and the obstruction to pushing a map off the interior of a cell of dimension greater than the source lies in the equivariant homotopy groups of the target, which vanish in the appropriate range for a $G$-CW complex. The argument is the equivariant form of the standard one, using the equivariant homotopy extension property of *Equivariant Maps and Equivariant Homotopy*. $\square$

## Equivariant Homotopy Groups and the Whitehead Theorem

### The Groups

**Definition.** For a based $G$-space $(X,x)$ and a closed subgroup $H$, the **equivariant homotopy group** is

$$
\pi_n^H(X,x) = \pi_n(X^H, x), \qquad n \geq 0,
$$

the ordinary homotopy group of the fixed set based at $x$; a $G$-map $f$ induces $\pi_n^H(f) = \pi_n(f^H)$ for every $H$, and an equivariant homotopy induces the same maps. The family $\{\pi_n^H\}_H$ is the **equivariant homotopy** of $X$.

**Proposition.** The equivariant homotopy groups are functors on the equivariant homotopy category; for $H \leq K$ the inclusion $X^K\subseteq X^H$ gives natural maps $\pi_n^K(X)\to\pi_n^H(X)$, and for the trivial subgroup $H=1$ the group $\pi_n^1(X)$ is the ordinary homotopy group of the underlying space. A $G$-map that induces isomorphisms on $\pi_n^H$ for all $H$ and $n$ is a **weak $G$-equivalence**, and every weak $G$-equivalence between $G$-CW complexes is a $G$-homotopy equivalence.

*Proof.* The first statements are the functoriality of the ordinary homotopy groups applied to the fixed-set functors, and the naturality of the inclusions; the last is the equivariant Whitehead theorem proved next. $\square$

### The Equivariant Whitehead Theorem

**Theorem.** A $G$-map $f : X \to Y$ between $G$-CW complexes is a $G$-homotopy equivalence if and only if it is a weak $G$-equivalence, that is, if and only if $f^H : X^H\to Y^H$ is a weak homotopy equivalence for every closed subgroup $H$.

*Proof sketch.* If $f$ is a $G$-homotopy equivalence then each $f^H$ is a homotopy equivalence, hence a weak equivalence. Conversely, the equivariant cellular approximation factorises $f$ into a sequence of cell attachments, and the vanishing of the relative equivariant homotopy groups of the mapping cylinder, computed on the fixed sets, gives the existence of an equivariant homotopy inverse by the standard induction over the skeleta; the details use the equivariant homotopy extension property of *Equivariant Maps and Equivariant Homotopy* and the ordinary Whitehead theorem of *CW Complexes and Cellular Approximation* on each fixed set. $\square$

**Corollary.** The fixed-point functors jointly reflect and detect the equivariant homotopy equivalences of $G$-CW complexes: two $G$-CW complexes are $G$-homotopy equivalent exactly when the fixed sets $X^H$ and $Y^H$ are homotopy equivalent for every $H$ and the equivalences are compatible with the inclusions; and an equivariant map is a homotopy equivalence exactly when each of its fixed-set restrictions is one.

*Proof.* Apply the theorem to the equivariant map; the compatibility is the naturality of the functors. $\square$

## Fibrations, Cofibrations and Coverings

### Equivariant Fibrations

**Definition.** A $G$-map $p : E \to B$ is an **equivariant Hurewicz fibration** (a **$G$-fibration**) when it has the equivariant homotopy lifting property for every $G$-space: for every $G$-map $f : Z \to E$ and every equivariant homotopy $H : Z\times I\to B$ starting at $p\circ f$, there is an equivariant lift $\tilde H : Z\times I\to E$ starting at $f$ and covering $H$. The **$G$-cofibration** is the dual notion with the extension property.

**Theorem.** An equivariant fibration is an ordinary fibration on the underlying spaces and, by restriction, a fibration $E^H\to B^H$ on every fixed set; the $G$-fibrations are stable under pullback and composition, the $G$-cofibrations are stable under pushout and composition, and a $G$-fibration between $G$-CW complexes has a long exact sequence of equivariant homotopy groups

$$
\cdots \to \pi_n^H(F) \to \pi_n^H(E) \to \pi_n^H(B) \to \pi_{n-1}^H(F)\to\cdots
$$

for every $H$, with $F$ the fibre.

*Proof.* Restrict the lifting property to fixed sets and to $G$-spaces of the form $G/H\times Z$; the exact sequence is that of the ordinary fibration $E^H\to B^H$ from *Homotopy Groups and Fibrations*. $\square$

### Coverings and the Orbit Category

**Theorem.** A $G$-map that is an ordinary covering and an equivariant fibration is an **equivariant covering**; an equivariant covering of a $G$-space $X$ by a free $G$-space is classified by the functor on the fundamental groupoid of the orbit category, and for a free $G$-action the equivariant coverings of $X$ correspond to the ordinary coverings of the orbit space $X/G$ with the deck transformations extended to the action.

*Proof.* The classification is that of the ordinary covering theory of *Covering Spaces and the Fundamental Group*, applied over the orbit category and with the equivariant monodromy; the free case is the orbit-space correspondence of *Equivariant Maps and Equivariant Homotopy*. $\square$

## Orbit Types and the Slice Decomposition

### The Isotropy and the Orbit Type

**Definition.** For a $G$-space $X$ and $x \in X$ the **isotropy group** is $G_x = \{g : g\cdot x=x\}$, a closed subgroup of $G$, and the **orbit type** of $x$ is the conjugacy class $(G_x)$ of its isotropy group. For a conjugacy class $(H)$ the **orbit-type subspace** is

$$
X_{(H)} = \{x \in X : (G_x) = (H)\},
$$

the set of points whose isotropy is conjugate to $H$.

**Theorem.** The orbit types partition $X$, the isotropy is constant along an orbit, and the orbit $G\cdot x\cong G/G_x$; the orbit-type subspaces are $G$-invariant and $X_{(H)}$ is a single orbit type, so that the $G$-space is the disjoint union of its orbit-type strata, each of which is a single homogeneous orbit type when the action is transitive. A $G$-CW complex may be chosen with the cells $G/H_\alpha\times D^n$ having orbit type $(H_\alpha)$ in the interior of the disk, and then the orbit-type strata are unions of open cells.

*Proof.* If $y=g\cdot x$ then $G_y = gG_xg^{-1}$, so the isotropy is constant along the orbit up to conjugacy, and the orbit map $G/G_x\to G\cdot x$ is an equivariant homeomorphism; the partition and the invariance are immediate, and the cell statement follows by taking the isotropy groups of the cells of a $G$-CW structure. $\square$

### The Slice Theorem

**Theorem (slice theorem; standard).** Let a compact Lie group $G$ act on a completely regular space $X$ and let $x \in X$. Then there are a $G_x$-invariant neighbourhood $S$ of $x$ (a **slice**) and an equivariant homeomorphism of the associated bundle onto a neighbourhood of the orbit,

$$
G\times_{G_x} S \;\cong\; U, \qquad U \text{ a } G\text{-invariant neighbourhood of } G\cdot x ,
$$

which is the identity on the orbit; consequently the space is locally modelled on the twisted product of the orbit with the slice, and the action is determined near each orbit by the representation of the isotropy group on the slice.

*Proof.* The theorem of Mostow and Palais for compact Lie groups acting on a completely regular space; the construction of the slice uses a smooth or a finite-dimensional structure and a partition of unity, and is quoted rather than reproduced, the smooth tools being those of the geometry of a later Part. The consequence for the orbit-type decomposition and the local structure of an equivariant neighbourhood is what the article uses. $\square$

### The Equivariant Homotopy of the Orbits

**Theorem.** For closed subgroups $H,K \leq G$ the fixed set of $H$ in the orbit $G/K$ is

$$
(G/K)^H = \{gK : g^{-1}Hg \subseteq K\},
$$

whose connected components are the double cosets, so that $\pi_0^H(G/K)$ is the set of cosets $gK$ with $g^{-1}Hg\subseteq K$ with the base point $eK$ when it is fixed; for $K=1$ the orbit is free and $(G/K)^H$ is empty for $H\neq1$, while for the trivial orbit $G/G=\mathrm{pt}$ all the equivariant homotopy groups vanish. For $H\leq K$ the fixed set is a homogeneous space of the normalizer, and the higher equivariant homotopy groups of the orbit are those of that homogeneous space.

*Proof.* The fixed set is the set of cosets fixed by the $H$-action, which is the stated condition; the components are the double-coset decomposition of the condition, and the homogeneous-space description is that of the normalizer $N_G(K)$ acting on $G/K$; the vanishing at the trivial orbit is immediate. $\square$

The computation is the reason the representations of the isotropy groups control the equivariant homotopy: the cells are orbits and the attaching data of a $G$-CW complex lie in the equivariant homotopy groups of the orbits, which are the homotopy groups of the homogeneous spaces of the normalizers.

## The Model Structure

### Weak Equivalences and the Fixed-Set Functors

**Definition.** The **equivariant homotopy theory** of $G$ is the homotopy theory of $G\text{-}\mathbf{Top}$ in which a **weak equivalence** is a $G$-map $f$ whose fixed-set maps $f^H : X^H\to Y^H$ are weak homotopy equivalences for every closed subgroup $H$; the theory is the **fine** equivariant homotopy theory, and it is contrasted with the **coarse** theory in which a weak equivalence is a $G$-map whose underlying map is an ordinary weak equivalence.

**Theorem.** The fine weak equivalences are the weak equivalences of a closed model structure on $G\text{-}\mathbf{Top}$ in the sense of *Model Categories and Homotopy Theory*: the fibrant objects include the $G$-CW complexes, the cofibrant objects include the free $G$-spaces, the homotopy category is the equivariant homotopy category of *Equivariant Maps and Equivariant Homotopy* and *Equivariant Homotopy Theory* is the name of that category, and the orbit functors $X\mapsto X^H$ are Quillen functors.

*Proof.* The model structure is the projective model structure on the diagram category of the fixed-set functors over $\mathcal{O}_G$; the fibrations and cofibrations are the maps that are fibrations and cofibrations on every fixed set, and the axioms are transported from the ordinary model structure of *Model Categories and Homotopy Theory*. The details are the equivariant model-category theorem, quoted here. $\square$

### The Coarse Theory and the Borel Construction

**Remark.** The coarse equivariant homotopy theory, in which only the underlying weak equivalences count, is the theory of the quotient and of the Borel construction: the homotopy quotient of *Equivariant Cohomology* is its derived functor, and the coarse equivalences are exactly the $G$-maps that become weak equivalences after applying $EG\times_G(-)$. The Borel cohomology of *Equivariant Cohomology* is thus the invariant of the coarse theory, while the equivariant homotopy groups of this article are the invariants of the fine theory; the two agree for free actions and differ by the fixed-set information otherwise. The comparison of the two is the reason the Borel spectral sequence carries the fixed-set data of *The Mod 2 Cohomology of an Involution*.

So the choice of the class of weak equivalences is a choice of a homotopy theory, and the fine theory, generated by the fixed-set functors, is the one in which the orbit category and the isotropy of the action are visible.

## The Burnside Ring and the Splitting

**Definition.** The **Burnside ring** $A(G)$ of a finite group is the Grothendieck ring of the finite $G$-sets under disjoint union and cartesian product; its additive basis is the set of orbit types $G/H$, and its multiplication is induced by the product of the orbits.

**Theorem (tom Dieck splitting).** For a finite group $G$ and a based $G$-CW complex, the equivariant stable homotopy is split into the ordinary stable homotopy of the fixed sets of the subgroups: the $G$-equivariant stable homotopy groups split as a direct sum of the stable homotopy groups of the fixed sets, indexed by the conjugacy classes of subgroups with the Weyl-group quotients, and the splitting is the algebraic form of the orbit decomposition. In the unstable theory the analogous statements are the equivariant attachings along the orbits of $\mathcal{O}_G$, and the Burnside ring is the coefficient ring of the theory.

*Proof sketch.* The tom Dieck splitting follows from the isotropy separation of the $G$-spheres and the fact that the orbits generate the stable category; the statement is quoted, and it is the bridge from the unstable theory of this article to the equivariant stable theory of *Stable Homotopy Theory*. $\square$

## Examples

**Example (the involution on the sphere).** Let $G = \mathbb{Z}/2$ act on $S^n$ by the antipodal map. The fixed set is empty for the whole group, and the fixed set of the trivial subgroup is the sphere; the equivariant homotopy is therefore the ordinary homotopy of $S^n$ together with the emptiness of the fixed set, and the action is fine-equivalent to the free action. The quotient is $\mathbb{RP}^n$, whose invariants are the coarse ones of the Borel construction.

**Example (the reflection).** Let $G = \mathbb{Z}/2$ act on $S^n$ by reflection in an equatorial $S^{n-1}$. Then the fixed set is $S^{n-1}$, and the equivariant homotopy groups of the whole group are the homotopy groups of $S^{n-1}$; the action is not fine-equivalent to any free action, the fixed set being non-empty, and the coarse quotient is the disk. The two involutions of this and the previous example have the same coarse quotient type in low dimensions and are distinguished by the fixed set, which is the content of the fine theory.

**Example (the classifying space).** For any $G$, the space $EG$ is a free $G$-CW complex, so its fixed sets $EG^H$ are empty for $H \neq 1$ and $EG^1 = EG$ is contractible; it is fine-equivalent to a point, consistently with its use as the universal free space, while its coarse theory is the classifying space $BG$.

## Summary

Equivariant homotopy theory is the homotopy theory of $G\text{-}\mathbf{Top}$ whose equivalences are detected by the fixed-point functors $X\mapsto X^H$; the orbit category $\mathcal{O}_G$ carries the isotropy, the $G$-CW complexes are built from cells $G/H\times D^n$, and every $G$-map between them is equivariantly homotopic to a cellular map. The equivariant homotopy groups $\pi_n^H(X)=\pi_n(X^H)$ are the ordinary homotopy groups of the fixed sets, and the equivariant Whitehead theorem says that a $G$-map between $G$-CW complexes is a $G$-homotopy equivalence exactly when it is a weak equivalence on every fixed set. Equivariant fibrations are fibrations on every fixed set and yield long exact sequences of the equivariant homotopy groups; equivariant coverings correspond, for free actions, to the coverings of the orbit space. The fine weak equivalences form a closed model structure on $G\text{-}\mathbf{Top}$ in the sense of *Model Categories and Homotopy Theory*, whose homotopy category is the equivariant homotopy category of *Equivariant Maps and Equivariant Homotopy*; the coarse theory, in which only the underlying weak equivalences count, is the theory of the Borel construction of *Equivariant Cohomology*, and the two theories agree for free actions and differ by the fixed-set information otherwise. The Burnside ring and the tom Dieck splitting are the algebraic expression of the orbit decomposition and the bridge to the stable theory. Nothing analytic and nothing geometric was used.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G\text{-}\mathbf{Top}$ | Category of $G$-spaces and $G$-maps |
| $G/H$ | Orbit, a homogeneous space; an object of the orbit category |
| $\mathcal{O}_G$ | Orbit category; its functors are the Bredon coefficient systems |
| $X^H$ | Fixed set of the closed subgroup $H$ |
| $G_x$, $(G_x)$, $X_{(H)}$ | Isotropy group, orbit type, orbit-type subspace |
| slice $S$, $G\times_{G_x}S$ | Slice at a point and the local model of the action |
| $X\mapsto X^H$ | Fixed-point functor; an invariant of the equivariant homotopy type |
| $G/H\times D^n$, $G/H\times S^{n-1}$ | Equivariant cell and its attaching sphere |
| $G$-CW complex, $X^n$ | Equivariant CW complex and its $n$-skeleton |
| $\pi_n^H(X,x) = \pi_n(X^H,x)$ | Equivariant homotopy groups |
| weak $G$-equivalence | $G$-map whose fixed-set maps are weak equivalences |
| $G$-homotopy equivalence iff weak on every $X^H$ | Equivariant Whitehead theorem |
| $G$-fibration, $G$-cofibration | Equivariant homotopy lifting and extension properties |
| fine vs coarse weak equivalences | Detected by all fixed sets vs by the underlying space only |
| $A(G)$ | Burnside ring; the tom Dieck splitting |

## Further Reading

- Tammo tom Dieck, *Transformation Groups* (de Gruyter, 1987), for $G$-CW complexes, the equivariant Whitehead theorem and the Burnside ring.
- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for the fixed-point functors, the orbit types and the equivariant homotopy theory.
- Glen E. Bredon, *Equivariant Cohomology Theories* (Lecture Notes in Mathematics 34, Springer, 1967), for the Bredon coefficients and the fine invariants.
- J. Peter May, *Equivariant Homotopy and Cohomology Theory* (CBMS Regional Conference Series 91, 1996), for the equivariant model structure, the orbit category and the stable theory.
- Peter S. Hirschhorn, *Model Categories and Their Localizations* (AMS, 2003), for the model-category machinery of the fine and coarse equivariant structures.
- George W. Whitehead, *Elements of Homotopy Theory* (Springer, 1978), for the ordinary homotopy theory, the fibrations and the Whitehead theorem that the equivariant case generalises.
