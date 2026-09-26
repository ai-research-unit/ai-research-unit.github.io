
# __Quaternion Integration__

## Introduction

This article develops the integration theory of quaternion-valued functions of a quaternion variable. It follows *Quaternion Analysis*, where the quaternion space, its metric, the limits and continuity of quaternion-valued functions, and the two notions of differentiability were set up: the naive difference quotient, which forces the function to be affine, and the Cauchy–Riemann operator, whose kernel is the class of regular functions. Here the integral is constructed and the integral theorems of that class are proved.

The treatment is mathematical throughout. The independent variable is a quaternion, the values are quaternions, and no physical object is introduced. The quaternion algebra, its basis, its conjugation and its norm form are taken from *Quaternion Algebra*; the topology of $\mathbb{H}$, the modulus, the Cauchy–Riemann operator and the class of regular functions are taken from *Quaternion Analysis*. Where a statement is the quaternionic instance of a general theorem of Clifford analysis, the general result is cited and the quaternionic constants are computed; the general shape of the integral theorems is that of *Hypercomplex Integration* and *Regularity and the Cauchy–Riemann Operator*.

Throughout, $\mathbb{H}$ is the quaternion algebra with basis $e_0 = 1, e_1, e_2, e_3$ and $e_k^2 = -e_0$. A general quaternion is written $q = \sum_{\mu=0}^{3} q_\mu e_\mu = q_0 + \mathbf{q}$, with quaternion conjugate $\bar{q} = q_0 - \mathbf{q}$ and norm form $N(q) = q\bar{q} = |q|^2 = \sum_\mu q_\mu^2$. The coordinates of a point are also written $x_0, x_1, x_2, x_3$, so that $q = x_0 + x_1 e_1 + x_2 e_2 + x_3 e_3$, and $\partial_\mu = \partial/\partial x_\mu$. The **Cauchy–Riemann operator** is

$$
D = \partial_0 + e_1 \partial_1 + e_2 \partial_2 + e_3 \partial_3,
$$

and its **conjugate** is $\bar{D} = \partial_0 - e_1\partial_1 - e_2\partial_2 - e_3\partial_3$. A function is **left regular** if $Df = 0$ and **right regular** if $fD = 0$, where $fD = \partial_0 f + (\partial_1 f)e_1 + (\partial_2 f)e_2 + (\partial_3 f)e_3$.

## The Integral of a Quaternion-Valued Function

### The Domain Integral

**Definition.** Let $\Omega \subseteq \mathbb{H}$ be a domain and let $f : \Omega \to \mathbb{H}$ be written in components as

$$
f(q) = \sum_{\mu=0}^{3} f_\mu(x_0, x_1, x_2, x_3)\, e_\mu, \qquad f_\mu \in \mathbb{R}.
$$

The **domain integral** of $f$ over $\Omega$ is

$$
\int_\Omega f \, dV = \sum_{\mu=0}^{3} \left(\int_\Omega f_\mu \, dV\right) e_\mu,
$$

where $dV$ is the Lebesgue measure on the four real coordinates and each scalar integral is an ordinary Lebesgue integral. The integral exists when each of the four real-valued functions $f_\mu$ is integrable over $\Omega$, and it is then a quaternion.

The definition is the componentwise one, so the integral inherits the properties of the Lebesgue integral coordinate by coordinate.

**Theorem (linearity).** For $a, b \in \mathbb{H}$ constant and $f, g$ integrable,

$$
\int_\Omega (a f + g b) \, dV = a \int_\Omega f \, dV + \left(\int_\Omega g \, dV\right) b .
$$

**Proof.** Multiplication by a constant quaternion is a real-linear map of $\mathbb{H}$, and it is applied after the componentwise integration. The left multiple $af$ has components given by the real matrix of left multiplication by $a$ acting on the components of $f$, and integration is linear in these; the same holds on the right for $b$. $\square$

**Theorem (additivity).** If $\Omega = \Omega_1 \cup \Omega_2$ with $\Omega_1 \cap \Omega_2$ of measure zero, then

$$
\int_\Omega f \, dV = \int_{\Omega_1} f \, dV + \int_{\Omega_2} f \, dV .
$$

**Proof.** Apply the additivity of the Lebesgue integral to each component. $\square$

**Theorem (fundamental estimate).** If $|f(q)| \leq M$ on $\Omega$ and $\operatorname{vol}(\Omega)$ is the volume of $\Omega$, then

$$
\left| \int_\Omega f \, dV \right| \leq M \, \operatorname{vol}(\Omega).
$$

**Proof.** The triangle inequality for the vector integral gives $\left|\int_\Omega f\,dV\right| \leq \int_\Omega |f|\,dV$, and $|f| \leq M$ bounds the last integral by $M\operatorname{vol}(\Omega)$. $\square$

**Theorem (integrability).** A continuous quaternion-valued function on a compact domain is integrable.

**Proof.** Each component is a continuous real-valued function on a compact subset of $\mathbb{R}^4$, hence bounded and Lebesgue integrable. $\square$

### Path Integrals

The integral along a curve in $\mathbb{H}$ was introduced in *Quaternion Analysis*, and it is recorded here in the two orders that the non-commutativity makes distinct.

**Definition.** Let $\gamma : [a, b] \to \mathbb{H}$ be a piecewise continuously differentiable path and let $f$ be continuous on a neighbourhood of its image. The **left path integral** and the **right path integral** of $f$ along $\gamma$ are

$$
\int_\gamma f \, dq = \int_a^b f(\gamma(t)) \gamma'(t) \, dt, \qquad \int_\gamma dq \, f = \int_a^b \gamma'(t) f(\gamma(t)) \, dt .
$$

