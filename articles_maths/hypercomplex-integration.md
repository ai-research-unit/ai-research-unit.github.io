
# __Hypercomplex Integration__

## Introduction

The preceding articles built the differential side of hypercomplex analysis: a generalised Cauchy–Riemann operator $D$, the regular functions it annihilates, and the Cauchy–Pompeiu representation of a function by its boundary values. This article develops the integral side as a subject in its own right: integrals of $A$-valued functions and forms, the Cauchy–Goursat theorem for closed hypersurfaces, the failure of the naive curve version of the Cauchy theorem over a non-commutative algebra, primitives and path independence in the commutative case, the Cauchy transform as a function of the parameter, and the jump formulas at a boundary.

The treatment is general. The particular systems of categories 26 to 29 have their own explicit kernels, residues and expansions, and those computations are not repeated here; what is common to all of them is the shape of the integral theorems, and it is that shape that this article fixes. Throughout, $(A,D)$ is an elliptic hypercomplex system in the sense of *Hypercomplex Analysis*: $A$ is a finite-dimensional unital associative real algebra of dimension $m$ with basis $e_0 = 1, \dots, e_{m-1}$,

$$
D = \partial_0 + \sum_{k \geq 1} B_k \partial_k, \qquad \bar D = \partial_0 - \sum_{k\geq1} B_k\partial_k, \qquad D\bar D = \bar D D = \Delta,
$$

the coefficients satisfying $B_jB_k + B_kB_j = -2\delta_{jk}$ and $B_k^2 = -1$. The conormal element $\nu_B = \sum_\alpha \nu_\alpha B_\alpha$ of *Regularity and the Cauchy–Riemann Operator* is used throughout, and $E$ denotes a fundamental solution of $D$, so that $E(x-y)$ is a Cauchy kernel.

## Integrals of Hypercomplex-Valued Functions

**Definition.** Let $\gamma : [a,b] \to A$ be a piecewise $C^1$ path and let $f$ be continuous on a neighbourhood of its image. The **left hypercomplex line integral** of $f$ along $\gamma$ is

$$
\int_\gamma f(\xi)\, d\xi = \int_a^b f(\gamma(t))\,\gamma'(t)\, dt,
$$

and the **right hypercomplex line integral** is

$$
\int_\gamma d\xi\, f(\xi) = \int_a^b \gamma'(t)\, f(\gamma(t))\, dt.
$$

The integral of a path is defined coordinatewise: writing $f = \sum_\alpha f^\alpha e_\alpha$ and $\gamma = \sum_\alpha \gamma^\alpha e_\alpha$, the product $f(\gamma(t))\gamma'(t)$ expands by the multiplication of $A$, and each of the $m$ resulting real integrals is an ordinary Riemann integral.

The two integrals differ for non-commutative $A$, and the order of the factors is part of the notation. For commutative $A$ they coincide. When $\gamma$ is a closed path the integral is called the **contour integral** of $f$ around $\gamma$, and it is the quantity to which the classical Cauchy theorem refers.

**Proposition (the estimate).** For a piecewise $C^1$ path $\gamma$ and a continuous $f$,

$$
\Bigl\|\int_\gamma f\, d\xi\Bigr\| \leq \sup_{t} \|f(\gamma(t))\|\,\int_a^b \|\gamma'(t)\|\, dt = \sup_\gamma \|f\|\cdot \ell(\gamma),
$$

where $\ell(\gamma)$ is the Euclidean length of $\gamma$.

*Proof.* The integral is a limit of Riemann sums $\sum_i f(\gamma(t_i))(\gamma(t_{i+1}) - \gamma(t_i))$; submultiplicativity gives the estimate for each sum, and the norm is continuous, so the inequality passes to the limit. $\square$

**Definition.** A **hypercomplex differential $1$-form** is an expression $\omega = f\,d\xi$ with $f$ an $A$-valued function; its integral along $\gamma$ is $\int_\gamma f\,d\xi$ as above. A form is **closed** if $\int_\gamma \omega = 0$ for every closed piecewise $C^1$ path $\gamma$ in the domain, and **exact** if $\omega = dG$ for some $A$-valued function $G$, where $(dG)(\xi) = $ the $A$-linear part of the differential of $G$.

