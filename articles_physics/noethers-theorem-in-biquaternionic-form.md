# __Noether's Theorem in Biquaternionic Form__

## Introduction

Noether's theorem connects two things a physical theory supplies separately: its **symmetries** and its **conservation laws**. Every continuous symmetry of an action corresponds to a conserved quantity, and in a field theory to a conserved current. The theorem is not specific to any algebra, so writing it biquaternionically does not by itself produce a conservation law that was not already there. What the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ fixes is the **form** the theorem takes: which subspace the conserved objects live in, how a symmetry acts on a biquaternion-valued field, and which biquaternion expressions are the currents.

The two ends of the theorem are both already in the read list. *Relativistic Mechanics in Biquaternionic Form* gives the free-particle action

$$
S = -mc\int\sqrt{-\,d\tilde{R}\,d\tilde{R}^{\natural}},
$$

whose integrand is built from the biquaternion norm of the displacement biquaternion, and it gives the conservation of the four-current in the framework form $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J}) = 0$. This article joins the two ends: it derives the current from the symmetry of the action, for the two kinds of symmetry the framework contains.

**Two kinds of symmetry.** A relativistic action has

- **internal** symmetries, which do not move the spacetime point — here the central phase $\tilde{\Phi}\mapsto \exp(i\alpha)\tilde{\Phi}$ of a complex biquaternion field, the symmetry whose localization is the gauge principle; and
- **spacetime** symmetries, the Poincaré transformations — four translations $\tilde{R}\mapsto\tilde{R}+\tilde{R}_0$ and six Lorentz transformations $\tilde{R}\mapsto\tilde U\tilde{R}\tilde U^{*}$. Translation invariance gives the conserved four-momentum; Lorentz invariance gives the conserved angular momentum.

The internal case produces a current biquaternion $\tilde{J}\in\mathbb{M}_-$ with $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J})=0$, the framework form of $\partial/\partial Q_\mu J^\mu = 0$. The spacetime case produces an energy–momentum current and an angular-momentum bivector.

**What is established, and what is not.** Established below, and recomputed: the central-phase current of the complex biquaternion scalar field,

$$
\tilde{J} = i\left[\tilde{\Phi}^{*}(\tilde{\nabla}\tilde{\Phi}) - (\tilde{\nabla}\tilde{\Phi}^{*})\tilde{\Phi}\right],
$$

lies in $\mathbb{M}_-$ and satisfies $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J}) = i\,\mathrm{Sc}[\tilde{\Phi}^{*}\Box\tilde{\Phi} - (\Box\tilde{\Phi}^{*})\tilde{\Phi}]$, which vanishes whenever the field obeys the Klein–Gordon equation; the free-particle four-momentum $\tilde{P} = m\tilde{V}$ is the Noether charge of translation invariance, and the **total** four-momentum of an isolated system is conserved; and a translation acts on a plane wave by the central phase $\exp(i\,\mathrm{Sc}(\tilde P\tilde{R}_0))$. What is standard, what is only transcribed, and what is interpretation is separated in its own section below.

**Two defects in the read list, handled rather than repeated.** First, the four-force of the parent is defined by the **proper**-time derivative, $\tilde{K}_{\mathrm{f}} = d\tilde{P}/d\tau$, so the sum $\sum_a\tilde{K}_{\mathrm{f},a}$ across bodies is *not* the rate of change of the total four-momentum unless all the Lorentz factors agree; *Exercise: Four-Momentum Conservation in a Collision* reports this, and the conservation law is stated correctly below. Second, the translation of a plane wave is by the **central** phase $\exp(i\,\mathrm{Sc}(\tilde P\tilde{R}_0))$ — the form *The Poincaré Group and the Biquaternion Frame* uses — not by $\exp(\mathrm{Sc}(\tilde P\tilde{R}_0^{\natural}))$, which is a positive real number and cannot be a phase.

**Conventions.** We use those of the read list unchanged. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the quaternion basis is $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $\vec e_\mu^2 = -e_t$ and $\vec e_\mu \vec e_\nu = -\delta_{\mu\nu}e_t + \varepsilon_{\mu\nu\lambda}\vec e_\lambda$; and $i$ is the scalar imaginary, $i^2 = -1$, commuting with every $\vec e_\mu$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian: imaginary scalar, real vector — the material sector) and $\mathbb{M}_+$ (Hermitian: real scalar, imaginary vector — the informational sector), with $\mathbb{B} = \mathbb{M}_-\oplus\mathbb{M}_+$; $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ is the complex scalar line, the centre of the algebra. The conjugations are ${}^{\natural}$ (quaternion), $\bar{\cdot}$ (complex), ${}^{*} = ({}^{\natural})^{\,*}$ (Hermitian), and ${}^\flat = -{}^{*}$ (anti-Hermitian). The biquaternionic gradient is $\tilde{\nabla} = e_t\partial/\partial Q_t + \vec e_x\partial/\partial Q_x + \vec e_y\partial/\partial Q_y + \vec e_z\partial/\partial Q_z$, its quaternion conjugate is $\tilde{\nabla}^{\natural} = e_t\partial/\partial Q_t - \vec e_x\partial/\partial Q_x - \vec e_y\partial/\partial Q_y - \vec e_z\partial/\partial Q_z$, and $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \partial^2/\partial Q_t^2 + \Delta$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the **speed of light in the medium** and $c_0$ the vacuum value; $\vec v$ is reserved for particle and frame velocities. The trace formula $\mathrm{Tr}(\tilde{Ϛ}\tilde H)=2\,\mathrm{Sc}(\tilde{Ϛ}\tilde H) = 2\langle\tilde{Ϛ},\tilde H\rangle$ is inherited unchanged.

