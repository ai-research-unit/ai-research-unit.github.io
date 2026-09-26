# __Noether's Theorem in Biquaternionic Form__

## Introduction

Noether's theorem connects two things a physical theory supplies separately: its **symmetries** and its **conservation laws**. Every continuous symmetry of an action corresponds to a conserved quantity, and in a field theory to a conserved current. The theorem is not specific to any algebra, so writing it biquaternionically does not by itself produce a conservation law that was not already there. What the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ fixes is the **form** the theorem takes: which subspace the conserved objects live in, how a symmetry acts on a biquaternion-valued field, and which biquaternion expressions are the currents.

The two ends of the theorem are both already in the read list. *Relativistic Mechanics in Biquaternionic Form* gives the free-particle action

$$
S = -mc\int\sqrt{-\,d\tilde{X}\,\overline{d\tilde{X}}},
$$

whose integrand is built from the norm form of the displacement biquaternion, and it gives the conservation of the four-current in the framework form $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{J}) = 0$. This article joins the two ends: it derives the current from the symmetry of the action, for the two kinds of symmetry the framework contains.

**Two kinds of symmetry.** A relativistic action has

- **internal** symmetries, which do not move the spacetime point — here the central phase $\tilde{\Phi}\mapsto e^{i\alpha}\tilde{\Phi}$ of a complex biquaternion field, the symmetry whose localization is the gauge principle; and
- **spacetime** symmetries, the Poincaré transformations — four translations $\tilde{X}\mapsto\tilde{X}+\tilde{a}$ and six Lorentz transformations $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$. Translation invariance gives the conserved four-momentum; Lorentz invariance gives the conserved angular momentum.

The internal case produces a current biquaternion $\tilde{J}\in\mathbb{M}_-$ with $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{J})=0$, the framework form of $\partial_\mu J^\mu = 0$. The spacetime case produces an energy–momentum current and an angular-momentum bivector.

**What is established, and what is not.** Established below, and recomputed: the central-phase current of the complex biquaternion scalar field,

$$
\tilde{J} = i\left[\tilde{\Phi}^\dagger(\tilde{\nabla}\tilde{\Phi}) - (\tilde{\nabla}\tilde{\Phi}^\dagger)\tilde{\Phi}\right],
$$

lies in $\mathbb{M}_-$ and satisfies $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{J}) = i\,\mathrm{Sc}[\tilde{\Phi}^\dagger\Box\tilde{\Phi} - (\Box\tilde{\Phi}^\dagger)\tilde{\Phi}]$, which vanishes whenever the field obeys the Klein–Gordon equation; the free-particle four-momentum $\tilde{P} = m\tilde{U}$ is the Noether charge of translation invariance, and the **total** four-momentum of an isolated system is conserved; and a translation acts on a plane wave by the central phase $\exp(i\,\mathrm{Sc}(\tilde{K}\tilde{a}))$. What is standard, what is only transcribed, and what is interpretation is separated in its own section below.

**Two defects in the read list, handled rather than repeated.** First, the four-force of the parent is defined by the **proper**-time derivative, $\tilde{F} = d\tilde{P}/d\tau$, so the sum $\sum_a\tilde{F}_a$ across bodies is *not* the rate of change of the total four-momentum unless all the Lorentz factors agree; *Exercise: Four-Momentum Conservation in a Collision* reports this, and the conservation law is stated correctly below. Second, the translation of a plane wave is by the **central** phase $\exp(i\,\mathrm{Sc}(\tilde{K}\tilde{a}))$ — the form *The Poincaré Group and the Biquaternion Frame* uses — not by $\exp(\mathrm{Sc}(\tilde{K}\bar{\tilde{a}}))$, which is a positive real number and cannot be a phase. Both are recomputed here from the definitions, not recited.

**Conventions.** We use those of the read list unchanged. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_je_k = -\delta_{jk}e_0 + \varepsilon_{jkl}e_l$; and $i$ is the scalar imaginary, $i^2 = -1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian: imaginary scalar, real vector — the material sector) and $\mathbb{M}_+$ (Hermitian: real scalar, imaginary vector — the informational sector), with $\mathbb{B} = \mathbb{M}_-\oplus\mathbb{M}_+$; $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the complex scalar line, the center of the algebra. The conjugations are $\bar{\cdot}$ (quaternion), ${}^*$ (complex), ${}^\dagger = \bar{\cdot}^{\,*}$ (Hermitian), and ${}^\flat = -\dagger$ (anti-Hermitian). The biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$, its quaternion conjugate is $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_1\partial_x - e_2\partial_y - e_3\partial_z$, and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \partial_{ict}^2 + \Delta$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the **speed of light in the medium** and $c_0$ the vacuum value; $\mathbf{v}$ is reserved for particle and frame velocities. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged.

## The Action and What a Symmetry Is

**The particle.** The free relativistic particle of rest mass $m$ has the action

$$
S[\tilde{X}] = -mc\int\sqrt{-\,d\tilde{X}\,\overline{d\tilde{X}}},
\qquad d\tilde{X} = ic\,dt\,e_0 + d\mathbf{x}\in\mathbb{M}_- .
$$

