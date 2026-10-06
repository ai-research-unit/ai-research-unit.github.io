# __Iterated Function Systems in the Complex Plane__

## Introduction

An **iterated function system** on the plane is a finite family of contractions, and its attractor is the compact set invariant under the family; when the contractions are **similarities** of $\mathbb{C}$, that is maps $z \mapsto u z + v$ with $u \neq 0$, the attractor is the self-similar set of the classical theory. This article works the complex case: it fixes the similarities of $\mathbb{C}$ and their rotation content, records the attractor theorem and the similarity dimension that the lead article *Fractal Geometry* supplies, and then turns to the geometric source of the systems, which is the theory of the **Kleinian groups**. A Kleinian group is a discrete group of Möbius transformations of the Riemann sphere, its **limit set** is the smallest closed invariant set of the action, and for the groups of the Schottky type the limit set is precisely the attractor of a system of inverse branches; the Apollonian gasket is the same construction at the tangent circles. The coding of the attractor by the shift space closes the article.

The article is the $\mathbb{C}$ instance of the self-similar theory. The general definition of an iterated function system, the attractor theorem, the open set condition, the similarity dimension, the Hausdorff dimension of a self-similar set and the standard examples (the Cantor set, the Sierpiński gasket, the Koch curve) are those of *Fractal Geometry*, the lead article of the subcategory, and are cited rather than restated; the self-similar **measure** and its dimension are those of *The Self-Similar Measure and the Invariant Measure* of Part III's *Fractal Analysis*; the Hutchinson operator and its adjoint are those of *The Hutchinson Operator and Its Adjoint* of Part IV; the Kleinian groups, their limit sets and their quotient manifolds are those of *Hyperbolic Geometry* and *Low-Dimensional Topology*, and the discretisation and the arithmetic of the groups are catalogued in *List of Discrete Geometric Groups*; the coding is that of *Symbolic Dynamics*. The Julia set as the attractor of the system of inverse branches is the subject of *The Julia Sets of a Complex Polynomial* and of *The Geometry of the Julia Sets*. No physics is invoked.

## Similarities of the Complex Plane

### The Group of Similarities

**Definition.** A **similarity** of $\mathbb{C}$ is a map

$$
S(z) = u z + v, \qquad u, v \in \mathbb{C},\ u \neq 0 ,
$$

and the **ratio** (or linear contraction factor) of $S$ is $|u|$. The similarity is a **contraction** if $|u| < 1$, and it is **direct** if it preserves the orientation, that is if $S$ is holomorphic; the map $z \mapsto u\bar z + v$ is the orientation-reversing similarity of ratio $|u|$.

**Proposition.** The similarities of $\mathbb{C}$ form a group, the semidirect product $\mathbb{C} \rtimes \mathbb{C}^\times$ of the translations with the multiplications, of real dimension four; the direct similarities with $|u| = 1$ form the group of the Euclidean isometries fixing the origin, which is $U(1)$ acting by rotations, and every similarity is the composition of a rotation, a homothety and a translation.

**Proof.** The composite of $z \mapsto u z+v$ and $z \mapsto u'z+v'$ is $z \mapsto u'u z + (u'v+v')$, again of the form; and every similarity with $u \neq 0$ is invertible with inverse $z \mapsto u^{-1}z - u^{-1}v$. The multiplication $z \mapsto uz$ is the rotation by $\arg u$ composed with the homothety of ratio $|u|$, since $uz = |u|e^{i\arg u}z$.

**Remark (the rotation content).** This is the point at which the complex systems differ from the real ones. A similarity of $\mathbb{R}$ is $x \mapsto ax+b$ and carries no rotation; a similarity of $\mathbb{C}$ carries the angle $\arg u$, and the group of contractive similarities is the group $U(1) \times (0,1) \times \mathbb{C}$ of a rotation, a homothety and a translation. Two complex systems with the same ratios and the same translations but different rotation angles have different attractors.

### The Attractor Theorem and the Similarity Dimension

