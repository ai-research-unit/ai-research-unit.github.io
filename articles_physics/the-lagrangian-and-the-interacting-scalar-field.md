# __The Lagrangian and the Interacting Scalar Field__

## Introduction

**The question.** The corpus's scalar field articles are free: the action is quadratic, the equation is linear, and two solutions can be added. This article writes the smallest action that is not, the quartic self-interaction of one complex scalar, and asks what the variational principle says about it. The answer is short and it is not a scattering theory.

**The answer in three sentences.** One action, the free Klein–Gordon action with $-\frac{\lambda}{4}\bigl(\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)\bigr)^{2}$ added, has the nonlinear equation $\bigl(\Box_\Phi-k_m^{2}\bigr)\tilde\Xi=\lambda\,\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)\,\tilde\Xi$ as its Euler–Lagrange equation. The nonlinearity is a density-dependent mass: on a plane wave the dispersion relation gains $\lambda N$ with $N=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$, so the field's own density acts as a mass. The current is unchanged, because the interaction depends on $\tilde\Xi^{*}\tilde\Xi$ and therefore commutes with the global phase.

**What is not done.** No scattering amplitude, no perturbation series, no Feynman rule, no loop, no renormalisation. This family has no quantised theory in which a four-point function could be computed, and this article does not manufacture one. What it has is the classical action, its exact equation, its exact current and its exact stress, and the observation that all three differ from the free ones in a controlled way.

**Declared omissions.** The reality of the action is settled inside *The Action*, term by term, so slot 5 is omitted. The action imposes no constraint beyond its own equation, so slot 6 is omitted. The second variation is not computed, so slot 8 is omitted. The two settings are not contrasted, so slot 10 is omitted. No limit is taken here, so slot 11 is omitted. No comparison with the textbook $\phi^{4}$ treatment is attempted, so slot 13 is omitted. The open questions are folded into the ledger, so slot 14 is omitted.

## Conventions

**The conventions are the free companion's, with one addition.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_\mu^{2}=-e_t$; the field is one element $\tilde\Xi\in\mathbb{B}$ with four complex coefficients; the pairing is $\mathrm{Sc}(\cdot^{*}\cdot)$, the Hermitian one, for the reasons the free article gives; the measure is $\mathrm{d}^{4}r$; $k_m=mc/\hbar$.

The addition is the coupling $\lambda$, a real number with the dimensions that make $\lambda N$ a squared wave number, and the density

$$
N=\mathrm{Sc}\bigl(\tilde\Xi^{*}\tilde\Xi\bigr)=\varrho^{2} ,
$$

which is real and non-negative for every field, because $\tilde\Xi^{*}\tilde\Xi$ is Hermitian and a Hermitian element's scalar part is real. The symbol $N$ is used for this number throughout and is not to be confused with a particle number: it is a density per unit volume, and the corpus's charge density is a different object.

## The Action

**The free action plus one term.**

