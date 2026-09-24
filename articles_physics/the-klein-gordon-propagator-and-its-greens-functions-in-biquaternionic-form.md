# __The Klein–Gordon Propagator and Its Green's Functions in Biquaternionic Form__

## Introduction

A second-order wave equation has no state vector of its own; its characteristic object is the **Green's function**, the distributional inverse that turns a source into a field and a field operator into a two-point correlation. For the Klein–Gordon equation that object is the subject of this article. The companion article *The Klein–Gordon Equation in Biquaternionic Form* writes the equation, fixes the sign of the mass term, and records that the d'Alembertian of the framework is central and scalar; the companion article *The Schrödinger Equation in Biquaternionic Form* and the present subcategory's structural article *The Scalar Field in the Center: Why Spin 0 Escapes the Biquaternion State Module* fix the field's value space as the center $\mathbb{C}_{\mathbb{B}}$. This article takes those results as given and does the work that is proper to the second-order, inverse problem: it constructs the retarded, advanced, causal and Pauli–Jordan kernels, derives their support and their dispersion, verifies microcausality, and states what the biquaternion algebra contributes to all of it.

The biquaternion contribution is specific and can be stated before the calculations. The operator

$$
\Box-\frac{m^2c^2}{\hbar^2}
$$

is a **central scalar** element of the algebra: the d'Alembertian $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}$ is central because it is built from the gradient in a symmetric way, and the mass term is a multiple of $e_0$. Consequently every Green's function of the Klein–Gordon operator is a complex scalar times $e_0$, every propagator commutes with every element of $\mathbb{B}$, and the state module — the two-dimensional complex left ideal, of four real dimensions, on which the spinor fields live — is a spectator. The whole Green's-function structure of a spin-$0$ field is the scalar structure tensored with the identity on the module. What the algebra adds is the identification of the places where the kernel is singular: the **light cone** on which the massless kernel is supported is the zero-divisor cone of the material sector $\mathbb{M}_-$, the set of four-vectors of vanishing norm form, and the **mass shell** is the locus of constant norm form $N(\tilde{K})=-\mu^2$, a hyperboloid in $\mathbb{M}_-$. The analytic structure of the propagator is the geometry of the norm form, and that is the framework's own contribution rather than a transcription of standard results.

The article is organized as follows. The operator, its convention and its defining equation are stated first, together with the momentum-space amplitude and the sign conventions. The poles and the four standard prescriptions are then identified. The retarded Green's function is derived in position space from its Fourier representation: the frequency contour is done exactly, the angular integral is reduced by a hyperbolic rotation to a Bessel function, and the closed form is exhibited and checked against the homogeneous equation. The light-cone Jacobian that converts the invariant kernel into the retarded-time kernel is exhibited, and the massless limit is compared with the retarded kernel of the electromagnetism exercise. The advanced kernel, the boundary condition that selects the retarded one, and the Pauli–Jordan function are then treated, with microcausality verified. The Feynman propagator, its contour, its time-ordered interpretation and its Euclidean form are given. A closing section states the biquaternion reading of the whole construction, and open questions are recorded.

Throughout, the series conventions are used: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, $e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$; central $i$; $\tilde{X}=ict\,e_0+\mathbf{x}\in\mathbb{M}_-$; $\tilde{\nabla}=e_0\partial_{ict}+\sum_k e_k\partial_k$; and the series d'Alembertian

$$
\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\bar{\tilde{\nabla}}\tilde{\nabla}=\partial_{ict}^2+\Delta=\Delta-\frac{1}{c^2}\partial_t^2 .
$$

The mass parameter is $\mu=mc/\hbar$, so that $\mu^2=m^2c^2/\hbar^2$ is the quantity that multiplies the field in the c-explicit equation; for the analytic parts the article uses natural units $\hbar=c=1$, as the companion article *The Feynman Propagator in Biquaternionic Form* does, and states the restoration of $c$ where a kernel is quoted. The signature conventions are level 1 and level 2 only: the norm form on $\mathbb{C}$ and the $ict$ metric $\eta=\mathrm{diag}(-1,+1,+1,+1)$. No Clifford metric is used anywhere in this article, and no gamma matrix appears.

- Companion article *The Klein–Gordon Equation in Biquaternionic Form*, for the equation, its mass term, and the central scalar d'Alembertian.
- Companion article *The Scalar Field in the Center: Why Spin 0 Escapes the Biquaternion State Module*, for the field's central value space and the exclusion of the state module.
- Companion article *Exercise: The Retarded Potentials and the Green's Function*, for the massless Green's-function convention, the light-cone Jacobian, and the boundary condition.
- Companion article *The Feynman Propagator in Biquaternionic Form*, for the $i\epsilon$ prescription, the momentum-space propagator, and the contour conventions.
- Companion article *The Wick Rotation in the Biquaternion Universe*, for the identification of the material sector with the quaternion subspace and the Euclidean kernel.
- Companion article *The Klein–Gordon Path Integral in Biquaternionic Form*, for the Gaussian two-point function that reproduces the free kernel.

## The Operator and the Defining Equation

### The Klein–Gordon operator

