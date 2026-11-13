# __The Non-Quantum Limit of the Coupled Proca Equation using the Variational Principle__

## Introduction

**The limit taken on the coupled action, and the one thing the coupled chart does that the free chart could not.** *The Variational Principle and the Coupled Proca Equation in Biquaternionic Polar Variables* writes the action in the eight chart variables as a quadratic form in the gradients with a field-dependent metric, proves that the connection cannot change the metric because it is a central scalar in every slot, and records the Hessian's non-degeneracy as an **open item** rather than asserting it. The free variational companion had to reach for a mode before it could expand anything, because the free chart's fast variation sits in the modulus. **Here the chart carries a phase**, so the expansion is available on the parent's own variables.

**The one operation that has to be got right, stated first because everything else follows from it.** The truncation must be written on the mechanical gradient $\pi_\mu=\hbar\partial_\mu\vartheta_{\mathrm{pha}}+ϙA_\mu$ and not on $\hbar\partial_\mu\vartheta_{\mathrm{pha}}$. The shift is not small: it is the coupling times the potential over $\hbar$, and no power of $\epsilon$ controls it. **A truncation written on the canonical gradient would delete a group whose size is not the one the criterion measures**, and it would not be gauge invariant. Written on $\pi$, the truncation is gauge invariant exactly, because $\pi$ is.

**What the article establishes, in five sentences.** The parent's metric is untouched by the coupling, so the truncation deletes the second-order group and shifts one gradient, and the two operations act on different objects and commute. The truncated action is algebraic in the amplitude and quadratic in $\pi$, and the curvature enters it as the traceless antisymmetric form the Fourier companion writes as $\frac{iϙ}{\hbar}F$. Its amplitude variation is the order-zero algebraic system, whose real projection is the mass shell corrected by the longitudinal part, and whose Hessian is minus the Fourier companion's symbol, with determinant $-k_m^{2}(\pi^{2}-k_m^{2})^{3}$-type structure and rank one on the shell. Its phase variation is $\partial_\mu[(\pi\cdot a)a^{\mu}-\pi^{\mu}\lvert a\rvert^{2}]=0$, which is the covariant transport once the constraint holds — **a Gauss law of the decomposition's redundancy, not a dynamical equation**. The amplitude stops being dynamical, four momenta vanish, and the parent's open item does not need to be settled for any statement here.

**Notation.** The parent's: the field is the four-factor word $\tilde A=r\,e^{i\vartheta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ with eight real parameters; $\mathbb{B}_\Phi$ the material sector; $\tilde A=ie_t a'_t+\vec e\cdot\vec A$; the interval $v^{2}=v'^{2}_t-\lvert\vec v\rvert^{2}$; $\partial/\partial R_t=-i\partial/\partial r'_t$; $r'_t=ct$; $k_m=mc/\hbar$; $\tilde\nabla_{\mathrm{gco},\mu}=\partial/\partial R_\mu+\frac{iϙ}{\hbar}A_\mu$. Below, $\mathcal A$ denotes the slowly varying part of the word — scale, boost and rotor — and $a_\mu$ its four components.

## The Action in the Chart, and the Two Things It Makes Exact

**The kinetic term is a sigma-model form.**

$$
\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)
=\tfrac12\sum_\mu G^{ab}(q)\,\partial_\mu q_a\,\partial_\mu q_b
+\text{(terms linear in the gradients and in the connection)},
$$

with $q$ the eight parameters and $G$ the metric built from the frame's brackets. **The parent's exact statement about it is that the connection cannot enter it**: the covariant derivative adds one central scalar per slot to the logarithmic derivative, a central scalar is a multiple of the identity in the frame's basis, and $G$ is built from the non-central parts. **The metric is therefore the same object in the coupled and the free actions**, which is why the coupled chart is a shift and not a rotation.

