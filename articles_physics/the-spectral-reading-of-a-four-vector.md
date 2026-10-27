# __The Spectral Reading of a Four-Vector__

## Introduction

The eigenvalue decomposition of a four-momentum returns two complex numbers. They are not two energies and not two particles. They are the two light-cone frequencies of one momentum, and their product is the mass squared.

The statement is a reading, not a theorem. The spectrum, the eigenprojections and the two-term writing are those of *The Biquaternion Eigenvalue Decomposition*. The material sector and the four-vector dictionary are those of *The Material Sector: Four-Vectors, Interval and Lorentz Action*. This article owns the interpretation: what the pair means, how it transforms, and what it does not mean.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The spectrum, the eigenprojections and the two-term writing | [The Biquaternion Eigenvalue Decomposition](../articles_maths/the-biquaternion-eigenvalue-decomposition.html) |
| The degenerate case and the scalar vertex | [The Spectrum](../articles_maths/spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html) |
| The Hermitian case and the Hermitian idempotents | [The Biquaternion Eigenvalue Decomposition](../articles_maths/the-biquaternion-eigenvalue-decomposition.html) |
| The four-vector dictionary and the interval | [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) |
| The boost spectrum and the Doppler factors | [Frames, Rotations and the Lorentz Group](frames-rotations-and-the-lorentz-group.html) |
| The zero-divisor cone and the massless spectrum | [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html) |

## The Eigenpair

With $\tilde P=i\frac{E}{c}e_t+\vec p$ and $B=\lvert\vec p\rvert$, the two eigenvalues are

$$
\boxed{\;\lambda_\pm=i\left(\frac{E}{c}\pm B\right)
=i\left(\frac{E}{c}\pm\lvert\vec p\rvert\right)\;}.
$$

Write $\nu_\pm=\lambda_\pm/i$. The pair $\nu_\pm$ is real and non-negative,

$$
\nu_\pm=\frac{E}{c}\pm\lvert\vec p\rvert\ge0,
$$

and it is the pair of light-cone frequencies of the momentum. The rapidity $\psi$ of the momentum is fixed by

$$
\cosh\psi=\frac{E}{mc},
\qquad
\sinh\psi=\frac{\lvert\vec p\rvert}{mc},
\qquad
\tanh\psi=\frac{\lvert\vec p\rvert c}{E},
$$

and the pair takes the compact form

$$
\boxed{\;\nu_\pm=mc\,e^{\pm\psi},
\qquad
\lambda_\pm=i\,mc\,e^{\pm\psi}\;}.
$$

This is the **Doppler pair**: the two frequencies are the rest frequency $mc$ scaled by the two reciprocal Doppler factors of the momentum's own rapidity. The sum, the difference, the product and the ratio are the four physical invariants of the pair.

| Quantity | Expression | Reading |
| --- | --- | --- |
| eigenvalues | $\lambda_\pm=i\,mc\,e^{\pm\psi}$ | the two light-cone frequencies, imaginary |
| frequencies | $\nu_\pm=\lambda_\pm/i=mc\,e^{\pm\psi}$ | the Doppler pair |
| sum | $\nu_++\nu_-=2E/c$ | twice the energy |
| difference | $\nu_+-\nu_-=2\lvert\vec p\rvert$ | twice the momentum |
| product | $\nu_+\nu_-=m^2c^2$ | the mass squared |
| norm | $\lambda_+\lambda_-=\langle\tilde P\rangle_{\natural}=-m^2c^2$ | the interval |
| ratio | $\nu_+/\nu_-=e^{2\psi}$ | the squared Doppler factor |

The product is the invariant. It does not depend on the frame and it does not depend on the direction of $\vec p$; it is the mass shell. The two factors separately do depend on the frame, and their dependence is exactly the Doppler rescaling.

## The Two-Term Writing

The eigenprojections are Hermitian idempotents,

