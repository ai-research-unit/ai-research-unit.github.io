# __The Lagrangian and the Proca Equation in Momentum Space__

## Introduction

The variational parent states its central structural fact in prose and this article puts a number on it. *The Lagrangian and the Proca Equation* writes the action $\mathcal{L}=\tfrac12\mathrm{Re}\,\mathrm{Sc}(\tilde F\tilde F)-\tfrac124\pi^{2}\nu_m^{2}\langle\tilde A_\Phi\rangle_\natural$, derives the equation, and then says the sentence the whole subject turns on: the mass term is the obstruction to gauge invariance. Shifting the potential by a gradient leaves the field term alone and moves the mass term, so the action has no gauge symmetry and the equation inherits a longitudinal part. The article says the obstruction is the presence of one term in the action. What it does not say is what the term costs.

The cost is $\tfrac12\nu_m^{2}\lvert A\rvert^{2}$ and it is the same number at every frequency. In momentum space the action at a mode is one quadratic form in the four amplitudes, and the form's coefficient along the four-wave-number is $\tfrac12\nu_m^{2}\lvert A\rvert^{2}$ — independent of $k^{2}$, independent of $\omega$, and equal to $0.245000000$ at $2\pi\nu_m=0.7$ for every frequency tested from $2\pi\nu_t'=0.5$ to $2.0$. That coefficient is the entire longitudinal action, and the article's first finding is that it is a constant of the mode.

The second finding is that gauge freedom is the vanishing of a coefficient and not the breaking of a symmetry. The constraint is the stationarity of the form along the wave number, and its coefficient is $\tfrac12\nu_m^{2}$; at $\nu_m=0$ the coefficient vanishes and the variation is identically satisfied. So the massless theory's gauge freedom is a zero coefficient in the quadratic form, and the massive theory's constraint is a non-zero one. The parent's prose and this sentence say the same thing, and the second is the one that can be computed.

The third finding is a primary constraint visible as an absent power of the frequency. The coefficient of $A_0^{2}$ in the form is $\tfrac12(\vec\nu_\Phi^{2}+\nu_m^{2})$, with no $\omega^{2}$ in it, and it therefore does not move when the frequency moves: $0.315000000$ at $2\pi\nu_t'=0.5$, $1.2$ and $2.0$. The three spatial coefficients move ($-0.145$, $+0.45$, $+1.73$). That asymmetry is the frequency-space form of "the second-order form carries a primary constraint", and it is why the count is four minus one.

The gradient of the form is $-\eta\,\sigma A$, verified to $2.1\times10^{-11}$ on a random amplitude at $2\pi\nu_t'=1.2$, so the momentum-space variational principle *is* the vanishing of the Proca symbol. The variational statement and the operator statement are one equation in two registers, and the form companion's determinant, rank and kernel are all statements about this form's Hessian.

There is no new solution, no new action and no new current. The action is the parent's, the form is its value at a mode, and what is added is the coefficient structure: the longitudinal constant, the absent frequency in the temporal slot, and the identification of the constraint's cost.

## Conventions

The algebra and the invertibles are those of *Algebra and Element Conventions*, the gradient those of *Operator and Calculus Conventions*, the products those of *Product and Form Conventions*, the two forms those of *Norm and Pairing Conventions*, the invertibles and the material time those of *Physics Units and Common Elements Conventions*. The transform is the one of *Derivatives, Fields and Transforms*, with the symbol rule

$$
\tilde\nabla_\Phi\longmapsto 2\pi i\tilde\Upsilon_\Phi ,
\qquad
\Box_\Phi\longmapsto k^{2} ,
\qquad
\tilde\Upsilon_\Phi=2\pi i\nu_t'e_t+2\pi\vec\nu_\Phi ,
\qquad
2\pi\nu_t'=\frac{\omega}{c},
\qquad
k^{2}=2\pi\nu_t'^{2}-2\pi\vec\nu_\Phi^{2}.
$$

The parent's action is quoted once and not re-derived:

$$
S=\int\mathrm{d}^4r\;\mathcal{L} ,
\qquad
\mathcal{L}=\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)-\tfrac12\,4\pi^{2}\nu_m^{2}\,\langle\tilde A_\Phi\rangle_\natural ,
\qquad
\tilde F=\mathrm{Vect}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr) .
$$

Replacing each derivative by its multiplier and each field by its transform, the density's transform is supported on the difference of the two wave numbers, so at a mode the action is

$$
S=\int\frac{\mathrm{d}^4k}{(2\pi)^4}\;\mathcal{Q}(A) ,
\qquad
\mathcal{Q}(A)=\tfrac12\Bigl([kA]^{2}-\bigl(k^{2}-4\pi^{2}\nu_m^{2}\bigr)\,A\!\cdot\!A\Bigr) ,
\qquad
[kA]=2\pi\nu_t'a_t'-2\pi\vec\nu_\Phi\cdot\vec a ,
$$

with $A\!\cdot\!A=-\lvert a_t'\rvert^{2}+\lvert\vec a\rvert^{2}$ the material form. **The first term is the field term and the second is the field term's transverse part together with the mass term**; the split is made below and matters.

The sign is the parent's and the article keeps it. Its normalisation fixes the relative sign of the two terms by requiring positive energy, and the overall sign of an action does not change its extremum. Every statement below is about a coefficient and a vanishing, so the overall sign drops out; the relative sign is the parent's and is not renegotiated.

$\partial\mathcal{Q}/\partial A_{\jmath}=-(\sigma A)_{\jmath}$ with $(\sigma A)_{\jmath}=(k^{2}-4\pi^{2}\nu_m^{2})A_{\jmath}-2\pi\nu_{\jmath}(k\cdot A)$, verified to $2.1\times10^{-11}$ at $2\pi\nu_t'=1.2$, $2\pi\vec\nu_\Phi=(0.3,0.2,0.1)$, $2\pi\nu_m=0.7$ on a random complex amplitude. So the momentum-space variational principle is $\sigma A=0$, and the form companion's matrix is this form's Hessian.

### The Constant-Coefficient Licence

The form is a form at one wave number only where the coefficients are constant. With a connection there is a form at a mode only for a constant connection, and the coupled companion treats that case.

The parent sets the Palatini form aside and the article follows it. A first-order form would have eight amplitudes and a pair of equations, and none of the coefficients above would be the coefficients of that form.

The relative sign of the two terms is the parent's, fixed by positive energy. The article's coefficients are quoted with that sign, and a reader who uses the opposite convention will find every coefficient negated and every vanishing unchanged.

No sector is exchanged. The form is a real number per wave number, the amplitude is four real components, and twice the scalar part is a sum of four numbers. **None of the three is a statement about $\mathbb{B}_\Phi$ and $\mathbb{B}_\Psi$.**

## The Action in Momentum Space: The Quadratic Form and Its Stationarity

At a wave number the action is a quadratic form and nothing more. There is no coupling between different wave numbers in the free case, so the transform does not merely simplify the action; it decomposes it into an independent form at each wave number. The variation is then algebraic at each index, and the Euler–Lagrange equation is the vanishing of one gradient.

The term $[kA]^{2}$ is the field term's longitudinal content: it is quadratic in the Lorenz form and it vanishes on the Lorenz plane. The term $-(k^{2}-\nu_m^{2})A\!\cdot\!A$ is the field term's transverse content together with the mass, and it is diagonal in the amplitude. Their competition is the whole of the Proca system's structure, and the two coefficients are read off below.

The action is real, the pairing is $\mathrm{Re}\,\mathrm{Sc}$, and the mass term is the invariant length. At a mode all three are statements about real coefficients of a real form: $\mathcal{Q}$ is real because every coefficient is real. There is no imaginary part to remove and no surface term to drop, which is the same gain that the Dirac variational companion records and for the same reason: a multiplier needs no integration by parts.

The parent adopts the second-order form and puts the Palatini form aside; the form below is the second-order one's. A first-order form would give a different form and a pair of equations, and §*Open Questions* records that the article does not treat it.

