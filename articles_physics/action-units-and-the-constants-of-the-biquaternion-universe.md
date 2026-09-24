# __Action, Units, and the Constants of the Biquaternion Universe__

## Introduction

The biquaternion framework is a statement about **form**. It fixes which quadratic form the algebra carries, which of its subspaces is material and which informational, which equations are linear in the field, and which phase is central. It fixes no **magnitude**. The algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ contains no dimensionful parameter and no free real parameter at all: every structure constant in its multiplication table is an integer, and its norm form is canonical. There is therefore nowhere inside the algebra for a unit to enter, and every unit that physics uses has to be brought in from outside.

The article is about action and about its unit. Action is the difference of kinetic and potential energy accumulated along a trajectory, $S=\int(T-V)\,dt=\int L\,dt$. Its dimension is energy × time, equivalently momentum × length, and its SI unit is the joule-second. Angular momentum, and the product of a generalized coordinate with its conjugate momentum, share that unit, and the section on action and angular momentum below asks why — the answer being that in this algebra the three are read off one object.

That much is already recorded, in one line, by the companion article *The Empirical Status of the Biquaternion Framework*: the algebra is dimensionless, and $c$, $\hbar$, $m$ and $e$ are inserted. The present article is the systematic treatment of that line. Three questions are left open by it, and each is taken up below.

1. **What does the algebra's dimensional blindness force?** The norm form is a sum of four squares, and a sum of four squares is meaningful only when its terms are commensurable. The algebra's own quadratic form therefore already constrains the units of its coefficients. The first result of this article is that this constraint is what the $ict$ convention amounts to: not a bookkeeping choice that could have gone the other way, but what a single quadratic form requires of a single physical object.
2. **Where does each imported constant enter?** The constants are not inserted at one place. Each enters at a different point of the structure — inside the norm form, in the exponent of the phase, in the boundary condition on a thermal state — and the point of entry is the sharpest available statement of what each constant is *for*. The second section develops a taxonomy of the constants by point of entry, and records the same division as it appears in the SI itself, where the dimensionful constants are defined and the dimensionless ones measured.
3. **Why do action and angular momentum share a unit?** Action, angular momentum, and the symplectic pairing of a configuration with its conjugate momentum all have the dimensions of energy × time. In the framework they are not three quantities that happen to share a unit: they are the scalar and the vector parts of one biquaternion product, $\tilde q\tilde p$. This is the structural core of the article.

The article is a **limitation statement**, of the same species as the companion articles *Conventions in the Biquaternion Universe* and *The Empirical Status of the Biquaternion Framework*: its content is what the algebra supplies and what it does not. It adds no physics, and it derives no constant. It is written because the corpus makes the dimensional remarks piecemeal — the Stern–Gerlach article records that $\hbar$ is supplied from outside, the electron article that the mass and the charge are inserted, the $g-2$ article that the algebra fixes the ratio and not the scale — and those remarks have no common home. The home is here.

The conventions are those of the companion articles, unchanged. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$ and $e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$; the scalar imaginary is $i$, central, with $i^2=-1$. The material sector is $\mathbb{M}_-=\mathrm{span}_{\mathbb{R}}\{ie_0,e_1,e_2,e_3\}$ (imaginary scalar, real vector), the informational sector is $\mathbb{M}_+=\mathrm{span}_{\mathbb{R}}\{e_0,ie_1,ie_2,ie_3\}$ (real scalar, imaginary vector), the real-quaternion subspace is $\mathbb{H}_{\mathbb{B}}$, and the center is $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$. The norm form is $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}=\sum_\mu Q_\mu^2$, the trace is normalized by $\mathrm{Tr}(e_0)=2$, and the trace formula is $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$. The material coordinate is $\tilde{X}=ict\,e_0+\mathbf{x}$, the biquaternionic gradient is $\tilde{\nabla}=e_0\partial_{ict}+e_1\partial_x+e_2\partial_y+e_3\partial_z$, and the series d'Alembertian is $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta$. The speed of light in the medium is $c=1/\sqrt{\epsilon\mu}$ and the vacuum speed is $c_0=1/\sqrt{\epsilon_0\mu_0}$; $\hbar=h/2\pi$ is the reduced Planck constant, $h$ the Planck constant, and $k_B$ the Boltzmann constant.

The companion articles used below are:

- Companion article *Conventions in the Biquaternion Universe*, for the algebra, the conjugations, the three levels of "metric", the d'Alembertian convention, and the presentation rules this article follows.
- Companion article *The Local Complex Structure and the Speed of Light*, for the sense in which the complex structure carries a scale $c$, and for the two routes that fix it.
- Companion article *The Empirical Status of the Biquaternion Framework*, for the standing position that the algebra is dimensionless and makes no distinguishing prediction.
- Companion article *Lagrangian and Hamiltonian Mechanics in Biquaternionic Form*, for the configuration quaternion, the conjugate momentum, and the product $\tilde q\tilde p$.
- Companion article *The Action Principle and the Classical Limit as Stationary Phase in Biquaternionic Form*, for the action, the symplectic potential, and the dimensionless ratio that governs the classical limit.
- Companion article *The Stern–Gerlach Experiment in Biquaternionic Form*, for the spin observable and the imported scale $\hbar/2$.
- Companion article *The KMS Condition and the Biquaternion Framework*, for the inverse temperature $\beta=\hbar/(k_BT)$ and the thermal circle.
- Companion article *The Classical Origin of g = 2 in Biquaternionic Form*, for the distinction between the ratio the algebra fixes and the scale it does not.

## The Algebra Has No Scale

### All Structure Constants Are Pure Numbers

The multiplication table of $\mathbb{B}$ is fixed once and for all:

$$
e_0=1,\qquad e_k^2=-e_0,\qquad e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l \quad (j\neq k).
$$

