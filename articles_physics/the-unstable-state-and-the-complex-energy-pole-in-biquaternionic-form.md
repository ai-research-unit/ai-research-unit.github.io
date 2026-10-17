# __The Unstable State and the Complex Energy Pole in Biquaternionic Form__

## Introduction

An **unstable state** is a state that is not an eigenstate of the Hamiltonian that governs it. A system prepared in it does not remain in it, and the probability of finding the system still in the initial state falls away from one. That probability is the **survival probability**, and the rate of its fall is the **decay rate**. The unstable state is one of the few objects in quantum theory whose natural description is not a real number: it is described by a **complex energy** whose imaginary part is half the width of the state, the width being the inverse lifetime.

This article treats the unstable state in the biquaternion framework of this series. It answers two questions.

- **How does a lifetime arise?** A state decays when the Hamiltonian couples it to a continuum of other states. The coupling displaces the pole of the resolvent off the real energy axis. The displacement is the **self-energy**; its real part is the **level shift** and its imaginary part is half the **width**, which fixes the lifetime by $\tau=\hbar/\Gamma$. The displaced pole lives on the second sheet of the energy plane, reached by continuing the self-energy across the cut that the continuum opens.
- **Where does the pole live in the algebra?** The answer is the article's principal structural finding. The pole is a **complex number of the centre** $\mathbb{C}_{\mathbb{B}}$. The Hamiltonian may carry an arbitrary non-central part, spread over the algebra's imaginary directions and coupling the two slots of the state module; the number that fixes the lifetime does not. A non-central coupling reaches the lifetime only after being traded for an **effective central self-energy** of the same kind a coupling to a continuum produces.

The article is organised as follows. A first section defines the survival amplitude and the survival probability in the module and records the exact short-time law, which is quadratic and which no pure exponential satisfies. A second writes the resolvent of the interacting Hamiltonian, defines the self-energy, and locates the pole on the second sheet. A third reads the pole in the algebra: its conjugate mirror, and its centrality. A fourth derives the effective central self-energy of a block that couples the two module slots, which is the framework's form of the statement that a state-dependent coupling can be eliminated into a complex central potential. A fifth treats the exactly soluble case and separates what is transcribed from the external literature from what is recomputed here. A sixth gives the decay law and its limits, and a seventh separates what the algebra adds from what it does not. The closing sections are the open questions, the summary, the notation table and the external reading.

**Conventions.** We use those of *Conventions in the Biquaternion Universe*, *Introduction to the Biquaternion Universe* and *Quantum Physics in Biquaternionic Form*. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with units $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_\mu^2=-e_t$, and central scalar imaginary $i$ with $i^2=-1$. The Hermitian subspace is $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$; the Hamiltonian is $\tilde H\in\mathbb{M}_+$, so that

$$
\tilde H = h_0\,e_t + i\,\vec h, \qquad h_0\in\mathbb{R},\quad \vec h\in\mathbb{R}^3,
$$

and the centre is $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$. The state module is $S=\mathbb{B}\tilde\Pi\cong\mathbb{C}^2$ with the dictionary $\mathsf{M}_2(\vec e_\mu)=-i\sigma_\mu$ and $\mathsf{M}_2(i\vec e_\mu)=\sigma_\mu$; a pure state is the idempotent $\tilde P=\tfrac12(e_t+i\vec u)$ with $\vec u$ a unit vector along the $\vec e_\mu$, and $\mathrm{Tr}(\tilde P)=1$. The trace convention is $\mathrm{Tr}=2\,\mathrm{Sc}$. The dynamics is $\tilde U(t)=\exp(-i\tilde Ht/\hbar)$ with the state evolving by conjugation, $\tilde\rho(t)=\tilde U(t)\tilde\rho(0)\tilde U(t)^{*}$; the evolution is unitary, $\tilde U\tilde U^{*}=e_t$, and the scalar part $h_0$ of the Hamiltonian contributes only a global phase to the conjugated state. Energies are measured in the same units as $\hbar\omega$.

The convention for the resolvent follows *The Resolvent Operator*, which writes $R(\lambda)=(L-\lambda)^{-1}$; this article writes the Green's function $G(z)=(z-\tilde H)^{-1}$, so the two are related by $G(z)=-R(z)$, and the poles are the eigenvalues in both.

## The Unstable State and the Survival Amplitude

### The survival amplitude and the survival probability

