# __The Biquaternion D'Alembertian and Its Green's Functions__

## Introduction

Every relativistic equation of this series is built from a single operator. The Klein–Gordon equation writes it with a scalar mass term, the Dirac equation uses its first-order square root, Maxwell's equations use the same square root on a bivector-valued field, and the retarded potentials use its inverse. That operator is the **biquaternion d'Alembertian**
$$
\Box_\Phi = \tilde\nabla_\Phi\,(\tilde\nabla_\Phi)^{\natural}= (\tilde\nabla_\Phi)^{\natural}\,\tilde\nabla_\Phi = \Delta_\Phi - \partial^2/\partial {r'_t}^2 ,
$$
built from the biquaternionic gradient $\tilde\nabla_\Phi$ and its quaternion conjugate. The purpose of this article is to establish the operator itself, its adjoint structure, and the collection of distributions that invert it — its **Green's functions** — once and for all, so that the spin-specific articles can cite the result instead of rebuilding it.

The article is deliberately not about a particle. The Klein–Gordon equation and its propagator belong to the companion articles on spin $0$; the Dirac equation and its descendants belong to the companions on spin $1/2$; Proca and Rarita–Schwinger belong to spin $1$ and above. What those articles share, and what is developed here, is the operator that all of them are written in terms of, together with the object that turns a source into a field. Three things are established.

First, the operator. The d'Alembertian is the **biquaternion norm of the gradient**, $\Box_\Phi = \langle\tilde\nabla_\Phi\rangle_{\natural}$, and it is *central*: it is a scalar multiple of the algebra's identity as an operator, so it commutes with every biquaternion. Its symbol on a plane wave is $\omega^2/c^2 - \vec\nu_\Phi^2$. Its formal adjoint is itself, and this is the first application of the involution lattice that the companion article on the involutions develops: the adjoint of the gradient is $-(\tilde\nabla_\Phi)^{\natural}$, and the two signs cancel in the composed operator. The sign convention is the series convention of the companion *Algebra and Element Conventions*,
$$
\Box_\Phi = \tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural} = \Delta_\Phi - \partial^2/\partial {r'_{t}}^2 \quad \text{on } \mathbb{B}_{\Phi} ,
$$
and it is the one used by the Klein–Gordon and Dirac companions and by every article of the series. The Weyl-spinor exercise writes the same operator in real time as $-\partial^2/\partial {r'_{t}}^2 + \vec\nabla_\Phi^2$.

Second, the kernels. Because the $i r'_t$ coordinate turns $\Box_\Phi$ into the four-dimensional Euclidean Laplacian, the inversion of $\Box_\Phi$ is the classical theory of the Laplacian's fundamental solutions, and its different Green's functions are different boundary conditions on one equation. The **invariant** (Euclidean) kernel is $1/(4\pi^2\rho^2)$ with $\rho^2 = \langle\tilde R_\Phi\rangle_{\natural}$; the **retarded** and **advanced** kernels are supported on the light cone, $G_{\mathrm{ret}} = \frac{1}{4\pi R}\delta(r'_t - R)$ and $G_{\mathrm{adv}} = \frac{1}{4\pi R}\delta(r'_t + R)$; their difference is the commutator function; and the **causal** kernel is the boundary-value combination that the Wick rotation continues to the Euclidean one. The light-cone delta and its Jacobian, which the companion exercise *Exercise: The Retarded Potentials and the Green's Function* derives for the electromagnetic problem, are re-derived here as the general statement they are an instance of.

Third, the genuinely biquaternionic kernel. The second-order operator $\Box_\Phi$ has a scalar Green's function, but the first-order operator $\tilde\nabla_\Phi$ — the one the Dirac and Maxwell equations are built from — has a **biquaternion-valued** Green's function, $\tilde{G}_{\Phi,\tilde\nabla_\Phi} = (\tilde\nabla_\Phi)^{\natural} G_{\Box,\Phi}$, and it lies in the material sector $\mathbb{B}_{\Phi}$. This is not a cosmetic difference. The scalar kernel is central and commutes with the whole algebra; the first-order kernel is a material four-vector, transforms under the rotor action, and does not commute. Both facts are consequences of the algebra and are verified below.

The article is organised as follows. The gradient and the d'Alembertian are established first, with the composition, the symbol, the central scalar, and the adjoint. The defining equation for the Green's function, the invariant kernel, and the causal kernels follow, with the light-cone Jacobian and the boundary condition that selects the retarded solution. The massive operator and the first-order kernel are treated next, together with the shifted gradient — central and non-central — and the Kirchhoff and Kirchhoff–Green representations the shift carries, and the article closes with the sector structure of the kernels and the table of results.

- Companion article *Algebra and Element Conventions*, for the series d'Alembertian, the metric (its three levels are ruled on in *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*), and the d'Alembertian convention.
- Companion article *Exercise: The Retarded Potentials and the Green's Function*, for the retarded kernel and boundary condition specialised to the electromagnetic potential.
- Companion article *The Klein–Gordon Equation in Biquaternionic Form*, for the second-order equation the operator carries.
- Companion article *The Dirac Equation in Biquaternionic Form*, for the first-order equation built from the gradient and the spinor on which it acts.
- Companion article *Bispinor Fields and the Fundamental Solution of the Generalized Maxwell–Dirac Equation*, for the solution theory of the shifted operator: its fundamental solution on the light cone, the general solution of the inhomogeneous equation, the harmonic bispinors, and the class in which the homogeneous equation has only the trivial solution.
- Companion article *Matrix Representations Conventions*, §*The Clifford Structure and the Frame*, for the reversal and the pairing formula used in the kernel identities.
- Companion article *Interpretation of the Wick Rotation in the Biquaternion Universe*, for the rotation relating the causal and invariant kernels.

## The Biquaternionic Gradient

The gradient is the material four-vector operator assembled from the basis,
$$
\tilde\nabla_\Phi = e_t\,\partial/\partial R_t + \vec e_x\,\partial/\partial R_x + \vec e_y\,\partial/\partial R_y + \vec e_z\,\partial/\partial R_z
= \sum_{\imath\in\{t,x,y,z\}} e_{\imath}\,\partial/\partial R_{\imath} ,
\qquad
\partial/\partial R_t = -i\partial/\partial r'_t ,
$$
with the spatial derivatives real and the time derivative carrying the $i r'_t$ factor. Its quaternion conjugate reverses the vector part and leaves the scalar part,
$$
(\tilde\nabla_\Phi)^{\natural} = e_t\,\partial/\partial R_t - \vec e_x\,\partial/\partial R_x - \vec e_y\,\partial/\partial R_y - \vec e_z\,\partial/\partial R_z
= \sum_{\imath\in\{t,x,y,z\}} e_{\imath}^{*}\,\partial/\partial R_{\imath} ,
$$
where the second equality uses $e_t^{*} = e_t$ and $\vec e_\eta^{*} = -\vec e_\eta$, that is, Hermitian conjugation of the basis. The identity $(\tilde\nabla_\Phi)^{\natural} = \sum_{\imath} e_{\imath}^{*} \partial/\partial R_{\imath}$ is the only algebraic input the operator theory needs, and it is the reason the adjoint of the operator is a conjugation of the operator.

Two warnings about reading $\tilde\nabla_\Phi$ as an element of $\mathbb{B}$ are needed, because they govern every manipulation that follows. The coefficients $\partial/\partial R_{\imath}$ are **operators**, not complex numbers, so $\tilde\nabla_\Phi$ is not an element of the algebra but an algebra-valued differential operator; statements about it are statements about its action. And the coefficients do not commute with the basis in the naive way, because the time coefficient $\partial/\partial R_t$ is imaginary while the basis is not: the product rule fixes the order, and $\tilde\nabla_\Phi$ acts by left multiplication on the field,
$$
\tilde\nabla_\Phi\tilde{Ξ} = \sum_{\imath} e_{\imath}\,\partial/\partial R_{\imath}\,\tilde{Ξ} .
$$
Nothing else in the construction depends on the choice of left or right action, because the d'Alembertian will turn out to be central; the first-order kernel will not be, and there the order is the content.

## The D'Alembertian as a Biquaternion Norm

### Composition and the central scalar

The two second-order operators built from the gradient are equal, and each is the scalar Laplacian in the $i r'_t$ coordinate. Composing,
$$
\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}
= \sum_{\imath,\jmath} e_{\imath} e_{\jmath}^{*}\,\partial^2/\partial R_{\imath}\partial R_{\jmath}
= \sum_{\imath} e_{\imath} e_{\imath}^{*}\,\partial^2/\partial R_{\imath}^2
+ \sum_{\imath \neq \jmath} e_{\imath} e_{\jmath}^{*}\,\partial^2/\partial R_{\imath}\partial R_{\jmath} .
$$
On the diagonal $e_{\imath} e_{\imath}^{*} = e_t$ for every $\mu$: for $\mu = 0$ this is $e_t e_t = e_t$, and for $\mu = k$ it is $\vec e_\eta(-\vec e_\eta) = -\vec e_\eta^2 = e_t$. On the off-diagonal the products are basis bivectors, $e_t \vec e_\eta^{*} = -\vec e_\eta$ and $\vec e_j \vec e_\eta^{*} = -\vec e_j \vec e_\eta$ for $j \neq k$, and the coefficient $\partial^2/\partial R_{\imath}\partial R_{\jmath}$ is symmetric in ${\imath},\jmath$ while the bivector part is antisymmetric. The off-diagonal sum therefore vanishes, and
$$
\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural} = e_t\sum_{\imath}\partial^2/\partial R_{\imath}^2 = e_t\left(\Delta_\Phi - \partial^2/\partial {r^{\prime}_t}^2\right).
$$
The same computation with the factors exchanged gives $(\tilde\nabla_\Phi)^{\natural} \tilde\nabla_\Phi = e_t(\Delta_\Phi - \partial^2/\partial {r^{\prime}_t}^2)$, so the two orders agree. Writing $e_t$ as the identity and dropping it, the series convention is
$$
\boxed{\;
\Box_\Phi = \tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}= (\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi = \Delta_\Phi - \partial^2/\partial {r'_{t}}^2\;}.
$$

The result says two things. It says that the d'Alembertian is the **biquaternion norm of the gradient**, $\Box_\Phi = \langle\tilde\nabla_\Phi\rangle_{\natural}$, evaluated on the operator rather than on a fixed biquaternion: the composition that defines $\langle\cdot\rangle_{\natural}$ is exactly the composition of the gradient with its reversal. And it says that $\Box_\Phi$ is a **central scalar** as an operator — a multiple of the identity of the algebra — so that it commutes with every biquaternion,
$$
\Box_\Phi(\tilde{Q}_1\tilde{Ξ}) = \tilde{Q}_1\,(\Box_\Phi\tilde{Ξ}), \qquad \tilde{Q}_1 \in \mathbb{B},\ \tilde{Ξ}\ \text{any field}.
$$
Every later statement about the scalar Green's function follows from this centrality, and every departure from it will be a statement about the first-order operator instead.

The verification of the composition was made on a random real symbol vector $s$, for which the two ordered sums $\sum_{\imath\jmath} e_{\imath} e_{\jmath}^{*} s_{\imath} s_{\jmath}$ and $\sum_{\imath\jmath} e_{\imath}^{*} e_{\jmath} s_{\imath} s_{\jmath}$ each reduce to $(s_0^2 + s_1^2 + s_2^2 + s_3^2)e_t$ exactly, in integer and rational arithmetic with no floating-point tolerance. It is the algebraic form of the statement that no bivector survives the symmetrisation.

### The symbol, and the sign convention

On a plane wave
$$
\tilde{Ξ} = \tilde{Ξ}_0\,\exp(-i\theta_{\mathrm{pwp}})
$$
the derivatives act as numbers: $\partial/\partial R_t \to -\frac{i}{c}(-i\omega) = -\omega/c$ and $\partial/\partial R_\eta \to i \nu_{\Phi\eta}$, so
$$
-\partial^2/\partial {r^{\prime}_t}^2 \to \frac{\omega^2}{c^2}, \qquad \Delta_\Phi \to -2\pi\vec\nu_\Phi^2,
\qquad
\Box_\Phi \to \frac{\omega^2}{c^2} - 2\pi\vec\nu_\Phi^2 .
$$
The symbol was checked by finite differences on such a wave, with the numerical value of $\Box_\Phi\tilde{Ξ}$ agreeing with $(\omega^2/c^2 - \vec\nu_\Phi^2)\tilde{Ξ}$ to the accuracy of the difference scheme. The zero set of the symbol, $\omega^2 = c^4\pi\vec\nu_\Phi^2$, is the light cone, which in this algebra is the zero-divisor cone of the biquaternion norm; the mass-shell condition $\Box_\Phi \to 4\pi^{2}\nu_m^{2}$ is the shifted cone. Here $\nu_m=\frac{mc}{h}$ is the mass wave number, the inverse of the mass length.

The sign convention deserves a paragraph of its own, because it is the series' most common false alarm. With $\partial/\partial R_t = -i\partial/\partial r'_t$, the operator above is $\Box_\Phi = \Delta_\Phi - \partial^2/\partial {r'_{t}}^2$, and the physical mass equation is
$$
\left(\Box_\Phi - 4\pi^{2}\nu_m^{2}\right)\tilde{Ξ} = 0 ,
$$
whose symbol reproduces $\omega^2 = c^4\pi\vec\nu_\Phi^2 + c^2\,4\pi^{2}\nu_m^{2}$. The companion article *Exercise: Chirality and the Weyl Spinors* carries $\frac{h}{2\pi}$ and works with the quantum-field-theory metric $(+,-,-,-)$ and writes the same operator in real time, $\Box_\Phi = -\partial^2/\partial {r'_{t}}^2 + \vec\nabla_\Phi^2$; its mass equation is $(\Box_\Phi-4\pi^{2}\nu_m^{2})\tilde{Ξ} = 0$, the same equation as here and as in every other companion. Throughout this article $\Box_\Phi$ means the series convention above and the mass term is $-\nu_m^{2}$ with $\nu_m=\frac{mc}{h}$.

### Self-adjointness

The adjoint of the gradient is computed with the Hermitian pairing on fields,
$$
\langle \tilde{F}, \tilde Q\rangle = \int 2\,\mathrm{Sc}\!\left(\tilde{F}^{*} \tilde Q\right) d^4r ,
$$
the integration running over real time and space. Integrating by parts and using $\bigl(\partial/\partial R_{\imath}\,\tilde{F}\bigr)^\dagger = \partial/\partial R_{\imath}\,\tilde{F}^{*}$ for the real differential operators,
$$
\langle \tilde{F}, \tilde\nabla_\Phi\tilde Q\rangle
= \int 2\,\mathrm{Sc}\!\left(\tilde{F}^{*}\, \sum_{\imath}\,e_{\imath}\,\partial/\partial R_{\imath}\,\tilde Q\right) d^4r
= -\int 2\,\mathrm{Sc}\!\left(\bigl(\partial/\partial R_{\imath} \tilde{F}^{*}\bigr) e_{\imath} \tilde Q\right) d^4r .
$$
The algebraic identity
$$
\sum_{\imath} \bigl(\partial/\partial R_{\imath}\,\tilde{F}\bigr)^\dagger e_{\imath}
= \left(\sum_{\imath} e_{\imath}^{*}\,\partial/\partial R_{\imath}\,\tilde{F}\right)^\dagger
= \bigl((\tilde\nabla_\Phi)^{\natural}\tilde{F}\bigr)^\dagger
$$
uses only the antilinearity of ${}^{*}$ and $(e_{\imath}^{*})^{*} = e_{\imath}$; it was verified on random complex biquaternion coefficients. Substituting,
$$
\langle \tilde{F}, \tilde\nabla_\Phi\tilde Q\rangle = -\langle (\tilde\nabla_\Phi)^{\natural}\tilde{F}, \tilde Q\rangle ,
\qquad\text{that is,}\qquad
\tilde\nabla_\Phi^{*} = -\,(\tilde\nabla_\Phi)^{\natural}.
$$
The adjoint of the gradient is minus its conjugate; equivalently, the adjoint of the conjugate gradient is minus the gradient, $\bigl((\tilde\nabla_\Phi)^{\natural}\bigr)^\dagger = -\,\tilde\nabla_\Phi$, since ${}^{*}$ is an involution on operators. The d'Alembertian is then self-adjoint with no residual sign,
$$
\Box_\Phi^{*} = \bigl(\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}\bigr)^\dagger
= \bigl((\tilde\nabla_\Phi)^{\natural}\bigr)^\dagger \tilde\nabla_\Phi^{*}
= \bigl(-\tilde\nabla_\Phi\bigr)\bigl(-(\tilde\nabla_\Phi)^{\natural}\bigr)
= \Box_\Phi ,
$$
which is the operator form of the statement that $\Box_\Phi$ is real and central. This is the first place the four involutions of the companion article on the involution lattice do work: the adjoint is $-{}^{\natural}$, the reversal, and self-adjointness after composition follows from composing the sign twice. The companion article develops the lattice, the fixed spaces, and the matrix realisations in full; here the only fact used is the one just displayed.

## The Defining Equation for the Green's Function

A Green's function of $\Box_\Phi$ is a distribution $G(\tilde R_\Phi,\tilde{R}_{\Phi,2})$ satisfying
$$
\Box_\Phi\,G(\tilde R_\Phi,\tilde{R}_{\Phi,2}) = -\,\delta^{(4)}(\tilde R_\Phi - \tilde{R}_{\Phi,2}) ,
$$
where the $\Box_\Phi$ differentiates in the first argument of $G$ and the right-hand side is the four-dimensional delta in the $i r'_t$ coordinate; the argument is written in the field and never in the subscript, so the glyph names the operator and not the variable it acts on. The sign is the series convention: it is the sign of the companion exercise, and with it the retarded kernel of the electromagnetic problem is $\Box_\Phi\tilde{A}_{\Phi} = -\mu\tilde J_{\Phi}$ inverted by convolution. With this normalisation the inhomogeneous equation
$$
\Box_\Phi\tilde{Ξ} = \tilde{J}_{\Phi}
$$
is solved by
$$
\tilde{Ξ}(\tilde R_\Phi) = -\int G(\tilde R_\Phi,\tilde{R}_{\Phi,2})\,\tilde{J}_{\Phi}(\tilde{R}_{\Phi,2})\,d^4Q_2 ,
$$
because $\Box_\Phi$ is central and may be moved through any algebraic factor. The minus sign and the sign of the source equation are a matched pair; changing either alone changes the sign of the field, which is the usual source of an apparent inconsistency between articles that state the convolution differently.

When the kernel depends only on the difference,
$$
G(\tilde R_\Phi,\tilde{R}_{\Phi,2}) = G(\tilde R_\Phi-\tilde{R}_{\Phi,2}) ,
$$
the operator is translation invariant and the convolution is a convolution. This will be the case for all the kernels below: $\Box_\Phi$ has constant coefficients, so the general solution is the sum of a particular convolution and a solution of the homogeneous equation, and the choice among kernels is a choice of boundary condition, not of algebra.

## The Invariant Kernel

### The four-dimensional Euclidean reading

With $\tilde R_\Phi = i r'_t\,e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$, the biquaternion norm is
$$
\rho^2 := \langle\tilde R_\Phi\rangle_{\natural} = (i r'_t)^2 +r_x^2+r_y^2+r_z^2 = -{r'_{t}}^2 +r_x^2+r_y^2+r_z^2 ,
$$
the Minkowski interval continued to imaginary time. Read as a quadratic form in the four coordinates $(x_0, x_1, x_2, x_3)$ with $x_0 = i r'_t$ and $x_\eta = r_\eta$, the operator $\Box_\Phi = \Delta_\Phi - \partial^2/\partial {r^{\prime}_t}^2$ is *exactly* the four-dimensional Laplacian,
$$
\Box_\Phi = \sum_{\imath\in\{t,x,y,z\}} \partial^2/\partial R_{\imath}^2 = \Delta_\Phi ,
$$
so that the inversion of the wave operator is the classical inversion of the Laplacian. This is the point of the $i r'_t$ convention, and it is why the framework's Green's functions are the standard ones of potential theory.

The rotationally invariant fundamental solution of $-\Delta_\Phi G = \delta^{(4)}$ in four dimensions is
$$
\boxed{\;
G_{\mathrm{inv}}(\tilde R_\Phi) = \frac{1}{4\pi^2\rho^2} ,
\qquad
-\Box_\Phi\,G_{\mathrm{inv}} = \delta^{(4)}(\tilde R_\Phi)\;}.
$$
The coefficient is fixed by the distributional identity $\Delta_\Phi\,\rho^{2-d} = -(d-2)\frac{2\pi^{d/2}}{\Gamma(d/2)}\delta^{(d)}$ at $d = 4$, which gives $\Delta_\Phi\rho^{-2} = -4\pi^2\delta^{(4)}$. The identity was verified independently here by parts against a radial Gaussian: the integral $\int G_{\mathrm{inv}}\,(-\Delta_\Phi f)\,d^4r$ evaluates to $f(0)$ with the coefficient $1/(4\pi^2)$, to four decimal places on a two-million-point radial grid. In the Fourier variable $k = (k_4,2\pi\vec\nu_\Phi)$ conjugate to the $i r'_t$ coordinate, $\Box_\Phi \to -k_4^2 - 2\pi\vec\nu_\Phi^2$ and
$$
G_{\mathrm{inv}}(k) = \frac{1}{k_4^2 + 2\pi\vec\nu_\Phi^2} ,
$$
the four-dimensional Coulomb kernel.

Three properties of $G_{\mathrm{inv}}$ are worth naming. It is **real and scalar**: it is a multiple of $e_t$, hence central, and it commutes with every biquaternion. It is **invariant**: it depends on $\tilde R_\Phi$ only through $\langle\tilde R_\Phi\rangle_{\natural}$, so it is unchanged by the Lorentz action $\tilde R_\Phi \mapsto \tilde{U}\tilde R_\Phi\tilde{U}^{*}$, which preserves the biquaternion norm. And it is **singular on the light cone**: $\rho^2$ vanishes exactly on the zero-divisor cone, and the kernel is not defined there as a function. As the Euclidean solution it is the one selected by decay at large $\rho$ with no reference to time; the causal solutions below differ from it by solutions of the homogeneous equation, and the difference is the whole of the physical content of the choice.

### The light-cone delta and the retarded kernel

The causal kernels are supported on the light cone and are obtained from the invariant kernel by a distributional identity on the cone. The relevant object is the light-cone delta, which resolves the quadratic form into the two cones,
$$
\delta(\rho^2) = \delta\!\left(-{r'_{t}}^2 + R^2\right) = \frac{1}{2R}\Bigl[\delta\!\left(r'_t - R\right) + \delta\!\left(r'_t + R\right)\Bigr] ,
\qquad R = |r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z| ,
$$
where the Jacobian is $|dg/dr'_t| = 2|r'_t| = 2R$ at either root. Applying the future step function selects the forward cone,
$$
\mathrm{H}_{\mathrm{hvs}}(r'_t)\,\delta(\rho^2) = \frac{1}{2R}\,\delta\!\left(r'_t - R\right) ,
\qquad\text{hence}\qquad
\boxed{\;
G_{\mathrm{ret}}(\tilde R_\Phi) := \frac{1}{4\pi R}\,\delta\!\left(r'_t - R\right) = \frac{1}{2\pi}\,\mathrm{H}_{\mathrm{hvs}}(r'_t)\,\delta(\rho^2)\;}.
$$
The Jacobian identity was checked by smearing $\mathrm{H}_{\mathrm{hvs}}(r'_t)\,\delta(\rho^2)$ against a test function on a two-million-point mesh, the numerical value reproducing $\xi(R)/(2R)$ for three values of $R$ to three decimal places. The normalisation is the one the display uses: $\delta$ of the argument $\rho^2$ carries the Jacobian $2R$ and gives $\xi(R)/(2R)$, as does $\delta$ of ${r'_{t}}^2 - R^2$; the two agree, and the agreement is the check that the $i r'_t$ coordinate carries no scale. The symmetric relation between the retarded and advanced kernels is then immediate,
$$
G_{\mathrm{adv}}(\tilde R_\Phi) = \frac{1}{4\pi R}\,\delta\!\left(r'_t + R\right) = \frac{1}{2\pi}\,\mathrm{H}_{\mathrm{hvs}}(-r'_t)\,\delta(\rho^2) .
$$

The retarded kernel inverts the operator. Applying $\Box_\Phi = \Delta_\Phi - \partial^2/\partial {r^{\prime}_t}^2$ to $\frac{u(r'_t - R)}{4\pi R}$ and using the two radial identities
$$
(\vec\nabla_\Phi g)^2 = 1 ,
\qquad
2\,\vec\nabla_\Phi\frac{1}{R}\cdot\nabla g + \frac{1}{R}\,\Delta_\Phi g = 0 ,
\qquad g = r'_t - R ,
$$
which hold off the origin and were verified to machine precision, the operator annihilates every such function where $R \neq 0$. The whole of $\Box_\Phi G_{\mathrm{ret}}$ is therefore concentrated at the origin, and the standard computation gives
$$
\Box_\Phi\,G_{\mathrm{ret}} = -\,\delta(r'_t)\,\delta^{(3)}(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) .
$$
The result was checked directly: on a smooth radial-$u$ kernel, $\Box_\Phi[u(r'_t-R)/(4\pi R)]$ evaluated by central differences at a generic off-origin point is at the level of the difference scheme's truncation error — below $10^{-8}$ for a step of $10^{-4}$, and falling as the square of the step until roundoff sets the floor, as a second-order scheme requires for an expression that vanishes identically. The advanced kernel solves the same equation, $\Box_\Phi G_{\mathrm{adv}} = -\delta$, so the two are distinguished only by the support condition: $G_{\mathrm{ret}}$ vanishes for $r'_t<0$ and $G_{\mathrm{adv}}$ for $r'_t>0$, and the physical kernel is chosen by the requirement that a source affect only its future. This is the boundary condition of the companion exercise, and it is not an algebraic consequence of $\Box_\Phi$.

### The advanced kernel, the commutator function, and the causal kernel

The difference of the two causal kernels solves the *homogeneous* equation, since the sources cancel:
$$
\mathcal{G}_{\mathrm{PJ}}(\tilde R_\Phi) := G_{\mathrm{ret}}(\tilde R_\Phi) - G_{\mathrm{adv}}(\tilde R_\Phi)
= \frac{1}{4\pi R}\Bigl[\delta\!\left(r'_t - R\right) - \delta\!\left(r'_t + R\right)\Bigr] ,
\qquad
\Box_\Phi\,\mathcal{G}_{\mathrm{PJ}} = 0 .
$$
This is the Pauli–Jordan (commutator) function: it is antisymmetric in time, supported on the full light cone, and in the quantum theory of the field it is the kernel of the equal-time commutator. Its vanishing outside the cone is the algebraic expression of microcausality, and it is the object that the companion articles on canonical quantisation use. In the framework's terms, $\mathcal{G}_{\mathrm{PJ}}$ is an odd distribution whose support is precisely the zero-divisor cone of the biquaternion norm — the statement that the algebraic null cone is the geometric causal cone.

The **causal** or Feynman kernel is the boundary-value combination that is symmetric in time and selects positive frequencies forward and negative frequencies backward. In the $i r'_t$ variables it is the analytic continuation of the Euclidean kernel with the Feynman prescription,
$$
G_{F}(\tilde R_\Phi) = \frac{1}{4\pi^2}\,\frac{1}{\rho^2 - i\epsilon} ,
\qquad \epsilon \to 0^+ ,
$$
whose Fourier transform is $1/(k_4^2 + \vec\nu_\Phi^2 - i\epsilon)$. Two facts make this the natural object of the quantum theory: its Wick rotation to imaginary time is exactly $G_{\mathrm{inv}}$, and its $i\epsilon$ prescription is the statement of which vacuum the propagator is referred to. The companion *Interpretation of the Wick Rotation in the Biquaternion Universe* develops the rotation in full; here it is enough to record that the four kernels — invariant, retarded, advanced, causal — are four boundary conditions on one operator, related by the cone identities above and by the time boundary conditions.

## The Massive Operator

Adding the mass term shifts the operator by a central scalar,
$$
\Box_\Phi - 4\pi^{2}\nu_m^{2} , \qquad \nu_m=\frac{mc}{h} ,
$$
and the defining equation becomes $(\Box_\Phi - 4\pi^{2}\nu_m^{2})G = -\delta$. In the $i r'_t$ variables the shifted operator is Helmholtz's, $-\Delta_\Phi + \nu_m^{2}$, and its invariant fundamental solution is the four-dimensional Yukawa kernel
$$
\boxed{\;
G^{(1/\nu_m)}_{\mathrm{inv}}(\tilde R_\Phi) = \frac{\nu_m}{4\pi^2\rho}\,\mathrm{Ki}_{1}(\rho\,\nu_m) ,
\qquad
\left(-\Delta_\Phi + \nu_m^{2}\right) G^{(1/\nu_m)}_{\mathrm{inv}} = \delta^{(4)}(\tilde R_\Phi)\;},
$$
with $K_1$ the modified Bessel function; its Fourier transform is
$$
G^{(1/\nu_m)}_{\mathrm{inv}}(k) = \frac{1}{k_4^2 + \vec\nu_\Phi^2 + \nu_m^{2}} .
$$
The short-distance behaviour is the massless kernel, $G^{(1/\nu_m)}_{\mathrm{inv}} \to 1/(4\pi^2\rho^2)$ as $\rho\,\nu_m \to 0$, and the large-distance behaviour is exponentially damped, $G^{(1/\nu_m)}_{\mathrm{inv}} \sim \frac{\nu_m^{1/2}}{2(2\pi)^{3/2}\rho^{3/2}}\exp(-\rho\,\nu_m)$: a mass screens. The retarded and advanced kernels acquire support inside the cone rather than on it, the sharp light-cone delta acquiring a tail in the Bessel functions; the closed form of the inside-cone part is the standard one and is cited rather than re-derived. The massless limit returns the delta on the cone, and the biquaternion content of the massive case is simply that the mass term is central, hence commutes with the algebra, and shifts the symbol by a constant without changing the sector structure.

The mass shell is the symbol condition
$$
\langle\tilde P_{\Phi}\rangle_{\natural} = -\!\left(\frac{\omega^2}{c^2} - 2\pi\vec\nu_\Phi^2\right)\Big|_{\text{on shell}} = -4\pi^{2}\nu_m^{2} ,
$$
which was checked on a random on-shell four-momentum $K = i(\omega/c)e_t + 2\pi\vec\nu_\Phi$ in $\mathbb{B}_{\Phi}$, the biquaternion norm returning $-\nu_m^{2}$ exactly. Off shell the operator is invertible on the algebra; on the mass shell the symbol vanishes on the zero-divisor cone of the relevant complex momentum, which is the algebraic origin of the propagation and of the rank drop that the massless limit will exhibit.

## The First-Order Kernel

The Dirac and Maxwell equations are first order, and their kernel is the kernel of $\tilde\nabla_\Phi$ rather than of $\Box_\Phi$. Since $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}= \Box_\Phi$, the inverse of left multiplication by $\tilde\nabla_\Phi$ is left multiplication by $(\tilde\nabla_\Phi)^{\natural}$ followed by the scalar kernel; the subscript names the operator inverted, as $G_{\Box,\Phi}$ names $\Box_\Phi$:
$$
\boxed{\;\begin{aligned}
\tilde{G}_{\Phi,\tilde\nabla_\Phi}(\tilde R_\Phi) &:= (\tilde\nabla_\Phi)^{\natural}\,G_{\Box_\Phi}(\tilde R_\Phi) \in \mathbb{B}_{\Phi} ,\\[2pt]
\tilde\nabla_\Phi\,\tilde{G}_{\Phi,\tilde\nabla_\Phi}(\tilde R_\Phi)
&= \tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}\,G_{\Box_\Phi}(\tilde R_\Phi)
= \Box_\Phi\,G_{\Box_\Phi}(\tilde R_\Phi)
= -\,\delta^{(4)}(\tilde R_\Phi) .
\end{aligned}\;}
$$
So $\tilde{G}_{\Phi,\tilde\nabla_\Phi}$ inverts the first-order operator with the same sign as $G_{\Box,\Phi}$ inverts the second. The result is not a scalar. With $G_{\Box,\Phi}$ a real scalar kernel,
$$
\tilde{G}_{\Phi,\tilde\nabla_\Phi} = e_t\,\partial/\partial R_t\,G_{\Box,\Phi} - \vec e_x\,\partial/\partial R_x\,G_{\Box,\Phi} - \vec e_y\,\partial/\partial R_y\,G_{\Box,\Phi} - \vec e_z\,\partial/\partial R_z\,G_{\Box,\Phi} ,
$$
and since $\partial/\partial R_t\,G_{\Box,\Phi} = -i\partial/\partial r'_t\,G_{\Box,\Phi}$ is imaginary while the spatial derivatives are real, the first-order kernel has an imaginary scalar part and a real vector part:
$$
\tilde{G}_{\Phi,\tilde\nabla_\Phi} \in \mathbb{B}_{\Phi} , \qquad\text{that is,}\qquad \tilde{G}_{\Phi,\tilde\nabla_\Phi}^{\flat} = \tilde{G}_{\Phi,\tilde\nabla_\Phi} .
$$
The sector assignment was verified on a representative scalar kernel by finite differences: the imaginary scalar and real vector character holds identically, with $\flat$ fixing the element to machine precision. This is the first genuinely biquaternionic structure in the article, and it is the reason the first-order articles differ from the second-order ones: the kernel that inverts the Dirac operator is a material four-vector, and the kernel that inverts the d'Alembertian is a central scalar.

Three consequences follow and are used by the companion articles.

**The kernel transforms as a vector.** Under the Lorentz action the scalar kernel is invariant, but the first-order kernel transforms by the four-vector rule,
$$
G_{\Box,\Phi}(\tilde R_\Phi) \mapsto G_{\Box,\Phi}(\tilde R_\Phi) ,
\qquad
\tilde{G}_{\Phi,\tilde\nabla_\Phi}(\tilde R_\Phi) \mapsto \tilde{U}\,\tilde{G}_{\Phi,\tilde\nabla_\Phi}(\tilde{U}^{-1}\tilde R_\Phi\tilde{U}^{-{}^{*}})\,\tilde{U}^{*} ,
$$
so that $\tilde\nabla_\Phi\tilde{G}_{\Phi,\tilde\nabla_\Phi} = -\delta$ is preserved with the rotated gradient. This is what makes the inverse of the Dirac operator a covariant object.

**The kernel does not commute.** Left multiplication by $\tilde{G}_{\Phi,\tilde\nabla_\Phi}$ does not commute with the algebra, because $\tilde{G}_{\Phi,\tilde\nabla_\Phi}$ is not central,
$$
\tilde{Q}_1\,\tilde{G}_{\Phi,\tilde\nabla_\Phi} \neq \tilde{G}_{\Phi,\tilde\nabla_\Phi}\tilde{Q}_1
\qquad \text{for generic } \tilde{Q}_1 \in \mathbb{B} ,
$$
in contrast with $G_{\Box,\Phi}$. The scalar kernel may be moved through any algebraic factor; the first-order kernel may not, and its order relative to a field is part of the equation.

**The massless first-order equation is the conjugation-invariant one.** The homogeneous first-order equation $\tilde\nabla_\Phi\tilde{Ξ} = 0$ is the massless Dirac equation on the spinor module and the source-free Maxwell equation on the field strength, and its kernel theory is the theory of the functions annihilated by $(\tilde\nabla_\Phi)^{\natural}$. The massive first-order operator requires the chirality-off-diagonal mass term of the companion *The Dirac Equation in Biquaternionic Form* and is treated in the spin-$1/2$ articles; the massless kernel above is the common structure those articles specialise.

## The Shifted Gradient and the Generalized Maxwell–Dirac Equation

The first-order kernel inverts $\tilde\nabla_\Phi$. The author's programme on generalised solutions writes its first-order equations with the mass carried by that same operator rather than by a separate additive term, and the object that carries it is the **shifted gradient**, the plain gradient plus a central scalar, $\tilde\nabla_\Phi + \kappa$ with $\kappa \in \mathbb{C}$. The shift is written out and is never absorbed into the glyph: the operator is $\tilde\nabla_\Phi$ and $\kappa$ is a coefficient added to it. Because a central scalar commutes with the whole algebra the shift changes no order of factors, and the conjugation acts on the units at fixed coefficient, so the shifted conjugate is $(\tilde\nabla_\Phi)^{\natural}+ \kappa$.

**The square.** The shifted gradient and its conjugate compose to a central scalar operator. Since $\tilde\nabla_\Phi + (\tilde\nabla_\Phi)^{\natural}= -2i\,e_t\,\partial/\partial r'_t$, the cross term is $-2i\kappa\,e_t\,\partial/\partial r'_t$ and
$$
(\tilde\nabla_\Phi+\kappa)\bigl((\tilde\nabla_\Phi)^{\natural}+\kappa\bigr) = \bigl((\tilde\nabla_\Phi)^{\natural}+\kappa\bigr)(\tilde\nabla_\Phi+\kappa)
= \Box_\Phi - 2i\kappa\,e_t\frac{\partial}{\partial r'_t} + \kappa^2
= \left(-i\,e_t\frac{\partial}{\partial r'_t} + \kappa\right)^2 + \Delta_\Phi ,
$$
which is central. On the plane wave $\exp(i\theta_{\mathrm{pwp}})$ its symbol is
$$
\left(\frac{\omega}{c} - \kappa\right)^2 - \|\vec\nu_\Phi\|^2 ,
$$
so the shift acts on the symbol as a **translation of the frequency** and nothing else: $\omega$ and $\kappa$ enter only through the combination $\omega/c - \kappa$. Both the identity and the symbol were checked on random $(\omega, \vec\nu_\Phi, \kappa)$ to machine precision.

Here $\theta_{\mathrm{pwp}}:=2\pi\vec\nu_\Phi\cdot\vec r-\omega r'_t/c\in\mathbb{R}$ is the plane-wave angle: $\omega$ and $\vec\nu_\Phi$ are real, so the exponent is $i$ times a real number and the wave form is $\exp(i\theta_{\mathrm{pwp}})$ wherever it is quoted.

**The generalized Maxwell–Dirac equation.** The single first-order equation
$$
\left(\tilde\nabla_\Phi + \kappa\right) B = F
$$
is the corpus form of the source's **generalized Maxwell–Dirac equation**. At $\kappa = 0$ it is the massless equation $\tilde\nabla_\Phi B = 0$ that the companion Dirac and Maxwell articles both use, and the source's point is that one operator, shifted by a single central number, is written for the Maxwell and the Dirac operators at once. The corpus records the algebraic content — a central shift of the single gradient is available, and the mass it can carry is one complex number — and separates it from the physical identification of the two fields, which is a claim about the interpretation of $B$ and not about the operator.

**A convention crossing.** The source's gradient is $\partial/\partial\tau \pm i\nabla = i\tilde\nabla_\Phi$ (the dictionary is recorded in the companion article on the electro-gravimagnetic programme), so its mass $m$ and the corpus shift are related by $\kappa = -im$. The case the source studies is an **imaginary** $m$, which is a **real** $\kappa$ here, and the dichotomy runs in opposite directions on the two sides. On the corpus side the symbol vanishes for real $(\omega, \vec\nu_\Phi)$ — non-trivial homogeneous plane waves exist — exactly when $\kappa$ is real, the vanishing set being the shifted cone $\omega/c = \kappa \pm \|2\pi\vec\nu_\Phi\|$. For non-real $\kappa$ the symbol never vanishes on real $(\omega, \vec\nu_\Phi)$, so there is no non-trivial **plane-wave** solution; the stronger statement, that there is no non-trivial solution at all, holds only in the tempered class, because the substitution $u = \exp(-\kappa x_4)v$ with $x_4 = i r'_t$ turns the operator into $\exp(-\kappa x_4)\Box_\Phi \exp(+\kappa x_4)$, so that *every* wave $v$ with $\Box_\Phi v = 0$ gives a homogeneous solution $u$ and that solution is not tempered. The companion article *Bispinor Fields and the Fundamental Solution of the Generalized Maxwell–Dirac Equation* states that class, the general homogeneous solution, and the fundamental solution of the shifted operator. Both branches were checked numerically, and the source's own statement (non-trivial solutions for imaginary $m$ alone) is the mirror image under $\kappa = -im$. An article that copies the source's "imaginary mass" into the corpus convention without the factor $i$ will place the interesting case on the wrong side of this dichotomy.

**The scalar-potential equation.** Applying $(\tilde\nabla_\Phi)^{\natural}+\kappa$ to $\left(\tilde\nabla_\Phi + \kappa\right) B = F$ gives
$$
\left(\Box_\Phi - 2i\kappa\,e_t\frac{\partial}{\partial r'_t} + \kappa^2\right) B = \bigl((\tilde\nabla_\Phi)^{\natural}+\kappa\bigr) F ,
$$
so each component of $B$ obeys the shifted scalar equation; and conversely a solution of the homogeneous scalar equation generates a solution of the homogeneous first-order equation,
$$
\left(\Box_\Phi - 2i\kappa\,e_t\frac{\partial}{\partial r'_t} + \kappa^2\right) u = 0
\quad\Longrightarrow\quad
\left(\tilde\nabla_\Phi + \kappa\right)\left(\bigl((\tilde\nabla_\Phi)^{\natural}+\kappa\bigr) u\right) = 0 .
$$
The converse is the shifted form of the **monogenic completion** the companion Dirac article uses at $\kappa = 0$, where a harmonic scalar $u$ is completed to the kernel element $(\tilde\nabla_\Phi)^{\natural}u$; the source generates its spinors this way, from a scalar "C-field" by convolution, and the companion Dirac article takes that up. The source names the scalar operator the **Klein–Gordon–Fock–Schrödinger equation**: its symbol carries a second-order term of Klein–Gordon–Fock type, $\Box_\Phi + \kappa^2$, and a first-order-in-time term $\kappa\,\partial/\partial R_t$ of Schrödinger type, and the name records that one operator contains one term of each kind. The corpus keeps the name only with that content attached. What the name does not supply is a derivation: one operator carrying a term of each type is not the same statement as the Klein–Gordon and Schrödinger equations following from it, and the corpus does not claim the latter.

**The Cauchy problem.** The second-order operator to which the shifted square reduces at $\kappa = 0$ is $\Box_\Phi$, the four-dimensional Laplacian in the $i r'_t$ variables, so the wave operator is $-\Box_\Phi$. The Cauchy problem $-\Box_\Phi G_{\mathrm{prop}} = G$ with data $G_{\mathrm{prop}}(0,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) = K^0(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)$ and $\partial/\partial\tau G_{\mathrm{prop}}(0,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) = K^1(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)$ is solved componentwise by the Kirchhoff formula of the companion *Partial Differential Equations*, with the retarded kernel $G_{\mathrm{ret}} = \frac{1}{4\pi R}\delta(r'_t - R)$ of the section above; the biquaternion content is that the data and the solution are read off component by component and the four scalar solutions are reassembled. The source writes the first-order version of the same representation, in which the solution carries an extra $\bigl((\tilde\nabla_\Phi)^{\natural}+\kappa\bigr)$ applied to the scalar potential, so that the scalar formula is recovered at $\kappa = 0$; the corpus records the second-order Kirchhoff form as the one it can state and verify, and the source's first-order integral form is now recorded and checked in the companion article *Bispinor Fields and the Fundamental Solution of the Generalized Maxwell–Dirac Equation*, together with the fundamental solution of the shifted operator itself.

**The bounded-domain form, and the Kirchhoff–Green representation.** The formula above is the whole-space form, in which the domain is all of space and the only data are the initial values. On a bounded domain the same kernel gives the **Kirchhoff–Green representation**, in which the value at an interior point is the volume integral of the wave operator applied to the field against the kernel together with a surface term carrying the field and its normal derivative; the surface splits into the initial surface, where the term is the Cauchy data, and the lateral boundary, where it is the boundary data. The biquaternionic form of that identity in the four-dimensional Laplacian variables, with its numerical verification, is in the companion *Biquaternion Integration*; the analogue for the biquaternionic wave ("biwave") operator, unifying the Maxwell- and Dirac-equivalent second-order equations in one operator and carrying the conditions on its shock fronts, is constructed by L. A. Alexeyeva in the 2021 paper cited in Further Reading.

### The Non-Central Structural Coefficient

The shift above is central: $\kappa$ is one complex number, it commutes with the whole algebra, and the operator it shifts is a single gradient. In the 2021 paper the shift is a full **constant biquaternion**, $f + F$ with $f$ a scalar and $F$ a constant vector, and what it shifts is the pair of **mutual bigradients** used by the electro-gravimagnetic programme,
$$
\vec\nabla_{+} = \partial/\partial\tau + i\vec\nabla_\Phi , \qquad
\vec\nabla_{-} = \partial/\partial\tau - i\vec\nabla_\Phi , \qquad
\tau = r'_{t} ,
$$
$$
D^{+}_F = \vec\nabla_{+} + f + F , \qquad
D^{-}_F = \vec\nabla_{-} + f - F ,
$$
written in the source's letters and without the corpus sector mark, because they are the source's operators and not glyphs of this calculus; the two are the $i$-multiples of the corpus gradient and of its conjugate, $\vec\nabla_{+} = i\tilde\nabla_\Phi$ and $\vec\nabla_{-} = i(\tilde\nabla_\Phi)^{\natural}$. The operator $D^+_F$ carries the coefficient and $D^-_F$ its mutual partner $f - F$. The paper's structural coefficient is the corpus shift $\kappa = -i(f+F)$. The corpus's central shift is therefore the case $F = 0$, and the whole of the new content is the non-central part.

**The composition.** The mutual bigradients compose to the wave operator, $\vec\nabla_{+}\vec\nabla_{-} = \vec\nabla_{-}\vec\nabla_{+} = -\Box_\Phi$, that is $\partial^2/\partial\tau^2 - \Delta_\Phi$ in the source's time $\tau$ — the massless composition of the section above, re-read in the source's variables — and so do the mutual MD-operators,
$$
D^+_F D^-_F = D^-_F D^+_F = -\Box_\Phi + 2f\,\partial/\partial\tau + 2i(F,\vec\nabla_\Phi) + f^2 + (F,F) .
$$
The cross terms cancel for the same reason as before — $[\,\partial/\partial\tau + f,\, i\nabla + F\,] = 0$ for a coefficient independent of $\tau$ — and the square acquires a **first-order directional derivative** $2i(F,\vec\nabla_\Phi)$ along the vector part of the coefficient, which no central shift can produce. The term has the shape of the KGFSh operator's first-order piece with the single number $\kappa$ replaced by a vector the operator differentiates along: the scalar part $f$ enters as a mass and the vector part $F$ enters as a direction, and the two are not interchangeable. The two identities and both candidate signs for the $2i(F,\vec\nabla_\Phi)$ term were checked on random fields: residual $2.5\times10^{-10}$ for the two identities and $3.6\times10^{-11}$ for their equality, against $7.5\times10^{-1}$ for the opposite sign.

**The weighted kernel, and a sign to pair correctly.** The fundamental solution of the scalar equation to which the square reduces is carried by the light cone with an exponential weight,
$$
\tilde{Ξ} = \frac{1}{4\pi r}\,\exp(-i\theta_{\mathrm{spa}})\exp(-\kappa_{\mathrm{dmp}})\,\delta(\tau - r) , \qquad r = |r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z| ,
$$
as the paper prints it, with the spatial angle $\theta_{\mathrm{spa}}:=(F,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)$ real because both factors are real and the decay $\kappa_{\mathrm{dmp}}:=rf$ real because the radius and the scalar part of the coefficient are real; on a plane wave the symbol becomes a shifted four-momentum and the transform of the kernel is its reciprocal. The exponent's **sign must match the sign of the $(F,\vec\nabla_\Phi)$ coefficient**, and this is the one place where the paper is not self-consistent. Substituting $\exp(\lambda(F,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) - f\tau)\xi$ into the operator leaves the residual $\bigl(\mu - 2\lambda\bigr)(F,\vec\nabla_\Phi\xi) + \bigl(1 + \lambda^2 - \mu\lambda\bigr)(F,F)\xi$; it vanishes for $\mu = 2\lambda$ with $\lambda = \pm i$ and for no other pairing. The coefficient and the exponent therefore carry the **same** sign: the coefficient $\mu = +2i(F,\vec\nabla_\Phi)$ is paired with
$$
\tilde{Ξ} = \frac{1}{4\pi r}\,\exp(+i\theta_{\mathrm{spa}})\exp(-\kappa_{\mathrm{dmp}})\,\delta(\tau - r) , \qquad
\text{symbol} \quad (\zeta - F)^2 - (\omega + if)^2 ,
$$
and $\mu = -2i(F,\vec\nabla_\Phi)$ with the mirror in which every sign of $F$ is reversed. The printed $\exp(-i\theta_{\mathrm{spa}})$ with the spatial angle $\theta_{\mathrm{spa}}=(F,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)$ real because both factors are real, with $(\zeta + F)^2 - (\omega + if)^2$ is that mirror; what the paper does not do is print it with the coefficient it uses. Its scalar equation, its KGFS equation and its theorem all carry the coefficient $+2i(F,\vec\nabla_\Phi)$ — its own derivation of the composition gives $+2i$ where its statement of the same lemma gives $-2i$ — while its kernel, its Fourier transform and the integral representations of its last three sections carry the opposite exponent. The two groups are therefore consistent only after $F \to -F$ in one of them, and the corpus records the pairing above, together with the discrepancy, rather than one of the printed halves.

**The weight, the phase, and the support.** At $F = 0$ the kernel is $\frac{\exp(-f\tau)}{4\pi r}\delta(\tau-r) = \exp(-f\tau)G_{\mathrm{ret}}$, which is the weighted retarded kernel of the companion bispinor article with the scalar part $f$ in the role of its $m$: on the cone $\tau = x$ the paper's weight $\exp(-xf)$ and the derived weight $\exp(-f\tau)$ are the same factor, and the section above records why the weight does not move the support. The non-central part behaves differently from the scalar part. For real $F$ the factor $\exp(i(F,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z))$ is a pure phase, so it rescales the phase at each light-cone point and moves no support, and the kernel is still a $\delta$ on the cone: Huygens' principle — which the scalar weight buys, in the bispinor article's account, at the price of self-adjointness — survives the non-central part. The price is not paid twice, and the reason is the adjoint behaviour of the two first-order pieces. The second-order operator's first-order part is $2f\partial/\partial\tau + 2i(F,\vec\nabla_\Phi)$; a first-order operator with a real coefficient is anti-self-adjoint, so the conjugating factor $i$ in the non-central term makes it **self-adjoint** for real $F$ while the scalar term stays anti-self-adjoint and carries the whole asymmetry.

**Where the hypotheses bite.** The closed composition is an identity for a constant coefficient, and the derivation shows what it really uses. Commutativity needs only $\partial/\partial\tau F = 0$, because the sole obstruction is $[\,\partial/\partial\tau, F\,] = \partial/\partial\tau F$; the **closed form** needs $\vec\nabla_\Phi F = 0$, the vector part both divergence-free and curl-free, at which the extra term $i(\vec\nabla_\Phi F)\circ B$ drops out. A coefficient that varies in space but not in time therefore keeps the two operators commuting and breaks the closed form: the difference between the true composition and the closed form is exactly $-i(\vec\nabla_\Phi F)\circ B$ (residual $2.8\times10^{-10}$), the closed-form residual of such a coefficient is $7.4\times10^{-2}$ while its commutator residual stays at $4.7\times10^{-11}$. A coefficient that varies in time breaks both ($7.1\times10^{-2}$ and $1.4\times10^{-1}$). Constant is the paper's case and the one in which both statements are exact.

The conditions on the shock fronts of this equation are the companion shock article's; the paper's Cauchy problem and its bounded-domain representation on the space–time cylinder are the biwave counterpart of the Kirchhoff and Kirchhoff–Green paragraphs above, and they inherit the same kernel with the same sign pairing.

## The Kernels and the Involutions

The four conjugations of the algebra act on the kernels in a way that is worth recording, because it is the bridge to the companion article on the involution lattice. The real scalar kernels — the invariant, the retarded and the advanced ones — are real multiples of $e_t$: the three involutions ${}^{\natural}$, $\bar{\cdot}$ and ${}^{*}$ fix them, while $\flat = -{}^{*}$ negates them,
$$
G_{\Box,\Phi}^{\natural} = \bar{G}_{\Box,\Phi} = G_{\Box,\Phi}^{*} = G_{\Box,\Phi} , \qquad G_{\Box,\Phi}^\flat = -\,G_{\Box,\Phi} ,
$$
where the last line uses $\flat = -{}^{*}$. The first-order kernel lies in the fixed space of $\flat$ and is negated by ${}^{*}$,
$$
\tilde{G}_{\Phi,\tilde\nabla_\Phi}^\flat = \tilde{G}_{\Phi,\tilde\nabla_\Phi} , \qquad \tilde{G}_{\Phi,\tilde\nabla_\Phi}^{*} = -\,\tilde{G}_{\Phi,\tilde\nabla_\Phi} ,
$$
which is exactly the definition of the material sector. Its $i$-multiple lies in the informational sector, $i\tilde{G}_{\Phi,\tilde\nabla_\Phi} \in \mathbb{B}_{\Psi}$, since $i\mathbb{B}_{\Phi} = \mathbb{B}_{\Psi}$; the conjugations themselves leave the sector untouched and it is the central multiplication that exchanges the two, as the companion article on the involutions establishes. The operator identities mirror these statements: $\Box_\Phi$ has real coefficients, hence is fixed by ${}^{\natural}$, $\bar{\cdot}$ and ${}^{*}$ and negated by $\flat$, exactly as the real scalar kernels are, and $\tilde\nabla_\Phi^{*} = -(\tilde\nabla_\Phi)^{\natural}$. The kernel's conjugation behaviour is therefore the operator's own: the reality of the kernel and the reality of the operator are one statement, inherited by the scalar kernel from the operator it inverts. The companion article *Algebra and Element Conventions* fixes the four conjugations and their real subspaces; the companion article on the involutions develops the lattice, the Klein four-group of $\{\mathrm{id}, {}^{\natural}, \bar{\cdot}, {}^{*}\}$ with $\flat = -{}^{*}$, and the matrix realisations. What this article adds is the operator content: the wave operator is the biquaternion norm of the gradient, its adjoint is itself because the adjoint of the gradient is $-(\tilde\nabla_\Phi)^{\natural}$, and the kernel that inverts it is central, while the kernel that inverts the first-order operator is a material four-vector.

A last structural remark ties the kernel theory to the algebra's null cone. The massless symbol vanishes on $\{\langle\tilde P_{\Phi}\rangle_{\natural} = 0\}$, the zero-divisor cone, and the causal kernels are supported on exactly the corresponding cone in position space. The algebra's zero divisors, its projective geometry, and the light-cone structure are the subject of the companion articles on the null quadric; for the operator theory the point is that the characteristic cone of $\Box_\Phi$ is the algebra's null cone, so that the propagation described by these Green's functions is the propagation of the biquaternion norm's zero set. That identification — the light cone *is* the zero-divisor cone — is what makes the framework's causal structure algebraic rather than postulated.

## Summary

The biquaternion d'Alembertian is the biquaternion norm of the gradient,
$$
\Box_\Phi = \tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}= (\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi = \Delta_\Phi - \partial^2/\partial {r'_{t}}^2 ,
$$
a central scalar operator whose symbol is $\omega^2/c^2 - \vec\nu_\Phi^2$ and whose sign is the series convention. Its adjoint is the gradient's adjoint composed with itself; the gradient obeys $\tilde\nabla_\Phi^{*} = -(\tilde\nabla_\Phi)^{\natural}$, so
$$
\Box_\Phi^{*} = \Box_\Phi ,
$$
the two minus signs cancelling. The adjoint statement was verified through the algebraic identity $\sum_{\imath}(\partial/\partial R_{\imath}\,\tilde{F})^\dagger e_{\imath} = ((\tilde\nabla_\Phi)^{\natural}\tilde{F})^\dagger$ on random complex coefficients, and the composition $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}= (\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi = \Delta_\Phi - \partial^2/\partial {r^{\prime}_t}^2$ was verified exactly on a random symbol.

The Green's functions are the boundary conditions on one equation, $-\Box_\Phi G = \delta^{(4)}$. The invariant kernel is
$$
G_{\mathrm{inv}} = \frac{1}{4\pi^2\rho^2} ,
\qquad \rho^2 = \langle\tilde R_\Phi\rangle_{\natural} = -{r'_{t}}^2 +r_x^2+r_y^2+r_z^2 ,
$$
the four-dimensional Euclidean fundamental solution, verified by parts against a radial test function. The causal kernels are supported on the light cone,
$$
G_{\mathrm{ret}} = \frac{1}{4\pi R}\delta\!\left(r'_t - R\right) , \qquad
G_{\mathrm{adv}} = \frac{1}{4\pi R}\delta\!\left(r'_t + R\right) ,
\qquad
\Box_\Phi G_{\mathrm{ret}} = \Box_\Phi G_{\mathrm{adv}} = -\delta ,
$$
obtained from the light-cone delta with Jacobian $|dg/dr'_t| = 2R$ and selected by the time boundary condition; the Jacobian and the off-cone annihilation of the kernel were verified numerically, and their difference $\mathcal{G}_{\mathrm{PJ}} = G_{\mathrm{ret}} - G_{\mathrm{adv}}$ is the commutator function. The causal kernel is $G_F = (4\pi^2)^{-1}(\rho^2 - i\epsilon)^{-1}$, whose Wick rotation is $G_{\mathrm{inv}}$.

The massive operator $\Box_\Phi - 4\pi^{2}\nu_m^{2}$ has the invariant kernel $\frac{\nu_m}{4\pi^2\rho}\mathrm{Ki}_{1}(\rho\,\nu_m)$, with the massless kernel as its short-distance limit and exponential screening at large distance, and a causal kernel with support inside the cone. The first-order operator has a biquaternion-valued kernel,
$$
\tilde{G}_{\Phi,\tilde\nabla_\Phi} = (\tilde\nabla_\Phi)^{\natural}G_{\Box_\Phi} \in \mathbb{B}_{\Phi} ,
\qquad
\tilde\nabla_\Phi\tilde{G}_{\Phi,\tilde\nabla_\Phi} = -\delta ,
$$
which is material-sector-valued, transforms as a four-vector, and does not commute — the object the Dirac and Maxwell articles invert their equations with. The scalar kernel is central and commutes; the contrast is the algebraic content of the difference between the second-order and first-order relativistic equations.

The shift carried by the first-order operator need not be central. With a constant biquaternion coefficient $f + F$ the mutual shifted gradients compose to
$$
D^+_F D^-_F = D^-_F D^+_F = -\Box_\Phi + 2f\partial/\partial\tau + 2i(F,\vec\nabla_\Phi) + f^2 + (F,F) ,
$$
so the scalar part of the coefficient acts as a mass and the vector part as a direction the operator differentiates along, the corpus's central shift being the case $F = 0$. The kernel is the retarded kernel weighted by $\exp(-f\tau)$ and multiplied by the phase $\exp(\pm i(F,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z))$, the sign of the phase matching the sign of the $(F,\vec\nabla_\Phi)$ coefficient — the source prints the two with opposite signs, and the paired form is the one verified here. Because the phase moves no support, Huygens' principle survives the non-central part; and because a first-order operator with a real coefficient is anti-self-adjoint, the non-central part is self-adjoint for real $F$: it neither buys the Huygens property nor pays for it, and both belong to the scalar part alone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\nabla_\Phi = \sum_{\imath} e_{\imath}\partial/\partial R_{\imath}$ | Biquaternionic gradient, $\partial/\partial R_t = \partial/\partial R_t = -i\partial/\partial r'_t$ |
| $(\tilde\nabla_\Phi)^{\natural} = \sum_{\imath} e_{\imath}^{*}\partial/\partial R_{\imath}$ | Quaternion-conjugate gradient, $(\tilde\nabla_\Phi)^{\natural} = e_t\partial/\partial R_t - \sum_\eta\,\vec e_\eta\partial/\partial R_\eta$ |
| $\Box_\Phi = \tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}= \Delta_\Phi - \partial^2/\partial {r^{\prime}_t}^2$ | Series d'Alembertian; central scalar; $\Box_\Phi \to \omega^2/c^2 - 2\pi\vec\nu_\Phi^2$ |
| $\tilde\nabla_\Phi^{*} = -(\tilde\nabla_\Phi)^{\natural}$, $\Box_\Phi^{*} = \Box_\Phi$ | Adjoints under $\langle\tilde{F},\tilde Q\rangle = \int2\,\mathrm{Sc}(\tilde{F}^{*}\tilde Q)$ |
| $\Box_\Phi^\flat = -\Box_\Phi$, $G_{\Box,\Phi}^\flat = -G_{\Box,\Phi}$, $\tilde{G}_{\Phi,\tilde\nabla_\Phi}^\flat = \tilde{G}_{\Phi,\tilde\nabla_\Phi}$ | Conjugation action on the operator and the kernels: ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ fix a real scalar and $\flat$ negates it; the conjugations preserve the sectors, multiplication by $i$ exchanges them, $i\tilde{G}_{\Phi,\tilde\nabla_\Phi} \in \mathbb{B}_{\Psi}$ |
| $\tilde R_\Phi = i r'_t\,e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ | Material four-position |
| $\rho^2 = \langle\tilde R_\Phi\rangle_{\natural} = -{r'_{t}}^2 +r_x^2+r_y^2+r_z^2$ | Biquaternion norm of the separation; Euclidean four-distance squared |
| $G_{\mathrm{inv}} = \frac{1}{4\pi^2\rho^2}$ | Invariant (Euclidean) kernel; $-\Box_\Phi G_{\mathrm{inv}} = \delta^{(4)}$ |
| $G_{\mathrm{ret}} = \frac{1}{4\pi R}\delta(r'_t - R)$ | Retarded kernel; $\Box_\Phi G_{\mathrm{ret}} = -\delta$ |
| $G_{\mathrm{adv}} = \frac{1}{4\pi R}\delta(r'_t + R)$ | Advanced kernel; $\Box_\Phi G_{\mathrm{adv}} = -\delta$ |
| $\mathcal{G}_{\mathrm{PJ}} = G_{\mathrm{ret}} - G_{\mathrm{adv}}$ | Pauli–Jordan commutator function; $\Box_\Phi\mathcal{G}_{\mathrm{PJ}} = 0$ |
| $G_F = \frac{1}{4\pi^2}\frac{1}{\rho^2 - i\epsilon}$ | Causal (Feynman) kernel; Wick-rotates to $G_{\mathrm{inv}}$ |
| $G^{(1/\nu_m)}_{\mathrm{inv}} = \frac{\nu_m}{4\pi^2\rho}\mathrm{Ki}_{1}(\rho\,\nu_m)$ | Massive invariant kernel; the label $1/\nu_m$ names the massive case, whose coefficient is $\nu_m=\frac{h}{2\pi mc}$ |
| $\tilde{G}_{\Phi,\tilde\nabla_\Phi} = (\tilde\nabla_\Phi)^{\natural}G_{\Box,\Phi} \in \mathbb{B}_{\Phi}$ | First-order kernel; $\tilde\nabla_\Phi\tilde{G}_{\Phi,\tilde\nabla_\Phi} = -\delta$ |
| $\tilde\nabla_\Phi + \kappa$, $\kappa \in \mathbb{C}$ | The shifted gradient, written out; the glyph is never extended |
| $(\tilde\nabla_\Phi+\kappa)((\tilde\nabla_\Phi)^{\natural}+\kappa) = \Box_\Phi - 2i\kappa\,e_t\partial/\partial r'_t + \kappa^2$ | Square of the shifted gradient; symbol $(\omega/c - \kappa)^2 - \|\vec\nu_\Phi\|^2$ |
| $\vec\nabla_{+} = \partial/\partial\tau + i\vec\nabla_\Phi$, $\vec\nabla_{-} = \partial/\partial\tau - i\vec\nabla_\Phi$; $D^{+}_F = \vec\nabla_{+} + f + F$, $D^{-}_F = \vec\nabla_{-} + f - F$ | The source's mutual bigradients and mutual Maxwell–Dirac operators, without the corpus sector mark; $\vec\nabla_{+} = i\tilde\nabla_\Phi$ and $\vec\nabla_{-} = i(\tilde\nabla_\Phi)^{\natural}$, and the non-central shift is the paper's own |
| $D^+_FD^-_F = -\Box_\Phi + 2f\partial/\partial\tau + 2i(F,\vec\nabla_\Phi) + f^2 + (F,F)$ | Square of the mutual MD-operators; the wave operator of the source's time is $-\Box_\Phi$, because $\partial^2/\partial\tau^2-\Delta_\Phi = -\Box_\Phi$ |
| $\tilde{Ξ} = \frac{1}{4\pi r}\exp(\pm i\theta_{\mathrm{spa}})\exp(-\kappa_{\mathrm{dmp}})\delta(\tau-r)$ | Weighted light-cone kernel; the exponent's sign matches the sign of the $(F,\vec\nabla_\Phi)$ coefficient |
| $\mathrm{H}_{\mathrm{hvs}}(r'_t)$ | Step function selecting the future cone |
| $\delta_{\imath\jmath}=(1,1,1,1)$ | The metric, the identity matrix; with $Q_t=i q'_t$ the material interval is $-{r'_{t}}^2+r_x^2+r_y^2+r_z^2$ (not used in $\Box_\Phi$) |

## Further Reading

- George B. Arfken, Hans J. Weber, and Frank E. Harris, *Mathematical Methods for Physicists* (Elsevier, 2013), for the fundamental solutions of the Laplacian and the Helmholtz operator and the distributional identity $\Delta_\Phi r^{2-d} = -(d-2)\frac{2\pi^{d/2}}{\Gamma(d/2)}\delta^{(d)}$.
- N. N. Bogoliubov and D. V. Shirkov, *Introduction to the Theory of Quantized Fields* (Interscience, 1959), for the causal, retarded and advanced Green's functions of the Klein–Gordon operator and the Pauli–Jordan commutator function.
- James D. Bjorken and Sidney D. Drell, *Relativistic Quantum Fields* (McGraw–Hill, 1965), for the four Green's functions of the wave operator, their contour prescriptions, and the Feynman propagator.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the propagators of the scalar, Dirac and Maxwell fields as inverses of their wave operators.
- Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory* (Addison–Wesley, 1995), for the $i\epsilon$ prescription and the relation between the Feynman propagator and the Euclidean Green's function.
- I. M. Gel'fand and G. E. Shilov, *Generalized Functions*, Vol. 1 (Academic Press, 1964), for the distributional calculus of the light-cone delta and the wave-front set of the causal kernels.
- Fritz John, *Plane Waves and Spherical Means Applied to Partial Differential Equations* (Interscience, 1955), for the Hadamard elementary solution and the propagation of the wave operator's singularities on the characteristic cone.
- L. A. Alexeyeva, "Biquaternions algebra and its applications by solving of some theoretical physics equations", *Clifford Analysis, Clifford Algebras and Their Applications* **7** (2012), 19–39 (arXiv:1302.0523), for the shifted gradient, the generalized Maxwell–Dirac equation, the Klein–Gordon–Fock–Schrödinger scalar equation, and the source's generalized Kirchhoff representation.
- L. A. Alexeyeva, "Biquaternionic wave equations and the properties of their generalized solutions", *Differential Equations* **57** (5) (2021) 594–604 (DOI 10.1134/S0012266121050049), for the mutual bigradients, the mutual Maxwell–Dirac operators with a general constant biquaternion structural coefficient, the composition lemma and both of its printed signs, the weighted light-cone kernel and its symbol, the conditions on its shock fronts, the Cauchy problem, and the analogues of the Kirchhoff and Green representation formulas. Three points of the paper are recorded in the article with corrections rather than as printed: the composition lemma's statement carries $-2i(F,\vec\nabla_\Phi)$ where its own derivation, its scalar equation and its Fourier transform carry $+2i(F,\vec\nabla_\Phi)$; the kernel's exponent $-i(F,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)$ pairs with the second of those, not the first; and the structural coefficient must be constant for the closed form to hold.
- L. A. Alexeyeva, "Biquaternion representation of the Dirac equations and bispinor fields", *Journal of Open Systems Evolution Problems* **25** (1–2) (2023), 15–24 (doi:10.26577/JPEOS.2023.v25.i1-2.i2), for the fundamental solution of the shifted operator and its light-cone support, the general solution of the inhomogeneous equation, the harmonic bispinors and their nullity, and the linear dispersion of the plane-wave family.
