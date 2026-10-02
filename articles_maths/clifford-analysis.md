
# __Clifford Analysis__

## Introduction

Clifford analysis is the function theory of a first-order operator built from a Clifford algebra. The variable is a vector $x = x_0 + \sum_{i=1}^{m}x_ie_i$ in a Euclidean space of dimension $m+1$, the values lie in the Clifford algebra $\mathrm{Cl}_{0,m}$ or in a Clifford module, and the operator is

$$
D = \partial_0 + \sum_{i=1}^{m}e_i\,\partial_i ,
$$

with generators satisfying $e_ie_j+e_je_i=-2\delta_{ij}$. This operator is the **Cauchy–Riemann operator** of the corpus; its classical name, the *Dirac operator*, is mentioned once here as a gloss and is carried by the family of operators treated in *Dirac Differential Operators*. The operator is elliptic, its square and the square of its conjugate are the Laplacian, and the functions it annihilates — the **monogenic** or left regular functions — form a class that generalises the holomorphic functions of one complex variable: for $m=1$ the algebra is $\mathrm{Cl}_{0,1}\cong\mathbb{C}$, the operator is the classical Cauchy–Riemann operator, and the monogenic functions are exactly the holomorphic ones.

The subject sits between two others. As a function theory over a real algebra it is an instance of the general hypercomplex analysis of *Hypercomplex Analysis* and *Regularity and the Cauchy–Riemann Operator*, and the definitions of the operator, of left and right regularity, of the symbol and of ellipticity are those articles' definitions, specialised to a Clifford algebra. As a theory of a Clifford algebra and its modules it depends on the Clifford theory of Part II: the algebra $\mathrm{Cl}_{0,m}$, its low-dimensional isomorphisms $\mathrm{Cl}_{0,1}\cong\mathbb{C}$, $\mathrm{Cl}_{0,2}\cong\mathbb{H}$, $\mathrm{Cl}_{0,3}\cong\mathbb{H}\oplus\mathbb{H}$, its spinor modules and the twisted operator on a Clifford module are all constructions of that Part, cited here and not re-derived.

What is genuinely specific to Clifford analysis, and what this article develops, is the analytic content that the Clifford structure makes available: the explicit Cauchy kernel $E(x) = \omega_m^{-1}x^{\natural}|x|^{-m-1}$, which exists because the algebra carries a conjugation and a norm; the Cauchy–Pompeiu and Cauchy integral formulas in their Clifford form; the harmonicity, mean value property, maximum principle and Liouville theorem that follow from the factorisation of the Laplacian; the Fischer decomposition of the space of polynomials into monogenic pieces; the **polymonogenic** functions, the solutions of $D^kf=0$, which are analysed by the Almansi representation; the **shifted** operator $D+\lambda$, whose square factorises the Helmholtz operator and whose theory is the Helmholtz theory in Clifford form; and the **Hermitean** refinement, in which the single operator is split into two operators over $\mathbb{C}$ and four over $\mathbb{H}$, whose simultaneous null solutions are the Hermitean monogenic functions and whose Cauchy kernels combine into a circulant matrix carrying the Hermitean integral formulae. One topic runs alongside the Cauchy theory and refines its boundary rather than its algebra: the **measure-theoretic boundary theory**, in which the boundary of the domain is required only to carry a Federer normal, or is a fractal of Hausdorff dimension strictly between $m$ and $m+1$, so that the Cauchy transform over the boundary does not exist and is replaced by the Teodorescu transform together with a Whitney extension of the datum; its Hilbert transform, its Plemelj calculus and its removable-singularity theory are the subject of a section below. The introduction states these topics and the boundaries: the per-system analyses of $\mathbb{C}$, $\mathbb{H}$ and the other number systems belong to Part V and are cited, and the construction that promotes a holomorphic function of one variable to a monogenic function of a vector variable is not covered here.

## The Clifford Setting

### The Algebra and the Module of Values

Let $V$ be a real vector space with basis $e_1,\dots,e_m$ and with the negative-definite quadratic form $q(\sum_ix_ie_i) = -\sum_ix_i^2$, and let $\mathrm{Cl}_{0,m} = \mathrm{Cl}(V,q)$ be the Clifford algebra: the quotient $T(V)/(v\otimes v - q(v)1)$. Its defining relation is

$$
uv + vu = 2q(u,v)\,1 \quad\Longleftrightarrow\quad e_ie_j+e_je_i = -2\delta_{ij} ,
$$

and the monomials $e_S = e_{i_1}\cdots e_{i_k}$, $S = \{i_1<\dots<i_k\}$, form a basis, so that $\dim_\mathbb{R}\mathrm{Cl}_{0,m} = 2^m$. The conjugation is the anti-automorphism defined by $x^{\natural} = x_0-\sum_{i=1}^{m}x_ie_i$ on a vector $x = x_0+\sum x_ie_i$ and extended by $(uv)^{\natural}=v^{\natural} u^{\natural}$; it satisfies $x x^{\natural} = x^{\natural}x = |x|^2$, where $|x|^2 = \sum_{\mu=0}^{m}x_\mu^2$ is the Euclidean norm of the ambient space $\mathbb{R}^{m+1}$. We write $A = \mathrm{Cl}_{0,m}$, identify $A$ with $\mathbb{R}^{2^m}$ through the basis, and let

$$
\mathcal{S} = \text{a Clifford module over } A ,
$$

that is, a module of the Clifford algebra as in *Clifford Modules and the Twisted Cauchy–Riemann Operator*; the scalar case $\mathcal{S} = A$ is the classical one, and the spinor case $\mathcal{S}$ an irreducible module of dimension $2^{\lfloor m/2\rfloor}$ is the case of *Spin Representations and Clifford Modules with Inner Conjugation*. The functions of the theory are the smooth functions $f : \Omega\to\mathcal{S}$ on an open set $\Omega\subseteq\mathbb{R}^{m+1}$; the operator acts on them by left multiplication of the coefficients, an operation defined because $\mathcal{S}$ is a left Clifford module.

**Remark (the ambient dimension and the corpus notation).** In the notation of *Hypercomplex Analysis* the pair $(A,D)$ is a hypercomplex system with $\dim_\mathbb{R}A = 2^m$, and the variable of this article ranges over the $(m+1)$-dimensional subspace $\mathrm{span}(1,e_1,\dots,e_m)$ of $A$ rather than over all of $A$. The defining features of the general theory — the operator assembled from the frame $(1,e_1,\dots,e_m)$, the Clifford relations, the factorisation of the Laplacian, ellipticity — are unchanged; the difference is that here the variable is a vector of the Clifford algebra rather than an arbitrary element of it, which is what makes an explicit kernel and an explicit basis of monogenics available. The number systems of Part V correspond to the low values: $m=1$ gives $\mathbb{C}$, $m=2$ gives $\mathbb{H}$, and $m=3$ gives $\mathbb{H}\oplus\mathbb{H}$.

### The Cauchy–Riemann Operator

**Definition.** The **Cauchy–Riemann operator** of Clifford analysis is

$$
D = \partial_0+\sum_{i=1}^{m}e_i\partial_i = \sum_{\mu=0}^{m}e_\mu\partial_\mu , \qquad e_0 = 1 ,
$$

and its conjugate is $\bar D = \partial_0-\sum_{i=1}^{m}e_i\partial_i$. It acts on a $C^1$ function $f : \Omega\to\mathcal{S}$ by $Df = \sum_\mu e_\mu\partial_\mu f$.

**Proposition (factorisation and ellipticity).** The identities

$$
D\bar D = \bar DD = \Delta = \sum_{\mu=0}^{m}\partial_\mu^2
$$

hold, and $D$ is elliptic: its principal symbol $\sigma(\xi) = \sum_\mu e_\mu\xi_\mu$ is a unit of $A$ for every $\xi = (\xi_0,\dots,\xi_m)\neq0$, with

$$
\sigma(\xi)^{-1} = \frac{\bar\sigma(\xi)}{|\xi|^2}, \qquad \bar\sigma(\xi) = \xi_0-\sum_{i=1}^{m}e_i\xi_i .
$$

*Proof.* The computation is the one of *Regularity and the Cauchy–Riemann Operator*: expanding $D\bar D$ gives $\partial_0^2-\sum_{i,j}e_ie_j\partial_i\partial_j$, the diagonal terms contribute $\sum_i\partial_i^2$ since $e_i^2=-1$, and the off-diagonal terms cancel pairwise by $e_ie_j=-e_je_i$. The symbol computation is identical: $\sigma(\xi)\bar\sigma(\xi) = \xi_0^2-\sum_{i,j}e_ie_j\xi_i\xi_j = \xi_0^2+\sum_i\xi_i^2 = |\xi|^2$, a positive real number, which is a unit of $A$; the same computation in the other order gives the same product, so $\sigma(\xi)$ is invertible.

The factorisation is the reason the Clifford case is the favourable one: the second-order operator that governs the theory is the ordinary Laplacian of the ambient space, so the harmonic tools of classical analysis apply to the components. The ellipticity is the reason the integral representation of the next section exists with a kernel of homogeneity $1-(m+1)$.

## Monogenic Functions

**Definition.** Let $\Omega\subseteq\mathbb{R}^{m+1}$ be open and $f : \Omega\to\mathcal{S}$ of class $C^1$. Then $f$ is **left monogenic** (or left regular) if $Df=0$ on $\Omega$, and **right monogenic** if $fD=0$, the operator acting on the right. When $\mathcal{S} = A$ is commutative, which happens only for $m=1$, the two notions coincide.

**Proposition (linear structure and one-sided multiplication).** The left monogenic functions on $\Omega$ form a real vector space, closed under right multiplication by constants of $A$; if $a\in A$ is central then $af$ is monogenic whenever $f$ is. The class is not closed under multiplication of two monogenic functions, and this is the non-commutative obstruction of *Hypercomplex Analysis* in its Clifford form.

*Proof.* Linearity of $D$ gives the vector space statement, and for a constant $a$ the Leibniz rule gives $D(fa) = \sum_\mu e_\mu(\partial_\mu f)a = (Df)a$ and $D(af) = \sum_\mu e_\mu a\partial_\mu f$, which vanishes for central $a$ because $e_\mu a = ae_\mu$. The failure of closure is exhibited by the monogenic function $x\mapsto x+ae_1$ of the next example and the monogenic function $x\mapsto x$ in the complex case; over $\mathbb{H}$ the product of two monogenic functions is in general not monogenic.

**Example (the complex case).** For $m=1$ let $z = x_0+e_1x_1$. Then $Dz = \partial_0z+e_1\partial_1z = 1+e_1^2=0$, so $z$ is left monogenic, and more generally $D(z^k)=0$ for every $k\ge0$: $\partial_0z^k = kz^{k-1}$ and $\partial_1z^k = kz^{k-1}e_1$, so $D(z^k) = kz^{k-1}+e_1kz^{k-1}e_1 = kz^{k-1}(1+e_1^2)=0$. Thus the polynomials in one complex variable are monogenic, and with $A=\mathbb{C}$ the monogenic functions are the holomorphic ones.

**Example (the vector variable is not monogenic).** For the variable $x$ itself, $Dx = \partial_0x+\sum_{i\ge1}e_i\partial_ix = 1-\sum_{i\ge1}e_i^2 = 1-m$; hence $x$ is monogenic only in the complex case $m=1$. In the Clifford case the elementary monogenic function is not $x$ but the **Cauchy kernel** of the next section, which is $x^{\natural}$ times a radial power. The computation also shows that the operator's action on polynomials records the ambient dimension, exactly as $\Delta(|x|^2)=2(m+1)$ does.

**Example (planes and the complex variable).** The functions $x\mapsto a$ (constants) and $x\mapsto z^k a$ are the elementary monogenic functions of the complex subalgebra generated by $1$ and $e_1$. The same construction works inside any subalgebra generated by $1$ and a unit vector $u$ with $u^2=-1$: the powers of $x_0+ux_1$ are monogenic. For $m\ge2$ this gives a family of monogenic functions depending on two of the $m+1$ coordinates, and it shows that the kernel of $D$ is infinite-dimensional on every nonempty open set.

**Example (monogenic functions of exponential type).** Complexifying, let $\zeta\in\mathbb{C}^{m+1}$ be isotropic, $\sum_\mu\zeta_\mu^2=0$, and let $\bar\sigma(\zeta) = \zeta_0-\sum_{i\ge1}e_i\zeta_i$. Then $x\mapsto e^{\langle\zeta,x\rangle}\bar\sigma(\zeta)$ is monogenic, as in *Regularity and the Cauchy–Riemann Operator*; the real and imaginary parts are real monogenic functions. For $m=1$ the isotropic vectors are $\zeta = \lambda(i,1)$ and the resulting family is the plane-wave family of the complex case.

**Theorem (regularity properties inherited from the Laplacian).** Every left monogenic function is real-analytic, each of its components is harmonic, and consequently:
1. (**mean value**) $f(x) = \frac{1}{\operatorname{vol}B(x,r)}\int_{B(x,r)}f(y)\,dy$ for every ball $B(x,r)\subseteq\Omega$, the average taken componentwise;
2. (**maximum principle**) if $\|f\|$ attains its maximum at an interior point of a domain $\Omega$, then $f$ is constant;
3. (**Liouville**) a monogenic function on all of $\mathbb{R}^{m+1}$ with bounded norm is constant;
4. (**identity**) two monogenic functions on a domain that agree on a set with an accumulation point agree everywhere.

*Proof.* If $Df=0$ then $\Delta f = \bar DDf = 0$, so each component of $f$ is harmonic; harmonic functions are real-analytic and satisfy the mean value property. The maximum principle follows because $\|f\|^2$ is a sum of squares of harmonic functions and hence subharmonic, and a subharmonic function attaining an interior maximum is constant; then $\Delta\|f\|^2=2\sum_\alpha|\nabla f^\alpha|^2=0$ forces the components to be constant. Liouville is the same argument applied on all of $\mathbb{R}^{m+1}$, and the identity theorem is real-analyticity on a connected set.

## The Cauchy Integral Formula

### The Cauchy Kernel

**Theorem (the kernel).** Define, for $x\neq0$,

