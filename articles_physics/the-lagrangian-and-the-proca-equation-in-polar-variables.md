# __The Lagrangian and the Proca Equation in Polar Variables__

## Introduction

This article substitutes the polar word of the material sector into the Proca action and reads the result. It is the polar companion of *The Lagrangian and the Proca Equation*, and it depends on three articles: *The Proca Equation in Biquaternionic Polar Variables* for the word and the equation in the chart, that element-form Lagrangian article for the action, and *The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Bivector Plane* for the carrier.

The substitution. The element-form action is

$$
S[\tilde A_\Phi]=\int d^4r\;\Bigl[\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)-\tfrac12\,k_m^2\,\langle\tilde A_\Phi\rangle_\natural\Bigr],
$$

and the word of the material sector is piecewise,

$$
\tilde A_\Phi=\varepsilon\,i\,\varrho\,\tilde U_{\Psi,\mathrm b}\ \ (\langle\tilde A_\Phi\rangle_\natural<0),
\qquad
\tilde A_\Phi=\varrho\,\tilde U_{\Psi,\mathrm b}\,\hat u\ \ (\langle\tilde A_\Phi\rangle_\natural>0),
$$

with $\varrho>0$, $\varepsilon=\pm1$, and $\tilde U_{\Psi,\mathrm b}$ the boost of rapidity $\theta_{\mathrm{rpd}}$ and axis $\hat u_{\mathrm b}$. On the timelike branch the parameters are $\varrho$ and the boost's three; on the spacelike branch they are $\varrho$, the signed rapidity and the direction $\hat u$. Two branches, four parameters each.

Three things are established, and their status differs.

*First, the action in the chart has a compact form.* Because the scalar part of the conjugate gradient splits additively from its vector part, the field term is the full quadratic minus its scalar square,

$$
\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)
=\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\Bigl[\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr)^2\Bigr]-\tfrac12 S^2,
\qquad
S=\mathrm{Sc}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr),
$$

and the mass term is a pure power of the modulus,

$$
-\tfrac12\,k_m^2\langle\tilde A_\Phi\rangle_\natural=
\begin{cases}+\tfrac12\,k_m^2\,\varrho^2, & \text{timelike},\\[2pt] -\tfrac12\,k_m^2\,\varrho^2, & \text{spacelike}.\end{cases}
$$

The sign of the mass term in the chart is the branch: it is the causal character of the four-vector, read as the sign of the term. This is the article's cleanest new statement.

*Second, the Euler–Lagrange equations in the chart are the transformed field equation.* The word is a diffeomorphism from its parameter set onto the branch, so a change of variables carries the variational problem into the chart without any loss: four parameters, four equations, and the equations are the two displays of the polar article — the scale equation with the frame's quadratic source, and the frame transport. Nothing has to be re-derived, and nothing can differ.

*Third, the count of multipliers is not the count of constraints.* The parametrization absorbs the unit condition of the boost exactly, so no Lagrange multiplier is needed for the normalization of the frame. The comparison with Takabayasi's tensor formulation has to be drawn on the right row, because that formulation is of the spin-$\tfrac12$ field: its multipliers $A_1,A_2,A_3$ carry the unit spin direction and the spin's transport, and its velocity's unit condition carries one more. The material sector has no spin direction of that kind — the boost axis is the velocity's, not a spin's — so the only row that compares is the velocity's, where the multiplier count would be one and not three. The chart pays none of it, because the angles are coordinates. But the Proca system still has its own constraint: the Hessian of the chart's Lagrangian has rank three and not four, and the missing direction is the one that changes the scalar potential at fixed vector potential. That is the primary constraint of the vector field, and the Lorenz condition is its secondary partner. The chart relabels them; it does not remove them.

What is at stake in the contrast. The Schrödinger polar article's action is first order in the time derivative, and its momenta vanish identically, so six of the eight are constraints and the closure needs Dirac analysis. The Proca action is second order, its Hessian has rank three out of four, and its single constraint is the standard one of a massive vector field. So the two polar variational principles are not the same kind of object, and the difference is the order of the Lagrangian, not the algebra.

