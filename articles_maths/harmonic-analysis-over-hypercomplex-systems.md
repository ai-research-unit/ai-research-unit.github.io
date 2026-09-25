
# __Harmonic Analysis over Hypercomplex Systems__

## Introduction

Harmonic analysis over a hypercomplex system means the analysis of functions on the finite-dimensional algebra $A$ that exploits two structures simultaneously: the abelian group structure underlying the addition of $A \cong \mathbb{R}^m$, which carries the Euclidean Fourier transform, and the subspace of regular functions defined by the Cauchy–Riemann operator $D$, which carries the Cauchy kernel and the Cauchy transform. The two are tied together by the symbol of $D$: on the Fourier side, differentiation becomes multiplication by the symbol, so the regularity condition becomes an algebraic condition on the Fourier transform, and the class of regular functions is described by the characteristic variety of the operator.

This is the general method. The explicit transforms, reproducing kernels, bases of spherical monogenics and $L^2$ decompositions of the particular systems — the complex numbers, the quaternions, the split and dual and biquaternion systems — are worked out in categories 26 to 29, and they are not repeated here. What is common to them is the shape of the analysis, and it is that shape that this article fixes. Throughout, $(A,D)$ is an elliptic hypercomplex system in the sense of *Hypercomplex Analysis*: $A$ is finite-dimensional of dimension $m$ over $\mathbb{R}$, with basis $e_0 = 1, \dots, e_{m-1}$, and

$$
D = \partial_0 + \sum_{k\geq1} B_k\partial_k, \qquad \sigma(\xi) = \xi_0 + \sum_{k\geq1} B_k\xi_k, \qquad D\bar D = \bar D D = \Delta,
$$

with $B_jB_k + B_kB_j = -2\delta_{jk}$, $B_k^2 = -1$. The symbol $\sigma(\xi)$ and its reflected companion $\tilde\sigma(\xi)$ are those of *Regularity and the Cauchy–Riemann Operator*, and $E$ is a fundamental solution of $D$.

## The Additive Fourier Transform

The additive group of $A$ is $\mathbb{R}^m$ through the fixed basis, and the real inner product $\langle \xi, x\rangle = \sum_\alpha \xi_\alpha x_\alpha$ identifies the dual of $A$ with $A$ itself. All functions in this section are complex-valued or $A$-valued and integrable as appropriate; the transform is taken componentwise.

**Definition.** For $f \in L^1(A)$, the **Fourier transform** is

$$
\hat f(\xi) = \int_A f(x)\, e^{-i\langle\xi, x\rangle}\, dx,
$$

and the inverse transform on a suitable Schwartz space is

$$
f(x) = \frac{1}{(2\pi)^m} \int_A \hat f(\xi)\, e^{\,i\langle\xi, x\rangle}\, d\xi.
$$

For $A$-valued $f$ the transform is $A$-valued, the exponentials being scalar-valued.

**Theorem (basic properties).** The Fourier transform extends to a unitary equivalence of $L^2(A)$ with itself up to the factor $(2\pi)^{-m/2}$ (Plancherel); it interchanges differentiation and multiplication by the coordinate,

$$
\widehat{\partial_\alpha f}(\xi) = i\,\xi_\alpha \,\hat f(\xi);
$$

and it turns the convolution

$$
(f * g)(x) = \int_A f(x-y)\,g(y)\,dy
$$

into the pointwise product with respect to the algebra multiplication of $A$,

$$
\widehat{(f * g)}(\xi) = \hat f(\xi)\,\hat g(\xi).
$$

*Proof.* These are the standard properties of the Euclidean Fourier transform, applied componentwise; for the last, substitute $x = u + y$ and use $\langle \xi, u+y\rangle = \langle\xi,u\rangle + \langle\xi,y\rangle$. $\square$

The multiplication in the convolution theorem is the multiplication of $A$, so the convolution algebra $\bigl(L^1(A), *\bigr)$ is commutative exactly when $A$ is, and it is the algebra of translation-invariant operators.

**Corollary.** A translation-invariant operator on $A$ is convolution with a distribution, and its Fourier multiplier is an $A$-valued function of $\xi$ acting by left multiplication. In particular $D$ is convolution with the distribution $\sum_\alpha B_\alpha\,\delta^{(\alpha)}$ and has multiplier $i\sigma(\xi)$.

### The Transforms of the Number Systems

The transform above is attached to the additive group $\mathbb{R}^m$, which is the same group for every $A$; hence the operator is literally the same for $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$, $\mathbb{H}$, $\mathbb{H}_{\mathbb{D}}$ and $\mathbb{B}$, and what distinguishes the systems is the algebra in which convolution multiplies and, through it, the symbol. This is the sense in which the transform theory depends on the underlying additive group rather than on the multiplication, and it is the first thing to record about the particular systems.

For a Clifford-type system the identity $\sigma(\xi)\tilde\sigma(\xi) = \sum_\alpha\xi_\alpha^2$ determines where the symbol fails to be invertible: it is invertible for every real $\xi \neq 0$ exactly when the quadratic form $\sum_\alpha\xi_\alpha^2$ is definite, and otherwise the set where it is not invertible is a genuine real variety contained in the isotropic cone. The systems of the corpus fall into the two cases as follows.

| $A$ | $m$ | $\sigma(\xi)$ | $\sigma(\xi)$ invertible iff | Real $\operatorname{Char}(D)$ |
|---|---|---|---|---|
| $\mathbb{C}$ | 2 | $\xi_0 + i\xi_1$ | $\xi \neq 0$ | $\{0\}$, elliptic |
| $\mathbb{D}$ | 2 | $\xi_0 + j\xi_1$ | $\xi_0^2 \neq \xi_1^2$ | the two lines $\xi_0 = \pm\xi_1$ |
| $\mathbb{D}'$ | 2 | $\xi_0 + \varepsilon\xi_1$ | $\xi_0 \neq 0$ | the line $\xi_0 = 0$ |
| $\mathbb{H}$ | 4 | $\xi_0 + e_1\xi_1 + e_2\xi_2 + e_3\xi_3$ | $\xi \neq 0$ | $\{0\}$, elliptic |
| $\mathbb{H}_{\mathbb{D}}$ | 8 | $\xi_0 + e_1\xi_1 + e_2\xi_2 + e_3\xi_3$ | $\xi \neq 0$ | $\{0\}$, elliptic |
| $\mathbb{B}$ | 8 | $\xi_0 + e_1\xi_1 + e_2\xi_2 + e_3\xi_3$ | $\xi \neq 0$ | $\{0\}$, elliptic |

