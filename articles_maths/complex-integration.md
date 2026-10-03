
# __Complex Integration__

## Introduction

This article develops integration for functions of one complex variable. It follows the article on complex analysis, which defined the complex plane, its metric, limits, continuity, holomorphy and the Cauchy–Riemann equations, and it takes up the contour integral in the form the rest of the complex theory needs. The aim is to construct the integral from first principles, to state the Cauchy theorem and the Cauchy integral formula with the hypotheses they actually require, and to derive the residue theory and analytic continuation from them.

The complex case is the model case of hypercomplex integration. Because $\mathbb{C}$ is a field, every non-zero element is invertible, there are no zero divisors, and the algebra is commutative; none of the obstructions that complicate the integration theory of $\mathbb{H}$, of the split complex numbers or of the dual numbers is present. The contour integral of a continuous function along a piecewise continuously differentiable path always exists, the Cauchy theorem holds without qualification on a simply connected domain, and the residue theorem computes the integral exactly. What is specific to $\mathbb{C}$ is that the values of the integral on closed paths are governed by the winding number, an integer-valued homotopy invariant of the path.

No physics is invoked. The complex numbers are the coefficient field, the plane $\mathbb{C}$ is the domain of the functions, and the independent variable is a complex number.

For notation, complex numbers are written $A = a + i a'$ with $a = \operatorname{Re} A$, $a' = \operatorname{Im} A$, and modulus $|A| = \sqrt{a^2+a'^2}$, following *Complex Analysis*. The Cauchy–Riemann operator is $\partial_{\bar A} = \tfrac12(\partial_a + i \partial_{a'})$, and a function is holomorphic exactly when $\partial_{\bar A} f = 0$. The exponential $e^{i\theta} = \cos\theta + i\sin\theta$ and the real trigonometric functions are used where an angle is parametrised and are taken. The circle of radius $r$ about $A_0$ is written $C(A_0, r)$ and is always positively oriented unless the opposite is stated.

## The Complex Integral

### Paths and Contours

**Definition.** A **path** is a continuous map $\gamma : [a, b] \to \mathbb{C}$. It is **piecewise continuously differentiable**, written piecewise $C^1$, if there is a finite subdivision $a = t_0 < t_1 < \cdots < t_n = b$ such that $\gamma$ is continuously differentiable on each closed subinterval $[t_{k-1}, t_k]$; the one-sided derivatives at the junctions may differ. A path is **smooth** if it is $C^1$ on all of $[a, b]$, **closed** if $\gamma(a) = \gamma(b)$, and **simple** if it is injective on $[a, b)$; a simple closed path is also called a **contour**.

The **trace** of $\gamma$ is the compact set $\gamma^* = \gamma([a, b])$. The **opposite path** $-\gamma$ is defined by $(-\gamma)(t) = \gamma(a + b - t)$, the same curve traversed backwards. If $\gamma_1 : [a, b] \to \mathbb{C}$ and $\gamma_2 : [b, c] \to \mathbb{C}$ agree at $b$, their **concatenation** $\gamma_1 + \gamma_2$ is the path on $[a, c]$ that follows first $\gamma_1$ and then $\gamma_2$. The **length** of a piecewise $C^1$ path is

$$
L(\gamma) = \int_a^b |\gamma'(t)| \, dt,
$$

finite because $\gamma'$ is piecewise continuous on a compact interval. The corresponding element of arclength is $|dA| = |\gamma'(t)| \, dt$.

**Example.** For $A_0 \in \mathbb{C}$ and $r > 0$ the positively oriented circle

$$
\gamma(t) = A_0 + r e^{it}, \qquad t \in [0, 2\pi],
$$

is a contour, with $\gamma'(t) = i r e^{it}$ and $L(\gamma) = 2\pi r$.

### Construction from the Riemann Sum

The integral along a path is defined by the limiting procedure that defines the Riemann integral, with the real increment of the variable replaced by the complex increment of the path.

**Definition.** Let $\gamma : [a, b] \to \mathbb{C}$ be piecewise $C^1$ and let $f$ be continuous on $\gamma^*$. Given a subdivision $a = t_0 < t_1 < \cdots < t_n = b$ and sample points $\tau_k \in [t_{k-1}, t_k]$, set $A_k = \gamma(t_k)$ and form the **Riemann sum**

$$
S = \sum_{k=1}^n f(\gamma(\tau_k)) (A_k - A_{k-1}).
$$

Writing $\|\Delta\| = \max_k (t_k - t_{k-1})$, the **complex integral** of $f$ along $\gamma$ is the limit

$$
\int_\gamma f(A) \, dA = \lim_{\|\Delta\| \to 0} S,
$$

whose existence is the content of the next theorem.

**Theorem.** For piecewise $C^1$ $\gamma$ and continuous $f$ on $\gamma^*$ the Riemann sums converge, and

$$
\int_\gamma f(A) \, dA = \int_a^b f(\gamma(t)) \gamma'(t) \, dt.
$$

**Proof.** On a subinterval on which $\gamma$ is $C^1$,

$$
A_k - A_{k-1} = \gamma(t_k) - \gamma(t_{k-1}) = \int_{t_{k-1}}^{t_k} \gamma'(t) \, dt = \gamma'(\tau_k)(t_k - t_{k-1}) + \rho_k,
$$

where $|\rho_k| \le \sup_{[t_{k-1}, t_k]} |\gamma' - \gamma'(\tau_k)| \, (t_k - t_{k-1})$. Each piece of $\gamma'$ is uniformly continuous and there are finitely many pieces, so $|\rho_k| \le \varepsilon(\|\Delta\|) (t_k - t_{k-1})$ with $\varepsilon(\|\Delta\|) \to 0$ as $\|\Delta\| \to 0$. Hence

$$
S = \sum_k f(\gamma(\tau_k)) \gamma'(\tau_k) (t_k - t_{k-1}) + \sum_k f(\gamma(\tau_k)) \rho_k .
$$

The first sum is a Riemann sum for the continuous function $t \mapsto f(\gamma(t)) \gamma'(t)$ on $[a, b]$, so it converges to the displayed integral; the second is bounded in modulus by $\max_{\gamma^*}|f| \, \varepsilon(\|\Delta\|) (b-a) \to 0$.

### Basic Properties

**Linearity.** For $\alpha, \beta \in \mathbb{C}$,

