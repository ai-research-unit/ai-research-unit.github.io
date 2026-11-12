# __Noether's Theorem in Biquaternionic Form__

## Introduction

Noether's theorem connects two things a physical theory supplies separately: its **symmetries** and its **conservation laws**. Every continuous symmetry of an action corresponds to a conserved quantity, and in a field theory to a conserved current. The theorem is not specific to any algebra, so writing it biquaternionically does not by itself produce a conservation law that was not already there. What the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ fixes is the **form** the theorem takes: which subspace the conserved objects live in, how a symmetry acts on a biquaternion-valued field, and which biquaternion expressions are the currents.

The two ends of the theorem are both already in the read list. *Relativistic Mechanics in Biquaternionic Form* gives the free-particle action

$$
S = -mc\int\sqrt{-\,d\tilde R_\Phi\,d\tilde{R}_\Phi^{\natural}},
$$

whose integrand is built from the biquaternion norm of the displacement biquaternion, and it gives the conservation of the four-current in the framework form $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}) = 0$. This article joins the two ends: it derives the current from the symmetry of the action, for the two kinds of symmetry the framework contains.

**Two kinds of symmetry.** A relativistic action has

- **internal** symmetries, which do not move the spacetime point — here the central phase $\tilde{Ξ}\mapsto \exp(i\alpha)\tilde{Ξ}$ of a complex biquaternion field, the symmetry whose localization is the gauge principle; and
- **spacetime** symmetries, the Poincaré transformations — four translations $\tilde R_\Phi\mapsto\tilde R_\Phi+\tilde{R}_{\Phi,0}$ and six Lorentz transformations $\tilde R_\Phi\mapsto\tilde U\tilde R_\Phi\tilde U^{*}$. Translation invariance gives the conserved four-momentum; Lorentz invariance gives the conserved angular momentum.

The internal case produces a current biquaternion $\tilde{J}_{\Phi}\in\mathbb{B}_{\Phi}$ with $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi})=0$ on shell, the framework form of $\sum_\mu\partial J_\mu/\partial R_\mu = 0$. The spacetime case produces an energy–momentum current and an angular-momentum bivector.

**What is established, and what is not.** Established below, and recomputed: the central-phase current of the complex biquaternion scalar field,

$$
\tilde{J}_{\Phi} = i\left[(\tilde\nabla_\Phi\tilde{Ξ}^{*})\tilde{Ξ} - \tilde{Ξ}^{*}(\tilde\nabla_\Phi\tilde{Ξ})\right],
$$

lies in $\mathbb{B}_{\Phi}$ and satisfies $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}) = i\,\mathrm{Sc}[(\Box_\Phi\tilde{Ξ}^{*})\tilde{Ξ} - \tilde{Ξ}^{*}(\Box_\Phi\tilde{Ξ})]$, which vanishes whenever the field obeys the Klein–Gordon equation, the sign of $\tilde{J}_{\Phi}$ being the one for which the charge density of a positive-frequency wave is positive; the same current for the Dirac field, whose components are $j_\mu=\mathrm{Sc}(\tilde{Ξ}^*e_\mu\tilde{Ξ}\,b_\mu)$ with $b_t=e_t$ and $b_k=\vec e_z$, conserved at every mass, while the axial current is conserved only at $m=0$; the free-particle four-momentum $\tilde{P}_{\Phi} = m\tilde{V}_{\Phi}$ is the Noether charge of translation invariance, and the **total** four-momentum of an isolated system is conserved; and a translation acts on a plane wave by the central unit-modulus phase $\exp(i\,\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_{\Phi,0}^{\natural})/\hbar)$. What is standard, what is only transcribed, and what is interpretation is separated in its own section below.

**Two defects in the read list, handled rather than repeated.** First, the four-force of the parent is defined by the **proper**-time derivative, $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = d\tilde{P}_{\Phi}/d\tau$, so the sum $\sum_a\tilde{\mathcal F}_{\mathrm{frc},a}$ across bodies is *not* the rate of change of the total four-momentum unless all the Lorentz factors agree; *Exercise: Four-Momentum Conservation in a Collision* reports this, and the conservation law is stated correctly below. Second, the translation of a plane wave is by a **central phase**, $\exp(i\,\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_{\Phi,0}^{\natural})/\hbar)$, and the $i$ is not optional: the same scalar in a real exponential, $\exp(\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_{\Phi,0}^{\natural}))$, is a dilation and not a phase at all.

**Conventions.** The units, the coefficient basis, the conjugations, the two sectors, the gradient and its quaternion conjugate, the d'Alembertian, the trace and the two displays are those of the read list and of the conventions files of the series; they are used here and not restated. One calibration is this article's own, and it belongs to the two coordinate charts rather than to the algebra: the gradient is taken with respect to the coefficients $Q_\mu$, with $Q_t=i q'_t$, and the energy–momentum tensor of the later sections is written in the real coordinates $x_\mu=(r'_{t},r_x,r_y,r_z)$, which are the same chart with $Q_t=i q'_t$; the two are held apart where they are used. Throughout, $c$ is the **speed of light in the medium** and $c_0$ the vacuum value; $\vec v$ is reserved for particle and frame velocities.

**The Dirac field, once.** The Dirac content of the later sections is the element $\tilde{Ξ}=\tilde{Ξ}_{L}+\tilde{Ξ}_{R}$ of $\mathbb{B}$, whose two parts carry the two values: the value of $\tilde{Ξ}_{L}$ is $-1$, the value of $\tilde{Ξ}_{R}$ is $+1$, and only the zero element carries both. A product takes the value of its right factor, and left multiplication keeps the value, so the two parts are stable under multiplication on the left. The adjoint with which the currents are formed is the algebra's own conjugation, $\tilde{Ξ}^*$. The same objects under their legacy names are collected in the closing section *The Legacy Pauli Gamma Formulation*, and none of those names is used before it.

## The Action and What a Symmetry Is

### The Particle

The free relativistic particle of rest mass $m$ has the action

$$
S[\tilde R_\Phi] = -mc\int\sqrt{-\,d\tilde R_\Phi\,d\tilde{R}_\Phi^{\natural}},
\qquad d\tilde R_\Phi = ic\,dr'_t\,e_t + d(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\in\mathbb{B}_{\Phi} .
$$

Because $d\tilde R_\Phi\,d\tilde{R}_\Phi^{\natural} = -d{r'_{t}}^2 +dr_x^2+dr_y^2+dr_z^2 = -c^2d\tau^2$ with $\tau$ the proper time, the action is $S = -mc^2\int dr'_t/\gamma$, and the Lagrangian in the coordinate time $r'_t$ is

$$
\mathrm{Lag}(\vec v) = -mc^2\sqrt{1-\vec v^2/c^2} = -\frac{mc^2}{\gamma},
\qquad \gamma = \frac{1}{\sqrt{1-\vec v^2/c^2}} .
$$

### The Field

The relativistic scalar field of the framework is the complex biquaternion field $\tilde{Ξ} = \xi_{\mathrm{scl}}\,e_t \in \mathbb{B}_{C}$, with $\xi_{\mathrm{scl}}$ a complex scalar function. Its action is $S[\tilde{Ξ}] = \int \mathcal{L}\,d^4r$ with the real Lagrangian density

$$
\mathcal{L} = +\,\mathrm{Sc}\!\left[((\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}^{*})(\tilde\nabla_\Phi\tilde{Ξ})\right] + k_m^{2}\,\mathrm{Sc}\!\left[\tilde{Ξ}^{*}\tilde{Ξ}\right].
$$

Because $\mathrm{Sc}(e_\mu^{\natural}e_\nu)=\delta_{\mu\nu}$, the first term expands over the four coordinates with a single sign,

$$
\mathcal{L} = +\frac{\partial{\xi_{\mathrm{scl}}}^{*}}{\partial R_t}\frac{\partial\xi_{\mathrm{scl}}}{\partial R_t}
+\sum_\eta\frac{\partial{\xi_{\mathrm{scl}}}^{*}}{\partial R_\eta}\frac{\partial\xi_{\mathrm{scl}}}{\partial R_\eta}
+k_m^{2}\,{\xi_{\mathrm{scl}}}^{*}\xi_{\mathrm{scl}} ,
$$

the uniform signs being what the $\natural$ conjugation supplies. The time term is nevertheless negative, because $\partial/\partial R_t=\partial/\partial i r'_t$ acts on both factors and two applications of it give $-\partial^2/\partial {r'_t}^2$; in the real coordinates $x_\mu=(r'_{t},r_x,r_y,r_z)$ the same expression reads

$$
\mathcal{L} = -\left|\frac{\partial\xi_{\mathrm{scl}}}{\partial r'_t}\right|^2 + |\nabla\xi_{\mathrm{scl}}|^2 + k_m^{2}|\xi_{\mathrm{scl}}|^2 .
$$

This is the form used with the energy–momentum tensor below. The Euler–Lagrange equation of $\mathcal{L}$ is the biquaternion Klein–Gordon equation

$$
\left(\Box - k_m^{2}\right)\tilde{Ξ} = 0,
$$

the overall sign of $\mathcal{L}$ being immaterial for the equation and fixed here by the positivity of the energy density. Both the action and the equation are those of the read list; $\mathcal{L}$ is exhibited only because a Noether current is read off a Lagrangian. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

### Symmetries of the Action and of the Equations

A one-parameter family $\tilde{Ξ}_\varepsilon$ with $\tilde{Ξ}_0 = \tilde{Ξ}$ is a **symmetry of the action** if $S[\tilde{Ξ}_\varepsilon] = S[\tilde{Ξ}]$ for every field configuration, and a **symmetry of the equations of motion** if it preserves the solution set. A symmetry of the action is the stronger notion, and it is the one that yields a conserved current by Noether's theorem.

### The Theorem in the Two Forms the Framework Needs

For an internal symmetry, the theorem states that there is a current biquaternion $\tilde{J}_{\Phi} = J_t\,e_t + \sum_\eta J_\eta\,\vec e_\eta$ whose divergence vanishes when the field obeys its equation:

$$
\delta S = 0 \ \text{for all fields}
\qquad\Longrightarrow\qquad
\mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}\right) = 0 \ \text{on shell}.
$$

