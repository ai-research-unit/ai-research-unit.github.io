# __The Petiau System and the Quantisation of Mass in Biquaternionic Form__

## Introduction

The masses of the elementary particles are the one part of the Standard Model that the theory does not explain. The renormalisable Lagrangian carries a Yukawa coupling for every charged fermion, and each of those couplings is a free parameter fixed only by measurement; the theory is consistent for any values, and no principle internal to it selects the ones nature uses. The same is true of the gauge-boson masses, which follow from one scalar parameter of the potential. Mass is an input, not an output.

The biquaternion framework does not by itself derive a single mass value — an algebra with no scale cannot. But it carries a specific line of work in which the mass parameter is treated as a **field** and the field equations for the mass are **closed on themselves**. That line runs from Lanczos's 1929 reformulation of Dirac's equation, through Einstein and Mayer's 1933 promotion of the mass to a biquaternion, to Petiau's 1965 closed nonlinear system. The present article states that line, verifies the parts that are pure algebra, and keeps the parts that are speculation labelled as such.

The position is stated at the outset, and the article defends it section by section.

- **Established.** The algebra carries the whole chain. Lanczos's coupled system $\tilde{\nabla}\tilde{A}=m\tilde{B}$, $\tilde{\nabla}\tilde{B}=m\tilde{A}$ is the massless Maxwell equation with a feedback; promoting the scalar $m$ to a biquaternion $\tilde{E}$ turns the second-order equations into **eigenvalue equations for the mass**, whose two eigenvalues are those of $\tilde{E}\tilde{E}^{*}$; the reduction of Petiau's closed system to Lanczos's, for a constant spin-0 field, is exact. These are algebra, and they are checked here.
- **Transcribed.** Petiau's double-periodic waves, the quartic Hamiltonian $H=C_0\mu^4k^2$, and the quantisation of the amplitude and the proper mass are taken from Petiau through the review of Gsponer and Hurni. They are not re-derived here, and their status is that of the source, not of the framework.
- **Empirical.** Barut's leptonic mass formula is an external numerical fit. Its agreement with the lepton data is a fact about the formula and the data, not a framework result, and the ratio $7.46$ of the two singular moduli is offered by the source as a plausible numerical coincidence, not as a derivation.
- **Not supplied.** No mass value is derived from $\mathbb{B}$. The algebra is scale-free, the standard-model agenda's ledger is unchanged, and the article's contribution is to place the Lanczos–Einstein–Mayer–Petiau construction in the corpus with its verified content and its labelled speculation separated.

The article is organised as follows. The next section sets up the mass as a field, from the Lanczos feedback through the Einstein–Mayer mass biquaternion to the eigenvalues that read as two masses. A section states Petiau's closure of the system and checks its reduction to Lanczos. Two sections give the double-periodic waves and the quartic Hamiltonian. A section gives Barut's empirical formula and the moduli ratio, with its status. A closing section separates what is supplied, transcribed, and missing.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, $e_1e_2=e_3$ and cyclic, central scalar imaginary $i$, $i^2=-1$, and $\mathbb{B}\cong M_2(\mathbb{C})$. The biquaternionic gradient is $\tilde{\nabla}=e_0\,\partial_{ict}+e_1\partial_x+e_2\partial_y+e_3\partial_z$, its quaternion conjugate is $\tilde{\nabla}^{\natural}=e_0\,\partial_{ict}-e_1\partial_x-e_2\partial_y-e_3\partial_z$, and $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}=\tilde{\nabla}^{\natural}\tilde{\nabla}=\partial_{ict}^2+\Delta$ is the series' d'Alembertian. The biquaternion norm is $N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}=\sum_\mu Q_\mu^2$, whose vanishing defines the **singular** (null) biquaternions; the conjugations are ${}^{\natural}$, the coefficient conjugation $\bar{\cdot}$, the Hermitian ${}^{*}={}^{\natural}\circ\bar{\cdot}$ and the anti-Hermitian $\flat=-{}^{*}$. The trace is $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H}) = 2\langle\tilde{P},\tilde{H}\rangle$. Standard-model quantities — Yukawa couplings, the charged-lepton and quark masses in $\mathrm{MeV}/c^2$, the fine-structure constant $\alpha$ — are used where standard physics is named and are not framework structure.

The framework results used here are those of the companion articles:

- Companion article *The Standard Model under the Biquaternion Framework — A Research Agenda*, whose sub-section *The Gürsey Reading, the Reversion Test, and the Einstein–Mayer Equation* first records the Lanczos system, the Einstein–Mayer equation and the isospin reading; the present article takes the same equations as its starting point and does not repeat the isospin reading.
- Companion article *The Dirac Equation in Biquaternionic Form*, for the biquaternionic Dirac equation, its linear off-diagonal mass term, and the relation of the massive equation to the massless one.
- Companion article *The Proca Equation: Massive Spin 1 in Biquaternionic Form*, for the massive spin-1 equation that the same feedback produces.
- Companion article *The Magnetic Monopole in Biquaternionic Form*, for the source-free half of the Maxwell equation that the subtraction of the feedback isolates.
- Companion article *Conventions in the Biquaternion Universe*, for the algebra, the conjugations, the metric and the d'Alembertian.
- Companion article *Biquaternion Idempotents and Projections* and *The Biquaternion Involution Lattice: Hermitian, Anti-Hermitian and Reversal*, for the idempotents, the zero divisors and the conjugations.
- Companion article *The Number of Generations and the Biquaternion Algebra*, for the corpus's standing position that the algebra accommodates but does not derive the particle spectrum.

## The Mass Term as a Field

### The Lanczos Feedback System

Maxwell's source-free equation in biquaternionic form is $\tilde{\nabla}\tilde{F}=0$, the complex-vector equation of Conway and Silberstein, and its inhomogeneous companion is $\tilde{\nabla}\tilde{F}=-\tilde{R}$ for a source biquaternion $\tilde{R}$. Lanczos's observation, in 1929, was that the same two-slot equation with a **feedback** on the right-hand side describes a massive particle of spin $\frac{1}{2}$:

$$
\tilde{\nabla}\tilde{A} = m\tilde{B},
\qquad
\tilde{\nabla}\tilde{B} = m\tilde{A},
$$

where $\tilde{A}$ and $\tilde{B}$ are two biquaternion fields and $m=mc/\hbar$ is the mass in inverse-length units. The equation is Maxwell's with the source replaced by the other field, and this is what "feedback" means: the two fields source each other. Following Lanczos, that self-sourcing is the algebraic mark of a **massive** particle, as against the massless photon, whose field is its own source-free equation.

The system is invariant under $\tilde{A}\to\tilde{A}G$, $\tilde{B}\to\tilde{B}G$ for a unitary biquaternion $G$, and its superposition $D=\tilde{A}\sigma+\tilde{B}^{*}\bar{\sigma}$, with $\sigma$ an idempotent of the algebra, is **strictly equivalent to Dirac's equation**. That equivalence, the spin axis it makes explicit, and the isospin reading of the doubled solution count are recorded in the standard-model agenda article and are not repeated here. What matters for the present article is one structural fact: **the mass enters as a single scalar parameter $m$ multiplying the other field**, and the two fields obey the same second-order equation, obtained by applying the conjugate gradient,

$$
\Box\tilde{A} = m^2\tilde{A},
\qquad
\Box\tilde{B} = m^2\tilde{B}.
$$

The mass is a number, the same for both fields, and this is the Standard Model's situation reproduced in the algebra.

### The Einstein–Mayer Mass Biquaternion

Einstein and Mayer, in 1933, took the step that makes the construction a theory of mass rather than a rewriting of Dirac's. The scalar $m$ is promoted to a biquaternion $\tilde{E}$, the **mass field**, and the system becomes

$$
\tilde{\nabla}\tilde{A} = \tilde{B}\tilde{E}^{*},
\qquad
\tilde{\nabla}\tilde{B} = \tilde{A}\tilde{E}.
$$

For a constant central $\tilde{E}=m e_0$ the equations reduce to the Lanczos system above, since a central element commutes with everything: $\tilde{B}\tilde{E}^{*}=\tilde{B}m=m\tilde{B}$ and $\tilde{A}\tilde{E}=m\tilde{A}$. This reduction is exact and is checked here. So the Einstein–Mayer system is the Lanczos system with a **field-valued** mass, and the mass parameter has become a dynamical object.

The reduction is not the point; the eigenvalue is. Applying the conjugate gradient to the first-order pair, and taking $\tilde{E}$ constant so that the derivatives do not act on it, gives

