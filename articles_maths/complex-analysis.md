
# __Complex Analysis__

## Introduction

This article introduces complex analysis as the study of differentiable functions of a complex variable. The goal is to define the core objects precisely, establish their basic properties, and describe the theorems that give the subject its shape.

The treatment is mathematically honest: every claim is either proved or stated as a definition. The complex plane is used as the ambient space, convergence is defined in terms of the modulus, and the consequences of complex differentiability are developed systematically. The complex algebra is not re-derived; it is assumed as the coefficient field. The exponential is not introduced here; it belongs to the article on special functions.

## The Complex Plane

### Points and Distance

A complex number is written

$$
Q = q + i q', \qquad q, q' \in \mathbb{R},
$$

where $i^2 = -1$. The real number $q$ is the **real part**, and $q'$ is the **imaginary part**. We write $q = \operatorname{Re} Q$ and $q' = \operatorname{Im} Q$.

The **modulus** of $Q$ is

$$
\sqrt{\langle Q\rangle_{*}} = \sqrt{q^2 + q'^2},
$$

and the **distance** between two complex numbers $Q$ and $Q_1$ is

$$
d(Q, Q_1) = \sqrt{\langle Q - Q_1\rangle_{*}}.
$$

This makes $\mathbb{C}$ a metric space isometric to $\mathbb{R}^2$. The modulus satisfies

$$
\sqrt{\langle Q Q_1\rangle_{*}} = \sqrt{\langle Q\rangle_{*}} \sqrt{\langle Q_1\rangle_{*}}, \qquad \sqrt{\langle Q + Q_1\rangle_{*}} \leq \sqrt{\langle Q\rangle_{*}} + \sqrt{\langle Q_1\rangle_{*}}, \qquad |\operatorname{Re} Q| \leq \sqrt{\langle Q\rangle_{*}}, \qquad |\operatorname{Im} Q| \leq \sqrt{\langle Q\rangle_{*}}.
$$

The last two inequalities are used constantly: they say that convergence of complex numbers is equivalent to convergence of real and imaginary parts.

### Balls and Neighborhoods

The **open ball** of radius $r > 0$ centred at $Q_0$ is

$$
B(Q_0, r) = \{Q \in \mathbb{C} : \sqrt{\langle Q - Q_0\rangle_{*}} < r\}.
$$

It is an open disk. The **closed ball** is

$$
\overline{B}(Q_0, r) = \{Q \in \mathbb{C} : \sqrt{\langle Q - Q_0\rangle_{*}} \leq r\}.
$$

A **neighborhood** of $Q_0$ is any set containing some $B(Q_0, r)$.

### Open and Closed Sets

A set $\Omega \subseteq \mathbb{C}$ is **open** if for every $Q_0 \in \Omega$ there exists $r > 0$ with $B(Q_0, r) \subseteq \Omega$.

A set $F \subseteq \mathbb{C}$ is **closed** if its complement $\mathbb{C} \setminus F$ is open.

Arbitrary unions of open sets are open. Finite intersections of open sets are open. Dually, arbitrary intersections of closed sets are closed. Finite unions of closed sets are closed.

**Theorem.** A set $F$ is closed iff every convergent sequence in $F$ has its limit in $F$.

### Connectedness and Domains

A set $\Omega \subseteq \mathbb{C}$ is **connected** if it cannot be written as the disjoint union of two non-empty sets open in $\Omega$. It is **path-connected** if any two points can be joined by a continuous path in $\Omega$. For open subsets of $\mathbb{C}$, connectedness and path-connectedness are equivalent.

A **domain** is a non-empty open connected subset of $\mathbb{C}$. Domains are the natural setting for complex analysis, because differentiability on a domain imposes strong global constraints.

### Compactness

A set $K \subseteq \mathbb{C}$ is **compact** if every open cover of $K$ has a finite subcover.

**Theorem (Heine–Borel).** A subset of $\mathbb{C}$ is compact iff it is closed and bounded.

**Theorem.** A continuous complex-valued function on a compact set is bounded and attains its maximum and minimum modulus.

## Limits and Continuity

### Limits of Sequences

A sequence $(Q_n)$ of complex numbers **converges** to $L \in \mathbb{C}$ if for every $\epsilon > 0$ there exists $N \in \mathbb{N}$ such that

$$
n \geq N \implies \sqrt{\langle Q_n - L\rangle_{*}} < \epsilon.
$$

We write $Q_n \to L$ or $\lim_{n \to \infty} Q_n = L$.

**Uniqueness.** If $Q_n \to L$ and $Q_n \to L'$, then $L = L'$.

**Componentwise convergence.** Write $Q_n = q_n + i q'_n$ and $L = a + i b$. Then

$$
Q_n \to L \iff q_n \to a \text{ and } q'_n \to b.
$$

This is the reason complex convergence is no harder than real convergence: it is two real convergences in parallel.

**Boundedness.** Every convergent sequence is bounded. The converse fails.

**Algebra of limits.** If $Q_n \to L$ and $Q_{1,n} \to M$, then

$$
Q_n + Q_{1,n} \to L + M, \qquad Q_n Q_{1,n} \to L M, \qquad \frac{Q_n}{Q_{1,n}} \to \frac{L}{M} \text{ if } M \neq 0.
$$

### Cauchy Sequences

A sequence $(Q_n)$ is **Cauchy** if for every $\epsilon > 0$ there exists $N \in \mathbb{N}$ such that

$$
m, n \geq N \implies \sqrt{\langle Q_m - Q_n\rangle_{*}} < \epsilon.
$$

**Theorem.** In $\mathbb{C}$, a sequence converges iff it is Cauchy. This is the completeness of $\mathbb{C}$ as a metric space. It follows from the completeness of $\mathbb{R}$ applied to the real and imaginary parts.

### Limits of Functions

Let $f : D \to \mathbb{C}$ with $D \subseteq \mathbb{C}$, and let $Q_0$ be a limit point of $D$. We say

$$
\lim_{Q \to Q_0} f(Q) = L
$$

if for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
Q \in D, \; 0 < \sqrt{\langle Q - Q_0\rangle_{*}} < \delta \implies |f(Q) - L| < \epsilon.
$$

**Uniqueness.** If the limit exists, it is unique.

**Sequential criterion.** $\lim_{Q \to Q_0} f(Q) = L$ iff for every sequence $(Q_n)$ in $D \setminus \{Q_0\}$ with $Q_n \to Q_0$, we have $f(Q_n) \to L$.

**Algebra of limits.** Sums, products, and quotients (where defined) of limits are the limits of the sums, products, and quotients.

### Continuity

A function $f : D \to \mathbb{C}$ is **continuous at** $Q_0 \in D$ if $\lim_{Q \to Q_0} f(Q) = f(Q_0)$ when $Q_0$ is a limit point of $D$; a point of $D$ that is isolated in $D$ is a point of continuity by convention. Equivalently, and in a form that covers isolated points as well, for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
Q \in D, \; \sqrt{\langle Q - Q_0\rangle_{*}} < \delta \implies |f(Q) - f(Q_0)| < \epsilon.
$$

$f$ is **continuous on** $D$ if it is continuous at every point of $D$.

**Theorem.** $f$ is continuous at $Q_0$ iff for every sequence $(Q_n)$ in $D$ with $Q_n \to Q_0$, we have $f(Q_n) \to f(Q_0)$.

**Theorem.** Sums, products, and quotients (where defined) of continuous functions are continuous. Compositions of continuous functions are continuous.

**Theorem.** $f$ is continuous iff the preimage of every open set is open. Equivalently, the preimage of every closed set is closed.

**Componentwise continuity.** Write $f(Q) = u(q, q') + i v(q, q')$. Then $f$ is continuous at $Q_0 = q_0 + i q'_0$ iff $u$ and $v$ are continuous at $(q_0, q'_0)$. This reduces complex continuity to real continuity of two functions of two variables.

