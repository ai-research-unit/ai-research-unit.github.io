# __Complex Analysis__

## Introduction

This article introduces complex analysis as the study of differentiable functions of a complex variable. The goal is to define the core objects precisely, establish their basic properties, and describe the theorems that give the subject its shape.

The treatment is mathematically honest: every claim is either proved or stated as a definition. The complex plane is used as the ambient space, convergence is defined in terms of the modulus, and the consequences of complex differentiability are developed systematically. The complex algebra is not re-derived; it is assumed as the coefficient field. The exponential is not introduced here; it belongs to the article on special functions.

## The Complex Plane

### Points and Distance

A complex number is written

$$
z = x + iy, \qquad x, y \in \mathbb{R},
$$

where $i^2 = -1$. The real number $x$ is the **real part**, and $y$ is the **imaginary part**. We write $x = \operatorname{Re} z$ and $y = \operatorname{Im} z$.

The **modulus** of $z$ is

$$
|z| = \sqrt{x^2 + y^2},
$$

and the **distance** between two complex numbers $z$ and $w$ is

$$
d(z, w) = |z - w|.
$$

This makes $\mathbb{C}$ a metric space isometric to $\mathbb{R}^2$. The modulus satisfies

$$
|z w| = |z| |w|, \qquad |z + w| \leq |z| + |w|, \qquad |\operatorname{Re} z| \leq |z|, \qquad |\operatorname{Im} z| \leq |z|.
$$

The last two inequalities are used constantly: they say that convergence of complex numbers is equivalent to convergence of real and imaginary parts.

### Balls and Neighborhoods

The **open ball** of radius $r > 0$ centered at $z_0$ is

$$
B(z_0, r) = \{z \in \mathbb{C} : |z - z_0| < r\}.
$$

It is an open disk. The **closed ball** is

$$
\overline{B}(z_0, r) = \{z \in \mathbb{C} : |z - z_0| \leq r\}.
$$

A **neighborhood** of $z_0$ is any set containing some $B(z_0, r)$.

### Open and Closed Sets

A set $U \subseteq \mathbb{C}$ is **open** if for every $z_0 \in U$ there exists $r > 0$ with $B(z_0, r) \subseteq U$.

A set $F \subseteq \mathbb{C}$ is **closed** if its complement $\mathbb{C} \setminus F$ is open.

Arbitrary unions of open sets are open. Finite intersections of open sets are open. Dually, arbitrary intersections of closed sets are closed. Finite unions of closed sets are closed.

**Theorem.** A set $F$ is closed iff every convergent sequence in $F$ has its limit in $F$.

### Connectedness and Domains

A set $U \subseteq \mathbb{C}$ is **connected** if it cannot be written as the disjoint union of two non-empty sets open in $U$. It is **path-connected** if any two points can be joined by a continuous path in $U$. For open subsets of $\mathbb{C}$, connectedness and path-connectedness are equivalent.

A **domain** is a non-empty open connected subset of $\mathbb{C}$. Domains are the natural setting for complex analysis, because differentiability on a domain imposes strong global constraints.

### Compactness

A set $K \subseteq \mathbb{C}$ is **compact** if every open cover of $K$ has a finite subcover.

**Theorem (Heine–Borel).** A subset of $\mathbb{C}$ is compact iff it is closed and bounded.

**Theorem.** A continuous complex-valued function on a compact set is bounded and attains its maximum and minimum modulus.

## Limits and Continuity

### Limits of Sequences

A sequence $(z_n)$ of complex numbers **converges** to $L \in \mathbb{C}$ if for every $\epsilon > 0$ there exists $N \in \mathbb{N}$ such that

$$
n \geq N \implies |z_n - L| < \epsilon.
$$

We write $z_n \to L$ or $\lim_{n \to \infty} z_n = L$.

**Uniqueness.** If $z_n \to L$ and $z_n \to L'$, then $L = L'$.

**Componentwise convergence.** Write $z_n = x_n + i y_n$ and $L = a + i b$. Then

$$
z_n \to L \iff x_n \to a \text{ and } y_n \to b.
$$

This is the reason complex convergence is no harder than real convergence: it is two real convergences in parallel.

**Boundedness.** Every convergent sequence is bounded. The converse fails.

**Algebra of limits.** If $z_n \to L$ and $w_n \to M$, then

$$
z_n + w_n \to L + M, \qquad z_n w_n \to L M, \qquad \frac{z_n}{w_n} \to \frac{L}{M} \text{ if } M \neq 0.
$$

