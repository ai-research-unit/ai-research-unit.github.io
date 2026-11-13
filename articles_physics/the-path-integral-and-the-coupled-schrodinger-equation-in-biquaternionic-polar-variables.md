# __The Path Integral and the Coupled Schrödinger Equation in Biquaternionic Polar Variables__

## Introduction

**The integral is the element companion's, and this article reads it in the word.** *The Path Integral and the Coupled Schrödinger Equation in Biquaternionic Form* puts the connection into the free integral, splits the exponent into four terms and shows that the measure stays flat. This article substitutes $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}e_t$ into that integral and reads where the connection lands.

**The finding is one sentence long: the connection shifts the two rates of the chart and appears nowhere else.** Writing the mechanical rates

$$
\kappa_t=\dot\theta_{\mathrm{pha}}-\frac{ϙ}{\hbar}\varphi,
\qquad
\kappa_\eta=\partial_\eta\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}A_\eta,
$$

the coupled exponent is the free exponent with $\dot\theta_{\mathrm{pha}}\to\kappa_t$ and $\vec\nabla\theta_{\mathrm{pha}}\to\vec\kappa$, and the potential $h_t$ untouched. That is the whole of the coupling in the chart, and it is the chart's form of the element companion's two shifts.

**Three consequences follow, and the first is the article's structural result.**

*First, the scalar potential enters linearly and the chart agrees with the element form exactly.* The temporal bracket of this chart is first order, so a constant $\varphi$ shifts the phase rate and produces no term in $\varphi^{2}$. The element companion's shift $h_t\mapsto h_t-ϙ\varphi$ is therefore reproduced by the chart, term for term. **The Klein–Gordon chart cannot do this** — its temporal bracket is a square, so a constant scalar potential contributes its square and no linear shift, and that is the fork its companion records. **The Schrödinger chart has no fork**, and the reason is the order in time.

*Second, the vector potential enters linearly and quadratically, and the two terms are the gauge invariance's two halves.* The linear term is what a gauge transformation turns into a total derivative; the quadratic term is what supplies the remainder. The element companion's four terms are this pair plus the free ones, and the chart makes the cancellation an identity between two displayed terms.

*Third, the measure is untouched and the invariance is exact at every step.* The transformation is a shift of the angle, the measure is flat in the density and the angle together, and no Jacobian appears. The chart's invariance is therefore a statement about the exact measure and not about a lattice.

**What the article does not do.** It does not produce a second integral, does not evaluate the coupled kernel beyond the constant background, does not decide the Landau spectrum, and does not treat a non-central connection. It reads one integral in another coordinate system and says what the coordinate system shows.

**Conventions.** The chart, the collapse on a central field, the density $n=r^{2}$ and the measure are the free polar companion's. The connection is $\tilde A_\Phi=i(\varphi/c)e_t+\vec A$, the coupling is $ϙ$, and the covariant derivative is $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{iϙ}{\hbar}\tilde A_\Phi$ with $D_t=\partial_{t'}-\frac{iϙ}{\hbar}\varphi$ and $D_\eta=\partial_\eta+\frac{iϙ}{\hbar}A_\eta$. The mechanical momentum is $\vec\pi=-i\hbar\vec\nabla+ϙ\vec A$ and the potential energy is $-ϙ\varphi$.

## The Exponent, and Where the Connection Sits

**One substitution and two identities.** Putting $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}e_t$ into the coupled action and using

$$
\mathrm{Sc}\bigl(i\hbar\,\tilde\Xi^{*}D_t\tilde\Xi\bigr)=-\hbar\,r^{2}\kappa_t,
\qquad
\mathrm{Sc}\bigl((D_\eta\tilde\Xi)^{*}(D_\eta\tilde\Xi)\bigr)=(\partial_\eta r)^{2}+r^{2}\kappa_\eta^{2},
$$

gives the chart's exponent