$$
\int_\gamma (\alpha f + \beta g)(A) \, dA = \alpha \int_\gamma f(A) \, dA + \beta \int_\gamma g(A) \, dA .
$$

**Reversal.** $\displaystyle\int_{-\gamma} f(A) \, dA = -\int_\gamma f(A) \, dA$.

**Additivity.** $\displaystyle\int_{\gamma_1 + \gamma_2} f(A) \, dA = \int_{\gamma_1} f(A) \, dA + \int_{\gamma_2} f(A) \, dA$.

**Invariance under reparametrisation.** If $\varphi : [c, d] \to [a, b]$ is a piecewise $C^1$ bijection with $\varphi(c) = a$, $\varphi(d) = b$, then $\int_{\gamma \circ \varphi} f \, dA = \int_\gamma f \, dA$; if $\varphi$ reverses the endpoints, the sign changes.

**Estimation.** If $|f(A)| \le m$ on $\gamma^*$, then

$$
\left| \int_\gamma f(A) \, dA \right| \le m \, L(\gamma).
$$

**Proof.** From the definition,

$$
\left| \int_a^b f(\gamma(t)) \gamma'(t) \, dt \right| \le \int_a^b |f(\gamma(t))| \, |\gamma'(t)| \, dt \le m \int_a^b |\gamma'(t)| \, dt = m L(\gamma).
$$

**Real and imaginary parts.** Writing $f = u + iv$ and $dA = da + i \, da'$ gives

$$
\int_\gamma f(A) \, dA = \int_\gamma (u \, da - v \, da') + i \int_\gamma (v \, da + u \, da'),
$$

in which each term on the right is an ordinary real line integral along $\gamma$. This is where the complex integral meets the real theory of line integrals, and it is also what makes the integral a functional of the path and not merely of the integrand.

### The Fundamental Theorem for Contour Integrals

**Definition.** A **primitive** of $f$ on a domain $U$ is a holomorphic $F : U \to \mathbb{C}$ with $F' = f$.

**Theorem (fundamental theorem).** If $F$ is a primitive of $f$ on $U$ and $\gamma$ is a piecewise $C^1$ path in $U$ from $A_1$ to $A_2$, then

$$
\int_\gamma f(A) \, dA = F(A_2) - F(A_1).
$$

**Proof.** On each smooth piece the chain rule gives $\frac{d}{dt} F(\gamma(t)) = F'(\gamma(t)) \gamma'(t) = f(\gamma(t)) \gamma'(t)$. Integrating over the piece, applying the fundamental theorem of calculus of the real theory to the real and imaginary parts, and summing the pieces gives the stated formula.

**Corollary.** If $f$ has a primitive on $U$, its integral along every closed path in $U$ vanishes.

**Example.** The monomial $A^n$ has the primitive $A^{n+1}/(n+1)$ on $\mathbb{C}$ for $n \ge 0$ and on $\mathbb{C}^\times$ for $n \le -2$, so

$$
\oint_\gamma A^n \, dA = 0 \qquad (n \ge 0 \text{ or } n \le -2)
$$

for every closed path that does not pass through the origin. The excluded case $n = -1$ is the fundamental one:

$$
\oint_{|A| = r} \frac{dA}{A} = \int_0^{2\pi} \frac{ire^{it}}{re^{it}} \, dt = 2\pi i \neq 0 .
$$

So $1/A$ admits no primitive on $\mathbb{C}^\times$, and the value $2\pi i$ is the source of the entire residue theory.

## The Winding Number

**Definition.** Let $\gamma$ be a closed piecewise $C^1$ path and let $A_0 \notin \gamma^*$. The **winding number** (or index) of $\gamma$ about $A_0$ is

$$
\operatorname{Ind}(\gamma, A_0) = \frac{1}{2\pi i} \oint_\gamma \frac{dA}{A - A_0}.
$$

**Theorem.** $\operatorname{Ind}(\gamma, A_0)$ is an integer; it is constant on each connected component of $\mathbb{C} \setminus \gamma^*$; and it is $0$ on the unbounded component.

**Proof.** The function

$$
h(A) = \oint_\gamma \frac{dB}{B - A}, \qquad A \notin \gamma^*,
$$

is holomorphic on $\mathbb{C} \setminus \gamma^*$, since differentiating under the integral sign is legitimate there, with

$$
h'(A) = \oint_\gamma \frac{dB}{(B - A)^2}.
$$

The integrand $(B-A)^{-2}$ has the primitive $-(B-A)^{-1}$ in the variable $B$ on $\mathbb{C} \setminus \{A\}$, so $h'(A) = 0$ and $h$ is locally constant. Put $\Phi(A) = \exp h(A)$; then $\Phi'(A) = h'(A) \Phi(A) = 0$, so $\Phi$ is constant, and as $|A| \to \infty$ the integrand tends to $0$ uniformly on the compact set $\gamma^*$, so $h(A) \to 0$ and $\Phi(A) \to 1$. Therefore $\Phi \equiv 1$, that is, $h(A) \in 2\pi i \mathbb{Z}$ for every $A$. A continuous function with values in a discrete set is locally constant, hence constant on each connected component, and on the unbounded component the limit at infinity forces the value $0$.

**Example.** For the positively oriented circle $\gamma(t) = A_0 + re^{it}$ one has $\operatorname{Ind}(\gamma, A_0) = 1$ and $\operatorname{Ind}(\gamma, A) = 0$ for $|A - A_0| > r$. For the same circle traversed $m$ times the index is $m$.

**Theorem (homotopy invariance).** Let $\gamma_0, \gamma_1$ be closed piecewise $C^1$ paths in a domain $U$ and let $H : [0,1] \times [a,b] \to U$ be continuous with $H(s, \cdot)$ closed and piecewise $C^1$ for every $s$, $H(0, \cdot) = \gamma_0$ and $H(1, \cdot) = \gamma_1$. Then $\operatorname{Ind}(\gamma_0, A_0) = \operatorname{Ind}(\gamma_1, A_0)$ for every $A_0 \notin U$.

