
# __Homotopy Groups and Fibrations__

## Introduction

The fundamental group of *The Fundamental Group and Covering Spaces* records the loops of a space; the **higher homotopy groups** record the maps of spheres of every dimension, and they are the most sensitive invariants of homotopy theory, in the sense that a map of simply connected CW complexes inducing isomorphisms on all of them is a homotopy equivalence. Unlike homology, they are not computable from a chain complex: they carry no excision, they are almost never finitely generated in an obvious way, and even the groups $\pi_k(S^n)$ for $k > n$ are not known in closed form. What replaces computability is a long exact sequence: for a **fibration** $F \to E \to B$ the homotopy groups of the three spaces are related by an exact sequence running downwards in degree, and this sequence, together with the standard fibrations — the path–loop fibration, the Hopf fibrations, the fibrations of classical groups — computes almost everything that is computed.

The article presents the homotopy groups, their basic properties — abelian in degree at least two, functorial, homotopy invariant, compatible with products — and the two theorems that connect them with the homology of *Simplicial and Singular Homology*: the **Hurewicz theorem**, which identifies the first nonvanishing homotopy and homology groups in the simply connected case, and the **Whitehead theorem**, which converts a homology equivalence into a homotopy equivalence for simply connected CW complexes. It then presents fibrations, the long exact sequence, and the Hopf fibrations with their consequences. The **Leray–Serre spectral sequence**, which computes the homology of a fibration and is the companion of the long exact sequence, is not covered here. The **bundles** that give the geometrically natural examples are those of the written *Fibre Bundles, Connections and Curvature*; a fibration is the homotopy-theoretic weakening of a bundle, in which the local triviality is replaced by a lifting property, and the two agree for the fibre bundles over paracompact bases.

Throughout, spaces are based and maps are basepoint-preserving unless stated; $\pi_n(X,x_0)$ is the set of homotopy classes of based maps $S^n \to X$, and $S^n$ carries the basepoint $* = (1,0,\ldots,0)$. The interval and sphere notation is that of *The Fundamental Group and Covering Spaces*.

## Homotopy Groups

### Definition

**Definition.** Let $X$ be a topological space with basepoint $x_0$ and let $n \geq 0$. The **$n$-th homotopy group** is the set of homotopy classes relative to the basepoint of based maps,

$$
\pi_n(X,x_0) = \bigl[(S^n, *), (X, x_0)\bigr],
$$

with the group structure defined for $n \geq 1$ by the suspension coordinate: a based map $S^n \to X$ is viewed as a map $I^n \to X$ with the boundary of the cube collapsed to $x_0$, and two such maps are added by using the first on $[0,\tfrac12]\times I^{n-1}$ and the second on $[\tfrac12,1]\times I^{n-1}$. For $n = 0$, $\pi_0(X,x_0)$ is the set of path components of $X$.

**Theorem.** For $n \geq 1$, $\pi_n(X,x_0)$ is a group under the operation above; for $n \geq 2$ it is abelian. The operation is independent of the order of the coordinates, and for $n \geq 2$ the two additions along two different coordinates coincide and give the same abelian group.

*Proof.* The concatenation in the first coordinate gives a group by the same reparametrisation argument as for $\pi_1$: the constant map is the identity and the reversed coordinate gives the inverse. For $n \geq 2$ there is a second, independent concatenation, in the second coordinate, and the standard **Eckmann–Hilton argument** shows that two operations on a set which are compatible in the sense of sharing a unit and satisfying the interchange law coincide and are abelian: writing $+_1$ and $+_2$ for the two additions, the interchange identity $(a+_1 b) +_2 (c +_1 d) = (a+_2 c) +_1 (b +_2 d)$ holds because the four blocks of the cube may be taken in either order, and setting $a = d = e$ (the identity) and $b$, $c$ arbitrary gives $b +_1 c = b +_2 c$, while setting $b = c = e$ gives $a +_1 d = d +_1 a$. $\square$

**Proposition.** A based continuous map $f : (X,x_0) \to (Y,y_0)$ induces $f_* : \pi_n(X,x_0) \to \pi_n(Y,y_0)$ by composition, $(gf)_* = g_*f_*$ and $(\mathrm{id})_* = \mathrm{id}$; homotopic based maps induce equal maps; a homotopy equivalence induces isomorphisms; and for $X \times Y$ the projections give $\pi_n(X\times Y) \cong \pi_n(X)\times\pi_n(Y)$.

