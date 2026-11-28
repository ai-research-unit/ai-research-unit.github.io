# __Classical Non-Relativistic: $\hbar\to0$ First, Then $v/c\to0$__

## Introduction

**The claim.** Move two coordinates, and move them in this order: $\hbar\to0$ first, then $v/c\to0$. The result is Newtonian mechanics with a spin, and the spin–orbit coupling that appears has a coefficient of one half of the value a naive substitution gives. That half is the Thomas factor, and it exists in this order because the spin was still relativistic when the frame started to be non-relativistic.

**The answer.**

$$
\boxed{\;\hbar\to0\ \text{then}\ v/c\to0:\qquad H=\frac{p^2}{2m}+V+\underbrace{\frac{1}{2m^2c^2}\frac{1}{r}\frac{dV}{dr}\,\mathbf L\cdot\mathbf S}_{\text{one half of the naive coefficient}}+\cdots\;}
$$

**Why the order is the content.** The reversed order — $v/c\to0$ first, then $\hbar\to0$ — gives a Galilean spin that does not precess and a spin–orbit coefficient with no factor of one half in it. Both orders are legitimate limits of the same Lagrangian; they are limits of different sequences, and the difference between them is a physical term rather than a remainder. [The Approximation Lattice](the-approximation-lattice-six-coordinates-eight-corners-and-why-the-limits-do-not-commute.html) calls this the section's exact demonstration, and this article is where it is worked.

## The Arrow

**Step one: $\hbar\to0$, which was [the previous article](classical-relativity-the-corner-with-no-quanta.html).** The fermion is a classical spinning particle: a trajectory $x^\mu(\tau)$, a four-velocity $u^\mu$, a spin four-vector $s^\mu$ with $s\cdot u=0$, and the BMT equation for the precession. The gauge fields are classical, and the scalar is a classical background. Nothing quantum remains, and in particular the spin is a *vector* and not an operator.

**Step two: $v/c\to0$.** Expand the BMT equation in powers of $v/c$, keeping the leading correction. The precession rate splits into two pieces with different origins:

| Piece | Origin | Size |
|---|---|---|
| Larmor precession | the magnetic field in the particle's rest frame | $\mathcal{O}(v/c)$ |
| Thomas precession | the rotation of the comoving frame, i.e. the Wigner rotation | $\mathcal{O}(v^2/c^2)$, opposite sign |

**The sum is the spin–orbit term with the factor one half.** For a central potential the two contributions give $\boldsymbol\omega_{\mathrm L}=\tfrac{1}{2m^2c^2}\frac{1}{r}\frac{dV}{dr}\mathbf L$ and $\boldsymbol\omega_{\mathrm T}=-\tfrac{1}{2}\boldsymbol\omega_{\mathrm L}$, so the net coefficient is one half of the Larmor value. In the atom this is the spin–orbit coupling, and in a storage ring it is the dominant precession of a stored polarised beam.

**Where a naive calculation goes wrong.** A scalar's orbital angular momentum in a central field precesses at the Larmor rate, and the temptation is to treat the spin as a small vector carried along by that precession. The temptation omits the fact that the frame in which the spin is defined is itself rotating as the particle turns, and that rotation is the Thomas term. A calculation that starts from a Galilean spin has no frame to rotate and gets the coefficient wrong by a factor of two, which is the size of the effect being computed.

## The Two Readings of the Same Expansion

**The expansion is shared; what differs is whether the phase is a variable or an operator.**

**Read as classical mechanics.** The result is a Kepler problem with a spin: the orbit is an ellipse, the spin precesses about the orbital angular momentum, and the precession rate contains the Thomas term. The observable is the polarisation of a stored beam, and [Thomas Precession as a Biquaternion Rotor Effect](thomas-precession-as-a-biquaternion-rotor-effect.html) computes it in the corpus's variables.

**Read as quantum mechanics.** Re-quantise the same expanded Hamiltonian and the result is the Pauli equation with its relativistic corrections: the spin–orbit term just derived, the Darwin term from the non-relativistic reduction of the Dirac equation, and the relativistic kinetic correction $-\mathbf p^4/8m^3c^2$. The three together give the fine structure of hydrogen, and [Exercise: The Non-Relativistic Limit and the Pauli Equation](exercise-the-non-relativistic-limit-and-the-pauli-equation.html) carries the algebra.

**The two readings agree because the half is kinematic.** It comes from the Lorentz group and not from the quantisation, so it is the same number whether the spin is a classical vector or a Pauli matrix. That is why the factor is quoted as a property of the corner rather than of the representation.

## What the Corner Reproduces

**Four results, and the third is the one that validates the order.**

**The Bohr spectrum.** The leading non-relativistic Hamiltonian is $p^2/2m-e^2/4\pi r$, and its spectrum is $E_n=-13.6\ \mathrm{eV}/n^2$. The corner contains this as its zeroth order, and reproducing it is a check on the potential and not on the expansion.

**The fine structure, in its $j$-dependent part.** Expanding the exact Dirac spectrum in $(Z\alpha)^2$ gives levels depending on $j$ and not on $\ell$, and the expansion of the corner reproduces that dependence, including the correct coefficient of the spin–orbit term. The check is genuine because the exact Dirac spectrum is known independently and its expansion is not how the corner was built.

**The Thomas factor, from a measurement.** The precession of a polarised muon beam in a storage ring is measured to high precision, and the rate contains the Thomas term with the factor one half. A corner that produced the Larmor value alone would disagree with the measurement by the size of the Thomas term.