## The Action and What a Symmetry Is

**The particle.** The free relativistic particle of rest mass $m$ has the action

$$
S[\tilde{R}] = -mc\int\sqrt{-\,d\tilde{R}\,d\tilde{R}^{\natural}},
\qquad d\tilde{R} = ic\,dt\,e_t + d(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\in\mathbb{M}_- .
$$

Because $d\tilde{R}\,d\tilde{R}^{\natural} = -c^2dt^2 +dx^2+dy^2+dz^2 = -c^2d\tau^2$ with $\tau$ the proper time, the action is $S = -mc^2\int dt/\gamma$, and the Lagrangian in the coordinate time $t$ is

$$
L(\vec v) = -mc^2\sqrt{1-\vec v^2/c^2} = -\frac{mc^2}{\gamma},
\qquad \gamma = \frac{1}{\sqrt{1-\vec v^2/c^2}} .
$$

**The field.** The relativistic scalar field of the framework is the complex biquaternion field $\tilde{\Phi} = \phi\,e_t \in \mathbb{C}_{\mathbb{B}}$, with $\phi$ a complex scalar function. Its action is $S[\tilde{\Phi}] = \int \mathcal{L}\,d^4x$ with the real Lagrangian density

$$
\mathcal{L} = -\,\mathrm{Sc}\!\left[(\tilde{\nabla}^{\natural}\tilde{\Phi}^{*})(\tilde{\nabla}\tilde{\Phi})\right] - \frac{m^2c^2}{\hbar^2}\,\mathrm{Sc}\!\left[\tilde{\Phi}^{*}\tilde{\Phi}\right].
$$

Expanding the scalar parts, $\mathcal{L} = -(\partial/\partial Q_t\,\phi^*)(\partial/\partial Q_t\,\phi) - \sum_k(\partial/\partial Q_k\,\phi^*)(\partial/\partial Q_k\,\phi) - (m^2c^2/\hbar^2)\phi^*\phi$, and its Euler–Lagrange equation is the biquaternion Klein–Gordon equation

$$
\left(\Box - \frac{m^2c^2}{\hbar^2}\right)\tilde{\Phi} = 0,
\qquad \Box = \tilde{\nabla}\tilde{\nabla}^{\natural} .
$$

Both the action and the equation are those of the read list; $\mathcal{L}$ is exhibited only because a Noether current is read off a Lagrangian.

**What a symmetry is.** A one-parameter family $\tilde{\Phi}_\varepsilon$ with $\tilde{\Phi}_0 = \tilde{\Phi}$ is a **symmetry of the action** if $S[\tilde{\Phi}_\varepsilon] = S[\tilde{\Phi}]$ for every field configuration, and a **symmetry of the equations of motion** if it preserves the solution set. A symmetry of the action is the stronger notion, and it is the one that yields a conserved current by Noether's theorem.

**Noether's theorem, in the two forms the framework needs.** For an internal symmetry, the theorem states that there is a current biquaternion $\tilde{J} = J^0e_t + J^\mu \vec e_\mu$ whose divergence vanishes when the field obeys its equation:

$$
\delta S = 0 \ \text{for all fields}
\qquad\Longrightarrow\qquad
\mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde{J}\right) = 0 \ \text{on shell}.
$$

For a spacetime symmetry, the same construction applied to a transformation that moves the point $\tilde{R}$ yields a current carrying one index per generator: for translations the energy–momentum current, for Lorentz transformations the angular-momentum current. The two forms differ only in what the symmetry variation acts on. The general identity behind both is that the divergence of the current is the field equation contracted with the symmetry variation; it is written out for the central phase in the next section and for translations after that.

## The Current of the Central Phase

**The symmetry.** Multiplication by a central phase,

$$
\tilde{\Phi}\ \longmapsto\ \exp(i\alpha)\tilde{\Phi},
\qquad \alpha\in\mathbb{R},
$$

leaves both terms of $\mathcal{L}$ unchanged, because $\exp(i\alpha)$ is central and $\tilde{\Phi}^{*}\mapsto \exp(-i\alpha)\tilde{\Phi}^{*}$: the two phase factors in $(\tilde{\nabla}^{\natural}\tilde{\Phi}^{*})(\tilde{\nabla}\tilde{\Phi})$ cancel, and $\tilde{\Phi}^{*}\tilde{\Phi}$ is invariant. The symmetry therefore holds for the **massive** field as well as the massless one, because the mass term depends on $\tilde{\Phi}$ only through the invariant $\tilde{\Phi}^{*}\tilde{\Phi}$ — a fact used again below.

