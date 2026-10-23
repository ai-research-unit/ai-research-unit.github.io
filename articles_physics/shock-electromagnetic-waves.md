# __Shock Electromagnetic Waves__

## Introduction

A **shock wave** is a discontinuity in a field or a medium that propagates through space. The concept is familiar from fluid dynamics (sonic booms, detonations) and from magnetohydrodynamics (solar flares, astrophysical jets), where the equations of motion are **nonlinear** and the nonlinearity causes smooth initial data to steepen into a discontinuity in finite time.

The question naturally arises whether electromagnetic waves can form shocks. This article answers the question carefully, distinguishing three regimes:

1. **Linear Maxwell in vacuum.** The equations are linear and the medium is non-dispersive. There are no shock electromagnetic waves in this regime. Smooth initial data produces smooth solutions for all time.
2. **Nonlinear electromagnetic media.** In a medium whose permittivity or permeability depends on the field intensity, the equations become nonlinear, and shock formation is possible. This is established physics and is observed in certain optical and plasma systems.
3. **Plasma electrodynamics.** In a plasma, the coupling of the electromagnetic field to the charged matter can produce nonlinear behavior. Shock-like electromagnetic structures are observed in astrophysical and laboratory plasmas.

This article treats the three regimes. The first is the one relevant to the linear biquaternion Maxwell equations of the companion article; the other two require nonlinear or material extensions of those equations. The article is honest about which results are established and which are the subject of ongoing research.

The biquaternionic gradient $\tilde{\nabla}$, the field-strength biquaternion $\tilde{F}$, the four-current $\tilde J$, and the wave equation $\Box\tilde{F} = -\sqrt{\mu}\,\tilde{\nabla}^{\natural}\tilde{J}$ are assumed from the companion article on Maxwell's equations. The conventions are those of that article: $\tilde{\nabla} = e_t \partial/\partial Q_t + \vec e_x \partial/\partial Q_x + \vec e_y \partial/\partial Q_y + \vec e_z \partial/\partial Q_z$, and $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \partial^2/\partial Q_t^2 + \Delta$. Throughout, the symbol $c$ denotes the **speed of light in the medium**, $c = 1/\sqrt{\epsilon\mu}$, and $c_0$ denotes the **vacuum speed of light**, $c_0 = 1/\sqrt{\epsilon_0\mu_0}$. In vacuum, $c = c_0$.

## Why Linear Vacuum Maxwell Has No Shocks

### The Linear Structure

The biquaternionic Maxwell equation in vacuum is

$$
\tilde{\nabla} \tilde{F} = -\sqrt{\mu}\,\tilde{J},
$$

where $\tilde J$ is the four-current and $\tilde{F}$ is the field-strength biquaternion. In the absence of sources, $\tilde J = 0$, and the equation is

$$
\tilde{\nabla} \tilde{F} = 0.
$$

Applying $\tilde{\nabla}^{\natural}$ to both sides and using $\Box = \tilde{\nabla}^{\natural}\tilde{\nabla}$ gives the wave equation

