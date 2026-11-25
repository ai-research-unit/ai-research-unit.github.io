# __The Lagrangian and the Coupled Proca Equation in Polar Variables__

## Introduction

This article substitutes the complete polar decomposition into the coupled Proca action and reads what the substitution makes visible. It is the polar companion of *The Lagrangian and the Coupled Proca Equation*, it depends on *The Coupled Proca Equation in Biquaternionic Polar Variables* for the word and the brackets, and its free counterpart is *The Lagrangian and the Proca Equation in Polar Variables*.

The action and the substitution. The element-form action is

$$
S[\tilde A,\tilde A^{*}]=\int d^{4}r\;\Bigl[\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)-\tfrac12\,4\pi^{2}\nu_m^{2}\,\mathrm{Sc}\bigl(\tilde A^{*}\tilde A^{\natural}\bigr)\Bigr],
$$

and the substitution is the four-factor word

$$
\tilde A=\varrho\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\bigl(\theta_{\mathrm{rpd}},\hat u_{\mathrm b}\bigr)\,\tilde u_{\mathrm r}\bigl(\theta_{\mathrm{axr}},\hat u_{\mathrm r}\bigr),
$$

with eight real parameters. The word is a bijection onto the N-regular set, so the eight parameters are coordinates on the carrier's units and the substitution loses nothing and adds no constraint.

Three findings.

*First, the chart turns the action into a quadratic form in the eight gradients, with a field-dependent metric and a mass potential, and the connection enters as a shift of one gradient and of one only.* The metric is the chart's analogue of the free article's two brackets: it is built from the frame, and because the connection is a central scalar in every slot it cannot change the metric. That is the variational form of the polar companion's type statement, and it is why the coupling in this chart is a shift and not a rotation.

*Second, no Lagrange multiplier is needed for the unit conditions.* The word is exact, the frame is invertible by construction, and the phases and angles are coordinates rather than constrained variables. This is the contrast the guide draws with the tensor formulations, whose unit-vector conditions require three multipliers: here the parameterization absorbs them. What the parameterization does *not* absorb is the equation of motion of each coordinate, and those are the Euler–Lagrange equations.

*Third, the chart's system is second order and regular in form, and the article does not establish that its Hessian is non-degenerate.* The Proca field is second order in the material time, so no momentum vanishes identically and there is no primary constraint to exhibit. That is the structural difference from the Schrödinger and Dirac companions, whose actions are first order and whose charts expose six vanishing momenta. The article states the count, states the difference, and records the Hessian's regularity as an open item rather than asserting it.

What is not here. The element-form companion owns the field term's normalization question; this article uses the action as given. The equation, the covariant field strength and the covariant Lorenz condition are the polar companion's. This article's subject is the action in the chart, what the chart makes exact, and what it does not.

## Conventions

The conventions are the free chart's, restated for the coupled article. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_{\imath}^{2}=-e_t$; the word is $\tilde A=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde u$, with $\varrho>0$ and $\tilde u$ a unit element of the frame; the connection is $\tilde A_\Phi$ with real components $A_{\imath}$ and the coupling is $ϙ$. The pairing and the measure are those of the free chart, $\nu_m=\frac{mc}{h}$, and the two settings are the parent's.

## The Action in Polar Variables

The mass term is a function of the frame and the scale. Substituting the word into the invariant length gives $\varrho^{2}$ times a real function of the four frame angles: the central phase cancels between $\tilde A^{*}$ and $\tilde A^{\natural}$, the scale factors out, and what is left is a scalar part of the frame's four units.

Two exact statements about it. With the rotor trivial the function is one:

$$
\mathrm{Sc}\bigl(\tilde A^{*}\tilde A^{\natural}\bigr)=\varrho^{2}
\qquad\text{when the rotor angle vanishes,}
$$

for every rapidity and every boost axis, to $10^{-14}$ over random draws. The reason is that the boost is a Lorentz transformation and the invariant length is Lorentz invariant.

With the rotor engaged the value departs from $\varrho^{2}$, and how it departs separates two cases. If the rotor's axis is parallel or antiparallel to the boost's, the ratio $\mathrm{Sc}(\tilde A^{*}\tilde A^{\natural})/\varrho^{2}$ is independent of the rapidity: for $\theta_{\mathrm{axr}}=0.7$ it is $0.7648$ at rapidity $0$, $2$ and $5$ alike. If the axes are perpendicular, the same angle gives $0.7648$, $0.7010$ and $0.4401$ at rapidity $0$, $1$ and $2$. The rotor is not a Lorentz transformation — it multiplies the frame from the right and it moves the four-vector's Minkowski square — and the rapidity can only matter where the two axes are not collinear.