**Definition.** An **iterated function system** (IFS) of similarities of $\mathbb{C}$ is a finite family $\mathcal{S} = \{S_1, \ldots, S_m\}$, $m \geq 2$, of similarities $S_i(z) = u_i z + v_i$ with $|u_i| < 1$.

**Theorem (the attractor, Hutchinson).** For every such family there is a unique nonempty compact set $\Lambda \subseteq \mathbb{C}$ with

$$
\Lambda = \bigcup_{i=1}^{m} S_i(\Lambda) ,
$$

the **attractor** of the system; it is the fixed point of the Hutchinson operator $E \mapsto \bigcup_i S_i(E)$ on the complete metric space of nonempty compact sets with the Hausdorff metric, and for every starting compact set the iterated union converges to $\Lambda$ in the Hausdorff metric.

**Proof sketch.** The operator is a contraction of the hyperspace, because each $S_i$ is a contraction of $\mathbb{C}$ and the Hausdorff metric contracts correspondingly; the Banach fixed-point theorem gives the unique fixed point and the convergence. The construction is the attractor theorem of *Fractal Geometry*; the operator and its spectral theory are those of *The Hutchinson Operator and Its Adjoint*.

**Definition.** The **similarity dimension** of $\mathcal{S}$ is the unique real $s \geq 0$ with

$$
\sum_{i=1}^{m} |u_i|^s = 1 .
$$

It exists and is unique when $m \geq 2$ and every $|u_i| < 1$, because the left-hand side is strictly decreasing in $s$, greater than $1$ at $s = 0$ and tending to $0$ at infinity.

**Theorem (the dimension under the open set condition).** If the system satisfies the **open set condition** — there is a nonempty open set $O$ with $\bigcup_i S_i(O) \subseteq O$, the union disjoint — then

$$
0 < \mathcal{H}^s(\Lambda) < \infty, \qquad \dim_H \Lambda = s ,
$$

where $s$ is the similarity dimension; likewise the box dimension of $\Lambda$ is $s$. Without the open set condition the attractor may have dimension strictly less than the similarity dimension, because the pieces may overlap.

**Proof sketch.** The open set condition lets the pieces of the $n$-th level be separated by the images of $O$, so the covering sum $\sum |(S_{i_1}\circ\cdots\circ S_{i_n})'|^s = \left(\sum|u_i|^s\right)^n = 1$ is uniformly controlled; the upper bound for the $s$-dimensional measure and the lower bound for the mass distribution both follow. The open set condition, the similarity dimension and this theorem are those of *Fractal Geometry*, and they are not reproved here.

**Example (a complex Cantor set).** Let $S_1(z) = u z$ and $S_2(z) = u z + (1-u)$ with $u$ a real number in $(0,1/2)$. The attractor is the real middle-third-type Cantor set on the segment $[0,1]$, of dimension $s$ with $|u|^s = 1/2$, that is $s = \log 2/\log(1/|u|)$; for $u = 1/3$ this is the middle-third set of dimension $\log 2/\log 3 = 0.6309297535\ldots$, the value recorded in *Fractal Geometry*. If instead $u = \tfrac13 e^{i\pi/3}$, the two pieces are rotated relative to one another and the attractor is a complex Cantor set of the same dimension, not contained in any line.

## The Kleinian Groups and Their Limit Sets

### Kleinian Groups

**Definition.** A **Kleinian group** is a discrete subgroup $\Gamma \leq PSL(2,\mathbb{C})$, acting on the Riemann sphere $\hat{\mathbb{C}}$ by Möbius transformations; a **Fuchsian group** is a discrete subgroup of $PSL(2,\mathbb{R})$, acting on the circle $\hat{\mathbb{R}} = \mathbb{R} \cup \{\infty\}$ and on the hyperbolic plane. The definitions, the classification of the elements into the elliptic, parabolic and hyperbolic (loxodromic) classes, the discreteness and the construction of the quotient manifolds are those of *Hyperbolic Geometry*, and the groups are catalogued in *List of Discrete Geometric Groups*.

