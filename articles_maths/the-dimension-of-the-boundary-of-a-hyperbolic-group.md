# __The Dimension of the Boundary of a Hyperbolic Group__

## Introduction

A finitely generated group that is **hyperbolic** in the sense of Gromov carries a boundary at infinity: the **Gromov boundary** $\partial G$, the set of the geodesic rays of the Cayley graph up to the relation of staying at finite distance, with the topology that makes the union $G \cup \partial G$ compact. The boundary is a fractal in the sense of *Fractal Geometry*: it is a compact metric space with a distance, the **visual metric**, which depends on a parameter, and its Hausdorff dimension measures the way the group grows. For the free group on $r$ generators the boundary is a Cantor set, for a surface group it is a circle, and for a Kleinian group it is the limit set; in every case the dimension is governed by a single number, the **critical exponent** $\delta$ of the Poincaré series of the group.

The theory is the meeting point of the category with the group theory of Part II. The group, its hyperbolicity, its boundary as a topological space and the quasi-isometries are the subject of *Hyperbolic Groups* and *Geometric Group Theory*; the **Patterson–Sullivan measure** on the boundary and the dynamics of the geodesic flow are the subject of *Analysis on Groups* and *Ergodic Theory of Group Actions*; the measure-theoretic construction is therefore cited and not repeated. What belongs here is the **dimension**: the visual metric, the critical exponent, the theorem that the two are equal in the cocompact case, the computation for the free group and the surface group, the behaviour of the dimension under quasi-isometry, and the conformal dimension, which is the genuine quasi-isometry invariant of the boundary.

The article defines the boundary and the visual metric, states the dimension formula $\dim_H(\partial G, d_\varepsilon) = \delta/\varepsilon$ and its normalisation $\dim_H \partial G = \delta$, defines the critical exponent by the Poincaré series and proves it finite and equal to the exponential growth rate, computes $\delta = \log(2r-1)$ for the free group and the boundary dimension in two normalisations, states the Patterson–Sullivan measure as an Ahlfors-regular measure of exponent $\delta$ and the equality of the dimensions in the cocompact case, treats the surface group and the Kleinian groups, and closes with the quasi-isometry invariance, the conformal dimension of Pansu and Cannon's conjecture. The end spaces of *Fractal Trees and Dendrites* are the same objects seen topologically, and the dimension used throughout is that of the lead article *Fractal Geometry*.

The article assumes *Hyperbolic Groups* and *Geometric Group Theory* for the hyperbolicity, the Cayley graph, the Gromov boundary, the visual metric, the geodesic rays and the quasi-isometries; *Metric, Uniform and Complete Spaces* for the distance, the diameter and completeness; *Metric Geometry* for the four-point condition and the real trees; and *Fractal Geometry* for the covering numbers, the Hausdorff content and the dimension. The Patterson–Sullivan measure, its construction by the Patterson–Sullivan series and its ergodic properties are *Analysis on Groups*' and *Ergodic Theory of Group Actions*', and only its dimension is used here. No physics is invoked.

## The Gromov Boundary and the Visual Metric

**Definition.** Let $G$ be a finitely generated group with the word metric $|\cdot|$ of *Hyperbolic Groups*, and let $X$ be the Cayley graph, a proper geodesic hyperbolic space. Two geodesic rays are **equivalent** when they stay at bounded distance, and the **Gromov boundary** $\partial G$ is the set of the equivalence classes, topologised by the neighbourhood base of the sets of rays that stay close to a given ray on a long initial segment. The union $G \cup \partial G$ is compact, and $\partial G$ is a compact metrisable space, nonempty when $G$ is non-elementary; the boundary is a quasi-isometry invariant of $G$.

**Definition (the visual metric).** Fix a base point $o \in X$. For $\xi, \eta \in \partial X$ let $(\xi|\eta) \in (0,\infty]$ be the **Gromov product**, the length of the common initial segment of two rays to $\xi$ and $\eta$; for $\varepsilon > 0$ the **visual metric** is