### Uniform Continuity

A function $f : D \to \mathbb{C}$ is **uniformly continuous** if for every $\epsilon > 0$ there exists $\delta > 0$ such that

$$
Q, Q_1 \in D, \; \sqrt{\langle Q - Q_1\rangle_{*}} < \delta \implies |f(Q) - f(Q_1)| < \epsilon.
$$

The difference from ordinary continuity is that $\delta$ depends only on $\epsilon$, not on the point.

**Theorem.** A continuous function on a compact set is uniformly continuous.

## Complex Differentiability

### The Derivative

Let $f : \Omega \to \mathbb{C}$ with $\Omega$ open, and let $Q_0 \in \Omega$. The **derivative** of $f$ at $Q_0$ is

$$
\frac{df}{dQ}(Q_0) = \lim_{h \to 0} \frac{f(Q_0 + h) - f(Q_0)}{h},
$$

provided the limit exists. If it does, $f$ is **complex differentiable** at $Q_0$, or **holomorphic** at $Q_0$.

The limit is taken in the complex plane, so $h$ can approach $0$ from any direction. This is a much stronger condition than real differentiability: the difference quotient must tend to the same limit along every path.

**Theorem.** Holomorphic implies continuous. The converse fails.

### The Cauchy–Riemann Equations

Write $f(Q) = u(q, q') + i v(q, q')$, where $Q = q + i q'$ and $u, v : \Omega \to \mathbb{R}$.