$$
\Box\tilde{A} = \tilde{A}\,\bigl(\tilde{E}\tilde{E}^{*}\bigr),
\qquad
\Box\tilde{B} = \tilde{B}\,\bigl(\tilde{E}^{*}\tilde{E}\bigr).
$$

The mass is no longer a number multiplying the field; it is an **operator** acting on the field from the right, and the mass-squareds of the two fields are the eigenvalues of $\tilde{E}\tilde{E}^{*}$ (equivalently of $\tilde{E}^{*}\tilde{E}$, which has the same nonzero spectrum). The mass field $\tilde{E}$ has become the object that **determines** the masses, and the two masses of a doublet are read off from one biquaternion.

### The Two Masses and the Two-Mode Structure

The two eigenvalues of $\tilde{E}\tilde{E}^{*}$ are the two mass-squareds, and everything depends on which kind of biquaternion $\tilde{E}$ is. Three cases exhaust the structure the corpus uses, and each is checked here on random elements.

**A real scalar, $\tilde{E}=s e_0$.** Then $\tilde{E}\tilde{E}^{*}=s^2 e_0$, a central element, and both eigenvalues equal $s^2$: the doublet is **degenerate**, the two particles have equal mass $|s|$, and the operator $\tilde{E}$ is a scalar in disguise. This is the case the source reads as the **proton–neutron** doublet, with the equal-mass pair of the isospin multiplet.

**A Hermitian idempotent, $\tilde{E}=\tilde{\Pi}$.** Then $\tilde{E}^{*}=\tilde{E}$ and $\tilde{E}^2=\tilde{E}$, so $\tilde{E}\tilde{E}^{*}=\tilde{E}$, which is a rank-one projection: its eigenvalues are $1$ and $0$. The doublet is **split**, one mode massive and one massless. This is the case the source reads as the **electron–neutrino** doublet — the charged fermion and its massless partner.

**A singular biquaternion, $N(\tilde{E}) = \langle\tilde{E},\tilde{E}\rangle_{\natural}=0$.** Then $\det\Phi(\tilde{E}\tilde{E}^{*})=|N(\tilde{E})|^2=0$, so at least one eigenvalue vanishes: **a singular mass field always leaves a massless mode**, whatever else it does. The identity $\det\Phi(\tilde{E}\tilde{E}^{*})=|N(\tilde{E})|^2$ is the determinant of the matrix of the mass operator, and it is verified here; the vanishing of the norm is exactly the condition the idempotent case realises. The corpus's example $\tilde{E}=e_1+ie_2$ is singular, $N(e_1+ie_2)=1+i^2=0$, and its two mass-squareds are $4$ and $0$ — one massive mode and the electron–neutrino skeleton, checked directly.

The three cases are collected in one table.

| mass field $\tilde{E}$ | $\tilde{E}\tilde{E}^{*}$ | mass-squareds | reading |
|---|---|---|---|
| real scalar $s e_0$ | $s^2 e_0$ | $s^2,\ s^2$ | degenerate doublet (proton–neutron) |
| Hermitian idempotent $\tilde{\Pi}$ | $\tilde{\Pi}$ | $1,\ 0$ | split doublet (electron–neutrino) |
| singular, $N(\tilde{E})=0$ | rank-deficient | $\lambda,\ 0$ | one massless mode |
| general | Hermitian, positive | $m_1^2,\ m_2^2$ | a massive doublet |

The **content of the construction, in one sentence**: the mass of a spin-$\frac{1}{2}$ doublet is not a number in this framework but a biquaternion, and the two masses of the doublet are the two eigenvalues of $\tilde{E}\tilde{E}^{*}$. That is a genuine structural statement, and it is the framework's own, not the Standard Model's.

## The Petiau Closure

### The Third Equation

The Einstein–Mayer system has a mass field $\tilde{E}$ that is put in by hand. Petiau's 1965 step, in the same feedback spirit, is to give $\tilde{E}$ an equation of its own and so **close** the system. Adding a spin-0 field $\tilde{C}$, in place of $\tilde{E}$, gives the closed system

$$
\tilde{\nabla}\tilde{A} = \tilde{B}\tilde{C},
\qquad
\tilde{\nabla}\tilde{B} = \tilde{A}\tilde{C},
\qquad
\tilde{\nabla}\tilde{C} = \tilde{A}\tilde{B}.
$$

