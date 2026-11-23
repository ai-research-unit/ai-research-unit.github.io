# __The Lagrangian and the Electromagnetic Field__

## Introduction

*Maxwell's Equations in the Biquaternionic Formulation* writes the free field as one equation for one biquaternion,

$$
\tilde\nabla_\Phi\tilde F=-Z\,\tilde J_\Phi ,
\qquad
\tilde F=c\,\mathrm{Vect}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr),
\qquad
\tilde J_\Phi=ic\rho\,e_t+\vec J ,
$$

with $\tilde A_\Phi\in\mathbb{B}_\Phi$ the potential, $\tilde F$ the field strength and $c=1/\sqrt{\epsilon\mu}$ the speed of light in the medium. The present article asks the question the family asks of every parent: which action has this equation as its Euler–Lagrange equation, what does its variation give, and what do its symmetries give?

Three results, and one of them is a warning.

*First, the action is one term.* $S=\int\mathrm{d}^{4}r\,\tfrac12\mathrm{Re}\,\mathrm{Sc}(\tilde F\tilde F)$, with the field strength inside it, so that the potential enters only through $\tilde F$. That single placement is what makes the gauge orbit visible from the action rather than from the equation.

*Second, the variation gives both halves of Maxwell.* Varying $\tilde A_\Phi$ gives $\tilde\nabla_\Phi\tilde F=0$ in the free case and $-Z\tilde J_\Phi$ once a matter action is added; the scalar part of the same equation is Gauss's law, and it is a constraint on the initial data and not an evolution equation.

*Third, the field's own symmetries give the stress and not a charge.* The free field has no phase symmetry, so there is no conserved charge intrinsic to it; what the action's translation invariance gives is the energy–momentum, whose temporal component is $\tfrac12(\epsilon\vec E^{2}+\vec B^{2}/\mu)$ and is positive. The charge appears only when a source is coupled, and its sign is the source's.

What this article does not do, stated in the first section because it is the first thing a reader may assume. It does not quantise the field. It does not introduce a Fock space, creation or annihilation operators, a path integral over histories, or a coupling to charged matter beyond naming the current that the coupled articles derive. This family's treatment of the electromagnetic field stops at the one-particle action and its classical consequences — the corpus's separate quantum-fields category quantises the free field, and does not derive the quantisation from this action — and the route beyond it is named in *The Lagrangian and the Second Quantisation: From the Action to the Commutator*, which is a statement of what is missing and not a derivation of what is present.

## Conventions

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_{\imath}^{2}=-e_t$; $\mathbb{B}_\Phi$ is the anti-Hermitian sector, where the potential lives; the gradient is $\tilde\nabla_\Phi=e_t\,\partial/\partial R_t+\sum_{\imath\in\{x,y,z\}}\vec e_{\imath}\,\partial/\partial r_{\imath}$ with $R_t=ir'_t$.

The medium enters through two constants. The permittivity is $\epsilon$ and the permeability $\mu$, both positive, and $c=1/\sqrt{\epsilon\mu}$ is the speed of light in the medium, so the vacuum is the case $\epsilon=\epsilon_0$, $\mu=\mu_0$. The field strength carries the normalisation

$$
\tilde F=c\,\mathrm{Vect}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr)
=i\vec E-c\vec B ,
$$

with $\vec H=\vec B/\mu$; the imaginary part is the electric field and the real part is the magnetic one, the electric term carrying the factor $i$ because it carries the time index. The source is $\tilde J_\Phi=ic\rho\,e_t+\vec J$, whose scalar part is the charge density and whose vector part is the current density. The pairing is $\mathrm{Re}\,\mathrm{Sc}(\cdot\,\cdot)$, the measure is $\mathrm{d}^{4}r$, and the symbol $\mathrm{Vect}$ is the pure-vector part.

## The Action in Element Form

**One term, and the potential appears only through the field strength.**

$$
S[\tilde A_\Phi]=\int\mathrm{d}^{4}r\;\tfrac{\epsilon}{2}\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr).
$$

