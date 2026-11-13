# __The Fourier Transform and the Charged Schrödinger Fluid: The Vorticity Is the Curvature__

## Introduction

**The charged Schrödinger fluid's vorticity is $\varkappa\vec B/m$, and $\vec B$ is a property of the connection and not of the wave.** That single fact decides the whole of the momentum-space reading. A connection that is constant is a multiplier, it carries no curvature, and it mixes no modes; a connection with curvature is not a multiplier and cannot be tested mode by mode. **So the fluid's rotation is exactly the part of the physics that a mode basis cannot represent**, and the four statements below are that sentence unwound.

**The article's claim, in one line.** The mode basis of the charged Schrödinger fluid is the mode basis of the flat connections. A curvature is invisible to it, and the vorticity of this fluid is nothing but its curvature.

**Why that is a result and not a tautology.** In the free rung the vorticity vanishes and the mode basis is the whole of the physics, since the density, the velocity and the quantum layer are all readable mode by mode. Here the vorticity is non-zero and no mode carries it. **The two rungs have the same Fourier basis and different physics**, and the difference is a property of the connection, which is external to the field. The transform tells the two apart by one quantity: whether the profile of the connection is constant.

**Position in the block.** This is the charged companion of [The Fourier Transform and the Schrödinger Fluid](the-fourier-transform-and-the-schrodinger-fluid.html) and the Fourier companion of [The Charged Schrödinger Fluid: The Vorticity Is the Magnetic Field](the-charged-schrodinger-fluid.html). It repeats, at this rung, the mode-counting finding of [The Fourier Transform and the Coupled Dirac Equation in Biquaternionic Polar Variables](the-fourier-transform-and-the-coupled-dirac-equation-in-biquaternionic-polar-variables.html), and it repeats it deliberately: the two rungs ask the same question and the answer is the same, with the vorticity named in place of the mode count.

## Conventions

The charged companion's: $\tilde A_\Phi=i(\varphi/c)e_t+\vec A$ with $\varphi$ and $\vec A$ real, the coupling $\varkappa$ being minus the electric charge, the covariant derivative $\partial_\mu+\frac{i\varkappa}{\hbar}A_\mu$, and the gauge transformation $\lambda=\exp(i\varkappa\Gamma/\hbar)$ with $\Gamma$ real. The field is central, $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon\,e_t$, and the two invariants are

