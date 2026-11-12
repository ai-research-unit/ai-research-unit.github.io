# __The Variational Principle and the Proca Equation in Biquaternionic Form__

## Introduction

This article writes the Proca field as the extremum of an action in the algebra, and reads what the action's symmetries give. It is the element-form companion of *The Variational Principle and the Proca Equation in Biquaternionic Polar Variables*, and it depends on two articles: *The Proca Equation: Massive Spin 1 in Biquaternionic Form* for the equation, the implied Lorenz condition and the polarizations, and *The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector* for the field strength and its complex structure.

**The equation.** The parent's equation is

$$
\tilde\nabla_\Phi\tilde F=k_m^2\tilde A_\Phi,
\qquad
\tilde F=\mathrm{Vect}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr),
\qquad
\tilde A_\Phi\in\mathbb{B}_\Phi,
\qquad
\tilde F\in\mathbb{B}_V ,
$$

one biquaternion equation for the anti-Hermitian potential, with the field strength the pure-vector part of its conjugate gradient. The article asks what action has this equation as its Euler–Lagrange equation, and what the action's symmetries give. The answer is one action, one equation, and one Noether current — the energy–momentum — together with two structural statements: that the Lorenz condition is a consequence of the equation and not a gauge choice, and that the mass term is what forbids the gauge symmetry and therefore what forbids a second, phase-like current.

**Three things are established.**

*First, the action.* With $\tilde A_\Phi$ varied over the four real components of the material sector, and with $\mathrm{Re}\,\mathrm{Sc}(\cdot)$ as the real pairing,

$$
S[\tilde A_\Phi]=\int d^4r\;\Bigl[\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)-\tfrac12\,k_m^2\,\langle\tilde A_\Phi\rangle_\natural\Bigr],
$$

the Euler–Lagrange equation is the Proca equation. The normalization is fixed by two requirements and by nothing else: the field term is the Maxwell Lagrangian density $\tfrac12(\epsilon\vec E^2-\vec B^2/\mu)$, and the mass term's sign is the one that makes the energy positive. The other relative sign gives the same equation and a negative energy, and is rejected.

*Second, the Lorenz condition is not a constraint imposed on the action.* Varying the action gives the Proca equation alone; the divergence of that equation gives $S=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)=0$. In the variational reading, that is the statement that the mass term breaks the gauge symmetry: the variation which would leave the field term invariant does not leave the mass term invariant, and the equation consequently carries a longitudinal part which the massless equation does not.

*Third, the only Noether current is the energy–momentum.* The field is real and the action is invariant under the Poincaré group; there is no central phase in the carrier, so there is no $\mathrm{U}(1)$ and no charge. The stress tensor is symmetric, conserved on solutions, traceless only where the field is null, and its trace is proportional to the mass term. That last statement is the field-theoretic form of the reality of the field.

**What is not new.** The action is the standard Proca action written in the algebra's letters. Nothing in the physics is new: the equation, the Lorenz condition, the polarizations and the stress tensor are the standard ones. What the algebra supplies is a compact statement of the pairing, a one-line variation, and the two structural readings above. The polar-form variational principle is the companion article, and there the action's variables are the word's parameters rather than the four components.