Because $d\tilde{X}\,\overline{d\tilde{X}} = -c^2dt^2 + d\mathbf{x}^2 = -c^2d\tau^2$ with $\tau$ the proper time, the action is $S = -mc^2\int dt/\gamma$, and the Lagrangian in the coordinate time $t$ is

$$
L(\mathbf{v}) = -mc^2\sqrt{1-\mathbf{v}^2/c^2} = -\frac{mc^2}{\gamma},
\qquad \gamma = \frac{1}{\sqrt{1-\mathbf{v}^2/c^2}} .
$$

**The field.** The relativistic scalar field of the framework is the complex biquaternion field $\tilde{\Phi} = \phi\,e_0 \in \mathbb{C}_{\mathbb{B}}$, with $\phi$ a complex scalar function. Its action is $S[\tilde{\Phi}] = \int \mathcal{L}\,d^4x$ with the real Lagrangian density

$$
\mathcal{L} = -\,\mathrm{Sc}\!\left[(\bar{\tilde{\nabla}}\tilde{\Phi}^\dagger)(\tilde{\nabla}\tilde{\Phi})\right] - \frac{m^2c^2}{\hbar^2}\,\mathrm{Sc}\!\left[\tilde{\Phi}^\dagger\tilde{\Phi}\right].
$$

Expanding the scalar parts, $\mathcal{L} = -(\partial_{ict}\phi^*)(\partial_{ict}\phi) - \sum_k(\partial_k\phi^*)(\partial_k\phi) - (m^2c^2/\hbar^2)\phi^*\phi$, and its Euler–Lagrange equation is the biquaternion Klein–Gordon equation

$$
\left(\Box - \frac{m^2c^2}{\hbar^2}\right)\tilde{\Phi} = 0,
\qquad \Box = \tilde{\nabla}\bar{\tilde{\nabla}} .
$$

Both the action and the equation are those of the read list; $\mathcal{L}$ is exhibited only because a Noether current is read off a Lagrangian.

**What a symmetry is.** A one-parameter family $\tilde{\Phi}_\varepsilon$ with $\tilde{\Phi}_0 = \tilde{\Phi}$ is a **symmetry of the action** if $S[\tilde{\Phi}_\varepsilon] = S[\tilde{\Phi}]$ for every field configuration, and a **symmetry of the equations of motion** if it preserves the solution set. A symmetry of the action is the stronger notion, and it is the one that yields a conserved current by Noether's theorem.

**Noether's theorem, in the two forms the framework needs.** For an internal symmetry, the theorem states that there is a current biquaternion $\tilde{J} = J^0e_0 + J^k e_k$ whose divergence vanishes when the field obeys its equation:

$$
\delta S = 0 \ \text{for all fields}
\qquad\Longrightarrow\qquad
\mathrm{Sc}\!\left(\bar{\tilde{\nabla}}\tilde{J}\right) = 0 \ \text{on shell}.
$$

For a spacetime symmetry, the same construction applied to a transformation that moves the point $\tilde{X}$ yields a current carrying one index per generator: for translations the energy–momentum current, for Lorentz transformations the angular-momentum current. The two forms differ only in what the symmetry variation acts on. The general identity behind both is that the divergence of the current is the field equation contracted with the symmetry variation; it is written out for the central phase in the next section and for translations after that.

## The Current of the Central Phase

**The symmetry.** Multiplication by a central phase,

$$
\tilde{\Phi}\ \longmapsto\ e^{i\alpha}\tilde{\Phi},
\qquad \alpha\in\mathbb{R},
$$

leaves both terms of $\mathcal{L}$ unchanged, because $e^{i\alpha}$ is central and $\tilde{\Phi}^\dagger\mapsto e^{-i\alpha}\tilde{\Phi}^\dagger$: the two phase factors in $(\bar{\tilde{\nabla}}\tilde{\Phi}^\dagger)(\tilde{\nabla}\tilde{\Phi})$ cancel, and $\tilde{\Phi}^\dagger\tilde{\Phi}$ is invariant. The symmetry therefore holds for the **massive** field as well as the massless one, because the mass term depends on $\tilde{\Phi}$ only through the invariant $\tilde{\Phi}^\dagger\tilde{\Phi}$ — a fact used again below.

**The current.** For the infinitesimal variation $\delta\tilde{\Phi} = i\alpha\tilde{\Phi}$, $\delta\tilde{\Phi}^\dagger = -i\alpha\tilde{\Phi}^\dagger$, the Noether current is

$$
J^\nu = \frac{\partial\mathcal{L}}{\partial(\partial_\nu\tilde{\Phi})}\,\delta\tilde{\Phi} + \frac{\partial\mathcal{L}}{\partial(\partial_\nu\tilde{\Phi}^\dagger)}\,\delta\tilde{\Phi}^\dagger
= i\left(\phi^*\partial_\nu\phi - \phi\,\partial_\nu\phi^*\right),
$$

the second equality after using $\partial\mathcal{L}/\partial(\partial_\nu\phi) = -\partial_\nu\phi^*$ and $\partial\mathcal{L}/\partial(\partial_\nu\phi^*) = -\partial_\nu\phi$, and setting $\alpha = 1$. Packaged as a biquaternion,