Here $\tilde{A}$ and $\tilde{B}$ are the Lanczos spin-$\frac{1}{2}$ fields and $\tilde{C}$ is an Einstein–Mayer field of spin 0. The system is **closed** in Petiau's sense: every field on the right-hand side is one of the three, so the equations determine one another with no external parameter left, and the third equation $\tilde{\nabla}\tilde{C}=\tilde{A}\tilde{B}$ is the relation that the first two lacked. The price is that the closed system is **nonlinear** — the right-hand sides are products of two fields — and its solutions are correspondingly more constrained than those of any linear wave equation.

### The Reduction to Lanczos

The closed system reduces to the Lanczos system when the spin-0 field is a **constant**, $\tilde{C}=m e_0$. Then the first two equations read $\tilde{\nabla}\tilde{A}=\tilde{B}(m e_0)=m\tilde{B}$ and $\tilde{\nabla}\tilde{B}=\tilde{A}(m e_0)=m\tilde{A}$, which is Lanczos's pair, and the third reads $\tilde{\nabla}(m e_0)=0$, which is satisfied because $m$ is constant. Conversely the third equation forbids $\tilde{C}$ being constant in the presence of nontrivial $\tilde{A}\tilde{B}$, so a solution of the closed system is **not** an arbitrary solution of the Lanczos system: the closure is a genuine constraint.

The reduction is exact, element by element — a central scalar commutes with a biquaternion, so $\tilde{B}\tilde{C}=\tilde{C}\tilde{B}=m\tilde{B}$ — and it is checked here on random $\tilde{A}$, $\tilde{B}$. It is the sense in which the Petiau system is "the Lanczos system with the mass promoted to a field and then closed": Lanczos has one scalar mass, Einstein–Mayer has a mass biquaternion, and Petiau lets the mass field be determined by the fields it masses.

### What the Closure Costs

The nonlinearity is not a technicality. In a linear theory the solutions form a vector space and superpositions of solutions are solutions; the closed system has no such structure, and its solutions are isolated or families of a much smaller dimension. The source's observations follow from this: the **amplitude** of a wave is fixed rather than free, the **proper mass** is fixed rather than free, and the waves that solve the system are a different class of functions from the trigonometric waves of the linear theory. The next two sections give those two consequences as the source states them.

## Double-Periodic Waves

### From Trigonometric to Elliptic

The free solutions of the linear wave equation are single-periodic: $\sin(kz)$ and $\cos(kz)$, with one period. Petiau's closed system has solutions that are **double-periodic** — the **Petiau waves** — built from the elliptic functions. Instead of linear combinations of $\sin z$ and $\cos z$ the solutions are superpositions of the Jacobi elliptic functions $\mathrm{sn}(z,k)$, $\mathrm{cn}(z,k)$, $\mathrm{dn}(z,k)$, whose periods are governed by the **modulus** $k\in[0,1]$. The proper mass $\mu$ enters the argument, so that a typical wave reads $\mathrm{sn}\bigl(\mu(Et-\vec p\cdot\vec x),\,k\bigr)$.

A linear wave has one scale, its frequency, and the amplitude is free. A Petiau wave has two independent periods and a fixed amplitude, and this is the structural difference that the elliptic functions encode.

### The Modulus and the Wave–Particle Interpolation

The modulus $k$ is the parameter that carries the interpolation the source emphasises. At $k=0$ the elliptic functions degenerate to the trigonometric ones and the Petiau wave is a pure **de Broglie** plane wave; at $k=1$ they degenerate to the hyperbolic ones and the wave becomes a localised **soliton**. The intermediate values are the interpolation, and the source reads the two limits as the two faces of wave–particle duality: the same equation has a delocalised periodic solution at one end of its parameter range and a localised solitary solution at the other. This is a property of the closed system's solution class, and it is the petiau-wave counterpart of the free-particle/free-wave dichotomy.

### The Quantised Amplitude and Proper Mass

The closure constrains the constants that a linear equation would leave free. Two are singled out: the **amplitude** of the wave and the **proper mass** $\mu$ appearing in the argument. Both are **quantised** in Petiau's treatment — the nonlinearity turns the free parameters of the linear theory into a discrete set — and the source states this as the system's central output. The quantisation is of the mass itself: the closed system does not merely describe a massive particle, it fixes which masses can occur.