**Theorem.** Both path integrals are additive under concatenation of paths, change sign under reversal of the path, and satisfy the estimate

$$
\left| \int_\gamma f \, dq \right| \leq \sup_\gamma |f| \cdot L(\gamma),
$$

where $L(\gamma) = \int_a^b |\gamma'(t)| \, dt$ is the length of $\gamma$. If $f$ is the constant $c$ then $\int_\gamma c \, dq = c(\gamma(b) - \gamma(a))$ and $\int_\gamma dq \, c = (\gamma(b) - \gamma(a))c$.

**Proof.** The integral is a limit of Riemann sums $\sum_i f(\gamma(t_i))(\gamma(t_{i+1}) - \gamma(t_i))$; submultiplicativity of the modulus bounds each sum by $\sup_\gamma|f|\sum_i|\gamma(t_{i+1})-\gamma(t_i)|$, which tends to $\sup_\gamma|f|\,L(\gamma)$, and the modulus is continuous. The remaining statements are immediate from the definition. $\square$

For a commutative algebra the two orders coincide; here they do not, and the order of the factors is part of the notation. The **contour integral** of *Quaternion Analysis* is the left path integral.

### Surface Integrals and the Conormal Element

**Definition.** Let $\Omega$ be a domain with smooth boundary, with outward unit normal $n(w) = (n_0, n_1, n_2, n_3)$ at $w \in \partial\Omega$. The **conormal element** is the quaternion

$$
\nu(w) = n_0(w) + n_1(w) e_1 + n_2(w) e_2 + n_3(w) e_3 = \sum_{\mu=0}^{3} n_\mu(w) e_\mu .
$$

It is a unit vector of $\mathbb{H}$, since $|\nu|^2 = \sum_\mu n_\mu^2 = 1$, and its conjugate is $\bar{\nu} = n_0 - n_1 e_1 - n_2 e_2 - n_3 e_3$.

**Definition.** For a continuous quaternion-valued function $f$ on $\partial\Omega$, the **surface integrals** are

$$
\int_{\partial\Omega} f \, dS, \qquad \int_{\partial\Omega} \nu f \, dS, \qquad \int_{\partial\Omega} f \nu \, dS,
$$

where $dS$ is the three-dimensional surface measure on $\partial\Omega$ and the integrals of the two products are taken componentwise.

The conormal element is the quaternionic form of the unit normal used by the divergence theorem: because the coefficients of $D$ are constant, the operator is the divergence of a quaternion-valued field, and the normal that appears in the boundary term is $\nu$. This is the element written $\nu_B$ in *Regularity and the Cauchy–Riemann Operator* for a general hypercomplex system, specialised to $B_\mu = e_\mu$.

## The Cauchy–Riemann Operator and its Conjugate

### The Operator and its Square

The Cauchy–Riemann operator $D$ and its conjugate $\bar{D}$ are first-order operators with constant coefficients; they act on a $C^1$ function by taking its partial derivatives and left-multiplying by the basis elements. Their elementary action on the coordinate functions is

$$
Dq = \sum_{\mu=0}^{3} e_\mu e_\mu = e_0 - 3e_0 = -2, \qquad D\bar{q} = \sum_{\mu=0}^{3} e_\mu \bar{e}_\mu = e_0 + 3e_0 = 4,
$$

and conjugating the first identity gives $\bar{D}\bar{q} = -2$ and $\bar{D}q = 4$. The two constant values $2$ and $4$ recur in the analysis of the operator.

**Theorem.** The operators satisfy

$$
D\bar{D} = \bar{D}D = \partial_0^2 + \partial_1^2 + \partial_2^2 + \partial_3^2 = \Delta,
$$

the Laplacian of $\mathbb{R}^4$.

**Proof.** Expand $D\bar{D} = \sum_{\mu,\nu} e_\mu \bar{e}_\nu \partial_\mu\partial_\nu$. The mixed second derivatives commute, so only the symmetric part of $e_\mu\bar{e}_\nu$ contributes. Since $e_\mu\bar{e}_\nu + e_\nu\bar{e}_\mu = 2\delta_{\mu\nu}$ (checking the four cases $\mu = \nu$, and $\mu = 0$ with $\nu = k$, and $\mu = k$, $\nu = l$ distinct imaginary), the sum reduces to $\sum_\mu \partial_\mu^2$. The same computation applies to $\bar{D}D$. $\square$

**Corollary.** If $f$ is left regular or right regular then $\Delta f = 0$: a regular function is harmonic, and each of its four components is a harmonic function of four real variables.

**Proof.** If $Df = 0$ then $\Delta f = \bar{D}Df = 0$; if $fD = 0$ then $\Delta f = (f\bar{D})D = 0$. $\square$

### Ellipticity

**Definition.** The **symbol** of $D$ at a covector $\xi = (\xi_0, \xi_1, \xi_2, \xi_3)$ is left multiplication by

$$
\sigma_D(\xi) = \xi_0 + \xi_1 e_1 + \xi_2 e_2 + \xi_3 e_3 .
$$

The operator is **elliptic** if $\sigma_D(\xi)$ is invertible for every $\xi \neq 0$.

**Theorem.** $D$ is elliptic, with $\sigma_D(\xi)^{-1} = \overline{\sigma_D(\xi)}/|\xi|^2$ for $\xi \neq 0$.

