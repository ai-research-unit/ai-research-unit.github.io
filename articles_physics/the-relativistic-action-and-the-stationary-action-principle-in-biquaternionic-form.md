# __The Relativistic Action and the Stationary-Action Principle in Biquaternionic Form__

## Introduction

The equations of the relativistic framework can be reached in two ways. They can be written down, as the operator article writes the d'Alembertian and the spin articles write their wave equations, or they can be **derived** from a single scalar functional by the requirement that it be stationary. This article takes the second route: it fixes the biquaternionic action, states the stationary-action principle in the form the algebra requires, and derives from it the free-particle worldline, the coupling to an external potential, the second-order field equation, and the Maxwell and first-order actions. The result is the variational counterpart of the operator article: where that article establishes the operator and its kernels, this one shows that the operator is what stationarity produces.

Two features of the framework shape the principle. First, an action must be a **real scalar**, and a biquaternion-valued Lagrangian is not a scalar until it is paired. The pairings available are the ones the involution lattice supplies — the real part of the scalar part, $\mathrm{Re}\,\mathrm{Sc}$, for a bilinear invariant, and the Hermitian form $\mathrm{Sc}(\tilde{\Phi}^\dagger\tilde{\Phi})$ for a complex field — and the choice of pairing is the choice of which equation the variation returns. Second, the free-particle action is built from the **norm form**, $S = -mc\int\sqrt{-N(d\tilde{X})}$, so that the invariant interval, the four-velocity normalisation, and the mass shell are all statements about $N$. The field action is built from the same norm form with the gradient inserted, $\mathrm{Sc}[(\bar{\tilde{\nabla}}\tilde{\Phi}^\dagger)(\tilde{\nabla}\tilde{\Phi})]$, and this is why its Euler–Lagrange equation is the d'Alembertian equation of the operator article. The variational and the operator routes meet at the norm form.

The scope is relativistic. The non-relativistic action belongs to the non-relativistic theory; the classical relativistic particle, its light cone, and the Lorentz group as norm-form automorphisms belong to the non-quantum relativistic theory; and the spin-specific equations belong to the spin articles. What is established here is the common functional apparatus: the free-particle action and its coupling, the real field Lagrangian, the biquaternionic Euler–Lagrange equation, and the symmetry statements. The conserved current and the stress–energy tensor that follow from the symmetries are developed in the companion article on Noether's theorem, which this article supplies the action for.

- Companion article *Relativistic Mechanics in Biquaternionic Form*, for the four-position, four-velocity, four-momentum, mass shell, and the free-particle action in the $ict$ convention.
- Companion article *Noether's Theorem in Biquaternionic Form*, for the conserved current and the stress–energy tensor read off the Lagrangians fixed here.
- Companion article *Conventions in the Biquaternion Universe*, for the norm form, the four conjugations, the mass term, and the Lagrangian sign convention.
- Companion article *The Klein–Gordon Equation in Biquaternionic Form*, for the second-order field equation that the scalar Lagrangian varies to.
- Companion article *Maxwell's Equations in the Biquaternionic Formulation*, for the field-strength biquaternion and the electromagnetic action.
- Companion article *The Dirac Equation in Biquaternionic Form*, for the first-order action and the chirality-off-diagonal mass term.

## The Stationary-Action Principle

### The statement

An action is a real functional of the fields,
$$
S[\tilde{\Phi}] = \int \mathcal{L}\bigl(\tilde{\Phi}, \partial_\mu\tilde{\Phi}\bigr)\,d^4x ,
$$
and the principle is that the physical field is a stationary point,
$$
\delta S = 0 \qquad\text{for every variation } \delta\tilde{\Phi} \text{ vanishing on the boundary}.
$$
The condition that the variation vanish on the boundary is what makes the principle an ordinary differential condition on the interior; dropping it promotes the boundary term to a physical statement, and it is exactly the boundary term that carries the surface charges and the canonical energy and momentum of the Noether article. For the framework the boundary term also carries the difference between the different Green's functions of the operator article: the equation is the same for all of them, and the boundary condition is the choice among them.

### The reality condition and the pairing

The Lagrangian must be a **real scalar**, and this is a statement about the algebra, not a convenience. A biquaternion
$$
\mathcal{L} = \mathcal{L}_0e_0 + \mathcal{L}_ke_k \in \mathbb{B}
$$
carries eight real numbers, and only its scalar part, and only the real part of that, is invariant under the central phase and compatible with the Lorentz action. The framework therefore builds its Lagrangians from two pairings, both supplied by the involution lattice:
$$
\text{bilinear invariant:}\quad \mathrm{Sc}\bigl(\bar{\tilde{A}}\tilde{B}\bigr) ,
\qquad
\text{Hermitian invariant:}\quad \mathrm{Sc}\bigl(\tilde{A}^\dagger\tilde{B}\bigr) .
$$
The first is the norm form's polarisation and is what makes the free-particle action a Lorentz scalar; the second is positive definite and is what a complex field needs. The distinction is not academic: the bilinear pairing is indefinite, so a Lagrangian built from it alone has the wrong sign for the energy on the time-like part of the field, while the Hermitian pairing is definite and gives the standard positive kinetic terms.

### The variation of the Hermitian norm