$$
\tilde\Pi_\pm=\frac12\left(e_t\mp i\vec u_p\right),
\qquad
\tilde\Pi_\pm^{2}=\tilde\Pi_\pm,
\qquad
\tilde\Pi_\pm^{*}=\tilde\Pi_\pm,
\qquad
\tilde\Pi_++\tilde\Pi_-=e_t,
\qquad
\tilde\Pi_+\tilde\Pi_-=0,
$$

and the decomposition is

$$
\boxed{\;\tilde P=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-
=i\,mc\left(e^{\psi}\tilde\Pi_++e^{-\psi}\tilde\Pi_-\right)\;}.
$$

Each term is a complex multiple of a minimal idempotent, hence a null element. The two terms are the two **lightlike components** of the momentum, and the coefficients are the Doppler-scaled rest frequencies. In light-cone coordinates the writing is the standard split of a timelike vector into two null vectors,

$$
\tilde P=k_++k_-,
\qquad
k_\pm=i\,mc\,e^{\pm\psi}\,\tilde\Pi_\pm,
\qquad
\langle k_\pm\rangle_{\natural}=0.
$$

The decomposition is unique up to the exchange of the two labels. The exchange is produced by $\vec u_p\mapsto-\vec u_p$, that is, by the other square root $B\mapsto-B$, and it leaves $\tilde P$ unchanged. No physical statement may depend on which term is called $+$.

The two idempotents are the pure states along $-\vec u_p$ and $+\vec u_p$ respectively: $\tilde\Pi_+$ has Bloch vector $-\vec u_p$ and $\tilde\Pi_-$ has Bloch vector $+\vec u_p$. The momentum therefore selects an axis, and the two null components are the two states on that axis. The axis is the direction of motion, and the pair of states is the pair of lightlike directions along it.

## Are They Two Particles?

No. The two eigenvalues are the one momentum written in the two idempotent coordinates, and the two terms are two null components of one element.

The sum is the check. The two coefficients satisfy $\nu_++\nu_-=2E/c$, not $E/c$; they are not the energies of two particles whose total is $E$. The two terms are null and complex, so neither is a positive-energy state. The density matrix of a physical particle is a Hermitian positive element of the informational sector, and the $k_\pm$ are not of that kind.

The comparison with a genuine two-particle object makes the difference explicit. A two-particle state is a tensor product or a pair of independent four-momenta; it lives in a larger space and carries two independent mass-shell conditions. The two-term writing lives in one algebra element and carries one mass-shell condition, $\nu_+\nu_-=m^2c^2$. It is a decomposition, not a pair.

The reading is therefore a spectral reading of one four-vector, not a particle count. The algebra supplies the two null directions and the two coefficients; it does not supply a second particle, a second energy, or an antiparticle.

## The Frame Dependence

The pair is frame-dependent and the product is not. Under a boost of rapidity $\xi$ along $\vec u_p$,

$$
\nu_+\longmapsto e^{-\xi}\nu_+,
\qquad
\nu_-\longmapsto e^{+\xi}\nu_-,
\qquad
\nu_+\nu_-\longmapsto\nu_+\nu_-,
$$

which is the Doppler rescaling written on the pair. Under a rotation the frequencies are unchanged and the axis $\vec u_p$ rotates. Under a general boost the new rapidity $\psi'$ is the rapidity of the new momentum, and the pair is $mc\,e^{\pm\psi'}$.

| Change of frame | $\nu_+$ | $\nu_-$ | product |
| --- | --- | --- | --- |
| boost along $\vec p$ by $\xi$ | $e^{-\xi}\nu_+$ | $e^{+\xi}\nu_-$ | unchanged |
| rotation | unchanged | unchanged | unchanged |
| general boost | $mc\,e^{\psi'}$ | $mc\,e^{-\psi'}$ | unchanged |

The transformation law is the reason for the name. The two coefficients are the two Doppler factors, and a boost along the direction of motion multiplies one by $e^{-\xi}$ and the other by $e^{+\xi}$. The product is the mass squared, and it is the invariant of the pair.

