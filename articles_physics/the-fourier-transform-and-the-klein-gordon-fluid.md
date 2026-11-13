# __The Fourier Transform and the Klein–Gordon Fluid: The Mode Is a Unit Velocity__

## Introduction

**The Klein–Gordon fluid's one defect is that its four-velocity is a unit only where the quantum potential vanishes, and a mode is exactly a point where it does.** That is the article's finding, and it is a statement about supports. The shell is $E^{2}/c^{2}-\lvert\vec p\rvert^{2}=m^{2}c^{2}+2mQ_{\mathrm{qnt}}$, so a mode — whose scale is constant and whose $Q_{\mathrm{qnt}}$ therefore vanishes — sits exactly on the mass shell, and it sits there with a unit four-velocity and with no qualification at all.

**The defect is a radial displacement of the support, and that is the second finding.** The quantum potential enters the shell's right-hand side, so it changes the radius of the local hyperboloid and not its centre. The charged companion's potential does the opposite: it enters as a translation and leaves the radius alone. **Two potentials, one radial and one translational, and the momentum-space picture separates them without any algebra.**

**The third finding is about the sheets.** The conserved density is the charge density and its sign is the sign of the energy, so a mode lies on one sheet and one sheet only. A single mode's charge density has a definite sign. A superposition that occupies both sheets has a density of both signs, and the article gives the measured range.

**Position in the block.** This is the Fourier companion of [The Klein–Gordon Fluid](the-klein-gordon-fluid.html) and of [The Lagrangian of the Klein–Gordon Fluid](the-lagrangian-of-the-klein-gordon-fluid.html). Its charged companion is [The Fourier Transform and the Charged Klein–Gordon Fluid](the-fourier-transform-and-the-charged-klein-gordon-fluid.html). The rung below is [The Fourier Transform and the Schrödinger Fluid](the-fourier-transform-and-the-schrodinger-fluid.html), and §*The Two Scalar Rungs* states what the passage removes.

## Conventions

The free companion's: $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon\,e_t$ on a central field, $\rho_{\mathrm{num}}=r^{2}$, $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$, $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial r_{t}^{\prime 2}$ on the material sector, and

$$
Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\frac{\Box_\Phi r}{r},
\qquad
\tilde V_{\Phi}=\frac{\tilde P_{\Phi}}{m},
\qquad
\tilde P_{\Phi}=\tilde\nabla_\Phi S_{\tilde\Xi},
\qquad
\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}},
\qquad
k_m=\frac{mc}{\hbar}.
$$

The symbol rule is the Schrödinger rung's, with the temporal slot written once: a plane wave carries $e^{i(\vec k_\Phi\cdot\vec r-k_t'r_t')}$ with $k_t'=\omega/c=E/(\hbar c)$, so $\partial/\partial r_t'\mapsto-ik_t'$ and $\tilde\nabla_\Phi\mapsto i\tilde K_\Phi$ with $\tilde K_\Phi=ik_t'e_t+\vec k_\Phi$.

## The Mode, and the Second-Order Shell

**A mode is a point of $\tilde K_\Phi$ and one complex amplitude.**