## The Cauchy–Goursat Theorem

The fundamental integral theorem of the theory is the hypersurface version; it follows from the divergence form of $D$ established in *Regularity and the Cauchy–Riemann Operator*.

**Theorem (Cauchy–Goursat).** Let $\Omega$ be a bounded domain with smooth boundary and let $f$ be left regular and of class $C^1$ on $\bar\Omega$. Then

$$
\int_{\partial\Omega} \nu_B(y)\, f(y)\, dS(y) = 0,
$$

where $\nu_B$ is the conormal element and $dS$ the surface measure.

This is the analogue of $\oint f\,dz = 0$ for a holomorphic function: the boundary integral of a regular function over a closed hypersurface vanishes. When $m = 2$ the hypersurface is a curve, and for the complex system the statement is exactly the classical Cauchy theorem.

**Proposition (when the curve theorem holds).** The form $\omega = f\,d\xi$ is closed if and only if

$$
\partial_\alpha f\, B_\beta = \partial_\beta f\, B_\alpha \qquad \text{for all } \alpha, \beta,
$$

with $B_0 = 1$. This condition is equivalent to regularity for the complex system, and is strictly stronger than regularity in general.

*Proof.* The exterior derivative is

$$
d(f\,d\xi) = df \wedge d\xi = \sum_{\alpha < \beta} \bigl(\partial_\alpha f\, B_\beta - \partial_\beta f\, B_\alpha\bigr)\, d\xi_\alpha \wedge d\xi_\beta,
$$

since $d\xi = \sum_\beta B_\beta\, d\xi_\beta$ and $f$ is $A$-valued. Hence closure is the stated system of equations. For the complex system, the equations with $(\alpha,\beta) = (0,1)$ read $\partial_0 f\, i = \partial_1 f$, that is $\partial_1 f = i\,\partial_0 f$; then

$$
\partial_0 f + i\,\partial_1 f = \partial_0 f + i\,(i\,\partial_0 f) = \partial_0 f - \partial_0 f = 0,
$$

so $Df = 0$, and conversely $Df = 0$ gives $i\,\partial_1 f = -\partial_0 f$, or $\partial_1 f = i\,\partial_0 f$. The general system imposes one $A$-valued condition per pair $(\alpha,\beta)$, that is, $m\binom{m}{2}$ real equations against the $m^2$ real equations of $Df = 0$; for $m \geq 4$ these are more, and the extra conditions need not follow — as the next proposition shows for $A = \mathbb{H}$. $\square$

**Theorem (the classical Cauchy theorem).** For the complex system $A = \mathbb{C}$, $D = \partial_0 + i\partial_1$, a $C^1$ function is left regular if and only if the form $f\,d\xi$ is closed; hence on a simply connected domain

$$
\int_\gamma f\,d\xi = 0
$$

for every closed piecewise $C^1$ path $\gamma$, and $f$ has a primitive. This is Cauchy's theorem.

**Proposition (failure of the curve version in the non-commutative case).** Let $A = \mathbb{H}$ with the quaternionic system. Then there is a left regular function whose integral over a closed curve does not vanish.

*Proof.* Consider the linear function

$$
f(q) = q_1 - e_1 q_0, \qquad q = q_0 + q_1 e_1 + q_2 e_2 + q_3 e_3 .
$$

It is left regular, since

$$
D f = e_0\,\partial_0 f + e_1\,\partial_1 f = e_0(-e_1) + e_1 e_0 = -e_1 + e_1 = 0 .
$$

Let $\gamma(t) = r\cos t\, e_1 + r \sin t\, e_2$ for $t \in [0, 2\pi]$, a closed circle in the plane spanned by $e_1, e_2$. Along $\gamma$ one has $q_0 = 0$ and $q_1 = r\cos t$, so $f(\gamma(t)) = r\cos t$, and $\gamma'(t) = -r\sin t\, e_1 + r\cos t\, e_2$. Therefore

