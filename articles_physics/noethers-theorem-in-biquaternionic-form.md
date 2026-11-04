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

The internal case produces a current biquaternion $\tilde{J}\in\mathbb{M}_-$ with $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J})=0$ on shell, the framework form of $\sum_\mu\partial J_\mu/\partial Q_\mu = 0$. The spacetime case produces an energy–momentum current and an angular-momentum bivector.

**What is established, and what is not.** Established below, and recomputed: the central-phase current of the complex biquaternion scalar field,

$$
\tilde{J} = i\left[(\tilde{\nabla}\tilde{\Phi}^{*})\tilde{\Phi} - \tilde{\Phi}^{*}(\tilde{\nabla}\tilde{\Phi})\right],
$$

lies in $\mathbb{M}_-$ and satisfies $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J}) = i\,\mathrm{Sc}[(\Box\tilde{\Phi}^{*})\tilde{\Phi} - \tilde{\Phi}^{*}(\Box\tilde{\Phi})]$, which vanishes whenever the field obeys the Klein–Gordon equation, the sign of $\tilde{J}$ being the one for which the charge density of a positive-frequency wave is positive; the same current on the Dirac module is the cell bilinear $j_\mu=\bar{\psi}\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}}\,\psi$, conserved at every mass, while the axial current carries the chirality cell and is conserved only at $m=0$; the free-particle four-momentum $\tilde{P} = m\tilde{V}$ is the Noether charge of translation invariance, and the **total** four-momentum of an isolated system is conserved; and a translation acts on a plane wave by the central unit-modulus phase $\exp(i\,\mathrm{Sc}(\tilde P\tilde{R}_0^{\natural}))$. What is standard, what is only transcribed, and what is interpretation is separated in its own section below.

**Two defects in the read list, handled rather than repeated.** First, the four-force of the parent is defined by the **proper**-time derivative, $\tilde{K}_{\mathrm{f}} = d\tilde{P}/d\tau$, so the sum $\sum_a\tilde{K}_{\mathrm{f},a}$ across bodies is *not* the rate of change of the total four-momentum unless all the Lorentz factors agree; *Exercise: Four-Momentum Conservation in a Collision* reports this, and the conservation law is stated correctly below. Second, the translation of a plane wave is by a **central phase**, $\exp(i\,\mathrm{Sc}(\tilde P\tilde{R}_0^{\natural}))$, and the $i$ is not optional: the same scalar in a real exponential, $\exp(\mathrm{Sc}(\tilde P\tilde{R}_0^{\natural}))$, is a dilation and not a phase at all.

**Conventions.** We use those of the read list unchanged. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the quaternion basis is $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $\vec e_x^2 = \vec e_y^2 = \vec e_z^2 = -e_t$ and $\vec e_x\vec e_y = -\vec e_y\vec e_x = \vec e_z$, cyclically; $i$ is the scalar imaginary, $i^2 = -1$, commuting with every unit; and $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ with $\varepsilon=(1,-1,-1,-1)$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian: imaginary scalar, real vector — the material sector) and $\mathbb{M}_+$ (Hermitian: real scalar, imaginary vector — the informational sector), with $\mathbb{B} = \mathbb{M}_-\oplus\mathbb{M}_+$; $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ is the complex scalar line, the centre of the algebra. The conjugations are ${}^{\natural}$ (quaternion), $\bar{\cdot}$ (complex), ${}^{*} = ({}^{\natural})^{\,*}$ (Hermitian), and ${}^\flat = -{}^{*}$ (anti-Hermitian). The biquaternionic gradient is $\tilde{\nabla} = e_t\partial/\partial Q_t + \vec e_x\partial/\partial Q_x + \vec e_y\partial/\partial Q_y + \vec e_z\partial/\partial Q_z$, its quaternion conjugate is $\tilde{\nabla}^{\natural} = e_t\partial/\partial Q_t - \vec e_x\partial/\partial Q_x - \vec e_y\partial/\partial Q_y - \vec e_z\partial/\partial Q_z$, and $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \partial^2/\partial Q_t^2 + \Delta$, with $Q_t=ict'$ so that $\partial/\partial Q_t = -i\partial/\partial(ct')$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the **speed of light in the medium** and $c_0$ the vacuum value; $\vec v$ is reserved for particle and frame velocities. The normalised Hermitian form, read as the trace formula $\mathrm{Tr}(\tilde{Ϛ}\tilde H^{*})=2\langle\tilde{Ϛ},\tilde H\rangle_{*} = 2\,\mathrm{Sc}(\tilde{Ϛ}\tilde H^{*})$, is inherited unchanged.

**The cells, once.** The Dirac content of the later sections is written in the two-sided cells of the module, $L_aR_b\psi=a\psi b$ with $L_aR_bL_cR_d=L_{ac}R_{db}$, so that right multipliers compose in the order in which they act; the chirality cell is $\chi=-iR_{\vec e_z}^{\mathrm{axf}}$; and the Dirac bar is $\bar{\psi}=\psi^{\dagger}iR_{\vec e_x}^{\mathrm{axf}}$. The same objects under their Clifford frame names are collected in the closing section *The Legacy Pauli Gamma Formulation*, and none of those names is used before it.

## The Action and What a Symmetry Is

### The Particle

The free relativistic particle of rest mass $m$ has the action

$$
S[\tilde{R}] = -mc\int\sqrt{-\,d\tilde{R}\,d\tilde{R}^{\natural}},
\qquad d\tilde{R} = ic\,dt'\,e_t + d(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\in\mathbb{M}_- .
$$