$$
\boxed{\;S=\int dt'\,d^{3}x\;\Bigl[-\hbar\,r^{2}\kappa_t-\frac{\hbar^{2}}{2m}\Bigl((\vec\nabla r)^{2}+r^{2}|\vec\kappa|^{2}\Bigr)-h_t\,r^{2}\Bigr],\;}
$$

in the constant setting, and the same with $V(\vec x)$ in place of $h_t$ in the operator setting. **The connection sits inside the two rates and nowhere else**: it does not multiply $r$, it does not meet $\vec\nabla r$, and it does not appear in a separate term. The two identities were checked on analytic fields at four points, the temporal one to a relative $1.4\times10^{-16}$ and the spatial one to $2.1\times10^{-16}$.

**The connection is central, so it multiplies the word and cannot act inside a factor.** That is the reason the two identities are so short: a central element passes through $e^{i\theta_{\mathrm{pha}}}$ and through $r$, so its only effect is on the derivative of the exponent, and the derivative of the exponent is the rate. The polar variational companion states the same fact and calls the result the covariant bracket.

**The rates are the chart's entire vocabulary for the connection.** There are two of them, one temporal and one spatial, and they are the mechanical phase rates: $\hbar\kappa_\mu$ is the mechanical momentum's $\mu$-th slot, up to the metric's sign. Everything the connection does in the chart is done to these two objects, and the rest of the article is their consequences.

## The Four Terms and Their Shapes

**Written out, the exponent is the free exponent plus three terms.** In the constant setting,

$$
S=\int dt'\,d^{3}x\;\Bigl[-\hbar r^{2}\dot\theta_{\mathrm{pha}}-\frac{\hbar^{2}}{2m}\bigl((\vec\nabla r)^{2}+r^{2}(\vec\nabla\theta_{\mathrm{pha}})^{2}\bigr)-h_t r^{2}
+ϙ\varphi\,r^{2}-\frac{\hbar}{m}ϙ\,r^{2}\vec A\cdot\vec\nabla\theta_{\mathrm{pha}}-\frac{ϙ^{2}}{2m}r^{2}|\vec A|^{2}\Bigr].
$$

The three interaction terms have the shapes $\varphi r^{2}$, $r^{2}\vec A\cdot\vec\nabla\theta_{\mathrm{pha}}$ and $r^{2}|\vec A|^{2}$, and no other shape appears.

**The scalar potential's term is linear in the potential and carries no derivative.** Its form is the density times the potential, which is the energy's slot and the current's time component; the element companion's potential term $ϙ\varphi\,n$ is the same object with $n=r^{2}$.

**The vector potential's terms are the momentum's translation, expanded.** The bracket's shift is $\vec\nabla\theta_{\mathrm{pha}}\to\vec\nabla\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A$, and squaring it gives exactly the linear and the quadratic term. **The two terms are one translation's expansion**, and the sign of the quadratic term is negative because the bracket enters the action with the negative sign of the kinetic energy.

**The fourth term that is absent.** No term multiplies the connection by $\vec\nabla r$. The two interaction terms contain $r^{2}$ and $\vec\nabla\theta_{\mathrm{pha}}$ and never $\vec\nabla r$, and the absence is exact: the chart has two coordinates, and the connection can only enter the one that carries the derivative of the exponent. **This is the chart's sharpest negative statement, and it is the reason the coupled Klein–Gordon pair has a fork and this pair does not.** There the equation's squared operator carries an amplitude–potential cross term that the action's modulus form does not, so the chart can write one reading and not the other; here the element exponent is itself the modulus form, the chart writes it exactly, and there is no second reading to be unable to write.

## The Scalar Potential Enters Linearly

**A constant scalar potential shifts the phase rate and produces no square.** With $\varphi$ constant,

$$
\hbar\kappa_t=\hbar\dot\theta_{\mathrm{pha}}-ϙ\varphi=-h_t,
\qquad\text{that is}\qquad
\dot\theta_{\mathrm{pha}}=\frac{ϙ\varphi-h_t}{\hbar},
$$

which is the element companion's $h_t\mapsto h_t-ϙ\varphi$ read as a rate. The chart has no term in $\varphi^{2}$ because the temporal bracket is first order: a bracket that is linear in the rate cannot produce a square of the shift.

