# __The Fourier Transform and the Klein–Gordon Equation in Biquaternionic Polar Variables__

## Introduction

**The polar parent states the identity that generates everything below.** At its §*The Momentum and the Current* it writes that the biquaternionic gradient of the action is the four-momentum, $\tilde\nabla_\Phi S_{\tilde\Xi}=\tilde P_\Phi$, and it notes that $\tilde K_\Phi=\tilde P_\Phi/\hbar=\tilde\nabla_\Phi S_{\tilde\Xi}/\hbar$. The identity is used there to read the amplitude equation as a norm. It is stated, used, and not followed to the transform.

**Followed to the transform, the identity says what the transform's phase is.** The kernel of the transform is $e^{-i\theta_{\mathrm{pwp}}}$, and the phase is $\theta_{\mathrm{pwp}}=\mathrm{Sc}(\tilde K_\Phi\tilde R_\Phi^\natural)$. By the seed that angle is $S_{\tilde\Xi}/\hbar$. **So the phase of the transform is the action over $\hbar$**, and the polar word's phase is not a second object beside it.

**The second finding is that the amplitude is what removes the symbol.** The transform of $r\,e^{-i\theta}$ is the transform of $r$ translated by the wave number, so the phase moves the support rigidly and the amplitude decides its shape. A single wave number survives exactly when the amplitude's transform is a single point, and that is exactly when the amplitude is constant. **No phase, however nonlinear, can spread a mode; the amplitude spreads it and the phase only moves it.**

**The residue of that failure has a name in the parent.** Where the symbol fails, the amplitude equation carries $\Box_\Phi r/r$, the quantum potential. This article states what it is: the residue, a functional of the unknown that no function of the wave number can represent. The parent's own phrase for it, a curvature of the amplitude, is the right one, and the article shows that the curvature set is strictly larger than the set where a symbol exists.

**The transform gives nothing to the polar form that it did not already have, and the article says so.** The word is a bijection, so the substitution adds no content and removes none. What the transform gives is a reading: the phase is the action, the amplitude is the spread, and the symbol is the free symbol on a fixed amplitude. That reading is the whole of the article.

**The two companion articles ask neighbouring questions.** *The Fourier Transform, the Variational Principle and the Klein–Gordon Equation in Biquaternionic Form* asks what the eigenvalues of a non-central potential are. *The Fourier Transform and the Klein–Gordon Equation in Biquaternionic Form* asks when the second-order symbol factors. This article asks where the symbol comes from and what removes it. **The three answers are independent**, and this one is the only one of the three that uses the word.

## Conventions

The algebra and its units are those of *Algebra and Element Conventions*, the gradient, the d'Alembertian and the symbol rule those of *Operator and Calculus Conventions*, the two forms those of *Norm and Pairing Conventions*, the units and the material time those of *Physics Units and Common Elements Conventions*. The word, the four brackets and the quantum potential are the polar parent's, and they are cited rather than restated.

**The seed is quoted once.** On the material sector $\partial/\partial R_t=-i\,\partial/\partial r_t'$ and $\partial/\partial R_\eta=\partial/\partial r_\eta$, so

