
# __Complex Analysis__

## Introduction

This article introduces complex analysis as the study of differentiable functions of a complex variable. The goal is to define the core objects precisely, establish their basic properties, and describe the theorems that give the subject its shape.

The treatment is mathematically honest: every claim is either proved or stated as a definition. The complex plane is used as the ambient space, convergence is defined in terms of the modulus, and the consequences of complex differentiability are developed systematically. The complex algebra is not re-derived; it is assumed as the coefficient field. The exponential is not introduced here; it belongs to the article on special functions.

## The Complex Plane

### Points and Distance

A complex number is written

$$
A = a + i a', \qquad a, a' \in \mathbb{R},
$$

where $i^2 = -1$. The real number $a$ is the **real part**, and $a'$ is the **imaginary part**. We write $a = \operatorname{Re} A$ and $a' = \operatorname{Im} A$.

The **modulus** of $A$ is

$$
|A| = \sqrt{a^2 + a'^2},
$$

and the **distance** between two complex numbers $A$ and $B$ is

$$
d(A, B) = |A - B|.
$$

This makes $\mathbb{C}$ a metric space isometric to $\mathbb{R}^2$. The modulus satisfies

$$
|A B| = |A| |B|, \qquad |A + B| \leq |A| + |B|, \qquad |\operatorname{Re} A| \leq |A|, \qquad |\operatorname{Im} A| \leq |A|.
$$

The last two inequalities are used constantly: they say that convergence of complex numbers is equivalent to convergence of real and imaginary parts.

### Balls and Neighborhoods

The **open ball** of radius $r > 0$ centered at $A_0$ is

$$
B(A_0, r) = \{A \in \mathbb{C} : |A - A_0| < r\}.
$$

It is an open disk. The **closed ball** is

$$
\overline{B}(A_0, r) = \{A \in \mathbb{C} : |A - A_0| \leq r\}.
$$

A **neighborhood** of $A_0$ is any set containing some $B(A_0, r)$.

### Open and Closed Sets

A set $U \subseteq \mathbb{C}$ is **open** if for every $A_0 \in U$ there exists $r > 0$ with $B(A_0, r) \subseteq U$.

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

A sequence $(A_n)$ of complex numbers **converges** to $L \in \mathbb{C}$ if for every $\epsilon > 0$ there exists $N \in \mathbb{N}$ such that

$$
n \geq N \implies |A_n - L| < \epsilon.
$$

We write $A_n \to L$ or $\lim_{n \to \infty} A_n = L$.

**Uniqueness.** If $A_n \to L$ and $A_n \to L'$, then $L = L'$.

**Componentwise convergence.** Write $A_n = a_n + i a'_n$ and $L = a + i b$. Then

$$
A_n \to L \iff a_n \to a \text{ and } a'_n \to b.
$$

This is the reason complex convergence is no harder than real convergence: it is two real convergences in parallel.

**Boundedness.** Every convergent sequence is bounded. The converse fails.

**Algebra of limits.** If $A_n \to L$ and $B_n \to M$, then

$$
A_n + B_n \to L + M, \qquad A_n B_n \to L M, \qquad \frac{A_n}{B_n} \to \frac{L}{M} \text{ if } M \neq 0.
$$

### Cauchy Sequences

A sequence $(A_n)$ is **Cauchy** if for every $\epsilon > 0$ there exists $N \in \mathbb{N}$ such that

$$
m, n \geq N \implies |A_m - A_n| < \epsilon.
$$

**Theorem.** In $\mathbb{C}$, a sequence converges iff it is Cauchy. This is the completeness of $\mathbb{C}$ as a metric space. It follows from the completeness of $\mathbb{R}$ applied to the real and imaginary parts.

### Limits of Functions

Let $f : D \to \mathbb{C}$ with $D \subseteq \mathbb{C}$, and let $A_0$ be a limit point of $D$. We say

$$
\lim_{A \to A_0} f(A) = L
$$

if for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
A \in D, \; 0 < |A - A_0| < \delta \implies |f(A) - L| < \epsilon.
$$

**Uniqueness.** If the limit exists, it is unique.

**Sequential criterion.** $\lim_{A \to A_0} f(A) = L$ iff for every sequence $(A_n)$ in $D \setminus \{A_0\}$ with $A_n \to A_0$, we have $f(A_n) \to L$.

**Algebra of limits.** Sums, products, and quotients (where defined) of limits are the limits of the sums, products, and quotients.

### Continuity

A function $f : D \to \mathbb{C}$ is **continuous at** $A_0 \in D$ if $\lim_{A \to A_0} f(A) = f(A_0)$ when $A_0$ is a limit point of $D$; a point of $D$ that is isolated in $D$ is a point of continuity by convention. Equivalently, and in a form that covers isolated points as well, for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
A \in D, \; |A - A_0| < \delta \implies |f(A) - f(A_0)| < \epsilon.
$$

$f$ is **continuous on** $D$ if it is continuous at every point of $D$.

**Theorem.** $f$ is continuous at $A_0$ iff for every sequence $(A_n)$ in $D$ with $A_n \to A_0$, we have $f(A_n) \to f(A_0)$.

**Theorem.** Sums, products, and quotients (where defined) of continuous functions are continuous. Compositions of continuous functions are continuous.

**Theorem.** $f$ is continuous iff the preimage of every open set is open. Equivalently, the preimage of every closed set is closed.

**Componentwise continuity.** Write $f(A) = u(a, a') + i v(a, a')$. Then $f$ is continuous at $A_0 = a_0 + i a'_0$ iff $u$ and $v$ are continuous at $(a_0, a'_0)$. This reduces complex continuity to real continuity of two functions of two variables.