**The agreement is exact and it is the article's structural result.** The element form's shift is linear, the chart's is linear, and the two agree at every value of the coupling. In the Klein–Gordon pair the same comparison fails: the chart's temporal bracket is a square with the metric's relative sign, so a constant scalar potential contributes $+\frac{ϛ^{2}}{\hbar^{2}}a_t'^{2}r^{2}$ and no linear shift, while the element form's shift is linear. **That is the fork, and the fork is the second-order temporal bracket.** The Schrödinger chart's bracket is not a square, so the fork's mechanism is absent, and the Schrödinger pair is free of the question.

**The reason is one line and it is worth stating twice.** In the Klein–Gordon chart the exponent is a sum of squares, one per slot, and the temporal square is where a scalar potential lands; in the Schrödinger chart the exponent is linear in the temporal rate, so it is the rate that receives the shift. The order in time decides the shape of the interaction term, and it decides it before the algebra says anything.

**The element companion's dispersion is therefore the chart's dispersion.** $E+ϙ\varphi=(\vec p+ϙ\vec A)^{2}/2m$ is $\hbar\kappa_t=-h_t$ with the momentum's translation, and both statements are the same two rates.

## The Vector Potential Is a Translation

**A constant $\vec A$ translates the phase's gradient, and the translation changes the bracket by its square.** This is the same operation as the scalar potential's shift, read in the spatial slots, and the difference between the two is the sign the bracket carries: the temporal rate enters the exponent multiplied by $-\hbar n$ and the spatial one by $-\frac{\hbar^{2}}{2m}n$.

**The linear term is a total derivative under a gauge transformation and the quadratic term is the remainder.** Writing $\theta_{\mathrm{pha}}\to\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\Lambda$ and $\vec A\to\vec A+\vec\nabla\Lambda$, the linear term changes by $-\frac{\hbar}{m}ϙ\,r^{2}\vec A\cdot\vec\nabla\Lambda$ plus a term in $\vec\nabla\Lambda\cdot\vec\nabla\theta_{\mathrm{pha}}$, and the sum of the changes is a total derivative once the continuity of the density is used. The quadratic term's change supplies the piece that makes the total derivative exact, which is the same cancellation the element companion records between the kinetic and the potential terms.

**The chart's invariance is exact and needs no link.** The transformation shifts one of the two chart coordinates by a function of the point, the measure is $dn\,d\theta_{\mathrm{pha}}$ up to a constant, and a shift of a coordinate has unit Jacobian. **The invariance therefore holds at any step size and for a finite transformation**, and there is no linearised link to fail and no exponential link to succeed: those are the Klein–Gordon companion's questions, and they arise there because its field has two independent slots whose covariance is a statement about each.

**The density is the response and the current is the phase's gradient.** The exponent's derivative with respect to $\varphi$ is $\frac{i}{\hbar}ϙ r^{2}$, so the density is the response to the scalar potential; the current is $\vec j=n\vec\pi/m$ with $\vec\pi=\hbar\vec\nabla\theta_{\mathrm{pha}}+ϙ\vec A$, which is the coupled element companion's current and is gauge invariant because both of its factors are.

**The two interaction terms are also the reason the continuity equation survives the coupling.** The continuity equation is the saddle of the angle's integral, and the angle's integral only sees the two rates; since both rates are gauge invariant combinations, the continuity equation the chart produces is gauge invariant without a separate argument.

## The Kernel in a Constant Background

**The element kernel's two factors are exactly the two shifts of the chart's rates.** For constant $\varphi$ and $\vec A$ the element companion's kernel is the free kernel times $\exp(-iϙ\varphi r'_t/\hbar c)$ and $\exp(iϙ\vec A\cdot\vec r/\hbar)$, and the chart reads them as

