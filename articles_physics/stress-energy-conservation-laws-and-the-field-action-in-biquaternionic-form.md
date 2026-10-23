# __Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form__

## Introduction

The preceding articles of this subcategory treat the particle's kinematics, the causal cone, the Lorentz group and its topology. Each of these is a statement about a single object or a single transformation. The present article treats the quantity that ties the objects together under evolution: the **stress–energy tensor**, and the **action** from which both the field equations and the conservation laws follow.

The organizing fact is that in a Lagrangian field theory the stress–energy tensor is not an independent input. It is the Noether current of translation invariance of the action,

$$
S[\psi] = \int \mathcal{L}(\psi,\partial/\partial Q_\mu\,\psi)\,d^4x ,
$$

so that the same action that yields the field equations through the Euler–Lagrange equations also yields the ten components of $T^{\mu\nu}$ through Noether's theorem, and the conservation law

$$
\partial/\partial Q_\mu T^{\mu\nu} = 0
$$

is the on-shell statement of that invariance. The biquaternion framework adds nothing to this logic, but it gives the objects a definite home and makes two constructions explicit: the stress–energy of a biquaternion-valued field is built from the algebra's bilinear form, and the electromagnetic stress–energy is a **bigeneral quaternionic bilinear** in the field-strength biquaternion, with the basis elements of $\mathbb{M}_-$ supplying the two vector directions of the two indices.

Three threads are developed.

- **The field action.** The scalar action whose Euler–Lagrange equation is the biquaternionic Klein–Gordon equation, and the electromagnetic action whose Euler–Lagrange equation is the biquaternionic Maxwell equation. Both are transcribed from standard field theory; the algebra supplies the packaging.
- **The Noether construction.** The general stress–energy of a field, its conservation on shell, and the explicit scalar stress–energy with its positive energy density, verified on a superposition of on-shell modes.
- **The electromagnetic tensor as a bigeneral quaternionic bilinear.** The construction $T^\mu{}_\nu = \tfrac12\mathrm{Sc}(\tilde{F}\mathcal{E}_\mu\tilde{F}^{*}\mathcal{E}_\nu)$, its component table, its symmetry, its tracelessness, and its conservation, including the source term that couples it to matter.

$$
\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \partial^2/\partial Q_t^2+\Delta .
$$

The biquaternion norm is $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}=\sum_\mu Q_\mu^2$ — level 1, the identity $\mathrm{diag}(+1,+1,+1,+1)$ on $\mathbb{C}$ — and its restriction to the real material slice is the level-2 form $\eta=\mathrm{diag}(-1,+1,+1,+1)$. The scalar mass parameter is $\mu = mc/\hbar$, so that the scalar equation is $(\Box-\mu^2)\tilde{\Phi}=0$, matching the companion article *The Klein–Gordon Equation in Biquaternionic Form*. The field strength is $\tilde{F}=i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H$, the source is $\sqrt{\mu}\,\tilde{J}=\frac{i\rho}{\sqrt{\epsilon}}e_t+\sqrt{\mu}\,\vec J$, and the Maxwell equation is $\tilde{\nabla}\tilde{F}=-\sqrt{\mu}\,\tilde{J}$, all as fixed in the companion article *Maxwell's Equations in the Biquaternionic Formulation*. The energy density is $W=\tfrac12(\epsilon\vec E^2+\mu\vec H^2)$ and the Poynting vector is $\vec S=\vec E\times\vec H$. The trace formula is $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2) = 2\langle\tilde Q_1,\tilde Q_2\rangle$. Throughout, $c=1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ its vacuum value.

**A sign warning.** As in the companion exercise *Exercise: The Electromagnetic Energy–Momentum Tensor*, the mixed component $T^0{}_0$ carries a sign in the $ict'$ convention: for the electromagnetic field $T^0{}_0=-W$, while the physical energy density is $T^{tt}=W$. This article keeps the same convention for the scalar field and states it at each tensor, so that the two fields can be compared without a sign discrepancy.

## The Field Action in Biquaternion Form

The action of a field theory is a functional of the field and its first derivatives,

$$
S = \int \mathcal{L}(\psi,\partial/\partial Q_\mu\,\psi)\,d^4x ,
\qquad
d^4x = c\,dt'\,dx\,dy\,dz ,
$$

and the field equation is its stationarity condition. For each field component $\psi_a$ the **Euler–Lagrange equation** is

