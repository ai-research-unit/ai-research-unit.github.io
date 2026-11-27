# __Noether's Theorem in Biquaternionic Form__

## Introduction

Noether's theorem connects two things a physical theory supplies separately: its **symmetries** and its **conservation laws**. Every continuous symmetry of an action corresponds to a conserved quantity, and in a field theory to a conserved current. The theorem is not specific to any algebra, so writing it biquaternionically does not by itself produce a conservation law that was not already there. What the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ fixes is the **form** the theorem takes: which subspace the conserved objects live in, how a symmetry acts on a biquaternion-valued field, and which biquaternion expressions are the currents.

**The theorem is universal; the columns are not.** The identity behind every display below — the current's divergence is the field equation contracted with the symmetry variation — holds for any carrier, and what the rung fixes is the *pairing* the current is read with: the Hermitian form for the complex scalar, the spinor bilinear for the Dirac field, the weighted vector sum for the Proca field, the trace for the matrix rung. **Two columns are worked here, the scalar and the Dirac; the other three are named in [The Rung Dictionary](the-rung-dictionary-what-the-general-symbols-mean-at-each-rung.html) and computed in their band articles**, and a reader who needs them should not read a scalar display as a general one — the order of the factors in the bilinear is what changes, and at a rung whose values do not commute it changes the current.

The two ends of the theorem are both already in the read list. *Relativistic Mechanics in Biquaternionic Form* gives the free-particle action

$$
S = -mc\int\sqrt{-\,d\tilde R_\Phi\,d\tilde{R}_\Phi^{\natural}},
$$

whose integrand is built from the biquaternion norm of the displacement biquaternion, and it gives the conservation of the four-current in the framework form $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}) = 0$. This article joins the two ends: it derives the current from the symmetry of the action, for the two kinds of symmetry the framework contains.

**Two kinds of symmetry.** A relativistic action has

- **internal** symmetries, which do not move the spacetime point — here the central phase $\tilde{Ξ}\mapsto \exp(i\theta_{\mathrm{cen}})\tilde{Ξ}$ of a complex biquaternion field, the symmetry whose localization is the minimal coupling; and
- **spacetime** symmetries, the Poincaré transformations — four translations $\tilde R_\Phi\mapsto\tilde R_\Phi+\tilde{R}_{\Phi,0}$ and six Lorentz transformations $\tilde R_\Phi\mapsto\tilde U\tilde R_\Phi\tilde U^{*}$. Translation invariance gives the conserved four-momentum; Lorentz invariance gives the conserved angular momentum.

The internal case produces a current biquaternion $\tilde{J}_{\Phi}\in\mathbb{B}_{\Phi}$ with $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi})=0$ on shell, the framework form of $\sum_{\imath}\partial J_{\imath}/\partial R_{\imath} = 0$. The spacetime case produces an energy–momentum current and an angular-momentum bivector.

**What is established, and what is not.** Established below, and recomputed: the central-phase current of the complex biquaternion scalar field,

$$
\tilde{J}_{\Phi} = i\left[(\tilde\nabla_\Phi\tilde{Ξ}^{*})\tilde{Ξ} - \tilde{Ξ}^{*}(\tilde\nabla_\Phi\tilde{Ξ})\right],
$$

lies in $\mathbb{B}_{\Phi}$ and satisfies $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}) = i\,\mathrm{Sc}[(\Box_\Phi\tilde{Ξ}^{*})\tilde{Ξ} - \tilde{Ξ}^{*}(\Box_\Phi\tilde{Ξ})]$, which vanishes whenever the field obeys the Klein–Gordon equation, the sign of $\tilde{J}_{\Phi}$ being the one for which the charge density of a positive-frequency wave is positive; the same current for the Dirac field, whose components are $j_{\imath}=\mathrm{Sc}(\tilde{Ξ}^*e_{\imath}\tilde{Ξ}\,b_{\imath})$ with $b_t=e_t$ and $b_{\imath}=\vec e_z$, conserved at every mass, while the axial current is conserved only at $m=0$; the free-particle four-momentum $\tilde{P}_{\Phi} = m\tilde{V}_{\Phi}$ is the Noether charge of translation invariance, and the **total** four-momentum of an isolated system is conserved; and a translation acts on a plane wave by the central unit-modulus phase $\exp(-i\theta_{\mathrm{pwp}})$. What is standard, what is only transcribed, and what is interpretation is separated in its own section below.

The angle is the Minkowski pairing of the four-momentum with the position, $\theta_{\mathrm{pwp}}=\omega r'_t/c-2\pi\vec\nu_\Phi\cdot\vec r$: both factors are real, so the angle is real, and the wave is $\tilde\Xi=\tilde\Xi_0\exp(-i\theta_{\mathrm{pwp}})$.

**Two defects in the read list, handled rather than repeated.** First, the four-force of the parent is defined by the **proper**-time derivative, $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = d\tilde{P}_{\Phi}/d\tau$, so the sum $\sum_a\tilde{\mathcal F}_{\mathrm{frc},a}$ across bodies is *not* the rate of change of the total four-momentum unless all the Lorentz factors agree; *Exercise: Four-Momentum Conservation in a Collision* reports this, and the conservation law is stated correctly below. Second, the translation of a plane wave is by a **central phase**, $\exp(-i\theta_{\mathrm{pwp}})$, and the $i$ is not optional: the same scalar in a real exponential, $\exp(\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_{\Phi,0}^{\natural}))$, is a dilation and not a phase at all.

**Symbols and signs.** Everything the later sections use is fixed once in §*Conventions* below: the algebra and its four conjugations, the two sectors, the gradient and the d'Alembertian with the imaginary temporal coordinate, the two pairings, the units, the plane-wave angle, and the one overall sign that the Lagrangian, the current and the energy–momentum tensor share.

**The Dirac field, once.** The Dirac content of the later sections is the element $\tilde{Ξ}=\tilde{Ξ}_{L}+\tilde{Ξ}_{R}$ of $\mathbb{B}$, whose two parts carry the two values: the value of $\tilde{Ξ}_{L}$ is $-1$, the value of $\tilde{Ξ}_{R}$ is $+1$, and only the zero element carries both. A product takes the value of its right factor, and left multiplication keeps the value, so the two parts are stable under multiplication on the left. The adjoint with which the currents are formed is the algebra's own conjugation, $\tilde{Ξ}^*$. The same objects under their legacy names are collected in the closing section *The Legacy Pauli Gamma Formulation*, and none of those names is used before it.

## Conventions

The symbols and the signs are fixed once, here, so that the derivations below can be checked without the companion articles.

**The algebra.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with $e_t=1$ and $\vec e_x,\vec e_y,\vec e_z$ the quaternion units, $\vec e_{\imath}^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ cyclically. An element is $\tilde Q=Q_te_t+\vec Q$ with four complex coefficients, $\mathrm{Sc}\,\tilde Q=Q_t$ is its **scalar part**, and $\mathrm{Sc}(e_{\imath}e_{\jmath})=\varepsilon_{\imath}\delta_{\imath\jmath}$ with $\varepsilon=(1,-1,-1,-1)$.

| map | mark | action on $\tilde Q=Q_te_t+\vec Q$ |
|---|---|---|
| complex conjugation | $\bar{\cdot}$ | conjugates the four coefficients, keeps the basis |
| quaternion conjugation | ${}^{\natural}$ | fixes $Q_t$, negates $\vec Q$ |
| Hermitian conjugation | ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ | $Q_t^{*}=\overline{Q_t}$, $\vec Q^{*}=-\overline{\vec Q}$ |
| anti-Hermitian | ${}^{\flat}=-{}^{*}$ | minus the star |

**The sectors.** $\mathbb{B}_{\Phi}$ is the $\flat$-fixed space, the **material** sector, which holds the four-vectors, $\tilde R_\Phi=ir'_t\,e_t+\vec r$ with $r'_t$ and $\vec r$ real. $\mathbb{B}_{\Psi}$ is the $*$-fixed space, the **informational** sector. $\mathbb{B}_{C}=\mathrm{span}_{\mathbb{R}}\{e_t,ie_t\}$ is the centre, and a field in it is $\tilde\Xi=\xi_{\mathrm{scl}}e_t$.

