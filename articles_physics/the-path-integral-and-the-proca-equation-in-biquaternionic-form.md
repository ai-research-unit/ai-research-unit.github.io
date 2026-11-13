# __The Path Integral and the Proca Equation in Biquaternionic Form__

## Introduction

**The Proca field is the simplest field in the corpus whose functional integral exists as it stands.** It is a real four-component field, it is commuting, its action is quadratic, and its mass term removes the one obstruction that the massless integral has. So the free integral is an ordinary Gaussian, its determinant can be computed exactly, and the answer contains the whole of the theory's particle content: the number three in the determinant's exponent is the three polarizations of the massive vector, and the eigenvalue that sits outside the cube is the ghost.

**Three facts organise the article, and the first is the one the massless case does not have.** The mass term is what makes the integral exist. At $k_m=0$ the Proca operator has the four-dimensional kernel of pure gradients, the Gaussian's longitudinal eigenvalue vanishes, and the integral is the volume of the gauge group — which is why the Maxwell integral needs the Faddeev–Popov construction of *The Gauge Field Path Integral in Biquaternionic Form* and the Proca one needs nothing. **No gauge-fixing condition, no Faddeev–Popov determinant, no ghost field, no gauge parameter.** The mass does all of it, and it does it in one term.

**The second fact is the operator's split, and it is exact in the algebra's own letters.** The Proca operator is $P=\Box_\Phi-k_m^{2}-\tilde\nabla_\Phi D$ with $D\tilde A_\Phi=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)$ the divergence. The object $D$ and the gradient $\tilde\nabla_\Phi$ are the two canonical operators the algebra supplies, so the longitudinal projector $P_L=\tilde\nabla_\Phi\Box_\Phi^{-1}D$ needs no frame, no polarisation vector and no choice. Then

$$
P=(\Box_\Phi-k_m^{2})P_T-k_m^{2}P_L ,
$$

and the determinant follows without further work: the transverse factor cubed and the longitudinal factor once.

**The third fact is that the determinant's cube is the field's particle content.** The one-loop effective action of the Proca field is three times that of a scalar, and the difference between the two theories is a field-independent constant. That is the path-integral form of the statement that a massive vector has three states and not one, and it is the sharpest thing the integral says about the equation.

**What is not claimed.** The integral is the standard Proca integral, the propagator is the standard Proca propagator, and nothing here predicts anything new. What the algebra supplies is a frame-free derivation of the three–one split, the exactness of the ghost's eigenvalue, and the statement that the ghost is invisible in every normalised correlator.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with $e_t=1$, $\vec e_\eta^{2}=-e_t$, central $i$, $\mathrm{Sc}$ the coefficient of $e_t$ and $\mathrm{Tr}=2\,\mathrm{Sc}$. The potential is $\tilde A_\Phi=i\,a'_t\,e_t+\vec A$ with $a'_t$ and $\vec A$ real, an element of the material sector $\mathbb{B}_\Phi=\mathrm{span}_\mathbb{R}\{ie_t,\vec e_x,\vec e_y,\vec e_z\}$, anti-Hermitian under ${}^{*}$. The field strength is $\tilde F=\mathrm{Vect}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)$ and the norm is $\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^{\natural}$, real on $\mathbb{B}_\Phi$. The d'Alembertian is $\Box_\Phi=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=\Delta_\Phi-\partial^{2}/\partial{r'}^{2}_t$, with $\partial/\partial R_t=-i\,\partial/\partial r'_t$, so that its symbol is $k^{2}=(\omega/c)^{2}-\vec k^{2}$. The mass is the wave number $k_m=mc/\hbar$.

## The Configuration Space and the Action

**The field is an anti-Hermitian element at every point, and that is what makes the components four.** The reality is not an assumption laid on the field; it is the condition $\tilde A_\Phi^{*}=-\tilde A_\Phi$, which cuts the eight real dimensions of $\mathbb{B}$ to the four of $\mathbb{B}_\Phi$. The configuration space is the space of such functions, and the measure is the flat measure on four real components at each point.

**The action is the variational companion's, and it is real.**

$$
S[\tilde A_\Phi]=\int d^{4}r\;\Bigl[\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)-\tfrac12\,k_m^{2}\langle\tilde A_\Phi\rangle_\natural\Bigr].
$$