$$
d_\varepsilon(\xi,\eta) = e^{-\varepsilon (\xi|\eta)} .
$$

The distance $d_\varepsilon$ is compatible with the topology, and there is $\varepsilon_0 > 0$, depending on the hyperbolicity constant, such that $d_\varepsilon$ is a metric for $0 < \varepsilon \leq \varepsilon_0$; when $X$ is a tree the space is $0$-hyperbolic and $d_\varepsilon$ is an ultrametric for every $\varepsilon > 0$. The metrics $d_\varepsilon$ for different $\varepsilon$ are Hölder equivalent and are the members of the **conformal gauge** of the boundary.

**Example (the standard boundaries).** The boundary of the free group $F_r$ on $r \geq 2$ generators is a Cantor set, being the end space of the $2r$-regular tree, which is computed in *Fractal Trees and Dendrites*. The boundary of a surface group is a circle. The boundary of a cocompact Kleinian group acting on hyperbolic three-space is the sphere $S^2$, and the limit set of a general Kleinian group is a closed subset of the sphere. The boundary of a hyperbolic group can also be a Sierpiński carpet or a Menger curve, by the theorem of Kapovich and Kleiner; the boundary with its quasi-Möbius structure, and not its topology alone, is what determines the group up to quasi-isometry.

## The Critical Exponent

**Definition.** The **Poincaré series** of $G$ at $s \in \mathbb{R}$ is

$$
\sum_{g \in G} e^{-s\,|g|} ,
$$

and its **critical exponent** is

$$
\delta = \inf\left\{s > 0 : \sum_{g \in G} e^{-s|g|} < \infty\right\} .
$$

**Theorem (finiteness and the growth rate).** Let $G$ be a non-elementary hyperbolic group. Then $0 < \delta < \infty$, and $\delta$ equals the **exponential growth rate** of the group:

$$
\delta = \lim_{n \to \infty} \frac{1}{n}\log \#\{g \in G : |g| \leq n\} .
$$

In particular $\delta$ is a quasi-isometry invariant of $G$, since the growth rate of the balls is.

**Proof sketch.** Writing the series by the spheres $\#\{|g| = n\}$, the comparison of a series with the exponential growth of its coefficients gives that the abscissa of convergence is exactly the growth rate, provided the coefficients grow exponentially; for a non-elementary hyperbolic group they do, and the growth rate is finite and positive because the group has at least two generators of infinite order and at most exponential growth. A quasi-isometry distorts the balls by bounded multiplicative and additive constants, so the growth rate is unchanged; this is the argument of *Geometric Group Theory*.

**Example (the free group).** For $F_r$ the number of reduced words of length $n \geq 1$ is

$$
\#\{g : |g| = n\} = 2r\,(2r-1)^{\,n-1} ,
$$

so the series is dominated by the ratio $2r-1$ and

$$
\delta(F_r) = \log(2r-1) .
$$

For $r = 2$ this is $\log 3 = 1.0986\ldots$, for $r = 3$ it is $\log 5 = 1.6094\ldots$, and the value grows logarithmically in the rank.

**Example (the surface group).** For a cocompact Fuchsian group, acting on the hyperbolic plane, the growth rate of the balls of the hyperbolic plane is one, and the critical exponent is $\delta = 1$; for a cocompact Kleinian group acting on hyperbolic three-space, the growth rate is two and $\delta = 2$. For a convex-cocompact Kleinian group that is not cocompact, the exponent $\delta$ is strictly less than two, and it is the exponent relevant to the limit set below.

## The Dimension of the Boundary

**Theorem (the dimension in the visual metric).** Let $X$ be a proper geodesic hyperbolic space with critical exponent $\delta$ and visual metrics $d_\varepsilon$. Then for every $0 < \varepsilon \leq \varepsilon_0$

$$
\dim_H(\partial X, d_\varepsilon) = \frac{\delta}{\varepsilon} ,
$$