For a spacetime symmetry, the same construction applied to a transformation that moves the point $\tilde R_\Phi$ yields a current carrying one index per generator: for translations the energy–momentum current, for Lorentz transformations the angular-momentum current. The two forms differ only in what the symmetry variation acts on. The general identity behind both is that the divergence of the current is the field equation contracted with the symmetry variation; it is written out for the central phase in the next section and for translations after that.

## The Current of the Central Phase

### The Symmetry and the Current

Multiplication by a central phase,

$$
\tilde{Ξ}\ \longmapsto\ \exp(i\alpha)\tilde{Ξ},
\qquad \alpha\in\mathbb{R},
$$

leaves both terms of $\mathcal{L}$ unchanged, because $\exp(i\alpha)$ is central and $\tilde{Ξ}^{*}\mapsto \exp(-i\alpha)\tilde{Ξ}^{*}$: the two phase factors in $((\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}^{*})(\tilde\nabla_\Phi\tilde{Ξ})$ cancel, and $\tilde{Ξ}^{*}\tilde{Ξ}$ is invariant. The symmetry therefore holds for the **massive** field as well as the massless one, because the mass term depends on $\tilde{Ξ}$ only through the invariant $\tilde{Ξ}^{*}\tilde{Ξ}$ — a fact used again below.

For the infinitesimal variation $\delta\tilde{Ξ} = i\alpha\tilde{Ξ}$, $\delta\tilde{Ξ}^{*} = -i\alpha\tilde{Ξ}^{*}$, Noether's construction gives

$$
J_\nu = \frac{\partial\mathcal{L}}{\partial(\partial\xi_{\mathrm{scl}}/\partial R_\nu)}\,\delta\xi_{\mathrm{scl}} + \frac{\partial\mathcal{L}}{\partial(\partial{\xi_{\mathrm{scl}}}^{*}/\partial R_\nu)}\,\delta{\xi_{\mathrm{scl}}}^{*}
= i\alpha\left(\frac{\partial{\xi_{\mathrm{scl}}}^{*}}{\partial R_\nu}\,\xi_{\mathrm{scl}} - \frac{\partial\xi_{\mathrm{scl}}}{\partial R_\nu}\,{\xi_{\mathrm{scl}}}^{*}\right),
$$

the second equality from $\partial\mathcal{L}/\partial(\partial\xi_{\mathrm{scl}}/\partial R_\nu) = +\partial{\xi_{\mathrm{scl}}}^{*}/\partial R_\nu$ and its conjugate, which is what the Lagrangian above supplies. Setting $\alpha = 1$ and packaging the four components,

$$
\boxed{\ \tilde{J}_{\Phi} = i\left[(\tilde\nabla_\Phi\tilde{Ξ}^{*})\tilde{Ξ} - \tilde{Ξ}^{*}(\tilde\nabla_\Phi\tilde{Ξ})\right] = \sum_\nu J_\nu e_\nu\ }
\qquad (\tilde{Ξ} = \xi_{\mathrm{scl}}\,e_t).
$$

The overall sign of a current is free — the symmetry with the opposite generator gives the opposite current — and it is fixed here by the charge density, as the next paragraph shows.

### The Current Lies in the Material Sector

The temporal component in the $i r'_t$ basis is $J_t = i\left(\xi_{\mathrm{scl}}\,\frac{\partial{\xi_{\mathrm{scl}}}^{*}}{\partial R_t} - {\xi_{\mathrm{scl}}}^{*}\frac{\partial\xi_{\mathrm{scl}}}{\partial R_t}\right)$. Because $\partial/\partial R_t=-i\,\partial/\partial r'_t$ and the spatial derivatives are plain, the two kinds of component are recorded separately:

$$
J_t = -\left({\xi_{\mathrm{scl}}}^{*}\partial/\partial r'_t\,\xi_{\mathrm{scl}} - \xi_{\mathrm{scl}}\,\partial/\partial r'_t\,{\xi_{\mathrm{scl}}}^{*}\right) = -2i\,\mathrm{Im}\!\left({\xi_{\mathrm{scl}}}^{*}\frac{\partial\xi_{\mathrm{scl}}}{\partial r'_t}\right),
$$

which is **purely imaginary**, while the spatial components

$$
J_\eta = +2\,\mathrm{Im}\!\left({\xi_{\mathrm{scl}}}^{*}\frac{\partial\xi_{\mathrm{scl}}}{\partial R_\eta}\right)
$$

are real, the $i$ of the current multiplying the $-2i$ of the Wronskian to $+2$. Hence $\tilde{J}_{\Phi}\in\mathbb{B}_{\Phi}$, with imaginary scalar part and real vector part, exactly as the four-current of relativistic mechanics. Writing $J_t = ic\rho$ recovers the parent's convention $\tilde{J}_{\Phi} = ic\rho\,e_t + \vec j$, with

$$
\rho = \frac{i}{c}\left({\xi_{\mathrm{scl}}}^{*}\partial/\partial r'_t\,\xi_{\mathrm{scl}} - \xi_{\mathrm{scl}}\,\partial/\partial r'_t\,{\xi_{\mathrm{scl}}}^{*}\right),
$$

which is real and **positive** on a positive-frequency wave $\xi_{\mathrm{scl}}\propto\exp(i(\vec k_\Phi\cdot\vec r-\omega r'_t/c))$, where it equals $\frac{2\omega}{c}|\xi_{\mathrm{scl}}|^2$. This is the sign convention of *The Klein–Gordon Equation in Biquaternionic Form*, and it is what fixes the sign of $\tilde{J}_{\Phi}$ above.

### Conservation and the Identity Behind It

Forming the scalar part of $(\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}$,

$$
\mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}\right) = \sum_\mu\partial/\partial R_\mu\,J_\mu = \langle\tilde\nabla_\Phi,\tilde J_{\Phi}\rangle_{\natural} ,
$$

the sum being plain, because the signs of $\varepsilon$ are spent inside $(\tilde\nabla_\Phi)^{\natural}$: on the diagonal $\mathrm{Sc}(e_\mu^{\natural}e_\mu)=1$ for all four $\mu$. Using the definitions and the d'Alembertian,

$$
\boxed{\ \mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}\right) = i\,\mathrm{Sc}\!\left[(\Box_\Phi\tilde{Ξ}^{*})\tilde{Ξ} - \tilde{Ξ}^{*}(\Box_\Phi\tilde{Ξ})\right]\ }
$$

The cross terms of each $\mu$ enter with opposite signs and cancel, so only the second derivatives survive. This is the Noether identity in biquaternion form: the scalar divergence of the current is the Klein–Gordon operator applied to the field, contracted with the symmetry variation. On shell, $\Box\tilde{Ξ} = (k_m^{2})\tilde{Ξ}$ and the same for the conjugate, both terms become the same real multiple of $\tilde{Ξ}^{*}\tilde{Ξ}$ and cancel, so