### Uniform Continuity

A function $f : D \to \mathbb{C}$ is **uniformly continuous** if for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
A, B \in D, \; |A - B| < \delta \implies |f(A) - f(B)| < \epsilon.
$$

The difference from ordinary continuity is that $\delta$ depends only on $\epsilon$, not on the point.

**Theorem.** A continuous function on a compact set is uniformly continuous.

## Complex Differentiability

### The Derivative

Let $f : U \to \mathbb{C}$ with $U$ open, and let $A_0 \in U$. The **derivative** of $f$ at $A_0$ is

$$
f'(A_0) = \lim_{h \to 0} \frac{f(A_0 + h) - f(A_0)}{h},
$$

provided the limit exists. If it does, $f$ is **complex differentiable** at $A_0$, or **holomorphic** at $A_0$.

The limit is taken in the complex plane, so $h$ can approach $0$ from any direction. This is a much stronger condition than real differentiability: the difference quotient must tend to the same limit along every path.

**Theorem.** Holomorphic implies continuous. The converse fails.

### The Cauchy–Riemann Equations

Write $f(A) = u(a, a') + i v(a, a')$, where $A = a + i a'$ and $u, v : U \to \mathbb{R}$.

**Theorem.** $f$ is holomorphic at $A_0 = a_0 + i a'_0$ iff $u$ and $v$ are real differentiable at $(a_0, a'_0)$ and satisfy the **Cauchy–Riemann equations**

$$
\frac{\partial u}{\partial a} = \frac{\partial v}{\partial a'}, \qquad \frac{\partial u}{\partial a'} = -\frac{\partial v}{\partial a}.
$$

**Proof.** Write $h = h_1 + i h_2$. The difference quotient is

$$
\frac{f(A_0 + h) - f(A_0)}{h} = \frac{(u_a h_1 + u_{a'} h_2) + i (v_a h_1 + v_{a'} h_2)}{h_1 + i h_2} + o(1).
$$

For the limit to exist independently of the direction of $h$, the numerator must be a complex multiple of $h$. This forces the Cauchy–Riemann equations.

**Corollary.** If $f$ is holomorphic, then $u$ and $v$ are harmonic:

$$
\Delta u = 0, \qquad \Delta v = 0.
$$

**Proof.** Differentiate the Cauchy–Riemann equations and use the equality of mixed partials.

### The Wirtinger Derivatives

Define the **Wirtinger derivatives**

$$
\frac{\partial}{\partial A} = \frac{1}{2}\left( \frac{\partial}{\partial a} - i \frac{\partial}{\partial a'} \right), \qquad \frac{\partial}{\partial \bar{A}} = \frac{1}{2}\left( \frac{\partial}{\partial a} + i \frac{\partial}{\partial a'} \right).
$$

**Theorem.** $f$ is holomorphic iff $f$ is real differentiable and $\partial f / \partial \bar{A} = 0$. In that case,