### Cauchy Sequences

A sequence $(z_n)$ is **Cauchy** if for every $\epsilon > 0$ there exists $N \in \mathbb{N}$ such that

$$
m, n \geq N \implies |z_m - z_n| < \epsilon.
$$

**Theorem.** In $\mathbb{C}$, a sequence converges iff it is Cauchy. This is the completeness of $\mathbb{C}$ as a metric space. It follows from the completeness of $\mathbb{R}$ applied to the real and imaginary parts.

### Limits of Functions

Let $f : D \to \mathbb{C}$ with $D \subseteq \mathbb{C}$, and let $z_0$ be a limit point of $D$. We say

$$
\lim_{z \to z_0} f(z) = L
$$

if for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
z \in D, \; 0 < |z - z_0| < \delta \implies |f(z) - L| < \epsilon.
$$

**Uniqueness.** If the limit exists, it is unique.

**Sequential criterion.** $\lim_{z \to z_0} f(z) = L$ iff for every sequence $(z_n)$ in $D \setminus \{z_0\}$ with $z_n \to z_0$, we have $f(z_n) \to L$.

**Algebra of limits.** Sums, products, and quotients (where defined) of limits are the limits of the sums, products, and quotients.

### Continuity

A function $f : D \to \mathbb{C}$ is **continuous at** $z_0 \in D$ if $\lim_{z \to z_0} f(z) = f(z_0)$ when $z_0$ is a limit point of $D$; a point of $D$ that is isolated in $D$ is a point of continuity by convention. Equivalently, and in a form that covers isolated points as well, for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
z \in D, \; |z - z_0| < \delta \implies |f(z) - f(z_0)| < \epsilon.
$$

$f$ is **continuous on** $D$ if it is continuous at every point of $D$.

**Theorem.** $f$ is continuous at $z_0$ iff for every sequence $(z_n)$ in $D$ with $z_n \to z_0$, we have $f(z_n) \to f(z_0)$.

**Theorem.** Sums, products, and quotients (where defined) of continuous functions are continuous. Compositions of continuous functions are continuous.

**Theorem.** $f$ is continuous iff the preimage of every open set is open. Equivalently, the preimage of every closed set is closed.

**Componentwise continuity.** Write $f(z) = u(x, y) + i v(x, y)$. Then $f$ is continuous at $z_0 = x_0 + i y_0$ iff $u$ and $v$ are continuous at $(x_0, y_0)$. This reduces complex continuity to real continuity of two functions of two variables.

### Uniform Continuity

A function $f : D \to \mathbb{C}$ is **uniformly continuous** if for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
z, w \in D, \; |z - w| < \delta \implies |f(z) - f(w)| < \epsilon.
$$

The difference from ordinary continuity is that $\delta$ depends only on $\epsilon$, not on the point.

**Theorem.** A continuous function on a compact set is uniformly continuous.

## Complex Differentiability

### The Derivative

Let $f : U \to \mathbb{C}$ with $U$ open, and let $z_0 \in U$. The **derivative** of $f$ at $z_0$ is

$$
f'(z_0) = \lim_{h \to 0} \frac{f(z_0 + h) - f(z_0)}{h},
$$

provided the limit exists. If it does, $f$ is **complex differentiable** at $z_0$, or **holomorphic** at $z_0$.

The limit is taken in the complex plane, so $h$ can approach $0$ from any direction. This is a much stronger condition than real differentiability: the difference quotient must tend to the same limit along every path.

**Theorem.** Holomorphic implies continuous. The converse fails.

### The Cauchy–Riemann Equations

Write $f(z) = u(x, y) + i v(x, y)$, where $z = x + iy$ and $u, v : U \to \mathbb{R}$.

**Theorem.** $f$ is holomorphic at $z_0 = x_0 + i y_0$ iff $u$ and $v$ are real differentiable at $(x_0, y_0)$ and satisfy the **Cauchy–Riemann equations**

$$
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \qquad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}.
$$

**Proof.** Write $h = h_1 + i h_2$. The difference quotient is

$$
\frac{f(z_0 + h) - f(z_0)}{h} = \frac{(u_x h_1 + u_y h_2) + i (v_x h_1 + v_y h_2)}{h_1 + i h_2} + o(1).
$$

For the limit to exist independently of the direction of $h$, the numerator must be a complex multiple of $h$. This forces the Cauchy–Riemann equations. $\square$

**Corollary.** If $f$ is holomorphic, then $u$ and $v$ are harmonic:

$$
\Delta u = 0, \qquad \Delta v = 0.
$$

**Proof.** Differentiate the Cauchy–Riemann equations and use the equality of mixed partials. $\square$

### The Wirtinger Derivatives

Define the **Wirtinger derivatives**

$$
\frac{\partial}{\partial z} = \frac{1}{2}\left( \frac{\partial}{\partial x} - i \frac{\partial}{\partial y} \right), \qquad \frac{\partial}{\partial \bar{z}} = \frac{1}{2}\left( \frac{\partial}{\partial x} + i \frac{\partial}{\partial y} \right).
$$

**Theorem.** $f$ is holomorphic iff $f$ is real differentiable and $\partial f / \partial \bar{z} = 0$. In that case,

$$
f'(z) = \frac{\partial f}{\partial z}.
$$

The condition $\partial f / \partial \bar{z} = 0$ is the Cauchy–Riemann equations in compact form.

### Rules of Differentiation

**Linearity.** $(af + bg)' = a f' + b g'$.

**Product rule.** $(fg)' = f' g + f g'$.

**Quotient rule.** $(f/g)' = (f' g - f g')/g^2$ where $g \neq 0$.

**Chain rule.** $(f \circ g)'(z) = f'(g(z)) g'(z)$.

**Inverse function rule.** If $f$ is holomorphic at $z_0$ with $f'(z_0) \neq 0$ and $f^{-1}$ is defined near $f(z_0)$, then

$$
(f^{-1})'(f(z_0)) = \frac{1}{f'(z_0)}.
$$

## Conformal Maps

### Definition

A map $f : U \to \mathbb{C}$ is **conformal** at $z_0$ if it preserves angles between curves through $z_0$. In particular, if $f$ is holomorphic at $z_0$ with $f'(z_0) \neq 0$, then $f$ is conformal at $z_0$.

**Theorem.** If $f$ is holomorphic at $z_0$ with $f'(z_0) \neq 0$, then $f$ is conformal at $z_0$, and the local behavior of $f$ near $z_0$ is multiplication by $f'(z_0)$, i.e., a rotation by $\arg f'(z_0)$ and a scaling by $|f'(z_0)|$.

**Proof.** Write $f(z) - f(z_0) = f'(z_0)(z - z_0) + o(|z - z_0|)$. The linear term is multiplication by $f'(z_0)$, which is a rotation and a scaling. $\square$

### Möbius Transformations

A **Möbius transformation** is a map of the form

$$
f(z) = \frac{az + b}{cz + d}, \qquad ad - bc \neq 0.
$$

It is holomorphic on $\mathbb{C} \setminus \{-d/c\}$ when $c \neq 0$, and entire when $c = 0$; it is conformal wherever $f'(z) \neq 0$. Möbius transformations map circles and lines to circles and lines, and they form a group under composition.

### The Riemann Mapping Theorem

**Theorem (Riemann Mapping).** Let $U \subsetneq \mathbb{C}$ be a simply connected domain. Then there exists a biholomorphic map $f : U \to B(0, 1)$.

The map is unique up to composition with a Möbius transformation of the disk.

## Integration

### Contour Integrals

Let $\gamma : [a, b] \to \mathbb{C}$ be a piecewise continuously differentiable path, and let $f$ be continuous on the image of $\gamma$. The **contour integral** of $f$ along $\gamma$ is

$$
\int_\gamma f(z) \, dz = \int_a^b f(\gamma(t)) \gamma'(t) \, dt.
$$

**Linearity.** $\int_\gamma (af + bg) = a \int_\gamma f + b \int_\gamma g$.

**Reversal.** $\int_{-\gamma} f = -\int_\gamma f$.

**Additivity.** If $\gamma$ is the concatenation of $\gamma_1$ and $\gamma_2$, then $\int_\gamma f = \int_{\gamma_1} f + \int_{\gamma_2} f$.

**Estimation.** If $|f(z)| \leq M$ on $\gamma$ and $L$ is the length of $\gamma$, then

$$
\left| \int_\gamma f(z) \, dz \right| \leq M L.
$$

### The Cauchy–Goursat Theorem

**Theorem (Cauchy–Goursat).** If $f$ is holomorphic on a simply connected domain $U$ and $\gamma$ is a closed contour in $U$, then

$$
\oint_\gamma f(z) \, dz = 0.
$$

**Proof.** For a triangle, subdivide repeatedly and use the fact that the integral over the small triangles is bounded by the area times the supremum of $|f'|$. For a general contour, approximate by polygons. $\square$