*Proof.* The first three statements are immediate from the description of $\pi_n$ as a set of homotopy classes. For the product, a based map $S^n \to X\times Y$ is a pair of based maps, and homotopies decompose in the same way. $\square$

**Remark.** There is no analogue of the covering-space classification for higher homotopy: the groups $\pi_n$ are not detectable by a covering space, and there is no excision theorem. What structure there is comes from fibrations, below, and from the suspension.

**Theorem (suspension).** There is a natural isomorphism

$$
\pi_n(X, x_0) \cong \bigl[(\Sigma S^{n-1}, *), (X,x_0)\bigr] \cong \bigl[(S^{n-1},*), (\Omega X, c)\bigr] \cong \pi_{n-1}(\Omega X),
$$

where $\Sigma$ is the reduced suspension and $\Omega X$ the based loop space of *The Fundamental Group and Covering Spaces*.

*Proof.* A based map $S^n \to X$ is adjoint to a based map $S^{n-1} \to \Omega X$ by the exponential law for compactly generated spaces, which holds for the closed interval and the sphere and is a formality of the product topology of *Topological Spaces*. $\square$

## Connecting Homotopy to Homology

### The Hurewicz Homomorphism

**Definition.** For $n \geq 1$ the **Hurewicz homomorphism** is

$$
h_n : \pi_n(X,x_0) \longrightarrow H_n(X;\mathbb{Z}), \qquad h_n[f] = f_*[S^n],
$$

the image of the fundamental class of the sphere under the induced map on homology. It is a natural transformation of functors, additive, and $h_1$ is the abelianisation of the fundamental group.

**Theorem (Hurewicz).** Let $X$ be a path-connected space and $n \geq 1$.

1. If $\pi_k(X) = 0$ for $k < n$ and $n \geq 2$, then $H_k(X;\mathbb{Z}) = 0$ for $0 < k < n$ and $h_n$ is an isomorphism.
2. If in addition $\pi_n(X)$ is free, then $H_{n+1}$ has no torsion part contributed by $\pi_n$, and $h_{n+1}$ is surjective when $H_{n+1}$ is generated by classes represented by spheres.

In the simply connected case with $n = 2$: if $X$ is simply connected then $h_2 : \pi_2(X) \to H_2(X;\mathbb{Z})$ is an isomorphism.

*Proof sketch.* The argument proceeds by induction over a CW structure: attach cells of dimension $n+1$ and higher to $X$ to form a space in the relevant range, and compare $\pi_n$ and $H_n$ on the resulting skeleta, using that the first group and homology of a simply connected space with no cells below dimension $n$ are both generated by the $n$-cells modulo the relations imposed by the $(n+1)$-cells. The cellular boundary formula of *CW Complexes and Cellular Approximation* supplies the comparison. $\square$

**Corollary (Hurewicz, $n = 1$).** If $X$ is path-connected then $h_1$ induces an isomorphism $H_1(X;\mathbb{Z}) \cong \pi_1(X,x_0)^{\mathrm{ab}}$, the abelianisation of the fundamental group.

*Proof.* The first homology is the quotient of the cycles by the boundaries, and the identification of the singular complex with the cellular complex of a one-dimensional approximation reduces to the definition of the abelianisation. $\square$

**Example.** For $S^n$ with $n \geq 2$, $X$ is simply connected and $H_k(S^n) = 0$ for $0 < k < n$, so $h_n$ is an isomorphism and $\pi_n(S^n) \cong \mathbb{Z}$. For a wedge of $m$ circles, $\pi_1$ is free of rank $m$ and $H_1 \cong \mathbb{Z}^m$, the abelianisation.

### The Whitehead Theorem

**Definition.** A map $f : X \to Y$ is a **weak homotopy equivalence** if it induces isomorphisms on $\pi_n$ for all $n$ and all basepoints. A CW approximation of $Y$ is a weak homotopy equivalence $\Gamma Y \to Y$ with $\Gamma Y$ a CW complex.