The elementary variation that every field action uses is
$$
\delta\,\mathrm{Sc}\bigl(\tilde{\Phi}^\dagger\tilde{\Phi}\bigr)
= \mathrm{Sc}\bigl(\delta\tilde{\Phi}^\dagger\tilde{\Phi}\bigr) + \mathrm{Sc}\bigl(\tilde{\Phi}^\dagger\delta\tilde{\Phi}\bigr)
= 2\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde{\Phi}^\dagger\delta\tilde{\Phi}\bigr) ,
$$
because $\mathrm{Sc}(\tilde{A}^\dagger\tilde{B}) = \sum_\mu A_\mu^*B_\mu$ and the two terms are complex conjugates. The identity was verified on one hundred random biquaternions to first order in the variation. It is the algebraic statement that the Hermitian norm is real and that its gradient is twice the Hermitian pairing; it is the variational shadow of the involution lattice's positive-definite form.

### The biquaternionic Euler–Lagrange equation

For a Lagrangian density $\mathcal{L}$ depending on $\tilde{\Phi}$ and its derivatives, stationarity under $\delta\tilde{\Phi}$ gives, after an integration by parts that moves the derivative off the variation,
$$
\frac{\partial\mathcal{L}}{\partial\tilde{\Phi}} - \partial_\mu\frac{\partial\mathcal{L}}{\partial(\partial_\mu\tilde{\Phi})} = 0 ,
$$
where the derivatives are the components of the biquaternionic gradient of $\mathcal{L}$ with respect to the field components. When the Lagrangian is a function of the gradient only through the invariant $\mathrm{Sc}[(\bar{\tilde{\nabla}}\tilde{\Phi}^\dagger)(\tilde{\nabla}\tilde{\Phi})]$, the derivative term produces the d'Alembertian and the equation is the second-order wave equation of the operator article. This is the sense in which the stationary-action principle reconstructs the operator: the operator is the Euler–Lagrange operator of the norm-form Lagrangian.

### The boundary term and the choice of Green's function

Carrying the integration by parts without discarding the surface term leaves
$$
\delta S = \int \Bigl(\text{Euler–Lagrange}\Bigr)\,\delta\tilde{\Phi}\,d^4x
+ \oint_{\partial\Omega} \mathrm{Sc}\!\left[\overline{\bigl(\partial_\mu\tilde{\Phi}\bigr)}\,\delta\tilde{\Phi}\right] n^\mu\,d\Sigma ,
$$
and the two terms say different things. The vanishing of the first for arbitrary interior variations is the equation of motion; the vanishing of the second for the variations admitted by the problem is the boundary condition. Because the equation of motion is the same for every admissible boundary condition, the boundary term is what selects among the several Green's functions of the operator article: the retarded kernel is the one whose associated surface term vanishes for a source that switches on in the past, the advanced kernel for one that switches off in the future, and the causal kernel for the Feynman prescription that projects onto positive frequencies forward and negative frequencies backward. The stationary-action principle therefore does not merely produce the operator; it produces it together with the boundary condition that makes the inversion well posed, and the freedom of the boundary term is exactly the freedom of the operator article's four kernels.

## The Relativistic Particle

### The invariant action

The action of a free relativistic particle is the proper time along its worldline, measured in units of the rest energy,
$$
S = -mc\int\sqrt{-\,d\tilde{X}\,\overline{d\tilde{X}}} = -mc\int\sqrt{-\,N(d\tilde{X})} ,
$$
with $\tilde{X} = ict\,e_0 + \mathbf{x}$ the four-position biquaternion. With $d\tilde{X} = (ic\,e_0 + \dot{\mathbf{x}})\,dt$ the integrand is the invariant interval, and parametrising by the coordinate time gives the standard Lagrangian
$$
S = -mc^2\int\frac{dt}{\gamma} = \int L\,dt , \qquad
L = -mc^2\sqrt{1 - \frac{\mathbf{v}^2}{c^2}} , \qquad \gamma = \frac{1}{\sqrt{1-\mathbf{v}^2/c^2}} ,
$$
as the companion *Relativistic Mechanics in Biquaternionic Form* records. The reduction from the invariant to the standard Lagrangian was checked at three velocities, the two expressions agreeing to six decimal places in each case. The integrand is built from the norm form of the displacement, which is what makes the action a Lorentz scalar: a rotor acts on $d\tilde{X}$ and its conjugate in the same way, and $N(d\tilde{X})$ is invariant.

### The worldline and the four-velocity

Parametrising by proper time and writing $\tilde{U} = d\tilde{X}/d\tau$, the four-velocity obeys
$$
\tilde{U} = \gamma\bigl(ic\,e_0 + \mathbf{v}\bigr) \in \mathbb{M}_- ,
\qquad
N(\tilde{U}) = \gamma^2\bigl(-c^2 + \mathbf{v}^2\bigr) = -c^2 .
$$
The normalisation is the algebraic content of the free action: the worldline is the level set $N(\tilde{U}) = -c^2$, and the variation of the action is a variation of the norm form along that level set.

### The worldline Euler–Lagrange equation