The article records this as the source's result and does not re-derive it. The reason for the caution is that the quantisation of $\mu$ comes from the periodic-orbit structure of the nonlinear system, whose analysis is Petiau's and is not reproduced in the corpus; what the corpus can state without overreach is the **shape** of the result, which the next section gives.

## The Hamiltonian and the Fourth Power

### The Hamiltonian

Taking one of the fields as fundamental — the source takes $\tilde{A}$ — and constructing the Hamiltonian of the closed system from its first integrals, Petiau obtained the remarkably simple form

$$
H = C_0\,\mu^4 k^2,
$$

where $k$ is the modulus of the elliptic function, $\mu$ the proper mass, and $C_0$ a constant. The Hamiltonian is quartic in the proper mass and quadratic in the modulus. Both dependences are significant: the $k^2$ is what the empirical formula of the next section will compare with, and the $\mu^4$ is the striking part.

### What the Fourth Power Means

For a single particle the total energy of the field is its **effective mass**, so the relation says that the effective mass scales as the **fourth power of the proper mass**. That is not the linear or quadratic dependence a free theory would give, and it is the source's reason for taking the construction seriously as a theory of the mass spectrum: a quartic dependence means that a small change in the mass parameter produces a large change in the observed mass, which is the kind of amplification a spectrum of very different masses would need. The source's own reading is that the fourth power is the point of contact between the closed system and the observed mass ratios — and, as the next section shows, it is at exactly this point that the argument passes from algebra to numerical coincidence.

## The Empirical Mass Formula

### Barut's Formula

The fourth-power scaling suggests a comparison with a mass formula, and the one the source uses is **Barut's leptonic formula** (1979). It is external: it is not derived from any of the systems above, it is an empirical fit, and it has the form

$$
M(N) = M_e\left(1 + \tfrac{3}{2}\,\alpha^{-1}\sum_{n=0}^{N} n^4\right),
$$

where $\alpha$ is the fine-structure constant, $M_e$ the electron mass, and $N=0,1,2,\dots$ a new quantum number counting the leptons of the chain $e,\mu,\tau,\dots$. The increment from one lepton to the next is a quantised self-energy of magnitude $\tfrac{3}{2}\alpha^{-1}M_e c^2 N^4$, proportional to the **fourth power** of the quantum number — the same fourth power that the Petiau Hamiltonian carries. Read against the data, the formula gives the following.

| $N$ | lepton | Barut's formula $(\mathrm{MeV}/c^2)$ | measured $(\mathrm{MeV}/c^2)$ |
|---|---|---|---|
| 0 | $e$ | $0.511$ | $0.511$ |
| 1 | $\mu$ | $105.55$ | $105.66$ |
| 2 | $\tau$ | $1786.1$ | $1784.1$ |
| 3 | — | $10294$ | — |
| 4 | — | $37184$ | — |

The agreement for $\mu$ and $\tau$ is at the level of a few parts in $10^3$, which for a one-parameter formula is striking. The formula predicts a fourth charged lepton at about $10.3\ \mathrm{GeV}/c^2$ and a fifth near $37\ \mathrm{GeV}/c^2$, neither of which exists in the observed spectrum — the electron, muon and tau exhaust the charged leptons, and a fourth is excluded by the $Z$-boson width. **The formula is a fit to the three known leptons and does not extrapolate to a correct fourth.**

### The Quark Extension and the Moduli Ratio

The same formula extends to the quarks by taking a different lightest mass, $M_u = M_e/7.47$; the source then obtains the quark masses $u,d,s,c,b,t$, with the heavier ones again in good numerical agreement with the ranges then quoted. The ratio

$$
\frac{M_e}{M_u} = \left[\frac{\sin(\pi/4)}{\sin(\pi/12)}\right]^2 = 7.464
$$

is the source's attempt to **explain** the number $7.47$ rather than fit it. The two values $\sin(\pi/4)$ and $\sin(\pi/12)$ are the two exceptional moduli of the elliptic functions — the **harmonic** (lemniscatic) case $k=\sin(\pi/4)=1/\sqrt2$ and the **equianharmonic** case $k=\sin(\pi/12)$ — whose poles in the complex plane have the $\pi/2$ and $\pi/3$ symmetries. Since the Petiau mass goes as $k^2$ from the Hamiltonian $H=C_0\mu^4k^2$, associating the harmonic case with the leptons and the equianharmonic case with the quarks gives the mass ratio $[\sin(\pi/4)/\sin(\pi/12)]^2$, which evaluates to $7.464$ and matches the $7.47$ the fit required. The source's own note is that this is a plausible numerical coincidence, not a derivation, and the article keeps the label: the source calls the whole comparison "very close to pure speculation".

