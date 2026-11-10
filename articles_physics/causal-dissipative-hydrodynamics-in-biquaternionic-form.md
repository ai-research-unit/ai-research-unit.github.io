# __Causal Dissipative Hydrodynamics in Biquaternionic Form__

## Introduction

**The first-order theory of [The Local Entropy Current](the-local-entropy-current.html) is not a theory of anything that propagates, and the corrections that make it one are Israel–Stewart's.**

$$
\tau_{\Pi}\,\frac{d\Pi}{d\tau}+\Pi=-\zeta\,\theta,
\qquad
\tau_{\pi}\,\frac{d\pi_{\lambda\nu}}{d\tau}+\pi_{\lambda\nu}=-2\eta_{\mathrm{sh}}\,\sigma^{\mathrm{sh}}_{\lambda\nu},
\qquad
\tau_{q}\,\frac{dq_{\lambda}}{d\tau}+q_{\lambda}=-\kappa_{\mathrm{th}}\,\partial_\lambda T ,
$$

**the three relaxation equations for the bulk stress, the shear and the heat flux**, with the three relaxation times as new transport coefficients. **The article's claim is that these three displays replace three algebraic relations and change nothing else** — the conservation laws, the equation of state and the entropy current of the earlier articles are untouched.

**Why the replacement is necessary, in one sentence.** The first-order relations make the shear stress respond instantaneously to the shear, which makes the shear's equation parabolic, which makes a signal travel at infinite speed; **the relaxation time gives the response an inertia and the equation a wave character, and the wave's speed is finite.**

**This article is a transcription: it is standard Israel–Stewart-type causal hydrodynamics in the corpus's letters, with no framework interpretation.** The equations are Israel's and Israel–Stewart's; the entropy current and its Hermiticity declaration are the category's own, inherited and not rewritten; **the algebra's contribution is the notation, and the article says so rather than dressing a transcription as a derivation.**

**What the article inherits and does not rewrite.** The entropy inequality of [The Local Entropy Current](the-local-entropy-current.html) is written once, with the current declared Hermitian; **this article's positivity section inherits that declaration and writes no fresh $\mathrm{Re}$**, because a second declaration would be a second convention and the corpus keeps one.

## Why the First-Order Theory Fails

### The parabolic equation

**A first-order theory relates the flux to the gradient at the same instant, and the resulting equation is parabolic.** For heat conduction the relation is $q_{\lambda}=-\kappa_{\mathrm{th}}\partial_\lambda T$ and, combined with energy conservation, it gives

$$
\partial_t T=\frac{\kappa_{\mathrm{th}}}{c_{V}}\,\partial_\lambda\partial_\lambda T ,
$$

**the diffusion equation, whose solutions spread a disturbance over all space in any non-zero time.** The equation is not wrong as a description of slow variations; it is wrong as a description of a propagation, **because a diffusion equation has no front**.

**The consequence, stated as the standard objection.** A localized initial disturbance has, at any $t>0$, a non-zero value at every point; **so the theory permits a signal to travel at unbounded speed**, which contradicts the framework's own causal structure — the light cone of the metric $\delta_{\mu\nu}$. **The contradiction is not a matter of interpretation and does not depend on the corpus's letters**: it is visible in the diffusion equation.

**The same objection in the shear channel.** The algebraic relation $\pi_{\lambda\nu}=-2\eta_{\mathrm{sh}}\sigma^{\mathrm{sh}}_{\lambda\nu}$ combined with momentum conservation gives a parabolic equation for the velocity, **so a shear disturbance also travels at unbounded speed.** The bulk channel is parabolic for the same reason. **Three channels, one defect.**

### The instability

**The first-order theory is also unstable, and the instability is not merely the acausality in another guise.** A linearized analysis of the full first-order system, with the equilibrium state as the background, gives modes whose growth rate is unbounded above: **the shortest-wavelength modes grow fastest**, so the equilibrium is not a stable solution of the theory at all.

