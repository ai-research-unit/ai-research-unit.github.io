# __The Mandelbrot Set and the Quadratic Family__

## Introduction

Every complex quadratic polynomial is affinely conjugate to exactly one map of the **quadratic family**

$$
f_c(z) = z^2 + c, \qquad c \in \mathbb{C},
$$

so the one-parameter family of the normalised quadratics carries the whole dynamics of degree two. The **Mandelbrot set** is the locus of the parameters whose orbit of the critical point $0$ stays bounded,

$$
M = \{c \in \mathbb{C} : (f_c^n(0))_{n \geq 0} \text{ is bounded}\},
$$

and it is the central object of one-complex-variable parameter theory. This article defines it, proves the equivalent characterisations that give the escape-time algorithm, describes the main cardioid and the period bulbs, and records the standing questions about the boundary. The Julia sets that the parameters generate are the subject of *The Julia Sets of a Complex Polynomial*; the escape criterion and the Green's function used by the algorithm are the subject of *The Escape Radius and the Green's Function*; and the dimension of the boundary is the subject of *The Hausdorff Dimension of the Julia Sets*.

The general theory of the parameter space of a family of rational maps — the bifurcation locus, the stability and the holomorphic motion — belongs to *The Geometry of the Julia Sets* of Part IV, and the theory of the polynomial-like mappings by which the connectedness of $M$ is proved belongs to the same article. Here the quadratic family is worked concretely, with the formulas that the following articles of the subcategory use. No physics is invoked.

## Normalisation of the Quadratic Family

**Theorem.** Every polynomial of degree two has the form $a z^2 + bz + d$ with $a \neq 0$; it is affinely conjugate to a unique map of the family $f_c(z) = z^2+c$.

**Proof.** Write $h(u) = \alpha u + \beta$, so that $h^{-1}(v) = (v-\beta)/\alpha$, and compute

$$
h^{-1}\circ f\circ h\,(u) = a\alpha\, u^2 + (2a\beta + b)\,u + \frac{a\beta^2 + b\beta + d - \beta}{\alpha} .
$$

Choosing $\alpha = 1/a$ kills the leading coefficient and choosing $\beta = -b/(2a)$ kills the linear term, leaving $u^2 + c$ with

$$
c = a\left(a\beta^2 + b\beta + d - \beta\right) = ad - \frac{b^2}{4} + \frac{b}{2} = \frac{4ad - b^2 + 2b}{4} .
$$

So $f$ is conjugate to $f_c$ with $c = ad - b^2/4 + b/2$, the conjugating map being $h(z) = (z - b/2)/a$. The conjugating affine map is unique, because the only affine automorphism of $f_c$ is the identity; the map $f_c$ is even, $f_c(-z) = f_c(z)$, so $z \mapsto -z$ leaves the two sets invariant although it is not a conjugacy of $f_c$ with itself. Affine conjugation carries orbits to orbits, hence preserves boundedness, the Julia set and the filled Julia set up to the conjugacy.

**Corollary.** The Mandelbrot set classifies the degree-two polynomials up to affine conjugacy: the normalised parameter of a quadratic polynomial is a complete invariant of its affine conjugacy class, the conjugacy preserving boundedness, the Julia set and the filled Julia set up to the transport of the conjugating map, and the classification of the parameters into the subsets of $M$ is the classification of the degree-two dynamics.

## The Mandelbrot Set

### Definition and First Properties

**Definition.** The **Mandelbrot set** is

$$
M = \{c \in \mathbb{C} : f_c^n(0) \text{ is bounded as } n \to \infty\} .
$$

Since the finite critical point of $f_c$ is $0$ and $(f_c^n)'(0) = 0$ for $n \geq 1$, the set $M$ is also called the **connectedness locus**.

**Theorem (characterisations).** For $c \in \mathbb{C}$ the following are equivalent:

**(a)** $c \in M$, that is, the critical orbit of $f_c$ is bounded;

**(b)** the filled Julia set $K(f_c)$ is connected;

**(c)** the Julia set $J(f_c)$ is connected;