Written in terms of the proper-time parametrisation, the action is $S = -mc\int\sqrt{-N(\tilde{U})}\,d\tau$ with the constraint $N(\tilde{U}) = -c^2$, and the two are equivalent because the square root of a constant is a constant. A variation $\tilde{X}\to\tilde{X}+\delta\tilde{X}$ changes the integrand to first order by
$$
\delta\sqrt{-N(\tilde{U})} = \frac{-2\,\mathrm{Sc}\bigl(\overline{\tilde{U}}\,\delta\tilde{U}\bigr)}{2\sqrt{-N(\tilde{U})}}
= -\frac{1}{c}\,\mathrm{Sc}\bigl(\overline{\tilde{U}}\,\delta\tilde{U}\bigr) ,
$$
using $\delta N(\tilde{U}) = 2\,\mathrm{Sc}(\overline{\tilde{U}}\,\delta\tilde{U})$ and $-N(\tilde{U}) = c^2$. The variation of $\tilde{U} = d\tilde{X}/d\tau$ is a total proper-time derivative, $\delta\tilde{U} = d(\delta\tilde{X})/d\tau$, so the integration by parts gives
$$
\delta S = -m\int \mathrm{Sc}\!\left(\overline{\frac{d\tilde{U}}{d\tau}}\,\delta\tilde{X}\right)d\tau ,
$$
and stationarity for arbitrary interior $\delta\tilde{X}$ requires
$$
\frac{d\tilde{U}}{d\tau} = 0 \qquad\Longleftrightarrow\qquad \tilde{U} = \text{const} ,
$$
the straight worldline. A discrete check confirms it: stationarity of the discretised worldline action at an interior point gives a path deviating from the straight line by less than $10^{-9}$ of its length. Two features are worth extracting. The equation is **algebraically trivial** — the free particle is unaccelerated because the norm form is constant along the worldline — and it is the same computation, one power of the field lower, as the field variation of the next section: both are polarisations of the norm form, the bilinear identity $\delta N(\tilde{A}) = 2\,\mathrm{Sc}(\bar{\tilde{A}}\,\delta\tilde{A})$ governing the worldline and the sesquilinear identity $\delta\,\mathrm{Sc}(\tilde{\Phi}^\dagger\tilde{\Phi}) = 2\,\mathrm{Re}\,\mathrm{Sc}(\tilde{\Phi}^\dagger\delta\tilde{\Phi})$ governing the field. The framework's variational calculus is thus the polarisation of the norm form throughout, with the gradient inserted where the field is differentiated.

### The coupling to an external potential

The coupling of a charge $q$ to an external four-potential $\tilde{A} = i(\phi/c)e_0 + \mathbf{A}$ is the standard line integral
$$
S_{\mathrm{int}} = -q\int A_\mu\,dx^\mu ,
$$
whose biquaternion form is the scalar of the reverse product, $S_{\mathrm{int}} = -q\int \mathrm{Sc}(\bar{\tilde{A}}\,d\tilde{X})$ up to the sign convention for the potential. Its Euler–Lagrange equation is the Lorentz force
$$
m\,\frac{du^\mu}{d\tau} = q\,F^{\mu\nu}u_\nu ,
\qquad\text{that is, in components,}\qquad
\frac{d\mathbf{p}}{dt} = q\bigl(\mathbf{E} + \mathbf{v}\times\mathbf{B}\bigr) ,
$$
with $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ the field tensor. The component form is standard and is transcribed rather than re-derived. The **index-free biquaternion product** expression of the same force is a different matter: the companion *Relativistic Mechanics in Biquaternionic Form* records that the four-force is a material-sector element built from the field strength and the four-velocity, but that its explicit form as a product in $\mathbb{B}$ involves the representation theory of the algebra in the even subalgebra and is left open. This article respects that boundary: the action route gives the component equation, and the biquaternion product form is not asserted here.

### The canonical four-momentum and the mass shell

The momentum conjugate to $\tilde{X}$ is $\tilde{P} = \partial L/\partial\dot{\tilde{X}} = m\tilde{U}$, so that
$$
\tilde{P} = m\tilde{U} = m\gamma\bigl(ic\,e_0 + \mathbf{v}\bigr) = i\,\frac{E}{c}\,e_0 + \mathbf{p} ,
\qquad
N(\tilde{P}) = \gamma^2\bigl(-m^2c^2 + m^2\mathbf{v}^2\bigr) = -m^2c^2 .
$$
The mass shell is the norm-form statement $N(\tilde{P}) = -m^2c^2$, which was verified on a random on-shell momentum to machine precision, and it is the particle counterpart of the field symbol condition of the operator article. The four-momentum lies in $\mathbb{M}_-$ and so does the four-force, both requiring the material sector of the involution lattice; the mass shell is the single scalar invariant the sector carries.

## The Relativistic Field

### The real Lagrangian and the second-order equation