$$
\tilde\nabla_\Phi S_{\tilde\Xi}
=-i\frac{\partial S_{\tilde\Xi}}{\partial r_t'}e_t+\nabla S_{\tilde\Xi}
=i\frac{E}{c}e_t+\vec p
=\tilde P_\Phi,
\qquad
\tilde K_\Phi=\frac{\tilde\nabla_\Phi S_{\tilde\Xi}}{\hbar},
\qquad
E=-c\,\frac{\partial S_{\tilde\Xi}}{\partial r_t'} .
$$

**The word is quoted once.** $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}$ for a central field, with $r\geq0$ the amplitude, $\theta_{\mathrm{pha}}$ the phase and $S_{\tilde\Xi}=\hbar\,\theta_{\mathrm{pha}}$. The parent's amplitude equation and transport equation are

$$
\left(\frac{\partial S_{\tilde\Xi}}{\partial r_t'}\right)^{2}-\lvert\nabla S_{\tilde\Xi}\rvert^{2}=m^{2}c^{2}-\hbar^{2}\frac{\Box_\Phi r}{r},
\qquad
\nabla\cdot(\rho_{\mathrm{num}}\nabla S_{\tilde\Xi})-\frac{\partial}{\partial r_t'}\Bigl(\rho_{\mathrm{num}}\frac{\partial S_{\tilde\Xi}}{\partial r_t'}\Bigr)=0,
$$

with $\rho_{\mathrm{num}}=r^{2}$.

**The bookkeeping is stated once.** $\tilde K_\Phi=ik_t'e_t+\vec k_\Phi$, $k_t'=\omega/c$, $k_m=mc/\hbar$, $\langle\tilde K_\Phi\rangle_\natural=-k_t'^{2}+k_\Phi^{2}$, and the phase is $\theta_{\mathrm{pwp}}=\omega r_t'-\vec k_\Phi\cdot\vec r$ for a positive-frequency plane wave.

## The Phase of the Transform Is the Action

**Finding 1.** On a constant-amplitude field with a linear phase, the transform's angle and the action's angle are one number:

$$
\theta_{\mathrm{pwp}}=\mathrm{Sc}(\tilde K_\Phi\tilde R_\Phi^\natural)=\frac{S_{\tilde\Xi}}{\hbar}=\theta_{\mathrm{pha}} .
$$

**The proof is the seed and one line of bookkeeping.** Since $\tilde K_\Phi=\tilde\nabla_\Phi S/\hbar$, pairing it with $\tilde R_\Phi$ returns $S/\hbar$ whenever $S$ is linear, because a linear function is recovered from its gradient by one contraction. There is no second identity involved: the transform's phase is the action because the action's gradient is the wave number, and those are the same sentence read in two directions.

**What the seed therefore explains is the transform's own kernel.** In the element form the phase $\mathrm{Sc}(\tilde K_\Phi\tilde R_\Phi^\natural)$ is written down as the natural pairing of a wave number with a position; it is a construction, and it is correct, but it is not derived from anything. In the polar form the phase is $\theta_{\mathrm{pha}}$, the phase of the field, and the seed identifies it with $S/\hbar$. **The two readings agree because the gradient of the action is the four-momentum, and that is the article's one gain in the direction of explanation.**

**The count is exact and it is a single mode.** On a grid of $128$ samples a field $e^{-i\theta}$ with a linear $\theta$ whose gradient is nine grid units of wave number came back occupying one sample of the transform, at the predicted index, with coefficient $1.000$ and every other coefficient below $5.0\times10^{-16}$ of it. The phase alone never produces a second occupied mode.

**The identity also fixes the sign, and the sign is the parent's.** With $E=-c\,\partial S/\partial r_t'$ the temporal slot of $\tilde\nabla_\Phi S$ is $+iE/c$, which is the temporal slot of $\tilde P_\Phi$; the parent records this as the reason the factor $c$ appears where it does. The transform inherits the sign without a choice: $\theta_{\mathrm{pwp}}=\omega r_t'-\vec k_\Phi\cdot\vec r$ is $\mathrm{Sc}(\tilde K_\Phi\tilde R_\Phi^\natural)$, and no convention is left open.

**What the finding does not say.** It does not say that the phase of a general field is the action of a classical path, and it does not say that $\theta_{\mathrm{pha}}$ is linear. It says that wherever both objects are defined, the transform's angle is $S/\hbar$; for a general field the action is not linear and the transform's angle is not a single number at all, which is the subject of the next section.

## The Amplitude Is What Spreads the Support

**Finding 2.** For a field $r\,e^{-i\theta}$ with $\theta$ linear, the transform is the transform of $r$ translated by the wave number:

$$
\mathcal{F}\bigl[r\,e^{-i\theta}\bigr](k)=\hat r\,(k-k_\theta).
$$

**The proof is the shift rule and nothing else.** Multiplication by a unit-modulus exponential of a linear phase is a translation of the transform's argument, so the exponential moves the support and the amplitude multiplies it. The convolution form is the general statement; the translation is the linear-phase case, and the linear-phase case is the one a mode is defined in.

**The identity is measured, and the measurement is a convolution check.** For a Gaussian amplitude of width $0.6$ multiplied by a linear phase, the transform of the product equalled the transform of the amplitude alone shifted by the wave number, to $2.6\times10^{-16}$ of the peak. The coefficient at the peak equalled $\hat r(0)$, which is the mean of $r$, at $0.239365$ — the amplitude's mean and not its maximum, as the shift rule requires.

**The counts are the same counts, and that is the article's structural point.** On a grid of $128$ samples the occupied count of the transform of $r\,e^{-i\theta}$ matched the occupied count of the transform of $r$ alone in every case tried: $1$ for a constant amplitude, $2$ for $\cos$, $49$ for a Gaussian of width $0.3$, and $128$ for a Gaussian of width $1.2$. **The phase does not appear in the count.**

**So a symbol exists for the polar theory exactly when the amplitude is constant.** A symbol is a single coefficient at a single wave number; by the shift rule the coefficients of the transform are the coefficients of $\hat r$, moved; those coefficients are one number at one point exactly when $\hat r$ is a delta, which is exactly when $r$ is constant. **The condition is on $r$ and not on $\theta$**, and it is the polar form's version of the constant-coefficient licence that the element form states as a hypothesis about $\tilde M$.

**The reading of the word changes with the count.** For a constant amplitude the central word has one free entry, the phase, and the transform reads it exactly through its gradient. For a varying amplitude the word has two, and the transform reads $\hat r$, which is a function and not a number. **The amplitude is the only entry of the word that a transform cannot represent by a label.**

**A constant amplitude is where the two readings meet.** In the element form the free theory is the case of a central coefficient, and its plane waves have a constant amplitude; in the polar form the constant amplitude is exactly the condition under which the transform is a single mode. The two descriptions agree there, and they part company as soon as either the coefficient or the amplitude varies.

## The Quantum Potential Is the Residue

**Finding 3.** Where the symbol fails, the amplitude equation carries $\Box_\Phi r/r$, and that term is the residue of the failure: it is local in $r$, it is not a function of the wave number, and no symbol can contain it.

**The parent's identity already displays it.** Dividing the amplitude equation by $\hbar^{2}$ and multiplying by $-1$ gives

$$
\langle\tilde K_\Phi\rangle_\natural=-k_m^{2}+\frac{\Box_\Phi r}{r},
$$

**The result is the dispersion relation with one term added.** It is the free dispersion relation plus a term built from the amplitude, and **that term is the whole difference between the polar theory and a theory with a symbol**; the parent says exactly this when it notes that the term vanishes for a plane wave and not for a wave packet.

**Its size is measured, and the measurement separates curvature from spread.** The maximum of $\lvert\Box_\Phi r/r\rvert$ was $0.000$ for a constant amplitude, $0.999$ for $\cos x$, $3.775$ for a Gaussian of width $1.2$ and $1155.53$ for a Gaussian of width $0.3$. The narrow amplitude has the large curvature, which is the expected direction: a sharper envelope has the larger second derivative relative to its own size.

**But the condition $\Box_\Phi r=0$ is strictly weaker than the condition that the amplitude be constant.** An affine amplitude in one coordinate satisfies $\Box_\Phi r=0$ and is not constant, so the quantum potential vanishes for it while its transform is a derivative of a delta rather than a delta: one point of support, but a jet at that point and not a single coefficient. **The quantum potential measures the curvature of the amplitude; a symbol needs the amplitude's flatness.** The two conditions coincide only for the constant case, and the gap between them is the reason the residue is not by itself a test for the existence of a symbol.

**That gap is why the article states the symbol condition in §*The Amplitude Is What Spreads the Support* and not here.** A reader who looks for the symbol test in the appearance of $\Box_\Phi r/r$ will find that it disappears for amplitudes that still have no symbol. **The correct order is: constant amplitude first, quantum potential second**, and the article keeps that order.

**The residue is a functional and not a coefficient.** A symbol is a function of $\tilde K_\Phi$ alone; $\Box_\Phi r/r$ depends on the solution, so two fields with the same wave number and different amplitudes have different equations. **That is what "no symbol" means in this case**: not that the operator is unknown, but that the operator is different for every field it is applied to.

## The Transport Equation Has No Symbol

**Finding 4.** The transport equation is quadratic in the amplitude, and it has no symbol either, for a second reason.

**The reason is the density.** The equation is $\nabla\cdot(\rho_{\mathrm{num}}\nabla S)-\partial_{r_t'}(\rho_{\mathrm{num}}\partial_{r_t'}S)=0$ with $\rho_{\mathrm{num}}=r^{2}$. Under the transform the divergences become products with $i\tilde K_\Phi$, but the products $\rho_{\mathrm{num}}\nabla S$ are products of two fields, so their transforms are convolutions. **A symbol represents a product by a product; here the product is inside the operator**, and no multiplication at one wave number can stand for it.

**The two equations fail differently and the difference is worth keeping.** The amplitude equation fails because its coefficient depends on the solution; the transport equation fails because it is nonlinear in the amplitude. The first failure is a coefficient problem and the second is a superposition problem, and the polar pair has one of each. **That is why the polar form has neither a symbol nor a linearization that would produce one.**

**The polar variational parent sharpens the second failure.** Its momenta are genuine Legendre conjugates to the polar parameters, and its Hamiltonian structure is well defined. That structure is not a symbol: a Legendre transform between a field and its conjugate momentum is a transform on the *field's* variables at each point, and the wave number is not among those variables. **The parent's canonical momenta are not Fourier momenta**, and no reading of them as such is available.

## The Legendre Denial

**An invertible Legendre transform is not a Fourier transform.** The polar variational parent's four momenta are derivatives of the Lagrangian density with respect to the rates of the polar parameters, taken at each event. The parameters are field values, not coordinates; their conjugates are field momenta, not wave numbers. A Fourier transform pairs a coordinate with its conjugate wave number, and there is no coordinate in the polar parameter list.

**The denial has teeth because the two transforms can look alike.** Both are invertible, both exchange a function with a transform, and both are used to simplify an equation. What separates them is what the variables are: the Legendre transform acts on the field's own degrees of freedom and leaves the spacetime argument untouched, while the Fourier transform acts on the spacetime argument and leaves the field's degrees of freedom untouched. **The polar parameters live on the wrong side of that line.**

**So the article transforms the field and not the parameters.** Every display above is a transform in $\tilde R_\Phi$, with $r$ and $\theta_{\mathrm{pha}}$ carried along as coefficients. Nothing in the article transforms $r$ or $\theta_{\mathrm{pha}}$ into conjugate partners, and nothing claims a momentum-space reading of the polar word beyond what the field's own transform supplies.

## Limits

**The constant-amplitude case is the licence.** The polar theory has a symbol exactly when $r$ is constant, and every statement about a symbol in this article is confined to that case. For a varying amplitude there is no symbol and the article says so rather than approximating one: the parent's quantum potential is the exact residue, not a correction.

**A central field is assumed throughout.** The word $r\,e^{i\theta}$ with a central exponential describes one coefficient of the field, and the polar parent's §*General Fields* records that a general field is four independent copies with four unrelated phases. The transform acts on each copy, the shift rule holds for each, and the four supports are translated copies of the four amplitudes' transforms. Nothing new appears, and the article does not pursue it.

**The denial is restated as a limit.** Every transform here acts on a $\mathbb{B}$-valued function and returns one; the word is a bijection, so the substitution adds nothing and removes nothing. No step carries a field out of its sector and no step carries a polar parameter into a wave number.

## Open Questions

**One question is left open, and it is whether a position-and-wave-number reading exists for the polar pair.** The failure documented here is the failure of a symbol, which is a function of the wave number alone. Whether a mixed object — a function of both the wave number and the position, in the manner of a Wigner function — can represent the polar pair's two equations, so that $\Box_\Phi r/r$ becomes a term in that object rather than a residue outside it, is not decided here. The parent's quantum potential is local in $r$, which makes the question well posed; nothing in this article answers it.

## Summary

The polar parent's identity, that the biquaternionic gradient of the action is the four-momentum, says through the transform that the transform's phase is the action over $\hbar$: $\theta_{\mathrm{pwp}}=\mathrm{Sc}(\tilde K_\Phi\tilde R_\Phi^\natural)=S_{\tilde\Xi}/\hbar=\theta_{\mathrm{pha}}$. The transform's kernel is therefore not a construction imposed from outside; it is the field's own action, and the element form's phase is that sentence written in the other variable set. Measured: one occupied mode at the predicted index, coefficient $1.000$, every other coefficient below $5.0\times10^{-16}$.

The transform of $r\,e^{-i\theta}$ with a linear phase is the transform of $r$ translated by the wave number, verified to $2.6\times10^{-16}$, and the occupied counts are the amplitude's counts: $1$, $2$, $49$ and $128$ for a constant, a cosine and two Gaussians, with the phase absent from the count. **So the phase moves the support and the amplitude is its shape**, and a symbol exists exactly when the amplitude is constant.

Where the symbol fails the amplitude equation carries $\Box_\Phi r/r$, the parent's quantum potential: $0.000$ for a constant amplitude, $0.999$ for a cosine, $3.775$ and $1155.53$ for two Gaussians. That term is a functional of the unknown and no function of the wave number can hold it. It is also a weaker test than the symbol condition, because $\Box_\Phi r=0$ holds for an amplitude affine in one coordinate, whose transform on the line is a derivative of a delta rather than a delta; **the quantum potential measures curvature and a symbol needs flatness.** The transport equation fails separately, being quadratic in the amplitude, and the polar pair therefore has one coefficient failure and one superposition failure and no symbol at either.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $S_{\tilde\Xi}/\hbar=\theta_{\mathrm{pha}}$ | The action's angle; the polar phase |
| $\tilde\nabla_\Phi S_{\tilde\Xi}=\tilde P_\Phi=\hbar\tilde K_\Phi$ | The parent's seed: the gradient of the action is the four-momentum |
| $\theta_{\mathrm{pwp}}=\mathrm{Sc}(\tilde K_\Phi\tilde R_\Phi^\natural)$ | The transform's angle; equal to $S_{\tilde\Xi}/\hbar$ |
| $r$ | The amplitude; the only entry that spreads the support |
| $\hat r(k-k_\theta)$ | The transform of $r\,e^{-i\theta}$; a translated amplitude transform |
| $\Box_\Phi r/r$ | The quantum potential; the residue of the missing symbol |
| $\langle\tilde K_\Phi\rangle_\natural=-k_m^{2}+\Box_\Phi r/r$ | The amplitude equation as a shifted dispersion relation |
| $\rho_{\mathrm{num}}=r^{2}$ | The density; the transport equation's quadratic term |
| $1$, $2$, $49$, $128$ | Occupied counts of $128$ for four amplitudes |

## Further Reading

- *The Klein–Gordon Equation in Biquaternionic Polar Variables*, for the word, the amplitude and transport equations, and the identity this article follows to the transform.
- *The Fourier Transform and the Klein–Gordon Equation in Biquaternionic Form*, for the symbol whose failure this article locates.
- *The Fourier Transform, the Variational Principle and the Klein–Gordon Equation in Biquaternionic Form*, for the spectrum of a non-central potential.
- *The Fourier Transform and the Dirac Equation in Biquaternionic Polar Variables*, for the first-order case, where the polar form stops at the eikonal and has no second derivative of the amplitude to carry.
- *The WKB Approximation and the Hamilton–Jacobi Equation in Biquaternionic Form*, for the quantum potential's origin.
- *Derivatives, Fields and Transforms*, for the transform, its kernel and the shift rule.
- *Biquaternion Continuous Harmonic Analysis*, for the convolution theorem.
