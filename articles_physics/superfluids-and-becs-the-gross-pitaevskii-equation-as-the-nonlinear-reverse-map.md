# __Superfluids and BECs: The Gross–Pitaevskii Equation as the Nonlinear Reverse Map__

## Introduction

**The Gross–Pitaevskii equation is the one case in which the reverse map's output is an equation that is written down, solved and measured.** The previous articles argued that a fluid with a pressure maps to a nonlinear wave equation; this one exhibits the fluid, the equation and the measurement. A dilute Bose gas at zero temperature has an order parameter, the order parameter obeys the Gross–Pitaevskii equation, and the fluid's density and phase obey the Madelung pair with a quadratic pressure.

**The direction of the map is the one the section has been arguing.** The order parameter is the fundamental object: it is what the theory is written in and what the experiment measures. The fluid is derived from it. The linear Schrödinger equation is the non-interacting limit of the Gross–Pitaevskii equation, and it is reached by setting the coupling to zero, which is also the limit in which the fluid loses its pressure.

**The constant is written $\hbar$ here because the medium is a condensate, and the same slot is written $\sigma_{\mathrm{dsp}}$ in the map's general form.** The two are the same object at two values of the physics: it is a length squared over a time in the classical dispersion case and an action per particle here, and the second-gradient term is $Q_{\mathrm{qnt}}$ in this article's notation and $Q_{\mathrm{kor}}$ in [The Reverse Madelung Map: Fluid to Nonlinear Wave](the-reverse-madelung-map-fluid-to-nonlinear-wave.html).

**The article's most useful content is the pair of exact solutions.** A uniform condensate with repulsive interaction gives the chemical potential and the healing length; a trapped condensate gives the Thomas–Fermi profile and its radius; an attractive condensate gives a bright soliton whose amplitude and width are fixed by its chemical potential. Each is exact, each is checked by substitution, and each is a place where the fluid's variables can be read off the order parameter.

**The article closes with the caveat that the block's denial requires.** The vocabulary of superfluidity agrees with the block's and the objects do not: the block's field is one element with no condensate, no broken symmetry and no many-body state. The agreement of formulas is real and the difference of objects is real, and the article states both.

## The Order Parameter and the Fluid

**The condensate is described by one complex function and its modulus squared is the density.** Write

$$
\psi=\sqrt{\rho_{\mathrm{num}}}\,e^{iS/\hbar},
\qquad
\vec v=\frac{1}{m}\nabla S ,
$$

with $\rho_{\mathrm{num}}$ the number density of condensed particles and $\vec v$ the velocity of the condensate's flow. The Gross–Pitaevskii equation is

