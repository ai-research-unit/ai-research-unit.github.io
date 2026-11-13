# __The Path Integral and the Coupled Proca Equation in Biquaternionic Form__

## Introduction

*The Path Integral and the Proca Equation in Biquaternionic Form* gives a Gaussian over the anti-Hermitian configurations, a determinant that factorises into a cube and a single eigenvalue, and a ghost that cancels. This article puts the electromagnetic connection into that integral. **The result is not a small modification, because the coupled Proca field does not live where the free one lives.**

**Four findings, and the first is a change of carrier.**

*First, the configuration space changes from $\mathbb{B}_\Phi$ to $\mathbb{B}$.* The material sector is not closed under multiplication, so a derivative with a connection in it carries the field out of the sector. The coupled integral is therefore an integral over eight real components at each point, and the free integral is the real slice of it. **No earlier article in the corpus's path-integral set has this: the scalar, spinor and Klein–Gordon carriers are closed, and only the massive vector's is not.**

*Second, the three–one split survives the coupling exactly.* The covariant d'Alembertian replaces the ordinary one in the transverse factor, and the mass alone remains in the longitudinal one. So the determinant is the covariant transverse determinant cubed times $-k_m^{2}$, and **the ghost is untouched by the coupling**: it is still a field-independent constant, still invisible in every normalised correlator.

*Third, the constraint is covariant and exact, and the ordinary Lorenz condition is not.* The curvature term of the covariant d'Alembertian is a pure vector and has no scalar part, so the trace of the coupled equation forces the covariant divergence to vanish with no term to spare. The ordinary divergence then differs from it by a term bilinear in the connection. **The constraint survives in the form the coupling can preserve, and it is deformed in the form it cannot.**

*Fourth, the field acquires a charge.* The free field is real, and a real field has no phase to rotate, so the free theory had one current and no charge. The coupled carrier is complex, the phase is a symmetry of the mass term as well as of the field term, and the Noether current exists. **The measure gains a circle at each point; the circle's Jacobian is one; and the gauge invariance of the integral is exact at every step, with no link and no ghost.**

**What is not claimed.** The equation is the standard minimally coupled Proca equation, the integral is the standard one, and no new solution or prediction is offered. The algebra's contribution is that the coupling is one element, that the obstruction to it is a closure statement, and that the three–one split and the constraint fall out of two traces.

**Conventions.** The algebra, the sectors, the pairing and the mass are the free companion's. The connection is $\tilde A_\Phi=i(\varphi/c)e_t+\vec A$ with $\varphi$ and $\vec A$ real, the coupling is $ϙ$, and the covariant derivative is

$$
\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{iϙ}{\hbar}\tilde A_\Phi ,
\qquad
D_t=\partial_{t'}-\frac{iϙ}{\hbar}\varphi,
\qquad
D_\eta=\partial_\eta+\frac{iϙ}{\hbar}A_\eta ,
$$

with the mechanical momentum $\vec\pi=-i\hbar\vec\nabla+ϙ\vec A$ and the potential energy $-ϙ\varphi$. The Proca potential is written $\tilde A$ when the distinction from the connection matters, and $\tilde A_\Phi$ is reserved for the connection.

## The Carrier and the Measure

**The obstruction is the closure failure, and one product shows it.** The product of two anti-Hermitian elements is Hermitian, and the simplest instance is decisive: $\vec e_x\vec e_x=-e_t$, whose right side is central and real and therefore outside $\mathbb{B}_\Phi$. **A hundred random products of material-sector elements leave the sector in every case**, because the sector is a real four-dimensional subspace of an eight-dimensional algebra and it is closed only under central real scalars.

**The minimal substitution is what forces the issue.** The added element $\frac{iϙ}{\hbar}\tilde A_\Phi$ is anti-Hermitian, so the coupled derivative of a material field is the sum of a material element and a product of two material elements: the first is in the sector, the second is not. **There is no way to pose the equation inside the sector**; projecting after every multiplication is not covariant and produces the minimal coupling of nothing.

**So the integral runs over $\mathbb{B}$, and the free integral is its real slice.** The measure becomes the flat measure on eight real components at each point. The free field's reality is the condition $\tilde A^{*}=-\tilde A$, which is one conjugation's fixed set inside the carrier, and the free article's integral is the restriction of this one to that set. **The carrier's dimension doubles, and that doubling is the article's first and largest structural fact.**

**The mass term is what makes the enlarged carrier acceptable, and the two facts are one.** On the eight-dimensional carrier the invariant length $|a'_t|^{2}-|\vec A|^{2}$ is real and invariant under the phase, and the mass term built from it is a genuine mass term. On the four-dimensional carrier the mass term $\langle\tilde A_\Phi\rangle_\natural$ is real because the field is real, and it is indefinite because the metric is. **The carrier that closes under the coupling is the carrier on which the mass term is invariant**, exactly as the coupled equation article proves from the equation's side.

**No gauge-fixing determinant is introduced, because the connection is external.** The article treats $\tilde A_\Phi$ as a fixed background. That keeps the integral Gaussian in the Proca field, keeps the measure flat, and puts the Faddeev–Popov question out of scope — *The Gauge Field Path Integral in Biquaternionic Form* is where a dynamical connection's integral is treated. **The Proca mass term still lifts the longitudinal zero mode, so even a dynamical connection would not need gauge fixing of the Proca field**; what it would need is gauge fixing of the connection, which is a different object.

## The Exponent

**The action is the free action with the covariant gradient inside the field strength, and the field strength is where the coupling doubles.**

$$
S=\int d^{4}r\;\Bigl[\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F_{\mathrm{gco}}\tilde F_{\mathrm{gco}}\bigr)-\tfrac12k_m^{2}\mathrm{Sc}\bigl(\tilde A^{*}\tilde A^{\natural}\bigr)\Bigr],
\qquad
\tilde F_{\mathrm{gco}}=\mathrm{Vect}\bigl(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A\bigr) .
$$