Let $\tilde P_0\in\mathbb{M}_+$ be the idempotent of the state prepared at $t=0$, and let $\tilde\rho(t)=\tilde U(t)\tilde P_0\tilde U(t)^{*}$ be its evolution. The probability that the system is found in the initial state at time $t$ is the pairing of the evolved state with the initial projector,

$$
P(t) = \mathrm{Tr}\bigl(\tilde P_0\,\tilde\rho(t)\bigr)
= \mathrm{Tr}\bigl(\tilde P_0\,\tilde U(t)\,\tilde P_0\,\tilde U(t)^{*}\bigr).
$$

Because $\tilde P_0$ has rank one, $\tilde P_0\tilde U\tilde P_0 = A(t)\,\tilde P_0$ with

$$
A(t) = \mathrm{Tr}\bigl(\tilde P_0\,\tilde U(t)\bigr) = \mathrm{Tr}\bigl(\tilde P_0\,\exp(-i\tilde Ht/\hbar)\bigr),
$$

and the survival probability is the squared modulus of the **survival amplitude**,

$$
P(t) = \lvert A(t)\rvert^{2}.
$$

Unitarity bounds it,

$$
0\le P(t)\le 1, \qquad P(0)=1,
$$

which is the norm-preservation theorem of *Unitarity from Centrality: The Biquaternion Norm-Preservation Theorem* read on a single state. The survival amplitude is thus the scalar reduction of the evolution operator, and it is a complex number at every time; the unstable state is the case in which its modulus falls away from one.

### The short-time law

The expansion of the exponential to second order gives the exact start of the survival probability. Writing the variance of the Hamiltonian in the initial state,

$$
(\Delta\tilde H)^{2} = \mathrm{Tr}\bigl(\tilde P_0\tilde H^{2}\bigr) - \Bigl(\mathrm{Tr}\bigl(\tilde P_0\tilde H\bigr)\Bigr)^{2} \ge 0,
$$

one has

$$
P(t) = 1 - \frac{(\Delta\tilde H)^{2}}{\hbar^{2}}\,t^{2} + O(t^{4}).
$$

The odd powers are absent: at order $t$ the two linear terms of $A(t)$ and its conjugate combine into the quadratic term of the modulus, and the cubic term of $A(t)$ is purely imaginary and does not reach the modulus at order $t^{3}$. The variance is non-negative, so the survival probability leaves one from below, quadratically. This is the analytic content of the quantum Zeno effect, and it is a constraint that no pure exponential can meet: a function $\exp(-\gamma t)$ has a linear slope $-\gamma$ at the origin, whereas the exact survival probability has vanishing slope there.

The consequences are worth stating together.

- **The exact law is quadratic at the origin.** For every state with $(\Delta\tilde H)^2>0$ the decay must begin as $1-O(t^2)$.
- **The exponential is an intermediate-time approximation.** A decay law of the form $\exp(-\Gamma t/\hbar)$ can hold only for times long compared with the inverse spectral width of the continuum and short compared with the onset of the long-time deviations, and it is the approximation, not the exact law.
- **The two statements do not conflict.** The measured exponential of an unstable state is a fit over an intermediate window; the quadratic start and the power-law tail are outside that window.

## The Resolvent, the Self-Energy, and the Pole

### The Green's function

For a Hamiltonian $\tilde H$ the Green's function is

$$
G(z) = (z-\tilde H)^{-1}, \qquad z\in\mathbb{C}_{\mathbb{B}},
$$

an operator-valued function analytic on the resolvent set and with the spectrum for its singular set. The energy $z$ is a complex number of the centre; the singularities of $G$ on the real axis are the eigenvalues of $\tilde H$, and they are real because $\tilde H$ is Hermitian. Hermiticity also gives the conjugation property used below,

$$
G(z)^{\dagger} = G(\bar z),
$$

which is the matrix form of the reflective symmetry of the resolvent in the real axis. The conventions for the four prescriptions that select the physical branch of $G$ at the real axis — retarded, advanced, Feynman and anti-Feynman — are those of *The Klein–Gordon Propagator and Its Green's Functions in Biquaternionic Form* and *The Feynman Propagator in Biquaternionic Form*; this article uses the retarded branch, that is, the boundary value from above, $z=E+i0^{+}$.

### The self-energy

Split the Hamiltonian into a solvable part and a coupling, $\tilde H=\tilde H_0+\tilde V$, and let $\tilde P_0$ project on the state of interest with $\tilde H_0\tilde P_0=E_0\tilde P_0$. Write $Q=e_t-\tilde P_0$ for the complementary projection and $Q\tilde HQ$ for the coupling restricted to it. The scalar Green's function of the distinguished state is the **reduced resolvent**

