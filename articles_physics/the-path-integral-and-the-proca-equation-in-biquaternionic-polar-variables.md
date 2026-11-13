# __The Path Integral and the Proca Equation in Biquaternionic Polar Variables__

## Introduction

**The integral is the element companion's, and this article reads it in the word.** *The Path Integral and the Proca Equation in Biquaternionic Form* defines the functional integral over the anti-Hermitian configurations, splits its operator, and computes its determinant. This article substitutes the polar word of the material sector into that integral and asks where each object lands.

**The substitution is the polar equation article's, and it is not the scalar substitution.** The carrier is four-dimensional, so the eight-parameter word of $\mathbb{B}$ cannot be a bijection onto it. What survives is a two-branch word with four parameters on each branch: a scale, a rapidity, and two angles for the axis. **The central angle is absent, because a real four-vector has no phase to carry one.** That absence is the whole of this article, and its consequences run further than they look.

**Four findings, and the first is the reason the article exists.**

*First, the weight has no chart coordinate.* The weight $\exp(iS/\hbar)e_t$ is central and $*$-unitary; the chart's coordinates are those of an anti-Hermitian element. **The chart is a chart of the carrier, and the weight does not live in the carrier.** So the sentence the scalar chart can say — every path has scale one — has no Proca analogue, and the Maslov phase, which lives in the centre, is invisible to this chart.

*Second, the measure does not cancel and it does not have to.* The chart's volume element is $r^{3}\sinh^{2}u\,\mathrm{d}r\,\mathrm{d}u\,\mathrm{d}\Omega$ on the timelike branch and $r^{3}\cosh^{2}u\,\mathrm{d}r\,\mathrm{d}u\,\mathrm{d}\Omega$ on the spacelike one, and the mass term supplies $r^{2}$ on both. The radial integral is then $\int_0^\infty r^{3}\mathrm{d}r\,e^{-ar^{2}}=\frac{1}{2a^{2}}$, which is the power a four-component Gaussian carries. **The radial power is one less than the carrier's dimension, and the mass term completes the count.**

*Third, the constraint is displayed and not imposed.* The action's divergence term $-\frac12S^{2}$ is one of the chart's three pieces, and its variation produces the Lorenz condition. In the integral the divergences are therefore integrated over as Gaussian directions whose saddle is the condition. **The constraint is a saddle, and not a multiplier.** That is the sharp difference from the scalar chart, where the phase was a multiplier and the density's integral was a delta.

*Fourth, the kernel is outside the chart.* The two-point function of the Proca field is a bivector-valued distribution; a bivector is not an element of the material sector. **The chart reads the classical field and the kernel's action on a fixed direction, and it cannot read the kernel itself**, because the carrier has four dimensions and the kernel has sixteen.

**What the article does not do.** It does not produce a second integral, does not change a value, and does not evaluate anything the element companion has not evaluated. It reads, and it says where the reading stops.

**Conventions.** The algebra and the pairing are the element companion's. The word is

$$
\tilde A_\Phi=\varepsilon\,i\,r\,\tilde U_{\Psi,\mathrm b}\ \ (\langle\tilde A_\Phi\rangle_\natural<0),
\qquad
\tilde A_\Phi=r\,\tilde U_{\Psi,\mathrm b}\,\hat u\ \ (\langle\tilde A_\Phi\rangle_\natural>0),
$$

with $r>0$, $\varepsilon=\pm1$, $\tilde U_{\Psi,\mathrm b}=\cosh u+i\sinh u\,\hat u_{\mathrm b}$ the boost of rapidity $2u$ about the unit axis $\hat u_{\mathrm b}$, and $\hat u$ a real unit vector. The parameters are $(r,u,\vartheta_1,\vartheta_2)$ on each branch: four for four components. **The chart's statements and its two branches are the polar equation article's**, and this article cites them rather than deriving them.

## The Word of a Value

**The chart is a bijection and its two branches are the two signs of the Minkowski form.** The norm of the timelike branch is $-r^{2}$:

$$
(\varepsilon ir\tilde U_{\Psi,\mathrm b})(\varepsilon ir\tilde U_{\Psi,\mathrm b})^{\natural}=\varepsilon^{2}i^{2}r^{2}\tilde U_{\Psi,\mathrm b}\tilde U_{\Psi,\mathrm b}^{\natural}=-r^{2},
$$