**The current.** For the infinitesimal variation $\delta\tilde{\Phi} = i\alpha\tilde{\Phi}$, $\delta\tilde{\Phi}^{*} = -i\alpha\tilde{\Phi}^{*}$, the Noether current is

$$
J^\nu = \frac{\partial\mathcal{L}}{\partial(\partial/\partial Q_\nu\,\tilde{\Phi})}\,\delta\tilde{\Phi} + \frac{\partial\mathcal{L}}{\partial(\partial/\partial Q_\nu\,\tilde{\Phi}^{*})}\,\delta\tilde{\Phi}^{*}
= i\left(\phi^*\partial/\partial Q_\nu\,\phi - \phi\,\partial/\partial Q_\nu\,\phi^*\right),
$$

the second equality after using $\partial\mathcal{L}/\partial(\partial/\partial Q_\nu\,\phi) = -\partial/\partial Q_\nu\,\phi^*$ and $\partial\mathcal{L}/\partial(\partial/\partial Q_\nu\,\phi^*) = -\partial/\partial Q_\nu\,\phi$, and setting $\alpha = 1$. Packaged as a biquaternion,

$$
\boxed{\ \tilde{J} = i\left[\tilde{\Phi}^{*}(\tilde{\nabla}\tilde{\Phi}) - (\tilde{\nabla}\tilde{\Phi}^{*})\tilde{\Phi}\right] = J^\nu e_\nu\ }
\qquad (\tilde{\Phi} = \phi\,e_t).
$$

**The current lies in the material sector.** The temporal component in the $ict$ basis is $J^0 = i(\phi^*\partial/\partial Q_t\,\phi - \phi\,\partial/\partial Q_t\,\phi^*)$, and since $\partial/\partial Q_t = -\frac{i}{c}\partial/\partial t$, it equals $\frac{1}{c}(\phi^*\partial/\partial t\phi - \phi\,\partial/\partial t\phi^*) = \frac{2i}{c}\,\mathrm{Im}(\phi^*\partial/\partial t\phi)$, which is **purely imaginary**; the spatial components $J^k = i(\phi^*\partial/\partial Q_k\,\phi - \phi\,\partial/\partial Q_k\,\phi^*)$ are real. Hence $\tilde{J}\in\mathbb{M}_-$, with imaginary scalar part and real vector part, exactly as the four-current of relativistic mechanics. Writing $J^0 = ic\rho$ recovers the parent's convention $\tilde{J} = ic\rho\,e_t + \vec j$.

**Conservation.** Forming the scalar part of $\tilde{\nabla}^{\natural}\tilde{J}$,

$$
\mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde{J}\right) = \sum_\mu\partial/\partial Q_\mu\,J_\mu = \langle\tilde\nabla,\tilde J\rangle_{\natural} ,
$$

the last equality because in the $ict$ basis the time component is $i$ times its physical value, so $\partial/\partial Q_t$ of the $ict$ component equals $\partial/\partial(ct)$ of the corresponding real physical component. Using the definitions and $\Box = \partial^2/\partial Q_t^2 + \Delta$,

$$
\boxed{\ \mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde{J}\right) = i\,\mathrm{Sc}\!\left[\tilde{\Phi}^{*}(\Box\tilde{\Phi}) - (\Box\tilde{\Phi}^{*})\tilde{\Phi}\right]\ }
$$

This is the Noether identity in biquaternion form: the scalar divergence of the current is the Klein–Gordon operator applied to the field, contracted with the symmetry variation. On shell, $\Box\tilde{\Phi} = (m^2c^2/\hbar^2)\tilde{\Phi}$, both terms become the same real multiple of $\tilde{\Phi}^{*}\tilde{\Phi}$ and cancel, so

$$
\mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde{J}\right) = 0 \quad\text{on shell},
$$

which is the continuity equation $\partial/\partial t\rho + \mathrm{div}\,\vec j = 0$.

**On what case was this checked?** A single plane wave is a trap: for $\tilde{\Phi} = \tilde{\Phi}_0\exp(i\,\mathrm{Sc}(\tilde P\tilde{R}))$ the current is *constant*, so its divergence vanishes whether or not the field is on shell, and the plane wave that suggests the formula cannot test it. The conservation was therefore checked on three other cases:

- **a superposition of on-shell plane waves.** With $c = \hbar = m = 1$ and the momenta $(|\vec k|,\omega) = (0,1)$, $(\tfrac34,\tfrac54)$, $(\tfrac{5}{12},\tfrac{13}{12})$ all satisfying $\omega^2 = \vec k^2 + 1$, and amplitudes $1, \tfrac12, \tfrac13$, the current has non-constant cross terms, and $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J})$ simplifies to **exactly zero**;
- **a standing wave**, $\tilde{\Phi} = \sin(kx)\cos(\omega t) + i\sin(kx)\sin(\omega t)$ with $\omega^2 = c^2k^2 + m^2c^4/\hbar^2$: this is on shell and is **not** a plane wave, and again $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J})$ is **exactly zero**;
- **an off-shell field.** A two-mode field with one mode off shell gives a divergence proportional to the field equation, explicitly nonzero. The identity above was also confirmed symbolically on a generic three-mode field, off shell: the difference $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J}) - i\,\mathrm{Sc}[\tilde{\Phi}^{*}\Box\tilde{\Phi} - (\Box\tilde{\Phi}^{*})\tilde{\Phi}]$ reduces to zero identically.

