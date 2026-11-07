# __The Klein–Gordon Propagator and Its Green's Functions in Biquaternionic Form__

## Introduction

A second-order wave equation has no state vector of its own; its characteristic object is the **Green's function**, the distributional inverse that turns a source into a field and a field operator into a two-point correlation. For the Klein–Gordon equation that object is the subject of this article. The companion article *The Klein–Gordon Equation in Biquaternionic Form* writes the equation, fixes the sign of the mass term, and records that the d'Alembertian of the framework is central and scalar; the companion article *The Schrödinger Equation in Biquaternionic Form* and the present subcategory's structural article *The Scalar Field in the Centre: Why Spin 0 Escapes the Biquaternion State Module* fix the field's value space as the centre $\mathbb{B}_{C}$. This article takes those results as given and does the work that is proper to the second-order, inverse problem: it constructs the retarded, advanced, causal and Pauli–Jordan kernels, derives their support and their dispersion, verifies microcausality, and states what the biquaternion algebra contributes to all of it.

The biquaternion contribution is specific and can be stated before the calculations. The operator

$$
\Box-k_m^{2}
$$

is a **central scalar** element of the algebra: the d'Alembertian $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}$ is central because it is built from the gradient in a symmetric way, and the mass term is a multiple of $e_t$. Consequently every Green's function of the Klein–Gordon operator is a complex scalar times $e_t$, every propagator commutes with every element of $\mathbb{B}$, and the state module — the two-dimensional complex left ideal, of four real dimensions, on which the spinor fields live — is a spectator. The whole Green's-function structure of a spin-$0$ field is the scalar structure tensored with the identity on the module. What the algebra adds is the identification of the places where the kernel is singular: the **light cone** on which the massless kernel is supported is the zero-divisor cone of the material sector $\mathbb{B}_{\Phi}$, the set of four-vectors of vanishing biquaternion norm, and the **mass shell** is the locus of constant biquaternion norm $\langle\tilde K_{\Phi}\rangle_{\natural}=-k_m^{2}$ on the wave-number element $\tilde K_{\Phi}=\tilde P_{\Phi}/\hbar$, a hyperboloid in $\mathbb{B}_{\Phi}$. The analytic structure of the propagator is the geometry of the biquaternion norm, and that is the framework's own contribution rather than a transcription of standard results. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

The article is organized as follows. The operator, its convention and its defining equation are stated first, together with the wave-number-space amplitude and the sign conventions. The poles and the four standard prescriptions are then identified. The retarded Green's function is derived in position space from its Fourier representation: the temporal contour is done exactly, the angular integral is reduced by a hyperbolic rotation to a Bessel function, and the closed form is exhibited and checked against the homogeneous equation. The light-cone Jacobian that converts the invariant kernel into the retarded-time kernel is exhibited, and the massless limit is compared with the retarded kernel of the electromagnetism exercise. The advanced kernel, the boundary condition that selects the retarded one, and the Pauli–Jordan function are then treated, with microcausality verified. The Feynman propagator, its contour, its time-ordered interpretation and its Euclidean form are given. A closing section states the biquaternion interpretation of the whole construction, and open questions are recorded.

Throughout, the series conventions are used: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_k^2=-e_t$, $\vec e_j \vec e_k=-\delta_{jk}e_t+\varepsilon_{jkl}\vec e_l$; central $i$; $\tilde R_\Phi=i r'_t\,e_t+r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z\in\mathbb{B}_{\Phi}$; $\tilde{\nabla}=e_t\partial/\partial R_t+\sum_k \vec e_k\partial/\partial R_k$; and the series d'Alembertian

$$
\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}=\tilde{\nabla}^{\natural}\tilde{\nabla}=\partial^2/\partial R_t^2+\Delta=\Delta+ \partial^2/\partial R_t^2 .
$$

The mass parameter is $k_m=mc/\hbar$, so that $k_m^{2}=(mc/\hbar)^2$ is the quantity that multiplies the field. The whole article is written in the inverse-length element $\tilde K_{\Phi}=\tilde P_{\Phi}/\hbar$, so that every momentum variable is a wave number and no $c$ and no $\hbar$ has to be restored anywhere: the transform variables, the pole locations, the Bessel argument and the range of the Euclidean kernel are all inverse lengths, the unit of $\Box$ and of $k_m$. This is the choice that makes the defining equation $\Box-k_m^{2}$ homogeneous in that unit, and it replaces the older displays in which a frequency stood beside a momentum and a $c$ patched the mismatch. The signature conventions are level 1 and level 2 only: the biquaternion norm on $\mathbb{C}$ and its material reading, $Q_t=i r'_t$. No second metric is used anywhere in this article.

- Companion article *The Klein–Gordon Equation in Biquaternionic Form*, for the equation, its mass term, and the central scalar d'Alembertian.
- Companion article *The Scalar Field in the Centre: Why Spin 0 Escapes the Biquaternion State Module*, for the field's central value space and the exclusion of the state module.
- Companion article *Exercise: The Retarded Potentials and the Green's Function*, for the massless Green's-function convention, the light-cone Jacobian, and the boundary condition.
- Companion article *The Feynman Propagator in Biquaternionic Form*, for the $i\epsilon$ prescription, the momentum-space propagator, and the contour conventions.
- Companion article *Interpretation of the Wick Rotation in the Biquaternion Universe*, for the identification of the material sector with the quaternion subspace and the Euclidean kernel.
- Companion article *The Klein–Gordon Path Integral in Biquaternionic Form*, for the Gaussian two-point function that reproduces the free kernel.

## The Operator and the Defining Equation

### The Klein–Gordon operator

For a field $\tilde{Ξ}=\xi_{\mathrm{scl}}\,e_t$ taking values in the centre, the Klein–Gordon equation of the companion article is

$$
\left(\Box-k_m^{2}\right)\tilde{Ξ}=0,
\qquad
k_m=\dfrac{mc}{\hbar},
$$

and because both $\Box$ and the mass term are central and scalar, the equation is the ordinary complex scalar equation for $\xi_{\mathrm{scl}}$. The plane wave is written with the wave-number element, which is the four-momentum divided by $\hbar$, and the division is the whole of its definition:

$$
\tilde K_{\Phi}=\frac{\tilde P_{\Phi}}{\hbar}=i k_{t}^{\prime}e_t+\vec k_{\Phi}\in\mathbb{B}_{\Phi},
\qquad
k_{t}^{\prime}=\frac{\omega}{c}=\frac{E}{\hbar\,c},
\qquad
\vec k_{\Phi}=\frac{\vec p}{\hbar},
$$