**The coordinates and the operators.** $R_t=ir'_t$, so $\partial/\partial R_t=-i\,\partial/\partial r'_t$; the gradient is $\tilde\nabla_\Phi=\sum_{\imath}e_{\imath}\partial/\partial R_{\imath}$ and $\Box_\Phi=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=\Delta_\Phi-\partial^{2}/\partial{r'_t}^{2}$, where $\Delta_\Phi=\sum_{\imath\in\{x,y,z\}}\partial^{2}/\partial R_{\imath}^{2}$. **The temporal derivative is not a real operator**, so $\partial(\xi^{*})/\partial R_t$ is $+i$ times the conjugate of $\partial\xi/\partial R_t$ and not $-i$; every time component below uses the derivative acting on the function it is written on, never the conjugate of a derivative.

**The pairings.** $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$, the bilinear form, complex and indefinite of realified inertia $(4,4)$; $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$, the Hermitian form, real and positive definite of realified inertia $(8,0)$. The field Lagrangian uses the second.

**The units.** $m$ a mass, $c$ the speed of light in the medium ($c_0$ in vacuum), $\vec v$ a particle or frame velocity, $d^{4}r=dr'_t\,dx\,dy\,dz$. The mass enters as an inverse length, the **mass parameter** $m_0:=mc$, whose square carries the dimensions of $\Box_\Phi$, and the **mass wave number** is $\nu_m:=m_0/(2\pi)$.

**The plane wave.** $\theta_{\mathrm{pwp}}=\omega r'_t/c-2\pi\vec\nu_\Phi\cdot\vec r\in\mathbb{R}$ and $\tilde\Xi=\tilde\Xi_0\exp(-i\theta_{\mathrm{pwp}})$, with $\omega$ an angular frequency and $\vec\nu_\Phi$ a spatial wave number. With $\tilde P_{\Phi}=i\frac{\omega}{c}e_t+2\pi\vec\nu_\Phi$ this is $\tilde\Xi\propto\exp(-i\theta_{\mathrm{pwp}})=\exp(i\,\mathrm{Sc}(\tilde P_{\Phi}\tilde R_\Phi^{\natural}))$, and the mass shell is $\omega^{2}=c^{2}4\pi^{2}\vec\nu_\Phi^{2}+m_0^{2}c^{2}$.

**The one sign that matters.** Three objects carry a common overall sign, and the choice is fixed by the positivity of the energy density, not by convenience:

| object | convention of this article | under $\mathcal{L}\mapsto-\mathcal{L}$ |
|---|---|---|
| field equation | $(\Box_\Phi-m_0^{2})\tilde\Xi=0$ | unchanged |
| central-phase current $\tilde J_{\Phi}$ | $i[(\tilde\nabla_\Phi\tilde\Xi^{*})\tilde\Xi-\tilde\Xi^{*}\tilde\nabla_\Phi\tilde\Xi]$, $\rho>0$ on a positive-frequency wave | negated |
| canonical tensor $T_{\imath\jmath}$ | $A_{\imath\jmath}+\varepsilon_{\imath}\delta_{\imath\jmath}\mathcal{L}$, $T_{00}>0$ | the $A$ part unchanged, the $\mathcal{L}$ part flips |

The Lagrangian density is therefore
$$
\mathcal{L}=+\,\mathrm{Sc}\!\left[((\tilde\nabla_\Phi)^{\natural}\tilde\Xi^{*})(\tilde\nabla_\Phi\tilde\Xi)\right]+m_0^{2}\,\mathrm{Sc}\!\left[\tilde\Xi^{*}\tilde\Xi\right]
=-\,\Bigl\lvert\frac{\partial\xi_{\mathrm{scl}}}{\partial r'_t}\Bigr\rvert^{2}+\bigl\lvert\vec\nabla_\Phi\xi_{\mathrm{scl}}\bigr\rvert^{2}+m_0^{2}\lvert\xi_{\mathrm{scl}}\rvert^{2},
$$
with the uniform $+$ in the $Q$ frame, which is what makes its temporal term negative once the derivative is written in the real coordinates. The companion variational article writes the same functional with these signs, so the two agree symbol for symbol; the sign of the current and of the tensor is the one for which the plane wave has a positive charge density and a positive energy density, and the alternative, if it is used, is obtained by the mapping in the table and not component by component.

**The coordinate charts.** The gradient is taken with respect to the coefficients $Q_{\imath}$ with $Q_t=i q'_t$, and the energy–momentum tensor is written in the real coordinates $x_{\imath}=(r'_t,r_x,r_y,r_z)$, which are the same chart with the $i$ of the time coefficient removed. The two are held apart where they are used, and §*A caution on the $i r'_t$ convention* states what mixing them costs.

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
\mathcal{L} = +\,\mathrm{Sc}\!\left[((\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}^{*})(\tilde\nabla_\Phi\tilde{Ξ})\right] + 4\pi^{2}\nu_m^{2}\,\mathrm{Sc}\!\left[\tilde{Ξ}^{*}\tilde{Ξ}\right].
$$

Because $\mathrm{Sc}(e_{\imath}^{\natural}e_{\jmath})=\delta_{\imath\jmath}$, the first term expands over the four coordinates with a single sign,

$$
\mathcal{L} = +\frac{\partial{\xi_{\mathrm{scl}}}^{*}}{\partial R_t}\frac{\partial\xi_{\mathrm{scl}}}{\partial R_t}
+\sum_{\imath\in\{x,y,z\}}\frac{\partial{\xi_{\mathrm{scl}}}^{*}}{\partial R_{\imath}}\frac{\partial\xi_{\mathrm{scl}}}{\partial R_{\imath}}
+4\pi^{2}\nu_m^{2}\,{\xi_{\mathrm{scl}}}^{*}\xi_{\mathrm{scl}} ,
$$

the uniform signs being what the $\natural$ conjugation supplies. The time term is nevertheless negative, because $\partial/\partial R_t=\partial/\partial i r'_t$ acts on both factors and two applications of it give $-\partial^2/\partial {r'_t}^2$; in the real coordinates $x_{\imath}=(r'_{t},r_x,r_y,r_z)$ the same expression reads

$$
\mathcal{L} = -\left|\frac{\partial\xi_{\mathrm{scl}}}{\partial r'_t}\right|^2 + |\vec\nabla_\Phi\xi_{\mathrm{scl}}|^2 + 4\pi^{2}\nu_m^{2}\lvert\xi_{\mathrm{scl}}\rvert^2 .
$$

This is the form used with the energy–momentum tensor below. The Euler–Lagrange equation of $\mathcal{L}$ is the biquaternion Klein–Gordon equation

$$
\left(\Box_\Phi - 4\pi^{2}\nu_m^{2}\right)\tilde{Ξ} = 0,
$$

the overall sign of $\mathcal{L}$ being immaterial for the equation and fixed here by the positivity of the energy density. Both the action and the equation are those of the read list; $\mathcal{L}$ is exhibited only because a Noether current is read off a Lagrangian. Here $\nu_m$ is the mass wave number, the inverse of the mass length up to $2\pi$.

### Symmetries of the Action and of the Equations

A one-parameter family $\tilde{Ξ}_\varepsilon$ with $\tilde{Ξ}_0 = \tilde{Ξ}$ is a **symmetry of the action** if $S[\tilde{Ξ}_\varepsilon] = S[\tilde{Ξ}]$ for every field configuration, and a **symmetry of the equations of motion** if it preserves the solution set. A symmetry of the action is the stronger notion, and it is the one that yields a conserved current by Noether's theorem.

### The Theorem in the Two Forms the Framework Needs

For an internal symmetry, the theorem states that there is a current biquaternion $\tilde{J}_{\Phi} = J_t\,e_t + \sum_{\imath\in\{x,y,z\}} J_{\imath}\,\vec e_{\imath}$ whose divergence vanishes when the field obeys its equation:

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
\tilde{Ξ}\ \longmapsto\ \exp(i\theta_{\mathrm{cen}})\tilde{Ξ},
\qquad \theta_{\mathrm{cen}}\in\mathbb{R},
$$

leaves both terms of $\mathcal{L}$ unchanged, because $\exp(i\theta_{\mathrm{cen}})$ is central and $\tilde{Ξ}^{*}\mapsto \exp(-i\theta_{\mathrm{cen}})\tilde{Ξ}^{*}$: the two phase factors in $((\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}^{*})(\tilde\nabla_\Phi\tilde{Ξ})$ cancel, and $\tilde{Ξ}^{*}\tilde{Ξ}$ is invariant. The symmetry therefore holds for the **massive** field as well as the massless one, because the mass term depends on $\tilde{Ξ}$ only through the invariant $\tilde{Ξ}^{*}\tilde{Ξ}$ — a fact used again below.

**The variation, in one display.** Let the phase depend on the point, $\delta\xi_{\mathrm{scl}}=i\theta_{\mathrm{cen}}(x)\xi_{\mathrm{scl}}$ and $\delta{\xi_{\mathrm{scl}}}^{*}=-i\theta_{\mathrm{cen}}(x){\xi_{\mathrm{scl}}}^{*}$, and expand the variation of the action, integrating the derivative term by parts:

$$
\delta S=\int\Big[\frac{\partial\mathcal{L}}{\partial\xi_{\mathrm{scl}}}\,\delta\xi_{\mathrm{scl}}+\frac{\partial\mathcal{L}}{\partial(\partial\xi_{\mathrm{scl}}/\partial R_{\jmath})}\,\partial/\partial R_{\jmath}\,\delta\xi_{\mathrm{scl}}+\text{c.c.}\Big]d^{4}r
=\int\Big[\frac{\partial\mathcal{L}}{\partial\xi_{\mathrm{scl}}}-\frac{\partial}{\partial R_{\jmath}}\frac{\partial\mathcal{L}}{\partial(\partial\xi_{\mathrm{scl}}/\partial R_{\jmath})}\Big]\delta\xi_{\mathrm{scl}}\,d^{4}r+\oint_{\partial\Omega}\frac{\partial\mathcal{L}}{\partial(\partial\xi_{\mathrm{scl}}/\partial R_{\jmath})}\,\delta\xi_{\mathrm{scl}}\,n_{\jmath}\,d\Sigma .
$$

The surface term is the one §*The boundary term* of the variational article keeps or drops; for variations vanishing on the boundary it is zero, and the volume term exhibits the Euler–Lagrange operator. Writing $\delta\xi_{\mathrm{scl}}=i\theta_{\mathrm{cen}}\xi_{\mathrm{scl}}$ in it and using that $\mathcal{L}$ is invariant for **constant** $\theta_{\mathrm{cen}}$, the part proportional to $\partial_{\jmath}\theta_{\mathrm{cen}}$ is isolated: it must vanish separately, because $\theta_{\mathrm{cen}}$ is arbitrary inside the integral, and it is

$$
\delta S\Big|_{\partial\theta_{\mathrm{cen}}}=\int\partial_{\jmath}\theta_{\mathrm{cen}}\;i\left(\frac{\partial{\xi_{\mathrm{scl}}}^{*}}{\partial R_{\jmath}}\,\xi_{\mathrm{scl}}-\frac{\partial\xi_{\mathrm{scl}}}{\partial R_{\jmath}}\,{\xi_{\mathrm{scl}}}^{*}\right)d^{4}r .
$$

**The current is the bracket.** Reading the coefficient of $\partial_{\jmath}\theta_{\mathrm{cen}}$ as $J_{\jmath}$, and noting that $\partial\mathcal{L}/\partial(\partial\xi_{\mathrm{scl}}/\partial R_{\jmath})=+\partial{\xi_{\mathrm{scl}}}^{*}/\partial R_{\jmath}$ and $\partial\mathcal{L}/\partial(\partial{\xi_{\mathrm{scl}}}^{*}/\partial R_{\jmath})=+\partial\xi_{\mathrm{scl}}/\partial R_{\jmath}$ for the Lagrangian of §*The Field*, which is what supplies the two terms,

$$
J_{\jmath} = \frac{\partial\mathcal{L}}{\partial(\partial\xi_{\mathrm{scl}}/\partial R_{\jmath})}\,\delta\xi_{\mathrm{scl}} + \frac{\partial\mathcal{L}}{\partial(\partial{\xi_{\mathrm{scl}}}^{*}/\partial R_{\jmath})}\,\delta{\xi_{\mathrm{scl}}}^{*}
= i\theta_{\mathrm{cen}}\left(\frac{\partial{\xi_{\mathrm{scl}}}^{*}}{\partial R_{\jmath}}\,\xi_{\mathrm{scl}} - \frac{\partial\xi_{\mathrm{scl}}}{\partial R_{\jmath}}\,{\xi_{\mathrm{scl}}}^{*}\right).
$$

The two displays are one statement: the first is the integration by parts, the second is the coefficient that survives it. Setting $\theta_{\mathrm{cen}} = 1$ and packaging the four components,

$$
\boxed{\ \tilde{J}_{\Phi} = i\left[(\tilde\nabla_\Phi\tilde{Ξ}^{*})\tilde{Ξ} - \tilde{Ξ}^{*}(\tilde\nabla_\Phi\tilde{Ξ})\right] = \sum_{\jmath} J_{\jmath} e_{\jmath}\ }
\qquad (\tilde{Ξ} = \xi_{\mathrm{scl}}\,e_t).
$$

The overall sign of a current is free — the symmetry with the opposite generator gives the opposite current — and it is fixed here by the charge density, as the next paragraph shows.

### The Current Lies in the Material Sector

The temporal component in the $i r'_t$ basis is $J_t = i\left(\xi_{\mathrm{scl}}\,\frac{\partial{\xi_{\mathrm{scl}}}^{*}}{\partial R_t} - {\xi_{\mathrm{scl}}}^{*}\frac{\partial\xi_{\mathrm{scl}}}{\partial R_t}\right)$. Because $\partial/\partial R_t=-i\,\partial/\partial r'_t$ and the spatial derivatives are plain, the two kinds of component are recorded separately, and the temporal one is carried through with the operator acting on the function it stands on, $\partial{\xi_{\mathrm{scl}}}^{*}/\partial R_t=-i\,\partial{\xi_{\mathrm{scl}}}^{*}/\partial r'_t$:

$$
J_t = i\Big[-i\,\xi_{\mathrm{scl}}\frac{\partial{\xi_{\mathrm{scl}}}^{*}}{\partial r'_t}+i\,{\xi_{\mathrm{scl}}}^{*}\frac{\partial\xi_{\mathrm{scl}}}{\partial r'_t}\Big]
=\xi_{\mathrm{scl}}\frac{\partial{\xi_{\mathrm{scl}}}^{*}}{\partial r'_t}-{\xi_{\mathrm{scl}}}^{*}\frac{\partial\xi_{\mathrm{scl}}}{\partial r'_t}
= -2i\,\mathrm{Im}\!\left({\xi_{\mathrm{scl}}}^{*}\frac{\partial\xi_{\mathrm{scl}}}{\partial r'_t}\right),
$$

the two central $i$'s multiplying to $-1$, which is **purely imaginary**, while the spatial components

$$
J_{\imath} = +2\,\mathrm{Im}\!\left({\xi_{\mathrm{scl}}}^{*}\frac{\partial\xi_{\mathrm{scl}}}{\partial R_{\imath}}\right)
$$

are real, the $i$ of the current multiplying the $-2i$ of the Wronskian to $+2$. Hence $\tilde{J}_{\Phi}\in\mathbb{B}_{\Phi}$, with imaginary scalar part and real vector part, exactly as the four-current of relativistic mechanics. **That is the proof of the sector statement**, and it is a two-line one: an element is fixed by $\flat=-{}^{*}$ exactly when $\tilde Q^{*}=-\tilde Q$, that is when $\overline{Q_t}=-Q_t$ and $\overline{Q_{\imath}}=+Q_{\imath}$ — imaginary scalar part, real vector part — and the two displays above are exactly those two statements. Writing $J_t = ic\rho$ recovers the parent's convention $\tilde{J}_{\Phi} = ic\rho\,e_t + \vec j$, with

$$
\rho = \frac{i}{c}\left({\xi_{\mathrm{scl}}}^{*}\partial/\partial r'_t\,\xi_{\mathrm{scl}} - \xi_{\mathrm{scl}}\,\partial/\partial r'_t\,{\xi_{\mathrm{scl}}}^{*}\right),
$$

which is real and **positive** on a positive-frequency wave $\xi_{\mathrm{scl}}\propto\exp(-i\theta_{\mathrm{pwp}})$. The evaluation is two lines: with $\dot{\xi}_{\mathrm{scl}}:=\partial\xi_{\mathrm{scl}}/\partial r'_t$ and $\dot\theta_{\mathrm{pwp}}=\omega/c$,
$$
{\xi_{\mathrm{scl}}}^{*}\dot\xi_{\mathrm{scl}}=-i\frac{\omega}{c}\lvert\xi_{\mathrm{scl}}\rvert^{2},
\qquad
\xi_{\mathrm{scl}}\dot{\xi}_{\mathrm{scl}}^{*}=+i\frac{\omega}{c}\lvert\xi_{\mathrm{scl}}\rvert^{2},
\qquad\text{so}\qquad
\rho=\frac{1}{ic}\Big(+2i\frac{\omega}{c}\lvert\xi_{\mathrm{scl}}\rvert^{2}\Big)=\frac{2\omega}{c^{2}}\lvert\xi_{\mathrm{scl}}\rvert^{2}>0 .
$$
The $c^{2}$ and not a single $c$ is the whole content of the two conventions being used at once: one $c$ sits in the phase, $\omega r'_t/c$, and the other in the relation between the density and the temporal component, $J_t=ic\rho$. This is the sign convention of *The Klein–Gordon Equation in Biquaternionic Form*, and it is what fixes the sign of $\tilde{J}_{\Phi}$ above.

### Conservation and the Identity Behind It

Forming the scalar part of $(\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}$,

$$
\mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}\right) = \sum_{\imath}\partial/\partial R_{\imath}\,J_{\imath} = \langle\tilde\nabla_\Phi,\tilde J_{\Phi}\rangle_{\natural} ,
$$

the sum being plain, because the signs of $\varepsilon$ are spent inside $(\tilde\nabla_\Phi)^{\natural}$: on the diagonal $\mathrm{Sc}(e_{\imath}^{\natural}e_{\imath})=1$ for all four $\mu$. Using the definitions and the d'Alembertian,

$$
\boxed{\ \mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}\right) = i\,\mathrm{Sc}\!\left[(\Box_\Phi\tilde{Ξ}^{*})\tilde{Ξ} - \tilde{Ξ}^{*}(\Box_\Phi\tilde{Ξ})\right]\ }
$$