The last case is the honest statement of the theorem: the current is conserved **whenever** the field equation holds; off shell it need not be, and its divergence *is* the field equation.

**Relation to the current already in the corpus.** *The Klein–Gordon Equation in Biquaternionic Form* posits the current with $\rho = \frac{i\hbar}{2mc^2}(\tilde{\Phi}^*\partial/\partial t\tilde{\Phi} - \tilde{\Phi}\partial/\partial t\tilde{\Phi}^*)$ and $\vec j = -\frac{i\hbar}{2m}(\tilde{\Phi}^*\nabla\tilde{\Phi} - \tilde{\Phi}\nabla\tilde{\Phi}^*)$. Comparing component by component, that current equals $-\frac{\hbar}{2m}\tilde{J}$: the Noether derivation reproduces the current the parent states, and fixes the normalization only up to the constant $-\hbar/2m$ that a current may always be multiplied by. What the derivation adds is **why** that combination is the conserved one, and that it is forced by the phase symmetry rather than chosen.

**Relation to the Maxwell source.** In the Maxwell article the source conservation is $\sqrt{\mu}\,\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J}) = 0$ with $\tilde J = ic\rho\,e_t + \vec J$. Expanding, $\sqrt{\mu}\,\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J}) = \sqrt{\mu}\,(\partial/\partial t\rho + \mathrm{div}\,\vec J)$, so the Maxwell integrability condition is the same continuity equation as the conservation of $\tilde{J}$ above. The electric four-current of the material sector is the Noether current of the central phase; the gauge freedom localized in *The Gauge Principle in Biquaternionic Form* is the localization of the symmetry that produces it.

**The mass, and where the symmetry stops.** The phase symmetry derived here holds for the massive Klein–Gordon field, and — with the parent's mass term now written in its linear, chirality-off-diagonal form $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$ — it holds for the massive Dirac field as well. A central phase passes through the linear mass term, so the current above is the conserved current of both fields, and $\langle\tilde\nabla,\tilde J\rangle_{\natural} = 0$ on shell for each. What the mass term breaks is the **axial** symmetry, not the phase: the associated divergence identity is

$$
\langle\tilde\nabla,\tilde J_5\rangle_{\natural} = 2im\,\tilde{\Psi}^{\natural}\gamma_5\tilde{\Psi},
$$

which vanishes only in the massless limit. In the biquaternion interpretation the mass term is the off-diagonal coupling between the two *central* ideals of $\mathbb{B}$ — the two chiralities — so it breaks exactly the symmetry that rotates them, and not the central $\mathrm{U}(1)$ that the algebra canonically carries. The previously recorded obstruction belonged to the retired antilinear single-field equation; the gauge principle article's corresponding section is revised on the same grounds.

## Translation Invariance and the Conserved Four-Momentum

**The particle charge.** The action $S[\tilde{R}]$ above depends on $\tilde{R}$ only through $d\tilde{R}$, so the constant shift

$$
\tilde{R}\ \longmapsto\ \tilde{R} + \tilde{R}_0,
\qquad \tilde{R}_0\in\mathbb{M}_-\ \text{constant},
$$

is a symmetry of the action. The Noether charges are the momentum conjugate to $x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ and the energy conjugate to $t$; computing the first from the Lagrangian,

$$
\vec p = \frac{\partial L}{\partial\vec v} = \gamma m\vec v,
\qquad
E = \vec p\cdot\vec v - L = \gamma mc^2,
$$

and combining them into the four-momentum,

$$
\boxed{\ \tilde{P} = m\tilde{V} = i\frac{E}{c}\,e_t + \vec p\ }
\qquad (\tilde{V} = \gamma(ic\,e_t + \vec v)).
$$

The mass-shell relation $\tilde{P}\tilde{P}^{\natural} = -m^2c^2$ follows. Translation invariance is thus the symmetry whose Noether charge is the four-momentum; the four-momentum is conserved for a free particle, $d\tilde{P}/d\tau = 0$, because $L$ has no explicit $\tilde{Q}$-dependence. As an independent check, a particle with $m = c = 1$, $\vec p = (0.6,0,0)$ and $E = \sqrt{1.36}$ was boosted by the rotor $\tilde U = \cosh(\psi/2) + i\sinh(\psi/2)\vec e_x$ with $\psi = 1.2$: the biquaternion norm is $-1$ in both frames, confirming that the Noether charge transforms as a four-vector.

**The conservation law for a system, stated correctly.** For an isolated system of bodies $a$ the conserved object is the **total** four-momentum, and the correct statement is

$$
\tilde{P}_{\mathrm{tot}} = \sum_a \tilde{P}_a,
\qquad
\frac{d\tilde{P}_{\mathrm{tot}}}{dt} = 0,
$$