$$
\Box \tilde{F} = 0, \qquad \Box = \partial^2/\partial Q_t^2 + \Delta = \Delta - \frac{1}{c_0^2}\frac{\partial^2}{\partial {t'}^2}.
$$

This is a **linear, constant-coefficient, hyperbolic** equation. Two structural features follow.

**Feature 1: The equation is linear.** If $\tilde{F}_1$ and $\tilde{F}_2$ are solutions, then any linear combination $\alpha\tilde{F}_1 + \beta\tilde{F}_2$ is also a solution. There is no mechanism for the solution to steepen or to form a discontinuity spontaneously.

**Feature 2: The characteristics are the light cone.** The characteristic equation of the wave operator $\Box$ is

$$
\left(\frac{\nu_4}{c_0}\right)^2 - \|\nu\|^2 = 0,
$$

i.e., $\nu_4 = \pm c_0\|\nu\|$. The characteristic surfaces are the light cones. The Cauchy problem with data on a non-characteristic surface is well-posed, and the solution propagates along the characteristics at the speed $c_0$.

### The Propagation of Smoothness

In a linear hyperbolic equation, discontinuities in the initial data propagate along the characteristics without changing their structure. But **smooth initial data remains smooth for all time**. If the initial field $\tilde{F}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z, 0)$ is $C^\infty$, then so is $\tilde{F}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z, t')$ for every $t' > 0$.

The reason is that the solution operator is a Fourier multiplier: in the frequency domain, the solution is obtained by multiplying the initial data by a bounded function. The multiplier does not create new singularities; it only propagates the existing ones.

This is the precise sense in which linear vacuum Maxwell has no shock electromagnetic waves: the nonlinearity that would drive shock formation is simply absent.

### The Characteristic Surfaces Are Not Shocks

The light cone is a characteristic surface of the wave operator, and the field can have discontinuities on it if the initial data is discontinuous. But a discontinuity on the light cone is not a shock in the fluid-dynamic sense. It is a **propagating wave front** with a fixed structure: the discontinuity stays on the light cone, and its amplitude does not steepen.

In the fluid-dynamic sense, a shock is a discontinuity that arises **from smooth initial data** through nonlinear steepening. This does not occur in linear vacuum Maxwell.

**A note on terminology.** The Russian-school literature on generalised solutions — Alexeyeva's work on the Hamiltonian form of the Maxwell equations included — calls any surface of discontinuity of a generalised solution a "shock", the light-cone wave fronts of the *linear* equations included. This article reserves the word for the fluid-dynamic sense above and calls the linear discontinuities **wave fronts** throughout; where a cited source's "shock" appears, it is a wave front in this article's usage. The distributional layer and jump calculus behind both is developed in *Distributions on Surfaces, Layers, and Jump Conditions*.

## The Jump Conditions of the Biquaternionic Equation

Although shock formation does not occur in vacuum, the biquaternionic framework can still describe the **geometry** of a hypothetical discontinuity surface. This is useful because the same jump conditions will appear in the nonlinear and plasma regimes.

### The Distributional Framework

Let $S$ be a three-dimensional surface in $\mathbb{R}^3$ at a fixed time, or a general three-dimensional hypersurface in spacetime. Let $[\,\cdot\,]_S$ denote the jump of a quantity across $S$: for a field $\tilde{F}$ that is discontinuous on $S$,

$$
[\tilde{F}]_S = \tilde{F}^+ - \tilde{F}^-,
$$

where $\tilde{F}^+$ and $\tilde{F}^-$ are the limiting values on the two sides of $S$.

The distributional derivative of a discontinuous function acquires a surface term. Let $\tilde U_{\mathrm n}$ be the unit normal to $S$ in the $ict'$ convention, $\tilde U_{\mathrm n} = i\nu_t\,e_t + \vec u$ with $\nu_t^2 + \lvert\vec u\rvert^2 = 1$, and let $\delta_S$ be the surface delta distribution. For a spatial surface $\nu_t = 0$, and the normal is the pure $\vec u$. Then

$$
\partial/\partial Q_\mu \tilde{F} = \{\partial/\partial Q_\mu \tilde{F}\} + [\tilde{F}]_S\, n_\mu\, \delta_S,
$$

where $\{\partial/\partial Q_\mu \tilde{F}\}$ denotes the classical derivative away from $S$.

### The Jump Condition

Applying the distributional derivative to the biquaternionic Maxwell equation $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}$ in a homogeneous medium, and separating the surface terms, one obtains the **jump condition** on $S$:

$$
\boxed{\;\tilde U_{\mathrm n}\,[\tilde{F}]_S = 0\;}.
$$

**Consequence for a homogeneous medium.** In a homogeneous medium, the normal $\tilde U_{\mathrm n}$ is invertible for any **non-characteristic** surface. For such surfaces, the jump condition $\tilde U_{\mathrm n}[\tilde{F}]_S = 0$ forces the jump to vanish:

$$
[\tilde{F}]_S = 0 \qquad \text{(non-characteristic surface, homogeneous medium)}.
$$

So a discontinuity cannot propagate on a non-characteristic surface; the field must be continuous across it.

**Consequence for a characteristic surface.** If the surface is **characteristic** (the light cone, $\tilde U_{\mathrm n}\tilde U_{\mathrm n}^{\natural} = 0$), then $\tilde U_{\mathrm n}$ is a zero divisor and the jump condition has nontrivial solutions. This is the case of a propagating wave front, treated in the next subsection.

**Remark on material interfaces.** At a **material interface** (a surface across which the electromagnetic properties $\epsilon$ and $\mu$ jump), the field $\tilde{F}$ can jump even for a non-characteristic surface, because the constitutive relation $\tilde{F} = i\sqrt{\epsilon}\vec E - \sqrt{\mu}\vec H$ itself involves quantities that jump. The boundary conditions at such an interface are the standard ones — $[\vec D]\cdot n = 0$ and $[\vec B]\cdot n = 0$, with the tangential components of $\vec E$ and $\vec H$ continuous — but these follow from the integral form of Maxwell's equations across the interface, not from the jump condition $\tilde U_{\mathrm n}[\tilde{F}]_S = 0$ in a homogeneous medium.

