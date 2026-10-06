# __The Fatou Components and the Classification of the Dynamics__

## Introduction

The Fatou set $F(f)$ of a rational map of degree $d \geq 2$ is open, and its connected components are the **Fatou components**. The classification of the dynamics of $f$ is the classification of what happens on these components: each component is carried by $f$ to another component, the components organise themselves into the orbits that the map permutes, and the dynamics on a component that the map revisits periodically is one of a small number of types. This article states the classification for the complex rational and polynomial maps: the periodic Fatou components are the attracting basins, the parabolic basins, the Siegel discs and the Herman rings, the last two named for the indifferent rotation they carry; the theorem of Sullivan shows that every component is eventually periodic, so the list is complete. The two theorems that reduce the polynomial case to this list, those of Böttcher and of Leau–Fatou–Julia–Ritt, are stated here and used by the following articles of the subcategory.

This article is placed after *The Julia Sets of a Complex Polynomial*, whose partition of the sphere into the Fatou and Julia sets it refines, and after *The Mandelbrot Set and the Quadratic Family*, because the parameter theory of that article tests the classification: the hyperbolic components are the parameters whose attracting basins survive a perturbation, and the bifurcations are the changes of type. The general theory of the rational maps, the stability of the classification under perturbation, the holomorphic motion and the rigidity theorems belong to *The Geometry of the Julia Sets* of Part IV; the theory of the normal family and the local dynamics of a holomorphic germ belong to *Complex Analysis*; the dynamics of the map as a topological system belongs to *Topological Dynamics*. The iterated function systems of the subcategory do not enter here.

No physics is invoked.

## Periodic Components and Their Orbits

**Definition.** Let $f$ be a rational map of degree $d \geq 2$ and let $U$ be a Fatou component. Since $f$ is an open map and $f(F) \subseteq F$, the image $f(U)$ is contained in a single component, written $f(U)$ again; the component $U$ is **periodic** if $f^p(U) = U$ for some $p \geq 1$, **preperiodic** if some iterate is periodic, and **wandering** otherwise. A periodic component of period $p$ is the domain of the dynamics of the restricted map $f^p : U \to U$.

**Proposition.** The image of a component is a component, $f(U)$ is a component of $F$, and the map $U \mapsto f(U)$ sends the set of components onto itself; a component is periodic exactly when it lies on a cycle of this map.

**Proof.** $f(U)$ is connected and open and is contained in $F$, so it lies in a unique component $V$; since $f$ is surjective and open, $f(U)$ is also open and closed in the component $V$ that contains it, so $f(U) = V$. The assignment is therefore well defined, and it is surjective because every point of $F$ has a preimage in $F$ by the complete invariance of $F$.

**Definition.** Let $U$ be a periodic component of period $p$. A **cycle** of $U$ is a periodic orbit of $f^p$ contained in $U$; such a cycle is attracting, superattracting, parabolic or indifferent according to the multiplier of the cycle, as in *The Julia Sets of a Complex Polynomial*.

**Theorem.** If $U$ is a periodic Fatou component and $z \in U$ has an accumulation point of its orbit in $U$, then the $\omega$-limit set of $z$ in $U$ is a compact $f^p$-invariant subset of $U$.

**Proof sketch.** The orbit of $z$ is relatively compact in $U$, because the iterates of $f^p$ on $U$ form a normal family and the limit of any convergent subsequence is a holomorphic map, by *Complex Analysis*; the $\omega$-limit set is then nonempty, compact and invariant, and it lies in $U$ rather than on its boundary by normality.

## The Classification Theorem

**Definition.** Let $U$ be a periodic Fatou component of period $p$.

**(a)** $U$ is an **attracting basin** if $U$ contains an attracting or superattracting cycle $\zeta$ of $f^p$ and $U$ is the component of the basin of $\zeta$ that contains $\zeta$; then $f^{pn}(z) \to \zeta$ for every $z \in U$.

**(b)** $U$ is a **parabolic basin** if $\partial U$ contains a parabolic cycle of $f^p$ and $f^{pn}(z) \to \partial U$ for every $z \in U$, the convergence being locally uniform, the cycle attracting the points of $U$ through the petals of the Leau–Fatou flower.

**(c)** $U$ is a **Siegel disc** if $f^p$ is holomorphically conjugate on $U$ to a rigid rotation $w \mapsto \lambda w$ with $|\lambda| = 1$, $\lambda$ not a root of unity, and the conjugacy is a bijection of $U$ onto a disc; the rotation is then ergodic on $U$.