$$
S[\tilde\Xi,\tilde\Xi^{*}]=\int\mathrm{d}^{4}r\;\Bigl\{\mathrm{Sc}\Bigl[(\partial_{r'_t}\tilde\Xi)^{*}\partial_{r'_t}\tilde\Xi-\sum_\eta(\partial_{r_\eta}\tilde\Xi)^{*}\partial_{r_\eta}\tilde\Xi-k_m^{2}\tilde\Xi^{*}\tilde\Xi\Bigr]-\frac{\lambda}{4}N^{2}\Bigr\}.
$$

The free part is the free article's, sign for sign, and the interaction is one central term. Three properties are checked in one line each.

**It is real.** $N=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$ is real, so $N^{2}$ is real and positive; the coupling $\lambda$ is real; so the added term is real and so is the whole density.

**It is invariant under the global phase.** $\tilde\Xi\mapsto e^{i\theta}\tilde\Xi$ leaves $\tilde\Xi^{*}\tilde\Xi$ unchanged, because $e^{-i\theta}e^{i\theta}=e_t$, so $N$ and every term built from it are invariant. The interaction therefore does not break the symmetry whose current the free article computes; it changes the current's conservation not at all and the equation's linearity completely.

**It is not a mass term.** A mass term is quadratic in the field; this is quartic, and it cannot be absorbed into $k_m^{2}$ because $N$ varies from point to point and from solution to solution. That distinction is the article's structural claim, and the next section but one makes it precise.

**Why the coefficient is $\lambda/4$ and not $\lambda$.** So that the equation's right side carries $\lambda$ and not $2\lambda$: the derivative of $-\frac{\lambda}{4}N^{2}$ with respect to $N$ is $-\frac{\lambda}{2}N$, and the variation of $N$ contributes a factor two, as the next section shows. The convention is the corpus's and is stated once, here.

## The Variation

**Varying the conjugate, with one new term.** The free part gives the free article's bracket after two integrations by parts. The interaction's variation is

$$
\delta\Bigl(-\frac{\lambda}{4}N^{2}\Bigr)=-\frac{\lambda}{2}N\,\delta N
=-\frac{\lambda}{2}N\,\mathrm{Sc}\bigl(\delta\tilde\Xi^{*}\tilde\Xi+\tilde\Xi^{*}\delta\tilde\Xi\bigr)
=-\lambda N\,\mathrm{Sc}\bigl(\delta\tilde\Xi^{*}\tilde\Xi\bigr),
$$

using that $N$ is real and that the second term is the conjugate of the first inside $\mathrm{Sc}$.

**The equation.** Collecting with the free bracket,

$$
\delta S=\int\mathrm{d}^{4}r\;\mathrm{Sc}\Bigl[\delta\tilde\Xi^{*}\Bigl(\bigl(\Box_\Phi-k_m^{2}\bigr)\tilde\Xi-\lambda N\tilde\Xi\Bigr)\Bigr]
+\text{(boundary)},
$$

and stationarity for every $\delta\tilde\Xi^{*}$ forces

$$
\bigl(\Box_\Phi-k_m^{2}\bigr)\tilde\Xi=\lambda\,\mathrm{Sc}\bigl(\tilde\Xi^{*}\tilde\Xi\bigr)\,\tilde\Xi .
$$

**The boundary term is the free one.** The interaction carries no derivative, so it adds nothing to the surface term; the free article's discussion applies unchanged.

**Two features worth naming.** The equation is nonlinear but *semilinear*: the second derivative appears linearly and the nonlinearity is algebraic in the field. And the right side is homogeneous of degree three, so the equation is invariant under $\tilde\Xi\mapsto-\tilde\Xi$ but not under a phase rotation of the field by a real scale: the $\mathbb{Z}_2$ survives, the $U(1)$ acts as a symmetry only because $N$ is invariant.

## The Structural Consequence: The Nonlinearity Is a Density-Dependent Mass

**The article's claim, in one sentence.** The quartic term does not add a force of a new kind; it changes the mass that a mode of the field carries, and the change is proportional to the density the mode itself contributes.

**The hand check.** Take a plane wave $\tilde\Xi=\tilde\Xi_0\exp\bigl(-i(\omega r'_t/c-\vec k_\Phi\cdot\vec r)\bigr)$ with a constant amplitude and $N=\mathrm{Sc}(\tilde\Xi_0^{*}\tilde\Xi_0)$. Then $\Box_\Phi\tilde\Xi=-(\omega^{2}/c^{2}-k_\Phi^{2})\tilde\Xi$, and the equation becomes

$$
\Bigl(\frac{\omega^{2}}{c^{2}}-k_\Phi^{2}\Bigr)\tilde\Xi_0=\bigl(k_m^{2}+\lambda N\bigr)\tilde\Xi_0 ,
$$

so the dispersion relation is $\omega^{2}=c^{2}\bigl(k_\Phi^{2}+k_m^{2}+\lambda N\bigr)$. The mass squared has become $k_m^{2}+\lambda N$: one number, shifted by the amplitude's own density.

**What follows from the shift.** For $\lambda>0$ the shift is positive and a denser wave is stiffer; for $\lambda<0$ it is negative and a sufficiently dense wave has a negative effective mass squared, so the constant-amplitude solution becomes unstable. That instability is the classical statement of what a quantised theory would call the instability of the symmetric vacuum, and the corpus can state it without quantising anything: it is a property of the dispersion relation.

**What the claim forbids.** It forbids describing the interaction as a potential energy between particles. There are no particles here: there is one field, and the only thing the quartic term does to it is to make the mass depend on the density. Any language of scattering would need states, and the corpus has no states.

## The Noether Currents and the Sign of the Charge

**The current is the free one, exactly.** The global phase leaves the interaction invariant, and the interaction carries no derivative, so it contributes nothing to the current:

$$
j_\mu=2\,\mathrm{Im}\,\mathrm{Sc}\bigl[\tilde\Xi^{*}\partial_\mu\tilde\Xi\bigr],
$$

the free article's bilinear, with the same sign convention. Its conservation on solutions is the statement that the equation's right side, $\lambda N\tilde\Xi$, transforms the same way as the left side under the phase: both are multiplied by $e^{i\theta}$, so the phase of the equation is not fixed and the current is conserved.

**The stress gains one term.** Translation invariance gives the free stress plus the interaction's contribution, which is the term $+\frac{\lambda}{4}N^{2}$ in the energy density, since the interaction is a function of the field and not of its derivatives: the canonical energy density is

$$
T^{00}=\sum_\mu\bigl\lvert\partial_\mu\tilde\Xi\bigr\rvert^{2}+k_m^{2}N+\frac{\lambda}{4}N^{2},
$$

in the flat notation, with the metric signs of the display. For $\lambda>0$ every term is positive and the energy is bounded below by zero.

**The sign of the charge.** The charge is the integral of $j_{r'_t}$, and its sign is the sign of the phase's orientation, exactly as in the free case. The interaction changes neither the charge nor its sign; it changes only the energy's dependence on the density. That separation is the reason the article can state the current in one line and spend its length on the equation.

## What the Principle Adds and What It Relabels

**Adds.** One exact nonlinear equation with an exact current and an exact stress, and the identification of the nonlinearity as a density-dependent mass. That identification is genuinely useful: it tells a reader what to expect from the quartic term without any perturbation theory, and it explains why the term is the standard first interaction of a scalar.

**Relabels.** The free theory's structures. The current is unchanged, the symmetry is unchanged, the boundary term is unchanged. What the interaction does is to make the equation nonlinear, and that is the whole of the addition.

**What it does not reach, and this family does not either.** A scattering amplitude requires asymptotic states, an $S$-matrix, a perturbative expansion and a renormalisation of $\lambda$; none of those exists here. A reader who wants the four-point function will find the action, the vertex's classical shadow in the quartic term, and no way to compute anything with it. The honest statement is that this family supplies the classical half of the theory and knows it.

**One consequence worth keeping.** Because the equations are exact, the article can make exact statements — the dispersion shift $\lambda N$, the stability threshold at $k_m^{2}+\lambda N=0$, the positive energy for $\lambda>0$ — that a perturbative treatment would only approximate. Whatever the corpus lacks, it does not lack exactness where it has an equation.

## Summary

The interacting scalar is the free scalar with one central quartic term, $-\frac{\lambda}{4}N^{2}$, and its Euler–Lagrange equation is $\bigl(\Box_\Phi-k_m^{2}\bigr)\tilde\Xi=\lambda N\tilde\Xi$. The nonlinearity is a density-dependent mass, with dispersion $\omega^{2}=c^{2}(k_\Phi^{2}+k_m^{2}+\lambda N)$; the current and the symmetry are the free ones; the energy gains a positive $\frac{\lambda}{4}N^{2}$ and is bounded below for $\lambda>0$. No scattering theory is constructed, and the article says why: the corpus has no quantised states to scatter.

$$
S=\int\mathrm{d}^{4}r\;\Bigl\{\mathrm{Sc}\bigl[(\partial_{r'_t}\tilde\Xi)^{*}\partial_{r'_t}\tilde\Xi-\textstyle\sum_\eta(\partial_{r_\eta}\tilde\Xi)^{*}\partial_{r_\eta}\tilde\Xi-k_m^{2}\tilde\Xi^{*}\tilde\Xi\bigr]-\frac{\lambda}{4}N^{2}\Bigr\},
\qquad N=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi).
$$

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\ \vec e_\mu^{2}=-e_t$ | Basis and its squares |
| $\mathrm{Sc}$ | Coefficient of $e_t$ |
| $\tilde\Xi$ | The scalar field, four complex coefficients |
| $N=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)=\varrho^{2}$ | Density, real and non-negative |
| $\lambda$ | Quartic coupling, real, dimension of a squared wave number per density |
| $k_m=mc/\hbar$ | Mass wave number |
| $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial r'^{2}_{t}$ | d'Alembertian on the material sector |
| $j_\mu$ | Phase current, the free bilinear |
| $T^{00}$ | Energy density |
| $S,\ \mathcal{L}$ | Action and Lagrangian density |

## Further Reading

- *The Lagrangian and the Klein–Gordon Equation*, the free companion, whose action, current and stress this article extends.
- *The Lagrangian and the Coupled Klein–Gordon Equation*, for a different way of making the scalar equation non-trivial: by a connection rather than by a self-interaction.
- *The Lagrangian and the Second Quantisation: From the Action to the Commutator*, for what would be needed before a four-point function could be written down.
- Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory*, for the quantised $\phi^{4}$ theory this article deliberately does not construct.
- Sidney Coleman, *Aspects of Symmetry*, for the classical stability and the effective-mass language.