$$
\mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}\right) = 0 \quad\text{on shell},
$$

which is the continuity equation $c\,\partial/\partial r'_t\rho + \mathrm{div}\,\vec j = 0$. The reason the time component needs no separate sign is the same one met above: $\partial/\partial R_t=-i\,\partial/\partial r'_t$ meets $J_t=ic\rho$, and the two central imaginaries cancel, $(-i)(i)=1$, leaving the factor $c$ of the current and the plain $\partial/\partial r'_t$ of the continuity equation.

### On What Case This Was Checked

A single plane wave is a trap: for $\tilde{Ξ} = \tilde{Ξ}_0\exp(i\,\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_\Phi^{\natural})/\hbar)$ the current is *constant*, so its divergence vanishes whether or not the field is on shell, and the plane wave that suggests the formula cannot test it. The conservation was therefore checked on three other cases:

- **a superposition of on-shell plane waves.** With $c = \hbar = m = 1$ and the momenta $(|\vec k_\Phi|,\omega) = (0,1)$, $(\tfrac34,\tfrac54)$, $(\tfrac{5}{12},\tfrac{13}{12})$ all satisfying $\omega^2 = \vec k_\Phi^2 + 1$, and amplitudes $1, \tfrac12, \tfrac13$, the current has non-constant cross terms, and $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi})$ cancels identically;
- **a standing wave**, $\tilde{Ξ} = \sin(kx)\cos(\omega r'_t/c) + i\sin(kx)\sin(\omega r'_t/c)$ with $\omega^2 = c^2k^2 + c^2k_m^{2}$: this is on shell and is **not** a plane wave, and again $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi})$ vanishes identically;
- **an off-shell field.** A two-mode field with one mode off shell gives a divergence proportional to the field equation, explicitly nonzero. The identity above was also confirmed on a generic three-mode field, off shell: the difference $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}) - i\,\mathrm{Sc}[(\Box_\Phi\tilde{Ξ}^{*})\tilde{Ξ} - \tilde{Ξ}^{*}(\Box_\Phi\tilde{Ξ})]$ reduces to zero identically, and the divergence is $2\,\mathrm{Im}(\tilde{Ξ}^{*}\Box\tilde{Ξ})$, which is what the identity gives.

The last case is the honest statement of the theorem: the current is conserved **whenever** the field equation holds; off shell it need not be, and its divergence *is* the field equation.

### Relation to the Current Already in the Corpus

*The Klein–Gordon Equation in Biquaternionic Form* posits the current with $\rho =\frac{i\,\hbar}{2\,m\,c^{2}}(\tilde{Ξ}^{*}\partial/\partial r'_t\tilde{Ξ} - \tilde{Ξ}\partial/\partial r'_t\tilde{Ξ}^{*})$ and $\vec j = -\frac{i\,\hbar}{2\,m}(\tilde{Ξ}^{*}\nabla\tilde{Ξ} - \tilde{Ξ}\nabla\tilde{Ξ}^{*})$. Comparing component by component, that current equals $+\frac{\hbar}{2\,m}\tilde{J}_{\Phi}$: the Noether derivation reproduces the current the parent states, and fixes the normalization only up to the constant $\frac{\hbar}{2\,m}$ that a current may always be multiplied by. What the derivation adds is **why** that combination is the conserved one, and that it is forced by the phase symmetry rather than chosen.

**Relation to the Maxwell source.** In the Maxwell article the source conservation is $\sqrt{\mu}\,\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}) = 0$ with $\tilde J_{\Phi} = ic\rho\,e_t + \vec J$. Expanding, $\sqrt{\mu}\,\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}) = \sqrt{\mu}\,(\partial/\partial r'_t\rho + \mathrm{div}\,\vec J)$, so the Maxwell integrability condition is the same continuity equation as the conservation of $\tilde{J}_{\Phi}$ above. The electric four-current of the material sector is the Noether current of the central phase; the gauge freedom localized in *The Gauge Principle in Biquaternionic Form* is the localization of the symmetry that produces it.

### The Dirac Field: the Pair, the Two-Sided Form, and the Axial Current

The same phase is a symmetry of the massive Dirac field. For the Dirac field the dynamics is the **chiral pair**

$$
\begin{aligned}
\tilde\nabla_\Phi\tilde{Ξ}_{R} &= k_m\,\tilde{Ξ}_{L},\\[4pt]
(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L} &= k_m\,\tilde{Ξ}_{R},
\end{aligned}
$$

two equations, one per part, each first order and linear in the field, with $m$ central. They are the two lines of one dynamics, not two independent ones: eliminating one half gives the massive Klein–Gordon equation, and at $m=0$ the pair decouples into the two Weyl equations, $\tilde\nabla_\Phi\tilde{Ξ}_{R}=0$ and $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=0$, one for each part. A central phase passes through both lines, since it passes through the central mass, so the current derived above is the conserved current of the Dirac field at every $m$, and $\langle\tilde\nabla_\Phi,\tilde J_{\Phi}\rangle_{\natural}=0$ on shell for it.

**The two-sided form.** Read on the whole algebra rather than on the two parts, the same dynamics is one equation in which the derivative acts on the left and the unit $\vec e_z$ on the right,

$$
(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ} = -\,m\,i\,\bar{\tilde{Ξ}}\,\vec e_z ,
$$

where $\bar{\tilde{Ξ}}$ is the coefficient conjugate, taken on the four coefficients and leaving the units fixed. The mass is thus a right multiplication by $\vec e_z$ carried with the imaginary unit: the central mass of the pair becomes a product, with the unit displayed and the factor $i$ left in front, one real mass multiplying one unit and one $i$. This is the operator-theoretic content of the two-sidedness: the derivative acts on the left, the mass on the right, and the conjugation supplies the antilinear part, so the second field of the $\natural$-side equation is the conjugate of the first carried on the right. The one-sided pair is the definition; this is its form on the algebra, one line, with the unit $\vec e_z$ standing where the second part stood.

**The currents on the algebra.** With the algebra's conjugation as the adjoint, the central-phase current of the Dirac field has the components

$$
j_\mu = \mathrm{Sc}\bigl(\tilde{Ξ}^*\,e_\mu\,\tilde{Ξ}\,b_\mu\bigr),
\qquad b_t = e_t,\quad b_k = \vec e_z\ \ (k=x,y,z),
$$

the unit of the coordinate inserted between the field and its adjoint: $j_t = \mathrm{Sc}(\tilde{Ξ}^*\tilde{Ξ})$ is the Hermitian norm of the field, and $j_\eta = \mathrm{Sc}(\tilde{Ξ}^*\vec e_\eta\tilde{Ξ}\vec e_z)$ is the component of the current along $\vec e_\eta$. The axial rotation assigns opposite phases to the two parts, so the mass term, which pairs them, is not invariant under it; the axial current therefore carries the unit $\vec e_z$ inside the product,

$$
j_{5\mu} = \mathrm{Sc}\bigl(\tilde{Ξ}^*\,i\,e_\mu\,\tilde{Ξ}\,\vec e_z\vec e_{\tau(\mu)}\vec e_x\bigr),
\qquad \tau(t)=x,\ \ \tau(k)=y\ \ (k=x,y,z),
$$

which reduces on the two cases to

$$
j_{5t} = -\,i\,\mathrm{Sc}\bigl(\tilde{Ξ}^*\tilde{Ξ}\vec e_z\bigr),
\qquad
j_{5\eta} = i\,\mathrm{Sc}\bigl(\tilde{Ξ}^*\vec e_\eta\tilde{Ξ}\bigr).
$$

The right multiplier of the general form is the product $\vec e_z\vec e_{\tau(\mu)}$ in that order, and it is not symmetric: writing the two units the other way round flips the sign of the current. The divergence is the **plain** sum of the four derivatives, since the $\natural$ in $\langle\tilde\nabla_\Phi,\tilde J_{\Phi,5}\rangle_{\natural}$ already carries the relative sign of the spatial derivatives; the mass is the obstruction:

$$
\langle\tilde\nabla_\Phi,\tilde J_{\Phi,5}\rangle_{\natural} = \sum_\mu\frac{\partial j_{5\mu}}{\partial R_\mu} = 2im\,\mathrm{Sc}\bigl(\tilde{Ξ}^*\tilde{Ξ}\vec e_y\bigr),
$$

using $\vec e_z\vec e_x=\vec e_y$, and this vanishes only at $m=0$. The same statement without the units on show: the axial rotation multiplies each part by a phase opposite to the other's, and on the algebra it is a right multiplication,

$$
\tilde{Ξ}\ \longmapsto\ \tilde{Ξ}\,(\cos\alpha+\sin\alpha\,\vec e_z),
$$

which multiplies $\tilde{Ξ}_{L}$ by $\exp(-i\alpha)$ and $\tilde{Ξ}_{R}$ by $\exp(+i\alpha)$, because right multiplication by $\vec e_z$ acts on the two parts as $-i$ and $+i$. That is why the axial current carries the unit $\vec e_z$ and not a separate object.

**What the mass breaks, and what it does not.** What the mass term breaks is the **axial** rotation, not the phase. The mass term is $-mi\bar{\tilde{Ξ}}\vec e_z$: one right factor $\vec e_z$ between the field and its conjugate. It is invariant under the central phase, which multiplies the field by a central scalar and leaves every unit alone, so both sides of the equation take the same phase and it is carried to itself; and it is not invariant under the axial rotation, which replaces that right factor by $\cos\alpha\,\vec e_z-\sin\alpha\,e_t$, since $\vec e_z\vec e_z=-e_t$. In the biquaternion reading the mass couples the two parts off the diagonal, so it breaks exactly the rotation that moves them against each other, and not the central $\mathrm{U}(1)$ that the algebra canonically carries. The previously recorded obstruction belonged to the retired antilinear single-field equation; the gauge principle article's corresponding section is revised on the same grounds.

## Translation Invariance and the Conserved Four-Momentum

### The Particle Charge

The action $S[\tilde R_\Phi]$ above depends on $\tilde R_\Phi$ only through $d\tilde R_\Phi$, so the constant shift

$$
\tilde R_\Phi\ \longmapsto\ \tilde R_\Phi + \tilde{R}_{\Phi,0},
\qquad \tilde{R}_{\Phi,0}\in\mathbb{B}_{\Phi}\ \text{constant},
$$

is a symmetry of the action. The Noether charges are the momentum conjugate to $r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ and the energy conjugate to $r'_t$; computing the first from the Lagrangian,

$$
\vec p = \frac{\partial \mathrm{Lag}}{\partial\vec v} = \gamma m\vec v,
\qquad
E = \vec p\cdot\vec v - \mathrm{Lag} = \gamma mc^2,
$$

and combining them into the four-momentum,

$$
\boxed{\ \tilde{P}_{\Phi} = m\tilde{V}_{\Phi} = i\frac{E}{c}\,e_t + \vec p\ }
\qquad (\tilde{V}_{\Phi} = \gamma(ic\,e_t + \vec v)).
$$

The mass-shell relation $\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural} = -m^{2}\,c^{2}$ follows, since $\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural}=-(E/c)^2+\vec p^{\,2}$ and $E^2=\vec p^{\,2}c^2+m^2c^4$. Translation invariance is thus the symmetry whose Noether charge is the four-momentum; the four-momentum is conserved for a free particle, $d\tilde{P}_{\Phi}/d\tau = 0$, because $\mathrm{Lag}$ has no explicit $\tilde{Q}$-dependence. As an independent check, a particle with $m = c = 1$, $\vec p = (0.6,0,0)$ and $E = \sqrt{1.36}$ was boosted by the rotor $\tilde U = \cosh(\theta_{\mathrm{rpd}}/2) + i\sinh(\theta_{\mathrm{rpd}}/2)\vec e_x$ with $\tilde{Ξ} = 1.2$, the conjugation being $\tilde U\tilde P_{\Phi}\tilde U^{*}$: the result is $E' = 1.206$ and $p'_x = -0.674$, which are the component formulas $E'=\cosh\theta_{\mathrm{rpd}}\,E-\sinh\theta_{\mathrm{rpd}}\,p_x$ and $p'_x=\cosh\theta_{\mathrm{rpd}}\,p_x-\sinh\theta_{\mathrm{rpd}}\,E$, and the biquaternion norm is $-1$ in both frames, confirming that the Noether charge transforms as a four-vector.

