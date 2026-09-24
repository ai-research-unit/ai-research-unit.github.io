
# __Split-Complex Integration__

## Introduction

This article develops integration for functions of one split complex variable. It follows *Split Complex Analysis*, which fixed the split complex plane, its Euclidean topology, split complex differentiability and the split Cauchy–Riemann equations, and it follows *Split-Complex Algebra* for the ring $\mathbb{D} = \mathbb{R}[j]$, $j^2 = +1$, the idempotents $e_\pm = \tfrac12(1 \pm j)$, the conjugation $\bar z$, and the norm form $N(z) = z\bar z = x^2 - y^2$. The aim is to construct the integral from first principles and then to determine exactly how much of the Cauchy theory survives when the coefficient ring is not a field.

The base ring throughout is $\mathbb{D}$. It is a commutative ring with identity, of characteristic zero, in which $2$ is invertible; it is not an integral domain, because $1 + j$ and $1 - j$ are non-zero and their product is zero. This single algebraic fact governs the whole theory, and it divides the classical Cauchy theory into a half that survives and a half that does not. The **vanishing** statement — the integral of a split complex differentiable function over a closed contour is zero — survives, and it in fact holds on every domain, not merely on the simply connected ones. The **representation** statement — the Cauchy integral formula that recovers an interior value from a boundary integral, and with it the residue theorem, the Cauchy estimates, the mean value property and the Laurent expansion — does not survive, and the obstruction is exactly the zero-divisor cone. The kernel $1/(\zeta - z)$ of the formula is defined only where $\zeta - z$ is a unit, and the set where it is not is not the point $z$ but the two lines through $z$; no contour that surrounds $z$ avoids them.

No physics is invoked. Split complex differentiability and the idempotent decomposition are used as they were set up in *Split Complex Analysis*, and the operator notation $\partial_z, \partial_{\bar z}$ is the one fixed there. The general shape of the integral theorems, and the place of the present theory among its companions for $\mathbb{C}$, $\mathbb{D}'$, $\mathbb{H}$ and $\mathbb{B}$, is the subject of *Hypercomplex Integration*.

Notation: $z = x + jy$ with $x, y \in \mathbb{R}$, $\bar z = x - jy$, and $\|z\|_E = \sqrt{x^2 + y^2}$. The idempotent coordinates are

$$
z_+ = x + y, \qquad z_- = x - y, \qquad z = z_+ e_+ + z_- e_-,
$$

and $N(z) = z_+ z_-$.

## The Split-Complex Integral

### Paths and Contours

**Definition.** A **path** is a continuous map $\gamma : [a,b] \to \mathbb{D}$. It is **piecewise continuously differentiable**, written piecewise $C^1$, if there is a finite subdivision $a = t_0 < t_1 < \cdots < t_n = b$ such that $\gamma$ is continuously differentiable on each closed subinterval $[t_{k-1}, t_k]$. A path is **closed** if $\gamma(a) = \gamma(b)$ and **simple** if it is injective on $[a,b)$; a simple closed path is a **contour**.

The **trace** of $\gamma$ is the compact set $\gamma^* = \gamma([a,b])$. The **opposite** path $-\gamma$ is $t \mapsto \gamma(a + b - t)$, and if $\gamma_1 : [a,b] \to \mathbb{D}$ and $\gamma_2 : [b,c] \to \mathbb{D}$ agree at $b$, their **concatenation** $\gamma_1 + \gamma_2$ follows first one and then the other. The **length** of a piecewise $C^1$ path is

$$
L(\gamma) = \int_a^b \|\gamma'(t)\|_E \, dt,
$$

finite because $\gamma'$ is piecewise continuous on a compact interval.

**Example.** For $z_0 \in \mathbb{D}$ and $r > 0$, the curve

$$
\gamma(t) = z_0 + r e^{jt} = z_0 + r(\cosh t + j \sinh t), \qquad t \in \mathbb{R},
$$

is a hyperbola and is not closed, because the split complex exponential is injective and $\cosh$ and $\sinh$ are not periodic. The closed curves along which integrals are taken are the ordinary Euclidean circles $\gamma(t) = z_0 + r(\cos t + j \sin t)$, of length $2\pi r$.

### Construction from the Riemann Sum

**Definition.** Let $\gamma : [a,b] \to \mathbb{D}$ be piecewise $C^1$ and let $f$ be continuous on a neighbourhood of $\gamma^*$. Given a subdivision $a = t_0 < t_1 < \cdots < t_n = b$ and sample points $\tau_k \in [t_{k-1}, t_k]$, set $z_k = \gamma(t_k)$ and form the **Riemann sum**

$$
S = \sum_{k=1}^{n} f(\gamma(\tau_k))\,(z_k - z_{k-1}).
$$

With $\|\Delta\| = \max_k (t_k - t_{k-1})$, the **split complex integral** of $f$ along $\gamma$ is the limit

$$
\int_\gamma f(z)\,dz = \lim_{\|\Delta\| \to 0} S.
$$

**Theorem.** For piecewise $C^1$ $\gamma$ and continuous $f$ the Riemann sums converge, and

$$
\int_\gamma f(z)\,dz = \int_a^b f(\gamma(t))\,\gamma'(t)\,dt.
$$

**Proof.** The product in $\mathbb{D}$ is bilinear, and $f$ is continuous, so the argument of the complex case applies verbatim: on each smooth piece

$$
z_k - z_{k-1} = \int_{t_{k-1}}^{t_k} \gamma'(t)\,dt = \gamma'(\tau_k)(t_k - t_{k-1}) + \rho_k, \qquad \|\rho_k\|_E \leq \omega(\|\Delta\|)(t_k - t_{k-1}),
$$

with $\omega(\|\Delta\|) \to 0$ by uniform continuity of $\gamma'$ on the finitely many pieces. Hence $S$ differs from the Riemann sum of $t \mapsto f(\gamma(t))\gamma'(t)$ by a term bounded in norm by $\max_{\gamma^*}\|f\|_E \,\omega(\|\Delta\|)(b-a) \to 0$. $\square$