**(d)** $0 \in K(f_c)$, that is, the critical point does not escape.

**Proof.** (b) $\Leftrightarrow$ (d) is part (e) of the theorem on the boundary of the Fatou components of *The Julia Sets of a Complex Polynomial*: $K$ is connected exactly when every critical point lies in $K$, and the finite critical point of $f_c$ is $0$. (a) $\Leftrightarrow$ (d) is the definition, the orbit of $0$ being bounded exactly when $0 \in K$. (b) $\Leftrightarrow$ (c): $J = \partial K$ and $K$ is full (its complement is the connected basin of $\infty$), so $K$ is connected iff $\partial K = J$ is connected. The equivalence of (a) with the connectedness of the Julia set is the classical dichotomy that gives the escape-time algorithm below, and it is the reason the critical orbit is the only orbit that has to be followed.

### The Escape Criterion and the Algorithm

**Theorem (escape radius).** If $|z| > 2$ and $|z| \geq |c|$ then $|f_c(z)| > |z|$, and $f_c^n(z) \to \infty$; moreover the orbit escapes as soon as it leaves the closed disk of radius $2$, and $M$ is contained in that disk.

**Proof.** $|f_c(z)| = |z^2+c| \geq |z|^2 - |c| \geq |z|^2 - |z| = |z|(|z| - 1) > |z|$ when $|z| > 2$ and $|c| \leq |z|$. Hence the orbit from such a $z$ is increasing in modulus and escapes; in particular if $|c| > 2$ the orbit of $0$ has $|f_c(0)| = |c| > 2$ and escapes, so $M \subseteq \overline{\mathbb{D}}(0,2)$. The full escape-radius statement, with the optimal radius $R(c) = \tfrac12\bigl(1+\sqrt{1+4|c|}\bigr)$, is in *The Escape Radius and the Green's Function*.

**Corollary (escape-time algorithm).** For a parameter $c$ and a bound $N$, iterate $z_{n+1} = z_n^2+c$ from $z_0 = 0$ and stop at the first $n$ with $|z_n| > 2$. If no such $n \leq N$ occurs, declare $c$ a candidate member of $M$. The algorithm is exact for the points that escape before the bound and approximate for the rest; the escape time $n(c)$ is the number of steps to leave the disk of radius $2$.

**Example (the algorithm on the integer lattice).** Running the algorithm with the bound $N = 500$ and the escape radius $2$ on the integer lattice of $[-3,3) \times [-3,3)$ gives the bounded points

$$
(0,0),\ (-1,0),\ (-2,0),\ (0,\pm1),
$$

that is, $c = 0, -1, -2, i, -i$; every other lattice point escapes. The computation reproduces the known facts: $0, -1, -2$ lie in $M \cap \mathbb{R}$ and $i, -i$ lie on the imaginary axis in $M$. The escape times at $c = 1, 2, 3$ are $3, 2, 1$, since $0 \mapsto 1 \mapsto 2 \mapsto 5$, $0 \mapsto 2 \mapsto 6$, $0 \mapsto 3$ and $|3| > 2$.

### The Real Slice

**Theorem.** The intersection of $M$ with the real axis is exactly the interval $[-2, 1/4]$:

$$
M \cap \mathbb{R} = [-2, 1/4].
$$

**Proof sketch.** For real $c$ the dynamics of $f_c$ on $\mathbb{R}$ is that of the real quadratic family, and the critical orbit is bounded exactly for $-2 \leq c \leq 1/4$: the interval $[-1/2, 1/2]$ is invariant for $-2 \leq c \leq 1/4$ and traps the critical orbit, while for $c < -2$ the orbit starts with $0 \mapsto c$ and then increases in modulus, and for $c > 1/4$ every orbit escapes. The detailed real dynamics is the subject of the real quadratic family, and the comparison of the real and the complex families is recorded there. The two endpoints are: $c = 1/4$, the parabolic cusp; $c = -2$, the tip, whose Julia set is the segment $[-2,2]$.