The field term is a quadratic form in the gradients. Because the action is second order in the material time, the field term in the chart is a quadratic form

$$
\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)
=\tfrac12\sum_{\imath}(G^{-1})_{ab}(q)\,\partial_{\imath} q_a\,\partial_{\imath} q_b
+\text{(terms linear in the gradients and in the connection)},
$$

with $q$ the eight parameters, $G$ the chart's metric built from the frame, and the summation conventions of the material sector understood. The display is structural and the article does not write $G$ in full: its point is that the chart's kinetic term is a sigma-model-type form with a field-dependent metric, and that the metric is the object the free article's bracket table describes.

Why the connection cannot change the metric. The covariant derivative adds one central scalar per slot to the logarithmic derivative, and a central scalar is a multiple of the identity in the frame's own basis. The metric is built from the frame's brackets, which are the non-central parts, so the connection's share is orthogonal to it in the sense of types and cannot enter. The statement is exact and it is the variational form of the polar companion's table.

The connection's only entry. The action depends on the connection through the shift of the four-momentum, so in the chart

$$
\partial_{\imath}\theta_{\mathrm{pha}}\longmapsto\partial_{\imath}\theta_{\mathrm{pha}}+\frac{2\pi ϙ}{h}A_{\imath}
$$

in the phase slot and in the phase slot alone, with the other seven parameters' gradients untouched. That is one substitution, in one coordinate, and it is what the classical $E\mapsto E+ϙc\,a'_t$, $\vec p\mapsto\vec p-q\vec A$ becomes when the phase is a coordinate. The polar companion states the same thing as the identity $\frac{h}{2\pi} c\kappa_t=E+ϙca'_t$, $\frac{h}{2\pi}\vec\kappa=\vec p-q\vec A$.

No multipliers for the normalisation. The word carries the frame as an exact unit, so the condition $\tilde U\tilde U^{\natural}=1$ and the condition $\tilde u\tilde u^{\natural}=1$ are not constraints on the eight parameters; they are properties of the parameterization. A formulation in which the frame is a set of four vectors with a normalization condition would need multipliers for the normalization, and the polar formulation needs none, because the parameters are angles. That is the structural gain of the chart over a tensor formulation, and it is a gain in bookkeeping rather than in physics.

The second-order structure. The action is second order in the material time, so its Hessian with respect to the eight velocities is the metric $G$ and not a matrix with zero eigenvalues. That is the formal difference from the first-order companions: there the action is linear in the velocities, the Hessian has six zero eigenvalues, and the chart's Euler–Lagrange equations are a constrained system. Here there is no such degeneracy in form, and the chart's equations are eight second-order equations for eight parameters.

The pairing. Inherited, and the connection is what the pairing now sees. The parent pairs the field term with $\mathrm{Re}\,\mathrm{Sc}(\cdot\cdot)$ and the mass term with $\mathrm{Sc}(\tilde A^{*}\tilde A^{\natural})$. The chart writes the vector as a density times a unit element and the connection as four components. The mass term is $\tfrac12\nu_m^{2}\varrho^{2}$ and is real; the field term's $\mathrm{Re}$ is still the explicit device that keeps it real.

The type of the coefficient. Two real coefficients and four bracket conditions. $\nu_m^{2}$ is real. The field term needs no coefficient beyond the metric, because $\mathrm{Re}$ does its work. The connection's four components must satisfy the reality of the covariant field term, which is a condition on their types and not on their size, and it is P1's.

The selection rule. The constraint is not a selection. The Proca action has no free potential. The Lorenz condition is a constraint from the variation of the field itself, which *The Constraints the Action Imposes* reads; a selection rule would be a statement about which potentials are admissible, and there are none.

**What reality does not buy. Reality does not enforce the constraint and does not sign the mass.** A real density is compatible with either sign of $\nu_m^{2}$ and with the constraint or without it. The constraint is the next section's; the sign of the conserved quantities is *The Noether Currents*'.

## The Variation: The Euler–Lagrange Equations

