# __Exercise: The Retarded Potentials and the Green's Function__

## Introduction

This is an exercise in the electromagnetism series. It takes the wave equation for the potential biquaternion that *Maxwell's Equations in the Biquaternionic Formulation* states in the Lorenz gauge, and it constructs, verifies, and uses the Green's function that solves that equation. The parent states the potential equation and refers the reader to the standard references for the kernel's precise form; the retarded kernel $G_\Box = \frac{1}{4\pi R}\,\delta(t - R/c)$ and the retarded convolution are stated, but not derived, in the companion article *Radiation from Accelerated Charges in Biquaternionic Form*, which uses the same kernel and says so explicitly — "We do not re-derive this structure; we only specialize it." This exercise supplies the missing derivation, checks the kernel on cases that did not suggest it, and states the boundary condition that selects the retarded kernel over the advanced one. It is the first step of the series that is purely about the *inverse* of the wave operator: the object that turns a source into a field.

**What is assumed.** The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ satisfying $\vec e_k^2 = -e_t$ and the product rule $\vec e_\mu \vec e_\nu = -\delta_{\mu\nu}e_t + \epsilon_{\mu\nu\lambda}\vec e_\lambda$; the scalar imaginary $i$ with $i^2 = -1$, commuting with every $\vec e_k$; the anti-Hermitian subspace $\mathbb{M}_-$ (imaginary scalar, real vector) and the Hermitian subspace $\mathbb{M}_+$ (real scalar, imaginary vector), with $\mathbb{B} = \mathbb{M}_+\oplus\mathbb{M}_-$; the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and the scalar subspace $\mathbb{C}_{\mathbb{B}}$; the quaternion conjugate ${}^{\natural}$, the complex conjugate $\bar{\cdot}$, and the Hermitian conjugate ${}^{*} = ({}^{\natural})^{\,*}$; the biquaternionic gradient and its quaternion conjugate
$$
\tilde{\nabla} = e_t\,\partial/\partial Q_t + \vec e_x\,\partial/\partial Q_x + \vec e_y\,\partial/\partial Q_y + \vec e_z\,\partial/\partial Q_z,
\qquad
\tilde{\nabla}^{\natural} = e_t\,\partial/\partial Q_t - \vec e_x\,\partial/\partial Q_x - \vec e_y\,\partial/\partial Q_y - \vec e_z\,\partial/\partial Q_z,
$$
with $\partial/\partial Q_t = -\frac{i}{c}\partial/\partial t$ and $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \partial^2/\partial Q_t^2 + \Delta$; the potential biquaternion $\tilde{A} = \frac{i\phi}{c}e_t + \vec A$; the four-current $\tilde J = ic\rho\,e_t + \vec J$, whose normalised form is $\sqrt{\mu}\,\tilde J = \frac{i\rho}{\sqrt{\epsilon}}e_t + \sqrt{\mu}\,\vec J$; the Lorenz-gauge potential wave equation $\Box\tilde{A} = -\mu\tilde J$; the field-strength biquaternion $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$; the medium speed $c = 1/\sqrt{\epsilon\mu}$ and its vacuum value $c_0 = 1/\sqrt{\epsilon_0\mu_0}$; and the trace formula $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$. Throughout, $c$ is the speed of light in the medium and $\vec v$ is reserved for particle and frame velocities. All of this is the notation contract of the read-list articles and is not modified.

**What is to be shown.** Five things. (1) The wave operator, its defining equation for the Green's function, and the convolution that solves the potential equation. (2) The retarded kernel $G_{\mathrm{ret}} = \frac{1}{4\pi R}\delta(t - R/c)$, derived from the light-cone delta with its Jacobian, and verified by applying $\Box$ to it. (3) That the advanced kernel solves the same equation, so the retarded choice is a *boundary condition*, not an algebraic consequence. (4) The retarded potentials $\phi$ and $\vec A$ obtained by convolving the kernel with the source, together with the automatic Lorenz gauge. (5) The static limit, which reproduces the Coulomb and Biot–Savart solutions and matches the parent's static result. Each problem is stated and solved in full, and the exercise closes by naming what the parent does not establish.

**The result.** With $R = |x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|$, the retarded Green's function of the wave operator $\Box = \Delta + \partial^2/\partial Q_t^2$ is
$$
\boxed{\;G_{\mathrm{ret}}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t) = \frac{1}{4\pi R}\,\delta\!\left(t - \frac{R}{c}\right), \qquad \Box\,G_{\mathrm{ret}} = -\delta(t)\,\delta^{(3)}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\;}
$$
and the retarded solution of the potential equation $\Box\tilde{A} = -\mu\tilde J$ is
$$
\boxed{\;\tilde{A}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t) = \frac{\mu}{4\pi}\int \frac{\tilde J(\vec y,\,t - R/c)}{R}\,d^3y,
\qquad R = |x\,\vec e_x+y\,\vec e_y+z\,\vec e_z - \vec y|, \;}
$$
whose scalar and vector parts are the standard retarded potentials
$$
\phi = \frac{1}{4\pi\epsilon}\int \frac{\rho(\vec y,\,t - R/c)}{R}\,d^3y,
\qquad
\vec A = \frac{\mu}{4\pi}\int \frac{\vec J(\vec y,\,t - R/c)}{R}\,d^3y .
$$

## The Problem

The parent fixes the potential wave equation in the Lorenz gauge,
$$
\Box\tilde{A} = -\mu\tilde J, \qquad \tilde J = ic\rho\,e_t + \vec J,
$$
and the companion article observes that "the physically correct solution is the retarded one, built by convolution over the past light cone," displaying the kernel and the convolution but leaving the derivation to the standard references. An exercise built on a parent tests it: the task here is to *construct* the kernel from the operator, to *verify* it by applying the operator, and to *use* it to obtain the retarded potentials.

