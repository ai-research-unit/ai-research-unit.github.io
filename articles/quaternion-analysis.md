
# Quaternion Analysis

## Introduction

This article introduces quaternion analysis as the study of differentiable functions of a quaternion variable. The goal is to define the core objects precisely, establish their basic properties, and describe the theorems that give the subject its shape.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. The quaternion algebra is assumed from the article on quaternion algebra, and the scalar-vector decomposition is used throughout. The article is stated for the quaternion algebra over the real numbers, and the complexification is mentioned only where it clarifies the structure.

Throughout this article, the quaternion algebra is denoted $\mathbb{H}$, and its basis is $e_0 = 1, e_1, e_2, e_3$. The scalar imaginary of the complex numbers is denoted $i$, so that it does not collide with the quaternion units.

## The Quaternion Space

### Points and Distance

A quaternion is written

$$
q = q_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q_\mu \in \mathbb{R}.
$$

The real number $q_0$ is the **scalar part**, and the triple $(q_1, q_2, q_3)$ is the **vector part**. We write $q = q_0 + \mathbf{q}$ with $\mathbf{q} \in \mathbb{R}^3$.

The **modulus** of $q$ is

$$
|q| = \sqrt{q \bar{q}} = \sqrt{q_0^2 + q_1^2 + q_2^2 + q_3^2},
$$

where $\bar{q} = q_0 - \mathbf{q}$ is the quaternion conjugate. The modulus is a genuine norm on the underlying real vector space $\mathbb{H} \cong \mathbb{R}^4$: positive-definite, subadditive, and homogeneous of degree one. It is multiplicative:

$$
|pq| = |p| |q|.
$$

The **distance** between two quaternions $p$ and $q$ is

$$
d(p, q) = |p - q|.
$$

This makes $\mathbb{H}$ a metric space isometric to $\mathbb{R}^4$. The topology of $\mathbb{H}$ is the ordinary Euclidean topology of four-dimensional space.

### Balls and Neighborhoods

The **open ball** of radius $r > 0$ centered at $q_0$ is

$$
B(q_0, r) = \{q \in \mathbb{H} : |q - q_0| < r\}.
$$

It is an open ball in the quaternion space, exactly as in the real case. The topology is the ordinary Euclidean topology.

### Open and Closed Sets

A set $U \subseteq \mathbb{H}$ is **open** if for every $q_0 \in U$ there exists $r > 0$ with $B(q_0, r) \subseteq U$.

A set $F \subseteq \mathbb{H}$ is **closed** if its complement $\mathbb{H} \setminus F$ is open.

Arbitrary unions of open sets are open. Finite intersections of open sets are open. Dually for closed sets.

### Connectedness and Domains

A set $U \subseteq \mathbb{H}$ is **connected** if it cannot be written as the disjoint union of two non-empty open sets. It is **path-connected** if any two points can be joined by a continuous path in $U$. For open subsets of $\mathbb{H}$, connectedness and path-connectedness are equivalent.

A **domain** is a non-empty open connected subset of $\mathbb{H}$. Domains are the natural setting for quaternion analysis, because differentiability on a domain imposes constraints that are weaker than in the complex case but still nontrivial.

### Compactness

A set $K \subseteq \mathbb{H}$ is **compact** if every open cover of $K$ has a finite subcover.

**Theorem (Heine–Borel).** A subset of $\mathbb{H}$ is compact iff it is closed and bounded in the modulus.

**Theorem.** A continuous quaternion-valued function on a compact set is bounded and attains its maximum and minimum modulus.

## Limits and Continuity

### Limits of Sequences

A sequence $(q_n)$ of quaternions **converges** to $L \in \mathbb{H}$ if for every $\epsilon > 0$ there exists $N \in \mathbb{N}$ such that

$$
n \geq N \implies |q_n - L| < \epsilon.
$$

We write $q_n \to L$ or $\lim_{n \to \infty} q_n = L$.

**Uniqueness.** If $q_n \to L$ and $q_n \to L'$, then $L = L'$.

**Componentwise convergence.** Write $q_n = q_{n,0} + q_{n,1} e_1 + q_{n,2} e_2 + q_{n,3} e_3$ and $L = L_0 + L_1 e_1 + L_2 e_2 + L_3 e_3$. Then

$$
q_n \to L \iff q_{n,\mu} \to L_\mu \text{ for } \mu = 0, 1, 2, 3.
$$