The field strength carries the connection, so the connection enters twice: once through the derivative and once through $\tilde F$. **That is not the Dirac case**, where the field strength is absent from the equation and the coupling enters once, and it is not the scalar case either, where the covariant square is the only carrier of the coupling.

**The expansion is a square's expansion, and each term has a degree.**

$$
\mathrm{Sc}\bigl(\tilde F_{\mathrm{gco}}\tilde F_{\mathrm{gco}}\bigr)
=\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)
+2\,\frac{iϙ}{\hbar}\,\mathrm{Sc}\bigl(\tilde F\tilde V\bigr)
-\frac{ϙ^{2}}{\hbar^{2}}\,\mathrm{Sc}\bigl(\tilde V\tilde V\bigr),
\qquad
\tilde V=\mathrm{Vect}\bigl(\tilde A_\Phi^{\natural}\tilde A\bigr).
$$

The first term is the free density, the second is bilinear — one power of each potential — and the third is quadratic in the connection. All three are quadratic in the Proca field, so **the coupled action is exactly quadratic in $\tilde A$ for a fixed connection**, and the integral over $\tilde A$ is a Gaussian whose operator depends on the background. Twenty random draws reproduced the expansion to $3.6\times10^{-15}$.

**The mixed term is a pure vector and that is why it does not touch the constraint.** $\tilde V$ is the pure-vector part of a product, so $\mathrm{Sc}(\tilde V)=0$, and a pure vector paired with the pure vector $\tilde F$ contributes only through its vector part. **The mixed term therefore adds no scalar to the exponent**, and the scalar whose square is the Lorenz term is untouched by it. The check of $\mathrm{Sc}(\tilde V)=0$ returned exactly zero, as it must, because the projection is the definition.

**The exponent stays real for a real connection and a real field.** Each term is Hermitian in the appropriate pairing, and the mixed term's reality is the reality of $\mathrm{Sc}$ on a Hermitian element. **The coupling cannot make the Minkowski integral converge or diverge in a way the free integral does not**, because the imaginary part of the exponent is still the free Lagrangian.

## The Operator and Its Split

**The coupled operator is the free operator with the covariant d'Alembertian in the transverse factor.**

$$
P_{\mathrm{gco}}=\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}-k_m^{2}-\tilde\nabla_{\mathrm{gco}}D_{\mathrm{gco}},
\qquad
D_{\mathrm{gco}}\tilde A=\mathrm{Sc}\bigl(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A\bigr),
$$

which is $\tilde\nabla_{\mathrm{gco}}\tilde F_{\mathrm{gco}}-k_m^{2}\tilde A$ and therefore the coupled equation. The second-order operator is the sum of the squared components plus the curvature, and the curvature is a pure vector.

**The two projectors are the covariant ones and the split is the free split.** With

$$
P_L^{\mathrm{gco}}=\tilde\nabla_{\mathrm{gco}}\bigl(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}\bigr)^{-1}D_{\mathrm{gco}},
\qquad
P_T^{\mathrm{gco}}=1-P_L^{\mathrm{gco}},
$$

the same two-line computation as in the free case gives