$$
\boxed{\ \tilde{J} = i\left[\tilde{\Phi}^\dagger(\tilde{\nabla}\tilde{\Phi}) - (\tilde{\nabla}\tilde{\Phi}^\dagger)\tilde{\Phi}\right] = J^\nu e_\nu\ }
\qquad (\tilde{\Phi} = \phi\,e_0).
$$

**The current lies in the material sector.** The temporal component in the $ict$ basis is $J^0 = i(\phi^*\partial_{ict}\phi - \phi\,\partial_{ict}\phi^*)$, and since $\partial_{ict} = -\frac{i}{c}\partial_t$, it equals $\frac{1}{c}(\phi^*\partial_t\phi - \phi\,\partial_t\phi^*) = \frac{2i}{c}\,\mathrm{Im}(\phi^*\partial_t\phi)$, which is **purely imaginary**; the spatial components $J^k = i(\phi^*\partial_k\phi - \phi\,\partial_k\phi^*)$ are real. Hence $\tilde{J}\in\mathbb{M}_-$, with imaginary scalar part and real vector part, exactly as the four-current of relativistic mechanics. Writing $J^0 = ic\rho$ recovers the parent's convention $\tilde{J} = ic\rho\,e_0 + \mathbf{j}$.

**Conservation.** Forming the scalar part of $\bar{\tilde{\nabla}}\tilde{J}$,

$$
\mathrm{Sc}\!\left(\bar{\tilde{\nabla}}\tilde{J}\right) = \partial_{ict}J^0 + \partial_kJ^k = \partial_\mu J^\mu ,
$$

the last equality because in the $ict$ basis the time component is $i$ times its physical value, so $\partial_{ict}$ of the $ict$ component equals $\partial_0$ of the corresponding real physical component. Using the definitions and $\Box = \partial_{ict}^2 + \Delta$,

$$
\boxed{\ \mathrm{Sc}\!\left(\bar{\tilde{\nabla}}\tilde{J}\right) = i\,\mathrm{Sc}\!\left[\tilde{\Phi}^\dagger(\Box\tilde{\Phi}) - (\Box\tilde{\Phi}^\dagger)\tilde{\Phi}\right]\ }
$$

This is the Noether identity in biquaternion form: the scalar divergence of the current is the Klein–Gordon operator applied to the field, contracted with the symmetry variation. On shell, $\Box\tilde{\Phi} = (m^2c^2/\hbar^2)\tilde{\Phi}$, both terms become the same real multiple of $\tilde{\Phi}^\dagger\tilde{\Phi}$ and cancel, so

$$
\mathrm{Sc}\!\left(\bar{\tilde{\nabla}}\tilde{J}\right) = 0 \quad\text{on shell},
$$

which is the continuity equation $\partial_t\rho + \mathrm{div}\,\mathbf{j} = 0$.

**On what case was this checked?** A single plane wave is a trap: for $\tilde{\Phi} = \tilde{\Phi}_0e^{i\,\mathrm{Sc}(\tilde{K}\tilde{X})}$ the current is *constant*, so its divergence vanishes whether or not the field is on shell, and the plane wave that suggests the formula cannot test it. The conservation was therefore checked on three other cases:

- **a superposition of on-shell plane waves.** With $c = \hbar = m = 1$ and the momenta $(|\mathbf{k}|,\omega) = (0,1)$, $(\tfrac34,\tfrac54)$, $(\tfrac{5}{12},\tfrac{13}{12})$ all satisfying $\omega^2 = \mathbf{k}^2 + 1$, and amplitudes $1, \tfrac12, \tfrac13$, the current has non-constant cross terms, and $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{J})$ simplifies to **exactly zero**;
- **a standing wave**, $\tilde{\Phi} = \sin(kx)\cos(\omega t) + i\sin(kx)\sin(\omega t)$ with $\omega^2 = c^2k^2 + m^2c^4/\hbar^2$: this is on shell and is **not** a plane wave, and again $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{J})$ is **exactly zero**;
- **an off-shell field.** A two-mode field with one mode off shell gives a divergence proportional to the field equation, explicitly nonzero. The identity above was also confirmed symbolically on a generic three-mode field, off shell: the difference $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{J}) - i\,\mathrm{Sc}[\tilde{\Phi}^\dagger\Box\tilde{\Phi} - (\Box\tilde{\Phi}^\dagger)\tilde{\Phi}]$ reduces to zero identically.

The last case is the honest statement of the theorem: the current is conserved **whenever** the field equation holds; off shell it need not be, and its divergence *is* the field equation.

**Relation to the current already in the corpus.** *The Klein–Gordon Equation in Biquaternionic Form* posits the current with $\rho = \frac{i\hbar}{2mc^2}(\tilde{\Phi}^*\partial_t\tilde{\Phi} - \tilde{\Phi}\partial_t\tilde{\Phi}^*)$ and $\mathbf{j} = -\frac{i\hbar}{2m}(\tilde{\Phi}^*\nabla\tilde{\Phi} - \tilde{\Phi}\nabla\tilde{\Phi}^*)$. Comparing component by component, that current equals $-\frac{\hbar}{2m}\tilde{J}$: the Noether derivation reproduces the current the parent states, and fixes the normalization only up to the constant $-\hbar/2m$ that a current may always be multiplied by. What the derivation adds is **why** that combination is the conserved one, and that it is forced by the phase symmetry rather than chosen.