**Corollary.** On a simply connected domain, the integral of a holomorphic function is path-independent. The function

$$
F(z) = \int_{z_0}^z f(w) \, dw
$$

is well-defined, holomorphic, and satisfies $F' = f$.

### The Cauchy Integral Formula

**Theorem (Cauchy Integral Formula).** Let $f$ be holomorphic on a domain containing the closed disk $\overline{B}(z_0, r)$. Then for every $z$ in the open disk,

$$
f(z) = \frac{1}{2\pi i} \oint_{|w - z_0| = r} \frac{f(w)}{w - z} \, dw.
$$

**Proof.** Apply the Cauchy–Goursat theorem to the function $g(w) = (f(w) - f(z))/(w - z)$ on the punctured disk, then let the radius of the small circle around $z$ tend to zero. $\square$

**Corollary (derivatives).** Under the same hypotheses, $f$ is infinitely differentiable, and

$$
f^{(n)}(z) = \frac{n!}{2\pi i} \oint_{|w - z_0| = r} \frac{f(w)}{(w - z)^{n+1}} \, dw.
$$

**Corollary (Cauchy estimates).** If $|f| \leq M$ on $|w - z_0| = r$, then

$$
|f^{(n)}(z_0)| \leq \frac{n! M}{r^n}.
$$

### Liouville's Theorem

**Theorem (Liouville).** Every bounded entire function is constant.

**Proof.** Apply the Cauchy estimates to $f'$ on a circle of radius $r$ around $z_0$. Since $f$ is bounded by $M$, we have $|f'(z_0)| \leq M/r$ for every $r > 0$. Let $r \to \infty$ to get $f'(z_0) = 0$. Since $z_0$ is arbitrary, $f' = 0$ everywhere, so $f$ is constant. $\square$

**Corollary (Fundamental Theorem of Algebra).** Every non-constant polynomial with complex coefficients has a root in $\mathbb{C}$.

**Proof.** If $p$ has no root, then $1/p$ is entire and bounded (since $|p(z)| \to \infty$ as $|z| \to \infty$), hence constant by Liouville. Contradiction. $\square$

### Morera's Theorem

**Theorem (Morera).** If $f$ is continuous on a domain $U$ and $\oint_\gamma f = 0$ for every closed contour $\gamma$ in $U$, then $f$ is holomorphic on $U$.

**Proof.** Define $F(z) = \int_{z_0}^z f(w) \, dw$. The hypothesis makes $F$ well-defined, and $F' = f$. Since $F$ is holomorphic, $F$ is infinitely differentiable, so $f$ is holomorphic. $\square$

## Series Representations

### Power Series

A **power series** centered at $z_0$ is

$$
\sum_{n=0}^\infty c_n (z - z_0)^n, \qquad c_n \in \mathbb{C}.
$$

The **radius of convergence** is

$$
R = \frac{1}{\limsup_{n \to \infty} |c_n|^{1/n}},
$$

with the conventions $R = 0$ if the limsup is $\infty$ and $R = \infty$ if the limsup is $0$.

**Theorem.** The series converges absolutely for $|z - z_0| < R$ and diverges for $|z - z_0| > R$. On $|z - z_0| < R$ it converges uniformly on compact subsets.

**Theorem.** A power series is holomorphic on $|z - z_0| < R$, and its derivative is obtained by term-by-term differentiation:

$$
\frac{d}{dz} \sum_{n=0}^\infty c_n (z - z_0)^n = \sum_{n=1}^\infty n c_n (z - z_0)^{n-1}.
$$

The differentiated series has the same radius of convergence.

### Taylor Series

**Theorem (Taylor).** If $f$ is holomorphic on a domain containing the closed disk $\overline{B}(z_0, r)$, then $f$ has a power series expansion

$$
f(z) = \sum_{n=0}^\infty \frac{f^{(n)}(z_0)}{n!} (z - z_0)^n
$$

valid for $|z - z_0| < r$.

**Proof.** Use the Cauchy integral formula and expand $1/(w - z)$ as a geometric series in $(z - z_0)/(w - z_0)$. $\square$

**Corollary.** A holomorphic function is analytic: it equals its Taylor series in a neighborhood of every point.

**Corollary (identity theorem).** If two holomorphic functions on a domain $U$ agree on a set with an accumulation point in $U$, they agree on all of $U$.

### Laurent Series

