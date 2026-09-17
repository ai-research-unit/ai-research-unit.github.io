
# __Shock Electromagnetic Waves__

## Introduction

A **shock wave** is a discontinuity in a field or a medium that propagates through space. The concept is familiar from fluid dynamics (sonic booms, detonations) and from magnetohydrodynamics (solar flares, astrophysical jets), where the equations of motion are **nonlinear** and the nonlinearity causes smooth initial data to steepen into a discontinuity in finite time.

The question naturally arises whether electromagnetic waves can form shocks. This article answers the question carefully, distinguishing three regimes:

1. **Linear Maxwell in vacuum.** The equations are linear and the medium is non-dispersive. There are no shock electromagnetic waves in this regime. Smooth initial data produces smooth solutions for all time.
2. **Nonlinear electromagnetic media.** In a medium whose permittivity or permeability depends on the field intensity, the equations become nonlinear, and shock formation is possible. This is established physics and is observed in certain optical and plasma systems.
3. **Plasma electrodynamics.** In a plasma, the coupling of the electromagnetic field to the charged matter can produce nonlinear behavior. Shock-like electromagnetic structures are observed in astrophysical and laboratory plasmas.

This article treats the three regimes. The first is the one relevant to the linear biquaternion Maxwell equations of the companion article; the other two require nonlinear or material extensions of those equations. The article is honest about which results are established and which are the subject of ongoing research.

The biquaternionic gradient $\tilde{\nabla}$, the field-strength biquaternion $\tilde{F}$, the source biquaternion $\tilde{R}$, and the wave equation $\Box\tilde{F} = -\tilde{\nabla}\tilde{R}$ are assumed from the companion article on Maxwell's equations. The conventions are those of that article: $\tilde{\nabla} = e_0 \partial_{ict} + e_1 \partial_x + e_2 \partial_y + e_3 \partial_z$, and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2 + \Delta$. Throughout, the symbol $c$ denotes the **speed of light in the medium**, $c = 1/\sqrt{\epsilon\mu}$, and $c_0$ denotes the **vacuum speed of light**, $c_0 = 1/\sqrt{\epsilon_0\mu_0}$. In vacuum, $c = c_0$.

## Why Linear Vacuum Maxwell Has No Shocks

### The Linear Structure

The biquaternionic Maxwell equation in vacuum is

$$
\tilde{\nabla} \tilde{F} = -\tilde{R},
$$

where $\tilde{R}$ is the source and $\tilde{F}$ is the field-strength biquaternion. In the absence of sources, $\tilde{R} = 0$, and the equation is

$$
\tilde{\nabla} \tilde{F} = 0.
$$

Applying $\bar{\tilde{\nabla}}$ to both sides and using $\Box = \bar{\tilde{\nabla}}\tilde{\nabla}$ gives the wave equation

$$
\Box \tilde{F} = 0, \qquad \Box = \partial_{ict}^2 + \Delta = \Delta - \frac{1}{c_0^2}\frac{\partial^2}{\partial t^2},
$$

where in vacuum $c = c_0$. This is a **linear, constant-coefficient, hyperbolic** equation. Two structural features follow.

**Feature 1: The equation is linear.** If $\tilde{F}_1$ and $\tilde{F}_2$ are solutions, then any linear combination $\alpha\tilde{F}_1 + \beta\tilde{F}_2$ is also a solution. There is no mechanism for the solution to steepen or to form a discontinuity spontaneously.

**Feature 2: The characteristics are the light cone.** The characteristic equation of the wave operator $\Box$ is

$$
\left(\frac{\nu_4}{c_0}\right)^2 - \|\nu\|^2 = 0,
$$

i.e., $\nu_4 = \pm c_0\|\nu\|$. The characteristic surfaces are the light cones. The Cauchy problem with data on a non-characteristic surface is well-posed, and the solution propagates along the characteristics at the speed $c_0$.

### The Propagation of Smoothness