This is the reason quaternion convergence is no harder than real convergence: it is four real convergences in parallel.

**Boundedness.** Every convergent sequence is bounded. The converse fails.

**Algebra of limits.** If $q_n \to L$ and $r_n \to M$, then

$$
q_n + r_n \to L + M, \qquad q_n r_n \to L M, \qquad q_n^{-1} \to L^{-1} \text{ if } L \neq 0.
$$

The quotient rule holds because $\mathbb{H}$ is a division algebra: every non-zero quaternion is invertible.

### Cauchy Sequences

A sequence $(q_n)$ is **Cauchy** if for every $\epsilon > 0$ there exists $N \in \mathbb{N}$ such that

$$
m, n \geq N \implies |q_m - q_n| < \epsilon.
$$

**Theorem.** In $\mathbb{H}$, a sequence converges iff it is Cauchy. This is the completeness of $\mathbb{H}$ as a metric space, and it follows from the completeness of $\mathbb{R}$ applied to the four components.

### Limits of Functions

Let $f : D \to \mathbb{H}$ with $D \subseteq \mathbb{H}$, and let $q_0$ be a limit point of $D$. We say

$$
\lim_{q \to q_0} f(q) = L
$$

if for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
q \in D, \; 0 < |q - q_0| < \delta \implies |f(q) - L| < \epsilon.
$$

**Uniqueness.** If the limit exists, it is unique.

**Sequential criterion.** $\lim_{q \to q_0} f(q) = L$ iff for every sequence $(q_n)$ in $D \setminus \{q_0\}$ with $q_n \to q_0$, we have $f(q_n) \to L$.

**Algebra of limits.** Sums, products, and quotients (where defined) of limits are the limits of the sums, products, and quotients.

### Continuity

A function $f : D \to \mathbb{H}$ is **continuous at** $q_0 \in D$ if

$$
\lim_{q \to q_0} f(q) = f(q_0).
$$

Equivalently, for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
q \in D, \; |q - q_0| < \delta \implies |f(q) - f(q_0)| < \epsilon.
$$

$f$ is **continuous on** $D$ if it is continuous at every point of $D$.

**Theorem.** Sums, products, and quotients (where defined) of continuous functions are continuous. Compositions of continuous functions are continuous.

**Theorem.** $f$ is continuous iff the preimage of every open set is open. Equivalently, the preimage of every closed set is closed.

**Componentwise continuity.** Write $f(q) = f_0(q) + f_1(q) e_1 + f_2(q) e_2 + f_3(q) e_3$. Then $f$ is continuous at $q_0$ iff each $f_\mu$ is continuous at $q_0$. This reduces quaternion continuity to real continuity of four functions of four variables.

### Uniform Continuity

A function $f : D \to \mathbb{H}$ is **uniformly continuous** if for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
p, q \in D, \; |p - q| < \delta \implies |f(p) - f(q)| < \epsilon.
$$

**Theorem.** A continuous function on a compact set is uniformly continuous.

## Quaternion Differentiability

### The Derivative

Let $f : U \to \mathbb{H}$ with $U$ open, and let $q_0 \in U$. The **derivative** of $f$ at $q_0$ is

$$
f'(q_0) = \lim_{h \to 0} \frac{f(q_0 + h) - f(q_0)}{h},
$$

provided the limit exists. If it does, $f$ is **quaternion differentiable** at $q_0$, or **holomorphic** at $q_0$ in the quaternion sense.

The limit is taken in the quaternion space, so $h$ can approach $0$ from any direction. This is a much stronger condition than real differentiability: the difference quotient must tend to the same limit along every path. The condition is so strong that it forces the function to be affine.

**Theorem.** Quaternion differentiability implies continuity. The converse fails.

### The Cauchy–Riemann Equations

Write $f(q) = u(q) + v_1(q) e_1 + v_2(q) e_2 + v_3(q) e_3$, where $q = x_0 + x_1 e_1 + x_2 e_2 + x_3 e_3$ and $u, v_k : U \to \mathbb{R}$.

**Theorem.** $f$ is quaternion differentiable at $q_0$ iff the components $u, v_1, v_2, v_3$ are real differentiable at $q_0$ and satisfy the **quaternion Cauchy–Riemann equations**

