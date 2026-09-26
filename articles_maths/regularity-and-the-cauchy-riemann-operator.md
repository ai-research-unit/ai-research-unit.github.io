
# __Regularity and the Cauchy–Riemann Operator__

## Introduction

*Hypercomplex Analysis* introduced a hypercomplex system $(A,D)$, where $A$ is a finite-dimensional unital associative real algebra and $D = \sum_\alpha B_\alpha \partial_\alpha$ is a generalised Cauchy–Riemann operator, and defined a function to be left regular when $Df = 0$. This article studies the operator itself: its symbol, the generalised Cauchy–Riemann equations it represents as a system of first-order equations, the ellipticity that follows from the Clifford relations, the relation between left and right regularity, the consequences of ellipticity for the kernel, and the sense in which the operator and the class of regular functions determine each other.

The subject is the operator, not a particular algebra. Everything below is a statement about $(A, D)$ under the standing hypotheses, and every particular hypercomplex theory is an instance: for $A = \mathbb{C}$ with $D = \partial_0 + i\partial_1$ the results reduce to the Cauchy–Riemann equations and the standard facts about holomorphic functions, and for $A = \mathbb{H}$ with the Fueter operator they reduce to the theory of monogenic functions. The systems themselves are treated in categories 26 to 29; here the operator is general.

Throughout, $A$ is a finite-dimensional unital associative real algebra of dimension $m$, with fixed basis $e_0 = 1, e_1, \dots, e_{m-1}$; coordinates $x = \sum_\alpha x_\alpha e_\alpha$; and

$$
D = \partial_0 + \sum_{k \geq 1} B_k \partial_k, \qquad \bar D = \partial_0 - \sum_{k \geq 1} B_k \partial_k,
$$

the coefficients $B_k \in A$ satisfying the Clifford relations

$$
B_j B_k + B_k B_j = -2\delta_{jk}\, 1, \qquad j, k \geq 1.
$$

The ordered tuple $(1, B_1, \dots, B_{m-1})$ is the **frame** of the system, and the operator is assembled from that frame and the coordinate derivatives: the coefficient $B_\alpha$ is the algebra element attached to the coordinate direction $\alpha$, and the single element $D$ of the algebra encodes the whole first-order system. A change of frame by an invertible matrix — the effect of a linear change of coordinates on $\mathbb{R}^m$ — replaces $B_\beta$ by $\sum_\alpha T_{\beta\alpha}B_\alpha$ and leaves the operator unchanged in the new coordinates, so the frame is the algebra-side data of the theory while the operator is the analytic-side data. The hypotheses are those under which the factorisation $D\bar D = \bar D D = \Delta$ of *Hypercomplex Analysis* holds and $D$ is elliptic. Open sets of $A$ are identified with open sets of $\mathbb{R}^m$ through the fixed basis.

## The Symbol and Ellipticity

**Definition.** The **principal symbol** of $D$ is the map

$$
\sigma_D : A \times \mathbb{R}^m \to A, \qquad (x, \xi) \longmapsto \sum_{\alpha=0}^{m-1} B_\alpha \xi_\alpha,
$$

where $B_0 = 1$; for the equation $Df = 0$ the symbol acts on values by left multiplication by $\sum_\alpha B_\alpha\xi_\alpha$. The operator is **elliptic** if this left multiplication is invertible for every $\xi \neq 0$.

**Proposition (symbol invertibility).** For every real $\xi = (\xi_0, \dots, \xi_{m-1}) \neq 0$, the element

$$
\sigma = \sum_\alpha B_\alpha \xi_\alpha = \xi_0 + \sum_{k \geq 1} B_k\xi_k
$$

satisfies $\sigma(\xi_0 - \sum_{k\geq1}B_k\xi_k) = |\xi|^2 = (\xi_0 - \sum_{k\geq1}B_k\xi_k)\sigma$, where $|\xi|^2 = \sum_\alpha \xi_\alpha^2 > 0$. Hence $\sigma$ is a unit of $A$, with

$$
\sigma^{-1} = \frac{\xi_0 - \sum_{k\geq1}B_k\xi_k}{|\xi|^2},
$$

and $D$ is elliptic.

*Proof.* The product is computed as in the factorisation of the Laplacian of *Hypercomplex Analysis*:

$$
\Bigl(\xi_0 + \sum_k B_k\xi_k\Bigr)\Bigl(\xi_0 - \sum_j B_j\xi_j\Bigr) = \xi_0^2 - \sum_{j,k}B_jB_k\xi_j\xi_k = \xi_0^2 + \sum_k\xi_k^2 = |\xi|^2,
$$

using $B_k^2 = -1$ and $B_jB_k = -B_kB_j$; the two factors commute because $\xi_0$ is a real scalar and $B_k\xi_0 = \xi_0 B_k$. The same computation in the other order gives the same result. Since $|\xi|^2$ is a nonzero real number, it is a unit of $A$, and the displayed expression is the inverse. $\square$