Every constant appearing on the right-hand side is $0$, $+1$ or $-1$. There is no free real parameter in the algebra, no modulus, no coupling, nothing that could carry a unit. The same is true of the norm form and of the four conjugations: they are canonical, and none of them introduces a scale. An algebra whose constants are all integers has nowhere to put a unit, and that is what makes the framework's silence about magnitudes structural rather than accidental.

The contrast that fixes the idea is with a structure that *does* carry a scale. A lattice carries its spacing; a string carries its tension; a field theory carries the masses of its fields. Each of those supplies a dimensionful number that the structure itself provides. The biquaternion algebra provides none, and the reason is visible in the multiplication table: the algebra is generated by four elements whose products close with integer coefficients.

### Rescaling Is Not an Automorphism, but It Is an Ambiguity

A rescaling $\tilde{Q}\mapsto\lambda\tilde{Q}$ with $\lambda>0$ is real-linear, but it is not an algebra homomorphism:

$$
(\lambda\tilde{A})(\lambda\tilde{B})=\lambda^2\tilde{A}\tilde{B}\neq\lambda(\tilde{A}\tilde{B}).
$$

This is worth stating carefully, because the algebraic fact has a physical reading. The multiplication of the algebra is not invariant under a rescaling of its elements — the product of two rescaled elements acquires a factor $\lambda^2$ — so the scale of an element of the algebra is not a redundancy of the algebra. It is data the algebra does not contain, and which must therefore be supplied by the identification that says what the element represents. When the framework says that $\tilde{X}=ict\,e_0+\mathbf{x}$ *is* a displacement in metres, it is supplying that data. Nothing in the algebra did it.

There is an exception worth noting, because it is the only place where the algebra speaks about a scale at all. An element's norm form is homogeneous of degree two under the rescaling, $N(\lambda\tilde{Q})=\lambda^2N(\tilde{Q})$, so a *ratio* of norm forms is rescaling-invariant. The framework therefore has access to ratios and to pure numbers, and to nothing dimensionful. This is the algebraic root of the dichotomy that organises the whole article and is stated flatly in the summary: **the framework's outputs are pure numbers; its inputs are dimensionful.**

## The One-Unit Constraint

### A Sum of Squares Requires Commensurable Terms

The norm form of a general element is

$$
N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}=Q_0^2+Q_1^2+Q_2^2+Q_3^2 .
$$

This is a sum of four squares. It is a single scalar, and it is meaningful as a sum only if its four terms carry the same unit. It follows that **the four coefficients of a single element of $\mathbb{B}$ must share one unit**, whatever that unit is. The constraint is not imposed from outside and it is not a convention of the series; it is a property of the algebra's quadratic form. It applies to every element of the algebra that carries a physical interpretation, and it applies in both sectors.

The constraint is **per element, and not across elements**. The norm form of a four-displacement is a length squared; of a four-velocity, a speed squared; of a four-momentum, a momentum squared; of a four-potential, a potential squared — which is why the relativistic four-potential carries $\phi/c$ in its temporal slot rather than $\phi$, so that all four of its components share a unit. The unit varies from one physical quantity to the next, and with it the unit of $N$. What does not vary is the requirement that the four coefficients *inside* one element be commensurable. Stating the constraint precisely in this way avoids the error of supposing that the algebra carries one global unit.

### It Forces $ict$ in the Material Sector

Apply the constraint to a displacement. A displacement must have the four components of a displacement — that is, all four of length — since only then is its norm form a length squared, the invariant interval. The material sector's temporal coordinate therefore has to be a length, and the framework writes it

$$
\tilde{X}=ict\,e_0+\mathbf{x}, \qquad \mathbf{x}=x e_1+y e_2+z e_3 ,
$$

with $ict$ a length because $c$ is a speed. The alternative, $\tilde{X}=it\,e_0+\mathbf{x}$, gives

$$
N(\tilde{X})=(it)^2+\mathbf{x}^2=-t^2+\mathbf{x}^2 ,
$$

a sum of a time squared and a length squared, which is not a quadratic form on any single space. The same requirement, applied to the four-velocity $\tilde{U}=\gamma(ic\,e_0+\mathbf{v})$, gives $N(\tilde{U})=-c^2$; applied to the four-momentum $\tilde{P}=m\tilde{U}$ it gives the mass shell $N(\tilde{P})=-m^2c^2$. Three different elements, three different units, one constraint.

This is the precise sense in which the $ict$ convention has content. The companion article *Conventions in the Biquaternion Universe* records it as a convention, chosen so that the Minkowski interval emerges as the algebra's own norm form; the companion article *The Local Complex Structure and the Speed of Light* records that the local structure is "a structure *with* a scale, and that scale is $c$". What the present section adds is why: a quadratic form that is a sum of four squares admits no other assignment. The **phase** is forced by the sector — the temporal basis vector of $\mathbb{M}_-$ is $ie_0$, whose square is $-e_0$, and it is this that makes the interval Lorentzian rather than Euclidean — and the **scale** $c$ is forced by the commensurability. The convention's freedom is not in whether $c$ appears but in the value $c$ takes, which is empirical, and in the fact that $c$ is local in a medium.

One caution, in the spirit of the conventions article. The statement above is internal to the requirement that $N$ be *the* quadratic form of the algebra, read on a real four-dimensional subspace with a single unit. A framework that relaxed that requirement — a graded norm, or a norm form with coefficients of two different dimensions — would not be *wrong*; it would be a different framework. The claim here is that within this one the $ict$ assignment is not a free choice, and that its two ingredients (the phase and the scale) are forced for different reasons. The constraint also presumes a **local** action — an integral of a density along the coordinate, which is what makes the terms of $N$ comparable term by term; nonlocal actions are a recognised extension of the action principle and lie outside its reach.

### It Applies to the Gradient, and to the Mass Term

The constraint is not confined to the algebra's elements; it propagates to every operator the framework builds. The biquaternionic gradient is

$$
\tilde{\nabla}=e_0\,\partial_{ict}+e_1\,\partial_x+e_2\,\partial_y+e_3\,\partial_z ,
$$