**Proof.** The element $\xi_0 + \sum_k \xi_k e_k$ has norm form $\sum_\mu \xi_\mu^2 = |\xi|^2 \neq 0$; since $\mathbb{H}$ is a division algebra it has the inverse $\overline{\sigma_D(\xi)}/|\xi|^2$. $\square$

Ellipticity is the analytic reason the regular functions are smooth and the Cauchy theory has the shape it has; the elliptic regularity and its consequences are developed in *Regularity and the Cauchy–Riemann Operator*.

### Left and Right Regular Functions

**Definition.** A $C^1$ function $f$ is **left regular** if $Df = 0$ and **right regular** if $fD = 0$, where the right action of the operator is $fD = \partial_0 f + (\partial_1 f)e_1 + (\partial_2 f)e_2 + (\partial_3 f)e_3$.

The two classes are exchanged by quaternion conjugation. Write $\tilde{f} = \bar{f}$; multiplication by a constant is conjugated into multiplication by the conjugate constant, and conjugation reverses the order of factors, so

$$
\overline{Df} = \sum_\mu (\partial_\mu \bar{f}) \bar{e}_\mu = \bar{f}\,\bar{D}, \qquad \overline{fD} = \sum_\mu \bar{e}_\mu (\partial_\mu \bar{f}) = \bar{D}\,\bar{f},
$$

so $f$ is left $D$-regular if and only if $\bar{f}$ is right $\bar{D}$-regular, and $f$ is right $D$-regular if and only if $\bar{f}$ is left $\bar{D}$-regular. For a non-commutative algebra the two classes are genuinely different: a constant function is both, but a regular function need not be regular on the other side.

**Example.** The function $f(q) = e_1\bar{q}$ is left regular but not right regular. On the one hand

$$
Df = \sum_{\mu=0}^{3} e_\mu\, \partial_\mu(e_1\bar{q}) = \sum_{\mu=0}^{3} e_\mu e_1\bar{e}_\mu = e_1 + e_1 - e_1 - e_1 = 0 ,
$$

since $\partial_\mu\bar{q} = \bar{e}_\mu$; on the other hand

$$
fD = \sum_{\mu=0}^{3} \partial_\mu(e_1\bar{q})\, e_\mu = \sum_{\mu=0}^{3} e_1\bar{e}_\mu e_\mu = e_1\sum_{\mu=0}^{3}|\bar{e}_\mu|^2 = 4e_1 \neq 0 .
$$

So $e_1\bar{q}$ lies in the left-regular class and not in the right-regular class, and the two-sided functions are the intersection of the two.

**Theorem (closure under constant multiplication).** If $f$ is left regular and $b\in\mathbb{H}$ is constant, then $fb$ is left regular. If $f$ is right regular and $a\in\mathbb{H}$ is constant, then $af$ is right regular. In particular a real scalar multiple of a regular function is regular, in the same sense.

**Proof.** Since $b$ is constant, the Leibniz rule gives $D(fb) = \sum_\mu e_\mu(\partial_\mu f)b = (Df)b$, so $Df = 0$ implies $D(fb) = 0$. Similarly $(af)D = \sum_\mu a(\partial_\mu f)e_\mu = a(fD)$. $\square$

**Remark.** The two closures are on opposite sides, and neither extends to a general constant on the other side: $D(af) = \sum_\mu e_\mu a\partial_\mu f$ equals $a(Df)$ only when $a$ commutes with each $e_\mu$, that is, only for a real scalar $a$. So the left-regular functions form a right module over $\mathbb{H}$ and a left module over the centre $\mathbb{R}$, and the right-regular functions the mirror image.

A product of two regular functions need not be regular, because the Leibniz rule for $D$ introduces the derivative of the first factor together with a reordering of the quaternion factors.

**Example.** The left-regular function $e_1\bar{q}$ has a square that is not left regular. Writing $e_1\bar{q} = q_1 + q_0e_1 + q_3e_2 - q_2e_3$ and squaring,

$$
(e_1\bar{q})^2 = \bigl(q_1^2 - q_0^2 - q_2^2 - q_3^2\bigr) + 2q_1q_0e_1 + 2q_1q_3e_2 - 2q_1q_2e_3,
$$

and hence

$$
D\bigl((e_1\bar{q})^2\bigr) = -4q_0,
$$

which is not identically zero. So the left-regular functions are not closed under multiplication, and the closure theorem above is genuinely only about constant multiplication.

## Stokes and Divergence Theorems

### The Divergence Form of the Operators

**Theorem.** With $\partial_\mu$ acting on the coordinate $x_\mu$,

$$
Df = \sum_{\mu=0}^{3} \partial_\mu (e_\mu f), \qquad fD = \sum_{\mu=0}^{3} \partial_\mu (f e_\mu).
$$

**Proof.** For the left form, the Leibniz rule gives $\partial_\mu(e_\mu f) = e_\mu \partial_\mu f$ because $e_\mu$ is constant; summing over $\mu$ gives $Df$. The right form is identical with the constant factor placed after $f$. $\square$

Thus $D$ is the divergence of the quaternion-valued field with components $e_\mu f$, and the divergence theorem of $\mathbb{R}^4$ applies to it directly.

### The Divergence Theorem

**Theorem (divergence theorem).** Let $\Omega$ be a bounded domain with smooth boundary and let $f$ be $C^1$ on $\bar{\Omega}$. Then

$$
\int_\Omega Df \, dV = \int_{\partial\Omega} \nu f \, dS, \qquad \int_\Omega fD \, dV = \int_{\partial\Omega} f \nu \, dS .
$$