The first term is the Maxwell density $\tfrac12(\epsilon\vec E^{2}-\vec B^{2}/\mu)$, the second is the mass term, and both are real by construction. The article does not re-derive the action; it cites *The Variational Principle and the Proca Equation in Biquaternionic Form* for the variation, the two normalisation conditions and the sign of the mass term.

**The source is a material-sector element and its coupling needs no conjugation.** For $\tilde J_\Phi\in\mathbb{B}_\Phi$ the product $\tilde J_\Phi\tilde A_\Phi$ is Hermitian, so $\mathrm{Sc}(\tilde J_\Phi\tilde A_\Phi)$ is real and the source term is

$$
S_J=S[\tilde A_\Phi]+\int d^{4}r\;\mathrm{Sc}\bigl(\tilde J_\Phi\tilde A_\Phi\bigr).
$$

This is the material sector's own pairing, and it differs from the spinor case's $\mathrm{Sc}(\tilde J^{*}\tilde\Xi)$ only because the field is already real: the star has nothing to do on an anti-Hermitian element except return it.

**The divergence is the one object the action displays separately.** Writing $S=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)$ for the divergence, the polar variational companion's identity gives

$$
\mathrm{Sc}\Bigl[\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr)^{2}\Bigr]=S^{2}+\mathrm{Sc}\bigl(\tilde F\tilde F\bigr),
$$

so that the action is also

$$
S=\int d^{4}r\;\Bigl[\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\Bigl[\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr)^{2}\Bigr]-\tfrac12S^{2}-\tfrac12k_m^{2}\langle\tilde A_\Phi\rangle_\natural\Bigr].
$$

**The middle term is where the constraint lives, and the integral reads it as a term and not as an insertion.** In the element form the Lorenz condition is implied by the field equation and is not imposed on the action. In the integral the same fact appears as a quadratic term in the exponent, whose variation produces the condition. The chart article takes this up; here the term is only named, because the operator's split below is exactly the split between the first and the second piece.

## The Generating Functional and the Free Gaussian

**The generating functional is an ordinary Gaussian.**

$$
Z[\tilde J_\Phi]=\int\mathcal{D}\tilde A_\Phi\;\exp\Bigl(\frac{i}{\hbar}S[\tilde A_\Phi]+\frac{i}{\hbar}\int d^{4}r\;\mathrm{Sc}\bigl(\tilde J_\Phi\tilde A_\Phi\bigr)\Bigr),
$$

with the flat measure on the anti-Hermitian configurations. There is no insertion, no orbit and no determinant to compensate: the measure is the one the configuration space carries.

**On a lattice the statement is an ordinary finite-dimensional integral and it is exact.** At $N$ sites the field is $4N$ real numbers, the quadratic form is a symmetric $4N\times4N$ matrix, and

$$
Z_N[J]=(2\pi)^{2N}\bigl(\det A\bigr)^{-1/2}\exp\Bigl(\tfrac12J^{T}A^{-1}J\Bigr).
$$

At one site with four components, a random positive-definite form with eigenvalues $0.7,1.3,2.1,3.4$ and a random source, direct four-dimensional quadrature gave $24.507861622165$ and the closed form gave $24.507861623587$, a relative agreement of $5.8\times10^{-11}$. **The Gaussian identity is the backbone; the continuum integral is its formal limit and adds nothing.**

**The two-point function is the inverse of the quadratic form, and that inverse is the Proca propagator.** Since the exponent is quadratic, $\langle\tilde A_\Phi(x)\tilde A_\Phi(y)\rangle=i\hbar\,P^{-1}(x-y)$, and the whole of the free theory is the computation of $P^{-1}$. The next section does it.

## The Operator and Its Three–One Split