Because $d\tilde{R}\,d\tilde{R}^{\natural} = -c^2d{t'}^2 +dx^2+dy^2+dz^2 = -c^2d\tau^2$ with $\tau$ the proper time, the action is $S = -mc^2\int dt'/\gamma$, and the Lagrangian in the coordinate time $t'$ is

$$
\mathrm{Lag}(\vec v) = -mc^2\sqrt{1-\vec v^2/c^2} = -\frac{mc^2}{\gamma},
\qquad \gamma = \frac{1}{\sqrt{1-\vec v^2/c^2}} .
$$

### The Field

The relativistic scalar field of the framework is the complex biquaternion field $\tilde{\Phi} = \phi\,e_t \in \mathbb{C}_{\mathbb{B}}$, with $\phi$ a complex scalar function. Its action is $S[\tilde{\Phi}] = \int \mathcal{L}\,d^4x$ with the real Lagrangian density

$$
\mathcal{L} = +\,\mathrm{Sc}\!\left[(\tilde{\nabla}^{\natural}\tilde{\Phi}^{*})(\tilde{\nabla}\tilde{\Phi})\right] + \frac{m^2c^2}{\hbar^2}\,\mathrm{Sc}\!\left[\tilde{\Phi}^{*}\tilde{\Phi}\right].
$$

Because $\mathrm{Sc}(e_\mu^{\natural}e_\nu)=\delta_{\mu\nu}$, the first term expands over the four coordinates with a single sign,

$$
\mathcal{L} = +\frac{\partial\phi^{*}}{\partial Q_t}\frac{\partial\phi}{\partial Q_t}
+\sum_k\frac{\partial\phi^{*}}{\partial Q_k}\frac{\partial\phi}{\partial Q_k}
+\frac{m^2c^2}{\hbar^2}\,\phi^{*}\phi ,
$$

the uniform signs being a property of the $Q$ frame. The time term is nevertheless negative, because $\partial/\partial Q_t = -i\partial/\partial(ct')$ acts on both factors and $(-i)^2=-1$; in the real frame the same expression reads

$$
\mathcal{L} = -\frac{1}{c^2}\left|\frac{\partial\phi}{\partial t'}\right|^2 + |\nabla\phi|^2 + \frac{m^2c^2}{\hbar^2}|\phi|^2 .
$$

This is the form used with the energy–momentum tensor below. The Euler–Lagrange equation of $\mathcal{L}$ is the biquaternion Klein–Gordon equation

$$
\left(\Box - \frac{m^2c^2}{\hbar^2}\right)\tilde{\Phi} = 0,
\qquad \Box = \tilde{\nabla}\tilde{\nabla}^{\natural},
$$

the overall sign of $\mathcal{L}$ being immaterial for the equation and fixed here by the positivity of the energy density. Both the action and the equation are those of the read list; $\mathcal{L}$ is exhibited only because a Noether current is read off a Lagrangian.

### Symmetries of the Action and of the Equations

A one-parameter family $\tilde{\Phi}_\varepsilon$ with $\tilde{\Phi}_0 = \tilde{\Phi}$ is a **symmetry of the action** if $S[\tilde{\Phi}_\varepsilon] = S[\tilde{\Phi}]$ for every field configuration, and a **symmetry of the equations of motion** if it preserves the solution set. A symmetry of the action is the stronger notion, and it is the one that yields a conserved current by Noether's theorem.

### The Theorem in the Two Forms the Framework Needs

For an internal symmetry, the theorem states that there is a current biquaternion $\tilde{J} = J_t\,e_t + \sum_k J_k\,\vec e_k$ whose divergence vanishes when the field obeys its equation:

$$
\delta S = 0 \ \text{for all fields}
\qquad\Longrightarrow\qquad
\mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde{J}\right) = 0 \ \text{on shell}.
$$

For a spacetime symmetry, the same construction applied to a transformation that moves the point $\tilde{R}$ yields a current carrying one index per generator: for translations the energy–momentum current, for Lorentz transformations the angular-momentum current. The two forms differ only in what the symmetry variation acts on. The general identity behind both is that the divergence of the current is the field equation contracted with the symmetry variation; it is written out for the central phase in the next section and for translations after that.

## The Current of the Central Phase

### The Symmetry and the Current

Multiplication by a central phase,

$$
\tilde{\Phi}\ \longmapsto\ \exp(i\alpha)\tilde{\Phi},
\qquad \alpha\in\mathbb{R},
$$

leaves both terms of $\mathcal{L}$ unchanged, because $\exp(i\alpha)$ is central and $\tilde{\Phi}^{*}\mapsto \exp(-i\alpha)\tilde{\Phi}^{*}$: the two phase factors in $(\tilde{\nabla}^{\natural}\tilde{\Phi}^{*})(\tilde{\nabla}\tilde{\Phi})$ cancel, and $\tilde{\Phi}^{*}\tilde{\Phi}$ is invariant. The symmetry therefore holds for the **massive** field as well as the massless one, because the mass term depends on $\tilde{\Phi}$ only through the invariant $\tilde{\Phi}^{*}\tilde{\Phi}$ — a fact used again below.

For the infinitesimal variation $\delta\tilde{\Phi} = i\alpha\tilde{\Phi}$, $\delta\tilde{\Phi}^{*} = -i\alpha\tilde{\Phi}^{*}$, Noether's construction gives

$$
J_\nu = \frac{\partial\mathcal{L}}{\partial(\partial\phi/\partial Q_\nu)}\,\delta\phi + \frac{\partial\mathcal{L}}{\partial(\partial\phi^{*}/\partial Q_\nu)}\,\delta\phi^{*}
= i\alpha\left(\frac{\partial\phi^{*}}{\partial Q_\nu}\,\phi - \frac{\partial\phi}{\partial Q_\nu}\,\phi^{*}\right),
$$

the second equality from $\partial\mathcal{L}/\partial(\partial\phi/\partial Q_\nu) = +\partial\phi^{*}/\partial Q_\nu$ and its conjugate, which is what the Lagrangian above supplies. Setting $\alpha = 1$ and packaging the four components,

$$
\boxed{\ \tilde{J} = i\left[(\tilde{\nabla}\tilde{\Phi}^{*})\tilde{\Phi} - \tilde{\Phi}^{*}(\tilde{\nabla}\tilde{\Phi})\right] = \sum_\nu J_\nu e_\nu\ }
\qquad (\tilde{\Phi} = \phi\,e_t).
$$

The overall sign of a current is free — the symmetry with the opposite generator gives the opposite current — and it is fixed here by the charge density, as the next paragraph shows.

### The Current Lies in the Material Sector

The temporal component in the $ict'$ basis is $J_t = i\left(\phi\,\frac{\partial\phi^{*}}{\partial Q_t} - \phi^{*}\frac{\partial\phi}{\partial Q_t}\right)$. Because $\partial/\partial Q_t = -\frac{i}{c}\partial/\partial t'$ and the spatial derivatives are plain, the two kinds of component are recorded separately:

$$
J_t = -\frac{1}{c}\left(\phi^{*}\partial/\partial t'\,\phi - \phi\,\partial/\partial t'\,\phi^{*}\right) = -\frac{2i}{c}\,\mathrm{Im}\!\left(\phi^{*}\frac{\partial\phi}{\partial t'}\right),
$$

which is **purely imaginary**, while the spatial components

$$
J_k = +2\,\mathrm{Im}\!\left(\phi^{*}\frac{\partial\phi}{\partial Q_k}\right)
$$

are real, the $i$ of the current multiplying the $-2i$ of the Wronskian to $+2$. Hence $\tilde{J}\in\mathbb{M}_-$, with imaginary scalar part and real vector part, exactly as the four-current of relativistic mechanics. Writing $J_t = ic\rho$ recovers the parent's convention $\tilde{J} = ic\rho\,e_t + \vec j$, with

$$
\rho = \frac{i}{c^2}\left(\phi^{*}\partial/\partial t'\,\phi - \phi\,\partial/\partial t'\,\phi^{*}\right),
$$

which is real and **positive** on a positive-frequency wave $\phi\propto\exp(i(\vec k\cdot\vec x-\omega t'))$, where it equals $\frac{2\omega}{c^2}|\phi|^2$. This is the sign convention of *The Klein–Gordon Equation in Biquaternionic Form*, and it is what fixes the sign of $\tilde{J}$ above.

### Conservation and the Identity Behind It

Forming the scalar part of $\tilde{\nabla}^{\natural}\tilde{J}$,

$$
\mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde{J}\right) = \sum_\mu\partial/\partial Q_\mu\,J_\mu = \langle\tilde\nabla,\tilde J\rangle_{\natural} ,
$$

the sum being plain, because the signs of $\varepsilon$ are spent inside $\tilde{\nabla}^{\natural}$: on the diagonal $\mathrm{Sc}(e_\mu^{\natural}e_\mu)=1$ for all four $\mu$. Using the definitions and $\Box = \partial^2/\partial Q_t^2 + \Delta$,

$$
\boxed{\ \mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde{J}\right) = i\,\mathrm{Sc}\!\left[(\Box\tilde{\Phi}^{*})\tilde{\Phi} - \tilde{\Phi}^{*}(\Box\tilde{\Phi})\right]\ }
$$

The cross terms of each $\mu$ enter with opposite signs and cancel, so only the second derivatives survive. This is the Noether identity in biquaternion form: the scalar divergence of the current is the Klein–Gordon operator applied to the field, contracted with the symmetry variation. On shell, $\Box\tilde{\Phi} = (m^2c^2/\hbar^2)\tilde{\Phi}$ and the same for the conjugate, both terms become the same real multiple of $\tilde{\Phi}^{*}\tilde{\Phi}$ and cancel, so

$$
\mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde{J}\right) = 0 \quad\text{on shell},
$$

which is the continuity equation $\partial/\partial t'\rho + \mathrm{div}\,\vec j = 0$. The reason the time component needs no separate sign is the same one met above: $\partial/\partial Q_t=-\frac{i}{c}\partial/\partial t'$ meets $J_t=ic\rho$, and $(-i)(i)=+1$ leaves the plain $\partial\rho/\partial t'$ of the continuity equation.

### On What Case This Was Checked

A single plane wave is a trap: for $\tilde{\Phi} = \tilde{\Phi}_0\exp(i\,\mathrm{Sc}(\tilde P\tilde{R}^{\natural}))$ the current is *constant*, so its divergence vanishes whether or not the field is on shell, and the plane wave that suggests the formula cannot test it. The conservation was therefore checked on three other cases:

- **a superposition of on-shell plane waves.** With $c = \hbar = m = 1$ and the momenta $(|\vec k|,\omega) = (0,1)$, $(\tfrac34,\tfrac54)$, $(\tfrac{5}{12},\tfrac{13}{12})$ all satisfying $\omega^2 = \vec k^2 + 1$, and amplitudes $1, \tfrac12, \tfrac13$, the current has non-constant cross terms, and $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J})$ cancels identically;
- **a standing wave**, $\tilde{\Phi} = \sin(kx)\cos(\omega t') + i\sin(kx)\sin(\omega t')$ with $\omega^2 = c^2k^2 + m^2c^4/\hbar^2$: this is on shell and is **not** a plane wave, and again $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J})$ vanishes identically;
- **an off-shell field.** A two-mode field with one mode off shell gives a divergence proportional to the field equation, explicitly nonzero. The identity above was also confirmed on a generic three-mode field, off shell: the difference $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J}) - i\,\mathrm{Sc}[(\Box\tilde{\Phi}^{*})\tilde{\Phi} - \tilde{\Phi}^{*}(\Box\tilde{\Phi})]$ reduces to zero identically, and the divergence is $2\,\mathrm{Im}(\tilde{\Phi}^{*}\Box\tilde{\Phi})$, which is what the identity gives.