$$
\frac{\partial\mathcal{L}}{\partial\psi_a}
- \partial/\partial Q_\mu\,\frac{\partial\mathcal{L}}{\partial(\partial/\partial Q_\mu\,\psi_a)} = 0 ,
$$

and the statement that a continuous transformation of the field leaves $S$ unchanged yields a **conserved current** by Noether's theorem. The framework adds no new principle here; it supplies the algebra in which the fields are written, and, as the next two subsections show, the equations come out in the biquaternionic forms already fixed by the companion articles.

### The Scalar Action

Let $\tilde{\Phi}$ be a biquaternion-valued field and take the Lagrangian density

$$
\boxed{\ \mathcal{L}_\phi = -\tfrac12\sum_\mu\partial/\partial Q_\mu\,\tilde{\Phi}\,\partial/\partial Q_\mu\,\tilde{\Phi}^{\natural} - \tfrac12\mu^2\,\tilde{\Phi}\tilde{\Phi}^{\natural}\ } ,
\qquad
\mu = \frac{mc}{\hbar} .
$$

Because $\Box$ is central and scalar, the field decomposes into its four components and the Euler–Lagrange equation is componentwise the scalar equation. For a real scalar component $\phi$ the variation gives

$$
\Box\phi - \mu^2\phi = 0 ,
$$

that is,

$$
\left(\Box-\mu^2\right)\tilde{\Phi} = 0 ,
$$

the biquaternionic Klein–Gordon equation of the companion article. The overall sign of $\mathcal{L}_\phi$ is fixed by the requirement that the energy be positive, as the stress–energy section shows; in the corpus's level-2 signature, the kinetic term of $\mathcal{L}_\phi$ written in coordinates is

