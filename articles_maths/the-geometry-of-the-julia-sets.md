# __The Geometry of the Julia Sets__

## Introduction

Let $R : \hat{\mathbb{C}} \to \hat{\mathbb{C}}$ be a rational map of degree $d \geq 2$ of the Riemann sphere. The iterates of $R$ partition the sphere into the **Fatou set** $F(R)$, the set on which the family $\{R^n\}$ is equicontinuous, and the **Julia set** $J(R) = \hat{\mathbb{C}} \setminus F(R)$, the set on which the dynamics is chaotic. The Julia set is compact, perfect, uncountable, completely invariant, and equal to the closure of the repelling periodic points; it is the boundary of every Fatou component, and for a polynomial it is the boundary of the filled Julia set. The Julia sets are the standard fractals of the plane: the circle for $z \mapsto z^d$, the segment $[-2,2]$ for $z \mapsto z^2 - 2$, the basilica, the rabbit, the dendrite and the Cantor sets of the parameters outside the Mandelbrot set.

This article is the **geometry** of these sets and of their parameter space. It states the Fatou–Julia partition for a rational map, the local connectivity of a connected filled Julia set together with the Carathéodory criterion, the **Böttcher coordinate**, the **external rays** and the **landing theorem** of Douady and Hubbard, the **Mandelbrot set** as parameter space with its connectedness — proved by the theory of polynomial-like mappings — its external rays and the open local-connectivity question, and the **dimension and the measure** of a Julia set in the hyperbolic and the parabolic cases. The tree-like and dendrite-like Julia sets are the examples of *Fractal Trees and Dendrites*, and the dimension used throughout is that of the lead article *Fractal Geometry*.

The scope is fixed by the corpus's split. The **dynamics** of the map — the partition as a topological system, the bifurcations, the ergodic theory and the pressure — is that of Part III, cited to *Topological Dynamics*, *Smooth Dynamical Systems* and *Ergodic Theory*, and the invariant measure is constructed there and in *Fractal Analysis*'s *The Self-Similar Measure and the Invariant Measure*. The **polynomial instance** — the partition for polynomials, the repelling periodic points, the filled Julia set, the invariance and the existence of the invariant measure — is that of *The Julia Sets of a Complex Polynomial*, the classification of the Fatou components is that of *The Fatou Components and the Classification of the Dynamics*, and the explicit quadratic formulas are those of *The Mandelbrot Set and the Quadratic Family*; all three are in the complex-number part of the corpus and are cited, not repeated. The **dimension computations for polynomials** — the two exact cases of the circle and the segment, the Bowen equation for hyperbolic parameters, the real-analyticity of Ruelle and the theorem of Shishikura — are the subject of *The Hausdorff Dimension of the Julia Sets*, and only the general rational statements are made here. The limit space of the **iterated monodromy group** of a subhyperbolic map is treated in *Limit Spaces and Schreier Graphs*.

The article assumes *Complex Analysis* for the normal families and Montel's theorem, the Riemann mapping theorem, the Carathéodory extension theorem, the holomorphic motions and the Böttcher construction; *Topological Spaces* for compactness, connectedness, local connectedness and the continua; *Metric Geometry* for the distance and the Lipschitz conditions; and *Fractal Geometry* for the covering numbers, the Hausdorff content and the dimension. No physics is invoked.

## The Fatou and Julia Sets

**Definition.** For a rational map $R$ of degree $d \geq 2$, a point $z$ belongs to the **Fatou set** $F(R)$ when there is a neighbourhood $U$ of $z$ on which the family $\{R^n\}$ of iterates is normal in the sense of *Complex Analysis*, that is, equicontinuous with respect to the spherical metric; the **Julia set** is the complement $J(R)$.

**Theorem (the Fatou–Julia properties).** For a rational map of degree $d \geq 2$:

**(a)** $F(R)$ is open and completely invariant, $R(F) = F$ and $R^{-1}(F) = F$, and $J(R)$ is compact, nonempty, perfect, uncountable and completely invariant;

