# __The Euclidean Semiclassical Expansion and the Dilute Gas in Biquaternionic Form__

## Introduction

**The object.** The path integral of a theory with topology is a sum over sectors, and each sector is dominated by the configurations of least action. Expanding about them turns each into a contribution to a physical quantity, with a measure on the collective coordinates and a one-loop prefactor. When the configurations are dilute, the sum exponentiates and the result is an explicit non-perturbative term.

**What this article is.** The general machinery, with no sector attached: steepest descent in the Euclidean integral, the collective-coordinate measure, the sum over sectors and the theta angle, the dilute-gas approximation, the one-loop prefactor, and dimensional transmutation. It names no force; it applies to any theory with instantons.

**Where the applications are.**

- The strong sector. The application is [The Semiclassical Expansion and the Instanton Gas in Biquaternionic Form](the-semiclassical-expansion-and-the-instanton-gas-in-biquaternionic-form.html), which sets the machinery in the framework's compact factor and follows what the algebra does and does not provide. The theta angle that the sum produces is the subject of [The Theta Parameter and Strong CP in Biquaternionic Form](the-theta-parameter-and-strong-cp-in-biquaternionic-form.html).
- The electroweak sector. The same expansion exists there, and it is not what that sector's articles treat, because the weak sector's non-perturbative effects are not the object of the corpus's electroweak series.

## The Euclidean Integral and Steepest Descent

**The continuation.** The path integral $e^{\frac{2\pi iS}{h}}$ becomes $e^{-\frac{2\pi S_E}{h}}$ after continuation to Euclidean signature, and the weight is then largest where the Euclidean action is smallest. The saddle points are the solutions of the Euclidean equations of motion, and the integral is a sum of Gaussian fluctuations about them.

**The expansion.** For a saddle $\xi_{\mathrm{pot},0}$,

$$
Z=\sum_{\xi_{\mathrm{pot},0}}e^{-S_E[\xi_{\mathrm{pot},0}]\frac{2\pi}{h}}\int\mathcal{D}\delta\xi_{\mathrm{pot}}\ e^{-\frac{1}{2}\delta\xi_{\mathrm{pot}}\,S''[\xi_{\mathrm{pot},0}]\,\frac{2\pi \delta\xi_{\mathrm{pot}}}{h}},
$$

the inner integral being the one-loop determinant, which contributes a prefactor rather than a phase.

## Collective Coordinates and the Measure

**The zero modes.** A saddle that is not isolated has flat directions: translations, rotations, scale and gauge orientation. Each flat direction corresponds to a zero eigenvalue of $S''$, and the Gaussian integral along it is not Gaussian.

**The Jacobian.** The cure is to change variables from the field to the collective coordinates plus the orthogonal fluctuations. The change of variables produces a Jacobian,

$$
\boxed{\;\mathcal{D}\xi_{\mathrm{pot}}=\prod_i d c_i\ \sqrt{\det\left(\left\langle\frac{\partial\xi_{\mathrm{pot},0}}{\partial c_i},\frac{\partial\xi_{\mathrm{pot},0}}{\partial c_j}\right\rangle\right)}\ \mathcal{D}\xi_{\mathrm{pot},\perp}\;}
$$

so each zero mode becomes an integration over its coordinate with a measure fixed by the field-space metric. The determinant is the overlap matrix of the tangent vectors, and it is what makes the answer finite and correct.

## The Theta Vacuum and the Sum over Sectors

**The sectors.** The configurations fall into classes labelled by an integer $n$, and the integral is a sum over them. Because the classes are not connected by any continuous deformation, the sum is not constrained by locality, and a relative phase between sectors is allowed:

$$
\boxed{\;|\theta\rangle=\sum_n e^{in\theta}\,|n\rangle\;}
$$

with $\theta$ a parameter of the theory. The sum over sectors in the presence of $\theta$ weights the $n$-th sector by $e^{in\theta}$.

**The consequence.** A parameter that no symmetry forbids appears in the action, and the theory has one more coupling than the classical Lagrangian suggests. The theta term is a total derivative and therefore does not affect the equations of motion, but it does affect the weights, so it is physical.

## The Dilute Gas

**The approximation.** When the density of instantons is small, the configurations can be treated as non-interacting, and the sum exponentiates:

$$
\boxed{\;Z_\theta=\exp\left(2V\!\!\int\!d\rho\ \frac{d(\rho)}{\rho^5}\cos\theta\right)\;}
$$

**The reading.** The partition function becomes the exponential of a single-instanton contribution, the vacuum energy acquires a $\cos\theta$ dependence, and the result is non-perturbative in the coupling because $d(\rho)$ carries the factor $e^{-8\pi^2/g^2}$.

**The limits.** The approximation fails at large density, where interactions matter, and at large instanton size, where the integral diverges in the infrared. The divergence is not a defect of the method; it signals that the dilute gas is an ultraviolet description and that the infrared requires a different argument.

## The One-Loop Prefactor and Dimensional Transmutation

**The prefactor.** The determinant around the instanton gives a power of the scale, $d(\rho)\propto\mu^{b_0}\rho^{b_0}$, with $b_0$ the one-loop coefficient of the beta function. The exponent is the same one that appears in the running coupling.

**The transmutation.** Combining the classical factor with the prefactor replaces the coupling by a scale,

$$
\boxed{\;\Lambda=\mu\,e^{-8\pi^2/(b_0g^2(\imath))}\;}
$$

so the theory trades a dimensionless coupling for a dimensionful parameter. This is dimensional transmutation, and it is the reason a theory with no mass parameter can have a mass gap.

## What the Framework Supplies

- **Supplied.** The Euclidean continuation, through the Wick rotation that identifies $\mathbb{B}_\Phi$ with its real-quaternion subspace, and the one-instanton data — charge, action, moduli — from the companion articles.
- **Imported.** The steepest-descent machinery, the collective-coordinate measure, the theta angle and the beta function. These are standard field theory, transcribed.
- **Not supplied.** A sector. The machinery is silent on which theory it is applied to, and the two applications are named above.

**Where the application is.** [The Semiclassical Expansion and the Instanton Gas in Biquaternionic Form](the-semiclassical-expansion-and-the-instanton-gas-in-biquaternionic-form.html) carries the whole expansion in the framework's compact factor and records the phase-integral content and the gaps.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S_E$ | the Euclidean action |
| $c_i$ | collective coordinates |
| $\theta$ | the vacuum angle |
| $n$ | the topological sector label |
| $\rho$ | the instanton size |
| $d(\rho)$ | the instanton density per unit size |
| $b_0$ | the one-loop beta-function coefficient |
| $\Lambda$ | the transmuted scale |

## Further Reading

- G. 't Hooft, "Computation of the Quantum Effects Due to a Four-Dimensional Pseudoparticle," *Physical Review D* **14** (1976) 3432, the measure and the prefactor.
- C. G. Callan, R. Dashen and D. J. Gross, "The Structure of the Connection theory Vacuum," *Physics Letters B* **63** (1976) 334, the theta vacuum.
- S. Coleman, *Aspects of Symmetry*, Chapter 7, for the dilute gas.
