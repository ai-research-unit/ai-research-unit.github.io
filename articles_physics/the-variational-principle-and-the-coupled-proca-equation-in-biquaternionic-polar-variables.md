# __The Variational Principle and the Coupled Proca Equation in Biquaternionic Polar Variables__

## Introduction

This article substitutes the polar word into the coupled Proca action and reads what the substitution makes visible. It is the polar companion of *The Variational Principle and the Coupled Proca Equation in Biquaternionic Form*, it depends on *The Coupled Proca Equation in Biquaternionic Polar Variables* for the word and the brackets, and its free counterpart is *The Variational Principle and the Proca Equation in Biquaternionic Polar Variables*.

**The action and the substitution.** The element-form action is

$$
S[\tilde A,\tilde A^{*}]=\int d^{4}r\;\Bigl[\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)-\tfrac12\,k_m^{2}\,\mathrm{Sc}\bigl(\tilde A^{*}\tilde A^{\natural}\bigr)\Bigr],
$$

and the substitution is the four-factor word

$$
\tilde A=r\,e^{i\vartheta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\bigl(\theta_{\mathrm{rpd}},\hat u_{\mathrm b}\bigr)\,\tilde u_{\mathrm r}\bigl(\theta_{\mathrm{axr}},\hat u_{\mathrm r}\bigr),
$$

with eight real parameters. The word is a bijection onto the N-regular set, so the eight parameters are coordinates on the carrier's units and the substitution loses nothing and adds no constraint.

**Three findings.**

*First, the chart turns the action into a quadratic form in the eight gradients, with a field-dependent metric and a mass potential, and the connection enters as a shift of one gradient and of one only.* The metric is the chart's analogue of the free article's two brackets: it is built from the frame, and because the connection is a central scalar in every slot it cannot change the metric. That is the variational form of the polar companion's type statement, and it is why the coupling in this chart is a shift and not a rotation.

*Second, no Lagrange multiplier is needed for the unit conditions.* The word is exact, the frame is a unit by construction, and the phases and angles are coordinates rather than constrained variables. This is the contrast the guide draws with the tensor formulations, whose unit-vector conditions require three multipliers: here the parameterization absorbs them. What the parameterization does *not* absorb is the equation of motion of each coordinate, and those are the Euler–Lagrange equations.

*Third, the chart's system is second order and regular in form, and the article does not establish that its Hessian is non-degenerate.* The Proca field is second order in the material time, so no momentum vanishes identically and there is no primary constraint to exhibit. That is the structural difference from the Schrödinger and Dirac companions, whose actions are first order and whose charts expose six vanishing momenta. The article states the count, states the difference, and records the Hessian's regularity as an open item rather than asserting it.

**What is not here.** The element-form companion owns the field term's normalization question; this article uses the action as given. The equation, the covariant field strength and the covariant Lorenz condition are the polar companion's. This article's subject is the action in the chart, what the chart makes exact, and what it does not.

## The Action in the Chart

**The mass term is a function of the frame and the scale.** Substituting the word into the invariant length gives $r^{2}$ times a real function of the four frame angles: the central phase cancels between $\tilde A^{*}$ and $\tilde A^{\natural}$, the scale factors out, and what is left is a scalar part of the frame's four units.

**Two exact statements about it.** With the rotor trivial the function is one:

$$
\mathrm{Sc}\bigl(\tilde A^{*}\tilde A^{\natural}\bigr)=r^{2}
\qquad\text{when the rotor angle vanishes,}
$$

for every rapidity and every boost axis, to $10^{-14}$ over random draws. The reason is that the boost is a Lorentz transformation and the invariant length is Lorentz invariant.

With the rotor engaged the value departs from $r^{2}$, and how it departs separates two cases. If the rotor's axis is parallel or antiparallel to the boost's, the ratio $\mathrm{Sc}(\tilde A^{*}\tilde A^{\natural})/r^{2}$ is independent of the rapidity: for $\theta_{\mathrm{axr}}=0.7$ it is $0.7648$ at rapidity $0$, $2$ and $5$ alike. If the axes are perpendicular, the same angle gives $0.7648$, $0.7010$ and $0.4401$ at rapidity $0$, $1$ and $2$. The rotor is not a Lorentz transformation — it multiplies the frame from the right and it moves the four-vector's Minkowski square — and the rapidity can only matter where the two axes are not collinear.

**The field term is a quadratic form in the gradients.** Because the action is second order in the material time, the field term in the chart is a quadratic form

$$
\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)
=\tfrac12\sum_{\mu}G^{ab}(q)\,\partial_\mu q_a\,\partial_\mu q_b
+\text{(terms linear in the gradients and in the connection)},
$$

