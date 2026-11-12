# __The Variational Principle and the Coupled Dirac Equation in Biquaternionic Form__

## Introduction

This article states the action whose Euler–Lagrange equations are the coupled Dirac equation, and it reads what the action's symmetries give. It is the element-form companion of *The Variational Principle and the Dirac Equation in Biquaternionic Form*, and it is the first of two coupled variational articles. The second substitutes the polar word into the action of this article and reads the constraint structure.

**The equation.** The coupled pair is

$$
\tilde\nabla_{\mathrm{gco}}\tilde\Xi_R=k_m\tilde\Xi_L,
\qquad
\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\Xi_L=k_m\tilde\Xi_R,
\qquad
\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_\Phi,
$$

with the connection in the material sector $\mathbb{B}_\Phi$ and with central scalar coefficients in the abelian case.

**Three things are established.**

*First, the action and its variation.* One functional, two residuals, and the pair. The mass term is the only term that couples the two parts, and the count of equations is the parent's count.

*Second, the coupling is derived and not postulated.* The action has a local central phase symmetry only when the gradient is replaced by the covariant derivative; the connection absorbs exactly the derivative of the phase and nothing else. Minimal coupling is therefore the answer to a question asked of the action, and the question cannot be asked of the element *equation* alone: the equation accepts any operator, and only the functional decides which operator is admissible.

*Third, the current is settled.* The local phase's Noether current is conserved on solutions, and it is the pairing with two fixed frame units that the element form states and the Gordon article identifies. The naive bilinear $i\tilde\Xi\tilde\Xi^{*}$ is gauge invariant, is of the density sign, and is not conserved. The action does not produce it and the equation does not conserve it. The positive statement and the counterexample are both in §*The Current: What the Action Produces and What It Does Not*.

**The two settings.** The action is stated for a connection that may depend on the coordinates. The two settings of the framework are distinct and are kept apart here. In the constant setting the connection is a fixed element of $\mathbb{B}_\Phi$ with constant coefficients; the equation becomes algebraic in momentum space, the propagator is a finite product of exponentials up to the gauge factor, and a constant potential is pure gauge. In the operator setting the connection is an operator or a general function of position; the equation is a partial differential equation, the propagator is not a finite product, and the variational principle is the standard field-theoretic one. The article computes in the constant setting and states where the operator setting differs. Nothing is transferred between them.

## The Coupled Action

The free action of the parent article is

$$
S_0=\frac{\hbar c}{2}\int\mathrm{d}^{4}r\;\mathrm{Re}\,\mathrm{Sc}\Bigl[\tilde\Xi_L^{*}\tilde\nabla_\Phi^{\natural}\tilde\Xi_L+\tilde\Xi_R^{*}\tilde\nabla_\Phi\tilde\Xi_R-k_m\bigl(\tilde\Xi_L^{*}\tilde\Xi_R+\tilde\Xi_R^{*}\tilde\Xi_L\bigr)\Bigr],
$$

with $\mathrm{d}^4r=\mathrm{d}r'_t\,\mathrm{d}^{3}r$. The coupled action is the same functional with the two gradients replaced by the two covariant operators:

$$
\boxed{\;
S=\frac{\hbar c}{2}\int\mathrm{d}^{4}r\;\mathrm{Re}\,\mathrm{Sc}\Bigl[\tilde\Xi_L^{*}\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\Xi_L+\tilde\Xi_R^{*}\tilde\nabla_{\mathrm{gco}}\tilde\Xi_R-k_m\bigl(\tilde\Xi_L^{*}\tilde\Xi_R+\tilde\Xi_R^{*}\tilde\Xi_L\bigr)\Bigr]\;}
$$

with $\tilde\nabla_{\mathrm{gco}}^{\natural}=(\tilde\nabla_\Phi)^{\natural}+\frac{i\,ϙ}{\hbar}\tilde A_\Phi^{\natural}$.