because the boost is a $\natural$-unit. The norm of the spacelike branch is $+r^{2}$, for the same reason with $\hat u\hat u^{\natural}=+1$. Both computations were checked on random values: the timelike branch gave $-0.810000000000$ for $r=0.9$, the spacelike branch $+0.810000000000$, and the anti-Hermiticity $\tilde A_\Phi^{*}+\tilde A_\Phi=0$ held exactly rather than to a tolerance.

**The lightlike set is outside both branches and it is of measure zero.** Where $\langle\tilde A_\Phi\rangle_\natural=0$ the field is a zero divisor of $\mathbb{B}$ and has no polar reading at all. The set is a cone in four dimensions, so its four-volume is zero and the chart misses nothing that the integral can see. **This is the material sector's version of the scalar chart's nodal set**, and the mechanism is the same: the excluded set is where the chart's coordinates fail, and it carries no weight.

**The branch is a label and not a coordinate.** $\varepsilon$ is not varied, it is summed: the two signs of the scalar potential are two pieces of the timelike region, and the region is covered once by the pair. The count of parameters is four on each branch, which is the count of components, and no condition is lost or added. **The chart is exact, and that is why the polar reading is a reading and not an approximation.**

## The Weight Has No Chart Coordinate

**The weight of one configuration is central, and the chart's coordinates are anti-Hermitian.** For a configuration of the field the weight is

$$
e^{\frac{i}{\hbar}S[\tilde A_\Phi]}\,e_t ,
$$

a central $*$-unitary element: scale one, angle $S/\hbar$, trivial boost, trivial rotor. The chart's coordinates describe an element of $\mathbb{B}_\Phi$, whose scalar part is a coefficient of $ie_t$ and whose vector part is real. **A central element is neither anti-Hermitian nor Hermitian-traceless; it is outside the material sector entirely.**

**So the chart cannot read the weight, and the scalar chart's first sentence does not survive.** There the weight and the field value lived in the same chart, so "every configuration has scale one" was a statement inside the chart. Here the weight has a scale and an angle and the chart has neither: the chart's $r$ is the magnitude of the *field value*, and the weight's modulus is one by construction. **The two scales are different objects and the chart names only one of them.**

**The consequence is that the Maslov phase is invisible.** In the scalar pair the kernel's angle was the classical action over $\hbar$ plus a central constant, and the constant was the argument of the Fresnel square root — a central object, read in the central angle's slot. Here there is no central angle's slot. **The Maslov phase of the Proca kernel exists, is central, and has no chart coordinate**; the chart's only discrete data are the branch sign $\varepsilon$ and the two halves of each branch.

**What the chart does say about a configuration is what the configuration is, and that is enough.** The scale, the rapidity and the axis are the field's own data, and every quantity built from the field value alone is readable. The weight is not such a quantity, and the article does not pretend otherwise — this is the one place in the corpus's path-integral set where the chart and the weight are in different sectors, and it should be said plainly rather than smoothed over.

## The Measure

**The chart's volume element is $r^{3}$ times an angular factor, and the angular factor differs by branch.** Inverting the two charts gives

$$
\mathrm{d}^{4}A=r^{3}\sinh^{2}u\,\mathrm{d}r\,\mathrm{d}u\,\mathrm{d}\Omega_{2}\ \ (\text{timelike}),
\qquad
\mathrm{d}^{4}A=r^{3}\cosh^{2}u\,\mathrm{d}r\,\mathrm{d}u\,\mathrm{d}\Omega_{2}\ \ (\text{spacelike}),
$$

with $\mathrm{d}\Omega_2$ the measure on the axis's sphere and $\mathrm{d}^{4}A=\mathrm{d}a'_t\,\mathrm{d}A_x\,\mathrm{d}A_y\,\mathrm{d}A_z$.

**The $r^{3}$ was checked pointwise and the checks are exact.** The $4\times4$ Jacobian of the timelike chart at three random parameter points matched $r^{3}\sinh^{2}u\,\sin\vartheta$ to a relative $5.6\times10^{-10}$, the residual being the finite difference's step. **Three powers of $r$ against four components: the radial power is the carrier's dimension less one**, because the scale is a radial coordinate and the other three parameters are angles.