**Theorem (Whitehead).** Let $f : X \to Y$ be a map of path-connected CW complexes and suppose $f$ is a weak homotopy equivalence. Then $f$ is a homotopy equivalence. More generally, if $f_* : \pi_k(X) \to \pi_k(Y)$ is an isomorphism for $k < n$ and a surjection for $k = n$, then $f$ is an **$n$-equivalence**: it induces isomorphisms on $H_k$ for $k < n$ and a surjection on $H_n$, and it is homotopic to a cellular map whose restriction to skeleta realises the same connectivity dimension by dimension.

*Proof sketch.* By cellular approximation, $f$ may be assumed cellular, and after replacing $Y$ by the mapping cylinder of $f$ one reduces to showing that a CW pair $(Y,X)$ with $\pi_k(Y,X) = 0$ for all $k$ is such that $X$ is a deformation retract of $Y$. The vanishing of the relative homotopy groups allows one to push the cells of $Y \setminus X$ off themselves one at a time, starting in the lowest dimension, and the weak topology makes the process converge. $\square$

**Corollary.** Every space has a CW approximation, and two spaces are weakly homotopy equivalent exactly when their CW approximations are homotopy equivalent. Consequently homology and homotopy invariants may always be computed on CW models.

**Example.** The **Hopf map** $\eta : S^3 \to S^2$ induces an isomorphism on $H_0$ and on $H_1$, where the groups are $\mathbb{Z}$ and $0$, and it induces the zero map in every degree $k \geq 2$: the group $H_2(S^3;\mathbb{Z})$ vanishes and the target has no homology above degree two. It is nevertheless not nullhomotopic, because it detects a nonzero class in $\pi_3(S^2) \cong \mathbb{Z}$, as computed below. The example shows that homology does not determine homotopy: $S^2$ is simply connected but $\pi_2(S^2) \cong \mathbb{Z} \neq 0$, so $S^2$ is not $2$-connected, the connectivity hypothesis of the Hurewicz theorem is unavailable in degree three, and this is exactly why $H_3(S^2;\mathbb{Z}) = 0$ carries no information about $\pi_3(S^2) \cong \mathbb{Z}$.

**Remark (the hypotheses of the Whitehead theorem).** The homology form of the theorem — a map of simply connected CW complexes inducing isomorphisms on all homology groups is a homotopy equivalence — needs the simple connectivity, and it cannot be weakened to a criterion on homology in general. Let $X$ be a closed oriented $3$-manifold with the homology of $S^3$ but $\pi_1(X) \neq 1$, for instance the **Poincaré homology sphere**, whose fundamental group is the binary icosahedral group of order $120$, a perfect group, so that $H_1(X;\mathbb{Z}) = 0$ as the homology of a sphere requires. By Hopf's theorem, which identifies $[X,S^3]$ with $H^3(X;\mathbb{Z})$ for a $3$-dimensional complex, there is a map $f : X \to S^3$ whose degree is $1$. Then $f_*$ is an isomorphism on $H_0$ and $H_3$, where both spaces have $\mathbb{Z}$, and on $H_1$ and $H_2$, where both have $0$; so $f$ is a homology equivalence. It is not a homotopy equivalence, since $\pi_1(X) \neq 1 = \pi_1(S^3)$ and a homotopy equivalence induces an isomorphism on the fundamental group. This is why the theorem is stated above in its homotopy form.

## Fibrations

### Definitions

**Definition.** A map $p : E \to B$ has the **homotopy lifting property (HLP)** with respect to a space $X$ if, for every commutative square

$$
X \times \{0\} \xrightarrow{\ \tilde h_0\ } E, \qquad X \times I \xrightarrow{\ h\ } B, \qquad h(\cdot,0) = p \circ \tilde h_0,
$$

there is a lift $\tilde h : X \times I \to E$ with $p \circ \tilde h = h$ and $\tilde h(\cdot,0) = \tilde h_0$. A **Serre fibration** is a map with the HLP for all CW complexes $X$; a **Hurewicz fibration** is a map with the HLP for all spaces $X$. The **fibre** over $b \in B$ is $F_b = p^{-1}(b)$. A fibration is a **fibre bundle** when in addition it is locally trivial, in the sense of *Fibre Bundles, Connections and Curvature*.

**Proposition.** A covering map is a Hurewicz fibration with discrete fibres; every fibre bundle over a paracompact base is a Hurewicz fibration.

