# __The Lagrangian and the Central Scalar Field__

## Introduction

This article writes the real central scalar field as the extremum of an action, and uses that action to state precisely what the centre does and does not carry. It is the action-first companion of *The Central Scalar Field: Classical Dynamics in the Biquaternion Centre*, which treats the field's dynamics and its Green functions; this article asks what functional produces the central wave equation, and what the answer says about the scalar's place in the algebra.

The equation. The parent's equation is

$$
\bigl(\Box_\Phi-4\pi^{2}\nu_m^2\bigr)\tilde\Xi=-g\rho\,e_t ,
\qquad
\tilde\Xi\in\mathbb{B}_\Phi ,
\qquad
\Box_\Phi=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural},
$$

one central scalar operator acting on an element whose four components are all governed by the same operator. The article asks what action has this equation as its stationarity condition.

Three things are established.

*First, the action.* With $\xi$ the single real function and $\rho$ a prescribed source,

$$
S[\xi]=\int d^4r\;\Bigl[-\tfrac12\sum_{\imath}\frac{\partial\xi}{\partial R_{\imath}}\frac{\partial\xi}{\partial R_{\imath}}-\tfrac124\pi^{2}\nu_m^2\xi^2+g\rho\,\xi\Bigr],
$$

the Euler–Lagrange equation is the parent's equation. The action is the standard real scalar action, and the corpus's contribution is the statement that the operator in it is the biquaternion norm of the gradient.

*Second, there is no constraint and that is the structural point.* A single real component with a second-order equation has one degree of freedom and no Gauss law. Nothing is removed from the action by a constraint, and nothing needs to be: the count is one and the equation is one.

*Third, the centre forbids self-interaction of the algebra's own kind.* A term $\xi^4$ is permitted and is the standard one; a term built from the algebra's structure constants is not, because the central operator has no structure constants to build it from. The absence is what the corpus calls the scalar sector's lack of a native ladder, and the action displays it as the absence of a cubic or quartic invariant of the element.

What is not new. The action is the standard real scalar action. What the corpus contributes is the identification of $\Box_\Phi$ with the norm of the gradient, the componentwise reading of the central operator, and the statement of the boundary this section draws.

## Conventions

The conventions are restated here so that every sign below is checkable from this page. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_{\imath}^{2}=-e_t$; the material sector is $\mathbb{B}_\Phi$; the centre is the span of $e_t$ and $ie_t$, so a central element commutes with everything.

The field. $\xi$ is a real function of the coordinates and $\tilde\Xi=\xi e_t$ is the element it defines; a general biquaternion-valued field has four components, and the central case is the one in which all four obey the same equation.

The operator. $\tilde\nabla_\Phi=e_t\partial/\partial r'_t+\sum_j\vec e_j\partial/\partial R_j$ and $\Box_\Phi=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}$, which is central because it is a sum of squares with real coefficients.

The source and the coupling. $\rho$ is a prescribed real density, $g$ a real coupling with the dimension that makes $g\rho\xi$ an energy density, and $\nu_m$ the mass. The sign of the source term is fixed by the requirement that like sources attract, which the parent derives from the static limit.

The sign convention. The kinetic term enters with $-\tfrac12$ under the corpus's sign rule, so that the time derivative's contribution is positive and the energy is bounded below.

## The Action in Element Form

The action, in the algebra's letters. The scalar case allows the action to be written as an element,

$$
S[\tilde\Xi]=\int d^4r\;\Bigl[-\tfrac12\,\mathrm{Sc}\bigl((\tilde\nabla_\Phi\tilde\Xi)^{\natural}\tilde\nabla_\Phi\tilde\Xi\bigr)-\tfrac124\pi^{2}\nu_m^2\,\mathrm{Sc}\bigl(\tilde\Xi^{\natural}\tilde\Xi\bigr)+g\rho\,\mathrm{Sc}(\tilde\Xi)\Bigr],
$$