**The four pieces sum to the Cartesian integral, and the sum was checked twice.** In two dimensions, where the chart is the hyperbolic analogue of polar coordinates and the axis is a point, the four pieces — timelike with $\varepsilon=\pm1$, spacelike with $\hat u=\pm\vec e_z$ — reproduce $\pi=\int\!\!\int e^{-(a^{2}+b^{2})}\mathrm{d}a\,\mathrm{d}b$ to a relative $7.5\times10^{-11}$. In four dimensions the two branches reproduce $\pi^{2}/a^{2}=\int\mathrm{d}^{4}A\,e^{-a(a_t'^{2}+\vec A^{2})}$ to $1.6\times10^{-9}$, with the timelike part contributing $1.061070739$ and the spacelike part $4.778931874$ of the total $5.840002613$.

**The measure does not cancel against the exponent, and the reason is the order in time.** The mass term is $\mp\frac12k_m^{2}r^{2}$ on the two branches, so it is a function of $r^{2}$ alone, and the radial integral is

$$
\int_0^{\infty}r^{3}\mathrm{d}r\,e^{\mp\frac{i}{2\hbar}k_m^{2}r^{2}}\ \propto\ \frac{1}{(k_m^{2})^{2}} ,
$$

which is the $a^{-2}$ a four-component Gaussian carries. **The Jacobian's three powers and the exponent's one power of $r^{2}$ together give exactly the four components' worth of Gaussian weight.** In the scalar chart the opposite happened: the exponent was linear in $n=r^{2}$, the Jacobian $r\,\mathrm{d}r=\frac12\mathrm{d}n$ cancelled it exactly, and the measure left no trace. **A linear exponent cancels the Jacobian; a quadratic one is completed by it.**

**The rapidity's integral is not convergent on the mass term alone, and the kinetic term is what converges it.** The mass term is flat in $u$, so $\int\mathrm{d}u\,\sinh^{2}u$ diverges; the kinetic term's dependence on $u$ is the frame's Maurer–Cartan form, and it is what supplies the falloff. **The chart's two coordinates are not on the same footing: $r$ is weighted by the mass and $u$ by the field strength**, which is the integral's version of the polar variational companion's statement that the mass fixes the scale's equation and the frame fixes the transport equation.

## The Exponent in the Chart

**The exponent's three pieces are the full square, the divergence's square, and the mass.** In the chart the action is

$$
S=\int d^{4}r\;\Bigl[\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\Bigl[\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr)^{2}\Bigr]-\tfrac12S^{2}-\tfrac12k_m^{2}\langle\tilde A_\Phi\rangle_\natural\Bigr],
\qquad S=\mathrm{Sc}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr),
$$

and each piece has a chart reading. The first is a quadratic form in the four gradients with a metric the frame builds; the second is a square of a scalar; the third is $\mp\frac12k_m^{2}r^{2}$.

**The mass term's sign is the branch's and its magnitude is the scale's.** On the timelike branch the scale enters with the sign of a positive mass term and the scale equation has the massive form; on the spacelike branch the sign is reversed. **Nothing in the element form displays this, because the element form's mass term is indefinite and the branch is not a thing the element form can name.**

**The first piece is where the frame's rapidity enters.** The quadratic form's coefficients are built from $\tilde U_{\Psi,\mathrm b}$ and its derivatives, so the exponent depends on $u$ through the Maurer–Cartan form $\Gamma_\mu=\tilde U_{\Psi,\mathrm b}^{-1}\partial_\mu\tilde U_{\Psi,\mathrm b}$ and through nothing else. **The chart separates the scale's dependence, which is polynomial and explicit, from the frame's, which is geometric**, and that separation is the reason the two saddles below are two different equations and not one.

## The Two Saddles Are the Companion's Pair

**Stationarity in the scale gives the scale equation.** Varying $r$ in the chart's exponent gives

$$
\bigl(\Box_\Phi-k_m^{2}\bigr)r+r\sum_\mu\mathrm{Sc}\bigl(\Gamma_\mu^{2}\bigr)=0 ,
$$

which is the polar equation article's first equation, with the branch's sign absorbed in the mass term's sign. It is a Klein–Gordon equation for the scale with a source built from the frame's Maurer–Cartan form.

**Stationarity in the frame gives the transport equation.**

$$
\sum_\mu\Bigl(\frac{\partial\Gamma_\mu}{\partial R_\mu}+\Gamma_\mu^{2}-\mathrm{Sc}(\Gamma_\mu^{2})\Bigr)+2\sum_\mu\frac{\partial\ln r}{\partial R_\mu}\Gamma_\mu=0 ,
$$

