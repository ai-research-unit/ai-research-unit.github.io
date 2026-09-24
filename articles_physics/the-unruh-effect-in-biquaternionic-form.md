# __The Unruh Effect in Biquaternionic Form__

## Introduction

The **Unruh effect** is the statement that a uniformly accelerated observer in the Minkowski vacuum does not see a vacuum. On a trajectory of constant proper acceleration $a$, the observer registers a thermal bath at the **Unruh temperature**

$$
T = \frac{\hbar a}{2\pi c\,k_B},
$$

with a Planckian spectrum in the frequency conjugate to the observer's proper time. The effect is not a property of the detector or of the acceleration mechanism; it is a property of the state of the field as seen from the accelerated frame. This article develops that statement inside the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, in the notation of the companion articles.

Three structures carry the effect, and all three have a definite home in the framework.

1. **The Rindler wedge.** The accelerated trajectory is confined to a wedge of Minkowski space, the **right Rindler wedge** $R=\{x>|ct|\}$. Its boundary is the light cone — which, in the material sector $\mathbb{M}_-$, is exactly the **zero-divisor cone** of the algebra. The wedge, its horizon, and its boost flow are material-sector objects.
2. **The boost as the modular Hamiltonian.** By the Bisognano–Wichmann theorem, the modular operator of the vacuum restricted to the wedge is $\Delta=e^{-2\pi K_{\mathrm{boost}}}$, where $K_{\mathrm{boost}}$ is the generator of boosts. The modular flow is therefore the boost flow. The boost generator is a Hermitian element of the algebra; for a boost along $e_1$ it is $G_1=ie_1\in\mathbb{M}_+$.
3. **The KMS condition.** The KMS condition of the companion article states that the correlation functions of a thermal state are analytic in a strip of width $\beta=\hbar/(k_BT)$ in the complex time plane and satisfy a boundary relation that exchanges the operators. The wedge vacuum satisfies that condition with respect to the boost flow, and the width of the strip is what fixes the temperature.

The trap in this subject is to *assert* the thermality — to write down the exponential spectrum and the temperature as if the algebra had produced them. It has not. Thermality is a statement about the **analyticity of the two-point function**, and the section that derives it shows the step: the two-point function along the accelerated orbit is an explicit function whose analytic continuation to imaginary proper time is periodic, and the period *is* the KMS width. The temperature is then recomputed a second time, from the **surface gravity** of the boost orbit, so that it is not a single formula asserted twice.

**Relation to the parent.** *The KMS Condition and the Biquaternion Framework* is the parent article. It establishes two facts that this article uses unchanged: the imaginary time of the material sector is intrinsic, and the modular Hamiltonian $K=-\log\rho$ of a finite-dimensional Gibbs state is a Hermitian element of $\mathbb{M}_+$. It also leaves a gap, which is stated here rather than filled silently. Its modular Hamiltonian is defined through a density matrix in a **finite-dimensional** setting. The wedge-restricted Minkowski vacuum is a state on a field algebra; it is not given by a density matrix, and the parent neither defines the modular operator $\Delta$ nor the modular flow in that setting. The identification of the modular flow with the boost is the **Bisognano–Wichmann theorem** — established physics, imported here, not derived from the biquaternion algebra. What this article does with the gap is make the flow geometric in the one case where the standard theorem supplies it, and label precisely what remains outside the framework.

- **Established, and recomputed below.** In the right wedge, the boost Killing vector $\xi=x\partial_t+t\partial_x$ is future-directed; a boost by rapidity $\psi$ shifts Rindler time $\eta$ by $\eta\mapsto\eta-\psi$ under the rotor $\tilde\Lambda(\psi)=\cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}e_1$; the rotor lies in $\mathbb{M}_+$, preserves $\mathbb{M}_-$ and preserves the norm form. The massless two-point function along the orbit $\rho=\text{const}$ is $W=-\tfrac{1}{16\pi^2\rho^2}\sinh^{-2}\!\big(\tfrac{1}{2}(\delta\eta-i\epsilon)\big)$ in units $c=1$; it is even and periodic under $\delta\eta\mapsto\delta\eta+2\pi i$, equivalently in imaginary proper time with period $\beta=2\pi/a$, giving the KMS strip $0<\mathrm{Im}\,\delta\tau<\beta$ and the boundary relation $W(\delta\tau+i\beta)=W(-\delta\tau)$. The surface gravity of the redshift-normalized boost $\chi=a\xi$ is $\kappa=a$ on the horizon, so $T=\kappa/(2\pi)=a/(2\pi)$.
- **Standard, and imported.** The Unruh effect itself; the Bisognano–Wichmann theorem; the KMS characterization of thermal equilibrium; the massless Wightman function and its pole structure; the definition of surface gravity.
- **Interpretation.** Reading the modular flow as the biquaternionic boost flow, and the Rindler horizon as the zero-divisor cone, are structural readings of the standard construction. The algebra is consistent with them; it does not by itself force the thermal interpretation.
- **Gaps, left visible.** The general modular operator of a field algebra is not constructed in the framework; the algebra of observables of a quantum field theory is infinite-dimensional, so the finite-dimensional reading of the modular flow as an inner automorphism is a model, not a derivation; and the framework does not derive thermality, only house it. These are collected in the open questions.