**Theorem.** $f$ is holomorphic at $Q_0 = q_0 + i q'_0$ iff $u$ and $v$ are real differentiable at $(q_0, q'_0)$ and satisfy the **Cauchy–Riemann equations**

$$
\frac{\partial u}{\partial q} = \frac{\partial v}{\partial q'}, \qquad \frac{\partial u}{\partial q'} = -\frac{\partial v}{\partial q}.
$$

**Proof.** Write $h = h_1 + i h_2$. The difference quotient is

$$
\frac{f(Q_0 + h) - f(Q_0)}{h} = \frac{(u_q h_1 + u_{q'} h_2) + i (v_q h_1 + v_{q'} h_2)}{h_1 + i h_2} + o(1).
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
\frac{\partial}{\partial Q} = \frac{1}{2}\left( \frac{\partial}{\partial q} - i \frac{\partial}{\partial q'} \right), \qquad \frac{\partial}{\partial \bar{Q}} = \frac{1}{2}\left( \frac{\partial}{\partial q} + i \frac{\partial}{\partial q'} \right).
$$

**Theorem.** $f$ is holomorphic iff $f$ is real differentiable and $\partial f / \partial \bar{Q} = 0$. In that case,

$$
\frac{df}{dQ} = \frac{\partial f}{\partial Q}.
$$

The condition $\partial f / \partial \bar{Q} = 0$ is the Cauchy–Riemann equations in compact form.

### Rules of Differentiation

**Linearity.** $\frac{d}{dQ}(af + bg) = a\frac{df}{dQ} + b\frac{dg}{dQ}$.

**Product rule.** $\frac{d}{dQ}(fg) = \frac{df}{dQ}g + f\frac{dg}{dQ}$.

**Quotient rule.** $\frac{d}{dQ}(f/g) = \left(\frac{df}{dQ}g - f\frac{dg}{dQ}\right)/g^2$ where $g \neq 0$.

**Chain rule.** $\frac{d}{dQ}(f \circ g)(Q) = \frac{df}{dQ}(g(Q))\,\frac{dg}{dQ}(Q)$.

**Inverse function rule.** If $f$ is holomorphic at $Q_0$ with $\frac{df}{dQ}(Q_0) \neq 0$ and $f^{-1}$ is defined near $f(Q_0)$, then

$$
\frac{df^{-1}}{dQ}(f(Q_0)) = \left(\frac{df}{dQ}(Q_0)\right)^{-1}.
$$

## Conformal Maps

### Definition

A map $f : \Omega \to \mathbb{C}$ is **conformal** at $Q_0$ if it preserves angles between curves through $Q_0$. In particular, if $f$ is holomorphic at $Q_0$ with $\frac{df}{dQ}(Q_0) \neq 0$, then $f$ is conformal at $Q_0$.

**Theorem.** If $f$ is holomorphic at $Q_0$ with $\frac{df}{dQ}(Q_0) \neq 0$, then $f$ is conformal at $Q_0$, and the local behavior of $f$ near $Q_0$ is multiplication by $\frac{df}{dQ}(Q_0)$, i.e., a rotation by $\arg \frac{df}{dQ}(Q_0)$ and a scaling by $|\frac{df}{dQ}(Q_0)|$.

**Proof.** Write $f(Q) - f(Q_0) = \frac{df}{dQ}(Q_0)(Q - Q_0) + o(\sqrt{\langle Q - Q_0\rangle_{*}})$. The linear term is multiplication by $\frac{df}{dQ}(Q_0)$, which is a rotation and a scaling.