**The two kinetic terms carry different operators, and that is the parent's arrangement.** The left part carries the conjugate and the right part carries the operator, so the two differ in the sign of the spatial derivative and in the sign of the connection's spatial slots. That arrangement is what makes the two spatial derivatives conjugate to each other, which is what the two-component structure of the equation requires.

**The potential enters the two terms with opposite entries.** Expanding the two kinetic terms,

$$
\mathrm{Sc}\Bigl[\tilde\Xi_L^{*}\bigl((\tilde\nabla_\Phi)^{\natural}+\tfrac{iϙ}{\hbar}\tilde A_\Phi^{\natural}\bigr)\tilde\Xi_L+\tilde\Xi_R^{*}\bigl(\tilde\nabla_\Phi+\tfrac{iϙ}{\hbar}\tilde A_\Phi\bigr)\tilde\Xi_R\Bigr],
$$

the left part sees $\tilde A_\Phi^{\natural}$ and the right part sees $\tilde A_\Phi$. For a purely electric potential the two entries are equal and the two parts are pushed the same way; for a purely magnetic one they are opposite and the two parts are pushed opposite ways. The asymmetry is not a choice: it is the conjugate operator's, and the conjugate operator is what the left part's kinetic term has.

**Reality.** Each kinetic term is self-adjoint for the Hermitian pairing, and the argument is the parent's: the temporal slot of each covariant component is $-i\partial_{r'_t}+\frac{iϙ}{\hbar}A_t$, which is a central imaginary operator and antisymmetric for $\mathrm{Sc}(\cdot^{*}\cdot)$, so the two signs cancel under integration by parts; each spatial slot is $\partial_\eta+\frac{iϙ}{\hbar}A_\eta$, which is a real-derivative-plus-imaginary-multiplication and is self-adjoint for the same reason. The mass terms are Hermitian because they pair one part with the conjugate of the other. Hence the bracket's imaginary part is a total divergence, the real part carries the content, and the integral is real on fields of compact support.

**The connection's contribution to reality is nil, and that is not an accident.** A central complex number multiplying the field multiplies the pairing by its modulus squared in each term, so the potential's contribution to the reality of the action cancels between the field and its conjugate. What the potential does to the action is not realness but *local invariance*, which is §*Why the Coupling Is Forced*.

**The constant $\hbar c$.** It multiplies the whole functional, it cancels in the variation, and the residuals do not carry it while the currents carry one power of it. The parent's reason for the convention is unchanged by the coupling.

## Why the Coupling Is Forced

The action's free part is invariant under a *constant* central phase. Localizing the phase destroys the invariance, and the repair is unique.

**The mass term is safe.** Under $\tilde\Xi\mapsto\lambda\tilde\Xi$ with $\lambda=\lambda(R)$ central, the mass term $\tilde\Xi_L^{*}\tilde\Xi_R$ becomes $\bar\lambda\lambda\,\tilde\Xi_L^{*}\tilde\Xi_R=\tilde\Xi_L^{*}\tilde\Xi_R$, since $\lambda$ commutes and has unit modulus. A mass term linear in two fields with one conjugate is invariant under a local central phase without any help.

**The kinetic term is not.** The derivative acts on $\lambda$:

$$
\tilde\Xi_L^{*}\tilde\nabla_\Phi^{\natural}\bigl(\lambda\tilde\Xi_L\bigr)
=\lambda\,\tilde\Xi_L^{*}\tilde\nabla_\Phi^{\natural}\tilde\Xi_L
+\tilde\Xi_L^{*}\bigl(\tilde\nabla_\Phi^{\natural}\lambda\bigr)\tilde\Xi_L,
$$

and the second term is nonzero. The obstruction is therefore the derivative and only the derivative.

**The repair is unique within the abelian class.** Demand that the action be invariant under $\tilde\Xi\mapsto\lambda\tilde\Xi$ with $\tilde A_\Phi\mapsto\tilde A_\Phi+\delta\tilde A_\Phi$. The kinetic terms acquire