$$
\int_\gamma f\, d\xi = \int_0^{2\pi} r\cos t\,\bigl(-r\sin t\, e_1 + r\cos t\, e_2\bigr)\, dt = -r^2 e_1 \int_0^{2\pi}\sin t\cos t\, dt + r^2 e_2\int_0^{2\pi}\cos^2 t\, dt = \pi r^2 e_2 \neq 0 .
$$

So a regular function over a non-commutative algebra need not have closed curve integrals. $\square$

**Remark.** The failure is structural, not accidental: the curve theorem is a statement about the closedness of the $1$-form $f\,d\xi$, and in a non-commutative algebra the order in which the coefficients $B_\alpha$ and the partial derivatives appear prevents the $m$ equations of regularity from implying the $\binom{m}{2}$ equations of closedness. The general integral theorem of the theory is therefore the hypersurface theorem, not the curve theorem.

## Idempotent and Characteristic Coordinates

The line integral is an ordinary integral together with the multiplication of $A$, so when the algebra decomposes the integral decomposes with it, and the whole integral theory of a decomposable system is the sum of ordinary one-dimensional theories.

**Proposition (splitting of the integral).** Let $e_1, \dots, e_r \in A$ be a complete set of orthogonal central idempotents: $e_i^2 = e_i$, $e_ie_j = 0$ for $i \neq j$, $\sum_i e_i = 1$. Then $A = \bigoplus_i A_i$ with $A_i = e_iA = Ae_i$ two-sided ideals, every element has the form $\sum_i e_i \xi e_i$, and for a piecewise $C^1$ path $\gamma$ and a continuous $f$,

$$
\int_\gamma f\,d\xi = \sum_{i=1}^{r} \int_\gamma f_i\,d\xi_i, \qquad f_i = e_if\,e_i, \quad \xi_i = e_i\xi\,e_i,
$$

each term being an integral in the subalgebra $A_i$ with unit $e_i$. If every $A_i$ is one-dimensional, the hypercomplex integral is the sum of $r$ ordinary real integrals.

*Proof.* Insert the decompositions into the Riemann sums $\sum_j f(\gamma(t_j))\,(\gamma(t_{j+1}) - \gamma(t_j)) = \sum_j f(\gamma(t_j))\,\gamma'(t_j)\,\Delta t_j + o(1)$; the orthogonality relations give $f_i\gamma_i'$ in the $i$-th component and kill every cross term, and the product of the sums is the sum of the products because the idempotents are central and orthogonal. $\square$

**Theorem (the hypersurface theorem, split).** Let $e_1, \dots, e_r$ be a complete set of orthogonal central idempotents, let $f$ be left regular, and let $\Omega$ be a bounded domain with smooth boundary. Then

$$
\int_{\partial\Omega}\nu_B(y)f(y)\,dS(y) = \sum_{i=1}^r \int_{\partial\Omega}\nu_B^{(i)}(y)f_i(y)\,dS(y) = 0,
$$

the $i$-th summand vanishing by the divergence theorem in the subalgebra $A_i$; in the split complex case the two summands vanish because $f_+$ is independent of $\xi_+$ and $f_-$ is independent of $\xi_-$.

**Example (the split complex numbers).** With $e_\pm = \tfrac12(1\pm j)$ and $\xi_\pm = x_0 \pm x_1$ one has $d\xi = e_+d\xi_+ + e_-d\xi_-$ and

$$
\int_\gamma f\,d\xi = e_+\int_{\gamma_+}f_+\,d\xi_+ + e_-\int_{\gamma_-}f_-\,d\xi_-,
$$