### The Conservation Law for a System, Stated Correctly

For an isolated system of bodies $a$ the conserved object is the **total** four-momentum, and the correct statement is

$$
\boxed{\;\tilde{P}_{\Phi,\mathrm{tot}} = \sum_a \tilde{P}_{\Phi,a},
\qquad
\frac{d\tilde{P}_{\Phi,\mathrm{tot}}}{dt'} = c\,\frac{d\tilde{P}_{\Phi,\mathrm{tot}}}{dr'_t} = 0\;},
$$

a vanishing **coordinate**-time derivative; the clock is $t'=r'_t/c$, so $d/dt'=c\,d/dr'_t$ and the coordinate time is a length divided by the speed of light. The parent defines the four-force by the **proper**-time derivative of a single body, $\tilde{\mathcal F}_{\mathrm{frc},a} = d\tilde{P}_{\Phi,a}/d\tau_a$, and since $d\tau_a = dr'_t/(c\gamma_a)$,

$$
\frac{d\tilde{P}_{\Phi,a}}{dr'_t} = \frac{1}{c\gamma_a}\tilde{\mathcal F}_{\mathrm{frc},a},
\qquad\text{so}\qquad
\sum_a \tilde{\mathcal F}_{\mathrm{frc},a} = \sum_a c\gamma_a\frac{d\tilde{P}_{\Phi,a}}{dr'_t} = \sum_a \gamma_a\frac{d\tilde{P}_{\Phi,a}}{dt'},
$$

which equals $c\,d\tilde{P}_{\Phi,\mathrm{tot}}/dr'_t = d\tilde{P}_{\Phi,\mathrm{tot}}/dt'$ only when all the $\gamma_a$ are equal. The parent's symbol $\tilde{\mathcal F}_{\Phi,\mathrm{frc}}$ is a per-body proper-time rate and cannot be summed across bodies. The conservation law in terms of the parent's four-forces is therefore

$$
\sum_a \frac{1}{c\gamma_a}\tilde{\mathcal F}_{\mathrm{frc},a} = \frac{d\tilde{P}_{\Phi,\mathrm{tot}}}{dr'_t} = 0,
$$

or, in the integrated form that avoids the derivative altogether, $\sum_{\mathrm{in}}\tilde{P}_{\Phi} = \sum_{\mathrm{out}}\tilde{P}_{\Phi}$ for a collision. The exercise reports this defect; the corrected statement above is the one to use.

**A numerical witness.** Two bodies connected by a translation-invariant interaction exchange momentum, so at some instant $d\tilde{P}_{\Phi,2}/dr'_t = -d\tilde{P}_{\Phi,1}/dr'_t = i\,e_t + \vec e_x$, and their Lorentz factors differ, $\gamma_1 = 5/3$, $\gamma_2 = 5/4$. Then $d\tilde{P}_{\Phi,\mathrm{tot}}/dr'_t = 0$, but

$$
\tilde{\mathcal F}_{\mathrm{frc},1} + \tilde{\mathcal F}_{\mathrm{frc},2} = c(\gamma_2 - \gamma_1)\left(i\,e_t + \vec e_x\right) = -\frac{5c}{12}\left(i\,e_t + \vec e_x\right) \neq 0 .
$$

The naive sum of the parent's four-forces is not zero even though the total four-momentum is conserved. For the collision of *Exercise: Four-Momentum Conservation in a Collision* ($E_1 = 3mc^2$, equal masses, $\theta^* = 90^\circ$), the total four-momenta $\tilde{P}_{\Phi,\mathrm{in}}$ and $\tilde{P}_{\Phi,\mathrm{out}}$ were recomputed and agree component by component in the laboratory.

### What Translation Does to a Plane Wave

A free field is a plane wave, and a translation acts on it by a central phase. With the series' phase convention $\tilde{Ξ} = \tilde{Ξ}_0\exp(i\,\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_\Phi^{\natural})/\hbar)$, whose phase is $\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_\Phi^{\natural}) = \vec k_\Phi\cdot\vec r-\omega r'_t/c$, and with $\tilde P_{\Phi}\in\mathbb{B}_{\Phi}$ and $\tilde R_\Phi\mapsto\tilde R_\Phi+\tilde{R}_{\Phi,0}$,

$$
\tilde{Ξ}\big|_{\tilde R_\Phi+\tilde{R}_{\Phi,0}} = \exp\!\bigl(i\,\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_{\Phi,0}^{\natural})/\hbar\bigr)\,\tilde{Ξ}\big|_{\tilde R_\Phi},
\qquad
\tilde{Ξ}_0\ \text{constant}.
$$

The multiplier is **central and of unit modulus**, because $\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_{\Phi,0}^{\natural}) = \langle\tilde P_{\Phi},\tilde{R}_{\Phi,0}\rangle_{\natural}$ is real: writing $\tilde P_{\Phi} = i\frac{\omega}{c}e_t + \vec k_\Phi$ and $\tilde{R}_{\Phi,0} = i R_{0t} e_t + \vec R_0$, with $R_{0t} = r'_{t,0$,

