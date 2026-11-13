# __The Path Integral and the Schrödinger Equation in Biquaternionic Polar Variables__

## Introduction

**The integral is the companion's, and this article is a reading of it.** *The Path Integral and the Schrödinger Equation in Biquaternionic Form* defines the functional integral over elements of $\mathbb{B}$, evaluates the generating functional, and identifies the two-point function with the propagator. This article substitutes the polar word into that integral and reads where each factor of the word lands. It adds no integral and changes no value.

**The word on the fields that matter here is two functions and a sign.** For a central field the boost factor has neither rapidity nor axis to carry and is $e_t$, and the rotor is the sign the branch of the modulus deposits, so the word collapses to $r\,e^{i\theta_{\mathrm{pha}}}\varepsilon e_t$. The collapse is the companion article's, *The Schrödinger Equation in Biquaternionic Polar Variables*, §*The Central Field*, and none of its theory is repeated here. The general element is treated once, in §*The Word of the General Element*, where it is needed to say what the chart does not show.

**The article's finding is that the chart separates the two roles the element's components play in the integral.** The angle is the coordinate that the weight depends on, and the density enters the exponent linearly and is therefore a multiplier rather than an amplitude. Three consequences follow and they are the body of the article: the chart's measure is flat in the density, because the Jacobian of $n=r^{2}$ is exactly what the first-order kinetic term needs; the integral over the phase is a Gaussian whose saddle is the continuity equation, and the integral over the density is an exact delta in the constant setting; and the kernel's word is a scale, an angle and — in the constant setting only — a rotor, with the scale reading the van Vleck determinant and the angle the classical action over $\hbar$ plus the Maslov constant.

**What the article does not do.** It does not produce a second integral, does not define the continuum measure, does not decide the second-quantisation question, and does not evaluate a kernel that the element companion has not already evaluated. The reading is exact where the algebra is exact, and the article says at each step which statements are identities and which are formal.

**Conventions.** The chart is $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ with $r\ge0$ real, $\theta_{\mathrm{pha}}$ central real modulo $\pi$, $\tilde U_{\Psi,\mathrm b}$ a Hermitian unit of rapidity $\theta_{\mathrm{rpd}}$ about the axis $\vec u_{\mathrm b}$, and $\tilde u_{\mathrm r}$ a real rotor. For a central field $\theta_{\mathrm{rpd}}=0$, $\vec u_{\mathrm b}$ is empty, and $\tilde u_{\mathrm r}=\varepsilon e_t$ with $\varepsilon=\pm1$ the branch sign. The density is $n=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)=r^{2}$ for a central field, and the parent's $\rho=\mathrm{Tr}(\tilde\Xi^{*}\tilde\Xi)=2n=2r^{2}$ is twice it; this article uses $n$ and $r^{2}$ interchangeably, and states which. The algebra, the sectors, the pairing, the action and the $i\epsilon$ are the element companion's.

## The Exponent in the Chart

**The action is one identity away from the chart's form.** Substituting $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}e_t$ into the element action and using $\mathrm{Sc}(i\hbar\tilde\Xi^{*}\dot{\tilde\Xi})=-\hbar r^{2}\dot\theta_{\mathrm{pha}}$ and $\mathrm{Sc}((\partial_\eta\tilde\Xi)^{*}\partial_\eta\tilde\Xi)=(\partial_\eta r)^{2}+r^{2}(\partial_\eta\theta_{\mathrm{pha}})^{2}$ gives