**(b)** $J(R) = \overline{\{\text{repelling periodic points}\}}$, and the preimages of any point of $J(R)$ are dense in $J(R)$;

**(c)** $J(R)$ is the boundary of every Fatou component, and $J(R^n) = J(R)$ for every $n \geq 1$;

**(d)** a point of $J(R)$ has no neighbourhood on which the iterates are uniformly bounded; if in addition $R$ is **hyperbolic**, meaning every critical point is attracted to an attracting cycle, then there are $C > 0$ and $\lambda > 1$ with $|(R^n)'(z)| \geq C \lambda^n$ for every $z \in J(R)$ and every $n$.

**Proof sketch.** (a) normality is a local property, so $F$ is open, and it is preserved by $R$ and by the branches of $R^{-1}$ because postcomposition and precomposition with a holomorphic map preserve normality. (b) is the theorem of Fatou and Julia: the repelling periodic points exist by the theory of the multiplier and the fixed-point formula, they lie in $J$ because the derivative grows, and their closure is forward and backward invariant; the complementary open set carries a normal family and is contained in $F$ by Montel's theorem. (c) the invariance of (a) makes the boundary of a Fatou component invariant and contained in $J$, and every point of $J$ is a limit of points whose orbits have different behaviour, hence of boundaries. (d) a neighbourhood with bounded iterates is normal; for a hyperbolic map the spherical derivative of $R^n$ grows exponentially on $J$ because the postcritical set stays away from $J$, which is a compact set carrying a repelling metric (the arguments of *Complex Analysis* and *Smooth Dynamical Systems*).

**Example (the elementary Julia sets).** For $R(z) = z^d$ the Fatou set is the unit disk and its exterior and $J$ is the unit circle, of dimension and topological dimension one. For $R(z) = z^2 - 2$ the Chebyshev conjugacy $w + w^{-1}$ identifies $R$ with $w \mapsto w^2$ and $J = [-2,2]$, a segment. For $R(z) = z^2 - 1$ the critical orbit $0 \mapsto -1 \mapsto 0$ is a superattracting cycle, the map is hyperbolic, and $J$ is the **basilica**, a Cantor set of circles. For $R(z) = z^2 + i$ the critical orbit is preperiodic to a repelling cycle, $J$ is a dendrite, and the topological structure is that of *Fractal Trees and Dendrites*. These four cases are the ones the article uses as computations, and the general polynomial theory is that of *The Julia Sets of a Complex Polynomial*.

**Remark (the two readings of the same set).** The Julia set is simultaneously a dynamical object and a metric object. As a dynamical object it is the repeller of $R$, with the shift coding of *Symbolic Dynamics* and the invariant measure of *Ergodic Theory*; as a metric object it is a compact subset of the sphere with a Hausdorff dimension, a local connectedness question and an external geometry. This article is the second reading; the first belongs to Part III.

## Local Connectivity and the Connected Filled Julia Set

**Definition (the filled Julia set).** For a polynomial $P$ of degree $d \geq 2$, the **filled Julia set** is $K(P) = \{z : \{P^n(z)\}$ is bounded$\}$, a compact set with $J(P) = \partial K(P)$, and the **basin of infinity** is the Fatou component $A(\infty) = \mathbb{C} \setminus K(P)$, which is simply connected exactly when $K(P)$ is connected.

**Theorem (connectedness and local connectivity).** Let $P$ be a polynomial of degree $d \geq 2$.

**(a)** $K(P)$ is connected if and only if the orbit of the critical point is bounded.

**(b)** $J(P)$ is locally connected if and only if the conformal map from the exterior of the disk onto $A(\infty)$ extends continuously to the boundary; when this holds, the boundary circle maps continuously onto $J(P)$ and $J(P)$ is a quotient of the circle.

**(c)** If $P$ is hyperbolic then $J(P)$ is locally connected.

