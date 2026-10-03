
# __Dual-Numbers Integration__

## Introduction

This article develops integration for functions of one dual variable. It follows *Dual-Numbers Analysis*, which fixed the dual plane, its Euclidean topology, dual differentiability and the dual Cauchy–Riemann equations, and it follows *Dual-Numbers Algebra* for the ring $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$, the maximal ideal $\mathrm{M} = (\varepsilon)$, the dual conjugation and the norm $N(A) = a^2$. The contour integral was introduced there as a definition; here it is developed as a subject in its own right, and the question addressed is exactly how much of the Cauchy theory survives when the coefficient ring has nilpotents and is not a field.

The algebraic statements below hold over any commutative ring $R$, but the integral itself is an analytic object and requires a complete ordered field of coefficients. Throughout, therefore, the base is $\mathbb{R}$ and the algebra is $\mathbb{D}' = \mathbb{D}'_{\mathbb{R}} = \mathbb{R}[\varepsilon]/(\varepsilon^2)$; the algebraic ingredients — the local structure, the group of units and the derivations — specialise to any such ring unchanged. The general shape of the integral theorems, and the place of the present theory among its companions for $\mathbb{C}$, $\mathbb{D}$, $\mathbb{H}$ and $\mathbb{B}$, is the subject of *Hypercomplex Integration*, and the closest neighbouring case, where the coefficient ring has zero divisors but no nilpotents, is *Split-Complex Integration*.

Two algebraic facts govern everything that follows. First, $\mathbb{D}'$ is a **local ring**: it has the unique maximal ideal $\mathrm{M} = \varepsilon\mathbb{R}$, which is nilpotent of index two, $\mathrm{M}^2 = 0$, and the augmentation

$$
\pi : \mathbb{D}' \to \mathbb{R}, \qquad \pi(a + \varepsilon a') = a,
$$

is a ring homomorphism whose kernel is $\mathrm{M}$. The algebra is the trivial extension $\mathbb{D}' = \mathbb{R} \oplus \mathrm{M}$ of the field $\mathbb{R}$ by the square-zero ideal $\mathrm{M}$. Second, the norm $N(A) = A\bar A = a^2$ is **degenerate**: it vanishes on the whole of $\mathrm{M}$, so it does not detect the infinitesimal part.

These two facts divide the classical Cauchy theory cleanly. The **vanishing** statement — the integral of a dual differentiable function over a closed path is zero — survives, and it holds on every domain, with no simple-connectivity hypothesis. But it is *soft*: its hypothesis is the differentiability condition, which forces the function into a form in which a primitive can be written down explicitly, so the theorem excludes nothing and constrains no topology. The **reconstruction** statement — the Cauchy integral formula that recovers an interior value from a boundary integral, and with it the residue theorem, the Cauchy estimates, the mean value property and the Laurent expansion — does not survive, and the obstruction is exactly the nilpotent ideal. The Cauchy kernel $(\zeta - A_0)^{-1}$ is defined only where $\zeta - A_0$ is a unit, that is only off the fibre $\pi^{-1}(\pi(A_0))$; no contour of non-zero winding about $A_0$ avoids that fibre.

What replaces the reconstruction half is a **derived** statement. Because the infinitesimal direction is nilpotent, a dual differentiable function is determined by its restriction to the real axis together with one derivative, and integration along a fibre evaluates the real part rather than reconstructing a general value from a boundary integral. In this sense the derived variable — the nilpotent coordinate — carries the information that a Cauchy integral would carry in the complex case.

No physics is invoked. The dual plane is used as the two-dimensional real algebra fixed in *Dual-Numbers Algebra*, and the operator notation $\partial_A, \partial_{\bar A}$ is the one fixed in *Dual-Numbers Analysis*.