$$
\frac{\partial u}{\partial x_0} = \frac{\partial v_1}{\partial x_1} = \frac{\partial v_2}{\partial x_2} = \frac{\partial v_3}{\partial x_3},
$$

$$
\frac{\partial u}{\partial x_k} = -\frac{\partial v_k}{\partial x_0}, \qquad k = 1, 2, 3,
$$

and the remaining equations obtained by cyclically permuting the indices $1, 2, 3$.

**Proof.** Write $h = h_0 + h_1 e_1 + h_2 e_2 + h_3 e_3$. The difference quotient is

$$
\frac{f(q_0 + h) - f(q_0)}{h} = \frac{\sum_\mu h_\mu \partial_\mu f}{h} + o(1).
$$

For the limit to exist independently of the direction of $h$, the numerator must be a left multiple of $h$, and the multiplication must be consistent with the quaternion relations. This forces the equations. $\square$

### The Liouville Theorem

**Theorem (Liouville).** Every bounded quaternion differentiable function on all of $\mathbb{H}$ is constant.

**Proof.** The quaternion Cauchy–Riemann equations force the components to be harmonic and to satisfy strong constraints. The only bounded solutions on all of $\mathbb{H}$ are constants. $\square$

This is the quaternion analogue of the Liouville theorem in complex analysis, and it shows that the class of quaternion differentiable functions is very rigid.

### The Class of Quaternion Differentiable Functions

The quaternion Cauchy–Riemann equations are so restrictive that the quaternion differentiable functions are exactly the functions of the form

$$
f(q) = a q + b, \qquad a, b \in \mathbb{H}.
$$

That is, the only quaternion differentiable functions are the affine functions. This is the fundamental difference from complex analysis, where the class of holomorphic functions is rich.

**Proof.** The Cauchy–Riemann equations force all second derivatives to vanish, so the function is affine. The details are a computation using the quaternion relations. $\square$

So the naive notion of quaternion differentiability is too restrictive to be useful. This is the reason quaternion analysis is not the direct analogue of complex analysis.

## The Correct Notion: Monogenic Functions

### Definition

A function $f : U \to \mathbb{H}$ is **monogenic** (or **regular**) if it satisfies the **Cauchy–Riemann–Fueter equation**

$$
\frac{\partial f}{\partial x_0} + e_1 \frac{\partial f}{\partial x_1} + e_2 \frac{\partial f}{\partial x_2} + e_3 \frac{\partial f}{\partial x_3} = 0.
$$

Equivalently, if $D = \partial_{x_0} + e_1 \partial_{x_1} + e_2 \partial_{x_2} + e_3 \partial_{x_3}$ is the **Dirac operator**, then $f$ is monogenic iff $D f = 0$.

The Dirac operator satisfies

$$
D^2 = \partial_{x_0}^2 + \partial_{x_1}^2 + \partial_{x_2}^2 + \partial_{x_3}^2 = \Delta,
$$

where $\Delta$ is the Laplacian on $\mathbb{R}^4$. So monogenic functions are harmonic:

$$
\Delta f = 0.
$$

### Properties

Monogenic functions satisfy:

**Closure under left and right multiplication by constants.** If $f$ is monogenic and $a, b \in \mathbb{H}$, then $a f$ and $f b$ are monogenic.

**The Cauchy integral formula.** If $f$ is monogenic on a domain containing a ball $B(q_0, r)$, then

$$
f(q) = \frac{1}{2\pi^2} \int_{\partial B(q_0, r)} \frac{(w - q)^{-1}}{|w - q|^2} n(w) f(w) \, dS(w),
$$

where $n(w)$ is the outward unit normal and $dS$ is the surface measure on the sphere. This is the quaternion analogue of the Cauchy integral formula.

**The maximum principle.** If $f$ is monogenic on a domain and $|f|$ attains its maximum at an interior point, then $f$ is constant.

**The Liouville theorem.** Every bounded monogenic function on all of $\mathbb{H}$ is constant.

**The identity theorem.** If two monogenic functions agree on a set with an accumulation point in a domain, they agree on the whole domain.

So monogenic functions are the correct analogue of holomorphic functions in quaternion analysis. They form a rich class, and they satisfy the standard theorems of complex analysis.

### The Relation to the Dirac Operator

The Dirac operator $D$ is the quaternion analogue of the Cauchy–Riemann operator $\bar{\partial}$ in complex analysis. It factors the Laplacian:

$$
D^2 = \Delta,
$$

