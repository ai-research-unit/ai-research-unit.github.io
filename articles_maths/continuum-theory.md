
# __Continuum Theory__

## Introduction

A **continuum** is a compact connected Hausdorff space, and continuum theory is the study of these spaces and of their subcontinua. The subject is the meeting point of the two properties developed in *Topological Spaces*: connectedness, which forbids a separation into two disjoint nonempty open pieces, and compactness, which supplies the finite intersection property, the accumulation of decreasing families, and the preservation of the structure under continuous images and products. The interval and the circle are continua, and so is every product of continua; the plane is not a continuum, but its subcontinua are the objects of the classical plane topology, in which the separation of the plane by a simple closed curve and the structure of the indecomposable continua are the two poles of the theory.

An indecomposable continuum is a continuum that is not the union of two proper subcontinua. Such spaces, of which the bucket-handle continuum, the solenoids and the pseudo-arc are the standard examples, have properties that are counterintuitive from the metric point of view: every proper subcontinuum has empty interior, the composants are pairwise disjoint dense sets, and the space is nevertheless connected and compact. Peano continua, the locally connected continua, behave in the opposite way and are exactly the continuous images of the interval, by the Hahn–Mazurkiewicz theorem.

This article develops the elementary properties of continua, the Peano continua and the Hahn–Mazurkiewicz theorem, the separation and unicoherence theory, the indecomposable continua with their composants, and the hereditarily indecomposable continua with the pseudo-arc. The dynamical systems that use the indecomposable continua as attractors belong to Part III, where the limits and the invariant measures are available; the hyperspaces of continua, the Vietoris topology on the closed subsets and the continuum-valued maps belong to the topology on groups and the algebraic topology of this Part, where the relevant constructions are made. No measure, integral, derivative or analytic limit is used, and no physics is invoked.

## Continua

### Definition and Elementary Properties

**Definition.** A **continuum** is a compact connected Hausdorff space, and a **subcontinuum** of a continuum $X$ is a subset that is a continuum in the subspace topology. A continuum is **degenerate** if it is a singleton and **nondegenerate** otherwise. An **arc** is a continuum homeomorphic to the interval $[0,1]$, a **simple closed curve** is a continuum homeomorphic to the circle $S^1$, and an **$n$-cell** is a continuum homeomorphic to the cube $[0,1]^n$. A **Peano continuum** is a metrisable continuum that is locally connected, and a **continuum in a space** $Y$ is a subcontinuum of $Y$.

The metrisability in the definition of a Peano continuum is needed for the Hahn–Mazurkiewicz theorem and for most of the classical theory; the general continuum is a compact connected Hausdorff space, and the compactness and the connectedness alone already give the elementary results below.

**Theorem.** The following hold:

**(i)** the continuous image of a continuum is a continuum;

**(ii)** the product of a nonempty family of continua is a continuum;

**(iii)** the intersection of a decreasing family of continua is a continuum, and if the family is directed by inclusion then the intersection is a continuum;

**(iv)** the union of a chain of continua is a continuum if its closure is taken, and the union of a directed family of continua with a point in common is a continuum;

**(v)** every component of a compact Hausdorff space is a continuum, and the components of a compact Hausdorff space are the quasi-components.

**Proof.** (i) is the preservation of compactness and connectedness by continuous images, both proved in *Topological Spaces*. (ii) is Tychonoff's theorem together with the connectedness of a product, also in *Topological Spaces*, and for finitely many factors it is the same statement. (iii) is the finite intersection property for the closed sets of a compact space, applied to the members of the family together with the requirement that no separation exists: an intersection of connected sets in a compact Hausdorff space is connected when the family is directed, because a separation of the intersection would produce, by compactness and the directedness, a separation of a member of the family. (iv) is the closure of a connected set being connected, together with the union theorem for connected sets with a common point. (v) is that a component is closed and hence compact in a compact space, and that a compact Hausdorff space is normal, whence its components and quasi-components coincide by the standard theorem on the coincidence of the two notions in compact Hausdorff spaces. $\square$