**Proof.** For a closed path $\gamma$ avoiding $A_0$ one may write $\gamma(t) - A_0 = r(t) e^{i\Theta(t)}$ with $r > 0$ and $\Theta$ continuous on $[a, b]$, and the total change of the argument is $2\pi \operatorname{Ind}(\gamma, A_0)$. Since $A_0 \notin U$, the map $H - A_0$ takes values in $\mathbb{C}^\times$, and because the rectangle $[0,1] \times [a,b]$ is simply connected the argument admits a continuous lift $\tilde\Theta$ on the whole rectangle, with $H(s,t) - A_0 = \rho(s,t) e^{i \tilde\Theta(s,t)}$ and $\rho > 0$. Then $s \mapsto \tilde\Theta(s, b) - \tilde\Theta(s, a)$ is continuous and takes values in the discrete set $2\pi\mathbb{Z}$, hence is constant, and its value is $2\pi \operatorname{Ind}(H(s, \cdot), A_0)$.

The winding number therefore depends only on the homotopy class of the path in $U$, and it is the reason a closed path in a simply connected domain has winding number zero about every point outside the domain.

## The Cauchy Theorem

### The Cauchy–Goursat Theorem

**Theorem (Cauchy–Goursat).** Let $f$ be holomorphic on an open set $U$ and let $T$ be a closed triangle whose interior and boundary lie in $U$. Then

$$
\oint_{\partial T} f(A) \, dA = 0 .
$$

**Proof.** Let $I = \oint_{\partial T} f \, dA$ and subdivide $T$ by joining the midpoints of its sides into four congruent triangles $T_1, T_2, T_3, T_4$. The integrals over the interior edges cancel in pairs, so

$$
I = \sum_{j=1}^{4} \oint_{\partial T_j} f(A) \, dA ,
$$

and one of the four triangles, call it $T^{(1)}$, satisfies $\left| \oint_{\partial T^{(1)}} f \right| \ge |I|/4$. Iterating produces nested triangles $T \supseteq T^{(1)} \supseteq T^{(2)} \supseteq \cdots$ with

$$
\operatorname{diam} T^{(n)} = 2^{-n} \operatorname{diam} T, \qquad L(\partial T^{(n)}) = 2^{-n} L(\partial T), \qquad \left| \oint_{\partial T^{(n)}} f \right| \ge |I| / 4^n .
$$

By compactness $\bigcap_n T^{(n)} = \{A_0\}$ for some $A_0 \in U$. Holomorphy at $A_0$ gives the expansion

$$
f(A) = f(A_0) + f'(A_0)(A - A_0) + (A - A_0)\eta(A), \qquad \eta(A) \to 0 \ \ (A \to A_0).
$$

The constant and the linear term have primitives and therefore integrate to zero over the closed curve $\partial T^{(n)}$, so $\oint_{\partial T^{(n)}} f = \oint_{\partial T^{(n)}} (A - A_0)\eta(A) \, dA$. For $A \in T^{(n)}$ one has $|A - A_0| \le \operatorname{diam} T^{(n)}$ and $|\eta(A)| \le \varepsilon_n$ with $\varepsilon_n \to 0$, whence by the estimation property

$$
\left| \oint_{\partial T^{(n)}} f \right| \le \operatorname{diam} T^{(n)} \cdot \varepsilon_n \cdot L(\partial T^{(n)}) = 4^{-n} \, \varepsilon_n \operatorname{diam} T \, L(\partial T).
$$

Combining with $|I| \le 4^n \left| \oint_{\partial T^{(n)}} f \right|$ gives $|I| \le \varepsilon_n \operatorname{diam} T \, L(\partial T) \to 0$, so $I = 0$.

**Remark.** The proof uses only that $f'$ exists, never that $f'$ is continuous. This is Goursat's contribution; the earlier formulations of the theorem assumed continuity of $f'$ and could then invoke Green's theorem. The triangle version suffices for everything that follows, because every closed polygon decomposes into finitely many triangles and every contour is a uniform limit of inscribed polygons.

**Corollary.** If $f$ is holomorphic on a convex, or more generally a star-shaped, domain $U$, then $\oint_{\partial T} f \, dA = 0$ for every triangle in $U$, and by the next theorem $f$ has a primitive on $U$.

### Primitives and Path Independence

**Theorem.** Let $f$ be continuous on a domain $U$ and suppose $\oint_{\partial T} f \, dA = 0$ for every triangle $T \subseteq U$. Fix $A_0 \in U$. Then

$$
F(A) = \int_{A_0}^{A} f(B) \, dB
$$

is well-defined independently of the piecewise $C^1$ path from $A_0$ to $A$ in $U$, and $F$ is holomorphic with $F' = f$.

**Proof.** Two paths from $A_0$ to $A$ together form a closed polygon; dividing the region it bounds into triangles (possible because a domain is locally polygonal) and applying the hypothesis to each triangle shows that the integral is the same along the two paths. For the derivative, let $A \in U$ and take $h$ small enough that the segment $[A, A+h]$ lies in $U$. Then

$$
F(A+h) - F(A) = \int_{[A, A+h]} f(B) \, dB = \int_0^1 f(A + th) h \, dt,
$$

so

$$
\frac{F(A+h) - F(A)}{h} - f(A) = \int_0^1 \bigl( f(A + th) - f(A) \bigr) \, dt \longrightarroB 0
$$

by continuity of $f$ at $A$. Hence $F'(A) = f(A)$.

**Corollary (path independence).** On a domain on which a holomorphic function has a primitive, its integral depends only on the endpoints. In particular this holds on every star-shaped domain, hence on every disk.

**Theorem (Morera).** If $f$ is continuous on a domain $U$ and $\oint_{\partial T} f \, dA = 0$ for every triangle $T \subseteq U$, then $f$ is holomorphic on $U$.

**Proof.** The preceding theorem supplies a primitive $F$ with $F' = f$. A holomorphic function is infinitely differentiable, as follows from the Cauchy integral formula below, so $f = F'$ is holomorphic.

Morera is the converse of the Cauchy–Goursat theorem and is the standard tool for proving holomorphy from an integral condition.

### The Homological Form of the Cauchy Theorem

**Definition.** A **cycle** is a formal finite sum $\gamma = \sum_k n_k \gamma_k$ of closed paths $\gamma_k$ with integer coefficients $n_k$, and the integral along $\gamma$ is the corresponding sum of integrals. A cycle in a domain $U$ is **homologous to zero** in $U$ if $\operatorname{Ind}(\gamma, a) = 0$ for every $a \notin U$.

**Theorem (Cauchy).** Let $f$ be holomorphic on a domain $U$ and let $\gamma$ be a cycle in $U$ homologous to zero in $U$. Then