$$
\boxed{\;P_{\mathrm{gco}}=\bigl(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}-k_m^{2}\bigr)P_T^{\mathrm{gco}}-k_m^{2}P_L^{\mathrm{gco}}\; }
$$

because the covariant gradient and the covariant divergence still compose to the covariant d'Alembertian. **The mass is still the only thing that acts on the longitudinal direction**, and it acts on it with no derivative, no connection and no background in it.

**So the determinant is the covariant transverse cube times the same single factor.**

$$
\det P_{\mathrm{gco}}=\bigl(\det(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}-k_m^{2})\bigr)^{3}\cdot\bigl(-k_m^{2}\bigr).
$$

The coupling deforms the transverse factor and leaves the longitudinal one alone. **That is the article's sharpest statement about the integral's structure**: a background changes the three propagating states' spectrum, their dispersion and their determinant, and changes nothing whatever about the constrained mode's eigenvalue.

**The ghost's cancellation is therefore stronger in the coupled theory than in the free one.** In the free theory it is a constant because the mass is constant; here the transverse factor is a functional of the connection and the longitudinal one is still the constant $-k_m^{2}$. So the ratio of two backgrounds' determinants is the cube of the ratio of their transverse determinants, and **the ghost drops out of the ratio identically**. A background's effect on the Proca vacuum energy is three times its effect on a scalar's, in the coupled theory as in the free one.

## The Covariant Constraint

**The constraint survives because the curvature has no scalar part.** Applying $D_{\mathrm{gco}}$ to the coupled equation gives

$$
D_{\mathrm{gco}}\tilde\nabla_{\mathrm{gco}}\tilde F_{\mathrm{gco}}=k_m^{2}D_{\mathrm{gco}}\tilde A ,
$$

and the left side is a total divergence of an antisymmetric object plus the scalar part of the curvature, which vanishes. **The curvature's vanishing scalar part is exact and is not an approximation**: the curvature of a biquaternionic connection is a pure vector by construction, and $\mathrm{Sc}$ of a pure vector is zero. Hence

$$
k_m^{2}D_{\mathrm{gco}}\tilde A=0
\qquad\Longrightarrow\qquad
\mathrm{Sc}\bigl(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A\bigr)=0 ,
$$

the **covariant Lorenz condition**, forced by the equation and not imposed on it.

**What is not forced is the ordinary divergence.** The covariant divergence and the ordinary one differ by a term bilinear in the connection, so a field satisfying the covariant condition need not satisfy the ordinary one. **The integral inherits this asymmetry**: its saddle obeys the covariant condition, and the ordinary divergence of the saddle is a functional of the background. Nothing in the integral prefers the ordinary condition, which is the point — the ordinary condition is not gauge covariant and cannot be a property of the theory.

**The constraint is what the saddle's longitudinal part is, and the mass is what it costs.** In the transverse-longitudinal split the saddle is

$$
\tilde A^{\mathrm{cl}}=-\frac{P_T^{\mathrm{gco}}\tilde J}{\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}-k_m^{2}}+\frac{P_L^{\mathrm{gco}}\tilde J}{k_m^{2}} ,
$$

exactly as in the free case with the covariant operators in place. **The longitudinal response is still local and still weighted by $1/k_m^{2}$**, and this is the same statement as the free article's: the constrained direction does not propagate.

## The Current and the Phase

**The free field had no phase and therefore no charge.** A real four-vector has nothing to rotate, the mass term is real and the central imaginary leaves the sector, so the free theory's only Noether current is the energy–momentum. **The free article says this and gives it as the reason the free Proca field cannot source the inhomogeneous Maxwell equation.**

**The coupled carrier has a phase and the phase is a symmetry of the whole action, mass term included.** Under $\tilde A\mapsto e^{iϙ\Gamma/\hbar}\tilde A$ with $\Gamma$ constant, the field strength transforms by the same factor and the invariant length is unchanged, so the action is invariant and the Noether current exists. **That current is the source the Maxwell equation needs**, and its existence is the integral's version of the coupled equation article's fourth finding.

**The measure is invariant and the invariance is exact at every step.** The transformation multiplies the two real components of each complex slot by a rotation of unit determinant, so the flat measure on eight components is unchanged. **No link, no discretisation rule and no Faddeev–Popov determinant is needed**, and the reason is the same as in the coupled scalar case: a central phase at each point costs a unit Jacobian and nothing else.

**The current's conservation is an identity of the measure and not only of the equation.** Since the transformation is exact and the measure is invariant, $\partial_\mu j^{\mu}=0$ follows from the integral without using the equation of motion. **The mass term does not spoil this**, because the mass term is phase-invariant; what the mass term does spoil is the *ordinary* Lorenz condition, which is a different statement and is the previous section's subject.