*Proof.* The first statement is the homotopy lifting theorem of *The Fundamental Group and Covering Spaces*. For the second, lift the homotopy locally using a trivialisation and glue with a partition of unity, the partition's existence being that of *Paracompactness and Partitions of Unity* and the gluing being the standard construction. $\square$

**Theorem (path lifting and the fibre).** Let $p : E \to B$ be a Serre fibration with $B$ path-connected and $E$ nonempty. Then for every $b, b' \in B$ the fibres $F_b$ and $F_{b'}$ are homotopy equivalent (weakly, and genuinely when $E$ and $B$ are CW complexes), and the fibre is well defined up to homotopy equivalence; the map $p$ is surjective and every path in $B$ lifts to a path in $E$ once a starting point over its initial point is chosen.

*Proof.* Choose a path from $b$ to $b'$ and lift the homotopy $F_b \times I \to B$ defining it, by the HLP applied to $X = F_b$; the endpoint is a map $F_b \to F_{b'}$, and the reverse path gives a homotopy inverse up to homotopy. $\square$

### The Long Exact Sequence

**Definition.** For a fibration $p : (E, e_0) \to (B, b_0)$ with fibre $F = p^{-1}(b_0)$ containing $e_0$, the **connecting homomorphism** $\partial : \pi_n(B,b_0) \to \pi_{n-1}(F,e_0)$ is defined by lifting: represent a class in $\pi_n(B,b_0)$ by a based map $f : (D^n, S^{n-1}) \to (B,b_0)$, lift $f$ over the $n$-disc using the HLP applied to a decomposition of $D^n$ into $D^{n-1}\times I$ with the HLP, and restrict the lift to the boundary $S^{n-1}$ to obtain a based map $S^{n-1} \to F$; its class is $\partial[f]$.

**Theorem (the long exact sequence of a fibration).** Let $p : E \to B$ be a Serre fibration with fibre $F$, all spaces path-connected and based compatibly. Then there is a long exact sequence of groups, abelian from $\pi_1$ onwards,

$$
\cdots \to \pi_n(F) \xrightarrow{\ i_*\ } \pi_n(E) \xrightarrow{\ p_*\ } \pi_n(B) \xrightarrow{\ \partial\ } \pi_{n-1}(F) \xrightarrow{\ i_*\ } \cdots \to \pi_0(F) \to \pi_0(E) \to \pi_0(B),
$$

natural in maps of fibrations; the sequence ends with the exact sequence of the sets $\pi_0$ of components.

*Proof sketch.* Exactness at $\pi_n(E)$: $p_* i_* = 0$ because $p \circ i$ is constant; conversely a class in $\ker p_*$ is represented by a based map $S^n \to E$ whose composite with $p$ is nullhomotopic, and the nullhomotopy lifts by the HLP to a homotopy of the original map into the fibre, exhibiting the class as in the image of $i_*$. Exactness at $\pi_n(B)$: $\partial p_* = 0$ by construction; conversely a class killed by $\partial$ has a lift of the disc which restricts to a nullhomotopic map on the boundary, and pasting gives a map $S^n \to E$. Exactness at $\pi_n(F)$: $i_* \partial = 0$ because the restriction of the lifted disc is nullhomotopic through the lift; conversely, a class in $\ker i_*$ bounds a map of a disc in $E$ whose composite with $p$ is a map of the disc constant on the boundary, and the HLP applied to the collapse of that disc to $B$ recovers the class from a map of $B$. $\square$

**Corollary.** If $F$ is contractible then $p_* : \pi_n(E) \to \pi_n(B)$ is an isomorphism for all $n$; if $E$ is contractible then $\pi_{n}(B) \cong \pi_{n-1}(F)$.

**Corollary (path–loop fibration).** Let $PX = \{\text{paths } I \to X \text{ from } x_0\}$ with the compact–open topology and let $p : PX \to X$ evaluate at $1$. Then $p$ is a Hurewicz fibration with fibre $\Omega X$, and $PX$ is contractible, so the long exact sequence gives

$$
\pi_n(X, x_0) \cong \pi_{n-1}(\Omega X, c_{x_0})
$$

for $n \geq 1$, recovering the suspension adjunction.

## The Hopf Fibrations

### The Classical Hopf Maps

**Theorem.** There are fibre bundles