**(d)** $U$ is a **Herman ring** if $U$ is an annulus and $f^p$ is holomorphically conjugate on $U$ to a rigid rotation of the annulus, with the rotation number irrational.

**Theorem (Fatou, Julia, Leau, Ritt).** Every periodic Fatou component of a rational map of degree $d \geq 2$ is of exactly one of the four types above. Every attracting basin contains a critical point of $f^p$, and there are at most $2d-2$ attracting cycles.

**Proof sketch.** The $\omega$-limit set of a point of $U$ is compact and invariant in $U$. If it is a single point, the point is a fixed point of $f^p$ and the local dynamics is classified by the multiplier: attracting or superattracting gives case (a); parabolic gives (b), by the Leau–Fatou flower; indifferent gives either (c) or the point is in $J$, and the case (c) is the linearisation theorem of Siegel. If the limit set is larger than a point, it is a compact connected infinite set on which $f^p$ acts, and the theory of the **Julia–Wolff** and the **Denjoy–Wolff** point and the classification of the automorphisms of a domain show that it is a circle on which $f^p$ is conjugate to a rotation, giving (d) or a degenerate case; the possibility of a non-injective limit is excluded by the Riemann–Hurwitz formula, which forces the presence of a critical point. The counting of the attracting cycles follows because each attracting basin contains a critical point and there are $2d-2$ critical points counted with multiplicity. The complete argument is that of the classification of the rational maps in *The Geometry of the Julia Sets*.

## The Polynomial Case

**Theorem (the absence of Herman rings).** A polynomial has no Herman rings, and every Fatou component of a polynomial is simply connected.

**Proof sketch.** A Herman ring has two invariant boundary circles, and each is mapped homeomorphically onto itself by $f^p$; on each the map is conjugate to the same irrational rotation, and the classical argument of Herman shows that a Herman ring forces the two complementary components of the ring to be exchanged by $f^p$ and each to contain a **pole** of the map, so that a Herman ring requires at least two poles. A polynomial has a single pole, at $\infty$, which lies in the unbounded component, so the configuration is impossible and a polynomial has no Herman rings. For the simple connectivity, every bounded component of $F$ lies in the basin of an attracting or parabolic cycle or is a Siegel disc, and each of these is simply connected: the basin of an attracting or parabolic point has the point or the parabolic cycle in its closure and is a union of preimages of a simply connected immediate basin, and the Siegel disc is a disc by definition. The details are in *The Geometry of the Julia Sets*.

**Theorem (Böttcher).** Let $f$ be a polynomial of degree $d \geq 2$. There is a conformal map $\varphi$ from a neighbourhood of $\infty$ onto the complement of a closed disk, with

$$
\varphi(f(z)) = \varphi(z)^d , \qquad \varphi(z) \sim z \ \text{as } z \to \infty ,
$$

the **Böttcher coordinate**. If $K(f)$ is connected then $\varphi$ extends conformally to the whole basin of $\infty$, $A(\infty) \to \hat{\mathbb{C}} \setminus \overline{\mathbb{D}}$, and the basin of $\infty$ is simply connected.

**Proof sketch.** Near $\infty$ the map $f$ is conjugate, by the local coordinate $w = 1/z$, to a holomorphic map tangent to $w \mapsto w^d$ at $w = 0$; the local inverse branches and the estimate $\varphi_n(z) = f^n(z)^{1/d^n}$ converge locally uniformly off $K$, defining $\varphi$ as the limit of the root $d^n$-th of the iterates. The convergence and the functional equation are the content of the theorem; the extension to the basin when $K$ is connected is the monodromy of the root along the simply connected complement. The Green's function $G = \log|\varphi|$ is the subject of *The Escape Radius and the Green's Function*.

**Theorem (Leau–Fatou–Julia–Ritt).** Let $f$ have a parabolic fixed point at $0$ with multiplier a primitive $q$-th root of unity, and let $k+1$ be the multiplicity of the fixed point of $f^q$ at $0$. Then there are $k$ **attracting petals** and $k$ **repelling petals**, each a simply connected domain with vertex at $0$, on each of which $f^q$ is conformally conjugate to the translation $w \mapsto w+1$; the union of the petals is a punctured neighbourhood of $0$, and the petals are exchanged by the dynamics. The same statement holds at a parabolic cycle.

