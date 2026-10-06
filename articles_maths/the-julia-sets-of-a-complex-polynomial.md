# __The Julia Sets of a Complex Polynomial__

## Introduction

Let $f$ be a complex polynomial of degree $d \geq 2$, read as a self-map of the Riemann sphere $\hat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$ by $f(\infty) = \infty$, and let $f^n$ be its $n$-th iterate. The points of the sphere are separated into two sets by the behaviour of the sequence $(f^n)$: the **Fatou set** $F(f)$, where the iterates form a normal family and the dynamics is stable under small perturbations of the starting point, and the **Julia set** $J(f)$, its complement, where the iterates are chaotic in the precise sense that they are not normal on any neighbourhood. This article defines the two sets, identifies the Julia set as the closure of the repelling periodic points and as the boundary of every Fatou component, records the invariance and the self-similarity that make the Julia set the object of the whole subcategory, and states the existence of an invariant measure carried by it. The quadratic and higher-degree examples are worked in the following articles of the subcategory.

The article is the $\mathbb{C}$ instance of the general theory, and the boundary is stated once here. The **general** theory of the Fatou and Julia sets of a rational map, the classification of the periodic components, the local connectivity, the external rays and the geometric measure theory of the Julia sets belong to *The Geometry of the Julia Sets*, written in Part IV; the dynamics of the map as a topological and a smooth dynamical system belong to *Topological Dynamics* and *Smooth Dynamical Systems* of Part III, and the coding of the dynamics by the shift to *Symbolic Dynamics*. This article uses the partition and the polynomial theorems that the corpus's complex analysis makes available, and it defers everything general to those articles rather than restating them. The escape criterion, the Green's function and the dimension of the Julia set are the subjects of *The Escape Radius and the Green's Function* and *The Hausdorff Dimension of the Julia Sets* of this subcategory, and are quoted here only where the dynamical picture needs them.

The complex analysis used is that of *Complex Analysis*: the Riemann sphere, the modulus and the spherical metric, holomorphic functions, and Montel's theorem on normal families. No physics is invoked.

## The Polynomial and Its Iterates

### The Map

**Definition.** A **complex polynomial of degree $d \geq 2$** is a map

$$
f(z) = a_d z^d + a_{d-1}z^{d-1} + \cdots + a_1 z + a_0, \qquad a_d \neq 0,\ d \geq 2,
$$

extended to $\hat{\mathbb{C}}$ by $f(\infty) = \infty$. The **iterates** are $f^0 = \mathrm{id}$ and $f^{n+1} = f \circ f^n$; the **orbit** of $z$ is the sequence $(f^n(z))_{n \geq 0}$.

**Proposition.** The extension is holomorphic at $\infty$, which is a fixed point of multiplier $0$; writing $w = 1/z$ near $\infty$, the map reads $w \mapsto w^d/\bigl(a_d + a_{d-1}w + \cdots\bigr)$, so $\infty$ is a **superattracting** fixed point of local degree $d$, and $f$ has degree $d$ as a map of the sphere onto itself.

**Proof.** Clearing denominators in $f(1/w)^{-1}$ gives the displayed expression, which is holomorphic and vanishes to order $d$ at $w = 0$; its derivative vanishes there, so the fixed point is superattracting, and a point of local degree $d$ is a critical point of multiplicity $d-1$. Every point of $\hat{\mathbb{C}}$ has $d$ preimages counted with multiplicity, by the fundamental theorem of algebra, so the map has degree $d$. Since the map $w \mapsto w^d/(a_d+\cdots)$ is tangent to $w \mapsto w^d/a_d$ and fixes $w = 0$ simply, the fixed point $\infty$ itself has **multiplicity one** in the sense of the fixed-point count: a degree-$d$ rational map has $d+1$ fixed points with multiplicity, and the $d$ finite ones given by $f(z) = z$ leave a single one at $\infty$.

### Periodic Points and Their Multipliers

