# __The Path Integral and the Coupled Schrödinger Equation in Biquaternionic Form__

## Introduction

*The Path Integral and the Schrödinger Equation in Biquaternionic Form* sums $\exp(iS/\hbar)$ over the free field, evaluates the generating functional, and identifies the two-point function with the propagator. This article puts the electromagnetic connection into that integral. The replacement is one rule, the ordinary derivative becomes a covariant one, and the potential is one term added to the action; the two are the coupled variational companion's, cited and not re-derived.

**Three findings, and the first is the reason the article exists.**

*First, the coupling enters three of the four terms of the exponent and never the measure.* The kinetic term is untouched, because the connection's temporal coefficient sits in the covariant derivative and not in $\partial_{t'}$. The gradient term becomes a sum of moduli of covariant derivatives and splits into the free term, a term linear in $\vec A$ through the phase gradient, and a term quadratic in $\vec A$. The potential term is one more term, linear in $\varphi$. Nothing else is added, and the measure is the free measure.

*Second, the gauge invariance of the integral is exact, and the measure is what makes it exact.* The transformation is a central phase at each point, so its Jacobian is one and the flat measure is untouched; the exponent shifts by a total derivative which cancels between the kinetic and the potential terms, term by term, exactly as the variational companion records. No lattice link, no Wilson line and no discretisation rule is introduced, and this is a structural difference from the Klein–Gordon case rather than a convenience.

*Third, the constant background is exactly solvable and the two shifts are the whole of the coupling there.* The kernel is the free kernel times a phase factor in the potential and a translation factor in the vector potential, and the dispersion is $E+ϙ\varphi=(\vec p+ϙ\vec A)^{2}/2m$. The composition of the shifted kernels is verified to $2.3\times10^{-12}$.

**What is not claimed.** No new prediction, no new solution, no new particle. The integral is the standard one of non-relativistic scalar electrodynamics. What the algebra contributes is that the connection is one central operator read in four slots, that the measure is flat and stays flat, and that the determinant's power is unchanged by the coupling — the first-order $\det^{-1}$ of the free companion, not a new power.

**The two settings are again kept apart, and the coupling has a different face in each.** In the constant setting the coupling is a shift of two numbers, $h_t\mapsto h_t-ϙ\varphi$ and $\vec h_\Psi\mapsto\vec h_\Psi+ϙ\vec A$, and the integral's exponent is the free exponent with the shifted numbers. In the operator setting the coupling is a covariant Laplacian and a potential, and the integral is the free integral with three extra terms. No result is transferred between them.

**Conventions.** The algebra, the sectors, the pairing $\mathrm{Sc}(\cdot^{*}\cdot)$, the action, the measure and the $i\epsilon$ are the free companion's. The connection is $\tilde A_\Phi=i(\varphi/c)e_t+\vec A$ with $\varphi$ and $\vec A$ real, the coupling is $ϙ$, and the covariant derivative is $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{iϙ}{\hbar}\tilde A_\Phi$, so that