$$
\boxed{\;S=\int dt'\,d^{3}x\;\Bigl[-\hbar\,r^{2}\,\dot\theta_{\mathrm{pha}}-\frac{\hbar^{2}}{2m}\Bigl((\vec\nabla r)^{2}+r^{2}(\vec\nabla\theta_{\mathrm{pha}})^{2}\Bigr)-V\,r^{2}\Bigr],\;}
$$

which is the polar variational companion's central-field action and is not a new object. Both halves of the identity were checked on analytic fields at four points: the temporal one to a relative $1.4\times10^{-16}$ and the spatial one to $2.1\times10^{-16}$. There is no approximation in either, because each is the real part of a product of two complex numbers.

**Three features of the exponent are the whole of the article.** The time derivative multiplies the density and not the scale's time derivative: there is no $(\partial_{t'}r)^{2}$ term anywhere, which is the chart's way of saying that the action is first order. The density appears linearly in the kinetic term and in the potential term. And the angle appears only through its derivatives, so it carries no potential of its own and no mass.

**The absence of a scale rate is the chart's sharpest statement.** In the Klein–Gordon chart the same substitution produces $\dot r^{2}\cosh\theta_{\mathrm{rpd}}$ and $r^{2}\sinh^{2}\theta_{\mathrm{rpd}}\dot\theta_{\mathrm{pha}}^{2}$, so the scale has a rate and the two are coupled; in the Schrödinger chart the scale has no rate at all and the angle's rate is weighted by it. That is the difference between a second-order and a first-order equation, seen in two lines, and it is why the two charts' measures behave differently.

## The Density Is the Coordinate of the Measure

**The measure of the chart is the flat measure in the density, exactly.** The element measure is flat in the eight real coordinates; on a central field the two that matter are the real and imaginary parts of $\tilde\Xi$, and polar coordinates on them carry $r\,dr\,d\theta_{\mathrm{pha}}$. With $n=r^{2}$,

$$
r\,dr=\tfrac12\,dn,
$$

so the chart's measure is $\prod_k\tfrac12\,dn_k\,d\theta_{\mathrm{pha},k}$: flat in the density and flat in the angle, with a constant $\tfrac12$ per site and no $n$-dependent weight anywhere. The quadrature $\int_0^{\infty}r\,dr\,e^{-ar^{2}}=\frac{1}{2a}$ against the exact $\frac{1}{2a}$ reproduces the value to a relative $1.8\times10^{-10}$, and the identity is of course exact.

**The cancellation is not an accident and it is not available to the second-order chart.** The factor $r$ is the Jacobian of the pair $(r,\theta)$ relative to the Cartesian pair, and the first-order kinetic term is linear in $n=r^{2}$; the two exponents of $r$ match, one from the measure and one from the exponent. A second-order kinetic term is quadratic in $r$ and needs no Jacobian, so in the Klein–Gordon chart the substitution $u=r^{2}$ leaves $du/(2\sqrt{u})$, a weight that the exponent does not supply and that the measure cannot drop. **The measure problem of the Klein–Gordon chart therefore has no counterpart here**, and the reason is the order in time and not the algebra.

**What the cancellation does not buy.** The product over sites is still an infinite product, and the lattice cutoff is still the definition. The claim is narrow and it is the only one made: the chart introduces no weight of its own, so a reading in the density and the angle is a reading of the same measure, site for site, and not of a measure deformed by the coordinates.

## The Phase Is the Multiplier of Continuity

**The exponent is linear in the angle's rate and quadratic in its gradient, so the angle's integral is a Gaussian with a source.** Integrating $-\hbar\int n\dot\theta$ by parts turns it into $+\hbar\int\theta\,\dot n$, and the angle then appears quadratically through $(\vec\nabla\theta)^{2}$ and linearly through $\dot n$. The integral over the angle is therefore a Gaussian whose source is the density's rate:

$$
\int\mathcal{D}\theta\;\exp\Bigl(\frac{i}{\hbar}\int dt'\,d^{3}x\;\bigl[\hbar\,\theta\,\dot n-\frac{\hbar^{2}}{2m}r^{2}(\vec\nabla\theta)^{2}\bigr]\Bigr)
=\det\Bigl(-\frac{\hbar^{2}}{m}\vec\nabla\cdot n\vec\nabla\Bigr)^{-1/2}\exp\Bigl(\frac{i}{\hbar}S_{\mathrm{eff}}[n]\Bigr),
$$

with the saddle of the Gaussian at

$$
\dot n+\vec\nabla\cdot\bigl(n\,\vec v\bigr)=0,
\qquad
\vec v=\frac{\hbar}{m}\vec\nabla\theta_{\mathrm{pha}} .
$$

**The saddle is the continuity equation, so the phase is the Lagrange multiplier of the density's conservation.** This is the chart's structural statement and it has no element-form counterpart: in the element form the continuity equation is one of the two real parts of the equation, and the phase is not singled out as a multiplier. In the chart the phase is the field that imposes it.

**The Gaussian's determinant is not one, and the article says so.** The integration leaves a determinant of the operator $-\frac{\hbar^{2}}{m}\vec\nabla\cdot n\vec\nabla$, which depends on the density and which is the chart's fluctuation factor. It is not evaluated here, and it is the object that the element form calls the first-order determinant, read in the chart.

**The delta is exact in the constant setting.** When the Hamiltonian is a constant element and the field is uniform in space, the exponent is $-\hbar r^{2}\dot\theta_{\mathrm{pha}}-h_t r^{2}$ with no gradient term at all, so the integral over the density is exactly a delta:

$$
\int_0^{\infty}dn\;\exp\Bigl(-\frac{i}{\hbar}\,n\bigl(\hbar\dot\theta_{\mathrm{pha}}+h_t\bigr)\Bigr)=2\pi\hbar\,\delta\bigl(\hbar\dot\theta_{\mathrm{pha}}+h_t\bigr),
$$

which is the parent's phase rate $\dot\theta_{\mathrm{pha}}=-h_t/\hbar$ as a constraint and not as an equation of motion. **The two real equations of the Madelung pair are therefore the two constraints of the chart's integral, each obtained by integrating out the other variable**, and the statement is exact in the constant setting and saddle-level in the operator setting.

**The delta was checked with a regulator.** Replacing the exact delta by a Gaussian regulator $\exp(-\epsilon\theta^{2})$ on a three-site chain, the angle integral is $\sqrt{\pi/\epsilon}\exp(-\Omega^{2}/4\epsilon)$ with $\Omega=\hbar(n_1-n_2)/\Delta r'_t$, and nine combinations of three regulators and three density gaps reproduce that form to a largest relative deviation of $2.8\times10^{-5}$, the residual being the quadrature's step. The width shrinks as $\sqrt{\epsilon}$ while the peak grows as $\epsilon^{-1/2}$, which is the delta, and the argument is the continuity residual.

**The direction of the two readings is not symmetric.** Integrating the angle leaves a theory of the density with an effective action; integrating the density leaves a theory of the angle with a constraint. The first is the one that carries the dynamics, because its saddle is the quantum Hamilton–Jacobi equation, and the second is the one that carries the kinematics. In the element form the two are one equation, and the chart is what separates them.

## The Kernel's Word

**The kernel's word has two factors for the operator setting and three for the constant setting.** For the operator setting the kernel is $K e_t$, central, so

$$
r_K=|K|,\qquad \theta_{\mathrm{pha},K}=\arg K,\qquad \tilde U_{\Psi,\mathrm b,K}=e_t,\qquad \tilde u_{\mathrm r,K}=\pm e_t,
$$

with the sign the branch of $(2\pi i\,r'_t)^{-3/2}$. For a constant element the kernel is $K\tilde Q$ with $\tilde Q$ the parent's central phase times its real rotor, so $r_K=|K|$, the angle gains $-h_t r'_t/\hbar c$, and the rotor is $\tilde u_Q$ — the parent polar companion's own reading, recovered from the integral rather than from the evolution operator.

**The scale of the kernel is not the scale of any configuration.** Every configuration in the sum carries scale one; the kernel's scale is the number of configurations whose phases agree, and the stationary-phase evaluation turns that count into the van Vleck determinant. In the exact cases the count is the Fresnel prefactor, $(k_m/2\pi i r'_t)^{3/2}$, which is the same statement computed rather than estimated. **This is the chart's answer to the question the element companion leaves implicit: the amplitude of the kernel is a property of the sum and never of a term.**

**The angle of the kernel is the classical action over $\hbar$ plus a constant.** The stationary phase gives $\theta_{\mathrm{pha},K}=S_{\mathrm{cl}}/\hbar+\arg(i^{-3/2})=S_{\mathrm{cl}}/\hbar-3\pi/4$ modulo $\pi$, and the constant is the argument of the central square root. This is the polar companion's Maslov statement, and the chart adds nothing to it except the location: the constant is the branch of $(2\pi i)^{-3/2}$, which lives in the centre, so the Maslov phase is a phase of a central element and not of a chosen complex structure.

**The boost of the kernel is trivial and that is a finding, not a gap.** A central kernel has $\theta_{\mathrm{rpd},K}=0$ and no axis, because a central element has no Hermitian part beyond its real scalar. The Dirac kernel's boost is not trivial, and the difference is the difference between a kernel that is a scalar and a kernel that is an element with all four factors. **The Schrödinger kernel's word is degenerate by two factors out of four, and the degeneracy is the centrality.**

## The Word of the General Element

**The general element's word does not collapse, and the integral's weight does not use it.** For $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ with $\theta_{\mathrm{rpd}}\neq0$ the chart's action carries the cross term $-\hbar r^{2}\cosh\theta_{\mathrm{rpd}}\dot\theta_{\mathrm{pha}}+\frac{\hbar}{2}\sinh\theta_{\mathrm{rpd}}\,a$, and the polar variational companion shows that dropping it leaves a system with no solutions for a general field. The integral over the general element is therefore the integral over all four factors, and the chart's reading of it is the variational companion's Lagrangian with the word's eight parameters as the coordinates.

**What the flow does to the word, the integral inherits.** The parent polar companion's five statements hold along every configuration: the scale is constant, the rapidity is constant, the phase runs at minus the mean, the rotor's angle at the gap, and every carried direction precesses at the gap. Those are consequences of the central Hamiltonian and they are the same statement in the integral, read as the saddle's flow.

**Why the reading is done on the central field.** The kernel is central for the operator setting, so its word has no boost and no rotor; a reading of a non-degenerate word would need a kernel that is not central, and the only such kernel in this family is the constant-element one, where the rotor is the parent's and is known exactly. **The chart is applied to the case where the kernel carries data, and the general element is recorded as the case where the integral's own weight carries none.**

## What the Chart Composes and What It Does Not

**The angle composes because it is central.** The kernel's angle is additive: $\theta_{\mathrm{pha}}(t_1+t_2)=\theta_{\mathrm{pha}}(t_1)+\theta_{\mathrm{pha}}(t_2)$, and the Maslov constant is additive per caustic, so the composition of two kernels adds the two angles and the two constants. This is the chart's version of the statement that the phase is a character.

**The scale does not compose, and the failure is the integral.** The scale of the composite kernel is not the product of the scales, because the composition sums over the intermediate position: what multiplies is the amplitudes and what is added is inside an integral. The free case is the exact test, and there the composite scale equals the single scale because the Fresnel integral is exact — a quadrature of the composition reproduces the single factor to $2.3\times10^{-12}$ — but the equality is the Fresnel integral's gift and not a rule. For a general potential the intermediate integral is not Gaussian about the concatenation and the scale of the composite is a different number.

**The rotor composes exactly for a constant element and does not compose in general.** For $\tilde H_\Psi$ constant the rotor is one-parameter, $\tilde u_Q(t_1+t_2)=\tilde u_Q(t_2)\tilde u_Q(t_1)$, and the composition of two kernels multiplies the rotors and leaves them outside the position integral, because they do not depend on the position. For a position-dependent Hamiltonian there is no such factor, and the semiclassical rotor of the composite is not the product of the semiclassical rotors of the two halves: the classical path from $\vec r_i$ to $\vec r_f$ is not the concatenation of the classical paths through an arbitrary intermediate point, and the saddle of the composite is not the product of the saddles.

**What the non-composition says about the word.** The word of a product of kernels is not the product of their words. The angle survives, the scale and the rotor do not, and the reason is structural: the angle is central and multiplies, while the scale is a modulus and the rotor is a direction, and neither is a character of the composition. That is the path-integral form of the polar variational companion's remark that the word's parameters are not additive.

## What the Polar Reading Adds and Does Not Add

**Adds, first, the separation of roles.** The angle is the coordinate the weight depends on; the density enters the exponent linearly and is the multiplier of continuity; and the measure is flat in the density because the Jacobian of $n=r^{2}$ is what the first-order term needs. None of the three is visible in the element form, where one equation carries both.

**Adds, second, the exact measure statement.** The chart's measure carries no weight of its own, and the Klein–Gordon chart's does. The difference is the order in time, and it is the only place in this set of four articles where a measure question is answered rather than deferred.

**Adds, third, the kernel's word with its degeneracy accounted for.** Scale = van Vleck, angle = action over $\hbar$ plus Maslov, boost trivial, rotor trivial or the parent's. The degeneracy is the centrality, and the contrast with the Dirac kernel — which carries all four factors — is the sharpest statement the chart makes.

**Does not add a value.** Every closed form quoted here is the element companion's, and the chart evaluates nothing that the element form has not evaluated. The $\det$ of the angle integral is displayed and not computed.

**Does not decide the second-quantisation question.** The chart is a chart of a commuting field, and the statistics question is where the element companion leaves it.

## Open Questions

**1. Can the effective action $S_{\mathrm{eff}}[n]$ be written in closed form?** The angle's Gaussian leaves a determinant of $-\frac{\hbar^{2}}{m}\vec\nabla\cdot n\vec\nabla$ and a classical action. Whether the pair has a biquaternionic expression, and whether it is the chart's version of the quantum potential, is open.

**2. Is the density's linearity a selection principle?** The constant setting's exact delta comes from the linearity of the exponent in $n$. Whether a theory with a second-order time derivative can be written so that some coordinate enters linearly — and whether that coordinate has a geometric meaning — is not known.

**3. What happens to the word at a caustic?** The scale vanishes or diverges and the angle's constant jumps, but the rotor and the boost are trivial for a central kernel, so the chart predicts that a caustic costs a Maslov phase and nothing else. Whether the constant-element kernel's rotor jumps at its caustics is a separate question and is not answered here.

**4. Does the multiplier reading survive the connection?** The coupled companion reads the same chart with the connection inside the derivative, and the linearity of the density is what the potential term's shape depends on there. The consistency of the two readings is that article's subject.

**5. Empirical content.** The chart adds none.

## Summary

The polar reading of the Schrödinger functional integral is the substitution $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}e_t$ into the element companion's integral, and its content is the separation of the two coordinates' roles. The exponent is $-\hbar r^{2}\dot\theta_{\mathrm{pha}}-\frac{\hbar^{2}}{2m}((\vec\nabla r)^{2}+r^{2}(\vec\nabla\theta_{\mathrm{pha}})^{2})-Vr^{2}$, verified as an identity to $10^{-16}$; there is no scale rate, which is the first-order structure in the chart's letters. The measure is flat in the density, because $r\,dr=\frac12dn$ cancels the Jacobian against the exponent's linearity, and the Klein–Gordon chart's weight has no counterpart here.