so that the product $\varepsilon \cdot \dim_H(\partial X, d_\varepsilon) = \delta$ is independent of the choice of the visual metric within the conformal gauge. In the normalisation $\varepsilon = 1$, when $d_1$ is a metric, the boundary has Hausdorff dimension exactly $\delta$, and this is the equality $\dim_H \partial G = \delta$ of the cocompact case.

**Proof sketch.** The covering number of the boundary at scale $r = e^{-\varepsilon n}$ is the number of the shadow sets at distance $n$ from the base point, which grows like $e^{\delta n}$; the covering dimension is the exponent of the growth, $\delta n / \varepsilon n = \delta/\varepsilon$. The shadow of a geodesic ray at distance $n$ is a ball of the visual metric of radius comparable to $e^{-\varepsilon n}$, and the counting of the shadows is the counting of the elements of $G$ at length $n$. The identity is the dimension formula of the Patterson–Sullivan theory, and the independence of $\varepsilon$ is the invariance of the product under the Hölder equivalence.

**Theorem (the Patterson–Sullivan measure).** For a non-elementary hyperbolic group there is a Borel probability measure $\mu$ on $\partial G$, the **Patterson–Sullivan measure**, supported on the whole boundary, that is Ahlfors $\delta$-regular in the normalised visual metric:

$$
\mu\bigl(B(\xi,r)\bigr) \asymp r^{\delta} \qquad (0 < r \leq 1) ,
$$

for every $\xi \in \partial G$. Consequently the Hausdorff dimension of $\mu$ is $\delta$, and in the cocompact case the dimension of the boundary equals the critical exponent,

$$
\dim_H \partial G = \delta = \dim_H \mu .
$$

**Proof sketch.** The measure is constructed as the weak limit of the normalised atomic measures $\sum_{g}e^{-s|g|}\delta_g / \sum_g e^{-s|g|}$ as $s \downarrow \delta$, a construction carried out in *Analysis on Groups*; the limit is a conformal measure and its Ahlfors regularity of exponent $\delta$ is the standard statement of the Patterson–Sullivan theory. The dimension of an Ahlfors $\delta$-regular measure is $\delta$ by the mass distribution principle of *Fractal Geometry*, and the Hausdorff dimension of the boundary is at least $\dim_H\mu$; the reverse inequality is the covering estimate above. The equality $\dim_H \partial G = \delta$ is the content of the cocompact case.

**Remark (the metric dependence and the conformal dimension).** The number $\dim_H \partial G$ is not an invariant of the group: it depends on the visual metric through the parameter $\varepsilon$, the product $\varepsilon \dim_H$ being the invariant. What is a genuine quasi-isometry invariant is the **conformal dimension**, the infimum of the Hausdorff dimensions of the boundary over the metrics of the conformal gauge,

$$
\dim_C \partial G = \inf\{\dim_H(\partial G, d) : d \ \text{in the conformal gauge}\} ,
$$

introduced by Pansu. It is a quasi-isometry invariant of the boundary, and by the theorem of Paulin and Bourdon the conformal gauge of the boundary, up to quasi-Möbius equivalence, determines the group up to quasi-isometry. For the free group the conformal dimension is zero, the boundary being a Cantor set quasisymmetrically equivalent to the standard middle-thirds Cantor set; for a surface group it is one, the boundary being a circle; and for a cocompact Kleinian group acting on hyperbolic three-space it is two.

## The Free Group and the Surface Group

**Theorem (the free group).** Let $F_r$ be the free group of rank $r \geq 2$, with the Cayley graph the $2r$-regular tree and the edge length one.

**(a)** The critical exponent is $\delta = \log(2r-1)$.

**(b)** With the visual metric $d(\xi,\eta) = e^{-(\xi|\eta)}$ of the tree, which is an ultrametric, the boundary has Hausdorff dimension

$$
\dim_H(\partial F_r, d) = \log(2r-1) .
$$