**Proof.** For each real component, the ordinary divergence theorem in $\mathbb{R}^4$ applied to the field with components $e_\mu f$ gives $\int_\Omega \sum_\mu \partial_\mu(e_\mu f)\,dV = \int_{\partial\Omega}\sum_\mu n_\mu e_\mu f\,dS$. The left side is $\int_\Omega Df\,dV$ by the divergence form, and the right side is $\int_{\partial\Omega}\nu f\,dS$ by the definition of the conormal element. The right-handed identity is the same computation for the field with components $f e_\mu$. $\square$

**Corollary (conjugate divergence theorem).** Under the same hypotheses,

$$
\int_\Omega \bar{D} f \, dV = \int_{\partial\Omega} \bar{\nu} f \, dS, \qquad \int_\Omega f \bar{D} \, dV = \int_{\partial\Omega} f \bar{\nu} \, dS .
$$

**Proof.** Replace $e_\mu$ by $\bar{e}_\mu$ throughout the preceding proof. $\square$

### Integration by Parts

**Theorem (integration by parts).** Let $\phi$ be real-valued and $C^1$ on $\bar{\Omega}$ and let $f$ be quaternion-valued and $C^1$ on $\bar{\Omega}$. Then

$$
\int_\Omega \bigl[\,(D\phi)\,f + \phi\,(Df)\,\bigr] dV = \int_{\partial\Omega} \nu \phi f \, dS .
$$

Equivalently, $\int_\Omega (D\phi) f \, dV = \int_{\partial\Omega}\nu\phi f\,dS - \int_\Omega \phi\,(Df)\,dV$.

**Proof.** A real scalar $\phi$ commutes with every $e_\mu$, so the Leibniz rule for $D$ gives $D(\phi f) = \sum_\mu e_\mu\partial_\mu(\phi f) = \sum_\mu e_\mu(\partial_\mu\phi) f + \sum_\mu e_\mu\phi\partial_\mu f = (D\phi)f + \phi\,Df$. The divergence theorem applied to $\phi f$ gives the displayed identity. $\square$

**Corollary (scalar Green identity).** Let $u, v$ be real-valued $C^2$ functions on $\bar{\Omega}$. Then

$$
\int_\Omega \bigl[\,v\,\Delta u - u\,\Delta v\,\bigr] dV = \int_{\partial\Omega} \Bigl[\,v\,\frac{\partial u}{\partial n} - u\,\frac{\partial v}{\partial n}\,\Bigr] dS,
$$

where $\Delta$ is the Laplacian of $\mathbb{R}^4$ and $\partial/\partial n$ is the outward normal derivative.

**Proof.** This is the classical Green identity for the Laplacian of $\mathbb{R}^4$ applied to two real-valued functions; it is the scalar case of the integration-by-parts identity, in which all factors commute. $\square$

### The Cauchy–Goursat Theorem

**Theorem (Cauchy–Goursat).** Let $f$ be left regular and $C^1$ on a bounded domain $\Omega$ with smooth boundary. Then

$$
\int_{\partial\Omega} \nu f \, dS = 0 .
$$

**Proof.** By the divergence theorem, $\int_{\partial\Omega}\nu f\,dS = \int_\Omega Df\,dV = 0$ because $f$ is left regular. $\square$

**Corollary.** If $f$ is right regular and $C^1$ then $\int_{\partial\Omega} f\nu\,dS = 0$.

The Cauchy–Goursat theorem is a statement about the boundary of a domain in $\mathbb{R}^4$, that is, about a three-dimensional hypersurface, not about a curve. A closed curve in a four-dimensional domain does not bound a hypersurface, so there is no curve form of the theorem; this is one of the structural differences from the complex case, where a closed contour bounds a surface and the integral of a holomorphic function vanishes on it.

## The Fundamental Solution

### Definition and Regularity

**Definition.** The **fundamental solution** of the Cauchy–Riemann operator on $\mathbb{H}$ is the function

$$
E(q) = \frac{\bar{q}}{|q|^4} = \frac{q^{-1}}{|q|^2}, \qquad q \neq 0 .
$$

It is homogeneous of degree $-3$, since $E(\lambda q) = \lambda^{-3}E(q)$ for $\lambda > 0$, and it is real-analytic away from the origin.

**Theorem.** $E$ is both left regular and right regular on $\mathbb{H} \setminus \{0\}$.

**Proof.** The partial derivatives of $E = \bar{q}|q|^{-4}$ are $\partial_\mu E = \bar{e}_\mu |q|^{-4} + \bar{q}\,\partial_\mu(|q|^{-4})$, and $\partial_\mu(|q|^{-4}) = -4 x_\mu |q|^{-6}$ because $\partial_\mu|q|^2 = 2x_\mu$. Hence

$$
DE = \sum_{\mu=0}^{3} e_\mu \partial_\mu E = \Bigl(\sum_\mu e_\mu \bar{e}_\mu\Bigr)|q|^{-4} - 4|q|^{-6}\Bigl(\sum_\mu x_\mu e_\mu\Bigr)\bar{q} = 4|q|^{-4} - 4|q|^{-6}q\bar{q},
$$

using $\sum_\mu e_\mu\bar{e}_\mu = 4$; since $q\bar{q} = |q|^2$ the two terms cancel and $DE = 0$. The computation of $ED$ is identical with $\bar{e}_\mu e_\mu$ in place of $e_\mu\bar{e}_\mu$ and $\bar{q}q$ in place of $q\bar{q}$, and also gives $0$. $\square$

The conjugate kernel is the fundamental solution of the conjugate operator: with

$$
\bar{E}(q) = \frac{q}{|q|^4} = \frac{(\bar{q})^{-1}}{|q|^2},
$$