$$
S^0 \to S^1 \to \mathbb{RP}^1, \qquad S^1 \to S^3 \to S^2, \qquad S^3 \to S^7 \to S^4, \qquad S^7 \to S^{15} \to S^8,
$$

the **Hopf fibrations**, obtained by restricting the maps $\mathbb{K}^2 \setminus\{0\} \to \mathbb{KP}^1$ to the unit sphere for $\mathbb{K} = \mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{O}$ respectively; the fibre is the unit sphere of $\mathbb{K}$ and the base is the projective line over $\mathbb{K}$. The structure group is the group of unit scalars, and the bundles are locally trivial in the sense of *Fibre Bundles, Connections and Curvature*.

*Proof.* The map $\mathbb{K}^2\setminus\{0\} \to \mathbb{KP}^1 \cong S^{\dim_\mathbb{R}\mathbb{K}}$ sending a pair to its class is smooth and satisfies the local triviality condition over the standard affine charts; restricting to unit spheres gives the bundle. $\square$

**Corollary.** For the fibration $S^1 \to S^3 \to S^2$ the long exact sequence contains the segments

$$
\pi_3(S^1) \to \pi_3(S^3) \to \pi_3(S^2) \to \pi_2(S^1), \qquad \pi_2(S^3) \to \pi_2(S^2) \to \pi_1(S^1) \to \pi_1(S^3).
$$

Since $\pi_k(S^1) = 0$ for $k \geq 2$ and $\pi_k(S^3) = 0$ for $k \leq 2$, the first segment reads $0 \to \mathbb{Z} \to \pi_3(S^2) \to 0$ and the second $0 \to \pi_2(S^2) \to \mathbb{Z} \to 0$. Hence

$$
\pi_3(S^2) \cong \mathbb{Z}, \qquad \pi_2(S^2) \cong \mathbb{Z},
$$

the first generated by the Hopf map $\eta$. Both groups are nonzero, which is why $\eta$ is not nullhomotopic.

**Remark.** The two computations above are the reason the Hopf map is the fundamental example of a map detected by homotopy and not by homology: it induces the zero map on homology in every positive degree and is nonetheless essential. The generators of the higher homotopy of spheres, and the stable range in which they stabilise, are not covered here.

### Applications

**Example (the infinite dimensional sphere).** Since $\pi_k(S^n) \cong \pi_k(S^{n+1})$ is surjective and eventually an isomorphism by Freudenthal, the colimit $S^\infty = \bigcup_n S^n$ is contractible, and the fibration $S^1 \to S^\infty \to \mathbb{CP}^\infty$ gives $\pi_k(\mathbb{CP}^\infty) \cong \pi_{k-1}(S^1)$, which is $\mathbb{Z}$ for $k = 2$ and zero otherwise.

**Example (the classical groups).** The fibrations $O(n) \to O(n+1) \to S^n$ and $U(n) \to U(n+1) \to S^{2n+1}$ are obtained by letting $O(n+1)$ (respectively $U(n+1)$) act on the unit sphere of $\mathbb{R}^{n+1}$ (respectively $\mathbb{C}^{n+1}$); the long exact sequence computes the homotopy groups of the classical groups by induction from those of spheres. The group theory is that of *Lie Groups*, and the detailed computations are not covered here.

**Example (the Freudenthal suspension theorem).** The suspension homomorphism

$$
\Sigma : \pi_k(S^n) \to \pi_{k+1}(S^{n+1})
$$

is an isomorphism for $k < 2n - 1$ and a surjection for $k = 2n - 1$. The proof uses homotopy excision (the **Blakers–Massey theorem**): the map $S^n \to \Omega S^{n+1}$ has connectivity $n-1$, achieved by comparing the two halves of $S^{n+1}$ with their intersection containing the suspension coordinate. The consequence is that the groups $\pi_{n+k}(S^n)$ for $k$ fixed are independent of $n$ once $n > k+1$; their common value is the **stable stem** $\pi_k^s$, computed.

## Summary