**Corollary.** The symbol $\sigma_D$ is invertible for every nonzero covector, so $D$ is a first-order elliptic operator with constant coefficients on $\mathbb{R}^m$; in particular the Laplace-type operators $D\bar D$ and $\bar D D$ are the Laplacian.

Ellipticity is exactly the property that makes the Cauchy–Riemann operator behave like the complex operator $\partial_0 + i\partial_1$ rather than like an arbitrary first-order system: it forces the solutions to be as regular as the coefficients, and it produces the integral representation of the next section.

## The Generalised Cauchy–Riemann Equations

Write the coefficients in the basis, $B_\alpha = \sum_{\gamma} b^{\gamma}_{\alpha} e_\gamma$, and write $f = \sum_\delta f^\delta e_\delta$ with component functions $f^\delta : \Omega \to \mathbb{R}$. Then

$$
Df = \sum_{\alpha,\gamma,\delta} b^{\gamma}_{\alpha} \bigl(\partial_\alpha f^\delta\bigr)\, e_\gamma e_\delta,
$$

and expanding $e_\gamma e_\delta = \sum_\varepsilon c^{\varepsilon}_{\gamma\delta} e_\varepsilon$ in the structure constants $c^{\varepsilon}_{\gamma\delta}$ of $A$ gives

$$
Df = \sum_\varepsilon \Bigl(\sum_{\alpha,\gamma,\delta} b^\gamma_\alpha c^\varepsilon_{\gamma\delta} \,\partial_\alpha f^\delta\Bigr) e_\varepsilon.
$$

**Proposition (the Cauchy–Riemann equations).** The equation $Df = 0$ is equivalent to the system of $m$ real first-order partial differential equations with constant coefficients

$$
\sum_{\delta=0}^{m-1} L^{\varepsilon}_{\delta}(\partial)\, f^\delta = 0, \qquad \varepsilon = 0, \dots, m-1,
$$

where $L^{\varepsilon}_{\delta}(\partial) = \sum_{\alpha,\gamma} b^{\gamma}_{\alpha} c^{\varepsilon}_{\gamma\delta} \partial_\alpha$ is a first-order scalar differential operator. For $A = \mathbb{C}$ and $D = \partial_0 + i\partial_1$ this system is the pair of Cauchy–Riemann equations; for $A = \mathbb{H}$ and the Fueter operator it is the quaternionic Cauchy–Riemann system.

The system has as many equations as unknowns, but it is not a determined system in the classical sense: its symbol is a multiplication operator in the algebra, and for a non-commutative $A$ the components are coupled in a way that no single scalar equation captures. The correct invariant of the system is the operator $D$, and the correct notion of regularity is $Df = 0$.

**Remark (overdeterminedness).** For $A = \mathbb{C}$ the Cauchy–Riemann system is a determined elliptic system and the regular functions are exactly the holomorphic functions, a class closed under composition and taking inverses. For $A = \mathbb{H}$ the system is elliptic but the class of regular functions is much smaller in some respects — it is not closed under products, as *Hypercomplex Analysis* shows — and much larger in others, since the kernel of $D$ is infinite-dimensional. Ellipticity controls smoothness and the integral representation; it does not make the non-commutative theory a second copy of complex analysis.

## Left Regularity and Right Regularity

The equation $Df = 0$ uses left multiplication of the values by the coefficients. Since $A$ is not commutative in general, the equation $fD = 0$ with right multiplication,

$$
fD = \sum_{\alpha=0}^{m-1} \partial_\alpha f\, B_\alpha,
$$

defines a different class of functions, the **right regular** functions. The two classes are exchanged by an anti-automorphism.

**Theorem (conjugation exchanges the sides).** Suppose $\rho : A \to A$ is an involutive anti-automorphism — an $\mathbb{R}$-linear bijection with $\rho(xy) = \rho(y)\rho(x)$ and $\rho^2 = \mathrm{id}$ — and set $\bar D = \sum_\alpha \rho(B_\alpha)\partial_\alpha$. Then $f$ is left $D$-regular if and only if $\rho \circ f$ is right $\bar D$-regular.

*Proof.* For a differentiable $f$ and a fixed index $\alpha$, linearity of $\rho$ gives $\partial_\alpha(\rho \circ f) = \rho \circ (\partial_\alpha f)$. Hence

$$
(\rho \circ f)\bar D = \sum_\alpha \partial_\alpha(\rho\circ f)\,\rho(B_\alpha) = \sum_\alpha \rho(\partial_\alpha f)\,\rho(B_\alpha) = \rho\Bigl(\sum_\alpha B_\alpha \partial_\alpha f\Bigr) = \rho(Df),
$$