### The Rest Frame

At $\vec p=0$ the rapidity vanishes, $\nu_\pm=mc$, and the two eigenvalues coincide at $imc$. The element is the scalar $i\frac{E}{c}e_t$ with $E=mc^2$, so the degeneracy is the diabolic case, the scalar vertex of *The Eigenbasis of a Spectrally Regular Biquaternion*, §*The Boundary*. The two-term writing still holds, but it is not unique: every complementary pair of Hermitian idempotents gives

$$
i\,mc\left(\tilde\Pi_++\tilde\Pi_-\right)=i\,mc\,e_t,
$$

and the pair is not determined by the element. The rest frame is the only frame in which the momentum has no preferred null pair.

### The Massless Limit

At $m=0$ the rapidity diverges and the pair degenerates to

$$
\nu_-=0,
\qquad
\nu_+=\frac{2E}{c},
\qquad
\lambda_-=0,
\qquad
\lambda_+=\frac{2iE}{c}.
$$

The eigenvalues are still distinct, because $B=\lvert\vec p\rvert=E/c\neq0$. The element is a zero divisor with distinct eigenvalues, and the spectral writing survives with one term,

$$
\tilde P=\lambda_+\tilde\Pi_+=2i\frac{E}{c}\tilde\Pi_+.
$$

The one-term writing is the spectral form of a null momentum, and it is the zero-divisor regime of the eigenvalue decomposition, not the exceptional regime. The massless limit of the pair is a limit of the coefficients, not a failure of the decomposition.

## The Hamilton Mass and the Frame

The Hamilton pairing writes the four-momentum as a central modulus times a unit:

$$
\tilde P=\Rho\exp(\vec U\Theta),
\qquad
\Rho=imc,
\qquad
\vec U=\hat p,
\qquad
\Theta=-i\psi .
$$

The expansion checks the identification. With $\vec U^{2}=-e_t$ and $\Theta=-i\psi$,

$$
\Rho e^{\vec U\Theta}
=imc\left(\cosh\psi-i\hat p\sinh\psi\right)
=i\frac{mc^{2}\cosh\psi}{c}+mc\sinh\psi\,\hat p
=i\frac{E}{c}e_t+\vec p .
$$

The three slots divide the data. The modulus $\Rho=imc$ is the mass; the angle $\Theta=-i\psi$ is the rapidity; the axis $\vec U=\hat p$ is the direction of motion. The energy is not a slot: it is $mc^{2}\cosh\psi$, the modulus times the frame factor. A boost changes $\psi$ and leaves $\Rho$ fixed.

The modulus is central, and that is the algebraic reason the mass is frame-independent while the energy is not. A change of frame conjugates the second factor and commutes with the first. The spectrum sees the same division: the product $\lambda_+\lambda_-=\Rho^{2}=-m^{2}c^{2}$ is the modulus, and the ratio $\lambda_+/\lambda_-=e^{2\psi}$ is the frame.

**The boundary.** The reading is licensed for the four-momentum chart and the principal branch. For a general element the Hamilton modulus is a complex amplitude, and calling it a mass is an extra identification. The branch matters: on the other branch the same element is written with $-\Rho$ and $\Theta+\pi$, and the mass is read from $\lvert\Rho\rvert$.

## What the Spectrum Does Not Determine

The spectrum is two complex numbers, and a general element is eight real numbers. The spectrum fixes the trace and the norm,

$$
\lambda_++\lambda_-=2Q_t,
\qquad
\lambda_+\lambda_-=Q_t^{2}+B^{2}=N,
$$

and it fixes nothing else about the direction.

| the spectrum fixes | the spectrum does not fix |
| --- | --- |
| the trace $2Q_t$ | the direction $\vec u_p$ |
| the vector square $B^{2}$ | the two angles of the axis |
| the norm $N$ | the eigenprojections when $\lambda_+=\lambda_-$ |
| the causal class through the sign of $N$ when $N$ is real | whether the vector part is real |