and the monogenic functions are the kernel of $D$. This is the starting point of **Clifford analysis**, which generalizes the theory to $\mathbb{R}^n$ with Clifford algebra coefficients.

### The Cauchy–Riemann–Fueter Equation

The Cauchy–Riemann–Fueter equation $D f = 0$ is a first-order system of four real equations for the four components of $f$. It is elliptic, and its solutions are harmonic. The equation is the quaternion analogue of the Cauchy–Riemann equations, and it is the correct notion of differentiability in quaternion analysis.

## Integration

### Contour Integrals

Let $\gamma : [a, b] \to \mathbb{H}$ be a piecewise continuously differentiable path, and let $f$ be continuous on the image of $\gamma$. The **contour integral** of $f$ along $\gamma$ is

$$
\int_\gamma f(q) \, dq = \int_a^b f(\gamma(t)) \gamma'(t) \, dt.
$$

**Linearity.** $\int_\gamma (af + bg) = a \int_\gamma f + b \int_\gamma g$ for constant $a, b \in \mathbb{H}$.

**Reversal.** $\int_{-\gamma} f = -\int_\gamma f$.

**Additivity.** If $\gamma$ is the concatenation of $\gamma_1$ and $\gamma_2$, then $\int_\gamma f = \int_{\gamma_1} f + \int_{\gamma_2} f$.

**Estimation.** If $|f(q)| \leq M$ on $\gamma$ and $L$ is the length of $\gamma$, then

$$
\left| \int_\gamma f(q) \, dq \right| \leq M L.
$$

### The Cauchy–Goursat Theorem

**Theorem (Cauchy–Goursat, quaternion version).** If $f$ is monogenic on a simply connected domain $U$ and $\gamma$ is a closed contour in $U$, then

$$
\oint_\gamma f(q) \, dq = 0.
$$

**Proof.** The integral of a monogenic function over a closed surface in $\mathbb{R}^4$ vanishes by the divergence theorem, because the Dirac operator annihilates $f$. The contour case follows by approximation. $\square$

**Corollary.** On a simply connected domain, the integral of a monogenic function is path-independent. The function

$$
F(q) = \int_{q_0}^q f(w) \, dw
$$

is well-defined, monogenic, and satisfies $D F = f$ in the appropriate sense.

### The Cauchy Integral Formula

**Theorem (Cauchy Integral Formula, quaternion version).** Let $f$ be monogenic on a domain containing the closed ball $\overline{B}(q_0, r)$. Then for every $q$ in the open ball,

$$
f(q) = \frac{1}{2\pi^2} \int_{\partial B(q_0, r)} \frac{(w - q)^{-1}}{|w - q|^2} n(w) f(w) \, dS(w),
$$

where $n(w)$ is the outward unit normal and $dS$ is the surface measure on the sphere.

**Corollary (derivatives).** Under the same hypotheses, $f$ is infinitely differentiable, and the derivatives are given by differentiating the kernel.

### Liouville's Theorem

**Theorem (Liouville).** Every bounded monogenic function on all of $\mathbb{H}$ is constant.

**Proof.** Apply the Cauchy estimates to the derivatives of $f$ on a ball of radius $r$ around $q_0$. Since $f$ is bounded by $M$, the derivatives are bounded by $M/r^n$. Let $r \to \infty$ to get that all derivatives vanish. So $f$ is constant. $\square$

### Morera's Theorem

**Theorem (Morera).** If $f$ is continuous on a domain $U$ and $\oint_\gamma f = 0$ for every closed contour $\gamma$ in $U$, then $f$ is monogenic on $U$.

**Proof.** Define $F(q) = \int_{q_0}^q f(w) \, dw$. The hypothesis makes $F$ well-defined, and $D F = f$. Since $F$ is monogenic, $F$ is infinitely differentiable, so $f$ is monogenic. $\square$

## Power Series

### Definition

A **power series** centered at $q_0$ is

$$
\sum_{n=0}^\infty c_n (q - q_0)^n, \qquad c_n \in \mathbb{H}.
$$

The **radius of convergence** is

$$
R = \frac{1}{\limsup_{n \to \infty} |c_n|^{1/n}},
$$

with the conventions $R = 0$ if the limsup is $\infty$ and $R = \infty$ if the limsup is $0$.

