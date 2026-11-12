# __The Variational Principle and the Proca Equation in Biquaternionic Polar Variables__

## Introduction

This article substitutes the polar word of the material sector into the Proca action and reads the result. It is the polar companion of *The Variational Principle and the Proca Equation in Biquaternionic Form*, and it depends on three articles: *The Proca Equation in Biquaternionic Polar Variables* for the word and the equation in the chart, that element-form variational article for the action, and *The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector* for the carrier.

**The substitution.** The element-form action is

$$
S[\tilde A_\Phi]=\int d^4r\;\Bigl[\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)-\tfrac12\,k_m^2\,\langle\tilde A_\Phi\rangle_\natural\Bigr],
$$

and the word of the material sector is piecewise,

$$
\tilde A_\Phi=\varepsilon\,i\,r\,\tilde U_{\Psi,\mathrm b}\ \ (\langle\tilde A_\Phi\rangle_\natural<0),
\qquad
\tilde A_\Phi=r\,\tilde U_{\Psi,\mathrm b}\,\hat u\ \ (\langle\tilde A_\Phi\rangle_\natural>0),
$$

with $r>0$, $\varepsilon=\pm1$, and $\tilde U_{\Psi,\mathrm b}$ the boost of rapidity $\theta_{\mathrm{rpd}}$ and axis $\hat u_{\mathrm b}$. On the timelike branch the parameters are $r$ and the boost's three; on the spacelike branch they are $r$, the signed rapidity and the direction $\hat u$. Two branches, four parameters each.

**Three things are established, and their status differs.**

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
\begin{cases}+\tfrac12\,k_m^2\,r^2, & \text{timelike},\\[2pt] -\tfrac12\,k_m^2\,r^2, & \text{spacelike}.\end{cases}
$$

The sign of the mass term in the chart **is** the branch: it is the causal character of the four-vector, read as the sign of the term. This is the article's cleanest new statement.

*Second, the Euler–Lagrange equations in the chart are the transformed field equation.* The word is a diffeomorphism from its parameter set onto the branch, so a change of variables carries the variational problem into the chart without any loss: four parameters, four equations, and the equations are the two displays of the polar article — the scale equation with the frame's quadratic source, and the frame transport. Nothing has to be re-derived, and nothing can differ.

*Third, the count of multipliers is not the count of constraints.* The parametrization absorbs the unit conditions of the boost exactly, so no Lagrange multiplier is needed for the normalization of the frame — in contrast with the tensor formulation of Takabayasi, whose unit vector requires three multipliers and whose phase requires a fourth. But the Proca system still has its own constraint: the Hessian of the chart's Lagrangian has rank three and not four, and the missing direction is the one that changes the scalar potential at fixed vector potential. That is the primary constraint of the vector field, and the Lorenz condition is its secondary partner. The chart relabels them; it does not remove them.

**What is at stake in the contrast.** The Schrödinger polar article's action is first order in the time derivative, and its momenta vanish identically, so six of the eight are constraints and the closure needs Dirac analysis. The Proca action is second order, its Hessian has rank three out of four, and its single constraint is the standard one of a massive vector field. So the two polar variational principles are not the same kind of object, and the difference is the order of the Lagrangian, not the algebra.

The conventions are those of the two companion articles: $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with central $i$; the material sector $\mathbb{B}_\Phi$ anti-Hermitian; $\mathrm{Sc}$ the coefficient of $e_t$; $\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^{\natural}$ the quaternionic norm, real on $\mathbb{B}_\Phi$; $\partial/\partial R_t=-i\,\partial/\partial r'_t$; $\Box_\Phi=\Delta_\Phi-\partial^2/\partial{r'_t}^2$; $k_m=mc/\hbar$.

## The Action in the Chart

**The field term.** Write $\tilde F=\mathrm{Vect}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)$ and $S=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)$, so that the conjugate gradient is the sum of a scalar and a pure vector,

$$
(\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi=S+\tilde F .
$$

Squaring, the cross term is $2S\tilde F$, whose scalar part vanishes because $\mathrm{Sc}(\tilde F)=0$; hence

$$
\mathrm{Sc}\Bigl[\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr)^2\Bigr]=S^2+\mathrm{Sc}\bigl(\tilde F\tilde F\bigr),
$$

