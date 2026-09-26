# __The Central Scalar Field: Classical Dynamics in the Biquaternion Center__

## Introduction

The biquaternion algebra carries a distinguished two-dimensional real subspace that commutes with everything: the **center** $\mathbb{C}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{e_0,ie_0\}$, the fixed-point set of quaternion conjugation. It is the algebra's rotationally invariant subspace, and it is the only place a field with a single Lorentz-scalar component can live. The companion article *The Scalar Field in the Center: Why Spin 0 Escapes the Biquaternion State Module* established that result representation-theoretically: the state module is the two-dimensional defining module of the algebra and carries spin $\tfrac12$, so a trivial-representation field has no module to occupy and must be valued in the center instead.

This article develops the **classical dynamics** of that field. The field is $\tilde{\Phi}=\phi e_0$, a single complex (or, in the real case, real) scalar function of the event; because it is valued in the center, it commutes with the biquaternionic gradient, with every rotation rotor and with every element of the algebra, and its dynamics is the classical field theory of one scalar degree of freedom. No quantization is used anywhere below: the field equation is a wave equation, the source is a prescribed classical density, and the objects computed are the classical field, its energy and its force on a test source.

The article has one configuration as its destination. A **static central source** produces a static, spherically symmetric field, and the interaction of a test source with that field is the central-force problem of the sibling article *The Relativistic Central Force Problem in Biquaternionic Form*. The reduction is exact, and it has a clean algebraic reason: because the field takes its values in the rotationally invariant subspace, the potential it produces is a **central scalar** in the sense of the companion article *The Central-Scalar Limit of Classical Mechanics in Biquaternionic Form*, so the force on a test source is a real vector parallel to the position, the angular momentum is conserved, and the orbit is the one solved relativistically in the sibling article. This article therefore supplies the field-theoretic origin of the $1/r$ potential that the central-force articles treat as given.

Four results are established.

- **The field equation in the center.** The classical action
$$
S=\int\left[-\tfrac12\,\partial_\mu\phi\,\partial^\mu\phi-\tfrac12\mu^2\phi^2+g\rho\,\phi\right]d^4x
$$
has the Euler–Lagrange equation $(\Box-\mu^2)\tilde{\Phi}=-g\rho\,e_0$, where $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}$ is central and scalar, so the equation acts on the single scalar component. The free field obeys $(\Box-\mu^2)\tilde{\Phi}=0$, with dispersion $\omega^2=c^2k^2+c^2\mu^2$ and range $\mu^{-1}$.
- **The static central solution.** A point source of strength $Q$ gives the Yukawa field $\tilde{\Phi}=gQ\,e^{-\mu r}/(4\pi r)\,e_0$, whose massless limit is the $1/r$ potential $gQ/(4\pi r)$.
- **The field energy.** The static field's energy is positive and diverges at a point source, $E_{\text{field}}=2\pi A^2/a$ outside a sphere of radius $a$ in the massless case, with $A=gQ/(4\pi)$; the divergence is the classical self-energy of the point-source idealization.
- **The reduction to the central-force problem.** A test source of coupling $g'$ has interaction energy $U(r)=-\kappa e^{-\mu r}/r$ with $\kappa=gg'Q/(4\pi)>0$, a central potential of the type solved in the sibling article; in the massless limit $U=-\kappa/r$ and the orbit is exactly the precessing conic of that article.