$$
f'(A) = \frac{\partial f}{\partial A}.
$$

The condition $\partial f / \partial \bar{A} = 0$ is the Cauchy–Riemann equations in compact form.

### Rules of Differentiation

**Linearity.** $(af + bg)' = a f' + b g'$.

**Product rule.** $(fg)' = f' g + f g'$.

**Quotient rule.** $(f/g)' = (f' g - f g')/g^2$ where $g \neq 0$.

**Chain rule.** $(f \circ g)'(A) = f'(g(A)) g'(A)$.

**Inverse function rule.** If $f$ is holomorphic at $A_0$ with $f'(A_0) \neq 0$ and $f^{-1}$ is defined near $f(A_0)$, then

$$
(f^{-1})'(f(A_0)) = \frac{1}{f'(A_0)}.
$$

## Conformal Maps

### Definition

A map $f : U \to \mathbb{C}$ is **conformal** at $A_0$ if it preserves angles between curves through $A_0$. In particular, if $f$ is holomorphic at $A_0$ with $f'(A_0) \neq 0$, then $f$ is conformal at $A_0$.

**Theorem.** If $f$ is holomorphic at $A_0$ with $f'(A_0) \neq 0$, then $f$ is conformal at $A_0$, and the local behavior of $f$ near $A_0$ is multiplication by $f'(A_0)$, i.e., a rotation by $\arg f'(A_0)$ and a scaling by $|f'(A_0)|$.

**Proof.** Write $f(A) - f(A_0) = f'(A_0)(A - A_0) + o(|A - A_0|)$. The linear term is multiplication by $f'(A_0)$, which is a rotation and a scaling.

### Möbius Transformations

A **Möbius transformation** is a map of the form

$$
f(A) = \frac{aA + b}{cA + d}, \qquad ad - bc \neq 0.
$$

It is holomorphic on $\mathbb{C} \setminus \{-d/c\}$ when $c \neq 0$, and entire when $c = 0$; it is conformal wherever $f'(A) \neq 0$. Möbius transformations map circles and lines to circles and lines, and they form a group under composition.

### The Riemann Mapping Theorem

**Theorem (Riemann Mapping).** Let $U \subsetneq \mathbb{C}$ be a simply connected domain. Then there exists a biholomorphic map $f : U \to B(0, 1)$.

The map is unique up to composition with a Möbius transformation of the disk.

## Integration

### Contour Integrals

Let $\gamma : [a, b] \to \mathbb{C}$ be a piecewise continuously differentiable path, and let $f$ be continuous on the image of $\gamma$. The **contour integral** of $f$ along $\gamma$ is

$$
\int_\gamma f(A) \, dA = \int_a^b f(\gamma(t)) \gamma'(t) \, dt.
$$

**Linearity.** $\int_\gamma (af + bg) = a \int_\gamma f + b \int_\gamma g$.

**Reversal.** $\int_{-\gamma} f = -\int_\gamma f$.

**Additivity.** If $\gamma$ is the concatenation of $\gamma_1$ and $\gamma_2$, then $\int_\gamma f = \int_{\gamma_1} f + \int_{\gamma_2} f$.

**Estimation.** If $|f(A)| \leq M$ on $\gamma$ and $L$ is the length of $\gamma$, then

$$
\left| \int_\gamma f(A) \, dA \right| \leq M L.
$$

### The Cauchy–Goursat Theorem

**Theorem (Cauchy–Goursat).** If $f$ is holomorphic on a simply connected domain $U$ and $\gamma$ is a closed contour in $U$, then

$$
\oint_\gamma f(A) \, dA = 0.
$$

**Proof.** For a triangle, subdivide repeatedly and use the fact that the integral over the small triangles is bounded by the area times the supremum of $|f'|$. For a general contour, approximate by polygons.

**Corollary.** On a simply connected domain, the integral of a holomorphic function is path-independent. The function

$$
F(A) = \int_{A_0}^A f(B) \, dB
$$

is well-defined, holomorphic, and satisfies $F' = f$.

### The Cauchy Integral Formula

**Theorem (Cauchy Integral Formula).** Let $f$ be holomorphic on a domain containing the closed disk $\overline{B}(A_0, r)$. Then for every $A$ in the open disk,