**Proof sketch.** (a) is the theorem of Douady–Hubbard for the polynomial-like restriction of $P$ to a neighbourhood of $K(P)$: the map is a polynomial-like map of degree $d$, its filled Julia set is connected exactly when all the critical points lie in the domain of definition of the straightening, and the critical points are the $d-1$ preimages of the critical point, so the criterion is the boundedness of the critical orbit. (b) is the Carathéodory extension theorem applied to the conformal isomorphism $\mathbb{C} \setminus \overline{\mathbb{D}} \to A(\infty)$: the inverse extends continuously to the boundary circle exactly when the boundary of $A(\infty)$, which is $J(P)$, is locally connected, and the extension is then a continuous surjection of the circle. (c) for a hyperbolic polynomial the Julia set carries the repelling metric of the previous section, and the expansion gives the local connectedness by the theorem of Douady–Hubbard; the case of a rational map is subtler and there are non-locally-connected Julia sets, so the hyperbolicity is not removable.

**Remark (why local connectivity is the combinatorial question).** A connected and locally connected Julia set is a **topological model** of the polynomial: it is the quotient of the circle by the equivalence that identifies the angles landing at the same point, and the equivalence is described by the kneading data. Without local connectivity the external rays still land at the rational angles, by the theorem below, but the coding is only measurable and not continuous. The open question of whether the Mandelbrot set is locally connected, stated below, is the same question for the parameter space.

## The Böttcher Coordinate and the External Rays

**Theorem (Böttcher).** Let $P$ be a monic polynomial of degree $d \geq 2$. There is a conformal map $\varphi$ of a neighbourhood of $\infty$ onto a neighbourhood of $\infty$ with

$$
\varphi(P(z)) = \varphi(z)^d, \qquad \varphi(z) = z + O(1)
$$

near infinity, unique up to multiplication by a $(d-1)$-th root of unity. The function $G = \log|\varphi|$ extends to a continuous **Green's function** $G : \mathbb{C} \to [0,\infty)$ that is harmonic on $A(\infty)$, vanishes exactly on $K(P)$, and satisfies $G(P(z)) = d\,G(z)$.

**Definition (equipotentials and external rays).** For $t > 0$ the **equipotential** is the level set $\{G = t\}$, a Jordan curve for $t$ small; the **external ray** of angle $\theta$ is

$$
\gamma_\theta = \{z \in A(\infty) : G(z) > 0, \ \arg \varphi(z) = 2\pi\theta\} ,
$$

and the ray **lands** at the limit $\lim_{t \to 0^+} \gamma_\theta(t)$, where $\gamma_\theta(t)$ is the point of the ray with $G = t$, when the limit exists.

**Theorem (the landing theorem).** Let $P$ be a polynomial of degree $d \geq 2$ with connected filled Julia set.

**(a)** For every rational $\theta \in \mathbb{Q}/\mathbb{Z}$ the external ray $\gamma_\theta$ lands at a point of $J(P)$.

**(b)** If $J(P)$ is locally connected then every ray lands, the map $\theta \mapsto \lim_{t\to0}\gamma_\theta(t)$ is continuous from the circle onto $J(P)$, and the landing angles of a point form a finite set.

**(c)** The map of (b) semiconjugates the doubling map $\theta \mapsto d\theta$ on the circle to $P$ on $J(P)$.

**Proof sketch.** (a) is the theorem of Douady and Hubbard: a rational ray cannot accumulate on a continuum of points of $J$ without crossing the equipotentials, and the landing angle is constrained by the critical orbits; the argument uses the count of the rays in each annulus and the theory of the polynomial-like restrictions. (b) the continuous extension is the Carathéodory criterion of the previous section, and the local connectedness makes the extension onto $J$ a quotient map; the landing angles are finite because the equivalence is semiconjugate to the doubling map. (c) the identity $\varphi(P(z)) = \varphi(z)^d$ says that $P$ sends the ray of angle $\theta$ to the ray of angle $d\theta$, and the landing points respect the identification.

**Example (the ray landings, computed).** For $z \mapsto z^2$ one has $\varphi(z) = z$ and the ray of angle $\theta$ is the radial line, landing at $e^{2\pi i\theta}$. For $z \mapsto z^2 - 2$ the Chebyshev conjugacy $z = w + w^{-1}$ gives $\varphi(z) = w$ for the branch at infinity, so the ray of angle $\theta$ lands at