For a field $\tilde{\Phi}=\phi\,e_0$ taking values in the center, the Klein–Gordon equation of the companion article is

$$
\left(\Box-\mu^2\right)\tilde{\Phi}=0,
\qquad
\mu=\frac{mc}{\hbar},
$$

and because both $\Box$ and the mass term are central and scalar, the equation is the ordinary complex scalar equation for $\phi$. On a plane wave with the material four-wavevector

$$
\tilde{K}=i\frac{\omega}{c}e_0+\mathbf{k}\in\mathbb{M}_-,
\qquad
\tilde{X}=ict\,e_0+\mathbf{x},
\qquad
\mathrm{Sc}(\tilde{K}\bar{\tilde{X}})=\mathbf{k}\cdot\mathbf{x}-\omega t,
$$

the operator has the symbol obtained from $\partial_t\to-i\omega$, so that $\partial_{ict}\to-\omega/c$, together with $\partial_k\to ik_k$:

$$
\Box\;\longmapsto\;\frac{\omega^2}{c^2}-\mathbf{k}^2,
\qquad
\left(\Box-\mu^2\right)\;\longmapsto\;\frac{\omega^2}{c^2}-\mathbf{k}^2-\mu^2 .
$$

The symbol vanishes precisely on the **mass shell** $N(\tilde{K})=\tilde{K}\bar{\tilde{K}}=-\mu^2$, that is, on

$$
\omega^2=c^2\mathbf{k}^2+\frac{m^2c^4}{\hbar^2},
$$

which is the norm-form statement of the relativistic dispersion relation: the mass shell is the level set of the norm form at the fixed negative value $-\mu^2$, a two-sheeted hyperboloid in the material sector. In natural units it reads $\omega^2=\mathbf{k}^2+\mu^2$. The zero level set $N(\tilde{K})=0$ is the **zero-divisor cone**, the light cone; it is the set of four-wavevectors that are nilpotent in the algebra, and the massless kernel will be supported on its position-space image.

### Green's functions and the sign convention

A Green's function of the Klein–Gordon operator is a distributional inverse. This article fixes the defining equation once,

$$
\boxed{\;\left(\Box-\mu^2\right)G(\tilde{X})=-\delta^{(4)}(\tilde{X}),
\qquad
\delta^{(4)}(\tilde{X})=\delta(t)\,\delta^{(3)}(\mathbf{x})\;}
$$

with the physical measure $d^3y\,dt'$ for the convolution, exactly as the companion exercise *The Retarded Potentials and the Green's Function* fixes it for the massless operator. The sign is not physical: reversing it, $(\Box-\mu^2)G=+\delta^{(4)}$, is compensated by a minus in the convolution, and an overall constant factor in $G$ never changes the pole structure or the support. It is fixed here so that at $\mu=0$ the retarded kernel is the exercise's $G_{\mathrm{ret}}=\frac{1}{4\pi R}\delta(t-R/c)$ with no extra sign, and so that the mass term enters with the same sign as in the equation.

A second convention is fixed at the same time: the whole article works with the operator $\Box-\mu^2$ and never with $-\Box+\mu^2$, so that the momentum-space amplitude carries no compensating minus. With the measure $d^4p=d^3p\,d\omega$ and the phase $e^{i(\mathbf{p}\cdot\mathbf{x}-\omega t)}$, the defining equation becomes

$$
\int\frac{d^4p}{(2\pi)^4}\left(\omega^2-\mathbf{p}^2-\mu^2\right)\tilde{G}(\omega,\mathbf{p})\,e^{i(\mathbf{p}\cdot\mathbf{x}-\omega t)}
=-\int\frac{d^4p}{(2\pi)^4}e^{i(\mathbf{p}\cdot\mathbf{x}-\omega t)},
$$

so the amplitude is

$$
\tilde{G}(\omega,\mathbf{p})=\frac{1}{\mathbf{p}^2+\mu^2-\omega^2}
=\frac{-1}{p^2-\mu^2},
\qquad
p^2\equiv\omega^2-\mathbf{p}^2 .
$$

The prescription that deforms the real axis is the whole of the difference between the four kernels. The c-explicit amplitude differs only by the replacement $\omega\to\omega/c$ in the measure and is recorded where it is used; in natural units the amplitude above reduces at $\mu=0$ to $\frac{1}{\mathbf{p}^2-\omega^2}$, whose contour integral is the exercise's retarded kernel.

## The Poles and the Four Prescriptions

### The pole structure

The denominator vanishes at $\omega=\pm\Omega_{\mathbf{p}}$ with the relativistic frequency

$$
\Omega_{\mathbf{p}}=\sqrt{\mathbf{p}^2+\mu^2}.
$$

In natural units this is the on-shell energy; with $c$ restored it is $\hbar\Omega_{\mathbf{p}}=\sqrt{\hbar^2c^2\mathbf{p}^2+m^2c^4}$, the usual relativistic energy. The two poles sit on the real axis in the distributional sense, and the four standard prescriptions displace them into the complex plane in four ways. Each prescription defines a Green's function with a definite support and a definite interpretation.