The last case is the honest statement of the theorem: the current is conserved **whenever** the field equation holds; off shell it need not be, and its divergence *is* the field equation.

### Relation to the Current Already in the Corpus

*The Klein–Gordon Equation in Biquaternionic Form* posits the current with $\rho = \frac{i\hbar}{2mc^2}(\tilde{\Phi}^*\partial/\partial t'\tilde{\Phi} - \tilde{\Phi}\partial/\partial t'\tilde{\Phi}^*)$ and $\vec j = -\frac{i\hbar}{2m}(\tilde{\Phi}^*\nabla\tilde{\Phi} - \tilde{\Phi}\nabla\tilde{\Phi}^*)$. Comparing component by component, that current equals $+\frac{\hbar}{2m}\tilde{J}$: the Noether derivation reproduces the current the parent states, and fixes the normalization only up to the constant $\frac{\hbar}{2m}$ that a current may always be multiplied by. What the derivation adds is **why** that combination is the conserved one, and that it is forced by the phase symmetry rather than chosen.

**Relation to the Maxwell source.** In the Maxwell article the source conservation is $\sqrt{\mu}\,\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J}) = 0$ with $\tilde J = ic\rho\,e_t + \vec J$. Expanding, $\sqrt{\mu}\,\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J}) = \sqrt{\mu}\,(\partial/\partial t'\rho + \mathrm{div}\,\vec J)$, so the Maxwell integrability condition is the same continuity equation as the conservation of $\tilde{J}$ above. The electric four-current of the material sector is the Noether current of the central phase; the gauge freedom localized in *The Gauge Principle in Biquaternionic Form* is the localization of the symmetry that produces it.

### The Dirac Field: the Pair, the Two-Sided Form, and the Axial Current

The same phase is a symmetry of the massive Dirac field. On the Dirac module the dynamics of the algebra is the **chiral pair**

$$
\begin{aligned}
\tilde\nabla\tilde{\Psi}_R &= m\,\tilde{\Psi}_L,\\[4pt]
\tilde\nabla^{\natural}\tilde{\Psi}_L &= m\,\tilde{\Psi}_R,
\end{aligned}
$$

two equations, one per chirality, each first order and linear in the field, with $m$ central. They are the two lines of one dynamics, not two independent ones: eliminating one half gives the massive Klein–Gordon equation, and at $m=0$ the pair decouples into the two Weyl equations, $\tilde\nabla\tilde\Psi_R=0$ and $\tilde\nabla^{\natural}\tilde\Psi_L=0$, one for each chirality. A central phase passes through both lines, since it passes through the central mass, so the current derived above is the conserved current of the Dirac field at every $m$, and $\langle\tilde\nabla,\tilde J\rangle_{\natural}=0$ on shell for it.

**The two-sided form.** Read on the whole algebra rather than on the module, the same dynamics is one equation in which the derivative acts on the left and the mass on the right,

$$
\tilde\nabla^{\natural}F = m\,\chi\,\bar{F},
\qquad
\chi = -iR_{\vec e_z}^{\mathrm{axf}},
$$

where $\bar{F}$ is the coefficient conjugate and $\chi$ is the **chirality cell**, the right multiplication by $\vec e_z$ carrying the unit that $i^2=-1$ removes. Equivalently the mass term is written with the unit displayed, $-mi\bar{F}\vec e_z$, and the two writings are one identity:

$$
-m\,i\,\bar{F}\,\vec e_z = -m\,(iR_{\vec e_z}^{\mathrm{axf}})\bar{F} = m\,(-iR_{\vec e_z}^{\mathrm{axf}})\bar{F} = m\,\chi\bar{F},
$$

the two imaginary units of the middle expression multiplying to $+1$. This is the operator-theoretic content of the two-sidedness: the derivative acts on the left, the mass on the right, and the conjugation supplies the antilinear part, so the second field of the $\natural$-side equation is the conjugate of the first carried on the right. The one-sided pair is the definition; the two-sided form is the representation in which the mass is a right multiplication and chirality is a cell.

**The currents, in cells.** On the module the central-phase current is the cell bilinear

$$
j_\mu = \bar{\psi}\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}}\,\psi,
\qquad \tau(t)=x,\ \ \tau(k)=y\ \ (k=x,y,z),
$$

the generator cell of the coordinate $x_\mu$ inserted between the field and its bar, $\bar\psi=\psi^{\dagger}iR_{\vec e_x}^{\mathrm{axf}}$. The axial rotation assigns opposite phases to the two chiralities, so the mass term, which pairs them, is not invariant under it; the axial current therefore carries the chirality cell,

$$
j_{5\mu} = \bar{\psi}\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}}\,\chi\,\psi
= \bar{\psi}\,L_{e_\mu}^{\mathrm{axf}}R_{\vec e_z\vec e_{\tau(\mu)}}^{\mathrm{axf}}\,\psi ,
$$

where the two imaginary units meet and reduce by $i\cdot(-i)=+1$. The surviving right multiplier is the product $\vec e_z\vec e_{\tau(\mu)}$ in that order, and it is not symmetric: writing the pair the other way round flips the sign of the current. The divergence is the **plain** sum of the four derivatives, since the $\natural$ in $\langle\tilde\nabla,\tilde J_5\rangle_{\natural}$ already carries the relative sign of the spatial derivatives and no metric is applied a second time; the mass is the obstruction:

$$
\langle\tilde\nabla,\tilde J_5\rangle_{\natural} = \sum_\mu\frac{\partial j_{5\mu}}{\partial Q_\mu} = 2im\,\bar{\psi}\,\chi\,\psi ,
$$

which vanishes only at $m=0$. The same statement without the cells: the axial rotation is generated by the chirality itself, $\psi\mapsto\exp(i\alpha\chi)\psi$, and $i\chi=i(-iR_{\vec e_z}^{\mathrm{axf}})=R_{\vec e_z}^{\mathrm{axf}}$, so the exponential is a right multiplication,