**The mechanism, in one line.** The first-order relations make the stress a function of the gradients, so the equations are a system of first-order equations in space and time whose symbol has no bound; **a mode of wave number $k$ has a growth rate proportional to $k$**, and no amount of care with the equilibrium state removes it.

**Why this matters for the earlier articles.** Everything they wrote — the equation of state, the entropy current, the production — remains true of the *equilibrium* and of *slow* departures from it. **What fails is the claim that the theory describes arbitrary departures**, and the relaxation equations are what restore that claim.

## The Israel–Stewart Corrections

### The three relaxation equations

**Each dissipative flux gains a relaxation time and an inertial term, and the algebraic relation becomes a differential one.**

$$
\tau_{\Pi}\,\frac{d\Pi}{d\tau}+\Pi=-\zeta\,\theta,
\qquad
\tau_{\pi}\,\frac{d\pi_{\lambda\nu}}{d\tau}+\pi_{\lambda\nu}=-2\eta_{\mathrm{sh}}\,\sigma^{\mathrm{sh}}_{\lambda\nu},
\qquad
\tau_{q}\,\frac{dq_{\lambda}}{d\tau}+q_{\lambda}=-\kappa_{\mathrm{th}}\,\partial_\lambda T ,
$$

**the displays at the head of the article, with $\tau$ the proper time along the flow and every index low.** The derivative is the comoving one, $\frac{d}{d\tau}=v_{\Phi,\mu}\partial_\mu/c$ in components, **so the equations are written in the fluid's own frame and are invariant because they are written on elements in the corpus's convention**.

**The relaxation time is a transport coefficient of the same standing as the viscosity**, and the second law constrains it: the production's new terms are quadratic in the fluxes and divided by the relaxation times, **so a positive production requires the relaxation times to be positive** as well as the coefficients.

**The limit in which the old theory is recovered.** As $\tau_{\Pi},\tau_{\pi},\tau_{q}\to0$ the inertial terms vanish, the algebraic relations return, and the theory returns to the first order's — **acausality and instability included**. That is the correct statement of the relationship: **the first-order theory is the singular limit of the causal one**, and the singularity is the loss of the highest derivative.

### What the correction changes and what it does not

**Changes: the number of transport coefficients.** A causal theory has six where the first-order theory has three — $\zeta$, $\eta_{\mathrm{sh}}$, $\kappa_{\mathrm{th}}$ and their three relaxation times. **A model with fewer is first-order in disguise.**

**Changes: the order of the equations.** The system is now second order in time for the fluxes, so it needs initial data for the fluxes and not only for the conserved densities. **That is the price of causality and it is not optional**: a hyperbolic system needs more data than a parabolic one.

**Does not change: the conservation laws.** The energy-momentum element's conservation is the same display, and the spin's is [Spin Conservation and the Frenkel Condition](spin-conservation-and-the-frenkel-condition.html)'s. **The relaxation equations modify the constitutive relations, not the conservation laws.**

**Does not change: the equation of state.** [The Equation of State in Biquaternion Form](the-equation-of-state-in-biquaternion-form.html)'s $p_{\mathrm{eff}}=p_{\mathrm{th}}+p_{\mathrm{qnt}}$ stands; the relaxation affects how fast the pressure reaches its value, not what the value is.

**Does not change: the entropy current's form.** [The Local Entropy Current](the-local-entropy-current.html)'s $\tilde J_{\Phi,\mathrm{ent}}=s_{\mathrm{ent}}\gamma(e_t+\vec\beta_{\mathrm{vel}})$ stands, with the production gaining the relaxation terms. **The current is Hermitian before and after**, which is why the positivity section writes no new declaration.

### The relaxation time against the hydrodynamic scale

**A relaxation time is a microscopic time, and the theory is a hydrodynamic one only while it is short against the macroscopic time.**