and the field term is the full quadratic minus the scalar square. The subtraction is the projection that the element form performs silently: $\tilde F$ is the antisymmetric part, and $\mathrm{Sc}(\tilde F^2)$ is the part of the full square that survives it. The identity is exact, holds for every element of $\mathbb{B}$ and not only on shell, and is verified by direct multiplication.

**The mass term.** On the timelike branch the norm is $-r^2$, because $(\varepsilon ir\tilde U)(\varepsilon ir\tilde U)^{\natural}=\varepsilon^2i^2r^2\tilde U\tilde U^{\natural}=-r^2$; on the spacelike branch it is $+r^2$, because $(r\tilde U\hat u)(r\tilde U\hat u)^{\natural}=r^2\tilde U\hat u\hat u^{\natural}\tilde U^{\natural}=r^2\tilde U(-\hat u)(-\hat u)\tilde U^{\natural}=r^2$. Hence

$$
-\tfrac12k_m^2\langle\tilde A_\Phi\rangle_\natural=
\begin{cases}+\tfrac12k_m^2r^2, & \text{timelike},\\[2pt]-\tfrac12k_m^2r^2, & \text{spacelike}.\end{cases}
$$

**The sign is the branch.** In the element form the mass term is indefinite, because $\langle\tilde A_\Phi\rangle_\natural$ is indefinite. In the chart it becomes a definite power of one positive parameter, and its sign is a property of the branch. For a timelike field the scale enters the Lagrangian with the sign of a positive mass term and the scale equation has the standard massive form; for a spacelike field the sign is reversed. Nothing in the element form displays this, because nothing in the element form distinguishes the two branches.

**The polar Lagrangian.** Collecting the two pieces,

$$
\boxed{\;\mathcal{L}=\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\Bigl[\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr)^2\Bigr]-\tfrac12S^2-\tfrac12k_m^2\langle\tilde A_\Phi\rangle_\natural\;}
$$

with the last term read from the branch. The three pieces are the full quadratic of the conjugate gradient, the negative square of its scalar part, and the mass. The middle piece is not a gauge-fixing term added by hand: it is what the projection removes, and it is present in the element form already, hidden inside $\mathrm{Re}\,\mathrm{Sc}(\tilde F\tilde F)$. In the chart it is displayed, and displayed is where its rôle can be read: its variation is what produces the Lorenz condition as an equation.

**The parameters.** On the timelike branch the field is $\tilde A_\Phi(q)$ with $q=(r,\theta_{\mathrm{rpd}},\vartheta_1,\vartheta_2)$ and the two angles parametrizing $\hat u_{\mathrm b}$; the discrete $\varepsilon$ is not varied, because it is a label and not a coordinate. On the spacelike branch $q=(r,\theta_{\mathrm{rpd}},\vartheta_1,\vartheta_2)$ with the angles those of $\hat u$. In both cases four.

## The Euler–Lagrange Equations

**The change-of-variables argument.** The word is a bijection from the parameter set onto the branch, and both are open subsets of four-dimensional spaces; it is smooth with smooth inverse away from the coordinate singularity at the pure scalar-potential line. A diffeomorphism carries a variational problem to a variational problem: if $\tilde A_\Phi=\Phi(q)$ and $S=\int\mathcal{L}(\Phi(q),\partial\Phi(q))$, then

$$
\frac{\delta S}{\delta q^i}=\Bigl(\frac{\delta S}{\delta\tilde A_\Phi}\Bigr)\Big|_{\tilde A_\Phi=\Phi(q)}\cdot\frac{\partial\Phi}{\partial q^i},
$$

and the Jacobian $\partial\Phi/\partial q^i$ is invertible on the branch. So the Euler–Lagrange equations in the chart vanish if and only if the element-form equation holds, and their content is the field equation and nothing else. This is an identity of the calculus, not a claim about the algebra, and it is what makes the polar variational principle exact.

**The explicit form.** Performing the differentiation gives the two displays of the polar article. The scalar part of the transformed equation is

$$
\bigl(\Box_\Phi-k_m^2\bigr)r+r\sum_\mu\mathrm{Sc}\bigl(\Gamma_\mu^2\bigr)=0,
\qquad
\Gamma_\mu=\tilde U_{\Psi,\mathrm b}^{-1}\frac{\partial\tilde U_{\Psi,\mathrm b}}{\partial R_\mu},
$$

