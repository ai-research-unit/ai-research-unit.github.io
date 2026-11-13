# __The Fourier Transform and the Dirac Equation in Biquaternionic Polar Variables__

## Introduction

**The word carries four factors; the transform keeps the support, its direction and two signs, and discards the factorization.** *The Dirac Equation in Biquaternionic Polar Variables* writes the field as $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ and proves one identity that this article uses as its starting point: the gradient of the word's angle is the four-momentum, $\tilde\nabla_\Phi\theta_{\mathrm{pha}}=\tilde K_\Phi$. That identity is exactly the statement that the Fourier variable is a coefficient the field already carries.

**So the transform's label is not imported.** For a plane wave the transform is supported on the single wave number equal to the phase gradient, and the amplitude is the mode's own element. The transform adds no data to the mode and removes none. The polar reading and the Fourier reading agree about where the mode sits, and the agreement is an identity rather than a convention.

**The factorization does not survive the transform.** The word is a product of four element-valued functions, and the transform of a product is a convolution, so the four factors do not come apart in momentum space. What the transform leaves is one element-valued density on the shell, its support point, the direction of that point, and two signs. **The polar word is therefore a position-space reading**, and this article says why in the algebra's own terms rather than by appeal to the size of a table.

**There is a second conjugacy in the corpus, and this article does not use it.** The polar variational parent computes the canonical momenta conjugate to the word's parameters and finds four of them vanishing. Those are Legendre momenta; the Fourier variable is not one of them. The distinction is recorded once, in §*Limits*, and it is the article's answer to the natural confusion.

**The denial is stated plainly.** The transform acts on $\mathbb{B}$-valued functions and returns $\mathbb{B}$-valued functions. No sector flip is claimed anywhere below, and no field is said to change its type. **There is no new prediction and no new solution**; the equation, the word and the physics are the parents'.

## Conventions

The algebra, the products, the two forms, the units and the sectors are those of *Algebra and Element Conventions*, *Product and Form Conventions*, *Norm and Pairing Conventions*, *Physics Units and Common Elements Conventions* and *Mirror Biquaternions and the Phy–Psy Switch*. The transform is the one of *Derivatives, Fields and Transforms*, with kernel $\exp(-2\pi\rho\omega r_t'/c)$ and root $\rho=i$ in the corpus, and the symbol rule

$$
\tilde\nabla_\Phi\longmapsto i\tilde K_\Phi ,
\qquad
(\tilde\nabla_\Phi)^{\natural}\longmapsto i\tilde K_\Phi^{\natural},
\qquad
\tilde K_\Phi=ik_t'e_t+\vec k_\Phi ,
\qquad
k_t'=\frac{\omega}{c}.
$$

The word and its parameters are the polar parent's:

$$
\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
\qquad
\tilde U_{\Psi,\mathrm b}=\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr),
\qquad
\tilde u_{\mathrm r}=\exp\Bigl(\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr),
$$

with $r\ge0$ the scale, $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$ the angle, $\theta_{\mathrm{rpd}}\ge0$ the rapidity and $\theta_{\mathrm{axr}}\in[0,2\pi]$ the rotor's angle. The parent's phase-gradient proposition is quoted, not re-proved:

$$
\tilde\nabla_\Phi\theta_{\mathrm{pha}}=\tilde K_\Phi ,
\qquad
\vec p=\hbar\nabla\theta_{\mathrm{pha}},
\qquad
E=-\hbar c\,\frac{\partial\theta_{\mathrm{pha}}}{\partial r_t'} .
$$

## The Phase Gradient Is the Fourier Variable

**The wave number of a mode is the gradient of the mode's own angle.** The parent proves this for any real angle, using only that the angle is real and that the gradient is the algebra's derivative, and it exhibits the match slot by slot: the temporal slot of the gradient is $-i\partial\theta_{\mathrm{pha}}/\partial r_t'$ and the temporal slot of the wave number is $iE/(\hbar c)$, so no factor is inserted by hand. On a plane wave, where the angle is linear, the identity is the statement that the phase's rate is the momentum.

**The transform reads the same coefficient.** Write the field of a single mode as $\tilde\Xi_{0}\exp(-i\theta_{\mathrm{pwp}})$ with $\theta_{\mathrm{pwp}}=\vec k_\Phi\cdot\vec r-k_t'r_t'$. The transform over the position is supported on the single wave number $\tilde K_\Phi$, and the amplitude there is $\tilde\Xi_{0}$ up to the convention's constant. **The label of the transform and the phase gradient of the field are the same element**, and the identity is the parent's.

**The check is exact on a lattice.** Take 64 samples of the mode $\exp(2\pi i\,m\,n/64)$ with $m=5$ and a unitary discrete transform. The transform was supported on the index $5$ with modulus $8.000000000000$, which is $\sqrt{64}$, and the largest of the other 63 coefficients was $1.4\times10^{-14}$. The support point is the phase gradient's value and the amplitude is the mode's unit.

**The identity is not restricted to linear phases; only the point support is.** For a general field the gradient of the angle varies from event to event, and the transform is a superposition over the values it takes. The parent's proof does not use linearity, so the identification of the variable with the phase gradient holds pointwise; what linearity supplies is that the support is one point rather than a distribution. Nothing below needs the general case, and the article does not use the eikonal reading.

**A phase is a translation, and that is the identity in its most useful form.** For a linear angle $\theta$,

$$
\mathcal{F}\bigl[e^{i\theta}f\bigr](\omega)=\hat f\bigl(\omega-\nabla\theta\bigr),
$$

so multiplying by a phase moves the support by the phase gradient and changes nothing else. The check used 64 samples with $m=7$: the two sides agreed to $1.1\times10^{-14}$, and the coefficient that had stood at index $0$ with modulus $0.087043$ stood at index $7$ with the same modulus. **The action's phase becomes a place, and a place carries no phase.** §*The Cross-Check with the Polar Path Integral* is this sentence applied to the kernel.

## The Word Is a Product, the Transform Is a Convolution

**The word is one product of four functions of the position.** The scale, the central phase, the boost and the rotor are each element-valued, and two of them are units. The field is their product and not their sum, and the polar reading depends on that: the four brackets of the parent's logarithmic derivative come from differentiating a product.

**The transform does not respect a product.** For two fields $f$ and $g$,

$$
\mathcal{F}[fg]=\mathcal{F}[f]*\mathcal{F}[g],
$$

the convolution of the two transforms, which is the harmonic analysis article's theorem. The check used 64 samples and two fields with generic complex coefficients: the relative residual was $1.4\times10^{-15}$.

**So no momentum-space function is the scale, the angle, the boost or the rotor.** A convolution is not a factorization. Whatever the transform of $\tilde\Xi$ is, it is not the product of the transforms of its four factors, and the four factors cannot be recovered from it one at a time. **The four factors do not survive the transform as four factors.**

**The failure is symmetric in the four, and that is worth saying.** It would be natural to expect the scale to survive as an envelope and the angle as a phase, because both are scalar-like in the position-space display. Neither does. The transform is linear and the factorization is multiplicative, and linear operations do not see multiplicative structure except through convolution.

## What the Transform Leaves of the Word

**For one mode the momentum-space object is a point and a density.** A free solution is a superposition of modes, each supported on its own $\tilde K_\Phi$; each mode contributes an element $\tilde\Xi_{0}$ at that point. So the transform of a solution is a measure supported on the mass shell with an element-valued density, and the support is the dispersion relation rather than a choice.

**The mode's own word has four factors, and they are constants.** The amplitude $\tilde\Xi_{0}$ can be written in the polar word like any other $N$-regular element, and its scale, angle, rapidity and rotor are numbers of the mode. None of them depends on the wave number, because there is only one wave number per mode. So the four factors have not been traded for four momentum-space functions; they have become four constants attached to a point.

**What is momentum-dependent is the support and its direction.** The support point $\tilde K_\Phi$ carries the frequency and the wave vector. Its direction $\hat n=\vec k_\Phi/k_t'$ is the only other data the point carries, and on the massless shell it is the data that divides the cone into the two idempotents: $\tilde\Pi_\pm=\tfrac12(e_t\pm i\hat n\cdot\vec e)$. *The Fourier Transform and the Dirac Equation in Biquaternionic Form* proves that these are the two massless ideals, and the sign of $\hat n$ is what selects between them.

**So the four factors become one label, one direction and two signs.** The label is the four-momentum, the direction is its unit vector, and the two signs are the sign of the frequency, which selects the branch, and the sign of $\hat n$, which selects the idempotent. The word's eight parameters have become a point, a direction and two discrete signs, and the amplitude's four constants are not momentum-space structures at all.

**This is the article's finding about the polar variables, and it is a statement about where the reading lives.** The word is a reading of the field at an event. The transform replaces the event by a point of the shell, and a point has no scale, no angle, no boost and no rotor of its own — it has a position and, on the cone, a direction. **The polar reading is a position-space reading**, and no momentum-space version of it is claimed or expected here.

## The Cross-Check with the Polar Path Integral

**The polar path-integral article states the same thing from the kernel's side.** Its finding is that in momentum space the free Dirac kernel carries no action phase, and that its angle is one of the two labels $0$ and $\pi/2$, selected by the side of the mass shell; the action's phase appears only in position space, where the pole of the denominator is crossed and the Fourier integral oscillates.

**The present article gives the reason.** The action's phase is the word's angle $\theta_{\mathrm{pha}}$, and a phase is a translation: it moves the support and contributes nothing to it. So a momentum-space kernel cannot carry the action's phase, because the transform of a phase is a place. What it can carry is the label of the place it was moved to, which is what the labels $0$ and $\pi/2$ are.

**The two statements are one statement, and the difference between them is the transform.** The angle is the action in position space and a label in momentum space; §*The Phase Gradient Is the Fourier Variable* is why. Neither article's statement is weaker, and neither is a different physics.

## Limits

**Constant coefficients.** The word's gradient identity is exact for any field; the transform's algebraic reading needs constant coefficients, because a symbol that depends on the position turns the transform of the equation into a convolution. The mass is constant, so the free case is exact throughout. *The Coupled Dirac Equation in Biquaternionic Polar Variables* and *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism* are where the potential is treated.

**The Legendre momenta are not the Fourier variable.** The canonical momenta conjugate to the word's parameters, $p_{\theta_{\mathrm{pha}}}=\hbar c\,r^{2}\cosh\theta_{\mathrm{rpd}}=\hbar c\rho\gamma$ and $\vec p_{\mathrm{spin}}=-\hbar c\,r^{2}\sinh\theta_{\mathrm{rpd}}\hat n_{\mathrm{rot}}$, are Legendre momenta of the variational problem, with four partners that vanish identically. They are not $\hbar\tilde K_\Phi$, and the operation that produces them is not the transform. The polar variational parent calls them canonical and records them as primary constraints; what this article adds is one sentence, that the Fourier variable is a different conjugacy from theirs.

**The denial, once more.** The transform of a $\mathbb{B}_\Phi$-valued field is a $\mathbb{B}_\Phi$-valued field. The four factors are a parametrisation of one element at one event, and the transform's amplitude at one wave number is one element at one point of the shell. At no step does a sector change, and no display above mixes one.

**The convention.** The kernel's constant, the sign of its exponent and the placement of the kernel left or right are the transform article's conventions. No identity above depends on them: the phase-gradient identity is an identity of elements, and the convolution theorem holds for every placement.

## Open Questions

**One question is left, and the article does not answer it.** Whether any function of the word corresponds to a selection rule in momentum space — a superselection of the support, a restriction of the amplitude to one ideal at a given point — is not known to the author, and nothing above assumes either answer.

**The question is well posed because the object it asks about exists.** The amplitude at a point of the shell is an element of $\mathbb{B}$, its word exists where the element is $N$-regular, and the parent says which elements are not. Whether the momentum-space amplitude is restricted by anything beyond the shell is a question about that element and not about the transform, and it is not asked here.

## Summary

The transform's variable is the gradient of the field's own phase. The polar parent proves $\tilde\nabla_\Phi\theta_{\mathrm{pha}}=\tilde K_\Phi$ for any real angle, and this article reads the transform as extracting that coefficient: on a linear phase the transform is supported on the single wave number equal to the gradient, with modulus $\sqrt{N}$ on a lattice of $N$ samples and every other coefficient at round-off. The general statement is that a phase is a translation, $\mathcal{F}[e^{i\theta}f](\omega)=\hat f(\omega-\nabla\theta)$, so the action's phase becomes a place and contributes nothing to the place.

The word is a product of four element-valued functions, and the transform of a product is a convolution, checked to $1.4\times10^{-15}$ on 64 samples. So the four factors do not survive the transform as four factors, and no momentum-space function is the scale, the angle, the boost or the rotor. What survives is one element-valued density per mode, supported at the wave number, together with the direction of that wave number and two signs: the sign of the frequency and the sign of the direction, which on the massless shell selects between the two idempotents $\tfrac12(e_t\pm i\hat n\cdot\vec e)$.

The amplitude's own word has four factors, and they are constants of the mode, because a mode has one wave number. The polar reading is therefore a position-space reading. The polar path-integral article's finding that the momentum-space free Dirac kernel carries no action phase is the same statement from the kernel's side, and the reason is the one above: the transform of a phase is a place.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde\Xi=r e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The polar word; four factors, eight parameters |
| $\theta_{\mathrm{pha}}$ | The word's angle; the action's phase per $\hbar$ |
| $\tilde K_\Phi=\tilde\nabla_\Phi\theta_{\mathrm{pha}}$ | The wave number; the gradient of the angle |
| $\mathcal{F}[e^{i\theta}f](\omega)=\hat f(\omega-\nabla\theta)$ | A phase is a translation of the support |
| $\mathcal{F}[fg]=\mathcal{F}[f]*\mathcal{F}[g]$ | The transform of a product is a convolution |
| $\hat n=\vec k_\Phi/k_t'$ | The direction of the support point |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm i\hat n\cdot\vec e)$ | The two idempotents the direction selects on the cone |
| $p_{\theta_{\mathrm{pha}}}=\hbar c\,r^{2}\cosh\theta_{\mathrm{rpd}}$ | The Legendre momentum of the angle; not the Fourier variable |
| $\vec p_{\mathrm{spin}}=-\hbar c\,r^{2}\sinh\theta_{\mathrm{rpd}}\hat n_{\mathrm{rot}}$ | The rotor's Legendre momentum; zero at rest |

## Further Reading

- *The Dirac Equation in Biquaternionic Polar Variables*, for the word, its domain and the phase-gradient proposition.
- *The Fourier Transform and the Dirac Equation in Biquaternionic Form*, for the symbol, the light cone as the idempotent variety and the two massless ideals.
- *The Path Integral and the Dirac Equation in Biquaternionic Polar Variables*, for the momentum-space kernel's angle as a label of a region.
- *The Variational Principle and the Dirac Equation in Biquaternionic Polar Variables*, for the canonical momenta of the word and the four vanishing constraints.
- *The Variational Principle and the Dirac Equation in Biquaternionic Form*, for the action and the sentence about the $i$ inside the material time.
- *Derivatives, Fields and Transforms*, for the transform, its kernel and its symbol rule.
- *Wave–Particle Duality and the Fourier Transform*, for the transform as a change of description and the interval as a symbol.
- *Biquaternion Continuous Harmonic Analysis*, for the convolution theorem and Plancherel's condition.
- *Mirror Biquaternions and the Phy–Psy Switch*, for the sector bookkeeping.
- *Wave–Particle Duality and the Weight of a Level Set*, for the measure-theoretic reading of a support.
- M. Plancherel, "Contribution à l'étude de la représentation d'une fonction arbitraire par des intégrales définies," *Rendiconti del Circolo Matematico di Palermo* **30** (1910) 289–335, for the isometry.
- L. Mandel and E. Wolf, *Optical Coherence and Quantum Optics* (Cambridge, 1995), Part I, for the modulation and shift theorems in the form used here.
- T. Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, for the spin fluid whose four brackets the word carries.
- P. R. Holland, *The Quantum Theory of Motion* (Cambridge, 1993), for the same structure read as a guidance equation.