**Remark.** The interval $[-2, 1/4]$ is the whole of the real slice, and the values $-3/4$ and $-5/4$ in it, at which the multiplier of the attracting cycle is $-1$, are the first two **period-doubling** parameters. At $c = -3/4$ the fixed point $z = -1/2$ has multiplier $2z = -1$, and at $c = -5/4$ the period-two cycle has multiplier $4(c+1) = -1$; the real period-doubling cascade accumulates at the Feigenbaum parameter, whose constant is not recomputed here and is quoted in the literature.

## The Hyperbolic Components

### The Main Cardioid

**Definition.** The **main cardioid** of $M$ is the set

$$
\mathcal{C} = \left\{ c = \frac{\mu}{2} - \frac{\mu^2}{4} : |\mu| < 1 \right\} ,
$$

a cardioid-shaped open region with cusp at $c = 1/4$ and the point $c = -3/4$ on its boundary.

**Theorem.** The main cardioid is the set of parameters for which $f_c$ has an attracting fixed point. The fixed point is $z = \mu/2$, its multiplier is $\mu = 2z$, and the map $\mu \mapsto c = \mu/2 - \mu^2/4$ is a bijection of the unit disk onto $\mathcal{C}$.

**Proof.** A fixed point satisfies $z^2+c = z$, so $c = z - z^2$, and its multiplier is $f_c'(z) = 2z$. Setting $\mu = 2z$ gives $c = \mu/2 - \mu^2/4$; the fixed point is attracting exactly when $|\mu| < 1$, and the assignment $z \mapsto 2z$ is a bijection of the disk of fixed points onto the unit disk. The boundary values are $\mu = 1$, giving $c = 1/4$ (the parabolic cusp) and $\mu = -1$, giving $c = -3/4$ (the period-doubling point).

**Example.** The centre $c = 0$ has $\mu = 0$, a superattracting fixed point at $0$ and the Julia set the unit circle; the parameter $c = 1/4$ is the cusp, with the parabolic fixed point $z = 1/2$ of multiplier $1$.

### The Period-Two Bulb

**Theorem.** The period-two cycle of $f_c$ exists for every $c$ and consists of the two roots of

$$
z^2 + z + c + 1 = 0 ,
$$

whose product is $c+1$; its multiplier is

$$
\lambda_2(c) = 4(c+1).
$$

The parameters for which the period-two cycle is attracting are the open disk $|c+1| < 1/4$, a **period-two bulb** attached to the main cardioid at the point $c = -3/4$ and centred at the superattracting parameter $c = -1$.

**Proof.** The equation $f_c^2(z) = z$ factors as $(z^2 - z + c)(z^2+z+c+1) = 0$; the first factor gives the fixed points, and the second gives the period-two points, with sum $-1$ and product $c+1$. The multiplier of the two-cycle is the product of the two derivatives,

$$
(f_c^2)'(z_1) = (2z_1)(2z_2) = 4z_1z_2 = 4(c+1),
$$

which is independent of which of the two roots is chosen. The cycle is attracting exactly when $|4(c+1)| < 1$, that is $|c+1| < 1/4$; the multiplier is $1$ at $c = -3/4$ and $0$ at $c = -1$.

**Example.** At $c = -1$ the cycle is $\{0, -1\}$ and the parameter is superattracting; at $c = -5/4$ the multiplier is $-1$, the left-hand endpoint of the bulb, where the cycle becomes parabolic and a period-four cycle is born.

### Hyperbolic Components and Their Classification

**Definition.** A **hyperbolic component** of $M$ is a connected component of the interior of $M$; it is **of period $p$** if the corresponding map $f_c$ has an attracting cycle of exact period $p$.

**Theorem (the multiplier map).** Let $H$ be a hyperbolic component of period $p$. The **multiplier map** $\lambda : H \to \mathbb{D}$, sending $c$ to the multiplier of the attracting cycle of period $p$, is a biholomorphism onto the unit disk; in particular $H$ contains exactly one parameter at which the cycle is superattracting, the **centre**, and exactly one parameter of each multiplier, and the closure of $H$ meets the rest of $M$ in finitely many points, the **roots**, at which the cycle is parabolic with multiplier a root of unity.

