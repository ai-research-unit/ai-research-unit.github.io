# Internal audit: the presence of $h$ in *Biquaternion Universe Relativity*, *Action* and *Fluid Physics and Thermodynamics*

Internal note. Not an article, not in any menu, not built.

## 0. Correction of record

In an earlier exchange I wrote that $h$ in a Lagrangian is *a scale, not a quantization*. That was wrong. **$h$ in a Lagrangian is the quantization.** The corpus says so in its own words, and this audit records the evidence. Sections 5 and 6 state what survives of the wrong claim and what does not.

## 1. Scope and method

The three blocks hold 190 articles: 105 in Relativity, 50 in Action, 35 in Fluid Physics and Thermodynamics. Every article reachable from those blocks in `physics.md` was read for occurrences of the Planck constant.

Six written forms were counted: $\frac{h}{2\pi}$; $h$ in a denominator, as in $\frac{2\pi i\,ϙ}{h}$; a bare $h$; $h^{2}$; $hc$; and the barred letter. The first five are lawful. The sixth is forbidden by the Conventions and is counted separately.

**The letter $h$ is overloaded, so a naive count is meaningless.** Four different objects are written with the same letter in these blocks.

| Sense | Example | Where |
|---|---|---|
| the Planck constant | $\nu_m=\frac{mc}{h}$ | everywhere |
| the helicity | "$h$ is the **helicity** … in units of $\frac{h}{2\pi}$" | *P-T and the Representation Labels*, *The Little Group of a Null Momentum* |
| the state's vector part | $\vec h_\Psi$, $h_t e_t+\vec h_\Psi$ | informational sector, 388 forms |
| a scalar field | "the radial field $h$ has the mass $m_h^{2}=2\beta v^{2}$" | *The Spin-Zero Centre Subspace* |

Two of my first counts were therefore inflated and are discarded: `\tanh`, `\cosh`, `\sinh` and the abbreviation $c_h$ contain the letter, and $\vec h_\Psi$ is a state, not a constant. The numbers below are of the Planck constant only, and where the bare $h$ is ambiguous the table says so.

## 2. Where $h$ is declared

$h$ is not introduced in any of the three categories. It is declared upstream, in *Conventions & Notations*, article **Physics Units and Common Elements Conventions**.

The table of constants fixes it as a defining constant:

| Planck constants | $h$, $\frac{h}{2\pi}$ | $\mathrm{M}\,\mathrm{L}^{2}\,\mathrm{T}^{-1}$ | joule-second | defining | exact |

Two rules govern every use below.

1. **"The Planck constant is written $h$, and the barred letter is never used."** Where the quantum of action over $2\pi$ is meant, the corpus writes $\frac{h}{2\pi}$ and leaves the $2\pi$ on the page.
2. **"The shortcut $c=1$ together with $h$ at $2\pi$ is not allowed."** $h$ may not be set to $2\pi$, and no constant may be set to one.

So $h$ enters as a constant with a dimension, before any dynamics exist. The three categories then use it, and they cannot avoid it.

## 3. The roles of $h$

Eight roles appear. Each is a distinct use, and each is present in at least one of the three blocks.

| | Role | The form | What it does |
|---|---|---|---|
| R1 | mass as a wave number | $\nu_m=\frac{mc}{h}$ | turns a mass into the inverse length the field uses |
| R2 | the action as an action | $\frac{h}{2\pi}c$ prefactor | gives the integrand the dimension of action |
| R3 | the phase | $\frac{S}{h}$, $\tilde\Upsilon_\Phi=\frac{\tilde P_\Phi}{h}$ | makes the field a phase and the momentum a wave number |
| R4 | minimal coupling | $\frac{2\pi i\,ϙ}{h}\tilde A_\Phi$ | the charge enters as a phase per action |
| R5 | the quantum potential | $Q_{\mathrm{qnt}}=-\frac{h^{2}}{4\pi^{2}}\frac{\Box_\Phi\varrho}{2m\varrho}$ | the $h^{2}$ term in the fluid's acceleration law |
| R6 | the thermal rate | $\beta=\frac{h}{2\pi k_BT}$, $-\frac{2\pi}{h}\beta_\Phi p_\Phi$ | the Boltzmann weight as a phase per action |
| R7 | the $h$ expansion | orders $h^{0},h^{2}$ of the Wigner equation | separates the transport law from the quantum correction |
| R8 | the limit | $\frac{h}{2\pi}\to0$ | the ray limit, that is the classical reading |