**Definition.** A point $z$ is **periodic** of period $p \geq 1$ if $f^p(z) = z$ and $p$ is the least such integer; it is **fixed** if $p = 1$. The **multiplier** of the cycle is $\lambda = (f^p)'(z)$. The cycle is **attracting** if $|\lambda| < 1$, **superattracting** if $\lambda = 0$, **repelling** if $|\lambda| > 1$, and **indifferent** if $|\lambda| = 1$, the indifferent case being **rationally indifferent** when $\lambda$ is a root of unity and **irrationally indifferent** otherwise. A point is **preperiodic** if some iterate of it is periodic.

**Proposition.** The multiplier is the same at every point of the cycle, and it is independent of the point chosen on the cycle; the chain rule gives $(f^p)'(z) = \prod_{k=0}^{p-1} f'(f^k(z))$, a product invariant under cyclic permutation.

**Definition.** A **critical point** of $f$ is a point at which $f'$ vanishes; the finite critical points are the $d-1$ roots of $f'$ counted with multiplicity, and $\infty$ is a critical point of multiplicity $d-1$. The **critical orbit** is the orbit of the critical points, and $f$ is **post-critically finite** if every critical orbit is finite.

**Example.** For the quadratic family $f_c(z) = z^2 + c$ the only finite critical point is $0$, the critical orbit is $0 \mapsto c \mapsto c^2+c \mapsto \cdots$, and $f_c$ is post-critically finite exactly when this orbit is finite; $c = 0$ and $c = -2$ are the first examples, and $c = i$ gives the finite orbit $0 \mapsto i \mapsto -1+i \mapsto -i \mapsto -1+i$, of preperiod $1$ and period $2$.

## The Fatou and Julia Sets

### Normal Families

**Definition.** Let $U \subseteq \hat{\mathbb{C}}$ be open and let $\mathcal{F}$ be a family of holomorphic maps $U \to \hat{\mathbb{C}}$. The family is **normal** if every sequence in it has a subsequence converging locally uniformly on $U$, in the spherical metric, to a holomorphic map $U \to \hat{\mathbb{C}}$. Equivalently, by *Complex Analysis*, the family is **equicontinuous** on compact subsets of $U$ with respect to the spherical metric.

**Theorem (Montel).** A family of holomorphic maps on a domain that omits three fixed values of $\hat{\mathbb{C}}$ is normal.

**Proof sketch.** Three omitted values may be moved to $0, 1, \infty$ by a Möbius transformation; the classical Montel theorem states that the family of holomorphic maps into $\hat{\mathbb{C}} \setminus \{0,1,\infty\}$ is normal, and conjugating by the Möbius map returns the statement. This is the normal-family theorem of *Complex Analysis*.

### The Two Sets

**Definition.** The **Fatou set** of $f$ is

$$
F(f) = \{z \in \hat{\mathbb{C}} : \text{the family } \{f^n\}_{n \geq 0} \text{ is normal on some neighbourhood of } z\},
$$

and the **Julia set** is its complement, $J(f) = \hat{\mathbb{C}} \setminus F(f)$.

**Theorem (basic properties).**

**(a)** $F(f)$ is open and $J(f)$ is closed and nonempty.

**(b)** Both sets are **completely invariant**: $f(F) \subseteq F$, $f^{-1}(F) = F$, and $f(J) = J = f^{-1}(J)$.

**(c)** $J(f) = J(f^n)$ for every $n \geq 1$, and $J(f)$ contains infinitely many points.

**(d)** If $z$ is an attracting, superattracting or rationally indifferent periodic point then $z \in F(f)$; if $z$ is a repelling periodic point then $z \in J(f)$.

**Proof sketch.** (a) Normality is a local property of the family, so its set of points is open; $J(f)$ is nonempty because otherwise the iterates would be normal on the whole sphere, hence equicontinuous, and the degrees of $f^n$ would be bounded, whereas $\deg f^n = d^n \to \infty$. (b) The composition of a normal family with a holomorphic map is normal, and $f$ is open, which gives the invariance of $F$, hence of $J$. (c) The family $\{f^{kn}\}$ is a subfamily of $\{f^n\}$ and normality of the whole family is equivalent to normality of the $n$-th powers, by a standard subfamily argument. (d) Near an attracting cycle the iterates contract towards it and form a normal family; near a repelling cycle the images of a small disk spread out and the family is not normal. The complete proof of (c) and (d) and the rational-map form of all four are in *The Geometry of the Julia Sets*.