using the anti-automorphism property $\rho(u)\rho(v) = \rho(vu)$ with $u = \partial_\alpha f$ and $v = B_\alpha$, and linearity for the sum. This vanishes if and only if $Df$ does. $\square$

With $\rho$ the principal conjugation of a Clifford-type system, $\rho(B_k) = -B_k$ for $k \geq 1$ and $\rho(1) = 1$, so $\bar D = \partial_0 - \sum_k B_k\partial_k$ is the conjugate operator of *Hypercomplex Analysis*, and the theorem says that conjugation converts left regularity into right regularity. When $A$ is commutative, left and right regularity coincide, and the distinction disappears.

**Example.** For $A = \mathbb{C}$, conjugation $\rho(z) = \bar z$ gives $\bar D = \partial_0 - i\partial_1$, and the theorem says that $f$ is holomorphic if and only if $\bar f$ is regular for $\bar D$, the usual reflection principle. For $A = \mathbb{H}$ it says that conjugation of a left monogenic function is right monogenic, a standard fact of quaternion analysis.

## Consequences of Ellipticity

**Theorem (Weyl lemma).** Let $f$ be locally integrable on an open set $\Omega$ and suppose $Df = 0$ in the sense of distributions. Then $f$ agrees almost everywhere with a smooth, indeed real-analytic, left regular function on $\Omega$.

*Proof.* The operator $D$ is elliptic with constant coefficients by the symbol computation, and elliptic regularity gives that any distributional solution is smooth; analytic hypoellipticity of elliptic operators upgrades this to real-analyticity. The equation then holds classically. $\square$

**Corollary (unique continuation and identity theorem).** If a left regular function vanishes on an open subset of a connected domain $\Omega$, it vanishes on all of $\Omega$; more generally, two left regular functions that agree on a set with an accumulation point in $\Omega$ agree on $\Omega$.

*Proof.* Smoothness and real-analyticity from the Weyl lemma, applied on a connected domain. $\square$

**Proposition (the kernel of $D$ and of $\Delta$).** Every left regular function is harmonic: $\ker D \subseteq \ker\Delta$, componentwise. Consequently the components of a regular function satisfy the classical maximum principle, mean value property and Liouville theorem for harmonic functions.

*Proof.* If $Df = 0$ then $\Delta f = \bar D D f = 0$ by the factorisation. $\square$

**Proposition (the kernel is infinite-dimensional).** Let $m = \dim_\mathbb{R} A$. If $m \geq 2$, then on every nonempty open set $\Omega \subseteq A$ the space of left regular functions is infinite-dimensional. If $m = 1$, so that $A = \mathbb{R}$ and $D = d/dx$, the left regular functions are exactly the constants.

*Proof.* The case $m = 1$ is immediate: $A = \mathbb{R}$, $D = d/dx_0$, and the regular functions are the constants. Let $m \geq 2$. Since $B_1^2 = -1$, the subalgebra $C = \mathbb{R}[B_1]$ is a copy of $\mathbb{C}$, and the element $z = x_0 + B_1x_1$ satisfies

$$
\partial_0 z = 1, \qquad \partial_1 z = B_1, \qquad zB_1 = B_1z, \qquad Dz = 1 + B_1^2 = 0 .
$$

For $n \geq 0$ and $a \in A$ the function $x \mapsto z^na$ therefore satisfies

$$
D(z^na) = nz^{n-1}a + B_1\,nz^{n-1}B_1a = nz^{n-1}\bigl(1+B_1^2\bigr)a = 0,
$$

using $\partial_0 z^n = nz^{n-1}$, $\partial_1z^n = nz^{n-1}B_1$ and the centrality of $B_1$ in $C$. The functions $z^na$, $n \geq 0$, are linearly independent for $a \neq 0$, because their Taylor expansions at the origin have distinct lowest-degree terms; restricting them to a ball about the origin, and then to a ball about any other point by translating the variable, gives an infinite linearly independent family of left regular functions on every nonempty open $\Omega$. $\square$

**Remark (plane waves).** The infinite dimensionality is also visible through plane waves, the standard mechanism for a constant-coefficient operator whose symbol is not injective over $\mathbb{C}$. Complexify the coefficients: for $\zeta \in \mathbb{C}^m$ the symbol element $\sigma(\zeta) = \sum_\alpha B_\alpha\zeta_\alpha$ and its conjugate $\tilde\sigma(\zeta) = \zeta_0 - \sum_kB_k\zeta_k$ satisfy

$$
\sigma(\zeta)\,\tilde\sigma(\zeta) = \sum_\alpha\zeta_\alpha^2,
$$

the complex scalars being central in $A_\mathbb{C} = A\otimes_\mathbb{R}\mathbb{C}$ and therefore commuting with the $B_k$. If $\zeta \neq 0$ is isotropic, $\sum_\alpha\zeta_\alpha^2 = 0$, then $\sigma(\zeta)$ and $\tilde\sigma(\zeta)$ are both nonzero — separating real and imaginary parts reduces $\sigma(\zeta) = 0$ to $\zeta = 0$ by the symbol computation — so $\sigma(\zeta)$ is a zero divisor of $A_\mathbb{C}$, and