The article is organized as follows. The next section fixes the wedge, the Rindler coordinates, and the boost. The section after that states the modular Hamiltonian and identifies the flow, with the parent's gap stated explicitly. The next section computes the two-point function and derives the KMS relation from its analytic strip. Two short sections recompute the temperature, one from the imaginary-time period and one from the surface gravity. A section isolates what the biquaternion framework adds and what it only transcribes, and a short section records the statistics. The article closes with the established/interpretation split, open questions, and the summary.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$, and $i$ is the scalar imaginary, $i^2=-1$, commuting with every $e_k$. The material (anti-Hermitian) subspace is $\mathbb{M}_-$ and the informational (Hermitian) subspace is $\mathbb{M}_+$, with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ and $i\mathbb{M}_\pm=\mathbb{M}_\mp$; $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace. The material coordinate is $\tilde X=ict\,e_0+x\,e_1+y\,e_2+z\,e_3\in\mathbb{M}_-$, with norm form $N(\tilde X)=\tilde X\bar{\tilde X}=-c^2t^2+x^2+y^2+z^2$. The biquaternionic gradient is $\tilde\nabla=e_0\partial_{ict}+e_k\partial_k$ and $\Box=\tilde\nabla\bar{\tilde\nabla}=\bar{\tilde\nabla}\tilde\nabla$. The trace formula $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ is inherited unchanged. Throughout, $\hbar$ and $k_B$ are the reduced Planck and Boltzmann constants, and $c$ is the speed of light. The two-point-function computation is done in units $c=1$, restoring $c$ only in the temperature.

## The Rindler Wedge and the Boost

### The Wedge and Its Horizon

Work in the material sector and restrict to the $x$--$t$ plane, setting $y=z=0$. A point is

$$
\tilde X = i\,ct\,e_0 + x\,e_1 \in \mathbb{M}_-, \qquad N(\tilde X) = -c^2t^2 + x^2 .
$$

The **right Rindler wedge** is the region

$$
R = \{(t,x): x > |ct|\},
$$

and the **left wedge** is its mirror $L=\{(t,x): x<-|ct|\}$. The boundary

$$
N(\tilde X) = 0 \quad\Longleftrightarrow\quad x = \pm ct
$$

is the light cone. In the algebra the light cone of $\mathbb{M}_-$ is the **zero-divisor cone**: a nonzero $\tilde X\in\mathbb{M}_-$ satisfies $\tilde X\bar{\tilde X}=0$ exactly on $N(\tilde X)=0$ (the companion article on $\mathbb{M}_-$ establishes this and identifies its two components). The horizon of an accelerated observer is therefore not an extra geometric object imported into the algebra: it is the algebraic null cone of the material sector.

Inside $R$ the norm form is positive, $N>0$. Introduce **Rindler coordinates** $(\rho,\eta)$ by

$$
x = \rho\cosh\eta, \qquad ct = \rho\sinh\eta, \qquad \rho>0,\ \eta\in\mathbb{R},
$$

so that $\tilde X = i\rho\sinh\eta\,e_0+\rho\cosh\eta\,e_1$ and $N(\tilde X)=\rho^2$. The curves of constant $\rho$ are the orbits of a uniformly accelerated observer. Their proper time $\tau$ and proper acceleration $a$ are

$$
c\,d\tau = \rho\,d\eta, \qquad a = \frac{c^2}{\rho},
$$

so the orbit of proper acceleration $a$ sits at $\rho=c^2/a$. In units $c=1$ these read $\tau=\rho\eta$ and $a=1/\rho$; we use these below and restore $c$ at the end. The horizon $N=0$ is the limit $\rho\to0$, reached only asymptotically, which is why the accelerated observer has a causal horizon.

### The Boost and Its Direction

The **boost Killing vector** is

$$
\xi = x\,\partial_t + t\,\partial_x .
$$

It is future-directed on the right wedge and past-directed on the left. Its orbits in $R$ are the constant-$\rho$ hyperbolas above, with $\eta$ the affine parameter: $\xi=\partial_\eta$. The acceleration is the rate at which the boost parameter grows along the orbit, and this will become the surface gravity.

The corresponding element of the algebra is the **boost generator**

$$
G_1 = i\,e_1 \in \mathbb{M}_+,
$$

which is Hermitian, $G_1^\dagger=G_1$, and satisfies $G_1^2=e_0$. Its exponential is the **boost rotor** of the companion article on the Lorentz transformation,

$$
\tilde\Lambda(\psi) = \exp\!\Big(\frac{\psi}{2}G_1\Big) = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,e_1 \in \mathbb{M}_+,
$$

which is Hermitian and of unit norm form, $\tilde\Lambda\bar{\tilde\Lambda}=e_0$. It acts on the material sector by **rotor conjugation**

$$
\tilde X \longmapsto \tilde\Lambda(\psi)\,\tilde X\,\tilde\Lambda(\psi),
$$