a vanishing **coordinate**-time derivative. The parent defines the four-force by the **proper**-time derivative of a single body, $\tilde{K}_{\mathrm{f},a} = d\tilde{P}_a/d\tau_a$, and since $d\tau_a = dt/\gamma_a$,

$$
\frac{d\tilde{P}_a}{dt} = \frac{1}{\gamma_a}\tilde{K}_{\mathrm{f},a},
\qquad\text{so}\qquad
\sum_a \tilde{K}_{\mathrm{f},a} = \sum_a \gamma_a\frac{d\tilde{P}_a}{dt},
$$

which equals $d\tilde{P}_{\mathrm{tot}}/dt$ only when all the $\gamma_a$ are equal. The parent's symbol $\tilde{K}_{\mathrm{f}}$ is a per-body proper-time rate and cannot be summed across bodies. The conservation law in terms of the parent's four-forces is therefore

$$
\sum_a \frac{1}{\gamma_a}\tilde{K}_{\mathrm{f},a} = \frac{d\tilde{P}_{\mathrm{tot}}}{dt} = 0,
$$

or, in the integrated form that avoids the derivative altogether, $\sum_{\mathrm{in}}\tilde{P} = \sum_{\mathrm{out}}\tilde{P}$ for a collision. The exercise reports this defect; the corrected statement above is the one to use.

**A numerical witness.** Two bodies connected by a translation-invariant interaction exchange momentum, so $d\tilde{P}_2/dt = -d\tilde{P}_1/dt = i\,e_t + \vec e_x$ at some instant, and their Lorentz factors differ, $\gamma_1 = 5/3$, $\gamma_2 = 5/4$. Then $d\tilde{P}_{\mathrm{tot}}/dt = 0$, but

$$
\tilde{K}_{\mathrm{f},1} + \tilde{K}_{\mathrm{f},2} = (\gamma_1 - \gamma_2)\frac{d\tilde{P}_1}{dt} = -\frac{5}{12}\left(i\,e_t + \vec e_x\right) \neq 0 .
$$

The naive sum of the parent's four-forces is not zero even though the total four-momentum is conserved. For the collision of *Exercise: Four-Momentum Conservation in a Collision* ($E_1 = 3mc^2$, equal masses, $\theta^* = 90^\circ$), the total four-momenta $\tilde{P}_{\mathrm{in}}$ and $\tilde{P}_{\mathrm{out}}$ were recomputed and agree component by component in the laboratory.

**What translation does to a plane wave.** A free field is a plane wave, and a translation acts on it by a central phase. With the series' phase convention $\tilde{\Phi} = \tilde{\Phi}_0\exp(i\,\mathrm{Sc}(\tilde P\tilde{R}))$, $\tilde P\in\mathbb{M}_-$, and $\tilde{R}\mapsto\tilde{R}+\tilde{R}_0$,

$$
\tilde{\Phi}\big|_{\tilde{R}+\tilde{R}_0} = \exp(\,i\,\mathrm{Sc}(\tilde P\tilde{R}_0))\,\tilde{\Phi}\big|_{\tilde{R}},
\qquad
\tilde{\Phi}_0\ \text{constant}.
$$

The multiplier $\exp(i\,\mathrm{Sc}(\tilde P\tilde{R}_0))$ is **central and of unit modulus**, because $\mathrm{Sc}(\tilde P\tilde{R}_0) = \langle\tilde P,\tilde{R}_0\rangle$ is real: writing $\tilde P = i\frac{\omega}{c}e_t + \vec k$ and $\tilde{R}_0 = i R_{0t} e_t + \vec R_0$,

$$
\mathrm{Sc}(\tilde P\tilde{R}_0) = -\frac{\omega R_{0t}}{c} - \vec k\cdot\vec R_0 .
$$

The pairing is $\mathrm{Sc}(\tilde P\tilde{R}_0) = \langle\tilde P,\tilde{R}_0\rangle$, **not** $\mathrm{Sc}(\tilde P\tilde{R}_0^{\natural}) = -\frac{\omega R_{0t}}{c} + \vec k\cdot\vec R_0$: the latter is real, so $\exp(\mathrm{Sc}(\tilde P\tilde{R}_0^{\natural}))$ is a positive real number rather than a phase, and a translation multiplier must have unit modulus. For the values $\tilde P = 2i\,e_t + 0.7\vec e_x - 0.3\vec e_y + 0.5\vec e_z$ and $\tilde{R}_0 = 0.4i\,e_t + 0.25\vec e_x - 0.35\vec e_y + 0.15\vec e_z$ (units $c = 1$) one has $\mathrm{Sc}(\tilde P\tilde{R}_0) = -1.155$ and $\mathrm{Sc}(\tilde P\tilde{R}_0^{\natural}) = -0.445$; the true multiplier is $\exp(-1.155i)$. This central phase is the finite, field-space form of the translation subgroup; its infinitesimal generator is the derivation $\partial/\partial Q_\mu$, and it is not a rotor, as *The Poincaré Group and the Biquaternion Frame* establishes.

## The Energy–Momentum of the Field

The same translation symmetry applied to the field action gives the **canonical energy–momentum**, the Noether current of spacetime translations. For the complex scalar field it is