$$
\mathrm{Kn}_{\tau}=\frac{\tau_{q}}{L/c},
$$

**the ratio of the relaxation time to the light-crossing time of the system's size $L$**, which plays the role of the Knudsen number for the causal theory. **The expansion is in this ratio**, so the relaxation equation is a controlled correction while $\mathrm{Kn}_\tau\ll1$ and an uncontrolled model when it is not.

**Numbers, so that the statement has a scale.** For $\tau_q=1\,\mathrm{fm}/c$ and a system of $L=10\,\mathrm{fm}$, the ratio is $0.1$: the relaxation time is a tenth of the crossing time and the expansion is reasonable. For $L=2\,\mathrm{fm}$ the ratio is $0.5$ and the expansion is marginal; **for a system smaller than a few relaxation lengths the causal theory is the only one available and the expansion is not**, which is the situation in which the corrections were invented.

**What the ratio does not measure.** It does not measure the accuracy of the transport coefficients, and it does not bound the front speed; **causality is the separate condition of the next section**, and the two conditions are independent. A theory can have a small $\mathrm{Kn}_\tau$ and be acausal if the diffusivity is too large, and a causal one with a large $\mathrm{Kn}_\tau$.

### What the relaxation time is not

**Not necessarily a mean free time.** In a kinetic derivation it is of the order of one, but the relation is a model-dependent statement and not an identity; **the article keeps the two apart because the identification is the step that a reader is most likely to assume and least likely to check.**

**Not a cutoff.** The relaxation equation is a differential equation, not a modification of the spectrum above some wave number; **the theory has modes at every wave number and the front speed is what limits their propagation**, which is why the causal statement is a statement about the dispersion relation's asymptotics and not about a truncation.

**Not a free parameter.** The second law fixes its sign and the causality condition bounds it below by $D_{\mathrm{th}}/c^{2}$; **so a fit that yields a relaxation time below that bound yields a theory that is not causal**, and the bound is the article's one predictive statement about the coefficient.

## Causal Propagation

### The dispersion relation of one channel

**The relaxation equation turns the diffusion equation into a wave equation with damping, and the dispersion relation shows both.**

$$
\omega^{2}+\frac{i}{\tau_{q}}\,\omega-\frac{D_{\mathrm{th}}}{\tau_{q}}\,k^{2}=0,
\qquad
D_{\mathrm{th}}=\frac{\kappa_{\mathrm{th}}}{c_{V}},
$$

**the quadratic that follows from the relaxation equation combined with energy conservation**, with $D_{\mathrm{th}}$ the thermal diffusivity and $k$ a wave number. **The equation is the article's whole causal structure in one line**: the $i\omega/\tau_q$ term is the damping and the $k^{2}$ term is the propagation whose speed the damping limits.

**The two roots, and what they mean.** The roots are

$$
\omega=-\frac{i}{2\tau_{q}}\pm\frac{1}{2}\sqrt{-\frac{1}{\tau_{q}^{2}}+4\,\frac{D_{\mathrm{th}}}{\tau_{q}}k^{2}} ,
$$

**so the sign of the discriminant decides between two over-damped modes and two propagating ones.** When $D_{\mathrm{th}}k^{2}\tau_{q}<\tfrac14$ the square root is imaginary, both roots are imaginary and the disturbance decays without oscillating; **when the inequality is reversed the roots have real parts and the disturbance propagates.**

**The asymptotic speed, which is the number that matters for causality.** For large $k$ the real part of the root tends to $\sqrt{D_{\mathrm{th}}/\tau_{q}}\,k$, so the front speed is

$$
v_{\mathrm{frt}}=\sqrt{\frac{D_{\mathrm{th}}}{\tau_{q}}} ,
$$

**the speed at which the shortest wavelengths travel** and therefore the fastest signal the theory permits. **Causality is the statement $v_{\mathrm{frt}}\le c$**, which is the inequality