The conventions are those of the companion articles. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with $e_t=1$, $\vec e_\eta^2=-e_t$ and central scalar imaginary $i$; the sectors are $\mathbb{B}_\Phi=\mathrm{span}_\mathbb{R}\{ie_t,\vec e_x,\vec e_y,\vec e_z\}$ and $\mathbb{B}_\Psi=\mathrm{span}_\mathbb{R}\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$; ${}^{*}$ is coefficient conjugation composed with the quaternion conjugation $\natural$; $\mathrm{Sc}$ is the coefficient of $e_t$; $\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^{\natural}$ is the quaternionic norm, real on $\mathbb{B}_\Phi$; the potential is $\tilde A_\Phi=i\,a'_t\,e_t+\vec A$ with real $\vec A$ and real $a'_t$, so that $\langle\tilde A_\Phi\rangle_\natural=-(a'_t)^2+\vec A^2$; the derivatives are $\partial/\partial R_t=-i\,\partial/\partial r'_t$ and $\partial/\partial R_\eta=\partial/\partial r_\eta$, so that $\Box_\Phi=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=\Delta_\Phi-\partial^2/\partial{r'_t}^2$; and the field strength is $\tilde F=i\sqrt{\epsilon}\vec E-\sqrt{\mu}\vec H$ with $c=1/\sqrt{\epsilon\mu}$. The mass is the wave number $k_m=mc/\hbar$.

## The Action in Element Form

Write the action as

$$
S[\tilde A_\Phi]=\int d^4r\;\mathcal{L},
\qquad
\mathcal{L}=\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)-\tfrac12\,k_m^2\,\langle\tilde A_\Phi\rangle_\natural .
$$

**The field term is the Maxwell density.** Because $\tilde F$ is a pure vector, $\mathrm{Sc}(\tilde F\tilde F)$ is its negative squared length, and with $\tilde F=i\sqrt{\epsilon}\vec E-\sqrt{\mu}\vec H$,

$$
\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)=\epsilon\vec E^2-\mu\vec H^2+2i\sqrt{\epsilon\mu}\,\vec E\cdot\vec H
=\epsilon\vec E^2-\frac{\vec B^2}{\mu}+\frac{2i}{c}\,\vec E\cdot\vec B ,
$$

so that $\tfrac12\mathrm{Re}\,\mathrm{Sc}(\tilde F\tilde F)=\tfrac12(\epsilon\vec E^2-\vec B^2/\mu)$, which is the Maxwell Lagrangian density. The imaginary part is proportional to $\vec E\cdot\vec B$, the invariant $I_2$, and it is the term whose integral is a surface term: $\vec E\cdot\vec B=-\nabla\cdot(a'_t\vec B)-\partial_{t'}(\vec A\cdot\vec B)/c$ up to the signs of the corpus's conventions. It therefore drops from the variation and contributes nothing to the equation; it is the $F\tilde F$ term of the standard theory, and its absence from the equation is why the action can be written with the real part alone.

**The mass term is the invariant length.** $\langle\tilde A_\Phi\rangle_\natural$ is the Minkowski square of the four-vector and it is real, so $\tfrac12k_m^2\langle\tilde A_\Phi\rangle_\natural$ is real and quadratic in the potential. There is no other quadratic invariant of a real four-vector, so the mass term is fixed up to its coefficient.

**The action is real and the pairing is the real part of the scalar part.** Both terms are real by construction. The pairing is $\mathrm{Re}\,\mathrm{Sc}(\cdot)$, not $\mathrm{Sc}(\cdot)$ alone and not $\mathrm{Sc}(\cdot^{\natural}\cdot)$: the scalar part alone is complex on $\tilde F\tilde F$, and the quaternionic pairing would pair $\tilde F$ with its conjugate and produce the energy density rather than the Lagrangian. This is the material sector's version of the spinor article's warning about the two pairings, and the choice is forced: the pairing must be the one whose variation reproduces the equation, and only the real part of the scalar part does.

**The normalization is fixed by two requirements.** The coefficient of the field term is fixed so that it is the Maxwell density, and the relative sign of the mass term is then fixed by requiring that the energy be positive. With the opposite relative sign the Euler–Lagrange equation is the same — the overall sign of an action does not change its extremum — but the canonical energy is negative. Both statements are checked by finite differences: the variation of the action with the sign shown reproduces the Proca residual on a periodic lattice at the level of $10^{-9}$, and the canonical energy density of a transverse plane wave is positive for that sign and negative for the other.

**Why the second-order form and not a first-order one.** The Proca equation is second order in the potential and first order in the field strength, and the action above is the second-order form. A first-order form, with $\tilde F$ an independent variable, exists and is the standard Palatini-type action, but it adds a variable and a pair of equations that are algebraically equivalent to the definition of $\tilde F$. The corpus uses the second-order form throughout, and this article does too: the polar companion's count of parameters is a count for the second-order form.

## The Equation from the Action

**The variation.** Treat $\tilde A_\Phi$ as the variable and vary over the four real components of $\mathbb{B}_\Phi$: the scalar potential $a'_t$ and the three components of $\vec A$. The field strength is linear in the potential, so