$$
x \longmapsto e^{\langle\zeta,x\rangle}\,\tilde\sigma(\zeta)
$$

is a $D$-regular $A_\mathbb{C}$-valued function that does not vanish at the origin. Its real and imaginary parts are real $D$-regular functions, at least one of them nonzero, since $D$ has real coefficients and $A \cap iA = 0$ in $A_\mathbb{C}$. For $m = 2$ the covectors $\zeta(\lambda) = \lambda(i,1)$, $\lambda \in \mathbb{R}$, are isotropic and $\sigma(\zeta(\lambda)) = \lambda(i+B_1)$ annihilates $v+iB_1v$ for every $v \in A$, so the real part

$$
x \longmapsto e^{\lambda x_1}\bigl(\cos(\lambda x_0)\,v - \sin(\lambda x_0)\,B_1v\bigr)
$$

is left regular for every $v \neq 0$, and distinct $\lambda$ give linearly independent functions. The isotropic family $\zeta(\theta) = (i,\cos\theta,\sin\theta,0,\dots,0)$ is the higher-dimensional analogue of this family.

**Remark.** The last statement is the qualitative reason the theory is rich: ellipticity together with the Cauchy formula makes the solution space large, while non-commutativity prevents it from being an algebra. The particular dimensions and bases of the solution spaces are properties of the individual systems.

**Remark (the hypotheses are not removable).** The consequences above use ellipticity, and so ultimately the relations $B_k^2 = -1$ on the coefficients. For the systems whose natural generator squares to $+1$ or to $0$ the conclusions fail, and the reason is visible in the symbol: for $\mathbb{D}$ with $D = \partial_0 + j\partial_1$ one has $\sigma(\xi)\tilde\sigma(\xi) = \xi_0^2 - \xi_1^2$, which vanishes on the two real lines $\xi_0 = \pm\xi_1$, so no component need be harmonic. In the characteristic coordinates $\xi_\pm = x_0 \pm x_1$ one has $D = 2(e_+\partial_+ + e_-\partial_-)$, so a left regular function has the form $f = f_+(\xi_-)e_+ + f_-(\xi_+)e_-$ with $f_\pm$ arbitrary differentiable functions of one real variable (*Hypercomplex Analysis*, §The Obstructions). The components then satisfy the wave equation rather than Laplace's equation: writing $u = \tfrac12(f_+ + f_-)$ one computes $\partial_0^2u = \tfrac12(f_+'' + f_-'') = \partial_1^2u$. Accordingly:

- **Liouville fails.** The bounded non-constant function $e^{-(x_0 - jx_1)^2}$ is left regular on all of $\mathbb{D}$.
- **The maximum principle fails.** Its Euclidean norm satisfies $\|e^{-(x_0-jx_1)^2}\| \leq 1 = \|f(0)\|$, so the maximum is attained at the interior point $0$.
- **The mean value property fails.** The regular function $x \mapsto \xi_-^2e_+$ has value $0$ at the centre of $B(0,r)$, while its average over the ball is $\frac{1}{\pi r^2}\int_{B(0,r)}(x_0-x_1)^2\,dx = \tfrac{r^2}{2} \neq 0$.

For $\mathbb{D}'$ with $D = \partial_0 + \varepsilon\partial_1$ the symbol satisfies $\sigma(\xi)\tilde\sigma(\xi) = \xi_0^2$, vanishing on $\xi_0 = 0$; the regular functions are $f = u(x_1) + \varepsilon v(x_0,x_1)$ with $\partial_0v = -u'$, the components satisfy the transport equations $\partial_0u = 0$ and $\partial_0v = -\partial_1u$, and the bounded non-constant regular function $1 + \varepsilon e^{-x_1^2}$ again defeats Liouville, its norm attaining its maximum along the line $x_1 = 0$. The two degenerate systems are therefore not covered by the theorems of this section, and they are treated by the idempotent and nilpotent methods and *Dual Numbers Analysis*.

## The Fischer and Stokes Decompositions

The ellipticity of $D$ also organises the polynomials, and the decomposition it produces is the algebraic source of the spherical harmonics and spherical monogenics that appear in the integral representation.

**Notation.** Let $\mathcal{P}_k$ be the real vector space of $A$-valued homogeneous polynomials of degree $k$ in $x_0,\dots,x_{m-1}$, of dimension $m\binom{m+k-1}{k}$, and let

$$
\mathcal{H}_k = \{P \in \mathcal{P}_k : \Delta P = 0\}, \qquad \mathcal{M}_k = \{P \in \mathcal{P}_k : DP = 0\}
$$