the conjugation identity above, applied to $E$, gives $\bar{E}\,\bar{D} = 0$ on $\mathbb{H}\setminus\{0\}$; the same computation as for $E$, with $\bar{e}_\mu$ in place of $e_\mu$, gives $\bar{D}\bar{E} = 0$ as well. The distributional computation below gives $\bar{D}\bar{E} = \bar{E}\bar{D} = 2\pi^2\delta_0$.

### The Distributional Identity

**Theorem.** In the sense of distributions on $\mathbb{H}$,

$$
DE = ED = 2\pi^2 \delta_0, \qquad \bar{D}\bar{E} = \bar{E}\bar{D} = 2\pi^2 \delta_0,
$$

where $\delta_0$ is the delta distribution at the origin and $2\pi^2$ is the area of the unit sphere $S^3 \subset \mathbb{R}^4$.

**Proof.** The function $E$ is locally integrable and smooth away from the origin, and $DE = 0$ there; hence the distribution $DE$ is supported at $\{0\}$. It is homogeneous of degree $-4$, because $D$ lowers the degree of a homogeneous function by one, and the only distribution supported at the origin and homogeneous of degree $-4$ in four variables is a multiple of $\delta_0$. To compute the multiple, excise the singularity. On the annulus $\varepsilon < |q| < 1$ the function $E$ is smooth and $DE = 0$, so the divergence theorem gives

$$
\int_{|q| = 1} \nu E \, dS = \int_{|q| = \varepsilon} \nu E \, dS,
$$

where on each sphere $\nu = q/|q|$ is the normal pointing away from the origin; the inner sphere carries the negative sign in the boundary of the annulus, which is why the two fluxes are equal rather than opposite. On a sphere of radius $s$ one has $E = \bar{q}/s^4$ and $\nu = q/s$, so $\nu E = q\bar{q}/s^5 = 1/s^3$, and the flux is $\int_{|q| = s} dS/s^3 = 2\pi^2 s^3/s^3 = 2\pi^2$, independent of $s$. The flux through the shrinking sphere is therefore $2\pi^2$, and this is the mass of the distribution at the origin. The computation of $ED$ is the same with the right-handed divergence theorem, and conjugation gives the two conjugate identities. $\square$

The constant $2\pi^2$ is the four-dimensional analogue of the factor $2\pi$ of complex analysis: it is the surface area $\omega_4 = 2\pi^{4/2}/\Gamma(2)$ of $S^3$, and it is the reciprocal of the normalisation constant of the Cauchy kernel below. The function $E$ is therefore the **Cauchy kernel** of the theory, up to the factor $2\pi^2$.

## The Cauchy Integral Formula

### The Kernel–Normal Product

On the boundary of a ball, the quaternion product of the kernel and the conormal element collapses to a scalar.

**Theorem.** Let $y \in \mathbb{H}$, let $r > 0$ and let $w \in \partial B(y, r)$. Then

$$
E(w - y)\,\nu(w) = \nu(w)\,E(w - y) = \frac{1}{|w - y|^3} = \frac{1}{r^3},
$$

a positive real scalar independent of the direction of $w - y$.

**Proof.** On the sphere, $\nu(w) = (w - y)/|w - y|$ and $E(w - y) = \overline{(w - y)}/|w - y|^4$. Hence

$$
E(w - y)\nu(w) = \frac{\overline{(w - y)}\,(w - y)}{|w - y|^5} = \frac{|w - y|^2}{|w - y|^5} = \frac{1}{|w - y|^3},
$$

and the opposite order gives the same scalar because $(w - y)\overline{(w - y)} = \overline{(w - y)}(w - y) = |w - y|^2$. $\square$

The collapse of the product to a scalar is special to the quaternion case, where $z\bar{z} = \bar{z}z$ is central, and it is the reason the boundary integrals below can be read as weighted averages of $f$ over the boundary.

### The Cauchy–Pompeiu Representation

**Theorem (Cauchy–Pompeiu).** Let $\Omega$ be a bounded domain with smooth boundary, let $f$ be $C^1$ on $\bar{\Omega}$, and let $y \in \Omega$. Then

$$
f(y) = \frac{1}{2\pi^2}\int_{\partial\Omega} \frac{\overline{w - y}}{|w - y|^4}\,\nu(w)\,f(w)\,dS(w) - \frac{1}{2\pi^2}\int_\Omega \frac{\overline{w - y}}{|w - y|^4}\,(Df)(w)\,dV(w).
$$

**Proof (sketch).** Fix $y$ and remove from $\Omega$ a closed ball $\overline{B(y,\varepsilon)}$ to obtain $\Omega_\varepsilon$. Apply the divergence theorem to the field with components $F_\mu(w) = E(w - y)\,e_\mu\,f(w)$, where $E(q) = \bar{q}/|q|^4$ is the fundamental solution. Its divergence is

$$
\sum_{\mu=0}^{3} \partial_\mu F_\mu = \sum_\mu (\partial_\mu E)\, e_\mu f + E \sum_\mu e_\mu \partial_\mu f = (ED)f + E(Df) = E(Df),
$$

since $E$ is right regular, and its boundary term is $\sum_\mu n_\mu F_\mu = E\nu f$. Hence

$$
\int_{\Omega_\varepsilon} E(w-y)\,(Df)(w)\,dV = \int_{\partial\Omega} E(w-y)\,\nu(w)\,f(w)\,dS - \int_{\partial B(y,\varepsilon)} E(w-y)\,\nu(w)\,f(w)\,dS .
$$