with $q$ the eight parameters, $G$ the chart's metric built from the frame, and the summation conventions of the material sector understood. The display is structural and the article does not write $G$ in full: its point is that the chart's kinetic term is a sigma-model-type form with a field-dependent metric, and that the metric is the object the free article's bracket table describes.

**Why the connection cannot change the metric.** The covariant derivative adds one central scalar per slot to the logarithmic derivative, and a central scalar is a multiple of the identity in the frame's own basis. The metric is built from the frame's brackets, which are the non-central parts, so the connection's share is orthogonal to it in the sense of types and cannot enter. The statement is exact and it is the variational form of the polar companion's table.

**The connection's only entry.** The action depends on the connection through the shift of the four-momentum, so in the chart

$$
\partial_\mu\vartheta_{\mathrm{pha}}\longmapsto\partial_\mu\vartheta_{\mathrm{pha}}+\frac{ϙ}{\hbar}A_\mu
$$

in the phase slot and in the phase slot alone, with the other seven parameters' gradients untouched. That is one substitution, in one coordinate, and it is what the classical $E\mapsto E+ϙc\,a'_t$, $\vec p\mapsto\vec p+ϙ\vec A$ becomes when the phase is a coordinate. The polar companion states the same thing as the identity $\hbar c\kappa_t=E+ϙca'_t$, $\hbar\vec\kappa=\vec p+ϙ\vec A$.

**No multipliers for the units.** The word carries the frame as an exact unit, so the condition $\tilde U\tilde U^{\natural}=1$ and the condition $\tilde u\tilde u^{\natural}=1$ are not constraints on the eight parameters; they are properties of the parameterization. A formulation in which the frame is a set of four vectors with a normalization condition would need multipliers for the normalization, and the polar formulation needs none, because the parameters are angles. That is the structural gain of the chart over a tensor formulation, and it is a gain in bookkeeping rather than in physics.

**The second-order structure.** The action is second order in the material time, so its Hessian with respect to the eight velocities is the metric $G$ and not a matrix with zero eigenvalues. That is the formal difference from the first-order companions: there the action is linear in the velocities, the Hessian has six zero eigenvalues, and the chart's Euler–Lagrange equations are a constrained system. Here there is no such degeneracy in form, and the chart's equations are eight second-order equations for eight parameters.

## The Euler–Lagrange Equations

**The count.** Eight parameters, eight equations, and each equation is second order. The two equations that the free article displays — one real equation for the modulus and one traceless equation for the frame — are the free case's reduction, and the coupling adds the connection's shift to the phase equation and to the others through it.

**The modulus equation.** The variation with respect to $r$ gives the equation whose free form is a Klein–Gordon equation with a source quadratic in the frame's connection. The coupling does not change its structure: $r$ is a real scalar, the connection is central, and the only effect is through the $\vartheta_{\mathrm{pha}}$ dependence that the phase's equation carries.

**The phase equation.** The variation with respect to $\vartheta_{\mathrm{pha}}$ is the chart's version of the constraint. It is not a constraint on the parameters: it is an equation of motion for the phase, and its content is the conservation of the object the phase's momentum is made of. That is the difference between this chart and the first-order charts, and the article states it plainly: in a first-order theory the phase's variation gives a *constraint*, because the phase's velocity appears linearly; in a second-order theory it gives an *equation*, because the phase's velocity appears squared and its momentum is a genuine momentum.

**The frame equations.** The variations with respect to the rapidity, the two boost angles, the rotor angle and the two rotor angles are the frame's equations. They are the chart's version of the traceless part of the element form's equation, they carry the curvature, and the article states their structure and not their explicit form: six equations, coupled through the metric, with the connection entering only through the phase.

**What the chart's equations do not do.** They do not turn the coupled Proca equation into a simpler system. They turn it into a system whose variables have physical names — scale, phase, rapidity, direction, rotation — and whose coupling is one shift. Whether that is a simplification is a question about what one wants to compute, and the article's answer is that it is a simplification for reading the coupling and not for solving the equation.

## The Gauge Transformation in the Chart

**The exact statement.** For a constant central unit $\lambda=\exp(i\vartheta_{\mathrm{gau}})$,

$$
\lambda\tilde A
=r\,e^{i(\vartheta_{\mathrm{pha}}+\vartheta_{\mathrm{gau}})}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
$$

exactly, with the other seven parameters fixed: the gauge transformation is the translation of one coordinate. The numerical check is exact to $10^{-16}$.