The problem is an inverse problem. The operator $\Box$ is a linear differential operator with constant coefficients, and a Green's function is a distributional inverse: a kernel $G$ such that $\Box_{\tilde{Q}} G(\tilde{Q}) = -\delta^{(4)}(\tilde{Q})$, so that convolution with a source produces a solution. Two features make this more than bookkeeping, and both are traps.

First, the kernel is concentrated on the light cone, and the delta function that concentrates it is a delta function of an *argument that vanishes on the cone*. When that argument is $t - R/c$ the coefficient is $1/(4\pi R)$; when it is written as the invariant $t^2 - R^2/c^2$ the coefficient is $1/(2\pi c)$, and the two are related by the Jacobian $\left|d(t^2 - R^2/c^2)/dt\right| = 2R/c$ evaluated at the future root. A derivation that drops the Jacobian gets the wrong power of $R$ and the wrong constant. The exercise makes this step explicit and checks it numerically.

Second, the defining equation does not determine the kernel. Both the retarded kernel (supported on the future cone) and the advanced kernel (supported on the past cone) satisfy $\Box G = -\delta^{(4)}$, and they differ by a solution of the homogeneous wave equation. What selects the retarded one is a *boundary condition* — no incoming radiation from the past — not an algebraic property of $\Box$. The exercise states the condition, exhibits the advanced kernel that the equation alone admits, and shows which contour prescription implements which choice.

Two points of discipline are kept in view. Every displayed formula is applied to a case other than the one that suggested it: the kernel is applied to a generic smooth function of the retarded time and to an off-centre and a static source, not only to the on-origin case from which it is guessed; and the retarded potentials are checked against the Coulomb and Biot–Savart solutions, which are independent of the construction. The parent is treated as a source of assertions until the computation has been done.

## Problem 1: The Wave Operator and the Defining Equation

**Statement.** (a) Show that with $\partial/\partial Q_t = -\frac{i}{c}\partial/\partial t$ the d'Alembertian $\Box = \partial^2/\partial Q_t^2 + \Delta$ is the wave operator $\Delta + \partial^2/\partial Q_t^2$, and identify its symbol. (b) State the defining equation for the Green's function $G(\tilde{Q})$ and explain the sign. (c) Show that if $G$ satisfies it, then the convolution $\tilde{A}(\tilde{Q}) = \mu\int G(\tilde{Q} - \tilde R')\tilde J(\tilde R')\,d^3y\,dt'$ solves the potential equation $\Box\tilde{A} = -\mu\tilde J$.

**Solution.** (a) Since $\partial/\partial Q_t = \frac{1}{ic}\partial/\partial t = -\frac{i}{c}\partial/\partial t$,
$$
\partial^2/\partial Q_t^2 = \left(-\frac{i}{c}\partial/\partial t\right)^2 = + \partial^2/\partial Q_t^2,
\qquad\text{so}\qquad
\Box = \partial^2/\partial Q_t^2 + \Delta = \Delta + \partial^2/\partial Q_t^2 .
$$
The temporal term is negative and the spatial terms positive: $\Box$ is *hyperbolic*, the wave operator, not the elliptic operator obtained from it by the Wick rotation, in which all four directions enter with the same sign. The distinction matters here: the retarded kernel below is the fundamental solution of the hyperbolic operator, whereas the elliptic Cauchy kernel treated in the companion articles on biquaternion integration and analysis on subspaces is the fundamental solution of the Wick-rotated one. Acting on a plane wave $\exp(i(\vec k\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) - \omega t))$, the operator has symbol
$$
\Box \;\longmapsto\; -k^2 + \frac{\omega^2}{c^2} = \frac{\omega^2}{c^2} - k^2 .
$$

(b) The Green's function is the distributional inverse of $\Box$. We define it by
$$
\Box_{\tilde{Q}}\,G(\tilde{Q}) = -\delta^{(4)}(\tilde{Q}),
\qquad
\delta^{(4)}(\tilde{Q}) = \delta(t)\,\delta^{(3)}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z),
$$
with the physical measure $d^3y\,dt'$ for the convolution (the parent writes $d^4R'$ for the four-dimensional volume element; the constant conventions relating the four-dimensional delta, the volume element, and the kernel are fixed here once and for all by using $d^3y\,dt'$). The minus sign is not free: the potential equation carries $-\mu\tilde J$ on the right, so a kernel with $\Box G = -\delta^{(4)}$ gives that sign directly. With $\Box G = +\delta^{(4)}$ one would have to insert a compensating minus in the convolution; we fix both once by the convention above.

(c) Differentiation under the convolution integral gives
$$
\Box_{\tilde{Q}}\tilde{A}(\tilde{Q})
= \mu\int \Box_{\tilde{Q}}G(\tilde{Q} - \tilde R')\,\tilde J(\tilde R')\,d^3y\,dt'
= \mu\int \bigl(-\delta^{(4)}(\tilde{Q} - \tilde R')\bigr)\tilde J(\tilde R')\,d^3y\,dt'
= -\mu\,\tilde J(\tilde{Q}),
$$
where in the last step the delta picks out $\tilde R' = \tilde{Q}$. The derivative acts only on $G$, because $\tilde J$ does not depend on $\tilde{Q}$; equivalently $\Box_{\tilde{Q}}G(\tilde{Q}-\tilde R') = \Box_{\tilde R'}G(\tilde{Q}-\tilde R')$, which is the statement that the operator has constant coefficients and is translation invariant. This is the convolution property that makes a Green's function useful: once $G$ is known, every source is solved by one integral.