### The Light-Cone Condition

If the surface $S$ is a **characteristic** surface (the light cone), the jump condition admits nontrivial solutions. On the light cone, the normal is a zero divisor, and the jump condition becomes the **wave-front condition**

$$
\boxed{\;[\tilde{F}]_S = -i\,[\tilde{F}]_S \times n\;},
$$

where $n$ is the spatial part of the normal to the moving surface. This is the condition for a **propagating wave front** in linear vacuum Maxwell. It is the same as the boundary condition for a wave front in the geometric-optics limit, and it does not describe a shock in the fluid-dynamic sense.

The wave-front condition implies that the jump $[\tilde{F}]_S$ has a specific structure: it is a complex combination of the electric and magnetic jumps, transverse to the propagation direction. Explicitly, in the basis aligned with the propagation direction, the jump is characterized by a single complex amplitude (corresponding to the two transverse polarizations of the wave).

### A Constant Zeroth-Order Term Does Not Change the Jump Condition

The derivation above uses the homogeneous biquaternionic Maxwell equation: a first-order operator and no zeroth-order term. The biquaternionic wave equations of the electro-gravimagnetic programme carry one, and it is worth recording that a **constant** zeroth-order term leaves the jump condition untouched. Write the biwave equation as $D^+_F B = G$ with $D^+_F = \nabla^+ + f + F$, $\nabla^+ = \partial/\partial\tau + i\nabla$, $f$ a scalar and $F$ a constant vector, and $B = B H$ the field extended across the front by a step. Only the derivative produces a layer, because the zeroth-order term contains the field and not its derivative:

$$
\nabla^+B = \{\nabla^+B\} + \{n_0 + i\vec u\}\circ[B]_F\,\delta_F ,
\qquad
(f+F)\circ B = \{(f+F)\circ B\} ,
$$

so separating the surface terms gives the same condition as before,

$$
\{n_0 + i\vec u\}\circ[B]_F = 0 .
$$

The $i$ on the spatial part of the normal is the bigradient's, and the condition is the article's $\tilde U_{\mathrm n}[\tilde{F}]_S = 0$: the two normals differ only by the position of the $i$, since $-i(n_0 + i\vec u) = \vec u - i n_0$ puts the imaginary unit in the time slot, which is the $ict'$ convention's $\tilde U_{\mathrm n} = i\nu_t e_t + \vec u$, and an overall factor in a vanishing condition is empty. Normalising the wave vector gives $n_0 = -1$, and separating the scalar and vector parts of $[B]_F = [b] + [\vec B]$,

$$
[b] + i(\vec u,[\vec B]) = 0 ,
\qquad
[\vec B] = i\,\bigl([b]\,\vec u + [\vec u,[\vec B]]\bigr) .
$$

The scalar equation carries the whole transversality statement: if the scalar jump vanishes — as it does for a pure-vector biquaternion, which is the electromagnetic case — then $(\vec u,[\vec B]) = 0$ and the front is transverse, exactly as in the light-cone condition above. The constant coefficient appears in neither, which is the same statement as the companion article's composition lemma read in the other direction: a constant zeroth-order coefficient enters the equation as a mass-like term and the jump condition not at all, because a discontinuity is a property of the derivative.

## The Joint Jump Conditions and Transversality

The wave-front condition is compact in the biquaternionic variable, but its content on the electric and magnetic fields is a **joint jump system**. Write the field strength,

$$
\tilde F = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H,
$$
 On a wave front $F_t$ moving with unit normal $\vec u$ at speed $c$, the condition $[\tilde{F}]_{F_t} = -i[\tilde{F}]_{F_t}\times\vec u$ is equivalent to the pair

$$
\sqrt{\epsilon}\,[\vec E]_{F_t} = \sqrt{\mu}\,[\vec H]_{F_t}\times\vec u,
\qquad
\sqrt{\mu}\,[\vec H]_{F_t} = \sqrt{\epsilon}\,\vec u\times[\vec E]_{F_t}.
$$

The two are not independent: each follows from the other together with transversality. Three corollaries make the geometry explicit.