**Relation to the Maxwell source.** In the Maxwell article the source conservation is $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{R}) = 0$ with $\tilde{R} = \frac{i\rho}{\sqrt{\epsilon}}e_0 + \sqrt{\mu}\,\mathbf{J}$. Expanding, $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{R}) = \frac{1}{c\sqrt{\epsilon}}(\partial_t\rho + \mathrm{div}\,\mathbf{J})$, so the Maxwell integrability condition is the same continuity equation as the conservation of $\tilde{J}$ above. The electric four-current of the material sector is the Noether current of the central phase; the gauge freedom localized in *The Gauge Principle in Biquaternionic Form* is the localization of the symmetry that produces it.

**The mass, and where the symmetry stops.** The phase symmetry derived here holds for the massive Klein–Gordon field, and — with the parent's mass term now written in its linear, chirality-off-diagonal form $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$ — it holds for the massive Dirac field as well. A central phase passes through the linear mass term, so the current above is the conserved current of both fields, and $\partial_\mu j^\mu = 0$ on shell for each. What the mass term breaks is the **axial** symmetry, not the phase: the associated divergence identity is

$$
\partial_\mu j_5^\mu = 2im\,\bar{\tilde{\Psi}}\gamma_5\tilde{\Psi},
$$

which vanishes only in the massless limit. In the biquaternion reading the mass term is the off-diagonal coupling between the two *central* ideals of $\mathbb{B}$ — the two chiralities — so it breaks exactly the symmetry that rotates them, and not the central $U(1)$ that the algebra canonically carries. The previously recorded obstruction belonged to the retired antilinear single-field equation; the gauge principle article's corresponding section is revised on the same grounds.

## Translation Invariance and the Conserved Four-Momentum

**The particle charge.** The action $S[\tilde{X}]$ above depends on $\tilde{X}$ only through $d\tilde{X}$, so the constant shift

$$
\tilde{X}\ \longmapsto\ \tilde{X} + \tilde{a},
\qquad \tilde{a}\in\mathbb{M}_-\ \text{constant},
$$

is a symmetry of the action. The Noether charges are the momentum conjugate to $\mathbf{x}$ and the energy conjugate to $t$; computing the first from the Lagrangian,

$$
\mathbf{p} = \frac{\partial L}{\partial\mathbf{v}} = \gamma m\mathbf{v},
\qquad
E = \mathbf{p}\cdot\mathbf{v} - L = \gamma mc^2,
$$

and combining them into the four-momentum,

$$
\boxed{\ \tilde{P} = m\tilde{U} = i\frac{E}{c}\,e_0 + \mathbf{p}\ }
\qquad (\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})).
$$

The mass-shell relation $\tilde{P}\bar{\tilde{P}} = -m^2c^2$ follows. Translation invariance is thus the symmetry whose Noether charge is the four-momentum; the four-momentum is conserved for a free particle, $\dot{\tilde{P}} = 0$, because $L$ has no explicit $\tilde{X}$-dependence. As an independent check, a particle with $m = c = 1$, $\mathbf{p} = (0.6,0,0)$ and $E = \sqrt{1.36}$ was boosted by the rotor $\tilde{\Lambda} = \cosh(\psi/2) + i\sinh(\psi/2)e_1$ with $\psi = 1.2$: the norm form is $-1$ in both frames, confirming that the Noether charge transforms as a four-vector.

**The conservation law for a system, stated correctly.** For an isolated system of bodies $a$ the conserved object is the **total** four-momentum, and the correct statement is

$$
\tilde{P}_{\mathrm{tot}} = \sum_a \tilde{P}_a,
\qquad
\frac{d\tilde{P}_{\mathrm{tot}}}{dt} = 0,
$$

a vanishing **coordinate**-time derivative. The parent defines the four-force by the **proper**-time derivative of a single body, $\tilde{F}_a = d\tilde{P}_a/d\tau_a$, and since $d\tau_a = dt/\gamma_a$,

$$
\frac{d\tilde{P}_a}{dt} = \frac{1}{\gamma_a}\tilde{F}_a,
\qquad\text{so}\qquad
\sum_a \tilde{F}_a = \sum_a \gamma_a\frac{d\tilde{P}_a}{dt},
$$

which equals $d\tilde{P}_{\mathrm{tot}}/dt$ only when all the $\gamma_a$ are equal. The parent's symbol $\tilde{F}$ is a per-body proper-time rate and cannot be summed across bodies. The conservation law in terms of the parent's four-forces is therefore

$$
\sum_a \frac{1}{\gamma_a}\tilde{F}_a = \frac{d\tilde{P}_{\mathrm{tot}}}{dt} = 0,
$$

or, in the integrated form that avoids the derivative altogether, $\sum_{\mathrm{in}}\tilde{P} = \sum_{\mathrm{out}}\tilde{P}$ for a collision. The exercise reports this defect; the corrected statement above is the one to use.