## The Julia Set as the Repelling Periodic Points

**Theorem (Fatou, Julia).** For a polynomial of degree $d \geq 2$,

$$
J(f) = \overline{\{\text{repelling periodic points of } f\}} .
$$

**Proof sketch.** A repelling periodic point lies in $J$, since at it the iterates are not equicontinuous. For the converse, one shows that the backward orbit of a repelling periodic point is dense in $J$: the set of repelling periodic points is nonempty and infinite, its limit points lie in $J$ by (d), and a counting argument over the $d^n$ preimages of a small disk shows that the backward orbit accumulates at every point of $J$. The argument uses Montel's theorem and the Julia set's complete invariance, and it is the Fatou–Julia theorem of *The Geometry of the Julia Sets*.

**Corollary.** $J(f)$ is the smallest closed completely invariant set with at least three points; equivalently, if a closed set $E$ satisfies $f^{-1}(E) = E$ and contains no critical point of $f$, then $J(f) \subseteq E$.

**Proof sketch.** A closed completely invariant set avoiding the critical points can be pulled back without ramification, which gives a normal family on its complement; hence its complement lies in $F(f)$.

**Corollary (the preimages of a generic point).** For every $z$ outside a set of at most two **exceptional** points,

$$
J(f) = \overline{\bigcup_{n \geq 0} f^{-n}(z)} .
$$

**Proof sketch.** The exceptional set is the set of points whose backward orbit is finite, and it has at most two points for a rational map of degree $d \geq 2$; for a polynomial it is contained in $\{\infty\}$. For a non-exceptional $z$ the backward orbit is infinite and its closure is completely invariant and not a finite set, so by the corollary above it contains $J$, and it is contained in $J$ by the invariance of $J$. The exceptional dichotomy is proved in *The Geometry of the Julia Sets*.

## The Boundary of the Fatou Components

**Definition.** The **filled Julia set** is

$$
K(f) = \{z \in \mathbb{C} : \text{the orbit } (f^n(z)) \text{ is bounded}\} ,
$$

a compact subset of $\mathbb{C}$; the **basin of infinity** is $A(\infty) = \hat{\mathbb{C}} \setminus K(f)$, the set of points escaping to $\infty$.

**Theorem.** For a polynomial of degree $d \geq 2$:

**(a)** $J(f) = \partial K(f) = \partial A(\infty)$;

**(b)** $F(f) = \mathring{K}(f) \cup A(\infty)$, the union of the interior of the filled Julia set and the basin of infinity;

**(c)** $A(\infty)$ is connected and simply connected, and $K(f)$ is connected if and only if $A(\infty)$ is simply connected;

**(d)** $J(f)$ is the boundary of **every** Fatou component: if $U$ is a component of $F(f)$, then $\partial U = J(f)$;

**(e)** $K(f)$ is connected if and only if every critical point of $f$ lies in $K(f)$; for the quadratic family this reads $K(f_c)$ connected $\iff 0 \in K(f_c) \iff c \in M$, where $M$ is the Mandelbrot set of *The Mandelbrot Set and the Quadratic Family*.

**Proof sketch.** (a) A point of $\partial K$ is not in the basin and cannot have a neighbourhood on which the iterates are normal and bounded, so it lies in $J$; conversely the iterates near a point of $A(\infty)$ converge locally uniformly to $\infty$, so $A(\infty) \subseteq F$, and near a point of $\mathring K$ the iterates are bounded and hence normal, so $F = \mathring K \cup A(\infty)$ and $J = \partial K = \partial A(\infty)$. (c) $A(\infty)$ is the domain of the Böttcher coordinate, whose construction is the subject of *The Escape Radius and the Green's Function*; a Riemann-map argument shows that $K$ is connected exactly when $A(\infty)$ is simply connected. (d) Each Fatou component is mapped eventually into a periodic component, and the boundary of every component is carried onto the boundary of its image by the open map $f$; the common boundary is therefore a closed completely invariant set with more than two points, hence $J$ by the corollary above. (e) If a critical point lies in $A(\infty)$ then its image and the whole critical orbit escape, and the preimages of a neighbourhood of $\infty$ disconnect $K$; conversely the escape of the critical orbit forces $K$ disconnected. The detailed arguments are in *The Geometry of the Julia Sets* and in the local-connectivity theory cited there.