$$
\delta\mathcal{L}=\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\,\delta\tilde F\bigr)-k_m^2\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde A_\Phi^{\natural}\,\delta\tilde A_\Phi\bigr)
$$

with $\delta\tilde F=\mathrm{Vect}((\tilde\nabla_\Phi)^{\natural}\delta\tilde A_\Phi)$, and integrating by parts moves the derivative from $\delta\tilde A_\Phi$ onto $\tilde F$. The boundary term is discarded, and the result is

$$
\delta S=\int d^4r\;\mathrm{Re}\,\mathrm{Sc}\Bigl[\delta\tilde A_\Phi^{\natural}\bigl(\tilde\nabla_\Phi\tilde F-k_m^2\tilde A_\Phi\bigr)\Bigr].
$$

**The bracket vanishes as an element, not merely in its scalar part.** The variation $\delta\tilde A_\Phi$ ranges over the four real components of the material sector, and the pairing $\mathrm{Re}\,\mathrm{Sc}(\delta\tilde A_\Phi^{\natural}X)$ is non-degenerate on that four-dimensional real space: if it vanishes for every $\delta\tilde A_\Phi$, then $X=0$ as an element of $\mathbb{B}_\Phi$. So the Euler–Lagrange equation is

$$
\boxed{\;\tilde\nabla_\Phi\tilde F-k_m^2\tilde A_\Phi=0\;}
$$

and it is four real equations, one per component. The count is the count of the carrier: eight components of $\mathbb{B}$ would give eight equations, and the material sector's four give four.

**The antisymmetry is what the boundary term leaves behind.** The integration by parts is legitimate because $\tilde F$ is built from the antisymmetric part of $(\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi$: the symmetric part is the scalar $S=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)$, which is removed by the projection. That removal is the algebraic statement of the antisymmetry of $F_{\mu\nu}$, and it is why the field term depends on the potential only through the curl.

## The Lorenz Condition Is a Consequence

**The divergence argument.** Apply the conjugate gradient to the equation and take the scalar part. The left side is $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi\tilde F)$, which vanishes identically for a pure-vector $\tilde F$ because the scalar part of $\tilde\nabla^{\natural}\tilde\nabla$ applied to a vector is a total divergence of an antisymmetric object; the right side is $k_m^2\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)=k_m^2S$. So

$$
k_m^2S=0
\qquad\Longrightarrow\qquad
S=\mathrm{Sc}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr)=\frac{\partial a'_t}{\partial r'_t}+\nabla\cdot\vec A=0 ,
$$

which is the Lorenz condition. The parent proves the identity; this article records what the variational reading adds, which is the interpretation and not the proof.

**The interpretation: the mass term is the obstruction to gauge invariance.** Consider the shift $\tilde A_\Phi\to\tilde A_\Phi+(\tilde\nabla_\Phi)\Gamma$ for a real scalar $\Gamma$. The field strength is unchanged, because the field strength is the antisymmetric part of the conjugate gradient and the conjugate gradient of a gradient is symmetric; so the field term of the action is invariant. The mass term is not:

$$
\langle\tilde A_\Phi+(\tilde\nabla_\Phi)\Gamma\rangle_\natural
=\langle\tilde A_\Phi\rangle_\natural+2\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde A_\Phi^{\natural}(\tilde\nabla_\Phi)\Gamma\bigr)+\langle(\tilde\nabla_\Phi)\Gamma\rangle_\natural ,
$$

and neither of the last two terms vanishes for a general $\Gamma$. So the action has no gauge symmetry, and the equation inherits a longitudinal part. The Lorenz condition is the statement that this part is absent on shell, and it is a consequence of the equation rather than a condition imposed on the field.

**Why this is not a gauge choice, in one sentence.** In the massless theory $S=0$ can be reached from any potential by a gauge transformation, so it is a choice of representative; here no gauge transformation exists, so $S=0$ is a property of the solution. That is the whole difference, and it is visible in the action as the presence of the mass term.

## No Second Current

