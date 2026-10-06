# __The Hausdorff Dimension of the Julia Sets__

## Introduction

The Julia set of a polynomial of degree $d \geq 2$ is a compact subset of the plane, and its **Hausdorff dimension** is the exponent that measures how much of the plane it occupies. This article states the general bounds, computes the two exactly known cases of the quadratic family — the circle and the segment — and records the formula that determines the dimension when the Julia set is hyperbolic: the **Bowen equation**, the unique root of the pressure equation. It then states the real-analyticity of the dimension in the parameter and the theorem of Shishikura that the dimension is two on the boundary of the Mandelbrot set. The definition of the Hausdorff dimension, its basic properties and its relation to the box dimension are those of *Fractal Geometry*, the lead article of the subcategory; the dimension of the measure and the thermodynamic formalism are those of *Ergodic Theory* and *The Julia Sets of a Complex Polynomial*; and the general geometric measure theory of the Julia sets, together with the local connectivity and the external geometry, belongs to *The Geometry of the Julia Sets* of Part IV.

The article is the $\mathbb{C}$ instance of the dimension theory: the definition, the pressure and the Bowen equation are general, and the quadratic and polynomial cases are what is worked out here. No physics is invoked, and no numerical constant is asserted that has not been recomputed or cited.

## The Hausdorff Dimension

**Definition.** Let $E \subseteq \mathbb{C}$ be a set and let $s \geq 0$. The **$s$-dimensional Hausdorff measure** is

$$
\mathcal{H}^s(E) = \lim_{\delta \to 0} \inf \Bigl\{ \sum_i (\operatorname{diam} E_i)^s : E \subseteq \bigcup_i E_i,\ \operatorname{diam} E_i < \delta \Bigr\} ,
$$

and the **Hausdorff dimension** is

$$
\dim_H E = \inf\{s : \mathcal{H}^s(E) = 0\} = \sup\{s : \mathcal{H}^s(E) = \infty\} .
$$

The definition, the countable stability, the product rules and the comparison with the box dimension are those of *Fractal Geometry*; the Hausdorff dimension is the refinement of the box dimension that the self-similar constructions of the subcategory use.

**Theorem (general bounds).** For a polynomial $f$ of degree $d \geq 2$:

**(a)** $0 \leq \dim_H J(f) \leq 2$, since $J(f) \subseteq \mathbb{C}$;

**(b)** if $J(f)$ is connected and contains more than one point, then $\dim_H J(f) \geq 1$, since a connected subset of the plane with more than one point contains a continuum, and every continuum in a metric space has Hausdorff dimension at least one;

**(c)** if $J(f)$ is disconnected, then it is a Cantor set of the plane and its dimension may be strictly less than one; for real parameters $c > 1/4$ the Julia set of $f_c$ is a Cantor subset of the real axis, and its dimension tends to $0$ as $c \to \infty$.

**Proof.** (a) and (b) are the general facts about subsets of the plane recalled in *Fractal Geometry*; (c) for real $c > 1/4$ the critical orbit escapes, the filled Julia set is a Cantor subset of $\mathbb{R}$ by the real dynamics, and the covering of the Cantor set by the $2^n$ intervals of the $n$-th level gives an upper bound tending to $0$ as $c$ grows. The real case is that of the real quadratic family, and the Cantor structure is the same construction as the middle-third set of the lead article.

**Remark.** The Hausdorff and box dimensions of a hyperbolic Julia set coincide, because the Julia set is the invariant set of a uniformly expanding conformal system and the Moran–Bowen theory applies; the two dimensions differ in general only when the set has an irregular density of scales, which the expansion forbids. The comparison of the two dimensions is in *Fractal Geometry*.

## The Two Computed Quadratic Cases

**Theorem (the circle).** For $f(z) = z^2$ the Julia set is the unit circle and $\dim_H J(f) = 1$, with $0 < \mathcal{H}^1(J) < \infty$: the Julia set is a rectifiable curve.

**Proof.** The orbits of points of modulus less than one converge to $0$ and the orbits of points of modulus greater than one diverge to $\infty$, so the Julia set is the unit circle $S^1$; the circle is a rectifiable curve of Hausdorff dimension one, and its length is $2\pi$.

**Theorem (the segment).** For $f(z) = z^2-2$ the Julia set is the segment $[-2,2]$ and $\dim_H J(f) = 1$, with $0 < \mathcal{H}^1(J) < \infty$.

**Proof.** The map $z \mapsto z^2-2$ is the restriction of the squaring map under the Chebyshev identification: the map $\Phi(w) = w + w^{-1}$ satisfies $\Phi(w^2) = \Phi(w)^2 - 2$, so $f$ is conjugate by $\Phi$ to $w \mapsto w^2$ on the exterior of the unit disk, and the Julia set is the image of the unit circle under $\Phi$, which is the segment $[-2,2]$. A rectifiable curve has Hausdorff dimension one.