$$
G_{00}(z) = \mathrm{Tr}\bigl(\tilde P_0\,G(z)\bigr) = \mathrm{Tr}\bigl(\tilde P_0\,G(z)\,\tilde P_0\bigr),
$$

and the block identity of *The Resolvent Operator* gives it the closed form

$$
G_{00}(z) = \frac{1}{z-E_0-\Sigma(z)},
\qquad
\Sigma(z) = \mathrm{Tr}\bigl(\tilde P_0\tilde V\tilde P_0\bigr)
+ \mathrm{Tr}\Bigl(\tilde P_0\tilde V\,Q\frac{1}{z-Q\tilde HQ}Q\,\tilde V\tilde P_0\Bigr).
$$

The quantity $\Sigma(z)$ is the **self-energy**. It is a scalar function of the central variable $z$ — a complex number of the centre — and it collects the entire effect of the coupling on the distinguished state. To second order in $\tilde V$, with $\lvert 0\rangle$ the state and $\lvert n\rangle$ a complete set spanning $Q$, it is

$$
\Sigma(z) = \langle 0\lvert\tilde V\rvert 0\rangle
+ \sum_{n\neq0}\frac{\lvert\langle 0\lvert\tilde V\rvert n\rangle\rvert^{2}}{z-E_n}
+ O(\tilde V^{3}).
$$

The sum is over the states the coupling reaches. When those states form a discrete set the sum is a finite or countable sum of simple poles on the real axis; when the Hamiltonian has a **continuum** the sum becomes an integral and its limit at the real axis is a **branch cut**. The distinction is the whole content of the unstable state.

### The pole

Write the boundary value of the self-energy from above as

$$
\Sigma(E+i0^{+}) = \Delta(E) - \tfrac{i}{2}\,\Gamma(E),
$$

with $\Delta$ and $\Gamma$ real. The sum representation identifies them: the real part is the **level shift**, present even without a continuum, and the imaginary part is produced by the on-shell states only, through the delta contribution of each pole as it is pushed onto the axis,

$$
\Gamma(E) = 2\pi\sum_{n}\lvert\langle 0\lvert\tilde V\rvert n\rangle\rvert^{2}\,\delta(E-E_n)
= 2\pi\,\lvert V_0(E)\rvert^{2}\,\rho(E),
$$

where $V_0(E)$ is the coupling to the continuum at energy $E$ and $\rho(E)$ is its density of states. This is the **Golden Rule** width. It is non-negative, so the self-energy moves the pole into the lower half plane and never into the upper one, and a state coupled to a continuum at the retarded prescription can only decay.

The pole itself is a zero of $z-E_0-\Sigma(z)$,

$$
z_\star = E_0 + \Delta(E_0) - \tfrac{i}{2}\,\Gamma(E_0) + O(\Gamma^{2}),
$$

to leading order in the width. The important point is that this zero does **not** lie on the first sheet, where the analytic structure of $G_{00}$ is the real axis with a cut. It lies on the **second sheet**, the one reached by continuing $z$ through the cut, across which the self-energy jumps by the discontinuity of the integral. That discontinuity is fixed by the same continuum density that gave the width: for a continuum of density $\rho$ and coupling $V_0$ the two boundary values of the self-energy differ by $-2\pi i\lvert V_0\rvert^{2}\rho = -i\,\Gamma$, so the continuation onto a second sheet replaces $\Sigma$ by $\Sigma\mp i\Gamma$, the two signs being the two sheets reached by going round the two ends of the cut. The decaying pole is the one on the sheet with the lower sign, $\Sigma_{\mathrm{II}}=\Sigma-i\Gamma$, whose denominator is $z-E_0-\Sigma(z)+i\Gamma$; its zero sits at $z_\star$ as stated. The opposite sign carries the zero to $E_0+\Delta+\tfrac{i}{2}\Gamma$, the mirror pole of the other sheet. The unstable state is therefore not an eigenstate of a non-Hermitian operator on the physical sheet; it is the shadow of the physical resolvent on the second one.

## The Pole in the Algebra

### The conjugate mirror

Because $\tilde H$ is Hermitian, the Green's function satisfies $G(\bar z)=G(z)^{\dagger}$, and the reduced scalar therefore satisfies

$$
G_{00}(\bar z) = \overline{G_{00}(z)}.
$$