**Proof sketch.** After a change of variable the germ reads $f^q(z) = z + z^{k+1} + \cdots$; the Fatou coordinate in the direction of a petal is $\psi(z) = -1/(kz^k) + \cdots$, which satisfies $\psi(f^q(z)) = \psi(z) + 1$, and the petals are the preimages under $\psi$ of the half-planes of the form $\{\operatorname{Re} w > R\}$ and $\{\operatorname{Re} w < -R\}$. The statement at a cycle follows by applying the result to a suitable iterate.

**Corollary (classification for polynomials).** Every periodic Fatou component of a polynomial of degree $d \geq 2$ is an attracting basin, a parabolic basin or a Siegel disc. The attracting and parabolic basins contain critical points of $f^p$, and a polynomial of degree $d$ has at most $d-1$ attracting cycles.

## The No-Wandering-Domains Theorem

**Theorem (Sullivan).** Let $f$ be a rational map of degree $d \geq 2$. Every Fatou component of $f$ is eventually periodic: there is a component $U$ and an $n \geq 0$ such that $f^n(U)$ is periodic. Equivalently, $f$ has no wandering domains.

**Proof sketch.** The proof is by **quasiconformal rigidity**. If a wandering domain existed, one constructs from it a non-trivial deformation of $f$ inside the space of rational maps, by pulling back a quasiconformal deformation of the sphere through the dynamics and using the measurability of the Julia set; the space of deformations is finite-dimensional, the deformations of a rational map of the given degree form a manifold of dimension $2d-2$, and the iteration produces an infinite-dimensional family of deformations, a contradiction. The energy estimates and the measurable Riemann mapping theorem that make the construction work are those of the theory of quasiconformal maps, and the theorem is proved in full in *The Geometry of the Julia Sets*; it is due to Sullivan.

**Corollary (the completeness of the list).** For a rational map of degree $d \geq 2$, the classification of the periodic components given above classifies **every** Fatou component: each is carried by some iterate to one of the four types, and the four types are exactly the periodic behaviours.

**Corollary (the case of the polynomials).** The Fatou set of a polynomial of degree $d \geq 2$ is the union of the basins of the attracting and parabolic cycles together with the Siegel discs, each component being eventually one of these, and the Julia set is the common boundary of all of them, by the theorem on the boundary of the Fatou components of *The Julia Sets of a Complex Polynomial*.

## Examples in the Quadratic Family

**Example (the circle and the two basins).** For $f(z) = z^2$ the Fatou set has exactly two components: the unit disk, the basin of the superattracting fixed point $0$, and the exterior of the closed disk, the basin of the superattracting fixed point $\infty$. The Julia set is the unit circle, the common boundary of the two basins, and it is the boundary of both.

**Example (the basilica).** For $f(z) = z^2-1$ the attracting cycle $\{0,-1\}$ has an immediate basin $U$ containing $0$ and $-1$, and the basin is the union of the iterated preimages of $U$; the component $U$ is the whole basin of the cycle, the Julia set is the boundary, and the parameter lies in the period-two bulb of *The Mandelbrot Set and the Quadratic Family*.

**Example (the parabolic flower).** For $f(z) = z^2 + 1/4$ the fixed point is $z = 1/2$, with multiplier $1$ and multiplicity two, so the fixed point is parabolic; there is one attracting petal, and the basin of the parabolic point is the Fatou component, on which $f$ is conjugate to a translation. The critical orbit $0, 1/4, 5/16, \ldots$ converges to $1/2$ through the petal, as the numerical orbit of *The Mandelbrot Set and the Quadratic Family* shows.

**Example (a Siegel disc).** On the boundary of the main cardioid of $M$ there are parameters at which the fixed point has multiplier $\lambda = e^{2\pi i\theta}$ with $\theta$ irrational and satisfying the Brjuno condition; for them the fixed point is the centre of a Siegel disc, a Fatou component on which $f$ is conjugate to the rigid rotation of angle $\theta$. If $\theta$ fails the Brjuno condition the fixed point is a **Cremer point** and lies in the Julia set. The Brjuno condition, its sharpness by Yoccoz, and the arithmetic of the rotation number belong to *Complex Analysis* and to *The Geometry of the Julia Sets*.

## The Other Algebras