where $\gamma_\pm$ are the projections of $\gamma$ onto the two characteristic coordinates. Each term is an ordinary real line integral, and no single Cauchy formula can represent their sum; this is the idempotent form of the failure of a Cauchy integral formula in $\mathbb{D}$ recorded. The curve form of Cauchy's theorem fails too: the closure condition $\partial_0fj = \partial_1f$ for a left regular $f = f_+(\xi_-)e_+ + f_-(\xi_+)e_-$ reads $-2f_+'(\xi_-)e_+ + 2f_-'(\xi_+)e_- = 0$, so it holds only for constant $f$, while the hypersurface form above holds for every regular $f$. The two statements are not in conflict: the curve theorem is the closedness of the form, the hypersurface theorem is the divergence theorem for $D$.

**Remark (path independence and zero divisors).** Path independence of $\int_\gamma f\,d\xi$ is governed by the closedness of the form, exactly as in the classical theory: on a simply connected domain a closed form is exact, and the primitive is built by integration, an operation that uses no division. The zero divisors enter elsewhere. First, a primitive is a function that is left $A$-differentiable with derivative $f$, so where $f$ takes a non-invertible value the differential is a non-invertible linear map and the inverse-function arguments that the classical theory uses locally are unavailable. Second, an expansion of a regular function at a singularity requires powers of $\xi - x_0$, and where $\xi - x_0$ is a zero divisor no such expansion exists; the singularities of a kernel supported on the null cone therefore have no Laurent description, which is why the residue calculus of the general theory is stated as an integral over a small sphere rather than as a coefficient extraction. Third, in an algebra with idempotents the integral splits, and the components that contribute nothing are exactly those in which the integrand is constant along the corresponding characteristic direction.

**Remark (the relation to the measure-theoretic integral).** The hypercomplex line integral is not the integral of an $A$-valued function against a measure, but the pairing of the values with the $A$-valued differential $d\xi$. For a parametrised path the two agree: since $A$ is finite-dimensional and its norm is equivalent to the Euclidean norm, the map $t \mapsto f(\gamma(t))\gamma'(t)$ is Bochner integrable on $[a,b]$ for continuous $f$, and $\int_\gamma f\,d\xi$ is its Bochner integral against Lebesgue measure. Every statement about the hypercomplex integral that uses only linearity, the triangle inequality and completeness therefore follows from the general theory of the Bochner integral, and in this sense the measure-theoretic integral supplies the underlying integration of an algebra-valued function. What the general theory does not supply is the algebra: it is the multiplication by $\gamma'$ on the right that makes the integral hypercomplex rather than vector-valued, and it is that multiplication which produces the two-sidedness, the splitting and the failure of the curve theorem over a non-commutative algebra.

## Primitives and the Cauchy Integral Formula

**Definition.** Let $f$ be $A$-valued on a domain $\Omega$. A **primitive** of $f$ is a $C^1$ function $G$ on $\Omega$ with $dG = f\,d\xi$, meaning that the $A$-linear differential of $G$ at $x$ is left multiplication by $f(x)$:

$$
G(x + h) = G(x) + f(x)\,h + o(\|h\|).
$$

A primitive in this sense is left $A$-differentiable with derivative $f$, and by the rigidity theorem of *Hypercomplex Analysis* such functions are scarce: over $\mathbb{H}$ the only left $\mathbb{H}$-differentiable functions are the affine ones. A primitive of a given $f$ therefore exists only when the form $f\,d\xi$ is exact, which by the closure computation requires the stronger condition $\partial_\alpha f\,B_\beta = \partial_\beta f\,B_\alpha$.

**Proposition (primitives and exactness).** A function $f$ has a primitive on $\Omega$ if and only if the form $f\,d\xi$ is exact on $\Omega$. If $\Omega$ is simply connected and $f\,d\xi$ is closed, then

$$
G(x) = \int_{x_0}^{x} f(\xi)\,d\xi
$$

along any path from a fixed base point is well defined and is a primitive of $f$.

*Proof.* A primitive $G$ satisfies $f\,d\xi = dG$ by definition. Conversely, closedness makes the integral path-independent on a simply connected domain (the Poincaré lemma for $A$-valued forms), and differentiating along a straight segment from $x$ to $x+h$ gives $G(x+h) - G(x) = f(x)h + o(\|h\|)$. $\square$