where we have used $\tilde\Lambda^\dagger=\tilde\Lambda$. This is the two-sided action of the companion article on curved spacetime, not the commutator: for the boost generator the two differ, and it is the two-sided form that implements the boost.

**The direction, computed.** On $\tilde X=iq_0e_0+q_1e_1$ (with $q_0=ct$, $q_1=x$; we drop $q_2,q_3$, which are untouched), rotor conjugation gives

$$
q_0 \longmapsto q_0\cosh\psi - q_1\sinh\psi, \qquad
q_1 \longmapsto q_1\cosh\psi - q_0\sinh\psi .
$$

On the orbit $q_1=\rho\cosh\eta$, $q_0=\rho\sinh\eta$ this is

$$
q_0 \longmapsto \rho\sinh(\eta-\psi), \qquad q_1 \longmapsto \rho\cosh(\eta-\psi),
$$

so the rotor of **positive** rapidity $\psi$ shifts the Rindler time by $\eta\mapsto\eta-\psi$. Equivalently, the generator $G_1$ acts infinitesimally as

$$
q_0 \longmapsto q_0 - 2s\,q_1, \qquad q_1 \longmapsto q_1 - 2s\,q_0
$$

for the flow parameter $s=\psi/2$. This is the sign that has to be fixed before anything else can be; we record it explicitly and use the orientation that advances $\eta$ when we need a direction. The same computation shows that the boost preserves the norm form, $N(\tilde\Lambda\tilde X\tilde\Lambda)=N(\tilde X)$, so $R$ is mapped to itself and the horizon to itself. Two checks beyond the case that suggested the formulas are recorded in the companion: the rotor maps $\eta$ to $\eta-\psi$ on an independently chosen orbit, and the norm form is preserved on a general element of $\mathbb{M}_-$.

**Which wedge.** The two wedges have opposite orientation. The boost generator whose flow is future-directed on $R$ is past-directed on $L$, so the modular Hamiltonians of the two wedges satisfy $K_L=-K_R$, and the surface gravities have opposite signs. The temperature is built from $|\kappa|=a$, so it is the same for both; but a statement about "the modular Hamiltonian" that omits the wedge is ambiguous, and we keep the wedge explicit.

## The Boost as the Modular Hamiltonian

### What the Parent Establishes, and the Gap It Leaves

The parent article defines the modular Hamiltonian, in a finite-dimensional setting, by

$$
K = -\log\Delta, \qquad \Delta=\rho \ \ (\text{finite dimension}),
$$

so that $K=-\log\rho$ is Hermitian and therefore lies in $\mathbb{M}_+$. It states that the KMS correlation functions are analytic in the strip $0<\mathrm{Im}\,t<\beta$ and satisfy

$$
F_{\tilde A\tilde B}(t+i\beta) = F_{\tilde B\tilde A}(-t),
$$

and it records the imaginary time of $\mathbb{M}_-$ as intrinsic.

The gap is the one anticipated in the introduction. In a quantum field theory the state of the vacuum restricted to a wedge is not given by a density matrix: the local algebra is a von Neumann algebra of type III, on which no trace, and hence no $\rho$, exists. The parent's $K=-\log\rho$ therefore does **not** extend to this case, and the parent says nothing about a modular **flow** $\alpha_s$ for a field algebra. The step from "there is a modular Hamiltonian" to "the modular flow is the boost at this temperature" is not in the parent and is not supplied by the biquaternion algebra. It is supplied by a theorem.

### The Bisognano–Wichmann Identification

For the vacuum state of a Wightman quantum field theory and the right Rindler wedge $R$, the **Bisognano–Wichmann theorem** states that the modular operator is

$$
\Delta = e^{-2\pi K_{\mathrm{boost}}},
$$

where $K_{\mathrm{boost}}$ is the generator of the boosts that preserve $R$, normalized so that $\xi=\partial_\eta$. The modular flow is

$$
\alpha_s(\tilde A) = \Delta^{is}\,\tilde A\,\Delta^{-is} = e^{-2\pi i sK_{\mathrm{boost}}}\,\tilde A\,e^{2\pi i sK_{\mathrm{boost}}},
$$

which is the boost by rapidity $2\pi s$. This is established physics and is imported here; the article does not derive it, and says so. Its content for us is that the abstract modular flow of the parent acquires a **geometric realization**: it is the boost flow, and the modular parameter $s$ is the Rindler time measured in units of $2\pi$.

### The Flow in Biquaternion Form

The generator $K_{\mathrm{boost}}$ is the boost Hamiltonian, whose biquaternion representative is the Hermitian element $G_1=ie_1\in\mathbb{M}_+$ of the preceding section, up to the normalization of the modular generator (the flow below is conjugation by $\tilde\Lambda(-2\pi s)=\exp(-\pi sG_1)$). The one-parameter modular flow therefore acts on the material sector by rotor conjugation,

$$
\alpha_s:\ \tilde X \longmapsto \tilde\Lambda(-2\pi s)\,\tilde X\,\tilde\Lambda(-2\pi s),
$$