On the first sheet the denominator $z-E_0-\Sigma(z)$ inherits that symmetry: its zero set is mapped to itself by $z\mapsto\bar z$, so a complex zero would have to appear in a conjugate pair. No such pair exists, and the reason is structural: $G_{00}$, the resolvent of a Hermitian operator compressed onto one vector, is analytic off the real axis, so it has no pole there, and the unstable state therefore has no home on the first sheet at all. The symmetry is broken on the second sheet, where the branch term $i\Gamma$ is a fixed imaginary constant rather than a conjugate-symmetric function: the decaying pole at $E_0+\Delta-\tfrac{i}{2}\Gamma$ and its mirror at $E_0+\Delta+\tfrac{i}{2}\Gamma$ are the two second sheets of the continuation — the retarded and the advanced one — and not two poles of a single function, and the retarded boundary condition is what selects the sheet. This is the same pairing that *Spectral Theory on Krein Spaces* records for the spectrum of a $J$-self-adjoint operator, where complex eigenvalues appear in conjugate pairs; here the pair is split across the two sheets, and the retarded condition keeps the decaying member. The algebra alone does not fix which sheet is realised: the boundary condition does.

### The pole is central

The self-energy $\Sigma(z)$ is a scalar function of the central variable $z$, and the equation that fixes the pole, $z-E_0-\Sigma(z)=0$, is an equation between complex numbers of the centre. The pole $z_\star$, the level shift $\Delta$, the width $\Gamma$ and the lifetime $\tau=\hbar/\Gamma$ are therefore **central**, whatever the direction of $\vec h$ in the Hamiltonian and however the non-central part couples the slots of the module. This is the article's structural statement, and it is the theorem behind the fifth limit of *The Biquaternion Universe as an Improvement of the Quaternionic Quantum Theory* — a dynamics that preserves the Hermitian norm for every Hermitian generator forces its unit into the centre, *Unitarity from Centrality: The Biquaternion Norm-Preservation Theorem* — read here at the level of a displaced pole. The same centrality that fixes the norm-preserving unit fixes the pole.

The centrality is not a coincidence of the models treated below. It is a consequence of taking the trace over the module to reach the scalar Green's function: the trace of a module operator is central, and any quantity read from the trace is central with it.

## Eliminating a Coupling Between the Two Slots

### The reduction

The state module splits into two orthogonal summands, and a Hamiltonian that couples them can be written in the corresponding block form. Let $\tilde\Pi$ be the idempotent of one summand and $S=S_1\oplus S_2$ the splitting $S_1=\tilde\Pi S$, $S_2=(e_t-\tilde\Pi)S$. In the module basis, with $\tilde H$ Hermitian, the matrix image of the Hamiltonian is

$$
H = \begin{pmatrix} H_{\mathrm{c}} & V \\ V^{*} & H_{\mathrm{nc}}\end{pmatrix},
$$

where $H_{\mathrm{c}}$ governs the first slot, $H_{\mathrm{nc}}$ the second, and $V$ is the off-diagonal entry through which the two are coupled — the entry into which the non-central part $i\vec h$ of $\tilde H$ enters. The block identity of *The Resolvent Operator*, applied to this splitting, gives the Green's function of the first slot its reduced form,

$$
G_{\mathrm{c}}(z) = \Bigl(z - H_{\mathrm{c}} - V\frac{1}{z-H_{\mathrm{nc}}}V^{*}\Bigr)^{-1}
= \bigl(z - H_{\mathrm{c}} - \Sigma_{\mathrm{nc}}(z)\bigr)^{-1},
\qquad
\Sigma_{\mathrm{nc}}(z) = V\frac{1}{z-H_{\mathrm{nc}}}V^{*}.
$$

The coupling $V$ has disappeared from the first slot and reappeared as the energy-dependent addition $\Sigma_{\mathrm{nc}}(z)$. Its entire effect on the first slot is that addition; and because the two slots are one-dimensional, the entries of the block matrix are complex numbers of the centre, so $\Sigma_{\mathrm{nc}}(z)$ is central, and with it the effective Hamiltonian of the first slot, $H_{\mathrm{c}}+\Sigma_{\mathrm{nc}}(z)$.

### The complex effective potential

The self-energy $\Sigma_{\mathrm{nc}}$ is the same object as before, with the eliminated slot playing the role of the continuum. Its two cases are the two familiar ones.