Its sign and its value. With $\tilde F=i\vec E-c\vec B$ and the quaternion rule $\vec u\vec u=-\lvert\vec u\rvert^{2}$ for a real vector, $\mathrm{Sc}(\tilde F\tilde F)=-\vec E^{2}-c^{2}\vec B^{2}=-2W/\epsilon$, the cross terms being vectors and dying in the scalar part when $\vec E$ and $\vec B$ are orthogonal, and cancelling in general because $\tilde F\tilde F$ is the square of one element. So

$$
\tfrac{\epsilon}{2}\,\mathrm{Re}\,\mathrm{Sc}(\tilde F\tilde F)=-\tfrac{\epsilon}{2}\bigl(\vec E^{2}+c^{2}\vec B^{2}\bigr)=-\tfrac12\bigl(\epsilon\vec E^{2}+\vec B^{2}/\mu\bigr),
$$

which is the standard Lagrangian up to one overall sign. The sign is the corpus's and is not chosen here: the Proca companion fixes it once, by requiring that the same field term, with the mass term added, give $\tilde\nabla_\Phi\tilde F=4\pi^{2}\nu_m^{2}\tilde A$ with the sign printed there. Flipping the sign of the field term without flipping the mass term would change the Proca equation's sign, and the corpus does not do that.

Three properties, each one line.

*It is real.* $\tilde F$ is a pure vector with complex coefficients, and $\mathrm{Sc}(\tilde F\tilde F)$ is real because it is a symmetric bilinear of one element evaluated in the scalar part, where the central $i$ enters squared. Equivalently $\tilde F\tilde F$ is invariant under both conjugations, since $\tilde F^{\natural}=\tilde F$ for a vector and $\tilde F^{*}$ conjugates the coefficients' $i$ twice in the product.

*It is gauge invariant.* The shift $\tilde A_\Phi\mapsto\tilde A_\Phi+\tilde\nabla_\Phi\Lambda$ leaves $\tilde F$ unchanged, because $\mathrm{Vect}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi\Lambda\bigr)=0$: the conjugate gradient of a gradient is symmetric, and a symmetric element has no vector part.

*It carries no mass.* A term $\tfrac12m^{2}\mathrm{Re}\,\mathrm{Sc}(\tilde A_\Phi\tilde A_\Phi)$ would break the invariance above and is the Proca article's subject; this article has no such term, and that absence is the difference between the two parents.

## The Variation

Varying the potential, and one integration by parts. The variation of the field strength is

$$
\delta\tilde F=c\,\mathrm{Vect}\bigl((\tilde\nabla_\Phi)^{\natural}\delta\tilde A_\Phi\bigr),
$$

because the normalisation and the projection are linear. Hence

$$
\delta S=\epsilon\int\mathrm{d}^{4}r\;\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\,\delta\tilde F\bigr)
=\frac{1}{Z}\int\mathrm{d}^{4}r\;\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\,\mathrm{Vect}\bigl((\tilde\nabla_\Phi)^{\natural}\delta\tilde A_\Phi\bigr)\bigr),
$$

The projection can be dropped. $\tilde F$ is a pure vector and the scalar part of a vector times a scalar is zero, so replacing $\mathrm{Vect}(X)$ by $X$ changes nothing inside the pairing. One integration by parts then moves the derivative onto $\tilde F$,

$$
\delta S=-\frac{1}{Z}\int\mathrm{d}^{4}r\;\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde\nabla_\Phi\tilde F\,\delta\tilde A_\Phi\bigr)
+\oint\mathrm{d}\Sigma\;\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\,\delta\tilde A_\Phi\bigr),
$$

with the surface term killed by holding the potential fixed on the boundary.

**The equation is recovered, not assumed.** Stationarity for every $\delta\tilde A_\Phi$ forces

$$
\tilde\nabla_\Phi\tilde F=0 ,
$$

the parent's homogeneous equation. Adding a matter action whose variation with respect to $\tilde A_\Phi$ is $-Z\,\tilde J_\Phi$ gives the inhomogeneous one. The constant $Z$ is therefore not a choice of this article: it is the normalisation that makes the source the current, and the coupled articles verify it by deriving the current from the matter action.

What the variation does not produce. It does not produce a condition on $\tilde A_\Phi$ alone, because the action depends on the potential only through a gauge-invariant combination; the longitudinal part is invisible to it, and that invisibility is the next section but two.