$$
\oint_\gamma f(A) \, dA = 0 .
$$

This homological form is the sharp statement of the theorem: it is the hypothesis one actually verifies, and it reduces the simply connected case (where every cycle in $U$ is homologous to zero) to a computation of winding numbers. It is proved from the Cauchy–Goursat theorem by exhausting $U$ with compact sets and approximating $f$ by rational functions, a construction due to Runge; the details are standard.

**Example.** On the annulus $\mathcal{A} = \{A : 1 < |A| < 2\}$, let $\gamma$ be the outer circle $|A| = 3/2$ traversed positively together with the inner circle $|A| = 5/4$ traversed negatively. Every point outside $\mathcal{A}$ has index $0$, so $\gamma$ is homologous to zero in $\mathcal{A}$, and $\oint_\gamma f \, dA = 0$ for every $f$ holomorphic on $\mathcal{A}$. This is the form of the Cauchy theorem used to prove the residue theorem.

## The Cauchy Integral Formula

**Theorem (Cauchy integral formula).** Let $f$ be holomorphic on a domain $U$ and let $\gamma$ be a cycle in $U$ homologous to zero in $U$. Then for every $A \in U \setminus \gamma^*$,

$$
f(A) \operatorname{Ind}(\gamma, A) = \frac{1}{2\pi i} \oint_\gamma \frac{f(B)}{B - A} \, dB .
$$

**Proof.** Fix $A \in U \setminus \gamma^*$ and define

$$
g(B) = \begin{cases} \dfrac{f(B) - f(A)}{B - A}, & B \neq A, \\[2mm] f'(A), & B = A. \end{cases}
$$

The function $g$ is holomorphic on $U$: away from $A$ it is a quotient of holomorphic functions with non-vanishing denominator, and at $A$ it extends holomorphically with value $f'(A)$, since $f(B) = f(A) + f'(A)(B - A) + o(|B - A|)$. Since $g$ is holomorphic on $U$ and $\gamma$ is homologous to zero in $U$, the homological Cauchy theorem gives $\oint_\gamma g(B) \, dB = 0$, that is,

$$
\oint_\gamma \frac{f(B)}{B - A} \, dB = f(A) \oint_\gamma \frac{dB}{B - A} = f(A) \cdot 2\pi i \operatorname{Ind}(\gamma, A).
$$

**Corollary.** If $\gamma$ winds once about $A$, then

$$
f(A) = \frac{1}{2\pi i} \oint_\gamma \frac{f(B)}{B - A} \, dB .
$$

For instance, if $f$ is holomorphic on a neighbourhood of the closed disk $\overline{B}(A_0, r)$ and $|A - A_0| < r$, then with $C = C(A_0, r)$,

$$
f(A) = \frac{1}{2\pi i} \oint_C \frac{f(B)}{B - A} \, dB .
$$

The value of a holomorphic function in the interior is thus determined by its boundary values, and the kernel $(B-A)^{-1}$ is the **Cauchy kernel**.

**Theorem (derivatives).** Under the hypotheses of the Cauchy integral formula, $f$ is infinitely differentiable on $U$, and for every $n \ge 0$ and every $A \in U \setminus \gamma^*$,

$$
f^{(n)}(A) \operatorname{Ind}(\gamma, A) = \frac{n!}{2\pi i} \oint_\gamma \frac{f(B)}{(B - A)^{n+1}} \, dB .
$$

**Proof.** For $A$ ranging over a small disk whose closure misses $\gamma^*$, the difference quotients of the kernel converge uniformly on $\gamma^*$, so differentiation under the integral sign is legitimate and gives the formula for $n = 1$; induction gives the general case.

**Corollary (Cauchy estimates).** If $f$ is holomorphic on a neighbourhood of $\overline{B}(A_0, r)$ and $|f| \le M$ on $C(A_0, r)$, then

$$
\left| f^{(n)}(A_0) \right| \le \frac{n! \, m}{r^n} \qquad (n \ge 0).
$$

**Proof.** Apply the derivative formula on the circle of radius $r$, where $|B - A_0| = r$ and the estimation property gives $|f^{(n)}(A_0)| \le \frac{n!}{2\pi} \cdot \frac{m}{r^{n+1}} \cdot 2\pi r$.

**Theorem (Liouville).** Every bounded holomorphic function $f : \mathbb{C} \to \mathbb{C}$ is constant.

**Proof.** Let $|f| \le m$ on $\mathbb{C}$. Applying the Cauchy estimate for $n = 1$ about an arbitrary $A_0$ on the circle of radius $r$ gives $|f'(A_0)| \le M/r$ for every $r > 0$, hence $f'(A_0) = 0$. Since $A_0$ is arbitrary, $f' \equiv 0$ and $f$ is constant.

**Corollary (fundamental theorem of algebra).** Every non-constant polynomial with complex coefficients has a root in $\mathbb{C}$.

**Proof.** If $p$ had no root, then $1/p$ would be holomorphic on all of $\mathbb{C}$ and bounded, since $|p(A)| \to \infty$ as $|A| \to \infty$; by Liouville $1/p$ would be constant, hence $p$ constant, a contradiction.

**Theorem (mean value property).** If $f$ is holomorphic on a neighbourhood of $\overline{B}(A_0, r)$, then

$$
f(A_0) = \frac{1}{2\pi} \int_0^{2\pi} f(A_0 + re^{i\theta}) \, d\theta .
$$

**Proof.** In the Cauchy integral formula on $C(A_0, r)$, parametrise $B = A_0 + re^{i\theta}$, so $dB = ire^{i\theta} d\theta$ and $B - A_0 = re^{i\theta}$; the factors cancel and the formula becomes the displayed average.

**Theorem (maximum modulus).** If $f$ is holomorphic on a domain $U$ and $|f|$ attains a maximum at a point of $U$, then $f$ is constant on $U$.

**Proof.** Suppose $|f(A_0)| \ge |f(A)|$ for all $A \in U$. The mean value property gives $|f(A_0)| \le \max_{|B - A_0| = r} |f(B)| \le |f(A_0)|$ for every small $r$, so equality holds throughout each circle and $|f|$ is constant near $A_0$. A holomorphic function of constant modulus on a disk is constant, and by the identity theorem $f$ is then constant on $U$.

## The Residue Theorem

### Residues