The first row of the second column is the physical statement. A rotation leaves the eigenvalues unchanged and rotates the axis; the spectrum is blind to the two angles of the direction. For a four-momentum the spectrum fixes the energy and the magnitude of the momentum and leaves the direction free. The set of momenta with a given spectrum is the two-sphere of directions at fixed $E$ and $\lvert\vec p\rvert$.

The second row is algebraic. The eigenvalues depend on the vector part only through the complex square $(\vec Q,\vec Q)$. Any $\vec Q\in\mathbb{C}^{3}$ with the same square gives the same spectrum, and a complex vector part with the right square is isospectral with a real one. The reality of $\vec Q$ is the material-sector condition, not a spectral condition; the spectrum cannot tell a four-momentum from a complex element with the same trace and the same vector square.

The third row is the degeneracy. When the eigenvalues coincide, the eigenprojections are not determined: at $\vec p=0$ every axis is an eigenaxis, and the two-term writing is not unique. The spectrum is then a single number repeated, and the frame data is entirely absent from it.

The element is the spectrum plus the eigenprojections,

$$
\tilde P=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-,
$$

and the two objects play different roles. The eigenvalues are the coefficients; the idempotents are the frame. A spectral measurement reads the coefficients and leaves the frame.

**The boundary.** "Not determined" is not "not constrained". The spectrum constrains the element to a quadric, and for a four-momentum it constrains the momentum to a sphere. The claim is that the spectrum is insufficient, not that it is uninformative. It is also not a claim about a measurement: a measurement that resolves the eigenprojections as well is a different measurement, and it reads the frame.

## Physical Readings

- **The eigenpair is the Doppler pair.** The two eigenvalues are the two light-cone frequencies, $mc\,e^{\pm\psi}$, and their ratio is the squared Doppler factor. The reading is the spectral form of the relativistic Doppler effect.
- **The sum and the difference are the energy and the momentum.** Twice the energy and twice the momentum are the symmetric and antisymmetric combinations of the pair. The reading is the light-cone bookkeeping of a four-vector.
- **The product is the mass shell.** The product of the eigenvalues is the norm, and the norm is $-m^2c^2$. The reading is that the mass is the invariant of the pair, not a property of either member.
- **The two terms are the two null components.** Each term is a complex multiple of a minimal idempotent, and the two idempotents are the two pure states along the direction of motion. The reading is the lightlike decomposition of a timelike momentum.
- **The frame dependence is the Doppler shift.** A boost rescales the two coefficients reciprocally. The reading is that the pair is a frame-dependent coordinate of a frame-independent product.
- **The rest frame is the degenerate frame.** At rest the pair coalesces and the two-term writing is not unique. The reading is that a massive particle at rest has no preferred null pair.
- **The massless limit is a one-term writing.** One coefficient vanishes and the element becomes a null multiple of one idempotent. The reading is the massless spectrum as the boundary of the massive pair.

## Limits

The algebra gives the frequencies, not a particle count. The two terms are null components of one element, not two particles, and the sum of the coefficients is twice the energy.

The mass is read from the product, not from either eigenvalue. No numerical mass is derived; the mass is the input that fixes the rapidity through $\cosh\psi=E/(mc)$.

The pair is frame-dependent. Only the product is invariant, and a statement about one member of the pair is a statement about a frame.

The reading needs the material sector. The four-momentum, the real vector part and the imaginary scalar are the data of $\mathbb{M}_-$, and the identification of the element with a physical four-momentum is the interpretive step of *The Material Sector: Four-Vectors, Interval and Lorentz Action*.

The two-term writing is not unique at rest and not two-term in the massless limit. The labels $\pm$ are conventional, and the decomposition is canonical only as an unordered pair.

No dynamics is supplied. The article reads one element at one instant; it does not say how the momentum evolves, and it does not supply a mass spectrum.

## Summary