**Remark.** The intersection of two continua with connected union is connected, but the intersection of two continua need not be connected and need not be a continuum; the standard example is the union of a circle of large radius and a circle of small radius tangent to it, whose intersection is a point, compared with two arcs of a circle meeting in two points, whose intersection is disconnected. The connectedness of the intersection of two continua whose union is connected is the property of **unicoherence**, developed in the third section.

**Theorem.** Every metrisable continuum with more than one point is the continuous image of the Cantor set, and every nondegenerate continuum contains a subcontinuum that is **irreducible** between two of its points, meaning that no proper subcontinuum of it contains both points.

**Proof.** A compact metrisable space is a continuous image of the Cantor set, by the standard construction of a surjection from the Cantor set onto the space, and a continuum that is a continuous image of a continuum with more than one point has more than one point; for a general compact Hausdorff continuum there is no such surjection from the Cantor set, since a continuous image of the Cantor set is metrisable. For the irreducible subcontinuum, order the subcontinua containing a fixed pair of distinct points by reverse inclusion and apply Zorn's lemma: the intersection of a chain of subcontinua containing the two points is a subcontinuum containing them by (iii), so a minimal element exists, and a minimal subcontinuum containing two points is irreducible between them. $\square$

### Cut Points and the Structure of Arcs

**Definition.** A point $x$ of a continuum $X$ is a **cut point** if $X \setminus \{x\}$ is disconnected; otherwise $x$ is a **non-cut point**. A continuum is **hereditarily unicoherent** if every subcontinuum is unicoherent in the sense of the third section.

**Theorem.** Every nondegenerate continuum has at least two non-cut points; the interval has exactly two, namely its endpoints; the circle has none; and a nondegenerate continuum that has exactly two non-cut points is an arc.

The existence of the two non-cut points is due to Moore, and the characterisation of the arc by the two non-cut points is the classical theorem of the theory; the proofs are in the references.

**Definition.** Let $X$ be a continuum and let $A, B \subseteq X$. One says that $A$ **separates** $B$ from $C$ in $X$ if $B$ and $C$ lie in different components of $X \setminus A$. A continuum is **irreducible** between $x$ and $y$ when no proper subcontinuum contains both points, and it is **irreducible about** $A$ when every proper subcontinuum misses $A$.

**Example (the arc, the circle and the figure eight)**. The circle is the simplest continuum with no cut points; the figure-eight curve, the union of two circles meeting at a point, is a continuum whose only cut point is the point of tangency; and the interval is the continuum with two non-cut points. These three continua show that the number of non-cut points distinguishes the arc, the circle and the curves that are unions of simple closed curves.

## Peano Continua

### Local Connectedness

**Definition.** A space $X$ is **locally connected** if every point has a neighbourhood base of connected neighbourhoods, and **locally path connected** if every point has a neighbourhood base of path connected neighbourhoods. A **Peano continuum** is a metrisable continuum that is locally connected, and a **Peano space** is a compact connected locally connected metric space.

**Theorem (Hahn–Mazurkiewicz).** A metrisable space $X$ is a continuous image of the interval $[0,1]$ if and only if it is a nonempty Peano continuum, that is, nonempty, compact, connected, locally connected and metrisable.
**Proof sketch.** If $f : [0,1] \to X$ is continuous and surjective then $X$ is compact, connected and metrisable as a continuous image, and it is locally connected: a compact metric space is locally connected exactly when for every $\varepsilon > 0$ it is covered by finitely many connected sets of diameter less than $\varepsilon$, a property preserved by a continuous surjection (equivalently, $[0,1]$ is locally connected and the map is closed by compactness). Conversely, for a Peano continuum one constructs by recursion a sequence of finite open covers by connected sets of diameter tending to zero and a sequence of polygonal approximations whose uniform limit is a surjection from the interval; local connectedness supplies the connected refinements and compactness supplies the convergence. The theorem is due to Hahn and Mazurkiewicz, and the proof is in the references. $\square$