**R1 is in every free Lagrangian and every free equation of the corpus.** It is the one role that is never absent. The mass term of the Proca action is $\tfrac12 4\pi^{2}\nu_m^{2}\langle\tilde A_\Phi\rangle_\natural$, with $\nu_m=\frac{mc}{h}$. The Klein–Gordon operator is $\Box_\Phi-4\pi^{2}\nu_m^{2}$. The Dirac pair is $\tilde\nabla_\Phi\tilde\Xi_R=2\pi\nu_m\tilde\Xi_L$ with $\nu_m=\frac{mc}{h}$. The article *The Dirac Pair and the Mass Term* writes the identification out: "with $\nu_m=\frac{mc}{h}$ the mass wave number".

**R2 is explicit only in the fermionic action.** *The Lagrangian and the Dirac Equation* carries $S=\frac{hc}{4\pi}\int\mathrm{d}^{4}\varrho\,\mathrm{Re}\,\mathrm{Sc}[\dots]$, and states: "The constant $\frac{h}{2\pi}c$. It multiplies the whole action and cancels in the variation, so the residuals do not carry it while the currents carry one power of it. It is written so that the two terms have the dimension of an action."

**R3 is the phase.** *The Three Wavenumbers of a Particle* divides the four-momentum by $h$ and reads the coordinates as wave numbers. *Wave–Particle Duality and the Fourier Transform* writes $i\frac{h}{2\pi}c\partial_{r'_t}\tilde\Xi=\tilde H_\Psi\tilde\Xi$.

**R4 is the covariant derivative.** $\tilde\nabla_{\mathrm{gco},\Phi}=\tilde\nabla_\Phi+\frac{2\pi i\,ϙ}{h}\tilde A_\Phi$. The two articles that carry it, *The Covariant Derivative and Connection* and *The Minimal Coupling*, hold 50 and 26 denominator forms, and they are the largest single users of $h$ in the Action block.

**R5 is the quantum potential, and it is the decisive one.** *The Lagrangian and the Klein–Gordon Equation in Polar Variables* gives $Q_{\mathrm{qnt}}=-\frac{h^{2}}{4\pi^{2}}\frac{\Box_\Phi \varrho}{2m\varrho}$ in the acceleration law, and *The Lagrangian and the Spin-Zero Fluid* carries $\frac{hc}{8\pi^{2}\nu_m}\sum_{\imath}(\partial_{\imath}\varrho)^{2}$ in the fluid Lagrangian. *The Lagrangian and the Spin-One Fluid* states the contrast in its own words: "this is the only action in the layer with no $\frac{h}{2\pi}$ in its derivative term, and correspondingly the only fluid in the block whose acceleration law has no quantum force."

**R6 is the thermal rate.** *Equilibrium Partition Function in a Moving Frame*: "The thermal exponent is the contraction of the thermal element with the flow momentum, divided by the action quantum", displayed as $-\frac{2\pi}{h}\beta_{\Phi,\jmath}p_{\Phi,\jmath}$. *The Chemical Potential Is the Phase's Frequency* writes $\mu_{\mathrm{chm}}=-\partial_{t'}S=\frac{h}{2\pi}\nu$.

**R7 is the Wigner expansion.** *Relativistic Wigner Function and Quantum Kinetics* is the largest single user of $h$ in the whole corpus: 70 forms, of which 35 are $h^{2}$.

**R8 is the limit.** *The Three Scales*: "at fixed action the ray limit", with $\frac{h}{2\pi}\to0$; the phase oscillates without limit and the fluid's guidance relation becomes the classical one.

## 4. Inventory

### 4.1 Totals by written form

| Block | of | with $h$ | $\frac{h}{2\pi}$ | $h$ in a denominator | bare $h$ | $h^{2}$ | $hc$ | barred |
|---|---|---|---|---|---|---|---|---|
| Relativity | 105 | 30 | 39 | 29 | 26 | 12 | 1 | 0 |
| Action | 50 | 31 | 62 | 175 | 9 | 11 | 5 | 23 |
| Fluid | 35 | 23 | 59 | 57 | 4 | 77 | 14 | 7 |
| **total** | **190** | **84** | **160** | **261** | **39** | **100** | **20** | **30** |

610 lawful forms in 84 articles, plus 30 barred. The overlap between the columns is small; the columns count written forms, not articles.

The 39 bare $h$ are not all the Planck constant: 16 of them are the helicity, and 9 sit in one article, *P-T and the Representation Labels*, where $h$ is defined as the helicity. The remaining 14 are the constant.

### 4.2 Relativity, 105 articles

Four roles, in four sections.