## Self-Similarity and Coding

**Theorem (the inverse branches).** Let $z$ be a point of $J(f)$ at which $(f^n)'(z) \neq 0$ for all $n$. Then for every neighbourhood $V$ of $z$ and every sufficiently large $n$ there is a branch $g_n$ of $f^{-n}$ defined on a disk about $f^n(z)$ with $g_n(f^n(z)) = z$; the branches are contractions by the factor $|(f^n)'(z)|^{-1}$, and the Julia set is the attractor of the resulting system of inverse branches on the repelling side.

**Proof sketch.** The inverse function theorem gives a local branch of $f^{-n}$ near $f^n(z)$, and its derivative at $f^n(z)$ is $1/(f^n)'(z)$; since $|(f^n)'(z)|$ grows exponentially along the repelling directions, the branch contracts. The branch maps a neighbourhood of $f^n(z)$ into a neighbourhood of $z$, and the union of the branches over $n$ generates $J$, by the density of the backward orbit stated above.

**Remark (the sense of self-similarity).** The Julia set is **invariant**, $J = f^{-1}(J)$, and it is covered by the $d^n$ preimages of any of its neighbourhoods; exact self-similarity, in the sense of the iterated function systems of *Fractal Geometry* with finitely many contracting similarities, holds only in the special cases of $z \mapsto z^d$, whose Julia set is the unit circle with $d$ rotational symmetries, and of the Chebyshev and Lattès examples constructed from a group action. For a general polynomial the self-similarity is **conformal**: the inverse branches are conformal contractions whose ratios vary, and it is the invariant measure, not a finite system of similitudes, that records the balance of the pieces. The iterated function systems proper are the subject of *Iterated Function Systems in the Complex Plane*, and the general self-similar construction is the subject of *Fractal Geometry*.

## The Invariant Measure

**Theorem (Brolin).** For a polynomial $f$ of degree $d \geq 2$ there is a unique probability measure $\mu$ on $\hat{\mathbb{C}}$ satisfying

$$
\int \varphi \, d\mu = \frac{1}{d^n}\sum_{f^n(w) = z} \varphi(w)
$$

for every continuous $\varphi$ and every $z$ outside the exceptional set, the sum being over the $d^n$ preimages of $z$ counted with multiplicity. The measure is $f$-invariant, $f_*\mu = \mu$; it is supported on $J(f)$; it is the measure of maximal entropy $\log d$; and it is the **equilibrium measure** of the basin, obtained as the weak limit of the normalised counting measures of the preimages of any non-exceptional point.

**Proof sketch.** The displayed average over the $d^n$ preimages converges weakly to a probability measure, by the Banach–Alaoglu theorem and the choice of a limit point of the sequence of averaged counting measures; the averaging identity makes the limit $f$-invariant and independent of $z$, and its entropy is $\log d$, the topological entropy of $f$. The identification of the maximal entropy measure with the equilibrium measure is the theory of *Ergodic Theory* and *The Geometry of the Julia Sets*. The computation of the entropy and the Lyapunov exponent as averages is the thermodynamic formalism, cited there.

**Theorem (the measure of full dimension).** If $J(f)$ is a hyperbolic Julia set in the sense below, then there is an $f$-invariant ergodic measure $\mu_s$ of Hausdorff dimension exactly $\dim_H J(f)$: it is the equilibrium state of the potential $-s\log|f'|$ at the value $s$ solving the pressure equation of *The Hausdorff Dimension of the Julia Sets*, and it satisfies the dimension formula

