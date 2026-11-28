# __WKB and Eikonal: The Adiabatic Corner and the Spin That Precesses__

## Introduction

**The claim.** Move two coordinates at once — the loop order and the adiabatic ratio, meaning that the action varies rapidly compared with the wavelength — and the wave equation becomes a phase carried along a trajectory. The result is the WKB approximation in bound systems and the eikonal approximation in scattering: one phase, one trajectory, one spin that precesses. What survives is interference between nearby paths; what dies is the wave-optical correction.

**The answer.**

$$
\boxed{\;\psi\sim\frac{1}{\sqrt{|\mathbf p|}}\exp\!\Bigl(\frac{i}{\hbar}\int\mathbf p\cdot d\mathbf x\Bigr),\qquad \dot{\mathbf p}=-\nabla V,\qquad \frac{ds^\mu}{d\tau}=\text{BMT}\;}
$$

**Why this corner is separate from case 2.** [Classical Relativity](classical-relativity-the-corner-with-no-quanta.html) sends $\hbar\to0$ and says nothing about how fast the action varies; the result is the exact classical field equation. Here the further statement that $\partial S$ is large selects the *stationary phase* of the path integral, and that selection produces a trajectory rather than a field. The two moves are different: one removes the loop, the other removes all but one path.

## The Arrow

**An ansatz, substituted into the wave equation, with the orders in $\hbar$ collected.**

**Step one: the phase.** Write $\psi=A\,e^{iS/\hbar}$ with $A$ slowly varying, substitute into the Klein–Gordon or Schrödinger equation, and collect powers of $\hbar$. At order $\hbar^0$ the phase satisfies $(\partial S)^2=m^2$, which is Hamilton–Jacobi. At order $\hbar^1$ the amplitude satisfies the transport equation $\partial_\mu(A^2\partial^\mu S)=0$, which is conservation of the current along the flow. The two together are the corner.

**Step two: the spin.** The spin does not enter the phase; it enters the transport. The spin vector is parallel-transported along the trajectory and precesses by the BMT equation, so the corner carries both the orbital phase and the spin precession, computed from the same trajectory.

**Step three: the same expansion in scattering form.** For a fast particle crossing a potential, the phase is $\exp(-i\int V\,dz/\hbar v)$ along a straight line, and the amplitude is the Fourier transform of $e^{i\chi(\mathbf b)}-1$ in the impact parameter $\mathbf b$. That is stationary phase applied to the path integral, with the trajectory frozen while the phase accumulates.

**The two names are one expansion.** WKB is the bound-state version, with the trajectory closed and the phase quantised; eikonal is the scattering version, with the trajectory open and the phase integrated. The adiabatic ratio is the same in both: the potential must vary slowly over a wavelength.

## What the Corner Reproduces

**Four results, and the second is the one that makes it legitimate.**

**Bohr–Sommerfeld quantisation.** $\oint p\,dq=2\pi\hbar\,(n+\tfrac12)$ reproduces the Coulomb spectrum exactly, including the Rydberg constant, and the harmonic oscillator exactly. These are the two cases where the WKB series terminates, which is why they are exact and not merely accurate.

**The Born amplitude, from the eikonal phase.** Expanding $e^{i\chi}-1$ in $\chi$ and Fourier transforming gives the first Born approximation. The corner contains perturbation theory as its weak-potential limit, and that is a genuine check: the eikonal is derived without Feynman diagrams and must agree with them.

**Spin precession in a storage ring.** The BMT equation along a circular trajectory gives a precession rate proportional to $a=(g-2)/2$ plus the Thomas term, and this is the operating principle of the muon $g-2$ experiment and of every polarised-beam measurement. The corner is not an approximation to that experiment; it is the description of it.

**The Airy connection at a turning point.** Where $p$ vanishes the WKB solution is replaced by an Airy function, and the connection formulas supply the correct phase shift — the $\tfrac12$ in Bohr–Sommerfeld, and the Stokes phenomenon at a caustic.

## What the Corner Cannot Reproduce

**Four failures, and the first two define the corner rather than limiting it.**

**No tunnelling.** A forbidden region requires a complex action, and the transmitted amplitude is $e^{-2\,\mathrm{Im}\,S/\hbar}$ — exponentially small in $\hbar$ and therefore invisible in the asymptotic series. The corner can be *extended* to produce the exponential, but the extension is a different, non-perturbative statement.