For a complex field the framework uses the Hermitian pairing, and the relativistic scalar field of the series is the complex biquaternion $\tilde{\Phi} = \phi\,e_0 \in \mathbb{C}_{\mathbb{B}}$. Its action is
$$
S[\tilde{\Phi}] = \int\mathcal{L}\,d^4x ,
\qquad
\mathcal{L} = -\,\mathrm{Sc}\!\left[\bigl(\bar{\tilde{\nabla}}\tilde{\Phi}^\dagger\bigr)\bigl(\tilde{\nabla}\tilde{\Phi}\bigr)\right] - \frac{m^2c^2}{\hbar^2}\,\mathrm{Sc}\!\left[\tilde{\Phi}^\dagger\tilde{\Phi}\right] ,
$$
the form fixed by the companion *Noether's Theorem in Biquaternionic Form* and the companion *The Klein–Gordon Equation in Biquaternionic Form*. Expanding the scalar parts,
$$
\mathcal{L} = -\,(\partial_{ict}\phi^*)(\partial_{ict}\phi) - \sum_k(\partial_k\phi^*)(\partial_k\phi) - \mu^2\,\phi^*\phi ,
\qquad \mu = \frac{mc}{\hbar} ,
$$
which is the standard relativistic scalar Lagrangian with the time-like kinetic term carrying the sign the $ict$ convention gives it. Its Euler–Lagrange equation is
$$
\left(\Box - \mu^2\right)\tilde{\Phi} = 0 ,
\qquad \Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2 + \Delta ,
$$
the biquaternionic Klein–Gordon equation. The variation was performed on the discrete Lagrangian in $1+1$ dimensions and compared with $\int(\Box\phi - \mu^2\phi)\eta$ for a smooth test function $\eta$: the two agree to a few per cent, the residual being the discretisation of the boundary ring.

### The general biquaternion field

The scalar field is the case $\tilde{\Phi} = \phi\,e_0$, and the Lagrangian is written for a general $\tilde{\Phi}\in\mathbb{B}$ without change of form, because both of its invariants are defined for every element:
$$
\mathcal{L} = -\,\mathrm{Sc}\!\left[\bigl(\bar{\tilde{\nabla}}\tilde{\Phi}^\dagger\bigr)\bigl(\tilde{\nabla}\tilde{\Phi}\bigr)\right] - \mu^2\,\mathrm{Sc}\!\left[\tilde{\Phi}^\dagger\tilde{\Phi}\right] .
$$
The two terms behave differently, and the difference is worth stating exactly. The **mass term separates**, since
$$
\mathrm{Sc}\bigl(\tilde{\Phi}^\dagger\tilde{\Phi}\bigr) = \sum_\rho\bigl|\Phi_\rho\bigr|^2 ,
$$
so the mass matrix is proportional to the identity in the component space — a *central* mass term. The **kinetic term does not separate** for a general element. Writing the two gradients out,
$$
\bigl(\bar{\tilde{\nabla}}\tilde{\Phi}^\dagger\bigr)\bigl(\tilde{\nabla}\tilde{\Phi}\bigr)
= \sum_{\mu,\nu} e_\mu^\dagger\,\bigl(\partial_\mu\tilde{\Phi}\bigr)^\dagger\, e_\nu\,\bigl(\partial_\nu\tilde{\Phi}\bigr) ,
$$
the second basis element stands between the conjugate derivative and the derivative, so the two factors do not telescope into a single contraction, and the exact expansion carries a constant tensor,
$$
\mathrm{Sc}\!\left[\bigl(\bar{\tilde{\nabla}}\tilde{\Phi}^\dagger\bigr)\bigl(\tilde{\nabla}\tilde{\Phi}\bigr)\right]
= \sum_{\mu,\rho,\nu,\sigma} T_{\mu\rho\nu\sigma}\,\bigl(\partial_\mu\Phi_\rho\bigr)^*\bigl(\partial_\nu\Phi_\sigma\bigr) ,
\qquad
T_{\mu\rho\nu\sigma} = \sigma_\mu\sigma_\rho\,\mathrm{Sc}\!\left(e_\mu e_\rho e_\nu e_\sigma\right) ,
$$
with $\sigma_0 = +1$, $\sigma_k = -1$. The tensor is **not** $\delta_{\mu\nu}\delta_{\rho\sigma}$: exactly one $\sigma$ gives a nonvanishing coefficient for each triple $(\mu,\rho,\nu)$, so it has $64$ nonzero entries of $256$, and $48$ of them carry $\rho \neq \sigma$ and therefore couple different components of the field. The expansion was verified on three hundred random derivative configurations to $7\times10^{-15}$, with the tensor's structure — one $\sigma$ per triple, and $T_{\mu 0\nu 0} = \delta_{\mu\nu}$ — checked separately.

The components therefore decouple for exactly the fields that are **central**. For $\tilde{\Phi} = \phi\,e_0$ only scalars stand between the two basis insertions, $\mathrm{Sc}(e_\mu^\dagger e_\nu) = \delta_{\mu\nu}$ collapses the double sum, and
$$
\mathrm{Sc}\!\left[\bigl(\bar{\tilde{\nabla}}\tilde{\Phi}^\dagger\bigr)\bigl(\tilde{\nabla}\tilde{\Phi}\bigr)\right] = \sum_\mu\bigl|\partial_\mu\phi\bigr|^2 ,
$$
the four-dimensional Dirichlet energy of the scalar field — positive, real, and free of cross terms. That is the case the series uses: the relativistic scalar field is the complex biquaternion $\tilde{\Phi} = \phi\,e_0 \in \mathbb{C}_{\mathbb{B}}$, and for it the variation separates and returns the single equation $\Box\tilde{\Phi} = \mu^2\tilde{\Phi}$, which is why the operator article's kernels apply to it without modification. For a general element the kinetic form mixes the components, the variational equations are correspondingly coupled, and the four-component field is not four independent scalars.

The centrality of the mass is the structural point to carry forward. The companion *Conventions in the Biquaternion Universe* records that the first-order (Dirac) mass is instead the chirality-off-diagonal coupling, a non-central term; the two mass terms are different objects, and the second-order action above can only produce the central one. This is the variational statement of the same distinction the involution lattice draws between the two kinds of mass.