- **A discrete eliminated slot** gives a real, energy-dependent shift: the coupling displaces the level of the first slot, and the displacement is the level shift.
- **An eliminated slot with a continuum** gives a complex self-energy, and the effective central potential acquires an imaginary part. The eliminated slot then acts as an absorber for the first: the coupling that would have moved probability into it appears in the first slot's equation as a width.

This is the framework's form of the standard statement that a degree of freedom coupled to a continuum and then integrated out produces an absorptive effective potential — the **optical potential** of scattering theory and of the quaternionic formulation of the same problem. It also explains why an effective potential must be allowed to be complex: complexity is the signature of a channel that has been removed and whose on-shell states are now a loss. The reduction is a different decomposition from the sector maps catalogued in *Cross-Sector Coupling in the Biquaternion Framework: A Catalogue of the Maps Between the Sectors*, because it splits the module rather than the algebra's Hermitian and anti-Hermitian parts, and it is not one of that catalogue's entries.

## The Exactly Soluble Case

### The model and its solution

The simplest illustration is the model in which a single discrete state of energy $E_0$ is coupled to a continuum of states $\{E\}$ and the continuum states do not couple among themselves. The model is soluble precisely because the second condition truncates the self-energy sum at second order: the reduced equation

$$
z - E_0 - v - \int dE\,\frac{\lvert V(E)\rvert^{2}\rho(E)}{z-E} = 0
$$

is one scalar equation, not an integral equation, and it determines the pole in closed form once the continuum coupling and density are specified. The diagonal element $v=\langle 0\rvert\tilde V\lvert 0\rangle$ is the discrete level shift, and the integral is the continuum part. For a band of constant density $\rho$ on $[-B,B]$ the integral is elementary,

$$
\int_{-B}^{B}\frac{\rho\,dE}{z-E} = \rho\ln\frac{z+B}{z-B},
$$

and the whole analytic structure of the model is the logarithm: a cut on the band, no complex zero on the first sheet, and a single complex zero on the second sheet at $E_0+v-\tfrac{i}{2}\Gamma$ for small coupling.

### What is transcribed, recomputed, and the corpus's own

**Transcribed from the external literature.** The model itself, its solubility, the log shape of the band self-energy, the Golden Rule width $\Gamma=2\pi\lvert V_0\rvert^{2}\rho$, the level shift, the placement of the resonance on the second sheet, and the intermediate-time exponential are standard results of scattering theory and are cited as such in the reading at the end of the article.

**Recomputed here.** The rules this article states were checked by direct recomputation on the explicit complex arithmetic of the module image. The short-time law was confirmed in two ways: from the moments of the Hamiltonian in the state, whose values $\langle\tilde H^n\rangle$ for $n=1,2,3,4$ are $-0.021836735$, $0.622340816$, $0.446589449$, $0.727840803$, giving the variance $(\Delta\tilde H)^{2}=0.621863973344$ and the exact fourth-order coefficient $0.160731108310$; and by an explicit evolution, whose ratio of $P(t)-[1-(\Delta\tilde H)^{2}t^{2}]$ to $t^{4}$ is $0.160690$, $0.160724$ and $0.160729$ at $t=0.05$, $0.02$ and $0.01$, converging to the coefficient. The survival probability does not exceed one on $t\in[0,20]$. The conjugation property $G(\bar z)=G(z)^{\dagger}$ was confirmed to $3\times10^{-15}$ over random Hermitian matrices and central complex $z$. The block identity $G_{\mathrm{c}}=(z-H_{\mathrm{c}}-\Sigma_{\mathrm{nc}})^{-1}$ was confirmed against the direct inverse of a $5\times5$ Hermitian block matrix to $2\times10^{-16}$ on a $2+3$ splitting. In the band model the boundary value was confirmed at $\mathrm{Im}\,\Sigma(E_0+i0^{+})=-\Gamma/2$ and the discontinuity at $\Sigma(E_0+i0^{+})-\Sigma(E_0-i0^{+})=-i\Gamma$ to nine digits; a random search of four thousand points found no complex zero of the first-sheet equation $z-E_0-\Sigma(z)=0$; and the second-sheet zero was located at $z_\star$ with $\lvert\mathrm{Im}\,z_\star\rvert/(\Gamma/2) = 1.0008$, $1.0050$ and $1.0204$ for $g=0.02,0.05,0.10$, the departure from one being $2g^{2}$ to three digits ($2.002$, $2.010$, $2.040$ divided by $g^{2}$ at the same three couplings).