$$
z(\theta) = 2\cos(2\pi\theta) .
$$

At the low periods this is $z(0) = 2$, the repelling fixed point; $z(1/2) = -2$, the preimage of $2$; $z(1/3) = z(2/3) = -1$, the other fixed point, at which two rays land; $z(1/4) = 0$, the preimage of $-2$; and $z(1/6) = 1$, which maps to $-1$. The computation reproduces the fixed points and the preperiodic points of the polynomial, so the landing theorem is visible at the first levels.

## The Mandelbrot Set as a Parameter Space

**Definition.** The **Mandelbrot set** is $M = \{c \in \mathbb{C} : \text{the orbit of } 0 \text{ under } z \mapsto z^2+c \text{ is bounded}\}$, the **connectedness locus** of the quadratic family.

**Theorem (Douady–Hubbard).** **(a)** $M$ is compact and connected, and its complement is conformally isomorphic to the complement of the closed unit disk; the isomorphism sends $M$ to the disk and is normalised at infinity. **(b)** $c \in M$ if and only if $J_c$ is connected; for $c \notin M$ the Julia set is a Cantor set. **(c)** The interior of $M$ is the set of hyperbolic parameters, whose maps have an attracting cycle, and the **bifurcation locus** — the parameters where the dynamics is not stable under perturbation — is the boundary $\partial M$.

**Proof sketch.** (a) the critical point $0$ is the only critical point and the map $c \mapsto \varphi_c(c)$ (the value at the critical point of the Böttcher coordinate of the polynomial, defined for $c \notin M$) is the conformal isomorphism of the complement; the theory of the polynomial-like mappings shows that it extends to a homeomorphism and that $M$ is connected, the proof being the one indicated in *The Mandelbrot Set and the Quadratic Family*. (b) the connectedness of $K_c$ is the critical-orbit criterion of the previous section, and the alternative is the Cantor case. (c) the attracting cycle exists exactly for the interior parameters by the theorem of Douady–Hubbard, and the stability fails exactly on the boundary by the definition of the bifurcation locus, which is the subject of *The Fatou Components and the Classification of the Dynamics*.

**Definition (parameter rays and the combinatorial model).** The **parameter ray** of angle $\theta$ is the image under the conformal isomorphism of the radial line of angle $\theta$ in the complement of the disk, and it **lands** at a point of $\partial M$ when the image extends to the boundary point.

**Theorem (the parameter rays).** For every rational $\theta$ the parameter ray of angle $\theta$ lands at a point of $\partial M$. The rays of angles $0$ and $1/2$ land at $c = 1/4$ and $c = -2$; the rays of angles $1/3$ and $2/3$ land at $c = -3/4$, the root of the period-two component; and the rays of angles $1/7$ and $2/7$ land at the root of the period-three **rabbit** component. The set of the landing angles of a point of $\partial M$ is finite and the landing is the combinatorial model of the boundary.

**Proof sketch.** The landing of the rational rays is the theorem of Douady and Hubbard for the parameter plane, the analogue of the landing theorem above with the critical orbit replaced by the critical value; the explicit angles are the characteristic angles of the hyperbolic components, computed from the multiplier: the period-two component has multiplier $-1$ at its root $c = -3/4$, and the two rays bounding the component land there. The finiteness of the landing angles is the combinatorial statement of the model. The local connectivity of $\partial M$ is **open**: it is the **MLC conjecture**, and it is equivalent to the landing of every parameter ray, rational or not, with the continuity of the landing.

**Remark (the dimension of the boundary).** The boundary $\partial M$ has Hausdorff dimension two, and for a generic $c \in \partial M$ the Julia set $J_c$ also has Hausdorff dimension two; this is the theorem of Shishikura, quoted here and stated with its polygonal approximation in *The Hausdorff Dimension of the Julia Sets*. The result shows that the metric complexity of the parameter space is as large as the plane: the boundary of $M$ is a fractal of maximal dimension, although it is not known whether it is locally connected.