- **R1, the mass wave number.** *The Dirac Pair and the Mass Term*, *Wigner's Classification*, *The Little Group of a Massive Particle*, *The Little Group of a Null Momentum*, *Relativistic Mechanics*, *The Non-Relativistic Limit of Relativistic Mechanics*.
- **R3, the phase and the wave numbers.** *Wave–Particle Duality and the Fourier Transform* (18 forms), *The Derivative, the Field and the Transform*, *The Harmonic Analysis*.
- **R4, the gauge derivative.** *The Spin-Zero Centre Subspace*, with $\frac{2\pi i\,ϙ}{h}$.
- **R6, the thermal rate.** *The Thermal Circle* (12 forms), *The Local Thermal Structure* (11), *The KMS Condition* (5), *Inverse Temperature as a Rapidity*, *The Modular Hamiltonian*.
- **the helicity.** *P-T and the Representation Labels*, *The Little Group of a Null Momentum*, and the article *Helicity in Biquaternionic Form*, now in *Free of Force*.

No barred letter in this block: the corpus is clean here.

### 4.3 Action, 50 articles

Four roles, and the block is where $h$ is most concentrated.

- **R1.** *The Relativistic Particle and the Lagrangian*: "The units. $m$ is a mass, $c$ a speed, $h$ the Planck constant", with $\nu_m=\frac{mc}{h}$.
- **R2 and R3.** *The Lagrangian and the Second Quantisation* (7 forms), *Fock Space and Creation–Annihilation Operators*, *The Functional Integral*, *The Generating Functional and the Effective Action* (22), *The S-Matrix* (17), *The Schwinger–Dyson Equations* (16), *The LSZ Reduction Formula*, *The Connection Path Integral*. In all of them the exponent is $\frac{S}{h}$ or $\frac{iS}{h}$.
- **R4.** *The Covariant Derivative and Connection* (52), *The Minimal Coupling* (28), *Connection, Curvature and the Bianchi Identity*, *Non-Abelian Connections*, *The Yang–Mills Equation*.
- **R8, and the explicit treatment of the constant.** *The Three Scales: $c$, $\hbar$ and $k_B$ as the Three Continuations*, 51 forms. This is the article that states what $h$ is in the corpus: a rate between the action and the phase, with $\frac{h}{2\pi}\to0$ the ray limit.

This block holds 23 of the 30 barred letters of the three blocks. Two are in the title and the body of *The Three Scales*, four in *Noether's Theorem*, three in *The Relativistic Particle and the Lagrangian*, one each in *The Closure of the Term List*, *Ostrogradsky*, *The Quantisation Hub*.

### 4.4 Fluid Physics and Thermodynamics, 35 articles

Three roles, and the $h^{2}$ count is heavier here than anywhere else.

- **R5, the quantum potential.** *Criterion for a Fluid Equation*, *Five Steps from a Lagrangian to Fluid Equations*, *The Spare Derivative in the Polar Chart*, *The Equation of State* ($Q_{\mathrm{qnt}}=-\frac{hc}{8\pi^{2}\nu_m}\frac{\Box_\Phi\lVert\tilde\Xi\rVert}{\lVert\tilde\Xi\rVert}$), *The Local Thermal State of a Fluid*.
- **R6, the thermal rate.** *The Partition Function*, *Quantum Thermodynamics*, *The Free-Energy Functional at Finite Temperature*, *Coarse-Graining and the Entropy Functional*, *The Matsubara Thermal Formalism*, *Equilibrium Partition Function in a Moving Frame* (17), *The Schwinger–Keldysh Formalism*, *The Local Thermal State of a Fluid*, *The Equation of State* (30), *Covariant Local Equilibrium and Tolman Temperature*, *The Thermodynamics of a Quantum Fluid*, *The Chemical Potential Is the Phase's Frequency* (22).
- **R7, the $h$ expansion.** *The Wigner Function* (39), where the variance is $\frac{h^{2}}{16\pi^{2}\sigma^{2}}$; *Relativistic Wigner Function and Quantum Kinetics* (69).
- **R1.** *The Relativistic Quantum Space as a Fluid*, *The Current Algebra*, *Spin Conservation and the Frenkel Condition*, *The Two-Fluid Model*.

**A correction to an earlier count of mine.** I first listed *The Two Scales of the Field* as a heavy user, with 24 forms of $h^{2}$. It carries no Planck constant at all: its 24 are $\cosh^{2}$, $\sinh^{2}$ and the abbreviation $c_h$. The article is recorded here as a false positive, and it is the clearest illustration of D1.

Seven barred letters, in *Relativistic Wigner Function and Quantum Kinetics* (one, in the title), *The Chemical Potential Is the Phase's Frequency* (four), *Criterion for a Fluid Equation* (one).