**The mass term is the chart's one place where the frame's non-Lorentz part shows.** The parent computes $\mathrm{Sc}(\tilde A^{*}\tilde A^{\natural})/r^{2}$: it is $1$ whenever the rotor angle vanishes, for every rapidity and axis, to $10^{-14}$ over random draws; with the rotor engaged it is $0.7648$ at $\theta_{\mathrm{axr}}=0.7$ independent of the rapidity when the axes are collinear, and $0.7648$, $0.7010$, $0.4401$ at rapidities $0$, $1$, $2$ when they are perpendicular. **The invariant length is Lorentz invariant, so the boost cannot cost; only the rotor can, and only through the angle between the two axes.**

**What that means at this article's order, stated once and used below.** The mass term is a *potential* — a function of the parameters and not of their gradients — so it sits in the leading group of any expansion and appears in the algebraic system with a coefficient that the frame's angles can change by a factor of order one. **The limit does not remove that dependence and does not order it**: it is a term of order zero like the mass shell itself, and its only role is to make the longitudinal coefficient depend on the polarisation's frame.

**What the parent leaves open, and how this article treats it.** The parent states that the chart's system is second order and regular *in form*, and that it does not establish the Hessian's non-degeneracy. **This article does not need that item**: every statement below is about the truncated action's own Hessian, which is computed and is degenerate in a stated way. The parent's open item is a statement about the untruncated chart and remains open.

## The Truncation, Written on the Mechanical Gradient

**The mode and the group it exposes.** Write the word's slowly varying part as $\mathcal A$ and the field as $\tilde A=\mathcal A e^{i\vartheta_{\mathrm{pha}}}$. The covariant derivative then acts as

$$
\tilde\nabla_{\mathrm{gco},\mu}\tilde A=e^{i\vartheta_{\mathrm{pha}}}\Bigl(\partial_\mu+\frac{i}{\hbar}\pi_\mu\Bigr)\mathcal A,
\qquad
\pi_\mu=\hbar\,\partial_\mu\vartheta_{\mathrm{pha}}+ϙA_\mu ,
$$

so the phase enters only through $\pi$ and the potential enters only through $\pi$. **That single display is the whole of the truncation's legitimacy**: two objects that were separate in the parent's variables have become one, and the truncation must be written on the one.

**The three groups of the action.**

$$
S=\int d^{4}r\;\Bigl[\tfrac12\bigl(\lvert\pi\cdot a\rvert^{2}-\pi^{2}\lvert a\rvert^{2}\bigr)+\tfrac12\,k_m^{2}\,w(\mathcal A)\,\lvert a\rvert^{2}\Bigr]
+\text{(one derivative of }\mathcal A\text{)}
+\text{(two derivatives of }\mathcal A\text{)},
$$

with $w(\mathcal A)=\mathrm{Sc}(\tilde A^{*}\tilde A^{\natural})/r^{2}$ the parent's mass ratio. **The parent's metric is inside the one- and two-derivative groups and nowhere else**, because it multiplies the gradients; and the connection is inside $\pi$ and nowhere else, because it is central. **The two exact statements of the parent's first section are therefore what makes the grouping possible**, and the grouping is the limit.

**The truncated action.**

$$
S_{\mathrm{trunc}}=\int d^{4}r\;\Bigl[\tfrac12\bigl(\lvert\pi\cdot a\rvert^{2}-\pi^{2}\lvert a\rvert^{2}+k_m^{2}w\,\lvert a\rvert^{2}\bigr)+\tfrac12\,\bar a_{\nu}K^{\nu}{}_{\mu}a^{\mu}\Bigr],
$$

where $K$ is the curvature's matrix, antisymmetric and traceless, written $\frac{iϙ}{\hbar}F^{\nu}{}_{\mu}$ in the Fourier companion's symbol and fixed by it up to the sign that symbol carries. **Nothing below uses that sign**; the article uses only that $K$ is antisymmetric and traceless, and both are exact.

