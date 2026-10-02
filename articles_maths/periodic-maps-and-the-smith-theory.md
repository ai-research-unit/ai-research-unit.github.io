
# __Periodic Maps and the Smith Theory__

## Introduction

A **periodic map** of prime order $p$ is a homeomorphism $g$ with $g^p = \mathrm{id}$ and $g\neq\mathrm{id}$; the group it generates is $\mathbb{Z}/p$, and its fixed set is the object of the **Smith theory**. The theory says that the fixed set of a $\mathbb{Z}/p$ action on a mod $p$ homology sphere is again a mod $p$ homology sphere of lower dimension, that the parity of the difference of the dimensions is constrained, and that the equivariant homology of the action is concentrated on the fixed set. This article develops the fixed-set theorem, the Smith exact sequences and the localisation theorem.

Two things motivate the subject. First, the fixed-set theorem is the qualitative input of the equivariant classification: it tells, before any surgery, that the fixed set of an action on a sphere is a sphere-like object of constrained dimension, and it is the reason the periodic knots of *Equivariant Knot Theory* have an axis. Second, the localisation theorem is the algebraic heart of the equivariant theory: it identifies the equivariant homology with the homology of the fixed set after inverting the classes of positive degree in $H^*(BG)$, and it is the mechanism by which the equivariant invariants are computable.

**The article assumes** the homology and cohomology with field coefficients, the Borel construction and the Serre spectral sequence from *The Leray–Serre Spectral Sequence and the Serre Classes*, the fixed-set theory of *Involutions on Manifolds and Equivariant Surgery*, and the representation theory of the cyclic group $\mathbb{Z}/p$ (*Linear Spaces*, Part I).

**The boundaries of the article.** The structure of a locally linear involution and its equivariant surgery are *Involutions on Manifolds and Equivariant Surgery*; the classification of the involutions of a surface is *The Classification of Involutions on Surfaces*; the free case is *Free Involutions and Lens Spaces*; the periodic knots are *Equivariant Knot Theory*. The equivariant homotopy theory of a compact Lie group, the equivariant stable homotopy and the completions are *Stable Homotopy Theory* and the modern equivariant literature; the cobordism of group actions is *Involutions and the Cobordism of Group Actions*. The differentiable and PL refinements are Part III.

## Periodic Maps and their Fixed Sets

**Definition.** A **periodic map** on a space $X$ is a homeomorphism $g$ of finite order; when the order is a prime $p$ the group is $\mathbb{Z}/p$ and the map is a **$\mathbb{Z}/p$-action**. The **fixed set** is $F = X^{\mathbb{Z}/p} = \{x : gx = x\}$, and $X$ is a **mod $p$ homology $n$-sphere** if $H_*(X;\mathbb{F}_p)\cong H_*(S^n;\mathbb{F}_p)$.