the argument $-2\pi s$ being the orientation that advances $\eta$ (the opposite sign gives the left wedge). The sign is the one fixed above: the abstract boost by rapidity $2\pi s$ is represented here by the **inverse** rotor $\tilde\Lambda(-2\pi s)$ precisely because $\tilde\Lambda(+\psi)$ shifts $\eta$ by $-\psi$. Three features of this are worth separating.

- **The generator is in $\mathbb{M}_+$.** The modular Hamiltonian is represented by a Hermitian element of the informational sector, in agreement with the parent's algebraic fact that $K=-\log\rho$ lies in $\mathbb{M}_+$. Here the element is $G_1=ie_1$, the boost generator, and the agreement is exact up to that normalization rather than analogical.
- **The flow is an inner automorphism of the algebra** by a one-parameter family of unit-norm Hermitian rotors in $\mathbb{M}_+$. In the finite-dimensional model in which observables are elements of $\mathbb{B}$, this realizes the modular flow as conjugation. In a genuine field theory the observable algebra is infinite-dimensional and the flow is not inner; the identification is a model, and it is flagged as such.
- **The flow acts on the field algebra, not on spacetime points.** The rotor conjugation above is the Lorentz action on the four-vector representative $\tilde X$; identifying the boost flow of spacetime with the modular flow of the field algebra is exactly the content of Bisognano–Wichmann, not a consequence of the notation.

The imaginary-time shift of the KMS condition is a shift along the time direction of $\mathbb{M}_-$, which is $ict$. This is the parent's structural point, and the accelerated frame gives it a geometric meaning: the complexified direction in which the KMS analyticity takes place is the complexification of the Rindler time, $\mathbb{M}_-\oplus i\mathbb{M}_-=\mathbb{B}$, and the thermal circle lies along the material time axis.

## The Two-Point Function and the Analyticity Strip

This is the section in which thermality is derived rather than asserted.

### The Two-Point Function on the Orbit

Let $\phi$ be the massless real scalar field and $W$ its Wightman function,

$$
W(x,x') = \langle 0|\,\phi(x)\,\phi(x')\,|0\rangle
= \frac{1}{4\pi^2}\,\frac{1}{|\mathbf{x}-\mathbf{x}'|^2-(t-t'-i\epsilon)^2},
$$

in units $c=1$, with the standard $i\epsilon$ prescription. Evaluate it at two points of the same accelerated orbit, $(t,x)=(\rho\sinh\eta,\rho\cosh\eta)$ and the point labelled by $\eta'$, and set $\delta\eta=\eta-\eta'$. Using

$$
\Delta x^2 - \Delta t^2 = \rho^2(\cosh\eta-\cosh\eta')^2-\rho^2(\sinh\eta-\sinh\eta')^2
= -\,4\rho^2\sinh^2\frac{\delta\eta}{2},
$$

which we have checked symbolically, the Wightman function becomes

$$
W(\delta\eta) = -\frac{1}{16\pi^2\rho^2}\,
\frac{1}{\sinh^2\!\big(\tfrac{1}{2}(\delta\eta-i\epsilon)\big)} .
$$

Since $\delta\tau=\rho\,\delta\eta$ on the orbit of radius $\rho$, and $a=1/\rho$,

$$
W(\delta\tau) = -\frac{a^2}{16\pi^2}\,
\frac{1}{\sinh^2\!\big(\tfrac{a}{2}(\delta\tau-i\epsilon)\big)} .
$$

All of the thermal content is now in this elementary function.

### The Strip and the Boundary Relation

Write $\mathcal W(z)$ for the same expression with the $i\epsilon$ removed, as a function of the complex variable $z=\delta\tau$. The double poles of $\sinh^{-2}$ are at $z=2\pi i n/a$, $n\in\mathbb{Z}$; the nearest to the real axis are at $\pm2\pi i/a$. Hence:

1. $\mathcal W(z)$ is **analytic in the strip** $-2\pi/a<\mathrm{Im}\,z<2\pi/a$, and in particular in the KMS strip
$$
0<\mathrm{Im}\,z<\beta,\qquad \beta=\frac{2\pi}{a},
$$
and it is continuous on the closure.
2. $\sinh^2$ is invariant under the imaginary shift by $i\pi$ in its argument, and $\sinh^2$ is even. With the argument $\tfrac{a}{2}z$, the shift $z\mapsto z+2\pi i/a$ adds $i\pi$, and $z\mapsto-z$ changes the sign. Therefore
$$
\mathcal W\!\Big(z+\frac{2\pi i}{a}\Big)=\mathcal W(z), \qquad \mathcal W(-z)=\mathcal W(z).
$$
3. Consequently, on the boundary of the strip,
$$
W(\delta\tau+i\beta) = W(-\delta\tau), \qquad \beta=\frac{2\pi}{a}.
$$