**(c)** With the visual metric normalised so that the child cylinders at each vertex have ratio $1/(2r)$, that is $d_{(2r)}(\xi,\eta) = (2r)^{-(\xi|\eta)}$, the dimension is

$$
\dim_H(\partial F_r, d_{(2r)}) = \frac{\log(2r-1)}{\log(2r)} ,
$$

which is $\log 3/\log 4 = 0.7925\ldots$ for $r = 2$ and $\log 5/\log 6 = 0.8982\ldots$ for $r = 3$.

**(d)** The Patterson–Sullivan measure is the Bernoulli measure that gives each of the $2r$ edges at the root the weight $1/(2r)$ and each of the $2r-1$ forward edges elsewhere the weight $1/(2r-1)$; it is Ahlfors $\delta$-regular with $\delta = \log(2r-1)$ in the normalisation (b).

**Proof sketch.** (a) is the count of the reduced words: the spheres have sizes $2r(2r-1)^{n-1}$ and the abscissa of the convergence of the Poincaré series is the logarithm of the branching, $\log(2r-1)$. (b) the covering number at the scale $e^{-n}$ is the number of the level-$n$ cylinders, comparable to $(2r-1)^n$, so the exponent is $\log(2r-1)$. (c) at the scale $(2r)^{-n}$ the covering number is again comparable to $(2r-1)^n$ and the exponent is $\log(2r-1)/\log(2r)$. (d) the weight of a cylinder of a reduced word of length $n$ is $(2r)^{-1}(2r-1)^{-(n-1)}$, which is comparable to $(e^{-n})^{\log(2r-1)}$ in the metric (b), so the measure is Ahlfors regular of exponent $\log(2r-1)$.

**Remark (the two normalisations).** The two values of (b) and (c) are the same object measured in two metrics of the conformal gauge: the ratio of the dimensions is the ratio of the parameters $\varepsilon$, and the product $\varepsilon\dim_H = \delta$ is the same. This is the phenomenon of the previous section made explicit, and it is the reason the invariants are the critical exponent and the conformal dimension, and not the unnormalised Hausdorff dimension.

**Theorem (the surface group).** Let $G$ be the fundamental group of a closed hyperbolic surface. Then $\partial G$ is a circle, $\delta = 1$, and the boundary in the visual metric of the hyperbolic plane is bi-Lipschitz to the Euclidean circle, so $\dim_H \partial G = 1$. More generally, for a cocompact Kleinian group acting on hyperbolic three-space the boundary is the sphere, $\delta = 2$ and the dimension is two; for a convex-cocompact group that is not cocompact the limit set is a proper closed subset of the sphere and its dimension is the critical exponent, strictly between one and two for a quasifuchsian group whose limit set is not a round circle.

**Proof sketch.** The boundary of the hyperbolic plane is its circle at infinity, and the visual metric of the hyperbolic plane is bi-Lipschitz to the Euclidean metric, so the dimension is one; the critical exponent is the growth rate, which is one. For hyperbolic three-space the same argument gives the sphere and the dimension two. For a quasifuchsian group that is not Fuchsian the limit set is a Jordan curve that is not a round circle, and its dimension is strictly greater than one and strictly less than two by the theorem of Bowen and the rigidity results; the exact value depends on the group.

## Summary