The cross terms of each $\mu$ enter with opposite signs and cancel, so only the second derivatives survive. This is the Noether identity in biquaternion form: the scalar divergence of the current is the Klein–Gordon operator applied to the field, contracted with the symmetry variation. On shell, $\Box_\Phi\tilde{Ξ} = (4\pi^{2}\nu_m^{2})\tilde{Ξ}$ and the same for the conjugate, both terms become the same real multiple of $\tilde{Ξ}^{*}\tilde{Ξ}$ and cancel, so

$$
\mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}\right) = 0 \quad\text{on shell},
$$

which is the continuity equation $c\,\partial/\partial r'_t\rho + \mathrm{div}\,\vec j = 0$. The reason the time component needs no separate sign is the same one met above: $\partial/\partial R_t=-i\,\partial/\partial r'_t$ meets $J_t=ic\rho$, and the two central imaginaries cancel, $(-i)(i)=1$, leaving the factor $c$ of the current and the plain $\partial/\partial r'_t$ of the continuity equation.

### On What Case This Was Checked

A single plane wave is a trap: for $\tilde{Ξ} = \tilde{Ξ}_0\exp(-i\theta_{\mathrm{pwp}})$ the current is *constant*, so its divergence vanishes whether or not the field is on shell, and the plane wave that suggests the formula cannot test it. The conservation was therefore checked on three other cases:

- **a superposition of on-shell plane waves.** With the wave numbers in units of $\nu_m$ and the frequencies in units of $\nu_mc$, and the momenta $(|2\pi\vec\nu_\Phi|,\omega) = (0,1)$, $(\tfrac34,\tfrac54)$, $(\tfrac{5}{12},\tfrac{13}{12})$ all satisfying $\omega^2 = c^{2}\,4\pi^{2}\nu_{\Phi}^{2} + c^2\,4\pi^{2}\nu_m^2$, and amplitudes $1, \tfrac12, \tfrac13$, the current has non-constant cross terms, and $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi})$ cancels identically;
- **a standing wave**, $\tilde{Ξ} = \sin(2\pi\nu_{\Phi,x}x)\cos(\omega r'_t/c) + i\sin(2\pi\nu_{\Phi,x}x)\sin(\omega r'_t/c)$ with $\omega^2 = c^2\,4\pi^{2}\nu_{\Phi,x}^{2} + c^2\,4\pi^{2}\nu_m^{2}$: this is on shell and is **not** a plane wave, and again $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi})$ vanishes identically;
- **an off-shell field.** A two-mode field with one mode off shell gives a divergence proportional to the field equation, explicitly nonzero. The identity above was also confirmed on a generic three-mode field, off shell: the difference $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}) - i\,\mathrm{Sc}[(\Box_\Phi\tilde{Ξ}^{*})\tilde{Ξ} - \tilde{Ξ}^{*}(\Box_\Phi\tilde{Ξ})]$ reduces to zero identically, and the divergence is $2\,\mathrm{Im}(\tilde{Ξ}^{*}\Box_\Phi\tilde{Ξ})$, which is what the identity gives.

The last case is the honest statement of the theorem: the current is conserved **whenever** the field equation holds; off shell it need not be, and its divergence *is* the field equation.

### Relation to the Current Already in the Corpus

*The Klein–Gordon Equation in Biquaternionic Form* posits the current with $\rho =\frac{i}{2\,m\,c^{2}}(\tilde{Ξ}^{*}\partial/\partial r'_t\tilde{Ξ} - \tilde{Ξ}\partial/\partial r'_t\tilde{Ξ}^{*})$ and $\vec j = -\frac{i\,c}{4\pi\nu_m}(\tilde{Ξ}^{*}\vec\nabla_\Phi\tilde{Ξ} - \tilde{Ξ}\vec\nabla_\Phi\tilde{Ξ}^{*})$. Comparing component by component, that current equals $+\frac{c}{4\pi\nu_m}\tilde{J}_{\Phi}$: the Noether derivation reproduces the current the parent states, and fixes the normalization only up to the constant $\frac{c}{4\pi\nu_m}$ that a current may always be multiplied by. What the derivation adds is **why** that combination is the conserved one, and that it is forced by the phase symmetry rather than chosen.

**Relation to the Maxwell source.** In the Maxwell article the source conservation is $Z\,\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}) = 0$ with $\tilde J_{\Phi} = ic\rho\,e_t + \vec J$. Expanding, $Z\,\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}) = \partial/\partial r'_t\,\rho/\epsilon + Z\,\mathrm{div}\,\vec J$, so the Maxwell integrability condition is the same continuity equation as the conservation of $\tilde{J}_{\Phi}$ above. The electric four-current of the material sector is the Noether current of the central phase; the redundancy localized in *The Minimal Coupling in Biquaternionic Form* is the localization of the symmetry that produces it.

### The Dirac Field: the Pair, the Two-Sided Form, and the Axial Current

The same phase is a symmetry of the massive Dirac field, and it acts on **both chiral parts alike**: the central phase multiplies $\tilde\Xi_{L}$ and $\tilde\Xi_{R}$ by the same factor, which is why it survives the mass term, while the **axial** rotation multiplies them by opposite factors and does not. Both statements are made precise below; the distinction is flagged here because a single phrase, "the phase symmetry of the Dirac field", would hide precisely the difference the axial current tests. For the Dirac field the dynamics is the **chiral pair**

$$
\begin{aligned}
\tilde\nabla_\Phi\tilde{Ξ}_{R} &= 2\pi\nu_m\,\tilde{Ξ}_{L},\\[4pt]
(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L} &= 2\pi\nu_m\,\tilde{Ξ}_{R},
\end{aligned}
$$