The homotopy groups $\pi_n(X,x_0)$ are the homotopy classes of based maps of spheres; they form groups for $n \geq 1$, are abelian for $n \geq 2$ by the Eckmann–Hilton argument, are functorial and homotopy invariant, and are additive over products. They are adjoint to the loop space, $\pi_n(X) \cong \pi_{n-1}(\Omega X)$, and hence in principle iterative, but they are not computable from a chain complex. The Hurewicz homomorphism relates the first nonvanishing homotopy group of a simply connected space to its first nonvanishing homology group by an isomorphism, and it identifies $H_1$ with the abelianisation of $\pi_1$ in general; the Whitehead theorem converts weak homotopy equivalence into homotopy equivalence for CW complexes, and gives an $n$-equivalence from hypotheses on $\pi_k$ for $k \leq n$.

A fibration is a map with the homotopy lifting property; coverings and bundles over paracompact bases are examples, and the fibres over different points of a path-connected base are homotopy equivalent. The homotopy groups of a fibration fit in a long exact sequence running downward in degree from the base through the total space to the fibre, natural in maps of fibrations, and the path–loop fibration recovers the loop-space suspension. The Hopf fibrations $S^1 \to S^3 \to S^2$ and its companions are the standard examples, and from the long exact sequence they give $\pi_2(S^2) \cong \mathbb{Z}$ and $\pi_3(S^2) \cong \mathbb{Z}$ generated by the Hopf map, which is therefore detected by homotopy and not by homology. The Freudenthal suspension theorem, proved by homotopy excision, makes the groups $\pi_{n+k}(S^n)$ stabilise for $n$ large, and the common stable values are not covered here after the spectral-sequence theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\pi_n(X,x_0)$ | $n$-th homotopy group: based homotopy classes $S^n \to X$ |
| $\pi_0(X)$ | Set of path components |
| $f_* : \pi_n(X) \to \pi_n(Y)$ | Induced homomorphism; functorial |
| $\Omega X$ | Based loop space; $\pi_n(X) \cong \pi_{n-1}(\Omega X)$ |
| $\Sigma X$ | Reduced suspension |
| $PX$ | Path space; $PX \to X$ is the path–loop fibration with fibre $\Omega X$ |
| $h_n : \pi_n(X) \to H_n(X;\mathbb{Z})$ | Hurewicz homomorphism, $h_n[f] = f_*[S^n]$ |
| $\pi_1^{\mathrm{ab}}$ | Abelianisation; $h_1$ induces $H_1 \cong \pi_1^{\mathrm{ab}}$ |
| Weak homotopy equivalence | Isomorphism on all $\pi_n$, all basepoints |
| $n$-equivalence | Isomorphism on $\pi_k$, $k<n$; surjection on $\pi_n$ |
| HLP | Homotopy lifting property defining a (Serre/Hurewicz) fibration |
| $p : E \to B$, $F = p^{-1}(b_0)$ | Fibration, total space, base, fibre |
| $\partial : \pi_n(B) \to \pi_{n-1}(F)$ | Connecting homomorphism of a fibration |
| $S^1 \to S^3 \to S^2$, $S^3 \to S^7 \to S^4$ | Hopf fibrations over $\mathbb{C}$ and $\mathbb{H}$; also $\mathbb{R}$ and $\mathbb{O}$ |
| $\eta$ | Hopf map $S^3 \to S^2$, generator of $\pi_3(S^2)$ |
| $\pi_k^s$ | Stable stem: $\pi_{n+k}(S^n)$ for $n > k+1$ |
| $\mathbb{CP}^\infty$, $S^\infty$ | Colimits of projective spaces and spheres |





## Further Reading

- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for homotopy groups, the Hurewicz and Whitehead theorems, fibrations and the long exact sequence.
- George W. Whitehead, *Elements of Homotopy Theory* (Springer, 1978), for homotopy excision, the Blakers–Massey theorem and the Freudenthal suspension.
- J. Peter May, *A Concise Course in Algebraic Topology* (University of Chicago Press, 1999), for fibrations and cofibrations as the two halves of the homotopy theory of a model category.
- Dale Husemoller, *Fibre Bundles* (Springer, 3rd ed. 1994), for the Hopf fibrations, the classical groups and their bundles.
- Norman Steenrod, *The Topology of Fibre Bundles* (Princeton University Press, 1951), for the homotopy theory of fibrations and the classification of bundles.
- Mimura Mamoru and Hirosi Toda, *Topology of Lie Groups* (American Mathematical Society, 1991), for the homotopy groups of the classical groups by induction.
- Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology* (Springer, 1982), for the fibrations of differential geometry and the route to the Leray–Serre spectral sequence.