The article closes by identifying why a central scalar field carries no intrinsic magnetism, and by separating what the algebra supplies from what it imports.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the basis is $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$ and $e_je_k=\varepsilon_{jkl}e_l$ for $j\neq k$; the scalar imaginary $i$ is central with $i^2=-e_0$. The anti-Hermitian subspace $\mathbb{M}_-$ is the material sector and the Hermitian subspace $\mathbb{M}_+$ the informational sector, with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ and $i\mathbb{M}_\pm=\mathbb{M}_\mp$; the center is $\mathbb{C}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{e_0,ie_0\}$, and $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace. The conjugations are $\bar{\cdot}$ (quaternion), ${}^*$ (complex), ${}^\dagger=\bar{\cdot}^{\,*}$ (Hermitian) and ${}^\flat=-\dagger$ (anti-Hermitian). The biquaternionic gradient is $\tilde{\nabla}=e_0\partial_{ict}+e_1\partial_x+e_2\partial_y+e_3\partial_z$, its quaternion conjugate is $\bar{\tilde{\nabla}}=e_0\partial_{ict}-e_1\partial_x-e_2\partial_y-e_3\partial_z$, and $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\bar{\tilde{\nabla}}\tilde{\nabla}=\partial_{ict}^2+\Delta=-\partial_t^2/c^2+\Delta$, the series convention of the companion article *Conventions in the Biquaternion Universe*. The mass parameter is $\mu=mc/\hbar$, the inverse Compton wavelength, exactly as in the companion articles *The Klein–Gordon Equation in Biquaternionic Form* and *Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form*; classically only the length $\mu^{-1}$ matters and $\hbar$ enters only through the identification of $\mu$ with a mass. The four-position is $\tilde{X}=ict\,e_0+\mathbf{x}$. The source density is $\rho$, the source strength $Q$, and the couplings are $g$ for the field and $g'$ for the test source. Throughout, $c=1/\sqrt{\epsilon\mu}$ is the **speed of light in the medium** and $c_0$ its vacuum value.

## The Center as the Scalar's Value Space

### The Center and Its Properties

The center is the centralizer of the quaternion units,

$$
\mathbb{C}_{\mathbb{B}}=\{\tilde{Q}\in\mathbb{B} : [\tilde{Q},e_k]=0,\ k=1,2,3\}=\{Q_0e_0 : Q_0\in\mathbb{C}\}=\operatorname{span}_{\mathbb{R}}\{e_0,ie_0\}.
$$

It is a subalgebra isomorphic to $\mathbb{C}$, it is two-dimensional over $\mathbb{R}$, and it meets the two sectors in one real direction each:

$$
\mathbb{C}_{\mathbb{B}}\cap\mathbb{M}_+=\mathbb{R}\,e_0, \qquad
\mathbb{C}_{\mathbb{B}}\cap\mathbb{M}_-=\mathbb{R}\,ie_0 .
$$

The first property to record is that the center is not merely a subspace: it is **closed under multiplication**, because $Q_0e_0\cdot Q_0'e_0=Q_0Q_0'e_0$. A scalar field valued in the center therefore admits polynomial self-interactions without leaving the center, a fact used in the open questions below. The second is that its elements commute with the rotation generators, so a centrally valued field is a **rotational scalar**: rotations act on it trivially, and there is no internal direction for a rotation to move.

### The Field and Its Components

The central scalar field is

$$
\tilde{\Phi}(x)=\phi(x)\,e_0, \qquad \phi:\mathbb{R}^{1,3}\to\mathbb{C},
$$

a single complex-valued function of the event. Its real and imaginary parts are

$$
\tilde{\Phi}=\phi_1 e_0+i\phi_2 e_0, \qquad \phi_1,\phi_2\in\mathbb{R},
$$

so the real part occupies the scalar direction of the informational sector and the imaginary part the scalar direction of the material sector. This is the algebraic reason the second-order scalar structure does not organise itself by the material/informational split: the sector decomposition of a complex scalar is its decomposition into real and imaginary parts, not into particle and antiparticle or state and operator, as discussed in the companion article on the scalar field in the center. For most of this article the field is taken **real**, $\phi_2=0$; the complex case is treated where the central phase matters, in the section on the conserved current.

A field in the center is a Lorentz scalar in two senses. It is invariant under the rotor conjugation $\tilde{\Phi}\mapsto\tilde{\Lambda}\tilde{\Phi}\tilde{\Lambda}^{-1}=\tilde{\Lambda}\tilde{\Phi}\bar{\tilde{\Lambda}}$ with $\tilde{\Lambda}\bar{\tilde{\Lambda}}=e_0$, because $\tilde{\Phi}$ commutes with $\tilde{\Lambda}$ and $\tilde{\Lambda}\bar{\tilde{\Lambda}}=e_0$; and it is invariant under spatial rotations, which are the unit real quaternions acting the same way, for the same reason. The scalar nature of the field is thus not an assumption about its transformation law but a consequence of its living in the center.

## The Classical Action and the Field Equation

### The Action

The classical action of a real central scalar field coupled to a prescribed source density $\rho$ is

$$
S=\int\mathcal{L}\,d^4x, \qquad
\mathcal{L}=-\tfrac12\,\partial_\mu\phi\,\partial^\mu\phi-\tfrac12\mu^2\phi^2+g\rho\,\phi,
\qquad d^4x=c\,dt\,dx\,dy\,dz .
$$