**Corollary.** Every Peano continuum is a continuous image of the circle as well, every nondegenerate Peano continuum contains an arc, and every Peano continuum is arcwise connected and locally arcwise connected.

**Proof.** The circle maps onto the interval, and the interval maps onto a nondegenerate Peano continuum, so the circle maps onto it too. A connected, locally connected compact metric space is arcwise connected, by joining any two points through a chain of connected neighbourhoods, and a nondegenerate Peano continuum contains an arc: it is arcwise connected, the image of a nonconstant path is again a Peano continuum, and applying the same construction inside that image produces a path that is injective on a subinterval, hence an arc. $\square$

**Example.** The interval, the circle, the $n$-cells, the spheres and the finite graphs are Peano continua. The topologist's sine curve of *Topological Spaces* is a continuum that is not a Peano continuum, since it is not locally connected at the points of the limiting segment. The Hilbert cube is a Peano continuum, being the countable product of intervals. The **Warsaw circle** is the union of the closed topologist's sine curve with an arc joining its two endpoints, and the **comb space** is the union of the base interval $[0,1]\times\{0\}$, the segment $\{0\}\times[0,1]$ and the segments $\{1/n\}\times[0,1]$ for $n\geq1$; both are continua that are not Peano continua, neither being locally connected at the points of the limiting segment, and the Warsaw circle has the Čech cohomology of a circle without being homotopy equivalent to one while the comb space is contractible.

## Separation and Unicoherence

### Unicoherent Continua

**Definition.** A continuum $X$ is **unicoherent** if for all subcontinua $A, B \subseteq X$ with $A \cup B = X$ the intersection $A \cap B$ is connected, and **hereditarily unicoherent** if every subcontinuum is unicoherent. A **triod** is a continuum that is the union of three proper subcontinua any two of which have a connected intersection.

**Example.** The interval and every subcontinuum of it are hereditarily unicoherent: a subcontinuum of $[0,1]$ is an interval, the union of two intervals is an interval only if they overlap, and the intersection of two intervals is an interval, hence connected. The circle is not unicoherent: it is the union of two closed arcs whose intersection consists of the two endpoints, a disconnected set. The figure-eight curve is unicoherent, its only cut point being the point of tangency, but it is not hereditarily unicoherent, since it contains the circle.

**Theorem.** Every indecomposable continuum is unicoherent, and every hereditarily indecomposable continuum is hereditarily unicoherent. A hereditarily unicoherent continuum contains no simple closed curve; a continuum that contains no simple closed curve and no triod is hereditarily unicoherent.

**Proof.** For the first statement, if an indecomposable continuum were the union of two subcontinua meeting in a disconnected set, the two components of the intersection would produce a decomposition of the continuum into two proper subcontinua, contradicting indecomposability; this is the classical argument of the theory. The second statement is that a simple closed curve is not unicoherent, so a hereditarily unicoherent continuum cannot contain one. The third is the standard characterisation of hereditary unicoherence for continua, proved by decomposing a supposed separation of an intersection and using the absence of a circle or a triod. $\square$

### Separation in the Plane

**Theorem (Jordan curve theorem).** A simple closed curve in the plane separates the plane into exactly two components, one bounded and one unbounded, and the curve is the boundary of each.

**Theorem.** An arc in the plane does not separate the plane, and more generally a continuum in the plane whose complement is connected does not separate the plane; a continuum in the plane separates the plane if and only if its complement is disconnected, and the bounded components of the complement are then precisely the bounded complementary domains.

The Jordan curve theorem and the plane separation theorems are proved by the methods of algebraic topology, using the degree of a map of the circle, and the proofs belong to the algebraic topology of this Part; the statements are the classical ones of plane continuum theory and are used here as the standard input for the examples.