and its four coefficients are all inverse lengths, because $ict$ and $x,y,z$ are all lengths. Its norm form is the d'Alembertian,

$$
\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta=\Delta-\frac{1}{c^2}\,\partial_t^2 ,
$$

a sum of four terms of dimension inverse length squared. The $c^{-2}$ in the last expression is not a choice of units; it is the scale of the imaginary time axis reappearing, exactly as the norm-form route requires.

The same reasoning constrains the mass parameter of a first-order equation. The companion article *Conventions in the Biquaternion Universe* writes the massive Dirac pair as

$$
\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L, \qquad \bar{\tilde{\nabla}}\tilde{\Psi}_L=m\tilde{\Psi}_R .
$$

Since $\tilde{\nabla}$ carries the dimension of inverse length, the parameter $m$ in this pair carries the same dimension once units are restored. In the second-order case the framework writes that dimension explicitly, as the inverse Compton length,

$$
(\Box-\mu^2)\tilde{\Phi}=0, \qquad \mu=\frac{mc}{\hbar},
$$

and the two are the same statement at the two orders. This is a small instance of the general rule, and it is worth extracting: **the mass parameter of an equation built on $\tilde{\nabla}$ is an inverse length, so it necessarily contains both a mass and $\hbar$**. The algebra supplies the position of the mass term — linear and chirality-off-diagonal — and not its magnitude. It supplies the fact that a mass term must be an inverse length; it supplies neither the mass nor $\hbar$.

### The Constraint Is Where the Constants Enter

The one-unit constraint has a consequence that organises the rest of the article. If the algebra fixes where a unit must appear and not what it is, then the question "what is a given constant for?" becomes the question "at which point of the structure does that constant have to appear?" That is a question the framework can answer, and the answer differs from constant to constant. The next section is the taxonomy.

## The Constants as Points of Entry

Every dimensionful constant of physics must be imported, but the imports are not of the same kind. Each constant is needed at a different place, and what it does there is what it is. Five entries are distinguished below by their point of entry: inside the norm form, in the exponent of the phase, in the boundary condition of a thermal state, in the coupling of a field to geometry, and in the specification of what a physical object *is*.

| Constant | Converts | Enters through | Status |
|---|---|---|---|
| $c=1/\sqrt{\epsilon\mu}$ | time ↔ length | the material coordinate $ict$ and the norm form | role forced by the one-unit constraint; value empirical, and local in a medium |
| $\hbar$ | action ↔ phase | the exponent $e^{iS/\hbar}$ and the operator $\tilde{p}=-i\hbar\nabla$ | value imported; the algebra supplies the action, not its unit |
| $k_B$ | energy ↔ temperature | the thermal weight $e^{-E/k_BT}$ and the strip width $\beta=\hbar/(k_BT)$ | value imported; the imaginary-time direction is algebraic, the scale is not |
| $G$ | stress–energy ↔ curvature | the Einstein–Hilbert term of the spectral action | not supplied; flagged open in the corpus |
| $m$, $e$ | the algebra's dimensionless labels ↔ measured magnitudes | the mass shell, the mass term, the gauge coupling | imported without a role fixed by the algebra |

### $c$: the Commensuration of the Material Sector

$c$ is the only constant of the list whose *role* is fixed by the algebra and only whose *value* is empirical. It is the scale of the imaginary time axis, and without it the material sector's norm form cannot be written at all. The companion article *The Local Complex Structure and the Speed of Light* fixes it independently by two routes — the aperture of the null cone of the norm form, and the characteristic speed of the medium's wave operator — which agree and both give $c=1/\sqrt{\epsilon\mu}$. Nothing is added to that here; the point to record is the asymmetry. Of the six constants in the table, $c$ is the one the framework needs in order to state its own quadratic form.

### $\hbar$: the Action–Phase Exchange Rate

$\hbar$ enters where a phase is formed. The action $S=\int L\,dt$ has the dimensions of energy × time, and a phase is dimensionless, so the exponent must be

$$
\frac{S}{\hbar},
$$

a pure number. This is the framework's own account of $\hbar$: the companion article *The Action Principle and the Classical Limit as Stationary Phase in Biquaternionic Form* states that $\hbar$ enters "only as the inverse scale of the phase, as the parameter of an asymptotic expansion, and nowhere as a quantum of action attributed to a physical system".

Two consequences follow, and both are structural rather than computational.

First, the classical limit is a statement about a **dimensionless ratio**. The companion article *Similitudes Between the Poisson Bracket and the Quantum Commutator* records that "$\hbar\to0$" means an expansion in (typical action)$/\hbar$, not a physical process in which a constant is varied. The framework therefore computes the action in units of $\hbar$; it does not compute $\hbar$. The familiar criterion that quantum effects matter when the action approaches the Planck constant is, in this reading, the statement $S/\hbar\sim1$: a criterion about a ratio the algebra can form and a denominator the algebra cannot supply.

Second, $\hbar$ is the **unit of the operator algebra**. The informational sector's elements are dimensionless as algebra, and their physical dimensions are assigned by the identification. The corpus's spin observable makes the assignment visible,

$$
\tilde{S}_3=\frac{\hbar}{2}\,i e_3 ,
$$

where the algebra supplies $i e_3$ and the factor $\tfrac12$, and $\hbar$ is inserted. The companion article *The Stern–Gerlach Experiment in Biquaternionic Form* states the position exactly: the algebra "fixes the form of the observable but not the value of the quantum of action".

### $k_B$: Energy and the Thermal Circle

$k_B$ enters where an energy is compared with a temperature. In the framework this happens in the companion article *The KMS Condition and the Biquaternion Framework*, where the inverse temperature is

$$
\beta=\frac{\hbar}{k_B T},
$$

the correlation functions are analytic in the strip $0<\mathrm{Im}(t)<\beta$, and the imaginary time direction is compact with circumference $\beta$.