### The Empirical Status

The three parts of this section have three different statuses, and the article keeps them apart.

- **Barut's formula** is an external empirical fit, checked against the lepton and quark data of its time. It is not derived from $\mathbb{B}$ and no framework result depends on it.
- **The fourth-power contact** between the Petiau Hamiltonian $H=C_0\mu^4k^2$ and Barut's $n^4$ increment is a numerical resemblance. Both are quartic, and the source proposes that this is not a coincidence; the corpus records the proposal and not a proof.
- **The moduli ratio** $7.464$ is arithmetic — the value is exact for the two stated moduli — but the assignment of the harmonic case to leptons and the equianharmonic case to quarks is a choice, and the match with the fitted $7.47$ is the observation the source itself flags as speculation.

What none of the three does is derive a mass from the algebra. The formula's input masses $M_e$ and $M_u$ are measured; the framework supplies the $n^4$ shape only by analogy with a quartic Hamiltonian whose constant $C_0$ it does not fix.

## What the Framework Supplies, Transcribes, and Does Not Supply

The article's accounting, collected.

**Supplied by the algebra, and verified here.** The Lanczos feedback system and its equivalence to a massive spin-$\frac{1}{2}$ equation; the promotion of the scalar mass to a biquaternion $\tilde{E}$ and the consequent eigenvalue equation $\Box\tilde{A}=\tilde{A}(\tilde{E}\tilde{E}^{*})$, $\Box\tilde{B}=\tilde{B}(\tilde{E}^{*}\tilde{E})$, whose two eigenvalues are the two masses of the doublet; the identity $\det\Phi(\tilde{E}\tilde{E}^{*})=|N(\tilde{E})|^2$, so that a singular mass field always leaves a massless mode; and the exact reduction of the closed Petiau system to Lanczos for a constant spin-0 field. These are statements about $\mathbb{B}$ and its modules, they are independent of any empirical input, and each was checked on random elements.

**Transcribed from the source.** The nonlinear character of the closed system; the double-periodic Petiau waves, their interpolation between de Broglie waves at $k=0$ and solitons at $k=1$, and the quantisation of the amplitude and the proper mass; and the Hamiltonian $H=C_0\mu^4k^2$. These are Petiau's results, reached in his non-linear wave mechanics, and the corpus records them with their provenance and without re-derivation.

**Empirical, and not a framework result.** Barut's leptonic formula and its quark extension, and the moduli ratio $7.464$ that the source proposes as their explanation. The formula fits the three known charged leptons well and extrapolates to a fourth that does not exist; the ratio is exact arithmetic offered as a plausible coincidence.

**Not supplied.** The framework derives no mass value. The algebra is scale-free — the companion article *Action, Units, and the Constants of the Biquaternion Universe* records that it fixes no scale — so a construction built on $\mathbb{B}$ cannot by itself produce the electron mass or any other. The construction's value is structural: it shows that the algebra can carry a **mass that is a field with its own equation**, whose eigenvalues are the masses of a doublet, and it makes the mass spectrum a question about a nonlinear system rather than about free Yukawa couplings. That reframing is the article's result; the mass values remain outside the framework, exactly as the standard-model agenda's ledger has it.

## Open Questions

1. **The second-order form of the closed system.** The eigenvalued form $\Box\tilde{A}=\tilde{A}(\tilde{E}\tilde{E}^{*})$ is the constant-$\tilde{E}$ reduction. For a field-valued $\tilde{E}$ or $\tilde{C}$ the derivatives act on the mass field as well, and the second-order system acquires terms the corpus has not written. The two-sided derivative the closed system needs is the subject of the companion articles on the covariant derivative and on the curvature; whether one biquaternion equation can carry it is open.

2. **The quantisation of $\mu$.** Petiau's quantisation of the proper mass comes from the periodic-orbit structure of the nonlinear system. Whether that structure can be stated inside $\mathbb{B}$ — as a condition on the elliptic modulus, on an idempotent, or on a topological invariant of the solution — is not settled, and the corpus records only the shape of the result.