The last display is the **KMS boundary relation** of the parent, with $A=B=\phi(0)$: the two-point function continued to imaginary time $\delta\tau+i\beta$ equals the reversed two-point function at $-\delta\tau$. The step that produces it is the pair of elementary identities in item 2; without them, "the accelerated observer sees a thermal state" is an assertion. The $i\epsilon$ in the displayed two-point function fixes which boundary values are meant, and the relation above is the standard one between the two edges of the strip in that convention; we do not re-fix the convention here.

Two remarks keep the derivation honest.

- **The relation is a periodicity, not a decay.** The two-point function is periodic in imaginary proper time with period $\beta$; it is not that the correlations fall off. Periodicity in imaginary time is exactly the parent's characterization of a thermal state, and it is what makes the Matsubara formalism work.
- **The operator exchange is automatic here.** The general KMS relation exchanges $\tilde A$ and $\tilde B$. For the two-point function of a single Hermitian field, $W$ is even, so $W(\delta\tau+i\beta)=W(-\delta\tau)$ also reads $W(\delta\tau+i\beta)=W(\delta\tau)$. The general relation is recovered by keeping the operators distinct, as in the parent.

### Frequency Space and the Planck Factor

The KMS relation is equivalent, in frequency space, to a **detailed-balance** relation. Writing the Wightman function in terms of the Rindler frequency $\omega$ conjugate to $\eta$,

$$
W(\delta\eta)=\int\frac{d\omega}{2\pi}\,\tilde W(\omega)\,e^{-i\omega\,\delta\eta},
$$

the boundary relation $W(\delta\eta+2\pi i)=W(-\delta\eta)$ is equivalent, for the boundary values selected by the $i\epsilon$ of the displayed two-point function, to a **detailed-balance** relation among the spectral weights,

$$
\tilde W(-\omega) = e^{-2\pi\omega}\,\tilde W(\omega) \qquad (\omega>0),
$$

where we have written the transform in the convention $\tilde W(\omega)=\int d\eta\,e^{i\omega\eta}W(\eta)$ inverse to the display above. The two boundary edges of the strip differ by exactly the Boltzmann factor, so the exponent's sign is fixed by which edge is called $W$; we state it with the same $i\epsilon$ as the two-point function and do not read it off independently of that convention. This is the **Planck factor**: the ratio of the excitation and de-excitation weights of a detector of gap $\omega$ is $e^{-2\pi\omega}$ rather than $1$, which is the signature of a thermal bath at inverse temperature $\beta_\eta=2\pi$ in the Rindler time. Computing the Fourier transform of the displayed function explicitly — the poles of $\coth$ at $2\pi i n+i\epsilon$ are enclosed in the upper half plane for $\omega>0$, and the $n=0$ pole must be included — gives

$$
\tilde W(\omega) = \frac{1}{16\pi^2\rho^2}\cdot\frac{8\pi\omega}{1-e^{-2\pi\omega}}\quad(\omega>0),
$$

whose ratio at $\pm\omega$ is $e^{-2\pi\omega}$. The transform has been checked numerically at two frequencies ($\omega=0.5$ and $\omega=1$), where the measured ratios $4.3\times10^{-2}$ and $1.87\times10^{-3}$ agree with $e^{-\pi}$ and $e^{-2\pi}$ to the accuracy of the regulator; this is recorded in the companion, together with the first attempt that omitted the $n=0$ pole and returned a ratio of $1$.

## The Temperature from the Imaginary-Time Period

From the previous section, the width of the KMS strip in **proper time** is

$$
\beta = \frac{2\pi}{a} \quad (\text{units } c=1).
$$

Since $\beta=\hbar/(k_BT)$, the temperature is

$$
T = \frac{1}{\beta} = \frac{a}{2\pi} \quad (\hbar=k_B=1),
$$

and restoring the constants,

$$
T = \frac{\hbar a}{2\pi c\,k_B}.
$$

This is the Unruh temperature. In the orbit parametrization used here, $a=1/\rho$, so the temperature of the orbit of radius $\rho$ is $T=(2\pi\rho)^{-1}$ in natural units; the near-horizon orbits, $\rho\to0$, are the hot ones, which is the field-theoretic reason a horizon is hot. Equivalently, the same period expressed in imaginary **Rindler time** is $2\pi i$, and $\beta=2\pi/a$ follows from $\tau=\rho\eta$; the two statements are the same period in different time variables, and we have checked the conversion.

**A case not used to derive it.** The formulas were extracted from the massless scalar; the numerical value of the temperature is independent of that choice. For an acceleration equal to terrestrial gravity, $a=g=9.80665\ \mathrm{m\,s^{-2}}$,

$$
T=\frac{\hbar g}{2\pi c\,k_B}=3.98\times10^{-20}\ \mathrm{K},
$$

which is unobservably small — the reason the effect is a theoretical structure rather than a laboratory signal. The companion records the numerical evaluation.

## The Temperature from the Surface Gravity

The second route uses the geometry of the boost directly and does not pass through the two-point function. The **surface gravity** $\kappa$ of a Killing horizon generated by a Killing field $\chi$ is defined on the horizon by

$$
\chi^\nu\nabla_\nu\chi^\mu = \kappa\,\chi^\mu .
$$