The conventions are those of the two companion articles: $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with central $i$; the material sector $\mathbb{B}_\Phi$ anti-Hermitian; $\mathrm{Sc}$ the coefficient of $e_t$; $\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^{\natural}$ the quaternionic norm, real on $\mathbb{B}_\Phi$; $\partial/\partial R_t=-i\,\partial/\partial r'_t$; $\Box_\Phi=\Delta_\Phi-\partial^2/\partial{r'_t}^2$; $k_m=mc/\hbar$.

## Conventions

The conventions are the corpus's, restated here for the chart. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_\mu^{2}=-e_t$; $\varrho>0$ is the scale, $\theta_{\mathrm{rpd}}\ge0$ the rapidity and $\hat u_{\mathrm b}$ the boost axis, so that $\vec A=-\varrho\sinh\frac{\theta_{\mathrm{rpd}}}{2}\hat u_{\mathrm b}$ on the branch. The measure is $\mathrm{d}^4r$, the pairing is $\mathrm{Sc}(\cdot)$ and $\mathrm{Re}\,\mathrm{Sc}(\cdot\cdot)$ for the field term, $k_m=mc/\hbar$, and the chart's velocities are the material-time derivatives. The branch is the timelike one; the spacelike branch is named where it matters and is not followed here.

## The Action in Polar Variables

The field term. Write $\tilde F=\mathrm{Vect}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)$ and $S=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)$, so that the conjugate gradient is the sum of a scalar and a pure vector,

$$
(\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi=S+\tilde F .
$$

Squaring, the cross term is $2S\tilde F$, whose scalar part vanishes because $\mathrm{Sc}(\tilde F)=0$; hence

$$
\mathrm{Sc}\Bigl[\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr)^2\Bigr]=S^2+\mathrm{Sc}\bigl(\tilde F\tilde F\bigr),
$$

and the field term is the full quadratic minus the scalar square. The subtraction is the projection that the element form performs silently: $\tilde F$ is the antisymmetric part, and $\mathrm{Sc}(\tilde F^2)$ is the part of the full square that survives it. The identity is exact, holds for every element of $\mathbb{B}$ and not only on shell, and is verified by direct multiplication.

The mass term. On the timelike branch the norm is $-\varrho^2$, because $(\varepsilon i\varrho\tilde U)(\varepsilon i\varrho\tilde U)^{\natural}=\varepsilon^2i^2\varrho^2\tilde U\tilde U^{\natural}=-\varrho^2$; on the spacelike branch it is $+\varrho^2$, because $(\varrho\tilde U\hat u)(\varrho\tilde U\hat u)^{\natural}=\varrho^2\tilde U\hat u\hat u^{\natural}\tilde U^{\natural}=\varrho^2\tilde U(-\hat u)(-\hat u)\tilde U^{\natural}=\varrho^2$. Hence

$$
-\tfrac12k_m^2\langle\tilde A_\Phi\rangle_\natural=
\begin{cases}+\tfrac12k_m^2\varrho^2, & \text{timelike},\\[2pt]-\tfrac12k_m^2\varrho^2, & \text{spacelike}.\end{cases}
$$

The sign is the branch. In the element form the mass term is indefinite, because $\langle\tilde A_\Phi\rangle_\natural$ is indefinite. In the chart it becomes a definite power of one positive parameter, and its sign is a property of the branch. For a timelike field the scale enters the Lagrangian with the sign of a positive mass term and the scale equation has the standard massive form; for a spacelike field the sign is reversed. Nothing in the element form displays this, because nothing in the element form distinguishes the two branches.

The polar Lagrangian. Collecting the two pieces,

$$
\boxed{\;\mathcal{L}=\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\Bigl[\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr)^2\Bigr]-\tfrac12S^2-\tfrac12k_m^2\langle\tilde A_\Phi\rangle_\natural\;}
$$