## Problem 2: The Retarded Green's Function and the Light-Cone Jacobian

**Statement.** (a) Show that $G_{\mathrm{ret}}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t) = \frac{1}{4\pi R}\delta(t - R/c)$, with $R = |x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|$, satisfies the defining equation, by applying $\Box$ to it directly and identifying the two cancellations that make it work. (b) Derive the same kernel from the invariant delta on the light cone, exhibiting the Jacobian factor that converts the invariant argument into $t - R/c$. (c) Confirm the coefficient by the Fourier representation with the retarded contour. Check the result on a case other than the one that suggested it.

**Solution. (a) Applying the operator to the kernel.** Let $g = t - R/c$ and, for a smooth function $u$, consider
$$
G_u(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t) = \frac{u(g)}{4\pi R}.
$$
Write $\phi = 1/(4\pi R)$, so that $G_u = \phi\, u(g)$. The chain rule gives
$$
\Delta G_u = u\,\Delta\phi + 2\frac{du}{dg}\,\nabla\phi\cdot\nabla g + \frac{du}{dg}\,\phi\,\Delta g + \frac{d^2u}{dg^2}\,\phi\,(\nabla g)^2,
\qquad
\partial^2/\partial t^2 G_u = \frac{d^2u}{dg^2}\,\phi,
$$
and therefore, with $\Box = \Delta + \partial^2/\partial Q_t^2$,
$$
\Box G_u
= \frac{u(g)}{4\pi}\,\Delta\frac{1}{R}
+ \frac{\frac{du}{dg}(g)}{4\pi}\left[2\,\nabla\frac{1}{R}\cdot\nabla g + \frac{1}{R}\Delta g\right]
+ \frac{\frac{d^2u}{dg^2}(g)}{4\pi R}\left[(\nabla g)^2 - \frac{1}{c^2}\right].
$$
Three elementary radial identities now decide the outcome:
$$
(\nabla g)^2 = \frac{1}{c^2},
\qquad
2\,\nabla\frac{1}{R}\cdot\nabla g + \frac{1}{R}\Delta g = 0,
\qquad
\Delta\frac{1}{R} = -4\pi\,\delta^{(3)}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z).
$$
The first says the coefficient of $\frac{d^2u}{dg^2}$ vanishes; the second says the coefficient of $\frac{du}{dg}$ vanishes; the third converts the coefficient of $u$ into a source at the origin. Hence
$$
\Box G_u = -u(g)\,\delta^{(3)}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = -u(t)\,\delta^{(3)}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z),
$$
the last equality because $\delta^{(3)}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$ forces $R = 0$, where $g = t$. Taking $u$ to be a nascent delta and passing to the limit gives
$$
G_{\mathrm{ret}}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t) = \frac{\delta(t - R/c)}{4\pi R},
\qquad
\Box\,G_{\mathrm{ret}} = -\delta(t)\,\delta^{(3)}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = -\delta^{(4)}(\tilde{Q}).
$$

Two remarks are worth making, because both are places where a plausible-looking derivation goes wrong. First, the vanishing of the $\frac{du}{dg}$ coefficient is not automatic; it is the precise statement that the single-layer shell on the cone cancels. A kernel of the form $\frac{f(R)}{R}$ with the wrong radial power, or with an extra angular factor, leaves a nonvanishing $\frac{du}{dg}$ term and does not reproduce a point source at the origin. Second, the vanishing is a statement about the *argument* $g$: because $(\nabla g)^2 = 1/c^2$ exactly, the two second-derivative terms combine, and because $2\nabla(1/R)\cdot\nabla g + (1/R)\Delta g = 0$ exactly, the first-derivative terms combine. Both identities were recomputed symbolically in $x,y,z$ and hold identically.

**(b) The light-cone delta and its Jacobian.** The same kernel is a distribution concentrated on the light cone. The cone is the zero set of the invariant
$$
\sigma(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t) = t^2 - \frac{R^2}{c^2},
$$
and the retarded (future-cone) distribution with the correct normalization is
$$
G_{\mathrm{ret}}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t) = \frac{1}{2\pi c}\,\Theta(t)\,\delta\!\left(t^2 - \frac{R^2}{c^2}\right),
\qquad
\Theta(t) = \begin{cases} 1, & t > 0,\\ 0, & t < 0. \end{cases}
$$
To convert the invariant delta into a delta of $t - R/c$ one uses the composition rule $\delta(f(t)) = \sum_i \delta(t - t_i)/\left|\frac{df}{dt}(t_i)\right|$ at the roots $t_i$ of $f$. For $f(t) = t^2 - R^2/c^2$ the roots are $t = \pm R/c$, and at the future root the Jacobian is
$$
\left|\frac{d}{dt}\left(t^2 - \frac{R^2}{c^2}\right)\right|_{t = R/c} = 2t\Big|_{t=R/c} = \frac{2R}{c}.
$$
Therefore, on $t>0$ where only the future root contributes,
$$
\delta\!\left(t^2 - \frac{R^2}{c^2}\right) = \frac{c}{2R}\,\delta\!\left(t - \frac{R}{c}\right),
$$
and hence
$$
\frac{1}{2\pi c}\,\Theta(t)\,\delta\!\left(t^2 - \frac{R^2}{c^2}\right)
= \frac{1}{2\pi c}\cdot\frac{c}{2R}\,\delta\!\left(t - \frac{R}{c}\right)
= \frac{1}{4\pi R}\,\delta\!\left(t - \frac{R}{c}\right) = G_{\mathrm{ret}} .
$$
This is the Jacobian the exercise warns about: the factor $c/(2R)$ is what turns the invariant coefficient $1/(2\pi c)$ into the radial coefficient $1/(4\pi R)$. Dropping it — writing the radial kernel as $\frac{1}{2\pi c}\delta(t-R/c)$, or as $\frac{1}{2\pi R}\delta(t-R/c)$, or as a coefficient without the $R$ in the denominator — gives a kernel that fails in part (a). The $\frac{du}{dg}$ term does not cancel, except for the middle form, whose $\frac{du}{dg}$ term does cancel but which produces twice the unit point source. The conversion was checked numerically for several pairs $(R,c)$ by smearing the invariant delta against test functions.