**Corollary (the complex case).** For the complex system, every left regular function on a simply connected domain has a primitive, by Cauchy's theorem. For the quaternionic system, by contrast, a primitive can exist only for constant functions, because the only left $\mathbb{H}$-differentiable functions are affine; this is the primitive-level form of the failure of the curve theorem.

**Theorem (Morera, general form).** Let $f$ be continuous on a simply connected domain $\Omega$ and suppose $\int_{\partial R} f\,d\xi = 0$ for every axis-parallel rectangle $R \subseteq \Omega$. Then $f\,d\xi$ is closed and $f$ has a primitive on $\Omega$.

*Proof.* Integrate $f$ along axis-parallel paths to build $G$; the rectangle hypothesis makes the result path-independent. Then $G$ is differentiable with $f\,d\xi = dG$, so the form is exact and hence closed. $\square$

**Theorem (Cauchy integral formula, general form).** Let $\Omega$ be a bounded domain with smooth boundary, $E$ a Cauchy kernel for $D$, and $f$ left regular on a neighbourhood of $\bar\Omega$. Then for every $x \in \Omega$,

$$
f(x) = \int_{\partial\Omega} E(x-y)\,\nu_B(y)\,f(y)\,dS(y).
$$

This was stated in *Hypercomplex Analysis* and derived there from the Cauchy–Pompeiu formula; in the commutative case it is the classical Cauchy formula, and in the quaternionic case it is the Cauchy formula for monogenic functions. The kernel $E$ is specific to the system; the formula is not.

**Corollary (Cauchy inequalities).** Let $f$ be left regular on a ball $B(x_0,r)$ and continuous on its closure. Then

$$
\|f(x_0)\| \leq \frac{1}{C r^{m-1}} \int_{\partial B(x_0,r)} \|E(x_0-y)\|\,\|\nu_B(y)\|\,\|f(y)\|\,dS(y),
$$

for a normalising constant $C$ depending on the kernel; in particular $\|f(x_0)\| \leq M(r)\sup_{\partial B}\|f\|$ for a constant $M(r)$ depending only on $r$ and the system.

*Proof.* Insert the Cauchy formula and apply the integral estimate of the first section. $\square$

## Singularities, Residues and Expansions

**Definition.** Let $x_0 \in A$ and let $f$ be left regular on a punctured neighbourhood $\dot U = U \setminus \{x_0\}$ but not on $U$. The **residue** of $f$ at $x_0$ is the element

$$
\operatorname{Res}_{x_0} f = \int_{\partial B(x_0,\epsilon)} \nu_B(y)\, f(y)\, dS(y) \in A,
$$

for $0 < \epsilon$ small enough that $B(x_0,\epsilon) \setminus \{x_0\} \subseteq \dot U$ and independent of $\epsilon$.

*Proof of independence of $\epsilon$.* The difference of the integrals over two spheres is the boundary integral of a regular function over the region between them, which vanishes by Cauchy–Goursat. $\square$

**Theorem (residue theorem, general form).** Let $\Omega$ be a bounded domain with smooth boundary and let $f$ be left regular on $\bar\Omega$ except at finitely many points $x_1, \dots, x_k$ in the interior, with a removable-type behaviour at the boundary. Then

$$
\int_{\partial\Omega} \nu_B(y)\,f(y)\,dS(y) = \sum_{i=1}^{k} \operatorname{Res}_{x_i} f.
$$

*Proof.* Excise a small ball around each $x_i$ and apply Cauchy–Goursat to the punctured domain. $\square$

**Expansions.** A regular function is real-analytic (*Regularity and the Cauchy–Riemann Operator*), so on a ball it has a convergent power series

$$
f(x) = \sum_{\nu} c_\nu\, x^\nu, \qquad c_\nu \in A,
$$

in the coordinates of $A$, but the coefficients are not free: the equation $Df = 0$ imposes linear relations among them of a definite shape. The **Taylor-type expansion** of the theory is the expression of $f$ in a basis of the kernel of $D$ inside the space of homogeneous polynomials of each degree, the *inner spherical monogenics* of the system. The dimension and the explicit basis of these spaces depend on the system, and they are computed in the particular theories of categories 26 to 29. What is general is the existence of the expansion and the finiteness of the dimension of each homogeneous piece.