## The Constraints the Action Imposes

**Gauss's law is the constraint, and the gauge orbit is the redundancy.** The two are different objects and the article keeps them apart.

The constraint. Take the scalar part of the field equation. The left side's scalar part is $\mathrm{Sc}(\tilde\nabla_\Phi\tilde F)$, and for a pure-vector $\tilde F$ it equals a divergence,

$$
\mathrm{Sc}\bigl(\tilde\nabla_\Phi\tilde F\bigr)=\vec\nabla_\Phi\cdot\vec D ,
\qquad
\vec D=\epsilon\vec E ,
$$

up to the factor $i$ that the time slot carries. So the scalar part of $\tilde\nabla_\Phi\tilde F=0$ is $\vec\nabla_\Phi\cdot\vec D=0$: Gauss's law without sources, a condition on the initial data at every time and not an equation that determines a rate. With a source it reads $\vec\nabla_\Phi\cdot\vec D=\rho$, and the charge density is then not free either: taking the divergence of Ampère's law and substituting gives $\partial\rho/\partial t'+\vec\nabla_\Phi\cdot\vec J=0$, the integrability condition the parent states.

The gauge orbit. The action is invariant under $\tilde A_\Phi\mapsto\tilde A_\Phi+\tilde\nabla_\Phi\Lambda$ for any real scalar $\Lambda$. Two potentials in the same orbit are one field configuration, and the action does not select a representative. Choosing one is a gauge choice; the orbit itself is a property of the description.

Which of the two this article looks at. The orbit, because it is exact and it is what makes the count of degrees of freedom come out right: four components of $\tilde A_\Phi$, one constraint, one orbit direction, two transverse polarisations. The constraint is stated because the count needs it, and it is not solved.

## The Structural Consequence: The Potential's Longitudinal Part Is Not a Degree of Freedom

The article owns one claim, and it is a count. The field strength depends on the potential only through the antisymmetric part of its conjugate gradient, and the antisymmetric part is blind to a gradient shift. Hence the potential's longitudinal part never enters the action, never enters the equation, and is not a degree of freedom.

The hand check, in one line. Take $\tilde A_\Phi=\tilde\nabla_\Phi\Lambda$ alone. Then