### Möbius Transformations

A **Möbius transformation** is a map of the form

$$
f(Q) = \frac{aQ + b}{cQ + d}, \qquad ad - bc \neq 0.
$$

It is holomorphic on $\mathbb{C} \setminus \{-d/c\}$ when $c \neq 0$, and entire when $c = 0$; it is conformal wherever $\frac{df}{dQ} \neq 0$. Möbius transformations map circles and lines to circles and lines, and they form a group under composition.

### The Riemann Mapping Theorem

**Theorem (Riemann Mapping).** Let $\Omega \subsetneq \mathbb{C}$ be a simply connected domain. Then there exists a biholomorphic map $f : \Omega \to B(0, 1)$.

The map is unique up to composition with a Möbius transformation of the disk.

## Integration

### Contour Integrals

Let $\gamma : [a, b] \to \mathbb{C}$ be a piecewise continuously differentiable path, and let $f$ be continuous on the image of $\gamma$. The **contour integral** of $f$ along $\gamma$ is

$$
\int_\gamma f(Q) \, dQ = \int_a^b f(\gamma(t)) \gamma'(t) \, dt.
$$

**Linearity.** $\int_\gamma (af + bg) = a \int_\gamma f + b \int_\gamma g$.

**Reversal.** $\int_{-\gamma} f = -\int_\gamma f$.

**Additivity.** If $\gamma$ is the concatenation of $\gamma_1$ and $\gamma_2$, then $\int_\gamma f = \int_{\gamma_1} f + \int_{\gamma_2} f$.

**Estimation.** If $|f(Q)| \leq M$ on $\gamma$ and $L$ is the length of $\gamma$, then

$$
\left| \int_\gamma f(Q) \, dQ \right| \leq M L.
$$

### The Cauchy–Goursat Theorem

**Theorem (Cauchy–Goursat).** If $f$ is holomorphic on a simply connected domain $\Omega$ and $\gamma$ is a closed contour in $\Omega$, then

$$
\oint_\gamma f(Q) \, dQ = 0.
$$

**Proof.** For a triangle, subdivide repeatedly and use the fact that the integral over the small triangles is bounded by the area times the supremum of $|\frac{df}{dQ}|$. For a general contour, approximate by polygons.

**Corollary.** On a simply connected domain, the integral of a holomorphic function is path-independent. The function

$$
F(Q) = \int_{Q_0}^Q f(Q_1) \, dQ_1
$$

is well-defined, holomorphic, and satisfies $F' = f$.

### The Cauchy Integral Formula

**Theorem (Cauchy Integral Formula).** Let $f$ be holomorphic on a domain containing the closed disk $\overline{B}(Q_0, r)$. Then for every $Q$ in the open disk,

$$
f(Q) = \frac{1}{2\pi i} \oint_{\sqrt{\langle Q_1 - Q_0\rangle_{*}} = r} \frac{f(Q_1)}{Q_1 - Q} \, dQ_1.
$$

**Proof.** Apply the Cauchy-Goursat theorem to the function $g(Q_1) = (f(Q_1) - f(Q))/(Q_1 - Q)$ on the punctured disk, then let the radius of the small circle around $Q$ tend to zero.

**Corollary (derivatives).** Under the same hypotheses, $f$ is infinitely differentiable, and

$$
f^{(n)}(Q) = \frac{n!}{2\pi i} \oint_{\sqrt{\langle Q_1 - Q_0\rangle_{*}} = r} \frac{f(Q_1)}{(Q_1 - Q)^{n+1}} \, dQ_1.
$$

**Corollary (Cauchy estimates).** If $|f| \leq M$ on $\sqrt{\langle Q_1 - Q_0\rangle_{*}} = r$, then

$$
|f^{(n)}(Q_0)| \leq \frac{n! M}{r^n}.
$$

### Liouville's Theorem

**Theorem (Liouville).** Every bounded entire function is constant.

**Proof.** Apply the Cauchy estimates to $\frac{df}{dQ}$ on a circle of radius $r$ around $Q_0$. Since $f$ is bounded by $M$, we have $|\frac{df}{dQ}(Q_0)| \leq M/r$ for every $r > 0$. Let $r \to \infty$ to get $\frac{df}{dQ}(Q_0) = 0$. Since $Q_0$ is arbitrary, $\frac{df}{dQ} = 0$ everywhere, so $f$ is constant.