**Remark (the iterated monodromy group).** For a subhyperbolic rational map the **iterated monodromy group** is contracting and its limit space is homeomorphic to the Julia set; this is the theorem of Nekrashevych, stated in *Limit Spaces and Schreier Graphs*, where the group, the action on the tree and the Schreier graphs are constructed. The two objects — the limit space of the group and the Julia set of the map — are the same fractal through two constructions, the group-theoretic one and the dynamical one, and the dimension is the invariant they share.

## The Dimension and the Measure of a Julia Set

**Theorem (the general dimension).** Let $R$ be a rational map of degree $d \geq 2$.

**(a)** $J(R)$ is a compact subset of the sphere and $0 \leq \dim_H J(R) \leq 2$; if $J(R)$ is connected and not a point then $\dim_H J(R) \geq 1$.

**(b)** If $R$ is hyperbolic, with the expansion $|(R^n)'| \geq C\lambda^n$ on $J$, then $\dim_H J = \dim_B J = s$, where $s$ is the unique root of the **Bowen equation** $P(-s\log|R'|) = 0$; the pressure is that of *Ergodic Theory*.

**(c)** If $R$ is parabolic, with a parabolic cycle of multiplier a root of unity, the expansion fails at the cycle and the Bowen equation must be modified; the dimension is still bounded below by one when $J$ is connected, and the parabolic parameters are the delicate boundary points of the hyperbolic components.

**(d)** The measure of maximal entropy of $R$ has dimension $\log d/\chi$, where $\chi$ is its Lyapunov exponent; this is at most $\dim_H J$, with equality exactly for the exceptional maps whose Julia set is a circle ($z \mapsto z^d$ and its conjugates) or the whole sphere (the Lattès maps).