$$
f(A) = \frac{1}{2\pi i} \oint_{|B - A_0| = r} \frac{f(B)}{B - A} \, dB.
$$

**Proof.** Apply the Cauchy–Goursat theorem to the function $g(B) = (f(B) - f(A))/(B - A)$ on the punctured disk, then let the radius of the small circle around $A$ tend to zero.

**Corollary (derivatives).** Under the same hypotheses, $f$ is infinitely differentiable, and

$$
f^{(n)}(A) = \frac{n!}{2\pi i} \oint_{|B - A_0| = r} \frac{f(B)}{(B - A)^{n+1}} \, dB.
$$

**Corollary (Cauchy estimates).** If $|f| \leq M$ on $|B - A_0| = r$, then

$$
|f^{(n)}(A_0)| \leq \frac{n! M}{r^n}.
$$

### Liouville's Theorem

**Theorem (Liouville).** Every bounded entire function is constant.

**Proof.** Apply the Cauchy estimates to $f'$ on a circle of radius $r$ around $A_0$. Since $f$ is bounded by $M$, we have $|f'(A_0)| \leq M/r$ for every $r > 0$. Let $r \to \infty$ to get $f'(A_0) = 0$. Since $A_0$ is arbitrary, $f' = 0$ everywhere, so $f$ is constant.

**Corollary (Fundamental Theorem of Algebra).** Every non-constant polynomial with complex coefficients has a root in $\mathbb{C}$.

**Proof.** If $p$ has no root, then $1/p$ is entire and bounded (since $|p(A)| \to \infty$ as $|A| \to \infty$), hence constant by Liouville. Contradiction.

### Morera's Theorem

**Theorem (Morera).** If $f$ is continuous on a domain $U$ and $\oint_\gamma f = 0$ for every closed contour $\gamma$ in $U$, then $f$ is holomorphic on $U$.

**Proof.** Define $F(A) = \int_{A_0}^A f(B) \, dB$. The hypothesis makes $F$ well-defined, and $F' = f$. Since $F$ is holomorphic, $F$ is infinitely differentiable, so $f$ is holomorphic.

## Series Representations

### Power Series

A **power series** centered at $A_0$ is

$$
\sum_{n=0}^\infty c_n (A - A_0)^n, \qquad c_n \in \mathbb{C}.
$$

The **radius of convergence** is

$$
R = \frac{1}{\limsup_{n \to \infty} |c_n|^{1/n}},
$$

with the conventions $R = 0$ if the limsup is $\infty$ and $R = \infty$ if the limsup is $0$.

**Theorem.** The series converges absolutely for $|A - A_0| < R$ and diverges for $|A - A_0| > R$. On $|A - A_0| < R$ it converges uniformly on compact subsets.

**Theorem.** A power series is holomorphic on $|A - A_0| < R$, and its derivative is obtained by term-by-term differentiation:

$$
\frac{d}{dA} \sum_{n=0}^\infty c_n (A - A_0)^n = \sum_{n=1}^\infty n c_n (A - A_0)^{n-1}.
$$

The differentiated series has the same radius of convergence.

### Taylor Series

**Theorem (Taylor).** If $f$ is holomorphic on a domain containing the closed disk $\overline{B}(A_0, r)$, then $f$ has a power series expansion

$$
f(A) = \sum_{n=0}^\infty \frac{f^{(n)}(A_0)}{n!} (A - A_0)^n
$$

valid for $|A - A_0| < r$.

**Proof.** Use the Cauchy integral formula and expand $1/(B - A)$ as a geometric series in $(A - A_0)/(B - A_0)$.

**Corollary.** A holomorphic function is analytic: it equals its Taylor series in a neighborhood of every point.

**Corollary (identity theorem).** If two holomorphic functions on a domain $U$ agree on a set with an accumulation point in $U$, they agree on all of $U$.

### Laurent Series

**Theorem (Laurent).** If $f$ is holomorphic on an annulus $r < |A - A_0| < R$, then $f$ has a unique expansion

$$
f(A) = \sum_{n=-\infty}^\infty c_n (A - A_0)^n
$$

valid on the annulus, with

$$
c_n = \frac{1}{2\pi i} \oint_{|B - A_0| = \rho} \frac{f(B)}{(B - A_0)^{n+1}} \, dB, \qquad r < \rho < R.
$$