$$
\exp(i\alpha\chi)\psi = \psi\,\exp(\alpha\vec e_z) = \cos\alpha\,\psi+\sin\alpha\,\psi\vec e_z ,
$$

two imaginary units reducing to one real parameter and one right multiplier. That is why the axial current carries the chirality cell and not a separate object.

**What the mass breaks, and what it does not.** What the mass term breaks is the **axial** symmetry, not the phase. The two chiralities are rotated against each other by the central grading $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$, where $\tilde\Xi_{\mathrm{ad}}$ is the adjoined central root of $-e_t$, so $\tilde\Xi_{\mathrm{ad}}^2=-e_t$ and

$$
\chi_{\mathrm{ad}}^2 = i^2\tilde\Xi_{\mathrm{ad}}^2 = (-1)(-e_t) = e_t ,
$$

the two minus signs of the $i^2$ and of the root cancelling. The grading is not an element of $\mathbb{B}$; it acts on the module as a sign, of which the chirality cell $\chi=-iR_{\vec e_z}^{\mathrm{axf}}$ is the representative. In the biquaternion interpretation the mass term is the off-diagonal coupling between the two *central* ideals of $\mathbb{B}$ — the two chiralities — so it breaks exactly the symmetry that rotates them, and not the central $\mathrm{U}(1)$ that the algebra canonically carries. The previously recorded obstruction belonged to the retired antilinear single-field equation; the gauge principle article's corresponding section is revised on the same grounds.

## Translation Invariance and the Conserved Four-Momentum

### The Particle Charge

The action $S[\tilde{R}]$ above depends on $\tilde{R}$ only through $d\tilde{R}$, so the constant shift

$$
\tilde{R}\ \longmapsto\ \tilde{R} + \tilde{R}_0,
\qquad \tilde{R}_0\in\mathbb{M}_-\ \text{constant},
$$

is a symmetry of the action. The Noether charges are the momentum conjugate to $x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ and the energy conjugate to $t'$; computing the first from the Lagrangian,

$$
\vec p = \frac{\partial \mathrm{Lag}}{\partial\vec v} = \gamma m\vec v,
\qquad
E = \vec p\cdot\vec v - \mathrm{Lag} = \gamma mc^2,
$$

and combining them into the four-momentum,

$$
\boxed{\ \tilde{P} = m\tilde{V} = i\frac{E}{c}\,e_t + \vec p\ }
\qquad (\tilde{V} = \gamma(ic\,e_t + \vec v)).
$$

The mass-shell relation $\tilde{P}\tilde{P}^{\natural} = -m^2c^2$ follows, since $\tilde{P}\tilde{P}^{\natural}=-(E/c)^2+\vec p^{\,2}$ and $E^2=\vec p^{\,2}c^2+m^2c^4$. Translation invariance is thus the symmetry whose Noether charge is the four-momentum; the four-momentum is conserved for a free particle, $d\tilde{P}/d\tau = 0$, because $\mathrm{Lag}$ has no explicit $\tilde{Q}$-dependence. As an independent check, a particle with $m = c = 1$, $\vec p = (0.6,0,0)$ and $E = \sqrt{1.36}$ was boosted by the rotor $\tilde U = \cosh(\psi/2) + i\sinh(\psi/2)\vec e_x$ with $\psi = 1.2$, the conjugation being $\tilde U\tilde P\tilde U^{*}$: the result is $E' = 1.206$ and $p'_x = -0.674$, which are the component formulas $E'=\cosh\psi\,E-\sinh\psi\,p_x$ and $p'_x=\cosh\psi\,p_x-\sinh\psi\,E$, and the biquaternion norm is $-1$ in both frames, confirming that the Noether charge transforms as a four-vector.

### The Conservation Law for a System, Stated Correctly

For an isolated system of bodies $a$ the conserved object is the **total** four-momentum, and the correct statement is

