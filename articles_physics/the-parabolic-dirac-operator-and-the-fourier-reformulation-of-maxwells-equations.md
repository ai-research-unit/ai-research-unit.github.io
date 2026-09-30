# __The Parabolic Dirac Operator and the Fourier Reformulation of Maxwell's Equations__

## Introduction

The series already carries two routes into Maxwell's equations quaternionically: *Maxwell's Equations in the Biquaternionic Formulation* reduces the full time-dependent system to the single equation $\tilde{\nabla}\tilde{F} = -\tilde{R}$, and *The Time-Harmonic Maxwell Operator and the Quaternionic Cauchy Integral* diagonalises the stationary system of a lossy isotropic medium into two conjugate Cauchy–Riemann equations. Both are algebraic or elliptic. The third route recorded here is different in kind: it factors the **wave operator itself** into two first-order operators and inverts them **by Fourier analysis**, and it is the object of the source paper of this article.

The source is A. Guillén-Villalobos, B. B. Delgado and H. Vargas Rodríguez, *A biquaternionic reformulation of Maxwell's equations via Fourier analysis*, arXiv:2605.21412v2 [math.AP] (22 May 2026). It studies the **parabolic Dirac operators** $D \pm i\partial_t$, where $D$ is the Moisil–Teodorescu operator and $i$ the scalar imaginary unit; characterises the kernel of $D \pm i\partial_t$ by a **generalized div-curl system** and by **Cauchy–Riemann-type relations** between the real and the imaginary parts of a biquaternion-valued function; computes the Fourier transform of a kernel of the operator, which turns out to be the **quaternionic exponential function** of unit modulus; constructs an explicit **right inverse**; and applies the inverse to the time-dependent Maxwell system, obtaining **purely vectorial** solutions. The paper follows the monograph V. V. Kravchenko, *Applied Quaternionic Analysis* (2003), to which the corpus's biquaternion Maxwell article also refers.

The article is written to separate three things. First, **what the corpus already has**: the single biquaternionic Maxwell equation $\tilde{\nabla}\tilde{F} = -\tilde{R}$, the field-strength biquaternion and its A-field form $\mathcal{A} = -i\tilde{F}$, the second-order factorisation $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$, and the elliptic Cauchy kernel. The paper's Maxwell statement (its Proposition 12) is the corpus's single equation written in real time, in Gaussian units, for the A-field; the reformulation itself is therefore not new to the corpus. Second, **what is new to the corpus**: the real-time first-order factorisation of the wave operator (both orderings), the time-dependent div-curl characterisation of the kernel, the description of the inverse's symbol as a unit quaternionic exponential, and the operator right inverse with its explicit vectorial solutions. Third, **what the source does not settle**: the naming and existence of its "fundamental solution", a homogeneous-medium reduction whose printed constants could not be read faithfully, and the exact hypotheses of its two solution theorems.

The plan is the operator, then its kernel, then its Fourier symbol, then its inverse, then the application. The section *What Is Verified and What Is Not* collects the recomputations and the defects.

## The Parabolic Dirac Operators

### The Factorization of the Wave Operator

The **Moisil–Teodorescu operator** is the three-dimensional Dirac-type operator

$$
D = e_1\partial_x + e_2\partial_y + e_3\partial_z = \sum_{k=1}^{3} e_k\partial_k,
$$

with $e_1, e_2, e_3$ the quaternion units of the algebra $\mathbb{B}$ of *Conventions in the Biquaternion Universe*, and $i$ the scalar imaginary unit commuting with them. The source's first statement is the **factorization of the wave operator**

$$
-\Delta + \partial_t^2 = (D + i\partial_t)(D - i\partial_t) = (D - i\partial_t)(D + i\partial_t),
\tag{1}
$$

where $\Delta = \partial_x^2 + \partial_y^2 + \partial_z^2$ is the three-dimensional Laplacian. The two orderings agree because $D$ and $\partial_t$ commute. The operators $D \pm i\partial_t$ are the **parabolic Dirac operators** of the source; the name is inherited from the quaternionic-analysis literature that uses these first-order perturbations of $D$, and it refers to the first-order perturbation, not to a parabolic (heat-type) symbol: the factorisation is of the **hyperbolic** wave operator.

The mechanism is the sign of the quaternion square. With $e_k^2 = -e_0$ and $e_je_k = -e_ke_j$ for $j \neq k$, the square of $D$ is a scalar,

$$
D^2 = \sum_{j,k=1}^{3} e_je_k\partial_j\partial_k = -\sum_{k=1}^{3}\partial_k^2 e_0 = -\Delta e_0,
\tag{2}
$$

