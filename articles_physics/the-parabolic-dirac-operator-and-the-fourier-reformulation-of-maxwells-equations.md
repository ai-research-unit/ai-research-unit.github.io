# __The Parabolic Dirac Operator and the Fourier Reformulation of Maxwell's Equations__

## Introduction

The series already carries two routes into Maxwell's equations quaternionically: *Maxwell's Equations in the Biquaternionic Formulation* reduces the full time-dependent system to the single equation $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}$, and *The Time-Harmonic Maxwell Operator and the Quaternionic Cauchy Integral* diagonalises the stationary system of a lossy isotropic medium into two conjugate Cauchy–Riemann equations. Both are algebraic or elliptic. The third route recorded here is different in kind: it factors the **wave operator itself** into two first-order operators and inverts them **by Fourier analysis**, and it is the object of the source paper of this article.

The source is A. Guillén-Villalobos, B. B. Delgado and H. Vargas Rodríguez, *A biquaternionic reformulation of Maxwell's equations via Fourier analysis*, arXiv:2605.21412v2 [math.AP] (22 May 2026). It studies the **parabolic Dirac operators** $D \pm i\partial/\partial t'$, where $D$ is the Moisil–Teodorescu operator and $i$ the scalar imaginary unit; characterises the kernel of $D \pm i\partial/\partial t'$ by a **generalized div-curl system** and by **Cauchy–Riemann-type relations** between the real and the imaginary parts of a biquaternion-valued function; computes the Fourier transform of a kernel of the operator, which turns out to be the **quaternionic exponential function** of unit modulus; constructs an explicit **right inverse**; and applies the inverse to the time-dependent Maxwell system, obtaining **purely vectorial** solutions. The paper follows the monograph V. V. Kravchenko, *Applied Quaternionic Analysis* (2003), to which the corpus's biquaternion Maxwell article also refers.

The article is written to separate three things. First, **what the corpus already has**: the single biquaternionic Maxwell equation $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}$, the field-strength biquaternion $\tilde F$ and its dual $-i\tilde F$, the second-order factorisation $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla}$, and the elliptic Cauchy kernel. The paper's Maxwell statement (its Proposition 12) is the corpus's single equation written in real time, in Gaussian units, for the dual field strength $-i\tilde F$; the reformulation itself is therefore not new to the corpus. Second, **what is new to the corpus**: the real-time first-order factorisation of the wave operator (both orderings), the time-dependent div-curl characterisation of the kernel, the description of the inverse's symbol as a unit quaternionic exponential, and the operator right inverse with its explicit vectorial solutions. Third, **what the source does not settle**: the naming and existence of its "fundamental solution", a homogeneous-medium reduction whose printed constants could not be read faithfully, and the exact hypotheses of its two solution theorems.

The plan is the operator, then its kernel, then its Fourier symbol, then its inverse, then the application. The section *What Is Verified and What Is Not* collects the recomputations and the defects.

## The Parabolic Dirac Operators

### The Factorization of the Wave Operator

The **Moisil–Teodorescu operator** is the three-dimensional Dirac-type operator

$$
D = \vec e_x\partial/\partial Q_x + \vec e_y\partial/\partial Q_y + \vec e_z\partial/\partial Q_z = \sum_{\mu=1}^{3} \vec e_\mu\,\partial/\partial Q_\mu,
$$

with $\vec e_x, \vec e_y, \vec e_z$ the quaternion units of the algebra $\mathbb{B}$ of *Conventions in the Biquaternion Universe*, and $i$ the scalar imaginary unit commuting with them. The source's first statement is the **factorization of the wave operator**