**The variational reading.** Because the action depends on the phase only through its gradient, a constant translation of the phase leaves it invariant, and a *local* translation is compensated by the connection's shift. The pair of statements is the chart's form of gauge invariance, and it is exact in the infinitesimal sense with no remainder: there is no multiplier, no gauge-fixing term, and no compensating field beyond the connection itself.

**The two-term structure of the invariance.** The mass term is invariant under a constant phase translation because it does not depend on the phase at all in the chart: the phase cancels in $\tilde A^{*}\tilde A^{\natural}$. The field term is invariant because it depends on the phase's gradient and a constant translation does not move a gradient. So in the chart the two invariants have visibly different reasons, and the element form's single computation splits into two.

**The range caveat.** A finite translation may carry $\vartheta_{\mathrm{pha}}$ outside $(-\pi/2,\pi/2]$, and the word's first factor is then not in the chart's normal form. The field is unaffected and the chart is; the article states the infinitesimal identity as the exact statement and records the range as a property of the coordinates. The polar companion makes the same remark for the same reason.

**What the chart does not need.** A Lagrange multiplier for the Lorenz condition. The condition is the trace of the equation and it is a consequence, not a constraint to be imposed, and in the chart it is the statement that the divergence of the word vanishes. A formulation that imposed it with a multiplier would be imposing an equation that the variation already gives, and the article records the redundancy rather than using it.

## The Currents in the Chart

**The charge is the momentum conjugate to the phase.** The action depends on $\vartheta_{\mathrm{pha}}$ only through its gradient, so the phase rotation is a symmetry and the Noether charge is the momentum conjugate to the phase:

$$
\varrho=\frac{\partial\mathcal{L}}{\partial(\partial_{r'_t}\vartheta_{\mathrm{pha}})}
=\mathrm{Sc}\bigl(\tilde A^{*}i\tilde\nabla_{\mathrm{gco},t}\tilde A\bigr),
$$

the temporal slot of the element form's current, by the chain rule and because the phase's generator on the field is multiplication by $i$. The identity is exact and it is the chart's cleanest statement about the current: the charge density is the momentum of the one coordinate that the gauge group translates, and no other coordinate's momentum contributes to it.

**The spatial slots.** The current's spatial components are the momenta conjugate to the phase's *gradients* in the same sense, and the conservation law is the statement that the four of them form a divergence-free object. The chart adds no new content here; it relocates the object to the phase's canonical pair.

**The energy–momentum in the chart.** The stress tensor's temporal slot is the Hamiltonian density, and in the chart it is the sum of the metric's quadratic form in the velocities and the mass potential. Its positivity is the positivity of the metric plus the positivity of the mass term on the material slice, and the article does not claim positivity for a general complex configuration: the metric's signature on the eight-dimensional parameter space is not established here, and it is the chart's version of the element form's open question about the trace.

**What is absent.** No spin current, for the reason the element-form companion gives: the frame's rotor is an internal rotation and not a spin density, and the free polar article exhibits the absence of a rotor bracket in the material sector. The rotor's return with the charge is the return of a frame, not of a spin.

## What the Polar Variational Principle Adds and What It Does Not

**Adds.**

- The exact form of the mass term in the chart, with the statement that it is $r^{2}$ precisely when the rotor is trivial, and the reason: the boost is a Lorentz transformation and the rotor is not.
- The statement that the connection enters the action as a shift of one gradient and cannot change the metric, which is the variational counterpart of the polar type table.
- The absence of Lagrange multipliers for the unit conditions, as a consequence of the word being exact.
- The charge as the momentum conjugate to the phase, in one line.
- The second-order, non-degenerate-in-form character of the chart's system, and the contrast with the first-order companions.

**Does not add.**

- No new solution and no new prediction: the action is the element form's, written in other coordinates.
- No simplification of the field term, whose algebraic normalization is the element-form companion's open question.
- No establishment of the Hessian's non-degeneracy on the whole N-regular set, and therefore no claim that the chart's system is regular everywhere.
- No constraint analysis, because there is no first-order degeneracy to analyse.

**The distinction that matters.** The first-order companions' charts expose a constrained system and their variational principles are constrained systems. This one does not, and the difference is the order of the field equation and not the choice of variables. The chart's genuine gain is that the coupling becomes a shift of one coordinate and the gauge group becomes one coordinate, and its genuine cost is that the equation becomes a contraction with a field-dependent frame.

## Open Questions

**The Hessian.** Whether the metric $G$ on the eight-dimensional parameter space is non-degenerate everywhere on the N-regular set — and if not, where it degenerates — is not established. The article states the count and the formal second-order structure and stops there.

**The metric's signature.** Positivity of the energy in the chart requires the metric's signature and the mass term's sign to cooperate. The mass term's sign is fixed on the material slice and its chart value is $r^{2}$ there; whether the general complex case has positive energy is open, and it is the chart's form of the element form's trace question.

**The field term's chart form.** The quadratic form's coefficients are not displayed. A future computation would give $G$ explicitly and would state which bracket each coefficient comes from; the article records the structure and not the table.

## Summary

The coupled Proca action in the polar variables is

$$
S=\int d^{4}r\;\Bigl[\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)-\tfrac12\,k_m^{2}\,R\bigl(\theta_{\mathrm{rpd}},\hat u_{\mathrm b},\theta_{\mathrm{axr}},\hat u_{\mathrm r}\bigr)\,r^{2}\Bigr],
$$

with $R$ the frame's own scalar, equal to one exactly when the rotor is trivial, independent of the rapidity when the two axes are collinear and dependent on it when they are not: a quadratic form in the eight gradients with a frame-built metric, a mass potential $Rr^{2}$, and a connection that shifts the phase's gradient and nothing else.

The chart needs no multipliers for the unit conditions, because the word is exact; the gauge transformation is the translation of the phase coordinate, exact infinitesimally; the charge is the momentum conjugate to that coordinate; and the system is second order, so the constrained-system structure of the first-order companions has no analogue here. What the chart does not do is simplify the field term or establish the regularity of its own metric, and the article says so.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde A=r\,e^{i\vartheta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The word: scale, phase, boost, rotor |
| $q=(\ln r,\vartheta_{\mathrm{pha}},\theta_{\mathrm{rpd}},\hat u_{\mathrm b},\theta_{\mathrm{axr}},\hat u_{\mathrm r})$ | The eight parameters |
| $r>0$ | Scale; $\langle\tilde A\rangle_\natural=r^{2}e^{2i\vartheta_{\mathrm{pha}}}$ |
| $\vartheta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$ | Central phase; the gauge coordinate |
| $\mathrm{Sc}(\tilde A^{*}\tilde A^{\natural})=R\,r^{2}$, $R(0)=1$ | The mass term in the chart; $R$ the frame's scalar |
| $G^{ab}(q)$ | The chart's metric; the coefficient of the kinetic form |
| $\tilde A_\Phi$, $A_\mu$ | The connection and its central components |
| $\tilde\nabla_{\mathrm{gco},\mu}=\partial_\mu+\frac{iϙ}{\hbar}A_\mu$ | The covariant derivative in the chart |
| $\partial_\mu\vartheta_{\mathrm{pha}}+\frac{ϙ}{\hbar}A_\mu$ | The one gradient the connection shifts |
| $\lambda=\exp(i\vartheta_{\mathrm{gau}})$ | Central gauge unit; translates $\vartheta_{\mathrm{pha}}$ |
| $\varrho=\partial\mathcal{L}/\partial(\partial_{r'_t}\vartheta_{\mathrm{pha}})$ | Charge density as the phase's conjugate momentum |
| $k_m=mc/\hbar$ | Mass wave number |
| $ϙ$ | Charge; a parameter |

## Further Reading

- [The Variational Principle and the Coupled Proca Equation in Biquaternionic Form](the-variational-principle-and-the-coupled-proca-equation-in-biquaternionic-form.html), the element form this article re-coordinatises.
- [The Coupled Proca Equation in Biquaternionic Polar Variables](the-coupled-proca-equation-in-biquaternionic-polar-variables.html), for the word, the type table and the momentum shift.
- [The Variational Principle and the Proca Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-proca-equation-in-biquaternionic-polar-variables.html), for the free action in the chart.
- [The Proca Equation in Biquaternionic Polar Variables](the-proca-equation-in-biquaternionic-polar-variables.html), for the free word, its branches and its two brackets.
- [The Variational Principle and the Coupled Dirac Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-coupled-dirac-equation-in-biquaternionic-polar-variables.html), for the first-order companion and its constrained system.
- [The Variational Principle and the Schrödinger Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-schrodinger-equation-in-biquaternionic-polar-variables.html), for the standard Madelung case and the contrast.
- [The Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html), for the word and its parameter count.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html), for the localization of the central phase.
- [Spin Hydrodynamics in Biquaternionic Form](spin-hydrodynamics-in-biquaternionic-form.html), for the frame's brackets as fluid variables.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor, the frame and the sigma-model reading of the kinetic term.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the standard coupled massive vector field.