**Proof sketch.** The attracting cycle depends holomorphically on $c$ by the implicit function theorem, so $\lambda$ is holomorphic; it is a proper map onto the disk, because a cycle that reaches $|\lambda| = 1$ is no longer attracting and the component is left. The properness and the normality of the family give that $\lambda$ is a finite covering of the disk; the argument principle applied to the cycle of period $p$ shows that the covering is of degree one, hence a biholomorphism. The details are the theory of the multiplier and the hyperbolic components of *The Geometry of the Julia Sets*.

**Theorem.** The interior of $M$ is exactly the union of the hyperbolic components: a parameter lies in $\mathring M$ if and only if $f_c$ has an attracting cycle.

**Proof sketch.** If $c \in \mathring M$ then the critical point $0$ does not escape and the family is stable near $c$; the stability implies that the critical point cannot be in the Julia set, by the $\lambda$-lemma, and the classification of *The Fatou Components and the Classification of the Dynamics* then places the critical orbit in an attracting basin, so $f_c$ is hyperbolic. Conversely, an attracting cycle persists under small perturbations, so a neighbourhood of $c$ is in $M$. The theorem is Douady–Hubbard's; the full proof is Part IV's.

**Remark.** The main cardioid is the hyperbolic component of period one, and the period-two bulb is the component of period two attached to it at $c = -3/4$. The remaining hyperbolic components are the period bulbs, attached to the main cardioid and to one another at their roots; the values of the multiplier at the root determine the **bifurcation** by which the daughter component is attached.

## The Boundary and the Standing Questions

### The Antenna

**Definition.** The **antenna** is the part of $\partial M$ on the real axis, that is, the compact subset $\partial M \cap [-2, 1/4]$.

**Theorem.** The antenna is

$$
\partial M \cap \mathbb{R} = \partial M \cap [-2, 1/4],
$$

and it contains the period-doubling parameters $-3/4, -5/4, \ldots$ together with their accumulation point, the **Feigenbaum parameter** $c_\infty \in (-1.41, -1.40)$, at which the attracting cycles of period $2^n$ accumulate. The antenna is a Cantor-like subset of the interval, and the hyperbolic components of $M$ that meet the real axis are dense in $[-2, 1/4]$.

**Proof sketch.** The real period-doubling cascade and the density of hyperbolicity in the real quadratic family are theorems of the real dynamics; the values of the period-doubling parameters are the roots of the equations $\lambda_{2^n}(c) = -1$, and $-3/4$ and $-5/4$ are their first two. The number $c_\infty$ is defined as the limit; no numerical value of the Feigenbaum constants is asserted here.

### The Boundary

**Theorem (Shishikura).** The Hausdorff dimension of the boundary of the Mandelbrot set is $2$:

$$
\dim_H \partial M = 2,
$$

and for every parameter $c$ on the boundary of $M$ the Hausdorff dimension of the Julia set $J(f_c)$ is also $2$.

**Proof sketch.** Shishikura's theorem is proved by a surgery construction that produces, near a parameter of the boundary, polynomial-like maps whose Julia sets contain quasi-self-similar circles of arbitrarily small diameter; the covering estimates then force the dimension to be the ambient two. The result is quoted here and developed in *The Hausdorff Dimension of the Julia Sets*, where the dimension is related to the Bowen equation; the definition of the Hausdorff dimension is the lead article *Fractal Geometry* of Part IV.

**Remark (the standing question).** Whether $\partial M$ is **locally connected** is the **MLC conjecture**, open since the 1980s; the conjecture is equivalent, by the theory of external rays, to the landing of every external ray of $M$, and it is one of the reasons the study of $M$ is a source of problems rather than a closed subject. The connectedness of $M$ and the simplicity of the complement $\hat{\mathbb{C}} \setminus M$, which is conformally isomorphic to the complement of the closed unit disk, are theorems of Douady and Hubbard and are proved by the theory of polynomial-like mappings in *The Geometry of the Julia Sets*.