- **No surface charge.** Taking the inner product with $\vec u$ gives $([\tilde F]_{F_t},\vec u) = 0$, hence $([\vec E]_{F_t},\vec u) = 0$ and $([\vec H]_{F_t},\vec u) = 0$: the normal components are continuous across the front, and no surface charge sits on it.
- **Transversality.** If the field ahead of the front vanishes, then $\vec E$, $\vec H$ and $\vec u$ are pairwise orthogonal: both jumps lie in the tangent plane of the front, and the Poynting vector is parallel to the wave vector. This is the sense in which the strong shocks of the field equation are transverse.
- **Electric and magnetic jumps vanish together.** $[\vec E]_{F_t} = 0$ if and only if $[\vec H]_{F_t} = 0$; an electric discontinuity cannot occur without a magnetic one.

The energy carried across the front satisfies the jump relation

$$
[W]_{F_t} = c^{-1}\,(\vec u,[\vec P]_{F_t}),
$$

which is the electric-energy component of the electromagnetic Rankine–Hugoniot condition; it is what makes the energy conservation law hold distributionally across the front, and the energy section below states the full biquaternionic relation $[\tilde U_{\mathrm n}\tilde{W}]_S = -[\tilde{\mathcal F}]_S$.

### The Shock Waves of the Charge–Current Field

The field strength is not the only object whose discontinuities the programme considers. The **charge–current field** $\tilde J_{\mathrm{eg}} = i\rho + \vec J$, with $\rho$ and $\vec J$ the combined complex charge and current of the electro-gravimagnetic programme, has shocks of its own, and they are **not** transverse in general. In a free field that field obeys the first-order system

$$
\partial/\partial\tau\,\rho + \mathrm{div}\,\vec J = 0,
\qquad
\nabla\rho + \partial/\partial\tau\,\vec J - i\,\mathrm{rot}\,\vec J = 0,
$$

which is the scalar and vector part of $D^-\tilde J_{\mathrm{eg}} = 0$, and whose characteristic equation — read off the three-vector part, the scalar part being a constraint on the divergence — is $\nu_t(\nu_t^2 - c^2\|\vec\nu\|^2) = 0$: the two speeds $\nu_t = \pm c\|\vec\nu\|$ together with the **simple** null root $\nu_t = 0$, so the characteristic cone is Maxwell's and the stationary surfaces are characteristic. The jump conditions across a front $F_\tau$ with unit normal $\vec m$ follow from the distributional form of the system:

$$
[\rho]_{F_\tau} = \big(\vec m, [\vec J]_{F_\tau}\big),
\qquad
[\vec J]_{F_\tau} = \vec m\,[\rho]_{F_\tau} - i\,\vec m\times[\vec J]_{F_\tau}.
$$

The second relation fixes the tangential jumps, and its inner product with $\vec m$ recovers the first, so the pair is consistent (checked numerically). The geometric conclusion is immediate:

- **The shocks are generally not transverse.** Taking the inner product of the second relation with $\vec m$ gives $(\vec m, [\vec J]_{F_\tau}) = [\rho]_{F_\tau}$: the longitudinal part of the current jump equals the charge jump. A nonzero charge jump therefore puts a longitudinal component into $[\vec J]_{F_\tau}$.
- **They are transverse exactly when the charge is continuous.** If $[\rho]_{F_\tau} = 0$, the pair reduces to $(\vec m,[\vec J]_{F_\tau}) = 0$ together with $[\vec J]_{F_\tau} = -i\,\vec m\times[\vec J]_{F_\tau}$, which is the transverse wave-front condition of the field.

The contrast with the field is the point, and the source states it explicitly: strong field shocks are transverse, while the shocks of the charge–current field are not, unless the charge jump vanishes. The jump conditions and the roots are recorded here as the external programme's, in the same sense as the rest of *The Electro-Gravimagnetic Field and the Magnetic-Charge–Mass Hypothesis*; the free system and the two relations above were recomputed, and the derivation from the distributional system is the source's.

The field's own fronts acquire a longitudinal term once the programme restores its scalar field. Taking the field as the scalar $\alpha$ plus the vector part, the jump conditions gain a term fixed by the scalar jump, and the wave fronts are transverse **exactly when the scalar field is continuous**: $[\alpha]_{F_\tau} = 0$ recovers the transverse conditions above, while a non-zero $[\alpha]_{F_\tau}$ puts a longitudinal component into the field jump, the normal components of $[\vec E]$ and $[\vec H]$ being the jumps of the two real parts of $\alpha$. The conditions, and their interpretation as the programme's attraction–resistance field, are recorded in *The Electro-Gravimagnetic Field and the Magnetic-Charge–Mass Hypothesis*; the classical case is the one above, with $\alpha$ absent.

## Shock Formation in Nonlinear Media

Shock electromagnetic waves **do** occur in nonlinear media. The mechanism is the same as in fluid dynamics: the nonlinearity causes the wave speed to depend on the field amplitude, and this dependence causes the wave profile to steepen.