**A numerical witness.** Two bodies connected by a translation-invariant interaction exchange momentum, so $d\tilde{P}_2/dt = -d\tilde{P}_1/dt = i\,e_0 + e_1$ at some instant, and their Lorentz factors differ, $\gamma_1 = 5/3$, $\gamma_2 = 5/4$. Then $d\tilde{P}_{\mathrm{tot}}/dt = 0$, but

$$
\tilde{F}_1 + \tilde{F}_2 = (\gamma_1 - \gamma_2)\frac{d\tilde{P}_1}{dt} = -\frac{5}{12}\left(i\,e_0 + e_1\right) \neq 0 .
$$

The naive sum of the parent's four-forces is not zero even though the total four-momentum is conserved. For the collision of *Exercise: Four-Momentum Conservation in a Collision* ($E_1 = 3mc^2$, equal masses, $\theta^* = 90^\circ$), the total four-momenta $\tilde{P}_{\mathrm{in}}$ and $\tilde{P}_{\mathrm{out}}$ were recomputed and agree component by component in the laboratory.

**What translation does to a plane wave.** A free field is a plane wave, and a translation acts on it by a central phase. With the series' phase convention $\tilde{\Phi} = \tilde{\Phi}_0\exp(i\,\mathrm{Sc}(\tilde{K}\tilde{X}))$, $\tilde{K}\in\mathbb{M}_-$, and $\tilde{X}\mapsto\tilde{X}+\tilde{a}$,

$$
\tilde{\Phi}\big|_{\tilde{X}+\tilde{a}} = e^{\,i\,\mathrm{Sc}(\tilde{K}\tilde{a})}\,\tilde{\Phi}\big|_{\tilde{X}},
\qquad
\tilde{\Phi}_0\ \text{constant}.
$$

The multiplier $\exp(i\,\mathrm{Sc}(\tilde{K}\tilde{a}))$ is **central and of unit modulus**, because $\mathrm{Sc}(\tilde{K}\tilde{a})$ is real: writing $\tilde{K} = i\frac{\omega}{c}e_0 + \mathbf{k}$ and $\tilde{a} = i a_0 e_0 + \mathbf{a}$,

$$
\mathrm{Sc}(\tilde{K}\tilde{a}) = -\frac{\omega a_0}{c} - \mathbf{k}\cdot\mathbf{a} .
$$

The pairing is $\mathrm{Sc}(\tilde{K}\tilde{a})$, **not** $\mathrm{Sc}(\tilde{K}\bar{\tilde{a}}) = -\frac{\omega a_0}{c} + \mathbf{k}\cdot\mathbf{a}$: the latter is real, so $\exp(\mathrm{Sc}(\tilde{K}\bar{\tilde{a}}))$ is a positive real number rather than a phase, and a translation multiplier must have unit modulus. For the values $\tilde{K} = 2i\,e_0 + 0.7e_1 - 0.3e_2 + 0.5e_3$ and $\tilde{a} = 0.4i\,e_0 + 0.25e_1 - 0.35e_2 + 0.15e_3$ (units $c = 1$) one has $\mathrm{Sc}(\tilde{K}\tilde{a}) = -1.155$ and $\mathrm{Sc}(\tilde{K}\bar{\tilde{a}}) = -0.445$; the true multiplier is $e^{-1.155i}$. This central phase is the finite, field-space form of the translation subgroup; its infinitesimal generator is the derivation $\partial_\mu$, and it is not a rotor, as *The Poincaré Group and the Biquaternion Frame* establishes.

## The Energy–Momentum of the Field

The same translation symmetry applied to the field action gives the **canonical energy–momentum**, the Noether current of spacetime translations. For the complex scalar field it is

$$
T^\mu{}_\nu = -(\partial^\mu\phi^*)\,\partial_\nu\phi - (\partial^\mu\phi)\,\partial_\nu\phi^* - \delta^\mu{}_\nu\,\mathcal{L},
$$

and translation invariance of $\mathcal{L}$ gives $\partial_\mu T^\mu{}_\nu = 0$ on shell. Its time–time component is the energy density,

$$
T^0{}_0 = |\partial_0\phi|^2 + |\nabla\phi|^2 + \frac{m^2c^2}{\hbar^2}|\phi|^2 > 0,
$$

positive, in contrast with the charge density, whose sign is not fixed. This was checked by symbolic recomputation on the on-shell superposition of three plane waves: all four divergences $\partial_\mu T^\mu{}_\nu$ simplify to zero, and $T^0{}_0$ is exactly the expression above.

**Why the framework does not write this as one biquaternion.** A symmetric rank-two tensor in four dimensions has ten independent components, while a biquaternion has four complex coefficients, that is eight real components, and $\tilde{W} = \tfrac12\tilde{F}\tilde{F}^\dagger$ carries only four of them. So no single biquaternion can be $T^{\mu\nu}$; the framework writes the translation current as a **biquaternion bilinear**, one basis element for each index. *Exercise: The Electromagnetic Energy–Momentum Tensor* constructs exactly this for the Maxwell field, $T^\mu{}_\nu = \tfrac12\mathrm{Sc}(\tilde{F}\mathcal{E}_\mu\tilde{F}^\dagger\mathcal{E}_\nu)$, and shows that the four-component object is its time row. The framework's energy–momentum biquaternion is therefore not the whole Noether current of translations; it is the energy–flux part of it.