$$
\boxed{\;\tilde{P}_{\mathrm{tot}} = \sum_a \tilde{P}_a,
\qquad
\frac{d\tilde{P}_{\mathrm{tot}}}{dt'} = 0\;},
$$

a vanishing **coordinate**-time derivative. The parent defines the four-force by the **proper**-time derivative of a single body, $\tilde{K}_{\mathrm{f},a} = d\tilde{P}_a/d\tau_a$, and since $d\tau_a = dt'/\gamma_a$,

$$
\frac{d\tilde{P}_a}{dt'} = \frac{1}{\gamma_a}\tilde{K}_{\mathrm{f},a},
\qquad\text{so}\qquad
\sum_a \tilde{K}_{\mathrm{f},a} = \sum_a \gamma_a\frac{d\tilde{P}_a}{dt'},
$$

which equals $d\tilde{P}_{\mathrm{tot}}/dt'$ only when all the $\gamma_a$ are equal. The parent's symbol $\tilde{K}_{\mathrm{f}}$ is a per-body proper-time rate and cannot be summed across bodies. The conservation law in terms of the parent's four-forces is therefore

$$
\sum_a \frac{1}{\gamma_a}\tilde{K}_{\mathrm{f},a} = \frac{d\tilde{P}_{\mathrm{tot}}}{dt'} = 0,
$$

or, in the integrated form that avoids the derivative altogether, $\sum_{\mathrm{in}}\tilde{P} = \sum_{\mathrm{out}}\tilde{P}$ for a collision. The exercise reports this defect; the corrected statement above is the one to use.

**A numerical witness.** Two bodies connected by a translation-invariant interaction exchange momentum, so at some instant $d\tilde{P}_2/dt' = -d\tilde{P}_1/dt' = i\,e_t + \vec e_x$, and their Lorentz factors differ, $\gamma_1 = 5/3$, $\gamma_2 = 5/4$. Then $d\tilde{P}_{\mathrm{tot}}/dt' = 0$, but

$$
\tilde{K}_{\mathrm{f},1} + \tilde{K}_{\mathrm{f},2} = (\gamma_2 - \gamma_1)\left(i\,e_t + \vec e_x\right) = -\frac{5}{12}\left(i\,e_t + \vec e_x\right) \neq 0 .
$$

The naive sum of the parent's four-forces is not zero even though the total four-momentum is conserved. For the collision of *Exercise: Four-Momentum Conservation in a Collision* ($E_1 = 3mc^2$, equal masses, $\theta^* = 90^\circ$), the total four-momenta $\tilde{P}_{\mathrm{in}}$ and $\tilde{P}_{\mathrm{out}}$ were recomputed and agree component by component in the laboratory.

### What Translation Does to a Plane Wave

A free field is a plane wave, and a translation acts on it by a central phase. With the series' phase convention $\tilde{\Phi} = \tilde{\Phi}_0\exp(i\,\mathrm{Sc}(\tilde P\tilde{R}^{\natural}))$, whose phase is $\mathrm{Sc}(\tilde P\tilde{R}^{\natural}) = \vec k\cdot\vec x-\omega t'$, and with $\tilde P\in\mathbb{M}_-$ and $\tilde{R}\mapsto\tilde{R}+\tilde{R}_0$,

$$
\tilde{\Phi}\big|_{\tilde{R}+\tilde{R}_0} = \exp\!\bigl(i\,\mathrm{Sc}(\tilde P\tilde{R}_0^{\natural})\bigr)\,\tilde{\Phi}\big|_{\tilde{R}},
\qquad
\tilde{\Phi}_0\ \text{constant}.
$$

The multiplier is **central and of unit modulus**, because $\mathrm{Sc}(\tilde P\tilde{R}_0^{\natural}) = \langle\tilde P,\tilde{R}_0\rangle_{\natural}$ is real: writing $\tilde P = i\frac{\omega}{c}e_t + \vec k$ and $\tilde{R}_0 = i R_{0t} e_t + \vec R_0$, with $R_{0t} = ct'_0$,

$$
\mathrm{Sc}\!\left(\tilde P\tilde{R}_0^{\natural}\right) = -\frac{\omega R_{0t}}{c} + \vec k\cdot\vec R_0 = \vec k\cdot\vec R_0-\omega t'_0 .
$$

What makes it a phase is the $i$: the same scalar in a real exponential is a dilation. For $\tilde P = 2i\,e_t + 0.7\vec e_x - 0.3\vec e_y + 0.5\vec e_z$ and $\tilde{R}_0 = 0.4i\,e_t + 0.25\vec e_x - 0.35\vec e_y + 0.15\vec e_z$ (units $c = 1$), $\mathrm{Sc}(\tilde P\tilde{R}_0^{\natural}) = -0.445$ and the multiplier is $\exp(-0.445i)$, of modulus $1$, whereas $\exp(\mathrm{Sc}(\tilde P\tilde{R}_0^{\natural})) = e^{-0.445}$ has modulus $0.641$. The $\natural$ inside the pairing must be the one the wave itself carries; the un-conjugated $\mathrm{Sc}(\tilde P\tilde{R}_0) = -\frac{\omega R_{0t}}{c}-\vec k\cdot\vec R_0$ belongs to the opposite sign convention for $\vec k$ in the phase, and mixing the two flips the sign of $\vec k\cdot\vec R_0$ alone. This central phase is the finite, field-space form of the translation subgroup; its infinitesimal generator is the derivation $\partial/\partial Q_\mu$, and it is not a rotor, as *The Poincaré Group and the Biquaternion Frame* establishes.

## The Energy–Momentum of the Field

### The Canonical Tensor

The same translation symmetry applied to the field action gives the **canonical energy–momentum**, the Noether current of spacetime translations. For the complex scalar field it is

$$
\boxed{\;T_{\mu\nu} = \frac{\partial\phi^*}{\partial x_\mu}\frac{\partial\phi}{\partial x_\nu} + \frac{\partial\phi}{\partial x_\mu}\frac{\partial\phi^*}{\partial x_\nu} - g_{\mu\nu}[\mathbb{M}_-]\,\mathcal{L}_\phi\;}
$$

with the scalar Lagrangian of the same frame,

$$
\mathcal{L}_\phi = \sum_{\mu,\nu}g^{\mu\nu}[\mathbb{M}_-]\frac{\partial\phi^*}{\partial x_\mu}\frac{\partial\phi}{\partial x_\nu} + \frac{m^2c^2}{\hbar^2}|\phi|^2
= -\frac{1}{c^2}\left|\frac{\partial\phi}{\partial t'}\right|^2 + |\nabla\phi|^2 + \frac{m^2c^2}{\hbar^2}|\phi|^2 .
$$

Here $x_\mu=(ct',x,y,z)$ is the real frame with $g_{\mu\nu}[\mathbb{M}_-]$, distinct from the $Q_\mu$ frame of the gradient: $Q_0=ict'$ carries the $i$, while $x_0=ct'$ does not. Both indices of $T$ are low, the first the row; the derivative index of the conservation law is contracted with $g_{\mu\mu}[\mathbb{M}_-]$, and it is $g_{\mu\mu}[\mathbb{M}_-]=(-1,+1,+1,+1)=-\varepsilon_\mu$ that carries the signs, not $\varepsilon$, because the $i^2$ of the time coordinate has already been spent once in $\eta$. Translation invariance gives

$$
\sum_\mug_{\mu\mu}[\mathbb{M}_-]\frac{\partial T_{\mu\nu}}{\partial x_\mu} = 0
$$

on shell. Its time–time component is the energy density,

$$
T_{00} = \frac{1}{c^2}\left|\frac{\partial\phi}{\partial t'}\right|^2 + |\nabla\phi|^2 + \frac{m^2c^2}{\hbar^2}|\phi|^2 > 0,
$$

positive for every configuration because each term is a square. This was checked by recomputation on an on-shell superposition of two plane waves: the four divergences $\sum_\mug_{\mu\mu}[\mathbb{M}_-]\partial T_{\mu\nu}/\partial x_\mu$ vanish to $10^{-10}$, the tensor is symmetric, and $T_{00}$ equals the expression above.

### Why the Framework Does Not Write It as One Biquaternion

A symmetric rank-two tensor in four dimensions has ten independent components, while a biquaternion has four complex coefficients, that is eight real components, and $\tilde{W} = \tfrac12\tilde{F}\tilde{F}^{*}$ carries only four of them. So no single biquaternion can be $T_{\mu\nu}$; the framework writes the translation current as a **bigeneral quaternionic bilinear**, one basis element for each index. *Exercise: The Electromagnetic Energy–Momentum Tensor* constructs exactly this for the Maxwell field, $\Pi_{\mu\nu} = \tfrac12\mathrm{Sc}(\tilde{F}\mathcal{E}_\mu\tilde{F}^{*}\mathcal{E}_\nu)$ with the first index the row, and shows that the four-component object is its time row. The framework's energy–momentum biquaternion is therefore not the whole Noether current of translations; it is the energy–flux part of it.

### The Maxwell Case in the Corpus Form

For the electromagnetic field the four-component object is $\tilde{W} = \tfrac12\tilde{F}\tilde{F}^{*} = W\,e_t + \frac{i}{c}\vec S\in\mathbb{M}_+$, with $W$ the energy density and $\vec S = \vec E\times\vec H$ the Poynting vector. Its scalar divergence is the energy law,

$$
\mathrm{Sc}\!\left(\tilde{\nabla}\tilde{W}\right) = -\frac{i}{c}\left(\frac{\partial W}{\partial t'}+\mathrm{div}\,\vec S\right) = \frac{i}{c}\,\vec J\cdot\vec E ,
$$

the last equality being the Poynting theorem. The factor $i$ is uniform across the two terms, as a temporal component must be in the $ict'$ convention, and dividing it out recovers $\partial W/\partial t' + \mathrm{div}\,\vec S + \vec J\cdot\vec E = 0$. The real form $\tilde W = W + \frac{1}{c}\vec S$ fails exactly this test: its scalar divergence carries the $i$ on the time term only, and on a free plane wave it equals $\frac{1-i}{c}\partial W/\partial t'$, which is not zero. What *Exercise: The Electromagnetic Energy–Momentum Tensor* isolates is that factor $i$ on the Poynting part, and the equation $\tilde{\nabla}\tilde{W} = -\tilde{\mathcal F}$, taken as a biquaternion identity with a power–force density on the right, is not what the corpus establishes for either form: what it verifies is the scalar statement above, not the vector one. Read as a Noether statement, $\mathrm{Sc}(\tilde{\nabla}\tilde{W}) = \frac{i}{c}\vec J\cdot\vec E$ says the translation current is conserved up to the work done on the charges — the source is present, so the field alone is not closed.

### A Caution on the $ict'$ Convention

The energy density is not $\mathcal{L}_\phi$ and is not obtained from it by a flat sum: $T_{00}=\frac{1}{c^2}|\dot\phi|^2+|\nabla\phi|^2+\mu^2|\phi|^2$ while $\mathcal{L}_\phi=-\frac{1}{c^2}|\dot\phi|^2+|\nabla\phi|^2+\mu^2|\phi|^2$, with $\mu=mc/\hbar$. The gradient and $\Box$ live in the $Q_\mu$ frame, where $Q_0=ict'$; the tensor lives in $x_\mu=(ct',x,y,z)$, where the time component is real and the metric signs sit in $\eta$. Mixing the two frames produces the wrong sign on the time derivative, and the mismatch is the same $(-i)^2=-1$ that makes the time term of the uniform $Q$-frame sum of $\mathcal{L}$ negative once written in the real frame. This is the same caution the energy–momentum exercise records for the trace.

## Lorentz Invariance and the Angular-Momentum Bivector

### The Particle Bivector

Lorentz invariance is a spacetime symmetry like translation, and it has a Noether current too. For a free particle the conserved quantity is the antisymmetric pair

$$
L_{\mu\nu} = x_\mu p_\nu - x_\nu p_\mu,
\qquad
\frac{dL_{\mu\nu}}{d\tau} = \frac{dx_\mu}{d\tau}p_\nu - \frac{dx_\nu}{d\tau}p_\mu = \frac{p_\mu p_\nu-p_\nu p_\mu}{m} = 0,
$$

using $dx_\mu/d\tau = p_\mu/m$ and $dp_\mu/d\tau = 0$ for a free particle; the conservation of the six independent components is the conservation of angular momentum and of the boost charges. In the biquaternion algebra the antisymmetric pair is a **bivector**, the same representation the field strength occupies: writing

$$
\boxed{\;\tilde L = \tfrac12\sum_{\mu,\nu}L_{\mu\nu}\,e^{\natural}_\mu e_\nu\;}
$$

the angular momentum of a free particle is a single biquaternion. The tilde rather than an arrow is deliberate: the vector part of $\tilde L$ is $L_{0k}-\tfrac12\epsilon_{kij}L_{ij}$ along $\vec e_k$, which pairs the boost charges with $\vec r\times\vec p$ and is not the three-vector of orbital angular momentum. This is the same construction by which $\tilde{F} = \mathrm{Vect}(\tilde{\nabla}^{\natural}\tilde{A}) = \tfrac12\sum_{\mu\nu}F_{\mu\nu}e^{\natural}_\mu e_\nu$ packages the antisymmetric field strength, and the Lorentz generators themselves are bivectors.

### The Rank-Three Field Current

For a field, the Noether current of Lorentz invariance is a rank-three object,

$$
L_{\mu\nu\rho} = x_\nu T_{\mu\rho} - x_\rho T_{\mu\nu} + S_{\mu\nu\rho},
$$

whose conservation

$$
\sum_\mug_{\mu\mu}[\mathbb{M}_-]\frac{\partial L_{\mu\nu\rho}}{\partial x_\mu} = 0
$$

expresses the symmetry of the energy–momentum tensor together with the conservation of spin. Being rank three, it is not a biquaternion and not even a single bilinear; the orbital and spin pieces separate, with the spin term vanishing for the classical scalar field. The particle bivector $\tilde L$ above is the finite-dimensional case where the rank-two object *is* the whole story.

## What Is Inherited, What Is Added, What Is Interpretation

**Inherited and unchanged.** The action, the four-momentum, the four-current and its conservation $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J}) = 0$, the algebra, the gradient, the sectors, and the trace formula, for a state $\tilde{Ϛ}$ and a Hermitian observable $\tilde H$, $\mathrm{Tr}(\tilde{Ϛ}\tilde H^{*})=\mathrm{Tr}(\tilde{Ϛ}\tilde H)=2\langle\tilde{Ϛ},\tilde H\rangle_{*} = 2\,\mathrm{Sc}(\tilde{Ϛ}\tilde H^{*})$ are those of the read list. No symbol is renamed, the sign of the current is the one for which $\rho>0$ on a positive-frequency wave, and what this article adds to the list is derivation and identification, not new definitions.

**Added by this article.** The derivation of the central-phase current $\tilde{J} = i[(\tilde{\nabla}\tilde{\Phi}^{*})\tilde{\Phi} - \tilde{\Phi}^{*}\tilde{\nabla}\tilde{\Phi}]$ from the phase symmetry of the field action, and its conservation identity; its cell form $j_\mu=\bar\psi\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}}\psi$ on the Dirac module, with the axial current and the chirality cell; the identification of the free-particle four-momentum as the Noether charge of translation invariance, with the corrected multi-body statement; the explicit translation multiplier $\exp(i\,\mathrm{Sc}(\tilde P\tilde{R}_0^{\natural}))$; the energy–momentum current and its packaging; and the angular-momentum bivector. These are transcriptions of the standard theorem into the algebra, with the subspace assignments the algebra supplies, not new physics.

**Only transcribed.** Noether's theorem itself is standard; the algebra does not produce a symmetry that the action did not already have, nor a conservation law beyond those the symmetries give. The framework supplies the home of each conserved object — the current in $\mathbb{M}_-$, the energy–momentum in the bilinear and its time row in $\mathbb{M}_+$ for Maxwell, the angular momentum in the bivector — and it makes the divergence identities compact. It does not supply the symmetries, the coupling constants, or the masses.

**Interpretation.** Reading the conserved currents as the physical four-current and energy–momentum is the standard interpretation, not an extra postulate; the biquaternion packaging is a representation-theoretic statement about which subspace carries which object, and it is exact. What remains interpretation is the physical hypothesis attached to the two sectors, which is the program's, not this article's.

## Open Questions

1. **The biquaternion form of the full translation current.** The energy–momentum tensor is rank two and cannot be one biquaternion. Is there a natural biquaternion-bilinear expression for the canonical $T_{\mu\nu}$ of a general biquaternion field, beyond the Maxwell case constructed in the energy–momentum exercise?

2. **Spin and the angular momentum of fields.** The rank-three Lorentz current carries a spin term. Can the spin density of a biquaternion field be written as a single algebra-valued object, and how does it relate to the bivector representation of angular momentum?

3. **Scale and conformal symmetry.** The massless Klein–Gordon and Maxwell actions have more symmetries than the Poincaré group. Do they have biquaternion Noether currents, and does the tracelessness of the electromagnetic energy–momentum tensor — established in the energy–momentum exercise — express one of them?

4. **The axial current and the two central ideals.** With the linear mass term the vector phase current is conserved for the massive field, so the open question is the axial one. The divergence identity $\sum_\mu\partial j_{5\mu}/\partial Q_\mu = 2im\,\bar{\psi}\chi\psi$ holds for the chiral pair, and its biquaternion interpretation is that the mass couples the two central ideals of $\mathbb{B}$ off-diagonally. Is there a Noether derivation that starts from the axial rotation $\psi\mapsto\exp(i\alpha\chi)\psi$ rather than from the pair — and does the central-element structure supply anything analogous to the would-be Goldstone statement?

5. **The current of the complexified theory.** In the complexified biquaternion theory of the Maxwell article, the source and potential are fully complex. Does the central-phase current acquire components outside $\mathbb{M}_-$, and are they conserved?

6. **Empirical content.** As everywhere in the framework, the currents derived here are the standard ones in new notation. Whether the biquaternion packaging imposes any constraint that the four-vector formulation does not is not established here.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. The two-sided cells act on the module by $L_a\psi=a\psi$ and $R_b\psi=\psi b$, with $L_aR_bL_cR_d=L_{ac}R_{db}$, and the frame of the article is

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad
\gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad
\gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

**The body's cells under their gamma names.** Because $L_{e_t}^{\mathrm{pau}}$ is the identity, $\gamma_5=-iR_{\vec e_z}^{\mathrm{pau}}$: the chirality cell of the body is the gamma-five cell itself. The generator cell of the coordinate $x_\mu$ is $\gamma_\mu$, so the vector current of the body is $\bar\psi\gamma_\mu\psi$, and the Dirac bar is $\psi^{\dagger}\gamma_0$, since $\gamma_0=iR_{\vec e_x}^{\mathrm{pau}}$. The axial current's cell is a product of two frame cells, and the reduction $i\cdot(-i)=+1$ of the body is exactly that product:

$$
\bigl(iL_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\tau(\mu)}}^{\mathrm{pau}}\bigr)\bigl(-iR_{\vec e_z}^{\mathrm{pau}}\bigr)
= L_{e_\mu}^{\mathrm{pau}}R_{\vec e_z\vec e_{\tau(\mu)}}^{\mathrm{pau}}
= \gamma_\mu\gamma_5 ,
$$

In the axis-free display:

$$
\bigl(iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}}\bigr)\bigl(-iR_{\vec e_z}^{\mathrm{axf}}\bigr)
= L_{e_\mu}^{\mathrm{axf}}R_{\vec e_z\vec e_{\tau(\mu)}}^{\mathrm{axf}}
= \gamma_\mu\gamma_5 ,
$$

so the two imaginary units the body cancels are the two that the gamma names carry, and $j_{5\mu}=\bar\psi\gamma_\mu\gamma_5\psi$. The single collapse behind it, and behind every simplification of the frame, is

$$
i\,\gamma_\mu = -L_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\tau(\mu)}}^{\mathrm{pau}} ,
$$