In the last two rows the algebra is eight-dimensional while the operator is built on the four-term quaternion frame $1, e_1, e_2, e_3$; the remaining four real coordinates of the algebra enter the transform as parameters rather than as derivatives, and the ellipticity statement is about the four differentiated directions.

In the four elliptic rows the symbol is invertible off the origin, so a left regular tempered distribution has Fourier transform supported at $\xi = 0$ and is therefore a polynomial, and a compactly supported left regular distribution vanishes — the vanishing theorem of the next section. On the elliptic systems the transform is thus a sharp but restricted tool, and the analysis of regular functions on unbounded domains is carried by the Cauchy representation below instead. In the two degenerate rows the symbol is not invertible on a real set of positive dimension, and the regularity condition becomes a support condition rather than a vanishing one: for $\mathbb{D}$ a left regular function has transform supported on the two lines $\xi_0 = \pm\xi_1$, the value on the line $\xi_0 = \xi_1$ lying in the null line $\mathbb{R}(1-j)$ and the value on the line $\xi_0 = -\xi_1$ in the null line $\mathbb{R}(1+j)$, which is the Fourier-side form of the fact that a regular function depends on one characteristic coordinate; for $\mathbb{D}'$ the transform is supported on the hyperplane $\xi_0 = 0$: writing $\hat f = \hat f_0 + \varepsilon\hat f_1$, the two equations $\xi_0\hat f_0 = 0$ and $\xi_0\hat f_1 + \xi_1\hat f_0 = 0$ force the support into that hyperplane, and there they impose no restriction on the data. Indeed

$$
\hat f_0 = \hat u(\xi_1)\,\delta(\xi_0), \qquad \hat f_1 = -i\,\hat u'(\xi_1)\,\delta'(\xi_0) + \hat w(\xi_1)\,\delta(\xi_0)
$$

solves both equations for arbitrary one-variable distributions $\hat u$ and $\hat w$, the second equation using $\xi_0\delta' = -\delta$ together with the identity $\hat u' = i\xi_1\hat u$; these are the transforms of $f_0 = u(x_1)$ and $f_1 = w(x_1) - x_0u'(x_1)$, up to the normalisation constants of the transform. With $u$ and $w$ arbitrary the space of regular functions is therefore far larger than in the elliptic case. It is exactly this extra freedom that makes the transform useful for the two degenerate systems and sharp but restricted for the elliptic ones.

The explicit transforms, the reproducing kernels and the spherical monogenics of each system, together with the classical Plancherel theory those systems inherit, are developed in the articles of categories 26 to 29; what is recorded here is the shape they share and the rule that decides it, namely that the transform is that of the additive group and that the symbol of $D$ decides which frequencies survive regularity.

## Regularity on the Fourier Side

**Theorem (the Fourier image of the operator).** For a suitable function or distribution $f$,

$$
\widehat{Df}(\xi) = i\,\sigma(\xi)\,\hat f(\xi), \qquad \sigma(\xi) = \xi_0 + \sum_{k\geq1}B_k\xi_k,
$$

the multiplication being left multiplication in $A$. Hence $f$ is left regular if and only if

$$
\sigma(\xi)\,\hat f(\xi) = 0 \qquad \text{for every } \xi.
$$

*Proof.* By linearity and the differentiation rule of the previous theorem,

$$
\widehat{Df} = \sum_\alpha B_\alpha\,\widehat{\partial_\alpha f} = i\sum_\alpha B_\alpha\xi_\alpha \hat f = i\,\sigma(\xi)\hat f. \qquad \square
$$

**Definition.** The **characteristic variety** of $D$ is

$$
\operatorname{Char}(D) = \{\zeta \in \mathbb{C}^m : \sigma(\zeta) \text{ is not invertible in } A_\mathbb{C}\},
$$

where $A_\mathbb{C} = A \otimes_\mathbb{R}\mathbb{C}$ is the complexification.

**Theorem (the characteristic variety of an elliptic system).** For an elliptic hypercomplex system,

$$
\operatorname{Char}(D) = \Bigl\{\zeta \in \mathbb{C}^m : \sum_{\alpha=0}^{m-1}\zeta_\alpha^2 = 0\Bigr\},
$$

the complex isotropic cone. In particular $\operatorname{Char}(D)$ meets the real subspace only at the origin, which is the ellipticity of $D$.

*Proof.* By the symbol computation, $\sigma(\zeta)\,\tilde\sigma(\zeta) = \sum_\alpha\zeta_\alpha^2$ with $\tilde\sigma(\zeta) = \zeta_0 - \sum_kB_k\zeta_k$. If $\sum_\alpha\zeta_\alpha^2 \neq 0$ then $\sigma(\zeta)$ is invertible, with inverse $\tilde\sigma(\zeta)/\sum_\alpha\zeta_\alpha^2$. Conversely, if $\sum_\alpha\zeta_\alpha^2 = 0$ and $\zeta \neq 0$, then $\sigma(\zeta)\tilde\sigma(\zeta) = 0$ with $\tilde\sigma(\zeta) \neq 0$ (if both vanished, then $\zeta_0 = 0$ and $\sum_kB_k\zeta_k = 0$, which forces all $\zeta_\alpha = 0$ by linear independence of the $B_k$, including $B_0 = 1$), so $\sigma(\zeta)$ is a zero divisor and not invertible; at $\zeta = 0$ one has $\sigma(0) = 0$, also not invertible. Hence $\operatorname{Char}(D)$ is exactly the isotropic cone. For real $\zeta$ the equation $\sum_\alpha\zeta_\alpha^2 = 0$ has only the solution $\zeta = 0$, so the characteristic variety meets the real subspace only at the origin. $\square$

The characteristic variety is the same for every Clifford-type system of a given dimension: it depends only on $m$, not on the finer multiplication. This is the Fourier-side explanation of the plane waves constructed in *Regularity and the Cauchy–Riemann Operator*, whose complex frequencies are precisely the points of $\operatorname{Char}(D)$.