with the last term read from the branch. The three pieces are the full quadratic of the conjugate gradient, the negative square of its scalar part, and the mass. The middle piece is not a gauge-fixing term added by hand: it is what the projection removes, and it is present in the element form already, hidden inside $\mathrm{Re}\,\mathrm{Sc}(\tilde F\tilde F)$. In the chart it is displayed, and displayed is where its rôle can be read: its variation is what produces the Lorenz condition as an equation.

The parameters. On the timelike branch the field is $\tilde A_\Phi(q)$ with $q=(\varrho,\theta_{\mathrm{rpd}},\vartheta_1,\vartheta_2)$ and the two angles parametrizing $\hat u_{\mathrm b}$; the discrete $\varepsilon$ is not varied, because it is a label and not a coordinate. On the spacelike branch $q=(\varrho,\theta_{\mathrm{rpd}},\vartheta_1,\vartheta_2)$ with the angles those of $\hat u$. In both cases four.

The pairing. Inherited, and the substitution cannot disturb it. The parent pairs with $\mathrm{Re}\,\mathrm{Sc}(\cdot\cdot)$ — the field term's reality is the explicit $\mathrm{Re}$ — and with $\mathrm{Sc}(\tilde A^{*}\tilde A^{\natural})$ for the mass. The chart writes $\tilde A_\Phi=\varrho\,u$ with $u$ a unit element, and the mass term becomes $\tfrac12k_m^{2}\varrho^{2}$, real. The field term's $\mathrm{Re}$ still does its work: the chart's $\varrho$ is real, so the term is the real part of a product of real multiples of $\tilde F(u)\tilde F(u)$.

The type of the coefficient. The mass, and the constraint is not a coefficient. $k_m^{2}$ is real, and the chart shows the mass as a square of the density. The other coefficient the Proca action appears to carry — the one that would fix the Lorenz condition — is not in the action at all; it is a consequence, and *The Constraints the Action Imposes* is where it is read.

The selection rule. Declared, and there is nothing to select. The Proca action has no free potential, so no admissible-variation question arises. The condition that removes the scalar polarisation is a constraint from the action's own variation, which is a different object from a selection rule on potentials.

**What reality does not buy. Reality does not remove the constraint and does not sign the energy.** A real Proca density is compatible with any sign of $k_m^{2}$ and with the Lorenz condition or its absence. The constraint belongs to *The Constraints the Action Imposes* and the sign of the four polarisations' energies to *The Noether Currents*.

## The Variation: The Euler–Lagrange Equations

The change-of-variables argument. **The word is a bijection from the parameter set onto the branch**, and both are open subsets of four-dimensional spaces; it is smooth with smooth inverse away from the coordinate singularity at the pure scalar-potential line. A diffeomorphism carries a variational problem to a variational problem: if $\tilde A_\Phi=\Phi(q)$ and $S=\int\mathcal{L}(\Phi(q),\partial\Phi(q))$, then

$$
\frac{\delta S}{\delta q^i}=\Bigl(\frac{\delta S}{\delta\tilde A_\Phi}\Bigr)\Big|_{\tilde A_\Phi=\Phi(q)}\cdot\frac{\partial\Phi}{\partial q^i},
$$

and the Jacobian $\partial\Phi/\partial q^i$ is invertible on the branch. So the Euler–Lagrange equations in the chart vanish if and only if the element-form equation holds, and their content is the field equation and nothing else. This is an identity of the calculus, not a claim about the algebra, and it is what makes the polar variational principle exact.

The singularity bounds the argument, and it is the chart's. On the timelike branch $\varrho=\sqrt{-\langle\tilde A_\Phi\rangle_\natural}$ and $\varepsilon=\mathrm{sign}\,a'_t$ are single-valued, but $\hat u_{\mathrm b}$ is not: it is $\vec A$ divided by its length, and at $\vec A=0$ — the pure scalar-potential line — the axis is undefined and the Jacobian degenerates. The field is perfectly regular there; the coordinates are not. So the change-of-variables identity holds on the branch minus that line, and a solution that crosses it needs a patching of the frame rather than a continuation of the chart. On the spacelike branch there is no such line, because a spacelike four-vector has $\vec A\neq0$, and the chart's only failure there is the light cone of field values, where the branch itself ends.