$$
\mathrm{Sc}\!\left(\tilde P_{\Phi}\tilde{R}_{\Phi,0}^{\natural}\right) = -\frac{\omega R_{0t}}{c} + \vec k_\Phi\cdot\vec R_0 = \vec k_\Phi\cdot\vec R_0-\omega r'_{t,0}/c .
$$

What makes it a phase is the $i$: the same scalar in a real exponential is a dilation. For $\tilde P_{\Phi} = 2i\,e_t + 0.7\vec e_x - 0.3\vec e_y + 0.5\vec e_z$ and $\tilde{R}_{\Phi,0} = 0.4i\,e_t + 0.25\vec e_x - 0.35\vec e_y + 0.15\vec e_z$ (in the units of the check), $\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_{\Phi,0}^{\natural}) = -0.445$ and the multiplier is $\exp(-0.445i)$, of modulus $1$, whereas $\exp(\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_{\Phi,0}^{\natural})) = e^{-0.445}$ has modulus $0.641$. The $\natural$ inside the pairing must be the one the wave itself carries; the un-conjugated $\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_{\Phi,0}) = -\frac{\omega R_{0t}}{c}-\vec k_\Phi\cdot\vec R_0$ belongs to the opposite sign convention for $\vec k_\Phi$ in the phase, and mixing the two flips the sign of $\vec k_\Phi\cdot\vec R_0$ alone. This central phase is the finite, field-space form of the translation subgroup; its infinitesimal generator is the derivation $\partial/\partial R_\mu$, and it is not a rotor, as *The Poincaré Group and the Biquaternion Frame* establishes.

## The Energy–Momentum of the Field

### The Canonical Tensor

The same translation symmetry applied to the field action gives the **canonical energy–momentum**, the Noether current of spacetime translations. For the complex scalar field it is

$$
\boxed{\;T_{\mu\nu} = \frac{\partial{\xi_{\mathrm{scl}}}^*}{\partial x_\mu}\frac{\partial\xi_{\mathrm{scl}}}{\partial x_\nu} + \frac{\partial\xi_{\mathrm{scl}}}{\partial x_\mu}\frac{\partial{\xi_{\mathrm{scl}}}^*}{\partial x_\nu} + \varepsilon_\mu\delta_{\mu\nu}\,\mathcal{L}_{\mathrm{scl},\xi}\;}
$$

with the scalar Lagrangian of the same coordinates,

$$
\mathcal{L}_{\mathrm{scl},\xi} = \sum_\mu\frac{\partial{\xi_{\mathrm{scl}}}^*}{\partial R_\mu}\frac{\partial\xi_{\mathrm{scl}}}{\partial R_\mu} + k_m^{2}|\xi_{\mathrm{scl}}|^2
= -\left|\frac{\partial\xi_{\mathrm{scl}}}{\partial r'_t}\right|^2 + |\nabla\xi_{\mathrm{scl}}|^2 + k_m^{2}|\xi_{\mathrm{scl}}|^2 .
$$

Here $x_\mu=(r'_{t},r_x,r_y,r_z)$ are the real coordinates, the chart of $Q_\mu$ with the $i$ of the time coefficient removed, $Q_t=i q'_t$: $Q_0=i q'_t$ carries the $i$, while $x_0=r'_{t}$ does not. Both indices of $T$ are low, the first the row. The coefficient of $\mathcal{L}_{\mathrm{scl},\xi}$ is the plain form of the two units, $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$: plus on the time entry and minus on the three space entries. The derivative index of the conservation law carries one minus on the time direction and none on the three space directions, and that minus is the square of the $i$ in $Q_t=i q'_t$, spent once and written out. Translation invariance gives

$$
-\frac{\partial T_{0\nu}}{\partial x_0}+\sum_\eta\frac{\partial T_{\eta\nu}}{\partial r_\eta} = 0
$$

on shell. Its time–time component is the energy density,

$$
T_{00} = \left|\frac{\partial\xi_{\mathrm{scl}}}{\partial r'_t}\right|^2 + |\nabla\xi_{\mathrm{scl}}|^2 + k_m^{2}|\xi_{\mathrm{scl}}|^2 > 0,
$$

positive for every configuration because each term is a square. This was checked by recomputation on an on-shell superposition of two plane waves: the four divergences $-\partial T_{0\nu}/\partial x_0+\sum_\eta\partial T_{\eta\nu}/\partial r_\eta$ vanish to $10^{-10}$, the tensor is symmetric, and $T_{00}$ equals the expression above.

### Why the Framework Does Not Write It as One Biquaternion

A symmetric rank-two tensor in four dimensions has ten independent components, while a biquaternion has four complex coefficients, that is eight real components, and $\tilde{W}_{\Psi} = \tfrac12\tilde{F}\tilde{F}^{*}$ carries only four of them. So no single biquaternion can be $T_{\mu\nu}$; the framework writes the translation current as a **bigeneral quaternionic bilinear**, one basis element for each index. *Exercise: The Electromagnetic Energy–Momentum Tensor* constructs exactly this for the Maxwell field, $\Pi_{\mu\nu} = \tfrac12\mathrm{Sc}(\tilde{F}\mathcal{E}_\mu\tilde{F}^{*}\mathcal{E}_\nu)$ with the first index the row, and shows that the four-component object is its time row. The framework's energy–momentum biquaternion is therefore not the whole Noether current of translations; it is the energy–flux part of it.

### The Maxwell Case in the Corpus Form

For the electromagnetic field the four-component object is $\tilde{W}_{\Psi} = \tfrac12\tilde{F}\tilde{F}^{*} = W\,e_t + \frac{i}{c}\vec S\in\mathbb{B}_{\Psi}$, with $W$ the energy density and $\vec S = \vec E\times\vec H$ the Poynting vector. Its scalar divergence is the energy law,

$$
\mathrm{Sc}\!\left(\tilde\nabla_\Phi\tilde{W}_{\Psi}\right) = -i\left(\frac{\partial W}{\partial r'_t}+\frac{1}{c}\,\mathrm{div}\,\vec S\right) = \frac{i}{c}\,\vec J\cdot\vec E ,
$$

the last equality being the Poynting theorem. The factor $i$ is uniform across the two terms, as a temporal component must be in the $i r'_t$ convention, and dividing it out recovers $c\,\partial W/\partial r'_t + \mathrm{div}\,\vec S + \vec J\cdot\vec E = 0$. The real form $\tilde W_{\Psi} = W + \frac{1}{c}\vec S$ fails exactly this test: its scalar divergence carries the $i$ on the time term only, and on a free plane wave it equals $\frac{1-i}{c}\partial W/\partial r'_t$, which is not zero. What *Exercise: The Electromagnetic Energy–Momentum Tensor* isolates is that factor $i$ on the Poynting part, and the equation $\tilde\nabla_\Phi\tilde{W}_{\Psi} = -\tilde{\mathcal F}$, taken as a biquaternion identity with a power–force density on the right, is not what the corpus establishes for either form: what it verifies is the scalar statement above, not the vector one. Read as a Noether statement, $\mathrm{Sc}(\tilde\nabla_\Phi\tilde{W}_{\Psi}) = \frac{i}{c}\vec J\cdot\vec E$ says the translation current is conserved up to the work done on the charges — the source is present, so the field alone is not closed.

### A Caution on the $i r'_t$ Convention

The energy density is not $\mathcal{L}_{\mathrm{scl},\xi}$ and is not obtained from it by a flat sum: $T_{00}=\frac{1}{c^2}|\dot\xi_{\mathrm{scl}}|^2+|\nabla\xi_{\mathrm{scl}}|^2+k_m^{2}|\xi_{\mathrm{scl}}|^2$ while $\mathcal{L}_{\mathrm{scl},\xi}=-\frac{1}{c^2}|\dot\xi_{\mathrm{scl}}|^2+|\nabla\xi_{\mathrm{scl}}|^2+k_m^{2}|\xi_{\mathrm{scl}}|^2$, with the mass wave number $k_m=mc/\hbar$ and its reciprocal $k_m=mc/\hbar$. The gradient and $\Box$ live in the $Q_\mu$ frame, where $Q_0=i q'_t$; the tensor lives in $x_\mu=(r'_{t},r_x,r_y,r_z)$, where the time component is real and the minus is written on the time derivative. Mixing the two charts produces the wrong sign on the time derivative, and the mismatch is the same $1/i^2=-1$ that makes the time term of the uniform $Q$-frame sum of $\mathcal{L}$ negative once written in the real coordinates. This is the same caution the energy–momentum exercise records for the trace.

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

the angular momentum of a free particle is a single biquaternion. The tilde rather than an arrow is deliberate: the vector part of $\tilde L$ is $L_{0\eta}-\tfrac12\epsilon_{\eta ij}L_{ij}$ along $\vec e_\eta$, which pairs the boost charges with $\vec r\times\vec p$ and is not the three-vector of orbital angular momentum. This is the same construction by which $\tilde{F} = \mathrm{Vect}((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}) = \tfrac12\sum_{\mu\nu}F_{\mu\nu}e^{\natural}_\mu e_\nu$ packages the antisymmetric field strength, and the Lorentz generators themselves are bivectors.

### The Rank-Three Field Current

For a field, the Noether current of Lorentz invariance is a rank-three object,

$$
L_{\mu\nu\rho} = x_\nu T_{\mu\rho} - x_\rho T_{\mu\nu} + S_{\mu\nu\rho},
$$

whose conservation

$$
-\frac{\partial L_{0\nu\rho}}{\partial x_0}+\sum_\eta\frac{\partial L_{\eta\nu\rho}}{\partial r_\eta} = 0
$$

expresses the symmetry of the energy–momentum tensor together with the conservation of spin. Being rank three, it is not a biquaternion and not even a single bilinear; the orbital and spin pieces separate, with the spin term vanishing for the classical scalar field. The particle bivector $\tilde L$ above is the finite-dimensional case where the rank-two object *is* the whole story.

## What Is Inherited, What Is Added, What Is Interpretation

**Inherited and unchanged.** The action, the four-momentum, the four-current and its conservation $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}) = 0$, the algebra, the gradient, the sectors, and the trace formula, for a state $\tilde{Ϛ}_{\Psi}$ and a Hermitian observable $\tilde H_\Psi$, $\mathrm{Tr}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})=\mathrm{Tr}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi)=2\langle\tilde{Ϛ}_{\Psi},\tilde H_\Psi\rangle_{*} = 2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})$ are those of the read list. No symbol is renamed, the sign of the current is the one for which $\rho>0$ on a positive-frequency wave, and what this article adds to the list is derivation and identification, not new definitions.