**The corpus's own.** The reading of the pole as a central complex number; the identification of the second sheet as the home of the unstable state, with the conjugate partner on the mirror sheet rather than on the first; the reduction of a coupling between the two slots to an effective central self-energy; the boundary condition's choice of sheet; and the separation of the level shift from the width as the Hermitian and anti-Hermitian aspects of one scalar.

## The Decay Law and Its Limits

The pole fixes the intermediate-time survival amplitude. Since the pole is at $z_\star=E_0+\Delta-\tfrac{i}{2}\Gamma$,

$$
A(t)\simeq \exp(-iz_\star t/\hbar) = \exp(-i(E_0+\Delta)t/\hbar)\,\exp(-\Gamma t/(2\hbar)),
\qquad
P(t)\simeq \exp(-\Gamma t/\hbar),
$$

and the lifetime is

$$
\tau = \frac{\hbar}{\Gamma}.
$$

The approximation has a definite domain, and outside it the pole does not describe the decay.

- **Very short times.** The exact law is $1-O(t^{2})$, and the exponential has a linear term. The pole sum cannot be correct at the origin; the full survival probability must be used there. For the model of this article the crossover is at times of order $\hbar/B$, the inverse bandwidth.
- **Very long times.** The long-time survival probability is governed by the threshold of the continuum and falls more slowly than exponentially, with a power law set by the density of states at the band edge. The pole captures the intermediate window only.
- **The residue.** The residue of $G_{00}$ at $z_\star$ is the squared overlap of the decaying state with the initial state, the quantity that in field theory is called the wave-function renormalization at the resonance, and it is less than one when the state is spread over the continuum. This is the same residue that *The LSZ Reduction Formula in Biquaternionic Form* reads as wave-function renormalization.

The article therefore states an approximation with its window, not a law. It makes no claim that the non-exponential terms are observable, and none is needed for the exponential regime to be correct where it is used.

## What the Algebra Adds and What It Does Not

**What the algebra adds.**

- **The pole is central.** The width and the level shift are the imaginary and real parts of one complex number of the centre, and this holds whatever non-central coupling is present. The lifetime is a central quantity even when the state is not the module's only content.
- **The coupling between the slots is not an independent channel.** A coupling that connects the two slots of the module can be eliminated, and its effect on the surviving slot is an effective central self-energy. The framework thus says in its own terms why a complex effective potential is not an extra degree of freedom but the trace of a removed one.
- **The two sheets and the branch.** The centrality of the pole and the conjugate symmetry together give the unstable state its place: the first sheet carries no complex pole, and the decaying complex number sits on the second sheet, with its mirror partner on the conjugate (advanced) sheet. The algebra's antiunitary structure supplies the pairing; the boundary condition supplies the choice of sheet.

**What the algebra does not add.**

- **No scale.** The algebra fixes no value of $\Gamma$. The decay rate is fixed by the coupling and the density of states, both of which are inputs. This is the same absence of scale recorded in *Action, Units, and the Constants of the Biquaternion Universe*, and it means the framework can describe a lifetime but cannot predict one.
- **No prediction.** For a given coupling and continuum the framework gives the same exponential, the same width and the same level shift as the standard treatment. Nothing here distinguishes the two.
- **No specific particle's lifetime.** A lifetime becomes a number only when the coupling is known. The neutron's beta decay, for instance, needs a weak chiral gauge structure the framework does not contain, and its lifetime therefore remains outside the framework; the mechanism by which a coupling becomes a lifetime is now stated, and is the boundary at which *The Neutron in Biquaternionic Form* now stands, but the coupling is not supplied.

## Open Questions

**1. Is there an algebraic home for the decaying state?** The pole is a central complex number, but the state that carries it is not a normalisable module element once the continuum is present. Whether the framework's direct-integral description of the module, used in *The Biquaternion Framework and the Canonical Commutation Relation: Independence, Not a Defect* to carry the continuum, can give the decaying state an algebraic home as a distributional element is not settled here.

**2. Is the decay rate a Lyapunov exponent?** The decay rate and the Lyapunov exponent of *The Lyapunov Exponent and Information Loss in the Biquaternion Framework* are both exponential loss rates of an initial condition. Whether they are the same quantity in the framework, or two limits of one, is not known.

**3. Does the second sheet have a module meaning?** The second sheet was reached here by the continuation of a scalar integral. Whether the sheet structure can be read from the module's own analytic geometry, as the corpus's function theory reads the polar and spinor representations, is open.

