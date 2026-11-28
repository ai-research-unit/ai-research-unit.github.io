# __Mean Field: The Large-$N$ Corner and the Fluid That Comes Out__

## Introduction

**The claim.** Move two coordinates together — $1/N\to0$ and the gradient, meaning that the density varies slowly compared with the inter-particle or coherence scale — and the quantum field becomes a fluid. The variables are a density, a velocity and a spin; the equations are continuity, Euler and spin transport; and the quantum potential, which is the term that produces interference, is discarded by construction.

**The answer.**

$$
\boxed{\;\partial_\mu(\rho u^\mu)=0,\qquad \rho\,u^\nu\partial_\nu u^\mu=\partial^\mu p,\qquad u^\nu\partial_\nu s^\mu=\text{BMT},\qquad \text{with } s\cdot u=0\;}
$$

**Why this corner is not case 2.** [Classical Relativity](classical-relativity-the-corner-with-no-quanta.html) removes the loop and keeps every degree of freedom, so its scalar sector is a field equation. Here the loop is not the coordinate being moved: $1/N$ is, together with the gradient, and the result is not a field equation but a closed system for a finite number of hydrodynamic variables. The difference is that a field has infinitely many degrees of freedom and a fluid has five per point.

## The Arrow

**Three steps, and the third one is the truncation.**

**Step one: the amplitude–phase split.** Write the wavefunction or the field as $\psi=\sqrt\rho\,e^{iS/\hbar}$, so that $\rho$ is a density and $u^\mu=\partial^\mu S/m$ is a velocity. The substitution is exact; nothing has been discarded yet.

**Step two: the quantum potential.** The real part of the equation produces

$$
u^\nu\partial_\nu u^\mu=\partial^\mu\Bigl(-\frac{\hbar^2}{2m^2}\frac{\Box\sqrt\rho}{\sqrt\rho}\Bigr),
$$

which is Euler's equation with an extra pressure-like term — the quantum potential. It is the only term in the equation that is not a function of $\rho$ and $u$ alone through a local equation of state, and it is what makes the system quantum.

**Step three: the gradient expansion.** The quantum potential is $\mathcal{O}(\ell^2/L^2)$ where $\ell$ is the scale over which $\rho$ varies at the level of a wavelength and $L$ is the scale over which it varies macroscopically. Dropping it leaves Euler's equation for a perfect fluid, with the pressure supplied by the equation of state. That drop is the corner.

**Where $1/N$ enters.** For a many-body system the same expansion organises as $1/N$: the leading term is the mean field, the next term is the fluctuation, and the fluctuation is what the corner discards. The two coordinates are therefore the same statement written twice — small gradients and large $N$ both say that the collective variables are slow compared with the microscopic ones.

## What the Corner Reproduces

**Four results, and the last two are the ones that make it a corner rather than an analogy.**

**The continuity equation, exactly.** It follows from the imaginary part of the wave equation with nothing discarded, so the corner's first equation is exact in both coordinates.

**Euler's equation with the correct equation of state.** For a relativistic gas the pressure and energy density satisfy $p=\varepsilon/3$ and the sound speed is $c_s^2=1/3$; the corner reproduces the relativistic Euler equation with the enthalpy in place of the mass density, which is the statement that the inertia of a relativistic fluid is its enthalpy and not its mass.

**Quantised circulation.** The velocity is a gradient, so $\oint u\cdot d\ell=(h/m)\times$ integer about a nodal line. The quantum of circulation survives the corner, because it is a topological statement about the phase and the phase is retained. This is a genuine success of the fluid reading: a quantum number emerging from a classical-looking system.

**The spin transport equation.** For a spin-½ system the fluid carries a spin density whose transport is the BMT equation with the Thomas term, and Takabayasi's four equations are exactly continuity, Euler, the spin transport, and the equation of state closure. The corner therefore contains the spin precession of [the adiabatic corner](wkb-and-eikonal-the-adiabatic-corner.html), derived from a different starting point, which is a check on both.

## What the Corner Cannot Reproduce

**Four failures, and the first is the definition of a mean field.**

**No interference.** The double slit requires two packets with a definite phase relation, and the corner has a single-valued velocity field with no room for two branches. The quantum potential, which was dropped, is precisely the term that would produce the fringes; keeping it would make the system quantum again and would remove the closure.