**Why the two-derivative group is the one to drop.** Its size is $\lvert a\rvert^{2}/L^{2}$ against the leading $\lvert a\rvert^{2}\pi^{2}$, so the ratio is $\epsilon^{2}$; and it is a functional of $\mathcal A$ alone, with no $\vartheta_{\mathrm{pha}}$ and no connection in it, so **dropping it cannot break gauge invariance** — the same argument the free variational companion makes, and here it is sharper because the action's gauge invariance is carried entirely by $\pi$.

**Gauge invariance, exactly, at the truncation's order.** Under $\vartheta_{\mathrm{pha}}\to\vartheta_{\mathrm{pha}}+\alpha$ and $\vec A\to\vec A-\frac{\hbar}{ϙ}\nabla\alpha$ the mechanical momentum is invariant, so $\pi$ is invariant and $S_{\mathrm{trunc}}$ is invariant. **The truncation is therefore gauge invariant for a structural reason and not by a check**: it is a functional of $\pi$ and of $\mathcal A$ alone.

## The Truncated Action's Two Variations

**The amplitude's variation, and what it is not.**

$$
\frac{\delta S_{\mathrm{trunc}}}{\delta\bar a^{\nu}}=0
\qquad\Longleftrightarrow\qquad
\bigl(\pi^{2}-k_m^{2}w\bigr)a^{\nu}-\pi^{\nu}(\pi\cdot a)-K^{\nu}{}_{\mu}a^{\mu}=0 .
$$

**This is four algebraic equations**, and it is the order-$\epsilon^{-2}$ group of the equation's route with the mass's frame factor made explicit. **Its Hessian is minus the Fourier companion's symbol**, with $k$ replaced by $\pi$ and with the mass's $w$:

$$
\frac{\partial^{2}S_{\mathrm{trunc}}}{\partial\bar a^{\mu}\,\partial a^{\nu}}
=\pi_{\mu}\pi_{\nu}-\bigl(\pi^{2}-k_m^{2}w\bigr)\eta_{\mu\nu}-K_{\mu\nu},
$$

whose trace is $-3\pi^{2}+4k_m^{2}w$ — a number the article records and does not use, because the trace of a matrix is not the trace of an equation.

**The real projection, which is the eikonal.** Multiplying by $\bar a_\nu$ and taking the real part, the curvature term drops because $K$ is antisymmetric and $\bar aKa$ is pure imaginary:

$$
\bigl(\pi^{2}-k_m^{2}w\bigr)\lvert a\rvert^{2}=\lvert\pi\cdot a\rvert^{2}.
$$

**That is the mass shell corrected by the longitudinal part at relative order $\epsilon^{2}$**, and it is the variational counterpart of the companion's statement that the eikonal is the amplitude equation's real projection. **Set the longitudinal part to zero and it is $\pi^{2}=k_m^{2}w$.**

**The phase's variation, which is the Gauss law.**

$$
\frac{\delta S_{\mathrm{trunc}}}{\delta\vartheta_{\mathrm{pha}}}=0
\qquad\Longleftrightarrow\qquad
\partial_\mu\Bigl[(\pi\cdot a)a^{\mu}-\pi^{\mu}\lvert a\rvert^{2}\Bigr]=0 .
$$

**Two terms and two meanings.** The second is the transport current $\pi^{\mu}\lvert a\rvert^{2}$; the first is the longitudinal part's contribution, which vanishes when the constraint holds and is otherwise the correction the redundancy absorbs. **With $\pi\cdot a=0$ the display is exactly the companion's covariant transport equation**, so the variational route derives the transport and the equation's route derives it too, and the two derivations agree because both are the same redundancy read once.

**Why it is a Gauss law and not an equation of motion.** The symmetry being varied is the decomposition's redundancy — shifting the phase by a constant and rotating the amplitude leaves the field unchanged — and it is exact at every order of the full action, not only in the truncation. **A conservation law belonging to a redundancy constrains and does not propagate**, which is why it survives a truncation that deletes every derivative of the amplitude.

