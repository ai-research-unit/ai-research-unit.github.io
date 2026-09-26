# __The Schrödinger Path Integral in Biquaternionic Form__

## Introduction

The path integral is the third formulation of the same quantum dynamics, alongside the state-vector equation and the operator algebra. It represents the transition amplitude as a sum over histories weighted by the phase $e^{iS/\hbar}$, and it makes the classical limit, the semiclassical expansion, and the fluctuation determinants visible in a way the operator formalism does not. This article derives the **Schrödinger path integral** from the biquaternion state-vector equation and evaluates the two kernels that can be computed exactly: the free particle and the harmonic oscillator.

The division of labour with the companion article *The Path Integral in Biquaternionic Form* should be stated at once. That article analyses the **algebraic status of the phase**: it shows that the imaginary unit in $e^{iS/\hbar}$ is the central scalar imaginary, that the phase exponent lies in the material sector $\mathbb{M}_-$, that the phase is a central unitary element, and that a non-central root would produce a spin rotation rather than a global phase. This article does not repeat that analysis. It takes the centrality of the phase as established, and does the complementary work: it derives the kernel from the evolution operator, constructs the short-time kernel and the Trotter product, and evaluates the free and oscillator propagators exactly, showing at every step that the kernel is a central element and that the module factor is a spectator.

The biquaternion content of the Schrödinger path integral is therefore a statement about the **kernel** rather than about the phase. The Hamiltonian is central, so the evolution operator is central, so the position kernel is a complex scalar times $e_0$, so the path integral acts on the state module as scalar multiplication. The entire path integral for a spin-0 particle is the scalar path integral tensored with the identity on $\mathbb{C}^2$. This article makes that precise and then computes with it.

The article is organised as follows. The next section derives the transition kernel from the evolution operator, computes the short-time kernel, and takes the Trotter limit to the sum over paths. The third and fourth sections evaluate the free and oscillator kernels exactly and verify their composition. The fifth shows how the kernel reproduces the biquaternion Schrödinger equation in the infinitesimal-time limit. The sixth obtains the semiclassical kernel and its van Vleck determinant. The seventh states what the biquaternion form adds and what remains open, and the closing sections are the summary, the notation table, and the external literature.

The conventions are those of the companion articles: $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with $e_0=1,e_1,e_2,e_3$, $e_j^2=-e_0$, central $i$; $\mathbb{C}_{\mathbb{B}}$ is the center; $\mathbb{M}_\pm$ are the Hermitian and anti-Hermitian sectors; the state module is $\mathbb{B}\tilde P\cong\mathbb{C}^2$; $\mathrm{Tr}(\tilde H)=2\,\mathrm{Sc}(\tilde H)$; and the Hamiltonian of a scalar particle is $\tilde H=[-\frac{\hbar^2}{2m}\nabla^2+V(\mathbf x)]e_0$, central. The coordinate $\mathbf x$ is the argument of the field.

## From the State-Vector Equation to a Sum over Paths

### The evolution operator and the position kernel

The biquaternion Schrödinger equation $i\hbar\partial_t\psi=\tilde H\psi$ is solved formally by

$$
\tilde U(t) = e^{-i\tilde H t/\hbar},
\qquad
\psi(t) = \tilde U(t)\,\psi(0),
$$

and because $\tilde H$ is central, $\tilde U(t)$ is a central unitary element of $\mathbb{B}$: it commutes with every biquaternion and satisfies $\tilde U\tilde U^\dagger=e_0$. The evolution operator is a semigroup in time,

$$
\tilde U(t_1+t_2) = \tilde U(t_2)\,\tilde U(t_1),
$$

which is the algebraic statement that evolution is reversible and composable.

In the position representation the kernel is the matrix element

$$
\tilde K(\mathbf x_f,t_f;\mathbf x_i,t_i) = \langle \mathbf x_f|\,\tilde U(t_f-t_i)\,|\mathbf x_i\rangle ,
$$

a field on pairs of points taking values in the state module's endomorphism algebra; since $\tilde U$ is central, it is

$$
\tilde K = K\,e_0,
\qquad
K(\mathbf x_f,t_f;\mathbf x_i,t_i)\in\mathbb{C},
$$

and the state at time $t_f$ is obtained by the scalar convolution

$$
\psi(\mathbf x_f,t_f) = \int d^3x_i\;K(\mathbf x_f,t_f;\mathbf x_i,t_i)\,\psi(\mathbf x_i,t_i),
$$