The first two terms are the standard kinetic and mass terms of a relativistic scalar field, with the sign that makes the energy positive; the third is the source coupling, whose sign convention is fixed below by the requirement that like sources attract. The action is a real central scalar, and the field is a single real function, so the variation is elementary.

### The Field Equation

The Euler–Lagrange equation for the single component $\phi$ is

$$
\frac{\partial\mathcal{L}}{\partial\phi}-\partial_\mu\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi)}=0
\quad\Longrightarrow\quad
-\mu^2\phi+g\rho+\Box\phi=0 ,
$$

that is,

$$
\boxed{\;\left(\Box-\mu^2\right)\tilde{\Phi}=-g\rho\,e_0 .\;}
$$

The operator $\Box-\mu^2$ is a **central scalar** differential operator with real coefficients, so it acts on the field by acting on the single component: the biquaternion-valued field equation and the ordinary scalar equation say the same thing. This is the first place the center is used. For a biquaternion-valued field with all four components active, the same operator would act componentwise and produce four decoupled scalar equations, none of which mixes the components; a genuinely multi-component field requires a noncentral operator, and the framework's only such operators are the module-theoretic ones described in the companion articles. The scalar field is the case in which the central operator and the single component match.

The free field obeys

$$
\left(\Box-\mu^2\right)\tilde{\Phi}=0 ,
$$

the biquaternionic Klein–Gordon equation of the companion article, here read as a **classical** wave equation. Its wave operator is the norm form of the gradient, $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}$, which is the algebraic content the biquaternion writing makes visible. Because the equation is second order in time, the field and its time derivative are the two pieces of initial data, exactly as for any classical wave field.

## Plane Waves and the Range of the Field

### The Plane-Wave Solutions

In the absence of sources, write a plane wave

$$
\tilde{\Phi}(x)=\tilde{\Phi}_0\,e^{i(\mathbf{k}\cdot\mathbf{x}-\omega t)}, \qquad \tilde{\Phi}_0\in\mathbb{C},
$$

with the central phase $e^{i(\mathbf{k}\cdot\mathbf{x}-\omega t)}$ understood as multiplication by a central element. Because $\Box=-\partial_t^2/c^2+\Delta$ acts on it as $\omega^2/c^2-k^2$, the free equation requires the **dispersion relation**

$$
\omega^2=c^2k^2+c^2\mu^2=c^2k^2+\frac{m^2c^4}{\hbar^2} .
$$

The wave speed is frequency-dependent and exceeds $c$ for every nonzero $\mu$, $\omega/k=c\sqrt{1+\mu^2/k^2}>c$: the field is dispersive, and the phase velocity is not the signal velocity. The front velocity is $c$, since the second-order hyperbolic equation has the same characteristic cone as the wave equation; the cone is the framework's zero-divisor cone, the subject of the companion article *The Light Cone as the Biquaternion Zero-Divisor Cone*. The classical statement is that a disturbance cannot be signalled faster than $c$, whatever the phase velocity.

### The Range of the Field

A static field obeys

$$
\left(\Delta-\mu^2\right)\phi=-g\rho .
$$

The operator $\Delta-\mu^2$ is the inverse of a screened Poisson operator, and its Green's function decays exponentially:

$$
G_\mu(\mathbf{x})=\frac{e^{-\mu r}}{4\pi r}, \qquad
\left(\Delta-\mu^2\right)G_\mu=-\delta^{(3)}(\mathbf{x}) ,
$$

with $r=|\mathbf{x}|$. The scale $\mu^{-1}$ is the **range** of the field: beyond a few $\mu^{-1}$ the field is exponentially suppressed, while in the massless case $\mu=0$ the decay is only $1/r$ and the range is infinite. This is the classical reason a massive scalar exchange produces a short-range force and a massless one a long-range force, and it is why the inverse-square law is singled out by the massless central scalar.

## The Static Central Solution

### The Point Source

Let the source be a point of strength $Q$ at the origin, $\rho(\mathbf{x})=Q\,\delta^{(3)}(\mathbf{x})$. The static field is

$$
\phi(\mathbf{x})=gQ\,G_\mu(\mathbf{x})=\frac{gQ\,e^{-\mu r}}{4\pi r},
\qquad\text{that is}\qquad
\tilde{\Phi}(\mathbf{x})=\frac{gQ\,e^{-\mu r}}{4\pi r}\,e_0 ,
$$