two equations, one per part, each first order and linear in the field, with $m$ central. They are the two lines of one dynamics, not two independent ones: eliminating one half gives the massive Klein–Gordon equation, and at $m=0$ the pair decouples into the two Weyl equations, $\tilde\nabla_\Phi\tilde{Ξ}_{R}=0$ and $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=0$, one for each part. A central phase passes through both lines, since it passes through the central mass, so the current derived above is the conserved current of the Dirac field at every $m$, and $\langle\tilde\nabla_\Phi,\tilde J_{\Phi}\rangle_{\natural}=0$ on shell for it.

**The two-sided form.** Read on the whole algebra rather than on the two parts, the same dynamics is one equation in which the derivative acts on the left and the unit $\vec e_z$ on the right,

$$
(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ} = -\,m\,i\,\bar{\tilde{Ξ}}\,\vec e_z ,
$$

where $\bar{\tilde{Ξ}}$ is the coefficient conjugate, taken on the four coefficients and leaving the units fixed. The mass is thus a right multiplication by $\vec e_z$ carried with the imaginary unit: the central mass of the pair becomes a product, with the unit displayed and the factor $i$ left in front, one real mass multiplying one unit and one $i$. This is the operator-theoretic content of the two-sidedness: the derivative acts on the left, the mass on the right, and the conjugation supplies the antilinear part, so the second field of the $\natural$-side equation is the conjugate of the first carried on the right. The one-sided pair is the definition; this is its form on the algebra, one line, with the unit $\vec e_z$ standing where the second part stood.

**Where these come from.** The vector current is the coefficient of $\partial_{\imath}\theta_{\mathrm{cen}}$ in the variation of the chiral pair under a **local** central phase — the same computation as §*The Symmetry and the Current*, run on a first-order system, where each of the two lines of the pair contributes one term and the two together leave the antisymmetrized insertion of the unit $e_{\imath}$ between the field and its adjoint. The companion *The Dirac Equation in Biquaternionic Form* derives it in this form; what is checked here is not the coefficient but the two properties the sections below use, that $j_t$ is the Hermitian norm and that the plain divergence $\sum_{\imath}\partial j_{\imath}/\partial R_{\imath}$ is the field equation contracted with the symmetry variation.

**The currents on the algebra.** With the algebra's conjugation as the adjoint, the central-phase current of the Dirac field has the components

$$
j_{\imath} = \mathrm{Sc}\bigl(\tilde{Ξ}^*\,e_{\imath}\,\tilde{Ξ}\,b_{\imath}\bigr),
\qquad b_t = e_t,\quad b_{\imath} = \vec e_z\ \ (k=x,y,z),
$$

the unit of the coordinate inserted between the field and its adjoint: $j_t = \mathrm{Sc}(\tilde{Ξ}^*\tilde{Ξ})$ is the Hermitian norm of the field, and $j_{\imath} = \mathrm{Sc}(\tilde{Ξ}^*\vec e_{\imath}\tilde{Ξ}\vec e_z)$ is the component of the current along $\vec e_{\imath}$. The axial rotation assigns opposite phases to the two parts, so the mass term, which pairs them, is not invariant under it. **The axial current is therefore not a Noether current of the massive theory** — its divergence below is nonzero, and that divergence is the statement of the breaking rather than a conservation law. It is transcribed from the companion *Chiral Fermions in the Biquaternion Framework*, where the axial rotation is derived, and it is used here for two things only: the order of the right multipliers, and the value of the divergence. It carries the unit $\vec e_z$ inside the product,

$$
j_{5\imath} = \mathrm{Sc}\bigl(\tilde{Ξ}^*\,i\,e_{\imath}\,\tilde{Ξ}\,\vec e_z\vec e_{\tau(\imath)}\vec e_x\bigr),
\qquad \tau(t)=x,\ \ \tau(k)=y\ \ (k=x,y,z),
$$

which reduces on the two cases to

$$
j_{5t} = -\,i\,\mathrm{Sc}\bigl(\tilde{Ξ}^*\tilde{Ξ}\vec e_z\bigr),
\qquad
j_{5k} = i\,\mathrm{Sc}\bigl(\tilde{Ξ}^*\vec e_{\imath}\tilde{Ξ}\bigr).
$$

**The right multiplier is ordered, and the order is the sign.** The product $\vec e_z\vec e_{\tau(\imath)}$ is written in that order and cannot be commuted past the other: for the spatial indices $\tau(x)=y$, and $\vec e_z\vec e_x=+\vec e_y$ while $\vec e_x\vec e_z=-\vec e_y$, so reversing the two units reverses the sign of $j_{5\imath}$ and with it the sign of the divergence. That is the algebraic content of the axial rotation multiplying the two parts oppositely, and it is why the unit $\vec e_z$ has to be carried on the right of the field rather than inserted on the left. The divergence is the **plain** sum of the four derivatives, since the $\natural$ in $\langle\tilde\nabla_\Phi,\tilde J_{\Phi,5}\rangle_{\natural}$ already carries the relative sign of the spatial derivatives; the mass is the obstruction:

$$
\langle\tilde\nabla_\Phi,\tilde J_{\Phi,5}\rangle_{\natural} = \sum_{\imath}\frac{\partial j_{5\imath}}{\partial R_{\imath}} = 2im\,\mathrm{Sc}\bigl(\tilde{Ξ}^*\tilde{Ξ}\vec e_y\bigr),
$$

using $\vec e_z\vec e_x=\vec e_y$, and this vanishes only at $m=0$. **The $m$ in this display is the mass wave number of §*Conventions*, $m=2\pi\nu_m$, i.e. the mass in the units of the gradient**; with the units restored the right-hand side reads $2i(2\pi\nu_m)\,\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi\vec e_y)$, which has the dimensions of a divergence of a density, $\ell^{-1}$ times the density, as it must. The same statement without the units on show: the axial rotation multiplies each part by a phase opposite to the other's, and on the algebra it is a right multiplication,

$$
\tilde{Ξ}\ \longmapsto\ \tilde{Ξ}\,(\cos\theta_{\mathrm{axr}}+\sin\theta_{\mathrm{axr}}\,\vec e_z),
$$

which multiplies $\tilde{Ξ}_{L}$ by $\exp(-i\theta_{\mathrm{axr}})$ and $\tilde{Ξ}_{R}$ by $\exp(+i\theta_{\mathrm{axr}})$, because right multiplication by $\vec e_z$ acts on the two parts as $-i$ and $+i$. That is why the axial current carries the unit $\vec e_z$ and not a separate object.

**What the mass breaks, and what it does not.** What the mass term breaks is the **axial** rotation, not the phase. The mass term is $-mi\bar{\tilde{Ξ}}\vec e_z$: one right factor $\vec e_z$ between the field and its conjugate. It is invariant under the central phase, which multiplies the field by a central scalar and leaves every unit alone, so both sides of the equation take the same phase and it is carried to itself; and it is not invariant under the axial rotation, which replaces that right factor by $\cos\theta_{\mathrm{axr}}\,\vec e_z-\sin\theta_{\mathrm{axr}}\,e_t$, since $\vec e_z\vec e_z=-e_t$. In the biquaternion reading the mass couples the two parts off the diagonal, so it breaks exactly the rotation that moves them against each other, and not the central $\mathrm{U}(1)$ that the algebra canonically carries. The obstruction belongs to the antilinear single-field equation; the minimal coupling article's corresponding section states the same reason.

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

The mass-shell relation $\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural} = -m^{2}\,c^{2}$ follows, since $\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural}=-(E/c)^2+\vec p^{\,2}$ and $E^2=\vec p^{\,2}c^2+m^2c^4$. Translation invariance is thus the symmetry whose Noether charge is the four-momentum; the four-momentum is conserved for a free particle, $d\tilde{P}_{\Phi}/d\tau = 0$, because $\mathrm{Lag}$ has no explicit $\tilde{Q}$-dependence. As an independent check, a particle with the momentum in units of $mc$ and the energy in units of $mc^2$, $\vec p = (0.6,0,0)$ and $E = \sqrt{1.36}$ was boosted by the rotor $\tilde U = \cosh(\theta_{\mathrm{rpd}}/2) + i\sinh(\theta_{\mathrm{rpd}}/2)\vec e_x$ with $\theta_{\mathrm{rpd}} = 1.2$, the conjugation being $\tilde U\tilde P_{\Phi}\tilde U^{*}$: the result is $E' = 1.206$ and $p'_x = -0.674$, which are the component formulas $E'=\cosh\theta_{\mathrm{rpd}}\,E-\sinh\theta_{\mathrm{rpd}}\,p_x$ and $p'_x=\cosh\theta_{\mathrm{rpd}}\,p_x-\sinh\theta_{\mathrm{rpd}}\,E$, and the biquaternion norm is $-1$ in both frames, confirming that the Noether charge transforms as a four-vector.

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

A free field is a plane wave, and a translation acts on it by a central phase. With the series' phase convention $\tilde{Ξ} = \tilde{Ξ}_0\exp(-i\theta_{\mathrm{pwp}})$, whose phase is $\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_\Phi^{\natural}) = 2\pi\vec\nu_\Phi\cdot\vec r-\omega r'_t/c$, and with $\tilde P_{\Phi}\in\mathbb{B}_{\Phi}$ and $\tilde R_\Phi\mapsto\tilde R_\Phi+\tilde{R}_{\Phi,0}$,

$$
\tilde{Ξ}\big|_{\tilde R_\Phi+\tilde{R}_{\Phi,0}} = \exp\!\bigl(i\,\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_{\Phi,0}^{\natural})\bigr)\,\tilde{Ξ}\big|_{\tilde R_\Phi},
\qquad
\tilde{Ξ}_0\ \text{constant}.
$$

The multiplier is **central and of unit modulus**, because $\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_{\Phi,0}^{\natural}) = \langle\tilde P_{\Phi},\tilde{R}_{\Phi,0}\rangle_{\natural}$ is real: writing $\tilde P_{\Phi} = i\frac{\omega}{c}e_t + 2\pi\vec\nu_\Phi$ and $\tilde{R}_{\Phi,0} = i R_{0t} e_t + \vec R_0$, with $R_{0t} = r'_{t,0}$,

$$
\mathrm{Sc}\!\left(\tilde P_{\Phi}\tilde{R}_{\Phi,0}^{\natural}\right) = -\frac{\omega R_{0t}}{c} + 2\pi\vec\nu_\Phi\cdot\vec R_0 = 2\pi\vec\nu_\Phi\cdot\vec R_0-\omega r'_{t,0}/c .
$$