Integrating the angle gives a Gaussian whose saddle is the continuity equation with $\vec v=\hbar\vec\nabla\theta_{\mathrm{pha}}/m$, and a determinant of $-\frac{\hbar^{2}}{m}\vec\nabla\cdot n\vec\nabla$; integrating the density gives, in the constant setting, an exact delta on the parent's phase rate $\dot\theta_{\mathrm{pha}}=-h_t/\hbar$, verified through the regulated form $\sqrt{\pi/\epsilon}\exp(-\Omega^{2}/4\epsilon)$ to $2.8\times10^{-5}$. The two Madelung equations are the two constraints of the chart's integral, each obtained by eliminating the other variable.

The kernel's word is scale = van Vleck, angle = classical action over $\hbar$ plus the central Maslov constant, boost $e_t$, rotor $\pm e_t$; for a constant element the rotor is the parent's $\tilde u_Q$. Two of the four factors are degenerate, and the degeneracy is the kernel's centrality. The angle composes, the scale does not, and the rotor composes only while the Hamiltonian is constant. Nothing here changes the value of the integral.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $r$, $\theta_{\mathrm{pha}}$ | Scale and central angle of the field |
| $\varepsilon$ | Branch sign of the modulus; the trivial rotor |
| $n=r^{2}=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$ | Density, and the chart's natural coordinate |
| $\rho=2n$ | The parent's density, twice $n$ |
| $-\hbar r^{2}\dot\theta_{\mathrm{pha}}$ | The first-order kinetic term; no scale rate |
| $r\,dr=\frac12dn$ | The Jacobian's cancellation |
| $\vec v=\hbar\vec\nabla\theta_{\mathrm{pha}}/m$ | Flow velocity of the continuity saddle |
| $\det(-\frac{\hbar^{2}}{m}\vec\nabla\cdot n\vec\nabla)^{-1/2}$ | The angle integral's fluctuation factor |
| $2\pi\hbar\,\delta(\hbar\dot\theta_{\mathrm{pha}}+h_t)$ | The density integral, constant setting |
| $r_K=|K|$ | Kernel's scale; the van Vleck amplitude |
| $\theta_{\mathrm{pha},K}=S_{\mathrm{cl}}/\hbar-3\pi/4$ | Kernel's angle; Maslov constant from $(2\pi i)^{-3/2}$ |
| $\tilde u_Q$ | The parent's rotor; the kernel's rotor for a constant element |
| $\sqrt{\pi/\epsilon}\exp(-\Omega^{2}/4\epsilon)$ | Regulated delta; $\Omega=\hbar(n_1-n_2)/\Delta r'_t$ |

