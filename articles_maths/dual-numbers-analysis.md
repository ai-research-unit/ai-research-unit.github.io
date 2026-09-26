# __Dual Numbers Analysis__

## Introduction

This article introduces dual numbers analysis as the study of differentiable functions of a dual variable. The goal is to define the core objects precisely, establish their basic properties, and describe the theorems that give the subject its shape.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. The dual number algebra is assumed from the article on dual numbers algebra, and the maximal ideal is used throughout. The article is stated for an arbitrary commutative ring $R$ in which $2$ is invertible, and no finiteness assumption is made unless stated.

Throughout this article, the dual number algebra is denoted $\mathbb{D}'$, and the split complex algebra is denoted $\mathbb{D}$. The unit of $\mathbb{D}'$ is denoted $\varepsilon$, and it satisfies $\varepsilon^2 = 0$.

## The Dual Number Plane

### Points and Distance

A dual number is written

$$
z = x + y \varepsilon, \qquad x, y \in R,
$$

where $\varepsilon^2 = 0$. The element $x$ is the **real part**, and $y$ is the **infinitesimal part**. We write $x = \operatorname{Re} z$ and $y = \operatorname{Inf} z$.

There is no Euclidean modulus intrinsic to the algebra, because the norm form $N(z) = x^2$ is degenerate and vanishes on the maximal ideal. The closest analogue is the **Euclidean modulus**

$$
\|z\|_E = \sqrt{x^2 + y^2},
$$

which is the ordinary Euclidean norm on the underlying module $\mathbb{D}' \cong R^2$, defined when $R$ is an ordered ring. It is not multiplicative with respect to the dual product.

The **dual distance** between two dual numbers $z$ and $w$ is

$$
d(z, w) = \|z - w\|_E.
$$

This makes $\mathbb{D}'$ a metric space when $R = \mathbb{R}$, isometric to $\mathbb{R}^2$. The topology of $\mathbb{D}'$ is the ordinary Euclidean topology of the plane.

### Balls and Neighborhoods

The **open ball** of radius $r > 0$ centered at $z_0$ is