The count. Eight parameters, eight equations, and each equation is second order. The two equations that the free article displays — one real equation for the modulus and one traceless equation for the frame — are the free case's reduction, and the coupling adds the connection's shift to the phase equation and to the others through it.

The modulus equation. The variation with respect to $\varrho$ gives the equation whose free form is a Klein–Gordon equation with a source quadratic in the frame's connection. The coupling does not change its structure: $\varrho$ is a real scalar, the connection is central, and the only effect is through the $\theta_{\mathrm{pha}}$ dependence that the phase's equation carries.

The phase equation. The variation with respect to $\theta_{\mathrm{pha}}$ is the chart's version of the constraint. It is not a constraint on the parameters: it is an equation of motion for the phase, and its content is the conservation of the object the phase's momentum is made of. That is the difference between this chart and the first-order charts, and the article states it plainly: in a first-order theory the phase's variation gives a *constraint*, because the phase's velocity appears linearly; in a second-order theory it gives an *equation*, because the phase's velocity appears squared and its momentum is a genuine momentum.

The frame equations. The variations with respect to the rapidity, the two boost angles, the rotor angle and the two rotor angles are the frame's equations. They are the chart's version of the scalar-free part of the element form's equation, they carry the curvature, and the article states their structure and not their explicit form: six equations, coupled through the metric, with the connection entering only through the phase.

What the chart's equations do not do. **They do not turn the coupled Proca equation into a simpler system.** They turn it into a system whose variables have physical names — scale, phase, rapidity, direction, rotation — and whose coupling is one shift. Whether that is a simplification is a question about what one wants to compute, and the article's answer is that it is a simplification for reading the coupling and not for solving the equation.

The parameter basis and the four brackets. The material word has the same four types. The polar decomposition of the material sector is the same word with the same parameter ranges, so its logarithmic derivative has the same four brackets:

$$
\tilde A_\Phi^{-1}\partial\tilde A_\Phi
=\partial\ln\varrho+i\,\partial\theta_{\mathrm{pha}}+\tfrac12\partial\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}+\tfrac12\bigl(\partial\theta_{\mathrm{axr}}\,\vec u_{\mathrm r}+\ldots\bigr),
$$

with the scale real, the phase central imaginary, the boost Hermitian and the rotor a real vector. Nothing about the brackets is specific to the scalar field: they are a property of the parameterisation and of the algebra's type decomposition, and every element field carries them.

What is specific is the bilinear. The scalar field's action pairs $\tilde\Xi$ with itself through $\tilde\Xi^{*}\tilde\Xi$, which is a single type, so only the matching brackets survive. The Proca action is built from the square of the conjugate gradient and a square is not a modulus: it pairs the scalar part with the scalar part and the vector part with the vector part while keeping the cross term between them. The four brackets therefore enter with the full quadratic form of the conjugate gradient, and the antisymmetric combination the square keeps and the modulus would discard is exactly the object whose variation returns the Lorenz condition.

Why the pairing is the content of the constraint. The middle piece of the Proca Lagrangian, $-\tfrac12S^{2}$ with $S$ the scalar part of the conjugate gradient, is the cross term. It is zero on a solution the scalar action would already allow and non-zero off it; varying it gives the condition that kills the longitudinal scalar. The Proca action is not the scalar action with a mass: it is the scalar action's brackets with the pairing changed, and the changed pairing is where the constraint lives.

The parameter basis is not the bracket basis. As in the free polar article, the eight parameters are coordinates and the four brackets are types, and the Jacobian between them mixes the roles: the rapidity's derivative carries part of the scale bracket, the rotor's derivative part of the boost bracket. The parameter equations are the same equations in a rotated basis, and the brackets remain the form in which each object has one type and one partner.

What the coupling adds. The connection is central, so it passes through $\tilde A_\Phi^{-1}$ and adds $\frac{2\pi iϙ}{h}A_\Phi$ to the logarithmic derivative, with a real temporal slot and central imaginary spatial slots. It therefore reaches the scale and phase brackets, leaves the boost and rotor brackets alone, and — entering as a shift and not as a factor — does not change the type pairing that produces the constraint.
## The Constraints the Action Imposes: The Gauge Transformation in the Chart

The exact statement. For a constant central unit $\digamma_{\mathrm{gau}}=\exp(i\vartheta_{\mathrm{gau}})$,

$$
\digamma_{\mathrm{gau}}\tilde A
=\varrho\,e^{i(\theta_{\mathrm{pha}}+\vartheta_{\mathrm{gau}})}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
$$