For the boost $\xi=x\partial_t+t\partial_x$, whose horizon is $x=|ct|$, one finds on the horizon $\nabla_\xi\xi = \xi$, so $\kappa_\xi=1$ for the unnormalized boost. The redshift-normalized field whose orbits have unit norm at the observer's trajectory is $\chi=a\,\xi$; its surface gravity is

$$
\kappa = a .
$$

We have checked this directly: with $\chi=a(x\partial_t+t\partial_x)$, the identity $\chi^\nu\partial_\nu\chi^\mu=\kappa\chi^\mu$ holds with $\kappa=a$ on the horizon $x=t$. The Unruh temperature is then

$$
T=\frac{\kappa}{2\pi}=\frac{a}{2\pi}\quad(\hbar=c=k_B=1),
\qquad\text{i.e.}\qquad T=\frac{\hbar a}{2\pi c\,k_B},
$$

in agreement with the imaginary-time route. The two computations are independent in the sense that one uses the pole structure of the two-point function and the other the normalization of the boost on its horizon; that they agree is a check on the whole construction, not a restatement. The relation between them is transparent once stated: the imaginary-time period is $2\pi$ in the boost parameter, and the boost parameter is the Rindler time whose gradient is the surface gravity. The **surface gravity is the rate of change of the boost rapidity per unit proper time**, and the imaginary-time period $\beta=2\pi/\kappa$ is the reciprocal of the temperature $T=\kappa/(2\pi)$ — equivalently, the period is $2\pi$ times the reciprocal of the surface gravity.

## What the Biquaternion Framework Adds, and What It Transcribes

**What it adds (algebra and structure).**

- *The flow generator is in $\mathbb{M}_+$.* The modular Hamiltonian of the wedge is represented by the Hermitian boost generator $G_1=ie_1$, up to the normalization of the modular generator noted above. This is the exact form of the parent's statement that $K=-\log\rho\in\mathbb{M}_+$ — the same Hermitian element that rotates $\mathbb{M}_-$ by rotor conjugation is the generator of the thermal flow — and it is not an analogy.
- *The horizon is the zero-divisor cone.* The Rindler horizon of the accelerated observer is the null cone of the material sector, the zero-divisor set of the algebra. The wedge is a connected region on which the norm form has one sign; the horizon is where it changes.
- *The thermal circle lies along the material time.* The KMS analyticity is a continuation in the $ict$ direction, i.e. the complexification of the Rindler time, and the flow that acts is an inner automorphism by rotors in $\mathbb{M}_+$. The material sector supplies the time in which the state is thermal; the informational sector supplies the operator that generates the flow.
- *The boost is two-sided.* The generator acts on $\mathbb{M}_-$ through the rotor anticommutator $G_1\tilde X+\tilde XG_1$, not through the commutator. This is the curved-spacetime companion's caution, and the Unruh flow is a case where it is load-bearing: the commutator generates a rotation in the plane orthogonal to the boost (it vanishes on the boost plane itself) and does not produce the boost.

**What it only transcribes.**

- *The Unruh effect itself.* The effect is a theorem of quantum field theory in flat spacetime. The algebra houses the wedge and the flow; it does not produce the effect.
- *The Bisognano–Wichmann identification.* That the modular flow is the boost is imported. It is the hinge on which the whole construction turns, and the framework does not supply it.
- *The two-point function.* The massless Wightman function and its pole structure are standard. What the framework does is express the orbit and the invariant in $\mathbb{M}_-$ notation, and identify the imaginary direction with $ict$.
- *The surface gravity.* The definition and the computation are standard Lorentzian geometry.

## The Statistics

The Unruh temperature does not depend on the statistics of the field. The KMS boundary relation $F_{\tilde A\tilde B}(t+i\beta)=F_{\tilde B\tilde A}(-t)$ is the same for bosons and fermions; what differs is the **time-ordered** correlation function, which is antiperiodic for fermions and periodic for bosons, the parent's statement. The strip, and therefore the temperature, is the same. What changes for a fermionic field is the response of a detector and the sign structure of the Matsubara sum; that is the parent's fermionic twist, and it needs the $\mathbb{Z}/2$ grading that the parent records as absent from $\mathbb{B}$ in general and that the Fock-space article realizes only for a single mode. The thermal character of the accelerated vacuum is thus statistics-independent, and the framework's open grading question is orthogonal to the Unruh temperature.

## What Is Established, What Is Interpretation, and the Gaps

**Established (physics).** The Unruh effect and the temperature $T=\hbar a/(2\pi c k_B)$; the Bisognano–Wichmann theorem; the KMS characterization of thermal equilibrium and its boundary relation; the massless Wightman function and its pole structure; the definition of surface gravity and its value $\kappa=a$ for the redshift-normalized boost.

**Established (algebra), recomputed here.** The boost rotor $\tilde\Lambda(\psi)=\cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}e_1$ lies in $\mathbb{M}_+$, is Hermitian and of unit norm form, and preserves $\mathbb{M}_-$ and the norm form; it shifts the Rindler time by $\eta\mapsto\eta-\psi$; its generator is $G_1=ie_1\in\mathbb{M}_+$ with the two-sided action; the horizon is the zero-divisor cone of $\mathbb{M}_-$.