**Theorem (Laurent).** If $f$ is holomorphic on an annulus $r < |z - z_0| < R$, then $f$ has a unique expansion

$$
f(z) = \sum_{n=-\infty}^\infty c_n (z - z_0)^n
$$

valid on the annulus, with

$$
c_n = \frac{1}{2\pi i} \oint_{|w - z_0| = \rho} \frac{f(w)}{(w - z_0)^{n+1}} \, dw, \qquad r < \rho < R.
$$

**Proof.** Apply the Cauchy integral formula on the annulus and expand the kernel in two geometric series, one for the inner boundary and one for the outer boundary. $\square$

## Singularities

### Classification

Let $f$ be holomorphic on a punctured disk $0 < |z - z_0| < R$.

**Removable singularity.** $z_0$ is removable if $f$ extends to a holomorphic function on $|z - z_0| < R$. Equivalently, the Laurent expansion has $c_n = 0$ for $n < 0$.

**Pole.** $z_0$ is a pole of order $m \geq 1$ if the Laurent expansion has $c_{-m} \neq 0$ and $c_n = 0$ for $n < -m$.

**Essential singularity.** $z_0$ is an essential singularity if the Laurent expansion has infinitely many non-zero $c_n$ with $n < 0$.

**Theorem (Riemann).** $z_0$ is removable iff $f$ is bounded near $z_0$.

**Theorem (Casorati–Weierstrass).** If $z_0$ is an essential singularity, then $f$ takes values arbitrarily close to every complex number in every neighborhood of $z_0$.

**Theorem (Picard).** If $z_0$ is an essential singularity, then $f$ takes every complex value, with at most one exception, in every punctured neighborhood of $z_0$.

### Residues

The **residue** of $f$ at an isolated singularity $z_0$ is the coefficient $c_{-1}$ in the Laurent expansion:

$$
\operatorname{Res}(f, z_0) = c_{-1} = \frac{1}{2\pi i} \oint_{|z - z_0| = \rho} f(z) \, dz.
$$

**Theorem (Residue Theorem).** Let $f$ be holomorphic on a simply connected domain except for isolated singularities $z_1, \dots, z_n$. Let $\gamma$ be a closed contour in the domain that does not pass through any $z_k$ and winds once around each. Then

$$
\oint_\gamma f(z) \, dz = 2\pi i \sum_{k=1}^n \operatorname{Res}(f, z_k).
$$

**Proof.** Apply the Cauchy–Goursat theorem to the domain with small disks removed around each singularity, then use the definition of the residue. $\square$

### Computation of Residues

**Simple pole.** If $f(z) = g(z)/h(z)$ with $g(z_0) \neq 0$, $h(z_0) = 0$, and $h'(z_0) \neq 0$, then