### Nonlinear Constitutive Relations

In a nonlinear optical medium, the constitutive relations are modified:

$$
\vec D = \epsilon_0\vec E + \vec P(\vec E), \qquad \vec B = \mu_0\vec H + \mu_0\vec M(\vec H),
$$

where $\vec P$ and $\vec M$ are the nonlinear polarization and magnetization. For a Kerr medium, the leading nonlinearity is

$$
\vec P = \epsilon_0(\chi^{(1)}\vec E + \chi^{(3)}|\vec E|^2\vec E),
$$

where $\chi^{(1)}$ is the linear susceptibility and $\chi^{(3)}$ is the third-order nonlinear susceptibility.

The effective refractive index becomes

$$
n = n_0 + n_2 I,
$$

where $I = |\vec E|^2$ is the intensity and $n_2$ is the nonlinear refractive index. The local phase velocity $c(I) = c_0/n(I)$ depends on the intensity.

### Steepening and Shock Formation

For a plane wave propagating in a Kerr medium, the wave equation for the envelope is approximately

$$
\partial/\partial t' \tilde{F} + c(I)\,\partial/\partial Q_x \tilde{F} = 0,
$$

where $c(I)$ depends on the intensity $I = |\tilde{F}|^2$. This is a **transport equation** of the nonlinear steepening type. For a scalar field $\phi$ satisfying $\partial/\partial t'\phi + c(\phi)\partial/\partial Q_x\phi = 0$, the equation can be written in conservation form

$$
\partial/\partial t'\phi + \partial/\partial Q_x f(\phi) = 0, \qquad \frac{df}{d\phi}(\phi) = c(\phi),
$$

where $f$ is a primitive of $c$. For the biquaternion-valued field, the same structure applies, with $f$ defined as the primitive of $c$ along the direction of propagation.

By the method of characteristics, the wave profile steepens and forms a **caustic** (the point where the characteristics cross) in finite time. Beyond the caustic, the field becomes multivalued, and the **weak solution** (the physical solution) develops a discontinuity. This is a shock.

### Established Observations

Shock electromagnetic waves in nonlinear media have been observed:

- **Optical shocks** in Kerr media (Wan, Jia, Fleischer, *Nature Physics* 2007).
- **Self-steepening** of ultrashort laser pulses (Ranka et al., *Optics Letters* 1988).
- **Shock waves in semiconductor plasmas** (various authors).

These are established physical phenomena, and they are described by nonlinear extensions of Maxwell's equations. The biquaternion framework of the companion article does not describe them directly; it describes the linear limit of the same equations.

## Shock Electromagnetic Waves in Plasma

Shock electromagnetic waves are also observed in plasmas. The mechanism is again nonlinear, but the nonlinearity is more complex than in a simple Kerr medium.

### Plasma Electrodynamics

A plasma consists of free electrons and ions. The electromagnetic field couples to the charged particles through the Lorentz force. The resulting equations are the **Vlasov–Maxwell** system (or, in the fluid limit, the **magnetohydrodynamic** equations).

The key nonlinearity is the coupling of the field to the plasma current. The current is not a simple function of the field; it depends on the particle distribution, which is itself affected by the field. This feedback causes a rich variety of nonlinear phenomena.

### Shock Structures in Plasma

Shock electromagnetic waves in plasma take several forms:

- **Collisionless shocks.** These occur in the solar wind and in astrophysical plasmas. The shock is maintained by plasma instabilities rather than by particle collisions.
- **Relativistic shocks.** These occur in gamma-ray bursts and active galactic nuclei, where the shock speed is close to $c_0$.
- **Electrostatic shocks.** These are localized electric field structures that propagate through a plasma, observed by satellites in the Earth's magnetosphere.

Each of these is an established phenomenon, with a substantial literature. The biquaternion framework can be used to describe the **electromagnetic** aspects of these shocks, but the **plasma dynamics** must be added separately.

## Magnetohydrodynamics and the Fluid Correspondence

Magnetohydrodynamics is the setting in which the fluid and electromagnetic descriptions genuinely coincide rather than merely resemble each other, and it is the plainest checkable instance of the fluid–electromagnetism correspondence. Its centre is the **induction equation**.

For a conducting fluid of velocity $\vec v$ and magnetic diffusivity $\eta$, the magnetic field obeys

$$
\partial/\partial t'\vec B = \nabla\times(\vec v\times\vec B) + \eta\,\nabla^2\vec B,
$$