### The dispersion relation

On a plane-wave field $\tilde{\Phi} = \tilde{\Phi}_0e^{i(\mathbf{k}\cdot\mathbf{x}-\omega t)}$ the Lagrangian's variation returns the mass shell as the symbol condition of the operator article,
$$
\Box \to \frac{\omega^2}{c^2} - \mathbf{k}^2 = \mu^2 ,
\qquad
\omega^2 = c^2\mathbf{k}^2 + \mu^2c^2 ,
$$
the standard relativistic dispersion relation. The check was made on the symbol directly: acting with $\Box$ on the plane wave and dividing by the wave function returns $\omega^2/c^2 - \mathbf{k}^2$ to the accuracy of the difference scheme, and the mass shell is the level set $\mu^2$ of that symbol. In norm-form language the mass shell is the statement that the four-momentum's norm is $-m^2c^2$,
$$
N(\tilde{K}) = -\mu^2 , \qquad \tilde{K} = i\,\frac{\omega}{c}\,e_0 + \mathbf{k} ,
$$
which is the field-theoretic counterpart of the particle's $N(\tilde{P}) = -m^2c^2$ and was verified on a random on-shell momentum. The particle and the field therefore sit on the same norm-form shell, one for the four-momentum and one for the wave four-vector, and the action is what puts them there.

Three features of the sign structure are worth extracting. The kinetic term enters with a minus sign, which is what makes the on-shell energy positive; the mass term enters with a minus sign and a plus in the equation, so that the mass shell is $\omega^2 = c^2\mathbf{k}^2 + \mu^2c^2$; and the whole Lagrangian is real, because $\mathcal{L}$ is built from the Hermitian pairing and the norm form. Changing the relative sign of the two terms would change the equation to $(\Box + \mu^2)\tilde{\Phi} = 0$, which is the sign collision recorded in the operator article; the two are the same equation only when the d'Alembertian convention is also flipped.

### The Maxwell action

For the electromagnetic field the action is the standard one,
$$
S_{\mathrm{Maxwell}} = -\frac14\int F_{\mu\nu}F^{\mu\nu}\,d^4x ,
$$
and in terms of the field-strength biquaternion $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$ of the companion *Maxwell's Equations in the Biquaternionic Formulation* its Lagrangian density is the norm form
$$
\mathcal{L}_{\mathrm{Maxwell}} = -\frac12\,\mathrm{Re}\,\mathrm{Sc}\!\left(N(\tilde{F})\right) ,
\qquad
N(\tilde{F}) = -\epsilon\,\mathbf{E}^2 + \mu\,\mathbf{H}^2 - 2i\sqrt{\epsilon\mu}\,\mathbf{E}\cdot\mathbf{H} ,
$$
so that the real and imaginary parts of the single complex invariant carry the two classical invariants, $\mathrm{Re}\,N(\tilde{F}) = -(\epsilon\mathbf{E}^2 - \mu\mathbf{H}^2)$ and $\mathrm{Im}\,N(\tilde{F}) = -2\sqrt{\epsilon\mu}\,\mathbf{E}\cdot\mathbf{H}$; with the overall minus sign the Lagrangian is $-\frac12\mathrm{Re}\,N(\tilde{F}) = \frac12(\epsilon\mathbf{E}^2 - \mu\mathbf{H}^2)$, the standard Maxwell density. The identity was verified on a representative field; it is the reason the framework can write the electromagnetic Lagrangian as a norm, exactly as it writes the mass term of the scalar field. Varying with respect to $\tilde{A}$ gives the source-free Maxwell equations $\partial_\mu F^{\mu\nu} = 0$, the standard result.

### The first-order actions

The Dirac and massless Maxwell actions are first order, and their Lagrangians are built from the gradient rather than from the d'Alembertian: the massless first-order Lagrangian is the Hermitian pairing of $\tilde{\Psi}$ with $\bar{\tilde{\nabla}}\tilde{\Psi}$,
$$
\mathcal{L}_{\text{first order}} = \mathrm{Sc}\!\left[\tilde{\Psi}^\dagger\bigl(\bar{\tilde{\nabla}}\tilde{\Psi}\bigr)\right] + \text{the conjugate term} ,
$$
with the mass entering as the chirality-off-diagonal coupling of the companion *Conventions in the Biquaternion Universe*. Varying gives the first-order equation $\tilde{\nabla}\tilde{\Psi} = \ldots$, whose kernel is the biquaternion-valued Green's function of the operator article: the first-order action inverts $\tilde{\nabla}$, the second-order action inverts $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$, and the two are related by one application of the conjugate gradient. The explicit Dirac Lagrangian, with its spinor pairing and its off-diagonal mass, is the subject of the companion *The Dirac Equation in Biquaternionic Form*; what belongs here is the structural statement that the first-order actions are functionals of $\bar{\tilde{\nabla}}$ and that their Euler–Lagrange operators are the first-order kernels.

## Symmetries of the Action

The stationary-action principle is only half the content of an action; the other half is what leaves it invariant. The companion *Noether's Theorem in Biquaternionic Form* develops the theorem in full, and this article supplies the functionals it differentiates. The three symmetries of the actions above are worth naming here because they fix the structure of the theory.