On the small sphere the kernel–normal product is the scalar $1/\varepsilon^3$, so by continuity of $f$ the last integral tends to $2\pi^2 f(y)$ as $\varepsilon \to 0$, while the left side tends to $\int_\Omega E(w-y)(Df)(w)\,dV$; the identity follows. $\square$

The representation is the quaternionic instance of the general Cauchy–Pompeiu formula of *Hypercomplex Integration*: the boundary term reproduces $f$ when $f$ is regular, and the volume term corrects for the failure of regularity through $Df$. The kernel depends on the system only through the fundamental solution of its operator.

### The Cauchy Integral Formula for Regular Functions

**Theorem (Cauchy integral formula).** Let $f$ be left regular and $C^1$ on a domain containing the closed ball $\overline{B(y, r)}$. Then for every $q$ with $|q - y| < r$,

$$
f(q) = \frac{1}{2\pi^2} \int_{\partial B(y, r)} \frac{\overline{w - q}}{|w - q|^4} \, \nu(w) \, f(w) \, dS(w).
$$

**Proof.** Apply the Cauchy–Pompeiu representation with $\Omega = B(y,r)$; since $Df = 0$ throughout $\Omega$, the volume term vanishes and only the boundary term remains. The kernel is $E(w-q) = \overline{(w-q)}/|w-q|^4$ with the normalisation $1/(2\pi^2)$ fixed by the distributional identity $DE = 2\pi^2\delta_0$. $\square$

For a ball centred at the point of evaluation, $q = y$, the kernel–normal product is the scalar $1/r^3$, and the formula becomes the **mean value property**

$$
f(y) = \frac{1}{2\pi^2 r^3} \int_{\partial B(y, r)} f(w) \, dS(w).
$$

This is the mean value formula for harmonic functions, applied to the four components of the regular function; it shows directly that the Cauchy kernel is correctly normalised, and it exhibits the constant $\omega_4 = 2\pi^2$ as the surface area that makes the average an average.

### The Right-Regular Formula

**Theorem (right-regular Cauchy integral formula).** Let $f$ be right regular and $C^1$ on a domain containing $\overline{B(y,r)}$. Then for $|q - y| < r$,

$$
f(q) = \frac{1}{2\pi^2} \int_{\partial B(y, r)} f(w) \, \nu(w) \, \frac{\overline{w - q}}{|w - q|^4} \, dS(w).
$$

**Proof.** Let $f$ be right $D$-regular, so that $\bar{f}$ is left $\bar{D}$-regular. The left-handed formula for the conjugate operator $\bar{D}$ reads $\bar{f}(q) = \frac{1}{2\pi^2}\int_{\partial B}\bar{E}(w-q)\,\bar{\nu}(w)\,\bar{f}(w)\,dS(w)$, with kernel $\bar{E}$ and conormal element $\bar{\nu}$. Conjugating this identity reverses the order of the factors and uses $\overline{\bar{E}} = E$ and $\overline{\bar{\nu}} = \nu$, giving the displayed formula for $f$; the constant $2\pi^2$ is unchanged. $\square$

### The Two-Sided Cauchy Integral Formula

**Definition.** A function is **two-sided regular** if it is both left regular and right regular.

**Theorem (two-sided Cauchy integral formula).** Let $f$ be two-sided regular and $C^1$ on a domain containing $\overline{B(y,r)}$. Then for $|q - y| < r$ both formulas hold and they coincide:

$$
f(q) = \frac{1}{2\pi^2} \int_{\partial B(y, r)} \frac{\overline{w - q}}{|w - q|^4} \, \nu(w) \, f(w) \, dS(w) = \frac{1}{2\pi^2} \int_{\partial B(y, r)} f(w) \, \nu(w) \, \frac{\overline{w - q}}{|w - q|^4} \, dS(w).
$$

**Proof.** A two-sided regular function is left regular and right regular, so both theorems apply: the first integral equals $f(q)$ by the left-regular formula and the second equals $f(q)$ by the right-regular formula, whence the two are equal. The equality is not termwise: when $q \neq y$ the product $E(w-q)\nu(w)$ has a non-zero vector part, and only for $q = y$ does the kernel–normal theorem make it the scalar $1/r^3$. $\square$

**Remark.** The kernel $E$ is itself two-sided regular by the theorem of the preceding section, so the two-sided formula can be read as the statement that both the function and the kernel are regular from both sides. In the complex case, where the algebra is commutative, the distinction between the two orders disappears and the two-sided formula reduces to the single classical formula. In the quaternion case the two integrands are genuinely different functions of $w$ for $q \neq y$; the kernel–normal collapse, and with it the coincidence of the two orders, takes place only at $q = y$, where the formula becomes the mean value property.

## Consequences of the Cauchy Integral Formula

### The Mean Value Property

**Theorem.** If $f$ is left regular on a domain containing the closed ball $\overline{B(y,r)}$, then

$$
f(y) = \frac{1}{2\pi^2 r^3} \int_{\partial B(y, r)} f(w) \, dS(w) = \frac{2}{\pi^2 r^4} \int_{B(y, r)} f(w) \, dV(w).
$$

**Proof.** The surface form was obtained above from the Cauchy formula at $q = y$. For the volume form, integrate the surface form over the radius: the volume of the ball is $\int_0^r 2\pi^2 s^3\,ds = \frac{\pi^2}{2}r^4$, so the average of $f$ over the ball of radius $r$ equals the common value $f(y)$. $\square$

### The Maximum Principle