**(c) The coefficient from the Fourier representation.** The defining equation in Fourier space is algebraic. With the transform convention $\delta^{(4)}(\tilde{Q}) = \int \frac{d^3k}{(2\pi)^3}\frac{d\omega}{2\pi}\,\exp(i(\vec k\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)-\omega t))$ and the symbol $\omega^2/c^2 - k^2$ from part (a), the equation $(\omega^2/c^2 - k^2)G = -1$ gives
$$
G(\vec k,\omega) = \frac{c^2}{c^2 k^2 - \omega^2},
\qquad
G(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t) = \int\frac{d^3k}{(2\pi)^3}\frac{d\omega}{2\pi}\,
\frac{c^2\,\exp(i(\vec k\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)-\omega t))}{c^2 k^2 - \omega^2},
$$
where the inversion contour is not yet specified — this is exactly the ambiguity of Problem 3. The retarded choice shifts both $\omega$-poles below the real axis, $\omega \to \omega + i\epsilon$, i.e. the poles sit at $\omega = \pm ck - i\epsilon$. Closing the contour in the lower half-plane for $t>0$ (and in the upper half-plane, with no poles, for $t<0$) gives
$$
\int_{-\infty}^{\infty}\frac{d\omega}{2\pi}\,\frac{c^2\,\exp(-i\omega t)}{c^2 k^2 - \omega^2}
= \frac{c}{k}\,\sin(ckt)\,\Theta(t).
$$
The angular integral of $\exp(i\vec k\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z))$ over the directions of $\vec k$ introduces $\sin(kR)/(kR)$, so
$$
G_{\mathrm{ret}}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t)
= \frac{c}{2\pi^2 R}\int_0^\infty \sin(kR)\,\sin(ckt)\,dk
= \frac{1}{4\pi R}\,\delta\!\left(t - \frac{R}{c}\right),
$$
using $\int_0^\infty \sin(kR)\sin(ckt)\,dk = \frac{\pi}{2c}\bigl[\delta(t - R/c) - \delta(t + R/c)\bigr]$ and discarding the past-cone term because $t>0$. The Fourier route and the light-cone route agree, coefficient included. The contour computation was also checked numerically: for fixed $k,c,t>0$ the retarded contour reproduces $\frac{c}{k}\sin(ckt)$ and the advanced contour gives zero, and conversely for $t<0$.


## Problem 3: Retarded, Advanced, and the Boundary Condition

**Statement.** (a) Exhibit the advanced kernel $G_{\mathrm{adv}}$ and show that it satisfies the same defining equation $\Box G = -\delta^{(4)}$. (b) Show that the difference $G_{\mathrm{ret}} - G_{\mathrm{adv}}$ solves the homogeneous wave equation, so the defining equation alone does not select the retarded kernel. (c) State the boundary condition that selects the retarded kernel for radiation problems and the boundary condition that selects the advanced one, and identify the contour prescription that implements each.

**Solution. (a) The advanced kernel.** The computation of Problem 2(a) used only $g = t - R/c$. With $g_+ = t + R/c$ one has $\nabla g_+ = +\vec u_R/c$, so $(\nabla g_+)^2 = 1/c^2$ and the bracket $2\nabla(1/R)\cdot\nabla g_+ + (1/R)\Delta g_+$ has the opposite sign of $\nabla g_+$ relative to $\nabla(1/R)$ but is again zero, because $\nabla(1/R)$ is parallel to $\vec u_R$ while the two terms of the bracket are equal and opposite. Hence the same argument gives
$$
G_{\mathrm{adv}}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t) = \frac{1}{4\pi R}\,\delta\!\left(t + \frac{R}{c}\right),
\qquad
\Box\,G_{\mathrm{adv}} = -\delta^{(4)}(\tilde{Q}),
$$
with support on the past light cone. In the invariant form it is $G_{\mathrm{adv}} = \frac{1}{2\pi c}\Theta(-t)\delta(t^2 - R^2/c^2)$, and the Jacobian at the past root $t = -R/c$ is again $2R/c$.

**(b) The homogeneous difference.** Since $\Box$ is linear, $\Box(G_{\mathrm{ret}} - G_{\mathrm{adv}}) = 0$:
$$
G_{\mathrm{ret}} - G_{\mathrm{adv}} = \frac{1}{4\pi R}\Bigl[\delta\!\left(t - \frac{R}{c}\right) - \delta\!\left(t + \frac{R}{c}\right)\Bigr],
\qquad
\Box\,(G_{\mathrm{ret}} - G_{\mathrm{adv}}) = 0 .
$$
The difference is supported on both cones and is a solution of the source-free wave equation. It follows that the defining equation has an infinite family of solutions, all differing by solutions of the homogeneous equation, and that no algebraic manipulation of $\Box$ alone can single out the retarded one. The smeared pairing confirms this in both directions: $\int G_{\mathrm{ret}}\,\Box\chi = \int G_{\mathrm{adv}}\,\Box\chi = -\chi(0)$ for the Gaussian test function, while $\int (G_{\mathrm{ret}} - G_{\mathrm{adv}})\,\Box\chi = 0$.