## Summary

Every complex quadratic polynomial is affinely conjugate to a unique $f_c(z) = z^2+c$, so the quadratic family is the one-parameter family of the degree-two dynamics. The Mandelbrot set is the locus of parameters whose critical orbit is bounded; equivalently it is the connectedness locus where the filled Julia set, and hence the Julia set, of $f_c$ is connected. The escape criterion in the disk of radius $2$ gives the escape-time algorithm, which computes $M$ outward from the critical point; the algorithm decides membership exactly for the escaping parameters and approximately otherwise.

The Mandelbrot set is contained in the closed disk of radius $2$, its real slice is $[-2, 1/4]$, and its interior is the union of the hyperbolic components: the main cardioid, where there is an attracting fixed point, parameterised by $c = \mu/2 - \mu^2/4$, and the period bulbs, beginning with the period-two bulb $|c+1| < 1/4$ attached at $c = -3/4$. On each hyperbolic component the multiplier map is a biholomorphism onto the unit disk, so the component carries a distinguished centre and finitely many roots. The boundary of $M$ has Hausdorff dimension $2$, and the Julia set of every parameter on it has dimension $2$; whether the boundary is locally connected is the open MLC conjecture. The connectedness of $M$ and the theory of polynomial-like mappings are Part IV's, and the dimension of the boundary is that of *The Hausdorff Dimension of the Julia Sets*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $f_c(z) = z^2+c$ | The quadratic family |
| $M$ | Mandelbrot set, the connectedness locus of $f_c$ |
| $K(f_c)$, $J(f_c)$ | Filled Julia set and Julia set of the parameter $c$ |
| $n(c)$ | Escape time, the first $n$ with $\lvert f_c^n(0)\rvert > 2$ |
| $R(c) = \tfrac12(1+\sqrt{1+4\lvert c\rvert})$ | Optimal escape radius, quoted from *The Escape Radius and the Green's Function* |
| $\mathcal{C}$, $\mu$ | Main cardioid and the multiplier of its fixed point, $c = \mu/2-\mu^2/4$ |
| $\lambda_2(c) = 4(c+1)$ | Multiplier of the period-two cycle |
| hyperbolic component, centre, root | Component of $\mathring M$; its superattracting parameter; the parabolic parameters on its boundary |
| $\lambda : H \to \mathbb{D}$ | Multiplier map, a biholomorphism |
| $\partial M$, antenna | Boundary of $M$; the part $\partial M \cap \mathbb{R}$ |
| $c_\infty$ | Feigenbaum accumulation parameter of the period-doubling cascade |

## Further Reading

- Benoit B. Mandelbrot, "On the quadratic mapping $z \mapsto z^2-\mu$ for complex $\mu$ and $z$: the fractal structure of its $M$ set and scaling", *Physica D* 7 (1983), 224–239, for the first pictures and the name.
- Adrien Douady and John H. Hubbard, "Itération des polynômes quadratiques complexes", *Comptes Rendus de l'Académie des Sciences de Paris* 294 (1982), 123–126, and "Étude dynamique des polynômes complexes", *Publications Mathématiques d'Orsay* (1984–85), for the connectedness of $M$ and the multiplier theory.
- John Milnor, *Dynamics in One Complex Variable*, 3rd edition (Princeton University Press, 2006), for the hyperbolic components, the cardioid and the bulbs.
- Mitsuhiro Shishikura, "The Hausdorff dimension of the boundary of the Mandelbrot set and Julia sets", *Annals of Mathematics* 147 (1998), 225–267, for $\dim_H \partial M = 2$.
- Curtis T. McMullen, *Complex Dynamics and Renormalization* (Princeton University Press, 1994), for the renormalisation and the structure of the boundary.
- Mitchell J. Feigenbaum, "Quantitative universality for a class of nonlinear transformations", *Journal of Statistical Physics* 19 (1978), 25–52, for the period-doubling constants quoted but not recomputed here.