**Added by this article.** The derivation of the central-phase current $\tilde{J}_{\Phi} = i[(\tilde\nabla_\Phi\tilde{Ξ}^{*})\tilde{Ξ} - \tilde{Ξ}^{*}\tilde\nabla_\Phi\tilde{Ξ}]$ from the phase symmetry of the field action, and its conservation identity; its form $j_\mu=\mathrm{Sc}(\tilde{Ξ}^*e_\mu\tilde{Ξ}\,b_\mu)$ on the Dirac field, with the axial current and its non-conservation; the identification of the free-particle four-momentum as the Noether charge of translation invariance, with the corrected multi-body statement; the explicit translation multiplier $\exp(i\,\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_{\Phi,0}^{\natural})/\hbar)$; the energy–momentum current and its packaging; and the angular-momentum bivector. These are transcriptions of the standard theorem into the algebra, with the subspace assignments the algebra supplies, not new physics.

**Only transcribed.** Noether's theorem itself is standard; the algebra does not produce a symmetry that the action did not already have, nor a conservation law beyond those the symmetries give. The framework supplies the home of each conserved object — the current in $\mathbb{B}_{\Phi}$, the energy–momentum in the bilinear and its time row in $\mathbb{B}_{\Psi}$ for Maxwell, the angular momentum in the bivector — and it makes the divergence identities compact. It does not supply the symmetries, the coupling constants, or the masses.

**Interpretation.** Reading the conserved currents as the physical four-current and energy–momentum is the standard interpretation, not an extra postulate; the biquaternion packaging is a representation-theoretic statement about which subspace carries which object, and it is exact. What remains interpretation is the physical hypothesis attached to the two sectors, which is the program's, not this article's.

## Open Questions

1. **The biquaternion form of the full translation current.** The energy–momentum tensor is rank two and cannot be one biquaternion. Is there a natural biquaternion-bilinear expression for the canonical $T_{\mu\nu}$ of a general biquaternion field, beyond the Maxwell case constructed in the energy–momentum exercise?

2. **Spin and the angular momentum of fields.** The rank-three Lorentz current carries a spin term. Can the spin density of a biquaternion field be written as a single algebra-valued object, and how does it relate to the bivector representation of angular momentum?

3. **Scale and conformal symmetry.** The massless Klein–Gordon and Maxwell actions have more symmetries than the Poincaré group. Do they have biquaternion Noether currents, and does the tracelessness of the electromagnetic energy–momentum tensor — established in the energy–momentum exercise — express one of them?

4. **The axial current and the two parts.** With the linear mass term the vector phase current is conserved for the massive field, so the open question is the axial one. The divergence identity $\sum_\mu\partial j_{5\mu}/\partial R_\mu = 2im\,\mathrm{Sc}(\tilde{Ξ}^*\tilde{Ξ}\vec e_y)$ holds for the chiral pair, and its biquaternion reading is that the mass couples the two parts off the diagonal. Is there a Noether derivation that starts from the axial rotation $\tilde{Ξ}\mapsto\tilde{Ξ}(\cos\alpha+\sin\alpha\vec e_z)$ rather than from the pair — and does the central-element structure supply anything analogous to the would-be Goldstone statement?

5. **The current of the complexified theory.** In the complexified biquaternion theory of the Maxwell article, the source and potential are fully complex. Does the central-phase current acquire components outside $\mathbb{B}_{\Phi}$, and are they conserved?

6. **Empirical content.** As everywhere in the framework, the currents derived here are the standard ones in new notation. Whether the biquaternion packaging imposes any constraint that the four-vector formulation does not is not established here.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. The two-sided basis operators act on the module by $L_a\tilde{Ξ}=a\tilde{Ξ}$ and $R_b\tilde{Ξ}=\tilde{Ξ} b$, with $L_aR_bL_cR_d=L_{ac}R_{db}$, and the frame of the article is

$$
\gamma_0=iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},\quad
\gamma_1=iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\quad
\gamma_2=iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\quad
\gamma_3=iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\quad
\gamma_5=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x},\quad
\gamma_1=iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\quad
\gamma_2=iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\quad
\gamma_3=iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\quad
\gamma_5=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z} .
$$

**The body's objects under their gamma names.** Because $L_{\mathrm{pau},e_t}$ is the identity, $\gamma_5=-iR_{\mathrm{pau},\vec e_z}$: the two-valued chirality of the body has the gamma-five basis operator as its display. The generator basis operator of the coordinate $x_\mu$ is $\gamma_\mu$, so the vector current of the body is $\tilde{Ξ}^{\dagger}iR_{\mathrm{axf},\vec e_x}\gamma_\mu\tilde{Ξ}$, and the Dirac adjoint is $\tilde{Ξ}^{\dagger}\gamma_0$, since $\gamma_0=iR_{\mathrm{pau},\vec e_x}$. The axial current's basis operator is a product of two frame basis operators, and the two units $\vec e_z$ and $\vec e_{\tau(\mu)}$ of the body's axial current are exactly that product:

$$
\bigl(iL_{\mathrm{pau},e_\mu}R_{\mathrm{pau},\vec e_{\tau(\mu)}}\bigr)\bigl(-iR_{\mathrm{pau},\vec e_z}\bigr)
= L_{\mathrm{pau},e_\mu}R_{\mathrm{pau},\vec e_z\vec e_{\tau(\mu)}}
= \gamma_\mu\gamma_5 ,
$$

In the axis-free display:

$$
\bigl(iL_{\mathrm{axf},e_\mu}R_{\mathrm{axf},\vec e_{\tau(\mu)}}\bigr)\bigl(-iR_{\mathrm{axf},\vec e_z}\bigr)
= L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},\vec e_z\vec e_{\tau(\mu)}}
= \gamma_\mu\gamma_5 ,
$$