What makes it a phase is the $i$: the same scalar in a real exponential is a dilation. For $\tilde P_{\Phi} = 2i\,e_t + 0.7\vec e_x - 0.3\vec e_y + 0.5\vec e_z$ and $\tilde{R}_{\Phi,0} = 0.4i\,e_t + 0.25\vec e_x - 0.35\vec e_y + 0.15\vec e_z$ (in the units of the check), $\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_{\Phi,0}^{\natural}) = -0.445$ and the multiplier is $\exp(-0.445i)$, of modulus $1$, whereas $\exp(\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_{\Phi,0}^{\natural})) = e^{-0.445}$ has modulus $0.641$. The $\natural$ inside the pairing must be the one the wave itself carries; the un-conjugated $\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_{\Phi,0}) = -\frac{\omega R_{0t}}{c}-2\pi\vec\nu_\Phi\cdot\vec R_0$ belongs to the opposite sign convention for $\vec\nu_\Phi$ in the phase, and mixing the two flips the sign of $\vec\nu_\Phi\cdot\vec R_0$ alone. This central phase is the finite, field-space form of the translation subgroup; its infinitesimal generator is the derivation $\partial/\partial R_{\imath}$, and it is not a rotor, as *The Poincaré Group and the Biquaternion Frame* establishes.

## The Energy–Momentum of the Field

### The Canonical Tensor

The same translation symmetry applied to the field action gives the **canonical energy–momentum**, the Noether current of spacetime translations. For the complex scalar field it is

$$
\boxed{\;T_{\imath\jmath} = \frac{\partial{\xi_{\mathrm{scl}}}^*}{\partial x_{\imath}}\frac{\partial\xi_{\mathrm{scl}}}{\partial x_{\jmath}} + \frac{\partial\xi_{\mathrm{scl}}}{\partial x_{\imath}}\frac{\partial{\xi_{\mathrm{scl}}}^*}{\partial x_{\jmath}} + \varepsilon_{\imath}\delta_{\imath\jmath}\,\mathcal{L}_{\mathrm{scl},\xi}\;}
$$

with the scalar Lagrangian of the same coordinates,