$$
\mathcal{L}_\phi = -\tfrac12\left(-\frac{1}{c^2}\left(\partial\phi/\partial t'\right)^{2}+(\nabla\phi)^2\right)-\tfrac12\mu^2\phi^2
= \frac{1}{2c^2}\left(\partial\phi/\partial t'\right)^{2}-\frac12(\nabla\phi)^2-\frac12\mu^2\phi^2 ,
$$

and it is this sign that makes the energy density of the next section positive. A complex scalar field, equivalently two real scalar fields, carries the doubling that the Klein–Gordon article records.

### The Electromagnetic Action

For the field strength $F_{\mu\nu}=\partial/\partial Q_\mu A_\nu-\partial/\partial Q_\nu A_\mu$ the free action is

$$
S_{\mathrm{em}} = -\frac14\int F_{\mu\nu}F^{\mu\nu}\,d^4x ,
\qquad
F_{\mu\nu}F^{\mu\nu} = 2\mu\,\mathrm{Re}\,\langle\tilde{F}\rangle_{\natural} ,
$$

the second equality being the statement, established in the companion article *The Field-Strength Biquaternion and Its Invariants*, that the two Lorentz invariants of the free field are the real and imaginary parts of the biquaternion norm $\langle\tilde{F}\rangle_{\natural} = \langle\tilde{F},\tilde{F}\rangle_{\natural}=\sum_kF_k^2$. Varying with respect to $A_\nu$ gives the source-free Maxwell equation

$$
\partial/\partial Q_\mu F^{\mu\nu} = 0 ,
$$

and adding the minimal-coupling term $S_{\mathrm{int}}=-\int A_\nu J^\nu\,d^4x$ with the four-current $J^\nu=(\rho c,\vec J)$ gives the inhomogeneous Maxwell equations, whose biquaternion form is the single equation

$$
\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J},
\qquad
\tilde J = ic\rho\,e_t+\vec J,
\qquad
\sqrt{\mu}\,\mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde{J}\right)=0 ,
$$

the form fixed in the companion article *Maxwell's Equations in the Biquaternionic Formulation*. Its content is exactly the four component equations together with the integrability condition $\sqrt{\mu}\,\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J})=0$, equivalent to charge conservation.

The two actions exhibit the same pattern. The kinetic term is the biquaternion norm of the derivative, $-\tfrac12\sum_\mu\partial/\partial Q_\mu\,\tilde{\Phi}\,\partial/\partial Q_\mu\,\tilde{\Phi}^{\natural}$ for the scalar and $-\tfrac14 F_{\mu\nu}F^{\mu\nu}\propto \langle\tilde{F}\rangle_{\natural}$ for the electromagnetic field; the equation of motion is the vanishing of the appropriate first-order or second-order operator; and the conservation of the source current is the integrability condition of the equation, not a separate law.

## Noether's Theorem and the Stress–Energy of Translation

The stress–energy tensor is the Noether current of invariance under spacetime translations. Under an infinitesimal translation $x^\mu\to x^\mu+\epsilon^\mu$ a Lagrangian that depends on $x$ only through the fields changes by

$$
\delta\mathcal{L} = \epsilon^\nu\partial/\partial Q_\nu\,\mathcal{L}
= \epsilon^\nu\partial/\partial Q_\mu\,\left(\frac{\partial\mathcal{L}}{\partial(\partial/\partial Q_\mu\,\psi_a)}\partial/\partial Q_\nu\,\psi_a\right),
$$

where the second equality uses the Euler–Lagrange equation to replace the derivative with respect to $\psi_a$. Bringing the Lagrangian term to the left gives the divergence of the **canonical stress–energy tensor**

$$
T^\mu{}_\nu = \sum_a \frac{\partial\mathcal{L}}{\partial(\partial/\partial Q_\mu\,\psi_a)}\,\partial/\partial Q_\nu\,\psi_a - \delta^\mu_\nu\,\mathcal{L},
\qquad
\partial/\partial Q_\mu T^\mu{}_\nu = 0 \ \text{on shell} .
$$

The four conserved quantities are the components of energy–momentum (from $\nu=0$); the six components of angular momentum follow from Lorentz invariance once the tensor is improved to a symmetric form. The biquaternion framework's contribution is not to this derivation but to the interpretation of the result: for a field whose values lie in $\mathbb{B}$, the sum over components makes $T^\mu{}_\nu$ the bilinear of the field with its conjugate, and for the electromagnetic field the bilinear has a closed algebraic form.

**Symmetry and improvement.** The canonical tensor need not be symmetric or gauge invariant; the physical stress–energy is obtained by adding a divergence of an antisymmetric tensor, which does not change the conserved charges. For the electromagnetic field the improved tensor is symmetric and gauge invariant, and it is the one constructed in the next sections. For a single real scalar the canonical tensor is already symmetric. The improvement is standard and is recorded here because the bigeneral quaternionic bilinear automatically gives the improved form.

**Overall sign.** The canonical tensor is defined up to an overall sign by the sign of the Lagrangian, and this article follows the convention of the companion exercise: the tensor is taken with the sign that makes the physical energy density positive, $T^{tt}>0$, which for the electromagnetic field means $T^0{}_0=-T^{tt}=-W$. Since an overall factor does not affect $\partial/\partial Q_\mu T^{\mu\nu}=0$, the conservation law is unaltered.

## The Scalar Field Stress–Energy

For a real scalar field with the Lagrangian $\mathcal{L}_\phi$ of the previous section, the conserved, symmetric stress–energy tensor with positive energy is

$$
\boxed{\ T_{\mu\nu} = \partial/\partial Q_\mu\,\phi\,\partial/\partial Q_\nu\,\phi + \eta_{\mu\nu}\mathcal{L}_\phi\ } ,
$$

the sign being the one that makes $T_{tt}>0$; the canonical Noether tensor is the negative of this expression, and the two differ only by the overall sign just discussed. Its components are, with $\eta=\mathrm{diag}(-1,+1,+1,+1)$ and $x^0=ct'$,

$$
\boxed{\ T^{tt} = T_{tt} = \frac{1}{2c^2}\left(\partial\phi/\partial t'\right)^{2} + \frac12(\nabla\phi)^2 + \frac12\mu^2\phi^2 > 0\ } ,
$$

$$
T^{tk} = T^{kt} = -\frac{1}{c}\,\partial\phi/\partial t'\,\partial/\partial Q_k\,\phi ,
\qquad
T^{jk} = T_{jk} = \partial/\partial Q_j\,\phi\,\partial/\partial Q_k\,\phi
+ \delta_{jk}\left(\frac{1}{2c^2}\left(\partial\phi/\partial t'\right)^{2}-\frac12(\nabla\phi)^2-\frac12\mu^2\phi^2\right) .
$$

For a right-moving massless wave, $\phi=f(x-ct')$, these reduce to $T^{tt}=T^{xx}=(\partial\phi/\partial x)^2$ and $T^{tx}=T^{tt}$, the null-field pattern of a single traveling wave.

The energy density is manifestly positive: it is the sum of three squares, one for the kinetic term, one for the gradient, and one for the mass. The conservation law

$$
\partial^\mu T_{\mu\nu} = 0
\qquad\text{on shell}
$$

is the statement that the four-momentum

$$
P_\nu = \frac{1}{c}\int T_{t\nu}\,d^3x
$$

is time-independent, which follows by integrating the conservation law over a spatial volume and using the vanishing of the flux at infinity.

As a check, consider the superposition

$$
\phi(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t') = \cos\!\left(k_1x-\omega_1t'\right) + 0.6\cos\!\left(k_2y-\omega_2t'\right),
\qquad
\vec k_1 = (1.1,0,0),
\quad
\vec k_2 = (0,0.9,0),
\quad
\mu = 1.3,
$$

with $\omega_i^2 = \vec k_i^2+\mu^2$ for each mode, so that each mode is on shell and the two are on shell simultaneously. Evaluating $\partial^\mu T_{\mu\nu}$ by second-order finite differences with step $10^{-3}$ at the event $t'=0.7$, $(x,y,z)=(0.3,-0.5,0.2)$ gave residuals of order $10^{-6}$ for all four $\nu$, which is the discretisation error $O(h^2)$; the energy density at the same event was $T^{tt}=3.37>0$. The cross terms between the two modes, which are the content of the check, cancel as they must for a conserved bilinear of on-shell fields.

## The Electromagnetic Stress–Energy as a Bigeneral quaternionic Bilinear

For the electromagnetic field the improved stress–energy tensor has a closed algebraic form in the biquaternion algebra. With the material basis $\mathcal{E}_\mu\in\{ie_t,\vec e_x,\vec e_y,\vec e_z\}$,

$$
\boxed{\;
T^\mu{}_\nu = \frac12\,\mathrm{Sc}\!\left(\tilde{F}\,\mathcal{E}_\mu\,\tilde{F}^{*}\,\mathcal{E}_\nu\right)
= \frac14\,\mathrm{Tr}\!\left(\tilde{F}\,\mathcal{E}_\mu\,\tilde{F}^{*}\,\mathcal{E}_\nu\right) \;}
$$

The two factors of $\mathcal{E}$ are what turn one biquaternion into a rank-two object: each supplies one vector direction, and the scalar part reads off the component. The construction is that of the companion exercise *Exercise: The Electromagnetic Energy–Momentum Tensor*, and its components are

$$
T^0{}_0 = -W,
\qquad
T^0{}_j = \frac{1}{c}S_j,
\qquad
T^j{}_0 = -\frac{1}{c}S_j,
\qquad
T^j{}_k = -\sigma_{jk},
$$

with the Maxwell stress

$$
\sigma_{jk} = \epsilon\,E_jE_k + \mu\,H_jH_k - W\,\delta_{jk},
\qquad
W = \tfrac12\left(\epsilon\vec E^2+\mu\vec H^2\right),
\qquad
\vec S = \vec E\times\vec H.
$$

Contracting the second slot with $\eta=\mathrm{diag}(-1,+1,+1,+1)$ gives the symmetric tensor

$$
T^{tt} = W,
\qquad
T^{tj} = T^{jt} = \frac{1}{c}S_j,
\qquad
T^{jk} = -\sigma_{jk} = W\delta_{jk}-\epsilon E_jE_k-\mu H_jH_k ,
$$

which is the standard electromagnetic energy–momentum tensor in a medium: $W$ is the energy density, $\tfrac1c\vec S$ is the energy flux and (times $c$) the momentum density, and $-\sigma_{jk}$ is the momentum flux. The mixed tensor is deliberately not symmetric; the asymmetry is exactly the metric factor between the energy flux and the momentum density, and it disappears once the metric contraction is made.

**Tracelessness.** The trace in the Minkowski pairing is

$$
\eta_{\mu\nu}T^{\mu\nu} = -T^{tt}+T^{kk} = -W - \sigma_{kk} = -W + W = 0 ,
$$

because $\sigma_{kk} = \epsilon\vec E^2+\mu\vec H^2-3W = 2W-3W=-W$. The tensor is traceless in the medium as well as in vacuum, and that is the classical statement that the source-free theory is invariant under the conformal rescaling of the metric.

**Conservation.** The divergence of the tensor is the Lorentz four-force density. The tensor is defined by

$$
T^{\mu}{}_\nu = \tfrac12\,\mathrm{Sc}\!\left(\tilde F\,\mathcal E_\mu\,\tilde F^{*}\,\mathcal E_\nu\right) ,
\qquad
T^{\mu\nu} = \eta^{\nu\beta}T^{\mu}{}_\beta ,
$$

the definition being exact over the field algebra up to the factors the $ict'$ basis elements carry. In the coordinates of the framework, $Q_t=ict'$ and $Q_k=q_k$, so $\partial/\partial Q_t=-\frac{i}{c}\partial/\partial t'$, and the divergence is

$$
\partial_\mu T^{\mu\nu}
= \sum_{\mu\in\{t,x,y,z\}}\frac{\partial}{\partial Q_\mu}\,T^{\mu\nu} ,
$$

which is the component law

$$
\frac{\partial}{\partial Q_\mu}\,T^{\mu\nu} = -f^\nu ,
\qquad
f^\nu = \left(\frac{1}{c}\vec E\cdot\vec J,\ \rho\vec E+\vec J\times\vec B\right),
$$

so that the source-free field has $\partial_\mu T^{\mu\nu}=0$ and in the presence of charges the field momentum is exchanged with the matter at the rate given by the Lorentz force. The companion article *The Lorentz Force in Biquaternion Form* treats the matter side of the exchange.

The identity was verified off shell: for random arbitrary fields the divergence reproduces $\partial/\partial Q_\mu T^{\mu\nu}$ to machine precision, ratio exactly one, for all four $\nu$. The source-free case was then checked on shell: on random superpositions of one to three transverse plane waves with $\omega_i=c|\vec k_i|$, $c=1$, $\epsilon=\mu=1$, at random events, second-order finite differences with step $10^{-5}$ give $|\partial_\mu T^{\mu\nu}|$ below $10^{-9}$ against tensor elements of order unity, at the discretisation floor, for all four $\nu$ — conservation for the interacting cross terms and not merely mode by mode.

**The reading is decisive.** It is the **plain** derivative, and the projection is the plain $e_\mu$, not the conjugated $e_\mu^{\natural}$. Scalar parts are blind to the conjugation, but the spatial basis elements are not, since $e_k^{\natural}=-\vec e_k$; the conjugated contraction is a different combination, it does not reproduce $\partial/\partial Q_\mu T^{\mu\nu}$, and on the same on-shell fields it stays at the scale of the tensor itself instead of vanishing. The conjugation is the right operation for the framework's four-vector currents, where $\mathrm{Sc}(\tilde\nabla^{\natural}\tilde J)$ is the divergence; for the rank-two tensor the plain derivative is what carries it.

**Where the algebra enters.** The bilinear form realizes the two-index object by the two inserted basis elements; the scalar projection extracts the component. This is why the natural object is the mixed tensor $T^\mu{}_\nu$ and not a doubly covariant one, and why one vector direction at a time is what the bilinear carries — the four-component object $\tilde{W}=\tfrac12\tilde{F}\tilde{F}^{*}$ carries only the time row, as the exercise shows, whereas fixing $\nu$ selects the four entries $T^{\mu}{}_\nu$. The rank-two object with two independent vector directions is the smallest algebraic structure that holds all the components, and the algebra supplies it through the bilinear rather than through a new field. The divergence of the row is then the plain derivative $\partial_\mu T^{\mu\nu}$, and it is that divergence which vanishes.

## The Conservation Law for Field and Matter

The conservation law of the preceding section is not closed: the field's four-momentum changes in the presence of charges. The total energy–momentum of field and matter,

$$
T^{\mu\nu}_{\mathrm{tot}} = T^{\mu\nu}_{\mathrm{em}} + T^{\mu\nu}_{\mathrm{matter}} ,
$$

is conserved. The matter tensor of a pressureless dust of proper density $n$ and four-velocity $\tilde{V}$ is the tensor form of the particle flux,

$$
T^{\mu\nu}_{\mathrm{matter}} = m\,n\,v^\mu v^\nu ,
\qquad
m = \text{particle mass},
$$

whose divergence is the negative of the field's:

$$
\partial/\partial Q_\mu T^{\mu\nu}_{\mathrm{matter}} = +f^\nu
\qquad\Longleftrightarrow\qquad
\partial/\partial Q_\mu T^{\mu\nu}_{\mathrm{tot}} = 0 .
$$

The component $\nu=0$ of this statement is the **Poynting theorem**,

$$
\partial/\partial t' W + \nabla\cdot\vec S + \vec E\cdot\vec J = 0 ,
$$

the $\nu=k$ components are the momentum-balance equations that underlie radiation pressure, and the biquaternionic form of the whole statement is the single equation

$$
\mathrm{Sc}\!\left(\tilde{\nabla}\tilde{W}\right) = \frac{i}{c}\,\vec J\cdot\vec E
$$

for the Hermitian form $\tilde{W}=\tfrac12\tilde{F}\tilde{F}^{*}$, which the companion article *Maxwell's Equations in the Biquaternionic Formulation* derives and the exercise re-derives by contrast with the failed real form. The pattern is general: the divergence of the field's stress–energy equals minus the four-force density, the divergence of the matter's tensor equals plus it, and the sum is conserved. The field action is what fixes both the field tensor and, through the coupling term, the force that appears on the matter side.

## What the Algebra Supplies and What Is Transcribed

**Supplied by the algebra.** The bigeneral quaternionic bilinear form of the electromagnetic stress–energy, $T^\mu{}_\nu=\tfrac12\mathrm{Sc}(\tilde{F}\mathcal{E}_\mu\tilde{F}^{*}\mathcal{E}_\nu)$, with the basis elements of $\mathbb{M}_-$ supplying the two index directions; the identification of the free-field Lagrangian with the biquaternion norm of the field strength, $\tfrac14F_{\mu\nu}F^{\mu\nu}\propto\mathrm{Re}\,\langle\tilde{F}\rangle_{\natural}$, so that the action is built from the same biquaternion norm that defines the cone; the packaging of the scalar action, whose equation is the biquaternionic Klein–Gordon equation because $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}$ is central and scalar; and the interchange law of the divergence, field action and conserved current that lets the divergence of the field tensor be read as the source term of the matter.

**Standard field theory transcribed.** The Euler–Lagrange equations, Noether's theorem, the canonical stress–energy tensor, its improvement to a symmetric gauge-invariant form, the positivity of the scalar energy, the Poynting theorem and the Lorentz four-force are standard. The algebra reproduces them in its own notation; it does not add a conservation law or modify one.

**Interpretation.** The interpretation of the bilinear as an element whose Hermitian part is a positive energy density, and of the algebra's basis elements as the index directions, is the framework's structural interpretation; the tensor components themselves are the standard ones. The one genuinely algebraic statement is that the free Lagrangians of the scalar and electromagnetic fields are both the biquaternion norm of their respective objects — the derivative for the scalar and the field strength for the gauge field — so that the action and the causal cone are constructed from the same quadratic form.

## Open Questions

1. **The gravitational coupling.** The stress–energy tensor is the source of gravity in any theory that couples gravity to matter. The framework so far is flat; whether the biquaternion algebra, whose biquaternion norm supplies the flat metric, can carry a dynamical metric in which $T^{\mu\nu}$ acts as source is the same open question the foundational articles record for curved spacetime.

2. **The scalar field's trace and conformal coupling.** The free electromagnetic tensor is traceless, and the free massless scalar tensor is not. The framework does not by itself distinguish the conformal coupling of the scalar; whether the algebra's structure prefers the conformally coupled scalar, whose tensor is traceless in four dimensions, is not settled here.

3. **The biquaternion packaging of the general tensor.** A rank-two tensor has ten independent components; a biquaternion has eight real dimensions. The bilinear construction solves the counting by using two basis-vector insertions, but the general classification of which biquaternion-valued bilinears produce which tensors is not developed in this article.

4. **The medium and the action.** The speed $c=1/\sqrt{\epsilon\mu}$ is local. The action written here treats $\epsilon$ and $\mu$ as constants; a dispersive medium would require a non-local action and would change both the conservation law and the tensor. The framework's treatment of a varying medium is an open question shared with the foundational article on the local complex structure.

5. **Conserved currents of the other symmetries.** Translation invariance gives the stress–energy; Lorentz invariance gives the angular-momentum tensor, and the internal symmetries of a complex scalar field give the vector current. A systematic biquaternionic account of all the Noether currents of these theories, and of their algebra, is left to the companion article *Noether's Theorem in Biquaternionic Form* and beyond it.

The conventions of the construction are those of the following companion articles:

- Companion article *Conventions in the Biquaternion Universe*, for the algebra and basis, the conjugations, the real subspaces, the metric levels and the d'Alembertian.
- Companion article *The Klein–Gordon Equation in Biquaternionic Form*, for the scalar equation and its mass parameter.
- Companion article *Maxwell's Equations in the Biquaternionic Formulation*, for the field strength, the four-current and the biquaternion Maxwell equation.
- Companion article *The Field-Strength Biquaternion and Its Invariants*, for the biquaternion norm of the field strength and the Lorentz invariants.
- Companion article *Exercise: The Electromagnetic Energy–Momentum Tensor*, for the bigeneral quaternionic bilinear form of the tensor and its component table.
- Companion article *The Lorentz Force in Biquaternion Form*, for the matter side of the field–matter exchange.
- Companion article *Noether's Theorem in Biquaternionic Form*, for the general construction of the conserved currents.

## Summary

The action of a field theory yields both its equations of motion and, by Noether's theorem, its conserved stress–energy. In biquaternion form the scalar action

$$
\mathcal{L}_\phi = -\tfrac12\sum_\mu\partial/\partial Q_\mu\,\tilde{\Phi}\,\partial/\partial Q_\mu\,\tilde{\Phi}^{\natural}-\tfrac12\mu^2\tilde{\Phi}\tilde{\Phi}^{\natural},
\qquad
\mu=\frac{mc}{\hbar},
$$

has the Euler–Lagrange equation $(\Box-\mu^2)\tilde{\Phi}=0$, and the electromagnetic action

$$
S_{\mathrm{em}} = -\frac14\int F_{\mu\nu}F^{\mu\nu}\,d^4x ,
\qquad
F_{\mu\nu}F^{\mu\nu} = 2\mu\,\mathrm{Re}\,\langle\tilde{F}\rangle_{\natural},
$$

has the equation $\tilde{\nabla}\tilde{F}=-\sqrt{\mu}\,\tilde{J}$, with $\tilde J=ic\rho\,e_t+\vec J$. The translation Noether current is the canonical tensor $T^\mu{}_\nu=\sum_a\frac{\partial\mathcal{L}}{\partial(\partial/\partial Q_\mu\,\psi_a)}\partial/\partial Q_\nu\,\psi_a-\delta^\mu_\nu\mathcal{L}$, conserved on shell, taken with the overall sign that makes $T^{tt}>0$.

The scalar stress–energy is $T_{\mu\nu}=\partial/\partial Q_\mu\,\phi\partial/\partial Q_\nu\,\phi+\eta_{\mu\nu}\mathcal{L}_\phi$, with

$$
T_{tt}=T^{tt}=\frac{1}{2c^2}\left(\partial\phi/\partial t'\right)^{2}+\frac12(\nabla\phi)^2+\frac12\mu^2\phi^2>0,
\qquad
\partial^\mu T_{\mu\nu}=0 \ \text{on shell},
$$

verified on a superposition of two on-shell modes. The electromagnetic tensor is the bigeneral quaternionic bilinear

$$
T^\mu{}_\nu = \frac12\,\mathrm{Sc}\!\left(\tilde{F}\mathcal{E}_\mu\tilde{F}^{*}\mathcal{E}_\nu\right),
\qquad
T^{tt}=W,
\quad
T^{tj}=\frac1cS_j,
\quad
T^{jk}=W\delta_{jk}-\epsilon E_jE_k-\mu H_jH_k ,
$$

symmetric once contracted with the metric, traceless in the Minkowski pairing, and conserved source-free — all verified by direct computation and by a superposition of two plane waves. With matter included, $\partial/\partial Q_\mu T^{\mu\nu}_{\mathrm{em}}=-f^\nu$ and $\partial/\partial Q_\mu T^{\mu\nu}_{\mathrm{matter}}=+f^\nu$, so the total tensor is conserved; the $\nu=0$ component is the Poynting theorem. The same action that defines the fields and the causal cone of the algebra defines the bookkeeping of their energy and momentum.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra; $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_\mu^2=-e_t$; central $i$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathcal{E}_\mu\in\{ie_t,\vec e_x,\vec e_y,\vec e_z\}$ | Basis of $\mathbb{M}_-$; supplies the tensor index directions |
| $\tilde{\nabla},\tilde{\nabla}^{\natural}$, $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}=\partial^2/\partial Q_t^2+\Delta$ | Gradient, conjugate gradient, d'Alembertian |
| $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}=\sum_\mu Q_\mu^2$ | Biquaternion norm; level-1 identity on $\mathbb{C}$ |
| $\eta=\mathrm{diag}(-1,+1,+1,+1)$ | Level-2 $ict'$-coordinate metric |
| $S=\int\mathcal{L}\,d^4x$ | Action; $\mathcal{L}$ the Lagrangian density |
| $\mathcal{L}_\phi=-\tfrac12\sum_\mu\partial/\partial Q_\mu\,\tilde{\Phi}\,\partial/\partial Q_\mu\,\tilde{\Phi}^{\natural}-\tfrac12\mu^2\tilde{\Phi}\tilde{\Phi}^{\natural}$ | Scalar Lagrangian |
| $\mu=mc/\hbar$ | Scalar mass parameter |
| $(\Box-\mu^2)\tilde{\Phi}=0$ | Biquaternionic Klein–Gordon equation |
| $F_{\mu\nu}=\partial/\partial Q_\mu A_\nu-\partial/\partial Q_\nu A_\mu$; $\tilde{F}=i\sqrt{\epsilon}\vec E-\sqrt{\mu}\vec H$ | Field strength |
| $S_{\mathrm{em}}=-\frac14\int F_{\mu\nu}F^{\mu\nu}d^4x$ | Electromagnetic action |
| $\tilde J=ic\rho\,e_t+\vec J$; $\tilde{\nabla}\tilde{F}=-\sqrt{\mu}\,\tilde{J}$ | Biquaternionic Maxwell system |
| $W=\tfrac12(\epsilon\vec E^2+\mu\vec H^2)$; $\vec S=\vec E\times\vec H$ | Energy density; Poynting vector |
| $\sigma_{jk}=\epsilon E_jE_k+\mu H_jH_k-W\delta_{jk}$ | Maxwell stress |
| $T^\mu{}_\nu=\tfrac12\mathrm{Sc}(\tilde{F}\mathcal{E}_\mu\tilde{F}^{*}\mathcal{E}_\nu)$ | Electromagnetic stress–energy, bigeneral quaternionic bilinear |
| $T^0{}_0=-W$, $T^0{}_j=\frac1cS_j$, $T^j{}_0=-\frac1cS_j$, $T^j{}_k=-\sigma_{jk}$ | Mixed components |
| $T^{tt}=W$, $T^{tj}=T^{jt}=\frac1cS_j$, $T^{jk}=-\sigma_{jk}$ | Symmetric components, after contraction with $\eta$ |
| $\eta_{\mu\nu}T^{\mu\nu}=-T^{tt}+T^{kk}=0$ | Tracelessness (Minkowski pairing) |
| $\partial_{Q_\mu}T^{\mu\nu}=-f^\nu$, $T^{\mu}{}_\nu=\tfrac12\mathrm{Sc}(\tilde F\mathcal{E}_\mu\tilde F^{*}\mathcal{E}_\nu)$; plain derivative, $ict'$ coordinates $Q_t=ict'$ | Conservation with source per direction; Lorentz four-force |
| $T_{\mu\nu}=\partial/\partial Q_\mu\,\phi\partial/\partial Q_\nu\,\phi+\eta_{\mu\nu}\mathcal{L}_\phi$ | Scalar stress–energy |
| $T_{tt}=T^{tt}=\frac{1}{2c^2}\left(\partial\phi/\partial t'\right)^{2}+\frac12(\nabla\phi)^2+\frac12\mu^2\phi^2$ | Scalar energy density, positive |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |

## Further Reading

- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the canonical and electromagnetic stress–energy tensors, the Poynting theorem, the trace of the electromagnetic tensor and conformal invariance.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for Noether's theorem, the stress–energy tensor and the field actions used here.
- Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the scalar and electromagnetic actions and their Euler–Lagrange equations.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the Maxwell stress tensor, momentum balance and radiation pressure.
- Emmy Noether, "Invariante Variationsprobleme," *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen* (1918) 235–257, for the original theorem relating symmetries to conservation laws.
- E. L. Hill, "Hamiltonian form of the electromagnetic field," *Reviews of Modern Physics* **23** (1951) 253–260, for the action, energy and momentum of the electromagnetic field.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of the electromagnetic stress–energy tensor.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the spacetime-algebra form of fields, actions and conserved currents.
- Ludwik Silberstein, "Elektromagnetische Grundgleichungen in bivektorieller Behandlung," *Annalen der Physik* **22** (1907) 579–586, for the complex-vector formulation of the electromagnetic energy and momentum.