$$
\vec\pi=\hbar\nabla\theta_{\mathrm{pha}}+\varkappa\vec A=\nabla S+\varkappa\vec A,
\qquad
\mathcal E=-\hbar\,\partial_{t'}\theta_{\mathrm{pha}}+\varkappa\varphi,
\qquad
\vec v=\frac{\vec\pi}{m}.
$$

The transform's symbol rule is the free companion's. The curvature is $\vec B=\nabla\times\vec A$ and $\vec E=-\nabla\varphi-\partial_{t'}\vec A$.

## The Mode of a Flat Connection

**A constant connection leaves the mode a mode.** Take $\tilde A_\Phi$ constant, so that $\vec B=0$ and $\varphi$ is constant. A plane wave $\tilde\Xi=a\,e^{i(\vec k\cdot\vec r-\omega t')}e_t$ is a solution with the label

$$
\vec\pi=\hbar\vec k+\varkappa\vec A,
\qquad
\vec v=\frac{\hbar\vec k+\varkappa\vec A}{m},
\qquad
\nabla\times\vec v=0 ,
$$

and the last equality is the article's first result. **The velocity is constant and its curl is exactly zero**, and the check on one hundred events gave $\max\lvert\nabla\times\vec v\rvert=2.5\times10^{-16}$ for a constant $\vec A$.

**The constant connection is a pure gradient and the mode is free in disguise.** With $\vec A=\nabla\chi$ and $\varphi=-\partial_{t'}\chi$ the gauge transformation $\lambda=\exp(i\varkappa\chi/\hbar)$ removes the connection and multiplies the field by a central phase, which moves the label and changes nothing else. So a mode of a flat connection is gauge-equivalent to a free mode with a translated wave number, and the translation is $\varkappa\vec A/\hbar$.

**The two labels, and which one the fluid reads.**

$$
\tilde K_\Phi=\tilde K_{\Phi,\mathrm{gco}}-\frac{\varkappa}{\hbar}\tilde A_\Phi ,
$$

so the canonical label is the free one and the kinetic label is the free one plus the potential. **The transform is a chart-dependent object here for the first time in this rung**: transforming in the canonical variable puts the support on the free shell, transforming in the kinetic variable puts it on the translated shell, and the two differ by a gauge. §*Two Supports, One Field* of the charged Klein–Gordon Fourier companion carries the same distinction with the mass present.

## The Curvature Is What a Multiplier Cannot Carry

**The identity is one line and the check is exact.**

$$
\nabla\times\vec v=\frac{1}{m}\nabla\times\bigl(\hbar\nabla\theta_{\mathrm{pha}}+\varkappa\vec A\bigr)=\frac{\varkappa}{m}\vec B ,
$$

since the curl of a gradient vanishes wherever the phase is twice differentiable. On one hundred events with a uniform field $\vec B=0.6\vec e_z$ and a phase carrying a cross term, the residual was $5.0\times10^{-16}$.

**Read as a statement about profiles, the identity says that the vorticity is the second derivative of the connection and nothing else.** A constant connection has zero curvature, a linear connection has constant curvature, and a connection of higher order has a varying one. **No mode of the field can supply a curvature, because a mode's connection is at most a constant**; so the vorticity of this fluid is invisible to the basis by construction and not by an unlucky cancellation.

**The mode count makes the same point in the coupled Dirac article's numbers, and they transfer.** There, a constant connection left one occupied mode out of sixty-four with the median coefficient at $3.6\times10^{-16}$ of the peak; a linear connection left all sixty-four, with the envelope $\lvert G(k_0+\Delta)\rvert\cdot\lvert\Delta\rvert$ constant at $38.4$ to within $1.3\%$ over $\Delta=1,\dots,8$. **A linear profile is the profile whose transform is the derivative of a delta**, so the coupling falls as the inverse of the separation; that inverse law is the momentum-space face of a constant field strength, and of nothing else.

**So the two cases are the two curvatures.**

| the connection | its curvature | its transform | what the fluid does |
| --- | --- | --- | --- |
| constant | zero | a delta | one mode, no vorticity, gauge-removable |
| linear | constant | a derivative of a delta | no mode survives; the vorticity is the constant |
| smooth bump | localised | a narrow kernel | a few neighbours; a localised eddy |
| a spike | a distribution | a nearly flat kernel | every mode; vorticity everywhere |

**The first two rows are the theorem and the last two are the illustration.** The theorem is that the vorticity is read from the curvature and the curvature from the profile's second derivative, so the mode basis, which is a basis of first derivatives, sees the profile only through its transform and never through its curvature directly.

## The Circulation of a Mode

**A mode carries the flux quantum and not the winding quantum.** The charged companion's circulation is

$$
\oint\vec\pi\cdot\mathrm{d}\vec l=2\pi\hbar\,n+\varkappa\Phi_B ,
\qquad
\Phi_B=\int_S\vec B\cdot\mathrm{d}\vec S ,
$$

around a loop that links a nodal line of winding $n$. A mode has no node, as the free companion's §*The Mode, and the One Bracket It Occupies* shows, so $n=0$ and what remains is

$$
\oint\vec\pi\cdot\mathrm{d}\vec l=\varkappa\Phi_B .
$$

**That is exact and it is the only circulation a single mode has.** The quantum of winding is inter-mode and the quantum of flux is not; the first needs a pair of waves and the second needs only a field. In the free rung both terms were absent at a mode; here one of the two survives, and the one that survives is the one the connection supplies.

**The statement is the Aharonov–Bohm phase, read on a loop.** The flux term is the phase $\exp(i\varkappa\Phi_B/\hbar)$ that a mode acquires on going round, and it is there whether or not the field strength vanishes on the loop. **A mode's loop datum is therefore a phase and not the integer**, and the integer appears only when a second mode is added and a node exists.

**The objection, and the answer.** The objection is that the flux term is a gauge artefact in a simply connected region with vanishing curvature, so a mode's circulation is removable. The answer is that it is removable iff $\Phi_B$ is a multiple of $2\pi\hbar/\varkappa$ on the loops at issue, and that on a loop that links a flux the integral is not removable in any single-valued gauge. **The quantum of flux is a statement about the topology of the region and the quantum of winding is a statement about the topology of the field**, and a mode has only the first.

## Two Supports, One Field

**The transform of a solution is a measure on a support, and which support depends on the variable.** In the canonical variable the support is the free shell $\mathcal E^{2}/c^{2}-\lvert\vec p\rvert^{2}=m^{2}c^{2}$; in the kinetic variable it is the same shell translated by the potential. Since the two variables differ by a gauge transformation, and a gauge transformation of a linear phase translates the support, **the two supports are the same set of physical states written in two charts.**

**What that buys the fluid reading is one sentence.** The velocity is $\vec\pi/m$, so it is the kinetic label over the mass; a mode's velocity is therefore read from the kinetic support and not from the canonical one. **The chart in which the support is free is the chart in which the fluid is not**, and the chart in which the fluid's velocity is the label is the chart in which the support is translated. The free companion's maxim that the canonical flow is irrotational and the kinetic flow is the field's is the same statement seen from the two charts.

**What is gauge invariant is the curvature, and it is the only thing that is.** The mode count, the support, the envelope, the label: all change with the chart. The curvature does not. **So the momentum-space reading of this fluid has exactly one invariant, and it is the vorticity.** That is the article's summary sentence in one line.

## Limits

**Constant coefficients.** The multiplier reading of the coupling needs the connection to be constant; the mode count does not, since a convolution is defined for any profile. The licence is stated, used in §*The Mode of a Flat Connection*, and dropped in §*The Curvature Is What a Multiplier Cannot Carry*.

**The abelian component form.** The connection's coefficients are central scalars, so the coupling is a convolution of the field with a kernel and the count of mixed modes is a property of one profile. A non-abelian connection would add a commutator and the count would not be a property of one profile.

**The denial.** Every object is an element of $\mathbb{B}$ or a coefficient of one, and no step carries a field out of its sector.

## Open Questions

1. **Whether the vorticity has a spectral measure.** The curvature is invariant and the mode count is not. Whether some spectral quantity — the second moment of the occupied modes, say — is a function of the curvature alone and not of the gauge is not settled, and the linear case suggests it may be, since its $1/\Delta k$ envelope is the transform of a constant field strength.

2. **A mode in a uniform field.** A uniform $\vec B$ admits no mode, so the fluid's rotation in a uniform field is not analysable mode by mode at all. Whether the Landau levels of the standard theory are the right image of that statement in this chart, and whether the fluid's velocity is the drift or the gyration, is not established here and the article claims nothing about it.

3. **The flux quantum without a node.** §*The Circulation of a Mode* finds $\varkappa\Phi_B$ for a mode with no node. Whether a single mode on a topologically non-trivial region is a legitimate solution of the equation in this chart, given that the chart needs the field nowhere zero and the region has a hole, is a question about the domain and not about the transform.

## Summary

The charged Schrödinger fluid's velocity is $(\hbar\nabla\theta_{\mathrm{pha}}+\varkappa\vec A)/m$ and its vorticity is $\varkappa\vec B/m$ exactly, with residual $5.0\times10^{-16}$ on one hundred events and the curl of a gradient vanishing identically.

A constant connection is a multiplier, carries no curvature, mixes no modes and is a pure gradient, so a mode of a flat connection is a free mode with a translated label and zero vorticity, checked at $2.5\times10^{-16}$.

A connection with curvature is not a multiplier. Its transform is a derivative of a delta for a linear profile, and the coupling then falls as the inverse of the separation, which is the momentum-space face of a constant field strength.

**So the mode basis is the mode basis of the flat connections, and the vorticity is exactly what it cannot carry.** The fluid's rotation is invisible to the Fourier decomposition by construction, and the one gauge-invariant object of the momentum-space reading is the curvature.

A mode carries the flux quantum and not the winding quantum: its circulation is $\varkappa\Phi_B$ and not $2\pi\hbar n+\varkappa\Phi_B$, because a mode has no node. The winding quantum is inter-mode and the flux quantum is not.

The field has two supports, the free shell in the canonical variable and the translated shell in the kinetic one, and they are the same states in two charts. The velocity is read from the kinetic label, so the chart in which the fluid's velocity is the label is the chart in which the support is translated.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\varkappa$ | The coupling; minus the electric charge |
| $\tilde A_\Phi=i(\varphi/c)e_t+\vec A$ | The connection |
| $\vec\pi=\hbar\nabla\theta_{\mathrm{pha}}+\varkappa\vec A$ | The kinetic momentum |
| $\mathcal E=-\hbar\partial_{t'}\theta_{\mathrm{pha}}+\varkappa\varphi$ | The kinetic energy |
| $\vec v=\vec\pi/m$ | The velocity |
| $\vec B=\nabla\times\vec A$, $\vec E=-\nabla\varphi-\partial_{t'}\vec A$ | The field strength |
| $\vec\omega=\varkappa\vec B/m$ | The vorticity; the curvature |
| $\Phi_B$ | The flux through a loop's spanning surface |
| $\tilde K_\Phi=\tilde K_{\Phi,\mathrm{gco}}-\varkappa\tilde A_\Phi/\hbar$ | The canonical label less the potential |
| $n$ | The winding of a loop around a nodal line; zero at a mode |
| $\lambda=\exp(i\varkappa\Gamma/\hbar)$ | The gauge element; central |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part |

## Further Reading

- Erwin Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1926) 322–326, for the pair the coupling modifies.
- Yakir Aharonov and David Bohm, "Significance of electromagnetic potentials in the quantum theory," *Physical Review* **115** (1959) 485–491, for the flux phase of a mode on a loop.
- Michael Berry, "Quantal phase factors accompanying adiabatic changes," *Proceedings of the Royal Society A* **392** (1984) 45–57, for the phase-versus-integer distinction the mode's circulation makes.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), chapter 4, for the charged fluid's vorticity and the vector potential's place in it.
- The companion articles: [The Charged Schrödinger Fluid: The Vorticity Is the Magnetic Field](the-charged-schrodinger-fluid.html), for the identity and its rank; [The Fourier Transform and the Schrödinger Fluid](the-fourier-transform-and-the-schrodinger-fluid.html), the free rung where no mode carries a vorticity because there is none; [The Fourier Transform and the Coupled Dirac Equation in Biquaternionic Polar Variables](the-fourier-transform-and-the-coupled-dirac-equation-in-biquaternionic-polar-variables.html), for the mode count this article repeats; and [The Fourier Transform and the Charged Klein–Gordon Fluid](the-fourier-transform-and-the-charged-klein-gordon-fluid.html), where the same two supports appear with the mass present.