while the vorticity of the same flow, $\vec\omega = \nabla\times\vec v$, obeys the Helmholtz equation

$$
\partial/\partial t'\vec\omega = \nabla\times(\vec v\times\vec\omega) + \nu\,\nabla^2\vec\omega
$$

with the kinematic viscosity $\nu$. The two equations have the same form, in the same velocity field, with the magnetic field in the place of the vorticity and the magnetic diffusivity in the place of the kinematic viscosity. The vector identity behind both, valid for divergence-free fields, is

$$
-\nabla\times(\vec v\times\vec B) = (\vec B\cdot\nabla)\vec v - (\vec v\cdot\nabla)\vec B,
$$

so that each is of the advection–diffusion type

$$
\partial/\partial t'\vec Q + (\vec v\cdot\nabla)\vec Q = (\vec Q\cdot\nabla)\vec v + \kappa\,\nabla^2\vec Q,
$$

with the diffusivity $\kappa = \eta$ for the field and $\kappa = \nu$ for the vorticity. One consequence is that the magnetic field is frozen into a perfectly conducting fluid ($\eta = 0$) exactly as the vorticity is frozen into an inviscid one ($\nu = 0$): Alfvén's frozen-flux theorem is the magnetic image of Kelvin's circulation theorem. The identity has been verified by exact numerical differentiation over random divergence-free fields; the residuals are at machine precision.

**Where the correspondence stops.** It is a statement about two equations for one three-dimensional vector field, and it does not extend to either theory as a whole. There is no magnetic charge density, so there is no magnetic counterpart of the electric charge density, which is what empties the analogy's magnetic-Gauss sector; a fluid has no displacement current, so the constitutive relations are not the same objects; the dissipative terms have different microscopic origins; and the fluid equations are Galilean invariant while Maxwell's equations are Lorentz invariant. The correspondence is between the incompressible fluid limit and the *magnetic* Galilean limit of the electromagnetic equations (the regime of the quasi-stationary approximation), both of which are Galilean; *Maxwell's Equations in the Biquaternionic Formulation* states these limits from the electromagnetic side, and the source paper discusses changes of reference frame within the analogy. The source also offers an interpretation of electric charge in hydrodynamic terms, which is presented as part of the analogy rather than as an established identification, and the corpus records it as such.

## The Biquaternionic Formulation of Shock Fronts

The biquaternion framework can be applied to shock fronts in nonlinear media and plasmas, in the following way.

### The Generalized Source

The nonlinearity of the medium can be absorbed into an effective four-current $\tilde J_{\mathrm{eff}}$, which enters the equation multiplied by $\sqrt{\mu}$. The biquaternionic Maxwell equation becomes

$$
\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}_{\mathrm{eff}},
$$

where $\tilde J_{\mathrm{eff}}$ includes both the external sources (free charges and currents) and the effective sources arising from the nonlinear response of the medium. In the vacuum limit, $\tilde J_{\mathrm{eff}} \to \tilde J$; in a linear medium, $\tilde J_{\mathrm{eff}}$ is a linear function of $\tilde{F}$; in a nonlinear medium, it is a nonlinear function.

### The Shock as a Jump in $\tilde J_{\mathrm{eff}}$

A shock front is a surface $S$ across which the effective four-current $\tilde J_{\mathrm{eff}}$ has a jump. The field $\tilde{F}$ also has a jump, and the jump conditions are determined by the distributional form of the equation:

$$
\tilde U_{\mathrm n}\,[\tilde{F}]_S = 0 \quad \text{when } \tilde J_{\mathrm{eff}} \text{ is continuous across } S,
$$

$$
\tilde U_{\mathrm n}\,[\tilde{F}]_S = -\sqrt{\mu}\,[\tilde J_{\mathrm{eff}}]_S \quad \text{when } \tilde J_{\mathrm{eff}} \text{ jumps across } S.
$$

In the linear vacuum case, $\tilde J_{\mathrm{eff}} = 0$ everywhere, and the jump in $\tilde{F}$ is forced to vanish (unless the surface is characteristic, in which case the wave-front structure appears). In the nonlinear case, the jump in $\sqrt{\mu}\,\tilde{J}_{\mathrm{eff}}$ provides the driving term for the shock.

### The Characteristic Structure

The characteristic equation of the nonlinear biquaternionic equation is more complex than in the linear case. It depends on the effective four-current $\tilde J_{\mathrm{eff}}$, which depends on $\tilde{F}$ itself. The characteristics are no longer the light cone; they are the **nonlinear characteristics** of the medium.