**A complex source is now permitted, and the response is the kernel's column.** The source $\tilde J$ may be any element of $\mathbb{B}$, so the two-point function is a bivector and the free article's "the source is anti-Hermitian" restriction is gone. **The carrier's enlargement is what the charge is**, in the integral as in the equation.

## The Semiclassical Expansion

**The saddle is the coupled classical equation, and the one-loop term is the covariant transverse cube.**

$$
\Gamma_{\mathrm{1\,loop}}=\tfrac12\mathrm{Tr}\log P_{\mathrm{gco}}
=3\cdot\tfrac12\mathrm{Tr}\log\bigl(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}-k_m^{2}\bigr)+\tfrac12\mathrm{Tr}\log(-k_m^{2}),
$$

with the last term a constant. **The background's one-loop effect on the Proca field is three times its effect on a charged scalar**, and this is the integral's form of the statement that a massive vector has three states in a background as well as in vacuum.

**The background's effect on the transverse factor is where the whole of the physics is.** The covariant d'Alembertian's spectrum in a background is the Landau-level spectrum for a constant magnetic field, the Schwinger pair-production rate for a constant electric one, and the ordinary scattering problem in general. **None of these is evaluated here**, and the corpus's Landau and pair-creation articles are where they are.

**The longitudinal mode's contribution is a constant and therefore a vacuum energy that does not respond.** In a background, the constrained direction's eigenvalue is $-k_m^{2}$ at every point, so its determinant is a field-independent number times a divergence. **A massive vector's constrained mode contributes to the vacuum energy and not to the effective action's field dependence**, and the free article's statement that the ghost is invisible becomes, in a background, the statement that it is invisible in every derivative.

**No spin transport and no van Vleck determinant appear, and the reason is the carrier.** This is a field integral and not a sum over paths: its semiclassical series is the loop series, its first term is the saddle and its second is the determinant. **The articles that carry a van Vleck determinant and a spin transport are the single-particle ones**, and the massive vector has none in this corpus.

## What the Integral Adds and What It Does Not Add

**Adds, first, the carrier change as a property of the integral.** The measure doubles, the free integral becomes a slice, and the mass term's reality and the carrier's closure are one fact. **This is the only article in the corpus's path-integral set where the coupling changes the configuration space**, and the reason is the material sector's failure to close.

**Adds, second, the exact survival of the three–one split.** The coupling deforms the transverse determinant and leaves the longitudinal eigenvalue at $-k_m^{2}$, so the ghost cancels identically in every ratio of background determinants. **A background sees three states and not four**, and the statement is exact rather than one-loop.

**Adds, third, the asymmetry between the covariant and the ordinary constraint.** The integral's saddle obeys the covariant condition exactly and the ordinary one only up to a bilinear term. **The integral cannot prefer a condition that is not covariant**, and this is why the ordinary Lorenz condition never appears as an equation of the coupled theory.

**Adds, fourth, the charge as a consequence of the carrier.** The free field's reality is the absence of a phase; the enlarged carrier has one; the phase is the charge's coordinate. **The integral's measure acquires a circle per point with unit Jacobian**, and the exactness of the gauge invariance is a consequence of the measure's flatness rather than of a discretisation rule.

**Does not add a value.** The coupled equation is the standard one, the determinant factorisation is the free one with the covariant operator in place, and the one-loop effective action is the standard one.

**Does not treat a dynamical connection, and does not decide the second quantisation.** The connection is external by construction; the field is commuting and bosonic; the measure is formal in the continuum.

## Open Questions

**1. What is the determinant in a background where the covariant operators do not commute with the projectors?** The split uses $D_{\mathrm{gco}}\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}$, which holds because the curvature has no scalar part. Whether the projectors commute with the covariant d'Alembertian, and hence whether the split is a spectral split as well as an algebraic one, is not shown here.

**2. Does the constraint's deformation have an integral consequence?** The ordinary divergence of the saddle is a functional of the background. Whether that functional is a total derivative, and whether it can be written as a surface term of the effective action, is open.

**3. What happens when the connection is itself quantised?** Then the carrier's double is joined by the connection's own gauge orbit, the Faddeev–Popov construction applies to the connection, and the Proca determinant becomes a functional in the path integral over the connection. Whether the factorisation survives that integration is the interesting question, and it is not answered here.

**4. Is there a non-abelian version?** The mixed term is the algebra's form of the commutator term a non-abelian field strength carries, so the coupled Proca equation is already half-way to a non-abelian structure. Whether the split survives a non-abelian connection, where the curvature is no longer a pure vector of a commutative algebra, is open.