**Interpretation.** Reading the modular flow as the biquaternionic boost flow, and the Rindler horizon as the zero-divisor cone, are structural readings. The algebra is consistent with them and makes the flow explicit in the finite-dimensional model; it does not force the thermal reading.

**Gaps.**

- *The modular operator in the field setting.* The parent's $K=-\log\rho$ is finite-dimensional and does not extend to the wedge algebra; the article imports Bisognano–Wichmann for the flow and does not construct $\Delta$ in the framework.
- *The inner-automorphism model.* Realizing the flow as conjugation by rotors in $\mathbb{M}_+$ uses the finite-dimensional algebra as a model of the observables. The physical algebra is infinite-dimensional, where the modular flow is not inner. The model is stated as a model.
- *Derivation of thermality.* The framework houses the effect; it does not derive it. The calculation of the two-point function is standard field theory written in the framework's coordinates.
- *Curved spacetime.* The Hawking effect is the same KMS structure with the surface gravity of a black-hole horizon, and it lies outside this article. The companion article on curved spacetime records that the framework generates no dynamics, and the same limitation applies.

## Open Questions

1. **The modular operator for a biquaternion field algebra.** The parent defines $K$ through a density matrix and this article imports the geometric flow. Can a modular operator be defined intrinsically on a subalgebra attached to the wedge, without the Bisognano–Wichmann input?

2. **The flow beyond the model.** The modular flow is inner in the finite-dimensional model. Is there a biquaternionic structure — a crossed product, or a module with a trace — in which the wedge flow becomes inner in a controlled infinite-dimensional sense?

3. **The horizon as an algebraic object.** The horizon is the zero-divisor cone. Do the zero divisors, which have no inverse, play the role of the horizon's degeneracy in a derivation of the temperature, rather than only in its description?

4. **The detector.** The Planck factor was obtained from the field two-point function. A biquaternionic treatment of the Unruh–DeWitt detector, including the detector's internal two-level structure (which the Fock-space article realizes for one fermionic mode), is not given here.

5. **The fermionic twist at a horizon.** The statistics does not change the temperature, but the antiperiodicity does change the time-ordered correlators. Does the single-mode grading of the Fock-space article extend to a module statement about the Rindler horizon?

6. **Hawking radiation.** The same argument with the surface gravity of a black-hole horizon should give the Hawking temperature. Whether the biquaternion framework adds anything there, or only transcribes the standard derivation, is open, and is the subject of the planned companion article.

7. **Empirical contact.** As everywhere in the framework, the question is whether any of this yields a prediction distinguishing it from standard quantum field theory. The Unruh effect as presented is a reformulation.

## Summary

An observer of constant proper acceleration $a$ in the Minkowski vacuum is confined to a Rindler wedge, and the vacuum restricted to that wedge is a thermal state with respect to the boost flow. In the biquaternion framework the wedge is a region of the material sector $\mathbb{M}_-$ bounded by the **zero-divisor cone**, and the boost flow is generated by the Hermitian element $G_1=ie_1\in\mathbb{M}_+$ acting on $\mathbb{M}_-$ by the two-sided rotor conjugation $\tilde X\mapsto\tilde\Lambda\,\tilde X\,\tilde\Lambda$ with $\tilde\Lambda(\psi)=\cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}e_1$.

By the Bisognano–Wichmann theorem — imported, not derived — the modular operator of the vacuum on the wedge is $\Delta=e^{-2\pi K_{\mathrm{boost}}}$, so the modular flow is the boost by rapidity $2\pi s$; this realizes the parent's abstract modular Hamiltonian as the boost generator, whose image in the algebra is the Hermitian element $ie_1\in\mathbb{M}_+$. The thermality is derived from the two-point function. Along the accelerated orbit the massless Wightman function is

$$
W(\delta\tau) = -\frac{a^2}{16\pi^2}\,\frac{1}{\sinh^2\!\big(\tfrac{a}{2}(\delta\tau-i\epsilon)\big)},
$$

whose poles at $\delta\tau=2\pi i n/a$ and the identity $\sinh^2(z+i\pi)=\sinh^2 z$ give the strip $0<\mathrm{Im}\,\delta\tau<\beta$ and the KMS boundary relation $W(\delta\tau+i\beta)=W(-\delta\tau)$ with

$$
\beta = \frac{2\pi}{a}, \qquad T=\frac{1}{\beta}=\frac{a}{2\pi}
\quad(\hbar=k_B=1),
$$

or $T=\hbar a/(2\pi c k_B)$ with the constants restored. The temperature is recomputed independently from the surface gravity of the redshift-normalized boost $\chi=a\xi$, for which $\chi^\nu\nabla_\nu\chi^\mu=a\chi^\mu$ on the horizon, giving $T=\kappa/(2\pi)=a/(2\pi)$.