A hyperbolic group has a Gromov boundary, a compact metric space under the visual metrics $d_\varepsilon(\xi,\eta) = e^{-\varepsilon(\xi|\eta)}$, which form the conformal gauge, and its Hausdorff dimension is governed by the critical exponent $\delta$ of the Poincaré series. The exponent is finite, positive, equal to the exponential growth rate and hence a quasi-isometry invariant, and the dimension formula is $\dim_H(\partial G, d_\varepsilon) = \delta/\varepsilon$, with the value $\delta$ in the normalisation $\varepsilon = 1$; this is the equality $\dim_H \partial G = \delta$ of the cocompact case. The Patterson–Sullivan measure is the Ahlfors $\delta$-regular probability measure on the boundary, so the boundary and the measure have the same dimension in the normalised metric. For the free group $F_r$ the boundary is a Cantor set and $\delta = \log(2r-1)$, giving the dimension $\log(2r-1)$ in the canonical visual metric and $\log(2r-1)/\log(2r)$ in the metric with child ratio $1/(2r)$; for a surface group the boundary is a circle and the dimension is one; for a cocompact Kleinian group acting on hyperbolic three-space the boundary is the sphere and the dimension is two. The unnormalised dimension is not an invariant; the invariants are the critical exponent and the conformal dimension of Pansu, and by the theorem of Paulin and Bourdon the boundary up to quasi-Möbius determines the group up to quasi-isometry. The group theory is that of *Hyperbolic Groups* and *Geometric Group Theory*, the measure is *Analysis on Groups*', the end spaces are those of *Fractal Trees and Dendrites*, and the dimension is that of *Fractal Geometry*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\partial G$, $\partial X$ | Gromov boundary of the group, of the hyperbolic space |
| $(\xi\lvert\eta)$, $o$ | Gromov product with respect to the base point; the base point |
| $d_\varepsilon$, conformal gauge | $e^{-\varepsilon(\xi\lvert\eta)}$; the family of the Hölder-equivalent visual metrics |
| $\delta$ | Critical exponent of the Poincaré series; exponential growth rate |
| $\sum_g e^{-s\lvert g\rvert}$ | Poincaré series; its abscissa of convergence is $\delta$ |
| $\mu$ | Patterson–Sullivan measure; Ahlfors $\delta$-regular |
| $\dim_H(\partial G, d_\varepsilon)$ | $\delta/\varepsilon$; equals $\delta$ in the normalisation $\varepsilon=1$ |
| $\dim_C \partial G$ | Conformal dimension of Pansu; quasi-isometry invariant |
| $\log(2r-1)$, $\log(2r-1)/\log(2r)$ | Boundary dimension of the free group in the two normalisations |
| $2r(2r-1)^{n-1}$ | Number of words of length $n \geq 1$ in the free group of rank $r$ |

## Further Reading

- Mikhael Gromov, "Hyperbolic groups", in *Essays in Group Theory* (Mathematical Sciences Research Institute Publications 8, 1987), 75–263, for the hyperbolicity, the boundary and the growth.
- Michel Coornaert, Thomas Delzant and Athanase Papadopoulos, *Géométrie et théorie des groupes* (Springer Lecture Notes in Mathematics 1441, 1990), for the boundary, the visual metric and the critical exponent.
- Michel Coornaert, "Mesures de Patterson–Sullivan sur le bord d'un espace hyperbolique au sens de Gromov", *Pacific Journal of Mathematics* 159 (1993), 241–270, for the Patterson–Sullivan measure and its regularity.
- Samuel J. Patterson, "The limit set of a Fuchsian group", *Acta Mathematica* 136 (1976), 241–273, and Dennis Sullivan, "The density at infinity of a discrete group of hyperbolic motions", *Publications Mathématiques de l'IHÉS* 50 (1979), 171–202, for the measure and the critical exponent.
- Pierre Pansu, "Dimension conforme et sphère à l'infini des variétés hyperboliques", *Annales de l'Institut Fourier* 39 (1989), 177–212, for the conformal dimension and its quasi-isometry invariance.
- Marc Bourdon, "Structure quasi-conformes des bords de groupes hyperboliques", *Annales de l'Institut Fourier* 46 (1996), 1245–1254, for the boundary, the quasi-Möbius structure and the quasi-isometry.
- Frédéric Paulin, "Un groupe hyperbolique est déterminé par son bord", *Journal of the London Mathematical Society* 54 (1996), 50–74, for the boundary as a quasi-isometry invariant.
- James W. Cannon, "The combinatorial Riemann mapping theorem", *Acta Mathematica* 173 (1994), 155–234, for the boundary and the conjecture that a hyperbolic group with the sphere as boundary acts on hyperbolic space.