$$
T^\mu{}_\nu = -(\partial^\mu\phi^*)\,\partial/\partial Q_\nu\,\phi - (\partial^\mu\phi)\,\partial/\partial Q_\nu\,\phi^* - \delta^\mu{}_\nu\,\mathcal{L},
$$

and translation invariance of $\mathcal{L}$ gives $\partial/\partial Q_\mu T^\mu{}_\nu = 0$ on shell. Its time–time component is the energy density,

$$
T^0{}_0 = |\partial/\partial(ct)\phi|^2 + |\nabla\phi|^2 + \frac{m^2c^2}{\hbar^2}|\phi|^2 > 0,
$$

positive, in contrast with the charge density, whose sign is not fixed. This was checked by symbolic recomputation on the on-shell superposition of three plane waves: all four divergences $\partial/\partial Q_\mu T^\mu{}_\nu$ simplify to zero, and $T^0{}_0$ is exactly the expression above.

**Why the framework does not write this as one biquaternion.** A symmetric rank-two tensor in four dimensions has ten independent components, while a biquaternion has four complex coefficients, that is eight real components, and $\tilde{W} = \tfrac12\tilde{F}\tilde{F}^{*}$ carries only four of them. So no single biquaternion can be $T^{\mu\nu}$; the framework writes the translation current as a **bigeneral quaternionic bilinear**, one basis element for each index. *Exercise: The Electromagnetic Energy–Momentum Tensor* constructs exactly this for the Maxwell field, $T^\mu{}_\nu = \tfrac12\mathrm{Sc}(\tilde{F}\mathcal{E}_\mu\tilde{F}^{*}\mathcal{E}_\nu)$, and shows that the four-component object is its time row. The framework's energy–momentum biquaternion is therefore not the whole Noether current of translations; it is the energy–flux part of it.

**The Maxwell case in the corpus form.** For the electromagnetic field the corpus's object is $\tilde{W} = \tfrac12\tilde{F}\tilde{F}^{*} = W\,e_t + \frac{i}{c}\vec S\in\mathbb{M}_+$, with $W$ the energy density and $\vec S = \vec E\times\vec H$ the Poynting vector, and the conservation law is $\tilde{\nabla}\tilde{W} = -\tilde{\mathcal F}$ with $\tilde{P}$ the power–force density; the source-free case is $\tilde{\nabla}\tilde{W} = 0$. Its scalar part is the Poynting theorem, and the sign structure is the one the energy–momentum exercise verifies: the Hermitian form passes the test, while the real form $W + \frac{1}{c}\vec S$ does not, by a factor $i$ on the Poynting part. Read as a Noether statement, $\tilde{\nabla}\tilde{W} = -\tilde{\mathcal F}$ says that the translation current of the Maxwell field is conserved up to the work done on the charges — the source is present, so the field alone is not closed.

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
\vec{L} = \tfrac12\sum_{\mu,\nu}L^{\mu\nu}\,\bar{e}_\mu e_\nu,
$$

the angular momentum of a free particle is a single biquaternion. This is the same construction by which $\tilde{F} = \mathrm{Vect}(\tilde{\nabla}^{\natural}\tilde{A}) = \tfrac12\sum_{\mu\nu}F_{\mu\nu}\bar{e}_\mu e_\nu$ packages the antisymmetric field strength, and the Lorentz generators themselves are bivectors.

**What does not carry over as a single biquaternion.** For a field, the Noether current of Lorentz invariance is a rank-three object, $L^{\mu\nu\rho} = x^\nu T^{\mu\rho} - x^\rho T^{\mu\nu} + S^{\mu\nu\rho}$, whose conservation $\partial/\partial Q_\mu L^{\mu\nu\rho} = 0$ expresses the symmetry of the energy–momentum tensor together with the conservation of spin. Being rank three, it is not a biquaternion and not even a single bilinear; the orbital and spin pieces separate, with the spin term vanishing for the classical scalar field. The particle bivector $\vec{L}$ above is the finite-dimensional case where the rank-two object *is* the whole story.

## What Is Inherited, What Is Added, What Is Interpretation

**Inherited and unchanged.** The action, the four-momentum, the four-current and its conservation $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J}) = 0$, the algebra, the gradient, the sectors, and the trace formula, for a state $\tilde{Ϛ}$ and an observable $\tilde H$, $\mathrm{Tr}(\tilde{Ϛ}\tilde H)=2\,\mathrm{Sc}(\tilde{Ϛ}\tilde H) = 2\langle\tilde{Ϛ},\tilde H\rangle$ are those of the read list. No symbol is renamed or rederived.

**Added by this article.** The derivation of the central-phase current $\tilde{J} = i[\tilde{\Phi}^{*}\tilde{\nabla}\tilde{\Phi} - (\tilde{\nabla}\tilde{\Phi}^{*})\tilde{\Phi}]$ from the phase symmetry of the field action, and its conservation identity; the identification of the free-particle four-momentum as the Noether charge of translation invariance, with the corrected multi-body statement; the explicit translation multiplier $\exp(i\,\mathrm{Sc}(\tilde P\tilde{R}_0))$; the energy–momentum current and its packaging; and the angular-momentum bivector. These are transcriptions of the standard theorem into the algebra, with the subspace assignments the algebra supplies, not new physics.