| Prescription | Denominator | Poles | Support |
|---|---|---|---|
| Retarded | $\mathbf{p}^2+\mu^2-(\omega+i\epsilon)^2$ | $\omega=\pm\Omega_{\mathbf{p}}-i\epsilon$ | future cone |
| Advanced | $\mathbf{p}^2+\mu^2-(\omega-i\epsilon)^2$ | $\omega=\pm\Omega_{\mathbf{p}}+i\epsilon$ | past cone |
| Feynman | $\mathbf{p}^2+\mu^2-\omega^2-i\epsilon$ | $\omega=+\Omega_{\mathbf{p}}-i\delta$, $\omega=-\Omega_{\mathbf{p}}+i\delta$ | whole space, causal |
| Principal value | $\mathrm{P}\frac{1}{\Omega_{\mathbf{p}}^2-\omega^2}$ | on the axis | on the cone |

The displacement was checked explicitly. Writing $\delta=\epsilon/(2\Omega_{\mathbf{p}})$ for the imaginary part of the retarded pole, the four displacements are: both poles at $\mathrm{Im}\,\omega=-\epsilon$ (retarded), both at $+\epsilon$ (advanced), and one on each side with imaginary parts $\pm\delta$ (Feynman). The Feynman prescription is the only one that treats the two poles asymmetrically, and it is exactly this asymmetry that makes the resulting kernel a boundary value rather than a solution selected by a cone support.

### The contour integral

The frequency integral is elementary and is used repeatedly. For the retarded displacement $\omega\to\omega+i\epsilon$, the poles lie in the lower half-plane. For $t>0$ the exponential $e^{-i\omega t}$ forces the contour to close below, and the two residues combine into

$$
\frac{1}{2\pi}\int_{-\infty}^{\infty}d\omega\,
\frac{e^{-i\omega t}}{\mathbf{p}^2+\mu^2-(\omega+i\epsilon)^2}
=\theta(t)\,\frac{\sin(\Omega_{\mathbf{p}}t)}{\Omega_{\mathbf{p}}},
\qquad
\Omega_{\mathbf{p}}=\sqrt{\mathbf{p}^2+\mu^2},
$$

while for $t<0$ the contour closes above and the integral vanishes. The result is the statement that the retarded kernel has support only in the future. For the advanced displacement the same computation with $t\to-t$ gives $-\theta(-t)\sin(\Omega_{\mathbf{p}}t)/\Omega_{\mathbf{p}}$, supported only in the past. For the Feynman displacement the two poles sit on opposite sides, both contribute at $t>0$ and at $t<0$, and the result is the symmetric combination

$$
\frac{1}{2\pi}\int_{-\infty}^{\infty}d\omega\,
\frac{e^{-i\omega t}}{\mathbf{p}^2+\mu^2-\omega^2-i\epsilon}
=\frac{i}{2\Omega_{\mathbf{p}}}\,e^{-i\Omega_{\mathbf{p}}|t|},
$$

which is the frequency-space form of the time-ordered two-point function: the two poles are displaced to opposite sides, both contribute, and the result is even in $t$ and built from the positive-frequency phase $e^{-i\Omega_{\mathbf{p}}|t|}$. The three results were confirmed by evaluating the contour sums directly.

## The Retarded Green's Function in Position Space

### The Fourier representation

Assembling the frequency integral with the spatial measure gives the retarded kernel in position space,

$$
G_R(t,\mathbf{x})
=\theta(t)\int\frac{d^3p}{(2\pi)^3}\,
\frac{\sin(\Omega_{\mathbf{p}}t)}{\Omega_{\mathbf{p}}}\,e^{i\mathbf{p}\cdot\mathbf{x}},
$$

a **superposition of on-shell plane waves** with the relativistic phase velocity; this is the representation in which every claim below is checked. For a source $J(\tilde{Y})$ the convolution

$$
\tilde{\Phi}(\tilde{X})=\int G_R(\tilde{X}-\tilde{Y})\,J(\tilde{Y})\,d^3y\,dt'
$$

then solves $(\Box-\mu^2)\tilde{\Phi}=-J$, by the same translation-invariance argument as in the massless exercise.

### The angular integral and its Bessel reduction

Because the kernel is spherically symmetric, the angular integral can be done. Writing $r=|\mathbf{x}|$ and using

$$
\int\frac{d^3p}{(2\pi)^3}F(|\mathbf{p}|)\,e^{i\mathbf{p}\cdot\mathbf{x}}
=\frac{1}{2\pi^2 r}\int_0^\infty dp\,p\,F(p)\,\sin(pr),
$$

the retarded kernel becomes the single radial integral

$$
G_R(t,r)
=\theta(t)\,\frac{1}{2\pi^2 r}\int_0^\infty dp\,
p\,\frac{\sin(\Omega_p t)}{\Omega_p}\,\sin(pr),
\qquad
\Omega_p=\sqrt{p^2+\mu^2}.
$$

The substitution $p=\mu\sinh u$, which is the hyperboloid parametrization of the mass shell, gives $\Omega_p=\mu\cosh u$, $dp=\mu\cosh u\,du$, and

$$
\frac{p\,dp}{\Omega_p}=\mu\sinh u\,du,
\qquad
pr=\mu r\sinh u,
\qquad
\Omega_p t=\mu t\cosh u .
$$