**4. Empirical content.** The framework's exponential agrees with the standard one wherever the standard one applies, and it supplies no discriminator. Whether any of the non-exponential departures could carry a signature is open and unexplored.

## Summary

The unstable state is the state that is not an eigenstate of the Hamiltonian. Its survival amplitude is the scalar reduction of the evolution, $A(t)=\mathrm{Tr}(\tilde P_0\tilde U(t))$, and its survival probability is $P(t)=\lvert A(t)\rvert^{2}$, unitarity bounding it by one. The exact short-time law is $P(t)=1-(\Delta\tilde H)^{2}t^{2}/\hbar^{2}+O(t^{4})$, with the variance of the Hamiltonian in the initial state as coefficient, and no pure exponential satisfies it.

The coupling of the state to a continuum displaces the pole of the reduced resolvent, $G_{00}(z)=[z-E_0-\Sigma(z)]^{-1}$, where the self-energy is $\Sigma(z)=\langle 0\rvert\tilde V\lvert 0\rangle+\sum_{n\neq0}\lvert V_{0n}\rvert^{2}/(z-E_n)+\cdots$ to second order. Its boundary value from above is $\Delta(E)-\tfrac{i}{2}\Gamma(E)$, with the level shift $\Delta$ real and the width non-negative, $\Gamma(E)=2\pi\lvert V_0(E)\rvert^{2}\rho(E)$ at the Golden Rule. The pole is at $z_\star=E_0+\Delta-\tfrac{i}{2}\Gamma$, and it lies on the second sheet, reached by continuing across the cut that the continuum opens, with the jump $\Sigma(E+i0^{+})-\Sigma(E-i0^{+})=-i\Gamma$; the first sheet carries no complex zero, only the real eigenvalues and the cut.

The pole is a **complex number of the centre**. Hermiticity gives $G(\bar z)=G(z)^{\dagger}$ and its scalar reduction $G_{00}(\bar z)=\overline{G_{00}(z)}$, so a complex pole cannot sit on the first sheet; the decaying number at $E_0+\Delta-\tfrac{i}{2}\Gamma$ and its mirror at $E_0+\Delta+\tfrac{i}{2}\Gamma$ are the two second sheets, and the retarded boundary condition keeps the decaying one — the Krein-space pairing of *Spectral Theory on Krein Spaces*, split here across the sheets of the energy plane. The self-energy is a scalar function of the central variable, and the level shift, the width, the pole and the lifetime $\tau=\hbar/\Gamma$ are all central, whatever non-central part the Hamiltonian carries. This is the theorem behind the fifth limit — the norm-preserving unit is central — read at the level of a displaced pole.

A coupling between the two slots of the module is eliminated by the block identity of *The Resolvent Operator*: relative to an orthogonal splitting $S=S_1\oplus S_2$ the Green's function of the first slot is $(z-H_{\mathrm{c}}-\Sigma_{\mathrm{nc}})^{-1}$ with $\Sigma_{\mathrm{nc}}(z)=V(z-H_{\mathrm{nc}})^{-1}V^{*}$. When the eliminated slot is discrete the addition is a real level shift; when it carries a continuum the addition is complex and the effective central potential is absorptive. This is the framework's form of the optical potential, and it explains why an effective potential must be allowed to be complex.

The soluble case is the discrete state coupled to a continuum with no continuum–continuum coupling, whose reduced equation is one scalar equation with the band logarithm $\rho\ln((z+B)/(z-B))$ as its continuum term. The model, the width, the second-sheet placement and the intermediate-time exponential are transcribed from the external literature; the rules of this article were recomputed on the module image, and the checks are listed in the ledger above. The decay law $P(t)\simeq \exp(-\Gamma t/\hbar)$ holds over an intermediate window bounded below by the inverse bandwidth, where the exact quadratic start governs, and above by the continuum threshold, where a power law replaces it.