The precise form of the characteristics, and the resulting shock structure, depends on the specific nonlinearity. This is the subject of ongoing research in nonlinear optics and plasma physics, and the biquaternionic formulation provides a compact language for expressing it.

## The Energy Jump Across a Shock Front

For a shock front in a nonlinear medium, the **energy** of the electromagnetic field is not conserved across the shock: some of the energy is dissipated into the medium. The jump in the biquaternionic energy–momentum is related to the flux of energy–momentum across the front.

### The Jump Relation

Let $\tilde{W}$ be the biquaternionic energy–momentum. Across the shock front $S$ with normal $\tilde U_{\mathrm n}$, the jump satisfies

$$
\boxed{\;[\tilde U_{\mathrm n}\tilde{W}]_S = -[\tilde{\mathcal F}]_S\;},
$$

where $\tilde{\mathcal F}$ is the biquaternionic power–force density. This is the biquaternionic form of the **Rankine–Hugoniot condition** for electromagnetic shocks, and it is the counterpart of the standard conservation-law relation for fluid shocks.

The physical content is the same as in the fluid case: the jump in the flux of energy–momentum across the shock is balanced by the work done by the medium on the field.

### Dissipation

In a shock wave, the kinetic energy of the incoming flow is partly converted into heat by dissipative processes. In electromagnetic shocks, the corresponding dissipation is the absorption of the electromagnetic field by the medium.

The dissipative mechanism depends on the medium:

- In a **Kerr medium**, two-photon absorption and other nonlinear processes dissipate energy.
- In a **plasma**, the dissipation is due to wave–particle interactions and to plasma instabilities.
- In a **nonlinear dielectric**, the dissipation may be due to the finite response time of the medium.

In each case, the dissipation is described by an effective absorption term in the constitutive relations, and the biquaternionic formulation can be extended to include it.

## Open Questions

1. **The nonlinear biquaternionic Maxwell equation.** The biquaternion framework is linear in the field strength. What is the correct nonlinear extension, and what are its characteristic surfaces?

2. **The relation to the Rankine–Hugoniot conditions.** The jump conditions in the biquaternion framework have the same form as the Rankine–Hugoniot conditions of fluid dynamics. Is this a deep structural relation, or a formal analogy?

3. **The relation to the linear biquaternion Maxwell equation.** The linear equation is the vacuum limit of the nonlinear one. How does the shock structure of the nonlinear equation degenerate in the linear limit?

4. **The connection to solitons and other coherent structures.** In some nonlinear media, electromagnetic waves can form solitons rather than shocks. What is the relation between the two?

5. **The connection to plasma shocks.** The plasma case is more complex than the simple Kerr medium. Can the biquaternion framework be extended to the plasma case?

6. **The role of dispersion.** Dispersion regularizes shocks into wave trains and solitons. What is the dispersion relation of the biquaternion formulation, and how does it modify the shock structure?

7. **The non-transverse shocks of the charge–current field.** The charge–current field of the electro-gravimagnetic programme has shocks whose longitudinal current jump equals the charge jump, so they are generally non-transverse. Does a physical charge–current distribution support such fronts, and what would they carry across?

These are open questions, and they are the subject of ongoing research in nonlinear electrodynamics and plasma physics.

## Summary

Shock electromagnetic waves are not a feature of linear Maxwell equations in vacuum. The linearity of the equations, together with the constancy of the wave speed, prevents the formation of discontinuities from smooth initial data. Smooth data produces smooth solutions for all time.

Shock electromagnetic waves **are** a feature of nonlinear media and plasmas. In a Kerr medium, the intensity-dependent refractive index causes the wave profile to steepen, and a shock forms in finite time. In a plasma, the coupling of the electromagnetic field to the charged matter produces a rich variety of shock structures.

The biquaternion framework provides a compact language for expressing the shock conditions in nonlinear media and plasmas. The jump conditions, the energy–momentum balance, and the characteristic structure can all be expressed in biquaternion form. On a wave front the single condition $[\tilde{F}] = -i[\tilde{F}]\times\vec u$ unpacks into a joint jump system for $\vec E$ and $\vec H$ — the normal components continuous, the tangential jumps transverse, and the electric and magnetic tangential jumps vanishing together — with the energy jump $[W] = c^{-1}(\vec u,[\vec P])$ closing the distributional conservation law. The **charge–current field** $\tilde J_{\mathrm{eg}} = i\rho + \vec J$ of the electro-gravimagnetic programme behaves differently: its shocks are generally **not** transverse, because the longitudinal part of the current jump equals the charge jump, and they become transverse only when the charge jump vanishes. But the framework is linear, and the nonlinearity that drives shock formation must be added separately.