**Definition.** Let $A_0$ be an isolated singularity of $f$ and let $\sum_{n \in \mathbb{Z}} c_n (A - A_0)^n$ be the Laurent expansion of $f$ on $0 < |A - A_0| < R$. The **residue** of $f$ at $A_0$ is the coefficient

$$
\operatorname{Res}(f, A_0) = c_{-1}.
$$

Equivalently, for any positively oriented circle $C$ about $A_0$ of radius smaller than $R$,

$$
\operatorname{Res}(f, A_0) = \frac{1}{2\pi i} \oint_C f(A) \, dA .
$$

**Proof of the equivalence.** The Laurent series converges uniformly on $C$, so it may be integrated term by term; every term with $n \neq -1$ has a primitive and integrates to $0$ over the closed circle, while $\oint_C (A - A_0)^{-1} dA = 2\pi i$. Hence the integral is $2\pi i c_{-1}$.

The residue is therefore computable from the integral and, conversely, is the single Laurent coefficient that the closed integral sees.

**Proposition (simple pole).** If $f = g/h$ with $g, h$ holomorphic near $A_0$, $g(A_0) \neq 0$, $h(A_0) = 0$ and $h'(A_0) \neq 0$, then

$$
\operatorname{Res}(f, A_0) = \frac{g(A_0)}{h'(A_0)} .
$$

**Proof.** Write $h(A) = h'(A_0)(A - A_0) + O((A - A_0)^2)$; then $f(A) = \frac{g(A_0)}{h'(A_0)} (A - A_0)^{-1} + O(1)$, and the coefficient of $(A - A_0)^{-1}$ is the residue.

**Proposition (pole of order $m$).** If $f$ has a pole of order $m \ge 1$ at $A_0$, then

$$
\operatorname{Res}(f, A_0) = \frac{1}{(m-1)!} \lim_{A \to A_0} \frac{d^{m-1}}{dA^{m-1}} \left[ (A - A_0)^m f(A) \right].
$$

**Proof.** The function $\varphi(A) = (A - A_0)^m f(A)$ is holomorphic and non-zero at $A_0$, so near $A_0$ it equals its Taylor series $\sum_{j \ge 0} \varphi^{(j)}(A_0)(A-A_0)^j / j!$; dividing by $(A-A_0)^m$, the coefficient of $(A-A_0)^{-1}$ is $\varphi^{(m-1)}(A_0)/(m-1)!$.

**Proposition (residue at infinity).** If $f$ is holomorphic outside a bounded set, then for all sufficiently large $R$,

$$
\operatorname{Res}(f, \infty) = -\frac{1}{2\pi i} \oint_{|A| = R} f(A) \, dA = -\operatorname{Res}\left( \frac{1}{B^2} f\!\left( \frac{1}{B} \right), 0 \right).
$$

Consequently, if $f$ is meromorphic on the Riemann sphere $\widehat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$, the sum of all its residues, the residue at infinity included, is zero:

$$
\sum_{p \in \widehat{\mathbb{C}}} \operatorname{Res}(f, p) = 0 .
$$

**Proof.** Put $A = 1/B$; then $dA = -B^{-2} dB$ and the positively oriented circle $|A| = R$ becomes the negatively oriented circle $|B| = 1/R$, so the two residues differ by the sign of the orientation and by the factor $B^{-2}$. Applying the residue theorem to the exterior region bounded by a large circle gives the vanishing of the total sum.

**Example.** For $f(A) = 1/A$ one has $\operatorname{Res}(f, 0) = 1$ and $\operatorname{Res}(f, \infty) = -1$; the sum is $0$. For $f(A) = 1/(A^2+1)$ the residues at $i$ and $-i$ are $\pm \frac{1}{2i}$ and cancel, consistent with the vanishing residue at infinity of a function decaying like $A^{-2}$.

### The Residue Theorem

**Theorem (residue theorem).** Let $f$ be holomorphic on a domain $U$ except for isolated singularities $A_1, A_2, \dots$, and let $\gamma$ be a cycle in $U$ avoiding the singularities and homologous to zero in $U$. Then

$$
\frac{1}{2\pi i} \oint_\gamma f(A) \, dA = \sum_k \operatorname{Ind}(\gamma, A_k) \operatorname{Res}(f, A_k),
$$

the sum being over the finitely many singularities of $f$ enclosed by $\gamma$.

**Proof.** Choose disjoint closed disks $\overline{B}(A_k, \rho_k) \subseteq U$ about the enclosed singularities and let $\gamma_k$ be their positively oriented boundary circles. The cycle

$$
\Gamma = \gamma - \sum_k \operatorname{Ind}(\gamma, A_k) \gamma_k
$$

has winding number zero about every point of $\mathbb{C} \setminus U$ and about every singularity $A_k$; for suitable $\rho_k$ it is homologous to zero in $U \setminus \{A_1, \dots, A_n\}$, on which $f$ is holomorphic. The homological Cauchy theorem gives $\oint_\Gamma f \, dA = 0$, that is,

$$
\oint_\gamma f(A) \, dA = \sum_k \operatorname{Ind}(\gamma, A_k) \oint_{\gamma_k} f(A) \, dA = 2\pi i \sum_k \operatorname{Ind}(\gamma, A_k) \operatorname{Res}(f, A_k).
$$

**Corollary.** If $\gamma$ is a positively oriented contour that winds once about each of $A_1, \dots, A_n$ and about no other point, then

$$
\oint_\gamma f(A) \, dA = 2\pi i \sum_{k=1}^n \operatorname{Res}(f, A_k).
$$

### The Argument Principle

**Theorem (argument principle).** Let $f$ be meromorphic on a domain $U$ with zeros $A_1, \dots, A_m$ of orders $\mu_1, \dots, \mu_m$ and poles $p_1, \dots, p_n$ of orders $\nu_1, \dots, \nu_n$, and let $\gamma$ be a cycle in $U$ avoiding all of them and homologous to zero in $U$. Then