the **Yukawa field**. In the massless limit,

$$
\tilde{\Phi}(\mathbf{x})=\frac{gQ}{4\pi r}\,e_0 ,
$$

the $1/r$ potential that the central-force articles treat as the inverse-square force's potential energy.

Two properties of the solution matter for what follows. It is **static** and **spherically symmetric**, being a function of $r=|\mathbf{x}|$ alone, and its value at every point lies in the center, so it commutes with the rotation generators and carries no direction. A distribution of sources superposes: for $\rho=\sum_aQ_a\delta^{(3)}(\mathbf{x}-\mathbf{x}_a)$ the field is the sum of the individual Yukawa fields, because the equation is linear and the center is closed under addition.

### The Field of a Moving Source

It is worth recording the moving case, both for completeness and because the absence of a magnetic counterpart is the subject of a later section. The retarded Green's function of the massless wave operator is $G_{\text{ret}}(x)={\delta(t'-t+|\mathbf{x}-\mathbf{x}'|/c)}/(4\pi|\mathbf{x}-\mathbf{x}'|)$, and for a point source moving on a worldline $\mathbf{x}_s(t)$ the field is the scalar Liénard–Wiechert potential

$$
\tilde{\Phi}(\mathbf{x},t)=\frac{gQ}{4\pi}\,\frac{1}{R\left(1-\boldsymbol{\beta}\cdot\hat{\mathbf{n}}\right)}\,e_0 ,
\qquad
R=|\mathbf{x}-\mathbf{x}_s(t_r)|,\quad
\boldsymbol{\beta}=\frac{\mathbf{v}_s}{c},\quad
\hat{\mathbf{n}}=\frac{\mathbf{x}-\mathbf{x}_s(t_r)}{R},
$$

evaluated at the retarded time $t_r=t-R/c$. The formula is the scalar counterpart of the electromagnetic Liénard–Wiechert potential: the retarded denominator is the same, but there is **one** potential function and no vector potential, so there is no field strength tensor, no electric–magnetic decomposition, and no magnetic field. A moving scalar source produces only a scalar potential, and this is the field-theoretic face of the subcategory's subject.

## The Field Energy and the Stress–Energy

### The Energy Density

The stress–energy tensor of the central scalar field is that of a real scalar field, computed in the companion article *Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form*. Its energy density is

$$
T^{00}=\frac{1}{2c^2}\dot{\phi}^2+\tfrac12(\nabla\phi)^2+\tfrac12\mu^2\phi^2>0 ,
$$

positive for every field configuration, and its conservation is the statement $\partial_\mu T^{\mu\nu}=0$ on shell. The three terms are the kinetic, gradient and mass contributions; all three are central scalars, and their positivity is what fixes the sign of the action above. For a **static** field the kinetic term vanishes and the energy is stored in the gradient and in the mass term, and the momentum density vanishes, $T^{0j}=0$: a static central scalar field carries energy but no momentum, which is the field-theoretic statement that it is a static central configuration.

### The Energy of the Static Field

The energy of the static solution is computed from the energy density. For the massless field $\phi=A/r$ with the useful abbreviation

$$
A=\frac{gQ}{4\pi},
$$

the gradient energy outside a sphere of radius $a$ is

$$
E_{\text{field}}(a)=\int_{r>a}\tfrac12(\nabla\phi)^2\,d^3x
=2\pi A^2\int_a^{\infty}\frac{dr}{r^2}
=\frac{2\pi A^2}{a}=\frac{g^2Q^2}{8\pi a},
$$

using $\nabla\phi=-A\hat{\mathbf{r}}/r^2$. The result is exact and was checked by direct integration. It has two features worth naming. It is **positive**, as it must be; and it **diverges as $a\to0$**, so the field energy of a point source is infinite. The massive case has the same short-distance divergence, since the Yukawa field still behaves as $A/r$ as $r\to0$; the exponential only cuts off the long-distance tail.

The divergence is the classical self-energy of the point-source idealization and not a property of the framework. A source of finite extent gives a finite field energy, and the self-energy is one of the standard reasons a point particle cannot be treated as a structureless classical object in a field theory. In the present article the source is prescribed, so the divergence does not affect the dynamics of the test source in the field, which is finite; it is recorded because it bounds the sense in which the static solution is physical.