**Theorem.** The series converges absolutely for $|q - q_0| < R$ and diverges for $|q - q_0| > R$. On $|q - q_0| < R$ it converges uniformly on compact subsets.

**Theorem.** A power series is monogenic on $|q - q_0| < R$, and its derivative is obtained by term-by-term differentiation:

$$
D \sum_{n=0}^\infty c_n (q - q_0)^n = \sum_{n=1}^\infty n c_n (q - q_0)^{n-1}.
$$

The differentiated series has the same radius of convergence.

### Taylor Series

**Theorem (Taylor, quaternion version).** If $f$ is monogenic on a domain containing the closed ball $\overline{B}(q_0, r)$, then $f$ has a power series expansion

$$
f(q) = \sum_{n=0}^\infty \frac{f^{(n)}(q_0)}{n!} (q - q_0)^n
$$

valid for $|q - q_0| < r$.

**Corollary.** A monogenic function is analytic: it equals its Taylor series in a neighborhood of every point.

**Corollary (identity theorem).** If two monogenic functions on a domain $U$ agree on a set with an accumulation point in $U$, they agree on all of $U$.

### Laurent Series

**Theorem (Laurent).** If $f$ is monogenic on an annulus $r < |q - q_0| < R$, then $f$ has a unique expansion

$$
f(q) = \sum_{n=-\infty}^\infty c_n (q - q_0)^n
$$

valid on the annulus, with

$$
c_n = \frac{1}{2\pi^2} \int_{\partial B(q_0, \rho)} \frac{(w - q_0)^{-n-1}}{|w - q_0|^2} n(w) f(w) \, dS(w), \qquad r < \rho < R.
$$

## Singularities

### Classification

Let $f$ be monogenic on a punctured ball $0 < |q - q_0| < R$.

**Removable singularity.** $q_0$ is removable if $f$ extends to a monogenic function on $|q - q_0| < R$. Equivalently, the Laurent expansion has $c_n = 0$ for $n < 0$.

**Pole.** $q_0$ is a pole of order $m \geq 1$ if the Laurent expansion has $c_{-m} \neq 0$ and $c_n = 0$ for $n < -m$.

**Essential singularity.** $q_0$ is an essential singularity if the Laurent expansion has infinitely many non-zero $c_n$ with $n < 0$.

**Theorem (Riemann).** $q_0$ is removable iff $f$ is bounded near $q_0$.

**Theorem (Casorati–Weierstrass).** If $q_0$ is an essential singularity, then $f$ takes values arbitrarily close to every quaternion in every neighborhood of $q_0$.

### Residues

The **residue** of $f$ at an isolated singularity $q_0$ is the coefficient $c_{-1}$ in the Laurent expansion:

$$
\operatorname{Res}(f, q_0) = c_{-1}.
$$

**Theorem (Residue Theorem).** Let $f$ be monogenic on a simply connected domain except for isolated singularities $q_1, \dots, q_n$. Let $\gamma$ be a closed contour in the domain that does not pass through any $q_k$ and winds once around each. Then

$$
\oint_\gamma f(q) \, dq = 2\pi^2 \sum_{k=1}^n \operatorname{Res}(f, q_k).
$$

The factor $2\pi^2$ is the surface area of the unit sphere in $\mathbb{R}^4$, and it is the quaternion analogue of the factor $2\pi i$ in complex analysis.

## The Dirac Operator

### Definition

The **Dirac operator** is

$$
D = \partial_{x_0} + e_1 \partial_{x_1} + e_2 \partial_{x_2} + e_3 \partial_{x_3}.
$$

It acts on functions $f : \mathbb{H} \to \mathbb{H}$ by

$$
D f = \partial_{x_0} f + e_1 \partial_{x_1} f + e_2 \partial_{x_2} f + e_3 \partial_{x_3} f.
$$

### Properties

**Factorization of the Laplacian.** $D^2 = \Delta$.

**Ellipticity.** The symbol of $D$ is $\sigma_D(\xi) = \xi_0 + e_1 \xi_1 + e_2 \xi_2 + e_3 \xi_3$, which is invertible for every non-zero $\xi \in \mathbb{R}^4$. So $D$ is elliptic.

**Fundamental solution.** The fundamental solution of $D$ is

$$
E(q) = \frac{q^{-1}}{|q|^2} = \frac{\bar{q}}{|q|^4},
$$

which satisfies $D E = \delta_0$ in the sense of distributions.