The structural interest of $k_B$ is that it enters **in series with $\hbar$**. The KMS condition says that the imaginary time direction is periodic; $\hbar$ converts the temperature into a time and $c$ converts that time into a length, so the thermal circle has circumference $\hbar c/(k_BT)$ in the material sector's units. The imaginary-time direction is algebraic — it is the direction of the $ie_0$ coordinate — and what the two constants do is give it a size. This is the same division of labour as in the norm form: the algebra supplies the direction and the phase, and the constants supply the scale.

### $G$, $m$ and $e$: the Scales With No Algebraic Role

The remaining constants enter at points the algebra does not single out. The gravitational coupling enters with the Einstein–Hilbert term, and the companion article on the Einstein field equations records that whether the algebra fixes the normalisation is open; the leading-order action is the spectral action, whose heat-kernel expansion supplies the term with the standard coefficient. The mass and the charge enter at the two places where a physical object is named: the mass shell $N(\tilde{P})=-m^2c^2$, which is a norm-form statement with a number in it, and the gauge coupling, which the corpus records as inserted.

The contrast with $c$ is sharp and is the content of the section. $c$ must appear for the algebra to state its own quadratic form; $\hbar$ must appear for a phase to exist; $k_B$ must appear for a temperature to be a time. None of $G$, $m$ or $e$ is required by any structure of the algebra. They are the parameters of the world the algebra is used to describe, and the framework's attitude to them is the one stated in the companion article *The Empirical Status of the Biquaternion Framework*: a dimensionless algebra that imports all its dimensional constants from outside fixes no scale, and therefore no signature.

### The Metrological Mirror: Defined Constants and Measured Ratios

The SI treats the constants of the table in exactly the way the dichotomy predicts, and the agreement is worth recording because it is an independent institution reaching the same division. The dimensionful constants are not measured; they are **defined**. The metre is defined through $c$, the kilogram through $h$ together with the caesium frequency, the ampere through $e$, and the kelvin through $k_B$: since the 2019 revision of the SI, $h$, $c$, $e$ and $k_B$ have exact values fixed by convention, and the units are realised from them; $\hbar$ is fixed with them, through $\hbar=h/2\pi$. Four of the entries in the table are therefore *defining* constants, and none of the four has a measured value.

The framework's position is the same statement from the other side. It cannot produce $c$, $h$, $e$ or $k_B$, because a dimensionful constant is a unit conversion and not a statement about the algebra. The SI does not measure them, for the same reason: there is nothing there to measure. What the SI cannot do is define away a **dimensionless** constant. The fine-structure constant $\alpha$ is not a defining constant and could not be one; it has to be measured, and its value is a fact. That is the metrological image of the article's central dichotomy — the dimensionful constants are definitions, the dimensionless ones measurements.

The exception proves the rule. $G$ is the one dimensionful constant in the table that the SI declines to define: it is measured, and it is the least precisely known of the fundamental constants. It is also the one entry whose *algebraic* role the corpus records as unsettled. The two facts are independent, but they point the same way.

The unit of action shows the conversion at work. The joule-second is the kilogram metre squared per second, equivalently the joule per hertz. Read as J⋅Hz⁻¹, the unit gives the operational content of $h$: it is the conversion factor between an energy and a frequency, which is what "the quantum of action" means at the one place where the constant is defined rather than measured.

## Action and Angular Momentum Are One Product

The dimensional identity that this section explains is elementary and well known: the joule-second is the unit of action, of angular momentum, and of the product of a canonical coordinate with its conjugate momentum. The framework's contribution is not the identity but its **algebraic seat**: the pairing that the action is built from, and the angular momentum, are the scalar and vector parts of the one product of a configuration with its conjugate momentum.

### The Product $\tilde q\tilde p$ in the Algebra

Let $\tilde q=q_0e_0+\mathbf{q}$ and $\tilde p=p_0e_0+\mathbf{p}$ be real quaternions, the configuration and its conjugate momentum of the companion article *Lagrangian and Hamiltonian Mechanics in Biquaternionic Form*. Their product is

$$
\tilde q\,\tilde p=(q_0e_0+\mathbf{q})(p_0e_0+\mathbf{p})
=q_0p_0+q_0\mathbf{p}+p_0\mathbf{q}+\mathbf{q}\mathbf{p} ,
$$

and the quaternion product of two pure vectors is $\mathbf{q}\mathbf{p}=-\mathbf{q}\cdot\mathbf{p}+\mathbf{q}\times\mathbf{p}$. Hence

$$
\tilde q\,\tilde p=\bigl(\underbrace{q_0p_0-\mathbf{q}\cdot\mathbf{p}}_{\text{scalar part}}\bigr)
+\bigl(\underbrace{q_0\mathbf{p}+p_0\mathbf{q}+\mathbf{q}\times\mathbf{p}}_{\text{vector part}}\bigr).
$$

The scalar part is $q_0p_0-\mathbf{q}\cdot\mathbf{p}$, the contraction of the configuration with the momentum. The corpus's scalar pairing is the conjugate version of it, $\mathrm{Sc}(\bar{\tilde q}\tilde p)=\sum_\mu q_\mu p_\mu$ — the pairing the companion article's conventions define, and the one whose momentum-differential is the symplectic potential. In the **pure-vector case** $q_0=p_0=0$ — a particle in three dimensions, the case that carries the spatial reading — the product collapses to

$$
\tilde q\,\tilde p=-\mathbf{q}\cdot\mathbf{p}+\mathbf{q}\times\mathbf{p},
$$

so that the scalar part is (minus) the contraction and the vector part is the angular momentum $\mathbf{L}=\mathbf{q}\times\mathbf{p}$. The companion article records the same decomposition, and the caution that the clean separation holds for the pure-vector three-degree-of-freedom configuration; in the general four-degree-of-freedom case the scalar and vector parts mix the two scalar components with the two vector parts, and the statement below is read accordingly.