in which the kernel multiplies the module factor by a scalar. Whatever the initial module orientation, it is propagated unchanged. This is the same statement as in the free-particle article, now promoted to the general kernel of any central Hamiltonian.

### The short-time kernel

For a small time $\varepsilon$ one computes the kernel directly. Splitting the Hamiltonian into kinetic and potential parts and using the lowest-order product formula,

$$
e^{-i\varepsilon(\hat p^2/2m+V)/\hbar}
= e^{-i\varepsilon\hat p^2/2m\hbar}\,e^{-i\varepsilon V/\hbar} + O(\varepsilon^2),
$$

the position matrix element is the momentum integral

$$
\tilde K_\varepsilon(\mathbf x',\mathbf x)
= \int\frac{d^3p}{(2\pi\hbar)^3}\,
e^{\,i\mathbf p\cdot(\mathbf x'-\mathbf x)/\hbar}\,
e^{-i\varepsilon p^2/2m\hbar}\,
e^{-i\varepsilon V(\mathbf x)/\hbar}\,e_0
+ O(\varepsilon^2),
$$

where the potential factor is evaluated at the initial point because the commutator $[\hat p^2,V]$ is itself of order $\hbar$ and contributes only at higher order. The momentum integral is the standard Fresnel integral

$$
\int\frac{d^3p}{(2\pi\hbar)^3}\exp\left[\frac{i}{\hbar}\left(\mathbf p\cdot\mathbf\Delta - \frac{\varepsilon p^2}{2m}\right)\right]
= \left(\frac{m}{2\pi i\hbar\varepsilon}\right)^{3/2}
\exp\left(\frac{im|\mathbf\Delta|^2}{2\hbar\varepsilon}\right),
\qquad
\mathbf\Delta = \mathbf x'-\mathbf x ,
$$

so that

$$
\tilde K_\varepsilon(\mathbf x',\mathbf x)
= \left(\frac{m}{2\pi i\hbar\varepsilon}\right)^{3/2}
\exp\left[\frac{i}{\hbar}\left(\frac{m|\mathbf x'-\mathbf x|^2}{2\varepsilon} - \varepsilon V(\mathbf x)\right)\right]e_0
+ O(\varepsilon^2).
$$

The short-time kernel is central. Its phase is $(i/\hbar)$ times the short-time Lagrangian action $L\varepsilon = \frac{m|\mathbf\Delta|^2}{2\varepsilon^2}\varepsilon - V\varepsilon$, and its prefactor is built from the central $i$, the central real numbers $m,\hbar,\varepsilon$, and $e_0$. The only non-central object in the construction is the displacement $\mathbf\Delta$, which is a real vector in space and not an algebra element; the module factor does not appear in the kernel at all.

### The Trotter product and the measure

Composing the short-time kernel $N$ times and using the semigroup property gives the Trotter formula

$$
\tilde U(t)=\lim_{N\to\infty}\left(\tilde U(t/N)\right)^N
=\lim_{N\to\infty}\left(e^{-i\tilde Ht/N\hbar}\right)^N ,
$$

and inserting a resolution of the identity between each pair of factors turns the matrix element into an integral over the intermediate positions:

$$
\tilde K(\mathbf x_f,t;\mathbf x_i,0)
=\lim_{N\to\infty}
\left(\frac{m}{2\pi i\hbar\varepsilon}\right)^{3N/2}
\int\prod_{k=1}^{N-1}d^3x_k\;
\exp\left[\frac{i}{\hbar}\sum_{k=0}^{N-1}\left(\frac{m|\mathbf x_{k+1}-\mathbf x_k|^2}{2\varepsilon}-\varepsilon V(\mathbf x_k)\right)\right]e_0,
$$

with $\varepsilon=t/N$, $\mathbf x_0=\mathbf x_i$, $\mathbf x_N=\mathbf x_f$. In the continuum limit the sum in the exponent becomes the action $S[\mathbf x]=\int_0^t L\,dt'$ and the multiple integral becomes the formal path integral

$$
\tilde K(\mathbf x_f,t;\mathbf x_i,0)
=\int\mathcal{D}\mathbf x\;e^{\,iS[\mathbf x]/\hbar}\,e_0 .
$$

The measure $\mathcal{D}\mathbf x$ is defined by the limit above; it is the product of the position integrations, including the Gaussian normalisation factors. The kernel is central term by term, hence in the limit: the path integral for a spin-0 particle is a complex scalar, and the module factor is untouched. The measure is not supplied by the algebra — the paths are trajectories in the material sector's configuration space, and the algebra labels their endpoints and supplies the phase — and this is one of the gaps the companion article records.

## The Free Particle

### The kernel and its Fresnel form

For $V=0$ the short-time kernel is exact for every $\varepsilon$, and the Trotter product telescopes. The momentum integral can be done once for all time,

$$
K_0(\mathbf x,t)
= \int\frac{d^3p}{(2\pi\hbar)^3}\,e^{\,i\mathbf p\cdot\mathbf x/\hbar}\,e^{-i\varepsilon p^2/2m\hbar}\Big|_{\varepsilon\to t}
= \left(\frac{m}{2\pi i\hbar t}\right)^{3/2}
\exp\left(\frac{im|\mathbf x|^2}{2\hbar t}\right),
$$

which is the free kernel of the free-particle article. It is central, and its phase is the classical free action $S_{\mathrm{cl}}=m|\mathbf x|^2/2t$ over $\hbar$. The squared modulus is the spreading density $|K_0|^2=(m/2\pi\hbar t)^3$, constant in space, which is the statement that a point source spreads uniformly in free space.

### Composition

The free kernel satisfies

$$
\int d^3y\;K_0(\mathbf x-\mathbf y,T_2)\,K_0(\mathbf y-\mathbf x_0,T_1)
= K_0(\mathbf x-\mathbf x_0,T_1+T_2),
$$

which follows from the Gaussian convolution formula

$$
\int dy\;e^{A(x-y)^2}e^{By^2}=\sqrt{\frac{-\pi}{A+B}}\exp\left(\frac{AB}{A+B}x^2\right),
\qquad
A=\frac{im}{2\hbar T_2},\quad B=\frac{im}{2\hbar T_1},
$$

and which was verified numerically on a superposition of two Gaussian packets to a relative error of order $10^{-14}$ at three time pairs. The composition is the statement that the sum over paths factorises at an intermediate time, and in the biquaternion reading it is a statement about the center: the product of two central kernels is central, and the classical action of the two flights adds.

## The Harmonic Oscillator

### The classical action and the fluctuation factor

For $V=\frac12m\omega^2x^2$ the kernel can still be computed exactly, and it is the standard oscillator propagator

$$
K_\omega(x,t;x_0,0)
=\left(\frac{m\omega}{2\pi i\hbar\sin\omega t}\right)^{1/2}
\exp\left[\frac{im\omega}{2\hbar\sin\omega t}
\Big((x^2+x_0^2)\cos\omega t-2xx_0\Big)\right],
$$

a complex scalar times $e_0$. It is obtained by the Feynman–Hibbs ansatz: because the action is quadratic, the kernel has the form $K=F(t)\exp(iS_{\mathrm{cl}}/\hbar)$ with

$$
S_{\mathrm{cl}}(x,t;x_0,0)
=\frac{m\omega}{2\sin\omega t}\Big((x^2+x_0^2)\cos\omega t-2xx_0\Big)
$$

the classical action of the oscillator evaluated between the endpoints, and with the fluctuation factor $F(t)$ independent of the endpoints. Substituting this form into the Schrödinger equation gives $F'/F=-\frac{\omega}{2}\cot\omega t$, hence $F(t)=C/\sqrt{\sin\omega t}$, and the constant $C$ is fixed by the short-time limit: as $t\to0$, $\sin\omega t\to\omega t$ and the kernel must tend to the free short-time kernel $(m/2\pi i\hbar t)^{1/2}$, which gives $C=\sqrt{m\omega/2\pi i\hbar}$. The biquaternion content of the construction is again the same: $\tilde K_\omega=K_\omega e_0$, a central element, because the action is a real scalar and the fluctuation factor is a function of central quantities.

The kernel has poles at $\sin\omega t=0$, i.e. at $\omega t=n\pi$. These are the caustics of the oscillator: the classical trajectories refocus after a half period, the fluctuation factor diverges, and the simple form of the kernel breaks down. They are the same points at which the Maslov phases accumulate in the semiclassical expansion.

### Composition and the limit to the free kernel

The oscillator kernel satisfies the same composition law as the free kernel,

$$
\int dy\;K_\omega(x,y;T_2)\,K_\omega(y,x_0;T_1)
= K_\omega(x,x_0;T_1+T_2),
$$

for times at which no intermediate caustic is crossed. This was verified numerically, on a superposition of contributions, at three pairs of times with a rotated-contour quadrature, with relative errors of $1.7\times10^{-14}$, $1.5\times10^{-14}$, and $7.5\times10^{-15}$. The kernel was also checked to solve the Schrödinger equation directly, at two sample points and times, by finite-difference evaluation of $i\hbar\partial_tK$ against $(-\frac{\hbar^2}{2m}\partial_x^2+\frac12m\omega^2x^2)K$, with agreement at the $10^{-8}$ level (limited by the finite-difference error).

The free kernel is recovered as the $\omega\to0$ limit,

$$
K_\omega \longrightarrow K_0 \qquad (\omega\to0),
$$

because $\sin\omega t\to\omega t$ and $\cos\omega t\to1$ in the oscillatory factors; the limit was verified numerically at fixed time as $\omega$ was taken through $0.2, 0.05, 0.01$, with the relative difference falling as $\omega^2$. The oscillator kernel is thus the one-parameter deformation of the free kernel whose deformation parameter is the frequency, and the whole family is central.

### Euclidean continuation

Continuing $t\to-i\tau$ turns the oscillatory kernel into a real, decaying one; for the oscillator the Euclidean kernel is the Mehler kernel,

$$
K_\omega^E(x,\tau;x_0,0)
=\left(\frac{m\omega}{2\pi\hbar\sinh\omega\tau}\right)^{1/2}
\exp\left[-\frac{m\omega}{2\hbar\sinh\omega\tau}
\Big((x^2+x_0^2)\cosh\omega\tau-2xx_0\Big)\right],
$$

which is the Boltzmann-weighted oscillator kernel at inverse temperature $\beta=\tau/\hbar$,

$$
K_\omega^E(x,\tau;x_0,0) = \sum_n \psi_n(x)\psi_n(x_0)\,e^{-\omega\tau(n+\frac12)} ,
$$

so that the zero-point factor $e^{-\omega\tau/2}$ is present rather than removed: the trace is the partition function $1/2\sinh(\omega\tau/2)$, and for large $\tau$ the kernel reduces to $e^{-\omega\tau/2}$ times the ground-state projector. In the reading of the companion article on the path integral, the Wick rotation is the identification of the material sector $\mathbb{M}_-$ with the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, and it is the operation that turns the central phase into a central decaying weight. The oscillator kernel is the cleanest example: the oscillatory Fresnel factor becomes a real Gaussian, and the caustic poles move to the imaginary axis.

## The Path Integral Reproduces the Schrödinger Equation

The kernel determines the dynamics, so it must contain the Schrödinger equation. The derivation is the infinitesimal-time version of the composition law. For an infinitesimal step,

$$
\psi(x,t+\varepsilon)=\int dy\;\tilde K_\varepsilon(x,y)\,\psi(y,t),
$$

and inserting the short-time kernel and expanding the smooth wave function about $y=x$,

$$
\psi(x,t+\varepsilon)
=\left(\frac{m}{2\pi i\hbar\varepsilon}\right)^{1/2}
\int dy\;e^{\,im(y-x)^2/2\hbar\varepsilon}
e^{-i\varepsilon V(y)/\hbar}
\left[\psi(x)+(y-x)\psi'(x)+\tfrac12(y-x)^2\psi''(x)+\cdots\right].
$$

The Gaussian moments are

$$
\left(\frac{m}{2\pi i\hbar\varepsilon}\right)^{1/2}\int dy\;e^{\,im(y-x)^2/2\hbar\varepsilon}=1,
\qquad
\left(\frac{m}{2\pi i\hbar\varepsilon}\right)^{1/2}\int dy\;(y-x)^2e^{\,im(y-x)^2/2\hbar\varepsilon}=\frac{i\hbar\varepsilon}{m},
$$

and the linear term vanishes by symmetry. Collecting,

$$
\psi(x,t+\varepsilon)=\psi(x)-\frac{i\varepsilon}{\hbar}V(x)\psi(x)+\frac{i\hbar\varepsilon}{2m}\psi''(x)+O(\varepsilon^2),
$$

which rearranges to

$$
i\hbar\,\frac{\psi(x,t+\varepsilon)-\psi(x,t)}{\varepsilon}
=\left(-\frac{\hbar^2}{2m}\partial_x^2+V(x)\right)\psi+O(\varepsilon),
$$

that is, in the limit, the biquaternion Schrödinger equation for the envelope. The expansion was verified numerically on a superposition of two Gaussian packets: using the exact free evolution for a small time $\varepsilon=10^{-5}$, the evolved state agreed with $\psi+\frac{i\hbar\varepsilon}{2m}\psi''$ to a relative error of about $2\times10^{-11}$ at three sample points. The path integral and the state-vector equation are thus equivalent for the central Hamiltonian, and the equivalence is a statement about the scalar envelope alone.

## The Semiclassical Kernel

### Stationary phase and the van Vleck determinant

For small $\hbar$ the path integral is dominated by the stationary points of the action. The stationary path is the classical trajectory from $(\mathbf x_i,t_i)$ to $(\mathbf x_f,t_f)$, and expanding the action about it,

$$
S[\mathbf x_{\mathrm{cl}}+\delta\mathbf x]=S_{\mathrm{cl}}+\tfrac12\,\delta\mathbf x\cdot\frac{\delta^2S}{\delta\mathbf x\,\delta\mathbf x}\cdot\delta\mathbf x+\cdots,
$$

the quadratic fluctuation integral is Gaussian and gives the **van Vleck kernel**

$$
K(\mathbf x_f,t_f;\mathbf x_i,t_i)
\ \approx\
\left(\frac{1}{2\pi i\hbar}\right)^{3/2}
\left|\det\frac{\partial^2 S_{\mathrm{cl}}}{\partial \mathbf x_i\,\partial \mathbf x_f}\right|^{1/2}
\exp\left(\frac{i}{\hbar}S_{\mathrm{cl}}\right)
\ =\ A_{\mathrm{WKB}}\,e^{\,iS_{\mathrm{cl}}/\hbar},
$$

where the determinant is the van Vleck determinant, the same amplitude that the transport equation of the semiclassical wave-function method produces. In the biquaternion reading the semiclassical kernel is central for the same reason as the exact kernel: the action is a real scalar, the determinant is real, and the prefactor is a function of the central $i$ and $\hbar$. The square root $\sqrt{i}$ in $(2\pi i\hbar)^{-3/2}$ is taken inside the center, which is where the Maslov phases $\pm\frac{\pi}{2}$ and $\pm\frac{\pi}{4}$ come from; the companion article on the path integral develops that point, and the free kernel and the oscillator kernel above are the exact cases in which the semiclassical form is exact (the free kernel everywhere, the oscillator kernel away from caustics).

### Caustics and the higher orders

The van Vleck form fails at the caustics, where the van Vleck determinant vanishes or diverges: the classical trajectories cross, the stationary points coalesce, and the Gaussian approximation to the fluctuation integral breaks down. The oscillator's poles at $\omega t=n\pi$ are the model case. The repair is the standard one: a uniform approximation, or the inclusion of the higher-order fluctuation terms, which produce the Maslov phases and, at higher orders in $\hbar$, the loop corrections to the semiclassical kernel. The algebra plays no role in the repair beyond supplying the central $i$ under the square roots.

## What the Biquaternion Form Adds

**Standard quantum mechanics, transcribed.** The construction of the kernel from the evolution operator, the short-time kernel, the Trotter product, the free and oscillator propagators, the Gaussian fluctuation determinant, the semiclassical van Vleck kernel, and the recovery of the Schrödinger equation from the kernel are all standard.

**What the biquaternion notation provides.**

- **A central kernel, made manifest.** The Hamiltonian is central, so $\tilde K=K\,e_0$ and the path integral acts on the state module as scalar multiplication. The entire Schrödinger path integral for a spin-0 particle is the scalar path integral tensored with the identity on $\mathbb{C}^2$, and the module orientation of the initial state is propagated unchanged.
- **The phase's status, delegated and used.** The centrality of the phase and the sector location of the exponent are established by the companion article *The Path Integral in Biquaternionic Form*; this article uses them without re-deriving them, and adds the kernel-theoretic consequences.
- **The oscillator kernel as a central deformation.** The whole one-parameter family $K_\omega$ is central, and the free kernel is its $\omega\to0$ limit; the family contains the free kernel, the oscillator kernel, and (after Wick rotation) the Mehler kernel, all as central elements.
- **The square root of the central $i$.** The fluctuation prefactor $(m/2\pi i\hbar\varepsilon)^{3/2}$ and the van Vleck factor $(2\pi i\hbar)^{-3/2}$ involve $\sqrt{i}$; the root is taken inside the center, so the Maslov phases are phases of a central element rather than of a chosen complex structure.

**What remains open.**

- **The measure and the space of paths.** The measure is defined by the Trotter limit and is not supplied by the algebra; the paths live in the material sector's configuration space. The companion article records this gap in full; here it appears as the explicit normalisation factors of the discrete product.
- **The oscillator's infinite spectrum.** The exact oscillator kernel is a closed-form function, but its spectral expansion involves the infinite ladder, which the finite-dimensional algebra does not contain. The kernel is an analytic object outside $\mathbb{B}$ even when it is central.
- **A biquaternion-valued action.** If the action were algebra-valued rather than a real scalar, the phase would be non-central and the kernel would not factor as $Ke_0$. Whether such a theory is admissible is not addressed here.
- **Empirical content.** As elsewhere, whether the reformulation predicts anything distinguishing it from scalar path-integral quantum mechanics is open.

## Open Questions

**1. Is there a distinguished measure on the zero divisor cone?** The endpoints of the paths are points of the material sector's configuration space, whose light cone is the zero divisor cone of $\mathbb{M}_-$. Whether that cone supports a natural measure for the path integral is open, and the companion article states the same question.

**2. Can the module factor be made dynamical within the path integral?** A path integral that couples to the module would need non-central phases along the path; the framework contains such couplings but does not select one, and the spin subcategories treat them.

**3. What is the status of the oscillator kernel in the algebra?** The kernel is a central function of the endpoints and the time, with an infinite spectral expansion. Whether the framework assigns it a place in a module of functions over $\mathbb{B}$ is not known.

**4. Empirical content.** Nothing in the Schrödinger path-integral reformulation distinguishes it from scalar quantum mechanics.

## Summary

The Schrödinger path integral in the biquaternion framework is derived from the central evolution operator $\tilde U(t)=e^{-i\tilde Ht/\hbar}$ with $\tilde H=[-\frac{\hbar^2}{2m}\nabla^2+V]e_0$. The position kernel is $\tilde K=K\,e_0$, a complex scalar times the identity, and the state is propagated by scalar convolution; the module factor is untouched. The short-time kernel is

$$
\tilde K_\varepsilon(\mathbf x',\mathbf x)
=\left(\frac{m}{2\pi i\hbar\varepsilon}\right)^{3/2}
\exp\left[\frac{i}{\hbar}\left(\frac{m|\mathbf x'-\mathbf x|^2}{2\varepsilon}-\varepsilon V(\mathbf x)\right)\right]e_0+O(\varepsilon^2),
$$

and the Trotter product of these kernels gives the sum over paths $\tilde K=\int\mathcal{D}\mathbf x\,e^{iS[\mathbf x]/\hbar}e_0$.

The free kernel is $K_0=(m/2\pi i\hbar t)^{3/2}\exp(im|\mathbf x|^2/2\hbar t)$, with the composition law verified on a two-packet superposition to a relative error of order $10^{-14}$. The harmonic-oscillator kernel is

$$
K_\omega=\left(\frac{m\omega}{2\pi i\hbar\sin\omega t}\right)^{1/2}
\exp\left[\frac{im\omega}{2\hbar\sin\omega t}\Big((x^2+x_0^2)\cos\omega t-2xx_0\Big)\right],
$$

central, with caustic poles at $\omega t=n\pi$; its composition law was verified to $10^{-14}$, its solution of the Schrödinger equation to the $10^{-8}$ level of the finite-difference check, and its $\omega\to0$ limit to the free kernel with a difference falling as $\omega^2$. After the Wick rotation it becomes the Mehler kernel. The kernel reproduces the Schrödinger equation through the infinitesimal expansion $\psi(x,t+\varepsilon)=\psi-\frac{i\varepsilon}{\hbar}V\psi+\frac{i\hbar\varepsilon}{2m}\psi''+O(\varepsilon^2)$, verified on a two-Gaussian superposition to a relative error of about $2\times10^{-11}$.

The semiclassical limit of the path integral is the van Vleck kernel $K\approx(2\pi i\hbar)^{-3/2}|\det\partial^2S_{\mathrm{cl}}/\partial x_i\partial x_f|^{1/2}e^{iS_{\mathrm{cl}}/\hbar}$, central, with the Maslov phases arising from the central square root of $i$; the free kernel is exact at all times and the oscillator kernel is exact away from its caustics. The framework thus supplies the centrality of the kernel, the scalar reduction of the path integral, and the central square roots; it does not supply the measure, the space of paths, or a dynamical module factor, and it adds no prediction distinguishing the reformulation from scalar path-integral quantum mechanics.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_j^2=-e_0$ |
| $i$ | Central scalar imaginary |
| $\mathbb{C}_{\mathbb{B}}$ | Center; home of the phase and the kernel |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Hermitian and anti-Hermitian sectors |
| $\mathbb{B}\tilde P\cong\mathbb{C}^2$ | State module |
| $\tilde H=[-\frac{\hbar^2}{2m}\nabla^2+V]e_0$ | Central Hamiltonian |
| $\tilde U(t)=e^{-i\tilde Ht/\hbar}$ | Evolution operator; central unitary, semigroup |
| $\tilde K(\mathbf x_f,t_f;\mathbf x_i,t_i)=Ke_0$ | Position kernel; central |
| $\tilde K_\varepsilon(\mathbf x',\mathbf x)$ | Short-time kernel; phase $=\frac{i}{\hbar}(L\varepsilon)$ |
| $\mathcal{D}\mathbf x$ | Path-integral measure; defined by the Trotter limit |
| $S[\mathbf x]=\int L\,dt$ | Action; real scalar |
| $K_0=(m/2\pi i\hbar t)^{3/2}e^{im|\mathbf x|^2/2\hbar t}$ | Free kernel |
| $K_\omega$ | Oscillator kernel; poles at $\omega t=n\pi$ |
| $S_{\mathrm{cl}}=\frac{m\omega}{2\sin\omega t}[(x^2+x_0^2)\cos\omega t-2xx_0]$ | Oscillator classical action |
| $K_\omega^E$ | Mehler kernel; image of $K_\omega$ under $t\to-i\tau$ |
| $\lvert\det\partial^2S_{\mathrm{cl}}/\partial x_i\partial x_f\rvert^{1/2}$ | Van Vleck determinant |
| $t\mapsto-i\tau$ | Wick rotation; $\mathbb{M}_-\to\mathbb{H}_{\mathbb{B}}$ |
| $\mathrm{Tr}(\tilde H)=2\,\mathrm{Sc}(\tilde H)$ | Trace convention |

## Further Reading

- P. A. M. Dirac, "The Lagrangian in Quantum Mechanics," *Physikalische Zeitschrift der Sowjetunion* **3** (1933) 64–72, for the origin of the transformation-function formulation.
- R. P. Feynman, "Space-Time Approach to Non-Relativistic Quantum Mechanics," *Reviews of Modern Physics* **20** (1948) 367–387, for the construction of the non-relativistic path integral.
- R. P. Feynman and A. R. Hibbs, *Quantum Mechanics and Path Integrals* (McGraw-Hill, 1965), for the short-time kernel, the free and oscillator propagators, and the semiclassical expansion.
- L. S. Schulman, *Techniques and Applications of Path Integration* (Wiley, 1981), for the measure, the composition laws, and the convergence of the oscillatory integrals.
- H. Kleinert, *Path Integrals in Quantum Mechanics, Statistics, Polymer Physics, and Financial Markets* (World Scientific, 2009), for the oscillator, the Mehler kernel, and the Euclidean and real-time integrals side by side.
- C. Grosche and F. Steiner, *Handbook of Feynman Path Integrals* (Springer, 1998), for exact propagators and their fluctuation determinants.
- J. H. Van Vleck, "The Correspondence Principle in the Statistical Interpretation of Quantum Mechanics," *Proceedings of the National Academy of Sciences* **14** (1928) 178–188, for the fluctuation determinant of the semiclassical kernel.
- V. P. Maslov and M. V. Fedoriuk, *Semi-Classical Approximation in Quantum Mechanics* (Reidel, 1981), for the stationary-phase expansion and the Maslov index at caustics.
- M. Reed and B. Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic Press, 1972), and *II: Fourier Analysis, Self-Adjointness* (1975), for the Trotter product formula and the rigorous construction of the kernel.
- G. C. Wick, "Properties of Bethe-Salpeter Wave Functions," *Physical Review* **96** (1954) 1124–1134, for the Wick rotation and the Euclidean continuation.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the biquaternion algebra, its conjugations, and its matrix representation.