$$
\mathcal{L}_{\mathrm{scl},\xi} = \sum_{\imath}\frac{\partial{\xi_{\mathrm{scl}}}^*}{\partial R_{\imath}}\frac{\partial\xi_{\mathrm{scl}}}{\partial R_{\imath}} + 4\pi^{2}\nu_m^{2}\lvert\xi_{\mathrm{scl}}\rvert^2
= -\left|\frac{\partial\xi_{\mathrm{scl}}}{\partial r'_t}\right|^2 + |\vec\nabla_\Phi\xi_{\mathrm{scl}}|^2 + 4\pi^{2}\nu_m^{2}\lvert\xi_{\mathrm{scl}}\rvert^2 .
$$

Here $x_{\imath}=(r'_{t},r_x,r_y,r_z)$ are the real coordinates, the chart of $Q_{\imath}$ with the $i$ of the time coefficient removed, $Q_t=i q'_t$: $Q_0=i q'_t$ carries the $i$, while $x_0=r'_{t}$ does not. Both indices of $T$ are low, the first the row. The coefficient of $\mathcal{L}_{\mathrm{scl},\xi}$ is the plain form of the two units, $\mathrm{Sc}(e_{\imath} e_{\jmath})=\varepsilon_{\imath}\delta_{\imath\jmath}$: plus on the time entry and minus on the three space entries. The derivative index of the conservation law carries one minus on the time direction and none on the three space directions, and that minus is the square of the $i$ in $Q_t=i q'_t$, spent once and written out. **The derivation, from translation invariance.** A constant shift moves the field without moving the Lagrangian's form, $\delta\xi_{\mathrm{scl}}=a^{\jmath}\partial_{\jmath}\xi_{\mathrm{scl}}$ with $a^{\jmath}$ constant, and the current carrying one index per generator is the coefficient of $a^{\jmath}$. The identity behind the conservation law is the chain rule for $\partial_{\jmath}\mathcal{L}_{\mathrm{scl},\xi}$, which holds with no remainder because $\mathcal{L}_{\mathrm{scl},\xi}$ has **no explicit dependence on $x$** — that absence *is* the translation invariance:

$$
\frac{\partial\mathcal{L}_{\mathrm{scl},\xi}}{\partial x_{\jmath}}=\frac{\partial\mathcal{L}_{\mathrm{scl},\xi}}{\partial\xi_{\mathrm{scl}}}\frac{\partial\xi_{\mathrm{scl}}}{\partial x_{\jmath}}+\frac{\partial\mathcal{L}_{\mathrm{scl},\xi}}{\partial\xi_{\mathrm{scl}}^{*}}\frac{\partial\xi_{\mathrm{scl}}^{*}}{\partial x_{\jmath}}+\sum_{\imath}\Big[\frac{\partial\mathcal{L}_{\mathrm{scl},\xi}}{\partial(\partial\xi_{\mathrm{scl}}/\partial x_{\imath})}\frac{\partial^{2}\xi_{\mathrm{scl}}}{\partial x_{\imath}\partial x_{\jmath}}+\text{c.c.}\Big].
$$

The second-derivative terms are precisely the ones that differentiating the first two terms of $T_{\imath\jmath}$ produces, so they cancel against them, and the remainder of the divergence is the field equation contracted with the variation:

$$
-\sum_{\imath}\varepsilon_{\imath}\frac{\partial}{\partial x_{\imath}}A_{\imath\jmath}-\frac{\partial\mathcal{L}_{\mathrm{scl},\xi}}{\partial x_{\jmath}}
=2\,\mathrm{Re}\Big[\frac{\partial\xi_{\mathrm{scl}}^{*}}{\partial x_{\jmath}}\Big(\Box_\Phi\xi_{\mathrm{scl}}-m_0^{2}\xi_{\mathrm{scl}}\Big)\Big],
\qquad
A_{\imath\jmath}:=\frac{\partial\xi_{\mathrm{scl}}^{*}}{\partial x_{\imath}}\frac{\partial\xi_{\mathrm{scl}}}{\partial x_{\jmath}}+\frac{\partial\xi_{\mathrm{scl}}}{\partial x_{\imath}}\frac{\partial\xi_{\mathrm{scl}}^{*}}{\partial x_{\jmath}} .
$$

Since the $\mathcal{L}$ term of $T$ contributes $-\partial_{\jmath}\mathcal{L}_{\mathrm{scl},\xi}$ under the same divergence, taken with the $\varepsilon_{\imath}$, the tensor above is conserved **exactly when the field equation holds**, and vanishes otherwise in proportion to it. Two things are therefore not choices: the sign in front of $\mathcal{L}_{\mathrm{scl},\xi}$ is the one that makes the second-derivative terms cancel, and the $\varepsilon_{\imath}$ inside the divergence is the same one that appears in the tensor. Translation invariance gives

$$
-\frac{\partial T_{0\jmath}}{\partial x_0}+\sum_{\imath\in\{x,y,z\}}\frac{\partial T_{k\jmath}}{\partial r_{\imath}} = 0
$$

on shell. Its time–time component is the energy density,

$$
T_{00} = \left|\frac{\partial\xi_{\mathrm{scl}}}{\partial r'_t}\right|^2 + |\vec\nabla_\Phi\xi_{\mathrm{scl}}|^2 + 4\pi^{2}\nu_m^{2}\lvert\xi_{\mathrm{scl}}\rvert^2 > 0,
$$

positive for every configuration because each term is a square. The check, with its parameters, is reproducible as it stands:

| item | value |
|---|---|
| field | $\xi_{\mathrm{scl}}=\exp(-i\theta_1)+\tfrac12\exp(-i\theta_2)$, both modes on shell |
| mode 1 | $\vec\nu_\Phi=(0.6,0,0)$, $\omega=\sqrt{c^{2}4\pi^{2}\nu^{2}+m_0^{2}c^{2}}$ |
| mode 2 | $\vec\nu_\Phi=0.45\,(0.6,0.8,0)$, $\omega$ from the same shell |
| constants | $m_0=1$, $c=1$ |
| scheme | centred differences, step $10^{-5}$, evaluated at $(r'_t,r_x,r_y,r_z)=(0.31,0.217,0.13,-0.09)$ |
| result | $\bigl|-\partial_0T_{0\jmath}+\sum_k\partial_kT_{k\jmath}\bigr|<2\times10^{-6}$ for all four $\jmath$ |
| result | $T_{\imath\jmath}=T_{\jmath\imath}$ to machine precision; $T_{00}$ equals the positive expression above to $10^{-14}$ |

A single plane wave is not a test here, for the same reason it was not one for the current: on it the tensor is constant, and a constant tensor has zero divergence whether or not the field is on shell.

### Why the Framework Does Not Write It as One Biquaternion

**The count, done on the right object.** The canonical tensor is **not symmetric**: $T_{\imath\jmath}$ of the display above is symmetric only because the scalar field's $A_{\imath\jmath}$ is, and for a field with a spin term the canonical tensor of translations has **sixteen** independent entries before any improvement. It is the *Belinfante-improved* tensor that is symmetric, and it is that one — not the canonical one — which has ten components, and whose tracelessness in the massless case carries scale invariance. Three counts are therefore three different statements:

| object | independent components | carried by |
|---|---|---|
| canonical translation current $T_{\imath\jmath}$ | $16$ | bigenerator bilinear, one basis element per index |
| Belinfante-improved, symmetric | $10$ | the same bilinear, after the improvement |
| one biquaternion | $8$ real ($4$ complex) | not enough for either |
| $\tilde\Sigma_{\Psi}=\tfrac{\epsilon}{2}\tilde{F}\tilde{F}^{*}$ | $4$ | the energy–flux row only |

So the correct statement is narrower than "a rank-two tensor cannot be a biquaternion": **no single biquaternion can carry the canonical translation current**, be it sixteen-component or ten, and the framework does not claim one. It writes the current as a **bigenerator quaternionic bilinear**, one basis element for each index, and only its time row — an object in $\mathbb{B}_{\Psi}$ with four real components — is ever displayed as a biquaternion. *Exercise: The Electromagnetic Energy–Momentum Tensor* constructs the bilinear for the Maxwell field, $\Pi_{\imath\jmath} = \tfrac12\mathrm{Sc}(\tilde{F}\mathcal{E}_{\imath}\tilde{F}^{*}\mathcal{E}_{\jmath})$ with the first index the row, and shows that $\tilde\Sigma_{\Psi}$ is its time row; that exercise also finds the improved tensor traceless, which is the Belinfante statement and not a property of the canonical one.

### The Maxwell Case in the Corpus Form

For the electromagnetic field the four-component object is $\tilde\Sigma_{\Psi} = \tfrac{\epsilon}{2}\tilde{F}\tilde{F}^{*} = W\,e_t + \frac{i}{c}\vec S\in\mathbb{B}_{\Psi}$, with $W$ the energy density and $\vec S = \vec E\times\vec H$ the Poynting vector. **The three conventions in that display are fixed once:** $\tilde F=i\vec E-c\vec B$ is the field-strength bivector of the Maxwell article, of scalar part zero and vector part $i\vec E-c\vec B$; $^{*}$ is the Hermitian conjugation of §*Conventions*, so $\tilde F^{*}=i\vec E+c\vec B$ for real fields; and $\epsilon$ is the permittivity of the medium, with $\mu$ its permeability and $c=1/\sqrt{\epsilon\mu}$. The factor $\epsilon/2$ is then not free: with these, the scalar part is $\tfrac{\epsilon}{2}(E^{2}+c^{2}B^{2})=\tfrac12(\epsilon E^{2}+B^{2}/\mu)$, which is the energy density of the medium, and the coefficient of the Poynting part is the normalization of *Exercise: The Electromagnetic Energy–Momentum Tensor*, quoted here and not used in the argument below. Its scalar divergence is the energy law,

$$
\mathrm{Sc}\!\left(\tilde\nabla_\Phi\tilde\Sigma_{\Psi}\right) = -i\left(\frac{\partial W}{\partial r'_t}+\frac{1}{c}\,\mathrm{div}\,\vec S\right) = \frac{i}{c}\,\vec J\cdot\vec E ,
$$

the last equality being the Poynting theorem. The factor $i$ is uniform across the two terms, as a temporal component must be in the $i r'_t$ convention, and dividing it out recovers $c\,\partial W/\partial r'_t + \mathrm{div}\,\vec S + \vec J\cdot\vec E = 0$. The real form $\tilde\Sigma_{\Psi} = W + \frac{1}{c}\vec S$ fails exactly this test: its scalar divergence carries the $i$ on the time term only, and on a free plane wave it equals $\frac{1-i}{c}\partial W/\partial r'_t$, which is not zero. What *Exercise: The Electromagnetic Energy–Momentum Tensor* isolates is that factor $i$ on the Poynting part, and the equation $\tilde\nabla_\Phi\tilde\Sigma_{\Psi} = -\tilde{\mathcal F}$, taken as a biquaternion identity with a power–force density on the right, is not what the corpus establishes for either form: what it verifies is the scalar statement above, not the vector one. Read as a Noether statement, $\mathrm{Sc}(\tilde\nabla_\Phi\tilde\Sigma_{\Psi}) = \frac{i}{c}\vec J\cdot\vec E$ says the translation current is conserved up to the work done on the charges — the source is present, so the field alone is not closed.

### A Caution on the $i r'_t$ Convention

The energy density is not $\mathcal{L}_{\mathrm{scl},\xi}$ and is not obtained from it by a flat sum: $T_{00}=\frac{1}{c^2}|\dot\xi_{\mathrm{scl}}|^2+|\vec\nabla_\Phi\xi_{\mathrm{scl}}|^2+4\pi^{2}\nu_m^{2}\lvert\xi_{\mathrm{scl}}\rvert^2$ while $\mathcal{L}_{\mathrm{scl},\xi}=-\frac{1}{c^2}|\dot\xi_{\mathrm{scl}}|^2+|\vec\nabla_\Phi\xi_{\mathrm{scl}}|^2+4\pi^{2}\nu_m^{2}\lvert\xi_{\mathrm{scl}}\rvert^2$, with the mass wave number $\nu_m=\frac{mc}{2\pi}$ and its reciprocal $\frac{1}{\nu_m}$. The gradient and $\Box_\Phi$ live in the $Q_{\imath}$ frame, where $Q_0=i q'_t$; the tensor lives in $x_{\imath}=(r'_{t},r_x,r_y,r_z)$, where the time component is real and the minus is written on the time derivative. Mixing the two charts produces the wrong sign on the time derivative, and the mismatch is the same $1/i^2=-1$ that makes the time term of the uniform $Q$-frame sum of $\mathcal{L}$ negative once written in the real coordinates. This is the same caution the energy–momentum exercise records for the trace.

## Lorentz Invariance and the Angular-Momentum Bivector

### The Particle Bivector

Lorentz invariance is a spacetime symmetry like translation, and it has a Noether current too. For a free particle the conserved quantity is the antisymmetric pair

$$
L_{\imath\jmath} = x_{\imath} p_{\jmath} - x_{\jmath} p_{\imath},
\qquad
\frac{dL_{\imath\jmath}}{d\tau} = \frac{dx_{\imath}}{d\tau}p_{\jmath} - \frac{dx_{\jmath}}{d\tau}p_{\imath} = \frac{p_{\imath} p_{\jmath}-p_{\jmath} p_{\imath}}{m} = 0,
$$

using $dx_{\imath}/d\tau = p_{\imath}/m$ and $dp_{\imath}/d\tau = 0$ for a free particle; the conservation of the six independent components is the conservation of angular momentum and of the boost charges. In the biquaternion algebra the antisymmetric pair is a **bivector**, the same representation the field strength occupies: writing

$$
\boxed{\;\tilde L = \tfrac12\sum_{\imath,\jmath}L_{\imath\jmath}\,e^{\natural}_{\imath} e_{\jmath}\;}
$$

the angular momentum of a free particle is a single biquaternion. The tilde rather than an arrow is deliberate: the vector part of $\tilde L$ is $L_{0k}-\tfrac12\epsilon_{\imath ij}L_{ij}$ along $\vec e_{\imath}$, which pairs the boost charges with $\vec r\times\vec p$ and is not the three-vector of orbital angular momentum. This is the same construction by which $\tilde{F} = \mathrm{Vect}((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}) = \tfrac12\sum_{\imath\jmath}F_{\imath\jmath}e^{\natural}_{\imath} e_{\jmath}$ packages the antisymmetric field strength, and the Lorentz generators themselves are bivectors.

### The Rank-Three Field Current

For a field, the Noether current of Lorentz invariance is a rank-three object,

$$
L_{\imath\jmath\rho} = x_{\jmath} T_{\imath\rho} - x_\rho T_{\imath\jmath} + S_{\imath\jmath\rho},
$$

whose conservation

$$
-\frac{\partial L_{0\jmath\rho}}{\partial x_0}+\sum_{\imath\in\{x,y,z\}}\frac{\partial L_{k\jmath\rho}}{\partial r_{\imath}} = 0
$$

expresses the symmetry of the energy–momentum tensor together with the conservation of spin. Being rank three, it is not a biquaternion and not even a single bilinear; the orbital and spin pieces separate, with the spin term vanishing for the classical scalar field. The particle bivector $\tilde L$ above is the finite-dimensional case where the rank-two object *is* the whole story.

## What Is Inherited, What Is Added, What Is Interpretation

**Inherited and unchanged.** The action, the four-momentum, the four-current and its conservation $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}) = 0$, the algebra, the gradient, the sectors, and the reduction formula, which for a state $\tilde{Ϛ}_{\Psi}$ and a Hermitian observable $\tilde H_\Psi\in\mathbb{B}_{\Psi}$ is the single statement $2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})=2\langle\tilde{Ϛ}_{\Psi},\tilde H_\Psi\rangle_{*}\in\mathbb{R}$, the sesquilinear pairing of §*Conventions* read on the diagonal, are those of the read list. No symbol is renamed, the sign of the current is the one for which $\rho>0$ on a positive-frequency wave, and what this article adds to the list is derivation and identification, not new definitions.

**Added by this article.** The derivation of the central-phase current $\tilde{J}_{\Phi} = i[(\tilde\nabla_\Phi\tilde{Ξ}^{*})\tilde{Ξ} - \tilde{Ξ}^{*}\tilde\nabla_\Phi\tilde{Ξ}]$ from the phase symmetry of the field action, and its conservation identity; its form $j_{\imath}=\mathrm{Sc}(\tilde{Ξ}^*e_{\imath}\tilde{Ξ}\,b_{\imath})$ on the Dirac field, with the axial current and its non-conservation; the identification of the free-particle four-momentum as the Noether charge of translation invariance, with the corrected multi-body statement; the explicit translation multiplier $\exp(-i\theta_{\mathrm{pwp}})$; the energy–momentum current and its packaging; and the angular-momentum bivector. These are transcriptions of the standard theorem into the algebra, with the subspace assignments the algebra supplies, not new physics.

**Only transcribed.** Noether's theorem itself is standard; the algebra does not produce a symmetry that the action did not already have, nor a conservation law beyond those the symmetries give. The framework supplies the home of each conserved object — the current in $\mathbb{B}_{\Phi}$, the energy–momentum in the bilinear and its time row in $\mathbb{B}_{\Psi}$ for Maxwell, the angular momentum in the bivector — and it makes the divergence identities compact. It does not supply the symmetries, the coupling constants, or the masses.

**Interpretation.** Reading the conserved currents as the physical four-current and energy–momentum is the standard interpretation, not an extra postulate; the biquaternion packaging is a representation-theoretic statement about which subspace carries which object, and it is exact. What remains interpretation is the physical hypothesis attached to the two sectors, which is the program's, not this article's.

## Open Questions

1. **The biquaternion form of the full translation current.** The energy–momentum tensor is rank two and cannot be one biquaternion. Is there a natural biquaternion-bilinear expression for the canonical $T_{\imath\jmath}$ of a general biquaternion field, beyond the Maxwell case constructed in the energy–momentum exercise?

2. **Spin and the angular momentum of fields.** The rank-three Lorentz current carries a spin term. Can the spin density of a biquaternion field be written as a single algebra-valued object, and how does it relate to the bivector representation of angular momentum?

3. **Scale and conformal symmetry.** The massless Klein–Gordon and Maxwell actions have more symmetries than the Poincaré group. Do they have biquaternion Noether currents, and does the tracelessness of the electromagnetic energy–momentum tensor — established in the energy–momentum exercise — express one of them?

4. **The axial current and the two parts.** With the linear mass term the vector phase current is conserved for the massive field, so the open question is the axial one. The divergence identity $\sum_{\imath}\partial j_{5\imath}/\partial R_{\imath} = 2im\,\mathrm{Sc}(\tilde{Ξ}^*\tilde{Ξ}\vec e_y)$ holds for the chiral pair, and its biquaternion reading is that the mass couples the two parts off the diagonal. Is there a Noether derivation that starts from the axial rotation $\tilde{Ξ}\mapsto\tilde{Ξ}(\cos\theta_{\mathrm{axr}}+\sin\theta_{\mathrm{axr}}\vec e_z)$ rather than from the pair — and does the central-element structure supply anything analogous to the would-be Goldstone statement?

5. **The current of the complexified theory.** In the complexified biquaternion theory of the Maxwell article, the source and potential are fully complex. Does the central-phase current acquire components outside $\mathbb{B}_{\Phi}$, and are they conserved?

6. **Empirical content.** As everywhere in the framework, the currents derived here are the standard ones in new notation. Whether the biquaternion packaging imposes any constraint that the four-vector formulation does not is not established here.

## Appendix: The Legacy Pauli Gamma Formulation

The Pauli and gamma arrays are a legacy display of the same algebra, refused as a language for the reasons of *The AXF Matrices: Axis-Free, Integer Entries*, §*Why the Pauli and the Gamma Displays Are Refused*. They are kept here for one purpose only: a reader who wants to compare the currents above with the Dirac literature has to be able to make the translation, and the translation is four lines long.

**The frame.** The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, and the two-sided operators act on the module by $L_a\tilde\Xi=a\tilde\Xi$ and $R_b\tilde\Xi=\tilde\Xi b$, with $L_aR_bL_cR_d=L_{ac}R_{db}$. The frame is

$$
\gamma_0=iL_{e_t}R_{\vec e_x},\qquad
\gamma_1=iL_{\vec e_x}R_{\vec e_y},\qquad
\gamma_2=iL_{\vec e_y}R_{\vec e_y},\qquad
\gamma_3=iL_{\vec e_z}R_{\vec e_y},\qquad
\gamma_5=-iL_{e_t}R_{\vec e_z},
$$

with the same arrays under the axis-free labels of that article, which differ from these by a change of basis of the module and not by a change of algebra. The display is written once here rather than twice, because nothing below depends on which of the two is used.

**The four identities that carry the dictionary.** Because $L_{e_t}$ is the identity,

$$
\gamma_5=-iR_{\vec e_z},\qquad
i\gamma_{\imath}=-L_{e_{\imath}}R_{\vec e_{\tau(\imath)}},\qquad
\gamma_{\imath}\gamma_5=\bigl(iL_{e_{\imath}}R_{\vec e_{\tau(\imath)}}\bigr)\bigl(-iR_{\vec e_z}\bigr)=L_{e_{\imath}}R_{\vec e_z\vec e_{\tau(\imath)}} .
$$

The first says that the two-valued chirality of the Dirac field is right multiplication by $\vec e_z$: the unit that appears in the two-sided equation and in the axial current is the gamma-five of the literature, with a factor $-i$ that the display absorbs. The second says that $i$ times a gamma is a plain generator basis operator; that is why a product of four gammas carries $i^{4}=+1$ and no residual unit. The third is the one the axial current needs: multiplying the two identities, the $i$ of the generator and the $-i$ of $\gamma_5$ cancel, and what survives is the **ordered** product $\vec e_z\vec e_{\tau(\imath)}$ on the right — the same order that §*The Dirac field* shows cannot be reversed without flipping the sign.

**What that gives for the currents.** Inserting the third identity in $\mathrm{Sc}(\tilde\Xi^{*}e_{\imath}\tilde\Xi\,b_{\imath})$ returns the vector current as $\tilde\Xi^{\dagger}\gamma_{\imath}\tilde\Xi$ up to the right factor $b_{\imath}$, and the axial current as $\tilde\Xi^{\dagger}iR_{\vec e_x}\gamma_{\imath}\gamma_5\tilde\Xi$, the left insertion $iR_{\vec e_x}$ being what the dagger convention of this series carries and the literature does not. And the mass term of the two-sided equation, $-mi\bar{\tilde\Xi}\vec e_z$, is $m\bar{\tilde\Xi}\gamma_5$ in the frame, because $-iR_{\vec e_z}$ is $\gamma_5$: the mass is a gamma-five insertion and nothing else, which is the statement that it is chirality-off-diagonal.

**The Clifford relations.** With $\varepsilon=(1,-1,-1,-1)$,

$$
\{\gamma_{\imath},\gamma_{\jmath}\}=2\varepsilon_{\imath}\delta_{\imath\jmath}I_4,\qquad
(\gamma_{\imath})^{2}=-I_4,\qquad
\gamma_5^{2}=I_4,\qquad
\{\gamma_{\imath},\gamma_5\}=0 ,
$$

the first being the quaternion multiplication table read in the frame: a generator that pairs $e_t$ with a spatial unit squares to the square of that unit, the central $i$ of each generator flips the sign, so the timelike generator squares to $+I_4$ and the three spatial ones to $-I_4$; and the last being what makes the chirality insertion axial. The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ while the plain basis operators span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$, the two Clifford algebras that differ by that relative $i$.

Nothing in the derivation of the currents above uses any of this. The appendix exists so that a reader who knows the gamma formulation can identify the objects, and so that the axial current's right multiplier can be recognized as $\gamma_\imath\gamma_5$ rather than accepted on trust.

## Summary

Noether's theorem in biquaternionic form joins the two ends that *Relativistic Mechanics in Biquaternionic Form* states separately, the free-particle action and the conserved four-current, by deriving the second from the first. The theorem has two forms. For an **internal** symmetry, that of the central phase $\tilde{Ξ}\mapsto \exp(i\theta_{\mathrm{cen}})\tilde{Ξ}$ of the complex biquaternion scalar field, the derived current is

$$
\tilde{J}_{\Phi} = i\left[(\tilde\nabla_\Phi\tilde{Ξ}^{*})\tilde{Ξ} - \tilde{Ξ}^{*}(\tilde\nabla_\Phi\tilde{Ξ})\right] = \sum_{\jmath} J_{\jmath} e_{\jmath},
\qquad J_{\jmath} = i\left(\xi_{\mathrm{scl}}\,\partial/\partial R_{\jmath}\,{\xi_{\mathrm{scl}}}^{*} - {\xi_{\mathrm{scl}}}^{*}\partial/\partial R_{\jmath}\,\xi_{\mathrm{scl}}\right),
$$

which lies in $\mathbb{B}_{\Phi}$ and satisfies the Noether identity

$$
\mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}\right) = i\,\mathrm{Sc}\!\left[(\Box_\Phi\tilde{Ξ}^{*})\tilde{Ξ} - \tilde{Ξ}^{*}(\Box_\Phi\tilde{Ξ})\right],
$$