exactly, with the other seven parameters fixed: the gauge transformation is the translation of one coordinate. The numerical check is exact to $10^{-16}$.

The variational reading. Because the action depends on the phase only through its gradient, a constant translation of the phase leaves it invariant, and a *local* translation is compensated by the connection's shift. The pair of statements is the chart's form of gauge invariance, and it is exact in the infinitesimal sense with no remainder: there is no multiplier, no gauge-fixing term, and no compensating field beyond the connection itself.

The two-term structure of the invariance. The mass term is invariant under a constant phase translation because it does not depend on the phase at all in the chart: the phase cancels in $\tilde A^{*}\tilde A^{\natural}$. The field term is invariant because it depends on the phase's gradient and a constant translation does not move a gradient. So in the chart the two invariants have visibly different reasons, and the element form's single computation splits into two.

The range caveat. A finite translation may carry $\theta_{\mathrm{pha}}$ outside $(-\pi/2,\pi/2]$, and the word's first factor is then not in the chart's normal form. The field is unaffected and the chart is; the article states the infinitesimal identity as the exact statement and records the range as a property of the coordinates. The polar companion makes the same remark for the same reason.

**What the chart does not need.** A Lagrange multiplier for the Lorenz condition. The condition is the trace of the equation and it is a consequence, not a constraint to be imposed, and in the chart it is the statement that the divergence of the word vanishes. A formulation that imposed it with a multiplier would be imposing an equation that the variation already gives, and the article records the redundancy rather than using it.

## The Structural Consequence: The Mass Term Is a Function of the Frame

In the chart the mass term loses the potential and keeps the frame. The element article's mass term is $\mathrm{Sc}(\tilde A^{*}\tilde A^{\natural})$, a bilinear of the complex potential. Substituting the word, the phases cancel inside the bilinear and what remains is

$$
\mathrm{Sc}\bigl(\tilde A^{*}\tilde A^{\natural}\bigr)=\varrho^{2}\,R(\text{frame}),
$$

with $R$ a function of the frame's angles alone. The scalar potential and the vector potential have become the scale and the frame, and the mass term depends on them only through the invariant length.

**The consequence, and it is the article's own.** Because the mass term carries no derivative, it cannot change the rank of the kinetic Hessian; because it depends on the frame, it is what makes the longitudinal direction massive. The two statements are the two halves of the Proca mechanism in this chart, and they are visible in one display: the Hessian is built from $\vec A=-\varrho\sinh\frac{\theta_{\mathrm{rpd}}}{2}\hat u_{\mathrm b}$ and the mass term from $\varrho^{2}R$.

The hand check. Set the frame to the identity, $\theta_{\mathrm{rpd}}=0$. Then $\vec A=0$, the Hessian vanishes, and the chart degenerates: the pure-scale configuration has no kinetic term at all. The mass term is still $\varrho^{2}R(1)$, so the configuration is a minimum of the potential and not a solution of the dynamics. That degeneration is the chart's way of saying that a Proca field with no vector part is not a field.

### The Reconstruction and Its Limits

The reconstruction is exact on a branch. The chart is a diffeomorphism from the parameter domain onto one branch of the material sector's N-regular set, so the word can be inverted there: the two norms give $\varrho$ and $\theta_{\mathrm{rpd}}$, the direction gives $\theta_{\mathrm{pha}}$, and the residual rotor gives $\theta_{\mathrm{axr}}$ and $\vec u_{\mathrm r}$. The inverse is the bijection read backwards and adds nothing to the action.

**The branch is an input and not an output.** This is the article's central qualification. The two branches differ by the sign of the algebraic mass term, $+\tfrac12\nu_m^{2}\varrho^{2}$ on the timelike one and $-\tfrac12\nu_m^{2}\varrho^{2}$ on the spacelike one, and **that sign is not a function of the eight parameters**. The chart is a chart on one branch; to move to the other the reader changes a discrete datum first and reconstructs afterwards. A reconstruction that claimed to recover the branch from the parameters would be claiming to recover a sign from a magnitude, and it cannot.

The scale's limit. $\varrho>0$ excludes the zero element, so a field that reaches $\varrho=0$ leaves the chart. For the Proca field that is not a pathology but a boundary: the mass shell's two branches meet only through the origin, and the origin is excluded.