$$
D_{\mathrm{th}}\le\tau_{q}\,c^{2},
$$

**a condition on the relaxation time and not on the diffusivity alone.** The article states it as the theory's causality condition and notes that it is a constraint the second law does not supply — **the entropy inequality fixes signs, and causality fixes magnitudes.**

### Numbers

**The front speed was evaluated at four pairs, and one of them is acausal, which is the point of the table.** The diffusivity enters as the length $D_{\mathrm{th}}/c$, in fm, because $\sqrt{D_{\mathrm{th}}/\tau_{q}}$ is a speed only when the diffusivity carries its own length$^{2}$/time.

| $D_{\mathrm{th}}/c$ (fm) | $\tau_{q}$ (fm/$c$) | $v_{\mathrm{frt}}/c$ | verdict |
|---|---|---|---|
| $0.1$ | $0.5$ | $0.4472$ | causal |
| $0.2$ | $1.0$ | $0.4472$ | causal |
| $0.5$ | $0.5$ | $1.0000$ | marginal |
| $1.0$ | $0.5$ | $1.4142$ | acausal |

**The third row is the boundary and the fourth is past it**, so the condition $D_{\mathrm{th}}\le\tau_q c^{2}$ is not a formality: **a physical diffusivity with too short a relaxation time gives a theory whose fastest signal outruns light**, and that is exactly the defect the first-order theory has in the limit $\tau_q\to0$.

**The dispersion, evaluated twice at $k=2\,\mathrm{fm}^{-1}$.** With $D_{\mathrm{th}}/c=0.2\,\mathrm{fm}$ and $\tau_{q}=1\,\mathrm{fm}/c$ the roots are $\omega=0.741\,620-0.500\,000\,i$ and its conjugate's negative, so the phase speed is $\mathrm{Re}\,\omega/k=0.370\,810\,c$ and the damping rate is $0.500\,000$ per $\mathrm{fm}/c$. With $D_{\mathrm{th}}/c=0.05\,\mathrm{fm}$ and the same $\tau_q$ the roots are $-0.276\,393\,i$ and $-0.723\,607\,i$, **both purely imaginary, so the mode is over-damped and does not propagate at that wave number.** The threshold between the two behaviours is $D_{\mathrm{th}}/c=0.062\,500\,\mathrm{fm}$ at $k=2\,\mathrm{fm}^{-1}$ and $\tau_q=1\,\mathrm{fm}/c$, **which is $1/(4k^{2}\tau_q)$ and is the discriminant's zero.**

**What the numbers establish and what they do not.** They establish that the relaxation equation has the two regimes and that the front speed is $\sqrt{D_{\mathrm{th}}/\tau_q}$; **they do not establish that a given fluid's coefficients satisfy the causality condition**, which is a statement about the fluid and not about the equation.

### The shear and bulk channels

**The same structure holds in the other two channels with the kinematic viscosities in place of the diffusivity.**

$$
v_{\mathrm{frt,sh}}=\sqrt{\frac{\eta_{\mathrm{sh}}}{\rho_{\mathrm{num}}\,\tau_{\pi}}},
\qquad
v_{\mathrm{frt,bk}}=\sqrt{\frac{\zeta}{\rho_{\mathrm{num}}\,\tau_{\Pi}}},
$$

**so each channel has its own causality condition and the theory is causal only if all three hold.** The article writes the three because **a single satisfied channel is the commonest way a causal claim is made falsely.**

**The combined condition, in one line.** With $v_{\mathrm{snd}}$ the sound speed, the Israel–Stewart system is causal when the three front speeds and the sound speed are all at most $c$; **the sound speed's own bound is the equation of state's and not the relaxation's**, and the article does not conflate the two.

## Positivity and Stability

### The quadratic form

**The equilibrium is stable when the energy's second variation is a positive definite quadratic form in the dissipative fluxes, and the causal theory's form is the first-order one divided by the relaxation times.**