**The Maxwell case in the corpus form.** For the electromagnetic field the corpus's object is $\tilde{W} = \tfrac12\tilde{F}\tilde{F}^\dagger = W\,e_0 + \frac{i}{c}\mathbf{S}\in\mathbb{M}_+$, with $W$ the energy density and $\mathbf{S} = \mathbf{E}\times\mathbf{H}$ the Poynting vector, and the conservation law is $\tilde{\nabla}\tilde{W} = -\tilde{P}$ with $\tilde{P}$ the power–force density; the source-free case is $\tilde{\nabla}\tilde{W} = 0$. Its scalar part is the Poynting theorem, and the sign structure is the one the energy–momentum exercise verifies: the Hermitian form passes the test, while the real form $W + \frac{1}{c}\mathbf{S}$ does not, by a factor $i$ on the Poynting part. Read as a Noether statement, $\tilde{\nabla}\tilde{W} = -\tilde{P}$ says that the translation current of the Maxwell field is conserved up to the work done on the charges — the source is present, so the field alone is not closed.

**A caution on the $ict$ convention.** The energy density is not $\mathcal{L}$ and is not obtained from $\mathcal{L}$ by a flat sum: in the $ict$ convention the time direction carries the sign that the metric would carry, and mixing the two conventions produces the wrong sign on the time derivative. The canonical tensor above is written with the physical index positions, where $T^0{}_0$ is manifestly positive; the biquaternion packaging must be read through the same convention. This is the same caution the energy–momentum exercise records for the trace.

## Lorentz Invariance and the Angular-Momentum Bivector

Lorentz invariance is a spacetime symmetry like translation, and it has a Noether current too. For a free particle the conserved quantity is the antisymmetric pair

$$
L^{\mu\nu} = x^\mu p^\nu - x^\nu p^\mu,
\qquad
\frac{dL^{\mu\nu}}{d\tau} = p^\mu\frac{dx^\nu}{d\tau} - p^\nu\frac{dx^\mu}{d\tau} = \frac{p^\mu p^\nu - p^\nu p^\mu}{m} = 0,
$$

using $dx^\mu/d\tau = p^\mu/m$; the conservation of the six independent components is the conservation of angular momentum and of the boost charges. In the biquaternion algebra the antisymmetric pair is a **bivector**, the same representation the field strength occupies: writing

$$
\tilde{L} = \tfrac12\sum_{\mu,\nu}L^{\mu\nu}\,\bar{e}_\mu e_\nu,
$$

the angular momentum of a free particle is a single biquaternion. This is the same construction by which $\tilde{F} = \mathrm{Vect}(\bar{\tilde{\nabla}}\tilde{A}) = \tfrac12\sum_{\mu\nu}F_{\mu\nu}\bar{e}_\mu e_\nu$ packages the antisymmetric field strength, and the Lorentz generators themselves are bivectors.

**What does not carry over as a single biquaternion.** For a field, the Noether current of Lorentz invariance is a rank-three object, $L^{\mu\nu\rho} = x^\nu T^{\mu\rho} - x^\rho T^{\mu\nu} + S^{\mu\nu\rho}$, whose conservation $\partial_\mu L^{\mu\nu\rho} = 0$ expresses the symmetry of the energy–momentum tensor together with the conservation of spin. Being rank three, it is not a biquaternion and not even a single bilinear; the orbital and spin pieces separate, with the spin term vanishing for the classical scalar field. The particle bivector $\tilde{L}$ above is the finite-dimensional case where the rank-two object *is* the whole story.

## What Is Inherited, What Is Added, What Is Interpretation

**Inherited and unchanged.** The action, the four-momentum, the four-current and its conservation $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{J}) = 0$, the algebra, the gradient, the sectors, and the trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ are those of the read list. No symbol is renamed or rederived.

**Added by this article.** The derivation of the central-phase current $\tilde{J} = i[\tilde{\Phi}^\dagger\tilde{\nabla}\tilde{\Phi} - (\tilde{\nabla}\tilde{\Phi}^\dagger)\tilde{\Phi}]$ from the phase symmetry of the field action, and its conservation identity; the identification of the free-particle four-momentum as the Noether charge of translation invariance, with the corrected multi-body statement; the explicit translation multiplier $\exp(i\,\mathrm{Sc}(\tilde{K}\tilde{a}))$; the energy–momentum current and its packaging; and the angular-momentum bivector. These are transcriptions of the standard theorem into the algebra, with the subspace assignments the algebra supplies, not new physics.

**Only transcribed.** Noether's theorem itself is standard; the algebra does not produce a symmetry that the action did not already have, nor a conservation law beyond those the symmetries give. The framework supplies the home of each conserved object — the current in $\mathbb{M}_-$, the energy–momentum in the bilinear and its time row in $\mathbb{M}_+$ for Maxwell, the angular momentum in the bivector — and it makes the divergence identities compact. It does not supply the symmetries, the coupling constants, or the masses.