**Proof sketch.** (a) a subset of the sphere has dimension at most two, and a connected set containing an arc has dimension at least one. (b) for a hyperbolic map the pressure function $t \mapsto P(-t\log|R'|)$ is strictly decreasing from $P(0) = \log d > 0$ to $-\infty$, so it has a unique root; the root is the dimension by the Bowen–Ruelle theorem for conformal repellers, and the box and Hausdorff dimensions agree for the expanding map. (c) at a parabolic cycle the derivative tends to one along the cycle, the potential $-\log|R'|$ is not bounded below by a positive constant, and the root of the pressure is replaced by the dimension of the repeller with the parabolic point removed; the arguments are those of *Ergodic Theory* and *The Hausdorff Dimension of the Julia Sets*. (d) is the theorem of Manning and Zdunik: the entropy is $\log d$, the Lyapunov exponent is $\chi$, the dimension of the measure is $\log d/\chi$ by the Shannon–McMillan–Breiman theorem, and it is strictly smaller than the dimension of the set unless the measure is the area, which forces the exceptional cases.

**Remark (what is quoted and what is computed).** The exact cases for the quadratic family are the circle at $c = 0$ and the segment at $c = -2$, both of dimension one; the Bowen equation is the instrument for the hyperbolic parameters; the real-analyticity of the dimension on a hyperbolic component is the theorem of Ruelle; and the dimension two on the boundary is the theorem of Shishikura. All of these are computed or stated in *The Hausdorff Dimension of the Julia Sets*, and the article here states only the general rational form of the statements and the parabolic caveat. For the **parabolic** parameter $c = 1/4$ the Julia set is connected and its dimension is strictly between one and two; the exact dimension is not given by the Bowen equation, and the numerical value is computed in *The Hausdorff Dimension of the Julia Sets*. The **multifractal** refinement of the dimension — the spectrum of the local exponents of the invariant measure — is the subject of *Multifractal Analysis and the Legendre Transform*.

## Summary

For a rational map of degree at least two the sphere splits into the Fatou set, where the iterates are equicontinuous, and the Julia set, which is compact, perfect, uncountable, completely invariant, the closure of the repelling periodic points and the boundary of every Fatou component. The Julia set is the standard fractal of the plane: a circle, a segment, a basilica, a dendrite or a Cantor set according to the parameter. The connected filled Julia set has a Böttcher coordinate at infinity, a Green's function and an external ray for every angle; the rational rays land at the points of the Julia set, and the local connectivity of the Julia set is exactly the continuity of the landing from the circle. The Mandelbrot set is compact and connected, its complement is conformally the complement of the disk, its interior is the hyperbolic parameters, its boundary is the bifurcation locus and carries the parameter rays, and the local connectivity of that boundary is the open MLC conjecture. The dimension of a hyperbolic Julia set is the root of the Bowen equation and the dimension of the maximal-entropy measure is $\log d/\chi \leq \dim_H J$; the parabolic case is the delicate one and the boundary of the Mandelbrot set has dimension two by the theorem of Shishikura. The dynamics and the ergodic theory belong to Part III, the polynomial instance and the classification of the Fatou components to the complex articles of the corpus, the dimension computations to *The Hausdorff Dimension of the Julia Sets*, and the limit space of the iterated monodromy group to *Limit Spaces and Schreier Graphs*; the topological shape of the tree-like cases is that of *Fractal Trees and Dendrites*, and the dimension used throughout is that of the lead article *Fractal Geometry*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $d$, $F(R)$, $J(R)$ | Rational map of degree $d \geq 2$; Fatou set; Julia set |
| $P$, $K(P)$, $A(\infty)$ | Polynomial; filled Julia set, $J(P)=\partial K(P)$; basin of infinity |
| $\varphi$, $G$ | Böttcher coordinate; Green's function $\log\lvert\varphi\rvert$ |
| $\gamma_\theta$, landing | External ray of angle $\theta$; the limit at $G\to0$ |
| $2\cos(2\pi\theta)$ | Landing point of the ray of $z\mapsto z^2-2$ |
| $M$, $\partial M$, MLC | Mandelbrot set; its boundary; the local-connectivity conjecture |
| Hyperbolic, parabolic | All critical points attracted; a periodic cycle of multiplier a root of unity |
| $P(-s\log\lvert R'\rvert)=0$ | Bowen equation for the dimension of a hyperbolic Julia set |
| $\log d/\chi$ | Dimension of the measure of maximal entropy; $\chi$ its Lyapunov exponent |
| $\dim_H$, $\dim_B$ | Hausdorff and box dimensions, as in *Fractal Geometry* |

## Further Reading

- John Milnor, *Dynamics in One Complex Variable* (Princeton University Press, 3rd edition, 2006), for the Fatou–Julia theory, the external rays and the landing theorems.
- Lennart Carleson and Theodore W. Gamelin, *Complex Dynamics* (Springer, 1993), for the polynomial-like mappings, the Mandelbrot set and the dimension theory.
- Adrien Douady and John H. Hubbard, "Étude dynamique des polynômes complexes", *Publications Mathématiques d'Orsay* 84-02 and 85-04 (1984–1985), for the Böttcher coordinate, the landing theorem and the connectedness of the Mandelbrot set.
- Curtis T. McMullen, *Complex Dynamics and Renormalization* (Princeton University Press, 1994), for the local connectivity, the rigidity and the parameter theory.
- Mitsuhiro Shishikura, "The Hausdorff dimension of the boundary of the Mandelbrot set and Julia sets", *Annals of Mathematics* 147 (1998), 225–267, for the dimension two results.
- Feliks Przytycki and Mariusz Urbański, *Conformal Fractals: Ergodic Theory Methods* (Cambridge University Press, 2010), for the Bowen equation, the pressure and the dimension of the invariant measures.
- Mariusz Urbański and Anna Zdunik, "Real analyticity of Hausdorff dimension of Julia sets", *Ergodic Theory and Dynamical Systems* 10 (1990), 605–631, for the analytic dependence of the dimension.
- Volodymyr Nekrashevych, *Self-Similar Groups* (American Mathematical Society, 2005), for the iterated monodromy groups and their limit spaces.