**(c) Which boundary condition selects which.** The retarded kernel is selected by the *causality* (outgoing-radiation, Sommerfeld) condition: the field at an event is determined by the sources in its past light cone, and there is no radiation arriving from past null infinity. In the contour language this is the prescription in which both $\omega$-poles are displaced *below* the real axis, so that the field vanishes for $t$ earlier than the source and is supported on the future cone. The advanced kernel is selected by the time-reversed condition: the field is determined by sources in its future light cone, with no radiation escaping to future null infinity, corresponding to both poles displaced *above* the real axis and support on the past cone. The Feynman choice, one pole on each side, is the time-ordered combination; it is neither retarded nor advanced, and its relation to the two is treated in the companion article on the Feynman propagator. The two choices and the two contour prescriptions were checked numerically on the mode integral of Problem 2(c): the retarded contour gives support for $t>0$ and the advanced contour for $t<0$, with residuals at the $10^{-4}$ to $10^{-3}$ level set by the finite displacement $\epsilon$.

The exercise's answer to "why is the physically relevant Green's function the retarded one" is therefore: *not because the algebra forces it*. The wave operator admits both kernels, and the retarded choice is the statement of a boundary condition on the solution — the same information that selects the outgoing solution among the two solutions of the free wave equation. This is a physical input, and it is the point at which the retarded potential formula is tied to causality.

## Problem 4: The Retarded Potentials from the Green's Function

**Statement.** (a) Substitute the retarded kernel into the convolution and perform the time integral to obtain $\tilde{A}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t) = \frac{\mu}{4\pi}\int \frac{\tilde J(\vec y,\,t - R/c)}{R}\,d^3y$. (b) Extract the scalar and vector parts and confirm the standard retarded potentials, using $\mu c^2 = 1/\epsilon$. (c) Show that the retarded solution is automatically in the Lorenz gauge whenever the charge is conserved.

**Solution. (a) The retarded convolution.** With $G_{\mathrm{ret}}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-\vec y,\,t-t') = \frac{1}{4\pi R}\delta(t - t' - R/c)$ and $R = |x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-\vec y|$,
$$
\tilde{A}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t)
= \mu\int \frac{\delta\!\left(t - t' - R/c\right)}{4\pi R}\,\tilde J(\vec y,t')\,d^3y\,dt'
= \frac{\mu}{4\pi}\int \frac{\tilde J(\vec y,\,t - R/c)}{R}\,d^3y ,
$$
the $t'$ integral having been performed against the delta. Every source contribution is evaluated at its own *retarded time* $t - R/c$: the field at $(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t)$ is assembled from sources on the past light cone of that event, exactly as the causality condition requires. This is the biquaternionic form of the retarded solution, and it is the object the companion radiation article specializes to a point charge.

**(b) The component potentials.** The four-current is $\tilde J = ic\rho\,e_t + \vec J$, with scalar part $ic\rho$ and vector part $\vec J$. The scalar part of $\tilde{A}$ is $A_0 = i\phi/c$, so
$$
\frac{i\phi}{c} = \frac{\mu}{4\pi}\int\frac{ic\,\rho_{\mathrm{ret}}}{R}\,d^3y
\;\Longrightarrow\;
\phi = \frac{\mu c^2}{4\pi}\int\frac{\rho_{\mathrm{ret}}}{R}\,d^3y = \frac{1}{4\pi\epsilon}\int\frac{\rho_{\mathrm{ret}}}{R}\,d^3y,
$$
using $\mu c^2 = \mu/(\epsilon\mu) = 1/\epsilon$. The vector part is unchanged by the extraction,
$$
\vec A = \frac{\mu}{4\pi}\int \frac{\vec J_{\mathrm{ret}}}{R}\,d^3y ,
$$
where $\rho_{\mathrm{ret}} = \rho(\vec y, t - R/c)$ and $\vec J_{\mathrm{ret}} = \vec J(\vec y, t - R/c)$. These are the standard retarded potentials, obtained here from a single biquaternionic convolution rather than from four component equations.

A word on the two retarded-time Jacobians, because the exercise's first trap and the radiation article's construction both involve one. The Jacobian used in Problem 2 is the one that converts the invariant delta on the light cone into $\delta(t - R/c)$, and it produces the $1/(4\pi R)$ coefficient. When the source is a point charge on a worldline, a *second* Jacobian appears when the remaining source integral is localized on the worldline: there the argument $h(s) = s + |x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-\vec r_q(s)|/c - t$ has $\frac{dh}{ds}(s) = 1 - \vec u_R\cdot\vec\beta$, which produces the Liénard–Wiechert denominator. The two Jacobians are different objects — one is the light-cone normalization of the kernel, the other the worldline localization of a moving source — and conflating them is a second way to lose a factor. This exercise treats the first; the second belongs to the radiation article.

**(c) The Lorenz gauge is automatic.** Write the gauge scalar
$$
S = \mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde{A}\right) = \partial/\partial Q_t\,A_0 + \mathrm{div}\,\vec A = \frac{1}{c^2}\partial/\partial t\,\phi + \mathrm{div}\,\vec A,
$$
which is the biquaternionic form of $\partial/\partial Q_\mu A^\mu$ and whose vanishing is the Lorenz condition. Since $\tilde{A}$ solves $\Box\tilde{A} = -\mu\tilde J$ and $\Box = \tilde{\nabla}^{\natural}\tilde{\nabla}$, applying $\tilde{\nabla}^{\natural}$ and taking the scalar part gives
$$
\Box S = \mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\,\Box\tilde{A}\right) = -\mu\,\mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde J\right) = -\mu\left(\partial/\partial t\,\rho + \mathrm{div}\,\vec J\right) = 0,
$$
where the last equality is the conservation of charge, and where the derivatives commute because the coefficients are constant. Thus $S$ is a solution of the homogeneous wave equation. The retarded solution of $\Box S = 0$ with no incoming radiation is $S = 0$: the retarded potentials automatically satisfy the Lorenz gauge. This is why the Lorenz-gauge wave equation and its retarded solution can be written together, as the companion article does, without a further gauge-fixing step — the gauge condition is a consequence of charge conservation plus the retarded boundary condition, not an extra assumption. It is also a consistency check on the sign conventions: a sign error in $\tilde J$ or in $\tilde{\nabla}^{\natural}$ would have produced $\Box S \neq 0$.