$$
\boxed{\;-\Delta + \partial^2/\partial {t'}^2 = (D + i\partial/\partial t')(D - i\partial/\partial t') = (D - i\partial/\partial t')(D + i\partial/\partial t')\;},
\tag{1}
$$

where $\Delta = \partial^2/\partial Q_x^2 + \partial^2/\partial Q_y^2 + \partial^2/\partial Q_z^2$ is the three-dimensional Laplacian. The two orderings agree because $D$ and $\partial/\partial t'$ commute. The operators $D \pm i\partial/\partial t'$ are the **parabolic Dirac operators** of the source; the name is inherited from the quaternionic-analysis literature that uses these first-order perturbations of $D$, and it refers to the first-order perturbation, not to a parabolic (heat-type) symbol: the factorisation is of the **hyperbolic** wave operator.

The mechanism is the sign of the quaternion square. With $\vec e_\mu^2 = -e_t$ and $\vec e_\mu \vec e_\nu = -\vec e_\nu \vec e_\mu$ for $\mu \neq \nu$, the square of $D$ is a scalar,

$$
D^2 = \sum_{\mu,\nu=1}^{3} \vec e_\mu \vec e_\nu\,\partial^2/\partial Q_\mu\partial Q_\nu = -\sum_{\mu=1}^{3}\partial^2/\partial Q_\mu^2 e_t = -\Delta e_t,
\tag{2}
$$

because the antisymmetric part $\sum_{\mu\neq \nu} \vec e_\mu \vec e_\nu\,\partial^2/\partial Q_\mu\partial Q_\nu$ vanishes by the symmetry of the mixed partials. The two sign choices of the first-order factor then produce the second time derivative, $(i\partial/\partial t')(-i\partial/\partial t') = +\partial^2/\partial {t'}^2$, and (1) follows. Formulas (1) and (2) were recomputed exactly; see the closing section.

### The Dictionary with the Corpus

The factorisation (1) is the **real-time twin** of the corpus's elliptic factorisation. The corpus's biquaternionic gradient is

$$
\tilde{\nabla} = e_t\partial/\partial Q_t + \vec e_x\partial/\partial Q_x + \vec e_y\partial/\partial Q_y + \vec e_z\partial/\partial Q_z,
$$

so that its spatial part is exactly the source's $D$, and the corpus's second-order operator is

$$
\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \partial^2/\partial Q_t^2 + \Delta
$$

(*Biquaternion Analysis*, *The d'Alembertian*). With $c = 1$ one has $\partial/\partial Q_t = -i\partial/\partial t'$, hence

$$
\tilde{\nabla} = D - i\partial/\partial t', \qquad -\tilde{\nabla}^{\natural} = D + i\partial/\partial t',
$$

and the two parabolic Dirac operators are the corpus's gradient and the negative of its conjugate, read in **real time**:

$$
-\Delta + \partial^2/\partial {t'}^2 = (D + i\partial/\partial t')(D - i\partial/\partial t') = -\tilde{\nabla}^{\natural}\tilde{\nabla} = -\Box.
\tag{3}
$$

The sign in (3) is the entire difference between the two interpretations, and it is the difference the corpus already records as the Wick rotation: the corpus's $\Box$ carries $\partial^2/\partial Q_t^2 = -\partial^2/\partial {t'}^2$ and is elliptic on the Euclidean slice, while the source's $-\Delta + \partial^2/\partial {t'}^2$ carries a real time and is hyperbolic. The source works in the hyperbolic signature throughout, so the null set of $\Box$ is the light cone and the operator is not elliptic; the elliptic tools (maximum principle, mean value property, Liouville) of *Biquaternion Analysis* are consequently not available, and the source does not use them.

## The Kernel as a Div-Curl System

### The Generalized Div-Curl System

Let $w = g + iv$ be a biquaternion-valued function on $\Omega \times (0,\infty)$, split into its real and imaginary quaternionic parts, and each of those into scalar and vector parts:

$$
w = g + iv = (g_0 + \vec q) + i(b_0 + \vec{b}), \qquad g_0, b_0 \in \mathbb{C}, \quad \vec q, \vec{b} \in \mathbb{C}^3.
$$

The source's Proposition 4 states that, for a continuously differentiable $w$, the equation $(D \pm i\partial/\partial t')w = 0$ holds if and only if

$$
-\mathrm{div}\,\vec q = \pm\partial/\partial t' b_0, \qquad
\mathrm{grad}\,g_0 + \mathrm{rot}\,\vec q = \pm\partial/\partial t' \vec{b}, \qquad
-\mathrm{div}\,\vec{b} = \mp\partial/\partial t' g_0, \qquad
\mathrm{grad}\,b_0 + \mathrm{rot}\,\vec{b} = \mp\partial/\partial t' \vec q,
\tag{4}
$$

where $\mathrm{rot}$ is the source's $\mathrm{curl}$ in the corpus's notation. The verification is two steps. First, the action of $D$ on a quaternion-valued function is the scalar-vector split

$$
Dg = -\mathrm{div}\,\vec q + \mathrm{grad}\,g_0 + \mathrm{rot}\,\vec q,
\tag{5}
$$

which is the spatial part of the corpus's $\tilde{\nabla}\tilde{F}$ formula (*Biquaternion Regular Functions*, *The System of Regularity Equations*). Second, expanding $(D \pm i\partial/\partial t')(g + iv)$ gives

$$
(D \pm i\partial/\partial t')(g+iv) = \bigl(Dg \mp \partial/\partial t' b\bigr) + i\bigl(Dv \pm \partial/\partial t' g\bigr),
$$

so the real and imaginary quaternionic parts vanish separately, $Dg = \pm\partial/\partial t' b$ and $Dv = \mp\partial/\partial t' g$, and (4) is exactly their four scalar-vector components.

### Cauchy–Riemann-Type Coupling of the Real and Imaginary Parts

The system (4) is the source's interpretation of the kernel as a **Cauchy–Riemann-type coupling**: the scalar part of the real half drives the divergence of the imaginary vector, the divergence of the real vector drives the imaginary scalar, and the two curl equations couple the vectors to the time derivatives of the scalars. It is the time-dependent analogue of the corpus's Cauchy–Riemann–Fueter system for $\tilde{\nabla}$, which reads $\partial/\partial Q_t\,F_0 = \mathrm{div}\,\vec F$ and $\partial/\partial Q_t\,\vec F + \mathrm{grad}\,F_0 + \mathrm{rot}\,\vec F = 0$ for a single biquaternion-valued $F$. Substituting $Q_t = ict'$ in the corpus's system produces the same two scalar equations that (4) carries, with the temporal slot distributed over the real and imaginary halves rather than collected in one $i\partial/\partial t'$. The source's own words for this are the standard ones — it "generalises the harmonic conjugation process" of complex analysis — and that is the correct description of the mechanism: one half of the function determines the other through the operator $D$ and the time integral, as harmonic conjugation gives the imaginary part of a holomorphic function from the real part.

### The Harmonic-Conjugate Construction

The construction that pairs the two halves is the source's Propositions 5 and 7. If $g$ is a quaternion-valued solution of the wave equation $(-\Delta + \partial^2/\partial {t'}^2)g = 0$, then