so the two imaginary units the body cancels are the two that the gamma names carry, and $j_{5\mu}=\tilde{Ξ}^{\dagger}iR_{\mathrm{axf},\vec e_x}\gamma_\mu\gamma_5\tilde{Ξ}$. The single collapse behind it, and behind every simplification of the frame, is

$$
i\,\gamma_\mu = -L_{\mathrm{pau},e_\mu}R_{\mathrm{pau},\vec e_{\tau(\mu)}} ,
$$

The same identities in the axis-free display:

$$
i\,\gamma_\mu = -L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},\vec e_{\tau(\mu)}} ,
$$

by $i^2=-1$: multiplying a generator basis operator by $i$ trades it for a plain one, which is why a product of four generator basis operators carries $i^4=+1$ and no residual unit. Under the same identity the mass term of the two-sided equation, $-mi\,\bar F\vec e_z$ in the body, is $m\,\bar F\gamma_5$ in the frame: right multiplication by $\vec e_z$ is the basis operator $i\gamma_5$, so $(-mi)(i\gamma_5)\bar F=-m\,i^2\gamma_5\bar F=+m\,\gamma_5\bar F$.

**The central grading.** The basis operator $\gamma_5$ is not the grading itself. The central grading $\xi_{\mathrm{ad}}=i\tilde{Ζ}_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, with $\tilde{Ζ}_{\mathrm{ad}}^2=-e_t$ and so $\xi_{\mathrm{ad}}^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module. That is how the two Dirac equations meet: the one-sided pair carries $\xi_{\mathrm{ad}}$ as a central sign, while the mass of the two-sided equation is a right multiplication by the chirality basis operator, and the basis operator is the representative of the sign on the module.

**The identities of the frame.** With $\varepsilon=(1,-1,-1,-1)$,

$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,
\qquad
(\gamma_\eta)^2=-I_4,
\qquad
\gamma_5^2=I_4,
\qquad
\{\gamma_\mu,\gamma_5\}=0 ,
$$

the anticommutation with $\gamma_5$ being what makes the chirality basis operator the axial insertion. The first relation is the quaternion multiplication table in the frame: a basis operator that pairs $e_t$ with a spatial unit squares to the square of that unit, and the central $i$ of each generator flips the sign, so the timelike basis operator squares to $+I_4$ and the three spatial ones to $-I_4$. The bracket carries the weight, and the reason is again $i^2$: each $\gamma_\mu$ is $i$ times the plain basis operator $L_{\mathrm{pau},e_\mu}R_{\mathrm{pau},\vec e_{\tau(\mu)}}$, whose own Clifford bracket is $-2\varepsilon_\mu\delta_{\mu\nu}I_4$, so the two factors of $i$ inside the bracket turn it into $+2\varepsilon_\mu\delta_{\mu\nu}I_4$.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the plain basis operators span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$, the two Clifford algebras that differ by that relative $i$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{\mathrm{axf},e_\mu}=C_{\Pi}L_{\mathrm{pau},e_\mu}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a basis operator named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

Noether's theorem in biquaternionic form joins the two ends that *Relativistic Mechanics in Biquaternionic Form* states separately, the free-particle action and the conserved four-current, by deriving the second from the first. The theorem has two forms. For an **internal** symmetry, that of the central phase $\tilde{Ξ}\mapsto \exp(i\alpha)\tilde{Ξ}$ of the complex biquaternion scalar field, the derived current is

$$
\tilde{J}_{\Phi} = i\left[(\tilde\nabla_\Phi\tilde{Ξ}^{*})\tilde{Ξ} - \tilde{Ξ}^{*}(\tilde\nabla_\Phi\tilde{Ξ})\right] = \sum_\nu J_\nu e_\nu,
\qquad J_\nu = i\left(\xi_{\mathrm{scl}}\,\partial/\partial R_\nu\,{\xi_{\mathrm{scl}}}^{*} - {\xi_{\mathrm{scl}}}^{*}\partial/\partial R_\nu\,\xi_{\mathrm{scl}}\right),
$$

which lies in $\mathbb{B}_{\Phi}$ and satisfies the Noether identity

$$
\mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}\right) = i\,\mathrm{Sc}\!\left[(\Box_\Phi\tilde{Ξ}^{*})\tilde{Ξ} - \tilde{Ξ}^{*}(\Box_\Phi\tilde{Ξ})\right],
$$

zero whenever the field is on shell. This is the framework form of $\langle\tilde\nabla_\Phi,\tilde J_{\Phi}\rangle_{\natural} = 0$; it reproduces the current the Klein–Gordon article posits, up to the conventional constant $c/k_m/2$, with $\rho>0$ on a positive-frequency wave; and its expansion at the Maxwell source is the charge-conservation condition $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\sqrt{\mu}\,\tilde{J}_{\Phi}) = 0$.

The same phase acts on the Dirac field, whose dynamics is the chiral pair $\tilde\nabla_\Phi\tilde{Ξ}_{R}=k_m\tilde{Ξ}_{L}$, $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=k_m\tilde{Ξ}_{R}$, equivalently the one equation on the algebra $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}=-mi\bar{\tilde{Ξ}}\vec e_z$. The vector current has the components $j_\mu=\mathrm{Sc}(\tilde{Ξ}^*e_\mu\tilde{Ξ}\,b_\mu)$, with $b_t=e_t$ and $b_k=\vec e_z$, conserved at every $m$; the axial current carries the unit $\vec e_z$ inside the product and obeys $\sum_\mu\partial j_{5\mu}/\partial R_\mu = 2im\,\mathrm{Sc}(\tilde{Ξ}^*\tilde{Ξ}\vec e_y)$, vanishing only at $m=0$. The mass therefore breaks the axial rotation and not the phase.

For a **spacetime** symmetry, translation invariance gives the four-momentum

$$
\tilde{P}_{\Phi} = m\tilde{V}_{\Phi} = i\frac{E}{c}e_t + \vec p,
\qquad E = \gamma mc^2,\quad \vec p = \gamma m\vec v,
$$

as the Noether charge, conserved for a free particle. The conservation law for a system is the vanishing of the **coordinate**-time derivative of the total, $d\tilde{P}_{\Phi,\mathrm{tot}}/dt' = c\,d\tilde{P}_{\Phi,\mathrm{tot}}/dr'_t = 0$; the parent's proper-time four-force cannot be summed across bodies, and the correct form is $\sum_a\tilde{\mathcal F}_{\mathrm{frc},a}/(c\gamma_a) = 0$, or the integrated $\sum_{\mathrm{in}}\tilde{P}_{\Phi} = \sum_{\mathrm{out}}\tilde{P}_{\Phi}$. A translation acts on a plane wave by the central unit-modulus phase $\exp(i\,\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_{\Phi,0}^{\natural})/\hbar)$, with $\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_{\Phi,0}^{\natural}) = \vec k_\Phi\cdot\vec R_0-\omega r'_{t,0}/c$.