**Definition.** The **solid spherical monogenics** of degree $\nu$ for $(A,D)$ are the left regular homogeneous polynomials of degree $\nu$ on $A$. Their space is written $\mathcal{M}_\nu(A,D)$ and is finite-dimensional, with $\mathcal{M}_0$ spanned by the constants.

**Proposition.** The restriction map to the unit sphere, $P \mapsto P|_{\partial B(0,1)}$, is injective on $\mathcal{M}_\nu(A,D)$ for every $\nu$.

*Proof.* A homogeneous polynomial vanishing on the unit sphere vanishes identically by homogeneity. $\square$

## The Cauchy Transform and Jump Formulas

**Definition.** Let $\Omega$ be a bounded domain with smooth boundary and let $h$ be a continuous $A$-valued function on $\partial\Omega$. The **Cauchy transform** of $h$ is

$$
(\mathcal{C}h)(x) = \int_{\partial\Omega} E(x-y)\,\nu_B(y)\,h(y)\,dS(y), \qquad x \in \Omega.
$$

**Theorem (regularity of the transform).** For $x \in \Omega$, the Cauchy transform $\mathcal{C}h$ is left regular in $x$.

*Proof.* For $x$ in the interior and away from $\partial\Omega$, the dependence on $x$ enters only through $E(x-y)$, so differentiating under the integral sign and using that $D_x E(x-y) = 0$ for $x \neq y$ (because $D_yE = 0$ away from the origin and the kernel depends on the difference) gives $D(\mathcal{C}h)(x) = 0$. $\square$

**Theorem (jump formula).** Let $h$ be continuous on $\partial\Omega$ and let $\mathcal{C}^\pm$ denote the Cauchy transform evaluated as $x$ approaches $\partial\Omega$ from inside and from outside. Then

$$
\mathcal{C}^+ h - \mathcal{C}^- h = h
$$

pointwise on $\partial\Omega$, up to the normalisation of the kernel.

*Proof (sketch).* The difference of the two transforms is the principal value of the boundary integral, and the singular part of the kernel contributes the value of the density; this is the Plemelj–Sokhotski computation, valid for the kernels of elliptic first-order operators. The precise constant is fixed by the normalisation of $E$. $\square$

**Corollary (the Cauchy transform as a projection).** On the space of boundary values of regular functions, the inside transform $\mathcal{C}^+$ acts as the identity and the outside transform $\mathcal{C}^-$ acts as zero.

The Cauchy transform and the jump formula are the abstract content of the integral representation theory; the explicit Hardy-space and singular-integral theory of a particular system is developed from these formulas with its own kernel.

## Summary

The **hypercomplex line integral** $\int_\gamma f\,d\xi = \int_a^b f(\gamma(t))\gamma'(t)\,dt$ and its right-handed analogue are the basic integrals of the theory; they satisfy the estimate $\|\int_\gamma f\,d\xi\| \leq \sup\|f\|\,\ell(\gamma)$. The **Cauchy–Goursat theorem** is the hypersurface statement $\int_{\partial\Omega}\nu_B f\,dS = 0$ for a left regular function, and it is the general integral theorem of hypercomplex analysis. The curve version, $\oint f\,d\xi = 0$ for a closed path, holds exactly when the form $f\,d\xi$ is closed, that is when $\partial_\alpha f\,B_\beta = \partial_\beta f\,B_\alpha$ for all $\alpha,\beta$; for the complex system this condition is equivalent to regularity, giving Cauchy's theorem, primitives and Morera's theorem. It **fails** in general: over $\mathbb{H}$ the regular function $f(q) = q_1 - e_1 q_0$ has $\int_\gamma f\,d\xi = \pi r^2 e_2 \neq 0$ over a circle of radius $r$, so regularity does not force closed curve integrals, and over $\mathbb{H}$ only constant functions possess primitives.