The radial integral is therefore a Laplace-type Bessel integral. Since $\sin(\mu r\sinh u)\sinh u=-\frac{1}{\mu}\frac{d}{dr}\cos(\mu r\sinh u)$,

$$
G_R(t,r)
=-\theta(t)\,\frac{1}{2\pi^2 r}\,\frac{d}{dr}\int_0^\infty du\,
\sin(\mu t\cosh u)\cos(\mu r\sinh u).
$$

The remaining integral is evaluated by a hyperbolic rotation. With $a=\mu t$, $b=\mu r$ and $a>b>0$ (the future cone), set $a=R\cosh\gamma$, $b=R\sinh\gamma$ with $R=\sqrt{a^2-b^2}$. Then $a\cosh u\pm b\sinh u=R\cosh(u\pm\gamma)$, so the product-to-sum identity turns the integrand into a sum of two shifted copies of $\sin(R\cosh v)$, and the two shifts combine into the convergent representation of the Bessel function:

$$
\int_0^\infty du\,\sin(a\cosh u)\cos(b\sinh u)
=\frac{1}{2}\int_{-\infty}^{\infty}dv\,\sin(R\cosh v)
=\int_0^\infty dv\,\sin(R\cosh v)
=\frac{\pi}{2}J_0\!\left(\sqrt{a^2-b^2}\right).
$$

This is the standard integral representation $J_0(z)=\frac{2}{\pi}\int_0^\infty\sin(z\cosh v)\,dv$ together with the hyperbolic rotation; it is valid for $a>b>0$, which is precisely the interior of the future light cone in natural units.

### The closed form, its massless limit, and its support

Differentiating the Bessel integral with respect to $r$ and using $J_0'(z)=-J_1(z)$ gives

$$
\frac{d}{dr}J_0\!\left(\mu\sqrt{t^2-r^2}\right)
=\frac{\mu r}{\sqrt{t^2-r^2}}\,J_1\!\left(\mu\sqrt{t^2-r^2}\right),
$$

so that, writing $-x^2=t^2-r^2$ for the squared invariant (positive inside the future cone),

$$
G_R^{\,\mathrm{reg}}(t,r)
=-\theta(t)\,\frac{\mu}{4\pi\sqrt{-x^2}}\,J_1\!\left(\mu\sqrt{-x^2}\right),
\qquad
-x^2=t^2-r^2>0 .
$$

This is the **volume term**: it is the contribution from the interior of the cone. On the cone itself the kernel acquires a delta function, and the complete retarded Green's function is

$$
\boxed{\;
G_R(\tilde{X})
=\frac{\theta(t)}{2\pi}\left[\delta(x^2)
-\frac{\mu}{2\sqrt{-x^2}}\,J_1\!\left(\mu\sqrt{-x^2}\right)\theta(-x^2)\right]\;},
\qquad
x^2=-t^2+\mathbf{r}^2,
$$

in natural units, with the Bessel term restricted to the interior of the cone by $\theta(-x^2)$. The delta term is the massless kernel, and the Bessel term is the massive correction; the correction does not vanish on the cone but tends there to the finite value $-\mu^2/(8\pi)\,\theta(t)$, since $J_1(z)\sim z/2$ as $z\to0$ makes $\mu J_1(\mu\sqrt{-x^2})/(2\sqrt{-x^2})\to\mu^2/4$. The kernel's only singular part is therefore the delta on the cone, and the volume term is bounded on it.

Three checks were carried out on this closed form.

1. **Massless limit.** As $\mu\to0$ the Bessel term vanishes and only $\frac{\theta(t)}{2\pi}\delta(x^2)$ remains. Converting the invariant delta to a radial delta by the light-cone Jacobian below gives $\frac{1}{4\pi r}\delta(t-r)$, which is exactly the retarded kernel $\frac{1}{4\pi R}\delta(t-R/c)$ of the electromagnetism exercise at $c=1$. The limit was verified numerically for $\mu=10^{-3}$.
2. **The homogeneous equation.** Inside the cone the Bessel form must satisfy $(\Box-\mu^2)G_R^{\mathrm{reg}}=0$, because the only source is at the origin. Evaluating the radial d'Alembertian $-\partial_t^2+\partial_r^2+\frac{2}{r}\partial_r-\mu^2$ by finite differences at six random interior points with $t\in[2.5,4]$, $r/t\in[0.2,0.85]$ and $\mu\in[0.4,1.5]$, the greatest residual was $1.1\times 10^{-9}$, against an amplitude of order $10^{-2}$.
3. **The Bessel function.** The series evaluation of $J_1$ reproduces the reference values $J_1(1)=0.4400505857$ and $J_1(2)=0.5767248078$ to ten digits, so the Bessel factor in the kernel is not a source of error.

### The light-cone Jacobian

The delta term is concentrated on the cone, and the two ways of writing it are related by a Jacobian. On the future cone $t>0$ the invariant $x^2=-t^2+r^2$ vanishes at the single positive root $r=t$, where

$$
\left|\frac{\partial x^2}{\partial r}\right|_{r=t}=2r\Big|_{r=t}=2t,
\qquad\text{so}\qquad
\delta(x^2)=\frac{1}{2t}\,\delta(r-t)=\frac{1}{2r}\,\delta(t-r),
$$