$$
\frac{i\,ϙ}{\hbar}\Bigl(\tilde\Xi_L^{*}\bigl(\tilde\nabla_\Phi^{\natural}\Gamma\bigr)\tilde\Xi_L+\tilde\Xi_R^{*}\bigl(\tilde\nabla_\Phi\Gamma\bigr)\tilde\Xi_R\Bigr)
+\frac{i\,ϙ}{\hbar}\Bigl(\tilde\Xi_L^{*}\delta\tilde A_\Phi^{\natural}\tilde\Xi_L+\tilde\Xi_R^{*}\delta\tilde A_\Phi\tilde\Xi_R\Bigr),
$$

and the two brackets cancel for every field exactly when $\delta\tilde A_\Phi=-\tilde\nabla_\Phi\Gamma$, that is, when the connection obeys the gauge law with the sign the element companion uses. **The covariant derivative is the unique repair of this shape**, and the sign of the coupling is fixed by the sign of the gauge law. No further term can be added: a term without a derivative would have to be a function of $\tilde A_\Phi$ alone, and such a term is not invariant under the shift of the connection.

**What this settles that the equation alone could not.** The coupled equation can be written down with any operator in place of the gradient, and every such equation is an equation. Only the functional selects the operator whose equation is *the* equation of a locally phased field. The variational principle therefore does real work here: it converts "couple by this prescription" into "the prescription is what local invariance requires".

**What it does not settle.** The repair is unique *within the abelian class* and up to terms of higher order in the field strength. A term built from $\tilde F$ alone is invariant and cannot be excluded by this argument; it is the gauge field's own action and belongs to the Maxwell article, not to the matter action. The argument also says nothing about non-abelian connections, where $\tilde A_\Phi$ does not commute with the field and the two terms above do not separate.

## The Variation

Vary both parts and take the real part. The result is

$$
\delta S=\hbar c\,\mathrm{Re}\int\mathrm{d}^{4}r\;\Bigl[\mathrm{Sc}\bigl(\delta\tilde\Xi_L^{*}\,r_L\bigr)+\mathrm{Sc}\bigl(\delta\tilde\Xi_R^{*}\,r_R\bigr)\Bigr],
$$

with the two residuals

$$
r_L=\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\Xi_L-k_m\tilde\Xi_R,
\qquad
r_R=\tilde\nabla_{\mathrm{gco}}\tilde\Xi_R-k_m\tilde\Xi_L .
$$

Stationarity for every variation of compact support is $r_L=r_R=0$, which is the coupled pair.

**The coefficient, once.** Varying $\tilde\Xi_R^{*}$ gives $\frac{\hbar c}{2}\mathrm{Re}\int\mathrm{Sc}[\delta\tilde\Xi_R^{*}\tilde\nabla_{\mathrm{gco}}\tilde\Xi_R]$; varying $\tilde\Xi_R$ gives the same expression again after the operator is moved to the other slot by self-adjointness. The two halves add, the $\frac12$ cancels, and the coefficient is $\hbar c$. The coupling does not change the argument, because the connection's contribution to the two halves is the same central number in both.

**The count.** Each residual is an element of $\mathbb{B}$ with eight real components, so the pair is sixteen real equations on sixteen real unknowns. The compatibility condition is obtained by applying $\tilde\nabla_{\mathrm{gco}}^{\natural}$ to the first residual and using the second:

$$
\Bigl(\sum_\mu\tilde\nabla_{\mathrm{gco},\mu}^{2}+\frac{i\,ϙ}{\hbar}\tilde F-k_m^{2}\Bigr)\tilde\Xi_R=0,
$$

the covariant wave equation with the curvature term. The coupling therefore changes the compatibility condition in exactly one place, the curvature, and nowhere else.

**Boundary terms.** The variation of a field of compact support produces none. For fields periodic in the spatial directions no boundary term appears either, provided the gauge function is periodic; a non-periodic gauge function changes the boundary data and the action is then stationary only within a gauge class. That is the standard statement and the coupling does not alter it.

## The Current: What the Action Produces and What It Does Not

The local phase is a symmetry of the coupled action, so it has a Noether current. This section states the current, states what the algebra does *not* hand over with it, and states the repair.