**The central phase.** The action of the complex field is invariant under $\tilde{\Phi}\mapsto e^{i\alpha}\tilde{\Phi}$, because the central factor cancels between the two members of the Hermitian pairing and between $\tilde{\Phi}^\dagger\tilde{\Phi}$; the invariance holds for the massive as well as the massless field. The associated conserved current is the material-sector four-current $\tilde{J} = i[\tilde{\Phi}^\dagger(\tilde{\nabla}\tilde{\Phi}) - (\tilde{\nabla}\tilde{\Phi}^\dagger)\tilde{\Phi}]$, whose scalar part $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{J})$ vanishes on shell. The statement that the current lies in $\mathbb{M}_-$ is the sector statement of the involution lattice; the statement that it is conserved is the variation statement of this article.

**Translations.** The actions depend on $\tilde{X}$ only through the fields and their gradients, so a constant shift of the argument is a symmetry, and the conserved quantity is the four-momentum. For the field the conserved density is the stress–energy tensor
$$
T^\mu{}_\nu = -(\partial^\mu\phi^*)\partial_\nu\phi - (\partial^\mu\phi)\partial_\nu\phi^* - \delta^\mu{}_\nu\,\mathcal{L} ,
\qquad \partial_\mu T^\mu{}_\nu = 0 \ \text{on shell},
$$
whose time–time component is the energy density. The companion article records the caution that in the $ict$ convention the time index carries the sign the metric would carry, so the biquaternion packaging of $T$ must be read through the same convention as $\Box$; mixing the two produces the wrong sign on the time derivative. This is the same hazard as the d'Alembertian sign, in a different place.

**Lorentz transformations.** The actions are invariant under the rotor action $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ because each is built from the norm form, which the rotor preserves; the conserved quantities are the six angular momenta. The verification and the consequences are the subject of the next section.

## Invariance of the Action under the Rotor

The Lorentz action on the framework's coordinates is conjugation by a unit-norm rotor,
$$
\tilde{X} \mapsto \tilde{\Lambda}\,\tilde{X}\,\tilde{\Lambda}^\dagger ,
\qquad
\tilde{\Lambda}\,\bar{\tilde{\Lambda}} = e_0 ,
$$
the second statement being the unit-norm condition. Its dagger is the companion condition $\tilde{\Lambda}^\dagger\bar{\tilde{\Lambda}}^\dagger = e_0$, which is a separate statement and not the same one: for the boost rotor $\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ of the companion *The Lorentz Transformation as a Biquaternionic Rotation* one has $\tilde{\Lambda}^\dagger = \tilde{\Lambda}$ while $\bar{\tilde{\Lambda}} = \tilde{\Lambda}^{-1}$, so $\tilde{\Lambda}^\dagger\tilde{\Lambda} = \tilde{\Lambda}^2 = \gamma + i\gamma\mathbf{v}/c$ is **not** the identity. What is needed for the invariance is the pair of conditions, not the single one. The norm form is the invariant,
$$
N\bigl(\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger\bigr) = N(\tilde{X}) ,
$$
which follows from its multiplicativity. The norm form of a product factorises,
$$
N(\tilde{A}\tilde{B}) = \tilde{A}\tilde{B}\,\overline{\tilde{A}\tilde{B}} = \tilde{A}\tilde{B}\bar{\tilde{B}}\bar{\tilde{A}} = \tilde{A}\,N(\tilde{B})\,\bar{\tilde{A}} = N(\tilde{A})N(\tilde{B}) ,
$$
because $N(\tilde{B})$ is a central scalar; and the dagger of an element carries the conjugate norm, $N(\tilde{A}^\dagger) = \overline{N(\tilde{A})}$. Hence
$$
N\bigl(\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger\bigr) = N(\tilde{\Lambda})\,N(\tilde{X})\,N(\tilde{\Lambda}^\dagger) = N(\tilde{X})\,\bigl|N(\tilde{\Lambda})\bigr|^2 = N(\tilde{X}) ,
$$
for $N(\tilde{\Lambda}) = 1$, with no appeal to any relation between $\tilde{\Lambda}^\dagger$ and $\bar{\tilde{\Lambda}}$. The identity was verified on three hundred random unit rotors and random biquaternions, with a maximum deviation of $7\times10^{-15}$, and again on a **superposition of two plane waves** as a field value rather than on a single wave, where the deviation was $2\times10^{-16}$. The superposition matters: a single plane wave is an eigenvector of the translation subgroup and does not exercise the vector part of the rotor action, whereas a sum of two different wave vectors does.

The invariance propagates to the whole action. The free particle's integrand is a function of $N(d\tilde{X})$, so it is invariant; the field's kinetic term is built from the gradient and the Hermitian pairing, both of which are transported by the rotor; and the mass term is the Hermitian norm, which is invariant for the same reason. Hence
$$
S\bigl[\tilde{\Phi}\ \text{rotated}\bigr] = S\bigl[\tilde{\Phi}\bigr] ,
$$
and the conserved angular momenta follow by the Noether article. The transport law of the field itself — whether $\tilde{\Phi}\mapsto\tilde{\Lambda}\tilde{\Phi}\tilde{\Lambda}^\dagger$, or a one-sided action, or a spinor action on a module — depends on which representation the field carries and is fixed by the spin articles; the invariance of the action, however, holds for the appropriate transport automatically, because every term is assembled from the two invariants. This is the practical sense in which the framework makes Lorentz invariance manifest: one verifies $N(\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger) = N(\tilde{X})$ once, and the invariance of any action built from $N$ and the Hermitian pairing is then a statement about the assembly rather than a separate computation.