In a linear hyperbolic equation, discontinuities in the initial data propagate along the characteristics without changing their structure. But **smooth initial data remains smooth for all time**. If the initial field $\tilde{F}(\mathbf{x}, 0)$ is $C^\infty$, then so is $\tilde{F}(\mathbf{x}, t)$ for every $t > 0$.

The reason is that the solution operator is a Fourier multiplier: in the frequency domain, the solution is obtained by multiplying the initial data by a bounded function. The multiplier does not create new singularities; it only propagates the existing ones.

This is the precise sense in which linear vacuum Maxwell has no shock electromagnetic waves: the nonlinearity that would drive shock formation is simply absent.

### The Characteristic Surfaces Are Not Shocks

The light cone is a characteristic surface of the wave operator, and the field can have discontinuities on it if the initial data is discontinuous. But a discontinuity on the light cone is not a shock in the fluid-dynamic sense. It is a **propagating wave front** with a fixed structure: the discontinuity stays on the light cone, and its amplitude does not steepen.

In the fluid-dynamic sense, a shock is a discontinuity that arises **from smooth initial data** through nonlinear steepening. This does not occur in linear vacuum Maxwell.

## The Jump Conditions of the Biquaternionic Equation

Although shock formation does not occur in vacuum, the biquaternionic framework can still describe the **geometry** of a hypothetical discontinuity surface. This is useful because the same jump conditions will appear in the nonlinear and plasma regimes.

### The Distributional Framework

Let $S$ be a three-dimensional surface in $\mathbb{R}^3$ at a fixed time, or a three-dimensional surface $F$ in spacetime $\mathbb{R}^4 = \{(x,t)\}$. Let $[\,\cdot\,]_S$ denote the jump of a quantity across $S$: for a field $\tilde{F}$ that is discontinuous on $S$,

$$
[\tilde{F}]_S = \tilde{F}^+ - \tilde{F}^-,
$$

where $\tilde{F}^+$ and $\tilde{F}^-$ are the limiting values on the two sides of $S$.

The distributional derivative of a discontinuous function acquires a surface term. If $n$ is the unit normal to $S$ and $\delta_S$ is the surface delta distribution, then

$$
\partial_j \tilde{F} = \{\partial_j \tilde{F}\} + [\tilde{F}]_S\, n_j\, \delta_S,
$$

where $\{\partial_j\tilde{F}\}$ denotes the classical derivative away from $S$.

### The Jump Condition

Applying the distributional derivative to the biquaternionic Maxwell equation $\tilde{\nabla}\tilde{F} = -\tilde{R}$, and separating the surface terms, one obtains the **jump condition** on $S$:

$$
\tilde{n}\,[\tilde{F}]_S = 0,
$$

where $\tilde{n} = n_0 e_0 + n_1 e_1 + n_2 e_2 + n_3 e_3$ is the biquaternion-valued normal.

For the field-strength biquaternion $\tilde{F} = \sqrt{\epsilon}\mathbf{E} + i\sqrt{\mu}\mathbf{H}$, this becomes two conditions:

$$
[\mathbf{D}]_S \cdot n = 0, \qquad [\mathbf{B}]_S \cdot n = 0,
$$

where $\mathbf{D} = \epsilon\mathbf{E}$ and $\mathbf{B} = \mu\mathbf{H}$. These are the standard **electromagnetic boundary conditions** for a surface: the normal components of the electric displacement and the magnetic induction are continuous across the surface. This is established physics: it is the same condition that holds at a dielectric interface or a conductor surface.

### The Light-Cone Condition

If the surface $S$ is moving in spacetime, with the normal $\tilde{n}$ varying from point to point, then the jump condition becomes a **characteristic condition** when $\tilde{n}\bar{\tilde{n}} = 0$, i.e., when the surface is a light cone. In this case, the jump condition has the additional structure

$$
[\tilde{F}]_S = -i\,[\tilde{F}]_S \times n,
$$

where $n$ is the spatial normal to the moving surface. This is the condition for a **propagating wave front** in linear vacuum Maxwell. It is the same as the boundary condition for a wave front in the geometric-optics limit, and it does not describe a shock in the fluid-dynamic sense.