$$
E(x) = \frac{1}{\omega_m}\frac{x^{\natural}}{|x|^{m+1}} , \qquad \omega_m = |S^m| = \frac{2\pi^{(m+1)/2}}{\Gamma\bigl(\frac{m+1}{2}\bigr)} ,
$$

the surface area of the unit sphere in $\mathbb{R}^{m+1}$. Then $E$ satisfies

$$
D E = \delta_0
$$

in the sense of distributions; consequently $E$ is a fundamental solution of $D$, and $E(x-y)$ is the **Cauchy kernel**.

*Proof.* Let $\Phi$ be the fundamental solution of the Laplacian in $\mathbb{R}^{m+1}$, normalised so that $\Delta\Phi=\delta_0$; then $D\bar D = \Delta$ gives $D(\bar D\Phi) = \delta_0$, so $E = \bar D\Phi$ is a fundamental solution, and the computation of $\bar D\Phi$ for the radially symmetric $\Phi$ produces the displayed formula. In one dimension $E(x) = \frac{1}{2\pi}\frac{x^{\natural}}{|x|^2}$, which is the classical kernel $1/(2\pi z)$; for $m=2$ the kernel is $\frac{1}{4\pi}\frac{x^{\natural}}{|x|^3}$; and in general the homogeneity is $1-(m+1)$.

**Remark (verification in the quaternionic case).** The identity $DE=0$ off the origin is readily checked by direct computation for $m=2$: with the quaternion multiplication of $\mathrm{Cl}_{0,2}\cong\mathbb{H}$ and the finite-difference approximation of $D=\partial_0+e_1\partial_1+e_2\partial_2$, the quantity $DE$ at the points $(0.3,0.4,0.5)$, $(1,-0.7,0.2)$ and $(0.11,0.22,-0.31)$ is zero to machine precision, and $Dx=-1=1-m$ at the same points, as the general formula requires.

### Cauchy–Pompeiu and Cauchy

**Theorem (Cauchy–Pompeiu).** Let $\Omega\subseteq\mathbb{R}^{m+1}$ be a bounded domain with smooth boundary, oriented by the outward normal $\nu$, and put $\nu_B = \sum_{\mu=0}^{m}\nu_\mu e_\mu$, $\nu_\mu$ the components of $\nu$. For $f$ of class $C^1$ on $\bar\Omega$ and $x\in\Omega$,

$$
f(x) = \int_{\partial\Omega}E(x-y)\,\nu_B(y)\,f(y)\,dS(y)-\int_{\Omega}E(x-y)\,(Df)(y)\,dy .
$$

*Proof.* Quoted as standard; it is the Clifford instance of the general Cauchy–Pompeiu formula of *Hypercomplex Analysis*, and it is proved by cutting the singular point out of the domain, applying the divergence theorem to the smooth part and letting the excision radius shrink, the singular integral at the boundary contributing the value $f(x)$.

**Corollary (Cauchy integral formula).** If $f$ is left monogenic on a neighbourhood of $\bar\Omega$, then

$$
f(x) = \int_{\partial\Omega}E(x-y)\,\nu_B(y)\,f(y)\,dS(y), \qquad x\in\Omega .
$$

**Corollary (Cauchy inequalities and the spherical mean).** With $B(x,r)\subseteq\Omega$,

$$
\|f(x)\|\le \frac{1}{\omega_m r^{m}}\int_{\partial B(x,r)}\|f(y)\|\,dS(y),
$$

so a monogenic function is controlled on a ball by its boundary values, and in particular $\|f(x)\|\le\sup_{\partial B(x,r)}\|f\|$.

*Proof.* Insert the Cauchy formula and estimate the integral using $\|x^{\natural}\|=|x|$ and $|E(x-y)|=\omega_m^{-1}|x-y|^{-m}$.

**Remark (the Cauchy transform and the Szegő projection).** The boundary integral defines the Cauchy transform $\mathcal{C}h(x)=\int_{\partial\Omega}E(x-y)\nu_B(y)h(y)dS(y)$, carrying a boundary datum $h$ to a function monogenic inside $\Omega$; the transform is the flat case of the general one, and the measure-theoretic version of the theory, in which the boundary is not required to be smooth, is the next section, while the general integration theory over an algebra is *Hypercomplex Integration*. The **Hardy space** $H^2(\partial\Omega)$ of boundary values of monogenic functions is a closed subspace of $L^2(\partial\Omega;\mathcal{S})$, and the Cauchy transform restricted to it is the identity, while on its orthogonal complement it vanishes: the transform is the orthogonal projection of $L^2$ onto the Hardy space, and it is self-adjoint and idempotent. This is the Clifford form of the Szegő projection of complex analysis, and it is the analytic heart of the singular-integral theory of the subject; the boundary value problem with a jump and the singular integral equation of Cauchy type that the projection and the jump formula lead to are *Riemann Boundary Value Problems and Singular Integral Equations*.

## Cauchy Transforms on Non-smooth Boundaries

The Cauchy integral formula of the previous sections is a statement about a boundary that is a hypersurface: the surface measure $dS$ must exist on $\partial\Omega$ and the outward unit conormal $\nu_B$ must be defined at every point of the integration. Neither hypothesis survives the boundary of a domain with a fractal boundary — infinite length in the plane, infinite area in space — and the object that replaces the surface measure is the $m$-dimensional Hausdorff measure $\mathcal{H}^m$ of *Geometric Measure Theory*, with a Borel normal field of Federer in place of the pointwise conormal. The replacement is exact: whenever $\mathcal{H}^m(\partial\Omega)<\infty$ the Federer normal exists and the divergence theorem holds with it, so the Cauchy transform is still defined by a boundary integral. When the boundary is rough enough that $\mathcal{H}^m(\partial\Omega)=\infty$, no such integral exists, and the Cauchy transform over the boundary is abandoned in favour of the restriction to $\Omega$ of the **Teodorescu transform**, a volume integral against the same kernel; the boundary datum is then extended off the boundary by a **Whitney extension**, and the theory remains a theory of the jump problem. This section records that measure-theoretic theory, whose sources are the survey of Abreu-Blaya and Bory-Reyes and the papers with their co-authors cited below; the complex case goes back to Kats, and the geometric input — Hausdorff measure, rectifiability, approximate tangent planes — is Federer's and is the subject of *Geometric Measure Theory*.

### The Federer Exterior Normal

**Theorem (Federer).** Let $\Omega\subseteq\mathbb{R}^{m+1}$ be a bounded domain with $\mathcal{H}^m(\partial\Omega)<\infty$. There is a Borel field $\nu_B:\mathbb{R}^{m+1}\to\mathbb{R}^{m+1}$, the **Federer exterior normal** of $\partial\Omega$, such that $\lvert\nu_B(x)\rvert=1$ at $\mathcal{H}^m$-almost every $x\in\partial\Omega$ and $\nu_B(x)=0$ elsewhere, the vector $\nu_B(x)$ is uniquely determined by $\Omega$ and $x$, and

$$
\mathcal{H}^m(\Sigma\cap\partial\Omega) = \int_\Sigma \lvert\nu_B\rvert\,d\mathcal{H}^m,
\qquad
\int_{\Omega}\operatorname{div}V\,d\mathcal{L}^{m+1} = \int_{\partial\Omega}\langle V,\nu_B\rangle\,d\mathcal{H}^m
$$

for every $\mathcal{H}^m$-measurable $\Sigma\subseteq\mathbb{R}^{m+1}$ and every $C^1$ vector field $V$ with $\int\lvert\operatorname{div}V\rvert\,d\mathcal{L}^{m+1}<\infty$; at a smooth point of $\partial\Omega$ the field $\nu_B$ is the classical exterior normal, and at a point where the density conditions

$$
\delta^{-(m+1)}\mathcal{L}^{m+1}\bigl(\{y\in\Omega:\langle y-x,\nu_B(x)\rangle>0,\ \lvert y-x\rvert<\delta\}\bigr)\to0 ,
$$

$$
\delta^{-(m+1)}\mathcal{L}^{m+1}\bigl(\{y\notin\bar\Omega:\langle y-x,\nu_B(x)\rangle<0,\ \lvert y-x\rvert<\delta\}\bigr)\to0
$$

fail to hold as $\delta\downarrow0$, the field vanishes. At such a point the boundary has no approximate tangent plane in the sense of *Geometric Measure Theory*; the pair of conditions says that the measure of the part of $\Omega$ lying beyond the hyperplane through $x$ with normal $\nu_B(x)$, and of the part of the complement lying below it, are both of lower order than a half-ball.

**Definition.** For a bounded domain $\Omega$ with $\mathcal{H}^m$-finite boundary and a function $u$ on $\partial\Omega$ with values in $\mathrm{Cl}_{0,m}$, the **Cauchy transform** and the **Hilbert transform** are

$$
\mathcal{C}u(x) = \int_{\partial\Omega}E(x-y)\,\nu_B(y)\,u(y)\,d\mathcal{H}^m(y), \qquad x\notin\partial\Omega ,
$$

$$
\mathcal{S}u(z) = \lim_{r\downarrow0}\int_{\partial\Omega\setminus\{y:\lvert y-z\rvert<r\}}E(z-y)\,\nu_B(y)\bigl(u(y)-u(z)\bigr)\,d\mathcal{H}^m(y), \qquad z\in\partial\Omega .
$$

The transform $\mathcal{C}u$ is left monogenic off $\partial\Omega$ by differentiation under the integral sign, since the kernel is monogenic in $x$ there; it is bounded at infinity and satisfies $\mathcal{C}u(\infty)=0$ in the sense that $\mathcal{C}u(x)\to0$ as $\lvert x\rvert\to\infty$, the kernel being homogeneous of degree $-(m+1)+1=-m$. The normal is the Federer field of the theorem, and the form of the measure identity is the point: the Hausdorff measure is carried by the set where the normal is defined and does not vanish, so the exceptional points contribute nothing to the integral. There are also **right-handed** versions, written $\mathcal{C}^l,\mathcal{S}^l$ and $\mathcal{C}^r,\mathcal{S}^r$, in which the kernel is multiplied on the right by the density rather than on the left; they are the operators of the right module $M^r$ below, and the passage between the two families is not a symmetry of the theory but an adjointness, as the third subsection records.