and the traceless part is

$$
\sum_\mu\Bigl(\frac{\partial\Gamma_\mu}{\partial R_\mu}+\Gamma_\mu^2\Bigr)
+2\sum_\mu\frac{\partial\ln r}{\partial R_\mu}\Gamma_\mu=0 .
$$

Both are exactly the equations that the direct substitution of the word into the field equation gives, which is the content of the change-of-variables argument: the variational route and the substitution route are the same route. For a fixed boost axis the pair reduces to

$$
\bigl(\Box_\Phi-k_m^2\bigr)r+\tfrac14r\sum_\mu\Bigl(\frac{\partial\theta_{\mathrm{rpd}}}{\partial R_\mu}\Bigr)^2=0,
\qquad
\sum_\mu\frac{\partial}{\partial R_\mu}\Bigl(r^2\frac{\partial\theta_{\mathrm{rpd}}}{\partial R_\mu}\Bigr)=0 ,
$$

which is the form the polar article verifies numerically. The mass term enters the first with the sign $+k_m^2r$ on the timelike branch, as the branch's sign of the mass term requires.

**What the variation of the middle piece does.** The term $-\tfrac12S^2$ is the only piece that pairs the scalar projection with itself. Its variation produces the scalar equation that is the Lorenz condition, and the remaining pieces produce the two dynamical equations. In this sense the chart separates the three jobs that the element form performs at once: the curl term carries the propagation, the square carries the constraint, and the mass carries the scale. The separation is a rewriting, but it is a rewriting that names each job.

## The Mass Term, the Branch, and the Constraint