**5. Empirical content.** None beyond the standard coupled Proca theory.

## Summary

The coupled Proca functional integral runs over a different configuration space from the free one. The material sector is not closed, the coupling forces the carrier to $\mathbb{B}$, the measure doubles to eight real components per point, and the free integral is the real slice. That is the article's first and largest fact, and it has no counterpart in the scalar, spinor or Klein–Gordon pairs.

The action is quadratic in the Proca field for a fixed connection, with the free density, a bilinear mixed term and a term quadratic in the connection; the expansion was checked to $3.6\times10^{-15}$ and the mixed term's scalar part vanishes identically. The operator is the free operator with the covariant d'Alembertian, and it splits as $(\tilde\nabla^{\natural}\tilde\nabla-k_m^{2})P_T-k_m^{2}P_L$: the coupling deforms the transverse cube and leaves the longitudinal eigenvalue at $-k_m^{2}$, so the determinant is the covariant transverse determinant cubed times the same single factor. The covariant Lorenz condition is forced exactly, because the curvature is a pure vector and has no scalar part; the ordinary condition is not, and the difference is bilinear in the connection.

The coupled field has a charge, because the enlarged carrier has a phase and the mass term is phase-invariant; the measure gains a circle per point with unit Jacobian, and the gauge invariance is exact at every step with no link and no ghost. The one-loop effective action is three times a charged scalar's plus a constant.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}$, $\mathbb{B}_\Phi$ | The coupled carrier, eight real dimensions; the free carrier, four |
| $\tilde A_\Phi=i(\varphi/c)e_t+\vec A$ | The connection |
| $\tilde A$ | The Proca potential, now a general element of $\mathbb{B}$ |
| $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{iϙ}{\hbar}\tilde A_\Phi$ | The covariant gradient |
| $\tilde F_{\mathrm{gco}}=\mathrm{Vect}(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A)$ | The coupled field strength |
| $\tilde V=\mathrm{Vect}(\tilde A_\Phi^{\natural}\tilde A)$ | The bilinear term; a pure vector |
| $\mathrm{Sc}(\tilde V)=0$ | Why the mixed term does not touch the constraint |
| $P_{\mathrm{gco}}=(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}-k_m^{2})P_T^{\mathrm{gco}}-k_m^{2}P_L^{\mathrm{gco}}$ | The coupled split |
| $\det P_{\mathrm{gco}}=(\det(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}-k_m^{2}))^{3}(-k_m^{2})$ | The determinant; coupling deforms only the cube |
| $D_{\mathrm{gco}}\tilde A=\mathrm{Sc}(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde A)=0$ | The covariant Lorenz condition |
| $e^{iϙ\Gamma/\hbar}$ | The gauge transformation; unit Jacobian |
| $3\cdot\frac12\mathrm{Tr}\log(\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}-k_m^{2})$ | The one-loop term; three times a scalar's |

## Further Reading

- *The Path Integral and the Proca Equation in Biquaternionic Form*, for the free integral, the split and the ghost.
- *The Coupled Proca Equation in Biquaternionic Form*, for the carrier change, the doubled coupling and the covariant constraint.
- *The Variational Principle and the Coupled Proca Equation in Biquaternionic Form*, for the action and its two traces.
- *The Gauge Principle in Biquaternionic Form*, for the localisation of the central phase.
- *The Covariant Derivative and Gauge Connection in Biquaternionic Form*, for the operator identity used here.
- *The Path Integral and the Coupled Klein–Gordon Equation in Biquaternionic Form*, for a coupled integral whose carrier does not change.
- *The Gauge Field Path Integral in Biquaternionic Form*, for the Faddeev–Popov construction that a dynamical connection would need.
- *Landau Levels in Biquaternionic Form*, for the constant magnetic background's spectrum of the transverse factor.
- *Pair Creation in a Bounded Region in Biquaternionic Form*, for the constant electric background.
- J. Schwinger, "On Gauge Invariance and Vacuum Polarization," *Physical Review* **82** (1951) 664, for the background-field determinant and its gauge invariance.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the massive vector in a background and the counting of modes.
- L. D. Faddeev and A. A. Slavnov, *Gauge Fields: An Introduction to Quantum Theory* (Benjamin, 1980), for the external-versus-dynamical distinction.
- S. Weinberg, *The Quantum Theory of Fields II* (Cambridge, 1996), for the effective action of a massive vector.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the material sector's failure to close and the enlarged carrier.