## The Test Particle and the Reduction to the Central-Force Problem

### The Interaction Energy

Let a test source of coupling $g'$ be placed in the field of the point source. The interaction Lagrangian of the test source is $g'\rho'\,\phi$ with $\rho'$ its density, so its potential energy in the field is

$$
U(r)=-g'\,\phi(r)=-\frac{gg'Q\,e^{-\mu r}}{4\pi r}=-\frac{\kappa\,e^{-\mu r}}{r},
\qquad \kappa=\frac{gg'Q}{4\pi}>0 ,
$$

the sign following from the Hamiltonian sign $H_{\text{int}}=-L_{\text{int}}$ and the convention that like sources attract. The interaction energy is negative and increases to zero at infinity: the configuration is bound, and the massless limit is the inverse-square attraction

$$
U(r)=-\frac{\kappa}{r}, \qquad
\mathbf{F}=-\nabla U=-\frac{\kappa}{r^2}\,\hat{\mathbf{r}},
$$

which is exactly the inverse-square force of the central-force articles, with $\kappa>0$ for attraction.

### Why the Force Is Central

The force is central for an algebraic reason. The field $\tilde{\Phi}=\phi(r)e_0$ is valued in the center and is therefore invariant under the rotation group, and its gradient transforms as a vector:

$$
\mathbf{F}(\mathbf{x})=-\nabla U(r)=g'\,\nabla\phi(r)=g'\,\frac{d\phi}{dr}\,\hat{\mathbf{r}} ,
$$

a real vector parallel to the position, pointing inward because $\frac{d\phi}{dr}<0$ for the attractive field. In the algebra's criterion, $[\mathbf{r},\mathbf{F}]=0$, so the force commutes with the position and the angular momentum $\mathbf{L}=\mathbf{r}\times\mathbf{p}=\tfrac12[\mathbf{r},\mathbf{p}]$ is conserved. The potential energy $U(r)e_0$ is a **central scalar**, an element of the center, so the whole configuration is a central-scalar configuration in the sense of the companion article *The Central-Scalar Limit of Classical Mechanics in Biquaternionic Form*: scalar data in the center, configuration a real vector in the material sector, no vector direction of the informational sector occupied. The field-theoretic origin of a central force is therefore the centrality of the field's value space, not an assumption about the force law.

### Which Central-Force Results Apply

The reduction is exact, and it hands the problem to the two sibling articles.

- **Massless central scalar.** For $\mu=0$ the potential is $U=-\kappa/r$ and the relativistic orbit is exactly the precessing conic of the companion article *The Relativistic Central Force Problem in Biquaternionic Form*: $r=p/[1+e\cos\omega(\theta-\theta_0)]$ with $\omega^2=1-\kappa^2/(c^2L^2)$, bound orbits requiring $L>\kappa/c$. The non-relativistic limit is the Kepler and Coulomb orbit of the companion articles *Central Forces and the Classical Kepler Problem in Biquaternionic Form* and *The Classical Coulomb Problem and Its Hidden SO(4) Symmetry in Biquaternionic Form*.
- **Massive central scalar.** For $\mu>0$ the potential is the Yukawa potential $U=-\kappa e^{-\mu r}/r$ and the force is $F=-\kappa e^{-\mu r}(\mu r+1)/r^2$. The relativistic Binet equation of the sibling article applies with this force, but the equation is nonlinear and the orbit is not a conic; the precessing-conic solution is special to the massless case. The field-theoretic statement is that a massive scalar exchange produces a short-range central force whose orbits are not closed, and the massless exchange produces the inverse-square force whose relativistic orbits are the exact precessing conics.

The reduction also identifies the coupling's meaning: $\kappa=gg'Q/(4\pi)$ is a product of the field coupling, the test coupling and the source strength. The framework does not fix these numbers, exactly as the central-force article does not fix $\kappa$; what the framework fixes is the **form** of the force once the field is the central scalar.

## The Central Phase and Its Current

### The Central Phase

A complex central scalar field carries the transformation

$$
\tilde{\Phi}\ \longrightarrow\ e^{i\alpha}\,\tilde{\Phi}, \qquad \alpha\in\mathbb{R},
$$

which acts on the single complex component by multiplication. Because $i$ is central, $e^{i\alpha}$ commutes with every element of $\mathbb{B}$ and in particular with the gradient, so the transformation is a symmetry of the field equation for constant $\alpha$. This is the framework's **central phase**, the natural continuous symmetry of the algebra; for the central scalar field it is literally a global $U(1)$ acting on the scalar line, and it is the reason the scalar field can carry a charge at all.

### The Conserved Current

The complex Lagrangian

$$
\mathcal{L}=-\tfrac12\,\partial_\mu\phi^*\,\partial^\mu\phi-\tfrac12\mu^2|\phi|^2
$$

is invariant under the central phase, and Noether's theorem gives the conserved current

$$
j^\nu=\frac{i}{2}\left(\phi^*\partial^\nu\phi-\phi\,\partial^\nu\phi^*\right),
\qquad
\partial_\nu j^\nu=0\ \text{on shell},
$$

whose conservation was checked on a superposition of two on-shell plane waves of different momenta. The time component $j^0$ is the charge density and its integral is the charge; the spatial components are the current. The current vanishes identically for a real field, which is the classical statement that a real scalar is its own antiparticle and carries no charge.

That the current's normalization is a convention, while its conservation is not, is worth stating: any multiple of $j^\nu$ is conserved, and the unit of charge fixes the multiple. What the framework supplies here is not the normalization but the identification of the symmetry with the algebra's central phase.

## Why There Is No Intrinsic Magnetism

The subcategory to which this article belongs is that of effects **without intrinsic magnetism**, and the central scalar field is the field-theoretic reason the restriction is a natural one. Three independent statements combine.

**No internal vector, hence no spin.** The value space is the center, the rotationally invariant subspace of $\mathbb{B}$. A field valued there has no internal direction for a rotation to act on and no internal vector degree of freedom to precess; it carries spin $0$. A magnetic moment requires either an intrinsic spin or an internal current distribution, and a single complex scalar has neither. This is the algebraic statement of the subcategory's subject, and it is the field-theoretic counterpart of the central-scalar limit's exclusion of internal vectors.

**No vector potential, hence no magnetic field.** The field equation is a single scalar equation. There is no gauge connection, no field-strength tensor and no electric–magnetic decomposition; the static solution has a scalar potential only, and the moving solution of the previous section has a scalar Liénard–Wiechert potential and no vector counterpart. The absence of a magnetic field is not a small effect or a limit; it is the statement that the theory has no object out of which a magnetic field could be built.

**No spin–orbit coupling of intrinsic origin.** The couplings that make an intrinsic magnetic moment visible — the spin–orbit coupling, the Zeeman and Stern–Gerlach interactions — all require the internal vector that the central scalar does not have. The orbital magnetic effects of a moving charge, such as the field of a moving test particle's current, are present for any charged particle and are not intrinsic magnetism; they are the orbital effects treated in the companion article on the classical Coulomb problem, and they are outside the present article.

The three statements are the field-theoretic form of the spin-zero condition: a central scalar field has one component, its value space is the rotationally invariant subspace, and everything that would produce an intrinsic magnetic moment is absent by construction.

## The Algebraic Reading

### What the Algebra Supplies

**The value space.** The center is the unique rotationally invariant subspace of $\mathbb{B}$, so the algebra determines where a scalar field must live rather than leaving it a choice.

**The centrality of the field equation.** The d'Alembertian is central and scalar, so the biquaternion field equation acts on the single component and no coupling between components is introduced. The reduction to one scalar equation is a consequence of the algebra, not an ansatz.

**The centrality of the force.** A centrally valued field is a rotational scalar, so the potential it generates is a central scalar and the force on a test source is a real vector parallel to the position. The link from the field's value space to the force's centrality is algebraic.

**The central phase.** The global $U(1)$ of the complex scalar is the algebra's central phase, and its conservation is Noether's theorem applied to a central transformation.

**The closure of the center.** The center is a subalgebra, so polynomial self-interactions of the scalar stay in the center and are available without leaving the scalar sector.

### What the Algebra Does Not Contain

**The numbers.** The couplings $g$, $g'$, the source strength $Q$ and the mass parameter $\mu$ are not fixed by the algebra. It fixes the form of the potential once they are given, and the inverse-square law follows from the massless case, but it does not select the massless case.

**The source's dynamics.** The source density is prescribed. A dynamical source, with its own equation of motion and its back-reaction on the field, is a coupled system that the present article does not treat; the framework's field–matter coupling is developed in the articles on the Lorentz force and on the external-field problem, and for the scalar field it is simpler and remains to be written out.

**The renormalization of the self-energy.** The divergence of the point-source field energy is a classical statement, and its resolution belongs to whatever regulates the source at short distances; the algebra does not regulate it.

## Open Questions

1. **The value of the couplings and the mass.** The framework fixes the form of the central potential and leaves $g$, $g'$, $Q$ and $\mu$ free. Is there any algebraic constraint on their ratios, in the way that the barrier condition $L>\kappa/c$ constrains the angular momentum? Not known.

2. **Self-interaction in the center.** Because the center is closed under multiplication, a potential $V(\tilde{\Phi})$ polynomial in a central field is well defined and stays in the center. Whether the framework's scalar sector should be linear or self-interacting — and how a self-interacting central scalar relates to the Higgs sector treated elsewhere in the corpus — is open.

3. **The dynamical source and back-reaction.** A source with its own equation of motion, radiating into the scalar field and recoiling, is the scalar analogue of the electromagnetic radiation-reaction problem. The framework treats prescribed sources here and the back-reaction elsewhere; the scalar case is not worked out.

4. **The classical self-energy.** The divergence of the point-source field energy is the classical self-energy problem. Whether the framework has a preferred short-distance structure — a minimal length, a smeared source, or the algebra's own discreteness — that regulates it is not known.

5. **The relation to the gauge principle.** The central phase is a global symmetry of the central scalar field. Whether it can be gauged, and whether a gauged central phase has a biquaternionic interpretation distinct from ordinary $U(1)$ electromagnetism, is a question for the articles on the gauge principle rather than for a classical scalar field.

6. **Coupling to the informational sector.** The field occupies the center and therefore one scalar direction of each sector. Whether the scalar direction of $\mathbb{M}_+$ couples to the informational structures of the framework, and how a scalar source would appear to an informational observer, is the central open question shared with the foundational article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*.

7. **Curved spacetime and the range.** The Yukawa range $\mu^{-1}$ and the $1/r$ tail are computed on flat spacetime. Whether the framework's local complex structure modifies the range in a medium, as it modifies the speed of light, is not addressed.

## Summary

The central scalar field in the biquaternion framework is a field valued in the center $\mathbb{C}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{e_0,ie_0\}$,

$$
\tilde{\Phi}(x)=\phi(x)e_0 ,
$$

a single complex scalar component. Because it is central it commutes with the biquaternionic gradient and with every rotation, so it is a Lorentz scalar and a rotational scalar, and its classical action

$$
S=\int\left[-\tfrac12\partial_\mu\phi\,\partial^\mu\phi-\tfrac12\mu^2\phi^2+g\rho\,\phi\right]d^4x,
\qquad \mu=\frac{mc}{\hbar},
$$

has the field equation $(\Box-\mu^2)\tilde{\Phi}=-g\rho\,e_0$, with $\Box$ central and scalar. The free field is dispersive with $\omega^2=c^2k^2+c^2\mu^2$ and has range $\mu^{-1}$.

A static point source of strength $Q$ produces the Yukawa field

$$
\tilde{\Phi}=\frac{gQ\,e^{-\mu r}}{4\pi r}\,e_0,
\qquad\text{whose massless limit is}\qquad
\tilde{\Phi}=\frac{gQ}{4\pi r}\,e_0 .
$$

The static field's energy density is $T^{00}=\tfrac12(\nabla\phi)^2+\tfrac12\mu^2\phi^2>0$, and the massless field's energy outside a sphere of radius $a$ is $E_{\text{field}}=2\pi A^2/a$ with $A=gQ/(4\pi)$, positive and divergent at a point source.

A test source of coupling $g'$ has the central potential energy

$$
U(r)=-\frac{\kappa e^{-\mu r}}{r}, \qquad \kappa=\frac{gg'Q}{4\pi}>0,
$$

whose massless limit $U=-\kappa/r$ is exactly the inverse-square central potential of the sibling article *The Relativistic Central Force Problem in Biquaternionic Form*. The force is central because the field's value space is the rotationally invariant subspace, so $[\mathbf{r},\mathbf{F}]=0$, the angular momentum $\mathbf{L}=\tfrac12[\mathbf{r},\mathbf{p}]$ is conserved, and the orbit is the precessing conic of that article in the massless case.

The complex field carries the algebra's central phase $\tilde{\Phi}\mapsto e^{i\alpha}\tilde{\Phi}$, with conserved current $j^\nu=\tfrac{i}{2}(\phi^*\partial^\nu\phi-\phi\,\partial^\nu\phi^*)$. A central scalar field has one component and no internal vector direction, so it has no spin, no vector potential and no intrinsic magnetic moment: the absence of intrinsic magnetism is a consequence of the field's living in the center, and it is the field-theoretic content of the spin-zero subcategory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra; $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$; central $i$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}}=\operatorname{span}_{\mathbb{R}}\{e_0,ie_0\}$ | Center of $\mathbb{B}$; the scalar field's value space |
| $\mathbb{C}_{\mathbb{B}}\cap\mathbb{M}_+=\mathbb{R}e_0$, $\mathbb{C}_{\mathbb{B}}\cap\mathbb{M}_-=\mathbb{R}ie_0$ | The center's one real direction in each sector |
| $\tilde{\Phi}=\phi e_0$ | Central scalar field; $\phi$ a complex scalar function |
| $\phi_1,\phi_2$ | Real and imaginary parts of $\phi$ |
| $\tilde{\nabla},\bar{\tilde{\nabla}}$, $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta$ | Gradient, conjugate gradient, d'Alembertian (central, scalar) |
| $\mu=mc/\hbar$ | Mass parameter, the inverse range; classically only $\mu^{-1}$ matters |
| $\mathcal{L}=-\tfrac12\partial_\mu\phi\partial^\mu\phi-\tfrac12\mu^2\phi^2+g\rho\phi$ | Real scalar Lagrangian |
| $(\Box-\mu^2)\tilde{\Phi}=-g\rho e_0$ | Field equation with source |
| $\omega^2=c^2k^2+c^2\mu^2$ | Dispersion relation of the free field |
| $G_\mu=e^{-\mu r}/(4\pi r)$ | Screened Green's function; $(\Delta-\mu^2)G_\mu=-\delta^{(3)}$ |
| $Q,\rho,g,g'$ | Source strength, source density, field coupling, test coupling |
| $\tilde{\Phi}=gQe^{-\mu r}/(4\pi r)\,e_0$ | Yukawa field of a point source; $gQ/(4\pi r)\,e_0$ for $\mu=0$ |
| $\boldsymbol{\beta}$, $R$, $t_r$ | Source velocity over $c$, retarded distance, retarded time |
| $T^{00}=\tfrac12\dot\phi^2/c^2+\tfrac12(\nabla\phi)^2+\tfrac12\mu^2\phi^2$ | Energy density, positive |
| $A=gQ/(4\pi)$; $E_{\text{field}}=2\pi A^2/a$ | Field amplitude; massless field energy outside radius $a$ |
| $U(r)=-\kappa e^{-\mu r}/r$, $\kappa=gg'Q/(4\pi)$ | Central interaction energy; $\kappa>0$ attractive |
| $\mathbf{F}=-\nabla U=g'\,\nabla\phi=g'\,(d\phi/dr)\,\hat{\mathbf{r}}$ | Central force on the test source (inward) |
| $j^\nu=\tfrac{i}{2}(\phi^*\partial^\nu\phi-\phi\partial^\nu\phi^*)$ | Conserved current of the central phase; $\partial_\nu j^\nu=0$ |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the scalar field, its stress–energy tensor and the retarded Green's function.
- Lev Landau and Evgeny Lifshitz, *Quantum Mechanics: Non-Relativistic Theory* (Pergamon, 1977), for the screened Coulomb (Yukawa) potential and its range.
- Hideki Yukawa, "On the interaction of elementary particles I," *Proceedings of the Physico-Mathematical Society of Japan* **17** (1935) 48–57, for the massive scalar exchange and the finite range.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I: Foundations* (Cambridge, 1995), for the scalar field action, its Noether currents and the transformation of scalar fields under the Lorentz group.
- Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the complex scalar field, its global $U(1)$ symmetry and the conserved current.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the Liénard–Wiechert potentials and the contrast between scalar and vector potentials.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of scalar fields and their conserved currents.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the spacetime-algebra formulation of scalar field theory.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the center of a Clifford algebra, its idempotents and its relation to the scalar representation.