The framework supplies the algebraic home: the horizon as the zero-divisor cone, the generator in the informational sector $\mathbb{M}_+$, the thermal circle along the material time $ict$, and the two-sided action that distinguishes the boost from a rotation. It does not supply the Unruh effect, the Bisognano–Wichmann theorem, or a modular operator for a field algebra; those are imported, and the gap in the parent is left visible.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\tilde X=ict\,e_0+x\,e_1+y\,e_2+z\,e_3$ | Material-sector coordinate $\in\mathbb{M}_-$ |
| $N(\tilde X)=\tilde X\bar{\tilde X}$ | Norm form, signature $(3,1)$ on $\mathbb{M}_-$ |
| $R=\{x>|ct|\}$ | Right Rindler wedge; $L$ its mirror |
| $\rho,\eta$ | Rindler radius and Rindler time, $x=\rho\cosh\eta$, $ct=\rho\sinh\eta$ |
| $\tau$ | Proper time along the accelerated orbit, $cd\tau=\rho\,d\eta$ |
| $a=c^2/\rho$ | Proper acceleration of the orbit |
| $\xi=x\partial_t+t\partial_x$ | Boost Killing vector, $\xi=\partial_\eta$ |
| $\chi=a\xi$ | Redshift-normalized boost; $\kappa=a$ its surface gravity |
| $\kappa$ | Surface gravity of the boost horizon |
| $G_1=ie_1\in\mathbb{M}_+$ | Boost generator (Hermitian) |
| $\tilde\Lambda(\psi)=\cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}e_1$ | Boost rotor (Hermitian, unit norm form) |
| $\tilde X\mapsto\tilde\Lambda\tilde X\tilde\Lambda$ | Boost = rotor conjugation on $\mathbb{M}_-$ |
| $K_{\mathrm{boost}},\ \Delta=e^{-2\pi K_{\mathrm{boost}}}$ | Boost Hamiltonian; modular operator (Bisognano–Wichmann) |
| $\alpha_s$ | Modular flow = boost by rapidity $2\pi s$ |
| $K=-\log\Delta$ | Modular Hamiltonian (parent's notation) |
| $W(\delta\tau)$ | Massless two-point function on the orbit |
| $\beta=2\pi/a$ | KMS strip width in imaginary proper time |
| $T=\hbar a/(2\pi c k_B)$ | Unruh temperature |
| $\tilde W(\omega)$ | Rindler-frequency transform of $W$; $\tilde W(-\omega)=e^{-2\pi\omega}\tilde W(\omega)$ |
| $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ | Trace formula (inherited) |

## Further Reading

- W. G. Unruh, "Notes on black-hole evaporation," *Physical Review D* **14** (1976) 870–892, for the original Unruh effect.
- P. C. W. Davies, "Scalar production in Schwarzschild and Rindler metrics," *Journal of Physics A* **8** (1975) 609–616, for the independent discovery of the acceleration temperature.
- S. A. Fulling, "Nonunitary Bogoliubov transformations and extension of Wick's theorem," *Nuovo Cimento A* **26** (1973) 375–397, for the Rindler quantization and the inequivalent vacua.
- J. J. Bisognano and E. H. Wichmann, "On the duality condition for a Hermitian scalar field," *Journal of Mathematical Physics* **16** (1975) 985–1007, and "On the duality condition for quantum fields," **17** (1976) 303–321, for the modular identification used here.
- R. Kubo, "Statistical-mechanical theory of irreversible processes. I," *Journal of the Physical Society of Japan* **12** (1957) 570–586; P. C. Martin and J. Schwinger, "Theory of many-particle systems. I," *Physical Review* **115** (1959) 1342–1373; and R. Haag, N. M. Hugenholtz, and M. Winnink, "On the equilibrium states in quantum statistical mechanics," *Communications in Mathematical Physics* **5** (1967) 215–236, for the KMS condition and its characterization of thermal equilibrium.
- M. Takesaki, *Tomita's Theory of Modular Hilbert Algebras and Its Applications* (Springer, 1970), for the modular theory of von Neumann algebras.
- N. D. Birrell and P. C. W. Davies, *Quantum Fields in Curved Space* (Cambridge, 1982), and R. M. Wald, *Quantum Field Theory in Curved Spacetime and Black Hole Thermodynamics* (Chicago, 1994), for the standard derivations of the temperature from the two-point function and from surface gravity.
- R. Haag, *Local Quantum Physics: Fields, Particles, Algebras* (Springer, 1996), for the algebraic setting in which the wedge-restricted vacuum is a KMS state.
- S. Takagi, "Vacuum noise and stress induced by uniform acceleration," *Progress of Theoretical Physics Supplement* **88** (1986) 1–142, for the detector response and the Planck spectrum.
- Companion articles: *The KMS Condition and the Biquaternion Framework*; *The Partition Function in Biquaternionic Form*; *Canonical Quantization of the Biquaternion Maxwell Field*; *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*; *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*; *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*; *Curved Spacetime and the Biquaternion Framework*; *The Lorentz Transformation as a Biquaternionic Rotation*; *The Lorentz Group in Biquaternionic Form: Structure and Representations*; *Introduction to the Biquaternion Universe*.