**Corollary (Fundamental Theorem of Algebra).** Every non-constant polynomial with complex coefficients has a root in $\mathbb{C}$.

**Proof.** If $p$ has no root, then $1/p$ is entire and bounded (since $|p(Q)| \to \infty$ as $\sqrt{\langle Q\rangle_{*}} \to \infty$), hence constant by Liouville. Contradiction.

### Morera's Theorem

**Theorem (Morera).** If $f$ is continuous on a domain $\Omega$ and $\oint_\gamma f = 0$ for every closed contour $\gamma$ in $\Omega$, then $f$ is holomorphic on $\Omega$.

**Proof.** Define $F(Q) = \int_{Q_0}^Q f(Q_1) \, dQ_1$. The hypothesis makes $F$ well-defined, and $F' = f$. Since $F$ is holomorphic, $F$ is infinitely differentiable, so $f$ is holomorphic.

## Series Representations

### Power Series

A **power series** centred at $Q_0$ is

$$
\sum_{n=0}^\infty c_n (Q - Q_0)^n, \qquad c_n \in \mathbb{C}.
$$

The **radius of convergence** is

$$
R = \frac{1}{\limsup_{n \to \infty} |c_n|^{1/n}},
$$

with the conventions $R = 0$ if the limsup is $\infty$ and $R = \infty$ if the limsup is $0$.

**Theorem.** The series converges absolutely for $\sqrt{\langle Q - Q_0\rangle_{*}} < R$ and diverges for $\sqrt{\langle Q - Q_0\rangle_{*}} > R$. On $\sqrt{\langle Q - Q_0\rangle_{*}} < R$ it converges uniformly on compact subsets.

**Theorem.** A power series is holomorphic on $\sqrt{\langle Q - Q_0\rangle_{*}} < R$, and its derivative is obtained by term-by-term differentiation:

$$
\frac{d}{dQ} \sum_{n=0}^\infty c_n (Q - Q_0)^n = \sum_{n=1}^\infty n c_n (Q - Q_0)^{n-1}.
$$

The differentiated series has the same radius of convergence.

### Taylor Series

**Theorem (Taylor).** If $f$ is holomorphic on a domain containing the closed disk $\overline{B}(Q_0, r)$, then $f$ has a power series expansion

$$
f(Q) = \sum_{n=0}^\infty \frac{f^{(n)}(Q_0)}{n!} (Q - Q_0)^n
$$

valid for $\sqrt{\langle Q - Q_0\rangle_{*}} < r$.

**Proof.** Use the Cauchy integral formula and expand $1/(Q_1 - Q)$ as a geometric series in $(Q - Q_0)/(Q_1 - Q_0)$.

**Corollary.** A holomorphic function is analytic: it equals its Taylor series in a neighborhood of every point.

**Corollary (identity theorem).** If two holomorphic functions on a domain $\Omega$ agree on a set with an accumulation point in $\Omega$, they agree on all of $\Omega$.

### Laurent Series

**Theorem (Laurent).** If $f$ is holomorphic on an annulus $r < \sqrt{\langle Q - Q_0\rangle_{*}} < R$, then $f$ has a unique expansion

$$
f(Q) = \sum_{n=-\infty}^\infty c_n (Q - Q_0)^n
$$

valid on the annulus, with

$$
c_n = \frac{1}{2\pi i} \oint_{\sqrt{\langle Q_1 - Q_0\rangle_{*}} = \rho} \frac{f(Q_1)}{(Q_1 - Q_0)^{n+1}} \, dQ_1, \qquad r < \rho < R.
$$

**Proof.** Apply the Cauchy integral formula on the annulus and expand the kernel in two geometric series, one for the inner boundary and one for the outer boundary.

## Singularities

### Classification

Let $f$ be holomorphic on a punctured disk $0 < \sqrt{\langle Q - Q_0\rangle_{*}} < R$.

**Removable singularity.** $Q_0$ is removable if $f$ extends to a holomorphic function on $\sqrt{\langle Q - Q_0\rangle_{*}} < R$. Equivalently, the Laurent expansion has $c_n = 0$ for $n < 0$.