**The Noether computation.** Take $\tilde\Xi\mapsto e^{i\alpha(R)}\tilde\Xi$ with $\alpha$ a local central angle and with the connection held fixed. The mass term contributes nothing, as §*Why the Coupling Is Forced* shows. The kinetic terms contribute $-\int(\partial_\mu\alpha)J^{\mu}$, and the current is the parent's:

$$
J^{t}=\mathrm{Re}\,\mathrm{Sc}\Bigl[\tilde\Xi_L^{*}\tilde\Xi_L+\tilde\Xi_R^{*}\tilde\Xi_R\Bigr],
\qquad
J^{\eta}=\mathrm{Re}\,\mathrm{Sc}\Bigl[i\Bigl(\tilde\Xi_R^{*}\vec e_\eta\tilde\Xi_R-\tilde\Xi_L^{*}\vec e_\eta\tilde\Xi_L\Bigr)\Bigr],
$$

with $\partial_\mu J^{\mu}=0$ on solutions. **The time component is a sum over the parts and the spatial component is a difference.** The difference is not an error and it is not a convention: the two parts carry conjugate spatial derivatives, and a current built from them inherits the relative sign.

**The three writings are one object.** The display above, the polar reading $J^{t}=\rho\cosh\theta_{\mathrm{rpd}}$, $J^{\eta}=\rho\sinh\theta_{\mathrm{rpd}}u_{\mathrm b,\eta}$, and the Gordon pairing

$$
j_\mu=\mathrm{Sc}\bigl(\tilde\Xi^{*}\,i\,\bigl(i e_\mu\tilde\Xi\,\vec e_{\nu(\mu)}\bigr)\vec e_x\bigr),
\qquad
\nu(t)=x,\ \nu(\eta)=y,
$$

are the same four numbers. The first two agree by the parent polar article's evaluation on the word; the first and the third agree by a direct evaluation on a general element, slot by slot, once the letter assignment $\tilde\Xi_R=\tilde\Xi\Pi_-$, $\tilde\Xi_L=\tilde\Xi\Pi_+$ is fixed. **The action, the chart and the pairing therefore say the same thing three ways**, and the three-fold agreement is the strongest statement this article makes.

**What the algebra does not hand over.** The desired current is the one that transforms with the desired local symmetry, and §*Introduction* of the element companion states that desired transformation: a phase rotating at one rate and a boost at another, with the two parts of the field related by the boost. The Noether current of the action is conserved for the phase alone. So the action gives a conserved object and the question is whether it is the right one.

**The candidate that fails, and the reason it is tempting.** The obvious bilinear is

$$
\tilde J_{\Phi,\mathrm{sp}}=i\,\tilde\Xi\,\tilde\Xi^{*},
$$

the value-side product that *The Dirac Equation in Biquaternionic Form* builds. It is an element of $\mathbb{B}$, it is gauge invariant because the two phases cancel, its scalar part is the density with the density's sign, and its vector part is the current-like object the letter suggests. Every formal property except one is right.