zero whenever the field is on shell. This is the framework form of $\langle\tilde\nabla_\Phi,\tilde J_{\Phi}\rangle_{\natural} = 0$; it reproduces the current the Klein–Gordon article posits, up to the conventional constant $c/(4\pi\nu_m)$, with $\rho=2\omega\lvert\xi_{\mathrm{scl}}\rvert^{2}/c^{2}>0$ on a positive-frequency wave; and its expansion at the Maxwell source is the charge-conservation condition $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}Z\,\tilde{J}_{\Phi}) = 0$.

The same phase acts on the Dirac field — on both chiral parts alike, which is why it survives the mass — whose dynamics is the chiral pair $\tilde\nabla_\Phi\tilde{Ξ}_{R}=2\pi\nu_m\tilde{Ξ}_{L}$, $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=2\pi\nu_m\tilde{Ξ}_{R}$, equivalently the one equation on the algebra $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}=-mi\bar{\tilde{Ξ}}\vec e_z$. The vector current has the components $j_{\imath}=\mathrm{Sc}(\tilde{Ξ}^*e_{\imath}\tilde{Ξ}\,b_{\imath})$, with $b_t=e_t$ and $b_{\imath}=\vec e_z$, conserved at every $m$; the axial current carries the unit $\vec e_z$ inside the product and obeys $\sum_{\imath}\partial j_{5\imath}/\partial R_{\imath} = 2im\,\mathrm{Sc}(\tilde{Ξ}^*\tilde{Ξ}\vec e_y)$, vanishing only at $m=0$. The mass therefore breaks the axial rotation and not the phase.

For a **spacetime** symmetry, translation invariance gives the four-momentum

$$
\tilde{P}_{\Phi} = m\tilde{V}_{\Phi} = i\frac{E}{c}e_t + \vec p,
\qquad E = \gamma mc^2,\quad \vec p = \gamma m\vec v,
$$

as the Noether charge, conserved for a free particle. The conservation law for a system is the vanishing of the **coordinate**-time derivative of the total, $d\tilde{P}_{\Phi,\mathrm{tot}}/dt' = c\,d\tilde{P}_{\Phi,\mathrm{tot}}/dr'_t = 0$; the parent's proper-time four-force cannot be summed across bodies, and the correct form is $\sum_a\tilde{\mathcal F}_{\mathrm{frc},a}/(c\gamma_a) = 0$, or the integrated $\sum_{\mathrm{in}}\tilde{P}_{\Phi} = \sum_{\mathrm{out}}\tilde{P}_{\Phi}$. A translation acts on a plane wave by the central unit-modulus phase $\exp(-i\theta_{\mathrm{pwp}})$, with $\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_{\Phi,0}^{\natural}) = 2\pi\vec\nu_\Phi\cdot\vec R_0-\omega r'_{t,0}/c$.