## The Variation

The mode form $Q$ of the previous section is a quadratic form in the amplitude: it contains the amplitude and its conjugate and no derivative of either, because the transform has replaced every derivative by a multiplier. So the variation with respect to the conjugate amplitude is

$$
\delta Q=\mathrm{Sc}\bigl[\delta X^{*}\,\mathcal{S}(\omega,2\pi\vec\nu_{\Phi})X\bigr],
$$

with no integration by parts, no surface term and no boundary condition. A boundary term appears in a variational principle because a derivative is varied; here no derivative is varied, so none appears. That is not a convenience of the calculation, it is what the transform does to the principle.

Vanishing for every $\delta X^{*}$ forces the bracket to vanish, by the same positivity argument as in the element article: choose $\delta X^{*}$ equal to the bracket and the scalar part becomes a sum of squared moduli. So

$$
\mathcal{S}(\omega,2\pi\vec\nu_{\Phi})\,X=0,
$$

The symbol equation the article solves. The passage from the action to the equation is one line and it is exact: the fixed-frequency action's stationarity and the symbol equation are the same statement.

The variation at a mode cannot see a boundary condition, a topological charge or a spatially varying coefficient, because a mode is defined only where the coefficients are constant. Every statement in this section inherits the constant-coefficient licence that the section on limits makes explicit.

### Zero, Pole and the On-Shell Action: Zero, Pole and Degeneracy Are One Locus

The transverse coefficient is $-\tfrac12(k^{2}-\nu_m^{2})A\!\cdot\!A$, so the form is degenerate on the Lorenz plane precisely at $k^{2}=4\pi^{2}\nu_m^{2}$. That is the same surface as the form companion's $\det\sigma=0$ and the same surface as the propagator's denominator's zero. **Three registers, one locus**, and the naming is *The Lagrangian and the Dirac Equation in Momentum Space*'s, whose §*Zero and Pole Are One Object* establishes it for the Dirac action.

The action's vanishing on shell selects the support; the symbol's singularity gives the pole; the form's degeneracy says the amplitude is unconstrained there. Write $N(k)=k^{2}-4\pi^{2}\nu_m^{2}$: the variational output is $N=0$, the symbol is $N$ times a projector plus $-\nu_m^{2}$ along $k$, and the propagator is proportional to $1/N$. The article states the three and does not claim that any one of them implies another.

In the Dirac case the second variation is one central scalar and the zero is a number's vanishing. Here the second variation is a matrix with two distinct eigenvalues, so the locus where the form degenerates is a locus where it degenerates *partially*: rank one on the shell, not rank zero. The partial degeneracy is the three polarisations, and the article's one addition to the precedent is that sentence.

The degeneracy is not the pole's whole story. A propagator's residue at the pole is a projector, and here it is the transverse projector: the residue is supported on the Lorenz plane and vanishes along the wave number. That is why the longitudinal mode's contribution to the propagator is not a pole at all but the $-1/\nu_m^{2}$ term the standard treatment records, and the form's eigenvalues say so in one line.

### The Legendre Transform

The Proca mode form is quadratic in the frequency, so the transform inverts in general; but the mass term removes one degree of freedom, and the direction it removes is the one where the transform's derivative does not depend on the frequency. The transform is therefore two-valued on the transverse form and single-valued on the longitudinal one, and that asymmetry is what the coupled article's section calls the inversion being two-valued.

The two roots of the quadratic are the two mass-shell branches, and they differ by the sign of the frequency. The branches are not two particles: they are the same form read at $\pm\omega$, and the density's sign is what distinguishes them.

On the longitudinal direction the form reduces to $\tfrac12\nu_m^{2}(A\cdot A)$ and the frequency has dropped out. The transform's derivative there is the mass and not the frequency, so the transform returns the coefficient $\nu_m^{2}$ and no branch. This is the precise sense in which the Proca field has three degrees of freedom and not four: one direction is a coefficient and the other three are a form.

The derivative of the action with respect to $\omega$ is the density per mode, and the transform's slope is therefore the density as a function of the energy. On the transverse directions the slope changes sign between branches; on the longitudinal direction it does not, because the density there carries the mass and not the frequency.