**Example (the Hecke groups).** The **Hecke group** $H(\lambda)$ is generated by the two Möbius transformations $z \mapsto -1/z$ and $z \mapsto z+\lambda$; it is discrete for $\lambda = 2\cos(\pi/q)$ with $q \geq 3$ and for $\lambda \geq 2$. Its limit set illustrates the two sides of the theory that concern the systems below: for $\lambda = 2\cos(\pi/q)$ the group is Fuchsian of the first kind and its limit set is the whole circle $\hat{\mathbb{R}}$, a non-fractal curve, while for $\lambda \geq 2$ it is Fuchsian of the second kind and its limit set is a Cantor subset of $\hat{\mathbb{R}}$ — the simplest explicit limit set that is the attractor of a system of inverse branches. Whether a group is of the first or the second kind is therefore what decides whether its limit set carries fractal structure, and the Schottky construction below is the case in which the group is of the second kind by construction.

**Definition.** The **limit set** $\Lambda(\Gamma)$ is the set of accumulation points in $\hat{\mathbb{C}}$ of the orbit $\Gamma z$ of a point $z$ whose orbit is infinite; it is independent of the chosen $z$, it is the smallest nonempty closed $\Gamma$-invariant subset of $\hat{\mathbb{C}}$, and it is the complement of the domain of discontinuity on which $\Gamma$ acts properly discontinuously.

**Theorem.** The limit set of a Kleinian group is either empty, a single point, two points, or a perfect set; for a non-elementary group it is perfect and uncountable, and for a **quasi-Fuchsian** group it is a Jordan curve. If the group is conjugate into $PSL(2,\mathbb{R})$ and is non-elementary, its limit set is contained in the circle $\hat{\mathbb{R}}$.

**Proof sketch.** If the limit set has three points, the Möbius transformations sending three arbitrary points to three fixed points accumulate, and the group is non-discrete unless the limit set is a perfect set; the alternatives exhaust the cases. The Jordan-curve case is the quasi-Fuchsian theorem, and the statements are those of *Hyperbolic Geometry*.

### The Schottky Systems

**Definition.** A **Schottky group** on $m$ generators is a group generated by $m$ Möbius transformations $T_1, \ldots, T_m$ for which there are $2m$ pairwise disjoint closed disks $D_1, \ldots, D_{2m}$ in $\hat{\mathbb{C}}$ with

$$
T_i\bigl(\hat{\mathbb{C}} \setminus D_{m+i}\bigr) = D_i , \qquad i = 1, \ldots, m ,
$$

the disks being paired; the group is classical when the disks are bounded by circles, and the region $\hat{\mathbb{C}} \setminus \bigcup_{j} D_j$ is a fundamental domain.

**Theorem.** The limit set of a Schottky group is the attractor of the iterated function system formed by the inverses $T_1^{-1}, \ldots, T_m^{-1}$ restricted to the disks $D_1, \ldots, D_m$: each $T_i^{-1}$ is a contraction of $D_i$ onto a disk contained in $D_{m+i}$, the system satisfies the open set condition with $O$ the exterior region of the fundamental domain, and the attractor is a Cantor set.

**Proof sketch.** The disks $D_{m+i}$ are disjoint from the disks $D_j$, so $T_i^{-1}(D_i) \subseteq D_{m+i}$ and the restricted maps are contractions by the Schwarz–Pick lemma; the family is a contraction system, its attractor is the limit set because the limit set is the smallest closed invariant set and the attractor is invariant under the inverses, hence under the group; the open set condition holds with the exterior of the fundamental domain. The classical theory is that of *Hyperbolic Geometry*.

**Remark.** The limit sets of the Schottky groups are the Cantor sets of the Kleinian theory, and their Hausdorff dimension is the exponent $\delta$ of the group: the exponent of convergence of the Poincaré series, equivalently the critical exponent of the group, which also gives the dimension of the Patterson–Sullivan measure. The equality $\dim_H \Lambda = \delta$ and the ergodic theory of the measure are Part III's, cited to *Ergodic Theory of Group Actions*, and the measure itself is constructed there.