**Theorem (exponential representation).** Every distribution solution of $Du = 0$ on a convex domain is the limit, in the distributional sense, of exponential-polynomial solutions $x \mapsto p(x)\,e^{\langle\zeta, x\rangle}$ with $\zeta \in \operatorname{Char}(D)$ and $p$ a polynomial.

*Proof.* This is the Ehrenpreis–Palamodov theorem for constant-coefficient systems: solutions are represented as integrals of exponential solutions over the characteristic variety, and on a convex domain the integral can be approximated by finite combinations. $\square$

**Corollary (no compactly supported regular functions).** If $f$ is left regular on all of $A$ and has compact support, then $f = 0$.

*Proof.* By the Paley–Wiener theorem, the Fourier transform of a compactly supported distribution is an entire function of the complex variable $\zeta \in \mathbb{C}^m$ of exponential type. The equation $\sigma(\zeta)\hat f(\zeta) = 0$, valid for real $\zeta$ and hence, by analyticity, for $\zeta$ in an open set where $\sigma$ is invertible, forces $\hat f$ to vanish on the complement of $\operatorname{Char}(D)$. Since the complement is open and nonempty, $\hat f = 0$ by analytic continuation, and so $f = 0$. $\square$

So the solution space of the Cauchy–Riemann operator consists of functions of slow decay: the exponential representation makes precise the intuitive picture of the previous articles that regular functions are the hypercomplex analogue of entire functions, and it is genuinely a harmonic-analytic statement, depending on the Fourier transform of the operator rather than on its kernel.

## The Fourier Transform of the Cauchy Kernel

**Theorem (Fourier transform of the fundamental solution).** Let $E$ be a fundamental solution of $D$. Then, in the distributional sense,

$$
i\,\sigma(\xi)\,\hat E(\xi) = 1,
$$

so away from the characteristic variety

$$
\hat E(\xi) = \frac{\tilde\sigma(\xi)}{i\sum_\alpha \xi_\alpha^2} = \frac{\xi_0 - \sum_k B_k\xi_k}{i\sum_\alpha\xi_\alpha^2},
$$

a distribution whose singular support is contained in $\operatorname{Char}(D)$.

*Proof.* Fourier transforming $DE = \delta_0$ and using the multiplier rule of the previous section gives $i\sigma(\xi)\hat E(\xi) = \hat\delta_0 = 1$, the identity being the constant function $1$. Multiplying by $\tilde\sigma(\xi)$ and using $\sigma\tilde\sigma = \sum_\alpha\xi_\alpha^2$ gives the displayed expression where $\sum_\alpha\xi_\alpha^2 \neq 0$. $\square$

**Theorem (explicit Cauchy kernel).** Let

$$
\omega_{m-1} = \frac{2\pi^{m/2}}{\Gamma(m/2)}
$$

be the surface area of the unit sphere in $\mathbb{R}^m$, and let $\bar x = x_0 - \sum_{k\geq1}B_kx_k$ be the conjugate of $x$ in the Clifford sense. Then

$$
E(x) = \frac{\bar x}{\omega_{m-1}\,|x|^m}, \qquad x \neq 0,
$$

is a fundamental solution of $D$.

*Proof.* Let $\Phi$ be the fundamental solution of the Laplacian, $\Phi(x) = \frac{1}{(2-m)\omega_{m-1}}|x|^{2-m}$ for $m \geq 3$ and $\Phi(x) = \frac{1}{\omega_1}\log|x|$ for $m = 2$. In both cases $\Delta \Phi = \delta_0$. By the theorem of *Regularity and the Cauchy–Riemann Operator*, $E = \bar D \Phi$ is a fundamental solution of $D$. Now $\partial_\alpha|x|^{2-m} = (2-m)x_\alpha|x|^{-m}$ for $m\neq 2$ and $\partial_\alpha\log|x| = x_\alpha|x|^{-2}$ for $m = 2$; in both cases

$$
\bar D \Phi = \frac{1}{\omega_{m-1}}\sum_{\alpha}\bar B_\alpha\, x_\alpha\,|x|^{-m} = \frac{\bar x}{\omega_{m-1}|x|^m},
$$

where $\bar B_0 = 1$ and $\bar B_k = -B_k$. $\square$

For the complex system ($m = 2$, $\omega_1 = 2\pi$, $\bar x = \bar z$) this is $E(z) = \bar z/(2\pi|z|^2) = 1/(2\pi z)$, the classical Cauchy kernel; for a four-dimensional Clifford system it is $\bar x/(2\pi^2|x|^4)$. The explicit kernels of the individual theories are therefore all one formula, specialised by the conjugation and the dimension, and this is the concrete sense in which the general theory contains the particular ones.

## Spherical Harmonics and the Monogenic Refinement

The Euclidean structure of $A$ gives a second decomposition, that into spherical harmonics, and the Cauchy–Riemann operator cuts it down to the monogenic pieces.

**Theorem (Fischer decomposition; the Stokes decomposition).** Let $\mathcal{P}_\nu$ denote the space of $A$-valued homogeneous polynomials of degree $\nu$ on $A$, and let $\mathcal{H}_\nu \subseteq \mathcal{P}_\nu$ denote the harmonic ones, those annihilated by $\Delta$. Then

$$
\mathcal{P}_\nu = \bigoplus_{j=0}^{\lfloor \nu/2\rfloor} |x|^{2j}\, \mathcal{H}_{\nu-2j},
$$

and

$$
\dim \mathcal{H}_\nu = \binom{\nu + m - 1}{m - 1} - \binom{\nu + m - 3}{m - 1}
$$

for $\nu \geq 2$, with $\dim\mathcal{H}_0 = 1$ and $\dim\mathcal{H}_1 = m$.

*Proof.* The Laplacian maps $\mathcal{P}_\nu$ onto $\mathcal{P}_{\nu-2}$ for $\nu \geq 2$; surjectivity is checked on monomials, and the kernel is $\mathcal{H}_\nu$, giving the splitting $\mathcal{P}_\nu = \mathcal{H}_\nu \oplus |x|^2\mathcal{P}_{\nu-2}$. Iterating gives the direct sum, and the dimension formula follows by induction using $\dim\mathcal{P}_\nu = \binom{\nu+m-1}{m-1}$. $\square$

**Definition.** The **solid spherical monogenics** of degree $\nu$ for $(A,D)$ are the left regular homogeneous polynomials of degree $\nu$,