What the algebra adds is that the pole is central, that a non-central coupling reaches the lifetime only through an effective central self-energy, and that the conjugate symmetry and the choice of sheet are the two halves of one statement. What it does not add is a scale, a prediction, or a specific particle's lifetime; the coupling is always an input, and the framework's agreement with the standard treatment here is exact wherever the standard treatment applies.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra; centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$ |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Hermitian and anti-Hermitian subspaces |
| $\tilde H=h_0e_t+i\vec h$ | Hamiltonian, Hermitian, $h_0\in\mathbb{R}$, $\vec h\in\mathbb{R}^3$ |
| $\tilde P_0$ | Idempotent of the initial state, rank one, $\mathrm{Tr}=1$ |
| $\tilde U(t)=\exp(-i\tilde Ht/\hbar)$ | Unitary evolution, $\tilde U\tilde U^{*}=e_t$ |
| $A(t)=\mathrm{Tr}(\tilde P_0\tilde U(t))$ | Survival amplitude; $P(t)=\lvert A(t)\rvert^{2}$ |
| $(\Delta\tilde H)^{2}$ | Variance of $\tilde H$ in the initial state |
| $G(z)=(z-\tilde H)^{-1}$ | Green's function; $G(z)^{\dagger}=G(\bar z)$ |
| $G_{00}(z)=[z-E_0-\Sigma(z)]^{-1}$ | Reduced resolvent of the distinguished state |
| $\Sigma(z)$ | Self-energy |
| $\Delta(E)$, $\Gamma(E)$ | Level shift and width, $\Sigma(E+i0^{+})=\Delta-\tfrac{i}{2}\Gamma$ |
| $\Gamma=2\pi\lvert V_0\rvert^{2}\rho$ | Golden Rule width |
| $z_\star=E_0+\Delta-\tfrac{i}{2}\Gamma$ | Pole on the second sheet |
| $\tau=\hbar/\Gamma$ | Lifetime |
| $\Sigma_{\mathrm{nc}}(z)=V(z-H_{\mathrm{nc}})^{-1}V^{*}$ | Effective self-energy of an eliminated slot |
| $H_{\mathrm{c}},H_{\mathrm{nc}},V$ | Entries of the slot block matrix; $V$ couples the two slots |
| $\rho(E)$ | Density of continuum states |
| $B$ | Half-width of the band |
| $\mathrm{Tr}=2\,\mathrm{Sc}$ | Trace convention |

## Further Reading

- G. Gamow, "Zur Quantentheorie des Atomkernes," *Zeitschrift für Physik* **51** (1928) 204–212, for the complex energy and the exponential decay law of an unstable state.
- V. Weisskopf and E. Wigner, "Berechnung der natürlichen Linienbreite auf Grund der Diracschen Lichttheorie," *Zeitschrift für Physik* **63** (1930) 54–73, for the self-energy of an unstable state, the level shift and the width.
- V. Fock and N. Krylov, "On the uncertainty relation between energy and time," *Journal of Physics (USSR)* **11** (1947) 112–115, for the energy–time structure of a decaying state.
- K. O. Friedrichs, "On the perturbation of continuous spectra," *Communications on Pure and Applied Mathematics* **1** (1948) 361–406, for the soluble discrete-state-plus-continuum model and its spectral structure.
- T. D. Lee, "Some special examples in renormalizable field theory," *Physical Review* **95** (1954) 1329–1334, for the exactly soluble model with no continuum–continuum coupling.
- U. Fano, "Effects of configuration interaction on intensities and phase shifts," *Physical Review* **124** (1961) 1866–1878, for the projection formalism, the self-energy and the complex pole.
- M. L. Goldberger and K. M. Watson, *Collision Theory* (Wiley, 1964), for the analytic structure of the scattering amplitude, the second sheet and the resonance pole.
- R. G. Newton, *Scattering Theory of Waves and Particles* (Springer, 2nd ed. 1982), for the resolvent, the Jost functions and the resonance poles.
- C. Cohen-Tannoudji, B. Diu, and F. Laloe, *Quantum Mechanics* (Wiley, 1977), for the Golden Rule and the survival probability.
- L. D. Landau and E. M. Lifshitz, *Quantum Mechanics: Non-Relativistic Theory* (Pergamon, 1977), for the quasibound states and the decay of a quasi-stationary state.
- K. Yosida, *Functional Analysis* (Springer, 6th ed. 1980), for the second-sheet continuation and the resolvent of a self-adjoint operator with continuous spectrum.
- S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields* (Oxford, 1995), for the quaternionic formulation of the same problem, the quaternionic inner product and the optical potential.
- L. P. Horwitz, "A soluble model for scattering and decay in quaternionic quantum mechanics I: Decay," report TAUP 2073-93 / IASSNS 92/75 (1993), arXiv:hep-th/9312028, for the exactly soluble decay model in the earlier quaternionic theory.
- L. P. Horwitz, "A soluble model for scattering and decay in quaternionic quantum mechanics II: Scattering," report TAUP 2084-93 / IASSNS 93/51 (1993), arXiv:hep-th/9312029, for the companion scattering theory and the effective optical potential of the same model.