$$
\dim_H J(f) = \frac{h_{\mu_s}}{\chi_{\mu_s}}, \qquad \chi_{\mu_s} = \int \log|f'| \, d\mu_s ,
$$

of Ledrappier and Young, where $h$ is the measure-theoretic entropy. For a polynomial the measure of maximal entropy has dimension $\log d / \chi_{\mu} < \dim_H J(f)$ whenever the Julia set is not a rectifiable curve, and the two coincide only in the exceptional cases such as $J(f) = \hat{\mathbb{C}}$ of a rational map.

**Proof sketch.** The equilibrium state of $-s\log|f'|$ exists by the Ruelle–Perron–Frobenius theorem, because the map is expanding on the Julia set; the Bowen equation $P(-s\log|f'|) = 0$ has a unique root, its equilibrium state has dimension $s$ by the Shannon–McMillan–Breiman theorem applied to the potential, and the root equals the Hausdorff dimension by the Bowen formula of *The Hausdorff Dimension of the Julia Sets*. The theorem is the measure-theoretic part of the dimension theory, and it is stated here only for completeness; the thermodynamic formalism is Part III's.

## The Hyperbolic and the Parabolic Cases

**Definition.** A polynomial $f$ is **hyperbolic** if every critical point lies in the basin of an attracting (or superattracting) cycle; it is **parabolic** if it has a rationally indifferent periodic point, so that a cycle of multiplier a root of unity attracts some critical orbit; and it is **subhyperbolic** if every critical orbit either converges to an attracting cycle or is eventually repelled, with no critical orbit in the Julia set.

**Theorem (the expanding characterisation).** A polynomial is hyperbolic if and only if its Julia set is **expanding**: there are constants $C > 0$ and $\rho > 1$ with $|(f^n)'(z)| \geq C\rho^n$ for every $z \in J(f)$ and every $n \geq 1$. Equivalently, a hyperbolic Julia set contains no critical point and the critical orbits stay a positive distance from it.

**Proof sketch.** If the Julia set is expanding then the iterates of a neighbourhood of it are controlled and the critical orbits cannot accumulate on $J$, so they fall into attracting basins, which is hyperbolicity; conversely hyperbolicity makes the critical orbits avoid $J$ and the expanding inequality follows from the compactness of $J$ and the absence of critical points on it. The statement is the Koebe-distortion argument of the doubling theory of *The Geometry of the Julia Sets*.

**Example (the quadratic cases).** For $f_c(z) = z^2+c$ the parameter $c = 0$ gives the superattracting fixed point at $0$ and the Julia set the unit circle; $c = -1$ gives the superattracting period-two cycle $0 \mapsto -1 \mapsto 0$ and the "basilica" Julia set. Both are hyperbolic. The parameter $c = i$ is different: the critical orbit is preperiodic,
$$
0 \mapsto i \mapsto -1+i \mapsto -i \mapsto -1+i,\qquad (f_i^2)'(-i) = 2(-i)\cdot 2(-1+i) = 4+4i ,
$$
of modulus $4\sqrt2 = 5.656854\ldots > 1$, so the critical point lands on a **repelling** two-cycle: $f_i$ is **not hyperbolic**, it is a **Misiurewicz** parameter, and its Julia set is a dendrite, of the tree-like type of *Fractal Trees and Dendrites*. The parameter $c = 1/4$ gives a parabolic fixed point: the point $z = 1/2$ satisfies $f_c(1/2) = 1/2$ and $f_c'(1/2) = 1$, so the multiplier is a root of unity and the critical orbit $0 \mapsto 1/4 \mapsto 5/16 \mapsto \cdots$ converges to $1/2$ without reaching it. The multiplier is exactly $1$ and the Julia set is a **parabolic** one, of the type treated in *The Fatou Components and the Classification of the Dynamics*. The values of the orbit and of the multiplier were recomputed.

## Summary