The integral exists because $\mathbb{D}$ is a complete normed space under $\| \cdot \|_E$, exactly as $\mathbb{C}$ is under the modulus; completeness is what makes the limit of Riemann sums legitimate, and it is not affected by the presence of zero divisors.

### Basic Properties

**Linearity.** For $\alpha, \beta \in \mathbb{D}$,

$$
\int_\gamma (\alpha f + \beta g)(z)\,dz = \alpha \int_\gamma f(z)\,dz + \beta \int_\gamma g(z)\,dz.
$$

**Reversal.** $\displaystyle\int_{-\gamma} f(z)\,dz = -\int_\gamma f(z)\,dz$.

**Additivity.** $\displaystyle\int_{\gamma_1 + \gamma_2} f(z)\,dz = \int_{\gamma_1} f(z)\,dz + \int_{\gamma_2} f(z)\,dz$.

**Reparametrisation.** If $\varphi : [c,d] \to [a,b]$ is a piecewise $C^1$ bijection with $\varphi(c) = a$, $\varphi(d) = b$, then $\int_{\gamma \circ \varphi} f\,dz = \int_\gamma f\,dz$; if $\varphi$ reverses the endpoints, the sign changes.

**Estimation.** If $\|f(z)\|_E \leq m$ on $\gamma^*$, then

$$
\left\|\int_\gamma f(z)\,dz\right\|_E \leq \sqrt{2}\,m\,L(\gamma).
$$

**Proof.** The Euclidean norm on $\mathbb{D}$ is a genuine norm but is not submultiplicative. The best constant is $\sqrt2$: writing $z = x + jy$, $w = c + dj$, one has

$$
\|zw\|_E^2 = (xc + yd)^2 + (xd + yc)^2 = (x^2 + y^2)(c^2 + d^2) + 4xycd,
$$

and $4xycd \leq 4\lvert xy\rvert \lvert cd\rvert \leq (x^2 + y^2)(c^2 + d^2)$ by the arithmetic–geometric mean inequality applied to each pair, so $\|zw\|_E^2 \leq 2\|z\|_E^2\|w\|_E^2$. Equality holds if and only if $\lvert x\rvert = \lvert y\rvert$, $\lvert c\rvert = \lvert d\rvert$ and $xycd > 0$, that is, if and only if $z$ and $w$ are non-zero elements of the same one of the two null lines $\mathbb{R}e_+$ and $\mathbb{R}e_-$; the bound is therefore attained and $\sqrt2$ cannot be lowered. Hence $\|f(\gamma(t))\gamma'(t)\|_E \leq \sqrt2\,m\,\|\gamma'(t)\|_E$, and integrating gives the estimate. $\square$

**Remark.** The factor $\sqrt2$ is a feature of the multiplicativity failure of the Euclidean norm and has no analogue in $\mathbb{C}$, where the modulus is multiplicative. It is the first sign that the Euclidean metric and the ring multiplication are not aligned; the alignment that does hold is the multiplicativity of $N$, used below.

### The Idempotent Decomposition of the Integral

The reason the split complex integral is tractable is that $z \mapsto (z_+, z_-)$ is an algebra isomorphism $\mathbb{D} \to \mathbb{R} \oplus \mathbb{R}$.

**Theorem.** Let $f : U \to \mathbb{D}$ be written in the idempotent basis as $f = f_+ e_+ + f_- e_-$, with $f_\pm$ real-valued, and let $\gamma : [a,b] \to U$ be piecewise $C^1$. Then

$$
\int_\gamma f(z)\,dz = e_+ \int_{\gamma_+} f_+(z_+)\,dz_+ + e_- \int_{\gamma_-} f_-(z_-)\,dz_-,
$$

where $\gamma_\pm(t) = x(\gamma(t)) \pm y(\gamma(t))$ are the projected paths and each integral on the right is an ordinary real line integral.

**Proof.** Since $dz = e_+\,dz_+ + e_-\,dz_-$ and $e_+ e_- = e_- e_+ = 0$, $e_\pm^2 = e_\pm$, the product $f(z)\,dz$ splits as $f_+(z_+)\,e_+\,dz_+ + f_-(z_-)\,e_-\,dz_-$. Integrating the two summands separately gives the stated identity. $\square$

So a split complex contour integral is exactly a pair of real line integrals, one for each idempotent, and the two are independent of each other. This is the source of both the strength and the weakness of the theory.

## The Cauchy–Riemann Operator in Idempotent Coordinates

### The Operator and Its Conjugate

**Definition.** The **split Wirtinger derivatives** are

$$
\frac{\partial}{\partial z} = \frac{1}{2}\left(\frac{\partial}{\partial x} + j\,\frac{\partial}{\partial y}\right), \qquad \frac{\partial}{\partial \bar z} = \frac{1}{2}\left(\frac{\partial}{\partial x} - j\,\frac{\partial}{\partial y}\right),
$$

and $D = 2\,\partial_{\bar z} = \partial_x - j\,\partial_y$ is the **split Cauchy–Riemann operator**.

**Proposition.** With $\partial_\pm = \partial/\partial z_\pm$,

$$
\frac{\partial}{\partial z} = e_+\, \partial_+ + e_-\, \partial_-, \qquad \frac{\partial}{\partial \bar z} = e_-\, \partial_+ + e_+\, \partial_-.
$$

**Proof.** Because $z_+ = x + y$ and $z_- = x - y$, one has $\partial_x = \partial_+ + \partial_-$ and $\partial_y = \partial_+ - \partial_-$. Substituting,

$$
\frac{\partial}{\partial z} = \tfrac12\big((\partial_+ + \partial_-) + j(\partial_+ - \partial_-)\big) = \tfrac12\big((1+j)\partial_+ + (1-j)\partial_-\big) = e_+\partial_+ + e_-\partial_-,
$$

