# __The Klein–Gordon Path Integral in Biquaternionic Polar Variables__

## Introduction

**The integral is the companion's, and this article is a reading of it.** *The Klein–Gordon Path Integral in Biquaternionic Form* defines the functional integral over central-valued fields, evaluates the free Gaussian on a lattice, and identifies its two-point function with the propagator. This article substitutes the polar word into that integral and reads where each factor of the word lands.

**The word on a central field is two functions and a sign.** The boost factor has neither rapidity nor axis to carry and is $e_t$; the rotor has neither angle nor axis and is the sign that the branch of the modulus deposits. What survives is the scale $r$ and the angle $\theta_{\mathrm{pha}}$, both central. The collapse is the companion article's, *The Klein–Gordon Equation in Biquaternionic Polar Variables*, §*The collapse of the word*, and none of its theory is repeated here.

**Three things change, and they are the article's content.** First, the measure gains a Jacobian at every point of spacetime. Second, the exponent splits into a scale part and a phase part, and the phase enters only through its derivatives. Third, the two Euler–Lagrange equations of the variational companion become the two stationary points of the two integrals.

**The findings are five, and each is one sentence.**

- The measure is $\prod_x r\,\mathrm{d}r\,\mathrm{d}\theta$: a product over points of one factor and two differentials, and the product is a number on a lattice and a formal divergence in the continuum.
- The chart's failure at a node costs nothing, because the Jacobian vanishes exactly where $r$ does.
- Stationarity in the scale gives the amplitude equation and stationarity in the angle gives the transport equation, so the polar pair of the variational companion is the two saddles of this one integral.
- The Euclidean chart is a sum of four squares, so convergence is term by term and the only obstruction is a negative mass squared.
- The change of variables is exact through the cancellation of three factors — the Jacobian, the determinant of the parameter metric, and the Fresnel factor of the Gaussian.

**What the article does not do.** It does not produce a second integral, does not define the continuum measure, and does not treat an interaction. The pair $(r,\theta_{\mathrm{pha}})$ is a coordinate system on the field, so the value of the integral cannot change; what changes is which object in it is legible.

## Conventions

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with $e_t=1$, $\vec e_\mu^{2}=-e_t$, $i$ central, $\mathrm{Sc}$ the coefficient of $e_t$ and $\mathrm{Tr}=2\,\mathrm{Sc}$. The pairing is the Hermitian $\mathrm{Sc}(\cdot^{*}\cdot)$. The word is $\tilde\Xi=r e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ with $r>0$, $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$, $\tilde U_{\Psi,\mathrm b}$ the boost and $\tilde u_{\mathrm r}$ the rotor; the ranges are those of the polar equation article and are not restated.

**The action and the weight.** The companion's action is

$$
S[\tilde\Xi]=\frac{\hbar}{2}\int d^{4}r\;\Bigl[\mathrm{Sc}\bigl(\partial_{r'_t}\tilde\Xi^{*}\,\partial_{r'_t}\tilde\Xi\bigr)-\sum_{\eta=1}^{3}\mathrm{Sc}\bigl(\partial_{\eta}\tilde\Xi^{*}\,\partial_{\eta}\tilde\Xi\bigr)-k_m^{2}\,\mathrm{Sc}\bigl(\tilde\Xi^{*}\tilde\Xi\bigr)\Bigr],
$$

with the metric of the material coordinate written out: the temporal slot enters with $+$ and the three spatial ones with $-$, which is $\partial/\partial R_t=-i\,\partial/\partial r'_t$ in explicit form. This is the free companion's action with the same convention; the companion's $\frac12\int\mathrm{Sc}[\tilde\Xi^{*}(\Box_\Phi-k_m^{2})\tilde\Xi]$ differs from it by a boundary term, and the polar bracket below follows from this display through the identity $\mathrm{Sc}(\partial_\mu\tilde\Xi^{*}\partial_\mu\tilde\Xi)=(\partial_\mu r)^{2}+r^{2}(\partial_\mu\theta_{\mathrm{pha}})^{2}$. The weight of one configuration is $\exp(iS/\hbar)$, central and $*$-unitary. On a central field $\tilde\Xi=re^{i\theta_{\mathrm{pha}}}e_t$ the weight becomes