3. **The $n^4$ contact.** Whether the fourth-power scaling of the Petiau Hamiltonian and the fourth-power increment of Barut's formula are two faces of one mechanism, or two unrelated quartics, is the source's speculation and remains a speculation. A derivation would have to produce the increment coefficient $\tfrac{3}{2}\alpha^{-1}$ from the closed system, which nothing in the corpus does.

4. **The moduli assignment.** The assignment of the harmonic and equianharmonic moduli to leptons and quarks is a choice. Whether the closed system selects the exceptional moduli — rather than admitting them among many — would be the test, and it is not made.

5. **The fourth lepton.** Barut's formula predicts a charged lepton near $10.3\ \mathrm{GeV}/c^2$, excluded by the $Z$ width. Any reading of the formula as a framework prediction has to explain the absence, and the source does not; the article records the formula as a fit with a wrong extrapolation.

## Summary

The biquaternion framework carries a definite line of work on mass, and this article states it with its parts separated. The **Lanczos** system $\tilde{\nabla}\tilde{A}=m\tilde{B}$, $\tilde{\nabla}\tilde{B}=m\tilde{A}$ is Maxwell's equation with a feedback, and it is strictly equivalent to a massive spin-$\frac{1}{2}$ equation; the **Einstein–Mayer** system $\tilde{\nabla}\tilde{A}=\tilde{B}\tilde{E}^{*}$, $\tilde{\nabla}\tilde{B}=\tilde{A}\tilde{E}$ promotes the scalar mass to a biquaternion $\tilde{E}$, so that the second-order equations become eigenvalue equations for the mass, with mass-squared operators $\tilde{E}\tilde{E}^{*}$ for $\tilde{A}$ and $\tilde{E}^{*}\tilde{E}$ for $\tilde{B}$; the two eigenvalues are the two masses of a doublet, equal when $\tilde{E}$ is a real scalar (the proton–neutron case), split with one massless mode when $\tilde{E}$ is a Hermitian idempotent or, more generally, a singular biquaternion (the electron–neutrino skeleton), the general case being controlled by $\det\Phi(\tilde{E}\tilde{E}^{*})=|N(\tilde{E})|^2$. The **Petiau** system $\tilde{\nabla}\tilde{A}=\tilde{B}\tilde{C}$, $\tilde{\nabla}\tilde{B}=\tilde{A}\tilde{C}$, $\tilde{\nabla}\tilde{C}=\tilde{A}\tilde{B}$ closes the system by giving the mass field its own equation, at the cost of nonlinearity, and reduces exactly to Lanczos when $\tilde{C}$ is constant. Its solutions are the **double-periodic Petiau waves**, built from elliptic functions, interpolating between de Broglie waves at modulus $k=0$ and solitons at $k=1$, with quantised amplitude and proper mass and with the quartic Hamiltonian $H=C_0\mu^4k^2$.