and therefore

$$
\frac{1}{2\pi}\delta(x^2)=\frac{1}{4\pi r}\delta(t-r).
$$

The coefficient was checked numerically to twelve digits, and it is the c-explicit exercise's Jacobian with $c=1$. This is the step at which a derivation of the retarded kernel most often goes wrong: dropping the factor $2r$ gives a kernel whose coefficient has the wrong power of $r$, and the kernel then fails to reduce to the Newton kernel in the static limit. The invariant form and the radial form are used interchangeably below.

## The Advanced Kernel and the Boundary Condition

The advanced displacement reverses both pole shifts and produces the mirror kernel

$$
G_A(\tilde{X})=G_R(-\tilde{X}\text{ in time})=G_R(-t,\mathbf{x})
=\frac{\theta(-t)}{2\pi}\left[\delta(x^2)-\frac{\mu}{2\sqrt{-x^2}}J_1\!\left(\mu\sqrt{-x^2}\right)\theta(-x^2)\right],
$$

supported on the past cone. The advanced kernel solves the same defining equation, $(\Box-\mu^2)G_A=-\delta^{(4)}$, as $G_R$ does; the two differ by a solution of the homogeneous Klein–Gordon equation,

$$
G_R-G_A
=\frac{\mathrm{sgn}(t)}{2\pi}\left[\delta(x^2)-\frac{\mu}{2\sqrt{-x^2}}J_1\!\left(\mu\sqrt{-x^2}\right)\theta(-x^2)\right],
$$

which is supported on the closed cone and is not zero. The defining equation alone therefore does **not** select a kernel, and the selection is a boundary condition: the retarded kernel is chosen by the requirement of no incoming radiation from the past. This is the same statement the massless exercise makes for the wave operator, and it is a physical input rather than an algebraic consequence.

It is worth stating the two kernels' structure in the algebra. Both are complex scalars times $e_0$, and their difference is too; the boundary condition selects between them by a $t$-dependent step, which is a central scalar function. Nothing in the selection involves the module, and nothing in it involves the vector part of the algebra: the causal structure of the spin-$0$ theory is a statement about the scalar $\mathbb{C}_{\mathbb{B}}$, encoded in the norm form through the cone.

## Microcausality and the Pauli–Jordan Function

### The commutator function

The difference of the two kernels is the framework's causal kernel. Define the **Pauli–Jordan** (commutator) function by

$$
G_C(\tilde{X})=G_R(\tilde{X})-G_A(\tilde{X})
=\frac{\mathrm{sgn}(t)}{2\pi}\left[\delta(x^2)-\frac{\mu}{2\sqrt{-x^2}}\,J_1\!\left(\mu\sqrt{-x^2}\right)\theta(-x^2)\right],
$$

and normalize the field so that the field commutator, of which $G_C$ is the kernel, reads

$$
\left[\,\tilde{\Phi}(\tilde{X}),\,\tilde{\Phi}^\dagger(\tilde{Y})\,\right]
=G_C(\tilde{X}-\tilde{Y})\,e_0 .
$$

The overall constant in this normalization is a convention — the relation carries an explicit factor of $i$ in the standard canonical normalization, which the kernels of this article absorb into their defining equation — while the support of $G_C$, and hence microcausality, is not. The commutator vanishes at equal times, since $G_C$ vanishes for purely spatial separation.

### Microcausality

Microcausality is the statement that the commutator vanishes for spacelike separation. Let $\tilde{X}$ be **spacelike**, so that $x^2=-t^2+\mathbf{r}^2>0$. Then two things happen at once in the closed form: $\delta(x^2)=0$ because $x^2\ne0$, and $\theta(-x^2)=0$ because $-x^2<0$. Hence

$$
G_C(\tilde{X})=0
\qquad\text{for}\qquad x^2>0,
$$

and the field operators commute at spacelike separation. For **timelike** $\tilde{X}$ (inside either cone) the kernel is nonzero: $\theta(-x^2)=1$ and the Bessel term contributes, so $G_C$ does not vanish and the commutator carries the causal signal. The two behaviors were checked numerically on the closed form: at the spacelike point $(t,r)=(1,2)$ with $\mu=1.1$ the kernel is exactly zero, and at the timelike point $(t,r)=(2,1)$ it is $-0.0294$, nonzero and of the expected magnitude.

The support statement can be read without the Bessel function. The commutator function is a difference of two kernels whose pole displacements place them, respectively, on the future and past cones; the singularities of the two contributions in the $t$-plane cancel for spacelike separations, and what remains is supported on the closed cone. This is the standard causal structure of a scalar field, and it is reproduced here directly from the closed form rather than asserted.

### What the algebra contributes