**Pole.** $Q_0$ is a pole of order $m \geq 1$ if the Laurent expansion has $c_{-m} \neq 0$ and $c_n = 0$ for $n < -m$.

**Essential singularity.** $Q_0$ is an essential singularity if the Laurent expansion has infinitely many non-zero $c_n$ with $n < 0$.

**Theorem (Riemann).** $Q_0$ is removable iff $f$ is bounded near $Q_0$.

**Theorem (Casorati–Weierstrass).** If $Q_0$ is an essential singularity, then $f$ takes values arbitrarily close to every complex number in every neighborhood of $Q_0$.

**Theorem (Picard).** If $Q_0$ is an essential singularity, then $f$ takes every complex value, with at most one exception, in every punctured neighborhood of $Q_0$.

### Residues

The **residue** of $f$ at an isolated singularity $Q_0$ is the coefficient $c_{-1}$ in the Laurent expansion:

$$
\operatorname{Res}(f, Q_0) = c_{-1} = \frac{1}{2\pi i} \oint_{\sqrt{\langle Q - Q_0\rangle_{*}} = \rho} f(Q) \, dQ.
$$

**Theorem (Residue Theorem).** Let $f$ be holomorphic on a simply connected domain except for isolated singularities $Q_1, \dots, Q_n$. Let $\gamma$ be a closed contour in the domain that does not pass through any $Q_k$ and winds once around each. Then

$$
\oint_\gamma f(Q) \, dQ = 2\pi i \sum_{k=1}^n \operatorname{Res}(f, Q_k).
$$

**Proof.** Apply the Cauchy–Goursat theorem to the domain with small disks removed around each singularity, then use the definition of the residue.

### Computation of Residues

**Simple pole.** If $f(Q) = g(Q)/h(Q)$ with $g(Q_0) \neq 0$, $h(Q_0) = 0$, and $\frac{dh}{dQ}(Q_0) \neq 0$, then

$$
\operatorname{Res}(f, Q_0) = \frac{g(Q_0)}{\frac{dh}{dQ}(Q_0)}.
$$

**Pole of order $m$.** If $f$ has a pole of order $m$ at $Q_0$, then

$$
\operatorname{Res}(f, Q_0) = \frac{1}{(m-1)!} \lim_{Q \to Q_0} \frac{d^{m-1}}{dQ^{m-1}} \left[ (Q - Q_0)^m f(Q) \right].
$$

## Applications of the Residue Theorem

### Evaluation of Real Integrals

**Integrals of trigonometric functions.** For an integral of the form

$$
\int_0^{2\pi} R(\cos\theta, \sin\theta) \, d\theta,
$$

substitute $Q = \exp(i\theta)$, so that $\cos\theta = (Q + Q^{-1})/2$, $\sin\theta = (Q - Q^{-1})/(2i)$, and $d\theta = dQ/(iQ)$. The integral becomes a contour integral over the unit circle, evaluated by residues.

**Integrals over the real line.** For an integral of the form

$$
\int_{-\infty}^\infty f(a) \, da,
$$

where $f$ is a rational function decaying faster than $1/|a|$ at infinity with no poles on the real axis, close the contour in the upper half-plane and use the residue theorem.

**Integrals with trigonometric kernels.** For an integral of the form

$$
\int_{-\infty}^\infty f(b) \exp(iab) \, db, \qquad a > 0,
$$

where $f$ is a rational function decaying at infinity with no poles on the real axis, use the same contour as above, with **Jordan's lemma** controlling the contribution from the semicircle.

### The Argument Principle

**Theorem (Argument Principle).** Let $f$ be meromorphic on a simply connected domain with zeros $Q_1, \dots, Q_m$ and poles $p_1, \dots, p_n$ (counted with multiplicity). Let $\gamma$ be a closed contour that winds once around each and does not pass through any. Then

$$
\frac{1}{2\pi i} \oint_\gamma \frac{\frac{df}{dQ}}{f(Q)} \, dQ = \sum_{k=1}^m \operatorname{ord}(f, Q_k) - \sum_{k=1}^n \operatorname{ord}(f, p_k),
$$

where $\operatorname{ord}(f, Q_k)$ is the order of the zero and $\operatorname{ord}(f, p_k)$ is the order of the pole.