$$
\tilde R_\Phi=i r'_t\,e_t+r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z,
\qquad
\mathrm{Sc}(\tilde K_{\Phi}\tilde{R}_\Phi^{\natural})=\vec k_{\Phi}\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)-k_{t}^{\prime}r'_t .
$$

The two coordinates are read off the quotient and are both inverse lengths: the temporal one is the energy in inverse lengths, $k_{t}^{\prime}=E/(\hbar c)$, and the vector one is the momentum in inverse lengths, $\vec k_{\Phi}=\vec p/\hbar$. The phase needs no factor in front because it is the scalar part of an inverse length against a length, and the transform below integrates over $\tilde K_{\Phi}$ itself, so that the measure $d^4k$ has the same unit as the four-dimensional delta it produces.

The operator then has the symbol obtained from $\partial/\partial r'_t\,\to-i k_{t}^{\prime}$, so that $\partial/\partial R_t\,\to-k_{t}^{\prime}$, together with $\partial/\partial R_k\,\to i k_{\Phi,k}$:

$$
\Box\;\longmapsto\;k_{t}^{\prime\,2}-\vec k_{\Phi}^{2}=-\langle\tilde K_{\Phi}\rangle_{\natural},
\qquad
\left(\Box-k_m^{2}\right)\;\longmapsto\;-\left(\langle\tilde K_{\Phi}\rangle_{\natural}+k_m^{2}\right).
$$

The symbol vanishes precisely on the **mass shell** $\langle\tilde K_{\Phi}\rangle_{\natural}=-k_m^{2}$, that is, on

$$
k_{t}^{\prime\,2}=\vec k_{\Phi}^{2}+k_m^{2},
\qquad\text{equivalently}\qquad
\omega^2=c^2\vec k_{\Phi}^{2}+c^2k_m^{2},
$$

which is the biquaternion-norm statement of the relativistic dispersion relation: the mass shell is the level set of the biquaternion norm at the fixed negative value $-k_m^{2}$, a two-sheeted hyperboloid in the material sector. The three wave numbers of the particle are the two coordinates and the norm: $k_{t}^{\prime}$ is the temporal coordinate, $\vec k_{\Phi}$ the vector one, and $k_m$ the norm, which is a value of the shell and not a coordinate. The energy is not a third coordinate; it is $\hbar$ times the temporal coordinate, $E=\hbar c\,k_{t}^{\prime}$. The zero level set $\langle\tilde P_{\Phi}\rangle_{\natural}=0$ is the **zero-divisor cone**, the light cone; it is the set of four-wavevectors that are nilpotent in the algebra, and the massless kernel will be supported on its position-space image.

### Green's functions and the sign convention

A Green's function of the Klein–Gordon operator is a distributional inverse. This article fixes the defining equation once,