The explicit form. Performing the differentiation gives the two displays of the polar article. The scalar part of the transformed equation is

$$
\bigl(\Box_\Phi-k_m^2\bigr)\varrho+\varrho\sum_\mu\mathrm{Sc}\bigl(\Gamma_\mu^2\bigr)=0,
\qquad
\Gamma_\mu=\tilde U_{\Psi,\mathrm b}^{-1}\frac{\partial\tilde U_{\Psi,\mathrm b}}{\partial R_\mu},
$$

and the scalar-free part is

$$
\sum_\mu\Bigl(\frac{\partial\Gamma_\mu}{\partial R_\mu}+\Gamma_\mu^2-\mathrm{Sc}\bigl(\Gamma_\mu^2\bigr)\Bigr)
+2\sum_\mu\frac{\partial\ln \varrho}{\partial R_\mu}\Gamma_\mu=0 ,
$$

the subtraction of $\mathrm{Sc}(\Gamma_\mu^2)$ being what makes the display traceless: without it the term $\sum_\mu\Gamma_\mu^2$ would repeat the source of the scalar equation.

Both are exactly the equations that the direct substitution of the word into the field equation gives, which is the content of the change-of-variables argument: the variational route and the substitution route are the same route. For a fixed boost axis the pair reduces to

$$
\bigl(\Box_\Phi-k_m^2\bigr)\varrho+\tfrac14\varrho\sum_\mu\Bigl(\frac{\partial\theta_{\mathrm{rpd}}}{\partial R_\mu}\Bigr)^2=0,
\qquad
\sum_\mu\frac{\partial}{\partial R_\mu}\Bigl(\varrho^2\frac{\partial\theta_{\mathrm{rpd}}}{\partial R_\mu}\Bigr)=0 ,
$$

which is the form the polar article verifies numerically. The mass term enters the first with the sign $+k_m^2\varrho$ on the timelike branch, as the branch's sign of the mass term requires.

What the variation of the middle piece does. The term $-\tfrac12S^2$ is the only piece that pairs the scalar projection with itself. Its variation produces the scalar equation that is the Lorenz condition, and the remaining pieces produce the two dynamical equations. In this sense the chart separates the three jobs that the element form performs at once: the curl term carries the propagation, the square carries the constraint, and the mass carries the scale. The separation is a rewriting, but it is a rewriting that names each job.

The parameter basis and the four brackets. One derivative, four types, for the material word. The polar word of the Proca field has the same four parameter groups as the scalar field's, so its logarithmic derivative has the same four brackets:

$$
\tilde A_\Phi^{-1}\partial\tilde A_\Phi
=\partial\ln\varrho+i\,\partial\theta_{\mathrm{pha}}+\tfrac12\partial\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}+\tfrac12\bigl(\partial\theta_{\mathrm{axr}}\,\vec u_{\mathrm r}+\ldots\bigr),
$$

real scalar, central imaginary, Hermitian and real vector. The brackets are a property of the parameterisation and of the algebra's type decomposition; they are not a feature of any one field.

Why the Proca action keeps more of them than the scalar action. The scalar action's bilinear $\tilde\Xi^{*}\tilde\Xi$ is one Hermitian object, so only the matching types survive. The Proca action is built from the square of the conjugate gradient, and a square pairs the scalar part with the scalar part and the vector part with the vector part while retaining the cross term between them. The full quadratic form of the conjugate gradient is therefore in the Lagrangian, and the antisymmetric combination it retains is the object whose variation gives the Lorenz condition. The middle piece $-\tfrac12S^{2}$ is that cross term, and it is what the element form's projection removes.