### Two Actions, One Dimension: Hamilton's and the Abbreviated

Only one of the functionals called "the action" has been used so far — Hamilton's, $S=\int L\,dt$, taken between fixed endpoints. There is a second, and it belongs here because it shares both the dimension and the algebra. The **abbreviated action** is the momentum summed along a path without regard to how the path is parametrised by time,

$$
S_0=\int \mathbf p\cdot d\mathbf q ,
$$

and Maupertuis's principle states that at fixed energy the true path is the one on which $S_0$ is stationary. Hamilton's action is an integral in time; the abbreviated action is an integral along the path; and both are momentum contracted with a coordinate displacement, which is why they share the dimension. The parametrisation is what the abbreviated action discards, and the energy is what it holds fixed.

The corpus already uses the abbreviated action, and one coordinate of it, under other names. Hamilton's **characteristic function** $\mathcal{W}$ of the companion article *The Action Principle and the Classical Limit as Stationary Phase in Biquaternionic Form*, the solution of $H(\tilde q,\partial_{\tilde q}\mathcal{W})=E$ for a time-independent problem, is the abbreviated action read as a function of the endpoint. The **action variable** $I_k=\oint p_k\,dq_k$ of the same article is the abbreviated action **of a single coordinate**: the abbreviated action is the full dot product $\int\mathbf p\cdot d\mathbf q$, the action variable is one coordinate's contribution to it, and the two coincide only for a system with one degree of freedom. This is the sense in which the action variable is the adiabatic invariant of the companion article *Hannay's Angles and the Classical Geometric Phase in Biquaternionic Form*. The dimensional identity of this section therefore has three members — action, abbreviated action (equivalently the characteristic function), and angular momentum — all of dimension action because each pairs a momentum with a displacement.

The two principles are not two names for one statement, because their **constraints are reversed**. Hamilton's principle fixes the two **events**, position and time at both ends, and varies at fixed $\Delta t$. Maupertuis's principle fixes the endpoints and the **energy** and leaves the time free; its solutions are therefore **orbits** — relations between coordinates with time as a parameter — rather than world lines. The same path with the same endpoints appears in both, but it carries **different times and different energies in the two forms**, so the second is not a rewriting of the first.

On the stationary path the two actions are related by a **Legendre transform**, which is what makes the reversal exact rather than rhetorical. For a time-independent potential, with the energy $E$ conserved and $\Delta t=t_2-t_1$,

$$
S=S_0-E\,\Delta t ,
$$

equivalently $S_0=S+E\,\Delta t$. The pair $(t,E)$ is the conjugate pair, so the passage between the two actions is the same transform that takes the Lagrangian to the Hamiltonian, and it reproduces the Hamilton–Jacobi statement $\partial S/\partial t=-E$, since the derivative of $S_0$ with respect to $E$ is $\Delta t$. Checked on the free particle, where $S=E\Delta t$ and $S_0=2E\Delta t$, and on the harmonic oscillator over a half period, where $S=0$ and $S_0=E\pi/\omega=E\,\Delta t$.

Two limits are worth naming. When no force acts — a rigid body with no net force — the two actions **coincide** and both principles reduce to Fermat's principle of least time, which is where the family meets optics. And in neither form is the stationary value of the action a maximum: a variation localised in a vanishingly short interval makes the kinetic term of the second variation dominate, so the extremum is a minimum or a saddle. This is why "the principle of least action", a common name for the family, is a misnomer — an elliptical orbit traversed in its two directions gives two paths of **equal** action, so neither direction is the least of anything.

### The Same Unit, Because It Is the Same Object

Both parts of $\tilde q\tilde p$ have the dimensions of length × momentum, which is action. But the framework's statement is stronger than a dimensional coincidence: the angular momentum is a **part of the same algebra element** whose scalar part is the contraction of the configuration with the momentum. There is no independent quantity "angular momentum" with a separately guaranteed unit; there is one biquaternion, of one dimension, whose two parts are read as two things. The two readings differ only in the conjugate convention on one factor — $\tilde q\tilde p$ has scalar part $q_0p_0-\mathbf q\cdot\mathbf p$, while $\mathrm{Sc}(\bar{\tilde q}\tilde p)=\sum_\mu q_\mu p_\mu$ is the Euclidean pairing — and that convention is fixed by the companion articles.

The same product appears at the other end of the theory. The symplectic potential of the companion article *The Action Principle and the Classical Limit as Stationary Phase in Biquaternionic Form* is

$$
\theta=\mathrm{Sc}\bigl(\bar{\tilde p}\,d\tilde q\bigr) ,
$$

momentum contracted with a configuration displacement, again of dimension action; and on shell the differential of the action is the difference of the pairing at the two endpoints, $dS=\theta_2-\theta_1$. The action variable of a periodic orbit,

$$
I_k=\oint p_k\,dq_k ,
$$

is that pairing integrated around a cycle. The symplectic potential, the differential of the on-shell action and the action variable are all readings of the scalar pairing of $\tilde q$ and $\tilde p$, and the angular momentum is the vector part of their product; all of them have the dimension of action, and the dimensional identity is the shadow of the algebraic one.

### Why One Constant Quantises Both

The point of the previous subsection is cashed here. The corpus quantises the two parts of $\tilde q\tilde p$ by one mechanism, and the comparison is sharpened by naming the two quanta separately.

The scalar part is quantised by the Bohr–Sommerfeld condition of the companion article *The WKB Approximation and the Hamilton–Jacobi Equation in Biquaternionic Form*,

$$
\oint p\,dx=2\pi\hbar\left(n+\tfrac12\right)=h\left(n+\tfrac12\right),
$$

the single-valuedness of the central phase $e^{iS/\hbar}$ around a closed orbit. The vector part is quantised by the spin spectrum: the observable is $\tilde{S}_3=\tfrac{\hbar}{2}ie_3$, its eigenvalues are half-integer multiples of $\hbar$, so the quantum of angular momentum is $\hbar$, with $\hbar/2$ the elementary value for spin $\tfrac12$.