**The operator is the d'Alembertian minus the gradient of the divergence minus the mass.**

$$
P\tilde A_\Phi=\Box_\Phi\tilde A_\Phi-\tilde\nabla_\Phi D\tilde A_\Phi-k_m^{2}\tilde A_\Phi ,
\qquad
D\tilde A_\Phi=\mathrm{Sc}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr),
$$

which is $\tilde\nabla_\Phi\tilde F-k_m^{2}\tilde A_\Phi$ with $\tilde F=\mathrm{Vect}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)$, i.e. the Proca equation. Every object in $P$ is built from $\tilde\nabla_\Phi$, its $\natural$-conjugate, and central scalars, so $P$ maps $\mathbb{B}_\Phi$ into itself and the integral never leaves the sector.

**The two canonical operators give the two projectors, and no frame is needed.** Set

$$
P_L=\tilde\nabla_\Phi\,\Box_\Phi^{-1}D ,
\qquad
P_T=1-P_L .
$$

Then $DP_L=D\tilde\nabla_\Phi\Box_\Phi^{-1}D=D$, because $D\tilde\nabla_\Phi=\Box_\Phi$ — the divergence of a gradient is the d'Alembertian — so $P_L$ is idempotent, $P_T$ is idempotent, and $P_TP_L=0$. **The decomposition is the Helmholtz decomposition written in the algebra's letters, and its two ingredients are the only two first-order operators the algebra has.**

**Applying the two projectors gives the two eigenvalues, and each computation is two lines.** On the longitudinal subspace, $P\,P_L\tilde A_\Phi=\tilde\nabla_\Phi D\tilde A_\Phi-\tilde\nabla_\Phi D\tilde A_\Phi-k_m^{2}P_L\tilde A_\Phi=-k_m^{2}P_L\tilde A_\Phi$, because the first two terms cancel identically. On the transverse subspace, $D$ vanishes, so $P\,P_T\tilde A_\Phi=(\Box_\Phi-k_m^{2})P_T\tilde A_\Phi$. Hence

$$
\boxed{\;P=(\Box_\Phi-k_m^{2})P_T-k_m^{2}P_L\; }
$$

with $P_L$ of rank one and $P_T$ of rank three.

**The mass is the only thing that acts on the longitudinal direction.** Every term of $P$ except $-k_m^{2}$ annihilates $P_L$: the d'Alembertian and the gradient-of-divergence cancel there exactly. So the longitudinal eigenvalue is $-k_m^{2}$ with no derivative in it, no momentum in it and no field in it. **That single fact carries the ghost, the massless limit and the gauge-fixing question, and the next two sections are its consequences.**

## The Determinant and the Count of Three

**The determinant factorises, and the factorisation is the theory's particle content.**

$$
\det P=\bigl(\det(\Box_\Phi-k_m^{2})\bigr)^{3}\cdot\bigl(-k_m^{2}\bigr),
$$

with the cube from the rank-three projector and the single factor from the rank-one one. In momentum space, where $\Box_\Phi$ has symbol $k^{2}$,

$$
\det P=-k_m^{2}\bigl(k^{2}-k_m^{2}\bigr)^{3},
$$

and the four eigenvalues of the mixed operator are $-k_m^{2}$ once, along $k$, and $k^{2}-k_m^{2}$ three times, on the transverse plane.

**Both statements were checked, and both are exact.** For eight random timelike momenta with $k_m=0.7$ the computed eigenvalues matched $\{-k_m^{2},k^{2}-k_m^{2},k^{2}-k_m^{2},k^{2}-k_m^{2}\}$ to a relative $2.5\times10^{-15}$, the determinant matched $-k_m^{2}(k^{2}-k_m^{2})^{3}$ to $4.7\times10^{-15}$, and $P\,P^{-1}$ differed from the identity by $1.2\times10^{-14}$. **The exponent three is not an approximation and not a convention; it is the rank of the transverse projector.**