**Only transcribed.** Noether's theorem itself is standard; the algebra does not produce a symmetry that the action did not already have, nor a conservation law beyond those the symmetries give. The framework supplies the home of each conserved object — the current in $\mathbb{M}_-$, the energy–momentum in the bilinear and its time row in $\mathbb{M}_+$ for Maxwell, the angular momentum in the bivector — and it makes the divergence identities compact. It does not supply the symmetries, the coupling constants, or the masses.

**Interpretation.** Interpretation the conserved currents as the physical four-current and energy–momentum is the standard interpretation, not an extra postulate; the biquaternion packaging is a representation-theoretic statement about which subspace carries which object, and it is exact. What remains interpretation is the physical hypothesis attached to the two sectors, which is the program's, not this article's.

## Open Questions

1. **The biquaternion form of the full translation current.** The energy–momentum tensor is rank two and cannot be one biquaternion. Is there a natural biquaternion-bilinear expression for the canonical $T^\mu{}_\nu$ of a general biquaternion field, beyond the Maxwell case constructed in the energy–momentum exercise?

2. **Spin and the angular momentum of fields.** The rank-three Lorentz current carries a spin term. Can the spin density of a biquaternion field be written as a biquaternion expression, and how does it relate to the bivector representation of angular momentum?

3. **Scale and conformal symmetry.** The massless Klein–Gordon and Maxwell actions have more symmetries than the Poincaré group. Do they have biquaternion Noether currents, and does the tracelessness of the electromagnetic energy–momentum tensor — established in the energy–momentum exercise — express one of them?

4. **The axial current and the two central ideals.** With the parent's linear mass term the vector phase current is conserved for the massive field, so the open question is the axial one. The divergence identity $\partial/\partial Q_\mu j_5^\mu = 2im\,\tilde{\Psi}^{\natural}\gamma_5\tilde{\Psi}$ holds for the linear mass term, and its biquaternion interpretation is that the mass couples the two central ideals of $\mathbb{B}$ off-diagonally. Is there a biquaternion Noether derivation of that identity — the axial current as the Noether current of the chirality rotation — and does the central-element structure supply anything analogous to the would-be Goldstone statement?

5. **The current of the complexified theory.** In the complexified biquaternion theory of the Maxwell article, the source and potential are fully complex. Does the central-phase current acquire components outside $\mathbb{M}_-$, and are they conserved?

6. **Empirical content.** As everywhere in the framework, the currents derived here are the standard ones in new notation. Whether the biquaternion packaging imposes any constraint that the four-vector formulation does not is not established here.

## Summary

Noether's theorem in biquaternionic form joins the action of *Relativistic Mechanics in Biquaternionic Form* to the conserved current of the same article. The theorem has two forms. For an **internal** symmetry, that of the central phase $\tilde{\Phi}\mapsto \exp(i\alpha)\tilde{\Phi}$ of the complex biquaternion scalar field, the derived current is

$$
\tilde{J} = i\left[\tilde{\Phi}^{*}(\tilde{\nabla}\tilde{\Phi}) - (\tilde{\nabla}\tilde{\Phi}^{*})\tilde{\Phi}\right] = J^\nu e_\nu,
\qquad J^\nu = i\left(\phi^*\partial/\partial Q_\nu\,\phi - \phi\,\partial/\partial Q_\nu\,\phi^*\right),
$$

which lies in $\mathbb{M}_-$ and satisfies the Noether identity

$$
\mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde{J}\right) = i\,\mathrm{Sc}\!\left[\tilde{\Phi}^{*}(\Box\tilde{\Phi}) - (\Box\tilde{\Phi}^{*})\tilde{\Phi}\right],
$$

zero whenever the field is on shell. This is the framework form of $\langle\tilde\nabla,\tilde J\rangle_{\natural} = 0$; it reproduces the current the Klein–Gordon article posits, up to the conventional constant $-\hbar/2m$, and its expansion at the Maxwell source is the charge-conservation condition $\mathrm{Sc}(\tilde{\nabla}^{\natural}\sqrt{\mu}\,\tilde{J}) = 0$.

For a **spacetime** symmetry, translation invariance gives the four-momentum

$$
\tilde{P} = m\tilde{V} = i\frac{E}{c}e_t + \vec p,
\qquad E = \gamma mc^2,\quad \vec p = \gamma m\vec v,
$$

as the Noether charge, conserved for a free particle. The conservation law for a system is the vanishing of the **coordinate**-time derivative of the total, $d\tilde{P}_{\mathrm{tot}}/dt = 0$; the parent's proper-time four-force cannot be summed across bodies, and the correct form is $\sum_a\tilde{K}_{\mathrm{f},a}/\gamma_a = 0$, or the integrated $\sum_{\mathrm{in}}\tilde{P} = \sum_{\mathrm{out}}\tilde{P}$. A translation acts on a plane wave by the central unit-modulus phase $\exp(i\,\mathrm{Sc}(\tilde P\tilde{R}_0))$, with $\mathrm{Sc}(\tilde P\tilde{R}_0) = -\frac{\omega R_{0t}}{c} - \vec k\cdot\vec R_0$.