**Interpretation.** The integral counts the winding number of $f(\gamma)$ around the origin, which equals the number of zeros minus the number of poles enclosed by $\gamma$.

### Rouché's Theorem

**Theorem (Rouché).** Let $f$ and $g$ be holomorphic on a simply connected domain, and let $\gamma$ be a closed contour such that $|g(Q)| < |f(Q)|$ on $\gamma$. Then $f$ and $f + g$ have the same number of zeros inside $\gamma$, counted with multiplicity.

**Proof.** Apply the argument principle to $f + tg$ for $t \in [0, 1]$ and note that the number of zeros is a continuous integer-valued function of $t$.

**Corollary (Fundamental Theorem of Algebra, again).** Every polynomial of degree $n \geq 1$ has exactly $n$ roots in $\mathbb{C}$, counted with multiplicity.

**Proof.** Write $p(Q) = a_n Q^n + \dots + a_0$. On a large circle, $|a_n Q^n| > |a_{n-1} Q^{n-1} + \dots + a_0|$, so by Rouché, $p$ has the same number of zeros as $a_n Q^n$, which is $n$.

## Summary

Complex analysis is the study of complex-valued functions of a complex variable that possess a derivative in the complex sense. The plane carries the modulus $\sqrt{\langle Q\rangle_{*}} = \sqrt{q^2 + q'^2}$, and with it the distance, the convergent sequences, the continuous functions and the open sets on which the subject is built.

The derivative $\frac{df}{dQ}(Q_0) = \lim_{h \to 0} (f(Q_0 + h) - f(Q_0))/h$ is the central object, and the article records how much stronger it is than its real analogue: a function that has it at every point of an open set is holomorphic, holomorphy is equivalent to the Cauchy–Riemann equations, and it forces the function to be analytic. Where the derivative is nonzero the map is conformal, preserving the angles between curves.

Integration along paths defines the contour integral, and the theorems the derivative buys are the substance of the subject: Cauchy's theorem, the Cauchy integral formula, the Liouville theorem, and the residue theorem, which evaluates an integral by summing the local contributions of the singularities. Power series, Taylor series and Laurent series describe the local behaviour of a holomorphic function, and the Laurent expansion classifies the isolated singularities as removable, a pole, or essential. The article closes by applying the residue theorem to the evaluation of real integrals.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}$ | Complex plane |
| $Q = q + i q'$ | General complex number |
| $\bar{Q} = q - i q'$ | Complex conjugate |
| $\sqrt{\langle Q\rangle_{*}} = \sqrt{q^2 + q'^2}$ | Modulus |
| $d(Q, Q_1) = \sqrt{\langle Q - Q_1\rangle_{*}}$ | Distance |
| $B(Q_0, r)$ | Open disk of radius $r$ |
| $\Omega, F, K$ | Open, closed, compact sets |
| $Q_n \to L$ | Convergence of a sequence |
| $\lim_{Q \to Q_0} f(Q)$ | Limit of a function |
| $\frac{df}{dQ}$ | Complex derivative |
| $\partial/\partial Q, \partial/\partial \bar{Q}$ | Wirtinger derivatives |
| $\int_\gamma f(Q) \, dQ$ | Contour integral |
| $f^{(n)}(Q)$ | $n$-th derivative |
| $\sum c_n (Q - Q_0)^n$ | Power series |
| $\operatorname{Res}(f, Q_0)$ | Residue |
| $\operatorname{ord}(f, Q_0)$ | Order of zero or pole |

## Further Reading

- Augustin-Louis Cauchy, *Cours d'analyse* (1821), for the origin of the subject.
- Bernhard Riemann, *Grundlagen für eine allgemeine Theorie der Functionen einer veränderlichen complexen Grösse* (1851), for the geometric viewpoint.
- Lars V. Ahlfors, *Complex Analysis* (McGraw-Hill, 1979), for the standard modern treatment.
- John B. Conway, *Functions of One Complex Variable* (Springer, 1978), for a thorough introduction.
- Walter Rudin, *Real and Complex Analysis* (McGraw-Hill, 1987), for the integration-theoretic perspective.
- Elias M. Stein and Rami Shakarchi, *Complex Analysis* (Princeton, 2003), for a modern treatment with connections to other areas.