The same identities in the axis-free display:

$$
i\,\gamma_\mu = -L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}} ,
$$

by $i^2=-1$: multiplying a generator cell by $i$ trades it for a plain one, which is why a product of four generator cells carries $i^4=+1$ and no residual unit. Under the same identity the mass term of the two-sided equation, $-mi\,\bar F\vec e_z$ in the body, is $m\,\bar F\gamma_5$ in the frame: right multiplication by $\vec e_z$ is the cell $i\gamma_5$, so $(-mi)(i\gamma_5)\bar F=-m\,i^2\gamma_5\bar F=+m\,\gamma_5\bar F$.

**The central grading.** The cell $\gamma_5$ is not the grading itself. The central grading $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, with $\tilde\Xi_{\mathrm{ad}}^2=-e_t$ and so $\chi_{\mathrm{ad}}^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module. That is how the two Dirac equations meet: the one-sided pair carries $\chi_{\mathrm{ad}}$ as a central sign, while the mass of the two-sided equation is a right multiplication by the chirality cell, and the cell is the representative of the sign on the module.

**The identities of the frame.** With $\varepsilon=(1,-1,-1,-1)$,

$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,
\qquad
(\gamma_k)^2=-I_4,
\qquad
\gamma_5^2=I_4,
\qquad
\{\gamma_\mu,\gamma_5\}=0 ,
$$