$$
\mathcal{M}_\nu(A,D) = \mathcal{P}_\nu \cap \ker D .
$$

**Proposition.** Every solid spherical monogenic is harmonic: $\mathcal{M}_\nu \subseteq \mathcal{H}_\nu$. The multiplication map $A \otimes_\mathbb{R} A \to A$ being surjective, one has $\dim \mathcal{M}_1 = m^2 - m$.

*Proof.* Regularity gives $\Delta P = \bar D D P = 0$ for $\Delta$-homogeneous $P$. For the dimension, the linear maps $f : A \to A$ form an $m^2$-dimensional space and $Df = 0$ is the condition that the linear map $\ell(f)$ vanish, where $\ell$ is the composite of the identification of linear maps with $A \otimes A$ and the multiplication $A\otimes A \to A$. This composite is surjective, so its kernel has dimension $m^2 - m$. $\square$

For the complex system this gives $\dim_\mathbb{R}\mathcal{M}_\nu = 2$ for every $\nu$, the space consisting of the maps $x \mapsto a\,x^\nu$ with $a \in \mathbb{C}$, as it must; for a four-dimensional Clifford-type system it gives $\dim\mathcal{M}_1 = 12$, and in general the spaces $\mathcal{M}_\nu$ are the irreducible pieces of the monogenic decomposition, whose explicit bases are computed in the particular theories.

**Theorem (Taylor expansion in solid spherical monogenics).** Let $f$ be left regular on the ball $B(0,R)$. Then $f$ has a unique expansion

$$
f(x) = \sum_{\nu=0}^{\infty} P_\nu(x), \qquad P_\nu \in \mathcal{M}_\nu(A,D),
$$

convergent uniformly on compact subsets of $B(0,R)$.

*Proof.* A regular function is real-analytic, so it has a convergent power series at the origin whose homogeneous parts $P_\nu$ are unique. Since $f$ is regular, $Df = \sum_\nu D P_\nu = 0$, and since $DP_\nu$ is homogeneous of degree $\nu - 1$, the homogeneous parts of distinct degrees are linearly independent; hence $DP_\nu = 0$ for every $\nu$. $\square$

**Theorem (orthogonality on the sphere).** For a Clifford-type system, the spaces of traces $\{P|_{\partial B(0,1)} : P \in \mathcal{M}_\nu\}$ for distinct degrees $\nu$ are mutually orthogonal in $L^2(\partial B(0,1))$ with respect to the surface measure, and their orthogonal sum is dense in the space of square-integrable boundary values of regular functions on the ball.

*Proof.* This is the Fischer decomposition of Clifford analysis: the solid spherical monogenics of different degrees are eigenfunctions of the spherical Cauchy–Riemann operator belonging to different eigenvalues, and eigenfunctions of a self-adjoint operator for distinct eigenvalues are orthogonal. Density follows from the Taylor expansion together with the convergence of the series on the closed ball for functions regular on a neighbourhood of it. $\square$

The theorem is the hypercomplex analogue of the Fourier series: a regular function is built from the monogenic harmonics exactly as a holomorphic function is built from the powers $z^\nu$, and the orthogonality on the sphere is the orthogonality of the trigonometric system.

## The Cauchy Transform as a Projection

The harmonic-analytic content of the Cauchy formula is that the Cauchy transform behaves like a Szegő projection onto the regular functions.

**Definition.** For a bounded domain $\Omega$ with smooth boundary and a boundary datum $h \in L^2(\partial\Omega)$, the **Cauchy transform** is

$$
(\mathcal{C}h)(x) = \int_{\partial\Omega} E(x-y)\, \nu_B(y)\, h(y)\, dS(y), \qquad x \in \Omega .
$$

**Theorem (reproducing property).** Let $f$ be left regular on a neighbourhood of $\bar\Omega$. Then $\mathcal{C}\bigl(f|_{\partial\Omega}\bigr) = f$ on $\Omega$; equivalently, the Cauchy kernel reproduces regular functions,

$$
f(x) = \int_{\partial\Omega} E(x-y)\,\nu_B(y)\,f(y)\,dS(y).
$$

This is the Cauchy integral formula of *Hypercomplex Integration*, reinterpreted as an integral operator with kernel $E(x-y)\nu_B(y)$ acting on boundary data.

**Theorem (the transform is a projection onto regular functions).** The Cauchy transform maps $L^2(\partial\Omega)$ onto the space of regular functions on $\Omega$, and it is the identity on the boundary values of those functions.

*Proof.* Regularity of $\mathcal{C}h$ inside $\Omega$ was proved in *Hypercomplex Integration*, as was the reproducing property. The two statements together say that $\mathcal{C}$ is a projection with image contained in the regular functions and containing them; hence its image is exactly the space of regular functions on $\Omega$. $\square$

**Remark.** The jump formula $\mathcal{C}^+h - \mathcal{C}^-h = h$ of *Hypercomplex Integration* is the statement that the two projections associated with the two sides of the boundary differ by the identity, exactly as the Szegő and Hardy-space projections do for the unit circle in the complex case. The harmonic analysis of a hypercomplex system is thus organised around two decompositions of the same function space: the Fourier decomposition of the translation-invariant side, indexed by the characteristic variety, and the monogenic decomposition of the Cauchy side, indexed by degree and by the symmetry of the system.

## The Other Integral Transforms

The Euclidean Fourier transform is one of a family, and the members of the family are distinguished by the group on which they are taken and by the module structure of $A$, not by the multiplication of $A$: the multiplication enters only through the target, where it makes the convolution algebra non-commutative.

**The Laplace transform.** For an $A$-valued function $f$ whose growth permits it, the **Laplace transform** is

$$
(\mathcal{L}f)(s) = \int_A f(x)\,e^{-\langle s, x\rangle}\,dx, \qquad s \in \mathbb{C}^m,
$$

holomorphic in the tube of convergence and reducing to the Fourier transform on the imaginary axis, $(\mathcal{L}f)(i\xi) = \hat f(\xi)$. The hypercomplex-specific feature is a rigidity on the side of compact support. A compactly supported left regular function on all of $A$ is zero (the corollary above), and more precisely the Fourier transform of a compactly supported $A$-valued distribution is entire of exponential type while the equation $\sigma(\zeta)\hat f(\zeta) = 0$ forces its support into the characteristic variety, so:

**Proposition.** If $f$ is a compactly supported left regular $A$-valued distribution, then $\mathcal{L}f = 0$ identically. Hence the Laplace theory of regular functions is a theory of functions on cones or of exponential growth.

*Proof.* The Fourier transform $\hat f$ is the restriction to $\mathbb{R}^m$ of an entire function of exponential type; the equation $\sigma(\zeta)\hat f(\zeta) = 0$ holds on the open set where $\sigma$ is invertible, hence by analytic continuation on all of $\mathbb{C}^m$ off the complex characteristic variety, so $\hat f$ vanishes on a dense open set and is identically zero. Then $(\mathcal{L}f)(i\xi) = \hat f(\xi) = 0$ for all real $\xi$, and by analyticity $\mathcal{L}f = 0$. $\square$

So the Laplace theory of regular functions is a theory of functions on cones or of exponential growth, and its inversion is the classical contour inversion along a translate of the imaginary axis.

**The Hilbert transform.** On the line the **Hilbert transform** is the principal value integral

$$
(Hf)(x) = \frac{1}{\pi}\,\mathrm{p.v.}\int_\mathbb{R}\frac{f(y)}{x-y}\,dy,
$$

the model singular integral and the boundary operator of the complex Cauchy transform: on the upper half-plane the inside and outside values of the Cauchy transform of a boundary datum $h$ are $\mathcal{C}^\pm h = \pm\tfrac12 h + \tfrac12 Hh$ up to the normalisation of the kernel, which is the classical Plemelj formula. For a hypercomplex system the same object appears with the conormal kernel: the principal value operator on the boundary,

$$
(Sh)(x) = \mathrm{p.v.}\int_{\partial\Omega}E(x-y)\,\nu_B(y)\,h(y)\,dS(y), \qquad x \in \partial\Omega,
$$

is the **Hilbert transform of the system**, and the jump formula of *Hypercomplex Integration* is the statement that the inside and outside Cauchy transforms differ by the identity. On the line the Hilbert transform satisfies $H^2 = -1$ and is an isometry of $L^2$, and its Fourier multiplier is $-i\,\mathrm{sgn}(\xi)$; these are the one-dimensional instances of the general theory below.

**The Mellin transform.** For a function of one positive real variable the **Mellin transform** is

$$
(\mathcal{M}f)(s) = \int_0^\infty f(r)\,r^{s-1}\,dr,
$$

the Fourier transform of the multiplicative group $\mathbb{R}_+$, and it is the transform adapted to the radial variable of $A$. Its infinitesimal generator is the Euler operator $\vartheta = \sum_\alpha x_\alpha\partial_\alpha$, which the Mellin transform converts into the multiplier $s$: a function homogeneous of degree $\lambda$ in the radius is a single Mellin mode, with exponent $\lambda$. This is why the Mellin transform is the natural bookkeeping device for the radial exponents of the theory: the solid spherical monogenics $\mathcal{M}_\nu$ are homogeneous of degree $\nu$, the Fischer decomposition is the statement that the exponents $\nu, \nu-2, \dots$ occur with multiplicity $\dim\mathcal{H}_{\nu-2j}$, and the Cauchy kernel is homogeneous of degree $-(m-1)$ in the Clifford sense, so its radial content is a single exponent. The Mellin transform also mediates between the Laplace and the Fourier transforms along each ray, and it is the transform in which the dilation-invariant operators of the theory (the Euler operator and the Laplacian composed with $|x|^2$) are diagonal.

**The Radon transform.** For $\omega \in \partial B(0,1)$ and $t \in \mathbb{R}$ let $H(\omega,t) = \{x \in A : \langle x,\omega\rangle = t\}$ be the hyperplane. The **Radon transform** of a suitable $f$ is

$$
(Rf)(\omega,t) = \int_{H(\omega,t)}f(x)\,dS(x).
$$

The central-slice theorem computes its one-dimensional Fourier transform in $t$ as the Fourier transform of $f$,

$$
\int_\mathbb{R}(Rf)(\omega,t)\,e^{-i\tau t}\,dt = \hat f(\tau\omega),
$$

so for a left regular $f$ the left-hand side vanishes unless $\tau\omega \in \operatorname{Char}(D)$, the Fourier transform being supported where the symbol is not invertible. The operator itself transforms by the symbol,

$$
R(Df)(\omega,t) = \sigma(\omega)\,\partial_t(Rf)(\omega,t),
$$

so $D$ becomes the first-order operator $\sigma(\omega)\partial_t$ along the normal; a hyperplane restriction of a regular function is therefore not regular but satisfies a one-dimensional equation. The Radon transform exhibits the regular functions as superpositions of plane waves whose frequencies lie on the characteristic variety, which is the geometric form of the Ehrenpreis–Palamodov representation recorded above. Inversion of the Radon transform is the standard inversion $f = c_m\,\Delta^{(m-1)/2}\int_{\partial B}Rf(\omega,\langle x,\omega\rangle)\,d\omega$ with the appropriate power of the Laplacian for the parity of $m$, and it is a theorem of the Euclidean theory, independent of the algebra.

**The Calderón–Zygmund theory.** The boundary operator $S$ above is not a convolution on a group, and the general theorem that makes it tractable is the theory of singular integrals. A **Calderón–Zygmund kernel** on $\mathbb{R}^d$ is a distribution $K$ away from the origin that is homogeneous of degree $-d$, smooth on the sphere, and has mean zero there, $\int_{\partial B}K\,dS = 0$; the associated operator $Tf(x) = \mathrm{p.v.}\int K(x-y)f(y)\,dy$ is bounded on $L^p$ for $1 < p < \infty$ and of weak type $(1,1)$. The boundary kernel of a hypercomplex system meets the hypothesis after the singular part is subtracted: the Cauchy kernel is homogeneous of degree $-(m-1)$, the boundary $\partial\Omega$ has dimension $m-1$, and the difference $\mathcal{C}^+ - \mathcal{C}^-$ is the identity, so the principal-value operator $S$ is a Calderón–Zygmund operator on $\partial\Omega$, bounded on $L^p(\partial\Omega)$ for $1 < p < \infty$ by the general theorem. This is the general reason the Cauchy transform of an $L^2$ boundary datum may be formed and why the jump formula holds pointwise almost everywhere, and it is the reason the one-dimensional theory of the Hilbert transform and the multi-dimensional theory of the boundary Cauchy transform are instances of one theorem. For a non-commutative $A$ the kernel takes values in $A$, and the theory is applied with operator-valued kernels: since $A$ is finite-dimensional and left multiplication by an element of $A$ is a bounded operator, the boundedness statements are unchanged, the relevant vector-valued theory being that of Cotlar–Stein.