$$
\frac{i}{\hbar}S=\frac{i}{2}\int d^{4}r\;\Bigl[(\partial_{r'_t}r)^{2}-\lvert\nabla r\rvert^{2}
+r^{2}\Bigl((\partial_{r'_t}\theta_{\mathrm{pha}})^{2}-\lvert\nabla\theta_{\mathrm{pha}}\rvert^{2}\Bigr)-k_m^{2}r^{2}\Bigr].
$$

**The factor two, stated once.** The bracket is the Madelung functional of the variational companion, *The Variational Principle and the Klein–Gordon Equation in Biquaternionic Polar Variables*, §*The action, assembled*, which writes it without the $\hbar$ and without the $\tfrac12$. The companion's action is $\hbar$ times the half of it, so the weight is $\exp(\tfrac{i}{2}S_{\mathrm{Madelung}})$. The stationarity is unaffected by the constant, and every equation below is the variational companion's.

## The Word on a Central Field

**One block of the metric survives.** The polar variational companion writes the kinetic Lagrangian as $g_{ab}(p)\partial_\mu p^{a}\partial_\mu p^{b}$ over eight parameters with the pull-back metric of the word. On a central field the rapidity vanishes, the axes are frozen and the rotor is a sign, so the metric is diagonal with $g_{rr}=1$ and $g_{\theta\theta}=r^{2}$ and every other entry zero. The exponent is therefore one diagonal quadratic form in two real functions.

**The sign is bookkeeping and not a parameter.** The chart holds the angle in $(-\pi/2,\pi/2]$ and deposits the half turn in the rotor's sign, so the pair $(r,\theta_{\mathrm{pha}},\varepsilon)$ with $\varepsilon=\pm1$ is a bijection onto the nonzero complex scalars. The measure below integrates the angle over a full turn; the two halves of the turn with the two signs are the same domain written twice. **The sign is a chart of the circle and contributes no factor to the measure**, and the count of parameters at each point is two.

**Nothing in the exponent prefers a sign.** The action depends on $r$, on $\partial r$, on $\partial\theta_{\mathrm{pha}}$ and on $r^{2}$, and on $\varepsilon$ not at all. So the two signs of one configuration carry the same weight, and the sum over them is a factor of two per point in a quantity that is only ever used as a ratio.

## The Measure

**The substitution is a change of variables at each point.** At one point the complex field is two real numbers and the chart is the polar map of the plane, so

$$
\mathcal{D}\tilde\Xi=\prod_{x}r(x)\,\mathrm{d}r(x)\,\mathrm{d}\theta_{\mathrm{pha}}(x),
$$

and the Jacobian is the product of the radial factor over the points. Nothing else appears: no derivative, no dependence on the angle, no dependence on the other point of any pair. **The polar measure is a functional of the scale alone.**

**On a lattice the product is finite and the measure is exact.** At $N$ sites the substitution is an ordinary change of variables in $\mathbb{R}^{2N}$, the Jacobian is $\prod_{i}r_i$, and the integral is an ordinary $2N$-dimensional integral. This is the companion's own regulator, and the polar form uses the same one.

**In the continuum the product is formal, and the article says so.** The product $\prod_x r(x)$ is $\exp\bigl(\int d^{4}x\,\ln r(x)\,\delta^{(4)}(0)\bigr)$, which is divergent at every point and requires a subtraction. This is not a new difficulty: it is the companion's measure problem, and it appears in the chart as one explicit factor rather than as a general warning. **The chart's contribution is to name the object the difficulty lives in**, and the name is the radial Jacobian.

**What the measure does not contain.** It is invariant under a central phase, because $r$ is. It is positive, because $r>0$. It does not couple the scale to the angle. Each of the three statements is used below.

## The Exponent

**Two terms and no cross term.** The weight's bracket of §*Conventions* is a sum of a scale part, $(\partial_{r'_t}r)^{2}-\lvert\nabla r\rvert^{2}-k_m^{2}r^{2}$, and a phase part, $r^{2}\bigl((\partial_{r'_t}\theta_{\mathrm{pha}})^{2}-\lvert\nabla\theta_{\mathrm{pha}}\rvert^{2}\bigr)$. The two are separate because a central field's word is a product of a real function and a unit, and the derivative of a product separates into the derivative of the modulus and the modulus times the derivative of the phase.

**The phase enters through its derivatives and through nothing else.** No term of the exponent contains $\theta_{\mathrm{pha}}$. The angle is a cyclic coordinate at every point, and the gauge transformation of the coupled companion is the translation of that coordinate. In the free case the consequence is the article's main structural fact: **the phase is integrated over a circle at every point and its value nowhere appears**, so the phase integral sees only the gradient field.

**The scale enters twice, and the second time is the coupling.** The scale appears as its own gradient and as the weight $r^{2}$ of the phase's square. That weight is the density, so the chart's exponent is the statement that the phase's kinetic term is the density times the squared four-gradient of the action. The variational companion says the same thing with the statement that the frame density multiplies the bracket.

## The Two Saddles Are the Companion's Pair

**Stationarity in the scale.** Varying $r$ in the bracket of §*Conventions* gives

$$
\Box_\Phi r=r\Bigl[k_m^{2}-\bigl(\partial_{r'_t}\theta_{\mathrm{pha}}\bigr)^{2}+\lvert\nabla\theta_{\mathrm{pha}}\rvert^{2}\Bigr],
$$

which is the amplitude equation of the polar equation article, §*The amplitude equation*, rearranged. Read through $S_{\tilde\Xi}=\hbar\theta_{\mathrm{pha}}$ and multiplied by $\hbar^{2}$, it is $(\partial_{r'_t}S_{\tilde\Xi})^{2}-\lvert\nabla S_{\tilde\Xi}\rvert^{2}=m^{2}c^{2}-\hbar^{2}\Box_\Phi r/r$, the mass shell shifted by the quantum potential.

**Stationarity in the angle.** Varying $\theta_{\mathrm{pha}}$ gives

$$
\nabla\cdot\bigl(r^{2}\nabla\theta_{\mathrm{pha}}\bigr)-\frac{\partial}{\partial r'_t}\Bigl(r^{2}\frac{\partial\theta_{\mathrm{pha}}}{\partial r'_t}\Bigr)=0,
$$

which is the transport equation, §*The transport equation*. It is the divergence of the density times the phase gradient, and the density times the phase gradient is the current.

**The pair is therefore the two saddles, and this is one statement and not two.** The variational companion derives the pair from one functional and exhibits it as two equations; the integral exhibits the same pair as the stationary conditions of two nested integrals. **The chart's reading of the pair is that the amplitude equation is the scale's saddle and the transport equation is the angle's saddle**, and the identification is exact.

**The check is exact in one direction.** Take one interior point of a chain with two links, weights $w_1=0.83$ and $w_2=1.47$, link phases $-0.61$ and $0.29$, and fixed endpoints $0.11$ and $-0.74$. The integral of the weight over the interior angle evaluates to $0.867685832861$ by quadrature, and the stationary value times the Fresnel factor $\sqrt{\pi/\alpha}$ evaluates to $0.867685832861$, a relative agreement of $1.2\times10^{-13}$; the stationary point satisfies the discrete divergence condition to $4\times10^{-16}$ against a link current of $0.28$. **The phase integral is its saddle times a Fresnel factor, and the saddle is the transport equation.**

## The Phase Is a Constraint and Not a Field

**The angle's integral is a Gaussian and its content is a determinant and a condition.** Because the exponent is quadratic in $\partial\theta_{\mathrm{pha}}$ and free of $\theta_{\mathrm{pha}}$, integrating the angle gives the inverse square root of the determinant of $-\partial_\mu r^{2}\partial_\mu$ and, whenever the integrand carries an insertion that depends on the angle, a factor supported on configurations whose current is conserved. **The transport equation is not an equation of motion in this reading; it is what the phase leaves behind.**

**What the insertion costs.** The companion's generating functional couples a central source, and in the chart that source is $J^{*}r e^{i\theta_{\mathrm{pha}}}$ plus its conjugate. The source multiplies the phase's exponential, so it is the one object in the article that sees the value of the angle and not its gradient. With a source the angle's integral stops being Gaussian. **The chart's statement of what a source does is that it couples to the coordinate whose gradient the free theory conserves**, which is the functional form of the statement that a source changes the charge.

**What the constraint is not.** The constraint is the divergence of a current and not the vanishing of a field, so it removes one function of four variables and leaves the amplitude free. The count matches the companion's: one complex field is two real functions, and one constraint on one of them leaves one amplitude and one transverse phase.

## The Scale's Integral

**At fixed angle the scale's integral is Gaussian.** The bracket is quadratic in $r$ and in $\partial r$, with the coefficient $r^{2}\bigl((\partial_{t}\theta)^{2}-\lvert\nabla\theta\rvert^{2}\bigr)-k_m^{2}$ multiplying $r^{2}$. So the two integrals are nested and either may be done first, and the chart's two orders are the two saddles of §*The Two Saddles Are the Companion's Pair* in the opposite order.

**The radial domain is automatic.** The Cartesian integral runs over the whole plane at each point; the chart's runs over $r\ge0$ with the weight $r$, and the two agree because the polar map of the plane is onto the half-line with that Jacobian. There is no image of $r<0$ to compensate.

**The scale's integral is not Gaussian once the angle is summed.** The coefficient of $r^{2}$ is the phase's squared gradient, which is integrated over, so the effective action for the scale is not quadratic. The chart's exponent is therefore a Gaussian in one variable and a quartic-type coupling in the other, and the coupling is the term $r^{2}(\partial\theta)^{2}$ that the variational companion calls the density's weight of the bracket.

## The Change of Variables, Exactly

**Three factors must cancel, and they do.** A change of variables in a Gaussian changes three things: the measure (Jacobian $\prod r$), the quadratic form (the parameter metric, whose determinant is $\prod r^{2}$ for the central block), and the Fresnel factor (the inverse square root of the determinant, hence $\prod r^{-1}$). The product is one. **The exactness of the polar reading is the cancellation of these three factors**, and it is the reason the chart can claim to read the integral without changing it.

**The cancellation is checked twice, once as an integral and once as a determinant.** The two-site Euclidean Gaussian with quadratic form $\xi^{\dagger}A\xi$ and $A=\begin{pmatrix}1.7&0.4\\0.4&1.1\end{pmatrix}$ evaluates to $5.771698480169$ in Cartesian variables, which is $\pi^{2}/\det A$, and to $5.771698480169$ in the chart with the measure $r_1\mathrm{d}r_1\mathrm{d}\theta_1\,r_2\mathrm{d}r_2\mathrm{d}\theta_2$, a relative agreement of $3.7\times10^{-15}$. Separately, on three sites with random scales and angles, the determinant of the polar second variation divided by $\prod r_i^{2}$ times the Cartesian determinant is $1.000000000000000$. **The Jacobian, the metric and the Fresnel factor are one factor written three ways.**

**The identity $\lvert\partial\xi\rvert^{2}=(\partial r)^{2}+r^{2}(\partial\theta)^{2}$ is the pointwise version.** It holds exactly for the analytic derivative, and to the second order of the difference scheme for a finite one: the residual of a centred difference of step $10^{-2}$, $5\times10^{-3}$ and $2.5\times10^{-3}$ is $3.96\times10^{-5}$, $9.90\times10^{-6}$ and $2.48\times10^{-6}$, falling by four as the step halves. **The chart is exact in the continuum and is a product rule away from it on a lattice.**

## The Nodes

**The chart fails where the field vanishes, and the measure does not.** The word needs $r>0$, and on the centre $r=0$ is exactly the nodal set of the wave. The polar measure carries the factor $r$, so the neighbourhood of a node carries weight proportional to $r$ and contributes nothing. **The set where the chart fails is the set where the Jacobian vanishes**, and the two integrals agree for that reason and not by a limiting argument.

**What is lost is differentiability and not the integral.** The action is undefined at a node because the phase of zero is undefined, and the current vanishes there. The variational companion writes the pair on the products $\rho_{\mathrm{num}}\partial S_{\tilde\Xi}$, which stay differentiable, and the integral's version of the same repair is that the weight of the offending configurations is zero. **The chart's domain is the complement of the nodal set, and the complement has full measure in the polar measure.**

## The Euclidean Chart

**The Wick rotation turns the bracket into four squares.** With $i r'_t=c\tau$ the bracket of §*Conventions* becomes

$$
S_{E}=\frac{1}{2}\int d^{4}r_{E}\;\Bigl[(\partial_{c\tau}r)^{2}+\lvert\nabla r\rvert^{2}
+r^{2}\Bigl((\partial_{c\tau}\theta_{\mathrm{pha}})^{2}+\lvert\nabla\theta_{\mathrm{pha}}\rvert^{2}\Bigr)+k_m^{2}r^{2}\Bigr],
$$

and the weight is $\exp(-S_E)$. Four terms and every one of them positive. **The convergence of the Euclidean functional is term by term in the chart**, and this is the sharpest form of the companion's statement that the Euclidean quadratic form is the biquaternion norm on the quaternion subspace.

**The mass is the only term that can change sign.** For $k_m^{2}<0$ the last term is negative, the radial integral grows at large $r$, and it does so uniformly in the angle because no other term contains $\theta_{\mathrm{pha}}$'s value. **The instability is radial and it is in the zero mode**, which is the companion's tachyon statement read as the failure of one of the four squares.

**The marginal case is visible in the chart and not in the Cartesian form.** At $k_m^{2}=0$ the constant mode has no restoring term in either variable, and the radial weight $r\,\mathrm{d}r$ leaves the integral of that mode divergent at large $r$. The chart names the mode: it is the one with $r$ constant and $\theta_{\mathrm{pha}}$ constant.

**The angle is compact and the weight is its measure.** In the Euclidean chart the phase runs over a circle with the weight $r^{2}(\partial\theta)^{2}$, which is the form of the planar model with a radial stiffness. The chart does not add a mechanism here; it records that the two variables of the exponent are one compact and one non-compact, and that the compact one appears only through its gradient.

## The Semiclassical Word

**The saddle is the classical field and the second variation is the parameter metric.** Expanding the bracket about a solution of the pair, the quadratic term is $g_{ab}(p)\partial_\mu\delta p^{a}\partial_\mu\delta p^{b}$ evaluated at the solution, with $g$ the polar variational companion's metric. The prefactor is the inverse square root of that operator's determinant. **The chart's one-loop factor is the determinant of the metric's operator**, and it is central because $g$ is built from $r$ and $\theta_{\mathrm{pha}}$ alone.

**The chart's determinant is the Cartesian one times the Jacobian's square.** That is the previous section's cancellation at the level of the fluctuation operator, and it is what makes the prefactor transform correctly: the amplitude gains $\prod r^{-1}$ from the determinant, the measure contributes $\prod r$, and the leftover $\prod r^{-1}$ is exactly the Jacobian of the change of variables in the amplitude.

**The Fresnel phase is the same constant counted in the same way.** Each integrated direction contributes $\sqrt{\pi/\alpha}$ with $\alpha$ complex in the Minkowski case, hence a phase $\arg(i^{-1/2})$ per direction, and the chart does not change the count. **The polar form relocates the constant and does not produce it**, which is the same finding as the free polar article's for the single-particle integral.

## The Placement Table

**Each factor of the word lands in one place, and the field case differs from the single-particle case.** The scale is in the measure, through the Jacobian, and in the exponent, through its gradient and through the density that weights the phase. The angle is in the exponent, through its gradient only. The boost and the rotor do not appear, and their absence is the statement that a central field has neither.

**Against the single-particle chart, the difference is the gradient.** For one history the scale is a number and lives in the measure alone, because a number has no derivative. For a field the scale is a function, so it has a gradient, and the gradient is a term of the exponent. **The scale is in the measure in both cases and in the exponent in one of them**, and the asymmetry is the difference between a path and a field.

**The gauge transformation would move one entry of the table.** A central phase multiplies the field, which in the chart translates $\theta_{\mathrm{pha}}$ and leaves $r$ and the measure alone. **The measure is gauge invariant because the Jacobian is the scale and the scale is gauge invariant**, and this is the fact the coupled companion turns on.

## What the Polar Reading Adds and Does Not Add

**Adds.**

- The measure's content, named: a radial Jacobian per point, exact on a lattice and formal in the continuum.
- The two saddles of one integral identified with the polar pair of the variational companion, one of them exact in one direction to $10^{-13}$.
- The phase's role, stated structurally: a Gaussian whose saddle is the transport equation, hence a constraint and not a field.
- The nodes' invisibility, as a consequence of the Jacobian and not as a convention.
- The Euclidean chart as four squares, with the tachyon and the marginal case located in one term each.
- The exactness of the change of variables, as the cancellation of three factors, checked as an integral and as a determinant.
- The placement table, and with it the reason the field chart carries the scale twice where the single-particle chart carries it once.

**Does not add.** No new value: the integral is the companion's number. No continuum measure and no regularisation of the Jacobian. No interaction. No statement about the operator setting. No fermionic-statistics question, which is not present for a scalar.

**The honest ledger.** The chart contributes one object the element form does not exhibit, the radial Jacobian; one identity the element form does not exhibit, the two saddles; and one reading, the phase as a constraint. It contributes nothing to the value, which is the point of a coordinate change, and it contributes a sharper statement of the measure problem, which is the point of doing it.

## Open Questions

1. **The Jacobian's regularisation.** Whether the product $\prod_x r(x)$ admits a subtraction that is natural to the framework — from the trace form, or from the biquaternion norm, or from the real structure — rather than the lattice's, is not settled. The chart makes the question one-dimensional per point, which may make it easier; it does not answer it.

2. **The winding sectors.** The angle is compact, so the field space splits by the winding of $\theta_{\mathrm{pha}}$ on a closed surface. Whether the polar integral in a fixed winding sector is a distinct object, and whether the sectors are summed with phases, is not treated. The variational companion's circulation is the classical shadow of the same question.

3. **The constraint's determinant.** The angle's integral produces the inverse square root of the determinant of $-\partial_\mu r^{2}\partial_\mu$, which depends on the scale and is therefore not a constant. Whether that determinant has a closed form on a lattice, and whether its scale dependence cancels against the radial integral, is not shown.

4. **The interaction.** A central interaction $\lambda r^{4}$ adds one term to the bracket and leaves the chart's structure unchanged; the exponent stays free of $\theta_{\mathrm{pha}}$'s value, so the phase remains a constraint. The article does not pursue it, and the statement is a conjecture about the chart and not a computation.

5. **The sign $\varepsilon$.** The article treats the sign as chart bookkeeping and sums it. Whether the two signs are distinguishable in any correlation function of the field — as opposed to of the word — is not examined, and the exponent's independence of the sign says they are not.

## Summary

The Klein–Gordon functional integral read in the word is the integral over a scale and an angle at every point, with the measure $r\,\mathrm{d}r\,\mathrm{d}\theta$ and the exponent

$$
\frac{i}{2}\int d^{4}r\;\Bigl[(\partial_{r'_t}r)^{2}-\lvert\nabla r\rvert^{2}
+r^{2}\Bigl((\partial_{r'_t}\theta_{\mathrm{pha}})^{2}-\lvert\nabla\theta_{\mathrm{pha}}\rvert^{2}\Bigr)-k_m^{2}r^{2}\Bigr].
$$

Three structural facts follow. The measure is a functional of the scale alone, so it is gauge invariant and positive, and its continuum form is a product over points that is exact on a lattice and formal in the continuum. The exponent is free of the angle's value, so the angle's integral is a Gaussian whose saddle is the transport equation: **the phase is a constraint, and the pair of the variational companion is the pair of saddles.** The chart's failure at the nodes is invisible, because the Jacobian vanishes there.

The change of variables is exact through three factors that cancel: the Jacobian of the measure, the determinant of the parameter metric, and the Fresnel factor of the Gaussian. The integral agrees with the Cartesian one to $3.7\times10^{-15}$ on a two-site lattice, and the determinant ratio is one to machine precision. In the Euclidean chart the exponent is four squares, so convergence is term by term and the only obstruction is a negative mass squared, which appears as the failure of the last square alone.

The placement table is the reading. The scale sits in the measure and in the exponent, because a function has a gradient where a number does not. The angle sits in the exponent and only through its gradient. The boost and the rotor are absent, which is what a central field is.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=r e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | The polar word; on a central field the last two factors are $e_t$ and $\pm e_t$ |
| $r>0$ | The scale; the modulus of the coefficient |
| $\theta_{\mathrm{pha}}\in(-\pi/2,\pi/2]$ | The angle; the action over $\hbar$, reduced into the range |
| $\varepsilon=\pm1$ | The branch sign of the modulus; the chart's other half turn |
| $\mathcal{D}\tilde\Xi=\prod_x r\,\mathrm{d}r\,\mathrm{d}\theta_{\mathrm{pha}}$ | The polar measure; its Jacobian is the scale at each point |
| $S[\tilde\Xi]$ | The companion's action; central, real, quadratic |
| $\exp(iS/\hbar)$ | The weight; central and $*$-unitary |
| $g_{ab}$ | The parameter metric of the polar variational companion; $g_{rr}=1$, $g_{\theta\theta}=r^{2}$ on the centre |
| $S_{\mathrm{Madelung}}$ | The variational companion's polar action; the weight is $\exp(\tfrac{i}{2}S_{\mathrm{Madelung}})$ |
| $\Box_\Phi r=r\bigl[k_m^{2}-(\partial_{r'_t}\theta_{\mathrm{pha}})^{2}+\lvert\nabla\theta_{\mathrm{pha}}\rvert^{2}\bigr]$ | The amplitude equation; the scale's saddle |
| $\partial_\mu(\rho_{\mathrm{num}}\partial^{\mu}\theta_{\mathrm{pha}})=0$ | The transport equation; the angle's saddle |
| $\rho_{\mathrm{num}}=r^{2}$ | The density |
| $S_{E}$ | The Euclidean bracket; four squares |
| $k_m=mc/\hbar$ | The mass parameter |

## Further Reading

- [The Klein–Gordon Path Integral in Biquaternionic Form](the-klein-gordon-path-integral-in-biquaternionic-form.html), the companion, for the integral read here: the configuration space, the Gaussian, the lattice regulator and the Wick rotation.
- [The Klein–Gordon Equation in Biquaternionic Polar Variables](the-klein-gordon-equation-in-biquaternionic-polar-variables.html), for the collapse of the word on a central field, the amplitude equation and the transport equation.
- [The Variational Principle and the Klein–Gordon Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-klein-gordon-equation-in-biquaternionic-polar-variables.html), for the parameter metric, the Madelung action and the current.
- [The Klein–Gordon Propagator and Its Green's Functions in Biquaternionic Form](the-klein-gordon-propagator-and-its-greens-functions-in-biquaternionic-form.html), for the two-point function that the Gaussian's inverse is.
- [The Scalar Field in the Centre: Why Spin 0 Escapes the Biquaternion State Module](the-scalar-field-in-the-centre-why-spin-0-escapes-the-biquaternion-state-module.html), for why the configuration space is the centre.
- [Interpretation of the Wick Rotation in the Biquaternion Universe](interpretation-of-the-wick-rotation-in-the-biquaternion-universe.html), for the sector relabelling behind the Euclidean chart.
- [The Path Integral and the Coupled Klein–Gordon Equation in Biquaternionic Polar Variables](the-path-integral-and-the-coupled-klein-gordon-equation-in-biquaternionic-polar-variables.html), for the same chart with a connection, where the measure's gauge invariance is used.
- J. Glimm and A. Jaffe, *Quantum Physics: A Functional Integral Point of View* (Springer, 1987), for the lattice definition of a scalar functional integral and the status of the continuum measure.
- L. D. Faddeev and A. A. Slavnov, *Gauge Fields: An Introduction to Quantum Theory* (Benjamin, 1980), for the change of variables in a functional integral and the determinants it produces.