the anticommutation with $\gamma_5$ being what makes the chirality cell the axial insertion. The first relation is the quaternion multiplication table in the frame: a cell that pairs $e_t$ with a spatial unit squares to the square of that unit, and the central $i$ of each generator flips the sign, so the timelike cell squares to $+I_4$ and the three spatial ones to $-I_4$. The frame's metric is $g=-\eta$, and the reason is again $i^2$: each $\gamma_\mu$ is $i$ times the plain cell $L_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\tau(\mu)}}^{\mathrm{pau}}$, whose own Clifford bracket is $2g_{\mu\nu}[\mathbb{M}_-]I_4$, so the two factors of $i$ inside the bracket turn $2\eta$ into $-2\eta$.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the plain cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$, the two Clifford algebras that differ by that relative $i$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

Noether's theorem in biquaternionic form joins the two ends that *Relativistic Mechanics in Biquaternionic Form* states separately, the free-particle action and the conserved four-current, by deriving the second from the first. The theorem has two forms. For an **internal** symmetry, that of the central phase $\tilde{\Phi}\mapsto \exp(i\alpha)\tilde{\Phi}$ of the complex biquaternion scalar field, the derived current is

$$
\tilde{J} = i\left[(\tilde{\nabla}\tilde{\Phi}^{*})\tilde{\Phi} - \tilde{\Phi}^{*}(\tilde{\nabla}\tilde{\Phi})\right] = \sum_\nu J_\nu e_\nu,
\qquad J_\nu = i\left(\phi\,\partial/\partial Q_\nu\,\phi^{*} - \phi^{*}\partial/\partial Q_\nu\,\phi\right),
$$

which lies in $\mathbb{M}_-$ and satisfies the Noether identity

$$
\mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde{J}\right) = i\,\mathrm{Sc}\!\left[(\Box\tilde{\Phi}^{*})\tilde{\Phi} - \tilde{\Phi}^{*}(\Box\tilde{\Phi})\right],
$$

zero whenever the field is on shell. This is the framework form of $\langle\tilde\nabla,\tilde J\rangle_{\natural} = 0$; it reproduces the current the Klein–Gordon article posits, up to the conventional constant $\hbar/2m$, with $\rho>0$ on a positive-frequency wave; and its expansion at the Maxwell source is the charge-conservation condition $\mathrm{Sc}(\tilde{\nabla}^{\natural}\sqrt{\mu}\,\tilde{J}) = 0$.

The same phase acts on the Dirac field, whose dynamics is the chiral pair $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$, $\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R$, equivalently the two-sided equation $\tilde\nabla^{\natural}F=m\chi\bar F$ with the chirality cell $\chi=-iR_{\vec e_z}^{\mathrm{axf}}$. Read on the module the vector current is the cell bilinear $j_\mu=\bar{\psi}\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}}\,\psi$, conserved at every $m$; the axial current carries the chirality cell and obeys $\sum_\mu\partial j_{5\mu}/\partial Q_\mu = 2im\,\bar\psi\chi\psi$, vanishing only at $m=0$. The mass therefore breaks the axial rotation and not the phase.

For a **spacetime** symmetry, translation invariance gives the four-momentum

$$
\tilde{P} = m\tilde{V} = i\frac{E}{c}e_t + \vec p,
\qquad E = \gamma mc^2,\quad \vec p = \gamma m\vec v,
$$

as the Noether charge, conserved for a free particle. The conservation law for a system is the vanishing of the **coordinate**-time derivative of the total, $d\tilde{P}_{\mathrm{tot}}/dt' = 0$; the parent's proper-time four-force cannot be summed across bodies, and the correct form is $\sum_a\tilde{K}_{\mathrm{f},a}/\gamma_a = 0$, or the integrated $\sum_{\mathrm{in}}\tilde{P} = \sum_{\mathrm{out}}\tilde{P}$. A translation acts on a plane wave by the central unit-modulus phase $\exp(i\,\mathrm{Sc}(\tilde P\tilde R_0^{\natural}))$, with $\mathrm{Sc}(\tilde P\tilde R_0^{\natural}) = \vec k\cdot\vec R_0-\omega t'_0$.