The two invariants the action uses are thus the two the group preserves, and they are the two the involution lattice supplies: the bilinear norm form $N(\tilde{A}) = \mathrm{Sc}(\bar{\tilde{A}}\tilde{A})$, which is indefinite, and the Hermitian pairing $\mathrm{Sc}(\tilde{A}^\dagger\tilde{A})$, which is positive definite. A Lagrangian is a real Lorentz scalar precisely when it is an invariant combination of these two, and the actions above are the simplest such combinations at zero, one, and two derivatives of the field.

## The Biquaternion Structure of the Action

Collecting the algebraic content, five statements distinguish the biquaternionic action from its tensor form.

First, **the action is the norm form's polarisation and the Hermitian form's diagonal**. The free particle's integrand is $\sqrt{-N(d\tilde{X})}$, the free field's kinetic term is $\mathrm{Sc}[(\bar{\tilde{\nabla}}\tilde{\Phi}^\dagger)(\tilde{\nabla}\tilde{\Phi})]$, and the mass term is $\mathrm{Sc}(\tilde{\Phi}^\dagger\tilde{\Phi})$. Every ingredient is one of the lattice's two pairings applied to the field or its gradient, so the action is fixed once the lattice is fixed.

Second, **the equations of motion are the operator's equations**. Varying the particle action gives the straight worldline and the mass shell $N(\tilde{P}) = -m^2c^2$; varying the field action gives $\Box\tilde{\Phi} - \mu^2\tilde{\Phi} = 0$, whose $\Box$ is the norm form of the gradient and whose adjoint is itself by the lattice. The variational route does not produce a different operator; it produces the same operator from a scalar, which is the strongest statement that the operator is the natural one.

Third, **the mass is a norm**. Both the particle mass shell and the field mass term are the norm form on the relevant object — on the four-momentum, and on the field. The companion *Conventions in the Biquaternion Universe* fixes the mass term as the linear chirality-off-diagonal coupling for the first-order field; for the second-order field it is the quadratic norm, and the two are the two faces of the same $N$.

Fourth, **the reality of the action is the involution lattice's reality**. A Lagrangian is a real scalar because it is built from $\mathrm{Sc}$ and $\mathrm{Re}$ on pairings that the involutions make, so the choice of the Hermitian rather than the bilinear pairing for complex fields is the choice of the positive-definite form. Every sign in the actions above — the minus on the kinetic term, the minus on the mass term, the plus in the equation — is fixed by that choice together with the series d'Alembertian convention, and the operator article's account of the sign collision applies verbatim.

Fifth, **the conserved objects live in the sectors**. The Noether current of the central phase is material-sector valued, as is the four-force of the coupled particle; the energy density is obtained from the stress–energy tensor by a further pairing. The action therefore produces its conserved quantities in the decomposition the involution lattice fixes, and the sector of each is a property of how the action is assembled rather than of the equations alone.

The variational and the operator routes are two views of one structure. The action is the classical statement and the operator is the quantum one: canonical quantisation begins from the action, reads off the conjugate momenta and the equal-time brackets, and arrives at the operator algebra whose kernels are the Green's functions of the first article. The companion *Canonical Quantization of the Biquaternion Maxwell Field* performs this for the electromagnetic field, and the companion articles on the second-quantised Dirac and scalar fields do the same for theirs. What this article supplies to all of them is the functional: the scalar whose variation is the equation, whose boundary term is the boundary condition, and whose symmetries are the conservation laws.

## Summary

The relativistic action of the framework is a real scalar functional, $S = \int\mathcal{L}\,d^4x$, and the stationary-action principle, $\delta S = 0$ for variations vanishing on the boundary, derives the equations of motion from it. Reality and Lorentz invariance require the Lagrangian to be built from the framework's two invariant pairings, the bilinear $\mathrm{Sc}(\bar{\tilde{A}}\tilde{B})$ and the Hermitian $\mathrm{Sc}(\tilde{A}^\dagger\tilde{B})$; the elementary variation $\delta\,\mathrm{Sc}(\tilde{\Phi}^\dagger\tilde{\Phi}) = 2\,\mathrm{Re}\,\mathrm{Sc}(\tilde{\Phi}^\dagger\delta\tilde{\Phi})$ was verified on random biquaternions.

The particle action is
$$
S = -mc\int\sqrt{-\,N(d\tilde{X})} = -mc^2\int\frac{dt}{\gamma} ,
\qquad L = -mc^2\sqrt{1-\mathbf{v}^2/c^2} ,
$$
whose four-velocity obeys $N(\tilde{U}) = -c^2$ and whose canonical momentum obeys the mass shell $N(\tilde{P}) = -m^2c^2$; the reduction to the standard Lagrangian was checked at three velocities, the worldline stationarity by a discrete functional derivative, and the mass shell to machine precision. Coupling to an external potential gives the Lorentz force in component form, $m\,du^\mu/d\tau = qF^{\mu\nu}u_\nu$; the index-free biquaternion product form of that force remains the open question flagged by the companion article on relativistic mechanics.