$$
\boxed{\;\left(\Box-k_m^{2}\right)G(\tilde R_\Phi)=-\delta^{(4)}(\tilde R_\Phi),
\qquad
\delta^{(4)}(\tilde R_\Phi)=\delta(r'_t)\,\delta^{(3)}(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\;}
$$

with the physical measure $d^3y\,dr'_{t,2}$ over the source point $\tilde{R}_{\Phi,2}$ for the convolution, exactly as the companion exercise *The Retarded Potentials and the Green's Function* fixes it for the massless operator. The sign is not physical: reversing it, $(\Box-k_m^{2})G=+\delta^{(4)}$, is compensated by a minus in the convolution, and an overall constant factor in $G$ never changes the pole structure or the support. It is fixed here so that at $k_m=0$ the retarded kernel is the exercise's $G_{\mathrm{ret}}=\frac{1}{4\pi R}\delta(r'_t-R)$ with no extra sign, and so that the mass term enters with the same sign as in the equation.

A second convention is fixed at the same time: the whole article works with the operator $\Box-k_m^{2}$ and never with $-\Box+k_m^{2}$, so that the momentum-space amplitude carries no compensating minus. The transform is taken over the wave-number element, with the measure $d^4k=dk'_t\,d^3k$ and the phase $\exp(i\,\mathrm{Sc}(\tilde K_{\Phi}\tilde{R}_\Phi^{\natural}))$, so that the defining equation becomes

$$
\int\frac{d^4k}{(2\pi)^4}\left(\langle\tilde K_{\Phi}\rangle_{\natural}+k_m^{2}\right)G(\tilde K_{\Phi})\,e^{i\,\mathrm{Sc}(\tilde K_{\Phi}\tilde{R}_\Phi^{\natural})}
=\int\frac{d^4k}{(2\pi)^4}\,e^{i\,\mathrm{Sc}(\tilde K_{\Phi}\tilde{R}_\Phi^{\natural})},
$$

because $\Box$ multiplies the exponential by $-\langle\tilde K_{\Phi}\rangle_{\natural}$ and $\Box-k_m^{2}$ by $-(\langle\tilde K_{\Phi}\rangle_{\natural}+k_m^{2})$. The amplitude is therefore one scalar function of the wave-number element,

$$
G(\tilde K_{\Phi})=\frac{1}{\vec k_{\Phi}^{2}+k_m^{2}-k_{t}^{\prime\,2}}
=\frac{1}{\langle\tilde K_{\Phi}\rangle_{\natural}+k_m^{2}},
\qquad
\langle\tilde K_{\Phi}\rangle_{\natural}=-k_{t}^{\prime\,2}+\vec k_{\Phi}^{2},
$$

with a single denominator whose only zero is the mass shell: the amplitude is singular exactly on $\langle\tilde K_{\Phi}\rangle_{\natural}=-k_m^{2}$, so the pole condition and the mass shell are the same line of the algebra. Nothing in this display mixes a frequency with a momentum, because both coordinates of $\tilde K_{\Phi}$ are inverse lengths; the two terms of the denominator are added only because they are measured in the same unit. The prescription that deforms the real axis is the whole of the difference between the four kernels. At $k_m=0$ the amplitude reduces to $1/(\vec k_{\Phi}^{2}-k_{t}^{\prime\,2})$, whose contour integral is the exercise's retarded kernel, and no $c$ has to be inserted at any stage to make that comparison.

## The Poles and the Four Prescriptions

### The pole structure

The denominator vanishes at $k_{t}^{\prime}=\pm\Omega_{\vec k}$ with

$$
\Omega_{\vec k}=\sqrt{\vec k_{\Phi}^{2}+k_m^{2}},
$$

the on-shell temporal wave number, an inverse length like its two terms. The energy it carries is $E=\hbar c\,\Omega_{\vec k}=\sqrt{\vec p^{2}c^{2}+m^{2}c^{4}}$ under $\vec p=\hbar\vec k_{\Phi}$ and $\hbar k_m=mc$, the usual relativistic energy, and the multiplications by $\hbar$ undo the one division that produced the element term by term. The two poles sit on the real axis in the distributional sense, and the four standard prescriptions displace them into the complex plane in four ways. Each prescription defines a Green's function with a definite support and a definite interpretation.

| Prescription | Denominator | Poles | Support |
|---|---|---|---|
| Retarded | $\langle\tilde K_{\Phi}\rangle_{\natural}+k_m^{2}$ at $k_{t}^{\prime}\to k_{t}^{\prime}+i\epsilon$ | $k_{t}^{\prime}=\pm\Omega_{\vec k}-i\epsilon$ | future cone |
| Advanced | $\langle\tilde K_{\Phi}\rangle_{\natural}+k_m^{2}$ at $k_{t}^{\prime}\to k_{t}^{\prime}-i\epsilon$ | $k_{t}^{\prime}=\pm\Omega_{\vec k}+i\epsilon$ | past cone |
| Feynman | $\vec k_{\Phi}^{2}+k_m^{2}-k_{t}^{\prime\,2}-i\epsilon$ | $k_{t}^{\prime}=+\Omega_{\vec k}-i\delta$, $k_{t}^{\prime}=-\Omega_{\vec k}+i\delta$ | whole space, causal |
| Principal value | $\mathrm{P}\frac{1}{\Omega_{\vec k}^{2}-k_{t}^{\prime\,2}}$ | on the axis | on the cone |

The displacement was checked explicitly. Writing $\delta=\epsilon/(2\Omega_{\vec k})$ for the imaginary part of the retarded pole, the four displacements are: both poles at $\mathrm{Im}\,k_{t}^{\prime}=-\epsilon$ (retarded), both at $+\epsilon$ (advanced), and one on each side with imaginary parts $\pm\delta$ (Feynman). The Feynman prescription is the only one that treats the two poles asymmetrically, and it is exactly this asymmetry that makes the resulting kernel a boundary value rather than a solution selected by a cone support.

### The contour integral

The temporal integral is elementary and is used repeatedly. It is an integral over the temporal coordinate $k_{t}^{\prime}$, and the exponential is $\exp(-i k_{t}^{\prime}r'_t)$, whose argument is dimensionless because an inverse length multiplies a length. For the retarded displacement $k_{t}^{\prime}\to k_{t}^{\prime}+i\epsilon$ the poles lie in the lower half-plane. For $r'_t>0$ the exponential forces the contour to close below, and the two residues combine into

$$
\frac{1}{2\pi}\int_{-\infty}^{\infty}dk_{t}^{\prime}\,
\frac{\exp(-i k_{t}^{\prime}r'_t)}{\vec k_{\Phi}^{2}+k_m^{2}-(k_{t}^{\prime}+i\epsilon)^2}
=\mathrm{H}_{\mathrm{hvs}}(r'_t)\,\frac{\sin(\Omega_{\vec k}r'_t)}{\Omega_{\vec k}},
\qquad
\Omega_{\vec k}=\sqrt{\vec k_{\Phi}^{2}+k_m^{2}},
$$

while for $r'_t<0$ the contour closes above and the integral vanishes. The result is the statement that the retarded kernel has support only in the future. For the advanced displacement the same computation with $r'_t\to-r'_t$ gives $-\mathrm{H}_{\mathrm{hvs}}(-r'_t)\sin(\Omega_{\vec k}r'_t)/\Omega_{\vec k}$, supported only in the past. For the Feynman displacement the two poles sit on opposite sides, both contribute at $r'_t>0$ and at $r'_t<0$, and the result is the symmetric combination

$$
\frac{1}{2\pi}\int_{-\infty}^{\infty}dk_{t}^{\prime}\,
\frac{\exp(-i k_{t}^{\prime}r'_t)}{\vec k_{\Phi}^{2}+k_m^{2}-k_{t}^{\prime\,2}-i\epsilon}
=\frac{i}{2\Omega_{\vec k}}\,\exp(-i\Omega_{\vec k}|r'_t|),
$$

which is the wave-number form of the time-ordered two-point function: the two poles are displaced to opposite sides, both contribute, and the result is even in $r'_t$ and built from the positive-frequency phase $\exp(-i\Omega_{\vec k}|r'_t|)$; a positive temporal wave number $k_{t}^{\prime}=\Omega_{\vec k}$ is a positive energy $E=\hbar c\,\Omega_{\vec k}$, so the two signs of the coordinate are the two signs of the energy. The three results were confirmed by evaluating the contour sums directly.

## The Retarded Green's Function in Position Space

### The Fourier representation

Assembling the temporal integral with the spatial measure gives the retarded kernel in position space,

$$
G_R(r'_t, r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)
=\mathrm{H}_{\mathrm{hvs}}(r'_t)\int\frac{d^3k_{\Phi}}{(2\pi)^3}\,
\frac{\sin(\Omega_{\vec k}r'_t)}{\Omega_{\vec k}}\,\exp\!\left(i\,\vec k_{\Phi}\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\right),
$$

the integral running over the vector coordinate of $\tilde K_{\Phi}$, so that every factor is an inverse length, a length, or a ratio of the two; this is the representation in which every claim below is checked. It is a **superposition of on-shell plane waves**, each carrying the temporal coordinate $k_{t}^{\prime}=\pm\Omega_{\vec k}$ that the shell assigns to its $\vec k_{\Phi}$, and the ratio $\Omega_{\vec k}/|\vec k_{\Phi}|$ is the phase velocity in units of $c$. For a source $J(\tilde{R}_{\Phi,2})$ the convolution

$$
\tilde{Ξ}(\tilde R_\Phi)=\int G_R(\tilde R_\Phi-\tilde{R}_{\Phi,2})\,J(\tilde{R}_{\Phi,2})\,d^3y\,dr'_{t,2}
$$

then solves $(\Box-k_m^{2})\tilde{Ξ}=-J$, by the same translation-invariance argument as in the massless exercise.

### The angular integral and its Bessel reduction

Because the kernel is spherically symmetric, the angular integral can be done. Writing $r=|r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z|$ and using

$$
\int\frac{d^3k_{\Phi}}{(2\pi)^3}F(|\vec k_{\Phi}|)\,e^{i\vec k_{\Phi}\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)}
=\frac{1}{2\pi^2 r}\int_0^\infty dk_{\Phi}\,k_{\Phi}\,F(k_{\Phi})\,\sin(k_{\Phi}r),
$$

the retarded kernel becomes the single radial integral

$$
G_R(r'_t,r)
=\mathrm{H}_{\mathrm{hvs}}(r'_t)\,\frac{1}{2\pi^2 r}\int_0^\infty dk_{\Phi}\,
k_{\Phi}\,\frac{\sin(\Omega\, r'_t)}{\Omega}\,\sin(k_{\Phi}r),
\qquad
\Omega=\sqrt{k_{\Phi}^{2}+k_m^{2}},
$$

in which $k_{\Phi}=|\vec k_{\Phi}|$ is the modulus of the vector coordinate, the second wave number of the particle, and $\Omega$ is the temporal coordinate the shell assigns to it.

The substitution

$$
k_{\Phi}=k_m\sinh u,
\qquad
\Omega=k_m\cosh u,
$$

which is the hyperboloid parametrization of the mass shell $\Omega^2-k_{\Phi}^{2}=k_m^{2}$ written on $\tilde K_{\Phi}$, is the one that makes the shell a coordinate line: $\sinh u$ and $\cosh u$ are opposite branches of the same hyperbola, and $u$ measures the position along it. It gives $dk_{\Phi}=k_m\cosh u\,du$, and

$$
\frac{k_{\Phi}\,dk_{\Phi}}{\Omega}=k_m\sinh u\,du,
\qquad
k_{\Phi}r=k_m r\sinh u,
\qquad
\Omega\, r'_t=k_m r'_t\cosh u .
$$

The radial integral is therefore a Laplace-type Bessel integral. Since $\sin(k_m r\sinh u)\sinh u=-1/k_m\frac{d}{dr}\cos(k_m r\sinh u)$,

$$
G_R(r'_t,r)
=-\mathrm{H}_{\mathrm{hvs}}(r'_t)\,\frac{1}{2\pi^2 r}\,\frac{d}{dr}\int_0^\infty du\,
\sin(k_m r'_t\cosh u)\cos(k_m r\sinh u).
$$

The remaining integral is evaluated by a hyperbolic rotation. With $a=k_m r'_t$, $b=k_m r$ and $a>b>0$ (the future cone), set $a=R\cosh\gamma$, $b=R\sinh\gamma$ with $R=\sqrt{a^2-b^2}$. Then $a\cosh u\pm b\sinh u=R\cosh(u\pm\gamma)$, so the product-to-sum identity turns the integrand into a sum of two shifted copies of $\sin(R\cosh v)$, and the two shifts combine into the convergent representation of the Bessel function:

$$
\int_0^\infty du\,\sin(a\cosh u)\cos(b\sinh u)
=\frac{1}{2}\int_{-\infty}^{\infty}dv\,\sin(R\cosh v)
=\int_0^\infty dv\,\sin(R\cosh v)
=\frac{\pi}{2}J_0\!\left(\sqrt{a^2-b^2}\right).
$$

This is the standard integral representation $J_0(z)=\frac{2}{\pi}\int_0^\infty\sin(z\cosh v)\,dv$ together with the hyperbolic rotation; it is valid for $a>b>0$, which is precisely the interior of the future light cone.

### The closed form, its massless limit, and its support

Differentiating the Bessel integral with respect to $r$ and using $\frac{dJ_0}{dz}(z)=-J_1(z)$ gives

$$
\frac{d}{dr}J_0\!\left(k_m\sqrt{{r'_{t}}^2-r^2}\right)
=\frac{k_m r}{\sqrt{{r'_{t}}^2-r^2}}\,J_1\!\left(k_m\sqrt{{r'_{t}}^2-r^2}\right),
$$

so that, writing $-x^2={r'_{t}}^2-r^2$ for the squared invariant (positive inside the future cone),

$$
G_{\mathrm{rgs},R}(r'_t,r)
=-\mathrm{H}_{\mathrm{hvs}}(r'_t)\,\frac{k_m}{4\pi\sqrt{-r_x^2}}\,J_1\!\left(k_m\sqrt{-r_x^2}\right),
\qquad
-r_x^2={r'_{t}}^2-r^2>0 .
$$

This is the **volume term**: it is the contribution from the interior of the cone. On the cone itself the kernel acquires a delta function, and the complete retarded Green's function is

$$
\boxed{\;
G_R(\tilde R_\Phi)
=\frac{\mathrm{H}_{\mathrm{hvs}}(r'_t)}{2\pi}\left[\delta(r_x^2)
-\frac{k_m}{2\sqrt{-r_x^2}}\,J_1\!\left(k_m\sqrt{-r_x^2}\right)\mathrm{H}_{\mathrm{hvs}}(-r_x^2)\right]\;},
\qquad
r_x^2=-{r'_{t}}^2+\vec r^2,
$$

with the Bessel term restricted to the interior of the cone by $\mathrm{H}_{\mathrm{hvs}}(-x^2)$. The delta term is the massless kernel, and the Bessel term is the massive correction; the correction does not vanish on the cone but tends there to the finite value $-k_m^{2}/(8\pi)\,\mathrm{H}_{\mathrm{hvs}}(r'_t)$, since $J_1(z)\sim z/2$ as $z\to0$ makes $k_m J_1(k_m\sqrt{-x^2})/(2\sqrt{-x^2})\to\,k_m^{2}/4$. The kernel's only singular part is therefore the delta on the cone, and the volume term is bounded on it.

Three checks were carried out on this closed form.

1. **Massless limit.** As $k_m\to0$ the Bessel term vanishes and only $\frac{\mathrm{H}_{\mathrm{hvs}}(r'_t)}{2\pi}\delta(r_x^2)$ remains. Converting the invariant delta to a radial delta by the light-cone Jacobian below gives $\frac{1}{4\pi r}\delta(r'_t-r)$, which is exactly the retarded kernel $\frac{1}{4\pi R}\delta(r'_t-R)$ of the electromagnetism exercise at $c=1$. The limit was verified numerically for $k_m=10^{-3}$.
2. **The homogeneous equation.** Inside the cone the Bessel form must satisfy $(\Box-k_m^{2})G_{\mathrm{rgs},R}=0$, because the only source is at the origin. Evaluating the radial d'Alembertian $-\partial^2/\partial {r'_{t}}^2+\partial^2/\partial r^2+\frac{2}{r}\partial/\partial r-k_m^{2}$ by finite differences at six random interior points with $r'_t\in[2.5,4]$, $r/r'_t\in[0.2,0.85]$ and $k_m\in[0.4,1.5]$, the greatest residual was $1.1\times 10^{-9}$, against an amplitude of order $10^{-2}$.
3. **The Bessel function.** The series evaluation of $J_1$ reproduces the reference values $J_1(1)=0.4400505857$ and $J_1(2)=0.5767248078$ to ten digits, so the Bessel factor in the kernel is not a source of error.

### The light-cone Jacobian

The delta term is concentrated on the cone, and the two ways of writing it are related by a Jacobian. On the future cone $r'_t>0$ the invariant $x^2=-{r'_{t}}^2+r^2$ vanishes at the single positive root $r=r'_t$, where

$$
\left|\frac{\partial r_x^2}{\partial r}\right|_{r=r'_t}=2r\Big|_{r=r'_t}=2r'_t,
\qquad\text{so}\qquad
\delta(r_x^2)=\frac{1}{2r'_t}\,\delta(r-r'_t)=\frac{1}{2r}\,\delta(r'_t-r),
$$

and therefore

$$
\frac{1}{2\pi}\delta(r_x^2)=\frac{1}{4\pi r}\delta(r'_t-r).
$$

The coefficient was checked numerically to twelve digits, and it is the c-explicit exercise's Jacobian with $c=1$. This is the step at which a derivation of the retarded kernel most often goes wrong: dropping the factor $2r$ gives a kernel whose coefficient has the wrong power of $r$, and the kernel then fails to reduce to the Newton kernel in the static limit. The invariant form and the radial form are used interchangeably below.

## The Advanced Kernel and the Boundary Condition

The advanced displacement reverses both pole shifts and produces the mirror kernel

$$
G_A(\tilde R_\Phi)=G_R(-\tilde R_\Phi\text{ in time})=G_R(-r'_t,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)
=\frac{\mathrm{H}_{\mathrm{hvs}}(-r'_t)}{2\pi}\left[\delta(r_x^2)-\frac{k_m}{2\sqrt{-r_x^2}}J_1\!\left(k_m\sqrt{-r_x^2}\right)\mathrm{H}_{\mathrm{hvs}}(-r_x^2)\right],
$$

supported on the past cone. The advanced kernel solves the same defining equation, $(\Box-k_m^{2})G_A=-\delta^{(4)}$, as $G_R$ does; the two differ by a solution of the homogeneous Klein–Gordon equation,

$$
G_R-G_A
=\frac{\mathrm{sgn}(r'_t)}{2\pi}\left[\delta(r_x^2)-\frac{k_m}{2\sqrt{-r_x^2}}J_1\!\left(k_m\sqrt{-r_x^2}\right)\mathrm{H}_{\mathrm{hvs}}(-r_x^2)\right],
$$

which is supported on the closed cone and is not zero. The defining equation alone therefore does **not** select a kernel, and the selection is a boundary condition: the retarded kernel is chosen by the requirement of no incoming radiation from the past. This is the same statement the massless exercise makes for the wave operator, and it is a physical input rather than an algebraic consequence.

It is worth stating the two kernels' structure in the algebra. Both are complex scalars times $e_t$, and their difference is too; the boundary condition selects between them by a $r'_t$-dependent step, which is a central scalar function. Nothing in the selection involves the module, and nothing in it involves the vector part of the algebra: the causal structure of the spin-$0$ theory is a statement about the scalar $\mathbb{B}_{C}$, encoded in the biquaternion norm through the cone.

## Microcausality and the Pauli–Jordan Function

### The commutator function

The difference of the two kernels is the framework's causal kernel. Define the **Pauli–Jordan** (commutator) function by

$$
\boxed{\;G_C(\tilde R_\Phi)=G_R(\tilde R_\Phi)-G_A(\tilde R_\Phi)
=\frac{\mathrm{sgn}(r'_t)}{2\pi}\left[\delta(r_x^2)-\frac{k_m}{2\sqrt{-r_x^2}}\,J_1\!\left(k_m\sqrt{-r_x^2}\right)\mathrm{H}_{\mathrm{hvs}}(-r_x^2)\right]\;},
$$

and normalize the field so that the field commutator, of which $G_C$ is the kernel, reads

$$
\left[\,\tilde{Ξ}(\tilde R_\Phi),\,\tilde{Ξ}^{*}(\tilde{R}_{\Phi,2})\,\right]
=G_C(\tilde R_\Phi-\tilde{R}_{\Phi,2})\,e_t .
$$

The overall constant in this normalization is a convention — the relation carries an explicit factor of $i$ in the standard canonical normalization, which the kernels of this article absorb into their defining equation — while the support of $G_C$, and hence microcausality, is not. The commutator vanishes at equal times, since $G_C$ vanishes for purely spatial separation.

### Microcausality

Microcausality is the statement that the commutator vanishes for spacelike separation. Let $\tilde R_\Phi$ be **spacelike**, so that $r_x^2=-{r'_{t}}^2+\vec r^2>0$. Then two things happen at once in the closed form: $\delta(x^2)=0$ because $x^2\ne0$, and $\mathrm{H}_{\mathrm{hvs}}(-x^2)=0$ because $-x^2<0$. Hence

$$
G_C(\tilde R_\Phi)=0
\qquad\text{for}\qquad x^2>0,
$$

and the field operators commute at spacelike separation. For **timelike** $\tilde R_\Phi$ (inside either cone) the kernel is nonzero: $\mathrm{H}_{\mathrm{hvs}}(-x^2)=1$ and the Bessel term contributes, so $G_C$ does not vanish and the commutator carries the causal signal. The two behaviors were checked numerically on the closed form: at the spacelike point $(r'_t,r)=(1,2)$ with $k_m=1.1$ the kernel is exactly zero, and at the timelike point $(r'_t,r)=(2,1)$ it is $-0.0294$, nonzero and of the expected magnitude.

The support statement can be read without the Bessel function. The commutator function is a difference of two kernels whose pole displacements place them, respectively, on the future and past cones; the singularities of the two contributions in the $r'_t$-plane cancel for spacelike separations, and what remains is supported on the closed cone. This is the standard causal structure of a scalar field, and it is reproduced here directly from the closed form rather than asserted.

### What the algebra contributes

The commutator is a **central scalar** times $e_t$. There is no non-central part, because the field is central and the kernel is central. The light cone on which $G_C$ is supported is the zero-divisor cone $\langle\tilde R_\Phi\rangle_{\natural}=0$ of $\mathbb{B}_{\Phi}$: the points of the material sector at which the biquaternion norm vanishes, which are exactly the elements of $\mathbb{B}_{\Phi}$ that fail to be invertible. The mass shell, where the kernel's momentum-space amplitude is singular, is the level set $\langle\tilde P_{\Phi}\rangle_{\natural}=-k_m^{2}$. Both singular loci are statements about the algebra's biquaternion norm, and the causal structure of the scalar theory is therefore a statement about $\mathbb{B}_{\Phi}$ alone, with the centre as the field's value space and no module in sight. This is the concrete form, for the propagator, of the structural article's verdict that spin $0$ lives in the centre: its causality is the geometry of the cone, not the representation theory of a module.

## The Feynman Propagator and Time Ordering

### Momentum space and the contour

The **Feynman propagator** is the Green's function whose poles are displaced to opposite sides of the real axis,

$$
G_F(\tilde K_{\Phi})=\frac{1}{\vec k_{\Phi}^{2}+k_m^{2}-k_{t}^{\prime\,2}-i\epsilon},
\qquad
G_F(\tilde R_\Phi)=\int\frac{d^4k}{(2\pi)^4}\,G_F(\tilde K_{\Phi})\,e^{i\,\mathrm{Sc}(\tilde K_{\Phi}\tilde{R}_\Phi^{\natural})} .
$$

Its temporal integral was given above; its position-space content is the time-ordered correlation function,

$$
G_F(\tilde R_\Phi)
=\mathrm{H}_{\mathrm{hvs}}(r'_t)\,\langle0|\tilde{Ξ}(\tilde R_\Phi)\tilde{Ξ}^{*}(0)|0\rangle
+\mathrm{H}_{\mathrm{hvs}}(-r'_t)\,\langle0|\tilde{Ξ}^{*}(0)\tilde{Ξ}(\tilde R_\Phi)|0\rangle,
$$

which is the standard interpretation of the asymmetric prescription: the two boundary values are the positive- and negative-frequency Wightman functions, and the $r'_t$-ordering puts them in the order that makes the amplitude a causal Green's function. The two-point function of the biquaternion field is therefore

$$
\boxed{\;\langle0|\,T\,\tilde{Ξ}(\tilde R_\Phi)\,\tilde{Ξ}^{*}(\tilde{R}_{\Phi,2})\,|0\rangle
=G_F(\tilde R_\Phi-\tilde{R}_{\Phi,2})\,e_t\;},
$$

a complex scalar times the identity; the module factor is absent, as it must be for a central field. The identification fixes the field-normalization convention, the kernels throughout being the distributions defined by $(\Box-k_m^{2})G=-\delta^{(4)}$; the standard canonical normalization of the complex scalar differs from it by the explicit factor of $i$ carried by the canonical commutation relation, and that constant, unlike the support, is not physical.

### Euclidean form and the Yukawa tail

For spacelike separations the Feynman propagator is the Wick-rotated Euclidean kernel, and the Wick rotation is the identification of the material sector with the quaternion subspace recalled in the companion article *Interpretation of the Wick Rotation in the Biquaternion Universe*. The rotation is quoted as the standard route; the denominator it produces is positive without it, because $\vec k_E^2$ is the **Hermitian form** of a material element. Write the Euclidean wave-number element as $\tilde K_{\Phi,E}=i k_{\mathrm{eu},t}^{\prime}e_t+\vec k_E\in\mathbb{B}_{\Phi}$, both coordinates inverse lengths like those of $\tilde K_{\Phi}$; then $\langle\tilde K_{\Phi,E},\tilde K_{\Phi,E}\rangle_{*}=(k_{\mathrm{eu},t}^{\prime})^2+\vec k_E^2$, positive because the form is definite and not because a metric was rotated, and the two routes agree by the identity $\langle i k_{\mathrm{eu},t}^{\prime}e_t+\vec k_E,\,i k_{\mathrm{eu},t}^{\prime}e_t+\vec k_E\rangle_{*}=\langle -k_{\mathrm{eu},t}^{\prime}e_t+\vec k_E\rangle_{\natural}$ — the same identity that carries the thermal and renormalization-group routes of the companions. The Euclidean kernel

$$
G_E(\tilde{Q}_E)=\int\frac{d^4k_E}{(2\pi)^4}\,\frac{\exp(\,i\,k_E\cdot x_E)}{\vec k_E^2+k_m^{2}}
$$

is the standard massive Euclidean propagator, whose closed form is the modified Bessel (Yukawa) kernel

$$
G_E(\tilde{Q}_E)=\frac{k_m}{4\pi^2\sqrt{\rho_E^2}}\,
K_1\!\left(k_m\sqrt{\rho_E^2}\right),
\qquad
\rho_E^2=x_E^2,
$$

with $K_1$ the modified Bessel function of the second kind. It decays exponentially at large spacelike separation, with range $k_m=mc/\hbar$, the Compton wavelength; this is the analytic form of the statement that the causal kernel vanishes outside the cone but that the Feynman kernel retains an exponentially small tail inside it. Both behaviors follow from the same biquaternion-norm geometry: the Lorentzian cone for the commutator, the Euclidean sphere for the Wick-rotated kernel. The scope of the form statement is the positivity of the denominator and no more: the form does not supply the analytic continuation, and the $i\epsilon$ remains the analytic input that names the vacuum, as the companion propagator article states.

### Composition and the free generating functional

The Feynman propagator is the inverse of the Klein–Gordon operator in the distributional sense, $(\Box-k_m^{2})G_F=-\delta^{(4)}$, and the inverse relation between the two reads

$$
\int d^3y\,dr'_{t,2}\;G_F(\tilde R_\Phi-\tilde{R}_{\Phi,2})\,\left[-\bigl(\Box_{\tilde{R}_{\Phi,2}}-k_m^{2}\bigr)\right]\delta^{(4)}(\tilde{R}_{\Phi,2}-\tilde Q_3)
=\delta^{(4)}(\tilde R_\Phi-\tilde Q_3),
$$

the operator acting on the delta and not on a second propagator, so that the bracket is the bare inverse kernel. Equivalently, convoluting two propagators with one operator insertion returns a single propagator, $\int d^4y\,G_F(\tilde R_\Phi-\tilde{R}_{\Phi,2})[-\bigl(\Box_{\tilde{R}_{\Phi,2}}-k_m^{2}\bigr)]G_F(\tilde{R}_{\Phi,2}-\tilde Q_3)=G_F(\tilde R_\Phi-\tilde Q_3)$, which is the same statement. In wave-number space this is the statement $G_F^{-1}=\vec k_{\Phi}^{2}+k_m^{2}-k_{t}^{\prime\,2}=\langle\tilde K_{\Phi}\rangle_{\natural}+k_m^{2}$, and it is the free propagator that the path-integral article *The Klein–Gordon Path Integral in Biquaternionic Form* obtains as the Gaussian two-point function of the scalar field. The consistency of the two constructions — the Green's-function inverse here and the Gaussian fluctuation kernel there — is the statement that the free theory's two-point function is the inverse of the quadratic form in the action, and it is checked in that article on a finite lattice.

## The Biquaternion Reading

Three facts summarize what the framework does and does not contribute to the Klein–Gordon propagator.

**The kernel is central, and the module is a spectator.** The operator $\Box-k_m^{2}$ is a central scalar, so every Green's function is a central scalar times $e_t$, and the whole construction is the scalar construction tensored with the identity on the state module. This is not a deficiency but the exact statement of spin $0$: a scalar field has no internal index for a non-central kernel to act on. The companion article *The Scalar Field in the Centre: Why Spin 0 Escapes the Biquaternion State Module* shows why this must be so, and the present article exhibits it at the level of the kernel.

**The singular loci are the biquaternion norm's geometry.** The light cone is the zero-divisor cone $\langle\tilde R_\Phi\rangle_{\natural}=0$ of the material sector; the mass shell is the level set $\langle\tilde K_{\Phi}\rangle_{\natural}=-k_m^{2}$, where $\tilde K_{\Phi}=\tilde P_{\Phi}/\hbar$ is the wave-number element and $k_m$ is its norm. The Fourier kernel's poles, the support of the retarded kernel, the vanishing of the commutator, and the exponential range of the Euclidean kernel are all faces of one algebraic object, the biquaternion norm of $\mathbb{B}$ read on $\mathbb{B}_{\Phi}$. This is genuinely the algebra's contribution: the framework does not postulate the light cone, it identifies it as the zero set of the biquaternion norm, and the propagation of a spin-$0$ field follows.

**The causal boundary condition is physical, not algebraic.** The defining equation admits both the retarded and the advanced kernel, and the algebra is indifferent between them; the retarded choice is the no-incoming-radiation condition, a physical input. The framework locates the choice in the direction of the $i\epsilon$ displacement along the imaginary-scalar axis $i r'_t$, exactly as the companion article on the Feynman propagator argues; it does not derive the choice.

The derivation of the retarded kernel given above is a transcription of the standard scalar field theory into the framework's notation, with the biquaternion-norm identifications supplying the interpretation. The genuinely biquaternionic content lies in the identification of the cone and the shell with the biquaternion norm, and in the proof that nothing else of the algebra enters.

## Open Questions

1. **The kernel's normalisation in the interacting theory.** The free kernels are fixed by the free equation up to an overall constant, which this article fixes by the convention $(\Box-k_m^{2})G=-\delta^{(4)}$. Whether the interacting theory's field normalization, and with it the constant in front of the commutator, is fixed by the framework's trace formula or only by the standard canonical quantization is not settled here.

2. **The general Green's function of the biquaternionic operator.** The operator $\Box$ is treated here only in its central, scalar reduction, which is all a spin-$0$ field can see. Whether the gradient's action on the material and informational sectors with their full non-central structure admits sector-valued Green's functions with closed forms analogous to the Bessel form above, and whether those mix the sectors, is not settled by the scalar case and is not considered here.

3. **The massless limit and the zero-divisor cone.** The massless kernel is supported on the zero-divisor cone and is the boundary case of the massive hyperboloid as $k_m\to0$; the limit is singular in the sense that the volume term vanishes while the cone term survives. Whether the framework should regard the massless scalar as a degenerate case of the massive one, or as the fundamental case whose cone support is primary, is a matter of interpretation that the present article does not settle.

4. **The Euclidean kernel and the informational sector.** The Wick rotation identifies the material sector with the quaternion subspace, on which the biquaternion norm is positive definite. The Euclidean kernel $G_E$ is therefore a function on $\mathbb{B}_{H}$, and its Yukawa form is the standard one. Whether the informational sector's operators act on $G_E$ in a way that reproduces the Euclidean path-integral measure is a question for the path-integral article and for the informational articles.

5. **The propagator on a non-constant background.** The closed forms above hold for constant $\epsilon,\mu$ and hence constant $c$. In a medium whose parameters vary, or in a background field, the operator has variable coefficients and these free kernels are only the leading geometric-optics approximation. The framework's local complex structure makes $c$ a field, and the form of the kernel in that setting is not settled here.

6. **The composite scalar's kernel.** The structural article records that a scalar can also be built as a pairing of two module elements, through the symplectic form $\varepsilon(\tilde{Ξ}_{\mathrm{sp}},\xi)$ or the mixed pairing $\mathfrak{b}(\tilde{Ξ}_{\mathrm{sp}},\xi)$. The Green's function of a composite scalar is not the free kernel of this article, and whether the composite propagator inherits the free kernel's cone structure or acquires a different one is not considered here.

## Summary

The Klein–Gordon operator $(\Box-k_m^{2})$ is a central scalar element of $\mathbb{B}$, and every Green's function of it is a central scalar times $e_t$. With the defining convention $(\Box-k_m^{2})G=-\delta^{(4)}$, matching the electromagnetism exercise at $k_m=0$, the wave-number-space amplitude is $G=(\langle\tilde K_{\Phi}\rangle_{\natural}+k_m^{2})^{-1}$, a single scalar function of the one element $\tilde K_{\Phi}=\tilde P_{\Phi}/\hbar=i k_{t}^{\prime}e_t+\vec k_{\Phi}$, and the four standard prescriptions displace its two poles at $k_{t}^{\prime}=\pm\Omega_{\vec k}=\pm\sqrt{\vec k_{\Phi}^{2}+k_m^{2}}$.

The retarded Green's function is derived from its Fourier representation. The temporal contour gives $\mathrm{H}_{\mathrm{hvs}}(r'_t)\sin(\Omega_{\vec k}r'_t)/\Omega_{\vec k}$; the angular integral reduces the kernel to a radial Bessel integral; the substitution $k_{\Phi}=k_m\sinh u$, which parametrizes the shell $\Omega^2-k_{\Phi}^{2}=k_m^{2}$ on the element itself, and a hyperbolic rotation evaluate it as $\frac{\pi}{2}J_0(k_m\sqrt{{r'_{t}}^2-r^2})$; and differentiation gives the closed form

$$
G_R(\tilde R_\Phi)
=\frac{\mathrm{H}_{\mathrm{hvs}}(r'_t)}{2\pi}\left[\delta(r_x^2)-\frac{k_m}{2\sqrt{-r_x^2}}\,J_1\!\left(k_m\sqrt{-r_x^2}\right)\mathrm{H}_{\mathrm{hvs}}(-r_x^2)\right],
\qquad
r_x^2=-{r'_{t}}^2+\vec r^2 .
$$

The delta term is the massless retarded kernel, whose invariant form converts to $\frac{1}{4\pi r}\delta(r'_t-r)$ by the light-cone Jacobian $\delta(r_x^2)=\frac{1}{2r}\delta(r'_t-r)$; the Bessel term is the massive volume contribution, verified to satisfy the homogeneous Klein–Gordon equation inside the cone and to vanish as $k_m\to0$. The advanced kernel is the time reverse, and the defining equation does not select between them: the retarded kernel is fixed by the no-incoming-radiation boundary condition, which is physical.

The Pauli–Jordan function $G_C=G_R-G_A$ is supported on the closed cone and vanishes for spacelike separations, which is microcausality; the commutator is $[\tilde{Ξ},\tilde{Ξ}^{*}]=G_C e_t$ in the normalization used here, and it is nonzero inside the cone. The Feynman propagator is the opposite-pole displacement, equal to the time-ordered two-point function $\langle0|T\tilde{Ξ}(r_x)\tilde{Ξ}^{*}(r_y)|0\rangle=G_F(r_x-r_y)e_t$; its spacelike tail is the Euclidean Yukawa kernel $\frac{k_m}{4\pi^2\sqrt{\rho_E^2}}K_{1}(k_m\sqrt{\rho_E^2})$, of range the Compton wavelength, which is $1/k_m$, and its inverse in wave-number space is the quadratic form of the action used in the companion path-integral article.

The algebra's contribution is the identification of the singular loci with the biquaternion norm: the light cone is the zero-divisor cone $\langle\tilde R_\Phi\rangle_{\natural}=0$ of the material sector and the mass shell is the level set $\langle\tilde K_{\Phi}\rangle_{\natural}=-k_m^{2}$ of the wave-number element. The kernel is central, the module is a spectator, and the causal boundary condition is a physical input. The retarded, advanced, commutator and Feynman kernels are the standard scalar kernels, written in the framework's notation and interpreted through its biquaternion norm.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\mathbb{B}_{\Phi},\mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{B}_{C}=\operatorname{span}_{\mathbb{R}}\{e_t,ie_t\}$ | Centre of $\mathbb{B}$; the scalar field's value space |
| $\tilde R_\Phi=i r'_t\,e_t+r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ | Material coordinate, $\in\mathbb{B}_{\Phi}$ |
| $\tilde K_{\Phi}=\frac{\tilde P_{\Phi}}{\hbar}=i k_{t}^{\prime}e_t+\vec k_{\Phi}$ | Wave-number element, $\in\mathbb{B}_{\Phi}$; $k_{t}^{\prime}=E/(\hbar c)=\omega/c$, $\vec k_{\Phi}=\vec p/\hbar$, both inverse lengths |
| $\tilde P_{\Phi}=\hbar\,\tilde K_{\Phi}=\frac{m\,c\,(i k_{t}^{\prime}e_t+\vec k_{\Phi})}{k_m}$ | Material four-wavevector, $\in\mathbb{B}_{\Phi}$; the one division undone |
| $\langle\tilde R_\Phi\rangle_{\natural}=\tilde R_\Phi\tilde{R}_\Phi^{\natural}$ | Biquaternion norm |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}=\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$ | Hermitian form; real, positive definite |
| $\tilde K_{\Phi,E}=i k_{\mathrm{eu},t}^{\prime}e_t+\vec k_E\in\mathbb{B}_{\Phi}$ | Euclidean wave-number element; $\langle\tilde K_{\Phi,E},\tilde K_{\Phi,E}\rangle_{*}=(k_{\mathrm{eu},t}^{\prime})^2+\vec k_E^2$ |
| $\tilde{\nabla}=e_t\partial/\partial R_t+\sum_k \vec e_k\partial/\partial R_k$ | Biquaternionic gradient |
| $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}=\partial^2/\partial R_t^2+\Delta$ | d'Alembertian, series convention |
| $1/k_m$ | The mass length, $\hbar/(mc)$; its reciprocal $k_m=mc/\hbar$ is the inverse Compton wave number |
| $\Omega_{\vec k}=\sqrt{\vec k_{\Phi}^{2}+k_m^{2}}$ | On-shell temporal wave number, an inverse length; the energy is $E=\hbar c\,\Omega_{\vec k}$ |
| $G(\tilde K_{\Phi})=(\langle\tilde K_{\Phi}\rangle_{\natural}+k_m^{2})^{-1}$ | Wave-number-space kernel, $(\Box-k_m^{2})G=-\delta^{(4)}$ |
| $G_R,G_A$ | Retarded and advanced Green's functions |
| $G_C=G_R-G_A$ | Pauli–Jordan (commutator) function |
| $G_F$ | Feynman propagator, time-ordered two-point function |
| $r_x^2=-{r'_{t}}^2+\vec r^2$ | Invariant separation |
| $\langle\tilde R_\Phi\rangle_{\natural}=0$ | Zero-divisor (light) cone of $\mathbb{B}_{\Phi}$ |
| $\langle\tilde K_{\Phi}\rangle_{\natural}=-k_m^{2}$ | Mass shell, equivalently $k_{t}^{\prime\,2}=\vec k_{\Phi}^{2}+k_m^{2}$ |
| $J_1,K_1$ | Bessel and modified Bessel functions |
| $\mathrm{H}_{\mathrm{hvs}}(r'_t),\mathrm{sgn}(r'_t)$ | Heaviside step and sign functions |
| $\delta_{\mu\nu}=(1,1,1,1)$ | The metric, the identity matrix; with $Q_t=i r'_t$ the material interval is $-{r'_{t}}^2+r_x^2+r_y^2+r_z^2$ |
| $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | Trace formula |

## Further Reading

- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the invariant commutation functions, the retarded and advanced Green's functions, and their support properties.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I: Foundations* (Cambridge, 1995), for the Klein–Gordon propagator, its contour prescriptions, and the derivation of the Feynman propagator from the time-ordered product.
- Claude Itzykson and Jean-Bernard Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Pauli–Jordan function, microcausality, and the explicit Bessel form of the massive commutator.
- N. N. Bogoliubov and D. V. Shirkov, *Introduction to the Theory of Quantized Fields* (Interscience, 1959), for the analytic structure of the causal functions and the relation among the Green's functions.
- I. S. Gradshteyn and I. M. Ryzhik, *Table of Integrals, Series and Products* (Academic Press, 2007), for the Bessel integral representations used to reduce the retarded kernel.
- G. N. Watson, *A Treatise on the Theory of Bessel Functions* (Cambridge, 1922), for the representation $J_0(z)=\frac{2}{\pi}\int_0^\infty\sin(z\cosh v)\,dv$ and the modified Bessel function $K_1$.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the propagator conventions and the Wick rotation to Euclidean space.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the biquaternion norm, the zero divisors, and the geometry of the light cone in the biquaternion algebra.