and for $\tilde\Xi=\xi e_t$ each term reduces to the scalar expression above. The element form is not an alternative notation: it is the statement that the action is a central element and can be read as a single number in the centre.

Why the reduction is exact and not approximate. Because $\Box_\Phi$ is central, it acts on $\tilde\Xi$ componentwise, and the four components do not mix. For $\tilde\Xi=\xi e_t$ there is one nonzero component, so the element action and the scalar action are the same functional restricted to a line. A noncentral operator would mix the components and the reduction would fail; that is the technical content of "central".

The mass term. $-\tfrac12\nu_m^2\mathrm{Sc}(\tilde\Xi^{\natural}\tilde\Xi)=-\tfrac12\nu_m^2\xi^2$ is the standard mass term, and its sign is what makes the dispersion relation $k^2=4\pi^{2}\nu_m^2$ rather than a tachyon. In the algebra it is the Minkowski square of the element, and it is real and non-positive with the corpus's sign rule.

The source term. $g\rho\,\mathrm{Sc}(\tilde\Xi)=g\rho\,\xi$ couples the field to a prescribed density and nothing else; it is linear, so it shifts the minimum without changing the quadratic structure. The sign convention that makes like sources attract is the one in which a positive $\rho$ produces a negative $\xi$, which is what the parent's static solution shows.

What the action does not contain. No cubic or quartic term in $\xi$ built from the algebra, because there is no invariant of the algebra of that degree in a central element; no derivative coupling, because there is no connection in this sector; and no spin term, because a central scalar carries no vector index. Each absence is a statement about the algebra and not an omission.

**The pairing. The pairing is the scalar part of the element product, and in the centre it is ordinary multiplication.** $\mathrm{Sc}(\tilde\Xi^{\natural}\tilde\Xi)=\xi^2$ and $\mathrm{Sc}((\tilde\nabla_\Phi\tilde\Xi)^{\natural}\tilde\nabla_\Phi\tilde\Xi)=\sum_{\imath}(\partial_{\imath}\xi)^2$, both real. There is no imaginary part to cancel and no conjugation to choose, because a central element is its own conjugate up to sign in the imaginary centre.

Why the scalar case is the degenerate case of the family's reality question. Every other article in the family has to argue that a pairing is real and that the argument is not circular. Here the question does not arise: the field is real and the pairing is multiplication. The contrast is informative, because it isolates what the family's other reality arguments are doing.

The type of the coefficient. Three real coefficients: a mass squared, a coupling, and nothing else. $\nu_m^2$ has dimension of mass squared; $g$ has the dimension that makes $g\rho\xi$ an energy density; $\rho$ is data. There is no dimensionless coupling, because there is no interaction term for it to multiply.

Why the absence of a dimensionless coupling is a statement about the algebra. A $\xi^4$ term would have one, and the corpus permits it as a standard scalar self-coupling; but a term built from the algebra's structure constants would need two vector indices per factor, and a central element has none. The interaction the algebra could build is therefore absent, and the scalar sector is free unless a coupling is added by hand.

The selection rule. The selection rule is Poincaré invariance and reality, and they leave the three terms written. The action is the most general one of dimension at most four for a single real scalar: a kinetic term, a mass term, a source and optionally a quartic. Nothing is selected away, and nothing is added beyond the standard list.

Three things the reality of the action does not supply:

- *No spin.* The field is central and has no vector index; the spin-zero articles record that this is why the scalar lies outside the state module.
- *No $\mathrm{U}(1)$ charge.* A real field has no phase to rotate; the complex scalar's charge is the interacting-scalar article's.
- *No interaction of the algebra's own kind.* A quartic term can be written, and it is not the algebra's.

## The Variation: One Component, One Equation

The variation. With $\delta\xi$ vanishing at the boundary,