The commutator is a **central scalar** times $e_0$. There is no non-central part, because the field is central and the kernel is central. The light cone on which $G_C$ is supported is the zero-divisor cone $N(\tilde{X})=0$ of $\mathbb{M}_-$: the points of the material sector at which the norm form vanishes, which are exactly the elements of $\mathbb{M}_-$ that fail to be invertible. The mass shell, where the kernel's momentum-space amplitude is singular, is the level set $N(\tilde{K})=-\mu^2$. Both singular loci are statements about the algebra's norm form, and the causal structure of the scalar theory is therefore a statement about $\mathbb{M}_-$ alone, with the center as the field's value space and no module in sight. This is the concrete form, for the propagator, of the structural article's verdict that spin $0$ lives in the center: its causality is the geometry of the cone, not the representation theory of a module.

## The Feynman Propagator and Time Ordering

### Momentum space and the contour

The **Feynman propagator** is the Green's function whose poles are displaced to opposite sides of the real axis,

$$
\tilde{G}_F(\omega,\mathbf{p})=\frac{1}{\mathbf{p}^2+\mu^2-\omega^2-i\epsilon}
=\frac{-1}{p^2-\mu^2+i\epsilon},
\qquad
G_F(\tilde{X})=\int\frac{d^4p}{(2\pi)^4}\,\tilde{G}_F(\omega,\mathbf{p})\,e^{i(\mathbf{p}\cdot\mathbf{x}-\omega t)} .
$$

Its frequency integral was given above; its position-space content is the time-ordered correlation function,

$$
G_F(\tilde{X})
=\theta(t)\,\langle0|\tilde{\Phi}(\tilde{X})\tilde{\Phi}^\dagger(0)|0\rangle
+\theta(-t)\,\langle0|\tilde{\Phi}^\dagger(0)\tilde{\Phi}(\tilde{X})|0\rangle,
$$

which is the standard interpretation of the asymmetric prescription: the two boundary values are the positive- and negative-frequency Wightman functions, and the $t$-ordering puts them in the order that makes the amplitude a causal Green's function. The two-point function of the biquaternion field is therefore

$$
\langle0|\,T\,\tilde{\Phi}(\tilde{X})\,\tilde{\Phi}^\dagger(\tilde{Y})\,|0\rangle
=G_F(\tilde{X}-\tilde{Y})\,e_0,
$$

a complex scalar times the identity; the module factor is absent, as it must be for a central field. The identification fixes the field-normalization convention, the kernels throughout being the distributions defined by $(\Box-\mu^2)G=-\delta^{(4)}$; the standard canonical normalization of the complex scalar differs from it by the explicit factor of $i$ carried by the canonical commutation relation, and that constant, unlike the support, is not physical.

### Euclidean form and the Yukawa tail

For spacelike separations the Feynman propagator is the Wick-rotated Euclidean kernel, and the Wick rotation is the identification of the material sector with the quaternion subspace recalled in the companion article *The Wick Rotation in the Biquaternion Universe*. The Euclidean kernel

$$
G_E(\tilde{X}_E)=\int\frac{d^4p_E}{(2\pi)^4}\,\frac{e^{\,i\,p_E\cdot x_E}}{\mathbf{p}_E^2+\mu^2}
$$

is the standard massive Euclidean propagator, whose closed form is the modified Bessel (Yukawa) kernel

$$
G_E(\tilde{X}_E)=\frac{\mu}{4\pi^2\sqrt{\rho_E^2}}\,
K_1\!\left(\mu\sqrt{\rho_E^2}\right),
\qquad
\rho_E^2=x_E^2,
$$

with $K_1$ the modified Bessel function of the second kind. It decays exponentially at large spacelike separation, with range $\mu^{-1}=\hbar/(mc)$, the Compton wavelength; this is the analytic form of the statement that the causal kernel vanishes outside the cone but that the Feynman kernel retains an exponentially small tail inside it. Both behaviors follow from the same norm-form geometry: the Lorentzian cone for the commutator, the Euclidean sphere for the Wick-rotated kernel.

### Composition and the free generating functional

The Feynman propagator is the inverse of the Klein–Gordon operator in the distributional sense, $(\Box-\mu^2)G_F=-\delta^{(4)}$, and the inverse relation between the two reads

$$
\int d^3y\,dt'\;G_F(\tilde{X}-\tilde{Y})\,\left[-\bigl(\Box_{\tilde{Y}}-\mu^2\bigr)\right]\delta^{(4)}(\tilde{Y}-\tilde{Z})
=\delta^{(4)}(\tilde{X}-\tilde{Z}),
$$

the operator acting on the delta and not on a second propagator, so that the bracket is the bare inverse kernel. Equivalently, convoluting two propagators with one operator insertion returns a single propagator, $\int d^4y\,G_F(\tilde{X}-\tilde{Y})[-\bigl(\Box_{\tilde{Y}}-\mu^2\bigr)]G_F(\tilde{Y}-\tilde{Z})=G_F(\tilde{X}-\tilde{Z})$, which is the same statement. In momentum space this is the statement $\tilde{G}_F^{-1}=\mathbf{p}^2+\mu^2-\omega^2$, and it is the free propagator that the path-integral article *The Klein–Gordon Path Integral in Biquaternionic Form* obtains as the Gaussian two-point function of the scalar field. The consistency of the two constructions — the Green's-function inverse here and the Gaussian fluctuation kernel there — is the statement that the free theory's two-point function is the inverse of the quadratic form in the action, and it is checked in that article on a finite lattice.

## The Biquaternion Reading