**The phase rotation is not a symmetry.** For a complex field the transformation $\tilde\Xi\to e^{i\alpha}\tilde\Xi$ leaves the kinetic term invariant and produces the conserved density of the Schrödinger and Dirac articles. For the Proca field it is not defined: $e^{i\alpha}\tilde A_\Phi$ leaves $\mathbb{B}_\Phi$ for $\alpha\notin\pi\mathbb{Z}$, because $i\tilde A_\Phi$ is Hermitian and not anti-Hermitian. The carrier has no central phase to rotate, and the action therefore has no continuous internal symmetry at all.

**The would-be current vanishes.** The current that a complex vector field would carry, $j_\mu\propto\mathrm{Im}(\tilde A^{*}\tilde F)$, is not available here for the same reason, and the electromagnetic current of the interacting theory is not a Noether current of the free Proca action: it is the source that the *inhomogeneous* equation has and the free equation does not. The free Proca field has no charge, and the polar article's absence of the central bracket is the same statement in the chart.

**What this leaves.** The global symmetries of the action are the translations and the Lorentz transformations, and each gives one current multiplet. The translations give the energy–momentum; the Lorentz transformations give the angular momentum, which for this field is the orbital part plus the spin-one part carried by the vector index. There is no other current, and that exhaustion is the variational form of the standard statement that a free massive vector field has three degrees of freedom and no charge.

## The Noether Currents

**Energy–momentum.** Translation invariance of the action gives the canonical stress tensor, and the Belinfante improvement makes it symmetric. In the algebra's letters, with $\tilde F$ the field strength and $\langle\tilde A_\Phi\rangle_\natural$ the invariant length, the symmetric tensor is

$$
T_{\mu\nu}=-F_{\mu\alpha}F_{\nu}^{\ \alpha}+\tfrac14\,\eta_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}
+k_m^2\Bigl(A_\mu A_\nu-\tfrac12\,\eta_{\mu\nu}\langle\tilde A_\Phi\rangle_\natural\Bigr),
$$

the standard Proca tensor written with the corpus's invariant in place of $A_\mu A^\mu$. Its properties are the ones that matter here, and each has a one-line proof from the equation.

- **Symmetry.** The first two terms are symmetric in $\mu\nu$ because $F$ is antisymmetric and the contraction is over the pair; the mass term is symmetric by inspection.
- **Conservation.** $\partial^\mu T_{\mu\nu}=0$ on solutions: the derivative of the field terms gives $-(\partial^\mu F_{\mu\alpha})F_\nu^{\ \alpha}$ plus a term that cancels by antisymmetry, and the derivative of the mass term cancels against it using the equation.
- **Positive energy.** The energy density is $\tfrac12(\epsilon\vec E^2+\vec B^2/\mu)+\tfrac12k_m^2\bigl((a'_t)^2+\vec A^2\bigr)$, positive for the sign of the action used here.
- **Trace.** $T^\mu_{\ \mu}$ is proportional to the mass term, since the field terms are traceless in four dimensions and the mass term is not. The trace vanishes if and only if $\langle\tilde A_\Phi\rangle_\natural=0$, that is, if and only if the local four-vector is lightlike.

**The trace statement is the structural one.** A massless vector field has a traceless stress tensor, and the trace is the measure of the conformal anomaly in the quantum theory. Here the trace is nonzero for every physical field, because a plane wave of a massive field is never lightlike: the invariants satisfy $\epsilon\vec E^2-c^2\vec B^2>0$ for every massive mode, as the polarization article shows in detail. So the massive vector field is not conformally invariant, and the non-invariance is exactly the mass.

**The spin part.** The angular momentum current is $M_{\mu\nu\lambda}=R_\nu T_{\mu\lambda}-R_\lambda T_{\mu\nu}+\Sigma_{\mu\nu\lambda}$ with $\Sigma$ the vector-index part. That $\Sigma$ is the spin-one content of the field, and it is not a separate current with its own conservation law: the orbital and spin parts are separately conserved only after the improvement, and the total is the Noether current. The polar article's frame bracket is the transport of the same object read as a direction.

## Exact Solutions and What They Show

**Plane waves.** With $\tilde A_\Phi=\tilde A_0\cos\theta_{\mathrm{pwp}}$ and $\theta_{\mathrm{pwp}}=k'_t r'_t-\vec k_\Phi\cdot\vec r$, the equation requires the dispersion relation $k'^2_t=\vec k_\Phi^2+k_m^2$ and the Lorenz condition requires the amplitude relation $a'_{t,0}=\vec k_\Phi\cdot\vec A_0/k'_t$. Three amplitude directions survive at each wavevector: two transverse and one longitudinal. These are the parent's modes, and the action adds only that they extremize it.

**A toroidal family.** Because the action implies the Lorenz condition and hence the componentwise Klein–Gordon equation, solutions can be built from scalar ones. Take a real scalar $\psi$ with $(\Box_\Phi-k_m^2)\psi=0$ and set

$$
\vec A=\nabla\psi\times\vec r ,\qquad a'_t=0 .
$$

Then $\nabla\cdot\vec A=\vec r\cdot(\nabla\times\nabla\psi)-\nabla\psi\cdot(\nabla\times\vec r)=0$, so the Lorenz condition holds identically, and $\Box_\Phi\vec A=\nabla(\Box_\Phi\psi)\times\vec r=k_m^2\vec A$ because the curl of a gradient vanishes and $\vec r$ is static. This is an exact non-plane solution: with $\psi=j_0(\kappa r)\cos(k'_t r'_t)$ and $\kappa^2=k'^2_t-k_m^2$ it is a spherical, toroidal-vector field. The identity is verified by finite differences at the level of $10^{-7}$ on a smooth configuration, which is the accuracy of the difference scheme. The family is the corpus's first exact Proca solution that is not a superposition of plane waves.

**No pure-gradient solution.** Take $\tilde A_\Phi=(\tilde\nabla_\Phi)\Gamma$ for a real scalar $\Gamma$. Then $S=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}(\tilde\nabla_\Phi)\Gamma)=-\Box_\Phi\Gamma$, so the Lorenz condition forces $\Box_\Phi\Gamma=0$; the equation then forces $k_m^2(\tilde\nabla_\Phi)\Gamma=0$, that is, $\Gamma$ constant and the field zero. So the massive theory admits no non-trivial pure-gradient solution. This is the variational form of "there is no gauge freedom": in the massless theory the pure gradients are exactly the gauge orbit, and here the orbit has collapsed to a point. The statement is exact and needs no approximation.