**The Hessian has rank three.** The kinetic part of the chart's Lagrangian is $\tfrac12\epsilon\vec E^2$ with $\vec E=-\nabla a'_t-\partial_{t'}\vec A$, so only $\vec A$ carries velocities, and

$$
\frac{\partial^2\mathcal{L}}{\partial\dot q^i\partial\dot q^j}
=\epsilon\,\frac{\partial\vec A}{\partial q^i}\cdot\frac{\partial\vec A}{\partial q^j},
$$

an outer product of four vectors in three dimensions. Its rank is therefore at most three, and it is exactly three wherever the four vectors $\partial\vec A/\partial q^i$ span $\mathbb{R}^3$, which they do at a generic point of the branch. So there is one null direction, and the chart has one primary constraint.

**The null direction is the scalar potential.** The four derivatives of $\vec A=-r\sinh\frac{\theta_{\mathrm{rpd}}}{2}\hat u_{\mathrm b}$ along the branch are not independent: the combination that changes $r$ and $\theta_{\mathrm{rpd}}$ while holding the product $r\sinh\frac{\theta_{\mathrm{rpd}}}{2}$ fixed leaves $\vec A$ unchanged and changes $a'_t=r\cosh\frac{\theta_{\mathrm{rpd}}}{2}$. That combination is the null vector, and it is exactly the direction in which the field changes by the gradient of a function of time — the primary constraint $\pi^0=0$ of the vector field, written in the chart's letters.

**The Lorenz condition is the secondary constraint.** Preserving the primary constraint in time produces the Lorenz condition, which in the chart is the single scalar equation displayed in the polar article. So the pair is second class, the physical count is three, and the chart's four parameters lose one on shell. That is the same count as the polarizations, and the same count as the element form's.

**No multipliers for the units, and no escape from the constraint.** The two statements must be kept apart.

| what is counted | element form | chart | Takabayasi's tensor form |
| --- | --- | --- | --- |
| normalization of the frame | automatic | automatic, by the word | three multipliers $A_1,A_2,A_3$ |
| phase | none | none | one multiplier |
| primary constraint | $\pi^0=0$ | rank-three Hessian | rank-three Hessian |
| secondary constraint | Lorenz | Lorenz | Lorenz |

The chart's gain is the first row: the boost is parametrized, not constrained, so its unit condition costs nothing. The chart's non-gain is the third and fourth rows: the vector field's own constraints are untouched, and any claim that the polar form removes them would be false. This is the honest ledger, and it is the opposite of the Schrödinger case, where the *action* is first order and the constraints are the momenta's vanishing.

**Why the Schrödinger case differs.** There the Lagrangian is linear in $\dot\theta_{\mathrm{pha}}$, so the momentum conjugate to $r$ vanishes identically and the system is a constrained one whose closure needs Dirac analysis. Here the Lagrangian is quadratic in the velocities, the momenta are the velocities' images under a rank-three map, and there is exactly one constraint pair. The order of the Lagrangian, and not the choice of variables, is what decides.

## The Lorenz Condition in the Chart

**One equation on four parameters.** The chart's form of the condition is

$$
S=\varepsilon\Bigl[c\,\partial_{r'_t}r-s\,\hat u_{\mathrm b}\cdot\nabla r
+\tfrac12rs\,\partial_{r'_t}\theta_{\mathrm{rpd}}-\tfrac12rc\,\hat u_{\mathrm b}\cdot\nabla\theta_{\mathrm{rpd}}-rs\,\nabla\cdot\hat u_{\mathrm b}\Bigr]=0,
$$

with $c=\cosh\frac{\theta_{\mathrm{rpd}}}{2}$ and $s=\sinh\frac{\theta_{\mathrm{rpd}}}{2}$. It is the divergence of the four-vector in the chart's variables, and it is the secondary constraint. On shell it removes one of the four parameters and leaves three.

**It is implied, and the variational reading says why.** In the element form the condition follows from the divergence of the equation. In the chart it follows from the variation of the $-\tfrac12S^2$ term together with the rest, and it is the statement that the longitudinal part of the field is not free. There is no multiplier attached to it, and there is no gauge orbit along which it could be reached: it is one equation among the four.

**What it is not.** It is not the continuity equation of a fluid and it is not a guidance equation, because the material sector has no phase and therefore no phase current to conserve. The scalar Madelung pair is a pair because the field is one complex function; here the field is a real four-vector, and the condition is a single divergence. The variational principle does not manufacture the missing half.

## What the Polar Variational Principle Adds and What It Does Not

**Adds.**

- The action in the chart, with the mass term reduced to a definite power of the modulus. Its sign is the branch, and that is a statement the element form cannot make.
- The explicit separation of the element-form Lagrangian into curl, scalar square and mass, with the middle piece identified as what the projection removes and as the term whose variation carries the Lorenz condition.
- The exactness of the chart's variational principle, with the change-of-variables argument making the equivalence a matter of calculus.
- The correct count: no multipliers for the unit conditions, one primary and one secondary constraint for the vector field, three physical parameters on shell.
- The fixed-axis reduction of the two Euler–Lagrange equations to a massive scale equation with a rapidity-gradient source and a conservation law with density $r^2$.

**Does not add.**

- No new prediction and no new solution. The solutions are the element form's, and the chart only re-reads them.
- No removal of the constraints. The rank-three Hessian is the vector field's, and the chart displays it rather than dissolving it.
- No second current. The action's symmetries are the element form's, and the absence of a central phase is inherited unchanged.
- No simplification of the equations. The chart's equations are nonlinear in the parameters, and they are longer than the field equation they encode.

**The distinction that matters.** The polar variational principle is a coordinate change of a standard variational problem, and its value is entirely in what the coordinates display: the sign of the mass term as the branch, the three jobs of the three pieces, and the constraint's exact location. It is not a new principle, and the article claims nothing of the kind.

## Open Questions

1. **The spacelike branch's equations.** The scale equation and the transport equation are displayed here for the timelike branch, where the frame is the only object differentiated. On the spacelike branch the direction $\hat u$ is differentiated as well, and the two are locked; the explicit Euler–Lagrange equations of that branch are not written out, and the polar article records the same gap.
2. **The crossing set.** The chart is a diffeomorphism on each branch and fails on the lightlike set of field values. What the variational problem does across the crossing — whether the action can be continued, and whether the continuation is stationary — is not settled.
3. **The constraint analysis in the chart.** The rank-three Hessian and the second-class pair are identified here but not carried through the Dirac bracket. The canonical quantization article performs the analysis in the component variables; whether the chart's variables simplify the bracket, or merely obscure it, is open.

## Summary

Substituting the polar word of the material sector into the Proca action gives

$$
\mathcal{L}=\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\Bigl[\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr)^2\Bigr]-\tfrac12S^2-\tfrac12k_m^2\langle\tilde A_\Phi\rangle_\natural ,
$$

with the mass term $+\tfrac12k_m^2r^2$ on the timelike branch and $-\tfrac12k_m^2r^2$ on the spacelike one: the sign of the mass term is the branch. The three pieces are the full quadratic of the conjugate gradient, the negative square of its scalar part, and the mass; the middle piece is what the element form's projection removes, and its variation carries the Lorenz condition.

The chart is a diffeomorphism onto the branch, so its Euler–Lagrange equations are the transformed field equation: the scale equation with the frame's quadratic source and the frame transport, which is what the polar article's direct substitution gives. The chart needs no Lagrange multiplier for the normalization of the boost, in contrast with the tensor formulation — but it does not remove the vector field's own constraints: the Hessian has rank three, its null direction is the scalar potential at fixed vector potential, and the Lorenz condition is the secondary constraint. Four parameters, four equations, three physical parameters on shell.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\eta^2=-e_t$ |
| $i$ | Central scalar imaginary |
| $\mathbb{B}_\Phi$, $\mathbb{B}_\Psi$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathrm{Sc}$, $\mathrm{Vect}$, ${}^{\natural}$, ${}^{*}$ | Scalar part, vector part, quaternion and Hermitian conjugations |
| $\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^{\natural}$ | Quaternionic norm; real on $\mathbb{B}_\Phi$ |
| $\tilde A_\Phi=\varepsilon ir\tilde U_{\Psi,\mathrm b}$ | Timelike branch of the word |
| $\tilde A_\Phi=r\tilde U_{\Psi,\mathrm b}\hat u$ | Spacelike branch, boost axis locked to $\hat u$ |
| $r>0$, $\theta_{\mathrm{rpd}}$, $\hat u_{\mathrm b}$, $\hat u$ | Modulus, rapidity, boost axis, direction |
| $\varepsilon=\pm1$ | Sign of the scalar potential, timelike branch |
| $\Gamma_\mu=\tilde U^{-1}\partial_\mu\tilde U$ | Frame bracket (Maurer–Cartan form) |
| $S=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)$ | Lorenz scalar |
| $\mathcal{L}$ | Lagrangian density in the chart |
| $\Box_\Phi=\Delta_\Phi-\partial^2/\partial{r'_t}^2$ | d'Alembertian of the corpus |
| $k_m=mc/\hbar$ | Mass wave number |

## Further Reading

- [The Proca Equation in Biquaternionic Polar Variables](the-proca-equation-in-biquaternionic-polar-variables.html), for the word and the equation in the chart.
- [The Variational Principle and the Proca Equation in Biquaternionic Form](the-variational-principle-and-the-proca-equation-in-biquaternionic-form.html), for the element-form action, its variation and the currents.
- [The Proca Equation: Massive Spin 1 in Biquaternionic Form](the-proca-equation-massive-spin-1-in-biquaternionic-form.html), for the equation, the Lorenz condition and the polarizations.
- [Canonical Quantization of the Biquaternion Proca Field](canonical-quantization-of-the-biquaternion-proca-field.html), for the Legendre transform and the constraint structure in the component variables.
- [The Variational Principle and the Schrödinger Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-schrodinger-equation-in-biquaternionic-polar-variables.html), for the first-order case, whose constrained structure is the contrast used here.
- [The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector](the-self-dual-and-anti-self-dual-split-spin-1-from-the-biquaternion-material-sector.html), for the carrier and the reality obstruction.
- [The Third Polarization and the Self-Dual Split of the Massive Field Strength](the-third-polarization-and-the-self-dual-split-of-the-massive-field-strength.html), for the three on-shell parameters.
- Takehiko Takabayasi, "Relativistic hydrodynamics of the Dirac matter", *Progress of Theoretical Physics Supplement* **4** (1957) 1–80, for the tensor formulation with unit-vector multipliers.
- Paul Adrien Maurice Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for the constraint analysis and the classification of constraints.
- Alexandre Proca, "Sur la théorie ondulatoire des électrons positifs et négatifs", *Journal de Physique et le Radium* **7** (1936) 347–353, for the equation and its mass.