The two quanta are not numerically the same, and the difference is worth being precise about. The quantum of *action* read off the closed orbit is $h$; the quantum of *angular momentum* is $\hbar$. The relation between them is exact and algebraic, $h=2\pi\hbar$, and the $2\pi$ is not a stray factor: it is the period of the phase. The orbit closes because $e^{iS/\hbar}$ is single-valued, and single-valuedness *is* $2\pi$ periodicity in the phase variable. The same $2\pi$ that makes the phase well defined therefore separates the quantum of the action from the quantum of the angular momentum. The two quanta are one constant written twice, $\hbar$ and $2\pi\hbar$: they differ by the phase's period and by nothing else. The $2\pi$ is not a second constant — but neither is it a structure constant of the multiplication table. It is the period of the exponential of the central imaginary unit $i$, so it is the central complex structure, not the quaternion arithmetic, that supplies it.

This is the framework's answer to why the unit of action and the unit of angular momentum are the same unit. What the two share is not one numerical value but one phase periodicity: the constant that converts the product into a phase is $\hbar$, and the quantisation of both the scalar pairing and the vector part of $\tilde q\tilde p$ is the single statement that this phase is $2\pi$-periodic. In the standard formalism the identity of units is a dimensional fact, recorded and used. Here it has an algebraic seat, and the $2\pi$ that distinguishes the two named quanta is supplied by the algebra's central complex structure rather than imported with $\hbar$.

A caution closes the section, in the manner of the corpus. This is a **reading of the identity, not a derivation of $\hbar$**. The algebra supplies the object and its two parts; it does not supply the constant by which the object is quantised, and the companion article *The Stern–Gerlach Experiment in Biquaternionic Form* is explicit that $\hbar$ "is supplied to the framework from outside". What the reading changes is not the physics but the bookkeeping: it removes the appearance of two coincidences — that the action and the angular momentum share a unit, and that one phase periodicity quantises both — and replaces it with one algebraic fact.

## What the Algebra Fixes

The dichotomy of the previous sections is worth tabulating, because it is the article's useful output. The left column lists what the algebra determines; the right column lists what has to be inserted. Nothing in the left column is dimensionful, and nothing in the right column is dimensionless.

| The algebra fixes | The algebra does not fix |
|---|---|
| the structure constants of the multiplication table (all integers) | the unit of any element |
| the norm form, up to the unit of its argument | the value of the unit; in particular $c$ |
| the signature of each sector, and the sign of the $ict$ term | the magnitude $c^2$ of the time–time coefficient |
| that a mass term is an inverse length | the mass, and $\hbar$ |
| that a phase is $e^{iS/\hbar}$, with $S$ the norm-form action | the value of $\hbar$ |
| the position of the constants, i.e. where each must appear | the value of any constant |
| pure numbers: $\mathrm{Tr}(e_0)=2$, the $\tfrac12$ of the idempotents, the half-angles of the rotors, the ratio $g=2$ | magnitudes: $\mu_B$, $m_e$, $e$, $\alpha$, $G$ |
| the dimension of the module (two), the number of sectors (two), of space directions (three) | any fundamental length or energy |

Two entries deserve a word.

**The half-angles.** The rotor $\tilde{R}=\cos(\theta/2)+\sin(\theta/2)\hat{\mathbf{m}}$ carries the half-angle because the group of unit quaternions double-covers the rotation group. The factor $\tfrac12$ is a pure number, and it is algebraic: it is the statement that a $2\pi$ rotation acts as $-1$. Once $\hbar$ is supplied as the unit of angular momentum, that pure number becomes the statement that angular momentum is quantised in half-integer multiples. The algebra supplies the half; the constant supplies the unit. This is a particularly clean instance of the dichotomy, and it is the reason the spin spectrum of the informational sector has the form it has.

**The ratio $g=2$.** The companion article *The Classical Origin of g = 2 in Biquaternionic Form* draws the distinction in the terms this article has been using: the algebra fixes the ratio of the magnetic moment to the spin, and therefore the dimensionless factor $g$, "because both quantities are carried by the same algebra and their weights are algebraically determined", while it "does not fix the scale of the moment, because the proportionality constant between the angular momentum and the numerical value of the moment involves $\hbar$ and the mass". A dimensionless ratio is algebraic; the scale is imported. The same article records the conclusion in the direction of this article: the algebra supplies the two, not the one Bohr magneton $\mu_B=e\hbar/2m_e$.

## Natural Units and What They Hide

The framework is often used with $\hbar=c=1$, and the corpus notes that the algebra literature routinely does so. The convention is efficient, and it is also the convention under which the subject of this article becomes invisible: with $c=1$, $ict$ and $it$ are indistinguishable in form; with $\hbar=1$, the action and the phase are the same object and the classical limit has no parameter. Both distinctions are exactly the ones the algebra is silent about and the ones physics supplies.

Two consequences are worth recording as guidance rather than as a rule.

First, the two constants do opposite things and are hidden by the same convention for different reasons. Setting $c=1$ removes the **commensuration** that made the material coordinate a length; setting $\hbar=1$ removes the **unit** in which the action is measured. A statement about the algebra's quadratic form is clearer with $c$ explicit, because the $c^{-2}$ in $\Box=\Delta-c^{-2}\partial_t^2$ is the same scale that makes $ict$ a length. A statement about quantisation is clearer with $\hbar$ explicit, because the Bohr–Sommerfeld offset $2\pi\hbar(n+\tfrac12)=h(n+\tfrac12)$ and the spin spectrum in units of $\hbar$ are statements about that unit.

Second, the corpus already follows this principle where it matters, and the pattern is consistent. The action articles keep $\hbar$ explicit because the phase and the classical-limit ratio depend on it; the relativistic articles keep $c$ explicit because the norm form and the mass shell depend on it; and the articles that set natural units are the ones whose subject is insensitive to both. Natural units are a presentation convention, and like the conventions collected in the companion article *Conventions in the Biquaternion Universe* they should be chosen per article for what the article is doing.