**Proof.** Apply the Cauchy integral formula on the annulus and expand the kernel in two geometric series, one for the inner boundary and one for the outer boundary.

## Singularities

### Classification

Let $f$ be holomorphic on a punctured disk $0 < |A - A_0| < R$.

**Removable singularity.** $A_0$ is removable if $f$ extends to a holomorphic function on $|A - A_0| < R$. Equivalently, the Laurent expansion has $c_n = 0$ for $n < 0$.

**Pole.** $A_0$ is a pole of order $m \geq 1$ if the Laurent expansion has $c_{-m} \neq 0$ and $c_n = 0$ for $n < -m$.

**Essential singularity.** $A_0$ is an essential singularity if the Laurent expansion has infinitely many non-zero $c_n$ with $n < 0$.

**Theorem (Riemann).** $A_0$ is removable iff $f$ is bounded near $A_0$.

**Theorem (Casorati–Weierstrass).** If $A_0$ is an essential singularity, then $f$ takes values arbitrarily close to every complex number in every neighborhood of $A_0$.

**Theorem (Picard).** If $A_0$ is an essential singularity, then $f$ takes every complex value, with at most one exception, in every punctured neighborhood of $A_0$.

### Residues

The **residue** of $f$ at an isolated singularity $A_0$ is the coefficient $c_{-1}$ in the Laurent expansion:

$$
\operatorname{Res}(f, A_0) = c_{-1} = \frac{1}{2\pi i} \oint_{|A - A_0| = \rho} f(A) \, dA.
$$

**Theorem (Residue Theorem).** Let $f$ be holomorphic on a simply connected domain except for isolated singularities $A_1, \dots, A_n$. Let $\gamma$ be a closed contour in the domain that does not pass through any $A_k$ and winds once around each. Then

$$
\oint_\gamma f(A) \, dA = 2\pi i \sum_{k=1}^n \operatorname{Res}(f, A_k).
$$

**Proof.** Apply the Cauchy–Goursat theorem to the domain with small disks removed around each singularity, then use the definition of the residue.

### Computation of Residues

**Simple pole.** If $f(A) = g(A)/h(A)$ with $g(A_0) \neq 0$, $h(A_0) = 0$, and $h'(A_0) \neq 0$, then