**Theorem (maximum modulus principle).** If $f$ is left regular on a domain $\Omega$ and $|f|$ attains a maximum at an interior point of $\Omega$, then $f$ is constant on $\Omega$.

**Proof.** Suppose $|f|$ attains its maximum $M$ at $y \in \Omega$. The mean value property bounds $|f(y)|$ by the average of $|f|$ over a small sphere, which is at most $M$; equality forces $|f| = M$ on that sphere. Extending along a connected chain of spheres, $|f| = M$ on $\Omega$, and a regular function of constant modulus is constant because $0 = \Delta|f|^2 = 2\sum_\mu|\partial_\mu f|^2$. $\square$

### Liouville's Theorem

**Theorem (Liouville).** Every bounded left regular function on all of $\mathbb{H}$ is constant.

**Proof.** Let $|f| \leq M$ and fix $y$. The Cauchy integral formula on the sphere $\partial B(y, r)$ expresses $f(y)$ as $\frac{1}{2\pi^2}\int_{\partial B(y,r)}K(y,w)\,dS(w)$ with kernel $K(q,w) = E(w-q)\nu(w)f(w)$. Differentiating under the integral sign, $\partial_k f(y) = \frac{1}{2\pi^2}\int_{\partial B(y,r)}\partial_k K(y,w)\,dS(w)$, and $\partial_k K = -\partial_{w_k}E(w-q)\big|_{q=y}\nu f$. On the sphere $|w - y| = r$, the derivative of $E$ is bounded by a constant times $r^{-4}$, so $|\partial_k K| \leq C M r^{-4}$; the surface area is $2\pi^2 r^3$, and therefore $|\partial_k f(y)| \leq C M r^{-1}$. Letting $r \to \infty$ gives $\partial_k f(y) = 0$ for every $k$; since $y$ was arbitrary, $f$ is constant. $\square$

### The Cauchy Estimates

**Theorem (Cauchy estimates).** Let $f$ be left regular on a ball $B(y, R)$ with $|f| \leq M$ on the boundary. Then for every multi-index $\alpha$ there is a constant $C_\alpha$, depending only on $\alpha$, with

$$
\left| \partial^\alpha f(y) \right| \leq \frac{C_\alpha M}{R^{|\alpha|}} .
$$

**Proof.** Differentiate the Cauchy integral formula $|\alpha|$ times with respect to $q$ under the integral sign. Each differentiation increases the order of the singularity of the kernel by one, so the integrand is bounded by a constant times $R^{-3-|\alpha|}$, and the surface area contributes $2\pi^2 R^3$. $\square$

**Corollary (Liouville, second proof).** A regular function bounded on $\mathbb{H}$ has all derivatives zero at every point and is constant.

### The Identity Theorem

**Theorem (identity theorem).** If two left regular functions on a connected domain $\Omega$ agree on a set with an accumulation point in $\Omega$, then they agree on all of $\Omega$.

**Proof.** The difference $h = f - g$ is left regular and vanishes on a set $S$ with an accumulation point $p \in \Omega$. A left regular function is real-analytic: its four real components are harmonic, and the Cauchy integral formula represents $h$ near $p$ by a power series that converges to $h$ on a ball about $p$ contained in $\Omega$. A real-analytic function on a connected open set that vanishes on a set having an accumulation point in that set is identically zero. Hence $h = 0$ on a neighbourhood of $p$, and by connectedness on all of $\Omega$. $\square$

## Relation to the General Hypercomplex Integration

The theory above is the quaternionic instance of the general integration theory of an elliptic hypercomplex system $(A, D)$ treated in *Hypercomplex Integration*. In that general setting $A$ is a finite-dimensional unital associative real algebra with basis $e_0 = 1, \dots, e_{m-1}$, the operator is $D = \partial_0 + \sum_{k\geq1} B_k\partial_k$ with $B_jB_k + B_kB_j = -2\delta_{jk}$, and $E$ denotes a fundamental solution of $D$, so that $E(x-y)$ is a Cauchy kernel. The conormal element $\nu_B = \sum_\alpha \nu_\alpha B_\alpha$ of *Regularity and the Cauchy–Riemann Operator* is the general form of the quaternion $\nu$.

The dictionary for the quaternion case is:

| general system | quaternion case |
|---|---|
| algebra $A$, dimension $m$ | $\mathbb{H}$, dimension $m = 4$ |
| coefficients $B_k$ | $e_k$, $k = 1, 2, 3$ |
| conormal element $\nu_B$ | $\nu = \sum_\mu n_\mu e_\mu$ |
| fundamental solution $E$ | $\bar{q}/\lvert q\rvert^4$, with $DE = ED = 2\pi^2\delta_0$ |
| surface area $\omega_m$ | $\omega_4 = 2\pi^2$ |
| Cauchy–Goursat | $\int_{\partial\Omega}\nu f\,dS = 0$ for left regular $f$ |
| Cauchy integral formula | $f(q) = \frac{1}{2\pi^2}\int_{\partial B}\frac{\overline{w-q}}{\lvert w-q\rvert^4}\nu(w)f(w)\,dS$ |

In the general theory the boundary of a domain is a hypersurface and the Cauchy–Goursat theorem is a hypersurface statement; the quaternion case is the case of dimension four. The two properties that the general theory isolates and that are special to the quaternion algebra are the multiplicativity of the norm form, which makes $\mathbb{H}$ a division algebra and makes the symbol invertible, and the centrality of $z\bar{z}$, which makes the kernel–normal product scalar. Both are needed for the statements above in their sharp form; the biquaternion algebra of category 30, which is $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ and is not a division algebra, is treated separately.

## Summary