be the **harmonic** and the **left regular** (or **monogenic**) homogeneous polynomials of degree $k$; the space $\mathcal{M}_k$ is the space written $\mathcal{M}_k(A,D)$.

**Lemma (Fischer).** For $k \geq 2$ the Laplacian $\Delta : \mathcal{P}_k \to \mathcal{P}_{k-2}$ is surjective, and the multiplication map $\Lambda : \mathcal{P}_{k-2} \to \mathcal{P}_k$, $Q \mapsto |x|^2Q$, is injective with image meeting $\mathcal{H}_k$ only at $0$.

*Proof.* For $Q \in \mathcal{P}_{k-2}$ the product rule for the Laplacian gives

$$
\Delta(|x|^2Q) = (\Delta|x|^2)Q + 2\sum_j x_j\,\partial_jQ + |x|^2\Delta Q = 2mQ + 4(k-2)Q + |x|^2\Delta Q,
$$

using $\Delta|x|^2 = 2m$ and Euler's identity $\sum_j x_j\partial_jQ = (k-2)Q$. Write $T = \lambda\,\mathrm{id} + |x|^2\Delta$ with $\lambda = 2m + 4(k-2) > 0$. Since $\Delta$ lowers degree by two, the operator $|x|^2\Delta$ satisfies $(|x|^2\Delta)^r = |x|^{2r}\Delta^r$, which is zero as soon as $2r > k-2$; hence $|x|^2\Delta$ is nilpotent on $\mathcal{P}_{k-2}$ and $T$ is invertible, with inverse a finite geometric series in $|x|^2\Delta$. For any $R \in \mathcal{P}_{k-2}$ the element $P = |x|^2T^{-1}R$ therefore satisfies $\Delta P = T T^{-1}R = R$, so $\Delta$ is surjective. Moreover $|x|^2Q \in \mathcal{H}_k$ forces $TQ = 0$, hence $Q = 0$, so the image meets $\mathcal{H}_k$ trivially. $\square$

**Theorem (Fischer decomposition; the Stokes decomposition).** For every $k \geq 0$,

$$
\mathcal{P}_k = \mathcal{H}_k \oplus |x|^2\mathcal{P}_{k-2} = \bigoplus_{j \geq 0}|x|^{2j}\mathcal{H}_{k-2j},
$$

and the expansion $P = \sum_j |x|^{2j}h_j$ with $h_j \in \mathcal{H}_{k-2j}$ is unique. In particular every $A$-valued polynomial on $A$ has a unique expansion as a sum of harmonic layers in the radial direction.

*Proof.* By the lemma, $\Delta : \mathcal{P}_k \to \mathcal{P}_{k-2}$ is surjective with kernel $\mathcal{H}_k$, so $\dim\mathcal{H}_k = \dim\mathcal{P}_k - \dim\mathcal{P}_{k-2}$; the image $|x|^2\mathcal{P}_{k-2}$ has dimension $\dim\mathcal{P}_{k-2}$ and meets $\mathcal{H}_k$ trivially, so the two summands are complementary and $\mathcal{P}_k = \mathcal{H}_k \oplus |x|^2\mathcal{P}_{k-2}$. Applying the same statement to $\mathcal{P}_{k-2}, \mathcal{P}_{k-4}, \dots$ gives the iterated form. $\square$

This is the classical decomposition of a homogeneous polynomial into harmonic layers, found by Stokes for the sphere and rediscovered by Fischer in the algebraic setting; it is the statement that the harmonic polynomials of all degrees, multiplied by the radial factors $|x|^{2j}$, exhaust the polynomials, and it reduces the theory of spherical harmonics to the linear algebra of the spaces $\mathcal{H}_k$.

**Theorem (the monogenic refinement, standard).** With $\mathcal{M}_k$ the left regular homogeneous polynomials,

$$
\mathcal{P}_k = \bigoplus_{j=0}^{k} x^j\,\mathcal{M}_{k-j},
$$

where $x^j$ denotes multiplication by the $j$-th power of the variable. This is the Fischer decomposition of Clifford analysis; it is proved by the same triangular argument with the Cauchy–Riemann operator in place of the Laplacian, and it is standard.

**Example (the complex case).** For $A = \mathbb{C}$ and $D = \partial_0 + i\partial_1$ the regular homogeneous polynomials of degree $j$ are $\mathcal{M}_j = \{az^j : a \in \mathbb{C}\}$, so $x^j\mathcal{M}_{k-j}$ is spanned by $x^jz^{k-j}$ and $ix^jz^{k-j}$. Writing $x = \tfrac12(z+\bar z)$, the element $x^jz^{k-j}$ has $\bar z$-degree at most $j$, and the term $\bar z^{\,j}$ occurs only in $x^jz^{k-j}$; the triangular form of the expansions therefore shows that the $2(k+1)$ generators are independent and that their span is $\mathcal{P}_k$, whose complex dimension is $k+1$. This is the elementary verification of the refinement in the one case where every term is explicit.