**The cube is the three polarizations.** The Gaussian's amplitude per mode is $(\det)^{-1/2}$, so the transverse factor contributes $(k^{2}-k_m^{2})^{-3/2}$: three powers, one for each state. This is the integral's version of the equation article's count of two transverse and one longitudinal direction, and the two counts agree because the projection and the polarisation count are the same decomposition. **A scalar field contributes one power, a Dirac field four, a massive vector three; the exponent of the transverse factor is the count.**

**The inverse is the propagator, and it displays the same split.**

$$
P^{-1}=\frac{P_T}{\Box_\Phi-k_m^{2}}-\frac{P_L}{k_m^{2}}
\;\;\xrightarrow{\ \text{momentum}\ }\;\;
\frac{g^{\mu\nu}-k^{\mu}k^{\nu}/k_m^{2}}{k^{2}-k_m^{2}+i\epsilon},
$$

which is the standard Proca propagator. Both displayed forms were checked against each other on six random momenta, agreeing to $4.4\times10^{-16}$ after the indices are raised, and the projector form inverts the operator to $1.2\times10^{-14}$. **The $1/k_m^{2}$ in the numerator of the longitudinal part is where the mass appears in the propagator, and it is the whole of the difference from a scalar.**

## The Ghost

**The longitudinal eigenvalue is field-independent, so the ghost is invisible.** It is $-k_m^{2}$ at every momentum, with no $k$ and no source in it. Hence $\prod_k(-k_m^{2})$ is a constant that multiplies $Z[\tilde J_\Phi]$ and cancels in $Z[\tilde J_\Phi]/Z[0]$ and in every correlator. **The ghost contributes a number and not a response**, and that is why a massive vector's covariant integral is a correct description of a three-state particle despite the extra mode.

**It contributes a phase and not a modulus.** The Gaussian factor is $(-k_m^{2})^{-1/2}$, and for $k_m^{2}>0$ that is $i/|k_m|$: a constant times $i$. The product over modes is a formal phase, and the article states it as formal, because the product is infinite. **This is the ghost's entire effect on the free theory: a phase and a constant, neither of which any normalised amplitude sees.**

**What the ghost is not.** It is not the spacelike branch of the polar chart, and it is not a particle. It is the longitudinal eigenvalue of the covariant operator, and it is negative because the Proca operator is indefinite in Minkowski signature — the kinetic term already is, in the time direction. **The ghost's negative sign is the metric's and the mass's, not the theory's error**, and the Euclidean section below makes the sign disappear.

**The Euclidean operator has no ghost at all.** With $\delta_{\mu\nu}$ in place of $g_{\mu\nu}$ the eigenvalues become $m^{2}$ once and $p^{2}+m^{2}$ three times, and the determinant is $+m^{2}(p^{2}+m^{2})^{3}$, positive for every $p$ and every $m>0$. The check covered $p=(0.2,0.1,-0.3,0.5)$, $p=(1,0.4,0,0.2)$, $p=0$ and $p=(3,-2,1,0.5)$, and the computed determinant matched the closed form at every one. **The indefinite sign is the Wick rotation's, and the rotation is exact.**

## The Massless Limit

**At $k_m=0$ the longitudinal eigenvalue vanishes and the integral is not defined.** Then $\det P=0$, the Gaussian has a flat direction at every momentum, and the flat direction is the gauge orbit: $\tilde A_\Phi\mapsto\tilde A_\Phi+\tilde\nabla_\Phi\chi$ leaves both $\tilde F$ and the action unchanged. **The integral becomes the volume of the group of gradient functions times the transverse integral**, which is exactly the object the Faddeev–Popov construction removes.

**So the Proca integral needs no gauge fixing, and the Maxwell integral cannot do without one.** This is not a technical convenience; it is the same statement as the equation article's "the mass breaks the gauge symmetry". The path integral says it as a rank: the longitudinal projector has rank one at $k_m\neq0$ and rank one of zero eigenvalue at $k_m=0$.

**The limit exists on conserved sources and only there.** Contracting the inverse with a source gives