which is the companion's second equation, in the traceless part.

**The pair is one statement and not two, and the integral exhibits it as two nested integrals.** Either order may be taken: the scale's integral at fixed frame is Gaussian in $r$, and the frame's integral at fixed scale is a theory of the rapidity with the scale as its weight. **The chart's reading is that the amplitude equation is the scale's saddle and the transport equation is the frame's saddle**, exactly as in the scalar chart, where the amplitude was the scale's saddle and the transport the angle's.

**What is missing from the pair is what the missing coordinate would have carried.** The scalar chart's pair had a continuity equation as the angle's saddle, and the continuity equation came from the phase's being a multiplier. Here there is no phase and no continuity equation: the companion says so, and calls the result a magnitude–direction decomposition rather than a fluid. **The chart's pair is a scale equation and a frame equation, and the current that a fluid reading would need does not exist**, because a real four-vector has no phase to make one.

## The Lorenz Term Is Displayed

**The divergence's square is a term in the exponent and its saddle is the Lorenz condition.** The second piece is $-\frac12\int S^{2}$, quadratic in $S$ and with no derivative of $S$ outside the divergence. Integrating over the configurations that change $S$ at fixed $\tilde F$ is a Gaussian whose saddle is $S=0$, and $S=0$ is $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)=0$. **The Lorenz condition is therefore the saddle of one of the chart's three pieces, and this is the integral's form of the polar variational companion's statement that the middle piece is what the projection removes and what its variation produces.**

**The mechanism is not the scalar chart's, and the difference is worth stating.** In the scalar chart the phase entered linearly in $\dot n$, so integrating the density gave an exact delta on the phase's rate: a constraint, exact, in the constant setting. Here the divergence enters quadratically, so integrating gives a Gaussian and a saddle: a condition, exact at the saddle, and not a delta. **A linear entry makes a constraint; a quadratic entry makes an equation.**

**The element form has neither, because it has only the equation.** There the divergence of the field equation forces $S=0$ and the forcing is one line. The chart displays the term whose variation does the forcing, and the integral displays the integration that produces the saddle. **Three descriptions, one identity**, and the chart's contribution is to show that the term is a square — a thing the element form's $\mathrm{Re}\,\mathrm{Sc}(\tilde F\tilde F)$ hides by construction.

## What the Chart Can and Cannot Read

**The classical field is readable, and it is the saddle.** The saddle of the sourced integral is $\tilde A_\Phi^{\mathrm{cl}}=-P^{-1}\tilde J_\Phi$, which lies in $\mathbb{B}_\Phi$ because $P$ maps the sector into itself. Its chart is a scale, a rapidity and an axis, the branch is decided by the sign of $\langle\tilde A_\Phi^{\mathrm{cl}}\rangle_\natural$, and **every statement the polar equation article makes about a solution applies to it.**

**The kernel is not readable, and the count is the reason.** The two-point function $\langle\tilde A_\Phi(x)\tilde A_\Phi(y)\rangle=i\hbar P^{-1}(x-y)$ is a bivector-valued distribution: sixteen real components at each pair of points, symmetric in the pair. A bivector is not a four-vector, so the two-branch word has nothing to act on. **The chart's carrier is four; the kernel's carrier is sixteen; the chart cannot be applied to an object that is not in its carrier.**

**What can be read is the kernel's action on a fixed direction.** For a fixed real unit $\hat e$ the object $P^{-1}\hat e$ is a material-sector element at each point, and the chart reads it. **So the chart reads a column of the propagator and not the propagator**, and the column is enough for the statements about a source that points one way — the transverse and longitudinal responses, the $1/k_m^{2}$ term and its divergence — but not for a statement about the kernel's own structure.

**The propagator's split has a chart reading through the column, and it is the branch's.** A transverse source's response is a spacelike-dominated value and a longitudinal source's is not, so the two projector images fall on the two sides of the lightlike cone in the leading case. **The chart therefore displays the three–one split as a split between the branches**, not as a split of a bivector; the count is the same three plus one, and the presentation is the carrier's.

## What Composes and What Does Not