What the transform does not do. It does not produce the constraint. The constraint is already in the form — the vanishing of the longitudinal coefficient's variation — and the transform only reports it as a coefficient that does not move. A reader who expected a Lagrange multiplier has looked for one in the wrong place: the exact parameterisation and the mass term both make it unnecessary.

The transform is taken before the equation is imposed. On shell the form vanishes, so the transform of the on-shell form is zero on both branches and on the longitudinal direction alike, and the article does not take it.

## The Constraints the Action Imposes: The Constraint Is the Vanishing of a Coefficient

The derivative in the direction of the wave number is

$$
\sum_{\imath}\frac{\partial\mathcal{Q}}{\partial A_{\imath}}\,2\pi\nu_{\imath}
=[kA]\,k^{2}-\bigl(k^{2}-4\pi^{2}\nu_m^{2}\bigr)\bigl(A\!\cdot\!k\bigr)
=4\pi^{2}\nu_m^{2}\,[kA] ,
$$

because $A\cdot k=[kA]$ and the two $k^{2}$ terms cancel. **So the directional derivative along $\nu_{\imath}$ is the mass times the Lorenz form**, and stationarity in every direction gives $\nu_m^{2}[kA]=0$, which is the parent's $\nu_m^{2}S=0$ with $S$'s symbol in place.

The parent derives the constraint by differentiating the equation; the article derives it by varying along one direction. Both give one condition because the form has one direction in which its coefficient is the mass, and neither needs the notion of a gauge transformation.

At $\nu_m=0$ the form is $\tfrac12([kA]^{2}-k^{2}A\!\cdot\!A)$, whose longitudinal coefficient is zero identically, so the variation along $\nu_{\imath}$ produces no condition and the amplitude along $\nu_{\imath}$ is free. That freedom is the gauge freedom, and in the form's language it is the freedom of a null direction rather than the orbit of a group.

A gauge freedom is a freedom, and a quadratic form that has a null direction does not select one. The parent's statement that in the massless theory $S=0$ can be reached from any potential by a gauge transformation is the statement that the null direction can be removed by a shift, and the form's version is that the kernel of the Hessian contains the wave number. The two agree and neither is deeper.

The coefficient of $A_0^{2}$ contains no $\omega^{2}$, and that is the primary constraint. Expanding the form's diagonal,