## The Discrete Case and the Reduction to the Factor Algebra

**Lattices and Fourier series.** Let $\Gamma \subseteq A$ be a lattice, that is, a discrete cocompact subgroup of the additive group, with dual lattice $\Gamma^* = \{\gamma^* : \langle \gamma^*,\gamma\rangle \in 2\pi\mathbb{Z} \text{ for all } \gamma \in \Gamma\}$. A function on the torus $A/\Gamma$ has a Fourier series

$$
f(x) = \sum_{\gamma^* \in \Gamma^*} c_{\gamma^*}\,e^{i\langle \gamma^*, x\rangle},
$$

and the regularity condition $\sigma(\gamma^*)c_{\gamma^*} = 0$ forces every coefficient whose frequency lies off the complex characteristic variety to vanish. Consequently:

**Proposition.** A left regular function on the torus $A/\Gamma$ has Fourier coefficients supported on $\Gamma^* \cap \operatorname{Char}(D)$, and if the dual lattice meets the complex isotropic cone only at the origin then every left regular function on $A/\Gamma$ is constant.

*Proof.* Apply $\widehat{Df}(\gamma^*) = i\sigma(\gamma^*)c_{\gamma^*} = 0$; where $\sigma(\gamma^*)$ is invertible this gives $c_{\gamma^*} = 0$, and invertibility fails only on $\operatorname{Char}(D)$. $\square$

This is the discrete case of the Fourier transform, and it shows that the characteristic variety controls periodic regular functions exactly as it controls compactly supported ones. The Poisson summation formula

$$
\sum_{\gamma \in \Gamma}f(x+\gamma) = \frac{1}{\mathrm{vol}(A/\Gamma)}\sum_{\gamma^* \in \Gamma^*}\hat f(\gamma^*)\,e^{i\langle\gamma^*,x\rangle}
$$

is the standard identity relating the two lattices and requires no new argument in the hypercomplex setting, being a statement about the additive group.

**Finite groups and the discrete Fourier transform.** For a finite abelian group $G$ the transform theory of the convolution algebra is purely algebraic and is the **discrete Fourier transform**: if the ground field $k$ contains the $|G|$-th roots of unity then the group algebra decomposes as $k[G] \cong \prod_{\chi}k$, the product running over the characters, and the isomorphism is the transform $f \mapsto (\hat f(\chi))_\chi$ with $\hat f(\chi) = \sum_{g \in G}f(g)\chi(g^{-1})$. Convolution becomes pointwise multiplication, exactly as in the continuous case, and the algebra is a product of copies of the ground field, hence semisimple. This is the finite model of the convolution algebra $(L^1(A),*)$ of the opening section, and it is the algebra of *Group Algebras* in the commutative case.

### The Quaternion Groups and the Matrix-Valued Transform

The quaternion systems supply the group transforms in which commutativity fails, and they show where the analysis of the additive group stops applying. For a finite group $G$ the correct object is not a function on characters but a function on the irreducible unitary representations, with **matrix values**: for $f \in \mathbb{C}[G]$, a complex-valued function on $G$,

$$
\hat f(\rho) = \sum_{g \in G}f(g)\,\rho(g), \qquad \widehat{f * h}(\rho) = \hat f(\rho)\,\hat h(\rho), \qquad f(g) = \frac{1}{|G|}\sum_{\rho}d_\rho\,\mathrm{Tr}\bigl(\rho(g^{-1})\hat f(\rho)\bigr),
$$

the last being Fourier inversion and the accompanying Plancherel identity being

$$
\sum_{g \in G}|f(g)|^2 = \frac{1}{|G|}\sum_\rho d_\rho\,\|\hat f(\rho)\|_{\mathrm{HS}}^2 ,
$$

where $d_\rho = \dim V_\rho$ and the sum runs over the irreducible unitary representations. These are standard facts of the representation theory of finite groups. The finite quaternion group

$$
Q_8 = \{\pm 1, \pm e_1, \pm e_2, \pm e_3\}
$$

has $Q_8/\{\pm1\} \cong \mathbb{Z}/2 \times \mathbb{Z}/2$, so it has four one-dimensional representations, and $\sum_\rho d_\rho^2 = |Q_8| = 8$ then forces exactly one two-dimensional irreducible representation, namely the defining one. The transform of $k[Q_8]$ is therefore the discrete Fourier transform of the four characters together with one $2\times2$ matrix-valued component; the first part is the transform of the abelian quotient and the second is the genuinely non-commutative addition. For a compact group the same statement holds with the sum over representations replaced by a direct integral over the unitary dual: for the group $S^3$ of unit quaternions, isomorphic to $\mathrm{Sp}(1)$ and to $SU(2)$, the irreducible representations are indexed by $\ell = 0, \tfrac12, 1, \tfrac32, \dots$ with $d_\ell = 2\ell + 1$, and the **Peter–Weyl theorem** decomposes $L^2(S^3)$ as the $\ell^2$-sum of the matrix-coefficient spaces $V_\ell^* \otimes V_\ell$, again matrix-valued.

The contrast with the additive theory is exact. The additive group $\mathbb{R}^m$ is abelian, its dual is a group, and its transform is a function theory on that dual; the multiplicative quaternion groups are non-abelian, their dual is not a group, and the transform is matrix-valued and is a sum or integral over representations. This is the reason the analysis of a non-abelian group algebra is not a Gelfand theory of a commutative algebra, and it is the same non-commutativity that is met in operator algebras: the group von Neumann algebra $L(G)$ and the reduced group $\mathrm{C}^*$-algebra $\mathrm{C}^*_r(G)$ of *Operator Algebras* are the completions of $\mathbb{C}[G]$ with respect to which the matrix-valued transform becomes a functional calculus, and they are the objects that replace the algebra of continuous functions on a dual group.