The integral of a quaternion-valued function is defined componentwise: the domain integral over a domain in $\mathbb{H}$ is the Lebesgue integral of the four components, the path integral along a curve has a left and a right form because of non-commutativity, and the surface integral over a hypersurface is taken against the conormal element $\nu = \sum_\mu n_\mu e_\mu$. The integral is linear, additive, and obeys the fundamental estimate.

Because the coefficients of the Cauchy–Riemann operator $D = \partial_0 + e_1\partial_1 + e_2\partial_2 + e_3\partial_3$ are constant, $Df = \sum_\mu \partial_\mu(e_\mu f)$ is a divergence, and the divergence theorem reads $\int_\Omega Df\,dV = \int_{\partial\Omega}\nu f\,dS$, with the conjugate identity for $\bar{D}$. The Cauchy–Goursat theorem, that $\int_{\partial\Omega}\nu f\,dS = 0$ for left regular $f$, is an immediate consequence, and it is a statement about a three-dimensional boundary, not about a curve. Left regularity and right regularity are distinct and are exchanged by quaternion conjugation; the operators satisfy $D\bar{D} = \bar{D}D = \Delta$ and $D$ is elliptic.

The fundamental solution is $E(q) = \bar{q}/|q|^4 = q^{-1}/|q|^2$, which is both left and right regular away from the origin and satisfies $DE = ED = 2\pi^2\delta_0$, with $2\pi^2$ the surface area of $S^3$. The kernel–normal product $E(w-y)\nu(w)$ is the scalar $1/|w-y|^3$, so that the Cauchy integral formula

$$
f(q) = \frac{1}{2\pi^2} \int_{\partial B(y,r)} \frac{\overline{w-q}}{|w-q|^4}\,\nu(w)\,f(w)\,dS(w)
$$

holds for left regular $f$, its mirror image with the kernel on the right holds for right regular $f$, and the two coincide for two-sided regular functions; this is the two-sided Cauchy integral formula. From it follow the mean value property, the maximum modulus principle, Liouville's theorem, the Cauchy estimates and the identity theorem. The general shape of all of these is that of *Hypercomplex Integration*, and the quaternion case is the four-dimensional instance of that theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $q = q_0 + \mathbf{q} = \sum_\mu q_\mu e_\mu$ | General quaternion, scalar part $q_0$, vector part $\mathbf{q}$ |
| $\bar{q} = q_0 - \mathbf{q}$ | Quaternion conjugate |
| $N(q) = q\bar{q} = \lvert q\rvert^2$ | Norm form and modulus |
| $\partial_\mu = \partial/\partial x_\mu$ | Coordinate derivatives, $q = x_0 + x_1e_1 + x_2e_2 + x_3e_3$ |
| $D = \partial_0 + e_1\partial_1 + e_2\partial_2 + e_3\partial_3$ | Cauchy–Riemann operator |
| $\bar{D} = \partial_0 - e_1\partial_1 - e_2\partial_2 - e_3\partial_3$ | Conjugate operator |
| $D\bar{D} = \bar{D}D = \Delta$ | Factorisation of the Laplacian |
| $\sigma_D(\xi) = \xi_0 + \xi_1e_1 + \xi_2e_2 + \xi_3e_3$ | Symbol of $D$ at the covector $\xi$; $D$ is elliptic |
| $Df = 0$ | Left regularity |
| $fD = \partial_0 f + (\partial_1 f)e_1 + (\partial_2 f)e_2 + (\partial_3 f)e_3 = 0$ | Right regularity |
| $\int_\Omega f\,dV$ | Domain integral, componentwise Lebesgue |
| $\operatorname{vol}(\Omega)$ | Volume of the domain $\Omega$ |
| $\int_\gamma f\,dq$, $\int_\gamma dq\,f$ | Left and right path integrals |
| $\nu = \sum_{\mu=0}^{3} n_\mu e_\mu$ | Conormal element, $\lvert \nu \rvert = 1$ |
| $\int_{\partial\Omega} \nu f\,dS$ | Conormal surface integral |
| $E(q) = \bar{q}/\lvert q\rvert^4 = q^{-1}/\lvert q\rvert^2$ | Fundamental solution and Cauchy kernel |
| $\bar{E}(q) = q/\lvert q\rvert^4$ | Fundamental solution of $\bar{D}$ |
| $DE = ED = 2\pi^2\delta_0$ | Distributional identity; $\delta_0$ is the delta distribution at the origin |
| $y$ | Fixed point of $\Omega$; centre of the ball $B(y,r)$ |
| $E(w-y)\nu(w) = \lvert w-y\rvert^{-3}$ | Kernel–normal product |
| $\omega_4 = 2\pi^2$ | Area of the unit sphere $S^3$ |
| two-sided regular | left regular and right regular |

## Further Reading

- Rudolf Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta\Delta u = 0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* **7** (1934–35) 307–330, for the origin of the Cauchy theory for quaternion-valued functions of four real variables.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Cauchy–Pompeiu formula, the Cauchy kernel and the monogenic function theory.
- R. Delanghe, F. Sommen, and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for spinor-valued function theory, its kernels and its function-theoretic invariants.
- A. Sudbery, "Quaternionic analysis", *Mathematical Proceedings of the Cambridge Philosophical Society* **85** (1979) 199–225, for the quaternionic Cauchy integral formula and its normalisation.
- John Ryan, *Clifford Algebras in Analysis and Related Topics* (CRC Press, 1996), for the analytic theory and the boundary-value problems.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the identification of $\mathbb{H}$ with a Clifford algebra and the role of the norm form.