The angle's limits. The rotor's angle must be closed at $2\pi$, or the word misses every element whose rotor factor is $-e_t$; the phase ranges over a half-open interval of length $\pi$, because the element and its negative are distinct while a shift by $\pi$ is not a symmetry of the action. Neither is a convention of this article; both are properties of the parameterisation it inherits.

What the reconstruction does not give. The flow. The bijection makes the variation the same variation, which is what the Euler–Lagrange section uses; it does not make the constrained system's flow the element equation's flow, and the article says so. The frame's reconstruction has a further weakness here: the mass term is a function of the frame, $R(\theta_{\mathrm{rpd}},\hat u_{\mathrm b},\theta_{\mathrm{axr}},\hat u_{\mathrm r})\varrho^{2}$, so the reconstructed frame is constrained by the potential and is not a free coordinate. That is not a defect of the map — it is the statement that the Proca field's frame is where the mass is extremal.

## The Noether Currents: The Currents in the Chart

The charge is the momentum conjugate to the phase. The action depends on $\theta_{\mathrm{pha}}$ only through its gradient, so the phase rotation is a symmetry and the Noether charge is the momentum conjugate to the phase:

$$
\rho_{\mathrm{chg}}=\frac{\partial\mathcal{L}}{\partial(\partial_{r'_t}\theta_{\mathrm{pha}})}
=\mathrm{Sc}\bigl(\tilde A^{*}i\tilde\nabla_{\mathrm{gco},\Phi,t}\tilde A\bigr),
$$

the temporal slot of the element form's current, by the chain rule and because the phase's generator on the field is multiplication by $i$. The identity is exact and it is the chart's cleanest statement about the current: the charge density is the momentum of the one coordinate that the gauge group translates, and no other coordinate's momentum contributes to it.

The spatial slots. The current's spatial components are the momenta conjugate to the phase's *gradients* in the same sense, and the conservation law is the statement that the four of them form a divergence-free object. The chart adds no new content here; it relocates the object to the phase's canonical pair.

The energy–momentum in the chart. The stress tensor's temporal slot is the Hamiltonian density, and in the chart it is the sum of the metric's quadratic form in the velocities and the mass potential. Its positivity is the positivity of the metric plus the positivity of the mass term on the material slice, and the article does not claim positivity for a general complex configuration: the metric's signs on the eight-dimensional parameter space are not established here, and it is the chart's version of the element form's open question about the trace.

**What is absent.** No spin current, for the reason the element-form companion gives: the frame's rotor is an internal rotation and not a spin density, and the free polar article exhibits the absence of a rotor bracket in the material sector. The rotor's return with the charge is the return of a frame, not of a spin.

## What the Principle Adds and What It Relabels: In the Polar Chart

Adds.

- The exact form of the mass term in the chart, with the statement that it is $\varrho^{2}$ precisely when the rotor is trivial, and the reason: the boost is a Lorentz transformation and the rotor is not.
- The statement that the connection enters the action as a shift of one gradient and cannot change the metric, which is the variational counterpart of the polar type table.
- The absence of Lagrange multipliers for the unit conditions, as a consequence of the word being exact.
- The charge as the momentum conjugate to the phase, in one line.
- The second-order, non-degenerate-in-form character of the chart's system, and the contrast with the first-order companions.

Does not add.

- No new solution and no new prediction: the action is the element form's, written in other coordinates.
- No simplification of the field term, whose algebraic normalization is the element-form companion's open question.
- No establishment of the Hessian's non-degeneracy on the whole N-regular set, and therefore no claim that the chart's system is regular everywhere.
- No constraint analysis, because there is no first-order degeneracy to analyse.

**The distinction that matters.** The first-order companions' charts expose a constrained system and their variational principles are constrained systems. This one does not, and the difference is the order of the field equation and not the choice of variables. The chart's genuine gain is that the coupling becomes a shift of one coordinate and the gauge group becomes one coordinate, and its genuine cost is that the equation becomes a contraction with a field-dependent frame.

## Open Questions

The Hessian. Whether the metric $G$ on the eight-dimensional parameter space is non-degenerate everywhere on the N-regular set — and if not, where it degenerates — is not established. The article states the count and the formal second-order structure and stops there.

The metric's signs. Positivity of the energy in the chart requires the metric's signs and the mass term's sign to cooperate. The mass term's sign is fixed on the material slice and its chart value is $\varrho^{2}$ there; whether the general complex case has positive energy is open, and it is the chart's form of the element form's trace question.

## Summary

The coupled Proca action in the polar variables is

$$
S=\int d^{4}r\;\Bigl[\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)-\tfrac12\,4\pi^{2}\nu_m^{2}\,R\bigl(\theta_{\mathrm{rpd}},\hat u_{\mathrm b},\theta_{\mathrm{axr}},\hat u_{\mathrm r}\bigr)\,\varrho^{2}\Bigr],
$$

with $R$ the frame's own scalar, equal to one exactly when the rotor is trivial, independent of the rapidity when the two axes are collinear and dependent on it when they are not: a quadratic form in the eight gradients with a frame-built metric, a mass potential $R\varrho^{2}$, and a connection that shifts the phase's gradient and nothing else.

The chart needs no multipliers for the unit conditions, because the word is exact; the gauge transformation is the translation of the phase coordinate, exact infinitesimally; the charge is the momentum conjugate to that coordinate; and the system is second order, so the constrained-system structure of the first-order companions has no analogue here. What the chart does not do is simplify the field term or establish the regularity of its own metric, and the article says so.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde A=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The word: scale, phase, boost, rotor |
| $q=(\ln \varrho,\theta_{\mathrm{pha}},\theta_{\mathrm{rpd}},\hat u_{\mathrm b},\theta_{\mathrm{axr}},\hat u_{\mathrm r})$ | The eight parameters |
| $\varrho>0$ | Scale; $\langle\tilde A\rangle_\natural=\varrho^{2}e^{2i\theta_{\mathrm{pha}}}$ |
| $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$ | Central phase; the gauge coordinate |
| $\mathrm{Sc}(\tilde A^{*}\tilde A^{\natural})=R\,\varrho^{2}$, $R(0)=1$ | The mass term in the chart; $R$ the frame's scalar |
| $(G^{-1})_{ab}(q)$ | The inverse of the chart's metric; the coefficient of the kinetic form |
| $\tilde A_\Phi$, $A_{\imath}$ | The connection and its central components |
| $\tilde\nabla_{\mathrm{gco},\Phi,\imath}=\partial_{\imath}+\frac{2\pi iϙ}{h}A_{\imath}$ | The covariant derivative in the chart |
| $\partial_{\imath}\theta_{\mathrm{pha}}+\frac{2\pi ϙ}{h}A_{\imath}$ | The one gradient the connection shifts |
| $\digamma_{\mathrm{gau}}=\exp(i\vartheta_{\mathrm{gau}})$ | Central gauge unit; translates $\theta_{\mathrm{pha}}$ |
| $\rho_{\mathrm{chg}}=\partial\mathcal{L}/\partial(\partial_{r'_t}\theta_{\mathrm{pha}})$ | Charge density as the phase's conjugate momentum |
| $\nu_m=\frac{mc}{h}$ | Mass wave number |
| $ϙ$ | Charge; a parameter |

## Further Reading

- [The Lagrangian and the Coupled Proca Equation](the-lagrangian-and-the-coupled-proca-equation.html), the element form this article re-coordinatises.
- [The Coupled Proca Equation in Biquaternionic Polar Variables](the-coupled-proca-equation-in-biquaternionic-polar-variables.html), for the word, the type table and the momentum shift.
- [The Lagrangian and the Proca Equation in Polar Variables](the-lagrangian-and-the-proca-equation-in-polar-variables.html), for the free action in the chart.
- [The Proca Equation in Biquaternionic Polar Variables](the-proca-equation-in-biquaternionic-polar-variables.html), for the free word, its branches and its two brackets.
- [The Lagrangian and the Coupled Dirac Equation in Polar Variables](the-lagrangian-and-the-coupled-dirac-equation-in-polar-variables.html), for the first-order companion and its constrained system.
- [The Lagrangian and the Schrödinger Equation in Polar Variables](the-lagrangian-and-the-schrodinger-equation-in-polar-variables.html), for the standard Madelung case and the contrast.
- [The Complete Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-complete-polar-decomposition-of-an-n-regular-biquaternion.html), for the word and its parameter count.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html), for the localization of the central phase.
- [Spin Fluid Mechanics in Biquaternionic Form](spin-fluid-mechanics-in-biquaternionic-form.html), for the frame's brackets as fluid variables.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor, the frame and the sigma-model reading of the kinetic term.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the standard coupled massive vector field.