**Obstruction and reduction to the factor algebra.** The convolution algebra $(L^1(A),*)$ contains $A$ as the subalgebra of measures supported at the origin, $a \mapsto a\delta_0$, so every zero divisor of $A$ is a zero divisor of the convolution algebra; and the algebra is commutative exactly when $A$ is, in which case a Gelfand transform exists and the convolution algebra is a function algebra on the dual group. For a non-commutative $A$ there is no Gelfand transform, and the Fourier transform is an isomorphism of $(L^1(A),*)$ onto the algebra of bounded continuous $A$-valued functions with the pointwise product: the translation-invariant algebra is non-commutative and its representation theory is that of $A$ itself, which belongs to category 08.

When $A$ decomposes, so does the analysis. If $e_1, \dots, e_r$ is a complete set of orthogonal central idempotents, then $A = \bigoplus_i A_i$ with $A_i = e_iA = Ae_i$, every $A$-valued function is the sum of its components $f_i = e_ife_i$, the Fourier transform acts componentwise,

$$
\hat f = \sum_i \hat f_i, \qquad \hat f_i(\xi) \in A_i,
$$

and the convolution theorem is the convolution theorem in each subalgebra separately. The transform theory of $A$ is therefore the product of the transform theories of the $A_i$, and no information passes between the summands. For the number systems this is the explicit reduction: $\mathbb{D} \cong \mathbb{R} \times \mathbb{R}$ reduces the analysis to two copies of the one-dimensional real theory, in the characteristic coordinates $\xi_\pm = x_0 \pm x_1$; the split biquaternions $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H} \times \mathbb{H}$ reduce to two copies of the quaternion theory; and the dual numbers $\mathbb{D}'$, which have no idempotents but a nilpotent, are analysed in the basis $1, \varepsilon$ by the same componentwise principle with $\varepsilon$-dependent terms. The biquaternions $\mathbb{B} \cong M_2(\mathbb{C})$ are simple, so they possess no central idempotents and no decomposition into a product, but they are a matrix algebra over the field $\mathbb{C}$: a $\mathbb{B}$-valued function is a $2\times2$ matrix of $\mathbb{C}$-valued functions, the additive Fourier transform acts entrywise, and the convolution theorem is the pointwise matrix product. The two reductions together cover every finite-dimensional semisimple $A$ over $\mathbb{R}$ or $\mathbb{C}$: by the structure theory of *Examples of Algebras*, such an algebra is a product of matrix algebras over division algebras, the product decomposes the analysis into factors, and each matrix factor is handled entrywise. This is the precise sense in which the harmonic analysis of a hypercomplex system reduces to the harmonic analysis of a division algebra, repeated according to the size of the matrix blocks, and it is the algebraic content of the obstruction that the zero divisors present.

## Summary

The additive group of $A$ is $\mathbb{R}^m$, and the Euclidean **Fourier transform** $\hat f(\xi) = \int_A f(x)e^{-i\langle\xi,x\rangle}dx$ intertwines differentiation with multiplication, turns **convolution** into the algebra product, and satisfies **Plancherel**. On the Fourier side the Cauchy–Riemann operator acts as multiplication by its symbol, $\widehat{Df}(\xi) = i\sigma(\xi)\hat f(\xi)$, so a function is **left regular** exactly when $\sigma(\xi)\hat f(\xi) = 0$ for all $\xi$. The **characteristic variety** $\operatorname{Char}(D) = \{\zeta \in \mathbb{C}^m : \sum_\alpha\zeta_\alpha^2 = 0\}$ is the complex isotropic cone, independent of the finer structure of a Clifford-type system, and it is the support locus of the Fourier transforms of regular functions; by the **Ehrenpreis–Palamodov theorem**, solutions on a convex domain are limits of exponential-polynomial solutions with frequencies in $\operatorname{Char}(D)$. A compactly supported left regular function on all of $A$ is zero, by Paley–Wiener and analytic continuation.

The Fourier transform of the Cauchy kernel is the inverse of the multiplier, $\hat E(\xi) = \tilde\sigma(\xi)/(i\sum_\alpha\xi_\alpha^2)$ away from $\operatorname{Char}(D)$, and inverting it gives the explicit kernel $E(x) = \bar x/(\omega_{m-1}|x|^m)$ with $\bar x = x_0 - \sum_kB_kx_k$ and $\omega_{m-1}$ the surface area of the unit sphere; for $m=2$ this is $1/(2\pi z)$, the classical Cauchy kernel.

The Euclidean structure gives the **Fischer decomposition** $\mathcal{P}_\nu = \bigoplus_j |x|^{2j}\mathcal{H}_{\nu-2j}$ of homogeneous polynomials into harmonic pieces, of dimensions $\binom{\nu+m-1}{m-1} - \binom{\nu+m-3}{m-1}$; the **solid spherical monogenics** $\mathcal{M}_\nu = \mathcal{P}_\nu \cap \ker D$ refine it, they lie in $\mathcal{H}_\nu$, and $\dim\mathcal{M}_1 = m^2 - m$. A regular function on a ball has a convergent **Taylor expansion** in solid spherical monogenics, and for a Clifford-type system the traces on the sphere of different degrees are mutually orthogonal, which is the hypercomplex **Fourier series**. The **Cauchy transform** reproduces regular functions and is the projection of boundary data onto them, the harmonic-analytic counterpart of the Szegő projection.

The Fourier transform is one of a family determined by the group on which it is taken. The **Laplace transform** $\mathcal{L}f(s) = \int_Af(x)e^{-\langle s,x\rangle}dx$ is holomorphic in a tube and agrees with the Fourier transform on the imaginary axis, but $\mathcal{L}f = 0$ for every compactly supported left regular distribution, so the Laplace theory of regular functions is a theory on cones; the **Hilbert transform** is the principal value operator $S$ with the conormal Cauchy kernel, the boundary operator of the jump formula, and on the line it has multiplier $-i\,\mathrm{sgn}(\xi)$; the **Mellin transform** is the Fourier transform of the multiplicative group, it diagonalises the Euler operator $\vartheta = \sum_\alpha x_\alpha\partial_\alpha$, and it records the radial exponents $\nu, \nu-2, \dots$ of the Fischer decomposition and the single homogeneity degree $-(m-1)$ of the Cauchy kernel; the **Radon transform** satisfies the central-slice theorem and the intertwining $R(Df) = \sigma(\omega)\partial_t(Rf)$, so the regular functions are superpositions of plane waves with frequencies on $\operatorname{Char}(D)$. The **Calderón–Zygmund theory** of singular integrals applies to $S$, whose kernel is homogeneous of degree $-(m-1)$ on the $(m-1)$-dimensional boundary with the singular part subtracted, and it gives the boundedness of the Cauchy transform on $L^p(\partial\Omega)$ with operator-valued kernels in the non-commutative case.