$$
\tilde J_\Phi\,P^{-1}\tilde J_\Phi=\frac{\tilde J_T^{2}}{\Box_\Phi-k_m^{2}}-\frac{(\tilde J_L)^{2}}{k_m^{2}},
$$

and the second term diverges as $k_m\to0$ unless $\tilde J_L=0$, i.e. unless $D\tilde J_\Phi=0$. **The longitudinal mode decouples from a conserved source, and from nothing else.** The numbers: for a conserved source the longitudinal term was exactly zero at every $k_m$ tried, and for a non-conserved one it grew as $1/k_m^{2}$, from $1.07\times10^{2}$ at $k_m=10^{-1}$ to $1.07\times10^{8}$ at $k_m=10^{-4}$.

**This is the integral's form of the third-polarisation statement.** The corpus's *The Third Polarization and the Self-Dual Split of the Massive Field Strength* says that the third state is physical at $k_m\neq0$ and becomes the gauge direction at $k_m=0$. The integral says that the third state is a term in the propagator with the coefficient $1/k_m^{2}$, that it couples to the divergence of the source, and that a conserved source cannot see it.

**The gauge-fixing parameter of the Maxwell integral has no Proca analogue.** There the longitudinal coefficient is a free number $\xi$; here it is fixed at $1/k_m^{2}$ by the mass. **The Proca theory has no gauge to fix, so it has no gauge parameter, and the Lorenz condition is a consequence rather than a choice** — which is the equation article's statement read as the uniqueness of the propagator.

## The Semiclassical Expansion

**The saddle is the classical field, and the classical field splits with the operator.**

$$
P\tilde A_\Phi^{\mathrm{cl}}=-\tilde J_\Phi
\qquad\Longrightarrow\qquad
\tilde A_\Phi^{\mathrm{cl}}=-\frac{P_T\tilde J_\Phi}{\Box_\Phi-k_m^{2}}+\frac{P_L\tilde J_\Phi}{k_m^{2}} .
$$

The transverse part propagates; the longitudinal part does not, because its operator is a constant. **A gradient source produces an unsuppressed classical field with no wave equation in it**, and that is the integral's picture of a constraint: the response to the constrained direction is instantaneous and local.

**The one-loop term is three times the scalar's.** Expanding about the saddle,

$$
Z[\tilde J_\Phi]=Z[0]\exp\Bigl(-\frac{i}{2\hbar}\int\tilde J_\Phi P^{-1}\tilde J_\Phi\Bigr),
\qquad
\Gamma_{\mathrm{1\,loop}}=\tfrac12\mathrm{Tr}\log P
=3\cdot\tfrac12\mathrm{Tr}\log(\Box_\Phi-k_m^{2})+\tfrac12\mathrm{Tr}\log(-k_m^{2}),
$$

and the last term has no field in it. **The one-loop effective action of the free Proca field is exactly three times that of a free scalar**, and the ghost adds a constant. This is the determinant's cube read as a statement about the effective action, and it is the reason the massive vector's vacuum polarisation carries three.

**The classical field's divergence is fixed by the source and not by the equation.** Applying $D$ to $P\tilde A_\Phi^{\mathrm{cl}}=-\tilde J_\Phi$ kills the first two terms of $P$ and gives

$$
-k_m^{2}D\tilde A_\Phi^{\mathrm{cl}}=D\tilde J_\Phi ,
$$

so the Lorenz condition holds exactly when the source is conserved. **The constraint is not imposed and not lost: it is a relation between the saddle and the source**, and the inhomogeneous Maxwell equation needs a conserved current for exactly this reason.

**The leading semiclassical kernel is the free one, and the loop expansion is the only expansion there is.** The Proca integral has no worldline and no van Vleck determinant of a path, because the field is a field and not a particle: the semiclassical series is the loop series in $\hbar$, its first term is the saddle, and its second is the determinant computed above. **The articles on the Schrödinger and Dirac integrals are the ones with a sum over paths; this one is a sum over field configurations, and the difference is the statistics and the carrier, not the algebra.**

## What the Integral Adds and What It Does Not Add