**Remark.** The two cases are the exceptional quadratic parameters for which the Julia set is a rectifiable curve; for every other parameter the Julia set is not a curve and its dimension is strictly greater than one when the Julia set is connected, in the sense of the theorem of Ruelle and the dimension formula below. The two cases are exactly the parameters at which the family is "rigid"; whether they are the only quadratic parameters of dimension one is a question of the geometric measure theory of Part IV.

## The Bowen Equation for Hyperbolic Julia Sets

**Definition.** Let $J = J(f)$ be a **hyperbolic** Julia set of a polynomial of degree $d \geq 2$, so that $f$ is expanding on $J$: there are $C > 0$ and $\rho > 1$ with $|(f^n)'(z)| \geq C\rho^n$ for all $z \in J$ and $n \geq 1$. The **pressure function** of the potential $-t\log|f'|$ is

$$
P(t) = \lim_{n \to \infty} \frac{1}{n} \log \sum_{f^n(w) = w} |(f^n)'(w)|^{-t} ,
$$

the sum being over the fixed points of $f^n$ or, equivalently, over any conformal partition of $J$ into pieces of diameter tending to zero.

**Theorem (Bowen).** For a hyperbolic Julia set the function $t \mapsto P(t)$ is strictly decreasing, convex and real-analytic, with $P(0) = \log d > 0$ and $P(t) \to -\infty$ as $t \to \infty$. Hence there is a unique $s > 0$ with

$$
P(s) = 0 ,
$$

the **Bowen equation**, and

$$
\dim_H J(f) = s .
$$

The equilibrium state $\mu_s$ of the potential $-s\log|f'|$ is the invariant measure of **full dimension**: it is ergodic, its measure-theoretic entropy is $h_{\mu_s} = s\,\chi_{\mu_s}$ with $\chi_{\mu_s} = \int\log|f'|\,d\mu_s$, and its Hausdorff dimension is $s$, so that $\dim_H \mu_s = \dim_H J(f)$.

**Proof sketch.** The pressure is finite and real-analytic for $t$ real, because the potential $-t\log|f'|$ is Hölder and the map is uniformly expanding; convexity is the general convexity of the pressure for a real potential, and monotonicity follows from $\log|f'| > 0$ on the hyperbolic Julia set. The Bowen equation has a unique root because $P(0) = \log d > 0$ and $P(t) \to -\infty$. The root equals the dimension because the level sets of the partition of $J$ into pieces of diameter $|(f^n)'|^{-1}$ obey the Moran covering bound: the sum $\sum|(f^n)'|^{-t}$ is comparable to the $t$-dimensional content of the $n$-th level, and its exponential growth rate passes through $0$ exactly at $t = \dim_H J$. The equilibrium state has dimension $s$ by the dimension formula of Ledrappier and Young, and it is the measure of maximal dimension by the same covering estimate. The pressure, the equilibrium states and the dimension formula are those of *Ergodic Theory* and of *The Julia Sets of a Complex Polynomial*.

**Example.** For $c = 0$ the Julia set is the circle, and the equations are solved by $s = 1$: the partition of the circle into the $2^n$ arcs carries the weight $2^{-n}$ each, the sum in the pressure is $2^n \cdot 2^{-nt} = 2^{n(1-t)}$, and its growth rate is $(1-t)\log 2$, which vanishes at $t = 1$. The Bowen value is $1$, in agreement with the direct computation.

**Remark (hyperbolic versus parabolic).** The Bowen equation determines the dimension for every **subhyperbolic** parameter as well, where the critical orbits are eventually repelled; at a **parabolic** parameter the expansion fails at the parabolic cycle, the pressure has a different behaviour, and the dimension is not given by the same equation, although it remains at least one when the Julia set is connected. The parabolic case, and the case of the parameters with an irrationally indifferent cycle, are the delicate points of the theory, and the general results are those of *The Geometry of the Julia Sets*.

## The Dimension as a Function of the Parameter

**Theorem (Ruelle).** The function $c \mapsto \dim_H J(f_c)$ is real-analytic on the set of parameters for which $f_c$ is hyperbolic; more generally, the pressure $P(t;c)$ is real-analytic in $(t,c)$ on the hyperbolic parameters, and the implicit function theorem applied to $P(s;c) = 0$ gives

$$
\frac{\partial s}{\partial c} = -\,\frac{\partial P/\partial c}{\partial P/\partial t} ,
$$

the denominator being nonzero because $P$ is strictly decreasing in $t$.

**Proof sketch.** For a hyperbolic parameter the potential $-t\log|f_c'|$ depends real-analytically on $c$, and the Ruelle–Perron–Frobenius theorem makes the pressure real-analytic in the potential by the analyticity of the transfer operator; the root of a real-analytic strictly decreasing function depends real-analytically on the parameters, by the implicit function theorem.