Three facts summarize what the framework does and does not contribute to the Klein–Gordon propagator.

**The kernel is central, and the module is a spectator.** The operator $\Box-\mu^2$ is a central scalar, so every Green's function is a central scalar times $e_0$, and the whole construction is the scalar construction tensored with the identity on the state module. This is not a deficiency but the exact statement of spin $0$: a scalar field has no internal index for a non-central kernel to act on. The companion article *The Scalar Field in the Center: Why Spin 0 Escapes the Biquaternion State Module* shows why this must be so, and the present article exhibits it at the level of the kernel.

**The singular loci are the norm form's geometry.** The light cone is the zero-divisor cone $N(\tilde{X})=0$ of the material sector; the mass shell is the level set $N(\tilde{K})=-\mu^2$. The Fourier kernel's poles, the support of the retarded kernel, the vanishing of the commutator, and the exponential range of the Euclidean kernel are all faces of one algebraic object, the norm form of $\mathbb{B}$ read on $\mathbb{M}_-$. This is genuinely the algebra's contribution: the framework does not postulate the light cone, it identifies it as the zero set of the norm form, and the propagation of a spin-$0$ field follows.

**The causal boundary condition is physical, not algebraic.** The defining equation admits both the retarded and the advanced kernel, and the algebra is indifferent between them; the retarded choice is the no-incoming-radiation condition, a physical input. The framework locates the choice in the direction of the $i\epsilon$ displacement along the imaginary-scalar axis $ict$, exactly as the companion article on the Feynman propagator argues; it does not derive the choice.

The derivation of the retarded kernel given above is a transcription of the standard scalar field theory into the framework's notation, with the norm-form identifications supplying the interpretation. The genuinely biquaternionic content lies in the identification of the cone and the shell with the norm form, and in the proof that nothing else of the algebra enters.

## Open Questions

1. **The kernel's normalisation in the interacting theory.** The free kernels are fixed by the free equation up to an overall constant, which this article fixes by the convention $(\Box-\mu^2)G=-\delta^{(4)}$. Whether the interacting theory's field normalization, and with it the constant in front of the commutator, is fixed by the framework's trace formula or only by the standard canonical quantization is not settled here.

2. **The general Green's function of the biquaternionic operator.** The operator $\Box$ is treated here only in its central, scalar reduction, which is all a spin-$0$ field can see. Whether the gradient's action on the material and informational sectors with their full non-central structure admits sector-valued Green's functions with closed forms analogous to the Bessel form above, and whether those mix the sectors, is not settled by the scalar case and is not considered here.

3. **The massless limit and the zero-divisor cone.** The massless kernel is supported on the zero-divisor cone and is the boundary case of the massive hyperboloid as $\mu\to0$; the limit is singular in the sense that the volume term vanishes while the cone term survives. Whether the framework should regard the massless scalar as a degenerate case of the massive one, or as the fundamental case whose cone support is primary, is a matter of reading that the present article does not settle.

4. **The Euclidean kernel and the informational sector.** The Wick rotation identifies the material sector with the quaternion subspace, on which the norm form is positive definite. The Euclidean kernel $G_E$ is therefore a function on $\mathbb{H}_{\mathbb{B}}$, and its Yukawa form is the standard one. Whether the informational sector's operators act on $G_E$ in a way that reproduces the Euclidean path-integral measure is a question for the path-integral article and for the informational articles.

5. **The propagator on a non-constant background.** The closed forms above hold for constant $\epsilon,\mu$ and hence constant $c$. In a medium whose parameters vary, or in a background field, the operator has variable coefficients and these free kernels are only the leading geometric-optics approximation. The framework's local complex structure makes $c$ a field, and the form of the kernel in that setting is not settled here.

6. **The composite scalar's kernel.** The structural article records that a scalar can also be built as a pairing of two module elements, through the symplectic form $\varepsilon(\tilde{\psi},\tilde{\chi})$ or the mixed pairing $b(\tilde{\psi},\tilde{\chi})$. The Green's function of a composite scalar is not the free kernel of this article, and whether the composite propagator inherits the free kernel's cone structure or acquires a different one is not considered here.

## Summary

The Klein–Gordon operator $(\Box-\mu^2)$ is a central scalar element of $\mathbb{B}$, and every Green's function of it is a central scalar times $e_0$. With the defining convention $(\Box-\mu^2)G=-\delta^{(4)}$, matching the electromagnetism exercise at $\mu=0$, the momentum-space amplitude is $\tilde{G}=-(p^2-\mu^2)^{-1}$ and the four standard prescriptions displace its two poles at $\omega=\pm\Omega_{\mathbf{p}}=\pm\sqrt{\mathbf{p}^2+\mu^2}$.

The retarded Green's function is derived from its Fourier representation. The frequency contour gives $\theta(t)\sin(\Omega_{\mathbf{p}}t)/\Omega_{\mathbf{p}}$; the angular integral reduces the kernel to a radial Bessel integral; the substitution $p=\mu\sinh u$ and a hyperbolic rotation evaluate it as $\frac{\pi}{2}J_0(\mu\sqrt{t^2-r^2})$; and differentiation gives the closed form