**Interpretation.** Reading the conserved currents as the physical four-current and energy–momentum is the standard reading, not an extra postulate; the biquaternion packaging is a representation-theoretic statement about which subspace carries which object, and it is exact. What remains interpretation is the physical hypothesis attached to the two sectors, which is the program's, not this article's.

## Open Questions

1. **The biquaternion form of the full translation current.** The energy–momentum tensor is rank two and cannot be one biquaternion. Is there a natural biquaternion-bilinear expression for the canonical $T^\mu{}_\nu$ of a general biquaternion field, beyond the Maxwell case constructed in the energy–momentum exercise?

2. **Spin and the angular momentum of fields.** The rank-three Lorentz current carries a spin term. Can the spin density of a biquaternion field be written as a biquaternion expression, and how does it relate to the bivector representation of angular momentum?

3. **Scale and conformal symmetry.** The massless Klein–Gordon and Maxwell actions have more symmetries than the Poincaré group. Do they have biquaternion Noether currents, and does the tracelessness of the electromagnetic energy–momentum tensor — established in the energy–momentum exercise — express one of them?

4. **The axial current and the two central ideals.** With the parent's linear mass term the vector phase current is conserved for the massive field, so the open question is the axial one. The divergence identity $\partial_\mu j_5^\mu = 2im\,\bar{\tilde{\Psi}}\gamma_5\tilde{\Psi}$ holds for the linear mass term, and its biquaternion reading is that the mass couples the two central ideals of $\mathbb{B}$ off-diagonally. Is there a biquaternion Noether derivation of that identity — the axial current as the Noether current of the chirality rotation — and does the central-element structure supply anything analogous to the would-be Goldstone statement?

5. **The current of the complexified theory.** In the complexified biquaternion theory of the Maxwell article, the source and potential are fully complex. Does the central-phase current acquire components outside $\mathbb{M}_-$, and are they conserved?

6. **Empirical content.** As everywhere in the framework, the currents derived here are the standard ones in new notation. Whether the biquaternion packaging imposes any constraint that the four-vector formulation does not is not established here.

## Summary

Noether's theorem in biquaternionic form joins the action of *Relativistic Mechanics in Biquaternionic Form* to the conserved current of the same article. The theorem has two forms. For an **internal** symmetry, that of the central phase $\tilde{\Phi}\mapsto e^{i\alpha}\tilde{\Phi}$ of the complex biquaternion scalar field, the derived current is

$$
\tilde{J} = i\left[\tilde{\Phi}^\dagger(\tilde{\nabla}\tilde{\Phi}) - (\tilde{\nabla}\tilde{\Phi}^\dagger)\tilde{\Phi}\right] = J^\nu e_\nu,
\qquad J^\nu = i\left(\phi^*\partial_\nu\phi - \phi\,\partial_\nu\phi^*\right),
$$

which lies in $\mathbb{M}_-$ and satisfies the Noether identity

$$
\mathrm{Sc}\!\left(\bar{\tilde{\nabla}}\tilde{J}\right) = i\,\mathrm{Sc}\!\left[\tilde{\Phi}^\dagger(\Box\tilde{\Phi}) - (\Box\tilde{\Phi}^\dagger)\tilde{\Phi}\right],
$$

zero whenever the field is on shell. This is the framework form of $\partial_\mu J^\mu = 0$; it reproduces the current the Klein–Gordon article posits, up to the conventional constant $-\hbar/2m$, and its expansion at the Maxwell source is the charge-conservation condition $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{R}) = 0$.

For a **spacetime** symmetry, translation invariance gives the four-momentum

$$
\tilde{P} = m\tilde{U} = i\frac{E}{c}e_0 + \mathbf{p},
\qquad E = \gamma mc^2,\quad \mathbf{p} = \gamma m\mathbf{v},
$$

as the Noether charge, conserved for a free particle. The conservation law for a system is the vanishing of the **coordinate**-time derivative of the total, $d\tilde{P}_{\mathrm{tot}}/dt = 0$; the parent's proper-time four-force cannot be summed across bodies, and the correct form is $\sum_a\tilde{F}_a/\gamma_a = 0$, or the integrated $\sum_{\mathrm{in}}\tilde{P} = \sum_{\mathrm{out}}\tilde{P}$. A translation acts on a plane wave by the central unit-modulus phase $\exp(i\,\mathrm{Sc}(\tilde{K}\tilde{a}))$, with $\mathrm{Sc}(\tilde{K}\tilde{a}) = -\frac{\omega a_0}{c} - \mathbf{k}\cdot\mathbf{a}$.