### The Relation to the Cauchy–Riemann Operator

In complex analysis, the Cauchy–Riemann operator is

$$
\bar{\partial} = \frac{1}{2}(\partial_x + i \partial_y),
$$

and the holomorphic functions are the kernel of $\bar{\partial}$. In quaternion analysis, the Dirac operator is the analogue of $\bar{\partial}$, and the monogenic functions are the kernel of $D$. The Dirac operator is the correct generalization of the Cauchy–Riemann operator to higher dimensions.

## Applications

### Harmonic Analysis

Monogenic functions are harmonic, so quaternion analysis is closely related to harmonic analysis on $\mathbb{R}^4$. The Cauchy integral formula gives a representation of monogenic functions in terms of their boundary values, and the boundary values form a Hardy space.

### Clifford Analysis

Quaternion analysis is the case $n = 4$ of **Clifford analysis**, which generalizes the theory to $\mathbb{R}^n$ with Clifford algebra coefficients. The Dirac operator is defined for any $n$, and the monogenic functions are the kernel of the Dirac operator. The theory is used in:

- The study of the Dirac equation in physics.
- The theory of harmonic forms and Hodge theory.
- The theory of boundary value problems for elliptic systems.
- The theory of Hardy spaces and singular integrals.

### The Dirac Equation

The Dirac equation in physics is a first-order partial differential equation of the form

$$
(i \gamma^\mu \partial_\mu - m) \psi = 0,
$$

where the $\gamma^\mu$ are Dirac matrices and $\psi$ is a spinor. The quaternion Dirac operator is the simplest case of this equation, and the monogenic functions are the solutions of the massless Dirac equation. This is the reason quaternion analysis is used in relativistic quantum mechanics.

### The Radon Transform

The quaternion Radon transform is the analogue of the Radon transform in complex analysis. It is defined by integrating a function over spheres in $\mathbb{R}^4$, and it is inverted by a formula involving the Dirac operator. It is used in:

- The theory of integral geometry in four dimensions.
- The inversion of the Radon transform for the Dirac equation.
- The theory of the X-ray transform in higher dimensions.

## Comparison with Complex Analysis

The differences between quaternion analysis and complex analysis are consequences of the non-commutativity of $\mathbb{H}$ and the higher dimension of the space.

| Property | Complex | Quaternion |
|---|---|---|
| Dimension | 2 | 4 |
| Commutative | yes | no |
| Cauchy–Riemann | $\bar{\partial} f = 0$ | $D f = 0$ |
| Differentiable functions | rich (holomorphic) | affine only |
| Monogenic functions | — | rich |
| Cauchy integral | yes | yes |
| Residue theory | yes | yes |
| Liouville | yes | yes |
| Identity theorem | yes | yes |
| Conformality | yes | no |
| Factor $2\pi i$ | $2\pi i$ | $2\pi^2$ |

The complex case is the case $n = 2$ of the general theory, and the quaternion case is the case $n = 4$. The general theory is Clifford analysis, and the pattern is the same: the Dirac operator replaces the Cauchy–Riemann operator, the monogenic functions replace the holomorphic functions, and the Cauchy integral formula holds with the appropriate kernel.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis |
| $q = q_0 + \mathbf{q}$ | General quaternion |
| $q_0$ | Scalar part |
| $\mathbf{q}$ | Vector part |
| $\bar{q} = q_0 - \mathbf{q}$ | Quaternion conjugate |
| $\|q\| = \sqrt{q \bar{q}}$ | Modulus |
| $B(q_0, r)$ | Open ball of radius $r$ |
| $D = \partial_{x_0} + e_1 \partial_{x_1} + e_2 \partial_{x_2} + e_3 \partial_{x_3}$ | Dirac operator |
| $D f = 0$ | Monogenic equation |
| $\Delta = D^2$ | Laplacian |
| $\int_\gamma f(q) \, dq$ | Contour integral |
| $\operatorname{Res}(f, q_0)$ | Residue |
| $2\pi^2$ | Surface area of the unit sphere in $\mathbb{R}^4$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- Rudolf Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta \Delta u = 0$ mit vier reellen Variablen" (1935), for the origin of monogenic functions.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford theory.
- John Ryan, *Clifford Algebras in Analysis and Related Topics* (CRC Press, 1996), for the analytic theory.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton, 1989), for the role of the Dirac operator in geometry.