## Divergence Form, the Cauchy Kernel and Green's Identities

Because the coefficients of $D$ are constant,

$$
D f = \sum_{\alpha=0}^{m-1} B_\alpha \,\partial_\alpha f = \sum_{\alpha=0}^{m-1} \partial_\alpha \bigl(B_\alpha f\bigr),
$$

so $D$ is the **divergence** of the $A$-valued vector field with components $B_\alpha f$ on $\mathbb{R}^m$. This is the form in which the divergence theorem applies.

**Definition.** For a domain $\Omega$ with smooth boundary and outward unit normal $\nu = (\nu_0, \dots, \nu_{m-1})$, the **conormal element** is

$$
\nu_B = \sum_{\alpha=0}^{m-1} \nu_\alpha B_\alpha \in A.
$$

**Theorem (Cauchy–Goursat).** Let $f$ be left regular and of class $C^1$ on a bounded domain $\Omega$ with smooth boundary. Then

$$
\int_{\partial\Omega} \nu_B(y)\, f(y)\, dS(y) = 0.
$$

*Proof.* The divergence theorem applied to the vector field with components $B_\alpha f$ on $\Omega$ gives

$$
\int_{\partial\Omega} \sum_\alpha \nu_\alpha B_\alpha f\, dS = \int_\Omega \sum_\alpha \partial_\alpha(B_\alpha f)\, dy = \int_\Omega Df\, dy = 0,
$$

using the divergence form of $D$ and $\partial_\alpha(B_\alpha f) = B_\alpha \partial_\alpha f$ because $B_\alpha$ is constant. $\square$

**Theorem (a fundamental solution from the Laplacian).** Let $\Phi$ be a fundamental solution of the Laplacian on $\mathbb{R}^m$, so that $\Delta \Phi = \delta_0$ in the sense of distributions. Then

$$
E = \bar D \Phi = \partial_0 \Phi - \sum_{k\geq1} B_k\,\partial_k \Phi
$$

satisfies $D E = \delta_0$; thus $E$ is a fundamental solution of $D$, and $E(x - y)$ is a Cauchy kernel.

*Proof.* Since $D\bar D = \Delta$ and the coefficients are constant, $D E = D\bar D \Phi = \Delta \Phi = \delta_0$, the operators acting on distributions by differentiation. $\square$

**Theorem (Cauchy–Pompeiu, derived from the divergence theorem).** Let $E$ be a fundamental solution of $D$ as above and let $\Omega \subseteq A$ be a bounded domain with smooth boundary. Then for $f$ of class $C^1$ on $\bar\Omega$ and $x \in \Omega$,

$$
f(x) = \int_{\partial\Omega} E(x-y)\,\nu_B(y)\,f(y)\,dS(y) - \int_{\Omega} E(x-y)\,(Df)(y)\,dy,
$$

with the normalisation of $E$ chosen so that the signs are as displayed.

*Proof (outline).* Fix $x \in \Omega$ and apply the divergence theorem to the vector field with components $B_\alpha\,E(x-\cdot)f$ on the punctured domain $\Omega \setminus \overline{B(x,\epsilon)}$. The divergence is

$$
\sum_\alpha \partial_\alpha\bigl(B_\alpha E(x-y)f(y)\bigr) = \bigl(D_y E(x-y)\bigr) f(y) + \sum_\alpha B_\alpha E(x-y)\,\partial_\alpha f(y),
$$

and $D_y E(x-y) = -(DE)(x-y) = -\delta_x(y)$ by translation invariance and the evenness of $\delta_0$. Integrating, letting $\epsilon \to 0$ and using that the small sphere around $x$ contributes $f(x)$ in the limit gives the stated formula. $\square$

**Corollary (Cauchy integral formula).** For a left regular $f$ the volume term vanishes and the representation becomes purely a boundary integral,

$$
f(x) = \int_{\partial\Omega} E(x-y)\,\nu_B(y)\,f(y)\,dS(y), \qquad x \in \Omega ,
$$

which is the general form of the Cauchy integral formula stated in *Hypercomplex Analysis*; the derivation above exhibits it as the case $Df = 0$ of the divergence theorem for $D$. Read through the operator, the formula says three things that its statement alone does not: the kernel is obtained from a fundamental solution of the Laplacian by applying the conjugate operator, $E = \bar D\Phi$, and it is a fundamental solution of $D$ itself, $DE = \delta_0$; ellipticity is exactly what supplies one, so no separate existence hypothesis is needed; and the one-sidedness of the product fixes the position of $E$ in the integrand, on the left for left regular $f$ and on the right for right regular $f$, with the order of the remaining factors reversed.