**No interference between non-stationary paths.** Stationary phase keeps the paths whose action is stationary and discards the rest. Two slits give two stationary paths and the corner keeps their interference — but any path whose action differs from the stationary one by more than $\hbar$ is discarded, and with it every diffraction correction.

**No exact spectrum beyond two cases.** The WKB series is asymptotic: exact for Coulomb and oscillator, approximate for everything else, and divergent if pushed. The anharmonic oscillator is reproduced to the correct order in the expansion and not beyond.

**No caustics without repair.** At a turning point the amplitude diverges, and the repair is a local Airy analysis. Where several caustics meet the repair needs a higher special function, and until one is supplied the corner is silent.

## The Error Bar, Stated

**The neglected term has a name: the curvature of the action relative to its gradient.**

**The dimensionless quantity.** The expansion is in $\lambda|\partial^2S|/|\partial S|^2$ — the de Broglie wavelength against the scale over which the potential varies. Call it $\epsilon$. For a hydrogenic orbit $\epsilon\sim Z\alpha$, so the corner is good to $10^{-2}$ in hydrogen and to $10^{-3}$ in heavier atoms: worse than the non-relativistic corner, which is why the two are used for different problems.

**The Fresnel zone.** The discarded paths are those outside a tube of width $\sqrt{\lambda L}$ around the classical trajectory, and the correction is the ratio of that width to the transverse scale of the potential. In the eikonal this is the statement that the straight-line approximation holds when the deflection is small against the momentum over the transverse scale.

**Where the corner is exact.** The linear potential after the Airy connection, the Coulomb problem, and the oscillator. These are the corner's exact islands, and a user should know that they are islands.

## Checks

1. The two coordinates. The loop order and the adiabatic ratio, moved together.
2. The ansatz. Amplitude times phase, phase at $\mathcal{O}(\hbar^0)$ and amplitude at $\mathcal{O}(\hbar^1)$.
3. The transport equation. Conservation of the current along the flow.
4. The spin. Parallel transport plus BMT, on the same trajectory.
5. The two names. WKB closed, eikonal open, and one expansion behind both.
6. The exact cases. Coulomb and oscillator, where the series terminates.
7. The Born limit. Expanding the eikonal phase in $\chi$ returns the first Born amplitude.
8. The measurement. Storage-ring precession is described, not approximated, by the corner.
9. The failure. Tunnelling lies beyond all orders.
10. The error. $\epsilon\sim Z\alpha$ in hydrogen, and the Fresnel zone in scattering.

## Summary

Sending the loop order and the adiabatic ratio to zero together turns the wave equation into a phase carried along a trajectory, with the amplitude transported by the current and the spin precessed by BMT. The corner is the stationary-phase approximation, written once and used twice: WKB for bound states, eikonal for scattering.

It reproduces Bohr–Sommerfeld quantisation in its two exact cases, the Born amplitude in the weak-potential limit, the equations that operate every storage-ring spin measurement, and the Airy connection at a turning point. It loses tunnelling, which is beyond all orders, every non-stationary path, and every wave-optical correction.

Its error is the curvature of the action relative to its gradient, of order $Z\alpha$ in hydrogen. That makes it the least accurate of the semiclassical corners and the only one that describes a spin-precession experiment directly.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S$ | the action, as a function on configuration space |
| adiabatic ratio | $\lambda|\partial^2S|/|\partial S|^2$, the expansion parameter of the corner |
| eikonal phase $\chi(\mathbf b)$ | the accumulated phase at impact parameter $\mathbf b$ |
| Fresnel zone | the tube around the classical path that the corner retains |
| caustic | a surface where the amplitude diverges and the corner needs repair |

## Further Reading

- [Classical Relativity: The Corner with No Quanta](classical-relativity-the-corner-with-no-quanta.html). The exact classical limit that this corner approximates by one path.
- [Classical Non-Relativistic: $\hbar\to0$ First, Then $v/c\to0$](classical-non-relativistic-planck-first-then-velocity.html). The other corner where the Thomas term appears.
- [The Discipline of a Limit](the-discipline-of-a-limit-truncation-error-bar-arrow-and-check.html). The four requirements, applied here to an asymptotic series.
- [Thomas Precession as a Biquaternion Rotor Effect](thomas-precession-as-a-biquaternion-rotor-effect.html). The spin transport, computed.
- [The Eight Corners in One Table](the-eight-corners-in-one-table.html). Where this corner sits between the exact classical limit and the non-relativistic one.