## Shock Formation in Nonlinear Media

Shock electromagnetic waves **do** occur in nonlinear media. The mechanism is the same as in fluid dynamics: the nonlinearity causes the wave speed to depend on the field amplitude, and this dependence causes the wave profile to steepen.

### Nonlinear Constitutive Relations

In a nonlinear optical medium, the constitutive relations are modified:

$$
\mathbf{D} = \epsilon_0\mathbf{E} + \mathbf{P}(\mathbf{E}), \qquad \mathbf{B} = \mu_0\mathbf{H} + \mu_0\mathbf{M}(\mathbf{H}),
$$

where $\mathbf{P}$ and $\mathbf{M}$ are the nonlinear polarization and magnetization. For a Kerr medium, the leading nonlinearity is

$$
\mathbf{P} = \epsilon_0(\chi^{(1)}\mathbf{E} + \chi^{(3)}|\mathbf{E}|^2\mathbf{E}),
$$

where $\chi^{(1)}$ is the linear susceptibility and $\chi^{(3)}$ is the third-order nonlinear susceptibility.

The effective refractive index becomes

$$
n = n_0 + n_2 I,
$$

where $I = |\mathbf{E}|^2$ is the intensity and $n_2$ is the nonlinear refractive index. The local phase velocity $c(I) = c_0/n(I)$ depends on the intensity.

### Steepening and Shock Formation

For a plane wave propagating in a Kerr medium, the wave equation for the envelope is approximately

$$
\partial_t \tilde{F} + c(I)\,\partial_x \tilde{F} = 0,
$$

which is a **conservation law** of the form $\partial_t \tilde{F} + \partial_x(c(I)\tilde{F}) = 0$ when $c(I) = c(|\tilde{F}|)$. This is the same equation that governs the formation of shocks in a simple nonlinear wave.

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

## The Biquaternionic Formulation of Shock Fronts

The biquaternion framework can be applied to shock fronts in nonlinear media and plasmas, in the following way.

### The Generalized Source

The nonlinearity of the medium can be absorbed into an effective source $\tilde{R}_{\mathrm{eff}}$. The biquaternionic Maxwell equation becomes

$$
\tilde{\nabla}\tilde{F} = -\tilde{R}_{\mathrm{eff}},
$$

where $\tilde{R}_{\mathrm{eff}}$ includes both the external sources (free charges and currents) and the effective sources arising from the nonlinear response of the medium. In the vacuum limit, $\tilde{R}_{\mathrm{eff}} \to \tilde{R}$; in a linear medium, $\tilde{R}_{\mathrm{eff}}$ is a linear function of $\tilde{F}$; in a nonlinear medium, it is a nonlinear function.

### The Shock as a Jump in $\tilde{R}_{\mathrm{eff}}$

A shock front is a surface $S$ across which the effective source $\tilde{R}_{\mathrm{eff}}$ has a jump. The field $\tilde{F}$ also has a jump, and the jump conditions are determined by the distributional form of the equation:

$$
\tilde{n}\,[\tilde{F}]_S = -[\tilde{R}_{\mathrm{eff}}]_S / (\text{coefficient}).
$$

In the linear vacuum case, $\tilde{R}_{\mathrm{eff}} = 0$ everywhere, and the jump in $\tilde{F}$ is forced to vanish (unless the surface is characteristic, in which case the wave front structure appears). In the nonlinear case, the jump in $\tilde{R}_{\mathrm{eff}}$ provides the driving term for the shock.

### The Characteristic Structure

The characteristic equation of the nonlinear biquaternionic equation is more complex than in the linear case. It depends on the effective source $\tilde{R}_{\mathrm{eff}}$, which depends on $\tilde{F}$ itself. The characteristics are no longer the light cone; they are the **nonlinear characteristics** of the medium.

The precise form of the characteristics, and the resulting shock structure, depends on the specific nonlinearity. This is the subject of ongoing research in nonlinear optics and plasma physics, and the biquaternionic formulation provides a compact language for expressing it.