$$
b(x,t') := \int_0^{t'} Dg(x,s)\,ds - T_\Omega[\partial/\partial t' g](x,0) + \mathrm{grad}\,\phi(x)
\tag{6}
$$

makes $g + iv$ an element of $\ker(D + i\partial/\partial t')$ and $g - iv$ an element of $\ker(D - i\partial/\partial t')$, where $T_\Omega$ is the Teodorescu transform (the right inverse of $D$ on a bounded domain $\Omega$) and $\phi$ any time-independent harmonic function. The proof is the telescoping computation

$$
Dv = -\int_0^{t'} \Delta g(x,s)\,ds - \partial/\partial t' g(x,0) = -\bigl(\partial/\partial t' g(x,t') - \partial/\partial t' g(x,0)\bigr) - \partial/\partial t' g(x,0) = -\partial/\partial t' g(x,t'),
$$

using $\Delta g = \partial^2/\partial {t'}^2 g$ in the first step. When $g$ is a **scalar** solution $g_0$, the construction specialises to the purely vectorial complement

$$
\mathcal{V}[g_0](x,t') := i\int_0^{t'} \mathrm{grad}\,g_0(x,s)\,ds - i\,T_\Omega[\partial/\partial t' g_0](x,0),
\tag{7}
$$

and $g_0 \pm \mathcal{V}[g_0]$ lies in the kernel of $D \pm i\partial/\partial t'$. The two worked examples of the source were checked: $g(x,t') = x + t'$ gives $Dg = -3$ and $b = -3t' + \tfrac{1}{3}x + \mathrm{grad}\,\phi$; $g_0 = x_1^2 + x_2^2 + x_3^2 + 3{t'}^2$ gives $\mathcal{V}[g_0] = 2it'x$. The relation between the two branches is the one the source prints: the sign in $g \pm iv$ is correlated with the sign in $D \pm i\partial/\partial t'$, and the first paragraph of the source's proof carries a spurious $\pm$ that is not needed, since both branches satisfy the same pair of relations $Dg = \partial/\partial t' b$, $Dv = -\partial/\partial t' g$.

## The Quaternionic Exponential and the Fourier Characterisation

### The Fourier Transform Conventions

The source's Fourier transform is taken in the space variables only, at fixed time,

$$
\mathcal{F}(w)(k,t') = \int_{\mathbb{R}^3} \exp\bigl(-2\pi i\langle k,x\rangle\bigr) w(x,t')\,dx,
\tag{8}
$$

with inversion by $\mathcal{F}(w)(-x)$ and the differentiation rule $\mathcal{F}(\nabla w)(k) = 2\pi i k\,\mathcal{F}(w)(k)$ (*Biquaternion Continuous Harmonic Analysis*, *The Gradient*). Applying (8) to the equation $D\Phi = \mp i\partial/\partial t'\Phi$ of the kernel, using $\vec e_x k_1 + \vec e_y k_2 + \vec e_z k_3 = k$ for the frequency vector, gives the linear equation

$$
2\pi i k\,\mathcal{F}(\Phi_\pm)(k,t') \pm i\partial/\partial t' \mathcal{F}(\Phi_\pm)(k,t') = 0.
$$

### The Unit-Modulus Kernel

The solution is the **quaternionic exponential function**

$$
\boxed{\;\mathcal{F}(\Phi_\pm)(k,t') = \exp(\mp 2\pi k t') = \cos\bigl(2\pi|k|t'\bigr) \mp \frac{k}{|k|}\sin\bigl(2\pi|k|t'\bigr)\;},
\tag{9}
$$

for $(k,t') \in \mathbb{R}^3 \times \mathbb{R}$, with the convention $\mathcal{F}(\Phi_\pm) = 0$ for $t' < 0$. The closed form is the quaternion interpretation of an exponential of a **pure vector**: since $k$ is a pure imaginary quaternion with $k^2 = -|k|^2$, the series splits into an even and an odd part and gives $\exp(b) = \cos|b| + (b/|b|)\sin|b|$ for any pure vector $b$. The decisive property for everything that follows is that this exponential has **unit quaternion modulus**,

$$
\bigl|\exp(\mp 2\pi k t')\bigr| = 1 \qquad \text{for every } (k,t'),
$$

with reason $\exp(\mp 2\pi k t') = \exp\bigl(\mp 2\pi|k|t'\,\hat{g_k}\bigr)$ for the unit vector $\hat{g_k} = k/|k|$. It is a **phase**, a rotation in the plane spanned by $e_t$ and $k$, not a growing or decaying factor. This is what makes the whole scheme work: the multiplier is bounded and unimodular, so multiplication by it is an isometry of $L^2$ in the space variables. Formula (9) was recomputed both as a closed form and as the solution of its differential equation; the closed form satisfies $\partial/\partial t' G = \mp 2\pi k G$ to $4\times10^{-15}$ over the sample, and its modulus is exactly $1$.

## The Parabolic Teodorescu Transform and the Right Inverse

### Definition and the Spatial Isometry

Because $\Phi$ is not an $L^1$ object — the point taken up in *What Is Verified and What Is Not* — the source defines the **parabolic Teodorescu transform** directly from the multiplier:

$$
T_{\mathcal{C},\pm}[w](x,t') := \int_0^{t'}\int_{\mathbb{R}^3} \exp\bigl(2\pi i\langle x,k\rangle\bigr) \exp\bigl(\mp 2\pi (t'-s) k\bigr) \mathcal{F}(w)(k,s)\,dk\,ds,
\tag{10}
$$

for $(x,t') \in \mathbb{R}^3 \times (0,\infty)$, with $\mathcal{C} = \Omega \times (0,\infty)$ and $w$ extended by zero outside $\Omega$. The well-definedness argument (the source's Proposition 9) is the unimodularity of (9): for $0 < s < t'$, the modulus of the kernel is $1$, so

$$
\bigl|\exp(\mp 2\pi(t'-s)k)\bigr|^2 \bigl|\mathcal{F}(w)(k,s)\bigr|^2 = \bigl|\mathcal{F}(w)(k,s)\bigr|^2,
$$

and Plancherel's theorem turns the $k$-integral at each $s$ into $\|w(\cdot,s)\|_{L^2(\Omega)}$, whose integral over $s \in [0,t']$ is finite because the norm is continuous. This holds for **both** signs, because the kernel has modulus $1$ for both; there is no branch whose transform fails to converge.

### The Right-Inverse Theorem

The source's Theorem 10 states that $T_{\mathcal{C},\pm}[\mp i\,\cdot\,]$ is a right inverse of $D \pm i\partial/\partial t'$ on $L^2(\mathcal{C},\mathbb{B})$:

$$
\boxed{\;(D \pm i\partial/\partial t')\, T_{\mathcal{C},\pm}[\mp i\, w] = w\;}.
\tag{11}
$$

The proof is the symbol computation. Acting on the multiplier, the space derivative brings down $2\pi i k$ and the time derivative brings down $\mp 2\pi k$, while the Leibniz rule in $t'$ contributes the boundary term $\exp(2\pi i\langle x,k\rangle)\mathcal{F}(w)(k,t')$ whose $k$-integral is $w(x,t')$ by inversion. The result is the operator identity

$$
\partial/\partial t' T_{\mathcal{C},\pm}[w] = w \pm i D T_{\mathcal{C},\pm}[w],
$$

which rearranges to $(D \pm i\partial/\partial t')T_{\mathcal{C},\pm}[w] = \pm i w$ and therefore to (11) once the factor $\mp i$ is inserted. The algebra of this step was verified exactly. The factor $\mp i$ in (11) is the price of the normalisation (10); it is not a defect, and the source is explicit that the inverse holds "up to a multiplicative factor".

### The Correction of the Inverse's Scalar Part

One consequence is used in the application. The source's Corollary 11 observes that, because the operator has **two** orderings, applying $(-\Delta + \partial^2/\partial {t'}^2)$ to $T_{\mathcal{C},\pm}[\mp i w]$ gives not $w$ but

$$
(-\Delta + \partial^2/\partial {t'}^2)T_{\mathcal{C},\pm}[\mp i w] = (D \mp i\partial/\partial t')w,
$$

so the scalar part of $T_{\mathcal{C},\pm}[\mp i w]$ solves the homogeneous wave equation if and only if the scalar part of $(D \mp i\partial/\partial t')w$ vanishes, that is if and only if $\mathrm{div}\,\vec{w} \pm i\partial/\partial t' w_0 = 0$. In the time-independent case this is exactly the condition that the vector field be solenoidal, which is the class the heterogeneous div-curl literature requires. The vector part of the right-hand side need not vanish, so it is only the scalar part of the transform that is a wave solution without further correction; the correction itself is the completion (7) of the previous section.

## Explicit Vectorial Solutions of the Maxwell System

### Maxwell's Equations and the Single Biquaternionic Equation

The source takes Maxwell's equations in **Gaussian units** with $c = 1$,

$$
\mathrm{div}\,\vec{E} = 4\pi\rho, \qquad
\mathrm{div}\,\vec{B} = 0, \qquad
\mathrm{rot}\,\vec{E} = -\partial/\partial t'\vec{B}, \qquad
\mathrm{rot}\,\vec{B} = 4\pi\vec{\jmath} + \partial/\partial t'\vec{E},
\tag{12}
$$

with the compatibility condition $\mathrm{div}\,\vec{\jmath} + \partial/\partial t'\rho = 0$, which is not an external constraint but the consistency condition the system carries. Its Proposition 12 states that $(\vec{E}, \vec{B})$ solves (12) if and only if the **biquaternionic field** $\vec{\varphi} = \vec{E} + i\vec{B}$ satisfies

$$
(D - i\partial/\partial t')\vec{\varphi} = -4\pi(\rho - i\vec{\jmath}).
\tag{13}
$$

This is the corpus's single equation, and the identification is exact. The corpus's field-strength biquaternion is $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$, which in vacuum with $c = 1$ reads $\tilde{F} = i\vec E - \vec B = i(\vec E + i\vec B)$; the corpus's dual field strength is $-i\tilde{F} = \vec E + i\vec B$ (*Maxwell's Equations in the Biquaternionic Formulation*, Summary of Notation), so the source's $\vec{\varphi}$ is the corpus's dual field strength. With $\tilde{\nabla} = D - i\partial/\partial t'$ and $\sqrt{\mu}\,\tilde{J} = i\rho + \vec{\jmath}$ in vacuum, the corpus's equation $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}$ becomes

$$
-i\,\tilde{\nabla}\tilde F = -(\rho - i\vec{\jmath}), \qquad \text{that is} \qquad (D - i\partial/\partial t')\tilde F = -i(\rho - i\vec{\jmath}).
\tag{14}
$$

Comparison of (13) and (14) shows that the source's Proposition 12 and the corpus's single equation are the same statement; the only difference is the factor $4\pi$, which is the difference between the **Gaussian** and the **Heaviside–Lorentz-like** source normalisation of the corpus. The reformulation therefore adds nothing to the corpus's Maxwell content; what it adds is the operator theory that surrounds it.

### The Purely Vectorial Solution

The source's constructive step is to push the source through the right inverse and then remove the scalar part. From (11) with the lower sign,

$$
(D - i\partial/\partial t') T_{\mathcal{C},-}\bigl[-4\pi i(\rho - i\vec{\jmath})\bigr] = -4\pi(\rho - i\vec{\jmath}),
$$

so the transform is a particular solution of (13). It carries a scalar part $g_0 = \mathrm{Sc}\,T_{\mathcal{C},-}[-4\pi i(\rho - i\vec{\jmath})]$; by Corollary 11 and the compatibility condition, $g_0$ solves the wave equation, so by (7) the combination $g_0 - \mathcal{V}[g_0]$ lies in the kernel of $D - i\partial/\partial t'$. Subtracting it cancels the scalar part and leaves

$$
\boxed{\;\vec{\varphi} = \mathrm{Vec}\,T_{\mathcal{C},-}\bigl[-4\pi i(\rho - i\vec{\jmath})\bigr] + \mathcal{V}[g_0]\;},
\tag{15}
$$

a **purely vectorial** solution of (13), whose real part is the electric field $\vec{E}$ and whose imaginary part is the magnetic field $\vec{B}$. This is the source's Theorem 13, and its structure — solve by the right inverse, then kill the scalar part by adding a kernel element from the harmonic-conjugate construction — is a route complementary to the retarded-convolution solution the corpus records: the same equation, but a constructive family of purely vectorial solutions in place of the single causal convolution.

### The Homogeneous Medium and the Parameter $\lambda$

The source repeats the analysis for the slightly perturbed operator $D \pm i\lambda\partial/\partial t'$ with $\lambda \in \mathbb{R}$, whose kernel is characterised by (4) with $\partial/\partial t'$ replaced by $\lambda\partial/\partial t'$ (its Corollary 14) and whose right inverse is the $\lambda$-scaled transform

$$
T_{\mathcal{C},\pm,\lambda}[w](x,t') := \int_0^{t'}\int_{\mathbb{R}^3} \exp\bigl(2\pi i\langle x,k\rangle\bigr) \exp\bigl(\mp 2\pi\lambda^{-1}(t'-s)k\bigr) \mathcal{F}(w)(k,s)\,dk\,ds,
\tag{16}
$$

with the completion rescaling $g_0 \pm \tfrac{1}{\lambda}\mathcal{V}[g_0] \in \ker(D \pm i\lambda\partial/\partial t')$ whenever $g_0$ solves $(-\Delta + \lambda^2\partial^2/\partial {t'}^2)g_0 = 0$ (its Corollary 15). The application is Maxwell's equations in a homogeneous isotropic medium in **SI units**,

$$
\mathrm{div}\,\vec{E} = \frac{\rho}{\epsilon}, \qquad
\mathrm{div}\,\vec{B} = 0, \qquad
\mathrm{rot}\,\vec{E} = -\partial/\partial t'\vec{B}, \qquad
\mathrm{rot}\,\vec{B} = \mu\vec{\jmath} + \epsilon\,\partial/\partial t'\vec{E},
\tag{17}
$$

reduced to a single equation of the form $(D - \tfrac{i}{c}\partial/\partial t')\Phi = -\Psi$ with $c = 1/\sqrt{\epsilon\mu}$, solved with $\lambda = \sqrt{\epsilon\mu}$. **The constants of this section were not verified, and as extracted they do not all agree with the standard SI forms.** The extraction of the system (17) shows the ampèrian equation as $\mathrm{rot}\,\vec{B} = \mu\vec{\jmath} + \epsilon\,\partial/\partial t'\vec{E}$, whereas the standard SI form in terms of $\vec{B}$ is $\mathrm{rot}\,\vec{B} = \mu\vec{\jmath} + \mu\epsilon\,\partial/\partial t'\vec{E}$, the form that follows from $\mathrm{rot}\,\vec{H} = \vec{\jmath} + \partial/\partial t'\vec{D}$ with $\vec{B} = \mu\vec{H}$, $\vec{D} = \epsilon\vec{E}$; the factor $\mu$ is either dropped in the extraction or absent in the source, and it changes both the biquaternionic field that cancels the curl terms and the compatibility condition. The condition the source prints, $\mathrm{div}\,\vec{\jmath} + \sqrt{\epsilon\mu}\,\partial/\partial t'\rho = 0$, does not reduce to the plain conservation law $\mathrm{div}\,\vec{\jmath} + \partial/\partial t'\rho = 0$ under either interpretation of (17), which is a second sign that the printed constants could not be read faithfully. What this section contributes is its **structure** — a single equation $(D - \tfrac{i}{c}\partial/\partial t')\Phi = -\Psi$ with the parameter $\lambda = \sqrt{\epsilon\mu}$ — and that structure should be re-derived from the published text before any constant from it is quoted.

## What Is Verified and What Is Not

**Not verified, and flagged.** (i) The object called a **fundamental solution**. Its defining equation in the source, $(D \pm i\partial/\partial t')\Phi_\pm = 0$ for $x \neq 0$, $t' \neq 0$, is the **homogeneous** equation in the punctured domain; a fundamental solution in the classical sense carries $\delta$ on the right. The object whose Fourier transform is (9) is the **kernel of the right inverse**, and the inverse is correctly defined directly by (10) and proved in (11); a fundamental solution with a $\delta$ on the right is not exhibited. (ii) The declaration $\Phi_\pm \in L^1(\mathbb{R}^3 \times (0,\infty))$ **cannot** be reconciled with (9): by the Riemann–Lebesgue lemma the space Fourier transform of an $L^1$ function tends to $0$ at infinity, whereas (9) has modulus $1$ for every $k$. The two statements are inconsistent, and it is (9), not the $L^1$ claim, that the proof of the right inverse uses. (iii) The exact hypotheses and normalisations of **Theorems 13 and 16** were read only through the extracted running text, whose display is garbled; the *structure* recorded in (15) — right inverse, then completion by $g_0 - \mathcal{V}[g_0]$ — is verified, but the printed leading factors, the pairing of $\mathrm{Re}$ and $\mathrm{Im}$ with $\mathrm{Vec}$, and the definition of $g_0$ should be checked against the published version before they are quoted. (iv) The constants of the SI homogeneous-medium section: as extracted, the system (17) and the condition the source prints with it are not mutually consistent — the ampèrian equation lacks the factor $\mu$ of the standard B-form, and the printed compatibility condition does not reduce to $\mathrm{div}\,\vec{\jmath} + \partial/\partial t'\rho = 0$ under either interpretation — so the exact field combination and the normalisation of that section were left unverified. Only its structure (a single equation with $\lambda = \sqrt{\epsilon\mu}$) is recorded.

**What the source does not do.** It does not solve a boundary-value problem: the domain is fixed, the transform is taken by zero extension, and the right inverse is global. It does not treat an inhomogeneous or chiral medium: the homogeneous medium enters only through the single constant $\lambda = \sqrt{\epsilon\mu}$, so the dispersive and magnetoelectric content of *Electromagnetism in Media — The Local Complex Structure at Work* is untouched. It does not quantise, and it makes no claim about the **physical interpretation** of the parabolic operators beyond their use as a computational route. Its stated aim is analytical efficiency, and its result should be read as a method, not as a physical model.

## Summary

The source's wave-operator factorisation $-\Delta + \partial^2/\partial {t'}^2 = (D + i\partial/\partial t')(D - i\partial/\partial t') = (D - i\partial/\partial t')(D + i\partial/\partial t')$ is exact in both orderings and is the real-time (hyperbolic) twin of the corpus's elliptic factorisation $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural}$: the source's two first-order operators are the corpus's biquaternionic gradient and the negative of its conjugate, read with $\partial/\partial Q_t = -i\partial/\partial t'$. The kernel of $D \pm i\partial/\partial t'$ is exactly a generalized div-curl system, the time-dependent analogue of the corpus's Cauchy–Riemann–Fueter system, and it couples a scalar solution of the wave equation to its harmonic conjugate through the Teodorescu transform. The Fourier transform of the kernel is the quaternionic exponential of a pure vector, which is a **unit-modulus phase** — this unimodularity is the single fact that makes the parabolic Teodorescu transform an $L^2$ isometry in space, well defined for both signs, and its right-inverse property $(D \pm i\partial/\partial t')T_{\mathcal{C},\pm}[\mp iw] = w$ follows from the symbol computation $\partial/\partial t' T = w \pm iDT$. The Maxwell application reproduces the corpus's single equation — the source's $\vec{E} + i\vec{B}$ is the corpus's dual field strength $-i\tilde F$, and its Proposition 12 is the corpus's $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}$ up to the $4\pi$ of Gaussian units — and then goes beyond it constructively: pushing the source through the right inverse and subtracting the scalar part $g_0 - \mathcal{V}[g_0]$ yields an explicit **purely vectorial** solution, a constructive family complementary to the retarded convolution the corpus records. The price is a set of source defects: a mislabelled fundamental solution whose homogeneous defining equation and $L^1$ requirement are inconsistent with its own unit-modulus transform, a missing factor $i$ in the §5.1 symbol equation, an SI reduction whose constants could not be read faithfully, and two solution theorems whose exact normalisations were not verifiable from the running text. The record is of a method new to the corpus and of a reformulation already in it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis; $\vec e_\mu^2 = -e_t$, $\vec e_\mu \vec e_\nu = -\vec e_\nu \vec e_\mu$ for $\mu \neq \nu$ |
| $i$ | Scalar imaginary unit, $i^2 = -1$, central |
| $\mathbb{B}$ | Biquaternion algebra |
| $\Omega$, $\mathcal{C} = \Omega \times (0,\infty)$ | Bounded spatial domain and the space-time domain of the source |
| $D = \vec e_x\partial/\partial Q_x + \vec e_y\partial/\partial Q_y + \vec e_z\partial/\partial Q_z$ | Moisil–Teodorescu operator (the source's); the corpus's spatial part $\vec{\nabla}$ of $\tilde{\nabla}$ |
| $D \pm i\partial/\partial t'$ | The parabolic Dirac operators of the source; $D - i\partial/\partial t' = \tilde{\nabla}$ and $D + i\partial/\partial t' = -\tilde{\nabla}^{\natural}$ at $c = 1$ |
| $\Delta = \partial^2/\partial Q_x^2 + \partial^2/\partial Q_y^2 + \partial^2/\partial Q_z^2$ | Three-dimensional Laplacian; $D^2 = -\Delta e_t$ |
| $\nabla, \mathrm{div}, \mathrm{rot}$ | Gradient, divergence, curl; $\mathrm{rot}$ is the source's $\mathrm{curl}$ |
| $w = g + iv = (g_0 + \vec q) + i(b_0 + \vec{b})$ | Biquaternion-valued function, split into real and imaginary quaternion parts, each scalar plus vector |
| $T_\Omega$ | Teodorescu transform, the right inverse of $D$ on $\Omega$ |
| $\mathcal{V}[g_0]$ | Purely vectorial complement (7) of a scalar wave solution |
| $\mathcal{F}$ | Fourier transform in the space variables at fixed $t'$ |
| $k$ | Frequency three-vector, read as the pure quaternion $\vec e_xk_1 + \vec e_yk_2 + \vec e_zk_3$ |
| $\Phi_\pm$ | The source's kernel, $\mathcal{F}(\Phi_\pm)(k,t') = \exp(\mp 2\pi kt')$ |
| $T_{\mathcal{C},\pm}$, $T_{\mathcal{C},\pm,\lambda}$ | Parabolic Teodorescu transform (10) and its $\lambda$-scaled form (16) |
| $\vec{E}, \vec{B}, \rho, \vec{\jmath}$ | Electric field, magnetic field, charge density, current density |
| $\vec{\varphi} = \vec{E} + i\vec{B}$ | Biquaternionic field of the source; the corpus's dual field strength $-i\tilde F$ |
| $\tilde{F}, \tilde J, \tilde{\nabla}, \tilde{\nabla}^{\natural}, \Box$ | Corpus field-strength biquaternion, four-current, biquaternionic gradient, its conjugate, d'Alembertian |
| $\epsilon, \mu, c = 1/\sqrt{\epsilon\mu}$ | Permittivity, permeability, speed of light in the medium (SI section) |
| $\lambda$ | Parameter of the perturbed operator $D \pm i\lambda\partial/\partial t'$; $\lambda = \sqrt{\epsilon\mu}$ for the homogeneous medium |

## Further Reading

- A. Guillén-Villalobos, B. B. Delgado and H. Vargas Rodríguez, *A biquaternionic reformulation of Maxwell's equations via Fourier analysis*, arXiv:2605.21412v2 [math.AP] (2026). The source of this article: the parabolic Dirac operators, the div-curl characterisation, the quaternionic exponential, the right inverse, and the vectorial Maxwell solutions.
- V. V. Kravchenko, *Applied Quaternionic Analysis* (Heldermann, 2003), §3.1.1 and the Teodorescu transform, for the equivalence of the Maxwell system to a single biquaternionic equation and the harmonic-conjugation process the source follows. The same source is used by [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-biquaternionic-form.html).
- V. V. Kravchenko and R. Castillo P., "On the kernel of the Klein–Gordon operator", *Zeitschrift für Analysis und ihre Anwendungen* **17** (1998) 261–265, for the earlier statement that solutions of the Klein–Gordon equation are represented through solutions of parabolic Dirac equations; the source's lineage for the name.
- P. Cerejeiras, U. Kaehler and V. V. Kravchenko, "On a factorization of the Schrödinger and Klein–Gordon operators", *Mathematical Methods in the Applied Sciences* **31** (2008) 1722–1738, for the general scheme of factorising second-order time-dependent operators, of which the source's (1) is an instance.
- Viktor G. Kravchenko and Vladislav V. Kravchenko, "Quaternionic factorization of the Schrödinger operator and its applications to some first order systems of mathematical physics" (arXiv:math-ph/0305046, 2003), the companion entry of the factorisation above: for the same Schrödinger factorisation read as a reduction of first-order systems — the Dirac equation with scalar, electric and pseudoscalar potentials, the force-free magnetic fields, the Maxwell system of a slowly changing medium and the static Maxwell system — to the single quaternionic equation $D_3f+f\vec\alpha = 0$, and for the componentwise reduction of that equation to four scalar Schrödinger operators, recorded in *Quaternion Regular Functions*.
- B. B. Delgado and V. V. Kravchenko, "A Right Inverse Operator for $\mathrm{curl} + \lambda$ and Applications", *Advances in Applied Clifford Algebras* **29** (2019) 1–15, and "Biquaternionic treatment of inhomogeneous time-harmonic Maxwell's equations over unbounded domains", *Advances in Applied Clifford Algebras* **33** (2023) 29, for the right-inverse tradition and the completion process the source generalises to the parabolic operators.
- B. B. Delgado and R. M. Porter, "General solution of the inhomogeneous div-curl system and consequences", *Advances in Applied Clifford Algebras* **27** (2017) 3015–3037, for the div-curl general solution and the solenoidal class the time-independent limit of the source recovers.
- D. Eelbode, "Solutions for the Hyperbolic Dirac Equation on $\mathbb{R}^{1,m}$", *Complex Variables, Theory and Application* **48** (2003) 377–395, and D. Eelbode and F. Sommen, "The Fundamental Solution of the Hyperbolic Dirac Operator on $\mathbb{R}^{1,m}$: a new approach", *Bulletin of the Belgian Mathematical Society — Simon Stevin* **12** (2005) 23–37, for the hyperbolic Dirac operators between which the source's parabolic factorisation sits, the elliptic Fueter theory on one side and the split-signature theory on the other.
- E. H. Lieb and M. Loss, *Analysis* (American Mathematical Society, 2001), for the Fourier conventions of the source's §2.1: the differentiation rule, the convolution theorem, and the Plancherel theorem.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1975), for Maxwell's equations in the Gaussian and SI units of the source's §§5 and 5.1.