## Open Questions

**1. Is any dimensionless constant an algebraic output?** This is the sharpest question the article raises, and it follows from the dichotomy. If the algebra's outputs are pure numbers, then the constants it could in principle produce are exactly the dimensionless ones: the mass ratios, the mixing angles, and above all the fine-structure constant $\alpha=e^2/(4\pi\epsilon_0\hbar c)$. The companion article *The Empirical Status of the Biquaternion Framework* records that the corpus derives no value for a coupling, a mass ratio or a mixing angle, and that this is a limit of the derivation and not of experimental precision. The present article suggests why the search should be aimed there and not at $c$ or $\hbar$: a dimensionful constant is *unreachable by construction*, while a dimensionless one is not excluded by the argument given here. Whether any dimensionless relation is forced is open, and it is the natural continuation of this article.

**2. Is the ratio-only access sharp enough to be a constraint?** The algebra gives access to ratios of norm forms, and to nothing else. Is there a sharper statement available — a classification of the dimensionless invariants the algebra admits, against which the physical ones could be compared? A negative result, of the kind the companion article on what the algebra cannot do supplies for other properties, would be as valuable as a positive one.

**3. Is $k_B$ a scale of the same kind as $c$?** The thermal circle has circumference $\hbar c/(k_BT)$ in the material sector's units, and its direction is the algebraic imaginary-time direction. This makes $k_B$ look like $c$: a scale attached to an imaginary coordinate, without which that coordinate has no size. Whether that parallel can be made precise — whether there is a "local thermal structure" playing the role the local complex structure plays for $c$ — is not developed here.

**4. Does the one-unit constraint constrain any equation?** The constraint was applied above to the norm form, the gradient, and the mass term. A systematic survey of the series' equations for dimensional consistency, in the manner of a global check, would be a useful verification exercise; it is not attempted here.

**5. The gravitational coupling.** Whether the algebra fixes the normalisation of the Einstein–Hilbert-like term is recorded as open by the companion article on the Einstein field equations. The present article adds nothing to that question, and records it as the one entry of the constants table whose *role* is not yet settled, as opposed to merely its value.

## Summary

The biquaternion algebra carries no scale. Every structure constant in its multiplication table is an integer, the algebra has no free real parameter, and the four conjugations and the norm form are canonical. The framework therefore fixes **form** and no **magnitude**: its outputs are pure numbers, and its inputs are dimensionful.

The algebra's quadratic form nevertheless constrains units, and the constraint is the article's first result. The norm form is a sum of four squares, so the four coefficients of a single element must share one unit; the constraint is per element, not across elements, since the norm form of a displacement is a length squared and of a four-momentum a momentum squared. Applied to a displacement this forces the material coordinate to be $ict$ with $c$ a speed: the phase $i$ is the material sector's temporal generator $ie_0$, and the scale $c$ is forced by commensurability. The same constraint propagates to the gradient, whose four coefficients are inverse lengths, so that the mass parameter of an equation built on $\tilde\nabla$ is necessarily an inverse length — as the framework's $\mu=mc/\hbar$ makes explicit.

The constants that physics supplies enter at different points, and the point of entry is what each constant is for. $c$ enters inside the norm form and is the only constant whose *role* the algebra fixes, its value remaining empirical and local in a medium. $\hbar$ enters in the exponent $e^{iS/\hbar}$, making the classical limit a statement about the dimensionless ratio $S/\hbar$ and supplying the unit of the operator algebra, as the spin observable $\tilde{S}_3=\tfrac{\hbar}{2}ie_3$ displays. $k_B$ enters in the thermal strip of width $\beta=\hbar/(k_BT)$, converting a temperature into a time and giving the algebraic imaginary-time direction a size. $G$, $m$ and $e$ enter at points the algebra does not single out: the gravitational term, the mass shell, and the gauge coupling.

The pairing whose integral is the action and the angular momentum share a unit because in the framework they are the scalar and vector parts of one product. For a configuration $\tilde q$ and its conjugate momentum $\tilde p$, the product in the pure-vector case is $\tilde q\tilde p=-\mathbf{q}\cdot\mathbf{p}+\mathbf{q}\times\mathbf{p}$: the scalar part is the contraction of the configuration with the momentum, the vector part the angular momentum, and both are of dimension action. The symplectic potential pairs a momentum with a configuration displacement, $\theta=\mathrm{Sc}(\bar{\tilde p}\,d\tilde q)$, its boundary values give the on-shell action differential $dS=\theta_2-\theta_1$, and the action variable $\oint p\,dq$ is that pairing around a cycle. The two parts are quantised by one phase periodicity — the scalar pairing by the Bohr–Sommerfeld condition $2\pi\hbar(n+\tfrac12)=h(n+\tfrac12)$, in quanta of the action $h$, and the vector part by the spin spectrum in units of $\hbar$ — and the $2\pi$ that separates the two named quanta is the period of the central phase, not a second constant. This is a reading of a known dimensional identity, not a derivation of $\hbar$.

The action family has more than one member: Hamilton's action in time, the abbreviated action along a path, and the action variable around a cycle. All of them have the dimension of action because each pairs a momentum with a displacement, and the corpus already carries Hamilton's characteristic function as the abbreviated action and the action variable as its per-coordinate form. Hamilton's and Maupertuis's principles have reversed constraints — fixed events against fixed energy — and on the stationary path the two actions are related by the Legendre transform in the time–energy pair, $S=S_0-E\,\Delta t$; for a rigid body with no net force they coincide, and both reduce to Fermat's principle of least time. In neither form is the stationary value a maximum, so "least action" is a misnomer.