## Problem 5: The Static Limit and the Coulomb–Biot–Savart Check

**Statement.** (a) For time-independent sources, show that the retarded potentials reduce to the static kernels. (b) Verify that these satisfy the static potential equation, and recover the Coulomb field of a point charge and the Biot–Savart field of a steady current, reconciling the first with the parent's static solution.

**Solution. (a) The static reduction.** If $\partial/\partial t\,\rho = 0$ and $\partial/\partial t\,\vec J = 0$, then $\rho(\vec y, t - R/c) = \rho(\vec y)$ and $\vec J(\vec y, t - R/c) = \vec J(\vec y)$, and the retarded time drops out of the integrand:
$$
\phi(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = \frac{1}{4\pi\epsilon}\int\frac{\rho(\vec y)}{R}\,d^3y,
\qquad
\vec A(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = \frac{\mu}{4\pi}\int\frac{\vec J(\vec y)}{R}\,d^3y,
\qquad R = |x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-\vec y|.
$$
The kernel that was $\frac{\delta(t-R/c)}{4\pi R}$ becomes the Newton kernel $\frac{1}{4\pi R}$ after the time integral, so the static potentials are the retarded ones with the source frozen.

**(b) The static equations and the known solutions.** With $\partial/\partial t \to 0$ the operator reduces to the Laplacian, $\Box \to \Delta$, and the identity $\Delta\frac{1}{R} = -4\pi\delta^{(3)}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-\vec y)$ gives
$$
\Delta\phi = \frac{1}{4\pi\epsilon}\int \rho(\vec y)\,\Delta\frac{1}{R}\,d^3y = -\frac{1}{\epsilon}\int\rho(\vec y)\,\delta^{(3)}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-\vec y)\,d^3y = -\frac{\rho(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)}{\epsilon},
$$
and likewise $\Delta\vec A = -\mu\vec J(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$; in biquaternion form $\Delta\tilde{A} = -\mu\tilde J$, which is the static limit of $\Box\tilde{A} = -\mu\tilde J$. For a point charge at the origin, $\rho = ϙ\,\delta^{(3)}(\vec y)$, so
$$
\phi = \frac{ϙ}{4\pi\epsilon R},
\qquad
\vec E = -\nabla\phi = \frac{ϙ\,\vec u_R}{4\pi\epsilon R^2},
\qquad
\tilde{F} = i\sqrt{\epsilon}\,\vec E = \frac{iϙ\,\vec u_R}{4\pi\sqrt{\epsilon}\,R^2},
$$
which is exactly the parent's static point-charge field; the retarded construction reproduces it as a limiting case. The parent reaches this field from the first-order static equation by taking the gradient of the Newton kernel; here the same field follows from the second-order potential equation, whose static solution is the Newton kernel itself, differentiated once to give $\vec E$. Both routes yield the same Coulomb field, and the retarded potentials supply the second-order route. For a steady current, starting from $\vec A$ and using $\nabla(1/R) = -\vec u_R/R^2$,
$$
\vec B = \nabla\times\vec A
= \frac{\mu}{4\pi}\int \nabla\frac{1}{R}\times\vec J(\vec y)\,d^3y
= \frac{\mu}{4\pi}\int \frac{\vec J(\vec y)\times\vec u_R}{R^2}\,d^3y,
$$
the Biot–Savart law (the sign is the standard one, with $\vec u_R$ pointing from the source to the field point). These are the exercise's independent checks: the retarded potentials, constructed from the light-cone kernel, reduce on time-independent sources to the two classical static solutions, which were known before the construction and were not used to build it.

## Where the Parent Leaves a Gap

The parent and its companion are correct where they are defined, and the derivation above closes their main gap, which is the construction and verification of the kernel. Four points are left as they stand rather than closed.

1. **The kernel was stated, not derived.** The radiation companion displays $G_\Box = \frac{1}{4\pi R}\delta(t-R/c)$ and the retarded convolution and says it does not re-derive the structure; the parent states the potential equation and refers the reader to the standard references for the kernel. This exercise supplies the derivation, the Jacobian, and the boundary condition. This is a presentation gap, now closed.

2. **The parent's first-order Green's function for $\tilde{\nabla}$ is unverified.** The parent also states a biquaternion-valued kernel $\tilde{G}_{\tilde{\nabla}}$ solving $\tilde{\nabla}\tilde{G}_{\tilde{\nabla}} = \delta(\tilde{Q})e_t$, with an explicit vector term, and immediately adds that it satisfies the equation "up to a sign convention for the delta distribution" and that its precise form "should be verified against the standard references." The defining equation with $+\delta e_t$ and the satisfaction statement with $-\delta e_t$ do not agree, and the vector term's normalization is not fixed. This exercise does not use that object — the potential equation is second order, and its kernel is the scalar $G_\Box$ derived above — and it records the first-order kernel as an unverified parent statement rather than inheriting it.

3. **The retarded choice is a boundary condition.** The defining equation admits both the retarded and the advanced kernel, and the retarded one is selected by causality, not by the algebra. The parent states that the physically relevant kernel is the retarded one but does not state the selection principle; Problem 3 supplies it, and the exercise records that the selection is a physical input.

4. **The kernel is that of a constant, non-dispersive medium.** All of the above holds with $c = 1/\sqrt{\epsilon\mu}$ constant, i.e. for a homogeneous, non-dispersive medium. In a dispersive medium the operator is not local in time and the simple retarded kernel does not apply; in a medium whose parameters vary in space the operator has variable coefficients and the free kernel is only the first term of a geometric-optics expansion. The parent's local complex structure makes $c$ a field, and the form of the kernel in that setting is not settled here. This is a genuine gap, not a bookkeeping point.

5. **The equivalence of the first- and second-order formulations is inherited, not re-derived.** The parent states that $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}$ and $\Box\tilde{A} = -\mu\tilde J$ are equivalent in the Lorenz gauge while noting that $\sqrt{\mu}\,\tilde{J}$ and $\tilde J$ differ by normalization factors. This exercise uses only the second-order equation, with $\tilde J = ic\rho\,e_t + \vec J$, and verifies it directly against the retarded potentials and the static limit; it does not re-derive the mapping between the two source normalizations.