**Remark.** The separation theory of the plane is the reason the unicoherence of the continua of the plane is a sharp property in the classical theory: a plane continuum is unicoherent exactly when, for every simple closed curve in the continuum, the curve does not separate the plane in the manner detected by the continuum, and the indecomposable plane continua are precisely the plane continua that are irreducible between suitable pairs of points. The precise statements are in the standard references; the present article records only the definitions and the role of unicoherence.

## Indecomposable Continua

### Decompositions and Composants

**Definition.** A continuum $X$ is **decomposable** if $X = A \cup B$ with $A$ and $B$ proper subcontinua of $X$, and **indecomposable** otherwise. A **composant** of an indecomposable continuum $X$ is the union of all proper subcontinua containing a fixed point $x$, written $\kappa(x)$; a continuum is **hereditarily indecomposable** if every subcontinuum is indecomposable.

**Theorem.** For a continuum $X$ with more than one point the following are equivalent:

**(i)** $X$ is indecomposable;

**(ii)** every proper subcontinuum of $X$ has empty interior.

**Proof.** If $X$ is decomposable, $X = A \cup B$ with $A$ and $B$ proper subcontinua, and at least one of them has nonempty interior, since a compact Hausdorff space is not the union of two closed sets with empty interior, by the Baire category theorem of *Baire Spaces and Category*; so (i) implies (ii). The converse is the classical theorem of the theory: a proper subcontinuum with nonempty interior is separated from its complement along its boundary, and the separation produces two proper subcontinua whose union is $X$. The proof is in the references. $\square$

**Theorem.** Let $X$ be a nondegenerate indecomposable continuum and define $x \sim y$ if $x = y$ or some proper subcontinuum of $X$ contains both points. Then $\sim$ is an equivalence relation whose classes are the **composants**, each composant is connected and dense in $X$, distinct composants are disjoint, and for a metrisable $X$ there are exactly $\mathfrak{c}$ composants.

**Proof.** Transitivity: if a proper subcontinuum $A$ contains $x, y$ and a proper subcontinuum $B$ contains $y, z$, then $A \cup B$ is a continuum containing $y$; were $A \cup B = X$, the continuum would be the union of the two proper subcontinua $A$ and $B$, contradicting indecomposability, so $A \cup B$ is a proper subcontinuum containing $x$ and $z$. A composant is a union of connected sets with the common point $x$, hence connected. Denseness and the count $\mathfrak{c}$ of the composants are the classical theorems of the theory: a proper subcontinuum has empty interior, so the composants are dense and there are at least two of them, and the standard cardinality theorem gives exactly $\mathfrak{c}$ composants in the metrisable case. $\square$

**Corollary.** A nondegenerate indecomposable continuum is irreducible between any two points that lie in different composants; in particular every indecomposable continuum is irreducible between some pair of its points.

**Proof.** Two points lie in the same composant exactly when a proper subcontinuum contains both, by the definition of the composant relation, so two points in different composants are contained together in no proper subcontinuum, which is irreducibility between them. Distinct composants exist because there are at least two, and the pair may be chosen from two different ones. $\square$

### The Standard Indecomposable Continua

**Example (the bucket-handle continuum).** The **bucket-handle continuum** is the classical plane indecomposable continuum of Brouwer, Janiszewski and Knaster: it is obtained from the Cantor set projected onto an interval of the plane, and it is the closure of a suitable pair of spiralling arcs, one of them the handle of the name. It is a nondegenerate indecomposable continuum whose proper subcontinua have empty interior, and it is also an inverse limit of an inverse sequence of intervals, as every indecomposable plane continuum of this kind is; its composants are the standard illustration of the general theory. The example is the first and simplest of the indecomposable continua.

**Example (the solenoids).** Let $(n_k)$ be a sequence of integers $n_k \geq 2$ and let the **solenoid** $S$ be the inverse limit of the inverse sequence of circles
$$
S^1 \xleftarrow{z \mapsto z^{n_1}} S^1 \xleftarrow{z \mapsto z^{n_2}} S^1 \leftarrow \cdots .
$$
The solenoid is a continuum, and it is indecomposable for every sequence with $n_k \geq 2$; the **dyadic solenoid**, with all $n_k = 2$, is the standard example. The solenoid is a compact connected group in its inverse limit topology, and its group structure belongs; the continuum theory records that it is homogeneous and not a Peano continuum, being not locally connected at any point.