$$
\frac{\partial^{2}\mathcal{Q}}{\partial A_0^{2}}=\tfrac12\Bigl(2\pi\nu_t'^{2}-k^{2}+4\pi^{2}\nu_m^{2}\Bigr)=\tfrac12\bigl(2\pi\vec\nu_\Phi^{2}+4\pi^{2}\nu_m^{2}\bigr) ,
\qquad
\frac{\partial^{2}\mathcal{Q}}{\partial A_\eta^{2}}=\tfrac12\Bigl(\kappa_\eta^{2}+k^{2}-4\pi^{2}\nu_m^{2}\Bigr) ,
$$

so the temporal coefficient is $\tfrac12(\vec\nu_\Phi^{2}+\nu_m^{2})$ and the three spatial coefficients each carry the frequency. **Measured at $2\pi\nu_m=0.7$ and $2\pi\vec\nu_\Phi=(0.3,0.2,0.1)$: the temporal coefficient is $0.315000000$ at $2\pi\nu_t'=0.5$, $1.2$ and $2.0$, while the first spatial coefficient is $-0.145$, $+0.450$ and $+1.730$.**

A coefficient with no $\omega^{2}$ is a constraint. The Hessian's temporal entry is a number, so the equation for $A_0$ is algebraic in the frequency and can be solved and substituted; that is exactly the parent's remark that the second-order form carries a primary constraint, and it is why the count is four minus one. The absent power is the constraint, and the article's contribution is to say that it is absent rather than small.

$F_{0\eta}=\partial_0A_\eta-\partial_\eta A_0$ contains no $\partial_0A_0$, so no amount of minimal coupling can put an $\omega^{2}$ on $A_0$. The variational coupled companion makes the same statement with the connection present, and the two agree because the reason is the antisymmetry of the field strength and not the absence of a potential.

The three spatial coefficients move because they are the propagating ones. Their frequency dependence is the dispersion relation's, read as a coefficient: on the shell the transverse coefficient vanishes, which is the symbol's rank drop. The temporal coefficient never vanishes for a massive field, which is why the primary constraint is not a dynamical equation at any frequency.

## The Structural Consequence: The Longitudinal Coefficient Is the Mass Alone

Put $A\parallel \nu_{\imath}$, so that $A=\lambda 2\pi\nu_{\imath}$ and $[kA]=\lambda k^{2}$. Then

$$
\mathcal{Q}\bigl(\lambda k\bigr)
=\tfrac12\Bigl(\lambda^{2}k^{4}-\bigl(k^{2}-4\pi^{2}\nu_m^{2}\bigr)\lambda^{2}k^{2}\Bigr)
=\tfrac12\lambda^{2}\,4\pi^{2}\nu_m^{2}k^{2}
=\tfrac12 4\pi^{2}\nu_m^{2}\bigl(A\!\cdot\!A\bigr) ,
$$

and the $k^{4}$ cancels against the $k^{4}$ inside the second term. The cancellation is the statement that the field term does not act along the wave number, which is the parent's "the field term depends on the longitudinal part only through a total derivative", read as an algebraic identity.

On a unit-norm longitudinal amplitude, with $2\pi\vec\nu_\Phi=(0.3,0.2,0.1)$:

| $\nu_m$ | $2\pi\nu_t'=0.5$ | $2\pi\nu_t'=1.2$ | $2\pi\nu_t'=2.0$ | $\tfrac12\nu_m^{2}\lvert A\!\cdot\!A\rvert$ |
| --- | --- | --- | --- | --- |
| $0.7$ | $+0.245000000$ | $+0.245000000$ | $+0.245000000$ | $+0.245000000$ |
| $0.3$ | $+0.045000000$ | $+0.045000000$ | $+0.045000000$ | $+0.045000000$ |
| $0$ | $0$ | $0$ | $0$ | $0$ |

Nine entries, three frequencies, one column. The value does not depend on $\nu_t'$ at all, which is the same statement as the algebra above: the longitudinal coefficient is a function of the mass and of the amplitude's norm and of nothing else. No other coefficient of the form has that property.

The transverse coefficient is the contrast, and it depends on both. On the Lorenz plane $[kA]=0$ and $\mathcal{Q}=-\tfrac12(k^{2}-4\pi^{2}\nu_m^{2})A\!\cdot\!A$, which moves with $k^{2}$ and therefore with the frequency and the wave vector. So the form is one constant direction and three moving ones, and the constant direction is the one the constraint removes. That is the sense in which the constraint's cost is fixed and the propagating modes' cost is not.

The variation along $\nu_{\imath}$ is $\partial\mathcal{Q}/\partial\lambda=2\lambda\tfrac124\pi^{2}\nu_m^{2}(A\!\cdot\!A)$, which vanishes for every $\lambda$ when $\nu_m=0$. **A coefficient that is proportional to the mass is a constraint that exists in proportion to the mass**, and that is a sharper statement than "the mass breaks the symmetry": nothing is broken, one coefficient is zero.

## The Structural Consequence: The Trace Is the Mass

$\mathrm{tr}\,\sigma=4(k^{2}-4\pi^{2}\nu_m^{2})-k^{2}=3k^{2}-44\pi^{2}\nu_m^{2}$, which at $k^{2}=4\pi^{2}\nu_m^{2}$ is $-\nu_m^{2}$ exactly. So on the mass shell the symbol's trace is the mass and nothing else, independent of the wave vector, the frequency and the direction.

The variational parent proves $T_{\imath\imath}=-4\pi^{2}\nu_m^{2}\langle\tilde A_\Phi\rangle_\natural$ exactly, and observes that the field terms' contributions cancel because $\delta_{\imath\imath}=4$. The symbol's trace carries the same cancellation: the four diagonal entries of $k^{2}-\nu_m^{2}$ minus the one from the rank-one part give three of the former and one of the latter, which is the four-minus-one count in the trace.

The parent traces over the spacetime indices of a tensor; the article traces over the amplitude directions of a Hessian. Both give the mass, and the agreement is the reason the trace statements are not two coincidences: the mass is the only term in the action that is a multiple of the identity in the amplitude space.

What the trace does not do is vanish anywhere physical. $\mathrm{tr}\,\sigma=0$ requires $k^{2}=\tfrac434\pi^{2}\nu_m^{2}$, which is not the mass shell. So the massive vector field's symbol is never traceless, and the parent's conformal non-invariance is the same fact: the mass is in the trace and cannot be removed from it. A massless field has $\mathrm{tr}\,\sigma=3k^{2}$, which vanishes exactly on the cone.

## The Noether Currents: The Stress Per Mode

The free Proca field has no phase symmetry, so there is no conserved charge and no bilinear to carry one; the element article proves it and the chart inherits it. What survives the transform is the energy–momentum, and at a mode it is the symbol acting as the energy.

The energy of a mode is $\mathcal{Q}$ evaluated on the shell, and the momentum flux is the same form with the wave number in place of the frequency. The two are the components of one object, and the object is the quadratic form of the article's third section read twice. No separate computation is needed, and none is offered.

What the mass term does. It fixes the longitudinal coefficient to $\nu_m^{2}$ and therefore fixes the energy of the longitudinal mode; the transverse modes keep the Maxwell dispersion. That split of the stress into two pieces is the mode-level statement of the count the element article makes, and it is the reason the Proca article's *Longitudinal Coefficient* section exists.

## What the Principle Adds and What It Relabels: In Momentum Space

What the transform adds. One identity: the action at a fixed frequency is the quadratic form whose kernel is the symbol. That identity is worth having, because it turns the variational principle into linear algebra and the equation into a null space, and because it makes the reality of the action and the Hermiticity of the symbol one statement seen twice.

What it relabels. The variational principle itself: nothing is added to the physics, no new current appears, and no equation is solved that the parent did not already solve. The word *action* at a mode is a density in the frequency and the wave number, not an integral over a region, and calling it an action is a shorthand that this section keeps because the shorthand is the point.

What it cannot reach. The boundary term, the varying coefficient and the operator ordering. The first two need position space; the third is invisible at a constant symbol, where left and right multiplication agree. Each of those is named where the article meets it, and none is repaired by the transform.

## Open Questions

Whether the first-order form has a longitudinal coefficient that is also $\omega$-independent. The parent records the Palatini form and does not use it. In the first-order form the field strength is an independent variable, and the longitudinal direction's cost would be a property of the constraint's multiplier rather than of the mass term. Whether the constant survives is not settled.

Whether the absent $\omega^{2}$ in the temporal coefficient has a chart reading. The polar companion shows that the chart's four parameters are not four momenta and that four of the Legendre momenta vanish. Whether the vanishing of those momenta and the absence of the frequency in the temporal coefficient are one statement is a question the two articles raise jointly and neither answers.

## Summary

At a wave number the Proca action is one quadratic form, $\mathcal{Q}=\tfrac12\{[kA]^{2}-(k^{2}-4\pi^{2}\nu_m^{2})A\!\cdot\!A\}$, whose gradient is $-\eta\,\sigma A$ and whose stationarity is therefore the Proca symbol's vanishing, verified to $2.1\times10^{-11}$ on a random amplitude.

Along the four-wave-number the form is $\tfrac12\nu_m^{2}(A\!\cdot\!A)$ exactly, because the $k^{4}$ of the field term cancels against the $k^{4}$ inside the second term. Measured on a unit-norm longitudinal amplitude, the coefficient is $0.245000000$ at $2\pi\nu_m=0.7$ and $0.045000000$ at $2\pi\nu_m=0.3$, at every frequency from $2\pi\nu_t'=0.5$ to $2.0$. The longitudinal coefficient is a function of the mass alone.

The constraint is that coefficient. Varying along $\nu_{\imath}$ gives $\nu_m^{2}[kA]=0$, which is the parent's $\nu_m^{2}S=0$; at $\nu_m=0$ the coefficient vanishes identically and the direction is free. Gauge freedom is a zero coefficient in the quadratic form, and the massless theory's $S=0$ is a null direction of the Hessian rather than the orbit of a group.

The coefficient of $A_0^{2}$ is $\tfrac12(\vec\nu_\Phi^{2}+\nu_m^{2})$, with no $\omega^{2}$: $0.315000000$ at all three frequencies, while the three spatial coefficients move from $-0.145$ to $+0.45$ to $+1.73$. The absent power is the primary constraint, and the coupling cannot add one because $F_{0\eta}$ contains no $\partial_0A_0$.

The form degenerates exactly where the symbol is singular and where the propagator has its pole, and the degeneracy is partial: rank one on the shell, which is the three polarisations. On the shell the symbol's trace is $3k^{2}-44\pi^{2}\nu_m^{2}=-4\pi^{2}\nu_m^{2}$, the same mass the parent's $T_{\imath\imath}=-4\pi^{2}\nu_m^{2}\langle\tilde A_\Phi\rangle_\natural$ carries, and it vanishes only at $k^{2}=\tfrac434\pi^{2}\nu_m^{2}$, which is not physical.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde\Upsilon_\Phi=i\nu_t'e_t+\vec\nu_\Phi$ | The four-wave number; $2\pi\nu_t'=\omega/c$ |
| $k^{2}=2\pi\nu_t'^{2}-2\pi\vec\nu_\Phi^{2}$ | The interval in wave numbers |
| $\nu_m=\frac{mc}{h}$ | The mass wave number |
| $[kA]=2\pi\nu_t'a_t'-2\pi\vec\nu_\Phi\cdot\vec a$ | The Lorenz form of the amplitude; the parent's $S$ up to $-i$ |
| $\mathcal{Q}(A)=\tfrac12\{[kA]^{2}-(k^{2}-4\pi^{2}\nu_m^{2})A\!\cdot\!A\}$ | The momentum-space quadratic form |
| $\partial\mathcal{Q}/\partial A=-\eta\,\sigma A$ | The stationarity; the Proca symbol's vanishing |
| $\tfrac12\nu_m^{2}(A\!\cdot\!A)$ | The longitudinal coefficient; independent of the frequency |
| $\tfrac12(\vec\nu_\Phi^{2}+\nu_m^{2})$ | The coefficient of $A_0^{2}$; no $\omega^{2}$ |
| $3k^{2}-4\nu_m^{2}$ | The symbol's trace; $-\nu_m^{2}$ on the shell |
| $N(k)=k^{2}-4\pi^{2}\nu_m^{2}$ | One function, read at its zero and at its pole |

## Further Reading

- *The Lagrangian and the Proca Equation*, for the action, the variation, the Lorenz condition as a consequence and the Noether currents.
- *The Fourier Transform and the Proca Equation in Biquaternionic Form*, for the symbol's determinant, rank and kernel.
- *The Fourier Transform and the Proca Equation in Biquaternionic Polar Variables*, for the chart reading of the same field.
- *The Lagrangian and the Dirac Equation in Momentum Space*, for the zero–pole relation and the momentum-space action of a first-order theory.
- *The Lagrangian and the Coupled Proca Equation in Momentum Space*, for the same form with a connection.
- *The Proca Equation: Massive Spin 1 in Biquaternionic Form*, for the plane waves and the polarisation count.
- *Derivatives, Fields and Transforms*, for the symbol rule.
- *Norm and Pairing Conventions*, for the material form's indefiniteness and the Hermitian pairing.
- L. D. Landau and E. M. Lifshitz, *The Classical Theory of Fields* (Pergamon, 4th ed., 1975), §31, for the massive vector field's Lagrangian and the primary constraint.
- P. A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for the counting of constraints by the vanishing of a Hessian entry.