$$
\delta^{2}w_{\mathrm{fl}}=\frac{\Pi^{2}}{2\zeta\tau_{\Pi}}+\frac{\pi_{\lambda\nu}\pi_{\lambda\nu}}{4\eta_{\mathrm{sh}}\tau_{\pi}}+\frac{q_{\lambda}q_{\lambda}}{2\kappa_{\mathrm{th}}\tau_{q}} ,
$$

**the standard Israel–Stewart result, quoted with every index low.** Each term is a square divided by a positive coefficient and a positive relaxation time, **so the form is positive definite exactly when the six coefficients are positive** — the three transport coefficients and the three relaxation times.

**Why this is the statement of stability.** The fluxes are the system's extra degrees of freedom, and the quadratic form is their energy cost; **a positive cost means that a departure from equilibrium raises the energy, so the equilibrium is a minimum and the linearized dynamics is oscillatory-damped rather than growing.** A negative coefficient would make some departure lower the energy, and the theory would have no equilibrium to return to.

**The relation to the entropy.** The same quadratic form divided by the temperature is the entropy's second variation, **so positivity of the energy's form and concavity of the entropy are one statement**; the corpus writes it on the energy because that is the element the earlier articles already have.

### The inherited declaration

**Every quantity in the display is the scalar part of an element, and the display is real because the currents are Hermitian — the declaration is [The Local Entropy Current](the-local-entropy-current.html)'s and this article does not repeat it.**

**How the inheritance works, spelled out because it is the article's only non-transcriptive claim.** The entropy current was declared Hermitian, $\tilde J_{\Phi,\mathrm{ent}}^{*}=\tilde J_{\Phi,\mathrm{ent}}$, so the scalar part of its divergence is a real number; the production's relaxation terms are built from the same elements, so their scalar parts are real for the same reason; **and the quadratic form above is the second variation of that real scalar part.** A fresh $\mathrm{Re}$ would be a second convention for the same fact, **and the corpus's rule is one declaration per category, not one per display.**

**What a reader should check, and it is one thing.** That no inequality in this article needs a $\mathrm{Re}$ in front of it, and that every inequality in it is a statement about a real number. **The check passes: the only inequalities are the causality conditions, which are comparisons of speeds, and the positivity of the six coefficients, which is a statement about real parameters.** The one $\mathrm{Re}$ the article does print stands in front of a dispersion root, $\mathrm{Re}\,\omega$, where the real part of a complex frequency is meant; that is a real part of a number and not a convention for reading a complex scalar part, and the two usages are different in kind.

**The stability statement, in its final form.** The causal theory is stable, causal and thermodynamically consistent when the six coefficients are positive and the three causality conditions hold; **the first-order theory is the limit in which the relaxation times vanish, in which the causality conditions cannot hold, and in which the stability statement loses its form because the denominators vanish.** That is why the corrections are not a refinement but a repair.

## What Is Established and What Is Interpretation

**Established, and standard.** That the first-order theory is parabolic, acausal and unstable; that the Israel–Stewart relaxation equations restore hyperbolicity; that the front speed of each channel is the square root of a diffusivity over a relaxation time; that causality is the condition that those speeds not exceed $c$; that the equilibrium is stable when the energy's second variation is positive definite in the fluxes; that the first-order theory is the singular limit of the causal one.

**What the corpus contributes, and it is only notation.** The relaxation equations written on elements with every index low; the comoving derivative written as a contraction with the flow's components; and the inheritance of the entropy article's Hermiticity declaration, so that the positivity section writes no fresh $\mathrm{Re}$. **No new physics is claimed, and the article's transcription sentence says so.**

**Interpretation, and there is none in this article beyond the transcription.** The article's claims are the standard theory's; where a reader might expect a framework reading — the meaning of the relaxation time in terms of the thermal circle, the relation between $\tau_q$ and $\beta$ — **the article declines to offer one, because the relation is not established and a speculative one would be worse than none.**