The field translation current is the canonical energy–momentum, $\partial_\mu T^\mu{}_\nu = 0$ on shell with positive energy density $T^0{}_0 = |\partial_0\phi|^2 + |\nabla\phi|^2 + \frac{m^2c^2}{\hbar^2}|\phi|^2$. Rank two cannot be one biquaternion, so the framework packages it bilinearly; the Maxwell object $\tilde{W} = \tfrac12\tilde{F}\tilde{F}^\dagger$ with $\tilde{\nabla}\tilde{W} = -\tilde{P}$ is its time row. Lorentz invariance gives the angular-momentum bivector $\tilde{L} = \tfrac12\sum L^{\mu\nu}\bar{e}_\mu e_\nu$, with the rank-three field current reduced to the rank-two particle bivector only when the spin term vanishes. The theorem is standard; the algebra supplies the home of each conserved object and the compact form of its divergence, and it supplies no conservation law the symmetries did not already give.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}, \mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ | Real-quaternion subspace; complex scalar line (the center) |
| $\tilde{\nabla} = e_0\partial_{ict} + e_k\partial_k$ | Biquaternionic gradient |
| $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_k\partial_k$ | Quaternion-conjugate gradient |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \partial_{ict}^2 + \Delta$ | d'Alembertian |
| $S = -mc\int\sqrt{-d\tilde{X}\,\overline{d\tilde{X}}}$ | Free-particle action |
| $L = -mc^2\sqrt{1-\mathbf{v}^2/c^2}$ | Free-particle Lagrangian |
| $\tilde{X} = ic\,t\,e_0 + \mathbf{x}$ | Four-position, in $\mathbb{M}_-$ |
| $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$ | Four-velocity, $\tilde{U}\bar{\tilde{U}} = -c^2$ |
| $\tilde{P} = m\tilde{U} = iE/c\,e_0 + \mathbf{p}$ | Four-momentum, Noether charge of translation |
| $\tilde{F}_a = d\tilde{P}_a/d\tau_a$ | Four-force (proper-time derivative; not summable) |
| $\tilde{a}\in\mathbb{M}_-$ | Constant translation (displacement) |
| $\tilde{\Phi} = \phi\,e_0\in\mathbb{C}_{\mathbb{B}}$ | Complex biquaternion scalar field |
| $\mathcal{L} = -\mathrm{Sc}[(\bar{\tilde{\nabla}}\tilde{\Phi}^\dagger)(\tilde{\nabla}\tilde{\Phi})] - \frac{m^2c^2}{\hbar^2}\mathrm{Sc}[\tilde{\Phi}^\dagger\tilde{\Phi}]$ | Field Lagrangian density |
| $\tilde{J} = i[\tilde{\Phi}^\dagger\tilde{\nabla}\tilde{\Phi} - (\tilde{\nabla}\tilde{\Phi}^\dagger)\tilde{\Phi}]$ | Central-phase Noether current, in $\mathbb{M}_-$ |
| $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{J}) = 0$ | Framework form of current conservation |
| $\tilde{R} = \frac{i\rho}{\sqrt{\epsilon}}e_0 + \sqrt{\mu}\,\mathbf{J}$ | Maxwell source; $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{R}) = 0$ is charge conservation |
| $T^\mu{}_\nu$ | Canonical energy–momentum of the field |
| $\tilde{W} = \tfrac12\tilde{F}\tilde{F}^\dagger = W\,e_0 + \frac{i}{c}\mathbf{S}$ | Maxwell energy–momentum (time row), in $\mathbb{M}_+$ |
| $L^{\mu\nu} = x^\mu p^\nu - x^\nu p^\mu$, $\tilde{L} = \tfrac12\sum L^{\mu\nu}\bar{e}_\mu e_\nu$ | Angular momentum and its bivector |
| $\tilde{K} = i\frac{\omega}{c}e_0 + \mathbf{k}$ | Four-wavevector, in $\mathbb{M}_-$ |
| $\exp(i\,\mathrm{Sc}(\tilde{K}\tilde{a}))$ | Central translation multiplier on a plane wave |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula of the informational sector |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- *Relativistic Mechanics in Biquaternionic Form* — the action and the conserved current this article starts from.
- *The Klein–Gordon Equation in Biquaternionic Form* — the field, its Lagrangian form, and the current the Noether derivation reproduces.
- *The Poincaré Group and the Biquaternion Frame* — the symmetry group, and the corrected central translation phase.
- *Exercise: Four-Momentum Conservation in a Collision* — the total four-momentum of an isolated system, and the report of the proper-time four-force defect.
- *Exercise: The Electromagnetic Energy–Momentum Tensor* — the rank-two translation current and why one biquaternion cannot carry it.
- *Maxwell's Equations in the Biquaternionic Formulation* — the source conservation and the energy–momentum biquaternion $\tilde{W}$.
- *The Field-Strength Biquaternion and Its Invariants* — the bivector representation used for the angular momentum.
- *Angular Momentum and Spin in Biquaternionic Form* — the angular-momentum algebra and the spin operators.
- *The Gauge Principle in Biquaternionic Form* — the localization of the central phase whose global current is derived here.
- *The Covariant Derivative and Gauge Connection in Biquaternionic Form* — the connection forced by localizing the same symmetry.
- *The Lorentz Transformation as a Biquaternionic Rotation* — the rotor whose conjugation carries the four-momentum between frames.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* and *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* — the two sectors that house the conserved objects.
- *Introduction to the Biquaternion Universe* — the algebra, its conjugations, and the local complex structure.