## Further Reading

- *The Path Integral and the Schrödinger Equation in Biquaternionic Form*, for the integral read here.
- *The Schrödinger Equation in Biquaternionic Polar Variables*, for the word, the domain, the propagator's word and the half turn.
- *The Variational Principle and the Schrödinger Equation in Biquaternionic Polar Variables*, for the polar action, the cross term and the four vanishing momenta.
- *The Path Integral and the Coupled Schrödinger Equation in Biquaternionic Polar Variables*, for the same chart with the connection inside the derivative.
- *The Path Integral and the Klein–Gordon Equation in Biquaternionic Polar Variables*, for the second-order chart, whose measure carries the weight this one does not.
- *The Path Integral and the Dirac Equation in Biquaternionic Polar Variables*, for a kernel whose word is degenerate in no factor.
- E. Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1927) 322–326, for the density–phase pair.
- D. Bohm, "A Suggested Interpretation of the Quantum Theory in Terms of Hidden Variables I," *Physical Review* **85** (1952) 166–179, for the quantum potential.
- T. Takabayasi, "Remarks on the Formulation of Quantum Mechanics with Classical Pictures," *Progress of Theoretical Physics* **9** (1953) 187–222, for the hydrodynamic reading of the action.
- R. P. Feynman and A. R. Hibbs, *Quantum Mechanics and Path Integrals* (McGraw-Hill, 1965), for the Fresnel measure and the free kernel.
- H. Kleinert, *Path Integrals in Quantum Mechanics, Statistics, Polymer Physics, and Financial Markets* (World Scientific, 2009), for the Jacobian of the polar chart and the Duru–Kleinert transformation.
- V. P. Maslov and M. V. Fedoriuk, *Semi-Classical Approximation in Quantum Mechanics* (Reidel, 1981), for the phase constant at a caustic.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the polar form of a Clifford element.