The treatment of shock electromagnetic waves in the biquaternion framework is therefore a treatment of the **linear skeleton** of a nonlinear theory. It describes the geometry of the shock front and the conservation laws that the shock must satisfy, but it does not describe the nonlinear dynamics that creates the shock. That dynamics is the subject of nonlinear optics and plasma physics, and the biquaternion framework provides a natural language for expressing it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $c = 1/\sqrt{\epsilon\mu}$ | **Speed of light in the medium** (local) |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | **Speed of light in vacuum** (global constant) |
| $\tilde{\nabla} = e_t\partial/\partial Q_t + \sum_\mu \vec e_\mu \partial/\partial Q_\mu$ | Biquaternionic gradient |
| $\Box = \partial^2/\partial Q_t^2 + \Delta$ | d'Alembertian |
| $\tilde U_{\mathrm n}$ | Unit normal to the surface, $i\nu_t e_t + \vec u$ in the $ict'$ convention; the spatial case is the pure $\vec u$ |
| $[\tilde{F}]_S$ | Jump of $\tilde{F}$ across the surface $S$ |
| $\tilde J_{\mathrm{eg}} = i\rho + \vec J$ | Charge–current biquaternion of the electro-gravimagnetic programme |
| $\rho = \rho_E/\sqrt{\epsilon} - i\rho_H/\sqrt{\mu}$ | Combined complex charge density |
| $\vec J = \sqrt{\mu}\,\vec j_E - i\sqrt{\epsilon}\,\vec j_H$ | Combined complex current |
| $\vec m$ | Unit normal to the charge–current front |
| $[\vec E]_{F_t}, [\vec H]_{F_t}$ | Jumps of the electric and magnetic fields across the wave front |
| $\vec u$ | Unit normal to the wave front, in the direction of motion |
| $\tilde J_{\mathrm{eff}}$ | Effective four-current including nonlinear medium response |

## Further Reading

- R. Ranka, R. W. Schirmer, A. L. Gaeta, "Observation of pulse splitting in nonlinear dispersive media," *Physical Review Letters* **77** (1996) 3783–3786.
- W. Wan, S. Jia, J. W. Fleischer, "Discrete solitons and soliton-induced dislocations in partially coherent photonic lattices," *Physical Review Letters* **98** (2007) 233901.
- L. A. Alexeyeva, "Hamiltonian Form of the Maxwell Equations and Its Generalized Solutions" (2001), for the distributional treatment of discontinuous solutions.
- L. A. Alexeyeva, "One Biquaternion Model of the Electro-Gravimagnetic Field. Field Analogues of Newton's Laws" (2007), for the charge–current field, its first-order system and the non-transverse character of its shocks; see *The Electro-Gravimagnetic Field and the Magnetic-Charge–Mass Hypothesis*.
- L. A. Alexeyeva, "Maxwell Equations, Their Hamiltonian and Biquaternionic Forms and Properties of Their Solutions" (2016), for the biquaternionic formulation.
- L. A. Alexeyeva, "Biquaternionic wave equations and the properties of their generalized solutions", *Differential Equations* **57** (5) (2021) 594–604, for the front condition $\{n_0 + i\vec u\}\circ[B]_F = 0$ of the biwave equation with a general constant structural coefficient and the transversality it implies; the composition lemma, the weighted kernel and the paper's sign discrepancy are recorded in *The Biquaternion D'Alembertian and Its Green's Functions*.
- R. Z. Sagdeev, "Cooperative phenomena and shock waves in collisionless plasmas," *Reviews of Plasma Physics* **4** (1966) 23–91.
- J. E. Allen, "Shock waves in plasmas," in *Encyclopedia of Physical Science and Technology* (Academic Press, 2001).
- A. Jeffrey and T. Taniuti, *Non-Linear Wave Propagation* (Academic Press, 1964), for the general theory of nonlinear hyperbolic equations and shock formation.
- G. B. Whitham, *Linear and Nonlinear Waves* (Wiley, 1974), for the general theory of shock waves and conservation laws.
- G. Rousseaux and É. Guyon, "À propos d'une analogie entre la mécanique des fluides et l'électromagnétisme", *Bulletin de l'Union des Physiciens* **96** (2002), no. 841 (2), 125–134, for the induction equation, its identification with the Helmholtz vorticity equation, and the limits of the fluid–electromagnetism correspondence recorded in *Magnetohydrodynamics and the Fluid Correspondence*. An expository article in a teachers' journal, in French.