**Example (the pseudo-arc).** A continuum is **arc-like**, or **chainable**, if it is the inverse limit of an inverse sequence of intervals with surjective bonding maps. The **pseudo-arc** is the unique arc-like hereditarily indecomposable continuum with more than one point; it is homogeneous, meaning that for any two of its points there is a homeomorphism carrying one to the other; it contains no arc, although it is arc-like; and it is homeomorphic to each of its nondegenerate subcontinua. The uniqueness and the homogeneity are theorems of Bing and Moise, and the construction of the pseudo-arc is by a careful inverse limit of intervals with bonding maps that wind back and forth.

### Hereditarily Indecomposable Continua

**Theorem.** A hereditarily indecomposable continuum is unicoherent and contains no simple closed curve and no triod; and every subcontinuum of a hereditarily indecomposable continuum is hereditarily indecomposable.

**Proof.** Every subcontinuum is indecomposable by hypothesis, and every indecomposable continuum is unicoherent by the theorem of the third section, so the continuum is hereditarily unicoherent; the absence of a simple closed curve and of a triod is then the characterisation of hereditary unicoherence in that section. The final statement is the definition. $\square$

**Theorem (Bing).** The pseudo-arc is the unique arc-like hereditarily indecomposable continuum with more than one point; every hereditarily indecomposable continuum with more than one point contains no arc; and every homogeneous hereditarily indecomposable continuum with more than one point is the pseudo-arc.

The theorems are due to Bing and to Moise and are the central results of the theory of the hereditarily indecomposable continua; the proofs use the inverse limit constructions and the approximation of homeomorphisms by maps that preserve the small links of a chain cover, and they are in the references.

**Remark.** The relation of the continuum theory to the dynamical systems is through the inverse limits: an inverse limit of intervals or of circles with bonding maps that are not monotone produces the indecomposable continua, and the attractors of the dynamical systems of Part III are frequently of this form. The theory of the attractors, of their invariant measures and of their periodic points belongs to Part III, where the limit and the measure are available; the present article supplies the topological objects that the theory uses, and its results on the inverse limits are exactly the ones that the dynamical theory quotes.

**Remark.** The continua are the compact connected objects of this Part, and the two categories of them, the decomposable and the indecomposable, behave in opposite ways: a decomposable continuum is the union of two proper subcontinua and hence admits a decomposition into smaller pieces, while in an indecomposable continuum the proper subcontinua are small in the strong sense of having empty interior and are organised into the pairwise disjoint dense composants. The hereditarily indecomposable continua are those for which the phenomenon persists in every subcontinuum, and the pseudo-arc shows that the phenomenon is compatible with arc-likeness, with homogeneity and with the failure to contain an arc. The separation theory of the plane and the hyperspace theory of the closed subsets of a continuum are the two further developments of the theory, and they belong to the algebraic topology and the topology on groups of this Part.

## Summary

A **continuum** is a compact connected Hausdorff space; a **subcontinuum** is a subset that is a continuum; an **arc** is a continuum homeomorphic to $[0,1]$; a **simple closed curve** is one homeomorphic to the circle; and a **Peano continuum** is a metrisable locally connected continuum. The class of continua is closed under continuous images, arbitrary products, decreasing and directed intersections, and the closures of chains and directed unions; the components of a compact Hausdorff space are continua and coincide with the quasi-components; and every nondegenerate continuum contains a subcontinuum **irreducible** between two of its points. Every nondegenerate continuum has at least two **non-cut points** (Moore), and a nondegenerate continuum with exactly two of them is an **arc**. By the **Hahn–Mazurkiewicz theorem** a metrisable space is a continuous image of $[0,1]$ exactly when it is a nonempty Peano continuum, so every Peano continuum is arcwise connected and contains an arc.