$$
r_K=|K_0|,
\qquad
\theta_{\mathrm{pha},K}=\arg K_0-\frac{ϙ\varphi\,r'_t}{\hbar c}+\frac{ϙ}{\hbar}\vec A\cdot\vec r,
\qquad
\tilde U_{\Psi,\mathrm b,K}=e_t,
\qquad
\tilde u_{\mathrm r,K}=\pm e_t .
$$

**The potential's factor is the phase rate's shift and the vector potential's factor is the gradient's shift.** The first is $\kappa_t$'s constant part, $\kappa_t=\dot\theta_{\mathrm{pha}}-\frac{ϙ}{\hbar}\varphi$, integrated over the time; the second is $\vec\kappa$'s constant part, $\vec\kappa=\vec\nabla\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A$, integrated over the displacement. **One kernel, two rates, two factors**, and nothing else in the word changes: the scale is the free scale and the boost and rotor are the free ones.

**The scale is untouched by a constant connection.** The potential's factor has modulus one, the vector potential's factor has modulus one, and the free kernel's modulus is the free modulus. **The constant background changes the kernel's angle and not its scale**, which is the chart's version of the element companion's statement that a constant connection is a shift and not a deformation.

**The composition of the word is the composition of the two factors.** The angle's two extra pieces add, the scale multiplies as the Fresnel integral requires, and the composition was verified in the element form to $2.3\times10^{-12}$. **The chart adds the reading and not the number**: the number is the element companion's, and the reading is that the coupling's two factors are the two rates' constants.

**The line integral is the chart's non-constant case.** For a connection that varies along the path, the vector potential's factor becomes $\exp(iϙ\int\vec A\cdot d\vec r/\hbar)$ and the potential's becomes $\exp(-iϙ\int\varphi\,dt'/\hbar c)$, the two being the temporal and spatial halves of one line integral of $\tilde A_\Phi$ along the classical path. **The chart states it as the shift of the two rates accumulated along the path**, which is the geometric phase of the corpus's Berry-phase article and is the coupling's only semiclassical content.

## What the Polar Reading Adds and Does Not Add

**Adds, first, the linearity of the scalar potential with its reason.** The chart's temporal bracket is first order, so the scalar potential's shift is linear and the chart agrees with the element form exactly. This is the sharpest difference between this pair and the Klein–Gordon pair, and it is a statement about the order in time rather than about the algebra.

**Adds, second, the absence of the amplitude–potential cross term as a structural fact.** The chart's exponent has no term in $\vec\nabla r$ times the connection, because the connection can only shift the exponent's derivative. The coupled Klein–Gordon pair's fork is therefore absent here, and its absence is not an approximation: the element exponent is the modulus form, so the chart writes it exactly.

**Adds, third, the two kernel factors as the two rates' constants.** The constant background's kernel is one scale and one angle, and the angle's two extra pieces are the two shifts integrated along the time and the displacement.

**Does not add a value.** The kernel is the element companion's, the dispersion is the element companion's, and the determinant is not evaluated.

**Does not decide anything about a non-central connection.** The chart's short identities use the connection's centrality twice: to pass through $e^{i\theta_{\mathrm{pha}}}$ and to leave $r$ alone. A connection in $\mathbb{B}_{\Psi}$ would break both, and the chart would need a third coordinate.

## Open Questions

**1. What is the chart's version of the Landau kernel?** The element kernel in a constant magnetic field is a sum over Landau levels. Its word would have a scale from the level sum, an angle from the level phases, and a rotor only if the field's internal frame were nontrivial. Whether the word is degenerate is not known.

**2. Is the linearity of $\varphi$ an invariant statement?** The chart shows that the scalar potential's shift is linear because the temporal bracket is first order. Whether a chart of a higher-order theory can be written with a linear slot — by a Legendre transform or by introducing a second field — is open, and it is the same question as the Klein–Gordon fork, asked from the other side.

**3. Does the chart's invariance survive a non-abelian connection?** A connection valued in the algebra rather than in its centre would not pass through the phase, and the chart's two identities would fail at their first step. The gauge-sector articles of the corpus are where that connection's algebra is discussed.

**4. What does the chart say at a caustic in a field?** The free scale vanishes or diverges at the free caustics; a constant background does not move them, because it does not touch the scale. Whether a varying field moves them is a question about the classical trajectories and not about the chart.

**5. Empirical content.** None.

## Summary