$$
\delta S=\int d^4r\;\delta\xi\Bigl[\tilde\nabla_\Phi^{\natural}\tilde\nabla_\Phi\xi-4\pi^{2}\nu_m^2\xi+g\rho\Bigr]=0 ,
$$

where the integration by parts is legitimate because $\tilde\nabla_\Phi$ is real and the boundary term vanishes. Stationarity for every $\delta\xi$ gives

$$
\boxed{\;\bigl(\Box_\Phi-4\pi^{2}\nu_m^2\bigr)\xi=-g\rho\;}
$$

which is the parent's equation with $\tilde\Xi=\xi e_t$.

Why the operator's order matters. $\Box_\Phi$ is second order in time, so the equation needs the field and its first time derivative as initial data, exactly as any classical wave field. A first-order action would need one piece of data and would describe a different theory; the second-order form is what the parent uses and what the corpus's canonical quantisation of the scalar field assumes.

The variational derivative's sign, checked against the static limit. For a static source the equation reduces to $\nabla^2\xi-4\pi^{2}\nu_m^2\xi=-g\rho$, whose solution for a point source is a Yukawa profile $-g\,e^{-\nu_mr}/(4\pi r)$, negative for positive $g\rho$ and decaying at $\nu_m^{-1}$. The sign is the experimental fact that like sources attract, and it fixes the source term's sign in the action. The check is not decoration: the opposite sign would give a repulsive and exponentially growing solution.

The Green function, and what it is not. The action's kernel is $\Box_\Phi-4\pi^{2}\nu_m^2$, so the propagator is its inverse, which the parent computes. The variation gives the equation; the inverse gives the response; the two are different objects and the article keeps them apart.

## The Constraints the Action Imposes: There Are None

The count. **One real function, one second-order equation, one degree of freedom. No local symmetry, no Gauss law, no constraint surface to restrict the variation.** The action is unconstrained and that is the whole of its constraint structure.

Why that is worth a section. Every other article in the family has a constraint: the Proca field has its Lorenz condition, the connections have their Gauss laws, the sigma model has its unit-norm surface. The scalar has none, and the absence is what makes it the reference case against which the others' constraints can be read.

What the absence implies for the canonical treatment. The scalar's canonical momentum is $\pi=\partial\mathcal{L}/\partial\dot\xi=\dot\xi$, and the relation is invertible, so there is no primary constraint and no Dirac bracket. The canonical quantisation of the scalar field is therefore the simplest in the corpus, and its simplicity is a consequence of the action's unconstrained form.

## The Structural Consequence: The Centre Acts Componentwise

The statement. **$\Box_\Phi$ is central, so it acts on each of the four components of $\tilde\Xi$ separately and identically.** A field with all four components active is four decoupled copies of the scalar, not one interacting system.

Why this is a boundary and not a defect. The family's other sectors need a noncentral operator to couple components: the Proca equation's field strength, the Dirac equation's $\gamma$-insertion, the connection's commutator. The scalar's operator has none, so the scalar cannot mix the algebra's directions. That is precisely why the scalar is said to lie outside the state module and why the corpus's ladder structure is absent in this sector.

The one thing the centre does carry. It carries the mass and the wave operator, and both are exact. The scalar's classical dynamics, its Green functions and its Yukawa profile are all correct in the algebra's letters. The boundary is at the interaction, not at the propagation.

What the structure predicts. That a real scalar's action needs no constraint, that its degree-of-freedom count is one, and that its quantisation is the simplest in the family. All three are true and all three follow from centrality.

## The Noether Currents: Energy–Momentum and Nothing Else

Energy–momentum. Translation invariance gives

$$
T_{\imath\jmath}=\frac{\partial\xi}{\partial R_{\imath}}\frac{\partial\xi}{\partial R_{\jmath}}-g_{\imath\jmath}\mathcal{L},
$$

whose time–time component is the energy density $\tfrac12(\dot\xi^2+\sum_j(\partial_j\xi)^2+\nu_m^2\xi^2)-g\rho\xi$. The tensor is symmetric by construction, because the field is a single scalar and there is no spin part.