The SI reaches the same division from the other side. Since its 2019 revision the dimensionful constants $h$, $c$, $e$ and $k_B$ are *defined* rather than measured, while the dimensionless $\alpha$ has to be measured and its value is a fact. That is the metrological image of the dichotomy: dimensionful constants are unit conversions, dimensionless ones are measurements.

The framework's guideline follows from the dichotomy: a dimensionful constant is unreachable by the algebra, and a dimensionless one is not excluded. If the framework is to produce a constant, it must be a ratio.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra; no free parameter, integer structure constants |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Material (imaginary scalar, real vector) and informational (real scalar, imaginary vector) sectors |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}$ | Real-quaternion subspace; center |
| $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}=\sum_\mu Q_\mu^2$ | Norm form; a sum of four commensurable squares |
| $\tilde{X}=ict\,e_0+\mathbf{x}$ | Material coordinate; the temporal coefficient is a length |
| $\tilde{\nabla}=e_0\partial_{ict}+\nabla$ | Biquaternionic gradient; coefficients of inverse length |
| $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta=\Delta-c^{-2}\partial_t^2$ | d'Alembertian |
| $\mu=mc/\hbar$ | Inverse Compton length; the mass parameter as an inverse length |
| $\tilde{q}$, $\tilde{p}$ | Configuration quaternion and conjugate momentum, both real quaternions |
| $\tilde{q}\tilde{p}=(q_0p_0-\mathbf{q}\cdot\mathbf{p})+(q_0\mathbf{p}+p_0\mathbf{q}+\mathbf{q}\times\mathbf{p})$ | The product carrying the contraction and the angular momentum |
| $\tilde{q}\tilde{p}=-\mathbf{q}\cdot\mathbf{p}+\mathbf{q}\times\mathbf{p}$ | Pure-vector case: scalar part the contraction, vector part $\mathbf{L}=\mathbf{q}\times\mathbf{p}$ |
| $\mathrm{Sc}(\bar{\tilde q}\tilde p)=\sum_\mu q_\mu p_\mu$ | Scalar pairing (the conjugate convention; $\mathrm{Sc}(\bar{\tilde p}\,d\tilde q)$ is its differential) |
| $\theta=\mathrm{Sc}(\bar{\tilde{p}}\,d\tilde{q})$, $dS=\theta_2-\theta_1$ | Symplectic potential and the action differential |
| $I_k=\oint p_k\,dq_k$ | Action variable; the abbreviated action of one coordinate around its cycle |
| $S_0=\int\mathbf p\cdot d\mathbf q$, $S=S_0-E\,\Delta t$ | Abbreviated action (Maupertuis), stationary at fixed energy; the two actions differ by a Legendre transform in the time–energy pair |
| $\mathcal{W}$ | Hamilton's characteristic function, $H(\tilde q,\partial_{\tilde q}\mathcal{W})=E$; the abbreviated action as endpoint function |
| $\tilde{S}_3=\tfrac{\hbar}{2}ie_3$ | Spin observable; algebra supplies $ie_3$ and $\tfrac12$, not $\hbar$ |
| $S/\hbar$ | Dimensionless phase; the classical-limit parameter |
| $\beta=\hbar/(k_BT)$ | Thermal strip width; thermal circle circumference $\hbar c/(k_BT)$ |
| $\mathrm{Tr}(e_0)=2$, $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace normalization and trace formula; the factor $2$ is a pure number |
| $c=1/\sqrt{\epsilon\mu}$, $c_0=1/\sqrt{\epsilon_0\mu_0}$ | Medium and vacuum speeds of light; $c$ is a defining constant of the SI |
| $\hbar=h/2\pi$ | Reduced Planck constant; the unit that makes the phase $S/\hbar$ dimensionless |
| $h=2\pi\hbar$ | Planck constant; the quantum of action, where $\hbar$ is the quantum of angular momentum |
| $m$, $e$, $\alpha=e^2/(4\pi\epsilon_0\hbar c)$ | Imported mass, charge and dimensionless coupling; $e$ is a defining constant of the SI, $m$ and $\alpha$ are measured |
| $k_B$, $G$ | Imported: energy–temperature, and stress–energy–curvature; $k_B$ is a defining constant of the SI, $G$ is measured |

## Further Reading

- Max Planck, "Zur Theorie des Gesetzes der Energieverteilung im Normalspectrum," *Verhandlungen der Deutschen Physikalischen Gesellschaft* **2** (1900) 237, for the introduction of the quantum of action.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the action as a phase and the classical limit as a stationary-phase statement.
- Lev Landau and Evgeny Lifshitz, *Mechanics* (Pergamon, 1976), for Maupertuis's principle and the abbreviated action, the action variable, the adiabatic invariant, and the quantisation of the action.
- Herbert Goldstein, Charles Poole and John Safko, *Classical Mechanics*, 3rd ed. (Addison Wesley, 2002), for the abbreviated action, Hamilton's characteristic function, and action-angle coordinates.
- Bureau International des Poids et Mesures, *The International System of Units (SI)*, 9th ed. (BIPM, 2019), for the defining constants and the derivation of the kilogram from $h$.
- Lev Landau and Evgeny Lifshitz, *Statistical Physics, Part 1* (Pergamon, 1980), for the thermal weight, the imaginary-time formalism, and the role of $k_B$.
- Percy W. Bridgman, *Dimensional Analysis* (Yale, 1922), for the classical account of the dimensional structure of physical laws and of dimensionless constants.
- Rudolf Haag, *Local Quantum Physics* (Springer, 1996), for the KMS condition and the characterisation of thermal states by the modular structure.
- Roger Penrose, *The Road to Reality* (Knopf, 2004), for the relation between angular momentum, the spinor representation, and the double cover of the rotation group.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the natural-units convention of quantum field theory and what it suppresses.
- N. P. Landsman, *Mathematical Topics Between Classical and Quantum Mechanics* (Springer, 1998), for the classical limit as a deformation and the sense in which $\hbar\to0$ is a formal contraction rather than a physical process.