**No discrete spectrum.** A fluid has a continuous set of states and no eigenvalues. Every quantised level — the hydrogen spectrum, the oscillator, the hadron masses — is outside, and the corner's own quantised circulation is the exception that proves the rule: it is topological and not spectral.

**No tunnelling.** A fluid cannot cross a barrier it does not have the energy for, because the velocity field is real. The exponentially small amplitude has no fluid counterpart.

**No fluctuations.** The $1/N$ correction is the fluctuation, and the corner is the leading term of the $1/N$ expansion. Correlations, variance, and every stochastic effect are in the next order, which is a different corner.

## The Error Bar, Stated

**Two coordinates, and one of them is not small in this theory.**

| Source | Size | Note |
|---|---|---|
| the gradient expansion | $(\ell/L)^2$ | small for a slowly varying density, and controllable |
| the $1/N$ expansion | $1/N=1/3$ for colour | not small, and not improvable by experiment |
| the neglected quantum potential | $\hbar^2\Box\sqrt\rho/(2m^2\sqrt\rho)$ | zero by construction in the corner |

**The honest statement is that $1/N=1/3$ is not a small parameter.** For QED with one species the expansion is in $1$ and there is no $N$; for QCD with three colours the expansion is in $1/3$, and a $30\%$ error is not an error bar but a warning. This is why the large-$N$ corner is used for *structure* — which operators are leading, which are suppressed, why the meson spectrum is narrow — rather than for numbers.

**The corner is exact where the gradient term vanishes.** For a uniform density the quantum potential is zero identically, so the corner is exact for homogeneous systems at any $N$. Its radius is the scale over which the density varies, and its accuracy there is the gradient expansion and nothing else.

## Checks

1. The two coordinates. $1/N\to0$ and the gradient, moved together.
2. The variables. Density, velocity, spin: five per point, against a field's infinity.
3. The continuity equation. Exact, from the imaginary part.
4. The quantum potential. Identified, of order $(\ell/L)^2$, and dropped.
5. Euler. With the enthalpy replacing the mass, and $c_s^2=1/3$ for a relativistic gas.
6. Quantised circulation. $h/m$ about a nodal line, and it survives.
7. The spin transport. BMT with Thomas, agreeing with the adiabatic corner.
8. The failures. No interference, no spectrum, no tunnelling, no fluctuations.
9. The coupling. $1/N=1/3$, and it is not small.
10. The exact case. Uniform density, where the corner is exact.

## Summary

Sending $1/N$ and the gradient to zero turns a quantum field into a fluid with five variables per point: density, velocity and spin. Continuity is exact, Euler follows once the quantum potential is dropped, and the spin is transported by BMT.

The corner keeps the topological quantum of circulation and loses everything spectral: interference, the discrete spectrum, tunnelling and fluctuations. Its gradient error is controllable and its $1/N$ error, at $1/3$ for colour, is not — which is why it is used for structure rather than for numbers.

Its value in this section is as a demonstration that the quantum potential is a single identifiable term, and that dropping it is the whole difference between a wave and a fluid.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho$, $u^\mu$, $s^\mu$ | density, velocity, spin density: the fluid variables |
| quantum potential | $-\hbar^2\Box\sqrt\rho/(2m^2\sqrt\rho)$, the term the corner drops |
| $\ell/L$ | the gradient expansion parameter |
| $N$ | the number of species or colours; $1/N$ is the mean-field parameter |
| Takabayasi equations | continuity, Euler, spin transport, and closure for a spin-½ fluid |

## Further Reading

- [Classical Relativity: The Corner with No Quanta](classical-relativity-the-corner-with-no-quanta.html). The field equation this corner replaces by a fluid.
- [WKB and Eikonal: The Adiabatic Corner](wkb-and-eikonal-the-adiabatic-corner.html). The same transport equation, from a different start.
- [The Reverse Madelung Map](the-reverse-madelung-map-fluid-to-nonlinear-wave.html). The amplitude–phase split in the corpus's variables.
- [The Discipline of a Limit](the-discipline-of-a-limit-truncation-error-bar-arrow-and-check.html). Why $1/N=1/3$ is a warning and not an error bar.
- [The Eight Corners in One Table](the-eight-corners-in-one-table.html). Where this corner sits, and why it is the weakest.