Why there is no vector current. A real field has no phase symmetry, so there is no conserved current of the $\mathrm{U}(1)$ kind. The corpus's charged-scalar article adds the complex structure and gets one; this article does not, and the absence is a statement about the field's reality.

Why there is no topological current. A single scalar with no winding has no topological charge. The Skyrme and gauge articles have one because their fields are group-valued; the central scalar is not.

The trace. $\sum_{\imath}\epsilon_{\imath} T_{\imath\imath}=4\pi^{2}\nu_m^2\xi^2-g\rho\xi$ up to a total derivative, nonzero for a massive field. The classical trace is the mass's measure, and the quantum trace anomaly is the quantum field theory articles'.

What there is not. **No second current, no central phase, no spin current.** The sector's current content is one tensor, and that is the minimum any relativistic field can have.

## What the Principle Adds and What It Relabels

Adds.

- *The operator's identity.* The action shows that the equation's operator is the norm of the gradient, which the equation alone states without explaining.
- *The source's sign.* The attraction of like sources is a statement about the action's sign convention, checkable from the static limit.
- *The absence of constraints as a structural fact.* The unconstrained variation is what makes the canonical treatment trivial.

Relabels.

- *The "central" of the field's name.* It is not a location; it is the statement that the operator is central and the components decouple.
- *The scalar's simplicity.* It is not a simplification of the other sectors; it is a different structure, and the difference is the missing noncentral operator.

The distinction that matters. The action is unconstrained and the operator is central. Every property of this sector follows from those two facts, and every contrast with the rest of the family follows from their absence elsewhere.

## Open Questions

Is a $\xi^4$ term the algebra's or an addition? The corpus treats the quartic scalar coupling as standard input. Whether the algebra can produce an interaction of the scalar with itself through a noncentral insertion is not established.

## Summary

The action. $S=\int d^4r\,[-\tfrac12\sum_{\imath}\partial_{\imath}\xi\partial_{\imath}\xi-\tfrac124\pi^{2}\nu_m^2\xi^2+g\rho\xi]$, whose Euler–Lagrange equation is $(\Box_\Phi-4\pi^{2}\nu_m^2)\xi=-g\rho$. The operator is the biquaternion norm of the gradient and is central.

The three findings. The action is unconstrained and the field has one degree of freedom. Centrality makes the operator act componentwise, which is why the four-component case is four decoupled scalars. The only current is the energy–momentum tensor, and the absence of a phase symmetry is the field's reality.

The boundary. The operator, the pairing and the componentwise reading are the algebra's; the quartic coupling, if used, is standard input.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\xi$ | real central scalar, $\tilde\Xi=\xi e_t$ |
| $\tilde\nabla_\Phi$, $\Box_\Phi$ | gradient and its norm, central |
| $\nu_m$ | mass |
| $g$ | source coupling |
| $\rho$ | prescribed real source density |
| $T_{\imath\jmath}$ | energy–momentum tensor |

## Further Reading

- [The Central Scalar Field: Classical Dynamics in the Biquaternion Centre](the-central-scalar-field-classical-dynamics-in-the-biquaternion-centre.html) — the parent: the Green functions, the static profile, the dynamics.
- [The Lagrangian and the Klein–Gordon Equation](the-lagrangian-and-the-klein-gordon-equation.html) — the same operator with the element's four components active.
- [The Lagrangian and the Interacting Scalar Field](the-lagrangian-and-the-interacting-scalar-field.html) — the complex scalar with a quartic coupling and a charge.
- [The Spin-Zero Centre Subspace](the-spin-zero-centre-subspace.html) — why the scalar lies outside the state module.
- [The Biquaternion d'Alembertian and Its Green Functions](the-biquaternion-dalembertian-and-its-greens-functions.html) — the operator's inverses.