In the **discrete case** the Fourier coefficients of a left regular function on a torus $A/\Gamma$ are supported on $\Gamma^* \cap \operatorname{Char}(D)$, so a lattice whose dual meets the isotropic cone only at the origin supports only constant regular functions; for a finite abelian group the transform is the discrete Fourier transform making $k[G] \cong \prod_\chi k$. Since the additive group of every $A$ is the same $\mathbb{R}^m$, the Euclidean transform of the systems differs only through the symbol: it is elliptic for $\mathbb{C}$, $\mathbb{H}$, $\mathbb{H}_{\mathbb{D}}$ and $\mathbb{B}$, where a left regular tempered distribution has transform supported at the origin, and it is a support condition on the two lines $\xi_0 = \pm\xi_1$ for $\mathbb{D}$ and on the hyperplane $\xi_0 = 0$ for $\mathbb{D}'$. The **quaternion groups** show the non-commutative case: for a finite group the transform is matrix-valued, $\hat f(\rho) = \sum_gf(g)\rho(g)$ with inversion and Plancherel summing over the irreducible representations weighted by $d_\rho = \dim V_\rho$, and for the finite quaternion group $Q_8$ it consists of the four characters of $Q_8/\{\pm1\}$ together with one two-dimensional component, while for the compact group $S^3$ of unit quaternions the **Peter–Weyl theorem** replaces the sum by the direct integral over representations of dimension $2\ell+1$. The convolution algebra $(L^1(A),*)$ contains $A$ as the measures at the origin, so its zero divisors are those of $A$, and it is commutative exactly when $A$ is. When $A$ has a complete set of orthogonal central idempotents the Fourier transform acts componentwise and the analysis splits as the product of the analyses of the subalgebras $A_i = e_iA = Ae_i$; a simple matrix algebra such as $\mathbb{B} \cong M_2(\mathbb{C})$ is instead handled entrywise, and the two reductions together reduce the harmonic analysis of any finite-dimensional semisimple $A$ to that of a division algebra, repeated over the matrix blocks.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | Finite-dimensional unital associative real algebra, $\dim_\mathbb{R} A = m$ |
| $D = \partial_0 + \sum_kB_k\partial_k$ | Cauchy–Riemann operator |
| $\sigma(\xi) = \sum_\alpha B_\alpha\xi_\alpha$ | Symbol of $D$ |
| $\hat f(\xi)$ | Euclidean Fourier transform of $f$ |
| $\langle\xi,x\rangle = \sum_\alpha\xi_\alpha x_\alpha$ | Real inner product, not the algebra product |
| $f * g$ | Convolution, $\widehat{f*g} = \hat f\hat g$ |
| $\operatorname{Char}(D)$ | Characteristic variety, the complex isotropic cone |
| $A_\mathbb{C} = A\otimes_\mathbb{R}\mathbb{C}$ | Complexification of $A$ |
| $\mathcal{P}_\nu$ | $A$-valued homogeneous polynomials of degree $\nu$ |
| $\mathcal{H}_\nu$ | Harmonic homogeneous polynomials of degree $\nu$ |
| $\mathcal{M}_\nu(A,D)$ | Solid spherical monogenics of degree $\nu$ |
| $\nu_B = \sum_\alpha\nu_\alpha B_\alpha$ | Conormal element |
| $\mathcal{C}h$ | Cauchy transform of a boundary datum |
| $E$ | Fundamental solution / Cauchy kernel |
| $\hat E$ | Fourier transform of the kernel, $\hat E = \tilde\sigma/(i\sum_\alpha\xi_\alpha^2)$ off $\operatorname{Char}(D)$ |
| $\Phi$ | Fundamental solution of the Laplacian, $E = \bar D\Phi$ |
| $\bar x = x_0 - \sum_kB_kx_k$ | Clifford conjugate of the variable |
| $\omega_{m-1} = 2\pi^{m/2}/\Gamma(m/2)$ | Surface area of the unit sphere in $\mathbb{R}^m$ |
| $\mathcal{L}f$ | Laplace transform, $\mathcal{L}f(s) = \int_Af(x)e^{-\langle s,x\rangle}dx$ |
| $Hf$ | Hilbert transform on the line, $(Hf)(x) = \frac{1}{\pi}\mathrm{p.v.}\int f(y)/(x-y)\,dy$ |
| $Sh$ | Boundary singular integral with the conormal Cauchy kernel |
| $\mathcal{M}f$ | Mellin transform, $(\mathcal{M}f)(s) = \int_0^\infty f(r)r^{s-1}dr$ |
| $\vartheta = \sum_\alpha x_\alpha\partial_\alpha$ | Euler (dilation) operator, distinct from the kernel $E$ |
| $Rf(\omega,t)$ | Radon transform over the hyperplane $\langle x,\omega\rangle = t$ |
| $\Gamma$, $\Gamma^*$ | Lattice in $A$ and its dual lattice |
| $e_i$, $A_i = e_iAe_i$ | Complete orthogonal idempotents and the split components of $A$ |
| $Q_8$ | Finite quaternion group $\{\pm1,\pm e_1,\pm e_2,\pm e_3\}$ |
| $S^3 \cong \mathrm{Sp}(1) \cong SU(2)$ | Group of unit quaternions, a compact group |
| $\hat f(\rho) = \sum_g f(g)\rho(g)$ | Matrix-valued Fourier transform on a group |
| $d_\rho = \dim V_\rho$ | Dimension of an irreducible representation |

## Further Reading

- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton, 1971), for the Euclidean Fourier transform and spherical harmonics.
- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the monogenic Fischer decomposition and spherical monogenics.
- R. Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for the harmonic analysis of the regular functions and the Cauchy transform.
- Victor P. Palamodov, *Linear Differential Operators with Constant Coefficients* (Springer, 1970), for the Ehrenpreis–Palamodov exponential representation.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* (Springer, 2nd ed. 1990), for the characteristic variety and Paley–Wiener theory.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the explicit spherical monogenics.