## The Energy Jump Across a Shock Front

For a shock front in a nonlinear medium, the **energy** of the electromagnetic field is not conserved across the shock: some of the energy is dissipated into the medium. The jump in the biquaternionic energy–momentum is related to the flux of energy–momentum across the front.

### The Jump Relation

Let $\tilde{W}$ be the biquaternionic energy–momentum. Across the shock front $S$ with normal $\tilde{n}$, the jump satisfies

$$
[\tilde{n}\tilde{W}]_S = -[\tilde{P}]_S,
$$

where $\tilde{P}$ is the biquaternionic power–force density. This is the biquaternionic form of the **Rankine–Hugoniot condition** for electromagnetic shocks, and it is the counterpart of the standard conservation-law relation for fluid shocks.

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

These are open questions, and they are the subject of ongoing research in nonlinear electrodynamics and plasma physics.

## Summary

Shock electromagnetic waves are not a feature of linear Maxwell equations in vacuum. The linearity of the equations, together with the constancy of the wave speed, prevents the formation of discontinuities from smooth initial data. Smooth data produces smooth solutions for all time.

Shock electromagnetic waves **are** a feature of nonlinear media and plasmas. In a Kerr medium, the intensity-dependent refractive index causes the wave profile to steepen, and a shock forms in finite time. In a plasma, the coupling of the electromagnetic field to the charged matter produces a rich variety of shock structures.

The biquaternion framework provides a compact language for expressing the shock conditions in nonlinear media and plasmas. The jump conditions, the energy–momentum balance, and the characteristic structure can all be expressed in biquaternion form. But the framework is linear, and the nonlinearity that drives shock formation must be added separately.

The treatment of shock electromagnetic waves in the biquaternion framework is therefore a treatment of the **linear skeleton** of a nonlinear theory. It describes the geometry of the shock front and the conservation laws that the shock must satisfy, but it does not describe the nonlinear dynamics that creates the shock. That dynamics is the subject of nonlinear optics and plasma physics, and the biquaternion framework provides a natural language for expressing it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $c = 1/\sqrt{\epsilon\mu}$ | **Speed of light in the medium** (local) |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | **Speed of light in vacuum** (global constant) |
| $\tilde{\nabla} = e_0\partial_{ict} + \sum_k e_k \partial_k$ | Biquaternionic gradient |
| $\Box = \partial_{ict}^2 + \Delta$ | d'Alembertian |
| $\tilde{n}$ | Biquaternion-valued normal to the shock front |
| $[\tilde{F}]_S$ | Jump of $\tilde{F}$ across the surface $S$ |

## Further Reading

- R. Ranka, R. W. Schirmer, A. L. Gaeta, "Observation of pulse splitting in nonlinear dispersive media," *Physical Review Letters* **77** (1996) 3783–3786.
- W. Wan, S. Jia, J. W. Fleischer, "Discrete solitons and soliton-induced dislocations in partially coherent photonic lattices," *Physical Review Letters* **98** (2007) 233901.
- L. A. Alexeyeva, "Hamiltonian Form of the Maxwell Equations and Its Generalized Solutions" (2001), for the distributional treatment of discontinuous solutions.
- L. A. Alexeyeva, "Maxwell Equations, Their Hamiltonian and Biquaternionic Forms and Properties of Their Solutions" (2016), for the biquaternionic formulation.
- R. Z. Sagdeev, "Cooperative phenomena and shock waves in collisionless plasmas," *Reviews of Plasma Physics* **4** (1966) 23–91.
- J. E. Allen, "Shock waves in plasmas," in *Encyclopedia of Physical Science and Technology* (Academic Press, 2001).
- A. Jeffrey and T. Taniuti, *Non-Linear Wave Propagation* (Academic Press, 1964), for the general theory of nonlinear hyperbolic equations and shock formation.
- G. B. Whitham, *Linear and Nonlinear Waves* (Wiley, 1974), for the general theory of shock waves and conservation laws.