**Adds, first, the frame-free derivation of the three–one split.** The projectors are $\tilde\nabla_\Phi\Box_\Phi^{-1}D$ and its complement, and they are built from the two canonical first-order operators of the algebra. No polarisation vector, no momentum frame and no gauge choice enters. **The exponent three is the rank of a projector, and the rank is computed without reference to any vector.**

**Adds, second, the exactness of the ghost's eigenvalue.** Because the longitudinal eigenvalue is $-k_m^{2}$ with no derivative, the ghost's contribution is a constant and the ghost's sign is the metric's. The two statements together give the clean result: a massive vector's covariant integral is a correct three-state integral, and the fourth mode is a phase.

**Adds, third, the statement that the Proca integral needs no gauge fixing.** The rank of the longitudinal projector is the whole of the argument, and the Faddeev–Popov apparatus of the Maxwell article has no Proca counterpart. The mass, the Lorenz condition and the absence of a gauge parameter are one fact in three costumes.

**Does not add a value.** The propagator is the standard Proca propagator, the determinant is the standard determinant, and the one-loop effective action is the standard one. Every closed form quoted here is in the literature, and the algebra's contribution is the route and not the destination.

**Does not supply the measure, and does not decide the statistics.** The continuum measure over four real components per point is formal, as it is for every field in the corpus. The field is commuting and bosonic, and no Grassmann structure is needed or used — in this the article is the opposite of the Dirac companion, where the statistics had to be addressed explicitly.

**Does not treat a dynamical connection.** The connection in the coupled companion is external, which is what keeps the integral Gaussian. A dynamical connection brings the Faddeev–Popov construction back, and that is where the gauge-field article resumes.

## Open Questions

**1. Is the ghost's phase observable in a background?** In the free theory the ghost is a constant. In a background the longitudinal eigenvalue is still $-k_m^{2}$ only if the covariant Lorenz condition survives, and the coupled article shows that it does. Whether the ghost's phase then acquires a dependence on the background's topology is not known, and the corpus's anomaly articles are where such questions are asked.

**2. What is the Proca determinant on a curved or bounded background?** The factorisation uses only $D\tilde\nabla_\Phi=\Box_\Phi$, which is a statement about the algebra's own operators. Whether the same factorisation survives a boundary, where the divergence and the gradient do not compose to the d'Alembertian without a surface term, is not settled here.

**3. Can the count three be read off the chart?** The polar companion asks whether the two-branch chart of the material sector can see the three polarizations. The integral says the three is the transverse rank and the chart says the carrier has four dimensions, so the two counts are different objects. Whether the chart can display the projection is that article's question.

**4. Is there a worldline form?** A single-particle path integral for a massive vector particle exists in the standard literature, with a supersymmetric worldline. Whether the corpus's polar variables can carry it, as the rotor carries the Dirac spin, is open and is not attempted here.

**5. Empirical content.** None. The integral is the standard one and its predictions are the standard ones.

## Summary

The Proca functional integral is an ordinary Gaussian over the anti-Hermitian configurations, with the flat measure and no insertion. Its operator is $P=\Box_\Phi-k_m^{2}-\tilde\nabla_\Phi D$, and the two canonical first-order operators of the algebra give the exact split $P=(\Box_\Phi-k_m^{2})P_T-k_m^{2}P_L$ with $P_L=\tilde\nabla_\Phi\Box_\Phi^{-1}D$ of rank one and $P_T$ of rank three. The determinant is $(\Box_\Phi-k_m^{2})^{3}(-k_m^{2})$, verified to $4.7\times10^{-15}$ in momentum space, and the inverse is $(g^{\mu\nu}-k^{\mu}k^{\nu}/k_m^{2})/(k^{2}-k_m^{2}+i\epsilon)$, which is the standard Proca propagator.