**Not claimed.** That the transport coefficients have been computed from the field theory; that the relaxation times are related to $\beta$; that the two-fluid model's relaxation structure has been written; that the spin channel's relaxation has been coupled to this one beyond the statement that it exists.

## Summary

The first-order theory's three algebraic relations make the shear, bulk and heat channels parabolic, so a signal travels unboundedly fast and the equilibrium is unstable against short wavelengths. The Israel–Stewart corrections replace them by three relaxation equations, $\tau_{\Pi}\dot\Pi+\Pi=-\zeta\theta$, $\tau_{\pi}\dot\pi_{\lambda\nu}+\pi_{\lambda\nu}=-2\eta_{\mathrm{sh}}\sigma^{\mathrm{sh}}_{\lambda\nu}$ and $\tau_{q}\dot q_{\lambda}+q_{\lambda}=-\kappa_{\mathrm{th}}\partial_\lambda T$, with six coefficients instead of three and a system that is second order in time for the fluxes.

The dispersion relation $\omega^{2}+(i/\tau_q)\omega-(D_{\mathrm{th}}/\tau_q)k^{2}=0$ gives two over-damped modes when $D_{\mathrm{th}}k^{2}\tau_q<\tfrac14$ and two propagating ones above it, with the asymptotic front speed $v_{\mathrm{frt}}=\sqrt{D_{\mathrm{th}}/\tau_q}$. Evaluated: $0.4472\,c$ for $(0.1,0.5)$ and $(0.2,1.0)$, $c$ exactly for $(0.5,0.5)$ and $1.4142\,c$ for $(1.0,0.5)$, so the causality condition $D_{\mathrm{th}}\le\tau_qc^{2}$ is a real constraint. At $k=2\,\mathrm{fm}^{-1}$ with $D_{\mathrm{th}}/c=0.2\,\mathrm{fm}$ and $\tau_q=1\,\mathrm{fm}/c$ the root is $0.741\,620-0.500\,000\,i$, a phase speed of $0.370\,810\,c$; at $D_{\mathrm{th}}/c=0.05\,\mathrm{fm}$ the roots are $-0.276\,393\,i$ and $-0.723\,607\,i$ and the mode is over-damped, with the threshold at $D_{\mathrm{th}}/c=0.062\,500\,\mathrm{fm}$.

The equilibrium is stable when the energy's second variation, $\delta^{2}w_{\mathrm{fl}}=\Pi^{2}/(2\zeta\tau_{\Pi})+\pi_{\lambda\nu}\pi_{\lambda\nu}/(4\eta_{\mathrm{sh}}\tau_{\pi})+q_{\lambda}q_{\lambda}/(2\kappa_{\mathrm{th}}\tau_{q})$, is positive definite — evaluated once at $\Pi=0.05$, $\pi=0.1$, $q=0.02$ with $\zeta=0.1$, $\eta_{\mathrm{sh}}=0.2$, $\kappa_{\mathrm{th}}=0.05$ and all three relaxation times $1$, $1$ and $0.5$, the three terms are $0.012\,500$, $0.012\,500$ and $0.008\,000$ for a total of $0.033\,000$. The form is real by the Hermiticity declaration of [The Local Entropy Current](the-local-entropy-current.html), which this article inherits and does not repeat.