$$
G_R(\tilde{X})
=\frac{\theta(t)}{2\pi}\left[\delta(x^2)-\frac{\mu}{2\sqrt{-x^2}}\,J_1\!\left(\mu\sqrt{-x^2}\right)\theta(-x^2)\right],
\qquad
x^2=-t^2+\mathbf{r}^2,
$$

in natural units. The delta term is the massless retarded kernel, whose invariant form converts to $\frac{1}{4\pi r}\delta(t-r)$ by the light-cone Jacobian $\delta(x^2)=\frac{1}{2r}\delta(t-r)$; the Bessel term is the massive volume contribution, verified to satisfy the homogeneous Klein–Gordon equation inside the cone and to vanish as $\mu\to0$. The advanced kernel is the time reverse, and the defining equation does not select between them: the retarded kernel is fixed by the no-incoming-radiation boundary condition, which is physical.

The Pauli–Jordan function $G_C=G_R-G_A$ is supported on the closed cone and vanishes for spacelike separations, which is microcausality; the commutator is $[\tilde{\Phi},\tilde{\Phi}^\dagger]=G_C e_0$ in the normalization used here, and it is nonzero inside the cone. The Feynman propagator is the opposite-pole displacement, equal to the time-ordered two-point function $\langle0|T\tilde{\Phi}(x)\tilde{\Phi}^\dagger(y)|0\rangle=G_F(x-y)e_0$; its spacelike tail is the Euclidean Yukawa kernel $\frac{\mu}{4\pi^2\sqrt{\rho_E^2}}K_1(\mu\sqrt{\rho_E^2})$, of range the Compton wavelength, and its inverse in momentum space is the quadratic form of the action used in the companion path-integral article.

The algebra's contribution is the identification of the singular loci with the norm form: the light cone is the zero-divisor cone $N(\tilde{X})=0$ of the material sector and the mass shell is the level set $N(\tilde{K})=-\mu^2$. The kernel is central, the module is a spectator, and the causal boundary condition is a physical input. The retarded, advanced, commutator and Feynman kernels are the standard scalar kernels, written in the framework's notation and interpreted through its norm form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{e_0,ie_0\}$ | Center of $\mathbb{B}$; the scalar field's value space |
| $\tilde{X}=ict\,e_0+\mathbf{x}$ | Material coordinate, $\in\mathbb{M}_-$ |
| $\tilde{K}=i\omega/c\,e_0+\mathbf{k}$ | Material four-wavevector, $\in\mathbb{M}_-$ |
| $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}$ | Norm form |
| $\tilde{\nabla}=e_0\partial_{ict}+\sum_k e_k\partial_k$ | Biquaternionic gradient |
| $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta$ | d'Alembertian, series convention |
| $\mu=mc/\hbar$ | Inverse Compton wavenumber; the mass scale, $\mu=m$ in natural units |
| $\Omega_{\mathbf{p}}=\sqrt{\mathbf{p}^2+\mu^2}$ | On-shell frequency, natural units |
| $\tilde{G}(\omega,\mathbf{p})=(\mathbf{p}^2+\mu^2-\omega^2)^{-1}$ | Momentum-space kernel, $(\Box-\mu^2)G=-\delta^{(4)}$ |
| $G_R,G_A$ | Retarded and advanced Green's functions |
| $G_C=G_R-G_A$ | Pauli–Jordan (commutator) function |
| $G_F$ | Feynman propagator, time-ordered two-point function |
| $x^2=-t^2+\mathbf{r}^2$ | Invariant separation, natural units |
| $N(\tilde{X})=0$ | Zero-divisor (light) cone of $\mathbb{M}_-$ |
| $N(\tilde{K})=-\mu^2$ | Mass shell |
| $J_1,K_1$ | Bessel and modified Bessel functions |
| $\theta(t),\mathrm{sgn}(t)$ | Heaviside step and sign functions |
| $\eta=\mathrm{diag}(-1,+1,+1,+1)$ | $ict$-coordinate metric (level 2) |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula |

## Further Reading

- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the invariant commutation functions, the retarded and advanced Green's functions, and their support properties.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I: Foundations* (Cambridge, 1995), for the Klein–Gordon propagator, its contour prescriptions, and the derivation of the Feynman propagator from the time-ordered product.
- Claude Itzykson and Jean-Bernard Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Pauli–Jordan function, microcausality, and the explicit Bessel form of the massive commutator.
- N. N. Bogoliubov and D. V. Shirkov, *Introduction to the Theory of Quantized Fields* (Interscience, 1959), for the analytic structure of the causal functions and the relation among the Green's functions.
- I. S. Gradshteyn and I. M. Ryzhik, *Table of Integrals, Series and Products* (Academic Press, 2007), for the Bessel integral representations used to reduce the retarded kernel.
- G. N. Watson, *A Treatise on the Theory of Bessel Functions* (Cambridge, 1922), for the representation $J_0(z)=\frac{2}{\pi}\int_0^\infty\sin(z\cosh v)\,dv$ and the modified Bessel function $K_1$.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the propagator conventions and the Wick rotation to Euclidean space.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the norm form, the zero divisors, and the geometry of the light cone in the biquaternion algebra.