The field translation current is the canonical energy–momentum, $\sum_\mug_{\mu\mu}[\mathbb{M}_-]\partial T_{\mu\nu}/\partial x_\mu = 0$ on shell in the real frame, with positive energy density $T_{00} = \frac{1}{c^2}|\partial\phi/\partial t'|^2 + |\nabla\phi|^2 + \frac{m^2c^2}{\hbar^2}|\phi|^2$. Rank two cannot be one biquaternion, so the framework packages it bilinearly; the Maxwell object $\tilde{W} = \tfrac12\tilde{F}\tilde{F}^{*}$ is its time row, and $\mathrm{Sc}(\tilde{\nabla}\tilde{W}) = \frac{i}{c}\vec J\cdot\vec E$ is the energy law it carries. Lorentz invariance gives the angular-momentum bivector $\tilde L = \tfrac12\sum L_{\mu\nu}\,e^{\natural}_\mu e_\nu$, with the rank-three field current reduced to the rank-two particle bivector only when the spin term vanishes. The theorem is standard; the algebra supplies the home of each conserved object and the compact form of its divergence, and it supplies no conservation law the symmetries did not already give.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$; $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$, $\varepsilon=(1,-1,-1,-1)$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}, \mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ | Real-quaternion subspace; complex scalar line (the centre) |
| $\tilde{\nabla} = e_t\partial/\partial Q_t + \sum_\mu\,\vec e_\mu\,\partial/\partial Q_\mu$ | Biquaternionic gradient |
| $\tilde{\nabla}^{\natural} = e_t\partial/\partial Q_t - \sum_\mu\,\vec e_\mu\,\partial/\partial Q_\mu$ | Quaternion-conjugate gradient; $\mathrm{Sc}(e_\mu^{\natural}e_\nu)=\delta_{\mu\nu}$ |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \partial^2/\partial Q_t^2 + \Delta$ | d'Alembertian, $Q_t=ict'$ |
| $S = -mc\int\sqrt{-d\tilde{R}\,d\tilde{R}^{\natural}}$ | Free-particle action |
| $\mathrm{Lag} = -mc^2\sqrt{1-\vec v^2/c^2}$ | Free-particle Lagrangian |
| $\tilde{R} = ic\,t'\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ | Four-position, in $\mathbb{M}_-$ |
| $\tilde{R}_0\in\mathbb{M}_-$ | Constant translation (displacement) |
| $\tilde{V} = \gamma(ic\,e_t + \vec v)$ | Four-velocity, $\tilde{V}\tilde{V}^{\natural} = -c^2$ |
| $\tilde{P} = m\tilde{V} = iE/c\,e_t + \vec p$ | Four-momentum, Noether charge of translation; real energy and momentum, so in $\mathbb{M}_-$ |
| $\tilde{K}_{\mathrm{f},a} = d\tilde{P}_a/d\tau_a$ | Four-force (proper-time derivative; not summable) |
| $\tilde{\Phi} = \phi\,e_t\in\mathbb{C}_{\mathbb{B}}$ | Complex biquaternion scalar field |
| $\mathcal{L} = \sum_\mu(\partial\phi^{*}/\partial Q_\mu)(\partial\phi/\partial Q_\mu) + \frac{m^2c^2}{\hbar^2}|\phi|^2$ | Field Lagrangian density, $Q$ frame |
| $\tilde{J} = i[(\tilde{\nabla}\tilde{\Phi}^{*})\tilde{\Phi} - \tilde{\Phi}^{*}\tilde{\nabla}\tilde{\Phi}]$ | Central-phase Noether current, in $\mathbb{M}_-$ |
| $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J}) = \langle\tilde\nabla,\tilde J\rangle_{\natural} = \sum_\mu\partial J_\mu/\partial Q_\mu$ | Divergence of the current, plain sum |
| $\tilde J = ic\rho\,e_t + \vec J$ | Maxwell source $\sqrt{\mu}\,\tilde J$; $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J}) = 0$ is charge conservation |
| $L_aR_b\psi=a\psi b$ | The two-sided cells; $L_aR_bL_cR_d=L_{ac}R_{db}$ |
| $\chi=-iR_{\vec e_z}^{\mathrm{axf}}$ | The chirality cell |
| $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$, $\tilde\Xi_{\mathrm{ad}}^2=-e_t$, $\chi_{\mathrm{ad}}^2=e_t$ | The central grading (axial generator); not an element of $\mathbb{B}$, represented by $\chi$ on the module |
| $\bar\psi=\psi^{\dagger}iR_{\vec e_x}^{\mathrm{axf}}$ | The Dirac bar |
| $j_\mu=\bar\psi\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}}\psi$, $\tau(t)=x$, $\tau(k)=y$ | Vector current on the module |
| $j_{5\mu}=\bar\psi\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\tau(\mu)}}^{\mathrm{axf}}\chi\,\psi=\bar\psi\,L_{e_\mu}^{\mathrm{axf}}R_{\vec e_z\vec e_{\tau(\mu)}}^{\mathrm{axf}}\psi$ | Axial current; $\sum_\mu\partial j_{5\mu}/\partial Q_\mu=2im\bar\psi\chi\psi$ |
| $x_\mu = (ct',x,y,z)$, $g_{\mu\nu}[\mathbb{M}_-]$ | Real frame of the energy–momentum tensor, distinct from $Q_\mu$; $g_{\mu\mu}[\mathbb{M}_-]=-\varepsilon_\mu$ |
| $T_{\mu\nu} = (\partial\phi^*/\partial x_\mu)(\partial\phi/\partial x_\nu) + (\partial\phi/\partial x_\mu)(\partial\phi^*/\partial x_\nu) - g_{\mu\nu}[\mathbb{M}_-]\mathcal{L}_\phi$ | Canonical energy–momentum, real frame |
| $\tilde{W} = \tfrac12\tilde{F}\tilde{F}^{*} = W\,e_t + \frac{i}{c}\vec S$ | Maxwell energy–momentum (time row), in $\mathbb{M}_+$; $\mathrm{Sc}(\tilde\nabla\tilde W)=\frac{i}{c}\vec J\cdot\vec E$ |
| $L_{\mu\nu} = x_\mu p_\nu - x_\nu p_\mu$, $\tilde L = \tfrac12\sum L_{\mu\nu}\,e^{\natural}_\mu e_\nu$ | Angular momentum and its bivector |
| $\tilde P = i\frac{\omega}{c}e_t + \vec k$ | Four-wavevector, in $\mathbb{M}_-$; plane-wave phase $\mathrm{Sc}(\tilde P\tilde R^{\natural}) = \vec k\cdot\vec x-\omega t'$ |
| $\exp(i\,\mathrm{Sc}(\tilde P\tilde{R}_0^{\natural}))$, $\mathrm{Sc}(\tilde P\tilde R_0^{\natural})=\vec k\cdot\vec R_0-\omega t'_0$ | Central translation multiplier on a plane wave, of unit modulus |
| $\operatorname{Tr}(\tilde{Ϛ}\tilde H^{*})=\operatorname{Tr}(\tilde{Ϛ}\tilde H)=2\langle\tilde{Ϛ},\tilde H\rangle_{*} = 2\,\mathrm{Sc}(\tilde{Ϛ}\tilde H^{*})$ | Trace formula of the informational sector, $\tilde H$ Hermitian |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle=\varepsilon_\mu Q_{1\mu}Q_{2\mu}$ | the general plain bilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2)$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{\natural}=\langle\tilde{Q}_2\rangle_{\natural}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- [Relativistic Mechanics in Biquaternionic Form](relativistic-mechanics-in-biquaternionic-form.html) — the action and the conserved current this article starts from.
- [The Klein–Gordon Equation in Biquaternionic Form](the-klein-gordon-equation-in-biquaternionic-form.html) — the field, its Lagrangian form, and the current the Noether derivation reproduces.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) — the chiral pair, the frame in the cell algebra, and Kravchenko's two-sided dictionary.
- [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html) — the mass term, the chirality cell, and the axial current of the module.
- [The Poincaré Group and the Biquaternion Frame](the-poincare-group-and-the-biquaternion-frame.html) — the symmetry group, and the corrected central translation phase.
- [Exercise: Four-Momentum Conservation in a Collision](exercise-four-momentum-conservation-in-a-collision.html) — the total four-momentum of an isolated system, and the report of the proper-time four-force defect.
- [Exercise: The Electromagnetic Energy–Momentum Tensor](exercise-the-electromagnetic-energy-momentum-tensor.html) — the rank-two translation current and why one biquaternion cannot carry it.
- [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html) — the source conservation and the energy–momentum biquaternion $\tilde{W}$.
- [The Field-Strength Biquaternion and Its Invariants](the-field-strength-biquaternion-and-its-invariants.html) — the bivector representation used for the angular momentum.
- [Angular Momentum and Spin in Biquaternionic Form](angular-momentum-and-spin-in-biquaternionic-form.html) — the angular-momentum algebra and the spin operators.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html) — the localization of the central phase whose global current is derived here.
- [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html) — the connection forced by localizing the same symmetry.
- [The Lorentz Transformation as a Biquaternionic Rotation](the-lorentz-transformation-as-a-biquaternionic-rotation.html) — the rotor whose conjugation carries the four-momentum between frames.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) and [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html) — the two sectors that house the conserved objects.
- [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html) — the algebra, its conjugations, and the local complex structure.