**The constraint itself, and where it comes from.** $\pi\cdot a=0$ is the covariant Lorenz condition at leading order, and the parent's polar companion states that the trace of the equation is exactly that condition and that the frame's brackets do not enter it. **In this article it enters as the statement that the longitudinal part is what the redundancy can absorb**, not as an extra Lagrange multiplier: the parent's parameterisation already absorbs the unit conditions, and the redundancy absorbs the longitudinal mode. **That is the chart's own account of why the count is three and not four.**

## The Amplitude Stops Being Dynamical

**Four momenta vanish, for the same reason as in the free case.** $S_{\mathrm{trunc}}$ contains no derivative of $a$, so

$$
p_{a^{\nu}}=\frac{\partial\mathcal{L}_{\mathrm{trunc}}}{\partial(\partial_{t'}a^{\nu})}=0 ,
$$

and the amplitude is algebraic. **The count is the same as the free companion's and the interpretation is sharper**: off the shell the Hessian's determinant is $-k_m^{2}(\pi^{2}-k_m^{2}w)^{3}$ up to the curvature's traceless correction, so there is no non-trivial solution; on the shell the rank falls and the kernel is the polarisation plane.

**The curvature does not change the rank, and the reason is the trace.** $K$ is traceless and antisymmetric, so it shifts the three equal eigenvalues of $\pi_{\mu}\pi_{\nu}-(\pi^{2}-k_m^{2}w)\eta_{\mu\nu}$ without creating or destroying the vanishing at $\pi^{2}=k_m^{2}w$. **The count is three with or without the field**, and what the field changes is the directions. **A traceless perturbation cannot change a rank that is produced by a mass factor, and that is the whole of the statement.**

**The phase is the only dynamical field.** Its momentum is $\lvert a\rvert^{2}$ times the temporal component of the current, the eikonal is a first-order equation for it, and the transport fixes the density along the rays. **The limit demotes the amplitude to a polarisation and promotes the phase**, exactly as in the free companion, and the coupling changes neither half of that sentence.

## What the Variational Route Adds

**Adds.**

- The criterion as the ratio of the dropped group to the kept one, $\epsilon^{2}$, with no sensitivity argument and no reference to a chart that cannot be ordered.
- The statement that the truncation is gauge invariant because it is a functional of $\pi$ alone, which is why the criterion had to be written on the mechanical gradient: the two facts are one fact.
- The identification of the truncated Hessian with the Fourier companion's symbol, so the count is a rank and the curvature's role is a traceless shift.
- The transport equation as a Gauss law of the decomposition's redundancy, with the longitudinal correction displayed.
- The mass's frame factor $w$ in its proper place, as a coefficient of order zero rather than as a correction.

**Does not add.**

- No settlement of the parent's open item. The parent does not assert that the chart's Hessian is non-degenerate, and this article's Hessian is the truncated one.
- No statement about the field term's normalisation, which the element-form companion owns.
- No derivation of the covariant Lorenz condition, which the polar companion supplies and this article uses.

**The one contrast with the free variational companion worth naming.** There the mode had to be introduced, because the free chart's fast scale is in the modulus and the criterion on the parent's own plane wave is $\lvert\tan\theta_{\mathrm{pwp}}\rvert$. **Here no such step exists**: the coupled chart carries a phase, the criterion on the parent's own word is $\epsilon=1/(k_\pi L)$ with $k_\pi=\lvert\vec\pi\rvert/\hbar$, and the limit is a statement about the parent's variables as they stand. **The coupling that made the field complex made the limit available**.

## Summary

The parent's action is a quadratic form in eight gradients with a metric the connection cannot enter, plus a mass potential whose frame dependence the parent measures ($0.7648$ independent of rapidity for collinear axes; $0.7648$, $0.7010$, $0.4401$ at rapidities $0$, $1$, $2$ for perpendicular ones). Because the phase and the potential enter the covariant derivative only through the mechanical momentum $\pi_\mu=\hbar\partial_\mu\vartheta_{\mathrm{pha}}+ϙA_\mu$, the truncation must be written on $\pi$, and written so it is gauge invariant exactly.

The truncation deletes the two-derivative group, whose ratio to the leading one is $\epsilon^{2}$ and which carries no phase. The truncated action, $\int\tfrac12[\lvert\pi\cdot a\rvert^{2}-\pi^{2}\lvert a\rvert^{2}+k_m^{2}w\lvert a\rvert^{2}]+\tfrac12\bar a_\nu K^{\nu}{}_\mu a^{\mu}$, is algebraic in the amplitude. Its amplitude variation is the order-zero system, whose real projection is $\pi^{2}-k_m^{2}w=\lvert\pi\cdot a\rvert^{2}/\lvert a\rvert^{2}$ — the mass shell corrected by the longitudinal part at order $\epsilon^{2}$ — and whose Hessian is minus the Fourier companion's symbol with a traceless curvature shift. Its phase variation is $\partial_\mu[(\pi\cdot a)a^{\mu}-\pi^{\mu}\lvert a\rvert^{2}]=0$, the Gauss law of the decomposition's redundancy, which is the covariant transport once the constraint holds. The amplitude stops being dynamical, four momenta vanish, the curvature shifts the polarisation directions without touching the rank, and the count is three. The parent's open item about the chart's own Hessian is not needed, and is left open.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde A=r e^{i\vartheta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The parent's four-factor word; eight parameters |
| $\tfrac12\sum_\mu G^{ab}(q)\partial_\mu q_a\partial_\mu q_b$ | The chart's kinetic term; the connection cannot enter $G$ |
| $w=\mathrm{Sc}(\tilde A^{*}\tilde A^{\natural})/r^{2}$ | The mass's frame factor; $1$ with the rotor trivial |
| $\pi_\mu=\hbar\partial_\mu\vartheta_{\mathrm{pha}}+ϙA_\mu$ | The mechanical momentum; the truncation's variable |
| $\tfrac12[\lvert\pi\cdot a\rvert^{2}-\pi^{2}\lvert a\rvert^{2}+k_m^{2}w\lvert a\rvert^{2}]+\tfrac12\bar a_\nu K^{\nu}{}_\mu a^{\mu}$ | The truncated density |
| $K^{\nu}{}_{\mu}=\frac{iϙ}{\hbar}F^{\nu}{}_{\mu}$ up to sign | The curvature's matrix; antisymmetric and traceless |
| $\pi_{\mu}\pi_{\nu}-(\pi^{2}-k_m^{2}w)\eta_{\mu\nu}-K_{\mu\nu}$ | The truncated Hessian |
| $(\pi^{2}-k_m^{2}w)\lvert a\rvert^{2}=\lvert\pi\cdot a\rvert^{2}$ | The amplitude variation's real projection |
| $\partial_\mu[(\pi\cdot a)a^{\mu}-\pi^{\mu}\lvert a\rvert^{2}]=0$ | The phase variation; the Gauss law |
| $p_{a^{\nu}}=0$ | The four primary constraints the truncation creates |
| $\epsilon=1/(k_\pi L)=\hbar/(\lvert\vec\pi\rvert L)$ | The criterion; the only gauge-invariant choice |

## Further Reading

- Alexandru Proca, "Sur la théorie ondulatoire des électrons positifs et négatifs," *Journal de Physique et le Radium* **7** (1936) 347–353, for the equation and its constraint.
- Paul A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for constraint analysis and the counting of momenta that vanish identically.
- Ludwig D. Faddeev and Victor N. Popov, "Feynman diagrams for the Yang–Mills field," *Physics Letters B* **25** (1967) 29–30, for a Gauss law treated as the conservation of a redundancy.
- G. B. Whitham, *Linear and Nonlinear Waves* (Wiley, 1974), chapter 11, for the averaged Lagrangian of a real wave and the algebraic amplitude it produces.
- Michael V. Berry and K. E. Mount, "Semiclassical approximations in wave mechanics," *Reports on Progress in Physics* **35** (1972) 315–397, for the eikonal and transport equations as the variations of a truncated action.
- Claude Itzykson and Jean-Bernard Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), §3-2, for the degrees of freedom of a massive vector field and the singular massless limit.