$$
\operatorname{Res}(f, z_0) = \frac{g(z_0)}{h'(z_0)}.
$$

**Pole of order $m$.** If $f$ has a pole of order $m$ at $z_0$, then

$$
\operatorname{Res}(f, z_0) = \frac{1}{(m-1)!} \lim_{z \to z_0} \frac{d^{m-1}}{dz^{m-1}} \left[ (z - z_0)^m f(z) \right].
$$

## Applications of the Residue Theorem

### Evaluation of Real Integrals

**Integrals of trigonometric functions.** For an integral of the form

$$
\int_0^{2\pi} R(\cos\theta, \sin\theta) \, d\theta,
$$

substitute $z = e^{i\theta}$, so that $\cos\theta = (z + z^{-1})/2$, $\sin\theta = (z - z^{-1})/(2i)$, and $d\theta = dz/(iz)$. The integral becomes a contour integral over the unit circle, evaluated by residues.

**Integrals over the real line.** For an integral of the form

$$
\int_{-\infty}^\infty f(x) \, dx,
$$

where $f$ is a rational function decaying faster than $1/|x|$ at infinity with no poles on the real axis, close the contour in the upper half-plane and use the residue theorem.

**Integrals with trigonometric kernels.** For an integral of the form

$$
\int_{-\infty}^\infty f(x) e^{iax} \, dx, \qquad a > 0,
$$

where $f$ is a rational function decaying at infinity with no poles on the real axis, use the same contour as above, with **Jordan's lemma** controlling the contribution from the semicircle.

### The Argument Principle

**Theorem (Argument Principle).** Let $f$ be meromorphic on a simply connected domain with zeros $z_1, \dots, z_m$ and poles $p_1, \dots, p_n$ (counted with multiplicity). Let $\gamma$ be a closed contour that winds once around each and does not pass through any. Then

$$
\frac{1}{2\pi i} \oint_\gamma \frac{f'(z)}{f(z)} \, dz = \sum_{k=1}^m \operatorname{ord}(f, z_k) - \sum_{k=1}^n \operatorname{ord}(f, p_k),
$$

where $\operatorname{ord}(f, z_k)$ is the order of the zero and $\operatorname{ord}(f, p_k)$ is the order of the pole.

**Interpretation.** The integral counts the winding number of $f(\gamma)$ around the origin, which equals the number of zeros minus the number of poles enclosed by $\gamma$.

### Rouché's Theorem

**Theorem (Rouché).** Let $f$ and $g$ be holomorphic on a simply connected domain, and let $\gamma$ be a closed contour such that $|g(z)| < |f(z)|$ on $\gamma$. Then $f$ and $f + g$ have the same number of zeros inside $\gamma$, counted with multiplicity.

**Proof.** Apply the argument principle to $f + tg$ for $t \in [0, 1]$ and note that the number of zeros is a continuous integer-valued function of $t$. $\square$

**Corollary (Fundamental Theorem of Algebra, again).** Every polynomial of degree $n \geq 1$ has exactly $n$ roots in $\mathbb{C}$, counted with multiplicity.

**Proof.** Write $p(z) = a_n z^n + \dots + a_0$. On a large circle, $|a_n z^n| > |a_{n-1} z^{n-1} + \dots + a_0|$, so by Rouché, $p$ has the same number of zeros as $a_n z^n$, which is $n$. $\square$

## Summary

Complex analysis is the study of complex-valued functions of a complex variable that possess a derivative in the complex sense. The plane carries the modulus $\lvert z\rvert = \sqrt{x^2 + y^2}$, and with it the distance, the convergent sequences, the continuous functions and the open sets on which the subject is built.

The derivative $f'(z_0) = \lim_{h \to 0} (f(z_0 + h) - f(z_0))/h$ is the central object, and the article records how much stronger it is than its real analogue: a function that has it at every point of an open set is holomorphic, holomorphy is equivalent to the Cauchy–Riemann equations, and it forces the function to be analytic. Where the derivative is nonzero the map is conformal, preserving the angles between curves.

Integration along paths defines the contour integral, and the theorems the derivative buys are the substance of the subject: Cauchy's theorem, the Cauchy integral formula, the Liouville theorem, and the residue theorem, which evaluates an integral by summing the local contributions of the singularities. Power series, Taylor series and Laurent series describe the local behaviour of a holomorphic function, and the Laurent expansion classifies the isolated singularities as removable, a pole, or essential. The article closes by applying the residue theorem to the evaluation of real integrals.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}$ | Complex plane |
| $z = x + iy$ | General complex number |
| $\bar{z} = x - iy$ | Complex conjugate |
| $\|z\| = \sqrt{x^2 + y^2}$ | Modulus |
| $d(z, w) = \|z - w\|$ | Distance |
| $B(z_0, r)$ | Open disk of radius $r$ |
| $U, F, K$ | Open, closed, compact sets |
| $z_n \to L$ | Convergence of a sequence |
| $\lim_{z \to z_0} f(z)$ | Limit of a function |
| $f'(z)$ | Complex derivative |
| $\partial/\partial z, \partial/\partial \bar{z}$ | Wirtinger derivatives |
| $\int_\gamma f(z) \, dz$ | Contour integral |
| $f^{(n)}(z)$ | $n$-th derivative |
| $\sum c_n (z - z_0)^n$ | Power series |
| $\operatorname{Res}(f, z_0)$ | Residue |
| $\operatorname{ord}(f, z_0)$ | Order of zero or pole |

## Further Reading

- Augustin-Louis Cauchy, *Cours d'analyse* (1821), for the origin of the subject.
- Bernhard Riemann, *Grundlagen für eine allgemeine Theorie der Functionen einer veränderlichen complexen Grösse* (1851), for the geometric viewpoint.
- Lars V. Ahlfors, *Complex Analysis* (McGraw-Hill, 1979), for the standard modern treatment.
- John B. Conway, *Functions of One Complex Variable* (Springer, 1978), for a thorough introduction.
- Walter Rudin, *Real and Complex Analysis* (McGraw-Hill, 1987), for the integration-theoretic perspective.
- Elias M. Stein and Rami Shakarchi, *Complex Analysis* (Princeton, 2003), for a modern treatment with connections to other areas.