The field translation current is the canonical energy–momentum, $\partial/\partial Q_\mu T^\mu{}_\nu = 0$ on shell with positive energy density $T^0{}_0 = |\partial/\partial(ct)\phi|^2 + |\nabla\phi|^2 + \frac{m^2c^2}{\hbar^2}|\phi|^2$. Rank two cannot be one biquaternion, so the framework packages it bilinearly; the Maxwell object $\tilde{W} = \tfrac12\tilde{F}\tilde{F}^{*}$ with $\tilde{\nabla}\tilde{W} = -\tilde{\mathcal F}$ is its time row. Lorentz invariance gives the angular-momentum bivector $\vec{L} = \tfrac12\sum L^{\mu\nu}\bar{e}_\mu e_\nu$, with the rank-three field current reduced to the rank-two particle bivector only when the spin term vanishes. The theorem is standard; the algebra supplies the home of each conserved object and the compact form of its divergence, and it supplies no conservation law the symmetries did not already give.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_\mu^2 = -e_t$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}, \mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ | Real-quaternion subspace; complex scalar line (the centre) |
| $\tilde{\nabla} = e_t\partial/\partial Q_t + \vec e_\mu\,\partial/\partial Q_\mu$ | Biquaternionic gradient |
| $\tilde{\nabla}^{\natural} = e_t\partial/\partial Q_t - \vec e_\mu\,\partial/\partial Q_\mu$ | Quaternion-conjugate gradient |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \partial^2/\partial Q_t^2 + \Delta$ | d'Alembertian |
| $S = -mc\int\sqrt{-d\tilde{R}\,d\tilde{R}^{\natural}}$ | Free-particle action |
| $L = -mc^2\sqrt{1-\vec v^2/c^2}$ | Free-particle Lagrangian |
| $\tilde{R} = ic\,t\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ | Four-position, in $\mathbb{M}_-$ |
| $\tilde{V} = \gamma(ic\,e_t + \vec v)$ | Four-velocity, $\tilde{V}\tilde{V}^{\natural} = -c^2$ |
| $\tilde{P} = m\tilde{V} = iE/c\,e_t + \vec p$ | Four-momentum, Noether charge of translation |
| $\tilde{K}_{\mathrm{f},a} = d\tilde{P}_a/d\tau_a$ | Four-force (proper-time derivative; not summable) |
| $\tilde{R}_0\in\mathbb{M}_-$ | Constant translation (displacement) |
| $\tilde{\Phi} = \phi\,e_t\in\mathbb{C}_{\mathbb{B}}$ | Complex biquaternion scalar field |
| $\mathcal{L} = -\mathrm{Sc}[(\tilde{\nabla}^{\natural}\tilde{\Phi}^{*})(\tilde{\nabla}\tilde{\Phi})] - \frac{m^2c^2}{\hbar^2}\mathrm{Sc}[\tilde{\Phi}^{*}\tilde{\Phi}]$ | Field Lagrangian density |
| $\tilde{J} = i[\tilde{\Phi}^{*}\tilde{\nabla}\tilde{\Phi} - (\tilde{\nabla}\tilde{\Phi}^{*})\tilde{\Phi}]$ | Central-phase Noether current, in $\mathbb{M}_-$ |
| $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J}) = 0$ | Framework form of current conservation |
| $\tilde J = ic\rho\,e_t + \vec J$ | Maxwell source $\sqrt{\mu}\,\tilde J$; $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J}) = 0$ is charge conservation |
| $T^\mu{}_\nu$ | Canonical energy–momentum of the field |
| $\tilde{W} = \tfrac12\tilde{F}\tilde{F}^{*} = W\,e_t + \frac{i}{c}\vec S$ | Maxwell energy–momentum (time row), in $\mathbb{M}_+$ |
| $L^{\mu\nu} = x^\mu p^\nu - x^\nu p^\mu$, $\vec{L} = \tfrac12\sum L^{\mu\nu}\bar{e}_\mu e_\nu$ | Angular momentum and its bivector |
| $\tilde P = i\frac{\omega}{c}e_t + \vec k$ | Four-wavevector, in $\mathbb{M}_-$ |
| $\exp(i\,\mathrm{Sc}(\tilde P\tilde{R}_0))$ | Central translation multiplier on a plane wave |
| $\mathrm{Tr}(\tilde{Ϛ}\tilde H)=2\,\mathrm{Sc}(\tilde{Ϛ}\tilde H) = 2\langle\tilde{Ϛ},\tilde H\rangle$ | Trace formula of the informational sector |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2)$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{\natural}=\langle\tilde{Q}_2\rangle_{\natural}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |

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
- *The Material Sector: Four-Vectors, Interval and Lorentz Action* and *The Informational Sector: States, Observables and Probability* — the two sectors that house the conserved objects.
- *Introduction to the Biquaternion Universe* — the algebra, its conjugations, and the local complex structure.