A continuum $X$ is **unicoherent** if the intersection of any two subcontinua whose union is $X$ is connected, and **hereditarily unicoherent** if every subcontinuum is; the interval is hereditarily unicoherent and the circle is not, and a hereditarily unicoherent continuum contains no simple closed curve, the locally connected ones among them being the dendrites. The **Jordan curve theorem** states that a simple closed curve separates the plane into a bounded and an unbounded component; an arc does not separate the plane. A continuum is **decomposable** if it is the union of two proper subcontinua and **indecomposable** otherwise; an indecomposable continuum has no proper subcontinuum with nonempty interior, is irreducible between any two points in different composants, is unicoherent, and is partitioned into its **composants**, pairwise disjoint dense connected sets, $\mathfrak{c}$ in number for a nondegenerate metrisable continuum. The **bucket-handle** continuum, the **solenoids** and the **pseudo-arc** are the standard examples; a continuum is **hereditarily indecomposable** if every subcontinuum is indecomposable, every such continuum is hereditarily unicoherent and contains no arc, and by **Bing's theorem** the pseudo-arc is the unique arc-like hereditarily indecomposable continuum with more than one point, as well as the unique homogeneous one. The continuum-theoretic input to the dynamical systems of Part III is the inverse limit construction and the indecomposable continua it produces.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| continuum | Compact connected Hausdorff space |
| subcontinuum | Closed connected subset that is a continuum |
| nondegenerate | Having more than one point |
| arc, simple closed curve, $n$-cell | Homeomorphs of $[0,1]$, $S^1$, $[0,1]^n$ |
| Peano continuum | Metrisable locally connected continuum |
| cut point | $X \setminus \{x\}$ disconnected |
| non-cut point | $X \setminus \{x\}$ connected |
| irreducible between $x,y$ | No proper subcontinuum contains both |
| unicoherent | $A \cup B = X$ subcontinua $\Rightarrow A \cap B$ connected |
| hereditarily unicoherent | Every subcontinuum unicoherent |
| triod | Union of three subcontinua with pairwise connected intersections |
| decomposable, indecomposable | Union of two proper subcontinua; otherwise |
| composant $\kappa(x)$ | Union of the proper subcontinua containing $x$ |
| hereditarily indecomposable | Every subcontinuum indecomposable |
| arc-like (chainable) | Inverse limit of intervals with surjective bonding maps |
| pseudo-arc | Unique arc-like hereditarily indecomposable nondegenerate continuum |
| solenoid | Inverse limit of circles with bonding maps $z \mapsto z^{n_k}$ |
| inverse limit | Subspace of the product of the terms of an inverse system |



## Further Reading

- K. Kuratowski, *Topology*, Volume II (Academic Press, 1968), for the classical theory of the continua and the separation theorems of the plane.
- Sam B. Nadler, Jr., *Continuum Theory: An Introduction* (Monographs and Textbooks in Pure and Applied Mathematics 158, Marcel Dekker, 1992), for the systematic account of continua, composants and indecomposable continua.
- Gordon Thomas Whyburn, *Analytic Topology* (American Mathematical Society Colloquium Publications 28, American Mathematical Society, 1942), for the Peano continua, the unicoherence and the separation theory.
- R. H. Bing, "Concerning Hereditarily Indecomposable Continua", *Transactions of the American Mathematical Society* 71 (1951), 267–273, for the pseudo-arc and its uniqueness.
- Edwin E. Moise, "A Note on the Pseudo-Arc", *Transactions of the American Mathematical Society* 67 (1949), 248–254, for the homogeneity of the pseudo-arc.
- R. H. Bing, "A Homogeneous Indecomposable Plane Continuum", *Duke Mathematical Journal* 15 (1948), 729–742, for the construction of the homogeneous indecomposable continua.
- James Dugundji, *Topology* (Allyn and Bacon, 1966), for the Hahn–Mazurkiewicz theorem and the elementary theory of the continua.