$$
(\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi=(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi\Lambda=\Box_\Phi\Lambda ,
$$

which is central, so its vector part vanishes, so $\tilde F=0$ and the action vanishes identically. A pure-gradient potential is not a field configuration with zero energy; it is the same configuration as no potential at all.

**The count, and where it comes from.** Four real components; one relation from the constraint; one direction in the kernel of the map from potential to field strength; two remaining. The two are the transverse polarisations, and the massless field has no third. The Proca companion's count is the same count with the kernel removed by the mass term, and the difference between the two articles is exactly that removal.

What the claim forbids. It forbids writing an action with a term in $\tilde A_\Phi$ alone: such a term would see the longitudinal part and would break the invariance. That is why the Proca mass term is a different theory and not a deformation of this one.

## The Noether Currents and the Sign of the Charge

**The free field has a stress and no charge.** Translation invariance gives the energy–momentum tensor, and its temporal component is

$$
T_{00}=\tfrac12\bigl(\epsilon\vec E^{2}+\vec B^{2}/\mu\bigr)>0 ,
$$

with the Poynting vector $\vec S=\vec E\times\vec H$ as the mixed components. The sign is positive and it is the sign that makes the energy bounded below; it is a statement about the stress and not about the sign of the Lagrangian, and the two signs are independent.

Why there is no charge. A central phase rotation $\tilde A_\Phi\mapsto e^{i\theta}\tilde A_\Phi$ is not a symmetry: the potential is real on the material sector, and multiplying it by $i$ moves it out of $\mathbb{B}_\Phi$. The Noether procedure therefore returns nothing, and the free field carries no conserved charge. This is the same verdict the Proca article records, and it is the reason neither article has a section called *the charge's sign*.

Where the charge and its sign come from. From the source. Once a charged matter action is added, the total action is invariant under the local phase only if the connection shifts, and the current is what the connection multiplies. Its sign is then the sign of the matter field's charge, fixed once in the coupled article that derives it, and the field equation's sign is fixed by the same constant. The free field has no sign to fix, and saying so is more useful than manufacturing one.

The stress's conservation. $\partial_{\imath} T_{\imath\jmath}=0$ on solutions is the divergence of the field equation contracted with $\tilde F$, the standard identity; it holds for the free field and it is not an extra assumption.

## What the Principle Adds and What It Relabels

What it adds. Two things, and both are structural rather than predictive. It exhibits the field strength as the only thing the action sees, so that the gauge orbit is a property of the action and not of a chosen equation. And it makes the constraint and the orbit visibly different: one comes from the scalar part of the variation, the other from the kernel of the map from potential to field strength.

What it relabels. The Maxwell equations themselves. The action adds no solution, no prediction and no constant that the parent does not have. The normalisation $Z$ is the parent's; the sign of the field term is the Proca companion's; the stress is the standard one. A reader who wants the physics will find all of it in the parent.

**What it does not reach.** The quantised theory. Nothing in this article creates a photon, counts modes in a Fock space, or sums histories. This family does not do that anywhere, and this article's honesty consists in not pretending that a classical action is a quantum theory. The route is named in the bridge article and it is a route, not a result.

## Summary

The Maxwell field is the extremum of one term, $S=\int\tfrac{\epsilon}{2}\mathrm{Re}\,\mathrm{Sc}(\tilde F\tilde F)$, and its variation recovers $\tilde\nabla_\Phi\tilde F=-Z\tilde J_\Phi$ with the constraint $\vec\nabla_\Phi\cdot\vec D=\rho$ as the scalar part. The potential enters only through the field strength, so the longitudinal part is a gauge orbit and not a degree of freedom, and the count is two transverse polarisations. The free field's symmetries give a positive stress and no charge; the charge appears with the source and its sign is the source's. Nothing here is quantised, and the article says so in its first section rather than its last.

$$
S[\tilde A_\Phi]=\int\mathrm{d}^{4}r\;\tfrac{\epsilon}{2}\,\mathrm{Re}\,\mathrm{Sc}\bigl(\tilde F\tilde F\bigr),
\qquad
\tilde F=c\,\mathrm{Vect}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr).
$$

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_{\imath}^{2}=-e_t$ |
| $\mathbb{B}_\Phi$ | Anti-Hermitian sector, where the potential lives |
| $^{*},\ ^{\natural}$ | Hermitian and quaternion conjugation |
| $\mathrm{Sc},\ \mathrm{Vect}$ | Scalar part; pure-vector part |
| $\epsilon,\ \mu$ | Permittivity and permeability of the medium |
| $c=1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $\tilde A_\Phi=\sum_{\imath} A_{\imath} e_{\imath}$ | Four-potential, anti-Hermitian |
| $\tilde F=i\vec E-c\vec B$ | Field strength, pure vector |
| $\tilde J_\Phi=ic\rho\,e_t+\vec J$ | Four-current |
| $\vec D=\epsilon\vec E,\ \vec B=\mu\vec H$ | Displacement and induction |
| $S,\ \mathcal{L}$ | Action and Lagrangian density |
| $T_{\imath\jmath}$ | Energy–momentum tensor |
| $\Lambda$ | Gauge parameter, a real scalar |

## Further Reading

- *Maxwell's Equations in the Biquaternionic Formulation*, the parent, for the field strength, the source and the normalisation $Z$.
- *The Lagrangian and the Proca Equation*, for the same field term with a mass and for the sign convention this article keeps.
- *The Lagrangian and the Coupled Klein–Gordon Equation*, for the derivation of the current that sources the field.
- *The Lagrangian and the Electromagnetic Field in Polar Variables* is not written; the chart of a massless field is the gauge orbit's own parameterisation and is the gap this family leaves open.
- Landau and Lifshitz, *The Classical Theory of Fields*, for the stress tensor and the sign conventions of the Lagrangian.
- Julian Schwinger, *Classical Electrodynamics*, for the source normalisation and the constraint's role in the initial-value problem.
- *The Lagrangian and the Second Quantisation: From the Action to the Commutator*, for what a quantised version of this action would require and for the statement that the corpus does not supply it.