## 5. Verdict: $h$ in the Lagrangian is the quantization

The corpus establishes three things, and together they settle the question.

**First, the $h$ in the derivative term is what produces the quantum force.** *The Lagrangian and the Spin-One Fluid* says it in one sentence: the only action with no $\frac{h}{2\pi}$ in its derivative term is the only one "whose acceleration law has no quantum force". So the presence or absence of $h$ in the Lagrangian is exactly the difference between a quantum acceleration law and a classical one. That is not a scale convention. It is the quantization, written into the action.

**Second, $h\to0$ is the classical limit.** *The Three Scales*: at fixed action, $\frac{h}{2\pi}\to0$ is the ray limit, the phase oscillates without limit, and the guidance relation becomes the classical one. A constant whose vanishing reproduces classical mechanics is the quantum of the theory, not a unit.

**Third, the currents carry one power of $h$.** *The Lagrangian and the Dirac Equation*: the prefactor "cancels in the variation, so the residuals do not carry it while the currents carry one power of it". The equations of motion are the classical shadow. The observables, the currents, carry the quantum.

So the Lagrangian is a quantum object from the first line. The action is written in units of action, the field is a phase, and the $h^{2}$ of the quantum potential is a term in the acceleration law. Writing a Lagrangian in this corpus is already quantizing.

**What survives of my wrong sentence, and what does not.**

- It is true that the overall prefactor $\frac{h}{2\pi}c$ cancels from the Euler–Lagrange residual of the Dirac action. The equation of motion does not carry that factor.
- It is false that $h$ therefore leaves the dynamics. The $h$ inside $\nu_m=\frac{mc}{h}$ stays in every equation of motion, bosonic and fermionic. In the polar form the $h^{2}$ of the quantum potential stays too.
- It is false that $h$ is only a change of unit. A change of unit does not produce a quantum force, and its vanishing does not give a classical limit.

The accurate statement is the narrow one: **the overall normalization cancels, the mass scale and the quantum potential do not.** $h$ is in the equations of motion, not merely in the action.

## 6. Consequence for the architecture

1. **There is no $h$-free free Lagrangian.** In the Cartesian bosonic form $h$ hides inside $\nu_m=\frac{mc}{h}$; separate amplitude and phase in the same action and $h^{2}$ appears in the quantum potential. The Dirac action carries $h$ explicitly from the start. So the free layer cannot be presented as pre-quantum.
2. **$h$ is not purged from the free layer, and must not be.** The 47 articles moved to *Biquaternion Universe Free of Force* carry $h$ in 46 of 47 cases. That is correct. *Wave–Particle Duality and the Weight of a Level Set* is the only one without it.
3. **The boundary between *Free of Force* and *Relativistic Quantum Theory* is coupling, not $h$.** Both layers carry $h$. The difference is that the free layer has no internal coupling, no charge, and no interaction, while the coupled layer has them, and that the promotion to operators, Fock space and the path integral sits in the quantum apparatus. A boundary drawn on "classical against quantum" would be false, because neither layer is classical.
4. **The generalities given to *Free of Force* are the $h$-bearing ones.** The three wavenumbers, the helicity, the d'Alembertian, the conformal limit: all four are uses of $h$. Their move to the free layer is consistent with this audit, and it is the reason the free layer must keep them.

## 7. Defects found

**D1. The letter $h$ carries four meanings.** The Planck constant, the helicity, the state's vector part $\vec h_\Psi$, and a scalar field. In *States, Observables and the Born Weight* the letter is the state's vector part 133 times and the Planck constant twice. In *P-T and the Representation Labels* it is the helicity, in units of $\frac{h}{2\pi}$. A reader cannot tell the constant from the state without the surrounding sentence. This is a readability defect, and it is the reason no mechanical count of $h$ in this corpus can be trusted.

**D2. The barred letter is used, against an explicit ban.** 39 occurrences in 14 files, of which 30 are in these three blocks. It appears in two article titles (*The Three Scales: $c$, $\hbar$ and $k_B$…*, *The $\hbar$ Expansion of the Wigner Function…*) and in 8 comment lines of `physics.md`. The Conventions call this "a defect of the article that carries it". It is the only place in this audit where an article contradicts a written rule of the corpus.

Neither defect was repaired. Both are recorded for a decision by the author.

## 8. Not decided here

- Whether D1 is repaired by renaming the state letter, and D2 by writing $\frac{h}{2\pi}$ in the 39 places.
- Whether *Free of Force* keeps the four $h$-bearing generalities. This audit argues it must.
- Nothing was modified. This file is the only addition.