**The product of two field values leaves the sector, so the word cannot be multiplied at all.** The material sector is not closed: $\vec e_x\vec e_x=-e_t$ is central and real, and the product of two anti-Hermitian elements is Hermitian. So $\tilde A_\Phi\tilde A_\Phi'$ is not a field value, and the question "does the word of a product equal the product of the words" does not arise. **The scalar pair's non-composition statement is replaced here by a closure failure**, and the closure failure is the stronger statement.

**The kernel composes, and its composition is outside the chart.** The composition of two propagators is a composition of bivectors: a matrix product in the four-valued indices and a convolution in the position. **It is well defined and the chart does not see it**, for the reason of the previous section. So the composition question has an answer and the answer lives outside the reading.

**The chart's own composition law is the one that fails first.** A scale and a rapidity can be composed as a product of values only if the product stays in the carrier, and it does not. **The scale of a product of two field values is not a scale of any field value**, and this is the chart's version of the closure statement — stated about the chart's coordinates rather than about the algebra.

**What survives is the classical field's own composition, and there is none.** A classical field is a function, and functions do not compose. The composition that matters is the kernel's, and the kernel is a bivector. **So this pair has no composition law to offer, neither inside the chart nor outside it**, and the contrast with the scalar pair is the contrast between a carrier that closes and one that does not.

## What the Polar Reading Adds and Does Not Add

**Adds, first, the statement that the weight has no chart coordinate.** The chart is a chart of the carrier and the weight is not in the carrier, so the scalar chart's "every path has scale one" and its Maslov bookkeeping have no counterpart. **This is the sharpest difference between this pair and the two scalar pairs**, and it is a difference of sectors rather than of formulas.

**Adds, second, the measure's radial power with its reason.** $r^{3}$ on four components, $r^{7}$ on eight — the radial power is the carrier's dimension less one — and the mass term's $r^{2}$ completes the Gaussian. The scalar chart's cancellation is the special case of a linear exponent; here the exponent is quadratic and the Jacobian is not cancelled but completed.

**Adds, third, the Lorenz term as a displayed square whose saddle is the condition.** The constraint's mechanism differs from the scalar chart's delta, and the difference is the order in the divergence: quadratic rather than linear.

**Adds, fourth, the negative statement about the kernel.** The chart reads a column and not the propagator, and the count four against sixteen is the reason. **A negative statement of this kind is worth as much as a positive one**, because it tells the next article where the reading must stop.

**Does not add a value.** Every closed form quoted is the element companion's; the determinant, the propagator and the saddle are its objects, and the chart locates them.

**Does not decide the statistics, the measure's continuum limit or the ghost's phase.** The field is commuting and bosonic; the product over sites is formal; the ghost is a central constant that the chart, being a chart of the carrier, cannot see at all.

## Open Questions

**1. Can a chart of the bivector be built?** The kernel's carrier is $\mathbb{B}\otimes\mathbb{B}$ symmetric, and a polar decomposition of that object would be the analogue of the word for a propagator. Whether such a decomposition exists and whether it carries the three–one split is open, and it is the natural next question of this pair.

**2. Is the branch a physical distinction?** The metric's sign decides the branch and the branch decides the mass term's sign. Whether a spacelike classical field is physically admissible, and whether the integral's spacelike piece contributes anything beyond the Fresnel factor, is not settled here — the degenerate-solutions article takes up the adjacent question.

**3. What is the chart's version of the ghost?** The ghost is a property of a momentum mode and the chart is a property of a field value. The chart's nearest object is the branch sign, and the two are not the same. Whether a momentum-space chart would display the ghost as a coordinate is open.

**4. Does the rapidity's divergence have a meaning?** The mass term is flat in $u$ and the kinetic term is not, so the rapidity's integral is convergent only because of the field strength. Whether the flat direction is the massless limit's gauge direction seen from the chart is a question this article does not answer.

**5. Empirical content.** None.

## Summary

The polar reading of the Proca functional integral is the substitution of the two-branch word into the element companion's integral, and its content is four statements about where the chart stops. The weight is central and the chart is anti-Hermitian, so **the weight has no chart coordinate**: the scale-one sentence and the Maslov phase belong to the scalar pair and not to this one.