**The one property that fails is conservation.** Evaluate the divergence on an exact solution — a superposition of two plane waves, so that the cross terms do not vanish by symmetry — and $\partial_{r'_t}\tilde J_{\Phi,\mathrm{sp}}^{\,t}+\sum_\eta\partial_\eta\tilde J_{\Phi,\mathrm{sp}}^{\,\eta}$ is nonzero, at the same order as the current itself. Evaluate the same divergence for the display above on the same field and it vanishes to machine precision. The difference is not small and it is not a boundary effect.

**Why it fails, in one sentence.** The product $\tilde\Xi\tilde\Xi^{*}$ carries the two parts with the *same* sign, and the conserved current carries them with *opposite* signs, because the two parts carry conjugate spatial derivatives.

**The repair, and what it costs.** The conserved current is not a product of the field with its conjugate. It is a pairing with one unit inserted between the two fields and one fixed frame unit on the right:

$$
j_\mu=\mathrm{Sc}\bigl(\tilde\Xi^{*}\,i\,\bigl(i e_\mu\tilde\Xi\,\vec e_{\nu(\mu)}\bigr)\vec e_x\bigr).
$$

The inner unit $e_\mu$ is what turns the product into a current, and the right multipliers are what give the two parts opposite signs: $\vec e_x$ maps one value sector to the other, and $\vec e_{\nu(\mu)}$ is the generator's own unit. Read in the older language, this is the adjoint row of the gamma formulation, and the Gordon companion shows the dictionary. **The current is a triple product, and the algebra supplies every factor of it.** No object outside $\mathbb{B}$ is needed and no second carrier is added.

**The residual gap, stated exactly.** What the action does not supply is the *choice of the two frame units*. The algebra contains the units and the scalar part, and it does not single out $\vec e_x$ and $\vec e_y$ as the ones the current uses. That choice is the frame's, made once with the basis, and inherited by every article in the corpus. It is a datum of the framework and not a consequence of its algebra: a different basis would give a different presentation of the same numbers, and the numbers would be the same. This is the honest residue of the current question, and it is smaller than the question the earlier version of this article recorded.

**Energy and momentum.** The Lagrangian does not depend explicitly on the coordinates when the connection is constant, so the four translations give four conserved charges with

$$
T^{\mu}{}_{\nu}=\sum_{p}\mathrm{Re}\,\mathrm{Sc}\Bigl[\tilde\Xi_p^{*}\,s_\mu e_\mu\,\tilde\nabla_{\mathrm{gco},\nu}\tilde\Xi_p\Bigr]-\delta^{\mu}_{\nu}\,\mathcal{L},
$$

and the gradient in the current is the covariant one. **When the connection depends on position the conservation is modified**: the divergence of the stress tensor is not zero but the Lorentz force density,

$$
\partial_\mu T^{\mu}{}_{\nu}=\frac{ϙ}{2}\,\mathrm{Re}\,\mathrm{Sc}\bigl[\tilde F_{\nu\mu}\,j^{\mu}\bigr],
$$

up to the normalization of the current, which is the statement that the matter stress tensor alone is not conserved in a background and that the field's own stress tensor takes up the difference. For a *static* background the total energy is conserved because the background does not change; for a general background only the total of matter and field is.

**What is deliberately absent.** There is no spin current in this section. The spin of this field is the rotor's, it is not a Noether current of the element action, and a spin current derived here would be a second derivation of something the polar companion states exactly. The Dirac spin current as a Noether current appears when the rotor is a variable of the action, which is the polar variational companion, and even there the coupling does not reach it.

## The Two Settings

**The constant setting.** $\tilde A_\Phi$ is a fixed element of $\mathbb{B}_\Phi$ with constant coefficients. The equation is algebraic in momentum space, the residual is linear with constant coefficients, and the solution is a finite product of exponentials up to the gauge factor:

$$
\tilde\Xi=\exp\Bigl(-i\frac{ϙ}{\hbar}\tilde A_\Phi\cdot R\Bigr)\tilde\Xi_{\mathrm{free}},
$$

with $\tilde\Xi_{\mathrm{free}}$ the free solution. The action's stationary points are the same set, and the value of the action on a solution is the free value, because a constant potential is pure gauge and the gauge factor's contribution cancels between the field and its conjugate.

**The closed-form propagator, and what it is not.** The propagator is a finite product of exponentials because the operator is a fixed element: the exponential of a fixed element can be computed by squaring, and no ordering problem arises. That is the whole reason the constant setting is closed, and it is the reason nothing in this setting transfers to the operator one.

**The operator setting.** $\tilde A_\Phi$ is a function of position or an operator, the covariant components do not commute with one another, and no finite product of exponentials gives the propagator. The variational principle is the standard field-theoretic one: the action is a functional on fields, stationarity is the equation, the Noether currents are the same display, and the stress tensor is the same tensor. What differs is that the currents are now functionals of a field that cannot be written in closed form, so their evaluation is a separate problem.

**The one statement that crosses is a negative one.** A constant potential opens no gap, and this is a statement about the constant setting. It does not say that no potential opens a gap; a non-constant potential with a non-vanishing field strength does, and the Landau-level article computes the spectrum for the constant magnetic field. The two statements are consistent and they are different statements.

**The loop phase and the flux.** The current's conservation on a closed surface is one consequence of the phase symmetry; the phase accumulated along a closed loop at fixed material time is another, and it is a property of the action's invariance rather than of the equations. In the constant setting the loop's phase is the holonomy $\exp(i\frac{ϙ}{\hbar}\oint\tilde A_\Phi\cdot\mathrm{d}l)$, and single-valuedness of the field requires the holonomy to be trivial, which is the flux quantum $\Phi=2\pi n\hbar/ϙ$ in the standard reading. **The framework's Wilson-loop construction reads the loop differently**, as the norm of a unit element rather than as the trace of a phase, and the two readings have not been reconciled in the corpus. The article records the tension rather than resolving it.

## What the Variational Principle Adds and What It Relabels

**Adds.**

- A derivation of the coupling rather than a prescription for it: the covariant derivative is the unique abelian repair of the localized phase, and the sign of the coupling follows from the sign of the gauge law.
- One current from one symmetry, in one computation, and the identification of three writings of it: the action's display, the chart's $\rho\tilde V_\Phi$, and the Gordon pairing.
- A sharp statement of what the naive bilinear fails to be, with the mechanism: the two parts enter a product with one sign and a current with two.
- The covariant stress tensor and its modified conservation, with the Lorentz force density as the compensating term.
- The status of the constant setting's closed form, and the statement that it does not transfer.

**Relabels.**

- No new prediction. The equation is the element companion's, and it is the standard minimally coupled Dirac equation.
- No new solution. The solutions are the plane waves of the constant setting and the standard field of the operator one.
- No new physical principle. The action is the standard first-order action written in the algebra.

**The distinction that matters.** The variational principle is integral in form and local in content: the functional is a functional on whole fields, and stationarity is a local differential equation. It is not opposed to the equation. What it is richer in is the *derivation*: an equation can be written with any operator, and only the functional says which operator belongs to a locally phased field.

## Open Questions

**The non-abelian action.** With a $\mathbb{B}$-valued connection the two kinetic terms no longer separate, because the connection does not commute with the field, and the reality argument has to be redone with the ordering explicit. Whether the resulting action is self-adjoint, and whether the Noether current is the covariant one, is the non-abelian article's subject and is not settled here.

**The choice of frame units in the current.** §*The Current* states the residue: the algebra does not single out $\vec e_x$ and $\vec e_y$. Whether the choice is forced by the requirement that the pairing be of a definite value, or whether it is a genuine datum of the framework, is not settled. A computation that derives the units from an invariance of the pairing would close it.

**The loop phase and the flux quantum.** The two readings of a closed loop — the trace of a holonomy and the norm of a unit element — give different statements about enclosed flux, and they have not been brought together. This is a corpus-level tension and not a question this article can settle.

**The operator setting's current.** The Noether current's conservation is an identity of the action and holds in both settings. What is not examined here is whether the operator-setting current, once renormalized, agrees with the element-form display order by order. That is a check and not a derivation, and it belongs with the stress-tensor article.

## Summary

The coupled action is the free action with the two gradients replaced by the two covariant operators,

$$
S=\frac{\hbar c}{2}\int\mathrm{d}^{4}r\;\mathrm{Re}\,\mathrm{Sc}\Bigl[\tilde\Xi_L^{*}\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\Xi_L+\tilde\Xi_R^{*}\tilde\nabla_{\mathrm{gco}}\tilde\Xi_R-k_m\bigl(\tilde\Xi_L^{*}\tilde\Xi_R+\tilde\Xi_R^{*}\tilde\Xi_L\bigr)\Bigr],
$$

and its variation gives the coupled pair. The mass term is invariant under a local central phase without help; the kinetic term is not; the repair is the covariant derivative with the gauge law's sign, and it is unique within the abelian class.

The local phase's Noether current is the parent's display, and it is one object with three writings: the action's two-part display, the chart's $\rho\cosh\theta_{\mathrm{rpd}}$ and $\rho\sinh\theta_{\mathrm{rpd}}u_{\mathrm b}$, and the Gordon pairing with two frame units. The time component is a sum over the parts and the spatial component is a difference, because the parts carry conjugate derivatives.

The naive bilinear $i\tilde\Xi\tilde\Xi^{*}$ is gauge invariant, of the density sign, and not conserved: it carries the two parts with one sign. The conserved current is a triple product, and the algebra supplies every factor. What the algebra does not supply is the choice of the two frame units, which is the frame's datum.

The covariant stress tensor is conserved when the connection is constant and its divergence is the Lorentz force density when the connection is not: matter alone is not conserved in a background.

The constant setting is closed — a finite product of exponentials up to the gauge factor, a constant potential pure gauge, the action's value on a solution the free value, and no gap. The operator setting is not closed and inherits none of it.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $S$ | The coupled action; functional on the pair $(\tilde\Xi_L,\tilde\Xi_R)$ |
| $\mathrm{d}^4r=\mathrm{d}r'_t\,\mathrm{d}^{3}r$ | Integration measure; $r'_t=ct'$ the material time |
| $\tilde\nabla_{\mathrm{gco}},\ \tilde\nabla_{\mathrm{gco}}^{\natural}$ | Covariant derivative and its $\natural$-image |
| $\tilde A_\Phi,\ \tilde F$ | Potential biquaternion and curvature |
| $\lambda=e^{iϙ\Gamma/\hbar}$ | Local central phase; $\Gamma$ real |
| $r_L,r_R$ | The two residuals; $r_L=r_R=0$ is the coupled pair |
| $\mathcal{L}$ | The Lagrangian density: the integrand of $S$ |
| $J^{t},J^{\eta}$ | Noether current of the local phase; sum over parts, difference over parts |
| $j_\mu$ | The same current as a pairing with two frame units |
| $\tilde J_{\Phi,\mathrm{sp}}=i\tilde\Xi\tilde\Xi^{*}$ | The naive bilinear: gauge invariant, density sign, **not conserved** |
| $T^{\mu}{}_{\nu}$ | Stress tensor; covariant gradient in the current |
| $\rho$ | Density; $\rho=r^{2}\cosh\theta_{\mathrm{rpd}}$ in the chart |
| $\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ | The frame's idempotents; $\tilde\Xi_R=\tilde\Xi\Pi_-$, $\tilde\Xi_L=\tilde\Xi\Pi_+$ |
| $s_\mu$ | Sign of the basis operator in the stress tensor's slot |

## Further Reading

- [The Variational Principle and the Dirac Equation in Biquaternionic Form](the-variational-principle-and-the-dirac-equation-in-biquaternionic-form.html), the free action this article couples.
- [The Coupled Dirac Equation in Biquaternionic Form](the-coupled-dirac-equation-in-biquaternionic-form.html), the equation the action reproduces.
- [The Coupled Dirac Equation in Biquaternionic Polar Variables](the-coupled-dirac-equation-in-biquaternionic-polar-variables.html), the equation in the chart.
- [The Variational Principle and the Coupled Dirac Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-coupled-dirac-equation-in-biquaternionic-polar-variables.html), the same action in the chart, and the constraints.
- [The Gordon Decomposition of the Dirac Current in Biquaternionic Form](the-gordon-decomposition-of-the-dirac-current-in-biquaternionic-form.html), for the pairing and the adjoint row's dictionary.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html), for the localization and the pair of signs.
- [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html), for the operator identity with the curvature.
- [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html), for the symmetric improvement and the operator-setting comparison.
- [Landau Levels in Biquaternionic Form](landau-levels-in-biquaternionic-form.html), for the spectrum a non-constant potential does produce.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the standard action, the Noether current and the stress tensor.
- Julian Schwinger, "On gauge invariance and vacuum polarization," *Physical Review* **82** (1951) 664–679, for the functional-derivative reading of the current.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the variational treatment of the Dirac action in geometric algebra.