**Theorem (Shishikura).** For every parameter $c$ on the boundary of the Mandelbrot set, the Julia set has full dimension:

$$
c \in \partial M \implies \dim_H J(f_c) = 2 .
$$

There are also parameters with a Siegel disc at which the Julia set has dimension two; the theorem of Shishikura produces them by a quasiconformal surgery from the boundary parameters.

**Proof sketch.** Shishikura's surgery replaces the dynamics in a neighbourhood of the (semiparabolic or indifferent) cycle by a quasi-self-similar circle whose Julia set contains translates of itself at all scales; the covering of the Julia set by the preimages of this circle gives the estimate $\mathcal{H}^s(J) = \infty$ for every $s < 2$. The full proof is in Shishikura's paper, and the construction is the geometric measure theory of Part IV.

**Corollary.** The dimension function $c \mapsto \dim_H J(f_c)$ equals $1$ at the two exceptional parameters $c = 0$ and $c = -2$, and equals $2$ on the boundary of $M$; whether the two exceptional parameters are the only quadratic parameters of dimension one is part of the geometric measure theory of Part IV.

**Remark (the open questions).** The dimension of the Julia set at a general parameter — at a Siegel parameter with unbounded rotation number, at an attractor-free parameter — is not known in closed form, and the question of the regularity of the dimension as a function of $c$ at the boundary of a hyperbolic component is open in general; the arithmetic of the rotation number enters, and the relevant results are those of the theory of the quadratic family and of the geometric measure theory of Part IV. The multifractal analysis of the measure of maximal dimension, the spectrum of local dimensions and the Legendre transform are those of *Multifractal Analysis and the Legendre Transform* of Part III and of the fractal analysis of that Part.

## Summary

The Hausdorff dimension of a polynomial Julia set lies between $0$ and $2$, and between $1$ and $2$ when the Julia set is connected; it can be below one when the Julia set is a Cantor set, as for real parameters $c > 1/4$. The quadratic family has two exactly computed cases: $z^2$, whose Julia set is the unit circle of dimension one, and $z^2-2$, whose Julia set is the segment $[-2,2]$, also of dimension one. For a hyperbolic Julia set the dimension is the unique root $s$ of the Bowen equation $P(-s\log|f'|) = 0$, and the equilibrium state of $-s\log|f'|$ is an ergodic invariant measure of Hausdorff dimension exactly $s$; the Bowen value is the measure of maximal dimension, and it agrees with the Hausdorff dimension of the set by the Moran estimate. The dimension is a real-analytic function of the parameter on the hyperbolic parameters, by Ruelle; it equals two on the boundary of the Mandelbrot set and at suitable Siegel parameters, by Shishikura. Beyond these cases the dimension is not known in closed form, and the general geometric measure theory of the Julia sets is that of Part IV.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\dim_H E$ | Hausdorff dimension of $E$ |
| $\mathcal{H}^s$, $\mathcal{H}^s(J)$ | $s$-dimensional Hausdorff measure and its value on $J$ |
| $P(t) = P(-t\log\lvert f'\rvert)$ | Pressure of the potential $-t\log\lvert f'\rvert$ |
| $s$, Bowen equation | Root of $P(s)=0$; $\dim_H J = s$ for hyperbolic $J$ |
| $\mu_s$ | Equilibrium state of $-s\log\lvert f'\rvert$, the measure of full dimension |
| $\chi_{\mu_s} = \int\log\lvert f'\rvert d\mu_s$ | Lyapunov exponent of $\mu_s$ |
| $\partial M$ | Boundary of the Mandelbrot set; $\dim_H J_c = 2$ there |

## Further Reading

- Rufus Bowen, "Hausdorff dimension of quasicircles", *Publications Mathématiques de l'IHÉS* 50 (1979), 11–25, for the pressure equation and the dimension of a conformal repeller.
- David Ruelle, "Repellers for real analytic maps", *Ergodic Theory and Dynamical Systems* 2 (1982), 99–107, for the real-analyticity of the pressure and the dimension.
- François Ledrappier and Lai-Sang Young, "The metric entropy of diffeomorphisms I, II", *Annals of Mathematics* 122 (1985), 509–574, for the dimension formula of a measure.
- Mitsuhiro Shishikura, "The Hausdorff dimension of the boundary of the Mandelbrot set and Julia sets", *Annals of Mathematics* 147 (1998), 225–267, for the dimension two on the boundary of $M$ and at Siegel parameters.
- Feliks Przytycki and Mariusz Urbański, *Conformal Fractals: Ergodic Theory Methods* (Cambridge University Press, 2010), for the Bowen equation, the pressure and the measure of maximal dimension.
- Curtis T. McMullen, *Complex Dynamics and Renormalization* (Princeton University Press, 1994), for the dimension, the rigidity and the quadratic family.
- Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications*, 3rd edition (Wiley, 2014), for the definition of the Hausdorff dimension and the comparison with the box dimension.