The measure is $r^{3}\sinh^{2}u\,\mathrm{d}r\,\mathrm{d}u\,\mathrm{d}\Omega$ on the timelike branch and $r^{3}\cosh^{2}u\,\mathrm{d}r\,\mathrm{d}u\,\mathrm{d}\Omega$ on the spacelike one, checked pointwise to $5.6\times10^{-10}$ and summed to the Cartesian integral to $7.5\times10^{-11}$ in two dimensions and $1.6\times10^{-9}$ in four. The radial power is the carrier's dimension less one, and the mass term's $\mp\frac12k_m^{2}r^{2}$ completes the Gaussian: $r^{3}$ and $r^{2}$ give $a^{-2}$, which is four components' worth. The scalar chart's cancellation is the linear-exponent special case.

The divergence's square is a displayed term of the exponent and its saddle is the Lorenz condition, so the constraint is an equation and not a delta. The two saddles are the companion's scale equation and transport equation. The classical field is readable; **the kernel is not, because it is a bivector and the carrier is a four-vector**; and the product of two field values leaves the sector, so the chart has no composition law to offer.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $r$ | Scale of the field value; the modulus of the Minkowski square |
| $u$ | Half the boost's rapidity; $\tilde U_{\Psi,\mathrm b}=\cosh u+i\sinh u\,\hat u_{\mathrm b}$ |
| $\varepsilon=\pm1$ | Sign of the scalar potential; a label, not a coordinate |
| $\hat u$ | Axis of the boost, or the direction of $\vec A$ on the spacelike branch |
| $\langle\tilde A_\Phi\rangle_\natural=-r^{2}$ | Timelike branch |
| $\langle\tilde A_\Phi\rangle_\natural=+r^{2}$ | Spacelike branch |
| $\mp\frac12k_m^{2}r^{2}$ | The mass term; the sign is the branch's |
| $r^{3}\sinh^{2}u\,\mathrm{d}r\,\mathrm{d}u\,\mathrm{d}\Omega_{2}$ | Timelike volume element |
| $r^{3}\cosh^{2}u\,\mathrm{d}r\,\mathrm{d}u\,\mathrm{d}\Omega_{2}$ | Spacelike volume element |
| $\int_0^\infty r^{3}\mathrm{d}r\,e^{-ar^{2}}=\frac{1}{2a^{2}}$ | The radial integral; four components' worth |
| $-\frac12S^{2}$, $S=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)$ | The displayed Lorenz term; its saddle is $S=0$ |
| $\Gamma_\mu=\tilde U_{\Psi,\mathrm b}^{-1}\partial_\mu\tilde U_{\Psi,\mathrm b}$ | The frame's Maurer–Cartan form |
| $\langle\tilde A_\Phi(x)\tilde A_\Phi(y)\rangle=i\hbar P^{-1}$ | The kernel; a bivector, outside the chart |

## Further Reading

- *The Path Integral and the Proca Equation in Biquaternionic Form*, for the integral read here.
- *The Proca Equation in Biquaternionic Polar Variables*, for the two-branch word, the logarithmic derivative and the pair of equations.
- *The Variational Principle and the Proca Equation in Biquaternionic Polar Variables*, for the chart's action, the displayed divergence term and the four vanishing momenta.
- *The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector*, for the carrier and its complex structure.
- *Degenerate Solutions of the Biquaternionic Proca Equation*, for the lightlike set that lies outside both branches.
- *The Path Integral and the Klein–Gordon Equation in Biquaternionic Polar Variables*, for the scalar chart, whose measure cancellation is the linear case.
- *The Path Integral and the Dirac Equation in Biquaternionic Polar Variables*, for a chart whose kernel is readable because its carrier closes.
- K. Schwarzschild, "Über das Gravitationsfeld eines Massenpunktes," *Sitzungsberichte der Königlich Preussischen Akademie der Wissenschaften* (1916) 189, for the hyperbolic polar coordinates of a four-dimensional space.
- R. P. Feynman and A. R. Hibbs, *Quantum Mechanics and Path Integrals* (McGraw-Hill, 1965), for the radial Jacobian and the Fresnel factor.
- H. Kleinert, *Path Integrals in Quantum Mechanics, Statistics, Polymer Physics, and Financial Markets* (World Scientific, 2009), for the change of variables in a Minkowski-signature Gaussian.
- V. P. Maslov and M. V. Fedoriuk, *Semi-Classical Approximation in Quantum Mechanics* (Reidel, 1981), for the phase constant that this chart has no slot for.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the polar decomposition of a four-vector and its hyperbolic coordinates.