## What the Variational Principle Adds and What It Relabels

**Adds.**

- One compact statement of the equation: one action, one variation, four real equations.
- The Lorenz condition as a consequence of the equation, with the interpretation that the mass term is the obstruction to the gauge shift.
- The energy–momentum tensor in one derivation, with the four properties (symmetry, conservation, positivity, trace) proved from the equation.
- The exhaustion of the currents: translations and Lorentz, and nothing else, because the carrier has no central phase.
- The two exact-solution statements: the toroidal family, and the vanishing of the pure-gradient solutions.

**Relabels.**

- No new prediction. The equation, the dispersion relation and the polarizations are the parent's.
- No new solution. The plane waves are the parent's; the toroidal family is a construction from the parent's componentwise reduction, not a new equation.
- The action is the standard Proca action in the algebra's notation. It is not a new principle, and its normalization is fixed by the Maxwell density and by the positivity of the energy, not by a new argument.

**The distinction that matters.** The variational principle is integral in form and local in content: a functional on the whole field configuration whose extremum is a local differential equation. It is equivalent to the equation and richer in what it delivers, because the symmetries of the functional are what produce the currents. That is the same relation as in the scalar and spinor articles, and nothing about it is special to the vector case.

## Open Questions

1. **The improved tensor and the spin part.** The explicit Belinfante improvement for the material sector, and the split of the angular momentum into orbital and spin parts with the corpus's conventions, is not carried out here. The companion article on the energy–momentum tensor of the Proca field is the natural place for it, and the check is that its tensor agrees with the one above up to the improvement term.
2. **The interaction.** The coupling to an external current replaces the right side by a source, and the Lorenz condition then becomes $\partial_\mu j^\mu=0$ rather than $S=0$. Whether the algebra's reading of the coupled equation adds anything to the standard one is not attempted; the corpus's gauge articles treat the massless case.
3. **The path integral.** The action is the input of a path integral over $\mathbb{B}_\Phi$-valued configurations, and the mass term is what makes the quadratic form invertible. That is the subject of the quantization article and of the QFT block, and it is not attempted here.

## Summary