because the antisymmetric part $\sum_{j\neq k} e_je_k\partial_j\partial_k$ vanishes by the symmetry of the mixed partials. The two sign choices of the first-order factor then produce the second time derivative, $(i\partial_t)(-i\partial_t) = +\partial_t^2$, and (1) follows. Formulas (1) and (2) were recomputed exactly; see the closing section.

### The Dictionary with the Corpus

The factorisation (1) is the **real-time twin** of the corpus's elliptic factorisation. The corpus's biquaternionic gradient is

$$
\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z,
$$

so that its spatial part is exactly the source's $D$, and the corpus's second-order operator is

$$
\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \partial_{ict}^2 + \Delta
$$

(*Biquaternion Analysis*, *The d'Alembertian*). With $c = 1$ one has $\partial_{ict} = -i\partial_t$, hence

$$
\tilde{\nabla} = D - i\partial_t, \qquad -\bar{\tilde{\nabla}} = D + i\partial_t,
$$

and the two parabolic Dirac operators are the corpus's gradient and the negative of its conjugate, read in **real time**:

$$
-\Delta + \partial_t^2 = (D + i\partial_t)(D - i\partial_t) = -\bar{\tilde{\nabla}}\tilde{\nabla} = -\Box.
\tag{3}
$$

The sign in (3) is the entire difference between the two readings, and it is the difference the corpus already records as the Wick rotation: the corpus's $\Box$ carries $\partial_{ict}^2 = -\partial_t^2$ and is elliptic on the Euclidean slice, while the source's $-\Delta + \partial_t^2$ carries a real time and is hyperbolic. The source works in the hyperbolic signature throughout, so the null set of $\Box$ is the light cone and the operator is not elliptic; the elliptic tools (maximum principle, mean value property, Liouville) of *Biquaternion Analysis* are consequently not available, and the source does not use them.

## The Kernel as a Div-Curl System

### The Generalized Div-Curl System

Let $w = u + iv$ be a biquaternion-valued function on $\Omega \times (0,\infty)$, split into its real and imaginary quaternionic parts, and each of those into scalar and vector parts:

$$
w = u + iv = (u_0 + \vec{u}) + i(v_0 + \vec{v}), \qquad u_0, v_0 \in \mathbb{C}, \quad \vec{u}, \vec{v} \in \mathbb{C}^3.
$$

The source's Proposition 4 states that, for a continuously differentiable $w$, the equation $(D \pm i\partial_t)w = 0$ holds if and only if

$$
-\mathrm{div}\,\vec{u} = \pm\partial_t v_0, \qquad
\mathrm{grad}\,u_0 + \mathrm{rot}\,\vec{u} = \pm\partial_t \vec{v}, \qquad
-\mathrm{div}\,\vec{v} = \mp\partial_t u_0, \qquad
\mathrm{grad}\,v_0 + \mathrm{rot}\,\vec{v} = \mp\partial_t \vec{u},
\tag{4}
$$

where $\mathrm{rot}$ is the source's $\mathrm{curl}$ in the corpus's notation. The verification is two steps. First, the action of $D$ on a quaternion-valued function is the scalar-vector split

$$
Du = -\mathrm{div}\,\vec{u} + \mathrm{grad}\,u_0 + \mathrm{rot}\,\vec{u},
\tag{5}
$$

which is the spatial part of the corpus's $\tilde{\nabla}\tilde{F}$ formula (*Biquaternion Regular Functions*, *The System of Regularity Equations*). Second, expanding $(D \pm i\partial_t)(u + iv)$ gives

$$
(D \pm i\partial_t)(u+iv) = \bigl(Du \mp \partial_t v\bigr) + i\bigl(Dv \pm \partial_t u\bigr),
$$

so the real and imaginary quaternionic parts vanish separately, $Du = \pm\partial_t v$ and $Dv = \mp\partial_t u$, and (4) is exactly their four scalar-vector components. Both (5) and the split of (4) were recomputed exactly.

### Cauchy–Riemann-Type Coupling of the Real and Imaginary Parts

The system (4) is the source's reading of the kernel as a **Cauchy–Riemann-type coupling**: the scalar part of the real half drives the divergence of the imaginary vector, the divergence of the real vector drives the imaginary scalar, and the two curl equations couple the vectors to the time derivatives of the scalars. It is the time-dependent analogue of the corpus's Cauchy–Riemann–Fueter system for $\tilde{\nabla}$, which reads $\partial_{Q_0}F_0 = \mathrm{div}\,\mathbf{F}$ and $\partial_{Q_0}\mathbf{F} + \mathrm{grad}\,F_0 + \mathrm{rot}\,\mathbf{F} = 0$ for a single biquaternion-valued $F$. Substituting $Q_0 = ict$ in the corpus's system produces the same two scalar equations that (4) carries, with the temporal slot distributed over the real and imaginary halves rather than collected in one $i\partial_t$. The source's own words for this are the standard ones — it "generalises the harmonic conjugation process" of complex analysis — and that is the correct description of the mechanism: one half of the function determines the other through the operator $D$ and the time integral, as harmonic conjugation gives the imaginary part of a holomorphic function from the real part.

### The Harmonic-Conjugate Construction

The construction that pairs the two halves is the source's Propositions 5 and 7. If $u$ is a quaternion-valued solution of the wave equation $(-\Delta + \partial_t^2)u = 0$, then

$$
v(x,t) := \int_0^t Du(x,s)\,ds - T_\Omega[\partial_t u](x,0) + \mathrm{grad}\,\phi(x)
\tag{6}
$$

makes $u + iv$ an element of $\ker(D + i\partial_t)$ and $u - iv$ an element of $\ker(D - i\partial_t)$, where $T_\Omega$ is the Teodorescu transform (the right inverse of $D$ on a bounded domain $\Omega$) and $\phi$ any time-independent harmonic function. The proof is the telescoping computation

$$
Dv = -\int_0^t \Delta u(x,s)\,ds - \partial_t u(x,0) = -\bigl(\partial_t u(x,t) - \partial_t u(x,0)\bigr) - \partial_t u(x,0) = -\partial_t u(x,t),
$$

using $\Delta u = \partial_t^2 u$ in the first step. When $u$ is a **scalar** solution $u_0$, the construction specialises to the purely vectorial complement

$$
U[u_0](x,t) := i\int_0^t \mathrm{grad}\,u_0(x,s)\,ds - i\,T_\Omega[\partial_t u_0](x,0),
\tag{7}
$$

and $u_0 \pm U[u_0]$ lies in the kernel of $D \pm i\partial_t$. The two worked examples of the source were checked: $u(x,t) = x + t$ gives $Du = -3$ and $v = -3t + \tfrac{1}{3}x + \mathrm{grad}\,\phi$; $u_0 = x_1^2 + x_2^2 + x_3^2 + 3t^2$ gives $U[u_0] = 2itx$. The relation between the two branches is the one the source prints: the sign in $u \pm iv$ is correlated with the sign in $D \pm i\partial_t$, and the first paragraph of the source's proof carries a spurious $\pm$ that is not needed, since both branches satisfy the same pair of relations $Du = \partial_t v$, $Dv = -\partial_t u$.

## The Quaternionic Exponential and the Fourier Characterisation

### The Fourier Transform Conventions

The source's Fourier transform is taken in the space variables only, at fixed time,

$$
\mathcal{F}(w)(k,t) = \int_{\mathbb{R}^3} \exp\bigl(-2\pi i\langle k,x\rangle\bigr) w(x,t)\,dx,
\tag{8}
$$

with inversion by $\mathcal{F}(w)(-x)$ and the differentiation rule $\mathcal{F}(\nabla w)(k) = 2\pi i k\,\mathcal{F}(w)(k)$ (*Biquaternion Continuous Harmonic Analysis*, *The Gradient*). Applying (8) to the equation $D\Phi = \mp i\partial_t\Phi$ of the kernel, using $e_1 k_1 + e_2 k_2 + e_3 k_3 = k$ for the frequency vector, gives the linear equation

$$
2\pi i k\,\mathcal{F}(\Phi_\pm)(k,t) \pm i\partial_t \mathcal{F}(\Phi_\pm)(k,t) = 0.
$$

### The Unit-Modulus Kernel

The solution is the **quaternionic exponential function**

$$
\mathcal{F}(\Phi_\pm)(k,t) = \exp(\mp 2\pi k t) = \cos\bigl(2\pi|k|t\bigr) \mp \frac{k}{|k|}\sin\bigl(2\pi|k|t\bigr),
\tag{9}
$$

for $(k,t) \in \mathbb{R}^3 \times \mathbb{R}$, with the convention $\mathcal{F}(\Phi_\pm) = 0$ for $t < 0$. The closed form is the quaternion reading of an exponential of a **pure vector**: since $k$ is a pure imaginary quaternion with $k^2 = -|k|^2$, the series splits into an even and an odd part and gives $\exp(v) = \cos|v| + (v/|v|)\sin|v|$ for any pure vector $v$. The decisive property for everything that follows is that this exponential has **unit quaternion modulus**,

$$
\bigl|\exp(\mp 2\pi k t)\bigr| = 1 \qquad \text{for every } (k,t),
$$

with reason $\exp(\mp 2\pi k t) = \exp\bigl(\mp 2\pi|k|t\,\hat{k}\bigr)$ for the unit vector $\hat{k} = k/|k|$. It is a **phase**, a rotation in the plane spanned by $e_0$ and $k$, not a growing or decaying factor. This is what makes the whole scheme work: the multiplier is bounded and unimodular, so multiplication by it is an isometry of $L^2$ in the space variables. Formula (9) was recomputed both as a closed form and as the solution of its differential equation; the closed form satisfies $\partial_t G = \mp 2\pi k G$ to $4\times10^{-15}$ over the sample, and its modulus is exactly $1$.

## The Parabolic Teodorescu Transform and the Right Inverse

### Definition and the Spatial Isometry

Because $\Phi$ is not an $L^1$ object — the point taken up in *What Is Verified and What Is Not* — the source defines the **parabolic Teodorescu transform** directly from the multiplier:

$$
T_{\mathcal{C},\pm}[w](x,t) := \int_0^t\int_{\mathbb{R}^3} \exp\bigl(2\pi i\langle x,k\rangle\bigr) \exp\bigl(\mp 2\pi (t-s) k\bigr) \mathcal{F}(w)(k,s)\,dk\,ds,
\tag{10}
$$

for $(x,t) \in \mathbb{R}^3 \times (0,\infty)$, with $\mathcal{C} = \Omega \times (0,\infty)$ and $w$ extended by zero outside $\Omega$. The well-definedness argument (the source's Proposition 9) is the unimodularity of (9): for $0 < s < t$, the modulus of the kernel is $1$, so

$$
\bigl|\exp(\mp 2\pi(t-s)k)\bigr|^2 \bigl|\mathcal{F}(w)(k,s)\bigr|^2 = \bigl|\mathcal{F}(w)(k,s)\bigr|^2,
$$

and Plancherel's theorem turns the $k$-integral at each $s$ into $\|w(\cdot,s)\|_{L^2(\Omega)}$, whose integral over $s \in [0,t]$ is finite because the norm is continuous. This holds for **both** signs, because the kernel has modulus $1$ for both; there is no branch whose transform fails to converge.

### The Right-Inverse Theorem

The source's Theorem 10 states that $T_{\mathcal{C},\pm}[\mp i\,\cdot\,]$ is a right inverse of $D \pm i\partial_t$ on $L^2(\mathcal{C},\mathbb{B})$:

$$
(D \pm i\partial_t)\, T_{\mathcal{C},\pm}[\mp i\, w] = w.
\tag{11}
$$

The proof is the symbol computation. Acting on the multiplier, the space derivative brings down $2\pi i k$ and the time derivative brings down $\mp 2\pi k$, while the Leibniz rule in $t$ contributes the boundary term $\exp(2\pi i\langle x,k\rangle)\mathcal{F}(w)(k,t)$ whose $k$-integral is $w(x,t)$ by inversion. The result is the operator identity

$$
\partial_t T_{\mathcal{C},\pm}[w] = w \pm i D T_{\mathcal{C},\pm}[w],
$$

which rearranges to $(D \pm i\partial_t)T_{\mathcal{C},\pm}[w] = \pm i w$ and therefore to (11) once the factor $\mp i$ is inserted. The algebra of this step was verified exactly. The factor $\mp i$ in (11) is the price of the normalisation (10); it is not a defect, and the source is explicit that the inverse holds "up to a multiplicative factor".

### The Correction of the Inverse's Scalar Part

One consequence is used in the application. The source's Corollary 11 observes that, because the operator has **two** orderings, applying $(-\Delta + \partial_t^2)$ to $T_{\mathcal{C},\pm}[\mp i w]$ gives not $w$ but

$$
(-\Delta + \partial_t^2)T_{\mathcal{C},\pm}[\mp i w] = (D \mp i\partial_t)w,
$$

so the scalar part of $T_{\mathcal{C},\pm}[\mp i w]$ solves the homogeneous wave equation if and only if the scalar part of $(D \mp i\partial_t)w$ vanishes, that is if and only if $\mathrm{div}\,\vec{w} \pm i\partial_t w_0 = 0$. In the time-independent case this is exactly the condition that the vector field be solenoidal, which is the class the heterogeneous div-curl literature requires. The vector part of the right-hand side need not vanish, so it is only the scalar part of the transform that is a wave solution without further correction; the correction itself is the completion (7) of the previous section.

## Explicit Vectorial Solutions of the Maxwell System

### Maxwell's Equations and the Single Biquaternionic Equation

The source takes Maxwell's equations in **Gaussian units** with $c = 1$,

$$
\mathrm{div}\,\vec{E} = 4\pi\rho, \qquad
\mathrm{div}\,\vec{B} = 0, \qquad
\mathrm{rot}\,\vec{E} = -\partial_t\vec{B}, \qquad
\mathrm{rot}\,\vec{B} = 4\pi\vec{\jmath} + \partial_t\vec{E},
\tag{12}
$$

with the compatibility condition $\mathrm{div}\,\vec{\jmath} + \partial_t\rho = 0$, which is not an external constraint but the consistency condition the system carries. Its Proposition 12 states that $(\vec{E}, \vec{B})$ solves (12) if and only if the **biquaternionic field** $\vec{\varphi} = \vec{E} + i\vec{B}$ satisfies

$$
(D - i\partial_t)\vec{\varphi} = -4\pi(\rho - i\vec{\jmath}).
\tag{13}
$$

This is the corpus's single equation, and the identification is exact. The corpus's field-strength biquaternion is $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$, which in vacuum with $c = 1$ reads $\tilde{F} = i\mathbf{E} - \mathbf{B} = i(\mathbf{E} + i\mathbf{B})$; the corpus's **A-field** is $\mathcal{A} = -i\tilde{F} = \mathbf{E} + i\mathbf{B}$ (*Maxwell's Equations in the Biquaternionic Formulation*, Summary of Notation), so the source's $\vec{\varphi}$ is the corpus's A-field. With $\tilde{\nabla} = D - i\partial_t$ and $\tilde{R} = i\rho + \vec{\jmath}$ in vacuum, the corpus's equation $\tilde{\nabla}\tilde{F} = -\tilde{R}$ becomes

$$
-i\,\tilde{\nabla}(i\mathcal{A}) = -(\rho - i\vec{\jmath}), \qquad \text{that is} \qquad (D - i\partial_t)\mathcal{A} = -\rho + i\vec{\jmath} = -(\rho - i\vec{\jmath}).
\tag{14}
$$

Comparison of (13) and (14) shows that the source's Proposition 12 and the corpus's single equation are the same statement; the only difference is the factor $4\pi$, which is the difference between the **Gaussian** and the **Heaviside–Lorentz-like** source normalisation of the corpus. The reformulation therefore adds nothing to the corpus's Maxwell content; what it adds is the operator theory that surrounds it. The equivalence (13) was verified exactly, component by component.

### The Purely Vectorial Solution

The source's constructive step is to push the source through the right inverse and then remove the scalar part. From (11) with the lower sign,

$$
(D - i\partial_t) T_{\mathcal{C},-}\bigl[-4\pi i(\rho - i\vec{\jmath})\bigr] = -4\pi(\rho - i\vec{\jmath}),
$$

so the transform is a particular solution of (13). It carries a scalar part $u_0 = \mathrm{Sc}\,T_{\mathcal{C},-}[-4\pi i(\rho - i\vec{\jmath})]$; by Corollary 11 and the compatibility condition, $u_0$ solves the wave equation, so by (7) the combination $u_0 - U[u_0]$ lies in the kernel of $D - i\partial_t$. Subtracting it cancels the scalar part and leaves

$$
\vec{\varphi} = \mathrm{Vec}\,T_{\mathcal{C},-}\bigl[-4\pi i(\rho - i\vec{\jmath})\bigr] + U[u_0],
\tag{15}
$$

a **purely vectorial** solution of (13), whose real part is the electric field $\vec{E}$ and whose imaginary part is the magnetic field $\vec{B}$. This is the source's Theorem 13, and its structure — solve by the right inverse, then kill the scalar part by adding a kernel element from the harmonic-conjugate construction — is a route complementary to the retarded-convolution solution the corpus records: the same equation, but a constructive family of purely vectorial solutions in place of the single causal convolution.

### The Homogeneous Medium and the Parameter $\lambda$

The source repeats the analysis for the slightly perturbed operator $D \pm i\lambda\partial_t$ with $\lambda \in \mathbb{R}$, whose kernel is characterised by (4) with $\partial_t$ replaced by $\lambda\partial_t$ (its Corollary 14) and whose right inverse is the $\lambda$-scaled transform

$$
T_{\mathcal{C},\pm,\lambda}[w](x,t) := \int_0^t\int_{\mathbb{R}^3} \exp\bigl(2\pi i\langle x,k\rangle\bigr) \exp\bigl(\mp 2\pi\lambda^{-1}(t-s)k\bigr) \mathcal{F}(w)(k,s)\,dk\,ds,
\tag{16}
$$

with the completion rescaling $u_0 \pm \tfrac{1}{\lambda}U[u_0] \in \ker(D \pm i\lambda\partial_t)$ whenever $u_0$ solves $(-\Delta + \lambda^2\partial_t^2)u_0 = 0$ (its Corollary 15). The application is Maxwell's equations in a homogeneous isotropic medium in **SI units**,

$$
\mathrm{div}\,\vec{E} = \frac{\rho}{\epsilon}, \qquad
\mathrm{div}\,\vec{B} = 0, \qquad
\mathrm{rot}\,\vec{E} = -\partial_t\vec{B}, \qquad
\mathrm{rot}\,\vec{B} = \mu\vec{\jmath} + \epsilon\,\partial_t\vec{E},
\tag{17}
$$

reduced to a single equation of the form $(D - \tfrac{i}{c}\partial_t)\Phi = -\Psi$ with $c = 1/\sqrt{\epsilon\mu}$, solved with $\lambda = \sqrt{\epsilon\mu}$. **The constants of this section were not verified, and as extracted they do not all agree with the standard SI forms.** The extraction of the system (17) shows the ampèrian equation as $\mathrm{rot}\,\vec{B} = \mu\vec{\jmath} + \epsilon\,\partial_t\vec{E}$, whereas the standard SI form in terms of $\vec{B}$ is $\mathrm{rot}\,\vec{B} = \mu\vec{\jmath} + \mu\epsilon\,\partial_t\vec{E}$, the form that follows from $\mathrm{rot}\,\vec{H} = \vec{\jmath} + \partial_t\vec{D}$ with $\vec{B} = \mu\vec{H}$, $\vec{D} = \epsilon\vec{E}$; the factor $\mu$ is either dropped in the extraction or absent in the source, and it changes both the biquaternionic field that cancels the curl terms and the compatibility condition. The condition the source prints, $\mathrm{div}\,\vec{\jmath} + \sqrt{\epsilon\mu}\,\partial_t\rho = 0$, does not reduce to the plain conservation law $\mathrm{div}\,\vec{\jmath} + \partial_t\rho = 0$ under either reading of (17), which is a second sign that the printed constants could not be read faithfully. What this section contributes is its **structure** — a single equation $(D - \tfrac{i}{c}\partial_t)\Phi = -\Psi$ with the parameter $\lambda = \sqrt{\epsilon\mu}$ — and that structure should be re-derived from the published text before any constant from it is quoted.

## What Is Verified and What Is Not

**Verified by exact recomputation.** The square rule (2); the two orderings of the factorisation (1) and the sign relation (3); the scalar-vector split (5) of $D$; the equivalence of the kernel to the div-curl system (4); the equivalence (13) of Maxwell's system to the single equation; the corpus dictionary (14), including the identification of the source's $\vec{\varphi}$ with the corpus's A-field $\mathcal{A}$ up to the $4\pi$ normalisation; the closed form (9) of the quaternionic exponential and its unit modulus; the algebra of the right-inverse factor in (11); and the two worked examples of the harmonic-conjugate construction. All of these are polynomial identities in the basis $e_0, e_1, e_2, e_3$, in the partial derivatives, and in the field components; they were evaluated symbolically and their residuals vanish.

**Verified by computation.** The closed form (9) satisfies the differential equation $\partial_t G = \mp 2\pi k G$ to within $4 \times 10^{-15}$ over a random sample of $100$ frequencies and times, with the correct modulus $1$. The source's §5.1 analogue of the symbol equation, printed as $2\pi k\,\mathcal{F}(\Phi_{\lambda,\pm}) \pm i\lambda\partial_t\mathcal{F}(\Phi_{\lambda,\pm}) = 0$, is missing the factor $i$ on its first term: with it, the residual of the printed expression on $\exp(\mp 2\pi\lambda^{-1}tk)$ is of order $10^{-15}$, and without it the residual is $8.6$ on the sample. The same equation also prints the variable pair as $(x,t)$ where the transform is taken in $k$ at fixed $t$ — a harmless slip.

**Not verified, and flagged.** (i) The object called a **fundamental solution**. Its defining equation in the source, $(D \pm i\partial_t)\Phi_\pm = 0$ for $x \neq 0$, $t \neq 0$, is the **homogeneous** equation in the punctured domain; a fundamental solution in the classical sense carries $\delta$ on the right. The object whose Fourier transform is (9) is the **kernel of the right inverse**, and the inverse is correctly defined directly by (10) and proved in (11); a fundamental solution with a $\delta$ on the right is not exhibited. (ii) The declaration $\Phi_\pm \in L^1(\mathbb{R}^3 \times (0,\infty))$ **cannot** be reconciled with (9): by the Riemann–Lebesgue lemma the space Fourier transform of an $L^1$ function tends to $0$ at infinity, whereas (9) has modulus $1$ for every $k$. The two statements are inconsistent, and it is (9), not the $L^1$ claim, that the proof of the right inverse uses. (iii) The exact hypotheses and normalisations of **Theorems 13 and 16** were read only through the extracted running text, whose display is garbled; the *structure* recorded in (15) — right inverse, then completion by $u_0 - U[u_0]$ — is verified, but the printed leading factors, the pairing of $\mathrm{Re}$ and $\mathrm{Im}$ with $\mathrm{Vec}$, and the definition of $u_0$ should be checked against the published version before they are quoted. (iv) The constants of the SI homogeneous-medium section: as extracted, the system (17) and the condition the source prints with it are not mutually consistent — the ampèrian equation lacks the factor $\mu$ of the standard B-form, and the printed compatibility condition does not reduce to $\mathrm{div}\,\vec{\jmath} + \partial_t\rho = 0$ under either reading — so the exact field combination and the normalisation of that section were left unverified. Only its structure (a single equation with $\lambda = \sqrt{\epsilon\mu}$) is recorded.

**What the source does not do.** It does not solve a boundary-value problem: the domain is fixed, the transform is taken by zero extension, and the right inverse is global. It does not treat an inhomogeneous or chiral medium: the homogeneous medium enters only through the single constant $\lambda = \sqrt{\epsilon\mu}$, so the dispersive and magnetoelectric content of *Electromagnetism in Media — The Local Complex Structure at Work* is untouched. It does not quantise, and it makes no claim about the physical reading of the parabolic operators beyond their use as a computational route. Its stated aim is analytical efficiency, and its result should be read as a method, not as a physical model.

## Summary

The source's wave-operator factorisation $-\Delta + \partial_t^2 = (D + i\partial_t)(D - i\partial_t) = (D - i\partial_t)(D + i\partial_t)$ is exact in both orderings and is the real-time (hyperbolic) twin of the corpus's elliptic factorisation $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$: the source's two first-order operators are the corpus's biquaternionic gradient and the negative of its conjugate, read with $\partial_{ict} = -i\partial_t$. The kernel of $D \pm i\partial_t$ is exactly a generalized div-curl system, the time-dependent analogue of the corpus's Cauchy–Riemann–Fueter system, and it couples a scalar solution of the wave equation to its harmonic conjugate through the Teodorescu transform. The Fourier transform of the kernel is the quaternionic exponential of a pure vector, which is a **unit-modulus phase** — this unimodularity is the single fact that makes the parabolic Teodorescu transform an $L^2$ isometry in space, well defined for both signs, and its right-inverse property $(D \pm i\partial_t)T_{\mathcal{C},\pm}[\mp iw] = w$ follows from the symbol computation $\partial_t T = w \pm iDT$. The Maxwell application reproduces the corpus's single equation — the source's $\vec{E} + i\vec{B}$ is the corpus's A-field, and its Proposition 12 is the corpus's $\tilde{\nabla}\tilde{F} = -\tilde{R}$ up to the $4\pi$ of Gaussian units — and then goes beyond it constructively: pushing the source through the right inverse and subtracting the scalar part $u_0 - U[u_0]$ yields an explicit **purely vectorial** solution, a constructive family complementary to the retarded convolution the corpus records. The price is a set of source defects: a mislabelled fundamental solution whose homogeneous defining equation and $L^1$ requirement are inconsistent with its own unit-modulus transform, a missing factor $i$ in the §5.1 symbol equation, an SI reduction whose constants could not be read faithfully, and two solution theorems whose exact normalisations were not verifiable from the running text. The record is of a method new to the corpus and of a reformulation already in it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis; $e_k^2 = -e_0$, $e_je_k = -e_ke_j$ for $j \neq k$ |
| $i$ | Scalar imaginary unit, $i^2 = -1$, central |
| $\mathbb{B}$ | Biquaternion algebra |
| $\Omega$, $\mathcal{C} = \Omega \times (0,\infty)$ | Bounded spatial domain and the space-time domain of the source |
| $D = e_1\partial_x + e_2\partial_y + e_3\partial_z$ | Moisil–Teodorescu operator (the source's); the corpus's spatial part $\vec{\nabla}$ of $\tilde{\nabla}$ |
| $D \pm i\partial_t$ | The parabolic Dirac operators of the source; $D - i\partial_t = \tilde{\nabla}$ and $D + i\partial_t = -\bar{\tilde{\nabla}}$ at $c = 1$ |
| $\Delta = \partial_x^2 + \partial_y^2 + \partial_z^2$ | Three-dimensional Laplacian; $D^2 = -\Delta e_0$ |
| $\nabla, \mathrm{div}, \mathrm{rot}$ | Gradient, divergence, curl; $\mathrm{rot}$ is the source's $\mathrm{curl}$ |
| $w = u + iv = (u_0 + \vec{u}) + i(v_0 + \vec{v})$ | Biquaternion-valued function, split into real and imaginary quaternion parts, each scalar plus vector |
| $T_\Omega$ | Teodorescu transform, the right inverse of $D$ on $\Omega$ |
| $U[u_0]$ | Purely vectorial complement (7) of a scalar wave solution |
| $\mathcal{F}$ | Fourier transform in the space variables at fixed $t$ |
| $k$ | Frequency three-vector, read as the pure quaternion $e_1k_1 + e_2k_2 + e_3k_3$ |
| $\Phi_\pm$ | The source's kernel, $\mathcal{F}(\Phi_\pm)(k,t) = \exp(\mp 2\pi kt)$ |
| $T_{\mathcal{C},\pm}$, $T_{\mathcal{C},\pm,\lambda}$ | Parabolic Teodorescu transform (10) and its $\lambda$-scaled form (16) |
| $\vec{E}, \vec{B}, \rho, \vec{\jmath}$ | Electric field, magnetic field, charge density, current density |
| $\vec{\varphi} = \vec{E} + i\vec{B}$ | Biquaternionic field of the source; the corpus's A-field $\mathcal{A} = -i\tilde{F}$ |
| $\tilde{F}, \tilde{R}, \tilde{\nabla}, \bar{\tilde{\nabla}}, \Box$ | Corpus field-strength biquaternion, source biquaternion, biquaternionic gradient, its conjugate, d'Alembertian |
| $\epsilon, \mu, c = 1/\sqrt{\epsilon\mu}$ | Permittivity, permeability, speed of light in the medium (SI section) |
| $\lambda$ | Parameter of the perturbed operator $D \pm i\lambda\partial_t$; $\lambda = \sqrt{\epsilon\mu}$ for the homogeneous medium |

## Further Reading

- A. Guillén-Villalobos, B. B. Delgado and H. Vargas Rodríguez, *A biquaternionic reformulation of Maxwell's equations via Fourier analysis*, arXiv:2605.21412v2 [math.AP] (2026). The source of this article: the parabolic Dirac operators, the div-curl characterisation, the quaternionic exponential, the right inverse, and the vectorial Maxwell solutions.
- V. V. Kravchenko, *Applied Quaternionic Analysis* (Heldermann, 2003), §3.1.1 and the Teodorescu transform, for the equivalence of the Maxwell system to a single biquaternionic equation and the harmonic-conjugation process the source follows. The same source is used by *Maxwell's Equations in the Biquaternionic Formulation*.
- V. V. Kravchenko and R. Castillo P., "On the kernel of the Klein–Gordon operator", *Zeitschrift für Analysis und ihre Anwendungen* **17** (1998) 261–265, for the earlier statement that solutions of the Klein–Gordon equation are represented through solutions of parabolic Dirac equations; the source's lineage for the name.
- P. Cerejeiras, U. Kaehler and V. V. Kravchenko, "On a factorization of the Schrödinger and Klein–Gordon operators", *Mathematical Methods in the Applied Sciences* **31** (2008) 1722–1738, for the general scheme of factorising second-order time-dependent operators, of which the source's (1) is an instance.
- Viktor G. Kravchenko and Vladislav V. Kravchenko, "Quaternionic factorization of the Schrödinger operator and its applications to some first order systems of mathematical physics" (arXiv:math-ph/0305046, 2003), the companion entry of the factorisation above: for the same Schrödinger factorisation read as a reduction of first-order systems — the Dirac equation with scalar, electric and pseudoscalar potentials, the force-free magnetic fields, the Maxwell system of a slowly changing medium and the static Maxwell system — to the single quaternionic equation $D_3f+f\vec\alpha = 0$, and for the componentwise reduction of that equation to four scalar Schrödinger operators, recorded in *Quaternion Regular Functions*.
- B. B. Delgado and V. V. Kravchenko, "A Right Inverse Operator for $\mathrm{curl} + \lambda$ and Applications", *Advances in Applied Clifford Algebras* **29** (2019) 1–15, and "Biquaternionic treatment of inhomogeneous time-harmonic Maxwell's equations over unbounded domains", *Advances in Applied Clifford Algebras* **33** (2023) 29, for the right-inverse tradition and the completion process the source generalises to the parabolic operators.
- B. B. Delgado and R. M. Porter, "General solution of the inhomogeneous div-curl system and consequences", *Advances in Applied Clifford Algebras* **27** (2017) 3015–3037, for the div-curl general solution and the solenoidal class the time-independent limit of the source recovers.
- D. Eelbode, "Solutions for the Hyperbolic Dirac Equation on $\mathbb{R}^{1,m}$", *Complex Variables, Theory and Application* **48** (2003) 377–395, and D. Eelbode and F. Sommen, "The Fundamental Solution of the Hyperbolic Dirac Operator on $\mathbb{R}^{1,m}$: a new approach", *Bulletin of the Belgian Mathematical Society — Simon Stevin* **12** (2005) 23–37, for the hyperbolic Dirac operators between which the source's parabolic factorisation sits, the elliptic Fueter theory on one side and the split-signature theory on the other.
- E. H. Lieb and M. Loss, *Analysis* (American Mathematical Society, 2001), for the Fourier conventions of the source's §2.1: the differentiation rule, the convolution theorem, and the Plancherel theorem.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1975), for Maxwell's equations in the Gaussian and SI units of the source's §§5 and 5.1.