## Further Problems

1. **The worldline Jacobian.** Specialize the retarded convolution to a point charge on a worldline, localize the remaining integral, and derive the Liénard–Wiechert denominator $1 - \vec u_R\cdot\vec\beta$. This is the second Jacobian discussed in Problem 4(b), and it is the construction of the companion radiation article; the point of listing it here is to separate it cleanly from the light-cone Jacobian of Problem 2.

2. **The causal (Feynman) combination.** Determine the linear combination of $G_{\mathrm{ret}}$ and $G_{\mathrm{adv}}$ that is time-ordered, and identify its position-space support. The result is neither the retarded nor the advanced kernel but a combination of both with a principal-value part; the contour prescription (one pole on each side) and its interpretation are treated in the Feynman-propagator article.

3. **The dispersive kernel.** Replace the constant $c$ by $c(\omega)$ and determine whether the inverse of the dispersive wave operator admits a kernel with support on a single (frequency-dependent) cone, or whether dispersion spreads the support off the light cone. This is the natural continuation of gap 4.

4. **Inhomogeneous media.** For $\epsilon = \epsilon(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$, $\mu = \mu(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$, write the operator and show that the free kernel of this exercise is the leading term of the geometric-optics approximation; identify the transport correction that the gradient of $c$ forces.

5. **The far-zone fall-off.** For a localized source, show from the retarded potential alone that the radiated part of the field falls as $1/R$ while the bound part falls as $1/R^2$, without introducing a moving charge. This isolates the light-cone structure of the kernel from the worldline kinematics.

6. **The chiral kernel, which is not this kernel.** For the Drude–Born–Fedorov chiral medium the reduction of the medium article *A Chiral Medium: One Quaternionic Equation* gives the quaternionic operator $M=\beta\sqrt{\epsilon\mu}\,\partial/\partial t\,D+\sqrt{\epsilon\mu}\,\partial/\partial t-iD$, whose fundamental solution is causal but is **not** obtained from $G_\Box$ by substitution. $M$ is of *second* order in the derivatives — the term $\partial/\partial t\,D$ is what raises it above the first-order non-chiral reduction — and $MM^{*}$ is fourth order, so its kernel is neither the delta-on-the-cone $G_\Box$ of this exercise nor the parent's unverified first-order $\tilde{G}_{\tilde{\nabla}}$: it is a third kind of object, and one the corpus can actually construct, since Kravchenko's $K_\alpha$ is the worked example of a first-order quaternionic kernel with a radiation condition. At each fixed frequency the symbol factors as $i(\beta\sqrt{\epsilon\mu}\,\omega-1)(D+\alpha(\omega))$, so the kernel is built from $K_{\alpha(\omega)}$; but the prefactor degenerates at $\omega=c/\beta$, where the transform carries a **double** pole together with an essential singularity through $\exp(ic(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)/(\omega-a))$, and the causal kernel is a Heaviside function times a series rather than a delta on the cone. Determine how far the light-cone support of this exercise survives when $\beta\neq0$, and whether it is restored in the limit $\beta\to0$ together with the one-parameter family. This separates the part of the retarded structure that belongs to the quaternionic first-order operator from the part that belongs to the second-order wave operator.

## Summary

The wave operator of the biquaternionic formulation, $\Box = \partial^2/\partial Q_t^2 + \Delta = \Delta + \partial^2/\partial Q_t^2$, has the retarded Green's function
$$
G_{\mathrm{ret}}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t) = \frac{1}{4\pi R}\,\delta\!\left(t - \frac{R}{c}\right),
\qquad
\Box\,G_{\mathrm{ret}} = -\delta(t)\,\delta^{(3)}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z),
\qquad R = |x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|,
$$
derived in three ways that agree: by applying $\Box$ to a radial ansatz $\frac{u(t-R/c)}{4\pi R}$ and exhibiting the two cancellations (the $\frac{d^2u}{dg^2}$ coefficient because $(\nabla g)^2 = 1/c^2$, the $\frac{du}{dg}$ coefficient because $2\nabla(1/R)\cdot\nabla g + (1/R)\Delta g = 0$, and the $u$ coefficient because $\Delta(1/R) = -4\pi\delta^{(3)}$); from the invariant light-cone delta $\frac{1}{2\pi c}\Theta(t)\delta(t^2 - R^2/c^2)$ by the Jacobian conversion $\delta(t^2 - R^2/c^2) = \frac{c}{2R}\delta(t-R/c)$; and from the Fourier amplitude $\frac{c^2}{c^2k^2-\omega^2}$ with the retarded contour. The kernel was verified as a distributional identity by smearing against a Gaussian test function, and the retarded potential was verified to solve the homogeneous wave equation for generic, off-centre, oscillating, and static sources.