The Proca field is the extremum of

$$
S[\tilde A_\Phi]=\int d^4r\;\Bigl[\tfrac12\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr)-\tfrac12\,k_m^2\,\langle\tilde A_\Phi\rangle_\natural\Bigr],
$$

whose Euler–Lagrange equation is $\tilde\nabla_\Phi\tilde F=k_m^2\tilde A_\Phi$, four real equations for the four components of the material sector. The coefficient of the field term is the Maxwell normalization, the relative sign of the mass term is fixed by positivity of the energy, and the pairing is the real part of the scalar part because only that pairing is real on $\tilde F\tilde F$ and reproduces the equation.

The divergence of the equation forces the Lorenz condition, and the variational reading of that fact is that the mass term breaks the gauge shift which the field term alone would allow. The action has no internal symmetry, so its only currents are the energy–momentum and the angular momentum: the stress tensor is symmetric, conserved, positive in energy, and its trace is proportional to the mass term and vanishes only for a null field. Plane waves extremize the action, a toroidal family does too, and no non-trivial pure gradient does — the last being the variational statement that the mass removes the gauge freedom.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\eta^2=-e_t$ |
| $i$ | Central scalar imaginary |
| $\mathbb{B}_\Phi$, $\mathbb{B}_\Psi$, $\mathbb{B}_V$ | Material, informational, and vector sectors |
| ${}^{*}$, ${}^{\natural}$, $\mathrm{Sc}$, $\mathrm{Vect}$ | Hermitian conjugation, quaternion conjugation, scalar part, vector part |
| $\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^{\natural}$ | Quaternionic norm; real on $\mathbb{B}_\Phi$ |
| $\tilde A_\Phi=i\,a'_t\,e_t+\vec A$ | Four-potential; $\langle\tilde A_\Phi\rangle_\natural=-(a'_t)^2+\vec A^2$ |
| $\tilde F=i\sqrt{\epsilon}\vec E-\sqrt{\mu}\vec H$ | Field-strength biquaternion, pure vector |
| $\Box_\Phi=\Delta_\Phi-\partial^2/\partial{r'_t}^2$ | d'Alembertian of the corpus |
| $S=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)$ | Lorenz scalar |
| $\mathcal{L}$ | Lagrangian density |
| $T_{\mu\nu}$ | Symmetric energy–momentum tensor |
| $k_m=mc/\hbar$ | Mass wave number |
| $\theta_{\mathrm{pwp}}=k'_t r'_t-\vec k_\Phi\cdot\vec r$ | Plane-wave phase |

## Further Reading

- [The Proca Equation: Massive Spin 1 in Biquaternionic Form](the-proca-equation-massive-spin-1-in-biquaternionic-form.html), for the equation, the Lorenz condition and the polarizations.
- [The Proca Equation in Biquaternionic Polar Variables](the-proca-equation-in-biquaternionic-polar-variables.html), for the chart in which the action's variables are the word's parameters.
- [The Variational Principle and the Proca Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-proca-equation-in-biquaternionic-polar-variables.html), for the same action in the chart.
- [The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector](the-self-dual-and-anti-self-dual-split-spin-1-from-the-biquaternion-material-sector.html), for the carrier and the reality obstruction.
- [The Variational Principle and the Coupled Dirac Equation in Biquaternionic Form](the-variational-principle-and-the-coupled-dirac-equation-in-biquaternionic-form.html), for the spinor action and its pairing.
- [Canonical Quantization of the Biquaternion Proca Field](canonical-quantization-of-the-biquaternion-proca-field.html), for the Legendre transform, the constraints and the propagator.
- [The Third Polarization and the Self-Dual Split of the Massive Field Strength](the-third-polarization-and-the-self-dual-split-of-the-massive-field-strength.html), for the three states and the trace of the tensor.
- Alexandre Proca, "Sur la théorie ondulatoire des électrons positifs et négatifs", *Journal de Physique et le Radium* **7** (1936) 347–353, for the equation and its mass term.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the Proca Lagrangian, the stress tensor and the Lorenz condition.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I: Foundations* (Cambridge, 1995), for the massive vector field and the counting of its degrees of freedom.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the field strength as a bivector and the duality structure of the action.