**Remark (the hypotheses in operator terms).** Relative to the classical Cauchy formula, which asks for holomorphy on a simply connected domain, the hypotheses here are those the divergence theorem needs for $D$: a bounded domain with a sufficiently smooth oriented boundary, so that $\nu_B$ and $dS$ are defined; $f$ of class $C^1$ on the closure $\bar\Omega$; and, when $A$ has zero divisors, a boundary that avoids the set on which the kernel is undefined, since $E$ is built from the inverse of $\bar x$ up to a scalar. Simply connectedness is not required, and the classical case is recovered for $A = \mathbb{C}$ with $D = \partial_0 + i\partial_1$, where $\partial\Omega$ is a closed contour traversed once and $E(z) = 1/(2\pi z)$.

## Change of Operator

**Proposition (equivalence of operators).** Let $u \in A^\times$ be a constant unit and let $D' = uD$, that is, $D'f = u\,(Df)$. Then $f$ is $D'$-regular if and only if $f$ is $D$-regular. More generally, if $D' = D + $ (a zeroth-order term) then the regular functions need not coincide, and the zeroth-order term changes the class.

*Proof.* If $u$ is a unit then $u(Df) = 0$ if and only if $Df = 0$. The second statement is immediate from an example: adding a constant multiple of the identity changes $Df = 0$ into a first-order system with a potential term. $\square$

**Proposition (characterisation of the operator by its kernel, locally).** Two first-order operators with the same leading-order symbol and the same kernel on a connected domain differ by a zeroth-order term whose action on the kernel vanishes. In particular a constant-coefficient operator is determined by its leading symbol up to a zeroth-order perturbation, and among operators with the same symbol, the elliptic ones all have kernels containing the constants.

*Proof.* If $D$ and $D'$ have the same leading symbol then $D' - D$ is a zeroth-order operator, that is, multiplication by a constant $c \in A$ (in the constant-coefficient case); $D'f = 0$ and $Df = 0$ coincide on the common kernel exactly when $cf = 0$ there. The last statement follows from $D(1) = 0$ for an operator with $B_0 = 1$. $\square$

**Definition.** Two hypercomplex systems $(A,D)$ and $(A',D')$ are **equivalent** if there is an algebra isomorphism $\phi : A \to A'$ carrying the coefficients of $D$ to those of $D'$, $\phi(B_\alpha) = B'_\alpha$. Equivalent systems have isomorphic spaces of regular functions, by the proposition on the action of the automorphism group in *Hypercomplex Analysis*.

The classification of admissible operators up to this equivalence, and the determination of which finite-dimensional algebras carry one, is the general structural problem of hypercomplex analysis. A necessary condition is that $A$ contain elements $B_1, \dots, B_{m-1}$ with $B_k^2 = -1$ and $B_jB_k = -B_kB_j$, that is, a Clifford subalgebra; this is why the systems of the following categories are the Clifford-type ones.

## Summary

The **generalised Cauchy–Riemann operator** $D = \partial_0 + \sum_k B_k\partial_k$ has principal symbol equal to left multiplication by $\sigma(\xi) = \xi_0 + \sum_k B_k\xi_k$. When the coefficients satisfy the Clifford relations $B_jB_k + B_kB_j = -2\delta_{jk}$ with $B_k^2 = -1$, this element is a unit for every nonzero $\xi$, with inverse $(\xi_0 - \sum_k B_k\xi_k)/|\xi|^2$; hence $D$ is elliptic, and the equation $Df = 0$ is the generalised Cauchy–Riemann system, a first-order system of $m$ equations in $m$ unknown components with constant coefficients, reducing to the classical Cauchy–Riemann equations when $A = \mathbb{C}$.

Left regularity $Df = 0$ and right regularity $fD = 0$ are distinct for non-commutative $A$ and are exchanged by an involutive anti-automorphism $\rho$ with $\rho(B_\alpha) = \bar B_\alpha$: $f$ is left $D$-regular if and only if $\rho \circ f$ is right $\bar D$-regular. Ellipticity gives the Weyl lemma, hence smoothness and real-analyticity of regular functions, the identity theorem and unique continuation, and the inclusion $\ker D \subseteq \ker\Delta$, so that regular functions are harmonic componentwise; the kernel is infinite-dimensional; and the components inherit the maximum principle, the mean value property and Liouville's theorem. These consequences need the relations $B_k^2 = -1$: for the degenerate systems $\mathbb{D}$ and $\mathbb{D}'$, whose symbols vanish on the real space, the regular functions are $f_+(\xi_-)e_+ + f_-(\xi_+)e_-$ and $u(x_1) + \varepsilon v(x_0,x_1)$ with $\partial_0 v = -u'$, their components satisfy the wave and transport equations rather than Laplace's equation, and Liouville, the maximum principle and the mean value property all fail, the first two defeated by $e^{-(x_0-jx_1)^2}$ on $\mathbb{D}$ and by $1 + \varepsilon e^{-x_1^2}$ on $\mathbb{D}'$.