**Remark (where the classification is open).** The classification above rests on the complex analysis of one variable: the Riemann mapping theorem, the classification of the automorphisms of a domain, the measurable Riemann mapping theorem and the local dynamics of a holomorphic germ. For a **split-complex** map the plane is a product of two real lines, and the classification of the real dynamics is different from the complex one; the split-complex Fatou and Julia sets are the subject of *The Split-Complex Julia Sets*, where the dichotomy is read off the two real maps and not from a classification of the components. For a **quaternion** or a **biquaternion** map there is no Cauchy–Riemann theory in the commutative sense, and the Fatou–Julia classification is not complete; the corresponding articles *The Quaternion Quadratic Map and Its Julia Sets* and *The Biquaternion Quadratic Map and Its Julia Sets* report the state of the question rather than a theorem. The several-variable theory, where the Fatou components acquire a richer structure and the classification is genuinely different, is that of *Several Complex Variables*.

## Summary

The Fatou set of a rational map of degree $d \geq 2$ is a union of components permuted by the map, and a periodic component is an attracting basin, a parabolic basin, a Siegel disc or a Herman ring. This classification of the periodic components is the theorem of Fatou, Julia, Leau and Ritt: the limit behaviour of the iterates is decided by the multiplier at the cycle, the attracting and superattracting cases giving a basin with a critical point in it, the parabolic case giving the Leau–Fatou flower and its petals, and the indifferent case giving the linearisation of Siegel when the rotation number satisfies the Brjuno condition and otherwise a Cremer point in the Julia set. Sullivan's no-wandering-domains theorem shows that every Fatou component is eventually periodic, so the list of the four types is complete; the proof is by quasiconformal rigidity.

For a polynomial the list shortens: there are no Herman rings, every Fatou component is simply connected, and every periodic component is an attracting basin, a parabolic basin or a Siegel disc. The Böttcher coordinate linearises the polynomial near infinity and is the local model of the basin of infinity; the Leau–Fatou–Julia–Ritt theorem gives the local model at a parabolic cycle. The quadratic family exhibits all the cases: $z^2$ has two basins and the circle; $z^2-1$ has an attracting two-cycle; $z^2+1/4$ has a parabolic basin with one petal; and the parameters on the main cardioid with Brjuno rotation number have Siegel discs. The general rational theory and the rigidity theorems are Part IV's, and for the other algebras of this Part the classification is not complete.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $U$, $f(U)$ | Fatou component and its image component |
| periodic, preperiodic, wandering | $f^p(U)=U$; eventually periodic; otherwise |
| attracting basin | Component of the basin of an attracting cycle |
| parabolic basin | Basin of a parabolic cycle, with the Leau–Fatou petals |
| Siegel disc | Component on which $f^p$ is conjugate to a rigid rotation |
| Herman ring | Annular component with a rigid rotation; absent for polynomials |
| $\varphi$ | Böttcher coordinate, $\varphi(f(z)) = \varphi(z)^d$ |
| petals, Fatou coordinate | Domains of conjugacy to a translation at a parabolic cycle |
| no-wandering-domains theorem | Every Fatou component is eventually periodic (Sullivan) |
| Brjuno condition | Arithmetical condition for linearisability at an indifferent fixed point |

## Further Reading

- Pierre Fatou, "Sur les équations fonctionnelles", *Bulletin de la Société Mathématique de France* 47 (1919), 161–271; 48 (1920), 33–94 and 208–314, for the classification of the components in the attracting and parabolic cases.
- Gaston Julia, "Mémoire sur l'itération des fonctions rationnelles", *Journal de Mathématiques Pures et Appliquées* 8 (1918), 47–245, for the local dynamics and the repelling case.
- Carl Ludwig Siegel, "Iteration of analytic functions", *Annals of Mathematics* 43 (1942), 607–612, for the linearisation at an indifferent fixed point.
- Jean-Christophe Yoccoz, "Théorème de Siegel, nombres de Bruno et polynômes quadratiques", *Astérisque* 231 (1995), 3–88, for the sharp arithmetic condition.
- Dennis P. Sullivan, "Quasiconformal homeomorphisms and dynamics I: Solution of the Fatou–Julia problem on wandering domains", *Annals of Mathematics* 122 (1985), 401–418, for the no-wandering-domains theorem.
- Alexander Brjuno, "Analytic form of differential equations", *Transactions of the Moscow Mathematical Society* 25 (1971), 131–288, for the Brjuno condition.
- John Milnor, *Dynamics in One Complex Variable*, 3rd edition (Princeton University Press, 2006), for the classification and the quadratic examples.