$$
\tilde\Xi=a\,e^{i(\vec k_\Phi\cdot\vec r-k_t'r_t')}e_t,
\qquad
r=\lvert a\rvert,
\qquad
\rho_{\mathrm{num}}=\lvert a\rvert^{2},
\qquad
\vec v=\frac{\hbar\vec k_\Phi}{m},
\qquad
\gamma=\frac{\hbar k_t'}{mc}.
$$

**The quantum potential vanishes at a mode for the same reason as at the rung below: the scale is constant.**

$$
\Box_\Phi r=0
\qquad\Longrightarrow\qquad
Q_{\mathrm{qnt}}=0 ,
$$

and this is not an approximation in any parameter. The amplitude equation, which is the mass shell with the curvature term, therefore loses its curvature term and becomes the mass shell outright:

$$
\frac{E^{2}}{c^{2}}-\lvert\vec p\rvert^{2}=m^{2}c^{2},
\qquad
E=\hbar c\,k_t',
\qquad
\vec p=\hbar\vec k_\Phi .
$$

**The unit velocity is then exact.**

$$
\langle\tilde V_\Phi\rangle_{\natural}
=-\frac{1}{m^{2}}\Bigl(\frac{E^{2}}{c^{2}}-\lvert\vec p\rvert^{2}\Bigr)
=-c^{2}
$$

at a mode, by the display above and by nothing else. The check on the two modes $(\vec k_\Phi,k_t')=(0.7,1.220656)$ and $(0.3,1.044031)$, with $m=c=\hbar=1$, gave $\langle\tilde V_\Phi\rangle_{\natural}=-1.000000$ in both cases.

**So the companion's qualification is a statement about how many modes are present.** The velocity is a unit wherever the local word is a single mode, and the failure of the unit is the measure of the local admixture. **That is what $Q_{\mathrm{qnt}}$ is, in the momentum-space reading: a measure of the distance between the local field and a single point of the shell.**

**The stated objection, and the answer.** The objection is that "$Q_{\mathrm{qnt}}=0$ at a mode" is trivial, since $Q_{\mathrm{qnt}}$ carries derivatives and a plane wave has none. The objection is correct and the triviality is the finding: a defect that vanishes on a dense set of the solutions and that is a derivative functional is a defect of the *superposition* and not of the equation. **The companion states the defect as a condition on the solution; this article states it as a condition on the support**, and the second statement is the one that says what has to be added to a mode to produce it.

## The Support, and the Two Potentials

**A transform is a measure on a support, and the two potentials of the block act on different attributes of that support.**

| what is added | what it does to the shell | the momentum-space face |
| --- | --- | --- |
| the quantum potential $Q_{\mathrm{qnt}}$ | changes the radius: $m^{2}c^{2}\mapsto m^{2}c^{2}+2mQ_{\mathrm{qnt}}$ | the local support is a hyperboloid of a different size |
| the connection $\varkappa\tilde A_\Phi$ | changes the centre: $\tilde K_\Phi\mapsto\tilde K_\Phi-\varkappa\tilde A_\Phi/\hbar$ | the local support is a translated hyperboloid |

**The first row is this article's and the second is the charged companion's, and the comparison is the reason to state both.** A radius cannot be removed by a change of variable and a centre can: a shift of a variable does not change a radius, and a translation is undone by a translation. **So the quantum potential is an intrinsic deformation of the support and the connection is a change of chart**, and the two statements are the two articles' first results in the momentum-space language.

**The radius reading survives the sum.** For a general solution the two effects compose and the local support is a translated hyperboloid of shifted radius, which is the mass shell of the companion's equation with both terms in it. Nothing in the composition is an approximation, because the shell is an identity and not an expansion.

## The Two Sheets

**A mode lies on one sheet.** The charge density is $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$ with $\gamma=E/(mc^{2})$, so its sign is the sign of the mode's energy:

$$
\rho_{\mathrm{chg}}=\frac{\hbar k_t'}{mc}\lvert a\rvert^{2}\ \text{ for the mode }(\vec k_\Phi,k_t'),
$$

and a negative-frequency mode carries a negative charge density. **The two sheets of the hyperboloid are two disjoint supports, so no mode can straddle them**: a point of the support is on one sheet or the other, and the transform of a mode is a delta at one point.

**A superposition that occupies both sheets has a density of both signs, and the amplitudes decide whether it does.** On one hundred events with $\vec k_\Phi=5.0$ on the positive sheet and $\vec k_\Phi=0.1$ on the negative one, amplitudes $0.5$ and $1.0$, the charge density ran from $-1.777$ to $+2.317$. With amplitudes $1.0$ and $1.0$ the same pair gave $0.0005$ to $8.188$, of one sign. **So the sign change is not automatic even when both sheets are occupied**, and the reason is arithmetic: the incoherent part and the cross term have opposite signs and the cross term's magnitude is bounded by twice the geometric mean of the two incoherent parts, so the balance decides.

**The exact statement that survives every case is the per-mode one.** A mode's density has the sign of its energy, exactly, and the two sheets are disjoint supports; anything beyond that is a statement about a particular pair of amplitudes. **That is the honest form of the companion's two-sheetedness in momentum space**, and the article claims no more.

## The Two Scalar Rungs

**The passage from this rung to the one below removes the mass from the shell, and the momentum-space table says so in one row.**

| | the Schrödinger rung | the Klein–Gordon rung |
| --- | --- | --- |
| the shell | none: the Hamilton–Jacobi equation constrains nothing | $E^{2}/c^{2}-\lvert\vec p\rvert^{2}=m^{2}c^{2}+2mQ_{\mathrm{qnt}}$ |
| the support of a solution | any set of points of the momentum space | a measure on the two-sheeted hyperboloid |
| the sign of the density | one sign, always | the sign of the energy |
| the velocity | $\hbar\vec k/m$, unbounded | $\hbar\vec k/m$ with $\gamma$ fixed by the shell |
| $Q$ at a mode | zero | zero |
| what $Q$ does | deforms the density | deforms the radius of the support |

**The last row is the one the rung above adds, and it is the whole of the difference.** At the first-order rung the quantum potential has no shell to deform and its only face is the density; here it has a shell and its face is a radius. **The same functional, two pictures**, and the second picture is available only because the equation is second order.

**The fifth row is the invariant across the two rungs.** The quantum potential vanishes at a mode at both, for the same reason and with no parameter in the statement, and the free companion's cross-term reading of it therefore transfers without change. That is why the two Fourier articles of the scalar rung are one article in two orders of the equation, and why their findings are the same finding.

## Limits

**Constant coefficients.** The shell is an identity for constant $m$, so the free case is exact throughout. A potential $V(\vec r)$ makes the symbol position-dependent, and the article uses none.

**The particle setting.** The article works with plane waves and their superpositions and never with a general solution's spectral measure. A general solution's support is a measure on the shell with an element-valued density, and nothing above needs it.

**The denial.** The transform carries $\mathbb{B}_\Phi$-valued fields to $\mathbb{B}_\Phi$-valued fields. No step carries a field out of its sector, and the amplitude at a wave number is the same numbers the field had at an event, resummed.

## Open Questions

1. **Whether the radius reading is a bound.** The companion's charge-sign boundary is a condition on the parameters; in momentum space the question is whether the shifted radius $m^{2}c^{2}+2mQ_{\mathrm{qnt}}$ can be made negative by a large enough curvature and, if so, what the support looks like there. The companion's discussion of the charge-sign boundary suggests the answer is a change of the support's topology, and the article does not settle it.

2. **The measure of the admixture.** $Q_{\mathrm{qnt}}$ is one scalar measure of how far the local field is from a single mode. Whether a spectral measure exists that is additive over modes and reduces to $Q_{\mathrm{qnt}}$ at a single mode is open, and the non-additivity proved at the rung below is evidence against the simplest candidate.

3. **The two-sheet balance.** §*The Two Sheets* exhibits amplitudes of one sign and of both signs at the same pair of wave numbers. Whether the boundary between the two cases is a simple inequality in the amplitudes and the two energies is not settled here.

## Summary

A mode has a constant scale, so its quantum potential vanishes exactly, and the mass shell it satisfies is the plain one, $E^{2}/c^{2}-\lvert\vec p\rvert^{2}=m^{2}c^{2}$. Its four-velocity is therefore a unit exactly, and the companion's qualification — a unit only where the quantum potential vanishes — is a statement that a mode is exactly such a place.

The quantum potential is a measure of the distance between the local field and a single point of the shell. It acts on the radius of the support; the connection acts on the centre. A radius cannot be removed by a change of variable and a centre can, so the quantum potential is an intrinsic deformation and the connection is a change of chart.

The charge density of a mode is $\hbar k_t'\lvert a\rvert^{2}/(mc)$ and its sign is the sign of the energy, so a mode lies on one sheet of the two-sheeted hyperboloid and the sheets are disjoint supports. A superposition that occupies both can have a density of both signs: on one hundred events the amplitudes $0.5$ and $1.0$ gave $-1.777$ to $+2.317$, and equal amplitudes gave $0.0005$ to $8.188$.

The passage to the first-order rung removes the shell and with it the radius reading, and keeps the vanishing of $Q_{\mathrm{qnt}}$ at a mode unchanged. The same functional has two pictures, one on the density and one on the radius, and the second exists only because the equation is second order.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon\,e_t$ | The central field, in its word |
| $k_t'=\omega/c=E/(\hbar c)$, $\vec k_\Phi=\vec p/\hbar$ | The label of a mode |
| $k_m=mc/\hbar$ | The mass wave number |
| $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial r_{t}^{\prime 2}$ | The d'Alembertian on the material sector |
| $Q_{\mathrm{qnt}}=-\hbar^{2}\Box_\Phi r/(2mr)$ | The quantum potential; zero at a mode |
| $\tilde V_\Phi=\tilde P_\Phi/m=\tilde\nabla_\Phi S_{\tilde\Xi}/m$ | The four-velocity |
| $\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}-2Q_{\mathrm{qnt}}/m$ | Its norm; $-c^{2}$ at a mode |
| $\rho_{\mathrm{chg}}=\gamma\rho_{\mathrm{num}}$, $\gamma=E/(mc^{2})$ | The conserved density |
| $\tilde K_\Phi=ik_t'e_t+\vec k_\Phi$ | The wave number element |
| $\varepsilon=\pm1$ | The branch |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part |

## Further Reading

- Erwin Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1926) 322–326, for the pair in its original form.
- Louis de Broglie, *Non-Linear Wave Mechanics: A Causal Interpretation* (Elsevier, 1960), for the second-order fluid and the quantum potential in the relativistic case.
- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 2–35, for the relativistic scalar and spinor fluids set side by side.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), chapter 9, for the Klein–Gordon fluid, its quantum potential and the two sheets.
- The companion articles: [The Klein–Gordon Fluid](the-klein-gordon-fluid.html), for the pair and the $\gamma^{-1}$ acceleration law; [The Lagrangian of the Klein–Gordon Fluid](the-lagrangian-of-the-klein-gordon-fluid.html), the rung as an action; [The Fourier Transform and the Schrödinger Fluid](the-fourier-transform-and-the-schrodinger-fluid.html), the rung below, where the cross-term reading of $Q$ is proved and the shell does not exist; and [The Fourier Transform and the Charged Klein–Gordon Fluid](the-fourier-transform-and-the-charged-klein-gordon-fluid.html), where the support is translated instead of dilated.