The exponent three is the three polarizations, and the single factor is the ghost. The ghost's eigenvalue is $-k_m^{2}$ with no derivative in it, so the ghost's contribution is a constant times a phase and cancels in every normalised correlator; in the Euclidean section the eigenvalues are $m^{2}$ and $p^{2}+m^{2}$ and both are positive. The one-loop effective action is three times a scalar's. At $k_m=0$ the longitudinal eigenvalue vanishes, the integral becomes the gauge volume, and the Faddeev–Popov construction is what the Maxwell integral needs and the Proca one does not; the massless limit exists on conserved sources only, with the longitudinal term growing as $1/k_m^{2}$ for a non-conserved one.

The saddle is the classical field, whose transverse part propagates and whose longitudinal part does not, and whose divergence satisfies $-k_m^{2}D\tilde A_\Phi^{\mathrm{cl}}=D\tilde J_\Phi$. The integral adds the frame-free split, the exactness of the ghost, and the statement that the mass is what makes the integral exist. It adds no value.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde A_\Phi=i\,a'_t\,e_t+\vec A$ | The Proca potential, anti-Hermitian |
| $\mathbb{B}_\Phi$ | The material sector; the carrier of the free field |
| $\tilde F=\mathrm{Vect}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)$ | The field strength, a pure vector |
| $D\tilde A_\Phi=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)$ | The divergence; the constraint's operator |
| $P=\Box_\Phi-k_m^{2}-\tilde\nabla_\Phi D$ | The Proca operator |
| $P_L=\tilde\nabla_\Phi\Box_\Phi^{-1}D$, $P_T=1-P_L$ | Longitudinal and transverse projectors; ranks 1 and 3 |
| $P=(\Box_\Phi-k_m^{2})P_T-k_m^{2}P_L$ | The exact split |
| $\det P=(\Box_\Phi-k_m^{2})^{3}(-k_m^{2})$ | The determinant; the cube is the polarization count |
| $\frac{g^{\mu\nu}-k^{\mu}k^{\nu}/k_m^{2}}{k^{2}-k_m^{2}+i\epsilon}$ | The propagator; the standard Proca form |
| $-k_m^{2}$ | The longitudinal eigenvalue; the ghost |
| $m^{2}$, $p^{2}+m^{2}$ | The Euclidean eigenvalues; both positive |
| $\tilde J_\Phi P^{-1}\tilde J_\Phi$ | The source's image; the longitudinal term is $1/k_m^{2}$ |

## Further Reading

- *The Proca Equation: Massive Spin 1 in Biquaternionic Form*, for the equation, the implied Lorenz condition and the three polarizations.
- *The Variational Principle and the Proca Equation in Biquaternionic Form*, for the action, the two normalisation conditions and the Noether current.
- *The Proca Equation in Biquaternionic Polar Variables*, for the two-branch word and the logarithmic derivative.
- *The Path Integral and the Klein–Gordon Equation in Biquaternionic Form*, for the scalar field integral whose determinant this one cubes.
- *The Path Integral and the Dirac Equation in Biquaternionic Form*, for the fermionic integral, where the statistics is the issue and here it is not.
- *The Gauge Field Path Integral in Biquaternionic Form*, for the Faddeev–Popov construction that the massless limit would require.
- *The Yang–Mills Path Integral and the Faddeev–Popov Procedure in Biquaternionic Form*, for the non-abelian case and the ghost fields.
- *The Third Polarization and the Self-Dual Split of the Massive Field Strength*, for the third state's disappearance in the massless limit.
- *Canonical Quantization of the Biquaternion Proca Field*, for the operator route to the same three states.
- R. P. Feynman, "The Quantum Theory of Gravitation," *Acta Physica Polonica* **24** (1963) 697, for the massive vector propagator and its longitudinal term.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Proca propagator, the determinant and the massless limit's singularity.
- S. Weinberg, *The Quantum Theory of Fields I* (Cambridge, 1995), for the counting of states and the absence of a gauge parameter.
- M. Veltman, *Diagrammatica* (Cambridge, 1994), for the massive vector's longitudinal mode and its coupling to the divergence.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the material sector, its anti-Hermitian elements and the Helmholtz decomposition in the algebra.