**Theorem (Smith's fixed-set theorem).** Let $\mathbb{Z}/p$ act on a finite-dimensional space $X$ which is a mod $p$ homology $n$-sphere. Then the fixed set $F$ is a mod $p$ homology $r$-sphere for some $r$ with $-1\leq r\leq n$, where $r = -1$ means $F = \varnothing$; if $p$ is odd then $n-r$ is even, and if $p = 2$ then $n-r$ may be any nonnegative integer. In particular $F$ is nonempty whenever the action is not free, and the dimension of $F$ is constrained by the dimension of $X$ and the prime.

**Proof sketch.** The proof is by induction on the dimension and on the order, using the Smith sequences below: the fixed set of a $\mathbb{Z}/p$ action on a mod $p$ homology sphere is again a mod $p$ homology sphere, because the localisation of the equivariant homology at the prime $p$ equals the homology of the fixed set, and the homological dimension drops by an even amount for odd $p$ by the representation theory of $\mathbb{Z}/p$ over $\mathbb{F}_p$ (the group ring is a truncated polynomial ring, whose indecomposable modules have even dimension for odd $p$). The induction realises the bound $r\leq n$.

**Corollary (actions on spheres).** A nontrivial $\mathbb{Z}/p$ action on $S^n$ has a nonempty fixed set unless it is free; for $p$ odd the fixed set is a mod $p$ homology sphere of dimension $r\equiv n\pmod 2$, in particular on $S^3$ a circle or empty, and for $p=2$ it is a mod $2$ homology sphere of dimension $0,1,2,3$, in particular on $S^3$ a circle, a two-sphere, two points or empty. The list is the one used in the classification of the periodic knots and in the theory of the free involutions.

**Proof.** The theorem gives the fixed set as a mod $p$ homology sphere of dimension at most $n$ with the parity constraint, and the low-dimensional cases are read off: on $S^3$ the fixed set of a $p$-group action is a mod $p$ homology sphere of dimension $r\leq3$ with $3-r$ even for odd $p$, so $r\in\{1,3\}$ or empty, and a three-dimensional fixed set would be all of $S^3$, excluded by nontriviality; the case $p=2$ allows $r\in\{0,1,2,3\}$.

**Theorem (fixed points of acyclic actions).** Let a finite $p$-group act on a finite-dimensional mod $p$ acyclic space $X$ (so that $H_*(X;\mathbb{F}_p)$ is that of a point). Then $F$ is nonempty and mod $p$ acyclic. In particular a nontrivial action of a $p$-group on a disc has a fixed point.

**Proof sketch.** The statement is a corollary of the fixed-set theorem applied to the cone or of the localisation theorem; the inductive proof uses the Smith sequences to show that a free action on an acyclic space would force a contradiction with the Euler characteristic of the group ring over $\mathbb{F}_p$. The theorem is Smith's, and it is the origin of the "fixed points of $p$-group actions on discs" that underlies the local-linear structure.

## The Smith Sequences

**Theorem (the Smith sequences).** Let $\mathbb{Z}/p$ act on a space $X$ and let $F\subseteq X$ be the fixed set. Then there are long exact sequences, the **Smith sequences**, relating the homology of $X$, of the quotient $X/\mathbb{Z}/p$ and of $F$ with coefficients $\mathbb{F}_p$, whose maps are the quotient map, the inclusion of the fixed set and the transfer, and which express the fixed set as the "defect" of the action:
$$
H_*(X;\mathbb{F}_p),\quad H_*(X/\mathbb{Z}/p;\mathbb{F}_p),\quad H_*(F;\mathbb{F}_p)
$$
fit into a long exact sequence of period three in the indexing. The existence and the exact form of the sequences are Smith's theorem, and they are the homological source of the fixed-set theorem.

**Proof sketch.** The sequences are extracted from the Serre spectral sequence of the fibration $X\to X_{\mathbb{Z}/p}\to B\mathbb{Z}/p$: the $E^2$ page is $H_*(B\mathbb{Z}/p;\mathbb{F}_p)\otimes H_*(X;\mathbb{F}_p)$ with the local coefficients given by the action, and the differentials and the edge maps assemble the three-term ladder into the exact sequences relating the three homologies; the identification of the maps with the quotient, the inclusion and the transfer is by the naturality of the construction.

**Remark (the content of the sequences).** The sequences say that the homology of the quotient is the homology of $X$ corrected by the shifted homology of the fixed set, and that the correction is measured by the transfer. Over a field the sequences split, so the homology of the quotient is additively the homology of $X$ together with the shifted homology of the fixed set, and the exact form of the splitting depends on the action; this is the homological content of the fixed-set theorem and the input to the computations of the quotient invariants in *Involutions on Manifolds and Equivariant Surgery*.

**Remark (the general prime).** For $\mathbb{Z}/p$ with $p$ odd the Smith sequences take the same form with $\mathbb{F}_p$ coefficients, with an additional correction from the truncated polynomial algebra $H^*(B\mathbb{Z}/p;\mathbb{F}_p) = \mathbb{F}_p[u]\otimes\Lambda(v)$; the representation theory of $\mathbb{Z}/p$ over $\mathbb{F}_p$ organises the correction. The statements and the corrections are in the sources; the present article uses the $\mathbb{Z}/2$ picture and records the general one.

## Localisation and the Borel Construction

**Definition.** For a $G$-space $X$ the **Borel construction** is $X_G = X\times_G EG$, with $EG\to BG$ the universal $G$-bundle, and the **equivariant homology** is $H_*^G(X;\mathbb{F}_p) = H_*(X_G;\mathbb{F}_p)$, a module over $H^*(BG;\mathbb{F}_p)$.

**Theorem (localisation).** Let $G = \mathbb{Z}/p$ act on a finite-dimensional $G$-CW complex $X$ with finitely many orbit types, and let $F\subseteq X$ be the fixed set. Then the map induced by the inclusion,
$$
H^*_G(X;\mathbb{F}_p)\longrightarrow H^*_G(F;\mathbb{F}_p),
$$
becomes an isomorphism after localising at the nonzero elements of $H^*(BG;\mathbb{F}_p)$; equivalently, the kernel and the cokernel of the restriction are annihilated by a power of the "positive-degree" classes of $H^*(BG;\mathbb{F}_p)$. In particular the equivariant cohomology of $X$ is determined by that of $F$ over the generic point of $\operatorname{Spec}H^*(BG;\mathbb{F}_p)$.

**Proof sketch.** The theorem is proved by induction on the number of orbit types and the dimension, reducing to the model of a single orbit $G/H$ and using the fact that the Euler class of the equivariant normal bundle of the fixed set becomes invertible after localisation; the orbits that are not fixed have equivariant cohomology annihilated by the positive-degree classes. The statement is due to Borel and Quillen; the details and the compact Lie group generalisations belong to the equivariant cohomology literature and to *Stable Homotopy Theory*.

**Corollary (the Smith theory as localisation).** The Smith fixed-set theorem follows from the localisation theorem: the equivariant cohomology of a mod $p$ homology $n$-sphere localises to that of the fixed set, and the structure of $H^*(BG;\mathbb{F}_p)$ as a truncated polynomial ring forces the fixed set to be a mod $p$ homology sphere of the constrained dimension. This is the algebraic reason behind the fixed-set theorem.

**Remark (the rational case).** Over $\mathbb{Q}$, or for actions of odd order with $\mathbb{Q}$ coefficients, the equivariant cohomology localises to the fixed set for every finite group, and the statement is the "rational localisation"; the integral and mod $p$ statements require the prime $p$ dividing the order, which is why the Smith theory is a mod $p$ theory.

## Applications

**Example (the periodic knots and the axis).** A periodic knot with an action of $\mathbb{Z}/n$ on $S^3$ has a fixed set which is a circle by the fixed-set theorem for the prime factors of $n$; this axis is the input to the equivariant Seifert surface of *Equivariant Knot Theory*, and the fixed-set theorem is the reason the periodic knots have an axis rather than a more complicated fixed set.

**Example (the involutions of a surface).** For a $\mathbb{Z}/2$ action on a closed surface the fixed set is a mod $2$ homology sphere of dimension $0$, $1$ or $2$; the local-linear refinement gives isolated points in the orientation-preserving case and circles in the orientation-reversing case, which is the classification of *The Classification of Involutions on Surfaces*. The example shows the gap between the Smith theorem (homological) and the structure theorem (local-linear).

**Example (the free actions).** For a free $\mathbb{Z}/p$ action on $S^n$ the fixed set is empty and the Smith theorem is vacuous; the quotients are the lens spaces and the fake projective spaces of *Free Involutions and Lens Spaces*, and the localisation theorem says that the equivariant homology is then a torsion module over $H^*(BG;\mathbb{F}_p)$ annihilated by the positive-degree classes. The contrast between the free and the non-free cases is the dichotomy of the equivariant theory.

**Example (the reflection of the circle).** Let $\mathbb{Z}/2$ act on the circle $S^1$ by reflection; the fixed set is two points and the quotient is an interval. With $\mathbb{F}_2$ coefficients, $H_0(F)=\mathbb{F}_2^2$, $H_0(S^1)=\mathbb{F}_2$, $H_0(S^1/\mathbb{Z}/2)=\mathbb{F}_2$ and $H_1(S^1)=\mathbb{F}_2$, $H_1(F)=H_1(S^1/\mathbb{Z}/2)=0$; the Smith ladder for the action is the simplest computation exhibiting the two fixed points as the homological defect and the interval as the invariant part, and it is the model for the mod $2$ bookkeeping of the fixed sets in the whole batch.

## Orbit Types and the Euler Characteristic

**Definition.** A $\mathbb{Z}/p$ action has two orbit types: the orbits of size one, which are the fixed points, and the orbits of size $p$, which are the free orbits; accordingly $X$ is the disjoint union of the fixed set $F$ and the free part $X\setminus F$, and the orbit space $X/\mathbb{Z}/p$ is the union of the image of $F$ and the image of the free part. Over the free part the quotient map is a $p$-fold covering, and the decomposition of the Borel construction into the pieces indexed by the orbit types is the **orbit-type stratification**.

**Theorem (the Euler characteristic of the quotient).** For a finite-dimensional space with a $\mathbb{Z}/p$ action and finitely generated homology, the Euler characteristic of the orbit space is
$$
\chi(X/\mathbb{Z}/p) = \frac{\chi(X)+(p-1)\chi(F)}{p}.
$$
In particular $\chi(X/\mathbb{Z}/2) = (\chi(X)+\chi(F))/2$, and the identity $\chi(X) = \chi(F)+p\,\chi(X\setminus F)$ from the orbit count gives the formula.

**Proof.** The free part consists of the orbits of size $p$, so its Euler characteristic satisfies $\chi(X\setminus F) = p\,\chi((X\setminus F)/\mathbb{Z}/p)$ by the multiplicativity of the Euler characteristic for a covering of finite degree; adding $\chi(F)$ to both sides and using $\chi(X) = \chi(F)+\chi(X\setminus F)$ gives the formula. The verification: for the reflection of $S^1$ the formula gives $(0+2)/2 = 1 = \chi([0,1])$, and for the involution $-I$ of the torus it gives $(0+4)/2 = 2 = \chi(S^2)$, both correct.

**Remark (the structure of the quotient).** For a locally linear action the quotient is a manifold away from the image of the fixed set; near a fixed point of the model $\mathbb{R}^k\times\mathbb{R}^{n-k}$ with the reflection of the first factor, the quotient is the cone $\mathbb{R}^k/\{\pm1\}\times\mathbb{R}^{n-k}$, which is a manifold exactly at the fixed sets of codimension one and otherwise has a singular stratum of the quotient. The quotient is therefore a manifold with the singular locus of the orbit type, and the orbifold structure of the quotient is the local model exploited in *The Classification of Involutions on Surfaces*.

## The Borel Construction and the Orbit-Type Splitting

**Proposition (the splitting of the Borel construction).** The Borel construction $X_{\mathbb{Z}/p} = X\times_{\mathbb{Z}/p}E\mathbb{Z}/p$ is built from the two orbit types: the piece over the free part fibres over $(X\setminus F)/\mathbb{Z}/p$ with the fibre $B\mathbb{Z}/p$, and the piece over the fixed set is $F\times B\mathbb{Z}/p$; the pieces are glued along the boundary of the tubular neighbourhood of the fixed set, and the Mayer–Vietoris sequence of the gluing is the source of the Smith sequences.

**Proof.** Over the free part the action is free, so the Borel construction is the total space of the bundle with the fibre $E\mathbb{Z}/p$ and the base the free quotient; over the fixed set the action is trivial, so $F\times_{\mathbb{Z}/p}E\mathbb{Z}/p = F\times B\mathbb{Z}/p$; the gluing is along the equivariant neighbourhood of the fixed set, which is $F\times D^k$ with the action on the disc, and the sequence of the pair of the two pieces gives the Mayer–Vietoris ladder.

**Corollary (the torsion of the equivariant homology).** The equivariant homology of a free action is a torsion module over $H^*(B\mathbb{Z}/p;\mathbb{F}_p) = \mathbb{F}_p[x]$ annihilated by the positive-degree classes, while the equivariant homology of the fixed set is a free module generated by $H_*(F;\mathbb{F}_p)$; the localisation theorem then says that the localisation of the equivariant homology of $X$ is the free part, which is the fixed-set contribution.

**Proof.** The free case is the statement that the classifying map $X_{\mathbb{Z}/p}\to B\mathbb{Z}/p$ has the homology of the base twisted by the free quotient, whose module structure is torsion; the fixed set gives $H_*(F)\otimes H^*(B\mathbb{Z}/p)$ free; the localisation inverts the positive-degree classes, killing the torsion and leaving the free part. The statement is the module-theoretic form of the localisation theorem.

## Summary

A periodic map of prime order $p$ generates a $\mathbb{Z}/p$ action; Smith's fixed-set theorem states that the fixed set of such an action on a mod $p$ homology $n$-sphere is a mod $p$ homology $r$-sphere for some $-1\leq r\leq n$, with $n-r$ even when $p$ is odd and unconstrained when $p=2$, and it forces a nonempty acyclic fixed set for a $p$-group action on a mod $p$ acyclic finite-dimensional space. On the sphere $S^3$ the fixed set of an odd-order action is a circle or empty, and of an involution a circle, a two-sphere, two points or empty, which is the list used throughout this batch. The Smith exact sequences relate the homology of the space, its quotient and its fixed set with mod $p$ coefficients, splitting over the fields to express the quotient homology additively as the homology of the space together with the shifted homology of the fixed set. The localisation theorem identifies the equivariant cohomology of $X$ with that of the fixed set after inverting the positive-degree classes of $H^*(BG;\mathbb{F}_p)$, and it is the algebraic mechanism behind the fixed-set theorem; over the rationals the localisation is unconditional, which is why the Smith theory is intrinsically a mod $p$ theory. The applications are the axis of a periodic knot, the involution of a surface, the free actions and the lens spaces.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $p$, $\mathbb{Z}/p$ | a prime and the cyclic group of order $p$ acting on $X$ |
| $F = X^{\mathbb{Z}/p}$ | the fixed set; a mod $p$ homology $r$-sphere, $-1\leq r\leq n$ |
| mod $p$ homology $n$-sphere | a space with $H_*(X;\mathbb{F}_p)\cong H_*(S^n;\mathbb{F}_p)$ |
| $n-r$ even for odd $p$ | the Smith parity constraint on the fixed-set dimension |
| Smith sequences | the long exact sequences relating $H_*(X)$, $H_*(X/\mathbb{Z}/p)$ and $H_*(F)$ over $\mathbb{F}_p$ |
| $\pi$, $i$, the transfer | the quotient map, the inclusion of the fixed set, and the transfer map |
| $X_G = X\times_G EG$, $H_*^G(X)$ | the Borel construction and the equivariant homology |
| $H^*_G(X;\mathbb{F}_p)\xrightarrow{\sim}H^*_G(F;\mathbb{F}_p)$ | the localisation theorem, after inverting positive-degree classes |
| $H^*(BG;\mathbb{F}_p)$ | the cohomology of the classifying space, a truncated polynomial ring for $G=\mathbb{Z}/p$ |
| orbit types | the fixed points (size one) and the free orbits (size $p$) |
| $\chi(X/\mathbb{Z}/p) = (\chi(X)+(p-1)\chi(F))/p$ | the Euler characteristic of the quotient from the two orbit types |
| $\mathbb{R}^k/\{\pm1\}$ | the local quotient model; a manifold only for $k=1$ |

## Further Reading

- Paul A. Smith, "Transformations of Finite Period", *Annals of Mathematics* 39 (1938), 127–164; 40 (1939), 690–711; 41 (1940), 373–390, for the fixed-set theorem and the exact sequences.
- Paul A. Smith, "Fixed-Point Theorems for Periodic Transformations", *American Journal of Mathematics* 63 (1941), 1–8, for the fixed points of $p$-group actions on discs and acyclic spaces.
- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for the Smith theory, the fixed-set structure and the equivariant neighbourhoods.
- Armand Borel, *Seminar on Transformation Groups* (Princeton University Press, 1960), for the Borel construction, the equivariant cohomology and the localisation.
- Daniel Quillen, "The Spectrum of an Equivariant Cohomology Ring I", *Annals of Mathematics* 94 (1971), 549–572, for the localisation theorem and the prime ideals of $H^*_G(X)$.
- Wu-yi Hsiang, *Cohomology Theory of Topological Transformation Groups* (Springer, 1975), for the systematic Smith theory and its applications to the group actions on spheres and manifolds.
- John McCleary, *A User's Guide to Spectral Sequences* (Cambridge University Press, 2001), for the Serre spectral sequence of the Borel construction and the edge homomorphisms behind the Smith sequences.