The integral representation is the divergence theorem for $D$ written in divergence form: the **Cauchy–Pompeiu formula** represents an arbitrary $C^1$ function on a bounded domain with smooth boundary by the boundary integral of the Cauchy kernel against the conormal element plus a volume integral of $Df$, and the **Cauchy integral formula** is the case $Df = 0$, in which the volume term drops. Its hypotheses are those the divergence theorem needs — a bounded domain with smooth boundary, $f$ of class $C^1$ on the closure, a global fundamental solution of the conjugate operator, which exists because $D$ is elliptic — and not the simple connectedness and holomorphy of the classical statement.

The homogeneous polynomials organise under ellipticity through the **Fischer lemma** — the Laplacian $\Delta : \mathcal{P}_k \to \mathcal{P}_{k-2}$ is surjective and $|x|^2\mathcal{P}_{k-2}$ meets $\mathcal{H}_k$ trivially — giving the **Fischer decomposition** $\mathcal{P}_k = \mathcal{H}_k \oplus |x|^2\mathcal{P}_{k-2} = \bigoplus_j |x|^{2j}\mathcal{H}_{k-2j}$, the Stokes decomposition into harmonic layers, and its **monogenic refinement** $\mathcal{P}_k = \bigoplus_{j=0}^k x^j\mathcal{M}_{k-j}$, whose summands are the spaces $\mathcal{M}_{k-j}(A,D)$ of solid spherical monogenics. Operators differing by a constant unit have the same regular functions, while a zeroth-order term changes the class; equivalent systems differ by an algebra isomorphism carrying coefficients to coefficients, and the existence of an admissible operator requires a Clifford subalgebra of $A$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | Finite-dimensional unital associative real algebra, $\dim_\mathbb{R} A = m$ |
| $e_0 = 1, \dots, e_{m-1}$ | Fixed basis of $A$ |
| $B_k$ | Coefficients of $D$, with $B_jB_k + B_kB_j = -2\delta_{jk}$ |
| $D = \partial_0 + \sum_k B_k\partial_k$ | Generalised Cauchy–Riemann operator |
| $\bar D = \partial_0 - \sum_k B_k\partial_k$ | Conjugate operator |
| $\sigma(\xi) = \sum_\alpha B_\alpha\xi_\alpha$ | Principal symbol |
| $\tilde\sigma(\xi) = \xi_0 - \sum_k B_k\xi_k$ | Reflected symbol, $\sigma\tilde\sigma = \sum_\alpha\xi_\alpha^2$ |
| $|\xi|^2 = \sum_\alpha \xi_\alpha^2$ | Euclidean squared norm of the covector |
| $c^\varepsilon_{\gamma\delta}$ | Structure constants of $A$ |
| $Df = 0$ | Left regularity |
| $fD = 0$ | Right regularity |
| $(1, B_1, \dots, B_{m-1})$ | Frame of the system |
| $\nu_B = \sum_\alpha \nu_\alpha B_\alpha$ | Conormal element of a boundary |
| $\partial\Omega, dS$ | Boundary of a domain, surface measure |
| $f(x) = \int_{\partial\Omega} E(x-y)\nu_B(y)f(y)dS(y)$ | Cauchy integral formula for left regular $f$ |
| $\Phi$ | Fundamental solution of the Laplacian, $\Delta\Phi = \delta_0$ |
| $E = \bar D\Phi$ | Fundamental solution of $D$ built from $\Phi$ |
| $\rho$ | Involutive anti-automorphism exchanging the sides |
| $\Delta$ | Laplacian, $D\bar D = \bar D D = \Delta$ |
| $(A,D) \sim (A',D')$ | Equivalence of hypercomplex systems |
| $\mathcal{P}_k$ | $A$-valued homogeneous polynomials of degree $k$ |
| $\mathcal{H}_k = \ker\Delta \cap \mathcal{P}_k$ | Harmonic homogeneous polynomials |
| $\mathcal{M}_k = \ker D \cap \mathcal{P}_k$ | Left regular homogeneous polynomials, $= \mathcal{M}_k(A,D)$ |
| $e_\pm = \tfrac12(1 \pm j)$, $\xi_\pm = x_0 \pm x_1$ | Idempotents and characteristic coordinates of $\mathbb{D}$ |



## Further Reading

- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the elliptic theory of the Cauchy–Riemann operator.
- R. Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for left and right regularity and the role of conjugation.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* (Springer, 2nd ed. 1990), for ellipticity, the symbol and Weyl's lemma.
- Michael E. Taylor, *Partial Differential Equations I* (Springer, 2nd ed. 2011), for the general theory of first-order elliptic systems.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the explicit Cauchy–Riemann systems.
- John Ryan (ed.), *Clifford Algebras in Analysis and Related Topics* (CRC Press, 1996), for further structural results on regular functions.