### The Apollonian Gasket

**Definition.** Four mutually tangent circles in $\hat{\mathbb{C}}$ determine the **Apollonian gasket**: the closure of the union of the circles obtained from the four by the repeated action of the inversions in the four circles.

**Theorem.** The Apollonian gasket is the limit set of the Kleinian group $\Gamma_A$ generated by the four inversions in the mutually tangent circles, and equivalently it is the closure of the orbit of the four circles under $\Gamma_A$. The group is geometrically finite and non-elementary, and the gasket is the minimal closed invariant set of the group on the sphere.

**Proof sketch.** The inversions are Möbius transformations and the group generated by them is discrete, because the four circles bound a fundamental domain of a rank-two group (or, for the Apollonian packing, because the inversions are in a "Schottky-like" configuration); its orbit on the four circles is countable, its accumulation set is the gasket, and the gasket is invariant and minimal, hence the limit set. The statement is that of the Kleinian theory of *Hyperbolic Geometry*; the dimension of the gasket is given by the critical exponent $\delta$ of the group, a quantity known rigorously and cited in the literature rather than recomputed here.

**Remark (the Hecke groups).** The Fuchsian analogue, the **Hecke group** $H(\lambda)$ generated by $z \mapsto -1/z$ and $z \mapsto z+\lambda$, is the linear source of the two-dimensional systems: the modular group $PSL(2,\mathbb{Z})$ is $H(1)$, the arithmetic values $\lambda = 2\cos(\pi/q)$ give the triangle groups, and the continued-fraction coding of the orbit of $0$ is the coding of the geodesic flow. For these arithmetic groups the limit set is the whole circle $\hat{\mathbb{R}}$, of dimension one, so the fractal constructions begin with the strictly Kleinian and Schottky groups and with the Apollonian group, not with the Hecke groups themselves.

## The Coding of the Attractor

**Theorem (the coding map).** Let $\mathcal{S} = \{S_1, \ldots, S_m\}$ be an iterated function system of similarities with attractor $\Lambda$, and let $\Sigma = \{1, \ldots, m\}^{\mathbb{N}}$ be the full shift on $m$ symbols. For each $\omega = (\omega_1, \omega_2, \ldots) \in \Sigma$ the intersections

$$
\bigcap_{n \geq 1} S_{\omega_1}\circ\cdots\circ S_{\omega_n}(\Lambda)
$$

are nested compact sets of diameter tending to $0$, so their intersection is a single point $\pi(\omega) \in \Lambda$; the map $\pi : \Sigma \to \Lambda$ is continuous and surjective, it satisfies $S_i \circ \pi = \pi \circ \sigma_i$ with $\sigma_i$ the $i$-th branch of the inverse of the shift, and it is injective exactly when the sets $S_i(\Lambda)$ are pairwise disjoint.

**Proof.** The diameter of $S_{\omega_1}\circ\cdots\circ S_{\omega_n}(\Lambda)$ is at most $|u_{\omega_1}\cdots u_{\omega_n}|\operatorname{diam}\Lambda \leq (\max_i |u_i|)^n \operatorname{diam}\Lambda \to 0$, so the nested intersection is a point; the continuity follows from the uniform contraction, the surjectivity from the invariance of $\Lambda$, and the injectivity statement from the overlap of the pieces. The coding, the shift and the subshift are those of *Symbolic Dynamics* and *Limit Spaces and Schreier Graphs*; the combinatorics of the address map is the same as for the real systems of *Fractal Geometry*.

**Example (the Cantor set as a shift space).** For the two-map system $S_1(z) = z/3$, $S_2(z) = z/3 + 2/3$ on the real segment, the coding map is a bijection $\{1,2\}^{\mathbb{N}} \to \Lambda$ onto the middle-third Cantor set, and the shift corresponds to the discarding of the first ternary digit. This is the middle-third set of *Fractal Geometry*, seen through its address map.