The field translation current is the canonical energy–momentum, $-\partial T_{0\nu}/\partial x_0+\sum_\eta\partial T_{\eta\nu}/\partial r_\eta = 0$ on shell in the real coordinates, with positive energy density $T_{00} = |\partial\xi_{\mathrm{scl}}/\partial r'_t|^2 + |\nabla\xi_{\mathrm{scl}}|^2 + k_m^{2}|\xi_{\mathrm{scl}}|^2$. Rank two cannot be one biquaternion, so the framework packages it bilinearly; the Maxwell object $\tilde{W}_{\Psi} = \tfrac12\tilde{F}\tilde{F}^{*}$ is its time row, and $\mathrm{Sc}(\tilde\nabla_\Phi\tilde{W}_{\Psi}) = \frac{i}{c}\vec J\cdot\vec E$ is the energy law it carries. Lorentz invariance gives the angular-momentum bivector $\tilde L = \tfrac12\sum L_{\mu\nu}\,e^{\natural}_\mu e_\nu$, with the rank-three field current reduced to the rank-two particle bivector only when the spin term vanishes. The theorem is standard; the algebra supplies the home of each conserved object and the compact form of its divergence, and it supplies no conservation law the symmetries did not already give.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_\eta^2 = -e_t$; $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$, $\varepsilon=(1,-1,-1,-1)$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{B}_{\Phi}, \mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{B}_{H}, \mathbb{B}_{C} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ | Real-quaternion subspace; complex scalar line (the centre) |
| $\tilde{\nabla} = e_t\partial/\partial R_t + \sum_\mu\,\vec e_\mu\,\partial/\partial R_\mu$ | Biquaternionic gradient |
| $\tilde{\nabla}^{\natural} = e_t\partial/\partial R_t - \sum_\mu\,\vec e_\mu\,\partial/\partial R_\mu$ | Quaternion-conjugate gradient; $\mathrm{Sc}(e_\mu^{\natural}e_\nu)=\delta_{\mu\nu}$ |
| $\Box_\Phi = \tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}= (\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi = \Delta_\Phi - \partial^2/\partial {r^{\prime}_t}^2$ | d'Alembertian, $Q_t=i q'_t$ |
| $S = -mc\int\sqrt{-d\tilde R_\Phi\,d\tilde{R}_\Phi^{\natural}}$ | Free-particle action |
| $\mathrm{Lag} = -mc^2\sqrt{1-\vec v^2/c^2}$ | Free-particle Lagrangian |
| $\tilde R_\Phi = i r'_{t}\,e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ | Four-position, in $\mathbb{B}_{\Phi}$ |
| $\tilde{R}_{\Phi,0}\in\mathbb{B}_{\Phi}$ | Constant translation (displacement) |
| $\tilde{V}_{\Phi} = \gamma(ic\,e_t + \vec v)$ | Four-velocity, $\tilde{V}_{\Phi}\tilde{V}_{\Phi}^{\natural} = -c^2$ |
| $\tilde{P}_{\Phi} = m\tilde{V}_{\Phi} = iE/c\,e_t + \vec p$ | Four-momentum, Noether charge of translation; real energy and momentum, so in $\mathbb{B}_{\Phi}$ |
| $\tilde{\mathcal F}_{\mathrm{frc},a} = d\tilde{P}_{\Phi,a}/d\tau_a$ | Four-force (proper-time derivative; not summable) |
| $\tilde{Ξ} = \xi_{\mathrm{scl}}\,e_t\in\mathbb{B}_{C}$ | Complex biquaternion scalar field |
| $\mathcal{L} = \sum_\mu(\partial{\xi_{\mathrm{scl}}}^{*}/\partial R_\mu)(\partial\xi_{\mathrm{scl}}/\partial R_\mu) + k_m^{2}|\xi_{\mathrm{scl}}|^2$ | Field Lagrangian density, $Q$ frame |
| $\tilde{J}_{\Phi} = i[(\tilde\nabla_\Phi\tilde{Ξ}^{*})\tilde{Ξ} - \tilde{Ξ}^{*}\tilde\nabla_\Phi\tilde{Ξ}]$ | Central-phase Noether current, in $\mathbb{B}_{\Phi}$ |
| $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}) = \langle\tilde\nabla_\Phi,\tilde J_{\Phi}\rangle_{\natural} = \sum_\mu\partial J_\mu/\partial R_\mu$ | Divergence of the current, plain sum |
| $\tilde J_{\Phi} = ic\rho\,e_t + \vec J$ | Maxwell source $\sqrt{\mu}\,\tilde J_{\Phi}$; $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}) = 0$ is charge conservation |
| $\tilde{Ξ}=\tilde{Ξ}_{L}+\tilde{Ξ}_{R}$ | The Dirac field, an element of $\mathbb{B}$; the value of $\tilde{Ξ}_{L}$ is $-1$, of $\tilde{Ξ}_{R}$ is $+1$ |
| $\tilde{Ξ}^*$ | The adjoint with which the currents are formed: the algebra's conjugation |
| $j_\mu=\mathrm{Sc}(\tilde{Ξ}^*e_\mu\tilde{Ξ}\,b_\mu)$, $b_t=e_t$, $b_k=\vec e_z$ | Vector current of the Dirac field; $j_t$ is its Hermitian norm |
| $j_{5\mu}=\mathrm{Sc}(\tilde{Ξ}^*ie_\mu\tilde{Ξ}\,\vec e_z\vec e_{\tau(\mu)}\vec e_x)$, $\tau(t)=x$, $\tau(k)=y$ | Axial current; $\sum_\mu\partial j_{5\mu}/\partial R_\mu=2im\,\mathrm{Sc}(\tilde{Ξ}^*\tilde{Ξ}\vec e_y)$ |
| $x_\mu = (r'_{t},r_x,r_y,r_z)$ | Real coordinates of the energy–momentum tensor, the chart of $Q_\mu$ at $Q_t=i q'_t$ |
| $T_{\mu\nu} = (\partial{\xi_{\mathrm{scl}}}^*/\partial x_\mu)(\partial\xi_{\mathrm{scl}}/\partial x_\nu) + (\partial\xi_{\mathrm{scl}}/\partial x_\mu)(\partial{\xi_{\mathrm{scl}}}^*/\partial x_\nu) + \varepsilon_\mu\delta_{\mu\nu}\mathcal{L}_{\mathrm{scl},\xi}$ | Canonical energy–momentum in the real coordinates; the coefficient of $\mathcal{L}_{\mathrm{scl},\xi}$ is the plain form of the two units |
| $\tilde{W}_{\Psi} = \tfrac12\tilde{F}\tilde{F}^{*} = W\,e_t + \frac{i}{c}\vec S$ | Maxwell energy–momentum (time row), in $\mathbb{B}_{\Psi}$; $\mathrm{Sc}(\tilde\nabla_\Phi\tilde W_{\Psi})=\frac{i}{c}\vec J\cdot\vec E$ |
| $L_{\mu\nu} = x_\mu p_\nu - x_\nu p_\mu$, $\tilde L = \tfrac12\sum L_{\mu\nu}\,e^{\natural}_\mu e_\nu$ | Angular momentum and its bivector |
| $\tilde P_{\Phi} = i\frac{\omega}{c}e_t + \vec k_\Phi$ | Four-wavevector, in $\mathbb{B}_{\Phi}$; plane-wave phase $\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_\Phi^{\natural}) = \vec k_\Phi\cdot\vec r-\omega r'_t/c$ |
| $\exp(i\,\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_{\Phi,0}^{\natural})/\hbar)$, $\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_{\Phi,0}^{\natural})=\vec k_\Phi\cdot\vec R_0-\omega r'_{t,0}/c$ | Central translation multiplier on a plane wave, of unit modulus |
| $\operatorname{Tr}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})=\operatorname{Tr}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi)=2\langle\tilde{Ϛ}_{\Psi},\tilde H_\Psi\rangle_{*} = 2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})$ | Trace formula of the informational sector, $\tilde H_\Psi$ Hermitian |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle=\varepsilon_\mu Q_{1\mu}Q_{2\mu}$ | the general plain bilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2)$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{\natural}=\langle\tilde{Q}_2\rangle_{\natural}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- [Relativistic Mechanics in Biquaternionic Form](relativistic-mechanics-in-biquaternionic-form.html) — the action and the conserved current this article starts from.
- [The Klein–Gordon Equation in Biquaternionic Form](the-klein-gordon-equation-in-biquaternionic-form.html) — the field, its Lagrangian form, and the current the Noether derivation reproduces.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) — the chiral pair, the frame in the basis operator algebra, and Kravchenko's two-sided dictionary.
- [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html) — the mass term, the two parts of the Dirac field, and the axial current.
- [The Poincaré Group and the Biquaternion Frame](the-poincare-group-and-the-biquaternion-frame.html) — the symmetry group, and the corrected central translation phase.
- [Exercise: Four-Momentum Conservation in a Collision](exercise-four-momentum-conservation-in-a-collision.html) — the total four-momentum of an isolated system, and the report of the proper-time four-force defect.
- [Exercise: The Electromagnetic Energy–Momentum Tensor](exercise-the-electromagnetic-energy-momentum-tensor.html) — the rank-two translation current and why one biquaternion cannot carry it.
- [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html) — the source conservation and the energy–momentum biquaternion $\tilde{W}_{\Psi}$.
- [The Field-Strength Biquaternion and Its Invariants](the-field-strength-biquaternion-and-its-invariants.html) — the bivector representation used for the angular momentum.
- [Angular Momentum and Spin in Biquaternionic Form](angular-momentum-and-spin-in-biquaternionic-form.html) — the angular-momentum algebra and the spin operators.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html) — the localization of the central phase whose global current is derived here.
- [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html) — the connection forced by localizing the same symmetry.
- [The Lorentz Transformation as a Biquaternionic Rotation](the-lorentz-transformation-as-a-biquaternionic-rotation.html) — the rotor whose conjugation carries the four-momentum between frames.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) and [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html) — the two sectors that house the conserved objects.
- [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html) — the algebra, its conjugations, and the local complex structure.