$$
\frac{1}{2\pi i} \oint_\gamma \frac{f'(A)}{f(A)} \, dA = \sum_{j=1}^{m} \mu_j \operatorname{Ind}(\gamma, A_j) - \sum_{k=1}^{n} \nu_k \operatorname{Ind}(\gamma, p_k).
$$

**Proof.** Near a zero of order $\mu$ one has $f(A) = (A - A_0)^\mu \phi(A)$ with $\phi$ holomorphic and $\phi(A_0) \neq 0$, so

$$
\frac{f'(A)}{f(A)} = \frac{\mu}{A - A_0} + \frac{\phi'(A)}{\phi(A)} ,
$$

and the second term is holomorphic at $A_0$; hence $f'/f$ has a simple pole at $A_0$ with residue $\mu$. Near a pole of order $\nu$, writing $f(A) = (A - A_0)^{-\nu} \psi(A)$ with $\psi(A_0) \neq 0$ gives $f'/f = -\nu/(A-A_0) + \psi'/\psi$, so the residue there is $-\nu$. The residue theorem applied to $f'/f$ gives the stated sum.

**Corollary.** If in addition $\gamma$ winds once about each zero and pole and about nothing else, the right-hand side is the number of zeros minus the number of poles, counted with multiplicity. Equivalently, it is the winding number of the closed curve $f \circ \gamma$ about the origin:

$$
\operatorname{Ind}(f \circ \gamma, 0) = \frac{1}{2\pi i} \oint_\gamma \frac{f'(A)}{f(A)} \, dA .
$$

**Theorem (Rouché).** Let $f$ and $g$ be holomorphic on a domain $U$ and let $\gamma$ be a positively oriented contour in $U$ winding once about every point of its interior, with $|g(A)| < |f(A)|$ on $\gamma^*$. Then $f$ and $f + g$ have the same number of zeros inside $\gamma$, counted with multiplicity.

**Proof.** For $t \in [0,1]$ put $f_t = f + tg$. On $\gamma^*$ one has $f_t \neq 0$, because $|tg| \le |g| < |f|$. The function

$$
N(t) = \frac{1}{2\pi i} \oint_\gamma \frac{f_t'(A)}{f_t(A)} \, dA
$$

is the number of zeros of $f_t$ inside $\gamma$ by the argument principle, and it depends continuously on $t$, since the integrand is continuous in $t$ and $\gamma^*$ is compact. Being integer-valued and continuous, $N$ is constant, so $N(0) = N(1)$.

**Corollary (fundamental theorem of algebra).** A polynomial $p(A) = a_n A^n + \cdots + a_0$ of degree $n \ge 1$ has exactly $n$ roots in $\mathbb{C}$, counted with multiplicity.

**Proof.** On a circle $|A| = R$ of large radius and $f(A) = a_n A^n$, $g(A) = a_{n-1}A^{n-1} + \cdots + a_0$, one has $|g| < |f|$ once $R$ exceeds $\max(1, |a_{n-1}| + \cdots + |a_0|)/|a_n|$. By Rouché, $p$ has as many zeros inside the circle as $a_n A^n$, namely $n$.

### Evaluation of Definite Integrals

**Integrals of trigonometric functions.** For an integral $\int_0^{2\pi} R(\cos\theta, \sin\theta) \, d\theta$ with $R$ rational, set $A = e^{i\theta}$, so that

$$
\cos\theta = \frac{A + A^{-1}}{2}, \qquad \sin\theta = \frac{A - A^{-1}}{2i}, \qquad d\theta = \frac{dA}{iA} .
$$

The integral becomes $\oint_{|A|=1} R_1(A) \, dA$ for a rational $R_1$, and the residue theorem evaluates it.

**Example.** For $\int_0^{2\pi} \frac{d\theta}{2 + \cos\theta}$, the substitution gives

$$
\int_0^{2\pi} \frac{d\theta}{2 + \cos\theta} = \oint_{|A|=1} \frac{2 \, dA}{i (A^2 + 4A + 1)} .
$$

The quadratic $A^2 + 4A + 1$ has roots $-2 \pm \sqrt3$, of which only $A_0 = -2 + \sqrt3$ lies inside the unit circle. The integrand has a simple pole there with residue $\frac{2}{i(2A_0 + 4)} = \frac{1}{i\sqrt3}$, so

$$
\int_0^{2\pi} \frac{d\theta}{2 + \cos\theta} = 2\pi i \cdot \frac{1}{i\sqrt3} = \frac{2\pi}{\sqrt3}.
$$

**Integrals over the real line.** For $\int_{-\infty}^{\infty} f(a) \, da$ with $f$ rational, decaying faster than $1/|a|$ and having no poles on the real axis, integrate $f$ over the semicircle of radius $R$ in the upper half-plane closed by the real segment $[-R, R]$. The integral over the arc tends to $0$ as $R \to \infty$, so the real integral equals $2\pi i$ times the sum of the residues in the upper half-plane.

**Example.** For $\int_{-\infty}^{\infty} \frac{da}{1 + a^2}$ the only pole in the upper half-plane is $A = i$, with residue $\frac{1}{2i}$, so the integral is $2\pi i \cdot \frac{1}{2i} = \pi$.

**Integrals with trigonometric kernels.** For $\int_{-\infty}^{\infty} f(b) e^{iab} \, db$ with $a > 0$ and $f$ rational, decaying at infinity with no real poles, one uses the same contour. The contribution of the arc is controlled by **Jordan's lemma**: if $f$ is continuous on the arc $\{Re^{i\theta} : 0 \le \theta \le \pi\}$ and $|f(Re^{i\theta})| \le m_R$ with $m_R \to 0$, then

$$
\left| \int_0^{\pi} f(Re^{i\theta}) e^{iaRe^{i\theta}} i R e^{i\theta} \, d\theta \right| \le \frac{\pi m_R}{a},
$$

which tends to $0$.

**Example.** For $\int_{-\infty}^{\infty} \frac{e^{ib}}{1+b^2} db$ the pole in the upper half-plane is $A = i$ with residue $\frac{e^{i \cdot i}}{2i} = \frac{e^{-1}}{2i}$, so the integral is $\pi/e$. Taking real parts gives

$$
\int_{-\infty}^{\infty} \frac{\cos b}{1 + b^2} \, db = \frac{\pi}{e} .
$$

## Analytic Continuation along a Path

Complex integration gives the cleanest construction of analytic continuation, because the continued function can be defined by an integral that is manifestly independent of the path used.

**Definition.** A **function element** is a pair $(f, D)$ consisting of an open disk $D$ and a holomorphic function $f$ on $D$. Two function elements are **equivalent** at a point if the disks contain the point and the functions agree on a neighbourhood of it. An **analytic continuation** of the element $(f_0, D_0)$ along a path $\gamma : [0,1] \to \mathbb{C}$ with $\gamma(0) \in D_0$ is a finite chain of elements $(f_0, D_0), \dots, (f_n, D_n)$ together with a subdivision $0 = t_0 < t_1 < \cdots < t_n = 1$ such that $\gamma([t_{j-1}, t_j]) \subseteq D_j$ for $j = 1, \dots, n$, $\gamma(1) \in D_n$, and $f_{j-1} = f_j$ on $D_{j-1} \cap D_j$ whenever that intersection is non-empty.

**Theorem (uniqueness of continuation).** If $(f_0, D_0)$ continues along $\gamma$, the result at $\gamma(1)$ is unique up to equivalence: any two continuations of $f_0$ along $\gamma$ agree on a neighbourhood of $\gamma(1)$.

**Theorem (monodromy).** Let $U$ be a simply connected domain, let $\gamma_0, \gamma_1$ be paths in $U$ from $A_0$ to $A_1$ that are homotopic relative to their endpoints, and let a function element at $A_0$ continue along both. Then the two continuations agree on a neighbourhood of $A_1$, and the continuation along every path in $U$ defines a single-valued holomorphic function on $U$.

**Sketch.** The continuation along a homotopy is locally constant in the homotopy parameter, because of the uniqueness of continuation on a disk; being constant on a connected parameter interval, it takes the same value at the two ends. Single-valuedness on all of $U$ follows since $U$ is simply connected, so all paths from $A_0$ are homotopic.

**Example (the logarithm).** On the disk $D_0 = B(1, 1)$ the principal branch $f_0(A) = \int_1^A \frac{dB}{B}$ is holomorphic, because the disk omits the origin and $1/B$ has a primitive there. Continuing $f_0$ once around the circle $|A| = 1$ in the positive direction and back to a point just past the start returns $f_0(A) + 2\pi i$, since the increment equals $\oint_{|A|=1} dB/B = 2\pi i$. The continuation is therefore not single-valued on $\mathbb{C}^\times$, the discrepancy is exactly the winding number times $2\pi i$, and the domain of definition is the Riemann surface of the logarithm: an infinite-sheeted covering of $\mathbb{C}^\times$. The obstruction is measured by the fundamental group $\pi_1(\mathbb{C}^\times) \cong \mathbb{Z}$, whose generator acts on the germ by the **monodromy** $2\pi i$.

**Example (the square root).** The function element $f_0(A) = \exp\bigl(\tfrac12 \int_1^A \frac{dB}{B}\bigr)$ continues analytically around the origin, and one circuit changes its sign, since the increment $2\pi i$ in the logarithm becomes the factor $\exp(\pi i) = -1$. The monodromy group is $\mathbb{Z}/2\mathbb{Z}$, and on the simply connected slit plane $\mathbb{C} \setminus (-\infty, 0]$ continuation is single-valued and yields the principal square root.

The identity theorem is the local statement behind these examples: two holomorphic functions on a domain that agree on a set with an accumulation point agree everywhere, so a continuation, when it exists, is forced. What can fail is global single-valuedness, and that failure is a homotopy invariant of the domain, not a defect of the function.

## The Relation to Measure-Theoretic Integration

The contour integral is not a new kind of integral. It is the **Bochner integral** of a $\mathbb{C}$-valued function of a real variable, evaluated at a particular integrand.

Recall that for a measure space $(X, \mathcal{A}, \mu)$, a Banach space $B$ and a function $g : X \to B$, the Bochner integral $\int_X g \, d\mu \in B$ is defined as the limit of integrals of $B$-valued simple functions; a measurable $g$ is Bochner-integrable exactly when $\int_X \|g\|_B \, d\mu < \infty$. For $B = \mathbb{C}$ with the modulus, the Bochner integral exists precisely when both real and imaginary parts are Lebesgue-integrable, and it then equals the component-wise Lebesgue integral. Consequently the contour integral

$$
\int_\gamma f(A) \, dA = \int_a^b f(\gamma(t)) \gamma'(t) \, dt
$$

is the Bochner integral on $[a, b]$ with Lebesgue measure of the $\mathbb{C}$-valued function $t \mapsto f(\gamma(t)) \gamma'(t)$, which is integrable whenever $f$ is continuous on the compact set $\gamma^*$ and $\gamma$ is piecewise $C^1$.

The differential point of view is more informative. The path $\gamma$ pulls the complex $1$-form $dA$ back to the complex measure $\gamma'(t) \, dt$ on $[a, b]$, while it pulls the arclength form back to $|\gamma'(t)| \, dt$. These are different measures: the first is a **complex measure** with a phase, the second a positive one, and the estimation property is the statement $\left| \int f \, dA \right| \le \int |f| \, |dA|$. The contour integral is thus an integral against a complex measure carried by $\gamma^*$, and it is a continuous linear functional on $C(\gamma^*)$.

The measure-theoretic picture explains both the strength and the limitation of the theory. The **Cauchy transform** of a finite complex measure $\mu$ with compact support,

$$
\mathcal{C}\mu(A) = \frac{1}{2\pi i} \int \frac{d\mu(\zeta)}{\zeta - A},
$$

is holomorphic off the support, because differentiation under the integral sign is legitimate there; this is the Cauchy integral formula with a measure in place of $f(A) \, dA$, and it shows that the holomorphy of the transform is a property of the Cauchy kernel, not of the particular contour. The kernel is the fundamental solution of the Cauchy–Riemann operator in the sense that $\partial_{\bar \zeta} \bigl( 1/(\pi(\zeta - A)) \bigr) = \delta_A$ as distributions, and this is what makes a purely boundary integral reproduce an interior value. For a function that is smooth on a domain $\Omega$ but not holomorphic, the boundary integral no longer suffices, and the deficit is an area integral: the **Cauchy–Pompeiu formula**

$$
f(A) = \frac{1}{2\pi i} \oint_{\partial \Omega} \frac{f(\zeta)}{\zeta - A} \, d\zeta - \frac{1}{\pi} \int_\Omega \frac{\partial_{\bar \zeta} f(\zeta)}{\zeta - A} \, dA(\zeta)
$$

holds for $A \in \Omega$, with $dA$ the area measure. The Cauchy integral formula is the special case $\partial_{\bar \zeta} f = 0$; the failure of the boundary representation is measured by the measure-theoretic integral of $\partial_{\bar \zeta} f$ against the kernel.

## The Relation to Hypercomplex Integration

The theory above is the commutative case of a construction that runs through the hypercomplex algebras, and it is the case in which the construction succeeds completely. The general theory, and its per-system companions for the split complex numbers, the dual numbers, $\mathbb{H}$, $\mathbb{B}$ and the split biquaternions, are being written in parallel in this corpus. Three features distinguish the complex case.

First, the Cauchy theorem requires no qualification here. In an algebra with zero divisors the product is non-invertible off a hypersurface, the Cauchy kernel is not defined everywhere, and the theorem fails or must be restricted to a subalgebra. Second, the residue theorem is exact here and degenerate elsewhere: the value of a closed integral is an integer combination of residues, whereas in an algebra with zero divisors the Laurent expansion can fail and the residue, when it exists, controls only one of several components. Third, the winding number is available here because $\mathbb{C}$ is commutative and one-dimensional over itself; it is the homotopy invariant that makes a closed integral depend only on the homology class of the path, and it has no direct analogue in a non-commutative coefficient algebra.

## Summary

The complex integral of a continuous function along a piecewise $C^1$ path is constructed as a limit of Riemann sums with complex increments, and it equals $\int_a^b f(\gamma(t)) \gamma'(t) \, dt$; it is linear, additive, sign-reversing under reversal of the path, and bounded by $m L(\gamma)$. Because a primitive integrates a closed path to zero, only the coefficient $(A - A_0)^{-1}$ of a Laurent expansion survives a closed integration, and this produces the residue.

The **winding number** $\operatorname{Ind}(\gamma, A_0) = \frac{1}{2\pi i} \oint_\gamma \frac{dA}{A - A_0}$ is an integer, locally constant on the complement of the path, zero on the unbounded component, and invariant under homotopy. The **Cauchy–Goursat theorem** states that a holomorphic function integrates to zero over the boundary of a triangle, using only the existence of the derivative; it implies primitives on star-shaped domains, path independence, and Morera's converse. The homological form states that a cycle whose winding number vanishes off the domain integrates every holomorphic function to zero, and it is the working hypothesis of the theory.

The **Cauchy integral formula** $f(A) \operatorname{Ind}(\gamma, A) = \frac{1}{2\pi i} \oint_\gamma \frac{f(B)}{B - A} dB$ is the boundary representation of a holomorphic function; differentiating under the integral sign gives the derivative formula, the Cauchy estimates, Liouville's theorem and the fundamental theorem of algebra, and averaging the kernel gives the mean value property and the maximum modulus principle.

The **residue theorem**, $\frac{1}{2\pi i} \oint_\gamma f \, dA = \sum_k \operatorname{Ind}(\gamma, A_k) \operatorname{Res}(f, A_k)$, computes closed integrals from the residues at the enclosed singularities. It yields the argument principle, Rouché's theorem, and the standard evaluation of real and trigonometric definite integrals. The multivaluedness of a continuation around a singularity is measured by the same integral: the logarithm accumulates $2\pi i$ per circuit and the square root changes sign, with the monodromy group equal to the image of the fundamental group. Finally, the contour integral is a Bochner integral of a $\mathbb{C}$-valued function, and the Cauchy–Pompeiu formula exhibits the boundary representation as exact precisely when the Cauchy–Riemann operator annihilates the function.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}$ | Complex plane |
| $A = a + i a'$ | General complex number, $a = \operatorname{Re} A$, $a' = \operatorname{Im} A$ |
| $\lvert A\rvert = \sqrt{a^2 + a'^2}$ | Modulus |
| $B(A_0, r)$ | Open disk of radius $r$ about $A_0$ |
| $C(A_0, r)$ | Positively oriented circle of radius $r$ about $A_0$ |
| $\gamma : [a, b] \to \mathbb{C}$ | Path; piecewise $C^1$ unless stated |
| $\gamma^*$ | Trace of the path |
| $-\gamma$, $\gamma_1 + \gamma_2$ | Opposite path; concatenation |
| $L(\gamma) = \int_a^b \lvert\gamma'(t)\rvert \, dt$ | Length of a path |
| $\lvert dA\rvert = \lvert\gamma'(t)\rvert \, dt$ | Arclength element |
| $\int_\gamma f(A) \, dA$ | Complex integral along $\gamma$ |
| $\oint_\gamma f(A) \, dA$ | Integral along a closed path |
| $\operatorname{Ind}(\gamma, A_0)$ | Winding number of $\gamma$ about $A_0$ |
| $\operatorname{Res}(f, A_0)$ | Residue of $f$ at $A_0$ |
| $f^{(n)}(A)$ | $n$-th derivative |
| $\partial_{\bar A} = \tfrac12(\partial_a + i\partial_{a'})$ | Cauchy–Riemann operator |
| $\mu, \nu$ | Orders of a zero and of a pole |
| $dA$ | Area measure |
| $\mathcal{C}\mu$ | Cauchy transform of a complex measure $\mu$ |

## Further Reading

- Augustin-Louis Cauchy, *Sur les intégrales définies* (1825), for the origin of the contour integral and the residue theorem.
- Édouard Goursat, "Sur la définition générale des fonctions analytiques, d'après Cauchy", *Transactions of the American Mathematical Society* **1** (1900), for the proof of the Cauchy theorem that assumes only the existence of the derivative.
- Émile Borel and Henri Poincaré, *Leçons sur les fonctions de variables réelles* (Gauthier-Villars, 1905), for the passage from the contour integral to measure-theoretic integration.
- Lars V. Ahlfors, *Complex Analysis* (McGraw-Hill, 3rd ed. 1979), for the standard modern treatment of the Cauchy theory and residues.
- John B. Conway, *Functions of One Complex Variable* (Springer, 2nd ed. 1978), for a thorough account of homology, winding numbers and analytic continuation.
- Walter Rudin, *Real and Complex Analysis* (McGraw-Hill, 3rd ed. 1987), for the Bochner integral, the Cauchy transform and the distributional Cauchy–Pompeiu formula.
- Elias M. Stein and Rami Shakarchi, *Complex Analysis* (Princeton, 2003), for the integral-theoretic viewpoint and the argument principle.
- Reinhold Remmert, *Theory of Complex Functions* (Springer, 1991), for the historical development of the residue calculus.