The field translation current is the canonical energy–momentum, $-\partial T_{0\jmath}/\partial x_0+\sum_{\imath\in\{x,y,z\}}\partial T_{k\jmath}/\partial r_{\imath} = 0$ on shell in the real coordinates, with positive energy density $T_{00} = |\partial\xi_{\mathrm{scl}}/\partial r'_t|^2 + |\vec\nabla_\Phi\xi_{\mathrm{scl}}|^2 + 4\pi^{2}\nu_m^{2}\lvert\xi_{\mathrm{scl}}\rvert^2$. Rank two cannot be one biquaternion, so the framework packages it bilinearly; the Maxwell object $\tilde\Sigma_{\Psi} = \tfrac{\epsilon}{2}\tilde{F}\tilde{F}^{*}$ is its time row, and $\mathrm{Sc}(\tilde\nabla_\Phi\tilde\Sigma_{\Psi}) = \frac{i}{c}\vec J\cdot\vec E$ is the energy law it carries. Lorentz invariance gives the angular-momentum bivector $\tilde L = \tfrac12\sum L_{\imath\jmath}\,e^{\natural}_{\imath} e_{\jmath}$, with the rank-three field current reduced to the rank-two particle bivector only when the spin term vanishes. The theorem is standard; the algebra supplies the home of each conserved object and the compact form of its divergence, and it supplies no conservation law the symmetries did not already give.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_{\imath}^2 = -e_t$; $\mathrm{Sc}(e_{\imath} e_{\jmath})=\varepsilon_{\imath}\delta_{\imath\jmath}$, $\varepsilon=(1,-1,-1,-1)$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{B}_{\Phi}, \mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{B}_{H}, \mathbb{B}_{C} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ | Real-quaternion subspace; complex scalar line (the centre) |
| $\tilde\nabla_\Phi = e_t\partial/\partial R_t + \sum_{\imath}\,\vec e_{\imath}\,\partial/\partial R_{\imath}$ | Biquaternionic gradient |
| $(\tilde\nabla_\Phi)^{\natural} = e_t\partial/\partial R_t - \sum_{\imath}\,\vec e_{\imath}\,\partial/\partial R_{\imath}$ | Quaternion-conjugate gradient; $\mathrm{Sc}(e_{\imath}^{\natural}e_{\jmath})=\delta_{\imath\jmath}$ |
| $\Box_\Phi = \tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}= (\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi = \Delta_\Phi - \partial^2/\partial {r^{\prime}_t}^2$ | d'Alembertian, $Q_t=i q'_t$ |
| $S = -mc\int\sqrt{-d\tilde R_\Phi\,d\tilde{R}_\Phi^{\natural}}$ | Free-particle action |
| $\mathrm{Lag} = -mc^2\sqrt{1-\vec v^2/c^2}$ | Free-particle Lagrangian |
| $\tilde R_\Phi = i r'_{t}\,e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ | Four-position, in $\mathbb{B}_{\Phi}$ |
| $\tilde{R}_{\Phi,0}\in\mathbb{B}_{\Phi}$ | Constant translation (displacement) |
| $\tilde{V}_{\Phi} = \gamma(ic\,e_t + \vec v)$ | Four-velocity, $\tilde{V}_{\Phi}\tilde{V}_{\Phi}^{\natural} = -c^2$ |
| $\tilde{P}_{\Phi} = m\tilde{V}_{\Phi} = iE/c\,e_t + \vec p$ | Four-momentum, Noether charge of translation; real energy and momentum, so in $\mathbb{B}_{\Phi}$ |
| $\tilde{\mathcal F}_{\mathrm{frc},a} = d\tilde{P}_{\Phi,a}/d\tau_a$ | Four-force (proper-time derivative; not summable) |
| $\tilde{Ξ} = \xi_{\mathrm{scl}}\,e_t\in\mathbb{B}_{C}$ | Complex biquaternion scalar field |
| $\mathcal{L} = \sum_{\imath}(\partial{\xi_{\mathrm{scl}}}^{*}/\partial R_{\imath})(\partial\xi_{\mathrm{scl}}/\partial R_{\imath}) + 4\pi^{2}\nu_m^{2}\lvert\xi_{\mathrm{scl}}\rvert^2$ | Field Lagrangian density, $Q$ frame; its overall sign is the one for which $T_{00}>0$ |
| $\nu_m$, $m_0=2\pi\nu_m=mc$ | Mass wave number, and the mass parameter, the mass in the units of $\Box_\Phi$; $m_0^{2}$ is the coefficient of the mass term |
| $A_{\imath\jmath} = (\partial_\imath{\xi_{\mathrm{scl}}}^{*})(\partial_\jmath\xi_{\mathrm{scl}})+(\partial_\jmath{\xi_{\mathrm{scl}}}^{*})(\partial_\imath\xi_{\mathrm{scl}})$ | The derivative part of the canonical tensor, before the $\varepsilon_\imath\delta_{\imath\jmath}\mathcal{L}$ term |
| $\theta_{\mathrm{pwp}} = \omega r'_t/c-2\pi\vec\nu_\Phi\cdot\vec r$ | Plane-wave angle; $\tilde\Xi=\tilde\Xi_0\exp(-i\theta_{\mathrm{pwp}})$, $\omega^{2}=c^{2}4\pi^{2}\vec\nu_\Phi^{2}+m_0^{2}c^{2}$ |
| $\rho = \frac{i}{c}\left({\xi_{\mathrm{scl}}}^{*}\dot\xi_{\mathrm{scl}}-\xi_{\mathrm{scl}}\dot{\xi_{\mathrm{scl}}}^{*}\right)=\frac{2\omega}{c^{2}}\lvert\xi_{\mathrm{scl}}\rvert^{2}$ | Charge density, $J_t=ic\rho$; positive on a positive-frequency wave |
| $\tilde{J}_{\Phi} = i[(\tilde\nabla_\Phi\tilde{Ξ}^{*})\tilde{Ξ} - \tilde{Ξ}^{*}\tilde\nabla_\Phi\tilde{Ξ}]$ | Central-phase Noether current, in $\mathbb{B}_{\Phi}$ |
| $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}) = \langle\tilde\nabla_\Phi,\tilde J_{\Phi}\rangle_{\natural} = \sum_{\imath}\partial J_{\imath}/\partial R_{\imath}$ | Divergence of the current, plain sum |
| $\tilde J_{\Phi} = ic\rho\,e_t + \vec J$ | Maxwell source $Z\,\tilde J_{\Phi}$; $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}) = 0$ is charge conservation |
| $\tilde{Ξ}=\tilde{Ξ}_{L}+\tilde{Ξ}_{R}$ | The Dirac field, an element of $\mathbb{B}$; the value of $\tilde{Ξ}_{L}$ is $-1$, of $\tilde{Ξ}_{R}$ is $+1$ |
| $\tilde{Ξ}^*$ | The adjoint with which the currents are formed: the algebra's conjugation |
| $j_{\imath}=\mathrm{Sc}(\tilde{Ξ}^*e_{\imath}\tilde{Ξ}\,b_{\imath})$, $b_t=e_t$, $b_{\imath}=\vec e_z$ | Vector current of the Dirac field; $j_t$ is its Hermitian norm |
| $j_{5\imath}=\mathrm{Sc}(\tilde{Ξ}^*ie_{\imath}\tilde{Ξ}\,\vec e_z\vec e_{\tau(\imath)}\vec e_x)$, $\tau(t)=x$, $\tau(k)=y$ | Axial current; $\sum_{\imath}\partial j_{5\imath}/\partial R_{\imath}=2im\,\mathrm{Sc}(\tilde{Ξ}^*\tilde{Ξ}\vec e_y)$ |
| $x_{\imath} = (r'_{t},r_x,r_y,r_z)$ | Real coordinates of the energy–momentum tensor, the chart of $Q_{\imath}$ at $Q_t=i q'_t$ |
| $T_{\imath\jmath} = (\partial{\xi_{\mathrm{scl}}}^*/\partial x_{\imath})(\partial\xi_{\mathrm{scl}}/\partial x_{\jmath}) + (\partial\xi_{\mathrm{scl}}/\partial x_{\imath})(\partial{\xi_{\mathrm{scl}}}^*/\partial x_{\jmath}) + \varepsilon_{\imath}\delta_{\imath\jmath}\mathcal{L}_{\mathrm{scl},\xi}$ | Canonical energy–momentum in the real coordinates; the coefficient of $\mathcal{L}_{\mathrm{scl},\xi}$ is the plain form of the two units |
| $\tilde\Sigma_{\Psi} = \tfrac{\epsilon}{2}\tilde{F}\tilde{F}^{*} = W\,e_t + \frac{i}{c}\vec S$ | Maxwell energy–momentum (time row), in $\mathbb{B}_{\Psi}$; $\mathrm{Sc}(\tilde\nabla_\Phi\tilde\Sigma_{\Psi})=\frac{i}{c}\vec J\cdot\vec E$ |
| $L_{\imath\jmath} = x_{\imath} p_{\jmath} - x_{\jmath} p_{\imath}$, $\tilde L = \tfrac12\sum L_{\imath\jmath}\,e^{\natural}_{\imath} e_{\jmath}$ | Angular momentum and its bivector |
| $\tilde P_{\Phi} = i\frac{\omega}{c}e_t + 2\pi\vec\nu_\Phi$ | Four-wavevector, in $\mathbb{B}_{\Phi}$; plane-wave phase $\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_\Phi^{\natural}) = 2\pi\vec\nu_\Phi\cdot\vec r-\omega r'_t/c$ |
| $\exp\!\bigl(i\,\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_{\Phi,0}^{\natural})\bigr)=\exp(-i\theta_{\mathrm{pwp}})$, $\mathrm{Sc}(\tilde P_{\Phi}\tilde{R}_{\Phi,0}^{\natural})=2\pi\vec\nu_\Phi\cdot\vec R_0-\omega r'_{t,0}/c$ | Central translation multiplier on a plane wave, of unit modulus |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle=\varepsilon_{\imath} Q_{1\imath}Q_{2\imath}$ | the general plain bilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2)$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{\natural}=\langle\tilde{Q}_2\rangle_{\natural}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_{\imath}\lvert Q_{2\imath}\rvert^{2}$ |

## Further Reading

- Emmy Noether, "Invariante Variationsprobleme", *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen*, Mathematisch-physikalische Klasse (1918), 235–257, for the theorem itself and both of its forms, the internal and the spacetime one; the biquaternion form below differs from it in the algebra of the currents, not in the construction.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the canonical energy–momentum tensor, its non-symmetry, and the Belinfante improvement; Steven Weinberg, *The Theory of Quantum Fields*, Vol. 1 (Cambridge, 1995), for the axial current and its divergence.
- [The Relativistic Particle and the Lagrangian: The Stationary-Action Principle](the-relativistic-particle-and-the-lagrangian-the-stationary-action-principle.html) — the actions differentiated here, with the same signs and the same pairing.
- [The AXF Matrices: Axis-Free, Integer Entries](the-axf-matrices-axis-free-integer-entries.html#why-the-pauli-and-the-gamma-displays-are-refused), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- [Relativistic Mechanics in Biquaternionic Form](relativistic-mechanics-in-biquaternionic-form.html) — the action and the conserved current this article starts from.
- [The Klein–Gordon Equation in Biquaternionic Form](the-klein-gordon-equation-in-biquaternionic-form.html) — the field, its Lagrangian form, and the current the Noether derivation reproduces.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) — the chiral pair, the frame in the basis operator algebra, and Kravchenko's two-sided dictionary.
- [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html) — the mass term, the two parts of the Dirac field, and the axial current.
- [The Poincaré Group and the Biquaternion Frame](the-poincare-group-and-the-biquaternion-frame.html) — the symmetry group, and the corrected central translation phase.
- [Exercise: Four-Momentum Conservation in a Collision](exercise-four-momentum-conservation-in-a-collision.html) — the total four-momentum of an isolated system, and the report of the proper-time four-force defect.
- [Exercise: The Electromagnetic Energy–Momentum Tensor](exercise-the-electromagnetic-energy-momentum-tensor.html) — the rank-two translation current and why one biquaternion cannot carry it.
- [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html) — the source conservation and the energy–momentum biquaternion $\tilde\Sigma_{\Psi}$.
- [The Field-Strength Biquaternion and Its Invariants](the-field-strength-biquaternion-and-its-invariants.html) — the bivector representation used for the angular momentum.
- [Angular Momentum and Spin in Biquaternionic Form](angular-momentum-and-spin-in-biquaternionic-form.html) — the angular-momentum algebra and the spin operators.
- [The Minimal Coupling in Biquaternionic Form](the-minimal-coupling-in-biquaternionic-form.html) — the localization of the central phase whose global current is derived here.
- [The Covariant Derivative and Connection in Biquaternionic Form](the-covariant-derivative-and-connection-in-biquaternionic-form.html) — the connection forced by localizing the same symmetry.
- [The Lorentz Transformation as a Biquaternionic Rotation](the-lorentz-transformation-as-a-biquaternionic-rotation.html) — the rotor whose conjugation carries the four-momentum between frames.
- [Four-Vectors and the Interval](four-vectors-and-the-interval.html) and [States, Observables and the Born Weight](states-observables-and-the-born-weight.html) — the two sectors that house the conserved objects.
- [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html) — the algebra, its conjugations, and the local complex structure.