The coupled integral in the chart is the free integral with the two phase rates replaced by the mechanical ones, $\kappa_t=\dot\theta_{\mathrm{pha}}-\frac{ϙ}{\hbar}\varphi$ and $\vec\kappa=\vec\nabla\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A$, and with the potential untouched. The exponent is $-\hbar r^{2}\kappa_t-\frac{\hbar^{2}}{2m}((\vec\nabla r)^{2}+r^{2}|\vec\kappa|^{2})-h_t r^{2}$, verified as an identity against the element form to a relative $10^{-16}$ in both halves, and its three interaction terms have the shapes $\varphi r^{2}$, $r^{2}\vec A\cdot\vec\nabla\theta_{\mathrm{pha}}$ and $r^{2}|\vec A|^{2}$ and no other.

The scalar potential enters linearly, so the chart's dispersion is the element companion's shift $h_t\mapsto h_t-ϙ\varphi$ exactly; the Klein–Gordon chart's temporal bracket is a square, which is why that pair has a fork and this one does not. The vector potential enters as a translation of the phase's gradient, its linear term is the total derivative and its quadratic term the remainder of the gauge invariance, and the invariance itself is exact at every step because the measure is flat in the density and the angle and the transformation shifts one of them.

The kernel in a constant background has the free scale and an angle that carries the two shifts: $-\frac{ϙ\varphi r'_t}{\hbar c}$ from the temporal rate and $\frac{ϙ}{\hbar}\vec A\cdot\vec r$ from the spatial one, with the composition verified to $2.3\times10^{-12}$ in the element form. There is no amplitude–potential cross term in the chart, and its absence is exact.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\kappa_t=\dot\theta_{\mathrm{pha}}-\frac{ϙ}{\hbar}\varphi$ | Mechanical temporal rate |
| $\vec\kappa=\vec\nabla\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\vec A$ | Mechanical spatial rate |
| $-\hbar r^{2}\kappa_t-\frac{\hbar^{2}}{2m}((\vec\nabla r)^{2}+r^{2}|\vec\kappa|^{2})$ | The chart's exponent |
| $\varphi r^{2}$ | The scalar potential's term; linear |
| $r^{2}\vec A\cdot\vec\nabla\theta_{\mathrm{pha}}$ | The vector potential's linear term |
| $r^{2}|\vec A|^{2}$ | The vector potential's quadratic term |
| $\theta_{\mathrm{pha}}\to\theta_{\mathrm{pha}}+\frac{ϙ}{\hbar}\Lambda$ | The gauge transformation in the chart |
| $\vec j=n\vec\pi/m$ | The current; gauge invariant |
| $\theta_{\mathrm{pha},K}=\arg K_0-\frac{ϙ\varphi r'_t}{\hbar c}+\frac{ϙ}{\hbar}\vec A\cdot\vec r$ | The kernel's angle in a constant background |

## Further Reading

- *The Path Integral and the Coupled Schrödinger Equation in Biquaternionic Form*, for the integral read here and for the element form's four terms.
- *The Coupled Schrödinger Equation in Biquaternionic Polar Variables*, for the covariant logarithmic derivative and the shifted potential.
- *The Variational Principle and the Coupled Schrödinger Equation in Biquaternionic Polar Variables*, for the polar Lagrangian with the covariant bracket.
- *The Path Integral and the Schrödinger Equation in Biquaternionic Polar Variables*, for the free chart, its measure and its constraints.
- *The Path Integral and the Coupled Klein–Gordon Equation in Biquaternionic Polar Variables*, for the second-order chart and the fork this one does not have.
- *The Berry Phase and Geometric Phases in Biquaternionic Form*, for the line-integral phase in its geometric reading.
- *Landau Levels in Biquaternionic Form*, for the constant magnetic field's spectrum.
- E. Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1927) 322–326, for the density–phase pair.
- M. P. A. Fisher and W. Zwerger, "Quantum Brownian Motion in a Periodic Potential," *Physical Review B* **32** (1985) 6190, for the minimal-coupling form of a first-order action.
- H. Kleinert, *Path Integrals in Quantum Mechanics, Statistics, Polymer Physics, and Financial Markets* (World Scientific, 2009), for the constant-background kernels and the gauge-invariant measure.
- L. D. Faddeev and A. A. Slavnov, *Gauge Fields: An Introduction to Quantum Theory* (Benjamin, 1980), for the first-order integral's gauge structure.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the polar form of a Clifford element and its central multipliers.