Notation: $A = a + \varepsilon a'$ with $a, a' \in \mathbb{R}$, $\bar A = a - \varepsilon a'$, $\operatorname{Re} A = a$, $\operatorname{Inf} A = a'$, and $\|A\|_E = \sqrt{a^2 + a'^2}$. The maximal ideal is $\mathrm{M} = \varepsilon\mathbb{R}$.

## The Dual Integral

### Paths and Contours

**Definition.** A **path** is a continuous map $\gamma : [a,b] \to \mathbb{D}'$. It is **piecewise continuously differentiable**, written piecewise $C^1$, if there is a finite subdivision $a = t_0 < t_1 < \cdots < t_n = b$ such that $\gamma$ is continuously differentiable on each closed subinterval $[t_{k-1}, t_k]$. A path is **closed** if $\gamma(a) = \gamma(b)$ and **simple** if it is injective on $[a,b)$; a simple closed path is a **contour**.

The **trace** of $\gamma$ is the compact set $\gamma^* = \gamma([a,b])$. The **opposite** path $-\gamma$ is $t \mapsto \gamma(a + b - t)$, and if $\gamma_1 : [a,b] \to \mathbb{D}'$ and $\gamma_2 : [b,c] \to \mathbb{D}'$ agree at $b$, their **concatenation** $\gamma_1 + \gamma_2$ follows first one and then the other. The **length** of a piecewise $C^1$ path is

$$
L(\gamma) = \int_a^b \|\gamma'(t)\|_E \, dt,
$$

finite because $\gamma'$ is piecewise continuous on a compact interval. Two paths recur below: the Euclidean circle $\gamma(t) = A_0 + r(\cos t + \varepsilon\sin t)$, a contour of length $2\pi r$, and the fibre segment $\sigma(t) = a_0 + t\varepsilon$, $t \in [b_0, b_1]$, which lies in the single fibre $\pi^{-1}(a_0)$ and has length $|b_1 - b_0|$.

### Construction from the Riemann Sum

**Definition.** Let $\gamma : [a,b] \to \mathbb{D}'$ be piecewise $C^1$ and let $f$ be continuous on a neighbourhood of $\gamma^*$. Given a subdivision $a = t_0 < t_1 < \cdots < t_n = b$ and sample points $\tau_k \in [t_{k-1}, t_k]$, set $A_k = \gamma(t_k)$ and form the **Riemann sum**

$$
S = \sum_{k=1}^{n} f(\gamma(\tau_k))\,(A_k - A_{k-1}).
$$

With $\|\Delta\| = \max_k (t_k - t_{k-1})$, the **dual integral** of $f$ along $\gamma$ is the limit

$$
\int_\gamma f(A)\,dA = \lim_{\|\Delta\| \to 0} S.
$$

**Theorem.** For piecewise $C^1$ $\gamma$ and continuous $f$ the Riemann sums converge, and

$$
\int_\gamma f(A)\,dA = \int_a^b f(\gamma(t))\,\gamma'(t)\,dt.
$$

**Proof.** The product in $\mathbb{D}'$ is bilinear and $f$ is continuous, so the argument of the complex case applies verbatim. On each smooth piece,

$$
A_k - A_{k-1} = \int_{t_{k-1}}^{t_k} \gamma'(t)\,dt = \gamma'(\tau_k)(t_k - t_{k-1}) + \rho_k, \qquad \|\rho_k\|_E \leq \omega(\|\Delta\|)(t_k - t_{k-1}),
$$

with $\omega(\|\Delta\|) \to 0$ by uniform continuity of $\gamma'$ on the finitely many pieces. Hence $S$ differs from the Riemann sum of $t \mapsto f(\gamma(t))\gamma'(t)$ by a term bounded in norm by $\max_{\gamma^*}\|f\|_E \,\omega(\|\Delta\|)(b-a) \to 0$.

The integral exists because $\mathbb{D}'$ is a complete normed space under $\|\cdot\|_E$, exactly as $\mathbb{C}$ is under the modulus. Completeness is what makes the limit of Riemann sums legitimate, and it is not affected by the nilpotence of $\varepsilon$.

### Basic Properties

Linearity, reversal, additivity and reparametrisation hold exactly as in *Dual-Numbers Analysis*: the integral is $\mathbb{D}'$-linear in the integrand, changes sign under $-\gamma$, is additive under concatenation, and is invariant under a piecewise $C^1$ orientation-preserving reparametrisation (with a sign change if the orientation is reversed). The one property that needs care is estimation, because the Euclidean norm is not multiplicative.

**Estimation.** If $\|f(A)\|_E \leq m$ on $\gamma^*$, then

$$
\left\|\int_\gamma f(A)\,dA\right\|_E \leq \frac{2}{\sqrt3}\,m\,L(\gamma).
$$

**Proof.** The multiplication map $A \mapsto AB$ for $B = c + \varepsilon c'$ has matrix

$$
M(B) = \begin{pmatrix} c & 0 \\ c' & c \end{pmatrix}
$$

in the basis $(1, \varepsilon)$, so $\|AB\|_E \leq \|M(B)\|_{\mathrm{op}} \|A\|_E$. The eigenvalues of $M(B)^{\mathsf{T}} M(B)$ are

$$
\lambda_\pm = \frac{2c^2 + c'^2 \pm \sqrt{c'^4 + 4c^2c'^2}}{2},
$$

so $\|M(B)\|_{\mathrm{op}}^2 = \lambda_+$. Dividing by $\|B\|_E^2 = c^2 + c'^2$ and maximising over the ratio $c^2/c'^2$ gives the supremum $\tfrac43$, attained when $c^2 = 2c'^2$; hence

$$
\|AB\|_E \leq \frac{2}{\sqrt3}\,\|A\|_E\|B\|_E
$$

with equality, for instance, at $A = B = \sqrt{2/3} + \varepsilon\,\sqrt{1/3}$. Applying this to $f(\gamma(t))\gamma'(t)$ and integrating gives the estimate.

**Remark.** The Euclidean norm is **not** submultiplicative on $\mathbb{D}'$, and $2/\sqrt3$ is the best constant. In particular the naive estimate $\|\int_\gamma f\,dA\|_E \leq M L(\gamma)$, obtained by bounding $\|f(\gamma(t))\gamma'(t)\|_E$ pointwise by $\|f\|_E\|\gamma'\|_E$, is not available, because that pointwise inequality is false; the factor $2/\sqrt3$ is exactly what replaces it. This is the first sign that the Euclidean metric and the nilpotent multiplication are not aligned. In $\mathbb{C}$ the modulus is multiplicative and the constant is $1$; in $\mathbb{D}$ the best constant is $\sqrt2$, attained on the null cone; in $\mathbb{D}'$ it is $2/\sqrt3$, which lies between them, and it is attained when $A = B$ and $\operatorname{Re}(B)^2 = 2\operatorname{Inf}(B)^2$, so no element of the zero-divisor set is extremal. The constant is a feature of the algebra alone and has no counterpart in the complex theory.

## Integration Along the Fibre

### The Augmentation and Its Fibres

The augmentation $\pi : \mathbb{D}' \to \mathbb{R}$ is the unique unital ring homomorphism onto $\mathbb{R}$, and its kernel is the maximal ideal $\mathrm{M}$. Its **fibres** are the sets

$$
\pi^{-1}(a) = a + \mathrm{M} = \{a + \varepsilon a' : a' \in \mathbb{R}\},
$$

which are the cosets of $\mathrm{M}$ and the straight lines parallel to the nilpotent direction. Every fibre is a copy of $\mathbb{R}$, and the algebra is the disjoint union of its fibres over the points of $\mathbb{R}$. The projection $\pi$ is the algebraic content of the phrase "the real part": the fibre through $A$ is the set of dual numbers indistinguishable from $A$ by the norm, since $N(a + \varepsilon a') = a^2$ is constant on it.

### Decomposition into Two Real Integrals

Write

$$
f(A) = u(a,a') + v(a,a')\,\varepsilon, \qquad u, v : U \to \mathbb{R}.
$$

Since $dA = da + \varepsilon\,da'$, the product $f\,dA$ expands without any use of $\varepsilon^2$ as

$$
f(A)\,dA = u\,da + \bigl(u\,da' + v\,da\bigr)\varepsilon.
$$

**Theorem (fibre decomposition).** Let $\gamma : [a,b] \to U$ be piecewise $C^1$ and let $f = u + v\varepsilon$ be continuous on a neighbourhood of $\gamma^*$. Then

$$
\int_\gamma f(A)\,dA = \int_\gamma u\,da + \varepsilon\left(\int_\gamma u\,da' + \int_\gamma v\,da\right),
$$

where each integral on the right is an ordinary real line integral of a real $1$-form, taken over the projections $t \mapsto a(\gamma(t))$ and $t \mapsto a'(\gamma(t))$.

**Proof.** Multiply $f(\gamma(t))$ by $\gamma'(t) = \dot a + \varepsilon\,\dot a'$ (the dot denotes $d/dt$) and expand, using that $\varepsilon^2 = 0$, to obtain

$$
f(\gamma(t))\gamma'(t) = u\,\dot a + \bigl(u\,\dot a' + v\,\dot a\bigr)\varepsilon,
$$

with $u, v$ evaluated at $\gamma(t)$. Each component is an ordinary real function of $t$, so the integral separates componentwise.

So a dual integral is exactly a pair of real line integrals, and — unlike the split complex case — the two are not independent: the infinitesimal part uses the real part $u$ as well as $v$. The decomposition is not into two copies of the algebra but into the real part and the nilpotent part, and this asymmetry is the analytic form of $\mathrm{M}^2 = 0$.

**Corollary.** For a closed path $\gamma$ the real part of $\oint_\gamma f\,dA$ is $\oint_\gamma u\,da$, and if $u$ depends only on $a$ then $u\,da$ is exact and this vanishes. In particular it vanishes for every dual differentiable $f$, for which the whole integral vanishes by the Cauchy–Goursat theorem below. For a differentiable integrand the infinitesimal component vanishes as well, so the algebra structure is invisible on the differentiable class; it is the infinitesimal component, built from the two real $1$-forms $u\,da'$ and $v\,da$, that detects the failure of differentiability, and the area detector of the next section is the first instance.

### The Fibre Integral as an Evaluation

The behaviour of the integral along a single fibre is the exact analogue of integration along a characteristic in the split complex case, and it is where the derived variable first appears.

**Theorem (fibre evaluation).** Let $f = u + v\varepsilon$ be continuous on a neighbourhood of the segment $\sigma(t) = a_0 + t\varepsilon$, $t \in [b_0, b_1]$. Then

$$
\int_\sigma f(A)\,dA = \left(\int_{b_0}^{b_1} u(a_0, t)\,dt\right)\varepsilon.
$$

If in addition $u$ does not depend on $a'$ — in particular if $f$ is dual differentiable — this reduces to $(b_1 - b_0)\,u(a_0)\,\varepsilon = (b_1 - b_0)\,\operatorname{Re} f(a_0)\,\varepsilon$.

**Proof.** Along $\sigma$ one has $\dot a = 0$ and $\dot a' = 1$, so $f(\sigma(t))\sigma'(t) = (u(a_0,t) + v\varepsilon)\varepsilon = u(a_0,t)\,\varepsilon$, a purely infinitesimal quantity. The real part of the integrand is zero, and the infinitesimal part integrates to $\varepsilon\int_{b_0}^{b_1}u(a_0,t)\,dt$.

Thus integration along a fibre is not a reconstruction but an **evaluation**: for a differentiable integrand it returns the real part of $f$ at the base point, multiplied by the length of the segment, and it is completely blind to the infinitesimal part. A single fibre therefore plays the role that a small circle plays in the complex Cauchy formula, but it probes one real number rather than the value of a holomorphic function.

### The Nilpotent Direction

The nilpotence of $\varepsilon$ makes the fibre direction **totally isotropic** for integration. Let $\sigma_1$ and $\sigma_2$ be two segments in the same fibre. By the evaluation theorem the inner integral is a constant multiple of $\varepsilon$, say $\int_{\sigma_1} f\,dA = C\varepsilon$, and integrating that constant along $\sigma_2$ multiplies it by a further fibre increment $dA = \varepsilon\,dt$, producing $\varepsilon^2 = 0$:

$$
\int_{\sigma_2}\Bigl(\int_{\sigma_1} f\,dA\Bigr) dA = C\varepsilon\int_{\sigma_2} dA = C\varepsilon\cdot(b_2 - b_1)\varepsilon = 0.
$$

Equivalently, iterating the fibre integration multiplies two infinitesimal increments and therefore annihilates them; the segment $\sigma_1$ has finite Euclidean length, but its second-order contribution vanishes. This is the precise sense in which the nilpotent direction is a direction the integral cannot iterate.

## Closedness and the Dual Cauchy–Goursat Theorem

### The Exterior Derivative of $f\,dA$

A $\mathbb{D}'$-valued $1$-form on $U$ is an expression $P\,da + Q\,da'$ with $P, Q : U \to \mathbb{D}'$; it is **closed** if $d\omega = 0$, that is if $\partial_{a'} P = \partial_a Q$ on $U$, and **exact** if $\omega = dF$ for some dual-valued function $F$. A closed form is exact on a simply connected domain, and for the forms $f\,dA$ considered here exactness holds on every domain, by the primitive constructed below. A direct computation gives the closedness criterion.

**Theorem.** Let $f = u + v\varepsilon$ be $C^1$ on a domain $U$. Then the form $f\,dA = P\,da + Q\,da'$ with $P = u + v\varepsilon$ and $Q = u\varepsilon$ is closed if and only if

$$
\frac{\partial u}{\partial a'} = 0, \qquad \frac{\partial v}{\partial a'} = \frac{\partial u}{\partial a}.
$$

**Proof.** For a $\mathbb{D}'$-valued form $P\,da + Q\,da'$ with $C^1$ coefficients, closedness is equivalent to $\partial_{a'} P = \partial_a Q$; this is the two-variable real criterion applied to each of the two components. Here $\partial_{a'} P = u_{a'} + v_{a'}\varepsilon$ and $\partial_a Q = u_a\varepsilon$, and the two agree exactly when the real parts agree, $u_{a'} = 0$, and the coefficients of $\varepsilon$ agree, $v_{a'} = u_a$.

Equivalently, with the dual Wirtinger operator of *Dual-Numbers Analysis*,

$$
\frac{\partial}{\partial \bar A} = \frac{\partial}{\partial a'} - \varepsilon\frac{\partial}{\partial a},
$$

one has $\partial_{\bar A} f = u_{a'} + (v_{a'} - u_a)\varepsilon$, so the form $f\,dA$ is closed if and only if $\partial_{\bar A} f = 0$.

### The Dual Cauchy–Riemann Equations

**Theorem (Cauchy–Riemann, dual form).** Let $f = u + v\varepsilon$ be real differentiable on a domain $U$. The following are equivalent.

1. $f$ is dual differentiable on $U$.
2. $\partial_{\bar A} f = 0$ on $U$, that is $u_{a'} = 0$ and $v_{a'} = u_a$.
3. The form $f\,dA$ is closed on $U$.

**Proof.** The equivalence of (1) and (2) is the dual Cauchy–Riemann theorem of *Dual-Numbers Analysis*. The equivalence of (2) and (3) is the computation just made.

**Corollary (structure of a differentiable function).** A dual differentiable $f$ on $U$ has the form

$$
f(a + \varepsilon a') = u(a) + \bigl(a'\,u'(a) + c(a)\bigr)\varepsilon,
$$

where $u$ and $c$ are ordinary differentiable functions of one real variable, and then $f'(A) = u'(a) + \bigl(a'\,u''(a) + c'(a)\bigr)\varepsilon$. So a differentiable dual function is determined by two ordinary differentiable functions of one variable.

The corollary is the reason every statement of the vanishing half of the theory is soft: the class of integrands is rigid, and its elements are written down by ordinary calculus.

### The Cauchy–Goursat Theorem

**Theorem (Cauchy–Goursat, dual form).** Let $f$ be dual differentiable on a domain $U$ and let $\gamma$ be a closed piecewise $C^1$ path in $U$. Then

$$
\oint_\gamma f(A)\,dA = 0.
$$

**Proof.** By the corollary, $f = u(a) + (a'u'(a) + c(a))\varepsilon$ with $u, c$ continuous on the projection of $U$. Choose ordinary antiderivatives $A$ of $u$ and $C$ of $c$ and set

$$
F(a + \varepsilon a') = A(a) + \bigl(a'\,u(a) + C(a)\bigr)\varepsilon.
$$

The real part $A(a)$ satisfies $\partial_{a'} A = 0$, and the infinitesimal part $\phi = a'u(a) + C(a)$ satisfies $\phi_{a'} = u(a) = A'(a)$, so $F$ is dual differentiable and $F' = f$. Along a piecewise $C^1$ path, $\frac{d}{dt}F(\gamma(t)) = F'(\gamma(t))\gamma'(t) = f(\gamma(t))\gamma'(t)$, and the fundamental theorem of calculus gives $\int_\gamma f\,dA = F(\gamma(b)) - F(\gamma(a))$, which vanishes for a closed path.

**Theorem (primitive).** Every dual differentiable function on a domain $U$ has a primitive on $U$, and the integral is given by the endpoint formula

$$
\int_\gamma f(A)\,dA = F(\gamma(b)) - F(\gamma(a)).
$$

**Proof.** The function $F$ constructed above is defined on all of $U$, and its construction uses only that $u$ and $c$ are continuous functions of one real variable on the intervals that are the projections of $U$.

### The Softness of the Theorem

The Cauchy–Goursat theorem holds in $\mathbb{D}'$ for a reason that gives it no force. The primitive exists on **every** domain, with no simple-connectivity hypothesis, because each of the two functions $u, c$ is a function of a single real variable and a continuous one-variable function always has an antiderivative. Consequently:

- The theorem is a statement about the differentiability of $f$, not about the shape of $U$; the fundamental group of the domain never enters.
- Since the primitive exists everywhere, there is no obstruction theory and no period: no closed integral can be non-zero for a differentiable integr, on any domain.
- The topological content that the complex Cauchy theorem carries — the winding number, the residue, the distinction between simply connected and multiply connected domains — has no counterpart here.

What does survive of path independence is therefore only the positive direction. The integral of a differentiable function is path-independent, but for the trivial reason that the primitive is explicit, and this path independence carries no information about $U$.

**Remark (a failing converse).** In the complex theory the vanishing of closed integrals *characterises* holomorphy and *forces* a primitive. Here the implication is one-way in content: closedness of $f\,dA$ does characterise differentiability, but it delivers nothing further, because differentiability alreada' delivers the primitive. This is the precise sense in which the dual vanishing theorem is the degenerate end of the general theory.

### The Rectangle Criterion

The Cauchy–Goursat theorem has a partial converse, and in the dual case — as in the split complex case — it stops one step short of differentiability.

**Theorem (rectangle criterion).** For a continuous $f : U \to \mathbb{D}'$ the following are equivalent.

1. $\oint_{\partial R} f(A)\,dA = 0$ for every axis-parallel rectangle $R \subseteq U$.
2. $f = F'$ for some dual differentiable $F$ on $U$; equivalently $f = A'(a) + (a'A''(a) + C'(a))\varepsilon$, where $F = A(a) + (a'A'(a) + C(a))\varepsilon$ is the structure form of $F$.

**Proof.** If $f = F'$ with $F$ dual differentiable, then $\oint_{\partial R} f\,dA = 0$ for every closed path by the primitive theorem. Conversely, integrate $f$ from a fixed base point along axis-parallel paths to define $F$; two such paths differ by the boundaries of the rectangles between them, so the rectangle hypothesis makes $F$ well defined. The standard difference-quotient computation along a horizontal and a vertical segment gives $\partial_a F = f$ and $\partial_{a'} F = \varepsilon f$; taking real and infinitesimal parts, $(\operatorname{Re}F)_{a'} = 0$ and $(\operatorname{Inf}F)_{a'} = \operatorname{Re}f = (\operatorname{Re}F)_a$, so $F$ is dual differentiable and $F' = f$. The structure theorem applied to $F$ gives the second form of (2).

**Remark (no regularity upgrade).** In $\mathbb{C}$ the rectangle hypothesis upgrades a merely continuous $f$ to a holomorphic one, because the primitive of a continuous function is holomorphic and the derivative of a holomorphic function is holomorphic. No such upgrade is available here, and the class of dual differentiable functions is not closed under differentiation. For the differentiable function

$$
F(A) = |a|^{3} + 3\,a'\,a\,|a|\,\varepsilon, \qquad A = a + \varepsilon a',
$$

the real part $u(a) = |a|^{3}$ and the infinitesimal part $v(a,a') = 3a'a|a|$ are real differentiable with $v_{a'} = 3a|a| = u_a$, so $F$ is dual differentiable; its derivative

$$
F'(A) = 3\,a\,|a| + 6\,a'\,|a|\,\varepsilon
$$

is not, because the infinitesimal part $6a'|a|$ has no $a$-derivative on the fibre $a = 0$ when $a' \neq 0$. The criterion therefore characterises the class of derivatives of dual differentiable functions, not the class of dual differentiable functions itself, and this is the exact analogue of the split complex situation. It is a further face of the failure of the reconstruction half of the theory.

### The Area Detector

The vanishing theorem would be empty if *every* continuous density had vanishing closed integrals. It does not, and the detecting device is the dual conjugate.

**Example.** Let $f(A) = \bar A = a - \varepsilon a'$ and let $\gamma$ be a closed contour. Then

$$
\oint_\gamma \bar A\,dA = \oint_\gamma a\,da + \varepsilon\oint_\gamma \bigl(a\,da' - a'\,da\bigr) = 2\,\operatorname{Area}(\gamma)\,\varepsilon,
$$

where $\operatorname{Area}(\gamma)$ is the signed Euclidean area enclosed by $\gamma$. The real part vanishes because $a\,da$ is exact, and the infinitesimal part is twice the area by Green's theorem. So $\bar A$ is not dual differentiable, and the dual integral detects the failure by returning an area rather than zero.

The detector returns an area, not an integer winding number: the quantity that survives is not homotopy-invariant, and this is the analytic face of the absence of a residue.

## The Obstruction to the Cauchy Integral Formula

### The Dual Cauchy Kernel

**Proposition.** Let $A_0 \in \mathbb{D}'$. The element $\zeta - A_0$ is a unit if and only if $\operatorname{Re}\zeta \neq \operatorname{Re} A_0$, and for such $\zeta$

$$
(\zeta - A_0)^{-1} = \frac{1}{\operatorname{Re}(\zeta - A_0)} - \frac{\operatorname{Inf}(\zeta - A_0)}{\operatorname{Re}(\zeta - A_0)^2}\,\varepsilon.
$$

**Proof.** Write $\zeta - A_0 = a + \varepsilon a'$ with $a = \operatorname{Re}(\zeta - A_0)$, $a' = \operatorname{Inf}(\zeta - A_0)$. By *Dual-Numbers Algebra* this is a unit if and only if $a \neq 0$, with inverse $a^{-1} - a^{-2}\varepsilon a'$.

So the set on which the Cauchy kernel is defined is not the punctured neighbourhood of $A_0$ but its complement in the whole fibre

$$
L_{A_0} = \pi^{-1}(\pi(A_0)) = \{\zeta : \operatorname{Re}\zeta = \operatorname{Re} A_0\}.
$$

The kernel is undefined on an entire line through $A_0$, not merely at $A_0$.

### No Contour Avoids the Fibre

**Theorem (obstruction).** There is no Cauchy integral formula in $\mathbb{D}'$ that recovers $f(A_0)$ from a contour integral of $f$ against the kernel $(\zeta - A_0)^{-1}$ along a contour $\gamma$ winding once about $A_0$.

**Proof.** A closed contour with non-zero winding number about $A_0$ meets both open half-planes $\{\operatorname{Re}\zeta > \operatorname{Re} A_0\}$ and $\{\operatorname{Re}\zeta < \operatorname{Re} A_0\}$; otherwise it would lie in a closed half-plane whose boundary contains $A_0$, a convex set in which $A_0$ has no interior, and a curve in such a set has winding number zero about $A_0$. Hence the continuous real function $\operatorname{Re}\gamma(t) - \operatorname{Re} A_0$ takes both signs, and by the intermediate value theorem there is a parameter at which it vanishes, that is a point at which $\gamma$ meets the fibre $L_{A_0}$. At that point $\zeta - A_0$ is not a unit, the kernel $(\zeta - A_0)^{-1}$ is undefined, and the contour integral does not exist.

The obstruction is of the same kind as in the split complex case but simpler: there the non-invertible set was the union of two lines through $A_0$, here it is the single fibre through $A_0$. The complement of one line in the plane has two components, each convex, and a closed curve lying in one component is null-homotopic in the punctured plane and has winding number zero about $A_0$.

### What Fails

The following are consequences of the obstruction. None of them has an analogue in $\mathbb{C}$, and each fails for the same reason: the singular set of the kernel is a whole fibre rather than a point, and a differentiable function is rigid, built from one ordinary differentiable function of one variable and its derivative.

- **No Cauchy integral formula.** As above.
- **No residue and no winding number.** A circle of small radius about $A_0$ meets the fibre in two points, where the integrand of a would-be residue is undefined; and the surviving area detector returns a real area rather than an integer.
- **No Cauchy estimates and no Liouville theorem.** The function $f(A) = \sin(a)\,\varepsilon$ is dual differentiable on all of $\mathbb{D}'$, because its real part vanishes and its infinitesimal part is independent of $a'$. It satisfies $\|f\|_E = |\sin a| \leq 1$, yet it is not constant. So a bounded dual differentiable function on the whole plane need not be constant.
- **No mean value property and no maximum principle.** Both would be consequences of the integral formula. The real part of a differentiable function depends only on $a$, so its average over a circle of radius $r$ about a point of real part $a_0$ is the weighted average $\frac{1}{2\pi}\int_0^{2\pi}u(a_0 + r\cos t)\,dt$ of $u$ over the interval $[a_0-r, a_0+r]$, which need not equal $u(a_0)$: for $u(a) = a^2$ it is $a_0^2 + r^2/2$.
- **No Laurent expansion at a point.** The negative powers $(\zeta - A_0)^{-n}$ are undefined on the whole fibre through $A_0$, so a Laurent series in $(\zeta - A_0)$ does not exist. Power series in non-negative powers do exist wherever the two real functions are real-analytic.
- **No identity theorem.** Distinctness of the zero set from the whole plane does not force a function to vanish. Let $c$ be a smooth function that vanishes for $|a| < 1$ and is positive outside that interval; then $f(A) = c(a)\,\varepsilon$ is dual differentiable, because its real part vanishes and its infinitesimal part is independent of $a'$, and it vanishes on the open strip $|a| < 1$ while being non-zero outside it. So a differentiable function may vanish on a non-empty open set without vanishing identically, and no accumulation argument for zero sets is available.

### The Fundamental Solution Is Not Point-Supported

The obstruction has an equivalent analytic form. Let

$$
D = \frac{\partial}{\partial \bar A} = \frac{\partial}{\partial a'} - \varepsilon\frac{\partial}{\partial a}
$$

be the dual Cauchy–Riemann operator, so that $Df = 0$ is dual differentiability. On $f = u + v\varepsilon$ it acts by $Df = u_{a'} + (v_{a'} - u_a)\varepsilon$. Squaring, the term $\varepsilon^2\partial_a^2$ vanishes but the cross terms do not cancel, and

$$
D^2 = \partial_{a'}^2 - 2\,\varepsilon\,\partial_a\partial_{a'} .
$$

So $D$ itself does not factor the Laplacian of the plane. With the conjugate operator $\bar D = \partial_{a'} + \varepsilon\partial_a$ the two mixed terms cancel instead, and

$$
D\bar D = \bar D D = \partial_{a'}^2 ,
$$

the one-dimensional operator in the nilpotent coordinate rather than $\Delta = \partial_a^2 + \partial_{a'}^2$; this is the ellipticity failure in operator form. The symbol of $D$, the algebra element $i\xi_{a'} - i\xi_a\varepsilon$, is invertible exactly when $\xi_{a'} \neq 0$, so the characteristic set of $D$ is the line $\xi_{a'} = 0$, the conormal of the fibre direction, and the operator is not elliptic.

**Theorem.** A fundamental solution of $D$ on the plane with Lebesgue measure is

$$
E(a + \varepsilon a') = H(a')\,\delta(a) + a'_+\,\delta'(a)\,\varepsilon,
$$

where $H$ is the Heaviside function, $a'_+ = \max(a',0)$, $\delta$ the one-dimensional Dirac distribution and $\delta'$ its derivative. The support of $E$ is the ray

$$
\{(a,a') : a = 0,\ a' \geq 0\},
$$

contained in the fibre over the origin.

**Proof.** With $E = E_0 + E_1\varepsilon$, the equation $DE = \delta_0$ reads

$$
\partial_{a'} E_0 = \delta_0, \qquad \partial_{a'} E_1 = \partial_a E_0.
$$

The first equation is solved by $E_0 = H(a')\delta(a)$, since $\partial_{a'} H(a')\delta(a) = \delta(a')\delta(a) = \delta_0$. Then $\partial_a E_0 = H(a')\delta'(a)$, and since $\partial_{a'} a'_+ = H(a')$, the second equation is solved by $E_1 = a'_+\delta'(a)$. Both $E_0$ and $E_1$ are supported on the closed half-line $a = 0$, $a' \geq 0$.

So the fundamental solution is carried by the fibre, not by a point. In $\mathbb{C}$ the fundamental solution of the Cauchy–Riemann operator is $1/(\pi A)$, a locally integrable function singular at the origin, and a small circle is an adequate contour. Here the singular support is one-dimensional and lies in a fibre, and every contour winding about $A_0$ meets that fibre, on which the kernel $(\zeta - A_0)^{-1}$ is undefined; so the boundary integral that would represent an interior value is never defined.

## The Substitute in the Derived Variable

The reconstruction half of the Cauchy theory is lost, but the structure of a differentiable function replaces it by a **derived** statement: the function is determined by its restriction to the real axis through one derivative of the real part, and integration in the nilpotent direction evaluates rather than reconstructs.

### The Structure Theorem

**Theorem (structure).** A dual differentiable function $f$ on a domain $U$ is determined by the pair of ordinary differentiable functions

$$
u(a) = \operatorname{Re} f(a), \qquad c(a) = \operatorname{Inf} f(a),
$$

through the formula

$$
f(a + \varepsilon a') = u(a) + \bigl(a'\,u'(a) + c(a)\bigr)\varepsilon.
$$

**Proof.** This is the corollary of the Cauchy–Riemann theorem.

The pair $(u, c)$ is exactly the restriction of $f$ to the real axis, $f(a) = u(a) + c(a)\varepsilon$, together with the derivative of its real part. So the real axis — a *screen* that meets every fibre in exactly one point — determines the whole function, and no contour integral is required to propagate the data off the screen.

### The Exact Taylor Expansion

Because the infinitesimal direction is nilpotent, the Taylor expansion of a differentiable function along it truncates exactly.

**Theorem (exact expansion).** Let $f$ be dual differentiable on an open set $U$ and let $A \in U$ and $h \in \mathrm{M}$ with $A + h \in U$. Then

$$
f(A + h) = f(A) + f'(A)\,h.
$$

**Proof.** Write $A = a + \varepsilon a'$ and $h = s\varepsilon$. By the structure theorem, $f(A + h) = u(a) + ((a'+s)u'(a) + c(a))\varepsilon = f(A) + s\,u'(a)\varepsilon$. Since $f'(A) = u'(a) + (a'u''(a) + c'(a))\varepsilon$ and $\varepsilon\cdot\varepsilon = 0$, one has $f'(A)h = u'(a)s\varepsilon$, and the two expressions agree. There is no remainder term because $h^2 = 0$.

So the first-order expansion is exact in the nilpotent direction: the "second derivative along the derived direction" vanishes identically, and the Taylor series along a fibre is a polynomial of degree one.

### Integration and Differentiation with Respect to the Nilpotent Parameter

The exact expansion is the bridge between integration along the fibre and differentiation. Write $\partial_\varepsilon$ for the **nilpotent-parameter derivation** of *Dual-Numbers Algebra*,

$$
\partial_\varepsilon(a + \varepsilon a') = \varepsilon a'.
$$

It is the derivation determined by $\partial_\varepsilon(1) = 0$ and $\partial_\varepsilon(\varepsilon) = \varepsilon$; its kernel is the real submodule $\mathbb{R}$, and its image is the maximal ideal $\mathrm{M}$. It is idempotent, $\partial_\varepsilon^2 = \partial_\varepsilon$, and it is **not** the formal derivative $d/\varepsilon d$ of the truncated polynomial ring: the formal derivative would send $\varepsilon$ to $1$, and the Leibniz rule would then force $0 = d(\varepsilon^2)/\varepsilon d = 2\varepsilon$, which fails. The only derivations of $\mathbb{D}'$ are the multiples $c\,\partial_\varepsilon$ of this one; $\partial_\varepsilon$ itself is idempotent rather than nilpotent, and $c\,\partial_\varepsilon$ is idempotent exactly for $c = 0$ and $c = 1$.

The relation between this derivation and the fibre integral is the following.

**Proposition (fundamental theorem along a fibre).** Let $f$ be dual differentiable on a neighbourhood of the fibre segment $\sigma$ from $a_0 + b_0\varepsilon$ to $a_0 + b_1\varepsilon$. Then

$$
\int_\sigma f(A)\,dA = (b_1 - b_0)\,\pi(f(a_0))\,\varepsilon = (b_1 - b_0)\,\operatorname{Re} f(a_0)\,\varepsilon,
$$

and for a differentiable $f$ the infinitesimal part is recovered from the derivative of the real part:

$$
\operatorname{Inf} f(a + \varepsilon a') = a'\,\frac{d}{da}\operatorname{Re} f(a) + \operatorname{Inf} f(a).
$$

**Proof.** The first identity is the fibre-evaluation theorem. For the second, differentiate the structure formula.

So the fibre integral returns the real part and the derivation recovers the infinitesimal part; together they recover the function. This is the exact sense in which "integration along the fibre" and "differentiation with respect to the nilpotent parameter" are the two halves of a substitute for the Cauchy integral formula: the integral evaluates, and the derivation differentiates, and between them they recover everything, without any boundary contour.

**Remark.** The pairing is one-way. The fibre integral is a functional of the real part alone and cannot see the infinitesimal part, while the derivation $\partial_\varepsilon$ sees only the infinitesimal part and annihilates the real part. There is no single operator that reproduces a value from the boundary, because the boundary of a small disk meets the singular fibre.

### Higher Nilpotent Truncations

The simplicity of the derived substitute is a consequence of truncation at order two. For the **truncated polynomial algebra** $\mathbb{D}'_{R,n} = R[\varepsilon]/(\varepsilon^{n+1})$ of *Dual-Numbers Algebra*, with $n \geq 1$, an element of the ideal $(\varepsilon)$ is nilpotent of index at most $n+1$, so the expansion in the nilpotent direction truncates at order $n$ rather than at order one.

**Theorem (truncated expansion).** Let $f$ be dual differentiable on a neighbourhood of the real point $a$ in $\mathbb{D}'_{R,n}$, and suppose that the iterated algebraic derivatives $f, f', \dots, f^{(n)}$ are dual differentiable on the fibre segment $\{a + th : 0 \leq t \leq 1\}$ for every $h \in (\varepsilon)$. Then

$$
f(a + h) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}\,h^k \qquad (h \in (\varepsilon)),
$$

with no remainder term.

**Proof.** Fix $h \in (\varepsilon)$ and put $g(t) = f(a + th)$. By the chain rule and the $A$-linearity of the differential of a dual differentiable function, $g^{(k)}(t) = f^{(k)}(a+th)h^k$ for $k \leq n+1$, so Taylor's formula with integral remainder for the one-variable function $g$ reads

$$
f(a + h) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}\,h^k + \frac{h^{n+1}}{n!}\int_0^1 (1-t)^n f^{(n+1)}(a+th)\,dt,
$$

and the remainder vanishes because $h^{n+1} = 0$.

For $n = 1$ the same conclusion holds under the weaker hypothesis that $f$ be merely dual differentiable, as proved in the previous section; the iterated differentiability is needed only so that the ordinary Taylor formula along the fibre is available.

The theorem says that a differentiable function of the truncated algebra is determined by its **$n$-jet** at the real point $a$. For $n = 1$ this is the structure theorem: the jet $(f(a), f'(a))$ determines $f$, and the fibre integral of the previous section is the way of reading the first piece of that data off the fibre, whose dimension is then one. For $n \geq 2$ the fibre of the augmentation has dimension $n$, and the corresponding data are the jet. The functional that extracts the top coefficient,

$$
\ell_n(f) = \text{the coefficient of } \varepsilon^n \text{ in } f,
$$

plays the role of the residue in the derived variable: it is a linear functional of the jet rather than a contour integral, the reason being that $\oint_\gamma f\,dA = 0$ for every differentiable $f$ and every closed path $\gamma$. The dual-number case is the first truncation, where the expansion reduces to $f(A+h) = f(A) + f'(A)h$ for $h \in \mathrm{M}$ and $\ell_1 = \operatorname{Inf}$.

## Comparison with Complex Integration

The differences are consequences of the single relation $\varepsilon^2 = 0$ against $i^2 = -1$, which makes $\mathbb{C}$ a field and $\mathbb{D}'$ a local ring with a nilpotent maximal ideal.

| Property | Complex | Dual |
|---|---|---|
| Coefficient ring | field, no zero divisors, no nilpotents | local ring, nilpotent $\varepsilon$ |
| Cauchy–Riemann operator | $\partial_a + i\partial_{a'}$, elliptic | $\partial_{a'} - \varepsilon\partial_a$, characteristic set $\xi_{a'} = 0$ |
| Second-order square | Laplacian $\Delta$ | $D\bar D = \bar D D = \partial_{a'}^2$ |
| Section of the singular set | a point | a fibre, a whole line |
| Fundamental solution | $1/(\pi A)$, singular at a point | supported on a ray of the fibre |
| Cauchy–Goursat, closed contour | holds, with content | holds, soft, on every domain |
| Path independence | on simply connected domains | on every domain, and vacuous |
| Primitive | exists when closed integrals vanish | exists for every differentiable function |
| Cauchy integral formula | holds | obstructed |
| Residue, winding number | integer-valued, homotopy invariant | no residue; a real area detector |
| Laurent expansion | at an isolated singularity | does not exist |
| Liouville, mean value, maximum principle, identity theorem | hold | fail |

The complex case is rigid because the kernel $(\zeta - A_0)^{-1}$ is defined on the punctured plane and a contour can surround the missing point. The dual case is degenerate in the opposite way: the kernel is undefined on a whole fibre, so no contour can surround anything, and the class of differentiable functions is so small that every one of them has an explicit primitive. The vanishing half of the Cauchy theory thus survives as an empty theorem, and the reconstruction half, which is its content, does not survive at all.

## The Relation to Hypercomplex Integration

The general theory of *Hypercomplex Integration* is stated for an **elliptic** hypercomplex system: a finite-dimensional unital associative real algebra $A$ with a Cauchy–Riemann operator

$$
D = \partial_0 + \sum_{k \geq 1} B_k \partial_k, \qquad B_j B_k + B_k B_j = -2\delta_{jk}, \qquad B_k^2 = -1,
$$

whose square $D\bar D = \bar D D$ is a Laplacian and whose fundamental solution is a Cauchy kernel singular at a point. The hypothesis $B_k^2 = -1$ is exactly the hypothesis that the system be elliptic, and it is exactly what fails for $\mathbb{D}'$.

**Proposition.** There is no element $A \in \mathbb{D}'$ with $A^2 = -1$. Hence the dual system cannot be presented as an elliptic hypercomplex system in the sense of the general theory, and no choice of generators $B_k$ satisfies the general hypotheses.

**Proof.** Write $A = a + \varepsilon a'$. Then $A^2 = a^2 + 2aa'\,\varepsilon$. The equation $A^2 = -1$ requires $a^2 = -1$, impossible for real $a$.

Equivalently, putting the dual operator in the general form $D = \partial_0 + B\,\partial_1$ with $\partial_0 = \partial_{a'}$ and $B = -\varepsilon$, one has $B^2 = \varepsilon^2 = 0$ and, for $\bar D = \partial_0 - B\partial_1 = \partial_{a'} + \varepsilon\partial_a$,

$$
D\bar D = \bar D D = \partial_{a'}^2,
$$

which is the degenerate second-order operator in the $a'$-direction and not the Laplacian $\Delta = \partial_a^2 + \partial_{a'}^2$ of the plane. So the dual system is not elliptic, and no scalar multiple of $D$ has an elliptic principal symbol.

The consequences are those of the preceding sections. The general **Cauchy–Goursat** theorem applies to the dual system, because $\mathbb{D}'$ is commutative and every dual differentiable function has an explicit primitive; but it carries no information there, since the vanishing half of the theory is soft. The general **residue theory** and **Cauchy integral formula**, by contrast, have no dual analogue, because their proofs use the point singularity of the fundamental solution and here the singular support is the fibre. The mechanism of the failure is the constant in the characteristic equation: for $\mathbb{C}$ the characteristic set of $D$ is the single point $\{\xi = 0\}$, for $\mathbb{D}$ it is the null cone, and for $\mathbb{D}'$ it is the line $\xi_{a'} = 0$. The dual theory is thus the most degenerate case of the general theory: the characteristic set is a line, the group of units modulo scaling is one-dimensional and unipotent, and the integral reduces to a pair of ordinary real integrals of which the real part is always exact.

## Summary

The **dual integral** $\int_\gamma f\,dA = \int_a^b f(\gamma(t))\gamma'(t)\,dt$ exists for every piecewise $C^1$ path and continuous $f$, is linear, additive, reversed by reversal of the path, and satisfies the sharp estimate $\|\int_\gamma f\,dA\|_E \leq (2/\sqrt3)\,m\,L(\gamma)$, the constant $2/\sqrt3$ being the operator-norm bound for multiplication, between the complex constant $1$ and the split complex constant $\sqrt2$.

The key structural fact is the **fibre decomposition**

$$
\int_\gamma f\,dA = \int_\gamma u\,da + \varepsilon\Bigl(\int_\gamma u\,da' + \int_\gamma v\,da\Bigr),
$$

which reduces a dual integral to a pair of real line integrals, with the real part seen only through $u\,da$ and the infinitesimal part through both $u$ and $v$. Integration along a **fibre** — a coset of the maximal ideal — evaluates the real part, $\int_\sigma f\,dA = (b_1-b_0)\operatorname{Re}f(a_0)\varepsilon$, and is blind to the infinitesimal part; the nilpotent direction is totally isotropic, so iterated fibre integration vanishes.

The form $f\,dA$ is **closed** exactly when $f$ is **dual differentiable**, that is when $u_{a'} = 0$ and $v_{a'} = u_a$; equivalently $\partial_{\bar A} f = 0$. Consequently the **Cauchy–Goursat theorem** $\oint_\gamma f\,dA = 0$ holds on every domain, and every differentiable function has an explicit primitive; the theorem is nevertheless **soft**, because it excludes nothing and its truth is the existence of the primitive rather than a property of the domain. A **rectangle criterion** characterises the continuous densities that are derivatives of dual differentiable functions — one step short of differentiability itself, since that class is not closed under differentiation — and the conjugate $\bar A$ supplies the detector $\oint_\gamma \bar A\,dA = 2\operatorname{Area}(\gamma)\varepsilon$.

The **obstruction** to the reconstruction half of the theory is the nilpotent ideal. The kernel $(\zeta - A_0)^{-1}$ is defined exactly off the fibre through $A_0$, and no contour of non-zero winding avoids that fibre, so there is no **Cauchy integral formula**, no residue, no winding number, no Cauchy estimates, no Liouville theorem, no mean value property, no maximum principle, no Laurent expansion and no identity theorem. Analytically the same obstruction is the **fundamental solution** of the dual Cauchy–Riemann operator $D = \partial_{a'} - \varepsilon\partial_a$, which is supported on a ray of the fibre and not at a point; the pair $D, \bar D = \partial_{a'} \pm \varepsilon\partial_a$ satisfies $D\bar D = \bar D D = \partial_{a'}^2$ and not $\Delta$, so $D$ is not elliptic.

What replaces the reconstruction half is the **derived** statement. A dual differentiable function is determined by its restriction to the real axis through $f(a + \varepsilon a') = u(a) + (a'u'(a)+c(a))\varepsilon$, its expansion in the nilpotent direction is exact, and the fibre integral evaluates while the derivation $\partial_\varepsilon$ differentiates; for higher truncations $R[\varepsilon]/(\varepsilon^{n+1})$ the same scheme returns an exact $n$-jet and the residue functional becomes coefficient extraction in the derived variable. Finally, the dual system fails the ellipticity hypothesis $B_k^2 = -1$ of *Hypercomplex Integration* — $\mathbb{D}'$ contains no square root of $-1$ — and it is the case in which the general theory degenerates to a soft vanishing theorem with no reconstruction theorem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$ | Dual number algebra, $\varepsilon^2 = 0$ |
| $\mathbb{D}'_{R,n} = R[\varepsilon]/(\varepsilon^{n+1})$ | Truncated polynomial algebra |
| $A = a + \varepsilon a'$ | General dual number, $a = \operatorname{Re} A$, $a' = \operatorname{Inf} A$ |
| $\bar A = a - \varepsilon a'$ | Dual conjugate |
| $N(A) = A\bar A = a^2$ | Degenerate norm |
| $\|A\|_E = \sqrt{a^2+a'^2}$ | Euclidean modulus |
| $\mathrm{M} = \varepsilon\mathbb{R}$ | Maximal ideal, nilpotent, $\mathrm{M}^2 = 0$ |
| $\pi : \mathbb{D}' \to \mathbb{R}$ | Augmentation, kernel $\mathrm{M}$ |
| $\gamma : [a,b] \to \mathbb{D}'$ | Piecewise $C^1$ path |
| $\gamma^*$, $-\gamma$, $\gamma_1+\gamma_2$ | Trace, opposite path, concatenation |
| $L(\gamma) = \int_a^b \|\gamma'(t)\|_E\,dt$ | Euclidean length |
| $\int_\gamma f\,dA$ | Dual integral |
| $f = u + v\varepsilon$ | Real and infinitesimal components |
| $\partial_{\bar A} f = 0$ | Dual Cauchy–Riemann equation, $u_{a'} = 0$, $v_{a'} = u_a$ |
| $D = \partial_{\bar A} = \partial_{a'} - \varepsilon\partial_a$ | Cauchy–Riemann operator, $D^2 = \partial_{a'}^2 - 2\varepsilon\partial_a\partial_{a'}$ |
| $\bar D = \partial_{a'} + \varepsilon\partial_a$ | Conjugate operator, $D\bar D = \bar D D = \partial_{a'}^2$ |
| $\partial_\varepsilon(a+\varepsilon a') = \varepsilon a'$ | Nilpotent-parameter derivation, idempotent |
| $F = A + (a'u + C)\varepsilon$ | Primitive of a differentiable $f$, with $A' = u$, $C' = c$ |
| $E = H(a')\delta(a) + a'_+\delta'(a)\varepsilon$ | Fundamental solution of $D$, supported on a fibre ray |
| $\operatorname{Area}(\gamma)$ | Signed area enclosed by a closed contour; $\oint_\gamma \bar A\,dA = 2\operatorname{Area}(\gamma)\varepsilon$ |
| $\ell_n(f)$ | Coefficient of $\varepsilon^n$ in $f$, the residue functional of $\mathbb{D}'_{R,n}$ |

## Further Reading

- Eduard Studa', *Geometrie der Dynamen* (Teubner, 1903), for the geometry of the dual numbers and their infinitesimal transformations.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the origin of the dual numbers in the biquaternion program.
- Lars V. Ahlfors, *Complex Analysis* (McGraw–Hill, 3rd ed. 1979), for the classical Cauchy theory, residues and winding numbers with which the dual theory is compared.
- Walter Rudin, *Real and Complex Analysis* (McGraw–Hill, 3rd ed. 1987), for the measure-theoretic foundation of the line and surface integrals used here.
- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Cauchy–Goursat theorem, the Cauchy kernel and the residue theory of elliptic hypercomplex systems.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* (Springer, 2nd ed. 1990), for the distinction between elliptic and non-elliptic operators and for fundamental solutions supported on characteristics.
- Andreas Griewank and Andrea Walther, *Evaluating Derivatives* (SIAM, 2008), for the dual numbers as the coefficient algebra of forward-mode differentiation.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of the two-dimensional real algebras.