and the conjugate is computed the same way with $j$ replaced by $-j$, which interchanges $e_+$ and $e_-$. $\square$

**Proposition (the d'Alembertian).** For the conjugate operator $\bar D = 2\,\partial_z = \partial_x + j\,\partial_y$,

$$
\bar D D = D \bar D = \Box := \partial_x^2 - \partial_y^2 = 4\,\partial_+ \partial_-.
$$

**Proof.** Expanding, $\bar D D = (\partial_x + j\partial_y)(\partial_x - j\partial_y) = \partial_x^2 - j^2 \partial_y^2 = \partial_x^2 - \partial_y^2$, the mixed terms cancelling; the same expansion gives $D\bar D$. In the idempotent coordinates $\partial_+ \partial_- = \tfrac14(\partial_x^2 - \partial_y^2)$. $\square$

So the split Cauchy–Riemann operator factors the wave operator, not the Laplacian. It is therefore not elliptic: the principal symbol of $D$ is $\xi_1 - j\,\xi_2$, whose norm is $\xi_1^2 - \xi_2^2$, so it is a unit off the two lines $\xi_1 = \pm\xi_2$ and a zero divisor on them; those lines are exactly the set on which the symbol of $\Box = 4\partial_+\partial_-$ vanishes. This is the analytic face of the algebra's zero divisors, and the next sections show that it is the same set.

### The Cauchy–Riemann Equations

**Theorem.** For a real differentiable $f : U \to \mathbb{D}$ with $f = f_+ e_+ + f_- e_-$, the following are equivalent.

1. $f$ is split complex differentiable on $U$.
2. $\partial_{\bar z} f = 0$, that is $D f = 0$.
3. $f_+$ is independent of $z_-$ and $f_-$ is independent of $z_+$.

**Proof.** The equivalence of (1) and (2) is the split Cauchy–Riemann equations of *Split Complex Analysis*. For (2) and (3), apply the factorised operator: for $f = f_+e_+ + f_-e_-$,

$$
\partial_{\bar z} f = (e_-\partial_+ + e_+\partial_-)(f_+e_+ + f_-e_-) = (\partial_+ f_-)\,e_- + (\partial_- f_+)\,e_+,
$$

because $e_- e_+ = e_+ e_- = 0$ and $e_\pm^2 = e_\pm$. The two idempotents are independent, so this vanishes if and only if $\partial_+ f_- = 0$ and $\partial_- f_+ = 0$, that is, if and only if $f_-$ is locally a function of $z_-$ alone and $f_+$ of $z_+$ alone. $\square$

**Corollary (the derivative in idempotent coordinates).** If $f$ is split complex differentiable, then

$$
f'(z) = \frac{\partial f}{\partial z} = f_+'(z_+)\,e_+ + f_-'(z_-)\,e_-,
$$

the primes denoting ordinary differentiation of the one-variable functions $f_\pm$.

The theorem says that split complex differentiability is not a restriction on the pair $(f_+, f_-)$ beyond the separation of variables: the two components do not interact at all. This is the precise sense in which the theory is soft, and it is visible at once in the idempotent basis.

**Corollary (real and imaginary parts).** Writing $f(z) = u(x,y) + j\,v(x,y)$ with $u, v$ real, $f$ is split complex differentiable if and only if

$$
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \qquad \frac{\partial u}{\partial y} = \frac{\partial v}{\partial x},
$$

and then $u$ and $v$ each satisfy the wave equation $\Box u = \Box v = 0$.

## The Cauchy–Goursat Theorem

### Closedness of $f\,dz$

**Theorem.** Let $f$ be $C^1$ on a domain $U$. Then the differential form $f\,dz$ is closed if and only if $f$ is split complex differentiable on $U$.

**Proof.** In the idempotent coordinates, $f\,dz = f_+ e_+ dz_+ + f_- e_- dz_-$, and since $e_+$ and $e_-$ are constant,

$$
d(f\,dz) = (\partial_- f_+)\,e_+\, dz_- \wedge dz_+ + (\partial_+ f_-)\,e_-\, dz_+ \wedge dz_- = \big[(\partial_+ f_-)\,e_- - (\partial_- f_+)\,e_+\big]\, dz_+ \wedge dz_-.
$$

The two idempotents are independent, so this vanishes if and only if $\partial_+ f_- = 0$ and $\partial_- f_+ = 0$. Now compute directly in the coordinates $x, y$: $dz = dx + j\,dy$ and

$$
d(f\,dz) = df \wedge dz = (\partial_x f\,dx + \partial_y f\,dy)\wedge(dx + j\,dy) = \big(\partial_x f \, j - \partial_y f\big)\,dx \wedge dy.
$$

This vanishes if and only if $\partial_y f = \partial_x f\, j$, which is the split Cauchy–Riemann equation $Df = 0$. The two computations agree because $\partial_+ f_- = 0$ and $\partial_- f_+ = 0$ is precisely that equation in the idempotent basis. $\square$

In the complex plane the same computation gives the same conclusion, closedness being equivalent to holomorphy, so on the differentiable side the two theories have the same shape. What differs is what the condition costs. There it is an elliptic system, whose solutions are rigid; here it says only that $f_+$ does not depend on $z_-$ and $f_-$ does not depend on $z_+$, so that the differentiable functions are exactly the pairs of one-variable functions, one for each idempotent, with no interaction between the two components and no exclusion beyond the separation itself.

### Primitives and Path Independence

**Theorem (primitive).** Let $f$ be split complex differentiable on a domain $U$. Then $f\,dz$ has a primitive on $U$: there is a split complex differentiable $F$ on $U$ with $F' = f$. The integral of $f$ depends only on the endpoints:

$$
\int_\gamma f(z)\,dz = F(\gamma(b)) - F(\gamma(a)).
$$

**Proof.** On $U$ the components satisfy $f_+ = f_+(z_+)$ and $f_- = f_-(z_-)$ with $f_\pm$ continuous functions of one real variable on intervals $I_\pm$, the projections of $U$. A continuous function of one real variable has an antiderivative, so choose $F_+$ on $I_+$ with $F_+' = f_+$ and $F_-$ on $I_-$ with $F_-' = f_-$, and set $F = F_+ \circ z_+ \cdot e_+ + F_- \circ z_- \cdot e_-$. Then $F$ is split complex differentiable with $F' = f$ by the corollary of the previous section. Along a piecewise $C^1$ path, $\frac{d}{dt}F(\gamma(t)) = F'(\gamma(t))\gamma'(t) = f(\gamma(t))\gamma'(t)$, and the fundamental theorem of calculus in the two idempotent components gives the endpoint formula. $\square$

Two facts distinguish this from the complex case. First, the primitive exists on *every* domain, with no simple connectivity hypothesis, because each component is a function of a single real variable and a real antiderivative always exists; in $\mathbb{C}$ the primitive exists only when the closed integrals vanish. Second, the primitive is determined only up to an additive split complex constant, since each one-variable antiderivative is determined up to a constant; the ambiguity does not affect differences.

### The Cauchy–Goursat Theorem

**Theorem (Cauchy–Goursat).** If $f$ is split complex differentiable on a domain $U$ and $\gamma$ is a closed piecewise $C^1$ path in $U$, then

$$
\oint_\gamma f(z)\,dz = 0.
$$

**Proof.** By the primitive theorem the integral equals $F(\gamma(b)) - F(\gamma(a))$, and for a closed path $\gamma(b) = \gamma(a)$. $\square$

**Remark (softness).** The theorem holds in $\mathbb{D}$ for a reason that gives it no force: every pair of one-variable functions is split complex differentiable, so the class of integrands for which closed integrals vanish is the class of *all* differentiable functions, and the vanishing is not a restriction. In $\mathbb{C}$ the same statement is the origin of the whole theory — it forces primitives, the Cauchy integral formula, the maximum principle and the identity theorem. In $\mathbb{D}$ it forces none of these, because nothing is excluded. The mean value property likewise fails: a split complex differentiable function is a pair of arbitrary one-variable functions, and its average over a circle need not equal its centre value.

**Theorem (rectangle criterion).** For a continuous $f : U \to \mathbb{D}$, the following are equivalent.

1. $\oint_{\partial R} f(z)\,dz = 0$ for every axis-parallel rectangle $R \subseteq U$.
2. $f$ has the separated form $f = f_+(z_+)e_+ + f_-(z_-)e_-$ with $f_\pm$ continuous functions of one variable.

**Proof.** If (2) holds, $\oint_{\partial R} f\,dz = e_+\oint_{\partial R} f_+(z_+)\,dz_+ + e_-\oint_{\partial R} f_-(z_-)\,dz_-$, and each term vanishes because the projected boundary of the rectangle is a closed real path over which a one-variable continuous function is integrated, and every continuous function of one real variable has an antiderivative. Conversely, if (1) holds, the integral $F$ of $f$ from a fixed base point along axis-parallel paths is well defined: two such paths inside a rectangle of $U$ differ by the boundaries of the subrectangles between them, and a chain of overlapping rectangles inside $U$ carries the independence from one rectangle to the next. The standard difference-quotient computation in each component then shows that $F$ is split complex differentiable with $F' = f$. By the Cauchy–Riemann theorem $F$ has the separated form $F = F_+(z_+)e_+ + F_-(z_-)e_-$, so $f = F' = F_+'(z_+)e_+ + F_-'(z_-)e_-$ has the separated form. $\square$

**Remark (no regularity upgrade).** In $\mathbb{C}$ the same rectangle hypothesis upgrades a merely continuous $f$ to a holomorphic one, because the primitive of a continuous function is holomorphic and the derivative of a holomorphic function is holomorphic. In $\mathbb{D}$ no such upgrade is available: the components $f_\pm = F_\pm'$ are derivatives of one-variable functions and are continuous by hypothesis, but a continuous function of one real variable need not be differentiable. The hypothesis of the theorem therefore stops at the separated form, one step short of differentiability, and this gap is a further face of the failure of the representation half of the theory. In particular there is no Morera theorem in $\mathbb{D}$ of the classical strength; the rectangle condition characterises the class of continuous separated densities, not the class of split complex differentiable functions.

## The Obstruction to the Cauchy Theorem

The Cauchy–Goursat theorem is the vanishing half of the Cauchy theory. The other half is the representation of an interior value by a boundary integral, and it is here that the zero divisors obstruct.

### The Cauchy Kernel and the Null Cone

**Proposition.** Let $z_0 \in \mathbb{D}$. The element $\zeta - z_0$ is a unit if and only if $\zeta$ lies off the **null cone** through $z_0$, that is, off the union of the two lines $\zeta_+ = z_{0+}$ and $\zeta_- = z_{0-}$. For $\zeta - z_0$ a unit,

$$
(\zeta - z_0)^{-1} = \frac{\overline{\zeta - z_0}}{N(\zeta - z_0)} = \frac{e_+}{\zeta_+ - z_{0+}} + \frac{e_-}{\zeta_- - z_{0-}}.
$$

**Proof.** The inverse formula $w^{-1} = \bar w / N(w)$ is valid whenever $N(w) \neq 0$, and $N(\zeta - z_0) = (\zeta_+ - z_{0+})(\zeta_- - z_{0-})$, which vanishes exactly on the two stated lines. $\square$

**Theorem (obstruction).** There is no Cauchy integral formula in $\mathbb{D}$: there is no constant $c \in \mathbb{D}$ such that

$$
f(z_0) = c \oint_\gamma \frac{f(\zeta)}{\zeta - z_0}\,d\zeta
$$

holds for every split complex differentiable $f$, every $z_0$ in the domain of $f$ and every closed piecewise $C^1$ path $\gamma$ in that domain. The constant of the classical formula, $1/(2\pi i)$, is not an element of $\mathbb{D}$ at all; but no constant whatever serves, because the kernel $(\zeta - z_0)^{-1}$ is undefined on the null cone through $z_0$, and every closed curve whose winding number about $z_0$ is non-zero meets that cone.

**Proof.** The complement of the two lines $\zeta_+ = z_{0+}$ and $\zeta_- = z_{0-}$ has four connected components, the open sectors determined by the signs of $\zeta_+ - z_{0+}$ and $\zeta_- - z_{0-}$, and each is convex. A closed curve lying in one component lies in a convex set omitting $z_0$, hence is null-homotopic in $\mathbb{D} \setminus \{z_0\}$ and has winding number zero about $z_0$. So a curve of non-zero winding about $z_0$ must leave every component, that is, must meet the cone, where the integrand is not defined. $\square$

This is the precise sense in which the Cauchy theorem of a ring with zero divisors is obstructed: the kernel of the would-be formula is not a function on the punctured neighbourhood of $z_0$, because the punctured neighbourhood is not the set on which $\zeta - z_0$ is invertible. In $\mathbb{C}$ the two sets coincide and the formula holds; in $\mathbb{D}$ the invertible set is the complement of a pair of lines.

### The Fundamental Solution Is Not Point-Supported

The obstruction has an equivalent analytic form. In $\mathbb{C}$ the locally integrable function $1/(\pi z)$ is the fundamental solution of the Cauchy–Riemann operator, and its singularity is carried by the single point $0$; that is what makes a small circle an adequate contour.

**Theorem.** Let $D = \partial_x - j\,\partial_y$ be the split Cauchy–Riemann operator. A fundamental solution of $D$ is

$$
E(z) = H(z_-)\,\delta(z_+)\,e_+ + H(z_+)\,\delta(z_-)\,e_-,
$$

where $H$ is the Heaviside function, $\delta$ is the one-dimensional Dirac distribution, and a normalisation is fixed by $D E = \delta_0$ in the Lebesgue measure of the plane. The support of $E$ is the union of the two null rays

$$
\{z : z_+ = 0,\ z_- \geq 0\} \cup \{z : z_- = 0,\ z_+ \geq 0\},
$$

so $E$ is not a locally integrable function: its support, and hence its singular support, is the union of those two rays rather than a single point.

**Proof.** In the idempotent coordinates $D = 2(e_-\partial_+ + e_+\partial_-)$, so for $E = E_+e_+ + E_-e_-$,

$$
D E = 2\,(\partial_+ E_-)\,e_- + 2\,(\partial_- E_+)\,e_+,
$$

the cross terms vanishing as before. Taking $E_+ = H(z_-)\delta(z_+)$ and $E_- = H(z_+)\delta(z_-)$ gives $\partial_- E_+ = \delta(z_-)\delta(z_+)$ and $\partial_+ E_- = \delta(z_+)\delta(z_-)$; with the Jacobian $\tfrac12$ of $(x,y) \mapsto (z_+,z_-)$, one has $2\,\delta(z_+)\delta(z_-) = \delta_0$ in the plane measure, so $DE = \delta_0$. The support statement is immediate from the factors $H$ and $\delta$. $\square$

The contrast with $\mathbb{C}$ is the contrast of an elliptic with a hyperbolic operator, and it is the same contrast as that of a field with a ring having zero divisors. In $\mathbb{C}$ the principal symbol never vanishes off the origin, the fundamental solution is a function singular at a point, and the boundary integral of the Cauchy formula is meaningful on any small circle. In $\mathbb{D}$ the principal symbol degenerates on the real characteristics, the fundamental solution is a distribution carried by those characteristics, and a boundary integral can represent an interior value only if the contour is allowed to meet the singular support — which the definition of the integral forbids.

### What Fails

The following are consequences of the obstruction, and they are recorded here to delimit the theory precisely. None of these failures occurs in $\mathbb{C}$, where each of the listed results holds.

- **No Cauchy integral formula.** No constant $c \in \mathbb{D}$ makes $f(z_0) = c\oint_\gamma f(\zeta)(\zeta - z_0)^{-1}\,d\zeta$ hold for all $f$ and all $z_0$, by the obstruction theorem above.
- **No Cauchy estimates and no Liouville theorem.** A bounded split complex differentiable function on $\mathbb{D}$ need not be constant: for instance $f(z) = \tanh(z_+) e_+ + \tanh(z_-) e_-$ is split complex differentiable, bounded, and non-constant.
- **No mean value property and no maximum principle.** Both would be consequences of the integral formula.
- **No Laurent expansion at a point.** The negative powers $(z - z_0)^{-n}$ for $n \geq 1$ are undefined on the null cone through $z_0$, so a Laurent series in $(z - z_0)$ does not exist; a power series in non-negative powers does exist wherever the components are real-analytic, by the corresponding one-variable expansions.
- **No analytic-continuation rigidity.** The identity theorem fails: the function $f(z) = z_+e_+$ is split complex differentiable and vanishes on the whole line $z_+ = 0$, every point of which is an accumulation point of its zero set, yet $f$ is not identically zero.

The common cause of all five is the same: the two idempotent components are independent, so a condition at a point or on a curve constrains only one component, and the other is free.

## Integration Along the Null Directions

### The Characteristic Lines

**Definition.** The **null directions** of $\mathbb{D}$ are the two directions spanned by $e_+$ and by $e_-$, equivalently the level lines of $z_+$ and of $z_-$. They are the characteristics of the operator $\Box$, and their union through the origin is the zero-divisor cone.

The behaviour of the integral along a null line is instructive. Let $f$ be split complex differentiable and let $\gamma$ run along a line on which $z_+$ is constant. Then $dz_+ = 0$, so $dz = e_-\,dz_-$ and

$$
\int_\gamma f(z)\,dz = e_- \int_{\gamma_-} f_-(z_-)\,dz_-.
$$

Along such a line the integral sees only the minus idempotent component of $f$; symmetrically, along a line on which $z_-$ is constant it sees only the plus component. A single null line is therefore blind to one of the two components of the integrand, and the two families of null lines probe the two components in opposite ways.

**Proposition (characteristic tangency).** If $\gamma$ is tangent to a null direction at $t_0$, then $\gamma'(t_0)$ is a zero divisor.

**Proof.** A null direction is the kernel of $dz_+$ or of $dz_-$; putting $z'(t_0) = p + jq$, tangency to the line $z_+ = \mathrm{const}$ means $p + q = 0$, that is $z'(t_0) = p(1 - j) = 2p\,e_-$, a multiple of the zero divisor $e_-$. The other family gives multiples of $e_+$. $\square$

So the derivative of a curve is a zero divisor exactly at its tangencies with the characteristics. The difference quotient $(f(z_0 + h) - f(z_0))/h$ is not defined for a null increment $h$, since $h$ is not invertible, so the limit defining the split derivative is taken over the invertible increments; the null directions are exactly the increments excluded from it, and they are the directions in which the argument reducing differentiability to the Cauchy–Riemann equations cannot be run.

### Path Independence Within a Sector

By the primitive theorem $f\,dz$ is exact on *every* domain, so path independence is a global property of the integrand and needs no hypothesis at all. The null cone therefore does not enter by creating a period; it enters by removing paths from the domain. A domain that omits the cone through $z_0$ falls into the four sectors bounded by the two null lines through $z_0$, and within one sector any two points can still be joined, so the integral between them is again independent of the route taken inside that sector.

**Proposition.** Let $f$ be split complex differentiable on a domain $U$, let $P, Q \in U$, and let $\gamma_1, \gamma_2$ be piecewise $C^1$ paths in $U$ from $P$ to $Q$. Then

$$
\int_{\gamma_1} f(z)\,dz = \int_{\gamma_2} f(z)\,dz,
$$

with no hypothesis on $U$ beyond $f$ being defined and differentiable on it. In particular, if $U$ omits the null cone through $z_0$ and $P, Q$ lie in the same component of $U$, the two points may be joined inside that component and the integral between them is independent of the path.

**Proof.** By the primitive theorem $f\,dz = dF$ for a globally defined primitive $F$ on $U$, and the integral of an exact form along a path depends only on the endpoints, so both integrals equal $F(Q) - F(P)$. $\square$

Thus path independence does hold within each sector bounded by the null lines; it is the *extension* to paths that would cross a line which fails, and that is the subject of the next subsection.

### The Failure of Path Independence Across the Null Directions

**Proposition (cut by a null line).** Let $a \in \mathbb{R}$ and let $f$ on $\{z : z_+ \neq a\}$ be given by $f(z) = e_+ (z_+ - a)^{-1}$. Then $f$ is split complex differentiable, $f$ has no singularity at a point, and its singular set is the whole null line $\{z : z_+ = a\}$. There is no path in the domain joining a point with $z_+ > a$ to a point with $z_+ < a$, and the primitive $F = e_+ \log|z_+ - a|$, which is defined on each half-plane, has no continuous extension across the line.

**Proof.** $f$ is of the form $f_+(z_+)e_+$ with $f_+(t) = (t-a)^{-1}$, so it is split complex differentiable by the Cauchy–Riemann theorem, and $f\,dz = e_+\,dz_+/(z_+ - a)$ has the primitive $e_+\log|z_+ - a|$ on each of the two half-planes $z_+ > a$ and $z_+ < a$. The line $z_+ = a$ is exactly the set on which $f$ is undefined, and it separates the two half-planes. $\square$

The failure of path independence is therefore not the appearance of a non-zero period, as it is in $\mathbb{C}$, where $\oint z^{-1}dz = 2\pi i$. The split complex form $f\,dz$ is closed and has zero integral over every closed path in each component; indeed no closed path in the domain can leave a single half-plane. What fails is the *extension* of path independence across the null direction: the characteristic is an impenetrable cut, and the fundamental group that controls the complex case is replaced by a purely local, sector-wise statement. In $\mathbb{C}$ the singular set of $(\zeta - z_0)^{-1}$ is a point, whose complement is connected, so a contour can encircle it and produce the residue $2\pi i$; in $\mathbb{D}$ the singular set is a line, whose complement has two components, and no contour can encircle it at all.

**Remark.** The absence of periods for split complex differentiable forms is a general feature of the idempotent decomposition: each component is integrated over the projection $\gamma_\pm$, which is a closed path in the real line, and a continuous one-variable function integrates to zero over a closed real path. A non-vanishing closed integral therefore requires a density that is not split complex differentiable, as in $\oint_\gamma \bar z\,dz = 2j\,\mathrm{Area}(\gamma)$, where the detecting device is the failure of $\bar z\,dz$ to be closed.

## Residues: What Survives

### Why the Point Residue Fails

In $\mathbb{C}$ the residue of $f$ at an isolated singularity $z_0$ is defined as the integral over a small positively oriented circle, and its independence of the radius is proved by Cauchy–Goursat applied to the annulus between two circles. In $\mathbb{D}$ the same construction fails at its first step: a small circle about $z_0$ meets the null cone through $z_0$ at four points, where the integrand is not defined, and no contour with non-zero winding about $z_0$ avoids the cone. Consequently there is no point residue defined as a contour integral.

### The Algebraic Residue of a Null-Line Singularity

What does survive is attached to a characteristic rather than to a point, and it is read off algebraically.

**Definition.** Let $a \in \mathbb{R}$ and let $f$ be split complex differentiable on a domain whose complement contains the null line $L : z_+ = a$, with $f = f_+(z_+)e_+ + f_-(z_-)e_-$ on that domain. If $f_+$ has a simple pole at $a$, the **residue** of $f$ at $L$ is

$$
\operatorname{Res}_L f = \Big(\lim_{z_+ \to a}(z_+ - a) f_+(z_+)\Big) e_+.
$$

The residue at the null line $z_- = b$ is defined symmetrically, and for a function with singularities on both lines the full residue datum is the pair.

**Example.** For $f(z) = (z - z_0)^{-1}$ on the complement of the null cone through $z_0$, the decomposition $(\zeta - z_0)^{-1} = e_+(\zeta_+ - z_{0+})^{-1} + e_-(\zeta_- - z_{0-})^{-1}$ shows that $f$ has a simple pole along each of the two null lines through $z_0$, and the pair of residues is $(e_+, e_-)$, whose sum is $1$. The number that a contour integral would return in $\mathbb{C}$ survives as the sum of the two line residues, but neither line residue is detected by any contour.

### The Line Residue as a Boundary Jump

The algebraic residue has a distributional realisation, which is the form in which it can be used analytically. It is the Sokhotski–Plemelj jump of the component across the characteristic.

**Proposition (standard).** Complexify the idempotent line and let $(t - a \pm i0)^{-1}$ denote the boundary values of $(t - a)^{-1}$ from the two half-planes. Then

$$
\frac{1}{t - a - i0} - \frac{1}{t - a + i0} = 2\pi i\,\delta(t - a),
$$

in the sense of distributions on the real line.

Applied to the component $f_+$ of the previous paragraph, the proposition gives

$$
f_+(t - i0) - f_+(t + i0) = 2\pi i\, r_+\, \delta(t - a), \qquad r_+ = \operatorname{Res}_L f \text{ in the } e_+ \text{ component},
$$

so the residue reappears as a measure carried by the null line: it is the density of the jump of the boundary value, exactly as a point residue in $\mathbb{C}$ is the coefficient that makes the primitive acquire a period. The reader will recognise the complexification of the idempotent component as the step already required for the inversion of the split complex Fourier transform.

**Remark.** The surviving residue theorem has no contour form. Its content is that for a split complex differentiable function with a simple pole along a null line, the jump of the component across that line is the residue times a one-dimensional delta supported on the line. The classical statement, in which a residue at a point equals a contour integral, is not available, because there is no contour to take.

## Comparison with Complex Integration

The differences are consequences of the single sign $j^2 = +1$ against $i^2 = -1$, which makes $\mathbb{C}$ a field and $\mathbb{D}$ a ring with zero divisors.

| Property | Complex | Split complex |
|---|---|---|
| Coefficient ring | field, no zero divisors | ring, zero divisors $1 \pm j$ |
| Cauchy–Riemann operator | $\partial_x + i\partial_y$, elliptic | $\partial_x - j\partial_y$, hyperbolic |
| Second-order operator | Laplacian $\Delta$ | d'Alembertian $\Box$ |
| Characteristic set | $\{0\}$ | the null cone $N = 0$ |
| Fundamental solution | a Cauchy kernel $z^{-1}$ up to a constant, singular at a point | supported on the null rays |
| Cauchy–Goursat, closed contour | holds | holds, but is soft |
| Path independence | on simply connected domains | on every domain, by the primitive |
| Cauchy integral formula | holds | obstructed |
| Point residue | holds | no point residue |
| Residue datum | a point residue | a line residue, a boundary jump |
| Winding number | integer-valued, homotopy invariant | trivial on curves that avoid the cone: a closed curve of non-zero winding must meet the cone |
| Laurent expansion | at an isolated singularity | does not exist |
| Liouville, mean value, maximum principle | hold | fail |

The complex case is rigid because the kernel $(\zeta - z_0)^{-1}$ is defined on the whole punctured plane and a contour can surround a point. The split case is soft because the same kernel is defined only off two lines, so a contour cannot surround anything, and because the two idempotent components of a differentiable function are independent.

## The Relation to Hypercomplex Integration

The general theory of *Hypercomplex Integration* is stated for an **elliptic** hypercomplex system: a finite-dimensional unital associative real algebra $A$ with a Cauchy–Riemann operator

$$
D = \partial_0 + \sum_{k \geq 1} B_k \partial_k, \qquad B_j B_k + B_k B_j = -2\delta_{jk}, \qquad B_k^2 = -1,
$$

whose square $D\bar D = \bar D D$ is a Laplacian and whose fundamental solution is a Cauchy kernel singular at a point. The hypothesis $B_k^2 = -1$ is exactly the hypothesis that $A$ contains square roots of $-1$ and that the system is elliptic, and it is exactly what fails for $\mathbb{D}$.

**Proposition.** There is no element $w \in \mathbb{D}$ with $w^2 = -1$. Hence the split complex system cannot be presented as an elliptic hypercomplex system in the sense of the general theory, and no choice of generators $B_k$ satisfies the general hypotheses.

**Proof.** Write $w = x + jy$. Then $w^2 = (x^2 + y^2) + 2xy\,j$. The equation $w^2 = -1$ requires $xy = 0$ and $x^2 + y^2 = -1$, impossible for real $x, y$ since $x^2 + y^2 \geq 0$. $\square$

The consequences are those of the preceding sections. The general Cauchy–Goursat theorem applies to the split system, because $\mathbb{D}$ is commutative, but it carries no information there, since the vanishing half of the theory is soft. The general residue theory and Cauchy integral formula, by contrast, have no split complex analogue, because their proofs use the point singularity of the fundamental solution. The mechanism of the failure is the constant in the characteristic equation: for $\mathbb{C}$ the characteristic set of $D$ is the single point $0$, for $\mathbb{D}$ it is the null cone, and the cone is the zero-divisor set. The split complex theory is thus the boundary case of the general theory at which ellipticity is lost and with it the representation half of the Cauchy theory, while the vanishing half survives in a form too weak to carry the rest.

## Summary

The **split complex integral** $\int_\gamma f\,dz = \int_a^b f(\gamma(t))\gamma'(t)\,dt$ exists for every piecewise $C^1$ path and continuous $f$, is linear, additive, reversed by reversal of the path, and satisfies the estimate $\|\int_\gamma f\,dz\|_E \leq \sqrt2\,m\,L(\gamma)$ with the sharp constant $\sqrt2$. Its **idempotent decomposition** $\int_\gamma f\,dz = e_+\int_{\gamma_+} f_+ \,dz_+ + e_-\int_{\gamma_-} f_-\,dz_-$ reduces it to a pair of real line integrals; this identity is the structural fact of the theory.

In the idempotent coordinates the operator factorises as $\partial_{\bar z} = e_-\partial_+ + e_+\partial_-$, and **split complex differentiability** is equivalent to $f_+$ depending on $z_+$ alone and $f_-$ on $z_-$ alone. Hence $f\,dz$ is closed exactly when $f$ is differentiable, every differentiable $f$ has a primitive on every domain, the **Cauchy–Goursat theorem** $\oint_\gamma f\,dz = 0$ holds for every closed path, and for continuous densities the rectangle criterion is equivalent to the separated form. The theorem is nevertheless soft, since differentiability excludes nothing, and the rectangle criterion stops one step short of differentiability.

The **obstruction to the Cauchy theorem** is the zero divisor. The element $\zeta - z_0$ is a unit exactly off the null cone through $z_0$, so the Cauchy kernel is undefined there and no contour of non-zero winding about $z_0$ avoids the cone; the **Cauchy integral formula** therefore does not exist, and with it the Cauchy estimates, the mean value property, the maximum principle, Liouville's theorem and the Laurent expansion all fail. The same obstruction appears analytically as the **fundamental solution** of the split Cauchy–Riemann operator, which is a distribution supported on the null rays rather than a function singular at the origin.

**Integration along the null directions** reproduces only one idempotent component at a time. **Path independence** is global — $f\,dz$ is exact on every domain — so the null lines create no periods to replace the complex winding number; what they do is cut the domain into sectors, so a path that would cross a characteristic is not available inside the domain at all. The residue datum that **survives** is attached to a null line rather than a point: it is the coefficient of the simple pole of an idempotent component, realised distributionally as the Sokhotski–Plemelj jump across the characteristic. Finally, the split complex system fails the ellipticity hypothesis $B_k^2 = -1$ of *Hypercomplex Integration* — $\mathbb{D}$ contains no square root of $-1$ — and it is the case in which the general theory degenerates to its vanishing half.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D} = \mathbb{R}[j]$, $j^2 = +1$ | Split complex numbers |
| $z = x + jy$ | General split complex number, $x = \operatorname{Re} z$, $y = \operatorname{Im} z$ |
| $\bar z = x - jy$ | Split complex conjugate |
| $N(z) = z\bar z = x^2 - y^2$ | Norm form, signature $(1,1)$ |
| $\{N = 0\}$ | Null cone, the zero-divisor set |
| $\|z\|_E = \sqrt{x^2 + y^2}$ | Euclidean modulus |
| $e_+ = \tfrac12(1+j), \ e_- = \tfrac12(1-j)$ | Idempotents, $e_\pm^2 = e_\pm$, $e_+e_- = 0$ |
| $z = z_+e_+ + z_-e_-$, $z_+ = x+y$, $z_- = x-y$ | Idempotent decomposition and coordinates |
| $\gamma : [a,b] \to \mathbb{D}$ | Piecewise $C^1$ path |
| $\gamma_\pm(t) = z_\pm(\gamma(t))$ | Projections of a path to the two null coordinates |
| $\gamma^*$, $-\gamma$, $\gamma_1 + \gamma_2$ | Trace, opposite path, concatenation |
| $L(\gamma) = \int_a^b \|\gamma'(t)\|_E\,dt$ | Euclidean length |
| $\int_\gamma f\,dz$ | Split complex integral |
| $\partial_z = \tfrac12(\partial_x + j\partial_y)$ | Split Wirtinger derivative |
| $\partial_{\bar z} = \tfrac12(\partial_x - j\partial_y)$ | Split Wirtinger derivative, conjugate of $\partial_z$ |
| $\partial_\pm = \partial/\partial z_\pm$ | Null-coordinate derivatives |
| $D = \partial_x - j\partial_y$ | Split Cauchy–Riemann operator, $D = 2\partial_{\bar z}$ |
| $\bar D = \partial_x + j\partial_y$ | Conjugate operator |
| $\Box = \partial_x^2 - \partial_y^2 = 4\partial_+\partial_-$ | d'Alembertian |
| $\|\Delta\|$ | Mesh of a partition of $[a,b]$, for the Riemann sums |
| $\omega(\|\Delta\|)$ | Modulus of continuity of $\gamma'$ on a partition of mesh $\|\Delta\|$ |
| $H$ | Heaviside function, $H(t) = 1$ for $t > 0$ and $0$ for $t < 0$ |
| $E = H(z_-)\delta(z_+)e_+ + H(z_+)\delta(z_-)e_-$ | Fundamental solution of $D$, supported on the two null rays |
| $\operatorname{Res}_L f$ | Residue at a null line $L$, an idempotent coefficient |
| $\delta$, $\delta_0$ | One-dimensional Dirac distribution, and the two-dimensional one at the origin |



## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the geometry of the split complex plane and its null directions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the identification of $\mathbb{D}$ with a Clifford algebra and the role of the zero divisors.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, 2012), for the hyperbolic analysis in which the null cone is the characteristic set.
- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the Cauchy–Goursat theorem, the Cauchy kernel and the residue theory that the elliptic case supports.
- Lars V. Ahlfors, *Complex Analysis* (McGraw-Hill, 3rd ed. 1979), for the classical Cauchy theory and the residue calculus with which the split complex theory is compared.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* (Springer, 2nd ed. 1990), for fundamental solutions supported on characteristics and the distinction between elliptic and hyperbolic operators.