$$
\operatorname{Res}(f, A_0) = \frac{g(A_0)}{h'(A_0)}.
$$

**Pole of order $m$.** If $f$ has a pole of order $m$ at $A_0$, then

$$
\operatorname{Res}(f, A_0) = \frac{1}{(m-1)!} \lim_{A \to A_0} \frac{d^{m-1}}{dA^{m-1}} \left[ (A - A_0)^m f(A) \right].
$$

## Applications of the Residue Theorem

### Evaluation of Real Integrals

**Integrals of trigonometric functions.** For an integral of the form

$$
\int_0^{2\pi} R(\cos\theta, \sin\theta) \, d\theta,
$$

substitute $A = e^{i\theta}$, so that $\cos\theta = (A + A^{-1})/2$, $\sin\theta = (A - A^{-1})/(2i)$, and $d\theta = dA/(iA)$. The integral becomes a contour integral over the unit circle, evaluated by residues.

**Integrals over the real line.** For an integral of the form

$$
\int_{-\infty}^\infty f(a) \, da,
$$

where $f$ is a rational function decaying faster than $1/|a|$ at infinity with no poles on the real axis, close the contour in the upper half-plane and use the residue theorem.

**Integrals with trigonometric kernels.** For an integral of the form

$$
\int_{-\infty}^\infty f(b) e^{iab} \, db, \qquad a > 0,
$$

where $f$ is a rational function decaying at infinity with no poles on the real axis, use the same contour as above, with **Jordan's lemma** controlling the contribution from the semicircle.

### The Argument Principle

**Theorem (Argument Principle).** Let $f$ be meromorphic on a simply connected domain with zeros $A_1, \dots, A_m$ and poles $p_1, \dots, p_n$ (counted with multiplicity). Let $\gamma$ be a closed contour that winds once around each and does not pass through any. Then

$$
\frac{1}{2\pi i} \oint_\gamma \frac{f'(A)}{f(A)} \, dA = \sum_{k=1}^m \operatorname{ord}(f, A_k) - \sum_{k=1}^n \operatorname{ord}(f, p_k),
$$

where $\operatorname{ord}(f, A_k)$ is the order of the zero and $\operatorname{ord}(f, p_k)$ is the order of the pole.

**Interpretation.** The integral counts the winding number of $f(\gamma)$ around the origin, which equals the number of zeros minus the number of poles enclosed by $\gamma$.

### Rouché's Theorem

**Theorem (Rouché).** Let $f$ and $g$ be holomorphic on a simply connected domain, and let $\gamma$ be a closed contour such that $|g(A)| < |f(A)|$ on $\gamma$. Then $f$ and $f + g$ have the same number of zeros inside $\gamma$, counted with multiplicity.

**Proof.** Apply the argument principle to $f + tg$ for $t \in [0, 1]$ and note that the number of zeros is a continuous integer-valued function of $t$.

**Corollary (Fundamental Theorem of Algebra, again).** Every polynomial of degree $n \geq 1$ has exactly $n$ roots in $\mathbb{C}$, counted with multiplicity.

**Proof.** Write $p(A) = a_n A^n + \dots + a_0$. On a large circle, $|a_n A^n| > |a_{n-1} A^{n-1} + \dots + a_0|$, so by Rouché, $p$ has the same number of zeros as $a_n A^n$, which is $n$.

## Summary

Complex analysis is the study of complex-valued functions of a complex variable that possess a derivative in the complex sense. The plane carries the modulus $\lvert A\rvert = \sqrt{a^2 + a'^2}$, and with it the distance, the convergent sequences, the continuous functions and the open sets on which the subject is built.

The derivative $f'(A_0) = \lim_{h \to 0} (f(A_0 + h) - f(A_0))/h$ is the central object, and the article records how much stronger it is than its real analogue: a function that has it at every point of an open set is holomorphic, holomorphy is equivalent to the Cauchy–Riemann equations, and it forces the function to be analytic. Where the derivative is nonzero the map is conformal, preserving the angles between curves.

Integration along paths defines the contour integral, and the theorems the derivative buys are the substance of the subject: Cauchy's theorem, the Cauchy integral formula, the Liouville theorem, and the residue theorem, which evaluates an integral by summing the local contributions of the singularities. Power series, Taylor series and Laurent series describe the local behaviour of a holomorphic function, and the Laurent expansion classifies the isolated singularities as removable, a pole, or essential. The article closes by applying the residue theorem to the evaluation of real integrals.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}$ | Complex plane |
| $A = a + i a'$ | General complex number |
| $\bar{A} = a - i a'$ | Complex conjugate |
| $\|A\| = \sqrt{a^2 + a'^2}$ | Modulus |
| $d(A, B) = \|A - B\|$ | Distance |
| $B(A_0, r)$ | Open disk of radius $r$ |
| $U, F, K$ | Open, closed, compact sets |
| $A_n \to L$ | Convergence of a sequence |
| $\lim_{A \to A_0} f(A)$ | Limit of a function |
| $f'(A)$ | Complex derivative |
| $\partial/\partial A, \partial/\partial \bar{A}$ | Wirtinger derivatives |
| $\int_\gamma f(A) \, dA$ | Contour integral |
| $f^{(n)}(A)$ | $n$-th derivative |
| $\sum c_n (A - A_0)^n$ | Power series |
| $\operatorname{Res}(f, A_0)$ | Residue |
| $\operatorname{ord}(f, A_0)$ | Order of zero or pole |

## Further Reading

- Augustin-Louis Cauchy, *Cours d'analyse* (1821), for the origin of the subject.
- Bernhard Riemann, *Grundlagen für eine allgemeine Theorie der Functionen einer veränderlichen complexen Grösse* (1851), for the geometric viewpoint.
- Lars V. Ahlfors, *Complex Analysis* (McGraw-Hill, 1979), for the standard modern treatment.
- John B. Conway, *Functions of One Complex Variable* (Springer, 1978), for a thorough introduction.
- Walter Rudin, *Real and Complex Analysis* (McGraw-Hill, 1987), for the integration-theoretic perspective.
- Elias M. Stein and Rami Shakarchi, *Complex Analysis* (Princeton, 2003), for a modern treatment with connections to other areas.