$$
i\hbar\,\partial_{t'}\psi=-\frac{\hbar^{2}}{2m}\Delta\psi+g\lvert\psi\rvert^{2}\psi ,
$$

with $g$ the contact coupling, positive for a repulsive interaction and negative for an attractive one.

**Its Madelung pair is the pair of the reverse map with a quadratic pressure.** The imaginary part is the continuity equation, and the real part is the Hamilton–Jacobi equation with the quantum potential and with $V=g\rho_{\mathrm{num}}$. Comparing with the reverse map's relation $\mathrm{d}p_{\mathrm{th}}=\rho_{\mathrm{num}}\mathrm{d}V$ gives

$$
p_{\mathrm{th}}=\frac{g}{2}\rho_{\mathrm{num}}^{2},
$$

which is the polytrope of exponent $2$ in [The Equation of State and the Barotropic Condition](the-equation-of-state-and-the-barotropic-condition.html). So the contact interaction and the quadratic pressure are one datum, and the article's fluid is the map's fourth row.

**The coupling has a microscopic reading and it is measured.** For a dilute gas of hard spheres, $g=4\pi\hbar^{2}a_{\mathrm{sc}}/m$ with $a_{\mathrm{sc}}$ the s-wave scattering length. So the nonlinear term of the wave equation is fixed by a two-body scattering measurement, and the fluid's pressure is fixed by the same number.

## Two Exact Solutions

**The uniform condensate fixes the chemical potential and the healing length.** With $\psi=\sqrt{\rho_0}\exp(-i\mu_{\mathrm{chm}}t'/\hbar)$ and $\mu_{\mathrm{chm}}=g\rho_0$, the equation is satisfied identically: the kinetic term vanishes and the two remaining terms cancel. The chemical potential is the interaction energy per particle, and it is the energy cost of adding one particle to the condensate.

**A disturbance of the uniform state has two scales.** A long-wavelength disturbance propagates at the sound speed

$$
c_{\mathrm{s}}^{2}=\frac{\mathrm{d}p_{\mathrm{th}}}{\mathrm{d}\rho_{\mathrm{mass}}}=\frac{g\rho_0}{m},
$$

and a short-wavelength disturbance is cut off at the healing length

$$
\xi=\frac{\hbar}{\sqrt{2mg\rho_0}}=\frac{\hbar}{\sqrt{2}\,m\,c_{\mathrm{s}}} .
$$

The healing length is the distance over which the density recovers from a boundary value, and the two scales are one: their ratio is the only dimensionless combination the uniform state has.

**A trapped condensate gives the Thomas–Fermi profile.** In a harmonic trap $V_{\mathrm{tr}}=\frac12m\omega_{\mathrm{tr}}^{2}r^{2}$, the quantum potential is negligible where the density is large, and the balance of the trap against the interaction gives

$$
g\rho_{\mathrm{num}}(r)=\mu_{\mathrm{chm}}-\tfrac12m\omega_{\mathrm{tr}}^{2}r^{2},
\qquad
R_{\mathrm{TF}}=\sqrt{\frac{2\mu_{\mathrm{chm}}}{m\omega_{\mathrm{tr}}^{2}}} .
$$

The radius is where the density vanishes, and the profile is an inverted parabola. The approximation is the neglect of $Q_{\mathrm{qnt}}$, which is legitimate when $R_{\mathrm{TF}}\gg\xi$ and fails at the edge.

**An attractive condensate gives a bright soliton.** With $g=-g_{\mathrm{att}}<0$ the equation admits

$$
\psi=\sqrt{\frac{2\mu_{\mathrm{chm}}}{g_{\mathrm{att}}}}\;\mathrm{sech}\!\left(\frac{\sqrt{2m\mu_{\mathrm{chm}}}}{\hbar}\,x\right)e^{i\mu_{\mathrm{chm}}t'/\hbar},
$$

which is checked by substitution: the three terms cancel identically for every $\mu_{\mathrm{chm}}>0$. The phase advances as $+\mu_{\mathrm{chm}}t'/\hbar$, so the state's energy is $-\mu_{\mathrm{chm}}$ and the soliton is bound. Its amplitude and its width are both fixed by $\mu_{\mathrm{chm}}$, so the pulse has one parameter and not two.

**The soliton is the fluid at its most nonlinear and its most rigid.** Its density is a sech squared, its velocity is zero, and its shape is preserved because the dispersion of the kinetic term and the steepening of the interaction cancel exactly. That is the same balance as the Korteweg–de Vries soliton, in a different equation, and it is the reason the two are often mentioned together.

## The Linear Limit

**Setting the coupling to zero gives the free Schrödinger equation.** With $g=0$ the Gross–Pitaevskii equation is $i\hbar\partial_{t'}\psi=-\frac{\hbar^{2}}{2m}\Delta\psi$, the free equation of the trilogy. In the fluid's variables the pressure vanishes, so the limit is the pressureless member of the reverse map's family, and its only force is the quantum potential.

**So the linear equation is the non-interacting limit and not the fundamental law.** The order parameter is the same object in both cases; what changes is whether the interaction is present. A condensate with $g=0$ is a gas of non-interacting bosons, which is the case in which the condensate is a single-particle state and the fluid has nothing to carry but the quantum potential.

**This is the article's contribution to the section's thesis, and it is a physical fact rather than a formal one.** In the one condensed-matter system where a Schrödinger-like equation is fundamental, the equation that is fundamental is the nonlinear one. The linear equation is the idealisation obtained by turning the interaction off, and the interaction is what the experiment measures.

## The Direction

**The order parameter is written first, and the fluid is read from it.** The theory's variable is $\psi$; the density and the velocity are defined from it by the polar decomposition; the pressure is not an independent datum but the interaction written in fluid variables. A reader who wanted to start from the fluid would have to invent $\hbar$, $m$ and $g$, and the three together are the theory.

**The measurement confirms the direction.** The condensate fraction, the healing length around a defect, the Thomas–Fermi radius and the soliton's width are all measured, and each is a measurement of the order parameter's parameters. None of them is a measurement of a pressure in a fluid that was known beforehand.

**The two-fluid model of helium is the historical case, and it is the fluid description of the same direction.** Superfluid helium is described by a normal component and a superfluid component, with the superfluid component's flow irrotational and its circulation quantised in units of $h/m$. The description is derived from the condensate's order parameter, and [The Two-Fluid Model in Biquaternionic Form](the-two-fluid-model-in-biquaternionic-form.html) is the block's account of the two-fluid construction. The circulation's unit is the same $h/m$ that the field's nodal set gives, and the agreement is an agreement of formulas with two different objects behind them.

## The Caveat

**The block's denial is about the object and not about the formulas.** [The Relativistic Quantum Space as a Fluid](the-relativistic-quantum-space-as-a-fluid.html) denies that its reading is a superfluid. The denial is exact and it is worth restating in this article's terms: a superfluid is a many-body state with a broken symmetry, an order parameter and a spectrum of excitations; the block's field is one element at each event, with no many-body state, no symmetry to break and no excitations of its own.

**What the two share is the algebra of the polar decomposition and the quantum of circulation.** Both write a complex function as a modulus times a phase, both read the phase's gradient as a velocity, and both find the circulation quantised when the phase winds. That sharing is why the vocabulary transfers, and it is not evidence that the objects are the same.

**The distinction has a testable face.** A condensate's healing length is a physical length set by $g$ and $\rho_0$; the block's field has no healing length, because it has no interaction and no density to heal to. So the two descriptions agree in the formulas that use only $\hbar$ and $m$ and diverge in the formulas that use $g$.

## What Is Established and What Is Interpretation

**Established.** That the Gross–Pitaevskii equation's Madelung pair is the reverse map's pair with $p_{\mathrm{th}}=\frac12g\rho_{\mathrm{num}}^{2}$, by comparison of the two. That the uniform state, the sound speed, the healing length, the Thomas–Fermi profile and the bright soliton are exact solutions of the stated equations, each checked by substitution. That $g=4\pi\hbar^{2}a_{\mathrm{sc}}/m$ for a dilute gas. That the linear Schrödinger equation is the $g=0$ limit.

**Interpretation.** That the direction of explanation is the order parameter to the fluid, and that this is the section's thesis in a physical case. That the agreement of the quantum of circulation with the field's is an agreement of formulas and not of objects is the block's reading, and the healing-length test is what makes it more than a preference.

**Not claimed.** It is not claimed that every superfluid is a dilute Bose gas; helium is strongly interacting and its two-fluid model is not the Gross–Pitaevskii equation. It is not claimed that the block's field is a condensate in any limit; it is not, and the section's thesis does not need it to be. It is not claimed that the bright soliton is stable in three dimensions without a trap; in three dimensions an attractive condensate collapses, and the soliton is a one-dimensional object.

## Summary

A dilute Bose gas at zero temperature has one order parameter, and its modulus squared is the density and its phase's gradient over the mass is the velocity.

The order parameter obeys the Gross–Pitaevskii equation, and its Madelung pair is the reverse map's pair with the quadratic pressure $p_{\mathrm{th}}=\frac12g\rho_{\mathrm{num}}^{2}$. The contact coupling $g=4\pi\hbar^{2}a_{\mathrm{sc}}/m$ is measured by two-body scattering.

The uniform state fixes the chemical potential $\mu_{\mathrm{chm}}=g\rho_0$, the sound speed $c_{\mathrm{s}}=\sqrt{g\rho_0/m}$ and the healing length $\xi=\hbar/(\sqrt2mc_{\mathrm{s}})$. A trapped condensate has the Thomas–Fermi profile and radius. An attractive condensate has a bright soliton whose amplitude and width are both fixed by $\mu_{\mathrm{chm}}$.

The linear Schrödinger equation is the $g=0$ limit, and the fluid's pressure vanishes in the same limit. So in the one case where a Schrödinger-like equation is fundamental the equation is the nonlinear one.

The direction is the order parameter to the fluid. The historical two-fluid model of helium is the same direction, and its quantum of circulation is the $h/m$ that the block's nodal set also gives.

The block's denial stands: the sharing is of formulas, not of objects, and the healing length is the formula where the two part company.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\psi=\sqrt{\rho_{\mathrm{num}}}e^{iS/\hbar}$ | Order parameter |
| $\rho_{\mathrm{num}},\ \rho_0$ | Number density and its uniform value |
| $S$ | Action; the phase is $S/\hbar$ |
| $\vec v=\nabla S/m$ | Condensate velocity |
| $g$ | Contact coupling; $g=4\pi\hbar^{2}a_{\mathrm{sc}}/m$ |
| $a_{\mathrm{sc}}$ | s-wave scattering length |
| $\mu_{\mathrm{chm}}$ | Chemical potential |
| $p_{\mathrm{th}}=\frac12g\rho_{\mathrm{num}}^{2}$ | Pressure of the condensate |
| $c_{\mathrm{s}}=\sqrt{g\rho_0/m}$ | Sound speed |
| $\xi=\hbar/\sqrt{2mg\rho_0}$ | Healing length |
| $V_{\mathrm{tr}}=\frac12m\omega_{\mathrm{tr}}^{2}r^{2}$ | Harmonic trap |
| $\omega_{\mathrm{tr}}$ | Trap frequency |
| $R_{\mathrm{TF}}=\sqrt{2\mu_{\mathrm{chm}}/(m\omega_{\mathrm{tr}}^{2})}$ | Thomas–Fermi radius |
| $g_{\mathrm{att}}=-g>0$ | Attractive coupling |
| $Q_{\mathrm{qnt}}$ | Quantum potential |

## Further Reading

- Eugene P. Gross, "Structure of a quantized vortex in boson systems," *Nuovo Cimento* **20** (1961) 454–477, and Lev P. Pitaevskii, "Vortex lines in an imperfect Bose gas," *Soviet Physics JETP* **13** (1961) 451–454, for the equation.
- Vitaly L. Ginzburg and Lev P. Pitaevskii, "On the theory of superfluidity," *Soviet Physics JETP* **7** (1958) 858–861, for the order parameter and the healing length.
- Nikolay N. Bogoliubov, "On the theory of superfluidity," *Journal of Physics USSR* **11** (1947) 23–32, for the sound speed and the microscopic reading of the coupling.
- Franco Dalfovo, Stefano Giorgini, Lev P. Pitaevskii and Sandro Stringari, "Theory of Bose–Einstein condensation in trapped gases," *Reviews of Modern Physics* **71** (1999) 463–512, for the Thomas–Fermi profile, the healing length and the solitons.
- Christopher J. Pethick and Henrik Smith, *Bose–Einstein Condensation in Dilute Gases* (Cambridge University Press, 2002), ch. 6 and 7, for the Gross–Pitaevskii equation and its exact solutions.
- Lev D. Landau and Evgeny M. Lifshitz, *Fluid Mechanics*, 2nd ed. (Pergamon, 1987), §141, for the two-fluid model of superfluid helium and the criterion for superfluidity.
- The companion articles: [The Equation of State and the Barotropic Condition](the-equation-of-state-and-the-barotropic-condition.html), [The Reverse Madelung Map: Fluid to Nonlinear Wave](the-reverse-madelung-map-fluid-to-nonlinear-wave.html), [The Direction of the Fluid-Wave Correspondence, Field by Field](the-direction-of-the-fluid-wave-correspondence-field-by-field.html), [The Two-Fluid Model in Biquaternionic Form](the-two-fluid-model-in-biquaternionic-form.html).
- [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html), for the same $h/m$ in the field, and [The Relativistic Quantum Space as a Fluid](the-relativistic-quantum-space-as-a-fluid.html), for the denial this article restates.