A complex polynomial of degree $d \geq 2$ is a holomorphic self-map of the Riemann sphere with a superattracting fixed point at $\infty$. Its iterates partition the sphere into the Fatou set, where the family of iterates is normal, and the Julia set, its complement; both are completely invariant, $J(f) = J(f^n)$, and $J(f)$ is nonempty, closed and infinite. The Julia set is the closure of the repelling periodic points, it is contained in the closure of the backward orbit of every non-exceptional point, and it is the common boundary of all the Fatou components and of the filled Julia set. The filled Julia set is compact, and it is connected exactly when every critical point lies in it; for the quadratic family this is the criterion that the parameter lies in the Mandelbrot set.

The Julia set is invariant under the inverse branches of $f$, which are conformal contractions on the repelling side; exact self-similarity holds only in the circle and Chebyshev cases, and the general self-similarity is conformal, recorded by the invariant measure. There is a unique $f$-invariant probability measure of maximal entropy $\log d$, supported on the Julia set; for a hyperbolic Julia set there is an ergodic invariant measure of Hausdorff dimension exactly $\dim_H J(f)$, the equilibrium state of $-s\log|f'|$ at the Bowen value, and the dimension formula expresses it as entropy over Lyapunov exponent.

The dynamics is hyperbolic when every critical point lies in an attracting basin, and then the Julia set is expanding; it is parabolic when a rationally indifferent cycle attracts a critical orbit, the parameter $c = 1/4$ of the quadratic family being the model case. The general theory of the Fatou and Julia sets of a rational map, the classification of the components, the local connectivity and the geometric measure theory belong to *The Geometry of the Julia Sets* of Part IV; the escape criterion and the Green's function are the subject of *The Escape Radius and the Green's Function*, and the dimension is the subject of *The Hausdorff Dimension of the Julia Sets*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $f$, $d$ | Complex polynomial of degree $d \geq 2$, read on $\hat{\mathbb{C}}$ |
| $f^n$ | $n$-th iterate, $f^0 = \mathrm{id}$ |
| $F(f)$, $J(f)$ | Fatou set, Julia set; $J(f) = \hat{\mathbb{C}} \setminus F(f)$ |
| $K(f)$ | Filled Julia set, the points with bounded orbit |
| $A(\infty)$ | Basin of infinity, $\hat{\mathbb{C}} \setminus K(f)$ |
| $\lambda = (f^p)'(z)$ | Multiplier of a $p$-periodic cycle |
| attracting, repelling, indifferent | $|\lambda| < 1$, $|\lambda| > 1$, $|\lambda| = 1$ |
| $\mu$ | Brolin measure, $f$-invariant of maximal entropy $\log d$ |
| $\mu_s$, $s = \dim_H J(f)$ | Equilibrium state of $-s\log|f'|$, measure of full dimension |
| $\chi = \int \log|f'| \, d\mu$ | Lyapunov exponent |
| hyperbolic, parabolic, subhyperbolic | Critical orbits in attracting basins; a rationally indifferent cycle; critical orbits off $J$ |
| $f_c(z) = z^2 + c$ | The quadratic family of *The Mandelbrot Set and the Quadratic Family* |

## Further Reading

- Pierre Fatou, "Sur les équations fonctionnelles", *Bulletin de la Société Mathématique de France* 47 (1919), 161–271; 48 (1920), 33–94 and 208–314, for the original partition into the two sets.
- Gaston Julia, "Mémoire sur l'itération des fonctions rationnelles", *Journal de Mathématiques Pures et Appliquées* 8 (1918), 47–245, for the repelling periodic points and the Julia set.
- Paul Montel, *Leçons sur les familles normales de fonctions analytiques et leurs applications* (Gauthier-Villars, 1927), for the normal families.
- Hans Brolin, "Invariant sets under iteration of rational functions", *Arkiv för Matematik* 6 (1965), 103–144, for the invariant measure.
- John Milnor, *Dynamics in One Complex Variable*, 3rd edition (Princeton University Press, 2006), for the general theory and the quadratic examples.
- Lennart Carleson and Theodore W. Gamelin, *Complex Dynamics* (Springer, 1993), for the polynomial case and the external rays.
- Feliks Przytycki and Mariusz Urbański, *Conformal Fractals: Ergodic Theory Methods* (Cambridge University Press, 2010), for the invariant measures and the dimension formula.