**This is standard Israel–Stewart-type causal hydrodynamics in the corpus's letters, with no framework interpretation.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Pi$ | Bulk stress |
| $\pi_{\lambda\nu}$ | Shear stress, indices low |
| $q_{\lambda}$ | Heat flux |
| $\tau_{\Pi}$, $\tau_{\pi}$, $\tau_{q}$ | Relaxation times |
| $\zeta$, $\eta_{\mathrm{sh}}$, $\kappa_{\mathrm{th}}$ | Bulk viscosity, shear viscosity, conductivity |
| $\theta=\partial_\mu v_{\Phi,\mu}$ | Expansion, the divergence of the flow |
| $d/d\tau=v_{\Phi,\mu}\partial_\mu$ | Comoving derivative along the flow |
| $\sigma^{\mathrm{sh}}_{\lambda\nu}$ | Shear of the flow |
| $\tau$ | Proper time along the flow |
| $D_{\mathrm{th}}=\kappa_{\mathrm{th}}/c_{V}$ | Thermal diffusivity |
| $c_{V}$ | Heat capacity per unit volume |
| $\omega$, $k$ | Frequency and wave number |
| $v_{\mathrm{frt}}$, $v_{\mathrm{frt,sh}}$, $v_{\mathrm{frt,bk}}$ | Front speeds of the three channels |
| $v_{\mathrm{snd}}$ | Sound speed |
| $\mathrm{Kn}_{\tau}=\tau_{q}/(L/c)$ | Relaxation time against the crossing time |
| $L$ | System size |
| $\delta^{2}w_{\mathrm{fl}}$ | Second variation of the energy density |
| $w_{\mathrm{fl}}$, $p_{\mathrm{eff}}$ | Energy density, effective pressure |
| $p_{\mathrm{th}}$, $p_{\mathrm{qnt}}$ | The thermal and quantum parts of $p_{\mathrm{eff}}$ |
| $s_{\mathrm{ent}}$ | Entropy density |
| $\tilde J_{\Phi,\mathrm{ent}}$ | Entropy current, Hermitian, inherited |
| $\rho_{\mathrm{num}}=\lVert\tilde\Xi\rVert^{2}$ | Proper density |
| $T$, $\beta$ | Temperature, imaginary-time circumference |
| $c$, $\hbar$ | Speed of light, Planck constant |
| $e_t$ | Unit temporal direction |
| $\gamma$ | Boost factor of the flow |
| $\vec\beta_{\mathrm{vel}}=\vec v/c$ | Dimensionless velocity of the flow |
| $\mathrm{Sc}$, $\langle\ \rangle_{\natural}$ | Scalar part, quaternionic norm |

## Further Reading

- W. Israel, "Nonstationary irreversible thermodynamics: a causal relativistic theory," *Annals of Physics* **100** (1976) 310–331, for the relaxation equations and the causality condition.
- W. Israel and J. M. Stewart, "Transient relativistic thermodynamics and kinetic theory," *Annals of Physics* **118** (1979) 341–372, for the systematic derivation and the quadratic form.
- I. Müller, "Zum Paradoxon der Wärmeleitungstheorie," *Zeitschrift für Physik* **198** (1967) 329–344, for the first causal correction and the infinite-speed objection.
- C. Cattaneo, "Sulla conduzione del calore," *Atti del Seminario Matematico e Fisico della Università di Modena* **3** (1948) 83–101, for the relaxation term in heat conduction.
- W. A. Hiscock and L. Lindblom, "Stability and causality in dissipative relativistic fluids," *Annals of Physics* **151** (1983) 466–496, for the instability proof in the first-order theory and the stability conditions in the second.
- R. P. Geroch and L. Lindblom, "Dissipative relativistic fluid theories of divergence type," *Physical Review D* **41** (1990) 1855–1861, for the general classification of causal dissipative theories.
- P. Romatschke, "New developments in relativistic viscous hydrodynamics," *International Journal of Modern Physics E* **19** (2010) 1–53, for the modern uses and the coefficient counting.
- The companion articles: [The Local Entropy Current](the-local-entropy-current.html), [The Equation of State in Biquaternion Form](the-equation-of-state-in-biquaternion-form.html), [The Two-Fluid Model in Biquaternionic Form](the-two-fluid-model-in-biquaternionic-form.html), and [Spin Hydrodynamics in Biquaternionic Form](spin-hydrodynamics-in-biquaternionic-form.html).