The **Cauchy integral formula** $f(x) = \int_{\partial\Omega}E(x-y)\nu_B(y)f(y)dS(y)$ represents a regular function by its boundary values against the Cauchy kernel $E = \bar D\Phi$, and yields the Cauchy inequalities. **Residues** are defined as integrals over small spheres, and the residue theorem sums them; regular functions have power series expansions whose coefficient spaces are the finite-dimensional spaces $\mathcal{M}_\nu(A,D)$ of solid spherical monogenics, whose explicit description is system-specific. The **Cauchy transform** $\mathcal{C}h$ is regular inside $\Omega$, and the **jump formula** $\mathcal{C}^+h - \mathcal{C}^-h = h$ recovers the density from the difference of the inside and outside values.

When $A$ has a complete set of orthogonal central idempotents the integral **splits**, $\int_\gamma f\,d\xi = \sum_i \int_\gamma f_i\,d\xi_i$ with $f_i = e_ife_i$ and $\xi_i = e_i\xi e_i$, and the integral theory of $A$ is the sum of the integral theories of the subalgebras $A_i$: in the split complex case the integral is the sum of two ordinary real line integrals, the hypersurface Cauchy–Goursat theorem holds componentwise, and the curve theorem fails because the closure condition degenerates. **Zero divisors** do not obstruct the construction of primitives by integration, but they make the differential non-invertible where $f$ is a non-unit and they remove the Laurent description of singularities on the null cone, which is why residues are defined by sphere integrals. The hypercomplex line integral agrees with the **Bochner integral** of $t \mapsto f(\gamma(t))\gamma'(t)$ and so inherits the general measure-theoretic integration of algebra-valued functions; the algebra enters only through the multiplication by $\gamma'$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | Finite-dimensional unital associative real algebra, $\dim_\mathbb{R} A = m$ |
| $D$, $\bar D$ | Cauchy–Riemann operator and its conjugate |
| $\gamma$ | Piecewise $C^1$ path in $A$ |
| $\int_\gamma f\,d\xi$ | Left hypercomplex line integral; the **contour integral** when $\gamma$ is closed |
| $\int_\gamma d\xi\,f$ | Right hypercomplex line integral |
| $\ell(\gamma)$ | Euclidean length of $\gamma$ |
| $\nu_B = \sum_\alpha \nu_\alpha B_\alpha$ | Conormal element |
| $dS$ | Surface measure on a hypersurface |
| $E$ | Fundamental solution of $D$, Cauchy kernel |
| $\Phi$ | Fundamental solution of the Laplacian, $E = \bar D\Phi$ |
| $G$ | Primitive of a regular function, $dG = f\,d\xi$ |
| $\operatorname{Res}_{x_0} f$ | Residue at $x_0$, a small-sphere integral |
| $\mathcal{M}_\nu(A,D)$ | Solid spherical monogenics of degree $\nu$ |
| $\mathcal{C}h$ | Cauchy transform of a boundary datum $h$ |
| $\mathcal{C}^\pm$ | Inside and outside boundary values of the transform |
| $f\,d\xi$ | Hypercomplex differential $1$-form |
| $e_i$, $A_i = e_iA = Ae_i$ | Complete orthogonal central idempotents and the split components of $A$ |
| $e_\pm = \tfrac12(1\pm j)$, $\xi_\pm = x_0 \pm x_1$ | Idempotents and characteristic coordinates of $\mathbb{D}$ |



## Further Reading

- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the Cauchy–Goursat theorem and the Cauchy integral formula over Clifford algebras.
- R. Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for residues, spherical monogenics and the singular integral theory.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the Cauchy transform and the jump formulas.
- Walter Rudin, *Real and Complex Analysis* (McGraw–Hill, 3rd ed. 1987), for the classical Cauchy theory that the commutative case specialises to.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* (Springer, 2nd ed. 1990), for the general theory of fundamental solutions.
- John Ryan (ed.), *Clifford Algebras in Analysis and Related Topics* (CRC Press, 1996), for integral representations and their applications.