## Summary

An iterated function system of similarities of the complex plane is a finite family $S_i(z) = u_i z + v_i$ with $|u_i| < 1$; its attractor is the unique compact set invariant under the family, obtained as the fixed point of the Hutchinson operator. The similarities of $\mathbb{C}$ carry a rotation in addition to the homothety, which the real systems do not, and the group of contractive similarities is $U(1) \times (0,1) \times \mathbb{C}$. When the open set condition holds, the attractor has Hausdorff and box dimension equal to the similarity dimension, the root of $\sum|u_i|^s = 1$; this theorem and the definition of the dimension are those of *Fractal Geometry*.

The geometric source of the complex systems is the theory of the Kleinian groups. A Kleinian group is a discrete subgroup of $PSL(2,\mathbb{C})$, and its limit set is the smallest closed invariant set; for a Schottky group the limit set is the attractor of the system of inverse branches of the generators, a Cantor set, and the Apollonian gasket is the limit set of the group generated by four inversions in mutually tangent circles. The Hausdorff dimension of a limit set is the critical exponent of the group, and the measure is the Patterson–Sullivan measure of Part III. Every attractor is coded by the full shift through the address map, which is a bijection exactly when the pieces are disjoint. The Kleinian groups and their quotients are those of *Hyperbolic Geometry* and *Low-Dimensional Topology*; the conformal self-similarity of the Julia sets, which are the attractors of the systems of inverse branches of a rational map, is the subject of *The Julia Sets of a Complex Polynomial* and of Part IV.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S_i(z) = u_i z + v_i$ | Similarity of $\mathbb{C}$ of ratio $\lvert u_i\rvert$; contraction if $\lvert u_i\rvert < 1$ |
| $\mathcal{S} = \{S_1,\ldots,S_m\}$ | Iterated function system of similarities |
| $\Lambda$ | Attractor, the unique compact set $\Lambda = \bigcup_i S_i(\Lambda)$ |
| $s$, similarity dimension | Root of $\sum_i\lvert u_i\rvert^s = 1$ |
| open set condition | Disjoint images of an open set $O$ inside $O$ |
| $\Gamma$, $\Lambda(\Gamma)$ | Kleinian group, its limit set |
| $D_1,\ldots,D_{2m}$, $T_1,\ldots,T_m$ | Schottky disks and generators |
| $\Gamma_A$, Apollonian gasket | The group of four inversions and its limit set |
| $H(\lambda)$ | Hecke group generated by $z\mapsto-1/z$, $z\mapsto z+\lambda$ |
| $\Sigma = \{1,\ldots,m\}^{\mathbb{N}}$, $\pi$ | Shift space and the address map |
| $\delta$ | Critical exponent of a Kleinian group; $\dim_H\Lambda(\Gamma)$ |

## Further Reading

- John E. Hutchinson, "Fractals and self-similarity", *Indiana University Mathematics Journal* 30 (1981), 713–747, for the attractor theorem and the open set condition.
- Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications*, 3rd edition (Wiley, 2014), for the similarity dimension and the self-similar sets.
- Alan F. Beardon, *The Geometry of Discrete Groups* (Springer, 1983), for the Möbius transformations, the Fuchsian and the Kleinian groups and the limit sets.
- David Mumford, Caroline Series and David Wright, *Indra's Pearls: The Vision of Felix Klein* (Cambridge University Press, 2002), for the Schottky groups and their limit sets.
- Dennis P. Sullivan, "The density at infinity of a discrete group of hyperbolic motions", *Publications Mathématiques de l'IHÉS* 50 (1979), 171–202, for the critical exponent and the Patterson–Sullivan measure.
- Curtis T. McMullen, "Hausdorff dimension and conformal dynamics II: Geometrically finite rational maps", *Commentarii Mathematici Helvetici* 75 (2000), 535–593, for the dimension of the Apollonian gasket and of the geometrically finite limit sets.