The empirical side is kept separate: **Barut's** formula $M(N)=M_e\bigl(1+\tfrac{3}{2}\alpha^{-1}\sum_{n=0}^{N}n^4\bigr)$ fits the lepton data to a few parts in $10^3$, matches the quartically-scaling Petiau Hamiltonian in shape, and is explained by the source as a moduli ratio $[\sin(\pi/4)/\sin(\pi/12)]^2=7.464$ between the harmonic and equianharmonic elliptic cases — a speculation the source itself labels as such, and one that predicts a fourth lepton the data exclude. The framework derives no mass value; what it supplies is a structure in which the mass is a field with an equation, the masses of a doublet are the eigenvalues of a biquaternion, and the spectrum problem becomes a nonlinear one. That is the article's result, and the mass values remain, as before, outside the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$, $\dim_{\mathbb{R}}=8$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_1e_2=e_3$ cyclic |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\tilde{\nabla},\ \tilde{\nabla}^{\natural}$ | Biquaternionic gradient and its quaternion conjugate |
| $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}=\tilde{\nabla}^{\natural}\tilde{\nabla}$ | d'Alembertian, $\partial_{ict}^2+\Delta$ (series convention) |
| $\tilde{A},\ \tilde{B}$ | Lanczos spin-$\frac{1}{2}$ fields |
| $m=mc/\hbar$ | Scalar mass parameter, inverse-length units |
| $\tilde{E}$ | Einstein–Mayer mass biquaternion |
| $\tilde{C}$ | Petiau spin-0 field, closing the system |
| $N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}=\sum_\mu Q_\mu^2$ | Biquaternion norm; $N=0$ defines the singular elements |
| $\tilde{Q}^{*}=\overline{\tilde{Q}^{\natural}}$ | Hermitian conjugation (the source's biconjugation) |
| $\tilde{E}\tilde{E}^{*},\ \tilde{E}^{*}\tilde{E}$ | Mass-squared operators of $\tilde{A}$ and $\tilde{B}$ |
| $\det\Phi(\tilde{E}\tilde{E}^{*})=|N(\tilde{E})|^2$ | Determinant identity; vanishing forces a massless mode |
| $\sigma=\tfrac12(e_0+i\hat{\nu})$ | Idempotent (nullquat), $\sigma^2=\sigma$, $N(\sigma)=0$ |
| $\Pi_\pm(\hat\mu)=\tfrac12(e_0\pm i\hat\mu)$ | Hermitian idempotents; mass eigenvalues $1,0$ |
| $e_1+ie_2$ | Singular mass field; mass-squareds $4,0$ |
| $\mathrm{sn}(z,k),\ \mathrm{cn}(z,k)$ | Jacobi elliptic functions of modulus $k$ |
| $k\in[0,1]$ | Modulus; $k=0$ de Broglie, $k=1$ soliton |
| $\mu$ | Proper mass of the Petiau field |
| $H=C_0\mu^4k^2$ | Petiau Hamiltonian (source) |
| $M(N)=M_e(1+\tfrac{3}{2}\alpha^{-1}\sum_{n=0}^{N}n^4)$ | Barut's empirical leptonic formula |
| $\alpha\approx1/137$ | Fine-structure constant |
| $[\sin(\pi/4)/\sin(\pi/12)]^2=7.464$ | Harmonic-to-equianharmonic moduli ratio (source) |
| $\langle\tilde{P},\tilde{Q}\rangle$ | the complex bilinear form, the scalar part of the complex bilinear product, $\mathrm{Sc}(\tilde{P}\tilde{Q})$ |
| $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | the complex sesquilinear form, $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ |

## Further Reading

- C. Lanczos, "Die tensoranalytischen Beziehungen der Diracschen Gleichung," *Zeitschrift für Physik* **57** (1929) 447–473, 474–483, 484–493, for the coupled biquaternion system from which Dirac's equation is derived.
- A. Einstein and W. Mayer, "Die Diracgleichung für Semivektoren," *Proceedings of the Royal Academy of Amsterdam* **36** (1933) 497–516, 615–619, for the promotion of the mass to a biquaternionic parameter.
- G. Petiau, "Sur les théories quantiques des champs associés à des modèles simples d'équations d'ondes non linéaires," *Il Nuovo Cimento* **40** (1965) 84–101, for the closed nonlinear system, the elliptic waves and the Hamiltonian.
- G. Petiau, "Sur une généralisation non linéaire de la mécanique ondulatoire et sur les propriétés des fonctions d'ondes correspondantes," *Il Nuovo Cimento* **9** (1958) 542–568, for the double-periodic waves.
- A. Gsponer and J.-P. Hurni, "Lanczos–Einstein–Petiau: From Dirac's equation to non-linear wave mechanics," in *Proceedings of the Cornelius Lanczos International Centenary Conference* (SIAM, 1994) 509–512, e-print arXiv:physics/0508036, the review from which the biquaternion form of the closed system is taken.
- A. Gsponer and J.-P. Hurni, "A non-linear field theory for the mass of the electrons and quarks," *Hadronic Journal* **19** (1996) 367–373, e-print arXiv:hep-ph/0201193, for the extension to quarks and the moduli ratio.
- A. O. Barut, "Lepton mass formula," *Physical Review Letters* **42** (1979) 1251, for the empirical formula compared here.
- Particle Data Group, *Review of Particle Properties*, *Physical Review D* **45** (1992), and later editions, for the lepton and quark mass data.
- D. F. Lawden, *Elliptic Functions and Applications* (Springer, 1989), for the Jacobi elliptic functions, the modulus and the exceptional (harmonic and equianharmonic) cases.
- S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields* (Oxford, 1995), for the wider programme in which the algebra is asked to carry physical structure beyond reformulation.