**Remark (the kernel's parity, and the two conventions).** The sources of this section write the kernel of the boundary integral as $E(y-x)$ where this article writes $E(x-y)$, as in the Cauchy–Pompeiu formula above; the two differ because the kernel is odd, $E(-z)=-E(z)$, which follows from the linearity of the Clifford conjugation and the evenness of $\lvert z\rvert$. The difference is therefore a global sign on the interior trace: with the convention of this article the Cauchy transform of the boundary value of a monogenic function reproduces the function inside $\Omega$, as the Cauchy formula requires, which is the convention used throughout below. The singular integral $\mathcal{S}$, the projectors and the algebra of the next subsection are insensitive to the choice, one sign appearing in the Cauchy transform and the opposite sign in the trace.

### Ahlfors–David Regular Surfaces and the Plemelj Formulae

**Definition.** A closed surface $\Gamma\subseteq\mathbb{R}^{m+1}$ is **Ahlfors–David regular** if there is a constant $c\ge1$ with

$$
c^{-1}r^m \le \mathcal{H}^m\bigl(\Gamma\cap\{y:\lvert y-z\rvert\le r\}\bigr) \le cr^m
$$

for every $z\in\Gamma$ and every $0<r\le\operatorname{diam}\Gamma$. The class contains the differentiable, chord-arc, piecewise smooth, Lipschitz and Liapunov surfaces, and simple Lipschitz graphs, as proper subclasses. The upper bound alone is a consequence of $\mathcal{H}^m$-rectifiability, and the content of the definition is the matching lower bound: it is the hypothesis that a surface has no holes and no thin parts at any scale, and it is exactly what makes the singular integral bounded. It is a weaker hypothesis than the *uniform rectifiability* of David and Semmes, which requires every piece of the surface to lie near a Lipschitz graph, whereas the Ahlfors–David condition is a statement about the growth of one measure only.

**Theorem (the Plemelj–Sokhotski formulae).** Let $\Gamma=\partial\Omega$ be an Ahlfors–David regular surface and let $\omega$ be a **majorant** — a non-decreasing continuous function with $\omega(0)=0$ — satisfying the doubling-type condition

$$
\int_0^\delta\frac{\omega(t)}{t}\,dt + \delta\int_\delta^{\operatorname{diam}\Gamma}\frac{\omega(t)}{t^2}\,dt \le c\,\omega(\delta), \qquad 0<\delta\le\operatorname{diam}\Gamma .
$$

For $u\in C^{0,\omega}(\Gamma)$ the following hold.

1. $\mathcal{C}u\in C^{0,\omega}(\Omega^\pm\cup\Gamma)$ with $\mathcal{C}u(\infty)=0$, where $\Omega^+=\Omega$ and $\Omega^-=\mathbb{R}^{m+1}\setminus(\Omega\cup\Gamma)$.
2. $\mathcal{C}u$ is left monogenic in $\mathbb{R}^{m+1}\setminus\Gamma$; this is the case also when the conditions of the next subsections hold, and it is always true of the transform of a function in $L^\infty$.
3. **(Cauchy's integral formula)** if $u$ is the trace on $\Gamma$ of a left monogenic $U$ in $\Omega$, then $U(x)=(\mathcal{C}u)(x)$ for $x\in\Omega$.
4. **(Plemelj–Sokhotski)** for $z\in\Gamma$, $(\mathcal{C}^\pm u)(z) = \lim_{\Omega^\pm\ni x\to z}(\mathcal{C}u)(x) = \tfrac12\bigl(\mathcal{S}u(z)\pm u(z)\bigr) \eqqcolon \pm P^\pm u(z)$.
5. $\mathcal{S}$ is bounded on $C^{0,\omega}(\Gamma)$ and $\mathcal{S}^2=I$.

*Proof.* Quoted from the literature cited below. The proof is the classical one. Near the boundary the transform is estimated by splitting the domain of integration into the ball $\lvert y-z\rvert<r$ and its complement: on the ball the singularity $\lvert x-y\rvert^{-m}$ is matched against the Hölder increment $\lvert u(y)-u(z)\rvert\le\omega(\lvert y-z\rvert)$, so that the integral becomes $\int_0^r\omega(t)\,t^{-1}dt$ against the measure of the intersection, and the two conditions on the majorant are exactly what makes this and the remaining piece comparable with $\omega(r)$; off the ball the kernel is bounded and the estimate is elementary. The Ahlfors–David lower bound is used in the estimate on the ball. The existence of the limits defining the traces is a Cauchy criterion in the Hölder norm, and the subtraction of $u(z)$ in the singular integral is what makes the principal value converge; the identity $\mathcal{S}^2=I$ is then the statement that the even part of the pair of traces is again trace-like, and it is proved by applying the formulae twice.

The general theory of the problem that these formulae solve — the linear conjugation problem $u^+=u^-B+h$, the singular integral equation of Cauchy type built on the projectors and its index — is *Riemann Boundary Value Problems and Singular Integral Equations*; the boundary is there assumed regular, and the attention is on the equation. What the present section records is the other half, the geometry of the boundary: on which surfaces the transform and its traces exist at all, which densities give continuous limit values, and which sets are removable.

**Corollary (the complementary projections).** The operators $P^\pm=\tfrac12(I\pm\mathcal{S})$ are mutually complementary projections on $C^{0,\omega}(\Gamma)$: $(P^\pm)^2=P^\pm$, $P^+P^-=0=P^-P^+$ and $P^++P^-=I$. Consequently

$$
C^{0,\omega}(\Gamma) = P^+C^{0,\omega}(\Gamma)\oplus P^-C^{0,\omega}(\Gamma),
$$

every $u\in C^{0,\omega}(\Gamma)$ has the unique decomposition $u=u^++u^-$ with $u^\pm\in P^\pm C^{0,\omega}(\Gamma)$, and $P^\pm$ are the spectral projections of the involution $\mathcal{S}$.

**Corollary (a norm in which $\mathcal{S}$ is an isometry).** For $0<\alpha\le1$ the quantity

$$
\lVert u\rVert_\star = \lVert u^+\rVert_\alpha + \lVert u^-\rVert_\alpha
$$

is a norm on $C^{0,\alpha}(\Gamma)$ equivalent to the Hölder norm, and in it $\mathcal{S}$ is a bounded operator of norm $1$: the computation of the norm of a singular integral operator in the Hölder norm is difficult even on a smooth contour, as Bernstein observed, whereas the decomposition makes the norm of $\mathcal{S}$ immediate in $\lVert\cdot\rVert_\star$, since it swaps the two summands.

**Example (the circle, and the identification of the projections).** The instance that can be computed in closed form is the unit circle, $m=1$, where the Clifford algebra is $\mathbb{C}$ and the Cauchy transform is the classical one. For the densities $u(z)=z^k$ on the circle, the transform is exact: $\mathcal{C}u(x)=x^k$ for $\lvert x\rvert<1$ and $\mathcal{C}u(x)=0$ for $\lvert x\rvert>1$ when $k\ge0$, and $\mathcal{C}u(x)=0$ for $\lvert x\rvert<1$ with $\mathcal{C}u(x)=-x^k$ for $\lvert x\rvert>1$ when $k<0$; the truncated quadrature of the transform reproduces this to $10^{-16}$, and the principal-value quadrature of $\mathcal{S}$ with the conjugate-Poisson kernel to $10^{-11}$ for $-3\le k\le3$. Hence $\mathcal{S}z^k=z^k$ for $k\ge0$ and $\mathcal{S}z^k=-z^k$ for $k<0$: the involution is the sign of the frequency, $P^+$ is the projection onto the non-negative frequencies, and $P^-$ onto the negative ones, which is the classical identification through the Hilbert transform of Fourier analysis. Comparing with the remark of the previous section, the projection $P^+$ is the Szegő projection $\mathcal{C}$ there, and the relation between the two operators is $\mathcal{S}=2\mathcal{C}-I$ on boundary data; the decomposition $u=u^++u^-$ is the Hardy decomposition of the boundary datum.

### The Spaces $M^l$ and $M^r$, and the Compactness of the Embedding

**Definition.** Let $\Gamma$ be a bounded Ahlfors–David regular surface. Let $M^l(\Gamma)$ be the real linear space of continuous functions $u$ on $\Gamma$ for which the truncated integral

$$
\int_{\Gamma\setminus\{y:\lvert y-z\rvert<\varepsilon\}}E(z-y)\nu_B(y)\bigl(u(y)-u(z)\bigr)d\mathcal{H}^m(y)
$$

converges uniformly in $z$ as $\varepsilon\downarrow0$, and let $M^r(\Gamma)$ be the space defined by the corresponding integral with the kernel on the right. Each of the two spaces inherits from $\mathcal{C}$ and $\mathcal{S}$ the splitting $M^\bullet = P^\bullet_+M^\bullet\oplus P^\bullet_-M^\bullet$ and carries the norm

$$
\lVert u\rVert_l = \bigl\lVert P^+_lu\bigr\rVert_{C(\Gamma)} + \bigl\lVert P^-_lu\bigr\rVert_{C(\Gamma)} ,
$$

and with it becomes a real Banach space. The definitions are organised so that the Hölder classes sit inside them.

**Theorem (the continuous and compact embedding).** The space $C^{0,\alpha}(\Gamma)$, $0<\alpha\le1$, is continuously embedded in each of $M^l(\Gamma)$ and $M^r(\Gamma)$, and the embedding operator is compact.

*Proof.* Quoted from the literature. Continuous embedding is the uniform convergence of the truncated singular integral for a Hölder density, which is Theorem 3 in the form stated in the next subsection; compactness is proved by the Arzelà–Ascoli criterion, which the splitting makes available: a set $E\subseteq M^l$ is relatively compact exactly when $E$ is bounded in $M^l$ and the two projected sets $P^\pm_lE$ are equicontinuous, so that the failure of compactness can be read off the two families of traces separately.

**Theorem (Zygmund-type estimates for the commutators, and their compactness).** Let $a\in C(\Gamma)$ satisfy $\int_0^{\operatorname{diam}\Gamma}\omega_a(t)\,dt/t<\infty$, where $\omega_a$ is the modulus of continuity of $a$, and let $[M_a,\mathcal{S}^l]=M_a\mathcal{S}^l-\mathcal{S}^lM_a$ and $[aM,\mathcal{S}^r]=aM\mathcal{S}^r-\mathcal{S}^raM$ be the commutators of the singular operator with the operators of right and left multiplication by $a$. Then for $u\in M^l$

$$
\omega_{[M_a,\mathcal{S}^l]u}(\delta) \le c\lVert u\rVert_l\left(\int_0^\delta\frac{\omega_a(t)}{t}\,dt + \delta\int_\delta^{\operatorname{diam}\Gamma}\frac{\omega_a(t)}{t^2}\,dt\right),
$$

with the corresponding estimate for $[aM,\mathcal{S}^r]$ and $\lVert u\rVert_r$. Consequently, for $a\in C^{0,\alpha}(\Gamma)$ the commutator is a continuous operator from $M^l$ into $C^{0,\alpha}$, and for $0<\alpha<1$ the two commutators are compact operators from $C^{0,\beta}(\Gamma)$, $0<\beta\le1$, into $C^{0,\alpha}(\Gamma)$.

*Proof.* Quoted from the literature. The estimates are of Zygmund type: the modulus of continuity of the commutator is controlled by the integral means of $\omega_a$, the same two integral conditions on the majorant that appear in the theorem on the Plemelj formulae, and they are what makes the operator gain the Hölder exponent. The compactness is then a consequence of the compact embedding of the previous theorem and of the fact that the commutator with a Hölder function improves the scale; for Liapunov surfaces in quaternionic analysis the compactness was proved by the earlier pair of authors cited below, and the estimates above extend the statement to the Ahlfors–David regular setting.

**Theorem (adjointness).** The left and right operators are adjoint to one another, not symmetric. In the right Hilbert module $L^2(\Gamma;\mathcal{S})$ with inner product $\langle u,v\rangle=\int_\Gamma uv^{\natural}\,d\mathcal{H}^m$ one has

$$
(\mathcal{S}^l)^\dagger = \nu_{B}M\,\mathcal{S}^l\,\nu_{B}M ,
$$

the operator of multiplication by the normal on both sides; in the flat case $\Gamma=\mathbb{R}^m$ with $\nu_B=e_{m+1}$ this gives $(\mathcal{S}^l)^\dagger=\mathcal{S}^l$, so that the projections $P^\pm_l$ are orthogonal on $L^2(\mathbb{R}^m)$. On a general surface the formula does not settle the duality, and the relevant adjointness is the relative one with respect to the **total subspace** of real functionals of the form $u\mapsto\int_\Gamma\varphi\,\nu_B\,u\,d\mathcal{H}^m$ with $\varphi\in C^{0,\alpha}(\Gamma)$, which is total in the dual of $C^{0,\alpha}(\Gamma)$: with respect to that subspace the adjoints of $\mathcal{S}^l$ and $P^\pm_l$ are $\mathcal{S}^r$ and $P^\pm_r$.

*Proof.* Quoted from the literature. The metric formula is a computation with the parity of the kernel and the symmetry of the normal; the relative adjointness is the general fact that $P^+_l$ and $P^-_l$ split the space and the right-handed operators split the dual pairing in the complementary way, which is the statement that the left and right function theories are dual to each other rather than identical.

### Removable Singularities

**Theorem (Dolzhenko; and the Clifford form).** Let $F\subseteq\Omega$ be closed and let $u$ be continuous on $\Omega$ and left monogenic on $\Omega\setminus F$. If the **inner** Hausdorff measure of $F$ with respect to the measure function $h(r)=r^m\omega(u,r)$ vanishes, $H_h(F)=0$, where $\omega(u,r)$ is the modulus of continuity of $u$ on $\Omega$, then $u$ is monogenic on $\Omega$. In the plane, $m=1$, this is Dolzhenko's theorem, which states that a function holomorphic off a set of vanishing inner measure with respect to $h(r)=r\omega(f,r)$ is holomorphic on the whole domain; in particular $F$ is removable for $C^{0,\alpha}(\Omega)$, $0<\alpha<1$, exactly when $\mathcal{H}^{1+\alpha}(F)=0$, and the case $\alpha=1$ is Nguyen's theorem.

*Proof.* Quoted from the literature. The proof is by the integral representation of a monogenic function on a domain with a slit: one applies the Cauchy formula to the function cut off near $F$ and estimates the resulting volume integral with the modulus of continuity and the vanishing measure, the estimate being uniform in the cutting parameter, and one concludes that the equation $Du=0$ holds across $F$.

**Corollary (Painlevé's theorem).** If $\mathcal{H}^m(F)<\infty$, if $u$ is left monogenic on $\Omega\setminus F$ and continuous on $\Omega$, then $u$ is monogenic on $\Omega$. Thus a closed set of finite $m$-dimensional Hausdorff measure is removable for continuous monogenic functions, exactly as a set of finite length is removable for continuous holomorphic functions in the plane; the hypothesis $\mathcal{H}^m(F)<\infty$ is the measure-theoretic form of the classical condition on a curve, and it is strictly weaker than rectifiability.

**Corollary (the Hölder classes).** If $\mathcal{H}^{m+\alpha}(F)=0$ for some $0<\alpha\le1$, then every $u\in C^{0,\alpha}(\Omega)$ left monogenic on $\Omega\setminus F$ is monogenic on $\Omega$. In particular a set of vanishing $\mathcal{H}^{m+\alpha}$ measure of the appropriate dimension is invisible to the functions of class $C^{0,\alpha}$, and the scale $m+\alpha$ interpolates between the two extreme corollaries: at $\alpha\to0$ the condition approaches finiteness of $\mathcal{H}^m$, at $\alpha=1$ it is the vanishing of $\mathcal{H}^{m+1}(F)$, which is the Lebesgue measure of $F$.

**Remark (the consequences for bounded functions).** Combined with Liouville's theorem, the theorem above shows that if $\omega$ is a non-negative non-decreasing function with $H_h(F)=0$ for $h(r)=r^m\omega(r)$, then the class of functions monogenic on $\mathbb{R}^{m+1}\setminus F$, continuous on $\mathbb{R}^{m+1}$ and with modulus of continuity dominated by $\omega$ consists of the constants alone. This is the quantitative form of the statement that a singularity removable by a Lipschitz-type condition cannot support a non-constant bounded solution, and it is the reason the removable-set theory and the Liouville theory of the first sections are used together. The analogous problem for quaternionic monogenic functions of **Zygmund class** — a modulus of continuity slightly above Lipschitz — was treated separately by the authors of the survey.

### The Jump Problem on $\mathcal{H}^m$-Finite Surfaces

Let $\Omega$ be a bounded Jordan domain and $\Gamma=\partial\Omega$. Two questions organise the boundary-value theory.

**Question I.** Under which conditions on $\Gamma$ and on $v$ is $\mathcal{C}v$ continuous on $\Omega^\pm\cup\Gamma$, that is, does the Cauchy transform of the density have continuous limit values?

**Question II.** Under which conditions on $\Gamma$ and $v$ is there a monogenic function $u$ on $\mathbb{R}^{m+1}\setminus\Gamma$ with prescribed jump $u^+-u^-=v$ on $\Gamma$ and $u(\infty)=0$?

The two are the same question when the answer to the first is yes, since $\mathcal{C}v$ is monogenic off $\Gamma$ by construction and has $\mathcal{C}v(\infty)=0$; the reconstruction then reads $u=\mathcal{C}v$, and it is unique by Painlevé's theorem and Liouville's theorem. In the smooth case both are answered by the Plemelj formulae of the second section. The results below answer them on boundaries of decreasing regularity: the questions are about the boundary and not about the equation, the equation with a coefficient being *Riemann Boundary Value Problems and Singular Integral Equations*.

**Theorem (Ahlfors–David regular surfaces).** Let $\Gamma$ be rectifiable and Ahlfors–David regular and let $v\in C(\Gamma)$. Then $\mathcal{C}v\in C(\Omega^\pm\cup\Gamma)$ if and only if the truncated integral

$$
\int_{\Gamma\setminus\{y:\lvert y-z\rvert<\varepsilon\}}E(z-y)\nu_B(y)\bigl(v(y)-v(z)\bigr)d\mathcal{H}^m(y)
$$

converges uniformly on $\Gamma$ as $\varepsilon\downarrow0$. The statement remains valid when $\Gamma$ is the union of an $\mathcal{H}^m$-null set and countably many Lipschitz images of subsets of $\mathbb{R}^m$, that is when $\Gamma$ is $\mathcal{H}^m$-rectifiable; the additional Ahlfors–David hypothesis serves only to ensure that the approximate tangent planes of the rectifiable set are genuine tangents at every point. The conjunction of rectifiability and Ahlfors–David regularity is strictly wider, in codimension one, than the uniform rectifiability of David and Semmes, the latter being the class for which the whole Calderón–Zygmund theory of singular integrals is available; the $L^2$-boundedness of the Clifford Cauchy transform on the standard rectifiable surfaces is due to Murray for Lipschitz graphs with small constant and to McIntosh in general, and it is what allows the scalar part — the double-layer potential — to be used for the Dirichlet and Neumann problems of a domain with Lipschitz boundary.

**Theorem (the higher-dimensional Davydov theorem).** Let $\Omega$ have $\mathcal{H}^m$-finite boundary and let $v\in C(\Gamma)$. If the limit

$$
\lim_{\varepsilon\downarrow0}\int_{\Gamma\setminus\{y:\lvert y-z\rvert<\varepsilon\}}\frac{\lvert v(y)-v(z)\rvert}{\lvert y-z\rvert^m}\,d\mathcal{H}^m(y)
$$

exists uniformly on $\Gamma$, then $\mathcal{C}v\in C(\Omega^\pm\cup\Gamma)$. This is the form of the answer to Question I that does not assume rectifiability or the Ahlfors–David lower bound, only the finiteness of the boundary measure; it is the $m$-dimensional analogue of Davydov's theorem in the plane, and it is the form used below when the boundary is a fractal of infinite measure.

**Theorem (the lower density condition, and the two majorant criteria).** Assume

$$
\mathcal{H}^m\bigl(\Gamma\cap\{y:\lvert y-z\rvert\le r\}\bigr)\ge cr^m , \qquad z\in\Gamma,\ 0<r\le\operatorname{diam}\Gamma ,
$$

a lower bound that is automatic for curves and for one-dimensional compact connected sets, and that carries no hypothesis of rectifiability. (i) If $\omega(t)/t$ is non-increasing and $\int_0^1\omega(t)\,t^{-(2m-1)/m}\,dt<\infty$, then $\mathcal{C}v\in C(\Omega^\pm\cup\Gamma)$ for every $v\in C^{0,\omega}(\Gamma)$. (ii) If $\omega(t)/t$ is non-increasing and $\omega(t)/t^{m/(m+1)}$ is non-decreasing, then $\mathcal{C}v\in C(\Omega^\pm\cup\Gamma)$ for every $v\in C^{0,\omega}(\Gamma)$ if and only if

$$
\int_0^1\omega^{\frac{m+1}{m}}(t)\,\frac{dt}{t^2}<\infty .
$$

Under either hypothesis the jump problem is solved by $u=\mathcal{C}v$, and the solution is unique by Painlevé's theorem and Liouville's theorem. A surface satisfying the lower bound, or merely rectifiable, has $\overline{\dim}_M\Gamma=\dim_H\Gamma=m$, so that these are results about boundaries of dimension $m$ and finite measure, not about fractal boundaries proper.

*Proof.* Quoted from the literature. The criterion (ii) is a two-sided one: the sufficiency is again the split estimate, and the necessity is proved by exhibiting, for a majorant that violates the integral condition, a surface satisfying the lower bound and a density of the class for which the truncated integral fails to converge uniformly.

**Theorem (the Hölder form).** Suppose $\alpha>m/(m+1)$ and let $v\in C^{0,\alpha}(\Gamma)$. Then $\mathcal{C}v\in C(\Omega^\pm\cup\Gamma)$ for every surface satisfying the lower density condition above, or merely rectifiable. The threshold $m/(m+1)$ is a genuine one, and it is the same threshold that reappears in the fractal case as $d/(m+1)$; the reason a scale strictly between $0$ and $1$ appears is that the estimate of the Cauchy transform near the boundary is not a two-piece estimate with comparable exponents, but one in which the $m$-dimensional measure of a ball and the vanishing of the density's increment compete with different weights.

**Theorem (the refinement for $\mathcal{H}^m$-finite surfaces).** Let $\dim_M\Gamma=m$ with $\mathcal{H}^m(\Gamma)<\infty$, and let the Hölder exponent satisfy $m/(m+1)<\alpha<1$. Then $\mathcal{C}v$ has continuous limit values on $\Gamma$ for every $v\in C^{0,\alpha}(\Gamma)$. The hypothesis of the previous theorem, the lower density bound, is not assumed: finiteness of the boundary measure and the value $m$ of the dimension are enough. A further refinement replaces the Hölder class by a class $C^{0,\omega}$ whose majorant satisfies one more monotonicity condition, of the form "$\omega(t)/t^{1-1/p}$ is non-decreasing for some $p>m+1$", and concludes the same extension for every density of that class.

### The Weighted Cauchy Transform on $\omega$-Regular Surfaces

Both hypotheses of the preceding subsections are bounds on the plain $m$-dimensional Hausdorff measure of the boundary: the Ahlfors–David condition is a two-sided bound and the finiteness of $\mathcal{H}^m(\Gamma)$ is the weaker one-sided statement, and under either the Cauchy transform is an integral against the unweighted measure. There is one hypothesis between them, in which the measure is weighted and the boundary integral exists for a class of surfaces strictly larger than the Ahlfors–David class. This subsection records that rung of the scale; it is the one layer of the measure-theoretic theory that is not a variant of the layers already written.

**Definition ($\omega$-regular and $|F|$-regular surfaces).** Let $\omega\ge0$ be a function on $\Gamma$, and let $\mathcal{H}^m_\omega$ be the Hausdorff measure taken with the weight $\omega$. The surface $\Gamma$ is **$\omega$-regular** if there is a constant $c_\omega$ with

$$
\mathcal{H}^m_\omega\bigl(\Gamma\cap\{y:\lvert y-z\rvert\le r\}\bigr)\le c_\omega r^m , \qquad z\in\Gamma,\ 0<r\le\operatorname{diam}\Gamma ,
$$

the upper half of the Ahlfors–David condition read with the weighted measure; only the upper bound is imposed. When the weight is the modulus $\lvert F\rvert$ of a continuous $\mathrm{Cl}_{0,m}$-valued function $F$ on $\Omega\cup\Gamma$ that is monogenic in $\Omega$, the surface is called **$\lvert F\rvert$-regular**. The class of weight functions is wide enough to contain examples of interest: a domain of $\mathbb{R}^3$ has been constructed whose boundary is *not* Ahlfors–David regular and is nevertheless $\lvert F\rvert$-regular with an $F$ of this kind.

**Proposition (the comparison with Ahlfors–David).** An Ahlfors–David regular surface is $\omega$-regular for every weight that does not vanish identically on $\Gamma$, with $c_\omega=\max_\Gamma\omega/c$ if $c_\omega$ and $c$ are the constants of the two conditions. The converse fails, since only the upper bound is imposed and the weighted measure may be concentrated on thin parts of the boundary where the plain measure is small: an $\lvert F\rvert$-regular surface need not satisfy the lower density bound of the Ahlfors–David condition, and the weighted theory is therefore not a restatement of it.

*Proof.* The first statement is the domination of the weighted measure by a multiple of the unweighted one, with the maximum of the weight as the constant. The second is the cited example, in which the lower density bound fails along a sequence of scales while the weighted upper bound holds.

**Definition (the weighted Cauchy transform and its singular operator).** For a boundary datum $u$ with values in $\mathrm{Cl}_{0,m}$ and a weight $F$, the **weighted Cauchy transform** and the **weighted singular integral** are

$$
\mathcal{C}_F u(x) = \int_\Gamma E(x-y)\,\nu_B(y)\,F(y)\,u(y)\,d\mathcal{H}^m(y), \qquad x\notin\Gamma ,
$$

$$
\mathcal{S}_F u(z) = \lim_{\varepsilon\downarrow0}\int_{\Gamma\setminus\{y:\lvert y-z\rvert<\varepsilon\}}E(z-y)\,\nu_B(y)\,F(y)\bigl(u(y)-u(z)\bigr)\,d\mathcal{H}^m(y) , \qquad z\in\Gamma ,
$$

with the same kernels as in the unweighted case and the weight inserted between the normal and the density. The transform $\mathcal{C}_F u$ is left monogenic off $\Gamma$ by differentiation under the integral sign, and it vanishes at infinity for the same reason as $\mathcal{C}$.

**Theorem (boundedness of the weighted singular operator).** If $\Gamma$ is $\lvert F\rvert$-regular, then $\mathcal{S}_F$ is a bounded operator from the generalised Hölder class $C^{0,\omega}(\Gamma)$ into itself.

*Proof.* Quoted from the literature. The estimate is the split estimate of the Plemelj theorem with the weighted measure in place of the plain one, the weight entering the constant and not the exponent.

**Theorem (the weighted Plemelj formulae).** Let $\Gamma$ be rectifiable and $\lvert F\rvert$-regular, and let $u$ be continuous on $\Gamma$ with values in $\mathrm{Cl}_{0,m}$. Then the following two conditions are equivalent.

1. $\mathcal{C}_F u$ has continuous limit values $(\mathcal{C}_F u)^\pm$ on $\Gamma$, given by the weighted Plemelj formula
    $$
    (\mathcal{C}_F u)^\pm = \tfrac12\bigl(\mathcal{S}_F u \pm F u\bigr) .
    $$
2. The truncated integrals converge uniformly on $\Gamma$: $\mathcal{S}^\varepsilon_F u\to\mathcal{S}_F u$ in the supremum norm as $\varepsilon\downarrow0$.

*Proof.* Quoted from the literature. The theorem is the weighted counterpart of the Plemelj–Sokhotski theorem of the Ahlfors–David subsection, and as a criterion it is genuinely stronger: there the existence of the limit values was concluded from a majorant condition on the modulus of continuity, whereas here the existence of the limit values is *equivalent* to the uniform convergence of the truncated integral, no majorant condition being assumed. For $F=1$ the weight is the constant weight and the formula reduces to the unweighted one of that subsection; a surface satisfying both density bounds is covered by both statements, and the weighted theorem extends the calculus to the $\lvert F\rvert$-regular surfaces on which the lower bound fails.

**Remark (where the layer sits).** The weighted theory is the rung between the Ahlfors–David subsection and the fractal transform. On an Ahlfors–David regular surface the boundary integral exists unweighted and the full Plemelj calculus holds; on an $\lvert F\rvert$-regular surface that is not Ahlfors–David the integral exists only with the weight $\lvert F\rvert$, and the calculus survives with $F$ in the boundary term of the Plemelj formula; on a $d$-summable fractal boundary neither the boundary measure nor the singular integral is available, and the transform is rebuilt from the Teodorescu transform and a Whitney extension. The weight is the price of the boundary's failing the lower density bound while retaining, after weighting, enough of it for the singular operator to be bounded.

### $d$-Summable Boundaries and the Fractal Cauchy Transform

**Definition (Minkowski dimension).** For a compact set $E\subseteq\mathbb{R}^{m+1}$ let $N_E(t)$ be the least number of balls of radius $t$ needed to cover $E$ — equivalently, the number of dyadic cubes of side $2^k$ with $2^k\le t<2^{k+1}$ meeting $E$ — and let

$$
\overline{\dim}_M E = \limsup_{t\downarrow0}\frac{\log N_E(t)}{\log(1/t)}
$$

be the **upper Minkowski dimension**, the upper box-counting dimension of *Fractal Geometry*. The Minkowski and Hausdorff dimensions agree for rectifiable surfaces and for self-similar sets satisfying the open set condition, and in general $\dim_{top}E\le\dim_HE\le\overline{\dim}_ME$ with both inequalities strict for a set that is fractal in the sense of Mandelbrot. A set of topological dimension $m$ that one wants to use as a boundary but that has $\overline{\dim}_ME>m$ has infinite $\mathcal{H}^m$ measure, and it is then that the Cauchy transform of the boundary has to be abandoned.

**Definition ($d$-summability).** Let $d>0$. A set $E$ is **$d$-summable** if the improper integral

$$
\int_0^\delta N_E(t)\,t^{d-1}\,dt
$$

converges for some $\delta>0$. The notion is due to Harrison and Norton, and it is the condition under which a differential form can be integrated over a fractal boundary.

**Lemma.** (i) A $d$-summable set $E$ has $\overline{\dim}_ME\le d$; (ii) conversely, if $\overline{\dim}_ME<d$ then $E$ is $d$-summable; (iii) if $E$ is $d$-summable it is $(d+\varepsilon)$-summable for every $\varepsilon>0$.

*Proof.* (i) Suppose $\overline{\dim}_ME=s>d$. Then along a sequence $t_k\downarrow0$ one has $N_E(t_k)\ge t_k^{-s}$, and since $N_E$ is non-increasing, $N_E(t)\ge N_E(t_k)\ge t_k^{-s}$ for $t\le t_k$; hence

$$
\int_0^{t_k}N_E(t)\,t^{d-1}dt \ge t_k^{-s}\int_0^{t_k}t^{d-1}dt = \frac{t_k^{d-s}}{d}\to\infty ,
$$

the growth being the power $t_k^{d-s}$, so the integral diverges and $E$ is not $d$-summable. (ii) If $\overline{\dim}_ME=s<d$, choose $d'$ with $s<d'<d$; then $N_E(t)\le Ct^{-d'}$ for small $t$, and $\int_0^\delta t^{d-1-d'}dt<\infty$ because $d-1-d'>-1$. (iii) $\int_0^\delta N_E(t)t^{d+\varepsilon-1}dt\le\delta^\varepsilon\int_0^\delta N_E(t)t^{d-1}dt<\infty$. $\square$

**Remark (the lemma on explicit sets).** The three statements were recomputed on the standard self-similar sets, for which the covering numbers are exact on the natural grid: $N(3^{-k})=2^k$ for the middle-thirds Cantor set, $N(3^{-k})=4^k$ for the Koch curve, and $N(2^{-k})=3^k$ for the Sierpiński triangle, with similarity dimensions $\log2/\log3=0.6309\ldots$, $\log4/\log3=1.2619\ldots$ and $\log3/\log2=1.5850\ldots$. The tail $\int_0^{t_K}N_E(t)t^{d-1}dt$ converges for $d$ above the similarity dimension and diverges below it, the divergent tail growing like $t_K^{d-D}$ as the estimate in the proof of (i) predicts, and the integrals for $d$ and for $d+\varepsilon$ satisfy the inequality of (iii); the dichotomy is exactly the one the lemma asserts.

**Definition (the fractal Cauchy transform).** Let $d\in(m,m+1)$, let $\Omega$ be a Jordan domain with $d$-summable boundary $\Gamma$, and let $\omega$ be a majorant such that $\omega(t)/t$ is non-increasing and $\omega(t)/t^{d-m}$ is non-decreasing. For $u\in C^{0,\omega}(\Gamma)$ let $\tilde u$ be a **Whitney extension** of $u$, continuous on $\mathbb{R}^{m+1}$ with the same modulus of continuity. The **fractal Cauchy transform** of $u$ is

$$
\mathcal{C}_\Gamma u(x) = \chi_\Omega(x)\,\tilde u(x) + \int_{\mathbb{R}^{m+1}}E(x-y)\,\partial_y\tilde u(y)\,d\mathcal{L}^{m+1}(y), \qquad x\in\mathbb{R}^{m+1}\setminus\Gamma ,
$$

in which $\chi_\Omega$ is the characteristic function of the domain and $\partial_y\tilde u$ is the Cauchy–Riemann derivative of the extension, which is the density the volume integral integrates against. Both terms are left monogenic in $x$ off $\Gamma$, and $\mathcal{C}_\Gamma u$ vanishes at infinity, the kernel being homogeneous of degree $-m$. The transform is built so that it reduces to the Cauchy transform of the previous subsection when the boundary is regular enough for the boundary integral to exist — on an Ahlfors–David regular surface, for instance — the characteristic term being the Cauchy–Pompeiu boundary term and the volume integral the **Teodorescu transform** $\mathcal{T}u(x)=\int_\Omega E(x-y)u(y)\,d\mathcal{L}^{m+1}(y)$, the Green-type inverse of the Cauchy–Riemann operator on the domain; the sources write that kernel as $E(y-x)$ and their sign accordingly. The construction goes back to Kats, whose method for Riemann boundary-value problems of analytic functions in the plane is the model; the role of the Whitney extension is to make the density defined off the boundary, which is the price of the boundary's having no measure to integrate against.

**Remark (why the transform is the right object).** The identity $\mathcal{S}=2\mathcal{C}-I$ on boundary data, or equivalently $2(\mathcal{C}u)^+-u(z)=\mathcal{S}u(z)$, is a formal consequence of the Plemelj formula and holds whether or not the boundary is smooth. The transform $\mathcal{C}_\Gamma$ provides a continuous trace $(\mathcal{C}_\Gamma u)^+$ on a fractal boundary, and it therefore provides a definition of the Hilbert transform

$$
\mathcal{S}_\Gamma u(z) = 2(\mathcal{C}_\Gamma u)^+(z) - u(z), \qquad z\in\Gamma ,
$$

in the case in which the singular integral defining $\mathcal{S}$ does not converge at all. This is the whole point of the construction: the singular integral is replaced by a volume integral with a Whitney extension, and the boundary operator is recovered from the trace of a function that does exist.

**Theorem (the extension on a $d$-summable boundary).** Let $\Gamma$ be $d$-summable with $d\in(m,m+1)$ and let $\alpha>d/(m+1)$. Then for every $u\in C^{0,\alpha}(\Gamma)$ the transform $\mathcal{C}_\Gamma u$ has a continuous extension to $\overline{\Omega}$, and $\mathcal{S}_\Gamma u\in C^{0,\beta}(\Gamma)$ for every

$$
\beta<\frac{(m+1)\alpha-d}{m+1-d} .
$$

*Proof.* Quoted from the literature. $\square$

**Remark (the exponent bookkeeping).** The two hypotheses of the theorem are the natural ones, as the arithmetic shows: since $d<m+1$ the denominator $m+1-d$ is strictly positive, so the bound on $\beta$ has positive numerator — that is, $\beta>0$ is available — exactly when $(m+1)\alpha>d$, which is the condition $\alpha>d/(m+1)$ of the theorem; and the numerator is less than the denominator exactly when $\alpha<1$, so that for the classes $C^{0,\alpha}$ with $\alpha<1$ the exponent $\beta$ is automatically less than $1$. The theorem therefore gains a Hölder exponent for the Hilbert transform from the Hölder exponent of the density, the gain being the ratio of the two gaps $(m+1)\alpha-d$ and $m+1-d$; and at $\alpha=1$ the bound on $\beta$ tends to $1$ and the statement degenerates to the continuity already asserted.

**Theorem (the sharpness of the threshold).** For every $d\in(m,m+1)$ and every Hölder exponent below the threshold $d/(m+1)$ there are a $d$-summable curve $\Gamma=\partial\Omega$ and a function $u$ on it, Hölder with that exponent, whose Cauchy transform has no continuous extension to $\overline{\Omega}$. In the plane, where the boundary is a curve and $m=1$, the theorem asserts that for any pair with $0<\alpha<d/2$ such a curve and such a density exist, so that the condition $\alpha>d/(m+1)$ of the preceding theorem cannot be relaxed within the class of $d$-summable boundaries.

*Proof.* Quoted from the literature. It is worth recording that the counterexample cannot be the classical curve of Kats, since that curve is not $d$-summable for $d$ its own Minkowski dimension: the sharpness statement requires a curve that *does* satisfy the summability hypothesis and *still* defeats the transform, which is a strictly stronger demand. $\square$

**Remark (the fractal Hilbert transform as an independent object).** The definition of $\mathcal{S}_\Gamma$ by the trace of $\mathcal{C}_\Gamma$ is not merely a substitute for the singular integral: on a $d$-summable boundary the analogue of the boundedness of $\mathcal{S}$ is a statement about $\mathcal{S}_\Gamma$ — the preceding theorem is exactly such a statement — while the classical operator $\mathcal{S}$ of the second section is not defined. The two agree whenever both are defined, by the identity above, and the family of surfaces on which the second is unavailable and the first is not is precisely the family of boundaries with $\mathcal{H}^m$ infinite and finite $d$-summability.

### The Approximate Dimension

**Definition (decompositions and $q$-mass).** An **inner decomposition** of the domain $\Omega$ is a sequence $\mathcal{P}^+=\{P_k\}_{k\ge1}$ of non-overlapping polygonal domains with $P_k\subseteq\Omega$ and $\bigcup_{k\ge1}P_k=\Omega$, such that every compact subset of $\Omega$ meets finitely many of the $P_k$ and $P_{k+1}$ has a side in common with $\bigcup_{j\le k}P_j$; the polygons $\Gamma^+_k=\partial\bigl(\bigcup_{j\le k}P_j\bigr)$ then converge to $\Gamma$ in the Hausdorff metric, from inside. An **outer decomposition** of the exterior is defined in the same way with $P_0$ containing the point at infinity, and gives polygons $\Gamma^-_k$ converging to $\Gamma$ from outside. For a polygonal domain $P$ write $p(P)=\mathcal{H}^m(\partial P)$ for its **perimeter** and $w(P)$ for the diameter of the largest ball contained in $P$, its **inner width**, and put

$$
M_q(\mathcal{P}^+) = \sum_{k\ge1}p(P_k)\,w^{q-m}(P_k) ,
$$

the **(refined) $q$-mass** of the decomposition. The definitions are calibrated for decompositions whose pieces accumulate on $\Gamma$; a decomposition into finitely many pieces has finite mass for every $q$ and carries no information about the boundary.

**Definition (the approximate dimension).** Let $N^+(\Gamma)$ be the set of $q$ for which some inner decomposition has finite $q$-mass and let $\dim^+_a\Gamma=\inf N^+(\Gamma)$ be the **inner approximate dimension**; let $\dim^-_a\Gamma$ be defined by the outer decompositions; the **approximate dimension** of $\Gamma$ is $\dim_a\Gamma=\min\{\dim^+_a\Gamma,\dim^-_a\Gamma\}$.

**Proposition.** If $\Gamma$ is $d$-summable, then $\dim_a\Gamma\le d$.

*Proof sketch.* One takes the decomposition of $\Omega$ into polygonal pieces carried by the dyadic cubes of a covering of the surface, each piece having perimeter at most a constant multiple of the $m$-content of the surface it carries and inner width comparable with the sidelength of the cube. The mass of a piece is then bounded by the $d$-th power of the sidelength of its cube, so that the total $d$-mass is comparable with the sum $\sum_Q\lvert Q\rvert^d$ over the dyadic cubes meeting $\Gamma$, which is exactly the sum appearing in the definition of $d$-summability through its encoding as the convergence of $\int N_\Gamma(t)t^{d-1}dt$; that sum is finite, so $d\in N^+(\Gamma)$ and $\dim^+_a\Gamma\le d$. The same argument with the outer decomposition gives $\dim^-_a\Gamma\le d$, and $\dim_a\Gamma=\min\{\dim^\pm_a\Gamma\}\le d$. $\square$

**Proposition (the improvement is strict).** For every $d\in(m,m+1)$ there is a $d$-summable surface $\Gamma$ with $\dim_a\Gamma<d$. Consequently the approximate dimension is a strictly finer invariant of a fractal boundary than the Minkowski dimension, and it is the invariant that should enter the solvability condition.

**Theorem (the jump problem in terms of the approximate dimension).** For every $v\in C^{0,\alpha}(\Gamma)$ the jump problem $u^+-u^-=v$ on $\Gamma$ has a solution whenever

$$
\alpha>\frac{\dim_a\Gamma}{m+1} .
$$

*Proof.* Quoted from the literature. The statement is the sharpening of the theorem of the previous subsection: since $\dim_a\Gamma\le\overline{\dim}_M\Gamma=d$ on a $d$-summable boundary, and since the inequality can be strict by the proposition above, the condition on $\alpha$ is weaker than $\alpha>d/(m+1)$ on a class of surfaces on which the earlier criterion is not optimal; the proof replaces the covering-number estimate by the two-sided polygonal decomposition, which measures the perimeter of the boundary against the widths of the pieces and therefore sees the cancellations that the covering number alone does not. $\square$

**Remark (the place of the theory in this article).** What has been added here is a boundary theory, not a new class of functions: the monogenic functions, the Cauchy kernel and the integral formulae are those of the previous sections, and the boundary of the domain is allowed to be a set of Hausdorff dimension strictly between $m$ and $m+1$. The layers of hypotheses are worth keeping apart. With $\mathcal{H}^m(\Gamma)<\infty$ the Federer normal exists, the boundary integral is defined, and the theory is the classical one with a measure-theoretic normal, the additional results being statements about which densities give continuous limit values. On an Ahlfors–David regular surface the full Plemelj calculus holds, with the involution $\mathcal{S}$, the complementary projections and the two spaces $M^l,M^r$ on which the transform acts as a bounded operator. On a rectifiable $\lvert F\rvert$-regular surface that is not Ahlfors–David the transform is defined with the weight $\lvert F\rvert$ and the Plemelj formula carries $F$ in its boundary term, the existence of the limit values being equivalent to the uniform convergence of the truncated integral. On a $d$-summable fractal boundary neither the boundary measure nor the singular integral is available, and the transform is rebuilt from the Teodorescu transform and a Whitney extension, with the approximate dimension as the invariant that replaces the Minkowski dimension in the solvability criterion. The Hermitean theory of the next sections is orthogonal to this one: it refines the algebra and the operator, whereas the present refinement is of the set on which the boundary condition is imposed, and the two refinements have not been combined in this article. They have been combined in the literature: the boundary-value problems for the complex (quaternionic) Hermitean system on non-smooth domains of $\mathbb{R}^{2n}$ ($\mathbb{R}^{4n}$) — the Hermitean Helmholtz equation, the Hermitean Cauchy formula on a domain with fractal boundary, and the matrix Cauchy and Hilbert transforms on fractal domains, all cited in Further Reading — are that combination, and the Hermitean non-smooth theory is the frontier this article leaves to be written.

## Homogeneous Monogenics and the Fischer Decomposition

**Definition.** A **solid spherical monogenic** of degree $k$ is a left monogenic $A$-valued (or $\mathcal{S}$-valued) polynomial that is homogeneous of degree $k$; the space of such polynomials is written $\mathcal{M}_k = \mathcal{M}_k(A,D)$. It is finite-dimensional, and $\mathcal{M}_0$ is the space of constants. The **inner spherical monogenics** of degree $k$ are the restrictions of the elements of $\mathcal{M}_k$ to the unit sphere.

**Proposition.** For each $k$ the restriction map $P\mapsto P|_{S^m}$ is injective on $\mathcal{M}_k$, and the spaces $\mathcal{M}_k$ for distinct $k$ are pairwise orthogonal in $L^2(S^m;\mathcal{S})$ with respect to the surface measure.

*Proof.* A homogeneous polynomial vanishing on the unit sphere vanishes identically by homogeneity. For the orthogonality, the Euclidean structure of the ambient space gives the spherical decomposition, and the monogenic polynomials of distinct degrees are eigenfunctions of the spherical Cauchy–Riemann operator for distinct eigenvalues; eigenfunctions of a self-adjoint operator for distinct eigenvalues are orthogonal.

**Theorem (Fischer decomposition).** Let $\mathcal{P}_k$ be the space of $\mathcal{S}$-valued homogeneous polynomials of degree $k$ on $\mathbb{R}^{m+1}$. Then

$$
\mathcal{P}_k = \bigoplus_{j=0}^{k} (x^{\natural})^{\,j}\,\mathcal{M}_{k-j} ,
$$

a finite direct sum in which $(x^{\natural})^{\,j}$ denotes left multiplication by the $j$-th power of the conjugate variable $x^{\natural} = x_0-\sum_{i=1}^{m}e_ix_i$.

*Proof.* Quoted as standard. Multiplication by $x^{\natural}$ raises the degree by one, and its interaction with $D$ differs from a scalar by terms of the same parity; the monogenic part of $\mathcal{P}_k$ is $\mathcal{M}_k$, the remainder is $x^{\natural}$ times the polynomials of degree $k-1$, and the argument is an induction on the degree of the same triangular kind as the Fischer decomposition for the Laplacian, with $D$ in place of $\Delta$ and $x^{\natural}$ in place of the radial factor. The decomposition is the Clifford analogue of the decomposition of harmonic polynomials into radial layers, with the solid harmonics replaced by the solid spherical monogenics.

**Remark (the multiplier and the sign convention).** The operator that raises the degree in the decomposition is the conjugate variable $x^{\natural}$, not $x$, and this is forced by the sign convention $D=\partial_0+\sum_{i\ge1}e_i\partial_i$ with $D\bar D=\Delta$: in the complex case $m=1$, where the monogenic polynomials of degree $d$ are the multiples of $z^d$, the piece $(x^{\natural})^{\,j}\mathcal{M}_{k-j}$ is the complex line spanned by $\bar z^{\,j}z^{k-j}$, and the $k+1$ lines of the decomposition are exactly the standard monomial basis of the homogeneous polynomials of degree $k$. The operator $\bar D=\partial_0-\sum_{i\ge1}e_i\partial_i$ plays the mirror role, and the decomposition can equally be written with $\bar D$ and the powers of $x$.

**Corollary (the dimension of the pieces).** The Fischer decomposition reduces the computation of $\dim\mathcal{M}_k$ to a recursion with initial value $\dim\mathcal{M}_0=\dim\mathcal{S}$; explicitly, for $k\ge1$,

$$
\dim\mathcal{M}_k = \dim\mathcal{P}_k-\dim\mathcal{P}_{k-1} = \dim\mathcal{S}\left[\binom{m+k}{k}-\binom{m+k-1}{k-1}\right],
$$

and the sum of the dimensions of the pieces equals $\dim\mathcal{S}\cdot\binom{m+k}{k}$, the dimension of $\mathcal{P}_k$. The explicit basis for a given $m$ is system-specific.

*Proof.* Multiplication by $x^{\natural}$ is injective on polynomials, because $x^{\natural}$ is a unit of $A$ at every point where $x_0\neq0$ and a polynomial identity is determined by its values on a nonempty open set; hence each summand has dimension $\dim\mathcal{M}_{k-j}$ and the direct sum counts dimensions: $\dim\mathcal{P}_k=\sum_{i=0}^{k}\dim\mathcal{M}_i$. Subtracting the same identity with $k$ replaced by $k-1$ gives the recursion.

**Example (the monogenic pieces in low dimension).** For $m=1$ and $\mathcal{S}=\mathbb{C}$, the monogenic polynomials of degree $d$ are the multiples of $z^d$, and the Fischer decomposition is the assertion that every homogeneous polynomial of degree $k$ in $z,\bar z$ has a unique expansion $\sum_{j=0}^{k}c_j\bar z^{\,j}z^{k-j}$ with $c_j\in\mathbb{C}$; this is the elementary identity $\mathcal{P}_k=\bigoplus_j\bar z^{\,j}\mathbb{C}z^{k-j}$. For $m\ge2$ the monogenic piece is larger, and the formula above computes its dimension from $\dim\mathcal{S}$; the classical tables of spherical monogenics give the explicit bases. The example shows the two features that the Clifford case adds to the complex one: several inequivalent monogenic polynomials of the same degree, and a dependence of the count on the value module.

## Polymonogenic Functions

**Definition.** Let $k\ge1$. A function $f$ of class $C^k$ is **$k$-monogenic** (or polymonogenic of order $k$) if

$$
D^kf = 0 .
$$

The monogenic functions are the case $k=1$, and $k$-monogenic functions with a value in $\mathcal{S}$ include the $(k-1)$-monogenic ones.

**Theorem (Almansi representation).** Let $\Omega\subseteq\mathbb{R}^{m+1}$ be star-shaped with respect to the origin and let $f$ be $k$-monogenic on $\Omega$. Then there are monogenic functions $f_0,\dots,f_{k-1}$ on $\Omega$ with

$$
f = \sum_{j=0}^{k-1}(x^{\natural})^{\,j}f_j .
$$

*Proof.* Quoted as standard (the Almansi theorem for the Cauchy–Riemann operator). The proof is an induction on $k$: the equation $D^kf=0$ is integrated along the rays from the origin, the primitive gained at each step being monogenic, and the representation is the result of iterating the step $k$ times; the star-shaped hypothesis is what makes the radial integration available, and the uniqueness of the decomposition follows from the Fischer decomposition on the homogeneous pieces. The representation is read with the conjugate variable, for the same sign reason as in that theorem: the solution $\bar z$ of $D^2f=0$ in the complex case has the representation $\bar z=0+\bar z\cdot1$ with monogenic data, and no representation of the form $f_0+zf_1$ with monogenic $f_0,f_1$, since $\bar z$ is not monogenic.

**Example (the polyharmonic parallel).** The classical Almansi theorem for the Laplacian states that a polyharmonic function of order $k$, $\Delta^kf=0$, has the representation $f=\sum_{j=0}^{k-1}|x|^{2j}h_j$ with $h_j$ harmonic. The Clifford theorem above is the same statement with the Laplacian replaced by $D$, the radial factor $|x|^{2j}$ replaced by $(x^{\natural})^{\,j}$, and the harmonic functions replaced by the monogenic ones; the factorisation $D\bar D=\Delta$ is what makes the two towers of equations comparable. The comparison is a clean instance of the general principle that a first-order elliptic operator whose square is the Laplacian carries the second-order theory inside it.

**Remark (the hierarchy of kernels).** The spaces $\ker D\subseteq\ker D^2\subseteq\ker D^3\subseteq\cdots$ form a strictly increasing chain of function spaces whose union is the space of all functions analytic near the origin that are in the kernel of some power of $D$; the Almansi theorem describes each stage as the sum of at most $k$ monogenic pieces multiplied by powers of the conjugate variable. The chain is the Clifford form of the classification of the solutions of an elliptic operator with a nilpotent leading term, and it is the reason the polymonogenic functions occur naturally in the boundary-value problems of the theory: the data of order $k$ are matched by the solutions of $D^kf=0$.

## The Shifted Operator and the Helmholtz Splitting

**Definition.** For a constant scalar $\lambda$ — real or complex, and therefore central in the algebra — the **shifted Cauchy–Riemann operator** is
$$
D_\lambda=D+\lambda .
$$
The shift is of order zero, so $D_\lambda$ has the same principal symbol as $D$: the ellipticity, the symbol, and the order of the singularity of the kernel are those of $D$, and the two operators differ in a lower-order term alone. Their function theories are parallel rather than nested, and for $\lambda\neq0$ they meet only at the origin: if $Df=0$ and $D_\lambda f=0$ simultaneously then $\lambda f=0$.

**Theorem (the Helmholtz splitting).** Let $\lambda\neq0$ and let $D=\sum_{k=1}^ne_k\partial_k$ with $e_k^2=-1$ for every $k$, so that $D^2=-\Delta$. Then
$$
D_\lambda D_{-\lambda}=D^2-\lambda^2=-(\Delta+\lambda^2),
\qquad
\ker(\Delta+\lambda^2)=\ker D_\lambda\oplus\ker D_{-\lambda},
$$
with the explicit projections
$$
f=f_++f_-,\qquad f_\pm=\mp\frac{1}{2\lambda}\,D_{\mp\lambda}f .
$$
*Proof.* The factorisation uses the centrality of $\lambda$, its constancy — which is what lets it pass through $D$ — and $D^2=-\Delta$; it shows that $\ker D_{\pm\lambda}\subseteq\ker(\Delta+\lambda^2)$. Conversely let $(\Delta+\lambda^2)f=0$. Then $D_\lambda D_{-\lambda}f=0$ and $D_{-\lambda}D_\lambda f=0$, so the two functions displayed satisfy $D_\lambda f_+=0$ and $D_{-\lambda}f_-=0$; and $f_++f_-=\frac{1}{2\lambda}(D_\lambda-D_{-\lambda})f=f$. The sum is direct, since $D_\lambda f=D_{-\lambda}f=0$ forces $2\lambda f=0$. $\square$

**Remark (the shifted kernel).** The same factorisation produces the fundamental solution of $D_\lambda$ from that of the Helmholtz operator. If $(\Delta+\lambda^2)\Phi_\lambda=-\delta_0$ then
$$
E_\lambda=D_{-\lambda}\Phi_\lambda,
\qquad
D_\lambda E_\lambda=D_\lambda D_{-\lambda}\Phi_\lambda=-(\Delta+\lambda^2)\Phi_\lambda=\delta_0 .
$$
One further application of the conjugate operator, then, turns the Helmholtz kernel into the kernel of the shifted operator, and the shift leaves the normalisation of the kernel unchanged, because its contribution to the flux through a small sphere is of lower order in the radius and vanishes with it. In $\mathbb{R}^3$ the Helmholtz kernel is $\Phi_\lambda(x)=e^{i\lambda|x|}/(4\pi|x|)$ with the outgoing branch selected by the radiation condition, and the construction yields the corresponding Helmholtz–Dirac kernel with its Borel–Pompeiu and Plemelj–Sokhotski formulas; those formulas belong to the articles that use them, *Electromagnetism in Media — The Local Complex Structure at Work* and *Maxwell's Equations in Chiral Media — The Quaternionic Reformulation*, and are not restated here.

**Remark (the two towers).** The shift is the second way of building a higher-order theory out of the first-order operator. The first is the power, and it is the polymonogenic chain $D^kf=0$ of the preceding section, described by the Almansi representation. The shift produces the Helmholtz family, and at $\lambda=0$ its splitting degenerates: the two operators coincide, the projections are undefined, and the second-order equation of the family becomes $\Delta f=0$, whose solutions contain the monogenic ones as a proper subspace. The two constructions are genuinely different families, and the applications use the shifted one.

The factorisation uses the constancy of $\lambda$ twice. For a variable shift the product rule gives
$$
\bigl(D+\lambda(x)\bigr)\bigl(D-\lambda(x)\bigr)=D^2-(D\lambda)-\lambda^2 ,
$$
so a variable shift costs the term $-(D\lambda)$: the splitting theorem fails, and the second-order operator is no longer the Helmholtz operator. What is gained in exchange is a conjugation that removes the variability again. With $\eta$ a scalar function and $Q=\lambda+\eta^{-1}D\eta$ one has
$$
D+\lambda=\eta\,(D+Q)\,\eta^{-1},
$$
so a variable-coefficient equation with a scalar shift is equivalent to a constant-coefficient one whenever $Q$ is constant; in the applications $\eta=e^{\varphi}$ and the constancy of $Q=\lambda+D\varphi$ is an eikonal condition. The constant $Q$ is then generally Clifford-valued rather than scalar, so the splitting theorem above does not apply to it: the reduction solves the equation by a zero-divisor device, not by a spectral one. That device and its use in slowly varying media belong to the articles that use it.

## The Hermitean Refinement

The theory above rests on a single operator. A second refinement of the Clifford setting keeps the algebra and replaces the single equation $Df=0$ by a system: the operator is **split** into several operators of the same first order, and the functions of the theory are their **simultaneous null solutions**. In the complex case, where the ambient space is even-dimensional, $\mathbb{R}^{2n}\cong\mathbb{C}^n$, the split is into **two** *Hermitean Dirac operators*, invariant under the unitary group, and the simultaneous null solutions are the **Hermitean monogenic** functions. In the quaternionic case, where the ambient dimension is a multiple of four, $\mathbb{R}^{4n}$, the split is into **four** such operators, and the simultaneous null solutions are the **q-Hermitean monogenic** functions. The number is dictated by the algebra — two for $\mathbb{C}$, four for $\mathbb{H}$ — and the class is *smaller* than the monogenic one of the preceding sections, because simultaneous vanishing is a system and not one equation: a function that is q-Hermitean monogenic is monogenic for each of the four operators, and the converse fails.

The construction starts from the Euclidean data. Let $N=4n$, let $\mathrm{Cl}_{0,N}$ be generated by $e_1,\dots,e_N$ with $e_ie_j+e_je_i=-2\delta_{ij}$, and let the quaternions act as central scalars, so that the values lie in $\mathbb{H}_N=\mathbb{H}\otimes_\mathbb{R}\mathrm{Cl}_{0,N}$; the variable is the pure vector $X=\sum_{i=1}^{N}e_ix_i$ and the operator is the vector part of the corpus's $D$,
$$
\partial_X=\sum_{i=1}^{N}e_i\partial_{x_i},\qquad \partial_X^2=-\Delta_N ,
$$
the sign being the one of *Regularity and the Cauchy–Riemann Operator* for the part of $D$ assembled from the generators (the corpus's $D\bar D=\Delta$ is unaffected; the squared vector part is $-\Delta$, as in the kernel computation of the Cauchy section). Group the generators in fours and put, for $l=1,\dots,n$,
$$
\begin{aligned}
X_0&=\sum_{l=1}^{n}\bigl(e_{4l-3}x_{4l-3}+e_{4l-2}x_{4l-2}+e_{4l-1}x_{4l-1}+e_{4l}x_{4l}\bigr),\\
X_1&=\sum_{l=1}^{n}\bigl(e_{4l-3}x_{4l-2}-e_{4l-2}x_{4l-3}-e_{4l-1}x_{4l}+e_{4l}x_{4l-1}\bigr),\\
X_2&=\sum_{l=1}^{n}\bigl(e_{4l-3}x_{4l-1}+e_{4l-2}x_{4l}-e_{4l-1}x_{4l-3}-e_{4l}x_{4l-2}\bigr),\\
X_3&=\sum_{l=1}^{n}\bigl(e_{4l-3}x_{4l}-e_{4l-2}x_{4l-1}+e_{4l-1}x_{4l-2}-e_{4l}x_{4l-3}\bigr).
\end{aligned}
$$
The first is the ordinary Clifford vector; the other three are its companions under the quaternionic sign changes (the *twisted* vectors of the Hermitean literature, a different use of the word from the twisted operator of the next section). The four are Fischer duals of the four operators $\partial_{X_r}$ and satisfy
$$
X_r^2=-|X|^2,\qquad \{X_r,X_s\}=X_rX_s+X_sX_r=0 \quad (r\neq s),
$$
with the same two relations for the operators in place of the vectors. The **Hermitean variables** and the **Hermitean Dirac operators** are the four invertible combinations
$$
\begin{aligned}
\partial_{Z_0}&=\tfrac{1}{16}\bigl(\partial_{X_0}+i\,\partial_{X_1}+j\,\partial_{X_2}+k\,\partial_{X_3}\bigr),&
\partial_{Z_1}&=\tfrac{1}{16}\bigl(\partial_{X_0}+i\,\partial_{X_1}-j\,\partial_{X_2}-k\,\partial_{X_3}\bigr),\\
\partial_{Z_2}&=\tfrac{1}{16}\bigl(\partial_{X_0}-i\,\partial_{X_1}+j\,\partial_{X_2}-k\,\partial_{X_3}\bigr),&
\partial_{Z_3}&=\tfrac{1}{16}\bigl(\partial_{X_0}-i\,\partial_{X_1}-j\,\partial_{X_2}+k\,\partial_{X_3}\bigr),
\end{aligned}
$$
with the variables $Z_r$ built from the $X_r$ by the *same* four sign patterns. The factor $\tfrac1{16}$ is the normalisation that makes the Laplacian split below; the patterns are the rows of the Hadamard matrix with $SS^{\mathsf T}=4I_4$ and $\det S=-16$, which is what makes the two descriptions equivalent.

The **Hermitean conjugation** is the composition of the $\mathbb{H}$-conjugation with the Clifford conjugation,
$$
\lambda^\dagger=\sum_A\bar\lambda_A\,e_A^{\natural},
$$
the sum running over the blades $e_A$ of $\mathrm{Cl}_{0,N}$, so that a vector is anti-self-adjoint, $X_r^\dagger=-X_r$, and the four operators are the conjugates of one another in pairs. With this involution the Hermitean variables reproduce the norm of $X$ and the four operators *split* the Laplacian:
$$
\sum_{r=0}^{3}Z_rZ_r^\dagger=\sum_{r=0}^{3}Z_r^\dagger Z_r=16|X|^2,\qquad
\Delta_N=16\sum_{r=0}^{3}\partial_{Z_r}\partial_{Z_r}^\dagger=16\sum_{r=0}^{3}\partial_{Z_r}^\dagger\partial_{Z_r}.
$$
The second display is the Hermitean counterpart of $D\bar D=\bar DD=\Delta$: the one second-order operator of the Euclidean theory is now the sum of four first-order squares. Note that the involution entering it is *not* the $L^2$ adjoint; it is the algebra anti-involution above, under which a 1-vector changes sign, and the identity holds with that sign.

**Definition.** Let $\Omega\subseteq\mathbb{R}^{4n}$ be open. A $C^1$ function $f:\Omega\to\mathbb{H}_N$ is **q-Hermitean monogenic** in $\Omega$ when
$$
\partial_{Z_0}f=\partial_{Z_1}f=\partial_{Z_2}f=\partial_{Z_3}f=0,
$$
equivalently, and by the same four sign patterns, when $\partial_{X_0}f=\partial_{X_1}f=\partial_{X_2}f=\partial_{X_3}f=0$. The two systems are equivalent because the sign matrix relating them is invertible; there is no claim that either equation alone defines the class.

### The Circulant Matrix Device

The Euclidean kernels of the four operators are
$$
F_r(X)=-\frac{X_r}{a_{4n}|X|^{4n}},\qquad a_{4n}=\frac{2\pi^{2n}}{\Gamma(2n)}=|S^{4n-1}| ,
$$
the area of the unit sphere in $\mathbb{R}^{4n}$. This is the corpus's Cauchy kernel $\omega_m^{-1}x^{\natural}|x|^{-m-1}$ for the pure vector variable, where $\bar X_r=-X_r$ and the sphere is $S^{4n-1}$; the homogeneity is $1-4n$. It satisfies
$$
\partial_{X_r}F_r=\delta,\qquad \partial_{X_r}F_s+\partial_{X_s}F_r=0\quad(r\neq s),
$$
the second identity being the operator form of $\{X_r,X_s\}=0$. The **Hermitean kernels** are
$$
E_r(Z)=\frac{Z_r^\dagger}{a_{4n}|Z|^{4n}} .
$$
The kernel $E_r$ is **not** a fundamental solution of $\partial_{Z_r}$; the four kernels are needed together, and the object that carries the fundamental solution is a matrix. With the circulant matrices
$$
D=\begin{pmatrix}\partial_{Z_0}&\partial_{Z_3}&\partial_{Z_2}&\partial_{Z_1}\\
\partial_{Z_1}&\partial_{Z_0}&\partial_{Z_3}&\partial_{Z_2}\\
\partial_{Z_2}&\partial_{Z_1}&\partial_{Z_0}&\partial_{Z_3}\\
\partial_{Z_3}&\partial_{Z_2}&\partial_{Z_1}&\partial_{Z_0}\end{pmatrix},
\qquad
E=\begin{pmatrix}E_0&E_3&E_2&E_1\\ E_1&E_0&E_3&E_2\\ E_2&E_1&E_0&E_3\\ E_3&E_2&E_1&E_0\end{pmatrix},
$$
one has
$$
D^{\mathsf T}E=\delta I ,
$$
so that $E$ is a fundamental solution of the matrix Dirac operator $D^{\mathsf T}$. The $(0,0)$ entry is the combination $\partial_{Z_0}E_0+\partial_{Z_1}E_1+\partial_{Z_2}E_2+\partial_{Z_3}E_3$, and it evaluates to
$$
\partial_{Z_0}E_0+\partial_{Z_1}E_1+\partial_{Z_2}E_2+\partial_{Z_3}E_3
=\tfrac{1}{16}\bigl(4\,\delta(X_0)+4\,\delta(X_1)+4\,\delta(X_2)+4\,\delta(X_3)\bigr)=\delta(Z),
$$
a single delta: the four Euclidean deltas coincide, because the vectors $X_r$ are related to $X$ by an orthogonal change of variables, and the factor of four in front of each is the contribution of the four rows of the Hadamard matrix. The same calculus gives the matrix form of the Laplacian split,
$$
16\,D^{\mathsf T}D^\dagger=\Delta_N I_4 .
$$

### The Integral Formulae

The matrix device yields the integral representation. Let $\Gamma$ be a compact, oriented $4n$-dimensional manifold with smooth boundary in $\Omega$, write $\Gamma^+$ for its interior and $\Gamma^-$ for $\Omega\setminus\Gamma$, and let $N$ be the circulant matrix associated with the four Hermitean conormals $N_r=\tfrac{1}{16}(n_0+s_{r1}\,in_1+s_{r2}\,jn_2+s_{r3}\,kn_3)$, $n_0,\dots,n_3$ the twisted normals of $\partial\Gamma$. For circulant matrix functions $F,G$ of the above shape,
$$
\int_\Gamma\bigl[(FD^{\mathsf T})G+F(D^{\mathsf T}G)\bigr]dV=\int_{\partial\Gamma}FN^{\mathsf T}G\,dS ,
$$
the Hermitean Clifford–Stokes theorem. From it follow the **Q-Hermitean Borel–Pompeiu formula**
$$
\int_{\partial\Gamma}E(Z-V)N^{\mathsf T}(Z)G(X)\,dS(X)-\int_\Gamma E(Z-V)\bigl[D^{\mathsf T}G(X)\bigr]dV(X)
=\begin{cases}G(Y),&Y\in\Gamma^+,\\ O,&Y\in\Gamma^-,\end{cases}
$$
and, when the second integral vanishes because $G$ is Q-Hermitean monogenic, the **Q-Hermitean Cauchy integral formula** with the same right-hand side. Applied to the diagonal matrix whose four diagonal entries coincide with a single function $g$, the two statements become the corresponding formulae for $g$, and the kernel $E$ is the quaternionic Hermitean Cauchy kernel. In a special case the representation reduces to the **Martinelli–Bochner type formula**
$$
\sum_{s=0}^{3}\Bigl[\int_{\partial\Gamma}E_s(Z-V)N_s(Z)g(X)\,dS(X)-\int_{\Gamma}E_s(Z-V)\bigl(\partial_{Z_s}g(X)\bigr)dV(X)\Bigr]=g(Y),
$$
the integral representation of several complex variables, which is the classical Cauchy formula when $n=1$. The complex theory follows the same plan with two operators and a circulant $(2\times2)$ matrix, and there Hermitean monogenicity is equivalent to holomorphy in the underlying complex variables in particular cases — another way in which the refinement is a statement about the *operator*, not about a new class of functions.

**Remark (what the refinement is, and is not).** Three distinct notions now carry the word *monogenic*, and they must not be run together: the corpus's $Df=0$ of this article and of *Regularity and the Cauchy–Riemann Operator*; the Hermitean monogenicity above, which is the simultaneous vanishing of two or four operators; and the nonlinear monogenicity of the algebrodynamics programme, where the equation is nonlinear and the solutions are not a linear class. The Hermitean refinement belongs to Clifford analysis and is function-theoretic: its results are integral representations, boundary-value problems and the matrix function theory built around them, not a physical model, and the corpus uses it as the analytic reference behind the quaternionic integral representations rather than as a source of physics. Its relation to the corpus is through the Cauchy theory: the Cauchy–Pompeiu and Cauchy formulae of the Cauchy section are the one-operator case, and the matrix formulae above are what the same theorems become when the operator is split.

**Remark (verification).** The identities above were recomputed in $\mathrm{Cl}_{0,4}$ with quaternion coefficients, in the model $\mathbb{H}\otimes_\mathbb{R}\mathrm{Cl}_{0,4}$. The coefficient matrices of the four vectors are column-orthonormal, whence $X_r^2=-|X|^2$ and $\{X_r,X_s\}=0$ for all six pairs; the corresponding operator identities give $\partial_{X_r}^2=-\Delta_4$ and $\{\partial_{X_r},\partial_{X_s}\}=0$. The norm identity $\sum_rZ_rZ_r^\dagger=16|X|^2$ and the split $\Delta_4=16\sum_r\partial_{Z_r}\partial_{Z_r}^\dagger=16\sum_r\partial_{Z_r}^\dagger\partial_{Z_r}$ both hold in that model, the second only when the involution is the composition of the two conjugations, as stated above; with the $\mathbb{H}$-conjugation alone the split comes out with the opposite sign, which is the one place in this section where a convention can silently invert a result. The Hadamard matrix has $SS^{\mathsf T}=4I_4$ and $\det S=-16$, so the Hermitean and Euclidean null systems are equivalent. In the $(0,0)$ entry of $D^{\mathsf T}E$, the sixteen cross terms cancel in antisymmetric pairs and the diagonal terms contribute $\delta$ with coefficient one, giving $\delta$ and hence $\delta(Z)$ after the factor $\tfrac1{16}$; the identity $\partial_{X_r}F_s+\partial_{X_s}F_r=0$ for $r\neq s$, on which the cancellation rests, is the operator form of the anticommutation verified above.

## Modules, Twisting and the Boundary to Part II

**Remark (the twisted operator).** For a Clifford module $\mathcal{S}$ and an auxiliary bundle with a connection, the operator of the theory can be twisted to act on sections of the tensor product; the result is the **twisted Cauchy–Riemann operator** of *Clifford Modules and the Twisted Cauchy–Riemann Operator*, an operator whose square is a Laplacian with a curvature endomorphism, and whose associated elliptic complex has an index. The construction, the complex and the index are Part II's; here the module language is only what allows the values of the monogenic functions to be spinors rather than the algebra itself. The classical theory is the case $\mathcal{S}=A$ with the flat connection.

**Remark (the operator and the spin geometry).** The Cauchy–Riemann operator of this article is the flat model of the operator constructed on a spin manifold in *Spin Geometry*: there the operator acts on spinor fields, its square is the Laplacian twisted by the scalar curvature through the Lichnerowicz formula, and its index is computed by the Atiyah–Singer theorem of *The Atiyah–Singer Index Theorem and K-Theory*. The flat theory is the local model of the curved one; the analytic regularity theory of the curved operator — self-adjointness, spectrum, Fredholm properties — belongs, which treats the family of operators bearing the classical name.

**Remark (the symmetry group).** The automorphism group of the Clifford algebra and the group of orthogonal transformations of the generating subspace act on the admissible operators, and their stabiliser, as in *Hypercomplex Analysis*, is the symmetry group of the system. The conformal group in $(m+1)$ dimensions acts on the monogenic functions by a matrix action, the **Vahlen matrices**, and it preserves the class of monogenic functions and transforms the Cauchy kernel; this is the Clifford form of the Möbius symmetry of complex analysis. The conformal geometry itself is treated in Part II, and the conformal invariance of the Cauchy kernel is the analytic statement of the same symmetry.

## Summary

Clifford analysis is the function theory of the Cauchy–Riemann operator $D=\partial_0+\sum_{i=1}^me_i\partial_i$ with $e_ie_j+e_je_i=-2\delta_{ij}$; the variable ranges over the vector space $\mathbb{R}^{m+1}$ and the values lie in the Clifford algebra $\mathrm{Cl}_{0,m}$ or a Clifford module. The operator satisfies $D\bar D=\bar DD=\Delta$ and is elliptic, with symbol $\sigma(\xi)=\xi_0+\sum_ie_i\xi_i$ invertible for $\xi\neq0$ and inverse $\bar\sigma(\xi)/|\xi|^2$. The functions annihilated by $D$ are the monogenic, or left regular, functions; they form a real vector space closed under right multiplication by constants but not under products, and they include the powers $z^k$ of the complex variable $z=x_0+e_1x_1$ as well as the exponential-type solutions generated by isotropic covectors. Because every monogenic function is harmonic componentwise, it is real-analytic, satisfies the mean value property, the maximum principle, Liouville's theorem and the identity theorem. The fundamental solution is the Cauchy kernel $E(x)=\omega_m^{-1}x^{\natural}|x|^{-m-1}$ with $\omega_m=|S^m|$, which reduces to $1/(2\pi z)$ in the complex case and is the kernel of the Cauchy–Pompeiu formula and of the Cauchy integral formula; the boundary Cauchy transform is the orthogonal projection onto the monogenic Hardy space. The homogeneous monogenic polynomials $\mathcal{M}_k$ are finite-dimensional, pairwise orthogonal by degree, and organise all polynomials through the Fischer decomposition $\mathcal{P}_k=\bigoplus_{j=0}^k (x^{\natural})^{\,j}\mathcal{M}_{k-j}$; the polymonogenic functions, the solutions of $D^kf=0$, are described by the Almansi representation $f=\sum_{j=0}^{k-1}(x^{\natural})^{\,j}f_j$ with $f_j$ monogenic, the Clifford counterpart of the Almansi theorem for polyharmonic functions. The **shifted** operator $D_\lambda=D+\lambda$ is the other way the Clifford structure builds a second-order theory out of the first-order one: its square factorises the Helmholtz operator, $D_\lambda D_{-\lambda}=-(\Delta+\lambda^2)$, the Helmholtz space splits with the explicit projections $f_\pm=\mp(1/2\lambda)D_{\mp\lambda}f$ as $\ker(\Delta+\lambda^2)=\ker D_\lambda\oplus\ker D_{-\lambda}$, and the kernel of $D_\lambda$ is one application of the conjugate operator to the Helmholtz kernel, the shift leaving the normalisation of the kernel unchanged. The **Hermitean** refinement keeps the algebra and splits the operator: in $\mathbb{R}^{4n}$ the four Hermitean Dirac operators $\partial_{Z_r}=\tfrac1{16}(\partial_{X_0}\pm i\partial_{X_1}\pm j\partial_{X_2}\pm k\partial_{X_3})$ split the Laplacian, $\Delta_{4n}=16\sum_r\partial_{Z_r}\partial_{Z_r}^\dagger$, their simultaneous null solutions are the q-Hermitean monogenic functions, defined by $\partial_{Z_0}f=\dots=\partial_{Z_3}f=0$ and equivalently by the same system for the four Euclidean operators, and the four Euclidean Cauchy kernels combine into a circulant matrix $E$ that is the fundamental solution of the matrix operator $D^{\mathsf T}$, giving the Hermitean Clifford–Stokes, Borel–Pompeiu and Cauchy formulae and, in a special case, the Martinelli–Bochner formula. The twisted operator on a Clifford module, the spin-geometric operator on a spin manifold and the index theory of both are Part II's and are cited rather than developed. The boundary theory is refined once more by the measure-theoretic version: on a boundary of finite $m$-dimensional Hausdorff measure the Cauchy transform is still a boundary integral, now against Federer's normal, and on an Ahlfors–David regular surface the Plemelj calculus holds with the involution $\mathcal{S}$ and the complementary projections $P^\pm=\tfrac12(I\pm\mathcal{S})$, with $\mathcal{S}$ of norm one in the norm associated to the splitting and with the embedding of the Hölder classes into the spaces $M^l,M^r$ compact; on a rectifiable $\lvert F\rvert$-regular surface the transform is defined with the weight $\lvert F\rvert$ and the weighted Plemelj formula carries $F$ in its boundary term, the existence of the continuous limit values being equivalent to the uniform convergence of the truncated integral; on a $d$-summable fractal boundary there is no boundary measure to integrate against, the transform is rebuilt from the Teodorescu transform and a Whitney extension, the fractal Hilbert transform is defined by the trace of the new transform, a density of class $C^{0,\alpha}$ with $(m+1)\alpha>d$ gains an exponent $\beta<((m+1)\alpha-d)/(m+1-d)$, and the approximate dimension replaces the Minkowski dimension in the solvability condition $\alpha>\dim_a\Gamma/(m+1)$ of the jump problem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $m$ | Number of Clifford generators; ambient dimension $m+1$ |
| $e_1,\dots,e_m$ | Generators, $e_ie_j+e_je_i=-2\delta_{ij}$; $e_0=1$ |
| $\mathrm{Cl}_{0,m}$, $A$ | Clifford algebra of the negative-definite form; $\dim_\mathbb{R}A=2^m$ |
| $x=x_0+\sum_ix_ie_i$ | Vector variable in $\mathbb{R}^{m+1}$ |
| $x^{\natural} = x_0-\sum_ix_ie_i$ | Clifford conjugation; $x x^{\natural}=|x|^2$ |
| $\mathcal{S}$ | Clifford module of values (spinor module in the classical case) |
| $D=\sum_{\mu=0}^me_\mu\partial_\mu$ | Cauchy–Riemann operator (classically, Dirac operator) |
| $\bar D=\partial_0-\sum_ie_i\partial_i$ | Conjugate operator; $D\bar D=\bar DD=\Delta$ |
| $\sigma(\xi)$, $\bar\sigma(\xi)$ | Symbol and conjugate symbol |
| $Df=0$, $fD=0$ | Left and right monogenicity |
| $E(x)=\omega_m^{-1}x^{\natural}|x|^{-m-1}$ | Cauchy kernel, $DE=\delta_0$ |
| $\omega_m=|S^m|$ | Surface area of the unit sphere in $\mathbb{R}^{m+1}$ |
| $\nu_B=\sum_\mu\nu_\mu e_\mu$ | Conormal element of a boundary |
| $\mathcal{M}_k$ | Solid spherical monogenics of degree $k$ |
| $\mathcal{P}_k$ | Homogeneous polynomials of degree $k$ |
| $\mathcal{C}$, $H^2$ | Cauchy transform and monogenic Hardy space |
| $D^kf=0$ | Polymonogenic of order $k$; Almansi representation |
| $D_\lambda=D+\lambda$ | Shifted operator ($\lambda$ central, constant); $D_\lambda D_{-\lambda}=-(\Delta+\lambda^2)$ |
| $E_\lambda=D_{-\lambda}\Phi_\lambda$ | Kernel of $D_\lambda$, from a fundamental solution of $-(\Delta+\lambda^2)$ |
| $X_0,\dots,X_3$ | The four Euclidean vectors; $X_r^2=-\lvert X\rvert^2$, $\{X_r,X_s\}=0$ |
| $\partial_{X_0},\dots,\partial_{X_3}$ | Their Fischer duals; $\partial_{X_r}^2=-\Delta_{4n}$ |
| $Z_0,\dots,Z_3$ | Hermitean variables, the four $X_0\pm iX_1\pm jX_2\pm kX_3$ |
| $\partial_{Z_0},\dots,\partial_{Z_3}$ | Hermitean Dirac operators; $\Delta_{4n}=16\sum_r\partial_{Z_r}\partial_{Z_r}^\dagger$ |
| q-Hermitean monogenic | $\partial_{Z_0}f=\partial_{Z_1}f=\partial_{Z_2}f=\partial_{Z_3}f=0$ |
| $F_r$, $a_{4n}$ | Euclidean Hermitean kernels $F_r=-X_r/(a_{4n}\lvert X\rvert^{4n})$; $a_{4n}=\lvert S^{4n-1}\rvert$ |
| $E_r$, $E$, $D$, $N$ | Hermitean kernels $E_r=Z_r^\dagger/(a_{4n}\lvert Z\rvert^{4n})$; circulant matrices, $D^{\mathsf T}E=\delta I$ |
| $\nu_B$, $\mathcal{H}^m$, $\mathcal{L}^{m+1}$ | Federer exterior normal of a boundary; Hausdorff boundary measure; Lebesgue measure |
| $\mathcal{C}$, $\mathcal{S}$, $P^\pm=\tfrac12(I\pm\mathcal{S})$ | Cauchy and Hilbert transforms on a non-smooth boundary; complementary projections $(\mathcal{C}^\pm u)=\pm P^\pm u$ |
| $M^l$, $M^r$, $\lVert\cdot\rVert_l$ | Densities with uniformly convergent truncated integral, left and right, with the trace norm |
| $F$, $\lvert F\rvert$-regular, $\mathcal{C}_F$, $\mathcal{S}_F$ | Weight (continuous monogenic $F$); surface whose weighted measure obeys the upper density bound; weighted Cauchy transform and weighted singular integral |
| $\overline{\dim}_M E$, $d$-summable | Upper Minkowski (box) dimension; $\int_0^\delta N_E(t)t^{d-1}dt<\infty$ |
| $\mathcal{T}$, $\mathcal{C}_\Gamma$, $\mathcal{S}_\Gamma$ | Teodorescu transform; fractal Cauchy transform; fractal Hilbert transform $2(\mathcal{C}_\Gamma u)^+-u$ |
| $\dim_a\Gamma$ | Approximate dimension; the jump problem is solvable for $\alpha>\dim_a\Gamma/(m+1)$ |





## Further Reading

- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the classical theory of monogenic functions and the Cauchy kernel.
- R. Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for the function theory over Clifford algebras and Clifford modules.
- John E. Gilbert and Margaret A. M. Murray, *Clifford Algebras and Dirac Operators in Harmonic Analysis* (Cambridge University Press, 1991), for the Hardy spaces, the Cauchy transform and the singular integrals.
- Klaus Gürlebeck, Klaus Habetha and Wolfgang Sprößig, *Holomorphic Functions in the Plane and $n$-dimensional Space* (Birkhäuser, 2008), for the operator-theoretic development in the Clifford setting.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the explicit Cauchy kernels and the boundary-value problems.
- Chun Li, Alan McIntosh and Tao Qian, "Clifford Algebras, Fourier Theory, and Hardy Spaces", in *Clifford Algebras and Their Applications in Mathematical Physics* (Birkhäuser, 2000), for the monogenic Hardy space and the Szegő projection.
- John Ryan (ed.), *Clifford Algebras in Analysis and Related Topics* (CRC Press, 1996), for the Fischer decomposition, spherical monogenics and polymonogenic functions.
- F. Sommen, "Plane Elliptic Systems and Clifford Algebra", *Complex Variables* 3 (1984), for the polymonogenic functions and the Almansi representation.
- V. V. Kravchenko and M. V. Shapiro, *Integral Representations for Spatial Models of Mathematical Physics* (Pitman Research Notes in Mathematics 351, Addison-Wesley Longman, 1996), for the shifted operators $D+\lambda$, the Helmholtz kernels, and the Borel–Pompeiu and Plemelj–Sokhotski formulas that go with them.
- F. Brackx, J. Bory Reyes, H. De Schepper and F. Sommen, "Fundaments of Hermitean Clifford analysis", Part I: Complex Structure, *Complex Analysis and Operator Theory* **1** (2007) 341–365, and Part II: Splitting of $h$-monogenic equations, *Complex Variables and Elliptic Equations* **52** (2007) 1063–1079, for the complex (two-operator) case, the Hermitean Clifford–Stokes theorems and the circulant $(2\times2)$ matrix formulation.
- D. Peña-Peña, I. Sabadini and F. Sommen, "Quaternionic Clifford analysis: the Hermitian setting", *Complex Analysis and Operator Theory* **1** (2007) 97–113, for the four Hermitean Dirac operators, the Hermitean variables and the quaternionic Hermitean setting.
- F. Brackx, B. De Knock, H. De Schepper and F. Sommen, "On Cauchy and Martinelli–Bochner integral formulae in Hermitean Clifford analysis", *Bulletin of the Brazilian Mathematical Society* **40** (2009) 395–416, for the Cauchy and Martinelli–Bochner formulae of the complex case.
- R. Abreu-Blaya, J. Bory-Reyes, F. Brackx, H. De Schepper and F. Sommen, "Cauchy integral formulae in quaternionic Hermitean Clifford analysis", *Complex Analysis and Operator Theory* (2011), DOI 10.1007/s11785-011-0168-8, for the circulant $4\times4$ matrix device, the Q-Hermitean Borel–Pompeiu and Cauchy formulae, and the reduction to the Martinelli–Bochner formula.
- R. Abreu-Blaya and J. Bory-Reyes, "Quaternionic and Clifford Analysis for Non-smooth Domains", in *Operator Theory* (Springer Basel, 2015), 1447–1470, DOI 10.1007/978-3-0348-0667-1_31, for the measure-theoretic Cauchy and Hilbert transforms, the Plemelj formulae on Ahlfors–David regular surfaces, the spaces $M^l$ and $M^r$, the removable-singularity theorems and the $d$-summable fractal theory of the section on non-smooth boundaries.
- R. Abreu-Blaya and J. Bory-Reyes, "Removable singularities for quaternionic monogenic functions of Zygmund class", *Journal of Natural Geometry* **18** (2000), 115–124, for the Zygmund-class case of the removable-set problem.
- J. Bory-Reyes and R. Abreu-Blaya, "Weighted singular integral operators in Clifford analysis", *Mathematical Methods in the Applied Sciences* **25** (2002), 1429–1440, for the weighted singular operator, the class of weight functions $|F|$ and the construction of a non-Ahlfors–David surface in $\mathbb{R}^3$ that is $|F|$-regular.
- R. Abreu-Blaya, J. Bory-Reyes, D. Peña-Peña and T. Moreno-García, "Weighted Cauchy transforms in Clifford analysis", *Complex Variables and Elliptic Equations* **51** (2006), 397–406, for the weighted Cauchy transform on $|F|$-regular surfaces and the equivalence of the existence of continuous limit values with the uniform convergence of the truncated weighted integral.
- R. Abreu-Blaya, J. Bory-Reyes, F. Brackx, H. De Schepper and F. Sommen, "A Hermitian Cauchy formula on a domain with fractal boundary", *Journal of Mathematical Analysis and Applications* **369** (2010), 273–282, and "Boundary value problems associated to a Hermitian Helmholtz equation", *Journal of Mathematical Analysis and Applications* **389** (2012), 1268–1279, for the complex (quaternionic) Hermitian system on non-smooth domains, the Hermitian Helmholtz boundary-value problem and the matrix Cauchy and Hilbert transforms on fractal domains.
- Herbert Federer, *Geometric Measure Theory* (Springer, 1969), for Hausdorff measure, rectifiability, the approximate tangent planes and the exterior normal of a set of finite measure.
- Jenny Harrison and Alec Norton, "The Gauss–Green theorem for fractal boundaries", *Duke Mathematical Journal* **67** (1992), for the $d$-summability of a fractal boundary, its Minkowski dimension, and integration over it.
- Guy David and Stephen Semmes, *Analysis of and on Uniformly Rectifiable Sets*, Mathematical Surveys and Monographs 38 (American Mathematical Society, 1993), for uniform rectifiability and the relation of the class to the Ahlfors–David condition used here.
- Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications* (Wiley, 3rd edition, 2014), for the Minkowski and Hausdorff dimensions and the box-counting dimension of the self-similar sets quoted in the lemma on $d$-summability.