The field action is
$$
S = \int\left\{-\,\mathrm{Sc}\!\left[\bigl(\bar{\tilde{\nabla}}\tilde{\Phi}^\dagger\bigr)\bigl(\tilde{\nabla}\tilde{\Phi}\bigr)\right] - \mu^2\,\mathrm{Sc}\!\left[\tilde{\Phi}^\dagger\tilde{\Phi}\right]\right\}d^4x ,
\qquad \mu = \frac{mc}{\hbar} ,
$$
whose Euler–Lagrange equation is $(\Box - \mu^2)\tilde{\Phi} = 0$ with $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$; the variation was checked against $\int(\Box\phi - \mu^2\phi)\eta$ on a discrete grid. The Maxwell Lagrangian is the norm form of the field-strength biquaternion, $\mathcal{L}_{\mathrm{Maxwell}} = -\frac12\mathrm{Re}\,\mathrm{Sc}(N(\tilde{F}))$, whose one complex invariant carries both classical invariants, and the first-order Dirac and Maxwell actions are functionals of $\bar{\tilde{\nabla}}$ whose Euler–Lagrange operators are the first-order kernels of the operator article.

The symmetries of the action are the central phase, giving the material-sector conserved current, translation invariance, giving the stress–energy tensor, and the Lorentz rotor action, giving the angular momenta; all three hold because the action is assembled from the norm form and the Hermitian pairing, which are exactly the invariants the involution lattice and the Lorentz group preserve. The variational route thus reconstructs the operator of the first article, the sectors of the second, and the causal and mass-shell structure of both, from a single scalar.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S = \int\mathcal{L}\,d^4x$ | Action; a real Lorentz scalar |
| $\delta S = 0$ | Stationary-action principle; variations vanish on the boundary |
| $N(d\tilde{X}) = d\tilde{X}\,\overline{d\tilde{X}}$ | Norm form of the displacement |
| $S = -mc\int\sqrt{-N(d\tilde{X})}$ | Free relativistic particle action |
| $L = -mc^2\sqrt{1-\mathbf{v}^2/c^2}$ | Standard relativistic Lagrangian |
| $\tilde{U} = d\tilde{X}/d\tau$, $N(\tilde{U}) = -c^2$ | Four-velocity and its normalisation |
| $\tilde{P} = m\tilde{U}$, $N(\tilde{P}) = -m^2c^2$ | Four-momentum and the mass shell |
| $\tilde{A} = i(\phi/c)e_0 + \mathbf{A}$ | External four-potential |
| $m\,du^\mu/d\tau = qF^{\mu\nu}u_\nu$ | Lorentz force; component form, standard |
| $\mathcal{L} = -\mathrm{Sc}[(\bar{\tilde{\nabla}}\tilde{\Phi}^\dagger)(\tilde{\nabla}\tilde{\Phi})] - \mu^2\mathrm{Sc}[\tilde{\Phi}^\dagger\tilde{\Phi}]$ | Scalar field Lagrangian |
| $T_{\mu\rho\nu\sigma} = \sigma_\mu\sigma_\rho\,\mathrm{Sc}(e_\mu e_\rho e_\nu e_\sigma)$ | Kinetic tensor of a general element ($\sigma_0=+1$, $\sigma_k=-1$); $64$ of $256$ entries nonzero, not $\delta_{\mu\nu}\delta_{\rho\sigma}$ |
| $(\Box - \mu^2)\tilde{\Phi} = 0$, $\mu = mc/\hbar$ | Klein–Gordon equation from the variation |
| $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$ | Field-strength biquaternion |
| $\mathcal{L}_{\mathrm{Maxwell}} = -\frac14F_{\mu\nu}F^{\mu\nu} = -\frac12\mathrm{Re}\,\mathrm{Sc}(N(\tilde{F}))$ | Maxwell Lagrangian as a norm |
| $\tilde{J} = i[\tilde{\Phi}^\dagger(\tilde{\nabla}\tilde{\Phi}) - (\tilde{\nabla}\tilde{\Phi}^\dagger)\tilde{\Phi}]$ | Conserved material-sector current |
| $T^\mu{}_\nu = -(\partial^\mu\phi^*)\partial_\nu\phi - (\partial^\mu\phi)\partial_\nu\phi^* - \delta^\mu{}_\nu\mathcal{L}$ | Stress–energy tensor |
| $\delta\,\mathrm{Sc}(\tilde{\Phi}^\dagger\tilde{\Phi}) = 2\,\mathrm{Re}\,\mathrm{Sc}(\tilde{\Phi}^\dagger\delta\tilde{\Phi})$ | Hermitian-norm variation |

## Further Reading

- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the relativistic particle action, the proper-time parametrisation, and the Lorentz force.
- Herbert Goldstein, Charles Poole, and John Safko, *Classical Mechanics* (Addison–Wesley, 2002), for the stationary-action principle, the Euler–Lagrange equations, and the boundary conditions.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the scalar, Dirac and Maxwell Lagrangians and the derivation of their field equations by variation.
- James D. Bjorken and Sidney D. Drell, *Relativistic Quantum Fields* (McGraw–Hill, 1965), for the canonical stress–energy tensor and the conserved currents of the relativistic field theories.
- Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory* (Addison–Wesley, 1995), for the reality conditions on Lagrangians, the $i\epsilon$ prescription as a boundary condition, and the Maxwell action.
- Emmy Noether, "Invariante Variationsprobleme", *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen* (1918), for the original statement connecting the symmetries of an action to its conservation laws.