**The classical limit of the orbit.** For $\mathbf S\to0$ the corner reduces to the Kepler problem, and its perihelion advance is zero — correctly, because the relativistic precession of the *orbit* is a different term of order $(Z\alpha)^2$ that this corner keeps only partially.

## What the Corner Cannot Reproduce

**Three failures, and the first is why the fine structure is called partial.**

**The Lamb shift is absent, and absent at every order.** The corner keeps the Dirac degeneracy of $2s_{1/2}$ and $2p_{1/2}$, because the degeneracy is a property of the exact relativistic one-particle spectrum and the expansion preserves it. The measured splitting is $1057.845\ \mathrm{MHz}$, it is a loop effect, and the corner has set $\hbar\to0$. No rearrangement of the corner's series produces it: the failure is structural, which is exactly the statement [The Discipline of a Limit](the-discipline-of-a-limit-truncation-error-bar-arrow-and-check.html) requires.

**The anomalous moment does not enter, so the fine structure is off by a computable amount.** Since $g=2$ exactly here, the spin–orbit and spin–spin terms that involve $g$ are off by a relative $\alpha/2\pi\approx1.2\times10^{-3}$ of their own size. The fine structure is a $(Z\alpha)^2$ effect, so the correction is $(Z\alpha)^2\alpha/2\pi$, which is $6\times10^{-8}$ in hydrogen — below the current precision of the Lamb shift but not below the precision of the $2s$–$2p$ measurement in muonic hydrogen.

**The hyperfine structure is present only in its leading form.** The magnetic dipole–dipole interaction between the electron and the proton spin is in the corner, but the proton's own structure enters as a form factor and a Zemach radius, both of which are matching coefficients from a lower-energy corner rather than objects this one computes. The $1420\ \mathrm{MHz}$ line is reproduced to the accuracy of the proton's magnetic radius, and not better.

## The Error Bar, Stated

**Three coordinates contribute, and the largest is not the one being discussed.**

| Source | Size in hydrogen | Note |
|---|---|---|
| the non-relativistic expansion at $\mathcal{O}(v^2/c^2)$ | $5.3\times10^{-5}$ | the coordinate of this corner |
| the next order, $\mathcal{O}(v^4/c^4)$ | $2.8\times10^{-9}$ | the first neglected term of the same series |
| the loop, absent by construction | $1.2\times10^{-3}$ | larger than both, and not in the series |

**The table is the article's most important statement.** A reader who takes this corner's fine structure as "hydrogen to $10^{-5}$" has quoted the smallest of the three numbers. The corner is a fine-structure calculation at $10^{-5}$ *of the fine structure*, and the loop correction it omits is a hundred times larger than the term it keeps beyond leading order.

## Checks

1. The order. $\hbar\to0$ first, then $v/c\to0$, stated explicitly.
2. The two precessions. Larmor and Thomas, opposite in sign, and the sum is one half the Larmor rate.
3. The factor. One half, kinematic, from the Wigner rotation of the comoving frame.
4. The naive error. A Galilean spin gives twice the measured coefficient.
5. The Bohr spectrum. $13.6\ \mathrm{eV}/n^2$, as the corner's zeroth order.
6. The Dirac check. The $(Z\alpha)^2$ expansion of the exact spectrum reproduces the $j$-dependence.
7. The measurement. Storage-ring precession contains the Thomas term.
8. The Lamb shift. Absent at every order, because it is a loop.
9. The anomalous moment. Absent, so the fine structure is off by $(Z\alpha)^2\alpha/2\pi$.
10. The budget. $10^{-5}$ relativistic, $10^{-3}$ loop, and the loop dominates.

## Summary

Moving $\hbar$ and then $v/c$ gives a classical non-relativistic theory with a spin whose spin–orbit coupling is one half of the naive value. The half is the Thomas term, and it exists in this order because the spin was relativistic before the frame became non-relativistic; taking the velocity limit first destroys it.

The corner reproduces the Bohr spectrum, the $j$-dependent fine structure, the measured precession rate, and the Kepler limit. It cannot produce the Lamb shift at any order, it has $g=2$ and therefore a fine structure off by a relative $\alpha/2\pi$, and it has only the leading hyperfine interaction.

Its error is $10^{-5}$ from the coordinate it moves, $10^{-9}$ from the next order of the same series, and $1.2\times10^{-3}$ from the loop it has set to zero. The last of the three is the one that decides whether the corner is adequate, and it is the reason the next corner keeps the loop and drops the antiparticle instead.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| Thomas precession | the precession of the comoving frame, $-\tfrac12$ of the Larmor rate |
| Larmor precession | the precession due to the rest-frame magnetic field |
| $\mathbf L\cdot\mathbf S$ | the spin–orbit operator whose coefficient carries the factor $\tfrac12$ |
| partial fine structure | the $j$-dependence reproduced, the Lamb splitting absent |

## Further Reading

- [Classical Relativity: The Corner with No Quanta](classical-relativity-the-corner-with-no-quanta.html). Step one of this arrow.
- [Quantum Non-Relativistic: $v/c\to0$ Alone](quantum-non-relativistic-velocity-alone-and-the-terms-that-survive.html). The other order, which keeps the loop.
- [Thomas Precession as a Biquaternion Rotor Effect](thomas-precession-as-a-biquaternion-rotor-effect.html). The half, computed.
- [Exercise: The Thomas Precession](exercise-the-thomas-precession.html). The same result as an exercise.
- [The Non-Relativistic Limit of Relativistic Mechanics](the-non-relativistic-limit-of-relativistic-mechanics-in-biquaternionic-form.html). The classical reading, in the corpus's variables.