$$
B(z_0, r) = \{z \in \mathbb{D}' : \|z - z_0\|_E < r\}.
$$

It is an open disk in the dual plane, exactly as in the complex plane. The topology of $\mathbb{D}'$ is the ordinary Euclidean topology, because the algebra is two-dimensional over $\mathbb{R}$ and the Euclidean norm is a genuine norm on the underlying real vector space.

### Open and Closed Sets

A set $U \subseteq \mathbb{D}'$ is **open** if for every $z_0 \in U$ there exists $r > 0$ with $B(z_0, r) \subseteq U$.

A set $F \subseteq \mathbb{D}'$ is **closed** if its complement $\mathbb{D}' \setminus F$ is open.

Arbitrary unions of open sets are open. Finite intersections of open sets are open. Dually for closed sets.

### Connectedness and Domains

A set $U \subseteq \mathbb{D}'$ is **connected** if it cannot be written as the disjoint union of two non-empty sets open in $U$. It is **path-connected** if any two points can be joined by a continuous path in $U$. For open subsets of $\mathbb{D}'$, connectedness and path-connectedness are equivalent.

A **domain** is a non-empty open connected subset of $\mathbb{D}'$. Domains are the natural setting for dual numbers analysis, because differentiability on a domain imposes constraints that are weaker than in the complex case but still nontrivial.

### Compactness

A set $K \subseteq \mathbb{D}'$ is **compact** if every open cover of $K$ has a finite subcover.

**Theorem (Heine–Borel).** A subset of $\mathbb{D}'$ is compact iff it is closed and bounded in the Euclidean norm.

**Theorem.** A continuous dual-valued function on a compact set is bounded and attains its maximum and minimum Euclidean modulus.

## Limits and Continuity

### Limits of Sequences

A sequence $(z_n)$ of dual numbers **converges** to $L \in \mathbb{D}'$ if for every $\epsilon > 0$ there exists $N \in \mathbb{N}$ such that

$$
n \geq N \implies \|z_n - L\|_E < \epsilon.
$$

We write $z_n \to L$ or $\lim_{n \to \infty} z_n = L$.

**Uniqueness.** If $z_n \to L$ and $z_n \to L'$, then $L = L'$.

**Componentwise convergence.** Write $z_n = x_n + y_n \varepsilon$ and $L = a + b \varepsilon$. Then

$$
z_n \to L \iff x_n \to a \text{ and } y_n \to b.
$$

This is the reason dual convergence is no harder than real convergence: it is two real convergences in parallel.

**Boundedness.** Every convergent sequence is bounded. The converse fails.

**Algebra of limits.** If $z_n \to L$ and $w_n \to M$, then

$$
z_n + w_n \to L + M, \qquad z_n w_n \to L M.
$$

There is no quotient rule in general, because $\mathbb{D}'$ has zero divisors.

### Cauchy Sequences

A sequence $(z_n)$ is **Cauchy** if for every $\epsilon > 0$ there exists $N \in \mathbb{N}$ such that

$$
m, n \geq N \implies \|z_m - z_n\|_E < \epsilon.
$$

**Theorem.** In $\mathbb{D}'$, a sequence converges iff it is Cauchy. This is the completeness of $\mathbb{D}'$ as a metric space, and it follows from the completeness of $\mathbb{R}$ applied to the real and infinitesimal parts.

### Limits of Functions

Let $f : D \to \mathbb{D}'$ with $D \subseteq \mathbb{D}'$, and let $z_0$ be a limit point of $D$. We say

$$
\lim_{z \to z_0} f(z) = L
$$

if for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
z \in D, \; 0 < \|z - z_0\|_E < \delta \implies \|f(z) - L\|_E < \epsilon.
$$

**Uniqueness.** If the limit exists, it is unique.

**Sequential criterion.** $\lim_{z \to z_0} f(z) = L$ iff for every sequence $(z_n)$ in $D \setminus \{z_0\}$ with $z_n \to z_0$, we have $f(z_n) \to L$.

**Algebra of limits.** Sums and products of limits are the limits of the sums and products.

### Continuity

A function $f : D \to \mathbb{D}'$ is **continuous at** $z_0 \in D$ if

$$
\lim_{z \to z_0} f(z) = f(z_0).
$$

Equivalently, for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
z \in D, \; \|z - z_0\|_E < \delta \implies \|f(z) - f(z_0)\|_E < \epsilon.
$$

$f$ is **continuous on** $D$ if it is continuous at every point of $D$.

**Theorem.** Sums and products of continuous functions are continuous. Compositions of continuous functions are continuous.

**Theorem.** $f$ is continuous iff the preimage of every open set is open. Equivalently, the preimage of every closed set is closed.

**Componentwise continuity.** Write $f(z) = u(x, y) + v(x, y) \varepsilon$. Then $f$ is continuous at $z_0 = x_0 + y_0 \varepsilon$ iff $u$ and $v$ are continuous at $(x_0, y_0)$. This reduces dual continuity to real continuity of two functions of two variables.

### Uniform Continuity

A function $f : D \to \mathbb{D}'$ is **uniformly continuous** if for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
z, w \in D, \; \|z - w\|_E < \delta \implies \|f(z) - f(w)\|_E < \epsilon.
$$

**Theorem.** A continuous function on a compact set is uniformly continuous.

## Dual Differentiability

### The Derivative

Let $f : U \to \mathbb{D}'$ with $U$ open, and let $z_0 \in U$. The **derivative** of $f$ at $z_0$ is

$$
f'(z_0) = \lim_{h \to 0} \frac{f(z_0 + h) - f(z_0)}{h},
$$

provided the limit exists. If it does, $f$ is **dual differentiable** at $z_0$, or **holomorphic** at $z_0$ in the dual sense.

The limit is taken in the dual plane, so $h$ can approach $0$ from any direction. But because $\mathbb{D}'$ has zero divisors, the quotient is not always defined, and the limit must be taken along paths where $h$ is invertible. This is the fundamental difference from the complex case.

**Theorem.** Dual differentiability implies continuity. The converse fails.

### The Cauchy–Riemann Equations

Write $f(z) = u(x, y) + v(x, y) \varepsilon$, where $z = x + y\varepsilon$ and $u, v : U \to R$.

**Theorem.** $f$ is dual differentiable at $z_0 = x_0 + y_0 \varepsilon$ iff $u$ and $v$ are real differentiable at $(x_0, y_0)$ and satisfy the **dual Cauchy–Riemann equations**

$$
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \qquad \frac{\partial u}{\partial y} = 0.
$$

**Proof.** Write $h = h_1 + h_2 \varepsilon$. The difference quotient is

$$
\frac{f(z_0 + h) - f(z_0)}{h} = \frac{(u_x h_1 + u_y h_2) + (v_x h_1 + v_y h_2) \varepsilon}{h_1 + h_2 \varepsilon} + o(1).
$$

For the limit to exist independently of the direction of $h$, the numerator must be a dual multiple of $h$. This forces $u_y = 0$ and $u_x = v_y$; the remaining partial $v_x$ is free and becomes the infinitesimal part of the derivative. $\square$

**Corollary.** If $f$ is dual differentiable on a domain, then $u$ depends only on $x$, and $v$ is affine in $y$ with slope $u'(x)$:

$$
f(x + y\varepsilon) = u(x) + \left( y u'(x) + c(x) \right) \varepsilon,
$$

where $u$ and $c$ are ordinary differentiable functions of one variable. So a dual differentiable function is determined by two ordinary differentiable functions of one real variable, and it is constant in the infinitesimal direction only when $u$ is constant.

This is the fundamental difference from complex analysis: the dual Cauchy–Riemann equations force the real part to be independent of the infinitesimal direction and force the infinitesimal part to be affine in it with slope $u'(x)$, while the complex Cauchy–Riemann equations force the function to be harmonic. The dual differentiable functions are a restrictive class, and this is the reason dual numbers analysis is less developed than complex analysis.

### The Wirtinger Derivatives

Define the **dual Wirtinger derivatives**

$$
\frac{\partial}{\partial z} = \frac{\partial}{\partial x}, \qquad \frac{\partial}{\partial \bar{z}} = \frac{\partial}{\partial y} - \varepsilon \frac{\partial}{\partial x}.
$$

**Theorem.** $f = u + v\varepsilon$ is dual differentiable iff $\partial f / \partial \bar{z} = 0$, that is, iff $u_y = 0$ and $v_y = u_x$. In that case,

$$
f'(z) = \frac{\partial f}{\partial z} = u'(x) + v_x \varepsilon.
$$

### Rules of Differentiation

**Linearity.** $(af + bg)' = a f' + b g'$.

**Product rule.** $(fg)' = f' g + f g'$.

**Quotient rule.** $(f/g)' = (f' g - f g')/g^2$ where $g$ is invertible.

**Chain rule.** $(f \circ g)'(z) = f'(g(z)) g'(z)$.

**Inverse function rule.** If $f$ is dual differentiable at $z_0$ with $f'(z_0)$ invertible and $f^{-1}$ is defined near $f(z_0)$, then

$$
(f^{-1})'(f(z_0)) = \frac{1}{f'(z_0)}.
$$

## The Infinitesimal Direction

### The Maximal Ideal

The **maximal ideal** of $\mathbb{D}'$ is

$$
\mathfrak{m} = (\varepsilon) = \{y \varepsilon : y \in R\}.
$$

It is the set of elements with vanishing real part, and it is nilpotent of index two:

$$
\mathfrak{m}^2 = 0.
$$

The maximal ideal is the infinitesimal direction, and it is the obstruction to the algebra being a field.

### The Infinitesimal Part

The **infinitesimal part** of a dual number $z = x + y\varepsilon$ is the component $y \varepsilon$ in the maximal ideal. The projection

$$
\pi : \mathbb{D}' \to R, \qquad \pi(x + y\varepsilon) = x,
$$

is the **augmentation map**, and its kernel is the maximal ideal. The augmentation is a ring homomorphism, and it is the unique one from $\mathbb{D}'$ to $R$.

### The Infinitesimal Translation

For $h \in \mathfrak{m}$, the map

$$
T_h : \mathbb{D}' \to \mathbb{D}', \qquad T_h(z) = z + h,
$$

is the **infinitesimal translation** by $h$. It is a bijection of $\mathbb{D}'$ onto itself, and it preserves differences: $T_h(z) - T_h(w) = z - w$. The infinitesimal translations form a group isomorphic to the additive group of the maximal ideal.

## Integration

### Contour Integrals

Let $\gamma : [a, b] \to \mathbb{D}'$ be a piecewise continuously differentiable path, and let $f$ be continuous on the image of $\gamma$. The **contour integral** of $f$ along $\gamma$ is

$$
\int_\gamma f(z) \, dz = \int_a^b f(\gamma(t)) \gamma'(t) \, dt.
$$

**Linearity.** $\int_\gamma (af + bg) = a \int_\gamma f + b \int_\gamma g$.

**Reversal.** $\int_{-\gamma} f = -\int_\gamma f$.

**Additivity.** If $\gamma$ is the concatenation of $\gamma_1$ and $\gamma_2$, then $\int_\gamma f = \int_{\gamma_1} f + \int_{\gamma_2} f$.

**Estimation.** If $\|f(z)\|_E \leq M$ on $\gamma$ and $L$ is the length of $\gamma$, then

$$
\left\| \int_\gamma f(z) \, dz \right\|_E \leq M L.
$$

### The Cauchy–Goursat Theorem

**Theorem (Cauchy–Goursat, dual version).** If $f$ is dual differentiable on a simply connected domain $U$ and $\gamma$ is a closed contour in $U$, then

$$
\oint_\gamma f(z) \, dz = 0
$$

provided the contour does not cross the maximal ideal in a way that makes the integral diverge.

**Proof.** Since $f$ is dual differentiable, it is of the form $f(x + y\varepsilon) = u(x) + (y u'(x) + c(x))\varepsilon$. Let $U$ be an antiderivative of $u$ and let $C$ be an antiderivative of $c$, and set $F(x + y\varepsilon) = U(x) + (y u(x) + C(x))\varepsilon$. Then $F$ is dual differentiable with $F' = f$: its real part is $U$ with $U' = u$, and the $x$-derivative of its infinitesimal part $y u(x) + C(x)$ is $y u'(x) + c(x)$. So $f$ has a primitive, and the integral of $f$ over a closed contour vanishes. $\square$

**Caution.** The theorem fails if the contour crosses the maximal ideal in a way that makes the integral diverge. The maximal ideal is the analogue of the branch cut in complex analysis, and it must be avoided.

### The Cauchy Integral Formula

There is **no** general Cauchy integral formula in dual numbers analysis. The reason is that the kernel $1/(w - z)$ has a singularity on the maximal ideal, and the integral around a point depends on the path in a way that cannot be removed by a single formula.

However, if the function is written in the form $f(x + y\varepsilon) = u(x) + (y u'(x) + c(x))\varepsilon$, then the real part $u$ and the function $c$ have the ordinary real Cauchy integral formula, and the infinitesimal part is recovered from them. So the dual differentiable functions are reconstructed from their real data by the real theory.

## Power Series

### Definition

A **power series** centered at $z_0$ is

$$
\sum_{n=0}^\infty c_n (z - z_0)^n, \qquad c_n \in \mathbb{D}'.
$$

The **radius of convergence** is

$$
R = \frac{1}{\limsup_{n \to \infty} \|c_n\|_E^{1/n}},
$$

with the conventions $R = 0$ if the limsup is $\infty$ and $R = \infty$ if the limsup is $0$.

**Theorem.** The series converges absolutely for $\|z - z_0\|_E < R$ and diverges for $\|z - z_0\|_E > R$. On $\|z - z_0\|_E < R$ it converges uniformly on compact subsets.

**Theorem.** A power series is dual differentiable on $\|z - z_0\|_E < R$, and its derivative is obtained by term-by-term differentiation:

$$
\frac{d}{dz} \sum_{n=0}^\infty c_n (z - z_0)^n = \sum_{n=1}^\infty n c_n (z - z_0)^{n-1}.
$$

The differentiated series has the same radius of convergence.

### Taylor Series

**Theorem (Taylor, dual version).** If $f$ is dual differentiable on a domain containing the closed disk $\overline{B}(z_0, r)$, then $f$ has a power series expansion

$$
f(z) = \sum_{n=0}^\infty \frac{f^{(n)}(z_0)}{n!} (z - z_0)^n
$$

valid for $\|z - z_0\|_E < r$.

**Proof.** Since $f$ is dual differentiable, it is of the form $f(x + y\varepsilon) = u(x) + (y u'(x) + c(x))\varepsilon$. The real part $u$ has an ordinary real Taylor expansion, and the infinitesimal part $y u'(x) + c(x)$ is expanded by differentiating term by term. So the expansion is the real Taylor expansion of $u$ plus $\varepsilon$ times the real Taylor expansion of $y u'(x) + c(x)$. $\square$

**Corollary.** A dual differentiable function is analytic: it equals its Taylor series in a neighborhood of every point.

**Caution.** The identity theorem fails in general, because a dual differentiable function can vanish on a set with an accumulation point without being identically zero. The reason is that the real part and the infinitesimal part are independent, and one can vanish while the other does not.

## Singularities

### Classification

Let $f$ be dual differentiable on a punctured disk $0 < \|z - z_0\|_E < R$.

**Removable singularity.** $z_0$ is removable if $f$ extends to a dual differentiable function on $\|z - z_0\|_E < R$.

**Pole.** $z_0$ is a pole if $f(z) \to \infty$ in Euclidean modulus as $z \to z_0$.

**Essential singularity.** $z_0$ is an essential singularity if it is neither removable nor a pole.

**Caution.** The classification is more complicated than in the complex case, because the function can behave differently on the real and infinitesimal components. A point can be removable for one component and a pole for the other, in which case it is neither removable nor a pole for the dual function.

### Residues

There is **no** general residue theory in dual numbers analysis. The reason is that the integral around a singularity depends on the path, and there is no single number that captures the singularity. The dual differentiable functions are of the form $u(x) + (y u'(x) + c(x))\varepsilon$, and the singularity structure is that of the real functions $u$ and $c$.

## Applications

### Automatic Differentiation

The dual numbers are the coefficient algebra for forward-mode automatic differentiation. A function $f : \mathbb{R} \to \mathbb{R}$ extends to a function on $\mathbb{D}'$ by the formula

$$
f(x + \varepsilon) = f(x) + f'(x) \varepsilon,
$$

which is exact because $\varepsilon^2 = 0$. This is the algebraic content of the derivative, and it is the basis of the computational technique.

### Infinitesimal Deformations

The dual numbers are the coefficients of first-order deformations. A deformation of a mathematical object over the dual numbers is a family parametrized by $\varepsilon$, with $\varepsilon^2 = 0$, and the first-order information is the derivative with respect to $\varepsilon$.

### The Tangent Space

In algebraic geometry, the tangent space at a point $x$ of a scheme $X$ is the set of morphisms $\operatorname{Spec} \mathbb{D}' \to X$ sending the closed point to $x$. The dual numbers are the algebraic model of the infinitesimal neighborhood of a point.

## Comparison with Complex Analysis

The differences between dual numbers analysis and complex analysis are consequences of the sign in the multiplication rule $\varepsilon^2 = 0$ versus $i^2 = -1$.

| Property | Complex | Dual |
|---|---|---|
| Multiplication | $i^2 = -1$ | $\varepsilon^2 = 0$ |
| Zero divisors | none | $\varepsilon$ |
| Cauchy–Riemann | $u_x = v_y$, $u_y = -v_x$ | $u_x = v_y$, $u_y = 0$ |
| Harmonic equation | $\Delta u = 0$ | $u_y = 0$, $v$ affine in $y$ |
| Cauchy integral | yes | no |
| Residue theory | yes | no |
| Liouville | yes | no |
| Identity theorem | yes | no |
| Conformality | yes | no |
| Differentiable functions | rich | $u(x) + (y u'(x) + c(x))\varepsilon$ |

The complex case is rigid: differentiability is a strong condition, and it forces the function to be determined by its boundary values. The dual case is also rigid: differentiability forces the real part to be independent of the infinitesimal direction, and leaves two ordinary differentiable functions of one variable (the real part and the value of the infinitesimal part along $y = 0$).

## Summary

Dual numbers analysis is the study of differentiable functions of a dual variable $z = x + y\varepsilon$ with $\varepsilon^2 = 0$. The plane carries the Euclidean norm inherited from $R^2$, and with it the convergent sequences and the continuous functions on which the subject is built.

The derivative is defined as in the complex case, but its behaviour differs because $\varepsilon$ is nilpotent. The structure theorem for dual differentiability records the consequence: the infinitesimal part of a dual differentiable function is determined by the derivative of its real part, so a dual function carries its own derivative inside itself. The maximal ideal $\mathfrak{m} = (\varepsilon)$, nilpotent of index two, is the infinitesimal direction, and it is the source of that rigidity.

The article develops what the nilpotent structure supports: contour integrals along paths, power series with their radius of convergence, and the classification of the isolated singularities as removable, a pole, or essential. The final sections record the relation of the dual calculus to ordinary differentiation and compare the subject with complex analysis, where the square of the imaginary unit vanishes rather than equalling $-1$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'$ | Dual number algebra |
| $\varepsilon$ | Dual unit, $\varepsilon^2 = 0$ |
| $z = x + y\varepsilon$ | General dual number |
| $x = \operatorname{Re} z$ | Real part |
| $y = \operatorname{Inf} z$ | Infinitesimal part |
| $\|z\|_E = \sqrt{x^2 + y^2}$ | Euclidean modulus |
| $B(z_0, r)$ | Open disk of radius $r$ |
| $f'(z)$ | Dual derivative |
| $\partial/\partial z, \partial/\partial \bar{z}$ | Dual Wirtinger derivatives |
| $\mathfrak{m} = (\varepsilon)$ | Maximal ideal |
| $\pi : \mathbb{D}' \to R$ | Augmentation map |
| $\int_\gamma f(z) \, dz$ | Contour integral |

## Further Reading

- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the origin of the dual numbers in the biquaternion program.
- Eduard Study, *Geometrie der Dynamen* (1903), for the geometry of dual numbers.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991), for the theory of algebras over commutative rings.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (AMS, 2005), for the general theory of quadratic forms.
- Andreas Griewank and Andrea Walther, *Evaluating Derivatives* (SIAM, 2008), for automatic differentiation with dual numbers.