The branch is not a bracket. The chart is a diffeomorphism onto one branch at a time, and the two branches -- timelike and spacelike -- differ by the sign of the mass term, $+\tfrac12k_m^{2}\varrho^{2}$ and $-\tfrac12k_m^{2}\varrho^{2}$. The four brackets are identical on the two branches; what changes is the algebraic mass term, which carries no derivative and therefore no bracket. This is the reason the bracket analysis of this article is branch-independent and the constraint analysis is not.

The parameter basis is not the bracket basis. The eight parameters are coordinates, the four brackets are types, and the Jacobian between them mixes: the rapidity's derivative carries part of the scale bracket, the rotor's derivative part of the boost bracket. The parameter equations are the same equations in a rotated basis and the brackets are the cleaner form, because each has one type and one partner.

**What the reader should take from the section.** The four brackets are the reason the polar Proca action has the structure it has: a quadratic form in the eight gradients with a frame-built metric, a mass potential, and no multiplier for the unit conditions. **The parameterisation absorbs the unit conditions by construction**, so the only price the chart pays is the cross term -- and the cross term is the constraint.
## The Constraints the Action Imposes: The Lorenz Condition in the Chart

One equation on four parameters. The chart's form of the condition is

$$
S=\varepsilon\Bigl[c\,\partial_{r'_t}\varrho-s\,\hat u_{\mathrm b}\cdot\nabla \varrho
+\tfrac12rs\,\partial_{r'_t}\theta_{\mathrm{rpd}}-\tfrac12rc\,\hat u_{\mathrm b}\cdot\nabla\theta_{\mathrm{rpd}}-rs\,\vec\nabla_\Phi\cdot\hat u_{\mathrm b}\Bigr]=0,
$$

with $c=\cosh\frac{\theta_{\mathrm{rpd}}}{2}$ and $s=\sinh\frac{\theta_{\mathrm{rpd}}}{2}$. It is the divergence of the four-vector in the chart's variables, and it is the secondary constraint. On shell it removes one of the four parameters and leaves three.

It is implied, and the variational reading says why. In the element form the condition follows from the divergence of the equation. In the chart it follows from the variation of the $-\tfrac12S^2$ term together with the rest, and it is the statement that the longitudinal part of the field is not free. There is no multiplier attached to it, and there is no gauge orbit along which it could be reached: it is one equation among the four.

**What it is not.** It is not the continuity equation of a fluid and it is not a guidance equation, because the material sector has no phase and therefore no phase current to conserve. The scalar Madelung pair is a pair because the field is one complex function; here the field is a real four-vector, and the condition is a single divergence. The variational principle does not manufacture the missing half.

## The Structural Consequence: The Mass Term, the Branch, and the Constraint

The Hessian has rank three. The kinetic part of the chart's Lagrangian is $\tfrac12\epsilon\vec E^2$ with $\vec E=-\vec\nabla_\Phi a'_t-\partial_{t'}\vec A$, so only $\vec A$ carries velocities, and

$$
\frac{\partial^2\mathcal{L}}{\partial\dot q^i\partial\dot q^j}
=\epsilon\,\frac{\partial\vec A}{\partial q^i}\cdot\frac{\partial\vec A}{\partial q^j},
$$

an outer product of four vectors in three dimensions. Its rank is therefore at most three, and it is exactly three wherever the four vectors $\partial\vec A/\partial q^i$ span $\mathbb{R}^3$, which they do at a generic point of the branch. So there is one null direction, and the chart has one primary constraint.

The null direction is the scalar potential. The four derivatives of $\vec A=-\varrho\sinh\frac{\theta_{\mathrm{rpd}}}{2}\hat u_{\mathrm b}$ along the branch are not independent: the combination that changes $\varrho$ and $\theta_{\mathrm{rpd}}$ while holding the product $\varrho\sinh\frac{\theta_{\mathrm{rpd}}}{2}$ fixed leaves $\vec A$ unchanged and changes $a'_t=\varrho\cosh\frac{\theta_{\mathrm{rpd}}}{2}$. That combination is the null vector, and it is exactly the direction in which the field changes by the gradient of a function of time — the primary constraint $\pi^0=0$ of the vector field, written in the chart's letters.

The Lorenz condition is the secondary constraint. Preserving the primary constraint in time produces the Lorenz condition, which in the chart is the single scalar equation displayed in the polar article. So the pair is second class, the physical count is three, and the chart's four parameters lose one on shell. That is the same count as the polarizations, and the same count as the element form's.

No multipliers for the invertibles, and no escape from the constraint. The two statements must be kept apart.

| what is counted | element form | chart | Takabayasi's tensor form (spin-$\tfrac12$) |
| --- | --- | --- | --- |
| unit condition of the frame (velocity) | automatic | automatic, by the word | one multiplier |
| unit spin direction | absent | absent | three multipliers $A_1,A_2,A_3$ |
| primary constraint | $\pi^0=0$ | rank-three Hessian | rank-three Hessian |
| secondary constraint | Lorenz | Lorenz | Lorenz |

The chart's gain is the first row: the boost is parametrized, not constrained, so its unit condition costs nothing, and the count it saves is one, not three. The second row is not a comparison at all — the material sector has no spin direction — and it is there exactly to say that the three multipliers usually quoted for Takabayasi are the price of a spin, not the price of a frame. The chart's non-gain is the third and fourth rows: the vector field's own constraints are untouched, and any claim that the polar form removes them would be false. This is the honest ledger, and it is the opposite of the Schrödinger case, where the *action* is first order and the constraints are the momenta's vanishing.

Why the Schrödinger case differs. There the Lagrangian is linear in $\dot\theta_{\mathrm{pha}}$, so the momentum conjugate to $\varrho$ vanishes identically and the system is a constrained one whose closure needs Dirac analysis. Here the Lagrangian is quadratic in the velocities, the momenta are the velocities' images under a rank-three map, and there is exactly one constraint pair. The order of the Lagrangian, and not the choice of variables, is what decides.

### The Reconstruction and Its Limits

The reconstruction is exact on a branch. The chart is a diffeomorphism from the parameter domain onto one branch of the material sector's N-regular set, so the word can be inverted there: the two norms give $\varrho$ and $\theta_{\mathrm{rpd}}$, the direction gives $\theta_{\mathrm{pha}}$, and the residual rotor gives $\theta_{\mathrm{axr}}$ and $\vec u_{\mathrm r}$. The inverse is the bijection read backwards and adds nothing to the action.

**The branch is an input and not an output.** This is the article's central qualification. The two branches differ by the sign of the algebraic mass term, $+\tfrac12k_m^{2}\varrho^{2}$ on the timelike one and $-\tfrac12k_m^{2}\varrho^{2}$ on the spacelike one, and **that sign is not a function of the eight parameters**. The chart is a chart on one branch; to move to the other the reader changes a discrete datum first and reconstructs afterwards. A reconstruction that claimed to recover the branch from the parameters would be claiming to recover a sign from a magnitude, and it cannot.

The scale's limit. $\varrho>0$ excludes the zero element, so a field that reaches $\varrho=0$ leaves the chart. For the Proca field that is not a pathology but a boundary: the mass shell's two branches meet only through the origin, and the origin is excluded.

The angle's limits. The rotor's angle must be closed at $2\pi$, or the word misses every element whose rotor factor is $-e_t$; the phase ranges over a half-open interval of length $\pi$, because the element and its negative are distinct while a shift by $\pi$ is not a symmetry of the action. Neither is a convention of this article; both are properties of the parameterisation it inherits.

What the reconstruction does not give. The flow. The bijection makes the variation the same variation, which is what the Euler–Lagrange section uses; it does not make the constrained system's flow the element equation's flow, and the article says so. The frame's reconstruction has a further weakness here: the mass term is a function of the frame, $R(\theta_{\mathrm{rpd}},\hat u_{\mathrm b},\theta_{\mathrm{axr}},\hat u_{\mathrm r})\varrho^{2}$, so the reconstructed frame is constrained by the potential and is not a free coordinate. That is not a defect of the map — it is the statement that the Proca field's frame is where the mass is extremal.

## The Noether Currents: The Stress and the Absence of a Charge

**One current and not two.** The free Proca field has no phase symmetry, and the article's element companion proves it: the potential is real on the material sector, so a central phase rotation is not a symmetry of the action but a complexification, and the Noether procedure returns nothing. The chart inherits the verdict, and it is worth stating in the chart because the chart is where a reader expects a density.

The stress. Translation invariance gives the canonical energy–momentum tensor, and in the chart it is the object whose components are the energy density $\tfrac12(\epsilon\vec E^{2}+\vec B^{2}/\mu+k_m^{2}\lvert\vec A\rvert^{2})$ and the Poynting flux. Both are read off the Lagrangian of the chart with the standard formula, and neither needs the phase.

What the absence means. The parameter that would carry a charge is $\theta_{\mathrm{pha}}$, and the chart's Lagrangian does not contain it: the word for the Proca field is real, $\theta_{\mathrm{pha}}=0$ is not a variable of the branch, and the mass term is $\varrho^{2}R$. So the chart has seven parameters and not eight on the physical branch, and the missing one is the one that would have carried a conserved charge. That is the chart's statement of "no second current", and it agrees with the element form's.

The hand check. Count the conjugate momenta from the Hessian of the previous section: three non-zero and one zero. The zero one is not a charge; it is the primary constraint. A charge would be a non-zero momentum whose conservation follows from a symmetry, and there is no such symmetry here.

## What the Principle Adds and What It Relabels: In the Polar Chart

Adds.

- The action in the chart, with the mass term reduced to a definite power of the modulus. Its sign is the branch, and that is a statement the element form cannot make.
- The explicit separation of the element-form Lagrangian into curl, scalar square and mass, with the middle piece identified as what the projection removes and as the term whose variation carries the Lorenz condition.
- The exactness of the chart's variational principle, with the change-of-variables argument making the equivalence a matter of calculus.
- The correct count: no multipliers for the unit conditions, one primary and one secondary constraint for the vector field, three physical parameters on shell.
- The fixed-axis reduction of the two Euler–Lagrange equations to a massive scale equation with a rapidity-gradient source and a conservation law with density $\varrho^2$.

Does not add.

- No new prediction and no new solution. The solutions are the element form's, and the chart only re-reads them.
- No removal of the constraints. The rank-three Hessian is the vector field's, and the chart displays it rather than dissolving it.
- No second current. The action's symmetries are the element form's, and the absence of a central phase is inherited unchanged.
- No simplification of the equations themselves. The chart's equations are nonlinear in the parameters, and they are longer than the field equation they encode. What the chart does simplify is the *identification* of the three jobs, and that is the gain recorded above and not a gain in brevity.

**The distinction that matters.** The polar variational principle is a coordinate change of a standard variational problem, and its value is entirely in what the coordinates display: the sign of the mass term as the branch, the three jobs of the three pieces, and the constraint's exact location. It is not a new principle, and the article claims nothing of the kind.

## Open Questions

The crossing set. The chart is a diffeomorphism on each branch and fails on the lightlike set of field values. What the variational problem does across the crossing — whether the action can be continued, and whether the continuation is stationary — is not settled.

The constraint analysis in the chart. The rank-three Hessian and the second-class pair are identified here but not carried through the Dirac bracket. The canonical quantization article performs the analysis in the component variables; whether the chart's variables simplify the bracket, or merely obscure it, is open.

## Summary

Substituting the polar word of the material sector into the Proca action gives

$$
\mathcal{L}=\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\Bigl[\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr)^2\Bigr]-\tfrac12S^2-\tfrac12k_m^2\langle\tilde A_\Phi\rangle_\natural ,
$$

with the mass term $+\tfrac12k_m^2\varrho^2$ on the timelike branch and $-\tfrac12k_m^2\varrho^2$ on the spacelike one: the sign of the mass term is the branch. The three pieces are the full quadratic of the conjugate gradient, the negative square of its scalar part, and the mass; the middle piece is what the element form's projection removes, and its variation carries the Lorenz condition.

The chart is a diffeomorphism onto the branch, so its Euler–Lagrange equations are the transformed field equation: the scale equation with the frame's quadratic source and the frame transport, which is what the polar article's direct substitution gives. The chart needs no Lagrange multiplier for the normalization of the boost, in contrast with the tensor formulation of the spin-$\tfrac12$ field, whose multipliers belong to its unit spin direction and its unit velocity — but it does not remove the vector field's own constraints: the Hessian has rank three, its null direction is the scalar potential at fixed vector potential, and the Lorenz condition is the secondary constraint. Four parameters, four equations, three physical parameters on shell.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\eta^2=-e_t$ |
| $i$ | Central scalar imaginary |
| $\mathbb{B}_\Phi$, $\mathbb{B}_\Psi$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathrm{Sc}$, $\mathrm{Vect}$, ${}^{\natural}$, ${}^{*}$ | Scalar part, vector part, quaternion and Hermitian conjugations |
| $\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^{\natural}$ | Quaternionic norm; real on $\mathbb{B}_\Phi$ |
| $\tilde A_\Phi=\varepsilon i\varrho\tilde U_{\Psi,\mathrm b}$ | Timelike branch of the word |
| $\tilde A_\Phi=\varrho\tilde U_{\Psi,\mathrm b}\hat u$ | Spacelike branch, boost axis locked to $\hat u$ |
| $\varrho>0$, $\theta_{\mathrm{rpd}}$, $\hat u_{\mathrm b}$, $\hat u$ | Modulus, rapidity, boost axis, direction |
| $\varepsilon=\pm1$ | Sign of the scalar potential, timelike branch |
| $\Gamma_\mu=\tilde U^{-1}\partial_\mu\tilde U$ | Frame bracket (Maurer–Cartan form) |
| $S=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)$ | Lorenz scalar |
| $\mathcal{L}$ | Lagrangian density in the chart |
| $\Box_\Phi=\Delta_\Phi-\partial^2/\partial{r'_t}^2$ | d'Alembertian of the corpus |
| $k_m=mc/\hbar$ | Mass wave number |

## Further Reading

- [The Proca Equation in Biquaternionic Polar Variables](the-proca-equation-in-biquaternionic-polar-variables.html), for the word and the equation in the chart.
- [The Lagrangian and the Proca Equation](the-lagrangian-and-the-proca-equation.html), for the element-form action, its variation and the currents.
- [The Proca Equation: Massive Spin 1 in Biquaternionic Form](the-proca-equation-massive-spin-1-in-biquaternionic-form.html), for the equation, the Lorenz condition and the polarizations.
- [Canonical Quantization of the Biquaternion Proca Field](canonical-quantization-of-the-biquaternion-proca-field.html), for the Legendre transform and the constraint structure in the component variables.
- [The Lagrangian and the Schrödinger Equation in Polar Variables](the-lagrangian-and-the-schrodinger-equation-in-polar-variables.html), for the first-order case, whose constrained structure is the contrast used here.
- [The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Bivector Plane](the-self-dual-and-anti-self-dual-split-spin-1-from-the-biquaternion-material-sector.html), for the carrier and the reality obstruction.
- [The Third Polarization and the Self-Dual Split of the Massive Field Strength](the-third-polarization-and-the-self-dual-split-of-the-massive-field-strength.html), for the three on-shell parameters.
- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter", *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, for the tensor formulation with unit-vector multipliers.
- Paul Adrien Maurice Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for the constraint analysis and the classification of constraints.
- Alexandre Proca, "Sur la théorie ondulatoire des électrons positifs et négatifs", *Journal de Physique et le Radium* **7** (1936) 347–353, for the equation and its mass.