- The four-momentum $\tilde P=i\frac{E}{c}e_t+\vec p$ has eigenvalues $\lambda_\pm=i(E/c\pm\lvert\vec p\rvert)=i\,mc\,e^{\pm\psi}$.
- The pair $\nu_\pm=mc\,e^{\pm\psi}$ is the Doppler pair; its ratio is $e^{2\psi}$ and its product is $m^2c^2$.
- The norm is $\lambda_+\lambda_-=-m^2c^2$; the mass is read from the product, not from either eigenvalue.
- The eigenprojections are the Hermitian idempotents $\tilde\Pi_\pm=\tfrac12(e_t\mp i\vec u_p)$, the two pure states along the direction of motion.
- The two-term writing is $\tilde P=i\,mc(e^{\psi}\tilde\Pi_++e^{-\psi}\tilde\Pi_-)$; the two terms are the two null components of one momentum.
- The terms are not two particles and not two energies; their sum is twice the energy and their difference is twice the momentum.
- A boost along $\vec p$ rescales the pair reciprocally; the product is invariant. A rotation leaves the pair unchanged and rotates the axis.
- At rest the pair coalesces and the two-term writing is not unique; at $m=0$ one coefficient vanishes and the writing has one term.
- The Hamilton reading is $\tilde P=\Rho e^{\vec U\Theta}$ with $\Rho=imc$, $\Theta=-i\psi$ and $\vec U=\hat p$: the mass is the modulus, the rapidity is the angle and the direction is the axis.
- The spectrum fixes the energy and the magnitude of the momentum, not the direction; it is blind to rotations and to the reality of the vector part, and it leaves the eigenprojections free at a degeneracy.
- The algebra gives the frequencies, not a particle count, a numerical mass, a dynamics or a mass spectrum.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde P=i\frac{E}{c}e_t+\vec p$ | the four-momentum of the material sector |
| $E$, $\vec p$, $m$ | energy, spatial momentum and mass |
| $B=\lvert\vec p\rvert$ | the modulus of the spatial momentum |
| $\vec u_p=\vec p/B$ | the direction of motion, a real unit vector |
| $\psi$ | the rapidity of the momentum, $\cosh\psi=E/(mc)$ |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues, $Q_t=iE/c$ |
| $\nu_\pm=\lambda_\pm/i=mc\,e^{\pm\psi}$ | the Doppler pair |
| $\vec\Xi=-i\vec u_p$ | the pure root of $+1$ of the momentum |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)=\tfrac12(e_t\mp i\vec u_p)$ | the eigenprojections, Hermitian idempotents |
| $\langle\tilde P\rangle_{\natural}=-m^2c^2$ | the biquaternion norm, the interval |
| $k_\pm=i\,mc\,e^{\pm\psi}\tilde\Pi_\pm$ | the two null components of $\tilde P$ |

## Further Reading

- [The Biquaternion Eigenvalue Decomposition](../articles_maths/the-biquaternion-eigenvalue-decomposition.html), for the spectrum and the eigenprojections, and [The Spectrum](../articles_maths/spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html) for the degenerate case.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), for the four-vector dictionary and the mass shell.
- [Frames, Rotations and the Lorentz Group](frames-rotations-and-the-lorentz-group.html), for the boost spectrum and the Doppler factors.
- [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html), for the massless limit and the null stratum.
- [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), for the pure states that the idempotents represent.
- [The Roots of a General Element: Mass, Frames and the Mass Shell](the-roots-of-a-general-element-mass-frames-and-the-mass-shell.html), for the mass shell read as a level set.
- [The Hamilton Pairing: Mass as Modulus and the Complex Angle](the-hamilton-pairing-mass-as-modulus-and-the-complex-angle.html), for the mass as a modulus and the complex angle of the frame.
- [Physical Interpretation of Spectral Regularity and Degeneracy in the Biquaternion Algebra](physical-interpretation-of-spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the general reading of the spectrum and of the degenerate strata.