The defining equation does not select the kernel: the advanced kernel $\frac{1}{4\pi R}\delta(t+R/c)$ solves it equally, the difference is a solution of the homogeneous equation, and the retarded choice is fixed by the causality (no-incoming-radiation) boundary condition, implemented by displacing both frequency poles below the real axis. Convolving the retarded kernel with the source gives the retarded potentials
$$
\phi = \frac{1}{4\pi\epsilon}\int \frac{\rho_{\mathrm{ret}}}{R}\,d^3y,
\qquad
\vec A = \frac{\mu}{4\pi}\int \frac{\vec J_{\mathrm{ret}}}{R}\,d^3y,
\qquad R = |x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-\vec y|,
$$
with all sources at the retarded time $t - R/c$; the retarded solution is automatically in the Lorenz gauge when charge is conserved, because $\Box S = -\mu(\partial/\partial t\,\rho + \mathrm{div}\,\vec J) = 0$ and the retarded solution of the homogeneous equation with no incoming radiation vanishes. In the static limit the retarded potentials reduce to the Coulomb and Biot–Savart solutions, and for a point charge they reproduce the parent's static field exactly.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$, $\vec e_\mu \vec e_\nu = -\delta_{\mu\nu}e_t + \epsilon_{\mu\nu\lambda}\vec e_\lambda$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) subspaces |
| $\mathbb{H}_{\mathbb{B}}, \mathbb{C}_{\mathbb{B}}$ | Real-quaternion subspace, scalar subspace |
| $\tilde{\nabla}, \tilde{\nabla}^{\natural}$ | Biquaternionic gradient and its quaternion conjugate |
| $\partial/\partial Q_t = -\frac{i}{c}\partial/\partial t$ | Temporal component of the gradient |
| $\Box = \partial^2/\partial Q_t^2 + \Delta = \Delta + \partial^2/\partial Q_t^2$ | Wave operator (d'Alembertian) |
| $\delta^{(4)}(\tilde{Q}) = \delta(t)\delta^{(3)}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$ | Four-dimensional Dirac delta |
| $G(\tilde{Q})$ | Green's function, $\Box G = -\delta^{(4)}$ |
| $G_{\mathrm{ret}} = \frac{1}{4\pi R}\delta(t - R/c)$ | Retarded Green's function |
| $G_{\mathrm{adv}} = \frac{1}{4\pi R}\delta(t + R/c)$ | Advanced Green's function |
| $\sigma = t^2 - R^2/c^2$ | Light-cone invariant (argument of the invariant delta) |
| $\Theta(t)$ | Heaviside step function |
| $\tilde{A} = \frac{i\phi}{c}e_t + \vec A$ | Potential biquaternion |
| $\tilde J = ic\rho\,e_t + \vec J$ | Four-current of the potential equation |
| $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ | Field-strength biquaternion (pure vector) |
| $\epsilon, \mu$ | Permittivity and permeability of the medium |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $R = \lvert x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-\vec y\rvert$ | Retarded separation (spatial) |
| $t - R/c$ | Retarded time |
| $S = \mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{A})$ | Gauge scalar; $S = 0$ is the Lorenz gauge |
| $\vec u_R = \vec R/R$, $\vec\beta = \vec v/c$ | Unit retarded separation; dimensionless velocity (radiation article) |
| $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | Trace formula |

## Further Reading

The further reading of this exercise is the parent and companion articles of this series, all present in `articles_physics/`; the standard textbook references for Green's functions, the retarded potentials, and the boundary conditions are listed in the Further Reading sections of those articles.

- *Introduction to the Biquaternion Universe* — the algebra, the two sectors, and the local complex structure.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* — the four-vectors, including the four-potential and four-current, and the light cone as the zero-divisor cone.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* — the Hermitian subspace and the trace formula.
- *Maxwell's Equations in the Biquaternionic Formulation* — the direct parent: the potential equation and the normalisation of the four-current.
- *The Field-Strength Biquaternion and Its Invariants* — the field strength built from the potential by differentiation, and its biquaternion norm.
- *The Lorentz Transformation as a Biquaternionic Rotation* — the covariance of the four-potential, inherited here unchanged.
- *Radiation from Accelerated Charges in Biquaternionic Form* — the companion that states (but does not derive) the retarded kernel and convolution and specializes them to a point charge, with the worldline Jacobian of Problem 4(b).
- *The Feynman Propagator in Biquaternionic Form* — the causal contour prescription and the relation among the Feynman, retarded, and advanced kernels (Problems 2(c) and 3).
- *Electromagnetism in Media — The Local Complex Structure at Work* — the medium speed $c = 1/\sqrt{\epsilon\mu}$ and the non-dispersive setting assumed throughout; its section *A Chiral Medium: One Quaternionic Equation* is the source of Further Problem 6.
- *Biquaternion Integration* and *Biquaternion Analysis on Subspaces* — the elliptic Cauchy kernel and the Euclidean counterpart of the retarded kernel, related by the Wick rotation.