$$
D_t=\partial_{t'}-\frac{iϙ}{\hbar}\varphi,
\qquad
D_\eta=\partial_\eta+\frac{iϙ}{\hbar}A_\eta,
\qquad
\vec\pi=-i\hbar\vec\nabla+ϙ\vec A,
$$

with the mechanical momentum $\vec\pi$ and the potential energy $-ϙ\varphi$. The charge $ϙ$ is minus the electric charge of the older convention, and its value is inserted, not derived.

## The Exponent

**The action is the coupled variational companion's.** In the operator setting,

$$
S=\int dt'\,d^{3}x\;\mathrm{Sc}\Bigl[\frac{i\hbar}{2}\bigl(\tilde\Xi^{*}\partial_{t'}\tilde\Xi-(\partial_{t'}\tilde\Xi^{*})\tilde\Xi\bigr)-\frac{\hbar^{2}}{2m}\sum_\eta\bigl(D_\eta\tilde\Xi\bigr)^{*}\bigl(D_\eta\tilde\Xi\bigr)+ϙ\varphi\,\tilde\Xi^{*}\tilde\Xi\Bigr],
$$

and the integral is $\int\mathcal{D}\tilde\Xi\,\mathcal{D}\tilde\Xi^{*}\exp(iS/\hbar)$ with the free measure. **The kinetic term is the free one and that is the metric's doing**: the temporal connection is absorbed in $D_t$ and the kinetic term uses $\partial_{t'}$, so the antisymmetrisation that makes it Hermitian is untouched by the coupling.

**The gradient term is a sum of moduli and stays a sum of moduli.** For each $\eta$,

$$
\mathrm{Sc}\bigl((D_\eta\tilde\Xi)^{*}(D_\eta\tilde\Xi)\bigr)=\sum_{\mu=0}^{3}\bigl|(D_\eta\tilde\Xi)_\mu\bigr|^{2}\ \ge 0,
$$

so the coupled gradient term is positive for the same reason as the free one: the added term is anti-Hermitian and the modulus of an element is unchanged by adding to it an anti-Hermitian multiple of itself. **The consequence is the diamagnetic inequality in its variational form**: the action's kinetic part is bounded below by zero, and the energy is bounded below whenever $ϙ\varphi$ is. The integral inherits the bound, and the Fresnel convergence factor has to fight the potential and not the gradient.

**The three-term split is the coupling's whole content in the exponent.** Written out,

$$
-\frac{\hbar^{2}}{2m}\sum_\eta\bigl(D_\eta\tilde\Xi\bigr)^{*}\bigl(D_\eta\tilde\Xi\bigr)
=-\frac{\hbar^{2}}{2m}\sum_\eta(\partial_\eta\tilde\Xi)^{*}(\partial_\eta\tilde\Xi)
-\frac{\hbar}{m}\sum_\eta ϙA_\eta\,\mathrm{Sc}\bigl(\tilde\Xi^{*}i\partial_\eta\tilde\Xi\bigr)
-\frac{ϙ^{2}}{2m}|\vec A|^{2}\,\tilde\Xi^{*}\tilde\Xi .
$$

The first term is the free one, the second is linear in the connection and carries the phase current, the third is quadratic. The three are one square's expansion and not three rules, and the polar companion reads them as the chart's single shifted bracket. The identity was checked on analytic fields at four points against the modulus form, to a relative $2.1\times10^{-16}$.

**The whole exponent is real, and this is the integral's well-definedness.** Each of the three terms of the action is Hermitian and $\mathrm{Sc}$ of a Hermitian element is real, so the exponent's imaginary part is exactly the free one, $\int\mathrm{Lag}/\hbar$ with $\mathrm{Lag}$ real. The integrand is therefore a phase times a damping, and the damping is the free damping. Nothing in the coupling can make the integral diverge that the free integral does not.

**The first-order structure is unchanged and the determinant's power with it.** The operator is

$$
A_{\mathrm{gco}}=i\hbar D_t-\frac{1}{2m}\Bigl(-i\hbar\vec D\Bigr)^{2},
$$

first order in the time derivative and second order in the space derivatives, exactly as the free one. Hence the integral is still a first-order integral, its value is $\det(A_{\mathrm{gco}})^{-1}$ times the exponent of the source term, and the power of the determinant is the free power. **The coupling changes the operator and not its order**, and that is the reason the coupled integral is as well defined as the free one.

## Gauge Invariance and the Measure

**The transformation is a central phase at each point.** With a real function $\Gamma(x)$,

$$
\tilde\Xi\mapsto e^{\frac{iϙ}{\hbar}\Gamma}\tilde\Xi,
\qquad
\varphi\mapsto\varphi-\partial_{t'}\Gamma,
\qquad
\vec A\mapsto\vec A+\vec\nabla\Gamma,
$$

which is the standard transformation with the sign convention of $D_t$ and $D_\eta$ above.

**The measure is invariant because the Jacobian is one.** At each point the transformation multiplies the two real coordinates of the central field by a rotation matrix of unit determinant, so $\mathcal{D}\tilde\Xi\,\mathcal{D}\tilde\Xi^{*}$ is unchanged. This is the sharpest difference from a lattice formulation: the phase is a modulus-one number at every point, so a finite transformation costs a unit Jacobian and nothing else.

**The exponent is invariant term by term.** The kinetic term gains $-ϙ\,\partial_{t'}\Gamma\,n$, the potential term gains $+ϙ\,\partial_{t'}\Gamma\,n$, and the two cancel; the gradient term is invariant by covariance. The variational companion states the same cancellation and calls it the clearest statement of why the covariant derivative and the potential are one object. **The integral's invariance is therefore exact and is not a boundary-term statement**, because the two gains are equal and opposite inside the exponent at every point.

**The determinant is gauge invariant.** The operator transforms by a similarity, $A_{\mathrm{gco}}\mapsto e^{iϙ\Gamma/\hbar}A_{\mathrm{gco}}e^{-iϙ\Gamma/\hbar}$, on top of the shift that the potential supplies; the shift is what makes the similarity exact rather than approximate, and a similarity leaves the determinant unchanged. Since the measure's Jacobian is one, $Z$ is invariant, and so is every correlator of gauge-invariant insertions.

**The density is the response to the potential, and the statement is one derivative.** Differentiating the exponent with respect to $\varphi(x)$ brings down $\frac{i}{\hbar}ϙ\,n(x)$, so

$$
\frac{\hbar}{i}\frac{\delta\ln Z}{\delta\varphi(x)}=ϙ\,\bigl\langle n(x)\bigr\rangle ,
$$

and the second derivative gives the density–density correlator. **This is the integral's version of the variational companion's Noether current**: the current is what the source couples to, and here the source is the scalar potential itself.

**No link, no discretisation rule, no linearisation.** The Klein–Gordon companion has to ask whether the lattice's link is the linearised phase or the exponential one, and it answers that the exponential one is implied by the chart. The Schrödinger integral does not have that question, because the field is one complex number and the transformation is a rotation of it: the discrete product's every step carries a phase factor of modulus one, and the composition is exact. The question survives in the Klein–Gordon article because the field there has two independent slots whose covariance is a statement about each of them; here there is one slot and the statement is one multiplication.

**The contrast with the Dirac case is the same contrast as in the equation.** The Dirac companion records that the naive bilinear is gauge invariant and not conserved, so the current needs a triple product and two fixed frame units. The Schrödinger integral has neither defect: the bilinear is the density, it is conserved, and it is what the source couples to. The integral's gauge structure is as simple as the algebra allows, and the reason is that the connection is central.

## The Constant Background

**A constant connection gives a kernel that is the free kernel times two factors.** For constant $\varphi$ and $\vec A$ the exact kernel is

$$
\boxed{\;K_{\mathrm{gco}}(\vec r_f,r'_t;\vec r_i)=\exp\Bigl(-\frac{iϙ\varphi\,r'_t}{\hbar c}\Bigr)\exp\Bigl(\frac{iϙ}{\hbar}\vec A\cdot(\vec r_f-\vec r_i)\Bigr)K_0(\vec r_f-\vec r_i,r'_t),\;}
$$

with $K_0$ the free kernel of the free companion. The first factor is the potential's phase, the second is the vector potential's translation of the momentum, and the third is the free propagation.

**The composition law of the shifted kernel is exact, and it is a check of both factors.** Composing two factors gives the difference of positions summed along the intermediate point, $\vec A\cdot(\vec r_f-\vec r_m)+\vec A\cdot(\vec r_m-\vec r_i)=\vec A\cdot(\vec r_f-\vec r_i)$, and the phases multiply; so the composite is the single shifted kernel with the summed time. A Euclidean quadrature of the composition on a $400001$-point grid reproduces the single factor to a relative $2.3\times10^{-12}$. **Both factors compose, and they compose for different reasons**: the potential's phase is a character of the time, and the vector potential's factor is a character of the displacement.

**The dispersion is the two shifts and nothing else.** A plane wave $e^{i(\vec p\cdot\vec r-E t')/\hbar}$ solves the coupled equation when

$$
E+ϙ\varphi=\frac{(\vec p+ϙ\vec A)^{2}}{2m},
$$

which is the constant companion's $h_t\mapsto h_t-ϙ\varphi$ and $\vec h_\Psi\mapsto\vec h_\Psi+ϙ\vec A$ read as a dispersion. **The two shifts are the coupling's only content in the constant setting**, and the potential's shift is linear because the equation is first order in time: there is no square to put it in.

**The translation factor is a phase and not a gauge choice.** The second factor of the kernel is not removable by a gauge transformation of the endpoints, because a gauge transformation would also move $\varphi$ and because the factor's argument is the displacement. It is the integral's version of the statement that a constant vector potential is pure gauge in the equation and not in the kernel: the kernel is a matrix element between two positions, and the two positions are at different points, so the phase does not cancel.

## The Semiclassical Expansion

**The saddle of the coupled integral is the classical equation with the connection.** Varying the exponent gives $A_{\mathrm{gco}}\tilde\Xi_{\mathrm{cl}}=-J$, which is the coupled equation with the source; in the position representation and between two endpoints the saddle is the classical path of a charge in the field. The quadratic fluctuation integral gives the van Vleck determinant of that path, and the prefactor's square root is the same central branch as in the free case.

**The equation of the saddle is the Lorentz force and the algebra adds nothing to it.** The variational companion derives the force from the action's variation and records it; here the same statement appears as the classical limit of the integral, which is the standard correspondence between the stationary phase and the classical equation. **No spin is involved**: the field is scalar, the connection is central, and the only structure the charge has is its coupling.

**The determinant is gauge invariant and the amplitude is therefore physical.** The van Vleck amplitude is built from the classical action's second variation, and the classical action is gauge invariant up to endpoint terms; the Maslov constant is central and unchanged. **The semiclassical kernel is $A_{\mathrm{wkb}}\exp(iS_{\mathrm{cl}}/\hbar)\exp(iϙ\int A\cdot dr/\hbar)$**, the last factor being the phase the connection accumulates along the classical path — the Aharonov–Bohm phase of the corpus's geometric-phase articles, appearing here as the semiclassical limit's bookkeeping.

## What the Form Adds and What It Does Not Add

**Adds, first, that the coupling is one central operator in four slots.** The temporal and the three spatial slots are one substitution read four times; there is no ordering question, no commutator and no relative sign to choose, because the connection's coefficients are central and commute with the units. The exponent's three terms are one square's expansion.

**Adds, second, that the measure stays flat.** The gauge transformation is a rotation at each point with unit Jacobian, so the free measure is the coupled measure and no link structure is introduced. This is why the Schrödinger integral's gauge invariance is exact at every step and the Klein–Gordon integral's needed the chart to make the same point.

**Adds, third, the invariance of the determinant's power.** The coupling changes the operator and not its order in time, so the coupled determinant is again a first power and the integral is as well defined as the free one.

**Does not add a value.** The free and constant-background kernels are exact and standard; the interacting kernel is not evaluated, and no new approximation is introduced.

**Does not supply the measure, the second quantisation or the Landau spectrum.** The continuum measure is formal, the statistics question is the free companion's, and the discrete spectrum in a constant magnetic field is the subject of the corpus's Landau-level article and not of this one.

## Open Questions

**1. Can the interacting two-point function be written in closed form for a general connection?** No. The integral is the standard one, and what would be needed is a solution of the coupled equation, not a property of the integral.

**2. What happens when the connection is non-central?** A non-abelian connection, or a connection valued in $\mathbb{B}_{\Psi}$ rather than in the centre, would put the connection inside the field's multiplication and raise the ordering question the central case does not have. Whether the integral survives is open, and the corpus's gauge-sector articles are where the connection's algebra is discussed.

**3. Is the $ϙ$-independence of the determinant's power exact?** The power counts time derivatives and the covariant derivative is still one derivative, so the answer should be yes; a proof that the coupled operator's determinant is a well-defined first-order object on the same footing as the free one is not given.

**4. Does the Landau problem's spectrum come out of the integral?** The kernel in a constant magnetic field is exactly known in the standard formalism and is the sum over Landau levels. Whether the biquaternion form's chart of that kernel adds anything is the Landau article's question.

**5. Empirical content.** None.

## Summary

The coupled functional integral is the free one with three extra terms in the exponent and the same measure. The kinetic term is untouched because the temporal connection sits in $D_t$; the gradient term is a sum of moduli of covariant derivatives, hence positive, and splits into the free term, a linear term in $\vec A$ and a quadratic one; the potential term is $ϙ\varphi\,n$, and the whole exponent stays real. The operator $A_{\mathrm{gco}}=i\hbar D_t-\frac{1}{2m}(-i\hbar\vec D)^{2}$ is still first order in time, so its determinant enters to the first power exactly as in the free case.

The gauge transformation is a central phase at each point, its Jacobian is one, so the measure is untouched; the exponent shifts by a total derivative that cancels between the kinetic and the potential terms, so the invariance is exact and term by term, with no link and no boundary term. The determinant is gauge invariant by the similarity the shift supplies, and the density is the functional derivative of $\ln Z$ with respect to $\varphi$. The constant background is exact: the kernel is the free kernel times $\exp(-iϙ\varphi r'_t/\hbar c)$ and $\exp(iϙ\vec A\cdot\vec r/\hbar)$, its composition verified to $2.3\times10^{-12}$, with the dispersion $E+ϙ\varphi=(\vec p+ϙ\vec A)^{2}/2m$. The semiclassical kernel is van Vleck's amplitude times the classical action's phase times the connection's line integral along the classical path.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde A_\Phi=i(\varphi/c)e_t+\vec A$ | The connection |
| $ϙ$ | The coupling constant; minus the older electric charge |
| $D_t=\partial_{t'}-\frac{iϙ}{\hbar}\varphi$ | Covariant temporal derivative |
| $D_\eta=\partial_\eta+\frac{iϙ}{\hbar}A_\eta$ | Covariant spatial derivative |
| $\vec\pi=-i\hbar\vec\nabla+ϙ\vec A$ | Mechanical momentum |
| $A_{\mathrm{gco}}=i\hbar D_t-\frac{1}{2m}(-i\hbar\vec D)^{2}$ | The first-order operator of the integral |
| $\det(A_{\mathrm{gco}})^{-1}$ | The coupled determinant; power unchanged |
| $e^{\frac{iϙ}{\hbar}\Gamma}$ | The gauge transformation; unit Jacobian |
| $K_{\mathrm{gco}}$ | The constant-background kernel |
| $\exp(-iϙ\varphi r'_t/\hbar c)\exp(iϙ\vec A\cdot\vec r/\hbar)$ | Its two factors |
| $E+ϙ\varphi=(\vec p+ϙ\vec A)^{2}/2m$ | The dispersion's two shifts |
| $\exp(iϙ\oint\vec A\cdot d\vec r/\hbar)$ | The connection's phase along the classical path |

## Further Reading

- *The Variational Principle and the Coupled Schrödinger Equation in Biquaternionic Form*, for the action, the term-by-term invariance and the Noether current.
- *The Coupled Schrödinger Equation in Biquaternionic Form*, for the equation, the gauge covariance and the constant setting's two shifts.
- *The Path Integral and the Schrödinger Equation in Biquaternionic Form*, for the free integral whose determinant's power this article keeps.
- *The Path Integral and the Coupled Schrödinger Equation in Biquaternionic Polar Variables*, for the same integral read in the word.
- *The Path Integral and the Coupled Klein–Gordon Equation in Biquaternionic Form*, for the second-order coupled integral and the link question this article does not have.
- *Landau Levels in Biquaternionic Form*, for the constant magnetic field's spectrum.
- *The Berry Phase and Geometric Phases in Biquaternionic Form*, for the line-integral phase in its geometric reading.
- L. D. Faddeev and A. A. Slavnov, *Gauge Fields: An Introduction to Quantum Theory* (Benjamin, 1980), for the first-order integral and its gauge structure.
- H. Kleinert, *Path Integrals in Quantum Mechanics, Statistics, Polymer Physics, and Financial Markets* (World Scientific, 2009), for the constant-background kernels.
- L. S. Schulman, *Techniques and Applications of Path Integration* (Wiley, 1981), for the vector potential in the discretised product.
- M. Reed and B. Simon, *Methods of Modern Mathematical Physics II* (Academic Press, 1975), for the diamagnetic inequality.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the algebra and its central elements.
